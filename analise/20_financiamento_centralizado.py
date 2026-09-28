"""
20 — Financiamento centralizado: o sinal de amplitude do apoio e a viabilidade dos desenhos retrospectivos.

Pedido do autor (28/09/2026): pensar retroativamente como evidenciar, com inferência causal e os dados que existem, o
financiamento centralizado na escolha das empresas, sem estimar efeitos no artigo (só o desenho e o método). A ideia
de que o valor de um bem público deveria crescer com quantos o apoiam (Buterin, Hitzig e Weyl, 2019) entra de forma
tácita, como medida da ausência desse sinal no mecanismo.

Entradas:
  dados/processados/transparencia_licc_termos.csv           termos de 2022-2025 (patrocinador por CNPJ)
  analise/tabelas/03_status_conversao_por_faixa_valor_e_ciclo.csv   habilitados resolvidos por faixa de valor e ciclo
  analise/tabelas/13_versoes_captados_fila.csv              versões do anexo de 2024 (validação tardia)
  analise/tabelas/03_anual.csv                              valor autorizado por ciclo
  analise/tabelas/07_funil_por_ciclo.csv                    habilitados com situação resolvida (captou × expirou)

Regras: patrocinador contado pela raiz do CNPJ (8 dígitos), para não contar filiais como apoiadores distintos; termos
de valor zero ficam fora; nada de efeito estimado: as tabelas trazem tamanhos de amostra e o EMD das fórmulas do curso
(analise/05_poder_mde.py; alfa = 5% bicaudal, poder de 80%, p0 = 0,5, o caso de maior variância, porque o desenho não
usa o resultado).

Saídas (analise/tabelas/):
  20_patrocinadores_por_projeto.csv   número de patrocinadores por projeto-ano: projetos e valor em cada classe
  20_desenho_retroativo.csv           por desenho: células, tamanhos e EMD
Uso: python analise/20_financiamento_centralizado.py
"""
from __future__ import annotations

import importlib.util
from pathlib import Path

import pandas as pd

RAIZ = Path(__file__).resolve().parents[1]
TAB = RAIZ / "analise" / "tabelas"
PROC = RAIZ / "dados" / "processados"
_spec = importlib.util.spec_from_file_location("poder", RAIZ / "analise" / "05_poder_mde.py")
poder = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(poder)
M = poder.multiplicador()


def patrocinadores_por_projeto() -> pd.DataFrame:
    t = pd.read_csv(PROC / "transparencia_licc_termos.csv", dtype={"cnpj_patrocinador": str})
    t = t[~t["valor_zero"]]
    g = (t.assign(raiz=t["cnpj_patrocinador"].str[:8])
         .groupby(["ano", "processo"]).agg(patrocinadores=("raiz", "nunique"), valor=("valor", "sum")).reset_index())
    linhas = []
    for rotulo, x in [("2022-2025", g)] + [(str(a), y) for a, y in g.groupby("ano")]:
        for k, z in x.groupby(x["patrocinadores"].clip(upper=3)):
            linhas.append({"periodo": rotulo, "patrocinadores": "3 ou mais" if k == 3 else str(k),
                           "projetos": len(z), "pct_projetos": len(z) / len(x),
                           "valor": z["valor"].sum(), "pct_valor": z["valor"].sum() / x["valor"].sum(),
                           "projetos_no_periodo": len(x)})
    out = pd.DataFrame(linhas)
    out["fonte"] = "Portal da Transparência, termos da LICC 2022-2025 (dados/processados/transparencia_licc_termos.csv)"
    return out


def emd_diferenca(ns: list[float]) -> float:
    """EMD (pontos) de uma diferença (ou diferença em diferenças) de proporções entre células independentes, p0 = 0,5."""
    return 100 * M * (sum(0.25 / n for n in ns)) ** 0.5


def desenho_retroativo() -> pd.DataFrame:
    linhas = []
    # H4: pequenos (até R$ 400 mil) × pedido exato no teto, ciclos 2022 e 2024
    f = pd.read_csv(TAB / "03_status_conversao_por_faixa_valor_e_ciclo.csv")
    cel = f.set_index(["ciclo", "faixa_valor_ciclo"])["registros_resolvidos"]
    for ciclo in (2022, 2023, 2024):
        for faixa in ("até 400 mil", "exatamente 500 mil"):
            linhas.append({"desenho": "H4: diferenças em diferenças, pequenos × teto", "celula": f"{ciclo}, {faixa}",
                           "n": int(cel[(ciclo, faixa)])})
    ns = [cel[(c, fx)] for c in (2022, 2024) for fx in ("até 400 mil", "exatamente 500 mil")]
    linhas.append({"desenho": "H4: diferenças em diferenças, pequenos × teto", "celula": "EMD, 2022 × 2024",
                   "n": int(sum(ns)), "emd_pontos": emd_diferenca(ns)})
    an = pd.read_csv(TAB / "03_anual.csv")
    an = an[an["ciclo"].astype(str).str.fullmatch(r"\d{4}")].set_index("ciclo")
    for ciclo in ("2022", "2023", "2024"):
        linhas.append({"desenho": "H4: intensidade da competição (valor autorizado do ciclo)", "celula": ciclo,
                       "n": int(an.loc[ciclo, "autorizado_n"]), "valor_autorizado": float(an.loc[ciclo, "autorizado_total"])})
    # H5 e H2: ampliação de 2024 como choque de oferta (versões do anexo)
    v = pd.read_csv(TAB / "13_versoes_captados_fila.csv").query("ano == 2024")
    antes = int(((v["versoes_indeferido"] == 0) & (v["versoes_validado"] > 0)).sum())
    tarde = int(v["indeferido_depois_validado"].sum())
    nunca = int(((v["versoes_indeferido"] > 0) & (v["versoes_validado"] == 0)).sum())
    for rot, n in (("validados sem recusa", antes), ("recusados e validados depois", tarde), ("recusados e nunca validados", nunca)):
        linhas.append({"desenho": "H5 e H2: ampliação de 2024, marginais × inframarginais", "celula": rot, "n": n})
    linhas.append({"desenho": "H5 e H2: ampliação de 2024, marginais × inframarginais",
                   "celula": "EMD, validados depois × validados sem recusa", "n": antes + tarde,
                   "emd_pontos": emd_diferenca([antes, tarde])})
    linhas.append({"desenho": "H5 e H2: ampliação de 2024, marginais × inframarginais",
                   "celula": "EMD, validados depois × nunca validados", "n": tarde + nunca,
                   "emd_pontos": emd_diferenca([tarde, nunca])})
    # H1: preferência revelada entre habilitados resolvidos de 2022-2024
    fun = pd.read_csv(TAB / "07_funil_por_ciclo.csv").query("ciclo <= 2024")
    n = int(fun["captou"].sum() + fun["expirou"].sum())
    linhas.append({"desenho": "H1: preferência revelada, ser escolhido entre habilitados",
                   "celula": "habilitados resolvidos 2022-2024 (atributo binário, metade com o atributo)", "n": n,
                   "emd_pontos": 100 * poder.mde_binario(0.5, n, T=0.5)})
    out = pd.DataFrame(linhas)
    out["fonte"] = ("03_status_conversao_por_faixa_valor_e_ciclo.csv; 03_anual.csv; 13_versoes_captados_fila.csv; "
                    "07_funil_por_ciclo.csv; fórmulas de analise/05_poder_mde.py")
    return out


def main() -> None:
    pp = patrocinadores_por_projeto()
    pp.to_csv(TAB / "20_patrocinadores_por_projeto.csv", index=False)
    dr = desenho_retroativo()
    dr.to_csv(TAB / "20_desenho_retroativo.csv", index=False)
    with pd.option_context("display.width", 220, "display.max_colwidth", 60):
        print(pp.drop(columns=["fonte"]).round(3).to_string(index=False))
        print(dr.drop(columns=["fonte"]).round(1).to_string(index=False))


if __name__ == "__main__":
    main()
