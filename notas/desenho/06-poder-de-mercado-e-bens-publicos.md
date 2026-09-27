# Poder de mercado, centralização, apropriação e exclusão: a nova moldura das hipóteses (27/09/2026)

> **Full mode** (deep-research, Fases 1-3 enxutas), pedido do autor em 27/09/2026. O autor não ficou satisfeito com
> H1a-H3. Ele quer um artigo que aponte para quatro coisas:
> - o poder de mercado de grandes empresas que fazem do financiamento de bens públicos culturais uma função de
>   marketing, com benefício fiscal;
> - a centralização da decisão sobre recurso público;
> - a apropriação por taxa de serviço;
> - a exclusão de quem não chega aos grandes contribuintes.
>
> A inspiração é **tácita**: financiamento quadrático e o trabalho de Zoë Hitzig (escolha ponderada por quantas
> pessoas valorizam o bem, e não pelo tamanho da bolsa), Hypercerts (declaração de impacto × entrega) e Open Source
> Observer (entrega medida por rastro público).
>
> Nenhum desses nomes entra no artigo, que segue no molde da 1ª parte da disciplina: avaliação do desenho +
> proposta de avaliação de impacto com inferência causal, lei estadual, Mapa Cultural e anexos oficiais.

## 1. Fatos de norma que sustentam a moldura (todos conferidos no texto)

| Fato | Fonte | Leitura |
| --- | --- | --- |
| Patrocinador é "pessoa jurídica, contribuinte tributário de ICMS" | Dec. 5.035-R/2021, art. 2º, IV | Pessoa física não financia: o público não tem canal de contribuição |
| Crédito presumido de até 100% do patrocínio | Dec. 5.035-R/2021, art. 10 | A empresa escolhe com dinheiro que pagaria de imposto |
| Limite por patrocinador proporcional ao ICMS recolhido (20%, 15%, 10% ou 5%) | Dec. 5.035-R/2021, art. 10, § 1º | O peso de cada empresa na escolha cresce com o imposto que ela paga |
| Empresas do Simples Nacional não podem emitir carta de intenção de patrocínio | IN 001/2026, art. 40, § 3º | Pequenas empresas ficam fora da escolha |
| O objeto do projeto inclui "uso correto da logomarca" | IN 001/2025, art. 64, par. único | A exposição da marca é parte do que se executa com recurso público |
| Divulgação e impulsionamento até 25% dos recursos (limite novo em 2025; não havia em 2023-2024) | IN 001/2025, art. 23, V | Até um quarto pode ir para comunicação |
| Captação até 10% (R\$ 50 mil) e elaboração até 5% (R\$ 15 mil), vedadas ao proponente (2023-2025) | IN 2023 e 2024, arts. 18-19; IN 001/2025, arts. 27-28 | Taxa de serviço a intermediários |
| Em 2026, captação e/ou elaboração viram uma despesa única de até 10% (R\$ 50 mil), que pode ser paga ao próprio proponente | IN 001/2026, art. 28, §§ 1º-2º | A taxa passa a poder ficar com o proponente |
| Proponente pode receber até 1/3 dos recursos como remuneração | IN 001/2025, art. 26 | Limite da apropriação pelo proponente |
| Parecer sem nota; fila de termos até esgotar o teto; CAP só depois do patrocínio (2025-2026) | IN 001/2025, arts. 37-45; IN 001/2026, art. 40 | A decisão que ordena é da empresa, e a que desempata é o relógio |

Tabela reproduzível: `analise/tabelas/10_rubricas_teto_in.csv`. O script `analise/10_poder_mercado_rubricas.py`
confere cada trecho no texto da norma.

**Taxa de serviço permitida em 2025** (`10_taxa_servico_permitida_2025.csv`): aplicando os limites de captação e
elaboração ao valor captado de cada projeto, até **R\$ 3,36 milhões (13% dos R\$ 25 milhões)** poderiam remunerar
intermediários, e até R\$ 6,25 milhões (25%), a divulgação. São limites, não gasto: o gasto efetivo só as planilhas
de custos (LAI) mostram.

## 2. Brief da pergunta (research_question_agent)

**Pergunta.** Quando o Estado abre mão de imposto e delega a escolha a quem o recolhe, o financiamento produz bem
público cultural ou financia a marca de quem escolhe, e para quem?

**Subperguntas (as novas premissas da teoria da mudança):**

| | Premissa testada | Substitui | Estado com o dado público |
| --- | --- | --- | --- |
| **H1 Marketing** | A empresa escolhe pelo valor público do projeto, não pelo retorno de marca que obtém sem custo | H1a | Não sustentada. Duas empresas somam metade da renúncia de 2025; energia e gás, 52%; a marca integra o objeto; divulgação até 25% |
| **H2 Centralização** | A decisão sobre recurso público segue critério público (mérito, preferência de quem usa) | H2a, H2b | Não assegurada pelo desenho. Parecer sem nota, fila no teto, escolha pela empresa; o público não participa |
| **H3 Apropriação** | O recurso incentivado chega ao bem cultural, não à intermediação | nova | Indeterminada sem planilhas. Os limites permitem até 13% em taxa de serviço (2025); em 2026 ela pode ficar com o proponente |
| **H4 Exclusão** | Quem não chega aos grandes contribuintes consegue financiar bem público | H3 + porte | Não sustentada. Captação dos pedidos até R\$ 400 mil: 79% → 27% (2022-2024); Simples Nacional fora (2026); 14 municípios do interior sem projeto |
| **Entrega** | O financiamento produz o bem cultural, que não ocorreria de todo modo, e isso é verificável | H1b | Indeterminada. Mais da metade dos recusados captou depois; o relatório de execução (público) não é publicado |

## 3. Blueprint (research_architect_agent)

| Hipótese | Desenho causal | Parâmetro | Hipótese de identificação | Dado | Poder |
| --- | --- | --- | --- | --- | --- |
| H1 | Experimento conjunto com decisores de empresas contribuintes (perfis sorteados: escala, visibilidade, local, gratuidade, público) | Efeito marginal médio de cada atributo sobre a escolha (AMCE) | Sorteio dos perfis; escolha declarada ≈ revelada (validar com os patrocínios reais) | Aplicação própria; lista de patrocinadores nos anexos | 60 respondentes × 12 tarefas: EMD de 7,4 a 13,4 pp (`10_poder_conjoint.csv`) |
| H2 | VI pela severidade do parecerista (designação por ordem e área); RD no tempo em torno do esgotamento | Efeito do parecer favorável; efeito de receber agora | Designação como sorteio dentro de área e período; chegada não manipulada perto do corte | Parecerista por inscrição e fila da SEFAZ (LAI) | Depende do nº de pareceristas por área (lista de 18/09/2026) |
| H3 | Mudança de regra por intensidade: teto de 25% de divulgação (2025) e taxa paga ao proponente (2026). DiD entre projetos com planilha acima e abaixo do limite antes da regra | Efeito do limite sobre a composição do gasto | Tendências paralelas da composição entre os grupos | Planilhas de custos (LAI) | A calcular com as planilhas |
| H4 | Promoção sorteada de apoio à inscrição e à busca de patrocínio entre municípios do interior | Intenção de tratar; LATE | Sorteio; saturação para o deslocamento | Mapa Cultural + inscrições (LAI) | 71 municípios: EMD de 2,8 a 8,5 pp |
| Entrega | Margem do racionamento (recusados × validados; RD no tempo), com resultado por rastro público: agenda do Mapa, DIO e lista de presença (art. 66), declarado × entregue | Efeito de receber agora | Ordem de validação não ligada ao projeto (testar com as datas) | Anexos + rastros | 32 × 32: 28 a 34 pp (só efeitos grandes) |

**Recomendação.**
- H1 é a pergunta nova de maior valor: identifica, por sorteio, se atributos de visibilidade pesam mais que os de
  valor público na escolha de quem decide.
- A entrega continua sendo o resultado da política, medida por rastro verificável, e não por relatório.
- H3 fica aberta ao DiD da 2ª parte.

## 4. Checkpoint do advogado do diabo

| # | Objeção | Gravidade | Resposta |
| --- | --- | --- | --- |
| 1 | "Marketing" não é ilegal nem necessariamente ruim: patrocínio com marca pode financiar bem público de verdade | Alta | A hipótese não é de desvio. Ela pergunta **o que pesa** na escolha. O *conjoint* separa visibilidade de valor público; se os dois andarem juntos, a premissa fica de pé |
| 2 | Escolha declarada no *conjoint* ≠ escolha real | Média | Validar com os patrocínios observados (anexos): os atributos que pesam no experimento precisam prever os pares empresa-projeto reais |
| 3 | Poucos decisores: a população de patrocinadores tem dezenas de empresas | Alta | Ampliar a população aos contribuintes elegíveis (não Simples) com ICMS relevante; 60 × 12 dá EMD de ~7-13 pp |
| 4 | "Apropriação" sugere irregularidade | Média | Usar "taxa de serviço permitida" e "gasto efetivo", sempre com o limite normativo e a ressalva de que o gasto é indeterminado sem as planilhas |
| 5 | A concentração em energia reflete a do ICMS, não uma escolha | Média | Já no texto; por isso a H1 pede o experimento, não a concentração |
| 6 | Linguagem de mecanismo alternativo vazando para o texto | Baixa | Verificação por busca: nenhum "quadrático", "Hypercerts", "Open Source Observer" ou "Hitzig" no artigo |

**Veredito: PASS**, com as ressalvas 1 e 4 incorporadas à redação.

## 5. Literatura (só conferida)

- **Já no artigo:** Throsby (1994); Feld, O'Hare e Schuster (1983); O'Hagan e Harvey (2000); Bertrand *et al.*
  (2020); Dekker e Rodrigues (2019); Costa, Medeiros e Bucco (2017); Belem e Donadone (2013); Moynihan, Herd e Harvey
  (2015); Finkelstein e Notowidigdo (2019); Maestas, Mullen e Strand (2013).
- **Conferidas pelo relé** (entram se couber):
  - Hainmueller, Hopkins e Yamamoto (2014), *conjoint*, 10.1093/pan/mpt024;
  - Cornwell e Maignan (1998), patrocínio, 10.1080/00913367.1998.10673539;
  - Bergstrom, Blume e Varian (1986), 10.1016/0047-2727(86)90024-1.
- **Uso tácito:** Ogava, Galvão e Adamczyk (2022), Enap. Só o diagnóstico da Rouanet (concentração no poder
  econômico dos doadores), depois de conferido no PDF pelo relé.
- **Fica nas notas, não no artigo:** Buterin, Hitzig e Weyl (2019), *A flexible design for funding public goods*,
  *Management Science*, 10.1287/mnsc.2019.3337 (não conferido; não será citado).
