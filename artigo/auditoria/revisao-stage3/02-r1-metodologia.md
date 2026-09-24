# Parecer — Revisor 1 (Metodologia)

## Informações
- **Rodada**: 1 · **Data**: 24/09/2026
- **Identidade**: econometrista de avaliação de impacto (diferenças em diferenças com adoção escalonada; poder com dados administrativos)
- **Foco**: identificação, unidade de análise, definição e data do tratamento, poder, viabilidade dos dados

## Avaliação geral
**Recomendação**: Major Revision · **Confiança**: 5

**Resumo.** A proposta deriva o método das regras da política, descarta com razão aleatorização, regressão
descontínua e pareamento isolado, e escolhe o estimador certo para adoção escalonada (Callaway e Sant'Anna, duplamente
robusto, com sensibilidade de Rambachan e Roth). O cálculo de poder é transparente. Três problemas, porém, afetam o
núcleo do desenho D1. A unidade de análise está indefinida: o parâmetro é do proponente, mas o poder é calculado em
projetos, com uma identificação de proponente (199) diferente da usada no resto do artigo (172), e 24 proponentes têm
projetos tratados e não tratados. A data do tratamento não é definida — status não tem data — e o grupo "ainda não
tratado" mistura ciclos sob regras diferentes. E os resultados (RAIS) têm massa em zero e chegam com defasagem que
empurra a avaliação para depois de 2028. Há ainda uma comparação melhor, trazida pelos próprios anexos de 2023 e 2024
(termos indeferidos por esgotamento do teto), que o texto não explora. Tudo é reparável sem abandonar a proposta.

## Pontos fortes
### S1: Método derivado das regras operacionais
**Evidence Anchor**: `text: §5.2 "As regras da política determinam o método (GERTLER et al., 2018)"`
A exclusão da regressão descontínua pelo limiar de patrocínio comprometido, escolhido pelos interessados, está correta.

### S2: Estimador e sensibilidade adequados à adoção escalonada
**Evidence Anchor**: `text: §5.2 "usamos o estimador de Callaway e Sant'Anna (2021) na versão duplamente robusta"`

### S3: Poder com cenários, efeito de desenho e erro tipo M
**Evidence Anchor**: `table: Tabela 2 — cenários de R² e ρ, poder 80% e 90%, desenho municipal`

## Fraquezas
### W1: Unidade de análise e identificação do proponente inconsistentes
**Problem**: O parâmetro e os resultados são do proponente (CNPJ), mas n = 293 projetos. O script de poder agrupa
proponentes por normalização simples do nome (199 grupos); a chave canônica usada no resto do artigo
(`chave_proponente`) dá 172 proponentes, m̄ = 1,70 e cv = 0,75. Com a chave canônica, o EMD sem covariáveis e com
ρ = 0,2 sobe de 0,39 para 0,41 (poder de 80%) e de 0,45 para 0,47 (90%). Além disso, 24 dos 172 proponentes têm projetos
que captaram e projetos que expiraram, e o texto não diz como o proponente é classificado.
**Evidence Anchor**: `text: §5.3 "dos quais 293 já tinham situação resolvida (198 captaram e 95 tiveram o prazo expirado), de 199 proponentes"`
**Why it matters**: a unidade de tratamento define o estimador, o agrupamento dos erros e o poder; a divergência entre
chaves faz o artigo relatar dois universos de proponentes.
**Suggestion**: usar a chave canônica em `05_poder_mde.py`; definir o tratamento no nível do proponente como a
primeira captação (coorte = ano da primeira captação) e tratar os mistos como tratados a partir dela; refazer a Tabela 2
em proponentes (G = 172) ou manter projetos com erros agrupados por proponente, mas de forma coerente com o parâmetro.
**Severity**: Major · **Confidence**: 5 — recalculado com `dados/processados/habilitados.csv`

### W2: Data do tratamento e grupo "ainda não tratado" indefinidos
**Problem**: O tratamento é definido pelo status ("em execução" ou "execução finalizada"), que não tem data, e as coortes
seguem o ciclo de habilitação, não o momento da captação. O grupo "ainda não tratado" inclui habilitados de ciclos
posteriores antes de captar, mas a partir de 2025 a habilitação exige compromisso ou carta de intenção, ou seja, esses
projetos já foram escolhidos por patrocinador.
**Evidence Anchor**: `text: §5.2 "como \"ainda não tratados\", os habilitados de ciclos posteriores antes de captar"`
**Why it matters**: em adoção escalonada, errar a data do tratamento contamina o estudo de evento e o teste de
tendências anteriores; e o "ainda não tratado" de 2025 em diante tem seleção diferente.
**Suggestion**: datar o tratamento pelo ano do termo validado nos anexos "Recurso financeiro captado" de 2022 a 2024
(ou pelo extrato de repasse no DIO); restringir os "ainda não tratados" aos projetos de 2022-2024 que captaram mais
tarde; declarar a intensidade (valor captado ÷ autorizado), já que a liberação exige só 50%.
**Severity**: Major · **Confidence**: 5 — regras das IN 2023/2024 (arts. 32-36, 41) e anexos de captação

### W3: Comparação mais crível disponível e não explorada
**Problem**: Os anexos de 2023 e 2024 listam termos de patrocínio indeferidos por ultrapassar o montante (11 termos e
R$ 4,18 mi em 2023; 22 termos e R$ 8,80 mi em 2024). Esses projetos tinham patrocinador disposto e foram racionados
pela ordem de validação, não por mérito nem por falta de interesse de empresa.
**Evidence Anchor**: `table: Tabela 1 — "Termos de patrocínio indeferidos por exceder o montante / montante (2023; 2024) | 28%; 35%"`
**Why it matters**: perto do esgotamento do teto, quem ficou de fora difere de quem entrou sobretudo pela data de
chegada do termo, o que enfraquece a seleção por não observáveis que o próprio texto aponta como principal ameaça.
**Suggestion**: acrescentar, em um parágrafo, um desenho complementar ou de robustez que compare projetos com termos
validados pouco antes do esgotamento com os que tiveram termos indeferidos, discutindo o tamanho pequeno (≈ 30 termos)
e a possível manipulação da ordem; se o limite de páginas apertar, trocar pelo desenho municipal, que o próprio texto
considera fraco.
**Severity**: Major · **Confidence**: 4 — a ordem exata de validação não é publicada e precisa ser confirmada

### W4: Resultados com massa em zero e defasagem de disponibilidade
**Problem**: Muitos proponentes são associações e pequenas empresas culturais com poucos ou nenhum vínculo formal; o EMD
em desvios-padrão não diz nada sobre a distribuição real. E medir de um a três anos após captações de 2023-2024 exige
RAIS de 2025 a 2027, com a defasagem de divulgação do dado identificado.
**Evidence Anchor**: `absence: §5.1 e §5.4 — expected distribuição de base e calendário de disponibilidade da RAIS; checked §5.1, §5.3, Quadro 3, §5.4`
**Why it matters**: com massa em zero, o EMD de uma variável contínua superestima o que se detecta; sem calendário, a
viabilidade fica indefinida.
**Suggestion**: acrescentar resultados na margem extensiva (ter vínculo formal; CNPJ ativo) e resultados disponíveis
antes (novos projetos na LICC, no SALIC e em editais); dizer quando a RAIS permitirá a primeira estimação.
**Severity**: Major · **Confidence**: 4 — conhecimento geral de RAIS; a defasagem exata não foi conferida

### W5: EMD só em desvios-padrão
**Problem**: 0,25 a 0,45 dp não é traduzido em unidades naturais (empregos, massa salarial).
**Evidence Anchor**: `text: §5.4 "O universo disponível detecta, portanto, efeitos a partir de 0,25 a 0,45 desvio-padrão"`
**Why it matters**: sem tradução, o leitor não compara o EMD com efeitos plausíveis.
**Suggestion**: indicar que a tradução virá do desvio-padrão da RAIS anterior a 2022 e dar um exemplo hipotético.
**Severity**: Minor · **Confidence**: 5

### W6: Estimando sob teto vinculante
**Problem**: Com teto vinculante, o grupo de comparação é, em parte, quem foi racionado porque outros captaram; o
EMPT compara "captar" com "ser racionado", não com a ausência da política.
**Evidence Anchor**: `text: §5.5 "com teto vinculante, o que um projeto capta pode faltar a outro"`
**Why it matters**: o texto trata a interferência só como ameaça; ela também define o que o parâmetro significa.
**Suggestion**: uma frase dizendo o que o EMPT mede sob racionamento.
**Severity**: Minor · **Confidence**: 5

## Perguntas aos autores
1. Qual será a data do tratamento: ano do termo validado, do primeiro repasse ou da execução?
2. Como serão classificados os 24 proponentes com projetos tratados e não tratados?
3. Quando a RAIS identificada permitirá medir um a três anos após as captações de 2024?

## Questões menores
- "análise de sensibilidade de Rambachan e Roth (2023) mostra quanto a conclusão resiste": ela mostra quanto de
  violação das tendências paralelas a conclusão tolera; ajustar a formulação.

## Julgamentos por critério
Calibration status: `NOT_CALIBRATED`

| Dimensão | Julgamento | Âncora | Racional | Decisivo? |
| --- | --- | --- | --- | --- |
| Rigor metodológico | PARTLY_MEETS | text: §5.3 "de 199 proponentes" | unidade, data do tratamento e controle "ainda não tratado" indefinidos | sim (reparável) |
| Suficiência de evidência | MEETS | table: Tabela 2 | poder transparente | não |
| Coerência do argumento | PARTLY_MEETS | text: §5.2 × §5.3 | parâmetro do proponente, poder em projetos | sim |
| Originalidade | NOT_ASSESSED | — | fora do foco | — |
| Qualidade da escrita | MEETS | — | — | não |
| Integração da literatura | MEETS | text: §5.2 | literatura de DiD escalonado citada | não |
| Significância e impacto | MEETS | — | desenho viável se a chave CNPJ for obtida | não |
