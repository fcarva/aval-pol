# Resultados descritivos da LICC (habilitados 2022-2026 e captados 2025)

> Status: seções 0 a 10 completas (23/09/2026). Números regerados nesta data a partir de `dados/` com os scripts
> listados abaixo; toda tabela citada está em `analise/tabelas/`.

## 0. Fontes, scripts e convenções

**Dados da política (proveniência oficial, transcritos pelo licc.gov):**

| Arquivo | Conteúdo | Fonte |
| --- | --- | --- |
| `dados/licc/habilitados/habilitados-{2022..2026}.csv` | 467 registros, um por projeto em cada seção "PROJETOS HABILITADOS - ANO X" | Lista única da SECULT, https://secult.es.gov.br/lista-de-projetos-habilitados (coluna `fonte_pagina` = página do PDF; seções 2026 nas p. 1-6, 2025 p. 7-11, 2024 p. 11-18, 2023 p. 18-24, 2022 p. 24-26) |
| `dados/licc/oficial/captados-2025.csv` | 63 projetos que captaram no ano-calendário 2025, 95 termos de patrocínio com CNPJ e valor | Anexo "RECURSO FINANCEIRO CAPTADO - 2025", https://secult.es.gov.br/Media/secult/LICC/RECURSO%20FINANCEIRO%20CAPTADO%20-%202025.pdf |

**Dados externos** (`analise/02_externos.py`, cache bruto em `dados/externos/*.json`): lista dos 78 municípios do ES com código IBGE (API de localidades), população do Censo 2022 (SIDRA t. 4709, v. 93), estimativas 2024-2026 (SIDRA t. 6579, v. 9324), PIB municipal a preços correntes 2021-2023 (SIDRA t. 5938, v. 37, R$ mil; 2023 é o último ano publicado), malha municipal GeoJSON (API de malhas v3). Consolidado em `dados/externos/municipios_es.csv`.

**RMGV (composição legal conferida no texto):** Lei Complementar estadual nº 318/2005, art. 2º: a RMGV é integrada por Cariacica, Fundão, Guarapari, Serra, Viana, Vila Velha e Vitória (PDF oficial lido em 23/09/2026: https://planometropolitano.es.gov.br/Media/comdevit/Legisla%C3%A7%C3%A3o/2005-01-lei318-05.pdf). A data exata da LC aparece como 17/01/2005 no Decreto 1.511-R/2005 e como 18/01/2005 na página de legislação do PDUI [VERIFICAR a data; a composição não muda].

**Scripts (rodar nesta ordem; todos em `analise/`):**

1. `_comum.py`: normalização de texto, Gini, Theil, HHI, CRk, cache das APIs.
2. `02_externos.py`: dados do IBGE e RMGV. Pode rodar antes do 01 (o 01 só usa a lista de municípios, que o `_comum` baixa sozinho).
3. `01_carregar.py`: padroniza, resolve municípios, cria chave de proponente, casa captados→habilitados. Saídas em `dados/processados/` e auditorias em `analise/tabelas/01_*.csv`.
4. `03_descritivas.py`: todas as tabelas `analise/tabelas/03_*.csv`.
5. `04_figuras.py`: figuras `analise/figuras/04_*.png` (300 dpi). [ainda não criado]

**Convenções que valem para todos os números abaixo:**

- **Unidade.** "Registro" = projeto × seção da lista (467). "Processo" = número de processo distinto (463): quatro processos aparecem nas seções 2025 **e** 2026 (2024-454L8, 2024-7NZLF, 2025-49GXP, 2025-SB2J8), com status divergentes entre as seções em dois deles. Estatística por ciclo usa registros da seção; estatística agregada 2022-2026 usa processos distintos (registro da seção mais recente).
- **"Ciclo" é a seção "ANO X" da lista, não o ano de protocolo.** O prefixo do processo é o ano de protocolo: a seção 2026 tem 74 processos de 2025, 12 de 2026 e 2 de 2024; a seção 2023 tem 61 processos de 2022 (`03_ciclo_x_ano_protocolo.csv`). O significado exato de "ANO X" (exercício de habilitação ou de captação pretendida) não está declarado no documento [VERIFICAR com a SECULT].
- **Ausência não é zero.** Célula vazia fica ausente e cada estatística traz a cobertura (n com dado / n total). Quatro valores de R$ 500,00 na p. 12 (seção 2024: 2024-XDJHX, 2024-VM90J, 2024-B7ZFZ autorizados; 2024-X6HWG total) são tratados como **ausentes**: a versão do PDF atualizada em 10/09/2026, lida por parser (firecrawl) em 23/09/2026, imprime "R$ 500,000,00" (separador malformado) para 2024-VM90J; o transcritor leu 500. Os valores brutos seguem em `valor_*_bruto` (`01_valores_suspeitos.csv`) [VERIFICAR no PDF].
- **Município = "Local de Execução"**, não a sede do proponente (a cota do art. 18, III, da IN 001/2025 exige sede **e** execução fora da RMGV; a sede não é publicada). A célula da fonte vem com quebras de linha misturadas; o resolvedor (i) casa os 78 nomes oficiais do IBGE, do mais longo para o mais curto; (ii) aplica uma tabela explícita de grafias/apelidos (ex.: "Vila Veha", "Cachoeiro" como prefixo único, distritos IBGE São Torquato→Vila Velha e Santa Marta→Ibitirama, "Itaúnas"→Conceição da Barra [VERIFICAR]); (iii) repara 9 transbordamentos de célula entre registros vizinhos e 1 célula com linhas intercaladas (16 registros marcados `flag_municipio_incerto`; `01_municipios_transbordo.csv`). Bairros, "a definir", regiões e locais fora do ES ficam **não resolvidos** (`01_municipios_resolucao.csv`).
- **Valor territorial** só é atribuído quando o registro nomeia **um único local** e ele é município do ES (regra do licc.gov: o rateio entre municípios não é publicado). Presença conta em todos os municípios nomeados.
- **Casamento captados→habilitados:** título normalizado **exato** (minúsculas, sem acento, só letras e números). Título que corresponde a mais de um processo é "ambíguo" e fica fora do resultado principal. Um casamento secundário (desempate por valor autorizado idêntico ao centavo) só aparece em sensibilidade.
- Normas citadas: textos conferidos em `notas/politica/fontes/` (IN SECULT 001/2025; Decreto 5.035-R/2021; Lei 11.246/2021; portarias).


## 1. Evolução anual dos habilitados (2022-2026)

Tabela: `03_anual.csv` (registros da seção de cada ciclo; a última linha usa processos distintos).

| Ciclo | Registros | Proponentes distintos | Autorizado (R$ mi) | Autorizado mediano (R$) | Valor total dos projetos (R$ mi) | Autorizado/total (agregado) | % com autorizado = total |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 2022 | 69 | 53 | 23,35 | 368.109 | 31,41 | 0,74 | 81,2% |
| 2023 | 113 | 92 | 44,29 (112/113) | 482.381 | 54,48 | 0,81 | 78,6% |
| 2024 | 123 | 95 | 46,72 (120/123) | 481.000 | 70,70 | 0,68 | 73,7% |
| 2025 | 74 | 57 | 33,49 | 499.765 | 47,55 | 0,70 | 73,0% |
| 2026 | 88 | 73 | 37,92 | 499.559 | 56,91 | 0,67 | 72,7% |
| 2022-2026 (processos) | 463 | 235 | 183,95 (459/463) | 485.088 | 259,23 | 0,72 | 75,5% |

Leituras:

- **A demanda habilitada supera o teto de renúncia em todos os ciclos com teto conhecido.** Tetos anuais
  (`dados/externos/licc_teto_vs_icms.csv`, com a fonte de cada um): R$ 10 mi (2022, Portaria SEFAZ 09-R/2022,
  conferida), R$ 15 mi (2023, [VERIFICAR]), R$ 25 mi (2024, ampliação anunciada pela SECULT; ato [VERIFICAR]),
  R$ 25 mi (2025, captação somada = R$ 25.000.000,00), R$ 25 mi (2026, [VERIFICAR]). Como a captação de um
  ciclo ocorre sobretudo no ano seguinte (§ 7), a comparação natural é com o teto do ano seguinte: a soma
  autorizada dos ciclos 2022-2025 é 1,6 (2022: R$ 23,4 mi para R$ 15 mi), 1,8 (2023), 1,9 (2024) e 1,3 (2025)
  vezes esse teto. Contra o teto do mesmo ano, o ciclo 2023 chega a 3,0 vezes. A comparação é indicativa, porque ciclo de habilitação não é ano de captação (regra 4 do
  `CLAUDE.md`; ver § 7), mas a ordem de grandeza não depende disso: **a LICC habilita mais do que pode
  pagar e o racionamento acontece na captação**, fora do controle da SECULT.
- **O valor autorizado mediano sobe até encostar no teto por projeto** (R$ 368 mil em 2022; R$ 499,8 mil em 2025 e
  R$ 499,6 mil em 2026). Ver § 4.
- **A LICC financia quase todo o projeto.** Em três de cada quatro registros o valor autorizado é igual ao
  valor total declarado do projeto (75,5% dos processos); no agregado, o autorizado é 72% do valor total,
  porque poucos projetos grandes declaram outras fontes (ex.: 2025-9R9X2, R$ 0,69 mi autorizados de
  R$ 2,51 mi; `03_acima_teto_geral.csv`). Isso importa para a adicionalidade: não há contrapartida
  financeira obrigatória do proponente nem da empresa (ver `notas/politica/01-desenho-legal.md`).
- **Anomalias de fonte.** Cinco registros têm autorizado maior que o total (2024-L44FD, 2024-VWLGS,
  2023-0HB19, 2024-Q2470 no ciclo 2024; 2025-R0CZP no ciclo 2025), com diferenças de R$ 0,60 a R$ 13,4 mil;
  e quatro valores de R$ 500,00 na p. 12 são tratados como ausentes (`01_valores_suspeitos.csv`). [VERIFICAR
  no PDF da SECULT.]
- **Ciclo ≠ ano de protocolo** (`03_ciclo_x_ano_protocolo.csv`): a seção 2023 tem 61 processos protocolados
  em 2022 e 52 em 2023; a seção 2024 tem 83 de 2023; a seção 2026 tem 74 de 2025. O "ANO X" da lista é o
  exercício de habilitação, que em geral vem um ano depois do protocolo [VERIFICAR com a SECULT o significado
  exato].

## 2. Status e "conversão" habilitado -> executado

Tabelas: `03_status_por_ciclo.csv`, `03_status_rotulos.csv`, `03_status_conversao_*.csv`. Rótulos da fonte
(versão da lista de 10/09/2026): "Em captação", "Em execução", "Execução finalizada", "Prazo de captação
expirado". **Hipótese de trabalho**: "executado" = em execução + finalizada = captou ao menos o mínimo;
"prazo expirado" = não captou o suficiente. A legenda oficial não define os estados [VERIFICAR].

| Ciclo | Em captação | Em execução | Finalizada | Prazo expirado | Executados / resolvidos | Expirados / resolvidos |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 2022 | 0 | 0 | 58 | 11 | 84,1% | 15,9% |
| 2023 | 0 | 9 | 70 | 34 | 69,9% | 30,1% |
| 2024 | 12 | 20 | 41 | 50 | 55,0% | 45,0% |
| 2025 | 18 | 46 | 7 | 3 | (ciclo aberto) | — |
| 2026 | 69 | 17 | 2 | 0 | (ciclo aberto) | — |

"Resolvidos" exclui os que ainda estão em captação. Os ciclos 2025 e 2026 estão abertos e não servem para
taxa de conversão.

- **A perda na captação cresce com a expansão da habilitação.** Entre 2022 e 2024 o número de habilitados
  quase dobrou (69 → 123) e a fração que expira foi de 16% para 45% dos resolvidos. É o "funil de atrito" da
  teoria da mudança (TdM [s.19-22]) medido no único elo que tem dado oficial.
- **Gradiente por valor autorizado, dentro de cada ciclo** (`03_status_conversao_por_faixa_valor_e_ciclo.csv`):

  | Ciclo | Até R$ 400 mil | R$ 400-500 mil (excl.) | Exatamente R$ 500 mil |
  | --- | ---: | ---: | ---: |
  | 2022 | 79% (38) | 91% (22) | 89% (9) |
  | 2023 | 59% (41) | 70% (47) | 87% (23) |
  | 2024 | 27% (45) | 69% (35) | 78% (27) |

  (taxa de executados entre resolvidos; n entre parênteses). No agregado 2022-2024
  (`03_status_conversao_por_faixa_valor_2022_2024.csv`): 52% até R$ 200 mil, 54% de R$ 200 a 400 mil,
  74% de R$ 400 a 500 mil e 83% em exatamente R$ 500 mil. **Projetos que pedem o teto captam mais**, e a
  diferença aumenta justamente quando o racionamento aperta (2024). Descrição, não causalidade: o valor
  pedido correlaciona com porte, rede e histórico do proponente.
- **Por natureza jurídica inferida** (`03_status_conversao_por_natureza_2022_2024.csv`; natureza inferida
  do nome, ver § 6): associações/institutos/fundações 75% (107), empresas com sufixo societário 69% (127),
  MEI/empresário individual 44% (25), grupos e coletivos 54% (13).
- **RMGV × interior** (`03_status_conversao_rmgv_interior_2022_2024.csv`; só registros com um único
  município, 227 de 293 resolvidos): 67,5% na RMGV (151) e 63,2% no interior (76). A diferença territorial
  na conversão é pequena; a desigualdade territorial nasce antes, na habilitação (§ 5).

## 3. Enquadramento nas cotas (IN LICC 001/2025, art. 18)

Tabelas: `03_enquadramento_cobertura.csv`, `03_enquadramento_por_ciclo.csv`, `03_cota_fora_rmgv_coerencia.csv`,
`03_cota_iv_execucao_so_interior.csv`. Texto da norma: `notas/politica/fontes/in-licc-001-2025.md`.

- **Cobertura:** a coluna "Enquadramento para efeito de captação" só existe a partir do ciclo 2024
  (123/123, 74/74, 88/88); 2022 e 2023 não trazem cota (0/69, 0/113). A regra das quatro cotas só pode
  ser descrita para 2024-2026.
- **Distribuição do valor autorizado por cota**, com a reserva normativa entre parênteses:

  | Cota (art. 18) | 2024 | 2025 | 2026 |
  | --- | ---: | ---: | ---: |
  | I eventos calendarizados > 10 anos (30%) | 16 proj., R$ 7,25 mi (15,5%) | 17, R$ 8,41 mi (25,1%) | 14, R$ 6,76 mi (17,8%) |
  | II planos plurianuais (10%) | 4, R$ 1,50 mi (3,2%) | 4, R$ 1,77 mi (5,3%) | 6, R$ 2,76 mi (7,3%) |
  | III fora da RMGV (10%) | 17, R$ 5,61 mi (12,0%) | 13, R$ 5,57 mi (16,6%) | 12, R$ 3,89 mi (10,3%) |
  | IV demais (50%) | 86, R$ 32,36 mi (69,3%) | 40, R$ 17,74 mi (53,0%) | 56, R$ 24,52 mi (64,7%) |

  (percentual sobre o autorizado do ciclo; 2024 com 120/123 valores).
- **As reservas são sobre o teto (R$ 25 mi), não sobre a demanda.** Comparando o autorizado classificado
  com a reserva em reais: cota I tem R$ 6,8 a 8,4 mi para R$ 7,5 mi reservados; cota II, R$ 1,5 a 2,8 mi
  para R$ 2,5 mi; cota III, R$ 3,9 a 5,6 mi para R$ 2,5 mi; cota IV, R$ 17,7 a 32,4 mi para R$ 12,5 mi.
  A demanda habilitada das cotas III e IV supera a reserva em todos os ciclos (cota III: 1,6 a 2,2 vezes os
  R$ 2,5 mi); a da cota I fica abaixo da reserva em 2024 (R$ 7,25 mi) e 2026 (R$ 6,76 mi), e a da cota II em
  2024 e 2025. Como 30-45% dos habilitados não captam (§ 2), mesmo uma demanda acima da reserva pode não
  preenchê-la. Pelo § 1º do art. 18, o que excede as reservas I-III disputa a cota IV. Se as cotas mudam o
  resultado depende da captação por cota, que não é publicada (o anexo de captados não traz cota; § 7) →
  **indeterminado** (regra 3 do `CLAUDE.md`).
- **Coerência territorial da cota III.** A cota exige sede **e** execução fora da RMGV; a sede não é
  publicada. Dos projetos classificados na cota III, 0 de 17 (2024), 3 de 13 (2025) e 3 de 12 (2026)
  listam algum município da RMGV como local de execução, e 2 (2025) e 1 (2026) não têm município
  resolvido. Pode ser erro de classificação, execução itinerante que inclui a RMGV ou leitura da regra
  pela SECULT [VERIFICAR]; não se afirma descumprimento.
- **Cota IV executada só no interior:** 9 de 86 (2024), 3 de 40 (2025) e 7 de 56 (2026) registros da cota
  IV têm todos os locais no interior. Poderiam, em tese, ter pedido a cota III, mas o critério da sede não é
  observável; é só um indicador de que a cota III não esgota a execução no interior.

## 4. Valores por projeto e bunching no teto por projeto

Tabelas: `03_bunching_teto.csv`, `03_bunching_faixas_10mil.csv`, `03_acima_teto_geral.csv`. Tetos por projeto
da IN 001/2025: R$ 500 mil (art. 14), R$ 300 mil para evento em 1ª edição (art. 14, § 2º), R$ 1 mi para
intervenção física em patrimônio e obra audiovisual de longa-metragem ou seriada (arts. 15-16).

| Ciclo | Com valor | Exatamente R$ 500 mil | R$ 490 mil a R$ 500 mil (incl.) | Acima de R$ 500 mil | Exatamente R$ 300 mil |
| --- | ---: | ---: | ---: | ---: | ---: |
| 2022 | 69 | 9 (13,0%) | 17,4% | 0 | 0 |
| 2023 | 112 | 23 (20,5%) | 42,0% | 1 | 0 |
| 2024 | 120 | 30 (25,0%) | 43,3% | 1 | 0 |
| 2025 | 74 | 27 (36,5%) | 67,6% | 2 | 2 |
| 2026 | 88 | 36 (40,9%) | 58,0% | 3 | 7 |
| 2022-2026 (processos) | 459 | 124 (27,0%) | 45,8% | 7 | 9 |

- **Há amontoamento no teto e ele cresce.** Nos processos distintos, 86 caem na faixa de R$ 490-500 mil
  (exclusive) e 124 em exatamente R$ 500 mil, contra 20 na faixa de R$ 480-490 mil e 1 a 15 em cada faixa
  de R$ 10 mil entre R$ 400 e 480 mil (`03_bunching_faixas_10mil.csv`). A parcela em exatamente R$ 500 mil
  triplica de 2022 para 2026.
- **Leitura para o desenho:** o teto por projeto é vinculante para boa parte da demanda. Somado ao § 2 (quem
  pede o teto capta mais), sugere que o valor pedido é escolhido pela regra, não pelo custo do projeto, e
  que o teto por projeto funciona como o principal instrumento de pulverização da renúncia. Hipótese
  (§ 9), não achado causal.
- **Acima do teto geral:** 7 processos (`03_acima_teto_geral.csv`); os de 2025-2026 são de R$ 0,69 a 1 mi,
  compatíveis com as exceções dos arts. 15-16 (audiovisual, patrimônio). Dois são de 2023-2024 (museus,
  R$ 0,70 e 0,77 mi), antes da IN 001/2025 [VERIFICAR a regra da época].
- **Captação de 2025** (`03_captados_resumo.csv`): 19 dos 63 projetos captaram exatamente R$ 500 mil;
  captação mediana R$ 489.200; média R$ 396.825.

## 5. Distribuição territorial

Tabelas: `03_territorio_indicadores.csv`, `03_territorio_rmgv_interior.csv`, `03_territorio_por_ciclo.csv`,
`03_municipios.csv`; coortes de presença calculadas sobre `dados/processados/habilitados_municipios.csv`
(ver nota de sensibilidade no fim da seção). Presença conta todos os municípios nomeados; valor só é
atribuído a processo com um único município do ES (340 de 463 processos; 74,1% do valor autorizado).

**RMGV × interior, 2022-2026 (processos distintos):**

| Grupo | Municípios | População 2022 | PIB 2023 | Presenças | Valor autorizado atribuível | R$ por habitante | Municípios nunca presentes |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| RMGV | 7 | 49,1% | 54,9% | 55,1% | 66,6% (R$ 90,8 mi) | 48,30 | 0 |
| Interior | 71 | 50,9% | 45,1% | 44,9% | 33,4% (R$ 45,5 mi) | 23,28 | 14 |
| ES | 78 | 3.833.712 hab. | R$ 209,8 bi | 735 | R$ 136,3 mi | 35,55 | 14 |

- **Concentração maior que a da população e a do PIB.** Gini do valor atribuível entre os 78 municípios
  (zeros incluídos) = **0,88**; per capita = 0,81; da população = 0,64; do PIB = 0,75. Por ciclo, o Gini do
  valor fica entre 0,88 e 0,93 (`03_territorio_por_ciclo.csv`). É o mesmo fato estilizado da Rouanet
  ("mais concentrada que o PIB", Guimarães, 2020, em `notas/literatura/01-brasil.md`, 1.10) reproduzido
  dentro do ES.
- **Vitória é o centro de gravidade:** 48,1% do valor atribuível, 30,1% das presenças, 8,4% da população;
  R$ 203 por habitante. Vila Velha (R$ 25/hab.), Cariacica (R$ 22) e Serra (R$ 8,6) estão abaixo da média
  estadual. Fora da RMGV, municípios pequenos com poucos proponentes recorrentes aparecem com valores per
  capita altos: Muqui (R$ 304/hab.), Mimoso do Sul (R$ 205), Santa Teresa (R$ 204), Ibiraçu (R$ 202).
- **A desigualdade é sobretudo dentro dos grupos, não entre RMGV e interior.** Decomposição de Theil
  (ponderada pela população): componente entre RMGV e interior = 6,9% do total. A cota III, que usa
  justamente a fronteira RMGV × interior, atua sobre a menor parte da desigualdade medida.
- **Porte:** correlação de Spearman entre valor atribuível e população = 0,57; entre presença e população =
  0,67. Entre os 34 municípios com valor positivo, a elasticidade valor-população (MQO em log) é 0,58.
- **Adoção e presença por ciclo (resolvedor canônico, `01_carregar.py`):** municípios com ao menos um
  projeto habilitado por ciclo: 39 (2022), 45 (2023), 31 (2024), 32 (2025), 42 (2026). Primeira presença
  (coorte): 39 em 2022, 16 em 2023, 3 em 2024, 3 em 2025, 3 em 2026; **14 municípios nunca aparecem** em
  2022-2026, todos no interior, com população mediana de 12,4 mil habitantes (`03_populacao_por_coorte.csv`).
  *Sensibilidade:* o resolvedor mais simples de `03_metodos_presenca_municipal.py` (sem reparo de
  transbordamento de célula) dá 39/44/31/31/43 municípios por ciclo e coortes 39/15/3/4/3, com os mesmos 14
  nunca presentes. Para o artigo vale o canônico.
- **Captadores de 2025** (`03_captados_perfil_territorial.csv`): dos 63, 48 casam por título exato com a
  lista de habilitados e 42 têm um único município; entre estes, 61,3% do captado (R$ 9,9 de R$ 16,2 mi)
  fica na RMGV (24 projetos) e 38,7% no interior (18). Com o casamento secundário: 61,8%. O licc.gov,
  com outro casamento, chegou a 66,4% (`notas/politica/02-licc-gov-sintese.md`, § 2.2).

## 6. Proponentes: recorrência, concentração e natureza jurídica

Tabelas: `03_proponentes_recorrencia.csv`, `03_proponentes_por_ciclo.csv`, `03_proponentes_natureza*.csv`,
`03_proponentes_ranking.csv`. **Identidade do proponente = chave normalizada do nome** (os anexos não
publicam CPF/CNPJ do proponente); grafias diferentes da mesma entidade foram unificadas pela regra de
`01_carregar.py` e estão listadas na coluna `variantes` do ranking.

- **235 proponentes distintos** em 2022-2026 (463 processos). Recorrência: 159 (67,7%) aparecem em um só
  ciclo e somam 33,0% do valor autorizado; 36 em dois ciclos (19,6% do valor); **40 (17,0%) em três ou mais
  ciclos concentram 47,4% do valor**; 4 aparecem nos cinco ciclos.
- **Incumbência crescente:** a parcela de proponentes do ciclo que já tinham aparecido em ciclo anterior
  sobe de 25% (2023) para 41% (2024), 63% (2025) e 51% (2026); a parcela do valor que vai a eles, de 33% para
  51%, 74% e 63%. Parte disso é mecânica (em 2023 só havia um ciclo anterior para olhar), mas o nível de
  2025-2026 indica uma carteira que se renova pouco.
- **Concentração por proponente é moderada:** HHI entre 145 e 297 por ciclo, Gini entre 0,28 e 0,40, dez
  maiores com 25% a 44% do valor do ciclo; o limite de 3 projetos por agente (art. 13) e o teto por projeto
  limitam a concentração individual. No agregado 2022-2026, os dez maiores somam 18,8%; o maior (Puri
  Produções e Eventos) 2,4%.
- **Natureza jurídica inferida do nome** (sufixo societário, termos como "associação", "instituto",
  "MEI"; regras em `03_proponentes_natureza_regras.csv`; não é cadastro): empresas com sufixo explícito
  37,4% dos proponentes e 45,1% do valor; associações/institutos/fundações 34,0% e 41,3%; MEI/empresário
  individual 11,1% e 3,4% (valor mediano por processo R$ 162 mil, contra R$ 494 mil das empresas);
  indeterminados 6,0%. [VERIFICAR a natureza no CNPJ quando houver chave.]
- **Limite de 3 projetos por agente (art. 13):** proponentes com 3 ou mais registros num ciclo: 4 (2022), 6
  (2023), 7 (2024), 3 (2025), 1 (2026); máximo de 5 registros de um proponente num ciclo (2024). O art. 13
  limita **inscrições** por ano e alcança CNPJs com o mesmo quadro societário, que o dado não observa; os
  registros de 2024 e 2025 vêm de anos de protocolo diferentes. **Cumprimento indeterminado** (regra 3).

## 7. Captação 2025: projetos e patrocinadores

Tabelas: `03_captados_resumo.csv`, `03_captados_por_ciclo_habilitacao.csv`, `03_captados_natureza.csv`,
`03_patrocinadores*.csv`, `03_captados_patrocinadores_por_projeto.csv`. Fonte: anexo "RECURSO FINANCEIRO
CAPTADO - 2025" (63 projetos, 95 termos de patrocínio com CNPJ e valor).

- **O teto amarrou:** R$ 25.000.000,00 captados (a soma dos 95 termos bate ao centavo) contra
  R$ 27.802.174,47 autorizados para esses 63 projetos (89,9%). 47 captaram 100% do autorizado; 16 parcialmente
  (razão mediana 52%); 2 captaram menos de 35% do autorizado no ano (mínimo 4,1%) — o anexo mede o ano
  calendário, não o prazo do projeto, então isso não indica descumprimento do art. 47 [VERIFICAR].
- **Seleção na variável de resultado:** o anexo só lista quem captou; os 89,9% são condicionais a ter
  captado. A conversão habilitado → captado se mede no § 2.
- **Defasagem habilitação → captação** (casamento por título exato): 33 projetos habilitados no ciclo 2024
  (R$ 12,9 mi), 11 no ciclo 2023 (R$ 4,0 mi), só 4 no ciclo 2025 (R$ 1,9 mi) e 15 sem casamento exato
  (R$ 6,3 mi). O dinheiro de um ano financia sobretudo quem foi habilitado no ano anterior.
- **Patrocinadores: 26 empresas** (raiz de CNPJ; 46 estabelecimentos; 32 grafias de nome).
  **EDP Espírito Santo (distribuidora de energia) = 43,9%** da renúncia, em 25 projetos; CR4 = 74,8%;
  CR8 = 88,7%; HHI = 2.313 (equivalente a 4,3 empresas iguais); Gini = 0,75; **2 empresas somam metade**.
- **Macrossetor inferido do nome** (confiança alta para 18 das 26, média para 3, baixa para 5; `03_patrocinadores.csv`): energia e gás,
  serviços regulados (EDP, ES Gás, TAG) = 51,8%; comércio de veículos e autopeças = 26,1%; distribuição
  atacadista = 12,5%; indústria = 6,9%; supermercados = 2,8%. [VERIFICAR CNAE na Receita Federal.]
- **Um patrocinador por projeto é a regra:** 47 projetos com 1 empresa, 9 com 2, 7 com 3.
- **Quem capta, por natureza inferida:** associações/institutos/fundações 32 projetos e 55,7% do captado;
  empresas 27 projetos e 40,7%; MEI 1 projeto (0,6%).

## 8. Evidências para avaliar o desenho

Síntese do que os dados permitem afirmar, na linguagem da avaliação de desenho (TIP1 p.20 [s.19]; perguntas
da seção 2.3 de `notas/disciplina/01-slides-e-guias.md`). Cada item diz o elo da teoria da mudança a que se
refere.

1. **Excesso de demanda e racionamento privado (insumo → produto).** Autorizado por ciclo de 1,3 a 1,9 vezes
   o teto do ano seguinte; em 2025 a captação esgotou o teto ao centavo (§ 1, § 7). Quem define os projetos financiados, entre
   os habilitados, são as empresas.
2. **Atrito crescente na captação (produto).** 16% → 30% → 45% de expirados entre os resolvidos de 2022 a
   2024 (§ 2).
3. **Seleção pelo patrocinador favorece projetos maiores e proponentes recorrentes (produto → resultado).**
   Gradiente de conversão por valor dentro do ciclo (27% × 78% em 2024); incumbência de 51-63% dos
   proponentes nos ciclos recentes (§ 2, § 6).
4. **Teto por projeto vinculante (regra de desenho).** 27% dos processos no teto exato e 46% entre R$ 490 e
   500 mil (§ 4).
5. **Concentração territorial acima da populacional e da econômica (resultado distributivo).** Gini 0,88;
   Vitória com 48% do valor e 8% da população; 14 municípios nunca presentes (§ 5).
6. **A cota fora da RMGV age sobre a menor parte da desigualdade** (Theil entre grupos = 7%) e seu
   cumprimento na captação é indeterminado (§ 3, § 5).
7. **Concentração do financiamento privado em poucos contribuintes, sobretudo serviços regulados.** EDP com
   44% da renúncia de 2025 (§ 7). Como o crédito é integral, a decisão de alocação é privada, mas o recurso é
   público (ver `notas/politica/01-desenho-legal.md`).
8. **Monitoramento insuficiente para avaliar resultados.** Não há, nos anexos: CNPJ/CPF do proponente,
   linguagem/segmento, sede, rateio entre municípios, inscritos inabilitados, captação por cota, datas de
   captação e execução, nem qualquer indicador de resultado (público, gratuidade, emprego). O desenho de
   monitoramento cobre insumo e produto, não resultado.

## 9. Hipóteses

Hipóteses geradas pelos descritivos, para a teoria da mudança e a proposta de avaliação (não são achados
causais):

- **H1 (seleção por visibilidade/porte).** Empresas patrocinam projetos maiores, consolidados e de
  proponentes com histórico, porque o retorno de imagem é maior e o custo é zero (crédito integral). Teste
  descritivo possível: conversão por valor, recorrência e cota I (eventos calendarizados), já esboçado no § 2.
- **H2 (incumbência).** Ter captado num ciclo aumenta a chance de captar no seguinte (rede com patrocinador).
  Teste: painel de proponentes 2022-2026 com chave estável.
- **H3 (teto vinculante e sobrepedido).** O teto por projeto induz pedidos no máximo, independentemente do
  custo do projeto; o valor total declarado é ajustado ao teto (75% com autorizado = total).
- **H4 (concentração mecânica dos patrocinadores).** O limite de aporte de cada contribuinte é uma fração do
  ICMS devido (Lei 7.000/2001, art. 5º-B, IX, b); grandes contribuintes (energia) dominam por tamanho do
  imposto, não por preferência cultural.
- **H5 (reprodução da desigualdade de capacidade).** Municípios sem fundo, plano ou equipamento de cultura
  (MUNIC 2021; `notas/politica/03-contexto-problema.md`, § 1.3) não geram proponentes habilitados; a LICC
  reproduz a distribuição prévia de capacidade.
- **H6 (adicionalidade parcial).** Parte dos projetos patrocinados, sobretudo eventos consolidados, ocorreria
  com outra fonte (patrocínio direto, Rouanet, editais); o efeito causal da captação é menor que o valor
  captado.

## 10. Limitações e itens [VERIFICAR]

- Legenda oficial dos quatro estados da lista de habilitados; data de corte da versão de 10/09/2026.
- Significado de "ANO X" (exercício de habilitação × ano de captação pretendida).
- Tetos de 2023, 2024 (ato de ampliação) e 2026 na norma primária; 2025 conferido pela soma captada.
- Cinco registros com autorizado > total e quatro valores de R$ 500,00 (p. 12 do PDF de habilitados).
- Natureza jurídica e setor dos patrocinadores inferidos do nome, sem consulta ao CNPJ/CNAE.
- Identidade do proponente por nome: fusões indevidas ou grafias não unificadas mudam a recorrência.
- Valor territorial só para processos com um único município (74% do valor); presença não é valor.
- Local de execução não é sede; a cota III não é apurável.
- O anexo de captados cobre só 2025 e só quem captou; não há captação por projeto nos demais anos.
- 15 dos 63 captadores de 2025 sem casamento exato com a lista de habilitados (6 ambíguos, 9 sem
  correspondência); o casamento secundário só entra em sensibilidade.
- `03d_licc_escala_icms.py` lê os CSV brutos e inclui os quatro valores suspeitos de R$ 500 (diferença de
  R$ 1.500 no autorizado de 2024 em relação a `03_anual.csv`); para o artigo valem os números do
  `03_descritivas.py`.
