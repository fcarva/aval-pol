"""
Registra as coletas feitas com o Firecrawl (ferramenta da sessão em nuvem, sem chave no ambiente) em
dados/fontes_web/firecrawl/manifesto.csv, no mesmo espírito de dados/fontes_web/manifesto.csv (relé).

Pedido do autor (28/09/2026): "coloque o pipeline de dados para rodar, com o firecrawl funcionando agora para fechar
lacunas de contexto antes perdidas". O Firecrawl não é chamável dos scripts (a rede do contêiner só alcança o GitHub e
os registros de pacotes); cada resultado é gravado à mão em dados/fontes_web/firecrawl/<id>.md, com cabeçalho:

    ---
    id: ijsn_cultura_em_dados_2026
    url: https://...
    ferramenta: firecrawl_scrape | firecrawl_search
    consulta: texto da busca ou do pedido (vazio no scrape simples)
    coletado_utc: 2026-09-28T18:00:00Z
    nota: por que foi coletado e o que se usa
    ---
    <conteúdo devolvido pelo Firecrawl, sem edição, ou só o trecho principal, dito na nota>

Este script lê os cabeçalhos, calcula sha256 e bytes do arquivo e reescreve o manifesto. Com --conferir, só confere
se todo .md tem linha no manifesto com o mesmo sha256 (saída 1 se não).

Uso: python analise/rede/registrar_firecrawl.py [--conferir]
"""
from __future__ import annotations

import csv
import hashlib
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
PASTA = RAIZ / "dados" / "fontes_web" / "firecrawl"
MANIFESTO = PASTA / "manifesto.csv"
CAMPOS = ["id", "url", "ferramenta", "consulta", "coletado_utc", "sha256", "bytes", "arquivo", "nota"]


def cabecalho(texto: str) -> dict[str, str]:
    if not texto.startswith("---\n"):
        return {}
    fim = texto.find("\n---\n", 4)
    if fim < 0:
        return {}
    meta = {}
    for linha in texto[4:fim].splitlines():
        if ":" in linha:
            k, v = linha.split(":", 1)
            meta[k.strip()] = v.strip()
    return meta


def linhas() -> list[dict[str, str]]:
    saida = []
    for arq in sorted(PASTA.glob("*.md")):
        bruto = arq.read_bytes()
        meta = cabecalho(bruto.decode("utf-8"))
        if not meta.get("id") or not meta.get("url"):
            raise SystemExit(f"{arq.name}: cabeçalho sem id ou url")
        saida.append({**{k: meta.get(k, "") for k in CAMPOS}, "sha256": hashlib.sha256(bruto).hexdigest(),
                      "bytes": str(len(bruto)), "arquivo": str(arq.relative_to(RAIZ))})
    return saida


def main() -> None:
    atuais = linhas()
    if "--conferir" in sys.argv:
        gravadas = {}
        if MANIFESTO.exists():
            with MANIFESTO.open(encoding="utf-8") as f:
                gravadas = {r["arquivo"]: r["sha256"] for r in csv.DictReader(f)}
        erros = [l["arquivo"] for l in atuais if gravadas.get(l["arquivo"]) != l["sha256"]]
        print(f"firecrawl: {len(atuais)} arquivos; {len(erros)} sem registro ou com sha256 divergente")
        for e in erros:
            print("  ", e)
        sys.exit(1 if erros else 0)
    with MANIFESTO.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=CAMPOS)
        w.writeheader()
        w.writerows(atuais)
    print(f"firecrawl: {len(atuais)} coletas registradas em {MANIFESTO.relative_to(RAIZ)}")


if __name__ == "__main__":
    main()
