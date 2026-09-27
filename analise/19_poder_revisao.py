"""
19 — Poder estatístico revisto (rodada 4 da revisão): braços de H4, regra de conglomerados e H5 por variável
instrumental.

Confere a Tabela 2 do artigo contra o material da disciplina (slides de amostragem e poder: "são necessários, pelo
menos, 30 a 50 conglomerados em cada um dos grupos"; "cumprimento parcial ou atrito exigem amostra maior") e calcula
as variantes que a revisão propõe. Mesmas fórmulas de analise/05_poder_mde.py (alfa = 5% bicaudal, poder de 80%).

Entradas:
  analise/tabelas/07_mapa_quadro_h3.csv      J, N, m e cv dos municípios do interior (coletivos; todos os agentes)
  analise/tabelas/09_reentrada_resumo.csv    recusados pelo teto em 2023-2024 e quantos captaram até 2026

Variantes de H4 (p0 de 2% a 10%; rho de 0,02 a 0,05):
  a) dois grupos por município (a Tabela 2 do artigo);
  b) três grupos por município (controle, apoio documental, apoio à busca de patrocínio): cada contraste usa 2/3
     dos municípios e dos agentes;
  c) híbrido: controle × tratado por município e os dois braços sorteados entre agentes dentro dos municípios
     tratados (o contraste entre braços compara agentes do mesmo município; efeito do desenho tomado como 1).
H5: o efeito de receber em algum momento, com a recusa como instrumento, é a razão entre o efeito da recusa e o
primeiro estágio; o EMD do efeito local é o da forma reduzida dividido pelo primeiro estágio. Cenário: recusados de
2025-2026 obtidos por LAI (a SEFAZ não publica a lista desde 2025) dobram a amostra da margem.
H4, cumprimento parcial: o efeito local para quem responde à oferta é o da oferta dividido pela adesão; o EMD cresce
na mesma razão (adesões de 25% e 50%, hipotéticas).

H1, braço da população (auditoria do desenho, 27/09/2026): os mesmos perfis de projeto avaliados por uma amostra de
residentes do ES; a premissa de H1 ("não deixa de fora bem público que a população valorizaria") é testada pela
diferença entre o efeito de um atributo na escolha da empresa e na da população. EMD da diferença =
raiz(EMD_empresas² + EMD_população²), com amostras independentes; 6 tarefas (12 perfis) por residente.

H2, avaliação cega (auditoria do desenho): avaliadores independentes dão nota, sem saber o destino, aos projetos
inscritos nos critérios de interesse público do decreto. Contrastes: (a) inabilitados das atas da CAP × amostra de igual
tamanho de habilitados; (b) entre os habilitados de 2022-2024 com situação resolvida, quem captou × quem não captou.
EMD em desvios-padrão da nota (resultado contínuo).
H5, desenho prospectivo: recusados necessários, por braço, para detectar 15 pontos na margem do teto.

Saída: analise/tabelas/19_poder_revisao.csv
Uso: python analise/19_poder_revisao.py
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

REGRA_MIN_POR_GRUPO = 30  # slides de amostragem e poder da disciplina: 30 a 50 conglomerados por grupo


def h4() -> list[dict]:
    q = pd.read_csv(TAB / "07_mapa_quadro_h3.csv")
    linhas = []
    for _, r in q.iterrows():
        for p0 in (0.02, 0.10):
            for icc in (0.02, 0.05):
                deff = poder.efeito_desenho(r["m"], icc, r["cv"])
                variantes = {
                    "a) dois grupos por município": (r["J"], r["N"], deff, r["J"] / 2),
                    "b) três grupos por município (contraste entre dois)": (2 * r["J"] / 3, 2 * r["N"] / 3, deff,
                                                                           r["J"] / 3),
                    "c) híbrido: braços sorteados entre agentes nos municípios tratados": (r["J"] / 2, r["N"] / 2, 1.0,
                                                                                          r["J"] / 2),
                }
                for nome, (J, N, d, por_grupo) in variantes.items():
                    linhas.append({"hipotese": "H4", "quadro": r["quadro"], "desenho": nome, "p0": p0, "icc": icc,
                                   "municipios_no_contraste": round(J, 1), "agentes_no_contraste": round(N, 1),
                                   "municipios_por_grupo": round(por_grupo, 1),
                                   "atende_30_por_grupo": bool(por_grupo >= REGRA_MIN_POR_GRUPO),
                                   "emd_pontos": 100 * poder.mde_binario(p0, N, T=0.5) * d ** 0.5})
                itt = 100 * poder.mde_binario(p0, r["N"], T=0.5) * deff ** 0.5
                for adesao in (0.25, 0.5):
                    linhas.append({"hipotese": "H4", "quadro": r["quadro"], "p0": p0, "icc": icc,
                                   "desenho": f"a) efeito local para quem adere (adesão {adesao:.0%})",
                                   "municipios_no_contraste": r["J"], "agentes_no_contraste": r["N"],
                                   "municipios_por_grupo": r["J"] / 2,
                                   "atende_30_por_grupo": bool(r["J"] / 2 >= REGRA_MIN_POR_GRUPO),
                                   "emd_pontos": itt / adesao})
    return linhas


def h5() -> list[dict]:
    r = pd.read_csv(TAB / "09_reentrada_resumo.csv")
    recusados = int(r["projetos_recusados"].sum())
    captaram = int(r["captaram_ate_2026"].sum())
    primeiro_estagio = 1 - captaram / recusados  # validados recebem todos; recusados, captaram/recusados
    linhas = []
    for p0 in (0.2, 0.4, 0.6):
        rf = 100 * poder.mde_binario(p0, 2 * recusados, T=0.5)
        linhas += [{"hipotese": "H5", "quadro": f"{recusados} recusados × {recusados} validados", "p0": p0,
                    "desenho": "receber agora (forma reduzida)", "emd_pontos": rf},
                   {"hipotese": "H5", "quadro": f"{recusados} recusados × {recusados} validados", "p0": p0,
                    "desenho": f"receber em algum momento (efeito local; primeiro estágio {primeiro_estagio:.3f})",
                    "emd_pontos": rf / primeiro_estagio},
                   {"hipotese": "H5", "quadro": f"cenário: {2 * recusados} recusados × {2 * recusados} validados", "p0": p0,
                    "desenho": "receber agora, com os recusados de 2025-2026 (LAI)",
                    "emd_pontos": 100 * poder.mde_binario(p0, 4 * recusados, T=0.5)}]
    return linhas


def emd_conjoint(respondentes: int, tarefas: int, icc: float) -> float:
    m = 2 * tarefas
    return 100 * poder.mde_binario(0.5, respondentes * m, T=0.5) * poder.efeito_desenho(m, icc, 0.0) ** 0.5


def h1_populacao() -> list[dict]:
    linhas = []
    for R_emp in (30, 60):
        for R_pop in (500, 1000):
            for icc in (0.0, 0.1):
                e_emp, e_pop = emd_conjoint(R_emp, 12, icc), emd_conjoint(R_pop, 6, icc)
                linhas.append({"hipotese": "H1", "quadro": f"{R_emp} decisores × 12 tarefas; {R_pop} residentes × 6 tarefas",
                               "desenho": "diferença de efeito do atributo: empresas − população", "p0": 0.5, "icc": icc,
                               "emd_empresas": e_emp, "emd_populacao": e_pop,
                               "emd_pontos": (e_emp ** 2 + e_pop ** 2) ** 0.5})
    return linhas


def h2_avaliacao_cega() -> list[dict]:
    cap = pd.read_csv(TAB / "12_cap_deliberacoes.csv")
    inab = cap.loc[cap["situacao"] == "inabilitado", "processo"].nunique()
    fun = pd.read_csv(TAB / "07_funil_por_ciclo.csv")
    fun = fun[fun["ciclo"] <= 2024]
    n1, n0 = int(fun["captou"].sum()), int(fun["expirou"].sum())
    return [{"hipotese": "H2", "quadro": f"{inab} inabilitados × {inab} habilitados sorteados",
             "desenho": "avaliação cega: diferença de nota, habilitados × inabilitados (desvios-padrão)",
             "emd_pontos": poder.mde_simples(1.0, 2 * inab, P=0.5)},
            {"hipotese": "H2", "quadro": f"{n1} captaram × {n0} não captaram (habilitados 2022-2024)",
             "desenho": "avaliação cega: diferença de nota, captou × não captou (desvios-padrão)",
             "emd_pontos": poder.mde_simples(1.0, n1 + n0, P=n1 / (n1 + n0))}]


def h5_prospectivo(delta: float = 0.15) -> list[dict]:
    return [{"hipotese": "H5", "quadro": "desenho prospectivo, margem acumulada", "p0": p0,
             "desenho": f"recusados necessários por braço para EMD de {delta * 100:.0f} pontos",
             "emd_pontos": delta * 100,
             "recusados_por_braco": poder.n_simples(delta, (p0 * (1 - p0)) ** 0.5, P=0.5) / 2}
            for p0 in (0.2, 0.4, 0.6)]


def main() -> None:
    out = pd.DataFrame(h4() + h5() + h1_populacao() + h2_avaliacao_cega() + h5_prospectivo())
    out["fonte"] = ("analise/tabelas/07_mapa_quadro_h3.csv; analise/tabelas/09_reentrada_resumo.csv; fórmulas de "
                    "analise/05_poder_mde.py")
    out.to_csv(TAB / "19_poder_revisao.csv", index=False)
    with pd.option_context("display.width", 250, "display.max_colwidth", 70):
        print(out.drop(columns=["fonte"]).round(1).to_string(index=False))


if __name__ == "__main__":
    main()
