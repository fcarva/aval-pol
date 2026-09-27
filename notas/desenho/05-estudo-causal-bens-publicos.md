# Estudo causal: o financiamento de bens públicos culturais pela LICC

> **deep-research, modo full, Fase 1 (escopo).** Contém o brief da pergunta, o blueprint metodológico e o
> checkpoint 1 do advogado do diabo. Pedido do autor em 24/09/2026: "buscar forma melhor … de fazer um estudo de
> inferência causal para avaliar o financiamento de bens públicos culturais a partir da LICC", deixando pontas em
> aberto para a 2ª parte da disciplina (aulas de 07/10 a 25/11).
>
> - As regras citadas estão conferidas nas normas (`notas/politica/fontes/`) e nos anexos (`dados/fontes_web/`).
> - A literatura marcada **[relé]** foi pedida ao relé em 24/09/2026 (`dados/fontes_web/dois.txt` e `buscas.tsv`)
>   e só entra no artigo depois de conferida (regra do CLAUDE.md).
> - Fases 2 a 6 (bibliografia verificada, síntese, relatório, revisão) aguardam a confirmação do autor
>   (checkpoint 1).

## 1. Brief da pergunta (research_question_agent)

**Tema.** O Estado abre mão de ICMS, e uma empresa privada escolhe qual projeto recebe. Quanto de bem público
cultural isso produz, e para quem?

**Pergunta principal (causal).** Receber financiamento pela LICC aumenta a provisão de bens culturais com
características de bem público? A provisão se mede pela realização do projeto no ano previsto, pelo público,
pela gratuidade e pelas ações fora da RMGV. Quanto disso seria provido sem a LICC (adicionalidade)?

**Subperguntas.**

1. **Adicionalidade (H1b).** Para o projeto na margem do teto, receber agora, e não depois ou nunca, muda se ele
   acontece, quando e com que alcance?
2. **Seleção pelo Estado (H2a).** A avaliação técnica da SECULT (parecer e certificado) muda o destino do projeto,
   ou apenas registra o que a empresa escolheria de qualquer forma?
3. **Quem fica de fora (H1a e H3).**
   - Projetos menores, de áreas com pouca visibilidade e do interior captam menos porque valem menos ao
     patrocinador (seleção pela empresa) ou porque entram menos e pior (atrito)?
   - Reduzir o atrito muda a composição de quem é financiado?

**FINER.**

| Critério | Avaliação |
| --- | --- |
| Factível | Parcial. O dado público cobre tratamento e intensidade; o resultado e as chaves (CNPJ, parecerista, datas da SEFAZ, relatório de execução) dependem de LAI |
| Interessante | Sim. É um gasto tributário de R\$ 25-31 milhões por ano, crescente e sem avaliação prevista |
| Novo | Sim. Não localizamos avaliação causal de incentivo cultural via ICMS no Brasil (artigo, §3) |
| Ético | Sim, se os desenhos não negarem acesso a elegíveis: a oferta a H3 chega aos controles ao fim; dados identificados exigem anonimização (LGPD) |
| Relevante | Sim. A SECULT fixa teto, cotas e fluxo por instrução normativa anual, e as respostas mudam essas escolhas sem mexer no mecanismo |

**Escopo.**

- **Dentro:** efeitos da LICC como ela está, de 2022 a 2026: habilitação, captação, execução e público.
- **Fora:** redesenho do mecanismo, incluindo financiamento quadrático (regra do projeto); efeito sobre a
  arrecadação; bem-estar do patrocinador.

## 2. As regras que geram variação (insumo do desenho)

| Regra | Fonte | Que variação gera |
| --- | --- | --- |
| Termos validados até esgotar o teto e cada cota do art. 18, com data e hora de recebimento no anexo (2025-2026) | IN 001/2025, art. 18; anexos de captação | Corte no tempo: termos que chegaram antes ou depois do esgotamento. Em 2025, a cota IV (50%) fechou em 28/01 às 16:02 (`09_cotas_2025_2026.csv`) |
| Termos "indeferidos por ultrapassar o montante" em 2023 e 2024: 32 projetos com patrocinador disposto | anexos 2023 e 2024 | Instrumento binário de recusa. Primeiro estágio: 13 de 32 nunca captaram depois (`09_reentrada_resumo.csv`) |
| Distribuição dos projetos aos pareceristas por ordem de inscrição e área, "de forma isonômica" | edital de credenciamento 001/2025, itens 2.1-2.4 | Designação quase aleatória do avaliador dentro de área e período. A severidade do parecerista serve de instrumento |
| Parecer favorável emite o certificado de aptidão; a CAP só delibera sobre inabilitação e depois de 35% de patrocínio | IN 001/2025, arts. 40, 41 e 45 | O parecer é decisivo para o projeto entrar no "cardápio" |
| Reforma de 2025: patrocinador antes da CAP, cotas do art. 18, inscrições fechadas em 2024 | IN 001/2025; SECULT (2024b; 2025b) | Choque de regra por coorte, confundido por mudanças simultâneas |
| Seis linhas de financiamento com limites por projeto próprios, sem reserva do teto por linha | IN 001/2025, arts. 9º e 14-16 | Nenhuma variação exógena por área. A área é covariável obtida por LAI |
| Nenhuma nota para projetos; o método do Mapa é "simplificado" (situação da inscrição) | modelos de parecer de 2022 e 2026; código do Mapas Culturais, `EvaluationMethodSimple`, commit `3f35b95` | Não há corte de nota, e portanto não há RD na habilitação |

## 3. Blueprint metodológico (research_architect_agent)

**Paradigma.** Pós-positivista, resultados potenciais (Rubin). O parâmetro-alvo muda por pergunta; declará-lo é a
primeira escolha do desenho.

**Unidade de análise.** O projeto-ano para a adicionalidade (H1b) e a seleção pelo Estado (H2a). O agente cultural
para a entrada (H3). O proponente-ano para os painéis.

**Resultados (*Y*), da teoria da mudança:**
- o projeto acontece no ano previsto (relatório de execução; agenda do Mapa Cultural; extratos do DIO);
- público e gratuidade: lista de presença e estimativa de público no relatório de execução (IN 001/2025,
  art. 66, I, e), dado interno pedido por LAI;
- execução fora da RMGV;
- troca de fonte: captação pela Rouanet no SALIC, por CNPJ.

### 3.1 Estratégias comparadas (uma por método da 2ª parte)

| Método (aula) | Pergunta | Parâmetro | Hipótese de identificação | Teste possível | Dado | Poder / tamanho |
| --- | --- | --- | --- | --- | --- | --- |
| **RD no tempo** (18/11) | H1b, H2b | Efeito de receber agora para o termo na margem do esgotamento (local) | A hora de chegada não se liga ao projeto perto do corte; não há manipulação da hora | Densidade das chegadas e balanceamento de covariáveis perto do corte | Hora de protocolo e de validação de **todos** os termos, inclusive recusados (SEFAZ, LAI) | Baixo por cota-ano: 2 a 4 termos validados nas 72 h antes do fechamento (`09_termos_2025_2026.csv`). Exige empilhar cotas e anos (2023-2026) |
| **VI: recusa pelo teto** (11/11) | H1b | LATE de receber em algum momento, para os que a recusa impede (*compliers*) | A recusa só afeta *Y* pela captação (exclusão). Monotonicidade | Primeiro estágio 41% (13/32); comparar pré-tratamento de recusados e validados no mesmo dia | Anexos 2023-2024 (público) + *Y* | 32 × 32: EMD 28-34 pp na forma reduzida (Tabela 2 do artigo). Só efeitos grandes |
| **VI: severidade do parecerista** (11/11) | H2a | Efeito do parecer favorável (certificado sem diligência) sobre captação e realização, para os projetos cuja sorte depende do avaliador | Designação como aleatória dentro de área e período (edital 2.1-2.4); o parecerista só afeta *Y* pelo parecer; monotonicidade entre avaliadores | Balanceamento de covariáveis entre pareceristas; severidade *leave-one-out*; teste de monotonicidade (Frandsen *et al.* [relé]) | Parecerista e parecer por inscrição: o Mapa registra o avaliador de cada fase (LAI) | Depende do número de pareceristas e de projetos por avaliador; a calcular com o dado |
| **Diferenças em diferenças** (21/10 e 04/11) | H1b, H1a | Efeito sobre os tratados (EMPT) de entrar na LICC, e efeito da reforma de 2025 sobre a composição (porte, interior) | Tendências paralelas entre proponentes que captam e os que não captam (ou entre porte e território na reforma) | Pré-tendências com vários anos antes; estimadores para adoção escalonada (Callaway e Sant'Anna [relé]) | Painel de proponente-ano com resultados antes e depois: agenda do Mapa, SALIC, RAIS por CNPJ | A reforma muda várias regras ao mesmo tempo, então identifica um pacote, não uma regra |
| **Pareamento** (14/10) | H1b | EMPT sob seleção nos observáveis: os 95 que expiraram × os que captaram no ciclo | Ignorabilidade condicional em porte, área, território, histórico e valor pedido | Sobreposição; análise de sensibilidade a não observáveis | Anexos (público) + CNPJ e porte (LAI + Receita) | 293 projetos: EMD 14-20 pp. Problema de viés, não de amostra |
| **Seleção aleatória / promoção** (07/10) | H3 | Efeito da oferta (ITT) e LATE para quem responde; composição de quem entra | Sorteio entre municípios; exclusão; saturação para medir o deslocamento pelo teto | Balanceamento; atrito diferencial | Cadastro do Mapa Cultural (público) + inscrições (LAI) | 71 municípios, 2.389 agentes: EMD 2,8-8,5 pp (Tabela 2) |
| **Controle sintético** (25/11) | Efeito agregado | Efeito da LICC (2022) sobre a participação da cultura no emprego do ES | Um ES sintético a partir de estados sem mudança de incentivo cultural em 2022 reproduz o pré-período | Placebos no espaço e no tempo (Abadie [relé]) | IBGE (SIIC/PNAD) ou RAIS por UF | Tratamento pequeno (0,1-0,2% do ICMS) contra ruído estadual; provável poder baixo. Serve como teto de plausibilidade |

### 3.2 Recomendação do arquiteto

A LICC raciona por **fila**, não por nota, e a única designação que se parece com sorteio é a **do parecerista**.
Por isso o desenho mais forte combina três braços, cada um com a hipótese de identificação ancorada numa regra
escrita:

1. **Adicionalidade:** margem do racionamento, RD no tempo + VI da recusa, empilhando 2023-2026. Só dá poder se
   a SEFAZ entregar a fila completa com as horas.
2. **Papel do Estado:** VI pela severidade do parecerista. É a leitura causal possível de H2a e a única que não
   exige mudar regra.
3. **Quem fica de fora:** descritivo com porte, área e território, depois da LAI; promoção sorteada para o atrito
   (H3).

O pareamento e o DiD entram como verificações, e o controle sintético como teto de plausibilidade do efeito
agregado.

**Validade.**
- *Interna:* SUTVA violada pelo teto fixo (o que um capta falta a outro); o deslocamento se mede pela saturação.
- *Externa:* os regimes 2022-2024 e 2025- diferem (inversão do fluxo).
- *Constructo:* "bem público cultural" se operacionaliza por gratuidade, público e local, e não pelo rótulo do
  projeto.

### 3.3 O que fica aberto para a 2ª parte (por aula)

| Aula | Ponta aberta | O que falta decidir |
| --- | --- | --- |
| 07/10 Seleção aleatória | Promoção de apoio à inscrição (H3) | Braços (documentação × patrocínio), saturação, pré-registro |
| 14/10 Pareamento | Expirados × captaram | Covariáveis de porte e área (LAI), sobreposição |
| 21/10 e 04/11 DiD | Proponente-ano; reforma de 2025 | Grupo de comparação e resultados com série anterior a 2022 |
| 11/11 VI | Recusa pelo teto; severidade do parecerista | Exclusão, monotonicidade, instrumento *leave-one-out* |
| 18/11 RD | Hora do protocolo em torno do esgotamento | Janela, densidade, empilhamento de cotas e anos |
| 25/11 Controle sintético | Participação da cultura no emprego do ES | *Donor pool* e escala do tratamento |

## 4. Checkpoint 1 (devils_advocate_agent)

| # | Objeção | Gravidade | Resposta ou pendência |
| --- | --- | --- | --- |
| 1 | "Bem público cultural" vira rótulo: um show pago numa capital não é bem público. Sem medir gratuidade e público, o estudo mede captação, não provisão | Alta | Resolvida no desenho: *Y* = realização, público, gratuidade e local, com o relatório de execução (art. 66). **Depende de LAI**; sem ela, *Y* se aproxima pela agenda do Mapa e fica "indeterminado" o alcance |
| 2 | Na severidade do parecerista, a exclusão falha se o parecerista também muda o projeto (diligências que melhoram a proposta) | Média | É efeito do parecer, não violação, se o parâmetro for "parecer favorável ou exigente". Declarar o parâmetro como pacote |
| 3 | A distribuição "por ordem de inscrição e área" pode não ser como aleatória: pareceristas de uma área podem receber projetos sistematicamente diferentes, e impedimentos (item 5.12) realocam | Média | Condicionar em área × período e testar o balanceamento. Se falhar, H2a volta a ser descritiva, e o texto já diz isso |
| 4 | O RD no tempo tem poucos termos perto do corte (2-4 em 72 h por cota) | Alta para poder | Declarar como verificação, empilhar cotas e anos e exigir a fila completa da SEFAZ; não prometer precisão |
| 5 | A reentrada (13 de 21 recusados de 2024 captaram até 2026) torna "não receber" raro: o LATE da recusa é de poucos *compliers* | Média | Separar "receber agora" (RD, forma reduzida) de "receber em algum momento" (VI), como o artigo já faz |
| 6 | O porte medido pelo valor pedido confunde tamanho com estratégia (quem tem patrocinador pede o teto) | Média | Usar o porte do proponente (Receita) e o valor pedido separadamente; a ressalva já está no artigo |
| 7 | Controle sintético com tratamento de 0,1-0,2% do ICMS dificilmente detecta algo | Baixa (escopo) | Manter como teto de plausibilidade e ponta para a aula de 25/11, sem prometer resultado |

**Veredito: PASS com pendências.** Nenhuma objeção crítica bloqueia. As pendências de dado (LAI: fila da SEFAZ,
parecerista por inscrição, relatório de execução, CNPJ, linha e área) estão declaradas.

## 5. Literatura (Fase 2, conferência)

Pedidas ao relé e **conferidas em 24/09/2026**: as 12 têm Crossref e OpenAlex com status 200, e autores, título,
periódico, volume e páginas estão em `dados/fontes_web/doi_resumo.csv`. Maestas, Mullen e Strand (2013) usam a
taxa de concessão do examinador designado como instrumento para o benefício (resumo no OpenAlex). Frandsen, Lefgren
e Leslie (2023) propõem um teste de exclusão e monotonicidade para desenhos com designação aleatória de juízes.
As marcas [relé] acima ficam resolvidas para esses DOIs.

- **Designação de avaliador como instrumento:**
  - Maestas, Mullen e Strand (2013), 10.1257/aer.103.5.1797;
  - Dobbie, Goldin e Yang (2018), 10.1257/aer.20161503;
  - Frandsen, Lefgren e Leslie (2023), 10.1257/aer.20201860.
- **Avaliação de financiamento por pares e pontuação:**
  - Jacob e Lefgren (2011), 10.1016/j.jpubeco.2011.05.005;
  - Li (2017), 10.1257/app.20150421;
  - Azoulay *et al.* (2019), 10.1093/restud/rdy034.
- **RD no tempo:** Hausman e Rapson (2018), 10.1146/annurev-resource-121517-033306.
- **Controle sintético:**
  - Abadie, Diamond e Hainmueller (2010), 10.1198/jasa.2009.ap08746;
  - Abadie (2021), 10.1257/jel.20191450.
- **DiD escalonado:** Callaway e Sant'Anna (2021), 10.1016/j.jeconom.2020.12.001.
- **Provisão privada de bens públicos:**
  - Bergstrom, Blume e Varian (1986), 10.1016/0047-2727(86)90024-1;
  - Andreoni (1990), 10.2307/2234133.
- **Buscas OpenAlex** (`buscas.tsv`): incentivos fiscais à cultura e patrocínio; RD em editais de arte; designação
  de avaliador; incentivo cultural via ICMS no Brasil.
