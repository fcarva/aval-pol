"""
16 — Termos da LICC no Portal da Transparência do ES: processo, data, patrocinador, proponente (com CNPJ) e valor.

Fonte: Portal da Transparência do Governo do ES, "Incentivos, isenções e beneficiários", seção 07, "Projetos
beneficiados pela Lei de Incentivo à Cultura Capixaba" (planilhas ODS de 2022 a 2025), coletadas pelo relé e
convertidas em CSV por aba (analise/rede/buscar_fontes.py):
  dados/fontes_web/paginas/transp377_378.txt  (2022)   https://transparencia.es.gov.br/Comum/incentivosfiscais/Download/378
  dados/fontes_web/paginas/transp377_379.txt  (2023)   .../Download/379
  dados/fontes_web/paginas/transp377_439.txt  (2024)   .../Download/439
  dados/fontes_web/paginas/transp377_536.txt  (2025)   .../Download/536
Só a aba "DADOS" é lida; as abas de gráfico (tabelas dinâmicas) e de legislação ficam de fora.

O que o dado é (e não é):
- uma linha por termo de patrocínio (patrocinador × projeto), com o número do processo da SECULT, a "data do processo",
  o CNPJ do patrocinador e do proponente e o valor "oferecido";
- a "data do processo" não é definida na planilha. A ordem das linhas segue essa data, e o total fecha no montante do
  ano, o que sugere a data de protocolo do termo (a fila). Isso é hipótese, não fato: fica "indeterminado" até a
  SEFAZ confirmar;
- linhas de continuação (outro patrocinador do mesmo projeto) vêm com processo, data ou projeto em branco. Herdam-nos
  da linha anterior, e a herança fica marcada (campo "herdado");
- termo com valor zero fica na tabela e marcado ("valor_zero"); não é somado como patrocínio;
- CNPJ com dígito verificador inválido fica como está e marcado ("cnpj_*_dv_ok" = False).

Saídas:
  dados/processados/transparencia_licc_termos.csv  um termo por linha (ano de captação = ano da planilha)
  analise/tabelas/16_transparencia_resumo.csv      por ano: termos, soma, total impresso, limite impresso, projetos,
                                                   proponentes e patrocinadores (CNPJ), comparação com o anexo da SECULT
  analise/tabelas/16_transparencia_x_anexo.csv     por ano: termos que casam com o anexo "Recurso financeiro captado"
                                                   pela chave (CNPJ do patrocinador, valor), e os que sobram de cada lado
  analise/tabelas/16_fila_por_mes.csv              por ano e mês da "data do processo": termos e valor acumulado
  analise/tabelas/16_pares_recorrentes.csv         pares patrocinador (raiz do CNPJ) × proponente (CNPJ) em mais de um ano
Uso: python analise/16_transparencia_licc.py
"""
from __future__ import annotations

import csv
import importlib.util
import io
import re
import sys
from decimal import Decimal
from pathlib import Path

import pandas as pd

RAIZ = Path(__file__).resolve().parents[1]
PAG = RAIZ / "dados" / "fontes_web" / "paginas"
TAB = RAIZ / "analise" / "tabelas"
PROC = RAIZ / "dados" / "processados"
sys.path.insert(0, str(RAIZ / "analise"))

ARQ = {2022: "transp377_378", 2023: "transp377_379", 2024: "transp377_439", 2025: "transp377_536"}
URL = "https://transparencia.es.gov.br/Comum/incentivosfiscais/Download/{}"
COLS = {"nro": "nro", "processo": "processo", "data do processo": "data_processo", "projeto": "projeto",
        "cnpj": "cnpj_patrocinador", "cnpj patrocinador": "cnpj_patrocinador", "patrocinador": "patrocinador",
        "preponente": "proponente", "proponente": "proponente", "cnpj preponente": "cnpj_proponente",
        "cnpj proponente": "cnpj_proponente", "oferecido": "valor"}


def _modulo(nome: str, caminho: Path):
    spec = importlib.util.spec_from_file_location(nome, caminho)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


aud = _modulo("aud", RAIZ / "artigo" / "auditoria" / "auditar_captacao.py")
dv_cnpj_ok = _modulo("consultas", RAIZ / "analise" / "rede" / "consultas_publicas.py").dv_cnpj_ok


def abas(arquivo: Path) -> dict[str, list[list[str]]]:
    texto = arquivo.read_text(encoding="utf-8")
    cab = re.search(r"^# sha256 do original: (\w+)", texto, re.M)
    partes = re.split(r"^## Planilha: (.+)$", texto, flags=re.M)
    saida = {"_sha256": cab.group(1) if cab else ""}
    for nome, corpo in zip(partes[1::2], partes[2::2]):
        saida[nome.strip()] = list(csv.reader(io.StringIO(corpo.strip("\n"))))
    return saida


def so_digitos(x: str) -> str:
    return re.sub(r"\D", "", x or "")


def ler_ano(ano: int) -> tuple[pd.DataFrame, dict]:
    a = abas(PAG / f"{ARQ[ano]}.txt")
    linhas = a["DADOS"]
    i_cab = next(i for i, l in enumerate(linhas) if any(c.strip().upper() == "OFERECIDO" for c in l))
    cab = [COLS.get(re.sub(r"\s+", " ", c.strip().lower()), "") for c in linhas[i_cab]]
    impresso = {"limite": None, "total_impresso": None}
    for l in linhas[:i_cab]:
        rot = " ".join(c for c in l if c and not re.fullmatch(r"[\d.]+", c)).upper()
        num = next((c for c in reversed(l) if re.fullmatch(r"\d+(\.\d+)?", c.strip())), None)
        if "LIMITE" in rot and num:
            impresso["limite"], impresso["limite_rotulo"] = float(num), rot.strip(" ,")
        elif "TOTAL PATROCINADO" in rot and num:
            impresso["total_impresso"] = float(num)
    regs, anterior = [], {}
    for l in linhas[i_cab + 1:]:
        r = {c: (l[j].strip() if j < len(l) else "") for j, c in enumerate(cab) if c}
        if not any(r.get(k) for k in ("projeto", "patrocinador", "cnpj_patrocinador", "proponente")):
            # linha de total (só o valor) ou modelo vazio ("Digite a razão social..."): o total é guardado
            vals = [c for c in l if re.fullmatch(r"\d+(\.\d+)?", c.strip())]
            if vals and not any(c.strip() and not re.fullmatch(r"\d+(\.\d+)?", c.strip()) for c in l):
                impresso["total_rodape"] = float(vals[-1])
            continue
        if r.get("patrocinador", "").lower().startswith("digite"):
            continue
        herdado = []
        for k in ("processo", "data_processo", "projeto", "proponente", "cnpj_proponente"):
            if not r.get(k) and anterior.get(k) and (k in ("processo", "data_processo", "projeto") or
                                                     r.get("projeto", anterior.get("projeto")) == anterior.get("projeto")):
                r[k] = anterior[k]
                herdado.append(k)
        r["herdado"] = ";".join(herdado)
        anterior = r
        regs.append(r)
    df = pd.DataFrame(regs)
    df["ano"] = ano
    df["valor"] = pd.to_numeric(df["valor"], errors="coerce").round(2)
    df["data_processo"] = pd.to_datetime(df["data_processo"].str[:10], errors="coerce")
    for lado in ("patrocinador", "proponente"):
        df[f"cnpj_{lado}"] = df[f"cnpj_{lado}"].map(so_digitos)
        df[f"cnpj_{lado}_dv_ok"] = df[f"cnpj_{lado}"].map(lambda c: len(c) == 14 and dv_cnpj_ok(c))
    df["valor_zero"] = df["valor"].fillna(0) == 0
    df["fonte_url"] = URL.format(ARQ[ano].split("_")[1])
    df["fonte_arquivo"] = f"dados/fontes_web/paginas/{ARQ[ano]}.txt"
    df["sha256_original"] = a["_sha256"]
    return df, impresso


def main() -> None:
    todos, resumo = [], []
    for ano in ARQ:
        df, imp = ler_ano(ano)
        todos.append(df)
        pos = df[~df["valor_zero"]]
        resumo.append({"ano_captacao": ano, "linhas": len(df), "termos_valor_positivo": len(pos),
                       "termos_valor_zero": int(df["valor_zero"].sum()), "soma": round(pos["valor"].sum(), 2),
                       "total_impresso": imp.get("total_impresso") or imp.get("total_rodape"),
                       "limite_impresso": imp.get("limite"), "limite_rotulo": imp.get("limite_rotulo", ""),
                       "processos": pos["processo"].nunique(), "proponentes_cnpj": pos["cnpj_proponente"].replace("", pd.NA).nunique(),
                       "patrocinadores_cnpj": pos["cnpj_patrocinador"].nunique(),
                       "patrocinadores_raiz": pos["cnpj_patrocinador"].str[:8].nunique(),
                       "linhas_com_heranca": int((df["herdado"] != "").sum()),
                       "cnpj_proponente_invalido": int((~pos["cnpj_proponente_dv_ok"]).sum()),
                       "cnpj_patrocinador_invalido": int((~pos["cnpj_patrocinador_dv_ok"]).sum()),
                       "data_min": pos["data_processo"].min().date(), "data_max": pos["data_processo"].max().date()})
    t = pd.concat(todos, ignore_index=True)
    col = ["ano", "nro", "processo", "data_processo", "projeto", "cnpj_patrocinador", "patrocinador", "proponente",
           "cnpj_proponente", "valor", "valor_zero", "herdado", "cnpj_patrocinador_dv_ok", "cnpj_proponente_dv_ok",
           "fonte_url", "fonte_arquivo", "sha256_original"]
    t[[c for c in col if c in t.columns]].to_csv(PROC / "transparencia_licc_termos.csv", index=False)

    # comparação com o anexo "Recurso financeiro captado" da SECULT (auditar_captacao.ler_anexo), chave CNPJ × valor
    man = aud.manifesto()
    anual = pd.read_csv(RAIZ / "artigo" / "auditoria" / "auditoria_captacao_anual.csv")
    comp = []
    for r in resumo:
        ano = r["ano_captacao"]
        sec = aud.ler_anexo(ano, aud.ANEXOS[ano], man)["termos"]
        chave_sec = pd.Series([f"{x['cnpj']}|{Decimal(x['valor']):.2f}" for x in sec]).value_counts()
        pos = t[(t["ano"] == ano) & ~t["valor_zero"]]
        chave_tr = pd.Series([f"{c}|{v:.2f}" for c, v in zip(pos["cnpj_patrocinador"], pos["valor"])]).value_counts()
        comum = int(sum(min(n, chave_sec.get(k, 0)) for k, n in chave_tr.items()))
        r["soma_anexo_secult"] = float(anual.loc[anual["ano_captacao"] == ano, "soma_termos"].iat[0])
        r["termos_anexo_secult"] = len(sec)
        r["diferenca_soma"] = round(r["soma"] - r["soma_anexo_secult"], 2)
        comp.append({"ano_captacao": ano, "termos_transparencia": int(chave_tr.sum()), "termos_anexo": len(sec),
                     "casam_cnpj_valor": comum, "so_transparencia": int(chave_tr.sum()) - comum,
                     "so_anexo": len(sec) - comum,
                     "nota": "chave = CNPJ do estabelecimento patrocinador × valor em centavos; o anexo de 2024 e 2025 "
                             "é a versão atual (ver 13_versoes_captados.csv)"})
    res = pd.DataFrame(resumo)
    res["fonte"] = "Portal da Transparência ES, seção 07 (Download/378, 379, 439, 536); anexos SECULT via auditar_captacao"
    res.to_csv(TAB / "16_transparencia_resumo.csv", index=False)
    pd.DataFrame(comp).to_csv(TAB / "16_transparencia_x_anexo.csv", index=False)
    print(res.T.to_string())
    print(pd.DataFrame(comp).to_string(index=False))

    # fila: termos e valor por mês da "data do processo"
    pos = t[~t["valor_zero"] & t["data_processo"].notna()].copy()
    pos["mes"] = pos["data_processo"].dt.to_period("M").astype(str)
    fila = pos.groupby(["ano", "mes"]).agg(termos=("valor", "size"), valor=("valor", "sum")).reset_index()
    fila["valor_acumulado"] = fila.groupby("ano")["valor"].cumsum()
    lim = res.set_index("ano_captacao")["limite_impresso"]
    fila["pct_do_limite_impresso"] = fila["valor_acumulado"] / fila["ano"].map(lim)
    fila.to_csv(TAB / "16_fila_por_mes.csv", index=False)
    print(fila.to_string(index=False))

    # pares patrocinador (raiz) × proponente (CNPJ) que se repetem entre anos
    pos = t[~t["valor_zero"] & t["cnpj_proponente_dv_ok"]].copy()
    pos["raiz_patrocinador"] = pos["cnpj_patrocinador"].str[:8]
    pares = pos.groupby(["raiz_patrocinador", "cnpj_proponente"]).agg(
        anos=("ano", lambda x: ";".join(map(str, sorted(set(x))))), n_anos=("ano", "nunique"),
        termos=("valor", "size"), valor=("valor", "sum"),
        patrocinador=("patrocinador", "first"), proponente=("proponente", "first")).reset_index()
    rec = pares[pares["n_anos"] > 1].sort_values(["n_anos", "valor"], ascending=False)
    rec.to_csv(TAB / "16_pares_recorrentes.csv", index=False)
    print(f"pares patrocinador×proponente: {len(pares)}; em mais de um ano: {len(rec)} "
          f"({rec['valor'].sum() / pares['valor'].sum():.1%} do valor)")


if __name__ == "__main__":
    main()
