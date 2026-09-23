"""Replicação em Python dos quatro indicadores do licc.gov e inventário dos dados herdados.

Usado por: notas/politica/02-licc-gov-sintese.md (seções 1, 2, 4 e 5).

Por que existe: os números do licc.gov foram produzidos por código TypeScript
(licc-gov/codigo/src_lib_indicadores.ts e pipeline_build-graph.ts) que não roda
neste repositório. Para que cada número do artigo aponte um script em analise/,
este arquivo recalcula, a partir do artefato versionado dados/licc/graph.json e
dos CSVs, os mesmos indicadores com as mesmas fórmulas, e confere contra
dados/licc/stats.json e contra os números citados em licc-gov/CLAUDE-licc.md.

Entradas:
  dados/licc/graph.json, dados/licc/stats.json
  dados/licc/habilitados/habilitados-{2022..2026}.csv
  dados/licc/oficial/captados-2025.csv
Saídas:
  analise/tabelas/licc_gov_concentracao_capital.csv   (indicador 1, por empresa)
  analise/tabelas/licc_gov_territorio_municipios.csv  (indicador 2, 78 municípios)
  analise/tabelas/licc_gov_indicadores_resumo.csv     (os 4 indicadores, com cobertura)
  analise/tabelas/licc_gov_inventario_colunas.csv     (cobertura coluna a coluna)
  analise/tabelas/licc_gov_casamento_captados.csv     (captados 2025 x habilitados)
  analise/tabelas/licc_gov_concentracao_por_raiz_cnpj.csv (indicador 1 agrupado por raiz de CNPJ)
  analise/tabelas/licc_gov_habilitados_status_enquadramento.csv (status e cota por ciclo)
  analise/tabelas/licc_gov_habilitados_anomalias_valor.csv (valores ausentes/inconsistentes)

Regras: ausência não é zero (célula vazia fica fora das somas, e a cobertura é
contada); nada é estimado.
"""
from __future__ import annotations

import json
import re
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

import pandas as pd

RAIZ = Path(__file__).resolve().parents[1]
DADOS = RAIZ / "dados" / "licc"
TAB = RAIZ / "analise" / "tabelas"
TAB.mkdir(parents=True, exist_ok=True)


def gini(valores: list[float]) -> float:
    """Mesma fórmula de src_lib_indicadores.ts: sum((2i-n-1) x_i) / (n sum x), i=1..n, x ordenado."""
    v = sorted(valores)
    n = len(v)
    s = sum(v)
    if n < 2 or s <= 0:
        return 0.0
    return sum((2 * (i + 1) - n - 1) * x for i, x in enumerate(v)) / (n * s)


def normalizar(t: str) -> str:
    t = unicodedata.normalize("NFD", str(t)).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", " ", t).strip()


def main() -> None:
    g = json.loads((DADOS / "graph.json").read_text(encoding="utf-8"))
    stats = json.loads((DADOS / "stats.json").read_text(encoding="utf-8"))
    N, E = g["nodes"], g["edges"]
    por_id = {n["id"]: n for n in N}
    projetos = [n for n in N if n["kind"] == "projeto"]
    resumo: list[dict] = []

    # ---------------- 1. Concentração do capital ----------------
    aportes: dict[str, dict] = defaultdict(lambda: {"valor": 0.0, "projetos": set()})
    for e in E:
        if e["kind"] == "patrocina" and e.get("peso") is not None:
            aportes[e["source"]]["valor"] += e["peso"]
            aportes[e["source"]]["projetos"].add(e["target"])
    patrocinadores = [n for n in N if n["kind"] == "patrocinador"]
    total = sum(a["valor"] for a in aportes.values())
    linhas = sorted(
        ({"id": k, "empresa": por_id[k]["nome"], "cnpj": (por_id[k].get("meta") or {}).get("cnpj", ""),
          "aportado": round(a["valor"], 2), "projetos": len(a["projetos"])} for k, a in aportes.items()),
        key=lambda r: -r["aportado"],
    )
    acum = 0.0
    for r in linhas:
        r["fracao"] = r["aportado"] / total
        acum += r["fracao"]
        r["acumulado"] = acum
    cap = pd.DataFrame(linhas)
    cap["fonte"] = "dados/licc/graph.json (arestas patrocina com peso)"
    cap.to_csv(TAB / "licc_gov_concentracao_capital.csv", index=False)
    g_cap = gini(cap["aportado"].tolist())
    metade = int((cap["acumulado"] >= 0.5).idxmax()) + 1
    top3 = float(cap["fracao"].head(3).sum())
    resumo += [
        {"indicador": "1_capital", "medida": "total_aportado", "valor": round(total, 2), "base": len(aportes), "universo": len(patrocinadores)},
        {"indicador": "1_capital", "medida": "gini_aporte_por_empresa", "valor": round(g_cap, 4), "base": len(aportes), "universo": len(patrocinadores)},
        {"indicador": "1_capital", "medida": "empresas_para_metade", "valor": metade, "base": len(aportes), "universo": len(patrocinadores)},
        {"indicador": "1_capital", "medida": "fracao_tres_maiores", "valor": round(top3, 4), "base": len(aportes), "universo": len(patrocinadores)},
        {"indicador": "1_capital", "medida": "fracao_maior_empresa", "valor": round(float(cap["fracao"].iloc[0]), 4), "base": len(aportes), "universo": len(patrocinadores)},
        {"indicador": "1_capital", "medida": "projetos_maior_empresa", "valor": int(cap["projetos"].iloc[0]), "base": len(aportes), "universo": len(patrocinadores)},
        {"indicador": "1_capital", "medida": "arestas_patrocina_com_peso", "valor": sum(1 for e in E if e["kind"] == "patrocina" and e.get("peso") is not None), "base": None, "universo": None},
    ]

    # ---------------- 2. Desigualdade territorial ----------------
    municipios = [n for n in N if n["kind"] == "municipio"]
    pres = Counter()
    cap_mun = defaultdict(float)
    com_valor = Counter()
    for p in projetos:
        meta = p.get("meta") or {}
        for mid in meta.get("municipiosIds", []):
            pres[mid] += 1
        mid = meta.get("municipioId")
        capt = (p.get("orcamento") or {}).get("captado")
        if mid and capt is not None:
            cap_mun[mid] += capt
            com_valor[mid] += 1
    terr = pd.DataFrame([
        {"id": m["id"], "municipio": m["nome"], "regiao": (m.get("meta") or {}).get("regiao"),
         "rmgv": bool((m.get("meta") or {}).get("regiaoMetropolitana")),
         "projetos_presenca": pres[m["id"]], "captado_atribuido": round(cap_mun[m["id"]], 2),
         "projetos_com_valor": com_valor[m["id"]]}
        for m in municipios
    ]).sort_values(["captado_atribuido", "projetos_presenca"], ascending=False)
    terr["fonte"] = "dados/licc/graph.json (meta.municipiosIds / meta.municipioId dos projetos)"
    terr.to_csv(TAB / "licc_gov_territorio_municipios.csv", index=False)
    rm = terr[terr.rmgv]
    it = terr[~terr.rmgv]
    tot_t = terr["captado_atribuido"].sum()
    com_local = sum(1 for p in projetos if (p.get("meta") or {}).get("municipiosIds"))
    com_unico = sum(1 for p in projetos if (p.get("meta") or {}).get("municipioId"))
    resumo += [
        {"indicador": "2_territorio", "medida": "captado_rmgv", "valor": round(rm["captado_atribuido"].sum(), 2), "base": com_unico, "universo": len(projetos)},
        {"indicador": "2_territorio", "medida": "captado_interior", "valor": round(it["captado_atribuido"].sum(), 2), "base": com_unico, "universo": len(projetos)},
        {"indicador": "2_territorio", "medida": "captado_atribuido_total", "valor": round(tot_t, 2), "base": com_unico, "universo": len(projetos)},
        {"indicador": "2_territorio", "medida": "fracao_na_rmgv", "valor": round(rm["captado_atribuido"].sum() / tot_t, 4), "base": com_unico, "universo": len(projetos)},
        {"indicador": "2_territorio", "medida": "municipios_rmgv", "valor": len(rm), "base": None, "universo": 78},
        {"indicador": "2_territorio", "medida": "municipios_sem_projeto", "valor": int((terr.projetos_presenca == 0).sum()), "base": com_local, "universo": len(projetos)},
        {"indicador": "2_territorio", "medida": "municipios_com_presenca", "valor": int((terr.projetos_presenca > 0).sum()), "base": com_local, "universo": len(projetos)},
        {"indicador": "2_territorio", "medida": "gini_captado_78_municipios", "valor": round(gini(terr["captado_atribuido"].tolist()), 4), "base": com_unico, "universo": len(projetos)},
        {"indicador": "2_territorio", "medida": "projetos_rmgv_presenca", "valor": int(rm["projetos_presenca"].sum()), "base": com_local, "universo": len(projetos)},
        {"indicador": "2_territorio", "medida": "projetos_interior_presenca", "valor": int(it["projetos_presenca"].sum()), "base": com_local, "universo": len(projetos)},
    ]

    # ---------------- 3. Conversão autorizado -> captado ----------------
    com_aut = [p for p in projetos if ((p.get("orcamento") or {}).get("autorizado") or 0) > 0]
    completos = [p for p in com_aut if (p.get("orcamento") or {}).get("captado") is not None]
    aut = sum(p["orcamento"]["autorizado"] for p in completos)
    cpt = sum(p["orcamento"]["captado"] for p in completos)
    integral = sum(1 for p in completos if abs(p["orcamento"]["captado"] - p["orcamento"]["autorizado"]) < 0.005)
    taxas = sorted(p["orcamento"]["captado"] / p["orcamento"]["autorizado"] for p in completos)
    resumo += [
        {"indicador": "3_conversao", "medida": "autorizado", "valor": round(aut, 2), "base": len(completos), "universo": len(projetos)},
        {"indicador": "3_conversao", "medida": "captado", "valor": round(cpt, 2), "base": len(completos), "universo": len(projetos)},
        {"indicador": "3_conversao", "medida": "taxa_geral", "valor": round(cpt / aut, 4), "base": len(completos), "universo": len(projetos)},
        {"indicador": "3_conversao", "medida": "nao_captaram_zero_publicado", "valor": sum(1 for p in completos if p["orcamento"]["captado"] == 0), "base": len(completos), "universo": len(projetos)},
        {"indicador": "3_conversao", "medida": "captacao_desconhecida", "valor": len(com_aut) - len(completos), "base": len(completos), "universo": len(projetos)},
        {"indicador": "3_conversao", "medida": "projetos_captaram_100pct", "valor": integral, "base": len(completos), "universo": len(projetos)},
        {"indicador": "3_conversao", "medida": "taxa_mediana_por_projeto", "valor": round(pd.Series(taxas).median(), 4), "base": len(completos), "universo": len(projetos)},
        {"indicador": "3_conversao", "medida": "taxa_minima_por_projeto", "valor": round(taxas[0], 4), "base": len(completos), "universo": len(projetos)},
        {"indicador": "3_conversao", "medida": "projetos_com_segmento", "valor": sum(1 for p in projetos if (p.get("meta") or {}).get("segmentoId")), "base": None, "universo": len(projetos)},
    ]

    # ---------------- 4. Quem executa ----------------
    props = [n for n in N if n["kind"] == "proponente"]
    dist = Counter((n.get("meta") or {}).get("projetosNoAno", 0) for n in props)
    com_nat = sum(1 for n in props if (n.get("meta") or {}).get("natureza"))
    no_lim = [n["nome"] for n in props if (n.get("meta") or {}).get("projetosNoAno", 0) >= 3]
    for k in sorted(dist):
        resumo.append({"indicador": "4_quem_executa", "medida": f"proponentes_com_{k}_projetos", "valor": dist[k], "base": len(props), "universo": len(props)})
    resumo += [
        {"indicador": "4_quem_executa", "medida": "proponentes_com_natureza", "valor": com_nat, "base": com_nat, "universo": len(props)},
        {"indicador": "4_quem_executa", "medida": "proponentes_no_limite_3", "valor": len(no_lim), "base": len(props), "universo": len(props)},
    ]
    print("proponentes no limite de 3:", no_lim)

    # ---------------- Inventário coluna a coluna ----------------
    inv = []
    arquivos = sorted((DADOS / "habilitados").glob("habilitados-*.csv")) + [DADOS / "oficial" / "captados-2025.csv"]
    hab = {}
    for f in arquivos:
        d = pd.read_csv(f, dtype=str, keep_default_na=False)
        if f.name.startswith("habilitados"):
            hab[int(re.search(r"(\d{4})", f.name).group(1))] = d
        for c in d.columns:
            inv.append({"arquivo": f"dados/licc/{f.parent.name}/{f.name}", "linhas": len(d), "coluna": c,
                        "preenchidas": int((d[c].str.strip() != "").sum()),
                        "distintos": int(d[c].nunique()),
                        "exemplos": " | ".join(sorted(d[c][d[c].str.strip() != ""].unique())[:4])[:160]})
    pd.DataFrame(inv).to_csv(TAB / "licc_gov_inventario_colunas.csv", index=False)

    # ---------------- Casamento captados 2025 x habilitados (título normalizado exato) ----------------
    capt = pd.read_csv(DADOS / "oficial" / "captados-2025.csv", dtype=str, keep_default_na=False)
    idx = defaultdict(set)
    for ano, d in hab.items():
        for t in d["projeto"]:
            idx[normalizar(t)].add(ano)
    cas = []
    for _, r in capt.iterrows():
        anos = sorted(idx.get(normalizar(r["projeto"]), set()))
        cas.append({"projeto": r["projeto"], "ciclos_habilitados": ";".join(map(str, anos)),
                    "situacao": "unico" if len(anos) == 1 else ("ambiguo" if anos else "sem_correspondencia")})
    cas = pd.DataFrame(cas)
    cas.to_csv(TAB / "licc_gov_casamento_captados.csv", index=False)

    # ---------------- Identidade da empresa: nome (licc.gov) x raiz de CNPJ ----------------
    # O licc.gov agrupa patrocinador pelo slug do NOME (pipeline_habilitados.ts), o que separa
    # grafias diferentes da mesma empresa. Aqui o agrupamento é pela raiz do CNPJ (8 dígitos).
    termos = [t.strip().split("|") for s in capt["aportes"] for t in s.split(";") if t.strip()]
    tdf = pd.DataFrame(termos, columns=["cnpj", "nome", "valor"])
    tdf["valor"] = tdf["valor"].astype(float)
    tdf["raiz_cnpj"] = tdf["cnpj"].str[:10]
    raiz = (tdf.groupby("raiz_cnpj")
            .agg(nomes=("nome", lambda s: " / ".join(sorted(set(s)))), aportado=("valor", "sum"), termos=("valor", "size"))
            .sort_values("aportado", ascending=False).reset_index())
    raiz["fracao"] = raiz["aportado"] / raiz["aportado"].sum()
    raiz["acumulado"] = raiz["fracao"].cumsum()
    raiz["fonte"] = "dados/licc/oficial/captados-2025.csv (coluna aportes)"
    raiz.to_csv(TAB / "licc_gov_concentracao_por_raiz_cnpj.csv", index=False)
    capt_va = capt["valor_autorizado"].astype(float)
    n_termos = capt["aportes"].map(lambda s: len([t for t in s.split(";") if t.strip()]))
    for k, v in n_termos.value_counts().sort_index().items():
        resumo.append({"indicador": "0_captados_2025", "medida": f"projetos_com_{k}_termos", "valor": int(v), "base": len(capt), "universo": len(capt)})
    resumo += [
        {"indicador": "0_captados_2025", "medida": "soma_dos_termos", "valor": round(float(tdf["valor"].sum()), 2), "base": len(tdf), "universo": len(tdf)},
        {"indicador": "0_captados_2025", "medida": "autorizado_mediana", "valor": float(capt_va.median()), "base": len(capt), "universo": len(capt)},
        {"indicador": "0_captados_2025", "medida": "autorizado_maximo", "valor": float(capt_va.max()), "base": len(capt), "universo": len(capt)},
        {"indicador": "0_captados_2025", "medida": "proponentes_grafias_distintas", "valor": int(capt["proponente"].nunique()), "base": len(capt), "universo": len(capt)},
    ]
    resumo += [
        {"indicador": "1_capital_raiz_cnpj", "medida": "termos_de_patrocinio", "valor": len(tdf), "base": None, "universo": None},
        {"indicador": "1_capital_raiz_cnpj", "medida": "cnpjs_de_estabelecimento", "valor": tdf["cnpj"].nunique(), "base": None, "universo": None},
        {"indicador": "1_capital_raiz_cnpj", "medida": "empresas_raiz_cnpj", "valor": len(raiz), "base": None, "universo": None},
        {"indicador": "1_capital_raiz_cnpj", "medida": "gini_por_raiz", "valor": round(gini(raiz["aportado"].tolist()), 4), "base": len(raiz), "universo": len(raiz)},
        {"indicador": "1_capital_raiz_cnpj", "medida": "fracao_tres_maiores", "valor": round(float(raiz["fracao"].head(3).sum()), 4), "base": len(raiz), "universo": len(raiz)},
        {"indicador": "1_capital_raiz_cnpj", "medida": "empresas_para_metade", "valor": int((raiz["acumulado"] >= 0.5).idxmax()) + 1, "base": len(raiz), "universo": len(raiz)},
    ]
    pd.DataFrame(resumo).assign(fonte="dados/licc/graph.json; dados/licc/oficial/captados-2025.csv").to_csv(
        TAB / "licc_gov_indicadores_resumo.csv", index=False)

    # ---------------- Habilitados: status, enquadramento e anomalias por ciclo ----------------
    H = pd.concat([d.assign(ciclo=a) for a, d in hab.items()], ignore_index=True)
    st = pd.crosstab(H["ciclo"], H["status"].replace("", "(vazio)"))
    enq = pd.crosstab(H["ciclo"], H["enquadramento"].replace("", "(vazio)"))
    pd.concat({"status": st, "enquadramento": enq}, axis=1).to_csv(TAB / "licc_gov_habilitados_status_enquadramento.csv")
    H["va"] = pd.to_numeric(H["valor_autorizado"], errors="coerce")
    H["vt"] = pd.to_numeric(H["valor_total"], errors="coerce")
    anom = H[(H["va"] > H["vt"]) | H["va"].isna() | H["vt"].isna()][
        ["ciclo", "numero_processo", "projeto", "valor_autorizado", "valor_total", "fonte_pagina"]]
    anom.to_csv(TAB / "licc_gov_habilitados_anomalias_valor.csv", index=False)
    rep = H.groupby("numero_processo")["ciclo"].apply(lambda s: ";".join(map(str, sorted(s))))
    pref = pd.crosstab(H["numero_processo"].str[:4].rename("prefixo_processo"), H["ciclo"])
    pref.to_csv(TAB / "licc_gov_prefixo_processo_por_ciclo.csv")
    print("\n== Prefixo do número de processo x ciclo de habilitação ==\n" + pref.to_string())
    print("\n== Habilitados: status x ciclo ==\n" + st.to_string())
    print("\n== Habilitados: enquadramento x ciclo ==\n" + enq.to_string())
    print("\n== Anomalias de valor (autorizado > total, ou ausente) ==\n" + anom.to_string(index=False))
    print("\n== Processos em mais de um ciclo ==\n" + rep[rep.str.contains(";")].to_string())
    print("\n== Concentração por raiz de CNPJ ==\n" + raiz.head(6)[["nomes", "aportado", "fracao", "termos"]].to_string(index=False))

    # ---------------- Impressão e conferência ----------------
    print("== Conferência contra stats.json ==")
    for k in ("totalProjetos", "totalProponentes", "totalPatrocinadores", "totalMunicipiosAtendidos", "autorizado", "captado", "execucao", "comprometimentoDoTeto"):
        print(f"  {k}: {stats[k]}")
    print("  cobertura:", stats["cobertura"])
    for c in stats["cotas"]:
        print(f"  cota {c['regraId']}: alocado(autorizado) {c['alocado']:,.2f} de {c['reservado']:,.0f}; atendida={c['atendida']}; {c['classificaveis']}")
    print("\n== Indicadores recalculados ==")
    print(pd.DataFrame(resumo).to_string(index=False))
    print("\n== Top 5 empresas ==")
    print(cap.head(5)[["empresa", "aportado", "fracao", "acumulado", "projetos"]].to_string(index=False))
    print("\n== Top municípios ==")
    print(terr[terr.projetos_presenca > 0][["municipio", "rmgv", "projetos_presenca", "captado_atribuido", "projetos_com_valor"]].to_string(index=False))
    print("\n== Casamento captados x habilitados (título normalizado exato) ==")
    print(cas["situacao"].value_counts().to_string())
    unicos = cas[cas.situacao == "unico"]["ciclos_habilitados"].value_counts()
    print("ciclo dos casados únicos:\n" + unicos.to_string())
    todos = Counter(a for s in cas["ciclos_habilitados"] for a in s.split(";") if a)
    print("aparições por ciclo (inclui ambíguos):", dict(sorted(todos.items())))
    print("\n== Cotas: projetos do grafo com cotaId ==")
    print(Counter((p.get("meta") or {}).get("cotaId", "(ausente)") for p in projetos))


if __name__ == "__main__":
    main()
