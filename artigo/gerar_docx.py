"""Gera artigo/rascunho-artigo.docx a partir de artigo/rascunho-artigo.md.

Usa o pandoc (pacote pypandoc_binary) com o modelo artigo/modelo/referencia-abnt.docx
(Times New Roman 12, espaçamento simples, margens 3/3/2/2 cm) e depois ajusta as tabelas
com python-docx: fonte 10, bordas simples, cabeçalho em negrito. Com --pdf, converte
também para PDF pelo LibreOffice, só para conferir o número de páginas (10 a 15).

Uso: python artigo/gerar_docx.py [--pdf]
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pypandoc
from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Pt

ART = Path(__file__).resolve().parent
MD = ART / "rascunho-artigo.md"
DOCX = ART / "rascunho-artigo.docx"
MODELO = ART / "modelo" / "referencia-abnt.docx"


def bordas(tabela, aberta: bool) -> None:
    """Quadro: grade completa. Tabela (norma tabular do IBGE, usada pela ABNT): sem traços verticais."""
    tblPr = tabela._tbl.tblPr
    for velho in tblPr.findall(qn("w:tblBorders")):
        tblPr.remove(velho)
    b = OxmlElement("w:tblBorders")
    lados = ("top", "bottom", "insideH") if aberta else ("top", "left", "bottom", "right", "insideH", "insideV")
    for lado in lados:
        e = OxmlElement(f"w:{lado}")
        e.set(qn("w:val"), "single")
        e.set(qn("w:sz"), "4")
        e.set(qn("w:space"), "0")
        e.set(qn("w:color"), "000000")
        b.append(e)
    tblPr.append(b)


def ajustar_tabelas(caminho: Path) -> None:
    doc = Document(caminho)
    # título de cada tabela = parágrafo imediatamente anterior no corpo do documento
    titulos = []  # na mesma ordem de doc.tables (tabelas de nível superior, em ordem do documento)
    anterior = ""
    for el in doc.element.body.iterchildren():
        if el.tag == qn("w:p"):
            anterior = "".join(x.text or "" for x in el.iter(qn("w:t")))
        elif el.tag == qn("w:tbl"):
            titulos.append(anterior)
    for t, titulo in zip(doc.tables, titulos):
        t.alignment = WD_TABLE_ALIGNMENT.CENTER
        bordas(t, aberta=titulo.startswith("Tabela"))
        for i, linha in enumerate(t.rows):
            for cel in linha.cells:
                for par in cel.paragraphs:
                    par.alignment = WD_ALIGN_PARAGRAPH.LEFT
                    par.paragraph_format.space_after = Pt(0)
                    par.paragraph_format.space_before = Pt(0)
                    for run in par.runs:
                        run.font.size = Pt(10)
                        if i == 0:
                            run.font.bold = True
        # cabeçalho repetido em quebra de página; tabela curta (até 8 linhas) não se divide
        cab = t.rows[0]._tr.get_or_add_trPr()
        rep = OxmlElement("w:tblHeader")
        rep.set(qn("w:val"), "true")
        cab.append(rep)
        if len(t.rows) <= 8:
            for linha in t.rows[:-1]:
                for cel in linha.cells:
                    for par in cel.paragraphs:
                        par.paragraph_format.keep_with_next = True
    # título de tabela, quadro e figura fica na mesma página do objeto
    for par in doc.paragraphs:
        if par.text.startswith(("Tabela ", "Quadro ", "Figura ")):
            par.paragraph_format.keep_with_next = True
    # "Fonte:" logo abaixo de tabelas e figuras, em corpo 10 (ABNT)
    for par in doc.paragraphs:
        if par.text.startswith("Fonte:"):
            for run in par.runs:
                run.font.size = Pt(10)
    doc.save(caminho)


def main() -> None:
    pypandoc.convert_file(
        str(MD), "docx", outputfile=str(DOCX),
        extra_args=[f"--reference-doc={MODELO}", f"--resource-path={ART}", "--wrap=none"],
    )
    ajustar_tabelas(DOCX)
    print(DOCX)
    if "--pdf" in sys.argv:
        subprocess.run(["soffice", "--headless", "--convert-to", "pdf", "--outdir", str(ART), str(DOCX)],
                       check=True, capture_output=True)
        print(ART / "rascunho-artigo.pdf")


if __name__ == "__main__":
    main()
