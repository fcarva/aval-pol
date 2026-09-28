# Revisão final frase a frase

- **Texto revisado:** `artigo/rascunho-artigo.md`, sha256 `9bd349035841425f…`, gerado por `artigo/revisao-final/gerar_frase_a_frase.py`.
- **Como usar:** cada parágrafo abre com o **passo** que ele cumpre no argumento. Cada frase vem literal, numerada como seção.parágrafo.frase, com uma caixa ☐ para marcar (☒ ok; ✎ editar). As edições vão para o `rascunho-artigo.md`; depois, rodar de novo `checar_dados.py`, `checar_referencias.py`, `gerar_tex.py --pdf` e este script.
- **Base de cada frase:**
  - *citações*: as referências que a frase cita;
  - *checagem de dados*: o número foi recalculado a partir da tabela indicada (✔ confere na última execução);
  - *⚠ números sem checagem automática*: número que nenhuma checagem cobre; conferir na norma ou na fonte citada (muitos são regras de norma, como percentuais e tetos, e não dados).

## Título

- ☐ **[0.1]** Avaliação do desenho da Lei de Incentivo à Cultura Capixaba e proposta de avaliação de impacto

## Resumo e palavras-chave

- **0.1** — *Passo:* O artigo em um parágrafo: mecanismo, o que se avalia, os achados de desenho e a proposta
  - ☐ **[0.1.1]** **Resumo.** A Lei de Incentivo à Cultura Capixaba (LICC) permite que empresas contribuintes do ICMS destinem a projetos culturais habilitados pela Secretaria da Cultura (SECULT) valores que recuperam integralmente como crédito presumido do imposto: o Estado paga, a empresa escolhe, e o público não entra na equação.
  - ☐ **[0.1.2]** Neste artigo, avalia-se o desenho da LICC: a partir da teoria da mudança derivam-se cinco premissas, por meio de normas, anexos oficiais e atas da comissão de 2022 a 2026, que orientam uma proposta de avaliação de impacto.
  - ☐ **[0.1.3]** A decisão de financiamento não mostra orientação evidente pelo valor público: duas empresas respondem por metade da renúncia de 2025, e o bem cultural oferecido à população confunde-se com o marketing das empresas.
    - checagem de dados: D03 ✔ (`analise/tabelas/03_patrocinadores_concentracao.csv`)
  - ☐ **[0.1.4]** A decisão se concentra em poucos atores: a habilitação qualifica sem priorizar, e o que excede o teto é decidido pela ordem de recebimento e validação dos termos de patrocínio.
  - ☐ **[0.1.5]** Até 13% do valor captado em 2025 poderia remunerar captação e elaboração, projetos pequenos captam cada vez menos, e só pessoas jurídicas contribuintes patrocinam.
    - checagem de dados: N51 ✔ (`analise/tabelas/10_taxa_servico_permitida_2025.csv`)
  - ☐ **[0.1.6]** A avaliação de impacto proposta faz uma pergunta, se a renúncia vai para os projetos que dependem dela, e a responde com os grupos que a própria regra cria (termos recusados por esgotamento da cota, habilitados sem patrocinador e inabilitados), com fontes de dados e poder estatístico.

- **0.2** — *Passo:* Palavras-chave
  - ☐ **[0.2.1]** **Palavras-chave:** incentivo fiscal à cultura; gasto tributário; patrocínio; bens públicos; teoria da mudança; avaliação de impacto.


## 1 Introdução

- **1.1** — *Passo:* Apresenta a lei e dimensiona a política: teto anual, teto esgotado e demanda habilitada acima do teto
  - ☐ **[1.1.1]** A Lei estadual nº 11.246/2021 incluiu na lei do ICMS um crédito presumido correspondente ao valor que o contribuinte destina a projetos culturais credenciados pela Secretaria da Cultura (SECULT), com efeitos a partir de 2022 (ESPÍRITO SANTO, 2021a).
    - citações: ESPÍRITO SANTO, 2021a
  - ☐ **[1.1.2]** A Lei de Incentivo à Cultura Capixaba (LICC) cresceu: o teto anual de captação, o montante fixado pela SEFAZ, passou de R\$ 15 milhões em 2023 para R\$ 31 milhões em 2026. [nota de rodapé: teto2022]
    - checagem de dados: D05 ✔ (`dados/externos/licc_teto_vs_icms.csv`)
    - ☐ *Nota de rodapé (teto2022):* Para 2022, a Portaria SEFAZ nº 09-R fixou R\$ 10 milhões, e a Portaria SEFAZ nº 83-R, de 26 de setembro, ampliou o montante em R\$ 5 milhões (DIO-ES, 2026): o teto de 2022 foi de R\$ 15 milhões, valor que o anexo de captação da SECULT e a lista do Portal da Transparência informam (ESPÍRITO SANTO, 2026a), dos quais R\$ 11,5 milhões foram validados.
      - citações: DIO-ES, 2026; ESPÍRITO SANTO, 2026a
      - checagem de dados: D65b ✔ (`analise/tabelas/16_transparencia_resumo.csv (LIMITE PORTARIA SEFAZ Nº 09-R/2022 = 15.000.000, Download/378)`); D65 ✔ (`dados/externos/dio_teto_trechos.csv (DIO-ES, 27/09/2022, p. 18-19: Portaria SEFAZ nº 83-R)`); D65c ✔ (`analise/tabelas/03f_captacao_anual_secult.csv`)
  - ☐ **[1.1.3]** De 2023 a 2025, a captação esgotou o teto em três registros distintos: os termos de patrocínio listados pela SECULT somam exatamente o montante de cada ano, e a soma coincide com a dos termos no Portal da Transparência e com a renúncia realizada informada pela SEFAZ (em 2025, 62 projetos validados somam R\$ 24,64 milhões, e um ainda "em análise na SEFAZ" no anexo, cujos termos estão no Portal e tiveram depósito publicado no Diário Oficial, completa os R\$ 25 milhões; os números de 2025 contam os 63).
    - checagem de dados: D07 ✔ (`artigo/auditoria/auditoria_captacao_anual.csv (auditar_captacao.py, sobre o anexo oficial de 2025)`); N45 ✔ (`artigo/auditoria/auditoria_captacao_anual.csv (2023-2025)`); N87 ✔ (`analise/tabelas/21_etapas_captacao.csv (anexo = Portal = renúncia realizada, 2023-2025)`)
    - ⚠ números sem checagem automática (conferir na fonte citada): 25, 63
  - ☐ **[1.1.4]** A demanda supera o teto: nos cinco ciclos de habilitação (2022-2026), 463 projetos foram autorizados a captar, somados, R\$ 184 milhões (459 com valor válido), acima da soma dos tetos do período, de R\$ 111 milhões. [nota de rodapé: repo]
    - checagem de dados: D06 ✔ (`analise/tabelas/03_anual.csv (valor autorizado`); D06b ✔ (`artigo/auditoria/auditoria_captacao_anual.csv (maior entre portaria e montante impresso, 2022-2026) < 03_anual.csv`)
    - ☐ *Nota de rodapé (repo):* Todos os números deste artigo vêm dos anexos oficiais da SECULT ("Lista de projetos habilitados" e "Recurso financeiro captado", de 2022 a 2026), de bases públicas do IBGE, do Tesouro Nacional (SICONFI) e do Portal da Transparência do ES. A lista de habilitados foi transcrita na versão disponível em 3 set. 2026 (repositório licc.gov); a SECULT atualizou o arquivo em 10 set. 2026, e os status publicados podem ter mudado desde então. Dados, scripts e tabelas: <https://github.com/fcarva/aval-pol>.
      - ⚠ números sem checagem automática (conferir na fonte citada): 3, 10

- **1.2** — *Passo:* Reconstrói o problema que a lei não declara e o enuncia
  - ☐ **[1.2.1]** O setor cultural capixaba é pequeno para o tamanho da economia do estado: em 2024, ocupava 4,2% dos trabalhadores do ES, contra 5,8% no país, a 18ª participação entre as 27 unidades da federação (IBGE, 2025).
    - citações: IBGE, 2025
    - checagem de dados: D08 ✔ (`dados/externos/siic_uf.csv`)
    - ⚠ números sem checagem automática (conferir na fonte citada): 27
  - ☐ **[1.2.2]** Na economia criativa, que soma às artes atividades de mercado como design e publicidade, o estado ficava perto da média: 8,2% dos ocupados no 2º trimestre de 2020, contra 8,5% no país, a 8ª posição (SECULT, 2020).
    - citações: SECULT, 2020
    - checagem de dados: N64 ✔ (`dados/fontes_web/paginas/boletim_ec_boletim_economia_criativa_02t_2020.txt (SECULT, Boletim 2T2020)`)
  - ☐ **[1.2.3]** O contraste sugere a falta de coordenação entre tomadores de decisão e proponentes dos bens públicos culturais, que a LICC financia, e não um atraso da atividade criativa em execução.
  - ☐ **[1.2.4]** A desigualdade de infraestrutura também é interna: em 2021, 95% da população da Região Metropolitana da Grande Vitória (RMGV) vivia em município com cinema, contra 34% da do interior, e metade dos municípios do interior não tinha fundo municipal de cultura (IBGE, 2022).
    - citações: IBGE, 2022
    - checagem de dados: D09 ✔ (`dados/externos/munic2021_cultura_es_resumo.csv`); D10 ✔ (`dados/externos/munic2021_cultura_es_resumo.csv`)
  - ☐ **[1.2.5]** O problema é, assim, a baixa e desigual capacidade de financiar a produção e a oferta cultural fora do circuito já consolidado, com causas na restrição de financiamento de pequenos produtores, na concentração de equipamentos e na dependência de poucos financiadores.

- **1.3** — *Passo:* Justifica a avaliação: gasto fora do orçamento e decisão privada
  - ☐ **[1.3.1]** A avaliação da LICC se justifica por duas razões.
  - ☐ **[1.3.2]** Primeiro, trata-se de gasto público que não passa pelo lado da despesa do orçamento: a renúncia efetiva equivale a 14% a 21% do gasto estadual direto na função cultura em 2022-2025 (SECULT, 2026c; BRASIL, 2026).
    - citações: SECULT, 2026c; BRASIL, 2026
    - checagem de dados: D11 ✔ (`analise/tabelas/03f_captacao_anual_secult.csv (validado_sobre_f13_estado, 2022-2025)`)
  - ☐ **[1.3.3]** Segundo, quem decide o destino do recurso é a empresa patrocinadora, e não o Estado, o que expõe a política às críticas de concentração e de lógica de marketing feitas à Lei Rouanet (SILVA, 2017; DEKKER; RODRIGUES, 2019).
    - citações: SILVA, 2017; DEKKER; RODRIGUES, 2019

- **1.4** — *Passo:* Declara os objetivos e o roteiro do artigo
  - ☐ **[1.4.1]** O artigo tem dois objetivos: avaliar o desenho da LICC, sem propor redesenho do mecanismo, e estruturar uma avaliação de impacto, com desenho amostral, fontes de dados e cálculo de poder.
  - ☐ **[1.4.2]** A seção 2 caracteriza a política, a 3 revisa a literatura, a 4 reconstrói e audita a teoria da mudança, a 5 propõe a avaliação de impacto e a 6 conclui.


## 2 Caracterização da política

- **2.1** — *Passo:* Descreve o fluxo do mecanismo: inscrição, habilitação, patrocínio e crédito
  - ☐ **[2.1.1]** A LICC é um **gasto tributário alocado por empresas**.
  - ☐ **[2.1.2]** O proponente inscreve o projeto na SECULT.
  - ☐ **[2.1.3]** Se o projeto for habilitado, o proponente procura uma empresa contribuinte do ICMS que aceite patrocinar.
  - ☐ **[2.1.4]** A empresa deposita o valor numa conta do projeto e compensa até 100% dele com o ICMS devido, sem contrapartida financeira (ESPÍRITO SANTO, 2021b, art. 10).
    - citações: ESPÍRITO SANTO, 2021b, art. 10
    - ⚠ números sem checagem automática (conferir na fonte citada): 100%
  - ☐ **[2.1.5]** O Quadro 1 resume as regras.

### Quadro 1 – Elementos do desenho da LICC

- **Colunas:** Elemento · Regra vigente · Norma
  - ☐ **Benefício ao patrocinador** — Crédito presumido de até 100% do patrocínio, compensado com o ICMS a recolher — Lei 7.000/2001, art. 5º-B, IX; Dec. 5.035-R/2021, art. 10
    - ⚠ números sem checagem automática (conferir na fonte citada): 100%
  - ☐ **Teto anual** — Fixado pela SEFAZ até 31/01, ampliável no exercício, limitado a 2% do ICMS estadual do ano anterior: R\$ 15 mi em 2022 (10 mi ampliados em setembro) e 2023, 25 mi em 2024 e 2025, 31 mi em 2026 — Dec. 5.035-R/2021, art. 4º; Dec. 5.210-R/2022; portarias SEFAZ
    - ⚠ números sem checagem automática (conferir na fonte citada): 31, 01, 2%, 15, 10, 25
  - ☐ **Patrocinador** — Pessoa jurídica contribuinte do ICMS fora do Simples Nacional, até 20%, 15%, 10% ou 5% do ICMS recolhido no ano anterior, conforme a faixa de imposto — Dec. 5.035-R/2021, arts. 2º e 10, § 1º; LC 123/2006, art. 24; IN 001/2026, art. 40
    - ⚠ números sem checagem automática (conferir na fonte citada): 20%, 15%, 10%, 5%
  - ☐ **Proponentes** — Pessoa jurídica com finalidade cultural e sede no ES há 2 anos; até 3 inscrições por ano — Dec. 5.035-R/2021, art. 5º; IN 001/2025, art. 13
    - ⚠ números sem checagem automática (conferir na fonte citada): 2, 3
  - ☐ **Linhas e limite por projeto** — Seis linhas, das linguagens artísticas ao audiovisual, sem reserva do teto por linha; até 2023, 5% do montante anual; desde 2024, R\$ 500 mil (R\$ 1 milhão para obra em patrimônio e longa-metragem; R\$ 300 mil em primeira edição, desde 2025) — IN 002/2022 e 001/2023, art. 8º; IN 001/2025, arts. 9º e 14-16
    - checagem de dados: N59 ✔ (`analise/tabelas/11_teto_projeto_por_ano.csv (trechos das INs 2023 e 2024 conferidos)`)
    - ⚠ números sem checagem automática (conferir na fonte citada): 1, 300, 001
  - ☐ **Seleção** — Parecer técnico sobre nove critérios qualitativos ("atende ou não"), sem nota; o parecer favorável emite o certificado, e a comissão paritária (CAP) habilita ou não, podendo exigir ajustes — Dec. 5.035-R/2021, art. 14; IN 001/2025, arts. 37-45
  - ☐ **Alocação entre habilitados** — Pela empresa patrocinadora; reservas do teto: 30% para eventos com mais de 10 anos, 10% para planos plurianuais, 10% para projetos fora da RMGV, 50% para os demais — IN 001/2025, art. 18
    - ⚠ números sem checagem automática (conferir na fonte citada): 30%, 10, 10%, 50%
  - ☐ **Custos com o recurso incentivado** — Captação até 10% (R\$ 50 mil) e elaboração até 5% (R\$ 15 mil); em 2026, despesa única de até 10%, paga até ao proponente; divulgação até 25%; marca do patrocinador em proporção com a do Governo — IN 001/2025, arts. 23, 27-28, 55 e 64; IN 001/2026, art. 28
    - ⚠ números sem checagem automática (conferir na fonte citada): 10%, 15, 25%
  - ☐ **Contrapartidas** — Ao menos cinco, de um cardápio de acesso, gratuidade, descentralização, ações afirmativas e acessibilidade — IN 001/2025, arts. 35-36
  - ☐ **Controle** — Extrato no Diário Oficial a cada repasse; prestação de contas do objeto; fiscalização por amostragem — Dec. 5.035-R/2021, arts. 17-19

- **2.2** (fonte do quadro, tabela ou figura)
  - ☐ **[2.2.1]** Fonte: elaboração própria a partir das normas citadas (ESPÍRITO SANTO, 2021a; 2021b; SECULT, 2022; 2023a; 2025a; 2026a).
    - citações: ESPÍRITO SANTO, 2021a; 2021b; SECULT, 2022; 2023a; 2025a; 2026a

- **2.3** — *Passo:* Destaca os três traços do arranjo que guiam a avaliação
  - ☐ **[2.3.1]** Três características do arranjo pesam na avaliação.
  - ☐ **[2.3.2]** A primeira é a delegação da escolha: o Estado define quem pode receber; a empresa define quem recebe.
  - ☐ **[2.3.3]** A segunda é a instabilidade: a SECULT edita uma instrução normativa por ano, fechou as inscrições em meados de 2024 e alterou o fluxo em meados de 2025 (SECULT, 2024b; 2025b); até 2024 a comissão habilitava antes da captação, e desde 2025 o projeto só vai à comissão com patrocinador (SECULT, 2025a, arts. 41-45).
    - citações: SECULT, 2024b; 2025b; SECULT, 2025a, arts. 41-45
  - ☐ **[2.3.4]** A terceira é a pouca informação publicada: os anexos não trazem dados dos projetos do proponente, o local de atuação nem indicadores de resultado, e os inabilitados só aparecem nos extratos das atas da comissão (SECULT, 2026f).
    - citações: SECULT, 2026f


## 3 Breve revisão da literatura

- **3.1** — *Passo:* Situa a LICC na literatura: incentivo fiscal com decisão privada e a cultura como bem público
  - ☐ **[3.1.1]** **Despesa tributária com decisão privada.** A literatura de economia da cultura trata o incentivo fiscal como um subsídio em que o doador decide a alocação e o Tesouro paga a conta: para Feld, O'Hare e Schuster (1983), os contribuintes se tornaram "mecenas apesar de si mesmos", porque financiam pela renúncia as escolhas que não fazem.
    - citações: O'Hare e Schuster (1983)
  - ☐ **[3.1.2]** A dificuldade de financiamento de bens públicos e a falta de coordenação entre conselhos de pareceristas e as preferências do público justificam a investigação econômica e o papel do bem público para a cultura: bens públicos são consumidos em grupo, e não por indivíduos, e por isso são "o tecido que conecta as pessoas" (HITZIG, 2021, tradução nossa); Buterin, Hitzig e Weyl (2019) tratam seu financiamento como formação de comunidades e mostram que, se o valor recebido cresce com o número de contribuintes, e não só com o total aportado, a provisão é ótima no modelo de fundo de contrapartida e contribuição por parte do público.
    - citações: HITZIG, 2021, tradução nossa; Hitzig e Weyl (2019)

- **3.2** — *Passo:* Traz a experiência da Lei Rouanet: concentração, mercado de patrocínios e adicionalidade
  - ☐ **[3.2.1]** **A experiência brasileira com a Lei Rouanet.** A LICC reproduz o núcleo do mecenato federal, que acumula três décadas de debate: concentração regional no Sudeste (SILVA, 2017), concentração persistente de patrocinadores e proponentes (COSTA; MEDEIROS; BUCCO, 2017) e um "mercado de patrocínios" com intermediários e departamentos de marketing (BELEM; DONADONE, 2013).
    - citações: SILVA, 2017; COSTA; MEDEIROS; BUCCO, 2017; BELEM; DONADONE, 2013
  - ☐ **[3.2.2]** Dekker e Rodrigues (2019) concluem que a lei beneficiou sobretudo projetos já bem-sucedidos e que não está claro qual falha de mercado ela corrige, dúvida que vale para a LICC (seção 4.2).
    - citações: Dekker e Rodrigues (2019)
  - ☐ **[3.2.3]** Em 2010-2019, o maior doador destinou 853 vezes o valor do doador médio, e o número de doadores de um projeto não se relaciona com a parcela do aprovado que ele capta (OGAVA; GALVÃO; ADAMCZYK, 2022).
    - citações: OGAVA; GALVÃO; ADAMCZYK, 2022
    - ⚠ números sem checagem automática (conferir na fonte citada): 853

- **3.3** — *Passo:* Mostra que a evidência sobre incentivos estaduais no Brasil é descritiva
  - ☐ **[3.3.1]** **Evidência causal.** Existem poucos trabalhos de avaliação do incentivo cultural no Brasil; as avaliações encontradas de leis estaduais via ICMS são correlacionais: em Minas Gerais, a captação pela lei estadual concentrou-se na região metropolitana de Belo Horizonte, e municípios com museu, teatro ou cinema tinham mais chance de captar (TEIXEIRA *et al.*, 2021).
    - citações: TEIXEIRA *et al.*, 2021
  - ☐ **[3.3.2]** A única avaliação da LICC, contratada pela SECULT ao IJSN com a FAPES em 2025, divulgou resultados preliminares com um "efeito multiplicador de 1,74" por real investido (IJSN, 2026; DIO-ES, 2026): a medida registra a atividade gerada pelo gasto, e não o que ocorreria sem o incentivo.
    - citações: IJSN, 2026; DIO-ES, 2026
    - checagem de dados: N102 ✔ (`dados/fontes_web/firecrawl/ijsn_cultura_em_dados_2026.md (IJSN, notícia de 01/07/2026)`)


## 4 Desenho da política e sua avaliação


### 4.1 Teoria da mudança

- **4.1.1** — *Passo:* Explica como a teoria da mudança é reconstruída e por que tem três cadeias
  - ☐ **[4.1.1.1]** A teoria da mudança da LICC (Figura 1) segue cinco passos: propósito, cadeia causal, premissas e riscos, hipótese causal e indicadores.
  - ☐ **[4.1.1.2]** Na cadeia de resultados de Gertler *et al.* (2018), os produtos estão sob controle do órgão executor; na LICC, o produto "projeto patrocinado" depende de um terceiro, a empresa.
    - citações: Gertler *et al.* (2018)
  - ☐ **[4.1.1.3]** Por isso a Figura 1 separa três cadeias: a entrada, o financiamento e a entrega, e indica quem decide em cada elo.

- **4.1.2** — *Passo:* Enuncia a hipótese causal no formato do J-PAL
  - ☐ **[4.1.2.1]** A hipótese causal é: *se* a SECULT abre a inscrição e habilita projetos culturais, e empresas contribuintes patrocinam parte deles com o ICMS que pagariam, *então* se forma um cardápio de projetos habilitados e um conjunto de projetos patrocinados e executados, *o que deveria levar* a mais bens culturais de acesso público, executados por proponentes mais diversos e mais capazes, *que ao final melhorarão* o acesso da população à cultura e reduzirão sua desigualdade territorial, *contribuindo para* ampliar e desconcentrar a capacidade de financiar a cultura no estado.

- **4.1.3** — *Passo:* Define as cinco premissas testadas (H1 a H5) e os riscos
  - ☐ **[4.1.3.1]** Cada seta da cadeia carrega uma premissa, uma condição que precisa valer para que um passo leve ao seguinte (MAYNE, 2015).
    - citações: MAYNE, 2015
  - ☐ **[4.1.3.2]** Cinco delas são tratadas como hipóteses a testar, marcadas nos elos da Figura 1 e auditadas no Quadro 2.
  - ☐ **[4.1.3.3]** H1 (marketing): a empresa escolhe pela marca, único retorno privado do crédito integral, sem deixar de fora bem público que a população valorizaria.
  - ☐ **[4.1.3.4]** H2 (decisão concentrada): a decisão sobre recurso público segue critério público e não fica com poucos decisores.
  - ☐ **[4.1.3.5]** H3 (taxa de serviço): o recurso chega ao bem cultural, e não à intermediação.
  - ☐ **[4.1.3.6]** H4 (exclusão): quem não tem acesso a grandes contribuintes consegue entrar.
  - ☐ **[4.1.3.7]** H5 (entrega): o bem financiado não existiria sem a LICC.
  - ☐ **[4.1.3.8]** H1 a H4 perguntam quem decide e a que custo; H5, se o que se financia é adicional.
  - ☐ **[4.1.3.9]** Há dois riscos (efeitos não esperados): o teto fixo desloca outros projetos, e o crédito integral pode substituir o patrocínio próprio da empresa.

### Figura 1 – Teoria da mudança da LICC

- **Figura 1 (textos da imagem, `analise/08_figura_teoria_da_mudanca.py`):**
  - ☐ Baixa e desigual capacidade de financiar a produção e a oferta cultural fora do circuito já consolidado
  - ☐ Teto anual de renúncia de ICMS (imposto que a população deixa de arrecadar) · SECULT, pareceristas, CAP e SEFAZ · Mapa Cultural
  - ☐ A1 · Inscrição no edital: on-line, com CNPJ e documentos (quem decide: agente cultural)
  - ☐ A2 · Parecer e CAP: parecer sem nota; a CAP habilita ou não (quem decide: SECULT e CAP)
  - ☐ P1 · Cardápio de projetos habilitados: autorização para captar por um ano
  - ☐ A3 · Escolha e termo: a empresa escolhe e compromete o ICMS (quem decide: empresa)
  - ☐ A4 · Validação no teto: termos validados até esgotar a cota (quem decide: SEFAZ)
  - ☐ P2 · Projetos patrocinados: captação por projeto e empresa
  - ☐ P3 · Projetos executados: com contrapartidas de acesso (quem decide: proponente)
  - ☐ RI1 · Bens culturais de acesso público: gratuidade, acessibilidade, interior
  - ☐ RI2 · Quem executa se diversifica: novos proponentes, interior, emprego
  - ☐ Acesso maior e menos desigual da população à cultura, e um setor cultural mais capaz de se financiar
  - ☐ H4 · Exclusão na entrada: Quem não chega a grandes contribuintes (projeto pequeno, interior, estreante) consegue entrar e captar?
  - ☐ H2 · Decisão concentrada: O parecer só qualifica; entre os habilitados, decidem a empresa e a fila dos termos. O público não escolhe.
  - ☐ H1 · Marketing: A escolha pela marca, retorno privado da empresa, deixa de fora bem público que a população valorizaria?
  - ☐ H3 · Taxa de serviço: Quanto do recurso fica com captação, elaboração e divulgação (até 10%, 5% e 25%)?
  - ☐ H5 · Entrega verificável: O bem cultural aconteceria sem a LICC? Chega ao público, e o declarado é entregue?

- **4.1.4** (fonte do quadro, tabela ou figura)
  - ☐ **[4.1.4.1]** Fonte: elaboração própria, no formato do J-PAL (GERTLER *et al.*, 2018), com base nas normas do Quadro 1.
    - citações: GERTLER *et al.*, 2018
  - ☐ **[4.1.4.2]** Setas tracejadas: elos sem dado público.


### 4.2 Avaliação do desenho

- **4.2.1** — *Passo:* Declara as perguntas de avaliação de desenho e a classificação das premissas
  - ☐ **[4.2.1.1]** Aplicam-se as perguntas usuais de avaliação de desenho: o problema está formulado?
  - ☐ **[4.2.1.2]** Os objetivos são mensuráveis?
  - ☐ **[4.2.1.3]** Cada elo tem premissa crível e indicador?
  - ☐ **[4.2.1.4]** Quanto se perde ao longo da cadeia?
  - ☐ **[4.2.1.5]** Pelo mecanismo de mapeamento de Williams (2020), a premissa de cada elo é confrontada com o contexto real e classificada como sustentada, não assegurada pelo desenho, não sustentada (evidência mista) ou indeterminada (Quadro 2).
    - citações: Williams (2020)

- **4.2.2** — *Passo:* Avalia problema e objetivos: sem objetivo mensurável, meta ou indicador
  - ☐ **[4.2.2.1]** **Problema e objetivos.** A lei não tem artigo de objetivos, e o decreto declara na ementa um objetivo de produto, "estimular a realização de projetos culturais"; suas onze finalidades de "interesse público", das quais o projeto atende **uma ou mais**, definem quem é elegível, não o que a política pretende alcançar (ESPÍRITO SANTO, 2021b, art. 3º).
    - citações: ESPÍRITO SANTO, 2021b, art. 3º
  - ☐ **[4.2.2.2]** Não há meta, magnitude esperada nem indicador: no relatório de avaliação do PPA, a LICC aparece só no relato de uma ação de despesa, sem produto nem meta física próprios (ESPÍRITO SANTO, 2026b).
    - citações: ESPÍRITO SANTO, 2026b
  - ☐ **[4.2.2.3]** A LICC não atende ao critério de que um programa declare resultados e magnitude esperados (BARROS; LIMA, 2017).
    - citações: BARROS; LIMA, 2017

- **4.2.3** — *Passo:* Avalia o funil de atrito e os indicadores da cadeia
  - ☐ **[4.2.3.1]** **Funil de atrito e indicadores.** O funil mede, elo a elo, quantos beneficiários potenciais chegam ao fim da cadeia (WHITE; RAITZER, 2017); suas etapas são os indicadores da cadeia, e os de resultado são os *Y* do Quadro 3.
    - citações: WHITE; RAITZER, 2017
  - ☐ **[4.2.3.2]** A Tabela 1 mostra que ele se estreita onde não há dado: entre os 25.441 agentes cadastrados no Mapa Cultural e os 53 a 95 proponentes habilitados por ciclo, não se sabe quantos se inscreveram.
    - checagem de dados: N02 ✔ (`analise/tabelas/07_mapa_cultural_universo.csv`); N44 ✔ (`analise/tabelas/07_composicao_por_ciclo.csv (2022-2026)`)
  - ☐ **[4.2.3.3]** Nas etapas observadas, a maioria passa: 68% dos habilitados de 2022-2024 com situação resolvida captaram.
    - checagem de dados: N04 ✔ (`analise/tabelas/07_funil_por_ciclo.csv`)

### Quadro 2 – Premissas da teoria da mudança

- **Colunas:** Elo · Premissa · Contexto real · Situação
  - ☐ **Escolha (H1)** — A escolha pela marca, único retorno privado da empresa, não deixa de fora bem público que a população valorizaria — Duas empresas somam metade da renúncia de 2025; energia e gás, 52%. As peças de divulgação (até 25%) trazem a marca. Recorrentes captam mais (71% contra 57%); 48 pares patrocinador–proponente se repetem (44% do valor) — Indeterminada: marca e valor público não se separam no dado público
    - checagem de dados: N12 ✔ (`analise/tabelas/03_patrocinadores_concentracao.csv`); N14 ✔ (`analise/tabelas/03_status_conversao_recorrencia_2023_2024.csv`); N61 ✔ (`analise/tabelas/16_pares_recorrentes.csv`)
    - ⚠ números sem checagem automática (conferir na fonte citada): 25%
  - ☐ **Habilitação e validação (H2)** — A decisão sobre recurso público segue critério público — Parecer sem nota nem ordem. Termos com patrocinador de 28% e 35% do montante recusados em 2023 e 2024; em 2025, a cota de 50% se completou com termos recebidos até 28/01. O público não escolhe — Não assegurada pelo desenho
    - checagem de dados: N15 ✔ (`analise/tabelas/03f_captacao_anual_secult.csv`); N34 ✔ (`analise/tabelas/09_cotas_2025_2026.csv`)
  - ☐ **Custos (H3)** — O recurso incentivado chega ao bem cultural, e não à intermediação — Captação e elaboração poderiam levar até 13% do valor captado em 2025; em 2026, a taxa pode ir ao proponente. Não há planilha de custos publicada — Indeterminada: sem planilhas
    - checagem de dados: N52 ✔ (`analise/tabelas/10_taxa_servico_permitida_2025.csv`)
  - ☐ **Entrada (H4)** — Quem não chega a grandes contribuintes consegue se inscrever e captar — A inscrição exige CNPJ com finalidade cultural, sede e certidão; só pessoa jurídica contribuinte patrocina. 14 municípios do interior nunca tiveram projeto habilitado; pedidos até R\$ 400 mil captaram 79% em 2022 e 27% em 2024; 44 de 107 proponentes voltaram a captar (68% do valor) — Não sustentada: evidência mista
    - checagem de dados: N10 ✔ (`analise/tabelas/03_coortes_primeira_presenca_canonico.csv`); N62 ✔ (`analise/tabelas/16_concentracao_proponentes.csv`); N74 ✔ (`analise/tabelas/03_status_conversao_por_faixa_valor_e_ciclo.csv`)
  - ☐ **Entrega (H5)** — O projeto financiado não aconteceria sem a LICC e chega ao público — A maior reserva do teto (30%) vai a eventos com mais de dez anos; o público alcançado não é publicado — Indeterminada: sem dado
    - ⚠ números sem checagem automática (conferir na fonte citada): 30%

- **4.2.4** (fonte do quadro, tabela ou figura)
  - ☐ **[4.2.4.1]** Fonte: elaboração própria, no formato do mecanismo de mapeamento de Williams (2020), com base nas normas do Quadro 1, em SECULT (2026b; 2026c; 2026d), no Portal da Transparência (ESPÍRITO SANTO, 2026a) e nas tabelas `03_*.csv`, `07_*.csv`, `09_*.csv`, `10_*.csv`, `14_*.csv` e `16_*.csv` de `analise/tabelas/`.
    - citações: ESPÍRITO SANTO, 2026a; Williams (2020)
    - ⚠ números sem checagem automática (conferir na fonte citada): 2026

### Tabela 1 – Funil de atrito da LICC

- **Colunas:** Etapa · Valor · Período
  - ☐ **Agentes culturais cadastrados no Mapa Cultural (coletivos)** — 25.441 (2.592) — set. 2026
    - checagem de dados: N03 ✔ (`analise/tabelas/07_mapa_cultural_universo.csv`)
  - ☐ **Projetos inscritos** — não publicado — —
  - ☐ **Projetos habilitados; proponentes por ciclo** — 305; 53, 92 e 95 — ciclos 2022-2024
    - checagem de dados: N05 ✔ (`analise/tabelas/07_funil_por_ciclo.csv`)
  - ☐ **Habilitados com situação resolvida; captaram** — 293; 198 — ciclos 2022-2024
    - checagem de dados: N06 ✔ (`analise/tabelas/07_funil_por_ciclo.csv`)
  - ☐ **Valor com patrocinador que coube no teto** — 78%; 74% — captação 2023; 2024
    - checagem de dados: N08 ✔ (`analise/tabelas/07_funil_captacao_anual.csv`)
  - ☐ **Público alcançado e gratuidade** — não publicado — —

- **4.2.5** (fonte do quadro, tabela ou figura)
  - ☐ **[4.2.5.1]** Fonte: elaboração própria com base em SECULT (2026b; 2026c) e na API pública do Mapa Cultural do Espírito Santo (SECULT, 2026d).
    - citações: SECULT, 2026d
    - ⚠ números sem checagem automática (conferir na fonte citada): 2026
  - ☐ **[4.2.5.2]** Tabelas de origem: `analise/tabelas/07_funil_por_ciclo.csv`, `07_funil_captacao_anual.csv` e `07_mapa_cultural_universo.csv`.

- **4.2.6** — *Passo:* Audita H4: barreiras de entrada, difusão territorial, projetos pequenos, acúmulo no teto
  - ☐ **[4.2.6.1]** **Exclusão na entrada (H4).** Pessoa física não se inscreve, e o microempreendedor individual tem limite de valor (SECULT, 2025a, arts. 17 e 19).
    - citações: SECULT, 2025a, arts. 17 e 19
  - ☐ **[4.2.6.2]** Do lado de quem financia, só pessoa jurídica contribuinte do ICMS patrocina (ESPÍRITO SANTO, 2021b, art. 2º), e as optantes do Simples Nacional, que não podem destinar valor a título de incentivo fiscal (BRASIL, 2006, art. 24), tampouco emitem a carta de intenção (SECULT, 2026a, art. 40): o público financia, pelo imposto que deixa de ser arrecadado, mas nem ele nem a pequena empresa local escolhem o que financiar.
    - citações: ESPÍRITO SANTO, 2021b, art. 2º; BRASIL, 2006, art. 24; SECULT, 2026a, art. 40
  - ☐ **[4.2.6.3]** A difusão territorial desacelerou: 39 municípios tiveram o primeiro projeto habilitado em 2022, 16 em 2023 e 3 por ciclo desde então, e restam 14 municípios do interior sem projeto.
    - checagem de dados: N16 ✔ (`analise/tabelas/03_coortes_primeira_presenca_canonico.csv`); N36 ✔ (`analise/tabelas/03_coortes_primeira_presenca_canonico.csv`)
  - ☐ **[4.2.6.4]** Entre os que pediram até R\$ 400 mil, a captação caiu de 79% no ciclo 2022 para 27% em 2024, enquanto no teto ficou entre 78% e 89%.
    - checagem de dados: N46 ✔ (`analise/tabelas/03_status_conversao_por_faixa_valor_e_ciclo.csv (taxa_execucao)`)
    - ⚠ números sem checagem automática (conferir na fonte citada): 400
  - ☐ **[4.2.6.5]** Os pedidos se acumulam no teto por projeto: 36% dos habilitados do ciclo 2025 pediram exatamente R\$ 500 mil, o que também ocorre se quem já tem patrocinador pede o máximo.
    - checagem de dados: N58 ✔ (`analise/tabelas/03_bunching_teto.csv`)
  - ☐ **[4.2.6.6]** O custo de entrada é o que a literatura chama de custo administrativo (MOYNIHAN; HERD; HARVEY, 2015); ele pode excluir sem selecionar ou funcionar como triagem (FINKELSTEIN; NOTOWIDIGDO, 2019).
    - citações: MOYNIHAN; HERD; HARVEY, 2015; FINKELSTEIN; NOTOWIDIGDO, 2019

- **4.2.7** — *Passo:* Audita H2: parecer sem nota, papel da comissão, inabilitações, racionamento pela ordem
  - ☐ **[4.2.7.1]** **Decisão concentrada (H2).** O parecer "deverá indicar a habilitação ou inabilitação" (ESPÍRITO SANTO, 2021b, art. 14): para cada critério, o parecerista indica se o projeto "atende ou não" (SECULT, 2026e), e o Mapa Cultural registra só a situação da inscrição (SECULT, 2026d).
    - citações: ESPÍRITO SANTO, 2021b, art. 14; SECULT, 2026e; SECULT, 2026d
  - ☐ **[4.2.7.2]** Nenhuma das normas examinadas prevê nota, peso ou ordem de prioridade; a única pontuação é a do credenciamento dos pareceristas, que recebem os projetos por ordem de inscrição e área (SECULT, 2025c).
    - citações: SECULT, 2025c
  - ☐ **[4.2.7.3]** Desde 2025, o parecer favorável já emite o certificado, e a comissão só delibera sobre inabilitações e, com 35% de patrocínio, sobre a habilitação (SECULT, 2025a, arts. 40, 41 e 45).
    - citações: SECULT, 2025a, arts. 40, 41 e 45
    - ⚠ números sem checagem automática (conferir na fonte citada): 35%
  - ☐ **[4.2.7.4]** As atas de 158 reuniões com deliberação, de 2022 a 2026, listam 86 projetos inabilitados, 15% dos deliberados, sem motivo nem critério publicados (SECULT, 2026f).
    - citações: SECULT, 2026f
    - checagem de dados: N60 ✔ (`analise/tabelas/12_cap_deliberacoes.csv`)
  - ☐ **[4.2.7.5]** A habilitação qualifica, mas não prioriza, e o que excedeu o teto em 2023-2025 ficou de fora pela regra da ordem de chegada e validação (SECULT, 2026c), cuja aplicação só as horas de protocolo dos recusados, não publicadas, permitiriam conferir.
    - citações: SECULT, 2026c
  - ☐ **[4.2.7.6]** A ordenação seria possível: no Funcultura, a mesma SECULT atribui nota e ordena os projetos por linha e porte do município (SECULT, 2026g).
    - citações: SECULT, 2026g

- **4.2.8** — *Passo:* Audita H1: a marca como retorno privado e o peso de cada empresa pelo imposto
  - ☐ **[4.2.8.1]** **Marketing (H1).** Com crédito integral, a empresa escolhe o destino do ICMS que pagaria e fica com o retorno de marketing: as peças de comunicação, parte do objeto, trazem a marca do patrocinador em proporção à do Governo, e a divulgação pode consumir até 25% dos recursos (SECULT, 2025a, arts. 23, 55 e 64).
    - citações: SECULT, 2025a, arts. 23, 55 e 64
    - checagem de dados: N54 ✔ (`analise/tabelas/10_rubricas_teto_in.csv (2025)`)
  - ☐ **[4.2.8.2]** Como o limite por patrocinador é uma fração do ICMS recolhido, o peso de cada empresa na escolha cresce com o imposto que ela paga, e a concentração da renúncia (Quadro 2) reflete também a do próprio imposto.
  - ☐ **[4.2.8.3]** Imagem e relações de negócio estão entre os motivos do patrocínio (O'HAGAN; HARVEY, 2000), e a filantropia empresarial também serve de canal de influência política (BERTRAND *et al.*, 2020); a maior patrocinadora de 2025 é uma distribuidora de energia, serviço regulado sob concessão.
    - citações: O'HAGAN; HARVEY, 2000; BERTRAND *et al.*, 2020
  - ☐ **[4.2.8.4]** Com o dado público, marca e valor público não se separam, porque os eventos grandes e antigos são os mais visíveis e os de maior público: a premissa fica indeterminada.
  - ☐ **[4.2.8.5]** Sob crédito integral, escolher pela marca é o esperado.
  - ☐ **[4.2.8.6]** O limite está no mecanismo: cada escolha pesa pelo imposto de quem escolhe, e o número de pessoas que valorizam o bem não entra no cálculo (BUTERIN; HITZIG; WEYL, 2019); a questão é o que essa escolha deixa de fora (H4) e se o escolhido ocorreria de todo modo (H5).
    - citações: BUTERIN; HITZIG; WEYL, 2019

- **4.2.9** — *Passo:* Audita H3: quanto os tetos de custos permitem pagar à intermediação
  - ☐ **[4.2.9.1]** **Taxa de serviço (H3).** Parte do recurso incentivado pode remunerar quem intermedia.
  - ☐ **[4.2.9.2]** A captação pode custar até 10% (R\$ 50 mil) e a elaboração do projeto até 5% (R\$ 15 mil), pagas a uma empresa contratada, e o proponente pode receber até 1/3 como remuneração (SECULT, 2025a, arts. 26-28).
    - citações: SECULT, 2025a, arts. 26-28
    - checagem de dados: N53 ✔ (`analise/tabelas/10_rubricas_teto_in.csv (2025)`)
    - ⚠ números sem checagem automática (conferir na fonte citada): 1, 3
  - ☐ **[4.2.9.3]** Aplicados ao valor captado de cada projeto de 2025, os dois primeiros limites somam R\$ 3,36 milhões, 13% dos R\$ 25 milhões.
    - checagem de dados: N50 ✔ (`analise/tabelas/10_taxa_servico_permitida_2025.csv`)
  - ☐ **[4.2.9.4]** Em 2026, captação e elaboração tornaram-se uma despesa única de até 10%, que pode ser paga ao próprio proponente (SECULT, 2026a, art. 28).
    - citações: SECULT, 2026a, art. 28
    - ⚠ números sem checagem automática (conferir na fonte citada): 10%
  - ☐ **[4.2.9.5]** Os limites fixam o preço máximo do "mercado de patrocínios", mas quanto se gasta de fato é indeterminado, porque as planilhas de custos não são publicadas.

- **4.2.10** — *Passo:* Audita H5 e o território: reserva para eventos antigos, RMGV, Gini e Theil
  - ☐ **[4.2.10.1]** **Entrega e território.** A maior reserva do teto, 30%, vai a eventos com mais de dez anos, provavelmente os de maior chance de financiamento sem incentivo, em tensão com o critério do TCU (BRASIL, 2016).
    - citações: BRASIL, 2016
    - ⚠ números sem checagem automática (conferir na fonte citada): 30%
  - ☐ **[4.2.10.2]** A RMGV tem 49% da população e fica com 67% do valor atribuível a um município em 2022-2026.
    - checagem de dados: D22 ✔ (`analise/tabelas/03_territorio_rmgv_interior.csv`); N19 ✔ (`analise/tabelas/03_territorio_rmgv_interior.csv`)

- **4.2.11** — *Passo:* Sintetiza a avaliação do desenho e liga à proposta
  - ☐ **[4.2.11.1]** Em síntese, o desenho entrega a escolha a quem recolhe mais imposto e raciona pela ordem de chegada: nenhum elo agrega a preferência de quem usa o bem cultural.
  - ☐ **[4.2.11.2]** O critério público na decisão (H2) não é assegurado pelo desenho, o que não implica que as escolhas sejam ruins; a exclusão (H4) não se sustenta, com evidência mista; o marketing (H1) fica indeterminado, porque marca e valor público não se separam no dado público, e a taxa de serviço (H3) e a entrega (H5), por falta de dado.
  - ☐ **[4.2.11.3]** A seção 5 propõe uma avaliação que liga três delas: se a escolha pela marca (H1) deixa de fora quem depende do incentivo (H4) e financia o que ocorreria de todo modo (H5).


## 5 Proposta de avaliação de impacto


### 5.1 Pergunta e parâmetros

- **5.1.1** — *Passo:* (a definir)
  - ☐ **[5.1.1.1]** Todo programa com mais demanda que recurso precisa de uma regra de racionamento: ordem de chegada, características observadas pelo gestor, características que só o candidato conhece ou sorteio (GERTLER *et al.*, 2018, p. 75).
    - citações: GERTLER *et al.*, 2018, p. 75
  - ☐ **[5.1.1.2]** A LICC combina duas.
  - ☐ **[5.1.1.3]** A primeira é a preferência de quem recolhe o imposto, que o Estado não observa; a segunda é a ordem de chegada dos termos à SEFAZ.
  - ☐ **[5.1.1.4]** A CAP qualifica, mas não ordena (seção 4.2).
  - ☐ **[5.1.1.5]** Por isso a avaliação faz uma única pergunta, que reúne H1, H4 e H5: **a renúncia vai para os projetos que dependem dela?**
  - ☐ **[5.1.1.6]** Se as empresas escolhem projetos grandes e recorrentes, que aconteceriam sem o incentivo, e ficam de fora os pequenos, que só acontecem com ele, o crédito integral paga a marca do patrocinador e compra pouco bem cultural adicional.

- **5.1.2** — *Passo:* (a definir)
  - ☐ **[5.1.2.1]** Seja *i* um projeto habilitado, *T* = 1 se um patrocinador o escolheu e o termo foi validado, e *Y* = 1 se o projeto se realizou na data prevista no plano de trabalho.
    - ⚠ números sem checagem automática (conferir na fonte citada): 1
  - ☐ **[5.1.2.2]** Há quatro médias (FOGUEL, 2017, p. 49): $E_{11}$ = E[*Y*(1) | *T* = 1] e $E_{00}$ = E[*Y*(0) | *T* = 0] se observam; $E_{10}$ = E[*Y*(0) | *T* = 1], o que os escolhidos fariam sem a LICC, e $E_{01}$ = E[*Y*(1) | *T* = 0], o que os preteridos fariam com ela, são contrafactuais.
    - citações: FOGUEL, 2017, p. 49
    - ⚠ números sem checagem automática (conferir na fonte citada): 1, 0
  - ☐ **[5.1.2.3]** A diferença simples entre quem captou e quem não captou é R = $E_{11}$ − $E_{00}$ = EMPT + *V*, em que *V* = $E_{10}$ − $E_{00}$ é o viés de seleção (FOGUEL, 2017, p. 50).
    - citações: FOGUEL, 2017, p. 50
  - ☐ **[5.1.2.4]** Numa avaliação de programa, *V* é o erro a eliminar.
  - ☐ **[5.1.2.5]** Aqui ele é o objeto: mede o quanto o mecanismo prefere projetos que aconteceriam de todo modo.

- **5.1.3** — *Passo:* (a definir)
  - ☐ **[5.1.3.1]** A hipótese do artigo é *V* > 0, concentrado nos projetos grandes e recorrentes.
    - ⚠ números sem checagem automática (conferir na fonte citada): 0
  - ☐ **[5.1.3.2]** Se o recurso realiza os preteridos tanto quanto os escolhidos, um *V* positivo significa que a LICC financia onde o efeito é menor, e o efeito sobre os não tratados, parâmetro de quem decide expandir um programa (FOGUEL, 2017, p. 47), é o que importa para um teto que mais que dobrou de 2023 a 2026.
    - citações: FOGUEL, 2017, p. 47
  - ☐ **[5.1.3.3]** O mecanismo tampouco registra quantos valorizam um projeto: 152 dos 213 projetos com termo em 2022-2025 (71%), com 68% do valor, têm um só patrocinador (BUTERIN; HITZIG; WEYL, 2019).
    - citações: BUTERIN; HITZIG; WEYL, 2019
    - checagem de dados: N84 ✔ (`analise/tabelas/20_patrocinadores_por_projeto.csv`)
  - ☐ **[5.1.3.4]** Duas premissas ficam fora do contrafactual: a regra da CAP (H2) entra pelo filtro que ela aplica, com os inabilitados, e a taxa de serviço (H3) é pergunta normativa (GERTLER *et al.*, 2018), respondida pela auditoria das despesas executadas, pedidas por LAI.
    - citações: GERTLER *et al.*, 2018
  - ☐ **[5.1.3.5]** O Quadro 3 resume os parâmetros.

### Quadro 3 – Parâmetros, grupos de comparação e regras de decisão

- **Colunas:** Parâmetro · Grupo que o mede · Suposição · Conclusão se
  - ☐ **$\theta_1$ ≈ $E_{10}$: o que os escolhidos fariam sem a LICC** — Termos recusados por esgotamento da cota, que tinham patrocinador — A recusa depende só da hora do protocolo — —
  - ☐ **$\theta_0$ = $E_{00}$: o que os preteridos fazem sem a LICC** — Habilitados cuja captação expirou — Nenhuma: observável — —
  - ☐ ***V* = $\theta_1$ − $\theta_0$ (H1, H4)** — Recusados × expirados, por faixa de valor — As duas acima — *V* > 0, maior nos pedidos grandes: a renúncia vai a quem menos depende dela
    - ⚠ números sem checagem automática (conferir na fonte citada): 0
  - ☐ **EMPT na margem = $E_{11}$ − $\theta_1$ (H5)** — Últimos validados de cada cota × recusados — Idem — EMPT próximo de zero: ampliar o teto financia o que ocorreria de todo modo
  - ☐ **Filtro da CAP (H2)** — Expirados × inabilitados — Inabilitados sem patrocínio pela LICC — Mesma realização: o filtro não separa necessidade de financiamento
  - ☐ **Substituição (lado da empresa)** — Recusados pagos pelo mesmo patrocinador fora da LICC — Resposta do patrocinador — Fração alta: o crédito paga patrocínio que ocorreria sem ele

- **5.1.4** (fonte do quadro, tabela ou figura)
  - ☐ **[5.1.4.1]** Fonte: elaboração própria, com base em Foguel (2017) e Gertler *et al.* (2018).
    - citações: Foguel (2017); Gertler *et al.* (2018)


### 5.2 Estratégia de identificação

- **5.2.1** — *Passo:* (a definir)
  - ☐ **[5.2.1.1]** Nenhum grupo precisa ser criado: a regra atual já os produz, e falta acompanhá-los.
  - ☐ **[5.2.1.2]** O contraste central é *V* = $\theta_1$ − $\theta_0$.
  - ☐ **[5.2.1.3]** Os termos recusados por esgotamento da cota tinham patrocinador, ou seja, foram escolhidos, e ficaram de fora pela hora em que chegaram: sua realização estima $E_{10}$ para os escolhidos na margem da fila.
  - ☐ **[5.2.1.4]** Os expirados, que nenhuma empresa escolheu, dão $E_{00}$.
  - ☐ **[5.2.1.5]** A comparação vale se, entre os escolhidos, a posição na fila não depende do que determina a realização, o que as horas de protocolo e validação (LAI) permitem testar, comparando recusados e últimos validados em valor, antiguidade do evento e recorrência.
  - ☐ **[5.2.1.6]** Entre os ciclos 2022 e 2024, a captação dos pedidos até R\$ 400 mil caiu de 79% para 27%, e a dos maiores, de 90% para 73%: a seleção cresceu entre os pequenos, o que pede estimar *V* por faixa de valor.
    - checagem de dados: N89 ✔ (`analise/tabelas/23_captacao_por_faixa.csv`)
  - ☐ **[5.2.1.7]** O estimador é a diferença de proporções num modelo de probabilidade linear com efeitos fixos de ciclo e faixa de valor e erro-padrão robusto.

- **5.2.2** — *Passo:* (a definir)
  - ☐ **[5.2.2.1]** O efeito na margem compara os últimos validados de cada cota com os recusados.
  - ☐ **[5.2.2.2]** É o efeito de receber agora, que já inclui o financiamento que o recusado obtém depois, sem precisar de instrumento, e vale para a margem da fila, não para a média dos escolhidos.
  - ☐ **[5.2.2.3]** Em 2024, das 47 recusas registradas nas versões sucessivas do anexo, 27 viraram validação quando o teto passou de R\$ 15 para R\$ 25 milhões; a comparação com as 20 que não viraram dá uma segunda margem, sob a condição, a conferir com as datas, de que a conversão tenha seguido a ordem da fila.
    - checagem de dados: N82 ✔ (`analise/tabelas/13_versoes_captados_fila.csv (2024)`); N90 ✔ (`analise/tabelas/13_versoes_captados_fila.csv (2024)`)
    - ⚠ números sem checagem automática (conferir na fonte citada): 25
  - ☐ **[5.2.2.4]** O filtro da CAP compara os expirados com os 86 inabilitados das atas.
    - ⚠ números sem checagem automática (conferir na fonte citada): 86
  - ☐ **[5.2.2.5]** Do lado da empresa, a fração dos recusados que o mesmo patrocinador pagou fora da LICC mede o quanto o crédito substitui patrocínio próprio, o segundo risco da teoria da mudança.


### 5.3 Desenho da amostra e fontes de dados

- **5.3.1** — *Passo:* (a definir)
  - ☐ **[5.3.1.1]** A amostra é o universo de cada grupo, sem sorteio: os 32 projetos recusados em 2023 e 2024, os 95 habilitados de 2022-2024 cuja captação expirou, os 86 inabilitados das atas da CAP de 2022 a 2026 e, para a margem, os últimos validados de cada cota; os ciclos seguintes somam-se aos mesmos grupos.
    - checagem de dados: N80 ✔ (`analise/tabelas/12_cap_deliberacoes.csv`); N91 ✔ (`analise/tabelas/09_reentrada_resumo.csv`)
  - ☐ **[5.3.1.2]** O resultado precisa ser medido do mesmo modo em todos eles, e o relatório de execução só existe para quem recebeu.
  - ☐ **[5.3.1.3]** Por isso *Y* vem de uma pesquisa de acompanhamento com os proponentes, conferida em registros que independem da LICC.
  - ☐ **[5.3.1.4]** Esses registros, sozinhos, não bastam: fora da própria LICC, só 2 dos 32 recusados têm registro público do projeto.
    - checagem de dados: N88 ✔ (`analise/tabelas/22_recusados_outras_fontes.csv (PRONAC de mesmo título ou evento datado no Mapa)`)
  - ☐ **[5.3.1.5]** A chave de ligação é o CNPJ do proponente: o Portal da Transparência o traz para quem captou (ESPÍRITO SANTO, 2026a), e os avisos de habilitação no Diário Oficial, para a maior parte dos demais (DIO-ES, 2026); juntas, cobrem 385 dos 463 habilitados (83%), e o restante e os inabilitados ficam para a LAI (Quadro 4).
    - citações: ESPÍRITO SANTO, 2026a; DIO-ES, 2026
    - checagem de dados: N65 ✔ (`analise/tabelas/18_cobertura_cnpj.csv`)

### Quadro 4 – Fontes de dados da avaliação

- **Colunas:** Fonte · Conteúdo · Uso · Acesso
  - ☐ **Anexos de habilitados e captados, com as versões antigas** — Status, valor e patrocinador; recusados por esgotamento (2023-2024) — Grupos $\theta_1$ e $\theta_0$; margem — Público
  - ☐ **Extratos das atas da CAP** — Inabilitados de 2022 a 2026 — Filtro da CAP — Público
  - ☐ **Portal da Transparência; avisos do Diário Oficial** — Termos com CNPJ de proponente e patrocinador; habilitação e depósitos — Chave de ligação; captação posterior — Público
  - ☐ **SEFAZ** — Hora de protocolo e de validação, cota e recusados desde 2025 — Teste da fila; grupos de 2025 em diante — Pedido por LAI
  - ☐ **Pesquisa de acompanhamento** — Realização, data, público e fonte de financiamento de cada projeto; patrocínio fora da LICC — *Y* em todos os grupos; substituição — Coleta
  - ☐ **SALIC; agenda do Mapa Cultural; relatórios de execução** — Captação pela Lei Rouanet; eventos datados; realização e público dos financiados — Conferência de *Y* — Público; LAI

- **5.3.2** (fonte do quadro, tabela ou figura)
  - ☐ **[5.3.2.1]** Fonte: elaboração própria.


### 5.4 Cálculo do poder estatístico

- **5.4.1** — *Passo:* (a definir)
  - ☐ **[5.4.1.1]** Para comparar a proporção de projetos realizados entre dois grupos independentes, o efeito mínimo detectável (EMD), em pontos percentuais, é:

- ☐ **Fórmula do EMD** (conferir no PDF; parâmetros definidos na frase seguinte)

- **5.4.2** — *Passo:* Define os parâmetros da fórmula
  - ☐ **[5.4.2.1]** A fórmula segue Djimeu e Houndolo (2016), com α = 5% bicaudal e poder de 80%.
    - citações: Djimeu e Houndolo (2016)
    - ⚠ números sem checagem automática (conferir na fonte citada): 5%, 80%
  - ☐ **[5.4.2.2]** Nela, $n_1$ e $n_0$ são os tamanhos dos grupos e $p_0$ a proporção de realizados, ainda não medida, tomada de 0,3 a 0,7.
    - ⚠ números sem checagem automática (conferir na fonte citada): 0,3, 0,7

### Tabela 2 – Efeito mínimo detectável por contraste (pontos percentuais; $p_0$ de 0,3 a 0,7)

- **Colunas:** Contraste · Grupos · Unidades · EMD
  - ☐ ***V*: recusados × expirados** — recusados de 2023-2024; expirados de 2022-2024 — 32 × 95 — 26 a 29
    - checagem de dados: N92 ✔ (`analise/tabelas/23_poder_secao5.csv`)
  - ☐ **$\theta_0$ por faixa de valor** — expirados até R\$ 400 mil × acima — 58 × 37 — 27 a 29
    - checagem de dados: N93 ✔ (`analise/tabelas/23_poder_secao5.csv`)
  - ☐ **Filtro da CAP** — expirados × inabilitados — 95 × 86 — 19 a 21
    - checagem de dados: N94 ✔ (`analise/tabelas/23_poder_secao5.csv`)
  - ☐ **EMPT na margem** — últimos validados × recusados — 32 × 32 — 32 a 35
    - checagem de dados: N95 ✔ (`analise/tabelas/23_poder_secao5.csv`)
  - ☐ **Ampliação do teto em 2024** — recusas convertidas × mantidas — 27 × 20 — 38 a 41
    - checagem de dados: N96 ✔ (`analise/tabelas/23_poder_secao5.csv`)
  - ☐ ***V*, com mais quatro ciclos** — recusados × expirados acumulados — 96 × 222 — 16 a 17
    - checagem de dados: N97 ✔ (`analise/tabelas/23_poder_secao5.csv`)

- **5.4.3** (fonte do quadro, tabela ou figura)
  - ☐ **[5.4.3.1]** Fonte: elaboração própria; `analise/tabelas/23_poder_secao5.csv`.

- **5.4.4** — *Passo:* (a definir)
  - ☐ **[5.4.4.1]** Com os dados de hoje, o contraste principal só detecta diferenças de 26 a 29 pontos: basta para rejeitar a ausência de seleção se ela for forte, como sugere a queda da captação dos pedidos pequenos, mas não para medir seu tamanho.
    - checagem de dados: N98 ✔ (`analise/tabelas/23_poder_secao5.csv`)
  - ☐ **[5.4.4.2]** Com mais quatro ciclos no ritmo de 2022-2024, o EMD cai para 16 a 17 pontos.
    - checagem de dados: N99 ✔ (`analise/tabelas/23_poder_secao5.csv`)
  - ☐ **[5.4.4.3]** Comparar recusados pequenos e grandes continua exploratório: com mais quatro ciclos, detecta só 28 a 30 pontos.
    - checagem de dados: N100 ✔ (`analise/tabelas/23_poder_secao5.csv`)
  - ☐ **[5.4.4.4]** Com poder baixo, uma estimativa "significativa" tende a exagerar o efeito verdadeiro (GELMAN; CARLIN, 2014), o que recomenda pré-registrar a análise.
    - citações: GELMAN; CARLIN, 2014


### 5.5 Ameaças à validade e ética

- **5.5.1** — *Passo:* (a definir)
  - ☐ **[5.5.1.1]** A suposição central falha se os proponentes mais organizados, que também realizam mais, protocolam primeiro: os recusados seriam piores que a média dos escolhidos, e *V* ficaria subestimado; as horas de protocolo permitem testá-la.
  - ☐ **[5.5.1.2]** *V* e o efeito na margem valem para os escolhidos na margem da fila, e não para todos.
  - ☐ **[5.5.1.3]** Seguem-se o atrito da pesquisa, que pode ser maior entre expirados e inabilitados que desistiram e que os registros independentes limitam; a troca de fonte, porque a realização com recurso da Lei Rouanet ou de editais é medida à parte; e a interferência pelo teto fixo (SUTVA), porque o que um projeto capta falta a outro.
  - ☐ **[5.5.1.4]** A validade externa se restringe ao regime de 2022-2024, em que a habilitação precedia a busca por patrocinador: desde 2025 os expirados quase desapareceram (3 em 56 resolvidos no ciclo 2025), e $\theta_0$ passa a depender dos inscritos sem patrocinador, que só a LAI identifica.
    - checagem de dados: N27 ✔ (`analise/tabelas/07_funil_por_ciclo.csv`)
  - ☐ **[5.5.1.5]** No plano ético, a avaliação não nega nem adia acesso a ninguém, porque só acompanha grupos que a regra já produz.
  - ☐ **[5.5.1.6]** Dados identificados exigem anonimização (LGPD), e pesquisas com pessoas, aprovação de comitê de ética.


## 6 Conclusão

- **6.1** — *Passo:* Resume os achados do desenho
  - ☐ **[6.1.1]** A LICC é um gasto tributário que mais que dobrou de 2023 a 2026, sem problema declarado nem objetivos mensuráveis, e a avaliação contratada mede o efeito do gasto sobre a economia, e não o que ele acrescenta: o Estado paga, as empresas escolhem, e o público que usaria o bem cultural não passa pelo mecanismo.
  - ☐ **[6.1.2]** A escolha se concentra em poucas empresas de serviços regulados, que expõem a marca nas peças do projeto; entre os habilitados, a decisão fica com a empresa e com a fila dos termos; parte do recurso pode remunerar a intermediação; e quem não chega a um grande contribuinte fica de fora.
  - ☐ **[6.1.3]** A entrega, extremo da cadeia, é indeterminada, porque a SECULT não publica o público alcançado.

- **6.2** — *Passo:* Recomenda o que a gestão pode fazer sem mudar o mecanismo
  - ☐ **[6.2.1]** Sem alterar o mecanismo, a gestão pode declarar objetivos, metas e indicadores e publicar, em formato aberto, os inscritos, com CNPJ, sede e motivo de inabilitação; a captação por cota; a fila de termos, com datas de protocolo e validação, também dos recusados; e custos, contrapartidas e público alcançado.

- **6.3** — *Passo:* (a definir)
  - ☐ **[6.3.1]** A pergunta de impacto é se a renúncia vai para os projetos que dependem dela.
  - ☐ **[6.3.2]** Os grupos para respondê-la já existem pela regra atual, recusados por esgotamento da cota, habilitados sem patrocinador e inabilitados, e falta medir do mesmo modo, em todos, se os projetos se realizaram.
  - ☐ **[6.3.3]** Mais da metade dos recusados por falta de teto captou no ano seguinte, e a captação dos pedidos pequenos caiu a cada ciclo: se a seleção do mecanismo for positiva e maior nos pedidos grandes, ampliar o teto financia sobretudo o que ocorreria de todo modo, e as decisões que importam passam a ser quem entra e o que se entrega.
    - checagem de dados: N101 ✔ (`analise/tabelas/09_reentrada_resumo.csv`)


## Referências

Status da última conferência (`artigo/auditoria/checagem_referencias.csv`): VERIFIED = DOI conferido na Crossref sem divergência; sem_doi = referência sem DOI (norma, página oficial, livro), conferida na fonte indicada.

- ☐ BARROS, Ricardo Paes de; LIMA, Lycia. Avaliação de impacto de programas sociais: por que, para que e quando fazer? *In*: MENEZES FILHO, Naercio Aquino; PINTO, Cristine Campos de Xavier (org.). **Avaliação econômica de projetos sociais**. 3. ed. São Paulo: Fundação Itaú Social, 2017. p. 13-37.
  - conferência: sem_doi
- ☐ BELEM, Marcela Purini; DONADONE, Julio Cesar. A Lei Rouanet e a construção do "mercado de patrocínios culturais". **NORUS – Novos Rumos Sociológicos**, Pelotas, v. 1, n. 1, 2013. Disponível em: https://periodicos.ufpel.edu.br/index.php/NORUS/article/view/2761.
  - conferência: sem_doi
- ☐ BERTRAND, Marianne; BOMBARDINI, Matilde; FISMAN, Raymond; TREBBI, Francesco. Tax-exempt lobbying: corporate philanthropy as a tool for political influence. **American Economic Review**, v. 110, n. 7, p. 2065-2102, 2020. DOI: 10.1257/aer.20180615.
  - conferência: VERIFIED
- ☐ BRASIL. Lei Complementar nº 123, de 14 de dezembro de 2006. Institui o Estatuto Nacional da Microempresa e da Empresa de Pequeno Porte. **Diário Oficial da União**, Brasília, 15 dez. 2006. Disponível em: https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp123.htm. Acesso em: 27 set. 2026.
  - conferência: sem_doi
- ☐ BRASIL. Tribunal de Contas da União. **Acórdão nº 191/2016 – Plenário**. Relator: Augusto Sherman Cavalcanti. Brasília, 3 fev. 2016.
  - conferência: sem_doi
- ☐ BRASIL. Secretaria do Tesouro Nacional. **SICONFI**: Declaração de Contas Anuais (DCA) do Estado do Espírito Santo e de seus municípios, 2021-2025. Brasília: STN, 2026. Disponível em: https://apidatalake.tesouro.gov.br/ords/siconfi/tt/dca. Acesso em: 23 set. 2026.
  - conferência: sem_doi
- ☐ BUTERIN, Vitalik; HITZIG, Zoë; WEYL, E. Glen. A flexible design for funding public goods. **Management Science**, v. 65, n. 11, p. 5171-5187, 2019. DOI: 10.1287/mnsc.2019.3337.
  - conferência: VERIFIED
- ☐ COSTA, Camila Furlan da; MEDEIROS, Igor Baptista de Oliveira; BUCCO, Guilherme Brandelli. O financiamento da cultura no Brasil no período 2003-15: um caminho para geração de renda monopolista. **Revista de Administração Pública**, Rio de Janeiro, v. 51, n. 4, p. 509-527, 2017. DOI: 10.1590/0034-7612162254.
  - conferência: VERIFIED
- ☐ DEKKER, Erwin; RODRIGUES, Ana Carolina. The political economy of Brazilian cultural policy: a case study of the Rouanet Law. **Journal of Public Finance and Public Choice**, v. 34, n. 2, p. 149-171, 2019. DOI: 10.1332/251569119X15675896589688.
  - conferência: VERIFIED
- ☐ DIO-ES – DEPARTAMENTO DE IMPRENSA OFICIAL DO ESPÍRITO SANTO. **Diário Oficial dos Poderes do Estado**: atos e avisos da LICC, 2022-2026. Vitória: DIO-ES, 2026. Disponível em: https://ioes.dio.es.gov.br. Acesso em: 27 set. 2026.
  - conferência: sem_doi
- ☐ DJIMEU, Eric W.; HOUNDOLO, Deo-Gracias. Power calculation for causal inference in social science: sample size and minimum detectable effect determination. **Journal of Development Effectiveness**, v. 8, n. 4, p. 508-527, 2016. DOI: 10.1080/19439342.2016.1244555.
  - conferência: VERIFIED
- ☐ ESPÍRITO SANTO (Estado). Lei nº 11.246, de 7 de abril de 2021. Introduz alterações na Lei nº 7.000, de 27 de dezembro de 2001. **Diário Oficial dos Poderes do Estado**, Vitória, 8 abr. 2021a.
  - conferência: sem_doi
- ☐ ESPÍRITO SANTO (Estado). Decreto nº 5.035-R, de 15 de dezembro de 2021. Dispõe sobre a regulamentação do incentivo fiscal concedido nos termos do art. 5º-B, IX, da Lei nº 7.000, de 27 de dezembro de 2001. **Diário Oficial dos Poderes do Estado**, Vitória, 16 dez. 2021b.
  - conferência: sem_doi
- ☐ ESPÍRITO SANTO (Estado). **Portal da Transparência**: incentivos, isenções e beneficiários. Vitória: SECONT, 2026a. Disponível em: https://transparencia.es.gov.br/comum/incentivosfiscais. Acesso em: 27 set. 2026.
  - conferência: sem_doi
- ☐ ESPÍRITO SANTO (Estado). Secretaria de Estado de Economia e Planejamento. **Relatório de avaliação 2025**: Plano Plurianual 2024-2027, exercício de 2025. Vitória: SEP, 2026b. Disponível em: https://planejamento.es.gov.br/media/Planejamento/PPA_2024_2027/RelatoriosAvaliacaoALES/relatorio_ales_oficial_2025-versao-final.pdf. Acesso em: 28 set. 2026.
  - conferência: sem_doi
- ☐ FELD, Alan L.; O'HARE, Michael; SCHUSTER, J. Mark Davidson. **Patrons despite themselves**: taxpayers and arts policy. New York: New York University Press, 1983.
  - conferência: sem_doi
- ☐ FINKELSTEIN, Amy; NOTOWIDIGDO, Matthew J. Take-up and targeting: experimental evidence from SNAP. **The Quarterly Journal of Economics**, v. 134, n. 3, p. 1505-1556, 2019. DOI: 10.1093/qje/qjz013.
  - conferência: VERIFIED
- ☐ FOGUEL, Miguel Nathan. Modelo de resultados potenciais. *In*: MENEZES FILHO, Naercio Aquino; PINTO, Cristine Campos de Xavier (org.). **Avaliação econômica de projetos sociais**. 3. ed. São Paulo: Fundação Itaú Social, 2017. p. 39-54.
  - conferência: sem_doi
- ☐ GELMAN, Andrew; CARLIN, John. Beyond power calculations: assessing type S (sign) and type M (magnitude) errors. **Perspectives on Psychological Science**, v. 9, n. 6, p. 641-651, 2014. DOI: 10.1177/1745691614551642.
  - conferência: VERIFIED
- ☐ GERTLER, Paul J.; MARTÍNEZ, Sebastián; PREMAND, Patrick; RAWLINGS, Laura B.; VERMEERSCH, Christel M. J. **Avaliação de impacto na prática**. 2. ed. Washington, DC: Banco Interamericano de Desenvolvimento; Banco Mundial, 2018.
  - conferência: sem_doi
- ☐ HITZIG, Zoë. What are public goods and how do they link people in a society? **EXPeditions**, 13 set. 2021. Disponível em: https://www.joinexpeditions.com/exps/332-what-are-public-goods-and-how-do-they-link-people-in-a-society-. Acesso em: 27 set. 2026.
  - conferência: sem_doi
- ☐ IBGE. **Sistema de Informações e Indicadores Culturais**. Rio de Janeiro: IBGE, 2025. Base de dados; períodos 2023 e 2024 publicados em 12 dez. 2025. Disponível em: https://servicodados.ibge.gov.br/api/v1/pesquisas/10092. Acesso em: 23 set. 2026.
  - conferência: sem_doi
- ☐ IBGE. **Pesquisa de Informações Básicas Municipais – MUNIC 2021**. Rio de Janeiro: IBGE, 2022. Dados consultados pela API de pesquisas do IBGE em 23 set. 2026.
  - conferência: sem_doi
- ☐ IJSN – INSTITUTO JONES DOS SANTOS NEVES. **Secult e IJSN divulgam estudo sobre impactos das políticas culturais capixabas durante o evento Cultura em Dados**. Vitória: IJSN, 2026. Notícia. Disponível em: https://ijsn.es.gov.br/Contents/Item/Display/17195. Acesso em: 28 set. 2026.
  - conferência: sem_doi
- ☐ MAYNE, John. Useful theory of change models. **Canadian Journal of Program Evaluation**, v. 30, n. 2, p. 119-142, 2015. DOI: 10.3138/cjpe.230.
  - conferência: VERIFIED
- ☐ MOYNIHAN, Donald; HERD, Pamela; HARVEY, Hope. Administrative burden: learning, psychological, and compliance costs in citizen-state interactions. **Journal of Public Administration Research and Theory**, v. 25, n. 1, p. 43-69, 2015. DOI: 10.1093/jopart/muu009.
  - conferência: VERIFIED
- ☐ OGAVA, Bruno; GALVÃO, César Augusto; ADAMCZYK, Willian. **Financiamento quadrático para os incentivos à cultura no Brasil**: simulações sobre a Lei Rouanet. Brasília: Enap; UnB, 2022. (Evidência Express). Disponível em: https://repositorio.enap.gov.br/handle/1/7004. Acesso em: 27 set. 2026.
  - conferência: sem_doi
- ☐ O'HAGAN, J.; HARVEY, D. Why do companies sponsor arts events? Some evidence and a proposed classification. **Journal of Cultural Economics**, v. 24, n. 3, p. 205-224, 2000. DOI: 10.1023/A:1007653328733.
  - conferência: VERIFIED
- ☐ SECULT – SECRETARIA DE ESTADO DA CULTURA DO ESPÍRITO SANTO. **Boletim de Economia Criativa**: Espírito Santo, 2º trimestre de 2020. Vitória: SECULT, 2020. Disponível em: https://secult.es.gov.br/media/002/Boletim_Economia_Criativa_02T_2020.pdf. Acesso em: 27 set. 2026.
  - conferência: sem_doi
- ☐ SECULT – SECRETARIA DE ESTADO DA CULTURA DO ESPÍRITO SANTO. **Instrução Normativa nº 002, de 31 de janeiro de 2022**. Vitória: SECULT, 2022. Disponível em: https://secult.es.gov.br/media/2022/INSTRU__O_NORMATIVA_LICC_-_SECULT.pdf. Acesso em: 27 set. 2026.
  - conferência: sem_doi
- ☐ SECULT – SECRETARIA DE ESTADO DA CULTURA DO ESPÍRITO SANTO. Instrução Normativa nº 001, de 31 de janeiro de 2023. **Diário Oficial dos Poderes do Estado**, Vitória, 1º fev. 2023a. Disponível em: https://secult.es.gov.br/instrucao-normativa-licc-2023. Acesso em: 24 set. 2026.
  - conferência: sem_doi
- ☐ SECULT – SECRETARIA DE ESTADO DA CULTURA DO ESPÍRITO SANTO. Regimento interno da Comissão de Avaliação Permanente (CAP) da Lei de Incentivo à Cultura Capixaba. **Diário Oficial dos Poderes do Estado**, Vitória, 16 fev. 2023b. Disponível em: https://secult.es.gov.br/legislacao-licc. Acesso em: 23 set. 2026.
  - conferência: sem_doi
- ☐ SECULT – SECRETARIA DE ESTADO DA CULTURA DO ESPÍRITO SANTO. Instrução Normativa nº 001, de 31 de janeiro de 2024. **Diário Oficial dos Poderes do Estado**, Vitória, 1º fev. 2024a. Disponível em: https://secult.es.gov.br/instrucao-normativa-licc-2024. Acesso em: 24 set. 2026.
  - conferência: sem_doi
- ☐ SECULT – SECRETARIA DE ESTADO DA CULTURA DO ESPÍRITO SANTO. Portaria nº 078, de 31 de julho de 2024. Introduz alterações no artigo 12 da Instrução Normativa nº 001 de 31 de janeiro de 2024. Vitória: SECULT, 2024b. Disponível em: https://secult.es.gov.br/media/2024/PORTARIA_SECULT_N%C2%BA_078%2C_DE_31_DE_JULHO_DE_2024.pdf. Acesso em: 23 set. 2026.
  - conferência: sem_doi
- ☐ SECULT – SECRETARIA DE ESTADO DA CULTURA DO ESPÍRITO SANTO. **Instrução Normativa nº 001/2025, de 14 de janeiro de 2025**. Vitória: SECULT, 2025a.
  - conferência: sem_doi
- ☐ SECULT – SECRETARIA DE ESTADO DA CULTURA DO ESPÍRITO SANTO. Portaria nº 062-S, de 9 de maio de 2025. Altera a Instrução Normativa nº 001 de 31 de janeiro de 2025. **Diário Oficial dos Poderes do Estado**, Vitória, 2025b.
  - conferência: sem_doi
- ☐ SECULT – SECRETARIA DE ESTADO DA CULTURA DO ESPÍRITO SANTO. **Edital de credenciamento nº 001/2025**: serviços de pareceristas da Lei de Incentivo à Cultura Capixaba; lista de credenciados por área, atualizada em 18 set. 2026. Vitória: SECULT, 2025c. Disponível em: https://secult.es.gov.br/credenciamento. Acesso em: 27 set. 2026.
  - conferência: sem_doi
- ☐ SECULT – SECRETARIA DE ESTADO DA CULTURA DO ESPÍRITO SANTO. **Instrução Normativa nº 001/2026, de 12 de janeiro de 2026**. Vitória: SECULT, 2026a.
  - conferência: sem_doi
- ☐ SECULT – SECRETARIA DE ESTADO DA CULTURA DO ESPÍRITO SANTO. **Recursos financeiros captados**: anexos "Recurso financeiro captado" de 2022 a 2026. Vitória: SECULT, 2026c. Disponível em: https://secult.es.gov.br/recursos-financeiros-captados. Acesso em: 24 set. 2026.
  - conferência: sem_doi
- ☐ SECULT – SECRETARIA DE ESTADO DA CULTURA DO ESPÍRITO SANTO. **Mapa Cultural do Espírito Santo**: API pública de agentes e oportunidades (inclusive as fases de avaliação da LICC). Vitória: SECULT, 2026d. Disponível em: https://mapa.cultura.es.gov.br. Acesso em: 24 set. 2026.
  - conferência: sem_doi
- ☐ SECULT – SECRETARIA DE ESTADO DA CULTURA DO ESPÍRITO SANTO. **Parecer técnico cultural LICC**: modelo padrão. Vitória: SECULT, 2026e. Disponível em: https://secult.es.gov.br/LICC. Acesso em: 24 set. 2026.
  - conferência: sem_doi
- ☐ SECULT – SECRETARIA DE ESTADO DA CULTURA DO ESPÍRITO SANTO. **Lista de projetos habilitados** (seções 2022 a 2026) e **Recurso financeiro captado – 2025**. Vitória: SECULT, 2026b. Disponível em: https://secult.es.gov.br/lista-de-projetos-habilitados. Acesso em: 3 set. 2026.
  - conferência: sem_doi
- ☐ SECULT – SECRETARIA DE ESTADO DA CULTURA DO ESPÍRITO SANTO. **Comissão de Avaliação Permanente (CAP)**: extratos das atas das reuniões, 2023 a 2026. Vitória: SECULT, 2026f. Disponível em: https://secult.es.gov.br/cap-2026. Acesso em: 27 set. 2026.
  - conferência: sem_doi
- ☐ SECULT – SECRETARIA DE ESTADO DA CULTURA DO ESPÍRITO SANTO. **Ata de julgamento de recursos e resultado final da etapa de pré-seleção de projetos**: Edital nº 29/2025, produção de curta e média-metragem. Vitória: SECULT, 2026g. Disponível em: https://secult.es.gov.br/media/ata-de-julgamento-de-recursos-pre-selecao-29-2025.pdf. Acesso em: 27 set. 2026.
  - conferência: sem_doi
- ☐ SILVA, Frederico Augusto Barbosa da. **Financiamento cultural no Brasil contemporâneo**. Brasília: Ipea, 2017. (Texto para Discussão, 2280).
  - conferência: sem_doi
- ☐ TEIXEIRA, Lusvânio Carlos; XAVIER, Wescley Silva; FARIA, Evandro Rodrigues de; BRAVIM, Márcio Teixeira. Relação entre os equipamentos e políticas culturais dos municípios de Minas Gerais e a captação de recursos via Lei Estadual de Incentivo à Cultura. **Interações**, Campo Grande, v. 22, n. 2, p. 405-419, 2021. DOI: 10.20435/inter.v22i2.2965.
  - conferência: VERIFIED
- ☐ WHITE, Howard; RAITZER, David A. **Impact evaluation of development interventions**: a practical guide. Mandaluyong City: Asian Development Bank, 2017. DOI: 10.22617/TCS179188-2.
  - conferência: VERIFIED
- ☐ WILLIAMS, Martin J. External validity and policy adaptation: from impact evaluation to policy design. **The World Bank Research Observer**, v. 35, n. 2, p. 158-191, 2020. DOI: 10.1093/wbro/lky010.
  - conferência: VERIFIED

## Números a conferir à mão

190 frases e linhas de tabela; 46 com checagem automática de dados. Abaixo, as que têm números sem checagem automática (a maioria é regra de norma; conferir na fonte citada):

### Dado ou literatura (17)

- ☐ [1.1.3]: 25, 63
- ☐ [1.2.1]: 27
- ☐ [3.2.3]: 853
- ☐ linha «Escolha (H1)»: 25%
- ☐ linha «Entrega (H5)»: 30%
- ☐ [4.2.4.1]: 2026
- ☐ [4.2.5.1]: 2026
- ☐ [4.2.6.4]: 400
- ☐ [4.2.10.1]: 30%
- ☐ [5.1.2.1]: 1
- ☐ [5.1.2.2]: 1, 0
- ☐ [5.1.3.1]: 0
- ☐ linha «*V* = $\theta_1$ − $\theta_0$ (H1, H4)»: 0
- ☐ [5.2.2.3]: 25
- ☐ [5.2.2.4]: 86
- ☐ [5.4.2.1]: 5%, 80%
- ☐ [5.4.2.2]: 0,3, 0,7

### Regra de norma (11)

- ☐ [2.1.4]: 100%
- ☐ linha «Benefício ao patrocinador»: 100%
- ☐ linha «Teto anual»: 31, 01, 2%, 15, 10, 25
- ☐ linha «Patrocinador»: 20%, 15%, 10%, 5%
- ☐ linha «Proponentes»: 2, 3
- ☐ linha «Linhas e limite por projeto»: 1, 300, 001
- ☐ linha «Alocação entre habilitados»: 30%, 10, 10%, 50%
- ☐ linha «Custos com o recurso incentivado»: 10%, 15, 25%
- ☐ [4.2.7.3]: 35%
- ☐ [4.2.9.2]: 1, 3
- ☐ [4.2.9.4]: 10%

