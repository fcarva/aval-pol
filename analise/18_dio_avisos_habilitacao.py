"""
18 — Avisos da LICC no Diário Oficial do ES: habilitação (processo, proponente, CNPJ, valor, data) e depósito do
patrocínio (patrocinador, CNPJ, valor do crédito presumido, projeto, data).

Fonte: trechos do DIO-ES coletados pelo relé (analise/rede/consultas_publicas.py, rota de busca pública do site),
dados/externos/dio_licc_trechos.csv. A SECULT publica "AVISO DE RESULTADO – LEI DE INCENTIVO À CULTURA CAPIXABA –
LICC ... torna público ... a HABILITAÇÃO do projeto abaixo indicado", com "Título do Projeto", "Processo nº",
"Proponente", "Cnpj" e "Valor".

Regras:
- leitura só pelo padrão "Processo ... Proponente ... Cnpj ... Valor"; o que não casa fica de fora e é contado;
- o CNPJ do aviso é comparado com o do Portal da Transparência (dados/processados/transparencia_licc_termos.csv)
  onde o processo aparece nos dois; divergência é contada, não corrigida;
- a busca do DIO devolve páginas inteiras, e um aviso pode aparecer em mais de um trecho: um registro por
  processo × CNPJ;
- não há aviso lido para o ciclo 2022 (formato diferente ou fora do alcance da busca): cobertura declarada;
- "AVISO DE DEPÓSITO DE PATROCÍNIO – LICC": um item por "Patrocinador ... CNPJ ... Valor do crédito presumido ...
  Beneficiário ... Projeto contemplado"; o trecho coletado é uma janela em volta do termo buscado, e um aviso longo
  pode ficar cortado (itens a menos, nunca inventados);
- depósito × termo do Portal: mesmo CNPJ do patrocinador e nome de projeto parecido; o aviso é por depósito, e o
  termo pode ser depositado em parcelas (ver deposito_x_portal); a defasagem é a data do DIO do primeiro depósito
  menos a "data do processo" do Portal (que não é a de protocolo; ver analise/16), e o que não casa é contado, não
  forçado. Pela Portaria Conjunta SEFAZ/SECULT nº 01-R/2022, arts. 5º e 6º, o crédito presumido só pode ser apropriado
  depois da publicação desse resumo no Diário Oficial: o aviso é o ato que valida o repasse;
- o nome do beneficiário não é gravado (pode ser pessoa física); fica o projeto, que é público.

Saídas:
  dados/processados/dio_avisos_habilitacao.csv    um aviso por processo × CNPJ, com a data do DIO
  analise/tabelas/18_cobertura_cnpj.csv           por ciclo: habilitados, com CNPJ no DIO, no Portal, em algum dos
                                                   dois, e concordância de CNPJ entre as fontes
  dados/processados/dio_avisos_deposito.csv       um depósito por patrocinador × valor × projeto, com a data do DIO
  dados/processados/dio_deposito_x_termo.csv      cada depósito ligado a um termo do Portal (integral ou parcela)
  analise/tabelas/18_deposito_x_portal.csv        por ano do Portal: termos, termos com depósito localizado, valor,
                                                   defasagem (dias) da "data do processo" ao aviso; depósitos sem termo
Uso: python analise/18_dio_avisos_habilitacao.py
"""
from __future__ import annotations

import re
import unicodedata
from pathlib import Path

import pandas as pd

RAIZ = Path(__file__).resolve().parents[1]
PROC = RAIZ / "dados" / "processados"
TAB = RAIZ / "analise" / "tabelas"

AVISO = re.compile(r"Processo\s*n?[°º]?\s*:?\s*(\d{4}-[A-Z0-9]{5})\s*Proponente\s*:?\s*(.{2,160}?)\s*Cnpj\s*:?\s*"
                   r"([\d./-]{14,20})\s*Valor\s*:?\s*R\$\s*([\d.,]+)", re.I)


def avisos() -> pd.DataFrame:
    d = pd.read_csv(RAIZ / "dados" / "externos" / "dio_licc_trechos.csv")
    regs = []
    for _, r in d.iterrows():
        t = re.sub(r"\s+", " ", str(r["trecho"]))
        for m in AVISO.finditer(t):
            valor = m.group(4).rstrip(".,")
            regs.append({"processo": m.group(1).upper(), "proponente_dio": m.group(2).strip(" -–,"),
                         "cnpj_dio": re.sub(r"\D", "", m.group(3)),
                         "valor_dio": pd.to_numeric(valor.replace(".", "").replace(",", "."), errors="coerce"),
                         "data_dio": r["data"], "pagina_dio": r["pagina"], "id_dio": r["id"]})
    a = pd.DataFrame(regs).sort_values("data_dio").drop_duplicates(["processo", "cnpj_dio"], keep="first")
    return a


DEPOSITO = re.compile(r"(?:\d{1,3}\)\s*)?Patrocinador:\s*(.{2,160}?)\s*CNPJ\s*:?\s*([\d./-]{14,20})\s*(?:IE\s*:?\s*[\d./-]*\s*)?"
                      r"Valor do cr[ée]dito presumido\s*:?\s*R\$\s*([\d.,]+)\s*Benefici[áa]rio\s*:?\s*(.{2,200}?)\s*"
                      r"Projeto contemplado\s*:?\s*(.{2,250}?)(?=\s*\d{1,3}\)\s*Patrocinador|\s*Assinado digitalmente|"
                      r"\s*Vit[óo]ria,|\s*Protocolo|\s*AVISO|$)")


def palavras(s: str) -> set[str]:
    s = "".join(c for c in unicodedata.normalize("NFD", str(s).lower()) if not unicodedata.combining(c))
    return {w for w in re.findall(r"[a-z0-9]+", s) if len(w) > 2}


def depositos() -> pd.DataFrame:
    d = pd.read_csv(RAIZ / "dados" / "externos" / "dio_licc_trechos.csv")
    regs = []
    for _, r in d.iterrows():
        for m in DEPOSITO.finditer(re.sub(r"\s+", " ", str(r["trecho"]))):
            regs.append({"data_dio": r["data"], "pagina_dio": r["pagina"], "id_dio": r["id"],
                         "patrocinador_dio": m.group(1).strip(), "cnpj_patrocinador": re.sub(r"\D", "", m.group(2)),
                         "valor_dio": pd.to_numeric(m.group(3).rstrip(".,").replace(".", "").replace(",", "."),
                                                    errors="coerce"),
                         "projeto_dio": m.group(5).strip()})
    a = pd.DataFrame(regs).sort_values("data_dio")
    return a.drop_duplicates(["cnpj_patrocinador", "valor_dio", "projeto_dio"]).reset_index(drop=True)


def deposito_x_portal(dep: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Liga cada termo do Portal aos avisos de depósito do mesmo patrocinador (CNPJ) e do mesmo projeto.

    O aviso é por depósito, e um termo pode ser depositado em parcelas (metade, um terço, um quarto do valor): cada
    depósito vai a um só termo, o de nome mais parecido, e a soma dos depósitos de um termo não passa do seu valor.
    1ª passada: mesmo valor (depósito integral), Jaccard >= 0,2; 2ª: parcelas, Jaccard >= 0,3.
    """
    t = pd.read_csv(PROC / "transparencia_licc_termos.csv", dtype={"cnpj_patrocinador": str})
    t = t[~t["valor_zero"]].reset_index(drop=True)
    t["tid"] = t.index
    a = dep.assign(did=dep.index)
    m = t.merge(a, on="cnpj_patrocinador")
    m["sim"] = [len(palavras(x) & palavras(y)) / max(1, len(palavras(x) | palavras(y)))
                for x, y in zip(m["projeto"], m["projeto_dio"])]
    m["integral"] = m["valor"].round(2) == m["valor_dio"].round(2)
    usados_d, soma, ligacoes = set(), {}, []
    for integral, corte in ((True, 0.2), (False, 0.3)):
        cand = m[(m["integral"] == integral) & (m["sim"] >= corte)].sort_values(["sim", "data_dio"],
                                                                               ascending=[False, True])
        for _, r in cand.iterrows():
            if r["did"] in usados_d or (integral and r["tid"] in soma):
                continue
            if soma.get(r["tid"], 0.0) + r["valor_dio"] > r["valor"] + 0.01:
                continue
            usados_d.add(r["did"])
            soma[r["tid"]] = soma.get(r["tid"], 0.0) + r["valor_dio"]
            ligacoes.append({"termo_id": r["tid"], "ano": r["ano"], "processo": r["processo"], "projeto": r["projeto"],
                             "cnpj_patrocinador": r["cnpj_patrocinador"], "valor_termo": r["valor"],
                             "data_processo": r["data_processo"], "data_dio": r["data_dio"],
                             "valor_dio": r["valor_dio"], "projeto_dio": r["projeto_dio"],
                             "deposito_integral": integral, "similaridade": round(r["sim"], 3)})
    k = pd.DataFrame(ligacoes)
    k["defasagem_dias"] = (pd.to_datetime(k["data_dio"]) - pd.to_datetime(k["data_processo"])).dt.days
    por_termo = k.groupby(["termo_id", "ano"], as_index=False).agg(
        depositos=("valor_dio", "size"), valor_depositado=("valor_dio", "sum"),
        primeiro_deposito=("data_dio", "min"), defasagem_primeiro=("defasagem_dias", "min"))
    out = t.groupby("ano").agg(termos=("valor", "size"), valor_termos=("valor", "sum"))
    g = por_termo.groupby("ano")
    out["termos_com_deposito"] = g.size()
    out["termos_deposito_integral"] = k[k["deposito_integral"]].groupby("ano")["termo_id"].nunique()
    out["valor_depositado_localizado"] = g["valor_depositado"].sum()
    out["pct_valor_localizado"] = out["valor_depositado_localizado"] / out["valor_termos"]
    out["defasagem_mediana"] = g["defasagem_primeiro"].median()
    out["defasagem_p25"] = g["defasagem_primeiro"].quantile(0.25)
    out["defasagem_p75"] = g["defasagem_primeiro"].quantile(0.75)
    out = out.fillna({"termos_com_deposito": 0, "termos_deposito_integral": 0}).reset_index()
    sem = a[~a["did"].isin(usados_d)]
    out = pd.concat([out, pd.DataFrame([{"ano": f"depósitos sem termo no Portal, publicados em {ano}", "termos": n}
                                        for ano, n in sem["data_dio"].str[:4].value_counts().sort_index().items()])])
    out["fonte"] = ("DIO-ES, avisos de depósito de patrocínio (dados/externos/dio_licc_trechos.csv); Portal da "
                    "Transparência (dados/processados/transparencia_licc_termos.csv)")
    return out, k


def main() -> None:
    dep = depositos()
    dep.to_csv(PROC / "dio_avisos_deposito.csv", index=False)
    dp, lig = deposito_x_portal(dep)
    dp.to_csv(TAB / "18_deposito_x_portal.csv", index=False)
    lig.to_csv(PROC / "dio_deposito_x_termo.csv", index=False)
    print(dp.drop(columns=["fonte"]).to_string(index=False))
    a = avisos()
    a.to_csv(PROC / "dio_avisos_habilitacao.csv", index=False)
    h = pd.read_csv(PROC / "habilitados.csv").sort_values("ciclo").drop_duplicates("numero_processo", keep="last")
    t = pd.read_csv(PROC / "transparencia_licc_termos.csv", dtype={"cnpj_proponente": str})
    portal = set(t.loc[t["cnpj_proponente_dv_ok"].astype(bool), "processo"])
    dio = set(a["processo"])
    h["cnpj_dio"] = h["numero_processo"].isin(dio)
    h["cnpj_portal"] = h["numero_processo"].isin(portal)
    linhas = []
    for rot, g in [("todos", h)] + [(str(c), x) for c, x in h.groupby("ciclo")]:
        linhas.append({"ciclo": rot, "habilitados": len(g), "cnpj_no_dio": int(g["cnpj_dio"].sum()),
                       "cnpj_no_portal": int(g["cnpj_portal"].sum()),
                       "cnpj_em_alguma_fonte": int((g["cnpj_dio"] | g["cnpj_portal"]).sum())})
    out = pd.DataFrame(linhas)
    out["pct_em_alguma_fonte"] = out["cnpj_em_alguma_fonte"] / out["habilitados"]
    m = t[t["cnpj_proponente_dv_ok"].astype(bool)].drop_duplicates("processo").merge(a, on="processo")
    out["processos_nas_duas_fontes"] = m["processo"].nunique()
    out["cnpj_igual_nas_duas"] = int((m["cnpj_proponente"] == m["cnpj_dio"]).sum())
    out["fonte"] = ("DIO-ES, avisos de resultado da LICC (dados/externos/dio_licc_trechos.csv); Portal da Transparência "
                    "(dados/processados/transparencia_licc_termos.csv); habilitados (dados/processados/habilitados.csv)")
    out.to_csv(TAB / "18_cobertura_cnpj.csv", index=False)
    print(out.drop(columns=["fonte"]).to_string(index=False))


if __name__ == "__main__":
    main()
