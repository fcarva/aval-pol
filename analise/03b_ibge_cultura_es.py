"""
03b — Setor cultural no ES: IBGE SIIC (por UF) e MUNIC 2021, bloco Cultura (por município do ES).

Fontes (consultadas em 2026-09-23):
- IBGE, API de pesquisas (servicodados.ibge.gov.br/api/v1/pesquisas):
    * pesquisa 10092 = Sistema de Informações e Indicadores Culturais (SIIC), publicação 01/12/2023
      (2011-2022) e atualizações posteriores; unidades e multiplicadores lidos dos metadados da API.
    * pesquisa 1 = MUNIC; período 2021 (publicado 08/12/2022), bloco "Cultura".
- IBGE, API SIDRA (apisidra.ibge.gov.br): tabela 4709 (população residente, Censo 2022) para municípios
  e UFs.

Saídas:
  dados/externos/siic_uf.csv                   (indicadores SIIC por UF e Brasil, formato longo)
  dados/externos/munic2021_cultura_es.csv      (equipamentos e institucionalidade por município do ES)
  dados/externos/munic2021_cultura_es_resumo.csv (RMGV x interior)
Regras: "Não informou"/"Recusa"/nulo ficam ausentes; contagens reportam cobertura.
"""
from __future__ import annotations

import json
from pathlib import Path

import pandas as pd
import requests

RAIZ = Path(__file__).resolve().parents[1]
OUT = RAIZ / "dados" / "externos"
RAW = OUT / "raw" / "ibge"
RAW.mkdir(parents=True, exist_ok=True)
API = "https://servicodados.ibge.gov.br/api/v1/pesquisas"

RMGV = {"Cariacica", "Fundão", "Guarapari", "Serra", "Viana", "Vila Velha", "Vitória"}  # licc-gov/codigo/src_ontology_municipios.ts

SIIC = {
    82732: "ocupados_setor_cultural_pnadc",      # mil pessoas (multiplicador 1000)
    82731: "ocupados_14mais_pnadc",
    82620: "rendimento_medio_setor_cultural_pnadc",
    82734: "assalariados_setor_cultural_cempre",
    82733: "unidades_locais_setor_cultural_cempre",
    82583: "empresas_setor_cultural_cempre",
    82584: "pct_empresas_setor_cultural_cempre",
    82585: "ocupados_empresas_setor_cultural_cempre",
    82586: "pct_ocupados_setor_cultural_cempre",
    82588: "valor_adicionado_atividades_culturais",
    82589: "pct_valor_adicionado_cultural",
    82622: "pct_residentes_mun_com_museu",
    82623: "pct_residentes_mun_com_teatro",
    82624: "pct_residentes_mun_com_cinema",
    82729: "pct_despesa_familiar_cultura_pof",
}

MUNIC21 = {
    94850: "bibliotecas_publicas",
    94852: "museus",
    94854: "teatros_salas_espetaculo",
    94856: "centro_cultural",
    94865: "cinema",
    94869: "livrarias",
    94870: "galerias_arte",
    94877: "ponto_de_cultura",
    94878: "ponto_de_cultura_qtd",
    94710: "plano_municipal_cultura",
    94734: "conselho_municipal_cultura",
    94786: "fundo_municipal_cultura",
    94881: "orcamento_cultura_executado_2020",
    94883: "distribuiu_lei_aldir_blanc",
}

UF_COD = {11: "RO", 12: "AC", 13: "AM", 14: "RR", 15: "PA", 16: "AP", 17: "TO", 21: "MA", 22: "PI",
          23: "CE", 24: "RN", 25: "PB", 26: "PE", 27: "AL", 28: "SE", 29: "BA", 31: "MG", 32: "ES",
          33: "RJ", 35: "SP", 41: "PR", 42: "SC", 43: "RS", 50: "MS", 51: "MT", 52: "GO", 53: "DF"}


def get_json(url: str, cache: str):
    p = RAW / cache
    if p.exists():
        return json.loads(p.read_text(encoding="utf-8"))
    r = requests.get(url, timeout=120)
    r.raise_for_status()
    d = r.json()
    p.write_text(json.dumps(d, ensure_ascii=False), encoding="utf-8")
    return d


def metadados(pesq: int, periodo: str | None = None) -> dict[int, dict]:
    url = f"{API}/{pesq}/periodos/{periodo}/indicadores" if periodo else f"{API}/{pesq}/indicadores/0"
    arv = get_json(url, f"meta_{pesq}_{periodo or 'all'}.json")
    out: dict[int, dict] = {}

    def walk(n, cam):
        for x in n:
            c = cam + [x.get("indicador") or ""]
            out[x["id"]] = {"nome": " > ".join(c), "unidade": (x.get("unidade") or {}).get("id"),
                            "mult": (x.get("unidade") or {}).get("multiplicador")}
            walk(x.get("children", []), c)
    walk(arv, [])
    return out


def siic() -> None:
    meta = metadados(10092)
    locs = "|".join(str(c) for c in UF_COD) + "|1"
    ids = "|".join(str(i) for i in SIIC)
    d = get_json(f"{API}/10092/periodos/all/indicadores/{ids}/resultados/{locs}", "siic_uf.json")
    linhas = []
    for ind in d:
        for r in ind["res"]:
            for ano, v in r["res"].items():
                if v in (None, "", "-", "..."):
                    continue
                try:
                    val = float(v)
                except ValueError:
                    continue
                loc = int(r["localidade"])
                mult = meta[ind["id"]]["mult"] or 1
                linhas.append({"indicador_id": ind["id"], "indicador": SIIC[ind["id"]],
                               "descricao_ibge": meta[ind["id"]]["nome"], "unidade": meta[ind["id"]]["unidade"],
                               "multiplicador": mult, "localidade": "BR" if loc == 1 else UF_COD.get(loc, loc),
                               "ano": int(ano), "valor_publicado": val, "valor": val * mult})
    df = pd.DataFrame(linhas).sort_values(["indicador", "localidade", "ano"])
    cab = ("# Fonte: IBGE, Sistema de Informacoes e Indicadores Culturais (SIIC), API "
           "servicodados.ibge.gov.br/api/v1/pesquisas/10092, consulta 2026-09-23. valor = valor_publicado x "
           "multiplicador dos metadados. Script: analise/03b_ibge_cultura_es.py\n")
    with open(OUT / "siic_uf.csv", "w", encoding="utf-8", newline="") as f:
        f.write(cab)
        df.to_csv(f, index=False)
    print("SIIC:", df.groupby("indicador")["ano"].agg(["min", "max", "count"]))


def populacao_mun_es() -> pd.DataFrame:
    url = "https://apisidra.ibge.gov.br/values/t/4709/n6/in%20n3%2032/v/93/p/2022?formato=json"
    d = get_json(url, "sidra_4709_mun_es.json")
    rows = [{"cod6": r["D1C"][:6], "cod7": r["D1C"], "municipio_uf": r["D1N"], "pop_2022": float(r["V"])}
            for r in d[1:]]
    df = pd.DataFrame(rows)
    df["municipio"] = df["municipio_uf"].str.replace(r" - ES$", "", regex=True)
    return df


def munic2021() -> None:
    meta = metadados(1, "2021")
    ids = "|".join(str(i) for i in MUNIC21)
    d = get_json(f"{API}/1/periodos/2021/indicadores/{ids}/resultados/32xxxx", "munic2021_cultura_es.json")
    reg: dict[str, dict] = {}
    for ind in d:
        for r in ind["res"]:
            reg.setdefault(r["localidade"], {})[MUNIC21[ind["id"]]] = r["res"].get("2021")
    df = pd.DataFrame.from_dict(reg, orient="index").reset_index().rename(columns={"index": "cod6"})
    pop = populacao_mun_es()
    df = pop.merge(df, on="cod6", how="left")
    df["rmgv"] = df["municipio"].isin(RMGV)
    cab = ("# Fonte: IBGE, MUNIC 2021 (Pesquisa de Informacoes Basicas Municipais), bloco Cultura, API "
           "servicodados.ibge.gov.br/api/v1/pesquisas/1/periodos/2021, consulta 2026-09-23; populacao: "
           "IBGE Censo 2022, SIDRA tabela 4709. Valores como publicados (Sim/Nao/Nao informou/quantidade). "
           "Script: analise/03b_ibge_cultura_es.py\n")
    with open(OUT / "munic2021_cultura_es.csv", "w", encoding="utf-8", newline="") as f:
        f.write(cab)
        df.to_csv(f, index=False)

    # Resumo RMGV x interior. Para itens Sim/Não: nº de municípios com "Sim" e nº com resposta válida.
    linhas = []
    itens_sn = ["museus", "teatros_salas_espetaculo", "centro_cultural", "cinema", "livrarias", "galerias_arte",
                "ponto_de_cultura", "bibliotecas_publicas", "plano_municipal_cultura",
                "conselho_municipal_cultura", "fundo_municipal_cultura", "distribuiu_lei_aldir_blanc"]
    for item in itens_sn:
        for grupo, sub in [("RMGV", df[df.rmgv]), ("Interior", df[~df.rmgv]), ("ES", df)]:
            s = sub[item]
            # "Sim, por instrumento legal" etc. contam como Sim; "Em elaboração" é resposta válida, não Sim
            valido = s.notna() & ~s.isin(["Não informou", "Recusa", "-"])
            sim = s.fillna("").str.startswith("Sim")
            linhas.append({"item": item, "grupo": grupo, "n_municipios": len(sub),
                           "n_resposta_valida": int(valido.sum()), "n_sim": int(sim.sum()),
                           "pop_2022": sub["pop_2022"].sum(),
                           "pop_em_municipio_com_sim": sub.loc[sim, "pop_2022"].sum()})
    res = pd.DataFrame(linhas)
    res["pct_mun_sim_sobre_validos"] = res["n_sim"] / res["n_resposta_valida"]
    res["pct_pop_em_mun_com_sim"] = res["pop_em_municipio_com_sim"] / res["pop_2022"]
    with open(OUT / "munic2021_cultura_es_resumo.csv", "w", encoding="utf-8", newline="") as f:
        f.write(cab)
        res.to_csv(f, index=False)
    # distribuição da execução do orçamento de cultura em 2020 (quesito categórico da MUNIC)
    orc = (df.groupby(["rmgv", "orcamento_cultura_executado_2020"]).size().rename("n_municipios").reset_index())
    with open(OUT / "munic2021_orcamento_cultura_es.csv", "w", encoding="utf-8", newline="") as f:
        f.write(cab)
        orc.to_csv(f, index=False)
    print(res.to_string())
    print("valores distintos:", {c: df[c].dropna().unique()[:6].tolist() for c in ["museus", "cinema", "bibliotecas_publicas", "orcamento_cultura_executado_2020"]})


if __name__ == "__main__":
    siic()
    munic2021()
