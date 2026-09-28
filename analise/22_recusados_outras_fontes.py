"""
22 — Os 32 projetos recusados pelo teto em 2023-2024: o que se observa deles depois, em fontes que não dependem de terem
recebido pela LICC (linha de base do resultado de H5).

Motivo (parecer externo de 27/09/2026, comentário 1 de H5): o relatório de execução da SECULT só existe para quem foi
financiado, e a ausência de relatório de um recusado não é prova de que o projeto não ocorreu. O resultado de H5 precisa
de fontes observáveis dos dois lados do corte. Aqui se mede, com dado público, quanto cada fonte cobre.

Fontes, todas com casamento exato (nunca por semelhança):
  LICC nos anos seguintes   analise/tabelas/09_reentrada_indeferidos.csv (captou em 2024, 2025, 2026)
  Lei Rouanet (SALIC)       cache da API em dados/externos/raw/salic/ (PRONACs de 2019 a 2025, mecenato), lido pela
                            função salic() de analise/15_licc_rouanet_proponentes.py; proponente pelo nome normalizado
                            exato (piso); PRONAC do ano da recusa em diante; título exato do projeto
  Agenda do Mapa Cultural   dados/externos/mapa_eventos_licc.csv (eventos ligados a processos da LICC), com o processo
                            do projeto tirado de dados/processados/habilitados.csv pelo título normalizado e pelo
                            proponente; evento com data no ano da recusa ou depois

Regras: ausência não é zero; "sem registro observado" quer dizer que nenhuma das fontes públicas registra o projeto, não
que ele deixou de ocorrer. O SALIC acumula a captação até a consulta, não a do ano. Pessoa física não é gravada.

Saídas (analise/tabelas/):
  22_recusados_outras_fontes.csv          um projeto recusado por linha, com o que cada fonte registra
  22_recusados_outras_fontes_resumo.csv   contagens por fonte e cobertura
Uso: python analise/22_recusados_outras_fontes.py
"""
from __future__ import annotations

import importlib.util
import re
import sys
import unicodedata
from pathlib import Path

import pandas as pd

RAIZ = Path(__file__).resolve().parents[1]
TAB = RAIZ / "analise" / "tabelas"
sys.path.insert(0, str(RAIZ / "analise"))


def _modulo(nome: str, arq: str):
    spec = importlib.util.spec_from_file_location(nome, RAIZ / "analise" / arq)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


carregar = _modulo("carregar", "01_carregar.py")
rouanet = _modulo("rouanet", "15_licc_rouanet_proponentes.py")


def titulo(s) -> str:
    s = "".join(c for c in unicodedata.normalize("NFD", str(s).lower()) if not unicodedata.combining(c))
    return " ".join(re.findall(r"[a-z0-9]+", s))


def main() -> None:
    r = pd.read_csv(TAB / "09_reentrada_indeferidos.csv")
    r["chave"] = r["proponente"].map(carregar.chave_proponente)
    r["titulo"] = r["projeto"].map(titulo)

    s = rouanet.salic()
    s["titulo"] = s["nome"].map(titulo)
    s = s[s["doc"].str.len() == 14]  # só pessoa jurídica

    h = pd.read_csv(RAIZ / "dados" / "processados" / "habilitados.csv")
    h["titulo"] = h["projeto"].map(titulo)
    ev = pd.read_csv(RAIZ / "dados" / "externos" / "mapa_eventos_licc.csv")
    ev["ano_evento"] = pd.to_datetime(ev["primeira_data"], errors="coerce").dt.year

    linhas = []
    for _, x in r.iterrows():
        ano = int(x["ano_recusa"])
        licc = [a for a in (2024, 2025, 2026) if a > ano and str(x.get(f"captou_{a}", "")).strip().lower() == "sim"]
        sp = s[(s["chave"] == x["chave"]) & (s["ano"] >= ano)]
        mesmo_titulo = s[(s["titulo"] == x["titulo"]) & (s["ano"] >= ano)]
        procs = set(h.loc[(h["titulo"] == x["titulo"]) & (h["chave_proponente"] == x["chave"]), "numero_processo"])
        e = ev[ev["numero_processo"].isin(procs) & (ev["ano_evento"] >= ano)]
        linha = {
            "ano_recusa": ano, "projeto": x["projeto"], "valor_recusado": x["valor_recusado"],
            "licc_captou_depois": bool(licc), "licc_anos": "; ".join(map(str, licc)),
            "rouanet_pronacs_do_proponente_desde_recusa": int(sp["PRONAC"].nunique()),
            "rouanet_pronacs_com_captacao": int(sp.loc[sp["valor_captado"] > 0, "PRONAC"].nunique()),
            "rouanet_mesmo_titulo": int(mesmo_titulo["PRONAC"].nunique()),
            "processos_licc_do_projeto": "; ".join(sorted(procs)),
            "mapa_eventos_datados_desde_recusa": int(len(e)),
        }
        linha["algum_registro"] = bool(linha["licc_captou_depois"] or linha["rouanet_pronacs_com_captacao"]
                                       or linha["rouanet_mesmo_titulo"] or linha["mapa_eventos_datados_desde_recusa"])
        linhas.append(linha)
    out = pd.DataFrame(linhas)
    out["fonte"] = ("09_reentrada_indeferidos.csv; SALIC (cache da API, 2019-2025, mecenato); mapa_eventos_licc.csv; "
                    "habilitados.csv; casamento exato por nome normalizado e título")
    out.to_csv(TAB / "22_recusados_outras_fontes.csv", index=False)

    n = len(out)
    resumo = pd.DataFrame([
        {"fonte": "LICC: captou em ano seguinte", "projetos": int(out["licc_captou_depois"].sum())},
        {"fonte": "Rouanet: proponente com PRONAC captado a partir do ano da recusa",
         "projetos": int((out["rouanet_pronacs_com_captacao"] > 0).sum())},
        {"fonte": "Rouanet: PRONAC com o mesmo título", "projetos": int((out["rouanet_mesmo_titulo"] > 0).sum())},
        {"fonte": "Mapa Cultural: evento do projeto datado a partir do ano da recusa",
         "projetos": int((out["mapa_eventos_datados_desde_recusa"] > 0).sum())},
        {"fonte": "alguma das fontes", "projetos": int(out["algum_registro"].sum())},
        {"fonte": "nenhuma das fontes (sem registro observado; não quer dizer que não ocorreu)",
         "projetos": int((~out["algum_registro"]).sum())},
    ])
    resumo["recusados"] = n
    resumo["pct"] = resumo["projetos"] / n
    resumo["cobertura"] = ("SALIC só até PRONACs de 2025 e com captação acumulada; Mapa só para projetos com processo "
                           "ligado a evento; Funcultura e PNAB sem lista estruturada no acervo (fora)")
    resumo.to_csv(TAB / "22_recusados_outras_fontes_resumo.csv", index=False)
    with pd.option_context("display.width", 220, "display.max_colwidth", 50):
        print(out.drop(columns=["fonte"]).to_string(index=False))
        print(resumo.drop(columns=["cobertura"]).to_string(index=False))


if __name__ == "__main__":
    main()
