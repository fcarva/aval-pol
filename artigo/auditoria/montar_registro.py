"""Monta o registro de afirmações (ARS claim-registry/1.0) de artigo/rascunho-artigo.md.

Cada afirmação é marcada por um trecho inicial e um final do texto; o script acha o intervalo,
converte em bytes e grava artigo/auditoria/claim_registry.json, amarrado ao sha256 do rascunho.
Todas as afirmações registradas são verificadas (selection_tier = "ALL"); high_impact_basis indica
as que pesam na conclusão. A lista é extração semântica feita à mão: não prova completude.

Uso: python artigo/auditoria/montar_registro.py
Depois: python ferramentas/academic-research-skills/scripts/claim_registry_coverage.py \
          --draft artigo/rascunho-artigo.md --registry artigo/auditoria/claim_registry.json \
          --output artigo/auditoria/claim_registry_coverage.json
"""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

AUD = Path(__file__).resolve().parent
ART = AUD.parent / "rascunho-artigo.md"
SAIDA = AUD / "claim_registry.json"

Q, CA, T, CAU, O = "quantitative", "categorical", "trend", "causal", "other_factual"
HC, NU, CS, MC, DI = "headline_conclusion", "numerical", "causal", "methods_critical", "disputed"

# (id, seção, início, fim, tipos, referências, bases de alto impacto)
AFIRMACOES = [
    ("C01", "Resumo", "a política não declara problema", "metas nem indicadores", [CA], ["esp2021a", "esp2021b"], [HC]),
    ("C02", "Resumo", "que a demanda habilitada supera", "pelas empresas patrocinadoras", [Q, CA], ["secult2026b"], [HC, NU]),
    ("C03", "Resumo", "que a captação favorece projetos", "atribuível a um município", [Q, CA], ["secult2026b"], [HC, NU]),
    ("C04", "Resumo", "duas empresas respondem", "renúncia de 2025", [Q], ["secult2026b"], [HC, NU]),
    ("C05", "Resumo", "mostramos que o universo disponível", "0,45 desvio-padrão.", [Q], [], [HC, NU, MC]),
    ("C06", "1 Introdução", "Em 2021, o Espírito Santo criou", "(SECULT, [202-]).", [CA], ["secult202x"], []),
    ("C07", "1 Introdução", "A Lei estadual nº 11.246/2021 incluiu", "(ESPÍRITO SANTO, 2021a).", [CA], ["esp2021a"], []),
    ("C08", "1 Introdução", "A Lei de Incentivo à Cultura Capixaba, como", "(459 com valor publicado).", [Q, T], ["esp2021b", "secult2026b"], [NU]),
    ("C09", "1 Introdução", "De 2023 a 2025, a captação esgotou o montante de cada ano", "R\\$ 25.000.000,00.", [Q], ["secult2026c"], [NU, HC]),
    ("C10", "1 Introdução", "O setor cultural capixaba é pequeno", "(IBGE, 2025).", [Q], ["ibge2025"], [NU]),
    ("C11", "1 Introdução", "Em 2021, 95% da população", "(IBGE, 2022).", [Q], ["ibge2022"], [NU]),
    ("C12", "1 Introdução", "Primeiro, é gasto público sem passar", "(Tabela 1).", [Q], [], [NU]),
    ("C13", "1 Introdução", "Segundo, quem decide o destino", "(SILVA, 2017; DEKKER; RODRIGUES, 2019).", [CA], ["silva2017", "dekker2019"], []),
    ("C14", "1 Introdução", "Terceiro, a política é nova", "aos quais este artigo não teve acesso.", [CA], ["secult2026d"], [DI]),
    ("C15", "2 Caracterização", "O proponente, pessoa jurídica", "inscreve o projeto na SECULT.", [CA], ["esp2021b"], []),
    ("C16", "2 Caracterização", "A empresa deposita o valor", "Não há contrapartida financeira da empresa.", [CA], ["esp2021b"], [MC]),
    ("C17", "2 Caracterização", "A segunda é a **instabilidade**", "(SECULT, 2024b; 2025b).", [CA, T], ["secult2024b", "secult2025b"], []),
    ("C18", "2 Caracterização", "Nas instruções de 2023 e 2024, a comissão habilitava", "2024a, arts. 32-36).", [CA], ["secult2023", "secult2024a"], [MC]),
    ("C18b", "2 Caracterização", "Em 2025 a ordem se inverteu", "(SECULT, 2025a, arts. 41-45).", [CA], ["secult2025a"], [MC]),
    ("C18c", "2 Caracterização", "Desde maio de 2025, o proponente tem 120 dias", "(SECULT, 2025b).", [CA], ["secult2025b"], [MC]),
    ("C19", "2 Caracterização", "A terceira é a **pouca informação publicada**", "qualquer indicador de resultado.", [CA], ["secult2026b"], [MC]),
    ("C20", "3 Revisão", "Feld, O'Hare e Schuster (1983) chamaram", "que servem a públicos diferentes.", [CA, Q], ["feld1983", "schuster2006", "brooks2004"], []),
    ("C21", "3 Revisão", "A justificativa econômica usual", "(THROSBY, 1994).", [CA], ["baumol1966", "throsby1994"], []),
    ("C22", "3 Revisão", "Os estudos documentam concentração regional", "(BELEM; DONADONE, 2013).", [CA], ["silva2017", "guimaraes2020", "teixeira2024", "costa2017", "belem2013"], []),
    ("C23", "3 Revisão", "Dekker e Rodrigues (2019) concluem", "qual falha de mercado ela corrige.", [CA], ["dekker2019"], []),
    ("C24", "3 Revisão", "O Tribunal de Contas da União recomendou", "(BRASIL, 2016).", [CA], ["tcu2014", "tcu2016"], [MC]),
    ("C25", "3 Revisão", "Silva (2017) oferece o contraponto", "no acesso da população.", [CA], ["silva2017"], []),
    ("C26", "3 Revisão", "Os motivos das empresas vão além", "(O'HAGAN; HARVEY, 2000).", [CA], ["ohagan2000"], []),
    ("C27", "3 Revisão", "Não localizamos avaliação causal", "de incentivo cultural no Brasil.", [CA], [], [DI]),
    ("C27b", "3 Revisão", "Para leis estaduais via ICMS, os estudos", "(TEIXEIRA *et al.*, 2021).", [CA], ["teixeira2021"], []),
    ("C28", "3 Revisão", "As avaliações com adoção escalonada", "(THOM, 2018; BUTTON, 2019; BRADBURY, 2020).", [CA, CAU], ["thom2018", "button2019", "bradbury2020"], [CS]),
    ("C29", "3 Revisão", "Com grandes eventos, os resultados variam", "MONGARDINI, 2020).", [CAU], ["gomes2018", "bronzini2020"], [CS]),
    ("C30", "3 Revisão", "Sobre a interação entre recurso", "O'HARE, 2004).", [CAU], ["smith2007", "borgonovi2004"], [CS]),
    ("C31", "3 Revisão", "E os desenhos críveis exploram", "com cidades candidatas.", [CA], ["gomes2018"], [MC]),
    ("C32", "4.2 Avaliação", "O decreto declara na ementa um objetivo de produto", "(ESPÍRITO SANTO, 2021b, art. 3º).", [CA], ["esp2021b"], [HC]),
    ("C33", "4.2 Avaliação", "Não há meta, magnitude esperada", "(BRASIL, 2014).", [CA], ["barros2017", "tcu2014"], [HC]),
    ("C34", "4.2 Avaliação", "O valor autorizado de cada ciclo foi", "montante de cada ano ao centavo.", [Q], ["secult2026b", "secult2026c"], [NU, HC]),
    ("C34b", "4.2 Avaliação", "Em 2023 e 2024, a SECULT ainda indeferiu", "(SECULT, 2026c).", [Q], ["secult2026c"], [NU, HC]),
    ("C35", "4.2 Avaliação", "O excesso de demanda é racionado", "quase dobrou.", [Q, T, CA], ["secult2026b"], [NU]),
    ("C36", "4.2 Avaliação", "Primeiro, a captação favorece projetos maiores", "(Figura 1a).", [Q], ["secult2026b"], [NU, HC]),
    ("C37", "4.2 Avaliação", "A parcela de pedidos no teto exato triplicou", "ao custo do projeto.", [Q, T, CAU], ["secult2026b"], [NU, CS]),
    ("C38", "4.2 Avaliação", "Segundo, a captação favorece quem já passou", "ficam com 47% do valor autorizado.", [Q], ["secult2026b"], [NU, HC]),
    ("C39", "4.2 Avaliação", "Terceiro, o financiamento vem de poucas empresas", "por 52%.", [Q], ["secult2026b"], [NU, HC]),
    ("C40", "4.2 Avaliação", "O limite por patrocinador, proporcional", "em valor absoluto.", [CA], ["esp2021b"], []),
    ("C41", "4.2 Avaliação", "A RMGV tem 49% da população", "(Figura 1b).", [Q], ["secult2026b"], [NU, HC]),
    ("C41b", "4.2 Avaliação", "A concentração nasce sobretudo em quem é habilitado", "ficou na RMGV.", [Q], ["secult2026b"], [NU, HC]),
    ("C42", "4.2 Avaliação", "O Gini do valor entre os 78", "em cinco ciclos.", [Q], ["secult2026b"], [NU]),
    ("C43", "4.2 Avaliação", "A reserva de 10% do teto para projetos fora", "está dentro dos grupos.", [Q], ["secult2025a"], [NU, HC]),
    ("C44", "4.2 Avaliação", "O padrão é o inverso do gasto municipal", "com dado no SICONFI).", [Q], [], [NU]),
    ("C45", "4.2 Avaliação", "A maior reserva do teto, 30%", "não descumprimento apurado.", [CA], ["secult2025a", "tcu2016"], [DI]),
    ("C46", "4.2 Avaliação", "O que a SECULT publica cobre", "por cota desde 2025).", [CA], ["secult2026b", "secult2026c"], [MC]),
    ("C46b", "4.2 Avaliação", "Não há chave que ligue", "em 2024 e em 2025.", [CA], [], [MC]),
    ("C46c", "4.2 Avaliação", "Em 2025, as reservas I e IV", "107% (SECULT, 2026c).", [Q], ["secult2026c"], [NU, HC]),
    ("C46d", "4.2 Avaliação", "Como o art. 18 manda aplicar a cota geral", "não o cumprimento da norma.", [CA], ["secult2025a"], [HC]),
    ("C47", "5.2 Identificação", "A regressão descontínua não se aplica", "dos próprios interessados.", [CA], ["secult2023", "secult2024a", "secult2025a"], [MC]),
    ("C48", "5.2 Identificação", "A janela se restringe a 2022-2024", "resolvidos no ciclo 2025).", [CA], ["secult2023", "secult2024a", "secult2025b"], [MC]),
    ("C48b", "5.2 Identificação", "A instrução de 2022 não foi lida", "antes da coleta.", [CA], [], [MC]),
    ("C49", "5.2 Identificação", "Com tratamento em datas diferentes", "(GOODMAN-BACON, 2021).", [CA], ["goodmanbacon2021"], [MC]),
    ("C50", "5.2 Identificação", "O estudo de evento testa tendências", "das tendências paralelas.", [CA], ["rambachan2023"], [MC]),
    ("C51", "5.2 Identificação", "O primeiro é um **diferenças em diferenças municipal**", "como resultado.", [Q], ["secult2026b"], [NU, MC]),
    ("C52", "5.2 Identificação", "Isso não altera a regra de alocação", "pode captar no lugar de outro.", [CA], ["angrist1996"], [MC]),
    ("C53", "5.3 População", "A população são os 305 projetos", "de 199 proponentes.", [Q], ["secult2026b"], [NU, MC]),
    ("C54", "5.3 População", "Os anexos publicados não trazem o CNPJ", "porque a inscrição o exige.", [CA], ["secult2025a"], [MC]),
    ("C55", "5.4 Poder", "Usamos a fórmula do efeito mínimo", "(DJIMEU; HOUNDOLO, 2016):", [CA], ["djimeu2016"], [MC]),
    ("C56", "5.4 Poder", "em que $n$ = 293 projetos", "(ELDRIDGE; ASHBY; KERRY, 2006).", [Q], ["eldridge2006"], [NU, MC]),
    ("C57", "5.4 Poder", "O universo disponível detecta, portanto", "conforme o cenário.", [Q], [], [NU, HC]),
    ("C58", "5.4 Poder", "Com poder de 17%, a estimativa", "(GELMAN; CARLIN, 2014).", [Q], ["gelman2014"], [NU]),
    ("C59", "6 Conclusão", "A avaliação do desenho, feita com os dados", "se sustenta mal.", [CA], [], [HC]),
    ("C60", "6 Conclusão", "A captação favorece projetos que pedem o teto", "serviços regulados.", [Q, CA], ["secult2026b"], [HC]),
    ("C61", "6 Conclusão", "As reservas do art. 18 foram preenchidas", "desigualdade territorial.", [CA], ["secult2025a"], [HC]),
    ("C62", "6 Conclusão", "A proposta de avaliação de impacto aproveita", "mesmo filtro de mérito.", [CA], [], [HC, MC]),
    ("C63", "6 Conclusão", "A conversão habilitado-captou usa", "cobre 74% do valor.", [Q], [], [NU]),
    ("C64", "5.2 Identificação", "As regras da política determinam o método", "(GERTLER *et al.*, 2018).", [CA], ["gertler2018"], [MC]),
    ("C65", "5.2 Identificação", "A lógica é a dos candidatos não escolhidos", "mesmo filtro de mérito.", [CA], ["gomes2018"], [MC]),
    ("C66", "5.2 Identificação", "Por isso usamos o estimador de Callaway", "histórico no SALIC.", [CA], ["callaway2021", "santanna2020"], [MC]),
    ("C67", "5.4 Poder", "| R² = 0,3, ρ = 0 | 0,29 | 0,34 |", "| R² = 0,3, ρ = 0 | 0,29 | 0,34 |", [Q], [], [NU]),
    ("C68", "5.4 Poder", "| R² = 0,5, ρ = 0 | 0,25 | 0,29 |", "| R² = 0,5, ρ = 0 | 0,25 | 0,29 |", [Q], [], [NU]),
    ("C69", "5.4 Poder", "| R² = 0,5, ρ = 0,2 | 0,28 | 0,32 |", "| R² = 0,5, ρ = 0,2 | 0,28 | 0,32 |", [Q], [], [NU]),
    ("C70", "5.4 Poder", "No desenho municipal, o EMD está", "(MCKENZIE, 2012).", [Q, CA], ["mckenzie2012"], [MC]),
    ("C71", "4.2 Avaliação", "| Patrocinadores (2025) | Empresas (raiz", "| 26; 44% |", [Q], ["secult2026b"], [NU]),
    ("C72", "2 Caracterização", "Fonte: elaboração própria a partir das normas", "2026a).", [O], ["esp2021a", "esp2021b", "secult2025a", "secult2026a"], []),
    ("C73", "4.1 Teoria da mudança", "Fonte: elaboração própria, com base em Gertler", "nas normas do Quadro 1.", [O], ["gertler2018", "white2017"], []),
    ("C74", "4.2 Avaliação", "Fonte: elaboração própria com base em SECULT (2026b; 2026c), portarias", "SICONFI.", [O], ["secult2026b"], []),
    ("C76", "1 Introdução", "[^teto2022]: Para 2022", "entre os dois valores.", [Q, CA], ["secult2026c"], [NU, DI]),
    ("C77", "4.2 Avaliação", "| | Captado / montante do ano", "100%; 100%; 100% |", [Q], ["secult2026c"], [NU]),
    ("C78", "4.2 Avaliação", "| | Termos de patrocínio indeferidos", "28%; 35% |", [Q], ["secult2026c"], [NU]),
    ("C79", "Referências", "Vitória: SECULT, [202-].", "Vitória: SECULT, [202-].", [O], ["secult202x"], []),
    ("C75", "4.2 Avaliação", "Fonte: elaboração própria com base em SECULT (2026b) e IBGE.", "Fonte: elaboração própria com base em SECULT (2026b) e IBGE.", [O], ["secult2026b"], []),
]


def main() -> int:
    raw = ART.read_bytes()
    texto = raw.decode("utf-8")
    claims, erros = [], []
    for cid, secao, ini, fim, tipos, refs, bases in AFIRMACOES:
        i = texto.find(ini)
        if i < 0 or texto.find(ini, i + 1) >= 0:
            erros.append(f"{cid}: início {'ausente' if i < 0 else 'ambíguo'}: {ini!r}")
            continue
        j = texto.find(fim, i)
        if j < 0:
            erros.append(f"{cid}: fim ausente: {fim!r}")
            continue
        j += len(fim)
        trecho = texto[i:j]
        sb, eb = len(texto[:i].encode("utf-8")), len(texto[:j].encode("utf-8"))
        c = {"claim_id": cid, "claim_text": trecho, "draft_span": {"start_byte": sb, "end_byte": eb},
             "claim_kinds": tipos, "ref_slugs": refs, "writer_anchors": [], "paper_section": secao,
             "selection_tier": "ALL"}
        if bases:
            c["high_impact_basis"] = bases
        claims.append(c)
    if erros:
        print("\n".join(erros))
        return 1
    reg = {"schema_version": "claim-registry/1.0", "draft_raw_sha256": hashlib.sha256(raw).hexdigest(), "claims": claims}
    SAIDA.write_text(json.dumps(reg, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"{len(claims)} afirmações → {SAIDA.name} (rascunho {reg['draft_raw_sha256'][:12]}…)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
