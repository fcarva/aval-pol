# Decisão editorial (Stage 3, rodada 4)

- **Manuscrito:** `artigo/rascunho-artigo.md` (sha256 `15d70ff9…fcd64a`, commit `898ac9c`).
- **Proveniência:** `review_panel_provenance.json`, replay **PASS**, sha256
  `b61b2235fdb0f9896337840a22c931559a8e4413b130cd0a48fa4e14c6c65490`.

| Eixo | Status |
| --- | --- |
| Papéis separados | sim |
| Contextos separados | não |
| Cegueira às saídas dos pares | não |
| Família de modelo única | claude |
| Provedor único | anthropic |
| Revisores humanos | nenhum |

Divulgação de erro correlacionado: "All model-executed review seats used one model family; role separation does not
remove correlated-error risk." Estado: `NOT_CALIBRATED`.

## Recomendações dos assentos

| EIC | R1 | R2 | R3 | DA |
| --- | --- | --- | --- | --- |
| Menor | Menor (M1, M2 e M5 obrigatórios) | Menor (D1 obrigatório) | Menor | Dois MAJOR, três MINOR, nenhum CRITICAL |

## Decisão: **REVISÃO MENOR**, com quatro itens obrigatórios

**Adjudicação do advogado do diabo:** não há CRITICAL.
- DA1 e DA2 (MAJOR) são **validados**: o poder de H5 está subdeclarado e o desenho de H4 não atende à regra de
  conglomerados. Entram como RV4-1 e RV4-2.
- DA3 e DA4 são validados e entram como RV4-3 e RV4-4.
- DA5 é parcialmente validado e entra como sugestão (SG4-2).

**Consenso:**
- A §5.3 trata como LAI um dado que o Diário Oficial publica: R1 M5, R3 P1 e DA3.
- Os passos 3 e 5 do J-PAL não aparecem com esse nome: EIC E1 e E2, R2 D1 e D2, e DA4.
- A Tabela 2 confere; o problema é o que ela não mostra: R1 M1 e M2, DA1 e DA2.

**Divergência:** nenhuma quanto à decisão. Todos os itens são de redação, com números já calculados e rastreáveis.

## Roteiro de revisão

### Obrigatórios

| Item | Fonte | O quê | Onde | Linhas |
| --- | --- | --- | --- | --- |
| RV4-1 | R1 M2, DA1 | Declarar o EMD do efeito local de H5 (de 69 a 85 pontos, primeiro estágio de 0,41) e o cenário com os recusados de 2025-2026 por LAI (de 20 a 24 pontos). Declarar que o efeito local de H4 tem o EMD da Tabela 2 dividido pela adesão | §5.4, depois de "serve como verificação de robustez" | +3 |
| RV4-2 | R1 M1, DA2 | H4 com todos os 71 municípios do interior (35 ou 36 por grupo, regra de 30 a 50 de Gertler *et al.*, 2018, p. 314); braços e intensidade sorteados entre agentes dos municípios tratados; diferença entre braços com EMD de 2,3 a 4,9 pontos; só com coletivos, 26 por grupo, abaixo da regra | §5.2 (H4); §5.4 | +2 |
| RV4-3 | R1 M5, R3 P1, DA3 | Chave de ligação: o Portal (quem captou) e os avisos de habilitação no Diário Oficial cobrem 385 dos 463 habilitados (83%); a LAI fica para o restante e para os inabilitados. Referência nova: DIO-ES (2026), busca no Diário Oficial | §5.3; Quadro 4 (linha dos extratos: "CNPJ na habilitação"); Referências | +1 |
| RV4-4 | EIC E1, R2 D1, DA4 | Uma oração: os indicadores da cadeia (passo 5) são as etapas do funil da Tabela 1, e os de resultado, os *Y* do Quadro 3; os que faltam (inscritos, público) coincidem com os elos tracejados da Figura 1 | §4.2, Funil de atrito | +1 |

### Sugeridos

| Item | Fonte | O quê |
| --- | --- | --- |
| SG4-1 | EIC E2, R2 D2 | Nomear dois riscos do passo 3: o deslocamento de outros projetos pelo teto e a substituição do patrocínio próprio da empresa pelo crédito integral |
| SG4-2 | R1 M3, DA5 | O teste da ordem da fila começa com dado público: a "data do processo" do Portal tem correlação de postos de 0,91 com o recebimento em 2025 |
| SG4-3 | R1 M4 | Datar o tratamento pelo aviso de depósito (386 depósitos; de 20 dos 48 termos em 2022 a 78 dos 96 em 2025); os 69 depósitos de 2026 antecipam o ano que o Portal não lista |
| SG4-4 | R3 P2 | Conclusão: "publicar **em formato aberto**" |
| SG4-5 | R2 D4 | Renomear a coluna "montante" de `09_racionamento_por_ano.csv` para "montante declarado no anexo" (fora do texto) |

### Restrição de páginas

O artigo tem 15 páginas, e os obrigatórios somam cerca de 7 linhas. A compensação sugerida:
- a última oração da conclusão (limitações) encurta, porque RV4-3 tira dela a "estreia medida por nome" na maior
  parte dos casos;
- a oração de Gelman e Carlin (2014) na §5.4 funde-se com RV4-1;
- SG4-1 e SG4-2 só entram se sobrar espaço.

### Proveniência dos números novos

| Número | Arquivo | Script |
| --- | --- | --- |
| 69 a 85; 20 a 24; 2,3 a 4,9; 26 e 35,5 por grupo; adesão | `analise/tabelas/19_poder_revisao.csv` | `analise/19_poder_revisao.py` |
| 385 de 463 (83%); 79 de 81 | `analise/tabelas/18_cobertura_cnpj.csv` | `analise/18_dio_avisos_habilitacao.py` |
| 386 depósitos; 20/48 a 78/96 | `analise/tabelas/18_deposito_x_portal.csv` | idem |
| 0,91; 19 dias | `analise/tabelas/16_data_processo_x_recebimento_2025.csv` | `analise/16_transparencia_licc.py` |

Cada número que entrar no texto ganha uma checagem em `artigo/auditoria/checar_dados.py`.

## Checkpoint obrigatório

Os revisores não alteram o manuscrito. A aplicação dos itens RV4-1 a RV4-4, e dos sugeridos que o autor escolher,
depende da decisão do autor.
