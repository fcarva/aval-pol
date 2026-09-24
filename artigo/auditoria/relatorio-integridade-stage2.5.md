# Relatório de verificação de integridade acadêmica — Stage 2.5

Pipeline: ARS `academic-pipeline` v3.22.1 (imbad0202/academic-research-skills, cópia local em
`ferramentas/academic-research-skills/`, commit d8494a0), entrada no meio do pipeline (rascunho pronto →
Stage 2.5 INTEGRITY). Modo: pré-revisão (Mode 1), com a Fase E ampliada a 100% das afirmações registradas.

| Item | Rodada 1 | Rodada 2 |
| --- | --- | --- |
| Rascunho | `artigo/rascunho-artigo.md` do commit f2e40ea, sha256 `97817ce6…4aa4ab8` | versão corrigida neste ramo (sha256 no fim do relatório) |
| Registro de afirmações | `r1_claim_registry.json` (76 afirmações) | `claim_registry.json` |
| Cobertura (script do ARS) | `r1_claim_registry_coverage.json`: 0 candidatas fora do registro; replay PASS | `claim_registry_coverage.json` |
| Números | `r1_checagem_dados.csv` (52/52) | `checagem_dados.csv` |
| Referências | — | `checagem_referencias.csv` |
| **Veredito** | **FAIL** (6 problemas graves, 15 médios) | ver § 7 |

Ferramentas: `checar_dados.py` (recalcula cada número a partir de `analise/tabelas/` e `dados/externos/`),
`checar_referencias.py` (compara cada referência com DOI aos metadados da Crossref e do OpenAlex),
`montar_registro.py` + `claim_registry_coverage.py` do ARS (registro e cobertura das afirmações), o relé
`buscar-fontes` (GitHub Actions; ver § 8) e buscas na web para existência, contexto e originalidade.

## 1. Resumo por fase

| Fase | Escopo | Verificado | Problemas na rodada 1 |
| --- | --- | --- | --- |
| A. Referências | 41 de 41 (100%) | 22 por DOI na Crossref/OpenAlex (script); 19 sem DOI à mão (normas transcritas, páginas oficiais, PDFs da disciplina, RePEc, buscas bibliográficas) | 1 MISMATCH (IBGE, 2023) |
| B. Contexto das citações | 30 de 37 citações a obras (81%) | resumos da Crossref/OpenAlex, páginas do TCU e da NORUS, notas de leitura com página | 1 distorção grave (Gomes; Librero-Cano, 2018) e 4 leves |
| C. Dados | 100% das afirmações numéricas registradas | 52 checagens na rodada 1, 59 na rodada 2 | 2 números sem tabela de origem |
| D. Originalidade | 11 de 34 parágrafos de texto corrido (32%) | busca exata de uma frase característica por parágrafo | nenhuma coincidência |
| E. Afirmações | 76 registradas (100% verificadas; 48 com base de alto impacto) | normas transcritas, tabelas, fontes das citações | 4 graves (2 ausências contraditas, 1 premissa não apurada, 1 conflação), 9 médias |

A cobertura semântica do registro não é detectável por máquina (`semantic_extraction_coverage:
not_machine_detectable`): o script garante só que toda frase com número ou citação caiu em alguma afirmação
registrada.

## 2. Fase A — referências

Todas as 41 referências existem. Detalhe em `checagem_referencias.csv` e na tabela abaixo para as que não
têm DOI.

| Referência | Veredito | Como foi conferida |
| --- | --- | --- |
| 22 referências com DOI | VERIFIED | Crossref (21) ou OpenAlex; autores, título, periódico, ano, volume, número e páginas batem (`checar_referencias.py`; teste de mutação acusa ano, volume, páginas, título e autor alterados) |
| Barros; Lima (2017) | VERIFIED | ficha catalográfica e folha de rosto do cap. 1 no PDF da disciplina (`notas/disciplina/04-itau-magenta-adb.md`, § 0.1) |
| Baumol; Bowen (1966) | VERIFIED | resenhas indexadas na Crossref (*Economica*, 1968; *American Literature*, 1967) |
| Belem; Donadone (2013) | VERIFIED | página do artigo na NORUS (`dados/fontes_web/paginas/norus_belem_donadone.txt`): v. 1, n. 1, 2013 |
| Brasil (2014), Ac. 1.205/2014 | VERIFIED | página do TCU: sessão 14/05/2014, relator Raimundo Carreiro |
| Brasil (2016), Ac. 191/2016 | VERIFIED | página do TCU: sessão 03/02/2016, relator Augusto Sherman |
| Espírito Santo (2021a; 2021b) | VERIFIED | textos oficiais transcritos em `notas/politica/fontes/` |
| Feld; O'Hare; Schuster (1983) | VERIFIED | resenhas de 1984 indexadas na Crossref (*Michigan Law Review*; *JPAM*) |
| Gertler *et al.* (2018) | VERIFIED | página de direitos do PDF da disciplina; o DOI impresso não resolve (Crossref e OpenAlex: 404) e fica fora |
| IBGE (2022), MUNIC 2021 | VERIFIED | API do IBGE: período 2021 publicado em 08/12/2022 |
| **IBGE (2023), SIIC 2011-2022** | **MISMATCH** | o dado citado é de 2024, publicado em 12/12/2025 (API do IBGE, `ibge_siic_periodos.txt`); a edição de 2023 não o contém → corrigido para IBGE (2025) |
| Schuster (2006) | VERIFIED | Crossref: cap. 36 do *Handbook*, p. 1253-1298; DOI acrescentado |
| SECULT (2024; 2025a; 2025b; 2026a; 2026b) | VERIFIED | textos oficiais transcritos e PDF do DIO-ES (Portaria 062-S: `secult_portaria_062s_2025.txt`) |
| Silva (2017), TD 2280 | VERIFIED | repositório do Ipea (título, autor, mar. 2017) |
| Throsby (1994) | VERIFIED | RePEc: *JEL*, v. 32, n. 1, p. 1-29 |

## 3. Fase B — contexto das citações

| Citação | Afirmação | Veredito | Evidência |
| --- | --- | --- | --- |
| Brooks (2004) | US$ 14 de renúncia por dólar de apoio direto; públicos diferentes | VERIFIED | resumo |
| Dekker; Rodrigues (2019) | benefício a projetos já bem-sucedidos; falha de mercado não clara | VERIFIED | resumo |
| Costa; Medeiros; Bucco (2017) | concentração persistente de incentivadores e proponentes | VERIFIED | resumo |
| Belem; Donadone (2013) | "mercado de patrocínios" com intermediários e marketing | VERIFIED | resumo na página da revista; nota de leitura |
| Silva (2017) | concentração em SP e RJ; lógica pulverizada coexistente; falta de estudos sobre acesso | VERIFIED | nota de leitura com páginas (p. 22-23, 28, 29) |
| Guimarães (2020) | concentração maior que a do PIB | VERIFIED | título e resumo |
| **Silva (2017); Teixeira *et al.* (2024)** | "concentração ... maior que a do PIB" | **MINOR_DISTORTION** | só Guimarães compara com o PIB → citações separadas |
| **TCU, Ac. 191/2016** | "recomendou que não financiem..." | **MINOR_DISTORTION** | foi determinação ao MinC → corrigido |
| O'Hagan; Harvey (2000) | motivos: imagem, cadeia de fornecedores, *rent-seeking*, gestores | VERIFIED | nota de leitura |
| Thom (2018); Bradbury (2020) | efeitos pequenos na atividade, nenhum efeito macro | VERIFIED | resumos |
| Button (2019) | mais filmagens de séries, sem efeito no emprego | VERIFIED | nota de leitura (resumo) |
| **Thom; Button; Bradbury** | "adoção escalonada, variáveis instrumentais e controle sintético" | **MINOR_DISTORTION** | nenhum dos três usa controle sintético → termo retirado |
| **Gomes; Librero-Cano (2018)** | "efeitos agregados modestos ou transitórios" | **MAJOR_DISTORTION** | o resumo diz PIB per capita 4,5% maior, com efeito que persiste por mais de 5 anos → reescrito |
| **Bronzini; Mocetti; Mongardini (2020)** | "efeitos modestos ou transitórios" de evento "cultural" | **MINOR_DISTORTION** | valor adicionado sobe só no curto prazo, mas a taxa de emprego sobe; o Jubileu é evento religioso → reescrito |
| Smith (2007); Borgonovi; O'Hare (2004) | de leve *crowding-in* a independência | VERIFIED | resumo; nota de leitura |
| Gomes; Librero-Cano (2018) | comparação com cidades candidatas | VERIFIED | resumo |
| Brasil (2014) | objetivos, indicadores e metas para renúncias | VERIFIED | página do TCU |
| Barros; Lima (2017) | resultados e magnitude esperados | VERIFIED | nota com página (p. 15) |
| Goodman-Bacon (2021); Callaway; Sant'Anna (2021); Sant'Anna; Zhao (2020); Rambachan; Roth (2023); Angrist; Imbens; Rubin (1996); Djimeu; Houndolo (2016); Gelman; Carlin (2014); McKenzie (2012); Gertler *et al.* (2018); White; Raitzer (2017) | usos metodológicos | VERIFIED | resumos e notas de leitura; o erro tipo M (2,5 vezes com poder de 17%) é recalculado por `05_poder_mde.py` |

## 4. Fase C — dados

`checar_dados.py` localiza o trecho literal de cada número no artigo e recalcula o valor na tabela de
origem, com arredondamento meio-para-cima e vírgula decimal. Rodada 1: 52/52 conferem. A checagem revelou dois
números sem tabela, violando a regra 2 do `CLAUDE.md`:

- **Coortes municipais 39/16/3/3/3** (seção 5.2): vinham do resolvedor canônico, mas nenhum script gravava a
  tabela; a nota citava a do resolvedor simples (39/15/3/4/3). `03_descritivas.py` passa a gravar
  `03_coortes_primeira_presenca_canonico.csv`.
- **"A captação favorece proponentes recorrentes"** (resumo e conclusão): sem número de conversão no texto nem
  tabela. `03_descritivas.py` passa a gravar `03_status_conversao_recorrencia_2023_2024.csv` (71% contra 57%),
  e o número entra no texto.

Rodada 2: 59/59, incluindo os números novos (71%/57%, 68%/63%, 61% do captado, 69/71 municípios, 3/56
expirados, cv = 0,73, cobertura 459/463).

## 5. Fase E — afirmações (problemas e correções)

Graves (bloqueiam):

| ID | Afirmação | Veredito | Correção |
| --- | --- | --- | --- |
| I-01 | C29: grandes eventos com efeitos "modestos ou transitórios" | MAJOR_DISTORTION | reescrita com os achados de cada estudo |
| I-02 | C14: a LICC "nunca foi avaliada: não localizamos nenhum estudo sobre ela" | contradita | o IJSN, com a SECULT e a FAPES, apresentou em julho de 2026 resultados preliminares de uma avaliação da LICC (evento "Cultura em Dados"); ver § 7 |
| I-03 | C27: "nem avaliação acadêmica de leis estaduais de incentivo via ICMS" | contradita | há estudo quantitativo da lei estadual de Minas Gerais (*Interações*, v. 22, n. 2, 2021, DOI 10.20435/inter.v22i2.2965) e monografia da FJP (2015); ver § 7 |
| I-04 | C18, C48, C62: em 2022-2024 "a habilitação precedia a busca por patrocinador" | UNVERIFIABLE | as instruções de 2022 a 2024 não foram lidas; na de 2025, a comissão só habilitava com termos de compromisso de ≥ 35% do valor (arts. 41-45). Reescrito como premissa explícita, com as duas leituras possíveis da lista e o que muda no grupo de comparação |
| I-05 | C03, C60: "a captação favorece ... a RMGV, onde fica 67%" | MAJOR_DISTORTION | 67% é do valor **habilitado**; a taxa de execução quase não difere (68% RMGV, 63% interior). Texto separa as medidas e acrescenta o captado de 2025 (61% na RMGV, 42 de 63 projetos) |
| I-06 | C10: SIIC citado como IBGE (2023) | MISMATCH | IBGE (2025) |

Médios:

| ID | Afirmação | Correção |
| --- | --- | --- |
| I-07 | coortes municipais sem tabela | tabela nova (§ 4) |
| I-08 | captação × recorrência sem número | tabela e número novos (§ 4) |
| I-09 | TCU 191/2016 como recomendação | "determinou" |
| I-10 | Bronzini *et al.* (2020) | efeito no emprego e evento não cultural |
| I-11 | "maior que a do PIB" em três fontes | citações separadas |
| I-12 | "controle sintético" | retirado |
| I-13 | C12: "a renúncia equivale a 14% a 21%" | "o teto de renúncia", 2022-2025 (a renúncia efetiva só é conhecida em 2025) |
| I-14 | C06: "descrito pela própria SECULT como iniciativa inédita" sem citação | página "Sobre a LICC" confere o texto; citação acrescentada |
| I-15 | C46: "as regras mudaram três vezes em quatro anos" | as notas documentam duas mudanças no meio do exercício (2024 e 2025) → texto específico |
| I-16 | C17: fechamento das inscrições em 2024 sem fonte | Portaria SECULT 078/2024 citada e referenciada |
| I-17 | C47: limiar de 35% sem escopo | "da instrução de 2025" (revogado pela 062-S) |
| I-18 | C32: objetivo do decreto atribuído ao art. 3º | está na ementa |
| I-19 | cobertura não declarada (regra 1) | 459 de 463 com valor; 69 de 71 municípios do interior com dado |
| I-20 | "que a literatura trata como moderados" sem fonte | retirado |
| I-21 | fórmula do EMD com efeito de desenho diferente do usado na Tabela 2 | fórmula com o ajuste pelo coeficiente de variação do tamanho das carteiras e citação de Eldridge, Ashby e Kerry (2006); ver § 7 |

Advertências da Fase E5 (afirmações de ausência, não bloqueiam): C14 e C27 continuam limitadas pela busca
feita. A redação corrigida diz o que foi localizado.

## 6. Checklist de 7 modos de falha de pesquisa com IA

| Modo | Rodada 1 | Evidência | Rodada 2 |
| --- | --- | --- | --- |
| 1. Erro de implementação aceito | CLEAR | cada número sai de script versionado; 59 checagens reproduzem; o erro de tolerância do `np.isclose` (contagem de "exatamente R$ 500 mil") e o teto de 2026 foram achados e corrigidos antes desta auditoria | CLEAR |
| 2. Citação alucinada ou mal atribuída | **SUSPECTED** | nenhuma referência inexistente, mas achados mal atribuídos (I-01, I-06, I-09 a I-12) | CLEAR após as correções |
| 3. Resultado inventado | CLEAR | 100% dos números com tabela de origem após I-07 e I-08 | CLEAR |
| 4. Atalho | CLEAR, com nota | as associações da seção 4.2 são descritivas (qualidade e capacidade do proponente não controladas); o texto diz "Isso não mede impacto" | CLEAR, com nota |
| 5. Erro lido como achado | CLEAR | nenhum achado "surpreendente"; a concentração territorial foi refeita com dois resolvedores | CLEAR |
| 6. Método descrito ≠ método rodado | **SUSPECTED** | a fórmula exibida não tinha o ajuste por cv usado na Tabela 2 (I-21) | CLEAR após a correção, pendente a conferência da fonte de Eldridge *et al.* (§ 7) |
| 7. Enquadramento travado cedo | **INSUFFICIENT EVIDENCE** | o desenho D1 depende de como a SECULT define "habilitado" em 2022-2024 (I-04) | INSUFFICIENT EVIDENCE: segue com aviso; depende de ler as instruções de 2022-2024 ou de confirmar com a SECULT |

## 7. Pendências da rodada 2

Preenchido na conclusão da rodada 2.

## 8. O que o repositório licc.gov acrescentou

Clonado em 24/09/2026 (`fcarva/licc.gov`, ramo `claude/licc-cultura-dashboard-hfgv61`, 15 commits, último
78163a4). A documentação já estava copiada em `licc-gov/` e sintetizada em
`notas/politica/02-licc-gov-sintese.md`; o que era novo está no histórico do git e no código das ferramentas:

- **Data da transcrição.** A lista de habilitados entrou no licc.gov em 03/09/2026 (commit 78163a4) e o anexo
  de captados em 02/09/2026 (acb3530). A página da SECULT informa atualização da lista em 10/09/2026. A
  referência do artigo dizia "Acesso em: 23 set. 2026" → corrigida para 3 set. 2026, com nota de que os
  status podem ter mudado na versão de 10/09 (I-23).
- **Lotes.** A SECULT publicou ao menos seis listas "ANO 2025" (28, 33, 35, 37, 41 e 74 projetos), porque a
  comissão é permanente e habilita ao longo do ano (commit 4d4d664; `docs/pipeline.md`). Isso reforça que
  "habilitado", na lista, é decisão da comissão — o que, pela instrução de 2025, ocorria depois de reunir
  termos de compromisso de patrocínio; a página da instrução de 2024 também traz o modelo "Anexo VIII –
  Termo de Compromisso de Patrocínio" (`dados/fontes_web/paginas/secult_in_2024.txt`). É evidência a favor da
  segunda leitura de I-04 (grupo de comparação com patrocínio parcial), não prova.
- **Empresas.** O licc.gov conta 28 "empresas"; esta análise conta 26 por raiz de CNPJ (46 estabelecimentos).
  O artigo passa a declarar a definição (I-24).
- **Cotas na captação (I-22, grave).** O leitor de captados do licc.gov (`tools/anexos-secult/extrair-captados.mjs`,
  l. 147-170 e 408-434), aferido no próprio documento, registra que o anexo "RECURSO FINANCEIRO CAPTADO 2025" é
  seccionado por cota (ex.: "IV - 50% serão destinados aos demais projetos. Valor: R$ 12.500.000,00") e imprime
  um "Total Captado" por cota e um geral. Logo, em 2025 a captação por cota **é publicada**, e o artigo dizia
  que o cumprimento das cotas "não é apurável com o que se publica" (C46, C61). Os §§ 1º e 2º do art. 18
  (migração para a cota IV e remanejamento a critério da SECULT) impedem afirmar descumprimento, mas não
  impedem medir quanto cada reserva captou.

## 9. Rede: como as fontes foram recuperadas

A sessão em nuvem só alcança o GitHub e os registros de pacotes; o Firecrawl ficou sem créditos. O relé
`.github/workflows/buscar-fontes.yml` roda `analise/rede/buscar_fontes.py` num runner do GitHub Actions
(rede aberta) quando a lista de pedidos muda e devolve o resultado por commit, com manifesto (status HTTP,
sha256, data UTC): metadados e resumos da Crossref e do OpenAlex para 108 DOIs, buscas bibliográficas para
referências sem DOI, texto de páginas e PDFs oficiais (com a lista de links da página) e a API do SALIC.
Nenhum e-mail ou dado pessoal vai nas requisições. Bloqueios observados: páginas do IBGE e de editoras
(Elsevier, SAGE) respondem 403 ao runner; a API de dados do IBGE e as páginas da SECULT, do TCU, do Ipea e da
NORUS respondem.
