"""02_externos.py — dados externos do IBGE para a análise territorial da LICC.

Baixa (uma vez; depois lê do cache em dados/externos/):
  1. lista oficial dos 78 municípios do ES com código IBGE
     (API de localidades: servicodados.ibge.gov.br/api/v1/localidades/estados/32/municipios);
  2. população residente do Censo 2022 (SIDRA, tabela 4709, variável 93) e
     estimativas de população 2024-2026 (SIDRA, tabela 6579, variável 9324);
  3. PIB municipal a preços correntes (SIDRA, tabela 5938, variável 37,
     unidade: mil reais), anos 2021-2023 (2023 é o mais recente publicado);
  4. malha municipal GeoJSON (API de malhas v3 do IBGE);
  5. composição legal da RMGV.

RMGV — composição legal conferida no texto oficial:
  Lei Complementar estadual nº 318/2005 (jan. 2005), art. 2º: "A RMGV é
  integrada pelos Municípios de Cariacica, Fundão, Guarapari, Serra, Viana,
  Vila Velha e Vitória". PDF lido via firecrawl em 2026-09-23:
  https://planometropolitano.es.gov.br/Media/comdevit/Legisla%C3%A7%C3%A3o/2005-01-lei318-05.pdf
  (a página de legislação do PDUI data a LC de 18/01/2005; o Decreto 1511-R/2005
  a cita como de 17/01/2005 — data exata [VERIFICAR]; a composição não muda).
  Histórico: LC 58/1995 institui a RMGV; LC 159/1999 inclui Guarapari;
  LC 204/2001 fixa os 7 municípios (fonte: planometropolitano.es.gov.br/legislacao-2).

Saídas:
  dados/externos/municipios_es.csv   (cod_ibge, municipio, regiões IBGE, rmgv,
                                      pop_censo2022, pop_est2024..2026, pib_2021..2023_mil)
  dados/externos/malha_municipios_es.geojson
  dados/externos/*.json               (respostas brutas das APIs, para auditoria)
"""
from __future__ import annotations

import json

import pandas as pd

from _comum import EXTERNOS, _get_json, municipios_ibge, normalizar

RMGV = ["Cariacica", "Fundão", "Guarapari", "Serra", "Viana", "Vila Velha", "Vitória"]
FONTE_RMGV = (
    "LC estadual 318/2005, art. 2º — "
    "https://planometropolitano.es.gov.br/Media/comdevit/Legisla%C3%A7%C3%A3o/2005-01-lei318-05.pdf"
)

SIDRA = "https://apisidra.ibge.gov.br/values"


def sidra(tabela: int, variavel: int, periodos: str, cache: str) -> pd.DataFrame:
    url = f"{SIDRA}/t/{tabela}/n6/in%20n3%2032/v/{variavel}/p/{periodos}"
    bruto = _get_json(url, EXTERNOS / cache, timeout=120)
    df = pd.DataFrame(bruto[1:])  # linha 0 é o cabeçalho descritivo
    out = pd.DataFrame(
        {
            "cod_ibge": df["D1C"].astype(int),
            "ano": df["D3C"].astype(int),
            "unidade": df["MN"],
            # SIDRA usa "-", "..", "X" para ausência/sigilo: vira NaN, nunca 0
            "valor": pd.to_numeric(df["V"], errors="coerce"),
        }
    )
    out.attrs["url"] = url
    return out


def main() -> None:
    mun = municipios_ibge()
    rmgv_chaves = {normalizar(n) for n in RMGV}
    mun["rmgv"] = mun["chave"].isin(rmgv_chaves)
    assert mun["rmgv"].sum() == 7, "RMGV deve ter 7 municípios (LC 318/2005, art. 2º)"

    censo = sidra(4709, 93, "2022", "sidra_t4709_v93_censo2022.json")
    est = sidra(6579, 9324, "2024,2025,2026", "sidra_t6579_v9324_estimativas.json")
    pib = sidra(5938, 37, "2021,2022,2023", "sidra_t5938_v37_pib.json")

    assert (pib["unidade"] == "Mil Reais").all(), pib["unidade"].unique()

    mun = mun.merge(
        censo[["cod_ibge", "valor"]].rename(columns={"valor": "pop_censo2022"}), on="cod_ibge", how="left"
    )
    for a in (2024, 2025, 2026):
        e = est.loc[est.ano == a, ["cod_ibge", "valor"]].rename(columns={"valor": f"pop_est{a}"})
        mun = mun.merge(e, on="cod_ibge", how="left")
    for a in (2021, 2022, 2023):
        p = pib.loc[pib.ano == a, ["cod_ibge", "valor"]].rename(columns={"valor": f"pib_{a}_mil"})
        mun = mun.merge(p, on="cod_ibge", how="left")

    mun["fonte_rmgv"] = FONTE_RMGV
    mun.to_csv(EXTERNOS / "municipios_es.csv", index=False, encoding="utf-8")

    malha_url = (
        "https://servicodados.ibge.gov.br/api/v3/malhas/estados/32"
        "?intrarregiao=municipio&formato=application/vnd.geo+json"
    )
    geo = _get_json(malha_url, EXTERNOS / "malha_municipios_es.geojson", timeout=120)
    n_feat = len(geo["features"])

    print(f"municípios: {len(mun)} | RMGV: {mun.rmgv.sum()} | feições na malha: {n_feat}")
    print("população Censo 2022 (ES):", int(mun.pop_censo2022.sum()),
          "| cobertura:", mun.pop_censo2022.notna().sum(), "/ 78")
    print("estimativa 2025 (ES):", int(mun.pop_est2025.sum()), "| cobertura:", mun.pop_est2025.notna().sum())
    print("PIB 2023 (ES, R$ mil):", int(mun.pib_2023_mil.sum()), "| cobertura:", mun.pib_2023_mil.notna().sum())
    print("URLs:", censo.attrs["url"], est.attrs["url"], pib.attrs["url"], malha_url, sep="\n  ")


if __name__ == "__main__":
    main()
