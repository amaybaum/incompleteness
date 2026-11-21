# A1-EXIT regression audit (#1468): read-only "before" baseline — result

**This is a baseline only. It contains no comparison with any Step-2 head and no verdict.** It records
the state of every inventoried prediction, empirical comparison and A1-exit site at the pin, so that
the later before/after comparison can be run mechanically. Whether removing A1 weakened, strengthened
or changed any physical prediction is not assessed here.

**Status.** Writer's paper-only record, WIP / UNVERIFIED. Independent review on #1471: round 1 at
`c2001d82` returned REVISE (light), round 2 at `ee96218d` returned ACCEPT-WITH-NITS, and round 3 at
`fe25954d` returned ACCEPT with one optional nit. All three are answered through amendment A1. No
manuscript, Lean, registry or ledger file is edited.

**Authorization.**
- Owner `amaybaum`, #1169 comment 7056875845, 2026-11-21T03:51:25Z: "#1468 read-only regression
  baseline | **authorized**".
- Owner `amaybaum`, #1169 comment 7057674976, 2026-11-21T05:05:42Z: "Add the 802 prose comparison lines
  to #1471 | Approved"; "Accept the baseline additions D1 and D2 | Approved, as coverage additions";
  "It stays pinned to `1c7eedc4` and takes in no Step 2 change. This approval covers completing the
  before-baseline only."

The before/after comparison and the audit's verdict are not authorized.

**Goal link (§A.47).** The A1-exit objective (#1169), through #1468: "Decides whether removing A1 has
weakened, strengthened or changed any physical prediction without explicit justification." This record
decides nothing for it. It fixes the "before" state.

**Pin.** `main` at `1c7eedc402eafd2bac654484fa790874a33f444d`. At drafting, both
`git log 1c7eedc4..origin/main -- papers book` and `git log e837e3db..1c7eedc4 -- papers book` were
empty, so the A1-EXIT ledger's site lines (pinned at `e837e3db`) are the lines at this pin. Every source
is read from the Git objects at the pin. The corpus digest is the SHA-256 the extractor computes over
the 42 `papers/*.md` and `book/*.md` files at the pin:
`6565dbcb26d5c2fd919e5c46def33c4eaa2baea40ebd34cdf04e381e75add41f`.

## 1. Files

| File | Content |
|---|---|
| `PREREG.md` | The inventory rule, entry schema, compare semantics and controls, pushed before extraction (`43eff402`). Frozen except for the D6 wording change |
| `amendments/A1-prose-and-lexical.md` | Owner-approved coverage additions P1/P1w, P2 (D1), P3 (D2), P4 and P5, and the review changes R1–R7. R1–R3 were pushed before the re-extraction that uses them (`8c43c6cf`,
`6f7da1f1`). R4–R6, and then R7, each landed in the same commit as its regenerated snapshot |
| `baseline.py` | The extractor: `build`, `check`, `self-test`, `--compare <commit>`, `--compare-tree <dir>`, `--json <path>`. Standard library only; reads Git objects at the pin |
| `snapshot.json` | The baseline: one compact JSON line per entry, plus the pin, corpus digest, ledger blob ids and counts (3.8 MB) |

## 2. Recipe and expected result (§A.42 item 1)

Run from a clone that contains the pin and this record's commit: the head of PR #1471 at landing, or
`main` after it lands.

```
python3 -I -B verification/audits/foundations/a1exit-regression-20261121/baseline.py check
python3 -I -B verification/audits/foundations/a1exit-regression-20261121/baseline.py self-test
python3 -I -B verification/audits/foundations/a1exit-regression-20261121/baseline.py --compare 1c7eedc402eafd2bac654484fa790874a33f444d
```

Expected:
- `check PASS: snapshot.json regenerates byte for byte from 1c7eedc402eafd2bac654484fa790874a33f444d
  (sha256 2db7832d7cb95b0ba77b42afad965696390d4ad67a6835b2c45f045bd04f88c8)`;
- `self-test PASS`, with every line above it `PASS`;
- `summary: {"deleted": 0, "deleted_flagged": 0, "moved": 0, "relocated": 0, "relocated_from_main": 0,
  "unaccounted": 0, "unaccounted_flagged": 0, "unchanged": 3105}; any change: False`, with exit status 0.

Run with Python 3.13. The output depends only on `re`, `difflib` and `json`. Another Python 3 version is
expected to give the same bytes, and `check` detects any difference.

**The later comparison, when it is authorized:** `baseline.py --compare <after-commit> --json <file>`.
- **Entries.** It reports each entry as `unchanged`, `text changed`, `value changed`, `label changed`
  (value and label together when both apply) or `removed`, with its new file and line and a `moved`
  flag.
- **Lines outside the entries.** It also lists every changed or inserted after-state line that is not
  the image of an entry (`unaccounted`), in every file including new ones, and every deleted line that
  is not an entry (`deleted`). Each is flagged for numbers, comparison markers, status/scope/negation
  terms, table rows and new files.
- **Moves.**
  - A move across files is a change. It is reported as `relocated`, and as `relocated_from_main` when
    the source file is `papers/Main.md`. It sets `any_change`.
  - A move within one file is not a change. The entry is reported `unchanged` with `moved` set and its
    new line, and the move alone sets neither `any_change` nor the exit status. Lines inserted or
    deleted around it are still reported as `unaccounted` or `deleted`.
- **Exit status.** It exits 1 when any entry is changed, removed or relocated, or when any line is
  `unaccounted` or `deleted`; otherwise it exits 0.
- **JSON file.** The schema is `a1exit-regression-compare/1`, stated in the extractor's usage text and
  in amendment A1, R1.
  - With `--compare <commit>`, `other` is the commit.
  - With `--compare-tree <dir>`, `other` is `tree:<basename>`, never a local path.
  - Compare reports are working files and are not committed.

The later audit must read every `text changed` entry and every flagged `unaccounted` or `deleted` line.

## 3. Coverage

3105 entries (709 table rows, 2396 prose lines), with 12057 numeric tokens. An entry can carry several
categories.

| Category | Entries | Ledger rows | Selected by |
|---|---|---|---|
| C-TAB, all table rows | 709 in 110 tables (prediction 405, status 109, other 195) | site-map row where the line has one | table detector over the whole corpus |
| C-PROSE, prose comparison lines | 1674 (1436 selected by this clause alone; the earlier narrow rule's 890 lines are a subset) | — | amendment A1, P1w |
| C-SITEMAP, every ledger site-map site | 697 (232 selected by this clause alone) | the site map's row | amendment A1, P4 |
| C-CDO, classical-dimension obstruction | 12 | X-48 | site map; ledger cells; FULL mirror; M:566 (P5); lexical X4 (P2) |
| C-FINL, finite-lattice numerics and extrapolations | 66 (36 ledger sites and mirrors, 30 only from P3) | X-47 | site map; ledger cells; mirrors; lexical (P3) |
| C-CAL, calibration chain | 77 | X-70, X-71, X-72 | site map; ledger home and "also" ranges; mirrors |
| C-OBS, observer selection and global phase | 19 | X-63 | site map; ledger cells (incl. M:764); mirrors |
| C-OPEN, R1 and C1 open items | 6 | X-11, X-71 | site map; ledger cells |
| C-LEDGER, other §6.1 row-6 inputs | 495 | X-00–X-02, X-12, X-20, X-23, X-25, X-40–X-46, X-74 | site map; ledger cells; mirrors |

**Routes.** An entry can take several routes.

| Route | Entries |
|---|---|
| prose-comparison | 1674 |
| table | 709 |
| sitemap-all | 697 |
| sitemap (input rows) | 376 |
| ledger home cell | 327 |
| ledger sites cell | 213 |
| mirror | 288 |
| lexical-FINL | 55 |
| lexical-X4 | 10 |
| explicit M:566 | 1 |

**Mirror search.**
- 288 exact matches.
- 12 fuzzy matches, with ratios 0.92–0.99. Each is a paper line with a near-identical FULL line:
  Cx:474, GR:428, GR:474, GR:480, M:113, M:115, M:131, SM:184, SM:202, SM:280, SM:314, Sub:389.
- 365 with no match at ratio 0.90.

**Named tables.** All are captured as C-TAB rows:
- appendix-a A.4.1–A.4.4 and A.5 (62 rows, including the G-rows at appA:106–113), and their FULL
  mirror at FULL:5517–5643;
- SM §7.6 (SM:1275–1296, 22 rows) and GR §7.4 (GR:544–549, 6 rows);
- the book's status tables ch06 §6.5–6.8, ch07 §7.10, ch08 §8.6–8.7, ch09 §9.2–9.4 and ch19 §19.4, and
  their FULL mirrors;
- the remaining summary tables of the companions:
  - Juno §§1.3, 4.1, 4.2, 5.3, 6.1;
  - SM §§3.2, 4.6, 6.2.1, 6.3, 7.2, 7.3, 7.5, 7.7, A.3;
  - Structure §§6.7, 7.7.4, 12.4, 14.5, 14.10;
  - Main §§3.2, 4.5;
  - Complexity, Computation, Medicine and Bioinformatics.

**Named family sites at the pin.**
- C-CDO: M:358, M:564, M:566, M:568, M:588, M:606, M:650, M:780, Sub:533, Intro:135, and
  ch04:146 = FULL:1250 (exact). The papers' sites have no FULL restatement at ratio 0.90.
- C-OPEN: SM:803, SM:809, SM:811, M:732, M:58 (X-11); GR:58 (X-71, also X-70).
- C-OBS: M:748, M:764, Sub:56, Sub:401, Sub:407, Sub:542, Str:718, Str:734, Comp:212, Meth:283,
  Meth:441, ch02:192 = FULL:822, ch03:58, ch04:36, ch04:178 = FULL:1282, FULL:919, FULL:1140.
- C-FINL and C-CAL: the site lists are in `snapshot.json` (`categories`).
- Examples from the review are now entries:
  - ch18:36 (about 10^17 s) is C-PROSE and C-SITEMAP;
  - SM:1582 (Cabibbo 0.04%, Koide 0.001%) is C-PROSE and C-SITEMAP;
  - FULL:1677 and FULL:1704 are C-PROSE.

**How the corpus was searched (§A.19).**
1. A table detector over every line of every top-level `papers/*.md` and `book/*.md` (110 tables).
2. The ledger's complete site map (`sitemap.json`, 697 sites; its extended scan reports 0 unmapped
   lines at this tree), both per input row and in full (P4).
3. The ledger's own site citations in each input row's home and sites cells, with ranges expanded.
4. A mirror search of every ledger-selected prose line against FULL, and of every FULL line against
   the chapters.
5. Two lexical scans, P2 and P3.
6. The prose comparison rule P1w over every line of the corpus.

## 4. What the rule does not capture automatically, and limits

- **The prose rule is lexical.**
  - It selects a line only when the line carries both one of the markers and one of the number forms.
    A prediction stated without either (for example "the value is three", or a bare integer with no
    marker) is not an entry.
  - It also selects some non-physics lines, such as bibliography entries with "measured" in a title.
  - A change to a line it misses is still reported by compare mode as a flagged `unaccounted` line.
- **The compare mode does not miss changes silently.** Every changed or inserted line in the
  after-state is reported, as an entry result, as `unaccounted` or as `deleted`. How far an
  `unaccounted` or `deleted` line matters is left to the later audit; the flags only sort them.
- **Pairing is greedy.**
  - Lines are paired by identical text first and then by similarity (ratio at least 0.6 in the same
    file, at least 0.8 across files).
  - A heavily rewritten line below the threshold is reported as `removed`, with its replacement as a
    flagged `unaccounted` line.
  - A paragraph split into two pairs with the more similar half; the other half is `unaccounted`.
- **Values and units are parsed heuristically.**
  - Numbers are tokens of the printed text. A unit is recorded only when one of the extractor's unit
    tokens follows, and LaTeX exponents (`^2`) give extra small-integer tokens.
  - The tokens and units are compared as printed, so any change to them is reported. The descriptive
    fields (role, unit) can be wrong without hiding a change.
  - Some row-name columns ("Observable") take the role `observed`.
- **Prose comparison data have no role.** A prose entry records its numbers in order and its text, not
  which number is the prediction and which the datum.
- **Labels** are the status, class-mark, scope and negation vocabularies, plus the text of label-role
  cells. A classification printed in other words is seen only as `text changed`.
- **Finite-lattice table rows outside X-47.** SM:735–740 (the A·B(N) data at N = 20–40) and SM:746–749
  (the A·B(∞) estimators) are C-TAB rows, not X-47 ledger sites.
- **Ledger rows with no line of their own.** X-12, X-23, X-71 and X-74 enter only through the sites
  named in their ledger cells.
- **CI.** No CI job runs `baseline.py check`. Adding one would change the workflow, which is outside
  this unit.

## 5. Controls

All passed at the commit that adds this revision.

| Control | Result |
|---|---|
| `check` (byte-for-byte regeneration from the pin) | PASS |
| Determinism (two builds identical, inside `self-test`) | PASS |
| Identity edit: 0 changed, 0 unaccounted, 0 deleted, `any_change` false | PASS |
| Shift: three lines (two non-blank) inserted above appendix-a; entries moved by 3, unchanged; 2 unaccounted | PASS |
| Changed value: appA:85 `2.361` → `2.362`, reported `value changed` only | PASS |
| Changed label: appA:85 class `L` → `C`, reported `label changed` only | PASS |
| Removed row: appA:72, reported `removed` only | PASS |
| Added row: one unaccounted line flagged `table`, `numbers` | PASS |
| Row swap (appA:72 and appA:73): both moved and unchanged | PASS |
| Move plus adjacent edit: appA:72 moved and unchanged, appA:73 `value changed` | PASS |
| Prose wording (Intro:135): `text changed` | PASS |
| Prose scope qualifier (Intro:135): `label changed` | PASS |
| Insertion inside a rewritten block: Intro:135 `text changed`, plus one unaccounted line flagged `numbers`, `marker` | PASS |
| Unit change: SM:964 MeV → GeV, reported `value changed` | PASS |
| Negation: FULL:1250 "is" → "is not", reported `label changed` | PASS |
| New paragraph away from every entry (top of Computation): one unaccounted line, flagged | PASS |
| New file: two unaccounted lines flagged `new-file` | PASS |
| Value change on a line that is not an entry: one unaccounted line and one deleted line, flagged `numbers` | PASS |
| Prose-comparison value (Bio:128): `value changed` only | PASS |
| Prose-comparison label (Bio:128): `label changed` only | PASS |
| Prose-comparison removal (Bio:128): `removed` only | PASS |
| Identifier digits: `X-48, G-2, spin-0 and 10-20 with -0.5` gives tokens `10`, `20`, `-0.5` | PASS |
| Passage moved out of Main: M:780 moved to Substratum; one `relocated` entry, flagged from Main; `any_change` true | PASS |
| Subtraction: Juno:238 `d−1` → `d−2`, reported `value changed` | PASS |
| Subtraction digits: `d−1`, `N−1`, `$2/(d-1)$` give tokens `1`, `1`, `2`, `1` | PASS |
| Display math: GR:480 `(d-3)` → `(d-4)` inside `$$…$$`, reported `value changed` | PASS |
| `--compare` against the pin: 3105 unchanged, nothing unaccounted or deleted, exit 0 | PASS |

**Scratch-copy test.** The pin corpus was copied to a temporary directory outside the repository and
edited in seven ways:
1. SM:1283's value `0.66667` → `0.66668`;
2. GR:547's match text `open` → `conditional`;
3. appA:106 (G2) deleted;
4. two lines inserted at the top of `papers/Main.md`;
5. a scope qualifier appended to M:780;
6. ch18:36's `10^{17}` → `10^{18}`;
7. a new file `papers/Synthetic.md`.

`--compare-tree --json` reported exactly these results, and exited 1:
- SM:1283 `value changed`;
- GR:547 `label changed`;
- appA:106 `removed`;
- M:780 `label changed`, at new line 782;
- ch18:36 `value changed`;
- three unaccounted lines: the inserted Main line and the two non-blank lines of the new file, the
  latter flagged;
- every other entry unchanged.

The copy is not retained. The same kinds of edit are re-run from `main` by `self-test`, which is the
support for the compare mode.

## 6. Departures from PREREG

Recorded in full in amendment A1. In brief:
- **P1/P1w.** The prose comparison rule, owner-approved; widened after the review.
- **P2 (was D1).** Lexical X4 scan for C-CDO, owner-approved. It adds M:650.
- **P3 (was D2).** Lexical finite-lattice scan for C-FINL, owner-approved. It adds 30 lines, among
  them SM:742 and Structure's large-N lines.
- **P4.** All 697 site-map sites.
- **P5.** M:566 in X-48.
- **R1.** Content pairing; unaccounted and deleted lines; unit in the value key; negation in the label
  signature; `--json <path>` with a schema; exit status.
- **R2.** Eight added countercontrols.
- **R3.** Identifier digits are not numbers.
- **R4.** A move across files is reported as `relocated` (flagged when it leaves Main) and counts as a
  change.
- **R5.** Subtraction digits (`d−1`, `$2/(d-1)$`) are kept. This changes number tokens in 59 entries;
  the entry set and texts are unchanged.
- **R6.** `--compare-tree` reports record the tree's basename only.
- **R7.** A one-line `$$…$$` display counts as math for R5. This changes number tokens in 10 entries;
  the entry set and texts are unchanged.

The unchanged earlier deviations:
- **D3.** Abbreviations `README`, `appb` and `appc` from the ledger cells were added. `Bio` and `Juno`
  were added for ids only (R3).
- **D4.** The mirror rule is applied to closure.
- **D5.** Format: one compact JSON line per entry; table numbers per cell; label-role cells keep their
  full text, and match-role cells keep their text with numbers removed.
- **D6.** The one in-place wording change to PREREG §5, which says where the scratch copy is kept. It
  was made after the CI added-text scan flagged a local-path word at `7dde93f3`. The note is in
  amendment A1.

## 7. Owner decisions

The two questions raised at `c2001d82` were decided in #1169 comment 7057674976. The prose expansion is
approved, and D1 and D2 are accepted as coverage additions. No owner decision is pending in this record.

## 8. Off-`main` references (§A.42 item 8)

| Reference | Claim it is attached to | Classification |
|---|---|---|
| #1169 comments 7056875845 and 7057674976 | Authorization, coverage approvals | provenance (quoted with author and time) |
| #1468 | Goal link, obligation | provenance |
| PR #1471 and its round-1 review record | Where this record is reviewed; the source of R1–R3 | provenance |
| `43eff402` (PREREG commit), `7dde93f3` (first extraction), `8c43c6cf` and `6f7da1f1` (amendment A1 commits) | The preregistration preceded the first extraction, and the amendment preceded the re-extraction | support: the claim uses the order of these commits. They are ancestors of this record's commit and become reachable from `main` only when the record lands by merge commit, which preserves them. A squash or rebase landing would not, and is excluded |
| Scratch-copy test (temporary directory outside the repository, not retained) | Compare mode on synthetic edits | provenance; the claim rests on `self-test`, on `main` with this record |
| `verification/audits/foundations/a1exit-ledger-20261120/` (blob ids in `snapshot.json`) | Ledger sites and rows | support on `main` |

## 9. Verification status (§A.46 item 4)

- **Evidence level.** A deterministic extraction from the Git objects at the pin. `check` regenerates
  it byte for byte, and the controls of §5 pass. It certifies only what the snapshot records about the
  pinned text, and makes no claim about the physics.
- **Missing.** A delta check of R7 (display math) and the regenerated snapshot. Round 3 at
  `fe25954d` returned ACCEPT.
- **Accountable Issue.** #1468.
- **Landing.** By merge commit only, so that the commits cited as support in §8 are reachable from
  `main`.
- **What would resolve it.** An independent review recorded on PR #1471. The before/after comparison
  and the verdict each need their own owner authorization.
