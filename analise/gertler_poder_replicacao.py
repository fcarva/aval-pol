"""
Replica os quadros de poder estatístico de Gertler et al. (2018, cap. 15) com a
fórmula dos slides PECO5046-6046 (Amostragem e poder, slides 23, 24 e 28) e
tabula os estados de tramitação dos habilitados da LICC por ciclo, para uso na
nota notas/disciplina/03-gertler.md.

Fontes:
- Gertler et al. (2018), Avaliação de Impacto na Prática, 2. ed., quadros 15.2
  (p. 311), 15.3 (p. 312), 15.4 (p. 313), 15.5 (p. 316) e 15.6 (p. 317).
  Parâmetros do livro: sigma = US$ 8 (p. 311), rho = 0,04 (p. 316),
  alfa = 5%, poder 0,9 (quadro 15.2) ou 0,8 (demais).
- Slides PECO5046-6046_Amostragem_e_poder_estatistico.pdf:
  n = (t_{a/2} + t_{1-b})^2 sigma^2 / (EMD^2 P(1-P))            (slide 23)
  EMD = (t_{a/2} + t_{1-b}) sigma sqrt(1 / (P(1-P) n))           (slide 24)
  n_cong = n * (1 + (m - 1) rho)                                  (slide 28)
- dados/licc/habilitados/habilitados-{2022..2026}.csv (transcrição dos anexos
  da SECULT; coluna `status` como publicada na lista de habilitados).

Saídas:
- analise/tabelas/gertler_replicacao_poder.csv
- analise/tabelas/licc_status_por_ciclo.csv
- analise/tabelas/licc_emd_ilustrativo.csv
- analise/tabelas/licc_captados_2025_totais.csv

Uso: python analise/gertler_poder_replicacao.py
"""

from __future__ import annotations

import glob
import math
import os

import pandas as pd
from scipy.stats import norm

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TAB = os.path.join(RAIZ, "analise", "tabelas")
os.makedirs(TAB, exist_ok=True)

ALFA = 0.05


def k(poder: float, alfa: float = ALFA) -> float:
    """(z_{1-a/2} + z_{poder}); aproximação normal dos t dos slides."""
    return norm.ppf(1 - alfa / 2) + norm.ppf(poder)


def n_por_grupo(emd: float, sigma: float, poder: float) -> float:
    """Slide 23 com P = 0,5: n_total = 4 k^2 sigma^2 / EMD^2; por grupo = metade."""
    return 2 * k(poder) ** 2 * sigma**2 / emd**2


def emd(n_t: int, n_c: int, sigma: float, poder: float) -> float:
    """Slide 24 escrito para grupos desiguais: EMD = k sigma sqrt(1/n_t + 1/n_c)."""
    return k(poder) * sigma * math.sqrt(1 / n_t + 1 / n_c)


def replicar_gertler() -> pd.DataFrame:
    linhas = []
    sigma = 8.0  # Gertler et al. 2018, p. 311

    # Quadros 15.2 (poder 0,9) e 15.3 (poder 0,8): sem conglomerados.
    livro = {
        ("15.2", 0.9): {1: 1344, 2: 336, 3: 150},
        ("15.3", 0.8): {1: 1004, 2: 251, 3: 112},
    }
    for (quadro, poder), valores in livro.items():
        for d, n_livro in valores.items():
            n = n_por_grupo(d, sigma, poder)
            linhas.append(
                dict(quadro=quadro, poder=poder, emd=d, m=None, rho=None,
                     conglomerados_total=None, n_calc_por_grupo=round(n, 1),
                     n_livro_por_grupo=n_livro,
                     dif=round(n - n_livro, 1))
            )

    # Quadro 15.4: variável binária, taxa de base 5%, aumento de 1, 2, 3 p.p.
    # O livro não explicita a fórmula; testamos a variância p0(1-p0).
    for d_pp, n_livro in {1: 7257, 2: 1815, 3: 807}.items():
        p0 = 0.05
        n = 2 * k(0.8) ** 2 * p0 * (1 - p0) / (d_pp / 100) ** 2
        linhas.append(
            dict(quadro="15.4 (var = p0(1-p0))", poder=0.8, emd=d_pp / 100,
                 m=None, rho=None, conglomerados_total=None,
                 n_calc_por_grupo=round(n, 1), n_livro_por_grupo=n_livro,
                 dif=round(n - n_livro, 1))
        )

    # Quadros 15.5 e 15.6: conglomerados, rho = 0,04 (p. 316), poder 0,8.
    rho = 0.04
    casos = [
        ("15.5", 1, 100, 102, 10200),
        ("15.5", 2, 90, 7, 630),
        ("15.5", 3, 82, 3, 246),
        ("15.6", 2, 30, 50, 1500),
        ("15.6", 2, 58, 13, 754),
        ("15.6", 2, 81, 8, 648),
        ("15.6", 2, 90, 7, 630),
        ("15.6", 2, 120, 5, 600),
    ]
    for quadro, d, cong, m, total_livro in casos:
        n_ind = n_por_grupo(d, sigma, 0.8) * (1 + (m - 1) * rho)  # por grupo
        cong_por_grupo = n_ind / m
        linhas.append(
            dict(quadro=quadro, poder=0.8, emd=d, m=m, rho=rho,
                 conglomerados_total=cong,
                 n_calc_por_grupo=round(n_ind, 1),
                 n_livro_por_grupo=total_livro / 2,
                 dif=round(n_ind - total_livro / 2, 1),
                 cong_necessarios_por_grupo=round(cong_por_grupo, 1),
                 cong_livro_por_grupo=cong / 2)
        )
    return pd.DataFrame(linhas)


def status_licc() -> pd.DataFrame:
    regs = []
    for f in sorted(glob.glob(os.path.join(RAIZ, "dados", "licc", "habilitados", "habilitados-*.csv"))):
        ciclo = int(os.path.basename(f).split("-")[1].split(".")[0])
        d = pd.read_csv(f)
        c = d["status"].value_counts(dropna=False)
        va = pd.to_numeric(d["valor_autorizado"], errors="coerce")
        regs.append(dict(ciclo=ciclo, habilitados=len(d),
                         soma_valor_autorizado=round(float(va.sum()), 2),
                         cobertura_valor_autorizado=int(va.notna().sum()),
                         concluido=int(c.get("concluido", 0)),
                         em_execucao=int(c.get("em_execucao", 0)),
                         captando=int(c.get("captando", 0)),
                         captacao_expirada=int(c.get("captacao_expirada", 0)),
                         status_ausente=int(d["status"].isna().sum()),
                         fonte="dados/licc/habilitados/" + os.path.basename(f)))
    return pd.DataFrame(regs)


def captados_2025() -> pd.DataFrame:
    """Totais do anexo 'Recurso financeiro captado 2025' (ano-calendário)."""
    c = pd.read_csv(os.path.join(RAIZ, "dados", "licc", "oficial", "captados-2025.csv"))
    return pd.DataFrame([dict(
        projetos=len(c),
        soma_valor_autorizado=round(float(c["valor_autorizado"].sum()), 2),
        soma_valor_captado=round(float(c["valor_captado"].sum()), 2),
        projetos_captado_igual_500k=int((c["valor_captado"] == 500000).sum()),
        projetos_autorizado_igual_500k=int((c["valor_autorizado"] == 500000).sum()),
        fonte="dados/licc/oficial/captados-2025.csv")])


def emd_ilustrativo(st: pd.DataFrame) -> pd.DataFrame:
    """EMD em desvios-padrão (sigma = 1) comparando 'captou' x 'não captou'.

    Hipótese de trabalho, a verificar: concluido + em_execucao = captou o mínimo
    exigido (art. 47 da IN 001/2025: 35%); captacao_expirada = não captou;
    captando = desfecho em aberto, excluído.
    """
    fechados = st[st["ciclo"] <= 2024].copy()
    fechados["tratados"] = fechados["concluido"] + fechados["em_execucao"]
    fechados["comparacao"] = fechados["captacao_expirada"]
    linhas = []
    for _, r in fechados.iterrows():
        for poder in (0.8, 0.9):
            linhas.append(dict(recorte=f"ciclo {int(r.ciclo)}", n_t=int(r.tratados),
                               n_c=int(r.comparacao), poder=poder,
                               emd_dp=round(emd(int(r.tratados), int(r.comparacao), 1.0, poder), 3)))
    nt, nc = int(fechados["tratados"].sum()), int(fechados["comparacao"].sum())
    for poder in (0.8, 0.9):
        linhas.append(dict(recorte="ciclos 2022-2024 empilhados", n_t=nt, n_c=nc,
                           poder=poder, emd_dp=round(emd(nt, nc, 1.0, poder), 3)))
    return pd.DataFrame(linhas)


if __name__ == "__main__":
    rep = replicar_gertler()
    rep.to_csv(os.path.join(TAB, "gertler_replicacao_poder.csv"), index=False)
    st = status_licc()
    st.to_csv(os.path.join(TAB, "licc_status_por_ciclo.csv"), index=False)
    em = emd_ilustrativo(st)
    em.to_csv(os.path.join(TAB, "licc_emd_ilustrativo.csv"), index=False)
    cap = captados_2025()
    cap.to_csv(os.path.join(TAB, "licc_captados_2025_totais.csv"), index=False)
    pd.set_option("display.width", 200)
    print(rep.to_string(index=False))
    print()
    print(st.to_string(index=False))
    print()
    print(em.to_string(index=False))
    print()
    print(cap.to_string(index=False))
