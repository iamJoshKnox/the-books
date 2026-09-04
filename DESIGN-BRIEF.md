# The Books — design brief

A long-form, single-authored reference site for the books of the Bible, in the
editorial style of `Foster The People/a-night-at-red-rocks.html`: hand-built HTML,
CSS custom-property theming, numbered chapters, custom CSS/SVG diagrams instead of
stock imagery, prose that respects the reader.

## Inherited from the Red Rocks page

- Single-file (or few-file) HTML. No framework, no build step.
- Three type roles: display / heading serif / body sans, set as `--f-display`,
  `--f-head`, `--f-body`.
- Full token palette redefined for light, `prefers-color-scheme: dark`, and
  `[data-theme]` override.
- Masthead with a textured CSS background, a `dl.facts` strip, a horizontal
  numbered TOC, then `section.chapter` blocks with `.ch-num` / `.ch-title` /
  `.sub`.
- Recurring components: `.prose`, `.note` (callout), `figure` + `figcaption`
  with `.cred`, `.table-wrap > table`, `.timeline`, and one bespoke diagram per
  chapter (the stratigraphic column is the model to beat).

## New for this project

### 1. Per-book theming, systematised

66 bespoke themes is chaos. Instead: **9 genre families**, each a complete token
set, with **one accent hue varied per book** inside the family. Section grounds
alternate light/dark down the page for rhythm.

| Family | Palette idea |
|---|---|
| Torah | Carved limestone, desert sand, basalt |
| Historical narrative | Bronze, iron, ochre, olive |
| Wisdom & poetry | Papyrus, indigo ink, gold leaf |
| Major prophets | Ash, ember, smoke |
| Minor prophets | Muted clay, verdigris |
| Gospels | Parchment, illuminated gold + lapis |
| Acts & journeys | Roman travertine, Mediterranean blue |
| Epistles | Wax tablet, oxblood, unbleached wool |
| Apocalyptic (Daniel, Revelation) | Obsidian, gold, blood red |

### 2. Per-book motif diagram

The thing that makes each section feel authored. Pure CSS/SVG, no images:

- Genesis — seven-day creation grid, then a descent through the toledot
- Exodus — tabernacle floor plan
- Leviticus — the altar, concentric holiness zones
- Numbers — census tally marks, two generations
- Deuteronomy — a covenant treaty document layout
- Joshua/Judges — the judges cycle (sin → oppression → cry → deliverer)
- Kings/Chronicles — parallel dynastic rails, north and south
- Psalms — the five-book division as a bar
- Job — a symmetrical speech-cycle diagram (the actual chiasm)
- Isaiah — the 1–39 / 40–66 hinge
- Ezekiel — the wheel
- Daniel — the four-metal statue
- Gospels — tetramorph, plus a synoptic-overlap Venn
- Acts — the three missionary journeys as route lines
- Epistles — a letter-form diagram (opening, thanksgiving, body, greetings)
- Revelation — seven seals / trumpets / bowls as nested rings

### 3. The timeline

Two problems with a naive linear timeline: the primeval material has no
bounded start, and ~90% of the books cluster between 1000 BC and AD 100.

**Solution — a banded, non-linear spine.** Eras as proportioned bands, with
linear scaling inside the historical era and a compressed symbolic segment for
primeval history:

`Creation · Patriarchs · Egypt & Exodus · Conquest & Judges · United Monarchy ·
Divided Kingdom · Exile · Return & Second Temple · Life of Jesus · Apostolic Age`

**Each book plots two marks:**
- a **bar** for the span of events it narrates
- a **dot** for when it was written (with an uncertainty whisker)

Special cases to design for: Job (setting patriarchal, composition much later),
Psalms (a span, not a point), the epistles (near-points), Revelation (a bar
that runs off the right edge — design the "beyond the end" treatment).

Each chapter header carries a **mini locator**: the full spine, shrunk, with
this book's bar lit. Plus a sticky global rail available from anywhere.

### 4. Required per-book content

- One-paragraph description of the events of the book
- Wikipedia link
- BibleProject YouTube overview, embedded

## Decisions (locked 2026-09-03)

1. **Canon** - 66-book Protestant, Genesis to Revelation. Matches BibleProject
   overview coverage almost exactly.
2. **Dating** - traditional / conservative throughout. Mosaic authorship of the
   Pentateuch, 8th-century Isaiah, 6th-century Daniel. One composition dot per
   book, no competing bars. Say so plainly in the sources chapter rather than
   letting the reader assume it is uncontested.
3. **Architecture** - one single page. Truest to the Red Rocks file, and the
   timeline-as-you-scroll effect is the reason to do it that way. Budget the
   weight accordingly (see performance note).
4. **Order** - canonical by default, with a chronological toggle.

### Implementing the order toggle — as built

`main` is a flex column and every `section.chapter` carries three order values
as inline custom properties (`--o-canon`, `--o-events`, `--o-written`).
Switching modes sets one `data-order` attribute on `<html>`; sections and the
TOC chips re-sort together with no DOM manipulation, no reload, and no loss of
an already-loaded video iframe.

Two corrections to the earlier plan:

- **The toggle is three-way, not two.** "By events" sorts on the start of the
  stretch a book narrates; "By date written" sorts on composition. They are
  genuinely different questions and the timeline data answers both. In the
  five-book slice only the written mode reorders anything (Jonah moves ahead of
  Psalms — written c. 760 BC against a Psalter not compiled until c. 430); the
  events mode will start to differ once the histories and the epistles land.
- **CSS counters cannot renumber the chapters.** Counters increment in DOM
  order, not flex-visual order, so a counter would number the sections wrongly
  the moment the order changed. The slice instead prints each book's fixed
  canonical number (01, 19, 32, 59, 66), which is the book's identity rather
  than its position and stays correct in all three modes. It also makes it
  obvious at a glance which books are missing.

## Status

**35 of 66 books built** — the Pentateuch, the twelve historical books, the five
wisdom books, the five major prophets, the four Gospels and Acts, plus Jonah,
James and Revelation. Three of five divisions complete; Writings and Prophets
stands at 11 of 22.

**All nine palettes are now in use.**

Remaining: the eleven minor prophets, and the twenty letters.

### Daniel: the first book whose division and family disagree

Every book so far has sat in a division whose palette matched its genre. Daniel
does not: it is shelved in Writings and Prophets but coloured as an apocalypse,
alongside Revelation, because that is the company it actually keeps. The
separation of the two systems — divisions structure the page, families colour
individual books — was designed on the assumption this case would eventually
arrive, and it holds up: Daniel reads as obsidian and gold in the middle of a
run of ember-coloured prophets, and nothing about the division structure
complains. Its note says so outright rather than leaving the reader to wonder.

### Lamentations resolved itself

Jeremiah, Lamentations and Ezekiel all cluster on 586 BC, and I expected either
the lane split or a new mechanism. Neither was needed: the spans are close but
not identical, so narrowest-on-top handles it — Lamentations, an 8px sliver
inside Jeremiah's 20px bar, sits on top and wins its own hover. The rule written
for Ruth inside Judges covered the prophets without modification.

### The era band floats

Expanding a division pushes the era strip out of view, and without it the rows
are unreadable — a bar at 45% means nothing unless you can see that 45% is the
Divided Kingdom. The strip and its colour band are now a page-level sticky
header that rides at the top for as long as the spine is on screen, handing off
to the main `.topbar` when the section ends.

Two things this needed:

- **The band had to be lifted out of `.spine-scroll`.** `position: sticky`
  resolves against the nearest scrolling ancestor, and that container is one —
  `overflow-x: auto` forces `overflow-y` to `auto` as well, so a sticky element
  inside it has no vertical range to travel in. The band now sits in its own
  wrapper outside the rows, with the two horizontal scroll positions synced in
  JS so they stay aligned on narrow screens.
- **Watch the class names.** The first pass called the wrapper `.spine-head`,
  which was already the class on the section's introductory heading and
  paragraph — so the intro went sticky too and overlapped the rows. It is
  `.spine-float` now.

### Job is what the chart was built for

Job is placed by setting, not composition: nobody in it is an Israelite, wealth
is counted in livestock, and Job sacrifices himself with no priesthood in sight,
all of which reads as patriarchal. When it was written is genuinely unknown —
estimates span a thousand years. So its bar sits in the Patriarchs band and its
dot sits four eras to the right, and the distance between them is the most
visible thing in its row.

It also finally makes the "by events" sort earn its place: Job is the eighteenth
book on the shelf and the **second** book by narrated events, ahead of Exodus.
That mode has existed since the five-book slice and until now had barely
reordered anything.

### Chronicles needed no new machinery

The retelling problem I had deferred since the Gospels turned out to be already
solved. 1 Chronicles narrates exactly the years 2 Samuel does, so the lane split
built for Matthew and Luke caught it automatically — the two share a stripe, top
and bottom half, and each tooltip now names the other: *"same years as
1 Chronicles"*. 2 Chronicles overlaps 1-2 Kings without matching it, so
narrowest-on-top resolves it with no special case at all. Two rules, written for
a different division, covering the case they were not designed for.

1 Chronicles also becomes the second book to run off the left edge of the chart,
after John: its nine chapters of genealogy reach back to Adam, so it gets the
same faded prologue bar.

### Two fixes folded in

- **The dot no longer hides the bar.** A 12px composition dot covers an 8px bar,
  so on point-in-time books — Leviticus, Deuteronomy, James, Revelation — the dot
  won the hover and the span of events was unreachable. Where the dot falls
  inside the bar, its tooltip now carries both facts.
- **Each book has its own accent** within its family. The first attempt blended
  each book further toward its family's *secondary* colour, which works where
  the two are neighbours and fails where they are near-complementary: the
  Gospels run lapis to gold, and 40% along that axis is grey. John came out
  `#9C9DA4`. The variation now stays on the family's own hue and moves only in
  hue (a few degrees) and lightness, so no blend can go muddy — Torah reads as
  five bronzes, the Gospels as four lapis blues.

## Scaling to 66 books

Three changes, made once 21 books had already made the spine unwieldy.

### The spine collapses to five density rows

By default each division is a single row: the chevron and division name sit in
the left column, in the division's own colour, and that division's combined
timeline sits on the same row, aligned to the same name column as the book rows
beneath. Every book's bar is stacked translucently in that one track, so where
books overlap the row simply gets darker — which turns the apostolic pile-up
from a problem into the information. Clicking a division expands it into
individual rows with composition dots; the combined row stays as the header and
dims. Dots are omitted when collapsed: twenty-two in one track is noise.

**Bars are emitted widest first.** The narrowest paints last, so it ends up on
top — which also means it wins the hover and its tooltip is the one you get.
Without that, Ruth (five years) is unreachable underneath Judges (three
centuries). Verified by hit-testing every pixel across a division row: 394 of
396 match the rule, and the two exceptions are shared boundary pixels where two
bars touch edge to edge.

**Every bar is a link.** Both the combined division rows and the individual book
rows: hovering names the book and the years it narrates, clicking navigates to
it. One delegated tooltip element rather than per-bar markup.

**Every date in a tooltip carries `c.`**, because every date on this site is a
traditional reckoning and approximate — matching the locator captions. One `c.`
governs a whole range, and the era suffix repeats only when a range crosses BC
into AD: `c. 1876 – 1445 BC`, `c. AD 30 – 62`, `c. 5 BC – AD 30`. Two cases take
no hedge: creation, which is not a date, and Revelation, whose bar deliberately
runs off the chart — its span reads `c. AD 95 onward` rather than inventing an
upper bound out of where the chart happens to stop. Where a bar and its dot sit far apart — 1 Kings narrates 970–853 BC but was
written from exile around 560 — one row yields two tooltips and two routes into
the same book, which makes the gap between happening and recording legible by
hovering.

**The locator inside each chapter is tipped as well** — bar and dot both, though
neither links, since you are already on that book. It also prints the book's own
name at the start of its row, set like the era labels directly above it. The
name is suppressed where the bar reaches the left edge and would sit underneath
it, which in practice means Genesis alone: its events begin at creation.

(An earlier note here argued the locators should stay plain, on the grounds that
naming the book you are already reading is redundant. That was wrong in use: the
tooltip carries the dates, and the row label tells you which line is the book's
own when the era band sits right above it.)

*Watch the delegation selector.* It was first written as
`.density .bar[data-tip]`, which silently scoped tooltips to the collapsed
division rows only — the book rows carried correct `data-tip` attributes that
never fired. It is now a bare `[data-tip]`.

**Coincident books split the track height into lanes.** Width cannot separate
books covering exactly the same years, so height does: Matthew and Luke both run
5 BC-AD 30 and become the top and bottom halves of one stripe, with a hairline
between them so the doubling is visible. The two rules compose - on the sliver
where all four gospels overlap, narrowest-on-top surfaces Mark and John, and the
lane split then separates those two. Verified by hit-testing: top half Matthew,
bottom half Luke on the wide stretch; top half Mark, bottom half John on the
narrow one.

### The header is a running title

Whichever book you are reading, the header names it: the division button marked
current, its chip row open beneath, and that book's chip highlighted. It is
driven by scroll position, not by clicks, so it is right however you arrived —
a chip, a timeline bar, a composition dot, a pasted URL, or plain scrolling.
The section under the header is found by testing which one's box contains a line
just below it, using visual rects rather than DOM order, so it stays correct in
the two sorted modes where those differ.

This replaced the manual expand/collapse on the division buttons. Two sources of
truth for "which chip row is open" was one too many; the buttons still navigate
by href, which lands you in the division and lets the spy open the row.

Two bugs fixed on the way, both worth remembering:

- **Anchor navigation was landing in the wrong place on a cold load.**
  Off-screen chapters are content-visibility placeholders sized by
  `contain-intrinsic-size`, so the browser's jump to `#james` is computed
  against estimates that are wildly wrong before anything has been measured —
  it stayed on Genesis. `alignToHash` now nudges repeatedly until the target
  sits at the intended offset; each correction resolves more real heights, and
  it converges in two passes. Called at DOM-ready, on load, and on hashchange.
- **The spy was throttled through `requestAnimationFrame`.** rAF does not fire
  in a background tab, so the header silently went stale. It is a read-only
  pass over about forty rects — cheap enough to run straight off the scroll
  event.

### The header carries divisions, not books

A chip row 66 wide is unusable, so the floating header now holds a link back to
the spine plus five division links with built counts. Opening a division reveals
its own book chips and scrolls to it. The order controls and the division nav
sit in one `.topbar` wrapper so they stick together - about 107px closed, 153px
with chips open.

### Off-screen sections are skipped, not unloaded

`content-visibility: auto` with `contain-intrinsic-size` on every chapter.
Deliberately **not** virtualisation: every section stays in the DOM, so anchor
links, find-in-page, the three sort orders and ordinary scrolling all behave
exactly as before. Scrolling down to a book still feels like scrolling down to a
book - nothing paginates, nothing swaps in. Virtualising would have broken the
order toggle outright, since it works by re-sorting sections that all exist.

Three bugs this round, each worth remembering:

- **`scrollIntoView` misses through `content-visibility`.** Off-screen sections
  are size estimates, so a scripted scroll lands at the wrong offset. Native
  anchor navigation resolves correctly against those placeholders, so the
  division links are `<a href="#part-N">` and JavaScript only intervenes in the
  sorted modes, where the prefaces are hidden. Verified: every anchor lands at
  exactly the intended 150px offset.
- **A `display` declaration beats the `hidden` attribute.** `.bn-books` was
  `display: flex`, so all five chip rows showed at once. Needs an explicit
  `[hidden] { display: none }`.
- **Sticky does not inherit.** Making `.controls` sticky left the nav below it
  scrolling away; both needed a shared sticky wrapper.

## The five divisions

The page is structured by the five canonical divisions, which are **orthogonal
to the nine genre families**: families colour individual books, divisions
structure the page.

| Part | Division | Built |
|---|---|---|
| I | The Pentateuch | 5 of 5 |
| II | The Historical Books | 0 of 12 |
| III | Writings and Prophets | 2 of 22 |
| IV | The Gospels | 4 of 4 |
| V | Acts, Letters and Revelation | 3 of 23 |

Each division opens with a **full-bleed colour preface** — part number, title, a
sentence or two, the book list, and a built count — separated from what precedes
it by a bright rule in the division's own colour. The same five groups are
bracketed on the spine with matching colours and the same counts.

Three things this settled:

- **It replaced a one-off.** The spine previously braced the four Gospels under
  "four accounts of the same three years", which annotated one group's quirk
  rather than giving the whole library a structure. Divisions cover all 66.
- **Prefaces are hidden outside canonical order.** In the by-events and
  by-written modes the books interleave across divisions, so a preface would be
  describing a group that is no longer contiguous. `display: none` on the two
  sorted modes; the sort still works, it just loses the chapter headings.
- **The gaps became visible.** An empty division still gets its preface, marked
  `0 of 12 built`, and the spine carries a faint ghost row for Joshua–Esther
  spanning the eras those books cover. A reader can see what is missing and
  where it belongs, which is better than silence in a slice this incomplete.

Order values are now spaced by ten so prefaces can be interleaved between books
without renumbering; keep that spacing as the remaining books land.

## Maps

Six books carry a map in the right-hand column beside the summary paragraph, on
three schematic bases: the Exodus theatre (Egypt, Sinai, Canaan) for Genesis,
Exodus, Numbers and Deuteronomy; the Mediterranean world for Jonah; western Asia
Minor for Revelation. Leviticus, Psalms and James have none on purpose —
Leviticus never leaves one spot, so its map would be a single dot, and the other
two have no geography worth drawing.

They are schematic rather than cartographic, and every caption says so. Drawing
coastlines from memory would look authoritative and be quietly wrong; the
timeline and the tabernacle plan are hedged the same way.

### They are baked images, and why

The first build made each map a live inline SVG themed with the section's own
`--k-*` tokens. Six of those made scrolling choppy — confirmed by the user in a
real window, not by instrumentation. Bisecting never isolated a culprit:
swapping `color-mix()` fills for solid tokens, moving all sixty-odd labels out of
SVG `<text>` into positioned HTML, adding `content-visibility: auto`, and hiding
the filled and stroked elements in turn each failed to help, while removing the
figures outright fixed it instantly.

So the fix stopped chasing the mechanism and removed the whole class of problem:
each map is now a single `<img>` holding a data-URI SVG, decoded once and
scrolled as a bitmap. The cost is per-family theming — an `<img>` cannot read the
page's custom properties — so each map carries its own parchment ground and
reads as an inset plate in either theme, the way a photograph would. That is
arguably the better call anyway: it matches how the Red Rocks page treats its
photographs.

### Settled

Confirmed good in real use at ten maps, scrolling in an ordinary window. The
baked-image approach stands; treat this as closed rather than as a performance
question still being watched.

### A caution about measuring this

Every timing figure gathered through the browser-automation harness in that
session was worthless, and it took far too long to notice. The automated tab
reported `document.visibilityState === "hidden"`, which throttles
`requestAnimationFrame` to nothing and stops the compositor producing frames, so
the rAF timing loops never completed and screenshot timeouts could not be read as
jank. The only sound signal was a human scrolling the file in an ordinary
window. Check `visibilityState` before trusting any rendering measurement taken
this way.

## Performance note

66 YouTube iframes will not load. Use click-to-load facades (poster + play
button, iframe injected on click). If this is ever published as a Claude
Artifact, remember external images are CSP-blocked — draw the facade in CSS
rather than pulling `i.ytimg.com` thumbnails.

## The running title, and why it kept pointing at the wrong book

The floating header names the division and book you are currently reading, so it
doubles as a title page while you read. Two faults had to be fixed before it
behaved.

### Flashing chips during a jump

Clicking a chip forty books away scrolls through every book in between, and the
spy ran the whole way down, turning the chip strip into a flickbook. The header
now freezes while a jump is in flight: `beginNav()` on any in-page click or
`hashchange` sets a flag, and a 150 ms quiet timer releases it once the scrolling
has actually stopped. Measured across a Genesis-to-Revelation jump: one chip
state change, `NONE -> 66Revelation`, with nothing in between.

### Off by one book

Landing on `#lamentations` lit the *Jeremiah* chip. The detection line was drawn
at the header's bottom edge, but an anchored section comes to rest with its top
at `scroll-margin-top` — a few pixels *below* that line — so the previous book,
whose bottom padding was still on screen, won by a hair. One constant,
`ANCHOR_TOP = 165`, is now shared by the aligner (`want = ANCHOR_TOP`) and the
spy (`line = ANCHOR_TOP + 20`), which puts the test in the blank space above the
incoming book's title, exactly as asked.

That alone was not enough. `runningTitle()` short-circuits when its answer has
not changed, which is right during ordinary scrolling and wrong at the end of a
jump: the final pass could run a frame before `alignToHash` had finished
settling, and then nothing scrolled again to correct it. `refreshTitle()` clears
the cached key and re-reads; the settle timer and `alignToHash`'s convergence
both call it, with one more pass 200 ms later for any late reflow. Verified on
ten anchors spread across all five divisions — Genesis, Deuteronomy, Esther, Job,
Song of Songs, Lamentations, Malachi, Matthew, Acts, Revelation — all landing at
`top 165` with the right chip and the right division.

### A second measurement trap

While verifying this, the chip appeared stale during ordinary scrolling:
geometry said Numbers, the chip said Genesis. It was neither. Sections carry
`content-visibility: auto`, so scrolling resolves real heights for placeholders
that had only estimates, and the document grows underneath you — between two
probes in separate tool calls the page had moved 5,000 px. Read the chip and the
geometry in the *same* evaluation, or the comparison is meaningless.

## The letters, and the crowding problem they created

The last twenty books are Romans through Jude, and they all happen at once. On
the traditional dating seventeen of them are written between AD 48 and AD 68 —
a twenty-year window inside a band that also has to hold Acts, the Johannine
letters and Revelation. At the old proportions that window was 5.2% of the
spine, which is not enough room for seventeen clickable bars.

Two changes fixed it, both in `ERAS`:

* **Apostolic 18% → 20%**, taking the two points from Life of Jesus (14 → 12).
  Both are New Testament bands, and twelve points is still generous for a
  thirty-five year span carrying four books.
* **A knee at `(70, 0.78)`**, the same mechanism Return & Second Temple already
  uses. AD 70 now sits at 78% of the band, which spreads AD 30–70 across most of
  it and squeezes the last thirty years, where only the Johannine writings
  remain. The letter window went from 5.2% to 7.8% of the spine.

Nothing else had to change: `build_spine.py` recomputed all sixty-six books, the
five division counts and the whole header nav from the new table.

### Lane splitting earned its keep

The mechanism written for Matthew and Luke turned out to encode real
relationships once the letters arrived. Books sharing an identical span split
the track's height between them, and four new pairs fell out of the dates:

| pair | why they share a span |
| --- | --- |
| Colossians / Philemon | same town, same delivery, carried by Tychicus and Onesimus |
| 1 Timothy / Titus | the same instructions to two colleagues in the same year |
| 2 Peter / Jude | share most of a chapter of material as well as a decade |
| 2 John / 3 John | one sheet of papyrus each, written together |

None of that was designed in. It fell out of dating the books honestly and
letting the existing rule run.

### Per-book accents are now generated

`_accents.py` replaces what had been a hand-maintained block. It reads each
family's `--k-accent` out of the stylesheet and fans that family's books across
fourteen degrees of hue and eleven points of lightness, centred on the base, in
canonical order. It reproduces the previous hand-written values exactly, which
is how the rule was recovered in the first place.

It matters here because the epistles family went from one book to twenty-one
overnight. Three families — wisdom, the major prophets and apocalyptic — are
dark in both themes and declare no themed override, so the generator falls back
to their single base for all three theme blocks.

The first version of it guessed where the generated run ended by matching
accent-shaped lines. That lookahead stopped on the *second line of its own
comment*, so the second run appended a duplicate block rather than replacing
one. It now writes an explicit end sentinel and replaces between markers, and
running it twice is verified to be a no-op.

### Verification

* All twenty-one video ids — Romans has two parts — were scraped from YouTube
  search results rather than recalled, then confirmed through oEmbed to be
  BibleProject uploads with the expected titles. Guessing an eleven-character id
  from memory is a coin flip, and a wrong one renders a dead player.
* All sixty-three distinct Wikipedia targets were resolved through the MediaWiki
  API in one round trip: no redirects, no missing pages.
* Structure: 66 chapters, no duplicate ids, 5/12/22/4/23 per division, 66 spine
  rows, every section carrying a video, no unfilled locator tracks.
* Anchor accuracy re-checked on the new books — Romans, Galatians, Philemon,
  Hebrews, 3 John, Jude — all landing at `top 165` with the right chip lit.

### One consequence worth knowing about

The chip strip for a 23-book division wraps to three rows, which makes the
floating header about 220px tall. The clearance between the header's bottom edge
and an anchored book's title drops to 29px there, against 96px for a
single-row division. It does not overlap, but it is the tightest the layout gets.
