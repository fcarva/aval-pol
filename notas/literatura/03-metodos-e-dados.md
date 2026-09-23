# Literatura de métodos e fontes de dados para a avaliação de impacto da LICC

> Nota de trabalho (skill deep-research, modo *lit-review*, padrão "Policy
> Analysis" de `references/methodology_patterns.md`). Status: seções 0 a 5 completas (23/09/2026);
> §§ 2-5 escritas em sessão sem acesso à Crossref, a partir das referências já verificadas no § 1.
>
> Regras desta nota: só entram referências cujo DOI (ou URL oficial) foi
> conferido em 23/09/2026 na API do Crossref (`api.crossref.org/works/<DOI>`),
> no OpenAlex ou no arXiv (`export.arxiv.org/api`). Marca `[VERIFICADO]` =
> metadados (autores, título, periódico, volume, número, páginas, ano) batem
> com o registro. O conteúdo atribuído a cada texto foi conferido no resumo
> oficial (OpenAlex/Crossref) quando disponível; quando o resumo não estava
> disponível, a anotação se limita ao que é o objeto central e amplamente
> documentado do trabalho, e o que for mais específico vai com `[VERIFICAR]`.
> O que não pôde ser conferido fica fora ou marcado `[VERIFICAR]`.

## 0. Protocolo de busca e verificação

**Pergunta desta nota.** Que desenhos quase-experimentais (e experimentais,
sem mudar a regra de alocação) servem para estimar o impacto da LICC como ela
está, com que requisitos de dados, com que poder estatístico e com que
inferência, dado que (i) a unidade natural de comparação agregada são os 78
municípios do ES (licc-gov/README-licc.md, linha 49; lista oficial do IBGE em
`dados/externos/ibge_municipios_es.csv`), (ii) a habilitação é decidida sem
nota numérica publicada (IN SECULT 001/2025, arts. 39-42, em
`notas/politica/fontes/in-licc-001-2025.md`) e (iii) quem recebe o recurso
entre os habilitados é decidido pelos patrocinadores, sob um teto anual
vinculante (em 2025 os 63 captadores somaram R$ 25.000.000,00, o teto
inteiro; licc-gov/CLAUDE-licc.md, linhas 343-358).

**Estratégia.** Busca dirigida (não sistemática, sem PRISMA): o escopo foi
fixado pela tarefa (lista de trabalhos-âncora) e ampliado por "bola de neve"
para trás e para frente nos surveys (Roth *et al.*, 2023; de Chaisemartin;
D'Haultfœuille, 2023; Abadie, 2021; MacKinnon; Nielsen; Webb, 2023) e por
consulta bibliográfica no Crossref/OpenAlex para temas sem âncora (poder com
adoção escalonada; transbordamentos espaciais). Critério de inclusão:
trabalho metodológico publicado em periódico revisado por pares ou livro de
editora acadêmica, ou *working paper*/preprint de referência quando ainda não
publicado (marcado como tal). Material da disciplina é a espinha: Gertler
*et al.* (2018), slides PECO e 3ie WP 26 — já sintetizados em
`notas/disciplina/01-slides-e-guias.md`, `03-gertler.md` e
`04-itau-magenta-adb.md`; esta nota não os repete, remete a eles.

**Verificação.** Scripts auxiliares (fora do projeto, no *scratchpad* da
sessão) consultaram o Crossref por DOI e o OpenAlex para resumos. Resultado:
64 DOIs consultados; 63 resolveram com metadados coerentes; 1 DOI que eu
tinha de memória para Schochet (2022) estava **errado** (HTTP 404) e foi
substituído pelo DOI encontrado por busca bibliográfica no Crossref
(10.3102/10769986211070625) — exemplo concreto de por que nenhuma referência
entra sem conferência. Dois preprints (Butts; Callaway, Goodman-Bacon e
Sant'Anna) foram conferidos na API do arXiv.

**Grau de evidência (source_quality_hierarchy.md).** Para esta nota, o
"padrão-ouro do campo" é o artigo metodológico em periódico de econometria
revisado por pares (Grau A em *Evidence Level*). *Working papers* e preprints
recebem no máximo B em *Peer Review* e são usados como apoio, não como base
única de uma recomendação.

## 1. Referências anotadas — métodos

Formato: referência ABNT (NBR 6023) + DOI + `[VERIFICADO]`; depois, o que o
trabalho faz e **o que muda para a LICC**.

### 1.1 DiD com adoção escalonada e efeitos heterogêneos

Por que importa: se a unidade de análise for o município (ou o proponente) e
o "tratamento" for receber o primeiro projeto LICC, a adoção é **escalonada**
por ciclo (2022 a 2026). Com efeitos heterogêneos entre coortes e no tempo, a
regressão de efeitos fixos de duas vias (TWFE) deixa de estimar uma média
interpretável. A seção 3 mostra, com os dados da LICC, que isso não é
hipótese remota.

**GOODMAN-BACON, Andrew.** Difference-in-differences with variation in
treatment timing. **Journal of Econometrics**, v. 225, n. 2, p. 254-277,
2021. DOI: 10.1016/j.jeconom.2021.03.014. `[VERIFICADO]`
- Decompõe o estimador TWFE com adoção escalonada em média ponderada de
  todos os DiD 2×2 possíveis entre coortes, inclusive comparações que usam
  unidades **já tratadas** como controle. Quando o efeito varia no tempo,
  essas comparações contaminam o estimador; os pesos dependem do tamanho das
  coortes e da variância do tratamento no painel.
- LICC: é o diagnóstico a rodar primeiro em qualquer TWFE municipal. Com 39
  dos 78 municípios já presentes no ciclo 2022 (seção 3), muitas comparações
  2×2 usariam municípios tratados desde 2022 como "controle" das coortes
  seguintes.

**CALLAWAY, Brantly; SANT'ANNA, Pedro H. C.** Difference-in-differences with
multiple time periods. **Journal of Econometrics**, v. 225, n. 2, p.
200-230, 2021. DOI: 10.1016/j.jeconom.2020.12.001. `[VERIFICADO]`
- Define o efeito médio por coorte e período, ATT(g,t), identificado sob
  tendências paralelas (possivelmente condicionais a covariáveis) usando como
  comparação os **nunca tratados** ou os **ainda não tratados**; agrega os
  ATT(g,t) em estudo de evento, por coorte ou por calendário; estima por
  regressão, ponderação pelo escore de propensão ou forma duplamente robusta
  (Sant'Anna; Zhao, 2020), com *bootstrap* multiplicador e bandas
  simultâneas.
- LICC: é o estimador-base recomendado (seção 3). A escolha do grupo de
  comparação não é detalhe: só 14 municípios nunca aparecem como local de
  projeto habilitado em 2022-2026 (seção 3), e eles são justamente os menos
  parecidos com os tratados em porte e oferta cultural — o "ainda não
  tratado" tende a ser a comparação mais crível, e a condição de tendências
  paralelas deve ser condicional a porte/população.

**SUN, Liyang; ABRAHAM, Sarah.** Estimating dynamic treatment effects in
event studies with heterogeneous treatment effects. **Journal of
Econometrics**, v. 225, n. 2, p. 175-199, 2021. DOI:
10.1016/j.jeconom.2020.09.006. `[VERIFICADO]`
- Mostra que, no estudo de evento com defasagens e antecipações em TWFE, o
  coeficiente de cada período relativo pode carregar efeitos de outros
  períodos quando há heterogeneidade entre coortes — o que também contamina
  o teste de pré-tendência; propõe o estimador "ponderado por interação"
  (IW), que usa uma coorte nunca tratada ou a última tratada como controle.
- LICC: o gráfico de estudo de evento (efeito por ano desde o primeiro
  projeto) é a peça visual natural do artigo; deve ser feito com IW ou
  Callaway-Sant'Anna, não com TWFE dinâmico.

**DE CHAISEMARTIN, Clément; D'HAULTFŒUILLE, Xavier.** Two-way fixed effects
estimators with heterogeneous treatment effects. **American Economic
Review**, v. 110, n. 9, p. 2964-2996, 2020. DOI: 10.1257/aer.20181169.
`[VERIFICADO]`
- Mostra (resumo oficial) que a regressão com efeitos fixos de grupo e
  período estima soma ponderada dos efeitos por grupo e período com pesos
  que **podem ser negativos** — o coeficiente pode ser negativo com todos os
  efeitos positivos — e propõe estimador alternativo que compara, a cada
  período, unidades que mudam de status com unidades de status estável.
- LICC: é o único dos quatro estimadores-âncora pensado para tratamento que
  **liga e desliga**. No município, "ter projeto LICC no ciclo" não é
  absorvente: um município pode ter projeto em 2022 e não em 2024 (o número
  de municípios com projeto habilitado oscila entre 31 e 44 por ciclo; seção
  3). Se o tratamento for definido por ciclo (e não "desde o primeiro
  projeto"), este é o estimador indicado.

**DE CHAISEMARTIN, Clément; D'HAULTFŒUILLE, Xavier.** Two-way fixed effects
and differences-in-differences with heterogeneous treatment effects: a
survey. **The Econometrics Journal**, v. 26, n. 3, p. C1-C30, 2023. DOI:
10.1093/ectj/utac017. `[VERIFICADO]`
- Survey dos problemas do TWFE com efeitos heterogêneos e dos estimadores
  robustos (resumo oficial: 26 dos 100 artigos mais citados da AER de 2015 a
  2019 usam essas regressões). Útil como referência única para justificar,
  no artigo, por que não se usa TWFE simples.

**BORUSYAK, Kirill; JARAVEL, Xavier; SPIESS, Jann.** Revisiting event-study
designs: robust and efficient estimation. **The Review of Economic
Studies**, v. 91, n. 6, p. 3253-3285, 2024. DOI: 10.1093/restud/rdae007.
`[VERIFICADO]`
- Deriva o estimador eficiente para adoção escalonada com efeitos
  heterogêneos, que toma a forma de **imputação**: estima o contrafactual
  Y(0) só com observações não tratadas e compara com o observado nas
  tratadas; separa estimação e teste das hipóteses de identificação; aceita
  covariáveis variáveis no tempo e triplas diferenças (resumo oficial).
- LICC: alternativa ao Callaway-Sant'Anna quando se quer usar todas as
  observações pré-tratamento de todos os municípios (ganho de precisão, que
  importa com N = 78). A tripla diferença permitida pelo método é útil para
  comparar setores culturais × não culturais dentro do município (seção 3).

**ROTH, Jonathan; SANT'ANNA, Pedro H. C.; BILINSKI, Alyssa; POE, John.**
What's trending in difference-in-differences? A synthesis of the recent
econometrics literature. **Journal of Econometrics**, v. 235, n. 2, p.
2218-2244, 2023. DOI: 10.1016/j.jeconom.2023.03.008. `[VERIFICADO]`
- Síntese organizada em três afastamentos do DiD canônico 2×2: múltiplos
  períodos e adoção escalonada; violações de tendências paralelas
  (condicionais, sensibilidade); e inferência/amostragem alternativas
  (poucos clusters, visão baseada no desenho). Termina com recomendações
  práticas. [VERIFICAR a lista exata de recomendações no texto integral antes
  de citá-la item a item.]
- LICC: é a referência-guarda-chuva para a seção de método do artigo.

**RAMBACHAN, Ashesh; ROTH, Jonathan.** A more credible approach to parallel
trends. **The Review of Economic Studies**, v. 90, n. 5, p. 2555-2591, 2023.
DOI: 10.1093/restud/rdad018. `[VERIFICADO]`
- Em vez de exigir tendências paralelas exatas, restringe o quanto a
  violação pós-tratamento pode diferir da pré-tendência observada e obtém
  identificação parcial com inferência uniforme (resumo oficial); serve como
  análise de sensibilidade.
- LICC: com apenas 2-3 anos pré-2022 de algumas fontes municipais e
  pré-tendências estimadas com pouca precisão (N = 78), a sensibilidade de
  Rambachan-Roth é mais honesta do que "não rejeitamos a pré-tendência".

**CALLAWAY, Brantly; GOODMAN-BACON, Andrew; SANT'ANNA, Pedro H. C.**
Difference-in-differences with a continuous treatment. Cambridge, MA:
National Bureau of Economic Research, 2024. (NBER Working Paper, 32117). DOI:
10.3386/w32117. Versão em preprint: arXiv:2107.02637 (v8, 31 dez. 2025).
`[VERIFICADO]` (*working paper*; não publicado em periódico até a consulta)
- Com tratamento contínuo (dose), parâmetros do tipo ATT por dose são
  identificados sob tendências paralelas generalizadas, mas **comparar doses**
  exige hipótese mais forte, porque tendências paralelas não afastam viés de
  seleção entre doses; o TWFE com dose linear é de difícil interpretação
  (resumo oficial).
- LICC: se o tratamento municipal for **intensidade** (R$ captados per
  capita), a pergunta "o efeito cresce com o valor?" exige essa hipótese mais
  forte. E há um obstáculo de dados anterior: a SECULT não publica o rateio
  do valor entre municípios em projetos com vários locais (100 dos 467
  registros; seção 3), então a dose municipal não é observável sem supor
  rateio — o que as regras do projeto proíbem fazer em silêncio.

**ATHEY, Susan; IMBENS, Guido W.** Design-based analysis in
difference-in-differences settings with staggered adoption. **Journal of
Econometrics**, v. 226, n. 1, p. 62-79, 2022. DOI:
10.1016/j.jeconom.2020.10.012. `[VERIFICADO]`
- Perspectiva baseada no desenho: se a **data de adoção** for aleatória, o
  DiD padrão é não viesado para uma média ponderada de efeitos causais, e o
  estimador usual de variância é conservador (resumo oficial).
- LICC: os 78 municípios são a **população**, não uma amostra; a incerteza
  relevante é a da atribuição, não a de amostragem — argumento para
  complementar erros-padrão por cluster com inferência por aleatorização
  (seção 1.7).

**SANT'ANNA, Pedro H. C.; ZHAO, Jun.** Doubly robust difference-in-differences
estimators. **Journal of Econometrics**, v. 219, n. 1, p. 101-122, 2020. DOI:
10.1016/j.jeconom.2020.06.003. `[VERIFICADO]`
- Estimador de DiD que combina modelo de resultado e escore de propensão e é
  consistente se um dos dois estiver correto. É o motor do
  Callaway-Sant'Anna com covariáveis e a forma recomendada de "DiD com
  pareamento" (seção 1.4).

**BAKER, Andrew C.; LARCKER, David F.; WANG, Charles C. Y.** How much should
we trust staggered difference-in-differences estimates? **Journal of
Financial Economics**, v. 144, n. 2, p. 370-395, 2022. DOI:
10.1016/j.jfineco.2022.01.004. `[VERIFICADO]`
- Explica quando o DiD escalonado por regressão é viesado, resume três
  estimadores alternativos e reestima resultados publicados, que mudam
  substancialmente em vários casos (resumo oficial). Leitura de apoio,
  didática.

### 1.2 Controle sintético e DiD sintético

Por que importa: a pergunta agregada "a LICC mudou o setor cultural do ES?"
tem **uma** unidade tratada (o estado, a partir de 2022) e 26 UFs
candidatas a doadoras — o caso típico do controle sintético.

**ABADIE, Alberto; GARDEAZABAL, Javier.** The economic costs of conflict: a
case study of the Basque Country. **American Economic Review**, v. 93, n. 1,
p. 113-132, 2003. DOI: 10.1257/000282803321455188. `[VERIFICADO]`
- Trabalho de origem: compara o PIB per capita do País Basco com uma região
  de controle sintético sem terrorismo (resumo oficial).

**ABADIE, Alberto; DIAMOND, Alexis; HAINMUELLER, Jens.** Synthetic control
methods for comparative case studies: estimating the effect of California's
tobacco control program. **Journal of the American Statistical
Association**, v. 105, n. 490, p. 493-505, 2010. DOI:
10.1198/jasa.2009.ap08746. `[VERIFICADO]`
- Formaliza o método (combinação ponderada de unidades doadoras que
  reproduz a trajetória pré-intervenção do tratado) e propõe inferência por
  placebos; o resumo oficial destaca a aplicabilidade a intervenções em
  **unidades agregadas** (países, regiões, cidades) com poucas unidades
  afetadas.
- LICC: ES × combinação de UFs, com desfecho anual de emprego formal
  cultural (RAIS) ou despesa cultural (SICONFI). Condição crítica: doadoras
  **sem** política semelhante no período — ver Abadie (2021) abaixo.

**ABADIE, Alberto; DIAMOND, Alexis; HAINMUELLER, Jens.** Comparative politics
and the synthetic control method. **American Journal of Political Science**,
v. 59, n. 2, p. 495-510, 2015. DOI: 10.1111/ajps.12116. `[VERIFICADO]`
- Apresenta o controle sintético como ponte entre abordagens qualitativa e
  quantitativa em estudos comparativos com amostra pequena (reunificação
  alemã). Útil para justificar a escolha transparente das doadoras.

**ABADIE, Alberto.** Using synthetic controls: feasibility, data
requirements, and methodological aspects. **Journal of Economic
Literature**, v. 59, n. 2, p. 391-425, 2021. DOI: 10.1257/jel.20191450.
`[VERIFICADO]`
- Guia prático: vantagens do desenho, **em que contextos** o método dá
  estimativas confiáveis e em quais pode falhar, extensões (resumo oficial).
  Os requisitos discutidos incluem, entre outros, efeito grande em relação à
  volatilidade do desfecho, doadoras não expostas a intervenções
  semelhantes, ausência de antecipação e de interferência, e período
  pré-intervenção suficientemente longo. [VERIFICAR no texto integral a
  lista e a numeração exatas antes de citar item a item.]
- LICC: três ameaças concretas. (a) **Doadoras contaminadas**: outras UFs
  têm leis estaduais de incentivo à cultura via ICMS [VERIFICAR quais e
  desde quando — levantamento não feito nesta nota]; (b) **efeito pequeno
  diante da volatilidade**: a renúncia de R$ 25 mi/ano (licc-gov/CLAUDE-licc.md)
  é pequena diante do emprego cultural do estado inteiro [VERIFICAR com a
  RAIS], o que torna o efeito agregado difícil de separar do ruído; (c)
  **choques simultâneos**: 2021-2023 coincidem com a retomada pós-pandemia e
  com transferências federais à cultura para estados e municípios (Lei Paulo
  Gustavo, Política Nacional Aldir Blanc) [VERIFICAR normas e datas], que
  atingem todas as UFs, mas com intensidades diferentes.

**BEN-MICHAEL, Eli; FELLER, Avi; ROTHSTEIN, Jesse.** The augmented synthetic
control method. **Journal of the American Statistical Association**, v.
116, n. 536, p. 1789-1803, 2021. DOI: 10.1080/01621459.2021.1929245.
`[VERIFICADO]`
- Para quando o ajuste pré-tratamento é imperfeito: usa modelo de resultado
  (ridge) para estimar e remover o viés do controle sintético (resumo
  oficial). LICC: provável necessidade, porque o ES pode ficar fora do
  "casco convexo" das UFs em algum indicador cultural.

**ARKHANGELSKY, Dmitry; ATHEY, Susan; HIRSHBERG, David A.; IMBENS, Guido W.;
WAGER, Stefan.** Synthetic difference-in-differences. **American Economic
Review**, v. 111, n. 12, p. 4088-4118, 2021. DOI: 10.1257/aer.20190159.
`[VERIFICADO]`
- Estimador que combina DiD e controle sintético (pesos para unidades e para
  períodos), com propriedades de robustez teóricas e empíricas sob modelo de
  fatores latentes (resumo oficial).
- LICC: é a versão recomendada para ES × UFs (menos dependente de ajuste
  perfeito que o controle sintético puro e menos dependente de tendências
  paralelas que o DiD). Também serve no nível municipal, comparando
  municípios tratados a um conjunto ponderado de não tratados. Com uma única
  unidade tratada, a inferência precisa ser por placebo [VERIFICAR no texto
  as condições dos métodos de variância propostos].

### 1.3 Regressão descontínua

Por que importa: a tarefa pede avaliar se há nota de corte na habilitação.
Pelas normas lidas, **não há** índice contínuo publicado; o limiar que
existe (35% de patrocínio comprometido) é manipulável.

**LEE, David S.; LEMIEUX, Thomas.** Regression discontinuity designs in
economics. **Journal of Economic Literature**, v. 48, n. 2, p. 281-355,
2010. DOI: 10.1257/jel.48.2.281. `[VERIFICADO]`
- Guia do RD para empiristas: teoria, **quando o RD é válido ou inválido
  dado os incentivos econômicos** dos agentes em torno do corte, por que é
  "quase-experimental", formas de estimação e limites de interpretação
  (resumo oficial).
- LICC: o critério de incentivos é o que desqualifica o limiar de 35% (IN
  001/2025, arts. 41, 46 e 47): proponentes e patrocinadores escolhem o
  percentual comprometido **justamente** para cruzá-lo.

**IMBENS, Guido W.; LEMIEUX, Thomas.** Regression discontinuity designs: a
guide to practice. **Journal of Econometrics**, v. 142, n. 2, p. 615-635,
2008. DOI: 10.1016/j.jeconom.2007.05.001. `[VERIFICADO]`
- Guia prático (RD nítido e difuso, regressão local, escolha de janela).

**CATTANEO, Matias D.; IDROBO, Nicolás; TITIUNIK, Rocío.** A practical
introduction to regression discontinuity designs: foundations. Cambridge:
Cambridge University Press, 2019. (Elements in Quantitative and
Computational Methods for the Social Sciences). DOI: 10.1017/9781108684606.
`[VERIFICADO]` (Crossref: publicação *online* 16/11/2019; ano de capa
frequentemente citado como 2020 — [VERIFICAR] qual ano usar.)
- RD nítido canônico: escore contínuo, um corte, cumprimento perfeito
  (resumo oficial); estimação por polinômio local, inferência robusta e
  testes de falsificação.

**CATTANEO, Matias D.; IDROBO, Nicolás; TITIUNIK, Rocío.** A practical
introduction to regression discontinuity designs: extensions. Cambridge:
Cambridge University Press, 2024. (Elements in Quantitative and
Computational Methods for the Social Sciences). DOI: 10.1017/9781009441896.
`[VERIFICADO]`
- Extensões: randomização local, RD difuso, **escores discretos** e RD
  **multidimensional** (inclusive geográfico) (resumo oficial).
- LICC: (a) se a SECULT tiver nota de parecer com corte, provavelmente será
  escore discreto (notas inteiras) — capítulo relevante; (b) a cota de 10%
  "fora da RMGV" (IN, art. 18, III) sugere RD geográfico na fronteira
  metropolitana, mas a unidade seria o município (poucos municípios na
  fronteira) e outras políticas mudam na mesma fronteira — descartado como
  desenho principal (ver também `notas/disciplina/03-gertler.md`, 11.3).

**CALONICO, Sebastian; CATTANEO, Matias D.; TITIUNIK, Rocío.** Robust
nonparametric confidence intervals for regression-discontinuity designs.
**Econometrica**, v. 82, n. 6, p. 2295-2326, 2014. DOI:
10.3982/ECTA11757. `[VERIFICADO]`
- Intervalos de confiança com correção de viés e erro-padrão robusto, porque
  as janelas "ótimas" por EQM geram cobertura abaixo da nominal (resumo
  oficial). Padrão atual de inferência em RD (pacote `rdrobust`).

**McCRARY, Justin.** Manipulation of the running variable in the regression
discontinuity design: a density test. **Journal of Econometrics**, v. 142,
n. 2, p. 698-714, 2008. DOI: 10.1016/j.jeconom.2007.05.005. `[VERIFICADO]`

**CATTANEO, Matias D.; JANSSON, Michael; MA, Xinwei.** Simple local
polynomial density estimators. **Journal of the American Statistical
Association**, v. 115, n. 531, p. 1449-1455, 2020. DOI:
10.1080/01621459.2019.1635480. `[VERIFICADO]`
- Os dois trabalhos dão o teste de descontinuidade da densidade do escore no
  corte (manipulação). LICC: se a SECULT fornecer o percentual de patrocínio
  comprometido por projeto (hoje **ausente** dos anexos), o teste de
  densidade em 35% documentaria o amontoamento esperado — resultado
  descritivo útil sobre o desenho, não estimativa de impacto.

### 1.4 Pareamento (PSM) e DiD com pareamento

**ROSENBAUM, Paul R.; RUBIN, Donald B.** The central role of the propensity
score in observational studies for causal effects. **Biometrika**, v. 70,
n. 1, p. 41-55, 1983. DOI: 10.1093/biomet/70.1.41. `[VERIFICADO]`
- Define o escore de propensão e mostra que ajustar por ele basta para
  remover o viés devido às covariáveis **observadas** (resumo oficial).

**HECKMAN, James J.; ICHIMURA, Hidehiko; TODD, Petra E.** Matching as an
econometric evaluation estimator: evidence from evaluating a job training
programme. **The Review of Economic Studies**, v. 64, n. 4, p. 605-654,
1997. DOI: 10.2307/2971733. `[VERIFICADO]`
- Contra um *benchmark* experimental, o pareamento elimina boa parte do viés
  quando os comparáveis estão **no mesmo mercado de trabalho local** e
  respondem ao **mesmo questionário**; o viés por não observáveis é menor
  que outros componentes, mas ainda é fração considerável do impacto
  (resumo oficial). O trabalho também desenvolve a versão de pareamento em
  diferenças [VERIFICAR a seção antes de citar esse ponto].
- LICC: argumento direto para parear **dentro do ES** (mesmo mercado local)
  e com a **mesma fonte de dados** (ex.: RAIS para tratados e comparáveis).

**SMITH, Jeffrey A.; TODD, Petra E.** Does matching overcome LaLonde's
critique of nonexperimental estimators? **Journal of Econometrics**, v. 125,
n. 1-2, p. 305-353, 2005. DOI: 10.1016/j.jeconom.2004.04.011.
`[VERIFICADO]`
- Reexamina os dados do NSW; conclusão amplamente citada de que o
  pareamento em diferenças (DiD com pareamento) se sai melhor que o
  pareamento transversal [VERIFICAR a formulação exata no texto].

**IMBENS, Guido W.** Nonparametric estimation of average treatment effects
under exogeneity: a review. **The Review of Economics and Statistics**, v.
86, n. 1, p. 4-29, 2004. DOI: 10.1162/003465304323023651. `[VERIFICADO]`

**ABADIE, Alberto; IMBENS, Guido W.** Large sample properties of matching
estimators for average treatment effects. **Econometrica**, v. 74, n. 1, p.
235-267, 2006. DOI: 10.1111/j.1468-0262.2006.00655.x. `[VERIFICADO]`
- Imbens (2004) revisa os estimadores sob não confundimento; Abadie e Imbens
  (2006) mostram que o pareamento com número fixo de vizinhos não é, em
  geral, √N-consistente nem eficiente (resumo oficial) — razão para usar
  correção de viés ou estimadores duplamente robustos.

**CALIENDO, Marco; KOPEINIG, Sabine.** Some practical guidance for the
implementation of propensity score matching. **Journal of Economic
Surveys**, v. 22, n. 1, p. 31-72, 2008. DOI:
10.1111/j.1467-6419.2007.00527.x. `[VERIFICADO]`
- Roteiro de implementação: estimação do escore, algoritmo, suporte comum,
  qualidade do pareamento, erros-padrão e sensibilidade (resumo oficial).

**Síntese para a LICC.** PSM isolado não serve: a seleção pelos
patrocinadores é por características não observadas (visibilidade, rede,
afinidade de marca) — `notas/disciplina/03-gertler.md`, 11.3, com Gertler
*et al.* (2018, p. 168-169). DiD com pareamento (ou DR-DiD de Sant'Anna e
Zhao, 2020) serve como refinamento, pareando por características **pré**
que determinam a captação: ciclo, cota do art. 18, valor autorizado,
RMGV × interior, histórico e porte do proponente.

### 1.5 Experimentos e desenhos de encorajamento

**DUFLO, Esther; GLENNERSTER, Rachel; KREMER, Michael.** Using randomization
in development economics research: a toolkit. In: SCHULTZ, T. Paul; STRAUSS,
John A. (ed.). **Handbook of Development Economics**. Amsterdam: Elsevier,
2007. v. 4, cap. 61, p. 3895-3962. DOI: 10.1016/S1573-4471(07)04061-2.
`[VERIFICADO]` (metadados do capítulo no Crossref; editores e volume
conferidos pelo DOI da série — [VERIFICAR] nomes dos editores na folha de
rosto antes da versão final.)
- Manual de desenho experimental em campo: formas de introduzir aleatorização
  sem negar o programa (sorteio em excesso de demanda, entrada em fases,
  **desenho de encorajamento**), cálculo de poder com conglomerados,
  estratificação, transbordamentos, cumprimento parcial e atrito.
- LICC: sustenta a proposta, já esboçada em `notas/disciplina/03-gertler.md`
  (11.3), de **encorajamento aleatório à captação** entre habilitados de um
  ciclo (ex.: rodadas de apresentação a contribuintes de ICMS), que não
  altera a regra de alocação. Ressalva estrutural: com teto vinculante, o
  encorajado pode captar **no lugar** de outro habilitado (violação da SUTVA
  entre projetos; seção 1.8).

**IMBENS, Guido W.; ANGRIST, Joshua D.** Identification and estimation of
local average treatment effects. **Econometrica**, v. 62, n. 2, p. 467-475,
1994. DOI: 10.2307/2951620. `[VERIFICADO]` (Crossref registra só a página
inicial; intervalo 467-475 [VERIFICAR] no JSTOR.)

**ANGRIST, Joshua D.; IMBENS, Guido W.; RUBIN, Donald B.** Identification of
causal effects using instrumental variables. **Journal of the American
Statistical Association**, v. 91, n. 434, p. 444-455, 1996. DOI:
10.1080/01621459.1996.10476902. `[VERIFICADO]`
- Com atribuição aleatória e cumprimento imperfeito, o estimador de VI
  identifica o efeito médio para os **cumpridores** (LATE), sob hipóteses
  explícitas (resumo oficial). LICC: o encorajamento identifica o efeito da
  captação para os projetos "na margem" — os que captam só se encorajados.

**HUSSEY, Michael A.; HUGHES, James P.** Design and analysis of stepped wedge
cluster randomized trials. **Contemporary Clinical Trials**, v. 28, n. 2, p.
182-191, 2007. DOI: 10.1016/j.cct.2006.05.007. `[VERIFICADO]`

**XIONG, Ruoxuan; ATHEY, Susan; BAYATI, Mohsen; IMBENS, Guido.** Optimal
experimental design for staggered rollouts. **Management Science**, v. 70, n.
8, p. 5317-5336, 2024. DOI: 10.1287/mnsc.2023.4928. `[VERIFICADO]`
- Hussey e Hughes (2007) formalizam o ensaio em "cunha escalonada" (os
  conglomerados passam do controle ao tratamento em datas sorteadas);
  Xiong *et al.* (2024) mostram que, no desenho não adaptativo ótimo, a
  fração que entra a cada período é baixa, depois alta, depois baixa (resumo
  oficial). LICC: se a SECULT expandir alguma **ação de apoio** (oficinas de
  elaboração de projetos, busca ativa de patrocinadores) a municípios sem
  histórico de projetos, a ordem de entrada pode ser sorteada — sem mexer no
  mecanismo de renúncia (fora do escopo).

### 1.6 Poder estatístico e MDE em painel/DiD

(Fórmulas e replicações numéricas já estão em `analise/05_poder_mde.py`,
`analise/gertler_poder_replicacao.py` e na nota da disciplina; aqui só a
literatura.)

**BLOOM, Howard S.** Minimum detectable effects: a simple way to report the
statistical power of experimental designs. **Evaluation Review**, v. 19, n.
5, p. 547-556, 1995. DOI: 10.1177/0193841X9501900504. `[VERIFICADO]`
(Crossref registra o título curto "Minimum Detectable Effects"; o subtítulo
[VERIFICAR] na página do artigo.)
- Define o efeito mínimo detectável (MDE) como o menor efeito verdadeiro que
  o desenho tem boa chance de detectar, para desfechos contínuos e binários
  (resumo oficial). É a forma de reportar poder adotada no artigo.

**DJIMEU, Eric W.; HOUNDOLO, Deo-Gracias.** Power calculation for causal
inference in social science: sample size and minimum detectable effect
determination. **Journal of Development Effectiveness**, v. 8, n. 4, p.
508-527, 2016. DOI: 10.1080/19439342.2016.1244555. `[VERIFICADO]`
- Versão publicada do 3ie Working Paper 26 (PDF da disciplina,
  `wp26-power-calculation.pdf`): fórmulas de tamanho amostral e MDE para
  aleatorização individual e por conglomerados, regras de bolso e
  calculadora (resumo oficial). [VERIFICAR] se o artigo e o WP têm a mesma
  numeração de fórmulas — o script `05_poder_mde.py` cita as páginas do WP.

**McKENZIE, David.** Beyond baseline and follow-up: the case for more T in
experiments. **Journal of Development Economics**, v. 99, n. 2, p. 210-221,
2012. DOI: 10.1016/j.jdeveco.2012.01.002. `[VERIFICADO]`
- Mostra que, com desfechos de baixa autocorrelação, mais rodadas antes e
  depois aumentam o poder, e que ANCOVA é mais poderosa que DiD (fórmulas de
  variância usadas em `analise/05_poder_mde.py`, eq. 7, 8 e 11 da versão WPS
  5639).
- LICC: dados administrativos anuais (RAIS, SICONFI) dão "T grande" de
  graça — vários anos pré-2022 —, o que é a principal fonte de poder num
  painel de só 78 municípios.

**BURLIG, Fiona; PREONAS, Louis; WOERMAN, Matt.** Panel data and experimental
design. **Journal of Development Economics**, v. 144, artigo 102458, 2020.
DOI: 10.1016/j.jdeveco.2020.102458. `[VERIFICADO]`
- Mostra que as fórmulas de poder em painel que ignoram correlação serial
  arbitrária erram o tamanho do teste e o poder, e deriva fórmula robusta à
  correlação serial, com abordagem por simulação (usada em
  `analise/05_poder_mde.py`, eq. 2 e 3 da versão NBER WP 26250).
- LICC: emprego cultural municipal é serialmente correlacionado; a
  recomendação é calibrar o poder **por simulação** nos dados pré-2022 da
  própria RAIS (placebos com datas falsas), não por fórmula fechada.

**SCHOCHET, Peter Z.** Statistical power for estimating treatment effects
using difference-in-differences and comparative interrupted time series
estimators with variation in treatment timing. **Journal of Educational and
Behavioral Statistics**, v. 47, n. 4, p. 367-405, 2022. DOI:
10.3102/10769986211070625. `[VERIFICADO]`
- Fórmulas de variância fechadas para poder de DiD e séries temporais
  interrompidas comparativas **com variação na data de tratamento**,
  erros autocorrelacionados e conglomerados; achado-chave: considerar a
  variação de datas **aumenta** o tamanho amostral necessário, e DiD tem
  bem mais poder que CITS/ITS (resumo oficial); há painel Shiny em R.
- LICC: é a referência mais próxima do desenho recomendado (DiD escalonado
  municipal) para o cálculo de poder do artigo.

**RAUDENBUSH, Stephen W.** Statistical analysis and optimal design for
cluster randomized trials. **Psychological Methods**, v. 2, n. 2, p.
173-185, 1997. DOI: 10.1037/1082-989X.2.2.173. `[VERIFICADO]`
- Referência clássica de desenho ótimo com conglomerados e ganho de poder
  por covariável no nível do conglomerado. [VERIFICAR conteúdo no texto
  integral; resumo não disponível no OpenAlex.]

**GELMAN, Andrew; CARLIN, John.** Beyond power calculations: assessing type S
(sign) and type M (magnitude) errors. **Perspectives on Psychological
Science**, v. 9, n. 6, p. 641-651, 2014. DOI: 10.1177/1745691614551642.
`[VERIFICADO]` (Crossref registra o título curto "Beyond Power
Calculations"; subtítulo [VERIFICAR].)
- Em estudos pequenos e ruidosos, resultados significativos podem ter sinal
  errado (erro tipo S) e magnitude exagerada (tipo M) (resumo oficial).
  LICC: com poder baixo em subgrupos (ex.: cotas do art. 18), qualquer
  efeito "significativo" deve vir com a razão de exagero
  (`analise/tabelas/05_poder_tipo_m.csv`).

### 1.7 Inferência com poucos clusters

Por que importa: com o município como unidade de tratamento há no máximo 78
clusters, de tamanhos muito desiguais (capital × municípios pequenos), e
algumas coortes de adoção têm **3 ou 4** municípios novos (seção 3). O
problema não é só "poucos clusters", é "poucos clusters **tratados**" por
coorte.

**BERTRAND, Marianne; DUFLO, Esther; MULLAINATHAN, Sendhil.** How much should
we trust differences-in-differences estimates? **The Quarterly Journal of
Economics**, v. 119, n. 1, p. 249-275, 2004. DOI:
10.1162/003355304772839588. `[VERIFICADO]`
- Com desfechos serialmente correlacionados e muitos anos, os erros-padrão
  convencionais do DiD subestimam muito a variabilidade: leis-placebo saem
  "significativas" a 5% em até 45% das vezes (resumo oficial).

**CAMERON, A. Colin; GELBACH, Jonah B.; MILLER, Douglas L.** Bootstrap-based
improvements for inference with clustered errors. **The Review of Economics
and Statistics**, v. 90, n. 3, p. 414-427, 2008. DOI:
10.1162/rest.90.3.414. `[VERIFICADO]`
- Com poucos clusters (5 a 30), testes com erro-padrão por cluster
  rejeitam demais; *bootstrap-t* por cluster (incluindo o *wild cluster
  bootstrap*) traz a rejeição de 10% para os 5% nominais (resumo oficial).

**CAMERON, A. Colin; MILLER, Douglas L.** A practitioner's guide to
cluster-robust inference. **Journal of Human Resources**, v. 50, n. 2, p.
317-372, 2015. DOI: 10.3368/jhr.50.2.317. `[VERIFICADO]`

**MACKINNON, James G.; WEBB, Matthew D.** Wild bootstrap inference for wildly
different cluster sizes. **Journal of Applied Econometrics**, v. 32, n. 2,
p. 233-254, 2017. DOI: 10.1002/jae.2508. `[VERIFICADO]`
- A "regra de 42" clusters não vale com clusters desbalanceados; o *wild
  cluster bootstrap* vai bem melhor, mas **falha quando poucos clusters são
  tratados**; discute o "número efetivo" de clusters (resumo oficial).
- LICC: exatamente o caso — municípios de tamanhos muito diferentes.

**MACKINNON, James G.; WEBB, Matthew D.** The wild bootstrap for few (treated)
clusters. **The Econometrics Journal**, v. 21, n. 2, p. 114-135, 2018. DOI:
10.1111/ectj.12107. `[VERIFICADO]`
- Propõe o *subcluster wild bootstrap*; o resumo adverte que a condição que o
  faz funcionar (clusters de tamanhos parecidos) **dificilmente vale em
  regressões de DiD**.

**MACKINNON, James G.; WEBB, Matthew D.** Randomization inference for
difference-in-differences with few treated clusters. **Journal of
Econometrics**, v. 218, n. 2, p. 435-450, 2020. DOI:
10.1016/j.jeconom.2020.04.024. `[VERIFICADO]` (resumo não disponível no
OpenAlex; conteúdo além do título [VERIFICAR].)

**CONLEY, Timothy G.; TABER, Christopher R.** Inference with "difference in
differences" with a small number of policy changes. **The Review of
Economics and Statistics**, v. 93, n. 1, p. 113-125, 2011. DOI:
10.1162/REST_a_00049. `[VERIFICADO]`
- Poucos grupos mudam de política, muitos não mudam: usa os não mudantes
  para estimar a distribuição do erro e constrói intervalos por inversão de
  teste (resumo oficial). LICC: base para inferência no controle
  ES × UFs (1 tratado, 26 controles) em versão DiD.

**FERMAN, Bruno; PINTO, Cristine.** Inference in differences-in-differences
with few treated groups and heteroskedasticity. **The Review of Economics
and Statistics**, v. 101, n. 3, p. 452-467, 2019. DOI:
10.1162/rest_a_00759. `[VERIFICADO]`
- Estende a lógica de Conley-Taber para heteroscedasticidade gerada por
  **tamanhos de grupo diferentes**, que invalida métodos anteriores mesmo com
  muitas observações por grupo (resumo oficial). LICC: é a correção
  pertinente quando o tratado é o ES (ou poucos municípios) e os grupos têm
  populações muito distintas.

**ROODMAN, David; NIELSEN, Morten Ørregaard; MACKINNON, James G.; WEBB,
Matthew D.** Fast and wild: bootstrap inference in Stata using boottest.
**The Stata Journal**, v. 19, n. 1, p. 4-60, 2019. DOI:
10.1177/1536867X19830877. `[VERIFICADO]`

**MACKINNON, James G.; NIELSEN, Morten Ørregaard; WEBB, Matthew D.**
Cluster-robust inference: a guide to empirical practice. **Journal of
Econometrics**, v. 232, n. 2, p. 272-299, 2023. DOI:
10.1016/j.jeconom.2022.04.001. `[VERIFICADO]`

**MACKINNON, James G.; NIELSEN, Morten Ørregaard; WEBB, Matthew D.** Fast
and reliable jackknife and bootstrap methods for cluster-robust inference.
**Journal of Applied Econometrics**, v. 38, n. 5, p. 671-694, 2023. DOI:
10.1002/jae.2969. `[VERIFICADO]`
- Implementação (`boottest`), guia prático atual e variantes com
  estimador *jackknife* (CV3) que se saem melhor quando há poucos clusters
  e/ou tamanhos muito desiguais (resumos oficiais). LICC: reportar,
  lado a lado, erro-padrão por cluster CV1, CV3 e p-valor do *wild cluster
  bootstrap* com a hipótese nula imposta.

### 1.8 Transbordamentos (*spillovers*) entre municípios e entre projetos

Na LICC há três canais plausíveis de interferência (violação da SUTVA):
(i) **espacial** — público, artistas e fornecedores circulam entre
municípios vizinhos; (ii) **multilocal** — 100 dos 467 registros de
habilitados listam mais de um município de execução (seção 3); (iii)
**competição pelo teto** — com teto vinculante, a captação de um projeto
reduz a de outro (Gertler *et al.*, 2018, p. 181-187, via
`notas/disciplina/03-gertler.md`, 11.4), o que contamina a comparação
captou × não captou dentro do mesmo ciclo.

**MIGUEL, Edward; KREMER, Michael.** Worms: identifying impacts on education
and health in the presence of treatment externalities. **Econometrica**, v.
72, n. 1, p. 159-217, 2004. DOI: 10.1111/j.1468-0262.2004.00481.x.
`[VERIFICADO]`
- Aleatorização por escola (não por indivíduo) com entrada em fases permite
  estimar efeitos totais e externalidades sobre não tratados em escolas
  **vizinhas** (resumo oficial). É o exemplo canônico de que ignorar
  transbordamento subestima o efeito.

**BAIRD, Sarah; BOHREN, J. Aislinn; McINTOSH, Craig; ÖZLER, Berk.** Optimal
design of experiments in the presence of interference. **The Review of
Economics and Statistics**, v. 100, n. 5, p. 844-860, 2018. DOI:
10.1162/rest_a_00716. `[VERIFICADO]`
- Desenhos de "saturação aleatória" (sorteia a proporção tratada no grupo,
  depois quem é tratado) e o custo em poder de identificar efeitos de
  transbordamento (resumo oficial). LICC: relevante se o encorajamento
  (1.5) for sorteado por **ciclo/cota** com saturações diferentes, para
  medir o deslocamento entre projetos sob teto vinculante.

**HUBER, Martin; STEINMAYR, Andreas.** A framework for separating
individual-level treatment effects from spillover effects. **Journal of
Business & Economic Statistics**, v. 39, n. 2, p. 422-436, 2021. DOI:
10.1080/07350015.2019.1668795. `[VERIFICADO]`
- Relaxa a SUTVA permitindo transbordamentos dentro de agregados (regiões) e
  propõe DiD para separar efeito individual de efeito de equilíbrio geral
  (resumo oficial).

**DELGADO, Michael S.; FLORAX, Raymond J. G. M.** Difference-in-differences
techniques for spatial data: local autocorrelation and spatial interaction.
**Economics Letters**, v. 137, p. 123-126, 2015. DOI:
10.1016/j.econlet.2015.10.035. `[VERIFICADO]` (resumo indisponível;
conteúdo além do título [VERIFICAR].)

**BUTTS, Kyle.** Difference-in-differences estimation with spatial
spillovers. [S. l.]: arXiv, 2021. Preprint arXiv:2105.03737 (v3, 10 jun.
2023). DOI: 10.48550/arXiv.2105.03737. `[VERIFICADO]` (preprint, sem
publicação em periódico registrada no arXiv)
- Com efeitos que cruzam fronteiras, o DiD clássico é viesado por dois
  canais: o controle deixa de identificar a tendência contrafactual e o
  tratado absorve o efeito dos vizinhos tratados; propõe condições de
  identificação e estimação dos transbordamentos, inclusive com adoção
  escalonada (resumo no arXiv).
- LICC: justifica duas checagens — (a) excluir do grupo de comparação os
  municípios vizinhos de tratados, ou (b) modelar a exposição dos vizinhos
  (proporção de vizinhos com projeto) como tratamento adicional.

**DEBARSY, Nicolas; LE GALLO, Julie.** Identification of spatial spillovers:
do's and don'ts. **Journal of Economic Surveys**, v. 39, n. 5, p.
2152-2173, 2025. DOI: 10.1111/joes.12692. `[VERIFICADO]`
- Adverte contra usar matrizes de vizinhança puramente geográficas "no
  escuro" para identificar transbordamentos e dá recomendações para modelos
  de avaliação com dados espaciais (resumo oficial). LICC: a definição de
  "vizinho" deve seguir o canal (deslocamento de público, região de
  planejamento, microrregião), não só a contiguidade.

**Leitura transversal de apoio (surveys gerais de avaliação):**

**IMBENS, Guido W.; WOOLDRIDGE, Jeffrey M.** Recent developments in the
econometrics of program evaluation. **Journal of Economic Literature**, v.
47, n. 1, p. 5-86, 2009. DOI: 10.1257/jel.47.1.5. `[VERIFICADO]`

**ATHEY, Susan; IMBENS, Guido W.** The state of applied econometrics:
causality and policy evaluation. **Journal of Economic Perspectives**, v.
31, n. 2, p. 3-32, 2017. DOI: 10.1257/jep.31.2.3. `[VERIFICADO]`

**GERTLER, Paul J.; MARTINEZ, Sebastian; PREMAND, Patrick; RAWLINGS, Laura
B.; VERMEERSCH, Christel M. J.** Impact evaluation in practice. 2. ed.
Washington, DC: Inter-American Development Bank; World Bank, 2016. DOI:
10.1596/978-1-4648-0779-4. `[VERIFICADO]` (edição em inglês; a edição em
português usada na disciplina está em `notas/disciplina/03-gertler.md`,
cujo DOI impresso não resolve.)

## 2. Quadro de fontes de dados

| Fonte | Unidade e chave | Período | O que mede | Acesso | Uso no desenho |
| --- | --- | --- | --- | --- | --- |
| Lista de habilitados da SECULT (`dados/licc/habilitados/`) | projeto × ciclo; **sem CNPJ** do proponente | ciclos 2022-2026 | tratamento (habilitação), status, valor, cota (2024+), local | público (PDF) | define coortes e tratamento; listagem da população |
| Anexo "Recurso financeiro captado" (`dados/licc/oficial/`) | projeto; CNPJ do **patrocinador** | 2025 | captação efetiva, patrocinador, valor | público (PDF) | intensidade do tratamento em 2025 |
| Extratos do DIO-ES (DEC, art. 17; IN25, art. 49) | repasse; processo, proponente, patrocinador, valor, data | 2022-2026 | captação com data | público, disperso | reconstruir a captação de todos os anos |
| Base de inscrições da SECULT (Mapa Cultural) | projeto; **CNPJ do proponente**, linha, cota, sede, datas | 2022-2026 | inscritos, inabilitados, arquivados | interno (pedido por LAI ou convênio) | chave para ligar às bases de resultado; grupo de comparação de inscritos não habilitados |
| Relatórios de execução e prestação de contas (IN25, arts. 65-66) | projeto | 2022-2026 | estimativa de público, gratuidade, locais, contrapartidas executadas | interno | resultado de uso/acesso |
| RAIS identificada | vínculo e estabelecimento; CNPJ, CNAE, município | anual, 2010-2024 [VERIFICAR último ano] | emprego formal, massa salarial, estabelecimentos | convênio com o MTE | resultado do proponente (emprego) e do município (emprego cultural por CNAE) |
| RAIS pública (agregada) | município × CNAE | anual | emprego e estabelecimentos culturais | público (PDET) | resultado municipal (DiD escalonado) |
| Cadastro CNPJ (Receita Federal, dados abertos) | CNPJ; CNAE, sede, data de abertura, situação, sócios | atual + histórico parcial | natureza jurídica, sobrevivência, sede, sócios comuns | público | classificar proponentes, apurar cota III e o art. 13 |
| SICONFI/DCA (`dados/externos/siconfi_*`) | ente × ano | 2015-2025 | gasto com cultura (função 13), ICMS | público (API) | covariável e choque concorrente; escala da renúncia |
| MUNIC/IBGE, bloco Cultura (`dados/externos/munic2021_*`) | município | 2021 (e edições anteriores com bloco Cultura [VERIFICAR anos]) | equipamentos, conselho, plano, fundo | público (API) | covariáveis pré-tratamento; heterogeneidade |
| SIIC/IBGE (`dados/externos/siic_uf.csv`) | UF × ano | 2011-2024 | ocupação e empresas culturais | público (API) | resultado agregado (controle sintético ES × UFs) |
| SALIC/MinC (`dados/externos/rouanet_*`) | projeto; CNPJ/CPF do proponente | 1993- | captação Rouanet | público (API) | viés de substituição (proponente capta pela Rouanet?) |
| Transferências LAB/LPG/PNAB | ente × ano | 2020-2026 | fomento direto concorrente | público [VERIFICAR fonte consolidada] | controle de choques simultâneos |

**Gargalo:** o identificador do proponente. Os anexos públicos não trazem CNPJ; a SECULT tem (a inscrição o
exige, IN25, art. 19, I, "a"). Sem ele, só o desenho municipal é viável com dados públicos.

## 3. Recomendações: qual desenho cabe na LICC e por quê

Critérios: regras operacionais da LICC como estão (`notas/disciplina/03-gertler.md`, § 11.1), dados
existentes (§ 2), poder (tabelas `analise/tabelas/05_*`, `licc_emd_ilustrativo.csv`) e as lições da
literatura (§ 1).

**Fatos do desenho que decidem o método** (`notas/politica/01-desenho-legal.md`; `notas/dados/01-resultados-descritivos.md`):
(i) a habilitação não usa nota nem corte → sem RD; (ii) a alocação entre habilitados é privada → seleção em
não observáveis, PSM isolado não serve; (iii) nos ciclos 2022-2024 houve habilitados que não captaram
(11, 34 e 50 expirados) → comparação natural dentro da oferta; (iv) desde maio de 2025 a CAP só recebe
projeto com carta de intenção → nos ciclos 2025+ habilitado ≈ captou; (v) presença municipal com adoção
escalonada: coortes de 39, 16, 3, 3 e 3 municípios em 2022-2026 e 14 municípios nunca presentes.

**Desenho principal (D1): DiD com adoção escalonada no nível do proponente, ciclos 2022-2024.**
- *Tratamento:* captar (status "Em execução" ou "Execução finalizada") entre os habilitados de um ciclo;
  *comparação:* habilitados do mesmo ciclo cuja captação expirou, e, como "ainda não tratados", habilitados
  de ciclos posteriores antes de captar.
- *Resultados:* emprego formal e massa salarial do CNPJ do proponente (RAIS identificada), sobrevivência do
  CNPJ, novos projetos culturais (SALIC, editais) — de 1 a 3 anos após a captação.
- *Estimador:* Callaway e Sant'Anna (2021), com o DR-DiD de Sant'Anna e Zhao (2020) e covariáveis pré
  (ciclo, cota, valor pedido, natureza, RMGV, histórico); estudo de evento; sensibilidade de Rambachan e
  Roth (2023) a violações de tendências paralelas.
- *Estimando:* ATT da captação para os projetos habilitados que captaram (EMPT, `notas/disciplina/01-slides-e-guias.md`, § 2.5).
- *Poder:* 293 registros resolvidos em 2022-2024 (198 captaram, 95 expiraram): EMD de **0,35 DP** (poder
  0,80, α = 0,05), subindo para 0,36-0,45 DP com correlação intraproponente de 0,05 a 0,5
  (`05_poder_deff_proponente.csv`; 199 proponentes). Linha de base e covariáveis reduzem o EMD na proporção
  de √(1 − R²) (McKenzie, 2012). Um ciclo isolado só detecta efeitos de 0,53-0,92 DP (`licc_emd_ilustrativo.csv`).
- *Ameaças:* seleção pelo patrocinador em não observáveis variáveis no tempo (a principal); competição pelo
  teto (SUTVA: o captado por um projeto falta a outro); substituição por outras fontes (Rouanet, editais);
  cumprimento parcial (captação parcial = dose).

**Desenho complementar (D2): DiD escalonado municipal.**
- *Tratamento:* primeiro projeto habilitado/executado no município; *comparação:* ainda não tratados e os
  14 nunca tratados (menores: mediana de 12 mil habitantes); *resultados:* emprego e estabelecimentos
  culturais (RAIS pública por CNAE), com o SIIC/IBGE como referência para a classificação.
- *Estimador:* Callaway-Sant'Anna ou imputação de Borusyak, Jaravel e Spiess (2024); inferência por *wild
  cluster bootstrap* e aleatorização (MacKinnon e Webb, 2020) por haver só 78 clusters e coortes de 3.
- *Poder:* com J = 78 e fração tratada de 0,25 a 0,5, o EMD fica entre **0,43 e 1,04 DP** do erro
  idiossincrático, conforme o número de anos pré/pós e a autocorrelação (`05_poder_mde_municipal_did.csv`).
  Como a coorte de 2022 tem 39 municípios, a maior parte da identificação vem de 2023 (16 municípios) em
  diante — poder baixo. Serve para **descrever** heterogeneidade territorial e testar efeitos grandes.
- *Ameaças:* choques simultâneos (LAB, LPG, PNAB), tratamento que liga e desliga (usar de Chaisemartin e
  D'Haultfœuille, 2020), transbordamentos entre municípios vizinhos (Butts, 2021).

**Desenho agregado (D3): controle sintético ou DiD sintético, ES × UFs.** Útil para a pergunta "a LICC mudou o
setor cultural do estado?", mas a renúncia é 0,16% do ICMS e pequena diante da ocupação cultural (85 mil
pessoas), então o efeito provável fica abaixo da volatilidade do indicador (Abadie, 2021) — e o *donor pool*
tem outras leis estaduais via ICMS [VERIFICAR]. Complementar, com expectativa explícita de baixo poder.

**Desenho prospectivo (D4): encorajamento aleatório à captação.** Sortear, entre os projetos com parecer
favorável, quem recebe apoio ativo de aproximação com contribuintes de ICMS (rodadas com patrocinadores),
sem mudar a regra de alocação. Estima o LATE da captação para os projetos "na margem". Ressalva: com teto
vinculante, o encorajado capta no lugar de outro (SUTVA; desenho de saturação de Baird *et al.*, 2018).

**Desenhos descartados:** RD na habilitação (sem nota de corte; o limiar de 35% é manipulável), PSM isolado
(seleção em não observáveis), antes-depois e com-sem sem ajuste (contrafactuais falsos, Gertler *et al.*,
2016).

**Complemento qualitativo:** a teoria da mudança da LICC tem elos (escolha do patrocinador, execução das
contrapartidas) que os dados administrativos não medem; análise de contribuição ou entrevistas com
proponentes e patrocinadores (HM Treasury, 2026, via `notas/disciplina/04-itau-magenta-adb.md`).

## 4. Lista de referências (ABNT)

As referências desta nota estão na seção 1, cada uma em formato ABNT (NBR 6023) com DOI e marca de
verificação. Para o artigo, a seleção mínima é: Callaway e Sant'Anna (2021); Goodman-Bacon (2021); Roth
*et al.* (2023); Rambachan e Roth (2023); Sant'Anna e Zhao (2020); Borusyak, Jaravel e Spiess (2024); Abadie
(2021); Arkhangelsky *et al.* (2021); McKenzie (2012); Burlig, Preonas e Woerman (2020); Bloom (1995);
Djimeu e Houndolo (2016); MacKinnon e Webb (2020); Gelman e Carlin (2014); Gertler *et al.* (2016).

## 5. Pendências e questões em aberto

- Acesso à RAIS identificada (convênio) e à base de inscrições da SECULT com CNPJ: sem elas, D1 não é
  executável; com dados públicos só D2 e D3.
- σ, CCI e autocorrelação dos resultados escolhidos: hoje são hipóteses ilustrativas nos scripts de poder;
  calibrar com a RAIS pré-2022 (placebos com datas falsas, Burlig, Preonas e Woerman, 2020).
- Quais UFs têm lei estadual de incentivo via ICMS e desde quando (D3).
- Série de captação por projeto para 2022-2024 (extratos do DIO) — hoje só 2025 está consolidado.
- Semântica exata dos status da lista de habilitados e composição da lista a partir de maio de 2025
  (`notas/politica/01-desenho-legal.md`, § 7).
