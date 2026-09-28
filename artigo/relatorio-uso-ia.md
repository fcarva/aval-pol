---
title: "ANEXO – REGISTRO DO USO DE INTELIGÊNCIA ARTIFICIAL NO REPOSITÓRIO DO TRABALHO"
lang: pt-BR
---

<!-- Anexo da declaração de uso de IA (artigo/declaracao-uso-ia.md). Fonte do texto; o .tex é gerado por
     artigo/gerar_uso_ia.py, que preenche os marcadores {{...}} com o git log e monta as Tabelas 1 a 3 e o Quadro 5.
     Hash de commit entre crases vira link para o commit. Voz impessoal, como no artigo. -->

Este anexo detalha a declaração a partir do histórico do repositório público do trabalho ([github.com/fcarva/aval-pol](https://github.com/fcarva/aval-pol)), onde ficaram os dados, os scripts, as notas, o texto do artigo e as auditorias. O objetivo é permitir que o leitor veja o que a ferramenta de IA fez, o que o autor decidiu e como o resultado foi conferido, com cada afirmação ligada ao commit ou ao arquivo que a registra.

# 1 Fonte e método

A fonte é o `git log` dos ramos `claude/fervent-shannon-jq7142`, onde o trabalho foi feito, e `main`, que recebeu o trabalho por pull request, até o commit `{{head}}` ({{head_data}}). Cada commit registra autoria, data, mensagem e arquivos alterados, e se classifica pela autoria registrada:

- **autor:** commits feitos pelo próprio autor;
- **agente de IA:** commits feitos pelo Claude Code em sessão aberta e conduzida pelo autor; os {{n_coautoria}} commits do agente trazem o marcador de coautoria da Anthropic na mensagem;
- **relé de coleta:** commits automáticos do GitHub Actions, que baixam as fontes pedidas e as devolvem ao repositório, sem IA (seção 2);
- **mesclagens:** junções de ramos, sem conteúdo próprio.

As contagens, as Tabelas 1 a 3 e a cronologia do Quadro 5 são geradas por `artigo/gerar_uso_ia.py` a partir do `git log`, com horários de Brasília (UTC−3). O restante do texto foi redigido a partir das mensagens dos commits e dos relatórios de auditoria que eles criaram. O histórico registra o que entrou no repositório, não as conversas: as instruções do autor aparecem nas regras do projeto (`CLAUDE.md`), nas decisões registradas nele, nas mensagens dos commits e nos relatórios de auditoria. As obras citadas de passagem, como Gertler *et al.* (2018), estão nas referências do artigo.

# 2 Ferramentas

O Quadro 1 separa a ferramenta de IA generativa das automações e programas que ela escreveu ou acionou. Na sessão em nuvem, a rede alcançava só o GitHub e os registros de pacotes; por isso as fontes da web vieram pelo relé de coleta e, na última fase, pelo Firecrawl, com URL, data e sha256 de cada arquivo coletado.

**Quadro 1 – Ferramentas usadas no trabalho e papel de cada uma**

| Ferramenta | O que fez | IA generativa? | Registro |
| ---------------- | -------------------------------------------- | ------------ | ------------------ |
| Claude (Anthropic), pelo Claude Code em sessão na nuvem (ANTHROPIC, 2026) | Leu e escreveu arquivos do repositório, rodou scripts e fez commits, sempre por instrução do autor: notas, scripts, tabelas, figura, texto, pareceres simulados e geradores do Word e do LaTeX | Sim | commits de autoria "Claude" (Quadro 5) |
| Academic Research Skills, versão 3.22.1 (WU, 2026) | Protocolos escritos que o agente seguiu para a checagem de integridade e o painel simulado de cinco pareceristas | Conduz o agente | `artigo/auditoria` |
| Relé de coleta (GitHub Actions) | Baixa DOIs, buscas bibliográficas, páginas, PDFs, legendas e consultas públicas pedidos em listas e devolve o texto por commit | Não (código escrito pelo agente) | `.github/workflows/buscar-fontes.yml`, `dados/fontes_web` |
| Firecrawl | Busca na web e raspagem de páginas HTML na Fase A ({{data:d58c3c0}}), acionado pelo agente | Não gera o texto usado | `dados/fontes_web/firecrawl` |
| Python (pandas), pandoc e XeLaTeX | Análise dos dados, conversão para Word e LaTeX e compilação | Não | `analise`, `artigo/gerar_docx.py`, `artigo/gerar_tex.py` |

Fonte: mensagens dos commits e arquivos citados; Anthropic (2026); Wu (2026).

# 3 O registro em números

Até `{{head}}`, o repositório tem {{n_total}} commits (Tabela 1): {{n_agente}} do agente, {{n_rele}} do relé, {{n_autor}} commit direto do autor e {{n_merges}} mesclagens, das quais {{n_merges_autor}} feita pelo autor. O commit do autor (`{{ini_curto}}`) é o ponto de partida: trouxe {{ini_arquivos}} arquivos preparados antes, fora deste histórico (seção 4). Os commits do agente alteraram {{ag_arquivos}} arquivos distintos, com {{ag_mais}} linhas incluídas e {{ag_menos}} excluídas (Tabela 2); o relé devolveu {{rele_arquivos}} arquivos em {{rele_etapas}} etapas (Tabela 3). As linhas incluem tabelas de dados e arquivos gerados; medem volume de alteração, não autoria do texto.

[[tabela-origens]]

[[tabela-areas]]

[[tabela-rele]]

# 4 O que a IA fez, etapa por etapa

**Ponto de partida (até {{data:82f7a41}}).** O commit inicial do autor (`82f7a41`) já trazia os dados herdados do repositório licc.gov, o texto extraído do material da disciplina, notas de leitura, scripts iniciais, a cópia dos protocolos Academic Research Skills e o `CLAUDE.md`, arquivo de instruções do Claude Code com as regras do projeto. O histórico não mostra como esse material foi produzido; ao menos uma nota traz a marca de que foi gerada por agente de IA e exige revisão humana (`notas/disciplina/04-itau-magenta-adb.md`).

**Base e primeiro rascunho ({{data:c5e2f38}}).** O agente gerou as tabelas descritivas, completou as notas sobre o desenho legal, o contexto, a literatura e os métodos, desenhou a figura e escreveu o primeiro rascunho completo do artigo, com 13 páginas (`f2e40ea`).

**Relé, auditoria e teoria da mudança ({{data:0b3cde1}} a {{data:a357578}}).** O agente escreveu o relé de coleta (`0b3cde1`) e a checagem automática dos números do artigo (`b0323e4`). A primeira checagem de integridade falhou (`3b4a01e`): havia estudo citado com resultado oposto ao seu e concentração do valor habilitado atribuída à captação; depois das correções, passou com ressalvas (`85a488d`). Seguiram-se o primeiro painel simulado, com decisão de revisão maior (`0108f5e`), o desenho causal e a teoria da mudança (`120c652`, `a246c4e`), a reestruturação do artigo (`49ae7ae`), a versão em LaTeX (`c8ed005`), o segundo painel (`7e601d6`), as correções (`2550a74`), a checagem final de integridade (`923c8d9`) e a auditoria da captação termo a termo, com a máscara dos CPFs (`a357578`).

**Mesclagem pelo autor ({{data:28b7ccc}}).** O autor mesclou o trabalho no ramo principal pelo pull request nº 1 (`28b7ccc`).

**Nova moldura, dados públicos e revisões ({{data:b236335}} a {{data:bbfabfa}}).** Por decisão do autor, as hipóteses foram reorientadas para a moldura de bens públicos (`b236335`, `b4184cd`), e o terceiro painel as examinou (`810b066`). O agente leu as atas da Comissão de Avaliação Permanente (`6b0b548`), testou rotas alternativas de dados, como cópias arquivadas, legendas de vídeos e minutas de pedidos por LAI (`c2397a8` a `af51877`), e cruzou a LICC com o Portal da Transparência (`31670a0`, `609de69`). Revisou os trechos que o autor grifou no PDF (`494399a`) e passou o texto à voz impessoal (`73f91c4`). Vieram então o quarto painel (`bca72a5`, `4e11aa7`), o roteiro frase a frase para a revisão do autor (`a254775`), as edições que o autor fez no `.tex`, trazidas ao texto-fonte (`0210713`), e um novo desenho de avaliação (`bbfabfa`).

**Revisões finais e parecer externo ({{data:d01657f}} a {{data:086671d}}).** Uma revisão metodológica (`d01657f`) e o quinto painel (`ed5f32f`) reorganizaram a §5 do artigo. Na Fase A, o agente usou o Firecrawl e o relé para fechar lacunas de contexto: a avaliação oficial da LICC contratada pelo Estado, o PPA sem metas para a lei e as etapas da captação (`d58c3c0`, `9980131`, `ab8cb18`). Na Fase B, a §5 do artigo foi refeita em torno de uma única pergunta, com o desenho que o autor trouxe de outra sessão de trabalho, e o parecer externo enviado pelo autor foi respondido ponto a ponto (`cd272da`). A versão final incorporou as edições do autor e os links (`086671d`).

# 5 O que o autor decidiu

O agente propôs, redigiu e conferiu; as escolhas de escopo, de desenho e de texto ficaram com o autor. O Quadro 2 lista as decisões que o repositório registra. O desenho da avaliação de impacto mudou três vezes (`bbfabfa`, `ed5f32f`, `cd272da`): a versão final segue o desenho trazido pelo autor e descarta os experimentos propostos antes pelo agente.

**Quadro 2 – Decisões do autor registradas no repositório**

| Data | Decisão | Registro |
| ------ | ------------------------------------------------------------ | -------------- |
| {{data:82f7a41}} | Regras do projeto: ausência de dado não é zero; todo número com fonte e script; não afirmar descumprimento que o dado não permite apurar; toda referência conferida; uso de IA conforme a Portaria CNPq nº 2.664/2026 | `CLAUDE.md` (`82f7a41`) |
| {{data:923c8d9}} | Autoria individual; declaração de IA separada do artigo | `923c8d9` |
| {{data:28b7ccc}} | Mesclagem do trabalho no ramo principal (pull request nº 1) | `28b7ccc` |
| {{data:b236335}} | Escopo revisto: avaliar a política como ela está, na moldura de bens públicos, sem nomear nem propor mecanismos alternativos | `CLAUDE.md` (`b236335`) |
| {{data:494399a}} | Comentários nos trechos grifados do PDF; Buterin, Hitzig e Weyl (2019) e Hitzig (2021) como literatura; página indicada pelo autor | `494399a`, `fb161bb` |
| {{data:73f91c4}} | Voz impessoal, por ser trabalho individual | `73f91c4` |
| {{data:0210713}} | Edições diretas no `artigo.tex`, trazidas ao texto-fonte | `0210713` |
| {{data:ed5f32f}} | §5 do artigo organizada pela pergunta central sobre o financiamento centralizado | `CLAUDE.md` (`ed5f32f`) |
| {{data:cd272da}} | §5 do artigo com uma só pergunta ("a renúncia vai para os projetos que dependem dela?"), com os grupos que a regra já produz; nenhum piloto nem regra futura no texto; resposta ao parecer externo | `cd272da`, `artigo/auditoria/revisao-stage3-r6/01-resposta-ao-parecer.md` |
| {{data:086671d}} | Versão final: edições no `.tex`, "tradução nossa" na citação traduzida, "27 unidades da federação" e citação de Buterin, Hitzig e Weyl (2019) movida para a afirmação conceitual | `086671d` |

Fonte: mensagens dos commits, `CLAUDE.md` e relatórios de auditoria citados.

# 6 Verificação e salvaguardas

O conteúdo gerado passou por conferência automática e por revisão. As salvaguardas, todas no repositório, são:

- **Números:** `artigo/auditoria/checar_dados.py` recalcula cada número do artigo a partir da tabela de origem e confere o trecho do texto; na versão final, {{checagens_ok}} de {{checagens}} checagens conferem. A soma da captação é refeita termo a termo a partir dos PDFs oficiais por `artigo/auditoria/auditar_captacao.py` ({{captacao_ok}} de {{captacao}} conferem).
- **Referências:** das {{refs}} referências do artigo, as {{refs_doi}} com DOI são conferidas item a item nos metadados da Crossref por `artigo/auditoria/checar_referencias.py`; as {{refs_sem_doi}} sem DOI (normas, documentos oficiais e livros) são conferidas à mão, nas páginas oficiais, nas normas transcritas e nas buscas do relé, conforme os relatórios de integridade. Pela regra do projeto, referência não conferida não entra no texto.
- **Fontes:** todo arquivo coletado pelo relé ou pelo Firecrawl fica com URL, data e sha256 em manifesto (`dados/fontes_web`).
- **Dados pessoais:** CPFs de proponentes pessoas físicas são mascarados antes de gravar (`analise/rede/mascarar_cpf.py`, com conferência), e a regra do projeto é não guardar nomes de pessoas privadas.
- **Revisão:** as rodadas de checagem e de revisão estão no Quadro 3. Os painéis simulados foram redigidos pelo mesmo modelo que redigiu o texto, em papéis separados, como registra o primeiro painel (`0108f5e`); a separação de papéis não elimina erros correlacionados e não substitui a revisão por pares humana. Os pareceres serviram como lista de verificação, e o autor decidiu o que aplicar.

**Quadro 3 – Rodadas de checagem e de revisão**

| Data | Rodada | Resultado | Registro |
| ------ | ------------------------------------------ | ---------------------------------- | ---------- |
| {{data:3b4a01e}} | Checagem de integridade (números e referências), 1ª rodada | Reprovada; correções aplicadas | `3b4a01e` |
| {{data:85a488d}} | Checagem de integridade, 2ª rodada | Aprovada com ressalvas | `85a488d` |
| {{data:0108f5e}} | Painel simulado de cinco pareceres, rodada 1 | Revisão maior (7 itens obrigatórios) | `0108f5e` |
| {{data:7e601d6}} | Painel simulado, rodada 2 | Revisão menor (10 itens) | `7e601d6` |
| {{data:923c8d9}} | Verificação das correções e checagem final de integridade | Aceito, com a declaração de IA pendente | `923c8d9` |
| {{data:810b066}} | Painel simulado, rodada 3 (novas hipóteses) | Revisão menor (6 itens) | `810b066` |
| {{data:bca72a5}} | Painel simulado, rodada 4 | Revisão menor (4 itens), aplicada em `4e11aa7` | `bca72a5` |
| {{data:d01657f}} | Revisão metodológica do desenho | Aplicada | `d01657f` |
| {{data:ed5f32f}} | Painel simulado, rodada 5 | Revisão menor (4 itens), aplicada | `ed5f32f` |
| {{data:cd272da}} | Parecer externo enviado pelo autor | Respondido ponto a ponto | `cd272da` |

Fonte: mensagens dos commits e `artigo/auditoria`.

A verificação encontrou erros do próprio agente, corrigidos antes da versão final. O Quadro 4 lista os que o histórico registra; eles mostram por que o texto gerado não pode ser aceito sem conferência.

**Quadro 4 – Erros do agente encontrados na verificação e corrigidos**

| Erro | Como foi encontrado | Correção |
| -------------------------------------------------- | ------------------------------ | ---------- |
| Estudo citado com resultado oposto ao que ele encontra, e concentração do valor habilitado atribuída à captação | Checagem de integridade | `3b4a01e` |
| DOI de Williams (2020) que pertencia a outro artigo | Conferência na Crossref | `0893982` |
| "Cerca de 100 proponentes por ciclo", quando os dados dão de 53 a 95 | Checagem final dos números | `923c8d9` |
| A máscara de CPF quebrava a chave do proponente e mascarou valores de capital social de 11 dígitos | Nova execução do pipeline inteiro | `c3cd882` |
| CPF de titular de MEI exposto na razão social vinda da Receita e do Mapa Cultural | Conferência de CPF estendida aos dados externos | `0778be8` |
| O cabeçalho da página do Diário Oficial cortava avisos e escondia dois depósitos | Nova execução do pipeline (Fase A) | `9980131` |
| Página de Gertler *et al.* (2018) citada como 75, quando o trecho está na 74 | Leitura do texto coletado pelo relé | `d668105` |
| Links para o ramo principal sem as tabelas novas (erro 404) | Conferência dos links | `086671d` |

Fonte: mensagens dos commits citados.

# 7 Limitações do registro

- O histórico não contém as conversas com a ferramenta; as instruções do autor aparecem só indiretamente (seção 1).
- O material do commit inicial foi preparado antes e fora deste histórico, assim como o repositório licc.gov, de onde vieram os dados; o que se sabe de seu preparo está na seção 4.
- O desenho final da §5 do artigo veio de outra sessão de trabalho do autor, cujo registro não está neste repositório.
- A autoria de um commit indica quem o gravou, não quem escreveu cada linha: commits do agente carregam edições do autor (`0210713`, `086671d`), e o commit do autor carrega material preparado, ao menos em parte, com apoio de IA (seção 4).

# Referências

ANTHROPIC. **Claude Code**: documentação. [*S. l.*]: Anthropic, 2026. Disponível em: https://code.claude.com/docs/en/claude-code-on-the-web. Acesso em: 28 set. 2026.

WU, Cheng-I. **Academic Research Skills for Claude Code**. Versão 3.22.1. [*S. l.*], 2026. Disponível em: https://github.com/Imbad0202/academic-research-skills. Acesso em: 28 set. 2026.
