# aval-pol — Avaliação da LICC (PECO 5046-6046, UFES)

Mini artigo para a disciplina **Avaliação de Políticas Públicas** (PECO 5046-6046,
PPGEco/UFES, profs. Ana Carolina Giuberti e Renato Nunes de Lima Seixas):
**avaliação do desenho** da Lei de Incentivo à Cultura Capixaba (LICC) e
**proposta de avaliação de impacto**. Entrega: **28/09/2026**, Word ou PDF,
Times New Roman 12, espaçamento simples, **10 a 15 páginas** incluindo tabelas,
gráficos e referências. Trabalho individual (autor único: voz impessoal no texto, sem 1ª pessoa do plural).

Seções obrigatórias (instruções da disciplina): introdução com caracterização do
problema/necessidade; caracterização da política; breve revisão da literatura
sobre a política ou similares; desenho da política (com teoria da mudança) e sua
avaliação; proposta de avaliação de impacto com desenho da amostra, fonte de
dados e cálculo do poder estatístico; conclusão; referências.

**Escopo (revisto em 27/09/2026, a pedido do autor):** avalia-se a política **como ela está**, com a moldura
de bens públicos (poder de mercado de grandes contribuintes, escolha ponderada pelo imposto de quem escolhe,
centralização, apropriação por taxa de serviço, exclusão de pequenos e verificação da entrega) — de forma
**tácita**. Mecanismos alternativos (financiamento quadrático, Hypercerts, Open Source Observer, Hitzig) inspiram
a análise, mas **não são nomeados nem propostos no artigo**; ficam em `notas/`. Redesenho do mecanismo segue fora
do texto. Ver `notas/desenho/06-poder-de-mercado-e-bens-publicos.md`. **Exceção (27/09/2026, tarde, comentários do
autor no PDF):** Buterin, Hitzig e Weyl (2019) entram como literatura (bens públicos e formação de comunidades; o
público não passa pelo mecanismo da LICC), conferidos na Crossref, sem nomear o mecanismo nem propô-lo à LICC. **Decisão de 28/09/2026 (revisão r5):** a ideia de que o valor deveria crescer com quantos apoiam entra
como medida da **ausência do sinal** (71% dos projetos com termo em 2022-2025 têm um só patrocinador, `analise/20_*`),
sem simular regra alternativa; a §5 do artigo organiza-se pela pergunta central (o financiamento centralizado nas
empresas desfavorece projetos pequenos e bens de valor público?), com desenho retrospectivo e estimador nomeado por
hipótese e desenho experimental ou prospectivo de confirmação; o artigo não reporta estimativas de efeito. **Decisão de 28/09/2026 (r6, parecer externo e sessão do autor):** a §5 passa a ter **uma** pergunta, "a renúncia vai para os projetos que dependem dela?", na decomposição do viés de seleção de Foguel (2017, cap. 2): *V* = E₁₀ − E₀₀ é o objeto, medido com os grupos que a regra já produz (recusados por esgotamento da cota, expirados, inabilitados; `analise/23_secao5_poder.py`). Saem o experimento conjunto, a nota cega, os sorteios e o instrumento; H1 fica "indeterminada" no Quadro 2; H3 é auditoria normativa; nenhum piloto ou regra futura no texto. Ver `artigo/auditoria/revisao-stage3-r6/`.

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
| `artigo/` | Mini artigo: `rascunho-artigo.md` é a fonte única do texto; `gerar_docx.py` gera o Word e `gerar_tex.py` gera `latex/artigo.tex` (XeLaTeX; `--pdf` compila e confere as 15 páginas); `links.py` liga caminhos de dados ao GitHub (ramo `main`) e DOIs a doi.org; a declaração de IA é separada (`declaracao-uso-ia.md`); `auditoria/` confere dados e referências no .md |

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
  autoria humana; o autor revisa e responde pelo texto; declaração de uso
  de IA vai anexa.

## Rede

Nesta máquina a rede funciona (secult.es.gov.br, mapa.cultura.es.gov.br,
servicodados.ibge.gov.br, api.openalex.org, transparencia.es.gov.br respondem).
`www3.al.es.gov.br` não respondeu.

Na sessão em nuvem a rede fica restrita ao GitHub e aos registros de pacotes. Para buscar fontes, edite
`dados/fontes_web/dois.txt` (DOIs), `buscas.tsv` (busca bibliográfica), `pedidos.tsv` (páginas e PDFs) ou
`salic_anos.txt`, ou `seguir.tsv` (índice + links que casam com uma regex, p. ex. extratos das atas da CAP), `videos.tsv` (legendas do YouTube via yt-dlp) e `canais.tsv` (lista de vídeos de um canal) e faça push: o workflow `.github/workflows/buscar-fontes.yml` coleta num runner com rede
aberta e devolve o resultado por commit em `dados/fontes_web/` (ver `analise/rede/buscar_fontes.py`; HTML, PDF e .docx viram texto). Leia fontes online com WebFetch/firecrawl. **Firecrawl (Fase A, 28/09/2026):** na sessão em nuvem é ferramenta MCP, sem chave no ambiente, e não é chamável dos scripts; cada coleta vai para `dados/fontes_web/firecrawl/<id>.md` (cabeçalho com id, url, ferramenta, consulta, coletado_utc, nota) e entra no manifesto com `python analise/rede/registrar_firecrawl.py` (`--conferir` confere o sha256). Use-o para descoberta e HTML (inclusive sites com 403 no relé) e mande PDFs grandes ao relé (o Firecrawl estoura 60 s). `www3.al.es.gov.br` falha também pelo Firecrawl;
APIs JSON (IBGE, OpenAlex, Crossref) podem ser consultadas e as tabelas
derivadas salvas em `dados/`.
