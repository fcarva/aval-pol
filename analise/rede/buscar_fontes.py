"""Busca fontes da web num ambiente com rede aberta (GitHub Actions) e grava tudo em dados/fontes_web/.

Existe porque a sessão de trabalho em nuvem só alcança o GitHub e os registros de pacotes:
Crossref, OpenAlex, SECULT, SALIC e demais fontes oficiais ficam bloqueados. O workflow
.github/workflows/buscar-fontes.yml roda este script e devolve o resultado por commit.

Entradas (editadas à mão e versionadas):
  dados/fontes_web/dois.txt        um DOI por linha → metadados da Crossref e do OpenAlex
  dados/fontes_web/pedidos.tsv     id<TAB>url<TAB>nota → página (HTML → texto; PDF → texto via pdftotext;
                                   id com prefixo raw_ grava o HTML/JS bruto, para achar endpoints de API)
  dados/fontes_web/buscas.tsv      id<TAB>consulta → busca bibliográfica na Crossref e no OpenAlex (referências sem DOI)
  dados/fontes_web/salic_anos.txt  anos AA do SALIC (ex.: 23) → roda analise/03a_salic_rouanet_uf.py
  dados/fontes_web/seguir.tsv      prefixo<TAB>url<TAB>regex<TAB>nota → baixa o índice e cada link cujo rótulo ou
                                   endereço casa com a regex (ex.: extratos das atas da CAP, ano a ano)
  dados/fontes_web/videos.tsv      id<TAB>url<TAB>nota → legenda em português do vídeo (yt-dlp), em texto com tempos
  dados/fontes_web/canais.tsv      id<TAB>url<TAB>regex<TAB>nota → lista os vídeos do canal cujo título casa

Saídas:
  dados/fontes_web/doi/<slug>.json        metadados essenciais da Crossref e do OpenAlex (com resumo)
  dados/fontes_web/doi_resumo.csv         uma linha por DOI: status nas duas bases, título, ano, periódico
  dados/fontes_web/paginas/<id>.txt       texto da página ou do PDF (o PDF em si não é versionado)
  dados/fontes_web/buscas/<id>.json       até 5 candidatos da Crossref e 5 do OpenAlex por consulta
  dados/fontes_web/seguir/<prefixo>.tsv   links do índice que casaram: rótulo, url, id, status
  dados/fontes_web/transcricoes/<id>.txt  legenda com marca de tempo, cabeçalho com título, canal, data e duração
  dados/fontes_web/videos_canal.tsv       vídeos dos canais que casaram com a regex (para a leva seguinte)
  dados/fontes_web/manifesto.csv          id, url, status HTTP, tipo, bytes, sha256, data da coleta (UTC)

Idempotente: o que já está no manifesto com status 200 não é buscado de novo (use --forcar).
Etapas: --etapa refs (DOIs e buscas), --etapa paginas, --etapa seguir, --etapa videos, --etapa canal,
--etapa salic, ou todas (padrão). O workflow
roda as etapas separadas e faz um commit depois de cada uma: página lenta ou SALIC não seguram o resto.
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
import unicodedata
from datetime import datetime, timezone
from pathlib import Path

import requests

from mascarar_cpf import mascarar  # CPF de proponente pessoa física impresso nos anexos (repositório público)

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
            r = requests.get(url, headers=UA, timeout=(15, 45), **kw)
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


def html_para_texto(html: str, base: str = "") -> str:
    """Texto da página e, no fim, a lista de links (para achar PDFs de normas na rodada seguinte)."""
    from urllib.parse import urljoin

    from bs4 import BeautifulSoup
    s = BeautifulSoup(html, "html.parser")
    links = []
    for a in s.find_all("a", href=True):
        rotulo = " ".join(a.get_text(" ").split())
        href = urljoin(base, a["href"])
        if href.startswith("http") and (rotulo, href) not in links:
            links.append((rotulo, href))
    for t in s(["script", "style", "noscript", "svg", "header", "footer", "nav"]):
        t.decompose()
    texto = re.sub(r"\n\s*\n+", "\n\n", s.get_text("\n")).strip()
    return texto + "\n\n## Links da página\n" + "\n".join(f"- [{r}]({h})" for r, h in links)


def baixar(pid: str, url: str) -> dict:
    """Baixa uma página, PDF ou .docx, grava o texto (CPF mascarado) em paginas/<pid>.txt e devolve o registro."""
    destino = PAG_DIR / f"{pid}.txt"
    r = get(url, allow_redirects=True)
    registro = {"id": pid, "url": url, "status": str(r.status_code) if r is not None else "erro",
                "coletado_utc": agora()}
    if r is not None and r.status_code == 200:
        ct = r.headers.get("content-type", "")
        registro.update(content_type=ct, bytes=str(len(r.content)), sha256=hashlib.sha256(r.content).hexdigest())
        # datas que permitem ordenar versões de um mesmo anexo (ex.: "RECURSO FINANCEIRO CAPTADO - 2025 (1..17)")
        datas = [f"# Last-Modified (servidor): {r.headers['last-modified']}"] if r.headers.get("last-modified") else []
        if "wordprocessingml" in ct.lower() or url.lower().split("?")[0].endswith(".docx"):
            texto = docx_para_texto(r.content)
        elif "pdf" in ct.lower() or url.lower().split("?")[0].endswith(".pdf"):
            tmp = Path("/tmp") / f"{pid}.pdf"
            tmp.write_bytes(r.content)
            texto = subprocess.run(["pdftotext", "-layout", str(tmp), "-"], capture_output=True,
                                   text=True).stdout
            info = subprocess.run(["pdfinfo", str(tmp)], capture_output=True, text=True).stdout
            datas += [f"# PDF {m.group(1)}: {m.group(2).strip()}"
                      for m in re.finditer(r"^(CreationDate|ModDate):\s*(.+)$", info, flags=re.M)]
        elif pid.startswith("raw_"):  # HTML ou JS bruto, para achar endpoints de API (scripts incluídos)
            r.encoding = r.encoding or r.apparent_encoding
            texto = r.text
        else:
            r.encoding = r.encoding or r.apparent_encoding
            texto = html_para_texto(r.text, r.url)
        cab = (f"# Fonte: {url}\n# Coletado (UTC): {registro['coletado_utc']}\n# sha256 do original: {registro['sha256']}\n"
               + "".join(d + "\n" for d in datas) + "\n")
        destino.write_text(cab + mascarar(texto)[0], encoding="utf-8")
        registro["arquivo"] = str(destino.relative_to(RAIZ))
    return registro


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
        ja_tem = man.get(pid, {}).get("status") == "200" and destino.exists()
        # página HTML coletada antes de o texto trazer a lista de links: coleta de novo uma vez
        sem_links = ja_tem and "pdf" not in man[pid].get("content_type", "").lower() \
            and "## Links da página" not in destino.read_text(encoding="utf-8")
        if not forcar and ja_tem and not sem_links:
            continue
        man[pid] = baixar(pid, url)
        print(f"{pid}: {man[pid]['status']}")
        time.sleep(1)


def ler_tsv(nome: str) -> list[dict]:
    arq = BASE / nome
    if not arq.exists():
        return []
    with arq.open(encoding="utf-8") as f:
        return [r for r in csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE)
                if (r.get("id") or r.get("prefixo")) and not (r.get("id") or r.get("prefixo")).startswith("#")]


def seguir_indices(man: dict, forcar: bool) -> None:
    """Baixa cada índice de seguir.tsv e, dele, todo link cujo rótulo ou endereço casa com a regex."""
    from urllib.parse import unquote, urljoin

    from bs4 import BeautifulSoup
    PAG_DIR.mkdir(parents=True, exist_ok=True)
    (BASE / "seguir").mkdir(parents=True, exist_ok=True)
    for p in ler_tsv("seguir.tsv"):
        pref, url, rx = p["prefixo"].strip(), p["url"].strip(), re.compile(p["regex"].strip())
        man[f"{pref}_indice"] = baixar(f"{pref}_indice", url)  # o índice traz as datas de atualização
        r = get(url, allow_redirects=True)
        if r is None or r.status_code != 200:
            print(f"{pref}: índice {r.status_code if r is not None else 'erro'}")
            continue
        r.encoding = r.encoding or r.apparent_encoding
        vistos, linhas = set(), []
        for a in BeautifulSoup(r.text, "html.parser").find_all("a", href=True):
            href = urljoin(r.url, a["href"])
            rotulo = " ".join(a.get_text(" ").split()) or (a.get("title") or "")
            if href in vistos or not href.startswith("http") or not (rx.search(rotulo) or rx.search(unquote(href))):
                continue
            vistos.add(href)
            nome = unquote(href.rstrip("/").split("/")[-1]).rsplit(".", 1)[0]
            nome = unicodedata.normalize("NFKD", nome).encode("ascii", "ignore").decode()
            pid = f"{pref}_{slug(nome)}"[:120].rstrip("_.-")
            destino = PAG_DIR / f"{pid}.txt"
            if forcar or man.get(pid, {}).get("status") != "200" or not destino.exists():
                man[pid] = baixar(pid, href)
                time.sleep(1)
            linhas.append({"rotulo": rotulo, "url": href, "id": pid, "status": man[pid]["status"]})
        with (BASE / "seguir" / f"{pref}.tsv").open("w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=["rotulo", "url", "id", "status"], delimiter="\t")
            w.writeheader()
            w.writerows(linhas)
        print(f"{pref}: {len(linhas)} links; {sum(l['status'] == '200' for l in linhas)} com 200")


def vtt_para_texto(vtt: str) -> str:
    """Legenda .vtt em linhas "[hh:mm:ss] fala", sem as repetições da legenda rolante do YouTube."""
    saida, anterior = [], ""
    for bloco in re.split(r"\n\s*\n", vtt):
        linhas = bloco.splitlines()
        i = next((k for k, l in enumerate(linhas) if "-->" in l), None)
        if i is None:
            continue
        inicio = linhas[i].split(".")[0].strip()
        for fala in (re.sub(r"<[^>]+>", "", l).strip() for l in linhas[i + 1:]):
            if fala and fala != anterior:
                saida.append(f"[{inicio}] {fala}")
                anterior = fala
    # a legenda automática repete a linha anterior no bloco seguinte: fica só a primeira ocorrência
    vistos, limpo = set(), []
    for l in saida:
        fala = l.split("] ", 1)[1]
        if fala not in vistos:
            limpo.append(l)
        vistos = {fala} | (vistos if len(vistos) < 3 else set())
    return "\n".join(limpo)


def buscar_videos(man: dict, forcar: bool) -> None:
    """Legenda em português (manual, se houver; senão automática) de cada vídeo de videos.tsv, via yt-dlp."""
    destino_dir, tmp = BASE / "transcricoes", Path("/tmp/yt")
    destino_dir.mkdir(parents=True, exist_ok=True)
    tmp.mkdir(parents=True, exist_ok=True)
    for p in ler_tsv("videos.tsv"):
        vid, url = p["id"].strip(), p["url"].strip()
        chave, destino = f"video:{vid}", destino_dir / f"{vid}.txt"
        if not forcar and man.get(chave, {}).get("status") == "200" and destino.exists():
            continue
        registro = {"id": chave, "url": url, "status": "erro", "coletado_utc": agora()}
        erro = ""
        for extra in ([], ["--extractor-args", "youtube:player_client=tv,web_safari,mweb"]):
            cmd = ["yt-dlp", "--skip-download", "--write-info-json", "--write-subs", "--write-auto-subs",
                   "--sub-langs", "pt-BR,pt,pt-orig,pt.*", "--sub-format", "vtt", "--no-progress",
                   "-o", str(tmp / "%(id)s.%(ext)s"), *extra, url]
            proc = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            legendas = sorted(tmp.glob(f"{vid}*.vtt"))
            if legendas:
                break
            erro = (proc.stderr.strip().splitlines() or ["sem legenda em português"])[-1][:300]
        info_arq = tmp / f"{vid}.info.json"
        info = json.loads(info_arq.read_text(encoding="utf-8")) if info_arq.exists() else {}
        if legendas:
            manual = set(info.get("subtitles") or {})
            # preferência: legenda manual em português; depois a automática no idioma original
            legendas.sort(key=lambda a: (a.name.split(".")[-2] not in manual, "orig" not in a.name))
            leg = legendas[0]
            lang = leg.name.split(".")[-2]
            bruto = leg.read_bytes()
            texto = vtt_para_texto(bruto.decode("utf-8", "replace"))
            cab = "\n".join([
                f"# Fonte: {url}", f"# Título: {info.get('title', '')}", f"# Canal: {info.get('channel') or info.get('uploader', '')}",
                f"# Data de publicação: {info.get('upload_date', '')}", f"# Duração (s): {info.get('duration', '')}",
                f"# Legenda: {lang}; automática: {'não' if lang in manual else 'sim'}",
                f"# Coletado (UTC): {registro['coletado_utc']}", f"# sha256 da legenda .vtt: {hashlib.sha256(bruto).hexdigest()}",
                f"# Nota: {p.get('nota', '')}", "", ""])
            destino.write_text(cab + mascarar(texto)[0] + "\n", encoding="utf-8")
            registro.update(status="200", content_type="text/vtt", bytes=str(len(bruto)),
                            sha256=hashlib.sha256(bruto).hexdigest(), arquivo=str(destino.relative_to(RAIZ)))
        else:
            registro["status"] = f"erro: {erro}"
        man[chave] = registro
        print(f"{chave}: {registro['status']}")
        time.sleep(2)


def listar_canais() -> None:
    """Lista os vídeos e transmissões de cada canal de canais.tsv cujo título casa com a regex."""
    linhas = []
    for p in ler_tsv("canais.tsv"):
        cid, base, rx = p["id"].strip(), p["url"].strip().rstrip("/"), re.compile(p["regex"].strip())
        for aba in ("videos", "streams"):
            proc = subprocess.run(["yt-dlp", "--flat-playlist", "--ignore-errors", "--print",
                                   "%(id)s\t%(title)s\t%(upload_date)s\t%(duration)s", f"{base}/{aba}"],
                                  capture_output=True, text=True, timeout=900)
            n = 0
            for l in proc.stdout.splitlines():
                partes = l.split("\t")
                if len(partes) == 4 and rx.search(partes[1]):
                    linhas.append({"canal": cid, "aba": aba, "id": partes[0], "titulo": partes[1],
                                   "data": partes[2], "duracao_s": partes[3],
                                   "url": f"https://www.youtube.com/watch?v={partes[0]}"})
                n += 1
            print(f"{cid}/{aba}: {n} vídeos listados; erro: {proc.stderr.strip().splitlines()[-1:] }")
    with (BASE / "videos_canal.tsv").open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["canal", "aba", "id", "titulo", "data", "duracao_s", "url"], delimiter="\t")
        w.writeheader()
        w.writerows(linhas)
    print(f"canais: {len(linhas)} vídeos com título relevante")


def docx_para_texto(conteudo: bytes) -> str:
    """Texto de um .docx sem dependência externa: parágrafos em linhas; células de tabela separadas por " | "."""
    import io
    import re
    import zipfile
    with zipfile.ZipFile(io.BytesIO(conteudo)) as z:
        xml = z.read("word/document.xml").decode("utf-8", "replace")
    xml = re.sub(r"</w:tc>", " | ", xml)
    xml = re.sub(r"</w:p>|</w:tr>", "\n", xml)
    xml = re.sub(r"<w:tab/>", "\t", xml)
    texto = re.sub(r"<[^>]+>", "", xml)
    for ent, car in (("&amp;", "&"), ("&lt;", "<"), ("&gt;", ">"), ("&quot;", '"'), ("&apos;", "'")):
        texto = texto.replace(ent, car)
    return "\n".join(l.rstrip() for l in texto.splitlines() if l.strip())


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
    if etapa in ("paginas", "tudo"):
        man = ler_manifesto()
        buscar_paginas(man, forcar)
        gravar_manifesto(man)
    if etapa in ("seguir", "tudo"):
        man = ler_manifesto()
        seguir_indices(man, forcar)
        gravar_manifesto(man)
    if etapa in ("videos", "tudo"):
        man = ler_manifesto()
        buscar_videos(man, forcar)
        gravar_manifesto(man)
    if etapa in ("canal", "tudo"):
        listar_canais()
    if etapa in ("salic", "tudo"):
        rodar_salic()


if __name__ == "__main__":
    main()
