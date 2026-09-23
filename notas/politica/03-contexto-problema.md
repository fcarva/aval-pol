# 03 — Contexto e problema/necessidade da LICC

> Nota de trabalho para a seção "Introdução com caracterização do problema/necessidade"
> do mini artigo (PECO 5046-6046). Regras: cada número com fonte e data; ausência não
> é zero; o que não foi verificado fica marcado [VERIFICAR].
>
> Status: EM CONSTRUÇÃO (gravação incremental). Iniciado em 2026-09-23.

## 0. Resumo executivo

[pendente]

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

[pendente]

## 3. Outros instrumentos de fomento no ES (mix de políticas)

[pendente]

## 4. Lei Rouanet no ES: concentração regional

[pendente]

## 5. Justificativa econômica e argumento declarado pelo governo

[pendente]

## 6. Renúncia da LICC em relação à arrecadação de ICMS do ES

[pendente]

## 7. Árvore de problemas (proposta)

[pendente]

## 8. Tabelas derivadas e scripts

[pendente]

## 9. Pendências [VERIFICAR]

[pendente]
