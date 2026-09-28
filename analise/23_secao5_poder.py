"""
23 — Poder da §5 refeita (r6): uma pergunta sobre o mecanismo de racionamento, "a renúncia vai para os projetos que
dependem dela?", montada na decomposição do viés de seleção de Foguel (2017, cap. 2): R = E11 − E00 = EMPT + V, com
V = E10 − E00 como objeto da avaliação.

Grupos de comparação que já existem pela regra da LICC (nenhum sorteio novo):
  theta1  realização dos termos recusados por esgotamento da cota (tinham patrocinador): E10 na margem
  theta0  realização dos habilitados cuja captação expirou (nenhuma empresa os escolheu): E00
  inabilitados pela CAP (filtro da comissão)
  validados na janela final de cada cota × recusados: EMPT na margem
  recusas de 2024 convertidas em validação após a ampliação do teto × mantidas (secundário)

Origem da lógica: rascunho de outra sessão do autor (analise/20_secao5_poder.py, 28/09/2026, não versionado), que
tinha as contagens digitadas; aqui todas vêm das tabelas do pipeline. Nada de efeito estimado: só tamanhos de amostra e
EMD pelas fórmulas do curso (analise/05_poder_mde.py: alfa = 5% bicaudal, poder de 80%), para diferença de proporções
entre grupos independentes, EMD = M·raiz(p0(1−p0)(1/n1 + 1/n0)), com p0 de 0,3 a 0,7 (o resultado ainda não medido).

Entradas (analise/tabelas/):
  03_status_conversao_por_faixa_valor_e_ciclo.csv  habilitados resolvidos e executados por faixa de valor, 2022-2024
  07_funil_por_ciclo.csv                           expirados por ciclo
  09_reentrada_resumo.csv, 09_reentrada_indeferidos.csv  recusados de 2023-2024 e valor de cada um
  12_cap_deliberacoes.csv                          inabilitados das atas da CAP
  13_versoes_captados_fila.csv                     recusas de 2024 convertidas e mantidas

Saídas (analise/tabelas/):
  23_captacao_por_faixa.csv   taxa de captação por faixa (até R$ 400 mil × acima) e ciclo, e expirados por faixa
  23_poder_secao5.csv         contraste, grupos, n, p0 e EMD
Uso: python analise/23_secao5_poder.py
"""
from __future__ import annotations

import importlib.util
from pathlib import Path

import pandas as pd

RAIZ = Path(__file__).resolve().parents[1]
TAB = RAIZ / "analise" / "tabelas"
_spec = importlib.util.spec_from_file_location("poder", RAIZ / "analise" / "05_poder_mde.py")
poder = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(poder)
M = poder.multiplicador()
P0 = (0.3, 0.5, 0.7)


def emd(n1: float, n0: float, p0: float) -> float:
    return 100 * M * (p0 * (1 - p0) * (1 / n1 + 1 / n0)) ** 0.5


def captacao_por_faixa() -> pd.DataFrame:
    f = pd.read_csv(TAB / "03_status_conversao_por_faixa_valor_e_ciclo.csv")
    f = f[f["ciclo"].between(2022, 2024)].copy()
    f["faixa"] = f["faixa_valor_ciclo"].map(lambda x: "até 400 mil" if x == "até 400 mil" else "acima de 400 mil")
    g = f.groupby(["ciclo", "faixa"], as_index=False)[["registros_resolvidos", "executados"]].sum()
    tot = f.groupby("faixa", as_index=False)[["registros_resolvidos", "executados"]].sum().assign(ciclo="2022-2024")
    out = pd.concat([g.assign(ciclo=g["ciclo"].astype(str)), tot], ignore_index=True)
    out["expirados"] = out["registros_resolvidos"] - out["executados"]
    out["taxa_captacao"] = out["executados"] / out["registros_resolvidos"]
    out["fonte"] = "03_status_conversao_por_faixa_valor_e_ciclo.csv (acima de 400 mil = 400-500 mil, 500 mil e acima)"
    return out


def main() -> None:
    faixas = captacao_por_faixa()
    faixas.to_csv(TAB / "23_captacao_por_faixa.csv", index=False)
    tot = faixas[faixas["ciclo"] == "2022-2024"].set_index("faixa")
    exp_peq, exp_gra = int(tot.loc["até 400 mil", "expirados"]), int(tot.loc["acima de 400 mil", "expirados"])

    fun = pd.read_csv(TAB / "07_funil_por_ciclo.csv").query("ciclo <= 2024")
    expirados = int(fun["expirou"].sum())
    if expirados != exp_peq + exp_gra:  # os resolvidos sem valor válido captaram; a soma por faixa tem de fechar
        raise SystemExit(f"expirados: funil {expirados} × faixas {exp_peq + exp_gra}")
    rr = pd.read_csv(TAB / "09_reentrada_resumo.csv")
    recusados = int(rr["projetos_recusados"].sum())
    recusas_ano = rr["projetos_recusados"].mean()
    ind = pd.read_csv(TAB / "09_reentrada_indeferidos.csv")
    rec_peq = int((ind["valor_recusado"] <= 400_000).sum())
    cap = pd.read_csv(TAB / "12_cap_deliberacoes.csv")
    inabilitados = int(cap.loc[cap["situacao"] == "inabilitado", "processo"].nunique())
    v = pd.read_csv(TAB / "13_versoes_captados_fila.csv").query("ano == 2024")
    convertidas = int(v["indeferido_depois_validado"].sum())
    mantidas = int((v["versoes_indeferido"] > 0).sum()) - convertidas
    expirados_ano = expirados / fun["ciclo"].nunique()

    linhas = []

    def add(contraste, grupo1, n1, grupo0, n0, uso):
        for p0 in P0:
            linhas.append({"contraste": contraste, "grupo1": grupo1, "n1": round(n1, 1), "grupo0": grupo0,
                           "n0": round(n0, 1), "p0": p0, "emd_pontos": emd(n1, n0, p0), "uso": uso})

    add("V = theta1 - theta0", "recusados por esgotamento (2023-2024)", recusados, "expirados (ciclos 2022-2024)",
        expirados, "retrospectivo, contraste principal")
    add("theta0 até 400 mil - theta0 acima", "expirados até 400 mil", exp_peq, "expirados acima de 400 mil", exp_gra,
        "retrospectivo, por faixa")
    add("filtro da CAP", "expirados", expirados, "inabilitados (atas da CAP, 2022-2026)", inabilitados,
        "retrospectivo")
    add("EMPT na margem", "validados na janela final de cada cota", recusados, "recusados por esgotamento", recusados,
        "retrospectivo, fila")
    add("EMPT na margem, ampliação de 2024", "recusas convertidas", convertidas, "recusas mantidas", mantidas,
        "retrospectivo, secundário")
    for anos in (2, 4):
        n1, n0 = recusados + anos * recusas_ano, expirados + anos * expirados_ano
        add(f"V, com mais {anos} ciclos", "recusados acumulados", n1, "expirados acumulados", n0, "prospectivo")
        add(f"theta1 até 400 mil - acima, com mais {anos} ciclos", "recusados até 400 mil (acumulados)",
            n1 * rec_peq / recusados, "recusados acima de 400 mil (acumulados)", n1 * (1 - rec_peq / recusados),
            "prospectivo, por faixa")
    out = pd.DataFrame(linhas)
    out["fonte"] = ("03_status_conversao_por_faixa_valor_e_ciclo.csv; 07_funil_por_ciclo.csv; 09_reentrada_*.csv; "
                    "12_cap_deliberacoes.csv; 13_versoes_captados_fila.csv; fórmulas de analise/05_poder_mde.py")
    out.to_csv(TAB / "23_poder_secao5.csv", index=False)
    with pd.option_context("display.width", 200):
        print(faixas.drop(columns=["fonte"]).round(3).to_string(index=False))
        print(f"recusados {recusados} (até 400 mil: {rec_peq}); expirados {expirados} ({exp_peq} + {exp_gra}); "
              f"inabilitados {inabilitados}; 2024: {convertidas} convertidas, {mantidas} mantidas")
        print(out.pivot_table(index=["contraste", "n1", "n0"], columns="p0", values="emd_pontos", sort=False)
              .round(1).to_string())


if __name__ == "__main__":
    main()
