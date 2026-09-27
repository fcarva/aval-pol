"""Consultas a bases públicas que não pedem LAI, rodadas no relé (GitHub Actions, rede aberta).

1. CNPJ dos patrocinadores (BrasilAPI; se falhar, minhareceita.org): porte, natureza jurídica, atividade (CNAE),
   município, capital social, data de abertura e opção pelo Simples. Os CNPJs saem dos anexos "Recurso financeiro
   captado" de 2022 a 2026 e das versões antigas coletadas (dados/fontes_web/paginas/). O quadro de sócios não é
   gravado.
2. Mapa Cultural: agentes, projetos e eventos, lidos por inteiro pela API pública, mas gravados só quando o nome
   normalizado coincide EXATAMENTE com um proponente ou um título de projeto da LICC (dados/processados/
   habilitados.csv). Sem semelhança aproximada, e sem gravar dados de quem não é proponente (LGPD).

Saídas (dados/externos/):
  cnpj_patrocinadores.csv          uma linha por CNPJ de patrocinador
  mapa_agentes_proponentes.csv     agentes do Mapa cujo nome casa com um proponente (área de atuação, município, tipo)
  mapa_projetos_licc.csv           projetos do Mapa cujo nome casa com um título da LICC
  mapa_eventos_licc.csv            eventos do Mapa cujo nome, ou o do projeto, casa com um título da LICC
  mapa_casamento_resumo.csv        quantos registros foram lidos e quantos casaram, por entidade
Uso: python analise/rede/consultas_publicas.py [--so cnpj|mapa]
"""
from __future__ import annotations

import csv
import importlib.util
import json
import re
import sys
import time
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


def consultar_cnpjs() -> None:
    EXT.mkdir(parents=True, exist_ok=True)
    destino = EXT / "cnpj_patrocinadores.csv"
    feitos = {}
    if destino.exists():
        feitos = {r["cnpj"]: r for r in csv.DictReader(destino.open(encoding="utf-8")) if r.get("razao_social")}
    linhas = []
    for c in cnpjs_patrocinadores():
        if c in feitos:
            linhas.append(feitos[c])
            continue
        d, fonte = get_json(f"https://brasilapi.com.br/api/cnpj/v1/{c}"), "brasilapi"
        if not d:
            d, fonte = get_json(f"https://minhareceita.org/{c}"), "minhareceita"
        linha = {k: (d or {}).get(k, "") for k in CAMPOS_CNPJ}
        linha.update(cnpj=c, fonte=fonte if d else "sem resposta",
                     consultado_utc=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()))
        linhas.append(linha)
        time.sleep(1.2)
    with destino.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=CAMPOS_CNPJ)
        w.writeheader()
        w.writerows(linhas)
    print(f"CNPJ de patrocinadores: {len(linhas)}; com resposta: {sum(bool(l['razao_social']) for l in linhas)}")


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
    prop = {carregar.chave_proponente(p) for p in h["proponente"].dropna()}
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


def main() -> None:
    so = sys.argv[sys.argv.index("--so") + 1] if "--so" in sys.argv else "tudo"
    if so in ("cnpj", "tudo"):
        consultar_cnpjs()
    if so in ("mapa", "tudo"):
        consultar_mapa()


if __name__ == "__main__":
    main()
