"""Confere as referências do artigo com os metadados da Crossref e do OpenAlex (auditoria ARS, Fase A).

Lê a lista de referências de artigo/rascunho-artigo.md e, para cada uma com DOI, o JSON coletado pelo
relé (dados/fontes_web/doi/<slug>.json). Compara, item a item: sobrenomes dos autores, título, periódico,
ano, volume, número e páginas. Referências sem DOI ficam "sem_doi" e são conferidas à mão no relatório
(buscas em dados/fontes_web/buscas/, páginas em dados/fontes_web/paginas/, normas em notas/politica/fontes/).

Saída: artigo/auditoria/checagem_referencias.csv
Uso:   python artigo/auditoria/checar_referencias.py
"""
from __future__ import annotations

import csv
import html
import json
import re
import sys
import unicodedata
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
ART = RAIZ / "artigo" / "rascunho-artigo.md"
DOI_DIR = RAIZ / "dados" / "fontes_web" / "doi"
SAIDA = Path(__file__).with_name("checagem_referencias.csv")


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s or "")
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()


def slug(doi: str) -> str:
    return re.sub(r"[^A-Za-z0-9._-]+", "_", doi.lower())


def referencias() -> list[str]:
    texto = ART.read_text(encoding="utf-8")
    bloco = texto.split("# Referências", 1)[1].split("\n# ", 1)[0]
    return [p.strip() for p in bloco.split("\n\n") if p.strip()]


def campo(ref: str, padrao: str) -> str:
    m = re.search(padrao, ref)
    return m.group(1) if m else ""


def conferir(ref: str) -> dict:
    doi = campo(ref, r"DOI: (10\.\S+?)\.?$")
    linha = {"referencia": ref[:90], "doi": doi}
    if not doi:
        linha["status"] = "sem_doi"
        return linha
    arq = DOI_DIR / f"{slug(doi)}.json"
    if not arq.exists():
        linha["status"] = "doi_nao_coletado"
        return linha
    d = json.loads(arq.read_text(encoding="utf-8"))
    cr, oa = d.get("crossref") or {}, d.get("openalex") or {}
    if not cr and not oa:
        linha["status"] = "NOT_FOUND (Crossref e OpenAlex)"
        return linha
    problemas = []
    autores_ref = norm(ref.split(". ", 1)[0] if "**" not in ref.split(". ", 1)[0] else ref)
    familias = [a.get("family") or a.get("name") or "" for a in cr.get("author", [])] if cr else \
        [n.split()[-1] for n in oa.get("authorships", []) if n]
    toks = set(norm(ref).split())
    faltam = [f for f in familias if f and not all(t in toks for t in norm(f).split())]
    if faltam:
        problemas.append("autor(es) da fonte ausentes na referência: " + ", ".join(faltam))
    titulo = html.unescape((cr.get("title") or [oa.get("title") or ""])[0] if cr.get("title") else (oa.get("title") or ""))
    t_fonte = norm(re.sub(r"<[^>]+>", "", titulo))
    t_ref = norm(ref)
    palavras = [w for w in t_fonte.split() if len(w) > 3]
    presentes = sum(w in t_ref.split() for w in palavras)
    if palavras and presentes / len(palavras) < 0.8:
        problemas.append(f"título difere da fonte: «{titulo}»")
    ano_fonte = None
    for chave in ("published_print", "issued", "published_online"):
        partes = cr.get(chave)
        if partes and partes[0] and partes[0][0]:
            ano_fonte = partes[0][0]
            break
    ano_fonte = ano_fonte or oa.get("publication_year")
    ano_ref = campo(ref, r", (\d{4})\. DOI") or campo(ref, r", (\d{4})\.")
    if ano_fonte and ano_ref and int(ano_ref) != int(ano_fonte):
        anos = {p[0][0] for k in ("issued", "published_print", "published_online") if (p := cr.get(k)) and p[0]}
        if int(ano_ref) not in anos:
            problemas.append(f"ano: referência {ano_ref}, fonte {sorted(anos) or ano_fonte}")
    bib = oa.get("biblio") or {}
    for rot, pad, fonte in (("volume", r", v\. (\w+)", cr.get("volume") or bib.get("volume")),
                            ("número", r", n\. (\w+)", cr.get("issue") or bib.get("issue"))):
        valor = campo(ref, pad)
        if fonte and valor and norm(str(valor)) != norm(str(fonte)):
            problemas.append(f"{rot}: referência {valor}, fonte {fonte}")
        if fonte and not valor:
            problemas.append(f"{rot} ausente na referência (fonte: {fonte})")
    pag_ref = campo(ref, r"p\. (\d+[-–]\d+)")
    pag_fonte = cr.get("page") or (f"{bib.get('first_page')}-{bib.get('last_page')}" if bib.get("first_page") else "")
    if pag_fonte and pag_ref and norm(pag_ref) != norm(pag_fonte):
        problemas.append(f"páginas: referência {pag_ref}, fonte {pag_fonte}")
    periodico = html.unescape((cr.get("container_title") or [oa.get("source") or ""])[0] if cr.get("container_title") else (oa.get("source") or ""))
    per_ref = campo(ref, r"\*\*(.+?)\*\*")
    if periodico and per_ref and norm(periodico) != norm(per_ref) and norm(periodico) not in norm(ref):
        problemas.append(f"periódico: referência «{per_ref}», fonte «{periodico}»")
    linha.update(status="VERIFIED" if not problemas else "CONFERIR", problemas=" | ".join(problemas),
                 titulo_fonte=titulo, periodico_fonte=periodico, ano_fonte=ano_fonte,
                 fonte="Crossref" if cr else "OpenAlex")
    return linha


def chave(ref: str) -> tuple[str, str]:
    """(sobrenome ou entidade do primeiro autor, ano com sufixo) de uma referência."""
    autor = re.split(r"[,.(–]", ref, 1)[0].strip()
    autor = {"SECULT": "SECULT", "ESPÍRITO SANTO": "ESPÍRITO SANTO"}.get(autor, autor)
    base = re.split(r"Disponível em|DOI:|Acesso em|Dados consultados|Base de dados", ref)[0]
    anos = re.findall(r"(\[20\d-\]|\b(?:19|20)\d\d[a-z]?\b)", base)
    ano = next((a for a in anos if re.search(r"(?:19|20)\d\d[a-z]$|\[", a)), None) or (anos[-1] if anos else "")
    return norm(autor), ano


def cruzamento() -> list[str]:
    """Citação sem referência e referência sem citação (sobrenome do 1º autor + ano)."""
    texto = ART.read_text(encoding="utf-8")
    corpo = texto.split("# Referências", 1)[0]
    problemas = []
    for ref in referencias():
        autor, ano = chave(ref)
        ano_base = re.sub(r"[a-z]$", "", ano)
        ano_corpo = ano if ano.startswith("[") else ano_base
        padrao = re.escape(ano) if re.search(r"[a-z]$|\[", ano) else re.escape(ano_base)
        achou = any(norm(autor) in norm(corpo[max(0, m.start() - 120):m.end()])
                    for m in re.finditer(padrao, corpo))
        if not achou and ano and re.search(r"[a-z]$", ano):
            # "2021a; 2021b" e "(ESPÍRITO SANTO, 2021a; 2021b)": o sufixo pode vir isolado
            achou = any(norm(autor) in norm(corpo[max(0, m.start() - 200):m.end()])
                        for m in re.finditer(re.escape(ano_base) + ano[-1], corpo))
        if not achou:
            problemas.append(f"referência sem citação no texto: {autor.upper()} ({ano_corpo})")
    return problemas


def main() -> int:
    for p in cruzamento():
        print("[CRUZAMENTO]", p)
    linhas = [conferir(r) for r in referencias()]
    campos = ["status", "doi", "referencia", "problemas", "titulo_fonte", "periodico_fonte", "ano_fonte", "fonte"]
    with SAIDA.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=campos, extrasaction="ignore")
        w.writeheader()
        w.writerows(linhas)
    for l in linhas:
        if l["status"] != "VERIFIED":
            print(f"[{l['status']}] {l['referencia'][:70]} {l.get('problemas', '')}")
    n = sum(l["status"] == "VERIFIED" for l in linhas)
    print(f"{len(linhas)} referências; {n} com DOI conferido sem divergência → {SAIDA.relative_to(RAIZ)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
