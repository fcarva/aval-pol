# Revisão de literatura brasileira: incentivo fiscal à cultura

> Bibliografia anotada (skill deep-research, modo `lit-review`: bibliografia + verificação + síntese).
> Objetivo: sustentar a seção "breve revisão da literatura" do mini artigo sobre a LICC (Lei ES 11.246/2021).
> Regra: só entram referências cuja existência foi CONFIRMADA (DOI resolvido em Crossref/OpenAlex, ou URL estável
> de repositório/periódico/órgão). Onde algo não pôde ser confirmado: `[VERIFICAR]` com explicação.
> Status: EM CONSTRUÇÃO (gravação incremental).

## 0. Protocolo de busca

- **Data das buscas:** 23/09/2026.
- **Bases e canais:** OpenAlex API (`/works?search=`, `filter=title.search:` e `title_and_abstract.search:`, `filter=author.id:` para os autores listados na tarefa); Crossref API (`/works/{doi}`) para conferir DOI, autores, volume, páginas; páginas de periódicos (OJS/SciELO), TCU, FGV, IPEA e repositórios, lidas com WebFetch/firecrawl; WebSearch para localizar relatórios institucionais e livros sem DOI. Scripts de consulta ficaram no scratchpad da sessão (não fazem parte do projeto).
- **Termos (pt/en):** "Lei Rouanet", "incentivo fiscal à cultura", "renúncia fiscal cultura", "mecenato", "patrocínio cultural marketing", "ProAC", "Fazcultura", "Pró-Cultura", "Lei Mendonça", "Lei Rubem Braga", "Funcultura", "ICMS cultura", "Lei Aldir Blanc", "Lei Paulo Gustavo", "Sistema Nacional de Cultura federalismo", "Rouanet law", "cultural tax incentives Brazil", "espírito santo política cultural", "capixaba cultura incentivo".
- **Autores checados (OpenAlex author.id):** Olivieri, Botelho, Rubim, Calabre, Barbalho, Valiati, Silva (Frederico A. Barbosa da), Sarkovas, Belem, Ortellado. Donadone e Lima entraram via os trabalhos em coautoria.
- **Critério de verificação:** uma referência só entra se ao menos uma destas fontes a confirmou: (a) DOI resolvido na Crossref, com título conferido; (b) registro no OpenAlex com URL da página do periódico; (c) página oficial do órgão ou editora (TCU, FGV, IPEA, editora universitária). A etiqueta `[VERIFICADO: ...]` diz qual foi. A linha **Base** diz o que foi de fato lido: *resumo* (abstract no OpenAlex/Crossref/página do periódico), *página* (página institucional ou sumário) ou *texto* (texto completo). O que está anotado não vai além do que a base lida permite dizer.
- **Nível de evidência:** hierarquia de `references/source_quality_hierarchy.md` do skill deep-research (I = revisão sistemática ... VI = estudo descritivo/qualitativo único; VII = opinião de especialista ou relatório de comitê). Em política cultural brasileira quase tudo é nível VI ou VII. Isso é um achado da revisão, não descuido da seleção (ver §8).
- **Limites:** não houve busca sistemática (PRISMA) nem avaliação formal de risco de viés; o Google Acadêmico não tem API e foi coberto só indiretamente, via WebSearch. Teses e dissertações sem DOI só entram quando localizadas em repositório institucional com URL estável.

## 1. Lei Rouanet / mecenato federal: concentração, lógica de marketing, "dinheiro público com decisão privada"

**Contexto para ler a seção.** A LICC reproduz o núcleo do desenho do mecenato da Rouanet. O Estado credencia projetos; um contribuinte (empresa) escolhe qual deles patrocinar; o valor destinado volta à empresa como crédito presumido de ICMS (Lei ES 7.000/2001, art. 5º-B, IX, na redação da Lei 11.246/2021; texto em `notas/politica/fontes/lei-11246-2021.md`). Por isso, a literatura crítica da Rouanet é o análogo mais próximo que existe para formar hipóteses sobre a LICC. A transposição tem um limite: a Rouanet deduz Imposto de Renda de empresas de lucro real em escala nacional, e a LICC compensa ICMS dentro de um só estado, com teto anual fixo e cotas.

**1.1 DURAND, José Carlos Garcia; GOUVEIA, Maria Alice; BERMAN, Graça. Patrocínio empresarial e incentivos fiscais à cultura no Brasil: análise de uma experiência recente. *Revista de Administração de Empresas*, São Paulo, v. 37, n. 4, p. 38-44, 1997.** DOI: https://doi.org/10.1590/S0034-75901997000400005. [VERIFICADO: Crossref DOI; SciELO]
- *Base:* resumo. *Nível:* VI (levantamento descritivo junto a gestores).
- *Método e achados:* primeiro balanço comparado das leis federal, estaduais e municipais de incentivo fiscal à cultura nos anos 1990, feito com levantamento junto às autoridades culturais e com dados numéricos até 1995. Compara as leis pela agilidade de operação, pela atratividade para empresários e pela prevenção de fraudes.
- *Implicação para a LICC:* mostra que o desenho estadual via ICMS é uma família de instrumentos com trinta anos de história. A LICC pode ser caracterizada nessas mesmas dimensões (agilidade, atratividade, controle), que servem de grade para a seção "caracterização da política".

**1.2 ARRUDA, Maria Arminda do Nascimento. A política cultural: regulação estatal e mecenato privado. *Tempo Social*, São Paulo, v. 15, n. 2, 2003.** DOI: https://doi.org/10.1590/S0103-20702003000200007. [VERIFICADO: Crossref DOI; SciELO] (a Crossref não informa páginas)
- *Base:* resumo. *Nível:* VI (análise sociológica e documental).
- *Método e achados:* analisa a política cultural do segundo governo FHC. Nela o Estado passa a ser intermediário que avaliza relações entre produtores e agentes econômicos, e não se trata de um mecenato privado típico. A autora conclui que a expansão das iniciativas não significou, necessariamente, renovação das linguagens.
- *Implicação para a LICC:* dá o conceito para a teoria da mudança. A LICC não é mecenato, é gasto público com intermediação privada. Resultado de "mais projetos" não equivale a resultado de "mais diversidade ou inovação".

**1.3 OLIVIERI, Cristiane Garcia. *Cultura neoliberal: leis de incentivo como política pública de cultura*. São Paulo: Escrituras; Instituto Pensarte, 2004. (Coleção Visões da Cultura).** [VERIFICADO: registro editorial em livrarias (Fnac) e nota do GIFE sobre o lançamento, localizados por WebSearch; sem DOI] `[VERIFICAR: cidade, paginação e ISBN no catálogo da Biblioteca Nacional ou da USP antes de citar no artigo]`
- *Base:* página de divulgação (o livro não foi lido). *Nível:* VII/VI.
- *Achados (segundo a divulgação):* distingue política cultural, apoio e patrocínio, e faz balanço crítico dos resultados das leis de incentivo e de seus impactos no setor cultural.
- *Implicação para a LICC:* é referência clássica para o argumento "dinheiro público, decisão privada". Só deve ser citada depois de conferida no original.

**1.4 SARKOVAS, Yacoff. O incentivo fiscal no Brasil. *Teoria e Debate*, São Paulo, n. 62, maio 2005.** URL: https://fpabramo.org.br/2005/05/18/o-incentivo-fiscal-no-brasil/. [VERIFICADO: página da Fundação Perseu Abramo, arquivo da revista; texto lido]
- *Base:* texto. *Nível:* VII (ensaio de consultor de patrocínio).
- *Argumento:* o autor, consultor de patrocínio empresarial, sustenta que a dedução integral (100% na Rouanet alterada; mais de 100% na Lei do Audiovisual) converte o incentivo em repasse de dinheiro público para aplicação decidida pela empresa, sem contrapartida privada real e na prática financiando marketing empresarial com o erário.
- *Implicação para a LICC:* o crédito presumido da LICC corresponde ao valor destinado, portanto também sem contrapartida financeira da empresa. O argumento se aplica diretamente e vem de alguém do próprio mercado de patrocínio, o que o torna útil no artigo como crítica "de dentro".

**1.5 BELEM, Marcela Purini; DONADONE, Julio Cesar. A Lei Rouanet e a construção do "mercado de patrocínios culturais". *NORUS – Novos Rumos Sociológicos*, Pelotas, v. 1, n. 1, 2013.** DOI declarado: 10.15210/norus.v1i1.2761 (não resolve na Crossref: HTTP 404). URL estável: https://periodicos.ufpel.edu.br/index.php/NORUS/article/view/2761. [VERIFICADO: OpenAlex W1537615740 + página do periódico UFPel]
- *Base:* resumo. *Nível:* VI (sociologia econômica, análise histórico-institucional).
- *Método e achados:* com teorias da sociologia econômica e dos mercados, mostra que a Rouanet criou um "mercado de patrocínios culturais", com intermediários, captadores e departamentos de marketing. O argumento central é que a regulação estatal da lei é condição da existência desse mercado.
- *Implicação para a LICC:* a teoria da mudança da LICC precisa incluir o elo de intermediação (captação e contato com patrocinador). O acesso a esse mercado, e não o mérito cultural, pode ser o gargalo que decide quem capta. Isso é coerente com a LICC habilitar mais do que o teto e deixar a disputa por patrocinador decidir (ver `licc-gov/CLAUDE-licc.md`).

**1.6 LOPES, Rafaela Araújo; BARREIROS, Bruno Costa. Folha de S.Paulo, Lei Rouanet e o mercado de patrocínios culturais incentivados. *Estudos de Sociologia*, Araraquara, v. 30, n. 3, p. 1123-1150, 2025.** DOI: https://doi.org/10.52780/res.v30i3.20239. [VERIFICADO: Crossref DOI] (v. 30, n. 3 conforme o DOI; a Crossref não traz volume)
- *Base:* resumo. *Nível:* VI (análise de discurso de 863 matérias da Folha de S.Paulo, 2013-2023).
- *Achados:* o mercado de patrocínios incentivados sobreviveu aos ataques simbólicos à Rouanet (agenda conservadora) e renovou sua legitimidade com o discurso da sustentabilidade e da economia criativa.
- *Implicação para a LICC:* a legitimação do incentivo passa pelo discurso do retorno econômico ("cada R$ 1 gera R$ X"). Uma avaliação de impacto da LICC deve separar esse argumento, que é de multiplicador, do efeito causal.

**1.7 COSTA, Camila Furlan da; MEDEIROS, Igor Baptista de Oliveira; BUCCO, Guilherme Brandelli. O financiamento da cultura no Brasil no período 2003-15: um caminho para geração de renda monopolista. *Revista de Administração Pública*, Rio de Janeiro, v. 51, n. 4, p. 509-527, 2017.** DOI: https://doi.org/10.1590/0034-7612162254. [VERIFICADO: Crossref DOI; SciELO]
- *Base:* resumo. *Nível:* VI (estudo longitudinal quantitativo descritivo dos projetos aprovados pelo MinC de 2003 a 2015).
- *Achados:* mesmo com a mudança na concepção de cultura nos governos do período, persiste a concentração de incentivadores e de proponentes. A política continua transferindo ao mercado a decisão sobre o que é financiado, e o recurso público favorece projetos de interesse da imagem corporativa sob controle de poucas produtoras e fundações ("renda monopolista").
- *Implicação para a LICC:* motiva medir a concentração por proponente e por patrocinador (HHI, participação dos maiores) como indicador de resultado intermediário. Os dados de `captados-2025.csv` (patrocinador e aportes por CNPJ) permitem fazer isso para 2025.

**1.8 DEKKER, Erwin; RODRIGUES, Ana Carolina. The political economy of Brazilian cultural policy: a case study of the Rouanet Law. *Journal of Public Finance and Public Choice*, Bristol, v. 34, n. 2, p. 149-171, 2019.** DOI: https://doi.org/10.1332/251569119X15675896589688. [VERIFICADO: Crossref DOI] Versão de trabalho: SSRN, DOI 10.2139/ssrn.3313990.
- *Base:* resumo. *Nível:* VI (análise descritiva de 1993 a 2016 com enquadramento de economia política; o primeiro autor é da Universidade Erasmus, e o estudo entra aqui por tratar do Brasil).
- *Achados:* a lei agravou desigualdades socioeconômicas, regionais e entre linguagens artísticas. Os recursos foram predominantemente para projetos já bem-sucedidos, às vezes já lucrativos, e vieram sobretudo de grandes empresas, muitas com participação estatal, funcionando como corte de imposto para elas. Não fica claro que alguma falha de mercado específica seja corrigida.
- *Implicação para a LICC:* obriga a teoria da mudança a nomear **qual falha de mercado** a LICC corrige (bem público, externalidade, restrição de crédito de pequenos produtores). Obriga também a avaliação a testar **adicionalidade**: o projeto aconteceria sem o incentivo? No desenho de impacto, a pergunta vira comparar projetos habilitados que captaram com habilitados que não captaram.

**1.9 SANTOS, Eduardo Gomor dos; PAULO, Carla Beatriz de. Gastos tributários e recursos orçamentários nas políticas culturais. *Revista de Políticas Públicas*, São Luís, v. 18, n. 1, p. 111-124, 2014.** DOI: https://doi.org/10.18764/2178-2865.v18n1p111-124. [VERIFICADO: Crossref DOI]
- *Base:* resumo. *Nível:* VI (análise documental e orçamentária).
- *Achados:* o mecenato movimenta por ano valores próximos ao orçamento do próprio Ministério da Cultura. As leis de incentivo perdem em controle democrático, reproduzem desigualdades regionais (concentração em SP e RJ) e servem de instrumento de marketing para grandes corporações. O Cultura Viva distribui de forma mais equitativa, mas com orçamento "irrisório" em comparação.
- *Implicação para a LICC:* propõe a comparação certa para o artigo, entre gasto tributário (LICC) e gasto direto (Funcultura/editais), e chama atenção para medir o tamanho relativo dos dois no orçamento da SECULT-ES.

**1.10 GUIMARÃES, Bruno Costa. Concentração cultural: por que podemos dizer que, no Brasil, o investimento na cultura está mais concentrado que o PIB? *Mediações – Revista de Ciências Sociais*, Londrina, v. 25, n. 2, p. 412-, 2020.** DOI: https://doi.org/10.5433/2176-6665.2020v25n2p412. [VERIFICADO: Crossref DOI] `[VERIFICAR: página final]`
- *Base:* resumo. *Nível:* VI (descritivo).
- *Achados:* argumenta que a captação da Rouanet é mais concentrada territorialmente (Rio e São Paulo) do que o próprio PIB, por efeito da lógica mercantil da lei.
- *Implicação para a LICC:* sugere um indicador simples e replicável para o ES: comparar a participação dos municípios na captação com a participação no PIB, no ICMS ou na população, e não só medir a concentração absoluta. Os dados do IBGE (PIB municipal) estão acessíveis por API.

**1.11 TEIXEIRA, Lusvânio Carlos; XAVIER, Wescley Silva; FARIA, Evandro Rodrigues de. Distribuição geográfica de projetos culturais com captação de recursos via Lei Rouanet. *DRd – Desenvolvimento Regional em Debate*, Canoinhas, v. 14, p. 556-578, 2024.** DOI: https://doi.org/10.24302/drd.v14.5320. [VERIFICADO: Crossref DOI]
- *Base:* resumo. *Nível:* VI/IV (descritivo mais comparação entre grupos de municípios com testes de Kolmogorov-Smirnov e Mann-Whitney).
- *Achados:* há concentração dos recursos no Sudeste. Os municípios com projetos captados têm maior população e maior PIB do que os que não têm. Os autores concluem que a lei tem dificuldade de desconcentrar geograficamente e atende mais a interesses de mercado.
- *Implicação para a LICC:* dá precedente metodológico direto para o descritivo municipal da LICC (78 municípios do ES): comparar municípios com e sem projeto captado por porte e PIB. Também antecipa o viés de seleção que qualquer desenho de impacto no nível municipal terá de enfrentar.

**1.12 EARP, Fabio de Silos Sá; ESTRELLA, Luiz Manoel. Evolução do mecenato no Brasil: os valores movimentados através da Lei Rouanet despidos do véu da inflação (1996-2014). *Políticas Culturais em Revista*, Salvador, v. 9, n. 1, p. 315-, 2016.** DOI: https://doi.org/10.9771/pcr.v9i1.15208. [VERIFICADO: Crossref DOI] `[VERIFICAR: página final]`
- *Base:* resumo. *Nível:* VI (séries descritivas).
- *Achados:* reconstrói em valores reais as séries do mecenato de 1996 a 2014 e critica as comparações "espúrias" entre valores nominais, frequentes na área.
- *Implicação para a LICC:* é uma regra prática para o artigo. Toda série da LICC (tetos de R$ de 2022 a 2026) deve ser deflacionada (IPCA) antes de comparar anos, e o índice usado deve ser declarado.

**1.13 FICHEIRA, Carolina Marques Henriques; BUARQUE DE HOLLANDA, Heloisa Helena Oliveira. Política cultural por meio do incentivo fiscal, 26 anos de caminhada: retrato da captação global e setorial no campo das humanidades. *Políticas Culturais em Revista*, Salvador, v. 11, n. 1, p. 255-277, 2019.** DOI: https://doi.org/10.9771/pcr.v11i1.25343. [VERIFICADO: Crossref DOI]
- *Base:* resumo. *Nível:* VI.
- *Achados:* compila todos os valores captados pela Rouanet de 1993 a 17/08/2017, por região e por produto, com foco nas humanidades, a partir da experiência de parecerista.
- *Implicação para a LICC:* confirma que o SALIC permite séries longas por região e segmento. A LICC **não publica segmento** (ver `licc-gov/CLAUDE-licc.md`: segmento com 0% de cobertura), o que limita a replicação da análise setorial no ES.

**1.14 MICHETTI, Miqueli. A definição privada do bem público: a atuação de institutos empresariais na esfera da cultura. *Caderno CRH*, Salvador, v. 29, n. 78, p. 513-534, 2016.** DOI: https://doi.org/10.1590/S0103-49792016000300007. [VERIFICADO: Crossref DOI; SciELO]
- *Base:* resumo. *Nível:* VI (revisão bibliográfica, dados quali-quantitativos sobre uso de renúncia e análise de discurso).
- *Achados:* institutos e fundações empresariais, viabilizados pelas leis de incentivo, convertem capital econômico em poder político e definem privadamente o que é bem público. A autora reabre o debate sobre a legitimidade democrática desse arranjo.
- *Implicação para a LICC:* recomenda verificar se há proponentes ligados a patrocinadores (institutos da própria empresa). O Decreto 5.035-R/2021, art. 10, § 3º, veda o uso do incentivo em projetos em que seja beneficiária a própria empresa patrocinadora, seus proprietários, sócios ou diretores e parentes até terceiro grau (`notas/politica/fontes/decreto-5035-r-2021.md`, l. 80). Pelo texto transcrito, a vedação não alcança expressamente institutos ou fundações mantidos pela patrocinadora. Esse é justamente o canal descrito por Michetti, e pode ser um ponto do desenho a discutir (`[VERIFICAR]` se alguma IN posterior tratou do caso).

**1.15 PIMENTEL, Cacia Campos. A qualidade do gasto tributário e a utilização das políticas de renúncia fiscal na cultura. *REI – Revista Estudos Institucionais*, Rio de Janeiro, v. 5, n. 2, p. 486-507, 2019.** DOI: https://doi.org/10.21783/rei.v5i2.314. [VERIFICADO: Crossref DOI]
- *Base:* resumo. *Nível:* VI/VII (análise jurídico-econômica com dados de prestação de contas da Rouanet).
- *Achados:* com base nas prestações de contas da Rouanet, conclui que os objetivos constitucionais da renúncia não estão sendo alcançados. Recomenda tratar a renúncia como mecanismo excepcional e temporário, integrado ao orçamento e sujeito a avaliação.
- *Implicação para a LICC:* sustenta a pergunta de avaliação *ex post* e a recomendação de que a SECULT-ES publique dados de execução e prestação de contas, hoje ausentes dos anexos (só há valor autorizado e captado).

**1.16 LIMA, Luciana; ORTELLADO, Pablo. Da compra de produtos e serviços culturais ao direito de produzir cultura: análise de um paradigma emergente. *Dados*, Rio de Janeiro, v. 56, n. 2, p. 351-382, 2013.** DOI: https://doi.org/10.1590/S0011-52582013000200004. [VERIFICADO: Crossref DOI; SciELO]
- *Base:* resumo. *Nível:* VI/VII (revisão teórica e análise de duas políticas: Cultura Viva e Lei de Fomento ao Teatro de SP).
- *Argumento:* distingue três paradigmas de financiamento: público direto; mercantil, que inclui incentivo fiscal e a economia criativa; e um terceiro, emergente, que financia o *processo* de produção cultural como direito social. Sistematiza os argumentos e críticas de cada um.
- *Implicação para a LICC:* dá o quadro conceitual da seção de revisão. A LICC fica no paradigma mercantil-incentivado, e a Lei Aldir Blanc e a Lei Paulo Gustavo (§7) mais perto do público direto descentralizado. É o texto certo para explicar por que "democratizar a produção" não é objetivo natural de um instrumento de incentivo.

**1.17 BOTELHO, Isaura. Dimensões da cultura e políticas públicas. *São Paulo em Perspectiva*, São Paulo, v. 15, n. 2, p. 73-83, 2001.** DOI: https://doi.org/10.1590/S0102-88392001000200011. [VERIFICADO: Crossref DOI; SciELO; OpenAlex, 83 citações]
- *Base:* resumo e metadados. *Nível:* VII (ensaio conceitual muito citado).
- *Argumento (conhecido e confirmado no resumo):* distingue a dimensão antropológica da cultura (cotidiano, modos de vida) da dimensão sociológica (produção especializada, circuito artístico) e mostra que as políticas públicas, inclusive as de incentivo, alcançam sobretudo a segunda.
- *Implicação para a LICC:* ajuda a delimitar o resultado esperado da LICC (oferta de bens e eventos culturais especializados). "Acesso à cultura" em sentido amplo não é resultado plausível de um instrumento de patrocínio de projetos.

**1.18 RUBIM, Antonio Albino Canelas. Políticas culturais no Brasil: tristes tradições. *Galáxia*, São Paulo, n. 13, p. 101-113, 2007.** URL: https://revistas.pucsp.br/index.php/galaxia/article/view/1469. [VERIFICADO: página do periódico PUC-SP] Versão ampliada: RUBIM, A. A. C. Políticas culturais no Brasil: tristes tradições, enormes desafios. In: RUBIM, A. A. C.; BARBALHO, A. (org.). *Políticas culturais no Brasil*. Salvador: EDUFBA, 2007. p. 11-36. `[VERIFICAR: páginas do capítulo no exemplar da EDUFBA; o repositório da UFBA recusou o certificado TLS no acesso]`
- *Base:* resumo. *Nível:* VII (revisão histórica).
- *Argumento:* as políticas culturais federais têm três "tristes tradições" (ausência, autoritarismo e instabilidade). A hegemonia das leis de incentivo nos anos 1990 aparece como forma de ausência do Estado na decisão.
- *Implicação para a LICC:* é a moldura histórica para a introdução do artigo. A pergunta é se a LICC repete a "ausência" (decisão delegada) ou se as cotas do art. 18 da IN 001/2025 são uma tentativa de o Estado recuperar capacidade de direcionamento.

**1.19 CALABRE, Lia. *Políticas culturais no Brasil: dos anos 1930 ao século XXI*. Rio de Janeiro: Editora FGV, 2009. (FGV de Bolso, Série Sociedade & Cultura).** URL: https://editora.fgv.br/produto/politicas-culturais-no-brasil-dos-anos-1930-ao-seculo-xxi-2247. [VERIFICADO: página da Editora FGV] `[VERIFICAR: número de páginas e ISBN]`
- *Base:* página da editora. *Nível:* VII (síntese histórica).
- *Conteúdo:* trajetória das ações públicas de cultura desde os anos 1930 até a institucionalização da cultura em estados e municípios no século XXI.
- *Implicação para a LICC:* referência de contexto para situar as leis estaduais, entre elas a do ES, na onda de municipalização e estadualização da política cultural.

**1.20 SILVA, Sara R. de Andrade. Corporate sponsorship as cultural policy: tax incentives in Brazilian contemporary art. *International Journal of Cultural Policy*, v. 32, n. 3, p. 359-376, 2026 (online 2025).** DOI: https://doi.org/10.1080/10286632.2025.2454580. [VERIFICADO: Crossref DOI]
- *Base:* resumo. *Nível:* VI (dados de uma década de financiamento cultural, com processamento de linguagem natural e aprendizado de máquina para identificar patrocínios de arte contemporânea).
- *Achados:* a desigualdade na distribuição de patrocínio é maior na arte contemporânea do que em música e teatro, o que reflete a forte institucionalização e a dependência de patrocínio corporativo do segmento.
- *Implicação para a LICC:* mostra que a concentração difere por linguagem. Sem a variável segmento nos anexos da SECULT, a avaliação da LICC não consegue testar essa heterogeneidade, e essa é uma lacuna de dados a registrar no artigo.

## 2. Avaliações institucionais (IPEA, FGV, TCU, CGU)

**Leitura geral.** Os órgãos de controle (TCU, CGU) avaliam **conformidade e governança**: análise de admissibilidade, prestação de contas, economicidade. O IPEA avalia **distribuição e concentração**, de forma descritiva. A FGV estima **impacto econômico por matriz insumo-produto**. Nenhum dos documentos localizados estima o efeito **causal** da renúncia sobre produção, emprego ou acesso. Essa é a lacuna que a proposta de avaliação de impacto do artigo pode ocupar.

**2.1 BRASIL. Tribunal de Contas da União. *Acórdão nº 1.205/2014 – Plenário*. Levantamento sobre a estrutura de governança das renúncias tributárias. Relator: Min. Raimundo Carreiro. Processo TC 018.259/2013-8. Sessão de 14/05/2014.** URL: https://portal.tcu.gov.br/imprensa/noticias/tcu-avalia-a-estrutura-de-governanca-das-renuncias-tributarias. [VERIFICADO: notícia oficial do Portal TCU; o inteiro teor não foi lido]
- *Base:* página. *Nível:* VII (relatório de controle externo).
- *Achados:* aponta, entre as fragilidades da governança das renúncias federais, a "ausência de acompanhamento e de avaliação das renúncias tributárias". Recomenda que os ministérios setoriais regulamentem a gestão das ações financiadas por renúncia e definam objetivos, indicadores e metas para permitir avaliar resultados.
- *Implicação para a LICC:* a Lei 11.246/2021 não tem artigo de objetivos nem diagnóstico (`notas/politica/fontes/lei-11246-2021.md`, observações). A recomendação do TCU para a esfera federal serve de padrão normativo para criticar o desenho da LICC: é um gasto tributário sem objetivos, indicadores e metas declarados em lei.

**2.2 BRASIL. Tribunal de Contas da União. *Acórdão nº 191/2016 – Plenário*. Relator: Min.-Subst. Augusto Sherman Cavalcanti. Processo TC 034.369/2011-2. Sessão de 03/02/2016.** URL: https://portal.tcu.gov.br/imprensa/noticias/captacao-de-recursos-pela-lei-rouanet-nao-deve-ser-aplicada-a-projetos-com-potencial-lucrativo-determina-tcu. [VERIFICADO: notícia oficial do Portal TCU]
- *Base:* página. *Nível:* VII.
- *Decisão:* determina ao MinC que não autorize captação por renúncia para projetos com "forte potencial lucrativo" ou capacidade de atrair investimento privado suficiente. Segundo o relator, a análise de projetos lucrativos e autossustentáveis deve ser restritiva. A alternativa apontada é o patrocínio com recursos privados ou via Ficart.
- *Implicação para a LICC:* o TCU formula aqui o critério de **adicionalidade**: a renúncia se justifica só onde o mercado não financiaria. Nas cotas da IN 001/2025, 30% do teto vai para eventos calendarizados há mais de 10 anos. São justamente os projetos mais consolidados e com maior chance de financiamento privado, o que sugere tensão entre esse desenho e o critério do TCU. É uma hipótese a discutir, não um descumprimento apurado.

**2.3 BRASIL. Tribunal de Contas da União. *Relatório de Políticas e Programas de Governo 2018*: Lei Rouanet. Brasília: TCU, 2018.** URL: https://sites.tcu.gov.br/relatorio-de-politicas/2018/lei-rouanet.htm. Remete aos **Acórdãos 2.513/2018-Plenário** (Rel. Min.-Subst. Marcos Bemquerer) e **2.608/2018-Plenário** (Rel. Min. Benjamin Zymler). [VERIFICADO: sítio oficial do TCU; os acórdãos não foram lidos no inteiro teor]
- *Base:* página. *Nível:* VII (auditoria de conformidade em amostra de projetos).
- *Achados:* registra mais de R$ 13 bilhões destinados ao setor cultural por renúncia da Rouanet entre 2006 e 2017. Os achados de auditoria incluem documentação insuficiente da entrega de produtos, ausência de verificação de compatibilidade de preços com o mercado, movimentação financeira em contas não oficiais, pagamentos sem comprovação e despesas vedadas.
- *Implicação para a LICC:* o risco de controle de execução é estrutural no modelo. O Decreto 5.035-R/2021 exige conta específica do projeto no BANESTES e extrato publicado no DIO a cada repasse (arts. 16-17, `notas/politica/fontes/decreto-5035-r-2021.md`). Isso resolve a rastreabilidade do repasse, não a verificação da entrega nem da economicidade.

**2.4 BRASIL. Tribunal de Contas da União. *Acórdão nº 1.318/2023 – Plenário*. Auditoria operacional na Lei de Incentivo à Cultura (Lei 8.313/1991). Relator: Min.-Subst. Augusto Sherman Cavalcanti. Processo TC 040.520/2021-8. Sessão de 28/06/2023.** URLs: https://portal.tcu.gov.br/imprensa/noticias/auditoria-analisa-eficiencia-da-lei-rouanet e https://portal.tcu.gov.br/publicacoes-institucionais/fichas-sinteses/auditoria-na-lei-rouanet. [VERIFICADO: Portal TCU, notícia e ficha-síntese]
- *Base:* página. *Nível:* VII.
- *Achados (segundo a notícia do TCU):* auditoria de set./2021 a ago./2022 sobre admissibilidade, aprovação, análise técnica e homologação. As propostas caíram 14,6% em 2021 frente a 2020. Os arquivamentos não definitivos chegaram a 66,2% das propostas de 2021 e os definitivos a 54,7%. O prazo regulamentar de 60 dias de análise foi descumprido. O total captado em 2021 passou de R$ 2 bilhões. Houve recomendações sobre controles do SALIC.
- *Implicação para a LICC:* é o gargalo da etapa de **habilitação**, que também existe na LICC, com ciclos anuais e grande diferença entre habilitados e captados. Uma avaliação de processo da LICC deveria medir as taxas de habilitação e de captação e os tempos entre etapas, e os anexos da SECULT permitem medir ao menos a razão captados/habilitados.

**2.5 BRASIL. Controladoria-Geral da União. Secretaria Federal de Controle Interno. *Relatório de Auditoria nº 201603460*: Instituto Itaú Cultural (Pronac nº 1410875, Plano Anual de Atividades 2015). São Paulo: CGU-Regional/SP, 2016.** URL: https://eaud.cgu.gov.br/relatorios/download/12304.pdf. [VERIFICADO: PDF oficial no sistema e-Aud da CGU, p. 1-6 lidas]
- *Base:* texto (p. 1-6). *Nível:* VII/VI (auditoria de caso, amostra não estatística de 17,06% dos recursos captados, p. 2).
- *Achados:* o projeto Pronac 1410875 captou R$ 14.730.000,00 em 2015, doados integralmente por oito empresas do Grupo Itaú Unibanco pelo art. 26 da Rouanet (dedução de 40%, R$ 5.892.000,00 em deduções) (p. 2-3, Quadro 1). O próprio Itaú Cultural, instituto do grupo, captou R$ 260,6 milhões pela Rouanet entre 2005 e 2015, dado que a CGU cita do sítio do instituto (p. 2).
- *Implicação para a LICC:* documenta o circuito "empresa → instituto da própria empresa" descrito por Michetti (1.14). No ES, o art. 10, § 3º, do Decreto 5.035-R/2021 veda o benefício à patrocinadora e a seus sócios, mas pelo texto transcrito não menciona institutos mantidos por ela. É um ponto a examinar no desenho.

**2.6 SILVA, Frederico Augusto Barbosa da. *Financiamento cultural no Brasil contemporâneo*. Brasília: Ipea, mar. 2017. (Texto para Discussão, 2280).** URL: http://repositorio.ipea.gov.br/handle/11058/7523. Versão em periódico: SILVA, F. A. B. da. Financiamento cultural no Brasil contemporâneo. *Revista Brasileira de Políticas Públicas*, Brasília, v. 7, n. 1, 2017. DOI: https://doi.org/10.5102/rbpp.v7i1.4351. [VERIFICADO: repositório Ipea (texto lido, p. 7 e 17-31) + Crossref DOI do artigo]
- *Base:* texto do TD. *Nível:* VI (descritivo com dados do SALIC, 1995-2013). **É a análise distributiva mais detalhada localizada.**
- *Achados (páginas do TD):* em alguns anos do período, a taxa de projetos aprovados que conseguem captar é "sempre muito pequena (menos de 30%)" (p. 19). O número de projetos incentivados vai de 267 (1995) a 27.656 (2010) e 16.875 (2013), e o valor médio por projeto cai de cerca de R$ 147 mil (1998) para cerca de R$ 50 mil (2010) (p. 21). Entre 1995 e 2013, 823 dos 5.565 municípios receberam recursos, e São Paulo e Rio de Janeiro concentraram 65% (75% somando Belo Horizonte e Porto Alegre) (p. 22-23). Os 30 maiores proponentes somam 21,47% e os 30 maiores financiadores 41,40%, com a Petrobras sozinha em 12,73% (Tabelas 3 e 4, p. 26-27). 2% dos proponentes absorveram 46% dos recursos (p. 28). Em 2013, 41 financiadores (0,3%) responderam por 41% dos recursos, enquanto 8.398 (74,3%) apoiaram 54,6% dos projetos com 1,4% dos recursos (p. 28, Tabela 5). O autor lê isso como **coexistência** de uma lógica de mercado concentrado com uma lógica pulverizada e complementar, e diz que faltam pesquisas empíricas sobre o impacto no acesso da população (p. 29).
- *Implicação para a LICC:* (i) o fato estilizado "poucos aprovados captam" reaparece no ES. Ali a habilitação supera o teto de renúncia e a disputa por patrocinador decide (ver `licc-gov/CLAUDE-licc.md`), o que dá **variação natural entre habilitados que captam e que não captam**, a base de um desenho quase-experimental. (ii) O Silva é o contraponto necessário a uma leitura só crítica. A concentração convive com pulverização, e a pergunta de avaliação deve ser empírica: para quem vai, e com que efeito.

**2.7 SILVA, Frederico Augusto Barbosa da; FREITAS FILHO, Roberto. *Financiamento cultural: uma visão de princípios*. Brasília: Ipea, abr. 2015. 46 p. (Texto para Discussão, 2083).** URL: http://repositorio.ipea.gov.br/handle/11058/4220. [VERIFICADO: repositório Ipea, metadados e resumo]
- *Base:* resumo. *Nível:* VII/VI.
- *Conteúdo:* qualifica os argumentos que justificam a participação do Estado no financiamento cultural e examina a crítica de que a política foi "deixada ao mercado" pela primazia da Rouanet, a partir da composição de recursos públicos, privados e gastos tributários indiretos. Discute também o Vale-Cultura como incentivo ao consumo.
- *Implicação para a LICC:* ajuda a escrever a justificativa econômica (falha de mercado, bem de mérito) que a lei estadual não traz, e a contrastar incentivo à oferta (LICC) com incentivo à demanda.

**2.8 SILVA, Frederico Augusto Barbosa da. *Os limites do financiamento cultural federal no Brasil: entre ideias e materialidades*. Brasília: Ipea, ago. 2018. 67 p. (Texto para Discussão, 2409).** URL: http://repositorio.ipea.gov.br/handle/11058/8693. [VERIFICADO: repositório Ipea; resumo e sumário executivo lidos]
- *Base:* sumário executivo. *Nível:* VI/VII.
- *Conteúdo:* descreve a estrutura, a evolução e a composição do financiamento federal (despesas do MinC e recursos incentivados, divididos em recursos novos das empresas e renúncia da União). Aponta a falta de recursos humanos e de instrumentos para uma atuação "sistêmica", apesar do uso recorrente do termo sistema.
- *Implicação para a LICC:* sustenta um ponto do desenho. A capacidade administrativa da SECULT para analisar, fiscalizar e avaliar é insumo da teoria da mudança, não detalhe. A separação "recursos novos das empresas vs. renúncia" é a métrica de alavancagem privada, que na LICC é nula por construção, porque o crédito presumido corresponde ao valor destinado.

**2.9 SILVA, Frederico Augusto Barbosa da. *Mecenato cultural e demanda*. Brasília: Ipea, 2005. 30 p.** URL: https://repositorio.ipea.gov.br/handle/11058/14508. [VERIFICADO: repositório Ipea; resumo] (pesquisa da Disoc/Ipea em parceria com UNESCO e MinC)
- *Base:* resumo. *Nível:* VII.
- *Conteúdo:* descreve o sistema federal de financiamento e os agentes envolvidos (produtores, gestores, empresas, público) e a passagem, nos anos 1990, de um modelo centrado no Estado para outro com incentivos fiscais à participação empresarial, sob restrição orçamentária.
- *Implicação para a LICC:* é fonte histórica para o argumento de que o incentivo nasce de restrição fiscal e da busca de alavancar recursos privados. A LICC, com crédito integral, não alavanca, e isso deve ser dito no artigo.

**2.10 SACCARO JUNIOR, Nilo Luiz; ROCHA, Wilsimara Maciel; MATION, Lucas Ferreira (org.). *CMAP 2016 a 2018: estudos e propostas do Comitê de Monitoramento e Avaliação de Políticas Públicas Federais*. Brasília: Ipea, 2018. 219 p. ISBN 9788578113407.** URL: http://repositorio.ipea.gov.br/handle/11058/8796. [VERIFICADO: repositório Ipea, metadados] O livro tem um capítulo sobre a Lei Rouanet, intitulado no PDF avulso do Ipea "A Lei Rouanet e os seus efeitos no campo cultural e na [gestão pública]". `[VERIFICAR: autores e páginas do capítulo 2. O PDF avulso (portalantigo.ipea.gov.br) respondeu 403 e o livro completo (14 MB) excedeu o limite de leitura. Um resultado de busca atribui o capítulo a Silva e Ziviani, p. 41-64, mas isso não foi confirmado]`
- *Base:* metadados. *Nível:* VII (avaliação governamental *ex post* no âmbito do CMAP).
- *Implicação para a LICC:* mostra que a Rouanet já passou por avaliação no ciclo federal do CMAP. Vale conferir o capítulo e usá-lo como modelo de "avaliação de desenho" governamental, aproveitando a proximidade de formato com o artigo.

**2.11 FUNDAÇÃO GETULIO VARGAS; MINISTÉRIO DA CULTURA; ORGANIZAÇÃO DE ESTADOS IBERO-AMERICANOS. *Impacto econômico da Lei Rouanet: dados 2024*. [S. l.]: FGV, 2026. 31 p.** URL: https://portal.fgv.br/sites/default/files/uploads/relatorio-diagramado-19h.pdf. [VERIFICADO: PDF no portal da FGV (31 p.), lido por consulta automatizada; a matéria da IstoÉ Dinheiro de 13/01/2026 confirma a divulgação] `[VERIFICAR: autoria/coordenação e cidade na ficha técnica]`
- *Base:* texto (consulta dirigida ao PDF). *Nível:* VI (modelo insumo-produto: TRU e Contas Econômicas Integradas do IBGE, dados SALIC e formulário aos proponentes; não é desenho causal).
- *Achados:* estima um "Índice de Alavancagem Econômica" de R$ 7,59 movimentados na economia por R$ 1 gasto na execução dos projetos em 2024, com 228.069 postos de trabalho diretos e indiretos. O próprio relatório diz que o resultado **não é comparável** ao estudo FGV de 2018 (R$ 1,59 por R$ 1), porque passou a incluir gastos do público e outras fontes. Proponentes pessoa física ficaram de fora por anonimização.
- *Implicação para a LICC:* é o tipo de número que circula como "impacto". O artigo deve separar três coisas: multiplicador de gasto (insumo-produto, sem contrafactual, e que valeria para qualquer gasto de mesmo tamanho), efeito causal da renúncia e custo de oportunidade (o ICMS renunciado teria outro uso). O salto de 1,59 para 7,59 por mudança de método mostra quanto esses números dependem de hipóteses.
- Estudo FGV de 2018 (R$ 1,59 por R$ 1; período 1993-2018): `[VERIFICAR: relatório primário não localizado com URL estável; conhecido apenas pela imprensa (Exame, "Lei Rouanet traz retorno 59% maior que valor financiado, mostra FGV") e pela comparação no relatório de 2026]`.

**2.12 SILVA, Frederico A. B. da; ZIVIANI, Paula. *Mercado de trabalho da cultura: considerações sobre a meta 11 do Plano Nacional de Cultura (PNC)*. Brasília: Ipea, 2022. 53 p. (Texto para Discussão, 2715).** DOI: https://doi.org/10.38116/td2715. [VERIFICADO: Crossref DOI]
- *Base:* metadados (título e paginação). *Nível:* VI. `[VERIFICAR: ler o texto antes de atribuir resultados]`
- *Implicação para a LICC:* é a referência institucional para medir o **emprego cultural** como resultado. A meta 11 do PNC trata do mercado de trabalho da cultura, e o TD indica as fontes e as classificações (CBO/CNAE) viáveis, o que conversa com o uso de RAIS/PNAD na proposta de avaliação.

## 3. Leis estaduais via ICMS e municipais (IPTU/ISS)

(pendente)

## 4. Espírito Santo: LICC, Funcultura, SECULT, IJSN, UFES

(pendente)

## 5. Federalismo cultural, Sistema Nacional de Cultura, CPF da cultura

(pendente)

## 6. Estudos quantitativos (econometria) sobre efeitos de incentivos culturais no Brasil

(pendente)

## 7. Contraste: Lei Aldir Blanc e Lei Paulo Gustavo (fomento direto descentralizado)

(pendente)

## 8. Síntese: consensos e controvérsias

(pendente)

## 9. As 12-15 referências mais úteis para o artigo

(pendente)

## 10. Buscas sem resultado e pendências [VERIFICAR]

(pendente)
