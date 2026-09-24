"""
09 — Racionamento no teto e reentrada dos projetos recusados, 2023-2026 (revisão Stage 3, rodada 2: RV-2, RV-3).

Perguntas descritivas:
  (a) Em que anos houve termos de patrocínio recusados por falta de teto, e quantos? Os anexos "Recurso financeiro
      captado" de 2023 e 2024 publicam a lista de "termos de compromisso de patrocínio indeferidos por ultrapassar o
      montante"; os de 2025 e 2026 não publicam lista de recusados (ausência não é zero: fica "não publicado").
  (b) Quando cada cota do art. 18 se esgotou? Os anexos de 2025 e 2026 trazem a data e a hora de recebimento de cada
      termo validado, o que permite datar o preenchimento de cada cota.
  (c) Os projetos recusados em 2023 e 2024 captaram depois? Se sim, o grupo "recusado" da comparação na margem do
      racionamento (H1b) recebe o tratamento com atraso, e a comparação mede o efeito de receber agora × depois.

Fontes:
  dados/processados/indeferidos_2023_2024.csv      transcrição manual das listas de recusados dos anexos de 2023 e
                                                   2024 (um termo por linha); o script confere cada valor no texto
                                                   do anexo e a soma contra o total
  dados/fontes_web/paginas/secult_captados_{2023,2024,2025_v17,2026}_pdf.txt   anexos oficiais em texto (relé)
  dados/processados/captados_2025.csv              captados de 2025 estruturados (01_carregar.py)
  dados/processados/indeferidos_reentrada_verificacao.csv   decisão manual sobre cada candidato a reentrada
                                                   (mesmo projeto, outra edição ou falso positivo), após ler o
                                                   contexto no anexo
  analise/tabelas/03f_captacao_anual_secult.csv    montante e totais anuais (03f_captados_por_cota.py)
Saídas (analise/tabelas/):
  09_racionamento_por_ano.csv       por ano de captação: montante, lista de recusados publicada, recusados, cotas
  09_termos_2025_2026.csv           termos validados de 2025 e 2026: cota, valor, data e hora de recebimento
  09_cotas_2025_2026.csv            por cota: valor da cota, total impresso, soma lida, datas, data de preenchimento
  09_reentrada_candidatos.csv       ocorrências do título de cada recusado nos anexos seguintes, com contexto
  09_reentrada_indeferidos.csv      por projeto recusado: captou depois? em que ano? (só casos verificados)
  09_reentrada_resumo.csv           por ano de recusa: projetos, reentradas no ano seguinte e até 2026
Uso: python analise/09_racionamento_2023_2026.py
"""
from __future__ import annotations

import re
import unicodedata
from datetime import datetime
from pathlib import Path

import pandas as pd

RAIZ = Path(__file__).resolve().parents[1]
TAB = RAIZ / "analise" / "tabelas"
PAG = RAIZ / "dados" / "fontes_web" / "paginas"
PROC = RAIZ / "dados" / "processados"
ANEXOS = {2023: "secult_captados_2023_pdf.txt", 2024: "secult_captados_2024_pdf.txt",
          2025: "secult_captados_2025_v17_pdf.txt", 2026: "secult_captados_2026_pdf.txt"}
MARCA_RECUSADOS = "INDEFERIDOS POR ULTRAPASSAR"
CNPJ = re.compile(r"\d{2}\.\d{3}\.\d{3}\s?[/.]\s?\d{3,4}\s?[-/]\s?\d{2}")  # o anexo de 2026 traz "00.412.876.0001/45"
VALOR = re.compile(r"R\$\s*([\d.]+,\d{2})")
# data e hora de recebimento: "10/01/2025 às 14:06hs" (2025) ou "12/01/2026 11:51:50" (2026)
RECEBIMENTO = re.compile(r"(\d{2}/\d{2}/\d{4})\s*(?:às|as)?\s+(\d{1,2}:\d{2})(?::\d{2})?")
COTA = re.compile(r"^\s*(I|II|III|IV) - (\d+)%")
ROMANO = {"I": 1, "II": 2, "III": 3, "IV": 4}


def reais(s: str) -> float:
    return float(s.replace(".", "").replace(",", "."))


def brl(v: float) -> str:
    return "R$ " + f"{v:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", str(s)).encode("ascii", "ignore").decode().lower()
    return re.sub(r"\s+", " ", s)


def linhas(ano: int) -> list[str]:
    return (PAG / ANEXOS[ano]).read_text(encoding="utf-8").splitlines()


def cabecalho(ano: int) -> dict:
    """URL e sha256 do original, das três primeiras linhas do arquivo do relé."""
    ls = linhas(ano)[:3]
    url = next((l.split(": ", 1)[1] for l in ls if l.startswith("# Fonte:")), "")
    sha = next((l.split(": ", 1)[1] for l in ls if l.startswith("# sha256")), "")
    return {"fonte_url": url, "sha256_pdf": sha}


# ---------------------------------------------------------------------------------------------------------------
# (a) recusados de 2023 e 2024
# ---------------------------------------------------------------------------------------------------------------
def recusados() -> pd.DataFrame:
    d = pd.read_csv(PROC / "indeferidos_2023_2024.csv", dtype={"ano_captacao": int})
    for ano, g in d.groupby("ano_captacao"):
        texto = "\n".join(linhas(ano))
        secao = texto[texto.index(MARCA_RECUSADOS):]
        valores = [reais(v) for v in VALOR.findall(secao)]
        faltam = [v for v in g["valor_termo"] if not any(abs(v - x) < 0.005 for x in valores)]
        assert not faltam, f"{ano}: valores da transcrição ausentes no anexo: {faltam}"
    return d


# ---------------------------------------------------------------------------------------------------------------
# (b) termos validados de 2025 e 2026, com data de recebimento
# ---------------------------------------------------------------------------------------------------------------
def termos_validados(ano: int) -> tuple[pd.DataFrame, pd.DataFrame]:
    ls = linhas(ano)
    inicios = [i for i, l in enumerate(ls) if COTA.match(l)]
    fins = [i for i, l in enumerate(ls) if "Total Captado" in l and "Geral" not in l]
    assert len(inicios) == len(fins) == 4, (ano, inicios, fins)
    termos, cotas = [], []
    for (ini, fim) in zip(inicios, fins):
        romano, pct = COTA.match(ls[ini]).groups()
        bloco = " ".join(ls[ini:ini + 4])
        m_valor = re.search(r"Valor:?\s*R\$\s*([\d.]+,\d{2})", bloco)
        for i in range(ini + 1, fim):
            m = CNPJ.search(ls[i])
            if not m:
                continue
            v = VALOR.search(ls[i][m.end():])
            for j in (i + 1, i - 1):  # valor deslocado uma linha na diagramação
                if v:
                    break
                v = VALOR.search(ls[j][max(m.start() - 5, 0):])
            rec = None
            for dlt in (0, -1, 1, -2, 2, -3, 3):
                if 0 <= i + dlt < fim and (r := RECEBIMENTO.search(ls[i + dlt])):
                    rec = datetime.strptime(f"{r.group(1)} {r.group(2)}", "%d/%m/%Y %H:%M")
                    break
            termos.append({"ano_captacao": ano, "cota": ROMANO[romano], "linha": i + 1,
                           "cnpj_patrocinador": re.sub(r"\s", "", m.group(0)),
                           "valor_captado": reais(v.group(1)) if v else None, "recebimento": rec})
        # projeto com vários patrocinadores: a data de recebimento aparece uma vez, na linha do primeiro termo;
        # os termos seguintes do mesmo bloco herdam a data do termo anterior (marcados em recebimento_herdado)
        anterior = None
        for reg in termos:
            if reg["ano_captacao"] != ano or reg["cota"] != ROMANO[romano]:
                continue
            reg["recebimento_herdado"] = reg["recebimento"] is None and anterior is not None
            if reg["recebimento"] is None:
                reg["recebimento"] = anterior
            anterior = reg["recebimento"]
            reg["data_antes_do_ano"] = reg["recebimento"] is not None and reg["recebimento"].year < ano
        impresso = reais(VALOR.search(ls[fim]).group(1))
        cotas.append({"ano_captacao": ano, "cota": ROMANO[romano], "percentual": int(pct),
                      "valor_cota": reais(m_valor.group(1)) if m_valor else None, "total_impresso": impresso})
    return pd.DataFrame(termos), pd.DataFrame(cotas)


def resumo_cotas(t: pd.DataFrame, c: pd.DataFrame, montante: dict) -> pd.DataFrame:
    linhas_out = []
    for _, r in c.iterrows():
        g = t[(t.ano_captacao == r.ano_captacao) & (t.cota == r.cota)].sort_values("recebimento")
        valor_cota = r.valor_cota if pd.notna(r.valor_cota) else montante[r.ano_captacao] * r.percentual / 100
        acumulado = g["valor_captado"].cumsum()
        cheia = g.loc[acumulado >= valor_cota - 0.005, "recebimento"]
        linhas_out.append({
            "ano_captacao": r.ano_captacao, "cota": r.cota, "percentual": r.percentual,
            "valor_cota": valor_cota,
            "origem_valor_cota": "impresso no anexo" if pd.notna(r.valor_cota) else "percentual × montante",
            "total_impresso": r.total_impresso, "soma_lida": round(g["valor_captado"].sum(), 2),
            "confere": abs(g["valor_captado"].sum() - r.total_impresso) < 0.01,
            "termos": len(g), "termos_sem_data": int(g["recebimento"].isna().sum()),
            "termos_com_data_herdada": int(g["recebimento_herdado"].sum()),
            "datas_anteriores_ao_ano": int(g["data_antes_do_ano"].sum()),
            "primeiro_recebimento": g["recebimento"].min(), "ultimo_recebimento": g["recebimento"].max(),
            "recebimento_que_completa_a_cota": cheia.min() if len(cheia) else pd.NaT,
            "total_menos_cota": round(r.total_impresso - valor_cota, 2),
        })
    return pd.DataFrame(linhas_out)


# ---------------------------------------------------------------------------------------------------------------
# (c) reentrada dos recusados
# ---------------------------------------------------------------------------------------------------------------
def candidatos(rec: pd.DataFrame) -> pd.DataFrame:
    proj = rec.groupby(["ano_captacao", "projeto", "proponente", "chave_busca"], as_index=False)["valor_termo"].sum()
    cap25 = pd.read_csv(PROC / "captados_2025.csv")
    saida = []
    for _, p in proj.iterrows():
        chave = norm(p.chave_busca)
        for ano in (2024, 2025, 2026):
            if ano <= p.ano_captacao:
                continue
            ls = linhas(ano)
            corte = next((i for i, l in enumerate(ls) if MARCA_RECUSADOS in l), len(ls))  # só a parte de captados
            for i in range(corte):
                if chave in norm(ls[i]):
                    contexto = " / ".join(x.strip() for x in ls[max(i - 3, 0):i + 4] if x.strip())
                    saida.append({"ano_recusa": p.ano_captacao, "projeto": p.projeto, "ano_captacao": ano,
                                  "fonte": ANEXOS[ano], "linha": i + 1, "contexto": re.sub(r"\s+", " ", contexto)[:400]})
            if ano == 2025:
                for _, c in cap25[cap25["projeto"].map(norm).str.contains(re.escape(chave))].iterrows():
                    saida.append({"ano_recusa": p.ano_captacao, "projeto": p.projeto, "ano_captacao": ano,
                                  "fonte": "dados/processados/captados_2025.csv", "linha": int(c.linha_arquivo),
                                  "contexto": f"{c.projeto} | {c.proponente} | {brl(c.valor_captado)} | {c.patrocinador}"})
    return pd.DataFrame(saida).drop_duplicates(["ano_recusa", "projeto", "ano_captacao", "fonte", "linha"])


def reentrada(rec: pd.DataFrame, cand: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    ver = pd.read_csv(PROC / "indeferidos_reentrada_verificacao.csv")
    chaves = ["ano_recusa", "projeto", "ano_captacao"]
    pend = cand.merge(ver[chaves].drop_duplicates(), on=chaves, how="left", indicator=True)
    pend = pend[pend["_merge"] == "left_only"]
    if len(pend):
        print("ATENÇÃO — candidatos sem verificação manual (não contados):")
        print(pend[chaves + ["fonte", "linha"]].to_string(index=False))
    proj = rec.groupby(["ano_captacao", "projeto", "proponente"], as_index=False)["valor_termo"].agg(["sum", "size"])
    proj = proj.rename(columns={"ano_captacao": "ano_recusa", "sum": "valor_recusado", "size": "termos"})
    mesmo = ver[ver["decisao"] == "mesmo projeto"]
    for ano in (2024, 2025, 2026):
        ok = set(mesmo.loc[mesmo.ano_captacao == ano, "projeto"])
        proj[f"captou_{ano}"] = [("—" if ano <= a else ("sim" if p in ok else "não"))
                                 for a, p in zip(proj.ano_recusa, proj.projeto)]
    obs = ver.groupby("projeto")["obs"].apply(lambda s: "; ".join(x for x in s.dropna().astype(str) if x))
    proj["obs"] = proj["projeto"].map(obs).fillna("")
    res = []
    for a, g in proj.groupby("ano_recusa"):
        seguinte = g[f"captou_{a + 1}"].eq("sim")
        algum = g[[f"captou_{x}" for x in (2024, 2025, 2026) if x > a]].eq("sim").any(axis=1)
        res.append({"ano_recusa": a, "projetos_recusados": len(g), "termos_recusados": int(g.termos.sum()),
                    "valor_recusado": round(g.valor_recusado.sum(), 2),
                    "captaram_no_ano_seguinte": int(seguinte.sum()),
                    "captaram_ate_2026": int(algum.sum()),
                    "pct_ano_seguinte": seguinte.mean(), "pct_ate_2026": algum.mean(),
                    "nota": "casamento por título, verificado à mão no contexto do anexo; 2026 inclui termos "
                            "'em análise' (a cor que os distingue se perde no texto)"})
    return proj, pd.DataFrame(res)


# ---------------------------------------------------------------------------------------------------------------
def main() -> None:
    anual = pd.read_csv(TAB / "03f_captacao_anual_secult.csv").set_index("ano_captacao")
    montante = anual["montante_declarado"].to_dict()
    montante[2026] = 31_000_000.0 if pd.isna(montante.get(2026)) else montante[2026]

    rec = recusados()
    termos, cotas = [], []
    for ano in (2025, 2026):
        t, c = termos_validados(ano)
        termos.append(t)
        cotas.append(c)
    termos, cotas = pd.concat(termos), pd.concat(cotas)
    rc = resumo_cotas(termos, cotas, montante)
    termos.to_csv(TAB / "09_termos_2025_2026.csv", index=False)
    rc.to_csv(TAB / "09_cotas_2025_2026.csv", index=False)

    cand = candidatos(rec)
    cand.to_csv(TAB / "09_reentrada_candidatos.csv", index=False)
    proj, res = reentrada(rec, cand)
    proj.to_csv(TAB / "09_reentrada_indeferidos.csv", index=False)
    res.to_csv(TAB / "09_reentrada_resumo.csv", index=False)

    por_ano = []
    for ano in (2022, 2023, 2024, 2025, 2026):
        g = rec[rec.ano_captacao == ano]
        c = rc[rc.ano_captacao == ano]
        linha = {"ano_captacao": ano, "montante": montante.get(ano),
                 "lista_de_recusados_publicada": "sim" if len(g) else "não",
                 "projetos_recusados": g["projeto"].nunique() if len(g) else None,
                 "termos_recusados": len(g) if len(g) else None,
                 "valor_recusado": round(g["valor_termo"].sum(), 2) if len(g) else None,
                 "cotas_no_limite_ou_acima": int((c["total_menos_cota"] >= -0.005).sum()) if len(c) else None,
                 "total_listado": round(c["total_impresso"].sum(), 2) if len(c) else anual.loc[ano, "total_validado"],
                 **(cabecalho(ano) if ano in ANEXOS else {})}
        por_ano.append(linha)
    pd.DataFrame(por_ano).to_csv(TAB / "09_racionamento_por_ano.csv", index=False)

    with pd.option_context("display.width", 200, "display.max_columns", 20):
        print(pd.DataFrame(por_ano).drop(columns=["fonte_url", "sha256_pdf"], errors="ignore"))
        print(rc[["ano_captacao", "cota", "valor_cota", "total_impresso", "confere", "termos", "termos_sem_data",
                  "primeiro_recebimento", "recebimento_que_completa_a_cota", "ultimo_recebimento"]])
        print(res)


if __name__ == "__main__":
    main()
