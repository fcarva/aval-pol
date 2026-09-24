"""Confere cada número do artigo contra a tabela que o produz (auditoria ARS, Stage 2.5, Fase C).

Para cada afirmação numérica de artigo/rascunho-artigo.md há uma linha em CHECAGENS com:
  - o trecho literal do artigo (precisa existir no texto: se o texto mudar, a checagem acusa);
  - a função que recalcula o valor a partir de analise/tabelas/ ou dados/externos/;
  - a formatação usada no texto (vírgula decimal, arredondamento meio-para-cima).
A checagem passa quando o valor recalculado e formatado aparece dentro do trecho.

Saída: artigo/auditoria/checagem_dados.csv (id, status, exibido, recalculado, fonte, trecho).
Uso:   python artigo/auditoria/checar_dados.py      (código de saída 1 se algo divergir)
"""
from __future__ import annotations

import csv
import sys
from decimal import ROUND_HALF_UP, Decimal
from pathlib import Path

import pandas as pd

RAIZ = Path(__file__).resolve().parents[2]
ART = RAIZ / "artigo" / "rascunho-artigo.md"
TAB = RAIZ / "analise" / "tabelas"
EXT = RAIZ / "dados" / "externos"
SAIDA = Path(__file__).with_name("checagem_dados.csv")
TOTAL = "2022-2026 (processos distintos)"


def ler(caminho: Path) -> pd.DataFrame:
    return pd.read_csv(caminho, comment="#")


def arred(x: float, casas: int) -> str:
    q = Decimal(1).scaleb(-casas)
    return str(Decimal(repr(float(x))).quantize(q, rounding=ROUND_HALF_UP)).replace(".", ",")


def pct(x: float, casas: int = 0) -> str:
    return arred(100 * x, casas) + "%"


def num(x: float, casas: int = 0) -> str:
    return arred(x, casas)


# ---------------------------------------------------------------- tabelas de origem
anual = ler(TAB / "03_anual.csv").set_index("ciclo")
status = ler(TAB / "03_status_por_ciclo.csv").set_index("ciclo")
bunch = ler(TAB / "03_bunching_teto.csv").set_index("ciclo")
prop = ler(TAB / "03_proponentes_por_ciclo.csv").set_index("ciclo")
recor = ler(TAB / "03_proponentes_recorrencia.csv")
terr = ler(TAB / "03_territorio_indicadores.csv").set_index("indicador")["valor"]
rmgv = ler(TAB / "03_territorio_rmgv_interior.csv").set_index("grupo")
muni = ler(TAB / "03_municipios.csv").set_index("municipio")
patr = ler(TAB / "03_patrocinadores_concentracao.csv").set_index("indicador")["valor"]
macro = ler(TAB / "03_patrocinadores_macrossetor.csv").set_index("macrossetor")
faixa = ler(TAB / "03_status_conversao_por_faixa_valor_e_ciclo.csv")
coorte = ler(TAB / "03_coortes_primeira_presenca_canonico.csv").set_index("primeiro_ciclo")
f13m = ler(TAB / "03e_f13_municipal_rmgv_interior.csv")
d1 = ler(TAB / "05_poder_d1_proponente.csv")
tipo_m = ler(TAB / "05_poder_tipo_m.csv")
deff = ler(TAB / "05_poder_deff_proponente.csv")
anu = ler(TAB / "03f_captacao_anual_secult.csv").set_index("ano_captacao")
cota = ler(TAB / "03f_captados_por_cota.csv").dropna(subset=["cota"]).set_index(["ano_captacao", "cota"])
mun_did = ler(TAB / "05_poder_mde_municipal_did.csv")
ilustr = ler(TAB / "licc_emd_ilustrativo.csv")
capt = ler(TAB / "licc_captados_2025_totais.csv").iloc[0]
capt_res = ler(TAB / "03_captados_resumo.csv").set_index("indicador")["valor"]
teto = ler(EXT / "licc_teto_vs_icms.csv").set_index("ano_teto")
munic = ler(EXT / "munic2021_cultura_es_resumo.csv").set_index(["item", "grupo"])
siic = ler(EXT / "siic_uf.csv")


def siic_2024() -> tuple[float, float, int]:
    o = siic[siic.indicador == "ocupados_setor_cultural_pnadc"].pivot(index="localidade", columns="ano", values="valor")[2024]
    t = siic[siic.indicador == "ocupados_14mais_pnadc"].pivot(index="localidade", columns="ano", values="valor")[2024]
    sh = (o / t).sort_values(ascending=False)
    return float(sh["ES"]), float(o.sum() / t.sum()), list(sh.index).index("ES") + 1


def d1_emd(r2: float, icc: float, poder: float) -> float:
    s = d1[(d1.R2_hipotese == r2) & (d1.icc_hipotese == icc) & (d1.poder == poder)]
    return float(s["EMD_dp"].iloc[0])


def ilustr_emd(recorte: str, poder: float) -> float:
    return float(ilustr[(ilustr.recorte == recorte) & (ilustr.poder == poder)]["emd_dp"].iloc[0])


def f13(ano: int, grupo: str) -> float:
    return float(f13m[(f13m.ano == ano) & (f13m.grupo == grupo)]["f13_per_capita"].iloc[0])


def razao_autorizado_teto() -> list[float]:
    # soma autorizada do ciclo / teto do ano seguinte (ano em que o ciclo capta)
    return [anual.loc[str(c), "autorizado_total"] / teto.loc[c + 1, "teto_renuncia"] for c in range(2022, 2026)]


def recorrentes(col: str) -> float:
    return float(recor.loc[recor.n_ciclos >= 3, col].sum())


def faixa_taxa(ciclo: int, fx: str) -> float:
    return float(faixa[(faixa.ciclo == ciclo) & (faixa.faixa_valor_ciclo == fx)]["taxa_execucao"].iloc[0])


rec = ler(TAB / "03_status_conversao_recorrencia_2023_2024.csv")
conv_ter = ler(TAB / "03_status_conversao_rmgv_interior_2022_2024.csv").set_index("territorio")
capt_ter = ler(TAB / "03_captados_perfil_territorial.csv").iloc[0]
f13_int = f13m[(f13m.ano == 2025) & (f13m.grupo == "Interior")].iloc[0]


def conv_rec(tipo: str) -> float:
    return float(rec[(rec.ciclo == "2023-2024") & (rec.proponente == tipo)]["taxa_execucao"].iloc[0])


ES_SH, BR_SH, ES_RANK = siic_2024()
RAZ = razao_autorizado_teto()
F13_TETO = [teto.loc[a, "teto_sobre_f13_estado"] for a in range(2022, 2026)]
F13_EF = [anu.loc[a, "validado_sobre_f13_estado"] for a in range(2022, 2026)]
S = {c: status.loc[c] for c in (2022, 2023, 2024)}
N_RES = sum(S[c]["resolvidos"] for c in S)
N_EXE = sum(S[c]["executados"] for c in S)
N_EXP = sum(S[c]["captacao_expirada"] for c in S)
N_PROP = int(d1["proponentes"].iloc[0])

# versão de 24/09/2026 (teoria da mudança com H1-H3): tabelas do script 07
fun07 = ler(TAB / "07_funil_por_ciclo.csv").set_index("ciclo")
cap07 = ler(TAB / "07_funil_captacao_anual.csv").set_index("ano_captacao")
comp07 = ler(TAB / "07_composicao_por_ciclo.csv").set_index("ciclo")
mapa07 = ler(TAB / "07_mapa_cultural_universo.csv").set_index("recorte")
rouan07 = ler(TAB / "07_patrocinadores_na_rouanet.csv", ) if False else pd.read_csv(TAB / "07_patrocinadores_na_rouanet.csv", dtype={"cnpj": str, "cnpj_raiz": str})
poder07 = ler(TAB / "07_poder_hipoteses.csv")


def milhar(x: float) -> str:
    return f"{int(round(x)):,}".replace(",", ".")


def rouanet_empresas() -> tuple[int, int, float]:
    r = rouan07.groupby("cnpj_raiz").agg(a=("aportado_licc_2025", "sum"), inc=("incentivador_rouanet", "any"))
    return int(r.inc.sum()), int(len(r)), float(r[r.inc].a.sum() / r.a.sum())


def faixa_emd(desenho: str, casas: int = 0, fator: float = 100) -> str:
    v = poder07[poder07.desenho == desenho]["emd_pontos"] * fator
    return f"{num(v.min(), casas)} a {num(v.max(), casas)}"


ROU_N, ROU_T, ROU_SH = rouanet_empresas()
RES07 = fun07.loc[[2022, 2023, 2024]]
N1_07, N0_07 = int(RES07["captou"].sum()), int(RES07["expirou"].sum())
H1B_NOTA = poder07[poder07.desenho.str.startswith("captou")]["nota"].iloc[0]

T = "analise/tabelas/"
# (id, trecho literal do artigo, valor formatado recalculado, fonte)
CHECAGENS = [
    ("D01", "anexos oficiais de 463 projetos habilitados", str(int(anual.loc[TOTAL, "processos"])), T + "03_anual.csv"),
    ("D02", "onde fica 67% do valor atribuível", pct(rmgv.loc["RMGV", "share_autorizado_atribuivel"]), T + "03_territorio_rmgv_interior.csv"),
    ("D03", "duas empresas respondem por metade da renúncia de 2025",
     {2: "duas"}.get(int(float(patr["empresas_para_metade"])), "?"), T + "03_patrocinadores_concentracao.csv"),
    ("D04", "detecta efeitos a partir de 0,25 a 0,45 desvio-padrão",
     f"{num(d1.EMD_dp.min(), 2)} a {num(d1.EMD_dp.max(), 2)}", T + "05_poder_d1_proponente.csv"),
    ("D05", "passou de R\\$ 15 milhões em 2023 para R\\$ 31 milhões em 2026",
     f"R\\$ {num(teto.loc[2023, 'teto_renuncia'] / 1e6)} milhões em 2023 para R\\$ {num(teto.loc[2026, 'teto_renuncia'] / 1e6)} milhões",
     "dados/externos/licc_teto_vs_icms.csv"),
    ("D06", "463 projetos foram habilitados a captar R\\$ 184 milhões nos cinco ciclos (459 com valor publicado)",
     f"{int(anual.loc[TOTAL, 'processos'])} projetos foram habilitados a captar R\\$ {num(anual.loc[TOTAL, 'autorizado_total'] / 1e6)} milhões "
     f"nos cinco ciclos ({int(anual.loc[TOTAL, 'autorizado_n'])} com valor publicado)", T + "03_anual.csv"),
    ("D07", "em 2025, 63 projetos captaram exatamente R\\$ 25.000.000,00",
     f"{int(capt['projetos'])} projetos captaram exatamente R\\$ {int(capt['soma_valor_captado']):,}".replace(",", ".") + ",00",
     T + "licc_captados_2025_totais.csv"),
    ("D08", "ocupava 4,2% dos trabalhadores do ES, contra 5,8% no país, a 18ª participação",
     f"{pct(ES_SH, 1)} dos trabalhadores do ES, contra {pct(BR_SH, 1)} no país, a {ES_RANK}ª", "dados/externos/siic_uf.csv"),
    ("D09", "95% da população da Região Metropolitana da Grande Vitória (RMGV) vivia em município com cinema, contra 34%",
     f"{pct(munic.loc[('cinema', 'RMGV'), 'pct_pop_em_mun_com_sim'])} da população da Região Metropolitana da Grande Vitória (RMGV) "
     f"vivia em município com cinema, contra {pct(munic.loc[('cinema', 'Interior'), 'pct_pop_em_mun_com_sim'])}",
     "dados/externos/munic2021_cultura_es_resumo.csv"),
    ("D10", "metade dos municípios do interior não tinha fundo municipal de cultura e só 16% tinham plano municipal",
     ("metade" if abs(munic.loc[("fundo_municipal_cultura", "Interior"), "pct_mun_sim_sobre_validos"] - 0.5) < 0.01 else "?")
     + f" dos municípios do interior não tinha fundo municipal de cultura e só "
       f"{pct(munic.loc[('plano_municipal_cultura', 'Interior'), 'pct_mun_sim_sobre_validos'])}",
     "dados/externos/munic2021_cultura_es_resumo.csv"),
    ("D11", "a renúncia efetiva equivale a 14% a 21% do gasto estadual direto", f"{pct(min(F13_EF))} a {pct(max(F13_EF))}",
     T + "03f_captacao_anual_secult.csv (validado_sobre_f13_estado, 2022-2025)"),
    ("D12", "| | Renúncia efetiva / gasto estadual na função cultura, 2022-2025 | 14% a 21% |", f"{pct(min(F13_EF))} a {pct(max(F13_EF))}",
     T + "03f_captacao_anual_secult.csv"),
    ("D13", "| Teto de 2025 / ICMS estadual de 2024 | 0,16% |", pct(teto.loc[2025, "teto_sobre_icms_estadual_base"], 2),
     "dados/externos/licc_teto_vs_icms.csv"),
    ("D14", "ciclos 2022-2025 | 1,1 a 1,9 |", f"{num(min(RAZ), 1)} a {num(max(RAZ), 1)}",
     T + "03_anual.csv ÷ dados/externos/licc_teto_vs_icms.csv (teto do ano seguinte)"),
    ("D15", "| | Captado / montante do ano (2023; 2024; 2025) | 100%; 100%; 100% |",
     "; ".join(pct(anu.loc[a, "total_validado"] / anu.loc[a, "montante_declarado"]) for a in (2023, 2024, 2025)),
     T + "03f_captacao_anual_secult.csv"),
    ("D61", "| | Termos de patrocínio indeferidos por exceder o montante / montante (2023; 2024) | 28%; 35% |",
     "; ".join(pct(anu.loc[a, "indeferido_sobre_montante"]) for a in (2023, 2024)), T + "03f_captacao_anual_secult.csv"),
    ("D62", "termos de patrocínio que somavam 28% e 35% dele",
     " e ".join(pct(anu.loc[a, "indeferido_sobre_montante"]) for a in (2023, 2024)), T + "03f_captacao_anual_secult.csv"),
    ("D63", "a de planos plurianuais 93% e a de projetos fora da RMGV 107%",
     f"plurianuais {pct(cota.loc[(2025, 'II'), 'captado_sobre_reservado'])} e a de projetos fora da RMGV {pct(cota.loc[(2025, 'III'), 'captado_sobre_reservado'])}",
     T + "03f_captados_por_cota.csv"),
    ("D64", "as reservas I e IV captaram exatamente o valor reservado",
     "exatamente" if all(abs(cota.loc[(2025, k), "captado_sobre_reservado"] - 1) < 1e-9 for k in ("I", "IV")) else "?",
     T + "03f_captados_por_cota.csv"),
    ("D65", "a Portaria SEFAZ nº 09-R fixou R\\$ 10 milhões, e o anexo de captação da SECULT informa R\\$ 15 milhões disponíveis (R\\$ 11,5 milhões validados)",
     f"fixou R\\$ {num(teto.loc[2022, 'teto_renuncia'] / 1e6)} milhões, e o anexo de captação da SECULT informa R\\$ "
     f"{num(anu.loc[2022, 'montante_declarado'] / 1e6)} milhões disponíveis (R\\$ {num(anu.loc[2022, 'total_validado'] / 1e6, 1)} milhões",
     T + "03f_captacao_anual_secult.csv; dados/externos/licc_teto_vs_icms.csv"),
    ("D16", "(2022; 2023; 2024) | 16%; 30%; 45% |",
     "; ".join(pct(S[c]["taxa_expiracao_sobre_resolvidos"]) for c in S), T + "03_status_por_ciclo.csv"),
    ("D17", "(2022 → 2026) | 13% → 41% |",
     f"{pct(bunch.loc['2022', 'pct_exatamente_500mil'])} → {pct(bunch.loc['2026', 'pct_exatamente_500mil'])}", T + "03_bunching_teto.csv"),
    ("D18", "(2025; 2026) | 63%; 51% |",
     f"{pct(prop.loc['2025', 'pct_proponentes_ja_vistos_em_ciclo_anterior'])}; {pct(prop.loc['2026', 'pct_proponentes_ja_vistos_em_ciclo_anterior'])}",
     T + "03_proponentes_por_ciclo.csv"),
    ("D19", "parcela dos proponentes e do valor | 17%; 47% |",
     f"{pct(recorrentes('pct_proponentes'))}; {pct(recorrentes('pct_autorizado'))}", T + "03_proponentes_recorrencia.csv"),
    ("D20", "os 17% que aparecem em três ou mais ciclos ficam com 47% do valor",
     f"os {pct(recorrentes('pct_proponentes'))} que aparecem em três ou mais ciclos ficam com {pct(recorrentes('pct_autorizado'))}",
     T + "03_proponentes_recorrencia.csv"),
    ("D21", "| Parcela da RMGV: população; valor atribuível | 49%; 67% |",
     f"{pct(rmgv.loc['RMGV', 'share_pop_censo2022'])}; {pct(rmgv.loc['RMGV', 'share_autorizado_atribuivel'])}",
     T + "03_territorio_rmgv_interior.csv"),
    ("D22", "A RMGV tem 49% da população e fica com 67% do valor",
     f"{pct(rmgv.loc['RMGV', 'share_pop_censo2022'])} da população e fica com {pct(rmgv.loc['RMGV', 'share_autorizado_atribuivel'])}",
     T + "03_territorio_rmgv_interior.csv"),
    ("D23", "| Vitória: população; valor atribuível | 8%; 48% |",
     f"{pct(muni.loc['Vitória', 'share_pop'])}; {pct(muni.loc['Vitória', 'share_valor'])}", T + "03_municipios.csv"),
    ("D24", "Vitória, com 8% da população, fica com 48%",
     f"{pct(muni.loc['Vitória', 'share_pop'])} da população, fica com {pct(muni.loc['Vitória', 'share_valor'])}", T + "03_municipios.csv"),
    ("D25", "entre os 78 municípios | 0,88 |", num(float(terr["gini_valor_78"]), 2), T + "03_territorio_indicadores.csv"),
    ("D26", "O Gini do valor entre os 78 municípios é 0,88, acima do Gini da população (0,64) e do PIB (0,75)",
     f"é {num(float(terr['gini_valor_78']), 2)}, acima do Gini da população ({num(float(terr['gini_populacao_78']), 2)}) "
     f"e do PIB ({num(float(terr['gini_pib_78']), 2)})", T + "03_territorio_indicadores.csv"),
    ("D27", "Municípios sem nenhum projeto habilitado em 2022-2026 | 14 |", str(int(rmgv.loc["ES", "municipios_sem_presenca"])),
     T + "03_territorio_rmgv_interior.csv"),
    ("D28", "14 municípios do interior não tiveram nenhum projeto habilitado",
     f"{int(rmgv.loc['Interior', 'municipios_sem_presenca'])} municípios do interior"
     + ("" if rmgv.loc["RMGV", "municipios_sem_presenca"] == 0 else " [RMGV também]"), T + "03_territorio_rmgv_interior.csv"),
    ("D29", "Empresas (raiz do CNPJ); maior empresa (distribuidora de energia) | 26; 44% |",
     f"{int(float(patr['empresas']))}; {pct(float(patr['CR1']))}", T + "03_patrocinadores_concentracao.csv"),
    ("D30", "parcela de energia e gás | 2; 52% |",
     f"{int(float(patr['empresas_para_metade']))}; {pct(macro.loc['Energia e gás (serviço regulado)', 'share'])}",
     T + "03_patrocinadores_concentracao.csv; 03_patrocinadores_macrossetor.csv"),
    ("D31", "em 2025, 26 empresas patrocinadoras (46 estabelecimentos), das quais a distribuidora de energia respondeu por 44% da renúncia, e empresas de energia e gás, serviços regulados, por 52%",
     f"{int(float(patr['empresas']))} empresas patrocinadoras ({int(capt_res['cnpjs_estabelecimento'])} estabelecimentos), das quais a distribuidora "
     f"de energia respondeu por {pct(float(patr['CR1']))} da renúncia, e empresas de energia e gás, serviços regulados, por "
     f"{pct(macro.loc['Energia e gás (serviço regulado)', 'share'])}",
     T + "03_patrocinadores_concentracao.csv; 03_patrocinadores_macrossetor.csv; 03_captados_resumo.csv"),
    ("D32", "projetos com um único município de execução (74% do valor autorizado)",
     pct(float(str(terr["cobertura_valor_atribuivel"]).split(";")[1].split()[0])), T + "03_territorio_indicadores.csv"),
    ("D33", "o retrato territorial cobre 74% do valor",
     pct(float(str(terr["cobertura_valor_atribuivel"]).split(";")[1].split()[0])), T + "03_territorio_indicadores.csv"),
    ("D34", "78% contra 27% no ciclo 2024",
     f"{pct(faixa_taxa(2024, 'exatamente 500 mil'))} contra {pct(faixa_taxa(2024, 'até 400 mil'))} no ciclo 2024",
     T + "03_status_conversao_por_faixa_valor_e_ciclo.csv"),
    ("D35", "A parcela de pedidos no teto exato triplicou entre 2022 e 2026",
     "triplicou" if round(bunch.loc["2026", "pct_exatamente_500mil"] / bunch.loc["2022", "pct_exatamente_500mil"]) == 3 else "?",
     T + "03_bunching_teto.csv"),
    ("D36", "subiu de 16% para 45% à medida que a habilitação quase dobrou",
     f"subiu de {pct(S[2022]['taxa_expiracao_sobre_resolvidos'])} para {pct(S[2024]['taxa_expiracao_sobre_resolvidos'])} "
     + ("à medida que a habilitação quase dobrou" if 1.7 <= S[2024]["total"] / S[2022]["total"] < 2 else "?"),
     T + "03_status_por_ciclo.csv"),
    ("D37", "a diferença entre RMGV e interior explica só 7% do total", f"explica só {pct(float(terr['pct_theil_entre_grupos']))}",
     T + "03_territorio_indicadores.csv"),
    ("D38", "maior por habitante no interior (R\\$ 93) que na RMGV (R\\$ 59) em 2025",
     f"interior (R\\$ {num(f13(2025, 'Interior'))}) que na RMGV (R\\$ {num(f13(2025, 'RMGV'))}) em 2025",
     T + "03e_f13_municipal_rmgv_interior.csv"),
    ("D39", "O valor autorizado de cada ciclo foi de 1,1 a 1,9 vez o teto", f"{num(min(RAZ), 1)} a {num(max(RAZ), 1)} vez",
     T + "03_anual.csv ÷ dados/externos/licc_teto_vs_icms.csv"),
    ("D41", "coortes de 39, 16, 3, 3 e 3 municípios entre 2022 e 2026, e 14 nunca tratados",
     "coortes de " + ", ".join(str(int(coorte.loc[str(c), "municipios"])) for c in range(2022, 2026))
     + f" e {int(coorte.loc['2026', 'municipios'])} municípios entre 2022 e 2026, e {int(coorte.loc['nunca (2022-2026)', 'municipios'])} nunca",
     T + "03_coortes_primeira_presenca_canonico.csv"),
    ("D42", "A população são os 305 projetos habilitados nos ciclos 2022-2024, dos quais 293 já tinham situação resolvida (198 captaram e 95 tiveram o prazo expirado), de 199 proponentes",
     f"os {int(sum(S[c]['total'] for c in S))} projetos habilitados nos ciclos 2022-2024, dos quais {int(N_RES)} já tinham situação "
     f"resolvida ({int(N_EXE)} captaram e {int(N_EXP)} tiveram o prazo expirado), de {N_PROP} proponentes",
     T + "03_status_por_ciclo.csv; 05_poder_d1_proponente.csv"),
    ("D43", "em que $n$ = 293 projetos, $P$ = 0,676 é a fração tratada",
     f"$n$ = {int(d1.n_projetos.iloc[0])} projetos, $P$ = {num(N_EXE / N_RES, 3)}", T + "05_poder_d1_proponente.csv"),
    ("D44", "$\\bar m$ = 1,47 projeto por proponente", f"$\\bar m$ = {num(N_RES / N_PROP, 2)}", T + "05_poder_d1_proponente.csv"),
    ("D45", "| Sem covariáveis, sem correlação intraproponente | 0,35 | 0,41 |",
     f"| {num(d1_emd(0, 0, .8), 2)} | {num(d1_emd(0, 0, .9), 2)} |", T + "05_poder_d1_proponente.csv"),
    ("D46", "| Sem covariáveis, ρ = 0,2 | 0,39 | 0,45 |", f"| {num(d1_emd(0, .2, .8), 2)} | {num(d1_emd(0, .2, .9), 2)} |",
     T + "05_poder_d1_proponente.csv"),
    ("D47", "| R² = 0,3, ρ = 0 | 0,29 | 0,34 |", f"| {num(d1_emd(.3, 0, .8), 2)} | {num(d1_emd(.3, 0, .9), 2)} |",
     T + "05_poder_d1_proponente.csv"),
    ("D48", "| R² = 0,5, ρ = 0 | 0,25 | 0,29 |", f"| {num(d1_emd(.5, 0, .8), 2)} | {num(d1_emd(.5, 0, .9), 2)} |",
     T + "05_poder_d1_proponente.csv"),
    ("D49", "| R² = 0,5, ρ = 0,2 | 0,28 | 0,32 |", f"| {num(d1_emd(.5, .2, .8), 2)} | {num(d1_emd(.5, .2, .9), 2)} |",
     T + "05_poder_d1_proponente.csv"),
    ("D50", "| Um ciclo isolado (2023 ou 2024), sem covariáveis | 0,53 a 0,58 | 0,62 a 0,67 |",
     f"| {num(ilustr_emd('ciclo 2024', .8), 2)} a {num(ilustr_emd('ciclo 2023', .8), 2)} | "
     f"{num(ilustr_emd('ciclo 2024', .9), 2)} a {num(ilustr_emd('ciclo 2023', .9), 2)} |", T + "licc_emd_ilustrativo.csv"),
    ("D51", "| Municipal, 78 municípios, 25% a 50% tratados | 0,43 a 1,04 |",
     f"| {num(mun_did.MDE_em_dp_idiossincratico_SCR.min(), 2)} a {num(mun_did.MDE_em_dp_idiossincratico_SCR.max(), 2)} |",
     T + "05_poder_mde_municipal_did.csv"),
    ("D52", "Com poder de 17%, a estimativa significativa superestima em média o efeito verdadeiro 2,5 vezes",
     f"Com poder de {pct(float(tipo_m.loc[tipo_m.efeito_verdadeiro_sobre_ep == 1.0, 'poder'].iloc[0]))}, a estimativa significativa "
     f"superestima em média o efeito verdadeiro {num(float(tipo_m.loc[tipo_m.efeito_verdadeiro_sobre_ep == 1.0, 'razao_exagero_tipo_M'].iloc[0]), 1)} vezes",
     T + "05_poder_tipo_m.csv"),
    ("D54", "71% dos projetos de proponentes já habilitados antes foram executados, contra 57% dos de estreantes",
     f"{pct(conv_rec('recorrente'))} dos projetos de proponentes já habilitados antes foram executados, contra {pct(conv_rec('estreante'))}",
     T + "03_status_conversao_recorrencia_2023_2024.csv"),
    ("D55", "a taxa de execução pouco difere entre RMGV e interior (68% e 63%)",
     f"({pct(conv_ter.loc['RMGV', 'taxa_execucao'])} e {pct(conv_ter.loc['Interior', 'taxa_execucao'])})",
     T + "03_status_conversao_rmgv_interior_2022_2024.csv"),
    ("D56", "com um único município identificado (42 de 63), 61% do valor captado ficou na RMGV",
     f"({int(capt_ter['com_municipio_unico'])} de {int(capt_ter['captados_total'])}), {pct(capt_ter['pct_captado_rmgv_entre_unicos'])} do valor captado",
     T + "03_captados_perfil_territorial.csv (casamento principal)"),
    ("D57", "(69 dos 71 municípios do interior com dado no SICONFI)",
     f"({int(f13_int['municipios_com_valor'])} dos {int(f13_int['municipios'])} municípios do interior",
     T + "03e_f13_municipal_rmgv_interior.csv"),
    ("D58", "(3 expirados em 56 resolvidos no ciclo 2025)",
     f"({int(status.loc[2025, 'captacao_expirada'])} expirados em {int(status.loc[2025, 'resolvidos'])} resolvidos",
     T + "03_status_por_ciclo.csv"),
    ("D59", "com coeficiente de variação $cv$ = 0,73 do tamanho das carteiras",
     f"$cv$ = {num(float(deff.cv_tamanho.iloc[0]), 2)}", T + "05_poder_deff_proponente.csv"),
    ("D60", "| Sem covariáveis, ρ = 0,2 | 0,39 | 0,45 |",
     f"| {num(float(deff.loc[deff.icc_hipotese == 0.2, 'MDE_dp_com_deff_cv'].iloc[0]), 2)} |", T + "05_poder_deff_proponente.csv (EMD com efeito de desenho ajustado por cv)"),
    ("D53", "O universo disponível detecta, portanto, efeitos a partir de 0,25 a 0,45 desvio-padrão",
     f"{num(d1.EMD_dp.min(), 2)} a {num(d1.EMD_dp.max(), 2)}", T + "05_poder_d1_proponente.csv"),
]

# ---- versão de 24/09/2026: seções 4-6 reescritas (teoria da mudança, auditoria das premissas, perguntas H1-H3).
# Checagens D01-D64 cujo trecho saiu do texto foram retiradas; ficam as que ainda se aplicam.
T7 = T + "07_"
CHECAGENS = [c for c in CHECAGENS if c[0] in {"D03", "D05", "D06", "D07", "D08", "D09", "D10", "D11", "D22", "D33", "D65"}]
CHECAGENS += [
    ("N01", "termos equivalentes a 28% e 35% do montante foram indeferidos",
     f"{pct(anu.loc[2023, 'indeferido_sobre_montante'])} e {pct(anu.loc[2024, 'indeferido_sobre_montante'])}", T + "03f_captacao_anual_secult.csv"),
    ("N02", "Entre os 25.441 agentes cadastrados no Mapa Cultural", milhar(mapa07.loc["todos", "agentes"]), T7 + "mapa_cultural_universo.csv"),
    ("N03", "| Agentes culturais cadastrados no Mapa Cultural (coletivos) | 25.441 (2.592) |",
     f"{milhar(mapa07.loc['todos', 'agentes'])} ({milhar(mapa07.loc['coletivo (type=2)', 'agentes'])})", T7 + "mapa_cultural_universo.csv"),
    ("N04", "68% dos habilitados de 2022-2024 com situação resolvida captaram", pct(N1_07 / (N1_07 + N0_07)), T7 + "funil_por_ciclo.csv"),
    ("N05", "| Projetos habilitados; proponentes por ciclo | 305; 53, 92 e 95 |",
     f"{int(RES07['habilitados'].sum())}; {int(comp07.loc[2022, 'proponentes'])}, {int(comp07.loc[2023, 'proponentes'])} e {int(comp07.loc[2024, 'proponentes'])}",
     T7 + "funil_por_ciclo.csv; 07_composicao_por_ciclo.csv"),
    ("N06", "| Habilitados com situação resolvida; captaram | 293; 198 |", f"{N1_07 + N0_07}; {N1_07}", T7 + "funil_por_ciclo.csv"),
    ("N07", "| Taxa de captação entre os resolvidos | 84%; 70%; 55% |",
     "; ".join(pct(fun07.loc[c, "taxa_captou_sobre_resolvidos"]) for c in (2022, 2023, 2024)), T7 + "funil_por_ciclo.csv"),
    ("N08", "| Valor com patrocinador que coube no teto | 78%; 74% |",
     f"{pct(1 / cap07.loc[2023, 'demanda_com_patrocinador_sobre_montante'])}; {pct(1 / cap07.loc[2024, 'demanda_com_patrocinador_sobre_montante'])}",
     T7 + "funil_captacao_anual.csv"),
    ("N09", "Estreantes: 56 no ciclo 2024, 26 em 2025, 40 em 2026",
     f"{int(comp07.loc[2024, 'estreantes_janela_2'])} no ciclo 2024, {int(comp07.loc[2025, 'estreantes_janela_2'])} em 2025, {int(comp07.loc[2026, 'estreantes_janela_2'])} em 2026",
     T7 + "composicao_por_ciclo.csv"),
    ("N10", "14 municípios do interior nunca tiveram projeto habilitado", str(int(coorte.loc["nunca (2022-2026)", "municipios"])),
     T + "03_coortes_primeira_presenca_canonico.csv"),
    ("N11", "Em 2022-2024, 95 de 293 habilitados expiraram sem captar", f"{N0_07} de {N1_07 + N0_07}", T7 + "funil_por_ciclo.csv"),
    ("N12", "Duas empresas somam metade da renúncia de 2025; energia e gás, 52%",
     f"{ {2: 'Duas'}.get(int(float(patr['empresas_para_metade'])), '?')} empresas somam metade da renúncia de 2025; energia e gás, "
     f"{pct(macro.loc['Energia e gás (serviço regulado)', 'share'])}", T + "03_patrocinadores_concentracao.csv; 03_patrocinadores_macrossetor.csv"),
    ("N13", "Execução de 68% na RMGV e 63% no interior",
     f"{pct(conv_ter.loc['RMGV', 'taxa_execucao'])} na RMGV e {pct(conv_ter.loc['Interior', 'taxa_execucao'])}", T + "03_status_conversao_rmgv_interior_2022_2024.csv"),
    ("N14", "Recorrentes captam mais (71% contra 57%)",
     f"{pct(float(rec[(rec.ciclo == '2023-2024') & (rec.proponente == 'recorrente')].taxa_execucao.iloc[0]))} contra "
     f"{pct(float(rec[(rec.ciclo == '2023-2024') & (rec.proponente == 'estreante')].taxa_execucao.iloc[0]))}", T + "03_status_conversao_recorrencia_2023_2024.csv"),
    ("N15", "termos com patrocinador de 28% e 35% do montante foram indeferidos pela ordem de chegada",
     f"{pct(anu.loc[2023, 'indeferido_sobre_montante'])} e {pct(anu.loc[2024, 'indeferido_sobre_montante'])}", T + "03f_captacao_anual_secult.csv"),
    ("N16", "39 municípios tiveram o primeiro projeto habilitado em 2022, 16 em 2023 e 3 por ciclo desde então",
     f"{int(coorte.loc['2022', 'municipios'])} municípios tiveram o primeiro projeto habilitado em 2022, {int(coorte.loc['2023', 'municipios'])} em 2023 e "
     + ("3 por ciclo" if {int(coorte.loc[c, 'municipios']) for c in ('2024', '2025', '2026')} == {3} else "?"), T + "03_coortes_primeira_presenca_canonico.csv"),
    ("N17", "Das 26 empresas que patrocinaram em 2025, 13 também aparecem como incentivadoras da Lei Rouanet, e elas responderam por 86% da renúncia",
     f"Das {ROU_T} empresas que patrocinaram em 2025, {ROU_N} também aparecem como incentivadoras da Lei Rouanet, e elas responderam por {pct(ROU_SH)}",
     T7 + "patrocinadores_na_rouanet.csv"),
    ("N18", "caiu de 74% (ciclo 2024) para 57% (2025)",
     f"{pct(comp07.loc[2024, 'pct_valor_rmgv_atribuivel'])} (ciclo 2024) para {pct(comp07.loc[2025, 'pct_valor_rmgv_atribuivel'])}", T7 + "composicao_por_ciclo.csv"),
    ("N19", "A RMGV tem 49% da população e fica com 67% do valor atribuível a um município",
     f"{pct(rmgv.loc['RMGV', 'share_pop_censo2022'])} da população e fica com {pct(rmgv.loc['RMGV', 'share_autorizado_atribuivel'])}",
     T + "03_territorio_rmgv_interior.csv"),
    ("N20", "O Gini do valor entre os 78 municípios é 0,88", num(float(terr["gini_valor_78"]), 2), T + "03_territorio_indicadores.csv"),
    ("N21", "explica só 7% da desigualdade", pct(float(terr["pct_theil_entre_grupos"])), T + "03_territorio_indicadores.csv"),
    ("N22", "São 293 projetos habilitados em 2022-2024 com situação resolvida, de 172 proponentes",
     f"{N1_07 + N0_07} projetos habilitados em 2022-2024 com situação resolvida, de {H1B_NOTA.split(' proponentes')[0].split('; ')[-1]}",
     T7 + "poder_hipoteses.csv (nota)"),
    ("N23", "| H1b: captou × expirou, 2022-2024 | 293 projetos (*T* = 0,68), 172 proponentes ($\\bar m$ = 1,70; *cv* = 0,75) | $p_0$ de 0,2 a 0,6; ρ = 0 ou 0,2 | 14 a 20 |",
     faixa_emd("captou × expirou, 2022-2024 (observacional)"), T7 + "poder_hipoteses.csv"),
    ("N24", "| H1b: margem do racionamento, 2023-2024 | 20 a 30 projetos por grupo | $p_0$ de 0,2 a 0,6 | 29 a 43 |",
     faixa_emd("racionamento pelo teto 2023-2024"), T7 + "poder_hipoteses.csv"),
    ("N25", "| H3: oferta sorteada por agente | 1.000 a 4.000 agentes | $p_0$ de 2% a 10% | 1,2 a 5,3 |",
     faixa_emd("encorajamento aleatório individual", 1), T7 + "poder_hipoteses.csv"),
    ("N26", "| H3: oferta sorteada por município | 71 municípios do interior, 20 a 50 agentes cada | $p_0$ de 5% a 10%; ρ de 0,02 a 0,05 | 2,9 a 6,3 |",
     faixa_emd("encorajamento aleatório por município (interior)", 1), T7 + "poder_hipoteses.csv"),
    ("N27", "(3 em 56 resolvidos no ciclo 2025)",
     f"({int(fun07.loc[2025, 'expirou'])} em {int(fun07.loc[2025, 'captou'] + fun07.loc[2025, 'expirou'])}", T7 + "funil_por_ciclo.csv"),
    ("N29", "172 proponentes ($\\bar m$ = 1,70; *cv* = 0,75)",
     f"$\\bar m$ = {num(float(poder07[poder07.desenho.str.startswith('captou')]['m'].iloc[0]), 2)}; *cv* = "
     f"{num(float(H1B_NOTA.split('cv = ')[1].split(';')[0]), 2)}", T7 + "poder_hipoteses.csv (m; nota)"),
    ("N28", "o retrato territorial cobre 74% do valor", pct(0.741), T + "03_territorio_indicadores.csv (cobertura_valor_atribuivel = 0.741)"),
]


def main() -> int:
    texto = ART.read_text(encoding="utf-8")
    linhas, falhas = [], 0
    for cid, trecho, recalc, fonte in CHECAGENS:
        if trecho not in texto:
            st = "TRECHO_AUSENTE"
        elif recalc in trecho:
            st = "CONFERE"
        else:
            st = "DIVERGE"
        falhas += st != "CONFERE"
        linhas.append({"id": cid, "status": st, "recalculado": recalc, "fonte": fonte, "trecho": trecho})
    with SAIDA.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["id", "status", "recalculado", "fonte", "trecho"])
        w.writeheader()
        w.writerows(linhas)
    for l in linhas:
        if l["status"] != "CONFERE":
            print(f"{l['id']} {l['status']}: recalculado «{l['recalculado']}» | texto «{l['trecho']}»")
    print(f"{len(linhas) - falhas}/{len(linhas)} checagens conferem → {SAIDA.relative_to(RAIZ)}")
    return 1 if falhas else 0


if __name__ == "__main__":
    sys.exit(main())
