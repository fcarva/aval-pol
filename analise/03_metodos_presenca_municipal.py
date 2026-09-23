"""
Presença municipal dos projetos habilitados da LICC por ciclo (2022-2026):
insumo para escolher o desenho de avaliação no nível municipal
(nota notas/literatura/03-metodos-e-dados.md, seção 3).

Pergunta: quantos dos 78 municípios do ES aparecem como local de execução de
ao menos um projeto habilitado em cada ciclo, quando cada um aparece pela
primeira vez (coorte de "adoção") e quantos nunca aparecem. Isso decide se um
DiD escalonado tem grupo "nunca tratado" ou só "ainda não tratado".

Fontes:
- dados/licc/habilitados/habilitados-{2022..2026}.csv (coluna `municipio`,
  que nomeia o(s) local(is) de execução do projeto; ver
  licc-gov/codigo/pipeline_habilitados.ts, linhas ~527-600).
- Lista oficial dos 78 municípios do ES: API de localidades do IBGE,
  https://servicodados.ibge.gov.br/api/v1/localidades/estados/32/municipios
  (salva em dados/externos/ibge_municipios_es.csv).
- População residente do Censo 2022: SIDRA, tabela 4709, variável 93,
  https://apisidra.ibge.gov.br/values/t/4709/n6/in%20n3%2032/v/93/p/2022
  (salva em dados/externos/ibge_censo2022_populacao_es.csv).

Método e limites (declarados, não escondidos):
- O campo é texto livre: 100 dos 467 registros listam vários municípios
  separados por ";", alguns vêm truncados ou com erro de digitação, 5 dizem
  "a definir" e 18 estão vazios. O casamento é por nome normalizado (sem
  acento, minúsculo, palavra inteira), dos nomes mais longos para os mais
  curtos, apagando cada casamento antes do próximo (evita que "Itapemirim"
  case dentro de "Cachoeiro de Itapemirim").
- Apelidos usados (lista fechada, abaixo): só grafias que designam sem
  ambiguidade um único município do ES. O que não casa fica AUSENTE e é
  listado em analise/tabelas/03_municipio_nao_casados.csv; nada é imputado.
- "Presença" não é valor: a SECULT não publica o rateio do valor entre
  municípios, então não se atribui valor por município.
- Presença de projeto HABILITADO não é captação. Uma segunda definição usa o
  status `concluido` ou `em_execucao` como aproximação de "captou" - hipótese
  de trabalho herdada de notas/disciplina/03-gertler.md, seção 11.5, cuja
  legenda não foi conferida com a SECULT [VERIFICAR].
- O ciclo 2026 ainda está em captação: sua presença é de habilitação apenas.

Saídas (analise/tabelas/):
- 03_presenca_municipal_por_ciclo.csv
- 03_coortes_primeira_presenca.csv
- 03_municipio_nao_casados.csv
- 03_cobertura_campo_municipio.csv
- 03_presenca_municipal_acumulada.csv
- 03_populacao_por_coorte.csv

Uso: python analise/03_metodos_presenca_municipal.py
"""

from __future__ import annotations

import glob
import os
import re
import unicodedata

import pandas as pd

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TAB = os.path.join(RAIZ, "analise", "tabelas")
EXT = os.path.join(RAIZ, "dados", "externos")
os.makedirs(TAB, exist_ok=True)
os.makedirs(EXT, exist_ok=True)

URL_IBGE = "https://servicodados.ibge.gov.br/api/v1/localidades/estados/32/municipios"
ARQ_IBGE = os.path.join(EXT, "ibge_municipios_es.csv")

# Apelidos: grafia encontrada no campo -> nome oficial IBGE. Só entram grafias
# que apontam, sem ambiguidade, para um único município do ES.
APELIDOS = {
    "cachoeiro": "Cachoeiro de Itapemirim",
    "cachoeiro itapemirim": "Cachoeiro de Itapemirim",
    "cachoeiro do itapemirim": "Cachoeiro de Itapemirim",
    "venda nova": "Venda Nova do Imigrante",
    "santa maria do jetiba": "Santa Maria de Jetibá",
    "jetiba": "Santa Maria de Jetibá",
    "vila veha": "Vila Velha",
    "vila velhae serra": "Vila Velha; Serra",
    "conceicao barra": "Conceição da Barra",
    "divino sao lourenco": "Divino de São Lourenço",
    "nova venecia": "Nova Venécia",
    "atilio vivacqua": "Atílio Vivácqua",
    "afonso claudio": "Afonso Cláudio",
}


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", str(s))
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = re.sub(r"[^a-z0-9 ]+", " ", s.lower())
    return re.sub(r"\s+", " ", s).strip()


def municipios_ibge() -> pd.DataFrame:
    if os.path.exists(ARQ_IBGE):
        return pd.read_csv(ARQ_IBGE, dtype={"cod_ibge": str})
    import requests  # a API do IBGE responde gzip; requests descomprime

    dados = requests.get(URL_IBGE, timeout=60).json()
    df = pd.DataFrame(
        {"cod_ibge": [str(d["id"]) for d in dados], "nome": [d["nome"] for d in dados]}
    ).sort_values("nome")
    df["fonte_url"] = URL_IBGE
    df.to_csv(ARQ_IBGE, index=False, encoding="utf-8")
    return df


def casar(texto: str, nomes: list[str]) -> tuple[list[str], str]:
    """Devolve (municípios casados, resto não casado) para um campo."""
    t = " " + norm(texto) + " "
    for ap, oficial in sorted(APELIDOS.items(), key=lambda kv: -len(kv[0])):
        alvo = norm(oficial)
        # Não reescreve a grafia oficial que já contém o apelido
        # ("venda nova do imigrante" não vira "... do imigrante do imigrante").
        cauda = alvo[len(ap):].strip() if alvo.startswith(ap + " ") else ""
        guarda = rf"(?! {re.escape(cauda)}\b)" if cauda else ""
        t = re.sub(rf"\b{re.escape(ap)}\b{guarda}", " " + alvo + " ", t)
    achados = []
    for nome in sorted(nomes, key=lambda n: -len(norm(n))):
        padrao = rf"\b{re.escape(norm(nome))}\b"
        if re.search(padrao, t):
            achados.append(nome)
            t = re.sub(padrao, " ", t)
    resto = re.sub(r"\b(es|e|municipio|de|do|da|regiao|nova york ny eua|sao paulo)\b", " ", t)
    return achados, re.sub(r"\s+", " ", resto).strip()


def main() -> None:
    ibge = municipios_ibge()
    nomes = ibge["nome"].tolist()
    assert len(nomes) == 78, len(nomes)

    fs = sorted(glob.glob(os.path.join(RAIZ, "dados", "licc", "habilitados", "habilitados-*.csv")))
    d = pd.concat([pd.read_csv(f).assign(ciclo=int(f[-8:-4])) for f in fs], ignore_index=True)

    campo = d["municipio"]
    cobertura = pd.DataFrame(
        {
            "indicador": [
                "registros",
                "municipio_vazio",
                "municipio_a_definir",
                "municipio_com_ponto_e_virgula",
            ],
            "n": [
                len(d),
                int(campo.isna().sum()),
                int(campo.str.contains("definir|defnir", case=False, na=False).sum()),
                int(campo.str.contains(";", na=False).sum()),
            ],
        }
    )

    linhas, nao_casados = [], []
    for _, r in d.iterrows():
        if pd.isna(r["municipio"]):
            continue
        achados, resto = casar(r["municipio"], nomes)
        for m in achados:
            linhas.append({"ciclo": r["ciclo"], "municipio": m, "status": r["status"],
                           "numero_processo": r["numero_processo"]})
        if resto:
            nao_casados.append({"ciclo": r["ciclo"], "numero_processo": r["numero_processo"],
                                "campo_original": r["municipio"], "resto_nao_casado": resto})
    p = pd.DataFrame(linhas)
    cobertura.loc[len(cobertura)] = ["registros_com_ao_menos_um_municipio_casado",
                                     int(p["numero_processo"].nunique())]
    cobertura.loc[len(cobertura)] = ["registros_com_resto_nao_casado", len(nao_casados)]
    cobertura.to_csv(os.path.join(TAB, "03_cobertura_campo_municipio.csv"), index=False)
    pd.DataFrame(nao_casados).to_csv(os.path.join(TAB, "03_municipio_nao_casados.csv"), index=False)

    p["captou_proxy"] = p["status"].isin(["concluido", "em_execucao"])
    por_ciclo = (
        p.groupby("ciclo")
        .agg(municipios_com_habilitado=("municipio", "nunique"))
        .join(p[p["captou_proxy"]].groupby("ciclo").agg(municipios_com_captou_proxy=("municipio", "nunique")))
        .fillna(0).astype(int)
        .reset_index()
    )

    rotulos = {"habilitado": p, "captou_proxy": p[p["captou_proxy"]]}
    coortes = []
    for rot, sub in rotulos.items():
        prim = sub.groupby("municipio")["ciclo"].min()
        for ciclo in sorted(d["ciclo"].unique()):
            coortes.append({"definicao": rot, "primeiro_ciclo": ciclo,
                            "municipios_novos": int((prim == ciclo).sum())})
        coortes.append({"definicao": rot, "primeiro_ciclo": "nunca (2022-2026)",
                        "municipios_novos": 78 - prim.size})
    pc = pd.DataFrame(coortes)
    acum = []
    for rot, sub in rotulos.items():
        prim = sub.groupby("municipio")["ciclo"].min()
        for ciclo in sorted(d["ciclo"].unique()):
            acum.append({"definicao": rot, "ate_ciclo": ciclo,
                         "municipios_ja_presentes": int((prim <= ciclo).sum())})
    por_ciclo.to_csv(os.path.join(TAB, "03_presenca_municipal_por_ciclo.csv"), index=False)
    pc.to_csv(os.path.join(TAB, "03_coortes_primeira_presenca.csv"), index=False)
    pd.DataFrame(acum).to_csv(os.path.join(TAB, "03_presenca_municipal_acumulada.csv"), index=False)

    # População (Censo 2022) por coorte de primeira presença: os nunca
    # presentes são comparáveis aos tratados? (só descritivo)
    pop = populacao_censo2022()
    prim_h = p.groupby("municipio")["ciclo"].min()
    pop["coorte_habilitado"] = pop["nome"].map(prim_h).fillna(0).astype(int)
    pop["coorte_habilitado"] = pop["coorte_habilitado"].replace(0, "nunca").astype(str)
    pop_coorte = (
        pop.groupby("coorte_habilitado")["populacao_2022"]
        .agg(municipios="size", pop_mediana="median", pop_min="min", pop_max="max")
        .reset_index()
    )
    pop_coorte.to_csv(os.path.join(TAB, "03_populacao_por_coorte.csv"), index=False)

    print(cobertura.to_string(index=False))
    print(por_ciclo.to_string(index=False))
    print(pc.to_string(index=False))
    print(pd.DataFrame(acum).to_string(index=False))
    print(pop_coorte.to_string(index=False))
    print(f"não casados: {len(nao_casados)} registros com resto de texto")


URL_SIDRA_POP = "https://apisidra.ibge.gov.br/values/t/4709/n6/in%20n3%2032/v/93/p/2022"
ARQ_POP = os.path.join(EXT, "ibge_censo2022_populacao_es.csv")


def populacao_censo2022() -> pd.DataFrame:
    """População residente, Censo 2022 (SIDRA tabela 4709, variável 93)."""
    if not os.path.exists(ARQ_POP):
        import requests

        linhas = requests.get(URL_SIDRA_POP, timeout=60).json()[1:]
        df = pd.DataFrame(
            {
                "cod_ibge": [r["D1C"] for r in linhas],
                "municipio_sidra": [r["D1N"] for r in linhas],
                "populacao_2022": [int(r["V"]) for r in linhas],
            }
        )
        df["fonte_url"] = URL_SIDRA_POP
        df.to_csv(ARQ_POP, index=False, encoding="utf-8")
    df = pd.read_csv(ARQ_POP, dtype={"cod_ibge": str})
    ibge = municipios_ibge()
    out = ibge.merge(df[["cod_ibge", "populacao_2022"]], on="cod_ibge", how="left")
    assert out["populacao_2022"].notna().all()
    return out


if __name__ == "__main__":
    main()
