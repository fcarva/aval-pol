"""08 — Figura da teoria da mudança da LICC, no formato de árvore do J-PAL usado nos slides da disciplina
(TdM [s.11]; M03 [s.11]): problema em vermelho, insumos e atividades em laranja, produtos em amarelo,
resultados intermediários em verde e resultado final em azul. As hipóteses H1–H3 dos autores aparecem como
premissas nos elos (M03 [s.33–34]); o traço tracejado marca elo sem dado público.

Conteúdo: notas/desenho/03-teoria-da-mudanca-e-hipoteses.md, § 1. Não lê dados.
Saída: analise/figuras/08_teoria_da_mudanca.png (300 dpi).
Uso: python analise/08_figura_teoria_da_mudanca.py
"""
from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

RAIZ = Path(__file__).resolve().parents[1]
SAIDA = RAIZ / "analise" / "figuras" / "08_teoria_da_mudanca.png"

plt.rcParams.update({"font.family": "Liberation Serif", "font.size": 8.5})

TINTA = "#1f1f1f"
# (preenchimento, borda) por componente, nas cores do slide do J-PAL
COR = {
    "problema": ("#f6d5d3", "#b03a2e"),
    "atividade": ("#fde3c8", "#c8641a"),
    "produto": ("#fff1c2", "#b8930b"),
    "intermediario": ("#dcecd6", "#2f7d3b"),
    "final": ("#d3e3f3", "#1f5f99"),
}
PREMISSA = ("#ffffff", "#555555")


def caixa(ax, x, y, w, h, titulo, sub, tipo, fs=8.5):
    fundo, borda = COR[tipo]
    ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h, boxstyle="round,pad=0.010,rounding_size=0.016",
                                fc=fundo, ec=borda, lw=1.0))
    if titulo and sub:
        ax.text(x, y + h * 0.20, titulo, ha="center", va="center", fontsize=fs, fontweight="bold", color=TINTA)
        ax.text(x, y - h * 0.18, sub, ha="center", va="center", fontsize=fs - 0.8, color=TINTA, linespacing=1.1)
    else:
        ax.text(x, y, titulo or sub, ha="center", va="center", fontsize=fs, color=TINTA, linespacing=1.15)


def seta(ax, p0, p1, tracejada=False):
    ax.add_patch(FancyArrowPatch(p0, p1, arrowstyle="-|>", mutation_scale=9, lw=0.9, color="#444444",
                                 linestyle=(0, (3, 2)) if tracejada else "-", shrinkA=0, shrinkB=0))


def premissa(ax, x, y, rotulo, texto, cor):
    ax.add_patch(FancyBboxPatch((x, y - 0.021), 0.225, 0.042, boxstyle="round,pad=0.005,rounding_size=0.010",
                                fc="#ffffff", ec=cor, lw=1.0, ls=(0, (2, 1.5))))
    ax.text(x + 0.008, y, rotulo, ha="left", va="center", fontsize=8.3, fontweight="bold", color=cor)
    ax.text(x + 0.052, y, texto, ha="left", va="center", fontsize=7.1, color=TINTA, linespacing=1.1)


def rotulo_camada(ax, y, texto, tipo):
    ax.text(0.012, y, texto, ha="left", va="center", fontsize=7.2, color=COR[tipo][1], fontweight="bold",
            linespacing=1.05)


def main() -> None:
    fig = plt.figure(figsize=(6.3, 7.4))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    xc, xe, xd = 0.445, 0.295, 0.595   # eixo, coluna esquerda, coluna direita
    w, W, h = 0.235, 0.55, 0.062        # caixa de coluna, caixa larga, altura
    y = {"prob": 0.945, "ins": 0.852, "a12": 0.752, "p1": 0.652, "a34": 0.552, "p23": 0.452,
         "ri": 0.342, "fin": 0.232}

    for chave, texto, tipo in [("prob", "PROBLEMA", "problema"), ("ins", "INSUMOS", "atividade"),
                               ("a12", "ATIVIDADES\n(entrada)", "atividade"), ("p1", "PRODUTO\n(oferta)", "produto"),
                               ("a34", "ATIVIDADES\n(financiamento)", "atividade"),
                               ("p23", "PRODUTOS\n(participação)", "produto"),
                               ("ri", "RESULTADOS\nINTERMEDIÁRIOS", "intermediario"),
                               ("fin", "RESULTADO\nFINAL", "final")]:
        rotulo_camada(ax, y[chave], texto, tipo)

    caixa(ax, xc, y["prob"], W, h, None, "Baixa e desigual capacidade de financiar a produção\n"
          "e a oferta cultural fora do circuito consolidado", "problema")
    caixa(ax, xc, y["ins"], W, h, None, "Teto de renúncia de ICMS (imposto que a população deixa de arrecadar)\n"
          "SECULT, pareceristas, CAP e SEFAZ · plataforma Mapa Cultural", "atividade", fs=8)
    caixa(ax, xe, y["a12"], w, h, "A1 Inscrição", "quem decide: agente cultural", "atividade")
    caixa(ax, xd, y["a12"], w, h, "A2 Parecer e CAP", "quem decide: SECULT e CAP", "atividade")
    caixa(ax, xc, y["p1"], 0.40, h, "P1 Cardápio de projetos habilitados", "habilitação binária, sem nota nem ranking",
          "produto")
    caixa(ax, xe, y["a34"], w, h, "A3 Escolha e termo", "quem decide: empresa", "atividade")
    caixa(ax, xd, y["a34"], w, h, "A4 Validação até o teto", "quem decide: ordem na SEFAZ", "atividade")
    caixa(ax, xd, y["p23"], w, h, "P2 Projetos patrocinados", "captação por projeto e empresa", "produto")
    caixa(ax, xe, y["p23"], w, h, "P3 Projetos executados", "com contrapartidas de acesso", "produto")
    caixa(ax, xe, y["ri"], w, 0.07, "RI1 Bens culturais", "de acesso público (gratuidade,\nacessibilidade, território)",
          "intermediario")
    caixa(ax, xd, y["ri"], w, 0.07, "RI2 Quem executa", "se diversifica e fica\nmais capaz", "intermediario")
    caixa(ax, xc, y["fin"], W, h, None, "Acesso maior e menos desigual da população à cultura;\n"
          "setor cultural mais capaz de se financiar", "final")

    b, m = h / 2 + 0.01, w / 2 + 0.01   # meia altura e meia largura com a margem do contorno
    seta(ax, (xc, y["prob"] - b), (xc, y["ins"] + b))
    seta(ax, (xe, y["ins"] - b), (xe, y["a12"] + b), tracejada=True)        # quem se inscreve: não publicado
    seta(ax, (xe + m, y["a12"]), (xd - m, y["a12"]), tracejada=True)        # inscritos → parecer: não publicado
    seta(ax, (xd, y["a12"] - b), (xc + 0.07, y["p1"] + b))
    seta(ax, (xc - 0.07, y["p1"] - b), (xe, y["a34"] + b))
    seta(ax, (xe + m, y["a34"]), (xd - m, y["a34"]))
    seta(ax, (xd, y["a34"] - b), (xd, y["p23"] + b))
    seta(ax, (xd - m, y["p23"]), (xe + m, y["p23"]))
    seta(ax, (xe, y["p23"] - b), (xe, y["ri"] + 0.045), tracejada=True)     # benefício: não agregado
    seta(ax, (xe + 0.06, y["p23"] - b), (xd - 0.06, y["ri"] + 0.045))
    seta(ax, (xe, y["ri"] - 0.045), (xc - 0.08, y["fin"] + b))
    seta(ax, (xd, y["ri"] - 0.045), (xc + 0.08, y["fin"] + b))

    xp, roxo = 0.765, "#7d3c98"
    premissa(ax, xp, y["a12"], "H3", "Atrito na entrada: quem\nconsegue se inscrever?", roxo)
    premissa(ax, xp, y["p1"], "H2", "Poucos passam: habilita\n1,1 a 1,9 vez o teto", roxo)
    premissa(ax, xp, y["a34"] + 0.030, "H1a", "Escolha da empresa por\nmarca e visibilidade?", roxo)
    premissa(ax, xp, y["a34"] - 0.030, "H2", "Racionamento pela\nordem de validação", roxo)
    premissa(ax, xp, y["ri"], "H1b", "Adicionalidade: o bem\nexistiria sem a LICC?", roxo)

    ax.plot([0.03, 0.97], [0.17, 0.17], color="#bbbbbb", lw=0.6)
    seta(ax, (0.04, 0.14), (0.10, 0.14), tracejada=True)
    ax.text(0.115, 0.14, "elo sem dado público (inscritos não publicados; público e gratuidade não agregados)",
            ha="left", va="center", fontsize=7.3, color=TINTA)
    ax.add_patch(FancyBboxPatch((0.045, 0.100), 0.05, 0.02, boxstyle="round,pad=0.004,rounding_size=0.008",
                                fc="#ffffff", ec=roxo, lw=1.0, ls=(0, (2, 1.5))))
    ax.text(0.115, 0.11, "premissa do elo tratada como hipótese dos autores (teoria negativa do programa)",
            ha="left", va="center", fontsize=7.3, color=TINTA)
    ax.text(0.04, 0.062, "Quem decide em cada elo segue os anéis do licc.gov: governo (SECULT, CAP, SEFAZ),\n"
            "capital (empresas), execução (proponentes) e população (financiadora indireta e beneficiária final).",
            ha="left", va="center", fontsize=7.1, color="#444444", linespacing=1.15)

    SAIDA.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(SAIDA, dpi=300, facecolor="white")
    print(SAIDA)


if __name__ == "__main__":
    main()
