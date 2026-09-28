# Stage 3, rodada 5: configuração do painel e proveniência

- **Modo:** `full`, sem contrato de sprint (manuscrito já no contexto). Revisores só leem: o manuscrito não é alterado
  por eles.

| Assento | Identidade configurada | Foco |
| --- | --- | --- |
| EIC (Journal-Fit) | Professor da disciplina que lê a §5 contra o intento declarado do autor | A seção responde à pergunta central? |
| R1 (Metodologia) | Economista de avaliação de impacto com dados administrativos retrospectivos (DiD com intensidade, choque de oferta, preferência revelada) | Desenhos retrospectivos possíveis com os dados que existem; estimadores; poder |
| R2 (Domínio) | Economista da cultura e de bens públicos (provisão privada, patrocínio, gasto tributário) | Se a moldura tácita (amplitude do apoio) está bem medida e bem citada |
| R3 (Perspectiva) | Especialista em política fiscal estadual e transparência | Uso para a gestão (decisão sobre o teto; publicação de dados) |
| DA (assento fixo) | — | O contra-argumento mais forte ao intento |

**Checkpoint da Phase 0:** o autor pediu o modo `full`; o plano aprovado fixou o escopo.

## Proveniência (ARS `review-panel-provenance/1.0`)

Artefato: `review_panel_provenance.json`, gerado de `provenance_input.json` e validado por replay com
`ferramentas/academic-research-skills/scripts/review_panel_provenance.py`.

| Assento | Ator | Contexto | Viu saídas dos pares | Família | Provedor | Revisor humano |
| --- | --- | --- | --- | --- | --- | --- |
| EIC, R1, R2, R3, DA | modelo | sessão única, em sequência | sim | claude | anthropic | nenhum |

Divulgação de erro correlacionado: "All model-executed review seats used one model family; role separation does not
remove correlated-error risk." O mesmo modelo escreveu o desenho. Estado: `NOT_CALIBRATED`.
