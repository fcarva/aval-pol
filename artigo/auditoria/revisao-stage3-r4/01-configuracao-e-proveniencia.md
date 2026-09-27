# Stage 3, rodada 4: configuração do painel e proveniência

- **Manuscrito:** `artigo/rascunho-artigo.md`, sha256 `15d70ff9…fcd64a`, commit `898ac9c`.
- **Modo:** `full`, sem contrato de sprint.
- **Data:** 27/09/2026, véspera da entrega.

## Phase 0: análise de campo

| Item | Leitura |
| --- | --- |
| Disciplina principal | Avaliação de políticas públicas (economia aplicada) |
| Disciplinas secundárias | Gasto tributário; economia da cultura; bens públicos; avaliação de impacto (promoção aleatória com conglomerados, VI, RD no tempo, experimento conjunto) |
| Paradigma | Avaliação de desenho com teoria da mudança + proposta de avaliação, sem estimação |
| Tipo de texto | Mini artigo de disciplina (PECO 5046-6046), 10-15 páginas, autor único |
| Critério de destino | Instruções da disciplina e o material de aula (slides de TdM, resultados potenciais, validade, amostragem e poder); regras do `CLAUDE.md` |
| Maturidade | Terceira revisão aplicada; texto estável; dados 60/60 e captação 75/75 |

## Cartões de configuração

O foco desta rodada é **pôr o texto à prova com o material da disciplina e com os dados**. Os cartões mudam de
acordo com isso.

| Assento | Identidade configurada | Foco |
| --- | --- | --- |
| EIC (Journal-Fit Reviewer) | Professor da disciplina que corrige com o roteiro das instruções e dos slides | Seções obrigatórias; os cinco passos do J-PAL entregues; clareza para o leitor da banca |
| R1 (Metodologia) | Economista de avaliação de impacto, especialista em amostragem e poder com conglomerados e cumprimento parcial | Tabela 2 contra as regras dos slides (30 a 50 conglomerados por grupo; cumprimento parcial; VI); dados que reforçam a identificação |
| R2 (Domínio) | Pesquisador de economia da cultura e gasto tributário, leitor atento das normas e da literatura citada | Alinhamento entre afirmação e fonte; vocabulário da disciplina; indicadores e riscos da TdM |
| R3 (Perspectiva) | Especialista em transparência fiscal e dados abertos (LAI, LGPD, Diário Oficial) | O que é público e o artigo trata como não publicado; recomendações de gestão |
| DA (assento fixo) | — | O ponto mais fraco da proposta: se as perguntas centrais têm desenho capaz de respondê-las |

**Checkpoint da Phase 0.** O autor pediu o modo `full` explicitamente; os cartões ficam registrados aqui.

## Proveniência (ARS `review-panel-provenance/1.0`)

Artefato: `review_panel_provenance.json`, gerado de `provenance_input.json` e validado com
`ferramentas/academic-research-skills/scripts/review_panel_provenance.py`.

| Assento | Ator | Contexto | Viu saídas dos pares | Família | Provedor | Revisor humano |
| --- | --- | --- | --- | --- | --- | --- |
| EIC, R1, R2, R3, DA | modelo | sessão única, em sequência | sim | claude | anthropic | nenhum |

- **Independência:** não computada. A separação de papéis prova só que os papéis foram separados.
- **Erro correlacionado (texto fixo do ARS):** "All model-executed review seats used one model family; role
  separation does not remove correlated-error risk."
- **Autorrevisão:** o mesmo modelo, na mesma sessão, escreveu e revisou o artigo. Para reduzir o risco, os achados com
  peso na decisão foram refeitos a partir de arquivos, não de memória:
  - o poder, por um script novo (`analise/19_poder_revisao.py`) com as fórmulas de `analise/05_poder_mde.py`;
  - a cobertura de CNPJ e os depósitos, por `analise/18_dio_avisos_habilitacao.py`;
  - as regras do material, nas sínteses de `notas/disciplina/`, com página ou slide.
- **Cegueira real:** exige sessões novas ou revisores humanos (os professores da disciplina).
- **Calibração:** `NOT_CALIBRATED`.
