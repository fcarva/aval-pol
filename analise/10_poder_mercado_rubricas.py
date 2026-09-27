"""
10 — Apoio às hipóteses de marketing, apropriação e centralização (revisão de 27/09/2026).

1. Tetos das rubricas de custo por instrução normativa (2023-2026): captação, elaboração do projeto, remuneração
   do agente cultural, equipe técnica e divulgação. Cada teto é transcrito com o trecho literal da norma, e o script
   confere que o trecho está no texto coletado (regra 2 do CLAUDE.md: proveniência em todo número). Onde a IN não
   traz a rubrica, o teto fica ausente, não zero (regra 1).
2. Taxa de serviço permitida na captação de 2025: soma, projeto a projeto, do máximo que as regras de captação
   (10%, até R$ 50 mil) e elaboração (5%, até R$ 15 mil) permitem pagar a terceiros. É um limite normativo, não o
   gasto efetivo, que só as planilhas de custos (LAI) mostram.
3. Poder de um experimento conjunto (conjoint) com decisores de empresas contribuintes: efeito mínimo detectável do
   efeito marginal médio de um atributo binário (AMCE) sobre a escolha, com escolha forçada entre dois perfis,
   correlação dentro do respondente e as funções de 05_poder_mde.py.
4. Pareceristas credenciados por área, se a lista da SECULT (18/09/2026) tiver sido coletada pelo relé.

Saídas (analise/tabelas/):
  10_rubricas_teto_in.csv
  10_taxa_servico_permitida_2025.csv
  10_poder_conjoint.csv
  10_pareceristas_por_area.csv   (se a lista estiver em dados/fontes_web/paginas/)
Uso: python analise/10_poder_mercado_rubricas.py
"""
from __future__ import annotations

import csv
import importlib.util
import re
from pathlib import Path

import pandas as pd

RAIZ = Path(__file__).resolve().parents[1]
PAG = RAIZ / "dados" / "fontes_web" / "paginas"
FONTES = RAIZ / "notas" / "politica" / "fontes"
TAB = RAIZ / "analise" / "tabelas"

_spec = importlib.util.spec_from_file_location("poder", RAIZ / "analise" / "05_poder_mde.py")
poder = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(poder)

ARQ = {
    2023: PAG / "secult_in_2023_pdf.txt",
    2024: PAG / "secult_in_2024_pdf.txt",
    2025: FONTES / "in-licc-001-2025.md",
    2026: FONTES / "in-licc-001-2026.md",
}
# (ano, rubrica, limite_pct, teto_reais, dispositivo, trecho literal que precisa estar no texto)
TETOS = [
    (2023, "captação de recursos (empresa contratada)", 10, 50000, "art. 18, par. único", "ficando limitado ao teto de R$50.000,00"),
    (2023, "elaboração do projeto (empresa contratada)", 5, 15000, "art. 19, par. único", "ficando limitado ao teto de R$15.000,00"),
    (2023, "remuneração do agente cultural (PJ)", 33.3, None, "art. 17", "poderá receber até 1/3 dos recursos incentivados"),
    (2023, "equipe técnica", 30, None, "art. 15, IV", "técnica não poderão exceder 30% dos recursos"),
    (2023, "divulgação e impulsionamento", None, None, "sem limite próprio na IN", None),
    (2024, "captação de recursos (empresa contratada)", 10, 50000, "art. 18, par. único", "ficando limitado ao teto de R$50.000,00"),
    (2024, "elaboração do projeto (empresa contratada)", 5, 15000, "art. 19, par. único", "ficando limitado ao teto de R$15.000,00"),
    (2024, "remuneração do agente cultural (PJ)", 33.3, None, "art. 17", "poderá receber até 1/3 dos recursos incentivados"),
    (2024, "equipe técnica", 30, None, "art. 15, IV", "técnica não poderão exceder 30% dos recursos"),
    (2024, "divulgação e impulsionamento", None, None, "sem limite próprio na IN", None),
    (2025, "captação de recursos (empresa contratada)", 10, 50000, "art. 27, par. único", "ficando limitado ao teto de\nR$50.000,00"),
    (2025, "elaboração do projeto (empresa contratada)", 5, 15000, "art. 28, par. único", "ficando limitado ao teto de\nR$15.000,00"),
    (2025, "remuneração do agente cultural (PJ)", 33.3, None, "art. 26", "poderá receber até 1/3 dos recursos"),
    (2025, "equipe técnica", 30, None, "art. 23, IV", "não poderão ultrapassar 30%"),
    (2025, "divulgação e impulsionamento", 25, None, "art. 23, V", "não poderão\nultrapassar 25% dos recursos incentivados via LICC"),
    (2026, "captação e/ou elaboração (despesa única, pode ser paga ao próprio agente)", 10, 50000, "art. 28, §§ 1º e 2º",
     "A remuneração desse serviço pode ser paga ao\npróprio agente cultural"),
    (2026, "remuneração do agente cultural (PJ)", 33.3, None, "art. 26", "poderá receber até 1/3 dos recursos incentivados"),
    (2026, "equipe técnica", 30, None, "art. 23, IV", "técnica não poderão ultrapassar 30% dos recursos"),
    (2026, "divulgação e impulsionamento", 25, None, "art. 23, V", "conteúdo, não poderão ultrapassar 25% dos recursos"),
]


def normal(txt: str) -> str:
    return re.sub(r"\s+", " ", txt)


def tetos() -> pd.DataFrame:
    textos = {a: normal(p.read_text(encoding="utf-8")) for a, p in ARQ.items()}
    linhas = []
    for ano, rub, pct, reais, disp, trecho in TETOS:
        achou = None if trecho is None else normal(trecho) in textos[ano]
        linhas.append({"ano_in": ano, "rubrica": rub, "limite_pct": pct, "teto_reais": reais, "dispositivo": disp,
                       "trecho": trecho.replace("\n", " ") if trecho else "", "trecho_no_texto": achou,
                       "arquivo": str(ARQ[ano].relative_to(RAIZ))})
    df = pd.DataFrame(linhas)
    faltam = df[df.trecho_no_texto == False]  # noqa: E712
    if len(faltam):
        raise SystemExit(f"trecho não encontrado no texto da norma:\n{faltam[['ano_in', 'rubrica', 'trecho']]}")
    return df


def taxa_servico_2025() -> pd.DataFrame:
    ap = pd.read_csv(RAIZ / "dados" / "processados" / "captados_2025.csv")
    v = ap["valor_captado"]
    capt = (0.10 * v).clip(upper=50000)
    elab = (0.05 * v).clip(upper=15000)
    return pd.DataFrame([{
        "projetos": len(v), "valor_captado": round(v.sum(), 2),
        "max_captacao": round(capt.sum(), 2), "max_elaboracao": round(elab.sum(), 2),
        "max_taxa_servico": round((capt + elab).sum(), 2),
        "max_taxa_servico_sobre_captado": round((capt + elab).sum() / v.sum(), 4),
        "max_divulgacao_25pct": round(0.25 * v.sum(), 2),
        "nota": "limites normativos (IN 001/2025, arts. 23, V, 27 e 28) aplicados ao valor captado de cada projeto; "
                "o gasto efetivo depende das planilhas de custos (LAI)",
    }])


def poder_conjoint() -> pd.DataFrame:
    """AMCE de atributo binário com escolha forçada: p0 = 0,5; metade dos perfis com cada nível."""
    linhas = []
    for R in (30, 60, 100):
        for K in (8, 12):
            m = 2 * K  # perfis avaliados por respondente
            n = R * m
            for icc in (0.0, 0.1):
                deff = poder.efeito_desenho(m, icc, 0.0)
                linhas.append({"respondentes": R, "tarefas": K, "perfis_por_respondente": m, "perfis": n,
                               "icc_respondente": icc, "p0": 0.5,
                               "emd_pontos": round(100 * poder.mde_binario(0.5, n, T=0.5) * deff ** 0.5, 1)})
    return pd.DataFrame(linhas)


def pareceristas() -> pd.DataFrame | None:
    """Lista de credenciados da SECULT (18/09/2026): uma tabela por área, com o mesmo parecerista em até três áreas.
    Conta pareceristas distintos (pelo número de encaminhamento) e o tamanho de cada tabela. Não grava nomes."""
    arq = PAG / "secult_pareceristas_credenciados_2026.txt"
    if not arq.exists():
        return None
    texto = arq.read_text(encoding="utf-8")
    linha = re.compile(r"^\s*\d+\s+(2025-[A-Z0-9]{6})\s+\d{2}/\d{2}/\d{4}\s+\d{2}:\d{2}:\d{2}", flags=re.M)
    blocos = texto.split("Colocação")[1:]
    tamanhos = [len(linha.findall(b)) for b in blocos]
    distintos = len(set(linha.findall(texto)))
    linhas = [{"tabela_area": i + 1, "pareceristas": n} for i, n in enumerate(tamanhos)]
    linhas.append({"tabela_area": "distintos (todas as áreas)", "pareceristas": distintos})
    df = pd.DataFrame(linhas)
    df["fonte"] = "dados/fontes_web/paginas/secult_pareceristas_credenciados_2026.txt"
    return df


def main() -> None:
    t = tetos()
    t.to_csv(TAB / "10_rubricas_teto_in.csv", index=False)
    s = taxa_servico_2025()
    s.to_csv(TAB / "10_taxa_servico_permitida_2025.csv", index=False)
    c = poder_conjoint()
    c.to_csv(TAB / "10_poder_conjoint.csv", index=False)
    pa = pareceristas()
    if pa is not None:
        pa.to_csv(TAB / "10_pareceristas_por_area.csv", index=False)
        print(pa.to_string(index=False))
    print(t[["ano_in", "rubrica", "limite_pct", "teto_reais", "trecho_no_texto"]].to_string(index=False))
    print(s.T.to_string())
    print(c.to_string(index=False))


if __name__ == "__main__":
    main()
