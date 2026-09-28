# Decisão editorial (Stage 3, rodada 5, final)

**Proveniência:** `review_panel_provenance.json`, replay registrado ao fim deste arquivo.

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
| Menor (E1) | Menor (M1, M2) | Menor (D1) | Menor | Dois MAJOR validados, um MINOR, nenhum CRITICAL |

## Resposta ao autor: "conseguimos fazer o que é pretendido?"

**Sim, com três ajustes.**
1. Escrever a pergunta central: o financiamento centralizado desfavorece projetos pequenos e bens de valor público?
2. Mostrar a ausência do sinal de amplitude.
3. Acrescentar desenhos retrospectivos com dado que já existe, com o estimador nomeado e o limite de cada um:
   - diferenças em diferenças com intensidade;
   - choque de oferta de 2024;
   - preferência revelada.

Os desenhos experimentais e prospectivos ficam como confirmação.

## Decisão: **revisão menor**, com quatro itens obrigatórios

| Item | Fonte | O quê | Onde |
| --- | --- | --- | --- |
| RV5-1 | EIC E1, R2 D1, DA2 | Pergunta central no início da §5.1. Ausência do sinal: 152 dos 213 projetos (71%), com 68% do valor, têm um só patrocinador; o mecanismo não tem canal para registrar quantos valorizam um projeto (BUTERIN; HITZIG; WEYL, 2019) | §5.1 |
| RV5-2 | R1 M1, DA1, DA3 | Desenhos retrospectivos com estimador: H4 diferenças em diferenças com intensidade; H5 e H2 choque de oferta de 2024 ("quem recebe o dinheiro marginal", não efeito); H1 preferência revelada (não causal). A avaliação cega serve de controle de qualidade | §5.2 |
| RV5-3 | R1 M2 | Regra de H5: diferença menor que o EMD, por teste de equivalência | Quadro 3 |
| RV5-4 | Plano aprovado | Manter hipóteses, 15 páginas e nenhuma estimativa de efeito; nada de nome de mecanismo | Todo o texto |

### Sugeridos

| Item | O quê |
| --- | --- |
| SG5-1 | Remissão a Dekker e Rodrigues (2019) em H4 (R2 D2) |
| SG5-2 | Oração sobre a decisão do teto (R3 P1, EIC E3) |
| SG5-3 | Inferência por aleatorização nas amostras pequenas (R1 M3) |

**Checkpoint:** o plano aprovado pelo autor em 28/09 autoriza aplicar RV5-1 a RV5-4 dentro das restrições. Os
sugeridos entram só se couberem nas 15 páginas.

## Replay da proveniência

`review_panel_provenance.py validate`: **PASS**; sha256 `8dfa0e4feb3fbcbcebc66fa127f6bb6e82f782dff206a4130757bea3a77cd3fa`.

## Aplicação (28/09/2026)

Manuscrito depois da aplicação: sha256 `1c2a5269418fa85d721d19f33cea8302c9d8e58674c3579df35ec6d18a87f250`.

| Item | Onde entrou |
| --- | --- |
| RV5-1 | §5.1 começa pela pergunta central. A ausência do sinal (152 dos 213 projetos, 71%, com 68% do valor, com um só patrocinador) vem com a formulação do DA2: "o mecanismo não tem canal para registrar quantos valorizam um projeto" (remissão à seção 4.2, onde está Buterin, Hitzig e Weyl, 2019). Cada hipótese é ligada a uma parte da pergunta |
| RV5-2 | §5.2: cada hipótese com desenho retrospectivo e confirmatório. H4, diferenças em diferenças com intensidade (R$ 23 milhões autorizados no ciclo 2022, R$ 47 milhões em 2024; efeitos fixos de ciclo e faixa; remissão a Dekker e Rodrigues). H1, logit condicional da escolha, declarado não causal. H5 e H2, choque de oferta de 2024: "quem recebe o dinheiro marginal", com inferência por aleatorização, e a pergunta da SEFAZ ao ampliar o teto. H2, a nota cega também como controle de qualidade (DA1) |
| RV5-3 | Quadro 3, H5: "diferença menor que o EMD, por teste de equivalência" |
| RV5-4 | Hipóteses, Quadro 2 e poder mantidos; nenhuma estimativa de efeito; nenhum nome de mecanismo no corpo (varredura: 0) |
| SG5-1, SG5-2, SG5-3 | Entraram em RV5-2 |

**Compensação para 15 páginas:**
- sai a linha "só coletivos" da Tabela 2 (o texto a mantém, com a checagem N40);
- sai a frase "O Mapa serve de retrato da demanda", coberta pela pergunta central;
- o acúmulo no teto por projeto fica numa frase (sai a checagem N57);
- planilhas de custos e relatórios de execução passam a uma linha só no Quadro 4, que agora flutua inteiro;
- a nota de fonte da Tabela 2 e três frases da §5 foram encurtadas;
- a figura passa a 80% da largura.

**Conferência:**
- `checar_dados.py`: 80/80 (N84 a N86 novas; N25 e N57 retiradas com seus trechos);
- `auditar_captacao.py`: 75/75;
- `checar_referencias.py`: 50;
- `mascarar_cpf.py --conferir`: 0;
- PDF com 15 páginas, sem glifos ausentes nem linhas estouradas.
