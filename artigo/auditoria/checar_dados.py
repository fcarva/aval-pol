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
import re
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


def fx(ciclo: int, faixa_valor: str) -> float:
    r = faixa[(faixa.ciclo == ciclo) & (faixa.faixa_valor_ciclo == faixa_valor)]
    return float(r["taxa_execucao"].iloc[0])


# auditoria independente da captação (artigo/auditoria/auditar_captacao.py): somas termo a termo nos anexos oficiais
aud = pd.read_csv(Path(__file__).with_name("auditoria_captacao_anual.csv")).set_index("ano_captacao")
aud25 = aud.loc[2025]
_capt_anual = ler(RAIZ / "artigo" / "auditoria" / "auditoria_captacao_anual.csv")
cj = ler(TAB / "10_poder_conjoint.csv")
cj60 = cj[(cj.respondentes == 60) & (cj.tarefas == 12)]
cj30 = cj[(cj.respondentes == 30) & (cj.tarefas == 12)]
teto11 = ler(TAB / "11_teto_projeto_por_ano.csv").set_index("ano")
# Portal da Transparência (analise/16_transparencia_licc.py) e Mapa Cultural (analise/14_dados_publicos.py)
pares16 = ler(TAB / "16_pares_recorrentes.csv")
_termos16 = ler(RAIZ / "dados" / "processados" / "transparencia_licc_termos.csv")
conc16 = ler(TAB / "16_concentracao_proponentes.csv").set_index("ano")
cap_d = ler(TAB / "12_cap_deliberacoes.csv")
cap_r = ler(TAB / "12_cap_reunioes.csv")
_hab = set(cap_d.loc[cap_d.situacao == "habilitado", "processo"])
_inab = set(cap_d.loc[cap_d.situacao == "inabilitado", "processo"])
cap_reunioes_delib = int((cap_r.lido.astype(bool) & ~cap_r.sem_quorum.fillna(False).astype(bool)).sum())
cap_anos = (pd.to_datetime(cap_d["data"]).dt.year.min(), pd.to_datetime(cap_d["data"]).dt.year.max())
taxa25 = ler(TAB / "10_taxa_servico_permitida_2025.csv").iloc[0]
rub = ler(TAB / "10_rubricas_teto_in.csv")
par = pd.read_csv(TAB / "10_pareceristas_por_area.csv", dtype={"tabela_area": str}).set_index("tabela_area")


def rub25(chave: str) -> pd.Series:
    return rub[(rub.ano_in == 2025) & rub.rubrica.str.startswith(chave)].iloc[0]
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


# revisão da rodada 2 (Stage 4): racionamento 2023-2026, reentrada e cadastro do Mapa por município
reent = ler(TAB / "09_reentrada_resumo.csv").set_index("ano_recusa")
cotas09 = ler(TAB / "09_cotas_2025_2026.csv")
faixa_val = ler(TAB / "03_status_conversao_por_faixa_valor_2022_2024.csv").set_index("faixa_valor")
mapacob = ler(TAB / "07_mapa_agentes_cobertura.csv").set_index("tipo")
quadro_h3 = ler(TAB / "07_mapa_quadro_h3.csv").set_index("quadro")
indef = pd.read_csv(RAIZ / "dados" / "processados" / "indeferidos_2023_2024.csv")  # sem comment="#": há título "#EP10"
MESES = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro",
         "novembro", "dezembro"]


def cota_completa(ano: int, cota: int, curto: bool = False) -> str:
    d = pd.Timestamp(cotas09[(cotas09.ano_captacao == ano) & (cotas09.cota == cota)]["recebimento_que_completa_a_cota"].iloc[0])
    return f"{d.day:02d}/{d.month:02d}" if curto else f"{d.day} de {MESES[d.month - 1]}"


def faixa_h3(quadro: str) -> str:
    v = poder07[(poder07.desenho == "encorajamento aleatório por município (interior)")
                & (poder07.unidade == f"município ({quadro})")]["emd_pontos"] * 100
    return f"{num(v.min(), 1)} a {num(v.max(), 1)}"


def linha_h3(quadro: str) -> str:
    q = quadro_h3.loc[quadro]
    return f"{int(q.J)} municípios, {milhar(q.N)} {'coletivos' if quadro == 'coletivos' else 'agentes'} ($\\bar m$ = {num(q.m, 1)}; *cv* = {num(q.cv, 2)})"


PROJ_REC = indef.groupby("ano_captacao")["projeto"].nunique()
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
    ("D06", "463 projetos foram autorizados a captar, somados, R\\$ 184 milhões (459 com valor válido)",
     f"{int(anual.loc[TOTAL, 'processos'])} projetos foram autorizados a captar, somados, R\\$ {num(anual.loc[TOTAL, 'autorizado_total'] / 1e6)} milhões "
     f"({int(anual.loc[TOTAL, 'autorizado_n'])} com valor válido)", T + "03_anual.csv (valor autorizado; R$ 500,00 impresso é tratado como ausente)"),
    ("D65b", "valor que o anexo de captação da SECULT e a lista do Portal da Transparência informam",
     (lambda r, a: "informam" if ("09-R/2022" in str(r["limite_rotulo"]) and float(r["limite_impresso"]) == 15e6
                                  and float(a) == 15e6) else "?")(
         ler(TAB / "16_transparencia_resumo.csv").set_index("ano_captacao").loc[2022],
         anu.loc[2022, "montante_declarado"]),
     T + "16_transparencia_resumo.csv (LIMITE PORTARIA SEFAZ Nº 09-R/2022 = 15.000.000, Download/378); 03f_captacao_anual_secult.csv"),
    ("D06b", "acima da soma dos tetos do período, de R\\$ 111 milhões",
     f"de R\\$ {num(sum(max(float(a), float(b)) for a, b in zip(_capt_anual['teto_portarias_sefaz'], _capt_anual['montante_impresso'])) / 1e6)} milhões"
     if sum(max(float(a), float(b)) for a, b in zip(_capt_anual['teto_portarias_sefaz'], _capt_anual['montante_impresso'])) < anual.loc[TOTAL, 'autorizado_total'] else "?",
     "artigo/auditoria/auditoria_captacao_anual.csv (maior entre portaria e montante impresso, 2022-2026) < 03_anual.csv"),
    ("D07", "em 2025, 62 projetos validados somam R\\$ 24,64 milhões, e um ainda",
     f"{int(aud25['projetos_validados'])} projetos validados somam R\\$ {num(float(aud25['soma_validados']) / 1e6, 2)} milhões, e "
     f"{ {1: 'um'}.get(int(aud25['projetos_em_analise']), '?')} ainda",
     "artigo/auditoria/auditoria_captacao_anual.csv (auditar_captacao.py, sobre o anexo oficial de 2025)"),
    ("D08", "ocupava 4,2% dos trabalhadores do ES, contra 5,8% no país, a 18ª participação",
     f"{pct(ES_SH, 1)} dos trabalhadores do ES, contra {pct(BR_SH, 1)} no país, a {ES_RANK}ª", "dados/externos/siic_uf.csv"),
    ("D09", "95% da população da Região Metropolitana da Grande Vitória (RMGV) vivia em município com cinema, contra 34%",
     f"{pct(munic.loc[('cinema', 'RMGV'), 'pct_pop_em_mun_com_sim'])} da população da Região Metropolitana da Grande Vitória (RMGV) "
     f"vivia em município com cinema, contra {pct(munic.loc[('cinema', 'Interior'), 'pct_pop_em_mun_com_sim'])}",
     "dados/externos/munic2021_cultura_es_resumo.csv"),
    ("D10", "metade dos municípios do interior não tinha fundo municipal de cultura",
     ("metade" if abs(munic.loc[("fundo_municipal_cultura", "Interior"), "pct_mun_sim_sobre_validos"] - 0.5) < 0.01 else "?")
     + " dos municípios do interior não tinha fundo municipal de cultura",
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
    ("D65", "a Portaria SEFAZ nº 09-R fixou R\\$ 10 milhões, e a Portaria SEFAZ nº 83-R, de 26 de setembro, ampliou o montante em R\\$ 5 milhões (DIO-ES, 2026): o teto de 2022 foi de R\\$ 15 milhões",
     (lambda amp: f"fixou R\\$ {num(teto.loc[2022, 'teto_renuncia'] / 1e6)} milhões, e a Portaria SEFAZ nº 83-R, de 26 de setembro, "
                  f"ampliou o montante em R\\$ {num(amp / 1e6)} milhões (DIO-ES, 2026): o teto de 2022 foi de R\\$ "
                  f"{num((teto.loc[2022, 'teto_renuncia'] + amp) / 1e6)} milhões")(
         float(re.search(r"Ampliar em R\$ ([\d.]+),00 \([^)]*\) o montante de recursos disponíveis no ano de 2022 para o "
                         r"financiamento dos projetos culturais, fixado pela Portaria nº 09-R",
                         " ".join(" ".join(pd.read_csv(EXT / "dio_teto_trechos.csv")["trecho"].astype(str)).split()))
               .group(1).replace(".", ""))),
     "dados/externos/dio_teto_trechos.csv (DIO-ES, 27/09/2022, p. 18-19: Portaria SEFAZ nº 83-R); dados/externos/licc_teto_vs_icms.csv"),
    ("D65c", "dos quais R\\$ 11,5 milhões foram validados",
     f"R\\$ {num(anu.loc[2022, 'total_validado'] / 1e6, 1)} milhões foram validados", T + "03f_captacao_anual_secult.csv"),
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
CHECAGENS = [c for c in CHECAGENS if c[0] in {"D03", "D05", "D06", "D06b", "D07", "D65b", "D65c", "D08", "D09", "D10", "D11", "D22", "D33", "D65"}]
CHECAGENS += [
    ("N02", "entre os 25.441 agentes cadastrados no Mapa Cultural", milhar(mapa07.loc["todos", "agentes"]), T7 + "mapa_cultural_universo.csv"),
    ("N03", "| Agentes culturais cadastrados no Mapa Cultural (coletivos) | 25.441 (2.592) |",
     f"{milhar(mapa07.loc['todos', 'agentes'])} ({milhar(mapa07.loc['coletivo (type=2)', 'agentes'])})", T7 + "mapa_cultural_universo.csv"),
    ("N04", "68% dos habilitados de 2022-2024 com situação resolvida captaram", pct(N1_07 / (N1_07 + N0_07)), T7 + "funil_por_ciclo.csv"),
    ("N05", "| Projetos habilitados; proponentes por ciclo | 305; 53, 92 e 95 |",
     f"{int(RES07['habilitados'].sum())}; {int(comp07.loc[2022, 'proponentes'])}, {int(comp07.loc[2023, 'proponentes'])} e {int(comp07.loc[2024, 'proponentes'])}",
     T7 + "funil_por_ciclo.csv; 07_composicao_por_ciclo.csv"),
    ("N06", "| Habilitados com situação resolvida; captaram | 293; 198 |", f"{N1_07 + N0_07}; {N1_07}", T7 + "funil_por_ciclo.csv"),
    ("N08", "| Valor com patrocinador que coube no teto | 78%; 74% |",
     f"{pct(1 / cap07.loc[2023, 'demanda_com_patrocinador_sobre_montante'])}; {pct(1 / cap07.loc[2024, 'demanda_com_patrocinador_sobre_montante'])}",
     T7 + "funil_captacao_anual.csv"),
    ("N10", "14 municípios do interior nunca tiveram projeto habilitado", str(int(coorte.loc["nunca (2022-2026)", "municipios"])),
     T + "03_coortes_primeira_presenca_canonico.csv"),
    ("N12", "Duas empresas somam metade da renúncia de 2025; energia e gás, 52%",
     f"{ {2: 'Duas'}.get(int(float(patr['empresas_para_metade'])), '?')} empresas somam metade da renúncia de 2025; energia e gás, "
     f"{pct(macro.loc['Energia e gás (serviço regulado)', 'share'])}", T + "03_patrocinadores_concentracao.csv; 03_patrocinadores_macrossetor.csv"),
    ("N14", "Recorrentes captam mais (71% contra 57%)",
     f"{pct(float(rec[(rec.ciclo == '2023-2024') & (rec.proponente == 'recorrente')].taxa_execucao.iloc[0]))} contra "
     f"{pct(float(rec[(rec.ciclo == '2023-2024') & (rec.proponente == 'estreante')].taxa_execucao.iloc[0]))}", T + "03_status_conversao_recorrencia_2023_2024.csv"),
    ("N15", "Termos com patrocinador de 28% e 35% do montante recusados em 2023 e 2024",
     f"{pct(anu.loc[2023, 'indeferido_sobre_montante'])} e {pct(anu.loc[2024, 'indeferido_sobre_montante'])}", T + "03f_captacao_anual_secult.csv"),
    ("N16", "39 municípios tiveram o primeiro projeto habilitado em 2022, 16 em 2023 e 3 por ciclo desde então",
     f"{int(coorte.loc['2022', 'municipios'])} municípios tiveram o primeiro projeto habilitado em 2022, {int(coorte.loc['2023', 'municipios'])} em 2023 e "
     + ("3 por ciclo" if {int(coorte.loc[c, 'municipios']) for c in ('2024', '2025', '2026')} == {3} else "?"), T + "03_coortes_primeira_presenca_canonico.csv"),
    ("N19", "A RMGV tem 49% da população e fica com 67% do valor atribuível a um município em 2022-2026",
     f"{pct(rmgv.loc['RMGV', 'share_pop_censo2022'])} da população e fica com {pct(rmgv.loc['RMGV', 'share_autorizado_atribuivel'])}",
     T + "03_territorio_rmgv_interior.csv"),
    ("N20", "O Gini do valor entre os 78 municípios é 0,88", num(float(terr["gini_valor_78"]), 2), T + "03_territorio_indicadores.csv"),
    ("N21", "explica só 7% do índice de Theil", pct(float(terr["pct_theil_entre_grupos"])), T + "03_territorio_indicadores.csv"),
    ("N22", "293 projetos habilitados em 2022-2024 com situação resolvida, de 172 proponentes",
     f"{N1_07 + N0_07} projetos habilitados em 2022-2024 com situação resolvida, de {H1B_NOTA.split(' proponentes')[0].split('; ')[-1]}",
     T7 + "poder_hipoteses.csv (nota)"),
    ("N24", "| H5: margem do racionamento, 2023-2024 | 32 recusados × 32 validados | $p_0$ de 0,2 a 0,6 | 28 a 34 |",
     f"{int(PROJ_REC.sum())} recusados × {int(PROJ_REC.sum())} validados | $p_0$ de 0,2 a 0,6 | "
     + faixa_emd("racionamento pelo teto 2023-2024"), T7 + "poder_hipoteses.csv; dados/processados/indeferidos_2023_2024.csv"),
    ("N25", "| H4: oferta por município, só coletivos | 52 municípios, 257 coletivos ($\\bar m$ = 4,9; *cv* = 1,32) | $p_0$ de 2% a 10%; ρ de 0,02 a 0,05 | 5,5 a 13,4 |",
     linha_h3("coletivos") + " | $p_0$ de 2% a 10%; ρ de 0,02 a 0,05 | " + faixa_h3("coletivos"), T7 + "poder_hipoteses.csv; 07_mapa_quadro_h3.csv"),
    ("N26", "| H4: oferta por município, todos os agentes | 71 municípios, 2.389 agentes ($\\bar m$ = 33,6; *cv* = 1,43) | $p_0$ de 2% a 10%; ρ de 0,02 a 0,05 | 2,8 a 8,5 |",
     linha_h3("coletivos e individuais") + " | $p_0$ de 2% a 10%; ρ de 0,02 a 0,05 | " + faixa_h3("coletivos e individuais"),
     T7 + "poder_hipoteses.csv; 07_mapa_quadro_h3.csv"),
    ("N27", "(3 em 56 resolvidos no ciclo 2025)",
     f"({int(fun07.loc[2025, 'expirou'])} em {int(fun07.loc[2025, 'captou'] + fun07.loc[2025, 'expirou'])}", T7 + "funil_por_ciclo.csv"),
    ("N30", "Mas 6 dos 11 recusados em 2023 e 12 dos 21 recusados em 2024 captaram no ano seguinte",
     f"{int(reent.loc[2023, 'captaram_no_ano_seguinte'])} dos {int(reent.loc[2023, 'projetos_recusados'])} recusados em 2023 e "
     f"{int(reent.loc[2024, 'captaram_no_ano_seguinte'])} dos {int(reent.loc[2024, 'projetos_recusados'])} recusados em 2024",
     T + "09_reentrada_resumo.csv"),
    ("N31", "os de 32 projetos recusados em 2023 e 2024", f"os de {int(PROJ_REC.sum())} projetos", "dados/processados/indeferidos_2023_2024.csv"),
    ("N34", "em 2025, a cota de 50% se completou com termos recebidos até 28/01",
     f"até {cota_completa(2025, 4, curto=True)}", T + "09_cotas_2025_2026.csv"),
    ("N36", "e restam 14 municípios do interior sem projeto", f"restam {int(coorte.loc['nunca (2022-2026)', 'municipios'])} municípios",
     T + "03_coortes_primeira_presenca_canonico.csv"),
    ("N38", "79% dos coletivos e 78% dos individuais não informam município",
     f"{pct(mapacob.loc['coletivos', 'sem_municipio'] / mapacob.loc['coletivos', 'cadastrados'])} dos coletivos e "
     f"{pct(mapacob.loc['individuais', 'sem_municipio'] / mapacob.loc['individuais', 'cadastrados'])} dos individuais",
     T7 + "mapa_agentes_cobertura.csv"),
    ("N39", "há 257 coletivos em 52 municípios e 2.389 agentes, somados os individuais, nos 71",
     f"há {int(quadro_h3.loc['coletivos', 'N'])} coletivos em {int(quadro_h3.loc['coletivos', 'J'])} municípios e "
     f"{milhar(quadro_h3.loc['coletivos e individuais', 'N'])} agentes, somados os individuais, nos {int(quadro_h3.loc['coletivos e individuais', 'J'])}",
     T7 + "mapa_quadro_h3.csv"),
    ("N40", "são 26 por grupo, e o efeito mínimo passa de 5 pontos",
     f"passa de {int(poder07[poder07.unidade == 'município (coletivos)']['emd_pontos'].min() * 100)} pontos", T7 + "poder_hipoteses.csv"),
    ("N42", "com primeiro estágio de 41% (13 dos 32 recusados não captaram depois)",
     f"de {pct(1 - reent['captaram_ate_2026'].sum() / reent['projetos_recusados'].sum())} "
     f"({int(reent['projetos_recusados'].sum() - reent['captaram_ate_2026'].sum())} dos {int(reent['projetos_recusados'].sum())} recusados",
     T + "09_reentrada_resumo.csv"),
    ("N44", "e os 53 a 95 proponentes habilitados por ciclo",
     f"os {int(comp07['proponentes'].min())} a {int(comp07['proponentes'].max())} proponentes", T7 + "composicao_por_ciclo.csv (2022-2026)"),
    ("N28", "o retrato territorial cobre 74% do valor", pct(0.741), T + "03_territorio_indicadores.csv (cobertura_valor_atribuivel = 0.741)"),
    # revisão de 27/09/2026: captação auditada termo a termo e captação por porte do pedido
    ("N45", "os termos de patrocínio listados pela SECULT somam exatamente o montante de cada ano",
     "somam exatamente" if all(bool(aud.loc[a, "esgotou_montante"]) for a in (2023, 2024, 2025)) else "?",
     "artigo/auditoria/auditoria_captacao_anual.csv (2023-2025)"),
    ("N46", "a captação caiu de 79% no ciclo 2022 para 27% em 2024, enquanto no teto ficou entre 78% e 89%",
     f"caiu de {pct(fx(2022, 'até 400 mil'))} no ciclo 2022 para {pct(fx(2024, 'até 400 mil'))} em 2024, enquanto no teto ficou entre "
     f"{pct(min(fx(c, 'exatamente 500 mil') for c in (2022, 2023, 2024)))} e {pct(max(fx(c, 'exatamente 500 mil') for c in (2022, 2023, 2024)))}",
     T + "03_status_conversao_por_faixa_valor_e_ciclo.csv (taxa_execucao)"),
    # revisão de 27/09/2026 (nova moldura): taxa de serviço, tetos das rubricas e poder do experimento conjunto
    ("N48", "| H1: experimento conjunto | 30 a 60 decisores × 12 tarefas | $p_0$ = 0,5; ρ = 0 ou 0,1 no decisor | 7,4 a 19,0 |",
     f"{int(cj30.respondentes.iloc[0])} a {int(cj60.respondentes.iloc[0])} decisores × {int(cj60.tarefas.iloc[0])} tarefas "
     f"| $p_0$ = 0,5; "
     f"ρ = 0 ou 0,1 no decisor | {num(cj60.emd_pontos.min(), 1)} a {num(cj30.emd_pontos.max(), 1)}", T + "10_poder_conjoint.csv (30 e 60 × 12)"),
    ("N49", "O experimento conjunto detecta diferenças de 7 a 13 pontos na probabilidade de escolha com 60 decisores, e de 10 a 19 com 30",
     f"diferenças de {num(cj60.emd_pontos.min())} a {num(cj60.emd_pontos.max())} pontos na probabilidade de escolha com 60 decisores, "
     f"e de {num(cj30.emd_pontos.min())} a {num(cj30.emd_pontos.max())} com 30", T + "10_poder_conjoint.csv (30 e 60 × 12)"),
    ("N50", "os dois primeiros limites somam R\\$ 3,36 milhões, 13% dos R\\$ 25 milhões",
     f"somam R\\$ {num(float(taxa25.max_taxa_servico) / 1e6, 2)} milhões, {pct(float(taxa25.max_taxa_servico_sobre_captado))} dos R\\$ "
     f"{num(float(taxa25.valor_captado) / 1e6)} milhões", T + "10_taxa_servico_permitida_2025.csv"),
    ("N51", "Até 13% do valor captado em 2025 poderia remunerar captação e elaboração",
     f"Até {pct(float(taxa25.max_taxa_servico_sobre_captado))}", T + "10_taxa_servico_permitida_2025.csv"),
    ("N52", "Captação e elaboração poderiam levar até 13% do valor captado em 2025",
     f"até {pct(float(taxa25.max_taxa_servico_sobre_captado))}", T + "10_taxa_servico_permitida_2025.csv"),
    ("N53", "A captação pode custar até 10% (R\\$ 50 mil) e a elaboração do projeto até 5% (R\\$ 15 mil)",
     f"até {num(rub25('captação').limite_pct)}% (R\\$ {num(rub25('captação').teto_reais / 1e3)} mil) e a elaboração do projeto até "
     f"{num(rub25('elaboração').limite_pct)}% (R\\$ {num(rub25('elaboração').teto_reais / 1e3)} mil)", T + "10_rubricas_teto_in.csv (2025)"),
    ("N54", "a divulgação pode consumir até 25% dos recursos",
     f"até {num(rub25('divulgação').limite_pct)}%", T + "10_rubricas_teto_in.csv (2025)"),
    ("N56", "mas é fraca com 41 pareceristas",
     f"fraca com {int(par.loc['distintos (todas as áreas)', 'pareceristas'])} pareceristas",
     T + "10_pareceristas_por_area.csv (lista da SECULT de 18/09/2026)"),
    ("N55", "a listagem parte das 26 patrocinadoras de 2025", f"das {int(float(patr['empresas']))} patrocinadoras",
     T + "03_patrocinadores_concentracao.csv"),
    # revisão de 27/09/2026 (atas e teto por projeto)
    ("N57", "O teto por projeto fixa um piso de projetos, ao menos 50 com os R\\$ 25 milhões de 2025 (captaram 63)",
     f"ao menos {int(teto11.loc[2025, 'minimo_projetos_todos_no_teto'])} com os R\\$ {num(teto11.loc[2025, 'montante'] / 1e6)} milhões de 2025 "
     f"(captaram {int(teto11.loc[2025, 'projetos_que_captaram'])})", T + "11_teto_projeto_por_ano.csv"),
    ("N58", "36% dos habilitados do ciclo 2025 pediram exatamente R\\$ 500 mil",
     f"{pct(bunch.loc['2025', 'pct_exatamente_500mil'])} dos habilitados do ciclo 2025", T + "03_bunching_teto.csv"),
    ("N60", "Os extratos das atas de 158 reuniões com deliberação, de 2022 a 2026, listam 86 projetos inabilitados, 15% dos deliberados",
     f"de {cap_reunioes_delib} reuniões com deliberação, de {cap_anos[0]} a {cap_anos[1]}, listam {len(_inab)} projetos inabilitados, "
     f"{pct(len(_inab - _hab) / len(_hab | _inab))} dos deliberados", T + "12_cap_deliberacoes.csv; 12_cap_reunioes.csv"),
    ("N59", "até 2023, 5% do montante anual; desde 2024, R\\$ 500 mil",
     f"até 2023, {num(teto11.loc[2023, 'pct_montante'])}% do montante anual; desde 2024, R\\$ {num(teto11.loc[2024, 'teto_geral_montante_final'] / 1e3)} mil"
     if bool(teto11.loc[2023, "trechos_conferidos_no_texto"]) and bool(teto11.loc[2024, "trechos_conferidos_no_texto"]) else "?",
     T + "11_teto_projeto_por_ano.csv (trechos das INs 2023 e 2024 conferidos)"),
    # revisão de 27/09/2026, tarde (grifos do autor): economia criativa no boletim da SECULT (PNAD Contínua, 2º tri 2020)
    ("N64", "8,2% dos ocupados no 2º trimestre de 2020, contra 8,5% no país, a 8ª posição",
     (lambda b: f"{b[0]} dos ocupados no 2º trimestre de 2020, contra {b[1]} no país, a {b[2]} posição")(
         (lambda x: (re.search(r"equivale a ([\d,]+%) do total de pessoas", x).group(1),
                     re.search(r"média brasileira \(([\d,]+%)\)", x).group(1),
                     re.search(r"na (\d+ª)\s+posição", x).group(1)))(
             (RAIZ / "dados/fontes_web/paginas/boletim_ec_boletim_economia_criativa_02t_2020.txt").read_text(encoding="utf-8"))),
     "dados/fontes_web/paginas/boletim_ec_boletim_economia_criativa_02t_2020.txt (SECULT, Boletim 2T2020)"),
    # revisão de 27/09/2026 (dados públicos sem LAI: Portal da Transparência e Mapa Cultural)
    ("N61", "48 pares patrocinador–proponente se repetem (44% do valor)",
     f"{len(pares16)} pares patrocinador–proponente se repetem ("
     f"{pct(pares16['valor'].sum() / _termos16.loc[~_termos16['valor_zero'].astype(bool) & _termos16['cnpj_proponente_dv_ok'].astype(bool), 'valor'].sum())} do valor)",
     T + "16_pares_recorrentes.csv; dados/processados/transparencia_licc_termos.csv"),
    ("N62", "44 de 107 proponentes voltaram a captar (68% do valor)",
     f"{int(conc16.loc['2022-2025', 'proponentes_em_mais_de_um_ano'])} de {int(conc16.loc['2022-2025', 'proponentes_cnpj'])} "
     f"proponentes voltaram a captar ("
     f"{pct(conc16.loc['2022-2025', 'valor_de_quem_captou_em_mais_de_um_ano'])} do valor)", T + "16_concentracao_proponentes.csv"),
]

# revisão r4 (27/09/2026): avisos do Diário Oficial (analise/18) e poder refeito (analise/19)
_cob18 = ler(TAB / "18_cobertura_cnpj.csv").set_index("ciclo")
_dep18 = ler(TAB / "18_deposito_x_portal.csv")
_dep18 = _dep18[_dep18["ano"].astype(str).str.fullmatch(r"\d{4}")]
_p19 = ler(TAB / "19_poder_revisao.csv")
_q3 = ler(TAB / "07_mapa_quadro_h3.csv").set_index("quadro")
_ev = pd.read_csv(EXT / "mapa_eventos_licc.csv")
_rec16 = ler(TAB / "16_data_processo_x_recebimento_2025.csv").dropna(subset=["dias_depois_do_recebimento"])


def _faixa(mask, casas: int = 0) -> str:
    v = _p19.loc[mask, "emd_pontos"]
    return f"{num(v.min(), casas)} a {num(v.max(), casas)}"


_h5 = _p19["hipotese"].eq("H5")
_todos = _p19["quadro"].eq("coletivos e individuais")
_primeiro = float(_p19.loc[_h5 & _p19["desenho"].str.contains("algum momento"), "desenho"].iloc[0]
                  .split("estágio ")[1].rstrip(")"))
_J = int(_q3.loc["coletivos e individuais", "J"])
CHECAGENS += [
    ("N65", "juntas, cobrem 385 dos 463 habilitados (83%)",
     f"cobrem {int(_cob18.loc['todos', 'cnpj_em_alguma_fonte'])} dos {int(_cob18.loc['todos', 'habilitados'])} habilitados "
     f"({pct(_cob18.loc['todos', 'pct_em_alguma_fonte'])})", T + "18_cobertura_cnpj.csv"),
    ("N66", "data de cada depósito (82% dos termos de 2022-2025)",
     f"({pct(_dep18['termos_com_deposito'].sum() / _dep18['termos'].sum())} dos termos de "
     f"{_dep18['ano'].astype(int).min()}-{_dep18['ano'].astype(int).max()})", T + "18_deposito_x_portal.csv"),
    ("N67", "eventos datados de 18 projetos",
     f"eventos datados de {_ev.loc[_ev['ocorrencias'] > 0, 'numero_processo'].nunique()} projetos",
     "dados/externos/mapa_eventos_licc.csv"),
    ("N68", "o EMD divide-se pelo primeiro estágio (0,41) e vai a 69 a 84 pontos",
     f"primeiro estágio ({num(_primeiro, 2)}) e vai a {_faixa(_h5 & _p19['desenho'].str.contains('algum momento'))} pontos",
     T + "19_poder_revisao.csv"),
    ("N69", "o desenho prospectivo precisa de 112 a 168 recusados por braço",
     (lambda r: f"precisa de {int(-(-r.min() // 1))} a {int(-(-r.max() // 1))} recusados por braço")(
         _p19.loc[_p19["desenho"].str.contains("recusados necessários"), "recusados_por_braco"]), T + "19_poder_revisao.csv"),
    ("N75", "a diferença entre empresas e população fica entre 8 e 20 pontos",
     f"fica entre {_faixa(_p19['desenho'].str.contains('empresas − população')).replace(' a ', ' e ')} pontos", T + "19_poder_revisao.csv"),
    ("N76", "| H1: diferença empresas − população | e 500 residentes × 6 tarefas | idem | 8,2 a 19,7 |",
     f"| {_faixa(_p19['desenho'].str.contains('empresas − população') & _p19['quadro'].str.contains('500 residentes'), 1)} |",
     T + "19_poder_revisao.csv"),
    ("N77", "| H2: nota cega, habilitados × inabilitados | 86 × 86 projetos | nota padronizada | 0,43 DP |",
     (lambda r: f"| {r['quadro'].split(' ')[0]} × {r['quadro'].split(' ')[0]} projetos | nota padronizada | {num(r['emd_pontos'], 2)} DP |")(
         _p19[_p19["desenho"].str.contains("habilitados × inabilitados")].iloc[0]), T + "19_poder_revisao.csv"),
    ("N78", "| H2: nota cega, captou × não captou | 198 × 95 habilitados | nota padronizada | 0,35 DP |",
     (lambda r: f"| {r['quadro'].split(' ')[0]} × {r['quadro'].split(' × ')[1].split(' ')[0]} habilitados | nota padronizada | {num(r['emd_pontos'], 2)} DP |")(
         _p19[_p19["desenho"].str.contains("captou × não captou")].iloc[0]), T + "19_poder_revisao.csv"),
    ("N79", "A avaliação cega detecta diferença de nota de 0,43 desvio-padrão",
     f"diferença de nota de {num(_p19.loc[_p19['desenho'].str.contains('habilitados × inabilitados'), 'emd_pontos'].iloc[0], 2)} desvio-padrão",
     T + "19_poder_revisao.csv"),
    ("N81", "das 47 recusas registradas nas versões sucessivas do anexo, 27 viraram validação em versão posterior",
     (lambda f: f"das {int((f['versoes_indeferido'] > 0).sum())} recusas registradas nas versões sucessivas do anexo, "
                f"{int(f['indeferido_depois_validado'].sum())} viraram validação em versão posterior")(
         ler(TAB / "13_versoes_captados_fila.csv").query("ano == 2024")), T + "13_versoes_captados_fila.csv (2024)"),
    ("N82", "a comparação com as 20 que não viraram",
     (lambda f: f"com as {int((f['versoes_indeferido'] > 0).sum() - f['indeferido_depois_validado'].sum())} que não viraram")(
         ler(TAB / "13_versoes_captados_fila.csv").query("ano == 2024")), T + "13_versoes_captados_fila.csv (2024)"),
    ("N83", "de 11 a 21 projetos recusados por ano, são de 6 a 16 ciclos",
     (lambda r, n: f"de {int(r.min())} a {int(r.max())} projetos recusados por ano, são de "
                   f"{int(-(-n.min() // r.max()))} a {int(-(-n.max() // r.min()))} ciclos")(
         ler(TAB / "09_reentrada_resumo.csv")["projetos_recusados"],
         _p19.loc[_p19["desenho"].str.contains("recusados necessários"), "recusados_por_braco"]),
     T + "09_reentrada_resumo.csv; 19_poder_revisao.csv"),
    ("N80", "os 86 inabilitados das atas da CAP",
     (lambda c: f"os {c.loc[c['situacao'] == 'inabilitado', 'processo'].nunique()} inabilitados")(ler(TAB / "12_cap_deliberacoes.csv")),
     T + "12_cap_deliberacoes.csv"),
    ("N70", "são 35 ou 36 municípios em cada, e a diferença entre os braços tem EMD de 2,3 a 4,9 pontos",
     f"são {_J // 2} ou {-(-_J // 2)} municípios em cada, e a diferença entre os braços tem EMD de "
     f"{_faixa(_todos & _p19['desenho'].str.startswith('c)'), 1)} pontos", T + "19_poder_revisao.csv; 07_mapa_quadro_h3.csv"),
    ("N71", "Só com os coletivos, são 26 por grupo",
     f"são {int(_q3.loc['coletivos', 'J']) // 2} por grupo", T + "07_mapa_quadro_h3.csv"),
    ("N72", "sorteada entre os 71 municípios do interior", f"entre os {_J} municípios", T + "07_mapa_quadro_h3.csv"),
    ("N74", "pedidos até R\\$ 400 mil captaram 79% em 2022 e 27% em 2024",
     f"captaram {pct(fx(2022, 'até 400 mil'))} em 2022 e {pct(fx(2024, 'até 400 mil'))} em 2024",
     T + "03_status_conversao_por_faixa_valor_e_ciclo.csv"),
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
