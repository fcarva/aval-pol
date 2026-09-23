"""03e — Resumos de contexto para a introdução do artigo (gasto com cultura e Rouanet no ES).

Só agrega tabelas já baixadas por outros scripts; não acessa a rede.

Entradas:
  dados/externos/siconfi_cultura_municipios_es.csv  (03c_siconfi_cultura_icms.py; DCA, função 13, municípios do ES)
  dados/externos/siconfi_cultura_uf.csv             (03c; DCA, função 13, governos estaduais)
  dados/externos/rouanet_captacao_uf_ano.csv        (03a_salic_rouanet_uf.py; mecenato por UF e ano do PRONAC)
  dados/externos/rouanet_es_municipio.csv           (03a; mecenato no ES por município)

Saídas (analise/tabelas/):
  03e_f13_municipal_rmgv_interior.csv  gasto municipal empenhado na função cultura, RMGV × interior, por ano
  03e_f13_estadual_ranking.csv         posição do governo do ES entre as 27 UFs (per capita e % da despesa)
  03e_rouanet_es.csv                   captação da Rouanet no ES, parcela nacional e concentração em Vitória

Regra: município sem função 13 declarada é ausente, não zero; o per capita usa só a população dos
municípios com valor declarado, e a cobertura vai na tabela.
"""
from __future__ import annotations

from pathlib import Path

import pandas as pd

RAIZ = Path(__file__).resolve().parents[1]
EXT = RAIZ / "dados" / "externos"
TAB = RAIZ / "analise" / "tabelas"


def f13_municipal() -> None:
    m = pd.read_csv(EXT / "siconfi_cultura_municipios_es.csv", comment="#")
    linhas = []
    for ano, g in m.groupby("ano"):
        com = g[g["f13_emp"].notna()]
        total = com["f13_emp"].sum()
        for rot, sel in (("RMGV", com["rmgv"]), ("Interior", ~com["rmgv"]), ("ES", com["rmgv"] | ~com["rmgv"])):
            s = com[sel]
            universo = g[g["rmgv"]] if rot == "RMGV" else g[~g["rmgv"]] if rot == "Interior" else g
            linhas.append({
                "ano": ano, "grupo": rot, "municipios_com_valor": len(s), "municipios": len(universo),
                "f13_empenhado": s["f13_emp"].sum(), "share_f13": s["f13_emp"].sum() / total,
                "pop_2022_com_valor": s["pop_2022"].sum(),
                "f13_per_capita": s["f13_emp"].sum() / s["pop_2022"].sum(),
                "vitoria_share_f13": (com.loc[com["municipio"] == "Vitória", "f13_emp"].sum() / total
                                      if rot == "ES" else None),
            })
    pd.DataFrame(linhas).to_csv(TAB / "03e_f13_municipal_rmgv_interior.csv", index=False)


def f13_estadual_ranking() -> None:
    u = pd.read_csv(EXT / "siconfi_cultura_uf.csv", comment="#")
    linhas = []
    for ano, g in u.groupby("ano"):
        g = g.dropna(subset=["f13_emp_per_capita"]).sort_values("f13_emp_per_capita", ascending=False)
        g = g.reset_index(drop=True)
        es = g[g["uf"] == "ES"].iloc[0]
        linhas.append({
            "ano": ano, "ufs_com_valor": len(g), "es_f13_empenhado": es["f13_emp"],
            "es_per_capita": es["f13_emp_per_capita"], "es_rank_per_capita": int(g.index[g["uf"] == "ES"][0]) + 1,
            "mediana_ufs_per_capita": g["f13_emp_per_capita"].median(),
            "es_pct_despesa": es["pct_f13_emp_na_despesa"], "mediana_ufs_pct_despesa": g["pct_f13_emp_na_despesa"].median(),
        })
    pd.DataFrame(linhas).to_csv(TAB / "03e_f13_estadual_ranking.csv", index=False)


def rouanet_es() -> None:
    g = pd.read_csv(EXT / "rouanet_captacao_uf_ano.csv", comment="#")
    m = pd.read_csv(EXT / "rouanet_es_municipio.csv", comment="#")
    linhas = []
    for ano, x in g.groupby("ano"):
        es = x[x["UF"] == "ES"].iloc[0]
        rank = x.sort_values("valor_captado", ascending=False).reset_index(drop=True)
        linhas.append({"periodo": str(ano), "es_projetos": es["n_projetos"], "es_com_captacao": es["n_com_captacao"],
                       "es_captado": es["valor_captado"], "share_brasil": es["share_captado_brasil"],
                       "rank_uf": int(rank.index[rank["UF"] == "ES"][0]) + 1})
    tot = g.groupby("UF")["valor_captado"].sum().sort_values(ascending=False)
    anos = sorted(g["ano"].unique())
    linhas.append({"periodo": f"{anos[0]}-{anos[-1]}", "es_projetos": g.loc[g.UF == "ES", "n_projetos"].sum(),
                   "es_com_captacao": g.loc[g.UF == "ES", "n_com_captacao"].sum(), "es_captado": tot["ES"],
                   "share_brasil": tot["ES"] / tot.sum(), "rank_uf": list(tot.index).index("ES") + 1,
                   "vitoria_share_es": m.loc[m["municipio"] == "Vitória", "valor_captado"].sum() / m["valor_captado"].sum(),
                   "municipios_es_com_projeto": int((m["n_projetos"] > 0).sum())})
    pd.DataFrame(linhas).to_csv(TAB / "03e_rouanet_es.csv", index=False)


if __name__ == "__main__":
    f13_municipal()
    f13_estadual_ranking()
    rouanet_es()
    for n in ("03e_f13_municipal_rmgv_interior", "03e_f13_estadual_ranking", "03e_rouanet_es"):
        print(pd.read_csv(TAB / f"{n}.csv").to_string(), "\n")
