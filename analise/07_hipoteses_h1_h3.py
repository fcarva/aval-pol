"""
07 — Evidência descritiva e poder estatístico para as hipóteses dos autores sobre a LICC
(notas/desenho/03-teoria-da-mudanca-e-hipoteses.md):

  H1  a coordenação centralizada (habilitação) + escolha privada favorece empresas que usam o crédito como
      orçamento de marketing;
  H2  poucos projetos passam (funil);
  H3  há atrito na entrada (custo de se inscrever e de chegar à habilitação).

O script não testa causalmente nenhuma hipótese: produz os fatos que delimitam o que precisa ser estimado e
o efeito mínimo detectável (EMD) dos desenhos propostos. Regras do CLAUDE.md: ausência não é zero (inscritos
não habilitados não são publicados: a coluna fica vazia, não zero); captados ≠ habilitados (funil por ciclo de
habilitação e funil por ano de captação ficam em tabelas separadas).

Fontes:
  dados/processados/habilitados.csv                (01_carregar.py; lista oficial da SECULT)
  dados/externos/municipios_es.csv                 (RMGV pela LC 318/2005)
  analise/tabelas/03f_captacao_anual_secult.csv    (03f_captados_por_cota.py; anexos "Recurso financeiro captado")
  dados/externos/raw/salic/projetos_ano*.json      (03a_salic_rouanet_uf.py; API pública do SALIC)
Saídas (analise/tabelas/):
  07_funil_por_ciclo.csv            habilitados → captou / expirou / captando, por ciclo e regime
  07_funil_captacao_anual.csv       montante, validado, indeferido por teto (demanda com patrocinador ÷ teto)
  07_composicao_por_ciclo.csv       quem entra: recorrência (janela fixa), teto de R$ 500 mil, RMGV, natureza
  07_rouanet_es_composicao.csv      mesma recorrência entre proponentes do ES na Rouanet (comparação)
  07_mudanca_regime.csv             variação 2024 → 2025-2026 na LICC e na Rouanet-ES (descritivo)
  07_poder_hipoteses.csv            EMD dos desenhos propostos para H1-H3
  07_mapa_cultural_universo.csv     agentes cadastrados no Mapa Cultural ES (topo do funil de H3)
  07_patrocinadores_na_rouanet.csv  patrocinadores LICC 2025 que também aparecem como incentivadores no SALIC (H1)
Uso: python analise/07_hipoteses_h1_h3.py
"""
from __future__ import annotations

import glob
import importlib.util
import json
import unicodedata
from pathlib import Path

import numpy as np
import pandas as pd

RAIZ = Path(__file__).resolve().parents[1]
TAB = RAIZ / "analise" / "tabelas"

_spec = importlib.util.spec_from_file_location("poder", RAIZ / "analise" / "05_poder_mde.py")
poder = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(poder)

# Regime da etapa análise → captação (notas/politica/01-desenho-legal.md, § 7 e atualização de 24/09/2026):
# 2022-2024 a CAP habilita antes de haver patrocinador; a partir da IN 001/2025 só chega à CAP quem já tem
# termos (≥ 35%) ou, desde a Portaria 062-S/2025, carta de intenção de patrocínio.
REGIME = {2022: "habilitação primeiro", 2023: "habilitação primeiro", 2024: "habilitação primeiro",
          2025: "patrocinador primeiro", 2026: "patrocinador primeiro"}


def _norm(s) -> str:
    s = unicodedata.normalize("NFKD", str(s))
    return "".join(c for c in s if not unicodedata.combining(c)).lower().strip()


def carregar() -> pd.DataFrame:
    # Por ciclo, conta registros como 03_descritivas.py (03_status_por_ciclo.csv): 4 processos aparecem nas
    # listas de 2025 e de 2026 e entram nos dois ciclos.
    h = pd.read_csv(RAIZ / "dados" / "processados" / "habilitados.csv")
    mun = pd.read_csv(RAIZ / "dados" / "externos" / "municipios_es.csv")
    rm = set(mun.loc[mun["rmgv"], "cod_ibge"])
    h["rmgv"] = h["cod_ibge_valor"].map(lambda c: np.nan if pd.isna(c) else float(int(c) in rm))
    return h


def funil_por_ciclo(h: pd.DataFrame) -> pd.DataFrame:
    linhas = []
    for ciclo, g in h.groupby("ciclo"):
        st = g["status"].value_counts()
        captou = int(st.get("concluido", 0) + st.get("em_execucao", 0))
        expirou = int(st.get("captacao_expirada", 0))
        captando = int(st.get("captando", 0))
        linhas.append({
            "ciclo": ciclo, "regime": REGIME[ciclo],
            "inscritos": np.nan,  # não publicado: pedir por LAI (ausência não é zero)
            "habilitados": len(g), "captou": captou, "expirou": expirou, "ainda_captando": captando,
            "taxa_captou_sobre_resolvidos": captou / (captou + expirou) if captou + expirou else np.nan,
            "pct_ainda_captando": captando / len(g),
        })
    return pd.DataFrame(linhas)


def funil_captacao_anual() -> pd.DataFrame:
    f = pd.read_csv(TAB / "03f_captacao_anual_secult.csv")
    f = f[["ano_captacao", "montante_declarado", "total_validado", "total_indeferido", "termos_indeferidos",
           "origem_total_indeferido"]].copy()
    f["demanda_com_patrocinador_sobre_montante"] = (
        (f["total_validado"] + f["total_indeferido"]) / f["montante_declarado"])
    return f


def composicao(h: pd.DataFrame) -> pd.DataFrame:
    ciclos = sorted(h["ciclo"].unique())
    por_ciclo = {c: set(h.loc[h["ciclo"] == c, "chave_proponente"]) for c in ciclos}
    linhas = []
    for c in ciclos:
        g = h[h["ciclo"] == c]
        props = por_ciclo[c]
        v1 = por_ciclo.get(c - 1)
        v2 = (por_ciclo.get(c - 1) or set()) | (por_ciclo.get(c - 2) or set()) if c - 2 in por_ciclo else None
        val = g.groupby("chave_proponente")["valor_autorizado"].sum()
        rm = g.dropna(subset=["rmgv"])
        linhas.append({
            "ciclo": c, "regime": REGIME[c], "habilitados": len(g), "proponentes": len(props),
            "pct_proponentes_em_t_1": len(props & v1) / len(props) if v1 is not None else np.nan,
            "pct_proponentes_em_t_1_ou_t_2": len(props & v2) / len(props) if v2 is not None else np.nan,
            "pct_valor_proponentes_em_t_1_ou_t_2": (val[val.index.isin(v2)].sum() / val.sum()
                                                    if v2 is not None else np.nan),
            "estreantes_janela_2": len(props - v2) if v2 is not None else np.nan,
            "pct_exatamente_500mil": (g["valor_autorizado"].dropna() == 500000).mean(),
            "cobertura_valor": f"{g['valor_autorizado'].notna().sum()}/{len(g)}",
            "pct_valor_rmgv_atribuivel": ((rm["valor_autorizado"] * rm["rmgv"]).sum() / rm["valor_autorizado"].sum()
                                          if len(rm) else np.nan),
            "cobertura_municipio": f"{len(rm)}/{len(g)}",
        })
    return pd.DataFrame(linhas)


def rouanet_es() -> pd.DataFrame:
    """Proponentes do ES no mecenato da Rouanet, por ano do PRONAC. Só agregados: o CPF/CNPJ do
    proponente é usado para contar recorrência e não é gravado."""
    reg, baixados, total_api = [], {}, {}
    for arq in sorted(glob.glob(str(RAIZ / "dados" / "externos" / "raw" / "salic" / "projetos_ano*.json"))):
        d = json.load(open(arq, encoding="utf-8"))
        aa = 2000 + int(Path(arq).name[len("projetos_ano"):][:2])
        baixados[aa] = baixados.get(aa, 0) + len(d.get("_embedded", {}).get("projetos", []))
        total_api[aa] = max(total_api.get(aa, 0), int(d.get("total") or 0))
        for p in d.get("_embedded", {}).get("projetos", []):
            if p.get("UF") == "ES" and p.get("mecanisnmo") == "Mecenato":
                reg.append({"ano": 2000 + int(p["ano_projeto"]), "pronac": p["PRONAC"], "prop": p.get("cgccpf"),
                            "municipio": _norm(p.get("municipio")), "captado": p.get("valor_captado")})
    r = pd.DataFrame(reg).drop_duplicates("pronac")
    mun = pd.read_csv(RAIZ / "dados" / "externos" / "municipios_es.csv")
    rm = set(mun.loc[mun["rmgv"], "chave"])
    r["rmgv"] = r["municipio"].isin(rm)
    anos = sorted(r["ano"].unique())
    por_ano = {a: set(r.loc[r["ano"] == a, "prop"].dropna()) for a in anos}
    linhas = []
    for a in anos:
        g = r[r["ano"] == a]
        props = por_ano[a]
        v2 = (por_ano.get(a - 1) or set()) | (por_ano.get(a - 2) or set()) if a - 2 in por_ano else None
        completo = baixados.get(a, 0) >= total_api.get(a, 0) > 0
        linhas.append({
            "ano_projeto": a, "download_completo": completo,
            "cobertura_download": f"{baixados.get(a, 0)}/{total_api.get(a, 0)} projetos do Brasil",
            "projetos": len(g), "proponentes": len(props),
            "pct_proponentes_em_t_1_ou_t_2": len(props & v2) / len(props) if v2 is not None and props else np.nan,
            "pct_projetos_com_captacao": (g["captado"].fillna(0) > 0).mean(),
            "pct_projetos_rmgv": g["rmgv"].mean(),
            "nota": "captação acumulada até a consulta (2026-09-23): anos recentes ainda captam",
        })
    return pd.DataFrame(linhas)


def mudanca_regime(comp: pd.DataFrame, rou: pd.DataFrame) -> pd.DataFrame:
    """Variação da recorrência (janela fixa t-1 ou t-2) de 2024 para 2025 e para a média 2025-2026.
    Descritivo: dois grupos, poucos períodos, sem erro-padrão confiável."""
    L = comp.set_index("ciclo")["pct_proponentes_em_t_1_ou_t_2"]
    # Ano com download incompleto do SALIC não entra (ausência não é zero; amostra parcial não é o ano).
    R = rou.set_index("ano_projeto")["pct_proponentes_em_t_1_ou_t_2"].where(
        rou.set_index("ano_projeto")["download_completo"])
    out = [{"serie": "LICC (habilitados)", "2024": L.get(2024), "2025": L.get(2025),
            "media_2025_2026": np.nanmean([L.get(2025, np.nan), L.get(2026, np.nan)])},
           {"serie": "Rouanet, proponentes do ES", "2024": R.get(2024), "2025": R.get(2025),
            "media_2025_2026": R.get(2025)}]
    df = pd.DataFrame(out)
    df["dif_2025_menos_2024"] = df["2025"] - df["2024"]
    df.loc[len(df)] = {"serie": "LICC menos Rouanet-ES (dif. em dif., pontos)",
                       "dif_2025_menos_2024": df.loc[0, "dif_2025_menos_2024"] - df.loc[1, "dif_2025_menos_2024"]}
    return df


def tabela_poder(fun: pd.DataFrame) -> pd.DataFrame:
    linhas = []
    res = fun[fun["ciclo"] <= 2024]
    n1, n0 = int(res["captou"].sum()), int(res["expirou"].sum())
    T = n1 / (n1 + n0)
    for p0 in (0.2, 0.4, 0.6):
        linhas.append({"hipotese": "H1/H2 adicionalidade", "desenho": "captou × expirou, 2022-2024 (observacional)",
                       "unidade": "projeto", "n_ou_J": n1 + n0, "m": np.nan, "icc": np.nan, "p0": p0,
                       "emd_pontos": poder.mde_binario(p0, n1 + n0, T=T),
                       "nota": f"{n1} captaram, {n0} expiraram; viés de seleção domina o erro amostral"})
    for n_braco in (20, 30):
        for p0 in (0.2, 0.4, 0.6):
            linhas.append({"hipotese": "H1 adicionalidade", "desenho": "racionamento pelo teto 2023-2024",
                           "unidade": "projeto", "n_ou_J": 2 * n_braco, "m": np.nan, "icc": np.nan, "p0": p0,
                           "emd_pontos": poder.mde_binario(p0, 2 * n_braco, T=0.5),
                           "nota": "termos indeferidos × validados pouco antes do esgotamento; n por braço hipotético"})
    for N in (1000, 2000, 4000):
        for p0 in (0.02, 0.05, 0.10):
            linhas.append({"hipotese": "H3 atrito", "desenho": "encorajamento aleatório individual",
                           "unidade": "agente cultural sem inscrição prévia", "n_ou_J": N, "m": np.nan,
                           "icc": np.nan, "p0": p0, "emd_pontos": poder.mde_binario(p0, N, T=0.5),
                           "nota": "N e p0 hipotéticos até contar os agentes do Mapa Cultural"})
    for m in (20, 50):
        for icc in (0.02, 0.05):
            for p0 in (0.05, 0.10):
                sig = (p0 * (1 - p0)) ** 0.5
                linhas.append({"hipotese": "H3 atrito", "desenho": "encorajamento aleatório por município (interior)",
                               "unidade": "município", "n_ou_J": 71, "m": m, "icc": icc, "p0": p0,
                               "emd_pontos": poder.mde_conglomerados(sig, 71, m, icc, P=0.5, gl=69),
                               "nota": "71 municípios fora da RMGV; m agentes por município hipotético"})
    return pd.DataFrame(linhas)


def _json_da_pagina(nome: str):
    """Corpo JSON de uma página coletada pelo relé (dados/fontes_web/paginas/<nome>.txt), ou None."""
    arq = RAIZ / "dados" / "fontes_web" / "paginas" / f"{nome}.txt"
    if not arq.exists():
        return None
    t = arq.read_text(encoding="utf-8")
    t = t[:t.rfind("## Links da página")] if "## Links da página" in t else t
    corpo = "\n".join(l for l in t.splitlines() if not l.startswith("#")).strip()  # tira o cabeçalho do relé
    try:
        return json.loads(corpo)
    except json.JSONDecodeError:
        return None


def mapa_cultural_universo() -> pd.DataFrame:
    """Contagens da API pública do Mapa Cultural ES (@count=1), coletadas pelo relé em 24/09/2026."""
    linhas = []
    for nome, recorte in [("mapa_api_agentes_contagem", "todos"),
                          ("mapa_api_agentes_contagem_individual", "individual (type=1)"),
                          ("mapa_api_agentes_contagem_coletivo", "coletivo (type=2)")]:
        v = _json_da_pagina(nome)
        linhas.append({"recorte": recorte, "agentes": v if isinstance(v, int) else np.nan,
                       "fonte": f"dados/fontes_web/paginas/{nome}.txt",
                       "nota": "cadastro não é elegibilidade: a inscrição na LICC exige CNPJ (IN 001/2025, art. 19)"})
    return pd.DataFrame(linhas)


def patrocinadores_na_rouanet() -> pd.DataFrame:
    """CNPJs que patrocinaram pela LICC em 2025 consultados no SALIC (/incentivadores?cgccpf=). total_doado é o
    acumulado de todos os anos; a série por ano exige o endpoint de doações (não coletado)."""
    a = pd.read_csv(RAIZ / "dados" / "processados" / "aportes_2025.csv", dtype={"cnpj_raiz": str})
    a["cnpj_num"] = a["cnpj"].str.replace(r"\D", "", regex=True)
    lic = a.groupby("cnpj_num").agg(patrocinador=("patrocinador_nome", "first"), cnpj_raiz=("cnpj_raiz", "first"),
                                     aportado_licc_2025=("valor", "sum")).reset_index()
    man = pd.read_csv(RAIZ / "dados" / "fontes_web" / "manifesto.csv")
    linhas = []
    for _, r in lic.iterrows():
        nome = f"salic_incentivador_{r['cnpj_num']}"
        st = man.loc[man["id"] == nome, "status"]
        j = _json_da_pagina(nome)
        inc = (j or {}).get("_embedded", {}).get("incentivadores", []) if isinstance(j, dict) else []
        linhas.append({"cnpj": r["cnpj_num"], "cnpj_raiz": r["cnpj_raiz"], "patrocinador": r["patrocinador"],
                       "aportado_licc_2025": r["aportado_licc_2025"],
                       "consultado_no_salic": nome in set(man["id"]),
                       "status_http": st.iloc[0] if len(st) else np.nan,
                       "incentivador_rouanet": bool(inc),
                       "total_doado_rouanet_acumulado": sum(i.get("total_doado") or 0 for i in inc) if inc else np.nan})
    return pd.DataFrame(linhas)


def main() -> None:
    h = carregar()
    fun = funil_por_ciclo(h)
    fun.to_csv(TAB / "07_funil_por_ciclo.csv", index=False)
    cap = funil_captacao_anual()
    cap.to_csv(TAB / "07_funil_captacao_anual.csv", index=False)
    comp = composicao(h)
    comp.to_csv(TAB / "07_composicao_por_ciclo.csv", index=False)
    rou = rouanet_es()
    rou.to_csv(TAB / "07_rouanet_es_composicao.csv", index=False)
    mud = mudanca_regime(comp, rou)
    mud.to_csv(TAB / "07_mudanca_regime.csv", index=False)
    pw = tabela_poder(fun)
    pw.to_csv(TAB / "07_poder_hipoteses.csv", index=False)
    mapa = mapa_cultural_universo()
    mapa.to_csv(TAB / "07_mapa_cultural_universo.csv", index=False)
    rou_pat = patrocinadores_na_rouanet()
    rou_pat.to_csv(TAB / "07_patrocinadores_na_rouanet.csv", index=False)
    with pd.option_context("display.width", 200, "display.max_columns", 20, "display.precision", 3):
        for nome, df in [("funil por ciclo", fun), ("captação anual", cap), ("composição", comp),
                         ("Rouanet-ES", rou), ("mudança de regime", mud)]:
            print(f"\n== {nome}\n{df.to_string(index=False)}")
        print("\n== Mapa Cultural\n" + mapa[["recorte", "agentes"]].to_string(index=False))
        emp = rou_pat.groupby("cnpj_raiz")["incentivador_rouanet"].any()
        print(f"\n== patrocinadores LICC 2025 no SALIC: {int(rou_pat['incentivador_rouanet'].sum())} de "
              f"{len(rou_pat)} CNPJs; {int(emp.sum())} de {len(emp)} empresas (raiz)")
        print("\n== poder\n" + pw.groupby(["desenho"])["emd_pontos"].agg(["min", "max"]).to_string())


if __name__ == "__main__":
    main()
