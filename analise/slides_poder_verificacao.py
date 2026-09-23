"""Verificacao numerica dos exemplos de poder estatistico dos slides da disciplina.

Fontes (material da disciplina, raiz do projeto):
- PECO5046-6046_Amostragem_e_poder_estatistico.pdf
    formula do EMD sem conglomerados: PDF p.23 [slide 24]
    exemplo Bolsa Capixaba (curvas EMD x n, alfa=0,05, poder=80%): PDF p.26-29 [slide 26]
- wp26-power-calculation.pdf (Djimeu e Houndolo, 2016, 3ie WP 26)
    7.1.1 e 7.1.2: PDF p.30-31 (impressas 21-22)
    7.2.1 e 7.2.2: PDF p.35-37 (impressas 26-28)

O objetivo e apenas conferir que as formulas transcritas em
notas/disciplina/01-slides-e-guias.md reproduzem os numeros impressos no material.
Saida: analise/tabelas/slides_poder_verificacao.csv
"""
from math import sqrt
from pathlib import Path

import pandas as pd
from scipy.stats import norm

RAIZ = Path(__file__).resolve().parents[1]
SAIDA = RAIZ / "analise" / "tabelas" / "slides_poder_verificacao.csv"

Z_ALFA = norm.ppf(1 - 0.05 / 2)   # t_{alfa/2} para alfa = 5%, bicaudal (aprox. normal)
Z_PODER = norm.ppf(0.80)          # t_{1-beta} para poder = 80%


def emd_individual(n, P=0.5, sigma=1.0, ta=Z_ALFA, tb=Z_PODER, r2=0.0):
    """EMD sem conglomerados (slide 24; WP26 7.1.1/7.1.2 quando r2 > 0)."""
    return (ta + tb) * sigma * sqrt((1.0 / (P * (1 - P) * n)) * (1 - r2))


def emd_conglomerado(J, m, rho, P=0.5, sigma=1.0, ta=Z_ALFA, tb=Z_PODER, r2=0.0):
    """EMD com conglomerados (WP26 7.2.1/7.2.2): J conglomerados, m individuos por conglomerado."""
    return (ta + tb) / sqrt(P * (1 - P) * J) * sigma * sqrt((rho + (1 - rho) / m) * (1 - r2))


linhas = []

# 1) Bolsa Capixaba: pontos rotulados nos graficos (EMD em desvios-padrao, P = 0,5)
rotulos = [
    ("Inseguranca alimentar", 1200, 0.16),
    ("Inseguranca de renda", 1200, 0.16),
    ("Qualidade de vida: dominio psicologico", 1200, 0.16),
    ("Locus de controle", 1200, 0.16),
    ("Gasto familiar per capita com alimentos", 996, 0.18),
    ("Gasto familiar per capita com moradia", 1125, 0.17),
    ("Renda familiar per capita", 1147, 0.17),
]
for nome, n, emd_slide in rotulos:
    linhas.append({
        "exemplo": "Bolsa Capixaba (AMO p.26-29 [s.26])",
        "caso": nome,
        "parametros": f"n={n}; P=0,5; alfa=0,05; poder=0,80; sigma=1 (EMD em DP)",
        "valor_no_material": emd_slide,
        "valor_recalculado": round(emd_individual(n), 4),
    })
# extremos das curvas (aprox. 300 e 3000 no eixo; valores lidos no grafico ~0,32 e ~0,10)
for n, lido in [(300, 0.32), (3000, 0.10)]:
    linhas.append({
        "exemplo": "Bolsa Capixaba (AMO p.26-29 [s.26])",
        "caso": f"extremo da curva n={n}",
        "parametros": "P=0,5; alfa=0,05; poder=0,80; sigma=1",
        "valor_no_material": lido,
        "valor_recalculado": round(emd_individual(n), 4),
    })

# 2) WP26, exemplos numericos (t1 e t2 como impressos no manual)
linhas.append({
    "exemplo": "WP26 7.1.1 (PDF p.30)", "caso": "aprendizagem Kisumu, sem covariadas",
    "parametros": "t1=1,96; t2=0,84; sigma=2400; P=0,5; n=1000",
    "valor_no_material": 425.7,
    "valor_recalculado": round(emd_individual(1000, sigma=2400, ta=1.96, tb=0.84), 1),
})
linhas.append({
    "exemplo": "WP26 7.1.2 (PDF p.31)", "caso": "aprendizagem Kisumu, R2=0,5",
    "parametros": "t1=1,96; t2=0,84; sigma=2400; P=0,5; n=1000; R2=0,5",
    "valor_no_material": 301,
    "valor_recalculado": round(emd_individual(1000, sigma=2400, ta=1.96, tb=0.84, r2=0.5), 1),
})
linhas.append({
    "exemplo": "WP26 7.2.1 (PDF p.36)", "caso": "farmer field schools, conglomerados",
    "parametros": "t1=2,58; t2=1,28; P=0,5; J=240; m=20; sigma=0,47; rho=0,037",
    "valor_no_material": 0.0683,
    "valor_recalculado": round(emd_conglomerado(240, 20, 0.037, sigma=0.47, ta=2.58, tb=1.28), 4),
})
linhas.append({
    "exemplo": "WP26 7.2.2 (PDF p.37)", "caso": "farmer field schools, conglomerados, R2=0,4",
    "parametros": "t1=2,58; t2=1,28; P=0,5; J=240; m=20; sigma=0,47; rho=0,037; R2=0,4",
    "valor_no_material": 0.053,
    "valor_recalculado": round(emd_conglomerado(240, 20, 0.037, sigma=0.47, ta=2.58, tb=1.28, r2=0.4), 4),
})

tab = pd.DataFrame(linhas)
SAIDA.parent.mkdir(parents=True, exist_ok=True)
tab.to_csv(SAIDA, index=False, encoding="utf-8")
print(f"z_(alfa/2)={Z_ALFA:.4f}  z_(1-beta)={Z_PODER:.4f}  soma={Z_ALFA + Z_PODER:.4f}")
print(tab.to_string(index=False))
