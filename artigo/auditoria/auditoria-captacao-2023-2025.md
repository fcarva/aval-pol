# Auditoria da captação de 2023 a 2025

- **Afirmação auditada** (§1, versão até 24/09/2026): "De 2023 a 2025, a captação esgotou o montante de cada ano
  ao centavo; em 2025, 63 projetos captaram, juntos, exatamente R\$ 25.000.000,00."
- **Script:** `artigo/auditoria/auditar_captacao.py`.
- **Saídas:**
  - `auditoria_captacao_anual.csv`
  - `auditoria_captacao_checagens.csv` (75 conferências)
  - `auditoria_captacao_sensibilidade_2025.csv`
- **Resultado:** os números estão certos, mas a frase precisava de uma ressalva. Um dos 63 projetos de 2025 está
  "(Em análise na SEFAZ)" no anexo, e por isso o §1 foi reescrito "só com validados".

## Método

O pipeline (`analise/03f_captados_por_cota.py`) lê só os totais que a SECULT imprime. A auditoria não confia neles.
Ela refaz tudo a partir do texto dos PDFs oficiais (`dados/fontes_web/paginas/`), cuja URL e sha256 conferem com
`dados/fontes_web/manifesto.csv`:

1. localiza cada valor em reais pela coluna em que o `pdftotext -layout` o imprime. Colunas por ano:
   - valor do termo;
   - valor habilitado do projeto, em 2024-2026;
   - total por projeto, em 2022-2023.

   Nenhum "R\$" pode cair fora dessas colunas, e todo termo precisa ter um CNPJ de 14 dígitos.
2. soma os termos e compara a soma com:
   - o total impresso ("TOTAL:" ou "Total Geral Captado");
   - o montante do cabeçalho;
   - o teto das portarias da SEFAZ (`dados/externos/licc_teto_vs_icms.csv`);
   - em 2025, o "Total Captado" de cada cota;
3. conta os projetos pela coluna do projeto. O total por projeto que o anexo reimprime depois de uma quebra de
   página conta uma vez só;
4. cruza 2025, termo a termo (CNPJ e valor), com:
   - a transcrição do licc.gov (`dados/licc/oficial/captados-2025.csv`);
   - `dados/processados/captados_2025.csv` e `aportes_2025.csv`;
   - `analise/tabelas/licc_captados_2025_totais.csv`, `03f_captacao_anual_secult.csv` e `09_cotas_2025_2026.csv`.

## Resultado por ano

| Ano | Teto (portarias SEFAZ) | Montante no anexo | Total impresso | Soma dos termos | Termos | Projetos | Esgotou? |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 2022 | 10.000.000,00 | 15.000.000,00 | 11.539.241,07 | 11.539.241,07 | 47 | 39 | não (fora da frase) |
| 2023 | 15.000.000,00 | 15.000.000,00 | 15.000.000,00 | 15.000.000,00 | 71 | 49 | sim |
| 2024 | 25.000.000,00 | 25.000.000,00 | 25.000.000,00 | 25.000.000,00 | 109 | 72 | sim |
| 2025 | 25.000.000,00 | 25.000.000,00 | 25.000.000,00 | 25.000.000,00 | 95 | 63 | sim, com 1 projeto em análise |
| 2026 | 31.000.000,00 | 31.000.000,00 | 31.512.958,04 | 31.512.958,04 | 120 | 103 | lista passa do teto (inclui termos em análise) |

As 75 conferências batem. Em 2025:
- a transcrição do licc.gov e `aportes_2025.csv` reproduzem os 95 termos do anexo v17 um a um;
- as quatro cotas somam o "Total Captado" impresso.

## O achado: um projeto "em análise" dentro dos "validados"

O anexo de 2025 (versão 17, a última publicada) tem o título "Termos de compromisso de patrocínios validados pela
SEFAZ". Mesmo assim, marca a **13ª Italia Unita** (Secretariado dos Imigrantes Friulanos de Aracruz) como
"(Em análise na SEFAZ)":
- são 4 termos, que somam R\$ 356.135,99;
- sem ela, ficam **62 projetos validados, com R\$ 24.643.864,01**;
- o termo dela recebido em 20/05/2025 é o que completa a cota I (30%).

Nenhum dos .csv estava errado: todos reproduzem o anexo. O que não se sustentava era a palavra "captaram" para os
63.

Sensibilidade das outras estatísticas de 2025 do artigo (`auditoria_captacao_sensibilidade_2025.csv`):

| Estatística | Anexo inteiro | Sem o projeto em análise |
| --- | ---: | ---: |
| Empresas (raiz do CNPJ); estabelecimentos | 26; 46 | 25; 42 |
| Empresas para metade da renúncia | 2 | 2 |
| Maior empresa (distribuidora de energia) | 44% | 45% |
| Energia e gás | 52% | 53% |
| Empresas também incentivadoras da Rouanet; parcela da renúncia | 13; 86% | 12; 86% |

O artigo mantém essas estatísticas sobre o anexo inteiro e diz isso no §1.

## Como refazer à mão

1. Abra os PDFs oficiais:
   - [2023](https://secult.es.gov.br/media/2023/RECURSO%20FINANCEIRO%20CAPTADO%20-%202023.pdf)
   - [2024](https://secult.es.gov.br/media/2024/RECURSO%20FINANCEIRO%20CAPTADO%20-%202024%20%286%29.pdf)
   - [2025](https://secult.es.gov.br/media/2025/RECURSO%20FINANCEIRO%20CAPTADO%20-%202025%20%2817%29.pdf)
2. No topo, confira o "Montante de recursos financeiros disponíveis". No fim da lista de validados, confira
   "TOTAL:" (2023 e 2024) ou "Total Geral Captado" (2025).
3. Em 2025, procure "Em análise" na cota I.
4. Para a soma termo a termo, rode `python artigo/auditoria/auditar_captacao.py`. Ele imprime a tabela acima e
   termina com "75/75 conferências batem", ou lista o que diverge.

## CPFs

Os anexos imprimem o CPF de alguns proponentes pessoa física junto ao nome. `analise/rede/mascarar_cpf.py` troca
cada dígito por "X", preservando o comprimento da linha, que a auditoria usa por coluna. A troca vale para:
- os textos do relé;
- as transcrições e tabelas derivadas;
- toda coleta nova do relé.

O histórico do git mantém as versões anteriores. Os dados brutos do SALIC, base federal aberta, não foram alterados.
