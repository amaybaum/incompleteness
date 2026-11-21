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
