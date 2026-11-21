# Amendment A1 to PREREG: prose comparison lines, and the lexical additions D1 and D2

**Status.** Append-only amendment to `../PREREG.md`, which stays unchanged as frozen at `43eff402`
(with the D6 wording change recorded in RESULT). This amendment is pushed before the snapshot is
re-extracted. It widens the inventory and removes nothing from it.

**Authorization.** Owner `amaybaum`, #1169 comment 7057674976, 2026-11-21T05:05:42Z:
"Add the 802 prose comparison lines to #1471 | Approved"; "Accept the baseline additions D1 and D2 |
Approved, as coverage additions. Record them as departures and preserve the frozen original. The
reviewer verifies them."; "**Baseline (#1471).** It stays pinned to `1c7eedc4` and takes in no Step 2
change. This approval covers completing the before-baseline only. It does not cover running the
before/after regression or accepting its conclusions."

**Goal link (§A.47).** Unchanged from PREREG: the A1-exit objective (#1169) through #1468. The
amendment widens the "before" state that the later comparison reads; it decides nothing.

**Pin.** Unchanged: `1c7eedc402eafd2bac654484fa790874a33f444d`. Every source is still read from the Git
objects at the pin.

## Departures from PREREG

All three add entries to the inventory of PREREG §2. None changes or removes an entry selected under
PREREG.

### P1. Prose comparison lines (new category C-PROSE)

An entry is added, with category `C-PROSE`, for every line of every corpus file (PREREG §1) that
satisfies all three conditions:
1. the line does not begin with `|`;
2. it matches, case-insensitively,
   `(\\pm|±|\\sigma|σ|\bPDG\b|CODATA|observed|measured|measurement|experimental)`;
3. it matches `(?<![\w.])\d+\.\d+` (a decimal number not preceded by a word character or a dot).

The regexes are Python `re` syntax as written in the extractor, in a raw string. This is the rule that
gave the count of 890 lines, of which 802 were not entries at `c2001d82` (RESULT §4). A line that is
already an entry gains the category. A line selected only by C-PROSE gets no mirror search: the rule
reads every corpus file, chapters and FULL alike, so each matching mirror line is selected directly.
Mirror propagation (PREREG §2 and D4) does not carry the C-PROSE category.

### P2 (was D1). Classical-dimension lexical scan

C-CDO also takes every corpus line matching `classical-dimension|N < \\infty|fixed finite carrier`
(the ledger's extended pattern X4 in `ledger_check.py`). Route tag: `lexical-X4`. At the pin this adds
M:650.

### P3 (was D2). Finite-lattice lexical scan

C-FINL also takes every corpus line matching
`[Ee]xtrapolat|[NL] *\\to *\\infty|[NL] *→ *∞|finite-[LN]\b|finite lattice`. Route tag:
`lexical-FINL`. At the pin this adds 30 lines that are not X-47 ledger sites or their mirrors. These
include SM:742 and Structure's large-N lines, Str:226–481. The large-N lines are not lattice-regulator
numerics, but the rule keeps them.

## Added controls

The self-test gains three countercontrols on one prose-comparison line. The line is the first entry
in file-then-line order that lies in `papers/`, has category `C-PROSE` alone, contains a decimal
token and has at least one status term. Each countercontrol must be detected at that entry only:
- **value:** the line's first decimal token gets its last digit changed, and the entry must be
  reported as `value changed`;
- **label:** an added sentence carries a status term, and the entry must be reported as
  `label changed`;
- **removal:** the line is deleted, and the entry must be reported as `removed`.

Every control of PREREG §5 is kept.

## Additions after the round-1 review at `c2001d82` (REVISE, light)

These additions answer the independent review of `c2001d82` recorded on #1471. They are appended
before the snapshot is re-extracted. The pin stays `1c7eedc4`, and PREREG keeps its frozen text.
P1w, P4 and P5 are coverage additions under the owner record quoted above (#1169 c.7057674976). R1
and R2 change the compare mode, which PREREG §4 specifies, and the self-test that §5 specifies. R3
changes the number tokenizer.

### P1w. Prose rule, widened (supersedes the selection clause of P1)

A `C-PROSE` entry is every corpus line that satisfies all three conditions:
1. it does not begin with `|`;
2. it matches, case-insensitively, the marker rule
   `\\pm|±|\\sigma|σ|\bPDG\b|CODATA|observed|measured|measurement|experimental|observation|match|agree|coincid|%|discrepanc|predict`;
3. it matches the number rule
   `(?<![\w.])\d+\.\d+|10\s*\^\s*\{?\s*[-−]?\d+|(?<![\w./])\d+\s*/\s*\d+(?![\w/.])|\\[dt]?frac\s*\{\s*\d+\s*\}\s*\{\s*\d+\s*\}|\d+(?:\.\d+)?\s*\\?%`.
   It takes decimals, powers of ten (`10^{n}`, `\sim 10^n`), exact fractions (`2/3`, `\frac{2}{3}`)
   and percentages.

The extractor holds these as `PROSE_MARK_W` and `PROSE_NUM_W`, and `build` applies them. The P1
rule's 890 lines are a subset of what this rule selects; the snapshot counts them as
`C-PROSE-narrow-rule`. The bare stems `observ` and `measur` are not used, because they select
"observer" and "probability measure" throughout the corpus. The rest of P1 is unchanged: no mirror
search, and no propagation.

### P4. Every site of the ledger's site map

An entry with category `C-SITEMAP` is added for every one of the 697 sites in the ledger's
`sitemap.json`, of every row, FP and FREE included. Its ledger row is recorded where the site map
names one. These entries are added after the mirror closure, because the map lists its own FULL
sites. This captures Step-2 edit targets outside the row-6 input list, for example X-10, X-15, X-26,
X-30, X-50, X-55, X-60 and X-82.

### P5. M:566 in the X-48 family

M:566 (the Remark "why the geometry alone cannot do it") is added to C-CDO with ledger row X-48.

### R1. Compare mode: content pairing and unaccounted lines (replaces PREREG §4's pairing)

- **Pairing.** Lines are paired by content in three stages:
  1. lines inside `difflib` equal blocks of the same file keep their pairing;
  2. an entry outside an equal block takes an unclaimed after-state line with identical text, in the
     same file first (nearest line), then in any file;
  3. the remaining entries take the most similar unclaimed changed line, greedily by
     `SequenceMatcher` ratio: at least 0.6 in the same file, at least 0.8 across files.

  An entry with no partner is `removed`. Entries are reported with their new file and line and a
  `moved` flag.
- **Unaccounted and deleted lines.** Every changed or inserted non-blank after-state line that is
  not the image of an entry is reported as `unaccounted`, in every file including new files. Every
  deleted non-blank pin line that is not an entry and does not reappear is reported as `deleted`.
  Both carry flags: `numbers`, `marker` (the P1w marker rule), `terms` (status, class-mark, scope or
  negation terms), `table`, and `new-file`.
- **Value key.** The value key includes the unit, so a change of unit is `value changed`.
- **Label signature.** The label signature includes negation terms
  (`not|no|never|cannot|can't|none|neither|nor|without|fails?|failed`), so a negation is
  `label changed`.
- **Output and exit status (§A.44).** `--json <path>` writes the report in schema
  `a1exit-regression-compare/1`, with keys `schema`, `pin`, `other`, `any_change`, `summary`,
  `entries`, `unaccounted` and `deleted`. Compare exits 1 when anything changed and 0 when nothing
  did.

### R2. Added self-test countercontrols

Each countercontrol must report exactly the stated outcome: the entry results, the number of
unaccounted lines, the number of deleted lines and `any_change`. The cases are:
- a row swap: both rows are moved and unchanged;
- a row moved together with an edit to the adjacent row: the moved row is unchanged, and the edited
  row is `value changed`;
- a line inserted inside a rewritten paragraph: the paragraph is `text changed`, and one unaccounted
  line is flagged `numbers` and `marker`;
- a unit change from MeV to GeV: `value changed`;
- a negation: `label changed`;
- a new paragraph away from every entry: one unaccounted line, flagged;
- a new file: two unaccounted lines, flagged `new-file`;
- a value change on a line that is not an entry: one unaccounted line and one deleted line, flagged
  `numbers`.

The earlier controls are kept, with their expected unaccounted counts stated.

### R3. Identifier digits

A minus sign directly after a letter is a hyphen inside an identifier, so `X-48`, `G-2` and `spin-0`
give no number token. A range such as `10-20` and a signed value such as `-0.5` are unaffected. A
self-test line checks all of these. Separately, the ids of Bioinformatics and Juno lines use the
abbreviations `Bio` and `Juno`, which changes ids only.

### Note on D6

D6 changed PREREG in place, at `c2001d82`. In §5, the location of the scratch copy became "in a
temporary directory outside the repository". The change was made because the CI added-text scan
flagged the earlier word as a local path. It changes wording only. PREREG has not been edited since, and corrections are recorded
in this amendment.

## Additions after the round-2 review at `ee96218d` (ACCEPT-WITH-NITS)

These answer the round-2 nits recorded on #1471. The pin stays `1c7eedc4`. The entry set and every
entry's text are unchanged. R5 changes number tokens, and the snapshot is regenerated for that reason
alone (§ R5 below).

### R4. Moves across files

An entry whose image lies in a different file is reported as `relocated`, and as
`relocated_from_main` when its source file is `papers/Main.md`, because Main must stay independent of
the downstream papers. The summary counts both. A relocation sets `any_change`, and compare then exits
1. A move within one file is not a change: such an entry is reported `unchanged` with `moved` set.
The text-diff consequences of a within-file move (the removal and insertion it causes) are not
reported, because the line is paired. A self-test countercontrol moves M:780 into
`papers/Substratum.md`. It must report one relocation, flagged from Main, and `any_change`.

### R5. Subtraction digits

R3 makes a minus sign after a letter part of an identifier. The exception is a subtraction, defined as
either of:
- a Unicode minus `−` (U+2212), as in `d−1` or `N−1`;
- an ASCII hyphen inside inline math, meaning an odd number of unescaped `$` before it, as in
  `$2/(d-1)$`.

In a subtraction the digit is kept as an unsigned number token. `X-48`, `G-2` and `spin-0` outside
math still give no token. Countercontrols:
- `d−1` → `d−2` at Juno:238 must be `value changed`;
- a tokenizer line checks `d−1`, `N−1` and `$2/(d-1)$`.

Effect on the snapshot: the same 3105 entries with the same text. 59 entries gain number tokens (55 in
`numbers`, 4 in table `cells`), and the total goes from 11932 to 12042.

### R6. Compare-tree output

With `--compare-tree`, the JSON report records the tree as `tree:<basename>`, never a local path.
Compare reports are working files and are not committed.

## Addition after the round-3 review at `fe25954d` (ACCEPT, one optional nit)

### R7. Display math

R5's math test counted single `$` signs, so a one-line `$$…$$` display formula read as outside math
and its subtraction digits were dropped. An example is GR:480, the a₀ formula (X-72),
`\frac{(d-3)}{(d-2)(d-1)}`. A `$$` pair now opens and closes display math, a single `$` opens and
closes inline math, and a position inside either counts as math.

Effect on the snapshot: the same 3105 entries with the same text. 10 entries gain number tokens, and
the total goes from 12042 to 12057. A countercontrol requires GR:480 `(d-3)` → `(d-4)` to be
`value changed`.
