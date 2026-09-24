"""Hiperlinks do artigo, comuns a gerar_tex.py e gerar_docx.py.

- Caminhos de dados e scripts citados no texto (entre crases no .md, como `analise/tabelas/07_funil_por_ciclo.csv`)
  viram links para o arquivo no GitHub (blob) ou para a pasta (tree). Nomes sem pasta são procurados em
  analise/tabelas/, analise/ e dados/; curingas (`07_*.csv`) apontam para a pasta onde estão os arquivos.
- DOIs das referências ("DOI: 10.xxxx/...") viram links para https://doi.org/.

Os links apontam para o ramo main (público); outro ramo pode ser escolhido com a variável AVAL_POL_REF.
"""
from __future__ import annotations

import os
import re
from functools import lru_cache
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
REPO = "https://github.com/fcarva/aval-pol"
PASTAS_PROCURA = ("analise/tabelas", "analise", "dados/processados", "dados/externos", "dados")
DOI = re.compile(r"(DOI: )(10\.\d{4,9}/\S+?)(\.?)$", flags=re.M)


@lru_cache(maxsize=1)
def ramo() -> str:
    return os.environ.get("AVAL_POL_REF") or "main"


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
