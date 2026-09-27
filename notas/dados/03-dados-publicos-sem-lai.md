# Dados públicos sem LAI: o que dá para saber da LICC sem pedir à SECULT ou à SEFAZ

Pedido do autor (27/09/2026): "esgotar as possibilidades de dados, dos que não precisam de LAI". Esta nota é o
inventário das rotas, com o resultado, a cobertura e o script de cada uma. O que só a LAI resolve está em
`notas/dados/02-pedidos-lai.md`. As rotas da CAP, das versões antigas dos anexos, da Wayback e do YouTube estão em
`notas/politica/04-atas-e-reunioes-publicas.md` (seções 1, 5, 7 e 10).

Regras aplicadas em todas as rotas:
- casamento só por nome normalizado exato (nunca semelhança): cada casamento é um **piso**;
- cobertura declarada em cada tabela;
- nada de dado pessoal de quem não é proponente. Pessoa física aparece só em contagem.

## 1. Inventário

| Rota | Fonte pública | Resultado | Script → saída |
| --- | --- | --- | --- |
| Perfil dos patrocinadores | Receita Federal via BrasilAPI (minhareceita.org de reserva), 134 CNPJs dos anexos de captação | feito | `analise/rede/consultas_publicas.py` → `dados/externos/cnpj_patrocinadores.csv`; `analise/14_dados_publicos.py` → `14_patrocinadores_*.csv` |
| Proponentes da LICC na Rouanet | API SALIC/MinC, PRONACs 2019-2025 (cache completo, 53.545 projetos de mecenato) | feito | `analise/15_licc_rouanet_proponentes.py` → `15_*.csv` |
| Perfil dos proponentes | Receita, 86 CNPJs de proponentes obtidos do SALIC | no relé | `consultas_publicas.py --so proponentes` → `dados/externos/cnpj_proponentes.csv` |
| Área de atuação dos proponentes | Mapa Cultural ES, 25.443 agentes | feito; refazendo com a chave canônica (os MEIs não casavam) | `consultas_publicas.py` → `mapa_agentes_proponentes.csv`; `14_proponentes_mapa_area.csv` |
| Rastro de entrega | Mapa Cultural ES, 1.738 eventos com ocorrências | feito | `14_entrega_mapa.csv` |
| Estimativa da renúncia | LDO 2023 a 2026 e PLOA 2026 (DIO e planejamento.es.gov.br) | feito (seção 5) | `dados/fontes_web/paginas/ldo_es_*.txt` |
| Lista de projetos beneficiados e renúncia executada | Portal da Transparência ES, "Incentivos, isenções e beneficiários", seções 377 e 370 | baixado como planilha ODS; conversão no relé | `buscar_fontes.py` (planilha → CSV) → `dados/fontes_web/paginas/transp377_*.txt`, `transp370_*.txt` |
| Avisos da LICC no DIO | Diário Oficial do ES, busca em texto | a busca é um app AngularJS; o script da busca foi pedido ao relé para achar a API | `raw_dio_busca_app_js*` |
| Renúncia nas contas do governador | Pareceres prévios do TCE-ES (exercícios 2023 e 2024), publicados pela SEFAZ | no relé | `tcees_parecer_previo_*` |

## 2. Quem patrocina (Receita Federal)

Fonte: `analise/tabelas/14_patrocinadores_resumo.csv`. Cobertura: 130 estabelecimentos com termo validado nos anexos de
2022 a 2026, que somam R\$ 107,48 milhões.

| Dimensão | Resultado (parcela do valor validado) |
| --- | --- |
| Porte na Receita | "Demais" (acima de EPP) 99,7%; microempresa 0,34%; EPP 0,01% |
| Natureza jurídica | limitada 36,2%; S.A. aberta 31,8% (3 empresas); S.A. fechada 30,5%; cooperativa 1,5% |
| Atividade (divisão CNAE) | eletricidade e gás 41,2% (2 estabelecimentos); veículos 21,4%; metalurgia 12,9%; varejo 10,7%; atacado 8,5% |
| Sede | RMGV 87,3%; interior do ES 12,4%; fora do ES 0,3% |
| Capital social | ≥ R\$ 100 milhões: 68,5% (15 grupos); ≥ R\$ 1 bilhão: 18,0% (6 grupos) |

Leitura para o desenho (tácita no artigo):
- a escolha de onde vai o imposto é feita por poucas empresas grandes, e quase metade dela por duas concessionárias de
  energia e gás;
- nenhum patrocinador com termo validado aparece como optante do Simples: 12 estabelecimentos "não optante" e 118 sem
  a informação na resposta. É coerente com o crédito presumido de ICMS, que não serve a quem recolhe pelo Simples: uma
  **exclusão por desenho**, não por escolha. A inferência vem da regra, não do dado, porque a cobertura do campo é
  pequena.

Limite: porte, capital e Simples são os de **hoje**, não os do ano do patrocínio.

## 3. Quem propõe: proponentes da LICC que também usam a Rouanet

Fonte: `analise/tabelas/15_licc_rouanet_resumo.csv` e `15_proponentes_licc_na_rouanet.csv`. SALIC: PRONACs de 2019 a
2025, mecenato. O cache de cada ano confere com o total da API.

| Ciclo | Proponentes | Também na Rouanet | % | % do valor autorizado na LICC |
| --- | --- | --- | --- | --- |
| 2022 | 53 | 27 | 51% | 62% |
| 2023 | 92 | 41 | 45% | 50% |
| 2024 | 95 | 45 | 47% | 54% |
| 2025 | 56 | 27 | 48% | 56% |
| 2026 | 73 | 37 | 51% | 59% |
| **2022-2026** | **235** | **95** | **40%** | **55%** (R\$ 101,7 mi de R\$ 184,0 mi) |

- Dos 95, 50 captaram algum valor na Rouanet, e 54 têm PRONAC de ano anterior ao seu primeiro ciclo na LICC.
- 7 dos 95 são pessoa física, só na contagem. 3 nomes são ambíguos (mais de um CPF/CNPJ no SALIC).
- No sentido inverso, 94 dos 445 proponentes do ES na Rouanet (2019-2025) aparecem na LICC (21%).
- Situação dos projetos 2022-2024, quem também está na Rouanet × só na LICC (do resumo, ciclos somados):
  - concluídos: 92 × 77;
  - captação expirada: 43 × 52.

  Sem teste: é descritivo e tem confusão por porte e experiência.

Leitura: a LICC reaproveita a base de proponentes profissionalizados do mecenato federal. Metade dos proponentes, com
mais da metade do valor, já operava a Rouanet. Para H4 (quem entra), isso é uma variável de experiência prévia
observável sem LAI. Não prova substituição: o proponente pode ter usado as duas leis para projetos diferentes.

Limites:
- o nome da LICC pode ser nome fantasia e o do SALIC a razão social, então 40% é piso;
- a experiência na Rouanet anterior a 2019 fica indeterminada, porque o cache começa em 2019;
- o SALIC só publica 6 dígitos do CPF.

## 4. Mapa Cultural: área de atuação e rastro de entrega

Fonte: `analise/tabelas/14_proponentes_mapa_area.csv` e `14_entrega_mapa.csv`. Primeira rodada: 117 dos 239 nomes
casados. Os MEIs não casavam, porque o nome deles na lista de habilitados traz o CPF mascarado. A correção
(`8d512de`) usa a chave canônica, que dá 235 proponentes, e o relé refaz o cruzamento.

- Tipo de agente: 98 coletivos e 19 individuais. Sede informada na RMGV: 24 de 117; a maioria não informa.
- Áreas mais frequentes, autodeclaradas e não iguais à linha de financiamento:
  - Produção Cultural: 39 proponentes;
  - Audiovisual: 33;
  - Música: 30;
  - Culturas Populares: 29;
  - Cultura e Educação: 28.
- Entrega: só 17 projetos têm evento de mesmo nome na agenda do Mapa com data a partir do ano do ciclo. Entre os
  concluídos, são 15 de 178 (8%). A agenda pública do Mapa **não serve** como verificação de entrega. Isso reforça que
  a prova de entrega (H5) depende do relatório de execução, que só sai pela LAI (pedido 2).

## 5. Renúncia estimada nas LDOs × montante fixado

Valores em R\$ mil, "Demonstrativo da estimativa e compensação da renúncia de receita" (anexo de metas fiscais):

| Documento | 2022 | 2023 | 2024 | 2025 | 2026 | Arquivo |
| --- | --- | --- | --- | --- | --- | --- |
| LDO 2023 | 0 | 10.000 | 10.000 | 10.000 | | `ldo_es_2023.txt`, l. 2853 |
| LDO 2024 | | 15.000 | 15.000 | 15.000 | 15.000 | `ldo_es_2024.txt`, l. 2909 |
| LDO 2025 | | | | tabela como imagem, sem texto | | `ldo_es_2025.txt` (só a nota f, l. 1450) |
| Montante fixado pela SEFAZ | 10.000* | 15.000 | 25.000 | 25.000 | 31.000 | `artigo/auditoria/auditoria_captacao_anual.csv` |

\* 2022: portaria de R\$ 10 mi; o anexo imprime montante de R\$ 15 mi (ver a auditoria).

- A estimativa da LDO fica abaixo do montante efetivo a partir de 2024: R\$ 15 mi estimados contra R\$ 25 mi fixados
  depois da ampliação.
- A LDO 2023 zera 2022, embora a LICC tenha captado R\$ 11,5 mi naquele ano. É um documento de previsão, não de
  execução.
- **Erro na LDO 2023**: as notas (f) e (g) trocam a finalidade. A LICC aparece como apoio "ao setor de esportes", e a
  LIEC "ao setor cultural". A LDO 2025 corrige e passa a chamar o benefício de crédito presumido (antes, "isenção").
- PLOA 2026: as ações 2298 (apoio, financiamento e incentivo à produção cultural, R\$ 24,6 mi) e 2320 (R\$ 1,6 mi) são
  despesa orçamentária da SECULT, não a renúncia da LICC. Não somar.

## 6. Resultados negativos (não repetir)

- Mapa Cultural: inscrições e fases da LICC não são públicas (`publishedRegistrations: false`).
- dados.es.gov.br: nenhum conjunto da LICC.
- licc.gov (repositório): brutos não versionados.
- Relatórios de LAI da SECULT: só até 2018.
- YouTube por espelhos: esgotado (seção 10 da nota 04).
- Habilitados não trazem CNPJ do proponente. O CNPJ vem do SALIC, só para quem também usa a Rouanet.
- LDO 2026: a tabela de renúncia não tem texto extraível.

## 7. Pendências (dependem do relé em curso)

- Converter e ler as listas de projetos beneficiados (2022-2025) e os demonstrativos de renúncia executada do Portal
  da Transparência. Conferir colunas (proponente, CNPJ, patrocinador, valor) contra os anexos da SECULT.
- Perfil dos proponentes pela Receita: natureza jurídica, idade da organização no primeiro ciclo, CNAE, sede.
- Refazer o cruzamento do Mapa com a chave canônica (entram os MEIs).
- API de busca do DIO: avisos de habilitação e de repasse com data.
- Pareceres prévios do TCE-ES: a LICC aparece no capítulo de renúncia?
