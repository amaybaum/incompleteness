# A1-EXIT regression audit (#1468): read-only "before" baseline — preregistration

**Status.** Writer's paper-only preregistration, WIP / UNVERIFIED. It is committed and pushed before
any extraction is run, and it fixes the inventory rule the extractor implements. This unit captures a
baseline only. It edits no manuscript, Lean module, registry or ledger file, compares against no
Step-2 head, and renders no verdict. Independent non-author review is required before any use.

**Authorization.** Owner `amaybaum`, #1169 comment 7056875845, 2026-11-21T03:51:25Z, Step 2 decisions
table: "#1468 read-only regression baseline | **authorized**"; execution order item 2: "Capture the
read-only "before" baseline under #1468, before any manuscript change." The later before/after
comparison and the audit's verdict are not authorized by that record and are not performed here.

**Goal link (§A.47).** The A1-exit objective (#1169), through #1468: "Decides whether removing A1 has
weakened, strengthened or changed any physical prediction without explicit justification." This unit
decides nothing for it. It fixes the "before" state so that the later comparison is mechanical.

**Pin.** `main` at `1c7eedc402eafd2bac654484fa790874a33f444d` (merge of #1469). No commit in
`1c7eedc4..origin/main` touches `papers/` or `book/` at drafting time, and no commit in
`e837e3db..1c7eedc4` does either, so the A1-EXIT ledger's site lines (pinned at `e837e3db`) are the
lines at this pin. `File:n` is line `n` at the pin. The extractor reads every source from Git objects
at the pin (`git show <pin>:<path>`), not from the working tree.

## 1. Corpus

Every top-level `*.md` file in `papers/` and `book/` at the pin (the ledger's `corpus_files()` set,
which includes `book/The-Incompleteness-of-Observation-FULL.md`). Generated `.tex`/`.pdf` files are
not read.

## 2. Inventory rule

An **entry** is one physical line of one corpus file at the pin, identified by `(file, line)`. A line
selected by several clauses is one entry carrying every category and ledger row that selects it.

**C-TAB (task item 1: status, prediction and numeric summary tables).** Every data row of every
pipe table in the corpus. A pipe table is a line beginning `|` immediately followed by a delimiter
line matching `^\|[\s:|-]+\|\s*$`; its data rows are the following consecutive lines beginning `|`.
All tables are taken, not a hand-picked subset, so that no summary table of predictions or numeric
values can be missed by judgement. Each table is given a class from its header row, recorded but not
used to exclude anything:
- `prediction` if the header matches `Predict|Observ|Match|Empirical|Measure|Deviation|Discrepanc|σ|\\sigma|Residual|Testab|Value|value|Leading`;
- else `status` if it matches `Status|Class|Tier|Emerges|Transports|Layer`;
- else `other`.

**Ledger clauses (task items 2–5 and LEDGER §6.1 row 6).** For each ledger row `R` in the input set
below, the entries are:
1. every site in `sitemap.json` whose `row` is `R`;
2. every site named in `R`'s "Dependency (home at the pin)" cell and in its "Sites" cell (including
   the sites after "also") in the §2 table of `LEDGER.md` (between `TABLE:BEGIN` and `TABLE:END`),
   with `a–b` ranges expanded and a bare `:n` taking the preceding file prefix; blank lines and table
   delimiter lines are skipped. Abbreviations are the ledger PREREG's (`M`, `SM`, `GR`, `Sub`, `Str`,
   `Meth`, `Comp`, `Cx`, `Intro`, `Med`, `chNN`, `appA/appa`, `appB`, `appC`, `gloss`, `FULL`); an
   unrecognized prefix in those cells fails the build;
3. the mirror of every entry selected by 1–2 (rule below).

| Category | Ledger rows | Source of the scope |
|---|---|---|
| C-CDO (classical-dimension obstruction) | X-48 | task item 2; #1468 |
| C-FINL (finite-lattice numerics and extrapolations) | X-47 | task item 3; #1468 |
| C-CAL (calibration chain) | X-70, X-71, X-72 | task item 4; LEDGER §6.1 row 6 |
| C-OBS (observer selection, global phase) | X-63 | task item 4; LEDGER §6.1 row 6 |
| C-OPEN (R1 and C1 open items) | X-11, X-71 | task item 5; LEDGER §6.1 "R1, C1" |
| C-LEDGER (other §6.1 row-6 inputs: rows whose correction changes a printed statement, and the P-indivisibility route) | X-00, X-01, X-02, X-12, X-20, X-23, X-25, X-40, X-41, X-42, X-43, X-44, X-45, X-46, X-74 | LEDGER §6.1 row 6 |

**Mirror rule.** For an entry's line text `t` in file `f`, the search set is
`book/The-Incompleteness-of-Observation-FULL.md` when `f` is any other corpus file, and every
`book/*.md` except FULL and `book/README.md` when `f` is FULL. The mirror is the unique line of the
search set equal to `t`; failing that, the line of highest `difflib.SequenceMatcher` ratio, if that
ratio is at least 0.90 (lowest file, then line, on ties); failing that, none. The method
(`exact` / `fuzzy:<ratio>`) is recorded. Lines shorter than 40 characters get no mirror search.

## 3. What each entry records

- `file`, `line`, `id` (`<abbrev>:<line>`), `categories`, `ledger_rows` (the sitemap row of the line
  where the sitemap has one, plus every input row that selected it), `mirror` (with method);
- `text`: the verbatim line;
- `kind`: `table` or `prose`. A table row also records its table (file ordinal, class, nearest
  preceding heading, header columns) and its cells, each with column name, a role and its numbers.
  The role is the first of these whose regex matches the column header (case-sensitive):
  `label` `Class|Status|Tier|Layer|Cat\b|Input|Testab|Emerges|Transports|role`;
  `match` `Match|match|Deviation|Discrepanc|Residual|σ|\\sigma`;
  `observed` `Observ|Measure|Data|PDG|Experiment`;
  `predicted` `Predict|Formula|Value|value|Leading|Quantitative|Required|Estimated`;
  otherwise `other`;
- `numbers`: every numeric token, in order, with the uncertainty (`±`/`\pm` terms, parenthesized
  digits, `^{+a}_{-b}`), power of ten, a unit when one of the listed unit tokens follows, and the
  number of printed decimals. Section, chapter and citation numerals (`§6.4`, `Ch 6`, `[55]`) and
  digits inside identifiers (`G11`, `C1`, `X-48`) are not numbers;
- `labels`: the ordered status terms and scope terms found in the line (vocabularies frozen in the
  extractor: theorem/proposition/lemma/proved/derived/conditional/open/hypothesis/posit/
  conjecture/retrodiction/calibration/imported/input/fit/empirical/numerical/estimate/inconclusive/
  established/exact/bound/compatible…; `**S**`…`**E**` class marks; `Tier n`, `Layer n`;
  finite/infinite/continuum/lattice/torus/periodic/carrier/extrapolat…/converge…/approximat…/
  `L → ∞`/ℤ); and for a table row the text of its `label` and `match` cells with numbers removed.

The snapshot also records the pin, a SHA-256 digest of the corpus at the pin, the blob ids of the
ledger files used, and counts per category.

## 4. Compare mode (implemented now; run only on synthetic edits in this unit)

`--compare <commit>` (or `--compare-tree <dir>`) reads the corpus at the other state and aligns each
file's lines with the pin by `difflib.SequenceMatcher(autojunk=False)`. A baseline entry in an
`equal` block maps to its new line. In a `replace` block, lines are paired by offset up to the shorter
side; unpaired old lines are `removed`; a `delete` block's lines are `removed`. A mapped entry is
re-extracted at its new line and reported as:
- `unchanged` (text identical; a moved line is reported with its new line number);
- `value changed` (the sequence of numeric tokens differs);
- `label changed` (the label signature differs);
- `text changed` (text differs, numbers and labels do not).
Value and label changes are reported together when both occur. **New entries** are table rows at the
other state that are not the image of a baseline entry, and lines inserted inside a `replace` or
`insert` block adjacent to a baseline prose entry (unpaired new lines). New prose lines elsewhere are
not detectable without a new site map; that limit is stated in RESULT.

## 5. Controls (all must pass before the snapshot is committed)

- **Determinism.** `build` twice gives identical bytes; `check` regenerates `snapshot.json` from the
  pin and compares bytes.
- **Self-test.** On in-memory copies of the pin corpus: the identity edit reports every entry
  `unchanged` and no new entry; inserting unrelated lines above entries reports them `unchanged`
  (moved); countercontrols must each be detected, and only at their target: a changed value in a
  prediction-table row (`value changed`), a changed class label in a table row (`label changed`), a
  removed table row (`removed`), an added table row (new), a wording change in a prose site that
  touches no number or term (`text changed`), and an added scope qualifier in a prose site
  (`label changed`).
- **Scratch-copy test.** A copy of the pin corpus in a temporary directory outside the repository, with a synthetic edit, is compared
  with `--compare-tree`; its report must show exactly the synthetic changes.

There is no decision rule over manuscript content: this unit records a state and renders no verdict.
