# Stage 3': verificação das correções da rodada 2

- **Manuscrito revisado:** `artigo/rascunho-artigo.md`, sha256 `b1ed5ad1…d2f8407`.
- **Versão LaTeX:** `artigo/latex/artigo.tex`, sha256 `94a20ba8…27b8b3cc`, 15 páginas.
- **Base de comparação:** a versão revisada na rodada 2 (sha256 `6b278d2d…26bcaf24`) e o roteiro de
  `06-decisao-editorial.md`.
- **Data:** 24/09/2026.

## Como foi feita

Cada item do roteiro foi conferido contra o texto revisado, com o trecho que o atende e, quando há número, com a
checagem correspondente em `artigo/auditoria/checar_dados.py`.

O contrato de re-review do ARS (três portões, pacote de evidências e decisão dos autores por item) não foi executado.
O mesmo modelo revisou e reescreveu o texto, então vale a mesma divulgação de risco de erro correlacionado da
rodada 2 (`00-configuracao-e-proveniencia.md`). Por isso o veredito de cada item se apoia no texto citado e nas
checagens reexecutáveis, e não na memória da revisão.

## Revisões obrigatórias

| Item | Veredito | Evidência no texto revisado |
| --- | --- | --- |
| RV-1 | Atendido | Quadro 3 (H1b): "*Y*(0) maior entre os escolhidos, viés de seleção positivo, e a comparação superestima o EMPT; efeito menor onde ela escolhe puxa no sentido oposto em relação ao efeito médio" |
| RV-2 | Atendido | §5.2 (H1b): "6 dos 11 recusados em 2023 e 12 dos 21 recusados em 2024 captaram no ano seguinte: a comparação mede o efeito de receber agora, não o de receber"; resultado datado; instrumento com primeiro estágio de 41%. Tabela 2: "32 recusados × 32 validados". Checagens N24, N30, N31, N42 |
| RV-3 | Atendido | "ordem de recebimento e validação" (Resumo); §4.2: "Nenhuma norma lida fixa a ordem de validação"; datas de 2025 (N33, N34, N43); cartão H2b da Figura 1 regenerado. Não resta "ordem de chegada" no texto nem na figura |
| RV-4 | Atendido | §5.2: "diferenças em diferenças exigiriam o proponente-ano como unidade, com resultados antes e depois (agenda do Mapa Cultural, SALIC)"; os 95 expirados "pareados … sob seleção nos observáveis" |
| RV-5 | Atendido | §5.3: 79% e 78% sem município; 257 coletivos em 52 municípios; 2.389 agentes nos 71 (N38, N39). Tabela 2 com *J*, *N*, m̄ e *cv* observados (N25, N26) |
| RV-6 | Atendido | Quadro 2: "Não assegurada pelo desenho" em H2a e H2b; síntese da §4.2 deriva a premissa do propósito ("Para desconcentrar o financiamento, algo na cadeia precisaria dirigir recursos…"); a evidência "95 de 293" saiu do Quadro 2 |
| RV-7 | Atendido | §5.2 (H3): a oferta "cobre a documentação (CNPJ, certidões) e a busca de patrocínio…; dois braços sorteados separam os dois atritos"; Quadro 3 (H3) e cartão H3 da figura ajustados |
| RV-8 | Atendido | §6: "A adicionalidade (H1b) é a que mais importa e a menos respondível … receber × não receber exige resultado datado e a fila de termos com as datas"; Resumo: "A adicionalidade é a mais difícil" |
| RV-9 | Atendido em parte | Autoria preenchida (Felipe Carvalho Souza Santos). A declaração de IA virou documento separado (`artigo/declaracao-uso-ia.md`), no singular; falta adequá-la ao modelo da disciplina, que o autor tem em mãos |
| RV-10 | Atendido | §1: "resultados de pesquisa sobre ela foram apresentados pela SECULT no evento Cultura em Dados, em 2026 (SECULT, 2026d)". A afirmação se limita ao título da página oficial; a marca `[VERIFICAR]` saiu |

## Revisões sugeridas

| Item | Veredito | Evidência ou motivo |
| --- | --- | --- |
| SG-1 | Atendido | §4.1: "H2a e H2b descrevem como o desenho seleciona; H1a e H3 são explicações concorrentes para quem fica de fora; H1b pergunta se o que é financiado é adicional" |
| SG-2 | Atendido | "63 projetos captaram, juntos"; "67% … em 2022-2026"; nota: "463 processos e 467 registros por ciclo" (N41) |
| SG-3 | Atendido | Quadro 3 (H2a): "A captação acompanha o que o parecer registrou? … Associação condicional (descritiva, não causal)" |
| SG-4 | Atendido | "83% contra 52% dos que pediram até R\$ 200 mil, em 2022-2024" (N37) |
| SG-5 | Atendido | §5.2: "O sorteio mudaria a regra de alocação e fica fora do escopo" |
| SG-6 | Atendido | §4.2: "Há duas leituras: marketing cultural já estruturado … ou troca de fonte, que reduz a adicionalidade (H1b)" |
| SG-7 | Atendido | §3: "Sem custo, não há efeito-preço sobre o patrocínio, e restam duas margens…" |
| SG-8 | Atendido | §4.2: "No Funcultura, fundo da própria SECULT, a seleção é comparativa (comissão julgadora de especialistas, selecionados e suplentes), e há oficinas de orientação à inscrição (IJSN, 2021)". Fonte lida no relatório do IJSN coletado pelo relé |
| SG-9 | Atendido em parte | "as avaliações localizadas de leis estaduais via ICMS são descritivas". Outras leis estaduais não entraram, por falta de espaço e de fonte conferida |
| SG-10 | Atendido em parte | §5.3: Lei de Acesso à Informação e alternativa se o pedido for negado. A exceção ao sigilo fiscal (LC 187/2021) não foi citada: não foi conferida |
| SG-11 | Atendido | §5.5: implementação gradual; deslocamento como custo para terceiros; oferta feita pela SECULT |
| SG-12 | Atendido | §6: "publicar a fila de termos, com as datas de protocolo e de validação, inclusive dos recusados" |
| SG-13 | Atendido | Estreantes 59% → 46% → 55% (N35); "difusão territorial desacelerou … restam 14 municípios" (N36); concentração da renúncia "reflete também a do próprio imposto"; "provavelmente os de maior chance" |
| SG-14 | Atendido para o LaTeX | Versão de entrega: PDF do LaTeX, com 15 páginas. A versão Word (16 páginas) ficou de fora por decisão do autor |

## Problemas novos

A revisão final (Stage 4.5) encontrou e corrigiu:
- "os cerca de 100 proponentes habilitados por ciclo" virou "os 53 a 95" (N44);
- uma concordância no parágrafo "Monitoramento".

Nenhum problema novo de método.

## Decisão

**Accept**, com uma pendência do autor: adequar a declaração de IA ao modelo da disciplina. As dez obrigatórias estão
atendidas, a RV-9 em parte, pelo mesmo motivo. Das 14 sugeridas, 11 foram atendidas e 3 em parte, com motivo
registrado.
