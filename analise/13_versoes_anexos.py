"""
13 — Versões antigas dos anexos da LICC como fotografias da fila (rota alternativa à fila da SEFAZ por LAI).

O sistema de arquivos do site da SECULT não apaga o arquivo substituído: acrescenta um sufixo "(n)" ou "-n" ao novo
("RECURSO FINANCEIRO CAPTADO - 2025 (17).pdf", "lista-de-projetos-habilitados-15.pdf"). As versões anteriores
continuam no servidor e, lidas em ordem, mostram quando cada termo de patrocínio passou a constar como validado e
quando cada projeto entrou na lista de habilitados.

Fonte: textos coletados pelo relé (pedidos.tsv, ids versao_captados_AAAA_NN e versao_habilitados_NN), com as datas
do PDF (CreationDate, ModDate) e o Last-Modified do servidor no cabeçalho (analise/rede/buscar_fontes.py).

Leitura dos termos: o leitor por colunas de artigo/auditoria/auditar_captacao.py (ler_anexo), que a auditoria confere
termo a termo na versão atual. Se uma versão antiga tiver outro layout e o leitor falhar, usa-se o genérico (toda
linha com CNPJ seguido de valor em reais), e a coluna "leitor" registra qual foi usado.

Regras: versão que não existe (404) fica registrada como ausente; nenhum termo é inferido entre duas versões.

Saídas (analise/tabelas/):
  13_versoes_captados.csv       uma linha por versão: datas, termos, soma, total impresso, em análise, indeferidos
  13_versoes_captados_fila.csv  por ano, cada termo (CNPJ raiz × valor) com a primeira e a última versão em que aparece
  13_versoes_habilitados.csv    uma linha por versão da lista de habilitados: datas, processos, por ciclo
Uso: python analise/13_versoes_anexos.py
"""
from __future__ import annotations

import csv
import importlib.util
import re
from collections import Counter
from decimal import Decimal
from pathlib import Path

import pandas as pd

RAIZ = Path(__file__).resolve().parents[1]
FW = RAIZ / "dados" / "fontes_web"
PAG = FW / "paginas"
TAB = RAIZ / "analise" / "tabelas"

_spec = importlib.util.spec_from_file_location("aud", RAIZ / "artigo" / "auditoria" / "auditar_captacao.py")
aud = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(aud)

TERMO = re.compile(aud.CNPJ.pattern + r"[^\n]*?R\$\s*([\d.]+,\d{2})")
PROCESSO = re.compile(r"\b(20\d{2})\s*-\s*([0-9A-Z]{5})\b")


def cabecalho(texto: str) -> dict:
    cab = dict(re.findall(r"^# ([^:]+?): (.+)$", texto.split("\n\n", 1)[0], flags=re.M))
    return {"url": cab.get("Fonte"), "sha256": cab.get("sha256 do original"), "pdf_criado": cab.get("PDF CreationDate"),
            "pdf_modificado": cab.get("PDF ModDate"), "servidor_last_modified": cab.get("Last-Modified (servidor)")}


def termos(texto: str) -> list[tuple[str, Decimal]]:
    """(CNPJ do patrocinador, valor) de cada linha de termo antes da seção de indeferidos."""
    corpo = re.split(r"INDEFERIDOS POR ULTRAPASSAR", texto, flags=re.I)[0]
    saida = []
    for linha in corpo.splitlines():
        if aud.IGNORAR.search(linha) and not aud.CNPJ.search(linha):
            continue
        for m in TERMO.finditer(linha):
            saida.append((re.sub(r"\D", "", m.group(1)), aud.d(m.group(2))))
    return saida


# sufixo da versão atual de cada ano (analise: aud.ANEXOS); a versão sem sufixo é a primeira publicada
SUFIXO_ATUAL = {2023: 0, 2024: 6, 2025: 17, 2026: 2}
DATA = re.compile(r"(\d{2})/(\d{2})/(20\d{2})")


def ordem_da_versao(ano: int, pid: str) -> int:
    if pid == aud.ANEXOS[ano]:
        return SUFIXO_ATUAL[ano]
    fim = pid.rsplit("_", 1)[1]
    return 0 if fim == "base" else int(fim)


def data_maxima(texto: str) -> str | None:
    """Data de recebimento mais recente impressa na versão: a versão foi publicada nesse dia ou depois."""
    datas = [(int(a), int(m), int(d)) for d, m, a in DATA.findall(texto) if 1 <= int(m) <= 12 and 1 <= int(d) <= 31]
    return "%04d-%02d-%02d" % max(datas) if datas else None


def versoes_captados() -> tuple[pd.DataFrame, pd.DataFrame]:
    man = {r["id"]: r for r in csv.DictReader((FW / "manifesto.csv").open(encoding="utf-8"))}
    linhas, fila = [], []
    atuais = {a: PAG / f"{pid}.txt" for a, pid in aud.ANEXOS.items()}
    for ano in range(2023, 2027):
        ids = sorted(k for k in man if k.startswith(f"versao_captados_{ano}_"))
        validos, indeferidos, usar = {}, {}, []
        for pid in ids + [aud.ANEXOS[ano]]:
            reg = man.get(pid, {})
            arq = atuais[ano] if pid == aud.ANEXOS[ano] else PAG / f"{pid}.txt"
            base = {"ano": ano, "versao": pid, "ordem": ordem_da_versao(ano, pid)}
            if reg.get("status") != "200" or not arq.exists():
                linhas.append({**base, "existe": False, "status": reg.get("status", "não pedido")})
                continue
            t = arq.read_text(encoding="utf-8")
            partes = re.split(r"INDEFERIDOS POR ULTRAPASSAR", t, flags=re.I)
            gen = termos(t)
            try:  # leitor por colunas do auditor, calibrado no layout da versão atual do ano
                col = [(x["cnpj"], x["valor"]) for x in aud.ler_anexo(ano, pid, man)["termos"]]
            except Exception:  # noqa: BLE001
                col = None
            imp = [aud.d(x) for x in aud.IMPRESSO.findall(partes[0])]
            impresso = imp[-1] if imp else None
            soma = lambda ts: sum((v for _, v in ts), Decimal(0))  # noqa: E731
            # fica o leitor cuja soma bate com o total impresso da versão; sem total, o de colunas
            if col is not None and (impresso is None or soma(col) == impresso):
                ts, leitor = col, "colunas"
            elif impresso is not None and soma(gen) == impresso:
                ts, leitor = gen, "genérico"
            else:
                ts, leitor = (col if col is not None else gen), "inconsistente"
            ind = termos(partes[1]) if len(partes) > 1 else []
            linhas.append({**base, "existe": True, "status": "200", "leitor": leitor, **cabecalho(t),
                           "data_recebimento_mais_recente": data_maxima(partes[0]),
                           "termos": len(ts), "soma_termos": soma(ts), "total_impresso": impresso,
                           "termos_leitor_colunas": len(col) if col is not None else None,
                           "termos_leitor_generico": len(gen),
                           "linhas_em_analise": len(re.findall(r"em an[áa]lise", t, flags=re.I)),
                           "termos_indeferidos": len(ind), "soma_indeferidos": soma(ind),
                           "atual": pid == aud.ANEXOS[ano]})
            if leitor != "inconsistente":
                validos[pid] = Counter((c[:8], v) for c, v in ts)
                indeferidos[pid] = Counter((c[:8], v) for c, v in ind)
                usar.append(pid)
        # fila: versões consistentes, em ordem de sufixo (conferida com as datas de recebimento onde há datas)
        usar.sort(key=lambda v: ordem_da_versao(ano, v))
        chaves = set().union(*[set(validos[v]) | set(indeferidos[v]) for v in usar]) if usar else set()
        for chave in chaves:
            val = [v for v in usar if validos[v][chave] > 0]
            ind = [v for v in usar if indeferidos[v][chave] > 0]
            fila.append({"ano": ano, "cnpj_raiz": chave[0], "valor": chave[1],
                         "primeira_versao_validado": val[0] if val else None,
                         "ultima_versao_validado": val[-1] if val else None,
                         "versoes_validado": len(val), "primeira_versao_indeferido": ind[0] if ind else None,
                         "versoes_indeferido": len(ind), "versoes_consistentes": len(usar),
                         "indeferido_depois_validado": bool(ind and val and ordem_da_versao(ano, val[-1]) > ordem_da_versao(ano, ind[0])),
                         "validado_depois_retirado": bool(val and val[-1] != usar[-1]),
                         "na_versao_atual": validos.get(aud.ANEXOS[ano], Counter())[chave] > 0})
    return pd.DataFrame(linhas), pd.DataFrame(fila)


def conferir_leitor(v: pd.DataFrame) -> pd.DataFrame:
    """A leitura genérica precisa reproduzir o auditor por colunas na versão atual de cada ano."""
    ref = pd.read_csv(RAIZ / "artigo" / "auditoria" / "auditoria_captacao_anual.csv").set_index("ano_captacao")
    atual = v[v.get("atual", False) == True].set_index("ano")  # noqa: E712
    out = []
    for ano, r in atual.iterrows():
        out.append({"ano": ano, "termos_leitor": r["termos"], "termos_auditor": int(ref.loc[ano, "termos"]),
                    "soma_leitor": r["soma_termos"], "soma_auditor": Decimal(str(ref.loc[ano, "soma_termos"])),
                    "confere": int(r["termos"]) == int(ref.loc[ano, "termos"])
                    and abs(Decimal(str(r["soma_termos"])) - Decimal(str(ref.loc[ano, "soma_termos"]))) < Decimal("0.01")})
    return pd.DataFrame(out)


def versoes_habilitados() -> pd.DataFrame:
    man = {r["id"]: r for r in csv.DictReader((FW / "manifesto.csv").open(encoding="utf-8"))}
    linhas = []
    for pid in sorted(k for k in man if k.startswith("versao_habilitados_")):
        arq = PAG / f"{pid}.txt"
        if man[pid].get("status") != "200" or not arq.exists():
            linhas.append({"versao": pid, "existe": False, "status": man[pid].get("status")})
            continue
        t = arq.read_text(encoding="utf-8")
        procs = {f"{a}-{b}" for a, b in PROCESSO.findall(t)}
        linhas.append({"versao": pid, "existe": True, "status": "200", **cabecalho(t), "processos": len(procs),
                       **{f"processos_{a}": sum(p.startswith(str(a)) for p in procs) for a in range(2021, 2027)}})
    return pd.DataFrame(linhas)


def main() -> None:
    v, fila = versoes_captados()
    v.to_csv(TAB / "13_versoes_captados.csv", index=False)
    fila.to_csv(TAB / "13_versoes_captados_fila.csv", index=False)
    h = versoes_habilitados()
    h.to_csv(TAB / "13_versoes_habilitados.csv", index=False)
    print(conferir_leitor(v).to_string(index=False))
    cols = [c for c in ("ano", "ordem", "existe", "leitor", "data_recebimento_mais_recente", "termos", "soma_termos",
                        "total_impresso", "linhas_em_analise", "termos_indeferidos", "soma_indeferidos") if c in v]
    v = v.sort_values(["ano", "ordem"])
    print(v[cols].to_string(index=False))
    if not h.empty:
        print(h[[c for c in ("versao", "existe", "pdf_modificado", "processos") if c in h]].to_string(index=False))


if __name__ == "__main__":
    main()
