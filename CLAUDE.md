# aval-pol — Avaliação da LICC (PECO 5046-6046, UFES)

Mini artigo para a disciplina **Avaliação de Políticas Públicas** (PECO 5046-6046,
PPGEco/UFES, profs. Ana Carolina Giuberti e Renato Nunes de Lima Seixas):
**avaliação do desenho** da Lei de Incentivo à Cultura Capixaba (LICC) e
**proposta de avaliação de impacto**. Entrega: **28/09/2026**, Word ou PDF,
Times New Roman 12, espaçamento simples, **10 a 15 páginas** incluindo tabelas,
gráficos e referências. Trabalho em dupla.

Seções obrigatórias (instruções da disciplina): introdução com caracterização do
problema/necessidade; caracterização da política; breve revisão da literatura
sobre a política ou similares; desenho da política (com teoria da mudança) e sua
avaliação; proposta de avaliação de impacto com desenho da amostra, fonte de
dados e cálculo do poder estatístico; conclusão; referências.

**Fora do escopo:** financiamento quadrático ou qualquer redesenho do mecanismo.
Avalia-se a política **como ela está**.

## Onde ficam as coisas

| Caminho | Conteúdo |
| --- | --- |
| `*.pdf` (raiz) | Material da disciplina (originais, não versionar) |
| `disciplina/txt/` | Texto extraído dos PDFs (`pdftotext -layout`), para busca |
| `dados/licc/` | Dados herdados do repositório `fcarva/licc.gov` (transcrição oficial dos anexos da SECULT) |
| `licc-gov/` | Documentação, notas e código-chave do licc.gov (ontologia, normas, indicadores, armadilhas) |
| `ferramentas/academic-research-skills/` | Cópia do ARS (imbad0202); skills instaladas em `.claude/skills/` |
| `notas/` | Sínteses: `disciplina/`, `politica/`, `literatura/`, `dados/`, `desenho/` |
| `analise/` | Scripts Python, `tabelas/`, `figuras/` |
| `artigo/` | Mini artigo: `rascunho-artigo.md` é a fonte única do texto; `gerar_docx.py` gera o Word e `gerar_tex.py` gera `latex/artigo.tex` (XeLaTeX; `--pdf` compila e confere as 15 páginas); `auditoria/` confere dados e referências no .md |

## Regras herdadas do licc.gov — valem para o artigo

1. **Ausência não é zero.** Onde a fonte não publica um valor, ele fica ausente
   e a cobertura é declarada ("63 projetos, 40 com município"). Nunca estimar,
   interpolar ou arredondar em silêncio.
2. **Proveniência em todo número.** Cada estatística do artigo precisa apontar o
   arquivo em `dados/` ou a fonte oficial (URL) e o script em `analise/` que a
   produz. Número sem origem não entra no texto.
3. **"Li a norma" ≠ "consigo apurar o cumprimento".** Não afirmar descumprimento
   de regra (ex.: cotas do art. 18, limite por proponente) quando o dado não
   permite apurar — dizer "indeterminado" e por quê.
4. **Captados ≠ habilitados.** "RECURSO FINANCEIRO CAPTADO 2025" é o ano-calendário
   de captação; "HABILITADOS – ANO 2025" é o ciclo de habilitação, que capta no
   ano seguinte. Dos 63 que captaram em 2025, 30 foram habilitados em 2024.
5. **Cotas do art. 18 da IN 01/2025 são quatro:** 30% eventos calendarizados
   com mais de 10 anos, 10% planos plurianuais, 10% fora da RMGV, 50% demais.

## Regras de escrita acadêmica

- Português do Brasil, registro acadêmico de economia. Citações autor-data
  (ABNT NBR 10520/6023), salvo instrução contrária.
- **Toda referência precisa existir e ser verificada** (DOI, OpenAlex, Crossref,
  SciELO, página oficial). Referência não verificada não entra — marque
  `[VERIFICAR]` em vez de inventar. Afirmações atribuídas a um autor precisam
  estar de fato no texto citado.
- Material da disciplina é a espinha metodológica: teoria da mudança (Módulo 03,
  slides), resultados potenciais, validade interna/externa, amostragem e poder
  (slides PECO, 3ie WP26, Gertler et al.), guias do IJSN/SiMAPP.
- Uso de IA segue a Portaria CNPq 2664/2026: conteúdo de IA não é submetido como
  autoria humana; os autores revisam e respondem pelo texto; declaração de uso
  de IA vai anexa.

## Rede

Nesta máquina a rede funciona (secult.es.gov.br, mapa.cultura.es.gov.br,
servicodados.ibge.gov.br, api.openalex.org, transparencia.es.gov.br respondem).
`www3.al.es.gov.br` não respondeu.

Na sessão em nuvem a rede fica restrita ao GitHub e aos registros de pacotes. Para buscar fontes, edite
`dados/fontes_web/dois.txt` (DOIs), `buscas.tsv` (busca bibliográfica), `pedidos.tsv` (páginas e PDFs) ou
`salic_anos.txt` e faça push: o workflow `.github/workflows/buscar-fontes.yml` coleta num runner com rede
aberta e devolve o resultado por commit em `dados/fontes_web/` (ver `analise/rede/buscar_fontes.py`; HTML, PDF e .docx viram texto). Leia fontes online com WebFetch/firecrawl;
APIs JSON (IBGE, OpenAlex, Crossref) podem ser consultadas e as tabelas
derivadas salvas em `dados/`.
