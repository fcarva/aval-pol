# Síntese do repositório licc.gov (o que já foi feito e pode ser aproveitado no artigo)

> Nota de trabalho (aval-pol), escrita em 23/09/2026. Absorve a cópia local do repositório
> `fcarva/licc.gov` guardada em `licc-gov/` (documentação, histórico de commits e código-chave)
> e os dados herdados em `dados/licc/`. Os números foram **recalculados em Python** por
> `analise/licc_gov_indicadores_replicacao.py` (tabelas `analise/tabelas/licc_gov_*.csv`), para
> que cada estatística do artigo aponte um script deste repositório, e não só o código TypeScript
> do licc.gov, que não roda aqui.
> Status: seções 0 a 7 completas (gravação incremental).

## 0. Como ler esta nota

**O que é o licc.gov.** Um catálogo relacional em grafo da LICC, construído entre 26/08 e
03/09/2026 (commits `84aeda1` a `78163a4`, `licc-gov/historico-git.txt`) no molde do *SF
Government Graph* do CivLab. Ele organiza entidades tipadas (órgãos, empresas, proponentes,
projetos, municípios, normas) ligadas por relações nomeadas, e ancora cada entidade na norma que a
institui (`licc-gov/README-licc.md`, l. 1-9; `licc-gov/docs/ontologia.md`, l. 1-14). Não é sítio
oficial da SECULT-ES (`README-licc.md`, l. 11-12). Para o artigo ele contribui com quatro coisas:
(i) os dados transcritos dos anexos oficiais, (ii) quatro indicadores já definidos, (iii) uma
ontologia de atores e relações que descreve o arranjo institucional e (iv) um catálogo de
armadilhas de dados já descobertas. Metade do repositório trata da interface web (cores, anéis,
abas) e **não interessa ao artigo**. `docs/referencia-civlab.md` e a maior parte de
`docs/referencias.md` são desse tipo e só aparecem aqui quando explicam uma decisão de modelagem.

**Siglas de origem usadas abaixo** (todas as linhas citadas foram lidas nesta sessão):

| Sigla | Arquivo |
| --- | --- |
| CL | `licc-gov/CLAUDE-licc.md` |
| RD | `licc-gov/README-licc.md` |
| ONT | `licc-gov/docs/ontologia.md` |
| PIPE | `licc-gov/docs/pipeline.md` |
| ANX | `licc-gov/docs/anexos-secult-README.md` |
| GIT `hash` | `licc-gov/historico-git.txt`, mensagem do commit indicado |
| IND | `licc-gov/codigo/src_lib_indicadores.ts` |
| BG | `licc-gov/codigo/pipeline_build-graph.ts` |
| HAB | `licc-gov/codigo/pipeline_habilitados.ts` |
| LEG | `licc-gov/codigo/src_ontology_legal.ts` |
| NOS / ARE / MUN / SEG | `licc-gov/codigo/src_ontology_{nodes,edges,municipios,segmentos}.ts` |
| PG-IND / PG-SOB / PG-ORC | `licc-gov/codigo/app_{indicadores,sobre,orcamento}_page.tsx` |
| REP | `analise/licc_gov_indicadores_replicacao.py` (esta tarefa) e as tabelas `analise/tabelas/licc_gov_*.csv` que ele grava |

**Três selos de confiança** usados nas tabelas:
- **replicado**: recalculado por REP a partir de `dados/licc/` e igual ao número do licc.gov;
- **divergente**: recalculado por REP e diferente do que o licc.gov registrou (a diferença é explicada);
- **só licc.gov**: afirmação do licc.gov que não dá para recalcular com os arquivos locais (em geral
  depende de PDF não baixado); vale como pista, e vai com [VERIFICAR] quando for para o artigo.

**Regras herdadas que valem para o artigo** (CL l. 25-40, 62-71; `CLAUDE.md` do projeto):
ausência não é zero; todo número tem proveniência; "li a norma" não significa "consigo apurar o
cumprimento"; captados ≠ habilitados; as cotas do art. 18 são quatro.

## 1. Fatos e números já estabelecidos (com cobertura e origem)

### 1.1 Norma, teto e calendário

| Fato | Valor | Origem | Selo |
| --- | --- | --- | --- |
| Base legal | Lei estadual 11.246/2021 alterou a Lei 7.000/2001 (ICMS-ES), criando o crédito presumido para patrocínio cultural | LEG l. 35-64; texto da lei conferido no DIO-ES em `notas/politica/fontes/lei-11246-2021.md` | conferido (fonte primária lida por outra tarefa) |
| Regulamento | Decreto 5.035-R, de 15/12/2021 | LEG l. 100-116 (lá `verificado: false`); texto conferido no DIO-ES em `notas/politica/fontes/decreto-5035-r-2021.md` | conferido por outra tarefa deste repositório; o licc.gov não o tinha lido |
| Instrução normativa de 2025 | IN SECULT nº 001/2025, anexo da oportunidade 1878 do Mapa Cultural ES | LEG l. 136-150; texto integral em `notas/politica/fontes/in-licc-001-2025.md` | conferido |
| Instrução normativa de 2026 | IN nº 001/2026, de 12/01/2026 (número e data pela página da SECULT) | LEG l. 80-99; `notas/politica/fontes/in-licc-001-2026.md` | só a identidade foi conferida pelo licc.gov (LEG l. 88-92) |
| Teto de renúncia 2025 | R$ 25.000.000,00, Portaria SEFAZ nº 01-R, de 07/01/2025 | LEG l. 65-79 e 307-313; RD l. 111 (fonte: notícia da SECULT) | só licc.gov (a portaria não foi lida; `notas/politica/fontes/portaria-conjunta-sefaz-secult-01r-2025.md` adverte para não confundi-la com a Portaria Conjunta 01-R de 21/01/2025) [VERIFICAR] |
| Exercício padrão do licc.gov | 2025, "último ciclo fechado" | LEG l. 291-300; CL l. 332-336 | decisão de projeto |
| Oportunidades no Mapa Cultural ES | 1878 = LICC 2025; 2317 = LICC 2026 | RD l. 114; PIPE l. 182-184 | só licc.gov |
| Inscrições 2026 | até 30/06/2026, só pelo Mapa Cultural | RD l. 113; LEG l. 87 | só licc.gov (fonte: notícia SECULT) |
| Cotas do art. 18 da IN 001/2025 | I 30% eventos calendarizados com mais de 10 anos; II 10% planos plurianuais (formação continuada, manutenção de equipamentos, corpos estáveis); III 10% projetos com sede do agente **e** locais de execução fora da RMGV; IV 50% demais | LEG l. 190-242; GIT `c757274` (l. 364-374); texto conferido em `fontes/in-licc-001-2025.md` l. 363-383 | conferido |
| Regra do art. 18, §§ 1º e 2º | esgotadas as reservas I-III, aplica-se a IV; sem captação suficiente, o remanescente pode ser remanejado a critério da SECULT | `fontes/in-licc-001-2025.md` l. 379-383 | conferido. **O licc.gov não modelou estes parágrafos** (ver § 4) |
| Limite por proponente | até 3 projetos por ano por agente cultural; o parágrafo único estende o limite a "CNPJs que tenham o mesmo quadro societário" | licc.gov: LEG l. 243-257, `verificado: false`, citado da LegisWeb para a IN 2026. Texto de 2025 conferido: `fontes/in-licc-001-2025.md` l. 327-331 (art. 13) | conferido agora para 2025; o `naoApuravel` continua valendo (§ 4) |
| RMGV (define a cota III por exclusão) | 7 municípios: Cariacica, Fundão, Guarapari, Serra, Viana, Vila Velha, Vitória | MUN l. 25-39; ONT l. 159-161 | lista normativa segundo o licc.gov; a base legal da lista não é citada no código [VERIFICAR a lei complementar da RMGV] |
| Microrregiões | 10 regiões de planejamento, "agrupamento de leitura" (o recorte varia conforme a fonte) | MUN l. 13-23, 134-140; RD l. 191-192 | uso descritivo, não normativo |

### 1.2 Captação de 2025 (anexo "RECURSO FINANCEIRO CAPTADO 2025")

Arquivo: `dados/licc/oficial/captados-2025.csv` (63 linhas). O licc.gov o transcreveu com
`tools/anexos-secult/extrair-captados.mjs` (CL l. 338-350; GIT `acb3530`).

| Fato | Valor | Cobertura | Origem | Selo |
| --- | --- | --- | --- | --- |
| Projetos que captaram em 2025 | 63 | 63/63 | CL l. 345; `stats.json` | replicado (REP) |
| Proponentes | 52 vértices no grafo; 55 grafias distintas no CSV | 63/63 | CL l. 346; REP | replicado; a diferença vem da identidade por slug do nome (§ 4.2) |
| Empresas patrocinadoras | 28 pelo nome (licc.gov); **26 pela raiz do CNPJ** | 95/95 termos | CL l. 347; REP → `licc_gov_concentracao_por_raiz_cnpj.csv` | **divergente**: TAG e Kurumá aparecem duas vezes cada no grafo com o mesmo CNPJ (§ 4.2) |
| CNPJs de estabelecimento | 46 | 95/95 | CL l. 347; REP | replicado |
| Termos de patrocínio | 95 (86 arestas `patrocina` depois de somar termos da mesma empresa no mesmo projeto) | — | CL l. 348; REP | replicado |
| Termos por projeto | 1 termo: 45 projetos; 2: 8; 3: 6; 4: 4 | 63/63 | REP → `licc_gov_indicadores_resumo.csv` | calculado agora |
| Valor autorizado (soma dos tetos por projeto) | R$ 27.802.174,47 | 63/63 | CL l. 349; `stats.json` | replicado |
| Valor captado | **R$ 25.000.000,00, o teto inteiro**; bate com os totais impressos no anexo | 63/63 | CL l. 350; ANX l. 86-88; GIT `c757274` l. 360-362 | replicado (a soma dos 95 termos dá exatamente R$ 25.000.000,00) |
| Comprometimento do teto (autorizado/teto) | 111,2% | — | `stats.json` (`comprometimentoDoTeto` = 1,1121) | replicado. "Não é erro": a SECULT habilita mais teto do que há renúncia e a disputa por patrocinador decide quem capta (CL l. 355-357) |
| Execução (captado/autorizado) | 89,9% | 63/63 | `stats.json` (`execucao` = 0,8992) | replicado |
| Projetos que captaram 100% do autorizado | 47 de 63; mediana da taxa por projeto = 100%; mínimo = 4,1% | 63/63 | REP | calculado agora |
| Captado acima do autorizado | 0 projetos (conferidor do extrator; captar acima do teto é impossível) | 63/63 | ANX l. 90-92; REP | replicado |
| Valor autorizado por projeto | mediana R$ 499.620; máximo R$ 500.000 (teto do art. 14 da IN 001/2025) | 63/63 | REP; `fontes/in-licc-001-2025.md` l. 333-341 | calculado agora |
| Página do anexo | p. 1: 12 projetos; p. 2: 13; p. 3: 17; p. 4: 19; p. 5: 2 | 63/63 | coluna `fonte_pagina` | — |

### 1.3 Habilitação 2022-2026 (anexo "LISTA DE PROJETOS HABILITADOS")

Arquivos: `dados/licc/habilitados/habilitados-{2022..2026}.csv`, 467 linhas. Vieram de **uma lista
contínua** com cinco seções, uma por ciclo, cada uma com a quantidade declarada no próprio anexo
(88, 74, 123, 113, 69 para 2026 a 2022), e todas as cinco fecharam com a contagem declarada
(GIT `78163a4`, l. 44-49).

| Ciclo | Projetos | `enquadramento` preenchido | `municipio` preenchido | `valor_autorizado` preenchido |
| --- | --- | --- | --- | --- |
| 2022 | 69 | 0 | 69 | 69 |
| 2023 | 113 | 0 | 113 | 112 |
| 2024 | 123 | 123 | 121 | 123 |
| 2025 | 74 | 74 | 58 | 74 |
| 2026 | 88 | 88 | 88 | 88 |

Origem: REP → `analise/tabelas/licc_gov_inventario_colunas.csv`. **O enquadramento na cota do
art. 18 só existe a partir do ciclo 2024**; os ciclos 2022 e 2023 não o trazem (o licc.gov já
tinha notado que os "enquadramentos" de 2022/2023 eram números de página lidos por engano:
CL l. 149-151).

Situação publicada (coluna `status`) por ciclo (REP → `licc_gov_habilitados_status_enquadramento.csv`):

| Ciclo | concluído | em execução | captando | captação expirada |
| --- | --- | --- | --- | --- |
| 2022 | 58 | 0 | 0 | 11 |
| 2023 | 70 | 9 | 0 | 34 |
| 2024 | 41 | 20 | 12 | 50 |
| 2025 | 7 | 46 | 18 | 3 |
| 2026 | 2 | 17 | 69 | 0 |

É um retrato na data de publicação da lista, que o CSV não registra [VERIFICAR a data de
atualização da página `https://secult.es.gov.br/lista-de-projetos-habilitados`]. Não é conversão
definitiva: um projeto "captando" em 2025 ou 2026 ainda pode captar ou expirar.

Enquadramento por ciclo (mesma tabela): 2024: 86 demais, 16 eventos calendarizados, 17 fora da
RMGV, 4 plurianuais; 2025: 40, 17, 13, 4; 2026: 56, 14, 12, 6.

### 1.4 Casamento entre os dois anexos

| Fato | Valor | Origem | Selo |
| --- | --- | --- | --- |
| Ciclo de habilitação dos 63 que captaram em 2025 | 30 na seção de 2024, 14 na de 2023, **só 4 na de 2025** | CL l. 130-136; GIT `78163a4` l. 9-13 | só licc.gov (o casamento dele) |
| Resultado do casamento do licc.gov | 40 por título exato; 4 ambíguos (mesmo título em mais de um ciclo); 18 sem correspondência | CL l. 375-382 | só licc.gov. 40+4+18 = 62, não 63: falta um projeto na conta [VERIFICAR] |
| Casamento refeito por REP (título sem acento e sem pontuação, igualdade exata) | 49 únicos (2024: 34; 2023: 11; 2025: 4), 6 ambíguos, 8 sem correspondência | REP → `licc_gov_casamento_captados.csv` | **divergente** porque a normalização é mais tolerante; os 9 casamentos a mais precisam de conferência manual antes de uso [VERIFICAR] |
| Consequência no grafo | 41 projetos com `numeroProcesso`, 40 com local de execução, 31 com cota (`cotaId`) | `graph.json`; `stats.json` (`cobertura`) | replicado |

Leitura: a captação de um ano calendário financia sobretudo projetos habilitados em ciclos
anteriores. Isso importa para o desenho da avaliação (o "tratamento" chega com defasagem de um a
dois anos em relação à habilitação) e está registrado como regra 4 do `CLAUDE.md` do projeto.

### 1.5 Território, capital, proponentes e cobertura (exercício 2025)

Todos sobre os 63 projetos que captaram em 2025; detalhes e fórmulas no § 2.

| Fato | Valor | Cobertura | Origem | Selo |
| --- | --- | --- | --- | --- |
| Projetos com local de execução | 40 de 63 (63%) | 40/63 | `stats.json`; CL l. 359-362 | replicado |
| Projetos com um único município (valor atribuível) | 37 de 63 | 37/63 | REP | calculado agora |
| Municípios com ao menos um projeto | 19 de 78 | 40/63 | `stats.json` (`totalMunicipiosAtendidos`) | replicado |
| Municípios sem nenhum projeto | 59 de 78 | 40/63 | CL l. 365-366 | replicado |
| Captado atribuído à RMGV (7 municípios) | R$ 9.538.391,67 (66,4% do atribuído) | 37/63 | CL l. 365; REP | replicado ("R$ 9,5 mi") |
| Captado atribuído ao interior (71 municípios) | R$ 4.830.727,38 | 37/63 | idem | replicado ("R$ 4,8 mi") |
| Captado com município atribuído | R$ 14.369.119,05 (57,5% dos R$ 25 mi); **R$ 10.630.880,95 sem município atribuível** | 37/63 | GIT `78163a4` l. 41-42 ("R$ 14,4 mi"); REP | replicado |
| Gini territorial do captado (78 municípios, zeros incluídos) | 0,921 | 37/63 | CL l. 366; REP | replicado |
| Gini do aporte por empresa | 0,742 (28 empresas por nome); 0,748 (26 por raiz de CNPJ) | 95/95 termos | GIT `acb3530` l. 282-284; REP | replicado / variante calculada agora |
| Maior patrocinadora | EDP Espírito Santo: R$ 10.975.277,24 = **43,9%** da renúncia, em 25 dos 63 projetos | 95/95 | GIT `acb3530` l. 282-284; REP | replicado |
| Empresas que somam metade do aporte | 2 | 95/95 | REP | calculado agora |
| Três maiores empresas | 65,1% (por nome) ou 66,1% (por raiz de CNPJ: EDP, Kurumá, VD) | 95/95 | REP | calculado agora |
| Projetos com linguagem cultural | **0 de 63** | 0/63 | CL l. 362-363; `stats.json` | replicado. Nenhum anexo publica linguagem; derivá-la do título "seria inferência vestida de dado" (CL l. 363) |
| Proponentes por número de projetos captados | 42 com 1; 9 com 2; 1 com 3 (Caju Produções LTDA ME) | 52/52 | `stats.json` (`proponentesNoLimite`); REP | replicado |
| Proponentes com natureza jurídica conhecida | 0 de 52 | 0/52 | REP | calculado agora: os CSVs não têm CPF/CNPJ do proponente, então a natureza (PF/PJ) não é derivável (HAB l. 671-684) |
| Projetos com cota classificada pela SECULT | 31 de 63: 16 demais, 7 eventos calendarizados, 4 plurianuais, 4 fora da RMGV | 31/63 | `stats.json`; REP | replicado |
| Situação publicada dos 63 | 30 concluídos, 10 em execução, 23 sem status | 40/63 | inspeção de `graph.json` (`meta.status` dos projetos, herdado da lista de habilitados) | calculado agora |

### 1.6 O artefato do grafo

| Fato | Valor | Origem |
| --- | --- | --- |
| Tamanho | 246 vértices, 496 arestas, exercício 2025, gerado em 03/09/2026 12:30 UTC | `dados/licc/graph.json` (`meta`) |
| Proveniência | oficial 536, derivado 206, demonstração 0 | `graph.json` `meta.contagemPorProveniencia`. CL l. 352-353 registra 533/159 e GIT `9c19ea1` registra 535/159: **números de antes** do commit `78163a4`, que acrescentou as 47 arestas `ocorre_em` (derivadas: 159 + 47 = 206). A diferença de 1 no oficial (535 → 536) não foi rastreada |
| Dados de demonstração | nenhum resta; a faixa de aviso sumiu | CL l. 338, 352-353 |
| Seed de demonstração | 82 projetos fictícios com nomes em letras gregas. PIPE chama o 82 de "contagem oficial de habilitados da LICC 1 em 2026", mas o commit `13b1734` corrigiu isso: o número serve só para calibrar ordem de grandeza. **Não deve ser citado** | PIPE l. 224-237; GIT `13b1734` l. 771-777 |

## 2. Os quatro indicadores

**Regra comum** (IND l. 1-40): todo indicador viaja com o denominador, na estrutura
`Confianca = {base, universo, cobertura = base/universo}`, e a função devolve `null` quando nenhum
registro tem o campo exigido ("não existe indicador sobre zero observações"). A página
`/indicadores` abre com um painel de cobertura campo a campo antes de qualquer gráfico
(PG-IND l. 410-504): sobre os 63 projetos de 2025, 63 de fonte oficial, 63 com valor autorizado,
63 com valor captado, 40 com município, **0 com linguagem cultural** e 63 com patrocinador
(`stats.json`, `cobertura`). Os quatro indicadores foram criados no commit `04a8598` e passaram
a ler dado real no `acb3530` (capital) e no `78163a4` (território).

Todos os resultados abaixo foram recalculados por REP (`analise/tabelas/licc_gov_indicadores_resumo.csv`).

### 2.1 Concentração do capital: "quem banca a cultura capixaba"

- **Definição** (IND l. 44-128): distribuição do aporte **efetivo** por empresa patrocinadora.
  A base são as arestas `patrocina` com peso, e o peso é a soma dos termos de patrocínio da
  empresa naquele projeto; não se usa o teto do projeto. Empresa sem aporte com valor publicado
  sai da conta mas fica no denominador.
- **Fórmulas.** Com $a_j$ o aporte da empresa $j$ e $A = \sum_j a_j$: fração $f_j = a_j/A$ e
  fração acumulada em ordem decrescente. Gini pela diferença média relativa, com $x_{(1)} \le \dots \le x_{(n)}$:
  $G = \dfrac{\sum_{i=1}^{n} (2i - n - 1)\, x_{(i)}}{n \sum_i x_i}$, e $G = 0$ se $n < 2$ (IND l. 130-146).
  "Empresas para metade" é o menor $k$ com acumulado $\ge 0{,}5$; mede-se também a fração das três maiores.
- **Resultado (2025).** 28 empresas (confiança 28/28), R$ 25.000.000,00 aportados; **Gini 0,742**;
  **2 empresas** respondem por metade do aporte; três maiores = 65,1%; EDP Espírito Santo = 43,9%
  em 25 projetos; seguem Kurumá Veículos (10,8%, 11 projetos), VD Comércio de Veículos (10,4%, 10)
  e Realmar Distribuidora (8,7%, 7) (REP → `licc_gov_concentracao_capital.csv`). Agrupando pela
  raiz do CNPJ (26 empresas), o Gini vai a 0,748 e as três maiores a 66,1%
  (`licc_gov_concentracao_por_raiz_cnpj.csv`).
- **Cautelas para o artigo.** (a) É concentração **entre quem patrocinou**; os contribuintes de
  ICMS que poderiam patrocinar e não o fizeram não estão no dado. (b) A fórmula é o Gini
  "populacional", sem a correção $n/(n-1)$ para amostra pequena; com $n = 28$ a versão corrigida
  daria cerca de 0,770 (cálculo aritmético sobre o 0,742, não reportado pelo licc.gov). (c) O
  aporte possível de cada contribuinte é limitado por percentuais do saldo devedor de ICMS por
  faixas (Lei 11.246/2021, art. 5º-B, IX, "b", em `fontes/lei-11246-2021.md`). Portanto parte da
  concentração pode ser mecânica, reflexo do tamanho do imposto devido. Isso é hipótese a
  testar, não achado do licc.gov.

### 2.2 Desigualdade territorial: "para onde o recurso chega"

- **Definição** (IND l. 148-260): distribuição do captado entre **os 78 municípios**, inclusive
  os que não receberam nada ("o zero é o dado", IND l. 180-182).
- **Regra de atribuição** (IND l. 192-199; BG l. 173-184; HAB l. 527-538). A *presença* de um
  projeto conta em todos os municípios que a fonte nomeia (`municipiosIds`). O *valor* só é
  atribuído quando a fonte nomeia um único município (`municipioId`), porque o rateio entre
  municípios não é publicado e somar o valor cheio em cada um contaria a mesma renúncia várias vezes.
- **Medidas.** Para RMGV (7 municípios) e interior (71): número de municípios, presenças e
  captado atribuído. Também: municípios sem projeto; `fracaoNaRmgv` = captado RMGV / captado
  atribuído; Gini do captado sobre os 78 municípios, zeros incluídos. A confiança é a presença
  (projetos com local / projetos).
- **Resultado (2025).** Confiança 40/63 para presença e 37/63 para valor. RMGV: R$ 9.538.391,67
  e 30 presenças; interior: R$ 4.830.727,38 e 17 presenças; **66,4% do valor atribuído ficou na
  RMGV**; **59 dos 78 municípios** sem projeto; **Gini 0,921**. Vitória sozinha tem 16 projetos e
  R$ 5,93 mi. Quatro municípios (Cachoeiro de Itapemirim, Guarapari, Linhares, Serra) aparecem só
  por presença em projeto multimunicipal, com valor atribuído zero (REP → `licc_gov_territorio_municipios.csv`).
- **Cautelas.** (a) A fração de 66,4% é sobre R$ 14,37 mi; **R$ 10,63 mi (42,5% da captação) não
  têm município atribuível**, então o retrato territorial é parcial. (b) O município publicado na
  lista de habilitados é o **local de execução**, não a sede do proponente (HAB l. 70-74), e a cota
  III do art. 18 exige as duas coisas fora da RMGV. Logo este indicador não apura a cota.
  (c) O licc.gov não normaliza por população; uma versão per capita exigiria população do IBGE
  (sugestão, não feito). (d) "Não é comparável ao Gini do capital: são desigualdades de naturezas
  diferentes" (PG-IND l. 164-166; IND l. 183-186): o territorial inclui os municípios sem nenhum
  projeto; o do capital só inclui as empresas que patrocinaram.

### 2.3 Conversão de autorizado em captado: "quanto da autorização virou dinheiro"

- **Definição** (IND l. 262-370): taxa captado/autorizado. "Autorização não é recurso": a LICC dá
  ao projeto um teto de captação, e cabe ao proponente convencer uma empresa contribuinte a
  aportar (IND l. 289-300; PG-IND l. 176-177). Só entram projetos com **os dois** valores
  publicados. "Captou zero" (publicado) é separado de "captação não publicada"; assumir zero
  "fabricaria um fracasso que a fonte não afirma" (PG-IND l. 184-189).
- **Fórmulas.** Taxa geral $= \sum \text{captado} / \sum \text{autorizado}$ sobre os projetos
  completos; taxa por linguagem e por proponente; os 8 proponentes de menor taxa; contagens
  `naoCaptaram` (captado = 0 publicado) e `captacaoDesconhecida`. A confiança é completos / projetos.
- **Resultado (2025).** 63/63 completos; R$ 25,0 mi de R$ 27,8 mi = **89,9%**; `naoCaptaram` = 0;
  `captacaoDesconhecida` = 0; por linguagem: **vazio** (segmento 0%); 47 dos 63 captaram 100% do
  autorizado; taxa mínima 4,1% (REP).
- **Cautela central para o artigo: seleção na variável de resultado.** O anexo "RECURSO FINANCEIRO
  CAPTADO" só lista quem captou algo no ano. Por construção ninguém ali tem captação zero, e os 89,9%
  são uma taxa **condicional a ter captado**, misturando projetos de três ciclos (§ 1.4). Não é a
  conversão "habilitado → captado". Essa conversão se mede na lista de habilitados, pela situação
  `captacao_expirada`: 11 de 69 no ciclo 2022, 34 de 113 em 2023, 50 de 123 em 2024, com ciclos
  ainda abertos a partir de 2024 (§ 1.3). O indicador do licc.gov, portanto, não mede a margem
  extensiva, que é justamente o ponto crítico do desenho (quem não consegue patrocinador).

### 2.4 Quem executa: perfil e reincidência dos proponentes

- **Definição** (IND l. 372-479). (a) Proponentes e projetos por natureza jurídica, inferida só
  pelo documento: 11 dígitos = pessoa física, 14 = pessoa jurídica. O CNPJ não distingue empresa,
  ONG ou prefeitura, e classificar pela palavra "instituto" no nome "seria classificar por
  adivinhação" (HAB l. 671-684). (b) Distribuição de quantos projetos cada proponente tem no
  exercício. (c) `noLimite`: proponentes com número de projetos ≥ limite da norma (3). A
  confiança é proponentes com natureza / proponentes.
- **Resultado (2025).** Natureza: **0 de 52** (os CSVs não trazem CPF/CNPJ do proponente, então o
  painel "por natureza" sai vazio). Distribuição: 42 proponentes com 1 projeto, 9 com 2, 1 com 3
  (Caju Produções LTDA ME), que é o único "no limite" (REP; `stats.json`, `proponentesNoLimite`).
- **Dois selos independentes na regra do limite** (IND l. 403-418; LEG l. 153-182): `verificado`
  ("li a norma?") e `naoApuravel` ("consigo apurar o cumprimento?"). Com `verificado: false` a tela
  diz que a lista mostra "quem alcançou o número, não quem descumpriu a norma"; com
  `verificado: true` e `naoApuravel`, diz que a regra foi conferida mas o cumprimento não é
  apurável (PG-IND l. 262-283).
- **Cautelas.** (a) O art. 13 da IN 001/2025 limita a **inscrição** (`fontes/in-licc-001-2025.md`
  l. 327-331). O dado disponível é de projetos que **captaram** num ano calendário, vindos de
  ciclos diferentes, então nem a contagem individual corresponde ao objeto da regra. (b) O
  parágrafo único alcança CNPJs com o mesmo quadro societário, que o dado não observa (§ 4.3).

### 2.5 Conferência das cotas do art. 18 (não é um dos quatro, mas mora ao lado)

- **Cálculo** (BG l. 283-348): para cada cota $r$, reservado $= 25\,\text{mi} \times$ cota;
  alocado $= \sum$ **valor autorizado** dos projetos com `cotaId = r`. `cotaId` é a coluna
  "Enquadramento para efeito de captação" da lista de habilitados, "lida, não deduzida"
  (BG l. 294-307; HAB l. 76-83). O estado tem três valores e é **assimétrico**: `atendida = true`
  se alocado ≥ reservado (o piso já prova); `false` só se todos os projetos estiverem
  classificados; senão `null` = "indeterminado" (BG l. 330-344).
- **Resultado (2025)**, todas indeterminadas, com 31 de 63 projetos classificados (`stats.json`):

| Cota (art. 18) | Reservado | Piso alocado (soma do **autorizado**) | Piso/reservado |
| --- | --- | --- | --- |
| I Eventos calendarizados > 10 anos (30%) | R$ 7.500.000 | R$ 3.491.999,84 | 46,6% |
| II Planos plurianuais (10%) | R$ 2.500.000 | R$ 1.999.896,00 | 80,0% |
| III Fora da RMGV (10%) | R$ 2.500.000 | R$ 1.636.345,47 | 65,5% |
| IV Demais (50%) | R$ 12.500.000 | R$ 7.265.241,73 | 58,1% |

- **Cautelas** (ver § 4.3): o piso soma o **autorizado**, não o captado; 32 projetos estão sem
  classificação; e o art. 18, §§ 1º e 2º, permite migrar para a cota IV e remanejar, o que o
  licc.gov não modelou.

## 3. Ontologia: atores e relações (arranjo institucional)

### 3.1 Princípio de modelagem: o grafo segue o dinheiro

No CivLab o cidadão fica no centro porque elege e paga imposto. Na LICC, segundo o licc.gov, o
mecanismo é outro: o Estado **abre mão** de ICMS para que a política exista, e por isso o capixaba
é ao mesmo tempo **financiador indireto e beneficiário final**. Os anéis desenham o **fluxo do
valor**, e não uma taxonomia (CL l. 73-89; ONT l. 16-30; RD l. 16-34):

| Anel | Papel no fluxo | Quem | Categoria |
| --- | --- | --- | --- |
| centro | origem e destino do valor | População capixaba | `publico` |
| 1 · Aprovação e fomento | define diretrizes e o teto | Governo do ES, SECULT, SEFAZ, CEC, CAP | `governanca` |
| 2 · O capital | aloca a renúncia de ICMS | empresas patrocinadoras | `patrocinador` |
| 3 · A execução | realiza o projeto | produtoras, coletivos, OSCs, artistas, prefeituras | `proponente` |
| 4 · O bem público | resultado entregue | projetos, setorizados por linguagem | `projeto` |

Sete categorias ficam fora do fluxo (`anel: null`), porque "existem como entidades e eixos de
leitura, mas não movem nem recebem recurso" (ONT l. 46-59): `segmento` (9 linguagens derivadas da
taxonomia do Mapas Culturais, eixo de leitura e não classificação oficial: SEG l. 21-29),
`municipio` (78, sustentam a cota territorial), `fundamento` (normas), `evento` e `espaco` (agenda
e equipamentos, camada "monitor"), `pessoa` (titular do cargo) e `edital` (a chamada do exercício).
São 12 categorias no total (NOS l. 64-232). Uma decisão registrada: segmento **não** virou anel,
porque isso "alongaria a cadeia de responsabilização com um elo que não move recurso" (GIT `4642fda`,
l. 715-719).

### 3.2 Atores (vértices) e o papel que o licc.gov atribui a cada um

Vértices institucionais presentes em `dados/licc/graph.json` (descrições em NOS e no próprio grafo):

| Vértice (id) | Papel segundo o licc.gov | Fonte citada no grafo | Observação desta nota |
| --- | --- | --- | --- |
| População Capixaba (`publico-es`) | destinatária final; "todo caminho no grafo termina aqui"; financiadora indireta via renúncia | fundamento Lei 11.246 | construção analítica, não ator jurídico |
| Governo do ES (`governo-es`) | Poder Executivo; nomeia o titular da SECULT e os membros do CEC | es.gov.br | — |
| SECULT-ES (`secult-es`) | órgão gestor da LICC: publica a IN do exercício, recebe inscrições pelo Mapa Cultural, conduz a análise documental e de mérito, fiscaliza a execução | secult.es.gov.br/sobre-a-licc | coerente com a Lei 11.246, art. 5º-B, IX, "e" (`fontes/lei-11246-2021.md`) |
| SEFAZ-ES (`sefaz-es`) | autoriza o teto anual de renúncia e controla o crédito presumido apropriado pelas patrocinadoras | Portaria SEFAZ 01-R/2025 | a Lei 11.246, art. 5º-B, IX, "c", atribui o teto a ato do Secretário da Fazenda, limitado a 2% da arrecadação do ano anterior, excluída a parte dos municípios (alínea "a") |
| Conselho Estadual de Cultura (`cec-es`) | "colegiado de participação social na política cultural capixaba" | **nenhuma fonte** | o licc.gov não diz qual é o papel do CEC na LICC. A palavra "conselho" não aparece, com esse sentido, no Decreto 5.035-R, na IN 001/2025, na Lei 11.246 nem no regimento da CAP transcritos em `notas/politica/fontes/` (a única ocorrência é o CONFAZ no decreto). **O CEC não tem papel formal documentado na LICC**; incluí-lo no arranjo exige fonte [VERIFICAR] |
| Comissão (`cap-licc`) | chamada de "Comissão de **Análise de Projetos**": delibera após análise documental e parecer de mérito, aprovando, convertendo em diligência ou inabilitando | oportunidade 1878 | **nome divergente**: o Decreto 5.035-R, art. 2º, V, define a CAP como "Comissão de **Avaliação Permanente**", colegiado paritário (Poder Público e sociedade civil) de 6 a 12 membros, responsável pela análise e habilitação; é designada pelo Secretário e presidida pela Subsecretaria de Fomento e Incentivo Cultural (`fontes/decreto-5035-r-2021.md` l. 36, 102-115; `fontes/regimento-interno-cap-2023.md`) |
| LICC exercício 2025 (`licc-programa`) | "mecanismo de renúncia fiscal que permite a empresas contribuintes do ICMS patrocinar projetos culturais e abater o valor do imposto devido via crédito presumido" | SECULT; Portaria SEFAZ | orçamento do vértice = teto (R$ 25 mi) e captado (BG l. 235-247) |
| Secretário de Estado da Cultura (`titular-secult`) | cargo, sem nome atribuído, porque o titular "não foi conferido em fonte primária" (GIT `13b1734` l. 784-785) | — | — |
| Edital LICC 2025 (`edital-licc-2025`) | chamada pública; oportunidade 1878, encerrada | Mapa Cultural | — |

Vértices de mercado e de execução (NOS l. 94-138):

- **Patrocinador** (28 no grafo; 26 empresas por raiz de CNPJ): "Empresas contribuintes do ICMS.
  Operam como intermediárias que escolhem onde alocar a renúncia fiscal — é aqui que se decide, na
  prática, qual cultura recebe dinheiro" (NOS l. 97-99). É a tese central do licc.gov sobre o
  desenho, e é útil para a teoria da mudança (§ 3.6).
- **Proponente** (52): quem executa, isto é, produtoras, OSCs, coletivos, artistas e prefeituras
  do interior com sede no ES (NOS l. 112-114). Identidade por CPF/CNPJ quando houver; senão, pelo
  slug do nome (HAB l. 445-457).
- **Projeto** (63): "o que a política produz: festivais, mostras, obras de restauro, salvaguarda
  de patrimônio, planos anuais de espaços e grupos estáveis" (NOS l. 127-129).

### 3.3 Relações (arestas)

A ontologia declara 15 relações, cada uma com forma ativa e passiva (ARE l. 26-184; ONT l. 61-88).
Oito aparecem no artefato de 2025 (contagem por REP sobre `graph.json`):

| Relação | Sentido | Significado | Arestas em 2025 | Proveniência |
| --- | --- | --- | --- | --- |
| `patrocina` | empresa → projeto | aporte; **a única aresta que move dinheiro**, com peso em R$ | 86 | oficial |
| `propoe` | proponente → projeto | inscreveu o projeto | 63 | oficial |
| `fiscaliza` | SECULT → projeto | acompanha a execução e julga a prestação de contas | 63 | derivado (a SECULT fiscaliza todo projeto por norma, não por registro individual) |
| `ocorre_em` | projeto → município | local de execução (presença) | 47 | derivado |
| `fundamenta` | entidade → norma | base legal | 231 | oficial 222, derivado 9 |
| `nomeia` | Governo → SECULT; Governo → CEC; SECULT → CAP | designação | 3 | oficial |
| `regula` | SECULT → LICC ("órgão gestor"); SEFAZ → LICC ("autoriza o teto via portaria") | edição de normas | 2 | oficial |
| `beneficia` | LICC → população | alcance da política | 1 | oficial |
| `aprova`, `publica`, `inscrito_em`, `ocupa`, `pertence_a`, `acontece_em`, `sediado_em` | — | declaradas na ontologia | **0** | — |

Três ausências dizem algo ao artigo. (a) Não há aresta `aprova` da CAP para cada projeto: a
habilitação individual não está representada, só a fiscalização genérica. (b) `pertence_a`
(linguagem) é zero porque segmento tem cobertura 0%. (c) `inscrito_em` também é zero, embora
HAB l. 476-477 e 601 a emitam. A causa provável é o id: o importador liga ao vértice
`edital-1878`, mas o grafo tem `edital-licc-2025`, e a poda de arestas órfãs (BG l. 403-407)
descarta a ligação. É inferência sobre o código, sem efeito nos números. A relação "renúncia de
ICMS" entre patrocinador e população é desenhada na interface (CL l. 86-89), mas **não existe
como tipo de aresta**, e a relação fiscal contribuinte-SEFAZ (crédito presumido) não está modelada.

Regra de direção que o licc.gov fez questão de registrar: "Quem publica o edital é a SECULT; quem
inscreve projeto nele é o proponente" (CL l. 259-262; ONT l. 81-84). Inverter as setas "conta uma
história falsa sobre como a lei funciona".

### 3.4 Cadeias de responsabilização

Cada tipo de vértice selecionado "conta uma história diferente sobre o mesmo mecanismo"
(ONT l. 90-103; RD l. 36-43):

- **Patrocinador** → linha até o centro (o ICMS que deixou de entrar no caixa), os projetos que
  escolheu e as linguagens que priorizou. Segundo o licc.gov, é "a leitura que revela concentração
  setorial do capital".
- **Projeto** → proponente (quem faz), patrocinadores (quem financiou) e SECULT (quem aprovou o
  enquadramento).
- **Proponente** → seus projetos e, através deles, quem os financia.
- **Órgão** → o que regula, aprova, fiscaliza e nomeia.

### 3.5 Normas e regras como parte do arranjo

LEG traz 7 normas, 6 estaduais e 1 federal. Só as estaduais **fundam** o programa
(`FUNDAMENTOS_DA_LICC`, LEG l. 319-329). A Lei federal 14.903/2024 (Marco Regulatório do Fomento
à Cultura) "incide" sobre a LICC mas não a institui (GIT `a2cb13c` l. 98-111).

| Regra (LEG `REGRAS`) | `verificado` no licc.gov | `naoApuravel` (motivo) | Estado agora |
| --- | --- | --- | --- |
| Cota I 30% eventos calendarizados > 10 anos | sim | — | conferida (`fontes/in-licc-001-2025.md` art. 18) |
| Cota II 10% planos plurianuais | sim | — | idem |
| Cota III 10% fora da RMGV | sim | — | idem; exige sede **e** locais fora da RMGV |
| Cota IV 50% demais | sim | — | idem |
| Máximo de 3 projetos por proponente/ano | **não** (LegisWeb, IN 2026) | soma PJs com sócios/dirigentes comuns; o QSA da Receita não é consultável | conferida para 2025 (art. 13); `naoApuravel` segue válido |
| Vedação ao fracionamento entre proponentes | não (LegisWeb, IN 2026) | anexos não trazem equipamento, temática nem cronograma | **conferida** nas duas INs: art. 21 veda apresentar o projeto "fragmentado ou parcelado, ainda que por agentes culturais diferentes" e lista seis indícios, dos quais bastam dois (cronograma, comunicação, atividades decorrentes, equipe, temática, relação profissional) (`fontes/in-licc-001-2025.md` l. 503-506; `fontes/in-licc-001-2026.md` l. 701-727). `naoApuravel` segue válido |
| Indeferimento liminar e Cadin-ES por descumprimento de diligência | não (LegisWeb, IN 2026) | tramitação e cadastro de inadimplentes não são publicados | **descrição imprecisa no licc.gov.** No texto oficial, a inclusão no CADIN-ES (e em dívida ativa) decorre de não recolher o valor definido após sanção na prestação de contas: IN 2025, art. 77, § 3º (`fontes/in-licc-001-2025.md` l. 1441-1454); IN 2026, art. 76 (`fontes/in-licc-001-2026.md` l. 1885-1908). O descumprimento de diligência documental leva a indeferimento de ofício (2025) ou arquivamento (2026), segundo a comparação em `fontes/in-licc-001-2026.md` l. 19 |

**Tensão normativa registrada** (PG-IND l. 338-408; LEG l. 117-135): a IN estadual controla pela
regularidade documental da prestação de contas (diligência, indeferimento liminar, Cadin-ES); o
marco federal orienta o controle ao **resultado cultural** alcançado. O painel "exibe os dois e não
arbitra". O conteúdo dos dois lados veio de fonte secundária e aparece com a tarja "conteúdo não
conferido no texto oficial". O lado estadual já se mostrou impreciso: o CADIN-ES está ligado à
sanção na prestação de contas, não à diligência (linha da tabela acima). Para o artigo, isso toca a
pergunta "o que a política monitora", ou seja, conformidade processual e não resultado, e pede
leitura da Lei 14.903/2024 antes de ser afirmado [VERIFICAR].

### 3.6 Leitura para a caracterização da política e a teoria da mudança (proposta desta nota)

O que segue **não** está escrito no licc.gov. É uma tradução da ontologia para o vocabulário da
disciplina (Módulo 03, teoria da mudança) e deve ser conferido contra o material de
`notas/disciplina/`.

- **Insumos:** renúncia de ICMS com teto anual fixado pela SEFAZ (R$ 25 mi em 2025), normas (Lei,
  Decreto, IN), estrutura da SECULT e da CAP, plataforma Mapa Cultural.
- **Atividades (duas etapas de seleção):** (1) seleção **pública**: edital, inscrição, análise
  documental e de mérito, habilitação pela CAP, com enquadramento em cota; (2) seleção **privada**:
  o proponente habilitado procura patrocinador, e a empresa contribuinte escolhe qual projeto
  financiar dentro do seu limite de crédito presumido. Depois vêm execução, fiscalização e
  prestação de contas pela SECULT.
- **Produtos:** projetos culturais executados (o "bem público" do anel 4).
- **Resultados e impactos pretendidos:** oferta e acesso cultural nos municípios, renda e emprego
  no setor, distribuição territorial (cota III). Isso **não** está nos dados do licc.gov: ele mede
  alocação de recursos, não resultado cultural.
- **Pressupostos críticos que o licc.gov ajuda a questionar com dados:** (i) a escolha privada
  preserva o interesse público definido na habilitação, mas o capital está muito concentrado
  (§ 2.1) e a linguagem cultural financiada é desconhecida; (ii) as cotas corrigem o viés
  territorial, mas a cota III não é apurável e 66,4% do valor atribuível ficou na RMGV (§ 2.2);
  (iii) habilitar gera execução, mas a captação expira para parte relevante dos habilitados (§ 1.3)
  e o indicador de conversão do licc.gov não enxerga isso (§ 2.3).

## 4. Armadilhas de dados e o que é indeterminado

As armadilhas marcadas "(licc.gov)" foram descobertas e documentadas lá, quase todas em CL
l. 128-264 ("Armadilhas já pagas"). As marcadas "(nova)" apareceram nesta tarefa, ao refazer as
contas com REP.

### 4.1 Como a SECULT publica (armadilhas de fonte)

1. **Dois anexos, dois recortes chamados "2025"** (licc.gov; CL l. 130-136; GIT `78163a4`
   l. 7-17). "RECURSO FINANCEIRO CAPTADO 2025" é dinheiro captado no **ano calendário**;
   "PROJETOS HABILITADOS – ANO 2025" é o **ciclo de habilitação**, que capta no ano seguinte.
   Tratar a lista de habilitados como lote gerava 115 projetos onde havia 63. Solução: ela entra
   como **dicionário** e enriquece quem já está no grafo, sem criar projeto.
2. **Os anexos publicam coisas diferentes** (licc.gov; PIPE l. 42-54). A lista de habilitados traz
   município (local de execução), cota e valor autorizado; o anexo de captados traz valor por
   patrocinador com CNPJ. Nenhum dos dois traz linguagem cultural, sede do proponente nem CPF/CNPJ
   do proponente (REP → `licc_gov_inventario_colunas.csv`).
3. **Três níveis de acesso** (licc.gov; PIPE l. 58-69; HAB l. 4-18). Editais, agentes, espaços e
   eventos são públicos na API do Mapas Culturais. As inscrições (`registration`) exigem JWT. Valores
   e patrocinadores só existem nos anexos em PDF. "A API dá o contexto; não dá a substância."
4. **`project` do Mapa Cultural não é projeto da LICC** (licc.gov; CL l. 55-61; PIPE l. 190-205).
   É qualquer projeto cadastrado na plataforma. Uma versão antiga carimbava todos como oficiais da
   LICC, o que "afirmaria que todo projeto cultural do ES é incentivado pela LICC" (GIT `04a8598`
   l. 465-469). Hoje servem só para enriquecer (URL, descrição).
5. **A comissão é permanente e publica em lotes** (licc.gov; CL l. 48-53; PIPE l. 71-87; GIT
   `4d4d664`). Para 2025 foram achadas pelo menos seis listas rotuladas "ANO 2025", com 28, 33, 35,
   37, 41 e 74 projetos. A transcrição final usou uma lista contínua de cinco ciclos cuja seção 2025
   declara 74 (GIT `78163a4` l. 46-49). **Não está documentado se as seis listas são cumulativas**
   (a de 74 contém as demais) **ou lotes disjuntos**. Se forem disjuntas, o ciclo 2025 teria mais
   de 74 habilitados [VERIFICAR antes de usar "74 habilitados em 2025" como população].
6. **No anexo de captados, o rótulo do projeto é centralizado sobre o grupo de termos** (licc.gov;
   CL l. 157-164; ANX l. 55-77). Ler por "âncora mais próxima acima" atribuía o aporte da Perfil
   Alumínio à escola de samba da linha de cima. A leitura correta é a partição contígua que minimiza
   a distância entre o rótulo e o centro do grupo, com resíduo médio de 0,4 pt e pior caso de 5,8 pt.
7. **O cabeçalho de cota no anexo de captados carrega o teto da cota** (licc.gov; CL l. 165-169).
   "Valor: R$ 12.500.000,00" virava projeto fantasma. Consequência útil (nova, inferida de CL l.
   165-169 e ANX l. 86-88): **o anexo de captados é seccionado por cota e imprime "Total Captado"
   por cota**, mas a seção de cada projeto não foi gravada no CSV. Relê-lo daria a cota de todos os
   63 e o total captado por cota, o que tornaria o cumprimento do art. 18 apurável pela captação
   [VERIFICAR no PDF `RECURSO FINANCEIRO CAPTADO - 2025.pdf`].
8. **Banda de coluna aberta engolia o número da página** (licc.gov; CL l. 149-151). Os
   "enquadramentos" de 2022 e 2023 eram "18", "24", "26". Hoje esses ciclos simplesmente não têm
   enquadramento (§ 1.3).
9. **A virada de ciclo acontece no meio da página** (licc.gov; GIT `78163a4` l. 53-56). Em duas
   passadas, a página inteira caía na seção errada **e a contagem total continuava batendo**.
10. **Conferidor que prova a leitura bloqueia; divergência que descreve a fonte, não** (licc.gov;
    CL l. 152-156). A fonte traz valores anômalos que foram mantidos como estão. REP lista 8 linhas
    com valor ausente ou autorizado > total (`licc_gov_habilitados_anomalias_valor.csv`):
    "Origraffes" (ciclo 2023, os dois valores ausentes, provavelmente o caso "500.000.00");
    "Biblioteca Itinerante Vila Quilombo" (2025, autorizado R$ 100 acima do total); "2ª Festa da
    Palavra" (2024, total = 500 contra autorizado 483.000); "Mais Cultura Nas Escolas" (2024, total
    ausente); e quatro casos de 2024 com autorizado acima do total (diferenças de R$ 0,60 a
    R$ 13.383,35). Leitura inferida dos nomes das colunas e de CL l. 153-154: `valor_total` é o custo
    total do projeto e `valor_autorizado` o valor LICC [VERIFICAR os oito no PDF e o significado das
    duas colunas no cabeçalho do anexo].
11. **A contagem declarada não basta** (licc.gov; ANX l. 98-107). Num teste, a contagem bateu (5 de 5)
    com todos os valores truncados. Por isso há conferidor de formato e junção de linha de continuação.
12. **Anexo de captados 2026 tem outro desenho de página** (licc.gov; CL l. 394-400). O valor
    habilitado se repete em 99 das 129 linhas de termo; a leitura dá 3 projetos com captado acima do
    autorizado e soma R$ 69.371,00 abaixo dos totais impressos. A ferramenta recusou gravar: **não há
    captação de 2026 no repositório**.

### 4.2 Identidade e casamento

13. **Casamento por semelhança funde projetos distintos** (licc.gov; CL l. 137-142). "Carna Barra"
    casava com "Carna Surpresa 2024", e "Boa Vista Carnaval Capixaba 2026" com o de 2025. Regra
    adotada: título normalizado **exato**, e título presente em mais de um ciclo fica de fora
    ("festival anual tem uma linha por edição").
14. **Empresa identificada pelo nome, não pelo CNPJ** (nova). O importador agrupa o patrocinador pelo
    slug do nome (HAB l. 614-638), então grafias diferentes da mesma empresa viram vértices
    diferentes. No grafo, "Transportadora Associada de Gás - TAG" e "TRANSPORTADORA ASSOCIADA DE GAS
    S.A. - TAG" têm o **mesmo CNPJ** (06.248.349/0004-76), assim como "Kuruma Veiculos S.A." e
    "Kuruma Veiculos S.A DECOLORES" (00.827.783/0001-81). Por raiz de CNPJ são **26 empresas, não
    28** (REP → `licc_gov_concentracao_por_raiz_cnpj.csv`). Para o artigo: usar raiz de CNPJ e
    reportar a diferença.
15. **Proponente sem documento** (licc.gov e nova; HAB l. 445-457). Sem CPF/CNPJ, duas grafias do
    mesmo agente viram dois vértices: 55 grafias distintas no CSV de captados, 52 vértices no grafo.
    Os CSVs de habilitados também não trazem documento, e há variantes visíveis ("1440. PRESS
    EDITORA..." / "1440.Press Editora..."; "Alpha Empreendimentos LTDA ME." / "Alpha Empreendimentos
    Ltda Me.") (`licc_gov_inventario_colunas.csv`). Qualquer contagem de proponentes distintos é
    aproximada.
16. **Anotação dentro do campo de proponente** (nova). Uma linha do CSV de captados tem proponente
    "(Em análise na SEFAZ) Secretariado dos Imigrantes Friulanos de Aracruz-ES" (projeto "13ª ITALIA
    UNITA"). O texto entre parênteses é situação, não nome.
17. **Nomes de município que não resolvem** (licc.gov; CL l. 380-382): "Vila Veha" (erro de digitação
    da fonte), "Marechal" e "Itaúnas", que o licc.gov descreve como "distrito, não município". O
    inventário mostra outras grafias sujas no CSV, como "Aracruz Vitória" sem separador e "(Vitória;
    Vila Velha; Serra; Cariacica" com parêntese solto (`licc_gov_inventario_colunas.csv`).
    "Várias Regiões" vira lista vazia (HAB l. 70-74).
18. **O número de processo não indica o ciclo** (nova). O prefixo do processo (ex.: "2022-...") é o
    ano de abertura, e processos de 2022 aparecem no ciclo 2023 (61 casos) e de 2023 no ciclo 2024
    (83 casos) (REP → `licc_gov_prefixo_processo_por_ciclo.csv`). Além disso, 4 processos aparecem em dois ciclos (2025
    e 2026): `2024-454L8`, `2024-7NZLF`, `2025-49GXP`, `2025-SB2J8` [VERIFICAR se é rehabilitação,
    plano plurianual ou duplicidade].

### 4.3 Interpretação de regras (o que o dado não autoriza a dizer)

19. **Ausência não é `false`** (licc.gov; CL l. 170-175; GIT `acb3530` l. 263-272). Ler "a fonte não
    diz" como "não se enquadra" e "sem município" como "fora da RMGV" fez o painel declarar **1112%**
    de cumprimento da cota territorial sobre 63 projetos sem município.
20. **Alocação de cota é piso, não total** (licc.gov; CL l. 143-148; BG l. 330-344). Com cobertura
    parcial, piso abaixo da reserva não prova descumprimento. Exibir "✗ 46,6%" sobre 31 de 63
    projetos era "o erro do 1112% de cabeça para baixo". Três ressalvas novas que o licc.gov não
    registrou: (a) o piso soma o **valor autorizado** dos projetos da cota (BG l. 291-292, 322), e
    não o captado, embora o caput do art. 18 fale no "uso do montante anual de recursos
    disponíveis", o que sugere que a cota recai sobre a captação (leitura desta nota, a confirmar
    com a SECULT); (b) o art. 18, § 1º, manda projetos de cotas I-III esgotadas para a cota IV, e o § 2º
    permite remanejar sobras "a critério da SECULT" (`fontes/in-licc-001-2025.md` l. 379-383), de
    modo que nem com cobertura completa "abaixo" equivaleria a descumprimento; (c) o enquadramento
    vem da lista de habilitados do ciclo do projeto, e os projetos de ciclos 2022-2023 que captam
    depois não têm classificação nenhuma.
21. **"Li a norma" ≠ "consigo apurar o cumprimento"** (licc.gov; CL l. 215-220; LEG l. 160-180).
    O limite de 3 projetos está agora conferido (IN 2025, art. 13), mas continua inapurável: o
    parágrafo único alcança CNPJs com o mesmo quadro societário, e o QSA da Receita não foi cruzado.
    Além disso, a regra limita a **inscrição**, e só se observam habilitados e captados.
22. **Ressalva fixa vira mentira ao avesso** (licc.gov; CL l. 176-179). Um texto de aviso que não
    acompanha o dado continuou dizendo "dados de demonstração" depois que os dados viraram reais.
    Vale para o artigo: toda ressalva deve citar a cobertura do número a que se refere.
23. **Nem toda norma que incide sobre a LICC a funda** (licc.gov; CL l. 192-196). A Lei federal
    14.903/2024 incide, mas não institui o programa.

### 4.4 Agregação

24. **Multimunicípio: presença sim, dinheiro não** (licc.gov; GIT `78163a4` l. 37-42). O rateio
    entre municípios não é publicado. Somar o valor cheio em cada município passaria do teto.
25. **Acumulador zerado não pode sobreviver** (licc.gov; CL l. 197-205; GIT `9c19ea1`). 101 nós
    saíam com "R$ 0" sem ter orçamento (municípios sem projeto, normas, órgãos). Município sem
    projeto não "recebeu zero": a fonte simplesmente não diz. Isso afeta a leitura do Gini
    territorial, que trata como zero o município sem projeto conhecido (§ 2.2).
26. **Tarja e número têm de contar a mesma coisa** (licc.gov; CL l. 206-209). "Sem dado" ao lado de
    "R$ 0 de R$ 12.500.000" se lê como "o Estado não destinou nada".
27. **Arredondamento** (licc.gov; CL l. 210-214; BG l. 97-122). Dinheiro é arredondado a centavo
    depois de agregar; razões não são arredondadas.
28. **Não há série anual no grafo** (nova). Os campos `orcamento.anterior` e `variacaoAnual` existem
    no modelo (herança do seed), mas no artefato de 2025 são todos zero ou nulos (REP: 0 nós com
    variação não nula). O grafo é um corte de um ano só.

### 4.5 Inconsistências remanescentes no próprio licc.gov (não copiar para o artigo)

- A descrição de `in-licc-001-2025` em LEG l. 143 e no `graph.json` ainda fala em "três cotas" com
  rótulos antigos ("projetos pautados", "programas continuados"). O mesmo vale para RD l. 112,
  PIPE l. 220 e o comentário de BG l. 283. O correto são as quatro cotas de LEG l. 190-242.
- Os ids `cota-pautados` e `cota-continuados` são nomes herdados: significam "eventos
  calendarizados com mais de 10 anos" e "planos plurianuais" (GIT `c757274` l. 372-374).
- Contagem de proveniência: CL fala em 533/159, o artefato em 536/206 (§ 1.6).
- A regra do limite está `verificado: false` e cita a IN 2026 via LegisWeb (LEG l. 243-257), mas o
  texto de 2025 já está lido em `notas/politica/fontes/` (§ 3.5).
- O nome da CAP diverge do decreto (§ 3.2).
- A conta "40 + 4 + 18" soma 62, não 63 (§ 1.4).
- `/sobre` ainda descreve a coleta pela API como caminho dos dados (PG-SOB l. 80-104). Hoje os
  projetos vêm dos anexos.

### 4.6 O que é indeterminado, e por quê

| Pergunta | Estado | Por quê | O que resolveria |
| --- | --- | --- | --- |
| As cotas do art. 18 foram cumpridas em 2025? | **indeterminado** | 32 de 63 projetos sem classificação; piso calculado sobre o autorizado; §§ 1º-2º permitem migração e remanejamento | reler o anexo de captados por seção de cota (item 7) e ler a regra de remanejamento aplicada pela SECULT |
| A cota III (fora da RMGV) foi cumprida? | **indeterminado** | exige sede do agente **e** locais de execução fora da RMGV, e a sede não é publicada | usar a classificação da SECULT (`cotaId`) em vez de deduzir; sede via cadastro do agente no Mapa Cultural (API pública de `agent`, sem garantia de ser a sede declarada) |
| Algum proponente passou do limite de 3 projetos? | **não apurável** | a regra vale para inscrições (não observadas) e soma CNPJs de mesmo quadro societário (QSA não cruzado) | lista de inscritos (exige JWT) + QSA da Receita |
| Houve fracionamento de projeto? | **não apurável** | faltam cronograma, equipe, temática e comunicação | processos individuais |
| Houve sanção ou inscrição no CADIN-ES? | **não apurável** | tramitação não publicada | dados de prestação de contas da SECULT |
| Que linguagens culturais a LICC financia? | **desconhecido (0%)** | nenhum anexo publica linguagem; classificar pelo título seria inferência | inscrição no Mapa Cultural (área/linguagem do projeto) ou classificação manual declarada como derivada |
| Quanto cada município recebeu? | **parcial** | R$ 10,63 mi (42,5%) sem município atribuível; rateio multimunicipal não publicado; 23 projetos sem casamento | casar os 23 por processo e valor (§ 7) |
| Qual a natureza jurídica de quem executa? | **desconhecido (0/52)** | sem CPF/CNPJ do proponente | CNPJ nos processos ou no Mapa Cultural; natureza jurídica na base CNPJ da Receita |
| Qual a conversão habilitado → captado? | **não medida pelo licc.gov** | o anexo de captados só tem quem captou | status por ciclo na lista de habilitados (§ 1.3), com a ressalva de ciclo aberto |
| Captação de 2026 | **ausente** | anexo com outro desenho, extração recusada | nova leitura com verificação humana |

## 5. Inventário de dados disponíveis

Cobertura coluna a coluna em `analise/tabelas/licc_gov_inventario_colunas.csv` (REP). Regra de
leitura para todos os CSVs: **célula vazia = a fonte não publicou**, nunca zero (PIPE l. 153-162;
HAB l. 20-28).

### 5.1 `dados/licc/habilitados/habilitados-{2022..2026}.csv`

- **Origem:** lista de projetos habilitados publicada pela SECULT; `fonte_url` =
  `https://secult.es.gov.br/lista-de-projetos-habilitados` em todas as linhas, com a página em
  `fonte_pagina`. É uma lista contínua de cinco seções, transcrita por leitura posicional do PDF com
  `tools/anexos-secult/extrair.mjs`, que não foi copiado para cá (GIT `78163a4` l. 44-62). A coluna
  de objeto do projeto foi **descartada** porque "sua prosa atravessa a fronteira entre registros"
  (GIT `78163a4` l. 46-48).
- **Unidade:** projeto habilitado num ciclo. 467 linhas (69, 113, 123, 74, 88).
- **Esquema:**

| Coluna | Conteúdo | Cobertura e ressalvas |
| --- | --- | --- |
| `numero_processo` | código do processo (ex.: `2025-V9F70`) | 100%; o prefixo é o ano de abertura, não o ciclo (§ 4.2, item 18); 4 processos aparecem em 2025 e 2026 |
| `projeto` | título | 100%; grafias com aspas e caracteres tipográficos |
| `proponente` | nome do agente cultural | 100%; **sem CPF/CNPJ**; variantes de grafia |
| `municipio` | "Local de Execução"; vários separados por `;` | 2022-2023: 100%; 2024: 121/123; **2025: 58/74**; 2026: 100%; grafias sujas (§ 4.2, item 17) |
| `valor_autorizado` | valor LICC habilitado (teto de captação do projeto) | 466/467 (falta 1 em 2023); anomalias em § 4.1, item 10 |
| `valor_total` | custo total do projeto | 465/467 |
| `status` | `concluido`, `em_execucao`, `captando`, `captacao_expirada` | 100%; retrato na data da publicação (não registrada) |
| `enquadramento` | cota do art. 18 (`cota-pautados` = eventos calendarizados > 10 anos; `cota-continuados` = planos plurianuais; `cota-fora-rmgv`; `cota-demais`) | **2022-2023: 0%**; 2024-2026: 100%. É a classificação publicada pela SECULT, não dedução |
| `fonte_url`, `fonte_pagina` | endereço e página | 100% |

- **Limitações:** não traz linguagem, sede, documento do proponente, valor captado nem patrocinador.
  Faltam as datas de habilitação dentro do ciclo. Não se sabe se o ciclo 2025 está completo com 74
  (§ 4.1, item 5).

### 5.2 `dados/licc/oficial/captados-2025.csv`

- **Origem:** anexo "RECURSO FINANCEIRO CAPTADO - 2025", `https://secult.es.gov.br/Media/secult/LICC/RECURSO%20FINANCEIRO%20CAPTADO%20-%202025.pdf`,
  pp. 1-5. Transcrito por `tools/anexos-secult/extrair-captados.mjs`, com conferidores de soma
  (bate em R$ 25.000.000,00), teto por projeto e resíduo de centralização (ANX l. 79-96).
- **Unidade:** projeto que captou no ano calendário de 2025 (63 linhas; o PDF tem uma linha por
  termo, o CSV agrega por projeto).
- **Esquema:**

| Coluna | Conteúdo | Cobertura e ressalvas |
| --- | --- | --- |
| `projeto` | título | 63/63; grafia difere da lista de habilitados em parte dos casos (§ 1.4) |
| `proponente` | nome | 63/63; uma linha com anotação "(Em análise na SEFAZ)" (§ 4.2, item 16) |
| `valor_autorizado` | valor habilitado impresso no anexo | 63/63 |
| `valor_captado` | soma dos termos | 63/63; igual à soma de `aportes` em todos os 63 (REP) |
| `patrocinador` | nomes separados por `;` (com repetição quando há mais de um termo) | 63/63 |
| `aportes` | termos `CNPJ|nome|valor; ...` | 63/63; 95 termos, 46 CNPJs de estabelecimento, 26 raízes |
| `fonte_url`, `fonte_pagina` | endereço e página | 63/63 |

- **Limitações:** não traz município, cota (embora o PDF seja seccionado por cota: § 4.1, item 7),
  número de processo, ciclo de habilitação, data do termo nem linguagem. Só tem quem captou (§ 2.3).

### 5.3 `dados/licc/graph.json` (artefato consolidado do licc.gov, exercício 2025)

- **Estrutura:** `{meta, nodes, edges}`. `meta` = `{ano: 2025, geradoEm, tetoAutorizado: 25000000,
  fontes[3], contagemPorProveniencia}`. 246 vértices e 496 arestas (REP).
- **Vértices por categoria:** municipio 78, projeto 63, proponente 52, patrocinador 28, segmento 9,
  fundamento 7, governanca 6 (inclui o vértice-programa `licc-programa`), publico 1, edital 1,
  pessoa 1. Não há `evento` nem `espaco` (a coleta do Mapa Cultural não foi incorporada).
- **Campos por categoria** (contagem de preenchimento feita por REP em inspeção do JSON):
  - `projeto`: `id` (`proj-<processo>` ou `proj-<slug do título>`), `nome`, `fontes` (anexo e
    página), `fundamentos`, `orcamento.{autorizado, captado}` (63/63), `meta.{ano, numeroProcesso
    (41), status (40), municipioId (37, só município único), municipiosIds (40), cotaId (31),
    proponenteId (63)}`, `posicao`, `variacaoAnual` (sempre nulo).
  - `proponente`: `meta.{municipioId (32, "aproximação da sede": HAB l. 583-591), projetosNoAno}`,
    `orcamento` agregado. **Sem `natureza`.**
  - `patrocinador`: `meta.cnpj` em 26 de 28. O campo é gravado só quando, no **primeiro** projeto
    em que a empresa aparece, ela assinou por um único estabelecimento (HAB l. 626-638). VD e
    Comercial Devens assinaram por dois estabelecimentos no primeiro projeto e ficaram sem CNPJ.
    `orcamento.captado` = soma dos pesos.
  - `municipio`: `meta.{regiao, regiaoMetropolitana}`; `orcamento` só nos 19 com projeto.
  - `fundamento`: `meta.{norma, publicadoEm, verificado}`.
- **Arestas:** `{id, source, target, kind, proveniencia, peso?, rotulo?}`; `peso` só em `patrocina`
  (86); contagens por tipo no § 3.3.
- **Uso no artigo:** fonte cômoda para o recorte de 2025 já casado (município e cota dos 40/31
  projetos casados). Toda estatística deve declarar a cobertura.

### 5.4 `dados/licc/stats.json`

Resumo gerado por `apurarEstatisticas` (BG l. 283-388): `totalProjetos`, `totalProponentes`,
`totalPatrocinadores`, `totalMunicipiosAtendidos`, `autorizado`, `captado`,
`comprometimentoDoTeto`, `execucao`, `cotas[4]` (`reservado`, `alocado`, `cumprimento`,
`atendida`, `classificaveis`), `proponentesNoLimite`, `cobertura` (`projetos`, `oficiais`,
`comValorAutorizado`, `comValorCaptado`, `comMunicipio`, `comSegmento`, `comPatrocinador`).
Valores em §§ 1.2, 1.5 e 2.5; todos replicados por REP.

### 5.5 Tabelas derivadas desta tarefa (`analise/tabelas/`, geradas por REP)

| Arquivo | Conteúdo |
| --- | --- |
| `licc_gov_indicadores_resumo.csv` | os 4 indicadores (e a variante por raiz de CNPJ), com base e universo |
| `licc_gov_concentracao_capital.csv` | aporte por empresa como o grafo agrupa (28) |
| `licc_gov_concentracao_por_raiz_cnpj.csv` | aporte por raiz de CNPJ (26) |
| `licc_gov_territorio_municipios.csv` | 78 municípios: presença, captado atribuído, projetos com valor |
| `licc_gov_casamento_captados.csv` | cada um dos 63 captados e os ciclos de habilitação em que o título aparece |
| `licc_gov_habilitados_status_enquadramento.csv` | status e cota por ciclo |
| `licc_gov_habilitados_anomalias_valor.csv` | 8 linhas com valor ausente ou autorizado > total |
| `licc_gov_prefixo_processo_por_ciclo.csv` | prefixo do processo × ciclo |
| `licc_gov_inventario_colunas.csv` | cobertura, número de valores distintos e exemplos por coluna |

### 5.6 O que existe no licc.gov mas **não** está aqui

- Os PDFs originais e as ferramentas `tools/anexos-secult/` (baixar, extrair, extrair-captados) e
  `tools/scrape-civlab/` (só interface). As URLs dos seis lotes de 2025 estão em PIPE l. 73-84.
- `data/raw/` (ignorado pelo git) e a coleta da API do Mapa Cultural (`pipeline/ingest.ts`,
  `pipeline/sources/mapas-culturais.ts`), com filtros e endpoints descritos em PIPE l. 164-205. A
  API é pública para `opportunity`, `agent`, `project`, `space` e `event`; as inscrições exigem JWT.
- `src/lib/text.ts` (funções `normalizar`, `slugificar`, `nomesCorrespondem`), por isso o casamento
  do licc.gov não é reproduzível à letra aqui (§ 1.4).
- Captação de 2026 (recusada, § 4.1, item 12) e captação de 2022-2024 (nunca transcrita; não se
  sabe se a SECULT publica anexo equivalente para esses anos [VERIFICAR]).

## 6. Textos interpretativos aproveitáveis (/sobre, /indicadores, /orcamento)

Paráfrases, com o arquivo e as linhas onde está o texto original. Ao usar no artigo, reescrever em
registro acadêmico e citar os dados, não o licc.gov. O licc.gov é projeto independente e não serve
como referência bibliográfica. Se for mencionado, vai como fonte dos dados transcritos.

**(a) O mecanismo e quem paga.** O Estado deixa de arrecadar ICMS para que a política exista. Por
isso a população é ao mesmo tempo financiadora indireta, pelo imposto que não entrou no caixa, e
destinatária final do bem cultural. É a justificativa do centro do grafo e serve para abrir a
caracterização da política como **gasto tributário** (CL l. 86-89; RD l. 18-21; ONT l. 18-22; NOS
l. 68-70; GIT `84aeda1` l. 878-885).

**(b) Autorização não é dinheiro.** O teto anual é a renúncia que o Estado autoriza. A habilitação
dá ao projeto um teto próprio de captação, mas o recurso só existe quando uma empresa contribuinte
aporta (PG-ORC l. 60-66; PG-IND l. 176-177; IND l. 289-295). Como a SECULT habilita mais teto do
que há renúncia (111% em 2025), é a disputa por patrocinador que decide quem capta, e isso não é
erro de gestão (CL l. 355-357). Serve para descrever a **segunda etapa de seleção** do desenho.

**(c) Quem decide a alocação é a empresa.** As empresas contribuintes "operam como intermediárias
que escolhem onde alocar a renúncia"; é nelas que se decide qual cultura recebe dinheiro (NOS
l. 97-99). A cadeia que parte do patrocinador revela a concentração setorial do capital (ONT
l. 95-97). É a hipótese central para a teoria da mudança (§ 3.6) e para a literatura sobre
incentivo fiscal à cultura, que deve ser citada a partir de fontes verificadas, não do licc.gov.

**(d) O território: o zero é informação.** O indicador territorial lista os 78 municípios, inclusive
os que nada receberam, porque mostrar só quem recebeu daria a impressão de que a política chega a
todo lugar (IND l. 177-186; PG-IND l. 115-116). O "monitor" do licc.gov acompanha a chegada efetiva
da política ao município, e "onde não há nada, o que também é informação" (RD l. 130-133; CL
l. 180-184). A cota territorial é "o piso, não o retrato" (PG-IND l. 123-129).

**(e) Desigualdades de naturezas diferentes.** O Gini territorial conta municípios zerados e o do
capital só conta empresas que patrocinaram, por isso "não devem ser comparados entre si" (IND
l. 183-186; PG-IND l. 164-166).

**(f) Ausência, denominador e cobertura.** Célula vazia é ausência, nunca zero, e trocar uma pela
outra é "a forma mais silenciosa de mentir num painel financeiro" (CL l. 62-66). Todo indicador vem
com o número de registros sobre os quais foi calculado (IND l. 9-17), e a página de indicadores
abre pela cobertura, porque "todo indicador desta página é tão bom quanto a linha correspondente"
(PG-IND l. 410-460). Divergência entre anexos oficiais "é achado, não ruído" (PIPE l. 125-127). Um
grafo que admite não saber vale mais do que um que preenche a lacuna com dado alheio (PIPE
l. 203-205). Serve para a seção de dados e limitações do artigo.

**(g) Não acusar sem dado.** A lista de proponentes no limite descreve "quem alcançou o número, não
quem descumpriu a norma" (PG-IND l. 266-271). Cota sem projeto classificável não admite conclusão
"nem a favor, nem contra" (PG-ORC l. 133-137). Tarja e número precisam contar a mesma coisa (CL
l. 206-209). É o tom certo para avaliar o desenho sem afirmar descumprimento.

**(h) A arquitetura do que o Estado publica.** O que a LICC publica se reparte em três níveis:
contexto público na API do Mapas Culturais, inscrições fechadas (JWT) e substância (valores,
patrocinadores) só em documento. "A API dá o contexto; não dá a substância" (PIPE l. 58-69; HAB
l. 4-18). Serve para a seção de fontes de dados da proposta de avaliação. A Lei 11.246/2021, art.
5º-B, IX, "e", 4, manda a SECULT definir a forma de publicação dos benefícios, "inclusive no Portal
da Transparência do Estado" (`fontes/lei-11246-2021.md`).

**(i) Dois desenhos de controle.** A IN estadual mira a regularidade documental; o marco federal
(Lei 14.903/2024) orienta o controle ao resultado cultural. O painel declara a norma sem arbitrar
(PG-IND l. 338-408). No artigo isso se liga à ausência de indicadores de resultado no monitoramento
da LICC, mas os dois lados precisam de conferência no texto oficial (§ 3.5).

**(j) Linguagem não é classificação oficial.** A norma não fecha uma lista de segmentos, e os 9 do
licc.gov vêm da taxonomia do Mapas Culturais, como eixo de leitura (SEG l. 21-29; ONT l. 143-152).
"Errar a classificação é pior que admitir a lacuna" (ONT l. 150-152). [VERIFICAR a expressão "em
qualquer formato ou linguagem cultural" (SEG l. 24) no texto da IN.]

**(k) Método de transcrição.** A extração dos anexos foi posicional, por coordenadas do PDF, e não
feita por modelo de linguagem, porque um modelo "arredonda valor e pula linha em silêncio". Os
conferidores foram contagem declarada, formato, soma contra o total impresso, teto por projeto e
resíduo de centralização (CL l. 298-303; ANX l. 41-46 e 79-107). Serve para a seção de dados e para
a declaração de uso de IA exigida pelo `CLAUDE.md` do projeto.

**(l) Proveniência como método.** "Um grafo bonito de dados sintéticos é indistinguível de um grafo
bonito de dados reais" (PG-SOB l. 41-45; CL l. 31-32). Daí os selos oficial, derivado e
demonstração em todo registro.

## 7. Lacunas e próximos passos registrados pelo licc.gov que importam para o artigo

### 7.1 Próximos passos do licc.gov (CL l. 368-400) e situação atual

| # | Passo registrado | Importa para o artigo? | Situação em 23/09/2026 |
| --- | --- | --- | --- |
| 1 | Calibrar o grafo radial contra medidas do CivLab | não (interface) | — |
| 2 | **Fechar os 23 projetos sem município**: casar por valor autorizado idêntico + proponente, sem semelhança de nome; resolver "Vila Veha", "Marechal", "Itaúnas" | **sim**: 42,5% do valor captado está sem município (§ 2.2) | em aberto. REP mostra que uma normalização mais tolerante (sem acento e pontuação) casa 49 títulos de forma única, contra 40 no licc.gov; falta conferir à mão e combinar com o valor autorizado |
| 3 | Valores por projeto vêm dos anexos, porque a API não expõe inscrições | sim (fonte de dados) | resolvido para 2025 (captados) e 2022-2026 (autorizado) |
| 4 | **Conferir a regra dos 3 projetos** na IN vigente sem apagar o `naoApuravel` | sim (caracterização) | **conferida**: IN 2025, art. 13, e IN 2026, art. 13, com redações diferentes no parágrafo único (§ 3.5; `fontes/in-licc-001-2026.md` l. 16). Continua inapurável |
| 5 | Anexo de captados de 2026 com outro desenho de página | sim, se o artigo quiser dois anos de captação | em aberto; exige conferência humana no PDF |

### 7.2 Outras lacunas que o licc.gov registrou

- **Linguagem cultural: 0%** (CL l. 362-363; RD l. 193-197). Nenhum anexo publica, e o licc.gov se
  recusou a inferir do título. Para o artigo é uma lacuna de caracterização ("que cultura a LICC
  financia?") e de avaliação (heterogeneidade por linguagem).
- **Natureza jurídica e documento do proponente** (HAB l. 444-457, 671-684). Sem CPF/CNPJ não há
  PF/PJ nem cruzamento societário.
- **Camada territorial do Mapa Cultural** (`space`, `event`; RD l. 128-133; PIPE l. 186-189). Está
  projetada mas não incorporada: o grafo de 2025 não tem espaços nem eventos. Seria uma medida de
  oferta cultural por município, possível variável de resultado ou de controle.
- **Coleta automática bloqueada no ambiente do licc.gov** (CL l. 266-303). Lá, planalto, Câmara,
  SEFAZ e IBGE respondiam bloqueado. **Neste repositório a rede funciona** (`CLAUDE.md` do projeto,
  seção "Rede"), então várias normas que ficaram `verificado: false` já foram lidas em
  `notas/politica/fontes/` (Decreto 5.035-R, INs 2025 e 2026, portarias).

### 7.3 Lacunas novas, identificadas nesta síntese, que o artigo precisa tratar

1. **Cumprimento das cotas pela captação.** Reler o anexo de captados 2025 registrando a seção de
   cota de cada projeto e o "Total Captado" por cota (§ 4.1, item 7). É o caminho mais curto para
   transformar "indeterminado" em resultado. Precisa de leitura do PDF (sem download binário para
   o disco, pela regra desta tarefa: usar leitura online).
2. **População do ciclo 2025.** Confirmar se os seis lotes "ANO 2025" (PIPE l. 73-84) são
   cumulativos ou disjuntos, antes de usar 74 como número de habilitados (§ 4.1, item 5).
3. **Identidade por CNPJ.** Recontar empresas por raiz de CNPJ (26, não 28) e manter as duas
   versões do Gini (§ 4.2, item 14).
4. **Conversão verdadeira.** Medir habilitado → captado pelo `status` da lista de habilitados, por
   ciclo, declarando ciclos abertos (§ 2.3). O indicador 3 do licc.gov é condicional a ter captado.
5. **Data de referência dos status.** Registrar a data de atualização da página de habilitados
   [VERIFICAR].
6. **Captação de outros anos.** Verificar se a SECULT publica anexo "RECURSO FINANCEIRO CAPTADO"
   para 2022-2024 [VERIFICAR]. Sem isso, a captação só é observada em um ano.
7. **Portal da Transparência.** A Lei 11.246/2021 manda publicar os benefícios concedidos, inclusive
   no Portal da Transparência (`fontes/lei-11246-2021.md`, art. 5º-B, IX, "e", 4). Conferir se
   `transparencia.es.gov.br` traz a renúncia por contribuinte ou por projeto [VERIFICAR]. Seria
   fonte independente dos anexos.
8. **Correções ao licc.gov que o artigo não deve herdar:** nome da CAP (Comissão de Avaliação
   Permanente, Decreto 5.035-R, art. 2º, V); descrição das três cotas em LEG l. 143; CADIN ligado
   à diligência (§ 3.5); contagem 40+4+18 = 62 (§ 1.4); 28 "empresas".

### 7.4 O que isto implica para a proposta de avaliação de impacto (pontes, não conclusões)

- **Estrutura de seleção em duas etapas** (§ 3.6). Habilitação pública e escolha privada dão dois
  contrastes possíveis. Entre habilitados, captou ou não captou (status `captacao_expirada`), com
  forte seleção pela empresa. Entre municípios, com e sem projeto, com 59 de 78 sem projeto em
  2025. Os dados disponíveis (lista de habilitados 2022-2026 com município e status) sustentam
  descrições por ciclo e município. A identificação causal depende de desenho a ser discutido nas
  notas `notas/desenho/`, e não é afirmada aqui.
- **Defasagem de tratamento.** A captação de um ano financia projetos habilitados um ou dois ciclos
  antes (§ 1.4). Qualquer desenho com tempo precisa fixar se o tratamento é a habilitação, a
  captação ou a execução.
- **Unidade de análise e cobertura.** Município só existe para o local de execução, com cobertura
  parcial e sem rateio (§ 2.2). Uma análise municipal precisa declarar essa limitação e,
  provavelmente, usar presença (projeto ocorre no município) em vez de valor.
- **Resultados não observados.** O licc.gov mede alocação, não resultado cultural. Variáveis de
  resultado (oferta cultural, emprego no setor, público) terão de vir de outras fontes, a
  especificar em `notas/dados/`.
