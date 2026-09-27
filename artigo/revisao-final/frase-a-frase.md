# Revisão final frase a frase

- **Texto revisado:** `artigo/rascunho-artigo.md`, sha256 `a8100b5b0235682d…`, gerado por `artigo/revisao-final/gerar_frase_a_frase.py`.
- **Como usar:** cada parágrafo abre com o **passo** que ele cumpre no argumento. Cada frase vem literal, numerada como seção.parágrafo.frase, com uma caixa ☐ para marcar (☒ ok; ✎ editar). As edições vão para o `rascunho-artigo.md`; depois, rodar de novo `checar_dados.py`, `checar_referencias.py`, `gerar_tex.py --pdf` e este script.
- **Base de cada frase:**
  - *citações*: as referências que a frase cita;
  - *checagem de dados*: o número foi recalculado a partir da tabela indicada (✔ confere na última execução);
  - *⚠ números sem checagem automática*: número que nenhuma checagem cobre; conferir na norma ou na fonte citada (muitos são regras de norma, como percentuais e tetos, e não dados).

## Título

- ☐ **[0.1]** Quem escolhe o que o Estado financia? Avaliação do desenho da Lei de Incentivo à Cultura Capixaba e proposta de avaliação de impacto

## Resumo e palavras-chave

- **0.1** — *Passo:* O artigo em um parágrafo: mecanismo, o que se avalia, os achados de desenho e a proposta
  - ☐ **[0.1.1]** **Resumo.** A Lei de Incentivo à Cultura Capixaba (LICC) permite que empresas contribuintes do ICMS destinem a projetos culturais habilitados pela Secretaria da Cultura (SECULT) valores que recuperam integralmente como crédito presumido do imposto: o Estado paga, a empresa escolhe, e o público a quem o bem cultural se destina não entra na escolha.
  - ☐ **[0.1.2]** Avalia-se o desenho como ele está, com a auditoria de cinco premissas da teoria da mudança a partir de normas, anexos oficiais e atas da comissão de 2022 a 2026, e estrutura-se uma avaliação de impacto.
  - ☐ **[0.1.3]** A escolha não se mostra orientada pelo valor público: duas empresas respondem por metade da renúncia de 2025, e as peças de comunicação dos projetos trazem a marca do patrocinador.
    - checagem de dados: D03 ✔ (`analise/tabelas/03_patrocinadores_concentracao.csv`)
  - ☐ **[0.1.4]** A decisão se concentra em poucos atores: a habilitação qualifica sem priorizar, e o que excede o teto é racionado pela ordem de recebimento e validação dos termos de patrocínio.
  - ☐ **[0.1.5]** Até 13% do valor captado em 2025 poderia remunerar captação e elaboração, projetos pequenos captam cada vez menos, e só pessoas jurídicas contribuintes patrocinam.
    - checagem de dados: N51 ✔ (`analise/tabelas/10_taxa_servico_permitida_2025.csv`)
  - ☐ **[0.1.6]** A entrega é indeterminada, porque a SECULT não publica o público alcançado.
  - ☐ **[0.1.7]** Propõem-se quatro perguntas de avaliação, com estratégias, dados e poder estatístico, entre elas um experimento conjunto com decisores de empresas.

- **0.2** — *Passo:* Palavras-chave
  - ☐ **[0.2.1]** **Palavras-chave:** incentivo fiscal à cultura; gasto tributário; patrocínio; bens públicos; teoria da mudança; avaliação de impacto.


## 1 Introdução

- **1.1** — *Passo:* Apresenta a lei e dimensiona a política: teto anual, teto esgotado e demanda habilitada acima do teto
  - ☐ **[1.1.1]** A Lei estadual nº 11.246/2021 incluiu na lei do ICMS um crédito presumido correspondente ao valor que o contribuinte destina a projetos culturais credenciados pela Secretaria da Cultura (SECULT), com efeitos a partir de 2022 (ESPÍRITO SANTO, 2021a).
    - citações: ESPÍRITO SANTO, 2021a
  - ☐ **[1.1.2]** A Lei de Incentivo à Cultura Capixaba, como o mecanismo passou a ser chamado no regulamento (ESPÍRITO SANTO, 2021b), cresceu rapidamente: o teto anual de captação, o montante fixado pela SEFAZ, passou de R\$ 15 milhões em 2023 para R\$ 31 milhões em 2026. [nota de rodapé: teto2022]
    - citações: ESPÍRITO SANTO, 2021b
    - checagem de dados: D05 ✔ (`dados/externos/licc_teto_vs_icms.csv`)
    - ☐ *Nota de rodapé (teto2022):* Para 2022, a Portaria SEFAZ nº 09-R fixou R\$ 10 milhões, e o anexo de captação da SECULT informa R\$ 15 milhões disponíveis (R\$ 11,5 milhões validados), valor que a lista do Portal da Transparência atribui à mesma portaria (ESPÍRITO SANTO, 2026). Sem ato de ampliação localizado, o teto de 2022 fica indeterminado.
      - citações: ESPÍRITO SANTO, 2026
      - checagem de dados: D65b ✔ (`analise/tabelas/16_transparencia_resumo.csv (LIMITE PORTARIA SEFAZ Nº 09-R/2022 = 15.000.000, Download/378)`); D65 ✔ (`analise/tabelas/03f_captacao_anual_secult.csv`)
  - ☐ **[1.1.3]** De 2023 a 2025, a captação esgotou o teto: os termos de patrocínio listados pela SECULT somam exatamente o montante de cada ano (em 2025, 62 projetos validados somam R\$ 24,64 milhões, e um ainda "em análise na SEFAZ" completa os R\$ 25 milhões; os números de 2025 contam os 63).
    - checagem de dados: D07 ✔ (`artigo/auditoria/auditoria_captacao_anual.csv (auditar_captacao.py, sobre o anexo oficial de 2025)`); N45 ✔ (`artigo/auditoria/auditoria_captacao_anual.csv (2023-2025)`)
    - ⚠ números sem checagem automática (conferir na fonte citada): 25, 63
  - ☐ **[1.1.4]** A demanda supera o teto: nos cinco ciclos de habilitação (2022-2026), 463 projetos foram autorizados a captar, somados, R\$ 184 milhões (459 com valor válido), acima da soma dos tetos do período, de no máximo R\$ 111 milhões. [nota de rodapé: repo]
    - checagem de dados: D06 ✔ (`analise/tabelas/03_anual.csv (valor autorizado`); D06b ✔ (`artigo/auditoria/auditoria_captacao_anual.csv (maior entre portaria e montante impresso, 2022-2026) < 03_anual.csv`)
    - ☐ *Nota de rodapé (repo):* Todos os números deste artigo vêm dos anexos oficiais da SECULT ("Lista de projetos habilitados" e "Recurso financeiro captado", de 2022 a 2026), de bases públicas do IBGE, do Tesouro Nacional (SICONFI) e do Portal da Transparência do ES. A lista de habilitados foi transcrita na versão disponível em 3 set. 2026 (repositório licc.gov); a SECULT atualizou o arquivo em 10 set. 2026, e os status publicados podem ter mudado desde então. Dados, scripts e tabelas: <https://github.com/fcarva/aval-pol>.
      - ⚠ números sem checagem automática (conferir na fonte citada): 3, 10

- **1.2** — *Passo:* Reconstrói o problema que a lei não declara e o enuncia
  - ☐ **[1.2.1]** Nenhuma norma da LICC declara o problema que ela enfrenta; o diagnóstico precisa ser reconstruído.
  - ☐ **[1.2.2]** O setor cultural capixaba é pequeno para o tamanho da economia do estado: em 2024, ocupava 4,2% dos trabalhadores do ES, contra 5,8% no país, a 18ª participação entre as 27 unidades da federação (IBGE, 2025).
    - citações: IBGE, 2025
    - checagem de dados: D08 ✔ (`dados/externos/siic_uf.csv`)
    - ⚠ números sem checagem automática (conferir na fonte citada): 27
  - ☐ **[1.2.3]** Na economia criativa, que soma às artes atividades de mercado como design e publicidade, o estado ficava perto da média: 8,2% dos ocupados no 2º trimestre de 2020, contra 8,5% no país, a 8ª posição (SECULT, 2020).
    - citações: SECULT, 2020
    - checagem de dados: N64 ✔ (`dados/fontes_web/paginas/boletim_ec_boletim_economia_criativa_02t_2020.txt (SECULT, Boletim 2T2020)`)
  - ☐ **[1.2.4]** O contraste sugere que o atraso está no núcleo cultural, e não na atividade criativa como um todo.
  - ☐ **[1.2.5]** A desigualdade relevante, porém, é interna: em 2021, 95% da população da Região Metropolitana da Grande Vitória (RMGV) vivia em município com cinema, contra 34% da do interior, e metade dos municípios do interior não tinha fundo municipal de cultura (IBGE, 2022).
    - citações: IBGE, 2022
    - checagem de dados: D09 ✔ (`dados/externos/munic2021_cultura_es_resumo.csv`); D10 ✔ (`dados/externos/munic2021_cultura_es_resumo.csv`)
  - ☐ **[1.2.6]** O problema é, assim, **a baixa e desigual capacidade de financiar a produção e a oferta cultural fora do circuito já consolidado**, com causas na restrição de financiamento de pequenos produtores, na concentração de equipamentos e na dependência de poucos financiadores.

- **1.3** — *Passo:* Justifica a avaliação: gasto fora do orçamento, decisão privada, regra instável
  - ☐ **[1.3.1]** A avaliação da LICC se justifica por três razões.
  - ☐ **[1.3.2]** Primeiro, trata-se de gasto público que não passa pelo lado da despesa do orçamento: a renúncia efetiva equivale a 14% a 21% do gasto estadual direto na função cultura em 2022-2025 (SECULT, 2026c; BRASIL, 2026).
    - citações: SECULT, 2026c; BRASIL, 2026
    - checagem de dados: D11 ✔ (`analise/tabelas/03f_captacao_anual_secult.csv (validado_sobre_f13_estado, 2022-2025)`)
  - ☐ **[1.3.3]** Segundo, quem decide o destino do recurso é a empresa patrocinadora, e não o Estado, o que expõe a política às críticas de concentração e de lógica de marketing feitas à Lei Rouanet (SILVA, 2017; DEKKER; RODRIGUES, 2019).
    - citações: SILVA, 2017; DEKKER; RODRIGUES, 2019
  - ☐ **[1.3.4]** Terceiro, a política é nova e muda de regra a cada ano.

- **1.4** — *Passo:* Declara os objetivos e o roteiro do artigo
  - ☐ **[1.4.1]** O artigo tem dois objetivos: avaliar o desenho da LICC **como ela está**, sem propor redesenho do mecanismo, e estruturar uma avaliação de impacto, com desenho amostral, fontes de dados e cálculo de poder.
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
  - ☐ **Teto anual** — Fixado pela SEFAZ até 31/01, ampliável no exercício, limitado a 2% do ICMS estadual do ano anterior: R\$ 10 mi em 2022, 15 mi (2023), 25 mi (2024 e 2025), 31 mi (2026) — Dec. 5.035-R/2021, art. 4º; Dec. 5.210-R/2022; portarias SEFAZ
    - ⚠ números sem checagem automática (conferir na fonte citada): 31, 01, 2%, 10, 15, 25
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
  - ☐ **[2.3.2]** A primeira é a **delegação da escolha**: o Estado define quem pode receber; a empresa define quem recebe.
  - ☐ **[2.3.3]** A segunda é a **instabilidade**: a SECULT edita uma instrução normativa por ano, fechou as inscrições em meados de 2024 e alterou o fluxo em meados de 2025 (SECULT, 2024b; 2025b); até 2024 a comissão habilitava antes da captação, e desde 2025 o projeto só vai à comissão com patrocinador (SECULT, 2025a, arts. 41-45).
    - citações: SECULT, 2024b; 2025b; SECULT, 2025a, arts. 41-45
  - ☐ **[2.3.4]** A terceira é a **pouca informação publicada**: os anexos não trazem o CNPJ do proponente, a sede nem indicador de resultado, e os inabilitados só aparecem, sem motivo, nos extratos das atas da comissão (SECULT, 2026f).
    - citações: SECULT, 2026f


## 3 Breve revisão da literatura

- **3.1** — *Passo:* Situa a LICC na literatura: incentivo fiscal com decisão privada, falha de mercado, bens públicos e o crédito de 100% como extremo
  - ☐ **[3.1.1]** **Despesa tributária com decisão privada.** A literatura de economia da cultura trata o incentivo fiscal como um subsídio em que o doador decide a alocação e o Tesouro paga a conta: para Feld, O'Hare e Schuster (1983), os contribuintes americanos se tornaram "mecenas apesar de si mesmos", porque financiam pela renúncia escolhas que não fazem.
    - citações: O'Hare e Schuster (1983)
  - ☐ **[3.1.2]** A justificativa econômica usual é de falha de mercado: a produtividade estagnada das artes ao vivo (BAUMOL; BOWEN, 1966) e os benefícios que a cultura gera também para quem não a consome, que fazem dela bem público ou meritório (THROSBY, 1994).
    - citações: BAUMOL; BOWEN, 1966; THROSBY, 1994
  - ☐ **[3.1.3]** Bens públicos são consumidos em grupo, e não por indivíduos, e por isso são "o tecido que conecta as pessoas" (HITZIG, 2021, tradução nossa); Buterin, Hitzig e Weyl (2019) tratam seu financiamento como formação de comunidades e mostram que, se o valor recebido cresce com o número de contribuintes, e não só com o total aportado, a provisão é ótima no modelo padrão.
    - citações: HITZIG, 2021, tradução nossa; Hitzig e Weyl (2019)
  - ☐ **[3.1.4]** Nesse espectro de subsídios, o crédito de 100% da LICC ocupa o extremo: o doador não tem custo líquido algum.
    - ⚠ números sem checagem automática (conferir na fonte citada): 100%
  - ☐ **[3.1.5]** Sem custo, não há efeito-preço sobre o patrocínio, e restam duas margens: a troca de fonte (a empresa paga com ICMS o patrocínio que já faria com verba própria ou pela Rouanet) e o efeito sobre o projeto.

- **3.2** — *Passo:* Traz a experiência da Lei Rouanet: concentração, mercado de patrocínios, adicionalidade e TCU
  - ☐ **[3.2.1]** **A experiência brasileira com a Lei Rouanet.** A LICC reproduz o núcleo do mecenato federal, que acumula três décadas de crítica: concentração regional no Sudeste (SILVA, 2017), concentração persistente de patrocinadores e proponentes (COSTA; MEDEIROS; BUCCO, 2017) e um "mercado de patrocínios" com intermediários e departamentos de marketing (BELEM; DONADONE, 2013).
    - citações: SILVA, 2017; COSTA; MEDEIROS; BUCCO, 2017; BELEM; DONADONE, 2013
  - ☐ **[3.2.2]** Dekker e Rodrigues (2019) concluem que a lei beneficiou sobretudo projetos já bem-sucedidos e que não está claro qual falha de mercado ela corrige, dúvida que vale para a LICC (seção 4.2).
    - citações: Dekker e Rodrigues (2019)
  - ☐ **[3.2.3]** O Tribunal de Contas da União recomendou objetivos, indicadores e metas para as renúncias (BRASIL, 2014) e determinou que não se autorizasse captação a projetos com forte potencial lucrativo ou capacidade de atrair investimento privado (BRASIL, 2016).
    - citações: BRASIL, 2014; BRASIL, 2016
  - ☐ **[3.2.4]** Em 2010-2019, o maior doador destinou 853 vezes o valor do doador médio, e o número de doadores de um projeto não se relaciona com a parcela do aprovado que ele capta (OGAVA; GALVÃO; ADAMCZYK, 2022).
    - citações: OGAVA; GALVÃO; ADAMCZYK, 2022
    - ⚠ números sem checagem automática (conferir na fonte citada): 853

- **3.3** — *Passo:* Mostra que não há evidência causal no Brasil e que a externa aponta efeitos pequenos
  - ☐ **[3.3.1]** **Evidência causal.** Não se localizou avaliação causal de incentivo cultural no Brasil; as avaliações encontradas de leis estaduais via ICMS são descritivas: em Minas Gerais, a captação pela lei estadual concentrou-se na região metropolitana de Belo Horizonte, e municípios com museu, teatro ou cinema tinham mais chance de captar (TEIXEIRA *et al.*, 2021).
    - citações: TEIXEIRA *et al.*, 2021
  - ☐ **[3.3.2]** Fora do Brasil, os créditos estaduais ao audiovisual nos Estados Unidos têm efeitos pequenos, restritos à própria atividade incentivada (THOM, 2018).
    - citações: THOM, 2018
  - ☐ **[3.3.3]** Para a LICC, que financia produções dispersas, os efeitos plausíveis são proximais e pequenos.


## 4 Desenho da política e sua avaliação


### 4.1 Teoria da mudança

- **4.1.1** — *Passo:* Explica como a teoria da mudança é reconstruída e por que tem três cadeias
  - ☐ **[4.1.1.1]** Como nenhuma norma da LICC explicita como ela produziria resultados, a teoria da mudança (Figura 1) é reconstruída pelos cinco passos do J-PAL: propósito, cadeia causal, premissas e riscos, hipótese causal e indicadores.
  - ☐ **[4.1.1.2]** Na cadeia de resultados de Gertler *et al.* (2018), os produtos estão sob controle da agência; na LICC, o produto "projeto patrocinado" depende de um terceiro, a empresa.
    - citações: Gertler *et al.* (2018)
  - ☐ **[4.1.1.3]** Por isso a Figura 1 separa três cadeias, como recomendam White e Raitzer (2017): a entrada, o financiamento e a entrega, e indica quem decide em cada elo.
    - citações: White e Raitzer (2017)

- **4.1.2** — *Passo:* Enuncia a hipótese causal no formato do J-PAL
  - ☐ **[4.1.2.1]** Na forma do J-PAL, a hipótese causal é: *se* a SECULT abre a inscrição e habilita projetos culturais, e empresas contribuintes patrocinam parte deles com o ICMS que pagariam, *então* se forma um cardápio de projetos habilitados e um conjunto de projetos patrocinados e executados, *o que deveria levar* a mais bens culturais de acesso público, executados por proponentes mais diversos e mais capazes, *que ao final melhorarão* o acesso da população à cultura e reduzirão sua desigualdade territorial, *contribuindo para* ampliar e desconcentrar a capacidade de financiar a cultura no estado.

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

### Figura 1 – Teoria da mudança da LICC, com as premissas testadas

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
  - ☐ **[4.2.2.2]** Não há meta, magnitude esperada nem indicador.
  - ☐ **[4.2.2.3]** A LICC não atende ao critério de que um programa declare resultados e magnitude esperados (BARROS; LIMA, 2017), nem ao padrão do TCU para renúncias, com objetivos, indicadores e metas (BRASIL, 2014).
    - citações: BARROS; LIMA, 2017; BRASIL, 2014

- **4.2.3** — *Passo:* Avalia o funil de atrito e os indicadores da cadeia
  - ☐ **[4.2.3.1]** **Funil de atrito e indicadores.** O funil mede, elo a elo, quantos beneficiários potenciais chegam ao fim da cadeia (WHITE; RAITZER, 2017); suas etapas são os indicadores da cadeia, e os de resultado são os *Y* do Quadro 3.
    - citações: WHITE; RAITZER, 2017
  - ☐ **[4.2.3.2]** A Tabela 1 mostra que ele se estreita onde não há dado: entre os 25.441 agentes cadastrados no Mapa Cultural e os 53 a 95 proponentes habilitados por ciclo, não se sabe quantos se inscreveram.
    - checagem de dados: N02 ✔ (`analise/tabelas/07_mapa_cultural_universo.csv`); N44 ✔ (`analise/tabelas/07_composicao_por_ciclo.csv (2022-2026)`)
  - ☐ **[4.2.3.3]** Nas etapas observadas, a maioria passa: 68% dos habilitados de 2022-2024 com situação resolvida captaram.
    - checagem de dados: N04 ✔ (`analise/tabelas/07_funil_por_ciclo.csv`)

### Quadro 2 – Auditoria das premissas da teoria da mudança

- **Colunas:** Elo · Premissa · Contexto real · Situação
  - ☐ **Escolha (H1)** — A escolha pela marca, único retorno privado da empresa, não deixa de fora bem público que a população valorizaria — Duas empresas somam metade da renúncia de 2025; energia e gás, 52%. As peças de divulgação (até 25%) trazem a marca. Recorrentes captam mais (71% contra 57%); 48 pares patrocinador–proponente se repetem (44% do valor) — Não sustentada: evidência mista
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
  - ☐ **[4.2.4.1]** Fonte: elaboração própria, no formato do mecanismo de mapeamento de Williams (2020), com base nas normas do Quadro 1, em SECULT (2026b; 2026c; 2026d), no Portal da Transparência (ESPÍRITO SANTO, 2026) e nas tabelas `03_*.csv`, `07_*.csv`, `09_*.csv`, `10_*.csv`, `14_*.csv` e `16_*.csv` de `analise/tabelas/`.
    - citações: ESPÍRITO SANTO, 2026; Williams (2020)
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
  - ☐ **[4.2.6.5]** O teto por projeto fixa um piso de projetos, ao menos 50 com os R\$ 25 milhões de 2025 (captaram 63), e os pedidos se acumulam nele: 36% dos habilitados do ciclo 2025 pediram exatamente R\$ 500 mil.
    - checagem de dados: N57 ✔ (`analise/tabelas/11_teto_projeto_por_ano.csv`); N58 ✔ (`analise/tabelas/03_bunching_teto.csv`)
  - ☐ **[4.2.6.6]** O acúmulo, porém, também ocorre se quem já tem patrocinador pede o teto.
  - ☐ **[4.2.6.7]** O custo de entrada é o que a literatura chama de custo administrativo (MOYNIHAN; HERD; HARVEY, 2015); ele pode excluir sem selecionar ou funcionar como triagem (FINKELSTEIN; NOTOWIDIGDO, 2019), e só uma variação exógena desse custo distingue os dois casos.
    - citações: MOYNIHAN; HERD; HARVEY, 2015; FINKELSTEIN; NOTOWIDIGDO, 2019

- **4.2.7** — *Passo:* Audita H2: parecer sem nota, papel da comissão, inabilitações, racionamento pela ordem
  - ☐ **[4.2.7.1]** **Decisão concentrada (H2).** O parecer "deverá indicar a habilitação ou inabilitação" (ESPÍRITO SANTO, 2021b, art. 14): para cada critério, o parecerista indica se o projeto "atende ou não" (SECULT, 2026e), e o Mapa Cultural registra só a situação da inscrição (SECULT, 2026d).
    - citações: ESPÍRITO SANTO, 2021b, art. 14; SECULT, 2026e; SECULT, 2026d
  - ☐ **[4.2.7.2]** Nenhuma das normas examinadas prevê nota, peso ou ordem de prioridade; a única pontuação é a do credenciamento dos pareceristas, que recebem os projetos por ordem de inscrição e área (SECULT, 2025c).
    - citações: SECULT, 2025c
  - ☐ **[4.2.7.3]** Desde 2025, o parecer favorável já emite o certificado, e a comissão só delibera sobre inabilitações e, com 35% de patrocínio, sobre a habilitação (SECULT, 2025a, arts. 40, 41 e 45).
    - citações: SECULT, 2025a, arts. 40, 41 e 45
    - ⚠ números sem checagem automática (conferir na fonte citada): 35%
  - ☐ **[4.2.7.4]** Os extratos das atas de 158 reuniões com deliberação, de 2022 a 2026, listam 86 projetos inabilitados, 15% dos deliberados, sem motivo nem critério publicados (SECULT, 2026f).
    - citações: SECULT, 2026f
    - checagem de dados: N60 ✔ (`analise/tabelas/12_cap_deliberacoes.csv`)
  - ☐ **[4.2.7.5]** A habilitação qualifica, mas não prioriza, e o que excedeu o teto em 2023-2025 ficou de fora pelo momento em que o termo chegou e foi validado (SECULT, 2026c).
    - citações: SECULT, 2026c
  - ☐ **[4.2.7.6]** A ordenação seria possível: no Funcultura, a mesma SECULT atribui nota e ordena os projetos por linha e porte do município (SECULT, 2026g).
    - citações: SECULT, 2026g

- **4.2.8** — *Passo:* Audita H1: a marca como retorno privado e o peso de cada empresa pelo imposto
  - ☐ **[4.2.8.1]** **Marketing (H1).** Com crédito integral, a empresa escolhe o destino do ICMS que pagaria e fica com a marca: as peças de comunicação, parte do objeto, trazem a marca do patrocinador em proporção à do Governo, e a divulgação pode consumir até 25% dos recursos (SECULT, 2025a, arts. 23, 55 e 64).
    - citações: SECULT, 2025a, arts. 23, 55 e 64
    - checagem de dados: N54 ✔ (`analise/tabelas/10_rubricas_teto_in.csv (2025)`)
  - ☐ **[4.2.8.2]** Como o limite por patrocinador é uma fração do ICMS recolhido, o peso de cada empresa na escolha cresce com o imposto que ela paga, e a concentração da renúncia (Quadro 2) reflete também a do próprio imposto.
  - ☐ **[4.2.8.3]** Imagem e relações de negócio estão entre os motivos do patrocínio (O'HAGAN; HARVEY, 2000), e a filantropia empresarial também serve de canal de influência política (BERTRAND *et al.*, 2020); a maior patrocinadora de 2025 é uma distribuidora de energia, serviço regulado sob concessão.
    - citações: O'HAGAN; HARVEY, 2000; BERTRAND *et al.*, 2020
  - ☐ **[4.2.8.4]** Com o dado público, marca e valor público não se separam, porque os eventos grandes e antigos são os mais visíveis e os de maior público: a premissa fica não sustentada, com evidência mista.
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
  - ☐ **[4.2.10.3]** O Gini do valor entre os 78 municípios é 0,88, mas quase toda essa desigualdade está dentro de cada região: a diferença entre RMGV e interior explica só 7% do índice de Theil, e é sobre essa parte que age a reserva de 10% para fora da RMGV.
    - checagem de dados: N20 ✔ (`analise/tabelas/03_territorio_indicadores.csv`); N21 ✔ (`analise/tabelas/03_territorio_indicadores.csv`)
    - ⚠ números sem checagem automática (conferir na fonte citada): 10%

- **4.2.11** — *Passo:* Sintetiza a avaliação do desenho e liga à proposta
  - ☐ **[4.2.11.1]** Em síntese, o desenho entrega a escolha a quem recolhe mais imposto e raciona pela ordem de chegada: nenhum elo agrega a preferência de quem usa o bem cultural.
  - ☐ **[4.2.11.2]** O critério público na decisão (H2) não é assegurado pelo desenho, o que não implica que as escolhas sejam ruins; marketing (H1) e exclusão (H4) não se sustentam, com evidência mista; taxa de serviço (H3) e entrega (H5) ficam indeterminadas por falta de dado.
  - ☐ **[4.2.11.3]** A seção 5 trata de H1, H2, H4 e H5 e deixa H3 em aberto.


## 5 Proposta de avaliação de impacto


### 5.1 Perguntas e parâmetros

- **5.1.1** — *Passo:* Converte as premissas em perguntas e define a notação e o viés da comparação simples
  - ☐ **[5.1.1.1]** As premissas do Quadro 2 convertem-se em perguntas de pesquisa: quatro perguntas de avaliação (Quadro 3), na notação de resultados potenciais.
  - ☐ **[5.1.1.2]** Seja *i* a unidade, *T* o tratamento e *Y*(1) e *Y*(0) os resultados com e sem ele.
  - ☐ **[5.1.1.3]** O Quadro 3 mostra também por que a comparação simples entre grupos não responde a nenhuma delas.
  - ☐ **[5.1.1.4]** A diferença simples de médias soma ao efeito médio o viés de seleção, $E[Y(0)\mid T=1]-E[Y(0)\mid T=0]$, e o de efeitos heterogêneos.

### Quadro 3 – Perguntas de avaliação

- **Colunas:** Hipótese · Pergunta · Unidade, tratamento e resultado · Parâmetro · Viés da comparação simples
  - ☐ **H5** — Receber pela LICC muda a realização e o alcance do projeto? — Projeto na margem do teto; *T* = termo validado; *Y* = acontece em janela fixa após o protocolo (agenda, Diário Oficial); público — Efeito de receber agora, na margem; fora dela, efeito médio sobre os tratados (EMPT) — *Y*(0) maior entre os escolhidos pela empresa: viés de seleção positivo
  - ☐ **H1** — O que pesa na escolha da empresa: marca ou valor público? — Decisor de empresa; *T* = atributos sorteados de perfis de projeto; *Y* = escolhe o perfil — Efeito marginal médio de cada atributo — Visibilidade e valor público andam juntos: confundimento
  - ☐ **H4** — Reduzir o custo de entrada muda quem entra? — Agente sem inscrição prévia; *T* = oferta de apoio à inscrição e à busca de patrocínio; *Y* = inscreveu-se, foi habilitado, captou — Efeito da oferta (intenção de tratar) e efeito local para quem responde a ela — Quem se inscreve por conta própria tem mais capacidade: viés de seleção
  - ☐ **H2** — O parecer favorável muda o destino do projeto? — Projeto inscrito; *T* = parecer favorável; *Y* = captou, realizou — Efeito local, se a designação do parecerista for como sorteio; senão, descritivo — Sem nota não há corte; a designação por ordem e área é a variação candidata

- **5.1.2** (fonte do quadro, tabela ou figura)
  - ☐ **[5.1.2.1]** Fonte: elaboração própria, com base em Gertler *et al.* (2018).
    - citações: Gertler *et al.* (2018)


### 5.2 Estratégias de identificação candidatas

- **5.2.1** — *Passo:* Justifica a escolha dos métodos pelas regras de operação
  - ☐ **[5.2.1.1]** As regras de operação determinam o método (GERTLER *et al.*, 2018).
    - citações: GERTLER *et al.*, 2018
  - ☐ **[5.2.1.2]** Com excesso de demanda, ciclos anuais e nenhum índice publicado com ponto de corte, cabem promoção aleatória, experimento com decisores, variáveis instrumentais e diferenças em diferenças.
  - ☐ **[5.2.1.3]** O sorteio mudaria a regra de alocação e fica fora do escopo.

- **5.2.2** — *Passo:* Estratégia para H5: margem do racionamento, reentrada e instrumento
  - ☐ **[5.2.2.1]** **H5.** Os termos validados pouco antes do esgotamento do teto e os de 32 projetos recusados em 2023 e 2024 tinham, todos, patrocinador disposto.
    - checagem de dados: N31 ✔ (`dados/processados/indeferidos_2023_2024.csv`)
  - ☐ **[5.2.2.2]** Mas 6 dos 11 recusados em 2023 e 12 dos 21 recusados em 2024 captaram no ano seguinte: com resultado datado (realização em janela fixa após o protocolo), a comparação estima o efeito de receber agora; para o de receber em algum momento, o indeferimento serve de instrumento, com primeiro estágio de 41% (13 dos 32 recusados não captaram depois).
    - checagem de dados: N30 ✔ (`analise/tabelas/09_reentrada_resumo.csv`); N42 ✔ (`analise/tabelas/09_reentrada_resumo.csv`)
  - ☐ **[5.2.2.3]** As duas leituras valem se a ordem de validação não se ligar ao projeto, o que as datas de protocolo permitem testar.

- **5.2.3** — *Passo:* Estratégia para H1: experimento conjunto com decisores
  - ☐ **[5.2.3.1]** **H1.** Um experimento conjunto separa marca e valor público: decisores de empresas contribuintes escolhem entre pares de perfis de projeto com atributos sorteados (escala, visibilidade, local, gratuidade, público estimado), e o sorteio identifica o efeito marginal médio de cada atributo sobre a escolha (HAINMUELLER; HOPKINS; YAMAMOTO, 2014).
    - citações: HAINMUELLER; HOPKINS; YAMAMOTO, 2014
  - ☐ **[5.2.3.2]** É uma pergunta de mecanismo: aplicados aos habilitados, os pesos estimados indicam o que fica sem patrocínio (o pequeno, o gratuito, o do interior), a confrontar com H4 e H5.

- **5.2.4** — *Passo:* Estratégia para H4: promoção aleatória por município e braços entre agentes
  - ☐ **[5.2.4.1]** **H4.** Uma promoção aleatória de apoio à inscrição e à busca de patrocínio, sorteada entre os 71 municípios do interior, não altera nenhuma regra de alocação; nos municípios sorteados, dois braços, sorteados entre os agentes, separam o atrito documental do de patrocínio.
    - checagem de dados: N72 ✔ (`analise/tabelas/07_mapa_quadro_h3.csv`)
  - ☐ **[5.2.4.2]** A promoção estima o efeito da oferta e, para quem responde a ela, o efeito local (ANGRIST; IMBENS; RUBIN, 1996).
    - citações: ANGRIST; IMBENS; RUBIN, 1996
  - ☐ **[5.2.4.3]** Como o teto é fixo, sortear também a intensidade da oferta mede o deslocamento de outros proponentes (BAIRD *et al.*, 2018), mas, com 71 municípios, só em caráter exploratório.
    - citações: BAIRD *et al.*, 2018
    - ⚠ números sem checagem automática (conferir na fonte citada): 71

- **5.2.5** — *Passo:* Estratégia para H2: severidade do parecerista como instrumento (exploratória)
  - ☐ **[5.2.5.1]** **H2.** Sem nota, não há corte para regressão descontínua, mas os projetos são distribuídos aos pareceristas por ordem de inscrição e área (SECULT, 2025c).
    - citações: SECULT, 2025c
  - ☐ **[5.2.5.2]** Se essa designação se comportar como sorteio dentro de área e período, a severidade do parecerista (a parcela de pareceres favoráveis nos seus outros projetos) é instrumento para o parecer, como o examinador designado em Maestas, Mullen e Strand (2013), sob exclusão e monotonicidade testáveis e com o parecerista de cada inscrição obtido pela Lei de Acesso à Informação (LAI).
    - citações: Mullen e Strand (2013)
  - ☐ **[5.2.5.3]** Como são 41 pareceristas credenciados, de 4 a 20 por área, o instrumento por área é fraco, e o desenho fica exploratório, com áreas afins agrupadas.
    - checagem de dados: N56 ✔ (`analise/tabelas/10_pareceristas_por_area.csv (lista da SECULT de 18/09/2026)`)

- **5.2.6** — *Passo:* Lista os métodos que ficam para depois
  - ☐ **[5.2.6.1]** **O que fica aberto.** Regressão descontínua no tempo (protocolo em torno do esgotamento de cada cota), variáveis instrumentais (recusa pelo teto; severidade do parecerista) e, para H3, diferenças em diferenças com as regras de custo de 2025 e 2026.


### 5.3 Desenho da amostra e fontes de dados

- **5.3.1** — *Passo:* Define populações, listagens e a chave de ligação por CNPJ
  - ☐ **[5.3.1.1]** Para H5 e H2, trabalha-se com o universo, e a listagem vem dos anexos oficiais: 293 projetos habilitados em 2022-2024 com situação resolvida, de 172 proponentes, e os termos de 2023 e 2024 na margem do racionamento.
    - checagem de dados: N22 ✔ (`analise/tabelas/07_poder_hipoteses.csv (nota)`)
  - ☐ **[5.3.1.2]** Para H1, a população principal é quem decide o patrocínio (marketing, diretoria ou relações institucionais): a listagem parte das 26 patrocinadoras de 2025, e os maiores contribuintes fora do Simples Nacional, listados com a SEFAZ, formam uma extensão, com parâmetro possivelmente diferente.
    - checagem de dados: N55 ✔ (`analise/tabelas/03_patrocinadores_concentracao.csv`)
  - ☐ **[5.3.1.3]** Para H4, a listagem é o cadastro de agentes do Mapa Cultural, em que 79% dos coletivos e 78% dos individuais não informam município; com município no interior, há 257 coletivos em 52 municípios e 2.389 agentes, somados os individuais, nos 71.
    - checagem de dados: N38 ✔ (`analise/tabelas/07_mapa_agentes_cobertura.csv`); N39 ✔ (`analise/tabelas/07_mapa_quadro_h3.csv`)
  - ☐ **[5.3.1.4]** A oferta é sorteada entre municípios do interior e chega a todos os agentes cadastrados sem inscrição anterior; quem não está no Mapa fica de fora, um viés de cobertura.
  - ☐ **[5.3.1.5]** A chave de ligação é o CNPJ do proponente: o Portal da Transparência o traz para quem captou (ESPÍRITO SANTO, 2026), e os avisos de habilitação no Diário Oficial, para a maior parte dos demais (DIO-ES, 2026); juntas, cobrem 385 dos 463 habilitados (83%), e o restante e os inabilitados ficam para a LAI (Quadro 4).
    - citações: ESPÍRITO SANTO, 2026; DIO-ES, 2026
    - checagem de dados: N65 ✔ (`analise/tabelas/18_cobertura_cnpj.csv`)

### Quadro 4 – Fontes de dados da avaliação

- **Colunas:** Fonte · Conteúdo · Uso · Acesso
  - ☐ **Inscrições da SECULT (Mapa Cultural)** — Todas as inscrições, inclusive inabilitadas e arquivadas, com linha, área, parecerista, parecer, CNPJ, sede e datas — H2, H4; chave de ligação — Pedido por LAI
  - ☐ **Planilhas de custos** — Rubricas de captação, elaboração, divulgação e remuneração, por projeto — H3 — Pedido por LAI
  - ☐ **Anexos de habilitados e captados; avisos do Diário Oficial; extratos das atas da CAP** — Status, valores e patrocinador; CNPJ e data da habilitação; data de cada depósito (82% dos termos de 2022-2025); inabilitados — H5 (tratamento e intensidade); H2 — Público
    - checagem de dados: N66 ✔ (`analise/tabelas/18_deposito_x_portal.csv`)
  - ☐ **Portal da Transparência (SEFAZ); Receita Federal** — Termos de 2022-2025: data, patrocinador e proponente (CNPJ); pelo CNPJ, porte, idade e sede — Fila (H5); pares e porte (H1, H4) — Público
  - ☐ **SEFAZ** — Hora de protocolo (pública só nos validados de 2025) e de validação dos termos, cota e indeferidos — H5 (racionamento) — Pedido por LAI
  - ☐ **Relatórios de execução** — Lista de presença e estimativa de público (IN 001/2025, art. 66), gratuidade, locais, contrapartidas — *Y* de H5 — Interno
  - ☐ **Mapa Cultural (API)** — Agentes, espaços e agenda de eventos por município — Listagem de H4; eventos datados de 18 projetos (*Y* de H5) — Público
    - checagem de dados: N67 ✔ (`dados/externos/mapa_eventos_licc.csv`)

- **5.3.2** (fonte do quadro, tabela ou figura)
  - ☐ **[5.3.2.1]** Fonte: elaboração própria.


### 5.4 Cálculo do poder estatístico

- **5.4.1** — *Passo:* Apresenta a fórmula do efeito mínimo detectável
  - ☐ **[5.4.1.1]** Para resultados binários, o efeito mínimo detectável (EMD), em pontos percentuais, é:

- ☐ **Fórmula do EMD** (conferir no PDF; parâmetros definidos na frase seguinte)

- **5.4.2** — *Passo:* Define os parâmetros da fórmula
  - ☐ **[5.4.2.1]** A fórmula segue Djimeu e Houndolo (2016), com α = 5% bicaudal e poder de 80%.
    - citações: Djimeu e Houndolo (2016)
    - ⚠ números sem checagem automática (conferir na fonte citada): 5%, 80%
  - ☐ **[5.4.2.2]** Nela, $p_0$ é a proporção no grupo de comparação, $T$ a fração tratada, $n$ o número de unidades, e o último termo é o efeito do desenho com unidades em grupos (agentes de um município, perfis de um decisor), com tamanho médio $\bar m$, coeficiente de variação $cv$ e correlação intragrupo $\rho$ (ELDRIDGE; ASHBY; KERRY, 2006); $p_0$ e $\rho$ são hipóteses a calibrar.
    - citações: ELDRIDGE; ASHBY; KERRY, 2006

### Tabela 2 – Efeito mínimo detectável por pergunta (pontos percentuais)

- **Colunas:** Pergunta e comparação · Unidades · Cenários · EMD
  - ☐ **H1: experimento conjunto** — 30 a 60 decisores × 12 tarefas — $p_0$ = 0,5; ρ = 0 ou 0,1 no decisor — 7,4 a 19,0
    - checagem de dados: N48 ✔ (`analise/tabelas/10_poder_conjoint.csv (30 e 60 × 12)`)
  - ☐ **H5: margem do racionamento, 2023-2024** — 32 recusados × 32 validados — $p_0$ de 0,2 a 0,6 — 28 a 34
    - checagem de dados: N24 ✔ (`analise/tabelas/07_poder_hipoteses.csv`)
  - ☐ **H4: oferta por município, só coletivos** — 52 municípios, 257 coletivos ($\bar m$ = 4,9; *cv* = 1,32) — $p_0$ de 2% a 10%; ρ de 0,02 a 0,05 — 5,5 a 13,4
    - checagem de dados: N25 ✔ (`analise/tabelas/07_poder_hipoteses.csv`)
  - ☐ **H4: oferta por município, todos os agentes** — 71 municípios, 2.389 agentes ($\bar m$ = 33,6; *cv* = 1,43) — $p_0$ de 2% a 10%; ρ de 0,02 a 0,05 — 2,8 a 8,5
    - checagem de dados: N26 ✔ (`analise/tabelas/07_poder_hipoteses.csv`)

- **5.4.3** (fonte do quadro, tabela ou figura)
  - ☐ **[5.4.3.1]** Fonte: elaboração própria; `analise/tabelas/07_poder_hipoteses.csv`, `07_mapa_quadro_h3.csv`, `10_poder_conjoint.csv` e `19_poder_revisao.csv` (scripts `analise/07_hipoteses_h1_h3.py`, `10_poder_mercado_rubricas.py` e `19_poder_revisao.py`).

- **5.4.4** — *Passo:* Interpreta o poder de cada desenho: margem, VI, conjunto, conglomerados e adesão
  - ☐ **[5.4.4.1]** A comparação na margem do racionamento só detecta efeitos muito grandes, acima dos esperados (seção 3), e serve como verificação de robustez; para o efeito de receber em algum momento, o EMD divide-se pelo primeiro estágio (0,41) e vai a 69 a 84 pontos.
    - checagem de dados: N68 ✔ (`analise/tabelas/19_poder_revisao.csv`)
  - ☐ **[5.4.4.2]** Com os recusados de 2025 e 2026 (LAI), se dobrarem a margem, o EMD de receber agora cai para 20 a 24 pontos.
    - checagem de dados: N69 ✔ (`analise/tabelas/19_poder_revisao.csv`)
  - ☐ **[5.4.4.3]** O experimento conjunto detecta diferenças de 7 a 13 pontos na probabilidade de escolha com 60 decisores, e de 10 a 19 com 30.
    - checagem de dados: N49 ✔ (`analise/tabelas/10_poder_conjoint.csv (30 e 60 × 12)`)
  - ☐ **[5.4.4.4]** O desenho de H4 detecta efeitos de poucos pontos se incluir os agentes individuais, que precisariam de CNPJ (MEI) para se inscrever, e só assim atende à regra de 30 a 50 conglomerados por grupo (GERTLER *et al.*, 2018): são 35 ou 36 municípios em cada, e a diferença entre os braços tem EMD de 2,3 a 4,9 pontos.
    - citações: GERTLER *et al.*, 2018
    - checagem de dados: N70 ✔ (`analise/tabelas/19_poder_revisao.csv`)
    - ⚠ números sem checagem automática (conferir na fonte citada): 30, 50
  - ☐ **[5.4.4.5]** Só com os coletivos, são 26 por grupo, e o efeito mínimo passa de 5 pontos.
    - checagem de dados: N40 ✔ (`analise/tabelas/07_poder_hipoteses.csv`); N71 ✔ (`analise/tabelas/07_mapa_quadro_h3.csv`)
  - ☐ **[5.4.4.6]** Para quem adere à oferta, o EMD é o da Tabela 2 dividido pela adesão.
  - ☐ **[5.4.4.7]** Com poder baixo, uma estimativa "significativa" tende a exagerar o efeito verdadeiro (GELMAN; CARLIN, 2014), o que recomenda pré-registrar a análise e corrigir comparações múltiplas.
    - citações: GELMAN; CARLIN, 2014


### 5.5 Ameaças à validade e ética

- **5.5.1** — *Passo:* Lista as ameaças à validade interna e externa e os cuidados éticos
  - ☐ **[5.5.1.1]** A primeira ameaça à validade interna é a violação da hipótese de ausência de interferência entre unidades (SUTVA): com o teto fixo, o que um projeto capta falta a outro.
  - ☐ **[5.5.1.2]** Seguem-se a substituição de fonte (a captação pela Lei Rouanet entra como resultado), os eventos externos do período (Lei Paulo Gustavo e Política Nacional Aldir Blanc) e o atrito dos dados.
  - ☐ **[5.5.1.3]** No experimento conjunto, a escolha declarada pode pender para o socialmente desejável; a escolha forçada entre perfis reduz o viés, e os patrocínios observados servem de validação.
  - ☐ **[5.5.1.4]** A validade externa é limitada: as comparações de H5 valem para o regime de 2022-2024, em que a habilitação precedia a busca por patrocinador, e desde 2025 os expirados quase desapareceram (3 em 56 resolvidos no ciclo 2025).
    - checagem de dados: N27 ✔ (`analise/tabelas/07_funil_por_ciclo.csv`)
  - ☐ **[5.5.1.5]** No plano ético, nenhum desenho nega acesso a elegíveis: o apoio chega aos controles ao fim, e o deslocamento pelo teto é medido pela saturação.
  - ☐ **[5.5.1.6]** Dados identificados exigem anonimização (LGPD), e pesquisas com pessoas, aprovação de comitê de ética.


## 6 Conclusão

- **6.1** — *Passo:* Resume os achados do desenho
  - ☐ **[6.1.1]** A LICC é um gasto tributário que mais que dobrou de 2023 a 2026, sem problema declarado, objetivos mensuráveis ou previsão de avaliação: o Estado paga, as empresas escolhem, e o público que usaria o bem cultural não passa pelo mecanismo.
  - ☐ **[6.1.2]** A escolha se concentra em poucas empresas de serviços regulados, que expõem a marca nas peças do projeto; entre os habilitados, a decisão fica com a empresa e com a fila dos termos; parte do recurso pode remunerar a intermediação; e quem não chega a um grande contribuinte fica de fora.
  - ☐ **[6.1.3]** A entrega, extremo da cadeia, é indeterminada, porque a SECULT não publica o público alcançado.

- **6.2** — *Passo:* Recomenda o que a gestão pode fazer sem mudar o mecanismo
  - ☐ **[6.2.1]** Sem alterar o mecanismo, a gestão pode declarar objetivos, metas e indicadores e publicar, em formato aberto, os inscritos, com CNPJ, sede e motivo de inabilitação; a captação por cota; a fila de termos, com datas de protocolo e validação, também dos recusados; e custos, contrapartidas e público alcançado.

- **6.3** — *Passo:* Retoma a pergunta central (H5), a implicação para o teto e as limitações
  - ☐ **[6.3.1]** Das quatro perguntas, a da entrega (H5) é a mais importante e a mais difícil: mais da metade dos recusados por falta de teto captou no ano seguinte, e comparar quem recebe com quem não recebe exige resultado datado e a fila de termos com as datas.
  - ☐ **[6.3.2]** Se a adicionalidade na margem for baixa, ampliar o teto financia sobretudo o que ocorreria de todo modo, e as decisões que importam passam a ser quem entra e o que se entrega.
  - ☐ **[6.3.3]** Limitações dos dados: a situação publicada aproxima a captação, a estreia é medida por nome de proponente, e o retrato territorial cobre 74% do valor.
    - checagem de dados: D33 ✔ (`analise/tabelas/03_territorio_indicadores.csv`); N28 ✔ (`analise/tabelas/03_territorio_indicadores.csv (cobertura_valor_atribuivel = 0.741)`)


## Referências

Status da última conferência (`artigo/auditoria/checagem_referencias.csv`): VERIFIED = DOI conferido na Crossref sem divergência; sem_doi = referência sem DOI (norma, página oficial, livro), conferida na fonte indicada.

- ☐ ANGRIST, Joshua D.; IMBENS, Guido W.; RUBIN, Donald B. Identification of causal effects using instrumental variables. **Journal of the American Statistical Association**, v. 91, n. 434, p. 444-455, 1996. DOI: 10.1080/01621459.1996.10476902.
  - conferência: VERIFIED
- ☐ BAIRD, Sarah; BOHREN, J. Aislinn; McINTOSH, Craig; ÖZLER, Berk. Optimal design of experiments in the presence of interference. **The Review of Economics and Statistics**, v. 100, n. 5, p. 844-860, 2018. DOI: 10.1162/rest_a_00716.
  - conferência: VERIFIED
- ☐ BARROS, Ricardo Paes de; LIMA, Lycia. Avaliação de impacto de programas sociais: por que, para que e quando fazer? *In*: MENEZES FILHO, Naercio Aquino; PINTO, Cristine Campos de Xavier (org.). **Avaliação econômica de projetos sociais**. 3. ed. São Paulo: Fundação Itaú Social, 2017. p. 13-37.
  - conferência: sem_doi
- ☐ BAUMOL, William J.; BOWEN, William G. **Performing arts**: the economic dilemma. New York: The Twentieth Century Fund, 1966.
  - conferência: sem_doi
- ☐ BELEM, Marcela Purini; DONADONE, Julio Cesar. A Lei Rouanet e a construção do "mercado de patrocínios culturais". **NORUS – Novos Rumos Sociológicos**, Pelotas, v. 1, n. 1, 2013. Disponível em: https://periodicos.ufpel.edu.br/index.php/NORUS/article/view/2761.
  - conferência: sem_doi
- ☐ BERTRAND, Marianne; BOMBARDINI, Matilde; FISMAN, Raymond; TREBBI, Francesco. Tax-exempt lobbying: corporate philanthropy as a tool for political influence. **American Economic Review**, v. 110, n. 7, p. 2065-2102, 2020. DOI: 10.1257/aer.20180615.
  - conferência: VERIFIED
- ☐ BRASIL. Lei Complementar nº 123, de 14 de dezembro de 2006. Institui o Estatuto Nacional da Microempresa e da Empresa de Pequeno Porte. **Diário Oficial da União**, Brasília, 15 dez. 2006. Disponível em: https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp123.htm. Acesso em: 27 set. 2026.
  - conferência: sem_doi
- ☐ BRASIL. Tribunal de Contas da União. **Acórdão nº 1.205/2014 – Plenário**. Relator: Raimundo Carreiro. Brasília, 14 maio 2014.
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
- ☐ DIO-ES – DEPARTAMENTO DE IMPRENSA OFICIAL DO ESPÍRITO SANTO. **Diário Oficial dos Poderes do Estado**: avisos de habilitação e de depósito da LICC, 2022-2026. Vitória: DIO-ES, 2026. Disponível em: https://ioes.dio.es.gov.br. Acesso em: 27 set. 2026.
  - conferência: sem_doi
- ☐ DJIMEU, Eric W.; HOUNDOLO, Deo-Gracias. Power calculation for causal inference in social science: sample size and minimum detectable effect determination. **Journal of Development Effectiveness**, v. 8, n. 4, p. 508-527, 2016. DOI: 10.1080/19439342.2016.1244555.
  - conferência: VERIFIED
- ☐ ELDRIDGE, Sandra M.; ASHBY, Deborah; KERRY, Sally. Sample size for cluster randomized trials: effect of coefficient of variation of cluster size and analysis method. **International Journal of Epidemiology**, v. 35, n. 5, p. 1292-1300, 2006. DOI: 10.1093/ije/dyl129.
  - conferência: VERIFIED
- ☐ ESPÍRITO SANTO (Estado). Lei nº 11.246, de 7 de abril de 2021. Introduz alterações na Lei nº 7.000, de 27 de dezembro de 2001. **Diário Oficial dos Poderes do Estado**, Vitória, 8 abr. 2021a.
  - conferência: sem_doi
- ☐ ESPÍRITO SANTO (Estado). Decreto nº 5.035-R, de 15 de dezembro de 2021. Dispõe sobre a regulamentação do incentivo fiscal concedido nos termos do art. 5º-B, IX, da Lei nº 7.000, de 27 de dezembro de 2001. **Diário Oficial dos Poderes do Estado**, Vitória, 16 dez. 2021b.
  - conferência: sem_doi
- ☐ ESPÍRITO SANTO (Estado). **Portal da Transparência**: incentivos, isenções e beneficiários. Vitória: SECONT, 2026. Disponível em: https://transparencia.es.gov.br/comum/incentivosfiscais. Acesso em: 27 set. 2026.
  - conferência: sem_doi
- ☐ FELD, Alan L.; O'HARE, Michael; SCHUSTER, J. Mark Davidson. **Patrons despite themselves**: taxpayers and arts policy. New York: New York University Press, 1983.
  - conferência: sem_doi
- ☐ FINKELSTEIN, Amy; NOTOWIDIGDO, Matthew J. Take-up and targeting: experimental evidence from SNAP. **The Quarterly Journal of Economics**, v. 134, n. 3, p. 1505-1556, 2019. DOI: 10.1093/qje/qjz013.
  - conferência: VERIFIED
- ☐ GELMAN, Andrew; CARLIN, John. Beyond power calculations: assessing type S (sign) and type M (magnitude) errors. **Perspectives on Psychological Science**, v. 9, n. 6, p. 641-651, 2014. DOI: 10.1177/1745691614551642.
  - conferência: VERIFIED
- ☐ GERTLER, Paul J.; MARTÍNEZ, Sebastián; PREMAND, Patrick; RAWLINGS, Laura B.; VERMEERSCH, Christel M. J. **Avaliação de impacto na prática**. 2. ed. Washington, DC: Banco Interamericano de Desenvolvimento; Banco Mundial, 2018.
  - conferência: sem_doi
- ☐ HAINMUELLER, Jens; HOPKINS, Daniel J.; YAMAMOTO, Teppei. Causal inference in conjoint analysis: understanding multidimensional choices via stated preference experiments. **Political Analysis**, v. 22, n. 1, p. 1-30, 2014. DOI: 10.1093/pan/mpt024.
  - conferência: VERIFIED
- ☐ HITZIG, Zoë. What are public goods and how do they link people in a society? **EXPeditions**, 13 set. 2021. Disponível em: https://www.joinexpeditions.com/exps/332-what-are-public-goods-and-how-do-they-link-people-in-a-society-. Acesso em: 27 set. 2026.
  - conferência: sem_doi
- ☐ IBGE. **Sistema de Informações e Indicadores Culturais**. Rio de Janeiro: IBGE, 2025. Base de dados; períodos 2023 e 2024 publicados em 12 dez. 2025. Disponível em: https://servicodados.ibge.gov.br/api/v1/pesquisas/10092. Acesso em: 23 set. 2026.
  - conferência: sem_doi
- ☐ IBGE. **Pesquisa de Informações Básicas Municipais – MUNIC 2021**. Rio de Janeiro: IBGE, 2022. Dados consultados pela API de pesquisas do IBGE em 23 set. 2026.
  - conferência: sem_doi
- ☐ MAESTAS, Nicole; MULLEN, Kathleen J.; STRAND, Alexander. Does disability insurance receipt discourage work? Using examiner assignment to estimate causal effects of SSDI receipt. **American Economic Review**, v. 103, n. 5, p. 1797-1829, 2013. DOI: 10.1257/aer.103.5.1797.
  - conferência: VERIFIED
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
- ☐ THOM, Michael. Lights, camera, but no action? Tax and economic development lessons from state motion picture incentive programs. **The American Review of Public Administration**, v. 48, n. 1, p. 33-51, 2018. DOI: 10.1177/0275074016651958.
  - conferência: VERIFIED
- ☐ THROSBY, David. The production and consumption of the arts: a view of cultural economics. **Journal of Economic Literature**, v. 32, n. 1, p. 1-29, 1994.
  - conferência: sem_doi
- ☐ WHITE, Howard; RAITZER, David A. **Impact evaluation of development interventions**: a practical guide. Mandaluyong City: Asian Development Bank, 2017. DOI: 10.22617/TCS179188-2.
  - conferência: VERIFIED
- ☐ WILLIAMS, Martin J. External validity and policy adaptation: from impact evaluation to policy design. **The World Bank Research Observer**, v. 35, n. 2, p. 158-191, 2020. DOI: 10.1093/wbro/lky010.
  - conferência: VERIFIED

## Números a conferir à mão

191 frases e linhas de tabela; 50 com checagem automática de dados. Abaixo, as que têm números sem checagem automática (a maioria é regra de norma; conferir na fonte citada):

### Dado ou literatura (14)

- ☐ [1.1.3]: 25, 63
- ☐ [1.2.2]: 27
- ☐ [3.1.4]: 100%
- ☐ [3.2.4]: 853
- ☐ linha «Escolha (H1)»: 25%
- ☐ linha «Entrega (H5)»: 30%
- ☐ [4.2.4.1]: 2026
- ☐ [4.2.5.1]: 2026
- ☐ [4.2.6.4]: 400
- ☐ [4.2.10.1]: 30%
- ☐ [4.2.10.3]: 10%
- ☐ [5.2.4.3]: 71
- ☐ [5.4.2.1]: 5%, 80%
- ☐ [5.4.4.4]: 30, 50

### Regra de norma (11)

- ☐ [2.1.4]: 100%
- ☐ linha «Benefício ao patrocinador»: 100%
- ☐ linha «Teto anual»: 31, 01, 2%, 10, 15, 25
- ☐ linha «Patrocinador»: 20%, 15%, 10%, 5%
- ☐ linha «Proponentes»: 2, 3
- ☐ linha «Linhas e limite por projeto»: 1, 300, 001
- ☐ linha «Alocação entre habilitados»: 30%, 10, 10%, 50%
- ☐ linha «Custos com o recurso incentivado»: 10%, 15, 25%
- ☐ [4.2.7.3]: 35%
- ☐ [4.2.9.2]: 1, 3
- ☐ [4.2.9.4]: 10%

