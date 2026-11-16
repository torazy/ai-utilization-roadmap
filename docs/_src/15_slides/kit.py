# -*- coding: utf-8 -*-
"""SVG drawing kit for the slide deck."""
import re

INK = '#101C36'; PAPER = '#FAF8F4'; WHITE = '#FFFFFF'; LINE = '#D8D2C6'; SOFT = '#4A5570'; MUTE = '#7A8296'
OR = '#C2410C'; ORT = '#FDEBDD'; TE = '#0F766E'; TET = '#DDF1EE'; BL = '#1D4ED8'; BLT = '#E3EBFC'
RD = '#B42318'; RDT = '#FBE6E3'; GD = '#92600E'; GDT = '#F7ECD2'; GRT = '#EFECE5'; NAVY2 = '#1C2B50'
W = 1664
WARN = []


def esc(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def est(s, size, bold=False):
    w = 0.0
    for ch in s:
        o = ord(ch)
        if ch == ' ':
            w += 0.3
        elif o < 0x2000:
            w += 0.62 if bold else 0.57
        else:
            w += 1.0
    return w * size


def wrap(s, size, maxw, bold=False):
    out = []
    for para in s.split('\n'):
        cur = ''; cw = 0.0
        for t in re.findall(r'[A-Za-z0-9_.\-/+%:,]+|.', para):
            tw = est(t, size, bold)
            if cur and cw + tw > maxw and t not in '、。）」・ ':
                out.append(cur.rstrip()); cur = t.lstrip(); cw = est(cur, size, bold)
            else:
                cur += t; cw += tw
        out.append(cur.rstrip())
    return out


def text(x, y, s, size=24, fill=INK, weight=400, anchor='start', maxw=None, lh=1.45):
    """y = top of the first line. Returns svg."""
    lines = wrap(s, size, maxw, weight >= 600) if maxw else s.split('\n')
    o = []
    for i, ln in enumerate(lines):
        by = y + size * 0.88 + i * size * lh
        o.append(f'<text x="{x:.1f}" y="{by:.1f}" font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}">{esc(ln)}</text>')
    return ''.join(o)


def th(s, size, maxw, lh=1.45, bold=False):
    return len(wrap(s, size, maxw, bold)) * size * lh


def box(x, y, w, h, fill=WHITE, stroke=LINE, sw=2, r=14, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    return f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>'


def line(pts, color=INK, sw=3, dash=None):
    d = 'M' + ' L'.join(f'{x:.1f} {y:.1f}' for x, y in pts)
    ds = f' stroke-dasharray="{dash}"' if dash else ''
    return f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"{ds}/>'


MK = {INK: 'ink', OR: 'or', TE: 'te', BL: 'bl', RD: 'rd', MUTE: 'mute', WHITE: 'wh', GD: 'gd'}


def arrow(x1, y1, x2, y2, color=INK, sw=3.5, dash=None, via=None):
    pts = [(x1, y1)] + (via or []) + [(x2, y2)]
    d = 'M' + ' L'.join(f'{x:.1f} {y:.1f}' for x, y in pts)
    ds = f' stroke-dasharray="{dash}"' if dash else ''
    return f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" marker-end="url(#m-{MK[color]})"{ds}/>'


def defs():
    o = '<defs>'
    for c, k in MK.items():
        o += f'<marker id="m-{k}" markerUnits="userSpaceOnUse" markerWidth="18" markerHeight="16" refX="15" refY="8" orient="auto"><path d="M0 1L17 8L0 15z" fill="{c}"/></marker>'
    return o + '</defs>'


ICON = {
    'user': '<circle cx="12" cy="8" r="4"/><path d="M4 21c0-4.4 3.6-7 8-7s8 2.6 8 7"/>',
    'db': '<ellipse cx="12" cy="5" rx="8" ry="3"/><path d="M4 5v14c0 1.7 3.6 3 8 3s8-1.3 8-3V5"/><path d="M4 12c0 1.7 3.6 3 8 3s8-1.3 8-3"/>',
    'shield': '<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="M9 12l2.2 2.2L15.5 10"/>',
    'lock': '<rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/>',
    'chat': '<path d="M4 5h16v11H10l-5 4v-4H4z"/><path d="M8 9h8M8 12.5h5"/>',
    'app': '<rect x="3" y="4" width="18" height="16" rx="2"/><path d="M3 9h18"/><path d="M6.5 6.5h.01M9.5 6.5h.01"/>',
    'doc': '<path d="M6 3h8l4 4v14H6z"/><path d="M14 3v4h4"/><path d="M9 12h6M9 16h6"/>',
    'gauge': '<path d="M4 17a8 8 0 1 1 16 0"/><path d="M12 17l4-6"/><path d="M4 17h16"/>',
    'list': '<path d="M9 6h11M9 12h11M9 18h11"/><path d="M4.5 6h.01M4.5 12h.01M4.5 18h.01"/>',
    'globe': '<circle cx="12" cy="12" r="9"/><path d="M3 12h18"/><path d="M12 3c3.2 3 3.2 15 0 18"/><path d="M12 3c-3.2 3-3.2 15 0 18"/>',
    'key': '<circle cx="8" cy="15" r="4"/><path d="M11 12l9-9"/><path d="M16.5 6.5l3 3"/>',
    'gate': '<path d="M4 21V9l8-6 8 6v12"/><path d="M9 21v-7h6v7"/><path d="M2 21h20"/>',
    'robot': '<rect x="5" y="8" width="14" height="11" rx="2"/><path d="M12 8V4.5"/><circle cx="12" cy="3.5" r="1"/><path d="M9.5 13h.01M14.5 13h.01"/><path d="M9.5 16.5h5"/>',
    'cube': '<path d="M12 3l8 4.5v9L12 21l-8-4.5v-9z"/><path d="M12 12l8-4.5M12 12v9M12 12L4 7.5"/>',
    'table': '<rect x="3" y="4" width="18" height="16" rx="2"/><path d="M3 10h18M3 15h18M9 4v16"/>',
    'book': '<path d="M5 4h14v16H7a2 2 0 0 1-2-2z"/><path d="M5 18a2 2 0 0 1 2-2h12"/><path d="M9 8h6"/>',
    'search': '<circle cx="11" cy="11" r="6"/><path d="M20 20l-4.6-4.6"/>',
    'gear': '<circle cx="12" cy="12" r="3.2"/><path d="M12 2.5v3M12 18.5v3M2.5 12h3M18.5 12h3M5.3 5.3l2.1 2.1M16.6 16.6l2.1 2.1M5.3 18.7l2.1-2.1M16.6 7.4l2.1-2.1"/>',
    'warn': '<path d="M12 3.5L22 20H2z"/><path d="M12 10v5"/><path d="M12 17.5h.01"/>',
    'check': '<circle cx="12" cy="12" r="9"/><path d="M8 12.2l2.8 2.8L16 9.5"/>',
    'layers': '<path d="M12 3l9 5-9 5-9-5z"/><path d="M3 13l9 5 9-5"/>',
    'plug': '<path d="M9 3v5M15 3v5"/><path d="M6 8h12v4a6 6 0 0 1-12 0z"/><path d="M12 18v3"/>',
    'bld': '<rect x="5" y="3" width="14" height="18"/><path d="M9 7h1.5M13.5 7H15M9 11h1.5M13.5 11H15M9 15h1.5M13.5 15H15"/>',
    'x': '<circle cx="12" cy="12" r="9"/><path d="M8.5 8.5l7 7M15.5 8.5l-7 7"/>',
}


def ico(name, x, y, size=38, color=INK, sw=1.8):
    return (f'<g transform="translate({x:.1f} {y:.1f}) scale({size / 24:.3f})" fill="none" stroke="{color}" '
            f'stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round">{ICON[name]}</g>')


THEME = {  # fill, stroke, title, sub, icon, dash
    'white': (WHITE, INK, INK, SOFT, OR, None),
    'plain': (WHITE, LINE, INK, SOFT, OR, None),
    'ink': (INK, INK, WHITE, '#C9D2E3', '#F0A070', None),
    'or': (ORT, OR, INK, SOFT, OR, None),
    'te': (TET, TE, INK, SOFT, TE, None),
    'bl': (BLT, BL, INK, SOFT, BL, None),
    'rd': (RDT, RD, INK, SOFT, RD, None),
    'gd': (GDT, GD, INK, SOFT, GD, None),
    'grey': (GRT, MUTE, INK, SOFT, MUTE, '8 6'),
}


def node(x, y, w, h, title, sub=None, icon=None, theme='white', ts=28, ss=23, isz=38, center=False, pad=22, tag=''):
    fill, stroke, tc, sc, ic, dash = THEME[theme]
    o = box(x, y, w, h, fill, stroke, 2.5, 14, dash)
    if center:
        tl = wrap(title, ts, w - 2 * pad, True)
        hh = len(tl) * ts * 1.3
        sl = wrap(sub, ss, w - 2 * pad) if sub else []
        tot = hh + (6 + len(sl) * ss * 1.45 if sub else 0)
        ty = y + (h - tot) / 2
        o += text(x + w / 2, ty, title, ts, tc, 700, 'middle', w - 2 * pad, 1.3)
        if sub:
            o += text(x + w / 2, ty + hh + 6, sub, ss, sc, 400, 'middle', w - 2 * pad)
        if tot > h - 8:
            WARN.append(f'{tag} node "{title}" needs {tot:.0f} > {h}')
        return o
    tx = x + pad + (isz + 14 if icon else 0)
    tw = w - (tx - x) - pad
    hh = len(wrap(title, ts, tw, True)) * ts * 1.3
    if sub:
        head = max(hh, isz if icon else 0)
        sh = th(sub, ss, w - 2 * pad)
        if icon:
            o += ico(icon, x + pad, y + pad + (head - isz) / 2, isz, ic)
        o += text(tx, y + pad + (head - hh) / 2, title, ts, tc, 700, 'start', tw, 1.3)
        o += text(x + pad, y + pad + head + 10, sub, ss, sc, 400, 'start', w - 2 * pad)
        need = pad * 2 + head + 10 + sh
    else:
        if icon:
            o += ico(icon, x + pad, y + (h - isz) / 2, isz, ic)
        o += text(tx, y + (h - hh) / 2, title, ts, tc, 700, 'start', tw, 1.3)
        need = hh + 16
    if need > h + 2:
        WARN.append(f'{tag} node "{title}" needs {need:.0f} > {h}')
    return o


def badge(cx, cy, n, r=22, fill=RD, size=None):
    size = size or int(r * 1.05)
    return (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}"/>'
            f'<text x="{cx}" y="{cy + size * 0.36:.1f}" font-size="{size}" font-weight="700" fill="#fff" text-anchor="middle">{n}</text>')


def chip(x, y, s, fill=GRT, color=INK, size=22, h=44, stroke=None, weight=500):
    w = est(s, size, weight >= 600) + 36
    o = f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h}" rx="{h / 2}" fill="{fill}" stroke="{stroke or fill}" stroke-width="2"/>'
    o += text(x + 18, y + (h - size * 1.45) / 2 + 2, s, size, color, weight)
    return o, w


def chips(x, y, items, gap=14, **kw):
    o = ''
    for s in items:
        c, w = chip(x, y, s, **kw)
        o += c; x += w + gap
    return o


def mtable(x, y, cw, rows, size=22, rh=48, head=INK, mute=()):
    o = ''
    tw = sum(cw)
    for r, row in enumerate(rows):
        yy = y + r * rh
        fill = head if r == 0 else WHITE
        o += f'<rect x="{x}" y="{yy}" width="{tw}" height="{rh}" fill="{fill}" stroke="{LINE}" stroke-width="2"/>'
        xx = x
        for c, cell in enumerate(row):
            col = WHITE if r == 0 else (MUTE if (r, c) in mute else INK)
            o += text(xx + 14, yy + (rh - size * 1.45) / 2 + 2, cell, size, col, 700 if r == 0 else 400)
            if c:
                o += f'<path d="M{xx} {yy}V{yy + rh}" stroke="{LINE}" stroke-width="2"/>'
            xx += cw[c]
    return o


def svg(h, inner, w=W, label=''):
    return (f'<svg class="fig" viewBox="0 0 {w} {h}" width="{w}" height="{h}" xmlns="http://www.w3.org/2000/svg" '
            f'role="img" aria-label="{esc(label)}">{inner}</svg>')
