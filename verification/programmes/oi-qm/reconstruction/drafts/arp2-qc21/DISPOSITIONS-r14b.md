# Q-C2-1 (ARP-2-QC21): dispositions of r14b

WIP / UNVERIFIED. Model-written. Drafting record, not a control-plane artifact.

- **Input:** r14a, sha256 `1dd595d30eafb65dce341b1c6306ef85b4876ce008f5e45639f893247daad708`, kept unchanged in
  `r14a/preregistration.draft.md`, with `r14a/DISPOSITIONS-r14a.md` (`680f1341…`) and `r14a/IMPL-DELTA-r14a.md`
  (`cb9f0c4e…`).
- **Output:** r14b, `preregistration.draft.md` (3633 lines). Its sha256 is reported with this file, not in it.
- **Work list:** `review/REVIEW-QC21-r14a.md` (`f30841bafd9742c93785bc153b75e5bca2ef1b0e1bc0714d0f535c7e10cfb3c3`),
  REVISE (minor): R14A-B1, N1–N13, I1–I5. The wording reused for R14A-B1 is Q-C2-2 r14's
  (`../qc22/preregistration.draft.md`, `9e3ef0c9…`; read only): its lines 1113 (template), 1494 (comment read) and
  1644 (`verdict` condition).
- **Authority:** #1169 c.6740078002 (amaybaum, OWNER, 2026-11-09T12:29:10Z): r14, script updates, ordinary
  non-scientific self-tests, independent preparation review. Not authorized: the design run, the gate tests, `F`,
  dispatch, any scientific computation.
- **Nothing was run** except text tools. No LP, stress test, script self-test or computation on any OI
  construction. The scripts in `wt-impl` were read, not run or changed. The review's text-only probes
  `review/probes-r14a/control_p_coverage.py` and `v3_blocks.py` were run on r14b (they read files only).
  `r14bwork/check_rows.py` is a text check of the new edit-log rows. No repo, git or GitHub write. No Q-C2-2 file
  was changed.
- **Build:** `r14bwork/make_r14b.py` checks r14a's sha256, then applies 56 exact replacements, each required to
  match once. Re-running it reproduces r14b byte for byte. Diff: `r14bwork/r14a-r14b.diff`. `IMPL-DELTA-r14b.md` is
  built the same way by `r14bwork/make_impl_r14b.py` from r14a's.
- **Line numbers** below are r14b's.

## Checks run on r14b (text only)

- **V3 blocks.** The `v3-round` and `v3-governed-paths` blocks are byte-identical to r14a's.
- **Control P's rule** (the review's probe). It catches 35 lines, r14a's 31 plus the four new placeholders: DSN's pin
  (661), the D18 and D14 items (1601–1602) and R9 (1675). The 9 lines it skips name the word only, as in r14a.
- **Edit-log rows 82 and 99–108.** Each "copied text" fragment occurs in r14a and each "becomes" fragment in r14b
  (`r14bwork/check_rows.py`).
- **Line width.** No line added by r14b exceeds 120 characters outside tables and quotations, the title excepted.

## 1. Blocker

| finding | change | r14b lines |
| --- | --- | --- |
| **R14A-B1** `verdict` cannot read the `E` approval comment | (i) Rule (g) gains the template `` `issues/comments/{DEC}` ``, in Q-C2-2 r14's wording, read by `verdict` and `e-entry` (edit row 99). (ii) C.3's *prior authorization* gains Q-C2-2's line "The comment is read through `GET issues/comments/{DEC}`" (row 101). (iii) C.3's `verdict` list gains Q-C2-2's condition "every approval entry holds, the `E` dispatch's included", stating that each entry is checked as *Approval entries* states and that `E`'s is built from the `E` approval comment's id (row 105). (iv) Under R8's draft default, the ratification comment is read through the same template (C.3's designation bullet, row 103; C.8 item 9). (v) C.8 item 9's inputs now include, as `a_ok` DEC arguments, the ids of the comments `verdict` reads besides the approval comments: the designation of `E`, and, under R8's default, the ratification. This is the same gap: C.3 already required `verdict` to check the designation of `E`, and no template or argument let it read that comment. (vi) IMPL-DELTA D20 adds the template to `GH_TEMPLATES` (I1), and D21 adds the `verdict` condition | 2812–2813; 2357; 2482–2488; 3189–3193; rows 99, 101, 103 and 105 (1892–1898) |

## 2. Nits

| finding | change (or refusal) | r14b lines |
| --- | --- | --- |
| **N1** (R8 sites) | Each site now says that the designation of `E` ratifies every entry in `approvals.json`, and that the `E` dispatch's own entry is ratified as R8 provides, labelled "draft default, pending owner ruling R8". Sites: 1395–1396, 1431–1432, 1486, 1501, the PENDING owner commitment at 1506–1508, C.3's *Authorship* (2361–2364, row 102) and C.3's designation bullet (2482–2485, row 103). The two invariant rows that cite "ratification at `E`" (1555, 3630) are labelled too. **In copied C.3 the wording is "every approval entry committed at `E` (C.8 item 9)", not "in `approvals.json`".** Reason: Scope's acceptance condition 3 and *After the edits* say that no copied `verdict` condition refers to `approvals`, meaning the Environment's approvals endpoint. The same file elsewhere uses the token `approvals.json`, but a literal check would read it as a hit. The meaning is the same | listed |
| **N2** (other unlabelled defaults) | **R2:** C.6's `E` line (row 108), C.6's S1 checker-outcome line (row 107) and `verdict`'s job-A condition (row 104). **R1:** invariant row 1571. **R3 and R5:** adaptation row 1926. **R6:** C.3's S1-binding condition (row 106), and the two Scope-table cells on S1's artifact (1485, 1496). Further sites carrying R5's default ("the general caps" for the reported-only fragments) are labelled: 395, 434, 1078, 1109, 1377, 3016 and 3228. **R7:** C.8 item 2's count sentence (3091–3093) | as listed |
| **N3** (R8 framing) | C.8 item 9 and R8 are narrowed. `order.json`, which the designation ratifies, is in `E`'s tree and cannot hold the entry. The designation follows the `E` run (§A.39), so it could quote the entry's sha256. The designation is now R8's concrete alternative. The step that builds the entry before `verdict`'s capture is named: a new `controls.py` mode, `e-entry <E> <comment id>`. It builds the entry with `verdict`'s own function, prints the entry and its sha256, and prints no `VERDICT` line. Both R8 options use it. The mode is added to C.5's mode list (row 100) | 1665–1674; 3196–3204; 2706–2707 |
| **N4** (R1 boundary) | R1's draft default now states the floor and the lowering rule together. The floor is `10^5`. After a red design run, the next `S_max` is at least `10^5` if the red run's value was above it. If the red run was at `10^5`, the next value is a smaller positive integer, and the same recorded decision removes the floor from `check --freeze`'s `S_max` check before that design run; B-P's binomial cap then stays `10^5`. So an admissible value exists after a red run at the floor. R1 also gets a self-contained alternative: no floor at any stage. No value is chosen. The `check --freeze` bullet and the *Before the design run* bullet carry the labelled rule | 1613–1623; 3055–3058; 3104–3106 |
| **N5** (R4 and R5 alternatives) | **R4's alternative** no longer presupposes R3's. The reference is chosen with the reported-only term set to 0, and the reported-only fragments share the remainder `W_RO = (1200 − t_810)/σ − W_max^BP − 2·W_fix − W_stress`, in job B's build order. Beyond it they are `out_of_scope` and reported, whatever R3's ruling. **R5's alternative** names B-P's caps and budget triple for every B fragment, the general ones for QM-P's restricted fragment and the fixtures, and the new left side `σ × (1204 · W_max^BP + 2·W_fix + W_stress) + t_810`. **R3's alternative** now names `W_RO`, its place in the left side, the order and SF-2's treatment. **R2, R6 and R7's alternatives** were also made self-contained (R2: the readings needed; R6: what still binds the measurements; R7: the roles' caps and the timeout charge) | 1631–1652; 1624–1630; 1653–1664 |
| **N6** (control P coverage) | DSN's Inputs row carries "(PENDING: path and blob on `main`)", like RCH's. Precondition 2's D18 and D14 items carry "(PENDING)", like the sketch-review item. Control P now catches all three | 661; 1601–1602 |
| **N7** (cap values) | **Option taken: the checker's constants govern.** C.8 item 1 gains a bullet. The values written for B-P's caps and both budget triples, in C.8 item 1 and in C.7, are copies of `check --freeze`'s printed recomputation. `check --freeze` does not parse them; it compares the checker's constants with the recomputation. Parsing would need the cap list restructured into one parseable line per value, a larger edit | 3021–3024 |
| **N8** (sketch-review item) | **Kept PENDING.** The item now states that *Proof reviews* quotes both verdicts with their sha256s. It is discharged only when both review files, `review/proofs/REVIEW-LEMMA-P.md` and `REVIEW-CONE.md`, are on `main`, with precondition 3's paper records or in the record directory, because CC-NAT's gating rests on Lemma P's verdict (§A.42 items 2 and 8). Which of the two homes is used is left to the coordinator and owner | 1603–1607 |
| **N9** (status bullet) | The r14a bullet now says that R1–R8 cover r14's choices **and** the defaults r14a added where r14 was silent (R3's SF-2 part, R7 and R8) | 4–13 |
| **N10** (typography) | The review's "line 63" matches no 130-character line in r14a; line 63 is a code fence. The 130-character line that r14a introduced is 471 (D21's rows sentence), and it is re-wrapped (now 478–479). The broken wrap at r14a 3167–3168 (M-RAY) is re-wrapped (3267–3268). The edit-log intro, which r14a lengthened to 303 characters and which r14b edits, is re-wrapped too | 478–479; 3267–3268; 1786–1790 |
| **N11** (`derive-run` "at `E`") | One wording throughout: `derive-run` reads S1's archive "run on S1's run before `E` is committed". Applied to rule (g)'s template list, to edit row 82 (its "becomes" cell and its tag, as r14a did for row 73) and to C.8 item 7 | 2810–2811; row 82 (1875); 3170–3171 |
| **N12** (provenance) | The QC22 Inputs row also cites Q-C2-2 r14 (`9e3ef0c9…`) as the source of the wording of edit rows 92–99, 101 and 105. It is provenance only (§A.42 item 8): no claim uses its content | 659 |
| **N13** (UPR-BC) | **Option taken: owner ruling R9**, unbackticked PENDING, with its draft default and alternative. Default: no label when the completion is `out_of_scope` or `undecided`; L-UPRIME is not reclassified; the completion's status is printed. Alternative: label it as a benchmark result, with the status printed. Not decided. Labelled where UPR-BC is defined (810–812), in its control row (now with a third synthetic case, 1273) and in its invariant row (1554). IMPL D25 implements the default and the third case | 1675–1681; 810–812; 1273; 1554 |

## 3. IMPL items (`IMPL-DELTA-r14b.md`; read-only against `wt-impl` `d87547a4a`)

| finding | change |
| --- | --- |
| **I1** | D20 adds `"issues/comments/{DEC}"` to `GH_TEMPLATES` (line 90 confirmed: no comment template) |
| **I2** | D16 corrected: lines 3316–3342 are in `fixture_section` (3288 ff.), not `assemble_decisive`. It now states what is missing: `s_decide_effect_facet` discards its certificate (`verdict, _ = s_step4(…)`, line 665, confirmed), it uses a fresh `Budget()`, and no verifier with the roles exchanged exists |
| **I3** | D2 corrected: the `C-CERT` in `b_red` at 3201 is the fixture section's (`fx["controls"]`, confirmed). The decisive-mode C-CERT over B-P and the reported-only fragments does not yet exist, and D2 now requires it |
| **I4** | D17 corrected to the review's AST count: 38 `set`/`frozenset` calls, 4 set displays and 6 set comprehensions (`review/probes-r14a/script_facts.out`; not re-counted here). **DISPOSITIONS-r14a §3's "26 `set(` calls" is wrong for the same reason.** That file is kept unchanged as a record, and this line is the correction |
| **I5** | New D27: `INPUTS` (52–66, confirmed) lacks QA, FB, M2D, MI-R, SUB, RCH and DSN, and maps `tools/v3_verifier.py` to `None`. D27 states what DS needs |

Part E also adds D21 (the `verdict` entry condition), D22 (`e-entry`), D23 (R8's default), D24 (R1's floor as one
constant), D25 (R9), D26 (N11 wording) and D28 (the text-only items).

## 4. Changes not traced directly to a finding; noticed, not changed

**Changes not traced directly to a finding:**
- the r14b status bullet and the title (housekeeping);
- the row-range sentences in the edit-log intro and the C.8 intro, which now include rows 99–108;
- the re-wraps of paragraphs whose lines grew past 120 characters through the labels (whitespace only).

**Noticed, not changed:**
- C.5 rule (h) says that the inputs pin the blob of `tools/v3_verifier.py`. *Inputs* has no row for it:
  precondition 1 gives its sha256 at `fd539e15`, and the frozen expectation cites it at `2cd49dc0`. This is
  pre-existing and is noted with I5 (IMPL D27). Whether to add a row is for the next review.
- "Remark R1" in *Proof reviews* (`DESIGN-DS.md` §6) shares its label with owner ruling R1. The two are
  unrelated, and the text keeps them distinct by context.

## 5. Refusals

- **N10's "line 63".** No change was made at line 63, which is a code fence. The line meant was taken to be 471 (§2).
- **Owner choices: none decided.** R1–R9 stay unbackticked PENDING, each with a draft default and a self-contained
  alternative. No value of `S_max`, of any cap, budget or pin, or of `T0` is entered.

## 6. Owner rulings, precondition 2 (1613–1681)

Each ruling is PENDING. Its draft default and its alternative are stated in full in the file. They are summarized in
the coordinator's report.
