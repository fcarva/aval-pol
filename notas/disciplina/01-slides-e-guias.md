# 01 — Slides e guias curtos da disciplina (PECO 5046-6046)

Síntese fiel dos slides e dos guias curtos de **Avaliação de Políticas Públicas**
(PPGEco/UFES, 2026/2, profs. Ana Carolina Giuberti e Renato Nunes de Lima Seixas),
elaborada em 23/09/2026 para servir de espinha metodológica do mini artigo sobre a LICC.

## 0. Convenções, fontes e avisos

**Arquivos lidos na íntegra** (texto em `disciplina/txt/`, PDFs na raiz do projeto;
PDFs abertos página a página para recuperar fórmulas, diagramas e tabelas):

| Sigla | Arquivo | Autoria / data no slide |
| --- | --- | --- |
| APR | `PECO 5046-6046 - apresentacao da disciplina_Rev (1).pdf` (11 p.) | Giuberti e Seixas, 12/08/2026 |
| TIP1 | `PECO5046-6046_importancia_e_tipos_de_avaliacao_parte1.pdf` (25 p.) | Giuberti, 12/08/2026 |
| TIP2 | `PECO5046-6046_importancia_e_tipos_de_avaliacao_parte2.pdf` (18 p.) | Giuberti, 19/08/2026 |
| TdM | `PECO5046-6046_Teoria_da_Mudanca.pdf` (25 p.) | Giuberti, 19/08/2026 |
| M03 | `Módulo 03 - Teoria da Mudança 20171003 (1).pdf` (50 p.) | Carolina Morais Araújo, gerente do J-PAL no Brasil |
| IC | `PECO5046-6046_Inferencia_causal.pdf` (19 p.) | Giuberti, 26/08/2026 |
| MRP | `PECO5046-6046_Modelo_de_resultados_potenciais.pdf` (39 p.) | Giuberti, 02/09/2026 |
| VAL | `PECO5046-6046_Validade_interna_e_externa.pdf` (32 p.) | Giuberti, "09/09/2025" na capa (o cronograma dá 09/09 de 2026/2; provável erro de digitação) |
| AMO | `PECO5046-6046_Amostragem_e_poder_estatistico.pdf` (36 p.) | Giuberti, 16/09/2026 |
| GUIA | `00_Guia_para_avaliar_politicas_publicas (1).pdf` (5 p.) | Governo do ES / IJSN (folder do SiMAPP) |
| INSTR | `C:\Users\DELL\OneDrive\Documentos\economia\economia\Instruções para o trabalho da disciplina.md` | instruções do trabalho (arquivo do usuário) |

**Material complementar consultado só em pontos específicos** (marcado como tal no texto):
WP26 = Djimeu e Houndolo (2016), *3ie Working Paper 26* (`wp26-power-calculation.pdf`),
guia da calculadora indicada nos slides; W&R = White e Raitzer (2017), *Impact Evaluation
of Development Interventions*, ADB (`impact-evaluation-development-interventions-guide (1).pdf`),
fonte das figuras 7.3–7.4 usadas em AMO; IJSN Vol. 1 (`IJSN_SiMAPP_Volume-01 (1).pdf`).

**Formato das citações:** `(SIGLA p.X [s.Y])` = página X do PDF, slide com número
impresso Y. A numeração impressa nos slides tem saltos e repetições (divisórias de seção
não numeradas, slides duplicados com o mesmo número, slides reaproveitados de outra aula
com numeração própria), por isso sempre dou as duas. Quando página e slide coincidem,
escrevo só `[s.Y]`. Em M03, TIP2 e APR a página do PDF é igual ao número do slide.

**Avisos de extração.** O `pdftotext` perdeu todas as fórmulas de MRP e AMO, os diagramas
de TdM/M03/IC/VAL e embaralhou tabelas (p. ex. a tabela SMART de TdM e a do cronograma de
artigos de APR). Tudo abaixo foi conferido na imagem da página. Onde interpreto um
diagrama sem texto explicativo, digo "leitura minha".

---

## 1. Roteiro do curso, cronograma, avaliação e o que se espera do trabalho

### 1.1 Conteúdo (APR [s.3–5])

1. **O uso de evidências na política pública:** 1.1 por que é importante avaliar;
   1.2 diferentes tipos de avaliação; 1.3 teoria da mudança.
2. **Desenho de avaliação:** 2.1 inferência causal e construção do contrafactual;
   2.2 modelo de resultados potenciais; 2.3 validade interna e externa; 2.4 poder
   estatístico; 2.5 agregação de evidências.
3. **Métodos econométricos de avaliação de impacto:** 3.1 seleção aleatória;
   3.2 pareamento; 3.3 diferenças em diferenças; 3.4 variáveis instrumentais;
   3.5 regressão descontínua; 3.6 controle sintético.

**Metodologia** (APR [s.6]): "metodologia mista" — aulas expositivas combinadas com aulas
práticas em sala e em laboratório de informática; objetivo de "romper com o ensino
transmissivo, colocando o aluno como protagonista".

### 1.2 Avaliação e aprovação (APR [s.7–8])

- **Nota final = 0,2·N1 + 0,2·N2 + 0,3·N3 + 0,3·N4**, cada nota de 0 a 10.
  - N1 — Controles de leitura: média aritmética simples dos controles do semestre.
  - N2 — Debate de artigo: apresentação e debate sobre artigo publicado.
  - **N3 — Trabalho: "um trabalho desenvolvido e apresentado na primeira parte do curso"** (peso 0,3).
  - N4 — Lista de exercícios aplicada na segunda parte do curso.
- Aprovação: média ≥ 6,0 **e** frequência ≥ 75% (no máximo 4 faltas).

### 1.3 Cronograma das aulas 2026/2 (APR [s.9])

| Aula | Data | Conteúdo |
| --- | --- | --- |
| 1 | 12/08 | Apresentação do curso; uso de evidências: por que avaliar e tipos de avaliação |
| 2 | 19/08 | Por que avaliar e tipos de avaliação; teoria da mudança |
| 3 | 26/08 | Teoria da mudança; avaliação de impacto: inferência causal e construção do contrafactual |
| 4 | 02/09 | Modelo de Resultados Potenciais |
| 5 | 09/09 | Validade interna e externa |
| 6 | 16/09 | Poder estatístico |
| 7 | 23/09 | Agregação de evidências |
| 8 | **30/09** | **Apresentação dos trabalhos** |
| 9 | 07/10 | Seleção aleatória |
| 10 | 14/10 | Pareamento |
| 11 | 21/10 | Diferenças em Diferenças |
| 12 | 04/11 | Diferenças em Diferenças |
| 13 | 11/11 | Variáveis Instrumentais |
| 14 | 18/11 | Regressão descontínua |
| 15 | 25/11 | Controle sintético |

**Cronograma dos artigos para debate (N2)** (APR [s.10], conferido na imagem):

| Tópico | Artigo | Link | Data | Alunos |
| --- | --- | --- | --- | --- |
| Seleção aleatória | Bruhn, Garber, Koyama e Zia (2022), "The Long-Term Impact of High School Financial Education: Evidence from Brazil", BCB WP 563 | https://www.bcb.gov.br/pec/wps/ingl/wps563.pdf | 14/10 | 2 |
| Pareamento | Maia, Eusébio e Silveira (2020), "Can Credit Help Small Family Farming? Evidence from Brazil", *Agricultural Finance Review* 80(2) | https://doi.org/10.1108/AFR-10-2018-0087 | 21/10 | 3 |
| Diferenças em diferenças | Bucher e Seixas (2026), "Do payments for environmental services impact forest cover? An evaluation of the Reflorestar program", *Ecological Economics* 242 | https://doi.org/10.1016/j.ecolecon.2025.108884 | 04/11 | 2 |
| Variáveis instrumentais | Piza, Zwager, Ruzzante, Dantas e Loureiro (2024), *Journal of Public Economics* 234 | https://doi.org/10.1016/j.jpubeco.2024.105123 | 11/11 | 2 |
| Regressão descontínua | Carvalho Filho e Litschig (2022), "Long-run impacts of intergovernmental transfers", *Journal of Human Resources* 57(3) | https://doi.org/10.3368/jhr.57.3.0917-9064R2 | 18/11 | 3 |
| Controle sintético | Sills et al. (2015), "Estimating the impacts of local policy innovation: The synthetic control method applied to tropical deforestation", *PLOS ONE* 10(7) | https://doi.org/10.1371/journal.pone.0132590 | 25/11 | 2 |

(Referências transcritas do slide; DOIs não conferidos nesta nota — [VERIFICAR] antes de citar.)

### 1.4 O trabalho (INSTR; resumo também no `CLAUDE.md` do projeto)

- **Tema registrado:** "Avaliação do financiamento de bens públicos culturais a partir da
  Lei de Incentivo à Cultura Capixaba (LICC)".
- **Objetivo:** "Elaborar um mini artigo avaliando o desenho da política pública
  selecionada, bem como estruturando uma avaliação de impacto da política."
- **Instruções gerais:** (1) dupla; estrutura de mini artigo; política pública
  brasileira, "preferencialmente municipal, previamente aprovada pela professora";
  (2) seções obrigatórias: introdução com caracterização do problema/necessidade;
  caracterização da política; breve revisão da literatura sobre a política ou políticas
  similares; desenho da política (com teoria da mudança) e sua avaliação; proposta de
  avaliação de impacto contendo desenho da amostra e fonte de dados, cálculo do poder
  estatístico; conclusão e referências; (3) Times New Roman 12, espaçamento simples,
  **10 a 15 páginas incluindo tabelas, gráficos e referências**; (4) entrega no Google
  Sala de Aula, Word ou PDF; (5) uso de IA conforme a Portaria CNPq 2.664/2026 — conteúdo
  de IA não pode ser submetido como autoria humana, autores integralmente responsáveis,
  declaração "conforme modelo em anexo".
- **Cronograma do trabalho:** 17/08 definição das duplas e da política; 26/08 aula prática
  de construção da teoria da mudança (cada dupla com a sua política); **28/09 entrega**.
  Pelo APR, a aula de **30/09 é de apresentação dos trabalhos**.
- **Pontos em aberto:** o "modelo em anexo" da declaração de IA não está no arquivo INSTR
  nem no repositório [VERIFICAR no Google Sala de Aula]. A LICC é estadual e a instrução
  prefere política municipal; o tema consta como "Selecionado", mas a aprovação formal
  não está documentada aqui [VERIFICAR].

**O que se espera, na lógica dos slides:** o trabalho é essencialmente uma **avaliação de
desenho** (TIP1 p.20 [s.19]) mais um **plano de avaliação de impacto** do tipo que o curso
chama de avaliação ex ante / plano de avaliação (TIP1 p.15 [s.14]): pergunta, método
(contrafactual), população e listagem, indicadores de resultado derivados da teoria da
mudança, EMD justificado como "questão de política pública", α, poder, P, ICC e tamanho de
amostra (AMO p.18–21 [s.19–23]). Não se pede estimar impacto.

---

## 2. Resumo por tema

### 2.1 Por que avaliar; monitoramento × avaliação (TIP1 [s.3–5]; GUIA p.2–4)

- **Avaliar** é "a análise sistemática do desenho, da implementação e dos resultados de uma
  intervenção ou política pública". Compreende: como a intervenção está sendo (ou foi)
  realizada; quem são os beneficiários; o porquê da realização; quais os efeitos (TIP1 [s.3]).
- **Por que avaliar:** base para políticas baseadas em evidências, "cujo foco está nos
  resultados da política — e não nos insumos"; dois fins: **aprendizado** (informação para
  decisão) e **accountability** (prestação de contas e responsabilização do agente público)
  (TIP1 [s.4]).
- **Monitoramento:** processo contínuo de acompanhamento sob o prisma da implementação;
  subsidia decisões do dia a dia. **Avaliação:** análises periódicas para responder a
  questões específicas sobre desenho, implementação e resultados (TIP1 [s.5]).
- **GUIA (SiMAPP/ES):** a avaliação busca entender como a política foi implementada, que
  efeitos teve, para quem foi planejada, quem se beneficiou e por que obteve os resultados
  (p.2). Benefícios: conhecer resultados, escolher como e onde investir melhor, elevar a
  qualidade do serviço público, fortalecer a prestação de contas e a transparência (p.2).
  Lei estadual nº 10.744, de 05/10/2017, cria o SiMAPP, vinculado ao ciclo de planejamento
  e orçamento (p.3). A cada ano o Governador, por decreto, estabelece um plano estadual de
  avaliação; resultados subsidiam o orçamento; o NuMA (Núcleo de Monitoramento e Avaliação)
  coordena as avaliações (p.4). Perguntas-guia: "a intervenção está sendo bem implementada?
  Quem está sendo beneficiado? Os impactos esperados foram alcançados? O custo é razoável
  em relação aos benefícios?" (p.4). Guia em 4 volumes (p.5): Vol. 1 "A política é nova?
  Avaliação ex ante!"; Vol. 2 "Como monitorar uma política pública?"; Vol. 3 "Avaliação ao
  alcance de todos: análise executiva"; Vol. 4 "E quando a política está em andamento?
  Avaliação ex post!". (A apresentação do Vol. 1, PDF p.9, troca a ordem dos Vols. 2 e 3;
  as capas dos volumes no repositório confirmam Vol. 2 = monitoramento.)

### 2.2 Tipos de avaliação

**Por questão a responder** (TIP1 [s.7]):
- *Perguntas descritivas* — o que está ocorrendo; processos, condições, relações
  organizacionais e pontos de vista das partes interessadas.
- *Perguntas normativas* — comparam o que está ocorrendo ao que deveria ocorrer; se as
  metas estão sendo alcançadas; aplicam-se a insumos, atividades e produtos.
- *Perguntas de causa e efeito* — concentram-se na **atribuição**: a diferença que a
  intervenção exerce nos resultados.

**Pela etapa da política** (TIP1 [s.8]): **ex-ante** (fase de elaboração); **ex-post**
(políticas em andamento ou finalizadas); **análise/avaliação executiva** (modalidade de
ex-post). Classificação usada: SIMAPP (Lei Estadual 10.744/2017, IJSN) e CMAP (Decreto
9.834/2019, IPEA).

**Avaliação ex-ante** (TIP1 [s.10–15]): "busca identificar se as ações previstas condizem
com o enfrentamento do problema diagnosticado e se são consistentes". Cinco etapas:
1. *Diagnóstico do problema* [s.11]: identificar o problema; caracterizar com dados
   quantitativos, comparando com outras regiões; identificar causas potenciais; considerar
   lições de experiências externas e/ou anteriores.
2. *Desenho da política — Teoria do Programa e Modelo Lógico* [s.12]: Problema/Necessidade →
   Insumos/Atividades → Produtos → Resultados Intermediários → Resultado Final. "Cada seta
   pressupõe uma hipótese causal necessária para o resultado acontecer." A segunda versão
   do slide (p.13 [s.12]) traz a árvore do J-PAL (ver 2.3).
3. *Projeto de implementação* [s.13 = p.14]: etapas (sequência de fases), atividades (o que
   será realizado em cada fase), recursos e fontes (meios e origem do financiamento),
   cronograma e governança (prazos e responsabilidades).
4. *Planos de monitoramento e avaliação* [s.14 = p.15], adaptados de World Bank Institute
   (2009):
   - Plano de Monitoramento — colunas: Indicador | Fase do marco lógico (insumos ·
     atividades · produtos · resultados · impactos) | Linha de base | Frequência da coleta |
     Metas (anos 1 a 3) | Órgão responsável.
   - **Plano de Avaliação — colunas: Pergunta a ser respondida | Sub-perguntas |
     Metodologia | Principais indicadores | Fonte de dados | Órgão responsável.**
5. *Análise de custos e impactos orçamentários* [s.15 = p.16] (só o título no slide).

**Análise executiva** (TIP1 p.18 [s.17]): "avaliação geral do desempenho da política para
fazer recomendações quanto à sua continuidade ou à necessidade de avaliações adicionais".
Etapas: caracterização da política; diagnóstico do problema; desenho da política;
processo; percepção dos beneficiários; resultados da política; matriz SWOT; recomendações.
O GUIA (p.4) a chama de "espécie de raio-x da intervenção", que pode ser feita pela
própria equipe responsável.

**Avaliações ex-post** (TIP1 p.19 [s.18]): avaliação do desempenho, a partir de determinados
aspectos, para recomendações diante dos gargalos. Tipos: *qualitativas* — avaliação de
desenho, avaliação de processos; *quantitativas* — avaliação de impacto, avaliação de
custo-benefício e custo-efetividade.

- **Avaliação de desenho** (TIP1 p.20 [s.19]): "analisa a racionalidade do programa: a lógica
  que conecta problema, ações e resultados esperados". Dois instrumentos: **Teoria do
  Programa** (explicita as hipóteses causais que sustentam a intervenção) e **Modelo
  Lógico** (organiza insumos, atividades, produtos e resultados em uma cadeia).
- **Avaliação de processos** (TIP1 p.21 [s.20]): analisa a implementação e o funcionamento
  para identificar fatores que afetam a efetividade; base: modelo lógico e documentos,
  entrevistas com atores-chave, grupos focais de beneficiários.
- **Avaliação de impacto** (TIP1 p.22 [s.21]): identificar a relação causal entre a
  política e os resultados — "o que teria acontecido na ausência da intervenção?".
- **Custo-benefício** (TIP1 p.23 [s.22]): "qual é o benefício gerado pelo programa para um
  dado custo?". **BL = Benefício Total − Custo Total** (em reais), recomendável se BL > 0;
  **RCB = Custo Total / Benefício Total** (em reais), recomendável se RCB < 1.
- **Custo-efetividade** (TIP1 p.24 [s.23]): "como as várias alternativas de implementação
  do programa se comparam em termos de custo-efetividade?". **RCE = Custo Total /
  Impacto** — investimento necessário por unidade de impacto não monetário; "quanto maior
  o RCE, menos eficiente é a intervenção".

**Revisão J-PAL** (M03 [s.2]): sequência Avaliação de Necessidades → **Avaliação Teórica**
(destacada; é onde se insere a teoria da mudança) → Avaliação de Processos → Avaliação de
Impacto → Avaliação de Eficiência.

**Avaliação de impacto para decisão** (TIP2):
- Impacto = relação causal entre a política e o resultado; todos os métodos tratam de causa
  e efeito [s.3]. **Contrafactual:** "qual teria sido o resultado para os beneficiários da
  política, caso eles não tivessem participado dela?"; a questão-chave é construí-lo — o
  grupo de controle ou de comparação [s.4].
- Escolha do método depende de (01) características operacionais do programa e (02) do
  momento da avaliação em relação ao programa [s.5].
- **Prospectiva** (desenvolvida junto com o programa, com coleta de dados anterior ao
  início) × **retrospectiva** (após a implementação, grupos formados a posteriori);
  prospectivas "tendem a produzir resultados mais robustos e confiáveis" [s.6].
- Metodologia [s.7]: método experimental (seleção aleatória, "padrão ouro"); não
  experimentais: pareamento (seleção a partir de observáveis); diferenças em diferenças e
  variável instrumental (seleção a partir de observáveis e não observáveis); regressão
  descontínua (seleção baseada em índice contínuo de classificação); controle sintético
  (contrafactual construído a partir de vários casos).
- **Ética** [s.8]: "O acesso à política pública não deve ser negado ou adiado em função da
  avaliação."
- Modelo básico: a intervenção é eficaz comparada à sua não existência? A
  comparabilidade entre tratamento e comparação é fundamental para a validade interna
  [s.10]. Também se testam inovações de desenho (aumentar efetividade ou reduzir custos)
  [s.11] e alternativas de implementação, com vistas à maior custo-efetividade [s.12].
  *Tratamentos alternativos*: um grupo por opção + um grupo de comparação puro; só é
  possível se o desenho previr os grupos desde o início [s.13]. *Subgrupos*: precisam ser
  incorporados ao desenho e exigem amostras suficientemente grandes [s.14].
- **Quando avaliar** [s.16–17]: perguntas prévias — o que está em jogo? há evidência de que
  funciona? qual a magnitude do impacto? há evidências de programas semelhantes em
  circunstâncias parecidas? Justifica-se se a política for **inovadora, replicável,
  estrategicamente relevante, não testada, influente**; pergunta final: "dispomos dos
  recursos necessários para fazer uma avaliação de impacto de qualidade?".

**IJSN Vol. 1, apresentação (PDF p.9)** — perguntas que uma avaliação ex post deve responder:
(i) o desenho da política é consistente com seus objetivos e adequado à solução dos
problemas-alvo? (ii) as atividades executadas são consistentes com o desenho? (iii) o
programa tem impactos causais sobre as dimensões esperadas, de que magnitude, e impactos
não esperados? (iv) qual o custo para alcançar o resultado e os benefícios compensam?

### 2.3 Teoria da mudança

**Definição e conteúdo.**
- "Uma teoria da mudança descreve a lógica causal entre uma intervenção e os resultados
  pretendidos." Falamos em **uma** teoria da mudança: "ela não é única"; é "a base para a
  avaliação de impacto" (TdM [s.3]).
- Retrata uma sequência de eventos que leva aos resultados. Contém: condições e
  pressupostos necessários para que a mudança ocorra; a lógica causal do programa; as
  intervenções realizadas. "Permite identificar os indicadores e as variáveis a serem
  coletadas para a avaliação de impacto" (TdM [s.4]).
- Formas de descrevê-la: cadeia de resultados; modelos teóricos; marcos lógicos;
  estruturas lógicas; modelos de resultados — "todas contêm a(s) cadeia(s) causal(is), as
  influências e condições externas e as principais hipóteses" (TdM [s.5]).
- J-PAL: "descrição ampla e ilustrada de como se espera que aconteça uma mudança num
  contexto particular"; meio de saber "até onde vamos (resultados) e como chegamos
  (processos)"; detalha todas as mudanças implícitas entre atividades e objetivos de longo
  prazo (M03 [s.5]). Objetivos: comunicação e descrição da intervenção; desenho de
  intervenção e planejamento estratégico; monitoramento e avaliação (M03 [s.6]). Pode ter
  formas diversas: exemplos Oxfam America/Freedom From Hunger, AmplifyChange, infográfico
  artofagency.com (M03 [s.7–9]).

**Cadeia de resultados — composição e elementos** (TdM [s.7–9], fonte Gertler et al., fig. 2.1):

| Elemento | Definição no slide | Bloco |
| --- | --- | --- |
| INSUMOS | Recursos financeiros, humanos e outros mobilizados para apoiar as atividades | Implementação · lado da oferta |
| ATIVIDADES | Ações e trabalho desenvolvidos para converter insumos em produtos | Implementação · lado da oferta |
| PRODUTOS | Bens e serviços produzidos, sob controle da agência de implementação | Implementação · lado da oferta |
| RESULTADOS | Uso dos produtos pelo público-alvo; não está sob controle da agência | Resultados · demanda + oferta |
| RESULTADOS FINAIS | Objetivos finais e metas de longo prazo, afetados por múltiplos fatores | Resultados · demanda + oferta |

- *Implementação* = "o trabalho realizado pela gestão: insumos, atividades e produtos",
  sob responsabilidade direta do projeto. *Resultados* = intermediários e finais, "não
  estão sob controle direto do projeto: dependem de mudanças de comportamento dos
  beneficiários" (TdM [s.7]).
- Para que serve: expor hipóteses e riscos implícitos; facilitar monitoramento e avaliação
  ao indicar os indicadores; **fontes de informação: os gestores e as evidências da
  literatura** (TdM [s.8]).

**Formato do diagrama (padrão J-PAL, usado pela professora)** (TdM [s.11]; TIP1 p.13
[s.12]; M03 [s.11]) — árvore vertical, de cima para baixo:

```
                 Problema / Necessidade
                           |
                   Insumo / Atividade
                    /              \
               Produto            Produto
              /      \           /       \
  Resultado interm.  Resultado interm.  Resultado interm.
          \         /          \         /
        Resultado final      Resultado final
```

Cores do slide: vermelho (problema), laranja (insumo/atividade), amarelo (produto), verde
(resultados intermediários), azul (resultado final). Há também a versão linear em cinco
caixas com setas (TIP1 [s.12]) e a versão em tabela de cinco colunas (TdM [s.9–10]).
M03 [s.31] separa "Desenho e implementação do programa" (problema → produtos) de
"Impactos do programa" (resultados intermediários e finais).

**Os cinco passos do J-PAL** (M03 [s.14]): 1. definir o propósito; 2. completar a cadeia
causal; 3. identificar premissas e riscos; 4. resumir a hipótese causal; 5. definir
indicadores.

1. **Propósito** (M03 [s.15–16]): a mudança macro que o programa quer realizar; "a razão
   pela qual existe nosso programa"; muitas vezes semelhante à missão da organização.
   Exemplo: "Melhorar a educação básica de regiões vulneráveis".
2. **Cadeia causal** (M03 [s.17–31]):
   - *Problemas/necessidades*: "explicitam as carências que queremos enfrentar, não o
     objetivo que queremos alcançar"; especificam a população-alvo; relacionam-se
     diretamente aos resultados finais [s.18]. Ex.: "Baixo desempenho escolar" [s.19].
   - *Resultados finais*: mudanças de longo prazo; avanço no estado de desenvolvimento da
     população-alvo; diretamente relacionados às necessidades [s.20]. Ex.: "Melhor
     desempenho escolar" [s.21].
   - Construção **"do final ao início"** [s.22] — útil no desenho porque obriga a focar nos
     resultados e "comprovar a credibilidade das nossas premissas" e a identificar a melhor
     estratégia [s.23]; depois conferência **"do início ao fim"** [s.24].
   - *Resultados intermediários*: mudanças devidas à intervenção e necessárias para o
     resultado final; mudanças em atitudes, conhecimentos, capacidades, comportamentos;
     "um dos principais focos das avaliações de impacto" [s.25].
   - *Produtos*: resultados diretos das atividades; muitas vezes "uma reformulação das
     atividades do ponto de vista dos beneficiários" [s.27].
   - *Insumos/atividades*: recursos e ações importantes para chegar aos produtos, "do ponto
     de vista de quem o implementa" [s.29].
3. **Premissas e riscos** (M03 [s.33]): *premissas* = "condições externas necessárias que
   devem ser cumpridas para que a cadeia causal estabelecida na Teoria da Mudança seja
   válida"; *riscos* = "efeitos negativos não esperados gerados pelo programa"; numa
   avaliação de impacto, "premissas e riscos podem ser perguntas de pesquisa". No
   diagrama, a premissa aparece como faixa entre produtos e resultados ("as escolas contam
   com acesso à rede elétrica") e o risco como faixa entre uso e resultados ("os alunos
   usam mais os laptops para escutar música e jogar...") (M03 [s.34]).
4. **Hipótese causal** — gabarito literal (M03 [s.35]): "Se [atividades] geram [produtos],
   isto deveria levar a [resultados intermediários] que ao final melhorarão [resultados
   finais], contribuindo para [propósito]". O mesmo formato aparece no exemplo Pé-de-meia
   citado de Santana e Giuberti (2026, p. 5) (TdM p.13, slide numerado "6").
5. **Indicadores** (M03 [s.36–37]): devem permitir quantificar insumos/atividades, avaliar a
   implementação, quantificar resultados e impactos e registrar percepções de quem está no
   programa. No diagrama, cada caixa recebe um indicador (ex.: "Nº de laptops enviados para
   escolas", "Número de horas de uso dos laptops em casa", "Pontuação em provas de
   matemática e português").

**Por que a TdM importa** (M03 [s.39–50]): permite identificar perguntas de avaliação,
"geralmente relacionadas às premissas"; define que dados coletar; ajuda a entender o
"porquê" dos resultados; importante para conhecimento generalizável e replicação. Os
slides 40–47 repetem o diagrama do laptop com marcações. *Leitura minha das marcações:*
[s.41] "Não há impacto"; [s.42] a cadeia coberta por uma caixa preta — sem TdM não se sabe
por quê; [s.43] ✗ entre atividades e produtos (falha de implementação: laptops/cursos não
entregues); [s.44] ✓ até o uso dos laptops e ✗ nos elos para o desempenho (a
implementação ocorreu, mas a teoria falhou); [s.45–47] "Impacto positivo" com caminhos
diferentes (s.46: só o canal "uso em casa → mais tempo de estudo"; s.47: só o canal "uso
em aula → aulas melhores/mais presença"). Conclusões: a TdM torna explícito o caminho
para o impacto; os cinco passos; ajuda a medir não só se o programa é efetivo, mas "quais
são os mecanismos necessários para que o impacto aconteça" [s.49]; é "um mapa dinâmico",
mostra relações de causa e efeito, "não apenas descritivo, mas explicativo" [s.50].

**Marco lógico** (TdM p.16 [s.14]; M03 [s.10]): matriz com linhas **Impacto, Propósito,
Componentes, Atividades** e colunas **Objetivos, Indicadores, Fonte de verificação,
Premissas**.

**Modelo lógico — formato da Bolsa Atleta** (TdM p.17–18 [s.15–16], fonte Almeida, 2025):
colunas **Componente | Descrição | Indicadores | Premissas e riscos**.

| Componente | Descrição | Indicadores | Premissas e riscos |
| --- | --- | --- | --- |
| Insumos | Recursos orçamentários federais; equipe administrativa; sistema de inscrição | Valor total do orçamento anual; nº de servidores envolvidos | P: recursos liberados sem atraso. R: contingenciamento de verbas |
| Atividades | Elaboração e lançamento do edital; processo de seleção; acompanhamento da execução | Nº de editais publicados por ano; tempo médio de seleção | P: critérios claros e acessíveis. R: falhas na inscrição |
| Produto | Pagamento mensal da bolsa aos atletas e paratletas selecionados | Nº de bolsas concedidas por categoria e ano; valor médio mensal | P: sistema financeiro funcional. R: atrasos nos pagamentos |
| Resultados intermediários | Dedicação integral ao esporte; aumento da participação em competições | Nº de atletas bolsistas em competições nacionais e internacionais | P: a bolsa custeia os treinos. R: desistência por falta de estrutura de treino |
| Impacto final | Melhoria do desempenho do Brasil no quadro de medalhas; democratização do acesso ao esporte de rendimento | Nº de medalhas em Olimpíadas e Paralimpíadas; evolução do ranking mundial | P: políticas complementares de apoio. R: mudança de prioridades governamentais |

(Exemplo especialmente útil: é o mais próximo da LICC — edital, seleção, transferência
financeira a beneficiários selecionados.)

**Outros exemplos de cadeia usados:** reforma do currículo de matemática do ensino médio
(Gertler et al., fig. B2.3.1; TdM [s.10]: insumos = recursos, pessoal do MEC e professores,
instalações; atividades = desenho do currículo, formação, impressão e distribuição de
livros; produtos = 5.000 professores formados, 100.000 livros distribuídos; resultados =
professores usando livros e currículo, melhor desempenho nos exames; finais = taxas de
conclusão mais elevadas, maiores salários e emprego); **Proaes/UFES** (do Val, 2023; TdM
[s.12]: problema = evasão dos estudantes de baixa renda; insumos = recursos humanos,
financeiros federais, físicos; produtos = auxílios alimentação, moradia, transporte,
material de consumo, empréstimo de livros, acolhimento; intermediários = segurança
alimentar, garantia de moradia, deslocamento garantido, acesso ao material, apoio
psicológico; final = redução da evasão e retenção motivadas por fatores socioeconômicos);
**Pé-de-meia** (Santana e Giuberti, 2026; TdM p.13: pagamento do benefício → permanência na
escola e queda do absenteísmo → menos retenção, abandono e evasão; mais conclusão →
desenvolvimento humano, mobilidade social e inclusão); **Qualifica-APS** (Soares, Thomas e
Giuberti, prelo; TdM p.14: diagnóstico = taxa de médicos por 1.000 hab. abaixo do
recomendado em áreas remotas e vulneráveis, baixa qualificação e desigualdades regionais
na APS; ... final = redução de internações e mortalidade por Condições Sensíveis à
Atenção Primária); **Um Laptop por Aluno** (M03 [s.13–47]).

**Indicadores SMART** (TdM p.20 [s.18], conferido na imagem — a extração embaralhou):
- **Específicos** — medem a informação necessária com a maior acurácia possível.
- **Mensuráveis** — garantem que as informações sejam facilmente obtidas.
- **Atribuíveis** — vinculam cada medida às dimensões embutidas no programa.
- **Realistas** — permitem obter os dados em tempo hábil, com frequência e custo razoáveis.
- **Direcionados** — referem-se à população-alvo do programa.

**Túnel (funil) de atrito** (TdM p.21–24 [s.19–22]; fonte White, 2013 [VERIFICAR referência
completa]). O título da seção é "Indicadores e funil de atrito"; os slides 19–21 dizem
"túnel de atrito" e o 22 "funil de atrito".
- "Ferramenta para apresentar e conceituar as hipóteses da cadeia causal." Motivação: a
  participação e o efeito se reduzem ao longo da cadeia; o efeito final pode ser menor que
  o esperado; **"superestimar participação e efeito leva a amostras pequenas demais para
  detectar efeitos significantes"** [s.19] (ponte direta com o cálculo de poder).
- "De cada 100 beneficiários potenciais, quantos de fato se beneficiam da política?"; o
  atrito pode ser substancial porque a exposição não é universal, a mudança de
  comportamento pode não acontecer e as condições para o pleno efeito podem não estar
  presentes [s.20].
- Questões [s.21]: Os beneficiários sabem da existência do programa? O público-alvo quer
  participar? Os beneficiários têm condições de participar? A transferência de
  conhecimento é efetiva? A mudança de comportamento esperada de fato ocorre? Restrições
  à efetividade permanecem sem tratamento? A intervenção possui um efeito frequente?
- Exemplo numérico [s.22]: população-alvo 100 → sabem da intervenção 75 → participam 45 →
  adquirem conhecimento 35 → mudam atitudes 25 → mudam comportamento 20 → produtos
  realizados 15 → resultados alcançados 10. Condições de cada passagem: intervenção bem
  promovida; o público-alvo quer e pode participar; comunicação eficaz; barreiras
  culturais não são insuperáveis; incentivos suficientemente alterados; todos os insumos
  necessários presentes; teoria da mudança correta e outros insumos presentes.

**Perguntas para avaliar o desenho — compiladas do material** (não há checklist único nos
slides; cada item traz a fonte):
1. O problema/necessidade está formulado como carência (não como objetivo), com
   população-alvo especificada e ligado diretamente aos resultados finais? (M03 [s.18])
2. O diagnóstico está caracterizado com dados quantitativos, comparação com outras regiões,
   causas potenciais e lições de experiências anteriores? (TIP1 [s.11])
3. As ações previstas condizem com o enfrentamento do problema diagnosticado e são
   consistentes? (TIP1 [s.10]) O desenho é consistente com os objetivos e adequado à
   solução dos problemas-alvo? (IJSN Vol. 1, PDF p.9)
4. A lógica conecta problema, ações e resultados esperados? Quais hipóteses causais a
   sustentam (teoria do programa)? (TIP1 p.20 [s.19]) Cada seta tem hipótese causal
   explícita e crível? (TIP1 [s.12]; M03 [s.23])
5. Quais premissas (condições externas) e riscos (efeitos negativos não esperados)? Viram
   perguntas de pesquisa? (M03 [s.33]; M03 [s.39])
6. Há indicadores SMART para cada elo, com linha de base, frequência, metas e responsável?
   (TdM [s.18]; TIP1 p.15 [s.14])
7. Quanto atrito há em cada etapa (as sete questões do túnel)? (TdM [s.21])
8. Quais hipóteses contextuais sustentam cada elo e o contexto real as confirma? (VAL
   mecanismo de mapeamento, p.24–26 [s.22–24])
9. Estão claros etapas, atividades, recursos e fontes, cronograma e governança? (TIP1 p.14 [s.13])

### 2.4 Inferência causal e construção do contrafactual (IC)

- **Inferência causal** = "estabelecer a relação de causa e efeito entre duas variáveis".
  A pergunta básica da avaliação de impacto é um problema de inferência causal: qual o
  impacto de um programa (P) sobre uma variável de resultado (Y)? [s.3]
  $$\Delta = (Y \mid P = 1) - (Y \mid P = 0)$$
- **O contrafactual não é conhecido:** "(Y | P = 0) não é observado → precisa ser
  estimado"; estima-se **a nível de grupo**; a partir de propriedades estatísticas é
  possível gerar dois grupos, tratamento e comparação, estatisticamente idênticos [s.5].
- **Grupo de comparação válido** — iguais em três quesitos, ao menos [s.6]: (1) as
  características médias devem ser idênticas* (*"ou, pelo menos, apresentar a mesma
  tendência para a variável de resultado"); (2) o tratamento não pode afetar o grupo de
  comparação, direta ou indiretamente; (3) os dois grupos devem reagir da mesma forma
  diante do programa.
- **Contrafactual válido** [s.7]: a única diferença é o tratamento; a condição *ceteris
  paribus* é atendida; é possível identificar o impacto. "Grupos de comparação inválidos
  geram estimativas viesadas: o efeito estimado será o do programa somado ao de outros
  fatores."
- **Estimativas falsas do contrafactual:**
  1. *Comparação antes e depois (pré-pós ou reflexiva)* [s.8]: equivale a supor que, sem o
     programa, o resultado teria o mesmo valor ao longo do tempo; não é crível para a
     maioria dos programas; não isola o efeito dos demais fatores. Exemplo do
     microcrédito (Gertler et al., fig. 3.3; [s.9]): produção de arroz vai de 1.000 (ano 0)
     a 1.100 kg/ha (ano 1), Δ = 100 observado (A); contrafactuais possíveis B (constante em
     1.000), C (sobe) e D (cai).
  2. *Comparação entre inscritos e não inscritos (autosseleção)* [s.10]: grupos não são
     estatisticamente idênticos quanto às características não observáveis; estimativas
     viesadas — **viés de seleção**.
- **Viés de seleção** [s.11]: "O viés de seleção ocorre quando as razões pelas quais um
  indivíduo participa de um programa estão correlacionadas com os resultados" (Gertler et
  al., p. 66). "Em um contexto de análise de regressão, o viés de seleção surge quando há
  omissão de variável relevante."
- **Exemplo 1 — Bolsa Capixaba** [s.13–16]: pesquisa possível porque a inclusão de novas
  famílias foi escalonada no tempo; três lotes de inclusão; plano amostral selecionado no
  último bloco; linha de base entre maio e julho de 2018. Beneficiários (mil famílias,
  registros do programa): abril 12; maio 12 + 5; junho 17 + 4; julho 21 + 4 (julho em
  destaque). Plano amostral [s.15]: último lote de inclusão em julho — atendidos 4 mil →
  na RMGV 2,4 mil → **tratamento 1,5 mil**; não atendidos 6,5 mil → na RMGV 3 mil →
  **controle 1,5 mil**; "ponto de corte: 25 mil famílias"; "seleção aleatória entre os
  grupos"; "amostra ponderada pela participação em programas remanescentes do MDS: cerca
  de 30%". Balanceamento na linha de base [s.16] (média, DP entre parênteses):

  | Indicador | Tratamento | Controle | Diferença | p-valor |
  | --- | --- | --- | --- | --- |
  | Insegurança alimentar | 4,462 (3,499) | 4,740 (3,695) | −0,279 | 0,184 |
  | Insegurança de renda | 12,204 (5,801) | 12,099 (6,291) | 0,104 | 0,767 |
  | Qualidade de vida: domínio psicológico | 20,487 (3,731) | 19,924 (4,046) | 0,563 | 0,013 |
  | Locus de controle | 18,331 (2,660) | 18,202 (2,728) | 0,129 | 0,414 |
  | Renda familiar per capita | 183,009 (176,692) | 180,084 (195,086) | 2,926 | 0,790 |
  | Gasto per capita com alimentos | 90,466 (53,779) | 96,683 (64,787) | −6,216 | 0,100 |
  | Gasto per capita com moradia | 265,050 (197,252) | 258,908 (209,715) | 6,142 | 0,613 |

  Notas do slide: alimentos exceto cesta básica, inclui alimentação fora do domicílio;
  moradia = aluguel, energia, água, gás e telefone. (Observação minha: só o domínio
  psicológico tem p < 0,05.)
- **Sorteio aleatório — exemplo fictício** (IC p.17, slide numerado "13"): programa de
  prevenção à retenção; vagas atribuídas aleatoriamente; base = alunos do CCJE
  matriculados em 2026/2. **Teste de médias** (IC p.18, numerado "15"): "o balanceamento
  verifica se os grupos são estatisticamente idênticos antes do tratamento" — sexo feminino
  0,520 × 0,537 (dif. −0,017; p 0,445); sexo masculino 0,481 × 0,463 (0,017; 0,445);
  idade 25,277 × 25,109 (0,168; 0,578); cotista 0,432 × 0,446 (−0,015; 0,516). (O slide
  guarda a nota residual "Preencher com os dados do exemplo escolhido (CCV 2015 ou Bolsa
  Capixaba)".)

### 2.5 Modelo de resultados potenciais (MRP) — notação exata

**Grupo de comparação** (MRP [s.3]): os mesmos três quesitos de IC [s.6].

**Notação** (MRP [s.5], com base em Itaú Social, 2017, cap. 2 — *Avaliação econômica de
projetos sociais*, 3. ed., org. Menezes Filho e Pinto, arquivo no repositório):
0 = não tratado; 1 = tratado; *i* = unidade de análise; *T* = tratamento; *Y* = variável de
resultado. $Y_i(1)$: valor da variável de resultado para a unidade *i*, caso ela seja
tratada; $Y_i(0)$: caso não seja tratada.

**Impacto individual** [s.6]: $\beta_i = Y_i(1) - Y_i(0)$; apenas uma situação é observada,
gerando o par de resultados potenciais $(Y_i(1),\,Y_i(0))$.

**Resultados potenciais** [s.7]:
$$Y_i(0) = \alpha + \varepsilon_i \qquad Y_i(1) = \alpha + \beta_i + \varepsilon_i$$
α = intercepto; $\varepsilon_i$ = componente não observável que afeta os resultados da
unidade *i*. "$\beta_i$ não pode ser estimado individualmente, mas pode ser estimado para
um grupo de unidades."

**Medidas de impacto** (atenção: o slide usa "/" para condicionamento):
- **EMP (ATE)** — efeito médio do programa [s.9]: $EMP = E[Y_i(1) - Y_i(0)] = E[\beta_i]$;
  "média do efeito do programa para todas as unidades da população, independentemente de
  quem participou ou não".
- **EMPT (ATT)** — efeito médio sobre os tratados [s.10]:
  $EMPT = E[Y_i(1) - Y_i(0) \,/\, T_i = 1] = E[\beta_i \,/\, T_i = 1]$; **"parâmetro
  particularmente útil quando a participação é voluntária"**.
- **EMPNT (ATU)** — efeito médio sobre os não tratados [s.11]:
  $EMPNT = E[Y_i(1) - Y_i(0) \,/\, T_i = 0] = E[\beta_i \,/\, T_i = 0]$; "com o EMP, passa a
  interessar quando se pretende expandir o programa".

**Exemplo numérico** [s.12–16] (MRP p.12–17):

| *i* | $T_i$ | $Y_i(0)$ | $Y_i(1)$ | $Y_i$ | $Y_i(1)-Y_i(0)$ |
| --- | --- | --- | --- | --- | --- |
| 1 | 0 | 15 | 15 | 15 | 0 |
| 2 | 1 | 12 | 16 | 16 | 4 |
| 3 | 1 | 15 | 14 | 14 | −1 |
| 4 | 0 | 15 | 17 | 15 | 2 |
| 5 | 1 | 11 | 14 | 14 | 3 |

EMP = (0 + 4 − 1 + 2 + 3)/5 = 8/5 = 1,6; EMPT = (4 − 1 + 3)/3 = 2; EMPNT = (0 + 2)/2 = 1
[s.13]. **O EMP é a média do EMPT e do EMPNT ponderada pela proporção de tratados e não
tratados:** EMP = (3/5)·EMPT + (2/5)·EMPNT = (3/5)(2) + (2/5)(1) = 1,6 [s.14].

**A questão central** [s.15]: apenas um resultado potencial é observado por unidade —
$Y_i(1) / T_i = 1$ e $Y_i(0) / T_i = 0$; "a diferença simples entre esses dois valores é um
estimador viesado do EMP". **Diferença simples (SDO)** [s.16]:
$$SDO = E[Y_i(1) / T_i = 1] - E[Y_i(0) / T_i = 0] = (16+14+14)/3 - (15+15)/2 = -1/3 = -0{,}33$$

**Decomposição do viés** (MRP p.19–26 [s.18–24], seguindo Cunningham, 2021, item 4.1
[VERIFICAR referência completa — o livro não está no repositório]):
- [s.18] $EMP = \pi\,EMPT + (1-\pi)\,EMPNT = \pi\{E[Y_i(1) - Y_i(0) / T_i = 1]\} + (1-\pi)\{E[Y_i(1) - Y_i(0) / T_i = 0]\}$ — equação (1); **π é a parcela das unidades de análise que recebem o tratamento**.
- [s.19] Denominando $a = E[Y_i(1)/T_i=1]$, $b = E[Y_i(1)/T_i=0]$, $c = E[Y_i(0)/T_i=1]$,
  $d = E[Y_i(0)/T_i=0]$, $EMP = e$.
- [s.20–21] $e = \{\pi a + (1-\pi) b\} - \{\pi c + (1-\pi) d\}$, somando e subtraindo *a*, *c*
  e *d*, chega-se a
  $$a - d = e + (c - d) + (1-\pi)(a - c) - (1-\pi)(b - d)$$
  "a − d é a diferença simples observada; as demais parcelas são os vieses".
- [s.22] **Na notação original:**
  $$\underbrace{E[Y_i(1)/T_i=1] - E[Y_i(0)/T_i=0]}_{SDO} = EMP + \underbrace{\{E[Y_i(0)/T_i=1] - E[Y_i(0)/T_i=0]\}}_{\text{viés de seleção}} + \underbrace{(1-\pi)\,[EMPT - EMPNT]}_{\text{viés de efeitos heterogêneos}}$$
  Viés de seleção: "gerado pela comparação de dois grupos distintos". Viés de efeitos
  heterogêneos: "gerado pela diferença do impacto do programa entre os dois grupos".
- [s.23–24] No exemplo: viés de seleção = −2,33; viés heterogêneo = (2/5)(2 − 1) = 0,4;
  identidade **−0,33 = 1,6 − 2,33 + 0,4**; "o sinal da diferença simples chega a se
  inverter em relação ao EMP".
- **Como lidar** [s.25]: a hipótese de **efeitos constantes de tratamento** elimina o viés
  de efeitos heterogêneos; a hipótese de **independência do tratamento em relação aos
  resultados potenciais** elimina os dois vieses — "as unidades são atribuídas ao
  tratamento e ao controle independentemente do seu resultado potencial".

**Regressão e hipóteses de identificação** (MRP p.29–34 [s.27–32]):
- Resultado observado [s.27]: $Y_i = T_i\,Y_i(1) + (1 - T_i)\,Y_i(0) = Y_i(0) + T_i\,(Y_i(1) - Y_i(0))$ — equação (3).
- Substituindo (2) em (3) [s.28]: $Y_i = \alpha + \varepsilon_i + T_i[(\alpha + \beta_i + \varepsilon_i) - (\alpha + \varepsilon_i)]$, logo
  $$Y_i = \alpha + \beta_i T_i + \varepsilon_i$$
  "$\beta_i$ capta o efeito de cada unidade: o modelo admite efeitos heterogêneos".
- **Hipótese de efeito homogêneo** [s.29]: $\beta_i = \beta \Rightarrow Y_i = \alpha + \beta T_i + \varepsilon_i$; EMPT = EMPNT; e
  $SDO = EMP + \{E[Y_i(0)/T_i=1] - E[Y_i(0)/T_i=0]\}$ (sobra só o viés de seleção).
- **Hipótese de independência** [s.30] ("randomização da atribuição"):
  $$(Y_i(1),\,Y_i(0)) \perp T$$
  implica $E[Y_i(1)/T_i=1] - E[Y_i(1)/T_i=0] = 0$ e $E[Y_i(0)/T_i=1] - E[Y_i(0)/T_i=0] = 0$ —
  "e o viés de seleção será zero". [s.31] Também elimina o viés de heterogeneidade
  (EMPT − EMPNT = 0), e $SDO = E[Y_i(1)/T_i=1] - E[Y_i(0)/T_i=0] = EMP$.
- **Métodos de estimação** [s.32] — "cada método busca garantir que a hipótese de
  independência seja válida": *aleatorização* (padrão ouro: a atribuição é sorteada);
  *diferenças em diferenças* (controla para características não observáveis constantes
  no tempo); *pareamento* (independência condicional às características observáveis);
  *variáveis instrumentais* (variável correlacionada com o tratamento, mas não com o termo
  de erro); *regressão descontínua* (usa unidades próximas à linha de corte, controlando
  por características observáveis e não observáveis).

**SUTVA — Stable Unit Treatment Value Assumption** (MRP p.36–38 [s.34–35]; referência
sugerida Cunningham, 2021, item 4.1):
- **Ausência de interferência:** "o resultado potencial de qualquer indivíduo depende apenas
  do tratamento que ele recebeu, e não do tratamento de outros indivíduos". Violações:
  efeitos de transbordamento (*spillovers*), efeitos de rede (*network interference*),
  efeitos de pares (*peer effects*) ou efeitos de equilíbrio geral.
- **Ausência de variação oculta nos tratamentos:** "a 'dosagem' ou a intensidade do
  tratamento é uniforme para todas as unidades tratadas". Violação: o tratamento tem
  variações ocultas de intensidade ou qualidade não consideradas na modelagem.
- Implicações [s.35]: o MRP assume o SUTVA "por simplicidade"; quando não vale, "os
  pesquisadores precisam identificar as violações e incorporá-las nos modelos
  estatísticos".

### 2.6 Validade interna e externa (VAL)

**Validade interna.**
- "Uma avaliação de impacto é válida internamente quando a condição *ceteris paribus* é
  atendida" — não há influência de outros fatores e a avaliação identifica corretamente o
  efeito causal; obtém-se por meio de um contrafactual válido (VAL [s.3]).
- Contrafactual válido = os três quesitos (IC [s.6]) ⇒ "hipótese de independência do
  tratamento em relação aos resultados potenciais" (VAL p.4 [s.3]).
- **Ameaças à validade interna** (VAL p.5 [s.4], lista exata, sem definições no slide):
  **viés de seleção; variável de confusão; maturação; efeitos de testes/prática;
  transbordamento; tamanho da amostra; eventos externos; instrumentação; atrito.**
- "Em geral, qualquer fator que reduza a habilidade do estudo de estabelecer a relação
  causal entre a variável dependente e independente, reduzirá a validade interna do
  estudo" (VAL p.6 [s.5]).

**Validade externa.**
- "Uma avaliação de impacto é válida externamente quando a amostra da avaliação representa
  corretamente a população alvo do programa, permitindo a generalização dos seus
  resultados." **Ameaças: características dos participantes; ambiente; tempo** (VAL p.8
  [s.7]). "Qualquer fator que reduza a generalização do estudo, reduzirá sua validade
  externa" (VAL p.9 [s.8]).
- Referência-base: Williams, M. J. "External Validity and Policy Adaptation: From Impact
  Evaluation to Policy Design", *The World Bank Research Observer* 35(2): 158–191, ago.
  2020 (VAL p.11 [s.9]; PDF no repositório).
- Um desenho baseado em evidência rigorosa pode não bastar: "o contexto local e sua
  interação com a teoria da mudança pode levar a resultados/impactos distintos" (VAL p.12
  [s.10]).
- Distinguir **generalização da evidência (academia: "a política teve impacto?")** de
  **aplicabilidade da evidência (gestor público: "a política terá impacto aqui?")** (VAL
  p.13 [s.11]).
- Dois tipos (VAL p.14–15 [s.12–13], Williams fig. 1): **a) ampliação da política**
  (*scale up*) dentro da mesma população de interesse — diagrama de elipses aninhadas
  população geral ⊃ população-alvo ⊃ amostra do estudo; **b) transposição da política**
  (*transporting*) para uma nova população-alvo.
- No caso a), validade externa exige amostra estatisticamente representativa da população
  de interesse; "a ampliação de escala de uma política pode reduzir sua efetividade"
  (VAL p.16 [s.14]). No caso b), além de a), depende "da interação entre o contexto local
  e a teoria da mudança"; diferenças de impacto entre contextos "devem ter afetado um ou
  mais elos da cadeia causal" (VAL p.17 [s.15]).
- **Dimensões de contexto** (não exaustivo; VAL p.18 [s.16]): local e suas características
  sociais, culturais, demográficas, econômicas e políticas; população-alvo; período de
  implementação; políticas relacionadas; estrutura de implementação (recursos,
  competência, restrições políticas etc.).
- Exemplo (Williams fig. 2 — Bangladesh Integrated Nutrition Programme; VAL p.19 [s.17]):
  insumos (recursos financeiros e trabalhadores potenciais) → atividades (comprar alimentos,
  contratar e treinar trabalhadores) → produtos (alimento suplementar e orientação
  nutricional às mães) → RI 1 (consciência nutricional das mães melhora) → RI 2 (mães
  decidem usar o alimento extra para si e para os filhos) → resultado final (nutrição da
  mãe e da criança melhora).
- **Abordagens para validade externa** (VAL p.21–22 [s.19–20]): as abordagens acadêmicas
  focam a generalização, com pouca discussão da aplicabilidade. *Agregação de evidências*
  calcula o efeito médio para um "contexto médio" — bom indicativo para contextos próximos
  da média, "indicadores 'pobres' na presença de alta heterogeneidade do impacto entre
  contextos (alta variância)"; *modelos estruturais com previsão fora da amostra* — limitados
  no número de variáveis e cenários; *avaliações piloto* — limitadas no número de
  dimensões que podem ser alteradas.
- **Mecanismo de mapeamento** (VAL p.23–28 [s.21–26]): "metodologia para mapear as
  interações entre contexto e teoria da mudança de forma a identificar possíveis falhas que
  afetariam o impacto da política" (foco: transposição). Três etapas: (1) **estabelecer a
  teoria da mudança** pela qual a política teve impacto medido no contexto anterior;
  (2) **definir as hipóteses contextuais** mais importantes que sustentam cada etapa;
  (3) **definir as reais características contextuais correspondentes**, destacando
  diferenças entre contexto e pressupostos. Formato da tabela: **Etapa da cadeia |
  Hipótese contextual | Contexto real**. No exemplo, todas as linhas coincidem, exceto RI 2:
  hipótese "mães controlam a alocação do alimento no domicílio" × contexto real "mães NÃO
  controlam" — **"Elo rompido"**. Desafios: definir a TdM, as hipóteses contextuais mais
  importantes e as características reais (dados); conduzir "de cima para baixo";
  limitação: "fornece a direção do impacto, mas não permite quantificá-lo".
- **Transposição e adaptação** (VAL p.30–31 [s.28–29]): pouca literatura; questão-chave
  "dado o contexto local, o quanto e como adaptar?"; o mapeamento não define a adaptação,
  mas identifica os aspectos problemáticos e o porquê; não há solução universal. Espectro
  (Williams fig. 4): **política própria — adaptações substantivas — adaptações superficiais
  — fidelidade total** (mais adaptação ↔ mais fidelidade); com melhor evidência de outros
  contextos, o ótimo se desloca para a fidelidade; com melhor informação local, para a
  adaptação.

**Validade × amostragem** (AMO [s.5, s.8]): listagem que não coincide com a população de
interesse gera **viés de cobertura**, e os resultados só têm validade externa para a
população da listagem; **amostragem aleatória ≠ seleção aleatória** — a amostragem
aleatória serve à validade externa; a seleção (atribuição) aleatória, à validade interna.

### 2.7 Amostragem e poder estatístico (AMO) — fórmulas exatas

**Amostragem** (AMO [s.3–8]):
- "Amostragem é o processo de escolher unidades a partir de uma população de interesse,
  com o objetivo de estimar as características dessa população"; o processo de extração
  "é crucial" [s.3].
- Etapas [s.4]: determinar a população de interesse; identificar a base de informação para
  amostragem (**listagem**); extrair a amostra de acordo com os cálculos do poder.
- Listagem = "a relação mais abrangente da população que pode ser obtida"; se não coincide
  com a população de interesse → viés de cobertura [s.5].
- Amostragem **probabilística** é a mais rigorosa (probabilidade bem definida de cada
  unidade ser extraída); a não probabilística pode gerar erros sérios (viés) [s.6].
  Métodos probabilísticos [s.7]: **aleatória** (mesma probabilidade para cada unidade);
  **aleatória estratificada** (população dividida em grupos, amostragem aleatória em cada
  grupo); **por conglomerados** (unidades agrupadas em conglomerados; amostra aleatória de
  conglomerados).

**Poder estatístico** (AMO [s.10–16]):
- "Determina o tamanho mínimo da amostra necessário para detectar o efeito esperado"; em
  avaliação de impacto, a menor amostra para detectar diferenças significativas entre
  tratamento e comparação; ajuda no *trade-off* tamanho da amostra × custo [s.10].
- Impacto = diferença entre as médias do resultado no tratamento e na comparação; testa-se
  H0: diferença = 0 (não há impacto) contra H1: diferença ≠ 0 (há impacto) [s.11].
- **Erro tipo I**: concluir que houve impacto quando não há (rejeitar H0 verdadeira).
  **Erro tipo II**: concluir que não houve impacto quando há (não rejeitar H0 falsa)
  (AMO p.12 [s.13]).
- Probabilidade do erro tipo I = **nível de significância α**. **Poder estatístico =
  probabilidade de detectar impacto quando ele existe = (1 − β)**; alto poder = baixo risco
  de erro tipo II (AMO p.13 [s.14]).
- Figuras 7.3 ("Reducing Type II Error by Reducing the Significance Level") e 7.4 ("...by
  Increasing Sample Size") (AMO p.14 [s.15], "Source: Authors"). *Complementar:* vêm de
  White e Raitzer (2017, p. 120 = PDF p.134): passar a significância de 5% para 10%
  reduz o erro tipo II de cerca de 40% para cerca de 25% no exemplo, à custa de mais erro
  tipo I; aumentar a amostra reduz o erro tipo II; nível aceitável usual 20% (poder 80%).
- Baixo poder compromete achar resultados significativos; "avaliações de baixo poder podem
  levar a fechamento de programas, que na verdade possuem impacto"; minimizar o erro tipo
  II exige amostras suficientemente grandes (AMO p.15 [s.16]).

**Cálculo do poder — passos** (AMO p.17–20 [s.18–22]). Cerne: "qual o tamanho da amostra
necessária para termos um nível aceitável do erro tipo II?"
1. O programa é implementado no nível de conglomerados?
2. Qual(is) o(s) indicador(es) de resultado? — "advém do objetivo, teoria da mudança e
   pergunta principal"; indicadores diferentes podem levar a amostras distintas [s.20].
3. Qual o nível mínimo de impacto que justificaria o investimento? — "questão de política
   pública"; a resposta fornece o **efeito mínimo detectável** que a avaliação precisa
   identificar [s.20].
4. Qual a média do resultado na população de interesse e a variância subjacente? — quanto
   maior a variabilidade, maior a amostra [s.22].
5. Níveis razoáveis de poder e significância? — **"Tradicionalmente trabalha-se com poder
   estatístico de 80% e α=5%"** [s.22].

**Sem conglomerados, indicador contínuo — tamanho da amostra** (AMO p.21 [s.23]):
$$n = \frac{\left(t_{\alpha/2} + t_{1-\beta}\right)^2 \sigma_y^2}{EMD^2\,P(1-P)}$$
"Sendo α o nível de significância, (1 − β) o poder estatístico, $\sigma_y$ o erro padrão da
variável de resultado, P a proporção da amostra alocada no grupo de tratamento e n o
tamanho da amostra. EMD é o efeito mínimo detectável." (O slide diz "erro padrão"; o WP26,
Tabela 2, define $\sigma_y$ como *standard deviation of the outcome variable* — no artigo,
escrever "desvio-padrão".)

**Definição do EMD** (AMO p.22 [s.21]): "o tamanho do efeito que uma avaliação de impacto é
desenhada para estimar para um determinado nível de significância e poder estatístico";
tudo mais constante, amostras maiores são necessárias para detectar diferenças menores ou
em resultados com maior variabilidade.

**Sem conglomerados, indicador contínuo — EMD** (AMO p.23 [s.24]):
$$EMD = \left(t_{\alpha/2} + t_{1-\beta}\right)\sigma_y\sqrt{\frac{1}{P(1-P)\,n}}$$
- Quanto menor o EMD, maior deve ser n.
- **O EMD é minimizado com amostra balanceada (P = 0,5).**
- Como $\sigma_y$ é desconhecido no desenho, "seu valor é estimado a partir de estudos
  similares".

**Com conglomerados, indicador contínuo — tamanho da amostra** (AMO p.30 [s.28]):
$$n = \frac{\left(t_{\alpha/2} + t_{1-\beta}\right)^2 \sigma_y^2}{EMD^2\,P(1-P)}\,\bigl(1 + (m-1)\rho\bigr)$$
onde $\rho = \dfrac{S_b^2}{S_b^2 + S_w^2}$ é **a correlação dentro do conglomerado** (ICC);
$S_b^2$ = variância **entre** os conglomerados da variável de resultado; $S_w^2$ = variância
**dentro** dos conglomerados; $(1 + (m-1)\rho)$ = **efeito do desenho**, "sendo m o número
de indivíduos dentro de cada conglomerado". (Aqui *n* é o total de indivíduos.)

*Derivação minha, não consta dos slides (útil para reportar EMD dado n):*
$EMD = (t_{\alpha/2} + t_{1-\beta})\,\sigma_y\sqrt{\dfrac{1 + (m-1)\rho}{P(1-P)\,n}}$.

**Regras com conglomerados** (AMO p.31 [s.29]): "o número de conglomerados importa muito
mais para os cálculos de poder estatístico do que o número de indivíduos dentro dos
conglomerados"; **"são necessários, pelo menos, 30 a 50 conglomerados em cada um dos
grupos de tratamento e de comparação"**, a depender da amostra; a variabilidade do
indicador dentro dos conglomerados afeta o cálculo.

**Exemplo 1 — Bolsa Capixaba** (AMO p.24–29 [s.25–26]); **calculadora indicada: "3ie Excel
Power Calculator and associated guide (Djimeu and Houndolo 2016)"** [s.25]. Estatísticas
descritivas da população-alvo [s.26]:

| Variável | Média | DP | Mín. | Máx. | Nº de indivíduos |
| --- | --- | --- | --- | --- | --- |
| Insegurança alimentar | 4,602 | 3,600 | 0 | 14 | 1.182 |
| Insegurança de renda | 12,151 | 6,050 | 0 | 36 | 1.182 |
| Qualidade de vida: domínio psicológico | 20,204 | 3,901 | 6 | 30 | 1.175 |
| Locus de controle | 18,267 | 2,694 | 7 | 28 | 1.167 |
| Renda familiar per capita | 181,543 | 186,065 | 10 | 2000 | 1.147 |
| Gasto familiar per capita com alimentos | 93,550 | 59,545 | 1,75 | 720 | 996 |
| Gasto familiar per capita com moradia | 261,998 | 203,473 | 13 | 1407 | 1.125 |

Gráficos "Poder estatístico, efeito mínimo detectável e amostra mínima" (AMO p.26–29
[s.26]): eixo x "Tamanho Total da Amostra" (0–4000; curva de ~300 a 3000), eixo y "Efeito
Mínimo Detectável (em DP)" (0–0,35); notas: significância 0,05, poder 80%. Pontos
rotulados: insegurança alimentar (1200; 0,16); insegurança de renda (1200; 0,16); qualidade
de vida psicológica (1200; 0,16); locus de controle (1200; 0,16); gasto com alimentos
(996; 0,18); gasto com moradia (1125; 0,17); renda familiar per capita (1147; 0,17).
*Verificação própria* (`analise/slides_poder_verificacao.py` →
`analise/tabelas/slides_poder_verificacao.csv`): com P = 0,5, $z_{0,975}$ = 1,960 e
$z_{0,80}$ = 0,842, a fórmula do [s.24] em unidades de DP dá 0,162 (n = 1200), 0,178
(996), 0,167 (1125), 0,165 (1147), 0,324 (300) e 0,102 (3000) — os rótulos dos slides são
esses valores arredondados, ou seja, as curvas são a fórmula sem conglomerados com
amostra balanceada. O EMD em DP depende só de n e P; a variável muda apenas o *n*
disponível.

**Exemplo 2 — Amigos do Zippy** (AMO p.32–33 [s.30]): alocação do tratamento por sorteio;
18 escolas no tratamento e 18 no controle (aprox. 1.750 crianças em cada grupo). Tabela
"Estimativas do Impacto do Programa Amigos do Zippy":

| Dimensão | Manaus: média | DP | Impacto detectável | Impacto estimado | Vila Velha: média | DP | Impacto detectável | Impacto estimado |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Inteligência Emocional | 14,9 | 3,8 | 12% | **18%** | 14,9 | 4,3 | 8% | −3% |
| Habilidades Sociais – Criança | 25,2 | 5,5 | 15% | 5% | 26,3 | 5,5 | 6% | −3% |
| Empatia | 7,2 | 2,0 | 11% | −10% | 7,5 | 2,0 | 5% | 3% |
| Responsabilidade | 7,6 | 1,8 | 13% | −8% | 7,7 | 1,8 | 7% | −9% |
| Autocontrole | 6,7 | 2,5 | 17% | 14% | 6,8 | 2,6 | 11% | −7% |
| Assertividade | 3,6 | 1,9 | 11% | 3% | 4,1 | 1,8 | 6% | **11%** |
| Habilidades Sociais – Pais | 28,5 | 7,0 | 16% | **20%** | 29,2 | 7,1 | 5% | 3% |
| Responsabilidade | 4,8 | 1,9 | 13% | **16%** | 4,1 | 2,0 | 5% | 4% |
| Autocontrole | 5,8 | 2,3 | 13% | −7% | 5,6 | 2,2 | 5% | 3% |
| Afetividade e cooperação | 8,1 | 2,3 | 11% | 6% | 8,7 | 2,2 | 5% | 0% |
| Desenvoltura social | 3,9 | 1,9 | 12% | **27%** | 4,3 | 2,0 | 8% | 4% |
| Civilidade | 5,7 | 1,7 | 11% | **16%** | 6,3 | 1,5 | 6% | −6% |
| Comportamento | 10,4 | 5,4 | 13% | −4% | 10,0 | 5,5 | 5% | 2% |
| Internalizantes | 3,5 | 2,0 | 12% | 1% | 3,3 | 2,0 | 5% | **6%** |
| Externalizantes | 6,8 | 4,1 | 14% | −6% | 6,8 | 4,2 | 5% | 1% |

Negrito = células destacadas em amarelo no slide. O slide não explica o destaque; *leitura
minha*: coincidem com os casos em que o impacto estimado positivo iguala ou supera o
impacto detectável. O slide também não diz se os 18 + 18 escolas são por cidade ou no
total [VERIFICAR]; de todo modo, 18 por braço fica abaixo da regra de 30–50 conglomerados
por grupo do [s.29] (observação minha).

**Considerações finais do cálculo de poder** (AMO p.34–35 [s.31–32]):
- *Métodos quase-experimentais* exigem amostras maiores do que a seleção aleatória; **o
  poder pode ser ampliado com dados de linha de base**.
- *Diferentes formas de implementação ou inovações no desenho*: o EMD pode ser menor do que
  o EMD em comparação ao grupo que não recebe o tratamento.
- *Comparação de subgrupos*: eleva o número de observações, podendo duplicar.
- *Múltiplos resultados*: aumentam a probabilidade de detectar impacto em um deles por
  acaso; considerar **testes de significância estatística conjunta** das mudanças em
  vários resultados.
- *Cumprimento parcial ou atrito*: exigem amostra maior, "mesmo que o cumprimento parcial ou
  atrito sejam aleatórios".

**Covariadas e R² — não constam dos slides.** Os slides só dizem que dados de linha de
base ampliam o poder ([s.31]). As fórmulas estão no guia da calculadora indicada
(*complementar*, WP26):

| Caso (WP26) | Fórmula do MDE ($\delta$) | Onde |
| --- | --- | --- |
| Individual, contínuo | $\delta = (t_1 + t_2)\,\sigma_y\sqrt{\dfrac{1}{P(1-P)n}}$ | PDF p.30 (impr. 21), §7.1.1, Tab. 2 |
| Individual, contínuo, com covariadas | $\delta = (t_1 + t_2)\,\sigma_y\sqrt{\dfrac{1}{P(1-P)n}\,(1 - R^2)}$ | PDF p.31 (impr. 22), §7.1.2, Tab. 3 |
| Conglomerados, contínuo | $\delta = \dfrac{t_1 + t_2}{\sqrt{P(1-P)J}}\,\sigma_y\sqrt{\rho + \dfrac{1-\rho}{n}}$ | PDF p.35 (impr. 26), §7.2.1, Tab. 7 |
| Conglomerados, contínuo, com covariadas | $\delta = \dfrac{t_1 + t_2}{\sqrt{P(1-P)J}}\,\sigma_y\sqrt{\left[\rho + \dfrac{1-\rho}{n}\right](1 - R^2)}$ | PDF p.36 (impr. 27), §7.2.2, Tab. 8 |

- No WP26, $t_1$ = valor t da significância; $t_2$ = valor t do poder; **nos casos com
  conglomerados, *n* = indivíduos por conglomerado e *J* = número de conglomerados** (nos
  slides, *n* é o total e *m* os indivíduos por conglomerado). $R^2$ = "proportion of
  outcome variance explained by level 1 covariate(s)"; nota 3 (PDF p.31): o quadrado da
  correlação entre a medida de linha de base da(s) covariada(s) e a medida pós-implementação
  do resultado (coeficiente de determinação). Armadilha: a lista de abreviaturas do WP26
  chama R² de "coefficient of variation".
- *Equivalência (derivação minha):* com $N = J\,m$, $\rho + (1-\rho)/m = [1 + (m-1)\rho]/m$,
  e a fórmula do WP26 §7.2.1 resolvida para *N* é exatamente a do slide [s.28].
- Exemplos WP26 (conferidos no script acima): individual, $t_1$ = 1,96, $t_2$ = 0,84,
  $\sigma_y$ = 2.400 xelins quenianos, P = 0,5, n = 1.000 → MDE = 425,7 (recalculado
  425,0; a diferença provavelmente vem de valores t com graus de liberdade na calculadora
  [interpretação]); com R² = 0,5 → 301. Conglomerados: $t_1$ = 2,58 (α = 0,01), $t_2$ = 1,28
  (poder 90%), P = 0,5, J = 240 aldeias, 20 agricultores por aldeia, $\sigma_y$ = 0,47 ha,
  ρ = 0,037 → MDE = 0,0683 ha; com R² = 0,4 → 0,053 ha.
- Múltiplos resultados (WP26 PDF p.29, impr. 20): recomenda ajustar a significância no
  cálculo de poder, por exemplo com Bonferroni (o mais conservador; reduz o poder).

### 2.8 Agregação de evidências

- É a aula 7 (23/09) do cronograma (APR [s.9]), mas **não há slides dessa aula no
  repositório** [VERIFICAR se foram disponibilizados no Google Sala de Aula].
- O único conteúdo em slide é o de VAL p.21 [s.19]: a agregação de evidências "calcula o
  efeito médio do tratamento para um 'contexto médio'"; é bom indicativo para contextos
  próximos da média e "pobre" sob alta heterogeneidade entre contextos (alta variância). O
  mesmo slide a coloca como abordagem acadêmica de **generalização**, não de
  aplicabilidade.
- Leituras no repositório sobre o tema (*complementar*; não resumidas aqui):
  Field e Gillett (2010), "How to do a meta-analysis", *British Journal of Mathematical
  and Statistical Psychology* 63: 665–694, DOI 10.1348/000711010X502733 — roteiro em seis
  passos (busca da literatura; critérios de inclusão; cálculo dos tamanhos de efeito;
  meta-análise básica; análises avançadas; redação); Havránek et al. (2020), "Reporting
  guidelines for meta-analysis in economics", *Journal of Economic Surveys* 34(3):
  469–475, DOI 10.1111/joes.12363 — atualização das diretrizes MAER-Net de 2013. Também
  estão no repositório Ellis (2010) sobre tamanhos de efeito e o cap. 2 de *Statistics
  Done Wrong*.
- Uso no artigo: a "breve revisão da literatura" deve dizer se há evidência agregada
  sobre leis de incentivo fiscal à cultura e se o contexto capixaba está perto do
  "contexto médio" (VAL [s.19]); com heterogeneidade alta, preferir o mecanismo de
  mapeamento.

---

## 3. Mapa: seção obrigatória do artigo → conceitos e ferramentas do curso

A coluna "Ponte para a LICC" traz **sugestões minhas**, não conteúdo do curso; os fatos
sobre a LICC vêm do contexto do projeto (`CLAUDE.md`, `licc-gov/`) e dos dados em
`dados/licc/` (contagens conferidas nesta sessão: 69, 113, 123, 74 e 88 projetos em
`habilitados-2022…2026.csv`, total 467; 63 linhas em `oficial/captados-2025.csv`).

| Seção (INSTR item 2) | Conceitos e ferramentas do curso | Fontes | Ponte para a LICC (sugestão) |
| --- | --- | --- | --- |
| **1. Introdução com caracterização do problema/necessidade** | Diagnóstico do problema: identificar; caracterizar com dados quantitativos **comparando com outras regiões**; causas potenciais; lições de experiências anteriores. Problema = carência (não objetivo), com população-alvo, ligado aos resultados finais. Por que avaliar (aprendizado, accountability); quando avaliar (inovadora, replicável, estrategicamente relevante, não testada, influente). | TIP1 [s.4, s.11]; M03 [s.18]; TIP2 [s.16–17] | Formular o problema como carência de financiamento/acesso a bens culturais, com comparação ES × outras UFs (fonte externa a levantar). Justificar a avaliação pelos critérios de TIP2 [s.17]. |
| **2. Caracterização da política** | Etapa "caracterização da política" da análise executiva; projeto de implementação (etapas, atividades, recursos e fontes, cronograma e governança); insumos × atividades × produtos. | TIP1 p.18 [s.17]; TIP1 p.14 [s.13]; TdM [s.9] | Insumo = renúncia de ICMS (teto anual; R$ 25 mi em 2025); atividades = edital, habilitação pela SECULT, captação; produto = projeto patrocinado. Cotas do art. 18 da IN 001/2025 (30/10/10/50%). Regras do `CLAUDE.md`: captados ≠ habilitados; ausência ≠ zero. |
| **3. Breve revisão da literatura** | Evidências da literatura como fonte da cadeia de resultados; "há evidências sobre programas semelhantes em circunstâncias parecidas?"; generalização × aplicabilidade; ampliação × transposição; agregação de evidências e seus limites. | TdM [s.8]; TIP2 [s.16]; VAL p.12–22 [s.10–20]; Field e Gillett (2010); Havránek et al. (2020) | Separar evidência de outras leis de incentivo (transposição, VAL [s.15]) da evidência sobre a própria LICC. Referências só com DOI/página conferidos. |
| **4. Desenho da política (com TdM) e sua avaliação** | Avaliação de desenho (teoria do programa + modelo lógico); cadeia de resultados em árvore J-PAL; cinco passos (propósito, cadeia, premissas e riscos, hipótese causal, indicadores); gabarito "Se [atividades] geram [produtos]..."; marco lógico/modelo lógico com premissas e riscos (formato Bolsa Atleta); indicadores SMART; túnel de atrito; falha de implementação × falha de teoria; mecanismo de mapeamento (hipótese contextual × contexto real, "elo rompido"); perguntas da seção 2.3. | TIP1 p.20 [s.19], [s.12]; TdM [s.3–22]; M03 [s.14–50]; VAL p.23–28 [s.21–26]; IJSN Vol. 1 p.9 | TdM da LICC: renúncia → habilitação → captação → execução → acesso/produção cultural. Túnel de atrito com dados: habilitados → captaram → executaram, **sem** dividir captados de 2025 por habilitados de 2025 (dos 63 que captaram em 2025, 30 foram habilitados em 2024, `CLAUDE.md` regra 4). Premissa candidata: existência de empresas contribuintes de ICMS dispostas a patrocinar fora da RMGV (hipótese contextual a checar). |
| **5. Proposta de avaliação de impacto** | Pergunta de causa e efeito; contrafactual; prospectiva × retrospectiva; escolha do método por características operacionais e momento; parâmetro de interesse (EMP, **EMPT — "útil quando a participação é voluntária"**, EMPNT para expansão); viés de seleção e autosseleção; decomposição SDO; independência/independência condicional; métodos (aleatorização, DiD, pareamento, VI, RD, controle sintético); SUTVA; ameaças à validade interna e externa; plano de avaliação (pergunta, sub-perguntas, metodologia, indicadores, fonte, órgão); ética ("acesso não deve ser negado ou adiado"). | TIP2 [s.3–14]; IC [s.3–11]; MRP [s.9–35]; VAL [s.3–8]; TIP1 p.15 [s.14] | Participação voluntária dos dois lados (proponente se inscreve, empresa escolhe o projeto) → EMPT. Comparar "captou × não captou" entre habilitados é o caso "inscritos × não inscritos" (IC [s.10]): viés de seleção provável. SUTVA: teto fixo de renúncia sugere interferência entre projetos (o que um capta pode faltar a outro — hipótese); valores captados diferentes = variação de "dosagem". Ética limita sorteio da habilitação; RD só se houver nota com linha de corte na habilitação [VERIFICAR nas normas]. |
| **5a. Desenho da amostra e fonte de dados** | População de interesse; listagem; viés de cobertura; amostragem probabilística (aleatória, estratificada, por conglomerados); amostragem ≠ seleção aleatória; linha de base. | AMO [s.3–8]; IC [s.13–16] (Bolsa Capixaba como modelo de plano amostral com escalonamento) | Listagem candidata: anexos oficiais de habilitados (`dados/licc/habilitados/`, 467 projetos 2022–2026; 2025 tem 58 de 74 com município). Estratos naturais: cotas do art. 18 (p.ex. fora da RMGV). Declarar cobertura, nunca imputar. |
| **5b. Cálculo do poder estatístico** | Passos 1–5; fórmulas de n e EMD sem e com conglomerados; ρ = $S_b^2/(S_b^2+S_w^2)$; efeito do desenho $1+(m-1)\rho$; α = 5%, poder 80%; P = 0,5 minimiza o EMD; $\sigma_y$ de estudos similares; ≥ 30–50 conglomerados por braço; ajustes (quase-experimento, subgrupos, múltiplos resultados, atrito, linha de base/R²); calculadora 3ie. | AMO p.17–35 [s.18–32]; WP26 §7 (complementar) | Se a unidade for o município (conglomerado), o número de municípios capixabas limita J [VERIFICAR número via IBGE] e pode inviabilizar 30–50 por braço. EMD a justificar como "questão de política pública" (AMO [s.20]). Usar o túnel de atrito para não superestimar participação (TdM [s.19]). |
| **6. Conclusão** | Recomendações; matriz SWOT (análise executiva); necessidade de avaliações adicionais; limitações de validade interna/externa. | TIP1 p.18 [s.17]; VAL | Recomendações sobre o desenho **como está** (sem redesenho do mecanismo — fora do escopo). |
| **7. Referências** | Citar material da disciplina (Gertler et al.; Itaú Social 2017; Williams 2020; Djimeu e Houndolo 2016; White e Raitzer 2017; IJSN/SiMAPP). | — | ABNT; só referências verificadas (`CLAUDE.md`). |
| **Anexo: declaração de uso de IA** | Portaria CNPq 2.664/2026; modelo em anexo das instruções. | INSTR item 5 | Modelo não localizado [VERIFICAR]. Os próprios slides trazem uma declaração-tipo no último slide (p.ex. AMO p.36), que pode orientar o texto. |

---

## 4. Glossário da notação e do vocabulário dos professores

### 4.1 Notação (com colisões de símbolos entre aulas)

| Símbolo | Significado exato no material | Onde | Atenção |
| --- | --- | --- | --- |
| *P* | Programa (P = 1 participa; P = 0 não) em $\Delta = (Y\mid P=1) - (Y\mid P=0)$ | IC [s.3, s.5] | **Colide** com *P* de AMO. |
| *P* | "Proporção da amostra alocada no grupo de tratamento" | AMO p.21 [s.23] | No MRP a parcela tratada na população é **π**. |
| Δ | Impacto/efeito causal do programa | IC [s.3] | — |
| *Y* | Variável de resultado | IC [s.3]; MRP [s.5] | — |
| *T*, $T_i$ | Tratamento (1 = tratado, 0 = não tratado) | MRP [s.5] | — |
| *i* | Unidade de análise | MRP [s.5] | — |
| $Y_i(1)$, $Y_i(0)$ | Resultado da unidade *i* caso seja / não seja tratada; o par é "resultados potenciais" | MRP [s.5–6] | — |
| $Y_i$ | Resultado efetivo observado $= T_iY_i(1) + (1-T_i)Y_i(0)$ | MRP p.29 [s.27] | — |
| $\beta_i$ | Impacto individual $Y_i(1) - Y_i(0)$; β sob efeito homogêneo | MRP [s.6], p.31 [s.29] | **Colide** com β de AMO (erro tipo II). |
| α | Intercepto em $Y_i(0) = \alpha + \varepsilon_i$ | MRP [s.7] | **Colide** com α de AMO (significância). |
| $\varepsilon_i$ | Componente não observável que afeta os resultados de *i* | MRP [s.7] | — |
| π | Parcela das unidades de análise que recebem o tratamento | MRP p.19 [s.18] | — |
| *a, b, c, d, e* | $E[Y_i(1)/T_i=1]$, $E[Y_i(1)/T_i=0]$, $E[Y_i(0)/T_i=1]$, $E[Y_i(0)/T_i=0]$, EMP | MRP p.20 [s.19] | "/" = condicional a. |
| EMP (ATE) | Efeito médio do programa $E[\beta_i]$ | MRP [s.9] | Siglas em português nos slides; inglês entre parênteses. |
| EMPT (ATT) | Efeito médio sobre os tratados $E[\beta_i / T_i = 1]$ | MRP [s.10] | — |
| EMPNT (ATU) | Efeito médio sobre os não tratados $E[\beta_i / T_i = 0]$ | MRP [s.11] | — |
| SDO | "Diferença simples" $E[Y_i(1)/T_i=1] - E[Y_i(0)/T_i=0]$ | MRP [s.16] | Sigla do inglês (*simple difference in outcomes*, Cunningham) — expansão não escrita no slide. |
| ⊥ | Independência: $(Y_i(1), Y_i(0)) \perp T$ | MRP p.32 [s.30] | — |
| α | Nível de significância = probabilidade do erro tipo I | AMO p.13 [s.14] | Padrão 5%. |
| 1 − β | Poder estatístico; β = probabilidade do erro tipo II | AMO p.13 [s.14] | Padrão 80%. |
| $t_{\alpha/2}$, $t_{1-\beta}$ | Valores críticos da significância (bicaudal) e do poder | AMO p.21 [s.23] | WP26 usa $t_1$, $t_2$ (1,96 e 0,84 para 5% e 80%). |
| $\sigma_y$ | "Erro padrão da variável de resultado" (slide) | AMO p.21 [s.23] | É o desvio-padrão do resultado (WP26 Tab. 2). |
| EMD | Efeito mínimo detectável | AMO p.21–23 [s.21–24] | Em inglês MDE; WP26 usa δ. |
| *n* | Tamanho (total) da amostra | AMO p.21, p.30 [s.23, s.28] | No WP26 com conglomerados, *n* = indivíduos **por** conglomerado. |
| *m* | Número de indivíduos dentro de cada conglomerado | AMO p.30 [s.28] | = *n* do WP26 §7.2. |
| ρ | Correlação dentro do conglomerado $S_b^2/(S_b^2+S_w^2)$ (ICC) | AMO p.30 [s.28] | — |
| $S_b^2$, $S_w^2$ | Variância entre / dentro dos conglomerados da variável de resultado | AMO p.30 [s.28] | — |
| $1+(m-1)\rho$ | Efeito do desenho | AMO p.30 [s.28] | — |
| *J* | Número de conglomerados | WP26 Tab. 7 (complementar) | Não aparece nos slides. |
| $R^2$ | Proporção da variância do resultado explicada por covariadas de nível 1 | WP26 Tab. 3 e nota 3 (complementar) | Não aparece nos slides. |
| BL, RCB, RCE | Benefício líquido; razão custo-benefício; razão custo-efetividade | TIP1 p.23–24 [s.22–23] | RCB = Custo/Benefício (não o inverso). |

### 4.2 Vocabulário (termos exatos usados pelos professores)

- **Avaliação** — "análise sistemática do desenho, da implementação e dos resultados de uma
  intervenção ou política pública" (TIP1 [s.3]).
- **Monitoramento** — "processo contínuo de acompanhamento ... sob o prisma da
  implementação" (TIP1 [s.5]).
- **Aprendizado / Accountability** — os dois fins da avaliação (TIP1 [s.4]).
- **Perguntas descritivas / normativas / de causa e efeito** (TIP1 [s.7]).
- **Avaliação ex-ante / ex-post / análise (avaliação) executiva** (TIP1 [s.8]).
- **Avaliação de desenho** — "analisa a racionalidade do programa: a lógica que conecta
  problema, ações e resultados esperados" (TIP1 p.20 [s.19]).
- **Teoria do Programa** — "explicita as hipóteses causais que sustentam a intervenção";
  **Modelo Lógico** — "organiza insumos, atividades, produtos e resultados em uma cadeia"
  (TIP1 p.20 [s.19]).
- **Avaliação de processos**, **avaliação de impacto**, **custo-benefício**,
  **custo-efetividade** (TIP1 p.21–24 [s.20–23]).
- **Avaliação teórica** — nome J-PAL da etapa em que entra a TdM (M03 [s.2]).
- **Impacto** — "relação causal entre a política e o resultado observado" (TIP2 [s.3]).
- **Contrafactual** — "qual teria sido o resultado para os beneficiários da política, caso
  eles não tivessem participado dela?" (TIP2 [s.4]).
- **Grupo de tratamento / grupo de controle ou de comparação** (TIP2 [s.4]; IC [s.5]).
- **Avaliação prospectiva / retrospectiva** (TIP2 [s.6]).
- **Padrão ouro** — seleção aleatória (TIP2 [s.7]; MRP [s.32]).
- **Condição ceteris paribus** (IC [s.7]; VAL [s.3]).
- **Estimativas falsas do contrafactual**: comparação **antes e depois (pré-pós ou
  reflexiva)**; comparação entre **inscritos e não inscritos (autosseleção)** (IC [s.8, s.10]).
- **Viés de seleção** — "ocorre quando as razões pelas quais um indivíduo participa de um
  programa estão correlacionadas com os resultados" (IC [s.11], citando Gertler et al.
  p. 66); em regressão, "omissão de variável relevante"; na decomposição,
  $E[Y_i(0)/T_i=1] - E[Y_i(0)/T_i=0]$ (MRP [s.22]).
- **Viés de efeitos heterogêneos** (ou "viés heterogêneo", "viés de heterogeneidade") —
  $(1-\pi)[EMPT - EMPNT]$ (MRP [s.22–23, s.31]).
- **Balanceamento / teste de médias** — "verifica se os grupos são estatisticamente
  idênticos antes do tratamento" (IC p.18); **linha de base** (IC [s.13, s.16]).
- **Hipótese de efeito homogêneo / efeitos constantes de tratamento**; **hipótese de
  independência** ("randomização da atribuição"); **independência condicional às
  características observáveis** (pareamento) (MRP [s.25, s.29–32]).
- **SUTVA** — **ausência de interferência**; **ausência de variação oculta nos
  tratamentos** ("dosagem"); violações: **transbordamento (spillovers), efeitos de rede,
  efeitos de pares, efeitos de equilíbrio geral** (MRP [s.34]).
- **Teoria da mudança** — "descreve a lógica causal entre uma intervenção e os resultados
  pretendidos" (TdM [s.3]); **cadeia de resultados**; **insumos, atividades, produtos,
  resultados (intermediários), resultados finais**; **implementação (lado da oferta)** ×
  **resultados (demanda + oferta)** (TdM [s.7–9]).
- **Problema/Necessidade; Propósito; Resultado intermediário; Resultado final** (M03
  [s.15–29]).
- **Premissas** — "condições externas necessárias"; **Riscos** — "efeitos negativos não
  esperados"; **hipótese causal** (M03 [s.33–35]). Os slides da professora usam
  "pressupostos" (TdM [s.4]) e "premissas e riscos" (TdM [s.15–16]).
- **Marco lógico** — matriz Impacto/Propósito/Componentes/Atividades × Objetivos/
  Indicadores/Fonte de verificação/Premissas (TdM [s.14]).
- **Indicadores SMART** — Específicos, Mensuráveis, Atribuíveis, Realistas, Direcionados
  (TdM [s.18]).
- **Túnel de atrito / funil de atrito** (TdM [s.19–22]).
- **Validade interna** — "quando a condição ceteris paribus é atendida"; **ameaças**: viés
  de seleção, variável de confusão, maturação, efeitos de testes/prática, transbordamento,
  tamanho da amostra, eventos externos, instrumentação, atrito (VAL [s.3–4]).
- **Validade externa** — "quando a amostra da avaliação representa corretamente a
  população alvo do programa, permitindo a generalização"; ameaças: características dos
  participantes, ambiente, tempo (VAL [s.7]).
- **Generalização da evidência (academia) × aplicabilidade da evidência (gestor público)**;
  **ampliação da política (scale up)** × **transposição da política (transporting)** (VAL
  [s.11–13]).
- **Mecanismo de mapeamento**; **hipóteses contextuais**; **contexto real**; **elo
  rompido**; **política própria / adaptações substantivas / adaptações superficiais /
  fidelidade total** (VAL [s.21–29]).
- **Agregação de evidências** — "calcula o efeito médio do tratamento para um 'contexto
  médio'" (VAL [s.19]).
- **Amostragem**; **população de interesse**; **listagem**; **viés de cobertura**;
  **amostragem probabilística / não probabilística**; **amostragem aleatória /
  aleatória estratificada / por conglomerados**; **"amostragem aleatória ≠ seleção
  aleatória"** (AMO [s.3–8]).
- **Poder estatístico**; **erro tipo I / tipo II**; **nível de significância**; **efeito
  mínimo detectável (EMD)**; **correlação dentro do conglomerado**; **variância entre /
  dentro dos conglomerados**; **efeito do desenho**; **cumprimento parcial**; **atrito**;
  **testes de significância estatística conjunta** (AMO [s.10–32]).

---

## 5. Pendências desta nota

- [VERIFICAR] Slides da aula de agregação de evidências (23/09) — não estão no repositório.
- [VERIFICAR] Modelo de declaração de uso de IA citado em INSTR item 5.
- [VERIFICAR] Referências citadas nos slides e ausentes do repositório: Cunningham (2021,
  item 4.1); White (2013, funil de atrito); World Bank Institute (2009); J-PAL; do Val
  (2023); Santana e Giuberti (2026); Soares, Thomas e Giuberti (prelo); Almeida (2025).
  Gertler et al. está no repositório (`Avaliação-de-impacto-na-prática-Segunda-edição (1).pdf`),
  mas as páginas citadas nos slides (p. 66; figs. 2.1, 3.3, B2.3.1) não foram conferidas
  nesta nota.
- [VERIFICAR] DOIs do cronograma de artigos (APR [s.10]).
- [VERIFICAR] Amigos do Zippy: 18 + 18 escolas por cidade ou no total.
