# Parecer do Journal-Fit Reviewer (EIC)

## Informações
- **Título:** Quem escolhe o que o Estado financia? Avaliação do desenho da Lei de Incentivo à Cultura Capixaba e proposta de avaliação de impacto
- **Rodada:** 2 · **Data:** 24/09/2026
- **Papel:** Journal-Fit Reviewer · **Identidade:** editor de revista aplicada de políticas públicas que confere também o enunciado da disciplina
- **Foco:** aderência às seções e ao gênero, clareza, prontidão para entrega

## Avaliação geral
**Recomendação:** Minor Revision · **Confiança:** 4 (as exigências formais podem ser conferidas no próprio enunciado)

**Resumo.** O artigo cumpre todas as seções exigidas e organiza a avaliação de desenho no formato ensinado na
disciplina, com os cinco passos do J-PAL, a cadeia de resultados, o funil de atrito e o mapeamento de premissas. É mais
coeso que a versão da rodada 1. A pergunta do título ("quem escolhe") orienta a teoria da mudança, a auditoria e a
proposta. A contribuição é real: não há avaliação publicada da LICC, e a do IJSN é preliminar e não pôde ser lida.

Do ponto de vista da entrega, os problemas são de acabamento:
- autoria e declaração de IA provisórias;
- uma referência ainda marcada `[VERIFICAR]`;
- três passagens ambíguas;
- uma frase de enquadramento que não combina com a própria definição das hipóteses.

Nada disso exige refazer argumento.

## Pontos fortes

### S1: Todas as seções exigidas, na ordem pedida
**Evidence Anchor:** `text: §1 "O artigo tem dois objetivos, definidos pela disciplina"`

Estão presentes, na ordem do enunciado:
- introdução com o problema reconstruído;
- caracterização (Quadro 1);
- revisão;
- teoria da mudança (Figura 1) e sua avaliação (Tabela 1, Quadro 2);
- proposta com perguntas (Quadro 3), estratégias, amostra e fontes (Quadro 4) e poder (Tabela 2);
- conclusão, referências e declaração.

### S2: A teoria da mudança segue o formato da disciplina e acrescenta o que o caso exige
**Evidence Anchor:** `figure: Figura 1 — árvore do J-PAL com "quem decide" em cada caixa e as premissas H1a-H3 sobre as setas`

O formato é a árvore do slide do J-PAL. As premissas marcadas nas setas (Mayne, 2015) e a separação em três cadeias
(White e Raitzer, 2017) tornam visível o traço central da política: o produto depende de um terceiro ator.

### S3: Proveniência verificável
**Evidence Anchor:** `text: nota de rodapé 2 "Dados, scripts e tabelas estão em <https://github.com/fcarva/aval-pol>"`

Cada tabela indica o arquivo de origem, e o leitor pode refazer os números.

## Fraquezas

### W1: Autoria e declaração de uso de IA provisórias
**Problem:** O bloco de autoria diz "[Autor(a) 1] e [Autor(a) 2]". A declaração começa com "[Adequar ao modelo anexo às
instruções da disciplina.]" A disciplina exige a declaração conforme modelo anexo (Portaria CNPq 2.664/2026).
**Evidence Anchor:** `text: Declaração "[Adequar ao modelo anexo às instruções da disciplina.]"`
**Why it matters:** o trabalho não pode ser entregue assim; é item formal do enunciado.
**Suggestion:** preencher a autoria e transcrever o modelo da disciplina, descrevendo o uso real da ferramenta:
- dados;
- scripts;
- figuras;
- busca e conferência de referências;
- rascunhos;
- revisão simulada.

Deve ficar dito também o que os autores decidiram e conferiram.
**Severity:** Minor · **Confidence:** 5 — texto do manuscrito

### W2: Uma referência ainda não verificada
**Problem:** SECULT (2026d), a página do evento "Cultura em Dados", sustenta a afirmação de que a avaliação do IJSN teve
resultados preliminares em julho de 2026. A referência leva "[VERIFICAR: página lida só pelo resumo do buscador.]".
**Evidence Anchor:** `text: Referências "SECULT … 2026d … [VERIFICAR: página lida só pelo resumo do buscador.]"`
**Why it matters:** a regra do projeto é que referência não verificada não entra. Uma marca de pendência no texto
entregue é visível para o avaliador.
**Suggestion:** pedir a página de novo pelo relé ou abri-la no navegador e ler o conteúdo. Se não for possível,
reformular a frase da introdução sem data nem conteúdo (por exemplo: "a SECULT anunciou uma avaliação conduzida pelo
IJSN, ainda não publicada") e manter a referência só com URL e data de acesso, sem a marca.
**Severity:** Minor · **Confidence:** 5 — texto e `checagem_referencias.csv`

### W3: A frase que organiza as hipóteses contradiz a definição de H1b
**Problem:** O fim da §4.1 diz: "H2 descreve o que se perde ao longo do funil; H1 e H3 são explicações concorrentes para
a perda." Mas H1b é a adicionalidade, isto é, o efeito do financiamento sobre a entrega, e não uma explicação para quem
se perde no funil. A frase vale para H1a e H3, não para H1.
**Evidence Anchor:** `text: §4.1 "H1 e H3 são explicações concorrentes para a perda"`
**Why it matters:** o leitor passa as seções 4 e 5 tentando encaixar as cinco siglas. É a única frase que explica a
lógica da numeração, e ela está errada para uma das três perguntas da seção 5.
**Suggestion:** reescrever. Por exemplo: "H2a e H2b descrevem como o desenho seleciona; H1a e H3 são explicações
concorrentes para quem fica de fora; H1b pergunta se o que é financiado é adicional."
**Severity:** Minor · **Confidence:** 4 — leitura do texto e da Figura 1

### W4: Três passagens ambíguas
**Problem:**
- (a) "em 2025, 63 projetos captaram exatamente R\$ 25.000.000,00" pode ser lido como valor por projeto; é o total.
- (b) "A RMGV tem 49% da população e fica com 67% do valor atribuível a um município" não diz o período. O número é o
  agregado de 2022-2026 (`03_territorio_rmgv_interior.csv`), mas o parágrafo anterior fala do ciclo 2025.
- (c) "463 projetos foram habilitados" nos cinco ciclos não bate com a soma dos ciclos da Tabela 1 e da nota (69 + 113 +
  123 + 74 + 88 = 467). A diferença são quatro processos listados em dois ciclos, e o texto não explica.

**Evidence Anchor:** `text: §1 "63 projetos captaram exatamente R\$ 25.000.000,00"`; `text: §4.2 "fica com 67% do valor atribuível a um município"`
**Why it matters:** são números do texto que o avaliador pode tentar refazer.
**Suggestion:**
- (a) "63 projetos captaram, juntos, exatamente…";
- (b) acrescentar "em 2022-2026";
- (c) "463 processos (467 registros por ciclo: quatro processos aparecem em dois ciclos)", na nota de rodapé.
**Severity:** Minor · **Confidence:** 5 — tabelas de `analise/tabelas/` e `notas/dados/01-resultados-descritivos.md`

### W5: Folga de páginas
**Problem:** A versão Word ocupa as 15 páginas inteiras. Na versão LaTeX sobra cerca de um quarto da página 15.
**Evidence Anchor:** `table: artigo/latex/artigo.pdf — 15 páginas; artigo/rascunho-artigo.pdf — p. 15 cheia`
**Why it matters:** a autoria e a declaração definitiva vão ocupar mais linhas, e qualquer acréscimo pedido pelos outros
pareceres precisa de compensação.
**Suggestion:** definir a versão de entrega (Word ou PDF do LaTeX) antes das correções, e compensar cada acréscimo com
um corte equivalente.
**Severity:** Minor · **Confidence:** 5 — contagem de páginas das duas versões

## Perguntas aos autores
1. A entrega será em PDF gerado pelo LaTeX ou em Word? Isso define a folga disponível.
2. O modelo de declaração de IA da disciplina pede itens específicos (ferramenta, versão, finalidade, trechos)?
