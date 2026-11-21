# A1-EXIT regression audit (#1468): read-only "before" baseline — result

**This is a baseline only. It contains no comparison with any Step-2 head and no verdict.** It records
the state of every inventoried prediction, empirical comparison and A1-exit input site at the pin, so
that the later before/after comparison can be run mechanically. Whether removing A1 weakened,
strengthened or changed any physical prediction is not assessed here.

**Status.** Writer's paper-only record, WIP / UNVERIFIED. No independent review yet. No manuscript,
Lean, registry or ledger file is edited.

**Authorization.** Owner `amaybaum`, #1169 comment 7056875845, 2026-11-21T03:51:25Z: "#1468 read-only
regression baseline | **authorized**"; execution order item 2: "Capture the read-only "before" baseline
under #1468, before any manuscript change." The before/after comparison and the audit's verdict are not
authorized.

**Goal link (§A.47).** The A1-exit objective (#1169), through #1468: "Decides whether removing A1 has
weakened, strengthened or changed any physical prediction without explicit justification." This record
decides nothing for it; it fixes the "before" state.

**Pin.** `main` at `1c7eedc402eafd2bac654484fa790874a33f444d`. At drafting, `git log 1c7eedc4..origin/main
-- papers book` was empty, and so was `git log e837e3db..1c7eedc4 -- papers book`, so the A1-EXIT
ledger's site lines (pinned at `e837e3db`) are the lines at this pin. Corpus digest (SHA-256 over the
42 `papers/*.md` and `book/*.md` files at the pin, as computed by the extractor):
`6565dbcb26d5c2fd919e5c46def33c4eaa2baea40ebd34cdf04e381e75add41f`.

## 1. Files

| File | Content |
|---|---|
| `PREREG.md` | The inventory rule, entry schema, compare semantics and controls, pushed before extraction (commit `43eff402`) |
| `baseline.py` | The extractor: `build`, `check`, `self-test`, `--compare <commit>`, `--compare-tree <dir>` (standard library; reads Git objects at the pin) |
| `snapshot.json` | The baseline: one compact JSON line per entry, plus the pin, corpus digest, ledger blob ids and counts |

## 2. Recipe and expected result (§A.42 item 1)

Run from a clone that contains the pin and this record's commit (the head of PR #1471 at landing,
or `main` after it lands):

```
python3 -I -B verification/audits/foundations/a1exit-regression-20261121/baseline.py check
python3 -I -B verification/audits/foundations/a1exit-regression-20261121/baseline.py self-test
python3 -I -B verification/audits/foundations/a1exit-regression-20261121/baseline.py --compare 1c7eedc402eafd2bac654484fa790874a33f444d
```

Expected:
- `check PASS: snapshot.json regenerates byte for byte from 1c7eedc402eafd2bac654484fa790874a33f444d
  (sha256 ac8ce89c09e16115e9de3d565d6c9714029a255b5b79030ed8d67487bd54753a)`;
- `self-test PASS`, with every line above it `PASS`;
- `summary: {"unchanged": 1365}; new entries: 0`.

Run with Python 3.13. The output depends on `re`, `difflib` and `json` only; another Python 3 version
is expected to give the same bytes, and `check` detects any difference.

The later comparison, when it is authorized, is
`baseline.py --compare <after-commit>` (add `--json` for a structured report). It reports each entry as
`unchanged`, `text changed`, `value changed`, `label changed` (the last two together when both apply)
or `removed`, gives the new line of every mapped entry, and lists new entries (PREREG §4).

## 3. Coverage

1365 entries (709 table rows, 656 prose lines), 4362 numeric tokens. An entry can carry several
categories.

| Category | Entries | Ledger rows | Selected by |
|---|---|---|---|
| C-TAB, all table rows | 709 (prediction 405, status 109, other 195) in 110 tables | sitemap row where the line has one | table detector over the whole corpus |
| C-CDO, classical-dimension obstruction | 11 | X-48 | sitemap; ledger cells; FULL mirror; lexical X4 (D1) |
| C-FINL, finite-lattice numerics and extrapolations | 66 (36 ledger sites and mirrors, 30 added only by D2) | X-47 | sitemap; ledger cells; mirrors; lexical (D2) |
| C-CAL, calibration chain | 77 | X-70, X-71, X-72 | sitemap; ledger home and "also" ranges; mirrors |
| C-OBS, observer selection and global phase | 19 | X-63 | sitemap; ledger cells (incl. M:764); mirrors |
| C-OPEN, R1 and C1 open items | 6 | X-11, X-71 | sitemap; ledger cells |
| C-LEDGER, other §6.1 row-6 inputs | 495 | X-00–X-02, X-12, X-20, X-23, X-25, X-40–X-46, X-74 | sitemap; ledger cells; mirrors |

Ledger-selected entries by route: sitemap 376, ledger home cell 327, ledger sites cell 213, mirror
288, lexical X4 10, lexical FINL 55. Mirror search: 288 exact, 12 fuzzy (ratio 0.92–0.99, all
paper lines with a near-identical FULL line: Cx:474, GR:428, GR:474, GR:480, M:113, M:115, M:131,
SM:184, SM:202, SM:280, SM:314, Sub:389), 364 none (paper lines with no FULL restatement at ratio
0.90, and `README:100`).

**The named tables are all captured as C-TAB rows:** appendix-a A.4.1–A.4.4 and A.5 (62 rows,
including the G-rows at appA:106–113) and their FULL mirror (FULL:5517–5643); SM §7.6 (SM:1275–1296,
22 rows); GR §7.4 (GR:544–549, 6 rows); the book's status tables ch06 §6.5–6.8, ch07 §7.10, ch08
§8.6–8.7, ch09 §9.2–9.4, ch19 §19.4 and their FULL mirrors; and the remaining summary tables of the
companions (Juno §§1.3, 4.1, 4.2, 5.3, 6.1; SM §§3.2, 4.6, 6.2.1, 6.3, 7.2, 7.3, 7.5, 7.7, A.3;
Structure §§6.7, 7.7.4, 12.4, 14.5, 14.10; Main §§3.2, 4.5; Complexity, Computation, Medicine,
Bioinformatics).

**Named family sites at the pin.**
- C-CDO: M:358, M:564, M:568, M:588, M:606, M:650, M:780, Sub:533, ch04:146 = FULL:1250 (exact),
  Intro:135. The papers' sites have no FULL restatement at ratio 0.90.
- C-OPEN: SM:803, SM:809, SM:811, M:732, M:58 (X-11); GR:58 (X-71, also X-70).
- C-OBS: M:748, M:764, Sub:56, Sub:401, Sub:407, Sub:542, Str:718, Str:734, Comp:212, Meth:283,
  Meth:441, ch02:192 = FULL:822, ch03:58, ch04:36, ch04:178 = FULL:1282, FULL:919, FULL:1140.
- C-FINL and C-CAL: the site lists are in `snapshot.json` (`categories`).

**How the corpus was searched (§A.19).** (1) A table detector over every line of every top-level
`papers/*.md` and `book/*.md` (110 tables; listed by `grep '"kind":"table"' snapshot.json`); (2) the
ledger's complete site map (`sitemap.json`, 697 sites, whose extended scan reports 0 unmapped lines at
this tree) for every input row; (3) the ledger's own site citations in each input row's home and sites
cells, ranges expanded; (4) a mirror search of every selected prose line against FULL, and of every
FULL line against the chapters; (5) two lexical scans, D1 and D2 below; (6) a grep for prose lines
with a comparison marker (`±`, `\pm`, `σ`, `\sigma`, `PDG`, `CODATA`, `observed`, `measured`,
`measurement`, `experimental`) and a decimal number, used to size what the rule does not capture
(§4).

## 4. What the rule does not capture automatically, and limits

- **Prose comparisons outside the inventoried sites.** The grep of §3 (6) finds 890 non-table lines
  that quote a decimal number beside a comparison marker; 802 of them are not entries (abstracts,
  body text, the book's narrative). Where such a sentence restates a table row the table row is in the
  baseline, but the sentence is not. A change to such a sentence in the after-state is not reported.
  Extending the inventory to them is an owner question (§7).
- **Table notes.** Footnotes and caption paragraphs printed beside tables (e.g. the `ᵃ` notes under
  SM §7.6) are entries only when a ledger or lexical clause selects them.
- **Finite-lattice table rows outside X-47.** SM:735–740 (the A·B(N) data at N = 20–40) and
  SM:746–749 (the A·B(∞) estimators) are C-TAB rows (class `other` and `prediction`), not X-47 ledger
  sites. Their introducing lines SM:731 (not selected) and SM:742 (D2) differ in coverage; SM:731 is
  not an entry.
- **Ledger rows with no line of their own.** X-12, X-23, X-71 and X-74 have no primary site; they enter
  only through the sites named in their home and sites cells.
- **Values and units are parsed heuristically.** Numbers are tokens of the printed text; the unit is
  recorded only when one of the extractor's unit tokens follows; LaTeX exponents (`^2`) and identifiers
  in display math give extra small-integer tokens. The tokens are compared as printed, so a change
  of any token is reported; the descriptive fields (unit, role) can be wrong without hiding a change.
  Roles are assigned from column headers by the frozen regexes, and some row-name columns
  ("Observable") take the role `observed`.
- **Comparison data in prose** have no role: a prose entry records its numbers in order and its text,
  not which number is the prediction and which the datum.
- **Labels** are the status, class-mark and scope vocabularies of PREREG §3 and the text of
  label-role cells; a classification printed in other words is seen only as `text changed`.
- **New entries** are detected for table rows anywhere and for prose lines inserted next to a baseline
  prose entry. A new prose sentence elsewhere is not detected without a new site map.
- **Line alignment** is `difflib` over whole lines. A paragraph split or merged in the after-state maps
  by offset and may be reported as a removal plus a new entry rather than a text change.

## 5. Controls

All passed at the commit that adds this record.

| Control | Result |
|---|---|
| `check` (byte-for-byte regeneration from the pin) | PASS |
| Determinism (two builds identical, inside `self-test`) | PASS |
| Identity edit: 0 changed, 0 new | PASS |
| Shift: 3 lines inserted above appendix-a; its 65 entries reported `unchanged`, each moved by 3 | PASS |
| Countercontrol, changed value: appA:85 `2.361` → `2.362` reported `value changed`, nothing else | PASS |
| Countercontrol, changed label: appA:85 class `L` → `C` reported `label changed`, nothing else | PASS |
| Countercontrol, removed row: appA:72 deleted, reported `removed`, nothing else | PASS |
| Countercontrol, added row: one new table row reported, nothing changed | PASS |
| Countercontrol, prose wording: one word of Intro:135 altered, reported `text changed` | PASS |
| Countercontrol, prose scope: "for a fixed finite carrier" appended to Intro:135, reported `label changed` | PASS |
| `--compare` against the pin: 1365 unchanged, 0 new | PASS |

**Scratch-copy test.** The pin corpus was copied to a scratch directory and edited: SM:1283 Koide value
`0.66667` → `0.66668`; GR:547 match text `open` → `conditional`; appA:106 (G2) deleted; two lines inserted
at the top of `papers/Main.md`; a scope qualifier appended to M:780. `--compare-tree` reported exactly
`SM:1283 value changed`, `GR:547 label changed`, `appA:106 removed`, `M:780 label changed` (new line 782),
1361 unchanged (Main and appendix-a entries moved), 0 new. The scratch copy is not retained; the same
kinds of edit are re-run from `main` by `self-test`, which is the support for the compare mode.

## 6. Deviations from PREREG

- **D1.** C-CDO also takes every corpus line matching the ledger's extended pattern X4
  (`classical-dimension|N < \infty|fixed finite carrier`, `ledger_check.py`). Reason: the corpus search
  found M:650, which bounds cross-horizon representation consistency by the classical-dimension
  obstruction and is mapped FREE in the ledger; it is a reading of the same obstruction. Effect: M:650
  added (via `lexical-X4`).
- **D2.** C-FINL also takes every corpus line matching
  `[Ee]xtrapolat|[NL] *\\to *\\infty|[NL] *→ *∞|finite-[LN]\b|finite lattice`. Reason: SM:742
  ("Extrapolation to N → ∞") and SM:723, 755, 756, 759, 765, 767 in the same section are not X-47
  ledger sites. Effect: 30
  entries added via `lexical-FINL`, tagged so that they can be separated from the ledger sites; some
  (Structure's large-N lines Str:226–481) are not lattice-regulator numerics and are kept by the rule.
- **D3.** Abbreviations `README`, `appb` and `appc`, used in the ledger cells, were added to the
  prefix table.
- **D4.** The mirror rule is applied to closure: a line added as a mirror also gets a mirror search,
  and categories and rows propagate to a fixed point.
- **D5.** Format. `snapshot.json` writes one compact JSON line per entry, and a table row's numbers
  are stored per cell rather than also at the top level of the entry; a role-`label` cell keeps its
  full text in the label signature, and a role-`match` cell keeps its text with numbers removed.
- **D6.** One wording change in PREREG §5 (where the scratch copy is kept), made after the CI
  added-text scan flagged a local-path word at `7dde93f3`. The rule is unchanged.

## 7. Owner decisions needed

1. Whether the inventory should be extended, before any Step-2 head is compared, to the 802 prose
   lines of §4 that quote numbers beside a comparison marker. Extending it is mechanical (one more
   clause) but adds about 0.8 MB to the snapshot.
2. Whether the lexical supplements D1 and D2 are accepted as part of the baseline. Both only add
   entries; neither removes a ledger site.

## 8. Off-`main` references (§A.42 item 8)

| Reference | Claim it is attached to | Classification |
|---|---|---|
| #1169 comment 7056875845 | Authorization | provenance (quoted with author and time) |
| #1468 | Goal link, obligation | provenance |
| PR #1471 | Where this record is reviewed | provenance |
| Scratch-copy test (temporary directory outside the repository, not retained) | Compare mode works on a synthetic edit | provenance; the claim rests on `self-test`, on `main` with this record |
| `verification/audits/foundations/a1exit-ledger-20261120/` (blob ids in `snapshot.json`) | Ledger sites and rows | support on `main` |

## 9. Verification status (§A.46 item 4)

- **Evidence level.** A deterministic extraction from Git objects at the pin, regenerated byte for
  byte by `check`, with the controls of §5. It certifies only what the snapshot records about the
  pinned text; it makes no claim about the physics.
- **Missing.** Independent non-author review of the inventory rule, the deviations D1–D6, and the
  snapshot's coverage.
- **Accountable Issue.** #1468.
- **What would resolve it.** An independent review recorded on PR #1471, and owner decisions on §7.
  The before/after comparison and the verdict need their own owner authorization.
