"""Auditoria independente da captação anual da LICC contra os anexos oficiais da SECULT.

Afirmação auditada (artigo, §1): "De 2023 a 2025, a captação esgotou o montante de cada ano ao centavo; em 2025,
63 projetos captaram, juntos, exatamente R$ 25.000.000,00."

O pipeline (analise/03f_captados_por_cota.py) lê só os totais que a SECULT imprime. Esta auditoria não confia neles:
refaz as contas termo a termo a partir do texto dos PDFs oficiais e cruza o resultado com todas as tabelas .csv do
repositório que carregam esses números.

Fontes primárias: anexos "RECURSO FINANCEIRO CAPTADO - {ano}" (secult.es.gov.br), baixados pelo relé e convertidos
com `pdftotext -layout` em dados/fontes_web/paginas/. O cabeçalho de cada .txt traz a URL e o sha256 do PDF, que
precisam bater com dados/fontes_web/manifesto.csv.

Como o valor é lido: no layout dos anexos, cada valor em reais cai numa coluna fixa. Por ano, fixam-se as faixas
de coluna do valor do termo (captado), do valor habilitado do projeto (2024-2026) e do total por projeto (2022-2023).
Todo "R$" fora dessas faixas é acusado. Cada termo precisa ter um CNPJ na mesma linha.

Conferências por ano:
  A. montante impresso no anexo × teto das portarias SEFAZ (dados/externos/licc_teto_vs_icms.csv)
  B. total impresso × soma dos termos recalculada
  C. soma dos termos × montante (esgotou?)
  D. número de projetos: valores na coluna do projeto (habilitado ou total por projeto)
  E. 2023: soma da coluna "valor total captado" (por projeto) × soma dos termos
  F. 2025: por cota, soma dos termos × "Total Captado" impresso; marcas "Em análise"
Conferências das tabelas .csv (2025 e anuais): 03f_captacao_anual_secult.csv, licc_captados_2025_totais.csv,
09_cotas_2025_2026.csv, dados/licc/oficial/captados-2025.csv (transcrição do licc.gov), dados/processados/
captados_2025.csv e aportes_2025.csv (termo a termo: CNPJ e valor).

Saídas: artigo/auditoria/auditoria_captacao_anual.csv  (uma linha por ano)
        artigo/auditoria/auditoria_captacao_checagens.csv (uma linha por conferência, com status)
        artigo/auditoria/auditoria_captacao_sensibilidade_2025.csv (estatísticas de patrocínio de 2025 com e sem o
        projeto "em análise na SEFAZ")
Uso:    python artigo/auditoria/auditar_captacao.py   (código de saída 1 se alguma conferência divergir)
"""
from __future__ import annotations

import csv
import hashlib
import re
import sys
from collections import Counter
from decimal import Decimal
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
PAG = RAIZ / "dados" / "fontes_web" / "paginas"
TAB = RAIZ / "analise" / "tabelas"
AQUI = Path(__file__).parent

ANEXOS = {
    2022: "secult_captados_2022_pdf",
    2023: "secult_captados_2023_pdf",
    2024: "secult_captados_2024_pdf",
    2025: "secult_captados_2025_v17_pdf",
    2026: "secult_captados_2026_pdf",
}
AFIRMACAO = (2023, 2024, 2025)  # anos cobertos pela frase do artigo; 2022 e 2026 entram como contraste
# faixas de coluna (início do "R$" na linha do pdftotext -layout)
FAIXAS = {
    2022: {"termo": (85, 105), "projeto_total": (105, 125)},
    2023: {"termo": (90, 110), "projeto_total": (110, 130)},
    2024: {"habilitado": (30, 60), "termo": (95, 120)},
    2025: {"habilitado": (40, 65), "termo": (100, 135)},
    2026: {"habilitado": (25, 55), "termo": (95, 130)},
}
REAIS = re.compile(r"R\$\s*([\d.]+,\d{2})")
CNPJ = re.compile(r"(\d{2}[.\s-]?\d{3}[.\s-]?\d{3}\s*[./-]?\s*\d{4}\s*[-/.]?\s*\d{2})")
INICIO_VALIDADOS = re.compile(r"VALIDADOS PELA SEFAZ")
# rodapé de página do pdftotext em 2022-2023 ("20/11/2023      1"): o total do projeto que atravessa a página se repete
QUEBRA = re.compile(r"^\s*\d{2}/\d{2}/\d{4}\s+\d+\s*$")
MONTANTE_SOMA = re.compile(r"=\s*R\$[\s\S]{0,400}?([\d.]+,\d{2})")
COTA = re.compile(r"^\s*(IV|III|II|I)\s*-\s*\d+%\s*serão destinados")
MONTANTE = re.compile(r"Montante de recursos financeiros dispon[ií]veis.*?ano (\d{4})\s+R\$\s*([\d.]+,\d{2})")
IMPRESSO = re.compile(r"(?:TOTAL:|Total Geral Captado:?)\s*R\$\s*([\d.]+,\d{2})")
TOTAL_COTA = re.compile(r"Total Captado:\s*R\$\s*([\d.]+,\d{2})")
FIM_VALIDADOS = re.compile(r"INDEFERIDOS POR ULTRAPASSAR", flags=re.I)
IGNORAR = re.compile(r"TOTAL|Total|Saldo|Valor|Montante|remanejado|recebido da cota")

checagens: list[dict] = []


def d(txt: str) -> Decimal:
    return Decimal(txt.replace(".", "").replace(",", "."))


def dec(x) -> Decimal:
    return Decimal(str(x)).quantize(Decimal("0.01"))


def br(x: Decimal | None) -> str:
    if x is None:
        return "-"
    s = f"{x:,.2f}"
    return s.replace(",", "_").replace(".", ",").replace("_", ".")


def checa(cid: str, ano, descricao: str, esperado, obtido, fonte: str) -> bool:
    ok = esperado == obtido
    checagens.append({"id": cid, "ano": ano, "descricao": descricao, "esperado": esperado, "obtido": obtido,
                      "status": "confere" if ok else "DIVERGE", "fonte": fonte})
    return ok


def manifesto() -> dict[str, dict]:
    with (RAIZ / "dados" / "fontes_web" / "manifesto.csv").open(encoding="utf-8") as f:
        return {r["id"]: r for r in csv.DictReader(f)}


def ler_csv(caminho: Path) -> list[dict]:
    # sem comment="#": há títulos de projeto que começam com "#" ("#EP10 - ENCONTRO DAS PRETAS")
    with caminho.open(encoding="utf-8") as f:
        linhas = [l for l in f if not l.startswith("# ")]
    return list(csv.DictReader(linhas))


def ler_anexo(ano: int, pid: str, man: dict) -> dict:
    arq = PAG / f"{pid}.txt"
    texto = arq.read_text(encoding="utf-8")
    cab = dict(re.findall(r"^# (Fonte|sha256 do original): (\S+)", texto, flags=re.M))
    reg = man[pid]
    checa("P1", ano, "URL do .txt = URL do manifesto do relé", reg["url"], cab.get("Fonte"), str(arq.relative_to(RAIZ)))
    checa("P2", ano, "sha256 do PDF no .txt = manifesto", reg["sha256"], cab.get("sha256 do original"),
          "dados/fontes_web/manifesto.csv")

    linhas = texto.splitlines()
    fim = next((i for i, l in enumerate(linhas) if FIM_VALIDADOS.search(l)), len(linhas))
    inicio = next(i for i, l in enumerate(linhas) if INICIO_VALIDADOS.search(l))
    # antes do título "validados" só há o cabeçalho (montante); em 2026 ele traz "R$ 25 mi + R$ 6 mi" na coluna do termo
    validados = [("#" if i < inicio else "") + l for i, l in enumerate(linhas[:fim])]
    faixas = FAIXAS[ano]
    termos, projetos, fora, cotas, repetidos = [], [], [], {}, []
    cota, quebra = None, False
    for i, l in enumerate(validados):
        if l.startswith("#"):
            continue
        if QUEBRA.match(l):
            quebra = True
            continue
        m = COTA.match(l)
        if m:
            cota = m.group(1)
            cotas[cota] = {"termos": [], "impresso": None}
            continue
        t = TOTAL_COTA.search(l)
        if t and cota:
            cotas[cota]["impresso"] = d(t.group(1))
        if IGNORAR.search(l) or (cota and re.fullmatch(r"\s*R\$\s*[\d.]+,\d{2}\s*", l) and i > 0
                                 and "serão destinados" in validados[i - 1]):
            continue  # totais, saldos e o valor reservado da cota
        for m in REAIS.finditer(l):
            col, v = m.start(), d(m.group(1))
            if faixas["termo"][0] <= col < faixas["termo"][1]:
                cnpj = CNPJ.findall(l[:col])
                if not cnpj:  # CNPJ quebrado na linha de cima ou de baixo
                    cnpj = CNPJ.findall(validados[i - 1]) or CNPJ.findall(validados[i + 1])
                termos.append({"linha": i + 1, "valor": v, "cota": cota,
                               "cnpj": re.sub(r"\D", "", cnpj[-1]) if cnpj else ""})
                if cota:
                    cotas[cota]["termos"].append(v)
            elif any(faixas[k][0] <= col < faixas[k][1] for k in ("habilitado", "projeto_total") if k in faixas):
                if quebra and projetos and projetos[-1]["valor"] == v:
                    repetidos.append({"linha": i + 1, "valor": v})  # mesmo projeto, reimpresso na página seguinte
                else:
                    projetos.append({"linha": i + 1, "valor": v})
                quebra = False
            else:
                fora.append((i + 1, col, m.group(0)))
    mont = MONTANTE.search(texto)
    if mont:
        mont_ano, mont_valor = int(mont.group(1)), d(mont.group(2))
    else:  # 2026: "R$ 25.000.000 + R$ 6.000.000,00 = R$ / 31.000.000,00", em linhas separadas
        cab_txt = "\n".join(linhas[:inicio])
        ano_m, soma_m = re.search(r"ano (\d{4})", cab_txt), MONTANTE_SOMA.search(cab_txt)
        mont_ano = int(ano_m.group(1)) if ano_m else None
        mont_valor = d(soma_m.group(1)) if soma_m else None
    impressos = [d(x) for x in IMPRESSO.findall("\n".join(validados))]
    em_analise = [i + 1 for i, l in enumerate(validados) if re.search(r"em an[áa]lise", l, flags=re.I)]
    return {"ano": ano, "arquivo": str(arq.relative_to(RAIZ)), "url": reg["url"], "sha256": reg["sha256"],
            "montante_ano": mont_ano, "montante": mont_valor,
            "impresso": impressos[-1] if impressos else None, "termos": termos, "projetos": projetos,
            "fora_da_faixa": fora, "cotas": cotas, "repetidos": repetidos, "linhas_em_analise": em_analise}


def sensibilidade_2025(sem: set[str]) -> list[dict]:
    """Estatísticas de patrocínio de 2025 citadas no artigo, com o anexo inteiro e sem os projetos em análise."""
    ap = ler_csv(RAIZ / "dados" / "processados" / "aportes_2025.csv")
    macro = {r["cnpj_raiz"]: r["macrossetor"] for r in ler_csv(TAB / "03_patrocinadores.csv")}
    rou: dict[str, bool] = {}
    for r in ler_csv(TAB / "07_patrocinadores_na_rouanet.csv"):
        rou[r["cnpj_raiz"]] = rou.get(r["cnpj_raiz"], False) or r["incentivador_rouanet"] == "True"
    saida = []
    for base, linhas in (("anexo inteiro", ap), ("sem projetos em análise", [r for r in ap if r["id_captado"] not in sem])):
        por_emp: Counter = Counter()
        for r in linhas:
            por_emp[r["cnpj_raiz"]] += dec(r["valor"])
        tot = sum(por_emp.values(), Decimal(0))
        ordem = [v for _, v in por_emp.most_common()]
        acum, para_metade = Decimal(0), 0
        for v in ordem:
            acum += v
            para_metade += 1
            if acum >= tot / 2:
                break
        energia = sum((v for k, v in por_emp.items() if macro.get(k) == "Energia e gás (serviço regulado)"), Decimal(0))
        rouanet = [k for k in por_emp if rou.get(k)]
        saida.append({"base": base, "projetos": len({r["id_captado"] for r in linhas}), "soma": tot,
                      "empresas": len(por_emp), "estabelecimentos": len({r["cnpj"] for r in linhas}),
                      "empresas_para_metade": para_metade, "maior_empresa": round(ordem[0] / tot, 4),
                      "energia_e_gas": round(energia / tot, 4), "empresas_rouanet": len(rouanet),
                      "renuncia_das_empresas_rouanet": round(sum((por_emp[k] for k in rouanet), Decimal(0)) / tot, 4)})
    return saida


def main() -> int:
    man = manifesto()
    teto = {int(r["ano_teto"]): Decimal(r["teto_renuncia"])
            for r in ler_csv(RAIZ / "dados" / "externos" / "licc_teto_vs_icms.csv")}
    f03 = {int(r["ano_captacao"]): r for r in ler_csv(TAB / "03f_captacao_anual_secult.csv")}
    anexos = {ano: ler_anexo(ano, pid, man) for ano, pid in ANEXOS.items()}

    anual = []
    for ano, a in anexos.items():
        soma = sum((t["valor"] for t in a["termos"]), Decimal(0))
        soma_proj = sum((p["valor"] for p in a["projetos"]), Decimal(0))
        fonte = a["arquivo"]
        checa("L1", ano, "nenhum R$ fora das colunas previstas (leitura completa)", 0, len(a["fora_da_faixa"]), fonte)
        checa("L2", ano, "todo termo tem CNPJ de 14 dígitos (na linha ou na vizinha)", len(a["termos"]),
              sum(len(t["cnpj"]) == 14 for t in a["termos"]), fonte)
        checa("A1", ano, "ano do montante impresso = ano do anexo", ano, a["montante_ano"], fonte)
        checa("B1", ano, "total impresso = soma dos termos recalculada", a["impresso"], soma, fonte)
        if ano in AFIRMACAO:
            checa("A2", ano, "montante impresso = teto das portarias SEFAZ", teto.get(ano), a["montante"],
                  "dados/externos/licc_teto_vs_icms.csv")
            checa("C1", ano, "soma dos termos = montante (esgotou ao centavo)", a["montante"], soma, fonte)
            checa("X1", ano, "03f: montante_declarado = montante impresso", a["montante"],
                  dec(f03[ano]["montante_declarado"]), "analise/tabelas/03f_captacao_anual_secult.csv")
            checa("X2", ano, "03f: total_validado = soma dos termos", soma, dec(f03[ano]["total_validado"]),
                  "analise/tabelas/03f_captacao_anual_secult.csv")
        if "projeto_total" in FAIXAS[ano]:
            checa("E1", ano, "soma da coluna 'valor total captado' (por projeto) = soma dos termos", soma, soma_proj, fonte)
        for c, v in a["cotas"].items():
            checa("F1", ano, f"cota {c}: 'Total Captado' impresso = soma dos termos da cota", v["impresso"],
                  sum(v["termos"], Decimal(0)), fonte)
        anual.append({
            "ano_captacao": ano, "na_afirmacao": ano in AFIRMACAO,
            "teto_portarias_sefaz": teto.get(ano), "montante_impresso": a["montante"], "total_impresso": a["impresso"],
            "soma_termos": soma, "termos": len(a["termos"]), "projetos": len(a["projetos"]),
            "totais_repetidos_apos_quebra": len(a["repetidos"]),
            "coluna_projeto": "habilitado" if "habilitado" in FAIXAS[ano] else "valor total captado",
            "soma_coluna_projeto": soma_proj, "esgotou_montante": (soma == a["montante"]) if a["montante"] is not None else None,
            "saldo": (a["montante"] - soma) if a["montante"] is not None else None,
            "linhas_em_analise": ";".join(map(str, a["linhas_em_analise"])),
            # 2023-2024: nenhuma marca; 2026 marca "em análise" só por cor, que o texto do PDF não guarda
            "projetos_em_analise": 0 if ano in (2022, 2023, 2024) else None, "valor_em_analise": Decimal(0)
            if ano in (2022, 2023, 2024) else None,
            "projetos_validados": len(a["projetos"]) if ano in (2022, 2023, 2024) else None,
            "soma_validados": soma if ano in (2022, 2023, 2024) else None,
            "fonte_url": a["url"], "sha256_pdf": a["sha256"], "arquivo_texto": a["arquivo"],
        })

    # ---------------------------------------------------------------- 2025: o número do artigo e as tabelas .csv
    a25 = anexos[2025]
    termos25 = Counter((t["cnpj"], t["valor"]) for t in a25["termos"])
    hab25 = Counter(p["valor"] for p in a25["projetos"])
    soma25 = sum((t["valor"] for t in a25["termos"]), Decimal(0))
    checa("G1", 2025, "projetos no anexo (valores na coluna 'valor habilitado')", 63, len(a25["projetos"]), a25["arquivo"])
    checa("G2", 2025, "termos no anexo", 95, len(a25["termos"]), a25["arquivo"])

    tot = ler_csv(TAB / "licc_captados_2025_totais.csv")[0]
    checa("T1", 2025, "licc_captados_2025_totais.csv: projetos = anexo", len(a25["projetos"]), int(tot["projetos"]),
          "analise/tabelas/licc_captados_2025_totais.csv")
    checa("T2", 2025, "licc_captados_2025_totais.csv: soma captada = anexo", soma25, dec(tot["soma_valor_captado"]),
          "analise/tabelas/licc_captados_2025_totais.csv")
    checa("T3", 2025, "licc_captados_2025_totais.csv: soma habilitada = anexo",
          sum(hab25.elements(), Decimal(0)), dec(tot["soma_valor_autorizado"]), "analise/tabelas/licc_captados_2025_totais.csv")

    lg = ler_csv(RAIZ / "dados" / "licc" / "oficial" / "captados-2025.csv")
    f_lg = "dados/licc/oficial/captados-2025.csv"
    checa("T4", 2025, "transcrição licc.gov: linhas (projetos) = anexo", len(a25["projetos"]), len(lg), f_lg)
    checa("T5", 2025, "transcrição licc.gov: projetos distintos (título) = linhas", len(lg), len({r["projeto"] for r in lg}), f_lg)
    checa("T6", 2025, "transcrição licc.gov: soma de valor_captado = anexo", soma25,
          sum((dec(r["valor_captado"]) for r in lg), Decimal(0)), f_lg)
    checa("T7", 2025, "transcrição licc.gov: valores habilitados (multiconjunto) = anexo", True,
          Counter(dec(r["valor_autorizado"]) for r in lg) == hab25, f_lg)
    ap_lg = Counter()
    for r in lg:
        for ap in r["aportes"].split(";"):
            cnpj, _, valor = ap.strip().split("|")
            ap_lg[(re.sub(r"\D", "", cnpj), dec(valor))] += 1
    checa("T8", 2025, "transcrição licc.gov: termos (CNPJ, valor) = anexo, um a um", True, ap_lg == termos25, f_lg)
    checa("T9", 2025, "transcrição licc.gov: soma dos aportes de cada projeto = valor_captado", len(lg),
          sum(sum((dec(ap.split("|")[2]) for ap in r["aportes"].split(";")), Decimal(0)) == dec(r["valor_captado"])
              for r in lg), f_lg)

    pc = ler_csv(RAIZ / "dados" / "processados" / "captados_2025.csv")
    f_pc = "dados/processados/captados_2025.csv"
    checa("T10", 2025, "captados_2025.csv: linhas = anexo", len(a25["projetos"]), len(pc), f_pc)
    checa("T11", 2025, "captados_2025.csv: soma de valor_captado = anexo", soma25,
          sum((dec(r["valor_captado"]) for r in pc), Decimal(0)), f_pc)
    ap = ler_csv(RAIZ / "dados" / "processados" / "aportes_2025.csv")
    f_ap = "dados/processados/aportes_2025.csv"
    checa("T12", 2025, "aportes_2025.csv: termos (CNPJ, valor) = anexo, um a um", True,
          Counter((re.sub(r"\D", "", r["cnpj"]), dec(r["valor"])) for r in ap) == termos25, f_ap)
    checa("T13", 2025, "aportes_2025.csv: projetos distintos (id_captado) = anexo", len(a25["projetos"]),
          len({r["id_captado"] for r in ap}), f_ap)

    c09 = {r["cota"]: r for r in ler_csv(TAB / "09_cotas_2025_2026.csv") if r["ano_captacao"].startswith("2025")}
    romano = {"1.0": "I", "2.0": "II", "3.0": "III", "4.0": "IV"}
    for k, r in c09.items():
        c = romano[k]
        checa("T14", 2025, f"09_cotas_2025_2026.csv: cota {c}, soma lida = auditoria",
              sum(a25["cotas"][c]["termos"], Decimal(0)), dec(r["soma_lida"]), "analise/tabelas/09_cotas_2025_2026.csv")

    # "Em análise na SEFAZ": o anexo se intitula "termos validados", mas marca um projeto como ainda em análise
    em_an = [r for r in lg if re.search(r"em an[áa]lise", r["proponente"], flags=re.I)]
    checa("H1", 2025, "marcas 'Em análise' no anexo = projetos marcados na transcrição", len(a25["linhas_em_analise"]),
          len(em_an), a25["arquivo"])
    for r in em_an:
        linha = a25["linhas_em_analise"][0]
        perto = Counter((t["cnpj"], t["valor"]) for t in a25["termos"] if abs(t["linha"] - linha) <= 10)
        seus = Counter((re.sub(r"\D", "", x.split("|")[0]), dec(x.split("|")[2])) for x in r["aportes"].split(";"))
        checa("H2", 2025, "termos do projeto em análise estão junto da marca no anexo", True, not (seus - perto),
              a25["arquivo"])
        checa("H3", 2025, "soma dos termos do projeto em análise = valor_captado transcrito",
              dec(r["valor_captado"]), sum((v for (_, v) in seus.elements()), Decimal(0)), f_lg)
    v_an = sum((dec(r["valor_captado"]) for r in em_an), Decimal(0))
    linha25 = next(r for r in anual if r["ano_captacao"] == 2025)
    linha25.update({"projetos_em_analise": len(em_an), "valor_em_analise": v_an,
                    "projetos_validados": len(a25["projetos"]) - len(em_an), "soma_validados": soma25 - v_an})

    sens = sensibilidade_2025({r["id_captado"] for r in ler_csv(RAIZ / "dados" / "processados" / "captados_2025.csv")
                               if re.search(r"em an[áa]lise", r["proponente"], flags=re.I)})
    with (AQUI / "auditoria_captacao_sensibilidade_2025.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(sens[0]))
        w.writeheader()
        w.writerows(sens)

    # ---------------------------------------------------------------- a frase no artigo
    art = (RAIZ / "artigo" / "rascunho-artigo.md").read_text(encoding="utf-8")
    frase = re.search(r"De 2023 a 2025,[^\n]*?2025[^\n]*?R\\\$ 25", art)
    checa("M1", "-", "a frase auditada está no artigo", True, bool(frase), "artigo/rascunho-artigo.md")

    # ---------------------------------------------------------------- saídas
    with (AQUI / "auditoria_captacao_anual.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(anual[0]))
        w.writeheader()
        w.writerows(anual)
    with (AQUI / "auditoria_captacao_checagens.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["id", "ano", "descricao", "esperado", "obtido", "status", "fonte"])
        w.writeheader()
        w.writerows(checagens)

    print(f"{'ano':<5}{'teto SEFAZ':>16}{'montante':>16}{'total impresso':>16}{'soma termos':>16}"
          f"{'termos':>7}{'proj.':>6}  esgotou")
    for r in anual:
        print(f"{r['ano_captacao']:<5}{br(r['teto_portarias_sefaz']):>16}"
              f"{br(r['montante_impresso']):>16}{br(r['total_impresso']):>16}{br(r['soma_termos']):>16}"
              f"{r['termos']:>7}{r['projetos']:>6}  { {True: 'sim', False: 'não', None: 'sem montante impresso'}[r['esgotou_montante']]}"
              f"{'' if r['na_afirmacao'] else '  (fora da frase)'}")
    print(f"\n2025: {len(em_an)} projeto marcado 'Em análise na SEFAZ' no anexo, com R$ {br(v_an)} em "
          f"{sum(len(r['aportes'].split(';')) for r in em_an)} termos; sem ele: {len(lg) - len(em_an)} projetos e "
          f"R$ {br(soma25 - v_an)}.")
    diverge = [c for c in checagens if c["status"] != "confere"]
    print(f"\n{len(checagens) - len(diverge)}/{len(checagens)} conferências batem.")
    for c in diverge:
        print(f"  DIVERGE {c['id']} {c['ano']}: {c['descricao']} — esperado {c['esperado']}, obtido {c['obtido']}")
    for a in anexos.values():
        for linha, col, txt in a["fora_da_faixa"]:
            print(f"  fora da faixa: {a['ano']} linha {linha}, coluna {col}: {txt}")
    return 1 if diverge else 0


if __name__ == "__main__":
    sys.exit(main())
