"""03_descritivas.py — estatísticas descritivas da LICC (habilitados 2022-2026, captados 2025).

Lê dados/processados/* (01_carregar.py) e dados/externos/municipios_es.csv (02_externos.py).
Escreve analise/tabelas/03_*.csv. Toda tabela traz a cobertura (n com dado / n total).
Nenhuma ausência vira zero; zeros territoriais só existem onde o dado é "nenhum projeto".
"""
from __future__ import annotations

import numpy as np
import pandas as pd
from scipy import stats

from _comum import (
    EXTERNOS,
    PROCESSADOS,
    TABELAS,
    TETO_ESPECIAL,
    TETO_GERAL,
    TETO_1A_EDICAO,
    cr,
    gini,
    hhi,
    igual_centavo,
    theil_t,
)

STATUS_ROTULO = {  # rótulo na lista da SECULT (versão 10/09/2026) ↔ código do CSV
    "captando": "Em captação",
    "em_execucao": "Em execução",
    "concluido": "Execução finalizada",
    "captacao_expirada": "Prazo de captação expirado",
}
COTA_ROTULO = {  # IN SECULT 001/2025, art. 18
    "cota-pautados": "I - eventos calendarizados >10 anos (30%)",
    "cota-continuados": "II - planos plurianuais (10%)",
    "cota-fora-rmgv": "III - fora da região metropolitana (10%)",
    "cota-demais": "IV - demais projetos (50%)",
}
COTA_PCT = {"cota-pautados": 0.30, "cota-continuados": 0.10, "cota-fora-rmgv": 0.10, "cota-demais": 0.50}

# Setor dos patrocinadores INFERIDO DO NOME (não consultado no cadastro CNPJ/CNAE).
# confiança: alta = o nome declara a atividade; média = declara o ramo genérico;
# baixa = o nome não permite inferir o ramo [VERIFICAR no CNAE da Receita Federal].
SETOR = {
    "28152650": ("Distribuição de energia elétrica", "Energia e gás (serviço regulado)", "alta"),
    "34307295": ("Distribuição de gás canalizado", "Energia e gás (serviço regulado)", "alta"),
    "06248349": ("Transporte de gás natural (gasodutos)", "Energia e gás (serviço regulado)", "alta"),
    "00827783": ("Comércio de veículos", "Comércio de veículos e autopeças", "alta"),
    "39786983": ("Comércio de veículos", "Comércio de veículos e autopeças", "alta"),
    "11277336": ("Comércio de veículos", "Comércio de veículos e autopeças", "alta"),
    "71189278": ("Comércio de veículos e peças", "Comércio de veículos e autopeças", "alta"),
    "45901867": ("Comércio de veículos", "Comércio de veículos e autopeças", "alta"),
    "27340074": ("Comércio de autopeças", "Comércio de veículos e autopeças", "alta"),
    "06955576": ("Supermercado", "Varejo supermercadista", "alta"),
    "27555390": ("Supermercado", "Varejo supermercadista", "alta"),
    "07526557": ("Bebidas (centro de distribuição)", "Indústria", "alta"),
    "05069718": ("Perfis de alumínio", "Indústria", "média"),
    "31790710": ("Metalmecânica", "Indústria", "alta"),
    "04023387": ("Mármores e granitos (rochas ornamentais)", "Indústria", "alta"),
    "03845717": ("Distribuidora (ramo não declarado no nome)", "Comércio atacadista/distribuição", "baixa"),
    "03380787": ("Distribuição de alimentos e embalagens", "Comércio atacadista/distribuição", "alta"),
    "07548056": ("Distribuidora (ramo não declarado no nome)", "Comércio atacadista/distribuição", "baixa"),
    "02689900": ("Distribuidora (ramo não declarado no nome)", "Comércio atacadista/distribuição", "baixa"),
    "09492311": ("Distribuição de cosméticos", "Comércio atacadista/distribuição", "alta"),
    "22280114": ("Distribuição de tintas e revestimentos", "Comércio atacadista/distribuição", "alta"),
    "31819139": ("Comércio de materiais de construção", "Comércio atacadista/distribuição", "média"),
    "04330073": ("Trading (comércio exterior)", "Comércio atacadista/distribuição", "média"),
    "08625038": ("Exportação e importação de café", "Comércio atacadista/distribuição", "alta"),
    "31731169": ("Comercial (ramo não declarado no nome)", "Comércio atacadista/distribuição", "baixa"),
    "31759699": ("Comercial (ramo não declarado no nome)", "Comércio atacadista/distribuição", "baixa"),
}


def salvar(df: pd.DataFrame, nome: str) -> pd.DataFrame:
    df.to_csv(TABELAS / f"03_{nome}.csv", index=False, encoding="utf-8")
    return df


def carregar():
    h = pd.read_csv(PROCESSADOS / "habilitados.csv")
    pm = pd.read_csv(PROCESSADOS / "habilitados_municipios.csv")
    c = pd.read_csv(PROCESSADOS / "captados_2025.csv")
    ap = pd.read_csv(PROCESSADOS / "aportes_2025.csv", dtype={"cnpj_raiz": str})
    prop = pd.read_csv(PROCESSADOS / "proponentes.csv")
    mun = pd.read_csv(EXTERNOS / "municipios_es.csv")
    h = h.merge(prop[["chave_proponente", "natureza", "natureza_rotulo"]], on="chave_proponente", how="left")
    # processo distinto: registro da seção mais recente (ciclo maior)
    hd = h.sort_values("ciclo").drop_duplicates("numero_processo", keep="last").copy()
    return h, hd, pm, c, ap, prop, mun


# --------------------------------------------------------------------------------------


def anual(h: pd.DataFrame, hd: pd.DataFrame) -> pd.DataFrame:
    salvar(pd.crosstab(h["ciclo"], h["ano_protocolo"]).reset_index(), "ciclo_x_ano_protocolo")
    linhas = []
    grupos = [(str(c), g) for c, g in h.groupby("ciclo")] + [("2022-2026 (processos distintos)", hd)]
    for rot, g in grupos:
        a, t = g["valor_autorizado"], g["valor_total"]
        ambos = g[a.notna() & t.notna()]
        razao = ambos["valor_autorizado"] / ambos["valor_total"]
        linhas.append({
            "ciclo": rot, "registros": len(g), "processos": g["numero_processo"].nunique(),
            "proponentes_distintos": g["chave_proponente"].nunique(),
            "autorizado_n": int(a.notna().sum()), "autorizado_total": a.sum(), "autorizado_media": a.mean(),
            "autorizado_mediana": a.median(), "autorizado_p90": a.quantile(0.9),
            "autorizado_min": a.min(), "autorizado_max": a.max(),
            "total_n": int(t.notna().sum()), "total_soma": t.sum(), "total_media": t.mean(),
            "total_mediana": t.median(),
            "razao_n": len(ambos), "razao_agregada": ambos["valor_autorizado"].sum() / ambos["valor_total"].sum(),
            "razao_mediana": razao.median(),
            "pct_razao_igual_1": float((igual_centavo(ambos["valor_autorizado"], ambos["valor_total"])).mean()),
            "n_autorizado_maior_total": int((ambos["valor_autorizado"] > ambos["valor_total"] + 0.005).sum()),
            "municipio_valor_n": int(g["municipio_valor"].notna().sum()),
        })
    return salvar(pd.DataFrame(linhas), "anual")


def status(h: pd.DataFrame, mun: pd.DataFrame) -> pd.DataFrame:
    tab = pd.crosstab(h["ciclo"], h["status"]).reindex(columns=list(STATUS_ROTULO), fill_value=0)
    tab["total"] = tab.sum(axis=1)
    tab["executados"] = tab["em_execucao"] + tab["concluido"]
    tab["resolvidos"] = tab["total"] - tab["captando"]
    tab["taxa_execucao_sobre_total"] = tab["executados"] / tab["total"]
    tab["taxa_execucao_sobre_resolvidos"] = tab["executados"] / tab["resolvidos"]
    tab["taxa_expiracao_sobre_resolvidos"] = tab["captacao_expirada"] / tab["resolvidos"]
    tab["pct_ainda_captando"] = tab["captando"] / tab["total"]
    out = tab.reset_index()
    salvar(pd.DataFrame({"codigo_csv": list(STATUS_ROTULO), "rotulo_fonte": list(STATUS_ROTULO.values())}),
           "status_rotulos")
    # Conversão por natureza jurídica (ciclos 2022-2024, quase todos resolvidos)
    g = h[h["ciclo"] <= 2024].copy()
    g["executado"] = g["status"].isin(["em_execucao", "concluido"])
    g["resolvido"] = g["status"] != "captando"
    nat = (g[g["resolvido"]].groupby("natureza_rotulo")
           .agg(registros_resolvidos=("executado", "size"), executados=("executado", "sum"))
           .assign(taxa_execucao=lambda x: x["executados"] / x["registros_resolvidos"]).reset_index())
    salvar(nat, "status_conversao_por_natureza_2022_2024")
    # Conversão por faixa de valor autorizado (ciclos 2022-2024)
    g["faixa_valor"] = pd.cut(g["valor_autorizado"], [0, 200_000, 400_000, 499_999.99, 500_000, 1_000_000],
                              labels=["até 200 mil", "200-400 mil", "400-500 mil (exclusive)", "exatamente 500 mil",
                                      "acima de 500 mil"])
    fx = (g[g["resolvido"]].groupby("faixa_valor", observed=False)
          .agg(registros_resolvidos=("executado", "size"), executados=("executado", "sum"))
          .assign(taxa_execucao=lambda x: x["executados"] / x["registros_resolvidos"]).reset_index())
    fx["nota"] = f"valor ausente em {int(g.loc[g['resolvido'], 'valor_autorizado'].isna().sum())} registros resolvidos"
    salvar(fx, "status_conversao_por_faixa_valor_2022_2024")
    # A mesma conversão por faixa DENTRO de cada ciclo: afasta a leitura de que o gradiente
    # agregado seria só composição (ciclos com projetos menores e conversão diferente).
    g["faixa_valor_ciclo"] = pd.cut(g["valor_autorizado"], [0, 400_000, 499_999.99, 500_000, 1_000_000],
                                    labels=["até 400 mil", "400-500 mil (exclusive)", "exatamente 500 mil",
                                            "acima de 500 mil"])
    fxc = (g[g["resolvido"]].groupby(["ciclo", "faixa_valor_ciclo"], observed=False)
           .agg(registros_resolvidos=("executado", "size"), executados=("executado", "sum"))
           .assign(taxa_execucao=lambda x: x["executados"] / x["registros_resolvidos"]).reset_index())
    salvar(fxc, "status_conversao_por_faixa_valor_e_ciclo")
    # Conversão RMGV x interior (só registros com um único município do ES: é a única
    # atribuição territorial sem rateio; os demais ficam fora, com a contagem declarada)
    rm = set(mun.loc[mun["rmgv"], "cod_ibge"])
    un = g[g["resolvido"] & g["cod_ibge_valor"].notna()].copy()
    un["territorio"] = np.where(un["cod_ibge_valor"].isin(rm), "RMGV", "Interior")
    ter = (un.groupby("territorio").agg(registros_resolvidos=("executado", "size"), executados=("executado", "sum"))
           .assign(taxa_execucao=lambda x: x["executados"] / x["registros_resolvidos"]).reset_index())
    ter["cobertura"] = f"{len(un)}/{int(g['resolvido'].sum())} registros resolvidos com município único"
    salvar(ter, "status_conversao_rmgv_interior_2022_2024")
    # Conversão por recorrência do proponente (ciclos 2023-2024: em 2022 ninguém tem ciclo anterior).
    # Recorrente = proponente (chave_proponente) já presente em ciclo anterior da lista.
    primeiro = h.groupby("chave_proponente")["ciclo"].min()
    rc = g[g["resolvido"] & (g["ciclo"] >= 2023)].copy()
    rc["proponente"] = np.where(rc["ciclo"] > rc["chave_proponente"].map(primeiro), "recorrente", "estreante")
    rec = pd.concat([
        rc.groupby(["ciclo", "proponente"]).agg(registros_resolvidos=("executado", "size"),
                                                executados=("executado", "sum")).reset_index(),
        rc.groupby("proponente").agg(registros_resolvidos=("executado", "size"), executados=("executado", "sum"))
          .reset_index().assign(ciclo="2023-2024")])
    rec["taxa_execucao"] = rec["executados"] / rec["registros_resolvidos"]
    salvar(rec[["ciclo", "proponente", "registros_resolvidos", "executados", "taxa_execucao"]],
           "status_conversao_recorrencia_2023_2024")
    return salvar(out, "status_por_ciclo")


def cotas(h: pd.DataFrame, mun: pd.DataFrame) -> pd.DataFrame:
    g = h[h["ciclo"] >= 2024]
    t = (g.groupby(["ciclo", "enquadramento"], dropna=False)
         .agg(registros=("numero_processo", "size"), autorizado_n=("valor_autorizado", "count"),
              autorizado_total=("valor_autorizado", "sum")).reset_index())
    t["pct_registros"] = t["registros"] / t.groupby("ciclo")["registros"].transform("sum")
    t["pct_autorizado"] = t["autorizado_total"] / t.groupby("ciclo")["autorizado_total"].transform("sum")
    t["pct_normativo_art18"] = t["enquadramento"].map(COTA_PCT)
    t["rotulo"] = t["enquadramento"].map(COTA_ROTULO)
    cobertura = h.groupby("ciclo")["enquadramento"].apply(lambda s: f"{s.notna().sum()}/{len(s)}").reset_index(
        name="cobertura_enquadramento")
    salvar(cobertura, "enquadramento_cobertura")
    # Coerência territorial da cota III (execução fora da RMGV; a sede não é publicada)
    rm = set(mun.loc[mun["rmgv"], "municipio"])
    f = h[h["enquadramento"] == "cota-fora-rmgv"].copy()
    f["municipios_lista"] = f["municipios_es"].fillna("").map(lambda s: [x for x in s.split("; ") if x])
    f["algum_municipio_rmgv"] = f["municipios_lista"].map(lambda xs: any(x in rm for x in xs))
    f["sem_municipio_resolvido"] = f["municipios_lista"].map(len) == 0
    salvar(f[["ciclo", "numero_processo", "projeto", "municipios_es", "locais_nao_resolvidos",
              "algum_municipio_rmgv", "sem_municipio_resolvido"]], "cota_fora_rmgv_coerencia")
    # Registros de cota IV executados só no interior (poderiam, em tese, ter pedido a III)
    d = h[(h["enquadramento"] == "cota-demais")].copy()
    d["municipios_lista"] = d["municipios_es"].fillna("").map(lambda s: [x for x in s.split("; ") if x])
    d["so_interior"] = d["municipios_lista"].map(lambda xs: len(xs) > 0 and all(x not in rm for x in xs))
    salvar(d.groupby("ciclo").agg(registros_cota_iv=("so_interior", "size"),
                                  execucao_so_no_interior=("so_interior", "sum")).reset_index(),
           "cota_iv_execucao_so_interior")
    return salvar(t, "enquadramento_por_ciclo")


def bunching(h: pd.DataFrame, hd: pd.DataFrame) -> pd.DataFrame:
    linhas = []
    for rot, g in [(str(c), x) for c, x in h.groupby("ciclo")] + [("2022-2026 (processos distintos)", hd)]:
        a = g["valor_autorizado"].dropna()
        n = len(a)
        linhas.append({
            "ciclo": rot, "n_com_valor": n, "n_total": len(g),
            "exatamente_500mil": int(igual_centavo(a, TETO_GERAL).sum()),
            "entre_490mil_e_500mil_excl": int(((a >= 490_000) & (a < TETO_GERAL - 0.005)).sum()),
            "entre_450mil_e_490mil": int(((a >= 450_000) & (a < 490_000)).sum()),
            "exatamente_300mil": int(igual_centavo(a, TETO_1A_EDICAO).sum()),
            "acima_500mil": int((a > TETO_GERAL + 0.005).sum()),
            "exatamente_1mi": int(igual_centavo(a, TETO_ESPECIAL).sum()),
            "abaixo_300mil": int((a < TETO_1A_EDICAO - 0.005).sum()),
        })
    t = pd.DataFrame(linhas)
    t["pct_exatamente_500mil"] = t["exatamente_500mil"] / t["n_com_valor"]
    t["pct_490_a_500mil_inclusive"] = (t["exatamente_500mil"] + t["entre_490mil_e_500mil_excl"]) / t["n_com_valor"]
    # Densidade em faixas de R$ 10 mil perto do teto (para o teste visual de bunching)
    a = hd["valor_autorizado"].dropna()
    bins = np.arange(400_000, 510_001, 10_000)
    cont, _ = np.histogram(a[(a >= 400_000) & (a <= 510_000)], bins=bins)
    salvar(pd.DataFrame({"faixa_inicio": bins[:-1], "faixa_fim": bins[1:], "processos": cont}),
           "bunching_faixas_10mil")
    acima = hd.loc[hd["valor_autorizado"] > TETO_GERAL + 0.005,
                   ["numero_processo", "ciclo", "projeto", "proponente", "valor_autorizado", "valor_total",
                    "enquadramento"]]
    salvar(acima, "acima_teto_geral")
    # Valor total > autorizado: projetos com outras fontes além da LICC
    return salvar(t, "bunching_teto")


# --------------------------------------------------------------------------------------


def theil_decomposto(s_val: pd.Series, pop: pd.Series, grupo: pd.Series) -> dict:
    s = s_val / s_val.sum()
    p = pop / pop.sum()
    total = theil_t(s_val.values, pop.values)
    entre, dentro = 0.0, 0.0
    for gname in grupo.unique():
        m = grupo == gname
        sg, pg = s[m].sum(), p[m].sum()
        if sg > 0:
            entre += sg * np.log(sg / pg)
            dentro += sg * theil_t(s_val[m].values, pop[m].values)
    return {"theil_total": total, "theil_entre_rmgv_interior": entre, "theil_dentro": dentro}


def territorio(h: pd.DataFrame, hd: pd.DataFrame, pm: pd.DataFrame, mun: pd.DataFrame, c: pd.DataFrame):
    m = mun[["cod_ibge", "municipio", "rmgv", "microrregiao", "regiao_intermediaria", "pop_censo2022",
             "pop_est2025", "pib_2023_mil"]].copy()
    # presença (processos distintos, qualquer seção)
    pmd = pm.drop_duplicates(["numero_processo", "cod_ibge"])
    pres = pmd.groupby("cod_ibge")["numero_processo"].nunique().rename("processos_presenca")
    # valor atribuível: processos com um único local, que é município do ES
    val = (hd[hd["cod_ibge_valor"].notna()].groupby("cod_ibge_valor")
           .agg(processos_valor=("numero_processo", "size"), autorizado_atribuivel=("valor_autorizado", "sum"),
                autorizado_n=("valor_autorizado", "count")))
    val.index = val.index.astype(int)
    m = m.join(pres, on="cod_ibge").join(val, on="cod_ibge")
    for col in ("processos_presenca", "processos_valor", "autorizado_atribuivel", "autorizado_n"):
        m[col] = m[col].fillna(0)  # aqui zero é dado: nenhum processo nomeou o município
    m["autorizado_per_capita"] = m["autorizado_atribuivel"] / m["pop_censo2022"]
    m["presenca_por_100mil_hab"] = m["processos_presenca"] / m["pop_censo2022"] * 1e5
    m["share_valor"] = m["autorizado_atribuivel"] / m["autorizado_atribuivel"].sum()
    m["share_pop"] = m["pop_censo2022"] / m["pop_censo2022"].sum()
    m["share_pib"] = m["pib_2023_mil"] / m["pib_2023_mil"].sum()
    m["share_presenca"] = m["processos_presenca"] / m["processos_presenca"].sum()
    m["razao_valor_pop"] = m["share_valor"] / m["share_pop"]
    m = m.sort_values("autorizado_atribuivel", ascending=False)
    salvar(m, "municipios")

    # por ciclo (presença e valor)
    pc = pm.merge(h[["numero_processo", "ciclo"]].drop_duplicates(), on=["numero_processo", "ciclo"])
    pres_c = pc.groupby("ciclo")["cod_ibge"].nunique()
    val_c = h[h["cod_ibge_valor"].notna()].groupby("ciclo")["cod_ibge_valor"].nunique()
    rm = set(mun.loc[mun["rmgv"], "cod_ibge"])
    linhas = []
    for ciclo, g in h.groupby("ciclo"):
        gv = g[g["cod_ibge_valor"].notna()]
        v_rm = gv.loc[gv["cod_ibge_valor"].astype(int).isin(rm), "valor_autorizado"].sum()
        v_all = gv["valor_autorizado"].sum()
        mc = mun[["cod_ibge", "pop_censo2022"]].merge(
            gv.groupby("cod_ibge_valor")["valor_autorizado"].sum().rename("v").rename_axis("cod_ibge").reset_index()
            .assign(cod_ibge=lambda x: x["cod_ibge"].astype(int)), on="cod_ibge", how="left").fillna({"v": 0})
        linhas.append({
            "ciclo": ciclo, "registros": len(g),
            "registros_com_municipio_unico": len(gv),
            "autorizado_atribuivel": v_all,
            "pct_autorizado_atribuivel": v_all / g["valor_autorizado"].sum(),
            "municipios_com_presenca": int(pres_c.get(ciclo, 0)),
            "municipios_sem_presenca": 78 - int(pres_c.get(ciclo, 0)),
            "municipios_com_valor_atribuivel": int(val_c.get(ciclo, 0)),
            "pct_valor_atribuivel_na_rmgv": v_rm / v_all if v_all else np.nan,
            "gini_valor_78_municipios": gini(mc["v"]),
            "gini_per_capita_78": gini(mc["v"] / mc["pop_censo2022"]),
        })
    por_ciclo = salvar(pd.DataFrame(linhas), "territorio_por_ciclo")

    # coortes de primeira presença (tratamento escalonado do desenho municipal, seção 5.2 do artigo)
    prim = pc.groupby("cod_ibge")["ciclo"].min()
    coortes = mun[["cod_ibge", "municipio", "rmgv", "pop_censo2022"]].copy()
    coortes["primeiro_ciclo"] = coortes["cod_ibge"].map(prim)
    resumo = (coortes.assign(primeiro_ciclo=coortes["primeiro_ciclo"].map(
                  lambda x: "nunca (2022-2026)" if pd.isna(x) else str(int(x))))
              .groupby("primeiro_ciclo")
              .agg(municipios=("cod_ibge", "size"), municipios_rmgv=("rmgv", "sum"),
                   pop_mediana=("pop_censo2022", "median"))
              .reset_index())
    salvar(resumo, "coortes_primeira_presenca_canonico")

    # resumo agregado 2022-2026
    grp = np.where(m["rmgv"], "RMGV", "Interior")
    res = []
    for rot, mask in (("RMGV", m["rmgv"]), ("Interior", ~m["rmgv"]), ("ES", m["rmgv"] | ~m["rmgv"])):
        g = m[mask]
        res.append({"grupo": rot, "municipios": len(g), "pop_censo2022": g["pop_censo2022"].sum(),
                    "pib_2023_mil": g["pib_2023_mil"].sum(),
                    "municipios_sem_presenca": int((g["processos_presenca"] == 0).sum()),
                    "municipios_sem_valor_atribuivel": int((g["autorizado_atribuivel"] == 0).sum()),
                    "processos_presenca_soma": g["processos_presenca"].sum(),
                    "processos_valor": g["processos_valor"].sum(),
                    "autorizado_atribuivel": g["autorizado_atribuivel"].sum()})
    r = pd.DataFrame(res)
    tot = r.loc[r.grupo == "ES"].iloc[0]
    for col in ("pop_censo2022", "pib_2023_mil", "processos_presenca_soma", "autorizado_atribuivel"):
        r[f"share_{col}"] = r[col] / tot[col]
    r["autorizado_per_capita"] = r["autorizado_atribuivel"] / r["pop_censo2022"]
    salvar(r, "territorio_rmgv_interior")

    # desigualdade e correlações
    th = theil_decomposto(m["autorizado_atribuivel"], m["pop_censo2022"], pd.Series(grp, index=m.index))
    pos = m[m["autorizado_atribuivel"] > 0]
    ind = {
        "cobertura_valor_atribuivel": f"{int(hd['cod_ibge_valor'].notna().sum())}/{len(hd)} processos; "
                                      f"{hd.loc[hd['cod_ibge_valor'].notna(), 'valor_autorizado'].sum() / hd['valor_autorizado'].sum():.3f} do valor autorizado conhecido",
        "gini_valor_78": gini(m["autorizado_atribuivel"]),
        "gini_per_capita_78": gini(m["autorizado_per_capita"]),
        "gini_presenca_78": gini(m["processos_presenca"]),
        "gini_populacao_78": gini(m["pop_censo2022"]),
        "gini_pib_78": gini(m["pib_2023_mil"]),
        "theil_t_nao_ponderado_78": theil_t(m["autorizado_atribuivel"].values),
        **{k: v for k, v in th.items()},
        "pct_theil_entre_grupos": th["theil_entre_rmgv_interior"] / th["theil_total"],
        "spearman_valor_pop_78": stats.spearmanr(m["autorizado_atribuivel"], m["pop_censo2022"])[0],
        "spearman_valor_pib_78": stats.spearmanr(m["autorizado_atribuivel"], m["pib_2023_mil"])[0],
        "spearman_presenca_pop_78": stats.spearmanr(m["processos_presenca"], m["pop_censo2022"])[0],
        "spearman_percapita_pop_78": stats.spearmanr(m["autorizado_per_capita"], m["pop_censo2022"])[0],
        "pearson_log_valor_log_pop_positivos": stats.pearsonr(np.log(pos["autorizado_atribuivel"]),
                                                               np.log(pos["pop_censo2022"]))[0],
        "n_positivos": len(pos),
        "elasticidade_ols_log_valor_log_pop_positivos": np.polyfit(np.log(pos["pop_censo2022"]),
                                                                  np.log(pos["autorizado_atribuivel"]), 1)[0],
        "vitoria_share_valor": float(m.loc[m["municipio"] == "Vitória", "share_valor"].iloc[0]),
        "vitoria_share_pop": float(m.loc[m["municipio"] == "Vitória", "share_pop"].iloc[0]),
        "vitoria_share_presenca": float(m.loc[m["municipio"] == "Vitória", "share_presenca"].iloc[0]),
    }
    salvar(pd.DataFrame({"indicador": list(ind), "valor": list(ind.values())}), "territorio_indicadores")

    # perfil territorial de quem captou em 2025 (via casamento exato; sensibilidade com secundário)
    cc = c.copy()
    base = hd.set_index("numero_processo")
    perfil = []
    for rot, col in (("principal (título exato)", "numero_processo"),
                     ("principal + secundário", None)):
        procs = cc["numero_processo"] if col else cc["numero_processo"].fillna(cc["numero_processo_secundario"])
        sub = cc.assign(proc=procs)
        sub = sub[sub["proc"].notna()]
        sub = sub.join(base[["tipo_local", "cod_ibge_valor", "municipios_es"]], on="proc")
        unico = sub[sub["cod_ibge_valor"].notna()]
        em_rm = unico["cod_ibge_valor"].astype(int).isin(rm)
        perfil.append({"casamento": rot, "captados_total": len(cc), "casados": len(sub),
                       "com_municipio_unico": len(unico),
                       "captado_casado": sub["valor_captado"].sum(),
                       "captado_com_municipio_unico": unico["valor_captado"].sum(),
                       "captado_rmgv": unico.loc[em_rm, "valor_captado"].sum(),
                       "captado_interior": unico.loc[~em_rm, "valor_captado"].sum(),
                       "pct_captado_rmgv_entre_unicos": unico.loc[em_rm, "valor_captado"].sum() / unico[
                           "valor_captado"].sum(),
                       "projetos_rmgv": int(em_rm.sum()), "projetos_interior": int((~em_rm).sum()),
                       "municipios_distintos": unico["cod_ibge_valor"].nunique(),
                       "varios_municipios": int((sub["tipo_local"] == "varios_municipios").sum())})
    salvar(pd.DataFrame(perfil), "captados_perfil_territorial")
    return m, por_ciclo


# --------------------------------------------------------------------------------------


def proponentes(h: pd.DataFrame, hd: pd.DataFrame, prop: pd.DataFrame, c: pd.DataFrame):
    # recorrência entre ciclos
    pc = h.groupby("chave_proponente").agg(ciclos=("ciclo", lambda s: ";".join(map(str, sorted(set(s))))),
                                           n_ciclos=("ciclo", "nunique"),
                                           registros=("numero_processo", "size"))
    vd = hd.groupby("chave_proponente").agg(processos=("numero_processo", "nunique"),
                                            autorizado_total=("valor_autorizado", "sum"),
                                            autorizado_n=("valor_autorizado", "count"))
    t = pc.join(vd).join(prop.set_index("chave_proponente")[["natureza_rotulo", "variantes"]])
    t = t.sort_values("autorizado_total", ascending=False).reset_index()
    t["share_autorizado"] = t["autorizado_total"] / t["autorizado_total"].sum()
    t["share_acumulado"] = t["share_autorizado"].cumsum()
    salvar(t, "proponentes_ranking")

    dist_ciclos = t["n_ciclos"].value_counts().sort_index().rename_axis("n_ciclos").reset_index(name="proponentes")
    dist_ciclos["autorizado"] = dist_ciclos["n_ciclos"].map(t.groupby("n_ciclos")["autorizado_total"].sum())
    dist_ciclos["pct_proponentes"] = dist_ciclos["proponentes"] / dist_ciclos["proponentes"].sum()
    dist_ciclos["pct_autorizado"] = dist_ciclos["autorizado"] / dist_ciclos["autorizado"].sum()
    salvar(dist_ciclos, "proponentes_recorrencia")

    # por ciclo: concentração e presença em ciclo anterior
    linhas = []
    vistos = set()
    for ciclo, g in h.groupby("ciclo"):
        v = g.groupby("chave_proponente")["valor_autorizado"].sum()
        n_por = g.groupby("chave_proponente").size()
        props = set(g["chave_proponente"])
        linhas.append({
            "ciclo": ciclo, "proponentes": len(props), "registros": len(g),
            "registros_por_proponente": len(g) / len(props),
            "proponentes_com_3_ou_mais": int((n_por >= 3).sum()),
            "max_registros_um_proponente": int(n_por.max()),
            "pct_proponentes_ja_vistos_em_ciclo_anterior": len(props & vistos) / len(props) if vistos else np.nan,
            "pct_valor_de_proponentes_ja_vistos": v[v.index.isin(vistos)].sum() / v.sum() if vistos else np.nan,
            "top10_share_valor": cr(v.values, 10), "top1_share_valor": cr(v.values, 1),
            "hhi_proponentes": hhi(v.values), "gini_proponentes": gini(v.values),
            "n_equivalente_1_sobre_hhi": 10_000 / hhi(v.values),
            "cobertura_valor": f"{int(g['valor_autorizado'].notna().sum())}/{len(g)}",
        })
        vistos |= props
    v_all = hd.groupby("chave_proponente")["valor_autorizado"].sum()
    linhas.append({"ciclo": "2022-2026 (processos distintos)", "proponentes": hd["chave_proponente"].nunique(),
                   "registros": len(hd), "registros_por_proponente": len(hd) / hd["chave_proponente"].nunique(),
                   "top10_share_valor": cr(v_all.values, 10), "top1_share_valor": cr(v_all.values, 1),
                   "hhi_proponentes": hhi(v_all.values), "gini_proponentes": gini(v_all.values),
                   "n_equivalente_1_sobre_hhi": 10_000 / hhi(v_all.values),
                   "cobertura_valor": f"{int(hd['valor_autorizado'].notna().sum())}/{len(hd)}"})
    salvar(pd.DataFrame(linhas), "proponentes_por_ciclo")

    # natureza jurídica inferida
    nat = (hd.groupby("natureza_rotulo")
           .agg(proponentes=("chave_proponente", "nunique"), processos=("numero_processo", "size"),
                autorizado=("valor_autorizado", "sum")).reset_index())
    for col in ("proponentes", "processos", "autorizado"):
        nat[f"pct_{col}"] = nat[col] / nat[col].sum()
    nat["autorizado_mediano_por_processo"] = nat["natureza_rotulo"].map(
        hd.groupby("natureza_rotulo")["valor_autorizado"].median())
    salvar(nat.sort_values("autorizado", ascending=False), "proponentes_natureza")
    natc = pd.crosstab(h["ciclo"], h["natureza_rotulo"], normalize="index").reset_index()
    salvar(natc, "proponentes_natureza_por_ciclo")
    salvar(pd.DataFrame({"ordem": range(1, 7), "codigo": ["mei_ei", "empresa_sufixo", "osc", "empresa_provavel",
                                                         "grupo_artistico", "indeterminado"],
                         "regra": [
                             "CPF (11 dígitos) ou raiz de CNPJ no nome, ou a palavra MEI (razão social de MEI é nome + CPF)",
                             "sufixo LTDA, EIRELI, EPP, S/A ou ME no nome",
                             "associação, instituto, instituição, fundação, grêmio, sociedade, federação, academia de letras, "
                             "centro cultural/de cultura/desportivo, circolo, colônia de pescadores, sindicato, mosteiro, "
                             "convention bureau, secretariado, programa de promoção, agência de desenvolvimento",
                             "termo comercial sem sufixo: produções, produtora, eventos, filmes, editora, estúdio/studio, "
                             "comunicação, marketing, projetos, design, entretenimento, consultoria, serviços, "
                             "empreendimentos, records, music, company, economia criativa, soluções, associados, press",
                             "coletivo, grupo teatral, cia/companhia, bloco, movimento cultural (natureza não inferível)",
                             "nenhuma regra casou (inclui nomes de pessoa natural sem CPF — prováveis MEI/EI)"]}),
           "proponentes_natureza_regras")

    # captados 2025: concentração por proponente
    vc = c.assign(ch=c["chave_proponente"]).groupby("ch")["valor_captado"].sum()
    return pd.DataFrame({"proponentes_captados_2025": [len(vc)], "top10_share": [cr(vc.values, 10)],
                         "top1_share": [cr(vc.values, 1)], "hhi": [hhi(vc.values)]})


def captados(c: pd.DataFrame, ap: pd.DataFrame, prop: pd.DataFrame, conc_prop: pd.DataFrame) -> None:
    c = c.copy()
    c["razao_captado"] = c["valor_captado"] / c["valor_autorizado"]
    c["captacao"] = np.where(c["valor_captado"] >= c["valor_autorizado"] - 0.005, "total", "parcial")
    npat = ap.groupby("id_captado")["cnpj_raiz"].nunique()
    nterm = ap.groupby("id_captado").size()
    c["n_patrocinadores"] = c["id_captado"].map(npat)
    c["n_termos"] = c["id_captado"].map(nterm)
    c = c.merge(prop[["chave_proponente", "natureza_rotulo"]], on="chave_proponente", how="left")
    salvar(c.drop(columns=["titulo_norm"]), "captados_projetos")

    resumo = {
        "projetos": len(c), "autorizado_total": c["valor_autorizado"].sum(),
        "captado_total": c["valor_captado"].sum(),
        "taxa_captado_sobre_autorizado": c["valor_captado"].sum() / c["valor_autorizado"].sum(),
        "captacao_total_n": int((c["captacao"] == "total").sum()),
        "captacao_parcial_n": int((c["captacao"] == "parcial").sum()),
        "captado_acima_autorizado_n": int((c["valor_captado"] > c["valor_autorizado"] + 0.005).sum()),
        "razao_min": c["razao_captado"].min(), "razao_mediana_parciais": c.loc[c.captacao == "parcial", "razao_captado"].median(),
        "parciais_abaixo_35pct": int((c["razao_captado"] < 0.35).sum()),
        "captado_medio": c["valor_captado"].mean(), "captado_mediano": c["valor_captado"].median(),
        "captado_exatamente_500mil": int(igual_centavo(c["valor_captado"], TETO_GERAL).sum()),
        "proponentes_distintos": c["chave_proponente"].nunique(),
        "termos": len(ap), "cnpjs_estabelecimento": ap["cnpj"].nunique(), "empresas_raiz_cnpj": ap["cnpj_raiz"].nunique(),
        "nomes_de_patrocinador_distintos": ap["patrocinador_nome"].nunique(),
        "soma_aportes": ap["valor"].sum(),
        "casamento_titulo_exato": int((c["casamento"] == "casado").sum()),
        "casamento_ambiguo": int((c["casamento"] == "ambiguo").sum()),
        "casamento_sem_correspondencia": int((c["casamento"] == "sem_correspondencia").sum()),
        "casamento_secundario_desempatados": int(c["numero_processo_secundario"].notna().sum()),
        **{f"proponentes_{k}": v for k, v in conc_prop.iloc[0].items()},
    }
    salvar(pd.DataFrame({"indicador": list(resumo), "valor": list(resumo.values())}), "captados_resumo")

    salvar(c["n_patrocinadores"].value_counts().sort_index().rename_axis("n_patrocinadores")
           .reset_index(name="projetos"), "captados_patrocinadores_por_projeto")
    ciclo = c["ciclos_habilitacao"].fillna("sem casamento exato").value_counts().rename_axis(
        "ciclos_habilitacao").reset_index(name="projetos")
    ciclo["captado"] = ciclo["ciclos_habilitacao"].map(
        c.assign(k=c["ciclos_habilitacao"].fillna("sem casamento exato")).groupby("k")["valor_captado"].sum())
    salvar(ciclo, "captados_por_ciclo_habilitacao")
    salvar(c.groupby("natureza_rotulo").agg(projetos=("id_captado", "size"), captado=("valor_captado", "sum"))
           .assign(pct_captado=lambda x: x["captado"] / x["captado"].sum()).reset_index(), "captados_natureza")

    # patrocinadores por raiz de CNPJ (= empresa)
    p = (ap.groupby("cnpj_raiz")
         .agg(nome=("patrocinador_nome", lambda s: s.value_counts().index[0]),
              variantes_nome=("patrocinador_nome", lambda s: " | ".join(sorted(set(s)))),
              cnpjs_estabelecimento=("cnpj", "nunique"), termos=("valor", "size"),
              projetos=("id_captado", "nunique"), aportado=("valor", "sum"))
         .sort_values("aportado", ascending=False).reset_index())
    p["share"] = p["aportado"] / p["aportado"].sum()
    p["share_acumulado"] = p["share"].cumsum()
    p[["setor_inferido", "macrossetor", "confianca_setor"]] = pd.DataFrame(
        p["cnpj_raiz"].map(lambda r: SETOR.get(r, ("[VERIFICAR]", "[VERIFICAR]", "baixa"))).tolist(), index=p.index)
    salvar(p, "patrocinadores")
    conc = {
        "empresas": len(p), "CR1": cr(p["aportado"], 1), "CR4": cr(p["aportado"], 4), "CR8": cr(p["aportado"], 8),
        "HHI": hhi(p["aportado"]), "n_equivalente_1_sobre_HHI": 10_000 / hhi(p["aportado"]),
        "gini": gini(p["aportado"]),
        "empresas_para_metade": int((p["share_acumulado"] < 0.5).sum() + 1),
        "maior_empresa": p.loc[0, "nome"], "maior_empresa_projetos": int(p.loc[0, "projetos"]),
        "maior_empresa_termos": int(p.loc[0, "termos"]),
        "cobertura": f"{int(ap['valor'].notna().sum())}/{len(ap)} termos com valor",
    }
    salvar(pd.DataFrame({"indicador": list(conc), "valor": list(conc.values())}), "patrocinadores_concentracao")
    ms = (p.groupby("macrossetor").agg(empresas=("cnpj_raiz", "size"), aportado=("aportado", "sum"),
                                        projetos_distintos=("cnpj_raiz", lambda s: ap.loc[
                                            ap["cnpj_raiz"].isin(s), "id_captado"].nunique()))
          .assign(share=lambda x: x["aportado"] / x["aportado"].sum()).sort_values("aportado", ascending=False)
          .reset_index())
    salvar(ms, "patrocinadores_macrossetor")


def main() -> None:
    h, hd, pm, c, ap, prop, mun = carregar()
    anual(h, hd)
    status(h, mun)
    cotas(h, mun)
    bunching(h, hd)
    territorio(h, hd, pm, mun, c)
    conc_prop = proponentes(h, hd, prop, c)
    captados(c, ap, prop, conc_prop)
    print("tabelas gravadas em", TABELAS)


if __name__ == "__main__":
    main()
