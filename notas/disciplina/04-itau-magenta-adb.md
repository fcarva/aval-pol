# 04 — Três guias de avaliação: Itaú Social (2017), Magenta Book (2026) e ADB (2017)

> Nota de leitura para o mini artigo da LICC (PECO 5046-6046). Gerada em 23/09/2026
> por agente de IA (Claude) a partir dos arquivos da disciplina; **exige revisão humana**
> antes de qualquer trecho ir para o artigo (Portaria CNPq 2664/2026, ver CLAUDE.md).

**Arquivos lidos**

| Guia | PDF (raiz do projeto) | Texto extraído |
| --- | --- | --- |
| Itaú Social | `avaliacao-economica-3a-ed_1513188151 (2).pdf` | `disciplina/txt/avaliacao-economica-3a-ed_1513188151 (2).txt` |
| Magenta Book | `CCS0126982978-001_PN10541411_Magenta_Book_Update_V2_Accessible_2__1_ (1).pdf` | `disciplina/txt/CCS0126982978-...(1).txt` |
| ADB | `impact-evaluation-development-interventions-guide (1).pdf` | `disciplina/txt/impact-evaluation-development-interventions-guide (1).txt` |

**Convenção de páginas.** Todas as páginas citadas são **impressas**. No Itaú e no
Magenta, página impressa = página do PDF. No ADB, **página do PDF = impressa + 14**
(ex.: eq. 7.1 está na p. 121 impressa = p. 135 do PDF). A contagem foi aferida pelos
cabeçalhos/rodapés de cada página (feita no scratchpad da sessão; reprodutível com
`pdftotext -layout` separando por `\f`). Fórmulas e figuras que a extração de texto
corrompeu foram conferidas abrindo o PDF (Itaú p. 112, 130, 154, 198-199, 204-205,
211; Magenta p. 55, 81; ADB p. 121-124).

**Sumário executivo**

- As três fontes estão identificadas e verificadas. **Atenção:** o arquivo do Magenta
  Book fornecido pela disciplina é a **atualização de maio de 2026**, não a edição de
  2020; a paginação e parte do conteúdo (IA, *Test and Learn*, intervenções
  territoriais, pré-registro) são próprias de 2026.
- **Itaú (2017)** é a melhor fonte em português para: definição de impacto e
  contrafactual (cap. 1-2), pressupostos formais de DD, pareamento, VI e RDD (cap. 4-7)
  e **retorno econômico / custo-efetividade** (cap. 8). Sobre poder estatístico é só
  qualitativo (seção 3.5, p. 78-81), sem fórmula.
- **Magenta (2026)** dá a moldura de **tipos de avaliação** (processo, impacto, *value
  for money*), **proporcionalidade**, **teoria da mudança**, escolha de abordagem
  (árvores de decisão, Fig. 2.4 e 3.1) e uso de dados administrativos. Poder: só
  princípios (p. 83-84); o detalhe está no anexo TIGER, que **não** está no arquivo.
- **ADB (2017)** é a melhor fonte para a **proposta de avaliação de impacto**: teoria da
  mudança com **funil de atrito** (p. 23-24), estimandos ATE/ITT/ATT/ATU/LATE e a
  identidade **ITT = ATT × taxa de participação** (p. 44), quadro-resumo dos métodos não
  experimentais (Tabela 5.5, p. 91), árvore de decisão do desenho (Tabela 8.1, p. 135) e
  **fórmulas de poder** 7.1-7.5 (p. 121-124), que reproduzimos numericamente.
- Nenhum dos três guias trata **renúncia fiscal** especificamente. O argumento de que a
  renúncia de ICMS é custo da LICC precisa ser construído (seção 5.4) a partir de
  "custo econômico = contábil + oportunidade" (Itaú, p. 200), da noção de
  adicionalidade (Magenta, p. 26-27) e da alternativa disponível na ausência do programa
  (Itaú, p. 19).

---

## 0. Identificação e referências (ABNT NBR 6023)

### 0.1 Itaú Social — organizadores e autores confirmados

Ficha catalográfica e créditos (PDF p. 4-5): organizadores **Naercio Aquino Menezes
Filho** e **Cristine Campos de Xavier Pinto**; autores Betânia Peixoto, Cristine Campos
de Xavier Pinto, Lycia Lima, Miguel Nathan Foguel e Ricardo Paes de Barros; editora
Fundação Itaú Social, São Paulo, 2017, 3. ed., ISBN 978-85-66932-31-7. A 1ª edição é de
2012 (prefácio, p. 9). Autoria por capítulo conferida nas folhas de rosto (p. 13, 39,
55, 85, 111, 145, 167, 193).

> MENEZES FILHO, Naercio Aquino; PINTO, Cristine Campos de Xavier (org.). **Avaliação
> econômica de projetos sociais**. 3. ed. São Paulo: Fundação Itaú Social, 2017.
> ISBN 978-85-66932-31-7.

Capítulos (citar o capítulo quando a ideia for do autor do capítulo):

| Cap. | Referência ABNT (parte de obra) | Páginas |
| --- | --- | --- |
| 1 | BARROS, Ricardo Paes de; LIMA, Lycia. Avaliação de impacto de programas sociais: por que, para que e quando fazer? In: MENEZES FILHO; PINTO (org.), 2017. | p. 13-37 |
| 2 | FOGUEL, Miguel Nathan. Modelo de resultados potenciais. In: idem. | p. 39-54 |
| 3 | FOGUEL, Miguel Nathan. Método de aleatorização. In: idem. | p. 55-84 |
| 4 | FOGUEL, Miguel Nathan. Diferenças em diferenças. In: idem. | p. 85-110 |
| 5 | PINTO, Cristine Campos de Xavier. Pareamento. In: idem. | p. 111-144 |
| 6 | PINTO, Cristine Campos de Xavier. Variáveis instrumentais. In: idem. | p. 145-166 |
| 7 | PINTO, Cristine Campos de Xavier. Regressão descontínua. In: idem. | p. 167-192 |
| 8 | PEIXOTO, Betânia. O cálculo do retorno econômico. In: idem. | p. 193-225 |

[VERIFICAR] URL oficial da versão digital no site do Itaú Social, se o artigo for citar
a versão online (não conferida; o arquivo local basta para a citação impressa).

### 0.2 Magenta Book — edição de maio de 2026

- Capa: "May/2026 — Magenta Book — Central Government guidance on evaluation" (PDF
  p. 1). O nome do arquivo coincide com o do PDF oficial em
  `assets.publishing.service.gov.uk/media/6a3157a0141f0690ad5fa438/...` (localizado por
  busca web em 23/09/2026).
- Página oficial (https://www.gov.uk/government/publications/the-magenta-book,
  consultada em 23/09/2026): publicado por **HM Treasury e Evaluation Task Force**;
  primeira publicação em 27/04/2011; **última atualização em 15/05/2026**. O **Anexo A**
  (métodos analíticos) é documento separado, atualizado em 14/05/2026; o anexo **TIGER**
  (transparência, pré-registro, poder) e o guia de complexidade também são separados.
- Autores/editores listados nos agradecimentos (p. 7), encabeçados por Levin Wheller;
  como é documento institucional, a autoria ABNT é o órgão.

> HM TREASURY. **Magenta Book**: central government guidance on evaluation. London: HM
> Treasury; Evaluation Task Force, maio 2026. Disponível em:
> https://assets.publishing.service.gov.uk/media/6a3157a0141f0690ad5fa438/CCS0126982978-001_PN10541411_Magenta_Book_Update_V2_Accessible_2__1_.pdf.
> Acesso em: 23 set. 2026.

**Cuidado:** se o artigo quiser citar "Magenta Book 2020" (como aparece em outras
listas da disciplina), a paginação desta nota **não vale** para aquela edição
[VERIFICAR com os professores qual edição usar; recomendação: citar a de 2026, que é a
vigente e a que está no material].

### 0.3 ADB — autoria confirmada: White e Raitzer

Folha de rosto (PDF p. 1 e 3): **Howard White** e **David A. Raitzer**, Asian
Development Bank. Página de créditos (PDF p. 4): © 2017 ADB, Mandaluyong City, Metro
Manila; ISBN 978-92-9261-058-6 (impresso) e 978-92-9261-059-3 (eletrônico); DOI
10.22617/TCS179188-2; licença CC BY 3.0 IGO. **DOI conferido na API da Crossref em
23/09/2026**: título idêntico, editora Asian Development Bank, data de emissão
dezembro de 2017, tipo *report*.

> WHITE, Howard; RAITZER, David A. **Impact evaluation of development interventions**:
> a practical guide. Mandaluyong City: Asian Development Bank, 2017. DOI:
> https://doi.org/10.22617/TCS179188-2.

---

## 1. Itaú Social — *Avaliação econômica de projetos sociais* (2017)

### 1.1 Mapa do livro

Avaliação econômica = **avaliação de impacto + cálculo do retorno econômico**
(prefácio, p. 9-10; cap. 8, p. 194). Parte I: métodos básicos (resultados potenciais,
aleatorização, DD, pareamento); parte II: VI e RDD; parte III: retorno econômico
(prefácio, p. 10-11). Cada capítulo traz exercícios.

### 1.2 Desenho, ex ante e teoria de mudança (Barros e Lima, cap. 1)

O livro não tem capítulo de modelo lógico, mas o cap. 1 dá os critérios de desenho
mais citáveis em português:

- **Programa existe para mudar resultados de interesse coletivo**; produtos só
  importam se a teoria de mudança que fundamenta o desenho levar deles ao resultado.
  Sucesso não se mede pela entrega de produtos, salvo se a teoria estiver plenamente
  comprovada (p. 15).
- Dois requisitos de desenho "rotineiramente esquecidos" (p. 15): (i) definir com
  precisão **quais resultados** o programa deve mudar — é o desenho que se adequa aos
  resultados, não o contrário; (ii) especificar **a magnitude da contribuição** esperada,
  porque a justificativa depende de custo e magnitude (princípio de custo-benefício).
- **Monitoramento ≠ avaliação de impacto** (p. 16-17): monitoramento verifica se o
  resultado agregado se move na direção/velocidade desejada; impacto isola a
  contribuição de cada programa. Um programa pode ter impacto nulo num contexto de
  sucesso agregado e vice-versa (p. 17).
- **Impacto = o que aconteceu − o que teria acontecido** para o mesmo grupo de
  referência; uma das situações é sempre contrafactual (p. 18-19).
- **A ausência do programa não é um vazio**: alternativas ocupam o espaço, e o impacto
  estimado é o valor adicionado em relação a elas; é preciso descrever a alternativa
  disponível na ausência do programa (p. 19).
- **Grupo de referência** decorre do objetivo da avaliação, não da conveniência
  metodológica: prestação de contas → beneficiários; expansão → futuros beneficiários
  (p. 20). **Impacto privado** (sobre beneficiários) vs **impacto social** (inclui não
  beneficiários afetados) (p. 20).
- **Heterogeneidade**: distribuição de impactos, não só a média; sensibilidade ao
  ambiente, ao tempo de exposição e a variações de desenho/dosagem/implementação
  (p. 21-22).
- **Quando avaliar** (p. 22-24): *ex ante* (prever impactos antes de implantar; a teoria
  predomina, via simulação com parâmetros calibrados; serve sobretudo para escolher o
  melhor desenho), *ex post de percurso* (durante a operação; tensão entre rapidez e
  maturação dos impactos) e *ex post de encerramento*. Toda avaliação combina teoria e
  evidência; mesmo ex post, interpretação, mecanismos e generalização exigem teoria
  (p. 24).
- **Impacto potencial vs efetivo** (p. 27-28): um desenho bom pode ter impacto efetivo
  pequeno por implementação deficiente; a avaliação mede quanto do potencial se perdeu.
- **Custo-efetividade e custo-benefício** exigem magnitude do impacto; considerar todos
  os custos e benefícios sociais, inclusive externalidades (p. 29-30). Alternativa de
  valoração: disposição a pagar (p. 31-32).
- **Usos**: interno (veredicto de continuidade; ajuste de desenho, "marco lógico") e
  externo (bem público; melhores práticas; validade externa) (p. 33-35).
- Sucesso de uma avaliação depende de **controle sobre a seleção** (sorteio dentro de
  estratos) e de **bom sistema de monitoramento** (p. 36-37). A p. 36 antecipa a
  intuição da descontinuidade (seleção por escore).

### 1.3 Resultados potenciais (Foguel, cap. 2)

- Comparações "ingênuas": antes-depois (p. 41-43) e tratados vs não tratados (p. 43-45).
- Notação: Y_i(1), Y_i(0); efeito individual β_i = Y_i(1) − Y_i(0) (p. 45).
  **EMP** = E[β_i] (eq. 3) e **EMPT** = E[β_i | T_i = 1] (eq. 4) (p. 46); EMPNT na
  nota 5 (p. 47). EMPT é o parâmetro natural de programas de adesão voluntária (p. 47);
  EMP/EMPNT interessam para expansão (nota 6, p. 47).
- Observado: Y_i = T_i Y_i(1) + (1 − T_i) Y_i(0) (eq. 5, p. 47) → regressão com
  coeficiente aleatório Y_i = α + β_i T_i + ε_i (eq. 6).
- **Decomposição do viés de seleção** (eq. 10, p. 50):
  R = E[Y(1)|T=1] − E[Y(0)|T=0] = **EMPT + V**, com
  V = E[Y(0)|T=1] − E[Y(0)|T=0]. Sumário das hipóteses de cada método (p. 50-53).

### 1.4 Métodos e pressupostos (notação do livro)

| Método | Hipótese(s) de identificação | Parâmetro | Diagnósticos/cuidados | Páginas |
| --- | --- | --- | --- | --- |
| Aleatorização (Foguel, cap. 3) | Sorteio torna E[Y(0)\|T=0] = E[Y(0)\|T=1] | EMP; EIT (intenção de tratar) com descumprimento | Validade interna vs externa (3.1); descumprimento, contaminação, atrito (3.4) | 57-60, 64, 68 |
| Diferenças em diferenças (Foguel, cap. 4) | **H1 tendências paralelas**: E[Y(0)\|T=1,t=1] − E[Y(0)\|T=1,t=0] = E[Y(0)\|T=0,t=1] − E[Y(0)\|T=0,t=0]; composição dos grupos estável; ausência de choques idiossincráticos pós-programa | EMTT (efeito sobre tratados) | Teste de tendências pré (p. 90); efeitos antecipatórios (nota 5, p. 90); *Ashenfelter dip* e não observáveis variantes no tempo invalidam (p. 104); correlação serial (nota 13, p. 102) e erros-padrão por conglomerado com dados agregados (nota 15, p. 103) | 89-104 |
| Controle sintético (Box 4.1) | Pesos W* ≥ 0, somando 1, sobre o *donor pool*, que minimizam a distância pré-intervenção no resultado e preditores (Abadie et al., 2010) | Efeito na unidade agregada tratada | Útil quando a intervenção é numa unidade agregada (ex.: um estado) | 103 (n. 16), 105-106 |
| Pareamento (Pinto, cap. 5) | **H1** Y_i(0) ⊥ T_i \| X_i (EMPT) ou H1′ (Y_i(0), Y_i(1)) ⊥ T_i \| X_i (EMP); **H2** Pr[T_i=1\|X_i] < 1 (EMPT) ou H2′ 0 < Pr < 1 (EMP) | EMPT, EMP | Não testável diretamente; sobreposição (suporte comum) verificável; escore de propensão (Rosenbaum e Rubin, 1983) | 112-113, 120-122 |
| Pareamento + DD | **H3**: E[Y⁰_{t1} − Y⁰_{t0} \| T=1, p(X)] = E[Y⁰_{t1} − Y⁰_{t0} \| T=0, p(X)]; suporte comum nos dois períodos | EMPT | Permite não observáveis fixos no tempo; X deve ser pré-programa (Heckman, Ichimura e Todd) | 130-132 |
| Variáveis instrumentais (Pinto, cap. 6) | **H1** alocação aleatória de Z; **H2** restrição de exclusão Y_i(z,t) = Y_i(z*,t); **H3** monotonicidade (elimina *defiers*) | **LATE** (compliers) | Estimador de Wald: [E(Y\|Z=1) − E(Y\|Z=0)] / [Pr(T=1\|Z=1) − Pr(T=1\|Z=0)] (eq. 6.8); MQ2E; validade externa limitada a compliers | 147-160 |
| Regressão descontínua (Pinto, cap. 7) | **H1** continuidade de E[Y(1)\|Z=z] e E[Y(0)\|Z=z] em z; **H2** ignorabilidade local em c; caso *fuzzy*: **H3** T_i(z) não decrescente | Efeito médio local no corte | *Sharp* vs *fuzzy* (p. 169); janela por validação cruzada (Imbens e Lemieux, 2008) (p. 181-182); gráficos de Y, X e T contra Z; teste de manipulação de McCrary (2008) (p. 184) | 169-185 |

Exemplos brasileiros úteis: **Box 4.2**, Programa Saúde da Família avaliado por DD com
datas de entrada diferentes dos municípios (Rocha e Soares, 2010) (p. 107) — análogo
direto para uma expansão municipal escalonada; desonerações fiscais citadas como
intervenção que atinge grupos inteiros, avaliável por DD agregado (p. 103).

### 1.5 Tamanho de amostra e poder (Foguel, seção 3.5, p. 78-81)

**Só qualitativo; não há fórmula no livro** (remete a Bloom, 1995, e Duflo et al.,
2008 — nota 15, p. 78). Fatores listados:

1. Nível de aleatorização: indivíduo vs conglomerado; com correlação intraconglomerado
   alta, amostrar mais conglomerados em vez de mais unidades por conglomerado (p. 79).
2. Subgrupos: cada subgrupo é um "miniexperimento" que precisa de poder próprio;
   estratificação aumenta a precisão (p. 79-80; nota 19).
3. Tamanho do efeito esperado: efeito pequeno exige amostra maior; não fixar efeito
   mínimo alto demais (p. 80).
4. Dispersão do resultado, estimada com outras pesquisas sobre a população-alvo (p. 80).
5. Nível de poder: usual 80% (p. 80).
6. Proporção tratados/controles: 50% se custos unitários semelhantes; mais controles se o
   tratamento é caro (p. 81).
7. Descumprimento parcial: identifica só compliers e exige amostra maior (p. 81).

Definições: poder = 1 − P(erro tipo II); erro tipo I vs II (nota 16, p. 78).

### 1.6 Retorno econômico (Peixoto, cap. 8) — útil para a renúncia como custo

- Benefício = **valor monetário do impacto**; só se calcula depois da avaliação de
  impacto e se ela mostrar efeito (p. 196). Benefício privado (participantes) vs
  benefício público/externalidade (p. 195).
- Desconto: VP = VF / (1 + i)^n (eq. 1, p. 198); VPTB_t0 = VB_t0 + Σ VFB_tn / (1 + i)^n
  (eq. 2, p. 199). Usar **taxa de juros real**; avaliadores costumam usar taxa de longo
  prazo menor que a corrente (p. 199-200).
- **Custo econômico = custo contábil + custo de oportunidade** (p. 200); exemplos de
  custo de oportunidade: imóvel cedido, trabalho voluntário, tempo do participante
  (p. 200-201). VPTC análogo (eq. 3, p. 202); mesma taxa de desconto para custos e
  benefícios (p. 202).
- Medidas (p. 203-208): **VPL** = (VB_t0 + Σ VFB_tn/(1+i)^n) − (VC_t0 + Σ VFC_tn/(1+i)^n)
  (eq. 5, p. 204); **TIR**: taxa que zera o VPL (eq. 6, p. 205), comparada a uma taxa
  mínima de atratividade; **razão custo-benefício** = VPTB/VPTC (eq. 7, p. 206) e
  retorno % = (RCB − 1) × 100 (eq. 8); **razão custo-efetividade** = impacto estimado /
  custo econômico (eq. 9, p. 207-208), para quando não se quer ou não se pode monetizar
  o impacto — não diz se o projeto é viável, só compara alternativas com o mesmo
  indicador, público e finalidade (p. 208).
- Comparar retornos só entre projetos com objetivos e públicos semelhantes (p. 203).
- **Sensibilidade** (p. 209-211): univariada (limites de IC 90-95% para parâmetros
  estimados; faixas históricas para parâmetros discricionários, como a taxa de desconto
  — Selic, poupança, IPCA/IGP) e conjunta: **total de cenários = 3^x − 1** para x
  parâmetros (eq. 10, p. 211); reportar % de cenários com conclusão contrária.

### 1.7 O que o Itaú diz sobre avaliar sem aleatorização

- A maior parte do livro é não experimental porque, na prática, a seleção não é
  aleatória (prefácio, p. 10). Métodos não experimentais "procuram mimetizar" o
  experimento (cap. 4, p. 86).
- Mesmo sem aleatorização total, há situações eticamente defensáveis de sorteio:
  **excesso de demanda**, **ordem de entrada**, **intragrupos** e **encorajamento**
  (p. 61-63) — base para propor aleatorização parcial prospectiva.
- Escolha do método segue a natureza da seleção: nos observáveis (cap. 5), em não
  observáveis fixos no tempo (cap. 4) ou em não observáveis com instrumento/corte
  (cap. 6-7) (nota 4, p. 89).

---

## 2. Magenta Book (HM Treasury, 2026)

### 2.1 Definição e momentos da avaliação

- Avaliação de política = avaliação sistemática do **desenho, implementação e
  resultados** de uma intervenção: como foi implementada, que efeitos teve, para quem e
  por quê; o que melhorar; impactos globais e custo-efetividade (p. 8, 15).
- Perguntas **antes / durante / depois** (p. 8, 21-22). "Antes": como a intervenção deve
  funcionar, por que pode falhar, onde estão riscos e incertezas, qual a linha de base
  (p. 21) — é a base para uma **avaliação de desenho ex ante/de meio de percurso**.
- Ciclo **ROAMEF** (Rationale, Objectives, Appraisal, Monitoring, Evaluation,
  Feedback) (Fig. 1.1, p. 18); objetivos **SMART** (nota 12, p. 19); teoria da mudança
  começa já na fase de racional/objetivos (p. 19).
- **Planejar cedo**: pequenas mudanças de desenho (dados administrativos individuais,
  questionário obrigatório para beneficiários, sequenciamento da implantação) decidem se
  a avaliação responderá às perguntas-chave (p. 23).
- Duas razões para avaliar: **aprendizado** e **accountability** (p. 16-17).

### 2.2 Tipos de avaliação (p. 28-29; Tabela 2.2, p. 52-53)

| Tipo | Pergunta-síntese | Exemplos de perguntas |
| --- | --- | --- |
| Processo | O que aprender de como foi entregue? | Entregue como previsto? Alcançou quem devia? O que funcionou, para quem e por quê? |
| Impacto | Que diferença a intervenção fez? | Alcançou os resultados? Quanto se atribui a ela? O que teria acontecido de qualquer forma? Efeitos não intencionais? Diferenças entre grupos? |
| *Value for money* | Foi bom uso dos recursos? | Custos e benefícios? Custo-efetividade vs alternativas e vs não fazer nada? Economia, eficiência, eficácia e equidade? |

Para entender se, como, por que, para quem e a que custo funcionou, **os três tipos
são necessários** (p. 13, 51).

### 2.3 Qualidade e proporcionalidade

- Boa avaliação é **útil, crível, robusta e proporcional** (p. 30-31). Robustez inclui
  amostras suficientes e **poder** adequado em desenhos experimentais (p. 31).
- **Proporcionalidade** (p. 31): intervenção de baixo risco, bem evidenciada e de baixa
  prioridade → monitoramento e avaliação leves; intervenção de alto risco, alto status e
  inovadora → avaliação de grande escala. **Critérios de prioridade**: (a) alto perfil;
  (b) alta incerteza/risco; (c) alto custo; (d) alto potencial de aprendizado (inclusive
  para preencher lacunas de evidência).
- Fatores que moldam o desenho: complexidade do sistema, escala/inovação, evidência
  existente, momento das decisões, margem para mudar a intervenção (p. 30).
- Transparência "tão aberta quanto possível e tão fechada quanto necessário",
  proporcional ao custo, perfil e potencial de aprendizado (p. 38). Não há percentual
  padrão do valor da intervenção a gastar com avaliação (Tabela 5.1, p. 120).
- Pré-registro (p. 66-67): registrar objetivos, perguntas, desenho, coleta e análise
  **antes** de ver os dados de resultado; em avaliações quantitativas, **incluir cálculo
  de poder e tamanho de amostra**; aplicar de forma proporcional.

### 2.4 Teoria da mudança (seção 2.2.1, p. 44-47)

- Entender a intervenção = problema, mudança pretendida, **cadeia causal**, atores,
  grupos afetados, condições para sucesso; expor **pressupostos** e a força da evidência
  que os sustenta; contexto; teste de estresse do desenho com quem desenha e implementa
  (p. 44).
- Síntese de evidência existente é parte central; reduz escala e foca a avaliação nas
  incertezas (quadro, p. 45).
- **Fig. 2.2 (p. 46)**, ToC linear baseada em Mayne (2017): insumos → produtos →
  resultados (curto/médio prazo) → impacto (longo prazo), com **pressupostos entre cada
  elo** (sobre quem adere, mudanças iniciais de comportamento, benefícios e efeitos não
  intencionais) e **fatores contextuais**. Diagramas/modelos lógicos são representações
  da ToC, não a ToC (nota 19, p. 45).
- Explorar a **teoria negativa do programa** — por que cada elo pode falhar (p. 47).
  Em intervenções complexas, laços de retroalimentação e fronteiras do sistema (p. 47).
  Desenvolver com *stakeholders* e revisar ao longo da avaliação (p. 47).
- A ToC gera as perguntas: incertezas, fraquezas de evidência, **resultados
  intermediários** que medem progresso (p. 48); ~6-7 perguntas de alto nível (p. 51).
- Referência verificada: MAYNE, John. Theory of change analysis: building robust
  theories of change. **Canadian Journal of Program Evaluation**, v. 32, n. 2,
  p. 155-173, 2017. DOI 10.3138/cjpe.31122 (Crossref, 23/09/2026). O Magenta traz o
  volume errado ("2(2)") na nota 20 da p. 46 e correto ("32(2)") na p. 47.

### 2.5 Escolha da abordagem de impacto (p. 53-61)

- **Fig. 2.3 (p. 54)**: o resultado depende da intervenção **e** de outras influências
  (tendências, coincidência, outras intervenções, **viés de seleção**).
- **Fig. 2.4 (p. 55)**, árvore de decisão (baseada em Hills e Junge, 2010), três
  colunas: (i) "Até que ponto os resultados foram alcançados?" → estudo antes-depois se
  a intervenção é de propósito único, local, estável, resultados em 1-3 anos, poucas
  explicações alternativas; (ii) "Os resultados foram alcançados e foi a intervenção?"
  → abordagem experimental se isolável, resultado único, curto prazo, hipótese robusta,
  estável, efeito pequeno a médio; senão quase-experimental (alvo em grupos/áreas,
  interação entre grupos, população mutável, grupo-alvo pequeno); (iii) "Que mudanças
  ocorreram e por quê?" → teoria-based se desenvolvimental, ambiente dinâmico,
  resultados difusos, vias causais complexas, implementação variável, médio-longo
  prazo; **desenho combinado** na base.
- Requisitos do contrafactual (p. 56): dados de qualidade e quantidade suficientes;
  grupo **genuinamente comparável**; efeito grande o bastante para se distinguir do
  **ruído** — o que costuma exigir embutir a avaliação no desenho da intervenção.
- **Tabela 2.3 (p. 57-58)**, viabilidade de abordagem (quase-)experimental — mais viável
  se: intervenção discreta e estável; sistema estável; relação direta; efeito grande e
  rápido; mudança clara em participantes identificáveis; dados sobre participantes, em
  períodos precisos, **antes e durante**; amostras suficientes; comparação embutida no
  desenho; **início escalonado**; alocação aleatória ou **por corte objetivo**; grupos de
  comparação "naturais". Menos viável se: alocação **subjetiva** (grupos diferentes de
  saída); **lançamento simultâneo em todo o território**; dados só em totais agregados;
  dados não buscados antes ou indisponíveis para não participantes; amostras pequenas.
- (Quase-)experimentos servem melhor quando o foco é accountability, resultados
  conhecidos e mensuráveis, muitos afetados mas não toda a população, implementação
  pouco variada e efeito homogêneo; não explicam **como** a mudança ocorre — combinar
  com teoria-based ou avaliação de processo (p. 58; nota 30 sobre validade interna e
  externa).
- **Teoria-based** (p. 59-61): testar se as cadeias causais são sustentadas por
  evidência suficientemente forte e **descartar explicações alternativas**; rigor vem de
  coerência, evidência específica, triangulação, exclusão de causas alternativas e
  escrutínio externo (p. 59; processo em 5 passos, Fig. 2.5, p. 60). Indicada quando
  há paisagem de políticas combinadas, sistema complexo, resultados emergentes,
  **impossibilidade de contrafactual adequado** ou necessidade de saber se funcionaria em
  outro contexto (p. 61). Observação direta do impacto só quando se tem confiança de que
  nada mais mudaria sem a intervenção (p. 61).

### 2.6 Métodos (cap. 3)

- Seleção de métodos guiada pela ToC, com *stakeholders*; quase sempre **métodos mistos**
  (p. 71). Estrutura **PICOT** (população, intervenção, controle, resultado, tempo)
  para planejar experimentos (p. 79).
- **Fig. 3.1 (p. 81)**, seleção de métodos: comparar afetados e não afetados? (não →
  teoria-based) → atribuir ao acaso? (sim → RCT individual, fatorial, por
  conglomerado, *stepped-wedge*; não → quase-experimentos): dados antes e depois para
  os dois grupos → **DD**; alocação por corte em medida pré-intervenção → **RDD**;
  dados individuais sobre fatores de participação → **pareamento**; histórico para
  construir um "clone" → **controle sintético**; fator externo que afeta a exposição e
  não o resultado → **VI**; o resultado afeta a probabilidade da intervenção →
  **timing of events**. **Atenção:** o ramo "tendências antes e depois, sem grupo de
  controle concorrente" aponta para "variáveis instrumentais" na figura, o que parece
  erro de diagramação — pela Tabela 3.3 (p. 82) o método para esse caso é a **série
  temporal interrompida**. Não reproduzir a figura sem corrigir/anotar.
- **Tabela 3.3 (p. 82-83)**, prós e contras: RCT; **série temporal interrompida e DD**
  (assume continuidade da tendência; DD reforça com tendência do controle; difícil sem
  data clara de início; controle pode ser difícil de achar); **RDD** (causal se
  observações dos dois lados do corte são plausivelmente aleatórias; exige muitas
  observações e sensibilidade à janela; vale perto do corte); **pareamento por escore**
  (exige dados ricos; viés se não observáveis afetam participação e resultado);
  **controle sintético** (comparação quando não há outros comparadores; muitos dados
  secundários; **pode ser usado com amostras pequenas**; só se houve relação entre
  tratado e controles no pré-período; mais comum em intervenções de **nível de área**);
  **VI/experimentos naturais** (instrumento válido é difícil; estima impactos marginais);
  **timing of events** (não observáveis na seleção; supõe ausência de antecipação).
- **Teoria-based (Tabela 3.2, p. 77-78)**: avaliação realista, **análise de
  contribuição** (linha de raciocínio evidenciada, não prova; trabalha com efeitos
  médios), *process tracing*, atualização bayesiana, *contribution tracing*, **QCA**
  (compara múltiplos casos; **funciona melhor com 10-50 casos**), *outcome harvesting*,
  *most significant change*. Nenhum dá tamanho de efeito preciso (nota da tabela, p. 78).

### 2.7 Poder estatístico (3.5.1, p. 83-84)

- Toda avaliação quantitativa deve fazer **cálculo de poder**; amostras pequenas com
  efeitos pequenos geram falsos negativos e também falsos positivos (p. 83-84).
- **Calibrar o poder ao contexto**: mais poder quando deixar de detectar um efeito é
  mais custoso — **gasto público significativo**, mudanças irreversíveis, risco de
  efeitos adversos (p. 84).
- Supostos necessários: tamanho da amostra, tamanho do efeito, variância do resultado;
  software R, Stata, G*Power (p. 84).
- **Publicar** a análise de poder (protocolo/plano de análise ou anexo do relatório)
  (p. 84). Detalhes técnicos no anexo TIGER — **não incluído no arquivo da disciplina**.

### 2.8 *Value for money* (3.6, p. 85-89)

- Princípios (p. 85): (1) embutir VfM no planejamento desde o início, alinhada a
  processo e impacto; (2) ligar à **avaliação ex ante** (*appraisal*) e comparar com as
  expectativas do *business case*; (3) partir de **dados empíricos** (execução,
  administrativos, pesquisa primária) e evitar dependência de modelagem; (4) apresentar
  achados monetizados **em contexto**, com os benefícios não monetizáveis.
- Métodos (Tabela 3.4, p. 87-88): **ACB social**, **custo-efetividade**, custo-utilidade,
  **SROI** (valor social por libra investida). Alternativas quando não se monetiza
  (Tabela 3.5, p. 89): **Quatro Es** (economia, eficiência, eficácia, **equidade**) e
  **rubricas**; podem ser combinados.
- VfM avalia valor **social**: custos e benefícios que afetam o bem-estar da população;
  VfM é julgamento equilibrado do melhor uso de recursos públicos (p. 29).

### 2.9 Dados (cap. 4)

- Planejar a coleta junto com a intervenção; sem isso a avaliação pode ser impossível,
  limitada ou cara; **linha de base** cedo; dados de comparação negociados (p. 96-97).
- Preferir **dados administrativos e de monitoramento** (baratos, cobrem a população,
  dão tendência anterior à intervenção), mas atenção a conceitos "relacionados mas não
  idênticos" aos de interesse (p. 100-101). Usos de dados de monitoramento em cada elo
  da ToC (Tabela 4.2, p. 102).
- **Vinculação de bases** por identificadores únicos (no Reino Unido, NI, NHS, VAT); sem
  identificador, *fuzzy matching* com falsos positivos e negativos (p. 112).
- Ligação avaliação-desenho (p. 124-125): embutir requisitos de avaliação no
  monitoramento; colher contato e consentimento; **censo/questionário obrigatório dos
  participantes** (ex.: **candidatos a um *grant* obrigados a responder**), piloto;
  **implantação escalonada** para criar comparação; alguns requisitos de dados exigem
  previsão em lei.

### 2.10 Carteiras de projetos e intervenções territoriais (2.3.1-2.3.2, p. 63-66)

- **Grupo de projetos** (p. 63-64): (1) intervenção ampla com implementação delegada; (2)
  "**fundo de inovação**", com propostas **competitivas**. No segundo, ênfase em
  projetos individuais e na medida em que o desenho estimulou inovação; em ambos,
  **medidas comuns** a todos os projetos, preferencialmente de sistemas
  administrativos; QCA e estudos de caso selecionados.
- **Intervenções territoriais** (p. 64-66): ToC territorial; definição espacial;
  **transbordamentos** (efeitos em áreas vizinhas) e **deslocamento** (melhora aqui,
  piora ali); **problema de seleção** — lugares não são escolhidos ao acaso; solução:
  **controle sintético**; se inviável, teoria-based; meta-avaliação com muitos lugares;
  defasagem de evidência e avaliação retrospectiva com dados administrativos.

### 2.11 IA na avaliação (5.6, p. 128-133)

Uso proporcional, com garantia de qualidade e verificável; saídas plausíveis porém
falsas exigem conferência humana (p. 128); IA complementa, não substitui o avaliador,
e riscos/limitações devem ser comunicados (p. 129); associações probabilísticas **não
estabelecem causalidade** (Tabela 5.2, p. 130). Útil para a **declaração de uso de IA**
do artigo.

### 2.12 O que o Magenta diz sobre avaliar sem aleatorização

Quase-experimentos quando a alocação não é aleatória, com ajuste analítico de
diferenças conhecidas (p. 79-80); a escolha depende da natureza da alocação, do tipo de
controle (concorrente ou histórico) e do formato e volume dos dados (p. 80); se nada
serve, teoria-based (Fig. 3.1, p. 81); em lugares escolhidos por suas características,
controle sintético (p. 65); combinar com processo/teoria para explicar mecanismos
(p. 58).

---

## 3. ADB — White e Raitzer (2017)

### 3.1 Avaliação de impacto, avaliação e análise econômica

- Avaliação no ADB é em geral **de processo** (normativa, qualitativa); avaliação de
  impacto é pesquisa **positiva** sobre efeitos causais (p. 13).
- Análise econômica é sobretudo **ex ante**, com efeitos previstos ou assumidos; a
  avaliação de impacto dá estimativas rigorosas desses efeitos e, na preparação, pode-se
  usar evidência de avaliações e revisões sistemáticas de projetos semelhantes
  (p. 14). **Tabela 1.1 (p. 14)**: contribuições da evidência de impacto para cada etapa
  da análise econômica (racional, ACB ex ante e ex post, sensibilidade, distribuição),
  inclusive "evidência sobre pressupostos críticos e passos da cadeia causal a
  monitorar".
- Perguntas de **primeira geração** (funciona?) e de **segunda geração** (qual desenho
  funciona melhor?) (p. 5-8).
- Avaliação no ciclo do projeto (Fig. 1.2, p. 11-13): pensar cedo; aleatorização precisa
  estar no desenho; linha de base fortalece qualquer estimativa.

### 3.2 Teoria da mudança (cap. 2, p. 20-29)

- ToC = como insumos (recursos, pessoas, **mudanças regulatórias ou de política**) levam
  a resultados e impactos, com os **pressupostos** que precisam valer; identifica
  indicadores e "**contrateorias**" (efeitos não planejados) (p. 21). Árvores de
  problemas ajudam (p. 21).
- Ir além dos "silos": ligar **cada atividade a produtos e resultados específicos** —
  muitas cadeias, não uma (p. 21); pressupostos escritos abaixo do diagrama (Fig. 2.1,
  p. 22); dimensão temporal (p. 23).
- **Funil de atrito** (Fig. 2.2, p. 23; White, 2013): taxas de participação e efeitos
  **diminuem ao longo da cadeia**, e superestimá-los produz **amostras pequenas demais**.
  Pontos de atrito típicos (p. 24): conhecimento do programa, querer participar
  (custos/benefícios privados, desconfiança), poder participar, transferência de
  conhecimento efetiva, mudança de comportamento, insumos complementares, frequência do
  efeito.
- Sustentabilidade e difusão em S; primeiros aderentes diferem dos tardios (p. 25).
- **Modelo de mudança comportamental** (Tabela 2.1, p. 26): resultado pretendido | ator
  que deve mudar | mudança necessária | indicadores.
- Externalidades e consequências não intencionais (p. 26).
- **Sete passos** (p. 26-27): (i) análise de contexto (problema, causas,
  consequências); (ii) intervenção, objetivos e resultados; (iii) passos da cadeia
  causal; (iv) indicadores ao longo da cadeia; (v) pressupostos; (vi) canais por
  grupo/resultado; (vii) **validar e revisar com *stakeholders*** (Box 2.1: *vouchers*
  nas Filipinas revelaram efeito sobre não beneficiários, p. 27).
- Aplicação (p. 28-29): selecionar perguntas e variáveis; triar relações contra o funil
  de atrito para ver se amostra e efeito bastam.

### 3.3 Conceitos centrais (cap. 3, p. 31-45)

- Impacto = Y¹_{t+1} − Y⁰_{t+1} (eq. 3.1, p. 32). Comparações reflexivas (antes-depois) e
  transversais ingênuas são confundidas (p. 33).
- Comparação vs controle; **equilíbrio** (tabela de balanço) e **mecanismo de
  atribuição** (p. 33-34, Box 3.1). Taxonomia: RCT; não experimentais — experimentos
  naturais, quase-experimentos (DD, PSM, RDD), abordagens por regressão (VI, tratamento
  endógeno, *switching*, duplamente robusto) (p. 35-36).
- Vieses (p. 36-37): **seleção** (por **alocação do programa** e por **autosseleção**);
  **contaminação** (outro programa atua no grupo de comparação — coletar dados sobre
  outras intervenções); **transbordamento/SUTVA** (Rubin, 1980) — prever grupos tratado,
  não tratado exposto e não tratado não exposto.
- ***Large-n* vs *small-n*** (p. 39-40): poder depende sobretudo do **número de unidades
  de atribuição**; com poucos tratados, **controle sintético** ou **série temporal
  interrompida**; para *middle-n*, QCA; para *small-n*, abordagens baseadas na ToC.
- Tempo (p. 40-42): medir cedo demais subestima o impacto; planos **ex ante** são mais
  fortes (linha de base, aleatorização); se só há demanda ex post, escolher o melhor
  desenho possível (p. 42).
- **Unidades de atribuição, tratamento e análise** (p. 42-43; Tabela 3.1): se diferem, o
  desenho é por conglomerados.
- **Estimandos** (p. 43-45): ATE, **ITT**, ATT, ATU, LATE; **ITT = ATT × taxa de
  participação (PR)** (eq. 3.2, p. 44), logo ITT ≤ ATT (eq. 3.3); taxa de participação
  baixa abre uma cunha entre os dois. ATT para accountability do efeito até agora; ATU
  para expansão (p. 44-45). Esperado **ATT > ATE > ATU** se alocação e autosseleção são
  racionais; se não aparecer, suspeitar da identificação ou da focalização (eq. 3.4,
  p. 45).
- **Validade interna e externa** (p. 45); externa melhora com ToC forte e amostra
  representativa.

### 3.4 Desenhos não experimentais (cap. 5, p. 66-92)

Perguntas sobre alocação que antecedem a escolha (p. 67-68): critérios de seleção das
áreas; determinantes da autosseleção; se alocação ou autosseleção dependem de não
observáveis correlacionados com o resultado. Não experimentais exigem **amostras
maiores** que RCT e ficam mais fortes com **linha de base** (p. 68).

| Método | Essência e fórmula | Pressupostos / requisitos | Prós e contras | Páginas |
| --- | --- | --- | --- | --- |
| DD / efeitos fixos | DiD = (Y¹_E − Y¹_B) − (Y⁰_E − Y⁰_B) (eq. 5.2); regressão Y_it = α + β1 W + β2 T + β3 (W×T) + ε (Apêndice 1, p. 160) | **Tendências paralelas** (testável só com ≥2 períodos pré); ameaças: composição, *Ashenfelter dip*, especificação (Ap. 1, nota 3, p. 159) | Simples; gera **ATT**; mais rigoroso com pareamento ou EF | 68-71, 159-162 |
| Controle sintético | Pesos que igualam tendências pré de covariáveis e resultado; inferência por **placebos** | Painel balanceado, tratamento binário, longo pré-período, não tratados até o fim | **Poucos tratados**; relaxa tendências paralelas; menos eficiente que DD se estas valem; ATT | 72-73, 163 |
| PSM | Escore de participação (probit/logit) com variáveis não afetadas pela intervenção; **suporte comum**; vizinho mais próximo, *caliper*, *kernel*; teste de balanço (eq. 5.3, Tabela 5.3) | **Só seleção em observáveis** | "Método de último recurso", possível ex post; ATT, ATU, ATE; crítica de King e Nielsen (2016) | 73-78 |
| Ponderação / duplamente robusto | IPW; AIPW consistente se o escore **ou** a regressão de resultado estiver correto | Seleção em observáveis | Menos sensível a especificação; ATE | 78-79 |
| RDD e série temporal interrompida | Salto na regressão no corte; regra de elegibilidade em variável contínua (linha de pobreza, fronteira administrativa, **escore de ranqueamento de subprojetos**) | Variável de atribuição **não manipulável**; limiar **exclusivo do programa** (ex. Mongólia: mesmo corte em dois programas impede separar efeitos, p. 80-81); *fuzzy* via VI | Controla não observáveis; usa dados administrativos, mas **programas raramente guardam dados dos rejeitados** (p. 83); LATE no corte | 79-84 |
| VI / MQ2E | Z correlacionado com W (**relevância**) e sem efeito direto em Y (**exclusão**) | Instrumento válido derivado do modelo estrutural/ToC | Controla observáveis e não observáveis; LATE; RCT e RDD *fuzzy* são casos de VI | 84-86 |
| Tratamento endógeno (Heckman) e *switching* | Equação de participação com ≥1 instrumento + razão de Mills | Normalidade e estrutura de covariância dos erros | ATE; *switching* dá ATT, ATU e ATE | 87-90 |

**Tabela 5.5 (p. 91)**, resumo — método | tratamento | dados mínimos | corrige seleção
em observáveis | em não observáveis | efeito: DD/EF (painel 2+ períodos; não
observáveis **fixos no tempo**; ATT); controle sintético (painel com várias rodadas
pré; aproximação; ATT); PSM (transversal; não; ATT/ATU/ATE); duplamente robusto
(transversal; não; ATE); RDD (transversal em torno do corte; sim; LATE); VI (com
instrumento; sim; LATE); tratamento endógeno e *switching* (sim, sob hipóteses sobre os
erros; ATE ou ATT/ATU/ATE). Critérios de escolha (p. 91-92): natureza do tratamento
(binário vs contínuo), linha de base, instrumento, seleção em não observáveis (se
variam no tempo, DD também é viesado) e estimando de interesse (ATT para
accountability; ATE para expansão).

### 3.5 Tamanho de amostra e poder (cap. 7, p. 116-128; Ap. 2, p. 190-191)

Fórmulas (conferidas no PDF, p. 121-124):

- **MES** (efeito mínimo detectável) = (t_{α/2} + t_{1−β}) · σ_y · √[1 / (P(1 − P) n)]
  (eq. 7.1, p. 121)
- **n** = (t_{α/2} + t_{1−β})² σ_y² / [MES² P(1 − P)] (eq. 7.2, p. 122) — n é o total
  (tratados + comparação); P = proporção tratada; MES mínimo com P = 0,5.
- **ICC** ρ = S_b² / (S_b² + S_w²) (eq. 7.3, p. 123); valores de 0,2 a 0,3 são comuns
  (p. 124).
- **Efeito de desenho** DE = 1 + (m − 1)ρ (eq. 7.4) e n com conglomerados = n · DE
  (eq. 7.5, p. 124), m = observações por conglomerado.
- **Regra de bolso**: n por braço = 16 / mes², com mes em desvios-padrão (p. 127); para
  conglomerados, **60 (30 + 30) como mínimo grosseiro**, 30 em casos de ICC baixo e MES
  alto (p. 127).

Exemplo do livro reproduzido em `analise/adb_poder_replicacao.py` →
`analise/tabelas/adb_replicacao_poder.csv` (aproximação normal):

| Cálculo | Livro | Reproduzido |
| --- | --- | --- |
| n para MES Rs1.500 (σ = Rs12.000, α = 5%, poder 80%) | 2.000 (p. 122) | 2.009 |
| MES com n = 2.000 | 1.504 | 1.503 |
| n para MES Rs750 | 8.000 | 8.037 |
| MES com n = 8.000 | 752 | 752 |
| Conglomerados, m = 40, ρ = 0,2: n para MES Rs1.500 | 17.800 / 445 conglomerados (p. 124) | 17.682 / 442 |
| MES com 50 conglomerados × 40 obs. | "quase Rs7.000" (p. 124) | **4.460 — não reproduz** |
| Regra 16/mes², mes = 0,5 e 0,1 (por braço) | 64 e 1.600 (p. 127) | 64 e 1.600 (exato z: 63 e 1.570) |

O "quase Rs7.000" é incompatível com a eq. 7.5 e com os demais números do mesmo
exemplo (que reproduzem); **não citar esse valor**.

Lições para o desenho (p. 117, 125-128; Ap. 2): poder se calcula no desenho e é
conferido por terceiro (p. 117); **halving the MES quadruplica n** (p. 122); **número de
conglomerados** pesa mais que observações por conglomerado (Fig. 7.7, p. 125);
**baixa adesão dilui o ITT** e deve entrar na escolha do MES (p. 125); causas de estudos
subdimensionados: ICC subestimado, MES alto demais (metas irrealistas), adesão
otimista, variância subestimada, só um resultado, subgrupos sem poder, atrito
(p. 126-127); +10% para reposição; subgrupos precisam de poder próprio; A/B exige mais
(p. 128); fontes de σ e ρ: avaliações do tema, estudos do país, pesquisas públicas,
revisões sistemáticas (p. 128). **Covariáveis de linha de base aumentam o poder**,
sobretudo o resultado defasado quando é persistente (Ap. 2, p. 190); **hipóteses
múltiplas**: FWER (Bonferroni α/k; melhor Westfall-Young ou Romano-Wolf) ou FDR (Ap. 2,
p. 190-191).

### 3.6 Escolha do desenho e gestão (cap. 8)

**Tabela 8.1 (p. 135)** — abordagem de decisão:

1. Desenho prospectivo? → aleatorização possível? → unidade de atribuição = tratamento e
   análise? e transbordamentos? → RCT simples ou por conglomerados.
2. Experimento natural possível? → experimento natural.
3. Intervenção **universalmente disponível, mas não universalmente adotada**? → há
   encorajamento válido? → **desenho de encorajamento**.
4. Muitas unidades tratadas? Se não: muitos períodos pré e não tratados comparáveis? →
   **controle sintético**; senão, alternativa à avaliação de impacto.
5. Regra de elegibilidade com limiar (inclusive **limiar temporal** de introdução)? →
   aplicada estritamente? → **RDD** (inclusive série temporal interrompida) ou *fuzzy*.
6. Não observáveis afetam a seleção? Se não: há linha de base? → **DD/EF**; senão,
   escore de propensão.
7. Se sim: são **fixos no tempo** e há linha de base? → **DD/EF**.
8. Senão: há restrição identificadora ou instrumento válido? → VI, tratamento endógeno,
   *switching*; senão, alternativas à avaliação de impacto.

Outros pontos: especificar a estratégia de identificação antes de iniciar e prever uma
**estratégia de identificação reserva** (p. 134); oficinas de ToC com *stakeholders*
(p. 134); ética — avaliação raramente cria a população não tratada, usa variação
existente ou sistematiza a atribuição; RCT muitas vezes só altera o **momento** ou
acrescenta incentivo (p. 136); interpretar **tamanho de efeito**, não só significância
(p. 146); **custo-efetividade** para resultado único (Box 8.2, p. 147: ranking muda por
causa do custo); orçamentos ilustrativos (Tabela 8.3, p. 140).

### 3.7 Dados (cap. 6)

Tipos de dados necessários: resultados, variáveis de processo e contexto, **medida de
engajamento** (binária ou dose) e atividade do programa, mais variáveis de
participação para desenhos não experimentais (p. 97-98). Fontes: censo, pesquisas,
SIG/sensoriamento, **dados administrativos**, dados em tempo real; ***piggybacking***
em pesquisa nacional com amostra de reforço (p. 98-100). Terminologia de linha de
base, *midline*, *endline*, painel (Box 6.1, p. 100).

### 3.8 O que o ADB diz sobre avaliar sem aleatorização

Avaliação rigorosa continua possível (mensagem-chave, p. 66): depende de entender a
**alocação**, de ter **antes e depois** para tratados e não tratados e de dados sobre
outros determinantes do resultado; hipóteses condicionantes são mínimas quando há
**regra de corte clara e linha de base** (p. 66); cada método estima um parâmetro para
uma população diferente (p. 66, 91-92).

---

## 4. Síntese comparativa

| Tema | Itaú (2017) | Magenta (2026) | ADB (2017) |
| --- | --- | --- | --- |
| Avaliação de desenho / ex ante | Ex ante, percurso, encerramento; resultados e magnitude definidos no desenho (p. 15, 22-24) | Perguntas "antes"; ROAMEF; SMART; planejar cedo (p. 18-23) | IE vs análise econômica ex ante; 1ª e 2ª geração (p. 5-14) |
| Teoria da mudança | Menção (p. 15, 33 "marco lógico") | Seção própria, Fig. 2.2, teoria negativa (p. 44-47) | Capítulo próprio, funil de atrito, 7 passos (p. 20-29) |
| Tipos e proporcionalidade | Usos interno/externo (p. 33-35) | 3 tipos; proporcionalidade com 4 critérios (p. 28-31) | Processo vs impacto (p. 13) |
| Quase-experimentos | Formalização das hipóteses (cap. 4-7) | Fig. 3.1 e Tab. 3.3 (p. 81-83) | Tab. 5.5 e Tab. 8.1 (p. 91, 135) |
| Poder | Qualitativo (p. 78-81) | Princípios; publicar (p. 83-84) | Fórmulas 7.1-7.5 e regras (p. 121-128) |
| Custo / retorno | VPL, TIR, RCB, RCE, sensibilidade (cap. 8) | VfM: ACB, CEA, SROI, Quatro Es (p. 85-89) | CEA (Box 8.2, p. 147); Tab. 1.1 (p. 14) |

---

## 5. O que usar no artigo da LICC

Lista objetiva, na ordem das seções obrigatórias. Números da LICC abaixo vêm de
`analise/tabelas/licc_status_por_ciclo.csv` e `licc_emd_ilustrativo.csv` (script
`analise/gertler_poder_replicacao.py`, de outra nota) e de
`analise/tabelas/adb_replicacao_poder.csv` (script `analise/adb_poder_replicacao.py`).

### 5.1 Introdução e caracterização (moldura)

1. **Definição** de avaliação de política e os **três tipos** (HM TREASURY, 2026,
   p. 15, 28-29): o artigo faz avaliação de **desenho** (com ToC) + proposta de
   **impacto**; VfM entra só como discussão do custo (renúncia).
2. **Proporcionalidade** (HM TREASURY, 2026, p. 31): justificar por que a LICC merece
   avaliação substantiva pelos critérios (c) custo e (d) potencial de aprendizado. O
   teto de R$ 25 mi (2025) precisa da fonte normativa citada [VERIFICAR fonte do teto];
   afirmar "ausência de avaliação de impacto da LICC" só depois da revisão de literatura
   [VERIFICAR].
3. **Monitoramento ≠ impacto** (BARROS; LIMA, 2017, p. 16-17): as listas da SECULT
   (habilitados, captados) são monitoramento; não isolam a contribuição da LICC.

### 5.2 Avaliação do desenho — critérios citáveis

4. **Resultados e magnitude esperados definidos?** (BARROS; LIMA, 2017, p. 15;
   objetivos SMART, HM TREASURY, 2026, p. 19). Aplicar à Lei 11.246/2021 e à IN
   001/2025: há objetivos mensuráveis e metas? [VERIFICAR no texto das normas].
5. **Alternativa na ausência do programa** (BARROS; LIMA, 2017, p. 19) +
   **adicionalidade** (HM TREASURY, 2026, p. 26-27): o contrafactual de um projeto
   habilitado não é "nenhum financiamento", mas outras fontes (editais estaduais,
   leis federais) e patrocínio que ocorreria de qualquer forma. Hipótese de desenho a
   testar, não fato [VERIFICAR literatura sobre adicionalidade de incentivo fiscal à
   cultura].
6. **Impacto potencial vs efetivo** (BARROS; LIMA, 2017, p. 27-28): a etapa de
   captação é onde o potencial se perde. Dado disponível: por ciclo, habilitados com
   "captação expirada" — 11 de 69 (2022), 34 de 113 (2023), 50 de 123 (2024)
   (`licc_status_por_ciclo.csv`) [VERIFICAR semântica exata de `captacao_expirada` no
   anexo da SECULT: nenhuma captação ou abaixo do mínimo?].
7. **Impacto privado vs social / benefício público** (BARROS; LIMA, 2017, p. 20;
   PEIXOTO, 2017, p. 195): proponentes vs público, território e cadeia cultural.
8. **Intervenção territorial** (HM TREASURY, 2026, p. 64-66): a cota de 10% fora da
   RMGV (IN 001/2025, art. 18) remete a transbordamento, deslocamento e seleção de
   lugares. Cumprimento de cota é "indeterminado" enquanto houver projeto sem
   classificação (CLAUDE.md, regra 3; 182 de 467 linhas sem `enquadramento` e 18 sem
   município nos CSVs de habilitados).
9. **Carteira competitiva de projetos** (HM TREASURY, 2026, p. 63-64): a LICC se parece
   com o "fundo de inovação" — exige **medidas comuns** a todos os projetos, idealmente
   administrativas; hoje não há medida de resultado comum publicada [VERIFICAR].

### 5.3 Teoria da mudança da LICC (quadro/figura)

10. **Formato**: Fig. 2.2 do Magenta (p. 46) — insumos → produtos → resultados →
    impacto, com pressupostos em cada elo e fatores de contexto; **cadeias separadas
    por atividade** (WHITE; RAITZER, 2017, p. 21); **contrateorias / teoria negativa**
    (WHITE; RAITZER, 2017, p. 21; HM TREASURY, 2026, p. 47).
11. **Sete passos** (WHITE; RAITZER, 2017, p. 26-27) como roteiro do texto da seção.
12. **Funil de atrito** (WHITE; RAITZER, 2017, p. 23-24) adaptado: proponentes
    elegíveis → inscritos → **habilitados** → **captam** → executam → prestam contas →
    resultados. Só os estágios habilitado/captação têm dado oficial; os demais ficam
    **ausentes, não zero** (CLAUDE.md, regra 1).
13. **Modelo de mudança comportamental** (Tabela 2.1, WHITE; RAITZER, 2017, p. 26) como
    quadro: empresa contribuinte (decide patrocinar e deduz ICMS), proponente (inscreve,
    capta, executa), SECULT/comissão (habilita, fiscaliza), público (frequenta).
    Pressupostos a explicitar: empresas respondem ao incentivo; patrocínio não
    substitui o que já fariam; projetos captados diferem dos não captados por mérito e
    não só por rede de contatos [hipóteses].

### 5.4 Proposta de avaliação de impacto

14. **Rota de decisão** (quadro): responder a Tabela 8.1 do ADB (p. 135) e a Fig. 3.1 do
    Magenta (p. 81) para a LICC — aleatorização da política: não; experimento natural:
    [VERIFICAR]; muitas unidades tratadas: sim (projetos; municípios); limiar de
    elegibilidade: só se a habilitação usar nota de corte [VERIFICAR IN/editais];
    seleção por não observáveis (qualidade do projeto, rede do proponente com
    patrocinadores): provável → DD/EF com linha de base ou instrumento.
15. **Desenhos candidatos** (com pressupostos do Itaú e da Tabela 5.5 do ADB):
    - **D1, intra-habilitados**: captou (concluído/em execução) vs captação expirada;
      unidade projeto/proponente; estimando: efeito de receber patrocínio entre
      habilitados (ATT). Seleção pelo patrocinador em não observáveis → exigir
      resultados pré-período do proponente e usar **DD/EF** (FOGUEL, 2017, p. 89-104)
      ou **pareamento + DD** (H3, PINTO, 2017, p. 130-131). O efeito da **habilitação**
      (ITT) exigiria dados dos inscritos **não habilitados**, que os programas
      raramente guardam (WHITE; RAITZER, 2017, p. 83) [VERIFICAR se a SECULT publica
      inabilitados].
    - **D2, municípios**: DD com entrada escalonada (1º projeto da LICC no município),
      análogo ao PSF de Rocha e Soares (2010) no Box 4.2 (FOGUEL, 2017, p. 107); erros
      por conglomerado (p. 103, nota 15). Com 78 municípios, fica perto do mínimo de
      60 conglomerados da regra do ADB (p. 127). A literatura recente de DD escalonado
      não está nesses guias [VERIFICAR e citar à parte].
    - **D3, estado**: **controle sintético** ES vs outras UFs para resultados culturais
      agregados (FOGUEL, 2017, p. 105-106; WHITE; RAITZER, 2017, p. 72-73; HM TREASURY,
      2026, p. 65, 83) — exige pré-período longo e *donor pool* sem mudança semelhante
      [VERIFICAR quais UFs mudaram leis de incentivo no período e se o ES tinha lei
      anterior].
    - **D4, RDD**: só se existir nota de corte na habilitação ou regra de ranqueamento
      nas cotas; fronteira da RMGV é candidata fraca porque o limiar não é exclusivo da
      LICC (WHITE; RAITZER, 2017, p. 80-81) [hipótese].
    - **D5, prospectivo com encorajamento**: sortear entre habilitados uma divulgação
      ativa a potenciais patrocinadores, usada como instrumento para a captação
      (LATE; PINTO, 2017, cap. 6; encorajamento em FOGUEL, 2017, p. 62-63; WHITE;
      RAITZER, 2017, p. 135-136). Não altera o mecanismo da lei; é instrumento de
      avaliação [opcional].
    - Complemento **teoria-based** (análise de contribuição, QCA para 10-50 casos) para
      resultados sem medida quantitativa (HM TREASURY, 2026, p. 58-61, 77-78).
    - Prever **estratégia reserva** (WHITE; RAITZER, 2017, p. 134).
16. **Estimandos**: ITT (habilitação como oferta) vs ATT (captação como adesão),
    **ITT = ATT × PR** (WHITE; RAITZER, 2017, p. 44). PR aproximada por
    (concluído + em execução)/habilitados em `licc_status_por_ciclo.csv`: 58/69 (2022),
    79/113 (2023), 61/123 (2024, com 12 ainda captando) [VERIFICAR semântica dos
    status antes de usar como taxa de captação].
17. **Poder** (quadro com fórmulas 7.1, 7.2, 7.4, 7.5 do ADB, p. 121-124, iguais às dos
    slides da disciplina):
    - EMD ilustrativo no nível de projeto, ciclos 2022-2024 empilhados (198 vs 95):
      **0,35 dp** com poder 80% e 0,405 dp com 90% (`licc_emd_ilustrativo.csv`) → só
      efeitos moderados a grandes são detectáveis.
    - Diluição do ITT: para detectar ATT de 0,2 dp, n total de **1.602 (PR = 0,7)** a
      **2.180 (PR = 0,6)** (`adb_replicacao_poder.csv`), muito acima dos 305 habilitados
      de 2022-2024 → proposta deve assumir baixa potência no ITT e priorizar ATT com
      linha de base.
    - Ajustes a declarar: covariáveis de linha de base (Ap. 2, p. 190), Bonferroni para
      vários resultados (p. 190-191), +10% de reposição e poder por subgrupo (p. 128),
      ICC de fonte comparável (p. 124, 128). Fatores qualitativos do Itaú (FOGUEL, 2017,
      p. 78-81) na redação.
    - Calibrar o poder ao risco (gasto público significativo) e **publicar/pré-registrar
      a análise de poder** (HM TREASURY, 2026, p. 66-67, 84).
18. **Dados**: priorizar administrativos e de monitoramento (HM TREASURY, 2026,
    p. 100-102); **vincular bases por identificador** (CNPJ dos patrocinadores está na
    coluna `aportes` de `captados-2025.csv`; CNPJ/CPF dos proponentes não está nos CSVs)
    (p. 112); propor **questionário obrigatório** a todos os inscritos, inclusive não
    captados, como requisito de dados (p. 124) — mudança de coleta, não de mecanismo.
19. **Ameaças à validade** (WHITE; RAITZER, 2017, p. 36-37, 45; FOGUEL, 2017, p. 91):
    contaminação por outros programas culturais simultâneos (fontes federais do mesmo
    período) [VERIFICAR datas e valores no ES]; transbordamento entre municípios
    vizinhos (SUTVA); choques idiossincráticos pós-2021 (pandemia e retomada).

### 5.5 Renúncia fiscal como custo (discussão de VfM)

20. Benefício = valor monetário do impacto e só existe depois da avaliação de impacto
    (PEIXOTO, 2017, p. 196) → o artigo **não** calcula VPL/RCB da LICC; propõe o
    **arcabouço** de custo-efetividade: RCE = impacto / custo econômico (eq. 9,
    p. 207-208), porque resultados culturais são difíceis de monetizar.
21. **Custo econômico = contábil + oportunidade** (PEIXOTO, 2017, p. 200). Inferência
    nossa (não está nos guias): para o Estado, o custo da LICC inclui o ICMS renunciado,
    cujo custo de oportunidade é o uso alternativo da receita, mais custos
    administrativos (SECULT, SEFAZ, comissão) e o tempo dos proponentes; do lado do
    benefício, descontar o patrocínio que ocorreria sem incentivo (adicionalidade, HM
    TREASURY, 2026, p. 26-27). [VERIFICAR na Lei 11.246/2021 o percentual dedutível do
    ICMS e se há contrapartida da empresa; VERIFICAR se a LRF, art. 14, exigiu
    estimativa de impacto da renúncia — seria a "appraisal" a comparar, HM TREASURY,
    2026, p. 85.]
22. **Quatro Es**, inclusive **equidade** (HM TREASURY, 2026, p. 89): dimensão
    territorial (RMGV vs interior) e de proponentes.
23. **Sensibilidade**: univariada e por cenários 3^x − 1 (PEIXOTO, 2017, p. 209-211);
    taxa de desconto real (p. 199-200); comparar só com políticas de objetivo e público
    semelhantes (p. 203), por exemplo editais de gasto direto [hipótese de comparação].

### 5.6 Quadros e figuras candidatos (com fonte)

| # | Quadro/figura | Adaptar de |
| --- | --- | --- |
| Q1 | Perguntas de avaliação da LICC por tipo (processo, impacto, VfM) | HM TREASURY (2026), Tab. 2.2, p. 52-53 |
| Q2 | Teoria da mudança da LICC com pressupostos | HM TREASURY (2026), Fig. 2.2, p. 46; WHITE e RAITZER (2017), Fig. 2.1, p. 22 |
| Q3 | Funil de atrito da LICC com os números por ciclo disponíveis | WHITE e RAITZER (2017), Fig. 2.2, p. 23 |
| Q4 | Modelo de mudança comportamental (atores da LICC) | WHITE e RAITZER (2017), Tab. 2.1, p. 26 |
| Q5 | Viabilidade de (quase-)experimento para a LICC | HM TREASURY (2026), Tab. 2.3, p. 57-58 |
| Q6 | Rota de decisão do desenho respondida para a LICC | WHITE e RAITZER (2017), Tab. 8.1, p. 135 (preferível à Fig. 3.1 do Magenta, que tem o erro apontado em 2.6) |
| Q7 | Desenhos candidatos × pressupostos × estimando × dados | WHITE e RAITZER (2017), Tab. 5.5, p. 91 + hipóteses do Itaú (cap. 4-7) |
| Q8 | Poder: fórmulas e EMD por recorte | WHITE e RAITZER (2017), eq. 7.1-7.5, p. 121-124; tabelas em `analise/tabelas/` |
| Q9 | Custos e benefícios da LICC para custo-efetividade | PEIXOTO (2017), p. 200, 207-208; HM TREASURY (2026), Tab. 3.4-3.5, p. 87-89 |

### 5.7 Fórmulas prontas (com fonte)

- Viés de seleção: R = EMPT + V, V = E[Y(0)|T=1] − E[Y(0)|T=0] (FOGUEL, 2017, eq. 10,
  p. 50).
- DD: β_DD = {E[Y|T=1,t=1] − E[Y|T=1,t=0]} − {E[Y|T=0,t=1] − E[Y|T=0,t=0]} (FOGUEL,
  2017, eq. 1, p. 92); regressão Y_it = α + γT_i + ρ dt_t + β(T_i·dt_t) + ε_it (eq. 4,
  p. 96); EF Y_it = X′_it α + ρ_t + β D_it + μ_i + ε_it (eq. 11, p. 101).
- Pareamento + DD: hipótese H3 (PINTO, 2017, p. 130).
- Wald/LATE (PINTO, 2017, eq. 6.8, p. 154).
- ITT = ATT × PR (WHITE; RAITZER, 2017, eq. 3.2, p. 44).
- MES, n, ICC, DE (WHITE; RAITZER, 2017, eq. 7.1-7.5, p. 121-124); n por braço ≈
  16/mes² (p. 127).
- VPL, TIR, RCB, RCE, cenários 3^x − 1 (PEIXOTO, 2017, eq. 5-10, p. 204-211).

### 5.8 Paráfrases citáveis (sem transcrição literal)

- Programas devem declarar não só quais resultados pretendem mudar, mas a magnitude
  esperada da contribuição (BARROS; LIMA, 2017, p. 15).
- O impacto estimado mede o valor adicionado em relação às alternativas que ocupariam o
  espaço do programa (BARROS; LIMA, 2017, p. 19).
- A avaliação deve ser proporcional; alto custo, alta incerteza e alto potencial de
  aprendizado justificam avaliação mais robusta (HM TREASURY, 2026, p. 31).
- Taxas de participação e efeitos diminuem ao longo da cadeia causal, e ignorar isso
  leva a amostras pequenas demais (WHITE; RAITZER, 2017, p. 23).
- Com adesão parcial, o efeito de intenção de tratar é o efeito sobre os tratados
  multiplicado pela taxa de participação (WHITE; RAITZER, 2017, p. 44).
- Em desenhos por conglomerados, o número de conglomerados importa mais para o poder
  do que o número de observações em cada um (WHITE; RAITZER, 2017, p. 116, 124-125).
- Associações estatísticas geradas por IA não estabelecem causalidade (HM TREASURY,
  2026, p. 130).

### 5.9 Pendências [VERIFICAR]

- Edição do Magenta a citar (2026, a do material, recomendada).
- Semântica dos status `captacao_expirada`, `concluido`, `em_execucao` no anexo da
  SECULT.
- Se a SECULT publica inscritos não habilitados e se a habilitação usa nota de corte.
- Teto anual de renúncia e percentual dedutível do ICMS na Lei 11.246/2021 e normas
  complementares; existência de estimativa de impacto da renúncia (LRF, art. 14).
- Acesso e recorte de dados administrativos de resultado (emprego formal cultural,
  público) por município e por CNPJ.
- Literatura sobre adicionalidade de incentivos fiscais à cultura e sobre DD
  escalonado (fora destes guias).
