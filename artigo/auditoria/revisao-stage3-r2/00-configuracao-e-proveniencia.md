# Stage 3, rodada 2: configuração do painel e proveniência

- **Manuscrito:** `artigo/rascunho-artigo.md`, sha256 `6b278d2d0993491d3d87883227310c8e2c1f94f3518944d4b8e8f83926bcaf24`, commit `9e688c0`.
- **Versão LaTeX correspondente:** `artigo/latex/artigo.tex`, sha256 `e6ccb7cd…69511e5`, 15 páginas.
- **Modo:** `full` · **Data:** 24/09/2026.

## Por que uma rodada completa, e não um re-review

A rodada 1 (`../revisao-stage3/`) examinou outra versão (sha256 `99ea6805…5a0834`). Naquela versão, a proposta era uma
avaliação por diferenças em diferenças com adoção escalonada no nível do proponente. Depois dela, o artigo foi
reestruturado em torno da teoria da mudança e de cinco premissas (H1a, H1b, H2a, H2b, H3). As seções 4 e 5 foram
reescritas, e a figura, o Quadro 2, o Quadro 3 e a Tabela 2 são novos. A maioria dos itens da rodada 1 perdeu o objeto.

Um re-review exigiria o pacote de evidências de revisão e as decisões dos autores item a item, e esse pacote não
existe. Por isso esta é uma revisão completa nova, que o protocolo do ARS prevê como "user-requested fresh full review".
O destino de cada item da rodada 1 está em `07-rastreabilidade-rodada1.md`.

## Phase 0: análise de campo

| Item | Leitura |
| --- | --- |
| Disciplina principal | Avaliação de políticas públicas (economia aplicada) |
| Disciplinas secundárias | Gasto tributário; economia da cultura; avaliação de impacto (resultados potenciais, experimentos e quase-experimentos) |
| Paradigma | Avaliação de desenho (teoria da mudança e auditoria de premissas com dados administrativos) + proposta de avaliação sem estimação |
| Tipo de texto | Mini artigo de disciplina de pós-graduação (PECO 5046-6046, PPGEco/UFES), 10-15 páginas, seções definidas pela disciplina |
| Referência de periódico | Revistas aplicadas brasileiras de políticas públicas (*Planejamento e Políticas Públicas*, *Revista de Administração Pública*) |
| Critérios de destino | Instruções da disciplina (seções obrigatórias; desenho amostral, fontes de dados e poder); material da disciplina como base metodológica; regras de `CLAUDE.md` |
| Maturidade | Rascunho avançado. Dados conferidos (40/40), 26 referências com DOI conferido, 15 páginas |

## Cartões de configuração

| Assento | Identidade configurada | Foco |
| --- | --- | --- |
| EIC (Journal-Fit Reviewer) | Editor de revista aplicada de políticas públicas que confere também o enunciado da disciplina | Aderência às seções e ao gênero, clareza, prontidão para entrega |
| R1 (Metodologia) | Economista de avaliação de impacto: resultados potenciais, experimentos naturais em filas e racionamento, desenhos com encorajamento, poder com conglomerados | Parâmetros, vieses, identificação, amostra, poder |
| R2 (Domínio) | Pesquisador de economia da cultura e de política cultural brasileira (Rouanet, leis estaduais, fomento direto) | Revisão, políticas similares, enquadramento teórico |
| R3 (Perspectiva) | Especialista em governança de gastos tributários, transparência e ética em pesquisa com dados administrativos | Viabilidade de acesso aos dados, ética, recomendações de gestão, partes interessadas |
| DA (Advogado do diabo, assento fixo) | — | Argumento contrário mais forte, explicações alternativas, generalizações, teste do "e daí?" |

**Checkpoint da Phase 0.** Os autores pediram para começar a revisão com o painel de cinco assentos. Os cartões ficam
registrados aqui e podem ser ajustados numa nova rodada.

## Proveniência do painel (ARS `review-panel-provenance/1.0`)

- **Artefato:** `review_panel_provenance.json`, gerado a partir de `provenance_input.json` e validado com
  `scripts/review_panel_provenance.py` do ARS (replay PASS). SHA-256 do artefato:
  `50640ee81d0af4b7716e1e783529e81795ea643d32f02397346607c5e03daee1`.
- **Escopo de contexto:** `within_panel_attempt_only`.

| Assento | Ator | Contexto | Viu saídas dos pares | Família de modelo | Provedor | Revisor humano |
| --- | --- | --- | --- | --- | --- | --- |
| EIC, R1, R2, R3, DA | modelo | sessão única, em sequência | sim | claude | anthropic | nenhum |

| Eixo | Status |
| --- | --- |
| Papéis separados | sim |
| Contextos separados | não |
| Cegueira às saídas dos pares | não |
| Famílias de modelo distintas | não |
| Provedores distintos | não |
| Revisores humanos distintos | não |

- **Independência:** não computada. A separação de papéis prova só que os papéis foram separados.
- **Divulgação de erro correlacionado (texto fixo do ARS):** "All model-executed review seats used one model family;
  role separation does not remove correlated-error risk."
- **Autorrevisão:** os cinco assentos foram executados pelo mesmo modelo, na mesma sessão que reescreveu o artigo.
  Para reduzir o risco de revisar o próprio texto de memória, cada achado com peso na decisão foi conferido de novo nas
  fontes primárias, e não na lembrança da redação:
  - os anexos de captação de 2023 e 2024, em `dados/fontes_web/paginas/`;
  - as IN de 2023 e 2024;
  - as tabelas em `analise/tabelas/`.

  A evidência nova está em `evidencia-reentrada-indeferidos-2023.csv`.
- **Contrato de sprint:** o contrato do ARS (Phase 1 cega ao manuscrito) não foi executado, porque o manuscrito já
  estava no contexto. A decisão segue o caminho "`full` sem contrato" (`references/editorial_decision_standards.md`,
  § 0).
- **Cegueira real:** exige rodar os assentos em sessões novas ou com revisores humanos, como os professores ou a dupla.
