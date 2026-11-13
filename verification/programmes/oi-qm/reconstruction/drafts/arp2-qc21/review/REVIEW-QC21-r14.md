# Independent preparation review: Q-C2-1 r14 (ARP-2-QC21)

**Verdict: REVISE (minor).** Two blockers and a set of nits. Both blockers can be fixed in a few lines and do not
reopen any owner decision.

**Authority.** #1169 c.6740078002 (amaybaum, OWNER, 2026-11-09T12:29:10Z) authorizes "r14, bringing the scripts up to
date, ordinary non-scientific self-tests, and independent preparation review". It does not authorize the design run,
the gate tests, `F` or dispatch, or any scientific computation. This review ran no LP, no stress test and no script
self-test. It made no repo, git or GitHub writes.

## Inputs (verified)

| file | sha256 | check |
| --- | --- | --- |
| r14 `preregistration.draft.md` | `ae6f0e26e3eefc5060dddd8b7fc8a3a4958f689cf99bcc699c18821225b477fd` | matches the brief |
| r13a `r13a/preregistration.draft.md` | `fefd3b6e1da1f3705421b542dadd3086a76ac5d9a1e32343641d5f37e84f3945` | matches |
| `DISPOSITIONS-r14.md` | `11a1e8781e43c53a14bf1928f6922c5de258a285ac10afc7bb44f3150cf80317` | matches |
| `IMPL-DELTA-r14.md` | `0fb8860943bc8960ea3919e3de254ff2a78dd6ef252285d0d8b36fb9e7aa1da1` | matches |
| `review/REVIEW-QC21-r13a.md` | `7a9aea15bb28c36c18efb755c0f0c420a6b14f16c3a1cd71644c7c20f6677184` | matches |
| `wt-impl` `qc21_check.py` / `controls.py` | `1f928334…` / `ce343d6f…` at `d87547a4a` (local, unpushed) | match IMPL-DELTA |

- **The build reproduces.** `r14work/make_r14.py`, redirected to `probes-r14/rebuild-r14.md`, applies 69 counted
  edits to r13a. Its output is byte-identical to r14 (`ae6f0e26…`).
- **The supplied diff is stale.** `r14work/r13a-r14.diff` (12:49:53) predates the final build (12:51:48). It lacks
  four passages that r14 contains: ST-BP's *Its record* bullet, the removal-order verifier text, C.7's "every stress
  fixture that is decided" sentence and the L-RING row. It also lacks the hunk offsets and re-wraps that follow from
  them. This review read r14 itself and a fresh diff.
- **Owner text.** The quotations of c.6740078002 and c.6737336374 match the comments as fetched through `gh api`.
- **Scope of the reading.** The whole of r14 was read. Appendices A, B and C.1 were read for the passages that r14's
  readings govern. Each changed section was read in full.

## Blockers

**R14-B1. SG-2's named checkpoint "Control P refuses `F` while any is `PENDING`" does not apply to r14's new fields.**
- **The rule.** Control P (C.5: "no unbackticked `PENDING` under `--freeze`"; `controls.py` `pending_unbackticked`)
  ignores backticked occurrences.
- **The new fields.** Every placeholder that r14 adds is backticked:
  - `S_max` (C.8 item 2; C.7; precondition 2's new item);
  - B-P's three caps and its budget triple (C.8 item 1);
  - the D19 (i)(a) values (line 418).
- **The probe.** `probes-r14/control_p_coverage.py`, a text check, finds 31 lines that carry `PENDING`. Control P
  catches 6 of them, and none of r14's.
- **What does work.** `check --freeze` does recompute the caps and budgets against the pinned checker. Nothing
  mechanical, though, checks `S_max`, or the file's own statement of the caps.
- **A pre-existing contradiction.** Line 2198 says that the stress pin is "an unbackticked `PENDING` field". At 2789 it
  is written backticked.
- **Fix:**
  - write r14's placeholders unbackticked, as the anchors and blobs are, or widen control P by an edit row;
  - have `check --freeze` require that the `S_max` recorded in `stress.json` equals the checker's constant and the
    value recorded in the file.
- **The same defect elsewhere.** The other backticked placeholders inherited from r13a have the same problem: the
  sketch-review item at 1565, the owner commitments, `T0`, the pins and the benchmark at 1353. The same fix covers
  them.

**R14-B2. r14 makes VOID-level and scope choices itself, which its own invariant reserves to the owner, with no
`PENDING` marker.**
- **The invariant.** "Scope choices and the level of a VOID are the owner's." Its checkpoint is "D19 to D23 recorded".
- **The choices r14 makes.**
  - C.8 item 14, the *Stop rule*, D21's provenance list and edit row 84 make a red fixture-mode control at S1 or `E`
    a round-level VOID.
  - D19 (b)'s adopted option text reads "A red control … voids its own test's token".
- **Where they are flagged.** `DISPOSITIONS` §6 marks these for an owner ruling (B, and also C and D). The file
  itself freezes them as rules, so nothing blocks `F` if no ruling is ever recorded.
- **Fix:**
  - add the open rulings to precondition 2 as unbackticked `PENDING` items: §6 B, and §6 C with the interaction in
    N5 below;
  - or have the owner rule before the design run and quote the ruling.

## Nits (one line each)

- **N1.** Regenerate `r13a-r14.diff` from the final build (see above). DISPOSITIONS' line references match r14.
- **N2.** C-CERT under D21 (b): say, as C-BUDGET does, that an undecided fragment (one given no verdict) does not
  count in `unverified`. Otherwise one failed reported-only certificate turns a B control red and gives B-VOID,
  against D19 (ii)(b), (iii)(c) and C.8 item 13.
- **N3.** `verdict` (C.3) still prints "`VERDICT <token>` … otherwise `VERDICT VOID`":
  - define the token line under test-level VOID: P, B and C tokens, VOID ones included, and the Level;
  - reserve `VERDICT VOID` for round-level failures;
  - let C.8 item 14 also govern C.1's "(0 when complete and green, 3 otherwise)".
- **N4.** B-RAY exercises removal only under step 2 (feasible) and step 4 (infeasible):
  - add a feasible step-3 or step-4 case with a removed row, for example B-S4F plus the mixture of two point laws;
  - state that a feasible model's `μ_p` covers the removed rows, through `g_j · a_p` or `Σ λ_q μ_q`;
  - state that the verifier checks reproduction on every preparation.
- **N5.** The reference-instance rule's timeout test contains `1203 · W_max`, so the volume of reported-only fragments
  can push B-P's caps down, to a smaller reference or to the copied caps. DISPOSITIONS §6 C does not mention this
  interaction. It needs an owner ruling on priority (see writer's point 3).
- **N6.** REP-INV and the count 1203: state whether an alternative whose B-P or B-C table differs beyond relabelling
  is re-decided, under which caps and budget and counted in the timeout test, or is read as a change without being
  decided.
- **N7.** D22 and SG-4 say "no ADA status rule reads" `bp_equals_qmp`. C-IFACE's rule and its mutation cover only
  `decide-*` and `decide-levels`. Extend them to the ADA status functions, or drop the claim (§A.41).
- **N8.** The failure rule's "ST-BP has shown that B-P cannot be decided … at its worst case" overstates the result.
  The SF-1 instances are random synthetic fragments, not B-P's worst case. State what was measured.
- **N9.** Require `S_max ≥ 10^5`; otherwise ST-BP cannot raise the binomial cap. Record the value in the file as well
  as in the checker (B1).
- **N10.** Add a mechanical guard so that ST-BP cannot run before the design run is authorized:
  - `--stress` refuses while `S_MAX` is unset;
  - no tree carrying the splice is pushed before that authorization;
  - the script self-tests of the cap rule use synthetic `stress.json` records, never SF-1.
- **N11.** The S1 binding reads "B5's frozen name", but r14 states no artifact names. The scripts' splice uses
  `arp2-qc21-<…>`. State the names of A4, A6 and B5 in C.2; `upload-artifact@v4` needs distinct names within a run.
- **N12.** C.6's list of post-`F` changes should name `S_max` and `P_max^BP`, `B_max^BP`, `W_max^BP`, since SG-1 says
  that C.6 covers them.
- **N13.** D21 and SG-3 file "a crash or a timeout" under "provenance".
  - These are round-level halts adopted with D21: r13a listed them under either option.
  - A crash in C's code is still a failure in C that erases P.
  - Label them as incomplete-output halts, so that the owner sees this exception to SG-3's first clause.
- **N14.** Say whether the general caps apply to SF-2 in `--stress`. C.8 item 1 names "every fixture" but not the
  stress fixtures. SF-2 has up to 91 preparations, so it can exceed 16 rays and `C(n, 3) ≤ 10^5`, and `stress-check`
  requires every fragment that is not `over_maximum` to be verified.
- **N15.** §A.41: D23's invariant row names the field, not a check. Name the self-test case: a synthetic ABL-SA1b
  record with `common` false and `added` non-empty (IMPL-DELTA B8).
- **N16.** The timeout test charges B-P's facet enumeration only implicitly, through `t_5`. That works because ST-BP
  runs in A5 and `σ·(2W_fix + W_stress) ≥ t_5`. The per-subset cost when B-P's `d`, which can reach
  `max(16, d_ref)`, exceeds `d_ref` is not charged. State this residual or close it.
- **N17.** A pre-existing gap that matters for SG-2 and SG-3:
  - job B's time for P, C, REP-INV and the diagnostics has no term in the timeout test;
  - "The benchmark is `PENDING`" (*Runtime*) is undefined;
  - a job-B timeout voids P's result.
- **N18.** Typography and records:
  - C.8 item 7 has a trailing space and a broken wrap at "The S1 binding ";
  - IMPL-DELTA gives `stress_output` at 1401; it is at 3401;
  - DISPOSITIONS §5 item 6 says "32 distinct laws" means "32 rows". It does not: two distinct cosets can agree on every
    effect of `Acc(B-P)` (`probes-r14/generic_rows.py`). r14's own text claims only distinct laws, and records
    `n_distinct`.
- **N19.** Retention and §A.42 item 8:
  - record the S1 binding's inputs in a structured file at `E`: artifact id, `digest`, run id, `head_sha` and member
    list;
  - classify S1's artifact as support at capture and provenance after its 90-day expiry; the enduring support is
    `E`'s committed file and `E`'s re-runnable workflow run (§A.42 item 7).
- **N20.** B-CONTEXTUAL's report names "the first restoring completion". Under the general caps a completion can be
  `out_of_scope`. Give the note's wording for that case.
- **N21 (process; not r14 content).** r1–r14 and the script commits are in session-local working files or local and unpushed, and no
  guiding PR exists (§A.43 items 1–2). Before any push, check the push-triggered workflows (N10).

## Decisions: applied as adopted, and nowhere more broadly

| decision | finding |
| --- | --- |
| D19 (0)(c) | Correct. The caps count retained rows. The reduction runs in frozen order with an exact phase-1 simplex and is budgeted. The verifier checks removals in removal order, allowing `q` "not removed before" `p`, and reverse induction shows every removed row lies in `cone(R)`, so facet enumeration over `R` is sound. `b_u · a_p = 1` makes the cone pointed. It applies to every fragment, which follows from "how the caps count". Gaps: N4 (control coverage) |
| D19 (i)(a) | Applied. B-P is whole; its caps and budget come from ST-BP by a mechanical, outcome-independent rule, are fixed before `F` and are never lowered below the copied values; a B-P over them gives B-VOID with the limitation text. `S_max` is a new owner parameter that the adopted text ("within budget") implies but does not name; DISPOSITIONS flags it. Gaps: B1, N5, N8, N9, N16 |
| D19 (ii)(b) | Correct: reported only, under the general caps, voiding nothing |
| D19 (iii)(c) | Correct: every flagged instance, reported only; "not built" is removed. Gaps: N2, N5 |
| D19 (iv)(a) | Correct and verbatim |
| D20 (b) | Correct. Depth 1 is applied to the diagnostics alone (D.2, the diagnostic forms in D.6, C-SCOPE's clause, L-RING). The decisive orbits to `K = 12` are untouched |
| D21 (b) | Applied, with the S1 binding by artifact zip. Edit rows 72–85 check out against r13a and r14 (`probes-r14/editlog_rows.py`; rows 73 and 74 use `…` notation; row 83's text survives only in the log). One reading is narrower than the option's literal text: a red fixture-mode control at S1 or `E` is round-level (B2). Gaps: N2, N3, N13 |
| D22 (a) | Correct. The map is slot 0 ↔ `X`, slot 1 ↔ `Z`; the CNOT-marker arms are used for the restricted fragment only; QM-P's P arms are unchanged; `bp_equals_qmp` gates nothing. Gap: N7 |
| D23 (c) | Correct: `{common, added}` for ABL-SA1b only; class ablations keep one boolean. Gap: N15 |
| (i)(d) | It is not selected, so no "not decided" token exists. The r13a nit is closed correctly |

**The overrides of r13a text in DISPOSITIONS §6** are all entailed by the adopted options:
- `decide-b` reads B-P alone: (ii)(b), (iii)(c) and D17(a);
- the one artifact read: D21 (b)'s adopted zip binding;
- the fragment count: (iii)(c), "every flagged instance";
- round-level VOID wording becomes test-level: D21 (b).

## Safeguards: frozen rules and checkpoints (§A.41)

| safeguard | frozen rule | checkpoint: real? |
| --- | --- | --- |
| SG-1 | yes | Real: `decide-b` step 1's 32-preparation, nine-setting check; C-IFACE's `decide-b` rule with its mutation; C-CERT, B-RAY and M-RAY. Gaps: N2 (C-CERT aggregation), N12 (C.6's list) |
| SG-2 | yes | `check --freeze`'s recomputation is real, as are M-BUDGET and the `out_of_scope` and `undecided` self-test cases. **Control P is vacuous for r14's fields (B1).** Gaps: N10, N17 |
| SG-3 | yes | Real: the `decide-levels` cases, `verdict`'s provenance cases and S1-BIND. Gap: N13 (crashes) |
| SG-4 | yes | Real: REP-INV, REP-PLANT and C-IFACE's `bp_equals_qmp` rule. The ADA claim has no check (N7). The "depth-1 label" is a label, not a measurement, but harmless: the diagnostics are unread through C-IFACE |

## ST-BP

- **What is specified.** The inputs, the procedure, the pass rule, the record, the reference rule, the failure rule
  and the timeout test are all frozen. ST-BP is synthetic and outcome-independent. No outcome narrows B-P.
- **When the caps are fixed.** Before `F` (C.7; `check --freeze`).
- **No implied early run.** Nothing in r14 suggests that ST-BP may run before an authorized design run (lines 359–362,
  precondition 7, C.8 item 2's last paragraph).
- **What is not fully specified:**
  - `S_max`'s value (owner; B1, N9);
  - whether caps apply to SF-2 (N14);
  - REP-INV re-decisions in the count (N6).

## The writer's eight points

These are recommendations, not decisions.

1. **`S_max`.**
   - **Form.** The per-enumeration subset count is sound, since it bounds both solver and verifier. It is fixed by the
     owner before the design run, from synthetic data only.
   - **Value.** Keep C.1's 1200 s / 60-min frame as the maximum time. Choose `S_max ≥ 10^5` so that A5 fits within the
     timeout test's job-A share; A5 visits up to `6 · S_max` subsets across the three SF-1 instances, solver and
     verifier together, plus SF-2 ×3 and the fixtures.
   - **Changes.** Allow only a smaller `S_max` after a red design run, as written.
   - **Recording.** Record the value in the file and check it (B1, N9).
2. **Fixture-mode controls at S1 or `E`.** Keep them round-level. They are fixed green at 6′ on the byte-identical
   tree, so a red one means nondeterminism or environment drift, which compromises every result. But this narrows
   D21 (b)'s literal text, so get an owner ruling recorded before `F` (B2).
3. **Reported-only volume.**
   - Keep the timeout test, which is P's only guard against a job-B timeout. A failure before `F` is fail-closed.
   - Ask the owner now about priority, because the volume can also lower B-P's caps (N5). The cheapest remedy, an
     aggregate work budget for reported-only fragments beyond which they are recorded `out_of_scope` and reported,
     narrows nothing that gates, but it is an SCI change like (iii)(b), and so the owner's.
4. **Raised caps for B-P only.** Accept as written. D19 (i) is B-P's part; the other fragments gate nothing, and
   raising their caps would only add timeout risk. A one-line owner confirmation is enough.
5. **Retention of 90 days.** Accept the fail-closed rule.
   - Add a timing condition: `verdict`'s capture at `E` falls before S1's artifact expires.
   - Record the binding's inputs in a structured file (N19).
   - The owner's no-deletion commitment already covers artifacts until `Q`.
6. **Overrides of r13a text.** All three are entailed by the adopted options (see above). Accept, with N6 on the
   count.
7. **The untraced changes in DISPOSITIONS §5.** Accept all fifteen, with these conditions:
   - item 1: B1 and N9;
   - item 3: N8 and N16;
   - item 4: N5 and N6;
   - item 6: the DISPOSITIONS wording (N18);
   - item 7: the soundness was checked; see N4;
   - item 8: extend it (N4);
   - item 9: N11;
   - item 13: B2.

   Items 10 to 12 are real checkpoints or direct consequences of the decisions.
8. **`DESIGN-DS.md`:260 and `PLAN.md`.**
   - DESIGN-DS lands on `main` as a paper record (precondition 3). Before it lands, restate line 260 timelessly: the
     preregistration fixes the map and arms (D22 (a)). Its "not adopted here" is still literally true but is now
     stale.
   - `PLAN.md` is a scratch drafting record that does not land. At most add a pointer to `DISPOSITIONS-r14.md`.
   - Neither blocks r14.

## IMPL-DELTA (spot-checked read-only against `wt-impl` at `d87547a4a`)

These items match the scripts:
- A1 (`replay` prints a sentence and exits 1);
- A2 (`sha256_hex` with two vectors);
- A3 (`run_entry`, `s_refusal(name)`, string `DECISIVE_BUILDERS`);
- A4 (no A3b);
- A5 (`E_FILES` without `approvals.json`);
- A6 (`--fixture-output`);
- A10 (`LEMMA_P_REVIEW = "pending"` excludes CC-NAT);
- A11 (`R12_STAB = False`);
- A12 (SF-1 is 8 laws × 4 copies with seeds mixed);
- A14 (`[:13]`);
- B1 (`all_reads` counts every read);
- B3 (`k_decide_b` reads B-C and voids on any fragment; C-BUDGET is added for any `out_of_scope`);
- B5 (`range(2)`; the old label);
- B6 (imports and templates lack `io`, `zipfile` and the zip template);
- B7 (`QM_SLOT_BASIS`);
- B8 (`OLC` merged into one boolean).

Corrections and omissions:
- `stress_output` is at line 3401, not 1401.
- IMPL-DELTA should add:
  - N2's C-CERT aggregation (`assemble_decisive` puts C-CERT in `b_red`);
  - N3's `verdict` token line;
  - N4's feasible-removal fixture;
  - N7's ADA rule;
  - N10's `--stress` refusal while `S_MAX` is `None`.

## Lifecycle and evidence rules

- **§A.39.** The draft is pre-`D` round drafting. It contains no `F`, `E` or dispatch, and the `v3-round` and
  `v3-governed-paths` blocks are unchanged.
- **Authorization.** Nothing implies authorization of the design run, the gate tests, `F` or scientific computation
  (lines 359–362; precondition 7).
- **§A.42 item 8.** The new owner records are quoted with author and time. `DISPOSITIONS-r14.md` and the probes are
  cited as provenance. N19 covers S1's artifact.
- **§A.44.** The S1 binding reads the artifacts API and the archive's JSON, and the timeout test reads step records.
  Both are structured. No log is read.
- **Register.** The added text is neutral, with no reader-instruction or self-assessment.
- **§A.43.** See N21.

## Probes (`review/probes-r14/`)

All are generic or text-only. None runs an LP, uses a round instance or runs the stress test.

| file | sha256 | what |
| --- | --- | --- |
| `make_r14_redirected.py` → `rebuild-r14.md` | `71c32576…` → `ae6f0e26…` | the r14 build, redirected; byte-identical to r14 |
| `control_p_coverage.py` / `.out` | `fc3f8b2f…` / `7a6af481…` | control P's rule applied to r14: 6 of 31 `PENDING` lines caught, none of r14's (B1) |
| `editlog_rows.py` / `.out` | `914c54ee…` / `ba741e28…` | edit rows 72–85 located in r13a and r14 |
| `generic_rows.py` / `.out` | `d9de6605…` / `2247e3b2…` | two distinct cosets on `F_2⁵` that agree on all 50 outcomes of `Acc(B-P)`; B-RAY-S and B-RAY-P each have 5 rows, 4 vertices, and the mixture with an exact `(½, ½)` certificate |
