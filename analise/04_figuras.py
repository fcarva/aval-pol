"""04_figuras.py — figuras do artigo (PNG, 300 dpi), lidas só de analise/tabelas/.

Figura 1 (analise/figuras/04_fig1_conversao_territorio.png), dois painéis:
  (a) taxa de execução entre habilitados resolvidos, por faixa de valor autorizado e ciclo (2022-2024)
      — 03_status_conversao_por_faixa_valor_e_ciclo.csv
  (b) participação da RMGV em população, PIB, presenças de projetos e valor autorizado atribuível,
      2022-2026 — 03_territorio_rmgv_interior.csv

Cores: rampa ordinal azul (passos 250/450/650 da paleta de referência do skill de visualização,
validada com --ordinal sobre fundo branco); um único azul no painel (b). Fonte Liberation Serif,
métrica igual à Times New Roman do artigo.
"""
from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402

RAIZ = Path(__file__).resolve().parents[1]
TAB = RAIZ / "analise" / "tabelas"
FIG = RAIZ / "analise" / "figuras"
FIG.mkdir(parents=True, exist_ok=True)

RAMPA = ["#86b6ef", "#2a78d6", "#104281"]  # ordinal: até 400 mil → exatamente 500 mil
AZUL = "#2a78d6"
TINTA, TINTA_2, GRADE = "#0b0b0b", "#52514e", "#e4e3df"

plt.rcParams.update({
    "font.family": "Liberation Serif", "font.size": 9, "axes.edgecolor": TINTA_2,
    "axes.labelcolor": TINTA, "xtick.color": TINTA_2, "ytick.color": TINTA_2,
    "axes.spines.top": False, "axes.spines.right": False,
})


def pct(x: float) -> str:
    return f"{100 * x:.0f}%".replace(".", ",")


def painel_conversao(ax) -> None:
    t = pd.read_csv(TAB / "03_status_conversao_por_faixa_valor_e_ciclo.csv")
    faixas = ["até 400 mil", "400-500 mil (exclusive)", "exatamente 500 mil"]
    rotulos = ["Até R$ 400 mil", "R$ 400-500 mil", "Exatamente R$ 500 mil"]
    ciclos = [2022, 2023, 2024]
    x = np.arange(len(ciclos))
    w = 0.27
    for i, (f, rot, cor) in enumerate(zip(faixas, rotulos, RAMPA)):
        s = t[t["faixa_valor_ciclo"] == f].set_index("ciclo").reindex(ciclos)
        pos = x + (i - 1) * (w + 0.03)
        ax.bar(pos, s["taxa_execucao"], width=w, color=cor, label=rot, zorder=2)
        for xp, v, n in zip(pos, s["taxa_execucao"], s["registros_resolvidos"]):
            ax.text(xp, v + 0.015, pct(v), ha="center", va="bottom", fontsize=6.5, color=TINTA)
            ax.text(xp, 0.02, f"n={int(n)}", ha="center", va="bottom", fontsize=6.5,
                    color="white" if cor != RAMPA[0] else TINTA, rotation=90)
    ax.set_xticks(x, [str(c) for c in ciclos])
    ax.set_xlabel("Ciclo de habilitação")
    ax.set_ylim(0, 1.0)
    ax.set_yticks([0, 0.25, 0.5, 0.75, 1.0], ["0%", "25%", "50%", "75%", "100%"])
    ax.yaxis.grid(True, color=GRADE, linewidth=0.6, zorder=0)
    ax.set_ylabel("Executados / resolvidos")
    ax.set_title("(a) Execução, por valor autorizado", loc="left", fontsize=9.5, color=TINTA)
    ax.legend(frameon=False, fontsize=7, loc="upper center", bbox_to_anchor=(0.5, -0.2), ncol=3,
              handlelength=1.0, columnspacing=0.8, handletextpad=0.4)


def painel_territorio(ax) -> None:
    r = pd.read_csv(TAB / "03_territorio_rmgv_interior.csv").set_index("grupo").loc["RMGV"]
    itens = [("População 2022", r["share_pop_censo2022"]),
             ("PIB 2023", r["share_pib_2023_mil"]),
             ("Presenças LICC", r["share_processos_presenca_soma"]),
             ("Valor LICC", r["share_autorizado_atribuivel"])]
    y = np.arange(len(itens))[::-1]
    vals = [v for _, v in itens]
    ax.barh(y, vals, height=0.55, color=AZUL, zorder=2)
    for yy, v in zip(y, vals):
        ax.text(v + 0.03, yy, pct(v), va="center", fontsize=8, color=TINTA)
    ax.set_yticks(y, [n for n, _ in itens])
    ax.set_xlim(0, 0.8)
    ax.set_xticks([0, 0.2, 0.4, 0.6, 0.8], ["0%", "20%", "40%", "60%", "80%"])
    ax.xaxis.grid(True, color=GRADE, linewidth=0.6, zorder=0)
    ax.axvline(0.5, color=TINTA_2, linewidth=0.8, linestyle=(0, (3, 2)), zorder=1)
    ax.set_title("(b) Parcela da RMGV no ES", loc="left", fontsize=9.5, color=TINTA)


def main() -> None:
    fig, (a, b) = plt.subplots(1, 2, figsize=(6.5, 3.1), gridspec_kw={"width_ratios": [1.3, 1]})
    painel_conversao(a)
    painel_territorio(b)
    fig.tight_layout(w_pad=2.0)
    out = FIG / "04_fig1_conversao_territorio.png"
    fig.savefig(out, dpi=300, facecolor="white")
    print(out)


if __name__ == "__main__":
    main()
