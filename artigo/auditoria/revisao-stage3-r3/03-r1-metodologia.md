# Parecer R1: metodologia e identificação

**Recomendação: revisão maior** (itens M1 e M2; os demais são menores).

## Síntese

A reorganização melhora a identificação de H5: o parâmetro na margem do racionamento e o desfecho em janela fixa
respondem à rodada anterior. O experimento conjunto é a peça nova e a mais promissora, porque é o único desenho que
separa, por sorteio, atributos que nos dados observados andam juntos. Mas ele está subespecificado em população,
recrutamento e ligação com o resultado da política.

## Achados

- **M1 (maior). População e viabilidade do experimento conjunto (linhas 142, 150, 179).**
  - A Tabela 2 calcula o poder com 60 decisores × 12 tarefas (EMD de 7,4 a 13,4 pp).
  - Mas a listagem "parte das 26 patrocinadoras de 2025 e se amplia, com a SEFAZ, aos maiores contribuintes fora do
    Simples Nacional" (linha 150). Isso mistura duas populações: quem escolheu patrocinar e quem poderia. O
    parâmetro muda com a população.
  - Faltam três coisas:
    - quem responde na empresa (marketing, diretoria, relações institucionais);
    - taxa de resposta esperada;
    - o cenário pessimista, que já está calculado em `analise/tabelas/10_poder_conjoint.csv`: com 30 decisores
      × 12 tarefas, o EMD vai de 10,4 a 19,0 pp.
  - Pedido:
    - definir a população-alvo (patrocinadoras reais como população principal; contribuintes elegíveis como
      extensão);
    - reportar a faixa de 30 a 60 decisores;
    - dizer que a escolha declarada tem viés de desejabilidade social (a empresa tende a declarar valor público) e
      que o desenho de escolha forçada entre perfis só o reduz.
- **M2 (maior). Ligação entre H1 e o resultado da política (linhas 131, 142).**
  - O experimento identifica o que pesa na escolha declarada. Não identifica se a escolha orientada por marca
    produz menos bem público.
  - Sem essa ponte, H1 responde a uma pergunta de comportamento da empresa, não de impacto da política.
  - Pedido: uma frase ligando os pesos estimados às escolhas reais e ao resultado de H5, por exemplo comparando
    realização e público dos projetos financiados segundo os atributos que o experimento indicar como decisivos.
    Ou declarar H1 como pergunta de mecanismo, e não de impacto.
- **M3 (menor). H2 com poucos avaliadores (linha 144).**
  - O texto já declara o desenho exploratório (41 pareceristas, de 4 a 20 por área). Falta dizer que a inferência com
    poucos agrupamentos pede erro-padrão robusto a poucos conglomerados.
  - A designação "por ordem de inscrição" é determinística: o balanceamento deve condicionar na posição da fila e
    no período.
- **M4 (menor). H5 com dado público (linha 141).**
  - A margem de 2023-2024 tem 32 × 32 e só detecta efeitos de 28 a 34 pp (Tabela 2).
  - Em 2025 o anexo não lista recusados, e o RD no tempo depende da fila da SEFAZ.
  - O texto diz isso em partes; convém uma frase dizendo que, sem a fila, o produto de H5 é uma comparação de
    robustez, não uma estimativa principal.
- **M5 (menor). H3 sem estimando (linhas 114, 146).** H3 fica fora do Quadro 3, o que é aceitável para uma ponta
  aberta, mas convém nomear o estimando descritivo e o causal:
  - descritivo: parcela dos recursos incentivados gasta em captação, elaboração e divulgação, por porte e por
    patrocinador;
  - causal: o teto de 25% para divulgação em 2025 como tratamento por intensidade, medida pela parcela de
    divulgação antes da regra.
- **M6 (menor). Termos e hipóteses do poder (linha 179).** "Efeito marginal médio" é o AMCE de Hainmueller *et al.*
  (2014). O ρ de 0 ou 0,1 "no decisor" é hipótese e deve ser dito como tal, como o texto já faz para $p_0$.

## Conferências feitas

- EMD do experimento: `10_poder_conjoint.csv`, com o efeito de desenho de 24 perfis e ρ = 0,1:
  $1 + 23 \times 0{,}1 = 3{,}3$, e $7{,}4 \times \sqrt{3{,}3} \approx 13{,}4$. Confere.
- Primeiro estágio da recusa: 0,41, F ≈ 22 (registro da rodada 3, `00-origem-e-resposta.md`). Não é fraco; a
  crítica relevante é à exclusão, e o texto a trata.
