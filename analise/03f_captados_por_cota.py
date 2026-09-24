"""
03f — Captação da LICC por cota do art. 18, como a própria SECULT imprime nos anexos
"RECURSO FINANCEIRO CAPTADO - {ano}".

Os anexos são seccionados por cota (desde a IN 001/2025): cada seção abre com o texto do inciso e
o valor reservado ("IV - 50% serão destinados aos demais projetos. Valor: R$ 12.500.000,00") e fecha
com "Total Captado: R$ ...". O documento termina com "Total Geral Captado". Este script lê só esses
totais impressos — não atribui projeto a cota — a partir do texto extraído pelo relé
(`pdftotext -layout`, em dados/fontes_web/paginas/, com URL e sha256 no manifesto).

Leitura: captado ÷ reservado mede quanto cada reserva captou. Não mede descumprimento: o art. 18,
§ 1º, manda aplicar a cota IV quando I a III se esgotam, e o § 2º permite remanejar sobras a critério
da SECULT (regra 3 do CLAUDE.md: ler a norma não basta para apurar cumprimento).

Também grava, por ano, o montante que o anexo declara disponível, o total de termos de patrocínio
validados pela SEFAZ (captação) e o total de termos "indeferidos por ultrapassar o montante" — seção que
os anexos de 2023 e 2024 publicam e que é evidência direta de racionamento pelo teto.

Saídas: analise/tabelas/03f_captados_por_cota.csv
        analise/tabelas/03f_captacao_anual_secult.csv
Uso:   python analise/03f_captados_por_cota.py
"""
from __future__ import annotations

import csv
import re
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
PAG = RAIZ / "dados" / "fontes_web" / "paginas"
MANIFESTO = RAIZ / "dados" / "fontes_web" / "manifesto.csv"
SAIDA = RAIZ / "analise" / "tabelas" / "03f_captados_por_cota.csv"

# ano de captação -> id no manifesto do relé (a versão mais recente de cada anexo)
ANEXOS = {
    2022: "secult_captados_2022_pdf",
    2023: "secult_captados_2023_pdf",
    2024: "secult_captados_2024_pdf",
    2025: "secult_captados_2025_v17_pdf",
    2026: "secult_captados_2026_pdf",
}
COTA = re.compile(r"^\s*(IV|III|II|I)\s*-\s*(\d+)%\s*serão destinados")
VALOR = re.compile(r"Valor:?\s*R\$\s*([\d.]+,\d{2})")
MONTANTE = re.compile(r"Montante de recursos financeiros dispon[ií]veis.*?ano (\d{4})\s+R\$\s*([\d.]+,\d{2})")
TOTAL_SIMPLES = re.compile(r"TOTAL:\s*R\$\s*([\d.]+,\d{2})")
TOTAL = re.compile(r"Total Captado:\s*R\$\s*([\d.]+,\d{2})")
GERAL = re.compile(r"Total Geral Captado:?\s*R\$\s*([\d.]+,\d{2})")


def reais(txt: str) -> float:
    return float(txt.replace(".", "").replace(",", "."))


def manifesto() -> dict[str, dict]:
    with MANIFESTO.open(encoding="utf-8") as f:
        return {r["id"]: r for r in csv.DictReader(f)}


def ler(ano: int, pid: str, man: dict) -> list[dict]:
    arq = PAG / f"{pid}.txt"
    reg = man.get(pid, {})
    base = {"ano_captacao": ano, "fonte_url": reg.get("url", ""), "sha256_pdf": reg.get("sha256", ""),
            "coletado_utc": reg.get("coletado_utc", ""), "arquivo_texto": str(arq.relative_to(RAIZ))}
    if not arq.exists() or reg.get("status") != "200":
        return [{**base, "cota": "", "status": f"anexo não coletado (HTTP {reg.get('status', '?')})"}]
    linhas = arq.read_text(encoding="utf-8").splitlines()
    saida, atual, geral = [], None, None
    for i, l in enumerate(linhas):
        m = COTA.match(l)
        if m:
            # o "Valor:" do teto da cota pode cair na linha seguinte (texto longo do inciso)
            v = VALOR.search(" ".join(x.strip() for x in linhas[i:i + 3]))
            atual = {**base, "cota": m.group(1), "pct_reserva": int(m.group(2)),
                     "reservado": reais(v.group(1)) if v else None, "captado": None}
            saida.append(atual)
            continue
        t = TOTAL.search(l)
        if t and atual is not None and atual["captado"] is None:
            atual["captado"] = reais(t.group(1))
        g = GERAL.search(l)
        if g:
            geral = reais(g.group(1))
    if not saida:
        return [{**base, "cota": "", "total_geral": geral,
                 "status": "anexo sem seções por cota (antes da IN 001/2025)" if geral is not None
                 else "sem seções por cota e sem total geral legível"}]
    for s in saida:
        s["total_geral"] = geral
        s["captado_sobre_reservado"] = (s["captado"] / s["reservado"]) if s["captado"] and s["reservado"] else None
        s["status"] = "ok" if s["captado"] is not None and s["reservado"] is not None else "total ausente"
    soma = sum(s["captado"] or 0 for s in saida)
    if geral is not None and abs(soma - geral) > 0.005:
        for s in saida:
            s["status"] += f"; soma das cotas {soma:.2f} ≠ total geral {geral:.2f}"
    return saida


def anual(ano: int, pid: str, man: dict) -> dict:
    """Montante declarado, total validado e total indeferido, como impressos no anexo."""
    arq = PAG / f"{pid}.txt"
    reg = man.get(pid, {})
    out = {"ano_captacao": ano, "montante_declarado": None, "total_validado": None, "total_indeferido": None,
           "fonte_url": reg.get("url", ""), "sha256_pdf": reg.get("sha256", "")}
    if not arq.exists() or reg.get("status") != "200":
        out["status"] = "anexo não coletado"
        return out
    texto = arq.read_text(encoding="utf-8")
    m = MONTANTE.search(texto)
    if m:
        out["montante_declarado"] = reais(m.group(2))
        out["ano_declarado"] = int(m.group(1))
    g = GERAL.search(texto)
    partes = re.split(r"INDEFERIDOS POR ULTRAPASSAR", texto, flags=re.I)
    totais_validos = [reais(x) for x in TOTAL_SIMPLES.findall(partes[0])]
    out["total_validado"] = reais(g.group(1)) if g else (totais_validos[-1] if totais_validos else None)
    if len(partes) > 1:
        t = TOTAL_SIMPLES.findall(partes[1])
        # valores da coluna mais à direita (valor do termo); em 2023 a soma reproduz o total impresso
        achados = [(m.start(), reais(m.group(1))) for l in partes[1].splitlines() if "TOTAL" not in l
                   for m in re.finditer(r"R\$\s*([\d.]+,\d{2})", l)]
        direita = max((p for p, _ in achados), default=0)
        termos = [v for p, v in achados if p >= direita - 15]
        out["termos_indeferidos"] = len(termos)
        out["soma_termos_indeferidos"] = round(sum(termos), 2)
        out["total_indeferido"] = reais(t[0]) if t else round(sum(termos), 2)
        out["origem_total_indeferido"] = "impresso no anexo" if t else "soma calculada da coluna do termo"
    out["status"] = "ok"
    return out


def main() -> None:
    man = manifesto()
    anos = [anual(a, p, man) for a, p in ANEXOS.items()]
    # renúncia efetiva (termos validados) ÷ gasto estadual empenhado na função cultura do mesmo ano (SICONFI)
    f13 = {}
    with (RAIZ / "dados" / "externos" / "licc_teto_vs_icms.csv").open(encoding="utf-8") as f:
        for r in csv.DictReader(l for l in f if not l.startswith("#")):
            if r.get("f13_estado_emp_mesmo_ano"):
                f13[int(r["ano_teto"])] = float(r["f13_estado_emp_mesmo_ano"])
    for a in anos:
        g = f13.get(a["ano_captacao"])
        a["f13_estado"] = g
        a["validado_sobre_f13_estado"] = (a["total_validado"] / g) if g and a["total_validado"] else None
        a["indeferido_sobre_montante"] = ((a["total_indeferido"] / a["montante_declarado"])
                                          if a.get("total_indeferido") and a.get("montante_declarado") else None)
    with (SAIDA.parent / "03f_captacao_anual_secult.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["ano_captacao", "ano_declarado", "montante_declarado", "total_validado",
                                          "total_indeferido", "termos_indeferidos", "soma_termos_indeferidos",
                                          "origem_total_indeferido", "indeferido_sobre_montante", "f13_estado",
                                          "validado_sobre_f13_estado", "status", "fonte_url", "sha256_pdf"], extrasaction="ignore")
        w.writeheader()
        w.writerows(anos)
    for a in anos:
        print("anual", a["ano_captacao"], a.get("montante_declarado"), a["total_validado"], a["total_indeferido"], a["status"])
    linhas = []
    for ano, pid in ANEXOS.items():
        linhas.extend(ler(ano, pid, man))
    campos = ["ano_captacao", "cota", "pct_reserva", "reservado", "captado", "captado_sobre_reservado",
              "total_geral", "status", "fonte_url", "sha256_pdf", "coletado_utc", "arquivo_texto"]
    with SAIDA.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=campos, extrasaction="ignore")
        w.writeheader()
        w.writerows(linhas)
    for l in linhas:
        print(l["ano_captacao"], l.get("cota"), l.get("reservado"), l.get("captado"),
              round(l["captado_sobre_reservado"], 3) if l.get("captado_sobre_reservado") else "", l.get("total_geral"), l["status"])
    print(SAIDA.relative_to(RAIZ))


if __name__ == "__main__":
    main()
