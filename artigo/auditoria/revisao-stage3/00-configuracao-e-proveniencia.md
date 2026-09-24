# Stage 3 — Configuração do painel e proveniência

Manuscrito: `artigo/rascunho-artigo.md`, sha256 `99ea68053bbfdb9443286dbe3099c0fbd13fb6a80787d2fb337257c1085a0834`
(versão aprovada com notas no Stage 2.5). Modo: `full`. Data: 24/09/2026. Rodada 1.

## Phase 0 — Análise de campo

| Item | Leitura |
| --- | --- |
| Disciplina principal | Avaliação de políticas públicas (economia aplicada) |
| Disciplinas secundárias | Economia do setor público (gasto tributário); economia da cultura; métodos quase-experimentais |
| Paradigma | Quantitativo-descritivo (avaliação de desenho com dados administrativos) + proposta metodológica (sem estimação) |
| Tipo de texto | Mini artigo de disciplina de pós-graduação (PECO 5046-6046, PPGEco/UFES), 10-15 páginas, com seções obrigatórias definidas pela disciplina |
| Referência de periódico | Revistas aplicadas brasileiras de políticas públicas (ex.: *Planejamento e Políticas Públicas*, Ipea; *Revista de Administração Pública*) |
| Maturidade | Rascunho avançado, auditado (Stage 2.5 PASS WITH NOTES) |

## Cartões de configuração

| Assento | Identidade configurada | Foco |
| --- | --- | --- |
| EIC — Journal-Fit Reviewer | Editor de revista aplicada de políticas públicas que também confere a aderência ao enunciado da disciplina | Adequação ao gênero e às exigências da disciplina, originalidade, prontidão para entrega |
| R1 — Metodologia | Econometrista de avaliação de impacto (diferenças em diferenças com adoção escalonada, cálculo de poder com dados administrativos) | Identificação, unidade de análise, definição do tratamento, poder, viabilidade de dados |
| R2 — Domínio | Pesquisador de economia da cultura e política cultural brasileira (Lei Rouanet, leis estaduais de incentivo) | Revisão da literatura, políticas similares, enquadramento teórico |
| R3 — Perspectiva | Especialista em governança de gastos tributários e controle externo (orçamento, transparência, LRF) | Enquadramento fiscal, recomendações, ética e conformidade |
| DA — Advogado do diabo (assento fixo) | — | Argumento contrário mais forte, explicações alternativas, generalizações |

Checkpoint da Phase 0: o usuário pediu para "continuar avançando"; os cartões ficam registrados aqui e podem ser
ajustados numa nova rodada.

## Proveniência do painel (ARS `review-panel-provenance/1.0`)

- Artefato: `review_panel_provenance.json` (entrada em `provenance_input.json`), construído e validado com
  `scripts/review_panel_provenance.py` do ARS (replay PASS). SHA-256 do artefato:
  `bf36391ca80db2764f834457e2f3108857c396d87cafb74bcc3281c5ac410cf0`.
- Escopo de contexto: `within_panel_attempt_only`.

| Assento | Role ID | Ator | Contexto | Viu saídas dos pares | Família de modelo | Provedor | Revisor humano |
| --- | --- | --- | --- | --- | --- | --- | --- |
| EIC | aval-pol-stage3:eic | modelo | sessão única | sim | claude | anthropic | nenhum |
| R1 | aval-pol-stage3:methodology | modelo | sessão única | sim | claude | anthropic | nenhum |
| R2 | aval-pol-stage3:domain | modelo | sessão única | sim | claude | anthropic | nenhum |
| R3 | aval-pol-stage3:perspective | modelo | sessão única | sim | claude | anthropic | nenhum |
| DA | aval-pol-stage3:devils_advocate | modelo | sessão única | sim | claude | anthropic | nenhum |

| Eixo | Status |
| --- | --- |
| Papéis separados | true |
| Contextos separados no painel | false |
| Cego às saídas dos pares | false |
| Famílias de modelo distintas | false |
| Provedores distintos | false |
| Revisores humanos distintos | false |

- **Independência**: não computada. A separação de papéis prova só a separação de papéis.
- **Divulgação de erro correlacionado (texto fixo do ARS)**: "All model-executed review seats used one model family;
  role separation does not remove correlated-error risk."
- **Divulgação adicional**: os cinco assentos foram executados pelo mesmo modelo, na mesma sessão, que redigiu o
  rascunho e fez a auditoria do Stage 2.5. O risco de erro correlacionado inclui o de autorrevisão: pontos cegos do
  autor tendem a se repetir no revisor. O contrato de sprint do ARS (Phase 1 cega ao manuscrito, Phase 2 com o
  manuscrito) não foi executado, porque o manuscrito já estava no contexto; por isso a decisão segue o caminho
  "`full` sem contrato" de `references/editorial_decision_standards.md` § 0 (critérios qualitativos), e os
  verificadores de conformidade de fase não se aplicam. Para uma revisão com cegueira real, rodar os assentos em
  sessões novas ou com revisores humanos (os professores e a dupla).
