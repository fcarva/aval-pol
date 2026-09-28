# Parecer do R1 (Metodologia), rodada 5

**Recomendação: revisão menor, com dois pontos obrigatórios (M1, M2).**

**Resposta à pergunta do autor ("conseguimos fazer o que é pretendido?"):** em parte, e mais do que o texto mostra.
Os desenhos atuais são prospectivos ou experimentais (conjunto, avaliação cega, promoção aleatória, fila prospectiva)
e testam a pergunta central no futuro. Os dados que **já existem** permitem três desenhos **retrospectivos**
(TIP2 [s.6]: grupos formados depois da implementação), que o texto não usa.

## M1 (obrigatório): desenhos retrospectivos, com o estimador nomeado

| Hipótese | Desenho retrospectivo | Estimador | Tamanho e EMD (`20_desenho_retroativo.csv`) | Leitura |
| --- | --- | --- | --- | --- |
| H4 | Captação dos pedidos pequenos (até R$ 400 mil) × pedidos maiores, quando a demanda habilitada cresce (valor autorizado de R$ 23 milhões em 2022 para R$ 47 milhões em 2024) | Diferenças em diferenças com intensidade: faixa de valor × valor autorizado do ciclo, com efeitos fixos de ciclo e de faixa e erro-padrão por proponente | 293 habilitados resolvidos; o contraste 2022 × 2024 só com o teto exato tem EMD de 62 pontos (9 projetos no teto em 2022) | Usar o valor pedido como variável contínua e todos os ciclos, e não só duas células; mesmo assim, é evidência sugestiva: tendências paralelas não se testam com três ciclos |
| H5 e H2 | Ampliação do teto em maio de 2024 como choque de oferta: 27 termos recusados foram validados depois; 64 validados sem recusa; 20 nunca validados | Comparação dos marginais (validados depois) com os inframarginais, com inferência por aleatorização (amostra pequena) | EMD de 32 pontos (27 × 64) e de 41 (27 × 20) | Diz quem recebe o dinheiro marginal: se forem os mesmos patrocinadores e projetos já escolhidos, ampliar o teto não muda quem escolhe |
| H1 | Preferência revelada: entre os habilitados de cada ciclo, quem é escolhido | Logit condicional (ou modelo linear de probabilidade) com escala, antiguidade do evento, RMGV, recorrência do proponente e efeitos fixos de ciclo e cota | 293 habilitados; EMD de 16 pontos por atributo binário | **Não é causal**: a qualidade do projeto confunde. É o retrato do critério revelado, que o experimento conjunto identifica causalmente |

## M2 (obrigatório): a regra de H5 pede teste de equivalência

"Os recusados realizam o projeto na mesma proporção que os validados" é uma afirmação de ausência de efeito. Não
rejeitar a hipótese nula não a sustenta. A regra correta é: diferença menor que o EMD, por teste de equivalência (dois
testes unilaterais).

## M3 (sugerido): amostras pequenas

Na comparação de 2024 e na margem de 2023-2024, usar inferência por aleatorização ou teste exato. O autor considerou a
parte de teste estatístico coerente; fica como menção.

## M4 (conferido)

A Tabela 2 e a §5.4 seguem as fórmulas do curso. Nada a mudar.
