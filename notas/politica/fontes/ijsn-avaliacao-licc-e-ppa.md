---
status: conferido nas fontes (Fase A, 28/09/2026)
fontes:
  - dados/externos/dio_licc_trechos.csv (DIO-ES; ids 10230_153, 10284_5, 11289_40, 11256_6)
  - dados/fontes_web/firecrawl/ijsn_cultura_em_dados_2026.md (IJSN, notícia de 01/07/2026)
  - dados/fontes_web/firecrawl/hubes_cultura_em_dados_2026.md (HUB ES+, 30/06/2026)
  - dados/fontes_web/paginas/ppa2023_relatorio_avaliacao_2022.txt, ppa2023_relatorio_avaliacao_2023.txt,
    ppa2427_relatorio_avaliacao_2024.txt, ppa2427_relatorio_avaliacao_2025.txt (SEP, relatórios de avaliação do PPA)
---

# A avaliação oficial da LICC (IJSN/FAPES) e o lugar da LICC no PPA

Lacuna que motivou a busca: o artigo diz, na conclusão, que a LICC não tem "previsão de avaliação", e na §4.2 que não
há "meta, magnitude esperada nem indicador". O Firecrawl achou a notícia do IJSN, e o acervo do DIO, que já estava no
repositório, tinha os atos que a sustentam. Os relatórios do PPA vieram pelo relé.

## 1. A avaliação existe e está contratada (2025-2027)

**Termo de Cooperação nº 002/2025, SECULT → FAPES** (DIO-ES de 06/06/2025, id 10230_153, protocolo 1566615):

> OBJETO: Realização de projeto de pesquisa com foco na análise executiva da Lei de Incentivo à Cultura Capixaba
> (LICC), a fim de identificar oportunidades e mensurar o impacto do investimento na economia capixaba. PERÍODO DE
> EXECUÇÃO 05 de junho de 2025 a 31 de maio de 2027 RECURSOS ORÇAMENTÁRIOS: O valor total da Ação é de R$ 365.203,60

A dotação é a ação 2111, "Pesquisa e Diagnóstico das Cadeias Produtivas da Cultura". O processo é o 2024-7C4WZ.

**Objetivo declarado** (DIO-ES de 27/06/2025, id 10284_5, notícia da seleção de bolsistas pelo IJSN): "O objetivo do
projeto é avaliar de forma integrada essa política pública, identificar indicadores de monitoramento, analisar o
retorno dos investimentos e propor melhorias. Os resultados esperados incluem a criação de um plano de monitoramento,
sugestões de aprimoramento da LICC e análise de seus impactos econômicos."

**Instrumento na FAPES:** Termo de Outorga nº 633/2025, "DI 025/2024 - Análise Executiva da Lei de Incentivo à Cultura
Capixaba (PM&APP - 2024)". A coordenação foi transferida por aditivo publicado no DIO-ES de 10/07/2026 (id 11289_40).

**Resultados preliminares** (IJSN, notícia de 01/07/2026, evento "Cultura em Dados"):
- método: "análise do desenho da política e das entrevistas que coletaram a percepção dos diferentes atores
  envolvidos, incluindo proponentes de projetos culturais e empresas patrocinadoras";
- resultado citado: "efeito multiplicador de 1,74, considerando o efeito-renda. Em termos práticos, isso significa que
  cada R$ 1,00 investido gera R$ 1,74 em atividade econômica na economia capixaba";
- prazo: "A conclusão do estudo […] está prevista para o fim do segundo semestre deste ano" (2026).

**Leitura para o artigo:**
- A frase "sem previsão de avaliação" (§6) não se sustenta. Há uma avaliação contratada, com produto "estudo concluído"
  no PPA (seção 2), ainda que nenhuma norma da LICC a preveja.
- O multiplicador é uma medida de insumo-produto: mede a atividade gerada por real gasto, **supondo** que o gasto não
  ocorreria sem a LICC. É exatamente a adicionalidade que H5 põe em dúvida: 19 dos 32 recusados de 2023-2024 captaram
  depois (`analise/tabelas/22_recusados_outras_fontes_resumo.csv`). Um multiplicador não é efeito causal contra um
  contrafactual (Gertler *et al.*, 2018: "contrafactual falso" do antes-depois e do com-sem).
- Cabe na §3 (evidência sobre a LICC) como a única avaliação oficial, preliminar, não causal, e sem relatório público
  até 28/09/2026. Citar pela notícia do IJSN e pelo DIO; o relatório não foi localizado.

## 2. A LICC no PPA: sem ação, produto, indicador ou meta próprios

| Relatório | Onde a LICC aparece | Meta física ligada à LICC |
| --- | --- | --- |
| Avaliação 2022 (PPA 2020-2023), ação 2298 "Apoio, financiamento e incentivo à produção cultural" | só no texto da "situação": "SECULT ratificou a viabilidade de execução para 31 iniciativas culturais, perfazendo o valor de R$ 9.813.577,95"; em outro trecho, "34 iniciativas […] R$ 10.602.366,10" | nenhuma; os produtos da ação são os do Funcultura e do coinvestimento ("ação realizada") |
| Avaliação 2023 (PPA 2020-2023), ação 2298 | idem, só no texto da situação | nenhuma |
| Avaliação 2024 (PPA 2024-2027), ação 2298 | "foram habilitados 30 projetos […] 5,4 milhões" (31/12/2024) e "64 projetos […] 19,6 milhões" (31/7/2024) | nenhuma |
| Avaliação 2024, ação 2111 "Pesquisa e diagnóstico das cadeias produtivas da cultura" | "não houve tempo hábil para adequação do projeto apresentado junto à FAPES, que visava a execução de pesquisa da LICC" | produto "estudo concluído": meta 1 (2024-2027), executado 0 |
| Avaliação 2025 (PPA 2024-2027), ação 2111 | "formalizado termo de cooperação com a FAPES […] análise executiva da LICC" (30/6/2025) | "estudo concluído": meta 1, executado 0 até 2025 |
| Avaliação 2025, ação 2298 | "realização dos processos de análise dos projetos apresentados via LICC" | nenhuma |

**Leitura:**
- A frase da §4.2, "Não há meta, magnitude esperada nem indicador", **se confirma** no instrumento de planejamento do
  próprio governo. A renúncia não é ação orçamentária, e a LICC só aparece como narrativa dentro de uma ação de
  despesa, sem produto próprio.
- A única meta ligada a ela é a do estudo de avaliação (1 estudo, ação 2111).
- Os números de habilitados dos relatórios (31, 34, 30, 64 projetos) não batem com os anexos da SECULT (ciclo 2024:
  123 habilitados; `dados/processados/habilitados.csv`), porque medem recortes semestrais sem definição. **Não usar
  como dado**; servem só como prova de que o PPA não acompanha a LICC por indicador.
- O relatório de execução programática de 2024 (`ppa2427_execucao_programatica_2024.txt`) não menciona a LICC.

## 3. O que continua sem fonte

- Relatório ou apresentação do estudo do IJSN: não localizado. O Boletim da Economia Criativa foi anunciado, o
  relatório da LICC não.
- Número de inscritos por ciclo: nem as notícias nem a página da oportunidade 2317 do Mapa o dão. O relatório final do
  IJSN pode trazê-lo; senão, fica a LAI.
