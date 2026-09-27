# Registro do trabalho: o repositório aval-pol e a busca de dados sobre a LICC

Mini artigo para Avaliação de Políticas Públicas (PECO 5046-6046, PPGEco/UFES).
- **Autor:** Felipe Carvalho Souza Santos.
- **Período:** 23 a 27 de setembro de 2026. Entrega em 28/09/2026.
- **Uso de IA:** o trabalho teve assistência do Claude Code (Anthropic). A declaração está em
  `artigo/declaracao-uso-ia.md`.

Este texto lista o que foi feito no repositório e o que se buscou na pesquisa de dados, com o resultado de cada busca e
onde ele está.

- **Commits:** 182 até a revisão final do artigo.
  - por dia: 14 em 23/09, 76 em 24/09 e 92 em 27/09;
  - 97 deles são devoluções automáticas do relé de coleta (seção 3).
- **Fontes coletadas:**
  - 451 arquivos de páginas e documentos convertidos em texto;
  - 158 registros de DOI;
  - 1.026 trechos do Diário Oficial;
  - dezenas de tabelas derivadas em `analise/tabelas/`.

---

## 1. O que há no repositório

| Pasta | Conteúdo |
| --- | --- |
| `artigo/` | `rascunho-artigo.md` é a fonte única do texto. `gerar_docx.py` gera o Word e `gerar_tex.py` gera o LaTeX e o PDF (confere o limite de 15 páginas). Em `auditoria/` ficam as checagens de números e referências e os pareceres das revisões |
| `analise/` | Scripts numerados de 01 a 17, mais scripts de replicação. Saídas em `tabelas/` e `figuras/` |
| `analise/rede/` | O relé de coleta (`buscar_fontes.py`, `consultas_publicas.py`) e a máscara de CPF (`mascarar_cpf.py`) |
| `dados/licc/` | Dados herdados do repositório `licc.gov`: habilitados de 2022 a 2026 e captados de 2025 |
| `dados/fontes_web/` | Tudo o que o relé trouxe: páginas, PDFs convertidos em texto, DOIs, buscas, índices seguidos, manifesto com URL, data e sha256 |
| `dados/externos/` | Bases públicas tratadas: IBGE, SICONFI, SALIC, Mapa Cultural, Receita (CNPJ), Diário Oficial |
| `dados/processados/` | Bases padronizadas: `habilitados.csv` e `transparencia_licc_termos.csv` |
| `notas/` | Sínteses: disciplina, política (com as normas transcritas em `politica/fontes/`), literatura, dados e desenho |
| `disciplina/txt/` | Texto extraído dos PDFs da disciplina, para busca |

## 2. O que foi feito, por etapa

**23/09: base e primeiro rascunho.**
- Os dados do `licc.gov` foram trazidos, e os quatro indicadores do licc.gov foram replicados.
- O material da disciplina foi extraído para texto e resumido (`notas/disciplina/`).
- Notas escritas:
  - desenho legal da LICC (lei, decreto, instruções normativas, portarias do teto, regimento da comissão);
  - contexto e problema;
  - literatura brasileira e internacional;
  - métodos e fontes de dados.
- Scripts 01 a 05:
  - carga e padronização dos anexos;
  - descritivas;
  - Rouanet no ES;
  - IBGE;
  - gasto com cultura (SICONFI);
  - escala da LICC diante do ICMS;
  - poder estatístico.
- Primeiro rascunho do artigo: 13 páginas.

**24/09: relé de coleta, auditoria e teoria da mudança.**
- **Relé de coleta:** a sessão em nuvem só alcança o GitHub. Um workflow do GitHub Actions passou a buscar as fontes
  com rede aberta e a devolvê-las por commit (seção 3).
- **Auditoria do artigo:** cada número foi recalculado e conferido com a fonte (`checar_dados.py`), e cada referência
  com a Crossref e o OpenAlex (`checar_referencias.py`).
  - Houve rodadas de revisão por painel de pareceres (Stage 3, rodadas 1 e 2) e correções.
  - A captação de 2023 a 2025 foi auditada termo a termo (`auditar_captacao.py`).
- **Teoria da mudança:** desenho causal da alocação de bens públicos culturais, hipóteses, Figura 1 redesenhada e
  auditoria das premissas.
- **Versão LaTeX** do artigo, tabelas abertas e hiperlinks para dados e DOIs.
- **Proteção de dados:** os CPFs impressos nos anexos da SECULT foram mascarados.

**27/09: nova moldura e dados públicos.**
- **Hipóteses reorientadas:** marketing, decisão concentrada, taxa de serviço, exclusão e entrega. Houve a terceira
  rodada de pareceres e suas correções.
- **Rotas de dados sem LAI:**
  - atas da comissão;
  - versões antigas dos anexos;
  - Wayback Machine;
  - Mapa Cultural;
  - Receita Federal;
  - Portal da Transparência;
  - Diário Oficial;
  - LDO;
  - TCE-ES.

  Scripts 11 a 17 (seção 4).
- **Revisão dos trechos grifados pelo autor:**
  - Hitzig e bens públicos;
  - economia criativa;
  - clareza;
  - quadros atualizados;
  - voz impessoal (autor único);
  - revisão do português.
- **Resultado:** 15 páginas, 58 checagens de números, 75 conferências da captação e 55 referências, sendo 19 com DOI
  conferido.

## 3. Como a busca foi feita: o relé

Da sessão em nuvem só se alcança o GitHub. A busca foi montada assim:
- o autor, ou o assistente, escreve o pedido num arquivo de `dados/fontes_web/`;
- o push dispara o workflow `.github/workflows/buscar-fontes.yml`;
- o workflow coleta com rede aberta e devolve o resultado por commit ("buscar-fontes: ...");
- HTML, PDF, Word e planilhas (ODS, XLSX) viram texto;
- toda página tem cabeçalho com URL, data da coleta e sha256, e entra no `manifesto.csv`.

| Arquivo de pedidos | Para quê | Entradas |
| --- | --- | --- |
| `pedidos.tsv` | páginas e PDFs avulsos | 287 |
| `seguir.tsv` | índice + todos os links que casam com um padrão (ex.: extratos das atas) | 14 |
| `dois.txt` | metadados de DOI (Crossref, OpenAlex) | 164 |
| `buscas.tsv` | busca bibliográfica por título/autor | 21 |
| `videos.tsv`, `canais.tsv` | legendas do YouTube e lista de vídeos de canais | 10 e 3 |
| `consultas_publicas.py` | APIs: Receita (CNPJ), Mapa Cultural, Diário Oficial, Portal da Transparência | — |

## 4. O que se buscou, fonte por fonte

### 4.1 Encontrado e usado

| Fonte | O que se buscou | Resultado | Onde está |
| --- | --- | --- | --- |
| **Normas** (Lei 11.246/2021, Decreto 5.035-R/2021, INs 2022 a 2026, portarias SEFAZ do teto, regimento da comissão, LC 123/2006) | regras de cada ano | transcritas e conferidas; teto por projeto de 2022 a 2026 | `notas/politica/fontes/`, `analise/11_teto_projeto_e_linhas.py` |
| **Anexos da SECULT** (habilitados e captados, 2022 a 2026) | quem foi habilitado, quem captou, quanto | base do artigo; totais conferidos ao centavo | `dados/licc/`, `artigo/auditoria/` |
| **Extratos das atas da comissão (CAP)**, 2022 a 2026 | inabilitados e datas de habilitação | 158 reuniões com deliberação, 86 projetos inabilitados (15% dos deliberados), sem motivo publicado | `analise/12_atas_cap.py` |
| **Versões antigas dos anexos** no servidor da SECULT | a fila ao longo do ano | 18 versões recuperadas; em 2024, 23 termos (R\$ 5,04 mi) recusados antes e validados depois da ampliação do teto | `analise/13_versoes_anexos.py` |
| **Wayback Machine** (Internet Archive) | documentos que saíram do ar | 83 arquivos da LICC nunca coletados; listas de habilitados datadas de 2022 e 2023 | `notas/politica/04-...` §10 |
| **Portal da Transparência do ES**, seção 07 | termos por projeto | **achado principal**: 2022 a 2025, cada termo com processo, data, patrocinador, **proponente com CNPJ** e valor; totais de 2023 a 2025 iguais aos da SECULT | `analise/16_transparencia_licc.py` |
| **Portal da Transparência**, seção 08 | renúncia prevista e realizada | realizada: R\$ 11,7 mi (2022), 15 mi, 25 mi e 25 mi (= teto); erros nas notas da LDO 2023 | `16_renuncia_sefaz.csv` |
| **LDO 2023 a 2026 e PLOA 2026** | estimativa da renúncia | previsão abaixo do realizado em 2024 e acima em 2025 | `notas/dados/03-...` §3 |
| **Receita Federal** (BrasilAPI, minhareceita.org) | perfil de patrocinadores (134 CNPJs) e proponentes (107) | patrocinadores grandes, de energia, veículos e metalurgia, com sede na RMGV; proponentes antigos, associações e limitadas, 75% do valor na RMGV | `analise/14_dados_publicos.py`, `17_proponentes_receita.py` |
| **Mapa Cultural do ES** (API) | agentes (25.443), projetos (2.373), eventos (1.738), oportunidades e fases da LICC | 131 de 235 proponentes com agente de mesmo nome; só 15 dos 178 projetos concluídos com evento datado | `analise/14_dados_publicos.py` |
| **Diário Oficial do ES** (API de busca, achada no script do site) | atos da LICC | 1.026 trechos coletados (485 páginas com o nome da lei, 529 com "LICC"); **ainda não analisados** | `dados/externos/dio_licc_trechos.csv` |
| **Funcultura, edital 29/2025** | contraste com seleção por nota | ata de julgamento: nota, linha e porte do município | `analise/11_...` |
| **IBGE** (SIIC, MUNIC 2021, Censo 2022, PIB) e **SICONFI** | contexto e problema | setor cultural no ES; cinema e fundo municipal; gasto estadual com cultura | scripts 02, 03b, 03c |
| **Boletim de Economia Criativa** (SECULT, 2017 a 2020) | economia criativa no ES | 8,2% dos ocupados (2º tri 2020), 8ª posição | `boletim_ec_*` |
| **SALIC** (Lei Rouanet) | contexto e substituição de fonte | 53.545 projetos de mecenato (2019-2025); patrocinadores da LICC na Rouanet. Mantido como registro, fora do artigo (foco só na LICC) | scripts 03a e 15 |
| **Lei de Incentivo à Cultura do RS** | análogo com seleção por nota | usado no artigo (H2) | `notas/politica/fontes/rs-lic-analogo.md` |
| **Literatura** | referências verificadas | 158 registros de DOI; Buterin, Hitzig e Weyl (2019) conferido; página de Hitzig (2021) indicada pelo autor | `dados/fontes_web/doi/`, `buscas/` |

### 4.2 Buscado e não encontrado (não repetir)

| Fonte | O que se buscou | Resultado |
| --- | --- | --- |
| Mapa Cultural, inscrições da LICC | linha de fomento, parecer, inabilitados | inscrições não públicas; a linha existe no sistema, como categoria da inscrição |
| Repositório `licc.gov` | dados brutos | não versionados lá |
| dados.es.gov.br | conjuntos da LICC | nenhum |
| Relatórios de LAI da SECULT | pedidos anteriores | só até 2018 |
| YouTube (lives da LICC) | transcrições em português | bloqueado no GitHub ("confirme que não é um robô"); espelhos (Invidious, Piped) sem legenda; 100 vídeos listados para obter localmente |
| Pareceres prévios do TCE-ES (contas de 2023 e 2024) | análise da renúncia da LICC | a LICC não aparece |
| Relatórios de gestão do governador (2022 a 2025) | números da LICC | a LICC não aparece |
| Portal, relação de beneficiários (2022 a 2025) | crédito da LICC por empresa | só o total renunciado por contribuinte, sem separar a LICC |
| Portal, dicionário de dados (2021) | significado da "data do processo" | anterior à lista da LICC; não define o campo |
| Planilhas "controle mensal" | fila da LICC | eram de outro edital (Circulação) |
| Manual de marcas LICC/Funcultura | regra de proporção da marca | PDF só com imagem |
| Firecrawl, Parallel, WebFetch | leitura direta de páginas | sem crédito, com limite atingido ou bloqueados; tudo passou pelo relé |

### 4.3 O que só a LAI resolve

Estão em `notas/dados/02-pedidos-lai.md`: quatro pedidos à SECULT e à SEFAZ.
- inscrições com linha, parecer e motivo da inabilitação;
- planilhas de custos e relatórios de execução (público alcançado);
- atas completas da comissão;
- fila da SEFAZ, com data de protocolo, cota e indeferidos.

O prazo da LAI (20 dias mais 10) não cabe antes da entrega. O Portal da Transparência já responde parte do quarto
pedido, porque traz uma data que ordena a fila.

## 5. Regras seguidas em toda a busca

- **Ausência não é zero:** onde a fonte não publica, o dado fica ausente e a cobertura é declarada.
- **Proveniência:** todo número do artigo aponta o arquivo e o script que o produzem. `checar_dados.py` recalcula cada
  um.
- **Norma lida não é cumprimento apurado:** onde o dado não permite apurar, o texto diz "indeterminado".
- **Referências:** só entra referência conferida (DOI, Crossref, OpenAlex, página oficial).
- **Casamento de bases:** só por chave exata (CNPJ, processo ou nome normalizado), nunca por semelhança; cada
  casamento é um piso.
- **LGPD:**
  - CPF sempre mascarado, inclusive o que vem colado ao nome do MEI na razão social da Receita;
  - dados de pessoas que não são proponentes não são gravados;
  - dos arquivos grandes (beneficiários de incentivos), só as linhas da LICC.

## 6. Pendências

- ~~Analisar os 1.026 trechos do Diário Oficial~~: feito para os avisos de habilitação (CNPJ de 83% dos habilitados, com o Portal) e de depósito (386 depósitos datados), em `analise/18_dio_avisos_habilitacao.py`. Faltam as portarias do teto e as designações da comissão.
- Revisão da rodada 4 (painel ARS completo, poder refeito em `analise/19_poder_revisao.py`): `artigo/auditoria/revisao-stage3-r4/`; os itens RV4-1 a RV4-4 aguardam a decisão do autor.
- Obter as transcrições do YouTube localmente (`yt-dlp` com cookies do navegador) ou pela opção "Mostrar
  transcrição".
- Enviar os pedidos de LAI; o material serve para a 2ª parte da disciplina.
- Adaptar a declaração de uso de IA ao modelo da disciplina antes da entrega.
- Decidir se o histórico do git deve ser reescrito para apagar CPFs de MEI de commits antigos. Os arquivos atuais estão
  mascarados.
