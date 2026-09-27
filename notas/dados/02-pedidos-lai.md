# Pedidos de acesso à informação (LAI): o que só a SECULT e a SEFAZ têm

Rota para o que não está publicado em lugar nenhum. Já foram tentados: anexos, extratos da CAP, aviso no DIO, API
pública do Mapa Cultural, versões antigas dos arquivos e Wayback Machine (ver
`notas/politica/04-atas-e-reunioes-publicas.md` e `analise/13_versoes_anexos.py`). Os pedidos vão pelo portal de
acesso à informação do Governo do ES (https://acessoainformacao.es.gov.br/, link que aparece nas páginas da SECULT),
com base na Lei nº 12.527/2011 (LAI). Formato pedido: planilha (CSV ou XLSX). Dados pessoais podem vir pseudonimizados
(LGPD); o que interessa é a estrutura, não o nome.

## Pedido 1: SECULT, inscrições e decisões da LICC (2022-2026)

Para cada inscrição na LICC (oportunidades do Mapa Cultural 265, 479, 1415, 1878 e 2317, e fases Parecerista, CAP e
Publicação final):
1. número da inscrição e do processo (E-Docs), data de envio;
2. linha de financiamento (IN, art. 9º, I a VI) e área ou segmento cultural;
3. município da sede do proponente e municípios de execução; natureza jurídica (associação, empresa, MEI);
4. valor solicitado e valor habilitado;
5. identificador pseudonimizado do parecerista designado e data da designação;
6. resultado do parecer, critério a critério ("atende ou não"), e data;
7. data e resultado da deliberação da CAP (habilitado, em diligência, inabilitado, não avaliado) e **motivo da
   inabilitação**;
8. situação final (captando, em execução, concluído, expirado, arquivado).

Uso no artigo: H2 (severidade do parecerista, decisão da CAP), H4 (quem entra), linha de fomento.

## Pedido 2: SECULT, custos e entrega dos projetos executados

Para cada projeto com captação validada:
1. planilha de custos aprovada e executada, com as rubricas de captação, elaboração, divulgação, remuneração do
   proponente e equipe técnica;
2. do relatório de execução (IN 001/2025, art. 66): público estimado, número de pessoas na lista de presença
   (agregado), ações gratuitas, municípios e datas de realização, contrapartidas cumpridas;
3. situação da prestação de contas (aprovada, com ressalva, reprovada) e data.

Uso no artigo: H3 (custo de intermediação) e H5 (entrega verificável).

## Pedido 3: SECULT, atas completas da CAP

Íntegra das atas das reuniões da CAP de 2022 a 2026, e não só os extratos publicados. Motivo: os extratos não trazem
motivo nem critério da inabilitação, nem o resultado dos recursos.

## Pedido 4: SEFAZ, fila dos termos de compromisso de patrocínio (2022-2026)

Para cada termo de compromisso:
1. data e hora de protocolo e de validação;
2. valor;
3. identificador pseudonimizado do patrocinador e faixa do limite (20%, 15%, 10% ou 5% do ICMS; sem o valor do imposto,
   por causa do sigilo fiscal);
4. cota do art. 18 em que foi validado;
5. situação (validado, indeferido por ultrapassar o montante, em análise) e processo do projeto.

Uso no artigo: H5 (RD no tempo em torno do esgotamento de cada cota) e H2 (a ordem da fila).

## Observações

- O prazo da LAI é de 20 dias, prorrogáveis por mais 10: não chega antes da entrega de 28/09/2026. É material da 2ª
  parte da disciplina, e o Quadro 4 do artigo já anuncia os pedidos.
- Enquanto a resposta não vem, as versões antigas dos anexos de captação (`13_versoes_captados*.csv`) aproximam a
  fila da SEFAZ com dado público.
