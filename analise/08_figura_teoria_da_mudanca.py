"""08 — Figura da teoria da mudança da LICC (Figura 1 do artigo).

Formato: cadeia de resultados vertical do J-PAL usada nos slides da disciplina (TdM [s.11]; M03 [s.11]), com as
cores por nível do slide (problema, insumos e atividades, produtos, resultados intermediários, resultado final). As
premissas testadas (H1-H3) são marcadas **sobre as setas** a que se referem e explicadas em cartões alinhados à
direita, como os "causal link assumptions" de Mayne (2015). Setas tracejadas marcam elos sem dado público. Decisões
de formato e de design: notas/desenho/04-formatos-e-design-da-teoria-da-mudanca.md.

Paleta: Flexoki, de Steph Ango (licença MIT; https://stephango.com/flexoki; valores conferidos no README de
github.com/kepano/flexoki). Preenchimento no tom 50, contorno no 300, rótulos no 700 para contraste.
Fonte: Inter (SIL Open Font License 1.1), arquivos e licença em analise/fontes/inter/.
Renderização: HTML/CSS no Chromium via Playwright (pip install playwright). O HTML fica salvo para edição.

Conteúdo: notas/desenho/03-teoria-da-mudanca-e-hipoteses.md, § 1. Não lê dados.
Saídas: analise/figuras/08_teoria_da_mudanca.html, .png (300 dpi a 16 cm de largura) e .pdf (vetorial).
Uso: python analise/08_figura_teoria_da_mudanca.py
"""
from __future__ import annotations

from pathlib import Path

from playwright.sync_api import sync_playwright

RAIZ = Path(__file__).resolve().parents[1]
FIG = RAIZ / "analise" / "figuras"
HTML = FIG / "08_teoria_da_mudanca.html"
PNG = FIG / "08_teoria_da_mudanca.png"
PDF = FIG / "08_teoria_da_mudanca.pdf"

LARGURA_CSS = 720            # px de CSS; ocupa 16 cm no artigo
ESCALA = 1890 / LARGURA_CSS  # 1890 px = 16 cm a 300 dpi

# Flexoki (README oficial): 50 = preenchimento, 300 = contorno, 700 = texto de rótulo
C = {
    "base150": "#DAD8CE", "base500": "#878580", "base600": "#6F6E69", "base700": "#575653", "base800": "#403E3C",
    "base950": "#1C1B1A",
    "red50": "#FFE1D5", "red300": "#E8705F", "red700": "#942822",
    "orange50": "#FFE7CE", "orange300": "#EC8B49", "orange700": "#9D4310",
    "yellow50": "#FAEEC6", "yellow300": "#DFB431", "yellow700": "#8E6B01",
    "green50": "#EDEECF", "green300": "#A0AF54", "green700": "#536907",
    "blue50": "#E1ECEB", "blue300": "#66A0C8", "blue700": "#1A4F8C",
    "purple50": "#F0EAEC", "purple400": "#8B7EC8", "purple700": "#4F3685",
}

# Níveis da cadeia: (id, rótulo, sublinha, cor)
NIVEIS = [
    ("prob", "Problema", "", "red"),
    ("ins", "Insumos", "", "orange"),
    ("ent", "Atividades", "entrada", "orange"),
    ("ofe", "Produto", "oferta", "yellow"),
    ("fin", "Atividades", "financiamento", "orange"),
    ("par", "Produtos", "participação", "yellow"),
    ("ri", "Resultados", "intermediários", "green"),
    ("rf", "Resultado", "final", "blue"),
]

# Caixas de cada nível: (id, título, texto, quem decide)
CAIXAS = {
    "prob": [("prob", None, "Baixa e desigual capacidade de financiar a produção e a oferta cultural fora do "
              "circuito já consolidado", None)],
    "ins": [("ins", None, "Teto anual de renúncia de ICMS (imposto que a população deixa de arrecadar) · "
             "SECULT, pareceristas, CAP e SEFAZ · Mapa Cultural", None)],
    "ent": [("a1", "A1 · Inscrição no edital", "on-line, com CNPJ e documentos", "agente cultural"),
            ("a2", "A2 · Parecer e CAP", "parecer técnico e mérito, resultado binário", "SECULT e CAP")],
    "ofe": [("p1", "P1 · Cardápio de projetos habilitados", "autorização para captar por um ano", None)],
    "fin": [("a3", "A3 · Escolha e termo", "a empresa escolhe e compromete o ICMS", "empresa"),
            ("a4", "A4 · Validação no teto", "termos validados até esgotar a cota", "SEFAZ")],
    "par": [("p2", "P2 · Projetos patrocinados", "captação por projeto e empresa", None),
            ("p3", "P3 · Projetos executados", "com contrapartidas de acesso", "proponente")],
    "ri": [("ri1", "RI1 · Bens culturais de acesso público", "gratuidade, acessibilidade, interior", None),
           ("ri2", "RI2 · Quem executa se diversifica", "novos proponentes, interior, emprego", None)],
    "rf": [("rf", None, "Acesso maior e menos desigual da população à cultura, e um setor cultural mais capaz de "
            "se financiar", None)],
}

# Setas: (origem, destino, tracejada, marcador)
SETAS = [
    ("prob", "ins", False, None),
    ("ins", "a1", True, "H3"),
    ("a1", "a2", True, None),
    ("a2", "p1", False, "H2a"),
    ("p1", "a3", False, "H1a"),
    ("a3", "a4", False, None),
    ("a4", "p2", False, "H2b"),
    ("p2", "p3", False, None),
    ("p3", "ri1", True, "H1b"),
    ("p3", "ri2", False, None),
    ("ri1", "rf", False, None),
    ("ri2", "rf", False, None),
]

# Cartões das premissas: (marcador, título, texto)
PREMISSAS = [
    ("H3", "Atrito na entrada",
     "Quem tem projeto de valor público consegue se inscrever (CNPJ, documentos, patrocinador)?"),
    ("H2a", "Qualifica, não prioriza",
     "O parecer decide se o projeto entra; entre os habilitados, quem recebe depende da empresa e da fila."),
    ("H1a", "Escolha da empresa",
     "A empresa escolhe por marca e visibilidade, e não por interesse público?"),
    ("H2b", "Racionamento no teto",
     "Termos com patrocinador recusados ao esgotar o teto; em 2025, a cota de 50% fechou em 28/01."),
    ("H1b", "Adicionalidade",
     "O projeto financiado aconteceria sem a LICC? E chega ao público?"),
]

CSS = """
@font-face { font-family: Inter; font-weight: 400; src: url('../fontes/inter/Inter-Regular.ttf'); }
@font-face { font-family: Inter; font-weight: 500; src: url('../fontes/inter/Inter-Medium.ttf'); }
@font-face { font-family: Inter; font-weight: 600; src: url('../fontes/inter/Inter-SemiBold.ttf'); }
@font-face { font-family: Inter; font-weight: 700; src: url('../fontes/inter/Inter-Bold.ttf'); }
* { box-sizing: border-box; margin: 0; }
html, body { background: #ffffff; }
body { font-family: Inter, sans-serif; color: $base950; -webkit-font-smoothing: antialiased; }
#fig { width: $LARGURApx; padding: 16px 18px 12px; position: relative; }
#grade { display: grid; grid-template-columns: 84px minmax(0, 1fr) 190px; column-gap: 16px; row-gap: 36px;
         position: relative; z-index: 1; }
.rot { grid-column: 1; font-size: 10.5px; font-weight: 600; letter-spacing: .07em; text-transform: uppercase;
       line-height: 1.25; align-self: center; }
.rot small { display: block; font-size: 10.5px; font-weight: 500; letter-spacing: .02em; text-transform: none;
             margin-top: 2px; }
.nivel { grid-column: 2; display: flex; gap: 38px; }
.nivel .caixa { flex: 1 1 0; min-width: 0; }
.caixa { border: 1.3px solid; border-radius: 9px; padding: 9px 12px 10px; display: flex; flex-direction: column;
         justify-content: center; gap: 3px; min-height: 56px; color: $base950; }
.caixa .t { font-size: 12.6px; font-weight: 600; line-height: 1.3; }
.caixa .x { font-size: 12px; line-height: 1.38; color: $base800; }
.caixa.larga .x { font-size: 12.4px; color: $base950; }
.caixa .d { margin-top: 3px; font-size: 10.8px; line-height: 1.3; font-weight: 500; }
.caixa .d b { font-weight: 500; white-space: nowrap; }
.caixa .d span { color: $base700; text-transform: uppercase; letter-spacing: .05em; font-size: 9.6px;
                 margin-right: 4px; white-space: nowrap; }
.rot.red { color: $red700; }       .caixa.red { background: $red50; border-color: $red300; }
.rot.orange { color: $orange700; } .caixa.orange { background: $orange50; border-color: $orange300; }
.rot.yellow { color: $yellow700; } .caixa.yellow { background: $yellow50; border-color: $yellow300; }
.rot.green { color: $green700; }   .caixa.green { background: $green50; border-color: $green300; }
.rot.blue { color: $blue700; }     .caixa.blue { background: $blue50; border-color: $blue300; }
#premissas { position: absolute; top: 0; right: 18px; width: 190px; z-index: 2; }
.cartao { position: absolute; left: 0; width: 190px; border: 1.2px dashed $purple400; border-radius: 9px;
          background: #ffffff; padding: 8px 10px 9px; }
.cartao .ct { font-size: 11.6px; font-weight: 600; color: $purple700; line-height: 1.3; }
.pilula { display: inline-block; font-weight: 700; color: $purple700; background: $purple50;
          border: 1.2px solid $purple400; border-radius: 99px; padding: 0 6px; font-size: 10.6px; line-height: 1.4; }
.cartao .ct .pilula { margin-right: 4px; }
.cartao .cx { margin-top: 4px; font-size: 11.2px; line-height: 1.42; color: $base800; }
svg#setas { position: absolute; left: 0; top: 0; overflow: visible; z-index: 0; }
.marca { position: absolute; transform: translate(-50%, -50%); z-index: 3; }
#legenda { margin-top: 22px; padding-top: 12px; border-top: 1px solid $base150; display: flex; flex-wrap: wrap;
           gap: 10px 26px; font-size: 11px; color: $base700; line-height: 1.4; }
#legenda div { display: flex; align-items: center; gap: 8px; }
#legenda .amostra { width: 34px; height: 0; border-top: 1.6px dashed $base500; }
#legenda .amostra.cheia { border-top-style: solid; }
"""

JS = """
const SETAS = __SETAS__;
const COR = "__COR__";
function desenhar() {
  const fig = document.getElementById('fig'), f = fig.getBoundingClientRect();
  const svg = document.getElementById('setas');
  svg.setAttribute('width', f.width); svg.setAttribute('height', f.height);
  const r = id => { const b = document.getElementById(id).getBoundingClientRect();
    return {l: b.left - f.left, r: b.right - f.left, t: b.top - f.top, b: b.bottom - f.top,
            cx: (b.left + b.right) / 2 - f.left, cy: (b.top + b.bottom) / 2 - f.top}; };
  const NS = 'http://www.w3.org/2000/svg';
  svg.innerHTML = '<defs><marker id="ponta" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" ' +
    'markerHeight="7" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" fill="' + COR + '"/></marker></defs>';
  const marcas = {};
  for (const [a, b, tracejada, m] of SETAS) {
    const A = r(a), B = r(b);
    let d, mx, my;
    if (Math.abs(A.cy - B.cy) < 4) {                       // mesma linha: seta horizontal
      const x1 = A.r + 3, x2 = B.l - 3;
      d = `M${x1},${A.cy} L${x2},${B.cy}`; mx = (x1 + x2) / 2; my = A.cy;
    } else {                                               // entre linhas: vertical ou ortogonal
      const larga = w => w > 300;
      let x1 = larga(A.r - A.l) ? Math.min(Math.max(B.cx, A.l + 24), A.r - 24) : A.cx;
      if (a === 'p3' && b === 'ri1') x1 = A.l + (A.r - A.l) * 0.28;
      const x2 = larga(B.r - B.l) ? Math.min(Math.max(x1, B.l + 24), B.r - 24) : B.cx;
      const y1 = A.b + 3, y2 = B.t - 4, ym = (y1 + y2) / 2;
      if (Math.abs(x1 - x2) < 2) { d = `M${x1},${y1} L${x2},${y2}`; mx = x1; my = ym; }
      else {
        const k = 9, s = x2 > x1 ? 1 : -1;
        d = `M${x1},${y1} L${x1},${ym - k} Q${x1},${ym} ${x1 + s * k},${ym} L${x2 - s * k},${ym} ` +
            `Q${x2},${ym} ${x2},${ym + k} L${x2},${y2}`;
        mx = (x1 + x2) / 2; my = ym;
      }
    }
    const p = document.createElementNS(NS, 'path');
    p.setAttribute('d', d); p.setAttribute('fill', 'none'); p.setAttribute('stroke', COR);
    p.setAttribute('stroke-width', '1.4'); p.setAttribute('marker-end', 'url(#ponta)');
    if (tracejada) p.setAttribute('stroke-dasharray', '4 3');
    svg.appendChild(p);
    if (m) {
      const e = document.createElement('div'); e.className = 'marca pilula'; e.textContent = m;
      e.style.left = mx + 'px'; e.style.top = my + 'px'; fig.appendChild(e); marcas[m] = my;
    }
  }
  // cartões: centrados na altura do marcador; se colidirem, descem
  let fundo = -Infinity;
  for (const c of document.querySelectorAll('.cartao')) {
    const h = c.getBoundingClientRect().height;
    const t = Math.max(marcas[c.dataset.m] - h / 2, fundo + 10);
    c.style.top = t + 'px'; fundo = t + h;
  }
  document.body.dataset.pronto = '1';
}
document.fonts.ready.then(desenhar);
"""


def _css() -> str:
    css = CSS.replace("$LARGURA", str(LARGURA_CSS))
    for k in sorted(C, key=len, reverse=True):
        css = css.replace("$" + k, C[k])
    return css


def _caixa(cid, titulo, texto, decide, cor, larga) -> str:
    t = f'<div class="t">{titulo}</div>' if titulo else ""
    d = f'<div class="d"><span>quem decide</span> <b>{decide}</b></div>' if decide else ""
    return f'<div class="caixa {cor}{" larga" if larga else ""}" id="{cid}">{t}<div class="x">{texto}</div>{d}</div>'


def montar_html() -> str:
    linhas = []
    for nid, rot, sub, cor in NIVEIS:
        caixas = CAIXAS[nid]
        corpo = "".join(_caixa(*cx, cor, len(caixas) == 1) for cx in caixas)
        sub_html = f"<small>{sub}</small>" if sub else ""
        linhas.append(f'<div class="rot {cor}">{rot}{sub_html}</div><div class="nivel">{corpo}</div>')
    cartoes = "".join(f'<div class="cartao" data-m="{m}"><div class="ct"><span class="pilula">{m}</span>{t}</div>'
                      f'<div class="cx">{x}</div></div>' for m, t, x in PREMISSAS)
    setas = "[" + ",".join(f'["{a}","{b}",{"true" if d else "false"},{("%s" % repr(m)) if m else "null"}]'
                           for a, b, d, m in SETAS) + "]"
    js = JS.replace("__SETAS__", setas.replace("'", '"')).replace("__COR__", C["base500"])
    return f"""<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8"><title>Teoria da mudança da LICC</title>
<style>{_css()}</style></head>
<body><div id="fig">
<svg id="setas"></svg>
<div id="grade">{''.join(linhas)}</div>
<div id="premissas">{cartoes}</div>
<div id="legenda">
  <div><span class="amostra cheia"></span>elo da cadeia</div>
  <div><span class="amostra"></span>elo sem dado público</div>
  <div><span class="pilula">H</span>premissa tratada como hipótese (ver Quadro 2)</div>
</div>
</div>
<script>{js}</script>
</body></html>
"""


def main() -> None:
    FIG.mkdir(parents=True, exist_ok=True)
    HTML.write_text(montar_html(), encoding="utf-8")
    with sync_playwright() as p:
        nav = p.chromium.launch()
        pag = nav.new_page(viewport={"width": LARGURA_CSS, "height": 1600}, device_scale_factor=ESCALA)
        pag.goto(HTML.as_uri())
        pag.wait_for_selector("body[data-pronto='1']")
        fig = pag.locator("#fig")
        fig.screenshot(path=str(PNG))
        altura = fig.bounding_box()["height"]
        pag.pdf(path=str(PDF), width=f"{LARGURA_CSS}px", height=f"{int(altura) + 2}px", print_background=True,
                margin={"top": "0", "right": "0", "bottom": "0", "left": "0"})
        nav.close()
    print(PNG)
    print(PDF)


if __name__ == "__main__":
    main()
