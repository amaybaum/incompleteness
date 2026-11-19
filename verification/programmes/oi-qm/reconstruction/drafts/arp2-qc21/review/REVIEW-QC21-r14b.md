# Independent preparation review: Q-C2-1 r14b (ARP-2-QC21)

**Verdict: REVISE (minor).** r14b fixes R14A-B1 as the r14a review scoped it, and N1–N13 and I1–I5 are fixed or soundly
disposed of. There are three blockers, each small:
- **R14B-B1.** The port of Q-C2-2's R13-B4 is still incomplete. `F`'s designation is never read, so the frozen check
  "`F`'s designation precedes the first execution run" cannot be implemented. This part of R13-B4 was missed in r14a,
  and the r14a review missed it too.
- **R14B-B2.** R1's lowering rule leaves no admissible value after a red design run below `10^5`.
- **R14B-B3.** R2's alternative cannot be implemented as written: when A3 exits 3, every later step of job A is
  skipped.

The coordinator's A3b `always()` input applies to r14b. It is reported as N1, and fixing it is part of B3's fix.

R1 and R2 need the changes below before they go to the owner. R3–R9 are ready as written; N5 is optional wording for
the owner's sheet.

**Authority.** #1169 c.6740078002 (amaybaum, OWNER, 2026-11-09T12:29:10Z) authorizes r14, the script updates,
ordinary non-scientific self-tests and independent preparation review. It does not authorize the design run, the gate
tests, `F`, dispatch or any scientific computation.

**What this review did.**
- It ran no LP, no stress test, no script self-test and no computation on any round instance.
- Its probes are text, integer and read-only `git` checks.
- It made no repo, git or GitHub writes, and changed no Q-C2-2 file.
- Its only writes are this file and `review/probes-r14b/`.

## Inputs (verified)

| file | sha256 | check |
| --- | --- | --- |
| r14b `preregistration.draft.md` | `57053e08a18f3357b86ea3956e88bbb1fb7a34c1d14fbd6b169ebbff8d1b65e1` | matches the brief |
| r14a `r14a/preregistration.draft.md` | `1dd595d30eafb65dce341b1c6306ef85b4876ce008f5e45639f893247daad708` | matches |
| `DISPOSITIONS-r14b.md` | `1703425b0307d1ff0c857f465911c1cebc5caa126637984af78979728c618d4e` | matches |
| `IMPL-DELTA-r14b.md` | `9489f79037996ab2341316673d02bece089a4753201b6576439b51f3eda7f5d2` | matches |
| `review/REVIEW-QC21-r14a.md` | `f30841bafd9742c93785bc153b75e5bca2ef1b0e1bc0714d0f535c7e10cfb3c3` | matches |
| Q-C2-2 r14, `../qc22/r14/preregistration.draft.md` | `9e3ef0c9ddea2876…` | the revision r14b cites |

**Q-C2-2's file has moved on.** `../qc22/preregistration.draft.md` now holds Q-C2-2 r14a (`d751a127…`, written at
14:09, after r14b's build at 14:06). The comparisons below use the r14 copy in `../qc22/r14/`, which is the one r14b
cites. Q-C2-2 r14a was read only for N1.

**The build reproduces.**
- `r14bwork/make_r14b.py`, with its output redirected, applies 56 edits.
- Its output is byte-identical to r14b (`probes-r14b/rebuild-r14b.md`, `57053e08…`).
- A fresh `diff -u` equals `r14bwork/r14a-r14b.diff` (`cde9e029…`).
- `r14bwork/check_rows.py` reports every fragment found for rows 82 and 99–108, in r14a for the copied text and in
  r14b for the "becomes" text.

**The V3 blocks are unchanged.** The `v3-round` and `v3-governed-paths` blocks are byte-identical in r14, r14a and
r14b (`probes-r14b/v3_blocks.out`).

**Control P.**
- The r14a probe's re-implementation of `pending_unbackticked` catches 35 lines on r14b
  (`probes-r14b/control_p_coverage_r14b.out`):
  - r14a's 31 lines;
  - DSN's pin (661);
  - the D18 and D14 items (1601–1602);
  - R9 (1675).
- The 9 lines it skips only name the word: 12, 17, 61, 62, 559, 1569, 1690, 2336 and 2869.
- No pre-`F` placeholder was found without an unbackticked PENDING. Checked:
  - the anchors, `T0`, the digest date and the stress pin;
  - the design-run and gate-test pins;
  - `S_max`, the caps and the budgets;
  - the blobs;
  - RCH and DSN;
  - the owner commitments and R1–R9.
- Precondition 3 (the paper records on `main`) is a process step, and its pins are the PENDING RCH and DSN rows.

## Blockers

**R14B-B1. R13-B4 is still only partly ported: `F`'s designation is never read.**

*What Q-C2-2 r14's R13-B4 contains.*
- The template `issues/comments/{DEC}` (its 1113).
- The approval-comment read (1494) and the `verdict` condition (1644).
- The `order.json` rule (1538–1541): "The owner's designation comment is read through `GET issues/comments/{DEC}`,
  its id given as an argument; its `created_at`, and its `updated_at` under the edited-comment rule, precede the first
  execution run's `created_at`. `order.json` records its id, author and times."
- `F`'s designation comment id among the `a_ok` arguments (1006).
- The APPROVALS self-test control, which includes "an `F` designation comment that follows the first execution run"
  (691–694).
- The invariant row "designations and approvals precede what they govern" (1741).

*What r14b ported.* The template and the approval reads.

*What r14b lacks.*
- Its `order.json` rule (2384) still reads only "`F`'s designation precedes the first execution run".
- C.8 item 9's comment-id arguments (3192–3193) name the designation of `E` and the R8 ratification, not `F`'s
  designation.
- Rule (g)'s template note says the comment template is read "by `verdict` and `e-entry`", not by `order`.
- The invariant row at 3617 names "`F` designated before the first execution run (`order.json`)" as the checkpoint
  for "fixed before any decisive computation". Nothing can measure it, which §A.41 forbids.
- No frozen control covers the approval logic. The approval self-tests exist only in IMPL D20, D21 and D23.

*Fix.* Add edit rows that port Q-C2-2 r14's 1538–1541 wording into C.3's `order.json` bullet. Then:
- add `F`'s designation comment id to C.8 item 9's arguments;
- add `order` to the template's "read by" note;
- freeze an APPROVALS-style control (Q-C2-2's 691–694) that also covers the `E` entry, `e-entry` ≡ `verdict` and
  R8's cases;
- name it in the invariant row;
- add the matching item to IMPL D20 or D21.

**R14B-B2. R1's lowering rule leaves no admissible value after a red run below `10^5`.**

*The two wordings disagree.*
- C.8 item 2 (3104–3106): "The owner may then fix a smaller `S_max` …, at least `10^5` unless the red run's `S_max`
  was `10^5`."
- Precondition 2's R1 (1617–1621): "the owner fixes a smaller `S_max` …: at least `10^5` if the red run's `S_max` was
  above `10^5`; if it was `10^5`, a smaller positive integer …".

*The failing case.* After a first red run at `10^5`, the floor is removed and, say, `5·10^4` is fixed. If that run is
red too:
- C.8 item 2 then requires a value that is at least `10^5` and smaller than `5·10^4`. No such value exists.
- Precondition 2 does not state this case.

`probes-r14b/r1_admissible.out` shows both. Two further points:
- **The verb differs.** Precondition 2 says "fixes", which makes lowering mandatory. C.8 item 2 says "may".
- **Mandatory lowering has problems.** With a strictly smaller value required:
  - a red run at `S_max = 1` leaves nothing admissible;
  - a design run that is red for a reason other than A5's timeout still forces a lower `S_max`.

  R1's alternative ("lowered by a recorded decision after a red design run") has the same wording.

*Fix, in both places and in the alternative.*
- "After a red design run, the owner may fix a positive `S_max` no larger than the red run's, by a recorded decision
  before another design run."
- "It is at least `10^5` unless the red run's `S_max` was at most `10^5`, in which case the same decision removes
  the floor."

**R14B-B3. R2's alternative cannot be implemented as written.**

*What the alternative says.* A3 exits 3 on a red fixture-mode control (C.1's fixture exit rule). The alternative
reads that exit as "neither a checker outcome … nor a failed `verdict` condition (job A's steps)".

*Why it fails.* C.2 says "No step continues on error, masks a status …" (2227), and no step after A3 has an `if:`
other than A10's `hashFiles` condition. Under GitHub's default `success()` gating, an exit 3 at A3 therefore causes
all of these:
- A3b, A4 and A5–A10 are skipped;
- job A's conclusion is `failure`;
- the aggregate's `test "${ARP2QC21_RESULT}" = success` fails;
- `verdict`'s conditions can never hold: every job `success`, A7 and A10 `success`, and the run's own conclusion
  `success`;
- the stress pin is never compared at S1 or `E`.

The S1 and `E` pushes to the round branch are also non-dispatch, checker-bearing attempts. Their A3b would be
`skipped`, so the no-unapproved-F1 rule would void the round anyway (N1).

*Fix.* The alternative must state a workflow-level change. Two forms would work:
- `if: ${{ always() }}` on A3b (as N1), and either `always()` on A4–A10 or a reading under which A3 exits 0 in that
  case and records the red control in its output;
- matching readings of the aggregate line, C.6's S1 and `E` lines, and `verdict`'s job-A condition.

Either form changes the frozen splice and control W's expectations, so it must be written into the alternative.
Otherwise the owner would be choosing between an implementable default and an alternative that cannot be implemented.

## Nits (one line each)

- **N1 (A3b `always()`; the coordinator's input).** It applies to r14b. A3b (2168–2170) has no `if:`. C.8 item 7
  (3172–3173) makes "an attempt … whose A3 fails, so that A3b is `skipped`" a violation. So a benign red A3 on any
  recorded-branch, non-dispatch attempt after `T0` voids the round: a fixture mismatch with complete fixture-mode
  output, on the dev branch or on the S1 or `E` push. Port Q-C2-2 r14a's N10:
  - A3b gets `if: ${{ always() }}`;
  - the rule sentence becomes "A3b not `success` because A3's output is missing or not fixture mode";
  - M-GUARD and control W gain the variant "the marker A3b, or its `if:`";
  - the C.2 *Common* sentence is reconciled.

  The rule fails closed, so this is a liveness trap, not a soundness hole. It must be fixed before `F`, and B3's fix
  needs it.
- **N2 (rule (h) and `v3_verifier.py`, D27).** The writer's note is right, and the gap is a §A.41 gap: rule (h)
  asserts "whose blob the inputs pin", but no Inputs row gives the pin and no checkpoint measures it.
  - The two citations agree. The blob is `681c673734427cb9f316feee09b7c5ffba348004` at `2cd49dc0`, at `D`
    (`fd539e15`) and on current `main`, and its sha256 is `fc6545f5…`, as precondition 1 states
    (`probes-r14b/v3_verifier_blob.out`).
  - Add an Inputs row for that blob at `D`.
  - Have DS, or control T before its process start, check the working-tree file's blob id against it at `F`, S1 and
    `E`.
  - Have D27 set `INPUTS` to it rather than keep `None`.
  - No owner decision is needed. Fix it in the next revision, not "the next review".
- **N3 (credential table, R8).** The third column of row 1501 still reads "It rests on the owner's direct act at the
  designation". Under R8's default it also rests on the ratification comment, so add "and, under R8's default, at the
  ratification".
- **N4 (IMPL D20 and D23 against the text).** D23's self-test "edited ratification ⇒ VOID" and D20's check of the
  designation's and the ratification's `created_at` and `updated_at` have no frozen rule. R8's default checks only
  authorship and the quoted sha256, and the designation of `E` has no time condition. Either state the rule (for
  example, unedited, or `updated_at` before `verdict`'s capture) in R8's default and in C.3, or drop it from IMPL.
- **N5 (R8, for the owner's sheet).** Both options rest on a comment under the owner's identity, which the
  credential table already counts as not independent of the session's credential. The choice is one of procedure,
  not of assurance: the default costs one more owner act, and the alternative folds the act into the designation.
- **N6 (`run_class_*`).** Rule (g)'s closing bullet (2827–2829) and C.8 item 8 say `run_class_*` functions are those
  "which `derive-run`, `order` and `verdict` call". `e-entry` calls them too (D22). Add it.
  - The implemented rule (`controls.py` 558–567) constrains only where the `"workflow_dispatch"` string appears, so
    nothing breaks.
- **N7 (R3 with R5).** R3's alternative says each reported-only fragment is "still under the general caps and
  budget". Under R5's alternative they take B-P's caps. Write "under its caps and budget (R5)".
- **N8 (record only).** DISPOSITIONS-r14b's reason for writing "every approval entry committed at `E`" in C.3 does not
  hold literally: copied C.5 already says `approvals.json` (2712), and C.3's heading says "approvals". The meaning is
  the same and the wording is harmless. No change.
- **N9 (input for r14c).** Q-C2-2 r14a (`d751a127…`) has shared-method changes that postdate r14b. Its N10 is N1
  above. Its §7 also flags a possible §A.42 item 8 question for Q-C2-1's R8 ratification and final-capture records.
  Trace these when r14c is drafted.

## Scope item 1: R14A-B1, N1–N13 and I1–I5

**R14A-B1. Fixed as scoped, but see B1.**
- **The comment template.** Rule (g) has `issues/comments/{DEC}` (2812–2813), in the right REST form under
  `repos/amaybaum/incompleteness/`. C.3 reads every approval comment through it (2357). D20 adds it to
  `GH_TEMPLATES` under the f-string rule.
- **The `E`-entry `verdict` condition** (2486–2488): "every approval entry holds, the `E` dispatch's included". Each
  entry is checked as *Approval entries* states, and `E`'s entry is built from the `E` approval comment's id. This
  matches Q-C2-2 r14's 1644. The checks it inherits are author, association, order, the edited-comment rule, no reuse
  and the binding. Every field of the entry is fixed once the `E` run exists, so `e-entry`'s sha256 and `verdict`'s
  agree.
- **The `e-entry` mode** (row 100; C.8 item 9; D22). It builds the entry with `verdict`'s function, prints canonical
  JSON and its sha256, prints no `VERDICT` line and decides nothing.
  - Its arguments `<E>` (HEX40) and `<comment id>` (DEC) are `a_ok` patterns.
  - Rules (e)–(g) admit it.
  - It runs before `verdict`'s capture and attests nothing, and `verdict` rebuilds the entry, so it adds no trust.
  - Only N6's description needs updating.
- **The R8 sites.** Every site that states the ratification is labelled: 1395–1396, 1431–1432, 1486, 1501,
  1506–1508, 1555, 2362–2363, 2482–2485, 3193, 3196–3204 and 3630. Row 29 (1822) is a historical edit-log row,
  superseded by row 103.

**N1–N13.**
- **N1, N2, N3, N6, N9, N10, N11, N12.** Correct.
  - N2 adds labels at the listed sites and at R5's seven extra sites.
  - N10's reading of "line 63" as 471 is right.
- **N4.** Partly fixed. See B2.
- **N5.** Fixed:
  - R4's alternative is self-contained, and `W_RO` matches the left side;
  - R5's alternative gives the left side `σ(1204·W_max^BP + 2W_fix + W_stress) + t_810`, which is consistent;
  - R6's and R7's alternatives are implementable.

  R2's alternative is still not implementable (B3).
- **N7.** Accepted: the checker's constants govern. It is stated at 3021–3024.
- **N8.** Correctly kept PENDING, and the discharge condition is right under §A.42 items 2 and 8.
- **N13.** R9 added (below).

**I1–I5.**
- **I1–I4.** Correct. D2, D16 and D17 now state what is missing.
- **I5.** Recorded as D27. See N2.

## Scope item 2: owner rulings R1–R9

**Status.** All nine are unbackticked PENDING items of precondition 2 (1613, 1624, 1631, 1640, 1647, 1653, 1658,
1665 and 1675). Control P and precondition 6 block `F` on each.

**Labels.** Every site that carries a default is labelled. Checked:
- R1 at 1571, 3056 and 3105;
- R2 at rows 104, 107 and 108;
- R3 at 1926 and 3091;
- R5 at 395, 434, 1078, 1109, 1377, 3016, 3228 and 1926;
- R6 at 1485, 1496 and row 106;
- R7 at 3091–3093;
- R8 as above;
- R9 at 810–812, 1273 and 1554.

At 1116, 551 and 3230, R9's reading does not change the text.

| ruling | self-contained | default implementable | alternative implementable | ready for the owner |
| --- | --- | --- | --- | --- |
| R1 | yes | no after a red run below `10^5` (B2) | same defect (B2) | after B2 |
| R2 | yes | yes | **no** (B3) | after B3 (needs N1) |
| R3 | yes | yes | yes (N7 wording) | yes |
| R4 | yes | yes | yes | yes |
| R5 | yes | yes | yes | yes |
| R6 | yes | yes | yes. It accepts that a deliberate deletion cannot be told from expiry; B6's replay still binds the measurements | yes |
| R7 | yes | yes | yes | yes |
| R8 | yes | yes (N4 on edits) | yes | yes (N5 for the sheet) |
| R9 | yes | yes (D25 and the third UPR-BC case) | yes | yes |

**R9.**
- **Default.** No label, no reclassification of L-UPRIME, and the result printed with the completion's status.
- **Alternative.** Imported for B-C, printed as a benchmark with the status.
- **Both.** Each is mechanical and changes no Level (D17(a)). This is a legitimate scope question, since reclassifying
  on an unresolved completion would read absence of evidence as evidence.

## Scope item 3: a re-read of changed sections and of sections that read a ruling

- **New errors.** B1 (pre-existing, but inside the R13-B4 port that r14b set out to complete), B2, B3, N3, N4, N6 and
  N7. Otherwise the added text is consistent, in a neutral register, and within 120 characters a line outside tables.
- **The build.** It reproduces byte for byte, and the V3 blocks are unchanged (above).
- **Control P.** It catches every pre-`F` placeholder (above).
- **The cap-value bullet** (3021–3024) and the `S_max` check bullet (3055–3058) agree with SG-2 (557–563) and
  invariant 1571.

## Scope item 4: rule (h) and `v3_verifier.py`

See N2. The note's facts are right, and the gap is real.
- **Severity.** It is pre-existing, and nothing reads the unpinned file to reach a verdict except control T, which
  runs the verifier from the tree. Under §A.41, either the pin is given a checkpoint or "whose blob the inputs pin"
  is not asserted.
- **Cost.** One Inputs row, one DS or T check and D27. The blob is already established.

## Scope item 5: authorization

Nothing in r14b implies authorization of the design run, the gate tests, `F` or computation:
- the authority block (361–386) is unchanged from r14a;
- precondition 7 says "c.6740078002 authorizes none of them";
- `e-entry` and the R8 ratification are post-`E` acts, under rulings still pending.

## Probes (`review/probes-r14b/`)

| file | sha256 | what |
| --- | --- | --- |
| `rebuild-r14b.md` | `57053e08…` | `make_r14b.py`'s output, redirected; byte-identical to r14b |
| `r14a-r14b.fresh.diff` | `cde9e029…` | fresh diff; identical to `r14bwork/r14a-r14b.diff` |
| `v3_blocks.py` / `.out` | `6b6e4f39…` / `c461d3d0…` | the V3 blocks are unchanged (r14a and r14 against r14b) |
| `control_p_coverage.py` / `control_p_coverage_r14b.out` | `fc3f8b2f…` / `a908d18f…` | control P's rule on r14b: 35 caught, 9 that only name the word |
| `r1_admissible.py` / `.out` | `c778bd3d…` / `acbcdcc8…` | R1's two wordings over red runs at `2·10^5`, `10^5 + 1`, `10^5`, `5·10^4` and `1` (integers only) |
| `sites_r14b.out` | `937c7a87…` | the cited lines for B1, B3, N1, N2 and N3 |
| `v3_verifier_blob.out` | `c2eedb01…` | `tools/v3_verifier.py`'s blob at `2cd49dc0`, `fd539e15` and `origin/main`, and its sha256 (read-only `git`) |
