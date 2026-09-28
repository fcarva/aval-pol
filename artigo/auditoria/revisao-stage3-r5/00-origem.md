# Stage 3, rodada 5 (final): origem e escopo

- **Pedido do autor (28/09/2026, dia da entrega):** "vamos fazer uma última avaliação usando full mode para pensar o
  desenho da avaliação de impacto, conseguimos fazer o que é pretendido? [...] acho que a parte do desenho de avaliação
  de impacto não casou com o intento de avaliar o financiamento de bens públicos culturais, centralizados na tomada de
  decisões e captura pela função objetivo marketing das empresas, não sendo ótimo para alocação de pequenos projetos
  [...] vamos pensar retroativamente como pensar o financiamento centralizado e evidenciar isso com inferência causal e
  os dados que a gente tem".
- **Decisões do autor antes do painel (plano aprovado):**
  - o artigo só indica o método de estimação, sem estimativas preliminares;
  - a parte de poder e teste estatístico "está coerente";
  - a ideia de Hitzig entra de forma tácita, como medida da ausência do sinal de amplitude, sem simulação e sem nomear
    o mecanismo;
  - hipóteses H1 a H5 inalteradas; 15 páginas.
- **Manuscrito:** `artigo/rascunho-artigo.md`, sha256 `c0a23e5da3e030d91b99fef8f8fc7ad7d714e747183a1c5ae36c68b9c7d15e0e`, commit `d01657f`.
- **Dados novos para o painel:** `analise/20_financiamento_centralizado.py`, com as tabelas
  `20_patrocinadores_por_projeto.csv` e `20_desenho_retroativo.csv`.

## Critério do painel

O desenho responde à **pergunta central do intento**, ou seja, se o financiamento centralizado na escolha das empresas
desfavorece projetos pequenos e bens de valor público? Âncoras no material:
- Gertler *et al.* (2018): p. 8-9 (tipos de pergunta) e p. 40-42 (hipótese testável; boxe 2.2 sobre avaliação de
  mecanismo);
- IC [s.3-7] (contrafactual válido);
- TIP2 [s.3-12] (prospectiva × retrospectiva; escolha do método pelas regras de operação);
- AMO [s.29-32] (poder).
