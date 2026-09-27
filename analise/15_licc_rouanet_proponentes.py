"""
15 — Proponentes da LICC que também são proponentes da Lei Rouanet (mecenato federal).

Fonte: cache da API pública do SALIC/MinC (dados/externos/raw/salic/projetos_ano{AA}_off*.json, gerado por
analise/03a_salic_rouanet_uf.py em 2026-09-23). O download de cada ano de PRONAC (2019 a 2025) está completo: a soma
das linhas é igual ao campo "total" da API, conferido aqui. Proponentes da LICC: dados/processados/habilitados.csv
(ciclos 2022-2026).

Regras:
- casamento só pelo nome normalizado EXATO (carregar.chave_proponente), nunca por semelhança; o nome da LICC pode ser
  nome fantasia e o do SALIC a razão social, então o casamento é um PISO do número de proponentes em comum;
- chave com mais de um CPF/CNPJ no SALIC fica marcada como ambígua e fora da lista de CNPJ;
- pessoa física (CPF; o SALIC só publica 6 dígitos) entra só nas contagens: nem nome nem documento são gravados por proponente;
- o SALIC só cobre PRONACs de 2019 a 2025: "Rouanet antes da LICC" quer dizer "PRONAC de 2019 em diante e de ano
  anterior ao primeiro ciclo do proponente na LICC"; experiência anterior a 2019 fica fora (indeterminada);
- valor_captado do SALIC é o acumulado do projeto até a consulta, não o captado no ano.

Saídas (analise/tabelas/):
  15_proponentes_licc_na_rouanet.csv   um proponente pessoa jurídica casado por linha: CNPJ (SALIC), PRONACs, captado na
                                       Rouanet, projetos e valor na LICC, primeiro ano em cada lei
  15_licc_rouanet_resumo.csv           por ciclo e no total: proponentes, casados, projetos e valor autorizado na LICC
                                       por grupo, e situação oficial dos projetos por grupo
Uso: python analise/15_licc_rouanet_proponentes.py
"""
from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

import pandas as pd

RAIZ = Path(__file__).resolve().parents[1]
RAW = RAIZ / "dados" / "externos" / "raw" / "salic"
TAB = RAIZ / "analise" / "tabelas"
sys.path.insert(0, str(RAIZ / "analise"))
_spec = importlib.util.spec_from_file_location("carregar", RAIZ / "analise" / "01_carregar.py")
carregar = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(carregar)

FONTE = ("API SALIC/MinC (https://api.salic.cultura.gov.br/api/v1/projetos), cache de 2026-09-23 em "
         "dados/externos/raw/salic/; habilitados: dados/processados/habilitados.csv")


def salic() -> pd.DataFrame:
    linhas, conferencia = [], []
    for aa in range(19, 26):
        n, total = 0, None
        for arq in sorted(RAW.glob(f"projetos_ano{aa:02d}_off*.json")):
            d = json.loads(arq.read_text(encoding="utf-8"))
            ps = d.get("_embedded", {}).get("projetos", [])
            total = d.get("total")
            n += len(ps)
            linhas += ps
        conferencia.append((2000 + aa, n, total))
        if n != total:
            raise SystemExit(f"SALIC {2000 + aa}: {n} linhas no cache, API informa {total}")
    s = pd.DataFrame(linhas)
    s = s[s["mecanisnmo"] == "Mecenato"].copy()
    s["ano"] = 2000 + s["ano_projeto"].astype(int)
    s["chave"] = s["proponente"].map(carregar.chave_proponente)
    s["doc"] = s["cgccpf"].astype(str).str.replace(r"\D", "", regex=True)
    s["valor_captado"] = pd.to_numeric(s["valor_captado"], errors="coerce")
    print("SALIC, linhas por ano (cache = total da API):", conferencia)
    return s


def main() -> None:
    s = salic()
    h = pd.read_csv(RAIZ / "dados" / "processados" / "habilitados.csv").drop_duplicates("numero_processo")
    h = h[h["chave_proponente"].notna() & (h["chave_proponente"] != "")]
    m = s[s["chave"].isin(set(h["chave_proponente"]))]
    docs = m.groupby("chave")["doc"].nunique()
    ambiguas = set(docs[docs > 1].index)
    pf = set(m.loc[m["doc"].str.len() != 14, "chave"])  # o SALIC publica o CPF truncado (6 dígitos)

    por = m.groupby("chave").agg(pronacs=("PRONAC", "nunique"),
                                 pronacs_com_captacao=("valor_captado", lambda v: int((v > 0).sum())),
                                 captado_rouanet=("valor_captado", "sum"),
                                 primeiro_pronac=("ano", "min"), ultimo_pronac=("ano", "max"),
                                 ufs_salic=("UF", lambda x: "; ".join(sorted(set(x.dropna())))),
                                 cnpj_salic=("doc", lambda x: "; ".join(sorted(set(x)))))
    lic = h.groupby("chave_proponente").agg(projetos_licc=("numero_processo", "size"),
                                            autorizado_licc=("valor_autorizado", "sum"),
                                            primeiro_ciclo_licc=("ciclo", "min"),
                                            concluidos_ou_em_execucao=("status", lambda x: int(x.isin(["concluido", "em_execucao"]).sum())))
    por = por.join(lic)
    por["rouanet_antes_da_licc"] = por["primeiro_pronac"] < por["primeiro_ciclo_licc"]
    por["ambigua"] = por.index.isin(ambiguas)
    por["pessoa_fisica"] = por.index.isin(pf)
    pj = por[~por["pessoa_fisica"]].reset_index().rename(columns={"chave": "chave_proponente"})
    pj.loc[pj["ambigua"], "cnpj_salic"] = "ambígua: mais de um CNPJ com o mesmo nome"
    pj.sort_values("autorizado_licc", ascending=False).to_csv(TAB / "15_proponentes_licc_na_rouanet.csv", index=False)

    casados = set(por.index)
    antes = set(por.index[por["rouanet_antes_da_licc"]])
    captou_r = set(por.index[por["pronacs_com_captacao"] > 0])
    h["grupo"] = h["chave_proponente"].map(lambda k: "também na Rouanet" if k in casados else "só na LICC")
    linhas = []
    for ciclo, g in [("todos", h)] + list(h.groupby("ciclo")):
        props = set(g["chave_proponente"])
        linha = {"ciclo": ciclo, "proponentes": len(props), "casados_rouanet": len(props & casados),
                 "casados_com_captacao_rouanet": len(props & captou_r),
                 "casados_rouanet_antes_da_licc": len(props & antes),
                 "projetos": len(g), "projetos_de_casados": int((g["grupo"] == "também na Rouanet").sum()),
                 "autorizado": g["valor_autorizado"].sum(),
                 "autorizado_de_casados": g.loc[g["grupo"] == "também na Rouanet", "valor_autorizado"].sum()}
        for st in ("concluido", "em_execucao", "captando", "captacao_expirada"):
            for grupo, rot in (("também na Rouanet", "casados"), ("só na LICC", "so_licc")):
                linha[f"{st}_{rot}"] = int(((g["grupo"] == grupo) & (g["status"] == st)).sum())
        linhas.append(linha)
    r = pd.DataFrame(linhas)
    r["pct_proponentes_casados"] = r["casados_rouanet"] / r["proponentes"]
    r["pct_autorizado_casados"] = r["autorizado_de_casados"] / r["autorizado"]
    es = s[s["UF"] == "ES"]
    r["cobertura"] = (f"SALIC: PRONACs 2019-2025, mecenato, {len(s)} projetos no Brasil, {es['chave'].nunique()} "
                      f"proponentes no ES; casamento por nome exato (piso); {len(pf)} casados são pessoa física "
                      f"(só contagem); {len(ambiguas)} chaves ambíguas")
    r["fonte"] = FONTE
    r.to_csv(TAB / "15_licc_rouanet_resumo.csv", index=False)
    print(r.drop(columns=["cobertura", "fonte"]).T.to_string())
    print(r["cobertura"].iat[0])
    print("proponentes ES da Rouanet 2019-2025 que também estão na LICC:",
          len(set(es["chave"]) & casados), "de", es["chave"].nunique())


if __name__ == "__main__":
    main()
