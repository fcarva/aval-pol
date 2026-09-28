"""Hiperlinks do artigo, comuns a gerar_tex.py e gerar_docx.py.

- Caminhos de dados e scripts citados no texto (entre crases no .md, como `analise/tabelas/07_funil_por_ciclo.csv`)
  viram links para o arquivo no GitHub (blob) ou para a pasta (tree). Nomes sem pasta são procurados em
  analise/tabelas/, analise/ e dados/; curingas (`07_*.csv`) apontam para a pasta onde estão os arquivos.
- DOIs das referências ("DOI: 10.xxxx/...") viram links para https://doi.org/.
- Citações autor-data (ABNT) viram links para a entrada da lista de referências: o ano de "(SECULT, 2026b; 2026c)" ou de
  "Gertler *et al.* (2018)" leva à entrada, que ganha uma âncora invisível. O texto visível não muda; só liga quando o
  par (primeiro sobrenome ou sigla, ano de publicação) aponta para uma única entrada.

Os links do GitHub são permanentes: apontam para o commit publicado (SHA de HEAD, que precisa existir em origin),
porque o ramo main não tem todas as tabelas e um ramo muda com o tempo. A variável AVAL_POL_REF escolhe outro ref.
"""
from __future__ import annotations

import os
import re
import subprocess
import unicodedata
from functools import lru_cache
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
REPO = "https://github.com/fcarva/aval-pol"
PASTAS_PROCURA = ("analise/tabelas", "analise", "dados/processados", "dados/externos", "dados")
DOI = re.compile(r"(DOI: )(10\.\d{4,9}/\S+?)(\.?)$", flags=re.M)


@lru_cache(maxsize=1)
def ramo() -> str:
    """Ref dos links do GitHub: AVAL_POL_REF, ou o SHA de HEAD se o commit já estiver publicado, ou main."""
    if os.environ.get("AVAL_POL_REF"):
        return os.environ["AVAL_POL_REF"]
    git = ["git", "-C", str(RAIZ)]
    sha = subprocess.run(git + ["rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    publicado = subprocess.run(git + ["branch", "-r", "--contains", sha], capture_output=True, text=True).stdout.strip()
    if sha and publicado:
        return sha
    print(f"aviso: HEAD ({sha[:7]}) não está em origin; os links do GitHub apontam para main")
    return "main"


def url_caminho(caminho: str) -> str | None:
    """URL no GitHub para um caminho do repositório citado no texto, ou None se não existir."""
    c = caminho.strip().strip("/")
    if "*" in c:
        pasta = Path(c).parent.as_posix()
        pastas = [pasta] if pasta != "." else list(PASTAS_PROCURA)
        for p in pastas:
            if list((RAIZ / p).glob(Path(c).name)):
                return f"{REPO}/tree/{ramo()}/{p}"
        return None
    candidatos = [c] + ([f"{p}/{c}" for p in PASTAS_PROCURA] if "/" not in c else [])
    for cand in candidatos:
        alvo = RAIZ / cand
        if alvo.is_dir():
            return f"{REPO}/tree/{ramo()}/{cand}"
        if alvo.is_file():
            return f"{REPO}/blob/{ramo()}/{cand}"
    return None


def dois_em_links(md: str) -> str:
    """'DOI: 10.x/y.' → 'DOI: [10.x/y](https://doi.org/10.x/y).' (markdown; o pandoc converte para \\href ou hyperlink)."""
    return DOI.sub(lambda m: f"{m.group(1)}[{m.group(2)}](https://doi.org/{m.group(2)}){m.group(3)}", md)


def codigo_em_links_md(md: str) -> str:
    """`caminho` → [`caminho`](url) no markdown (para o .docx)."""
    def troca(m: re.Match) -> str:
        url = url_caminho(m.group(1))
        return f"[`{m.group(1)}`]({url})" if url else m.group(0)
    return re.sub(r"(?<!\[)`([^`\n]+)`", troca, md)


# ---------------------------------------------------------------- citações autor-data → referências
ANO = re.compile(r"(?<![\w/.-])((?:19|20)\d\d[a-z]?)(?![\w/-])")
MAIUSCULA = re.compile(r"[A-ZÀ-Ý][A-ZÀ-Ý'’-]+")


def _norm(palavra: str) -> str:
    p = "".join(c for c in unicodedata.normalize("NFD", palavra) if not unicodedata.combining(c))
    return p.upper().replace("’", "'")


def _entradas(refs: str) -> list[dict]:
    """Uma entrada por parágrafo da lista: primeira palavra (sobrenome ou sigla), anos de publicação e âncora."""
    saida = []
    for texto in [e.strip() for e in re.split(r"\n[ \t]*\n", refs) if e.strip()]:
        chave = _norm(re.match(r"[^\s,.(]+", texto).group(0))
        limpo = re.sub(r"Acesso em:\s*\d{1,2}º?\s+\w+\.?\s+\d{4}\.?|Dispon[íi]vel em:\s*\S+|DOI:\s*\S+|https?://\S+",
                       " ", texto)
        anos = set(ANO.findall(limpo))
        saida.append({"texto": texto, "chave": chave, "anos": anos, "limpo": limpo})
    return saida


def _resolver(entradas: list[dict], chave: str, ano: str) -> dict | None:
    achadas = [e for e in entradas if e["chave"] == chave and ano in e["anos"]]
    if len(achadas) > 1:  # desempate pelo ano da imprenta (", 2022."), e não por um ano citado no título
        achadas = [e for e in achadas if re.search(rf"[,:]\s*{ano}\.", e["limpo"])]
    return achadas[0] if len(achadas) == 1 else None


def citacoes_em_links(md: str, relatorio: list | None = None) -> str:
    """Liga cada ano citado no texto à entrada da lista de referências (âncora #ref-...).

    Só o texto antes de '# Referências' é lido; a lista ganha uma âncora vazia ([]{#ref-...}) no início de cada entrada.
    Em `relatorio` (se dado) entram as citações sem par e as entradas que nenhuma citação alcançou.
    """
    frente = ""
    m = re.match(r"---\n.*?\n---\n", md, flags=re.S)
    if m:
        frente, md = md[:m.end()], md[m.end():]
    i = md.find("# Referências")
    if i < 0:
        return frente + md
    corpo, refs = md[:i], md[i:]
    cab, lista = refs.split("\n", 1)
    entradas = _entradas(lista)
    chaves = {e["chave"] for e in entradas}
    for k, e in enumerate(entradas):
        e["id"] = "ref-" + re.sub(r"[^a-z0-9]+", "-", e["chave"].lower()).strip("-") + f"-{k + 1}"
    usadas, sem_par = set(), []

    def link(ano: str, chave: str | None) -> str:
        e = _resolver(entradas, chave, ano) if chave else None
        if not e:
            if chave:
                sem_par.append(f"{chave} {ano}")
            return ano
        usadas.add(e["id"])
        return f"[{ano}](#{e['id']})"

    def entre_parenteses(m: re.Match) -> str:
        dentro, autor, pos, partes = m.group(1), None, 0, []
        for a in ANO.finditer(dentro):
            trecho = dentro[pos:a.start()]
            achados = [_norm(w) for w in MAIUSCULA.findall(trecho) if _norm(w) in chaves]
            if achados:
                autor = achados[0]
            partes.append(trecho + link(a.group(1), autor))
            pos = a.end()
        return "(" + "".join(partes) + dentro[pos:] + ")"

    def narrativa(m: re.Match) -> str:
        antes = corpo_atual[max(0, m.start() - 70):m.start()]
        nomes = [_norm(w) for w in re.findall(r"[A-ZÀ-Ý][\wÀ-ÿ'’-]+", antes)]
        anos = ANO.findall(m.group(1))
        autor = next((n for n in reversed(nomes) if n in chaves and all(_resolver(entradas, n, a) for a in anos)), None)
        if not autor:
            return m.group(0)
        return "(" + ANO.sub(lambda a: link(a.group(1), autor), m.group(1)) + ")"

    # narrativas primeiro: "(2018)" ou "(2026b; 2026c)" logo depois do nome
    corpo_atual = corpo
    corpo = re.sub(r"\(((?:19|20)\d\d[a-z]?(?:;\s*(?:19|20)\d\d[a-z]?)*)\)", narrativa, corpo)
    # entre parênteses: grupos com ao menos um nome de autor e um ano (ignora os já ligados)
    corpo = re.sub(r"\(((?:[^()\n]|\([^()\n]*\))*?[A-ZÀ-Ý]{2}(?:[^()\n]|\([^()\n]*\))*?)\)",
                   lambda m: m.group(0) if "](#ref-" in m.group(0) else entre_parenteses(m), corpo)
    lista = "\n\n".join(f"[]{{#{e['id']}}}{e['texto']}" for e in entradas)
    if relatorio is not None:
        relatorio += [f"citação sem referência: {c}" for c in sem_par]
        relatorio += [f"referência não citada: {e['texto'][:70]}" for e in entradas if e["id"] not in usadas]
    return frente + corpo + cab + "\n\n" + lista + "\n"
