---
id: 03-gertler
fonte: Gertler et al. (2018), "Avaliação de Impacto na Prática", 2. ed. (BID/Banco Mundial)
arquivo_pdf: Avaliação-de-impacto-na-prática-Segunda-edição (1).pdf (raiz do projeto)
arquivo_txt: disciplina/txt/Avaliação-de-impacto-na-prática-Segunda-edição (1).txt
paginacao: "p. N" = página impressa do livro. Página do PDF = p. impressa + 30 (conferido em p. 3, 71, 211, 243, 277, 313).
leitura: capítulos 1-13 e 15-17 lidos no texto extraído; quadros 11.1, 12.1, 12.2, 15.4, 15.5 e 15.6 conferidos na imagem do PDF; capítulo 14 (disseminação) só sumarizado pelo sumário.
script: analise/gertler_poder_replicacao.py (replica os quadros 15.2-15.6 e tabula os dados da LICC)
licenca_da_obra: CC BY 3.0 IGO (p. iv) — adaptação permitida com atribuição
data: 2026-09-23
---

# 03 — Gertler et al. (2018): *Avaliação de impacto na prática*

## Referência (ABNT NBR 6023)

GERTLER, Paul J.; MARTÍNEZ, Sebastián; PREMAND, Patrick; RAWLINGS, Laura B.;
VERMEERSCH, Christel M. J. **Avaliação de impacto na prática**. 2. ed.
Washington, DC: Banco Interamericano de Desenvolvimento; Banco Mundial, 2018.
Disponível em: https://openknowledge.worldbank.org/handle/10986/25030. Acesso
em: 23 set. 2026.

Notas de verificação:

- Autoria, título, edição, editoras, ano e forma de citação sugerida conferidos
  na página de direitos (p. iv, PDF p. 6). Tradução da edição inglesa de 2016
  (*Impact Evaluation in Practice, Second Edition*), conforme a mesma página.
- ISBN (papel) 978-1-4648-0889-0; eISBN 978-1-4648-1264-4 (p. iv).
- O DOI impresso na p. iv (10.1596/978-1-4648-0889-0) **não resolve**: doi.org
  e Crossref responderam "não encontrado" em 23/09/2026. Por isso o DOI foi
  deixado fora da referência. [VERIFICAR] se há DOI válido para a edição em
  português.
- O handle 10986/25030 redireciona para o Open Knowledge Repository do Banco
  Mundial (teste HTTP 302 em 23/09/2026); a página do registro não pôde ser
  lida (conexão recusada), então os metadados do repositório não foram
  conferidos. [VERIFICAR] antes de usar o link no artigo.
- Citação no texto: (Gertler *et al.*, 2018, p. X). Abaixo, "G" = este livro.

## O que tirar daqui para o artigo (resumo executivo)

1. **A regra de alocação escolhe o método, não o contrário** (G, p. 9-10, 71,
   208). Três perguntas operacionais — recursos (há excesso de demanda?),
   critério de elegibilidade (há índice contínuo com ponto de corte?) e tempo
   de implementação (em fases ou imediata?) — levam ao quadro 11.1 (p. 211),
   reproduzido na seção 6.
2. **Contrafactual válido** exige grupo de comparação que (i) seja igual em
   média na ausência do programa, (ii) não seja afetado pelo programa e (iii)
   reagiria ao programa como o tratado (p. 58-59). As comparações antes-depois
   e com-sem (inscritos x não inscritos) são "contrafactuais falsos" (p. 60-68).
3. **Hierarquia de pressupostos**: seleção aleatória < VI < RDD < DD <
   pareamento, em força crescente de hipóteses; o pareamento isolado é o mais
   frágil (p. 143, 168-169, 218). Preferir o método que cabe nas regras e exige
   as hipóteses mais fracas e menos dados (p. 208, 218).
4. **Poder estatístico** em cinco perguntas (+ uma para conglomerados), com
   efeito mínimo detectável definido como questão de política pública, poder
   0,8 a 0,9, α = 5% (p. 305-309); o número de conglomerados pesa mais do que o
   número de indivíduos (p. 314-315).
5. **Para a LICC**: a alocação do benefício entre habilitados é feita por
   empresas patrocinadoras, não pelo Estado, e não usa índice com ponto de
   corte. No quadro 11.1 isso a coloca na coluna "excesso de demanda, sem
   ordenação por índice" (células A2/B2). Dentro das regras atuais, o livro
   aponta **diferença em diferenças com pareamento** (retrospectivo, com dados
   administrativos) e **promoção aleatória como variável instrumental**
   (prospectivo). Descarta antes-depois, com-sem e pareamento isolado. Seleção
   aleatória e RDD só caberiam com mudança de regra ou com dado que não temos
   (seção 11).

---

## 1. Por que avaliar e o que é avaliação de impacto (cap. 1)

- **Monitoramento x avaliação** (p. 8). Monitoramento é contínuo, usa sobretudo
  dados administrativos e acompanha insumos, atividades e produtos. Avaliação é
  análise periódica e objetiva de programa planejado, em curso ou concluído,
  para responder perguntas específicas sobre desenho, implementação ou
  resultados.
- **Três tipos de pergunta** (p. 8, citando Imas e Rist, 2009): *descritivas*
  (o que está ocorrendo), *normativas* (o que ocorre x o que deveria ocorrer) e
  *de causa e efeito* (atribuição). A avaliação de impacto responde só ao
  terceiro tipo: "qual é o impacto (ou efeito causal) de um programa sobre um
  resultado de interesse?" (p. 9).
- **A escolha do método depende das características operacionais** do
  programa, em particular dos recursos, dos critérios de elegibilidade e do
  cronograma (p. 9-10). Regras equitativas, transparentes e que permitem
  prestação de contas quase sempre admitem bom desenho, **desde que a avaliação
  seja planejada cedo** (p. 10).
- **Prospectiva x retrospectiva** (p. 10-12). A prospectiva é desenhada junto
  com o programa, tem linha de base e define tratamento e comparação antes da
  intervenção. É mais robusta por três razões (p. 10-11). A retrospectiva
  depende de regras claras de alocação e de dados antes e depois para os dois
  grupos, "nunca é garantida" e costuma recorrer a métodos quase-experimentais,
  com pressupostos mais fortes e evidência mais contestável (p. 11-12).
  **A LICC está neste segundo caso** para os ciclos 2022-2025.
- **Eficácia x efetividade** (p. 12-13). Eficácia: funciona em condições
  ideais, como em piloto controlado. Efetividade: funciona em condições
  normais, generalizável se a expansão usar as mesmas estruturas (validade
  externa).
- **Abordagens complementares** (p. 14-22). Monitoramento (p. 15); simulações
  ex-ante (p. 15-16); métodos mistos, com as três abordagens de Creswell
  (paralelo convergente, sequencial explicativa, sequencial exploratória; p.
  18); avaliação de processo, cujos elementos estão listados na p. 20;
  custo-benefício e custo-efetividade (p. 20-21). Aplicar avaliação de impacto
  a programa com processos não validados arrisca desperdiçar recursos (p. 20).
- **Quando vale a pena avaliar** (p. 29-31). Perguntas-guia: o que está em
  jogo, se já existe evidência e se há recursos. A intervenção deve ser
  inovadora, replicável, estrategicamente relevante, não testada e influente
  (p. 30).

## 2. Teoria da mudança, cadeia de resultados, perguntas e indicadores (cap. 2)

### 2.1 Teoria da mudança (p. 36-38)

Descrição de como a intervenção deve gerar os resultados: a lógica causal, as
condições e os pressupostos necessários para a mudança, mapeados em trajetórias
lógico-causais. O melhor momento para construí-la é o início da concepção,
envolvendo as partes interessadas e a literatura sobre programas semelhantes
(p. 36-37). Exemplo: Piso Firme, no México (boxe 2.1, p. 37-38).

### 2.2 Cadeia de resultados (p. 38-40; figura 2.1, p. 39)

A cadeia de resultados é uma das formas de descrever a teoria da mudança, ao
lado de modelos teóricos, marcos lógicos e modelos de resultados. Todas contêm
cadeia causal, influências externas e hipóteses principais (p. 38). O livro
adota a cadeia por ser "o modelo mais simples e mais claro" (p. 38).

| Elemento | Definição (G, p. 38-39) | Controle da agência |
| --- | --- | --- |
| Insumos | Recursos à disposição do projeto: pessoal, orçamento | Sim (oferta) |
| Atividades | Ações que convertem insumos em produtos | Sim (oferta) |
| Produtos | Bens e serviços tangíveis gerados pelas atividades | Sim (oferta) |
| Resultados | Efeitos de curto e médio prazo após o uso dos produtos pela população | Não completamente (demanda + oferta) |
| Resultados finais | Objetivos de longo prazo, afetados por múltiplos fatores | Não (demanda + oferta) |

Insumos, atividades e produtos formam a **implementação**, objeto de
monitoramento. Resultados e resultados finais dependem do comportamento dos
beneficiários e são o objeto típico da avaliação de impacto (p. 39). Uma boa
cadeia expõe hipóteses e riscos implícitos e identifica elos fracos do desenho
(p. 39-40).

### 2.3 Perguntas de avaliação (p. 40-45)

- A pergunta deve ser formulada como **hipótese testável e quantificável** da
  diferença entre tratamento e comparação (p. 40, 42).
- Três focos possíveis: efeito clássico do programa sobre resultados finais,
  custo-efetividade relativa de formas de implementação, ou inovação de
  desenho (p. 40-41).
- **Avaliação de mecanismo** (boxe 2.2, p. 41-42, citando Ludwig, Kling e
  Mullainathan, 2011): testa um elo causal da cadeia em vez do programa
  inteiro. É mais barata e, se o mecanismo falha, o programa dificilmente
  funciona.
- Exemplos: currículo de matemática (boxe 2.3, p. 43-44) e HISP (p. 44-45),
  cuja pergunta é "qual o efeito do HISP sobre as despesas diretas com saúde
  das famílias pobres?" (p. 45).

### 2.4 Indicadores e SMART (p. 46-48)

- Os indicadores determinam o sucesso do programa e alimentam o cálculo de
  poder (p. 46). Gestores e pesquisadores precisam concordar sobre os
  indicadores e o **tamanho de efeito esperado**. Amostras pequenas geram
  avaliações de "baixo poder" (p. 46).
- **SMART** (p. 47): **E**specíficos (medem com a maior acurácia possível),
  **M**ensuráveis (dados facilmente obtidos), **A**tribuíveis (vinculados às
  dimensões do programa), **R**ealistas (dados em tempo, frequência e custo
  razoáveis), **D**irecionados à população-alvo.
- Deve haver indicadores **ao longo de toda a cadeia**, não só de impacto; sem
  isso a avaliação vira "caixa preta" (p. 47).
- **Lista de verificação para obter os dados** (p. 48, adaptada de PNUD,
  2009): indicadores especificados e SMART; fonte de cada indicador;
  frequência; responsável pela coleta; responsável pela análise; recursos;
  documentação e anonimato; riscos.

## 3. Inferência causal e contrafactual (cap. 3)

- **Fórmula básica** (p. 54): Δ = (Y | P = 1) − (Y | P = 0). O impacto causal
  Δ do programa P sobre Y é a diferença entre o resultado com o programa e o
  resultado da **mesma unidade, no mesmo momento**, sem o programa.
- **Problema do contrafactual** (p. 55): (Y | P = 0) não é observável para o
  participante e precisa ser estimado. O livro usa o modelo causal de Rubin
  (nota 1, p. 69).
- **Clone perfeito** (fig. 3.1, p. 57): não existe no nível individual. A
  solução é passar para o nível de grupo e construir grupos estatisticamente
  idênticos em média (p. 57-58).
- **Três condições do grupo de comparação válido** (p. 58-59):
  1. mesmas características médias do tratado na ausência do programa;
  2. não é afetado, direta ou indiretamente, pelo programa;
  3. reagiria ao programa da mesma forma que o grupo de tratamento.
- Grupo de comparação inválido gera estimativa **enviesada**: o livro chama de
  viés a diferença entre o impacto estimado e o real (p. 60; glossário, p.
  374).
- A nota 2 (p. 69) antecipa que a condição 1 é afrouxada em alguns métodos:
  basta a mesma **tendência** na ausência do programa, como no DD.

## 4. Os dois contrafactuais falsos (cap. 3, p. 60-68)

### 4.1 Antes-depois (reflexivo; p. 60-65)

- Usa o resultado do próprio grupo antes do programa como contrafactual. Supõe
  que, sem o programa, nada teria mudado (p. 60).
- Exemplo do microcrédito e da chuva (fig. 3.3, p. 61): com seca, o
  contrafactual cai para D e o impacto verdadeiro supera os 100 kg; com chuva
  melhor, sobe para C e o impacto é menor. O resultado da linha de base "quase
  nunca" é uma boa estimativa do contrafactual (p. 65).
- HISP: redução de US$ 6,65 (t = −39,76), ou US$ 6,71 com controles (quadros
  3.1-3.2, p. 64-65). Estatisticamente significativo, mas **enviesado**, porque
  não controla choques temporais como a crise financeira e o lançamento de
  medicamentos (p. 64).

### 4.2 Com-sem (inscritos x não inscritos, autosselecionados; p. 65-68)

- **Viés de seleção** (p. 66): surge quando as razões da participação estão
  correlacionadas com os resultados mesmo na ausência do programa. Vale também
  quando a admissão depende de preferências não observadas **dos
  administradores**, como numa entrevista de seleção (p. 66). Garantir
  estimativa livre desse viés é "um dos principais objetivos e desafios" de
  toda avaliação (p. 66).
- HISP: −US$ 14,46 na comparação simples e −US$ 9,98 com controles (quadros
  3.3-3.4, p. 67-68). Controlar observáveis não resolve o viés vindo de não
  observáveis.

## 5. Os métodos (caps. 4-10)

### 5.1 Seleção aleatória (cap. 4)

- **Princípio** (p. 71-72): as regras de seleção do programa são o parâmetro
  fundamental para escolher o método; o método se ajusta a elas, e não o
  inverso. O sorteio entre elegíveis é regra justa e transparente e
  "padrão-ouro" da avaliação (p. 72).
- **Por que funciona** (p. 76-77): com número suficiente de unidades, o sorteio
  equilibra observáveis **e não observáveis** (motivação, preferências). O
  impacto é a diferença de médias (fig. 4.5, p. 90).
- **Validade interna x externa** (p. 81-83; fig. 4.2): a **seleção** aleatória
  garante a validade interna; a **amostragem** aleatória da população elegível
  garante a validade externa. São duas aleatorizações com finalidades
  distintas (p. 82; boxe 15.1, p. 297-299).
- **Quando usar** (p. 83-84): (1) população elegível maior que as vagas
  (excesso de demanda); (2) implantação gradual, sorteando a ordem de entrada
  (*phase-in*).
- **Como** (fig. 4.3, p. 85; p. 84-87): definir elegíveis, selecionar a amostra
  de avaliação e aleatorizar. A regra deve ser fixada **antes** de gerar os
  números aleatórios, pública, documentada e replicável, com semente (p. 87;
  nota 5, p. 96).
- **Nível da aleatorização** (p. 87-90): níveis agregados, como estados ou
  regiões, têm poucas unidades e não equilibram; níveis baixos aumentam
  transbordamentos e cumprimento parcial. Regra geral: o nível mais baixo em
  que os transbordamentos sejam aceitáveis (p. 90).
- **Lista de verificação** (p. 91): equilíbrio na linha de base; cumprimento
  (se houver falha, usar VI); tamanho dos grupos (se pequeno, combinar com
  DD); interdependência entre unidades.
- **Exemplos**: Progresa (boxe 4.2, p. 78); Uganda, 535 propostas elegíveis
  para financiamento, 265 sorteadas para tratamento e 270 para comparação
  (boxe 4.3, p. 78-79). O caso de Uganda é **o mais próximo da LICC**:
  propostas avaliadas por mérito, excesso de demanda e financiamento a projetos.
  Ver também boxes 4.1 e 4.4-4.6.
- HISP: balanceamento (quadro 4.1, p. 93) e impacto de −US$ 10,14, ou −US$ 10,01
  com controles (quadros 4.2-4.3, p. 94). É a referência "verdadeira" do caso.

### 5.2 Variáveis instrumentais, cumprimento parcial e promoção aleatória (cap. 5)

- **Ideia** (p. 99-100): uma fonte externa de variação, fora do controle do
  indivíduo, que afeta a probabilidade de participar mas não está associada às
  suas características. Serve a programas com cumprimento parcial, adesão
  voluntária ou cobertura universal.
- **Estimandos** (p. 101-105):
  - **ATE**: efeito médio com cumprimento completo;
  - **ITT** (intenção de tratar): compara quem recebeu e quem não recebeu a
    **oferta**, independentemente da participação;
  - **TOT** (tratamento no tratado): efeito sobre quem de fato participou, um
    caso particular de LATE quando o descumprimento ocorre só no tratamento
    (p. 105);
  - **LATE**: efeito para os cumpridores (p. 105).
- **Tipos de unidade** (p. 105-106): *Participa se for selecionado*
  (cumpridores), *Nunca* e *Sempre*. Os tipos não são observáveis
  individualmente, mas suas proporções são dedutíveis das taxas de inscrição
  (p. 107-109).
- **Cálculo do LATE** (fig. 5.2, p. 108-109): LATE = ITT / (diferença nas taxas
  de participação entre os grupos). Exemplo: ITT = 110 − 70 = 40; participação
  de 90% x 10%, diferença de 80 p.p.; LATE = 40/0,8 = 50. Na prática,
  estima-se por MQ2E (nota 2, p. 124).
- **Duas condições da VI válida** (p. 111): **exogeneidade** (não
  correlacionada com as características dos grupos e sem efeito direto sobre o
  resultado) e **relevância** (afeta a participação de forma diferente entre os
  grupos).
- **Interpretação** (p. 111-112): o LATE vale só para os cumpridores e **não se
  extrapola** para os tipos Nunca e Sempre.
- **Promoção aleatória, ou desenho de encorajamento** (p. 113-122): em
  programas abertos, sorteia-se quem recebe um **encorajamento** adicional
  (informação, visita, incentivo). As condições estão na p. 116: (1) grupos
  encorajados e não encorajados semelhantes; (2) a promoção não afeta
  diretamente o resultado; (3) a promoção altera substancialmente a adesão.
  Exemplo numérico: inscrição de 80% x 30% e ΔY = 40, logo LATE = 40/0,5 = 80
  (fig. 5.4, p. 118-119). No HISP: −3,87/0,4078 = −US$ 9,49 (quadro 5.1, p.
  121); por MQ2E, −9,50 e −9,74 (quadro 5.2, p. 122).
- **Limitações** (p. 122-123): a promoção precisa ser efetiva e o LATE é o dos
  que "participam se encorajados", que podem diferir justamente do público
  pretendido (os Sempre).
- **Lista de verificação** (p. 123): equilíbrio da linha de base; efeito da
  promoção sobre a adesão; ausência de efeito direto da promoção sobre o
  resultado. A última condição é **não testável** e depende de teoria e
  conhecimento do contexto.
- Exemplos: Vila Sésamo com distância à torre UHF como instrumento (boxe 5.1,
  p. 100-101); vouchers PACES na Colômbia (boxe 5.2, p. 110); SIF na Bolívia
  (boxe 5.3, p. 119-120).

### 5.3 Regressão descontínua — RDD (cap. 6)

- **Aplicação** (p. 125-127): programas que ordenam unidades por **índice
  contínuo** com **ponto de corte** de elegibilidade.
- **Quatro condições** (p. 127):
  1. índice contínuo ou "suave", não categórico;
  2. ponto de corte claramente definido;
  3. ponto de corte **exclusivo** do programa avaliado;
  4. pontuação **não manipulável** por recenseadores, beneficiários, gestores
     ou políticos.
- **Estimativa** (p. 127-129): diferença de resultados logo acima e logo abaixo
  do corte. É um **LATE local** em torno do corte (p. 130, 137).
- **Sharp x fuzzy** (p. 131-132; fig. 6.3): com descumprimento, usa-se o lado
  do corte como instrumento. A estimativa fica ainda mais local, restrita aos
  que participam por causa do critério (p. 138; nota 4, p. 140).
- **Validade** (p. 132-134, 137): teste de **densidade** do índice no corte
  ("concentração" logo abaixo indica manipulação; fig. 6.4, p. 133) e teste de
  ausência de salto em variáveis da linha de base.
- **Limitações** (p. 137-139): responde bem à pergunta sobre expandir ou
  reduzir o programa **na margem**, mas não à pergunta "o programa deve
  existir?" (p. 138). Perde poder por usar só observações perto do corte; deve
  testar sensibilidade à janela e à forma funcional (p. 138-139). Não exige
  excluir elegíveis (p. 130, 139).
- **Lista de verificação** (p. 139-140). HISP: −US$ 9,03 (quadro 6.1, p. 137).
- Exemplos: Colômbia/SISBEN (boxe 6.1, p. 126); PATH na Jamaica (boxe 6.2, p.
  130-131); *tracking* no Quênia (boxe 6.3, p. 133); PRAF em Honduras, com RDD
  em fronteira municipal (boxe 16.2, p. 333).

### 5.4 Diferença em diferenças — DD (cap. 7)

- **Quando** (p. 143): regra de seleção pouco clara, ou nenhum dos três métodos
  anteriores é factível. DD e pareamento exigem pressupostos mais fortes.
- **Fórmula** (fig. 7.1, p. 146; quadro 7.1, p. 147):
  **DD = (B − A) − (D − C)**, em que A e B são o tratamento antes e depois e C
  e D, a comparação antes e depois. Exemplo: (0,74 − 0,60) − (0,81 − 0,78) =
  0,11. Equivale a DD = (B − D) − (A − C) (p. 148).
- **O que elimina** (p. 148-149): diferenças **constantes no tempo** entre os
  grupos, observáveis e não observáveis.
- **Hipótese de igualdade de tendências** (p. 150): na ausência do programa, os
  resultados dos dois grupos evoluiriam em paralelo. Não se prova, porque o
  contrafactual não é observável. Com tendências diferentes, o DD é enviesado
  (fig. 7.2, p. 151).
- **Quatro formas de testar** (p. 151-152):
  1. comparar as tendências **pré-programa**, o que exige ao menos duas
     observações antes do programa e, portanto, **três rodadas** no total
     (p. 151);
  2. **placebo com grupo de tratamento falso**, sabidamente não afetado;
  3. **placebo com resultado falso**, que o programa não deveria afetar;
  4. estimar com **grupos de comparação diferentes** e verificar se o
     resultado se mantém.
  Exemplos: privatização da água na Argentina, com placebo de causas de
  mortalidade não hídricas (boxe 7.3, p. 153); escolas na Indonésia, com
  coortes velhas demais como placebo (boxe 7.4, p. 154).
- **Limitação** (p. 156): qualquer fator que afete desproporcionalmente um dos
  grupos ao mesmo tempo que o programa, e não esteja modelado, enviesa a
  estimativa, mesmo com tendências pré iguais. A lista de verificação está nas
  p. 156-157.
- HISP: −US$ 8,16 (quadros 7.2-7.3, p. 155).
- Exemplo brasileiro: Bolsa Escola e incentivos eleitorais de prefeitos em
  primeiro mandato (boxe 7.1, p. 145, citando De Janvry, Finan e Sadoulet,
  2011).
- Fora do livro: DD com adoção escalonada (tratamentos que começam em anos
  diferentes, como os ciclos da LICC) tem literatura própria posterior que
  Gertler não cobre. [VERIFICAR] em nota específica, antes de qualquer
  referência entrar no artigo.

### 5.5 Pareamento e escore de propensão — PSM (cap. 8)

- **Ideia** (p. 159): construir um grupo de comparação artificial de não
  participantes com características observáveis semelhantes às dos
  participantes. Serve a quase qualquer regra de seleção, desde que exista um
  grupo não participante.
- **Maldição da dimensionalidade** (p. 160; fig. 8.1) e a solução de
  Rosenbaum e Rubin (1983): o **escore de propensão**, probabilidade de
  participar dados os observáveis **da linha de base**, entre 0 e 1 (p. 161).
  Variáveis pós-tratamento enviesam (p. 161, 163-164).
- **Suporte comum** (fig. 8.2, p. 162-163): sem sobreposição nas caudas, o
  efeito vale só no suporte comum (LATE).
- **Seis passos** (p. 163, citando Jalan e Ravallion, 2003): dados comparáveis
  de inscritos e não inscritos; estimar o escore; restringir ao suporte comum;
  achar pares; comparar resultados; tirar a média dos impactos individuais.
- **Três advertências** (p. 163-164): (1) só observáveis entram, e não
  observáveis correlacionados com participação e resultado enviesam; (2) só
  variáveis não afetadas pelo programa; (3) o resultado vale o que valem as
  variáveis usadas, e o mais importante é conhecer **os determinantes da
  inscrição**.
- **DD com pareamento** (p. 164-165), em cinco passos: parear pela linha de
  base, calcular a primeira e a segunda diferenças para cada par, aplicar o DD
  e tirar a média. Remove também os não observáveis fixos no tempo. Exemplos:
  estradas rurais no Vietnã (boxe 8.1, p. 165-166) e Piso Firme (boxe 8.2, p.
  166-167).
- **Controle sintético** (p. 167; boxe 8.3, p. 168): para **uma única unidade
  tratada**, como um país ou região, pondera-se as não tratadas para compor uma
  comparação sintética. Requer longa série temporal (Abadie e Gardeazabal,
  2003, País Basco).
- **Limitações** (p. 168-169): exige bases grandes; pode faltar suporte comum;
  a hipótese de ausência de seleção em não observáveis é "muito forte" e **não
  testável**. O pareamento *ex post* sem linha de base é "muito arriscado"
  (p. 169). É mais confiável quando a regra de seleção e suas variáveis são
  conhecidas (p. 169).
- **Lista de verificação** (p. 174). HISP (quadros 8.1-8.4, p. 171-173):
  −US$ 9,95 com o conjunto completo de variáveis; −US$ 11,35 com o conjunto
  limitado; −US$ 9,41 no DD pareado.

### 5.6 Programas multifacetados e combinações (cap. 10; cap. 11)

- **Níveis de tratamento** (p. 196-198): n níveis pedem n grupos de tratamento
  mais um de comparação.
- **Intervenções múltiplas** (p. 200-203; fig. 10.3): desenho cruzado; todas as
  combinações de n intervenções exigem 2ⁿ grupos (p. 203). Mais comparações
  pedem mais amostra e correção para **testes múltiplos** (nota 3, p. 204).
- **Combinações de métodos**: seleção aleatória + DD quando os grupos são
  pequenos (p. 91); RDD + VI no caso fuzzy (p. 131); pareamento + DD (p.
  164-165); cruzamento de métodos por intervenção, como RDD numa e sorteio na
  outra (p. 203). O plano B é ter um segundo método e linha de base; exemplo:
  sorteio mais promoção aleatória (p. 219).

### 5.7 Desafios transversais (cap. 9)

- **Efeitos heterogêneos** (p. 177-178): subgrupos pequenos exigem amostra
  estratificada.
- **Efeitos comportamentais indesejados** (p. 178-179): Hawthorne, John Henry,
  **antecipação** e **viés de substituição**. Neste último, as unidades de
  comparação encontram programas substitutos por conta própria (p. 178;
  glossário, p. 374).
- **Cumprimento parcial** (p. 179-181): seis formas. Os métodos padrão passam a
  estimar ITT; o LATE se recupera por VI. Não se deve deixar grande fração da
  comparação entrar ou grande fração do tratamento sair (p. 181).
- **Transbordamentos** (p. 181-187), em quatro tipos segundo Angelucci e Di
  Maro (2015): externalidades, interações sociais, efeitos de equilíbrio de
  contexto e **efeitos de equilíbrio geral**, quando o programa altera oferta,
  demanda e preços (p. 182). Transbordamento sobre a comparação viola a
  **SUTVA** (p. 182-183). Uma avaliação com transbordamentos precisa de duas
  perguntas (direta e indireta) e de um grupo de comparação adicional (p.
  186-187). Exemplo de deslocamento no mercado de trabalho da França (boxe
  9.2, p. 183).
- **Atrição** (p. 187-191): ameaça a validade externa e a interna. Dois testes:
  comparar a linha de base de quem saiu com a de quem ficou, e comparar as
  taxas de atrição entre os grupos. Correção possível por ponderação pela
  probabilidade inversa (p. 191).
- **Tempo e persistência** (p. 191-192): os efeitos podem demorar ou persistir,
  e pode ser preciso mais de um acompanhamento.

### 5.8 Quadro-síntese: o mesmo programa (HISP), métodos diferentes

| Método | Estimativa do impacto (US$) | Página |
| --- | --- | --- |
| Antes-depois (simples / multivariada) | −6,65 / −6,71 | 64-65 |
| Inscritos x não inscritos (simples / multivariada) | −14,46 / −9,98 | 67-68 |
| Seleção aleatória (médias / multivariada) | −10,14 / −10,01 | 94 |
| Promoção aleatória, VI (Wald / MQ2E / MQ2E multivariada) | −9,49 / −9,50 / −9,74 | 121-122 |
| RDD (multivariada) | −9,03 | 137 |
| DD (simples = multivariada) | −8,16 | 155 |
| Pareamento (conjunto completo / limitado de variáveis) | −9,95 / −11,35 | 172-173 |
| DD com pareamento | −9,41 | 173 |

Moral pedagógica: os contrafactuais falsos erram para os dois lados. O
pareamento com poucas variáveis se afasta da referência experimental, e com o
conjunto completo se aproxima dela. O limiar de política do HISP era redução
de US$ 10 (p. 62-63), de modo que a escolha do método muda a recomendação.

## 6. As regras operacionais determinam o método (cap. 11)

### 6.1 Princípios (p. 207-210)

- As regras operacionais "podem e devem determinar o método de avaliação — e
  não vice-versa". A avaliação não deve alterar drasticamente regras bem
  definidas em nome de um desenho mais "limpo" (p. 208).
- Os grupos de comparação vêm das unidades **elegíveis que não podem ser
  atendidas** num dado momento (restrição de recursos, excesso de demanda) ou
  das unidades **próximas do ponto de corte** (p. 208).
- **Regras de seleção equitativas, transparentes e responsáveis** (p. 208-209):
  - equitativas: priorizam por indicador de necessidade acordado, oferecem a
    todos ou dão a todos a mesma chance;
  - transparentes: públicas, quantificáveis e observáveis por terceiros;
  - responsáveis: sua execução serve de base para medir o desempenho dos
    gestores.
  Se as regras não são quantificáveis e verificáveis, a equipe nem consegue
  documentar como a seleção ocorreu (p. 209).
- **Três perguntas operacionais** (p. 210):
  1. **Recursos**: há recursos para toda a população elegível?
  2. **Elegibilidade**: há índice contínuo com ponto de corte, ou o programa é
     aberto a todos?
  3. **Tempo**: a implementação é em fases ou imediata?

### 6.2 Quadro 11.1 — regras operacionais e métodos (p. 211; conferido no PDF, p. 241)

| Tempo de implementação | (1) Excesso de demanda; ordenação por índice contínuo com ponto de corte | (2) Excesso de demanda; sem ordenação por índice | (3) Sem excesso de demanda; ordenação por índice | (4) Sem excesso de demanda; sem ordenação por índice |
| --- | --- | --- | --- | --- |
| **(A) Em fases ao longo do tempo** | A1: Seleção aleatória (cap. 4); RDD (cap. 6) | A2: Seleção aleatória (cap. 4); VI — promoção aleatória (cap. 5); DD (cap. 7); DD com pareamento (cap. 8) | A3: Seleção aleatória em fases (cap. 4); RDD (cap. 6) | A4: Seleção aleatória em fases (cap. 4); VI — promoção aleatória para a participação inicial (cap. 5); DD (cap. 7); DD com pareamento (cap. 8) |
| **(B) Imediata** | B1: Seleção aleatória (cap. 4); RDD (cap. 6) | B2: Seleção aleatória (cap. 4); VI — promoção aleatória (cap. 5); DD (cap. 7); DD com pareamento (cap. 8) | B3: RDD (cap. 6) | B4: Se a participação não for completa: VI — promoção aleatória (cap. 5); DD (cap. 7); DD com pareamento (cap. 8) |

Fonte: Gertler *et al.* (2018, p. 211), quadro 11.1, adaptado (licença CC BY
3.0 IGO). DD = diferença em diferenças; RDD = regressão descontínua.

Leitura do quadro (p. 212-213): a maior parte dos programas entra em fases
(linha A), e a regra equitativa é dar a todos a mesma chance de entrar
primeiro. Com recursos limitados (A1, A2, B1, B2), o sorteio é regra viável.
Se há critério quantificável com corte (A1, A3), cabe RDD. Sem excesso de
demanda e sem critério (B4), resta a VI por promoção aleatória.

### 6.3 Quadro 11.2 — comparação dos métodos (p. 215-217, adaptado do J-PAL)

| Método | Quem é a comparação | Hipótese-chave | Dados necessários |
| --- | --- | --- | --- |
| Seleção aleatória | Elegíveis sorteados para a comparação | A aleatorização gera grupos estatisticamente idênticos em observáveis e não observáveis | Resultado pós-intervenção dos dois grupos; linha de base e características para checar o equilíbrio |
| VI (promoção aleatória) | "Cumpridores" cuja participação é afetada pelo instrumento | O instrumento afeta a participação, mas não afeta diretamente os resultados | Resultado pós para todos; participação efetiva; linha de base e características |
| RDD | Unidades próximas do corte, do lado inelegível | Logo acima e logo abaixo do corte as unidades são estatisticamente idênticas; para generalizar, a vizinhança do corte precisa representar a população | Resultado pós; índice e ponto de corte; linha de base e características |
| DD | Não participantes, por qualquer motivo, com dados antes e depois | Sem o programa, os resultados de participantes e não participantes evoluiriam em paralelo | Linha de base e dados pós, de resultados e características, para os dois grupos |
| Pareamento (PSM) | Para cada participante, o não participante com a mesma probabilidade prevista de participar | Nenhuma característica além das observáveis usadas no pareamento afeta a participação | Resultado pós para os dois grupos; participação efetiva; características da linha de base |

Síntese do conceito-chave (p. 218): o método preferido é o que melhor se
ajusta ao contexto operacional, exige as hipóteses mais fracas e o menor volume
de dados. Por isso a seleção aleatória é o padrão-ouro, e ela também tende a
exigir amostras menores (p. 218). O pareamento é o de hipóteses "mais fortes"
(p. 218).

### 6.4 Plano B e menor unidade viável (p. 219-222)

- Ter método alternativo e linha de base, porque a primeira opção pode falhar
  (p. 219; também p. 338 e 359).
- Escolher a **menor unidade de intervenção operacionalmente viável** (p.
  219-222). Os determinantes são economias de escala e complexidade
  administrativa, capacidade de alocar no nível individual, tensões e
  transbordamentos (p. 221). O que conta para equilibrar é o **número de
  unidades alocadas**, não o de indivíduos: seis províncias não bastam (p.
  220).

## 7. Amostragem e cálculo de poder estatístico (cap. 15)

### 7.1 Amostragem (p. 293-299)

- **Três etapas** (p. 294): definir a população de interesse; obter a
  **listagem** (cadastro de seleção); extrair as unidades segundo o cálculo de
  poder.
- **Viés de cobertura** (p. 294-295): ocorre quando a listagem não coincide com
  a população (fig. 15.2). A validade externa passa a valer só para a
  população listada.
- **Amostragem probabilística** (p. 296): aleatória simples; **estratificada**,
  útil para sobreamostrar subgrupos e essencial para comparar impactos entre
  subgrupos; **por conglomerados**, que surge naturalmente quando a unidade de
  implementação é maior que a de observação. A amostragem não probabilística
  gera erro sério (p. 297).
- **Amostragem aleatória ≠ seleção aleatória** (boxe 15.1, p. 297-299):
  amostrar aleatoriamente participantes e não participantes não os torna
  comparáveis.

### 7.2 A lógica do poder (p. 299-305)

- O cálculo de poder dá a **menor amostra** capaz de detectar diferença
  significativa entre tratamento e comparação (p. 300). Serve para decidir se
  bases existentes bastam, para evitar coletar pouco e para equilibrar custo e
  precisão (p. 300).
- H₀: impacto = 0; Hₐ: impacto ≠ 0 (p. 302).
- **Erro tipo I**: concluir que há impacto quando não há, com probabilidade
  igual ao nível de significância, em geral 5%. **Erro tipo II**: concluir que
  não há impacto quando há (p. 303-304). **Poder = 1 − P(erro tipo II)** (p.
  304-305). Avaliações de baixo poder são "inúteis" e podem levar a encerrar
  programa eficaz (p. 305).
- Base estatística (nota 4, p. 322): var(ȳ) = σ²/n. A variância da média cai
  com n.

### 7.3 Passo a passo (p. 305-309)

Cinco perguntas (p. 305), mais uma se houver conglomerados (p. 314):

1. O programa é implementado em **conglomerados**? (quadro 15.1, p. 306: nível
   de alocação x unidade de medida). Se sim, o número de conglomerados
   determina o tamanho efetivo da amostra.
2. Qual o **indicador de resultado**? Ele vem da teoria da mudança; indicadores
   diferentes exigem amostras diferentes (p. 307).
3. Qual o **impacto mínimo que justificaria o investimento**? É o **efeito
   mínimo detectável (EMD)**, uma decisão **de política, não técnica** (p.
   307). Pode ser ancorado em estudos semelhantes: em educação, 0,1 DP é ganho
   pequeno e 0,5 DP é grande (p. 307). Também pode vir de simulação ex-ante ou
   de retorno econômico, e deve ser fixado de forma conservadora (p. 308).
4. **Média e variância** do indicador na linha de base, de dados existentes ou
   de piloto. Maior variância exige amostra maior (p. 308).
5. **Poder e significância**: poder de 0,8 é a referência usual e 0,9 é mais
   conservador; significância de 5%, com 1% e 10% como alternativas (p.
   308-309).
6. (Com conglomerados) **variabilidade dentro dos conglomerados**, isto é, a
   correlação intraconglomerado (p. 314).

Boas práticas (p. 309): pedir **análise de sensibilidade** do cálculo; calcular
para vários indicadores; calcular para cada subgrupo de interesse.

### 7.4 Fórmulas

O livro não imprime a fórmula de tamanho de amostra; remete ao complemento
técnico online e aos programas Stata e Optimal Design (p. 309; nota 7, p. 322).
As fórmulas usadas nesta nota vêm dos slides da disciplina
(PECO5046-6046_Amostragem_e_poder_estatistico.pdf):

- Sem conglomerados, resultado contínuo (slide 23, PDF p. 21):
  **n = (t_{α/2} + t_{1−β})² σ_y² / [EMD² · P(1 − P)]**, com n o tamanho total
  e P a fração tratada.
- EMD (slide 24, PDF p. 23):
  **EMD = (t_{α/2} + t_{1−β}) · σ_y · √{1 / [P(1 − P) n]}**. O EMD é mínimo com
  P = 0,5. A nota 8 do livro (p. 322) diz o mesmo.
- Com conglomerados (slide 28, PDF p. 30):
  **n = (t_{α/2} + t_{1−β})² σ_y² / [EMD² P(1 − P)] · [1 + (m − 1)ρ]**, com ρ
  = S_b² / (S_b² + S_w²) e m o número de indivíduos por conglomerado; o termo
  [1 + (m − 1)ρ] é o **efeito do desenho**.

**Verificação por replicação** (script `analise/gertler_poder_replicacao.py`,
tabela `analise/tabelas/gertler_replicacao_poder.csv`): com σ = 8 (p. 311),
ρ = 0,04 (p. 316) e aproximação normal dos t, essas fórmulas reproduzem os
quadros 15.2, 15.3, 15.5 e 15.6 com diferença de no máximo 1 unidade por grupo
nos quadros sem conglomerados. Com conglomerados, as diferenças são de
arredondamento para m e número de conglomerados inteiros. O quadro 15.4 (taxa
binária, base de 5%) **não** é reproduzido com a variância p₀(1 − p₀): o
cálculo dá cerca de 2,7% a mais, 7.456 contra 7.257 por grupo para 1 p.p. O
livro não diz qual fórmula usou para proporções. [VERIFICAR] no complemento
técnico.

### 7.5 O exemplo HISP+ (p. 309-317)

Parâmetros (p. 310-311): resultado igual à despesa direta com saúde, média de
US$ 7,84 e DP de US$ 8. O EMD de política é US$ 2, com simulações para 1, 2 e
3; α = 5%.

| Quadro | Situação | EMD US$ 1 | EMD US$ 2 | EMD US$ 3 |
| --- | --- | --- | --- | --- |
| 15.2 (p. 311) | Poder 0,9, sem conglomerados: total (por grupo) | 2.688 (1.344) | 672 (336) | 300 (150) |
| 15.3 (p. 312) | Poder 0,8, sem conglomerados | 2.008 (1.004) | 502 (251) | 224 (112) |
| 15.5 (p. 316) | Poder 0,8, ρ = 0,04, máximo de 100 conglomerados: conglomerados × unidades = total | 100 × 102 = 10.200 | 90 × 7 = 630 | 82 × 3 = 246 |

- **Quadro 15.4** (p. 313), taxa de hospitalização com base de 5% e poder 0,8:
  aumentos de 1, 2 e 3 p.p. exigem 14.514, 3.630 e 1.614 no total. Eventos
  raros pedem amostras grandes. Se houver vários resultados, usa-se a maior
  amostra; caso contrário, é preciso avisar que falta poder para o outro
  resultado (p. 313).
- **Quadro 15.6** (p. 317), EMD de US$ 2 e poder 0,8, variando o total de
  conglomerados: 30 conglomerados × 50 unidades = 1.500; 58 × 13 = 754; 81 × 8
  = 648; 90 × 7 = 630; 120 × 5 = 600. **Menos conglomerados exigem muito mais
  observações.**
- **Regras de bolso**: "pelo menos 30 a 50 conglomerados em cada grupo"
  (conceito-chave, p. 314) e "40 a 50 conglomerados" no corpo do texto (p.
  315). O próprio livro oscila; o slide 29 da disciplina repete 30 a 50.
- **Além do caso de referência** (p. 318-320):
  - métodos quase-experimentais (RDD, pareamento, DD) costumam exigir amostras
    **maiores** que a seleção aleatória (p. 318);
  - linha de base e várias medições aumentam o poder (p. 318; nota 6, p. 322,
    sobre a correlação dos resultados no tempo);
  - comparar dois subgrupos pode **dobrar** a amostra, e estratificar a
    aleatorização ajuda (p. 319);
  - múltiplos resultados pedem testes conjuntos ou índices (p. 319);
  - cumprimento parcial e atrição exigem margem sobre o mínimo calculado (p.
    319-320).

## 8. Fontes de dados: administrativos x coleta primária (cap. 16)

- **Dados ao longo da cadeia** (p. 326-328): resultados finais, resultados
  intermediários (também para contornar falta de poder em eventos raros; p.
  326-327), atividades e produtos a partir do monitoramento, que mostra quem
  recebeu o quê, com que intensidade e quando (p. 327), e dados adicionais
  exigidos pelo método. O DD pede séries temporais (p. 327-328). Recomenda-se
  uma matriz pergunta × indicador × fonte (p. 328).
- **Checklist para usar dados existentes** (p. 328-329): amostragem (cobre
  tratamento e comparação? vem de listagem representativa?), tamanho
  suficiente para o poder, **linha de base**, **frequência**, **escopo** dos
  indicadores, **conexão com o monitoramento do programa** e **identificadores
  únicos** para ligar bases.
- **Censos e pesquisas nacionais** (p. 329-330) raramente têm tratados
  suficientes. Exemplo: programa que atinge 10% das famílias numa pesquisa de
  5.000 famílias rende cerca de 500 tratadas (p. 330). Pode-se sobreamostrar
  numa pesquisa planejada (p. 330).
- **Dados administrativos** (p. 330-334): registros de escola, saúde, tributos,
  serviços públicos e sistema financeiro, às vezes com longas séries. Podem ser
  **mais confiáveis** que autodeclaração (Malaui, p. 331), mas têm qualidade
  irregular e exigem **identificadores únicos** e proteção de
  confidencialidade (p. 331). Avaliações retrospectivas influentes usaram
  registros administrativos (p. 331-332): Plan Nacer, com cinco bases
  combinadas (boxe 16.1, p. 332), e PRAF com dados censitários (boxe 16.2, p.
  333). Construir o sistema de informação antes do lançamento permite medir a
  comparação. Dados administrativos "podem reduzir drasticamente o custo",
  mas nem sempre bastam (p. 333).
- **Coleta primária** (p. 334-347):
  - a maioria das avaliações precisa de ao menos linha de base e um
    acompanhamento (p. 334);
  - quem coleta: o executor, o órgão estatístico ou empresa ou instituto
    independente (p. 335-337). **Os mesmos procedimentos** devem valer para
    tratamento e comparação (p. 336), e uma instituição independente dá
    credibilidade (p. 336);
  - o contrato pode ter incentivos contra a não resposta (p. 337);
  - ser seletivo nos indicadores (p. 338); a linha de base funciona como
    "apólice de seguro" que permite recorrer ao DD se a aleatorização falhar
    (p. 338);
  - medir igual para os dois grupos, sem que o entrevistador saiba o status
    (p. 339);
  - não resposta e atrição: muitas avaliações miram **abaixo de 5%** (p. 347);
    erro de medida sistemático gera viés (p. 346).

## 9. Ética e ciência aberta (cap. 1, p. 22-24; cap. 13)

- **Não avaliar também pode ser antiético**: gastar recursos públicos em
  programas de eficácia desconhecida (p. 22, 262).
- **Princípio básico**: não negar ou adiar benefício de eficácia conhecida só
  por causa da avaliação (p. 23, 261). **A avaliação se ajusta às regras de
  seleção**, desde que claras e justas, e as questões éticas da alocação são
  das regras do programa, não da avaliação (p. 23, 261). Com recursos escassos,
  o sorteio entre igualmente elegíveis é ético (p. 23, 261).
- **Proteção de pessoas** (p. 262-266): critérios da OMS (p. 263); o **Relatório
  Belmont** (respeito às pessoas, beneficência, justiça; p. 263); aprovação de
  **comitê de ética** (IRB ou CEP), que leva de 2 a 3 meses (p. 264) e é
  condição necessária mas não suficiente (p. 264); protocolo de pesquisa (p.
  264-265); **consentimento informado** (p. 265); **confidencialidade**, com
  identificadores codificados e atenção a combinações de variáveis que
  identificam pessoas ou locais (p. 266).
- **Ciência aberta** (quadro 13.1, p. 267-268):
  - viés de publicação → **registro** da avaliação (p. 268-269; boxe 13.1:
    AEA RCT Registry, RIDIE/3ie, OSF);
  - mineração de dados, hipóteses múltiplas e subgrupos → **plano de
    pré-análise** e correções (p. 270-271). O plano especifica resultados,
    variáveis, subgrupos e abordagem de estimação, sem engessar a exploração
    (p. 271-272);
  - falta de replicação → dados, código e protocolos documentados e
    disponíveis (p. 272-273).
- **Lista de verificação** para uma avaliação ética e crível (p. 273-274).

## 10. Custo e gestão da avaliação (cap. 12; cap. 17)

- **Equipe** (p. 225-233): pesquisador principal, gerente ou coordenador de
  campo, amostrista e equipe de coleta; do lado da gestão, formuladores e
  gestores. As regras operacionais precisam ser transmitidas à equipe de
  pesquisa (p. 230).
- **Roteiro do plano de avaliação** (boxe 12.2, p. 231): introdução;
  intervenção; objetivos (hipóteses/teoria da mudança/cadeia, questões,
  indicadores, riscos); desenho; amostragem e dados (estratégia, cálculo de
  poder); plano de pré-análise; coleta (linha de base e acompanhamentos);
  produtos; disseminação; protocolos éticos. **Serve de esqueleto para a
  seção "proposta de avaliação de impacto" do artigo.**
- **Quando medir** (p. 239-242): cedo demais, o impacto é parcial; tarde
  demais, o programa pode perder apoio (King e Behrman, 2009, citados na p.
  240). A medição deve se alinhar ao ciclo do programa e aos ciclos
  orçamentários.
- **Custos** (p. 242-250):
  - Nas amostras do SIEF, os custos diretos vão de US$ 130 mil a US$ 2,78
    milhões, com média de cerca de US$ 1 milhão (p. 242).
  - Quadro 12.1 (p. 243): custo médio da avaliação de US$ 936 mil, igual a
    **6,2%** do custo médio dos programas (US$ 59,8 milhões).
  - Quadro 12.2 (p. 244-248): média de US$ 1,026 milhão, com **63% em coleta
    de dados**, 21% em equipe e consultores, 7% em viagens, 3% em
    disseminação e 7% em outros (média conferida no PDF, p. 248; texto na p.
    249).
  - Quadro 12.3 (p. 251-254): orçamento-exemplo por etapa (desenho, linha de
    base e dois acompanhamentos), com total de US$ 697.740.
  - Fontes de financiamento (p. 250).
- **Duração**: desenhar e coletar a linha de base leva um ano ou mais; a
  exposição, de um a cinco anos; o ciclo completo, "pelo menos de três a
  quatro anos" (p. 359-360).
- **Listas finais** (p. 358-360): elementos centrais de uma avaliação bem
  elaborada e mitigação de riscos, entre eles o **mesmo identificador da
  unidade** em todas as bases (p. 359).

---

## 11. Implicações para a LICC

Aqui se aplica o arcabouço de Gertler às regras **como estão**. Não se propõe
redesenho do mecanismo, que está fora do escopo. Quando a leitura depende de
dado ou norma não conferidos, isso vai marcado.

### 11.1 As regras operacionais da LICC pelas três perguntas do livro

| Pergunta de Gertler (p. 210) | Regra da LICC | Fonte | Consequência no quadro 11.1 |
| --- | --- | --- | --- |
| **Recursos**: dá para atender todos os elegíveis? | Não. Há teto anual de renúncia, de R$ 25 mi em 2025. Os 63 projetos que captaram em 2025 somam R$ 25.000.000,00 captados contra R$ 27,8 mi autorizados, e a soma autorizada de cada ciclo de habilitação 2023-2026 fica entre R$ 33 mi e R$ 47 mi. Há habilitados que não captaram: 11, 34 e 50 com `captacao_expirada` nos ciclos 2022, 2023 e 2024. O art. 18, §2 prevê remanejamento se não houver captação suficiente. | Teto: licc-gov/README-licc.md (Portaria SEFAZ nº 01-R/2025 e notícia da SECULT), norma primária não relida aqui [VERIFICAR]. Somas e contagens: `analise/tabelas/licc_captados_2025_totais.csv` e `licc_status_por_ciclo.csv`. Art. 18: IN SECULT 001/2025, transcrição em notas/politica/fontes/in-licc-001-2025.md | **Excesso de demanda**, colunas (1) ou (2). A comparação soma de ciclo x teto anual é só indicativa, porque ciclo de habilitação ≠ ano de captação (CLAUDE.md, regra 4) e os tetos anteriores a 2025 não foram verificados. |
| **Elegibilidade**: há índice contínuo com ponto de corte? | Não, na habilitação. A análise segue três etapas: documentação, parecer técnico e deliberação da CAP (arts. 37-42). Os critérios do Decreto 5.035-R/21 são qualitativos (art. 39, I-IX) e o parecer "deverá indicar a habilitação ou inabilitação" (art. 40), sem nota ou corte publicados na IN. **Entre habilitados, quem recebe é decidido pelas empresas patrocinadoras**, que firmam Termos de Compromisso (art. 46). | IN 001/2025, arts. 37-42 e 46. Existência de nota numérica no decreto ou nos pareceres: [VERIFICAR] | Coluna **(2), sem ordenação por índice**. A regra de alocação efetiva é descentralizada e não observável: preferências de patrocinadores e esforço dos proponentes. |
| **Tempo**: implementação em fases ou imediata? | Ciclos anuais: inscrição de 02/02 a 30/06 (art. 19). O certificado de captação vale 1 ano, prorrogável uma vez por mais 1 (art. 45, §1), e planos plurianuais captam por até 3 anos (art. 45, §4). Cada ciclo é uma nova coorte, não a mesma população entrando em fases. | IN 001/2025, arts. 19 e 45 | Mais próximo de **B2** (imediata, a cada ciclo) do que de A2. As duas células têm o mesmo menu. |

Outras regras que importam para o desenho:

- **Limiar de 35%**: só vai à CAP o projeto com Termos de Compromisso de ao
  menos 35% do valor total (art. 41). Pelo menos 35% precisam estar validados
  pela SEFAZ antes do evento (art. 46, §2). É arquivado o projeto que termina o
  prazo sem manifestação de interesse de ao menos 35% do aprovado (art. 47).
  Fonte: IN 001/2025.
- **Tetos por projeto**: R$ 500 mil (art. 14); R$ 300 mil para eventos em
  primeira edição (art. 14, §2); R$ 1 milhão para intervenção física (art.
  15). Limite de 3 projetos por agente por ano (art. 13). No anexo de captados
  de 2025, 21 dos 63 projetos têm valor autorizado de exatamente R$ 500 mil e
  19 captaram exatamente R$ 500 mil
  (`analise/tabelas/licc_captados_2025_totais.csv`).
- **Quatro cotas do teto** (art. 18): 30% para eventos calendarizados com mais
  de 10 anos, 10% para planos plurianuais, 10% para fora da RMGV e 50% para os
  demais. Esgotadas as três primeiras, aplica-se a quarta (§1).
- **Dado administrativo previsto em norma**: após o repasse, a SECULT publica
  no DOE extrato com projeto, patrocinador e valor (art. 49).

### 11.2 O que é "tratamento" na LICC, na linguagem do cap. 5

A LICC tem **dois estágios** de acesso, que correspondem aos conceitos de oferta
e participação de Gertler (p. 101-106):

1. **Habilitação**, com o certificado de aptidão (art. 45), funciona como a
   **oferta** do programa. Comparar habilitados com inabilitados é uma ITT.
2. **Captação**, com patrocínio efetivo acima do mínimo de 35%, funciona como a
   **participação**. Comparar captadores com habilitados que não captaram é um
   "inscritos x não inscritos" (p. 65-68).

Os habilitados que não captam são os "Nunca" relativos à oferta, e há
"Sempre" potenciais: inabilitados ou não captadores que executam o projeto com
outra fonte. Isso é o **viés de substituição** (p. 178). Fontes plausíveis de
substituto: Lei Rouanet (consultável pela API do SALIC, listada no escopo do
projeto), editais estaduais e municipais e recursos próprios. [VERIFICAR] quais
estão disponíveis e com que identificador.

### 11.3 Método por método: o que o livro indicaria, o que não, e por quê

| Método | Indicado para a LICC como está? | Por quê (Gertler) | Requisito crítico de dados |
| --- | --- | --- | --- |
| **Antes-depois** (evolução do setor cultural capixaba desde 2021) | **Não** como estimativa causal | Confunde a LICC com tudo o que muda no tempo (p. 60-65). Entre 2021 e 2025 há choques comuns ao setor cultural, como a retomada de eventos presenciais, que é hipótese de contexto e não achado. | — |
| **Com-sem** (captou x não captou; habilitado x inabilitado) | **Não** como estimativa causal; serve só como descrição | Viés de seleção duplo (p. 66): (i) patrocinadores escolhem projetos por características não observadas, como visibilidade, rede e afinidade de marca, que também afetam os resultados; (ii) proponentes com mais capacidade captam mais. É o caso "preferências dos administradores" do livro (p. 66), com a empresa no papel do administrador. | — |
| **Seleção aleatória** | **Não** dentro das regras atuais | Quem aloca o benefício entre habilitados é o patrocinador, não a SECULT. Sortear exigiria mudar a regra, e o livro diz que a avaliação não deve alterar regras bem definidas (p. 208) nem excluir elegíveis só para avaliar (p. 261). O sorteio entre habilitados quando o teto se esgota seria redesenho, **fora do escopo**. Só cabe mencionar como regra de racionamento equitativa discutida pelo livro (p. 75, 212). | — |
| **VI por promoção aleatória** | **Sim, prospectivamente**, como desenho de avaliação que não muda a regra de alocação | A LICC tem adesão voluntária do lado das empresas (célula B2). Sortear, entre os habilitados de um ciclo, quem recebe um encorajamento de captação (por exemplo, divulgação dirigida a contribuintes de ICMS ou rodada com patrocinadores) cria instrumento para a captação e estima o LATE dos que "captam se encorajados", os projetos na margem da captação. Isso é relevante para a política (p. 113-122, 138). **Riscos**: (a) exclusão, porque a visibilidade da promoção pode afetar o público diretamente, o que viola a condição 2 da p. 116, não é testável (p. 123) e exige promoção restrita ao contato com patrocinadores; (b) **teto vinculante**, porque em 2025 a captação esgotou o teto, e então o encorajado capta **no lugar** de outro habilitado. É efeito de equilíbrio geral e violação da SUTVA (p. 182-183; boxe 9.2), e o grupo de comparação perde captação por causa do tratamento. | Lista de habilitados do ciclo antes da captação; captação efetiva por projeto (DOE, art. 49; anexo de captados); resultado medido igual nos dois grupos (p. 339) |
| **RDD** | **Não**, com a informação disponível | A habilitação não usa índice contínuo com corte publicado (IN, arts. 39-40), o que falha a condição 1 da p. 127. O **limiar de 35%** (arts. 41, 46 e 47) é um corte, mas sobre uma variável que o proponente e o patrocinador **manipulam** ao buscar o mínimo, o que falha a condição 4 (p. 127, 132-134). Esse limiar poderia ser testado pela densidade da fig. 6.4 se houvesse dados do percentual comprometido por projeto, e esse dado **não está nos anexos** (ausente, não zero). Tetos por projeto (arts. 14-15) limitam intensidade, não elegibilidade. A cota "fora da RMGV" é fronteira geográfica e não índice contínuo; outras políticas também mudam na fronteira metropolitana, o que falha a condição 3. Seria preciso usar uma fronteira em RDD geográfico, como no boxe 16.2, p. 333, [VERIFICAR]. | Se a SECULT tiver **nota numérica de parecer com ponto de corte**, o RDD na habilitação passa a ser candidato. [VERIFICAR] no Decreto 5.035-R/21 e nos pareceres. |
| **DD** | **Sim, retrospectivamente**, como desenho principal | É o método do livro quando "a regra de seleção é menos clara" (p. 143). Elimina diferenças fixas no tempo entre captadores e não captadores (p. 148-149). Exemplos de unidade e resultado: **proponente** (CNPJ), com emprego e massa salarial formais e continuidade de atividade de uma base administrativa anual; ou **município**, com emprego e estabelecimentos culturais. As fontes e sua cobertura precisam ser [VERIFICAR]. Os testes de tendência paralela exigem **duas observações pré** ou mais (p. 151). Dá para fazer placebos com: coorte habilitada depois, antes de captar (tratamento falso); resultado que não deveria mudar (resultado falso); e comparações alternativas, como expirados, inabilitados e ainda não habilitados (p. 151-152, 157). | Série anual pré e pós para tratados e comparação; **identificador único** que ligue projeto, proponente e base de resultado. Os anexos trazem o nome do proponente, não o CNPJ (colunas de `habilitados-*.csv`), e o casamento por nome já falhou no licc.gov (licc-gov/CLAUDE-licc.md, "Armadilhas"). |
| **Pareamento (PSM) isolado** | **Não** | Supõe ausência de seleção em não observáveis, "muito forte" e não testável (p. 168-169). Na LICC a seleção é justamente por não observáveis dos patrocinadores. Sem linha de base, é "muito arriscado" (p. 169). | — |
| **DD com pareamento** | **Sim**, como refinamento do DD | O pareamento nas características da linha de base dentro de ciclo e cota (art. 18), usando valor autorizado, localização RMGV x interior, histórico e porte do proponente, restringe a comparação ao **suporte comum**; o DD remove os não observáveis fixos (p. 164-165, 169). As variáveis de pareamento devem ser as que **determinam a captação** (p. 164). | As mesmas do DD, mais covariáveis pré-habilitação |
| **Controle sintético** | **Complementar**, para uma pergunta agregada | Uma unidade tratada, o estado do ES, com séries longas (p. 167). A pergunta seria sobre o emprego cultural estadual após a lei. O risco é que outros estados tenham leis de incentivo semelhantes, contaminando o *donor pool*. [VERIFICAR] | Série estadual longa de indicador cultural |

### 11.4 Desafios do cap. 9 que a LICC ativa

- **Transbordamento e SUTVA** (p. 181-187): com o teto vinculante, a captação
  de um projeto reduz a chance dos outros, porque os habilitados competem pelo
  mesmo teto. Eventos patrocinados podem ainda deslocar público de eventos não
  patrocinados no mesmo município (equilíbrio geral, p. 182). É preciso
  perguntar pelo impacto direto e pelo indireto (p. 186).
- **Viés de substituição** (p. 178): projetos não captados que executam com
  outra fonte atenuam o contraste. Deve-se medir a participação dos dois
  grupos em outros mecanismos.
- **Heterogeneidade** (p. 177-178, 319): as quatro cotas do art. 18 e a divisão
  RMGV x interior são subgrupos naturais. Estratificar e calcular poder por
  subgrupo, porque comparar dois subgrupos pode dobrar a amostra (p. 319).
- **Tempo** (p. 191-192, 240-241): o certificado vale até 2 anos e a execução
  vem depois. O acompanhamento precisa respeitar esse ciclo, e a regra 4 do
  CLAUDE.md (captados ≠ habilitados) deve orientar a definição de coorte.
- **Cumprimento parcial** (p. 179-181): um projeto habilitado que capta menos
  que o autorizado tem **intensidade** de tratamento diferente. Isso remete ao
  cap. 10 (níveis de tratamento) ou a uma medida contínua de dose. Não há
  método específico no livro para dose contínua observacional. [VERIFICAR] em
  outra fonte.

### 11.5 Poder: o que o universo de habilitados permite

Com dados administrativos, a "amostra" é o universo de habilitados e o que
limita o poder é o **N finito**. Ilustração com σ = 1 (EMD em desvios-padrão),
α = 5% e bilateral, pela fórmula do slide 24 escrita para grupos desiguais,
sob a **hipótese de trabalho** de que `concluido` + `em_execucao` = captou e
`captacao_expirada` = não captou. A legenda desses estados não foi conferida
na fonte: [VERIFICAR com a SECULT]. `captando` fica excluído por ter desfecho
em aberto. Script `analise/gertler_poder_replicacao.py`; tabela
`analise/tabelas/licc_emd_ilustrativo.csv`.

| Recorte | Captou (n_T) | Não captou (n_C) | EMD, poder 0,8 | EMD, poder 0,9 |
| --- | --- | --- | --- | --- |
| Ciclo 2022 | 58 | 11 | 0,92 DP | 1,07 DP |
| Ciclo 2023 | 79 | 34 | 0,58 DP | 0,67 DP |
| Ciclo 2024 | 61 | 50 | 0,53 DP | 0,62 DP |
| Ciclos 2022-2024 empilhados | 198 | 95 | 0,35 DP | 0,41 DP |

Leitura pela régua do livro, em que 0,1 DP é pequeno e 0,5 DP é grande em
educação (p. 307): **um ciclo isolado só detecta efeitos grandes**. Empilhar
ciclos, usar a linha de base e covariáveis para ganhar poder (p. 318) e usar a
correlação no tempo (nota 6, p. 322) são necessários. O pareamento que descarta
unidades fora do suporte comum **reduz** o N (p. 162-163), e métodos
quase-experimentais pedem amostra maior que a do experimento (p. 318).

No **nível municipal**, os conglomerados são os 78 municípios, e as regras de
bolso do livro pedem 30 a 50 por grupo (p. 314-315). A RMGV tem só 7
municípios, um número de unidades que o livro considera insuficiente para
equilibrar grupos (p. 88, 220). A contagem de 78 municípios e 7 na RMGV vem de
licc-gov/CLAUDE-licc.md.

Estes números são ilustração de ordem de grandeza, não o cálculo de poder do
artigo. Esse cálculo precisa de σ e, se for o caso, de ρ do **indicador
escolhido**, obtidos de dados existentes (p. 308), e fica para
`notas/desenho/`.

### 11.6 Dados, ética e custo aplicados

- **Dados**: a estratégia recomendada é **administrativa** (p. 330-333): anexos
  da SECULT, extratos do DOE (art. 49), bases de emprego formal, SALIC e Mapa
  Cultural. Pelo checklist das p. 328-329, o gargalo é o **identificador
  único**. Hoje o proponente é identificado por nome, e 23 dos 63 captadores de
  2025 continuam sem município (licc-gov/CLAUDE-licc.md), o que já ilustra o
  custo da falta de chave. Coleta primária sobre público e fruição cultural
  seria o componente caro: 63% do custo médio das avaliações do SIEF vai para
  coleta (p. 249). Se houver coleta, os mesmos procedimentos valem para
  captadores e não captadores (p. 336).
- **Ética**: nenhum desenho indicado exclui elegíveis. O DD usa quem já ficou
  sem patrocínio pela regra vigente, e a promoção aleatória só acrescenta
  encorajamento, em linha com as p. 23 e 261. Proteção de dados de proponentes
  e patrocinadores (p. 266) implica anonimização e cuidado com combinações
  identificadoras, como município pequeno com um único proponente. Pesquisa com
  público exige CEP, que leva de 2 a 3 meses (p. 264). Recomenda-se **registro
  e plano de pré-análise** (p. 269-271).
- **Custo**: usar dados administrativos é o que torna a proposta viável dentro
  do tamanho da LICC (p. 333). O quadro 12.1 dá como referência avaliações que
  custam em média 6,2% do programa (p. 243). O orçamento da proposta deve ser
  explicitado pelo roteiro do boxe 12.2 (p. 231). [VERIFICAR] se o artigo vai
  orçar em reais; isso não entra sem fonte de custo local.

### 11.7 Perguntas de avaliação candidatas, no formato do cap. 2

Hipóteses testáveis e quantificáveis (p. 40, 42), a validar com a teoria da
mudança da LICC em nota própria:

1. Qual é o efeito da **captação via LICC** sobre o emprego formal e a massa
   salarial do proponente nos dois anos seguintes, para projetos habilitados
   no mesmo ciclo e na mesma cota? Desenho: DD com pareamento.
2. Qual é o efeito de **encorajar a captação** sobre a probabilidade de captar
   e sobre a execução do projeto? Primeiro estágio e ITT da promoção
   aleatória; LATE para os que captam se encorajados.
3. (Mecanismo, boxe 2.2, p. 41-42) O **limiar de 35%** e o **teto vinculante**
   deslocam a captação para projetos e proponentes com mais rede? É pergunta
   descritiva e normativa (p. 8), não causal, e pode ser respondida com os
   anexos existentes.

---

## Questões em aberto

- [VERIFICAR] DOI da edição em português: o DOI impresso não resolve.
  Metadados do handle 10986/25030 não conferidos.
- [VERIFICAR] O Decreto 5.035-R/21 ou os pareceres atribuem **nota numérica com
  ponto de corte** na habilitação? Se sim, o RDD passa a ser candidato.
- [VERIFICAR] A legenda dos estados `concluido`, `em_execucao`, `captando` e
  `captacao_expirada` da lista de habilitados da SECULT. A equivalência
  "concluido/em_execucao = captou" é hipótese de trabalho.
- [VERIFICAR] O percentual comprometido por projeto em relação ao limiar de 35%
  é publicado em algum lugar? Sem ele, o limiar não pode ser examinado.
- [VERIFICAR] Tetos anuais de renúncia anteriores a 2025, na norma primária.
  Hoje só R$ 25 mi (2025) consta, via licc-gov/README-licc.md.
- [VERIFICAR] Que base administrativa fornece o resultado por proponente e se
  há CNPJ do proponente para o *linkage*. O anexo de captados traz CNPJ só dos
  patrocinadores.
- [VERIFICAR] Fórmula usada por Gertler para o quadro 15.4 (proporções); a
  replicação com p₀(1 − p₀) difere em cerca de 2,7%.
- [VERIFICAR] Literatura de DD com adoção escalonada: fora de Gertler, e
  necessária porque os ciclos da LICC entram em anos diferentes.
- [VERIFICAR] Outros estados com lei de incentivo via ICMS, antes de propor
  controle sintético.
