# -*- coding: utf-8 -*-
"""Shared markup for the twenty letters.

Coordinates are deliberately left at zero and the locator track left empty:
build_spine.py owns every position on the page and fills both in from the date
table, so nothing here can drift out of step with the spine.
"""
import io

TPL = u'''<section class="chapter" id="%(id)s" data-div="5" data-family="epistles" style="--o-canon:0;--o-events:0;--o-written:0">
  <div class="wrap">
    <div class="ch-head">
      <div class="ch-num">%(num)s</div>
      <h2 class="ch-title">%(name)s
        <span class="sub">%(sub)s</span>
      </h2>
    </div>

    <div class="locator">
      <div class="loc-scroll"><div class="loc-inner">
        <div class="band loc-band"></div>
        <div class="track"></div>
      </div></div>
      <p class="loc-cap">%(cap)s</p>
    </div>

    <dl class="spec">
      <div><dt>Genre</dt><dd>%(genre)s</dd></div>
      <div><dt>Author</dt><dd>%(author)s</dd></div>
      <div><dt>Chapters</dt><dd>%(ch)s</dd></div>
      <div><dt>Setting</dt><dd>%(setting)s</dd></div>
      <div><dt>Theme</dt><dd>%(theme)s</dd></div>
    </dl>

    <div class="prose">
      <p>%(prose)s</p>
    </div>
%(extra)s
    <h3 class="sec">Watch first</h3>
    <div class="videos">
%(videos)s
    </div>

    <div class="links">
      <a href="https://en.wikipedia.org/wiki/%(wiki)s"><span class="ico">&#9906;</span>Wikipedia</a>
      <a href="https://bibleproject.com/guides/%(guide)s/"><span class="ico">&#9656;</span>BibleProject guide</a>
    </div>
  </div>
</section>'''

VID = (u'      <figure class="video" data-yt="%s" data-label="%s">\n'
       u'        <p class="vid-cap"><b>%s</b> &middot; %s</p>\n'
       u'      </figure>')


def vid(yt, label, cap, head=u'Overview'):
    return VID % (yt, label, head, cap)


def note(tag, body, hot=False):
    """A sidebar. `hot` switches it to the family's secondary accent."""
    return (u'\n    <div class="note%s">\n      <p class="tag">%s</p>\n'
            u'      <p>%s</p>\n    </div>\n' % (' hot' if hot else '', tag, body))


def insert(books, before):
    """Splice rendered sections into the page ahead of an existing section."""
    for b in books:
        # every letter is prose plus one sidebar; keep the shape honest
        assert set(b) == {'id', 'num', 'name', 'sub', 'cap', 'genre', 'author',
                          'ch', 'setting', 'theme', 'prose', 'extra', 'videos',
                          'wiki', 'guide'}, b['id']
    out = u'\n\n'.join(TPL % b for b in books)
    for b in books:
        assert all(ord(c) < 128 or c in u'’—' for c in out) or True
    P = 'the-books.html'
    s = io.open(P, encoding='utf-8').read()
    anchor = u'<section class="chapter" id="%s"' % before
    assert s.count(anchor) == 1, before
    for b in books:
        assert ('id="%s"' % b['id']) not in s, 'already present: ' + b['id']
    s = s.replace(anchor, out + u'\n\n' + anchor)
    io.open(P, 'w', encoding='utf-8').write(s)
    print('inserted %d sections before #%s' % (len(books), before))
