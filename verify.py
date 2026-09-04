# -*- coding: utf-8 -*-
"""Check index.html against books.py and against itself.

Every audit that used to be run by hand in a browser console, in one place,
with one exit code. Run it after every build:

    python verify.py          structural checks, offline, a second or so
    python verify.py --net    also asks YouTube and Wikipedia whether every
                              video id and article slug still resolves

Exit status is 0 on PASS and 1 on FAIL, so it can sit in a hook or an Action.
"""
import io
import json
import re
import sys
import urllib.parse
import urllib.request

from books import BOOKS, DIVISIONS, ERAS

# an explicit path lets a deliberately broken copy prove the checks bite
P = next((a for a in sys.argv[1:] if not a.startswith('--')), 'index.html')
s = io.open(P, encoding='utf-8').read()

fails = []


def check(ok, what):
    if not ok:
        fails.append(what)
    return ok


def section(bid):
    """The markup of one chapter, from its <section> to the next chapter's."""
    m = re.search(r'<section class="chapter" id="%s".*?(?=<section class="chapter"|<section class="sources")'
                  % re.escape(bid), s, re.S)
    return m.group(0) if m else ''


# ------------------------------------------------------------ document
check(s.startswith('<!doctype html>'), 'first line is not <!doctype html>')
check('<html lang="en">' in s, 'missing <html lang="en">')
check('<meta charset="utf-8">' in s, 'missing <meta charset="utf-8">')
check('<meta name="viewport"' in s, 'missing viewport meta')
check(s.count('<body>') == 1 and s.count('</body>') == 1, 'body must open and close exactly once')
check('�' not in s, 'contains U+FFFD replacement characters (mojibake)')
for tag in ('name="description"', 'property="og:image"', 'rel="icon"', 'rel="canonical"'):
    check(tag in s, 'head is missing <meta/link %s>' % tag)
try:
    with open('og.png', 'rb') as fh:
        head = fh.read(24)
    check(head[:8] == b'\x89PNG\r\n\x1a\n' and int.from_bytes(head[16:20], 'big') == 1200
          and int.from_bytes(head[20:24], 'big') == 630, 'og.png is not a 1200x630 PNG')
except OSError:
    check(False, 'og.png is missing')

# ------------------------------------------------------------ chapters
ids = re.findall(r'<section class="chapter" id="([^"]+)"', s)
want = [b[0] for b in BOOKS]
check(ids == want, 'chapter ids are not the %d books of books.py in canonical order '
      '(page has %d; first difference at %s)'
      % (len(want), len(ids), next((i for i, (a, b) in enumerate(zip(ids, want)) if a != b), 'end')))

all_ids = re.findall(r'\sid="([^"]+)"', s)
dupes = sorted({i for i in all_ids if all_ids.count(i) > 1})
check(not dupes, 'duplicate ids: %s' % ', '.join(dupes))

for d, (name, n) in DIVISIONS.items():
    got = len(re.findall(r'<section class="chapter" id="[^"]+" data-div="%d"' % d, s))
    check(got == n, 'division %d (%s) has %d chapters, books.py says %d' % (d, name, got, n))
    check(len([b for b in BOOKS if b[3] == d]) == n,
          'books.py: division %d lists %d books but declares %d' % (d, len([b for b in BOOKS if b[3] == d]), n))
    lab = '%d books' % n
    check(('data-div="%d"' % d) in s and re.search(
        r'id="part-%d".*?<p class="div-count">%s</p>' % (d, lab), s, re.S) is not None,
        'division %d preface does not read "%s"' % (d, lab))

for bid, num, name, div, fam, ev, wrote, flag in BOOKS:
    sec = section(bid)
    check(bool(sec), 'no section for %s' % bid)
    if not sec:
        continue
    check(('data-family="%s"' % fam) in sec, '%s: family is not %s' % (bid, fam))
    check(('data-div="%d"' % div) in sec, '%s: division is not %d' % (bid, div))
    check(('<div class="ch-num">%s</div>' % num) in sec, '%s: chapter number is not %s' % (bid, num))
    check('data-yt="' in sec, '%s: no video' % bid)
    check('https://en.wikipedia.org/wiki/' in sec, '%s: no Wikipedia link' % bid)
    check('https://bibleproject.com/' in sec, '%s: no BibleProject link' % bid)
    check('<div class="track"></div>' not in sec, '%s: locator track was never filled' % bid)
    check(re.search(r'<div class="prose">\s*<p>', sec) is not None, '%s: no prose paragraph' % bid)

# ------------------------------------------------------------ the maps
PAUL = ('romans', 'corinthians-1', 'corinthians-2', 'galatians', 'ephesians', 'philippians',
        'colossians', 'thessalonians-1', 'thessalonians-2', 'timothy-1', 'timothy-2', 'titus', 'philemon')
for bid in PAUL:
    sec = section(bid)
    check('data-map="paul"' in sec and sec.count('<figure class="mapfig"') == 1,
          '%s: expected exactly one Paul map' % bid)
    check(sec.count('<div class="book-body">') == 1, '%s: map is not laid out beside the prose' % bid)
LAND = ('kings-2', 'chronicles-1', 'chronicles-2', 'hosea', 'joel', 'amos', 'obadiah', 'micah',
        'nahum', 'habakkuk', 'zephaniah', 'matthew', 'mark', 'luke', 'john',
        'judges', 'ruth', 'samuel-1', 'samuel-2', 'haggai', 'zechariah', 'malachi')
EMPIRE = ('isaiah', 'jeremiah', 'ezekiel', 'daniel', 'esther', 'nehemiah')
for kind, books in (('land', LAND), ('empire', EMPIRE)):
    for bid in books:
        sec = section(bid)
        check(('data-map="%s"' % kind) in sec and sec.count('<figure class="mapfig"') == 1,
              '%s: expected exactly one %s map' % (bid, kind))
        check(sec.count('<div class="book-body">') == 1, '%s: map is not laid out beside the prose' % bid)
mapped = len(re.findall(r'<figure class="mapfig"', s))
want_maps = 10 + len(PAUL) + len(LAND) + len(EMPIRE)
check(mapped == want_maps, 'expected %d map figures, found %d' % (want_maps, mapped))

# --------------------------------------------------------- read it
from books import USFM, ESV
for bid in want:
    sec = section(bid)
    href = 'https://www.bible.com/bible/%d/%s.1.ESV' % (ESV, USFM.get(bid, '???'))
    n = sec.count('<a class="read" href="%s">' % href)
    check(n == 1, '%s: expected one ESV link to %s, found %d' % (bid, href, n))
check(len(set(USFM.values())) == 66, 'USFM codes are not 66 distinct values')

# ------------------------------------------------------- reads with
# every book has a line, and every link on it has its mirror on the other book
links = {}
for bid in want:
    sec = section(bid)
    m = re.search(r'<p class="reads">(.*?)</p>', sec, re.S)
    check(m is not None, '%s: no "reads with" line' % bid)
    links[bid] = set(re.findall(r'<a href="#([^"]+)">', m.group(1))) if m else set()
    check(bool(links[bid]), '%s: "reads with" names no books' % bid)
for a, tos in links.items():
    for b in tos:
        check(b in links, '%s reads with %s, which is not a book' % (a, b))
        check(a in links.get(b, ()), '%s reads with %s but not the other way round' % (a, b))

# ---------------------------------------------------------- front matter
for stale in ('46 of 66', 'Built so far', 'slice-note', 'design slice', 'none built yet',
              'in progress</span>'):
    check(stale not in s, 'stale copy still present: %r' % stale)

# ----------------------------------------------------------- the spine
srows = re.findall(r'<div class="srow"', s)
check(len(srows) == len(BOOKS), 'spine has %d book rows, not %d' % (len(srows), len(BOOKS)))
chips = re.findall(r'<div class="bn-books" data-div="\d+"[^>]*>(.*?)</div>', s, re.S)
chip_hrefs = [h for blk in chips for h in re.findall(r'<a href="#([^"]+)"', blk)]
check(chip_hrefs == want, 'header chips are not the 66 books in canonical order')
js_eras = re.search(r'var ERAS = \[(.*?)\];', s, re.S)
check(js_eras is not None and js_eras.group(1).count('{ n:') == len(ERAS),
      'the JS ERAS array does not match books.py')
# ----------------------------------------------------- internal anchors
targets = set(all_ids)
markup = re.sub(r'<script>.*?</script>', '', s, flags=re.S)   # the JS builds selectors that look like hrefs
broken = sorted({h for h in re.findall(r'href="#([^"]+)"', markup) if h not in targets})
check(not broken, 'internal links to ids that do not exist: %s' % ', '.join(broken))

# --------------------------------------------------------- per-book accents
fams = {}
for b in BOOKS:
    fams.setdefault(b[4], []).append(b[0])
for fam, members in fams.items():
    if len(members) < 2:
        continue
    for bid in members:
        n = len(re.findall(r'#%s \{ --k-accent: #[0-9A-F]{6}; \}' % re.escape(bid), s))
        check(n == 3, '%s: expected 3 accent rules (one per theme block), found %d' % (bid, n))
check(s.count('/* ---------- per-book accent:') == 1, 'accent block is duplicated or missing')
hues = len(re.findall(r'--era-(\d+):', s)) // 3
check(hues == len(ERAS), 'stylesheet declares %d era hues, books.py has %d eras' % (hues, len(ERAS)))

# -------------------------------------------------------------- overflow
# the bar that runs off the end must be pinned to the end, or the spine grows a
# scrollbar for one pixel of overhang
check(re.search(r'\.track \.bar\.runs-off \{[^}]*right: 0;', s, re.S) is not None,
      '.track .bar.runs-off is not pinned to the right edge')


# ------------------------------------------------------------------ net
def net():
    vids = sorted(set(re.findall(r'data-yt="([^"]+)"', s)))
    wikis = sorted(set(re.findall(r'https://en\.wikipedia\.org/wiki/([^"]+)"', s)))
    print('net: %d video ids, %d Wikipedia articles' % (len(vids), len(wikis)))

    for v in vids:
        url = ('https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=%s&format=json' % v)
        try:
            with urllib.request.urlopen(url, timeout=20) as r:
                j = json.load(r)
            check('bibleproject' in j.get('author_name', '').lower(),
                  'video %s is not a BibleProject upload (%r)' % (v, j.get('author_name')))
        except Exception as e:
            check(False, 'video %s: %s' % (v, e))

    for bid, code in USFM.items():
        url = 'https://www.bible.com/bible/%d/%s.1.ESV' % (ESV, code)
        req = urllib.request.Request(url, method='HEAD', headers={'User-Agent': 'Mozilla/5.0 the-books verify.py'})
        try:
            with urllib.request.urlopen(req, timeout=20) as r:
                check(r.status == 200 and r.geturl() == url, 'bible.com: %s now %s -> %s' % (bid, r.status, r.geturl()))
        except Exception as e:
            check(False, 'bible.com: %s: %s' % (bid, e))

    titles = [urllib.parse.unquote(w).replace('_', ' ') for w in wikis]
    for i in range(0, len(titles), 50):
        batch = titles[i:i + 50]
        q = urllib.parse.urlencode({'action': 'query', 'titles': '|'.join(batch),
                                    'redirects': 1, 'format': 'json'})
        req = urllib.request.Request('https://en.wikipedia.org/w/api.php?' + q,
                                     headers={'User-Agent': 'the-books verify.py (iamjoshknox@gmail.com)'})
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                j = json.load(r)
        except Exception as e:
            check(False, 'wikipedia batch %d: %s' % (i // 50, e))
            continue
        for rd in j.get('query', {}).get('redirects', []):
            check(False, 'wikipedia: %r now redirects to %r' % (rd['from'], rd['to']))
        for pg in j.get('query', {}).get('pages', {}).values():
            check('missing' not in pg, 'wikipedia: %r does not exist' % pg.get('title'))


if '--net' in sys.argv:
    net()

# --------------------------------------------------------------- report
if fails:
    print('FAIL: %d problem%s' % (len(fails), '' if len(fails) == 1 else 's'))
    for f in fails:
        print('  - ' + f)
    sys.exit(1)
print('PASS: %d books, %d divisions, %d eras%s'
      % (len(BOOKS), len(DIVISIONS), len(ERAS), ', links live' if '--net' in sys.argv else ''))
