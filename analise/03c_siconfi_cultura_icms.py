"""
03c — Gasto público com cultura (função 13) no ES e arrecadação de ICMS, a partir do SICONFI (STN).

Fonte: API de dados abertos do SICONFI/Tesouro Nacional,
       https://apidatalake.tesouro.gov.br/ords/siconfi/tt/dca  (Declaração de Contas Anuais - DCA)
       - Anexo I-E: despesa orçamentária por função/subfunção (colunas empenhadas, liquidadas, pagas)
       - Anexo I-C: receita orçamentária (receita bruta e deduções: transferências constitucionais, FUNDEB)
       Consulta em 2026-09-23. A DCA é declarada pelo próprio ente; ente que não declarou fica AUSENTE.
       IPCA: IBGE/SIDRA tabela 1737, variável 2266 (número-índice), média anual.

Saídas (dados/externos/):
  siconfi_cultura_es_estado.csv     função 13 do Governo do ES, 2015-2025 (nominal e a preços de 2025)
  siconfi_cultura_uf.csv            função 13 de todos os estados + DF, 2024 e 2025 (per capita, % da despesa)
  siconfi_cultura_municipios_es.csv função 13 dos 78 municípios do ES, 2023-2025
  siconfi_icms_es.csv               ICMS do ES (bruto, parcela municipal, FUNDEB), 2018-2025, e teto de 2% da lei
"""
from __future__ import annotations

import json
import time
from pathlib import Path

import pandas as pd
import requests

RAIZ = Path(__file__).resolve().parents[1]
OUT = RAIZ / "dados" / "externos"
RAW = OUT / "raw" / "siconfi"
RAW.mkdir(parents=True, exist_ok=True)
URL = "https://apidatalake.tesouro.gov.br/ords/siconfi/tt/dca"
UFS = {11: "RO", 12: "AC", 13: "AM", 14: "RR", 15: "PA", 16: "AP", 17: "TO", 21: "MA", 22: "PI", 23: "CE",
       24: "RN", 25: "PB", 26: "PE", 27: "AL", 28: "SE", 29: "BA", 31: "MG", 32: "ES", 33: "RJ", 35: "SP",
       41: "PR", 42: "SC", 43: "RS", 50: "MS", 51: "MT", 52: "GO", 53: "DF"}
RMGV = {"Cariacica", "Fundão", "Guarapari", "Serra", "Viana", "Vila Velha", "Vitória"}
CAB = ("# Fonte: SICONFI/STN, API https://apidatalake.tesouro.gov.br/ords/siconfi/tt/dca ({anexo}), consulta "
       "2026-09-23; valores declarados pelo ente; ente sem declaracao = ausente. {extra}"
       "Script: analise/03c_siconfi_cultura_icms.py\n")


def dca(ano: int, anexo: str, ente: int) -> list[dict] | None:
    cache = RAW / f"dca_{anexo.replace(' ', '_')}_{ano}_{ente}.json"
    if cache.exists():
        d = json.loads(cache.read_text(encoding="utf-8"))
        return d if d else None
    for tent in range(4):
        try:
            r = requests.get(URL, params={"an_exercicio": ano, "no_anexo": anexo, "id_ente": ente}, timeout=120)
            r.raise_for_status()
            items = r.json().get("items", [])
            break
        except Exception as e:  # noqa: BLE001
            print(f"  falha {anexo} {ano} {ente}: {e}", flush=True)
            time.sleep(4 * (tent + 1))
    else:
        return None
    cache.write_text(json.dumps(items, ensure_ascii=False), encoding="utf-8")
    return items or None


def funcao13(items: list[dict]) -> dict:
    """Extrai total de despesa e função 13 (e subfunções) por coluna."""
    out: dict = {}
    for x in items:
        conta, col = x["conta"], x["coluna"]
        tag = {"Despesas Empenhadas": "emp", "Despesas Liquidadas": "liq", "Despesas Pagas": "pag"}.get(col)
        if not tag:
            continue
        if conta == "Despesas Exceto Intraorçamentárias":
            out[f"desp_total_{tag}"] = x["valor"]
        elif conta.startswith("13 - "):
            out[f"f13_{tag}"] = x["valor"]
        elif conta.startswith("13.391"):
            out[f"f13_391_patrimonio_{tag}"] = x["valor"]
        elif conta.startswith("13.392"):
            out[f"f13_392_difusao_{tag}"] = x["valor"]
        elif conta.startswith("FU13"):
            out[f"f13_demais_{tag}"] = x["valor"]
        out["populacao"] = x.get("populacao")
        out["instituicao"] = x.get("instituicao")
    return out


def ipca_media_anual() -> pd.Series:
    cache = RAW / "sidra_1737_ipca.json"
    if cache.exists():
        d = json.loads(cache.read_text(encoding="utf-8"))
    else:
        u = "https://apisidra.ibge.gov.br/values/t/1737/n1/all/v/2266/p/201501-202512?formato=json"
        d = requests.get(u, timeout=120).json()
        cache.write_text(json.dumps(d, ensure_ascii=False), encoding="utf-8")
    df = pd.DataFrame([{"mes": r["D3C"], "idx": float(r["V"])} for r in d[1:] if r["V"] not in ("...", "-")])
    df["ano"] = df["mes"].str[:4].astype(int)
    return df.groupby("ano")["idx"].mean()


def salvar(df: pd.DataFrame, nome: str, anexo: str, extra: str = "") -> None:
    with open(OUT / nome, "w", encoding="utf-8", newline="") as f:
        f.write(CAB.format(anexo=anexo, extra=extra))
        df.to_csv(f, index=False)
    print("gravado", nome, df.shape)


def estado_es() -> None:
    ipca = ipca_media_anual()
    rows = []
    for ano in range(2015, 2026):
        it = dca(ano, "DCA-Anexo I-E", 32)
        if not it:
            rows.append({"ano": ano})
            continue
        rows.append({"ano": ano, **funcao13(it)})
    df = pd.DataFrame(rows)
    fator = ipca.loc[2025] / df["ano"].map(ipca)
    for c in ["f13_emp", "f13_liq", "f13_pag", "desp_total_emp", "desp_total_liq"]:
        if c in df:
            df[f"{c}_real2025"] = df[c] * fator
    df["pct_f13_emp_na_despesa"] = df["f13_emp"] / df["desp_total_emp"]
    df["f13_emp_per_capita"] = df["f13_emp"] / df["populacao"]
    salvar(df, "siconfi_cultura_es_estado.csv", "DCA-Anexo I-E, ente 32 Governo do ES",
           "Precos de 2025 pelo IPCA medio anual (SIDRA 1737). ")


def todas_ufs() -> None:
    rows = []
    for ano in (2024, 2025):
        for cod, uf in UFS.items():
            it = dca(ano, "DCA-Anexo I-E", cod)
            rows.append({"ano": ano, "uf": uf, **(funcao13(it) if it else {})})
    df = pd.DataFrame(rows)
    df["pct_f13_emp_na_despesa"] = df["f13_emp"] / df["desp_total_emp"]
    df["f13_emp_per_capita"] = df["f13_emp"] / df["populacao"]
    df["f13_liq_per_capita"] = df["f13_liq"] / df["populacao"]
    df["rank_per_capita_emp"] = df.groupby("ano")["f13_emp_per_capita"].rank(ascending=False)
    salvar(df, "siconfi_cultura_uf.csv", "DCA-Anexo I-E, governos estaduais e DF")


def municipios_es() -> None:
    mun = pd.read_csv(OUT / "munic2021_cultura_es.csv", comment="#", dtype={"cod7": str})[["cod7", "municipio", "pop_2022"]]
    rows = []
    for ano in (2023, 2024, 2025):
        for _, m in mun.iterrows():
            it = dca(ano, "DCA-Anexo I-E", int(m.cod7))
            rows.append({"ano": ano, "cod7": m.cod7, "municipio": m.municipio, "pop_2022": m.pop_2022,
                         "declarou_dca": bool(it), **(funcao13(it) if it else {})})
    df = pd.DataFrame(rows)
    df["rmgv"] = df["municipio"].isin(RMGV)
    df["f13_emp_per_capita"] = df["f13_emp"] / df["populacao"]
    df["pct_f13_emp_na_despesa"] = df["f13_emp"] / df["desp_total_emp"]
    salvar(df, "siconfi_cultura_municipios_es.csv", "DCA-Anexo I-E, 78 municipios do ES",
           "Municipio que declarou DCA mas nao registrou funcao 13 fica com f13 ausente (nao zero). ")


def icms_es() -> None:
    rows = []
    for ano in range(2018, 2026):
        it = dca(ano, "DCA-Anexo I-C", 32)
        r = {"ano": ano}
        for x in it or []:
            # ICMS (exclui adicional do Fundo de Combate à Pobreza). Ementário de receita mudou em 2022:
            # até 2021 a conta era 1.1.1.8.02.1.0; a partir de 2022, 1.1.1.4.50.1.0.
            if x["cod_conta"] in ("RO1.1.1.4.50.1.0", "RO1.1.1.8.02.1.0"):
                tag = {"Receitas Brutas Realizadas": "icms_bruto",
                       "Deduções - Transferências Constitucionais": "icms_ded_transf_municipios",
                       "Deduções - FUNDEB": "icms_ded_fundeb",
                       "Outras Deduções da Receita": "icms_outras_deducoes"}[x["coluna"]]
                r[tag] = x["valor"]
            if (x["cod_conta"] in ("RO1.1.1.4.50.2.0", "RO1.1.1.8.02.2.0")
                    and x["coluna"] == "Receitas Brutas Realizadas"):
                r["icms_adicional_fecp_bruto"] = x["valor"]
        rows.append(r)
    df = pd.DataFrame(rows)
    df["icms_liquido_parcela_estadual"] = df["icms_bruto"] - df["icms_ded_transf_municipios"]
    df["limite_2pct_lei_11246"] = 0.02 * df["icms_liquido_parcela_estadual"]
    df["pct_municipios"] = df["icms_ded_transf_municipios"] / df["icms_bruto"]
    salvar(df, "siconfi_icms_es.csv", "DCA-Anexo I-C, ente 32, conta 1.1.1.4.50.1.0 ICMS",
           "limite_2pct = 2% x (ICMS bruto - deducao de transferencias constitucionais aos municipios), "
           "leitura do autor do art. 5-B, IX, a, da Lei 7.000/2001 (red. Lei 11.246/2021); aplica-se ao teto do "
           "exercicio SEGUINTE. ")


if __name__ == "__main__":
    import sys
    etapas = sys.argv[1:] or ["estado", "icms", "ufs", "municipios"]
    if "estado" in etapas:
        estado_es()
    if "icms" in etapas:
        icms_es()
    if "ufs" in etapas:
        todas_ufs()
    if "municipios" in etapas:
        municipios_es()
