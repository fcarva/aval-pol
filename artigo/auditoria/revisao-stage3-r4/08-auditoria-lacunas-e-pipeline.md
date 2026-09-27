# Auditoria de lacunas de dados e do pipeline (rodada 4)

**Pedido do autor (27/09/2026):** "Auditar contra lacuna de dados e pipeline de dados, buscar o que foi extraído e ver
se contempla, e seguir com revisões, seguir conferir o pdf e gerar zip no final".

## 1. Pipeline: reprodutibilidade

Todos os 27 scripts numerados de `analise/` (`01_carregar.py` a `19_poder_revisao.py`) foram rodados em sequência,
sem rede. Todos terminaram sem erro, e as saídas foram comparadas com as versionadas. Três defeitos apareceram e foram
corrigidos (commit `c3cd882`):

| Defeito | Efeito | Correção |
| --- | --- | --- |
| A máscara de CPF ("XXXXXXXXXXX") entrava na chave do proponente e tirava o MEI da regra de natureza jurídica | Ao regenerar, o mesmo proponente podia virar duas chaves, e o MEI podia cair em "indeterminado" | `01_carregar.py`: a chave e a regra reconhecem o CPF mascarado; a saída volta a coincidir com a versionada (só muda a ordem de duas variantes de nome) |
| `mascarar_cpf.py` tomou por CPF o capital social de 11 dígitos da Receita (Ambev, ArcelorMittal, Claro) | Faixas de capital social de `14_patrocinadores_resumo.csv` mudariam ao regenerar (≥ R$ 1 bilhão: de 7 para 4 estabelecimentos) | Valores restaurados do commit `1dcb4b5`; a coluna `capital_social` fica protegida. O artigo não usa essa tabela |
| `13_versoes_anexos.py` gravava a fila na ordem de um conjunto | Mesmo conteúdo, ordem diferente a cada execução | Ordem estável |

Uma tabela mudou por dado novo, e não por defeito: `03e_rouanet_es.csv` passou a incluir 2023-2025 do SALIC, que o
relé coletou depois da última geração. Está fora do artigo.

Depois das correções:
- `checar_dados.py` 60/60;
- `auditar_captacao.py` 75/75;
- `mascarar_cpf.py --conferir` 0.

## 2. Lacunas declaradas no artigo × o que já foi extraído

| Lacuna no artigo | Onde | O que o acervo tem | Situação |
| --- | --- | --- | --- |
| Teto de 2022 indeterminado (sem ato de ampliação de R$ 10 para R$ 15 milhões) | nota da introdução | A Portaria SEFAZ nº 09-R/2022 (R$ 10 milhões) está transcrita em `notas/politica/fontes/portarias-sefaz-secult-2022.md`. Os 1.026 trechos do Diário Oficial buscados por "LICC" e pelo nome da lei não trazem ato de ampliação, mas a busca não alcançava atos que não citam a lei | **Resolvida.** A busca dirigida do relé (`consultar_dio_teto`) achou a Portaria SEFAZ nº 83-R, de 26/09/2022 (DIO-ES de 27/09/2022), que amplia o montante de 2022 em R$ 5 milhões: teto de R$ 15 milhões. A nota de rodapé, o Quadro 1 e a soma dos tetos (R$ 111 milhões, antes "no máximo") foram corrigidos; transcrição em `notas/politica/fontes/portarias-sefaz-secult-2022.md`; checagens D65, D65b, D65c e D06b |
| Projetos inscritos: não publicado | Tabela 1; §4.2 | Os extratos da CAP listam deliberados (habilitados, em diligência, inabilitados e não avaliados), mas, desde 2025, a comissão só delibera sobre parte dos projetos; o Mapa devolve `[]` para as inscrições; o Diário Oficial não traz contagem | **Mantida** |
| Público alcançado: não publicado | resumo; Tabela 1; Quadro 2; §6 | No Diário Oficial, só uma notícia com público *esperado* (2023). No Mapa, 84 eventos ligados a 24 processos, 18 com ocorrência datada | **Mantida.** O Quadro 4 passa a declarar a cobertura do Mapa como resultado de H5 (18 projetos) |
| Planilhas de custos não publicadas | Quadro 2 (H3); §4.2 | O Diário Oficial traz só a regra (IN), não as planilhas | **Mantida** |
| CNPJ do proponente para quem não captou: por LAI | §5.3; Quadro 4 | Os avisos de habilitação do Diário Oficial dão o CNPJ; com o Portal, 385 de 463 habilitados (83%) | **Reduzida** (RV4-3) |
| Data de cada repasse | Quadro 4 ("Público") | Os avisos de depósito localizam pelo menos um depósito para 267 dos 325 termos de 2022-2025 (82%; 77% do valor). Pela Portaria Conjunta 01-R/2022, arts. 5º e 6º, o aviso valida o repasse | **Confirmada**, com cobertura a declarar (SG4-3) |
| Data de protocolo dos termos: SEFAZ, por LAI | Quadro 4 | O anexo de 2025 publica a hora de recebimento dos termos validados; o Portal traz a "data do processo" de 2022-2025 (correlação de postos de 0,91 com o recebimento em 2025); as versões antigas dos anexos fotografam a fila (`13_*.csv`) | **Reduzida**: a LAI fica para os recusados e para a hora de protocolo antes de 2025 |
| Motivo da inabilitação | §4.2 (H2); §6 | Os extratos da CAP listam os inabilitados, sem motivo | **Mantida** |
| Transcrições das lives da SECULT | fora do texto | O YouTube barrou o runner ("Sign in to confirm you're not a bot"); o vídeo da 37ª reunião do Conselho é privado | **Mantida**; o artigo não cita as lives |
| LC 123/2006, art. 24 | Quadro 1; §4.2 | O relé não obteve a página do Planalto, mas o artigo foi transcrito por outra via (`notas/politica/fontes/lc-123-2006-art24.md`) | Conferido |

## 3. O que já foi extraído e o artigo não usa (e por quê)

| Fonte | Por que fica fora |
| --- | --- |
| Receita Federal dos proponentes: natureza, idade e sede (`17_*.csv`) | Já entra no Quadro 4 como fonte; os números (associação 47% do valor, RMGV 75%) caberiam na §4.2 (H4), mas não há espaço nas 15 páginas |
| Renúncia realizada pela SEFAZ (R$ 11,7 mi em 2022; R$ 15, 25 e 25 mi) | Coincide com os tetos; reforça a introdução sem mudar número |
| Pares patrocinador–proponente e concentração por CNPJ (`16_*.csv`) | Já no Quadro 2 (H1 e H4) |
| Ata do Funcultura 29/2025 (seleção por nota) | Contraste na mesma secretaria; fica para a 2ª parte |
| SALIC (Lei Rouanet) | Fora do foco (pedido do autor: só a LICC) |
