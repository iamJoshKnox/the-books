# -*- coding: utf-8 -*-
"""Float the era band at the top of the spine while its rows scroll past.

Expanding a division pushes the era strip out of view, and without it the rows
are unreadable — a bar at 45% means nothing unless you can see that 45% is the
Divided Kingdom. So the strip and its colour band are lifted out of the rows'
scroll container into a page-level sticky header.

The lift is necessary: position:sticky resolves against the nearest scrolling
ancestor, and .spine-scroll is one (overflow-x:auto forces overflow-y to auto
too), so a sticky element inside it has no vertical range to travel in.
"""
import io, re

P = 'the-books.html'
s = io.open(P, encoding='utf-8').read()

def rep(o, n, c=1):
    global s
    assert s.count(o) == c, (o[:70], s.count(o))
    s = s.replace(o, n)

# ---------------------------------------------------------------- markup
m = re.search(r'    <div class="spine-scroll">\n      <div class="spine">\n'
              r'(        <div class="era-strip">\n.*?\n        </div>\n)'
              r'(        <div class="band" id="master-band">\n.*?\n        </div>\n)',
              s, re.S)
assert m, 'spine header markup not found'
strip_html, band_html = m.group(1), m.group(2)

new_head = ('    <div class="spine-head">\n'
            '      <div class="spine-head-scroll">\n'
            '        <div class="spine">\n'
            + strip_html + band_html +
            '        </div>\n'
            '      </div>\n'
            '    </div>\n\n'
            '    <div class="spine-scroll">\n'
            '      <div class="spine">\n')
s = s[:m.start()] + new_head + s[m.end():]

# ------------------------------------------------------------------- CSS
rep('.spine-scroll { overflow-x: auto; padding-bottom: .5rem; }',
    '''.spine-scroll { overflow-x: auto; padding-bottom: .5rem; }
/* The era band rides at the top of the spine so the rows stay readable: a bar
   at 45% means nothing unless you can see that 45% is the Divided Kingdom.
   It has to sit outside .spine-scroll — sticky resolves against the nearest
   scrolling ancestor, and that container scrolls. */
.spine-head {
  position: sticky; top: 0; z-index: 15;
  background: var(--surface-2);
  padding-top: .45rem;
  box-shadow: 0 8px 12px -10px rgba(0,0,0,.5);
}
.spine-head-scroll { overflow-x: auto; scrollbar-width: none; }
.spine-head-scroll::-webkit-scrollbar { height: 0; }''')

# -------------------------------------------------------------------- JS
rep('''  var master = document.getElementById("master-band");''',
    '''  /* the floating era band and the rows scroll horizontally together */
  var headScroll = document.querySelector(".spine-head-scroll");
  var rowScroll = document.querySelector(".spine-scroll");
  if (headScroll && rowScroll) {
    var syncing = false;
    function sync(from, to) {
      return function () {
        if (syncing) return;
        syncing = true;
        to.scrollLeft = from.scrollLeft;
        syncing = false;
      };
    }
    rowScroll.addEventListener("scroll", sync(rowScroll, headScroll), { passive: true });
    headScroll.addEventListener("scroll", sync(headScroll, rowScroll), { passive: true });
  }

  var master = document.getElementById("master-band");''')

io.open(P, 'w', encoding='utf-8').write(s)
print('era band lifted into a sticky header')
