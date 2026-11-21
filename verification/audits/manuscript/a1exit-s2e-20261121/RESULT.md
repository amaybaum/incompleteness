# A1-EXIT Step 2, unit S2-E — Q3 propagation of the 81 remaining sites: result

**Status.** Writer's result, WIP / UNVERIFIED. Independent non-author review is required; merge is a
separate owner decision. Consistency work only (§A.23): no premise is added, no claim is strengthened,
bands unchanged.

**Authorization and Goal link.** As in `PREREG.md` (owner `amaybaum`, #1169 comment 7056875845; the
A1-exit objective, #1169).

**Commits.** PREREG and checker `a0a6a81fb` (pushed before any manuscript edit; draft PR #1475 opened
on it); edits with rebuilt `.tex`/`.pdf` `4fc9faef8`; RESULT `8e52b2177`. After review round 1
(REVISE, light; §8): amendment A1 `8caf2378d`, then its edits, the rebuilt book and this revision of
the record. Base `main`
at `1c7eedc40`. No edit adds or removes a line, so every site keeps its base (= ledger pin) line number.

## 1. Edits as applied

All 45 edits of `PREREG.md` §5 were applied verbatim by `checks/s2e_check.py apply`, with no deviation.
The five amending edits of `amendments/A1.md` (`checks/s2e_amend1.json`) were then applied verbatim by
`apply-amend`; they change the new strings of B07, B17, B16b, B11c and B14c.
`python3 -I -B verification/audits/manuscript/a1exit-s2e-20261121/checks/s2e_check.py` (mode `applied`)
prints `applied check PASS (45 edits, 5 amending, 0 failure(s))`: each new string occurs exactly once in its file
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
| B07 (+ A1-R1a) | ch18:226 = FULL:4957 | routed | as B06, with A4's standard and qualified cases |
| B08 | ch18:230 = FULL:4961 | routed | Klein-bottle quotient not a quotient by translations alone |
| B09 | ch18:36 = FULL:4767 | X-10 | maximal-entropy measure "of a finite representative" |
| B10 | ch18:162 = FULL:4893 | X-26 | finite substratum |
| B11a–c (+ A1-N2 on B11c) | ch18:166 = FULL:4897 | X-26, X-20 | finite substratum; exact-return form; near-return condition with S2-C's book parenthesis |
| B12 | ch18:168 = FULL:4899 | X-26 | finite substratum |
| B13a, B13b | ch18:170 = FULL:4901 | X-26, X-20 | exact-return form; scope to the named update and prior |
| B14a–c (+ A1-N6 on B14c) | ch18:172 = FULL:4903 | X-26, X-20 | sufficient condition, exact-return form |
| B15 | ch18:190 = FULL:4921 | X-26 | "of a finite model" |
| B16a, B16b (+ A1-N1 on B16b) | ch18:192 = FULL:4923 | X-26, X-20 | exact-return form; near-return condition |
| B17 (+ A1-R1b) | ch18:242 = FULL:4973 | X-80 | $\mathbb{Z}^3/P$ as A4's qualified case; Klein-bottle-type not a translation quotient; finite substratum |
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
  no dropped glyphs. The regenerated `.tex`/`.pdf` are in `4fc9faef8`; the book was rebuilt after
  amendment A1 (`build: OK`, 490 pages).

  | Artifact | Pages (base → branch) | Median characters per page (base → branch) |
  |---|---|---|
  | Computation | 21 → 21 | 2816 → 2816 |
  | Complexity | 31 → 31 | 2499 → 2499 |
  | Medicine | 28 → 28 | 2241 → 2241 |
  | Methodology | 53 → 53 | 3061 → 3066 |
  | book (FULL) | 489 → 490 | 2936 → 2936 (2937 before amendment A1) |

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
the diff is the seven entries above. After amendment A1 the diff is unchanged: the same six
prefixes and one added entry (the amended text lies beyond each stored 60-character prefix).

## 4. Deviations from PREREG

- **Manuscript.** None outside amendment A1, whose five edits were preregistered in `amendments/A1.md`
  (`8caf2378d`) before they were applied.
- **Checker.** As pushed in `8caf2378d`, the amendment check required each amendment's own new string to
  be absent before applying. A1-R1a's new string ("which is not a quotient by translations alone;") is a
  substring of B06's ch18:22 text, so that clause failed. It was replaced, before any amending edit was
  applied, by a count of the old string (once before, absent after); the full amended new string of each
  base edit remains checked for uniqueness. Stated in `amendments/A1.md`.

## 5. Points for review

- **Nit 5 (for the reconciliation).** ch14:184 and Comp:180: the conclusion that the framework's
  silence on P vs NP is "a feature" of what its axioms deliver stays unconditional, while its premise
  (finite physical structures) is scoped to a finite substratum by B03b and E01. The text predates S2-E
  and is not edited here.
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
| PR #1470, branch `research/a1exit-s2a-20261121` at `dd95fcd0b` | A4 restatement and the conditions on $P$ stated with each result ([SM §4.1], S2-A's E1), used by Meth:339 (E07), ch18:226 (B07) and ch18:242 (B17) | **support off `main`** (review round 1 R2): these sentences cite A4 in S2-A's form and SM §4.1's stated conditions, which are on #1470's branch only. Closed by landing order: S2-E lands only after #1470 (it lands fifth, after S2-A to S2-D). #1470 is on `main` (merged before `4de2eabd6`) and is merged into this branch by `66ccecc39`, so this is support on `main` (§9) ch18:22 (B06) uses only the owner's A4 decision (#1169 c.7048255658) |
| #1169 comments 7056875845, 7048255658, 7035888700, 7057200720 | authorization; A4 decision; glossary:105 routing; SC-42 precedent | provenance (owner records) |
| PR #1475 | this unit's guiding PR | provenance |

## 7. Verification status (§A.46 item 4)

- **Evidence level.** Manuscript consistency corrections with an exact-string checker; builds and the
  cheap gate checks above. No mathematical claim is added or strengthened; the near-return condition,
  (REV) and the region-level form are taken from statements on `main` (Main §2.3 corollary, §4.5 item
  (iii), §4.6) and S2-C/S2-D wording.
- **Missing.** Independent non-author review of the 45 edits, amendment A1 and the catch-up merge (§9);
  the ledger reconciliation after Step 2 (not done here); the deletion edit for the three
  deferred sites and ch18:40's pointer.
- **Accountable Issue.** #1169.
- **Resolution.** A recorded review of this branch's head. The SC-42 result was regenerated in §9.

## 8. Answer to review round 1 (REVISE, light, at `8e52b2177`)

| Item | Answer |
|---|---|
| R1 (blocking) | Applied: A1-R1a, A1-R1b delete "not among the cases A4 admits" at ch18:226 and :242 (and FULL); the statement that the identification is not a quotient by translations alone is kept |
| R2 (blocking) | Applied in §6 and the PR body: #1470 reclassified as support off `main` for Meth:339, ch18:226, ch18:242; S2-E lands only after #1470 |
| Nit 1 | Applied: A1-N1, "rests, as a sufficient condition, on" |
| Nit 2 | Applied: A1-N2, ", assumed as a hypothesis and not adopted," |
| Nit 3, nit 4 | Skipped (coordinator instruction) |
| Nit 5 | Recorded in §5 for the reconciliation |
| Nit 6 | Applied: A1-N6 drops "For a finite substratum," |

## 9. Catch-up with `main` at `4de2eabd6` (S2-A to S2-D landed)

**Merge.** `66ccecc39` merges `origin/main` at `4de2eabd6c7c88dc214db70a813ec44b8641b630` (first parent
this branch, second parent `main`; no rebase). Since the base `1c7eedc40`, `main` took in S2-A #1470,
#1476, S2-B #1473, S2-C #1474, the baseline record #1471 and S2-D #1472.

**Conflicts.** No `.md` file conflicted: the only file both sides changed is FULL.md, at disjoint lines,
and git merged it line by line. No manuscript line was resolved by hand, so there is no resolved line to
quote. The two conflicts were the generated `book/The-Incompleteness-of-Observation-FULL.tex` and
`.pdf`, both regenerated from the merged FULL.md by `sh ./build.sh --book` (`build: OK`, 490 pages;
median characters per page 2946, against 2937 for `main`'s PDF).

**Union check.** Every `.md` equals the base plus all landed units plus S2-E's accepted edits, and
nothing more:
- the 13 `.md` files only `main` changed (Main, SM, GR, Substratum, Structure, ch01, ch02, ch04, ch05,
  ch06, ch19, appB, appC) are byte-identical to `main` (`git diff origin/main` empty);
- the 7 `.md` files only S2-E changed (Computation, Complexity, Medicine, Methodology, ch14, ch18,
  glossary) are byte-identical to the S2-E head before the merge (`git diff` against it empty);
- FULL.md: applying S2-E's 28 FULL edits (the book edits of the 45, with the five amendments composed in)
  to `main`'s FULL.md, each old string unique there, reproduces the merged FULL.md byte for byte;
- `s2e_check.py`: `applied check PASS (45 edits, 5 amending, 0 failure(s))` on the merged tree.

**Copied wordings against what landed.**
- S2-C's return parenthesis occurs verbatim in `main`'s appC:104 and ch01:179 and in S2-E's ch18:166 and
  glossary:105; "assumed as a hypothesis and not adopted" as in ch01:179.
- S2-D's two Cx:212 new strings, extracted from `main`'s `a1exit-s2d-20261121/RESULT.md` §3, both occur in
  Cx:212.
- S2-A's A4 phrases on `main` (Sub:98, ch02:82: "as the standard construction, distinct from a continuous
  space", "admitted as a qualified case, under the conditions on $P$ stated with each result that uses
  it") are those S2-E's E07, B07 and B17 restate.

**Coverage and other checks.** `coverage_check`: OK, no stale entry. `duplicate_check`: it first failed on
this record, because PREREG E08a and E10 carried the same "Ledger row / Source" bullet. E10's source
annotation (PREREG line 303 and `s2e_edits.json`) gains ", applied to the constructive-OSR claim". This
changes no edit string; `duplicate_check` is then OK. The `s2e_check.py` docstring now states the
amendment check as implemented (round-2 nit). Register: the SC-42 added-text scan reports 0 failures.

**SC-42 regeneration** (owner approval as for S2-D, #1169 comment 7057200720, relayed by the
coordinator for this unit). From the merged tree:
- `check_sc42_integration.py` (normal) exits 0 with 0 `"ok": false`; the `-O` run is byte-identical;
- `--verbose` output (the CI comparison) is byte-identical to the regenerated
  `sc42-integration-result.json`;
- `--self-test`, normal and `-O`, are byte-identical to the unchanged `sc42-integration-controls.json`.

The diff against `main`'s file is exactly the earlier list, at shifted line numbers: six changed
predicates (lines 7067, 7079, 7127, 7171, 7175, 7203; ch18:166, :172, :192, :242, :244, :288) and one
added entry after line 7158 (ch18:230, the Levin paragraph). Every entry is a stored prefix of an S2-E
ch18 line, and each check is `ok`.
