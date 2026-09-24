# Teoria da mudança da LICC e as hipóteses H1–H3

**Escopo definido pelos autores (24/09/2026).** O trabalho da primeira parte do curso é avaliar o desenho da LICC
com a teoria da mudança e estruturar a avaliação de impacto: o que seria preciso estimar, com que dados e sob quais
vieses. **Nada é estimado agora.** A escolha do método (seleção aleatória, pareamento, diferenças em diferenças,
variáveis instrumentais, regressão descontínua, controle sintético) fica para a segunda parte do curso (aulas 9 a
15, de 07/10 a 25/11; APR [s.9]). As instruções continuam pedindo, na proposta, desenho da amostra, fonte de dados e
cálculo do poder (INSTR, item 2). O poder aqui é conta de ordem de grandeza, não escolha de método.

Hipóteses dos autores, tratadas como **teoria negativa** do programa (HM TREASURY, 2026, p. 47), ou "contrateorias"
(WHITE; RAITZER, 2017, p. 21):

- **H1 — escolha**: a coordenação centralizada (edital e habilitação) somada à escolha da empresa favorece
  empresas que usam o crédito como orçamento de marketing.
- **H2 — funil**: poucos projetos passam.
- **H3 — atrito**: é caro e difícil se inscrever e chegar à habilitação.

No material do J-PAL, "premissas e riscos podem ser perguntas de pesquisa" (M03 [s.33]). É exatamente o papel de
H1–H3.

Siglas das fontes do curso: `notas/disciplina/01-slides-e-guias.md` (TdM, M03, IC, MRP, VAL, AMO, APR, INSTR),
`03-gertler.md` e `04-itau-magenta-adb.md`. Números: `analise/07_hipoteses_h1_h3.py` → `analise/tabelas/07_*.csv`,
salvo outra tabela indicada. Diagrama: `analise/08_figura_teoria_da_mudanca.py` →
`analise/figuras/08_teoria_da_mudanca.png`.

## 1. A teoria da mudança pelos cinco passos do J-PAL (M03 [s.14])

### Passo 1 — Propósito

Ampliar e desconcentrar o acesso da população capixaba a bens culturais, financiando produção e oferta fora do
circuito já consolidado. O problema que o artigo reconstrói na introdução é uma carência: **a baixa e desigual
capacidade de financiar a produção e a oferta cultural fora do circuito já consolidado**. A LICC não declara nenhum
dos dois; ambos são reconstrução.

### Passo 2 — Cadeia causal, do final ao início (M03 [s.22–24])

A LICC tem uma particularidade que a cadeia do Quadro 2 atual do artigo esconde. Na cadeia de Gertler, os
**produtos estão sob controle da agência** (TdM [s.7]). Na LICC, o produto "projeto patrocinado" depende de um
**terceiro ator**, a empresa, que decide quem recebe. Por isso a cadeia precisa separar as etapas e nomear quem
decide em cada uma. A separação segue os anéis do licc.gov, que são os atores pelo caminho do dinheiro
(`fcarva/licc.gov/docs/ontologia.md`), e o "modelo de mudança comportamental" (WHITE; RAITZER, 2017, Tabela 2.1,
p. 26): cada elo diz quem precisa mudar de comportamento.

| Componente | Descrição | Quem decide (anel do licc.gov) | Indicador | Publicado? |
| --- | --- | --- | --- | --- |
| Problema | Baixa e desigual capacidade de financiar a produção e a oferta cultural fora do circuito consolidado | — | ocupação cultural; equipamentos e fundos municipais por território | sim (IBGE) |
| Insumos | Teto de renúncia de ICMS (o imposto que a população deixa de arrecadar); SECULT, pareceristas, CAP, SEFAZ; Mapa Cultural | Governo (anel 1) e população como financiadora indireta (centro) | teto; renúncia efetiva; equipe | sim |
| Atividade A1 | Edital e inscrição on-line no Mapa Cultural | SECULT abre; **agente cultural decide se inscrever** | inscritos por ciclo, território, natureza | **não** |
| Atividade A2 | Parecer documental e deliberação da CAP | SECULT e CAP (anel 1) | habilitados e inabilitados; motivo | só habilitados |
| Produto P1 | Cardápio de projetos habilitados (oferta) | — | habilitados e valor autorizado por ciclo | sim |
| Atividade A3 | Busca de patrocinador; termo de compromisso | **empresa decide quem patrocina** (anel 2) | termos por projeto e empresa | sim (anexos 2022-2026) |
| Atividade A4 | Validação dos termos pela SEFAZ até o teto | SEFAZ, pela ordem de chegada | validados e indeferidos por teto | só 2023-2024 |
| Produto P2 | Projetos patrocinados (participação) | — | captação por projeto, cota, patrocinador | sim |
| Produto P3 | Projetos executados, com contrapartidas | proponente (anel 3) | status; prestação de contas | status sim; contas não |
| Resultado intermediário RI1 | Mais bens culturais de acesso público (gratuidade, acessibilidade, território) | proponente e público | público, gratuidade, locais | **não** |
| Resultado intermediário RI2 | Quem executa se diversifica e fica mais capaz | proponente | estreantes; interior; emprego formal | parcial |
| Resultado final | Maior e menos desigual acesso da população à cultura; setor mais capaz de se financiar | população (centro) | acesso por território; ocupação cultural | parcial |

Cada aresta do grafo do licc.gov é um elo dessa cadeia: `inscrito_em` (A1), `aprova` (A2 → P1), `patrocina` (A3 →
P2, a única aresta que move R$) e `beneficia` (P3 → RI1). **Só `patrocina` tem dado público completo.** A entrada
e o benefício, os dois elos de que as hipóteses mais precisam, são opacos. A API do Mapa Cultural devolve lista
vazia para as inscrições de 2025 (`dados/fontes_web/paginas/mapa_api_inscricoes_1878.txt`). É a "cadeia de
responsabilização" do licc.gov com buracos.

Há três cadeias paralelas, como pede White e Raitzer (2017, p. 21: "muitas cadeias, não uma"):

- **entrada**: A1 → A2 → P1, decidida pelo agente e pela SECULT;
- **financiamento**: P1 → A3 → A4 → P2, decidida pela empresa e pelo teto;
- **entrega**: P2 → P3 → RI1/RI2 → final, decidida pelo proponente.

### Passo 3 — Premissas e riscos: onde entram H1–H3

Premissa é a "condição externa necessária" para que o elo valha; risco é o "efeito negativo não esperado" (M03
[s.33]).

| Elo | Premissa (P) | Risco / contrateoria (R) | Hipótese |
| --- | --- | --- | --- |
| A1: agente → inscrição | Agentes com projetos de valor público sabem da lei, querem e conseguem se inscrever | Exigências (CNPJ com finalidade cultural, sede em nome próprio, certidão estadual, até 13 documentos; IN 001/2025, arts. 13-19) selecionam por capacidade administrativa, não por mérito cultural | **H3** |
| A2: inscrição → habilitação | A CAP seleciona por mérito, com critério claro, e habilita o que o teto comporta | Avaliação "documental", binária, sem nota ou ranking; habilita 1,1 a 1,9 vez o teto | **H2** |
| A3: habilitado → patrocinado | Empresas escolhem projetos alinhados ao interesse público e diversos | Escolha por marca, visibilidade e relacionamento (orçamento de marketing); poucas empresas | **H1** |
| A4: termo → validado | O racionamento no teto segue critério público | Racionamento pela ordem de validação: termos com patrocinador indeferidos | **H2** |
| P3 → RI1: executado → acesso | O projeto não aconteceria sem o incentivo e entrega acesso | Financia o que já aconteceria (substituição de patrocínio próprio); bem com componente privado | **H1** (versão causal) |
| RI → final | Políticas complementares (fomento direto, capacidade municipal) | A política reproduz a concentração prévia | — |

H2 descreve **o quê** (quanto se perde em cada elo). H1 e H3 são dois **porquês** concorrentes: a perda nasce na
escolha da empresa (H1) ou na entrada (H3)? É a mesma distinção que o advogado do diabo cobrou no Stage 3 (DA-1).
A concentração medida na habilitação não pode ser atribuída à escolha da empresa.

### Passo 4 — Hipótese causal (gabarito de M03 [s.35])

*Se* a SECULT abre a inscrição e habilita projetos culturais, e empresas contribuintes patrocinam parte deles com o
ICMS que pagariam (atividades), *isto gera* um cardápio de projetos habilitados e um conjunto de projetos
patrocinados e executados (produtos), *o que deveria levar* a mais bens culturais de acesso público, executados por
proponentes mais diversos e mais capazes (resultados intermediários), *que ao final melhorarão* o acesso da população
à cultura e reduzirão sua desigualdade territorial (resultados finais), *contribuindo para* ampliar e desconcentrar a
capacidade de financiar a cultura no estado (propósito).

A versão atual do artigo (§ 4.1) pula a entrada e junta habilitação e captação num só passo. Esta versão explicita as
duas decisões.

### Passo 5 — Indicadores (SMART; TdM [s.18])

A tabela do Passo 2 dá um indicador por elo. O teste SMART falha em dois pontos por **falta de publicação**, não por
falta de dado:

- **"Mensurável" falha na entrada**: a SECULT tem os inscritos no Mapa Cultural, mas não os publica.
- **"Atribuível" falha no resultado**: o público é autodeclarado nos relatórios de execução, conferido projeto a
  projeto e nunca agregado.

Isso é achado de avaliação do desenho, e cada falha vira pedido de dado (§ 6).

## 2. Funil de atrito da LICC (TdM [s.19–22]; WHITE; RAITZER, 2017, p. 23-24)

"De cada 100 beneficiários potenciais, quantos de fato se beneficiam?" (TdM [s.20]).

| Etapa | 2022-2024 | Fonte | Situação |
| --- | --- | --- | --- |
| Agentes culturais cadastrados | 25.441 no Mapa Cultural em 24/09/2026 (22.849 individuais, 2.592 coletivos); cadastro não é elegibilidade, pois a inscrição exige CNPJ | Mapa Cultural (API pública; `07_mapa_cultural_universo.csv`) | medido (topo) |
| Inscritos | — | SECULT (não publica) | **ausente** |
| Habilitados | 305 (69, 113, 123), de 53, 92 e 95 proponentes | lista oficial | medido |
| Com situação resolvida | 293 | idem | medido |
| Captaram | 198, ou 68 de cada 100 resolvidos (84, 70 e 55 por ciclo) | idem | medido |
| Termos com patrocinador que couberam no teto | 78 de cada 100 R$ em 2023; 74 em 2024 | anexos de captação | medido |
| Executados com prestação de contas | status "concluído" | lista oficial | parcial |
| Público alcançado, gratuidade | — | relatórios de execução (internos) | **ausente** |

Tabelas: `07_funil_por_ciclo.csv` e `07_funil_captacao_anual.csv`.

Três leituras para a avaliação do desenho:

1. **O funil se estreita justamente onde não há dado**: antes da habilitação e depois da execução. Entre dezenas de
   milhares de agentes cadastrados e menos de 100 proponentes habilitados por ciclo, não se sabe quantos eram
   elegíveis, quantos se inscreveram e quantos foram inabilitados.
2. **Mudança de regime em 2025.** Desde a IN 001/2025 (termos de ao menos 35% antes da CAP) e a Portaria 062-S/2025
   (carta de intenção em 120 dias, sob pena de arquivamento), a busca de patrocinador passou para antes da
   habilitação. A expiração cai para 3 de 56 resolvidos no ciclo 2025, e os habilitados, de 123 para 74. A perda não
   sumiu: mudou para uma etapa que não é publicada (pareceres favoráveis arquivados sem carta).
3. **O funil alimenta o cálculo de poder.** "Superestimar participação e efeito leva a amostras pequenas demais" (TdM
   [s.19]). A taxa de 68% de captação e as taxas das etapas ausentes entram diretamente no poder da proposta.

As sete perguntas do túnel (TdM [s.21]) aplicadas à LICC:

1. **Os agentes sabem da lei?** Indeterminado. Há apresentações da LICC nos municípios; a lista não foi obtida.
2. **Querem participar?** Indeterminado.
3. **Podem participar?** Exigências formais altas (H3).
4. **A transferência é efetiva?** Não se aplica no sentido de conhecimento. O análogo é o proponente conseguir
   patrocinador (H1).
5. **O comportamento muda?** O análogo é a empresa escolher por interesse público (H1).
6. **Restrições permanecem?** Sim: o teto (H2).
7. **O efeito é frequente?** Indeterminado: não há dado de público.

## 3. Mecanismo de mapeamento: onde a cadeia pode estar rompida (VAL [s.21–26]; Williams, 2020)

Formato do slide: **Etapa | Hipótese contextual | Contexto real**. Aqui não se transpõe política de outro lugar; o
mapeamento é usado para confrontar as premissas com o contexto do ES. A limitação do método vale: ele "fornece a
direção do impacto, mas não permite quantificá-lo" (VAL [s.26]).

| Etapa | Hipótese contextual | Contexto real (com fonte) | Situação |
| --- | --- | --- | --- |
| Entrada (A1) | Agentes do interior e da periferia conseguem cumprir as exigências de inscrição | CNPJ obrigatório; pessoa física não se inscreve (IN 001/2025, art. 19). 14 municípios, todos do interior, nunca tiveram projeto habilitado. Desde 2024 entram 3 municípios novos por ciclo (`03_coortes_primeira_presenca_canonico.csv`). Estreantes: 56 em 2024, 26 em 2025 e 40 em 2026 (`07_composicao_por_ciclo.csv`) | **indeterminado**, com sinais de restrição (sem inscritos, não há como separar falta de demanda de barreira) |
| Habilitação (A2) | A CAP seleciona por mérito e habilita o que o teto financia | Sem nota nem ranking; valor habilitado de 1,1 a 1,9 vez o teto | premissa de critério **não atendida** (racionamento transferido às etapas seguintes) |
| Captação (A3) | As empresas escolhem por interesse público, inclusive fora do circuito consolidado | 2 empresas somam metade de 2025; energia e gás, 52%. Execução de 68% na RMGV e 63% no interior. Recorrentes 71% e estreantes 57%. Sob "patrocinador primeiro", a fatia da RMGV no valor caiu de 74% para 57% e foi a 67% | **contestado**: concentração no capital, mas sem viés territorial forte na escolha |
| Validação (A4) | O teto financia quem tem patrocinador, por critério público | Em 2023 e 2024, 22% e 26% do valor com patrocinador foi indeferido pela ordem de chegada | premissa de critério **não atendida** |
| Entrega (P3 → RI1) | O projeto financiado não aconteceria sem a LICC e chega ao público | A maior reserva (30%) vai a eventos com mais de 10 anos; não há dado de público | **indeterminado** |

Leitura: nenhum elo aparece claramente "rompido" com o dado público. Dois têm premissa de critério não atendida
(habilitação e validação), dois são indeterminados por falta de dado (entrada e entrega) e um é contestado
(captação). A avaliação de impacto serve para resolver os indeterminados e o contestado.

## 4. Cada hipótese: o que seria preciso para estimar

Roteiro da disciplina para cada uma:

- **pergunta de avaliação**, no formato de Gertler (cap. 2);
- **parâmetro** na notação de resultados potenciais (MRP [s.5–11]);
- **comparação ingênua e seus vieses**: SDO = EMP + viés de seleção + viés de efeitos heterogêneos (MRP [s.22]);
- **SUTVA** (MRP [s.34–35]);
- **ameaças à validade interna e externa** (VAL [s.4, s.7]);
- **dados**;
- **regras operacionais** (Gertler, quadro 11.1): qual variação a política já produz e que métodos ela admitiria. A
  escolha fica para a segunda parte.

### H2 — "poucos passam" (medir o funil)

- **Pergunta.** Que fração dos projetos passa em cada elo (inscrição → habilitação → captação → validação →
  execução), e essa fração difere por território, recorrência, natureza jurídica, faixa de valor e linguagem?
- **Parâmetro.** Taxas de passagem condicionais, por exemplo P(habilitado | inscrito, X). É **descritivo**: não há
  tratamento, e sim um diagnóstico do desenho (TIP1 [s.19]). Não requer contrafactual.
- **Onde vira causal.** Quando se pergunta **por que** não passam, a questão vira H1 ou H3. Há uma pergunta causal
  própria de H2: o efeito do **racionamento pelo teto** sobre o projeto. Com Y = o projeto é executado, compara-se o
  termo validado logo antes do esgotamento com o indeferido logo depois (§ H1).
- **Dados.** Inscritos com motivo de inabilitação (LAI); pareceres arquivados sem carta em 2025-2026 (LAI);
  habilitados e anexos de captação (públicos).
- **O que já dá para dizer.** O funil de 2022-2024 (§ 2); o teto é vinculante; a mudança de regime escondeu a perda.

### H1 — "orçamento de marketing" (a escolha da empresa)

Com crédito de 100%, a empresa não põe dinheiro próprio. Ela escolhe o destino do ICMS que pagaria e fica com a marca.
Patrocínio é comunicação de marketing (CORNWELL; MAIGNAN, 1998), e a doação corporativa responde a motivos de lucro
(NAVARRO, 1988). Empresas também usam a filantropia como instrumento de influência política (BERTRAND *et al.*,
2020), motivo plausível para concessionária regulada. Usar o crédito como marketing é, portanto, o comportamento
esperado. A pergunta de política é se isso **custa bem público**. H1 tem duas versões:

**H1a — a escolha pesa marca mais que interesse público (elo A3).**

- **Pergunta.** Entre os projetos habilitados disponíveis, que atributos aumentam a chance de uma empresa
  patrocinar?
  - Atributos de visibilidade: valor no teto, evento grande e calendarizado, RMGV.
  - Atributos de bem público: gratuidade, formação, periferia.
- **Parâmetro.** Pesos da escolha da empresa: modelo de escolha discreta sobre o cardápio vigente (nota 02, E3). Não
  é efeito de tratamento. Descreve a regra de decisão do terceiro ator da cadeia.
- **Viés.** "Causalidade reversa": quem já tem patrocinador acertado pede o teto (DA-2). A comparação "no teto × fora
  do teto" mistura escolha da empresa e escolha do proponente.
- **Dados.** Anexos de captação de 2022-2026 (projeto × empresa × valor). Falta a data de cada termo, para saber o
  que estava disponível quando a empresa escolheu.
- **Comparação com a população.** A distância entre os pesos da empresa e as preferências da população nos mesmos
  atributos (experimento de escolha; HAINMUELLER; HOPKINS; YAMAMOTO, 2014) é a medida da cunha. É o único
  indicador que põe no centro do grafo a população, que financia e é beneficiária.

**H1b — o que a empresa financia aconteceria sem a LICC (elo P3 → RI1; adicionalidade).**

- **Pergunta.** Qual é o efeito de captar pela LICC sobre a realização e o alcance do projeto?
- **Parâmetro.** Unidade i = projeto habilitado; T_i = 1 se captou; Y_i = 1 se o bem cultural acontece (e, se houver
  dado, público e gratuidade). O parâmetro é o **EMPT**: é "particularmente útil quando a participação é
  voluntária" (MRP [s.10]), e responde se o que foi financiado dependia do financiamento. O contraste EMPT × EMPNT
  diz se a escolha da empresa acerta onde o efeito é maior (nota 02, E2).
- **Comparação ingênua.** Captou × expirou (198 × 95, 2022-2024).
  - *Viés de seleção*: E[Y(0) | T = 1] − E[Y(0) | T = 0]. Se a empresa escolhe eventos consolidados, que
    aconteceriam de todo modo, Y(0) é maior entre os tratados, e a diferença simples **subestima** a
    adicionalidade.
  - *Viés de efeitos heterogêneos*: (1 − π)(EMPT − EMPNT). Se a empresa escolhe onde o efeito é pequeno (H1), EMPT <
    EMPNT, e o termo tem sinal negativo.
  - Os dois vieses vão na mesma direção sob H1. Por isso a comparação simples é inútil para testar H1.
- **SUTVA.** O teto torna o financiamento soma zero: se um projeto capta, outro deixa de captar. O grupo de
  comparação é afetado pelo tratamento. É o caso de "equilíbrio geral" (MRP [s.34]; Gertler, p. 182-183).
- **Outras ameaças** (VAL [s.4]).
  - *Substituição*: quem não capta executa com Rouanet, edital ou recurso próprio (Gertler, p. 178).
  - *Eventos externos*: Lei Paulo Gustavo e PNAB no mesmo período.
  - *Atrito de dados*: projeto que some não é projeto que não aconteceu.
  - *Validade externa*: vale só para o regime "habilitação primeiro" (2022-2024).
- **Variação que a política já produz** (Gertler, quadro 11.1).
  - Excesso de demanda sem índice de ordenação e ciclos anuais: célula B2. O quadro admite seleção aleatória, VI
    por promoção aleatória, DD e DD com pareamento.
  - Duas variações específicas da LICC:
    - (i) o **racionamento pela ordem de validação** em 2023 e 2024: 11 e 22 termos com patrocinador indeferidos. Se
      a ordem for "como se aleatória" perto do esgotamento, é um experimento natural;
    - (ii) a **reserva de 30% para eventos com mais de 10 anos** (art. 18, I): um corte na idade do evento, candidato
      a regressão descontínua se a idade for observável (não é publicada).
- **Dados.**
  - Ocorrência do evento: agenda do Mapa Cultural, SALIC, DIO, nova habilitação.
  - Relatórios de execução: público e gratuidade (internos).
  - Data e ordem de validação dos termos (SEFAZ).
  - Patrocínio das mesmas empresas pela Rouanet. Das 26 empresas que patrocinaram em 2025, 13 aparecem como
    incentivadoras no SALIC, e elas responderam por 86% da renúncia daquele ano (`07_patrocinadores_na_rouanet.csv`).
    O SALIC dá o total doado acumulado; a série por ano, necessária para medir substituição, exige o endpoint de
    doações. São empresas que já patrocinavam cultura por outra via, o que torna a pergunta de adicionalidade
    concreta.

### H3 — atrito na entrada (elo A1)

- **Pergunta.** Qual é o efeito de reduzir o custo de entrada (informação, apoio documental, CNPJ) sobre a
  inscrição, a habilitação e **quem** entra?
- **Parâmetro.** Unidade i = agente cultural sem inscrição prévia (ou o município); T_i = 1 se exposto à redução do
  custo; Y_i = inscreveu-se / foi habilitado / captou.
  - Se a exposição é oferecida e nem todos usam, o parâmetro é a intenção de tratar e, para os que usam por causa da
    oferta, o efeito local (Gertler, cap. 5).
  - Em focalização interessa **quem** entra por causa da redução: se os novos entrantes passam nos filtros seguintes
    na mesma taxa que os demais, o atrito exclui sem selecionar; se passam menos, ele funciona em parte como
    triagem (KLEVEN; KOPCZUK, 2011; DESHPANDE; LI, 2019; FINKELSTEIN; NOTOWIDIGDO, 2019).
  - O conceito na administração pública é o de **custo administrativo**: custos de aprendizado, de conformidade e
    psicológicos (MOYNIHAN; HERD; HARVEY, 2015). Em programas sociais, simplificar e informar aumenta a adesão
    (BHARGAVA; MANOLI, 2015).
- **Comparação ingênua.** Inscritos × não inscritos: viés de seleção, pois quem se inscreve tem mais capacidade
  (IC [s.10–11]). Antes × depois da mudança de 2025: comparação reflexiva, que confunde a regra com o teto e com
  tudo o que muda no tempo (IC [s.8]).
- **SUTVA.** Mais entrantes disputam o mesmo teto; o efeito sobre captação é de equilíbrio parcial. Os resultados
  de entrada (inscrição, habilitação) sofrem menos.
- **Variação que a política já produz.**
  - (i) A **mudança de regime em 2025** ("patrocinador primeiro"), uma mudança de regra no tempo, com a Rouanet no
    ES como possível grupo de comparação. O download do SALIC de 2025 está incompleto (6.000 de 15.415 projetos);
    a comparação fica vazia até completar.
  - (ii) As **apresentações da LICC nos municípios**, se tiverem datas e locais, criam exposição escalonada por
    município.
  - (iii) Uma **promoção aleatória de apoio à inscrição** não muda o mecanismo (só acrescenta informação) e é
    compatível com o escopo (`notas/politica/01-desenho-legal.md`, § 16).
  - (iv) O limite de valor do MEI (2 vezes o faturamento anual; IN 001/2025, art. 17) é um corte de elegibilidade
    por natureza jurídica.
- **Dados.**
  - Universo de agentes no Mapa Cultural (API pública): 25.441 cadastrados, 2.592 coletivos. Falta saber quantos
    têm CNPJ, e a lista com município exige paginar a API.
  - Inscritos com CNPJ e município (LAI).
  - Lista de apresentações (SECULT).

### Poder: o que a proposta vai precisar informar (AMO [s.19–23])

Qualquer que seja o método, o cálculo pede o EMD relevante para a política, α, poder, a fração tratada P, a
prevalência ou o desvio-padrão do resultado e, com conglomerados, a CCI.

| Questão | Unidade e N disponível | Ordem de grandeza (α = 5%, poder 80%) |
| --- | --- | --- |
| H1b | 293 projetos resolvidos em 2022-2024 (P = 0,68) | EMD de 14 a 17 pontos percentuais em Y binário |
| H1b | margem do racionamento: 20 a 30 por grupo | 29 a 43 pontos |
| H3 | 1.000 a 4.000 agentes, individual | 1,2 a 5,3 pontos, para inscrição de base de 2% a 10% |
| H3 | 71 municípios do interior, m = 20 a 50 | 2,9 a 6,3 pontos |

Fonte: `07_poder_hipoteses.csv`. O N de H3 cabe no universo do Mapa Cultural (25.441 agentes, 2.592 coletivos); a
prevalência de base e a CCI seguem hipóteses. Essas contas
já mostram, sem escolher método, que a margem do racionamento só detecta efeitos enormes.

## 5. O que muda no artigo (proposta; decisão dos autores)

1. **§ 4.1 Teoria da mudança.**
   - Trocar o Quadro 2 pela cadeia do Passo 2, com quem decide em cada elo.
   - Acrescentar a figura em árvore (`08_teoria_da_mudanca.png`, formato J-PAL de TdM [s.11]), com H1–H3 como
     premissas marcadas nos elos.
   - Reescrever a hipótese causal (Passo 4).
   - Pôr o funil de atrito (§ 2) numa tabela curta.
2. **§ 4.2 Avaliação do desenho.** Organizar pelos elos (entrada, habilitação, captação, validação, entrega) e usar o
   mapeamento (§ 3) como síntese. Isso resolve o bloqueio B2 do Stage 3 (separar habilitação de captação), e o
   "se sustenta mal" da conclusão vira "contestado" na captação e "indeterminado" na entrada e na entrega.
3. **§ 5 Proposta.** Organizar por H1–H3: pergunta, parâmetro, vieses da comparação ingênua, SUTVA, dados e
   variações que a política produz (§ 4). Os métodos aparecem como candidatos, a decidir na segunda parte do curso.
   - O desenho da amostra, as fontes e o poder continuam obrigatórios: a Tabela 2 passa a ter uma linha por
     questão.
   - O D1 atual (efeito da captação sobre emprego do proponente) cabe como resultado secundário de H1b (RI2), ou
     sai.
4. **Páginas.** A figura ocupa cerca de meia página; o limite é 15. O corte vem das redundâncias apontadas no Stage 3
   (SUG-3).

## 6. Pedidos de dados (LAI à SECULT; SEFAZ para a fila de validação)

1. Inscrições por ciclo, 2022-2026: todas, inclusive inabilitadas e arquivadas, com motivo, CNPJ, município da
   sede, linguagem, valor pedido e data (A1, A2; H2, H3).
2. Pareceres favoráveis arquivados sem carta de intenção em 120 dias, 2025-2026 (H2).
3. Data e ordem de validação de cada termo, 2023-2024, inclusive os indeferidos (H1b, H2).
4. Relatórios de execução: público, gratuidade, locais (RI1; H1b).
5. Apresentações da LICC nos municípios: datas e locais (H3). A página de notícia pedida ao relé deu 404.

## 7. Horizonte (fora do artigo)

Os parâmetros acima não dependem do mecanismo: passagem por elo, custo de entrada, pesos de quem escolhe contra
preferências da população, e adicionalidade. São a linha de base contra a qual qualquer alternativa futura seria
comparada, inclusive um mapa da cultura com financiamento quadrático sobre o licc.gov. O artigo avalia a LICC como ela
está e não trata disso.

## Referências

Material da disciplina (sínteses em `notas/disciplina/`, com página e slide):

- GERTLER, P. J. *et al.* **Avaliação de impacto na prática**. 2. ed. Washington, DC: Banco Mundial, 2018.
  [VERIFICAR o DOI da edição em português, como em `03-gertler.md`]
- HM TREASURY. **The Magenta Book**: central government guidance on evaluation. London, 2026.
- WHITE, H.; RAITZER, D. A. **Impact evaluation of development interventions**: a practical guide. Manila: Asian
  Development Bank, 2017.
- WILLIAMS, M. J. External validity and policy adaptation: from impact evaluation to policy design. **The World Bank
  Research Observer**, v. 35, n. 2, p. 158-191, 2020.
- Slides PECO 5046-6046 (Giuberti, 2026) e Módulo 03 do J-PAL (Araújo, 2017). O funil de atrito é atribuído a White
  (2013) nos slides [VERIFICAR a referência completa].

Conferidas na Crossref pelo relé em 24/09/2026 (`dados/fontes_web/doi/`):

- BERTRAND, M.; BOMBARDINI, M.; FISMAN, R.; TREBBI, F. Tax-exempt lobbying: corporate philanthropy as a tool for
  political influence. **American Economic Review**, v. 110, n. 7, p. 2065-2102, 2020. DOI: 10.1257/aer.20180615.
- BHARGAVA, S.; MANOLI, D. Psychological frictions and the incomplete take-up of social benefits: evidence from an
  IRS field experiment. **American Economic Review**, v. 105, n. 11, p. 3489-3529, 2015. DOI: 10.1257/aer.20121493.
- CORNWELL, T. B.; MAIGNAN, I. An international review of sponsorship research. **Journal of Advertising**, v. 27,
  n. 1, p. 1-21, 1998. DOI: 10.1080/00913367.1998.10673539.
- DESHPANDE, M.; LI, Y. Who is screened out? Application costs and the targeting of disability programs.
  **American Economic Journal: Economic Policy**, v. 11, n. 4, p. 213-248, 2019. DOI: 10.1257/pol.20180076.
- FINKELSTEIN, A.; NOTOWIDIGDO, M. J. Take-up and targeting: experimental evidence from SNAP. **The Quarterly
  Journal of Economics**, v. 134, n. 3, p. 1505-1556, 2019. DOI: 10.1093/qje/qjz013.
- HAINMUELLER, J.; HOPKINS, D. J.; YAMAMOTO, T. Causal inference in conjoint analysis: understanding
  multidimensional choices via stated preference experiments. **Political Analysis**, v. 22, n. 1, p. 1-30, 2014.
  DOI: 10.1093/pan/mpt024.
- KLEVEN, H. J.; KOPCZUK, W. Transfer program complexity and the take-up of social benefits. **American Economic
  Journal: Economic Policy**, v. 3, n. 1, p. 54-90, 2011. DOI: 10.1257/pol.3.1.54.
- MOYNIHAN, D.; HERD, P.; HARVEY, H. Administrative burden: learning, psychological, and compliance costs in
  citizen-state interactions. **Journal of Public Administration Research and Theory**, v. 25, n. 1, p. 43-69,
  2015. DOI: 10.1093/jopart/muu009. (A Crossref registra a publicação on-line em 2014.)
- NAVARRO, P. Why do corporations give to charity? **The Journal of Business**, v. 61, n. 1, p. 65-, 1988. DOI:
  10.1086/296420. (A Crossref só dá a página inicial.)

Também conferidas e úteis para a segunda parte (desenhos com interferência e experimentos de mecanismo):
BAIRD, S.; BOHREN, J. A.; McINTOSH, C.; ÖZLER, B. **The Review of Economics and Statistics**, v. 100, n. 5,
p. 844-860, 2018, DOI 10.1162/rest_a_00716; LUDWIG, J.; KLING, J. R.; MULLAINATHAN, S. **Journal of Economic
Perspectives**, v. 25, n. 3, p. 17-38, 2011, DOI 10.1257/jep.25.3.17.
