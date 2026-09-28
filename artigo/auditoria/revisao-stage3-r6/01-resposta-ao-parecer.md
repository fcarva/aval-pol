# Resposta ao parecer externo de 27/09/2026 (revisão r6, Fase B)

- **Parecer:** `feedback-avalia-o-do-desenho-da-lei-de-incentivo-cultura-ca-2026-09-28.md` (enviado pelo autor).
- **Decisões do autor (28/09/2026):**
  - a §5 segue o desenho de outra sessão dele: uma pergunta, "a renúncia vai para os projetos que dependem dela?",
    na decomposição de Foguel (2017), com os grupos que a regra atual já produz;
  - aplicam-se os pontos do parecer fora da §5: etapas da captação e H1;
  - corrigem-se tipos e concordância nas frases dele;
  - nenhum piloto nem regra futura no texto.

| Ponto do parecer | Onde | O que mudou | Checagem |
| --- | --- | --- | --- |
| Geral: padrão normativo de "valor público"; o experimento conjunto não mede benefício perdido | §5 | O experimento conjunto saiu. A pergunta passa a ser positiva (*V* = E₁₀ − E₀₀: o mecanismo prefere o que ocorreria de todo modo?) e dispensa um padrão normativo de preferência | — |
| Geral: H1 "não sustentada" vai além da evidência | Quadro 2, §4.2 | H1 passa a "Indeterminada: marca e valor público não se separam no dado público"; o enunciado da premissa não muda | — |
| Etapas: "esgotou o teto" contando um termo "em análise" | §1 | A captação esgotou o teto "em três registros distintos": anexo, Portal e renúncia realizada coincidem com o montante em 2023-2025. O termo em análise de 2025 está no Portal e teve depósito publicado no DIO | N87; `analise/21_etapas_captacao.py` |
| Etapas: exclusão por ordem de chegada sem as horas de protocolo | §4.2 (H2) | "pela regra da ordem de chegada e validação […], cuja aplicação só as horas de protocolo dos recusados, não publicadas, permitiriam conferir"; o teste da fila entra na §5.2 como condição a conferir por LAI | — |
| H2: a nota cega não corresponde à decisão real | §5 | A nota cega saiu. O filtro da CAP passa a ser medido por um resultado observável (realização sem a LICC): expirados × 86 inabilitados | N80, N94 |
| H3: 13% é teto legal; bunching; grupos do DiD | §5.1 | H3 sai do contrafactual: pergunta normativa, respondida pela auditoria das despesas **executadas** (LAI). O DiD da regra de 2026 saiu | — |
| H4: competição e mudanças de regra confundidas; população elegível (pessoas físicas) | §5 | O DiD por porte e o sorteio entre 71 municípios saíram. A queda da captação dos pequenos (79% → 27%, maiores 90% → 73%) virou só motivação para estimar *V* por faixa | N89; `analise/23_secao5_poder.py` |
| H5 (1): resultado não observado para recusados | §5.3 | *Y* vem de pesquisa de acompanhamento em todos os grupos, conferida em registros independentes. Fase A: fora da LICC, só 2 dos 32 recusados têm registro público do projeto | N88; `analise/22_recusados_outras_fontes.py` |
| H5 (2): o instrumento altera o momento da entrega | §5.2 | Sem instrumento. O efeito na margem é o de "receber agora", que já inclui o financiamento que o recusado obtém depois | — |
| H5 (3): as recusas de 2024 não formam um sorteio | §5.2 | A inferência por aleatorização saiu. A comparação 27 × 20 fica secundária, "sob a condição, a conferir com as datas, de que a conversão tenha seguido a ordem da fila" | N90, N82 |
| H5 (5): poder de RD × comparação balanceada | §5.4 | Sem RD. Os contrastes são entre grupos independentes, com a fórmula de proporções que corresponde a eles (Djimeu e Houndolo, 2016): *V* de 26 a 29 pontos hoje; de 16 a 17 com mais quatro ciclos | N92-N100 |
| H5 (7): equivalência com o EMD como margem | §5.1, Quadro 3, §6 | Sem teste de equivalência. A regra é rejeitar a ausência de seleção (*V* = 0). A conclusão sobre adicionalidade é condicional a *V* > 0 e maior nos grandes | — |

## Também aplicado nesta rodada

- **Fase A:**
  - a avaliação oficial (IJSN/FAPES, multiplicador de 1,74) entra na §3; a §6 não diz mais "sem previsão de
    avaliação";
  - "sem meta nem indicador" (§4.2) ganha a fonte do PPA (ESPÍRITO SANTO, 2026b);
  - Teixeira *et al.* (2021) passam a "correlacionais".
- **Edições do autor no `.tex`,** portadas ao `.md` palavra por palavra, com tipos e concordância corrigidos. A última
  frase do resumo, que ele editou, citava desenhos que saíram e foi reescrita para o novo desenho.
- **Referências:**
  - entram Foguel (2017) e IJSN (2026);
  - saem Angrist, Imbens e Rubin (1996), Baird *et al.* (2018), Eldridge, Ashby e Kerry (2006), Hainmueller, Hopkins
    e Yamamoto (2014) e Maestas, Mullen e Strand (2013), que ficaram sem citação.
- **Conferido depois (28/09):** a lista dos modos de racionar (ordem de chegada, características observadas, características não observadas, sorteio) está em Gertler *et al.* (2018), na **p. 74**, e não na p. 75 do rascunho herdado. A citação foi corrigida. Fonte: `dados/fontes_web/paginas/gertler_2018_pt.txt` (relé, pedido `gertler_2018_pt`), entre os cabeçalhos das páginas 74 e 75.
- **Versão final (28/09, pedido do autor):**
  - **Sai da §5.3 a frase "só 2 dos 32 recusados têm registro público do projeto".** A contagem confere (1 PRONAC de mesmo
    título e 1 evento datado no Mapa, `analise/tabelas/22_recusados_outras_fontes.csv`), mas ela mede a busca, não a
    existência de registro: Funcultura e PNAB ficaram fora, o SALIC vai até os PRONACs de 2025 e o Mapa só cobre projetos
    com processo ligado a evento. A própria tabela diz "sem registro observado; não quer dizer que não ocorreu". A frase
    feria a regra 1 (ausência não é zero). A checagem N88 sai.
  - **A última frase da conclusão foi refeita.** O texto anterior tirava "ampliar o teto financia sobretudo o que ocorreria
    de todo modo" de *V* > 0. Pelo Quadro 3, essa é a leitura do EMPT na margem próximo de zero (H5); *V* > 0 e maior nos
    pedidos grandes quer dizer "a renúncia vai a quem menos depende dela". O texto novo separa as duas condições. Troca
    também "as decisões que importam passam a ser quem entra e o que se entrega" por "o valor público da LICC passa a
    depender menos do tamanho do teto que da regra que define quais projetos recebem a renúncia e do que se exige e se
    verifica na entrega". Nova checagem N103: a captação dos pedidos até R$ 400 mil caiu a cada ciclo (79%, 59%, 27%).
  - **Diagramação:** as larguras das colunas dos Quadros 1, 3 e 4 e das Tabelas 1 e 2 foram redistribuídas, sem mudar o
    texto. As referências continuam separadas por meia linha: a linha inteira da NBR 6023 foi testada e passa de 15
    páginas.
