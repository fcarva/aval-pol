# 03 — Contexto e problema/necessidade da LICC

> Nota de trabalho para a seção "Introdução com caracterização do problema/necessidade"
> do mini artigo (PECO 5046-6046). Regras: cada número com fonte e data; ausência não
> é zero; o que não foi verificado fica marcado [VERIFICAR].
>
> Status: seções 0 a 9 completas (23/09/2026). Seções 2-6 escritas a partir de tabelas geradas por
> `analise/03a`, `03c`, `03d` e `03e` (cache local; sem rede nesta rodada).

## 0. Resumo executivo

1. **O setor cultural capixaba é pequeno para o tamanho da economia do estado**: 4,2% da ocupação contra 5,8%
   no país (PNADC 2024), 18º lugar entre as UFs (§ 1.1).
2. **A desigualdade relevante é interna ao estado**: equipamentos de mercado (cinema, livraria, galeria) e
   capacidade institucional (plano, fundo) se concentram na RMGV (§§ 1.2-1.3).
3. **O gasto público direto com cultura cresceu muito em 2023-2025** (estado: R$ 57 mi em 2022 → R$ 182 mi em
   2025, empenhado nominal; municípios: R$ 179 mi → R$ 289 mi em 2023-2025), puxado em parte por
   transferências federais (Lei Paulo Gustavo, PNAB) (§§ 2-3). A LICC nasce e cresce no mesmo período.
4. **A LICC é de ordem de grandeza comparável à Rouanet no ES** (R$ 25-31 mi/ano contra cerca de R$ 35 mi por
   ano de projeto na Rouanet em 2019-2022) e, como a Rouanet, concentra-se em Vitória (§ 4).
5. **A renúncia é pequena para o ICMS** (0,16% da parcela estadual; 8% do limite legal de 2%), mas
   **relevante para a política cultural**: equivale a 14-21% do gasto estadual na função cultura (§ 6).
6. **Nenhuma norma declara o problema.** A árvore de problemas proposta (§ 7) formula como carência central a
   **baixa e desigual capacidade de financiar a produção e a oferta cultural fora do circuito já consolidado**,
   com causas na restrição de financiamento de pequenos produtores, na concentração territorial de
   equipamentos e capacidade e na dependência de poucos financiadores.

## 1. Setor cultural no ES e distribuição territorial

Todas as séries desta seção foram obtidas por API do IBGE em 2026-09-23 e salvas com cabeçalho de
fonte. Script: `analise/03b_ibge_cultura_es.py`.

### 1.1 Tamanho do setor (IBGE, SIIC)

Fonte: IBGE, Sistema de Informações e Indicadores Culturais (SIIC), pesquisa 10092 da API
`servicodados.ibge.gov.br/api/v1/pesquisas/10092` (última publicação da série 2011-2022 em
01/12/2023, com indicadores da PNAD Contínua atualizados até 2024). Tabela derivada:
`dados/externos/siic_uf.csv`. Unidades e multiplicadores vêm dos metadados da API (o indicador
82732 é publicado em **mil pessoas**).

| Indicador (ano) | ES | Brasil (soma das 27 UFs) | ES/BR |
| --- | ---: | ---: | ---: |
| Ocupados de 14+ anos no setor cultural, PNADC (2024) | 85 mil | 5.863 mil | 1,45% |
| Ocupados de 14+ anos, todos os setores, PNADC (2024) | 2.044 mil | 101.308 mil | 2,02% |
| Participação do setor cultural na ocupação (2024) | **4,16%** | **5,79%** | — |
| Pessoal assalariado no setor cultural, CEMPRE (2021) | 21.436 | 1.604.972 | 1,34% |
| Unidades locais do setor cultural, CEMPRE (2021) | 7.498 | 415.419 | 1,80% |
| Rendimento médio real habitual no setor cultural, PNADC (2024) | R$ 3.358 | — | — |
| % da despesa de consumo familiar com o grupo cultura, POF (2017-2018) | 7,8% | — | — |

Leituras (cálculos sobre `siic_uf.csv`):

- O ES tem 2,02% da ocupação do país e só 1,45% da ocupação cultural; a participação da
  cultura na ocupação capixaba (4,16%) é a **18ª entre as 27 UFs** em 2024 — abaixo de SP
  (7,55%), RJ (7,03%) e MG (5,01%), os vizinhos do Sudeste. O setor é relativamente pequeno
  no estado, não relativamente grande.
- A série de ocupados no setor cultural no ES oscila entre 73 mil (2014) e 89 mil (2018-2019),
  caiu para 79 mil em 2022 e voltou a 85 mil em 2024 — sem tendência clara de expansão no
  período da LICC (2022-2024). Isto é **contexto**, não efeito: nada aqui permite atribuir
  variação à política.
- A demanda das famílias não parece ser o gargalo: a fatia do orçamento familiar em cultura
  no ES (7,8%, POF 2017-2018) está entre as maiores do país (só RS 8,0%, RJ 8,6% e DF 8,7% acima;
  empatado com PB e AM). O "grupo cultura" da POF, no SIIC, inclui TV por assinatura/internet,
  eletrodomésticos e acessórios, então este número mede consumo cultural amplo, não frequência a
  espetáculos. [VERIFICAR a composição exata do grupo na publicação do SIIC antes de usar no texto.]
- Nota de método: a "soma das 27 UFs" é usada como total nacional porque a consulta à localidade
  Brasil não retornou valores nesta API; para PNADC a soma das UFs é consistente com o total
  nacional por construção amostral, mas difere dele em arredondamento (valores publicados em mil).

### 1.2 Acesso a equipamentos culturais (SIIC e MUNIC 2021)

SIIC, indicador "residentes em municípios com acesso a equipamentos culturais" (2021):
no ES, 74,5% da população vive em município com museu, 78,2% com teatro ou sala de
espetáculo e 65,1% com cinema. Referências: SP 86,6/88,1/77,8; RJ 81,2/93,6/85,8; MG
66,9/66,2/50,6 (`siic_uf.csv`, ano 2021).

A desigualdade relevante para a LICC é **interna ao estado**. MUNIC 2021, bloco Cultura
(IBGE, pesquisa 1, período 2021, publicado em 08/12/2022), 78 municípios do ES, população do
Censo 2022 (SIDRA 4709). Tabelas: `dados/externos/munic2021_cultura_es.csv` (por município) e
`dados/externos/munic2021_cultura_es_resumo.csv` (RMGV x interior). Cobertura: 77 dos 78
municípios responderam os itens de equipamento (Apiacá "Não informou").

| Existe no município (MUNIC 2021) | RMGV: municípios com "Sim" (de 7) | Interior: municípios com "Sim" (de 70 válidos) | % da pop. do interior em município com o item |
| --- | ---: | ---: | ---: |
| Cinema | 5 | 6 (8,6%) | 33,8% |
| Livraria | 6 | 7 (10,0%) | 24,2% |
| Galeria de arte | 4 | 7 (10,0%) | 19,4% |
| Teatro ou sala de espetáculo | 5 | 24 (34,3%) | 53,0% |
| Museu | 5 | 27 (38,6%) | 52,1% |
| Centro cultural | 5 | 31 (44,3%) | 61,7% |
| Ponto de Cultura | 5 | 33 (47,1%) | 38,3% |
| Biblioteca pública | 7 | 64 (91,4%) | 94,9% |

Na RMGV (7 municípios, 1,88 milhão de habitantes em 2022), 95,1% da população vive em município
com cinema; no interior (71 municípios, 1,95 milhão), 33,8%. Equipamento de mercado (cinema,
livraria, galeria) praticamente não existe fora da RMGV e de poucos polos; equipamento público
de base (biblioteca) é quase universal. A RMGV concentra **49,1% da população** do estado
(1.880.828 de 3.833.712, Censo 2022).

### 1.3 Capacidade institucional municipal (MUNIC 2021)

| Item (MUNIC 2021) | RMGV (de 7) | Interior (de 70 válidos) |
| --- | ---: | ---: |
| Conselho municipal de cultura | 7 | 50 (71,4%) |
| Fundo municipal de cultura | 5 | 35 (50,0%) |
| Plano municipal de cultura ("Sim", com ou sem instrumento legal) | 3 | 11 (15,7%) |
| Distribuiu recursos da Lei Aldir Blanc (2020) | 7 | 35 (50,0%) |

Quesito "quanto do orçamento previsto para a cultura foi executado em 2020"
(`dados/externos/munic2021_orcamento_cultura_es.csv`): 18 dos 78 municípios responderam
"Sem orçamento previsto" (17 no interior), 16 "até 10%", e 6 municípios do interior têm o valor
publicado "0" [VERIFICAR no questionário da MUNIC 2021 o significado do código "0" — não
tratar como 0% sem conferir]. 2020 é ano de pandemia; o quesito não serve para tendência.

**Síntese da seção 1.** O setor cultural capixaba é pequeno em relação ao seu peso na economia
(4,2% da ocupação contra 5,8% no país) e a oferta de equipamentos e a capacidade institucional
municipal se concentram na RMGV. Metade dos municípios do interior não tem fundo municipal de
cultura e a maioria não tem plano municipal — isto é, falta canal local para receber e aplicar
fomento. Essas são as condições em que um incentivo fiscal que depende de empresa patrocinadora
tende a reproduzir a concentração, o que a IN 001/2025 tenta corrigir com a cota de 10% fora da
RMGV (art. 18; ver `notas/politica/fontes/in-licc-001-2025.md`).

## 2. Gasto público com cultura no ES (estadual e municipal)

Fonte: SICONFI/STN, DCA (Anexo I-E), função 13 (Cultura), valores **empenhados** declarados pelo ente;
`dados/externos/siconfi_cultura_es_estado.csv`, `siconfi_cultura_uf.csv`, `siconfi_cultura_municipios_es.csv`
(script `analise/03c_siconfi_cultura_icms.py`); resumos em `analise/tabelas/03e_*.csv`
(`analise/03e_contexto_resumo.py`). Valores nominais, salvo indicação.

**Governo do estado (função 13, empenhado):**

| Ano | R$ mi (nominal) | R$ mi de 2025 (IPCA) | % da despesa total | Posição per capita entre as 27 UFs |
| --- | ---: | ---: | ---: | ---: |
| 2019 | 34,5 | 48,3 | 0,25% | — |
| 2020 | 62,1 | 84,3 | 0,40% | — |
| 2021 | 41,8 | 52,3 | 0,23% | — |
| 2022 | 56,8 | 65,1 | 0,25% | — |
| 2023 | 103,1 | 113,1 | 0,42% | — |
| 2024 | 119,5 | 125,5 | 0,43% | 18ª (R$ 30,1; mediana das UFs R$ 34,5) |
| 2025 | 181,9 | 181,9 | 0,59% | 10ª (R$ 45,8; mediana R$ 34,3) |

- O gasto estadual direto mais que triplicou de 2022 a 2025 em termos nominais. Parte disso é transferência
  federal que passa pelo orçamento estadual (Lei Paulo Gustavo e PNAB, § 3); o DCA não separa a fonte
  [VERIFICAR por fonte de recurso no Portal da Transparência do ES].
- A comparação entre UFs só está disponível para 2024-2025 no cache; em 2024 o ES estava abaixo da mediana
  per capita e da mediana da participação na despesa (0,43% × 0,54%); em 2025, acima (0,59% × 0,51%).
- A população usada pelo SICONFI para o per capita estadual é a declarada pelo ente (3.975.100 em 2024 e
  2025), não a estimativa do IBGE; serve para ordenar, não para comparar com o per capita municipal.

**Municípios (função 13, empenhado; `03e_f13_municipal_rmgv_interior.csv`):**

| Ano | Municípios com valor | Total (R$ mi) | RMGV: parcela / R$ por hab. | Interior: parcela / R$ por hab. | Vitória |
| --- | ---: | ---: | --- | --- | ---: |
| 2023 | 75/78 | 179,0 | 33,2% / 31,6 | 66,8% / 65,1 | 14,8% |
| 2024 | 77/78 | 250,7 | 30,1% / 40,2 | 69,9% / 94,3 | 11,8% |
| 2025 | 76/78 | 288,7 | 38,6% / 59,2 | 61,4% / 92,7 | 10,6% |

(per capita sobre a população de 2022 dos municípios com valor declarado; município sem função 13 fica
ausente.)

- **O gasto municipal direto é mais alto por habitante no interior do que na RMGV** — o inverso da LICC, que
  entrega R$ 48 por habitante à RMGV e R$ 23 ao interior (`notas/dados/01-resultados-descritivos.md`, § 5).
  Municípios pequenos têm custo fixo de equipamento e festas tradicionais pagas diretamente pela prefeitura;
  é contexto, não explicação causal.
- Somando estado e municípios, o gasto direto com cultura no ES foi de cerca de R$ 370 mi em 2024 e
  R$ 470 mi em 2025 (empenhado nominal; soma das duas tabelas acima).

## 3. Outros instrumentos de fomento no ES (mix de políticas)

| Instrumento | Natureza | Escala conhecida | Quem decide a alocação | Fonte |
| --- | --- | --- | --- | --- |
| **LICC** | gasto tributário (crédito de ICMS de 100%) | teto de R$ 10 mi (2022) a R$ 31 mi (2026) | empresa patrocinadora, entre habilitados | `notas/politica/01-desenho-legal.md` |
| **Funcultura / Editais da Cultura** | gasto direto do Fundo de Cultura do ES (LC 458/2008 [VERIFICAR]), com recursos da PNAB | R$ 46,85 mi em editais em 2025 (R$ 34,09 mi em 24 editais + 5 anteriores) | comissões de seleção, com critérios e pontuação por edital | notícia oficial do Governo do ES, "Editais da Cultura 2025" (resumo da busca; [VERIFICAR no texto]) |
| **Fundo a Fundo** | transferência estadual a municípios (editais municipais, patrimônio tombado, espaços culturais) | R$ 48 mi no ciclo 2025, dos quais R$ 8 mi para editais municipais | municípios aptos | mesma notícia [VERIFICAR] |
| **Lei Paulo Gustavo (LC 195/2022)** | transferência federal emergencial, execução 2023-2024 | R$ 75,8 mi ao ES: R$ 40,8 mi ao Funcultura e R$ 35,1 mi aos municípios | estado e municípios, por editais | Secom/Governo Federal (resumo da busca; [VERIFICAR]) |
| **PNAB (Lei 14.399/2022)** | transferência federal anual a estados e municípios | [VERIFICAR valores anuais do ES] | estado e municípios, por editais | [VERIFICAR] |
| **Lei Rouanet (Lei 8.313/1991)** | gasto tributário federal (IR) | cerca de R$ 35 mi por ano de projeto no ES em 2019-2022 | empresa ou pessoa patrocinadora | § 4 |
| Leis municipais de incentivo | gasto tributário municipal (ISS/IPTU) | [VERIFICAR, ex.: Vitória] | — | — |

Leitura: a LICC é **um de vários canais**, e o único estadual em que a escolha do projeto financiado é
privada. Em 2023-2025 o fomento direto (Funcultura, PNAB, LPG, Fundo a Fundo) cresceu mais depressa que a
LICC e com desenho distributivo explícito (editais por território e por público). Para a avaliação de
impacto isso significa **tratamentos concorrentes** no mesmo período e nos mesmos municípios, e um
contrafactual de "outras fontes" que existe de fato (viés de substituição; `notas/disciplina/03-gertler.md`,
§ 11.2).

## 4. Lei Rouanet no ES: concentração regional

Fonte: API do SALIC (MinC), mecanismo = Mecenato; `dados/externos/rouanet_captacao_uf_ano.csv` e
`rouanet_es_municipio.csv` (script `analise/03a_salic_rouanet_uf.py`, rodado para 2019-2022 com cache
completo; 2023 em diante depende de nova consulta à API, que não responde deste ambiente); resumo em
`analise/tabelas/03e_rouanet_es.csv`. **Atenção:** `valor_captado` é o acumulado do projeto até a consulta,
agrupado pelo ano do PRONAC, não a captação do ano calendário.

| Ano do PRONAC | Projetos no ES | Com captação | Captado (R$ mi) | Parcela do Brasil | Posição entre UFs |
| --- | ---: | ---: | ---: | ---: | ---: |
| 2019 | 49 | 28 | 35,2 | 2,20% | 7ª |
| 2020 | 65 | 31 | 25,7 | 1,20% | 9ª |
| 2021 | 60 | 36 | 48,3 | 3,88% | 6ª |
| 2022 | 58 | 31 | 30,1 | 1,90% | 10ª |
| 2019-2022 | 232 | 126 | 139,3 | 2,12% | 7ª |

- **O ES não é um "perdedor" regional da Rouanet**: com 1,9% da população do país (Censo 2022), capta 2,1%;
  SP (41,6%), RJ (17,6%) e MG (14,4%) somam 74% do total de 2019-2022.
- **A concentração é interna**: Vitória responde por **75,7%** do captado no ES em 2019-2022 (R$ 105,5 mi);
  Vila Velha e Serra somam 17%. Só 22 municípios capixabas têm algum projeto (o arquivo lista 23 linhas,
  uma delas "Rio de Janeiro" com UF = ES no SALIC, erro de cadastro da fonte).
- **Metade dos projetos aprovados não capta**: 126 de 232 (54%) tiveram alguma captação, na linha do
  "poucos aprovados captam" de Silva (2017; `notas/literatura/01-brasil.md`, 2.6).
- **Ordem de grandeza:** a LICC (R$ 25 mi captados em 2025) é comparável ao que a Rouanet leva ao ES por ano,
  e reproduz a mesma concentração em Vitória (48% do valor atribuível da LICC em 2022-2026).

## 5. Justificativa econômica e argumento declarado pelo governo

- **Argumento declarado:** as normas não trazem justificativa (`notas/politica/01-desenho-legal.md`, § 2).
  O discurso público da SECULT sobre a LICC [VERIFICAR notícias oficiais de 2021-2026] enfatiza volume
  investido e número de projetos, isto é, **insumo e produto**.
- **Justificativas econômicas possíveis** (a teoria da mudança precisa escolher e nomear pelo menos uma;
  Dekker e Rodrigues, 2019, sobre a Rouanet, em `notas/literatura/01-brasil.md`, 1.8):
  1. *Bem público / externalidade*: parte do valor da cultura (identidade, memória, patrimônio, efeitos de
     aglomeração criativa) não é apropriada por quem paga ingresso → subprovisão pelo mercado.
  2. *Bem de mérito*: o Estado considera o acesso à cultura um direito (Constituição, art. 215) e quer
     consumo maior que o escolhido pelas famílias.
  3. *Restrição de crédito e de financiamento* de pequenos produtores, com receitas incertas e ativos
     intangíveis.
  4. *Doença de custos* (Baumol) nas artes cênicas e na música ao vivo: produtividade estagnada, custos
     crescentes [a literatura internacional está pendente: `notas/literatura/02-internacional.md`].
- **O instrumento escolhido e a falha que ele corrige.** Um crédito integral com escolha privada corrige
  bem a falha 3 **para quem já tem acesso a patrocinadores**, e pouco as falhas 1 e 2 fora do circuito
  consolidado; a escolha pelo patrocinador tende a seguir visibilidade de marca, que correlaciona com
  público grande e evento consolidado. Os descritivos (conversão maior no teto, incumbência, concentração em
  Vitória) são compatíveis com isso.
- **Adicionalidade e alavancagem:** com crédito de 100%, a LICC **não alavanca recurso privado**; a
  adicionalidade relevante é se o projeto aconteceria sem o incentivo (TCU, Acórdão 191/2016).

## 6. Renúncia da LICC em relação à arrecadação de ICMS do ES

Fonte: `dados/externos/licc_teto_vs_icms.csv` (`analise/03d_licc_escala_icms.py`), com ICMS do SICONFI/DCA
(`siconfi_icms_es.csv`, conta 1.1.1.4.50.1.0) e tetos das portarias da SEFAZ conferidas no DIO-ES.

| Ano | Teto (R$ mi) | Limite legal de 2% (R$ mi) | Teto / limite | Teto / ICMS estadual do ano anterior | Teto / função 13 estadual | Teto / função 13 estado + municípios |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 2022 | 10 | 230,0 | 4,3% | 0,09% | 17,6% | — |
| 2023 | 15 | 248,6 | 6,0% | 0,12% | 14,5% | 5,3% |
| 2024 | 25 | 264,9 | 9,4% | 0,19% | 20,9% | 6,8% |
| 2025 | 25 | 312,1 | 8,0% | 0,16% | 13,7% | 5,3% |
| 2026 | 31 | 337,8 | 9,2% | 0,18% | — | — |

(limite de 2% = 2% × (ICMS bruto − parcela dos municípios) do exercício anterior; leitura do art. 5º-B, IX,
"a", da Lei 7.000/2001.)

- **Para o Tesouro a renúncia é pequena** (menos de 0,2% do ICMS estadual) e está muito abaixo do limite
  legal: a lei permitiria uma LICC de mais de R$ 300 mi. O tamanho é escolha anual da SEFAZ, não restrição
  legal — e o teto foi ampliado no meio do ano três vezes (`notas/politica/01-desenho-legal.md`, § 13).
- **Para a política cultural a renúncia é grande**: equivale a 14-21% do gasto estadual direto com cultura.
  É gasto público sem passar pelo orçamento da SECULT e sem decisão pública sobre qual projeto recebe.
- **Custo econômico**: o custo da LICC para o Estado é o ICMS renunciado (igual ao captado, por ser crédito
  integral) mais o custo administrativo (SECULT, SEFAZ, CAP, pareceristas) e o custo de captação dos
  proponentes (até 10% do projeto pode pagar captação, IN25, art. 27; IN26, art. 28), menos o patrocínio que
  as empresas fariam de qualquer forma (`notas/disciplina/04-itau-magenta-adb.md`, § 5.5).

## 7. Árvore de problemas (proposta)

Proposta do avaliador, porque a norma não traz diagnóstico (M03 [s.18]: o problema é uma carência, com
população-alvo, ligada aos resultados finais). Cada causa vem com a evidência disponível; o que é hipótese
está marcado.

**Problema central:** produtores e agentes culturais capixabas, sobretudo os de pequeno porte e os de fora
do circuito consolidado da RMGV, têm **baixa e desigual capacidade de financiar a produção e a oferta
cultural**, o que limita a oferta de bens e serviços culturais e o acesso da população a eles.

| Nível | Conteúdo | Evidência / fonte |
| --- | --- | --- |
| Efeitos (consequências) | Oferta cultural pequena e concentrada; ocupação cultural abaixo da média nacional; acesso desigual a equipamentos; produção dependente de poucos financiadores e de editais públicos | § 1.1 (4,2% × 5,8%); § 1.2 (cinema: 95% da população da RMGV × 34% do interior); § 4 |
| Causa 1 | **Restrição de financiamento** de pequenos produtores: receitas incertas, ativos intangíveis, pouca garantia | hipótese da literatura (§ 5); nos dados, MEI capta 44% × 75% das associações (`01-resultados-descritivos.md`, § 2) |
| Causa 2 | **Poucos financiadores privados** e concentrados em setores regulados e grandes contribuintes | EDP = 44% da LICC 2025; Vitória = 76% da Rouanet no ES (§ 4) |
| Causa 3 | **Capacidade institucional municipal desigual**: sem plano, fundo ou equipamento, o município não gera nem recebe projetos | § 1.3 (metade do interior sem fundo; 16% com plano) |
| Causa 4 | **Custos de transação para acessar fomento** (elaborar projeto, cumprir exigências, achar patrocinador) | hipótese; a IN permite pagar elaboração e captação (IN25, arts. 27-28) |
| Causa 5 | **Base de demanda local pequena** fora dos polos (renda, escala, distância) | hipótese contextual; POF indica gasto familiar alto com cultura no agregado (§ 1.1), o que sugere que a demanda não é o gargalo principal |

**Leitura para a avaliação de desenho:** a LICC ataca a causa 1 **condicionada à causa 2** — o recurso só
chega a quem convence um patrocinador —, e só marginalmente as causas 3 e 4 (cota III, contrapartidas). A
teoria da mudança deve explicitar isso como premissa ("existem contribuintes dispostos a patrocinar projetos
fora do circuito consolidado") e testá-la (`notas/disciplina/01-slides-e-guias.md`, § 2.3, perguntas 5 e 8).

## 8. Tabelas derivadas e scripts

| Tabela | Script | Conteúdo |
| --- | --- | --- |
| `dados/externos/siic_uf.csv` | `03b_ibge_cultura_es.py` | SIIC por UF (§ 1.1) |
| `dados/externos/munic2021_cultura_es*.csv`, `munic2021_orcamento_cultura_es.csv` | `03b_ibge_cultura_es.py` | MUNIC 2021, bloco Cultura (§§ 1.2-1.3) |
| `dados/externos/siconfi_cultura_*.csv`, `siconfi_icms_es.csv` | `03c_siconfi_cultura_icms.py` | Função 13 e ICMS (§§ 2, 6) |
| `dados/externos/licc_teto_vs_icms.csv`, `licc_habilitados_por_cota.csv` | `03d_licc_escala_icms.py` | Escala da renúncia (§ 6) |
| `dados/externos/rouanet_captacao_uf_ano.csv`, `rouanet_es_municipio.csv` | `03a_salic_rouanet_uf.py 19 20 21 22` | Rouanet 2019-2022 (§ 4) |
| `analise/tabelas/03e_*.csv` | `03e_contexto_resumo.py` | Resumos das seções 2 e 4 |

## 9. Pendências [VERIFICAR]

- Rouanet 2023 em diante: rodar `analise/03a_salic_rouanet_uf.py` numa máquina com acesso à API do SALIC
  (o cache de 2023 parou no offset 5.000 de 10.722).
- Separar o gasto estadual da função 13 por fonte de recurso (tesouro estadual × transferências federais).
- Valores anuais da PNAB para o ES e para os municípios; Funcultura (LC 458/2008) e Fundo a Fundo no texto
  das notícias e dos atos oficiais (lidos só em resumo de busca).
- Composição do "grupo cultura" da POF no SIIC (§ 1.1) e significado do código "0" no quesito de orçamento
  executado da MUNIC 2021 (§ 1.3).
- Leis municipais de incentivo fiscal à cultura no ES (existência e escala).
- Discurso oficial da SECULT sobre objetivos e resultados da LICC (notícias 2021-2026) e mensagem do projeto
  de lei que virou a Lei 11.246/2021.
