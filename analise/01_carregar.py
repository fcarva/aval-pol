"""01_carregar.py — padroniza e une os habilitados 2022-2026 e os captados de 2025.

Entradas (transcrição oficial herdada do licc.gov, com fonte_url em cada linha):
  dados/licc/habilitados/habilitados-{2022..2026}.csv  (seções "PROJETOS HABILITADOS - ANO X"
      da lista única da SECULT: https://secult.es.gov.br/lista-de-projetos-habilitados)
  dados/licc/oficial/captados-2025.csv  (anexo "RECURSO FINANCEIRO CAPTADO - 2025")
  lista oficial de municípios do IBGE (via _comum.municipios_ibge(), cache em dados/externos/)

Saídas (dados/processados/):
  habilitados.csv            uma linha por REGISTRO (projeto × seção/ciclo): 467
  habilitados_municipios.csv uma linha por registro × município do ES resolvido (presença)
  captados_2025.csv          uma linha por projeto que captou em 2025 (63), com o casamento
  aportes_2025.csv           uma linha por termo de patrocínio (95)
  proponentes.csv            chave canônica de proponente, variantes e natureza inferida
e tabelas de auditoria em analise/tabelas/01_*.csv.

Decisões (todas declaradas; nenhuma troca ausência por zero):
  * "ciclo" = ano da seção "PROJETOS HABILITADOS - ANO X" em que o registro aparece.
    O prefixo do número de processo (ano de protocolo) NÃO é o ciclo: a seção 2026 tem
    74 processos protocolados em 2025. 4 processos aparecem em duas seções (2025 e 2026).
  * Valores de R$ 500,00 (4 casos na p. 12, seção 2024) são tratados como AUSENTES na
    análise: a versão de 10/09/2026 do PDF imprime "R$ 500,000,00" (separador malformado)
    para ao menos um deles (lido via firecrawl); o transcritor leu 500. O bruto é mantido.
  * Município = "Local de Execução" (não é a sede do proponente). A célula da fonte mistura
    quebras de linha; o resolvedor casa nomes oficiais do IBGE (mais longo primeiro) + uma
    tabela explícita de apelidos/erros de grafia + reparos de transbordamento entre
    registros vizinhos (lista TRANSBORDO), todos auditáveis em 01_municipios_resolucao.csv.
  * Valor só é atribuído a um município quando o registro nomeia UM único local e ele é
    um município do ES (regra do licc.gov). Presença conta em todos os municípios nomeados.
  * Casamento captados→habilitados: título normalizado EXATO (regra do licc.gov). Título que
    corresponde a mais de um processo distinto fica fora (ambíguo) e é relatado.
"""
from __future__ import annotations

import re

import numpy as np
import pandas as pd

from _comum import (
    LICC,
    PROCESSADOS,
    TABELAS,
    distritos_ibge,
    municipios_ibge,
    normalizar,
)

CICLOS_ORDEM_DOC = (2026, 2025, 2024, 2023, 2022)  # ordem em que as seções aparecem no PDF

# --------------------------------------------------------------------------------------
# 1. Habilitados
# --------------------------------------------------------------------------------------


def carregar_habilitados() -> pd.DataFrame:
    partes = []
    for ciclo in CICLOS_ORDEM_DOC:
        df = pd.read_csv(LICC / "habilitados" / f"habilitados-{ciclo}.csv", dtype=str, encoding="utf-8")
        df["ciclo"] = ciclo
        df["linha_arquivo"] = np.arange(2, len(df) + 2)  # linha 1 = cabeçalho
        partes.append(df)
    d = pd.concat(partes, ignore_index=True)
    d["ordem_doc"] = np.arange(len(d))
    d["ano_protocolo"] = d["numero_processo"].str[:4].astype(int)
    d["fonte_pagina"] = d["fonte_pagina"].astype(int)
    for c in ("valor_autorizado", "valor_total"):
        d[f"{c}_bruto"] = pd.to_numeric(d[c], errors="coerce")
    # R$ 500,00 é artefato de separador malformado na fonte ("R$ 500,000,00"): ausente.
    d["flag_valor_suspeito"] = (d["valor_autorizado_bruto"] <= 1000) | (d["valor_total_bruto"] <= 1000)
    d["valor_autorizado"] = d["valor_autorizado_bruto"].where(d["valor_autorizado_bruto"] > 1000)
    d["valor_total"] = d["valor_total_bruto"].where(d["valor_total_bruto"] > 1000)
    d["titulo_norm"] = d["projeto"].map(normalizar)
    return d


# --------------------------------------------------------------------------------------
# 2. Municípios
# --------------------------------------------------------------------------------------

# Apelidos e grafias da fonte -> nome oficial IBGE. Cada entrada é conferível na própria
# célula (ver 01_municipios_resolucao.csv). "prefixo único" = o fragmento é início de um
# único nome oficial entre os 78 (ex.: nenhum outro município começa com "Cachoeiro").
APELIDOS = {
    "divino sao lourenco": ("Divino de São Lourenço", "grafia sem 'de'"),
    "santa maria do jetiba": ("Santa Maria de Jetibá", "grafia 'do'"),
    "cachoeiro do itapemirim": ("Cachoeiro de Itapemirim", "grafia 'do'"),
    "cachoeiro itapemirim": ("Cachoeiro de Itapemirim", "grafia sem 'de'"),
    "conceicao barra": ("Conceição da Barra", "grafia sem 'da'"),
    "vila veha": ("Vila Velha", "erro de digitação da fonte"),
    "vila velhae": ("Vila Velha", "'Vila Velhae Serra' (conjunção colada)"),
    "cachoeiro": ("Cachoeiro de Itapemirim", "prefixo único"),
    "venda nova": ("Venda Nova do Imigrante", "prefixo único"),
    "santa maria": ("Santa Maria de Jetibá", "prefixo único [VERIFICAR]"),
    # distritos (API de localidades do IBGE, /distritos) -> município-sede
    "sao torquatro": ("Vila Velha", "distrito IBGE São Torquato (320520025), grafia 'Torquatro'"),
    "santa marta": ("Ibitirama", "distrito IBGE Santa Marta (320255310)"),
    # vila/distrito citado no objeto do projeto 2026-9T9CZ da própria lista da SECULT
    # ("Itaúnas, distrito de Conceição da Barra/ES"); não consta como distrito na API IBGE
    "itaunas": ("Conceição da Barra", "localidade de Conceição da Barra segundo o objeto do projeto 2026-9T9CZ na lista SECULT [VERIFICAR]"),
}

# Locais nomeados que NÃO são município do ES: ficam não resolvidos (ausência declarada).
FORA_ES = {"sao paulo": "São Paulo", "espanha": "Espanha", "nova york ny eua": "Nova York - NY/EUA"}
NAO_RESOLVIDOS = {
    "a definir": "local a definir",
    "a defnir": "local a definir",
    "regiao do caparao": "região (não município)",
    "caparao": "região do Caparaó (não há município do ES com esse nome; o homônimo é de MG)",
    "patrimonio da penha": "localidade não municipal",
    "manguinhos": "bairro/localidade não municipal",
    "flexal": "bairro/localidade não municipal",
    "terra vermelha": "bairro/localidade não municipal",
    "sao pedro": "ambíguo (distrito de Muniz Freire ou região administrativa de Vitória)",
    "itarare": "bairro/localidade não municipal",
    "novo horizonte": "bairro/localidade não municipal",
    "feu rosa": "bairro/localidade não municipal",
    "costa rica": "local não identificado (provavelmente fora do ES)",
}
PALAVRAS_VAZIAS = {"e", "de", "do", "da", "es", "municipio"}

# Transbordamento: a célula "Local de Execução" quebra em várias linhas e o extrator
# posicional atribuiu linhas ao registro vizinho (no PDF o rótulo é centralizado sobre o
# grupo de linhas — ver CLAUDE-licc.md). Evidência: o registro A termina num fragmento e
# o registro seguinte B começa com o complemento exato de um nome oficial.
# (processo_A, ciclo, fragmento_final_A, processo_B, fragmento_inicial_B, nome resultante)
# O nome é atribuído a A por convenção; A e B recebem flag_municipio_incerto.
TRANSBORDO = [
    ("2022-JBZVN", 2022, "Divino São", "2022-83B3M", "Lourenço", "Divino de São Lourenço"),
    ("2022-83B3M", 2022, "Santa", "2022-220W3", "Maria", "Santa Maria de Jetibá"),
    ("2022-0PP25", 2022, "Domingos", "2022-KSSWD", "Martins", "Domingos Martins"),
    ("2022-PHX83", 2022, "Vargem", "2022-87D66", "Alta", "Vargem Alta"),
    ("2022-HH970", 2023, "Marechal", "2023-MZ120", "Floriano", "Marechal Floriano"),
    ("2022-GHF1N", 2023, "Vila", "2022-8S91R", "Pavão", "Vila Pavão"),
    ("2022-MH6GF", 2023, "Santa", "2022-61S2R", "Teresa", "Santa Teresa"),
    ("2025-49GXP", 2026, "Santa Maria de", "2024-454L8", "Jetibá", "Santa Maria de Jetibá"),
    ("2024-454L8", 2026, "Cachoeiro de", "2025-SB2J8", "Itapemirim", "Cachoeiro de Itapemirim"),
]
# Célula com linhas intercaladas dentro do próprio registro (duas colunas de texto):
# "Domingos Vargem Alta; Martins; ...; Cachoeiro Brejetuba. de Itapemirim".
REESCRITA_CELULA = {
    ("2022-220W3", 2022): (
        "Santa Teresa; Domingos Martins; Vargem Alta; Castelo; Cachoeiro de Itapemirim; Brejetuba; Caparaó; Marataízes",
        "linhas intercaladas na célula: 'Domingos … Martins' e 'Cachoeiro … de Itapemirim' + 'Brejetuba'",
    ),
}


def _remover_prefixo(texto: str, fragmento: str) -> str:
    t = texto.lstrip()
    assert t.startswith(fragmento), (texto, fragmento)
    return t[len(fragmento):].lstrip(" ;.,")


def _remover_sufixo(texto: str, fragmento: str) -> str:
    t = texto.rstrip()
    assert t.endswith(fragmento), (texto, fragmento)
    return t[: -len(fragmento)].rstrip(" ;.,")


def reparar_celulas(d: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    d = d.copy()
    d["municipio_fonte"] = d["municipio"]
    d["municipio_reparado"] = d["municipio"]
    d["flag_municipio_incerto"] = False
    d["nota_municipio"] = ""
    log = []
    idx = {(r.numero_processo, r.ciclo): i for i, r in d.iterrows()}
    for pa, ciclo, fa, pb, fb, nome in TRANSBORDO:
        ia, ib = idx[(pa, ciclo)], idx[(pb, ciclo)]
        assert d.at[ib, "ordem_doc"] == d.at[ia, "ordem_doc"] + 1, (pa, pb)
        d.at[ia, "municipio_reparado"] = _remover_sufixo(d.at[ia, "municipio_reparado"], fa) + "; " + nome
        d.at[ib, "municipio_reparado"] = _remover_prefixo(d.at[ib, "municipio_reparado"], fb)
        for i, papel in ((ia, "A"), (ib, "B")):
            d.at[i, "flag_municipio_incerto"] = True
            d.at[i, "nota_municipio"] += f"transbordo {pa}->{pb} ('{fa}'+'{fb}'='{nome}', papel {papel}); "
        log.append({"tipo": "transbordo", "processo_A": pa, "processo_B": pb, "ciclo": ciclo,
                    "fragmento_A": fa, "fragmento_B": fb, "resultado": nome})
    for (p, ciclo), (novo, motivo) in REESCRITA_CELULA.items():
        i = idx[(p, ciclo)]
        antes = d.at[i, "municipio_reparado"]
        d.at[i, "municipio_reparado"] = novo
        d.at[i, "flag_municipio_incerto"] = True
        d.at[i, "nota_municipio"] += f"reescrita: {motivo}; "
        log.append({"tipo": "reescrita", "processo_A": p, "processo_B": "", "ciclo": ciclo,
                    "fragmento_A": antes, "fragmento_B": "", "resultado": novo})
    return d, pd.DataFrame(log)


def resolver_municipios(d: pd.DataFrame, mun: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    oficiais = {r.chave: r.municipio for r in mun.itertuples()}
    cod = {r.municipio: r.cod_ibge for r in mun.itertuples()}
    padroes = {k: (v, "nome oficial IBGE") for k, v in oficiais.items()}
    padroes.update(APELIDOS)
    ordem = sorted(padroes, key=len, reverse=True)
    nao_mun = {**{k: ("fora_es", v) for k, v in FORA_ES.items()},
               **{k: ("nao_resolvido", v) for k, v in NAO_RESOLVIDOS.items()}}
    ordem_nao = sorted(nao_mun, key=len, reverse=True)

    linhas, auditoria = [], []
    for r in d.itertuples():
        bruto = r.municipio_reparado
        if pd.isna(bruto) or not str(bruto).strip():
            linhas.append({"i": r.Index, "mun": [], "fora": [], "nres": [], "resto": "", "ausente": True})
            continue
        s = " " + normalizar(bruto) + " "
        achados, fora, nres = [], [], []
        for k in ordem:
            pat = f" {k} "
            while pat in s:
                nome, regra = padroes[k]
                achados.append(nome)
                if regra != "nome oficial IBGE":
                    auditoria.append({"numero_processo": r.numero_processo, "ciclo": r.ciclo,
                                      "trecho": k, "resolvido_para": nome, "regra": regra})
                s = s.replace(pat, " ", 1)
        for k in ordem_nao:
            pat = f" {k} "
            while pat in s:
                tipo, rot = nao_mun[k]
                (fora if tipo == "fora_es" else nres).append(rot if tipo == "fora_es" else f"{k} ({rot})")
                s = s.replace(pat, " ", 1)
        resto = " ".join(w for w in s.split() if w not in PALAVRAS_VAZIAS)
        linhas.append({"i": r.Index, "mun": list(dict.fromkeys(achados)), "fora": fora, "nres": nres,
                       "resto": resto, "ausente": False})

    res = pd.DataFrame(linhas).set_index("i")
    assert (res["resto"] == "").all(), res.loc[res["resto"] != "", "resto"]
    d = d.copy()
    d["municipios_es"] = res["mun"].map(lambda xs: "; ".join(xs))
    d["cod_ibge_lista"] = res["mun"].map(lambda xs: ";".join(str(cod[x]) for x in xs))
    d["n_municipios_es"] = res["mun"].map(len)
    d["locais_fora_es"] = res["fora"].map(lambda xs: "; ".join(xs))
    d["locais_nao_resolvidos"] = res["nres"].map(lambda xs: "; ".join(xs))
    d["municipio_ausente_na_fonte"] = res["ausente"]
    n_locais = res["mun"].map(len) + res["fora"].map(len) + res["nres"].map(len)
    unico = (res["mun"].map(len) == 1) & (n_locais == 1)
    d["municipio_valor"] = np.where(unico, res["mun"].map(lambda xs: xs[0] if xs else None), None)
    d["cod_ibge_valor"] = np.where(unico, res["mun"].map(lambda xs: cod[xs[0]] if xs else np.nan), np.nan)
    d["tipo_local"] = np.select(
        [res["ausente"], unico, res["mun"].map(len) >= 2, (res["mun"].map(len) == 1) & (n_locais > 1)],
        ["ausente", "um_municipio", "varios_municipios", "um_municipio_mais_outros_locais"],
        default="so_locais_nao_municipais",
    )
    return d, pd.DataFrame(auditoria)


# --------------------------------------------------------------------------------------
# 3. Proponentes: chave canônica e natureza jurídica inferida do NOME
# --------------------------------------------------------------------------------------

SUFIXOS = {"ltda", "me", "epp", "eireli", "mei", "sa"}
# Variantes que a normalização não une, unidas à mão (cada par é conferível lado a lado
# em proponentes.csv). Chave: variante normalizada; valor: chave canônica.
ALIAS_PROPONENTE = {
    "karoline del": "karoline delfino felicio",
    "ananda": "ananda lugon bourguignon",
    "associacao amigos da justica cidadania": "associacao amigos da justica cidadania educacao e arte",
    "instituto tres pontoes de acao social e cultural instituto cultural das montanhas":
        "instituto tres pontoes de acao social e cultural",
    "programa de promocao e assistencia social casa verde": "programa de promocao e assistencia social",
    "institutos ultimos refugios": "instituto ultimos refugios",
    "ws projetos criatrivos": "ws projetos criativos",
    "regiao sul capixaba dos vales e cafe convention visitours bureau":
        "regiao sul capixaba dos vales e cafe convention visitors bureau",
    "cluster comunicacoes e marketing": "cluster comunicacao e marketing",
    "w par associados": "wpar associados",
    "alpha empreendimentos galpao de ideias": "alpha empreendimentos",
    "instituto das pretas org": "instituto das pretas",
    "wb producoes artisticas e culturais org": "wb producoes artisticas e culturais",
    "coes cia de opera do espirito santo": "companhia de opera do espirito santo",
    "associacao de bandas de congo de cariacica abcc": "associacao de bandas de congo de cariacica",
    "instituto modus vivendi de desenvolvimento social cultural e ambiental": "instituto modus vivendi",
    "r v vagmaker produtora": "rv vagmaker produtora",
    "julia cabral abreu sodre": "julia cabral abreu sodre",
}


def chave_proponente(nome: str) -> str:
    s = normalizar(re.sub(r"\(.*?\)", " ", str(nome)))  # "(Em análise na SEFAZ) ..." sai
    s = re.sub(r"^\d{2} \d{3} \d{3} ", "", s)  # raiz de CNPJ no início (MEI)
    s = re.sub(r" \d{11}$", "", s)  # CPF no fim (razão social de MEI)
    # sufixos societários saem em qualquer posição ("Alpha Empreendimentos LTDA - Galpão
    # de Ideias"); "me" e "sa" só no fim, porque podem ser palavra do nome.
    toks = [t for t in s.split() if t not in {"ltda", "eireli", "epp", "mei"}]
    while toks and toks[-1] in SUFIXOS:
        toks.pop()
    if len(toks) >= 2 and toks[-2:] == ["s", "a"]:
        toks = toks[:-2]
    s = " ".join(toks)
    return ALIAS_PROPONENTE.get(s, s)


# Regras de natureza jurídica, aplicadas NESTA ORDEM ao nome como publicado:
REGRAS_NATUREZA = [
    ("mei_ei", "MEI/empresário individual",
     r"(\b\d{11}\b|^\d{2}\.?\d{3}\.?\d{3}\s|\bmei\b)"),
    ("empresa_sufixo", "Empresa (sufixo societário explícito)",
     r"\b(ltda|eireli|epp|s\s*/?\s*a|me)\b\.?\s*[-;.]?\s*$|\bltda\b|\beireli\b|\bepp\b|\bs/a\b"),
    ("osc", "Associação/instituto/fundação e outras entidades associativas",
     r"\b(associacao|instituto|institutos|instituicao|fundacao|gremio|sociedade|federacao|"
     r"academia de letras|centro cultural|centro de cultura|centro desportivo|circolo|"
     r"colonia de pescadores|sindicato|mosteiro|convention|secretariado|"
     r"programa de promocao|agencia de desenvolvimento)\b"),
    ("empresa_provavel", "Empresa provável (termo comercial, sem sufixo)",
     r"\b(producoes|producao|produtora|eventos|filmes|editora|estudio|studio|comunicacao|"
     r"marketing|projetos|design|entretenimento|consultoria|servicos|empreendimentos|records|"
     r"music|company|economia criativa|solucoes|associados|press)\b"),
    ("grupo_artistico", "Grupo/coletivo/companhia artística (natureza não inferível)",
     r"\b(coletivo|grupo teatral|cia|companhia|bloco|movimento cultural)\b"),
]
ROTULO_INDETERMINADO = "Indeterminado (inclui nomes de pessoa natural sem CPF)"


def natureza_do_nome(nome: str) -> str:
    s = normalizar(nome) if not re.search(r"^\d{2}\.\d{3}\.\d{3}\s", str(nome)) else str(nome)
    alvo = f"{s} || {str(nome).lower()}"
    for codigo, _, rx in REGRAS_NATUREZA:
        if re.search(rx, alvo):
            return codigo
    return "indeterminado"


PRIORIDADE = ["mei_ei", "empresa_sufixo", "osc", "empresa_provavel", "grupo_artistico", "indeterminado"]


def tabela_proponentes(nomes: pd.Series) -> pd.DataFrame:
    df = pd.DataFrame({"proponente": nomes.dropna().unique()})
    df["chave_proponente"] = df["proponente"].map(chave_proponente)
    df["natureza_variante"] = df["proponente"].map(natureza_do_nome)
    agg = (
        df.groupby("chave_proponente")
        .agg(variantes=("proponente", lambda s: " | ".join(sorted(s))),
             n_variantes=("proponente", "size"),
             naturezas_variantes=("natureza_variante", lambda s: ",".join(sorted(set(s)))))
        .reset_index()
    )
    agg["natureza"] = agg["naturezas_variantes"].map(
        lambda s: min(s.split(","), key=PRIORIDADE.index))
    rot = {c: r for c, r, _ in REGRAS_NATUREZA}
    rot["indeterminado"] = ROTULO_INDETERMINADO
    agg["natureza_rotulo"] = agg["natureza"].map(rot)
    return agg


# --------------------------------------------------------------------------------------
# 4. Captados 2025
# --------------------------------------------------------------------------------------


def carregar_captados() -> tuple[pd.DataFrame, pd.DataFrame]:
    c = pd.read_csv(LICC / "oficial" / "captados-2025.csv", dtype=str, encoding="utf-8")
    c["linha_arquivo"] = np.arange(2, len(c) + 2)
    c["valor_autorizado"] = pd.to_numeric(c["valor_autorizado"], errors="coerce")
    c["valor_captado"] = pd.to_numeric(c["valor_captado"], errors="coerce")
    c["titulo_norm"] = c["projeto"].map(normalizar)
    c["id_captado"] = [f"C25-{i:02d}" for i in range(1, len(c) + 1)]
    ap = []
    for r in c.itertuples():
        for termo in str(r.aportes).split(";"):
            termo = termo.strip()
            if not termo:
                continue
            cnpj, nome, valor = (termo.split("|") + [None, None])[:3]
            ap.append({"id_captado": r.id_captado, "projeto": r.projeto, "cnpj": cnpj.strip(),
                       "patrocinador_nome": nome.strip() if nome else None,
                       "valor": pd.to_numeric(valor, errors="coerce")})
    ap = pd.DataFrame(ap)
    ap["cnpj_raiz"] = ap["cnpj"].str.replace(r"\D", "", regex=True).str[:8]
    return c, ap


def casar_captados(c: pd.DataFrame, h: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Título normalizado EXATO; ambíguo se o título corresponde a >1 processo distinto."""
    por_titulo = h.groupby("titulo_norm")["numero_processo"].apply(lambda s: sorted(set(s)))
    c = c.copy()
    status, proc = [], []
    for t in c["titulo_norm"]:
        ps = por_titulo.get(t)
        if ps is None:
            status.append("sem_correspondencia"); proc.append(None)
        elif len(ps) > 1:
            status.append("ambiguo"); proc.append(";".join(ps))
        else:
            status.append("casado"); proc.append(ps[0])
    c["casamento"] = status
    c["numero_processo"] = [p if s == "casado" else None for p, s in zip(proc, status)]
    c["processos_candidatos"] = [p if s == "ambiguo" else None for p, s in zip(proc, status)]
    # Ciclos em que o processo casado aparece (pode ser mais de uma seção)
    ciclos = h.groupby("numero_processo")["ciclo"].apply(lambda s: ";".join(str(x) for x in sorted(set(s))))
    c["ciclos_habilitacao"] = c["numero_processo"].map(ciclos)
    c["ciclo_habilitacao_min"] = c["ciclos_habilitacao"].map(
        lambda s: int(s.split(";")[0]) if isinstance(s, str) else np.nan)

    # Casamento SECUNDÁRIO (só para análise de sensibilidade, nunca no resultado principal):
    # título ambíguo desempatado por valor autorizado idêntico ao centavo (candidato único).
    h_val = h.drop_duplicates("numero_processo", keep="first").set_index("numero_processo")["valor_autorizado"]
    sec = []
    for r in c.itertuples():
        p2 = None
        if r.casamento == "ambiguo":
            cands = r.processos_candidatos.split(";")
            iguais = [p for p in cands
                      if pd.notna(h_val.get(p)) and abs(h_val.get(p) - r.valor_autorizado) < 0.005]
            # candidato com valor ausente poderia ser o verdadeiro: aí não se desempata
            if len(iguais) == 1 and all(pd.notna(h_val.get(p)) for p in cands):
                p2 = iguais[0]
        sec.append(p2)
    c["numero_processo_secundario"] = sec
    c["ciclo_habilitacao_min_secundario"] = c["numero_processo_secundario"].map(
        lambda p: int(ciclos[p].split(";")[0]) if isinstance(p, str) else np.nan)

    # Diagnóstico (NÃO usado nos resultados principais): entre os sem
    # correspondência, candidatos com mesma chave de proponente E mesmo valor autorizado.
    diag = []
    hh = h.assign(chave_proponente=h["proponente"].map(chave_proponente))
    for r in c[c["casamento"] == "sem_correspondencia"].itertuples():
        kp = chave_proponente(r.proponente)
        cand = hh[(hh["chave_proponente"] == kp) & (np.isclose(hh["valor_autorizado"], r.valor_autorizado))]
        diag.append({"id_captado": r.id_captado, "projeto_captados": r.projeto, "proponente": r.proponente,
                     "valor_autorizado": r.valor_autorizado, "n_candidatos": cand["numero_processo"].nunique(),
                     "candidatos": " | ".join(f"{p} [{t}] ciclo {cy}" for p, t, cy in
                                               cand[["numero_processo", "projeto", "ciclo"]].itertuples(index=False))})
    return c, pd.DataFrame(diag)


# --------------------------------------------------------------------------------------


def main() -> None:
    mun = municipios_ibge()
    distritos_ibge()  # cache para auditoria dos apelidos de distrito
    h = carregar_habilitados()
    h, log_transbordo = reparar_celulas(h)
    h, aud_apelidos = resolver_municipios(h, mun)
    h["chave_proponente"] = h["proponente"].map(chave_proponente)

    c, ap = carregar_captados()
    c["chave_proponente"] = c["proponente"].map(chave_proponente)
    c, diag = casar_captados(c, h)

    prop = tabela_proponentes(pd.concat([h["proponente"], c["proponente"]]))

    # Presença: registro × município
    longo = (
        h.loc[h["n_municipios_es"] > 0, ["numero_processo", "ciclo", "municipios_es", "flag_municipio_incerto"]]
        .assign(municipio=lambda x: x["municipios_es"].str.split("; "))
        .explode("municipio")
        .drop(columns="municipios_es")
        .merge(mun[["municipio", "cod_ibge"]], on="municipio", how="left")
    )
    assert longo["cod_ibge"].notna().all()

    cols = ["ordem_doc", "ciclo", "numero_processo", "ano_protocolo", "projeto", "titulo_norm", "proponente",
            "chave_proponente", "valor_autorizado", "valor_total", "valor_autorizado_bruto", "valor_total_bruto",
            "flag_valor_suspeito", "status", "enquadramento", "municipio_fonte", "municipio_reparado",
            "municipios_es", "cod_ibge_lista", "n_municipios_es", "locais_fora_es", "locais_nao_resolvidos",
            "municipio_ausente_na_fonte", "tipo_local", "municipio_valor", "cod_ibge_valor",
            "flag_municipio_incerto", "nota_municipio", "fonte_url", "fonte_pagina", "linha_arquivo"]
    h[cols].to_csv(PROCESSADOS / "habilitados.csv", index=False, encoding="utf-8")
    longo.to_csv(PROCESSADOS / "habilitados_municipios.csv", index=False, encoding="utf-8")
    c.drop(columns=["aportes"]).to_csv(PROCESSADOS / "captados_2025.csv", index=False, encoding="utf-8")
    ap.to_csv(PROCESSADOS / "aportes_2025.csv", index=False, encoding="utf-8")
    prop.to_csv(PROCESSADOS / "proponentes.csv", index=False, encoding="utf-8")

    log_transbordo.to_csv(TABELAS / "01_municipios_transbordo.csv", index=False, encoding="utf-8")
    aud = h.loc[(h["locais_fora_es"] != "") | (h["locais_nao_resolvidos"] != "") | h["flag_municipio_incerto"]
                | h["municipio_ausente_na_fonte"],
                ["numero_processo", "ciclo", "municipio_fonte", "municipio_reparado", "municipios_es",
                 "locais_fora_es", "locais_nao_resolvidos", "tipo_local", "nota_municipio"]]
    aud.to_csv(TABELAS / "01_municipios_resolucao.csv", index=False, encoding="utf-8")
    aud_apelidos.to_csv(TABELAS / "01_municipios_apelidos_aplicados.csv", index=False, encoding="utf-8")
    diag.to_csv(TABELAS / "01_captados_diagnostico_sem_correspondencia.csv", index=False, encoding="utf-8")
    h.loc[h["flag_valor_suspeito"], ["numero_processo", "ciclo", "projeto", "valor_autorizado_bruto",
                                      "valor_total_bruto", "fonte_pagina"]].to_csv(
        TABELAS / "01_valores_suspeitos.csv", index=False, encoding="utf-8")

    # Resumo no console
    print(f"habilitados: {len(h)} registros, {h.numero_processo.nunique()} processos distintos")
    print(h.groupby("ciclo").size().to_dict())
    print("tipo_local:", h["tipo_local"].value_counts().to_dict())
    print("flag_municipio_incerto:", int(h["flag_municipio_incerto"].sum()),
          "| valores suspeitos:", int(h["flag_valor_suspeito"].sum()))
    print("captados:", len(c), c["casamento"].value_counts().to_dict())
    print("aportes:", len(ap), "| CNPJ:", ap.cnpj.nunique(), "| raízes CNPJ:", ap.cnpj_raiz.nunique())
    print("proponentes (chaves):", prop.shape[0], prop["natureza"].value_counts().to_dict())


if __name__ == "__main__":
    main()
