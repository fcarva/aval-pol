# A LICC como financiadora de bens públicos culturais: tradução da pergunta de alocação para inferência causal

Pergunta dos autores (24/09/2026): quanto a LICC é um instrumento de financiamento de bens públicos culturais, e
se o arranjo em que o Estado define o cardápio (habilitação) e a empresa escolhe no cardápio leva os recursos para
onde a população, principal beneficiária, mais ganha. Exemplo: parte da população frequenta batalhas de rima, que
não são financiadas, enquanto a distribuidora de energia põe a marca em música de concerto.

Escopo: avaliar a política **como ela está**. As "alocações de referência" abaixo são contrafactuais analíticos para
medir a distância entre o que é financiado e o que geraria mais valor público; não são proposta de novo mecanismo
(o `CLAUDE.md` exclui redesenho).

Referências conferidas pelo relé na Crossref (`dados/fontes_web/doi/`); McFadden (1974), capítulo de livro, segue [VERIFICAR].

## 1. O que os dados já dizem sobre o exemplo

Classificação por linguagem **inferida do título** (`analise/06_alocacao_linguagens.py`; 163 de 463 títulos ainda
sem classe; amostra de 60 para conferência manual em `analise/tabelas/06_amostra_conferencia.csv`). Números
exploratórios, não entram no artigo sem a conferência:

- **Cardápio (habilitados 2022-2026)**: hip-hop, rap e cultura urbana = 7 projetos, 1,4% do valor autorizado;
  música erudita e coral = 31 projetos, 6,5%; tradição popular e festas = 17,6%; música popular e festivais =
  18,3% (`06_linguagem_cardapio_por_ciclo.csv`).
- **Conversão (2022-2024, resolvidos)**: hip-hop e cultura urbana 4 de 4; erudita 14 de 18 (78%); tradição
  popular 34 de 46 (74%); música popular 41 de 50 (82%); títulos não classificados 54%
  (`06_linguagem_conversao_2022_2024.csv`).
- **Patrocinador**: em 2025 a EDP patrocinou 25 projetos (R$ 11,1 mi). A carteira tem música de concerto
  (Bach, orquestra, coral, formação em música clássica), mas é dominada por cultura popular tradicional do
  interior (folias de reis, boi pintadinho, festival de sanfona e viola), além de encontro de mulheres negras e
  festival de grafite (`06_linguagem_patrocinador_2025.csv`). A anedota vira hipótese, não premissa.
- **A batalha de rima existe no cardápio**: "Batalha do N9V: cultura, arte e lazer na favela", habilitada no
  ciclo 2024, seguia "captando" na lista de setembro de 2026 e não aparece em nenhum anexo de captação.

Leitura: o que chama atenção não é a empresa rejeitar cultura urbana na captação (a amostra é pequena demais para
dizer), e sim quão pouca cultura urbana chega ao cardápio. O problema tem **duas margens** — entrada (quem se
inscreve e é habilitado) e escolha (quem a empresa patrocina) — e a inferência precisa separá-las.

## 2. O problema em termos econômicos

- **Bem público cultural**: o valor de um projeto para a população depende do grau em que ele é não rival e não
  excludente (evento gratuito em espaço público; patrimônio; acervo aberto) e de sua qualidade de bem meritório
  (Throsby, 1994). Um espetáculo com ingresso ou um evento fechado para clientes do patrocinador tem componente
  privado.
- **Condição de eficiência** (Samuelson, 1954): provisão eficiente quando a soma dos benefícios
  marginais da população iguala o custo marginal. Na LICC, quem escolhe o projeto (a empresa) tem custo líquido
  zero — o crédito é de 100% — e internaliza só o próprio benefício: marca, relação com clientes, fornecedores e
  regulador (O'Hagan; Harvey, 2000), além do *warm glow* (Andreoni, 1990). Sem preço, a escolha não
  revela quanto a população valoriza o projeto.
- **A cunha**: para cada projeto j, o valor social W_j e o valor privado para o patrocinador s, B_sj. A alocação
  observada maximiza Σ B_sj sob o teto; a eficiente maximizaria Σ W_j. A batalha de rima é o caso de W alto e B baixo
  para uma distribuidora de energia; um concerto consolidado pode ser B alto e W baixo, se aconteceria de todo modo
  (baixa adicionalidade) ou alcança pouca gente.
- **Três decisores**: a SECULT/CAP define o cardápio; a empresa escolhe no cardápio; o teto raciona, e em 2023-2024 o
  racionamento final foi pela ordem de validação dos termos (termos indeferidos por ultrapassar o montante: 28% e 35%
  do montante).

## 3. Tradução para resultados potenciais

- **Unidade**: projeto habilitado j (o cardápio). **Tratamento**: D_j = 1 se captou pela LICC.
- **Resultado** Y_j = valor público produzido, em três camadas: (a) **ocorrência** — o bem existe (o evento
  aconteceu, o produto foi feito); (b) **alcance** — público, gratuidade, território, perfil do público; (c)
  **valor** — quanto a população valoriza aquele bem (preferência).
- **Efeito do financiamento**: τ_j = Y_j(1) − Y_j(0). Ele combina adicionalidade (o bem só existe com o recurso?)
  e alcance/valor.

### Estimandos

| # | Pergunta | Estimando | Natureza |
| --- | --- | --- | --- |
| E1 | Quanto do que a LICC financia é bem público cultural? | parcela do valor captado em bens de acesso livre e gratuito (descritivo) + adicionalidade: E[Y(1) − Y(0)] na margem extensiva (o evento só acontece com o recurso?) | descritivo + causal |
| E2 | A escolha da empresa acerta o alvo dentro do cardápio? | EMPT (captados) × EMPNT (habilitados racionados). Se o efeito nos racionados supera o efeito nos captados, realocar dentro do mesmo cardápio aumentaria o valor público. Ganho da escolha privada sobre uma alocação aleatória com o mesmo teto: Σ τ_j (D_j − D_j^aleatória), proporcional a Cov(τ_j, D_j) — **seleção sobre ganhos** | causal (escolha de tratamento: Manski, 2004; Kitagawa; Tetenov, 2018; Athey; Wager, 2021) |
| E3 | O que a empresa valoriza difere do que a população valoriza? | pesos implícitos da empresa nos atributos dos projetos (linguagem, território, porte, recorrência, gratuidade) × pesos da população nos mesmos atributos; a cunha é a diferença | modelo de escolha (empresa) + experimento de escolha (população) |
| E4 | Quem chega ao cardápio? | taxa de habilitação por linguagem e território entre inscritos | descritivo; exige os inscritos não habilitados (LAI) |

E2 é a tradução direta de "a população gosta da batalha de rima, e ela não é financiada": um projeto com τ alto e
D = 0. E3 diz por quê. E4 mede se o problema está antes da escolha.

## 4. Identificação com as bases disponíveis

**A. Racionamento pelo teto (2023-2024) → adicionalidade na margem (E1, E2).** Os anexos de captação listam, projeto a
projeto, os termos indeferidos por ultrapassar o montante: 11 termos em 2023 e 22 em 2024 (21 projetos), todos com
patrocinador disposto. Perto do esgotamento, entrar ou ficar de fora dependeu sobretudo da ordem de validação.
Comparar esses projetos com os que tiveram termos validados pouco antes do esgotamento identifica o efeito do
financiamento na margem: **o evento aconteceu mesmo assim?** Resultado observável em dados públicos: eventos no Mapa
Cultural ES, nova habilitação no ciclo seguinte, projeto no SALIC, extratos no DIO. Ameaças: n pequeno; a ordem pode
não ser aleatória (proponentes mais organizados chegam antes) — testar balanço nos atributos observáveis.

**B. Captou × expirou (2022-2024) → adicionalidade por linguagem (E1, E2).** Para os 95 expirados, verificar se o
evento aconteceu sem a LICC. Seleção não aleatória: reportar limites (Manski) em vez de ponto.

**C. Escolha do patrocinador → pesos da empresa (E3).** Cada termo validado nos anexos de 2022 a 2026 é uma escolha de
uma empresa entre os projetos "captando" naquele momento. Logit condicional (McFadden, 1974 [VERIFICAR]) sobre o
cardápio vigente estima quanto a empresa pesa linguagem, território, porte, recorrência. Heterogeneidade por setor
(serviço regulado de energia e gás × comércio × indústria) testa o motivo de marca/regulação. Hipótese de
identificação: utilidade aleatória e cardápio exógeno à empresa.

**D. Preferências da população (E3).**
- *Revelada*: eventos e agentes culturais no Mapa Cultural ES (API pública para eventos e agentes, com linguagem e
  município; teste de acesso no relé) medem a atividade cultural que existe sem a LICC — por exemplo, batalhas de
  rima cadastradas — e onde ela está; editais de escolha pública no mesmo estado (Funcultura, PNAB/LPG) servem de
  alocação de referência por linguagem e território.
- *Declarada, com identificação experimental*: experimento de escolha (conjoint) com moradores. Cada respondente
  escolhe entre pares de projetos com atributos sorteados — linguagem (batalha de rima, concerto, festa tradicional,
  teatro...), local (bairro periférico, centro, interior), gratuidade, público. O sorteio dos atributos identifica o
  efeito causal médio de cada atributo na preferência, o AMCE (Hainmueller; Hopkins; Yamamoto, 2014).
  Comparar com os pesos da empresa (C) mede a cunha. Custo baixo (questionário online); exige revisão ética e LGPD.

**E. Mesmo proponente, decisores diferentes.** Proponentes com projetos na LICC e em editais públicos: a diferença de
composição (linguagem, local, gratuidade) com o proponente fixo mede o efeito de quem escolhe.

## 5. O que dá para fazer já, com o que está no repositório

1. Conferir à mão a amostra de 60 títulos e reduzir os 163 não classificados (regras em `06_alocacao_linguagens.py`).
2. Tabelas por linguagem × território: cardápio, conversão, carteira dos patrocinadores (2025 pronto; 2022-2024
   exige extrair projeto e patrocinador dos anexos, com o leitor posicional do licc.gov).
3. Lista dos termos indeferidos por projeto, linguagem e território (anexos de 2023 e 2024 já coletados).
4. A API pública de eventos do Mapa Cultural ES responde pelo relé e traz a linguagem de cada evento
   (`dados/fontes_web/paginas/mapa_cultural_api_eventos.txt`); falta coletar todos os eventos com local e data.

Sem dado de público e de ocorrência, E1 e E2 ficam como desenho; E3 do lado da empresa é estimável já com os anexos.

## 6. Como entra no artigo (decisão dos autores)

- **Opção 1 — agenda**: manter o artigo e citar esta pergunta em um parágrafo na conclusão.
- **Opção 2 — recomendada**: trocar o desenho municipal (que o próprio texto considera fraco) por um desenho de
  alocação em cerca de uma página: estimando E2, identificação pelo racionamento do teto (A) e experimento de escolha
  com a população (D). Aproveita o item REV-3 do Stage 3, responde à pergunta sobre o beneficiário e cabe no prazo.
- **Opção 3**: tornar a alocação a pergunta principal da seção 5. É o maior trabalho e o mais arriscado a 4 dias da
  entrega.

## Referências

Conferidas na Crossref pelo relé (24/09/2026):

- ANDREONI, J. Impure altruism and donations to public goods: a theory of warm-glow giving. **The Economic Journal**, v. 100, n. 401, p. 464-477, 1990. DOI: 10.2307/2234133.
- ATHEY, S.; WAGER, S. Policy learning with observational data. **Econometrica**, v. 89, n. 1, p. 133-161, 2021. DOI: 10.3982/ECTA15732.
- BERGSTROM, T.; BLUME, L.; VARIAN, H. On the private provision of public goods. **Journal of Public Economics**, v. 29, n. 1, p. 25-49, 1986. DOI: 10.1016/0047-2727(86)90024-1.
- HAINMUELLER, J.; HOPKINS, D. J.; YAMAMOTO, T. Causal inference in conjoint analysis: understanding multidimensional choices via stated preference experiments. **Political Analysis**, v. 22, n. 1, p. 1-30, 2014. DOI: 10.1093/pan/mpt024.
- HECKMAN, J. J.; VYTLACIL, E. Structural equations, treatment effects, and econometric policy evaluation. **Econometrica**, v. 73, n. 3, p. 669-738, 2005. DOI: 10.1111/j.1468-0262.2005.00594.x.
- KITAGAWA, T.; TETENOV, A. Who should be treated? Empirical welfare maximization methods for treatment choice. **Econometrica**, v. 86, n. 2, p. 591-616, 2018. DOI: 10.3982/ECTA13288.
- MANSKI, C. F. Statistical treatment rules for heterogeneous populations. **Econometrica**, v. 72, n. 4, p. 1221-1246, 2004. DOI: 10.1111/j.1468-0262.2004.00530.x.
- SAMUELSON, P. A. The pure theory of public expenditure. **The Review of Economics and Statistics**, v. 36, n. 4, p. 387-389, 1954. DOI: 10.2307/1925895.

Já no artigo: O'HAGAN; HARVEY (2000); THROSBY (1994); BROOKS (2004). A conferir: McFADDEN, D. Conditional logit analysis
of qualitative choice behavior. *In*: ZAREMBKA, P. (ed.). **Frontiers in econometrics**. New York: Academic Press, 1974
[VERIFICAR].
