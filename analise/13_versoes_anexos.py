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


def versoes_captados() -> tuple[pd.DataFrame, pd.DataFrame]:
    man = {r["id"]: r for r in csv.DictReader((FW / "manifesto.csv").open(encoding="utf-8"))}
    linhas, fila = [], []
    atuais = {a: PAG / f"{pid}.txt" for a, pid in aud.ANEXOS.items()}
    for ano in range(2023, 2027):
        ids = sorted(k for k in man if k.startswith(f"versao_captados_{ano}_"))
        conjuntos = {}
        for pid in ids + [aud.ANEXOS[ano]]:
            reg = man.get(pid, {})
            arq = atuais[ano] if pid == aud.ANEXOS[ano] else PAG / f"{pid}.txt"
            if reg.get("status") != "200" or not arq.exists():
                linhas.append({"ano": ano, "versao": pid, "existe": False, "status": reg.get("status", "não pedido")})
                continue
            t = arq.read_text(encoding="utf-8")
            try:  # leitor por colunas do auditor (mesmo layout do ano); se a versão tiver outro layout, o genérico
                ts = [(x["cnpj"], x["valor"]) for x in aud.ler_anexo(ano, pid, man)["termos"]]
                leitor = "colunas (auditar_captacao.ler_anexo)"
            except Exception:  # noqa: BLE001
                ts, leitor = termos(t), "genérico (CNPJ + R$ na linha)"
            imp = [aud.d(x) for x in aud.IMPRESSO.findall(t)]
            ind = re.split(r"INDEFERIDOS POR ULTRAPASSAR", t, flags=re.I)
            linhas.append({"ano": ano, "versao": pid, "existe": True, "status": "200", "leitor": leitor, **cabecalho(t),
                           "termos": len(ts), "soma_termos": sum((v for _, v in ts), Decimal(0)),
                           "total_impresso": imp[-1] if imp else None,
                           "linhas_em_analise": len(re.findall(r"em an[áa]lise", t, flags=re.I)),
                           "tem_secao_indeferidos": len(ind) > 1,
                           "termos_indeferidos": len(termos(ind[1].replace("INDEFERIDOS", ""))) if len(ind) > 1 else 0,
                           "atual": pid == aud.ANEXOS[ano]})
            conjuntos[pid] = Counter((c[:8], v) for c, v in ts)
        # ordem das versões pela data de modificação do PDF (ou do servidor); sem data, fica fora da fila
        df = pd.DataFrame([l for l in linhas if l["ano"] == ano and l.get("existe")])
        if df.empty:
            continue
        df["ordem"] = pd.to_datetime(df["pdf_modificado"].fillna(df["servidor_last_modified"]), errors="coerce", utc=True)
        ordem = [v for v in df.sort_values("ordem")["versao"] if pd.notna(df.set_index("versao").loc[v, "ordem"])]
        todos = set().union(*[set(conjuntos[v]) for v in ordem]) if ordem else set()
        for chave in todos:
            presentes = [v for v in ordem if conjuntos[v][chave] > 0]
            fila.append({"ano": ano, "cnpj_raiz": chave[0], "valor": chave[1], "primeira_versao": presentes[0],
                         "ultima_versao": presentes[-1], "versoes_presentes": len(presentes), "versoes_datadas": len(ordem),
                         "na_versao_atual": conjuntos.get(aud.ANEXOS[ano], Counter())[chave] > 0})
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
    cols = [c for c in ("ano", "versao", "existe", "pdf_modificado", "termos", "soma_termos", "total_impresso",
                        "linhas_em_analise", "termos_indeferidos") if c in v]
    print(v[cols].to_string(index=False))
    if not h.empty:
        print(h[[c for c in ("versao", "existe", "pdf_modificado", "processos") if c in h]].to_string(index=False))


if __name__ == "__main__":
    main()
