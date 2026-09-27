"""
12 — Extratos das atas da Comissão de Avaliação Permanente (CAP) da LICC, 2022-2026.

A SECULT publica, reunião a reunião, o extrato da ata da CAP (IN 2024, art. 32, § 3º; Regimento da CAP), com os
processos habilitados, em diligência, inabilitados e, em 2026, não avaliados. A lista oficial de habilitados não traz
os inabilitados; os extratos trazem, e trazem a data da reunião em que cada projeto foi habilitado.

Fonte: textos coletados pelo relé (analise/rede/buscar_fontes.py, etapa "seguir", prefixos cap2022 a cap2026), com a
lista de links e rótulos em dados/fontes_web/seguir/cap20XX.tsv. O rótulo do link dá o número e a data da reunião.

Regras (CLAUDE.md):
- o extrato não traz motivo nem critério da inabilitação: o motivo fica indeterminado, não se infere;
- nomes de pessoa física não entram nas tabelas: guarda-se o processo e a natureza inferida do proponente;
- a cobertura é declarada: quantos habilitados da lista oficial aparecem habilitados em algum extrato.

Saídas (analise/tabelas/):
  12_cap_deliberacoes.csv       uma linha por processo × reunião × situação
  12_cap_reunioes.csv           uma linha por extrato lido (reunião, data, contagens, arquivo)
  12_cap_status_por_ano.csv     contagens e taxa de inabilitação por ano da reunião
  12_cap_cobertura.csv          habilitados da lista oficial × extratos, por ciclo
Uso: python analise/12_atas_cap.py
"""
from __future__ import annotations

import csv
import importlib.util
import re
import unicodedata
from pathlib import Path

import pandas as pd

RAIZ = Path(__file__).resolve().parents[1]
FW = RAIZ / "dados" / "fontes_web"
PAG = FW / "paginas"
TAB = RAIZ / "analise" / "tabelas"
PROC = RAIZ / "dados" / "processados"

_spec = importlib.util.spec_from_file_location("carregar", RAIZ / "analise" / "01_carregar.py")
carregar = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(carregar)

PROCESSO = re.compile(r"\b(20\d{2})\s*-\s*([0-9A-Z]{5})\b")
SECAO = re.compile(
    r"projetos?\s+(em\s+aprecia\w+\s+de\s+altera\w+|indeferid\w*\s+a\s+solicita\w+\s+de\s+altera\w+|"
    r"habilitad\w*|em\s+dilig\w*|inabilitad\w*|n[ãa]o\s+avaliad\w*|n[ãa]o\s+habilitad\w*|"
    r"arquivad\w*|indeferid\w*|desclassificad\w*|retirad\w*|reconsidera\w*)"
    r"|aprecia\w+\s+de\s+recurso", re.I)
MESES = {m: i + 1 for i, m in enumerate(["janeiro", "fevereiro", "marco", "abril", "maio", "junho", "julho", "agosto",
                                          "setembro", "outubro", "novembro", "dezembro"])}


def sem_acento(s: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFKD", s) if not unicodedata.combining(c)).lower()


def situacao(cabecalho: str) -> str:
    c = sem_acento(cabecalho)
    if "recurso" in c:
        return "recurso contra inabilitação (apreciado)"
    if "altera" in c:
        return "alteração indeferida" if "indeferid" in c else "alteração em apreciação"
    if "inabilitad" in c or "nao habilitad" in c:
        return "inabilitado"
    if "habilitad" in c:
        return "habilitado"
    if "dilig" in c:
        return "em diligência"
    if "nao avaliad" in c:
        return "não avaliado"
    return re.sub(r"^projetos?\s+", "", c)


def data_do_rotulo(rotulo: str, nome: str) -> pd.Timestamp | None:
    for alvo in (rotulo, nome):
        m = re.search(r"(\d{1,2})[._/-](\d{1,2})[._/-](\d{2,4})", alvo)
        if m:
            d, mes, a = int(m.group(1)), int(m.group(2)), int(m.group(3))
            a = a + 2000 if a < 100 else a
            try:
                return pd.Timestamp(a, mes, d)
            except ValueError:
                pass
    return None


def data_do_texto(texto: str) -> pd.Timestamp | None:
    t = sem_acento(texto)
    m = re.search(r"vitoria\s*[,-]\s*(\d{1,2})\s+de\s+([a-z]+)\s+de\s+(\d{4})", t)
    if m and m.group(2) in MESES:
        return pd.Timestamp(int(m.group(3)), MESES[m.group(2)], int(m.group(1)))
    return None


def natureza(trecho: str) -> str:
    """Natureza inferida do nome do proponente (regras de 01_carregar.py); CPF mascarado = pessoa física ou MEI."""
    trecho = " ".join(re.split(r"\n\s*\n", trecho)[0].split())  # o nome pode quebrar a linha
    m = re.search(r"proponente\s*:\s*(.+?)(?:\.\s+o proponente|;|$)", trecho, flags=re.I)
    if not m:
        return "sem proponente no extrato"
    nome = m.group(1).strip()
    if re.search(r"X{3}\.?X{3}\.?X{3}-?X{2}|X{11}", nome):
        return "mei_ei"
    return carregar.natureza_do_nome(nome)


def ler_extratos() -> tuple[pd.DataFrame, pd.DataFrame]:
    delib, reunioes = [], []
    for indice in sorted((FW / "seguir").glob("cap20*.tsv")):
        ano_indice = int(indice.stem[3:])
        with indice.open(encoding="utf-8") as f:
            links = list(csv.DictReader(f, delimiter="\t"))
        for ln in links:
            arq = PAG / f"{ln['id']}.txt"
            if ln["status"] != "200" or not arq.exists():
                reunioes.append({"ano_indice": ano_indice, "rotulo": ln["rotulo"], "arquivo": str(arq.relative_to(RAIZ)),
                                 "lido": False, "motivo": f"status {ln['status']}"})
                continue
            texto = arq.read_text(encoding="utf-8")
            corpo = texto.split("\n\n", 1)[1] if texto.startswith("# Fonte") else texto
            if re.search(r"qu[óo]rum", corpo, flags=re.I) and not PROCESSO.search(corpo):
                data = data_do_rotulo(ln["rotulo"], ln["id"]) or data_do_texto(corpo)
                reunioes.append({"ano_indice": ano_indice, "data": data.date().isoformat() if data is not None else None,
                                 "rotulo": ln["rotulo"], "arquivo": str(arq.relative_to(RAIZ)), "lido": True,
                                 "sem_quorum": True, "motivo": "reunião sem quórum"})
                continue
            if not re.search(r"deliberou|habilitad", corpo, flags=re.I):
                reunioes.append({"ano_indice": ano_indice, "rotulo": ln["rotulo"], "arquivo": str(arq.relative_to(RAIZ)),
                                 "lido": False, "motivo": "não é extrato de deliberação (calendário, portaria etc.)"})
                continue
            n = re.search(r"(\d{1,2})\s*[ºª°o]\s*REUNI", ln["rotulo"] + " " + corpo, flags=re.I)
            data = data_do_rotulo(ln["rotulo"], ln["id"]) or data_do_texto(corpo)
            # percorre o texto: cada cabeçalho de seção vale até o próximo; cada processo cai na seção corrente
            eventos = sorted([(m.start(), "secao", situacao(m.group(0))) for m in SECAO.finditer(corpo)] +
                             [(m.start(), "processo", f"{m.group(1)}-{m.group(2)}") for m in PROCESSO.finditer(corpo)])
            atual, vistos = None, set()
            for pos, tipo, valor in eventos:
                if tipo == "secao":
                    atual = valor
                    continue
                if atual is None or (valor, atual) in vistos:
                    continue
                vistos.add((valor, atual))
                delib.append({"ano_indice": ano_indice, "reuniao": int(n.group(1)) if n else None,
                              "data": data.date().isoformat() if data is not None else None, "processo": valor,
                              "situacao": atual, "natureza_proponente": natureza(corpo[pos:pos + 400]),
                              "arquivo": str(arq.relative_to(RAIZ))})
            cont = pd.Series([s for _, s in vistos]).value_counts() if vistos else pd.Series(dtype=int)
            reunioes.append({"ano_indice": ano_indice, "reuniao": int(n.group(1)) if n else None,
                             "data": data.date().isoformat() if data is not None else None, "rotulo": ln["rotulo"],
                             "arquivo": str(arq.relative_to(RAIZ)), "lido": True, "sem_quorum": False, "motivo": "",
                             **{f"n_{k}": int(v) for k, v in cont.items()}})
    return pd.DataFrame(delib), pd.DataFrame(reunioes)


def por_ano(d: pd.DataFrame, r: pd.DataFrame) -> pd.DataFrame:
    d = d.assign(ano=pd.to_datetime(d["data"]).dt.year.fillna(d["ano_indice"]).astype(int))
    linhas = []
    for ano, g in d.groupby("ano"):
        hab = set(g.loc[g.situacao == "habilitado", "processo"])
        inab = set(g.loc[g.situacao == "inabilitado", "processo"])
        linhas.append({
            "ano": ano,
            "extratos_lidos": int(r[(r.lido) & (pd.to_datetime(r["data"]).dt.year.fillna(r["ano_indice"]) == ano)].shape[0]),
            "reunioes_sem_quorum": int(r[(r.sem_quorum.fillna(False).astype(bool)) & (pd.to_datetime(r["data"]).dt.year.fillna(r["ano_indice"]) == ano)].shape[0]),
            "recursos_contra_inabilitacao": g.loc[g.situacao.str.startswith("recurso"), "processo"].nunique(),
            "habilitados": len(hab), "em_diligencia": g.loc[g.situacao == "em diligência", "processo"].nunique(),
            "inabilitados": len(inab), "nao_avaliados": g.loc[g.situacao == "não avaliado", "processo"].nunique(),
            "inabilitados_e_habilitados_no_ano": len(hab & inab),
            "taxa_inabilitacao": len(inab - hab) / len(hab | inab) if hab | inab else None,
            "outras_situacoes": "; ".join(sorted(set(g.situacao) - {"habilitado", "inabilitado", "em diligência", "não avaliado",
                                                                    "recurso contra inabilitação (apreciado)"})),
        })
    return pd.DataFrame(linhas)


def cobertura(d: pd.DataFrame) -> pd.DataFrame:
    h = pd.read_csv(PROC / "habilitados.csv").drop_duplicates(["ciclo", "numero_processo"])
    hab = set(d.loc[d.situacao == "habilitado", "processo"])
    alguma = set(d["processo"])
    inab = set(d.loc[d.situacao == "inabilitado", "processo"])
    linhas = []
    for ciclo, g in h.groupby("ciclo"):
        ps = set(g["numero_processo"])
        linhas.append({"ciclo": ciclo, "habilitados_lista_oficial": len(ps),
                       "habilitados_em_algum_extrato": len(ps & hab), "em_algum_extrato": len(ps & alguma),
                       "tambem_inabilitados_em_algum_extrato": len(ps & inab),
                       "cobertura": len(ps & hab) / len(ps)})
    return pd.DataFrame(linhas)


def main() -> None:
    d, r = ler_extratos()
    if d.empty:
        print("Nenhum extrato lido: rode o relé (etapa seguir) antes.")
        return
    d.to_csv(TAB / "12_cap_deliberacoes.csv", index=False)
    r.to_csv(TAB / "12_cap_reunioes.csv", index=False)
    a = por_ano(d, r)
    a.to_csv(TAB / "12_cap_status_por_ano.csv", index=False)
    c = cobertura(d)
    c.to_csv(TAB / "12_cap_cobertura.csv", index=False)
    print(f"extratos lidos: {int(r.lido.sum())} de {len(r)}; deliberações: {len(d)}")
    print(a.to_string(index=False))
    print(c.to_string(index=False))
    print(d.groupby("situacao")["natureza_proponente"].value_counts().unstack(fill_value=0).to_string())


if __name__ == "__main__":
    main()
