"""Gera a declaração de uso de IA (modelo do PPGEco/UFES) e o anexo com o registro do repositório.

Fontes do texto (não edite o .tex à mão):
- artigo/declaracao-uso-ia.md: a declaração, no modelo da disciplina (cabeçalho da UFES, itens "A [ferramenta] foi
  utilizada para [finalidade], na etapa de [etapa]" e o parágrafo de responsabilidade da Portaria CNPq nº 2.664/2026);
- artigo/relatorio-uso-ia.md: o anexo, que detalha o uso a partir do histórico git.

Os números do anexo vêm do `git log` dos ramos de trabalho e principal (REFS), lidos por este script, e entram no texto
por marcadores: {{chave}} para as contagens e {{data:<commit>}} para a data de um commit. As Tabelas 1 a 3 e a cronologia
(Quadro 5) são montadas aqui. Hash de commit entre crases (`0893982`) vira link para o commit no GitHub; caminhos viram
links permanentes (artigo/links.py). Horários em Brasília (UTC−3).

Saídas: artigo/latex/declaracao-ia.tex (só a declaração, uma página) e artigo/latex/uso-ia.tex (declaração e anexo).
Uso: python artigo/gerar_uso_ia.py [--pdf]
     --pdf compila os dois com XeLaTeX e lista páginas, glifos ausentes e linhas estouradas.
"""
from __future__ import annotations

import csv
import re
import subprocess
import sys
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

import pypandoc
import yaml

from gerar_tex import (FORMATO, PREAMBULO, ancora, celulas, md_latex, preparar, remissoes, secoes, separar_blocos,
                       tabela_latex)
from links import REPO

ART = Path(__file__).resolve().parent
RAIZ = ART.parent
DIR = ART / "latex"
MD_DECL = ART / "declaracao-uso-ia.md"
MD_ANEXO = ART / "relatorio-uso-ia.md"
REFS = ("HEAD", "origin/main")  # ramo de trabalho e principal (o merge do PR #1 só está no main)
BRT = timezone(timedelta(hours=-3))
AUTOR = {"fcarva", "Felipe"}
AGENTE = "Claude"
RELE = "github-actions[bot]"
ORIGENS = {"autor": "Autor", "agente": "Agente de IA (Claude Code)", "rele": "Relé de coleta (GitHub Actions)",
           "merge": "Mesclagens de ramos"}
AREAS = [  # prefixo, nome na tabela, conteúdo
    ("artigo/auditoria/", "artigo/auditoria", "checagens de números e referências, pareceres das revisões"),
    ("artigo/latex/", "artigo/latex", ".tex gerados e figura"),
    ("artigo/", "artigo (demais)", "texto-fonte, geradores do Word e do LaTeX, roteiros"),
    ("analise/", "analise", "scripts, tabelas e figuras"),
    ("dados/fontes_web/", "dados/fontes_web", "pedidos ao relé e coletas do Firecrawl"),
    ("dados/", "dados (demais)", "bases tratadas"),
    ("notas/", "notas", "sínteses de normas, literatura, dados e desenho"),
    (".github/", ".github", "automação do relé"),
    ("CLAUDE.md", "CLAUDE.md", "regras e decisões de escopo do projeto"),
    (".gitignore", ".gitignore", "o que fica fora do controle de versão"),
    ("", "outros", ""),
]
CABECALHO_TEX = """% !TEX program = xelatex
% Gerado por artigo/gerar_uso_ia.py a partir de artigo/declaracao-uso-ia.md e artigo/relatorio-uso-ia.md.
% Não edite à mão: altere os .md e rode `python artigo/gerar_uso_ia.py --pdf`.
"""


def git(*args: str) -> str:
    return subprocess.run(["git", "-C", str(RAIZ), *args], capture_output=True, text=True, check=True).stdout


def historico() -> list[dict]:
    """Commits alcançáveis por REFS, com origem, data em Brasília, linhas e arquivos."""
    fmt = "%x1e%H%x1f%an%x1f%at%x1f%P%x1f%s%x1f%(trailers:key=Co-Authored-By,valueonly,separator=%x2c)"
    saida = []
    for bloco in git("log", "--no-renames", "--numstat", f"--format={fmt}", *REFS).split("\x1e")[1:]:
        cab, *linhas = bloco.split("\n")
        sha, autor, quando, pais, assunto, coautor = cab.split("\x1f")
        numstat = []  # (caminho, linhas incluídas, linhas excluídas); binários contam zero linhas
        for l in linhas:
            if l.strip():
                a, d, caminho = l.split("\t", 2)
                numstat.append((caminho, int(a) if a != "-" else 0, int(d) if d != "-" else 0))
        if len(pais.split()) > 1:
            origem = "merge"
        elif autor == RELE:
            origem = "rele"
        elif autor == AGENTE:
            origem = "agente"
        elif autor in AUTOR:
            origem = "autor"
        else:
            raise SystemExit(f"autor não classificado: {autor} ({sha[:7]})")
        etapa = re.match(r"buscar-fontes: (.+?) \(", assunto)
        saida.append({"sha": sha, "curto": sha[:7], "autor": autor, "origem": origem, "assunto": assunto,
                      "quando": datetime.fromtimestamp(int(quando), BRT),
                      "mais": sum(x[1] for x in numstat), "menos": sum(x[2] for x in numstat), "numstat": numstat,
                      "arquivos": [x[0] for x in numstat], "coautoria": "anthropic.com" in coautor,
                      "etapa": etapa.group(1) if etapa else None})
    return sorted(saida, key=lambda c: c["quando"])


def n(x: int) -> str:
    return f"{x:,}".replace(",", ".")


def dia(c: dict) -> str:
    return c["quando"].strftime("%d/%m")


def tabela(titulo: str, cab: list[str], linhas: list[list], fonte: str, larguras: list[int]) -> str:
    sep = "| " + " | ".join("-" * w for w in larguras) + " |"
    corpo = ["| " + " | ".join(str(x) for x in l) + " |" for l in linhas]
    return "\n".join([f"**{titulo}**", "", "| " + " | ".join(cab) + " |", sep, *corpo, "", f"Fonte: {fonte}"])


def fonte_git(extra: str = "") -> str:
    return (f"`git log` dos ramos `claude/fervent-shannon-jq7142` e `main` até `{HEAD[:7]}`{extra}; "
            "gerado por `artigo/gerar_uso_ia.py`.")


def tabela_origens(cs: list[dict]) -> str:
    dias = sorted({dia(c) for c in cs}, key=lambda d: d[3:] + d[:2])
    linhas = []
    for o, nome in ORIGENS.items():
        sub = [c for c in cs if c["origem"] == o]
        por_dia = [sum(dia(c) == d for c in sub) for d in dias]
        linhas.append([nome, *[n(x) if x else "–" for x in por_dia], n(len(sub)),
                       n(sum(c["mais"] for c in sub)), n(sum(c["menos"] for c in sub))])
    linhas.append(["**Total**", *[f"**{n(sum(dia(c) == d for c in cs))}**" for d in dias], f"**{n(len(cs))}**",
                   f"**{n(sum(c['mais'] for c in cs))}**", f"**{n(sum(c['menos'] for c in cs))}**"])
    return tabela("Tabela 1 – Commits por origem e dia (horário de Brasília)",
                  ["Origem", *dias, "Total", "Linhas incluídas", "Linhas excluídas"], linhas,
                  fonte_git("; mesclagens não alteram linhas por conta própria"),
                  [22] + [5] * len(dias) + [5, 8, 8])


def tabela_areas(cs: list[dict]) -> str:
    arq, mais, menos = defaultdict(set), defaultdict(int), defaultdict(int)
    for c in cs:
        if c["origem"] != "agente":
            continue
        for caminho, a, d in c["numstat"]:
            nome = next(nome for pref, nome, _ in AREAS if caminho.startswith(pref))
            arq[nome].add(caminho)
            mais[nome] += a
            menos[nome] += d
    linhas = [[f"`{nome}`" if nome != "outros" and "(" not in nome else nome, conteudo, n(len(arq[nome])),
               n(mais[nome]), n(menos[nome])] for _, nome, conteudo in AREAS if arq[nome]]
    todos = set().union(*arq.values())
    linhas.append(["**Total**", "", f"**{n(len(todos))}**", f"**{n(sum(mais.values()))}**",
                   f"**{n(sum(menos.values()))}**"])
    return tabela("Tabela 2 – Arquivos alterados pelos commits do agente, por pasta",
                  ["Pasta", "Conteúdo", "Arquivos distintos", "Linhas incluídas", "Linhas excluídas"], linhas,
                  fonte_git("; só commits do agente, sem mesclagens"), [16, 34, 9, 9, 9])


def tabela_rele(cs: list[dict]) -> str:
    grupos = defaultdict(list)
    for c in cs:
        if c["origem"] == "rele":
            grupos[c["etapa"] or "outras"].append(c)
    linhas = []
    for etapa, sub in sorted(grupos.items(), key=lambda kv: -len(kv[1])):
        arquivos = {a for c in sub for a in c["arquivos"]}
        periodo = f"{dia(sub[0])} a {dia(sub[-1])}" if dia(sub[0]) != dia(sub[-1]) else dia(sub[0])
        linhas.append([etapa[0].upper() + etapa[1:], n(len(sub)), n(len(arquivos)), periodo])
    rele = [c for c in cs if c["origem"] == "rele"]
    linhas.append(["**Total**", f"**{n(len(rele))}**", f"**{n(len({a for c in rele for a in c['arquivos']}))}**", ""])
    return tabela("Tabela 3 – Coletas devolvidas pelo relé, por etapa",
                  ["Etapa do relé", "Commits", "Arquivos distintos", "Período"], linhas,
                  fonte_git("; commits de `github-actions[bot]`"), [24, 8, 10, 12])


def escapar(texto: str) -> str:
    """Assunto de commit como texto literal no markdown."""
    texto = re.sub(r"([\\`*_\[\]<>#$|~^])", r"\\\1", texto)
    return texto.replace("→", "$\\rightarrow$")


def link_commit(sha: str) -> str:
    return f"[{sha[:7]}]({REPO}/commit/{sha})"


def cronologia(cs: list[dict]) -> str:
    linhas = [[c["quando"].strftime("%d/%m %H:%M"), link_commit(c["sha"]),
               "Autor" if c["origem"] == "autor" or c["autor"] in AUTOR else "Agente", escapar(c["assunto"])]
              for c in cs if c["origem"] == "agente" or c["autor"] in AUTOR]
    return tabela("Quadro 5 – Cronologia dos commits do autor e do agente",
                  ["Data e hora", "Commit", "Origem", "Mensagem do commit"], linhas,
                  fonte_git("; sem as coletas do relé (Tabela 3) e sem as mesclagens feitas pelo agente"),
                  [11, 8, 7, 58])


def contagens(cs: list[dict]) -> dict[str, str]:
    por = defaultdict(list)
    for c in cs:
        por[c["origem"]].append(c)
    agente = por["agente"]
    ini = next(c for c in cs if c["origem"] == "autor")
    dados = list(csv.DictReader((ART / "auditoria" / "checagem_dados.csv").open(encoding="utf-8")))
    refs = list(csv.DictReader((ART / "auditoria" / "checagem_referencias.csv").open(encoding="utf-8")))
    capt = list(csv.DictReader((ART / "auditoria" / "auditoria_captacao_checagens.csv").open(encoding="utf-8")))
    v = {
        "head": HEAD[:7], "head_data": next(c for c in cs if c["sha"] == HEAD)["quando"].strftime("%d/%m/%Y, %Hh%M"),
        "n_total": len(cs), "n_agente": len(agente), "n_rele": len(por["rele"]), "n_autor": len(por["autor"]),
        "n_merges": len(por["merge"]),
        "n_merges_autor": sum(c["autor"] in AUTOR for c in por["merge"]),
        "n_coautoria": sum(c["coautoria"] for c in agente),
        "ag_arquivos": len({a for c in agente for a in c["arquivos"]}),
        "ag_mais": sum(c["mais"] for c in agente), "ag_menos": sum(c["menos"] for c in agente),
        "ini_curto": ini["curto"], "ini_arquivos": len(ini["arquivos"]), "ini_mais": ini["mais"],
        "rele_arquivos": len({a for c in por["rele"] for a in c["arquivos"]}),
        "rele_etapas": len({c["etapa"] for c in por["rele"]}),
        "primeiro": cs[0]["quando"].strftime("%d/%m"), "ultimo": cs[-1]["quando"].strftime("%d/%m"),
        "checagens": len(dados), "checagens_ok": sum(r["status"] == "CONFERE" for r in dados),
        "refs": len(refs), "refs_doi": sum(r["status"] == "VERIFIED" for r in refs),
        "refs_sem_doi": sum(r["status"] == "sem_doi" for r in refs),
        "captacao": len(capt), "captacao_ok": sum(r["status"].lower() == "confere" for r in capt),
    }
    return {k: n(x) if isinstance(x, int) else x for k, x in v.items()}


def preencher(md: str, v: dict[str, str], cs: list[dict]) -> str:
    por_sha = {c["curto"]: c for c in cs}

    def marca(m: re.Match) -> str:
        chave = m.group(1)
        if chave.startswith("data:"):
            return por_sha[chave[5:]]["quando"].strftime("%d/%m")
        if chave not in v:
            raise SystemExit(f"marcador sem valor: {chave}")
        return v[chave]
    md = re.sub(r"\{\{([\w:]+)\}\}", marca, md)

    def commit(m: re.Match) -> str:
        c = por_sha.get(m.group(1)[:7])
        return link_commit(c["sha"]) if c else m.group(0)
    return re.sub(r"`([0-9a-f]{7,40})`", commit, md)


def ler(md: Path) -> tuple[dict, str]:
    texto = md.read_text(encoding="utf-8")
    m = re.match(r"---\n(.*?)\n---\n", texto, flags=re.S)
    return yaml.safe_load(m.group(1)), re.sub(r"<!--.*?-->", "", texto[m.end():], flags=re.S).strip()


def converter(md: str) -> tuple[str, set[str]]:
    """Markdown com quadros e tabelas no padrão do artigo (título acima, fonte abaixo) → LaTeX."""
    corpo, blocos = separar_blocos(md)
    trechos = []
    for b in blocos:
        trechos += [b["titulo"], b["fonte"]]
        linhas = [l for l in b["objeto"].splitlines() if l.strip()]
        trechos += [c for l in linhas[:1] + linhas[2:] for c in celulas(l)]
    conv = dict(zip(trechos, md_latex(trechos))) if trechos else {}
    tex = pypandoc.convert_text(corpo, "latex", format=FORMATO, extra_args=["--wrap=auto", "--columns=100"])
    for k, b in enumerate(blocos):
        tex = tex.replace(f"XXBLOCO{k}XX", tabela_latex(b, conv.__getitem__))
    return tex, {ancora(b["titulo"]) for b in blocos}


def declaracao(com_anexo: bool) -> str:
    """Página da declaração; sem o anexo, sai a frase que remete a ele (bloco ::: anexo do .md)."""
    meta, corpo = ler(MD_DECL)
    if not com_anexo:
        corpo = re.sub(r"^::: anexo\n.*?^:::\n?", "", corpo + "\n", flags=re.S | re.M).strip()
    texto = pypandoc.convert_text(corpo, "latex", format=FORMATO, extra_args=["--wrap=auto", "--columns=100"])
    instituicao = "\n".join(rf"{{\bfseries {linha}\par}}" for linha in meta["instituicao"])
    # local e data, nome e, em corpo menor, a identificação do trabalho
    assinatura = "\n".join(rf"{linha}\par" if i < 2 else rf"{{\small {linha}\par}}"
                           for i, linha in enumerate(md_latex(meta["assinatura"])))
    return "\n".join([
        r"\thispagestyle{empty}",
        r"\begin{center}", instituicao, r"\vspace{12pt}", rf"{{\bfseries {meta['title']}\par}}", r"\end{center}",
        r"\vspace{6pt}",
        r"\begingroup\setlength{\parindent}{0pt}\setlength{\parskip}{6pt}\setlist[itemize]{itemsep=2pt, topsep=3pt}",
        texto.strip(),
        r"\par\endgroup",
        r"\vspace{14pt}",
        r"\begin{center}", assinatura, r"\end{center}",
    ])


def anexo(cs: list[dict]) -> tuple[str, dict]:
    meta, corpo = ler(MD_ANEXO)
    v = contagens(cs)
    corpo = preencher(corpo, v, cs)
    for marcador, gerar in {"tabela-origens": tabela_origens, "tabela-areas": tabela_areas,
                            "tabela-rele": tabela_rele}.items():
        corpo = corpo.replace(f"[[{marcador}]]", gerar(cs))
    assert "[[" not in corpo, re.findall(r"\[\[[\w-]+\]\]", corpo)
    corpo = preparar(corpo)  # caminhos → links permanentes, citações → referências, DOIs → doi.org
    tex, ancoras = converter(corpo)
    tex = secoes(tex)
    apendice, ancoras_ap = converter(preparar(cronologia(cs)))
    tex += "\n\\section*{Apêndice – Cronologia dos commits}\n" + apendice
    tex = remissoes(tex, ancoras | ancoras_ap)
    titulo = rf"\begin{{center}}{{\bfseries {meta['title']}\par}}\end{{center}}" + "\n\\vspace{6pt}\n"
    return titulo + tex, meta


def gerar() -> None:
    cs = historico()
    dmeta, _ = ler(MD_DECL)
    pre = CABECALHO_TEX + re.sub(r"\A% !TEX program = xelatex\n(?:%.*\n)+", "", PREAMBULO)
    # quadros e tabelas flutuam só dentro da própria seção (não caem nas Referências)
    info = (r"\usepackage[section]{placeins}" + "\n" + rf"\hypersetup{{pdftitle={{{dmeta['pdf_title']}}}, pdfauthor={{{dmeta['author']}}}, "
            rf"pdfsubject={{{dmeta['subject']}}}, pdflang={{pt-BR}}}}")
    DIR.mkdir(parents=True, exist_ok=True)
    (DIR / "declaracao-ia.tex").write_text(pre + info + "\n\n\\begin{document}\n\n" + declaracao(False)
                                           + "\n\n\\end{document}\n", encoding="utf-8")
    corpo_anexo, _ = anexo(cs)
    (DIR / "uso-ia.tex").write_text(pre + info + "\n\n\\begin{document}\n\n" + declaracao(True) + "\n\n\\newpage\n\n"
                                    + corpo_anexo.strip() + "\n\n\\end{document}\n", encoding="utf-8")
    print(DIR / "declaracao-ia.tex")
    print(DIR / "uso-ia.tex")


def compilar() -> None:
    for nome in ("declaracao-ia", "uso-ia"):
        r = subprocess.run(["latexmk", "-xelatex", "-interaction=nonstopmode", "-halt-on-error", f"{nome}.tex"],
                           cwd=DIR, capture_output=True, text=True)
        log = (DIR / f"{nome}.log").read_text(encoding="utf-8", errors="replace")
        if r.returncode != 0:
            print(log[-3000:])
            sys.exit(f"falha na compilação de {nome}.tex")
        info = subprocess.run(["pdfinfo", str(DIR / f"{nome}.pdf")], capture_output=True, text=True).stdout
        paginas = int(re.search(r"Pages:\s+(\d+)", info).group(1))
        ausentes = sorted(set(re.findall(r"Missing character: There is no (.+?) in font", log)))
        largas = sum(float(x) > 1 for x in re.findall(r"Overfull \\hbox \((\d+\.\d+)pt too wide", log))
        print(f"{DIR / (nome + '.pdf')}: {paginas} páginas; glifos ausentes: {ausentes or 'nenhum'}; "
              f"linhas estouradas: {largas}")
        if ausentes:
            sys.exit(1)


HEAD = git("rev-parse", "HEAD").strip()

if __name__ == "__main__":
    gerar()
    if "--pdf" in sys.argv:
        compilar()
