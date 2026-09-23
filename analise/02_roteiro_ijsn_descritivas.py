"""Descritivas de apoio ao "Roteiro IJSN aplicado à LICC".

Usado por: notas/disciplina/02-ijsn-simapp.md (seção "Roteiro IJSN aplicado à LICC").

Entradas (transcrição oficial dos anexos da SECULT, herdada do licc.gov):
  dados/licc/habilitados/habilitados-{2022..2026}.csv
  dados/licc/oficial/captados-2025.csv
Saídas:
  analise/tabelas/02_roteiro_ijsn_habilitados_por_ciclo.csv
  analise/tabelas/02_roteiro_ijsn_captados_2025.csv
  (e um resumo impresso no terminal)

Regras (CLAUDE.md do projeto):
  - Ausência não é zero: célula vazia fica fora das somas e a cobertura é contada.
  - Território: um projeto só é classificado se TODOS os municípios listados
    forem resolvidos contra a lista de 78 municípios do ES; do contrário,
    "indeterminado". A coluna `municipio` do anexo não diz se é sede do agente
    ou local de execução, então esta classificação NÃO apura a cota do art. 18,
    III, da IN 001/2025 (que exige as duas coisas fora da RMGV).
"""
from __future__ import annotations

import re
import unicodedata
from pathlib import Path

import pandas as pd

RAIZ = Path(__file__).resolve().parents[1]
HAB = RAIZ / "dados" / "licc" / "habilitados"
CAP = RAIZ / "dados" / "licc" / "oficial" / "captados-2025.csv"
TAB = RAIZ / "analise" / "tabelas"
TAB.mkdir(parents=True, exist_ok=True)

# RMGV e municípios do ES: licc-gov/codigo/src_ontology_municipios.ts
RMGV = ["Cariacica", "Fundão", "Guarapari", "Serra", "Viana", "Vila Velha", "Vitória"]
INTERIOR = [
    "Itaguaçu", "Itarana", "Santa Leopoldina", "Santa Maria de Jetibá", "Santa Teresa",
    "Afonso Cláudio", "Brejetuba", "Conceição do Castelo", "Domingos Martins",
    "Laranja da Terra", "Marechal Floriano", "Venda Nova do Imigrante",
    "Alfredo Chaves", "Anchieta", "Iconha", "Itapemirim", "Marataízes", "Piúma",
    "Presidente Kennedy", "Rio Novo do Sul",
    "Atílio Vivácqua", "Cachoeiro de Itapemirim", "Castelo", "Jerônimo Monteiro",
    "Mimoso do Sul", "Muqui", "Vargem Alta",
    "Alegre", "Apiacá", "Bom Jesus do Norte", "Divino de São Lourenço",
    "Dores do Rio Preto", "Guaçuí", "Ibatiba", "Ibitirama", "Irupi", "Iúna",
    "Muniz Freire", "São José do Calçado",
    "Aracruz", "Baixo Guandu", "Colatina", "Governador Lindenberg", "Ibiraçu",
    "João Neiva", "Linhares", "Marilândia", "Rio Bananal", "São Roque do Canaã",
    "Sooretama",
    "Água Doce do Norte", "Águia Branca", "Alto Rio Novo", "Mantenópolis", "Pancas",
    "São Domingos do Norte", "São Gabriel da Palha",
    "Boa Esperança", "Conceição da Barra", "Jaguaré", "Montanha", "Mucurici",
    "Pedro Canário", "Pinheiros", "Ponto Belo", "São Mateus",
    "Barra de São Francisco", "Ecoporanga", "Nova Venécia", "Vila Pavão", "Vila Valério",
]
assert len(RMGV) + len(INTERIOR) == 78


def chave(txt: str) -> str:
    t = unicodedata.normalize("NFKD", str(txt)).encode("ascii", "ignore").decode()
    return re.sub(r"\s+", " ", t).strip().lower()


K_RMGV = {chave(m) for m in RMGV}
K_INT = {chave(m) for m in INTERIOR}


def municipios(celula) -> list[str]:
    if pd.isna(celula) or not str(celula).strip():
        return []
    partes = [p.strip() for p in str(celula).split(";")]
    return [re.sub(r"^munic[ií]pio\s+(de\s+)?", "", p, flags=re.I).strip() for p in partes if p]


def classe_territorial(celula) -> str:
    ms = municipios(celula)
    if not ms:
        return "sem_municipio"
    ks = [chave(m) for m in ms]
    if any(k not in K_RMGV and k not in K_INT for k in ks):
        return "indeterminado"
    em_rmgv = [k in K_RMGV for k in ks]
    if all(em_rmgv):
        return "so_rmgv"
    if not any(em_rmgv):
        return "so_interior"
    return "misto"


nao_resolvidos: set[str] = set()
linhas = []
for f in sorted(HAB.glob("habilitados-*.csv")):
    ciclo = int(re.search(r"(\d{4})", f.name).group(1))
    d = pd.read_csv(f)
    for c in d["municipio"].dropna():
        for m in municipios(c):
            if chave(m) not in K_RMGV and chave(m) not in K_INT:
                nao_resolvidos.add(m)
    va = pd.to_numeric(d["valor_autorizado"], errors="coerce")
    terr = d["municipio"].map(classe_territorial).value_counts()
    st = d["status"].fillna("sem_dado").value_counts()
    enq = d["enquadramento"].fillna("sem_dado").value_counts()
    distintos = {
        chave(m) for c in d["municipio"].dropna() for m in municipios(c)
        if chave(m) in K_RMGV or chave(m) in K_INT
    }
    linhas.append({
        "ciclo_habilitacao": ciclo,
        "n_projetos": len(d),
        "n_proponentes_distintos_nome": d["proponente"].map(chave).nunique(),
        "n_com_valor_autorizado": int(va.notna().sum()),
        "valor_autorizado_soma": round(float(va.sum(skipna=True)), 2),
        "valor_autorizado_mediana": round(float(va.median(skipna=True)), 2),
        "n_valor_autorizado_igual_500mil": int((va == 500000).sum()),
        "n_valor_autorizado_acima_500mil": int((va > 500000).sum()),
        "n_com_municipio": int(d["municipio"].notna().sum()),
        "n_municipios_distintos_resolvidos": len(distintos),
        "terr_so_rmgv": int(terr.get("so_rmgv", 0)),
        "terr_so_interior": int(terr.get("so_interior", 0)),
        "terr_misto": int(terr.get("misto", 0)),
        "terr_indeterminado": int(terr.get("indeterminado", 0)),
        "terr_sem_municipio": int(terr.get("sem_municipio", 0)),
        "status_concluido": int(st.get("concluido", 0)),
        "status_em_execucao": int(st.get("em_execucao", 0)),
        "status_captando": int(st.get("captando", 0)),
        "status_captacao_expirada": int(st.get("captacao_expirada", 0)),
        "status_sem_dado": int(st.get("sem_dado", 0)),
        "enq_cota_pautados": int(enq.get("cota-pautados", 0)),
        "enq_cota_continuados": int(enq.get("cota-continuados", 0)),
        "enq_cota_fora_rmgv": int(enq.get("cota-fora-rmgv", 0)),
        "enq_cota_demais": int(enq.get("cota-demais", 0)),
        "enq_sem_dado": int(enq.get("sem_dado", 0)),
    })

hab = pd.DataFrame(linhas).sort_values("ciclo_habilitacao")
hab.to_csv(TAB / "02_roteiro_ijsn_habilitados_por_ciclo.csv", index=False)

# ---------------------------------------------------------------- captados 2025
c = pd.read_csv(CAP)
aut = pd.to_numeric(c["valor_autorizado"], errors="coerce")
cap = pd.to_numeric(c["valor_captado"], errors="coerce")

aportes = []
for _, r in c.iterrows():
    if pd.isna(r["aportes"]):
        continue
    for termo in str(r["aportes"]).split(";"):
        partes = [p.strip() for p in termo.split("|")]
        if len(partes) != 3 or not partes[2]:
            continue
        cnpj = re.sub(r"\D", "", partes[0])
        aportes.append({"projeto": r["projeto"], "cnpj": cnpj, "raiz": cnpj[:8],
                        "nome": partes[1], "valor": float(partes[2])})
ap = pd.DataFrame(aportes)
soma_ap_proj = ap.groupby("projeto")["valor"].sum()
dif = (soma_ap_proj.reindex(c["projeto"]).values - cap.values)
por_raiz = ap.groupby("raiz")["valor"].sum().sort_values(ascending=False)
part = por_raiz / por_raiz.sum()

resumo_cap = {
    "n_projetos": len(c),
    "n_proponentes_distintos_nome": c["proponente"].map(chave).nunique(),
    "valor_autorizado_soma": round(float(aut.sum()), 2),
    "valor_captado_soma": round(float(cap.sum()), 2),
    "n_captado_igual_autorizado": int((abs(cap - aut) < 0.005).sum()),
    "n_captado_menor_autorizado": int((cap < aut - 0.005).sum()),
    "razao_captado_autorizado_mediana": round(float((cap / aut).median()), 4),
    "n_termos_patrocinio": len(ap),
    "n_cnpj_estabelecimento": ap["cnpj"].nunique(),
    "n_cnpj_raiz_empresas": ap["raiz"].nunique(),
    "participacao_maior_empresa": round(float(part.iloc[0]), 4),
    "participacao_5_maiores_empresas": round(float(part.iloc[:5].sum()), 4),
    "hhi_empresas_0a10000": round(float((part ** 2).sum() * 10000), 1),
    "n_projetos_soma_aportes_difere_captado": int((abs(dif) > 0.005).sum()),
}
pd.DataFrame([resumo_cap]).to_csv(TAB / "02_roteiro_ijsn_captados_2025.csv", index=False)

# ------------------------------------------- EMD ilustrativo (IJSN vol. 4, p. 93)
# EMD = (t_{1-k} + t_a) * sqrt(1/(P(1-P))) * sqrt(sigma^2/N), em desvios-padrão
# (sigma = 1). Valores de referência do Boxe P: t_0,8 = 0,84 e t_0,05 = 1,96.
# "Tratado" = habilitado com status concluido ou em_execucao; "comparação" =
# captacao_expirada; "captando" fica fora (desfecho ainda aberto). A fórmula
# supõe atribuição aleatória e unidades independentes: aqui é só a ordem de
# grandeza do que a população de habilitados permitiria detectar.
T_PODER, T_ALFA = 0.84, 1.96
emd_linhas = []
for rotulo, anos in [("2022", [2022]), ("2023", [2023]), ("2024", [2024]),
                     ("2022-2024", [2022, 2023, 2024])]:
    h = hab[hab["ciclo_habilitacao"].isin(anos)]
    nt = int(h["status_concluido"].sum() + h["status_em_execucao"].sum())
    nc = int(h["status_captacao_expirada"].sum())
    n = nt + nc
    p = nt / n
    emd = (T_PODER + T_ALFA) * (1 / (p * (1 - p))) ** 0.5 * (1 / n) ** 0.5
    emd_linhas.append({"ciclos": rotulo, "n_tratados": nt, "n_comparacao": nc,
                       "N": n, "P": round(p, 4), "EMD_desvios_padrao": round(emd, 3)})
emd_df = pd.DataFrame(emd_linhas)
emd_df.to_csv(TAB / "02_roteiro_ijsn_emd_ilustrativo.csv", index=False)

pd.set_option("display.width", 200)
print(emd_df.to_string(index=False))
print()
print(hab.T.to_string())
print()
for k, v in resumo_cap.items():
    print(f"{k}: {v}")
print("\nmaior empresa (raiz CNPJ):", por_raiz.index[0],
      ap.loc[ap["raiz"] == por_raiz.index[0], "nome"].iloc[0])
print("municípios não resolvidos (entram como 'indeterminado'):", sorted(nao_resolvidos))
