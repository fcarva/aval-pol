# Relatório de integridade final (Stage 4.5)

- **Artigo:** `artigo/rascunho-artigo.md`, sha256 `b1ed5ad1e34352b8d901ca52b2d84d979744ad76b4a766c4f57bcc364d2f8407`.
- **Versão de entrega:** `artigo/latex/artigo.tex` (sha256 `94a20ba8…27b8b3cc`), compilado em `artigo/latex/artigo.pdf`.
- **Declaração de uso de IA:** separada, em `artigo/declaracao-uso-ia.md` e `artigo/latex/declaracao-ia.tex`.
- **Data:** 24/09/2026. Antecedentes: Stage 2.5 (`relatorio-integridade-stage2.5.md`), revisão da rodada 2 e sua
  verificação (`revisao-stage3-r2/`).

## Veredito: **PASS**, com três notas

| Verificação | Como | Resultado |
| --- | --- | --- |
| Números contra a tabela de origem | `checar_dados.py`: acha o trecho literal no texto e recalcula o número na tabela | **54/54 conferem** (`checagem_dados.csv`) |
| Números sem checagem própria | Varredura de todo número do corpo fora das 54 checagens | 36 ocorrências, classificadas abaixo; 1 imprecisão, corrigida |
| Referências com DOI | `checar_referencias.py`: autores, título, periódico, ano, volume e páginas contra Crossref e OpenAlex | **24/24 conferidas**, sem divergência |
| Referências sem DOI | Conferência à mão (normas no DIO, páginas oficiais, livros, relatórios) | 28; a única nova, IJSN (2021), foi lida no PDF coletado pelo relé |
| Citação ↔ referência | Cruzamento pelo sobrenome do primeiro autor e pelo ano, nos dois sentidos | Nenhuma citação sem referência e nenhuma referência sem citação |
| Afirmações atribuídas a autores | Contexto conferido no resumo ou no texto da fonte | Alcântara *et al.* (2019) e Colombo e Cruz (2023): resumos da Crossref. IJSN (2021): seleção por comissão julgadora, suplentes e oficinas de inscrição (p. 16 e seção 5.2 do relatório). Demais: conferidas no Stage 2.5 |
| Marcas pendentes | Busca por `[VERIFICAR]` no artigo | Nenhuma |
| Coerência entre tabelas | Tamanho da margem de racionamento, cadastro de H3 e poder amarrados às mesmas tabelas | N24 a N26 conferem com `indeferidos_2023_2024.csv` e `07_mapa_quadro_h3.csv` |
| Vocabulário entre figura, quadros e texto | Busca de "ordem de chegada" e "não atendida" | Nenhuma ocorrência no artigo nem na Figura 1 |
| Links | Requisição HTTP a cada endereço do GitHub no .tex (ramo `main`) | 10/10 respondem 200. Os 24 DOIs apontam para doi.org |
| Formato | Compilação XeLaTeX (e teste com pdfLaTeX) | 15 páginas; nenhum glifo ausente; nenhuma linha estourada |

### Números sem checagem própria (varredura)

| Grupo | Exemplos | Situação |
| --- | --- | --- |
| Números de norma | Lei 11.246/2021; Lei 7.000/2001; Dec. 5.035-R/2021; IN 001/2025, arts. 13, 18, 35-36, 37-42 | Conferidos no DIO no Stage 2.5; sem mudança |
| Parâmetros de regra | Crédito de até 100%; limites de 20%, 15%, 10% e 5%; R\$ 500 mil, R\$ 300 mil e R\$ 1 milhão; 35% e 120 dias; cotas de 30%, 10%, 10% e 50% | Conferidos nas normas no Stage 2.5; sem mudança |
| Literatura | 4,5% do PIB per capita (Gomes e Librero-Cano, 2018) | Conferido no Stage 2.5 (fase B) |
| Escolhas de desenho | α = 5%; poder de 80% | Parâmetros da proposta |
| Estrutura | Numeração das seções, código da disciplina, nome do arquivo da figura | Não são afirmações |
| **Imprecisão encontrada** | "os cerca de 100 proponentes habilitados por ciclo" | **Corrigido** para "os 53 a 95" e acrescentada a checagem N44 |

## Notas

1. **SECULT (2026d).** A página oficial existe: o título e a URL aparecem em duas buscas, e há uma segunda página
   oficial sobre o mesmo evento. O corpo, porém, não abriu na coleta. A frase do artigo se limita ao que o título
   sustenta, sem data, conteúdo nem autoria do estudo.
2. **Espaçamento das referências.** As referências estão separadas por 3 pt, não por uma linha em branco como pede a
   ABNT NBR 6023. Seguir a norma à risca levaria o artigo a 16 páginas.
3. **Word.** A versão Word (`artigo/rascunho-artigo.docx`) não foi atualizada com as tabelas abertas nem com os links
   e tem 16 páginas. Por decisão do autor, a entrega é o PDF do LaTeX.

## Mudanças desde o Stage 2.5 que afetam a integridade

- **Números novos com proveniência:**
  - reentrada dos recusados (`analise/09_racionamento_2023_2026.py`; transcrição conferida contra os totais dos
    anexos: R\$ 4.176.644,33 e R\$ 8.799.851,49);
  - cotas de 2025 e 2026, com as quatro cotas de cada ano somando exatamente o total impresso;
  - cadastro do Mapa Cultural por município (`analise/07_hipoteses_h1_h3.py`).
- **Referências retiradas:**
  - Brooks (2004) e Schuster (2006), por espaço;
  - SECULT ([202-]), com a frase que a citava.
- **Referência acrescentada:** IJSN (2021).
- **Errata da revisão:** 6 de 11, não 7; 38 termos em 32 projetos (`revisao-stage3-r2/06-decisao-editorial.md`).
