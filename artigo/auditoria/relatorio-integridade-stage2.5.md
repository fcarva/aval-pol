# Relatório de verificação de integridade acadêmica — Stage 2.5

Pipeline: ARS `academic-pipeline` v3.22.1 (imbad0202/academic-research-skills, cópia local em
`ferramentas/academic-research-skills/`, commit d8494a0), entrada no meio do pipeline (rascunho pronto →
Stage 2.5 INTEGRITY), modo pré-revisão, com a Fase E estendida a 100% das afirmações registradas.
Data: 24/09/2026.

| Item | Rodada 1 (rascunho original) | Rodada 2 (rascunho corrigido) |
| --- | --- | --- |
| Rascunho | commit f2e40ea, sha256 `97817ce68cbe…aa4ab8` | sha256 `99ea68053bbf…5a0834` |
| Registro de afirmações (claim-registry/1.0) | `r1_claim_registry.json`: 76 | `claim_registry.json`: 88 |
| Cobertura (`claim_registry_coverage.py` do ARS) | 0 candidatas fora do registro; replay PASS | 0 candidatas fora do registro; replay PASS |
| Números conferidos contra a tabela de origem | `r1_checagem_dados.csv`: 52/52 | `checagem_dados.csv`: 64/64 |
| Referências | 41 | 48 (`checagem_referencias.csv`) |
| **Veredito** | **FAIL**: 9 graves, 19 médios | **PASS WITH NOTES** (§ 7) |

Ferramentas, todas versionadas e reexecutáveis: `checar_dados.py` (acha o trecho literal de cada número no
artigo e o recalcula na tabela de origem), `checar_referencias.py` (compara cada referência com DOI aos
metadados da Crossref e do OpenAlex e cruza citação com referência), `montar_registro.py` + o script de
cobertura do ARS, o relé `buscar-fontes` (§ 9) e buscas na web para existência, contexto e originalidade.
Cada script foi testado com mutações: número, ano, volume, página, título, autor e citação alterados são
acusados.

## 1. Resumo por fase

| Fase | Escopo | Como | Rodada 1 | Rodada 2 |
| --- | --- | --- | --- | --- |
| A. Referências | 100% (48) | 25 por DOI na Crossref/OpenAlex; 23 à mão (normas no DIO, páginas oficiais, PDFs da disciplina, RePEc, resenhas indexadas); cruzamento citação ↔ referência | 1 MISMATCH | 0 MISMATCH, 0 NOT_FOUND; 1 UNVERIFIABLE_ACCESS |
| B. Contexto das citações | 31 de 32 obras citadas (97%), mais os 2 acórdãos do TCU; Throsby (1994) não conferido no texto | resumos (Crossref/OpenAlex), PDF do TD 2280, páginas do TCU e da NORUS, notas de leitura com página | 1 MAJOR_DISTORTION, 4 MINOR_DISTORTION | todas corrigidas |
| C. Dados | 100% das afirmações numéricas | 64 checagens | 3 números sem tabela | 0 |
| D. Originalidade | 11 de 34 parágrafos (32%) | busca exata de uma frase característica por parágrafo | nenhuma coincidência | — |
| E. Afirmações | 100% das registradas (88; 57 com base de alto impacto) | normas, tabelas, anexos oficiais, fontes das citações | 8 graves, 14 médias | 0 graves; 3 notas |

A cobertura semântica do registro não é detectável por máquina (`semantic_extraction_coverage:
not_machine_detectable`): o script garante só que toda frase com número ou citação caiu em alguma afirmação
registrada.

## 2. Fase A — referências

As 25 referências com DOI batem com a Crossref ou o OpenAlex em autores, título, periódico, ano, volume,
número e páginas. As demais:

| Referência | Veredito | Como foi conferida |
| --- | --- | --- |
| Barros; Lima (2017) | VERIFIED | ficha catalográfica e folha de rosto do cap. 1 no PDF da disciplina |
| Baumol; Bowen (1966) | VERIFIED | resenhas indexadas na Crossref (*Economica*, 1968; *American Literature*, 1967) |
| Belem; Donadone (2013) | VERIFIED | página do artigo na NORUS: v. 1, n. 1, 2013 |
| Brasil (2014), Ac. 1.205/2014 | VERIFIED | página do TCU: sessão 14/05/2014, relator Raimundo Carreiro |
| Brasil (2016), Ac. 191/2016 | VERIFIED | página do TCU: sessão 03/02/2016, relator Augusto Sherman |
| Espírito Santo (2021a; 2021b) | VERIFIED | textos oficiais transcritos em `notas/politica/fontes/` |
| Feld; O'Hare; Schuster (1983) | VERIFIED | resenhas de 1984 na Crossref (*Michigan Law Review*; *JPAM*) |
| Gertler *et al.* (2018) | VERIFIED | página de direitos do PDF da disciplina; o DOI impresso não resolve (Crossref e OpenAlex: 404) e fica fora |
| IBGE (2022), MUNIC 2021 | VERIFIED | API do IBGE: período 2021 publicado em 08/12/2022 |
| **IBGE (2023), SIIC 2011-2022** | **MISMATCH → corrigido** | o dado de 2024 foi publicado em 12/12/2025 (API do IBGE); referência trocada por IBGE (2025) |
| SECULT (2023; 2024a) | VERIFIED | instruções 001/2023 e 001/2024 no DIO de 1º/02 (PDF pelo relé) |
| SECULT (2024b; 2025a; 2025b; 2026a; 2026b; 2026c; [202-]) | VERIFIED | Portaria 078/2024 e IN 2025 transcritas; Portaria 062-S no DIO; páginas oficiais pelo relé |
| **SECULT (2026d), "Cultura em Dados"** | **UNVERIFIABLE_ACCESS** | página existe (URL e título em duas buscas), mas o corpo não abriu na coleta; conteúdo lido só pelo resumo do buscador; a referência leva [VERIFICAR] |
| Silva (2017), TD 2280 | VERIFIED | PDF do repositório do Ipea |
| Throsby (1994) | VERIFIED | RePEc: *JEL*, v. 32, n. 1, p. 1-29 |

Cruzamento: toda referência é citada no texto e toda citação tem referência (teste de mutação acusa
citação apagada ou com ano trocado).

## 3. Fase B — contexto das citações

| Citação | Afirmação no artigo | Veredito | Evidência |
| --- | --- | --- | --- |
| Brooks (2004) | US$ 14 de renúncia por dólar de apoio direto; públicos distintos | VERIFIED | resumo |
| Dekker; Rodrigues (2019) | benefício a projetos já bem-sucedidos; falha de mercado não clara | VERIFIED | resumo |
| Costa; Medeiros; Bucco (2017) | concentração persistente de incentivadores e proponentes | VERIFIED | resumo |
| Belem; Donadone (2013) | "mercado de patrocínios" com intermediários e marketing | VERIFIED | resumo; nota de leitura |
| Silva (2017) | SP e RJ com 65%; lógica pulverizada complementar; faltam estudos sobre acesso | VERIFIED | TD 2280, texto integral |
| Guimarães (2020) | concentração maior que a do PIB | VERIFIED | título e resumo |
| Silva (2017); Teixeira *et al.* (2024) com "maior que a do PIB" | — | MINOR_DISTORTION → corrigida | só Guimarães compara com o PIB |
| TCU, Ac. 191/2016 | "recomendou que não financiem..." | MINOR_DISTORTION → corrigida | foi determinação ao MinC |
| O'Hagan; Harvey (2000) | motivos do patrocínio | VERIFIED | nota de leitura |
| Thom (2018); Bradbury (2020); Button (2019) | efeitos pequenos na atividade, sem efeito macro | VERIFIED | resumos; nota |
| Thom; Button; Bradbury com "controle sintético" | — | MINOR_DISTORTION → corrigida | nenhum dos três usa o método |
| **Gomes; Librero-Cano (2018)** | "efeitos agregados modestos ou transitórios" | **MAJOR_DISTORTION → corrigida** | resumo: PIB per capita 4,5% maior, efeito persiste mais de 5 anos |
| Bronzini; Mocetti; Mongardini (2020) | idem | MINOR_DISTORTION → corrigida | valor adicionado só no curto prazo, mas emprego maior; evento religioso |
| Teixeira *et al.* (2021) | MG: concentração na RMBH; museu, teatro ou cinema elevam a chance de captar | VERIFIED | resumo (Crossref) |
| Smith (2007); Borgonovi; O'Hare (2004) | de leve *crowding-in* a independência | VERIFIED | resumo; nota |
| Brasil (2014); Barros; Lima (2017) | objetivos, indicadores e metas; magnitude esperada | VERIFIED | página do TCU; nota com página |
| Eldridge; Ashby; Kerry (2006) | efeito de desenho com coeficiente de variação do tamanho dos conglomerados | VERIFIED; forma algébrica exata UNVERIFIABLE_ACCESS | resumo e PLOS One 2015 (PMC4382318) confirmam a ideia; texto integral não lido |
| Feld; O'Hare; Schuster (1983); Schuster (2006); Baumol; Bowen (1966) | "mecenas apesar de si mesmos"; sistematização dos instrumentos; produtividade estagnada das artes ao vivo | VERIFIED | títulos e resenhas |
| Goodman-Bacon; Callaway; Sant'Anna; Sant'Anna; Zhao; Rambachan; Roth; Angrist *et al.*; Djimeu; Houndolo; Gelman; Carlin; McKenzie; Gertler *et al.*; White; Raitzer | usos metodológicos | VERIFIED | resumos e notas de leitura |

## 4. Fase C — dados

Rodada 1: 52/52 números batiam, mas três não tinham tabela de origem (regra 2 do `CLAUDE.md`), e as
correções geraram tabelas novas:

- coortes municipais 39/16/3/3/3 → `03_coortes_primeira_presenca_canonico.csv` (a nota citava a tabela do
  resolvedor simples, 39/15/3/4/3);
- captação por recorrência do proponente → `03_status_conversao_recorrencia_2023_2024.csv` (71% contra 57%);
- captação anual e por cota, termos indeferidos e renúncia efetiva ÷ gasto estadual em cultura →
  `analise/03f_captados_por_cota.py` → `03f_captacao_anual_secult.csv` e `03f_captados_por_cota.csv`, lidos dos
  anexos oficiais com URL e sha256. O total indeferido de 2024 não vem impresso: é soma da coluna do termo,
  método que reproduz ao centavo o total impresso de 2023.

Rodada 2: 64/64.

## 5. Fase E — afirmações

Graves (bloqueavam), todas corrigidas no rascunho:

| ID | Afirmação original | Veredito | Correção |
| --- | --- | --- | --- |
| I-01 | C29: grandes eventos com efeitos "modestos ou transitórios" | MAJOR_DISTORTION | achados de cada estudo |
| I-02 | C14: a LICC "nunca foi avaliada: não localizamos nenhum estudo sobre ela" | contradita | IJSN, SECULT e FAPES apresentaram resultados preliminares de avaliação em julho de 2026 |
| I-03 | C27: "nem avaliação acadêmica de leis estaduais de incentivo via ICMS" | contradita | Teixeira *et al.* (2021) sobre a lei de MG, que entra na revisão |
| I-04 | C18, C48, C62: em 2022-2024 "a habilitação precedia a busca por patrocinador" | UNVERIFIABLE na rodada 1 | **confirmada** pelas instruções de 2023 e 2024 (arts. 32-36): habilitação publicada no DIO, prazo de captação de um ano, termo firmado com projeto já habilitado, arquivamento sem 50% de compromissos. A inversão (compromisso antes da comissão) é de 2025. A instrução de 2022 não foi lida e isso está dito |
| I-05 | C03, C60: "a captação favorece ... a RMGV, onde fica 67%" | MAJOR_DISTORTION | 67% é do valor habilitado; execução quase igual (68% e 63%); captado de 2025: 61% na RMGV |
| I-06 | C10: SIIC como IBGE (2023) | MISMATCH | IBGE (2025) |
| I-22 | C46, C61: cumprimento das cotas "não é apurável com o que se publica" | contradita | o anexo de captação publica total por cota desde 2025 (I e IV 100%, II 93%, III 107%); o texto diz que isso descreve a execução das reservas, não o cumprimento, por causa dos §§ 1º e 2º do art. 18 |
| I-25 | C08, Quadro 1, Tabela 1: teto de 2022 = R$ 10 mi | conflito entre fontes oficiais | a Portaria 09-R fixou R$ 10 mi; o anexo de captação de 2022 declara R$ 15 mi disponíveis e R$ 11,5 mi validados; ampliação não localizada. O texto passa a medir o crescimento de 2023 a 2026 e declara o conflito em nota |

Médias, todas corrigidas:

| ID | Correção |
| --- | --- |
| I-07, I-08 | tabelas de origem novas (§ 4) |
| I-09 a I-12 | contexto das citações (§ 3) |
| I-13 | "o teto de renúncia equivale a 14%-21%" → "a renúncia efetiva", agora medida pelos anexos de 2022-2025 (mesma faixa) |
| I-14 | "iniciativa inédita" sem citação → página "Sobre a LICC" |
| I-15 | "as regras mudaram três vezes em quatro anos" → mudanças no meio do exercício em 2024 e 2025 |
| I-16 | fechamento das inscrições de 2024 sem fonte → Portaria 078/2024 |
| I-17 | limiar de 35% sem escopo → 50% em 2023-2024 e 35% no início de 2025 |
| I-18 | objetivo do decreto está na ementa, não no art. 3º |
| I-19 | cobertura não declarada (regra 1): 459/463 com valor; 69/71 municípios |
| I-20 | "que a literatura trata como moderados" sem fonte → retirado |
| I-21 | fórmula do EMD sem o ajuste por cv usado na Tabela 2 → fórmula e citação de Eldridge *et al.* (2006) |
| I-23 | lista de habilitados com "acesso em 23 set." → transcrição de 3 set.; a versão de 10/09 mantém as quantidades de 2022-2025 e os 98 expirados, e as diferenças ficam no ciclo 2026 (≈ 7 processos e poucos status) |
| I-24 | "26 patrocinadores" sem definição → 26 empresas (raiz do CNPJ), 46 estabelecimentos |
| I-26 | "O excesso de demanda é racionado pelas empresas, não pela SECULT" → pela escolha das empresas e pela ordem de validação dos termos, já que a SECULT indeferiu termos que excediam o montante |

Achado que reforça o artigo: de 2023 a 2025 a captação esgotou o montante de cada ano ao centavo, e em 2023
e 2024 a SECULT indeferiu termos de patrocínio equivalentes a 28% e 35% do montante — evidência direta do
racionamento pelo teto.

Advertências da Fase E5 (afirmações de ausência, não bloqueiam): "Não localizamos avaliação causal de
incentivo cultural no Brasil" (C27) segue limitada às buscas feitas.

## 6. Checklist de 7 modos de falha de pesquisa com IA

| Modo | Rodada 1 | Rodada 2 | Evidência |
| --- | --- | --- | --- |
| 1. Erro de implementação aceito | CLEAR | CLEAR | todo número sai de script versionado; 64 checagens reproduzem; os erros de tolerância do `np.isclose` e do teto de 2026 foram achados e corrigidos antes desta auditoria |
| 2. Citação alucinada ou mal atribuída | **SUSPECTED** | CLEAR | nenhuma referência inexistente; achados mal atribuídos (I-01, I-06, I-09 a I-12) corrigidos |
| 3. Resultado inventado | CLEAR | CLEAR | 100% dos números com tabela de origem |
| 4. Atalho | CLEAR com nota | CLEAR com nota | as associações da seção 4.2 são descritivas; o texto diz "Isso não mede impacto" |
| 5. Erro lido como achado | CLEAR | CLEAR | nenhum achado "surpreendente"; território conferido com dois resolvedores |
| 6. Método descrito ≠ método rodado | **SUSPECTED** | CLEAR | a fórmula exibida não tinha o ajuste por cv (I-21) |
| 7. Enquadramento travado cedo | **INSUFFICIENT EVIDENCE** | CLEAR com nota | a premissa do desenho D1 foi conferida nas instruções de 2023 e 2024; falta a de 2022 (primeiro ciclo) |

## 7. Veredito da rodada 2: PASS WITH NOTES

Zero problema grave ou médio aberto, zero MAJOR_DISTORTION, zero UNVERIFIABLE. Notas que acompanham o artigo
para a revisão (Stage 3):

1. **SECULT (2026d)** — avaliação preliminar do IJSN: página lida só pelo resumo do buscador
   (UNVERIFIABLE_ACCESS; a referência leva [VERIFICAR]). Convém abrir a página no navegador ou pedir o material
   ao IJSN.
2. **Montante de 2022** — R$ 10 mi (Portaria SEFAZ 09-R) contra R$ 15 mi (anexo da SECULT). Ato de ampliação não
   localizado; declarado no texto como indeterminado.
3. **Instrução de 2022** não lida (primeiro ciclo do desenho D1); declarado no texto.
4. **Eldridge *et al.* (2006)** — forma algébrica exata não conferida no texto integral.
5. **Página-limite** — o PDF gerado tem 15 páginas, o máximo permitido.
6. **Oportunidade de desenho (para o Stage 3, não é correção de integridade)** — os anexos de 2023 e 2024 listam
   os termos indeferidos por excesso do montante, projeto a projeto. Projetos com termos aceitos e indeferidos
   pela ordem de validação formam uma comparação ainda mais próxima do que a do desenho D1 (mesmo patrocinador
   disposto, corte pelo esgotamento do teto). E os anexos de 2022-2024 dão a captação de cada projeto, o que
   permite medir o tratamento diretamente em vez de pela situação publicada.

## 8. O que o repositório licc.gov acrescentou

Clonado em 24/09/2026 (`fcarva/licc.gov`, 15 commits, último 78163a4). A documentação já estava copiada em
`licc-gov/` e sintetizada em `notas/politica/02-licc-gov-sintese.md`; o que era novo está no histórico do git
e no código das ferramentas:

- **Data da transcrição**: a lista de habilitados entrou no licc.gov em 03/09/2026 (commit 78163a4) e o anexo de
  captados em 02/09/2026 (acb3530), antes da atualização da SECULT de 10/09 (I-23).
- **Lotes**: ao menos seis listas "ANO 2025" (28 a 74 projetos), porque a comissão é permanente (commit
  4d4d664; `docs/pipeline.md`).
- **Empresas**: licc.gov conta 28 "empresas"; esta análise, 26 por raiz de CNPJ (I-24).
- **Cotas no anexo de captados**: o leitor de captados (`tools/anexos-secult/extrair-captados.mjs`, l. 147-170
  e 408-434) registra que o anexo é seccionado por cota e imprime "Total Captado" por cota — a pista que levou a
  I-22 e, pela página "Recursos Financeiros Captados", aos anexos de 2022 a 2026.

## 9. Rede: como as fontes foram recuperadas

A sessão em nuvem só alcança o GitHub e os registros de pacotes, e o Firecrawl ficou sem créditos. O relé
`.github/workflows/buscar-fontes.yml` roda `analise/rede/buscar_fontes.py` num runner do GitHub Actions (rede
aberta) quando a lista de pedidos muda e devolve o resultado por commit, em três etapas com commit próprio
(DOIs e buscas bibliográficas; páginas e PDFs, com a lista de links de cada página; API do SALIC com cache
versionado), com manifesto (status HTTP, sha256, data UTC). Um push novo cancela o run anterior, e o que já
foi coletado fica salvo. Nenhum e-mail ou dado pessoal vai nas requisições. Seis rodadas nesta auditoria
trouxeram 109 DOIs, 12 buscas bibliográficas e 50 páginas e PDFs pedidos (40 com sucesso). Bloqueios: páginas do IBGE, SciELO,
FJP e editoras (Elsevier, SAGE) respondem 403 ao runner; notícias recentes da SECULT voltam sem corpo. A API de
dados do IBGE e as páginas da SECULT, do TCU, do Ipea e da NORUS respondem.
