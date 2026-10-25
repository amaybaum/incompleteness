ACCEPT WITH NITS — fb05dea83b2b61ed9ff6be189f35077426aa2037 (post-review revision of a2_memory_v8; single parent 200fcd9f9265e79167d33d20af62deb543a9a117)

Overall verdict on 1dfec979721336cc9f0ce703b544f9d6be8e906c..fb05dea83b2b61ed9ff6be189f35077426aa2037: ACCEPT WITH NITS.
- The plan is unchanged.
- The class theorem and its proof are correct.
- Every finite result I re-derived independently matches.
- The first review's F1–F6 and its nits are resolved.
- Four residual items remain: one wording overreach (R1), one control that restates the rule it checks (R2), one
  omission in the preregistration correction (R3), and one unlabelled count (R4). The deferred handoff
  propagation (R5) is still outstanding.
- None blocks.

Re-check under the same read-only rules. Files were exported with `git show fb05dea8:<path>` into `tree/`, and all
Python ran as `python3 -I -B` (3.13.16) from empty work directories. The reviewer scripts and outputs, relative to
this directory, are:
- `leafmap.py` / `leafmap.out`;
- `fd_and_lists.py` / `fd_and_lists.out`;
- `rev_mutants.py` / `rev_mutants.out`, the first-round reviewer mutants rerun;
- `rev_mutants2.py` / `rev_mutants2.out`, new double and report-level mutants;
- `../indep.out`, the first-round independent rows reused for the comparison lists.

## Changed-file inventory

- `1dfec979..fb05dea8`: 7 files added, all under `a2_memory_v8/`:
  - `PROVENANCE.json`, `REPORT.md`, `SHA256SUMS`, `checks.py`;
  - `mutants/mutants.out`, `mutants/run_mutants.py`;
  - `result.json`.
- `PLAN.md` came in at 1dfec979 and is byte-identical at fb05dea8 (b7f7eaae…a275).
- `200fcd9f..fb05dea8`: the same 7 files are modified (397 insertions, 168 deletions); `PLAN.md` is untouched.
- `49e1a119..fb05dea8`: 8 files, nothing outside `a2_memory_v8/`.

## Resolution of the first review's findings

| item | status | evidence |
| --- | --- | --- |
| F1 comparator | resolved | `nearest_dyadic(B)` with a minimality check over 2^-B Z; its exact crossings are 127, 127 and 1819. These equal my round-1 values (3/4 → 127; 13/16 → 1819), and I also computed the B=4 floor neighbour 12/16 → 127. My round-1 independent depths reproduce all 45 regenerated lists (`fd_and_lists.out`, 0 mismatches): B=2: all k fail first; B=3: k=3..15 fail first, k=2 and 16 undetermined; B=4: k=4..16 fail first, k=2 and 3 undetermined; none outlasts. RS(B,1) is renamed the ceiling-rounded reset. Reviewer mutant D4 (wrong neighbour) is caught by the minimality check. Remaining wording issue: R1 below. |
| F2 preregistration | resolved, with R3 | REPORT and PROVENANCE carry an explicit correction; PLAN.md is left as committed. The correction identifies the decoder as a bounded-state class member, describes what it showed and what it steered, and renames the key to `plan_commit`. The preregistered, post-plan and post-review lists are accurate against the diffs I reviewed. `family_verdict` is split into a "preregistered rule" part and a "post-plan" part, and post-plan fields sit under `post_plan` keys. |
| F3 power-rule controls | resolved, with R2 | Three controls were added: a least-n check; exact T(h) at k=1 against 1−BC_up^h, sqrt(1−BC_lo^{2h}) and h·T_1; and the power-rule bracket in the n·k≤16 loop. Sampling: B=2 every h≤14, B=3 every h≤266, B=4 every h≤600 plus multiples of 256 to 11,008 and n_hp±1 (644 depths). I re-derived that count (600 + 41 + 3). |
| F4 necessity/sufficiency | resolved | Both the resource statement and the REPORT section now separate necessity, non-sufficiency (v7's full-record controllers) and the one escaping sampler, and add "from a finite initial support". |
| F5 verbatim verdicts | resolved | REPORT quotes the three strings verbatim. |
| F6 proof step 3 | resolved | The strong law is applied per residue class mod n, with the Bernoulli-shift alternative. Correct. |
| F7 handoff propagation | open (R5) | Deferred to acceptance. `CURRENT-HANDOFF.md` still says "open for controllers that carry randomness across slots". |
| nits a–e | resolved | Singular system now gives VOID. The K6 string is fixed. K2/K6 counts are split 41/3. Census and K4 counts are checked in closed form. A memory-column bound is added, checked against the explicit chain sizes. PLAN computation 3 is addressed with FD as the second member. |

## Specific checks requested

**Moved values.** My own leaf mapping (`leafmap.py`) compares 939 old leaves with 1,157 new; my counting
convention differs from the author's 927/1,145 by 12 on both sides.
- 554 leaves are unchanged in place and 378 are moved and identical. Every old leaf maps, with none unmapped.
- 7 leaves changed, all expected: `class_verdict`, `family_verdict`, `resource_statement`, `schema`, the K6 and
  K7 strings, and K2 43→41 (the 2 K6 checks now counted separately as 3).
- All preregistered depth fields (`certified_T_above_half_for_h_at_least`, `…tenth…`) are unchanged in place.
- The additions are the nearest-dyadic comparators, the persistent-state counts, the nearest-dyadic before/outlast
  flags, the k=1 exact-check metadata, the FD member, `controls/counts` and `K6_retained_value_checks`.

**FD(B,m).** I re-implemented FD from the REPORT's prose, using exact rescaling and the floor of y·2^m. Stationary
laws come from cofactors of I−P (tree theorem), and χ(λ) from a determinant.
- All 15 chains and 16 classes match the author's sizes, least mismatches and exact stationary frequencies.
- FD(2,4) has an absorbing class with frequency 1 and a 15-state class with frequency exactly 4/5 that mismatches
  at n=2. Every other class mismatches at n=1.
- FD has finite state and a fixed rule, so it is a genuine class member. The B=2, m=4 exact class confirms the
  exploration's float observation described in the F2 correction.

**Power-rule sampling at B=4.**
- The sampling is adequate for what the control is: an implementation check of a textbook inequality
  (1 − TV ≤ BC, with BC multiplicative over products).
- Exhaustive h to 2·n_hp = 11,086 would cost O(h²) big-integer work and would not certify anything further.
- The k≥2 depths have no exact comparison at any sampling density.
- REPORT states the sampling honestly ("644 depths to h=11,008"). The `result.json` metadata agrees:
  `all_h_up_to=600`, `depths_checked=644`, `max_h=11008`.

**Control reordering for M3/M4.** Only the first-failure label changes; every check still runs on the unmutated
path. In `run()` the FD member now runs after the census and the base-5 control. In `base5_countercontrol` the
closed-form count check runs after the exact-match check. Neither move skips or weakens a check.

**Mutants.**
- The author's runner reproduces `mutants/mutants.out` byte for byte; M1–M14 are all caught on their labels.
- My 16 round-1 mutants all exit 2 with VOID on sensible labels (`rev_mutants.out`). R1, R4, R10 and R15 are now
  caught, as are I1 (tampered input) and R14.
- New mutants:
  - D4: the wrong neighbour is caught.
  - D1: changing the power-rule exponent consistently in both the computation and its least-n check exits 0. See
    R2.
  - D5: computing the nearest-dyadic flags against the ceiling crossing exits 0. That is report-level: replay
    catches it, and my independent list check confirms the shipped lists.

**Replay and hygiene.**
- Normal and `-O` runs from empty directories are byte-identical to `result.json` (about 3 min 05 s each).
- The mutant run, with TMPDIR inside the review directory, is byte-identical.
- `SHA256SUMS` verifies all 7 files, and `PROVENANCE.json` parses.
- No absolute paths, emails, IPs, tokens or `__pycache__`.
- `tools/duplicate_check.py`, `tools/voice_check.py` and `tools/artifact_placement_check.py` all pass.
- The clone's worktree is clean, with HEAD at fb05dea8.

## Residual findings (ranked)

**R1 (low-medium; wording overreach, post-review text).**
- REPORT calls the nearest-dyadic reset "the best memoryless B-bit law". It also says "retaining seed bits within
  blocks makes the record law worse than the best memoryless reset at the same fresh-bit rate, at every tested B".
- What is shown is narrower:
  - The comparator is the nearest-dyadic i.i.d. reset. The checker proves distance-minimality, not depth
    optimality.
  - It is best among i.i.d. B-bit laws at the tested B by the exact crossings of both neighbours: 127 against 4,
    127 against 45, and 1819 against 127. The checker compares the two neighbours at B=2,3; I computed 12/16 at
    B=4.
  - It is not compared with record-dependent or time-varying controllers in v7's memoryless class.
  - The ordering is certified only for the members listed; B=3 k=2,16 and B=4 k=2,3 are undetermined.
- Fix:
  - say "the nearest-dyadic i.i.d. reset (best i.i.d. B-bit law at these B)";
  - narrow the sentence to "for every member whose ordering is certified (all but B=3, k=2,16 and B=4, k=2,3);
    none is certified to outlast it".

**R2 (low; control independence, §A.41 / "a control must not merely reproduce the formula").**
- M11 (R1 in round 1) is caught only by `check(bh ** n_hp < HALF and …)`. That check restates the depth
  definition.
- The double mutant D1 changes the definition consistently in both places and passes every control.
- The new exact k=1 check validates the inequality with the correct `bh`, not the expression that produces the
  reported depths.
- Fix: use one function for the power-rule lower bound in both the depth search and the k=1 exact check. A
  consistent exponent error in it would then fail at B=3, where the invalid 1−BC^(2h) bound is violated by exact
  T from h=149, inside the checked range h≤266 (round-1 `pow_probe.py`).
- Alternatively, recompute n_hp independently, for example from a high-precision logarithm with exact boundary
  verification.

**R3 (low; F2 correction completeness).**
- The exploration found a class with frequency 4/5 and differing run masses. That bears directly on K5, the
  preregistered expectation that exact-frequency dyadic classes exist and mismatch at some n ≥ 2. Plausibly it also
  bears on the choice of run masses rather than frequency in the proof route.
- The correction lists what the exploration did not touch, but omits K5.
- "In the author's working record, the Cayley–Hamilton route on run masses was sketched before that run" cannot be
  verified from the repository.
- Fix: add "it may have informed K5", and label the working-record sentence as an unverifiable self-report, or
  drop it.

**R4 (nit).** The preregistered `class_verdict` string now carries post-review FD counts ("15 floor-truncated
decoder chains (16 closed classes)") without a post-review label. Label it, as was done in `family_verdict`.

**R5 (open propagation, outside this diff).** First-round F7 is still open. When the result is accepted, update the
mutable `CURRENT-HANDOFF.md` §"Depth extension" with the adopted attribution wording. Its "open for controllers that
carry randomness across slots" is now answered for bounded whole state. Leave `a2_depth_v7/` unchanged.

No new overclaim beyond R1. A1 and A2 remain separate. The theorem's scope and the open case (bounded private
memory with unbounded public state) are stated correctly. The attribution paragraph matches the wording proposed in
the first review.
