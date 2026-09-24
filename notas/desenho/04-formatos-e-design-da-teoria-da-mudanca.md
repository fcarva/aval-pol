# Formatos de teoria da mudança e decisões de design da Figura 2

Pedido dos autores (24/09/2026): manter o formato J-PAL e reformular com boas práticas de diagramação. Tons pastel no
estilo Flexoki, fonte Inter, espaçamento adequado, sem comprimir informação. Figura gerada por
`analise/08_figura_teoria_da_mudanca.py` → `analise/figuras/08_teoria_da_mudanca.{html,png,pdf}`.

## 1. Formatos consultados

| Formato | Como representa premissas | Onde aparece | Serve para a LICC? |
| --- | --- | --- | --- |
| Cadeia de resultados linear (insumos → atividades → produtos → resultados → finais) | abaixo ou ao lado, em texto | Gertler *et al.* (2018, fig. 2.1); TdM [s.7–9] | base conceitual; esconde as duas decisões da LICC |
| **Árvore vertical do J-PAL**, com cores por nível | faixas entre produtos e resultados | TdM [s.11]; M03 [s.11, s.34] | **formato da professora; mantido** |
| Tabela de cinco colunas / modelo lógico (componente, descrição, indicadores, premissas e riscos) | coluna própria | TdM [s.15–16] (Bolsa Atleta) | vira o Quadro 2 do artigo |
| Marco lógico (impacto, propósito, componentes, atividades × objetivos, indicadores, fonte, premissas) | coluna própria | TdM [s.14]; M03 [s.10] | redundante com o modelo lógico |
| Cadeia linear com pressupostos **entre cada elo** e fatores de contexto | caixas entre os elos | HM Treasury (2026, fig. 2.2, p. 46), com base em Mayne (2017) | inspira a marcação nos elos |
| Cadeias separadas por atividade; pressupostos abaixo do diagrama; funil de atrito; modelo de mudança comportamental (ator, mudança, indicador) | lista abaixo | White e Raitzer (2017, p. 21-26) | três cadeias (entrada, financiamento, entrega) e "quem decide" |
| "Causal link assumptions" em caixas pontilhadas junto de cada elo; teorias aninhadas | caixa pontilhada ligada ao elo | Mayne (2015) [VERIFICAR: DOI enviado ao relé]; Mayne e Johnson (2015) [VERIFICAR] | **adotado**: marcadores H nos elos e cartões tracejados |
| Caminho de resultados por mapeamento reverso (*backwards mapping*); precondições; premissas numeradas na narrativa | números nas setas e texto à parte | Center for Theory of Change / ActKnowledge (*Theory of Change Basics*; *Technical Papers*) | numeração H1a...H3 remete ao Quadro 2 |
| Guia do UNDG (2017): mudança, análise causal, premissas e riscos explícitos, atores | lista de premissas e riscos por caminho | UNDG, *Theory of Change: UNDAF Companion Guidance* | reforça premissa × risco |
| Raias por ator (*swimlane*) | — | prática de diagramação de processos | trocado por uma etiqueta "quem decide" em cada caixa, para não multiplicar colunas |

Fontes da web consultadas em 24/09/2026 (páginas institucionais; só orientam o design, não entram no artigo):
[theoryofchange.org](https://www.theoryofchange.org/what-is-theory-of-change/how-does-theory-of-change-work/),
[ToC Basics](https://www.theoryofchange.org/wp-content/uploads/toco_library/pdf/ToCBasics.pdf),
[UNDG](https://unsdg.un.org/resources/theory-change-undaf-companion-guidance),
[Mayne 2015 (resumo)](https://www.researchgate.net/publication/279533296_Useful_Theory_of_Change_Models),
[Mayne e Johnson 2015](https://journals.sagepub.com/doi/10.1177/1356389015605198),
[CRS, guia prático](https://www.crs.org/sites/default/files/2025-03/2022_08_toc_eng.pdf) (bloqueado no proxy; só o
resumo da busca), [FANTA, checklist](https://www.fantaproject.org/sites/default/files/resources/2B-Theory-of-Change-Checklist.pdf).
Consenso dessas fontes:

- toda seta é uma premissa ("por que este passo leva ao próximo?");
- atividade e produto ficam em caixas diferentes;
- uma direção de leitura;
- evitar cruzamento de setas;
- não depender só da cor.

## 2. Decisões de design da Figura 2

1. **Estrutura.** Árvore vertical do J-PAL (formato da disciplina), de cima para baixo. Dentro de cada linha, a
   leitura vai da esquerda para a direita. As três cadeias de White e Raitzer (entrada, financiamento, entrega)
   aparecem como linhas de atividade e produto que se alternam, e cada caixa diz **quem decide**. O dinheiro passa
   por quatro atores; é a leitura do licc.gov.
2. **Premissas nos elos.** Cada hipótese é uma pílula (H1a, H1b, H2a, H2b, H3) posta **sobre a seta** a que se
   refere. A explicação fica num cartão tracejado à direita, na mesma altura (Mayne, 2015). O texto completo, com
   evidência, vai para o Quadro 2 do artigo. O diagrama mostra a estrutura; o quadro argumenta.
3. **Setas.** Conectores ortogonais com cantos arredondados, sem cruzamentos. Tracejado = elo sem dado público
   (inscrição e benefício). A legenda explica os três códigos: seta cheia, seta tracejada, pílula.
4. **Cor.** A cor codifica **só o nível** da cadeia, nas cores do slide do J-PAL (vermelho, laranja, amarelo, verde,
   azul), em tons pastel da Flexoki:
   - preenchimento no tom 50;
   - contorno no 300;
   - rótulos no 700;
   - o roxo é reservado às premissas.

   A cor nunca é o único sinal: cada nível tem rótulo escrito, e as premissas têm borda tracejada e sigla.
5. **Contraste (WCAG 2.1).** Todo texto passa o nível AA (4,5:1):
   - corpo sobre os pastéis: de 8,9 a 14,2:1;
   - rótulos de nível sobre branco: de 4,9 (amarelo) a 8,3:1;
   - "quem decide": 6,1:1, depois da troca do base-600 pelo base-700, que dava 4,3:1.
6. **Tipografia.** Inter:
   - rótulo de nível em versalete com espaçamento de 0,07 em;
   - título da caixa em seminegrito, 12,6 px;
   - corpo, 12 px;
   - metadados, de 9,6 a 10,8 px;
   - entrelinha de 1,38 a 1,42.

   Na largura de 16 cm, o corpo sai com cerca de 7,5 pt e o menor texto com cerca de 6 pt.
7. **Espaço.** 36 px entre linhas, 38 px entre caixas pareadas, margem interna de 9 a 12 px. A figura ocupa 16 ×
   21,7 cm, uma página inteira com legenda e fonte, sem espremer texto. Os textos das caixas foram editados para
   não repetir o que o rótulo do nível já diz (ex.: "a participação:" saiu de P2).
8. **Saída.** PNG a 300 dpi para o Word, PDF vetorial e HTML editável; tudo reproduzível pelo script.

## 3. Licenças

Flexoki: licença MIT, © Steph Ango, https://stephango.com/flexoki (valores conferidos no README de
github.com/kepano/flexoki). Inter: SIL Open Font License 1.1, © The Inter Project Authors; arquivos e licença em
`analise/fontes/inter/`.
