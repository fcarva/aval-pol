# Atas de julgamento, teto por projeto, linhas de fomento e reuniões públicas (27/09/2026)

Pedidos do autor: "procure por atas de julgamento"; "ver o teto de cada projeto financiado por ano para determinar o
número de projetos" e "por linha de fomento, para detalhar escopos e a separação de proponentes"; "procure por
reuniões públicas no YouTube e olhe a transcrição".

Regras que valem aqui: ausência não é zero; todo número tem arquivo e script; o que a fonte não permite apurar fica
"indeterminado". As tabelas derivadas não trazem nomes de pessoas físicas. O texto das páginas oficiais fica em
`dados/fontes_web/paginas/` com CPF mascarado, como os demais anexos.

## 1. Atas da CAP da LICC (extratos)

- A SECULT publica o **extrato da ata** de cada reunião da Comissão de Avaliação Permanente. Base normativa: IN 2024,
  art. 32, § 3º ("Os extratos das atas das reuniões da CAP serão publicados na página eletrônica da Secretaria"), e
  Regimento da CAP (`notas/politica/fontes/regimento-interno-cap-2023.md`).
- Índices por ano (coletados pelo relé, etapa `seguir`, prefixos `cap2022` a `cap2026`; lista em
  `dados/fontes_web/seguir/`):

  | Ano | Página | Observação |
  | --- | --- | --- |
  | 2022 | https://secult.es.gov.br/GrupodeArquivos/comissao-de-avaliacao-de-projetos-cap | |
  | 2023 | https://secult.es.gov.br/comissao-de-avaliacao-permanente-cap-2023 | até a 37ª reunião |
  | 2024 | https://secult.es.gov.br/cap-2024 | até a 32ª reunião (07/11/2024) |
  | 2025 | https://secult.es.gov.br/cap-2025 | 29 reuniões (até 18/12/2025) e calendário |
  | 2026 | https://secult.es.gov.br/cap-2026 | 24 reuniões até 03/09/2026 e calendário |

- Cada extrato lista, por processo, projeto e proponente, os **habilitados**, os **em diligência**, os
  **inabilitados** e (em 2026) os **não avaliados**.
- Exemplos lidos na web:
  - 4ª reunião de 2023: nenhum habilitado, 3 em diligência, 3 inabilitados;
  - 13ª reunião de 2026 (07/05/2026): 4 habilitados, 2 inabilitados, 2 não avaliados.
- **O extrato não traz motivo nem critério** da inabilitação: o motivo fica indeterminado (regra 3).
- Por que importa:
  - a lista oficial de habilitados não traz os inabilitados, e os extratos trazem;
  - também trazem a **data da habilitação** de cada projeto. Com ela, o RD no tempo de H5 e a severidade do
    parecerista de H2 ganham dado público; a fila da SEFAZ continua pedida por LAI.
- Tabulação: `analise/12_atas_cap.py` → `analise/tabelas/12_cap_*.csv`. Resultado (relé de 27/09/2026, 165 links, todos
  com status 200):
  - 160 extratos lidos: 158 reuniões com deliberação, de 16/03/2022 a 24/09/2026, e **2 reuniões sem quórum**
    (23/06/2022 e 26/02/2026). Os outros 5 links são calendários e uma portaria de designação;
  - **86 projetos inabilitados** (81 nunca habilitados depois; 5 habilitados em outra reunião), **15% dos
    deliberados** (habilitados ∪ inabilitados); por ano, de 11% (2022) a 17% (2023 e 2025);
  - "não avaliados" (pauta não apreciada): 43 em 2024, 38 em 2025 e 52 em 2026;
  - 5 recursos contra inabilitação apreciados em 2023, sem o resultado no extrato;
  - **cobertura**: de 94% (ciclo 2023) a 99% (2024 e 2026) dos habilitados da lista oficial aparecem habilitados em
    algum extrato, o que valida os extratos como fonte do universo deliberado;
  - natureza inferida nas linhas de deliberação de inabilitados: 35 empresas com sufixo societário, 27 associações,
    8 MEI ou pessoa física. Inabilitados sobre habilitados + inabilitados, por natureza: de 7% ("empresa provável")
    a 19% (MEI), com associações em 13% e empresas com sufixo em 17%. São contagens de linhas, não de processos
    distintos, e sem padrão claro;
  - a data da reunião de habilitação de cada processo está em `12_cap_deliberacoes.csv` (insumo de H5 e H2).
- No artigo (§4.2, H2): "Os extratos das atas de 158 reuniões com deliberação, de 2022 a 2026, listam 86 projetos
  inabilitados, 15% dos deliberados, sem motivo nem critério publicados (SECULT, 2026g)" (checagem N60).
- A página `https://secult.es.gov.br/atas` é do **Conselho Estadual de Cultura** (CEC), não da CAP.

## 2. Ata do Funcultura, edital 29/2025 (curtas e médias-metragens): contraste de seleção

Documento fornecido pelo autor: "Ata de julgamento de recursos e resultado final da etapa de pré-seleção de
projetos", Processo 2025-KPM2C, homologada em 04/08/2026. URL oficial achada pelo relé na página `edital-2025`:
https://secult.es.gov.br/media/ata-de-julgamento-de-recursos-pre-selecao-29-2025.pdf. O sha256 é idêntico ao do PDF
anexado (`ff88cfc7…`). A mesma página traz o edital 29/2025, a ata da pré-seleção, a da defesa oral e a de recursos pós-defesa
(`dados/fontes_web/seguir/fun2025e.tsv`). Resumo agregado em:
- `analise/tabelas/11_funcultura_29_2025_resumo.csv`;
- `analise/tabelas/11_funcultura_29_2025_recursos.csv` (script `analise/11_teto_projeto_e_linhas.py`, opção
  `--ata-pdf`).

**Como a mesma SECULT seleciona no Funcultura:**
- **nota** de 0 a 100 e ranking dentro de cada célula (linha × faixa de município);
- **4 linhas**: ficção, documentário, animação e diretor estreante;
- **2 faixas**: municípios com mais de 150 mil habitantes e com menos;
- situações: classificado para a seleção, não pré-selecionado e desclassificado. Há desclassificados com nota entre
  50 e 58, e não só com 0, o que sugere nota mínima;
- a legenda marca **pessoa negra, indígena e com deficiência**. Na Linha 1, faixa acima de 150 mil, um classificado
  com 86,00 fica à frente de não pré-selecionados com 92,00, compatível com vaga reservada ou induzida (a conferir no
  edital);
- 136 inscrições no anexo, todas lidas pelo script.

**Recursos:**

| Decisão | Recursos |
| --- | --- |
| Listados na ata | 25 |
| Deferidos, com nota corrigida | 2 |
| Deferidos em parte | 6 |
| Indeferidos | 16 |
| Fora do prazo | 1 |
| **Listados sem decisão na ata** | **1** (Linha 1; inconsistência da própria ata) |

**Contraste com a LICC:**
- Na LICC o parecer é "atende ou não", sem nota (modelos de 2022 e 2026; Mapa com método `simple`).
- A CAP habilita ou não, e entre os habilitados decidem a empresa e a fila dos termos. Não há faixa por porte de
  município, nem linha com reserva, nem marca de grupo.
- É variação dentro da mesma secretaria, com o mesmo cadastro (Mapa Cultural). Candidata, na 2ª parte da disciplina, a
  comparar quem entra e quem é financiado sob seleção por nota e sob escolha da empresa, sem estimar agora.
- No artigo (§4.2, H2): "no Funcultura, a SECULT dá nota e ordena os projetos por linha e porte do município (SECULT,
  2026h)", no lugar da citação ao IJSN (2021).

## 3. Teto por projeto por ano e número mínimo de projetos

Tabela `analise/tabelas/11_teto_projeto_por_ano.csv`:

| Ano | Regra do teto por projeto | Fonte | Montante | Mínimo de projetos (todos no teto) | Captaram | Pedidos exatamente em R\$ 500 mil |
| --- | --- | --- | --- | --- | --- | --- |
| 2022 | 5% do montante; 10% para obra em patrimônio | IN 002/2022, arts. 8º e 9º (conferido; relé) e live de 19/04/2022 | R\$ 15 mi no anexo (portaria: 10 mi) | 20 | 39 | 13% |
| 2023 | idem | IN 2023, arts. 8º e 9º (conferido) | R\$ 15 mi | 20 | 49 | 21% |
| 2024 | R\$ 500 mil; R\$ 1 mi para obra em patrimônio e longa | IN 2024, arts. 8º a 10 (conferido) | R\$ 25 mi | 50 | 72 | 25% |
| 2025 | idem; R\$ 300 mil em 1ª edição; até 3 projetos por agente | IN 2025, arts. 13 a 16 (conferido) | R\$ 25 mi | 50 | 63 (62 validados) | 36% |
| 2026 | idem | IN 2026, arts. 13 a 16 (conferido) | R\$ 31 mi | 62 | 103 (ano em curso) | 41% |

- Sob a regra dos 5%, o mínimo é sempre 20, qualquer que seja o montante. Com o valor fixo, o mínimo cresce com o
  montante.
- A razão teto/montante caiu de 5% para 1,6%: o desenho pulveriza por projeto, mas **não limita o valor por
  patrocinador** além da fração do ICMS (a concentração está no patrocinador, não no projeto).
- Os pedidos se acumulam no teto (13% → 41%), e quem tem patrocinador pede o teto. O projeto pequeno disputa o mesmo
  montante e a mesma fila (H4).
- Indeterminado: em 2023 o montante subiu de R\$ 10 mi para R\$ 15 mi. Não se sabe se o teto de 5% passou a
  R\$ 750 mil; os pedidos acumulam em R\$ 500 mil.
- Separação de proponentes ao longo do tempo:
  - em 2022, sem limite de projetos por CNPJ (live de 2022, cerca de 27 min);
  - desde 2025, até 3 por agente, somando CNPJs com o mesmo quadro societário (IN 2025, art. 13), e em 2026 com
    "sócios ou dirigentes em comum";
  - teto do MEI de 2 vezes o faturamento anual do MEI (art. 17);
  - optantes do Simples não patrocinam (LC 123/2006, art. 24; IN 2026, art. 40, § 3º).

## 4. Linha de fomento por projeto (inferida; não entra no artigo)

- A SECULT não publica a linha (art. 9º, I-VI) de cada projeto. Não aparece:
  - nos anexos;
  - no aviso de habilitação do DIO (`dados/fontes_web/paginas/secult_dio_aviso_2025_10_14.txt`, com título, processo,
    proponente, CNPJ e valores por ano);
  - na API pública do Mapa (`mapa_api_inscricoes_1878.txt` = `[]`).
- Inferência em `analise/tabelas/11_linhas_proxy_por_ciclo.csv`:
  - a linguagem vem do título, pelas regras de `06_alocacao_linguagens.py`, e é mapeada para a linha;
  - valor acima de R\$ 500 mil ⇒ V ou VI;
  - cota de plurianuais ⇒ III.
- Resultado 2022-2026 (463 processos):

  | Linha inferida | Projetos |
  | --- | --- |
  | Título não classifica | 158 (34%) |
  | I, linguagens artísticas | 146 |
  | IV, patrimônio imaterial e culturas tradicionais | 76 |
  | VI, audiovisual | 29 |
  | IV ou V (patrimônio) | 17 |
  | I ou III (formação) | 16 |
  | III, plurianuais (cota) | 14 |
  | V ou VI, acima do teto geral | 7 |

- A linha II (economia criativa: design, moda, gastronomia, jogos) não tem regra de título e não é identificável.
- Natureza do proponente por linha (a partir de `dados/processados/proponentes.csv`):
  - o audiovisual é sobretudo empresa: 21 de 29;
  - patrimônio imaterial e tradições, sobretudo associação: 55 de 76;
  - o MEI aparece quase só em linguagens artísticas (15) e em títulos não classificados (12).
- Para a linha verdadeira: pedido por LAI (Quadro 4 do artigo: "Inscrições da SECULT (Mapa Cultural) … com linha,
  área, parecerista").

## 5. Reuniões públicas no YouTube

**Acesso.** Nesta sessão o YouTube está bloqueado (403). O relé tenta as legendas em português com `yt-dlp` (etapa
`videos`, lista em `dados/fontes_web/videos.tsv`; saída em `dados/fontes_web/transcricoes/`) e lista os canais da
Secult ES e da TVE (etapa `canal`, saída em `dados/fontes_web/videos_canal.tsv`). O `web_fetch` do Parallel Search
devolveu a transcrição automática **traduzida para o inglês**, com tempos. As passagens abaixo são paráfrases dessa
tradução e **não servem para citação literal** até a legenda em português ser coletada.

**Vídeos localizados:**

| Vídeo | Canal e data | Tema |
| --- | --- | --- |
| [KvXStH6-Iy4](https://www.youtube.com/watch?v=KvXStH6-Iy4) | Secult ES, 19/04/2022, 58 min | Live Tira-Dúvidas da LICC |
| [p68POFJdp8Y](https://www.youtube.com/watch?v=p68POFJdp8Y) | Secult ES, 2022, 2h29 | Live de lançamento da LICC |
| [jUeXQurYnqU](https://www.youtube.com/watch?v=jUeXQurYnqU) | TVE ES, 02/02/2022, 2h29 | Live de lançamento (retransmissão) |
| [Xxx46zelBkU](https://www.youtube.com/watch?v=Xxx46zelBkU) | TVE ES, 2022, 57 min | Perguntas e respostas sobre a LICC |
| [eVWNz7Gw19o](https://www.youtube.com/watch?v=eVWNz7Gw19o) | — | "LICC visa dobrar o investimento em projetos culturais" |
| [i9q5QJpAfOo](https://www.youtube.com/watch?v=i9q5QJpAfOo) | — | LICC com o secretário de Cultura |
| [qoDuwiELdZI](https://www.youtube.com/watch?v=qoDuwiELdZI) | evento externo | "Reflexões sobre a nova LICC" (aspectos práticos e jurídicos) |
| [a3VjhSXbhMI](https://www.youtube.com/watch?v=a3VjhSXbhMI) | Secult ES | 37ª reunião extraordinária (Conselho Estadual de Cultura) |
| [L0PBukc4mb8](https://www.youtube.com/watch?v=L0PBukc4mb8) | — | "Secult lança editais de R\$ 34 milhões" (Funcultura) |

- Não localizados: a gravação do "Cultura em Dados" (01/07/2026, apresentação da avaliação IJSN da LICC, com
  multiplicador de 1,74 segundo a SECULT); a "live orienta contadores"; a 134ª reunião do CEC (apresentação da LICC).
  A notícia da 134ª reunião deu 404 no relé.

**Live Tira-Dúvidas (KvXStH6-Iy4), passagens ligadas às hipóteses** (paráfrase da tradução automática):

| Tempo | Conteúdo | Hipótese | Norma que confirma |
| --- | --- | --- | --- |
| ~7 min | Ao falar das empresas, a apresentação destaca "o impacto que o projeto pode trazer à marca"; "empresas" são todos os contribuintes de ICMS | H1: o próprio gestor vende a LICC às empresas pelo retorno de marca | — |
| ~9 min | O parecerista e a CAP avaliam pelos critérios do decreto: interesse público, qualidade da proposta e outros | H2 | Dec. 5.035-R, art. 14 |
| ~10 min | Depois da habilitação, o proponente procura empresas contribuintes e formaliza o termo; depósito em conta do projeto; execução com ao menos 50% captado | cadeia de financiamento | IN |
| ~27 min | Em 2022 não havia limite de projetos por CNPJ | separação de proponentes | até 3 por agente só desde 2025 |
| ~27-28 min | O limite de R\$ 10 mi é contado pelos termos de compromisso; atingido, a SECULT continua avaliando, mas não publica novas habilitações até haver recurso | H5 e H2 (fila) | Portaria 078/2024 e 062-S/2025 |
| ~42 min | A empresa patrocinadora pode ser de qualquer lugar do ES, desde que recolha ICMS | H1 | Dec., art. 2º |
| ~46 min | Teto de 5% do autorizado no ano (R\$ 500 mil, com R\$ 10 mi) para todas as linguagens e 10% (R\$ 1 mi) para patrimônio arquitetônico | teto | IN 2023, arts. 8º e 9º |
| ~55 min | Diferente dos editais, a LICC admite diligências na análise documental e na CAP | H2 | IN, diligências |

**O que é discurso e o que é norma.**
- O apelo à marca (H1) é discurso do gestor, não regra. A regra é a proporcionalidade das logomarcas com as do Governo
  (IN 2025, art. 55) e a divulgação até 25%.
- O teto de 5% e a fila por termos têm norma.

## 6. Outros achados para H1 (marketing)

- **Prêmio LICC 2024** (SECULT, notícia de 16/04/2024; lida pelo web_fetch, porque o relé recebeu 404):
  - o Governo premiou as seis empresas "que mais investiram": ES Gás, com mais de R\$ 11,2 mi em 50 projetos;
    ArcelorMittal, com cerca de R\$ 9,2 mi em 22; EDP, com cerca de R\$ 7,7 mi em 32; Grupo Águia Branca; Ambev; Grupo
    Coutinho;
  - o prêmio "reconhece e valoriza os maiores patrocinadores" e visa "despertar o interesse" de mais empresas;
  - na mesma cerimônia, o governador: "A lei nada mais é que o pagamento do imposto que seria pago ao Estado, vai
    direto para um evento cultural".
  - Leitura: o próprio Estado acrescenta retorno de reputação **proporcional ao valor destinado**, isto é, ao imposto
    de quem escolhe. Reforça H1 e a leitura de que a escolha pesa pelo imposto, e não pelo número de pessoas que
    valorizam o bem.
- **Chamada própria da ES Gás (2023)**: a notícia da SECULT existe, mas o corpo não veio no HTML (relé e web_fetch).
  A empresa roda uma seleção privada de projetos incentivados; o critério e quem decide ficam indeterminados até
  ler a chamada.

## 7. Resultado do relé para os vídeos

- **Legendas: bloqueadas.** Os 9 vídeos deram "Sign in to confirm you're not a bot" no runner do GitHub, e o
  a3VjhSXbhMI é privado (`dados/fontes_web/manifesto.csv`, ids `video:*`). O plano B (`web_fetch` do Parallel) atingiu o
  limite do plano gratuito. As passagens da seção 5 continuam como paráfrase da tradução automática.
- **Canais: listados.** `dados/fontes_web/videos_canal.tsv` tem 100 vídeos com título relevante, entre eles:
  - as transmissões das reuniões ordinárias do Conselho Estadual de Cultura, da 168ª à 191ª, e extraordinárias;
  - "FestCria | Bate-papo: A importância do patrocínio empresarial na promoção da cultura" (-igzJ8YBq1I), para H1;
  - "Guia Editais Funcultura | Critérios de seleção" (1wHaPByDvtI), para o contraste de seleção.
- Para obter as transcrições:
  - rodar `yt-dlp` localmente com cookies do navegador (`--cookies-from-browser`), com a mesma lista (`videos.tsv`);
  - ou abrir "Mostrar transcrição" no YouTube e salvar o texto em `dados/fontes_web/transcricoes/<id>.txt`.

  Fica para a 2ª parte da disciplina.

## 8. Análogo para complementar: LIC do Rio Grande do Sul

Ver `notas/politica/fontes/rs-lic-analogo.md` (trechos literais da Sedac/RS e do Governo do RS).
- Mesmo instrumento: empresa contribuinte do ICMS abate 100%, com limite de 5% a 20% do imposto do ano anterior.
- Duas diferenças de desenho que tocam H1 e H2:
  - o patrocinador faz repasse adicional **não incentivado** de 5% ou 10% ao Fundo de Apoio à Cultura;
  - os projetos passam por edital com **nota** (mínimo de 60), são contemplados em ordem decrescente, com vagas por
    finalidade e repescagem por descentralização regional.
- No artigo (§4.2, H2), numa frase junto com o Funcultura (RIO GRANDE DO SUL, 2024; 2026).
- Outros análogos vizinhos (MG, Lei 22.944/2018; RJ, lei de 1992 e Lei 7.035/2015): localizados, sem conferência do
  texto legal nesta sessão. Minas já entra na revisão por Teixeira *et al.* (2021).

## 9. Pendências

- Transcrições (ver a seção 7).
- Chamada própria da ES Gás (2023): o corpo da notícia não veio no HTML.

## 10. Rotas alternativas para o que faltava (27/09/2026, madrugada)

Pedido do autor: "procurar outra rota para resgatar contexto perdido ou não encontrado dos dados da CAP e da LICC".
Resultado de cada rota (relé, runs 36301577545 e 36302216421):

| Rota | O que buscou | Resultado |
| --- | --- | --- |
| Repositório `fcarva/licc.gov` | dados não trazidos para cá | nada novo: os brutos (`data/raw`) não são versionados lá |
| Links já coletados e nunca seguidos | documentos da LICC citados em páginas coletadas | aviso no DIO (era o credenciamento de pareceristas, não depósitos), cartilha 2022, modelo do relatório de execução |
| **Versões antigas dos anexos no servidor da SECULT** | o CMS guarda o arquivo substituído e acrescenta "(n)" ou "-n" ao novo | **18 versões recuperadas** (2024: 5; 2025: 11; 2026: 2) e 2 da lista de habilitados. Ver `analise/13_versoes_anexos.py` |
| **Wayback Machine (CDX)** | tudo o que foi arquivado em `secult.es.gov.br/media` (16.725 capturas) | 83 arquivos da LICC nunca coletados. Recuperadas: listas "Projetos habilitados para captação" de 13/06/2022, 30/06/2022 e 12/12/2023; atas da comissão julgadora do credenciamento de pareceristas (2022-2023); datas de captura que datam as versões dos anexos |
| Mapa Cultural, fases da LICC | inscrições das fases Parecerista, CAP e Publicação final (2024-2026) | as inscrições **não são públicas** (`publishedRegistrations: false`, respostas vazias). Mas a oportunidade de 2025 e 2026 registra como **categoria da inscrição as seis linhas do art. 9º**: a linha existe no sistema, e só a LAI a libera |
| Mapa Cultural, projetos e eventos | entidades marcadas LICC | 19 projetos autodeclarados e 5 eventos com linguagem: cobertura pequena, só ilustrativa |
| dados.es.gov.br (CKAN) | conjuntos de cultura e incentivo | nenhum da LICC (só contratos, convênios e parcerias da SECULT) |
| Relatórios da LAI da SECULT | pedidos e respostas | só estatísticas até 2018, antes da LICC |
| Planilhas "controle mensal" | pareciam da LICC | são do edital de Circulação e Intercâmbio (R\$ 100 mil por mês) |
| Manual de marcas LICC/Funcultura | regra de proporcionalidade das logomarcas (H1) | PDF só com imagem e truncado em 1 MB: sem texto |
| YouTube por espelho (Invidious) | legendas em português que o runner não obtém | **funciona**: a live Tira-Dúvidas tem legenda automática em português. Pedidas as legendas de 11 vídeos |

### A fila de 2024 nas versões do anexo de captação

`analise/tabelas/13_versoes_captados.csv` e `13_versoes_captados_fila.csv`:
- As versões (0) a (4), a (4) capturada pela Wayback em 15/05/2024, trazem **58 termos validados somando exatamente
  R\$ 15 milhões** (o montante antes da ampliação). A seção "indeferidos por ultrapassar o montante" cresce de 18
  termos (R\$ 3,24 mi) para 31 (R\$ 7,29 mi).
- Depois da ampliação para R\$ 25 milhões (Portaria SEFAZ 41-R/2024), a versão (5), com recebimentos até 11/06/2024,
  traz 110 termos e R\$ 25 milhões. A atual, (6), traz 109 termos e 22 indeferidos (R\$ 8,80 mi).
- Na chave patrocinador (raiz do CNPJ) × valor do termo, **23 termos (R\$ 5,04 mi) foram recusados antes e validados
  depois da ampliação**, e cerca de 20 nunca foram validados. Quatro chaves são ambíguas, porque o mesmo patrocinador
  tem o mesmo valor em projetos diferentes, e ficaram fora da contagem.
- Para a 2ª parte da disciplina, é uma **segunda chance quase experimental** para H5: termos com patrocinador,
  recusados pelo montante, uns validados pela ampliação e outros não. Resta saber qual regra decidiu quem entrou (a
  ordem de protocolo?), e a fila da SEFAZ (LAI) responde. Não entra no artigo sem essa verificação.

### 2025 e 2026

- 2025: as versões (7) a (17) têm data de recebimento em cada termo, e a ordem dos sufixos confere com as datas:
  - (7) até 01/04;
  - (11) até 08/04;
  - (13) até 14/04, capturada em 26/04;
  - (15) até 28/04;
  - (16) até 20/05, com 95 termos e R\$ 25 mi.

  As versões (0) a (6) têm outro layout, e o leitor por colunas não reproduz o total impresso: ficam marcadas como
  "inconsistente". Os totais impressos sobem de R\$ 8,4 mi para R\$ 25 mi.
- 2026: a versão (0), com recebimentos até 19/02, já soma R\$ 25,67 mi, acima dos R\$ 25 mi iniciais. A data de
  publicação é indeterminada, então não se sabe se ela saiu antes ou depois da ampliação para R\$ 31 mi (05/03). A (1),
  até 02/03, soma R\$ 31,19 mi, e a atual R\$ 31,51 mi.
