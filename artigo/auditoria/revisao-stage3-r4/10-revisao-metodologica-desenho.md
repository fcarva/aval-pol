# Revisão metodológica do desenho refeito (ARS `methodology-focus`)

- **Pedido do autor (27-28/09/2026):** "Não mudar as hipóteses, mudar o desenho de avaliação de política"; "vamos
  reexecutar as skills, rever os dados para tentar atacar esse problema". A ideia, tácita, é ver se a escolha
  concentrada deixa de fora bens públicos e projetos pequenos que sinalizariam necessidades reais de financiamento.
- **Texto revisado:** §5 de `artigo/rascunho-artigo.md`, na versão do commit `bbfabfa`: Quadro 3 com regras de
  decisão; H1 com braço de residentes; H2 com avaliação cega; H3 com acúmulo no teto; H5 prospectivo.
- **Modo:** `methodology-focus`, com dois assentos: Journal-Fit (EIC) e Metodologia (R1). Sem contrato de sprint,
  porque o manuscrito já estava no contexto.
- **Proveniência:** o artefato `review-panel-provenance/1.0` só se aplica ao modo `full`. Os dois assentos rodaram no
  mesmo modelo e na mesma sessão que escreveu o desenho. Divulgação: "All model-executed review seats used one model
  family; role separation does not remove correlated-error risk." Estado: `NOT_CALIBRATED`.
- **Regra de leitura:** os revisores não alteram o texto. As correções abaixo foram aplicadas depois, dentro do
  mandato do autor ("mudar o desenho de avaliação").

## Dados revistos para esta rodada

| Fonte | O que se buscou | Resultado |
| --- | --- | --- |
| API do Mapa, resumo das oportunidades da LICC (479, 1415, 1878, 2317) | Número de inscritos (Tabela 1, "Projetos inscritos") | `summary: null` nas quatro oportunidades: a contagem não é pública. O método de avaliação registrado é "Avaliação Documental", sem nota, o que reforça H2. As categorias de 2025 e 2026 são as seis linhas |
| API do Mapa, eventos ligados a projetos | Resultado de H5 (realização datada) | 432 eventos ligados a 161 projetos do Mapa todo; ligados a processos da LICC, 18 projetos com evento datado (`dados/externos/mapa_eventos_licc.csv`). Fonte de *Y* parcial |
| Versões do anexo de captação de 2024 (`13_versoes_captados_fila.csv`) | Variação no momento do recebimento | 47 termos recusados em alguma versão; 27 validados em versão posterior, no ano da ampliação do teto (Portaria SEFAZ 57-S/2024, de R$ 15 para R$ 25 milhões); 20 nunca validados |
| Poder (`analise/19_poder_revisao.py`) | Desenhos novos | H1, diferença empresas − população, de 8,2 a 19,7 pontos; H2, avaliação cega, 0,43 DP (habilitados × inabilitados) e 0,35 DP (captou × não captou); H5, de 112 a 168 recusados por braço para detectar 15 pontos |

## EIC (Journal-Fit): aderência ao material

- **E1.** O desenho agora cumpre o critério de Gertler *et al.* (2018, p. 40-42) de "hipótese testável e quantificável":
  o Quadro 3 traz a regra que derruba cada premissa. Resolve a queixa de "enrolação" da auditoria anterior
  (`09-auditoria-desenho-hipoteses.md`).
- **E2.** A §5 chama-se "Proposta de avaliação de impacto", mas H2 (e o acúmulo de H3) são testes descritivos da regra
  de decisão, que é pergunta normativa (Gertler *et al.*, p. 8). **Pede-se rótulo explícito** para não prometer efeito
  causal onde não há. Aplicado: "O teste, descritivo, é uma avaliação cega da regra de decisão".
- **E3.** A frase de enquadramento (avaliação de elos, sem efeito sobre o resultado final) segue o boxe 2.2 e é honesta.
  Sem mudança.

## R1 (Metodologia)

- **M1 (MAJOR): o tempo de H5 estava subdeclarado.** O texto dizia "acumulados em alguns ciclos". Com 11 a 21 projetos
  recusados por ano (2023-2024), 112 a 168 por braço exigem de 6 a 16 ciclos. **Pedido:** dizer o número e que H5 só
  decide no longo prazo ou com esgotamentos mais frequentes. Aplicado.
- **M2 (MAJOR): uma variação existente não era usada.** Em 2024, 27 das 47 recusas viraram validação em versão
  posterior do anexo. A comparação com as 20 que não viraram mede o efeito de receber mais tarde, com dado público.
  Aplicado em H5, com as checagens N81 e N82. Cuidado a declarar na análise: a validação tardia pode ter seguido a
  ordem da fila, e isso se testa com as datas.
- **M3 (MINOR): manipulação da variável de corte.** Na regressão descontínua no tempo, o momento do esgotamento não é
  conhecido de antemão, o que dificulta a manipulação da posição na fila. Aplicado numa oração.
- **M4 (MINOR): comparação entre grupos no experimento conjunto.** Comparar efeitos marginais médios entre subgrupos
  depende da categoria de referência; comparam-se as médias marginais de escolha. E o elo com a premissa precisa ser
  dito: aplicados aos habilitados, os dois conjuntos de pesos indicam o que cada grupo financiaria. Aplicado. (A
  referência metodológica para médias marginais não foi acrescentada, porque não há como conferi-la hoje.)
- **M5 (MINOR): avaliação cega de projetos conhecidos.** Festivais antigos não são anônimos para avaliadores locais. Os
  dois avaliadores por projeto (§5.5) medem a confiabilidade; recomenda-se ainda que um deles seja de fora do estado.
  Fica para o plano de campo, sem espaço nas 15 páginas.
- **M6 (sem mudança):** H4 segue o desenho mais sólido; a regra de 30 a 50 conglomerados por grupo é atendida com todos
  os agentes.

## Decisão: **revisão menor**, aplicada

| Item | Onde | Status |
| --- | --- | --- |
| E2 | §5.2, H2 | aplicado |
| M1 | §5.4 | aplicado (N83) |
| M2 | §5.2, H5 | aplicado (N81, N82) |
| M3 | §5.2, H5 | aplicado |
| M4 | §5.2, H1 | aplicado |
| M5 | plano de campo | registrado, fora do texto |

**Conferência depois da aplicação:**
- `checar_dados.py`: 79/79;
- `checar_referencias.py`: 50 referências;
- PDF com 15 páginas, sem glifos ausentes nem linhas estouradas.
