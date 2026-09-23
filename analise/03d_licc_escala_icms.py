"""
03d — Escala da LICC: teto anual de renúncia x ICMS do ES x gasto direto com cultura; demanda habilitada x teto;
distribuição da demanda habilitada pelas cotas do art. 18 (classificação da própria SECULT).

Entradas:
  dados/externos/siconfi_icms_es.csv            (analise/03c_siconfi_cultura_icms.py)
  dados/externos/siconfi_cultura_es_estado.csv  (idem)
  dados/externos/siconfi_cultura_municipios_es.csv (idem)
  dados/licc/habilitados/habilitados-{2022..2026}.csv (transcrição oficial dos anexos da SECULT)
  dados/licc/oficial/captados-2025.csv          (anexo "RECURSO FINANCEIRO CAPTADO 2025")
Tetos anuais: digitados abaixo COM a fonte de cada um; status "verificado" = lido no texto oficial;
"[VERIFICAR]" = visto só em fonte secundária/busca.

Saídas:
  dados/externos/licc_teto_vs_icms.csv
  dados/externos/licc_habilitados_por_cota.csv
"""
from __future__ import annotations

import glob
from pathlib import Path

import pandas as pd

RAIZ = Path(__file__).resolve().parents[1]
EXT = RAIZ / "dados" / "externos"

TETOS = [
    # ano, teto R$, fonte, status
    (2022, 10_000_000, "Portaria SEFAZ nº 09-R, de 27/01/2022 (DIO-ES 28/01/2022); notas/politica/fontes/portarias-sefaz-secult-2022.md", "verificado"),
    (2023, 15_000_000, "Resumo de busca (WebSearch, 2026-09-23): 'R$ 15 milhões ... assim como no ano de 2023'; ato da SEFAZ não lido", "[VERIFICAR]"),
    (2024, 25_000_000, "SECULT, notícia 'Governo amplia para R$ 25 milhões...' (anúncio de 16/04/2024; teto inicial R$ 15 mi fixado pela SEFAZ); ato da SEFAZ de ampliação não lido", "verificado (notícia oficial); ato [VERIFICAR]"),
    (2025, 25_000_000, "Portaria SEFAZ nº 01-R, de 07/01/2025, citada pela SECULT; soma do anexo 'RECURSO FINANCEIRO CAPTADO 2025' = R$ 25.000.000,00", "verificado (captado); portaria [VERIFICAR texto]"),
    (2026, 25_000_000, "Portaria SEFAZ nº 02-R, de 08/01/2026, segundo jornaloalegrense.com.br (resultado de busca); ato não lido", "[VERIFICAR]"),
]

CAB = ("# Fonte: {fonte}. Script: analise/03d_licc_escala_icms.py (2026-09-23)\n")


def escala() -> None:
    icms = pd.read_csv(EXT / "siconfi_icms_es.csv", comment="#").set_index("ano")
    est = pd.read_csv(EXT / "siconfi_cultura_es_estado.csv", comment="#").set_index("ano")
    mun = pd.read_csv(EXT / "siconfi_cultura_municipios_es.csv", comment="#")
    mun_tot = mun.groupby("ano").agg(f13_mun_emp=("f13_emp", "sum"), n_mun_com_f13=("f13_emp", "count"))
    rows = []
    for ano, teto, fonte, status in TETOS:
        base = ano - 1  # o limite de 2% incide sobre a arrecadação do exercício ANTERIOR
        r = {"ano_teto": ano, "teto_renuncia": teto, "fonte_teto": fonte, "status_teto": status,
             "ano_base_icms": base,
             "icms_bruto_ano_base": icms["icms_bruto"].get(base),
             "icms_parcela_estadual_ano_base": icms["icms_liquido_parcela_estadual"].get(base),
             "limite_legal_2pct": icms["limite_2pct_lei_11246"].get(base),
             "icms_bruto_mesmo_ano": icms["icms_bruto"].get(ano),
             "f13_estado_emp_mesmo_ano": est["f13_emp"].get(ano),
             "f13_municipios_emp_mesmo_ano": mun_tot["f13_mun_emp"].get(ano),
             "n_municipios_com_f13": mun_tot["n_mun_com_f13"].get(ano)}
        rows.append(r)
    df = pd.DataFrame(rows)
    df["teto_sobre_icms_estadual_base"] = df["teto_renuncia"] / df["icms_parcela_estadual_ano_base"]
    df["teto_sobre_limite_legal"] = df["teto_renuncia"] / df["limite_legal_2pct"]
    df["teto_sobre_icms_bruto_mesmo_ano"] = df["teto_renuncia"] / df["icms_bruto_mesmo_ano"]
    df["teto_sobre_f13_estado"] = df["teto_renuncia"] / df["f13_estado_emp_mesmo_ano"]
    df["teto_sobre_f13_estado_mais_mun"] = df["teto_renuncia"] / (df["f13_estado_emp_mesmo_ano"] + df["f13_municipios_emp_mesmo_ano"])
    with open(EXT / "licc_teto_vs_icms.csv", "w", encoding="utf-8", newline="") as f:
        f.write(CAB.format(fonte="tetos conforme coluna fonte_teto; ICMS e funcao 13: SICONFI/DCA (siconfi_icms_es.csv, "
                                 "siconfi_cultura_es_estado.csv, siconfi_cultura_municipios_es.csv). A renuncia e gasto "
                                 "tributario: NAO esta contida na funcao 13"))
        df.to_csv(f, index=False)
    print(df.drop(columns=["fonte_teto"]).T.to_string())


def habilitados() -> None:
    fs = sorted(glob.glob(str(RAIZ / "dados" / "licc" / "habilitados" / "habilitados-*.csv")))
    h = pd.concat([pd.read_csv(f).assign(ciclo=int(Path(f).stem[-4:])) for f in fs], ignore_index=True)
    h["valor_autorizado"] = pd.to_numeric(h["valor_autorizado"], errors="coerce")
    g = (h.assign(enq=h["enquadramento"].fillna("(sem classificação publicada)"))
          .groupby(["ciclo", "enq"])
          .agg(n_projetos=("projeto", "count"), n_com_valor=("valor_autorizado", "count"),
               valor_autorizado=("valor_autorizado", "sum"))
          .reset_index())
    tot = h.groupby("ciclo").agg(n_ciclo=("projeto", "count"), valor_ciclo=("valor_autorizado", "sum"))
    g = g.merge(tot, on="ciclo")
    g["share_valor_no_ciclo"] = g["valor_autorizado"] / g["valor_ciclo"]
    teto = {a: t for a, t, *_ in TETOS}
    # O ciclo de habilitação N capta, em regra, no ano seguinte (CLAUDE.md, regra 4); comparamos com o teto de N+1.
    g["teto_ano_seguinte"] = g["ciclo"].map(lambda c: teto.get(c + 1))
    with open(EXT / "licc_habilitados_por_cota.csv", "w", encoding="utf-8", newline="") as f:
        f.write(CAB.format(fonte="dados/licc/habilitados/habilitados-{2022..2026}.csv (anexos oficiais SECULT); "
                                 "enquadramento = cota do art. 18 como publicada pela SECULT; valor_autorizado = teto "
                                 "de captacao habilitado, nao captado"))
        g.to_csv(f, index=False)
    print(tot.assign(teto_ano_seguinte=tot.index.map(lambda c: teto.get(c + 1)),
                     razao=lambda d: d.valor_ciclo / d.teto_ano_seguinte).to_string())
    print(g.to_string())


if __name__ == "__main__":
    escala()
    habilitados()
