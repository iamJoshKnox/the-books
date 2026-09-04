# The Books — backlog

Written 3 Sep 2026, against the 66-of-66 build. Ordered by what it costs to
leave alone, not by what it costs to do. Effort is S (under an hour), M (an
afternoon), L (a day or more).

---

## Done — 3 Sep 2026

**1–4, the whole P0 block, plus the chip abbreviations.** Verified in Chrome:
`document.compatMode` is now `CSS1Compat`, `documentElement.lang` is `en`,
`characterSet` is `UTF-8`, the viewport meta is present, and the document has a
real `<body>`. 66 chapters, no duplicate ids, no surviving "46 of 66".

The six longest chip labels contract to `1 Cor.` / `2 Cor.` / `1 Thess.` /
`2 Thess.` / `1 Tim.` / `2 Tim.`, each carrying the full name as an
`aria-label`. **Acts, Letters and Revelation now fits two rows instead of
three:** the header goes 220px → 187px and clearance above an anchored book's
title goes **29px → 62px**. Writings and Prophets (22 books) rides along at the
same two rows. The single-row divisions are unchanged at 96px of clearance.

Original text of items 1–4 is in git — or would be, if item 9 were done.

---

## P0 — wrong on the page right now

*(all cleared; kept for the record)*

**1. Four stale "46 of 66" claims.** (S) &mdash; done
The build finished; the front matter did not. All four are visible copy:
- line 1371, `.slice-note`: *"Design slice — 46 of 66 books built … Only the letters remain."*
- line 1374, `.facts`: *"Built so far — 46 books"* and its `<small>`
- line 1377, `.facts`: *"9 palettes — All nine defined, eight in use here"* — all nine are now in use
- line 5753, `<footer>`: *"46 of 66 built · design slice"*

The slice-note element should probably be deleted outright rather than
updated; it existed to explain an incomplete page.

**2. No `<meta charset="utf-8">`.** (S)
The file contains 22 raw U+2014 em-dashes. Everything else is entities, so
this went unnoticed. Served over `http.server` the response header rescues it;
opened from disk with a double-click it will not, and those 22 spots render as
`â€"`. One line in the head fixes it — or normalise the 22 to `&mdash;` and
add the meta anyway.

**3. No `<meta name="viewport">`.** (S)
This is the significant one. Without it, mobile Safari and Chrome lay the page
out at a 980px virtual viewport and scale down, so **none of the thirteen
`max-width` breakpoints in the stylesheet ever fire.** All that responsive
work — `.numline` stacking, `.rails` collapsing, `.treaty` dropping a column —
is currently dead code on the devices it was written for. Adding the meta will
*change the mobile layout substantially*, which means it needs a real pass on
a phone afterwards, not just the one line.

**4. No doctype, no `<html>`, `<head>` or `<body>`.** (S)
The file starts at `<title>`. Browsers recover and build the tree, but with no
doctype the document is in **quirks mode**. It looks correct today because the
stylesheet sets `box-sizing` explicitly; it is still a bad footing for a page
this geometric, and it costs one line. Add `<!doctype html>` and
`<html lang="en">` — the `lang` also matters for screen readers and for
hyphenation of the long prose paragraphs.

---

## P1 — the site is unusable in ways we have not tested

**4a. `alignToHash` corrects with `behavior: "auto"`.** (S, but verify carefully)
Found while verifying the P0 block. The stylesheet sets
`html { scroll-behavior: smooth }`, and per spec `behavior: "auto"` means *use
the element's CSS scroll-behavior* &mdash; so it resolves to **smooth**, not to
"don't animate", which is what the call site plainly intends. That makes every
one of the ten 60ms correction nudges start a fresh animation that the next
nudge interrupts, so the loop can expire long before it converges. This is the
likely mechanism behind the landing-a-hair-off symptom that ANCHOR_TOP was
introduced to chase.

The fix is not simply `behavior: "instant"`. The animated travel to a book is
wanted &mdash; *"I still do want to preserve that scrolling down to the book in
question feel"* &mdash; and that travel comes from the browser's own fragment
navigation, which honours the smooth CSS. An instant nudge fired while that
animation is still running would cancel it and teleport. So the correction pass
needs to **wait for the travel to settle, then correct instantly**, reusing the
`armSettle` machinery that already exists a few lines below. Worth doing, worth
testing on a real machine rather than under automation &mdash; see the note
below.

**Note on verifying any of this.** Smooth scrolling is a complete no-op in the
Chrome instance driving these checks: `scrollBy({behavior:'instant'})` moves the
page, `'auto'` and `'smooth'` do nothing at all. Programmatic scrolling is also
gesture-gated until the tab receives a real click or wheel event, and scroll
events raised from the extension's isolated world do not reach the page's own
listener, so the scroll-spy never fires under instrumentation (confirmed
identical on the pre-P0 file, so it is the harness, not the page). Anchor
geometry can still be checked by converging by hand with instant scrolls
&mdash; all eight books tested land at exactly `top: 165`. Chip behaviour
cannot be checked this way at all and needs a human with a mouse.

**5. Tooltips are mouse-only.** (M)
Wiring is `mouseover` / `mousemove` / `mouseout` and nothing else. Two
consequences:
- **On touch there are no tooltips at all.** Every timeline bar is an `<a>`,
  so a tap navigates. On a phone the spine is a wall of unlabelled colour.
- **The lane-split is unreachable there.** The top-half/bottom-half mechanism —
  the nicest idea on the page, and the only way to discover Philemon behind
  Colossians — has no touch equivalent whatsoever.

Proposal: move to pointer events, and on `pointerType === 'touch'` make the
first tap show the tooltip and the second follow the link. For the lane pairs,
a tap could cycle: Colossians → Philemon → navigate.

**6. Tooltips do not appear on focus.** (S)
Same handler, same fix — add `focusin`/`focusout` to whatever `mouseover`
does. Cheap, and it is what makes the spine legible to a keyboard user.

**7. ~130 tab stops before the first paragraph.** (M)
66 bars plus 66 written-dots are all focusable `<a>`s in the spine, ahead of
all the content. Tabbing into the page is currently a punishment. Wants either
a roving `tabindex` (one stop for the spine, arrow keys within it) or a
skip-link, and probably both.

**8. Mobile pass on the floating header.** (M)
Half-addressed: at desktop width the 23-book strip is now two rows, a 187px
header and 62px of clearance. But item 3 has landed, so the real breakpoints
now engage on a phone for the first time and none of them has ever been seen.
Twenty-three chips at 390px will wrap far past two rows. Options: scroll the
chip strip horizontally instead of wrapping, or collapse it to the current book
plus a count. Needs a real handset, or at least a device-emulation pass.

---

## P2 — process, and the risk of losing the thing

**9. The project is not under version control.** (S to fix, large to regret)
`git rev-parse` says no. There is a 489KB hand-tuned artifact here, eight
build scripts, and a 29KB design brief, with no history and no way to see what
a re-run of `_accents.py` changed. We have already had one incident where a
non-idempotent generator appended a duplicate 200-line block and the recovery
was a copy in the temp directory. `git init` plus a first commit is ten
minutes and removes an entire category of bad day. (OneDrive versioning is not
a substitute — it is per-file and has no diff.)

**10. Split-brain source of truth.** (M)
`build_spine.py` owns every date and position. The prose, specs and sidebars
now live only in the HTML — `_letters_a/b/c.py` were one-shot inserters and
are dead weight that still look authoritative. Nothing enforces which file
wins. Proposal: a single `books.py` holding the 66-row table (dates, family,
division, wiki slug, video id), with the HTML explicitly the store for prose
only, and a comment at the top of each script saying so. Delete or clearly
retire the `_letters_*` files.

**11. No automated verification.** (M)
Every audit so far has been ad hoc: chapter count, duplicate ids, per-division
counts, unfilled locator tracks, division labels, anchor accuracy. Fold them
into `verify.py` so a build ends with a pass/fail instead of a browser
session. Add a `--net` mode that re-checks the 21 YouTube ids through oEmbed
and the 63 Wikipedia targets through the MediaWiki API — those are the two
things that will rot without any local change.

**12. Bake the `contain-intrinsic-size` values.** (M)
The estimates are close enough that scrolling is smooth, but they are wrong
enough that the document grew ~5,000px between two measurements during
testing, which is what made the scroll-spy look broken when it was not.
Measure the 66 real heights once with the sections forced visible, and emit
per-section values from `build_spine.py`. Removes the last source of scroll
jitter and makes the scrollbar honest.

---

## P3 — content the structure is already asking for

**13. Maps for the other 56 books.** (L, but divisible)
Ten books have one: Genesis, Exodus, Numbers, Deuteronomy, Joshua, 1 Kings,
Ezra, Jonah, Acts, Revelation. The cheapest large win is **one shared "Paul's
world" map** — the Aegean and the eastern Mediterranean — reused across all
thirteen Pauline letters with only the destination city lit. Thirteen books
covered for roughly the cost of one map. After that, in value order: the
divided kingdom (serves Kings, Chronicles and most of the minor prophets), the
empires (Isaiah, Jeremiah, Ezekiel, Daniel, Esther, Nehemiah), and Galilee and
Judea (the four gospels).

**14. "Read next" cross-references.** (M)
The lane-splitting already found the pairs; the page does not yet say so.
Kings ↔ Chronicles, Luke ↔ Acts, Colossians ↔ Philemon, 2 Peter ↔ Jude,
Jeremiah ↔ Lamentations, Ezra ↔ Nehemiah ↔ Haggai ↔ Zechariah, 1 Timothy ↔
Titus. A single line under the spec block — *"Reads with: …"* — turns 66 rooms
into a connected building, and the relationships are the most genuinely useful
thing a reader's guide can hand over.

**15. A fourth sort: by author.** (M)
The machinery is there — three `--o-*` custom properties and a class on
`<html>`. A fourth would put Paul's thirteen together, Moses' five, John's
five, Luke's two. It reframes the library as a shelf of people rather than a
chronology, and it costs one more `order` value per section.

**16. Filter / jump box.** (M)
66 chips across five divisions is past the point where scanning beats typing.
A `/` key that focuses a filter over the chip strip, with Enter jumping.

**17. The contested-date overlay.** (L)
The end-note is honest about the traditional chronology being one defensible
reconstruction, and names the four places it is contested. The spine could
*show* it: a toggle that draws ghost bars at the critical-scholarship
positions — Daniel sliding four hundred years, Isaiah splitting into two, the
Pentateuch moving to the monarchy. It would be the most intellectually
interesting thing on the page and it makes the disclaimer visible rather than
footnoted. Opt-in, off by default, keeping the traditional dating as the
site's own position.

**18. Sharing metadata.** (S)
No description, no Open Graph tags, no favicon. A link to this page currently
previews as bare text. One block in the head.

---

## Deliberately not proposed

- **Splitting the single file.** The one-file build is a feature: it opens from
  disk, survives being emailed, and has no toolchain. 489KB is not a problem.
- **A framework.** Nothing here would be shorter in one.
- **More sort modes beyond author.** Three was already generous; five would be
  a menu no one reads.
