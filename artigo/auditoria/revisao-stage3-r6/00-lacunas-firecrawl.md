# Fase A (r6): lacunas de dados e contexto fechadas com o Firecrawl e o relé

- **Pedido do autor (28/09/2026):** "coloque o pipeline de dados para rodar, com o firecrawl funcionando agora para
  fechar lacunas de contexto antes perdidas; vamos focar full nisso por enquanto".
- **O artigo não foi editado nesta fase.** As propostas de texto da última coluna vão para a Fase B, com aprovação do
  autor (plano em `/root/.claude/plans/rustling-orbiting-popcorn.md`).

## Como se coletou

| Rota | O que faz | Registro |
| --- | --- | --- |
| Firecrawl (ferramenta da sessão; sem chave no ambiente) | busca na web e raspagem de páginas HTML, inclusive as que o relé recebeu com 403 | `dados/fontes_web/firecrawl/*.md`; manifesto com sha256 por `analise/rede/registrar_firecrawl.py` (`--conferir`: 4/4) |
| Relé (`buscar-fontes.yml`) | PDFs grandes e APIs achados pelo Firecrawl | `dados/fontes_web/pedidos.tsv` → `dados/fontes_web/paginas/*.txt`, manifesto do relé |
| Acervo já coletado | releitura dirigida dos 1.026 trechos do DIO (`dados/externos/dio_licc_trechos.csv`) | notas abaixo |

## Pipeline

- Os 30 scripts numerados de `analise/` (01 a 22) rodaram em sequência, sem erro.
- Única diferença nas saídas: a correção do parser do DIO (script 18). O cabeçalho corrido da página ("DIÁRIO OFICIAL
  DOS PODERES DO ESTADO" e o número da página) caía no meio dos avisos que atravessam a página. Efeitos:
  - dois depósitos se perdiam: 13ª Italia Unita, R$ 75 mil, 06/08/2025; e uma parcela da Orquestra Brasileira de
    Cantores Cegos, 24/11/2022;
  - agora são 389 avisos lidos (eram 386) e 268 de 325 termos com depósito localizado (82%; 77,7% do valor);
  - o número que o artigo usa (82% dos termos) não muda.
- Checagens depois: `checar_dados.py` 80/80; `auditar_captacao.py` 75/75; `checar_referencias.py` 50 referências;
  `mascarar_cpf.py --conferir` 0.
- Scripts novos:
  - `21_etapas_captacao.py` concilia, por ano, o termo listado no anexo, o Portal, a renúncia realizada e os depósitos;
  - `22_recusados_outras_fontes.py` procura os 32 recusados de 2023-2024 em fontes independentes da LICC.

## Lacuna por lacuna

| # | Lacuna | Rota | Resultado | Situação | Afirmação do artigo afetada → proposta (Fase B) |
| --- | --- | --- | --- | --- | --- |
| 1 | Avaliação da LICC | Firecrawl (IJSN, HUB ES+); DIO já coletado; relé (PPA 2024 e 2025) | Avaliação oficial contratada (detalhes abaixo) | **Fechada** (`notas/politica/fontes/ijsn-avaliacao-licc-e-ppa.md`) | §6 "sem […] previsão de avaliação" → não se sustenta. §3 ganha uma frase: a única avaliação oficial é preliminar e de insumo-produto, e supõe a adicionalidade que H5 testa |
| 2 | Metas e indicadores | Relé: relatórios de avaliação do PPA de 2022 a 2025 e execução programática de 2024 | A LICC não tem ação, produto, indicador ou meta próprios. Aparece só no texto da ação 2298; a única meta ligada é "1 estudo concluído" (ação 2111) | **Fechada, confirma o artigo** | §4.2 "Não há meta, magnitude esperada nem indicador" → mantida, com a fonte do PPA |
| 3 | Etapas da captação (ponto 2 do parecer) | Script 21 com dados já no acervo | Em 2023, 2024 e 2025, anexo = Portal = renúncia realizada = montante. O projeto "em análise na SEFAZ" de 2025 (13ª Italia Unita) tem os mesmos R$ 356.135,99 em cinco termos no Portal e em cinco avisos de depósito (jul.-ago./2025). A composição difere: o anexo lista quatro termos, um deles de um patrocinador (Oriundi) que não aparece no Portal, onde estão só Imetame e Comercial Devens Em 2022 o Portal soma R$ 146.910,22 a mais que o anexo, diferença já explicada | **Fechada** (`21_etapas_captacao.csv`, `21_em_analise_2025.csv`) | §1: "esgotou o teto" pode ser dito etapa a etapa; o termo em análise foi validado e depositado depois (Portal e DIO) |
| 4 | Resultado de H5 para os recusados | Script 22 (LICC nos anos seguintes, SALIC, agenda do Mapa) | Detalhes abaixo | **Reduzida**: mede-se a cobertura, e ela é baixa no nível do projeto | §5, H5: confirma o parecer. O resultado precisa de pesquisa de acompanhamento com os dois grupos, conferida nesses registros |
| 5 | Teixeira *et al.* (2021) | Firecrawl na SciELO (o relé recebeu 403) | Confere com o resumo: concentração na RMBH; museu, teatro e cinema aumentam as chances de captar | **Conferida** | §3 chama as avaliações estaduais de "descritivas"; o estudo usa regressão logística, logo "correlacionais, não causais" é mais exato |
| 6 | Objetivo declarado das regras de 2025-2026 | Firecrawl: reportagem do Século Diário de 23/01/2026 (nomes privados omitidos) | Nota oficial da SECULT: o limite de três projetos por CNPJ "busca evitar a concentração de recursos e ampliar o acesso de novos agentes culturais"; as reservas de 2025 vieram de "ampla escuta pública". O setor critica barreiras de acesso e a "política concentradora" | **Contexto** | §4.2 (H4): a desconcentração e a entrada de novos agentes são objetivo declarado pela SECULT, não só uma premissa inferida; fonte jornalística com nota oficial |
| 7 | Número de inscritos (Tabela 1) | Firecrawl: notícias e oportunidade 2317 do Mapa; relé na mesma página | Nenhuma contagem pública | **Mantida** | Tabela 1 continua "não publicado" |
| 8 | Origem e justificativa da Lei 11.246/2021 (Assembleia) | Firecrawl em `www3.al.es.gov.br` | Erro de túnel do proxy do Firecrawl, duas vezes (o relé também não alcança) | **Mantida** (negativo registrado) | nenhuma |
| 9 | Lives da SECULT (YouTube) | Firecrawl na página do vídeo | Volta só a página, sem transcrição (o relé é barrado como robô) | **Mantida** (negativo) | nenhuma; o artigo não cita as lives |
| 10 | SALIC (API antiga `/incentivadores` com 404) | Firecrawl achou a documentação nova (`api.salic.cultura.gov.br/docs`); o relé a baixou | Endpoints atuais `/api/v1/projetos`, `/proponentes`, `/propostas`, `/fornecedores`. O cache de PRONACs 2019-2025 já cobre o script 22 | **Reduzida** | nenhuma |
| 11 | População elegível para H4 (pessoa jurídica cultural por município) | Catálogo do Firecrawl sem base de CNPJ; dados abertos da Receita pelo relé seriam possíveis | Não executado (opcional no plano) | **Mantida** | Fase B usa os 257 coletivos do Mapa como piso, como no plano |

**Detalhe da lacuna 1.** A avaliação oficial é o Termo de Cooperação SECULT–FAPES nº 002/2025 (DIO-ES de 06/06/2025):
- valor de R$ 365.203,60;
- execução de 05/06/2025 a 31/05/2027;
- objeto: "análise executiva da LICC […] mensurar o impacto do investimento na economia capixaba".

Os resultados preliminares foram divulgados em 01/07/2026: "efeito multiplicador de 1,74, considerando o
efeito-renda", com entrevistas com proponentes e patrocinadores. O relatório final está previsto para o fim de 2026 e não
foi localizado.

**Detalhe da lacuna 4.** Dos 32 recusados, 23 têm algum registro depois:
- 19 captaram pela LICC em ano posterior;
- 11 têm o proponente com PRONAC captado na Rouanet a partir do ano da recusa;
- 1 tem PRONAC com o mesmo título;
- 1 tem evento datado no Mapa.

Nove não aparecem em fonte nenhuma. Fora da própria LICC, só 2 registros são do projeto em si.

## O que a Fase A muda na leitura do artigo (para a Fase B)

1. **Conclusão e §3.** O Estado contratou uma avaliação, mas de insumo-produto: mede a atividade econômica por real
   gasto e supõe que nada ocorreria sem o incentivo. O artigo pode dizer isso com fonte oficial. Reforça a proposta da
   §5, que testa justamente a adicionalidade (H5) e quem decide (H1-H4).
2. **§4.2.** "Sem meta nem indicador" passa a ter prova documental no PPA.
3. **§1 e parecer.** A objeção das "etapas" se resolve com dado: nas três etapas observáveis a captação de 2023-2025
   bate o montante ao centavo.
4. **§5, H5.** A linha de base do resultado dos recusados mostra por que o desenho precisa de pesquisa de
   acompanhamento dos dois grupos: fora da LICC, os registros públicos cobrem só 2 dos 32 projetos.
