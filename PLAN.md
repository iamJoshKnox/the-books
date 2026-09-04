# The Books — plan

Written 3 Sep 2026. The audience is a small group who will get a link. So
the order is: make the thing safe to change, make it survive a phone, then
add what makes it worth sending, then polish. Items reference BACKLOG.md.

Five phases. Each is one sitting, and each ends with something a person
could look at. Nothing in a later phase should start before the earlier
phase's acceptance line is met — the point of the order is that every phase
after the first is *regenerating* the page, and regenerating a page you
cannot diff or verify is how the accent block got duplicated.

---

## Phase 0 — a link that exists, and a build you can trust

**Why first.** "Send the link" needs a link. And every phase after this one
rebuilds the HTML from scripts; without history and a verifier, each rebuild
is a bet.

| # | Task | Backlog | Done when | |
|---|------|---------|-----------|---|
| 0.1 | `git init`, `.gitignore` for `__pycache__`, first commit of everything as it stands | 9 | `git log` shows one commit; `git status` clean | ✅ |
| 0.2 | Push to a GitHub repo and turn on Pages from `main` (or Netlify drop, if you'd rather not have a repo be public) | — | A URL you can open on your phone | ⬜ needs you |
| 0.3 | Fold the ad-hoc audits into `verify.py`: 66 chapters, no duplicate ids, five division counts, no unfilled locator tracks, no `46 of 66`, every `data-yt` present, every section has a Wikipedia link, no horizontal overflow markers | 11 | `python verify.py` prints PASS and exits 0; a deliberately broken copy fails | ✅ |
| 0.4 | `verify.py --net`: oEmbed every video id, MediaWiki-resolve every Wikipedia slug, fail on a redirect or a 404 | 11 | Runs clean once; then leave it for the month-later check | ✅ |
| 0.5 | One `books.py` holding the 66-row table; `build_spine.py` imports it; delete `_letters_a/b/c.py` and `_lettertpl.py` (their output is in the HTML and in git now) | 10 | `build_spine.py` produces a byte-identical page from `books.py`; the folder has no one-shot scripts | ✅ |
| 0.6 | Fix 4a: `alignToHash` waits for the settle timer, then corrects with `behavior: "instant"`. Keep the smooth travel from native anchor navigation | 4a | You click ten chips on a real machine and every one lands with the right chip lit and no visible hop | ✅ in a throttled tab; your eyes on a real one still wanted |

**Acceptance:** a public URL, a green `verify.py`, one source of truth, and
a git history. About two hours.

---

## Phase 1 — it works on the phone in their pocket

**Why now.** A small group opening a link will open it on a phone first.
Item 3 (viewport meta) is done, which means the thirteen breakpoints now
fire — and no one has ever seen the result. This phase is mostly *looking*,
then fixing what is broken, not redesigning.

| # | Task | Backlog | Done when |
|---|------|---------|-----------|
| 1.1 | Open the Pages URL on an actual phone. Walk Genesis → Revelation. Screenshot every breakage. Fix layout breakages only — no new features | 8 | A list of what broke, and it is fixed | ⬜ first pass reported: the floating header; fixed below. Keep walking |
| 1.2 | ~~Chip strip on narrow screens: horizontal scroll~~ **Done differently, and further:** below 720px the whole floating stack collapses to one 44px bar reading *division › book*, coloured by division, that drops the order controls, division row and chip row down on tap — each a single scrolling line with the current item scrolled into view — overlaying the page. Tap a chip, a link, outside, or Escape to close. The per-book locator now fits the width with only the book's own era labelled; the orphan fifth spec cell spans its row | 8 | On a 390px screen the header is ≤ 110px tall in every division | ✅ 44px collapsed, 189px open, in every division |
| 1.3 | Tooltips on touch: switch the three mouse listeners to pointer events; on `pointerType === "touch"`, first tap shows the tooltip, second tap follows the link; for lane-split pairs, taps cycle top → bottom → navigate | 5 | You can discover Philemon behind Colossians on a phone |
| 1.4 | Tooltips on focus: `focusin` / `focusout` mirror `mouseover` / `mouseout` | 6 | Tab to a bar, the tooltip appears |
| 1.5 | Roving tabindex on the spine: one tab stop enters it, arrow keys move between bars, Escape leaves | 7 | Tab from the masthead reaches the first paragraph in under ten presses |

**Acceptance:** you hand your own phone to someone and they find a book
without help. One long sitting, or two.

---

## Phase 2 — what makes it worth sending

**Why third.** Once it is safe and it works, the reason to send it is the
content. These are ordered by value per hour.

| # | Task | Backlog | Done when |
|---|------|---------|-----------|
| 2.1 | Sharing metadata: `<meta name="description">`, Open Graph title / description / image (a cropped screenshot of the spine, baked as a data URI or committed PNG), favicon | 18 | Pasting the link into a chat shows a card with the spine on it |
| 2.2 | **One "Paul's world" map** — Aegean and eastern Mediterranean, same baked-SVG pipeline as the ten existing maps — reused across all thirteen Pauline letters with the destination city lit per letter via a CSS variable | 13 | Thirteen more books have a map, from one drawing |
| 2.3 | "Reads with" line under each spec block, from a `PAIRS` table in `books.py`: Kings ↔ Chronicles, Luke ↔ Acts, Jeremiah ↔ Lamentations, Ezra ↔ Nehemiah ↔ Haggai ↔ Zechariah, Colossians ↔ Philemon, 1 Timothy ↔ Titus, 2 Peter ↔ Jude, 1–3 John | 14 | Every pair links both ways; `verify.py` checks symmetry |
| 2.4 | Divided-kingdom map — serves Kings, Chronicles, Hosea, Amos, Micah and most of the minor prophets | 13 | ~14 more books mapped |
| 2.5 | Empires map (Assyria → Babylon → Persia) for Isaiah, Jeremiah, Ezekiel, Daniel, Esther, Nehemiah; Galilee and Judea for the four gospels | 13 | Under ten books left unmapped; decide whether those need one at all |

**Acceptance:** the link previews well, and a first-time reader has a map on
most pages. Three sittings; 2.1–2.3 are the first one.

---

## Phase 3 — the features that reward a second visit

| # | Task | Backlog | Done when |
|---|------|---------|-----------|
| 3.1 | Fourth sort, by author: one more `--o-author` per section from `books.py`; Paul's thirteen, Moses' five, John's five, Luke's two, Solomon's three, then the rest canonical | 15 | The topbar has four buttons and the caption explains the fourth |
| 3.2 | `/` opens a filter over the chip strip; typing narrows; Enter jumps to the first match | 16 | You can reach Habakkuk in four keystrokes |
| 3.3 | Contested-date overlay: a toggle that draws ghost bars at the critical-scholarship positions (Pentateuch → monarchy and later; Isaiah split; Daniel → 160s BC; the Pastorals → early second century). Data as a second date column in `books.py`, off by default | 17 | The footnote at the end becomes something you can *see* |

**Acceptance:** each feature is independent; do them in any order, or skip
3.3 if it feels like it changes what the site is claiming.

---

## Phase 4 — polish that only matters once people are using it

| # | Task | Backlog | Done when |
|---|------|---------|-----------|
| 4.1 | Bake real `contain-intrinsic-size` per section, measured once with sections forced visible and emitted by `build_spine.py` | 12 | Document height does not change as you scroll; anchors land first try on a cold load |
| 4.2 | Run `verify.py --net` monthly, or on push via a GitHub Action | 11 | A dead video or moved Wikipedia page emails you instead of a reader finding it |
| 4.3 | Print stylesheet pass: hide the floating header and spine, one book per page, show link URLs | — | Print to PDF gives something usable |

---

## Deliberately deferred

- **Splitting the single file** — still a feature.
- **Dark-mode screenshots for OG** — light is fine for a preview card.
- **Any redesign of the spine's proportions** — they were tuned by hand
  across sixty-six books and they are right; leave them.

## The rule for every phase

`git commit` before, `python verify.py` after, and look at it in a browser
before moving on. The one time none of those happened is the one time the
generator wrote 200 duplicate lines.
