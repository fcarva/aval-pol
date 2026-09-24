"""Busca fontes da web num ambiente com rede aberta (GitHub Actions) e grava tudo em dados/fontes_web/.

Existe porque a sessão de trabalho em nuvem só alcança o GitHub e os registros de pacotes:
Crossref, OpenAlex, SECULT, SALIC e demais fontes oficiais ficam bloqueados. O workflow
.github/workflows/buscar-fontes.yml roda este script e devolve o resultado por commit.

Entradas (editadas à mão e versionadas):
  dados/fontes_web/dois.txt        um DOI por linha → metadados da Crossref e do OpenAlex
  dados/fontes_web/pedidos.tsv     id<TAB>url<TAB>nota → página (HTML → texto; PDF → texto via pdftotext)
  dados/fontes_web/buscas.tsv      id<TAB>consulta → busca bibliográfica na Crossref e no OpenAlex (referências sem DOI)
  dados/fontes_web/salic_anos.txt  anos AA do SALIC (ex.: 23) → roda analise/03a_salic_rouanet_uf.py

Saídas:
  dados/fontes_web/doi/<slug>.json        metadados essenciais da Crossref e do OpenAlex (com resumo)
  dados/fontes_web/doi_resumo.csv         uma linha por DOI: status nas duas bases, título, ano, periódico
  dados/fontes_web/paginas/<id>.txt       texto da página ou do PDF (o PDF em si não é versionado)
  dados/fontes_web/buscas/<id>.json       até 5 candidatos da Crossref e 5 do OpenAlex por consulta
  dados/fontes_web/manifesto.csv          id, url, status HTTP, tipo, bytes, sha256, data da coleta (UTC)

Idempotente: o que já está no manifesto com status 200 não é buscado de novo (use --forcar).
Etapas: --etapa refs (DOIs, buscas e páginas), --etapa salic, ou as duas (padrão). O workflow roda
as etapas separadas e faz um commit depois de cada uma, para o SALIC (lento) não segurar o resto.
Não envia e-mail nem identificação pessoal às APIs; o User-Agent aponta para o repositório.
"""
from __future__ import annotations

import csv
import hashlib
import json
import re
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import requests

RAIZ = Path(__file__).resolve().parents[2]
BASE = RAIZ / "dados" / "fontes_web"
DOI_DIR = BASE / "doi"
PAG_DIR = BASE / "paginas"
MANIFESTO = BASE / "manifesto.csv"
UA = {"User-Agent": "aval-pol/1.0 (+https://github.com/fcarva/aval-pol; verificacao de referencias academicas)"}
CAMPOS_MANIFESTO = ["id", "url", "status", "content_type", "bytes", "sha256", "coletado_utc", "arquivo"]


def agora() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def slug(doi: str) -> str:
    return re.sub(r"[^A-Za-z0-9._-]+", "_", doi.lower())


def ler_manifesto() -> dict[str, dict]:
    if not MANIFESTO.exists():
        return {}
    with MANIFESTO.open(encoding="utf-8") as f:
        return {r["id"]: r for r in csv.DictReader(f)}


def gravar_manifesto(m: dict[str, dict]) -> None:
    with MANIFESTO.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=CAMPOS_MANIFESTO)
        w.writeheader()
        for k in sorted(m):
            w.writerow({c: m[k].get(c, "") for c in CAMPOS_MANIFESTO})


def get(url: str, **kw) -> requests.Response | None:
    for tent in range(3):
        try:
            r = requests.get(url, headers=UA, timeout=60, **kw)
            if r.status_code in (429, 502, 503, 504):
                time.sleep(5 * (tent + 1))
                continue
            return r
        except requests.RequestException:
            time.sleep(5 * (tent + 1))
    return None


def resumo_openalex(inv: dict | None) -> str:
    if not inv:
        return ""
    pos = {}
    for palavra, idx in inv.items():
        for i in idx:
            pos[i] = palavra
    return " ".join(pos[i] for i in sorted(pos))


def buscar_dois(man: dict, forcar: bool) -> None:
    arq = BASE / "dois.txt"
    if not arq.exists():
        return
    DOI_DIR.mkdir(parents=True, exist_ok=True)
    dois = [l.strip() for l in arq.read_text(encoding="utf-8").splitlines() if l.strip() and not l.startswith("#")]
    linhas = []
    for doi in dois:
        chave = f"doi:{doi}"
        destino = DOI_DIR / f"{slug(doi)}.json"
        if not forcar and man.get(chave, {}).get("status") == "200" and destino.exists():
            dados = json.loads(destino.read_text(encoding="utf-8"))
        else:
            dados = {"doi": doi, "coletado_utc": agora()}
            rc = get(f"https://api.crossref.org/works/{requests.utils.quote(doi, safe='/()')}")
            dados["crossref_status"] = rc.status_code if rc is not None else None
            if rc is not None and rc.status_code == 200:
                msg = rc.json().get("message", {})
                dados["crossref"] = {
                    "title": msg.get("title"), "subtitle": msg.get("subtitle"),
                    "author": [{"given": a.get("given"), "family": a.get("family"), "name": a.get("name")}
                               for a in msg.get("author", [])],
                    "container_title": msg.get("container-title"), "publisher": msg.get("publisher"),
                    "type": msg.get("type"), "volume": msg.get("volume"), "issue": msg.get("issue"),
                    "page": msg.get("page"), "article_number": msg.get("article-number"),
                    "issued": msg.get("issued", {}).get("date-parts"),
                    "published_print": msg.get("published-print", {}).get("date-parts"),
                    "published_online": msg.get("published-online", {}).get("date-parts"),
                    "isbn": msg.get("ISBN"), "url": msg.get("URL"),
                    "abstract": msg.get("abstract"),
                }
            ro = get(f"https://api.openalex.org/works/doi:{doi}")
            dados["openalex_status"] = ro.status_code if ro is not None else None
            if ro is not None and ro.status_code == 200:
                w = ro.json()
                loc = (w.get("primary_location") or {})
                dados["openalex"] = {
                    "id": w.get("id"), "title": w.get("title"), "publication_year": w.get("publication_year"),
                    "type": w.get("type"), "source": (loc.get("source") or {}).get("display_name"),
                    "landing_page_url": loc.get("landing_page_url"),
                    "authorships": [a.get("author", {}).get("display_name") for a in w.get("authorships", [])],
                    "biblio": w.get("biblio"), "cited_by_count": w.get("cited_by_count"),
                    "abstract": resumo_openalex(w.get("abstract_inverted_index")),
                }
            texto = json.dumps(dados, ensure_ascii=False, indent=1)
            destino.write_text(texto, encoding="utf-8")
            man[chave] = {"id": chave, "url": f"https://api.crossref.org/works/{doi}",
                          "status": str(dados["crossref_status"] or dados["openalex_status"] or ""),
                          "content_type": "application/json", "bytes": str(len(texto.encode())),
                          "sha256": hashlib.sha256(texto.encode()).hexdigest(), "coletado_utc": dados["coletado_utc"],
                          "arquivo": str(destino.relative_to(RAIZ))}
            time.sleep(0.3)
        cr, oa = dados.get("crossref") or {}, dados.get("openalex") or {}
        linhas.append({
            "doi": doi, "crossref_status": dados.get("crossref_status"), "openalex_status": dados.get("openalex_status"),
            "titulo": (cr.get("title") or [oa.get("title") or ""])[0] if cr.get("title") else oa.get("title") or "",
            "ano": (cr.get("issued") or [[None]])[0][0] if cr.get("issued") else oa.get("publication_year"),
            "periodico": (cr.get("container_title") or [""])[0] if cr.get("container_title") else oa.get("source") or "",
            "volume": cr.get("volume") or (oa.get("biblio") or {}).get("volume") or "",
            "numero": cr.get("issue") or (oa.get("biblio") or {}).get("issue") or "",
            "paginas": cr.get("page") or "",
            "autores": "; ".join(filter(None, [a.get("family") or a.get("name") for a in cr.get("author", [])]))
                       or "; ".join(filter(None, oa.get("authorships") or [])),
            "tem_resumo": bool(cr.get("abstract") or oa.get("abstract")),
        })
    with (BASE / "doi_resumo.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(linhas[0].keys()) if linhas else ["doi"])
        w.writeheader()
        w.writerows(linhas)
    print(f"DOIs: {len(linhas)}; Crossref 200: {sum(l['crossref_status'] == 200 for l in linhas)}; "
          f"OpenAlex 200: {sum(l['openalex_status'] == 200 for l in linhas)}")


def buscar_bibliografia(man: dict, forcar: bool) -> None:
    arq = BASE / "buscas.tsv"
    if not arq.exists():
        return
    destino_dir = BASE / "buscas"
    destino_dir.mkdir(parents=True, exist_ok=True)
    with arq.open(encoding="utf-8") as f:
        pedidos = [r for r in csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE) if r.get("id") and not r["id"].startswith("#")]
    for p in pedidos:
        bid, consulta = p["id"].strip(), p["consulta"].strip()
        chave, destino = f"busca:{bid}", destino_dir / f"{bid}.json"
        if not forcar and man.get(chave, {}).get("status") == "200" and destino.exists():
            continue
        dados = {"id": bid, "consulta": consulta, "coletado_utc": agora(), "crossref": [], "openalex": []}
        rc = get("https://api.crossref.org/works", params={"query.bibliographic": consulta, "rows": 5})
        dados["crossref_status"] = rc.status_code if rc is not None else None
        if rc is not None and rc.status_code == 200:
            for it in rc.json().get("message", {}).get("items", []):
                dados["crossref"].append({
                    "doi": it.get("DOI"), "title": it.get("title"), "type": it.get("type"),
                    "author": [a.get("family") or a.get("name") for a in it.get("author", [])],
                    "container_title": it.get("container-title"), "publisher": it.get("publisher"),
                    "issued": it.get("issued", {}).get("date-parts"), "volume": it.get("volume"),
                    "issue": it.get("issue"), "page": it.get("page"), "isbn": it.get("ISBN"),
                    "score": it.get("score")})
        ro = get("https://api.openalex.org/works", params={"search": consulta, "per-page": 5})
        dados["openalex_status"] = ro.status_code if ro is not None else None
        if ro is not None and ro.status_code == 200:
            for w in ro.json().get("results", []):
                loc = (w.get("primary_location") or {})
                dados["openalex"].append({
                    "id": w.get("id"), "doi": w.get("doi"), "title": w.get("title"),
                    "publication_year": w.get("publication_year"), "type": w.get("type"),
                    "source": (loc.get("source") or {}).get("display_name"),
                    "authorships": [a.get("author", {}).get("display_name") for a in w.get("authorships", [])],
                    "biblio": w.get("biblio"), "abstract": resumo_openalex(w.get("abstract_inverted_index"))})
        texto = json.dumps(dados, ensure_ascii=False, indent=1)
        destino.write_text(texto, encoding="utf-8")
        man[chave] = {"id": chave, "url": consulta, "status": str(dados["crossref_status"] or dados["openalex_status"] or ""),
                      "content_type": "application/json", "bytes": str(len(texto.encode())),
                      "sha256": hashlib.sha256(texto.encode()).hexdigest(), "coletado_utc": dados["coletado_utc"],
                      "arquivo": str(destino.relative_to(RAIZ))}
        print(f"{chave}: crossref {dados['crossref_status']}, openalex {dados['openalex_status']}")
        time.sleep(0.5)


def html_para_texto(html: str) -> str:
    from bs4 import BeautifulSoup
    s = BeautifulSoup(html, "html.parser")
    for t in s(["script", "style", "noscript", "svg", "header", "footer", "nav"]):
        t.decompose()
    texto = s.get_text("\n")
    return re.sub(r"\n\s*\n+", "\n\n", texto).strip()


def buscar_paginas(man: dict, forcar: bool) -> None:
    arq = BASE / "pedidos.tsv"
    if not arq.exists():
        return
    PAG_DIR.mkdir(parents=True, exist_ok=True)
    with arq.open(encoding="utf-8") as f:
        pedidos = [r for r in csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE) if r.get("id") and not r["id"].startswith("#")]
    for p in pedidos:
        pid, url = p["id"].strip(), p["url"].strip()
        destino = PAG_DIR / f"{pid}.txt"
        if not forcar and man.get(pid, {}).get("status") == "200" and destino.exists():
            continue
        r = get(url, allow_redirects=True)
        registro = {"id": pid, "url": url, "status": str(r.status_code) if r is not None else "erro",
                    "coletado_utc": agora()}
        if r is not None and r.status_code == 200:
            ct = r.headers.get("content-type", "")
            registro.update(content_type=ct, bytes=str(len(r.content)), sha256=hashlib.sha256(r.content).hexdigest())
            if "pdf" in ct.lower() or url.lower().endswith(".pdf"):
                tmp = Path("/tmp") / f"{pid}.pdf"
                tmp.write_bytes(r.content)
                texto = subprocess.run(["pdftotext", "-layout", str(tmp), "-"], capture_output=True,
                                       text=True).stdout
            else:
                r.encoding = r.encoding or r.apparent_encoding
                texto = html_para_texto(r.text)
            cab = f"# Fonte: {url}\n# Coletado (UTC): {registro['coletado_utc']}\n# sha256 do original: {registro['sha256']}\n\n"
            destino.write_text(cab + texto, encoding="utf-8")
            registro["arquivo"] = str(destino.relative_to(RAIZ))
        man[pid] = registro
        print(f"{pid}: {registro['status']}")
        time.sleep(1)


def rodar_salic() -> None:
    arq = BASE / "salic_anos.txt"
    if not arq.exists():
        return
    anos = [a.strip() for a in arq.read_text().split() if a.strip().isdigit()]
    if anos:
        subprocess.run([sys.executable, str(RAIZ / "analise" / "03a_salic_rouanet_uf.py"), *anos], check=True)


def main() -> None:
    forcar = "--forcar" in sys.argv
    etapa = sys.argv[sys.argv.index("--etapa") + 1] if "--etapa" in sys.argv else "tudo"
    BASE.mkdir(parents=True, exist_ok=True)
    if etapa in ("refs", "tudo"):
        man = ler_manifesto()
        buscar_dois(man, forcar)
        gravar_manifesto(man)
        buscar_bibliografia(man, forcar)
        gravar_manifesto(man)
        buscar_paginas(man, forcar)
        gravar_manifesto(man)
    if etapa in ("salic", "tudo"):
        rodar_salic()


if __name__ == "__main__":
    main()
