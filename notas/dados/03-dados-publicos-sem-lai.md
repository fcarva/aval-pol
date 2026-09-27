# Dados públicos sem LAI: o que dá para saber da LICC sem pedir à SECULT ou à SEFAZ

Pedidos do autor (27/09/2026):
- "esgotar as possibilidades de dados, dos que não precisam de LAI";
- depois, "focar apenas na LICC".

Esta nota é o inventário das rotas, com o resultado, a cobertura e o script de cada uma. O que só a LAI resolve está
em `notas/dados/02-pedidos-lai.md`. As rotas da CAP, das versões antigas dos anexos, da Wayback e do YouTube estão em
`notas/politica/04-atas-e-reunioes-publicas.md` (seções 1, 5, 7 e 10).

Regras aplicadas em todas as rotas:
- casamento só por chave exata (CNPJ, processo ou nome normalizado), nunca por semelhança;
- cobertura declarada em cada tabela;
- nenhum dado pessoal além do que a fonte oficial já publica sobre proponentes e patrocinadores;
- CPF sempre mascarado. `mascarar_cpf.py` passou a pegar também o CPF colado ao nome do MEI quando a célula seguinte
  começa por dígitos (32 casos nas planilhas do Portal). As versões antigas desses dois arquivos continuam no histórico
  do git.

## 1. Inventário

| Rota | Fonte pública | Resultado | Script → saída |
| --- | --- | --- | --- |
| **Termos por projeto, com CNPJ do proponente** | Portal da Transparência ES, seção 07 (Download/378, 379, 439, 536) | **feito** (seção 2) | `analise/16_transparencia_licc.py` → `dados/processados/transparencia_licc_termos.csv`, `16_*.csv` |
| **Renúncia realizada** | Portal da Transparência ES, seção 08 (Download/376, 426, 486, 545, 546) | **feito** (seção 3) | `16_renuncia_sefaz.csv` |
| Perfil dos patrocinadores | Receita Federal via BrasilAPI (minhareceita.org de reserva), 134 CNPJs dos anexos | feito (seção 4) | `consultas_publicas.py` → `dados/externos/cnpj_patrocinadores.csv`; `14_patrocinadores_*.csv` |
| Perfil dos proponentes | Receita, 107 CNPJs de proponentes das listas do Portal | **feito** (seção 2A) | `consultas_publicas.py` → `dados/externos/cnpj_proponentes.csv`; `analise/17_proponentes_receita.py` → `17_*.csv` |
| Área de atuação dos proponentes | Mapa Cultural ES, 25.443 agentes | feito: 131 de 235 proponentes (seção 5) | `mapa_agentes_proponentes.csv`; `14_proponentes_mapa_area.csv` |
| Rastro de entrega | Mapa Cultural ES, 1.738 eventos com ocorrências | feito (seção 5) | `14_entrega_mapa.csv` |
| Estimativa da renúncia | LDO 2023-2026, PLOA 2026 | feito (seção 3) | `dados/fontes_web/paginas/ldo_es_*.txt` |
| Atos da LICC no DIO | Diário Oficial do ES, rota de busca `/busca/busca/buscar/query/<pág>/di:AAAA-MM-DD/df:AAAA-MM-DD/?1=1&q="termo"` (lida no script do site, `raw_dio_busca_app_js2.txt`) | **coletado**: 485 páginas com "Lei de Incentivo à Cultura Capixaba", 529 com "LICC", 1.026 trechos (a analisar) | `consultas_publicas.py` → `dados/externos/dio_licc_trechos.csv` |
| Renúncia total dos patrocinadores | Portal, "Relação de beneficiários e valores renunciados" 2022-2025 (CNPJ, razão social, total; todos os incentivos somados, sem separar a LICC) | no relé: linhas dos patrocinadores da LICC | `transparencia_beneficiarios_licc.csv` |
| Relatórios de gestão do governador (2022-2025) | SEFAZ, prestação de contas | no relé | `sefaz_relatorio_gestao_*` |
| Renúncia nas contas do governador | Pareceres prévios do TCE-ES (exercícios 2023 e 2024) | **negativo**: a LICC não aparece | `tcees_parecer_previo_*.txt` |

Fora do foco (só LICC), mantido como registro: o cruzamento dos proponentes com a Rouanet
(`analise/15_licc_rouanet_proponentes.py`). Resultado: 95 de 235 proponentes também têm PRONAC de mecenato em
2019-2025, e respondem por 55% do valor autorizado. Não entra no artigo nem será ampliado.

## 2. Termos por projeto no Portal da Transparência (a melhor fonte pública da LICC)

A planilha "Projetos beneficiados pela Lei de Incentivo à Cultura Capixaba" (2022 a 2025) traz, por termo:
- número do processo (o mesmo da lista de habilitados);
- "data do processo";
- projeto;
- CNPJ e nome do patrocinador;
- **CNPJ e nome do proponente**;
- valor.

Não há ainda planilha de 2026.

**Conferência com os anexos da SECULT** (`16_transparencia_resumo.csv`, `16_transparencia_x_anexo.csv`):

| Ano de captação | Termos (Portal) | Soma (Portal) | Soma (anexo SECULT) | Termos que casam (CNPJ × valor) |
| --- | --- | --- | --- | --- |
| 2022 | 48 | R\$ 11.686.151,29 | R\$ 11.539.241,07 | 44 de 47 |
| 2023 | 71 | R\$ 15.000.000,00 | R\$ 15.000.000,00 | 70 de 71 |
| 2024 | 110 (+4 com valor zero) | R\$ 25.000.000,00 | R\$ 25.000.000,00 | 103 de 109 |
| 2025 | 96 (+1 com valor zero) | R\$ 25.000.000,00 | R\$ 25.000.000,00 | 93 de 95 |

- 2023-2025 fecham ao centavo.
- Em 2022 o Portal soma R\$ 146.910,22 a mais que o anexo da SECULT, e a diferença se explica toda:
  - um termo de R\$ 150.000,00 (processo 2022-RWW2K, festival de jazz, patrocinador sociedade anônima) está no
    Portal e não no anexo;
  - três valores divergem por digitação: R\$ 311.332,22 × 311.332,00; R\$ 314.563,15 × 314.653,15; R\$ 465.965,00 ×
    468.965,00.

  A renúncia realizada informada pela SEFAZ é a do Portal (R\$ 11,686 mi, seção 3). Qual digitação está certa é
  indeterminado.
- **100% dos 204 processos** do Portal estão na lista de habilitados: o CNPJ do proponente passa a existir para todo
  projeto que captou em 2022-2025.
- CNPJ do proponente: 107 distintos com dígito verificador válido. Seis termos de 2024 (R\$ 751 mil, um proponente)
  têm CNPJ com 13 dígitos e ficam marcados, sem correção.

**Concentração por proponente (CNPJ)** (`16_concentracao_proponentes.csv`), 2022-2025:
- 107 proponentes captaram R\$ 75,9 mi;
- os 10 maiores têm 30% do valor;
- **44 proponentes (41%) captaram em mais de um ano e ficam com 68% do valor**.

Por ano, a parcela dos 10 maiores cai de 56% (2022) para 35-43% (2023-2025).

**Relação patrocinador × proponente** (`16_pares_recorrentes.csv`): de 222 pares (raiz do CNPJ do patrocinador ×
CNPJ do proponente), 48 se repetem em mais de um ano e concentram 43,6% do valor. Para H1, é a relação de patrocínio
que se renova, observável sem LAI.

**Fila** (`16_fila_por_mes.csv`, `16_data_processo_x_recebimento_2025.csv`):
- A "data do processo" **não é a data de recebimento do termo**. Em 2025 o anexo da SECULT imprime data e hora de
  recebimento, e nos 62 termos comparáveis a data do Portal vem sempre depois: mediana de 19 dias, de 2 a 377. A ordem,
  porém, é quase a mesma (correlação de postos 0,91). Serve como ordem aproximada da fila, com defasagem. O que ela
  data (validação? registro?) fica indeterminado.
- Com essa ressalva:
  - 2023: o montante de R\$ 15 mi se esgota em 18/07/2023;
  - 2024: R\$ 13,5 mi estão processados até fevereiro, e os R\$ 15 mi do montante inicial, até 14/03/2024. Isso bate
    com as versões (0) a (4) do anexo: 58 termos, R\$ 15 mi, antes da ampliação;
  - 2025: R\$ 19,0 mi (76% dos R\$ 25 mi) até fevereiro;
  - 2022: o ano fecha em R\$ 11,7 mi, abaixo do limite, sem esgotar.
- É a corrida do primeiro trimestre, descrita com dado oficial. A data exata de protocolo continua no pedido 4 da LAI.

## 2A. Quem capta: perfil dos proponentes na Receita

Fonte: `17_proponentes_resumo.csv` e `17_mesma_sede.csv`. Os 107 CNPJs de proponentes que captaram em 2022-2025
(R\$ 75,9 mi) têm resposta da Receita. Porte, natureza e sede são os de hoje.

| Dimensão | Resultado (parcela do valor captado) |
| --- | --- |
| Natureza jurídica | associação privada 47% (45 proponentes); sociedade limitada 46% (49); fundação 4%; empresário individual 3% (8) |
| Porte | "demais" 51%; microempresa 35% (48); EPP 14% |
| MEI hoje | 4 proponentes, 1% do valor |
| Atividade (CNAE) | organizações associativas 40%; cinema e vídeo 18%; atividades artísticas e de espetáculos 16%; eventos (8230) 7% |
| Sede | RMGV 75% (78 proponentes); interior 25% (29) |
| Idade no ano da primeira captação | 10 anos ou mais 59% (65 proponentes); 5 a 10 anos 17%; 3 a 5 anos 11%; 1 a 3 anos 13%; **nenhum com menos de 1 ano** |

- Quem capta é, em regra, organização antiga, da RMGV, associação ou produtora limitada. A regra de dois anos de sede
  explica a ausência de CNPJ novo, mas não o peso das organizações com dez anos ou mais: incumbência, para H4.
- Patrocinador e proponente com sede no mesmo município: 24% a 32% do valor por ano (2022-2025).

## 3. Renúncia prevista e realizada (SEFAZ)

Fonte: demonstrativos da estimativa e execução da renúncia (Portal da Transparência, seção 08), linha "Incentivo à
Cultura" (Lei 11.246/2021, crédito presumido). Valores em R\$ mil (`16_renuncia_sefaz.csv`, trecho conferido no arquivo):

| Ano | Prevista | Realizada | Montante fixado (portarias; `auditoria_captacao_anual.csv`) |
| --- | --- | --- | --- |
| 2022 | 0 (LDO 2023 zera 2022) | **11.686** | 10.000 (portaria) / 15.000 (limite impresso no Portal e no anexo) |
| 2023 | 10.000 (LDO 2023) | **15.000** | 15.000 |
| 2024 | 15.000 (LDO 2024) | **25.000** | 25.000 (após a ampliação) |
| 2025 | 30.000 | **25.000** | 25.000 |
| 2026 | 70.000 para "Artes, Cultura, Esporte e Recreação", somados (LDO 2026) | | 31.000 |

- A renúncia realizada é igual ao montante fixado em 2023-2025: o teto amarra, e a execução é de 100%.
- A LDO 2023 zera 2022, embora a LICC tenha captado no ano.
- A previsão da LDO fica abaixo do realizado em 2024 (R\$ 15 mi contra R\$ 25 mi) e acima em 2025 (R\$ 30 mi contra
  R\$ 25 mi). A previsão não acompanha as ampliações por portaria.
- **Erros nos documentos oficiais**:
  - o demonstrativo de 2023 e a LDO 2023 trocam as finalidades da LICC e da LIEC nas notas (f) e (g): a LICC aparece
    "para apoiar o setor de esportes";
  - o demonstrativo de 2023 cita a "Lei nº 11.246/2001" (é 2021).
- PLOA 2026: as ações 2298 (R\$ 24,6 mi) e 2320 (R\$ 1,6 mi) são despesa da SECULT, não a renúncia da LICC. Não somar.

## 4. Quem patrocina (Receita Federal)

Fonte: `analise/tabelas/14_patrocinadores_resumo.csv`. Cobertura: 130 estabelecimentos com termo validado nos anexos de
2022 a 2026, que somam R\$ 107,48 milhões.

| Dimensão | Resultado (parcela do valor validado) |
| --- | --- |
| Porte na Receita | "Demais" (acima de EPP) 99,7%; microempresa 0,34%; EPP 0,01% |
| Natureza jurídica | limitada 36,2%; S.A. aberta 31,8% (3 empresas); S.A. fechada 30,5%; cooperativa 1,5% |
| Atividade (divisão CNAE) | eletricidade e gás 41,2% (2 estabelecimentos); veículos 21,4%; metalurgia 12,9%; varejo 10,7%; atacado 8,5% |
| Sede | RMGV 87,3%; interior do ES 12,4%; fora do ES 0,3% |
| Capital social | ≥ R\$ 100 milhões: 68,5% (15 grupos); ≥ R\$ 1 bilhão: 18,0% (6 grupos) |

- Nenhum patrocinador com termo validado aparece como optante do Simples: 12 estabelecimentos "não optante", 118 sem a
  informação.
- Isso é coerente com o crédito presumido de ICMS, que não serve a quem recolhe pelo Simples: uma **exclusão por
  desenho**. A inferência vem da regra, não do dado.
- Limite: porte, capital e Simples são os de hoje, não os do ano do patrocínio.

## 5. Mapa Cultural: área de atuação e rastro de entrega

Fonte: `14_proponentes_mapa_area.csv` e `14_entrega_mapa.csv`. Com a chave canônica, 131 dos 235 proponentes casam com
um agente de mesmo nome. Na primeira rodada eram 117, porque os MEIs não casavam: o nome na lista de habilitados traz o
CPF mascarado.

- 99 agentes coletivos e 32 individuais. Sede informada na RMGV: 27 de 131; a maioria não informa.
- Áreas autodeclaradas (não são a linha de financiamento): Produção Cultural, Audiovisual, Música e Culturas Populares
  lideram.
- Entrega: só 17 projetos têm evento de mesmo nome na agenda do Mapa com data a partir do ano do ciclo. Entre os
  concluídos, são 15 de 178 (8%). A agenda pública **não serve** para verificar entrega: isso depende do relatório de
  execução (LAI, pedido 2).

## 6. Resultados negativos (não repetir)

- Mapa Cultural: inscrições e fases da LICC não são públicas (`publishedRegistrations: false`). A linha de
  financiamento só sai pela LAI.
- TCE-ES, pareceres prévios das contas de 2023 e 2024: a LICC não aparece.
- dados.es.gov.br: nenhum conjunto da LICC.
- licc.gov (repositório): brutos não versionados.
- Relatórios de LAI da SECULT: só até 2018.
- YouTube por espelhos: esgotado.
- LDO 2025 e 2026: tabela de renúncia sem texto extraível. Os valores vêm dos demonstrativos do Portal (seção 3).

## 7. O que muda nos pedidos de LAI

- Pedido 4 (fila da SEFAZ), em parte respondido sem LAI:
  - o Portal dá patrocinador, proponente, valor e uma data que ordena a fila (correlação 0,91 com o recebimento);
  - o anexo de 2025 dá data e hora de recebimento.

  Continuam na LAI a data de protocolo de 2022-2024, a cota do art. 18 de cada termo e os indeferidos.
- Pedido 1: o CNPJ do proponente deixa de ser necessário para quem captou. Os que não captaram continuam sem CNPJ.
