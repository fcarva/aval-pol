"""
Roteiro de revisão frase a frase da versão final do artigo (para o autor revisar, editar e auditar).

Lê artigo/rascunho-artigo.md (fonte única do texto) e escreve, na ordem do artigo:
  - para cada parágrafo, o passo que ele cumpre no argumento (PASSOS, abaixo; parágrafo novo fica "passo a definir");
  - cada frase, literal, numerada (seção.parágrafo.frase) e com caixa de marcação;
  - a base da frase: citações, checagens de dados que cobrem o trecho (artigo/auditoria/checagem_dados.csv, com o
    status da última execução) e os números que nenhuma checagem cobre ("conferir na fonte citada");
  - quadros e tabelas linha a linha; os textos da Figura 1 (analise/08_figura_teoria_da_mudanca.py);
  - as referências, com o status da conferência (artigo/auditoria/checagem_referencias.csv).

Saídas: artigo/revisao-final/frase-a-frase.md e frase-a-frase.docx (pandoc).
Uso: python artigo/revisao-final/gerar_frase_a_frase.py  (rodar antes checar_dados.py e checar_referencias.py)
"""
from __future__ import annotations

import csv
import hashlib
import importlib.util
import re
import subprocess
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
ART = RAIZ / "artigo" / "rascunho-artigo.md"
AUD = RAIZ / "artigo" / "auditoria"
SAIDA = Path(__file__).with_name("frase-a-frase.md")

# passo de cada parágrafo no argumento, pela abertura do parágrafo
PASSOS = [
    ("**Resumo.**", "O artigo em um parágrafo: mecanismo, o que se avalia, os achados de desenho e a proposta"),
    ("**Palavras-chave", "Palavras-chave"),
    ("A Lei estadual nº 11.246", "Apresenta a lei e dimensiona a política: teto anual, teto esgotado e demanda habilitada acima do teto"),
    ("O setor cultural capixaba é pequeno", "Reconstrói o problema que a lei não declara e o enuncia"),
    ("A avaliação da LICC se justifica", "Justifica a avaliação: gasto fora do orçamento e decisão privada"),
    ("O artigo tem dois objetivos", "Declara os objetivos e o roteiro do artigo"),
    ("A LICC é um **gasto tributário", "Descreve o fluxo do mecanismo: inscrição, habilitação, patrocínio e crédito"),
    ("Três características do arranjo", "Destaca os três traços do arranjo que guiam a avaliação"),
    ("**Despesa tributária com decisão privada.**", "Situa a LICC na literatura: incentivo fiscal com decisão privada e a cultura como bem público"),
    ("**A experiência brasileira com a Lei Rouanet.**", "Traz a experiência da Lei Rouanet: concentração, mercado de patrocínios e adicionalidade"),
    ("**Evidência causal.**", "Mostra que a evidência sobre incentivos estaduais no Brasil é descritiva"),
    ("A teoria da mudança da LICC (Figura 1)", "Explica como a teoria da mudança é reconstruída e por que tem três cadeias"),
    ("A hipótese causal é:", "Enuncia a hipótese causal no formato do J-PAL"),
    ("Cada seta da cadeia carrega", "Define as cinco premissas testadas (H1 a H5) e os riscos"),
    ("Aplicam-se as perguntas usuais", "Declara as perguntas de avaliação de desenho e a classificação das premissas"),
    ("**Problema e objetivos.**", "Avalia problema e objetivos: sem objetivo mensurável, meta ou indicador"),
    ("**Funil de atrito e indicadores.**", "Avalia o funil de atrito e os indicadores da cadeia"),
    ("**Exclusão na entrada (H4).**", "Audita H4: barreiras de entrada, difusão territorial, projetos pequenos, acúmulo no teto"),
    ("**Decisão concentrada (H2).**", "Audita H2: parecer sem nota, papel da comissão, inabilitações, racionamento pela ordem"),
    ("**Marketing (H1).**", "Audita H1: a marca como retorno privado e o peso de cada empresa pelo imposto"),
    ("**Taxa de serviço (H3).**", "Audita H3: quanto os tetos de custos permitem pagar à intermediação"),
    ("**Entrega e território.**", "Audita H5 e o território: reserva para eventos antigos, RMGV, Gini e Theil"),
    ("Em síntese, o desenho", "Sintetiza a avaliação do desenho e liga à proposta"),
    ("As premissas do Quadro 2 convertem-se", "Converte as premissas em perguntas e define a notação e o viés da comparação simples"),
    ("As regras de operação determinam", "Justifica a escolha dos métodos pelas regras de operação"),
    ("- **H5.**", "Estratégia para H5: margem do racionamento, reentrada e instrumento"),
    ("- **H1.**", "Estratégia para H1: experimento conjunto com decisores"),
    ("- **H4.**", "Estratégia para H4: promoção aleatória por município e braços entre agentes"),
    ("- **H2.**", "Estratégia para H2: severidade do parecerista como instrumento (exploratória)"),
    ("**O que fica aberto.**", "Lista os métodos que ficam para depois"),
    ("Para H5 e H2, trabalha-se com o universo", "Define populações, listagens e a chave de ligação por CNPJ"),
    ("Para resultados binários, o efeito mínimo", "Apresenta a fórmula do efeito mínimo detectável"),
    ("A fórmula segue Djimeu", "Define os parâmetros da fórmula"),
    ("A comparação na margem do racionamento", "Interpreta o poder de cada desenho: margem, VI, conjunto, conglomerados e adesão"),
    ("A primeira ameaça à validade interna", "Lista as ameaças à validade interna e externa e os cuidados éticos"),
    ("A LICC é um gasto tributário que mais", "Resume os achados do desenho"),
    ("Sem alterar o mecanismo, a gestão", "Recomenda o que a gestão pode fazer sem mudar o mecanismo"),
    ("Das quatro perguntas, a da entrega", "Retoma a pergunta central (H5), a implicação para o teto e as limitações"),
]
ABREV = {"al", "art", "arts", "p", "n", "v", "dec", "nº", "set", "jan", "fev", "mar", "abr", "mai", "jun", "jul",
         "ago", "out", "nov", "dez", "sr", "sra", "etc", "ed", "org", "cf", "mi", "fig", "tab", "ex"}
CITACAO = re.compile(r"\([^()]*?[A-ZÀ-Ú]{2,}[^()]*?,\s*(?:19|20)\d{2}[a-h]?\b[^()]*\)")
CITACAO_NARR = re.compile(r"[A-ZÀ-Ú][\w'’-]+(?:,? (?:e|&) [A-ZÀ-Ú][\w'’-]+)*(?: \*et al\.\*)? \((?:19|20)\d{2}[a-h]?\)")
NAO_NUMERO = re.compile(
    r"\([^()]*?[A-ZÀ-Ú]{2,}[^()]*?,\s*(?:19|20)\d{2}[a-h]?\b[^()]*\)|\barts?\.\s*[\dº\-–, e]+|\bnº\s*[\d./\-A-Z]+|\b\d{1,2}\.\d{3}/\d{4}\b"
    r"|\bIN \d{3}/\d{4}|\bDec\. [\d.\-R/]+|\bLC \d+/\d{4}|\bLei [\d./]+|\bH\d\b|\b(?:Quadro|Tabela|Figura|seção|Seção) \d(?:\.\d)?"
    r"|§ ?\d+º?|\b(?:19|20)\d{2}(?:[-–](?:19|20)?\d{2,4})?\b|\bPECO \d+-\d+|`[^`]*`|<[^>]*>|\$[^$]*\$|\[\^[^\]]*\]"
    r"|\bRI?\d\b|\bA\d\b|\bP\d\b|\*?Y\*?\(\d\)|\b[aA] (?:seção )?\d(?= [a-zà-ú])")
NUMERO = re.compile(r"\d+(?:[.,]\d+)*(?:\s?%)?")


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def checagens() -> list[dict]:
    with (AUD / "checagem_dados.csv").open(encoding="utf-8") as f:
        return list(csv.DictReader(f))


def refs_status() -> list[dict]:
    with (AUD / "checagem_referencias.csv").open(encoding="utf-8") as f:
        return list(csv.DictReader(f))


def frases(texto: str) -> list[tuple[int, int]]:
    """Intervalos (início, fim) das frases no texto cru, sem cortar em abreviatura nem em "*et al.*"."""
    cortes, ini = [], 0
    for m in re.finditer(r"[.?!][\"”»)*]*(?:\[\^[^\]]+\])?\s+", texto):
        antes = re.sub(r"[*\"”»)]+$", "", texto[ini:m.start()]).split()
        ult = antes[-1].lower().strip("(*") if antes else ""
        prox = texto[m.end():m.end() + 1]
        if ult in ABREV or not re.match(r"[A-ZÀ-Ú\"“*\d]", prox):
            continue
        if re.fullmatch(r"\*\*[^*]+[.:]\*\*", texto[ini:m.end()].strip()):  # rótulo em negrito no início
            continue
        cortes.append((ini, m.end()))
        ini = m.end()
    if texto[ini:].strip():
        cortes.append((ini, len(texto)))
    return cortes


def base(texto: str, ini: int, fim: int, chk: list[dict]) -> list[str]:
    f = texto[ini:fim]
    itens = []
    cits = [c.strip("()") for c in CITACAO.findall(f)] + CITACAO_NARR.findall(f)
    if cits:
        itens.append("citações: " + "; ".join(dict.fromkeys(cits)))
    cobertos, ids = [], []
    for c in chk:
        j = texto.find(c["trecho"])
        while j >= 0:
            if j < fim and j + len(c["trecho"]) > ini:
                cobertos.append((j, j + len(c["trecho"])))
                ids.append(f"{c['id']} {'✔' if c['status'] == 'CONFERE' else '✘ ' + c['status']} "
                           f"(`{c['fonte'].split(';')[0].strip()}`)")
            j = texto.find(c["trecho"], j + 1)
    if ids:
        itens.append("checagem de dados: " + "; ".join(dict.fromkeys(ids)))
    mascara = [(m.start() + ini, m.end() + ini) for m in NAO_NUMERO.finditer(f)]
    soltos = []
    for m in NUMERO.finditer(f):
        a, b = m.start() + ini, m.end() + ini
        if any(x <= a and b <= y for x, y in mascara) or any(x <= a < y for x, y in cobertos):
            continue
        soltos.append(m.group().strip().rstrip(".,"))
    soltos = [s for s in dict.fromkeys(soltos) if s]
    if soltos:
        itens.append("⚠ números sem checagem automática (conferir na fonte citada): " + ", ".join(soltos))
    return itens


def tipo(frase: str) -> str:
    """Número de regra (a frase cita norma) ou dado/literatura (conferir na tabela ou no texto citado)."""
    norma = r"\barts?\.|\bIN \d|IN 00|Dec\.|\bLei\b|Portaria|LC \d|SECULT, 20\d\d[a-h]?, arts?|ESPÍRITO SANTO, 2021b"
    return "regra de norma" if re.search(norma, frase) else "dado ou literatura"


def limpa(s: str) -> str:
    s = re.sub(r"\[\^([^\]]+)\]", r" [nota de rodapé: \1]", s)
    return s.strip()


def passo(bloco: str) -> str | None:
    for chave, txt in PASSOS:
        if bloco.startswith(chave):
            return txt
    return None


def figura() -> list[str]:
    spec = importlib.util.spec_from_file_location("fig08", RAIZ / "analise" / "08_figura_teoria_da_mudanca.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    linhas = []
    for nivel, caixas in mod.CAIXAS.items():
        for _, titulo, texto, quem in caixas:
            t = f"{titulo}: {texto}" if titulo else texto
            linhas.append(t + (f" (quem decide: {quem})" if quem else ""))
    linhas += [f"{h} · {t}: {x}" for h, t, x in mod.PREMISSAS]
    return linhas


def main() -> None:
    md = ART.read_text(encoding="utf-8")
    chk = checagens()
    yaml, corpo = md.split("\n---\n", 1) if md.startswith("---") else ("", md)
    titulo = re.search(r'title: "(.*)"', yaml).group(1) if yaml else ""
    corpo, refs = corpo.split("\n# Referências\n", 1)
    notas = dict(re.findall(r"^\[\^([^\]]+)\]: (.*)$", corpo, flags=re.M))
    corpo = re.sub(r"^\[\^[^\]]+\]: .*$", "", corpo, flags=re.M)
    blocos = [b.strip() for b in re.split(r"\n\s*\n", corpo) if b.strip()]
    # itens de lista viram blocos próprios
    exp = []
    for b in blocos:
        if b.startswith("- "):
            exp += ["- " + x for x in re.split(r"\n- ", b[2:])]
        else:
            exp.append(b)

    out = [
        "# Revisão final frase a frase",
        "",
        f"- **Texto revisado:** `artigo/rascunho-artigo.md`, sha256 `{sha(ART)[:16]}…`, gerado por "
        "`artigo/revisao-final/gerar_frase_a_frase.py`.",
        "- **Como usar:** cada parágrafo abre com o **passo** que ele cumpre no argumento. Cada frase vem literal, "
        "numerada como seção.parágrafo.frase, com uma caixa ☐ para marcar (☒ ok; ✎ editar). As edições vão para "
        "o `rascunho-artigo.md`; depois, rodar de novo `checar_dados.py`, `checar_referencias.py`, "
        "`gerar_tex.py --pdf` e este script.",
        "- **Base de cada frase:**",
        "  - *citações*: as referências que a frase cita;",
        "  - *checagem de dados*: o número foi recalculado a partir da tabela indicada (✔ confere na última "
        "execução);",
        "  - *⚠ números sem checagem automática*: número que nenhuma checagem cobre; conferir na norma ou "
        "na fonte citada (muitos são regras de norma, como percentuais e tetos, e não dados).",
        "",
        "## Título",
        "",
        f"- ☐ **[0.1]** {titulo}",
        "",
        "## Resumo e palavras-chave",
        "",
    ]
    secao, par, pendentes, n_frases, n_chk = "0", 0, [], 0, 0
    for b in exp:
        if b.startswith("#"):
            nivel = len(b) - len(b.lstrip("#"))
            nome = b.lstrip("# ").strip()
            m = re.match(r"(\d+(?:\.\d+)?)", nome)
            if m:
                secao, par = m.group(1), 0
            out += ["", "#" * (nivel + 1) + " " + nome, ""]
            continue
        if b.startswith("!["):
            out += ["- **Figura 1 (textos da imagem, `analise/08_figura_teoria_da_mudanca.py`):**"]
            out += [f"  - ☐ {x}" for x in figura()]
            out.append("")
            continue
        if b.startswith("$$"):
            out += ["- ☐ **Fórmula do EMD** (conferir no PDF; parâmetros definidos na frase seguinte)", ""]
            continue
        if b.startswith("|"):
            linhas = [l for l in b.split("\n") if not re.match(r"^\|[-| ]+\|$", l)]
            cab = [c.strip() for c in linhas[0].strip("|").split("|")]
            out.append(f"- **Colunas:** {' · '.join(cab)}")
            for l in linhas[1:]:
                cel = [c.strip() for c in l.strip("|").split("|")]
                itens = base(b, b.find(l), b.find(l) + len(l), chk)
                n_frases += 1
                n_chk += any(i.startswith("checagem") for i in itens)
                out.append(f"  - ☐ **{cel[0]}** — " + " — ".join(cel[1:]))
                out += [f"    - {i}" for i in itens]
                pendentes += [(f"linha «{cel[0]}»", i, tipo(l)) for i in itens if i.startswith("⚠")]
            out.append("")
            continue
        if re.fullmatch(r"\*\*(Quadro|Tabela|Figura) \d+ – [^*]+\*\*", b):
            out += [f"### {b.strip('*')}", ""]
            continue
        par += 1
        p = passo(b)
        rotulo = re.match(r"^(?:- )?\*\*([^*]+?)[.:]?\*\*", b)
        cab = f"**{secao}.{par}**"
        if b.startswith("- "):
            b = b[2:]
        if b.startswith("Fonte:"):
            cab += " (fonte do quadro, tabela ou figura)"
        elif p:
            cab += f" — *Passo:* {p}"
        elif not b.startswith("Fonte:"):
            cab += " — *Passo:* (a definir)"
        out.append(f"- {cab}")
        for k, (i, f) in enumerate(frases(b), 1):
            txt = limpa(b[i:f])
            if rotulo and k == 1:
                txt = txt  # o rótulo em negrito fica na primeira frase
            itens = base(b, i, f, chk)
            n_frases += 1
            n_chk += any(x.startswith("checagem") for x in itens)
            out.append(f"  - ☐ **[{secao}.{par}.{k}]** {txt}")
            out += [f"    - {x}" for x in itens]
            pendentes += [(f"[{secao}.{par}.{k}]", x, tipo(b[i:f])) for x in itens if x.startswith("⚠")]
            for nota in re.findall(r"\[\^([^\]]+)\]", b[i:f]):
                if nota in notas:
                    out.append(f"    - ☐ *Nota de rodapé ({nota}):* {notas[nota]}")
                    for x in base(notas[nota], 0, len(notas[nota]), chk):
                        out.append(f"      - {x}")
        out.append("")

    out += ["", "## Referências", "",
            "Status da última conferência (`artigo/auditoria/checagem_referencias.csv`): VERIFIED = DOI conferido na "
            "Crossref sem divergência; sem_doi = referência sem DOI (norma, página oficial, livro), conferida na fonte "
            "indicada.", ""]
    st = refs_status()
    for r in [l.strip() for l in refs.split("\n") if l.strip()]:
        s = next((x for x in st if r.startswith(x["referencia"][:60])), None)
        rot = f"{s['status']}" + (f" — {s['problemas']}" if s and s.get("problemas") else "") if s else "sem status"
        out.append(f"- ☐ {r}")
        out.append(f"  - conferência: {rot}")
    out += ["", "## Números a conferir à mão", "",
            f"{n_frases} frases e linhas de tabela; {n_chk} com checagem automática de dados. Abaixo, as que têm "
            "números sem checagem automática (a maioria é regra de norma; conferir na fonte citada):", ""]
    for rot in ("dado ou literatura", "regra de norma"):
        sel = [(onde, o) for onde, o, t in pendentes if t == rot]
        out += [f"### {rot.capitalize()} ({len(sel)})", ""] + [f"- ☐ {onde}: {o.split(': ', 1)[1]}" for onde, o in sel] + [""]
    SAIDA.write_text("\n".join(out) + "\n", encoding="utf-8")
    import pypandoc
    pypandoc.convert_file(str(SAIDA), "docx", outputfile=str(SAIDA.with_suffix(".docx")),
                          extra_args=["--from=markdown-tex_math_dollars+tex_math_dollars"])
    print(f"{SAIDA.relative_to(RAIZ)}: {n_frases} frases/linhas, {n_chk} com checagem, {len(pendentes)} a conferir")


if __name__ == "__main__":
    main()
