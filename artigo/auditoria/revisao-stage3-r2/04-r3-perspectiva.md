# Parecer do Revisor 3 (Perspectiva: governança de gastos tributários, transparência e ética)

## Informações
- **Rodada:** 2 · **Data:** 24/09/2026
- **Identidade:** especialista em governança de gastos tributários, transparência e ética em pesquisa com dados administrativos
- **Foco:** viabilidade de acesso aos dados, ética, recomendações de gestão, partes interessadas

## Avaliação geral
**Recomendação:** Minor Revision · **Confiança:** 4

**Resumo.** O enquadramento fiscal está correto e bem dimensionado: gasto tributário que não passa pelo lado da despesa,
equivalente a 14% a 21% do gasto direto na função cultura. As recomendações de gestão ficam dentro do escopo e têm base
legal. Três pontos merecem ajuste:
- a proposta depende de dados obtidos por LAI ou internos, sem dizer como obtê-los nem o que fazer se o pedido for
  negado;
- a frase sobre ética ("nenhum desenho nega ou adia o acesso") não combina com o desenho de H3 descrito pelo próprio
  texto;
- falta a recomendação mais direta da auditoria de H2b: publicar a fila de validação dos termos.

## Pontos fortes

### S1: Dimensão fiscal ancorada em fonte oficial
**Evidence Anchor:** `text: §1 "a renúncia efetiva equivale a 14% a 21% do gasto estadual direto na função cultura em 2022-2025 (SECULT, 2026c; BRASIL, 2026a)"`

A comparação com o gasto direto (SICONFI) dá ao leitor a ordem de grandeza certa.

### S2: Recomendações dentro do escopo e com base legal
**Evidence Anchor:** `text: §4.2 "A lei já manda o regulamento definir a divulgação dos benefícios, 'inclusive no Portal da Transparência do Estado'"`

As recomendações do §6 cumprem o que a própria lei já manda e não redesenham o mecanismo.

### S3: Ética e LGPD mencionadas
**Evidence Anchor:** `text: §5.5 "O uso de dados identificados exige anonimização, conforme a LGPD"`

## Fraquezas

### W1: Plano de acesso aos dados ausente
**Problem:** Das seis fontes do Quadro 4, três não são públicas:
- inscrições da SECULT, por LAI;
- datas de validação da SEFAZ, por LAI;
- relatórios de execução, internos.

Os resultados de H1b além da ocorrência (público, gratuidade) vêm da fonte interna, para a qual o texto não dá caminho
de acesso. Dados da SEFAZ sobre termos de patrocínio podem esbarrar no sigilo fiscal (CTN, art. 198). O texto não
diz:
- qual é a base legal do pedido;
- o que fazer se ele for negado;
- quanto tempo o pedido leva.

**Evidence Anchor:** `table: Quadro 4, coluna "Acesso" ("Pedido por LAI"; "Interno")`
**Why it matters:** a viabilidade da proposta depende desses pedidos. Um avaliador de política pública pergunta
primeiro pelo acesso.
**Suggestion:** uma ou duas frases na §5.3:
- **Base legal:** Lei 12.527/2011 (LAI). Para a SEFAZ, verificar se a exceção ao sigilo sobre benefícios tributários de
  pessoa jurídica, incluída no art. 198 do CTN pela Lei Complementar 187/2021, cobre os termos [conferir o texto da LC
  antes de citar]. Lembrar também que a SECULT já publica patrocinador e valor.
- **Alternativa se o pedido for negado:** ocorrência pelo Mapa Cultural e pelos extratos do Diário Oficial; público só
  com a cooperação da SECULT.
- **Prazo:** a LAI dá 20 dias, prorrogáveis por mais 10.
**Severity:** Minor · **Confidence:** 4 — Quadro 4; o alcance da LC 187/2021 precisa ser conferido

### W2: A frase sobre ética contradiz o desenho de H3
**Problem:** A §5.5 afirma que "nenhum desenho nega ou adia o acesso de elegíveis, e a oferta de apoio só acrescenta
informação". No desenho de H3, porém, dois efeitos contrariam a frase:
- os municípios de controle ficam sem o apoio durante o estudo;
- com o teto fixo, "novos entrantes deslocam outros" (§5.2). A oferta muda a chance de financiamento de quem não foi
  sorteado, ainda que de forma difusa.

**Evidence Anchor:** `text: §5.5 "nenhum desenho nega ou adia o acesso de elegíveis"`; `text: §5.2 "Como o teto é fixo, novos entrantes deslocam outros"`
**Why it matters:** a seção de ética é lida pelo que admite. Uma frase absoluta, contradita três parágrafos antes,
enfraquece o resto.
**Suggestion:**
- oferecer o apoio aos municípios de controle depois do acompanhamento, em implementação gradual (Gertler *et al.*,
  2018, já citado);
- reconhecer o deslocamento como custo para terceiros, que o desenho de saturação mede;
- dizer que o contato com agentes usa dados do Mapa Cultural sob base legal da LGPD para execução de política pública,
  e por isso a oferta deve ser feita pela SECULT, não pelos pesquisadores.
**Severity:** Minor · **Confidence:** 4 — texto do manuscrito

### W3: Falta a recomendação que decorre de H2b
**Problem:** A auditoria conclui que o excesso de demanda foi racionado pela ordem de validação dos termos. Entre as
recomendações de gestão, porém, não está publicar a fila: a data de protocolo e de validação de cada termo, inclusive
os indeferidos. É medida de transparência, dentro do escopo, que também produziria o dado de H1b.
**Evidence Anchor:** `text: §6 "publicar os inscritos e os motivos de inabilitação; publicar, por projeto, o CNPJ do proponente, a sede, a captação por cota e as datas"`
**Why it matters:** as recomendações devem sair dos achados, e o achado mais novo do artigo (H2b) não gera recomendação.
**Suggestion:** acrescentar "e a fila de validação dos termos, com data de protocolo e de validação, inclusive dos
indeferidos". Pode trocar "as datas", que é genérico.
**Severity:** Minor · **Confidence:** 5 — texto do manuscrito

## Observações (não são defeitos)
- **Municípios e plateia.** Os municípios aparecem no diagnóstico (MUNIC: fundos e planos municipais) e somem da teoria
  da mudança. No desenho de H3 por município, as secretarias municipais de cultura poderiam ser parceiras na oferta, o
  que ajuda na viabilidade e na aceitação. O público, beneficiário final, não tem indicador próprio. O texto reconhece
  isso como elo sem dado.
- O repositório público guarda só agregados. Vale dizer na §5.5 que os microdados identificados obtidos por LAI não
  serão publicados, como já prevê a regra do projeto.
