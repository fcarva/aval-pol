"""Mascara números com formato de CPF (11 dígitos, com ou sem pontuação) nos textos e tabelas do repositório.

Os anexos da SECULT imprimem o CPF de alguns proponentes pessoa física junto ao nome. O repositório é público e o
artigo não usa esse dado, então cada dígito vira "X", preservando o comprimento da linha (a auditoria da captação
lê os anexos por coluna). Os dados brutos do SALIC (dados/externos/raw/salic/), base federal aberta, não
entram. CNPJ (14 dígitos), valores monetários e hashes não casam com o padrão; linhas de
cabeçalho do relé ("# Fonte", "# sha256") ficam intactas. O histórico do git mantém as versões anteriores.

Uso: python analise/rede/mascarar_cpf.py            (mascara no lugar e lista o que trocou)
     python analise/rede/mascarar_cpf.py --conferir (só conta; código de saída 1 se achar CPF)
O relé (buscar_fontes.py) aplica mascarar() a toda página coletada.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
# fora do padrão: dígito ou letra colados, decimal com ponto ("15333611913.86", SICONFI) e decimal com vírgula ("…,23")
CPF = re.compile(r"(?<![0-9A-Za-z./])\d{3}\.?\d{3}\.?\d{3}-?\d{2}(?![0-9A-Za-z/]|\.\d|,\d{2}(?!\d))")
ALVOS = ("dados/fontes_web/paginas/*.txt", "dados/licc/**/*.csv", "dados/licc/**/*.json", "dados/processados/*.csv", "analise/tabelas/*.csv")


def mascarar(texto: str) -> tuple[str, int]:
    n = 0

    def troca(m: re.Match) -> str:
        nonlocal n
        n += 1
        return re.sub(r"\d", "X", m.group(0))

    linhas = [l if l.startswith("# ") else CPF.sub(troca, l) for l in texto.split("\n")]
    return "\n".join(linhas), n


def main() -> int:
    conferir = "--conferir" in sys.argv
    total = 0
    for padrao in ALVOS:
        for arq in sorted(RAIZ.glob(padrao)):
            texto = arq.read_text(encoding="utf-8")
            novo, n = mascarar(texto)
            if n:
                total += n
                print(f"{arq.relative_to(RAIZ)}: {n}")
                if not conferir:
                    arq.write_text(novo, encoding="utf-8")
    print(f"{total} ocorrências {'encontradas' if conferir else 'mascaradas'}")
    return 1 if conferir and total else 0


if __name__ == "__main__":
    sys.exit(main())
