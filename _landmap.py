# -*- coding: utf-8 -*-
"""The land, lit eleven ways: the divided kingdom and the prophets who worked it.

The base drawing — coast, the two lakes, the Jordan, the region names, the
930 BC border — is the one already under the Joshua and 1 Kings plates, lifted
verbatim so a reader sees the same land every time. Each book lights the
kingdom, city or neighbour it is about, and draws the arrivals from off the
map: Assyria from the north-east, Babylon from the east.

Same pipeline as _paulmap.py: idempotent, base64 <img>, checked by verify.py.
"""
import base64
import io
import math
import re

P = 'index.html'

PARCH, SEA_C, INK, MUTED, FAINT = '#E4D8C0', '#C3D3D9', '#2E2519', '#6E6250', '#8A7E68'
HOT, ORIGIN, DIM = '#A8552E', '#6E5A2E', '#B3A68C'

# ------------------------------------------------------- the base plate
BASE = [
    '<rect width="340" height="460" fill="%s"/>' % PARCH,
    '<path d="M0,0 L119,0 C 128,57 119,115 102,172 C 90,200 68,218 34,253 L0,287 Z" fill="%s"/>' % SEA_C,
    '<ellipse cx="238" cy="80" rx="11" ry="16" fill="%s"/>' % SEA_C,
    '<path d="M206,192 L222,192 L219,252 L203,252 Z" fill="%s"/>' % SEA_C,
    '<path d="M236,96 C 230,130 222,160 213,190" fill="none" stroke="#7C9EAC" stroke-width="2.4" stroke-linecap="round"/>',
]
# regions as translucent shapes, drawn only when a book lights them
REGIONS = {
    'israel':    'M119,0 C128,57 119,115 102,172 L218,170 L236,96 L238,64 L238,0 Z',
    # the same ground under New Testament names
    'galilee':   'M119,0 C128,57 124,88 122,110 L236,110 L236,96 L238,64 L238,0 Z',
    'samaria':   'M122,110 C120,136 112,156 104,172 L218,170 L226,140 L236,110 Z',
    'judea':     'M104,172 L218,170 L206,192 L203,252 L196,300 L112,300 L82,258 C94,232 100,204 104,172 Z',
    'judah':     'M104,172 L218,170 L206,192 L203,252 L196,300 L112,300 L82,258 C94,232 100,204 104,172 Z',
    'philistia': 'M34,253 L0,287 L0,332 L112,300 L82,258 Z',
    'moab':      'M224,196 C250,188 280,190 304,198 C306,230 300,262 292,288 C268,292 240,280 219,252 Z',
    'edom':      'M192,296 C226,286 264,290 300,302 C304,330 300,356 292,378 C258,386 226,382 198,372 C188,348 186,320 192,296 Z',
}
REGION_LABEL = {   # x, y, text — where the base plate already puts them
    'israel': (124, 112, 'SAMARIA'), 'judah': (146, 224, 'JUDAH'), 'philistia': (28, 226, 'PHILISTIA'),
    'moab': (256, 240, 'MOAB'), 'edom': (238, 330, 'EDOM'),
}
FIXED_LABELS = [
    (30, 70, 'Mediterranean', 'start', 12, '#7C9EAC', True), (30, 86, 'Sea', 'start', 12, '#7C9EAC', True),
    (252, 50, 'GALILEE', 'start', 10, FAINT, False), (276, 168, 'AMMON', 'start', 10, FAINT, False),
    (228, 96, 'Sea of', 'start', 11, MUTED, None), (228, 108, 'Galilee', 'start', 11, MUTED, None),
    (198, 268, 'Dead Sea', 'middle', 11, MUTED, None),
]
BORDER = '<path d="M92,170 L262,170" fill="none" stroke="%s" stroke-width="2" stroke-dasharray="9 6" stroke-linecap="round" stroke-opacity=".55"/>'

# id: x, y, label, anchor, dx, dy
CITIES = {
    'dan':       (246, 32,  'Dan',       'start',  8,  -4),
    'samaria':   (170, 140, 'Samaria',   'start', 10,  -4),
    'bethel':    (173, 180, 'Bethel',    'end',   -7,  -2),
    'jerusalem': (175, 198, 'Jerusalem', 'end',   -7,  10),
    'tekoa':     (188, 218, 'Tekoa',     'start',  9,  13),
    'moresheth': (138, 212, 'Moresheth', 'end',   -6,  16),
    'hebron':    (168, 236, 'Hebron',    'end',   -7,   4),
}
# arrivals from off the map: where the arrow starts, and the label that names it
OFFMAP = {   # arrow start, title, sub-label, label anchor; the labels sit above the start
    'nineveh': ((334, 36), 'Assyria', 'from Nineveh', 'end'),
    'babylon': ((334, 158), 'Babylon', 'from the east', 'end'),
    'egypt':   ((8, 322), 'Egypt', 'the flight, and back', 'start'),
}

# book: dict(regions=[lit], cities=[lit], marked=[cities], arrows=[(from, to)],
#            offmap=[name], caption)
BOOKS = {
    'kings-2': dict(regions=['israel', 'judah'], cities=['samaria', 'jerusalem'], marked=['bethel'],
        arrows=[('nineveh', 'samaria'), ('babylon', 'jerusalem')],
        lead='Two capitals, two falls.',
        caption='Samaria to Assyria in 722 BC, Jerusalem to Babylon in 586. The book ends with both kingdoms gone and the land under other flags.'),
    'chronicles-1': dict(regions=[], cities=['jerusalem'], marked=['hebron'], arrows=[('hebron', 'jerusalem')],
        lead='From Hebron to Jerusalem.',
        caption='David reigns seven years in Hebron before taking Jerusalem. The north is here only as the tribes who came south to crown him.'),
    'chronicles-2': dict(regions=['judah'], cities=['jerusalem'], marked=['samaria'], arrows=[],
        lead='Judah only.',
        caption='The northern kingdom appears when Judah&rsquo;s kings marry into it, fight it, or take its refugees; its own story is not told.'),
    'hosea': dict(regions=['israel'], cities=['samaria'], marked=['bethel'], arrows=[],
        lead='The north, in its last thirty years.',
        caption='Hosea preaches in Israel, calls Bethel Beth-aven &mdash; house of nothing &mdash; and watches Samaria&rsquo;s kings come and go like twigs on the water.'),
    'joel': dict(regions=['judah'], cities=['jerusalem'], marked=[], arrows=[],
        lead='Jerusalem and the land around it.',
        caption='Stripped bare by locusts, then promised rain and the Spirit. No king is named and no date given, which is why the book has been placed anywhere from the ninth century to the fourth.'),
    'amos': dict(regions=['israel'], cities=['bethel'], marked=['tekoa'], arrows=[('tekoa', 'bethel')],
        lead='From Tekoa to Bethel.',
        caption='A shepherd from the hills of Judah walks north across the border to preach at the royal sanctuary of the other kingdom &mdash; and is told by its priest to go home.'),
    'obadiah': dict(regions=['edom'], cities=[], marked=['jerusalem'], arrows=[],
        lead='Edom, across the Dead Sea.',
        caption='Jacob&rsquo;s brother Esau, in the red hills to the south-east, who stood and watched while Jerusalem fell and then helped himself.'),
    'micah': dict(regions=['judah'], cities=['jerusalem', 'samaria'], marked=['moresheth'], arrows=[],
        lead='Both capitals, from the lowlands.',
        caption='Micah comes from Moresheth, a small town toward Philistia, and his first chapter takes Samaria and Jerusalem in turn: the same sins, the same end.'),
    'nahum': dict(regions=['judah'], cities=[], marked=['jerusalem'], arrows=[('jerusalem', 'nineveh')],
        lead='Nineveh, off this map.',
        caption='Five hundred and fifty miles to the north-east, up the Tigris. The good news for Judah, in the very first chapter, is that the Assyrians will not be coming back down this road.'),
    'habakkuk': dict(regions=['judah'], cities=['jerusalem'], marked=[], arrows=[('babylon', 'jerusalem')],
        lead='The Chaldeans, from the east.',
        caption='Habakkuk&rsquo;s complaint is not that Babylon is coming but that God is the one sending it, against a people who, whatever their faults, are better than their conquerors.'),
    'zephaniah': dict(regions=['philistia', 'moab', 'edom'], cities=['jerusalem'], marked=[], arrows=[],
        lead='Jerusalem first, then the neighbours.',
        caption='The day of the Lord lands on Judah in chapter one and works outward in chapter two &mdash; Philistia, Moab and Ammon, Cush, Assyria &mdash; before the book turns, at the last, to singing.'),
}


# ------------------------------------------------ the same land, AD 30
NT_CITIES = {
    'caesarea-philippi': (250, 18, 'Caesarea Philippi', 'start', 8, 4),
    'capernaum': (228, 62,  'Capernaum', 'end',   -8,  -4),
    'cana':      (208, 80,  'Cana',      'end',   -7,  -2),
    'nazareth':  (204, 98,  'Nazareth',  'end',   -8,   4),
    'sychar':    (172, 140, 'Sychar',    'start',  9,   4),
    'jericho':   (206, 176, 'Jericho',   'start',  9,  -3),
    'jerusalem': (175, 198, 'Jerusalem', 'end',   -7,  10),
    'bethany':   (186, 200, 'Bethany',   'start',  9,  -2),
    'bethlehem': (178, 214, 'Bethlehem', 'end',   -8,  20),
}
NT_LABELS = {
    'galilee': (252, 50, 'GALILEE'), 'samaria': (124, 112, 'SAMARIA'), 'judea': (118, 252, 'JUDEA'),
    'decapolis': (262, 130, 'DECAPOLIS'), 'perea': (262, 210, 'PEREA'), 'idumea': (140, 330, 'IDUMEA'),
}
GOSPELS = {
    'matthew': dict(era='nt', regions=['galilee'], cities=['bethlehem', 'jerusalem'], marked=['nazareth', 'capernaum'],
        arrows=[('bethlehem', 'egypt')],
        lead='Bethlehem, Egypt, Nazareth, Galilee, Jerusalem.',
        caption='Matthew&rsquo;s geography is a chain of fulfilments: born in Bethlehem as Micah said, called out of Egypt as Hosea said, settled in Nazareth, teaching in Galilee of the nations, and going up to Jerusalem to die.'),
    'mark': dict(era='nt', regions=['galilee'], cities=['capernaum', 'jerusalem'], marked=[],
        arrows=[('capernaum', 'jerusalem')],
        lead='One road.',
        caption='Half the book happens around Capernaum and the lake. Then in chapter ten Jesus turns south, and the road to Jerusalem is the other half. He goes to the city once and does not come back.'),
    'luke': dict(era='nt', regions=['galilee', 'samaria'], cities=['nazareth', 'jerusalem'], marked=['bethlehem'],
        arrows=[('nazareth', 'jerusalem')],
        lead='The long way to Jerusalem.',
        caption='Luke opens and closes in the temple. In between, from 9:51, Jesus sets his face toward Jerusalem and takes ten chapters to arrive &mdash; through Samaria, which the other gospels go around.'),
    'john': dict(era='nt', regions=[], cities=['jerusalem'], marked=['cana', 'sychar', 'bethany'], arrows=[],
        lead='Mostly Jerusalem.',
        caption='The other three keep Jesus in Galilee until the last week. John has him in Jerusalem for feast after feast, with excursions: water into wine at Cana, the well at Sychar, Lazarus at Bethany.'),
}
# what each era draws
LABELS = {'ot': REGION_LABEL, 'nt': NT_LABELS}
CITY_SETS = {'ot': CITIES, 'nt': NT_CITIES}
BEARINGS = {'ot': ('samaria', 'jerusalem'), 'nt': ('jerusalem',)}   # always there, faintly
ALT_PLACE = {'ot': 'Israel and Judah between the Mediterranean and the Jordan',
             'nt': 'Galilee, Samaria and Judea in the first century'}


def text(x, y, s, anchor='start', size=13, fill=INK, italic=False, sans=False, weight=None, spacing=None):
    fam = 'Helvetica,Arial,sans-serif' if sans else 'Georgia,serif'
    extra = ''
    if italic: extra += ' font-style="italic"'
    if weight: extra += ' font-weight="%s"' % weight
    if spacing: extra += ' letter-spacing="%s"' % spacing
    return ('<text x="%s" y="%s" text-anchor="%s" font-family="%s" font-size="%s" fill="%s"%s>%s</text>'
            % (x, y, anchor, fam, size, fill, extra, s))


def point(name):
    if name in OFFMAP:
        return OFFMAP[name][0]
    return (CITIES.get(name) or NT_CITIES[name])[:2]


def arrow(a, b, hot=True):
    """A route from a to b: a gentle curve, stopping short of the target's halo."""
    x0, y0 = point(a)
    x1, y1 = point(b)
    mx, my = (x0 + x1) / 2.0, (y0 + y1) / 2.0
    dx, dy = x1 - x0, y1 - y0
    d = math.hypot(dx, dy) or 1
    px, py = -dy / d, dx / d
    k = min(26, d * 0.18)
    cx, cy = mx + px * k, my + py * k
    tx, ty = x1 - cx, y1 - cy
    t = math.hypot(tx, ty) or 1
    gap = 6 if b in OFFMAP else 13
    ex, ey = x1 - tx / t * gap, y1 - ty / t * gap
    ang = math.atan2(ey - cy, ex - cx)
    h = 7
    p1 = (ex - h * math.cos(ang - 0.5), ey - h * math.sin(ang - 0.5))
    p2 = (ex - h * math.cos(ang + 0.5), ey - h * math.sin(ang + 0.5))
    col = HOT if hot else ORIGIN
    return ('<path d="M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f" fill="none" stroke="%s" stroke-width="2.6" stroke-linecap="round"/>'
            % (x0, y0, cx, cy, ex, ey, col)
            + '<path d="M%.1f,%.1f L%.1f,%.1f L%.1f,%.1f Z" fill="%s"/>' % (ex, ey, p1[0], p1[1], p2[0], p2[1], col))


def svg(cfg):
    out = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 340 460" width="340" height="460">'] + BASE[:]
    for rid in cfg['regions']:
        out.append('<path d="%s" fill="%s" fill-opacity=".2"/>' % (REGIONS[rid], HOT))
    era = cfg.get('era', 'ot')
    if era == 'ot':
        out.append(BORDER % ORIGIN)
    for x, y, s, anchor, size, fill, italic in FIXED_LABELS:
        if era == 'nt' and s in ('GALILEE', 'AMMON'):
            continue      # the era's own region names cover these
        out.append(text(x, y, s, anchor, size, fill, italic=bool(italic), sans=italic is not True,
                        weight=700 if italic is False else None, spacing=1.6 if italic is False else None))
    for rid, (x, y, s) in LABELS[era].items():
        lit = rid in cfg['regions']
        out.append(text(x, y, s, 'start', 10, HOT if lit else FAINT, sans=True, weight=700, spacing=1.6))
    # arrivals from off the map, named at the edge
    named = set()
    for a, b in cfg['arrows']:
        out.append(arrow(a, b, hot=True))
        for n in (a, b):
            if n in OFFMAP and n not in named:
                named.add(n)
                (x, y), title, sub, anchor = OFFMAP[n]
                lx = x - 2 if anchor == 'end' else x + 2
                out.append(text(lx, y - 20, title, anchor, 12.5, INK, weight=700))
                out.append(text(lx, y - 8, sub, anchor, 10, MUTED, sans=True))
    for cid, (x, y, label, anchor, dx, dy) in CITY_SETS[era].items():
        if cid in cfg['cities']:
            out.append('<circle cx="%s" cy="%s" r="11" fill="none" stroke="%s" stroke-opacity=".45" stroke-width="2"/>' % (x, y, HOT))
            out.append('<circle cx="%s" cy="%s" r="6" fill="%s" stroke="#F2EAD9" stroke-width="2"/>' % (x, y, HOT))
            out.append(text(x + dx, y + dy, label, anchor, 14, INK, weight=700))
        elif cid in cfg['marked']:
            out.append('<circle cx="%s" cy="%s" r="5" fill="%s" stroke="#F2EAD9" stroke-width="2"/>' % (x, y, ORIGIN))
            out.append(text(x + dx, y + dy, label, anchor, 13, INK))
        elif cid in BEARINGS[era]:
            # the two capitals are always there, faintly, for bearings
            out.append('<circle cx="%s" cy="%s" r="3" fill="%s"/>' % (x, y, DIM))
            out.append(text(x + dx, y + dy, label, anchor, 11, FAINT))
    out.append('</svg>')
    return ''.join(out)


def figure(bid):
    cfg = BOOKS[bid]
    era = cfg.get('era', 'ot')
    alt = ('Schematic map of ' + ALT_PLACE[era] + ', with %s marked.') % (
        ', '.join([LABELS[era][r][2].title() for r in cfg['regions']]
                  + [CITY_SETS[era][c][2] for c in cfg['cities']]) or 'the two kingdoms')
    uri = 'data:image/svg+xml;base64,' + base64.b64encode(svg(cfg).encode('utf-8')).decode('ascii')
    return ('<figure class="mapfig" data-map="land">\n'
            '      <img class="mapimg" loading="lazy" width="340" height="460" alt="%s" src="%s">\n'
            '      <figcaption><b>%s</b> %s</figcaption>\n'
            '    </figure>' % (alt, uri, cfg['lead'], cfg['caption']))


BOOKS.update(GOSPELS)

s = io.open(P, encoding='utf-8').read()
placed = replaced = 0
for bid in BOOKS:
    m = re.search(r'<section class="chapter" id="%s".*?(?=<section class="chapter")' % bid, s, re.S)
    assert m, bid
    sec = m.group(0)
    fig = figure(bid)
    if 'data-map="land"' in sec:
        new = re.sub(r'<figure class="mapfig" data-map="land">.*?</figure>', lambda _: fig, sec, count=1, flags=re.S)
        replaced += 1
    else:
        pm = re.search(r'<div class="prose">.*?</div>', sec, re.S)
        assert pm and 'book-body' not in sec, bid
        new = (sec[:pm.start()] + '<div class="book-body">\n    ' + pm.group(0)
               + '\n\n    ' + fig + '\n    </div>' + sec[pm.end():])
        placed += 1
    s = s[:m.start()] + new + s[m.end():]

io.open(P, 'w', encoding='utf-8').write(s)
print('land map: %d placed, %d replaced; one plate is %d bytes'
      % (placed, replaced, len(svg(BOOKS['kings-2']))))
