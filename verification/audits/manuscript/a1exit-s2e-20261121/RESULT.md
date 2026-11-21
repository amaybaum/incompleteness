# A1-EXIT Step 2, unit S2-E — Q3 propagation of the 81 remaining sites: result

**Status.** Writer's result, WIP / UNVERIFIED. Independent non-author review is required; merge is a
separate owner decision. Consistency work only (§A.23): no premise is added, no claim is strengthened,
bands unchanged.

**Authorization and Goal link.** As in `PREREG.md` (owner `amaybaum`, #1169 comment 7056875845; the
A1-exit objective, #1169).

**Commits.** PREREG and checker `a0a6a81fb` (pushed before any manuscript edit; draft PR #1475 opened
on it); edits with rebuilt `.tex`/`.pdf` `4fc9faef8`; this RESULT in the following commit. Base `main`
at `1c7eedc40`. No edit adds or removes a line, so every site keeps its base (= ledger pin) line number.

## 1. Edits as applied

All 45 edits of `PREREG.md` §5 were applied verbatim by `checks/s2e_check.py apply`, with no deviation.
`python3 -I -B verification/audits/manuscript/a1exit-s2e-20261121/checks/s2e_check.py` (mode `applied`)
prints `applied check PASS (45 edits, 0 failure(s))`: each new string occurs exactly once in its file
and, for a book edit, in FULL.md; no old string survives; each edited book line is byte-identical to
its FULL line.

| Edit | Site (line on this branch) | Row | Form |
|---|---|---|---|
| E01 | Comp:178 | X-55 | finite substratum |
| E02 | Comp:182 | X-55 | ledger wording "A finite substratum" |
| E03a, E03b | Cx:212 | X-82, X-63 (T17b) | S2-D wording: region form; past hypothesis and inflow open |
| E04 | Med:35 | X-20 | "on a finite representative" |
| E05a–c | Meth:146 | X-30 | "on a finite representative" (eventual-image horn) |
| E06 | Meth:148 | X-30 | (REV) as the posit, finite case from injectivity |
| E07 | Meth:339 | X-45 | finite substratum, A4's qualified quotient, A2–A6 |
| E08a, E08b | Meth:345 | X-45 | A2–A6 and the restriction to finite substrata |
| E09a, E09b | Meth:357 | X-45 | finite substratum |
| E10 | Meth:367 | X-45 | class of finite substrata satisfying A2–A6 |
| E11 | Meth:369 | X-45 | as E10 |
| E12 | Meth:517 | X-01 (owner Q3) | substrate stated as $\varphi$ on $S$, no finiteness asserted |
| B01–B04 | ch14:160, :164, :184, :262 = FULL:3760, :3764, :3784, :3862 | X-55 | finite substratum |
| B05 | ch18:20 = FULL:4751 | X-26 | finite substratum |
| B06 | ch18:22 = FULL:4753 | routed | $\mathbb{Z}^3$ distinct from $\mathbb{R}^3$; Klein-bottle-type not a translation quotient |
| B07 | ch18:226 = FULL:4957 | routed | as B06, with A4's standard and qualified cases |
| B08 | ch18:230 = FULL:4961 | routed | Klein-bottle quotient not a quotient by translations alone |
| B09 | ch18:36 = FULL:4767 | X-10 | maximal-entropy measure "of a finite representative" |
| B10 | ch18:162 = FULL:4893 | X-26 | finite substratum |
| B11a–c | ch18:166 = FULL:4897 | X-26, X-20 | finite substratum; exact-return form; near-return condition with S2-C's book parenthesis |
| B12 | ch18:168 = FULL:4899 | X-26 | finite substratum |
| B13a, B13b | ch18:170 = FULL:4901 | X-26, X-20 | exact-return form; scope to the named update and prior |
| B14a–c | ch18:172 = FULL:4903 | X-26, X-20 | sufficient condition, exact-return form |
| B15 | ch18:190 = FULL:4921 | X-26 | "of a finite model" |
| B16a, B16b | ch18:192 = FULL:4923 | X-26, X-20 | exact-return form; near-return condition |
| B17 | ch18:242 = FULL:4973 | X-80 | $\mathbb{Z}^3/P$ as A4's qualified case; Klein-bottle-type not admitted; finite substratum |
| B18–B20 | ch18:244, :260, :288 = FULL:4975, :4991, :5019 | X-80 | finite substratum |
| G01 | gloss:105 = FULL:6596 | X-20 | "or the near-return condition (NR), assumed as a hypothesis and not adopted" + S2-C parenthesis |

**Ledger sites changed (for the post-Step-2 reconciliation; base = new line).** Comp:178, :182 (X-55);
Cx:212 (X-82); Med:35 (X-20); Meth:146, :148 (X-30); Meth:339, :345, :357, :367, :369 (X-45);
Meth:517 (X-01); ch14:160, :164, :184, :262 and FULL:3760, :3764, :3784, :3862 (X-55); ch18:20, :162,
:166, :168, :170, :172, :190, :192 and FULL:4751, :4893, :4897, :4899, :4901, :4903, :4921, :4923
(X-26); ch18:36 and FULL:4767 (X-10); ch18:242, :244, :260, :288 and FULL:4973, :4975, :4991, :5019
(X-80); glossary:105 (X-20). 47 ledger sites. Also changed, not ledger Q3 sites: FULL:6596 (glossary
mirror), ch18:22, :226, :230 and FULL:4753, :4957, :4961 (routed).

**Deferred to the deletion edit (unchanged).** Comp:120, Meth:156, Meth:158 (row X-01): each site's
only A1 content is a pointer to the posit.

**No change (31).** Comp:122 and ch14:272 = FULL:3872 (X-10, already "of a finite representative");
Intro:12, :93 (X-20, already scoped to finite reversible models); Med:25 (X-24, already "one fixed
finite reversible representative"); Meth:106 (X-30, a rung of the ladder, status stated at :146–:148);
Meth:283, :441 (X-63, region-level exclusion on a finite bijective model, S2-D §3); ch18:40 = FULL:4771
(X-82, per the S2-D reviewer: the sentence does not use finiteness to exclude an inflow; its
"recurrent under A1 (§18.7)" is a pointer left for the deletion edit); ch18:164, :174, :176, :178,
:179, :180, :183, :184, :186, :188 and their FULL mirrors (X-26: the section heading, and mathematics of
a finite set, an illustration, or statements already scoped "a finite model", inside the section that
B11 finite-scopes).

## 2. Propagation (§A.25, §A.14)

Re-grep of `papers/*.md` and `book/*.md` (FULL included) on this branch:

| Phrase | Remaining | Note |
|---|---|---|
| "realize A1", "model A1", "hypothesis of finite information" | 0 | all were S2-E sites |
| "finiteness hypothesis" | appC 1, ch19 1, FULL 2 | X-01 pointer sites (appC:98, ch19:360 and their FULL mirrors), deletion edit; none in Comp or Meth |
| "under A1" in S2-E files | ch18:40 = FULL:4771 | no change (above) |
| "A1" in Comp, Cx, Med, Meth, ch14, ch18 | Meth:156, :158; ch18:40 | deferred / no change; the Comp:120 pointer says "the total-finiteness posit" |
| "A1–A6" | Str 23, Sub 9, GR 2, ch02 4, ch03 3, ch04 4, ch05 1, glossary 1, FULL 13; Meth 0 | outside S2-E: X-45 home sites are pointer sites of the deletion edit (Sub:104, ch02, ch04, glossary:13) or X-46 |
| "Klein-bottle quotient" | ch18:230 = FULL | qualified in place (B08) |
| "Klein-bottle-type identification" | ch18 3, FULL 3 | B06, B07, B17 |
| "has no finite-window test" | ch18:166, glossary:105, FULL 2 | S2-C's parenthesis (S2-C's own sites are on its branch) |
| "non-equilibrium phase" | Main 1, Sub 3, ch02 2, FULL 2; Cx 0 | S2-D sites on its branch; Cx:212 done here |

- **Book mirrors.** Every edited ch14, ch18 and glossary line is byte-identical to its FULL line
  (`s2e_check.py`).
- **Companion restatements.** No other paper restates the Comp, Cx, Med or Meth sentences edited here
  (distinctive-phrase grep at the base found one occurrence of each). Main is not edited.
- **Counts.** No inventory or count changes.

## 3. Build, coverage and checks

- `sh ./build.sh Computation Complexity Medicine Methodology` and `sh ./build.sh --book`: `build: OK`,
  no dropped glyphs. The regenerated `.tex`/`.pdf` are in `4fc9faef8`.

  | Artifact | Pages (base → branch) | Median characters per page (base → branch) |
  |---|---|---|
  | Computation | 21 → 21 | 2816 → 2816 |
  | Complexity | 31 → 31 | 2499 → 2499 |
  | Medicine | 28 → 28 | 2241 → 2241 |
  | Methodology | 53 → 53 | 3061 → 3066 |
  | book (FULL) | 489 → 490 | 2936 → 2937 |

- `python3 tools/coverage_check.py`: `coverage_check: OK (132 canonical statements, 20 unattached
  checkers)`, no stale fingerprint; `verification/coverage/LEDGER.json` unchanged.
- `tools/lean_manuscript_census.py`: OK. `tools/artifact_placement_check.py`: OK.
  `tools/legacy_records_check.py <head>`: `UNDECIDABLE (shallow-repository)` in this worktree; no file
  is added under a closed namespace.
- Added-text register scan (§A.32, §A.33) over the 45 new strings: no revision-history word,
  meta-commentary, reader instruction or caps emphasis.

### SC-42 integration result (open item; needs an owner decision)

`verification/audits/manuscript/bell-operational-reconciliation-20261029/check_sc42_integration.py`
exits 0 on this branch, and every check is `ok` (0 `"ok": false`), but its output differs from the
checked-in `sc42-integration-result.json`. The file stores 60-character prefixes of book lines whose
FULL mirroring it checks. The edits change six stored prefixes (ch18:166, :172, :192, :242, :244,
:288) and add one entry (the ch18:230 line enters the checker's diff). CI's SC-42 step will therefore
fail until the file is regenerated. S2-D regenerated the same file under a narrowly scoped owner
approval (#1169 comment 7057200720). No regeneration is made here without the same approval; when
given, the procedure is S2-D's (normal and `-O` runs byte-identical, the controls file unchanged), and
the diff is the seven entries above.

## 4. Deviations from PREREG

None. Every edit was applied as preregistered.

## 5. Points for review

- **ch18:226 (B07).** The paragraph keeps "that is not determined by the framework's structural
  commitments" after listing a Klein-bottle-type identification, which B07 marks as not among the cases
  A4 admits. The sentence is accurate for the cases A4 admits; whether the paragraph should also state
  that A4 excludes the Klein-bottle-type option is left to review rather than added here.
- **Med:35 (E04).** The finite-only scope was chosen over adding (NR) inside the parenthesis; the
  sentence is then a statement about a finite representative, as at Med:25.
- **Meth:517 (E12).** Row X-01 site that is not a pointer: the type-level argument does not use
  finiteness, so the finite set is replaced by $\varphi$ on $S$ (Methodology §3.1's own definition).
- **Meth X-45 sites.** Edited per X-45's correction while the home site Sub:104 (a pointer site) keeps
  "A1–A6" until the deletion edit. The two readings agree: A1 together with A2–A6 is a finite
  substratum satisfying A2–A6.

## 6. Off-`main` references (§A.42 item 8)

| Reference | Attached to | Class |
|---|---|---|
| PR #1474, branch `research/a1exit-s2c-20261121` at `cb6d1b87e` (S2-C RESULT §2) | source of the return-form parenthesis and finite-only scope (B11c, B16b, G01, E04) | provenance: the wording is reproduced in full in `checks/s2e_edits.json`; no claim here uses S2-C's edits |
| PR #1472, branch `research/a1exit-s2d-20261121` at `c5aaeb73f` (S2-D RESULT §3) | source of E03a, E03b; no change at ch18:40, Meth:283, :441 | provenance: wording reproduced in full; the region-level reading rests on Main §4.6 on `main` |
| PR #1470, branch `research/a1exit-s2a-20261121` at `dd95fcd0b` | A4 qualified-case wording (E07, B06, B07, B17) | provenance: the owner's A4 decision (#1169 c.7048255658) is the authority; wording reproduced in full |
| #1169 comments 7056875845, 7048255658, 7035888700, 7057200720 | authorization; A4 decision; glossary:105 routing; SC-42 precedent | provenance (owner records) |
| PR #1475 | this unit's guiding PR | provenance |

## 7. Verification status (§A.46 item 4)

- **Evidence level.** Manuscript consistency corrections with an exact-string checker; builds and the
  cheap gate checks above. No mathematical claim is added or strengthened; the near-return condition,
  (REV) and the region-level form are taken from statements on `main` (Main §2.3 corollary, §4.5 item
  (iii), §4.6) and S2-C/S2-D wording.
- **Missing.** Independent non-author review of the 45 edits; the SC-42 result regeneration (owner
  decision); the ledger reconciliation after Step 2 (not done here); the deletion edit for the three
  deferred sites and ch18:40's pointer.
- **Accountable Issue.** #1169.
- **Resolution.** A recorded review of this branch's head, and the owner's decision on the SC-42
  regeneration.
