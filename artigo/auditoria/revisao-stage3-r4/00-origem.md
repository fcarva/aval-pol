# Stage 3, rodada 4: origem e escopo

- **Pedido do autor (27/09/2026):** "fazer uma super revisão, auditoria e checagem, ver pontos de melhoria, tanto no
  desenho do experimento, checar os dados e colocar em prova com o material, usar o modo de reflexão full mode".
- **Manuscrito revisto:** `artigo/rascunho-artigo.md`, sha256
  `15d70ff9ae9b93739b5861e1e217145059ffd36b8e0b22f7279f36c4fcecd64a`, commit `898ac9c`.
- **Versão LaTeX:** `artigo/latex/artigo.tex`, sha256 `4a39742c…afb172890`, 15 páginas.
- **Material da disciplina:** a pasta local do autor (`C:\Users\DELL\Documents\aval-pol\Material`) não é acessível
  da sessão em nuvem. O confronto usa as sínteses do repositório: `notas/disciplina/01-slides-e-guias.md` (slides de
  teoria da mudança, resultados potenciais, validade, amostragem e poder) e `notas/disciplina/04-itau-magenta-adb.md`
  (Barros e Lima; HM Treasury; White e Raitzer).

## O que esta rodada faz além da r3

A rodada 3 revisou a moldura (H1 a H5). Esta rodada põe o texto à prova em três frentes:

1. **Integridade.** Reexecução das checagens, conferência das afirmações atribuídas a autores e varredura de números
   sem origem.
2. **Método contra o material.** Os cinco passos do J-PAL, a notação de resultados potenciais, as ameaças à validade
   e as regras de amostragem e poder dos slides.
3. **Dados novos, sem LAI.** Os avisos do Diário Oficial (habilitação com CNPJ; depósito do patrocínio com data),
   lidos por `analise/18_dio_avisos_habilitacao.py`. O poder foi recalculado em `analise/19_poder_revisao.py`.

## Integridade (resultado)

| Conferência | Resultado |
| --- | --- |
| `checar_dados.py` | 60/60 |
| `auditar_captacao.py` | 75/75 |
| `checar_referencias.py` | 55 referências; 19 DOIs conferidos, sem divergência; nenhum `[VERIFICAR]` |
| Nomes fora do escopo (financiamento quadrático, Hypercerts, OSO) | 0 ocorrências no corpo do texto; o termo aparece só no título da obra de Ogava *et al.* (2022), na lista de referências. Hitzig e Buterin, Hitzig e Weyl entram como literatura, pela exceção do `CLAUDE.md` |
| CPF no repositório (`mascarar_cpf.py --conferir`) | 0 ocorrências |

### Afirmações atribuídas a autores (conferidas no texto ou no resumo da fonte)

| Citação | Afirmação no artigo | Onde conferida | Situação |
| --- | --- | --- | --- |
| Ogava *et al.* | concentração dos patrocínios; sem relação entre número de doadores e parcela recebida | texto, l. 532-534 e 558 | confere |
| TCU (BRASIL, 2016) | critério de adicionalidade para renúncias | acórdão, l. 15 | confere |
| Thom (2018) | crédito transferível com efeito pequeno no emprego e nulo em salários e PIB | resumo (Crossref) | confere |
| Teixeira *et al.* (2021) | leitura da Rouanet | resumo | confere |
| Dekker e Rodrigues (2019) | incentivo vai a projetos já bem-sucedidos | resumo | confere |
| Throsby (1994) | bem público, externalidade e bem de mérito | RePEc; `notas/literatura/02-internacional.md` | confere |
| White e Raitzer (2017) | cadeias separadas (p. 21); funil de atrito (Fig. 2.2, p. 23) | `notas/disciplina/04-itau-magenta-adb.md`, l. 504-506 | confere; os slides creditam o funil a White (2013), que o livro reproduz |
| Barros e Lima (2017) | o programa deve declarar resultado e magnitude esperados | idem, l. 140 e 707 (p. 15) | confere |
| Mayne (2015) | premissa em cada elo da cadeia | `notas/desenho/04-…`, l. 17 (DOI 10.3138/cjpe.230) | confere |
| Williams (2020) | mapeamento do mecanismo: premissa × contexto real | `notas/desenho/03-…`, § 3 | confere |

## Dados novos lidos nesta rodada (sem LAI)

| Fonte | O que dá | Resultado |
| --- | --- | --- |
| DIO-ES, "Aviso de resultado… habilitação" | processo, proponente, CNPJ, valor e data | 264 processos com CNPJ. Com o Portal, **385 de 463 habilitados (83%)** têm CNPJ público. Nos 81 processos presentes nas duas fontes, o CNPJ coincide em 79. Ciclos: 2022, 88%; 2023, 86%; 2024, 93%; 2025, 71%; 2026, 72% (`analise/tabelas/18_cobertura_cnpj.csv`) |
| DIO-ES, "Aviso de depósito de patrocínio" | patrocinador, CNPJ, valor do crédito presumido, projeto e data | 386 depósitos (2022-2026), um aviso por parcela. Pelo menos um depósito localizado para 267 dos 325 termos do Portal (82%; 77% do valor): 38 de 48 (2022), 58 de 71 (2023), 89 de 110 (2024) e 82 de 96 (2025). Mediana de 32 a 48 dias entre a "data do processo" e o primeiro aviso. Há 65 depósitos de 2026 sem termo no Portal, que ainda não lista o ano (`18_deposito_x_portal.csv`; ligação por termo em `dados/processados/dio_deposito_x_termo.csv`). Pela Portaria Conjunta SEFAZ/SECULT nº 01-R/2022, arts. 5º e 6º, o crédito só é apropriado depois desse aviso |
| Portal, "data do processo" × recebimento no anexo de 2025 | ordem da fila | 62 termos; a data do processo vem 19 dias depois do recebimento (mediana; de 2 a 377); correlação de postos de 0,91 (`16_data_processo_x_recebimento_2025.csv`) |
