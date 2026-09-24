# Decisão editorial — Stage 3, rodada 1

- **Manuscrito**: `artigo/rascunho-artigo.md`, sha256 `99ea68053bbf…5a0834`
- **Data**: 24/09/2026 · **Modo**: `full`, sem contrato de sprint executado (critérios qualitativos,
  `references/editorial_decision_standards.md` § 0)
- **Proveniência do painel**: `00-configuracao-e-proveniencia.md` (artefato `review_panel_provenance.json`, replay PASS).
  Papéis separados: sim. Contextos separados, cegueira às saídas dos pares e diversidade de modelo, provedor e humano: não.
  Independência não computada. Divulgação obrigatória: "All model-executed review seats used one model family; role
  separation does not remove correlated-error risk." O mesmo modelo redigiu o rascunho; há risco de autorrevisão.

## Decisão: **Major Revision**

As recomendações (EIC Minor, R1 Major, R2 Minor, R3 Minor) caem na linha "Minor-to-Major, depende dos problemas" da
matriz. Decide pelos problemas: os itens do R1 e os dois MAJOR do advogado do diabo exigem reestruturar definições do
desenho D1 e reformular a conclusão central da avaliação de desenho, o que o critério de Minor Revision exclui. Nenhum
problema é fatal: os dados necessários já estão no repositório, e as análises pedidas são descritivas. Pelo volume, a
revisão é de dias, não de semanas.

## Problemas que bloqueiam (ordem de origem)

| Ref. | Problema | Origem | Âncora | Item do roteiro |
| --- | --- | --- | --- | --- |
| B1 | Unidade de análise, identificação do proponente (199 × 172), data do tratamento e grupo "ainda não tratado" do D1 | R1 (W1, W2) | `text: §5.3 "de 199 proponentes"` | REV-1, REV-2 |
| B2 | Conclusão central atribui à escolha do patrocinador a concentração medida na habilitação; explicações alternativas não discutidas | DA (DA-1, DA-2) | `text: §6 "se sustenta mal"` | REV-5 |
| B3 | Declaração de uso de IA provisória e aquém do uso real; autoria em branco | EIC (W3); R3 subscreve | `text: Declaração "[MODELO A CONFERIR"` | REV-6 |

## Consenso e divergências

- **Consenso** (todos os assentos): o artigo cumpre a estrutura exigida, a avaliação de desenho é bem documentada e as
  recomendações de gestão ficam dentro do escopo. Ninguém pediu redesenho do mecanismo.
- **Corroboração**: R1 (W3) e DA (caminhos ignorados) apontam, por ângulos diferentes, os termos indeferidos por
  esgotamento do teto como evidência subaproveitada. R3 (W3) e DA (partes interessadas) apontam a ausência do público.
- **Divergência**: o EIC recomenda Minor por olhar só forma e escopo; o R1, Major por olhar o desenho. Arbitragem
  pelo critério "evidência primeiro": os problemas do R1 estão ancorados em recálculo com os dados (172 proponentes;
  EMD com ρ = 0,2 de 0,39 para 0,41 e de 0,45 para 0,47) e nas regras das instruções de 2023-2024; prevalecem.
- **Advogado do diabo**: nenhum CRITICAL. DA-1 e DA-2 (MAJOR) foram validados pelo sintetizador com os números do
  próprio artigo (67% é do valor habilitado; a execução é 68% na RMGV e 63% no interior) e entram como bloqueio B2.

## Revisões obrigatórias

| Item | O que fazer | Origem |
| --- | --- | --- |
| REV-1 | Usar a chave canônica de proponente em `05_poder_mde.py` (172 proponentes, m̄ = 1,70, cv = 0,75); refazer a Tabela 2 e os números do texto e do resumo (faixa do EMD); definir o tratamento no nível do proponente (primeira captação) e dizer como entram os 24 proponentes mistos | R1-W1 |
| REV-2 | Datar o tratamento pelo ano do termo validado nos anexos de captação 2022-2024 (ou pelo extrato de repasse); limitar os "ainda não tratados" a projetos de 2022-2024; registrar a intensidade (captado ÷ autorizado) | R1-W2 |
| REV-3 | Um parágrafo com a comparação entre termos validados pouco antes do esgotamento e termos indeferidos (2023-2024), como desenho complementar ou de robustez, com as limitações (n ≈ 30 termos; ordem de validação a confirmar); considerar trocar pelo desenho municipal para caber no limite | R1-W3 |
| REV-4 | Acrescentar resultados na margem extensiva (vínculo formal; CNPJ ativo) e resultados disponíveis antes da RAIS; dizer quando a RAIS permitirá a primeira estimação | R1-W4 |
| REV-5 | Separar, na seção 4.2 e na conclusão, o que ocorre na habilitação do que ocorre na captação; discutir as explicações alternativas (patrocínio pré-acordado; capacidade dos recorrentes; oferta de projetos no interior); se possível, duas tabelas simples já calculáveis — conversão por faixa de valor dentro de RMGV/interior e conversão por recorrência dentro da faixa de valor; reescrever o veredito de "se sustenta mal" para o que a evidência mostra | DA-1, DA-2 |
| REV-6 | Preencher a autoria; obter o modelo de declaração da disciplina; declarar com precisão o papel da IA (análise, programação, redação, auditoria) e o que os autores revisaram e decidiram | EIC-W3 |
| REV-7 | Parágrafo curto com duas ou três leis estaduais de incentivo via ICMS, conferidas na fonte | R2-W1 |

## Revisões sugeridas

| Item | O que fazer | Origem |
| --- | --- | --- |
| SUG-1 | Atualizar o resumo (anexos de 2022-2026; racionamento também pela ordem de validação; indeferimentos) | EIC-W1 |
| SUG-2 | Datar o fluxo da abertura da seção 2 | EIC-W2 |
| SUG-3 | Cortar redundâncias para caber nas 15 páginas (Tabela 1 × §4.2; Quadro 1 × parágrafo seguinte) | EIC-W4 |
| SUG-4 | Traduzir o EMD em unidades naturais; dizer o que o EMPT mede sob racionamento | R1-W5, R1-W6 |
| SUG-5 | Comparar com o Funcultura; explicitar a diferença de dedução em relação à Rouanet | R2-W2, R2-W3 |
| SUG-6 | "Não passa pelo lado da despesa do orçamento"; citar a obrigação legal de divulgação no Portal da Transparência | R3-W1, R3-W2 |
| SUG-7 | Declarar que o acesso do público não é mensurável com o que se publica | R3-W3 |
| SUG-8 | Dar a faixa de conversão por ciclo (não só 2024); medir a concentração de patrocinadores também em 2022-2024; corrigir "uma única decisão administrativa" (a RAIS identificada exige convênio) | DA-3, DA-4, DA-5 |

## Observação para o Stage 4.5 (integridade final)

O número de proponentes (199 × 172) passou pela checagem de dados do Stage 2.5 porque o texto batia com a tabela de
poder, que por sua vez usava outra chave. A checagem final deve conferir também a consistência entre tabelas
(mesma população, mesma chave), não só texto contra tabela.

## Pareceres completos
`01-eic-adequacao.md`, `02-r1-metodologia.md`, `03-r2-dominio.md`, `04-r3-perspectiva.md`, `05-da-advogado-do-diabo.md`.
