"""
14 — Dados públicos sem LAI: perfil dos patrocinadores (Receita Federal), área de atuação dos proponentes e rastro
de entrega no Mapa Cultural.

Fontes (coletadas pelo relé, analise/rede/consultas_publicas.py):
  dados/externos/cnpj_patrocinadores.csv       CNPJ dos patrocinadores (BrasilAPI): porte, natureza, CNAE, sede,
                                               capital social, abertura, Simples. Um CNPJ por estabelecimento.
  dados/externos/mapa_agentes_proponentes.csv  agentes do Mapa cujo nome casa exatamente com um proponente
  dados/externos/mapa_eventos_licc.csv         eventos do Mapa cujo nome, ou o do projeto, casa com um título da LICC
  dados/externos/mapa_projetos_licc.csv        projetos do Mapa cujo nome casa com um título da LICC
Valores por termo: anexos "Recurso financeiro captado" (artigo/auditoria/auditar_captacao.py, ler_anexo).

Regras: casamento só por nome normalizado exato (nunca semelhança); cobertura declarada em cada tabela; o que não
casa fica ausente. Evento só conta como rastro de entrega se tiver ocorrência a partir do ano do ciclo do projeto
(títulos de eventos recorrentes se repetem entre anos).

Saídas (analise/tabelas/):
  14_patrocinadores_perfil.csv      um CNPJ de patrocinador por linha, com o valor validado por ano
  14_patrocinadores_resumo.csv      renúncia por porte, natureza jurídica, atividade (CNAE, divisão) e sede
  14_proponentes_mapa_area.csv      proponentes cadastrados no Mapa por área de atuação, com projetos e valor
  14_entrega_mapa.csv               projetos da LICC com evento datado na agenda do Mapa, por situação oficial
Uso: python analise/14_dados_publicos.py
"""
from __future__ import annotations

import importlib.util
import sys
from decimal import Decimal
from pathlib import Path

import pandas as pd

RAIZ = Path(__file__).resolve().parents[1]
EXT = RAIZ / "dados" / "externos"
PROC = RAIZ / "dados" / "processados"
TAB = RAIZ / "analise" / "tabelas"
sys.path.insert(0, str(RAIZ / "analise"))


def _modulo(nome: str, caminho: Path):
    spec = importlib.util.spec_from_file_location(nome, caminho)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


aud = _modulo("aud", RAIZ / "artigo" / "auditoria" / "auditar_captacao.py")
carregar = _modulo("carregar", RAIZ / "analise" / "01_carregar.py")

RMGV = {"VITORIA", "VILA VELHA", "SERRA", "CARIACICA", "VIANA", "GUARAPARI", "FUNDAO"}
# divisões da CNAE 2.0 que aparecem entre os patrocinadores (as demais ficam com o código)
DIVISAO = {"35": "eletricidade e gás", "47": "comércio varejista", "46": "comércio atacadista",
           "45": "comércio e reparação de veículos", "24": "metalurgia", "11": "bebidas", "10": "alimentos",
           "49": "transporte terrestre", "52": "armazenagem e apoio ao transporte", "61": "telecomunicações",
           "23": "minerais não metálicos", "08": "extração de minerais não metálicos", "17": "celulose e papel",
           "06": "extração de petróleo e gás", "64": "serviços financeiros", "41": "construção de edifícios"}


def termos_por_cnpj() -> pd.DataFrame:
    man = aud.manifesto()
    linhas = []
    for ano, pid in aud.ANEXOS.items():
        for t in aud.ler_anexo(ano, pid, man)["termos"]:
            linhas.append({"ano": ano, "cnpj": t["cnpj"], "valor": float(t["valor"])})
    return pd.DataFrame(linhas)


def patrocinadores() -> tuple[pd.DataFrame, pd.DataFrame]:
    c = pd.read_csv(EXT / "cnpj_patrocinadores.csv", dtype=str)
    t = termos_por_cnpj()
    val = t.pivot_table(index="cnpj", columns="ano", values="valor", aggfunc="sum").fillna(0.0)
    val.columns = [f"validado_{a}" for a in val.columns]
    val["validado_total"] = val.sum(axis=1)
    val["termos"] = t.groupby("cnpj").size()
    p = c.merge(val, left_on="cnpj", right_index=True, how="left")
    p["papel"] = p["validado_total"].notna().map({True: "patrocinador em termo validado", False: "CNPJ no anexo sem termo validado lido"})
    p["cnpj_raiz"] = p["cnpj"].str[:8]
    p["divisao_cnae"] = p["cnae_fiscal"].str.zfill(7).str[:2]
    p["atividade"] = p["divisao_cnae"].map(DIVISAO).fillna("divisão " + p["divisao_cnae"])
    p["sede"] = p.apply(lambda r: "fora do ES" if r["uf"] != "ES" else ("RMGV" if str(r["municipio"]).upper() in RMGV else "interior do ES"), axis=1)
    p["capital_social"] = pd.to_numeric(p["capital_social"], errors="coerce")
    p["anos_de_abertura"] = (pd.Timestamp("2026-01-01") - pd.to_datetime(p["data_inicio_atividade"], errors="coerce")).dt.days / 365.25
    p["simples_hoje"] = p["opcao_pelo_simples"].map({"True": "sim", "False": "não"}).fillna("não informado")
    total = p["validado_total"].sum()
    resumo = []
    for dim in ("porte", "natureza_juridica", "atividade", "sede", "simples_hoje"):
        g = p[p["validado_total"] > 0].groupby(dim).agg(estabelecimentos=("cnpj", "size"),
                                                       grupos_cnpj_raiz=("cnpj_raiz", "nunique"),
                                                       validado=("validado_total", "sum"))
        g["pct_validado"] = g["validado"] / total
        for k, r in g.sort_values("validado", ascending=False).iterrows():
            resumo.append({"dimensao": dim, "categoria": k, **r.to_dict()})
    # capital social: parcela da renúncia de empresas com capital acima de faixas
    com = p[(p["validado_total"] > 0) & p["capital_social"].notna()]
    for faixa in (1e6, 10e6, 100e6, 1e9):
        resumo.append({"dimensao": "capital_social", "categoria": f">= R$ {faixa:,.0f}".replace(",", "."),
                       "estabelecimentos": int((com["capital_social"] >= faixa).sum()),
                       "grupos_cnpj_raiz": com.loc[com["capital_social"] >= faixa, "cnpj_raiz"].nunique(),
                       "validado": com.loc[com["capital_social"] >= faixa, "validado_total"].sum(),
                       "pct_validado": com.loc[com["capital_social"] >= faixa, "validado_total"].sum() / total})
    r = pd.DataFrame(resumo)
    r["cobertura"] = f"{int((p['validado_total'] > 0).sum())} estabelecimentos com termo validado 2022-2026; soma {total:,.2f}"
    r["fonte"] = "dados/externos/cnpj_patrocinadores.csv (BrasilAPI); anexos de captação (auditar_captacao.ler_anexo)"
    return p, r


def proponentes_mapa() -> pd.DataFrame:
    a = pd.read_csv(EXT / "mapa_agentes_proponentes.csv")
    h = pd.read_csv(PROC / "habilitados.csv").drop_duplicates("numero_processo")
    h["chave"] = h["proponente"].map(carregar.chave_proponente)
    chaves = h["chave"].nunique()
    # um proponente pode ter mais de um agente com o mesmo nome: as áreas se somam, sem repetir
    areas = (a.assign(area=a["area_atuacao"].fillna("").str.split("; ")).explode("area")
             .query("area != ''")[["chave", "area"]].drop_duplicates())
    casadas = set(a["chave"])
    por_prop = h[h["chave"].isin(casadas)].groupby("chave").agg(projetos=("numero_processo", "size"),
                                                                autorizado=("valor_autorizado", "sum"))
    t = areas.merge(por_prop, left_on="chave", right_index=True)
    out = t.groupby("area").agg(proponentes=("chave", "nunique"), projetos=("projetos", "sum"),
                                autorizado=("autorizado", "sum")).sort_values("proponentes", ascending=False)
    out["pct_proponentes_casados"] = out["proponentes"] / len(casadas)
    out["cobertura"] = f"{len(casadas)} de {chaves} proponentes com agente no Mapa de mesmo nome"
    tipo = a.drop_duplicates("chave")["tipo"].value_counts().to_dict()
    mun = a.drop_duplicates("chave")["municipio"].fillna("não informado")
    rmgv = mun.str.upper().map(lambda m: "RMGV" if carregar.normalizar(m).upper() in RMGV else m).value_counts()
    out["nota"] = (f"tipo do agente: {tipo}; sede informada na RMGV: {int(rmgv.get('RMGV', 0))} de {len(mun)}; "
                   "área de atuação é autodeclarada no cadastro, não é a linha de financiamento do projeto")
    return out.reset_index()


def entrega_mapa() -> pd.DataFrame:
    e = pd.read_csv(EXT / "mapa_eventos_licc.csv")
    h = pd.read_csv(PROC / "habilitados.csv").drop_duplicates("numero_processo")
    e["ano_ocorrencia"] = pd.to_datetime(e["ultima_data"], errors="coerce").dt.year
    e = e.merge(h[["numero_processo", "ciclo", "status"]], on="numero_processo", how="left")
    valido = e[e["ano_ocorrencia"] >= e["ciclo"]]
    com_evento = set(valido["numero_processo"])
    linhas = []
    for st, g in h.groupby("status"):
        linhas.append({"situacao_oficial": st, "projetos": len(g),
                       "com_evento_datado_no_mapa": int(g["numero_processo"].isin(com_evento).sum())})
    out = pd.DataFrame(linhas)
    out["pct"] = out["com_evento_datado_no_mapa"] / out["projetos"]
    out["cobertura"] = (f"{len(com_evento)} projetos com evento cujo nome casa com o título e ocorre a partir do ano do "
                        f"ciclo; {e['numero_processo'].nunique()} com algum evento de mesmo nome")
    return out


def main() -> None:
    p, r = patrocinadores()
    p.to_csv(TAB / "14_patrocinadores_perfil.csv", index=False)
    r.to_csv(TAB / "14_patrocinadores_resumo.csv", index=False)
    print(r[["dimensao", "categoria", "estabelecimentos", "grupos_cnpj_raiz", "validado", "pct_validado"]].to_string(index=False))
    a = proponentes_mapa()
    a.to_csv(TAB / "14_proponentes_mapa_area.csv", index=False)
    print(a.head(15).to_string(index=False))
    print(a["cobertura"].iat[0], "|", a["nota"].iat[0])
    ent = entrega_mapa()
    ent.to_csv(TAB / "14_entrega_mapa.csv", index=False)
    print(ent.to_string(index=False))


if __name__ == "__main__":
    main()
