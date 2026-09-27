"""
17 — Quem capta na LICC: perfil dos proponentes na Receita Federal (CNPJ das listas do Portal da Transparência).

Fontes:
  dados/processados/transparencia_licc_termos.csv  termos de 2022-2025 com CNPJ do proponente (analise/16_transparencia_licc.py)
  dados/externos/cnpj_proponentes.csv              Receita Federal via BrasilAPI/minhareceita.org, consultada pelo relé
                                                   (analise/rede/consultas_publicas.py); porte, natureza, CNAE, município,
                                                   abertura, Simples e MEI são os de HOJE, não os do ano da captação
  dados/externos/cnpj_patrocinadores.csv           sede do patrocinador, para comparar com a do proponente

Regras: só CNPJ com dígito verificador válido; sem resposta da Receita fica ausente e é contado; nada de sócios.

Saídas (analise/tabelas/):
  17_proponentes_perfil.csv   um CNPJ de proponente por linha: primeiro e último ano de captação, termos, valor,
                              natureza, porte, MEI, CNAE, município, idade (anos) no 1º de janeiro do primeiro ano
  17_proponentes_resumo.csv   valor captado e número de proponentes por natureza jurídica, porte, MEI, atividade
                              (CNAE, divisão), sede e faixa de idade na primeira captação
  17_mesma_sede.csv           termos em que patrocinador e proponente têm sede no mesmo município, por ano
Uso: python analise/17_proponentes_receita.py
"""
from __future__ import annotations

from pathlib import Path

import pandas as pd

RAIZ = Path(__file__).resolve().parents[1]
EXT = RAIZ / "dados" / "externos"
TAB = RAIZ / "analise" / "tabelas"
RMGV = {"VITORIA", "VILA VELHA", "SERRA", "CARIACICA", "VIANA", "GUARAPARI", "FUNDAO"}
# divisões da CNAE 2.0 esperadas entre proponentes culturais (as demais ficam com o código)
DIVISAO = {"90": "atividades artísticas, criativas e de espetáculos", "94": "organizações associativas",
           "59": "cinema, vídeo e televisão", "82": "serviços de escritório e apoio (inclui eventos, 8230)",
           "73": "publicidade e pesquisa de mercado", "85": "educação", "91": "patrimônio, museus e bibliotecas",
           "93": "esporte e recreação", "58": "edição", "18": "impressão e reprodução", "74": "outras atividades profissionais",
           "70": "consultoria em gestão", "47": "comércio varejista", "56": "alimentação", "88": "assistência social sem alojamento"}


def faixa_idade(anos: float) -> str:
    if pd.isna(anos):
        return "não informado"
    for lim, rot in ((1, "menos de 1 ano"), (3, "1 a 3 anos"), (5, "3 a 5 anos"), (10, "5 a 10 anos")):
        if anos < lim:
            return rot
    return "10 anos ou mais"


def main() -> None:
    t = pd.read_csv(RAIZ / "dados" / "processados" / "transparencia_licc_termos.csv",
                    dtype={"cnpj_proponente": str, "cnpj_patrocinador": str})
    t = t[~t["valor_zero"] & t["cnpj_proponente_dv_ok"]]
    r = pd.read_csv(EXT / "cnpj_proponentes.csv", dtype=str)
    capt = t.groupby("cnpj_proponente").agg(primeiro_ano=("ano", "min"), ultimo_ano=("ano", "max"),
                                            anos=("ano", "nunique"), termos=("valor", "size"), valor=("valor", "sum"))
    p = capt.join(r.set_index("cnpj"), how="left")
    p["com_resposta"] = p["razao_social"].fillna("").ne("")
    p["divisao_cnae"] = p["cnae_fiscal"].fillna("").str.zfill(7).str[:2].where(p["com_resposta"])
    p["atividade"] = p["divisao_cnae"].map(DIVISAO).fillna("divisão " + p["divisao_cnae"].fillna("?"))
    p.loc[~p["com_resposta"], "atividade"] = "sem resposta"
    p["sede"] = [("sem resposta" if not ok else "fora do ES" if uf != "ES" else
                  "RMGV" if str(m).upper() in RMGV else "interior do ES")
                 for ok, uf, m in zip(p["com_resposta"], p["uf"], p["municipio"])]
    abertura = pd.to_datetime(p["data_inicio_atividade"], errors="coerce")
    p["idade_na_primeira_captacao"] = (pd.to_datetime(p["primeiro_ano"].astype(str) + "-01-01") - abertura).dt.days / 365.25
    p["faixa_idade"] = p["idade_na_primeira_captacao"].map(faixa_idade)
    p["mei_hoje"] = p["opcao_pelo_mei"].map({"True": "sim", "False": "não"}).fillna("não informado")
    p.reset_index().rename(columns={"index": "cnpj_proponente"}).drop(columns=["consultado_utc"], errors="ignore") \
        .to_csv(TAB / "17_proponentes_perfil.csv", index=False)

    total = p["valor"].sum()
    linhas = []
    for dim in ("natureza_juridica", "porte", "mei_hoje", "atividade", "sede", "faixa_idade"):
        g = p.assign(**{dim: p[dim].fillna("sem resposta")}).groupby(dim).agg(
            proponentes=("valor", "size"), valor=("valor", "sum"), em_mais_de_um_ano=("anos", lambda a: int((a > 1).sum())))
        g["pct_valor"] = g["valor"] / total
        for k, row in g.sort_values("valor", ascending=False).iterrows():
            linhas.append({"dimensao": dim, "categoria": k, **row.to_dict()})
    res = pd.DataFrame(linhas)
    res["cobertura"] = (f"{len(p)} CNPJs de proponentes (2022-2025, DV válido), {int(p['com_resposta'].sum())} com resposta "
                        f"da Receita; valor R$ {total:,.2f}")
    res["fonte"] = "Portal da Transparência (analise/16) + Receita via dados/externos/cnpj_proponentes.csv"
    res.to_csv(TAB / "17_proponentes_resumo.csv", index=False)
    print(res.drop(columns=["fonte"]).to_string(index=False))

    # mesma sede: município do patrocinador (estabelecimento) × do proponente, na Receita
    pat = pd.read_csv(EXT / "cnpj_patrocinadores.csv", dtype=str).set_index("cnpj")["municipio"]
    t = t.assign(mun_pat=t["cnpj_patrocinador"].map(pat), mun_prop=t["cnpj_proponente"].map(p["municipio"]))
    ok = t[t["mun_pat"].notna() & t["mun_prop"].notna() & (t["mun_pat"] != "") & (t["mun_prop"] != "")]
    ms = ok.assign(mesma=ok["mun_pat"].str.upper() == ok["mun_prop"].str.upper()).groupby("ano").agg(
        termos_com_os_dois_municipios=("valor", "size"), termos_mesma_sede=("mesma", "sum"),
        valor=("valor", "sum"), valor_mesma_sede=("valor", lambda v: v[ok.loc[v.index, "mun_pat"].str.upper() ==
                                                                       ok.loc[v.index, "mun_prop"].str.upper()].sum()))
    ms["pct_valor_mesma_sede"] = ms["valor_mesma_sede"] / ms["valor"]
    ms["termos_no_ano"] = t.groupby("ano").size()
    ms.reset_index().to_csv(TAB / "17_mesma_sede.csv", index=False)
    print(ms.to_string())


if __name__ == "__main__":
    main()
