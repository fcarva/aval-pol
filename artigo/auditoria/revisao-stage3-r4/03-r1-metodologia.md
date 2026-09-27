# Parecer do R1 (Metodologia), rodada 4

**Recomendação: revisão menor, com três pontos obrigatórios (M1, M2 e M5).**

A Tabela 2 foi refeita à mão e confere: H5, de 28 a 34 pontos; H4 só com coletivos, de 5,5 a 13,4; H4 com todos os
agentes, de 2,8 a 8,5. Os problemas não estão nas contas, e sim em três regras dos slides de amostragem e poder que o
texto não aplica.

## M1. H4: número de conglomerados por grupo e braços (obrigatório)

Regra dos slides de amostragem (s. 29): "são necessários, pelo menos, 30 a 50 conglomerados em cada um dos grupos". O
texto propõe três coisas:
- sortear a oferta entre municípios do interior;
- "dois braços sorteados" (atrito documental × de patrocínio);
- sortear também a intensidade (saturação).

Resultado de `analise/19_poder_revisao.py` (EMD em pontos percentuais; *p*₀ de 2% a 10%; ρ de 0,02 a 0,05):

| Desenho | Coletivos (52 municípios) | Todos os agentes (71 municípios) |
| --- | --- | --- |
| a) dois grupos por município (Tabela 2) | 26 por grupo, **abaixo da regra**; 5,5 a 13,4 | 35,5 por grupo, atende; 2,8 a 8,5 |
| b) três grupos por município (controle e dois braços) | 17 por grupo, abaixo; 6,7 a 16,4 | 24 por grupo, **abaixo**; 3,4 a 10,4 |
| c) híbrido: oferta sorteada por município, braços sorteados entre agentes dos municípios tratados | 26 por grupo, abaixo; braços de 6,9 a 14,8 | 35,5 por grupo, atende; braços de **2,3 a 4,9** |

Leitura:
- Só com coletivos, nenhum desenho atende à regra.
- Com todos os agentes, os braços sorteados por município (b) também não atendem.
- O desenho híbrido (c) mantém 35 ou 36 municípios por grupo no contraste oferta × controle e compara os braços dentro
  do mesmo município, o que também elimina a correlação intragrupo desse contraste.
- A saturação, com 71 municípios, não comporta dois níveis de intensidade com 30 municípios em cada um; fica
  exploratória, ou é sorteada entre agentes dentro do município.

**Pedido:** na §5.2 (H4), dizer que a oferta é sorteada entre os 71 municípios e que os braços são sorteados entre
agentes dos municípios tratados. Na §5.4, uma oração com a regra dos 30 conglomerados por grupo, que só a versão com
todos os agentes atende.

## M2. Cumprimento parcial e VI: o EMD relevante é maior do que o da Tabela 2 (obrigatório)

Regra dos slides (s. 32): "cumprimento parcial ou atrito exigem amostra maior". O texto anuncia dois efeitos locais,
mas a Tabela 2 só mostra a forma reduzida:
- **H5, receber em algum momento.** A recusa é o instrumento, e o primeiro estágio é de 13/32 = 0,406. O EMD do efeito
  local é o da forma reduzida dividido por 0,406: **de 69 a 85 pontos**. Com uma amostra de 64 projetos, essa leitura
  não é informativa. Se a LAI trouxer os recusados de 2025 e 2026 e isso dobrar a margem (cenário), o EMD de receber
  agora cai para 20 a 24 pontos.
- **H4, efeito para quem adere.** Divide-se o EMD pela adesão. Com todos os agentes e adesão de 25%, fica de 11 a 34
  pontos; com adesão de 50%, de 5,6 a 17.

**Pedido:** uma oração na §5.4 com o EMD do efeito local de H5, de 69 a 85 pontos, e a regra de H4 (dividir pela
adesão). O parágrafo final da §5.4 já diz que a margem "só detecta efeitos muito grandes". Falta dizer que a leitura
por VI detecta ainda menos e que o cenário com LAI é o que torna H5 testável.

## M3. Teste da ordem da fila sem LAI (sugerido)

A identificação de H5 supõe que "a ordem de validação não se ligue ao projeto", e o texto diz que as datas de
protocolo, que dependem de LAI, permitem testar isso. Um primeiro teste já cabe com dado público: em 2025, a ordem da
"data do processo" do Portal tem correlação de postos de 0,91 com a hora de recebimento do anexo (62 termos; a data do
processo vem 19 dias depois do recebimento, na mediana). Com essa ordem, dá para comparar, dentro de cada cota:
- porte e idade do proponente (Receita);
- recorrência do par patrocinador–proponente;
- porte do patrocinador

entre os primeiros e os últimos da fila. Isso também responde ao DA5.

## M4. Data do tratamento: avisos de depósito (sugerido)

Os avisos de depósito do Diário Oficial dão a data em que o patrocínio entrou:
- 386 depósitos de 2022 a 2026;
- casam com 20 dos 48 termos do Portal em 2022 e com 78 dos 96 em 2025;
- mediana de 30 a 48 dias depois da "data do processo".

A janela fixa do resultado de H5 pode começar no depósito, e não na validação. Os 69 depósitos de 2026 antecipam o
ano que o Portal ainda não lista. No Quadro 4, "data de cada repasse" passa a ter cobertura declarada.

## M5. Chave de ligação (obrigatório; coincide com R3 P1)

A §5.3 diz: "o Portal da Transparência o traz para quem captou, e a SECULT, para os demais, por pedido de acesso à
informação". Os avisos de habilitação do Diário Oficial trazem o CNPJ, e, somados ao Portal, cobrem 385 dos 463
habilitados (83%), com concordância de 79 em 81 onde as duas fontes se sobrepõem. A LAI fica para os 17% restantes e
para os não habilitados. A mudança é de uma oração e tira da limitação da conclusão o "medida por nome de proponente"
para a maior parte dos casos.

## M6. Notação (conferida)

O Quadro 3 usa EMPT e "efeito local", como os slides (EMP, EMPT, EMPNT). A decomposição da diferença simples de
médias, na §5.1, segue a dos slides (efeito médio + viés de seleção + efeitos heterogêneos). Nada a mudar.
