# Stage 3, rodada 3: configuração do painel e proveniência

- **Manuscrito:** `artigo/rascunho-artigo.md`, sha256
  `efc89e2a1e2d6b947c3ec3cd5e86e9f727c0bec02c74f798d15140f75b9ddbf7`, commit `b4184cd`.
- **Versão LaTeX:** `artigo/latex/artigo.tex`, sha256 `f318d8ce…f116140`, 15 páginas.
- **Modo:** `full`, sem contrato de sprint.
- **Data:** 27/09/2026.
- **Pedido do autor:** "faça a revisão dos pareceristas de novo com as novas hipóteses".

## Por que uma rodada completa

A versão revisada na rodada 2 tinha as hipóteses H1a, H1b, H2a, H2b e H3. Esta versão reorganiza a teoria da mudança
em torno de cinco novas premissas:

| Nova premissa | Origem |
| --- | --- |
| H1 marketing | antiga H1a |
| H2 centralização | antigas H2a + H2b |
| H3 taxa de serviço | nova |
| H4 exclusão | antiga H3 + porte |
| H5 entrega | antiga H1b |

O que mudou no texto:
- as seções 4 e 5 foram reescritas;
- o Quadro 2, o Quadro 3, a Tabela 2 e a Figura 1 são novos;
- entraram fatos de norma novos (IN 001/2026) e um desenho novo (experimento conjunto).

Como o objeto da revisão mudou, cabe uma revisão completa, e não um re-review.

## Phase 0: análise de campo

| Item | Leitura |
| --- | --- |
| Disciplina principal | Avaliação de políticas públicas (economia aplicada) |
| Disciplinas secundárias | Gasto tributário; economia da cultura e do patrocínio; provisão de bens públicos; avaliação de impacto (experimentos com decisores, VI com designação de avaliador, RD no tempo) |
| Paradigma | Avaliação de desenho (teoria da mudança e auditoria de premissas com normas e dados administrativos) + proposta de avaliação sem estimação |
| Tipo de texto | Mini artigo de disciplina (PECO 5046-6046, PPGEco/UFES), 10-15 páginas, seções definidas pela disciplina, 1ª parte do curso |
| Critérios de destino | Instruções da disciplina (seções obrigatórias; desenho amostral, fontes e poder); regras do `CLAUDE.md`, com o escopo revisto em 27/09/2026 (moldura de bens públicos tácita, sem redesenho do mecanismo) |
| Maturidade | Versão reescrita na véspera da entrega (28/09). Dados 57/57, captação 75/75, 20 DOIs conferidos |

## Cartões de configuração

| Assento | Identidade configurada | Foco |
| --- | --- | --- |
| EIC (Journal-Fit Reviewer) | Editor de revista aplicada de políticas públicas que confere também o enunciado da disciplina | Coerência entre problema, premissas e perguntas; aderência às seções; clareza da nova moldura |
| R1 (Metodologia) | Economista de avaliação de impacto: experimentos de escolha (*conjoint*), designação de avaliadores como instrumento, filas e racionamento, poder com conglomerados | Identificação de H1, H2, H4 e H5; parâmetros; amostra; poder |
| R2 (Domínio) | Pesquisador de economia da cultura, patrocínio empresarial e gasto tributário no Brasil (Rouanet e leis estaduais via ICMS), com leitura das normas | Exatidão das afirmações sobre as normas; literatura da nova moldura |
| R3 (Perspectiva) | Especialista em governança de gastos tributários, transparência (LAI, LGPD) e ética em pesquisa com empresas | Conceitos (centralização × delegação), viabilidade de dados e de campo, recomendações |
| DA (advogado do diabo, assento fixo) | — | Contra-argumento mais forte à nova moldura, tautologias, vocabulário normativo, alternativas |

**Checkpoint da Phase 0.** O autor pediu a revisão com o painel de cinco assentos; os cartões ficam registrados aqui.

## Proveniência (ARS `review-panel-provenance/1.0`)

Artefato: `review_panel_provenance.json`, gerado de `provenance_input.json` e validado com
`ferramentas/academic-research-skills/scripts/review_panel_provenance.py` (ver `07-decisao-editorial.md` para o
resultado do replay).

| Assento | Ator | Contexto | Viu saídas dos pares | Família | Provedor | Revisor humano |
| --- | --- | --- | --- | --- | --- | --- |
| EIC, R1, R2, R3, DA | modelo | sessão única, em sequência | sim | claude | anthropic | nenhum |

- **Independência:** não computada. A separação de papéis prova só que os papéis foram separados.
- **Erro correlacionado (texto fixo do ARS):** "All model-executed review seats used one model family; role
  separation does not remove correlated-error risk."
- **Autorrevisão:** o mesmo modelo, na mesma sessão, reescreveu o artigo. Para reduzir o risco de revisar o próprio
  texto de memória, os achados com peso na decisão foram conferidos de novo nas fontes primárias:
  - IN 001/2025, arts. 23, 26-28, 55 e 64, e IN 001/2026, arts. 28 e 40, nos textos de
    `notas/politica/fontes/`;
  - a lista de pareceristas e as tabelas `10_*.csv`;
  - as linhas do manuscrito citadas em cada achado.
- **Contrato de sprint:** não executado (manuscrito já no contexto); caminho "`full` sem contrato"
  (`references/editorial_decision_standards.md`, § 0).
- **Cegueira real:** exige sessões novas ou revisores humanos (a professora, o professor ou a dupla).
