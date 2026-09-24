# Hipóteses H1–H3: o que estimar para avaliar a LICC

Pedido dos autores (24/09/2026): fundamentar o que precisa ser estimado para avaliar a LICC **como ela está**,
com inferência causal e com os métodos da disciplina, para testar três hipóteses:

- **H1 (escolha)**: a coordenação centralizada (edital e habilitação) combinada com a escolha da empresa favorece
  empresas que usam o crédito de ICMS como orçamento de marketing.
- **H2 (funil)**: poucos projetos passam.
- **H3 (atrito)**: é caro e difícil se inscrever e chegar à habilitação.

O exemplo da batalha de rima contra a música de concerto era só analogia. Esta nota substitui a leitura por
linguagem da nota 02 como eixo e reaproveita dela os estimandos E1–E4.

Números: `analise/07_hipoteses_h1_h3.py` → `analise/tabelas/07_*.csv`, salvo quando se indica outra tabela.
O financiamento quadrático aparece só no § 8, como horizonte fora do artigo.

## 1. Onde cada hipótese entra na teoria da mudança e no grafo do licc.gov

O licc.gov modela a LICC como o SF Government Graph do CivLab modela a prefeitura: entidades tipadas, relações
nomeadas e âncora legal em toda entidade (`licc-gov/` e `fcarva/licc.gov/docs/ontologia.md`). O ponto útil para a
avaliação é que **os anéis seguem o dinheiro**:

> População capixaba (financiadora indireta e beneficiária final) → Aprovação e fomento (SECULT, SEFAZ, CEC, CAP)
> → O capital (empresas) → A execução (proponentes) → O bem público (projetos por linguagem).

Cada aresta do grafo é um elo da teoria da mudança (Módulo 03). Cada hipótese nega uma premissa desse elo:

| Hipótese | Premissa da teoria da mudança que ela nega | Aresta do licc.gov | Indicador do licc.gov | O elo tem dado público? |
| --- | --- | --- | --- | --- |
| H3 atrito | Agentes culturais com bons projetos conseguem se inscrever | `inscrito_em` (projeto → edital) | quem executa | **Não.** A API do Mapa Cultural devolve lista vazia para as inscrições de 2025 (`mapa_api_inscricoes_1878.txt`); os inscritos não habilitados não são publicados |
| H2 funil | A habilitação seleciona pelo mérito, e o teto financia os habilitados | `aprova` (CAP → projeto) | autorizado que virou dinheiro (conversão) | Em parte: habilitados e status por ciclo; termos indeferidos só nos anexos de 2023 e 2024 |
| H1 escolha | A empresa escolhe, entre os habilitados, projetos alinhados ao interesse público | `patrocina` (a única aresta que move R$) | concentração do capital | Sim para 2022-2026, nos anexos de captação (projeto × patrocinador × valor) |
| Resultado final | O projeto financiado entrega bem público à população | `beneficia` (projeto → população) | nenhum | **Não** (público, gratuidade e local executado não são publicados) |

Lida assim, a tabela já é um achado de desenho: **o único elo com dado completo é o do dinheiro**. Os dois elos que
as hipóteses mais precisam (entrada e benefício) são opacos. É a "cadeia de responsabilização" do licc.gov com
buracos, e cada buraco é um pedido de LAI (§ 7).

## 2. H2 — "poucos projetos passam": três filtros, não um

O funil tem três filtros com decisores diferentes. A hipótese só é testável se eles forem separados
(`07_funil_por_ciclo.csv`, `07_funil_captacao_anual.csv`):

| Filtro | Quem decide | O que o dado mostra | Cobertura |
| --- | --- | --- | --- |
| 1. Inscrição → habilitação | parecerista e CAP ("avaliação documental" no Mapa Cultural; habilitação binária, sem nota nem ranking) | **indeterminado**: sem inscritos | 0 de 5 ciclos |
| 2. Habilitação → captação | empresa | captou/resolvidos: 84% (2022), 70% (2023), 55% (2024); 95 dos 293 resolvidos expiraram | ciclos 2022-2024 |
| 3. Termo → validação | teto e ordem de validação na SEFAZ | a demanda com patrocinador foi 1,28 × o montante em 2023 e 1,35 × em 2024; 11 e 22 termos indeferidos por ultrapassar o montante | anos de captação 2023 e 2024 |

Três leituras:

1. **No filtro 3, "poucos passam" não é falta de interesse de empresas.** Em 2023-2024 havia empresa disposta a
   patrocinar 28% e 35% além do teto. Na margem, o que corta é o teto, e a ordem de validação decide quem fica.
2. **A mudança de regime em 2025 escondeu o filtro 2.** Desde a IN 001/2025 (termos de ≥ 35% antes da CAP) e a
   Portaria 062-S/2025 (carta de intenção em 120 dias, sob pena de arquivamento), só chega à habilitação quem já tem
   patrocinador. A expiração cai para 3 de 56 resolvidos no ciclo 2025, e os habilitados caem de 123 para 74. A
   seleção pela empresa não diminuiu: foi para antes da etapa publicada. Os projetos com parecer favorável
   arquivados sem carta são o novo "expirado", e ninguém os publica.
3. **H2 é pergunta de desenho, não de impacto.** Os estimandos são taxas de passagem por filtro e por grupo,
   P(habilitação | inscrição, X), P(captação | habilitação, X) e P(validação | termo, X), com X = território,
   recorrência, natureza jurídica, faixa de valor e linguagem. São descritivos e entram na avaliação do desenho
   (seção 4 do artigo). Não precisam de contrafactual. Precisam dos inscritos.

## 3. H1 — "orçamento de marketing": o que a hipótese prevê e o que os dados já dizem

Com crédito de 100%, a empresa não põe dinheiro próprio. Ela escolhe onde vai o ICMS que pagaria e fica com a marca
(O'Hagan; Harvey, 2000). Patrocínio é comunicação de marketing (Cornwell; Maignan, 1998), e a doação
corporativa responde a motivos de lucro, como publicidade (Navarro, 1988). Usar o crédito como marketing é o
comportamento esperado, não um desvio. Para a avaliação,
a pergunta é se essa escolha **custa bem público**. Isso se desdobra em três previsões testáveis:

| Previsão | Estimando | O que já se vê | Leitura |
| --- | --- | --- | --- |
| (a) A escolha pesa atributos de visibilidade (valor no teto, evento grande e calendarizado, RMGV) mais que os de bem público (gratuidade, formação, periferia) | pesos β da empresa num logit condicional sobre o cardápio vigente (nota 02, E3) | no teto de R$ 500 mil a conversão é de 83%, contra 52% abaixo de R$ 200 mil (`03_status_conversao_por_faixa_valor_2022_2024.csv`) | compatível com H1 **e** com patrocínio pré-acordado: quem já tem empresa pede o teto (DA-2, Stage 3) |
| (b) O capital concentra-se em setores com exposição de marca e regulatória | concentração e composição setorial | 2 empresas somam metade de 2025; CR1 = 0,44; energia e gás (serviço regulado) = 52% (`03_patrocinadores_concentracao.csv`, `03_patrocinadores_macrossetor.csv`) | compatível com H1; empresas também usam a filantropia como instrumento de influência política (Bertrand et al., 2020), motivo plausível para concessionária regulada. O limite por patrocinador proporcional ao ICMS devido também explica a concentração |
| (c) A escolha desfavorece o interior e os estreantes | diferença de conversão por grupo dentro do cardápio | execução 68% na RMGV e 63% no interior; recorrentes 71% e estreantes 57% (2023-2024) | território: diferença pequena. Recorrência: compatível com H1 (relação com a marca) **e** com capacidade (DA-1) |

Há também evidência **contra** a versão territorial de H1. Sob o regime "patrocinador primeiro", a fatia RMGV do
valor atribuível a um município **caiu** de 74% (2024) para 57% (2025) e ficou em 67% (2026), com cobertura
de 107/123, 51/74 e 54/88 registros (`07_composicao_por_ciclo.csv`). A
maior patrocinadora de 2025 tem carteira dominada por cultura popular do interior (nota 02, § 1). O que H1 prevê
com mais força não é "a empresa não vai ao interior". É "a empresa financia o que aconteceria de todo modo". Esse é
o ponto causal:

- **Adicionalidade** (nota 02, E1). Seja Y_j = 1 se o bem público j acontece (e chega ao público). O efeito do
  financiamento é τ_j = Y_j(1) − Y_j(0). Se a empresa escolhe eventos consolidados que ela já patrocinaria com
  verba própria, τ_j ≈ 0: a LICC troca gasto privado de marketing por receita pública, e o bem público é o mesmo.
  O estimando é o EMPT, E[τ | D = 1], junto com o contraste EMPT × EMPNT, que mede se a escolha acerta o alvo (E2).
- **Substituição no nível da empresa.** Com D_f = 1 a partir do ano em que a empresa f passa a patrocinar pela
  LICC, o estimando é o efeito sobre o patrocínio cultural que ela fazia fora da LICC (Rouanet, verba própria).
  Uma queda indica que a LICC substitui patrocínio que já existia. Os 46 CNPJs que patrocinaram em 2025 (26 empresas pela raiz) foram
  enviados ao relé para consulta no SALIC (incentivadores). A verba própria não é observável.
- **A cunha** (nota 02, E3). Os pesos da empresa (a) contra os pesos da população nos mesmos atributos, medidos por
  experimento de escolha (AMCE; Hainmueller; Hopkins; Yamamoto, 2014). É o único estimando que põe a população, a
  "estrela" central do grafo, na avaliação.

## 4. H3 — atrito na entrada: o que a norma impõe e o que o dado sugere

**O que a norma impõe** (IN 001/2025, arts. 13, 14, 17 e 19; `notas/politica/fontes/in-licc-001-2025.md`):

- inscrição só on-line, no Mapa Cultural;
- **CNPJ** com finalidade cultural no ato constitutivo (pessoa física não se inscreve; o MEI tem limite de valor);
- comprovante de sede no ES **em nome do agente**;
- certidão negativa estadual;
- formulário, planilha de custos no modelo, cartas de anuência, currículos, plano de distribuição e, conforme o
  caso, plano pedagógico, plano de comercialização, memorial descritivo, autorização do órgão de tombamento e
  roteiro;
- teto menor (R$ 300 mil) para evento em primeira edição;
- a norma prevê pagar a elaboração do projeto com recurso da LICC (art. 19, II, "j"), o que indica um mercado de
  elaboradores;
- desde 2025, o proponente precisa conseguir o patrocinador **antes** da habilitação, sem certificado para mostrar
  à empresa;
- as janelas mudam: em 2024 as inscrições foram fechadas por esgotamento do teto (Portaria 078/2024). As
  oportunidades do Mapa Cultural (479, 1415, 1878 e 2317) aparecem com "avaliação documental" e datas de
  encerramento que misturam inscrição e retorno de diligências
  (`dados/externos/mapa-cultural-licc-oportunidades-metodo-avaliacao-2026-09-23.jsonl`).

**O que o dado sugere** (`07_composicao_por_ciclo.csv`, `03_coortes_primeira_presenca_canonico.csv`):

- A entrada de proponentes novos caiu com o regime "patrocinador primeiro": 56 estreantes em 2024, 26 em 2025, 40
  em 2026. Estreante é quem não aparece em t−1 nem em t−2, janela fixa para não confundir com o envelhecimento do
  painel. A fatia de recorrentes subiu de 41% para 54% e voltou a 45%.
- A difusão territorial parou: 39 municípios entraram em 2022, 16 em 2023 e 3 por ciclo depois disso. Os 14
  municípios que nunca entraram são todos do interior.
- Leitura honesta: nada disso isola o atrito. O teto, as janelas e as regras mudaram ao mesmo tempo. A comparação
  com a Rouanet-ES (proponentes do ES, mesma janela fixa) serviria de grupo de comparação, mas o download do SALIC
  de 2025 está incompleto (6.000 de 15.415 projetos; `07_rouanet_es_composicao.csv`). O script deixa a diferença
  em diferenças vazia até completar. Mesmo completa, seriam dois grupos e dois períodos: descrição, não
  identificação.

**O que estimar.** O atrito só é identificado se for **mexido de forma exógena**:

- **Estimando principal**: o efeito de intenção de tratar (ITT) de reduzir o atrito sobre P(inscrição),
  P(habilitação) e P(captação) de agentes culturais sem inscrição prévia.
- **Estimandos de focalização** (Finkelstein; Notowidigdo, 2019; Deshpande; Li, 2019): quem são os
  que entram por causa da redução, os *compliers* (interior, coletivos, sem CNPJ), e se passam nos filtros 1 e 2
  na mesma taxa que os demais.
  - Se passam menos, o atrito funciona em parte como triagem útil (Nichols; Zeckhauser, 1982 [VERIFICAR];
    Kleven; Kopczuk, 2011).
  - Se passam igual, o atrito exclui sem selecionar.
- O conceito na literatura de administração pública é **custo administrativo** (Moynihan; Herd; Harvey, 2015):
  custos de aprendizado, de conformidade e psicológicos. Em programas sociais, simplificar e informar aumenta a
  adesão de elegíveis (Bhargava; Manoli, 2015).

## 5. Quadro de estimandos, identificação, dados e poder

| # | Hipótese | Estimando | Identificação | Dados | EMD (80%, α = 5%) | Viável até 28/09? |
| --- | --- | --- | --- | --- | --- | --- |
| F1 | H2 | taxas de passagem por filtro × grupo | descritivo | habilitados e anexos (filtros 2-3); inscritos via LAI (filtro 1) | — | filtros 2-3 sim |
| F2 | H2 | teto obrigatório: demanda ÷ montante | descritivo | anexos 2023-2024 | — | sim (1,28 e 1,35) |
| C1 | H1 | pesos β da empresa | logit condicional; cardápio exógeno à empresa | anexos 2022-2026 + lista de habilitados "captando" em cada data | — | parcial (sem data do termo) |
| C2 | H1 | adicionalidade EMPT, E[Y(1) − Y(0) \| D = 1] | racionamento pelo teto 2023-2024 (validados logo antes do esgotamento × indeferidos) | anexos 2023-2024; ocorrência pelo Mapa Cultural, SALIC, DIO, nova habilitação | 29-43 pontos com 20-30 projetos por braço | só o desenho |
| C3 | H1 | idem, captou × expirou | observacional, com limites de Manski (seleção) | 198 captaram × 95 expiraram (2022-2024) | 14-17 pontos (o viés domina) | só o desenho |
| C4 | H1 | substituição do patrocínio da empresa | DiD escalonado por empresa (primeiro ano na LICC) | SALIC incentivadores por CNPJ (no relé) | a calcular com o n de empresas | não |
| C5 | H1 | cunha: AMCE da população − pesos da empresa | experimento de escolha (atributos sorteados) | questionário (LGPD e comitê de ética) | a calcular | não |
| A1 | H3 | ITT de reduzir o atrito sobre inscrição e habilitação | **experimento de encorajamento** (assistência técnica e informação), sorteado | Mapa Cultural (universo de agentes; contagem pedida ao relé) + inscritos (LAI) | individual, N = 1.000-4.000: 1,2-5,3 pontos; por município (71 do interior, m = 20-50, CCI 0,02-0,05): 2,9-6,3 pontos | só o desenho |
| A2 | H3 | composição sob o regime "patrocinador primeiro" | série interrompida / DiD contra a Rouanet-ES | habilitados 2022-2026; SALIC completo | sem erro-padrão confiável (2 grupos) | descritivo |

Parâmetros de poder em `07_poder_hipoteses.csv`, com as fórmulas de `05_poder_mde.py` (3ie WP26 7.1.3-7.1.4 e
7.2.1-7.2.2; slides de amostragem e poder). N, p0, m e CCI de A1 são **hipóteses ilustrativas** até a contagem de
agentes no Mapa Cultural e a taxa de inscrição de base.

### Ameaças que mudam o estimando (vocabulário da disciplina)

- **SUTVA e interferência pelo teto.** O teto torna a captação soma zero: se o encorajamento de A1 aumenta a entrada,
  os novos projetos disputam o mesmo montante e deslocam outros. O ITT sobre **captação** é de equilíbrio parcial.
  Os resultados de entrada (inscrição e habilitação) sofrem menos, e o desenho em dois níveis (saturação sorteada
  por município; Baird et al., 2018) mede o deslocamento.
- **Seleção sobre ganhos** (C2, C3): proponentes que sabem que o evento sai de todo modo podem desistir de captar,
  e a comparação ingênua superestima a adicionalidade.
- **Ordem de validação** (C2): pode refletir organização do proponente (chega antes quem é mais estruturado). Testar
  balanço nos atributos observáveis e confirmar com a SEFAZ como a fila é formada.
- **Validade externa**: C2 e C3 valem para o regime 2022-2024 ("habilitação primeiro"); o regime atual não gera
  expirados publicados.
- **Tempo**: até 2 anos de captação e 2 de execução. A1 mede inscrição e habilitação no ciclo seguinte ao sorteio;
  captação e execução, com 1 a 2 anos de defasagem.

## 6. O que isso sugere para a seção 5 do artigo (decisão dos autores)

A disciplina pede desenho de impacto com amostra, fonte de dados e poder. Das hipóteses, só H3 admite um desenho
prospectivo limpo **sem mexer no mecanismo**. A1 é um experimento de mecanismo (Ludwig; Kling; Mullainathan,
2011): testa um elo da teoria da mudança (a entrada), não o efeito do programa inteiro. A1 acrescenta informação e assistência e não altera teto, cotas,
crédito nem a escolha da empresa, o que já estava registrado como compatível com o escopo em
`notas/politica/01-desenho-legal.md`, § 16. H1 tem identificação retrospectiva fraca (C2 só detecta efeitos de ~30
pontos ou mais). H2 é descritiva.

**Recomendação.** Reorganizar a seção 5 em torno das hipóteses, em cerca de 3 páginas:

1. **5.1 Perguntas e estimandos.** H1–H3 como premissas da teoria da mudança (quadro do § 1); o que é descritivo
   (F1, F2, C1), que vai para a seção 4, e o que é causal.
2. **5.2 Desenho principal: encorajamento na entrada (A1).**
   - Unidade: agente cultural sem inscrição prévia, ou o município como conglomerado.
   - Sorteio estratificado RMGV × interior; tratamento: oficina, assistência para CNPJ e documentação, e
     informação sobre patrocinadores.
   - Resultados: inscrição, habilitação e captação.
   - Amostra e poder: tabela 07.
   - Ameaça: interferência pelo teto, tratada com saturação sorteada.
3. **5.3 Desenho complementar: adicionalidade pelo racionamento do teto (C2)**, que também atende ao REV-3 do Stage 3,
   com o EMD declarado e os limites de C3 como robustez.
4. **5.4 Dados a pedir** (§ 7).

O D1 atual (efeito da captação sobre o proponente, DiD escalonado) passa a parágrafo de agenda. Isso **dispensa** o
REV-1 e o REV-2 do roteiro do Stage 3, que só existem por causa dele. Os demais itens (REV-3 a REV-7) continuam.

**Custo.** Reescrever a seção 5 e parte da 4 a quatro dias da entrega. **Contrapartida.** O artigo passa a testar
as hipóteses dos autores, e não uma pergunta que eles não fizeram. A alternativa conservadora é manter o D1 com
REV-1/REV-2 e pôr H1–H3 como perguntas da avaliação do desenho (seção 4), com A1 em um parágrafo.

## 7. Pedidos de dados (LAI à SECULT; SEFAZ para a fila de validação)

1. Inscrições por ciclo, 2022-2026: todas, inclusive inabilitadas e arquivadas, com motivo, CNPJ, município da
   sede, linguagem, valor pedido e data (filtro 1; H2, H3).
2. Pareceres favoráveis arquivados sem carta de intenção em 120 dias, 2025-2026 (o "expirado" do regime novo; H2).
3. Data e ordem de validação de cada termo de compromisso, 2023-2024, inclusive os indeferidos (C2).
4. Relatórios de execução: público estimado, gratuidade, locais (resultado final; H1, adicionalidade).
5. Participantes das apresentações da LICC nos municípios (a página de notícia pedida ao relé deu 404; A1 e desenho
   municipal).

## 8. Horizonte (fora do artigo): por que medir isso agora

Os estimandos acima não dependem do mecanismo: custo de entrada (A1), passagem por filtro (F1), cunha entre quem
escolhe e a população (C5) e adicionalidade (C2). São a linha de base contra a qual qualquer alternativa futura seria
comparada, inclusive a do licc.gov como mapa da cultura com financiamento quadrático. Medi-los sobre a LICC como ela
está é o que o artigo pode fazer. A comparação com outro mecanismo fica para depois e não entra no texto.

## Referências

Já conferidas (Crossref, via relé): ver a nota 02 (Andreoni; Athey; Wager; Bergstrom; Blume; Varian; Hainmueller;
Hopkins; Yamamoto; Heckman; Vytlacil; Kitagawa; Tetenov; Manski; Samuelson).

Conferidas na Crossref pelo relé em 24/09/2026 (`dados/fontes_web/doi/`):

- BAIRD, S.; BOHREN, J. A.; McINTOSH, C.; ÖZLER, B. Optimal design of experiments in the presence of interference.
  **The Review of Economics and Statistics**, v. 100, n. 5, p. 844-860, 2018. DOI: 10.1162/rest_a_00716.
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
- KLEVEN, H. J.; KOPCZUK, W. Transfer program complexity and the take-up of social benefits. **American Economic
  Journal: Economic Policy**, v. 3, n. 1, p. 54-90, 2011. DOI: 10.1257/pol.3.1.54.
- LUDWIG, J.; KLING, J. R.; MULLAINATHAN, S. Mechanism experiments and policy evaluations. **Journal of Economic
  Perspectives**, v. 25, n. 3, p. 17-38, 2011. DOI: 10.1257/jep.25.3.17.
- MOYNIHAN, D.; HERD, P.; HARVEY, H. Administrative burden: learning, psychological, and compliance costs in
  citizen-state interactions. **Journal of Public Administration Research and Theory**, v. 25, n. 1, p. 43-69,
  2015. DOI: 10.1093/jopart/muu009. (A Crossref registra a publicação on-line em 2014.)
- NAVARRO, P. Why do corporations give to charity? **The Journal of Business**, v. 61, n. 1, p. 65-, 1988. DOI:
  10.1086/296420. (A Crossref só dá a página inicial.)

Sem DOI, a conferir: NICHOLS, A. L.; ZECKHAUSER, R. J. Targeting transfers through restrictions on recipients.
**American Economic Review**, v. 72, n. 2, p. 372-377, 1982 [VERIFICAR].

Já no artigo: O'HAGAN; HARVEY (2000).
