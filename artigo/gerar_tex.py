"""Gera artigo/latex/artigo.tex a partir de artigo/rascunho-artigo.md.

O .md continua sendo a fonte única do texto: as checagens de artigo/auditoria/ leem o .md, e o .tex
é regenerado por este script (não edite o .tex à mão). O corpo passa pelo pandoc; quadros, tabelas
e a Figura 1 são montados aqui, no padrão do .docx (artigo/gerar_docx.py):

- Times New Roman 12 (TeX Gyre Termes onde a TNR não estiver instalada), espaçamento simples,
  margens de 3 cm (superior e esquerda) e 2 cm (inferior e direita);
- título acima e fonte abaixo de quadros, tabelas e figuras, em corpo 10;
- quadro com grade completa e divisível entre páginas (cabeçalho repetido); tabela no padrão
  tabular do IBGE, sem traços verticais, mantida inteira;
- Figura 1 em PDF vetorial, numa página própria logo após a primeira menção.

Uso: python artigo/gerar_tex.py [--pdf]
     --pdf compila com XeLaTeX (latexmk), conta as páginas (limite: 15) e lista glifos ausentes.
"""
from __future__ import annotations

import re
import shutil
import subprocess
import sys
from pathlib import Path

import pypandoc
import yaml

ART = Path(__file__).resolve().parent
MD = ART / "rascunho-artigo.md"
DIR = ART / "latex"
TEX = DIR / "artigo.tex"
FIGURAS = ART.parent / "analise" / "figuras"
FORMATO = "markdown-auto_identifiers+autolink_bare_uris"
SEP = "XXSEPARADORXX"
LIMITE_PAGINAS = 15

PREAMBULO = r"""% !TEX program = xelatex
% Gerado por artigo/gerar_tex.py a partir de artigo/rascunho-artigo.md. Não edite à mão:
% altere o .md e rode `python artigo/gerar_tex.py --pdf`. Compila com XeLaTeX (recomendado),
% LuaLaTeX ou pdfLaTeX; no Overleaf, o arquivo latexmkrc desta pasta já seleciona o XeLaTeX.
\documentclass[12pt,a4paper]{article}
\usepackage[top=3cm,bottom=2cm,left=3cm,right=2cm,headsep=0.8cm]{geometry}
\usepackage{iftex}
\usepackage{amsmath}
\usepackage[brazilian]{babel}
\ifPDFTeX
  % pdfLaTeX: Times pelo newtx (ou pelo mathptmx, se o newtx não estiver instalado)
  \usepackage[T1]{fontenc}
  \usepackage[utf8]{inputenc}
  \IfFileExists{newtxtext.sty}{\usepackage{newtxtext,newtxmath}}{\usepackage{mathptmx}}
\else
  % XeLaTeX/LuaLaTeX: Times New Roman 12, como pedem as instruções da disciplina. Onde ela não
  % estiver instalada (Overleaf, Linux), usa a TeX Gyre Termes, clone métrico da Times do TeX Live.
  \usepackage{unicode-math}
  \IfFontExistsTF{Times New Roman}
    {\setmainfont{Times New Roman}}
    {\setmainfont{texgyretermes}[Extension=.otf, UprightFont=*-regular, BoldFont=*-bold,
       ItalicFont=*-italic, BoldItalicFont=*-bolditalic]}
  \setmathfont{texgyretermes-math.otf}
\fi
\usepackage{microtype}
\usepackage{graphicx}
\usepackage{calc}
\usepackage{array}
\usepackage{longtable}
\usepackage{booktabs}
\usepackage{enumitem}
\usepackage{titlesec}
\usepackage{fancyhdr}
\usepackage{xurl}
\usepackage[hidelinks]{hyperref}
\urlstyle{same}

% Espaçamento simples, sem recuo e com 6 pt entre parágrafos (o mesmo do .docx)
\setlength{\parindent}{0pt}
\setlength{\parskip}{6pt plus 2pt minus 1pt}
\setlength{\emergencystretch}{1.5em}
\frenchspacing  % espaço simples depois do ponto, como no português
\setcounter{secnumdepth}{2}
\titleformat{\section}{\normalfont\normalsize\bfseries}{\thesection}{0.5em}{}
\titleformat{\subsection}{\normalfont\normalsize\bfseries}{\thesubsection}{0.5em}{}
\titlespacing*{\section}{0pt}{12pt}{0pt}
\titlespacing*{\subsection}{0pt}{12pt}{0pt}
\setlist[itemize]{leftmargin=1.2em, topsep=0pt, itemsep=3pt, parsep=0pt}
\providecommand{\tightlist}{\setlength{\itemsep}{3pt}\setlength{\parskip}{0pt}}

% Número da página no canto superior direito (ABNT)
\pagestyle{fancy}
\fancyhf{}
\fancyhead[R]{\footnotesize\thepage}
\renewcommand{\headrulewidth}{0pt}
\setlength{\headheight}{14.5pt}
\fancypagestyle{plain}{\fancyhf{}\fancyhead[R]{\footnotesize\thepage}}

% A Figura 1 ocupa uma página; floats grandes vão para a página seguinte à menção
\renewcommand{\floatpagefraction}{0.8}
\setlength{\LTpre}{6pt}
\setlength{\LTpost}{0pt}

% Referências: alinhadas à esquerda, espaço simples, separadas por 6 pt (como no .docx)
\newenvironment{referencias}{\raggedright\setlength{\parskip}{6pt}}{\par}
"""


def ler() -> tuple[dict, str]:
    texto = MD.read_text(encoding="utf-8")
    m = re.match(r"---\n(.*?)\n---\n", texto, flags=re.S)
    return yaml.safe_load(m.group(1)), texto[m.end():]


def preparar(md: str) -> str:
    """Letras gregas fora de fórmula viram fórmula (a Termes não tem grego); código vira \\path."""
    partes = re.split(r"(\$\$.*?\$\$|(?<!\\)\$[^$\n]+?(?<!\\)\$)", md, flags=re.S)
    for i in range(0, len(partes), 2):
        for letra, cmd in {"α": r"\alpha", "β": r"\beta", "ρ": r"\rho"}.items():
            partes[i] = partes[i].replace(letra, f"${cmd}$")
    md = "".join(partes)
    return re.sub(r"`([^`\n]+)`", lambda m: "`\\path{" + m.group(1) + "}`{=latex}", md)


def md_latex(fragmentos: list[str]) -> list[str]:
    """Converte vários trechos de markdown numa só chamada do pandoc."""
    junto = f"\n\n{SEP}\n\n".join(fragmentos)
    saida = pypandoc.convert_text(junto, "latex", format=FORMATO, extra_args=["--wrap=none"])
    partes = re.split(rf"\s*{SEP}\s*", saida.strip())
    assert len(partes) == len(fragmentos), (len(partes), len(fragmentos))
    return partes


def celulas(linha: str) -> list[str]:
    return [c.strip() for c in re.split(r"(?<!\\)\|", linha.strip().strip("|"))]


def separar_blocos(corpo: str) -> tuple[str, list[dict]]:
    """Troca cada quadro, tabela ou figura (título + objeto + fonte) por um marcador."""
    paragrafos = re.split(r"\n[ \t]*\n", corpo.strip())
    saida, blocos = [], []
    i = 0
    while i < len(paragrafos):
        p = paragrafos[i]
        if p.startswith("|") or p.startswith("!["):
            titulo = saida.pop()
            m = re.fullmatch(r"\*\*((Quadro|Tabela|Figura) \d+ – .+)\*\*", titulo.strip())
            assert m, f"título ausente antes de: {p[:60]}"
            fonte = paragrafos[i + 1] if i + 1 < len(paragrafos) and paragrafos[i + 1].startswith("Fonte:") else ""
            assert fonte, f"fonte ausente depois de: {m.group(1)}"
            blocos.append({"tipo": m.group(2), "titulo": m.group(1), "objeto": p, "fonte": fonte})
            saida.append(f"XXBLOCO{len(blocos) - 1}XX")
            i += 2
            continue
        saida.append(p)
        i += 1
    return "\n\n".join(saida), blocos


def tabela_latex(bloco: dict, conv) -> str:
    linhas = [l for l in bloco["objeto"].splitlines() if l.strip()]
    cab, sep, dados = celulas(linhas[0]), celulas(linhas[1]), [celulas(l) for l in linhas[2:]]
    n = len(cab)
    assert all(len(r) == n for r in dados), bloco["titulo"]
    tracos = [len(s.strip(":")) for s in sep]
    larguras = [t / sum(tracos) for t in tracos]
    quadro = bloco["tipo"] == "Quadro"
    util = rf"\linewidth - {2 * n}\tabcolsep" + (rf" - {n + 1}\arrayrulewidth" if quadro else "")
    colunas = [rf">{{\raggedright\arraybackslash}}p{{({util}) * \real{{{w:.4f}}}}}" for w in larguras]
    spec = ("|" + "|".join(colunas) + "|") if quadro else "".join(colunas)
    titulo = rf"\multicolumn{{{n}}}{{@{{}}p{{\linewidth}}@{{}}}}{{\normalsize\bfseries\raggedright {conv(bloco['titulo'])}}}"
    fonte = rf"\multicolumn{{{n}}}{{@{{}}p{{\linewidth}}@{{}}}}{{\raggedright {conv(bloco['fonte'])}}}"
    cabecalho = " & ".join(rf"\textbf{{{conv(c)}}}" for c in cab) + r" \\"
    corpo = [" & ".join(conv(c) for c in r) for r in dados]
    if quadro:  # grade completa; pode dividir entre páginas, com cabeçalho repetido
        cabeca = [titulo + r" \\[3pt]", r"\hline", cabecalho, r"\hline", r"\endfirsthead",
                  r"\hline", cabecalho, r"\hline", r"\endhead",
                  fonte + r" \\", r"\endlastfoot"]
        miolo = [r + r" \\ \hline" for r in corpo]
    else:  # padrão tabular do IBGE: sem traços verticais; \\* impede a quebra de página
        cabeca = [titulo + r" \\*[3pt]", r"\toprule", cabecalho[:-2] + r"\\*", r"\midrule", r"\endfirsthead",
                  r"\bottomrule", fonte + r" \\", r"\endlastfoot"]
        miolo = [r + r" \\*" for r in corpo[:-1]] + [corpo[-1] + r" \\"]
    return "\n".join([r"\begingroup\footnotesize\renewcommand{\arraystretch}{1.15}",
                      rf"\begin{{longtable}}{{{spec}}}", *cabeca, *miolo,
                      r"\end{longtable}", r"\endgroup"])


def figura_latex(bloco: dict, conv) -> str:
    m = re.match(r"!\[[^\]]*\]\(([^)]+)\)", bloco["objeto"])
    origem = (ART / m.group(1)).resolve().with_suffix(".pdf")  # PDF vetorial em vez do PNG do .docx
    destino = DIR / "figuras" / origem.name
    destino.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(origem, destino)
    return "\n".join([
        r"\begin{figure}[p]",
        rf"{{\raggedright\bfseries {conv(bloco['titulo'])}\par}}",
        r"\vspace{6pt}",
        rf"\centering\includegraphics[width=\linewidth]{{figuras/{destino.name}}}\par",
        r"\vspace{4pt}",
        rf"{{\raggedright\footnotesize {conv(bloco['fonte'])}\par}}",
        r"\end{figure}",
    ])


def secoes(tex: str) -> str:
    """Tira a numeração manual dos títulos e confere que a do LaTeX dá os mesmos números."""
    lidos, sec, sub = [], 0, 0

    def trocar(m: re.Match) -> str:
        nonlocal sec, sub
        cmd, titulo = m.group(1), m.group(2)
        num = re.match(r"(\d+(?:\.\d+)?) (.+)", titulo)
        if not num:
            return rf"\{cmd}*{{{titulo}}}"
        if cmd == "section":
            sec, sub = sec + 1, 0
            esperado = str(sec)
        else:
            sub += 1
            esperado = f"{sec}.{sub}"
        assert num.group(1) == esperado, f"numeração do .md ({num.group(1)}) ≠ LaTeX ({esperado})"
        lidos.append(esperado)
        return rf"\{cmd}{{{num.group(2)}}}"

    tex = re.sub(r"\\(section|subsection)\{(.+?)\}", trocar, tex)
    ini = tex.index(r"\section*{Referências}") + len(r"\section*{Referências}")
    fim = tex.index(r"\section*{Declaração")
    return tex[:ini] + "\n\\begin{referencias}\n" + tex[ini:fim].strip() + "\n\\end{referencias}\n\n" + tex[fim:]


def gerar() -> None:
    meta, corpo = ler()
    corpo, blocos = separar_blocos(preparar(corpo))

    # todos os trechos de quadros, tabelas, figuras e da página de rosto numa só conversão
    trechos: list[str] = []
    for b in blocos:
        trechos += [b["titulo"], b["fonte"]]
        if b["tipo"] != "Figura":
            for l in [l for l in b["objeto"].splitlines() if l.strip()][:1] + b["objeto"].splitlines()[2:]:
                trechos += celulas(l)
    autores = meta["author"] if isinstance(meta["author"], list) else [meta["author"]]
    trechos += [meta["title"], meta["date"], *autores]
    convertidos = dict(zip(trechos, md_latex(trechos)))
    conv = convertidos.__getitem__

    tex = pypandoc.convert_text(corpo, "latex", format=FORMATO, extra_args=["--wrap=auto", "--columns=100"])
    for k, b in enumerate(blocos):
        latex = figura_latex(b, conv) if b["tipo"] == "Figura" else tabela_latex(b, conv)
        tex = tex.replace(f"XXBLOCO{k}XX", latex)
    assert "XXBLOCO" not in tex
    tex = secoes(tex)

    rosto = "\n".join([
        r"\begin{center}",
        rf"{{\large\bfseries {conv(meta['title'])}\par}}",
        r"\vspace{6pt}",
        *[rf"{conv(a)}\par" for a in autores],
        r"\vspace{3pt}",
        rf"{conv(meta['date'])}\par",
        r"\end{center}",
    ])
    info = rf"\hypersetup{{pdftitle={{{meta['title']}}}, pdflang={{pt-BR}}}}"
    DIR.mkdir(parents=True, exist_ok=True)
    TEX.write_text(PREAMBULO + info + "\n\n\\begin{document}\n\n" + rosto + "\n\n" + tex.strip()
                   + "\n\n\\end{document}\n", encoding="utf-8")
    (DIR / "latexmkrc").write_text("# XeLaTeX (também no Overleaf)\n$pdf_mode = 5;\n", encoding="utf-8")
    print(TEX)


def compilar() -> None:
    r = subprocess.run(["latexmk", "-xelatex", "-interaction=nonstopmode", "-halt-on-error", "artigo.tex"],
                       cwd=DIR, capture_output=True, text=True)
    log = (DIR / "artigo.log").read_text(encoding="utf-8", errors="replace")
    if r.returncode != 0:
        print(log[-3000:])
        sys.exit("falha na compilação")
    info = subprocess.run(["pdfinfo", str(DIR / "artigo.pdf")], capture_output=True, text=True).stdout
    paginas = int(re.search(r"Pages:\s+(\d+)", info).group(1))
    ausentes = sorted(set(re.findall(r"Missing character: There is no (.+?) in font", log)))
    largas = sum(float(x) > 1 for x in re.findall(r"Overfull \\hbox \((\d+\.\d+)pt too wide", log))  # < 1 pt não se vê
    print(f"{DIR / 'artigo.pdf'}: {paginas} páginas (limite {LIMITE_PAGINAS}); "
          f"glifos ausentes: {ausentes or 'nenhum'}; linhas estouradas: {largas}")
    if paginas > LIMITE_PAGINAS or ausentes:
        sys.exit(1)


if __name__ == "__main__":
    gerar()
    if "--pdf" in sys.argv:
        compilar()
