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

import csv
import io
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
# fora do padrão: dígito ou letra colados, decimal com ponto ("15333611913.86", SICONFI) e decimal com vírgula ("…,23")
CPF = re.compile(r"(?<![0-9A-Za-z./])\d{3}\.?\d{3}\.?\d{3}-?\d{2}(?![0-9A-Za-z/]|\.\d|,\d{2}(?!\d))")
# razão social de MEI: nome seguido do CPF ("FULANO DE TAL 12345678901"), mesmo quando a célula seguinte da planilha
# começa por dígitos (",28.096.224/0001-68"), caso que o padrão acima toma por decimal com vírgula
CPF_MEI = re.compile(r"(?<=[A-Za-zÀ-ÿ] )\d{3}\.?\d{3}\.?\d{3}-?\d{2}(?![0-9/]|\.\d)")
# colunas numéricas que podem ter 11 dígitos sem ser CPF: capital social da Receita acima de R$ 10 bilhões (Ambev,
# ArcelorMittal, Claro) foi mascarado por engano em 27/09/2026 e restaurado; nessas tabelas a coluna é pulada
COLUNAS_PROTEGIDAS = {"capital_social"}
ALVOS = ("dados/fontes_web/paginas/*.txt", "dados/licc/**/*.csv", "dados/licc/**/*.json", "dados/processados/*.csv",
         "analise/tabelas/*.csv", "dados/externos/*.csv")


def mascarar(texto: str) -> tuple[str, int]:
    n = 0

    def troca(m: re.Match) -> str:
        nonlocal n
        n += 1
        return re.sub(r"\d", "X", m.group(0))

    linhas = [l if l.startswith("# ") else CPF_MEI.sub(troca, CPF.sub(troca, l)) for l in texto.split("\n")]
    return "\n".join(linhas), n


def mascarar_arquivo(arq: Path, texto: str) -> tuple[str, int]:
    """Como mascarar(), mas, num CSV com coluna protegida, campo a campo e sem tocar a coluna protegida."""
    cab = texto.split("\n", 1)[0] + "\n"
    if arq.suffix != ".csv" or not COLUNAS_PROTEGIDAS & set(next(csv.reader([cab]), [])):
        return mascarar(texto)
    linhas = list(csv.reader(io.StringIO(texto)))
    prot = {i for i, h in enumerate(linhas[0]) if h in COLUNAS_PROTEGIDAS}
    n = 0
    for linha in linhas[1:]:
        for i, v in enumerate(linha):
            if i not in prot:
                linha[i], k = mascarar(v)
                n += k
    if not n:
        return texto, 0
    saida = io.StringIO()
    csv.writer(saida, lineterminator="\r\n" if "\r\n" in cab + "\n" else "\n").writerows(linhas)
    return saida.getvalue(), n


def main() -> int:
    conferir = "--conferir" in sys.argv
    total = 0
    for padrao in ALVOS:
        for arq in sorted(RAIZ.glob(padrao)):
            texto = arq.read_text(encoding="utf-8")
            novo, n = mascarar_arquivo(arq, texto)
            if n:
                total += n
                print(f"{arq.relative_to(RAIZ)}: {n}")
                if not conferir:
                    arq.write_text(novo, encoding="utf-8")
    print(f"{total} ocorrências {'encontradas' if conferir else 'mascaradas'}")
    return 1 if conferir and total else 0


if __name__ == "__main__":
    sys.exit(main())
