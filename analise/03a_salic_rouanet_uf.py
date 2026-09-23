"""
03a — Lei Rouanet (mecenato) por UF e, no ES, por município, a partir da API pública do SALIC.

Fonte: API REST do SALIC/MinC, https://api.salic.cultura.gov.br/api/v1/projetos
       (consultada em 2026-09-23; paginação limit/offset; filtro ano_projeto = 2 dígitos do PRONAC).

O que o dado é (e não é):
- `valor_captado` é o total captado ACUMULADO pelo projeto até a data da consulta, não o captado
  em um ano-calendário. Agregamos pelo `ano_projeto` (ano de autuação do PRONAC). Projetos recentes
  (2025, 2026) ainda estão captando: a série é incompleta no fim.
- `UF`/`municipio` são os campos de localização do projeto no SALIC (em regra, o domicílio do
  proponente) — não necessariamente onde o projeto é executado (`local_realizacao`). [VERIFICAR
  no dicionário da API qual é a semântica exata do campo UF.]
- Filtramos `mecanisnmo == 'Mecenato'` (grafia da API) para ficar só com a renúncia do art. 18/26.
- Ausência não é zero: projeto sem valor_captado informado entra como ausente (NaN), e a cobertura
  é reportada.

Saídas:
  dados/externos/rouanet_captacao_uf_ano.csv
  dados/externos/rouanet_es_municipio.csv
Cache bruto: dados/externos/raw/salic/projetos_ano{AA}_off{N}.json
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import pandas as pd
import requests

RAIZ = Path(__file__).resolve().parents[1]
RAW = RAIZ / "dados" / "externos" / "raw" / "salic"
RAW.mkdir(parents=True, exist_ok=True)
OUT = RAIZ / "dados" / "externos"
URL = "https://api.salic.cultura.gov.br/api/v1/projetos"
ANOS = [int(a) for a in sys.argv[1:]] or list(range(19, 26))  # 2019..2025
CAMPOS = ["PRONAC", "nome", "UF", "municipio", "segmento", "mecanisnmo", "enquadradmento",
          "ano_projeto", "valor_solicitado", "valor_aprovado", "valor_captado", "situacao",
          "proponente", "cgccpf"]


def baixar_ano(aa: int) -> list[dict]:
    regs: list[dict] = []
    off, lim = 0, 100
    while True:
        cache = RAW / f"projetos_ano{aa:02d}_off{off:06d}.json"
        if cache.exists():
            d = json.loads(cache.read_text(encoding="utf-8"))
        else:
            for tent in range(4):
                try:
                    r = requests.get(URL, params={"ano_projeto": f"{aa:02d}", "limit": lim,
                                                  "offset": off, "format": "json"}, timeout=90)
                    r.raise_for_status()
                    d = r.json()
                    break
                except Exception as e:  # noqa: BLE001
                    print(f"  falha ano {aa} off {off}: {e}; tentativa {tent+1}", flush=True)
                    time.sleep(5 * (tent + 1))
            else:
                raise RuntimeError(f"não baixou ano {aa} offset {off}")
            # guarda só os campos usados (o registro completo tem textos longos)
            enx = {"total": d.get("total"),
                   "_embedded": {"projetos": [{k: p.get(k) for k in CAMPOS}
                                              for p in d.get("_embedded", {}).get("projetos", [])]}}
            cache.write_text(json.dumps(enx, ensure_ascii=False), encoding="utf-8")
            d = enx
        ps = d.get("_embedded", {}).get("projetos", [])
        regs.extend(ps)
        total = d.get("total") or 0
        off += lim
        if off >= total or not ps:
            print(f"ano {aa}: {len(regs)} de total {total}", flush=True)
            return regs


def main() -> None:
    todos = []
    for aa in ANOS:
        todos.extend(baixar_ano(aa))
    df = pd.DataFrame(todos)
    for c in ["valor_solicitado", "valor_aprovado", "valor_captado"]:
        df[c] = pd.to_numeric(df[c], errors="coerce")
    df["ano"] = 2000 + df["ano_projeto"].astype(int)
    print("mecanismos:", df["mecanisnmo"].value_counts(dropna=False).to_dict())
    mec = df[df["mecanisnmo"] == "Mecenato"].copy()
    mec["captou"] = mec["valor_captado"] > 0

    g = (mec.groupby(["ano", "UF"])
            .agg(n_projetos=("PRONAC", "count"),
                 n_com_captacao=("captou", "sum"),
                 n_valor_captado_informado=("valor_captado", "count"),
                 valor_aprovado=("valor_aprovado", "sum"),
                 valor_captado=("valor_captado", "sum"))
            .reset_index())
    tot = g.groupby("ano")["valor_captado"].transform("sum")
    g["share_captado_brasil"] = g["valor_captado"] / tot
    cab = ("# Fonte: API SALIC/MinC https://api.salic.cultura.gov.br/api/v1/projetos, consulta 2026-09-23; "
           "mecanismo=Mecenato; valor_captado = acumulado do projeto ate a consulta, agregado por ano do PRONAC "
           "(ano_projeto); UF = campo UF do SALIC. Script: analise/03a_salic_rouanet_uf.py\n")
    p1 = OUT / "rouanet_captacao_uf_ano.csv"
    with open(p1, "w", encoding="utf-8", newline="") as f:
        f.write(cab)
        g.to_csv(f, index=False)

    es = mec[mec["UF"] == "ES"]
    m = (es.groupby(["municipio"])
           .agg(n_projetos=("PRONAC", "count"), n_com_captacao=("captou", "sum"),
                valor_captado=("valor_captado", "sum"))
           .reset_index().sort_values("valor_captado", ascending=False))
    p2 = OUT / "rouanet_es_municipio.csv"
    with open(p2, "w", encoding="utf-8", newline="") as f:
        f.write(cab.replace("\n", f" Recorte: UF=ES, anos {min(ANOS)+2000}-{max(ANOS)+2000}.\n"))
        m.to_csv(f, index=False)
    print(p1, p2)


if __name__ == "__main__":
    main()
