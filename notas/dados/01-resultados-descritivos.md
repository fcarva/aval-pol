# Resultados descritivos da LICC (habilitados 2022-2026 e captados 2025)

> Status: EM CONSTRUÇÃO (gravação incremental). Seções marcadas [PENDENTE] ainda não foram preenchidas.

## 0. Fontes, scripts e convenções

**Dados da política (proveniência oficial, transcritos pelo licc.gov):**

| Arquivo | Conteúdo | Fonte |
| --- | --- | --- |
| `dados/licc/habilitados/habilitados-{2022..2026}.csv` | 467 registros, um por projeto em cada seção "PROJETOS HABILITADOS - ANO X" | Lista única da SECULT, https://secult.es.gov.br/lista-de-projetos-habilitados (coluna `fonte_pagina` = página do PDF; seções 2026 nas p. 1-6, 2025 p. 7-11, 2024 p. 11-18, 2023 p. 18-24, 2022 p. 24-26) |
| `dados/licc/oficial/captados-2025.csv` | 63 projetos que captaram no ano-calendário 2025, 95 termos de patrocínio com CNPJ e valor | Anexo "RECURSO FINANCEIRO CAPTADO - 2025", https://secult.es.gov.br/Media/secult/LICC/RECURSO%20FINANCEIRO%20CAPTADO%20-%202025.pdf |

**Dados externos** (`analise/02_externos.py`, cache bruto em `dados/externos/*.json`): lista dos 78 municípios do ES com código IBGE (API de localidades), população do Censo 2022 (SIDRA t. 4709, v. 93), estimativas 2024-2026 (SIDRA t. 6579, v. 9324), PIB municipal a preços correntes 2021-2023 (SIDRA t. 5938, v. 37, R$ mil; 2023 é o último ano publicado), malha municipal GeoJSON (API de malhas v3). Consolidado em `dados/externos/municipios_es.csv`.

**RMGV (composição legal conferida no texto):** Lei Complementar estadual nº 318/2005, art. 2º: a RMGV é integrada por Cariacica, Fundão, Guarapari, Serra, Viana, Vila Velha e Vitória (PDF oficial lido em 23/09/2026: https://planometropolitano.es.gov.br/Media/comdevit/Legisla%C3%A7%C3%A3o/2005-01-lei318-05.pdf). A data exata da LC aparece como 17/01/2005 no Decreto 1.511-R/2005 e como 18/01/2005 na página de legislação do PDUI [VERIFICAR a data; a composição não muda].

**Scripts (rodar nesta ordem; todos em `analise/`):**

1. `_comum.py`: normalização de texto, Gini, Theil, HHI, CRk, cache das APIs.
2. `02_externos.py`: dados do IBGE e RMGV. Pode rodar antes do 01 (o 01 só usa a lista de municípios, que o `_comum` baixa sozinho).
3. `01_carregar.py`: padroniza, resolve municípios, cria chave de proponente, casa captados→habilitados. Saídas em `dados/processados/` e auditorias em `analise/tabelas/01_*.csv`.
4. `03_descritivas.py`: todas as tabelas `analise/tabelas/03_*.csv`.
5. `04_figuras.py`: figuras `analise/figuras/04_*.png` (300 dpi).

**Convenções que valem para todos os números abaixo:**

- **Unidade.** "Registro" = projeto × seção da lista (467). "Processo" = número de processo distinto (463): quatro processos aparecem nas seções 2025 **e** 2026 (2024-454L8, 2024-7NZLF, 2025-49GXP, 2025-SB2J8), com status divergentes entre as seções em dois deles. Estatística por ciclo usa registros da seção; estatística agregada 2022-2026 usa processos distintos (registro da seção mais recente).
- **"Ciclo" é a seção "ANO X" da lista, não o ano de protocolo.** O prefixo do processo é o ano de protocolo: a seção 2026 tem 74 processos de 2025, 12 de 2026 e 2 de 2024; a seção 2023 tem 61 processos de 2022 (`03_ciclo_x_ano_protocolo.csv`). O significado exato de "ANO X" (exercício de habilitação ou de captação pretendida) não está declarado no documento [VERIFICAR com a SECULT].
- **Ausência não é zero.** Célula vazia fica ausente e cada estatística traz a cobertura (n com dado / n total). Quatro valores de R$ 500,00 na p. 12 (seção 2024: 2024-XDJHX, 2024-VM90J, 2024-B7ZFZ autorizados; 2024-X6HWG total) são tratados como **ausentes**: a versão do PDF atualizada em 10/09/2026, lida por parser (firecrawl) em 23/09/2026, imprime "R$ 500,000,00" (separador malformado) para 2024-VM90J; o transcritor leu 500. Os valores brutos seguem em `valor_*_bruto` (`01_valores_suspeitos.csv`) [VERIFICAR no PDF].
- **Município = "Local de Execução"**, não a sede do proponente (a cota do art. 18, III, da IN 001/2025 exige sede **e** execução fora da RMGV; a sede não é publicada). A célula da fonte vem com quebras de linha misturadas; o resolvedor (i) casa os 78 nomes oficiais do IBGE, do mais longo para o mais curto; (ii) aplica uma tabela explícita de grafias/apelidos (ex.: "Vila Veha", "Cachoeiro" como prefixo único, distritos IBGE São Torquato→Vila Velha e Santa Marta→Ibitirama, "Itaúnas"→Conceição da Barra [VERIFICAR]); (iii) repara 9 transbordamentos de célula entre registros vizinhos e 1 célula com linhas intercaladas (16 registros marcados `flag_municipio_incerto`; `01_municipios_transbordo.csv`). Bairros, "a definir", regiões e locais fora do ES ficam **não resolvidos** (`01_municipios_resolucao.csv`).
- **Valor territorial** só é atribuído quando o registro nomeia **um único local** e ele é município do ES (regra do licc.gov: o rateio entre municípios não é publicado). Presença conta em todos os municípios nomeados.
- **Casamento captados→habilitados:** título normalizado **exato** (minúsculas, sem acento, só letras e números). Título que corresponde a mais de um processo é "ambíguo" e fica fora do resultado principal. Um casamento secundário (desempate por valor autorizado idêntico ao centavo) só aparece em sensibilidade.
- Normas citadas: textos conferidos em `notas/politica/fontes/` (IN SECULT 001/2025; Decreto 5.035-R/2021; Lei 11.246/2021; portarias).


## 1. Evolução anual dos habilitados (2022-2026)
[PENDENTE]

## 2. Status e "conversão" habilitado -> executado
[PENDENTE]

## 3. Enquadramento nas cotas (IN LICC 001/2025, art. 18)
[PENDENTE]

## 4. Valores por projeto e bunching no teto por projeto
[PENDENTE]

## 5. Distribuição territorial
[PENDENTE]

## 6. Proponentes: recorrência, concentração e natureza jurídica
[PENDENTE]

## 7. Captação 2025: projetos e patrocinadores
[PENDENTE]

## 8. Evidências para avaliar o desenho
[PENDENTE]

## 9. Hipóteses
[PENDENTE]

## 10. Limitações e itens [VERIFICAR]
[PENDENTE]
