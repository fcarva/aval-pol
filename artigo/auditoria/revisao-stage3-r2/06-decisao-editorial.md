# Decisão editorial: Stage 3, rodada 2

- **Manuscrito:** `artigo/rascunho-artigo.md`, sha256 `6b278d2d…26bcaf24` (commit `9e688c0`)
- **Data:** 24/09/2026
- **Modo:** `full`, sem contrato de sprint executado: critérios qualitativos (`references/editorial_decision_standards.md`, § 0).
- **Proveniência do painel:** ver `00-configuracao-e-proveniencia.md`.
  - Papéis separados: sim.
  - Contextos separados, cegueira às saídas dos pares e diversidade de modelo, provedor e revisor humano: não.
  - Independência não computada.
  - Divulgação obrigatória: "All model-executed review seats used one model family; role separation does not remove
    correlated-error risk."
  - O mesmo modelo reescreveu o artigo, com risco de autorrevisão. Por isso os achados com peso na decisão foram
    conferidos de novo nas fontes primárias.

## Decisão: **Minor Revision**, com dez revisões obrigatórias

| Assento | Recomendação | Principal motivo |
| --- | --- | --- |
| EIC | Minor | Acabamento: autoria, declaração, uma referência `[VERIFICAR]`, ambiguidades |
| R1 | Major | Cinco problemas de método nas perguntas H1b e H3 |
| R2 | Minor | Interpretação e contraste, não volume |
| R3 | Minor | Plano de acesso aos dados, ética de H3, recomendação sobre a fila |
| DA | — | Nenhum CRITICAL; três MAJOR |

Três dos quatro assentos com recomendação indicam Minor. A matriz de decisão manda decidir pelos problemas. O critério
de Minor exige que "nenhum problema exija reestruturar argumentos ou métodos centrais". Os cinco MAJOR do R1 e os três
do DA:
- mudam o que a proposta diz que consegue estimar;
- corrigem um sinal de viés;
- trocam um rótulo de veredito;
- ajustam o conteúdo de uma oferta.

Todos se resolvem dentro da estrutura atual: seção 4 com cinco premissas, seção 5 com três perguntas. Dois pedem
análise nova, mas pequena e com dados já no repositório ou acessíveis pelo relé: a reentrada dos indeferidos de 2024 e
a contagem do cadastro do Mapa Cultural. Por isso a decisão é Minor Revision, **no limite superior**.

Todos os itens de gravidade MAJOR são **obrigatórios**. A reavaliação (Stage 3') confere cada um contra o texto
revisado.

**Arbitragem da divergência EIC × R1.** O R1 recomenda Major por olhar o núcleo metodológico; o EIC, Minor por olhar
forma e escopo. Prevalece a evidência. Os problemas do R1 estão ancorados:
- na álgebra da decomposição que o próprio artigo anuncia (W1);
- em conferência nos anexos oficiais (W2: 7 de 11 projetos com termo indeferido em 2023 captaram em 2024);
- no título oficial da lista de indeferidos (W3);
- na definição do estimador (W4);
- na nota da tabela de poder (W5).

Por isso entram todos como obrigatórios. A gravidade, porém, não exige reestruturação, e a decisão fica em Minor.

## Adjudicação dos achados MAJOR do advogado do diabo

| Achado | Veredito do sintetizador | Justificativa |
| --- | --- | --- |
| DA-M1 (padrão de avaliação de H2a e H2b) | **Validado** | O Quadro 2 usa "95 de 293 expiraram" como evidência para H2a, e esse número não distingue empresa que ignora o mérito de empresa que segue o mérito (não há nota). O rótulo "não atendida" sugere violação observada; o que o texto demonstra é que nada no desenho assegura a premissa. |
| DA-M2 (oferta de H3 mira o atrito errado) | **Validado** | A própria §2 diz que, desde 2025, o projeto só vai à comissão com termo ou carta de intenção; a oferta da §5.2 cobre só documentação. |
| DA-M3 (H1b sem desenho crível para receber × não receber) | **Validado** | Corrobora R1-W2 com a mesma evidência (reentrada) e o próprio texto ("sem afastar a seleção"). |

Nenhum CRITICAL foi levantado, e nenhum bloqueio de aceitação fica pendente de adjudicação.

## Consenso e corroboração

- **Consenso** (todos os assentos): o artigo cumpre as seções exigidas; a teoria da mudança segue o formato da
  disciplina; a regra "ausência não é zero" é aplicada; as recomendações ficam no escopo. Ninguém pediu redesenho.
- **Corroboração:**
  - R1-W2 e DA-M3 chegam à reentrada dos indeferidos por caminhos diferentes;
  - R1-W3, R3-W3 e DA (caminhos ignorados) chegam à ordem de validação como mecanismo não documentado e como dado a
    publicar;
  - R3-W2 e R1-S2 chegam ao deslocamento pelo teto fixo.

## Revisões obrigatórias (roteiro)

| Item | O que fazer | Onde | Origem |
| --- | --- | --- | --- |
| RV-1 | Corrigir o sinal dos vieses de H1b: com *Y*(0) maior entre os escolhidos, o viés de seleção é positivo e a comparação simples superestima o EMPT; o viés de efeitos heterogêneos age no sentido oposto em relação ao efeito médio | Quadro 3 (H1b) | R1-W1 |
| RV-2 | Racionamento: conferir a reentrada dos 22 projetos indeferidos em 2024 no anexo de 2025; redefinir *Y* com janela de tempo (realizado no ano previsto); tratar o indeferimento como instrumento, com a reentrada como primeiro estágio; ancorar o poder nos 33 termos observados (11 + 22) e dizer que o número de projetos é menor ou igual a 33; retirar "quase experimental" ou qualificá-lo | §5.2 (H1b); Tabela 2; `analise/07_hipoteses_h1_h3.py` | R1-W2; DA-M3 |
| RV-3 | Trocar "ordem de chegada" por "ordem de validação" (o que o anexo documenta) e listar as ameaças à ordem "como se aleatória": calendário da empresa, documentação, tempo da SEFAZ | Resumo; Quadro 2; §4.2; §6; cartão H2b da Figura 1 | R1-W3 |
| RV-4 | Definir as diferenças em diferenças: ou o proponente-ano como unidade (primeira captação; resultados com antes e depois, como a agenda do Mapa Cultural e o SALIC), com a Tabela 2 coerente; ou o projeto como unidade e a estratégia chamada de pareamento sob seleção nos observáveis | §5.2 (H1b); Quadro 3; Tabela 2 | R1-W4 |
| RV-5 | Poder de H3: contar pelo relé os agentes por município e tipo (e com CNPJ, se houver o campo) e recalcular com *J* e *cv* observados; ou dizer que *N* e *m* são hipotéticos e dar o cadastro mínimo para um EMD de 5 pontos | Tabela 2 (H3); §5.4; `dados/fontes_web/pedidos.tsv` | R1-W5 |
| RV-6 | Derivar em uma frase as premissas de H2a e H2b do propósito reconstruído e trocar o rótulo "não atendida" por "não assegurada pelo desenho"; tirar do Quadro 2 a evidência que não decide (95 de 293) ou dizer que ela não distingue as leituras | Resumo; Quadro 2; §4.2 (síntese); §6 | DA-M1 |
| RV-7 | Oferta de H3: incluir informação sobre patrocínio (patrocinadores já publicados; termo e carta de intenção), ou dois braços sorteados (documentação × patrocínio) para separar os atritos, sem mudar regra de alocação | §5.2 (H3); Quadro 3 (H3) | DA-M2 |
| RV-8 | Conclusão: dizer que, com os dados atuais, a adicionalidade (receber × não receber) não tem desenho crível, e qual dado resolveria (ocorrência com janela de tempo e reentrada medida) | §6 | DA-M3 |
| RV-9 | Preencher a autoria e a declaração de IA conforme o modelo da disciplina, com o uso real da ferramenta | Página de rosto; Declaração | EIC-W1 (pendência dos autores) |
| RV-10 | Resolver SECULT (2026d): ler a página, ou reformular a frase sem conteúdo nem data e retirar a marca `[VERIFICAR]` | §1; Referências | EIC-W2 |

## Revisões sugeridas

| Item | O que fazer | Origem |
| --- | --- | --- |
| SG-1 | Reescrever a frase que organiza as hipóteses ("H2a e H2b descrevem como o desenho seleciona; H1a e H3 são explicações concorrentes para quem fica de fora; H1b pergunta se o que é financiado é adicional") | EIC-W3 |
| SG-2 | Desfazer as ambiguidades: "63 projetos captaram, juntos"; "67% em 2022-2026"; 463 processos × 467 registros na nota | EIC-W4 |
| SG-3 | Reescrever a linha H2a do Quadro 3 como pergunta descritiva, coerente com a §5.2 | R1-W6 |
| SG-4 | Dar os números de conversão por faixa de valor (83% × 52%, 2022-2024) | R1-W7 |
| SG-5 | Ressalvar que o sorteio mudaria a regra de alocação e está fora do escopo | R1-W8 |
| SG-6 | Interpretar a sobreposição com a Rouanet (13 de 26 empresas, 86% da renúncia): marketing estruturado × troca de fonte | R2-W1 |
| SG-7 | Uma frase ligando o crédito de 100% às margens avaliadas: sem efeito-preço, restam a troca de fonte e o efeito sobre o projeto | R2-W2 |
| SG-8 | Contraste com o fomento direto estadual (Funcultura ou PNAB, com nota e classificação), se houver espaço | R2-W3 |
| SG-9 | Leis estaduais similares, ou "as avaliações localizadas" | R2-W4 |
| SG-10 | Plano de acesso aos dados: base legal, alternativa se o pedido for negado, prazo (conferir a LC 187/2021 antes de citar) | R3-W1 |
| SG-11 | Ética de H3: implementação gradual para os controles; deslocamento como custo para terceiros; a oferta feita pela SECULT | R3-W2 |
| SG-12 | Recomendar a publicação da fila de validação dos termos | R3-W3 |
| SG-13 | Corrigir as generalizações: estreantes (queda em 2025, recuperação em 2026); difusão (desacelerou, restam 14 municípios); concentração sem referência de comparação; "provavelmente" nos eventos com mais de dez anos | DA-m1 a m4 |
| SG-14 | Definir a versão de entrega (Word ou PDF do LaTeX) e compensar cada acréscimo com um corte | EIC-W5 |

## Orçamento de páginas

As obrigatórias acrescentam, por estimativa, de 12 a 18 linhas. RV-2, RV-4, RV-7 e RV-8 mexem em parágrafos existentes;
RV-3 e RV-6 trocam palavras. A versão LaTeX tem cerca de um quarto de página livre, e a Word, nenhuma.

Cortes candidatos, sem perda de argumento:
- a segunda frase de cada bullet da §5.2 que repete o Quadro 3;
- a lição final da §3 ("Duas lições…"), que a §5.2 já aplica.

## Observações para o Stage 4.5 (integridade final)

- **Figura 1.** Regenerar com o texto do cartão H2b corrigido (RV-3) e conferir que figura, quadro e texto usem o mesmo
  vocabulário: "ordem de validação" e "não assegurada".
- **Números novos.** Reentrada dos indeferidos e contagem do cadastro entram em `checar_dados.py` com a tabela de
  origem.
- **Consistência entre tabelas** (lição da rodada 1). O *n* da Tabela 2 (racionamento) deve bater com
  `03f_captacao_anual_secult.csv` (11 + 22 termos).

## Pareceres completos
- `01-eic-adequacao.md`
- `02-r1-metodologia.md`
- `03-r2-dominio.md`
- `04-r3-perspectiva.md`
- `05-da-advogado-do-diabo.md`
- Evidência: `evidencia-reentrada-indeferidos-2023.csv`
- Itens da rodada 1: `07-rastreabilidade-rodada1.md`

## Errata (Stage 4, 24/09/2026)

A conferência completa e automatizada da reentrada (`analise/09_racionamento_2023_2026.py`, com decisão manual por
candidato em `dados/processados/indeferidos_reentrada_verificacao.csv`) corrige dois números citados nos pareceres R1-W2
e DA-M3:

- **Reentrada.** São **6 de 11** projetos recusados em 2023 que captaram o mesmo projeto em 2024, e não 7. O "Roda
  de Boteco" de 2024 é outra edição (Grande Vitória, e não Colatina). Para 2024: **12 de 21** captaram em 2025 e
  13 até 2026.
- **Tamanho da margem.** São **38 termos em 32 projetos** (16 termos em 11 projetos em 2023; 22 termos em 21
  projetos em 2024), e não "33 termos (11 + 22)". A coluna `termos_indeferidos` de `03f_captacao_anual_secult.csv`
  conta projetos em 2023 e termos em 2024.

As conclusões dos pareceres não mudam: mais da metade dos recusados captou no ano seguinte. A tabela de evidência da
rodada 2 foi substituída por `analise/tabelas/09_reentrada_indeferidos.csv`.
