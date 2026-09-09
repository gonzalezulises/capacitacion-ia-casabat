# -*- coding: utf-8 -*-
"""Render del deck. La estructura de datos manda; la numeracion de slides,
los contadores del top-rail y los footers se derivan — nunca se escriben a mano."""
from style import CSS

FOOT_L = 'R I Z O . M A'
FOOT_R = 'C A S A B A T'
FONTS = ("https://fonts.googleapis.com/css2?family=Antonio:wght@400;600;700"
         "&family=Roboto:wght@300;400;500;700&family=IBM+Plex+Mono:wght@400;500&display=swap")


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
            + '\n'.join(out) +
            '\n</deck-stage>\n\n</body>\n</html>\n'
        )


# ---------- constructores de slide ----------

def cover(eyebrow, h1_html, sub, fecha):
    def b(i, total):
        return (f'{_rail("", fecha)}\n'
                f'    <div style="margin:auto 0;">\n'
                f'      <div class="eyebrow">{eyebrow}</div>\n'
                f'      <h1>{h1_html}</h1>\n'
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
    """blocks: [(bnum, titulo, [(item, min)])]"""
    def b(i, total):
        cols = []
        for bnum, tit, items in blocks:
            lis = '\n'.join(f'          <li>{t} <span>{m}</span></li>' for t, m in items)
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
        return (f'{_rail(f"BLOQUE {bloque_n} DE {de}", f"{minutos} MIN <span class=\'sep\'></span> {n_ej}")}\n'
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
    _dens = ' denser' if _peso > 700 else (' dense' if _peso > 560 else '')

    def b(i, total):
        ps = '\n'.join(f'            <li>{p}</li>' for p in pasos)
        cav = ''
        if caveat:
            cav = f'\n        <div class="caveat"><b>Límite</b>{caveat}</div>'
        return (f'{_rail(rail_l, f"{minutos} MINUTOS")}\n'
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
