# -*- coding: utf-8 -*-
"""Generate every timeline coordinate in the-books.html from dates.

Positions used to be worked out by hand against era boundaries, which is fine
for five books and a liability for sixty-six: the spine has now been
re-proportioned twice, and each time every book's numbers had to be redone.
This holds the era table and the book dates, computes the rest, and rewrites
the file. Re-proportioning is now a one-line edit to ERAS.

Years are signed: -1406 is 1406 BC, 30 is AD 30.

Run from the bible/ directory: python build_spine.py
"""
import io, re, sys

# ---------------------------------------------------------------- eras
# (short name for locators, long name for the spine, date caption, width, from, to, knee)
#
# `knee` bends a band internally: (year, fraction) puts that year at that
# fraction of the band's width instead of where linear time would place it.
# Return & Second Temple runs 538-5 BC, but everything in it happens before
# 430 BC and the four centuries after are silence — so 430 BC sits at 70%,
# and the empty stretch is squeezed into the last 30%. Splitting it into two
# bands instead gave a 3%-wide band that could not carry a label.
ERAS = [
    ('Creation',    'Creation',              'before c. 2100 BC',  6, None,  -2100, None),
    ('Patriarchs',  'Patriarchs',            '2100&ndash;1876 BC', 7, -2100, -1876, None),
    ('Egypt',       'Egypt &amp; Exodus',    '1876&ndash;1406 BC', 9, -1876, -1406, None),
    ('Judges',      'Conquest &amp; Judges', '1406&ndash;1050 BC', 9, -1406, -1050, None),
    ('Monarchy',    'United Monarchy',       '1050&ndash;930 BC',  9, -1050, -930,  None),
    ('Divided',     'Divided Kingdom',       '930&ndash;586 BC',  12, -930,  -586,  None),
    ('Exile',       'Exile',                 '586&ndash;538 BC',   6, -586,  -538,  None),
    ('Return',      'Return &amp; Second Temple', '538&ndash;5 BC', 10, -538, -5,   (-430, 0.7)),
    ('Jesus',       'Life of Jesus',         '5 BC&ndash;AD 30',  12, -5,     30,   None),
    # Twenty-three books land in this band and seventeen of them inside a single
    # twenty-year stretch, so it takes two percent from the gospels' band and
    # bends the rest: AD 70 sits at 78%, which spreads the letters out and
    # squeezes the last thirty years, where only the Johannine writings remain.
    ('Apostolic',   'Apostolic Age',         'AD 30&ndash;100',   20, 30,    100,   (70, 0.78)),
]
assert sum(e[3] for e in ERAS) == 100, 'era widths must total 100'

BOUNDS = []
_c = 0
for e in ERAS:
    BOUNDS.append((_c, _c + e[3]))
    _c += e[3]

def pos(year):
    """Percentage along the spine for a signed year."""
    if year is None:
        return 0.0
    for i, (short, long_, cap, w, a, b, knee) in enumerate(ERAS):
        if a is None:
            continue
        if a <= year <= b:
            p0, p1 = BOUNDS[i]
            if knee:
                ky, kf = knee
                if year <= ky:
                    f = (year - a) / float(ky - a) * kf
                else:
                    f = kf + (year - ky) / float(b - ky) * (1 - kf)
            else:
                f = (year - a) / float(b - a)
            return round(p0 + f * (p1 - p0), 2)
    if year < -2100:
        return 0.0
    raise ValueError('year %s falls outside the era table' % year)

def fmt(x):
    return ('%g' % round(x, 2))

# --------------------------------------------------------------- books
# id, canonical no., display name, division, family, events (from, to), written,
# flags: runs_off | prologue (a faded bar back to the left edge)
MIN_BAR = 0.35   # a book covering a month still needs a visible bar

BOOKS = [
 ('genesis',      '01', 'Genesis',      1, 'torah',          (None, -1805), -1440, ''),
 ('exodus',       '02', 'Exodus',       1, 'torah',          (-1876, -1445), -1440, ''),
 ('leviticus',    '03', 'Leviticus',    1, 'torah',          (-1445, -1445), -1440, ''),
 ('numbers',      '04', 'Numbers',      1, 'torah',          (-1445, -1406), -1406, ''),
 ('deuteronomy',  '05', 'Deuteronomy',  1, 'torah',          (-1406, -1406), -1406, ''),
 ('joshua',       '06', 'Joshua',       2, 'historical',     (-1406, -1375), -1375, ''),
 ('judges',       '07', 'Judges',       2, 'historical',     (-1375, -1050), -1043, ''),
 ('ruth',         '08', 'Ruth',         2, 'historical',     (-1100, -1095), -1000, ''),
 ('samuel-1',     '09', '1 Samuel',     2, 'historical',     (-1105, -1010), -1000, ''),
 ('samuel-2',     '10', '2 Samuel',     2, 'historical',     (-1010, -970),  -960,  ''),
 ('kings-1',      '11', '1 Kings',      2, 'historical',     (-970,  -853),  -560,  ''),
 ('kings-2',      '12', '2 Kings',      2, 'historical',     (-853,  -586),  -560,  ''),
 ('chronicles-1', '13', '1 Chronicles', 2, 'historical',     (-1010, -970),  -430,  'prologue'),
 ('chronicles-2', '14', '2 Chronicles', 2, 'historical',     (-970,  -538),  -430,  ''),
 ('ezra',         '15', 'Ezra',         2, 'historical',     (-538,  -457),  -440,  ''),
 ('nehemiah',     '16', 'Nehemiah',     2, 'historical',     (-445,  -430),  -430,  ''),
 ('esther',       '17', 'Esther',       2, 'historical',     (-483,  -473),  -460,  ''),
 ('job',          '18', 'Job',          3, 'wisdom',         (-2000, -1950), -1400, ''),
 ('psalms',       '19', 'Psalms',       3, 'wisdom',         (-1440, -430),  -430,  ''),
 ('proverbs',     '20', 'Proverbs',     3, 'wisdom',         (-950,  -700),  -700,  ''),
 ('ecclesiastes', '21', 'Ecclesiastes', 3, 'wisdom',         (-940,  -935),  -935,  ''),
 ('song-of-songs','22', 'Song of Songs',3, 'wisdom',         (-970,  -965),  -965,  ''),
 ('isaiah',       '23', 'Isaiah',       3, 'prophets-major', (-740,  -681),  -681,  ''),
 ('jeremiah',     '24', 'Jeremiah',     3, 'prophets-major', (-627,  -580),  -580,  ''),
 ('lamentations', '25', 'Lamentations', 3, 'prophets-major', (-586,  -586),  -586,  ''),
 ('ezekiel',      '26', 'Ezekiel',      3, 'prophets-major', (-593,  -571),  -571,  ''),
 ('daniel',       '27', 'Daniel',       3, 'apocalyptic',    (-605,  -536),  -530,  ''),
 ('hosea',        '28', 'Hosea',        3, 'prophets-minor', (-755,  -715),  -715,  ''),
 ('joel',         '29', 'Joel',         3, 'prophets-minor', (-835,  -830),  -830,  ''),
 ('amos',         '30', 'Amos',         3, 'prophets-minor', (-760,  -750),  -750,  ''),
 ('obadiah',      '31', 'Obadiah',      3, 'prophets-minor', (-586,  -585),  -585,  ''),
 ('jonah',        '32', 'Jonah',        3, 'prophets-minor', (-780,  -778),  -760,  ''),
 ('micah',        '33', 'Micah',        3, 'prophets-minor', (-735,  -700),  -700,  ''),
 ('nahum',        '34', 'Nahum',        3, 'prophets-minor', (-663,  -640),  -640,  ''),
 ('habakkuk',     '35', 'Habakkuk',     3, 'prophets-minor', (-610,  -605),  -605,  ''),
 ('zephaniah',    '36', 'Zephaniah',    3, 'prophets-minor', (-640,  -630),  -630,  ''),
 ('haggai',       '37', 'Haggai',       3, 'prophets-minor', (-520,  -520),  -520,  ''),
 ('zechariah',    '38', 'Zechariah',    3, 'prophets-minor', (-520,  -480),  -480,  ''),
 ('malachi',      '39', 'Malachi',      3, 'prophets-minor', (-433,  -430),  -430,  ''),
 ('matthew',      '40', 'Matthew',      4, 'gospels',        (-5,     30),    60,   ''),
 ('mark',         '41', 'Mark',         4, 'gospels',        (27,     30),    55,   ''),
 ('luke',         '42', 'Luke',         4, 'gospels',        (-5,     30),    62,   ''),
 ('john',         '43', 'John',         4, 'gospels',        (27,     30),    90,   'prologue'),
 ('acts',         '44', 'Acts',         5, 'acts',           (30,     62),    62,   ''),
 ('romans',       '45', 'Romans',       5, 'epistles',       (57,     57),    57,   ''),
 ('corinthians-1','46', '1 Corinthians',5, 'epistles',       (55,     55),    55,   ''),
 ('corinthians-2','47', '2 Corinthians',5, 'epistles',       (56,     56),    56,   ''),
 ('galatians',    '48', 'Galatians',    5, 'epistles',       (48,     49),    48,   ''),
 ('ephesians',    '49', 'Ephesians',    5, 'epistles',       (60,     62),    60,   ''),
 ('philippians',  '50', 'Philippians',  5, 'epistles',       (61,     62),    61,   ''),
 # Colossians and Philemon went to the same town in the same hand, carried by
 # Tychicus and Onesimus together, so they share a span and split the lane
 ('colossians',   '51', 'Colossians',   5, 'epistles',       (60,     61),    60,   ''),
 ('thessalonians-1','52','1 Thessalonians',5,'epistles',     (50,     51),    50,   ''),
 ('thessalonians-2','53','2 Thessalonians',5,'epistles',     (51,     52),    51,   ''),
 ('timothy-1',    '54', '1 Timothy',    5, 'epistles',       (63,     64),    63,   ''),
 ('timothy-2',    '55', '2 Timothy',    5, 'epistles',       (66,     67),    66,   ''),
 ('titus',        '56', 'Titus',        5, 'epistles',       (63,     64),    63,   ''),
 ('philemon',     '57', 'Philemon',     5, 'epistles',       (60,     61),    60,   ''),
 ('hebrews',      '58', 'Hebrews',      5, 'epistles',       (65,     68),    65,   ''),
 ('james',        '59', 'James',        5, 'epistles',       (45,     46),    45,   ''),
 ('peter-1',      '60', '1 Peter',      5, 'epistles',       (62,     64),    62,   ''),
 # 2 Peter and Jude share most of a chapter of material as well as a decade
 ('peter-2',      '61', '2 Peter',      5, 'epistles',       (65,     67),    65,   ''),
 ('john-1',       '62', '1 John',       5, 'epistles',       (85,     95),    90,   ''),
 ('john-2',       '63', '2 John',       5, 'epistles',       (90,     95),    90,   ''),
 ('john-3',       '64', '3 John',       5, 'epistles',       (90,     95),    90,   ''),
 ('jude',         '65', 'Jude',         5, 'epistles',       (65,     67),    65,   ''),
 ('revelation',   '66', 'Revelation',   5, 'apocalyptic',    (95,    100),    95,   'runs_off'),
]

DIVISIONS = {1: ('Pentateuch', 5), 2: ('Historical Books', 12),
             3: ('Writings and Prophets', 22), 4: ('Gospels', 4),
             5: ('Acts, Letters and Revelation', 23)}

# ---------------------------------------------------- computed geometry
G = {}
for bid, num, name, div, fam, (ef, et), wrote, flag in BOOKS:
    a, b = pos(ef), pos(et)
    if b - a < MIN_BAR:
        # extend backwards, not forwards: a book covering a single month ends at
        # that moment, and growing it forwards pushes books sitting on an era
        # boundary (Deuteronomy, 1406 BC) into the following era by mistake
        a = b - MIN_BAR
    G[bid] = dict(a=a, b=b, p=pos(wrote), num=num, name=name, div=div,
                  fam=fam, flag=flag, wrote=wrote, mid=(a + b) / 2.0)

canon = {b[0]: (i + 1) * 10 for i, b in enumerate(BOOKS)}
events = {bid: (i + 1) * 10 for i, bid in enumerate(
    sorted(G, key=lambda k: (G[k]['mid'], canon[k])))}
written = {bid: (i + 1) * 10 for i, bid in enumerate(
    sorted(G, key=lambda k: (G[k]['wrote'], canon[k])))}
for bid in G:
    G[bid].update(o_canon=canon[bid], o_events=events[bid], o_written=written[bid])

# preface orders sit just before their division's first book
PREF = {}
for d in DIVISIONS:
    firsts = [canon[b[0]] for b in BOOKS if b[3] == d]
    PREF[d] = (min(firsts) - 5) if firsts else (
        max(canon[b[0]] for b in BOOKS if b[3] < d) + 5)

# =====================================================================
P = 'the-books.html'
s = io.open(P, encoding='utf-8').read()
edits = 0

def sub(pattern, repl, count=1, flags=0):
    global s, edits
    out, k = re.subn(pattern, repl, s, count=count, flags=flags)
    assert k == count, 'pattern matched %d times, wanted %d: %r' % (k, count, pattern[:60])
    s = out; edits += 1

# ---- era strip, colour band, and the JS array the locators read
strip = '\n'.join(
  '          <div class="era" style="--w:%d"><span class="era-name">%s</span>'
  '<span class="era-date">%s</span></div>' % (e[3], e[1], e[2]) for e in ERAS)
band = '\n'.join(
  '          <span class="seg" style="--w:%d; --c:var(--era-%d)"></span>' % (e[3], i + 1)
  for i, e in enumerate(ERAS))
sub(r'        <div class="era-strip">\n.*?\n        </div>',
    '        <div class="era-strip">\n%s\n        </div>' % strip, flags=re.S)
sub(r'        <div class="band" id="master-band">\n.*?\n        </div>',
    '        <div class="band" id="master-band">\n%s\n        </div>' % band, flags=re.S)
js = ',\n'.join('    { n: "%s", w: %d }' % (e[0], e[3]) for e in ERAS)
sub(r'  var ERAS = \[\n.*?\n  \];', '  var ERAS = [\n%s\n  ];' % js, flags=re.S)

# The --era-N hues live in the stylesheet, not here: they change rarely, and an
# earlier version of this script appended one on every run, which duplicated the
# declaration each time it was re-run. Adding an era means adding its colour to
# all three theme blocks by hand; the assertion below catches it if you forget.
declared = len(re.findall(r'--era-(\d+):', s)) // 3
assert declared == len(ERAS), (
    'stylesheet declares %d era hues but the table has %d — add --era-%d to all '
    'three theme blocks' % (declared, len(ERAS), len(ERAS)))

# ------------------------- push the coordinates into every book and the spine
EVENTS = {b[0]: b[5] for b in BOOKS}

def yr(y):
    if y is None:
        return 'creation'
    return ('%d BC' % -y) if y < 0 else ('AD %d' % y)

def span_label(bid):
    """Human-readable span of narrated events, for the timeline tooltip.

    Every date here is a traditional reckoning and approximate, so they carry
    "c." — matching the locator captions. One "c." governs a whole range, and
    the era suffix is only repeated when the range crosses BC into AD.
    Creation is not a date and takes no hedge.
    """
    a, b = EVENTS[bid]
    if a is None:
        return 'creation &ndash; c. %s' % yr(b)
    if a == b:
        return 'c. %s' % yr(a)
    if a < 0 and b < 0:
        return 'c. %d &ndash; %d BC' % (-a, -b)
    if a > 0 and b > 0:
        return 'c. AD %d &ndash; %d' % (a, b)
    return 'c. %s &ndash; %s' % (yr(a), yr(b))

def track(g, bid, link=True, label=False):
    """One book's timeline row.

    link=True   bar and dot are anchors to the book (the spine's book rows)
    link=False  same tooltips, no navigation (the locator inside that book)
    label=True  print the book's name at the start of the row, unless its bar
                reaches the left edge and would sit underneath it
    """
    pro = ('<span class="bar prologue" style="--a:0; --b:%s"></span>' % fmt(g['a'])
           if g['flag'] == 'prologue' else '')
    cls = ' runs-off' if g['flag'] == 'runs_off' else ''
    # the dot keeps its "c." — a composition date is a good deal more
    # speculative than the span of events a book narrates
    span = span_label(bid)
    if g['flag'] == 'runs_off':
        # the upper bound is where the chart stops, not where the book does
        span = span.split('&ndash;')[0].rstrip() + ' onward'
    tb = ' data-tip="%s|%s"' % (g['name'], span)
    # A 12px dot covers an 8px bar, so on point-in-time books the dot wins the
    # hover and the span of events becomes unreachable. Carry both there.
    if g['a'] <= g['p'] <= g['b']:
        td = ' data-tip="%s|%s &middot; written c. %s"' % (g['name'], span, yr(g['wrote']))
    else:
        td = ' data-tip="%s|written c. %s"' % (g['name'], yr(g['wrote']))
    if link:
        bar = ('<a class="bar%s" href="#%s" style="--a:%s; --b:%s"%s></a>'
               % (cls, bid, fmt(g['a']), fmt(g['b']), tb))
        dot = ('<a class="dot" href="#%s" style="--p:%s"%s></a>'
               % (bid, fmt(g['p']), td))
    else:
        bar = ('<span class="bar%s" style="--a:%s; --b:%s"%s></span>'
               % (cls, fmt(g['a']), fmt(g['b']), tb))
        dot = '<span class="dot" style="--p:%s"%s></span>' % (fmt(g['p']), td)

    lab = ''
    if label:
        # rough width of the label as a percentage of the row, plus a gap
        need = len(g['name']) * 0.8 + 1.5
        if g['a'] > need:
            lab = '<span class="loc-name">%s</span>' % g['name']
    return '<div class="track">%s%s%s%s</div>' % (lab, pro, bar, dot)

built = []
for bid in [b[0] for b in BOOKS]:
    g = G[bid]
    m = re.search(r'<section class="chapter" id="%s"' % re.escape(bid), s)
    if not m:
        continue                                    # section not written yet
    built.append(bid)
    nxt = s.find('<section ', m.end())
    end = nxt if nxt > 0 else len(s)
    seg = s[m.start():end]
    seg = re.sub(r'<div class="track">.*?</div>',
                 track(g, bid, link=False, label=True), seg, count=1, flags=re.S)
    seg = re.sub(r'style="--o-canon:\d+;--o-events:\d+;--o-written:\d+"',
                 'style="--o-canon:%d;--o-events:%d;--o-written:%d"'
                 % (g['o_canon'], g['o_events'], g['o_written']), seg, count=1)
    # the header's division buttons need to find their books in any sort order
    seg = re.sub(r'(<section class="chapter" id="%s")(?: data-div="\d+")?' % re.escape(bid),
                 r'\1 data-div="%d"' % g['div'], seg, count=1)
    s = s[:m.start()] + seg + s[end:]
    edits += 1

def srow(bid):
    g = G[bid]
    return ('          <div class="srow">\n'
            '            <a class="srow-name" href="#%s">%s</a>\n'
            '            %s\n          </div>'
            % (bid, g['name'], track(g, bid=bid)))

def count_label(built, total):
    """A finished division just states its size; an unfinished one shows progress."""
    if built == total:
        return '%d book%s' % (total, '' if total == 1 else 's')
    return '%d of %d' % (built, total)

DIVNAME = {d: DIVISIONS[d][0] for d in DIVISIONS}
GHOST = {2: ('1 Chronicles &ndash; Esther', 34, 65)}   # not yet built
groups = []
for d in sorted(DIVISIONS):
    rows = [srow(b) for b in built if G[b]['div'] == d]
    if d in GHOST and DIVISIONS[d][1] > len(rows):
        lbl, ga, gb = GHOST[d]
        rows.append('          <div class="srow ghostrow">\n'
                    '            <span class="srow-name">%s</span>\n'
                    '            <div class="track"><span class="bar" style="--a:%s; --b:%s">'
                    '</span></div>\n          </div>' % (lbl, fmt(ga), fmt(gb)))
    # Collapsed view: every bar in the division stacked in one translucent
    # track, so where books overlap the row simply gets darker. No dots —
    # twenty-two of them in one row is noise. Dots return on expand.
    #
    # Emitted widest first so the narrowest bar paints last: it ends up on top,
    # which also means it wins the hover and its tooltip is the one you get.
    # Without that, a book covering a single month is unreachable underneath
    # one covering four centuries.
    mine = [b for b in built if G[b]['div'] == d]

    # Books covering exactly the same stretch cannot be told apart by width, so
    # they split the track's height into lanes instead: Matthew and Luke both
    # run 5 BC-AD 30, and become top half and bottom half of the same stripe.
    lanes = {}
    for b in mine:
        lanes.setdefault((G[b]['a'], G[b]['b']), []).append(b)
    lane_of = {}
    for key, group in lanes.items():
        for i, b in enumerate(group):
            lane_of[b] = (i, len(group))

    spans = [(G[b]['b'] - G[b]['a'], b, None) for b in mine]
    if d in GHOST and DIVISIONS[d][1] > len(mine):
        lbl, ga, gb_ = GHOST[d]
        spans.append((gb_ - ga, None, (lbl, ga, gb_)))
    spans.sort(key=lambda t: -t[0])

    dens = []
    for _w, b, gh in spans:
        if gh:
            lbl, ga, gb_ = gh
            dens.append('<span class="bar" style="--a:%s; --b:%s" data-tip="%s|not built yet">'
                        '</span>' % (fmt(ga), fmt(gb_), lbl))
            continue
        gb = G[b]
        cls = ' runs-off' if gb['flag'] == 'runs_off' else ''
        lane, count = lane_of[b]
        lane_css = ''
        if count > 1:
            lane_css = '; --lane:%d; --lanes:%d' % (lane, count)
            cls += ' laned'
        tip = span_label(b)
        if gb['flag'] == 'runs_off':
            tip = tip.split('&ndash;')[0].rstrip() + ' onward'
        if count > 1:
            others = [G[o]['name'] for o in lanes[(gb['a'], gb['b'])] if o != b]
            tip += ' &middot; same years as ' + ', '.join(others)
        dens.append('<a class="bar%s" href="#%s" style="--a:%s; --b:%s%s" data-tip="%s|%s"></a>'
                    % (cls, b, fmt(gb['a']), fmt(gb['b']), lane_css, gb['name'], tip))
    groups.append(
        '        <div class="sgroup" data-div="%d">\n'
        '          <div class="sgroup-head">\n'
        '            <button class="sgroup-lab" type="button" aria-expanded="false">'
        '<span class="sg-chev" aria-hidden="true">&#9656;</span>'
        '<span class="sg-name">%s</span>'
        '<span class="sg-n">%s</span></button>\n'
        '            <div class="track density">%s</div>\n'
        '          </div>\n'
        '          <div class="sgroup-books">\n%s\n          </div>\n'
        '        </div>'
        % (d, DIVNAME[d], count_label(len(mine), DIVISIONS[d][1]),
           ''.join(dens), '\n'.join(rows)))
# Anchored to the real close: the .spine-rows </div> is the one followed by the
# </div> that closes .spine. A plain non-greedy match stopped at the first nested
# </div> and left four orphaned groups rendering under the chart; a plain greedy
# one ran to the last </div> in the file and swallowed the table of contents.
sub(r'        <div class="spine-rows">\n.*?\n        </div>\n(?=      </div>)',
    '        <div class="spine-rows">\n%s\n        </div>\n' % '\n'.join(groups), flags=re.S)

# Header nav: five division buttons rather than a chip row that would be 66
# wide. A division expands its own books and scrolls to itself.

# Chip labels only. Acts, Letters and Revelation is twenty-three books and
# wrapped to three rows, which took the floating header to ~220px and left
# almost no clearance above an anchored title. Contracting the six longest
# names buys back a row. Everywhere else -- section headings, spine tooltips,
# the table of contents -- keeps the full name, and the chip carries it as an
# aria-label so nothing is lost to a screen reader.
SHORT = {
    'corinthians-1':   '1 Cor.',
    'corinthians-2':   '2 Cor.',
    'thessalonians-1': '1 Thess.',
    'thessalonians-2': '2 Thess.',
    'timothy-1':       '1 Tim.',
    'timothy-2':       '2 Tim.',
}


def chip_label(b):
    return SHORT.get(b, G[b]['name'])


def aria(b):
    return ' aria-label="%s"' % G[b]['name'] if b in SHORT else ''


btns = ['      <a class="bn-spine" href="#spine">&uarr; The spine</a>']
rows_html = []
for d in sorted(DIVISIONS):
    mine = [b for b in built if G[b]['div'] == d]
    # An anchor, not a button: native anchor navigation resolves correctly
    # against content-visibility placeholders, where scrollIntoView does not.
    btns.append('      <a class="bn-div" href="#part-%d" data-div="%d" aria-expanded="false">'
                '%s <span class="bn-n">%d</span></a>' % (d, d, DIVNAME[d], len(mine)))
    chips = '\n'.join(
      '        <a href="#%s"%s style="--o-canon:%d;--o-events:%d;--o-written:%d">'
      '<span class="n">%s</span>%s</a>'
      % (b, aria(b), G[b]['o_canon'], G[b]['o_events'], G[b]['o_written'],
         G[b]['num'], chip_label(b))
      for b in mine)
    if not chips:
        chips = '        <span class="n">none built yet</span>'
    rows_html.append('      <div class="bn-books" data-div="%d" hidden>\n%s\n      </div>'
                     % (d, chips))
nav = ('<nav class="booknav" aria-label="Sections">\n'
       '  <div class="booknav-inner">\n'
       '    <div class="booknav-row">\n%s\n    </div>\n%s\n  </div>\n</nav>'
       % ('\n'.join(btns), '\n'.join(rows_html)))
sub(r'<nav class="booknav" aria-label="Sections">\n.*?</nav>', nav, flags=re.S)

for d in sorted(DIVISIONS):
    n_built = len([b for b in built if G[b]['div'] == d])
    sub(r'(id="part-%d" data-div="%d" )style="[^"]*"' % (d, d),
        r'\1style="--o-canon:%d;--o-events:%d;--o-written:%d"'
        % (PREF[d], PREF[d], PREF[d]))
    m = re.search(r'(id="part-%d".*?<p class="div-count">)[^<]*(</p>)' % d, s, re.S)
    assert m, d
    label = count_label(n_built, DIVISIONS[d][1])
    if n_built != DIVISIONS[d][1]:
        label += ' built'
    s = s[:m.start()] + m.group(1) + label + m.group(2) + s[m.end():]
    edits += 1

print('eras: %d bands, boundaries %s' % (len(ERAS), [b[0] for b in BOUNDS] + [100]))
print('books: %d of %d written' % (len(built), len(BOOKS)))
for bid in ('genesis', 'joshua', 'kings-2', 'psalms', 'matthew', 'revelation'):
    if bid in G:
        g = G[bid]
        print('  %-12s bar %5s-%-5s dot %-5s  canon %3d events %3d written %3d'
              % (bid, fmt(g['a']), fmt(g['b']), fmt(g['p']),
                 g['o_canon'], g['o_events'], g['o_written']))

io.open('_coords.py', 'w', encoding='utf-8').write(
    '# generated by build_spine.py\nG = %r\nPREF = %r\n' % (G, PREF))
io.open(P, 'w', encoding='utf-8').write(s)
print('applied: %d edits' % edits)
