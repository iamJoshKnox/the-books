# -*- coding: utf-8 -*-
"""One map of Paul's world, lit thirteen ways.

The thirteen Pauline letters share a geography — the Aegean and the eastern
Mediterranean — so they share one drawing. Each letter's copy lights the city
it was sent to, marks the city it was sent from, and draws the route between.
Same schematic parchment style as the ten hand-drawn maps, and baked to a
base64 <img> for the same reason (see .mapimg in the stylesheet).

Idempotent: a figure it has already placed carries data-map="paul" and is
replaced in place. Run after build_spine.py; verify.py checks the result.
"""
import base64
import io
import math
import re

P = 'index.html'

# ------------------------------------------------------------- geography
# viewBox 460x250, matching the other plates. Everything is schematic.
SEA = ('M0,76 C50,82 100,72 150,78 C170,80 185,82 200,80 C225,78 245,82 262,80 '
       'C268,92 274,106 282,116 C292,126 310,132 330,134 C342,132 350,128 353,126 '
       'C358,144 354,165 350,182 C300,192 240,182 180,188 C120,194 60,184 0,190 Z')
ITALY = 'M124,60 C132,74 142,92 152,108 C158,118 166,126 170,132 C164,136 156,130 150,120 C140,104 128,84 118,66 Z'
GREECE = 'M192,60 C204,78 214,96 222,112 C226,120 228,128 224,132 C216,130 210,116 204,100 C198,86 190,72 186,62 Z'
CRETE = (246, 164, 18, 5.5)                 # cx, cy, rx, ry

PARCH, SEA_C, INK, MUTED, FAINT = '#E4D8C0', '#C3D3D9', '#2E2519', '#6E6250', '#8A7E68'
HOT, ORIGIN, DIM, HALO = '#A8552E', '#6E5A2E', '#B3A68C', '#A8552E'

# id: (x, y, label, anchor, dx, dy)
CITIES = {
    'rome':         (142, 92,  'Rome',         'end',    -8,  -4),
    'corinth':      (223, 118, 'Corinth',      'end',    -8,  12),
    'thessalonica': (238, 84,  'Thessalonica', 'end',    -7,  -6),
    'philippi':     (258, 78,  'Philippi',     'start',   7,  -5),
    'ephesus':      (280, 118, 'Ephesus',      'start',   6,  14),
    'colossae':     (306, 110, 'Colossae',     'start',   7,  -6),
    'galatia':      (340, 80,  'Galatia',      'middle',  0,   4),    # named inside its ring
    'crete':        (246, 164, 'Crete',        'start',  23,   4),
    'antioch':      (352, 126, 'Antioch',      'start',   7,  -5),
    'jerusalem':    (356, 172, 'Jerusalem',    'start',   7,   5),
}
REGION = {'galatia': (340, 80, 27, 10)}     # a district, not a city: dashed ellipse

# letter id: (to, from, caption). `from` may be None.
LETTERS = {
    'romans':          ('rome', 'corinth',
        'Written at the end of the third journey to a church Paul had never visited, '
        'ahead of a visit he meant to make on the way to Spain.'),
    'corinthians-1':   ('corinth', 'ephesus',
        'Across the Aegean to a church Paul had founded and was hearing bad reports of, '
        'answering their letter point by point.'),
    'corinthians-2':   ('corinth', 'philippi',
        'Written on the road south through Macedonia, after a painful visit and a harsher '
        'letter, before Paul arrived in person for the third time.'),
    'galatians':       ('galatia', 'antioch',
        'To the towns of the first journey &mdash; Pisidian Antioch, Iconium, Lystra, Derbe '
        '&mdash; on the traditional early dating, before the Jerusalem council.'),
    'ephesians':       ('ephesus', 'rome',
        'A prison letter, carried by Tychicus, to the city where Paul had stayed longer '
        'than anywhere else.'),
    'philippians':     ('philippi', 'rome',
        'A prison letter to the first church Paul planted in Europe, thanking them for a '
        'gift brought by Epaphroditus.'),
    'colossians':      ('colossae', 'rome',
        'A prison letter to a church Paul had never seen, in the Lycus valley inland from '
        'Ephesus, delivered together with Philemon.'),
    'thessalonians-1': ('thessalonica', 'corinth',
        'Written within months of leaving, once Timothy had come back with news that the '
        'church had survived.'),
    'thessalonians-2': ('thessalonica', 'corinth',
        'A follow-up from the same stay, correcting what the first letter had been taken '
        'to mean.'),
    'timothy-1':       ('ephesus', 'philippi',
        'From Macedonia to Timothy, left behind in Ephesus to sort out the church there.'),
    'timothy-2':       ('ephesus', 'rome',
        'Paul&rsquo;s last letter, from a second and harsher imprisonment, asking Timothy '
        'to come before winter.'),
    'titus':           ('crete', 'philippi',
        'From Macedonia, probably, to Titus, left on the island to appoint elders in every '
        'town; Paul planned to winter at Nicopolis.'),
    'philemon':        ('colossae', 'rome',
        'Carried with Colossians by Tychicus and Onesimus himself, to a house in the same '
        'town.'),
}
FROM_NAME = {'philippi': 'Macedonia'}     # the origin as the caption names it


def text(x, y, s, anchor='start', size=13, fill=INK, italic=False, sans=False, weight=None, spacing=None):
    fam = 'Helvetica,Arial,sans-serif' if sans else 'Georgia,serif'
    extra = ''
    if italic: extra += ' font-style="italic"'
    if weight: extra += ' font-weight="%s"' % weight
    if spacing: extra += ' letter-spacing="%s"' % spacing
    return ('<text x="%s" y="%s" text-anchor="%s" font-family="%s" font-size="%s" fill="%s"%s>%s</text>'
            % (x, y, anchor, fam, size, fill, extra, s))


def arrow(a, b):
    """A route from city a to city b: a curve bowed toward the open sea, with a head."""
    x0, y0 = CITIES[a][:2]
    x1, y1 = CITIES[b][:2]
    mx, my = (x0 + x1) / 2.0, (y0 + y1) / 2.0
    dx, dy = x1 - x0, y1 - y0
    d = math.hypot(dx, dy) or 1
    # perpendicular, pointed toward the middle of the sea so the curve crosses water
    px, py = -dy / d, dx / d
    if (px * (200 - mx) + py * (140 - my)) < 0:
        px, py = -px, -py
    k = min(34, d * 0.28)
    cx, cy = mx + px * k, my + py * k
    # stop short of the lit city's halo
    tx, ty = x1 - cx, y1 - cy
    t = math.hypot(tx, ty) or 1
    ex, ey = x1 - tx / t * 13, y1 - ty / t * 13
    ang = math.atan2(ey - cy, ex - cx)
    h = 7
    p1 = (ex - h * math.cos(ang - 0.5), ey - h * math.sin(ang - 0.5))
    p2 = (ex - h * math.cos(ang + 0.5), ey - h * math.sin(ang + 0.5))
    return ('<path d="M%.1f,%.1f Q%.1f,%.1f %.1f,%.1f" fill="none" stroke="%s" stroke-width="2.6" '
            'stroke-linecap="round"/>' % (x0, y0, cx, cy, ex, ey, HOT)
            + '<path d="M%.1f,%.1f L%.1f,%.1f L%.1f,%.1f Z" fill="%s"/>'
            % (ex, ey, p1[0], p1[1], p2[0], p2[1], HOT))


def svg(to, frm):
    out = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 460 250" width="460" height="250">',
           '<rect width="460" height="250" fill="%s"/>' % PARCH,
           '<path d="%s" fill="%s"/>' % (SEA, SEA_C),
           '<path d="%s" fill="%s"/>' % (ITALY, PARCH),
           '<path d="%s" fill="%s"/>' % (GREECE, PARCH),
           '<ellipse cx="%s" cy="%s" rx="%s" ry="%s" fill="%s"/>' % (CRETE + (PARCH,)),
           text(60, 48, 'EUROPE', 'start', 10.5, FAINT, sans=True, weight=700, spacing=1.8),
           text(296, 56, 'ASIA MINOR', 'start', 10.5, FAINT, sans=True, weight=700, spacing=1.8),
           text(80, 226, 'AFRICA', 'start', 10.5, FAINT, sans=True, weight=700, spacing=1.8),
           text(92, 142, 'Mediterranean Sea', 'middle', 13, '#7C9EAC', italic=True),
           text(250, 102, 'Aegean', 'middle', 10, '#7C9EAC', italic=True)]
    # the district, drawn under the dots
    for rid, (cx, cy, rx, ry) in REGION.items():
        lit = rid == to
        out.append('<ellipse cx="%s" cy="%s" rx="%s" ry="%s" fill="%s" fill-opacity="%s" stroke="%s" '
                   'stroke-width="1.6" stroke-dasharray="4 3"/>'
                   % (cx, cy, rx, ry, HOT if lit else DIM, '.22' if lit else '.12', HOT if lit else DIM))
    if frm:
        out.append(arrow(frm, to))
    for cid, (x, y, label, anchor, dx, dy) in CITIES.items():
        if cid in REGION:
            fill = HOT if cid == to else FAINT
            out.append(text(x + dx, y + dy, label, anchor, 12.5 if cid == to else 11.5, fill,
                            italic=True, weight=700 if cid == to else None))
            continue
        if cid == to:
            out.append('<circle cx="%s" cy="%s" r="11" fill="none" stroke="%s" stroke-opacity=".45" stroke-width="2"/>' % (x, y, HALO))
            out.append('<circle cx="%s" cy="%s" r="6" fill="%s" stroke="%s" stroke-width="2"/>' % (x, y, HOT, '#F2EAD9'))
            out.append(text(x + dx, y + dy, label, anchor, 14, INK, weight=700))
        elif cid == frm:
            out.append('<circle cx="%s" cy="%s" r="5" fill="%s" stroke="%s" stroke-width="2"/>' % (x, y, ORIGIN, '#F2EAD9'))
            out.append(text(x + dx, y + dy, label, anchor, 13, INK))
        else:
            out.append('<circle cx="%s" cy="%s" r="3" fill="%s"/>' % (x, y, DIM))
            out.append(text(x + dx, y + dy, label, anchor, 11, FAINT))
    out.append('</svg>')
    return ''.join(out)


def figure(bid):
    to, frm, cap = LETTERS[bid]
    name = lambda c: FROM_NAME.get(c, CITIES[c][2])
    lead = ('From %s to %s.' % (name(frm), name(to))) if frm else ('To %s.' % name(to))
    alt = ('Schematic map of the Aegean and eastern Mediterranean with %s marked%s.'
           % (name(to), (' and the route of the letter from %s' % name(frm)) if frm else ''))
    uri = 'data:image/svg+xml;base64,' + base64.b64encode(svg(to, frm).encode('utf-8')).decode('ascii')
    return ('<figure class="mapfig" data-map="paul">\n'
            '      <img class="mapimg" loading="lazy" width="460" height="250" alt="%s" src="%s">\n'
            '      <figcaption><b>%s</b> %s</figcaption>\n'
            '    </figure>' % (alt, uri, lead, cap))


s = io.open(P, encoding='utf-8').read()
placed = replaced = 0
for bid in LETTERS:
    m = re.search(r'<section class="chapter" id="%s".*?(?=<section class="chapter")' % bid, s, re.S)
    assert m, bid
    sec = m.group(0)
    fig = figure(bid)
    if 'data-map="paul"' in sec:
        new = re.sub(r'<figure class="mapfig" data-map="paul">.*?</figure>', lambda _: fig, sec, count=1, flags=re.S)
        replaced += 1
    else:
        pm = re.search(r'<div class="prose">.*?</div>', sec, re.S)
        assert pm and 'book-body' not in sec, bid
        new = (sec[:pm.start()] + '<div class="book-body">\n    ' + pm.group(0)
               + '\n\n    ' + fig + '\n    </div>' + sec[pm.end():])
        placed += 1
    s = s[:m.start()] + new + s[m.end():]

io.open(P, 'w', encoding='utf-8').write(s)
print('paul map: %d placed, %d replaced; one plate is %d bytes'
      % (placed, replaced, len(svg('rome', 'corinth'))))
