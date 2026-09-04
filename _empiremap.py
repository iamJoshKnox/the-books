# -*- coding: utf-8 -*-
"""The empires, lit six ways: Assyria, Babylon and Persia at the scale they need.

Isaiah, Jeremiah, Ezekiel, Daniel, Esther and Nehemiah are all about what
comes from the east, or what happens there, and the land plate stops at the
Jordan. This one runs from the Nile delta to Susa. Same style, same pipeline
as the other generators; idempotent; checked by verify.py.
"""
import base64
import io
import math
import re

P = 'index.html'
PARCH, SEA_C, INK, MUTED, FAINT = '#E4D8C0', '#C3D3D9', '#2E2519', '#6E6250', '#8A7E68'
HOT, ORIGIN, DIM, RIVER = '#A8552E', '#6E5A2E', '#B3A68C', '#7C9EAC'

# ----------------------------------------------------------- geography
# viewBox 460x250. The Mediterranean fills the left, the Levant coast runs down
# from (130,60); the two rivers fall from the top to the Gulf at bottom right.
SEA = 'M0,30 C50,40 100,36 128,58 C138,86 138,116 130,142 C118,172 92,186 62,204 L0,214 Z'
GULF = 'M356,222 C376,214 402,216 424,226 C412,240 386,246 360,238 Z'
EUPHRATES = 'M236,0 C246,50 272,110 318,150 C338,168 350,196 356,222'
TIGRIS = 'M290,0 C298,44 312,100 342,150 C356,172 362,196 366,222'
NILE = 'M56,250 C60,232 62,216 66,204'

CITIES = {
    'jerusalem': (146, 150, 'Jerusalem', 'start',  9,   4),
    'tahpanhes': (70,  200, 'Tahpanhes', 'start',  9,  12),
    'nineveh':   (312, 68,  'Nineveh',   'start',  9,   4),
    'babylon':   (322, 150, 'Babylon',   'start',  9,  -6),
    'chebar':    (338, 172, 'Chebar canal', 'start', 9, 14),
    'susa':      (404, 148, 'Susa',      'start',  9,  -4),
}
LABELS = [
    (52, 128, 'Mediterranean Sea', 'middle', 12, RIVER, 'italic'),
    (390, 236, 'Persian Gulf', 'start', 9.5, RIVER, 'italic'),
    (300, 40, 'ASSYRIA', 'middle', 10.5, FAINT, 'caps'),
    (300, 206, 'BABYLONIA', 'middle', 10.5, FAINT, 'caps'),
    (412, 104, 'PERSIA', 'middle', 10.5, FAINT, 'caps'),
    (36, 234, 'EGYPT', 'start', 10.5, FAINT, 'caps'),
    (160, 100, 'ARAM', 'start', 10.5, FAINT, 'caps'),
    (262, 92, 'Euphrates', 'end', 9.5, RIVER, 'italic'),
    (334, 118, 'Tigris', 'start', 9.5, RIVER, 'italic'),
]

BOOKS = {
    'isaiah': dict(cities=['jerusalem'], marked=['nineveh'], faint=['babylon'], arrows=[('nineveh', 'jerusalem')],
        lead='Assyria at the gates.',
        caption='Sennacherib&rsquo;s army reaches Jerusalem in 701 BC and, in chapters 36&ndash;37, leaves without taking it. Babylon, still faint on the horizon, is where the second half of the book is addressed.'),
    'jeremiah': dict(cities=['jerusalem'], marked=['babylon', 'tahpanhes'], faint=[], arrows=[('babylon', 'jerusalem'), ('jerusalem', 'tahpanhes')],
        lead='Babylon comes; Jeremiah goes to Egypt.',
        caption='Forty years of telling Jerusalem not to resist, then the city falls anyway. The survivors flee to Egypt against his advice and take him with them; the book loses him at Tahpanhes.'),
    'ezekiel': dict(cities=['chebar'], marked=['jerusalem', 'babylon'], faint=[], arrows=[('jerusalem', 'chebar')],
        lead='Deported, 597 BC.',
        caption='Ezekiel is taken to Babylonia in the first deportation, ten years before the city falls, and prophesies from a settlement of exiles on the Chebar canal &mdash; the temple he describes at the end, he never sees again.'),
    'daniel': dict(cities=['babylon'], marked=['jerusalem', 'susa'], faint=['nineveh'], arrows=[('jerusalem', 'babylon')],
        lead='Babylon, then Persia.',
        caption='Taken as a boy in 605 BC, Daniel serves under three empires in one city. One vision places him at Susa, the Persian capital &mdash; the same palace where Esther&rsquo;s story is set two generations later.'),
    'esther': dict(cities=['susa'], marked=[], faint=['jerusalem', 'babylon'], arrows=[],
        lead='Susa, and nowhere else.',
        caption='The whole book is inside the Persian winter palace; Jerusalem is never mentioned. The empire the decrees go out to ran from India to Cush, and this map shows the western half of it.'),
    'nehemiah': dict(cities=['jerusalem'], marked=['susa'], faint=['babylon'], arrows=[('susa', 'jerusalem')],
        lead='From Susa to Jerusalem.',
        caption='Cupbearer to the Persian king, Nehemiah asks for leave and a letter, rides west with an escort, and rebuilds the wall in fifty-two days. Nine hundred miles, in the other direction from the exile.'),
}


def text(x, y, s, anchor='start', size=13, fill=INK, style=None, weight=None):
    fam = 'Helvetica,Arial,sans-serif' if style == 'caps' else 'Georgia,serif'
    extra = ''
    if style == 'italic': extra += ' font-style="italic"'
    if style == 'caps': extra += ' font-weight="700" letter-spacing="1.6"'
    if weight: extra += ' font-weight="%s"' % weight
    return ('<text x="%s" y="%s" text-anchor="%s" font-family="%s" font-size="%s" fill="%s"%s>%s</text>'
            % (x, y, anchor, fam, size, fill, extra, s))


def arrow(a, b):
    x0, y0 = CITIES[a][:2]
    x1, y1 = CITIES[b][:2]
    mx, my = (x0 + x1) / 2.0, (y0 + y1) / 2.0
    dx, dy = x1 - x0, y1 - y0
    d = math.hypot(dx, dy) or 1
    px, py = -dy / d, dx / d
    if py > 0:                       # bow upward, over the desert rather than through the sea
        px, py = -px, -py
    k = min(30, d * 0.2)
    cx, cy = mx + px * k, my + py * k
    tx, ty = x1 - cx, y1 - cy
    t = math.hypot(tx, ty) or 1
    ex, ey = x1 - tx / t * 13, y1 - ty / t * 13
    ang = math.atan2(ey - cy, ex - cx)
    h = 7
    p1 = (ex - h * math.cos(ang - 0.5), ey - h * math.sin(ang - 0.5))
    p2 = (ex - h * math.cos(ang + 0.5), ey - h * math.sin(ang + 0.5))
    return ('<path d="M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f" fill="none" stroke="%s" stroke-width="2.6" stroke-linecap="round"/>'
            % (x0, y0, cx, cy, ex, ey, HOT)
            + '<path d="M%.1f,%.1f L%.1f,%.1f L%.1f,%.1f Z" fill="%s"/>' % (ex, ey, p1[0], p1[1], p2[0], p2[1], HOT))


def svg(cfg):
    out = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 460 250" width="460" height="250">',
           '<rect width="460" height="250" fill="%s"/>' % PARCH,
           '<path d="%s" fill="%s"/>' % (SEA, SEA_C),
           '<path d="%s" fill="%s"/>' % (GULF, SEA_C)]
    for r in (EUPHRATES, TIGRIS, NILE):
        out.append('<path d="%s" fill="none" stroke="%s" stroke-width="2.2" stroke-linecap="round"/>' % (r, RIVER))
    for x, y, s, anchor, size, fill, style in LABELS:
        out.append(text(x, y, s, anchor, size, fill, style))
    for a, b in cfg['arrows']:
        out.append(arrow(a, b))
    for cid, (x, y, label, anchor, dx, dy) in CITIES.items():
        if cid in cfg['cities']:
            out.append('<circle cx="%s" cy="%s" r="11" fill="none" stroke="%s" stroke-opacity=".45" stroke-width="2"/>' % (x, y, HOT))
            out.append('<circle cx="%s" cy="%s" r="6" fill="%s" stroke="#F2EAD9" stroke-width="2"/>' % (x, y, HOT))
            out.append(text(x + dx, y + dy, label, anchor, 14, INK, weight=700))
        elif cid in cfg['marked']:
            out.append('<circle cx="%s" cy="%s" r="5" fill="%s" stroke="#F2EAD9" stroke-width="2"/>' % (x, y, ORIGIN))
            out.append(text(x + dx, y + dy, label, anchor, 13, INK))
        elif cid in cfg['faint']:
            out.append('<circle cx="%s" cy="%s" r="3" fill="%s"/>' % (x, y, DIM))
            out.append(text(x + dx, y + dy, label, anchor, 11, FAINT))
    out.append('</svg>')
    return ''.join(out)


def figure(bid):
    cfg = BOOKS[bid]
    alt = 'Schematic map from the Nile to Persia, with %s marked.' % ', '.join(CITIES[c][2] for c in cfg['cities'])
    uri = 'data:image/svg+xml;base64,' + base64.b64encode(svg(cfg).encode('utf-8')).decode('ascii')
    return ('<figure class="mapfig" data-map="empire">\n'
            '      <img class="mapimg" loading="lazy" width="460" height="250" alt="%s" src="%s">\n'
            '      <figcaption><b>%s</b> %s</figcaption>\n'
            '    </figure>' % (alt, uri, cfg['lead'], cfg['caption']))


s = io.open(P, encoding='utf-8').read()
placed = replaced = 0
for bid in BOOKS:
    m = re.search(r'<section class="chapter" id="%s".*?(?=<section class="chapter")' % bid, s, re.S)
    assert m, bid
    sec = m.group(0)
    fig = figure(bid)
    if 'data-map="empire"' in sec:
        new = re.sub(r'<figure class="mapfig" data-map="empire">.*?</figure>', lambda _: fig, sec, count=1, flags=re.S)
        replaced += 1
    else:
        pm = re.search(r'<div class="prose">.*?</div>', sec, re.S)
        assert pm and 'book-body' not in sec, bid
        new = (sec[:pm.start()] + '<div class="book-body">\n    ' + pm.group(0)
               + '\n\n    ' + fig + '\n    </div>' + sec[pm.end():])
        placed += 1
    s = s[:m.start()] + new + s[m.end():]

io.open(P, 'w', encoding='utf-8').write(s)
print('empire map: %d placed, %d replaced; one plate is %d bytes'
      % (placed, replaced, len(svg(BOOKS['daniel']))))
