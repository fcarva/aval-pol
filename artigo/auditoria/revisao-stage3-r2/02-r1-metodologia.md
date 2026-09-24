# Parecer do Revisor 1 (Metodologia)

## Informações
- **Rodada:** 2 · **Data:** 24/09/2026
- **Identidade:** economista de avaliação de impacto (resultados potenciais, experimentos naturais em filas e
  racionamento, desenhos com encorajamento, poder com conglomerados)
- **Foco:** parâmetros, vieses, identificação, amostra e poder

## Avaliação geral
**Recomendação:** Major Revision · **Confiança:** 5

**Resumo.** A seção 5 faz o que a disciplina pede e na ordem certa:
- parte das premissas;
- escreve as perguntas em resultados potenciais;
- deriva o método das regras de operação;
- define a amostra;
- calcula o poder com efeito de desenho.

A exclusão da regressão descontínua, depois da auditoria do parecer, está correta. O tratamento da interferência pelo
teto fixo, com saturação aleatória, é sofisticado para o gênero.

Quatro problemas, porém, atingem justamente as duas perguntas centrais (H1b e H3):
- o sinal de um viés está trocado no Quadro 3;
- o grupo de comparação do racionamento recebe o tratamento um ano depois;
- a "ordem de chegada" é uma inferência, não uma regra documentada;
- as diferenças em diferenças não estão definidas na unidade escolhida.

Há ainda o poder de H3, apoiado em um cadastro que não foi contado. Tudo se corrige sem mudar a estrutura, mas as
correções mudam o que a proposta diz que consegue estimar.

## Pontos fortes

### S1: Método derivado das regras de operação
**Evidence Anchor:** `text: §5.2 "As regras de operação determinam o método (GERTLER et al., 2018)"`

A lista de métodos cabíveis segue a tabela de Gertler *et al.* para excesso de demanda sem índice. A exclusão da
regressão descontínua ("Como o parecer não atribui nota, não há ponto de corte") decorre da auditoria do modelo de
parecer, não de preferência.

### S2: Interferência pelo teto tratada no desenho
**Evidence Anchor:** `text: §5.2 "sortear também a intensidade da oferta entre municípios mede esse deslocamento (BAIRD et al., 2018)"`

O artigo reconhece que, com teto fixo, um novo entrante desloca outro (§5.5, SUTVA), e propõe o desenho de saturação que
mede o deslocamento em vez de ignorá-lo.

### S3: Poder transparente
**Evidence Anchor:** `equation: §5.4 EMD com efeito de desenho (cv² + 1) m̄`; `text: §5.4 "o que recomenda pré-registrar o plano de análise"`

A fórmula é a do material da disciplina e inclui a variação no tamanho dos grupos. Os cenários estão em tabela
versionada, e o risco de erro tipo M (Gelman e Carlin) é dito.

## Fraquezas

### W1: O sinal do viés de H1b está trocado no Quadro 3
**Problem:** O Quadro 3 diz, para H1b: "Se a empresa escolhe eventos consolidados, *Y*(0) é maior entre os escolhidos e
o efeito é menor onde ela escolhe: os dois vieses subestimam a adicionalidade." Na decomposição que o próprio texto
anuncia na §5.1 (diferença simples = efeito médio + viés de seleção + viés de efeitos heterogêneos), os dois vieses
agem em sentidos opostos:
- **Viés de seleção.** *Y*(0) maior entre os tratados torna o viés de seleção, E[*Y*(0) | *T* = 1] − E[*Y*(0) | *T* = 0],
  **positivo**. A comparação simples **superestima** o EMPT, que é o parâmetro escolhido.
- **Viés de efeitos heterogêneos.** Efeito menor entre os escolhidos (EMPT < EMPNT) faz o termo (1 − π)(EMPT − EMPNT)
  ser negativo. Em relação ao efeito médio, esse termo age no sentido oposto ao do viés de seleção.

**Evidence Anchor:** `table: Quadro 3, linha H1b, coluna "Viés da comparação simples"`
**Why it matters:** é o conteúdo central de resultados potenciais da disciplina, e o erro está na pergunta mais
importante do artigo. Um avaliador da disciplina vai notar.
**Suggestion:** "*Y*(0) é maior entre os escolhidos: o viés de seleção é positivo, e a comparação simples superestima o
EMPT. Se o efeito também for menor onde a empresa escolhe, o viés de efeitos heterogêneos puxa a comparação para baixo
em relação ao efeito médio."
**Severity:** Major · **Confidence:** 5 — álgebra da decomposição da §5.1

### W2: No racionamento, o grupo de comparação recebe o tratamento um ano depois
**Problem:** A §5.2 chama de "quase experimental" a comparação entre termos validados pouco antes do esgotamento do teto
e termos indeferidos. Conferi os 11 projetos com termo indeferido em 2023 no anexo de captação de 2024. **Sete aparecem
entre os que captaram em 2024**:
- CineMarias;
- Roda de Boteco;
- Ready to Rock;
- Museu das Tartarugas Marinhas;
- residência literária no Caparaó;
- BRAVOS;
- Coral ArcelorMittal.

Os outros quatro não aparecem em 2024, 2025 nem 2026. A conferência foi por título do projeto, e parte dos casos pode
ser outra edição do mesmo projeto. O indeferimento, portanto, em geral adiou o financiamento em vez de negá-lo.

Além disso, o tamanho da margem é conhecido: 11 termos indeferidos em 2023 e 22 em 2024 (`03f_captacao_anual_secult.csv`).
A Tabela 2, porém, usa "20 a 30 projetos por grupo", que `07_poder_hipoteses.csv` registra como "n por braço
hipotético", sem que o texto diga isso.
**Evidence Anchor:** `dataset: artigo/auditoria/revisao-stage3-r2/evidencia-reentrada-indeferidos-2023.csv (a partir de dados/fontes_web/paginas/secult_captados_2023_pdf.txt e secult_captados_2024_pdf.txt)`
**Why it matters:**
- Com reentrada de cerca de 64%, a comparação estima o efeito de **receber agora em vez de no ano seguinte**, e não o de
  receber em vez de não receber, que é a adicionalidade.
- Com *Y* = "o bem cultural acontece", sem janela de tempo, o efeito tende a zero por construção.

**Suggestion:**
- (i) Definir o resultado com janela: realizado no ano previsto, ou realizado em até 12 meses.
- (ii) Tratar o indeferimento como instrumento para o financiamento no ano *t* e relatar a reentrada como primeiro
  estágio.
- (iii) Ancorar o poder nos 33 termos observados (11 + 22), recalculando o EMD, e dizer que o número de projetos é menor
  ou igual a 33.
- (iv) Repetir a conferência para os 22 termos indeferidos em 2024 no anexo de 2025
  (`secult_captados_2025_v17_pdf.txt`).
**Severity:** Major · **Confidence:** 4 — conferência por título nos anexos oficiais; edição do projeto não conferida

### W3: "Ordem de chegada" é inferência; o documentado é "indeferidos por ultrapassar o montante"
**Problem:** A §4.2 afirma que o excesso de demanda "foi racionado pela ordem de chegada dos termos" (e o Quadro 2 diz
"pela ordem de chegada"). O anexo oficial diz outra coisa: "Termos de compromisso de patrocínio indeferidos por
ultrapassar o montante de recursos financeiros disponíveis". A IN de 2024 (art. 35, § 2º) exige que os termos sejam
validados pela SEFAZ, mas nenhuma norma lida fixa a ordem de validação. O que os dados mostram é que ficou de fora quem
foi validado depois do esgotamento.

A ordem de validação pode depender de fatores ligados ao projeto:
- da data escolhida pela empresa para assinar, como no planejamento tributário de fim de ano (o anexo de 2023 é de
  20/11/2023);
- da completude da documentação;
- do tempo de análise da SEFAZ.

**Evidence Anchor:** `text: §4.2 "racionado pela ordem de chegada dos termos, não por mérito (SECULT, 2026c)"`; `dataset: dados/fontes_web/paginas/secult_captados_2023_pdf.txt, título da lista de indeferidos`
**Why it matters:** o caráter "quase experimental" de H1b depende de a ordem não se ligar ao projeto. A regra 3 do
projeto ("li a norma ≠ consigo apurar") pede que o texto diga o que foi observado, e não o mecanismo presumido.
**Suggestion:**
- trocar por "ordem de validação" no resumo, no Quadro 2, na §4.2, na §6 e na figura;
- na §5.2, listar as ameaças à hipótese de ordem "como se aleatória";
- manter o pedido da data de protocolo e da data de validação (Quadro 4, SEFAZ). Com as duas datas é possível testar se
  a ordem se liga ao porte da empresa ou do projeto.
**Severity:** Major · **Confidence:** 5 — anexo de 2023, IN 2024 e notas de desenho legal

### W4: As diferenças em diferenças não estão definidas na unidade escolhida
**Problem:** Para H1b, a unidade é o "projeto habilitado" e *Y* = "o bem cultural acontece" (Quadro 3). A §5.2 propõe
comparar captou × expirou "com diferenças em diferenças e pareamento dentro do ciclo (o desenho de Colombo e Cruz,
2023)". Um projeto acontece uma vez e não tem período anterior, então não existe diferença em diferenças no nível do
projeto. Colombo e Cruz usam um painel de empresas (PINTEC 2008 e 2011).
**Evidence Anchor:** `text: §5.2 "comparados aos que captaram com diferenças em diferenças e pareamento dentro do ciclo"`; `table: Quadro 3, linha H1b, "Projeto habilitado; T = captou; Y = o bem cultural acontece"`
**Why it matters:** como está, o método citado não se aplica ao dado descrito. O leitor não sabe qual parâmetro essa
comparação estima nem com quais dados.
**Suggestion:** escolher uma de duas opções:
- **(a) Proponente-ano como unidade.** Tratamento = primeira captação; resultados observáveis antes e depois, como
  eventos na agenda do Mapa Cultural, projetos no SALIC e, se houver convênio, vínculos formais. Nesse caso, ajustar a
  Tabela 2 à nova unidade.
- **(b) Manter o projeto como unidade.** Chamar a estratégia de pareamento (ou regressão) sob seleção nos observáveis,
  com análise de sensibilidade, e retirar as "diferenças em diferenças".
**Severity:** Major · **Confidence:** 5 — definição do estimador de diferenças em diferenças

### W5: O poder de H3 não se apoia no cadastro, que não foi contado
**Problem:** A Tabela 2 dá, para H3, "1.000 a 4.000 agentes" e "71 municípios do interior, 20 a 50 agentes cada", e a
§5.4 conclui que "o desenho de H3 detecta efeitos de poucos pontos". A tabela de origem registra "N e p0 hipotéticos até
contar os agentes do Mapa Cultural" e "m agentes por município hipotético".

O único cadastro contado é o da Tabela 1: 25.441 agentes, dos quais 2.592 coletivos, no estado todo. A listagem proposta
(com CNPJ, sem inscrição anterior, no interior) não foi contada nem por município. O cenário por município supõe de
1.420 a 3.550 agentes elegíveis só no interior. Supõe também tamanho igual entre municípios (sem *cv*), quando a fórmula
da §5.4 tem esse termo justamente porque municípios pequenos terão poucos agentes.
**Evidence Anchor:** `table: Tabela 2, linhas H3`; `dataset: analise/tabelas/07_poder_hipoteses.csv, coluna nota`
**Why it matters:** o poder é item exigido pela disciplina, e a conclusão "detecta efeitos de poucos pontos" depende do
tamanho do cadastro.
**Suggestion:**
- contar, pela API do Mapa Cultural (com o relé), os agentes por tipo e por município do interior e, se o campo existir,
  os que têm CNPJ;
- recalcular com *J* = número de municípios com agentes e com o *cv* observado;
- se não houver tempo, dizer no texto que *N* e *m* são hipotéticos e dar o cadastro mínimo necessário para um EMD de
  5 pontos.
**Severity:** Major · **Confidence:** 4 — tabelas do repositório; o tamanho real do cadastro é desconhecido

### W6: O Quadro 3 mantém um parâmetro causal para H2a, que a §5.2 declara descritiva
**Problem:** A linha H2a traz "Efeito de ser habilitado (oferta) na margem da decisão" e compara inabilitados com
habilitados. A §5.2 diz que "a pergunta fica descritiva: se a captação se associa ao que o parecer registrou". A pergunta
do quadro junta duas perguntas ("A habilitação muda o destino do projeto, e a empresa segue o mérito avaliado pela
SECULT?").
**Evidence Anchor:** `table: Quadro 3, linha H2a`; `text: §5.2 "A pergunta fica descritiva"`
**Why it matters:** incoerência interna entre o quadro e o texto. O parâmetro do quadro não tem estratégia de
identificação no artigo.
**Suggestion:** reescrever a linha:
- **pergunta:** "A captação acompanha o que o parecer registrou?";
- **unidade:** projeto habilitado; ***T*:** critérios atendidos e diligências; ***Y*:** captou;
- **parâmetro:** associação condicional (descritiva);
- **viés:** o parecer não é aleatório nem pontuado.
**Severity:** Minor · **Confidence:** 5 — texto do manuscrito

### W7: Um fato quantitativo sem número
**Problem:** "Projetos que pediram exatamente o teto de R\$ 500 mil foram executados com mais frequência que os
menores" não dá magnitude. Em 2022-2024, foram 83% dos que pediram exatamente R\$ 500 mil (49 de 59), contra 52% dos que
pediram até R\$ 200 mil (27 de 52) (`03_status_conversao_por_faixa_valor_2022_2024.csv`). "Executado" é o status "em
execução" ou "execução finalizada", isto é, captou pelo menos 50%.
**Evidence Anchor:** `text: §4.2 "foram executados com mais frequência que os menores"`
**Why it matters:** a regra 2 do projeto (proveniência em todo número) vale também para comparações; e o tamanho da
diferença pesa na discussão de H1a.
**Suggestion:** "83% contra 52% dos que pediram até R\$ 200 mil (2022-2024)".
**Severity:** Minor · **Confidence:** 5 — tabela de origem

### W8: "Sorteio" aparece como método cabível sem a ressalva do escopo
**Problem:** A §5.2 diz que "cabem sorteio, promoção aleatória, diferenças em diferenças…". Sortear entre habilitados
mudaria a regra de alocação, o que está fora do escopo declarado ("sem propor redesenho").
**Evidence Anchor:** `text: §5.2 "cabem sorteio, promoção aleatória"`
**Why it matters:** o texto parece propor o que a introdução exclui.
**Suggestion:** "o sorteio, que mudaria a regra de alocação, fica fora do escopo; o racionamento pela ordem de validação
é o seu análogo natural".
**Severity:** Minor · **Confidence:** 4 — escopo declarado na §1

## Perguntas aos autores
1. Os 22 projetos com termo indeferido em 2024 captaram em 2025? A reentrada muda a leitura de H1b.
2. A SEFAZ registra a data de protocolo do termo, além da data de validação?
3. Em H3, o tratamento endógeno do efeito local é "usar o apoio" ou "inscrever-se"? A exclusão (a oferta só age pelo
   apoio) precisa ser dita.
