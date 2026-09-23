"""
Efeito mínimo detectável (EMD/MDE) e tamanho amostral para a proposta de
avaliação de impacto da LICC — conglomerados, covariadas, proporções e painel
(diferenças em diferenças), conforme o material da disciplina e a literatura
indicada na nota notas/disciplina/05-poder-validade-agregacao.md.

Fontes das fórmulas (página do documento impresso; "PDF p." quando diferente):
- Djimeu, E. W.; Houndolo, D.-G. (2016). 3ie Working Paper 26.
  MDE genérico (p. 12); e = sqrt(2 sigma^2 / n) (p. 13); efeito de desenho
  e2_TSS = e2_SRS [1 + rho (m - 1)] (p. 15); fórmulas 7.1.1-7.1.5 (p. 21-25)
  e 7.2.1-7.2.4 (p. 26-30). PDF p. = p. impressa + 9.
- Slides PECO5046-6046 "Amostragem e poder estatístico" (Giuberti, 2026):
  n (slide 23), EMD (slide 24), n com conglomerados e efeito do desenho
  (slide 28).
- McKenzie, D. (2012). J. Dev. Econ. 99(2): 210-221 (versão WPS 5639, 2011):
  variâncias POST, DiD e ANCOVA com m rodadas pré e r pós, eq. (7), (8), (11)
  da versão WPS 5639.
- Burlig, F.; Preonas, L.; Woerman, M. (2020). J. Dev. Econ. 144: 102458
  (versão NBER WP 26250, 2019): MDE robusto à correlação serial, eq. (2);
  forma de McKenzie na notação deles, eq. (3).
- Gelman, A.; Carlin, J. (2014). Perspect. Psychol. Sci. 9(6): 641-651:
  erros tipo S e tipo M (razão de exagero), usados para quantificar a
  "truth inflation" de Reinhart (2015, cap. 2, p. 23-25).

Saídas (analise/tabelas/):
- 05_poder_verificacao.csv          reprodução dos exemplos numéricos das fontes
- 05_poder_mde_municipal_did.csv    cenários ilustrativos, painel municipal (J = 78)
- 05_poder_deff_proponente.csv      projetos por proponente e efeito de desenho
- 05_poder_tipo_m.csv               razão de exagero e erro de sinal por poder

Uso: python analise/05_poder_mde.py

Todos os parâmetros de variância, CCI (rho), autocorrelação e P nos cenários
LICC são HIPÓTESES ILUSTRATIVAS, não estimativas: a nota explica onde buscá-los.
Os únicos números da LICC usados aqui vêm de dados/licc/habilitados/*.csv.
"""

from __future__ import annotations

import glob
import math
import os
import unicodedata

import pandas as pd
from scipy.stats import norm
from scipy.stats import t as tdist

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TAB = os.path.join(RAIZ, "analise", "tabelas")
os.makedirs(TAB, exist_ok=True)


# ---------------------------------------------------------------------------
# Multiplicador (t_{1-alpha/2} + t_{1-beta})
# ---------------------------------------------------------------------------
def multiplicador(alpha: float = 0.05, poder: float = 0.80,
                  bicaudal: bool = True, gl: int | None = None) -> float:
    """Soma dos valores críticos que multiplica o erro-padrão no MDE.

    MDE = (t_{1-alpha/2} + t_{1-beta}) * e   (3ie WP26, p. 12; Bloom, 1995).
    Com gl=None usa a normal (z); com gl inteiro usa t de Student com gl graus
    de liberdade (WP26, notas das tabelas 2-8: os t dependem do tamanho
    amostral). Teste unicaudal só com justificativa prévia (WP26, p. 8-9).
    """
    a = alpha / 2 if bicaudal else alpha
    if gl is None:
        return norm.ppf(1 - a) + norm.ppf(poder)
    return tdist.ppf(1 - a, gl) + tdist.ppf(poder, gl)


# ---------------------------------------------------------------------------
# Aleatorização / comparação individual (WP26, seção 7.1)
# ---------------------------------------------------------------------------
def mde_simples(sigma: float, n: float, P: float = 0.5, R2: float = 0.0,
                alpha: float = 0.05, poder: float = 0.80,
                bicaudal: bool = True, gl: int | None = None) -> float:
    """MDE para resultado contínuo, n TOTAL, fração P tratada.

    delta = M * sigma * sqrt( (1 - R2) / (P (1 - P) n) )
    (WP26 7.1.1 e 7.1.2, p. 21-22; slide 24 com R2 = 0).
    R2 = fração da variância do resultado explicada por covariadas de linha
    de base (WP26, nota 3, p. 22).
    """
    M = multiplicador(alpha, poder, bicaudal, gl)
    return M * sigma * math.sqrt((1 - R2) / (P * (1 - P) * n))


def n_simples(delta: float, sigma: float, P: float = 0.5, R2: float = 0.0,
              alpha: float = 0.05, poder: float = 0.80,
              bicaudal: bool = True) -> float:
    """Tamanho amostral TOTAL (inversa de mde_simples; slide 23; WP26 p. 21-22)."""
    M = multiplicador(alpha, poder, bicaudal)
    return (M ** 2) * sigma ** 2 * (1 - R2) / (delta ** 2 * P * (1 - P))


def mde_binario(p0: float, n: float, T: float = 0.5, R2: float = 0.0,
                alpha: float = 0.05, poder: float = 0.80,
                bicaudal: bool = True) -> float:
    """MDE (em pontos de proporção) para resultado binário.

    delta = M * sqrt( p0 (1 - p0) (1 - R2) / (T (1 - T) n) )
    (WP26 7.1.3 e 7.1.4, p. 23-24). ATENÇÃO à notação do WP26: nesta seção
    P é a prevalência sem o programa e T a fração tratada (em 7.1.1 P é a
    fração tratada). Aqui: p0 = prevalência, T = fração tratada.
    """
    M = multiplicador(alpha, poder, bicaudal)
    return M * math.sqrt(p0 * (1 - p0) * (1 - R2) / (T * (1 - T) * n))


def pessoas_ano_taxas(mu0: float, mu1: float, alpha: float = 0.05,
                      poder: float = 0.80, bicaudal: bool = True) -> float:
    """Pessoas-ano por grupo para comparar taxas (WP26 7.1.5, p. 25):
    R = (z1 + z2)^2 (mu0 + mu1) / (mu0 - mu1)^2."""
    M = multiplicador(alpha, poder, bicaudal)
    return M ** 2 * (mu0 + mu1) / (mu0 - mu1) ** 2


# ---------------------------------------------------------------------------
# Conglomerados (WP26, seção 7.2; slide 28)
# ---------------------------------------------------------------------------
def efeito_desenho(m: float, icc: float, cv: float = 0.0) -> float:
    """Efeito do desenho 1 + (m - 1) rho (WP26 p. 15; slide 28).

    Com cv > 0 (coeficiente de variação do tamanho dos conglomerados) usa a
    aproximação 1 + ((cv^2 + 1) m - 1) rho, atribuída a Eldridge, Ashby e
    Kerry (2006) [VERIFICAR a forma exata no original]; cv = 0 recupera a
    fórmula do material da disciplina.
    """
    return 1 + ((cv ** 2 + 1) * m - 1) * icc


def mde_conglomerados(sigma: float, J: float, m: float, icc: float,
                      P: float = 0.5, R2: float = 0.0, alpha: float = 0.05,
                      poder: float = 0.80, bicaudal: bool = True,
                      gl: int | None = None) -> float:
    """MDE com J conglomerados NO TOTAL e m unidades por conglomerado.

    delta = M / sqrt(P (1 - P) J) * sigma * sqrt( [rho + (1 - rho)/m] (1 - R2) )
    (WP26 7.2.1 e 7.2.2, p. 26-27; no WP26 'n' = indivíduos por conglomerado).
    Equivale ao slide 28: n_total = n_simples * [1 + (m - 1) rho], pois
    sigma^2 [rho + (1 - rho)/m] / J = sigma^2 [1 + (m - 1) rho] / (m J).
    Observação: o WP26 aplica (1 - R2) ao termo inteiro (covariada de nível 1).
    """
    M = multiplicador(alpha, poder, bicaudal, gl)
    return (M / math.sqrt(P * (1 - P) * J)) * sigma * math.sqrt(
        (icc + (1 - icc) / m) * (1 - R2))


def J_conglomerados(delta: float, sigma: float, m: float, icc: float,
                    P: float = 0.5, R2: float = 0.0, alpha: float = 0.05,
                    poder: float = 0.80, bicaudal: bool = True) -> float:
    """Número TOTAL de conglomerados (inversa de mde_conglomerados)."""
    M = multiplicador(alpha, poder, bicaudal)
    return (M ** 2) * sigma ** 2 * (1 - R2) * (icc + (1 - icc) / m) / (
        delta ** 2 * P * (1 - P))


def J_hayes_bennett(mu0: float, mu1: float, m: float, k: float,
                    alpha: float = 0.05, poder: float = 0.80,
                    taxa: bool = False, bicaudal: bool = True) -> float:
    """Conglomerados POR GRUPO (Hayes e Bennett, 1999, via WP26 7.2.3-7.2.4).

    Proporções (p. 29): J = 1 + M^2 [mu0(1-mu0)/m + mu1(1-mu1)/m
                                     + k^2 (mu0^2 + mu1^2)] / (mu0 - mu1)^2
    Taxas (p. 30):      J = 1 + M^2 [(mu0 + mu1)/m + k^2 (mu0^2 + mu1^2)]
                                     / (mu0 - mu1)^2
    k = coeficiente de variação das proporções/taxas verdadeiras entre
    conglomerados (não é o CCI; ver Pagel et al., 2011, citado no WP26 nota 5).
    Para taxas, m é a exposição (pessoas-ano) por conglomerado.
    """
    M = multiplicador(alpha, poder, bicaudal)
    if taxa:
        termo = (mu0 + mu1) / m
    else:
        termo = mu0 * (1 - mu0) / m + mu1 * (1 - mu1) / m
    return 1 + M ** 2 * (termo + k ** 2 * (mu0 ** 2 + mu1 ** 2)) / (mu0 - mu1) ** 2


# ---------------------------------------------------------------------------
# Painel: McKenzie (2012) e Burlig, Preonas e Woerman (2020)
# ---------------------------------------------------------------------------
def var_mckenzie(sigma: float, n_por_grupo: float, m: int, r: int, rho: float,
                 estimador: str = "did") -> float:
    """Variância do efeito com m rodadas pré e r pós, autocorrelação constante
    rho, n unidades em cada grupo (McKenzie, 2012; eq. da versão WPS 5639):

    POST   (8):  2 sigma^2/n * (1 + (r-1) rho) / r
    DiD    (7):  2 sigma^2/n * [ (1 + (r-1) rho)/r - ((m+1) rho - 1)/m ]
                 = 2 sigma^2/n * (1 - rho)(m + r)/(m r)
    ANCOVA (11): 2 sigma^2/n * [ (1 + (r-1) rho)/r - m rho^2 / (1 + (m-1) rho) ]
    Aqui rho é a autocorrelação do RESULTADO entre rodadas (não o CCI).
    """
    base = 2 * sigma ** 2 / n_por_grupo
    post = (1 + (r - 1) * rho) / r
    if estimador == "post":
        return base * post
    if estimador == "did":
        return base * (post - ((m + 1) * rho - 1) / m)
    if estimador == "ancova":
        return base * (post - m * rho ** 2 / (1 + (m - 1) * rho))
    raise ValueError("estimador deve ser 'post', 'did' ou 'ancova'")


def n_mckenzie(delta: float, sigma: float, m: int, r: int, rho: float,
               estimador: str = "did", alpha: float = 0.05,
               poder: float = 0.80) -> float:
    """n por grupo tal que M * sqrt(Var) = delta (inversa de var_mckenzie)."""
    M = multiplicador(alpha, poder)
    v1 = var_mckenzie(sigma, 1.0, m, r, rho, estimador)  # variância com n = 1
    return M ** 2 * v1 / delta ** 2


def psi_ar1(sigma2_omega: float, phi: float, m: int, r: int) -> tuple:
    """Covariâncias médias (psi_B, psi_A, psi_X) de Burlig et al. (2020,
    Assumption 5) SOB A HIPÓTESE ILUSTRATIVA de erro idiossincrático AR(1):
    Cov(omega_t, omega_s) = sigma2_omega * phi^|t - s|.
    Pré: t = -m+1..0; pós: s = 1..r.
    A hipótese AR(1) é nossa, para gerar cenários; na prática os psi devem ser
    estimados em dados de painel pré-existentes (Burlig et al., 2020).
    """
    pre = list(range(-m + 1, 1))
    pos = list(range(1, r + 1))

    def media_pares(ts):
        pares = [(a, b) for i, a in enumerate(ts) for b in ts[i + 1:]]
        if not pares:
            return 0.0
        return sum(sigma2_omega * phi ** abs(a - b) for a, b in pares) / len(pares)

    psi_B = media_pares(pre)
    psi_A = media_pares(pos)
    psi_X = sum(sigma2_omega * phi ** abs(a - b) for a in pre for b in pos) / (m * r)
    return psi_B, psi_A, psi_X


def mde_did_bpw(J: int, P: float, m: int, r: int, sigma2_omega: float,
                psi_B: float = 0.0, psi_A: float = 0.0, psi_X: float = 0.0,
                alpha: float = 0.05, poder: float = 0.80,
                gl: int | None = None) -> float:
    """MDE de diferenças em diferenças com efeitos fixos de unidade e tempo,
    robusto a correlação serial arbitrária (Burlig, Preonas e Woerman, 2020,
    eq. 2 da versão NBER WP 26250):

    MDE = M * sqrt( 1/(P(1-P)J) * [ (m+r)/(m r) * sigma2_omega
                                    + (m-1)/m * psi_B + (r-1)/r * psi_A
                                    - 2 psi_X ] )

    J = unidades (ex.: municípios), P = fração tratada, m/r = períodos pré/pós.
    Com psi = 0 reduz-se à forma de McKenzie na notação dos autores (eq. 3).
    Os autores usam t com graus de liberdade ligados a J (t^J); aqui gl=None
    usa a normal [VERIFICAR gl exato no original].
    """
    M = multiplicador(alpha, poder, True, gl)
    v = (1 / (P * (1 - P) * J)) * (
        (m + r) / (m * r) * sigma2_omega + (m - 1) / m * psi_B
        + (r - 1) / r * psi_A - 2 * psi_X)
    return M * math.sqrt(v)


# ---------------------------------------------------------------------------
# Erros tipo S e tipo M ("truth inflation")
# ---------------------------------------------------------------------------
def tipo_s_m(efeito_verdadeiro: float, ep: float, alpha: float = 0.05) -> dict:
    """Poder, erro de sinal (tipo S) e razão de exagero (tipo M) de um
    estimador ~ N(D, ep^2) testado a nível alpha bicaudal (Gelman e Carlin,
    2014). Formaliza a "truth inflation" de Reinhart (2015, p. 23-25):
    entre os resultados significativos de um estudo de baixo poder, a
    magnitude estimada exagera sistematicamente o efeito verdadeiro.
    """
    lam = efeito_verdadeiro / ep
    z = norm.ppf(1 - alpha / 2)
    p_sup = 1 - norm.cdf(z - lam)          # significativo com sinal certo
    p_inf = norm.cdf(-z - lam)             # significativo com sinal trocado
    poder = p_sup + p_inf
    # E[|X| ; |X| > z] para X ~ N(lam, 1)
    e_sup = lam * p_sup + norm.pdf(z - lam)
    e_inf = -lam * p_inf + norm.pdf(z + lam)
    return {
        "poder": poder,
        "erro_tipo_S": p_inf / poder,
        "razao_exagero_tipo_M": (e_sup + e_inf) / poder / lam,
    }


# ---------------------------------------------------------------------------
# Rotinas de verificação e cenários
# ---------------------------------------------------------------------------
def verificacao() -> pd.DataFrame:
    """Reproduz os exemplos numéricos das fontes."""
    linhas = []

    def add(fonte, caso, publicado, calculado, obs=""):
        linhas.append({"fonte": fonte, "caso": caso, "publicado": publicado,
                       "calculado": round(calculado, 4), "obs": obs})

    # WP26 7.1.1 (p. 21): t1=1.96, t2=0.84 -> MDE = 425,7
    add("WP26 7.1.1 p.21", "MDE continuo, n=1000, P=0.5, sd=2400, a=.05 bic, poder .8",
        425.7, 2.80 * 2400 * math.sqrt(1 / (0.25 * 1000)), "t1+t2 = 2,80 (valores do texto)")
    add("WP26 7.1.1 p.21", "idem, t de Student gl=998", 425.7,
        mde_simples(2400, 1000, gl=998), "diferença de arredondamento")
    # WP26 7.1.2 (p. 22): R2 = 0.5 -> 301
    add("WP26 7.1.2 p.22", "idem com R2=0.5", 301,
        2.80 * 2400 * math.sqrt((1 / (0.25 * 1000)) * 0.5))
    # WP26 7.1.3 (p. 23): unicaudal t1=1.65, t2=0.84, P=0.03, T=0.5 -> 0,027
    add("WP26 7.1.3 p.23", "binario, p0=0.03, T=0.5, n=1000, unicaudal", 0.027,
        2.49 * math.sqrt(0.03 * 0.97 / (0.25 * 1000)))
    # WP26 7.1.4 (p. 24): n=991, R2=0.6 -> 0,017
    add("WP26 7.1.4 p.24", "binario com R2=0.6, n=991", 0.017,
        2.49 * math.sqrt(0.03 * 0.97 / (0.25 * 991) * (1 - 0.6)))
    # WP26 7.1.5 (p. 25): z1=2.58, z2=1.28, mu0=0.072, mu1=0.0432 -> 2.067
    add("WP26 7.1.5 p.25", "taxas: pessoas-ano por grupo", 2067,
        3.86 ** 2 * (0.072 + 0.0432) / (0.072 - 0.0432) ** 2,
        "diferença de arredondamento de mu0")
    # WP26 7.2.1 (p. 26-27): J=240, n=20, rho=0.037, sd=0.47, 2.58+1.28 -> 0,0683
    add("WP26 7.2.1 p.27", "conglomerados J=240 m=20 icc=.037 sd=.47 a=.01 poder .9",
        0.0683, (3.86 / math.sqrt(0.25 * 240)) * 0.47 * math.sqrt(0.037 + 0.963 / 20))
    add("WP26 7.2.1 p.27", "idem via funcao mde_conglomerados (z exatos)", 0.0683,
        mde_conglomerados(0.47, 240, 20, 0.037, alpha=0.01, poder=0.90))
    # WP26 7.2.2 (p. 28): + R2 = 0.4 -> 0,053
    add("WP26 7.2.2 p.28", "idem com R2=0.4", 0.053,
        (3.86 / math.sqrt(0.25 * 240)) * 0.47 * math.sqrt((0.037 + 0.963 / 20) * 0.6))
    # Slide 28 = WP26 7.2.1 (equivalência algébrica)
    n_tot = n_simples(0.0683, 0.47, alpha=0.01, poder=0.90) * efeito_desenho(20, 0.037)
    add("Slide 28 x WP26 7.2.1", "n_total pelo slide / 20 = J do WP26", 240,
        n_tot / 20, "equivalência: mesmo desenho, J ~ 240")
    # WP26 7.2.3 (p. 29-30): z 2.58+0.84, mu0=.25, mu1=.65, k=.25, n=50 -> 4
    M = 2.58 + 0.84
    Jb = 1 + M ** 2 * (0.25 * 0.75 / 50 + 0.65 * 0.35 / 50
                       + 0.25 ** 2 * (0.25 ** 2 + 0.65 ** 2)) / (0.25 - 0.65) ** 2
    add("WP26 7.2.3 p.30", "Hayes-Bennett proporcoes: conglomerados por grupo", 4, Jb,
        "arredondar para cima")
    # WP26 7.2.4 (p. 30-31): z 2.57+0.84, mu0=.05, mu1=.025, k=.25, n=50 -> 33
    M = 2.57 + 0.84
    Jt = 1 + M ** 2 * ((0.05 + 0.025) / 50 + 0.25 ** 2 * (0.05 ** 2 + 0.025 ** 2)) / (0.025) ** 2
    add("WP26 7.2.4 p.31", "Hayes-Bennett taxas: conglomerados por grupo", 33, Jt,
        "arredondar para cima")
    # McKenzie (2012), Tabela 3: delta=10, sigma=100, poder .8, alfa .05
    for est, pub in [("post", 1570), ("did", 2355), ("ancova", 1472)]:
        add("McKenzie 2012 tab.3", f"{est}, m=1 r=1 rho=.25 (n por grupo)", pub,
            n_mckenzie(10, 100, 1, 1, 0.25, est))
    add("McKenzie 2012 tab.3", "ancova, m=1 r=2 rho=.5", 785, n_mckenzie(10, 100, 1, 2, 0.5, "ancova"))
    add("McKenzie 2012 tab.3", "ancova, m=2 r=1 rho=.5", 1047, n_mckenzie(10, 100, 2, 1, 0.5, "ancova"))
    add("McKenzie 2012 tab.3", "did, m=2 r=2 rho=.5", 785, n_mckenzie(10, 100, 2, 2, 0.5, "did"))
    # Consistência BPW eq.(2) com psi=0  vs  McKenzie DiD com sigma2_omega = sigma^2 (1 - rho)
    J, rho, s = 200, 0.3, 1.0
    v_mck = var_mckenzie(s, J / 2, 3, 3, rho, "did")
    mde_mck = multiplicador() * math.sqrt(v_mck)
    add("BPW 2020 eq.2 x McKenzie eq.7", "psi=0 e sigma2_omega = sigma2(1-rho): MDEs iguais",
        round(mde_mck, 4), mde_did_bpw(J, 0.5, 3, 3, s * (1 - rho)))
    return pd.DataFrame(linhas)


def cenarios_municipais() -> pd.DataFrame:
    """Painel municipal ilustrativo: J = 78 municípios do ES, MDE em unidades
    de desvio-padrão do erro idiossincrático (sigma_omega = 1).
    P, m, r e phi (AR(1)) são hipóteses; nada aqui é estimativa da LICC."""
    linhas = []
    for P in (0.25, 0.50):
        for m, r in ((1, 1), (3, 3), (5, 4)):
            for phi in (0.0, 0.3, 0.5, 0.7):
                psiB, psiA, psiX = psi_ar1(1.0, phi, m, r)
                linhas.append({
                    "J_municipios": 78, "P_tratados": P, "m_pre": m, "r_pos": r,
                    "phi_AR1_hipotese": phi,
                    "MDE_em_dp_idiossincratico_SCR": round(
                        mde_did_bpw(78, P, m, r, 1.0, psiB, psiA, psiX), 3),
                    "MDE_ignorando_correlacao_serial": round(
                        mde_did_bpw(78, P, m, r, 1.0), 3),
                })
    return pd.DataFrame(linhas)


def _norm(s: str) -> str:
    return " ".join(unicodedata.normalize("NFKD", str(s)).encode(
        "ascii", "ignore").decode().upper().split())


def deff_proponente() -> pd.DataFrame:
    """Projetos por proponente nos ciclos 2022-2024 (status encerrados ou em
    execução, mesmo recorte de analise/tabelas/licc_emd_ilustrativo.csv) e o
    efeito de desenho implicado para CCIs hipotéticos."""
    fs = sorted(glob.glob(os.path.join(RAIZ, "dados", "licc", "habilitados",
                                       "habilitados-202[2-4].csv")))
    d = pd.concat([pd.read_csv(f) for f in fs], ignore_index=True)
    d = d[d["status"].isin(["concluido", "em_execucao", "captacao_expirada"])]
    d = d[d["proponente"].notna()].copy()
    d["prop"] = d["proponente"].map(_norm)
    tam = d.groupby("prop").size()
    n, g = len(d), len(tam)
    mbar = n / g
    cv = tam.std(ddof=0) / mbar
    P = (d["status"] != "captacao_expirada").mean()
    linhas = []
    for icc in (0.0, 0.05, 0.20, 0.50):
        de = efeito_desenho(mbar, icc)
        de_cv = efeito_desenho(mbar, icc, cv)
        linhas.append({
            "projetos": n, "proponentes_nomes_normalizados": g,
            "m_medio": round(mbar, 3), "cv_tamanho": round(cv, 3),
            "max_projetos_por_proponente": int(tam.max()),
            "P_captou": round(P, 4), "icc_hipotese": icc,
            "deff_m_medio": round(de, 3), "deff_com_cv": round(de_cv, 3),
            "n_efetivo": round(n / de_cv, 1),
            "MDE_dp_sem_conglomerado": round(mde_simples(1.0, n, P), 3),
            "MDE_dp_com_deff_cv": round(mde_simples(1.0, n, P) * math.sqrt(de_cv), 3),
            "fonte": "dados/licc/habilitados/habilitados-2022..2024.csv",
        })
    return pd.DataFrame(linhas)


def tabela_tipo_m() -> pd.DataFrame:
    linhas = []
    for lam in (0.5, 1.0, 1.5, 2.0, 2.8, 3.5):
        r = tipo_s_m(lam, 1.0)
        linhas.append({"efeito_verdadeiro_sobre_ep": lam,
                       **{k: round(v, 3) for k, v in r.items()}})
    return pd.DataFrame(linhas)


if __name__ == "__main__":
    pd.set_option("display.width", 200)
    saidas = {
        "05_poder_verificacao.csv": verificacao(),
        "05_poder_mde_municipal_did.csv": cenarios_municipais(),
        "05_poder_deff_proponente.csv": deff_proponente(),
        "05_poder_tipo_m.csv": tabela_tipo_m(),
    }
    for nome, df in saidas.items():
        df.to_csv(os.path.join(TAB, nome), index=False)
        print(f"\n== {nome}\n{df.to_string(index=False)}")
