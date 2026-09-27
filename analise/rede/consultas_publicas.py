"""Consultas a bases públicas que não pedem LAI, rodadas no relé (GitHub Actions, rede aberta).

1. CNPJ dos patrocinadores (BrasilAPI; se falhar, minhareceita.org): porte, natureza jurídica, atividade (CNAE),
   município, capital social, data de abertura e opção pelo Simples. Os CNPJs saem dos anexos "Recurso financeiro
   captado" de 2022 a 2026 e das versões antigas coletadas (dados/fontes_web/paginas/). O quadro de sócios não é
   gravado.
   Também os CNPJs dos proponentes que captaram na LICC (2022-2025), lidos das listas de projetos beneficiados do
   Portal da Transparência (dados/processados/transparencia_licc_termos.csv, analise/16_transparencia_licc.py):
   natureza jurídica, abertura, atividade, porte e sede.
2. Mapa Cultural: agentes, projetos e eventos, lidos por inteiro pela API pública, mas gravados só quando o nome
   normalizado coincide EXATAMENTE com um proponente ou um título de projeto da LICC (dados/processados/
   habilitados.csv). Sem semelhança aproximada, e sem gravar dados de quem não é proponente (LGPD).
3. Diário Oficial do ES (IOES): busca em texto pela rota pública da plataforma (Elasticsearch cru,
   /busca/busca/buscar/query/<página>/di:<início>/df:<fim>/?q="termo", paginação a partir de zero), para os atos da LICC:
   portarias do montante, designação da CAP, avisos de habilitação e resultados. Grava só o trecho em volta do termo,
   com CPF mascarado; o texto da página inteira (outros atos, outras pessoas) não é gravado.
4. Portal da Transparência, "Incentivos vigentes" e "Relação de beneficiários e valores renunciados" (2022-2025, CSV,
   valores da EFD não necessariamente auditados pela SEFAZ): só as linhas da LICC são gravadas; do resto, só o
   cabeçalho, a contagem de linhas e os rótulos de benefício (diagnóstico), sem dado de contribuinte.

Saídas (dados/externos/):
  cnpj_patrocinadores.csv          uma linha por CNPJ de patrocinador
  cnpj_proponentes.csv             uma linha por CNPJ de proponente que captou (Portal da Transparência, DV válido)
  mapa_agentes_proponentes.csv     agentes do Mapa cujo nome casa com um proponente (área de atuação, município, tipo)
  mapa_projetos_licc.csv           projetos do Mapa cujo nome casa com um título da LICC
  mapa_eventos_licc.csv            eventos do Mapa cujo nome, ou o do projeto, casa com um título da LICC
  mapa_casamento_resumo.csv        quantos registros foram lidos e quantos casaram, por entidade
  dio_licc_trechos.csv             um trecho por ocorrência do termo no DIO: data, diário, página, termo, trecho
  dio_licc_diagnostico.txt         rotas e formatos de data tentados, com status e início da resposta
  transparencia_beneficiarios_licc.csv   linhas da LICC nos incentivos vigentes; nas relações de beneficiários, as
                                         linhas dos patrocinadores da LICC (renúncia total, todos os incentivos)
  transparencia_beneficiarios_diagnostico.txt  por arquivo: status, codificação, separador, cabeçalho, linhas, rótulos
Uso: python analise/rede/consultas_publicas.py [--so cnpj|proponentes|mapa|dio|beneficiarios]
"""
from __future__ import annotations

import csv
import importlib.util
import json
import re
import sys
import time
import unicodedata
from pathlib import Path

import pandas as pd
import requests

RAIZ = Path(__file__).resolve().parents[2]
PAG = RAIZ / "dados" / "fontes_web" / "paginas"
EXT = RAIZ / "dados" / "externos"
UA = {"User-Agent": "aval-pol/1.0 (+https://github.com/fcarva/aval-pol; pesquisa academica)"}
MAPA = "https://mapa.cultura.es.gov.br/api"

_spec = importlib.util.spec_from_file_location("carregar", RAIZ / "analise" / "01_carregar.py")
carregar = importlib.util.module_from_spec(_spec)
sys.path.insert(0, str(RAIZ / "analise"))
_spec.loader.exec_module(carregar)

CNPJ = re.compile(r"(\d{2})[.\s-]?(\d{3})[.\s-]?(\d{3})\s*[./-]?\s*(\d{4})\s*[-/.]?\s*(\d{2})")
CAMPOS_CNPJ = ["cnpj", "razao_social", "nome_fantasia", "porte", "natureza_juridica", "cnae_fiscal",
               "cnae_fiscal_descricao", "municipio", "uf", "capital_social", "data_inicio_atividade",
               "descricao_situacao_cadastral", "opcao_pelo_simples", "data_opcao_pelo_simples",
               "data_exclusao_do_simples", "opcao_pelo_mei", "fonte", "consultado_utc"]


def get_json(url: str, **kw):
    for tent in range(3):
        try:
            r = requests.get(url, headers=UA, timeout=(15, 60), **kw)
            if r.status_code == 200:
                return r.json()
            if r.status_code in (429, 502, 503, 504):
                time.sleep(5 * (tent + 1))
                continue
            return None
        except (requests.RequestException, json.JSONDecodeError):
            time.sleep(5 * (tent + 1))
    return None


def dv_cnpj_ok(c: str) -> bool:
    if len(c) != 14 or len(set(c)) == 1:
        return False
    def dv(base: str, pesos: list[int]) -> str:
        s = sum(int(d) * p for d, p in zip(base, pesos)) % 11
        return "0" if s < 2 else str(11 - s)
    p1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    return c[12] == dv(c[:12], p1) and c[13] == dv(c[:13], [6] + p1)


def cnpjs_patrocinadores() -> list[str]:
    achados = set()
    for arq in list(PAG.glob("secult_captados_*.txt")) + list(PAG.glob("versao_captados_*.txt")):
        for m in CNPJ.finditer(arq.read_text(encoding="utf-8")):
            c = "".join(m.groups())
            if dv_cnpj_ok(c):
                achados.add(c)
    return sorted(achados)


def cnpjs_proponentes() -> list[str]:
    arq = RAIZ / "dados" / "processados" / "transparencia_licc_termos.csv"
    if not arq.exists():
        return []
    t = pd.read_csv(arq, dtype=str)
    return sorted({c for c in t["cnpj_proponente"].dropna() if re.fullmatch(r"\d{14}", c) and dv_cnpj_ok(c)})


def consultar_cnpjs(cnpjs: list[str] | None = None, nome: str = "cnpj_patrocinadores.csv") -> None:
    EXT.mkdir(parents=True, exist_ok=True)
    destino = EXT / nome
    cnpjs = cnpjs_patrocinadores() if cnpjs is None else cnpjs
    feitos = {}
    if destino.exists():
        feitos = {r["cnpj"]: r for r in csv.DictReader(destino.open(encoding="utf-8")) if r.get("razao_social")}
    linhas = []
    for c in cnpjs:
        if c in feitos:
            linhas.append(feitos[c])
            continue
        d, fonte = get_json(f"https://brasilapi.com.br/api/cnpj/v1/{c}"), "brasilapi"
        if not d:
            d, fonte = get_json(f"https://minhareceita.org/{c}"), "minhareceita"
        linha = {k: (d or {}).get(k, "") for k in CAMPOS_CNPJ}
        # razão social de MEI traz o CPF do titular: mascarado antes de gravar (repositório público)
        sys.path.insert(0, str(RAIZ / "analise" / "rede"))
        from mascarar_cpf import mascarar
        for k in ("razao_social", "nome_fantasia"):
            linha[k] = mascarar(str(linha[k] or ""))[0]
        linha.update(cnpj=c, fonte=fonte if d else "sem resposta",
                     consultado_utc=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()))
        linhas.append(linha)
        time.sleep(1.2)
    with destino.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=CAMPOS_CNPJ)
        w.writeheader()
        w.writerows(linhas)
    print(f"{nome}: {len(linhas)} CNPJs; com resposta: {sum(bool(l['razao_social']) for l in linhas)}")


def paginar(entidade: str, select: str, limite: int = 1000, maximo: int = 100):
    """Todas as páginas de /api/{entidade}/find; se o @select falhar, devolve None na primeira página."""
    for pagina in range(1, maximo + 1):
        d = get_json(f"{MAPA}/{entidade}/find", params={"@select": select, "@limit": limite, "@page": pagina,
                                                         "@order": "id ASC"})
        if not isinstance(d, list):
            yield None
            return
        if not d:
            return
        yield from d
        time.sleep(0.5)


def chave_titulo(s) -> str:
    return " ".join(re.sub(r"[^a-z0-9 ]", " ", carregar.normalizar(str(s or ""))).split())


def consultar_mapa() -> None:
    EXT.mkdir(parents=True, exist_ok=True)
    h = pd.read_csv(RAIZ / "dados" / "processados" / "habilitados.csv")
    # chave canônica já gravada: recalcular a partir de "proponente" deixa o CPF mascarado (XXXXXXXXXXX) dos MEIs
    prop = set(h["chave_proponente"].dropna())
    prop.discard("")
    titulos = {chave_titulo(t): p for t, p in zip(h["projeto"], h["numero_processo"]) if chave_titulo(t)}
    resumo = []

    # agentes: nome (e, se houver, nome completo) contra a chave do proponente
    lidos, casados = 0, []
    for a in paginar("agent", "id,name,type,terms,En_Municipio,createTimestamp"):
        if a is None:
            break
        lidos += 1
        if carregar.chave_proponente(a.get("name")) in prop:
            casados.append({"agente_id": a.get("id"), "nome": a.get("name"), "chave": carregar.chave_proponente(a.get("name")),
                            "tipo": (a.get("type") or {}).get("name"),
                            "area_atuacao": "; ".join((a.get("terms") or {}).get("area") or []),
                            "municipio": a.get("En_Municipio"),
                            "criado": ((a.get("createTimestamp") or {}).get("date") or "")[:10]})
    pd.DataFrame(casados).to_csv(EXT / "mapa_agentes_proponentes.csv", index=False)
    resumo.append({"entidade": "agent", "lidos": lidos, "casados": len(casados),
                   "chaves_de_proponente": len(prop), "proponentes_casados": len({c["chave"] for c in casados})})

    # projetos: nome contra o título do projeto da LICC
    lidos, casados = 0, []
    for p in paginar("project", "id,name,type,terms,createTimestamp,owner.name"):
        if p is None:
            break
        lidos += 1
        k = chave_titulo(p.get("name"))
        if k in titulos:
            casados.append({"projeto_mapa_id": p.get("id"), "numero_processo": titulos[k], "nome": p.get("name"),
                            "tipo": (p.get("type") or {}).get("name"),
                            "linguagem": "; ".join((p.get("terms") or {}).get("linguagem") or []),
                            "area": "; ".join((p.get("terms") or {}).get("area") or []),
                            "tags": "; ".join((p.get("terms") or {}).get("tag") or []),
                            "criado": ((p.get("createTimestamp") or {}).get("date") or "")[:10]})
    pd.DataFrame(casados).to_csv(EXT / "mapa_projetos_licc.csv", index=False)
    resumo.append({"entidade": "project", "lidos": lidos, "casados": len(casados), "titulos_licc": len(titulos),
                   "titulos_casados": len({c["numero_processo"] for c in casados})})

    # eventos: nome do evento ou do projeto a que pertence, contra o título da LICC; com ocorrências, se a API der
    sel = "id,name,terms,createTimestamp,project.name,occurrences.{startsOn,space.En_Municipio}"
    it = paginar("event", sel)
    primeiro = next(it, None)
    if primeiro is None:
        sel = "id,name,terms,createTimestamp,project.name"
        it, primeiro = paginar("event", sel), None
    lidos, casados = 0, []
    for e in ([primeiro] if primeiro else []) + list(it):
        if e is None:
            break
        lidos += 1
        nomes = [e.get("name"), (e.get("project") or {}).get("name")]
        k = next((chave_titulo(n) for n in nomes if chave_titulo(n) in titulos), None)
        if k:
            oc = e.get("occurrences") if isinstance(e.get("occurrences"), list) else []
            datas = sorted(((o.get("startsOn") or {}).get("date") or "")[:10] for o in oc if isinstance(o, dict))
            casados.append({"evento_id": e.get("id"), "numero_processo": titulos[k], "nome": e.get("name"),
                            "projeto": (e.get("project") or {}).get("name"),
                            "linguagem": "; ".join((e.get("terms") or {}).get("linguagem") or []),
                            "ocorrencias": len(oc),
                            "primeira_data": next((d for d in datas if d), ""),
                            "ultima_data": datas[-1] if datas else "",
                            "municipios": "; ".join(sorted({((o.get("space") or {}).get("En_Municipio") or "") for o in oc
                                                            if isinstance(o, dict)} - {""})),
                            "criado": ((e.get("createTimestamp") or {}).get("date") or "")[:10]})
    pd.DataFrame(casados).to_csv(EXT / "mapa_eventos_licc.csv", index=False)
    resumo.append({"entidade": "event", "lidos": lidos, "casados": len(casados), "titulos_licc": len(titulos),
                   "titulos_casados": len({c["numero_processo"] for c in casados}), "select": sel})
    pd.DataFrame(resumo).to_csv(EXT / "mapa_casamento_resumo.csv", index=False)
    print(pd.DataFrame(resumo).to_string(index=False))


DIO = "https://ioes.dio.es.gov.br"
# só a LICC (pedido do autor, 27/09/2026): a lei, a sigla, a lei de criação e a comissão que habilita os projetos
TERMOS_DIO = ["Lei de Incentivo à Cultura Capixaba", "LICC", "11.246/2021", "Comissão de Avaliação de Projetos"]


def _dio_pagina(termo: str, pagina: int, di: str, df: str):
    # rota montada como no script da busca (assets/javascripts/application.7d10c6fa.js, $scope.search)
    url = f"{DIO}/busca/busca/buscar/query/{pagina}/di:{di}/df:{df}/"
    try:
        r = requests.get(url, params={"1": "1", "q": f'"{termo}"'}, headers=UA, timeout=(15, 90))
    except requests.RequestException as e:
        return None, f"{url} erro {e}"
    diag = f"{r.url} -> {r.status_code} {r.headers.get('content-type', '')} {r.text[:300]!r}"
    try:
        return r.json(), diag
    except ValueError:
        return None, diag


def _trechos(conteudo: str, termo: str, antes: int = 1200, depois: int = 2800) -> list[str]:
    """Janela em volta de cada ocorrência do termo (sem acento e caixa), fundindo janelas que se sobrepõem."""
    def simples(x: str) -> str:  # sem acento e sem caixa, caractere a caractere (mantém as posições)
        return "".join((unicodedata.normalize("NFD", ch)[:1] or ch).lower()[:1] or ch for ch in x)
    alvo, base = " ".join(simples(termo).split()), simples(conteudo)
    janelas = []
    i = base.find(alvo)
    while i >= 0:
        a, b = max(0, i - antes), min(len(conteudo), i + len(alvo) + depois)
        if janelas and a <= janelas[-1][1]:
            janelas[-1] = (janelas[-1][0], b)
        else:
            janelas.append((a, b))
        i = base.find(alvo, i + len(alvo))
    return [conteudo[a:b] for a, b in janelas]


def consultar_dio() -> None:
    sys.path.insert(0, str(RAIZ / "analise" / "rede"))
    from mascarar_cpf import mascarar
    EXT.mkdir(parents=True, exist_ok=True)
    diag, linhas = [], []
    fim = time.strftime("%Y-%m-%d")
    formatos = [("2021-04-01", fim), ("01-04-2021", time.strftime("%d-%m-%Y")),
                ("2021-04-01T00:00:00", f"{fim}T23:59:59"), ("20210401", time.strftime("%Y%m%d"))]
    escolhido = None
    for di, df in formatos:
        d, msg = _dio_pagina(TERMOS_DIO[0], 0, di, df)
        diag.append(f"formato {di} / {df}: {msg}")
        if isinstance(d, dict) and isinstance(d.get("hits"), dict) and d["hits"].get("hits"):
            escolhido = (di, df)
            break
    if not escolhido:
        (EXT / "dio_licc_diagnostico.txt").write_text("\n".join(diag) + "\n", encoding="utf-8")
        print("DIO: nenhuma rota/formato devolveu resultados; ver dio_licc_diagnostico.txt")
        return
    vistos = set()
    for termo in TERMOS_DIO:
        total = None
        for pagina in range(0, 80):
            d, msg = _dio_pagina(termo, pagina, *escolhido)
            if pagina == 0:
                diag.append(f"{termo}: {msg[:200]}")
            hits = ((d or {}).get("hits") or {}) if isinstance(d, dict) else {}
            total = hits.get("total", total)
            if isinstance(total, dict):
                total = total.get("value")
            lista = hits.get("hits") or []
            if not lista:
                break
            for h in lista:
                src = h.get("_source") or {}
                conteudo = str(src.get("conteudo") or "")
                meta = {k: v for k, v in src.items() if k != "conteudo" and not isinstance(v, (dict, list))}
                chave = (h.get("_id"), termo)
                if chave in vistos:
                    continue
                vistos.add(chave)
                for j, t in enumerate(_trechos(conteudo, termo)):
                    t, _ = mascarar(" ".join(t.split()))
                    linhas.append({"termo": termo, "id": h.get("_id"), "trecho_n": j,
                                   "data": "-".join(str(src.get(k, "")).zfill(2) for k in ("year", "month", "day")),
                                   "pagina": src.get("pagina"), "diario": h.get("diario") or src.get("diario"),
                                   "meta": json.dumps(meta, ensure_ascii=False)[:500], "trecho": t})
            time.sleep(0.5)
        diag.append(f"{termo}: total informado {total}; trechos acumulados {len(linhas)}")
    pd.DataFrame(linhas).to_csv(EXT / "dio_licc_trechos.csv", index=False)
    (EXT / "dio_licc_diagnostico.txt").write_text("\n".join(diag) + "\n", encoding="utf-8")
    print(f"DIO: {len(linhas)} trechos; formato de data {escolhido}")


TRANSP = "https://transparencia.es.gov.br/Comum/incentivosfiscais/Download/{}"
ARQ_BENEF = {"vigentes": 311, "beneficiarios_2022": 544, "beneficiarios_2023": 543, "beneficiarios_2024": 437,
             "beneficiarios_2025": 538}
LICC_RX = re.compile(r"(?<!\d)11[.\s]?246(?!\d)|INCENTIVO\s+[ÀA]\s+CULTURA|CULTURA\s+CAPIXABA|\bLICC\b", re.I)


def consultar_beneficiarios() -> None:
    import io
    from collections import Counter
    EXT.mkdir(parents=True, exist_ok=True)
    diag, saida = [], []
    for nome, did in ARQ_BENEF.items():
        url = TRANSP.format(did)
        try:
            r = requests.get(url, headers=UA, timeout=(15, 300))
        except requests.RequestException as e:
            diag.append(f"## {nome} {url}: erro {e}")
            continue
        bruto = r.content
        cod = "utf-8"
        try:
            texto = bruto.decode("utf-8-sig")
        except UnicodeDecodeError:
            texto, cod = bruto.decode("latin-1"), "latin-1"
        amostra = texto[:5000]
        sep = max([";", ",", "\t", "|"], key=amostra.count)
        linhas = list(csv.reader(io.StringIO(texto), delimiter=sep))
        cab = linhas[0] if linhas else []
        corpo = linhas[1:]
        # rótulos de benefício: colunas de texto com poucos valores distintos (sem nome de contribuinte)
        rotulos = []
        for j, c in enumerate(cab):
            vals = Counter(l[j] for l in corpo if j < len(l))
            numericos = sum(n for k, n in vals.items() if re.fullmatch(r"[\d.,\s-]*", k))
            if (1 < len(vals) <= 400 and numericos < 0.5 * sum(vals.values())
                    and not re.search(r"cnpj|cpf|raz|nome|contribuinte|inscri", c, re.I)):
                rotulos.append(f"  coluna '{c}': {len(vals)} valores; mais frequentes: "
                               + "; ".join(f"{k[:60]} ({n})" for k, n in vals.most_common(25)))
        # a Lei 11.246/2021 também criou o incentivo ao esporte (LIEC): linhas do esporte ficam de fora (só LICC).
        # As relações de beneficiários só trazem CNPJ, razão social e total renunciado (todos os incentivos somados):
        # delas se gravam os patrocinadores da LICC (raiz do CNPJ nos anexos de captação), empresa a empresa.
        raizes = {c[:8] for c in cnpjs_patrocinadores()}
        casadas = [l for l in corpo if LICC_RX.search(" ".join(l))
                   or (nome.startswith("beneficiarios") and l and re.sub(r"\D", "", l[0])[:8] in raizes)]
        licc = [l for l in casadas if not re.search(r"ESPORT", " ".join(l), re.I)]
        for l in licc:
            saida.append({"arquivo": nome, "url": url, **{c or f"col{j}": (l[j] if j < len(l) else "") for j, c in enumerate(cab)}})
        diag.append(f"## {nome} {url}\nstatus {r.status_code}; {len(bruto)} bytes; content-type {r.headers.get('content-type')}; "
                    f"codificação {cod}; separador {sep!r}; linhas {len(corpo)}; linhas da LICC {len(licc)} "
                    f"(fora {len(casadas) - len(licc)} do esporte)\n"
                    f"cabeçalho: {cab}\n" + "\n".join(rotulos))
        time.sleep(1)
    pd.DataFrame(saida).to_csv(EXT / "transparencia_beneficiarios_licc.csv", index=False)
    (EXT / "transparencia_beneficiarios_diagnostico.txt").write_text("\n\n".join(diag) + "\n", encoding="utf-8")
    print(f"beneficiários: {len(saida)} linhas da LICC; ver transparencia_beneficiarios_diagnostico.txt")


def main() -> None:
    so = sys.argv[sys.argv.index("--so") + 1] if "--so" in sys.argv else "tudo"
    if so in ("cnpj", "tudo"):
        consultar_cnpjs()
    if so in ("proponentes", "tudo"):
        consultar_cnpjs(cnpjs_proponentes(), "cnpj_proponentes.csv")
    if so in ("mapa", "tudo"):
        consultar_mapa()
    if so in ("beneficiarios", "tudo"):
        consultar_beneficiarios()
    if so in ("dio", "tudo"):
        consultar_dio()


if __name__ == "__main__":
    main()
