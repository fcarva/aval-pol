"""
Replica os exemplos numéricos do cap. 7 de White e Raitzer (2017), "Impact
Evaluation of Development Interventions: A Practical Guide" (ADB), para conferir
a transcrição das fórmulas usada em notas/disciplina/04-itau-magenta-adb.md, e
tabula a diluição do efeito de intenção de tratar (ITT) pela taxa de
participação (eq. 3.2 do mesmo guia), ponto relevante para a LICC, em que a
habilitação é a "oferta" e a captação é a "participação".

Fontes (páginas impressas do guia; página do PDF = impressa + 14):
- eq. 7.1, p. 121: MES = (t_{a/2} + t_{1-b}) * sigma_y * sqrt(1 / (P(1-P) n))
- eq. 7.2, p. 122: n = (t_{a/2} + t_{1-b})^2 sigma_y^2 / (MES^2 P(1-P))
- eq. 7.4-7.5, p. 124: DE = 1 + (m-1) rho ; n_cong = n * DE
- exemplo Andhra Pradesh, p. 122: sigma = Rs12.000, MES = Rs1.500 (10% de
  Rs15.000), alfa = 5%, poder 80% => n = 2.000 (MES 1.504); MES Rs750 => n = 8.000
  (MES 752).
- exemplo por conglomerados, p. 124: 50 conglomerados x 40 obs., rho = 0,2 =>
  MES "quase Rs7.000"; MES Rs1.500 com 40 obs./conglomerado => 445 conglomerados
  (17.800 obs.).
- regra de bolso, p. 127: n por braço = 16 / mes^2 (mes em desvios-padrão).
- eq. 3.2, p. 44: ITT = ATT x taxa de participação (PR).

Aproximação normal (z em vez de t), como é usual em cálculo de poder com
amostras grandes; o guia diz que t ~ 2 a 5% (p. 119).

Saída: analise/tabelas/adb_replicacao_poder.csv
Uso:   python analise/adb_poder_replicacao.py
"""

from __future__ import annotations

import math
import os

import pandas as pd
from scipy.stats import norm

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TAB = os.path.join(RAIZ, "analise", "tabelas")
os.makedirs(TAB, exist_ok=True)


def fator(alfa: float = 0.05, poder: float = 0.80) -> float:
    """(z_{a/2} + z_{poder})."""
    return norm.ppf(1 - alfa / 2) + norm.ppf(poder)


def mes(sigma: float, n: float, p: float = 0.5, de: float = 1.0, **kw) -> float:
    """Eq. 7.1 (com efeito de desenho DE opcional, eq. 7.5)."""
    return fator(**kw) * sigma * math.sqrt(de / (p * (1 - p) * n))


def n_req(sigma: float, efeito: float, p: float = 0.5, de: float = 1.0, **kw) -> float:
    """Eq. 7.2 / 7.5: tamanho total da amostra (tratados + comparação)."""
    return fator(**kw) ** 2 * sigma**2 / (efeito**2 * p * (1 - p)) * de


linhas = []

# Exemplo 1 (p. 122): desenho simples
n1 = n_req(12000, 1500)
linhas.append(("ADB p.122: n p/ MES Rs1.500", "livro: 2.000", round(n1)))
linhas.append(("ADB p.122: MES com n=2.000", "livro: 1.504", round(mes(12000, 2000))))
n2 = n_req(12000, 750)
linhas.append(("ADB p.122: n p/ MES Rs750", "livro: 8.000", round(n2)))
linhas.append(("ADB p.122: MES com n=8.000", "livro: 752", round(mes(12000, 8000))))

# Exemplo 2 (p. 124): conglomerados, rho = 0,2, m = 40
de40 = 1 + (40 - 1) * 0.2
linhas.append(("ADB p.124: MES 50 cong. x 40 obs.", "livro: quase 7.000",
               round(mes(12000, 2000, de=de40))))
n3 = n_req(12000, 1500, de=de40)
linhas.append(("ADB p.124: obs. p/ MES Rs1.500 (m=40)", "livro: 17.800", round(n3)))
linhas.append(("ADB p.124: conglomerados (n/40)", "livro: 445", round(n3 / 40)))

# Regra de bolso (p. 127): n por braço = 16/mes^2
for d in (0.5, 0.1):
    linhas.append((f"ADB p.127: regra 16/mes^2, mes={d} (por braço)",
                   "livro: 64" if d == 0.5 else "livro: 1.600",
                   round(16 / d**2)))
    linhas.append((f"conferência exata z, mes={d} (por braço)", "",
                   round(n_req(1.0, d) / 2)))

# Diluição do ITT (eq. 3.2, p. 44): para detectar um ATT de 0,2 dp quando só
# uma fração PR dos habilitados participa, o efeito observável na comparação
# por intenção de tratar é 0,2 x PR, e n cresce com 1/PR^2.
for pr in (1.0, 0.8, 0.7, 0.6, 0.5):
    linhas.append((f"ITT: n total p/ ATT=0,2 dp com PR={pr}", "derivado eq. 3.2 + 7.2",
                   round(n_req(1.0, 0.2 * pr))))

df = pd.DataFrame(linhas, columns=["calculo", "referencia", "valor_reproduzido"])
saida = os.path.join(TAB, "adb_replicacao_poder.csv")
df.to_csv(saida, index=False)
print(df.to_string(index=False))
print(f"\nsalvo em {saida}")
