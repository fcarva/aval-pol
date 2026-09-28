"""
21 — Etapas da captação por ano: termo listado no anexo, validado, no Portal da Transparência, depositado (aviso no DIO)
e renúncia realizada (SEFAZ).

Motivo (parecer externo de 27/09/2026, ponto "Etapas administrativas e o status da captação"): o artigo dizia que a
captação de 2025 esgotou o teto contando um termo ainda "em análise na SEFAZ". Termo apresentado, validação, depósito e
renúncia efetiva são etapas distintas; aqui se concilia cada uma, ano a ano, com a fonte de cada número, e se rastreia o
termo em análise de 2025. Ausência não é zero: onde a fonte não cobre, a célula fica vazia.

Entradas:
  artigo/auditoria/auditoria_captacao_anual.csv   anexos da SECULT: montante, soma dos termos, validados, em análise
                                                  (saída de artigo/auditoria/auditar_captacao.py, versionada)
  dados/processados/transparencia_licc_termos.csv termos do Portal da Transparência, 2022-2025 (16_transparencia_licc.py)
  analise/tabelas/16_renuncia_sefaz.csv           renúncia realizada, demonstrativos da SEFAZ (R$ mil)
  analise/tabelas/18_deposito_x_portal.csv        depósitos localizados nos avisos do DIO (18_dio_avisos_habilitacao.py)
  dados/processados/captados_2025.csv             anexo de 2025 (marca "(Em análise na SEFAZ)" no proponente)
  dados/processados/dio_avisos_deposito.csv       avisos de depósito do DIO

Saídas (analise/tabelas/):
  21_etapas_captacao.csv        uma linha por ano de captação
  21_em_analise_2025.csv        os termos do projeto em análise em 2025, no Portal e nos avisos de depósito
Uso: python analise/21_etapas_captacao.py
"""
from __future__ import annotations

import re
import unicodedata
from pathlib import Path

import pandas as pd

RAIZ = Path(__file__).resolve().parents[1]
TAB = RAIZ / "analise" / "tabelas"
PROC = RAIZ / "dados" / "processados"


def chave(s) -> str:
    s = "".join(c for c in unicodedata.normalize("NFD", str(s).lower()) if not unicodedata.combining(c))
    return " ".join(re.findall(r"[a-z0-9]+", s))


def etapas() -> pd.DataFrame:
    a = pd.read_csv(RAIZ / "artigo" / "auditoria" / "auditoria_captacao_anual.csv").set_index("ano_captacao")
    t = pd.read_csv(PROC / "transparencia_licc_termos.csv")
    t = t[~t["valor_zero"]]
    portal = t.groupby("ano").agg(portal_termos=("valor", "size"), portal_processos=("processo", "nunique"),
                                  portal_valor=("valor", "sum"))
    r = pd.read_csv(TAB / "16_renuncia_sefaz.csv")
    ren = r[r["tipo"] == "realizada"].groupby("ano_ref")["valor_mil_reais"].first() * 1000
    d = pd.read_csv(TAB / "18_deposito_x_portal.csv")
    d = d[d["ano"].astype(str).str.fullmatch(r"\d{4}")].assign(ano=lambda x: x["ano"].astype(int)).set_index("ano")
    linhas = []
    for ano in a.index:
        x = a.loc[ano]
        validados = x["soma_validados"] if pd.notna(x["soma_validados"]) else None
        linha = {
            "ano_captacao": int(ano),
            "teto_portarias_sefaz": x["teto_portarias_sefaz"],
            "montante_impresso_anexo": x["montante_impresso"],
            "anexo_soma_termos": x["soma_termos"],
            "anexo_termos": x["termos"],
            "anexo_projetos": x["projetos"],
            "anexo_validados": validados,
            "anexo_em_analise": x["valor_em_analise"] if pd.notna(x["valor_em_analise"]) else None,
            "anexo_projetos_em_analise": x["projetos_em_analise"] if pd.notna(x["projetos_em_analise"]) else None,
            "portal_termos": portal["portal_termos"].get(ano),
            "portal_processos": portal["portal_processos"].get(ano),
            "portal_valor": portal["portal_valor"].get(ano),
            "renuncia_realizada": ren.get(ano),
            "dio_valor_depositado_localizado": d["valor_depositado_localizado"].get(ano),
            "dio_pct_valor_localizado": d["pct_valor_localizado"].get(ano),
        }
        # o montante esgota quando a soma listada iguala o montante impresso; confere quando anexo, Portal e renúncia
        # realizada coincidem (ao centavo; a renúncia vem em R$ mil)
        linha["anexo_esgota_montante"] = bool(abs(x["soma_termos"] - x["montante_impresso"]) < 0.01)
        if linha["portal_valor"] is not None and linha["renuncia_realizada"] is not None:
            linha["anexo_portal_renuncia_conferem"] = bool(abs(x["soma_termos"] - linha["portal_valor"]) < 0.01
                                                           and abs(linha["portal_valor"] - linha["renuncia_realizada"]) < 1000)
        else:
            linha["anexo_portal_renuncia_conferem"] = None
        linhas.append(linha)
    out = pd.DataFrame(linhas)
    out["fonte"] = ("anexos da SECULT (auditoria_captacao_anual.csv); Portal da Transparência (transparencia_licc_termos.csv); "
                    "demonstrativos da renúncia (16_renuncia_sefaz.csv); avisos de depósito do DIO (18_deposito_x_portal.csv)")
    return out


def em_analise_2025() -> pd.DataFrame:
    c = pd.read_csv(PROC / "captados_2025.csv")
    marcado = c[c["proponente"].astype(str).str.contains(r"em an[áa]lise", case=False, regex=True)]
    t = pd.read_csv(PROC / "transparencia_licc_termos.csv", dtype={"cnpj_patrocinador": str})
    dep = pd.read_csv(PROC / "dio_avisos_deposito.csv", dtype={"cnpj_patrocinador": str})
    linhas = []
    for _, m in marcado.iterrows():
        proc, titulo = m["numero_processo"], chave(m["projeto"])
        for _, r in t[(t["processo"] == proc) & (~t["valor_zero"])].iterrows():
            linhas.append({"processo": proc, "etapa": "termo no Portal (2025)", "data": r["data_processo"],
                           "cnpj_patrocinador": r["cnpj_patrocinador"], "valor": r["valor"]})
        casados = dep[dep["projeto_dio"].map(chave) == titulo]
        for _, r in casados.iterrows():
            linhas.append({"processo": proc, "etapa": "aviso de depósito no DIO", "data": r["data_dio"],
                           "cnpj_patrocinador": r["cnpj_patrocinador"], "valor": r["valor_dio"]})
        linhas.append({"processo": proc, "etapa": "anexo de 2025: valor captado marcado em análise", "data": None,
                       "cnpj_patrocinador": None, "valor": m["valor_captado"]})
    out = pd.DataFrame(linhas)
    out["fonte"] = "captados_2025.csv; transparencia_licc_termos.csv; dio_avisos_deposito.csv (título exato, sem acento)"
    return out


def main() -> None:
    e = etapas()
    e.to_csv(TAB / "21_etapas_captacao.csv", index=False)
    a = em_analise_2025()
    a.to_csv(TAB / "21_em_analise_2025.csv", index=False)
    with pd.option_context("display.width", 250, "display.max_columns", 30):
        print(e.drop(columns=["fonte"]).to_string(index=False))
        print(a.drop(columns=["fonte"]).to_string(index=False))
        s = a.groupby("etapa")["valor"].sum()
        print(s.round(2).to_string())


if __name__ == "__main__":
    main()
