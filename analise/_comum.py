"""Funções compartilhadas pelos scripts 01-04 da análise descritiva da LICC.

Regras que este módulo existe para não quebrar (herdadas do licc.gov):
- célula vazia é ausência, nunca zero: nenhuma função aqui troca NaN por 0;
- todo indicador viaja com o denominador (n com dado / n total);
- casamento entre anexos é por título normalizado EXATO, nunca por semelhança.
"""
from __future__ import annotations

import json
import re
import unicodedata
from pathlib import Path

import numpy as np
import pandas as pd
import requests

RAIZ = Path(__file__).resolve().parents[1]
DADOS = RAIZ / "dados"
LICC = DADOS / "licc"
EXTERNOS = DADOS / "externos"
PROCESSADOS = DADOS / "processados"
TABELAS = RAIZ / "analise" / "tabelas"
FIGURAS = RAIZ / "analise" / "figuras"
for _p in (EXTERNOS, PROCESSADOS, TABELAS, FIGURAS):
    _p.mkdir(parents=True, exist_ok=True)

URL_MUNICIPIOS = "https://servicodados.ibge.gov.br/api/v1/localidades/estados/32/municipios"
URL_DISTRITOS = "https://servicodados.ibge.gov.br/api/v1/localidades/estados/32/distritos"

# Teto por projeto: IN SECULT 001/2025, art. 14 (R$ 500 mil, regra geral),
# art. 14 §2º (R$ 300 mil, evento em 1ª edição), arts. 15-16 (R$ 1 mi,
# intervenção física em patrimônio / longa-metragem e obra seriada).
# Texto conferido em notas/politica/fontes/in-licc-001-2025.md.
TETO_GERAL = 500_000.0
TETO_1A_EDICAO = 300_000.0
TETO_ESPECIAL = 1_000_000.0


def normalizar(texto: str | float | None) -> str:
    """Minúsculas, sem acento, só [a-z0-9] separados por um espaço.

    É a normalização usada para casar títulos (exato) e nomes de município.
    """
    if texto is None or (isinstance(texto, float) and np.isnan(texto)):
        return ""
    s = unicodedata.normalize("NFKD", str(texto))
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = s.lower()
    s = re.sub(r"[^a-z0-9]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def _get_json(url: str, cache: Path, timeout: int = 60):
    """Baixa JSON uma vez e guarda cópia em dados/externos (reprodutível offline)."""
    if cache.exists():
        return json.loads(cache.read_text(encoding="utf-8"))
    r = requests.get(url, timeout=timeout, headers={"User-Agent": "aval-pol-ufes/1.0 (pesquisa academica)"})
    r.raise_for_status()
    dados = r.json()
    cache.write_text(json.dumps(dados, ensure_ascii=False, indent=1), encoding="utf-8")
    return dados


def municipios_ibge() -> pd.DataFrame:
    """Os 78 municípios do ES com código IBGE (API de localidades do IBGE)."""
    bruto = _get_json(URL_MUNICIPIOS, EXTERNOS / "ibge_localidades_municipios_es.json")
    linhas = []
    for m in bruto:
        ri = m.get("regiao-imediata") or {}
        linhas.append(
            {
                "cod_ibge": int(m["id"]),
                "municipio": m["nome"],
                "microrregiao": m["microrregiao"]["nome"],
                "mesorregiao": m["microrregiao"]["mesorregiao"]["nome"],
                "regiao_imediata": ri.get("nome"),
                "regiao_intermediaria": (ri.get("regiao-intermediaria") or {}).get("nome"),
            }
        )
    df = pd.DataFrame(linhas).sort_values("municipio").reset_index(drop=True)
    df["chave"] = df["municipio"].map(normalizar)
    assert len(df) == 78, f"esperados 78 municípios no ES, vieram {len(df)}"
    return df


def distritos_ibge() -> pd.DataFrame:
    bruto = _get_json(URL_DISTRITOS, EXTERNOS / "ibge_localidades_distritos_es.json")
    return pd.DataFrame(
        [
            {"cod_distrito": int(d["id"]), "distrito": d["nome"], "cod_ibge": int(d["municipio"]["id"]),
             "municipio": d["municipio"]["nome"]}
            for d in bruto
        ]
    )


# --- Medidas de concentração/desigualdade -----------------------------------

def gini(valores) -> float:
    """Gini pela diferença média relativa (mesma fórmula do licc.gov).

    Σ (2i − n − 1)·xᵢ / (n · Σxᵢ), lista ordenada. Zeros ENTRAM (são dado:
    município sem projeto). NaN não entra (é ausência). n<2 ou soma 0 → NaN.
    """
    v = np.sort(np.asarray([x for x in valores if pd.notna(x)], dtype=float))
    n, soma = len(v), v.sum() if len(v) else 0.0
    if n < 2 or soma <= 0:
        return float("nan")
    i = np.arange(1, n + 1)
    return float(((2 * i - n - 1) * v).sum() / (n * soma))


def theil_t(valores, pesos=None) -> float:
    """Índice de Theil T.

    Sem pesos: T = (1/n) Σ (x/μ) ln(x/μ), com 0·ln0 = 0.
    Com pesos (população): T = Σ s_i ln(s_i / p_i), s = parcela do valor,
    p = parcela da população — mede o afastamento da distribuição per capita
    igualitária. Unidades com valor zero contribuem 0 (limite de s ln s).
    """
    x = np.asarray(valores, dtype=float)
    if pesos is None:
        x = x[~np.isnan(x)]
        mu = x.mean()
        if mu <= 0:
            return float("nan")
        r = x / mu
        with np.errstate(divide="ignore", invalid="ignore"):
            termos = np.where(r > 0, r * np.log(r), 0.0)
        return float(termos.mean())
    p = np.asarray(pesos, dtype=float)
    ok = ~(np.isnan(x) | np.isnan(p))
    x, p = x[ok], p[ok]
    s = x / x.sum()
    p = p / p.sum()
    with np.errstate(divide="ignore", invalid="ignore"):
        termos = np.where(s > 0, s * np.log(s / p), 0.0)
    return float(termos.sum())


def hhi(valores) -> float:
    """Herfindahl-Hirschman em escala 0-10.000 sobre parcelas do total."""
    v = np.asarray([x for x in valores if pd.notna(x)], dtype=float)
    if v.sum() <= 0:
        return float("nan")
    s = v / v.sum()
    return float((s**2).sum() * 10_000)


def cr(valores, k: int) -> float:
    """Razão de concentração CRk: parcela das k maiores unidades."""
    v = np.sort(np.asarray([x for x in valores if pd.notna(x)], dtype=float))[::-1]
    return float(v[:k].sum() / v.sum()) if v.sum() > 0 else float("nan")


def cobertura(n_com: int, n_total: int) -> str:
    return f"{n_com}/{n_total} ({100 * n_com / n_total:.1f}%)" if n_total else "0/0"


def brl(x: float, casas: int = 2) -> str:
    if pd.isna(x):
        return "—"
    s = f"{x:,.{casas}f}"
    return "R$ " + s.replace(",", "X").replace(".", ",").replace("X", ".")
