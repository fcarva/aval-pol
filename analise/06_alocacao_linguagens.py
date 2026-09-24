"""
06 — O que a LICC financia, por linguagem cultural e território: cardápio (habilitados), conversão
(captou × expirou) e carteira de cada patrocinador. Insumo descritivo para a pergunta de alocação de bens
públicos culturais (notas/desenho/02-alocacao-bens-publicos-culturais.md).

Limite declarado (regra 3 do CLAUDE.md): a SECULT não publica a linguagem do projeto. A classificação
abaixo é INFERIDA DO TÍTULO por regras explícitas (lista REGRAS, aplicada na ordem; o primeiro casamento
vale). Título que não casa fica "não classificado" — ausente, não "outros". O script grava uma amostra
para conferência manual (06_amostra_conferencia.csv). Nenhum número daqui entra no artigo sem essa
conferência.

Fontes: dados/processados/habilitados.csv (01_carregar.py), dados/licc/oficial/captados-2025.csv.
Saídas (analise/tabelas/):
  06_linguagem_cardapio_por_ciclo.csv     habilitados e valor autorizado por linguagem e ciclo
  06_linguagem_conversao_2022_2024.csv    taxa de execução por linguagem, total e dentro de RMGV/interior
  06_linguagem_patrocinador_2025.csv      captado de 2025 por linguagem e patrocinador (raiz do CNPJ)
  06_amostra_conferencia.csv              60 títulos sorteados (semente fixa) para conferir à mão
Uso: python analise/06_alocacao_linguagens.py
"""
from __future__ import annotations

import re
import unicodedata
from pathlib import Path

import pandas as pd

RAIZ = Path(__file__).resolve().parents[1]
PROC = RAIZ / "dados" / "processados"
TAB = RAIZ / "analise" / "tabelas"

# (linguagem, padrão sobre o título normalizado: minúsculas, sem acento)
REGRAS = [
    ("hip-hop, rap e cultura urbana", r"hip.?hop|\brap\b|batalha|\bslam\b|breaking|\bbreak\b|grafit|graffit|\brima|\bfunk\b|perifer|quebrada|favela"),
    ("música erudita e coral", r"orquestr|sinfon|filarm|camerat|classic|erudit|\bopera\b|\bcoral\b|\bcorais\b|\bcoro\b|concerto|\bbach\b|\blirico"),
    ("tradição popular e festas", r"congo|folia|\breis\b|jongo|ticumbi|folclor|carnaval|\bsamba\b|\bboi\b|caxambu|pomeran|festa|quadrilh|capoeira|tradic"),
    ("audiovisual", r"cinema|\bfilme|curta|longa.?metragem|document|audiovisual|\bmostra de cine|animac|cine\w*|\bserie\b|webserie"),
    ("teatro, dança e circo", r"teatr|espetacul|\bdanca|\bballet|\bbale\b|circo|circens|palhac|\bcenic"),
    ("literatura e livro", r"\blivro|literat|leitura|poesi|\bpoet|biblioteca|\bfeira do livro|\bflip|editor"),
    ("patrimônio e memória", r"patrimon|museu|memoria|restaur|histori|acervo|arquiv|igreja"),
    ("música popular e festivais", r"music|\bshow|festival|\bsom\b|sanfon|viola|\bbanda|\bjazz|\brock|\bblues|\bforro|\bsertanej|cancao|\bcanto"),
    ("formação e oficinas", r"oficina|formac|\bescola|\bcurso|capacit|\blab\b|laborat|residencia|educa"),
]


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", str(s))
    return "".join(c for c in s if not unicodedata.combining(c)).lower()


def classificar(titulo: str) -> str:
    t = norm(titulo)
    for nome, padrao in REGRAS:
        if re.search(padrao, t):
            return nome
    return "não classificado"


def main() -> None:
    h = pd.read_csv(PROC / "habilitados.csv").drop_duplicates("numero_processo").copy()
    mun = pd.read_csv(RAIZ / "dados" / "externos" / "municipios_es.csv")
    rm = set(mun.loc[mun["rmgv"], "cod_ibge"])
    h["linguagem"] = h["projeto"].map(classificar)
    h["territorio"] = h["cod_ibge_valor"].map(lambda c: "" if pd.isna(c) else ("RMGV" if int(c) in rm else "Interior"))

    card = (h.groupby(["ciclo", "linguagem"]).agg(projetos=("numero_processo", "size"),
                                                   autorizado=("valor_autorizado", "sum")).reset_index())
    card["pct_autorizado_no_ciclo"] = card["autorizado"] / card.groupby("ciclo")["autorizado"].transform("sum")
    tot = (h.groupby("linguagem").agg(projetos=("numero_processo", "size"), autorizado=("valor_autorizado", "sum"))
           .reset_index().assign(ciclo="2022-2026"))
    tot["pct_autorizado_no_ciclo"] = tot["autorizado"] / tot["autorizado"].sum()
    pd.concat([card, tot]).to_csv(TAB / "06_linguagem_cardapio_por_ciclo.csv", index=False)

    g = h[(h["ciclo"] <= 2024) & (h["status"] != "captando")].copy()
    g["executado"] = g["status"].isin(["concluido", "em_execucao"])
    conv = [g.groupby("linguagem")["executado"].agg(resolvidos="size", executados="sum").reset_index()
            .assign(recorte="todos")]
    for ter in ("RMGV", "Interior"):
        conv.append(g[g["territorio"] == ter].groupby("linguagem")["executado"]
                    .agg(resolvidos="size", executados="sum").reset_index().assign(recorte=ter))
    conv = pd.concat(conv)
    conv["taxa_execucao"] = conv["executados"] / conv["resolvidos"]
    conv[["recorte", "linguagem", "resolvidos", "executados", "taxa_execucao"]].to_csv(
        TAB / "06_linguagem_conversao_2022_2024.csv", index=False)

    c = pd.read_csv(RAIZ / "dados" / "licc" / "oficial" / "captados-2025.csv")
    c["linguagem"] = c["projeto"].map(classificar)
    linhas = []
    for _, r in c.iterrows():
        for ap in str(r["aportes"]).split(";"):
            partes = ap.split("|")
            if len(partes) == 3:
                cnpj, nome, valor = partes
                linhas.append({"linguagem": r["linguagem"], "projeto": r["projeto"],
                               "cnpj_raiz": re.sub(r"\D", "", cnpj)[:8], "patrocinador": nome.strip(),
                               "valor": float(valor)})
    ap = pd.DataFrame(linhas)
    pat = (ap.groupby(["cnpj_raiz", "linguagem"]).agg(patrocinador=("patrocinador", "first"),
                                                      projetos=("projeto", "nunique"), valor=("valor", "sum"))
           .reset_index())
    pat["pct_da_carteira"] = pat["valor"] / pat.groupby("cnpj_raiz")["valor"].transform("sum")
    pat.sort_values(["cnpj_raiz", "valor"], ascending=[True, False]).to_csv(
        TAB / "06_linguagem_patrocinador_2025.csv", index=False)

    amostra = h.sample(n=60, random_state=20260924)[["ciclo", "numero_processo", "projeto", "linguagem"]]
    amostra.assign(linguagem_conferida="").to_csv(TAB / "06_amostra_conferencia.csv", index=False)

    print(tot.sort_values("autorizado", ascending=False).to_string(index=False))
    print(conv[conv.recorte == "todos"].to_string(index=False))
    print("não classificados:", (h["linguagem"] == "não classificado").sum(), "de", len(h))


if __name__ == "__main__":
    main()
