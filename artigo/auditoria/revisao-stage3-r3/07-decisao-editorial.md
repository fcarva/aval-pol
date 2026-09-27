# Decisão editorial (Stage 3, rodada 3)

- **Manuscrito:** `artigo/rascunho-artigo.md` (sha256 `efc89e2a…ddbf7`, commit `b4184cd`).
- **Proveniência:** `review_panel_provenance.json`, replay **PASS**, sha256
  `388211e739eec5b83ed77eb889bd46d095e45265c4853e4049231bd74f4466a2`.

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
| Menor | **Maior** (M1, M2) | Menor, com duas correções obrigatórias | Menor | Três MAJOR, nenhum CRITICAL |

Pela matriz sem contrato (Minor/Major/Minor/Minor), o caso é "menor ou maior, conforme os problemas". Os problemas
maiores são de **formulação e exatidão**. Nenhum exige dado novo nem refazer o método:
- corrigir duas leituras de norma;
- renomear um conceito;
- reformular uma premissa;
- especificar a população de um desenho.

Todos cabem no texto antes da entrega.

## Decisão: **REVISÃO MENOR**, com seis itens obrigatórios

**Adjudicação do advogado do diabo:** não há CRITICAL. DA1, DA2 e DA3 são **validados** e entram como obrigatórios
(RV-3, RV-2 e RV-1). DA4 e DA5 entram como RV-5 e SG-5.

**Consenso** (vários assentos no mesmo ponto):
- "A marca integra o objeto" lê a norma a favor da tese: R2 D1, DA3 e EIC E3.
- "Centralização" contradiz "delegação": R3 P1 e DA2.
- H1 precisa ligar a escolha pela marca ao que fica de fora e à entrega: R1 M2 e DA1.

**Divergência:** o R1 pede revisão maior por M1 e M2. O EIC e o R2 consideram que ambos se resolvem com redação
(população definida, faixa de poder pessimista e H1 declarada como pergunta de mecanismo ligada a H4 e H5). A decisão
segue a leitura menor, porque o R1 não aponta falha de identificação: aponta subespecificação.

## Roteiro de revisão

### Obrigatórios

| Item | Fonte | O quê | Onde |
| --- | --- | --- | --- |
| RV-1 | R2 D1, DA3, EIC E3 | Trocar "a marca integra o objeto" por redação fiel à norma: as peças de comunicação, parte do objeto, trazem a marca do patrocinador em proporção com a do Governo (IN 001/2025, arts. 55, 64 e 73) | Resumo; Quadro 1; Quadro 2 (H1); §4.2 Marketing |
| RV-2 | R3 P1, DA2 | Renomear H2 de "centralização" para "decisão concentrada" (ou definir o termo na primeira ocorrência) | §4.1; Quadro 2; §4.2; §6; Figura 1 |
| RV-3 | DA1, R1 M2 | Reformular H1: sob crédito de 100% a marca é o retorno privado por desenho; a premissa testada é que a escolha pela marca não deixa de fora bem público que a população valorizaria. Declarar o experimento como pergunta de mecanismo, ligada a H4 e H5 | §4.1; Quadro 2; Quadro 3; §5.2 (H1) |
| RV-4 | R1 M1 | População do experimento: patrocinadoras reais como população principal, contribuintes elegíveis como extensão; faixa de 30 a 60 decisores (EMD de 7,4 a 19,0 pp); viés de desejabilidade social | §5.2 (H1); §5.3; Tabela 2 |
| RV-5 | DA4, R2 D2 | "Quem se apropria" → "custo de intermediação"; "financiar" → "escolher o que financiar" (público) | §4.1; §4.2 Exclusão |
| RV-6 | R2 D2 | Conferir a LC 123/2006, art. 24 (vedação de incentivo fiscal às optantes do Simples). Se confirmada, dizer que a exclusão é estrutural e que a IN 2026 a explicitou. Se não puder ser conferida até a entrega, manter só o fato da IN 2026, sem "desde" | Quadro 1; §4.2 Exclusão |

### Sugeridos

| Item | Fonte | O quê |
| --- | --- | --- |
| SG-1 | EIC E1 | Avisar que a numeração segue a ordem de interesse, e a figura, a ordem da cadeia |
| SG-2 | EIC E2 | Uma oração ligando "dependência de poucos financiadores" (problema) a H1 e H2 |
| SG-3 | R1 M3, M6 | Erro-padrão para poucos conglomerados em H2; balanceamento condicional à posição na fila; definir AMCE e ρ como hipóteses |
| SG-4 | R1 M4, M5 | Dizer que, sem a fila da SEFAZ, H5 é verificação de robustez; nomear o estimando descritivo e causal de H3 |
| SG-5 | R2 D4, DA5 | Motivo regulatório da distribuidora como hipótese; o público financia via imposto, não escolhe |
| SG-6 | R2 D3 | Uma frase com Cornwell e Maignan (1998) e Bergstrom, Blume e Varian (1986), se couber |
| SG-7 | R3 P2, P3 | Parecerista pseudonimizado (LGPD); consentimento, sigilo e análise agregada no experimento com empresas |

### Restrição

Manter 15 páginas. As trocas de RV-1, RV-2, RV-5 e RV-6 são de redação e quase não mudam o tamanho. RV-3 e RV-4
acrescentam cerca de 4 a 6 linhas, a compensar nos sugeridos não aplicados.
