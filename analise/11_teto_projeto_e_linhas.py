"""
11 — Teto por projeto, número mínimo de projetos, linha de fomento (proxy) e o contraste com uma seleção por nota.

1. Teto por projeto em cada ano (2022-2026), com o trecho literal da norma conferido no texto coletado (regra 2 do
   CLAUDE.md). Em 2022-2023 o teto era uma fração do montante anual (5%; 10% para intervenção física em
   patrimônio); a partir de 2024 é um valor fixo (R$ 500 mil). O montante dividido pelo teto dá o número MÍNIMO de
   projetos que o ano financia se todos captarem o teto: é uma identidade do desenho, não uma estimativa. Onde a
   norma do ano não está no repositório, o trecho fica sem conferência e a fonte diz qual é (regra 1).
2. Linha de fomento (IN, art. 9º, I-VI) por projeto habilitado. A SECULT não publica a linha: nem os anexos, nem o
   aviso no DIO, nem a API pública do Mapa Cultural (dados/fontes_web/paginas/mapa_api_inscricoes_1878.txt devolve
   lista vazia). A linha aqui é INFERIDA da linguagem, que por sua vez é inferida do título pelas regras de
   analise/06_alocacao_linguagens.py, mais marcadores de valor (acima do teto geral só cabe patrimônio com obra ou
   longa-metragem). Título sem regra fica ausente, não vira "outros". Nenhum número desta parte entra no artigo.
3. Resumo agregado da ata de julgamento de recursos e resultado da pré-seleção do edital Funcultura nº 29/2025
   (curtas e médias-metragens): contagens e notas por linha, faixa de município e situação, e recursos por
   decisão. Sem nomes (a ata identifica pessoas físicas). Fonte: a página que o relé coletar com a ata; se não
   houver, um PDF passado na linha de comando, registrado como "documento fornecido pelo autor".

Saídas (analise/tabelas/):
  11_teto_projeto_por_ano.csv
  11_linhas_proxy_por_ciclo.csv
  11_funcultura_29_2025_resumo.csv    (se a ata estiver disponível)
  11_funcultura_29_2025_recursos.csv  (idem)
Uso: python analise/11_teto_projeto_e_linhas.py [--ata-pdf caminho/para/ata.pdf]
"""
from __future__ import annotations

import hashlib
import importlib.util
import re
import statistics
import subprocess
import sys
from pathlib import Path

import pandas as pd

RAIZ = Path(__file__).resolve().parents[1]
PAG = RAIZ / "dados" / "fontes_web" / "paginas"
FONTES = RAIZ / "notas" / "politica" / "fontes"
TAB = RAIZ / "analise" / "tabelas"
PROC = RAIZ / "dados" / "processados"

_spec = importlib.util.spec_from_file_location("ling", RAIZ / "analise" / "06_alocacao_linguagens.py")
ling = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ling)

ARQ = {
    2022: PAG / "in2022_instru__o_normativa_licc_-_secult.txt",  # IN nº 002/2022, coletada pelo relé (etapa seguir)
    2023: PAG / "secult_in_2023_pdf.txt",
    2024: PAG / "secult_in_2024_pdf.txt",
    2025: FONTES / "in-licc-001-2025.md",
    2026: FONTES / "in-licc-001-2026.md",
}
# Regra do teto por ano. Os trechos cabem numa linha do texto coletado (as INs de 2023 e 2024 vêm do DIO em duas
# colunas; trecho que cruza linha seria misturado com a outra coluna).
REGRAS_TETO = [
    {"ano": 2022, "regra": "fração do montante", "pct_montante": 5.0, "pct_montante_patrimonio": 10.0,
     "teto_fixo": None, "teto_patrimonio_obra": None, "teto_longa": None, "teto_primeira_edicao": None,
     "limite_projetos_por_agente": None, "dispositivo": "IN 002/2022, arts. 8º e 9º",
     "trechos": ["projeto cultural não poderá ser superior a 5% do valor total anual previsto no montante dos",
                 "não poderá ser superior a 10% do valor total anual previsto no montante dos recursos destinados"],
     "fonte_alternativa": "confirmado também na live Tira-Dúvidas da SECULT, 19/04/2022, cerca de 46 min "
     "(https://www.youtube.com/watch?v=KvXStH6-Iy4): R$ 10 mi → R$ 500 mil e R$ 1 mi para patrimônio"},
    {"ano": 2023, "regra": "fração do montante", "pct_montante": 5.0, "pct_montante_patrimonio": 10.0,
     "teto_fixo": None, "teto_patrimonio_obra": None, "teto_longa": None, "teto_primeira_edicao": None,
     "limite_projetos_por_agente": None, "dispositivo": "IN 2023, arts. 8º e 9º",
     "trechos": ["cada projeto cultural não poderá ser superior a 5% do",
                 "ser superior a 10% do valor total anual previsto no"], "fonte_alternativa": ""},
    {"ano": 2024, "regra": "valor fixo", "pct_montante": None, "pct_montante_patrimonio": None,
     "teto_fixo": 500_000, "teto_patrimonio_obra": 1_000_000, "teto_longa": 1_000_000, "teto_primeira_edicao": None,
     "limite_projetos_por_agente": None, "dispositivo": "IN 2024, arts. 8º a 10",
     "trechos": ["poderá ser superior a R$ 500.000,00 (quinhentos",
                 "o valor de até R$ 1.000.000,00 (um milhão de reais)",
                 "projeto poderá atingir o valor de até R$ 1.000.000,00"], "fonte_alternativa": ""},
    {"ano": 2025, "regra": "valor fixo", "pct_montante": None, "pct_montante_patrimonio": None,
     "teto_fixo": 500_000, "teto_patrimonio_obra": 1_000_000, "teto_longa": 1_000_000, "teto_primeira_edicao": 300_000,
     "limite_projetos_por_agente": 3, "dispositivo": "IN 001/2025, arts. 13 a 16",
     "trechos": ["não poderá ser superior a R$500.000,00 (quinhentos mil reais)",
                 "não poderá ser superior a R$300.000,00",
                 "de R$ 1.000.000,00 (um milhão de reais) por projeto",
                 "poderá atingir o valor de até R$1.000.000,00",
                 "O limite anual para inscrição de projetos pelo mesmo agente cultural é de até 03"],
     "fonte_alternativa": ""},
    {"ano": 2026, "regra": "valor fixo", "pct_montante": None, "pct_montante_patrimonio": None,
     "teto_fixo": 500_000, "teto_patrimonio_obra": 1_000_000, "teto_longa": 1_000_000, "teto_primeira_edicao": 300_000,
     "limite_projetos_por_agente": 3, "dispositivo": "IN 001/2026, arts. 13 a 16",
     "trechos": ["ser superior a R$500.000,00 (quinhentos mil reais)",
                 "poderá ser superior a R$300.000,00",
                 "via LICC terá o limite de R$ 1.000.000,00",
                 "poderá atingir o valor de até R$1.000.000,00",
                 "Cada agente cultural pode inscrever até **3"],
     "fonte_alternativa": ""},
]
# Montante inicial (primeira portaria do ano), para o teto de 2022-2023, que é fração do montante "definido em ato
# do Secretário da SEFAZ": dados/externos/licc_teto_vs_icms.csv (coluna fonte_teto) e notas/politica/01-desenho-legal.md.
MONTANTE_INICIAL = {2022: 10_000_000, 2023: 10_000_000}


def normal(txt: str) -> str:
    return re.sub(r"\s+", " ", txt)


def in_2022_coletada() -> tuple[Path | None, bool]:
    """Se o relé trouxe a IN 2022 (etapa seguir, prefixo in2022), confere a regra dos 5%."""
    for arq in sorted(PAG.glob("in2022_*.txt")):
        if arq.name == "in2022_indice.txt":
            continue
        t = normal(arq.read_text(encoding="utf-8"))
        if re.search(r"superior a 5 ?% do valor total anual", t):
            return arq, True
        return arq, False
    return None, False


def teto_por_ano() -> pd.DataFrame:
    aud = pd.read_csv(RAIZ / "artigo" / "auditoria" / "auditoria_captacao_anual.csv").set_index("ano_captacao")
    bun = pd.read_csv(TAB / "03_bunching_teto.csv")
    bun = bun[bun["ciclo"].astype(str).str.fullmatch(r"\d{4}")].assign(ciclo=lambda d: d["ciclo"].astype(int)).set_index("ciclo")
    textos = {a: normal(p.read_text(encoding="utf-8")) for a, p in ARQ.items()}
    arq22, ok22 = in_2022_coletada()
    linhas = []
    for r in REGRAS_TETO:
        a = r["ano"]
        if r["trechos"]:
            conferidos = [normal(t) in textos[a] for t in r["trechos"]]
            conferencia = all(conferidos)
            arquivo = str(ARQ[a].relative_to(RAIZ))
        elif arq22 is not None:
            conferencia, arquivo = ok22, str(arq22.relative_to(RAIZ))
        else:
            conferencia, arquivo = None, ""
        montante = float(aud.loc[a, "montante_impresso"])
        if r["regra"] == "fração do montante":
            teto_inicial = r["pct_montante"] / 100 * MONTANTE_INICIAL[a]
            teto_final = r["pct_montante"] / 100 * montante
            minimo = 100 / r["pct_montante"]  # se o teto acompanha o montante, o mínimo não depende dele
        else:
            teto_inicial = teto_final = float(r["teto_fixo"])
            minimo = montante / r["teto_fixo"]
        linhas.append({
            "ano": a, "regra": r["regra"], "pct_montante": r["pct_montante"],
            "pct_montante_patrimonio_obra": r["pct_montante_patrimonio"],
            "teto_geral_montante_inicial": teto_inicial, "teto_geral_montante_final": teto_final,
            "teto_patrimonio_obra": r["teto_patrimonio_obra"], "teto_longa_metragem": r["teto_longa"],
            "teto_primeira_edicao": r["teto_primeira_edicao"], "limite_projetos_por_agente": r["limite_projetos_por_agente"],
            "montante_inicial": MONTANTE_INICIAL.get(a), "montante": montante,
            "teto_sobre_montante": teto_final / montante,
            "minimo_projetos_todos_no_teto": minimo,
            "minimo_projetos_teto_500mil": montante / 500_000,
            "projetos_que_captaram": int(aud.loc[a, "projetos"]),
            "projetos_validados": None if pd.isna(aud.loc[a, "projetos_validados"]) else int(aud.loc[a, "projetos_validados"]),
            "soma_validados": None if pd.isna(aud.loc[a, "soma_validados"]) else float(aud.loc[a, "soma_validados"]),
            "habilitados_com_valor": int(bun.loc[a, "n_com_valor"]),
            "pct_habilitados_exatamente_500mil": float(bun.loc[a, "pct_exatamente_500mil"]),
            "pct_habilitados_490_a_500mil": float(bun.loc[a, "pct_490_a_500mil_inclusive"]),
            "dispositivo": r["dispositivo"], "trechos_conferidos_no_texto": conferencia, "arquivo_norma": arquivo,
            "fonte_alternativa": r["fonte_alternativa"],
            "nota": ("teto fracionário: com o montante ampliado no ano, não se sabe se o teto subiu junto "
                     "(indeterminado); os pedidos acumulam em R$ 500 mil" if r["regra"] == "fração do montante" else ""),
            "fonte_montante": "artigo/auditoria/auditoria_captacao_anual.csv (montante impresso no anexo de captação)",
        })
    df = pd.DataFrame(linhas)
    df["valor_medio_validado"] = df["soma_validados"] / df["projetos_validados"]
    return df


# linguagem (06_alocacao_linguagens.py) → linha de financiamento da IN (art. 9º)
LINHA_DA_LINGUAGEM = {
    "audiovisual": "VI audiovisual",
    "música erudita e coral": "I linguagens artísticas",
    "música popular e festivais": "I linguagens artísticas",
    "teatro, dança e circo": "I linguagens artísticas",
    "literatura e livro": "I linguagens artísticas",
    "hip-hop, rap e cultura urbana": "I linguagens artísticas",
    "tradição popular e festas": "IV patrimônio imaterial e culturas tradicionais",
    "patrimônio e memória": "IV ou V (patrimônio; título não separa)",
    "formação e oficinas": "I ou III (formação; título não separa)",
}


def linhas_proxy() -> pd.DataFrame:
    h = pd.read_csv(PROC / "habilitados.csv").drop_duplicates("numero_processo").copy()
    prop = pd.read_csv(PROC / "proponentes.csv")[["chave_proponente", "natureza_rotulo"]]
    h = h.merge(prop, on="chave_proponente", how="left")
    h["linguagem"] = h["projeto"].map(ling.classificar)
    h["linha_proxy"] = h["linguagem"].map(LINHA_DA_LINGUAGEM)  # "não classificado" → ausente
    acima = h["valor_autorizado"] > 500_000
    h.loc[acima, "linha_proxy"] = "V ou VI (acima do teto geral: obra em patrimônio ou longa)"
    h.loc[h["enquadramento"].eq("cota-continuados"), "linha_proxy"] = "III planos plurianuais (cota)"
    h["marcador_primeira_edicao"] = h["valor_autorizado"].eq(300_000)
    grupos = []
    for ciclo, g in h.groupby("ciclo"):
        n = len(g)
        for linha, gg in g.groupby(g["linha_proxy"].fillna("ausente (título não classifica)")):
            grupos.append({
                "ciclo": ciclo, "linha_proxy": linha, "projetos": len(gg), "projetos_no_ciclo": n,
                "pct_projetos": len(gg) / n, "autorizado": gg["valor_autorizado"].sum(),
                "pct_autorizado": gg["valor_autorizado"].sum() / g["valor_autorizado"].sum(),
                "autorizado_mediano": gg["valor_autorizado"].median(),
                "mei": int(gg["natureza_rotulo"].eq("MEI/empresário individual").sum()),
                "osc": int(gg["natureza_rotulo"].str.startswith("Associação", na=False).sum()),
                "empresa": int(gg["natureza_rotulo"].str.startswith("Empresa", na=False).sum()),
                "natureza_indeterminada": int((~gg["natureza_rotulo"].str.startswith(("MEI", "Associação", "Empresa"), na=False)).sum()),
                "primeira_edicao_300mil": int(gg["marcador_primeira_edicao"].sum()),
            })
    df = pd.DataFrame(grupos)
    df["fonte"] = ("dados/processados/habilitados.csv; linguagem inferida do título (analise/06_alocacao_linguagens.py); "
                   "linha = correspondência LINHA_DA_LINGUAGEM; valor > R$ 500 mil e cota de plurianuais sobrepõem")
    return df


# ------------------------------------------------------------------ Funcultura, edital 29/2025 (contraste de seleção)
ID = re.compile(r"es-\s*(\d{6,})")  # o número pode quebrar a linha depois do hífen
LINHA_ANEXO = re.compile(r"^\s*(\d+)\s+es-\s?(\d{6,})\b.*?\s(\d{1,3},\d{2}|0)\s*$")


def texto_da_ata(argv: list[str]) -> tuple[str, str, str] | None:
    """(texto, fonte, sha256) da ata: primeiro a coletada pelo relé; senão o PDF passado em --ata-pdf."""
    for arq in sorted(PAG.glob("fun20*_*.txt")):
        t = arq.read_text(encoding="utf-8")
        tn = " ".join(t.split())
        if "29/2025" in tn and "PLANILHA DE RESULTADO" in tn and "JULGAMENTO DE RECURSOS E RESULTADO FINAL DA ETAPA DE PRÉ" in tn:
            url = re.search(r"^# Fonte: (\S+)", t, flags=re.M)
            sha = re.search(r"^# sha256 do original: (\S+)", t, flags=re.M)
            return t, url.group(1) if url else str(arq.relative_to(RAIZ)), sha.group(1) if sha else ""
    if "--ata-pdf" in argv:
        pdf = Path(argv[argv.index("--ata-pdf") + 1])
        t = subprocess.run(["pdftotext", "-layout", str(pdf), "-"], capture_output=True, text=True).stdout
        return t, f"documento fornecido pelo autor ({pdf.name}); URL oficial não localizada", \
            hashlib.sha256(pdf.read_bytes()).hexdigest()
    return None


def funcultura(texto: str, fonte: str, sha: str) -> tuple[pd.DataFrame, pd.DataFrame]:
    ini_anexo = texto.index("PLANILHA DE RESULTADO")
    corpo, anexo = texto[:ini_anexo], texto[ini_anexo:]
    linhas, linha, faixa, situacao = [], None, None, None
    for l in anexo.splitlines():
        if m := re.search(r"LINHA DE FOMENTO (\d)", l):
            linha, faixa = int(m.group(1)), None
        elif "MAIS de 150 mil" in l:
            faixa = "mais de 150 mil hab."
        elif "MENOS de 150 mil" in l or "ATÉ 150 mil" in l.upper():
            faixa = "até 150 mil hab."
        elif "classificados para a etapa de seleção" in l and "não" not in l:
            situacao = "classificado para a seleção"
        elif "não pré-selecionados" in l:
            situacao = "não pré-selecionado"
        elif "desclassificados" in l:
            situacao = "desclassificado"
        elif m := LINHA_ANEXO.match(l):
            linhas.append({"linha": linha, "faixa": faixa, "situacao": situacao, "ordem": int(m.group(1)),
                           "inscricao": m.group(2), "nota": float(m.group(3).replace(",", "."))})
    ins = pd.DataFrame(linhas)
    # toda inscrição do anexo precisa ter entrado (as que não têm nota na linha do número ficariam de fora)
    no_anexo = set(ID.findall(anexo))
    faltam = no_anexo - set(ins["inscricao"])
    resumo = []
    for (linha, faixa, sit), g in ins.groupby(["linha", "faixa", "situacao"], dropna=False):
        resumo.append({"edital": "Funcultura 29/2025 (curtas e médias-metragens)", "linha": linha, "faixa_municipio": faixa,
                       "situacao": sit, "inscricoes": len(g), "nota_min": g["nota"].min(),
                       "nota_mediana": statistics.median(g["nota"]), "nota_max": g["nota"].max()})
    res = pd.DataFrame(resumo)
    res["inscricoes_no_anexo"] = len(no_anexo)
    res["inscricoes_lidas"] = len(ins)
    res["inscricoes_sem_nota_lida"] = len(faltam)
    res["fonte"], res["sha256"] = fonte, sha

    # recursos: listados, decididos por tipo, fora do prazo, e os listados sem decisão
    def ids(trecho: str) -> set[str]:
        return set(ID.findall(trecho))
    pos_fora = corpo.index("fora do")
    frase_fora = corpo.rfind("O proponente", 0, pos_fora)
    listados = ids(corpo[corpo.index("dos seguintes proponentes"):frase_fora])
    fora = ids(corpo[frase_fora:pos_fora])
    deferidos = ids(corpo[corpo.index("Pelo DEFERIMENTO dos recursos"):corpo.index("DEFERIMENTO PARCIAL")])
    parciais = ids(corpo[corpo.index("DEFERIMENTO PARCIAL"):corpo.index("INDEFERIMENTO")])
    indeferidos = ids(corpo[corpo.index("INDEFERIMENTO"):corpo.index("Assim, considerando")])
    rec = pd.DataFrame([
        {"decisao": "listado na ata", "recursos": len(listados)},
        {"decisao": "deferido (nota corrigida)", "recursos": len(deferidos)},
        {"decisao": "deferido em parte (nota corrigida)", "recursos": len(parciais)},
        {"decisao": "indeferido", "recursos": len(indeferidos)},
        {"decisao": "fora do prazo (não analisado)", "recursos": len(fora - listados)},
        {"decisao": "listado sem decisão na ata", "recursos": len(listados - deferidos - parciais - indeferidos)},
    ])
    rec["fonte"], rec["sha256"] = fonte, sha
    return res, rec


def main() -> None:
    t = teto_por_ano()
    t.to_csv(TAB / "11_teto_projeto_por_ano.csv", index=False)
    print(t[["ano", "regra", "teto_geral_montante_inicial", "teto_geral_montante_final", "montante",
             "minimo_projetos_todos_no_teto", "projetos_que_captaram", "pct_habilitados_exatamente_500mil",
             "trechos_conferidos_no_texto"]].to_string(index=False))
    lp = linhas_proxy()
    lp.to_csv(TAB / "11_linhas_proxy_por_ciclo.csv", index=False)
    print(lp.groupby("linha_proxy")["projetos"].sum().sort_values(ascending=False).to_string())
    ata = texto_da_ata(sys.argv)
    if ata is None:
        print("Ata do edital Funcultura 29/2025 não encontrada (relé ou --ata-pdf): resumo não gerado.")
        return
    res, rec = funcultura(*ata)
    res.to_csv(TAB / "11_funcultura_29_2025_resumo.csv", index=False)
    rec.to_csv(TAB / "11_funcultura_29_2025_recursos.csv", index=False)
    print(res[["linha", "faixa_municipio", "situacao", "inscricoes", "nota_min", "nota_max"]].to_string(index=False))
    print(rec[["decisao", "recursos"]].to_string(index=False))
    print(f"inscrições no anexo: {res['inscricoes_no_anexo'].iat[0]}; lidas: {res['inscricoes_lidas'].iat[0]}; "
          f"sem nota lida: {res['inscricoes_sem_nota_lida'].iat[0]}")


if __name__ == "__main__":
    main()
