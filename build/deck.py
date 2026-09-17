# -*- coding: utf-8 -*-
"""Render del deck. La estructura de datos manda; la numeracion de slides,
los contadores del top-rail y los footers se derivan — nunca se escriben a mano."""
import os
import re
from urllib.parse import quote
from style import CSS

_RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_MATS = os.path.join(_RAIZ, 'materiales')


def _indice_materiales():
    """nombre de archivo -> ruta relativa desde la raiz del sitio."""
    idx = {}
    for base, _dirs, files in os.walk(_MATS):
        for f in files:
            if f.startswith('.'):
                continue
            rel = os.path.relpath(os.path.join(base, f), _RAIZ)
            idx[f] = '/'.join(quote(p) for p in rel.split(os.sep))
    # la carpeta del expediente no tiene indice propio: se manda al hub
    idx['expediente-PR-ADM-014/'] = 'index.html#expediente'
    idx['materiales/'] = 'index.html#materiales'
    return idx


MATERIALES = _indice_materiales()


def _enlazar(html):
    """Convierte <code>archivo</code> en un enlace al archivo, cuando existe.
    Los <code> que no son materiales (nombres de columna, marcadores) se dejan."""
    def sub(m):
        nombre = m.group(1)
        ruta = MATERIALES.get(nombre)
        if not ruta:
            return m.group(0)
        return (f'<a class="mat" href="{ruta}" target="_blank" rel="noopener">'
                f'<code>{nombre}</code></a>')
    return re.sub(r'<code>([^<]+)</code>', sub, html)

FOOT_L = 'R I Z O . M A'
FOOT_R = 'C A S A B A T'
FONTS = ("https://fonts.googleapis.com/css2?family=Antonio:wght@400;600;700"
         "&family=Inter:wght@300;400;500;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap")


def _footer(n, right=FOOT_R):
    return (f'    <div class="footer">\n'
            f'      <div class="lhs"><span>{FOOT_L}</span><span class="dot"></span><span>{right}</span></div>\n'
            f'      <div class="rhs">{n:02d}</div>\n'
            f'    </div>')


def _rail(left, right):
    return f'    <div class="top-rail"><span>{left}</span><span>{right}</span></div>'


class Deck:
    def __init__(self, title, meta):
        self.title = title
        self.meta = meta          # dict: eyebrow, h1, sub, fecha
        self.slides = []          # (label, css_class, builder)

    def add(self, label, cls, builder):
        self.slides.append((label, cls, builder))

    def render(self):
        total = len(self.slides)
        out = []
        for i, (label, cls, builder) in enumerate(self.slides, start=1):
            cls_attr = f' class="{cls}"' if cls else ''
            body = builder(i, total)
            out.append(f'<!-- ===== {i:02d} · {label} ===== -->\n'
                       f'<section{cls_attr} data-label="{i:02d} {label}">\n'
                       f'  <div class="frame">\n{body}\n{_footer(i)}\n  </div>\n</section>\n')
        cuerpo = _enlazar('\n'.join(out))
        return (
            '<!doctype html>\n<html lang="es">\n<head>\n<meta charset="utf-8" />\n'
            f'<title>{self.title}</title>\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1" />\n'
            '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
            '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
            f'<link href="{FONTS}" rel="stylesheet">\n'
            '<script src="deck-stage.js"></script>\n'
            f'<style>{CSS}</style>\n</head>\n<body>\n\n'
            '<deck-stage width="1920" height="1080">\n\n'
            + cuerpo +
            '\n</deck-stage>\n\n</body>\n</html>\n'
        )


# ---------- constructores de slide ----------

def cover(eyebrow, h1_html, sub, fecha, size=250):
    def b(i, total):
        style = '' if size == 250 else f' style="font-size:{size}px;"'
        return (f'{_rail(fecha, "")}\n'
                f'    <img class="marca" src="assets/logo-casabat.jpg" '
                f'alt="La Casa de las Baterías" width="1080" height="1080" />\n'
                f'    <div style="margin:auto 0;">\n'
                f'      <div class="eyebrow">{eyebrow}</div>\n'
                f'      <h1{style}>{h1_html}</h1>\n'
                f'      <p class="sub">{sub}</p>\n'
                f'    </div>')
    return b


def statement(rail_l, h1_html, body_html, size=96):
    def b(i, total):
        return (f'{_rail(rail_l, f"{i:02d} / {total:02d}")}\n'
                f'    <div style="margin:auto 0;">\n'
                f'      <h1 class="display" style="font-size:{size}px;max-width:1560px;">{h1_html}</h1>\n'
                f'      {body_html}\n'
                f'    </div>')
    return b


def stats(rail_l, h1_html, items):
    """items: [(label, cifra, texto)]"""
    def b(i, total):
        def _b(v):
            # un valor con letras es una palabra, no una cifra: se compone mas pequeno
            cls = ' class="word"' if any(c.isalpha() for c in v) else ''
            return f'<b{cls}>{v}</b>'
        cards = '\n'.join(
            f'      <div class="stat"><span class="label">{l}</span>{_b(n)}<p>{t}</p></div>'
            for l, n, t in items)
        return (f'{_rail(rail_l, f"{i:02d} / {total:02d}")}\n'
                f'    <h1 class="display" style="margin-top:48px;font-size:88px;max-width:1560px;">{h1_html}</h1>\n'
                f'    <div class="stats-grid">\n{cards}\n    </div>')
    return b


def agenda(rail_r, h1_html, blocks):
    """blocks: [(bnum, titulo, [(item, detalle)])]. El ritmo lo marca el facilitador."""
    def b(i, total):
        cols = []
        for bnum, tit, items in blocks:
            bnum = re.sub(r'\s*·\s*\d+\s+MIN\s*$', '', bnum)
            lis = '\n'.join(f'          <li>{t}</li>' for t, _detalle in items)
            cols.append(f'      <div class="ag-block">\n'
                        f'        <div class="bnum">{bnum}</div>\n'
                        f'        <h3>{tit}</h3>\n'
                        f'        <ul>\n{lis}\n        </ul>\n'
                        f'      </div>')
        return (f'{_rail("AGENDA DE LA SESIÓN", rail_r)}\n'
                f'    <h1 class="display" style="margin-top:52px;font-size:96px;">{h1_html}</h1>\n'
                f'    <div class="agenda-grid">\n' + '\n'.join(cols) + '\n    </div>')
    return b


def howto(rail_l, h1_html, cards):
    """cards: [(titulo, texto)]"""
    def b(i, total):
        cs = '\n'.join(
            f'      <div class="howto-card"><div class="n">{k:02d}</div><h3>{t}</h3><p>{p}</p></div>'
            for k, (t, p) in enumerate(cards, start=1))
        return (f'{_rail(rail_l, f"{i:02d} / {total:02d}")}\n'
                f'    <h1 class="display" style="margin-top:52px;font-size:88px;max-width:1560px;">{h1_html}</h1>\n'
                f'    <div class="howto-grid">\n{cs}\n    </div>')
    return b


def divider(bloque_n, de, minutos, n_ej, h1_html, herramientas, objetivo, entregable):
    def b(i, total):
        return (f'{_rail(f"BLOQUE {bloque_n} DE {de}", n_ej)}\n'
                f'    <div class="layout">\n'
                f'      <div class="block-no">{bloque_n:02d}</div>\n'
                f'      <div><h1>{h1_html}</h1></div>\n'
                f'      <div class="meta">\n'
                f'        <div><b>Herramientas</b>{herramientas}</div>\n'
                f'        <div><b>Objetivo</b>{objetivo}</div>\n'
                f'        <div><b>Te llevas</b>{entregable}</div>\n'
                f'      </div>\n'
                f'    </div>')
    return b


def exercise(num, rail_l, minutos, titulo, herramienta, concepto, pasos, prompt_html,
             resultado, caveat=None, prompt_label='PROMPT DEL PARTICIPANTE'):
    import re as _re
    _plano = _re.sub(r'<[^>]+>', '', prompt_html)
    _peso = len(_plano) + (330 if caveat else 0)
    _dens = ' denser' if _peso > 620 else (' dense' if _peso > 470 else '')

    def b(i, total):
        ps = '\n'.join(f'            <li>{p}</li>' for p in pasos)
        cav = ''
        if caveat:
            cav = f'\n        <div class="caveat"><b>Límite</b>{caveat}</div>'
        return (f'{_rail(rail_l, "APLICACIÓN PRÁCTICA")}\n'
                f'    <div class="ex-header">\n'
                f'      <div class="ex-num-block">\n'
                f'        <div class="ex-num-label">EJERCICIO</div>\n'
                f'        <div class="ex-num">{num:02d}</div>\n'
                f'      </div>\n'
                f'      <div>\n'
                f'        <h2 class="ex-title">{titulo}</h2>\n'
                f'        <div class="ex-tool"><b>HERRAMIENTA</b>{herramienta}</div>\n'
                f'      </div>\n'
                f'    </div>\n'
                f'    <div class="ex-body">\n'
                f'      <div class="col">\n'
                f'        <div class="concept-block">\n'
                f'          <span class="label acc">CONCEPTO CLAVE</span>\n'
                f'          <div class="concept">{concepto}</div>\n'
                f'        </div>\n'
                f'        <div class="steps-block">\n'
                f'          <span class="label">PASO A PASO</span>\n'
                f'          <ol class="steps">\n{ps}\n          </ol>\n'
                f'        </div>\n'
                f'      </div>\n'
                f'      <div class="col">\n'
                f'        <div class="prompt-card{_dens}">\n'
                f'          <span class="label">{prompt_label}</span>\n'
                f'{prompt_html}\n'
                f'        </div>\n'
                f'        <div class="result">\n'
                f'          <b>RESULTADO ESPERADO</b>\n          {resultado}\n'
                f'        </div>{cav}\n'
                f'      </div>\n'
                f'    </div>')
    return b


def exercise_case(num, rail_l, minutos, titulo, rol, entrada, herramienta, situacion,
                  decision, pasos, prompt_html, entregable, criterio, caveat=None,
                  prompt_label='PROMPT DEL PARTICIPANTE'):
    """Laboratorio centrado en una situación de trabajo, no en la técnica."""
    import re as _re
    plano = _re.sub(r'<[^>]+>', '', prompt_html)
    peso = len(plano) + len(entregable) + len(criterio) + (260 if caveat else 0)
    dens = ' denser' if peso > 760 else (' dense' if peso > 580 else '')

    def b(i, total):
        ps = '\n'.join(f'            <li>{p}</li>' for p in pasos)
        cav = ''
        if caveat:
            cav = f'\n        <div class="caveat"><b>Límite</b>{caveat}</div>'
        return (f'{_rail(rail_l, "APLICACIÓN PRÁCTICA")}\n'
                f'    <div class="ex-header case-header">\n'
                f'      <div class="ex-num-block">\n'
                f'        <div class="ex-num-label">LABORATORIO</div>\n'
                f'        <div class="ex-num">{num:02d}</div>\n'
                f'      </div>\n'
                f'      <div>\n'
                f'        <h2 class="ex-title">{titulo}</h2>\n'
                f'        <div class="case-meta">\n'
                f'          <span class="role"><b>ROL</b>{rol}</span>\n'
                f'          <span class="input"><b>ENTRADA</b>{entrada}</span>\n'
                f'          <span class="case-tool"><b>IA</b>{herramienta}</span>\n'
                f'        </div>\n'
                f'      </div>\n'
                f'    </div>\n'
                f'    <div class="ex-body case-body">\n'
                f'      <div class="col">\n'
                f'        <div class="concept-block">\n'
                f'          <span class="label acc">SITUACIÓN CASABAT</span>\n'
                f'          <div class="situation">{situacion}</div>\n'
                f'        </div>\n'
                f'        <div class="decision"><span class="label">DECISIÓN</span>{decision}</div>\n'
                f'        <div class="steps-block">\n'
                f'          <span class="label">PASO A PASO</span>\n'
                f'          <ol class="steps">\n{ps}\n          </ol>\n'
                f'        </div>\n'
                f'      </div>\n'
                f'      <div class="col">\n'
                f'        <div class="prompt-card{dens}">\n'
                f'          <span class="label">{prompt_label}</span>\n'
                f'{prompt_html}\n'
                f'        </div>\n'
                f'        <div class="result">\n'
                f'          <b>ENTREGABLE</b>\n          {entregable}\n'
                f'          <div class="criterion"><span>CRITERIO</span>{criterio}</div>\n'
                f'        </div>{cav}\n'
                f'      </div>\n'
                f'    </div>')
    return b


def governance(rail_l, h1_html, intro, items):
    def b(i, total):
        gs = '\n'.join(f'      <div class="gov-item"><h3>{t}</h3><p>{p}</p></div>' for t, p in items)
        return (f'{_rail(rail_l, f"{i:02d} / {total:02d}")}\n'
                f'    <div style="margin-top:44px;">\n'
                f'      <h1 class="display" style="font-size:88px;color:var(--bone);">{h1_html}</h1>\n'
                f'      <p style="font-size:24px;color:var(--bone-2);line-height:1.5;max-width:1400px;margin-top:24px;">{intro}</p>\n'
                f'    </div>\n'
                f'    <div class="gov-grid">\n{gs}\n    </div>')
    return b


def closing(rail_l, h1_html, nexts):
    def b(i, total):
        ns = '\n'.join(f'      <div><span class="lbl">{l}</span><p>{p}</p></div>' for l, p in nexts)
        return (f'{_rail(rail_l, f"{i:02d} / {total:02d}")}\n'
                f'    <div class="layout"><h1>{h1_html}</h1></div>\n'
                f'    <div class="next">\n{ns}\n    </div>')
    return b


def filelist(rail_l, h1_html, intro, grupos):
    """Slide de materiales: qué archivo se usa en qué ejercicio.
    grupos: [(titulo, [(archivo, para_que)])]"""
    def b(i, total):
        cols = []
        for tit, items in grupos:
            lis = '\n'.join(
                f'          <li><code>{a}</code><span>{d}</span></li>' for a, d in items)
            cols.append(f'      <div class="ag-block">\n'
                        f'        <div class="bnum">{tit}</div>\n'
                        f'        <ul class="files">\n{lis}\n        </ul>\n'
                        f'      </div>')
        return (f'{_rail(rail_l, f"{i:02d} / {total:02d}")}\n'
                f'    <h1 class="display" style="margin-top:44px;font-size:88px;">{h1_html}</h1>\n'
                f'    <p style="font-size:24px;line-height:1.45;color:var(--graphite-2);max-width:1500px;margin:20px 0 0;">{intro}</p>\n'
                f'    <div class="agenda-grid" style="margin-top:28px;">\n' + '\n'.join(cols) + '\n    </div>')
    return b


def theory(rail_l, h1_html, ideas, demo):
    """Slide de teoria minima con acceso a una demo externa.
    ideas: [(titulo, texto)]   ·   demo: dict(url, kicker, pasos[list], observa)"""
    def b(i, total):
        lis = '\n'.join(
            f'          <li><b>{t}</b> {d}</li>' for t, d in ideas)
        pasos = '\n'.join(f'            <li>{p}</li>' for p in demo['pasos'])
        return (f'{_rail(rail_l, f"{i:02d} / {total:02d}")}\n'
                f'    <h1 class="display" style="margin-top:30px;font-size:80px;max-width:1500px;">{h1_html}</h1>\n'
                f'    <div class="teoria">\n'
                f'      <div>\n'
                f'        <span class="label acc">LA TEORÍA MÍNIMA</span>\n'
                f'        <ol class="ideas">\n{lis}\n        </ol>\n'
                f'      </div>\n'
                f'      <div class="demo">\n'
                f'        <span class="label">{demo["kicker"]}</span>\n'
                f'        <a class="url" href="{demo["url"]}" target="_blank" rel="noopener">{demo["url"]}</a>\n'
                f'        <ol class="steps">\n{pasos}\n        </ol>\n'
                f'        <p class="observa"><b>Qué observar</b>{demo["observa"]}</p>\n'
                f'      </div>\n'
                f'    </div>')
    return b


def cards(rail_l, h1_html, intro, items, cols=3):
    """Rejilla de tarjetas — para catalogos (tecnicas, opciones).
    items: [(titulo, cuando, ejemplo)]"""
    def b(i, total):
        cs = '\n'.join(
            f'      <div class="tc">\n'
            f'        <h3>{t}</h3>\n'
            f'        <p class="cuando">{c}</p>\n'
            f'        <p class="ej">{e}</p>\n'
            f'      </div>' for t, c, e in items)
        pin = f'    <p class="intro-cards">{intro}</p>\n' if intro else ''
        return (f'{_rail(rail_l, f"{i:02d} / {total:02d}")}\n'
                f'    <h1 class="display" style="margin-top:24px;font-size:76px;">{h1_html}</h1>\n'
                f'{pin}'
                f'    <div class="cards-grid" style="grid-template-columns:repeat({cols},1fr);">\n{cs}\n    </div>')
    return b


def recipe(rail_l, h1_html, intro, pasos, bloque_label, bloque_html, nota=None):
    """Slide de receta: pasos a la izquierda, bloque copiable a la derecha."""
    def b(i, total):
        ps = '\n'.join(f'          <li>{p}</li>' for p in pasos)
        nt = f'\n        <div class="caveat"><b>Ojo</b>{nota}</div>' if nota else ''
        return (f'{_rail(rail_l, f"{i:02d} / {total:02d}")}\n'
                f'    <h1 class="display" style="margin-top:24px;font-size:72px;">{h1_html}</h1>\n'
                f'    <p class="intro-cards">{intro}</p>\n'
                f'    <div class="ex-body" style="margin-top:24px;">\n'
                f'      <div class="col">\n'
                f'        <div class="steps-block">\n'
                f'          <span class="label">PASO A PASO</span>\n'
                f'          <ol class="steps">\n{ps}\n          </ol>\n'
                f'        </div>{nt}\n'
                f'      </div>\n'
                f'      <div class="col">\n'
                f'        <div class="prompt-card denser">\n'
                f'          <span class="label">{bloque_label}</span>\n'
                f'{bloque_html}\n'
                f'        </div>\n'
                f'      </div>\n'
                f'    </div>')
    return b


def divider_anexo(h1_html, rotulo, herramientas, objetivo, entregable):
    """Divider de la seccion de anexos: no es un bloque de la sesion, asi que
    no declara minutos — de lo contrario descuadraria la agenda."""
    def b(i, total):
        return (f'{_rail("MATERIAL DE CONSULTA", rotulo)}\n'
                f'    <div class="layout">\n'
                f'      <div class="block-no" style="font-size:300px;letter-spacing:-0.02em;">A</div>\n'
                f'      <div><h1>{h1_html}</h1></div>\n'
                f'      <div class="meta">\n'
                f'        <div><b>Herramientas</b>{herramientas}</div>\n'
                f'        <div><b>Cuándo se usa</b>{objetivo}</div>\n'
                f'        <div><b>Contiene</b>{entregable}</div>\n'
                f'      </div>\n'
                f'    </div>')
    return b


def contrast(rail_l, h1_html, intro, izq, der, cierre=None):
    """Dos columnas contrapuestas — para separar lo que una herramienta hace
    de lo que solo parece que hace. izq/der: (rotulo, titular, [puntos])"""
    def col(cl, datos):
        rot, tit, puntos = datos
        lis = '\n'.join(f'          <li>{p}</li>' for p in puntos)
        return (f'      <div class="cc {cl}">\n'
                f'        <span class="label">{rot}</span>\n'
                f'        <h3>{tit}</h3>\n'
                f'        <ul>\n{lis}\n        </ul>\n'
                f'      </div>')
    def b(i, total):
        fin = (f'    <p class="cc-cierre">{cierre}</p>\n' if cierre else '')
        return (f'{_rail(rail_l, f"{i:02d} / {total:02d}")}\n'
                f'    <h1 class="display" style="margin-top:26px;font-size:78px;max-width:1560px;">{h1_html}</h1>\n'
                f'    <p class="intro-cards">{intro}</p>\n'
                f'    <div class="contraste">\n{col("si", izq)}\n{col("no", der)}\n    </div>\n'
                f'{fin}')
    return b
