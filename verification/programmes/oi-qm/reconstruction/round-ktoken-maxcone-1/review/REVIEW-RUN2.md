# KTOKEN-MAXCONE-1 (#829): run 2 for owner review

**Where things are.** Nothing has been dispatched, and PR #829's branch is untouched.

| Branch | State |
|---|---|
| Review branch `wip/ktoken-maxcone-run2-draft` | On GitHub at `2b561a22`. This note, the revised preregistration, `controls.py` and `review/preregistration.diff` are in its follow-up commit on top of `2b561a22` |
| Run-2 tree branch `dev-equivalence/ktoken-maxcone-r2` | **Still local.** Head **`814621265a70aa301199276d4338d2c88bbd9283`** (tree `59ed73a8`), which is `1a3439c9` plus the checker fix below. This is the commit to push and dispatch for run 2. Pushing keeps the id |

The review branch is for reading, not for dispatching. It lacks the shard's `controls.py --self-test` step, which is in
the run-2 tree. Its `review/` folder would also fail the round's record control R at `E`.

The local result outputs quoted below (self-tests, the gate, the simulated chains) are kept only in the session
scratchpad. They are not in either branch, so the relevant lines are reproduced here.

## (a) What changed after run 1, and why

Run 1 was dispatch run 39043849411 on `1ab0fd9d`. The host shows conclusion success, 38 of 38 jobs green, the Mathlib
bridge's Build, Release gate and A3 steps green with `A3-CHECK-NONVACUOUS: 13 cases as expected`, and the probe shard
printing `VERDICT KTOKEN-K3-EXACT`. The module, the probe and the A3 files are unchanged: their blobs are run 1's, and
the preregistration freezes them.

The run-2 tree adds three things.
1. **`controls.py`**, the round's static controls, in the style of BG-2: `--self-test`, `check E --freeze F`, and
   `verdict E --freeze F --axioms LOG`. Its expected values come from two sources:
   - **The preregistration:**
     - the statement surface and hypotheses;
     - the S1 mutations, the S4 phrases and the four decision cells.
   - **What run 1 compiled:**
     - the compiled surface;
     - the 68 prints in order;
     - the probe's N = 3196, measured locally and byte-identical across replays; run 1 showed the probe's final lines;
     - the census family;
     - the workflow, import and census edits.

   The workflow, import and census edits were compared with `D`'s files through the splice functions: all three equal.
2. **The shard's `controls.py --self-test` step**, as in every landed native round.
3. **The revised preregistration**, re-cut at `D` = `b96662e6`:
   - every line reference re-measured, and the import of `OIBridge.EqvK2Generation`;
   - the compiled proof route: `sign_induction` with CNOT conjugation, `su_euler` branchwise, no Gray schedule;
   - Q-PAIR resting on S1's textual identity, check A3 (the W1 step) and the absence line in the build log;
   - S2 and S3 extended;
   - new controls W, I, J, C2, P, R and T;
   - the §A.42 retention rows, with two pins pending;
   - a §A.41 invariant table, now 13 rows.

   The diff against the PR's file at `625f853f` is `review/preregistration.diff`.

### The checker fix (owner review)

**The defect.** `verdict()` gated the cells only on S1–S3, so with C2 failing it still printed every positive token.
Suppressing only `READ` did not fix it.

**The fix.** Every cell token and `READ` are now gated on all thirteen required static controls: C1, C2, S1–S4, W, I,
J, P, R, G and T. If any of them fails or is unreported:
- `verdict` prints `STATIC CONTROLS FAILED: …`;
- runs no probe and reads no axiom report;
- prints every cell as `…-NOT-ESTABLISHED` and `KTOKEN-MAXCONE-1-NOT-READ`;
- exits 1.

The preregistration's decision-rule section now states this, and its invariant table carries a row for it.

**The owner's case, run through `verdict()`** (C2 failing; every other static control, the probe output and the axiom
log clean; all inputs synthetic).

Before the fix, with the `controls.py` of `1a3439c9`:
```
FAIL C2 (synthetic)
TOKEN Q-INCL  KTOKEN-MAXCONE-INCLUSIONS-PROVED
TOKEN Q-EQ    KTOKEN-MAXCONE-EQ-PROVED
TOKEN Q-PAIR  KTOKEN-MAXCONE-PAIR-RECOVERED
TOKEN Q-EXACT KTOKEN-MAXCONE-K3-EXACT
KTOKEN-MAXCONE-1-NOT-READ (a static control failed)
verdict returned False
```

After the fix, with the `controls.py` of `81462126`:
```
FAIL C2 (synthetic)
STATIC CONTROLS FAILED: C2
probe not run and axiom reports not read: a required static control failed
TOKEN Q-INCL  KTOKEN-MAXCONE-INCLUSIONS-NOT-ESTABLISHED
TOKEN Q-EQ    KTOKEN-MAXCONE-EQ-NOT-ESTABLISHED
TOKEN Q-PAIR  KTOKEN-MAXCONE-PAIR-NOT-ESTABLISHED
TOKEN Q-EXACT KTOKEN-MAXCONE-K3-NOT-ESTABLISHED
KTOKEN-MAXCONE-1-NOT-READ (static controls failed: C2)
verdict returned False
```

**The regression test, in `--self-test` and therefore in the CI shard.** It goes through `verdict()` itself, with the
static results and the probe supplied as test inputs, over 15 cases:
- each of the 13 controls failing alone;
- C2 left unreported;
- the all-clean case.

Every failing case must print none of the positive tokens (including `READ`) and return failure. The all-clean case
must print all of them.

Results:
- **Fixed `controls.py`:** 0 problems. `controls.py --self-test`: 36 PASS lines, `controls: OK (0 failure(s))`.
- **The regression test is itself mutation-tested** (scratch only). It rejects:
  - the gate removed, which is the owner's defect reintroduced (14 problems);
  - a missing control treated as passing (1 problem);
  - cells gated on S1–S3 only (11 problems).

**The simulated chain, repeated.** I built `D` → `F′` → `C1` → `S1` → `E′` locally, with a stub result note, and
deleted it afterwards.

| Variant | `check` | `verdict` |
|---|---|---|
| As drafted (pins pending) | all PASS except **P** and **R**; exit 1 | `STATIC CONTROLS FAILED: P, R`, four `…-NOT-ESTABLISHED`, `NOT-READ`, exit 1 |
| With two dummy evidence files pinned (synthetic, labelled as such; not run evidence) | all 13 PASS; exit 0 | ran the real probe blob (`checks: 3196, failures: 0`, 5 rejections, `VERDICT KTOKEN-K3-EXACT`). With a **synthetic** axiom log, it printed the four positive tokens and `READ`; exit 0 |

The positive tokens in the second variant exercise the code path only. They establish nothing about the theorem.

## (b) Each control or check, and its expected result in run 2

**How a red is handled.** A red job or step is recorded as the failed check, by name. It is diagnosed from evidence:
the job's log, and a rerun only under the repository's rules (§A.39, §A.40). Unchanged source blobs narrow where to
look, but they do not establish a cause, and no cause is assumed in advance. Run 2 is unusable for acceptance until the
failure is resolved.

| Job / step | Expected in run 2 |
|---|---|
| `kernel` | success |
| `bridge` › Build | success; the KTokenMaxCone blob is run 1's |
| `bridge` › Release gate | `release gate: PASS`, all 22 steps. Locally, on `81462126`, 21 of 22 pass; `lean-axioms` needs Lean |
| `bridge` › A3 step | success, with `A3-CHECK-NONVACUOUS: 13 cases as expected` |
| `probes_ktokenmaxcone1` › probe `--self-test` | 14 PASS codes, `checks: 3196, failures: 0`, 5/5 rejected, `VERDICT KTOKEN-K3-EXACT` |
| `probes_ktokenmaxcone1` › `controls.py --self-test` | `controls: OK (0 failure(s))`, 36 PASS lines (as locally), including the `verdict()` regression. This is the step run 2 adds |
| other probe shards, A42 shards, aggregate | success. The 15 A42 exclusion shards cost about 6 CPU-hours on dispatch |

Run 2 does not test these, which stay with the round:
- P and R, which need the retained evidence;
- S4 on a result note;
- `check` and `verdict` at the real `F` and `E`;
- `F`'s and `E`'s exact-head attestations.

## (c) Acceptance criteria for run 2 (preregistered decision rule)

**PREDICTED-TREE-GREEN** requires all of the following on the dispatch at exactly `81462126`:
1. every job concludes `success`, including the aggregate and all 15 A42 exclusion shards;
2. the gate prints `release gate: PASS`;
3. the A3 step's final line is `A3-CHECK-NONVACUOUS: 13 cases as expected`;
4. the probe step prints `VERDICT KTOKEN-K3-EXACT`, `checks: 3196, failures: 0` and
   `mutations: 5 rejected, 0 accepted`;
5. the `controls.py --self-test` step prints `controls: OK (0 failure(s))`.

Any other outcome is a failed acceptance:
- a run at another commit;
- any red, cancelled or unexpectedly skipped job;
- any missing line.

The failure is recorded and diagnosed as in (b), and run 2 is unusable for acceptance until it is resolved. The run cap
of two is reached with run 2, so any further run needs a new owner allowance.

## (d) Run 2's tree, exactly

`git diff --stat b96662e6 81462126` touches 9 files, with 4726 insertions and 1 deletion. This is the predicted
execution tree less the result note **and less the §A.42 evidence files**, which cannot be produced before the logs are
retrieved. Nothing in it is disposable.

| Path | Note |
|---|---|
| `verification/lean-mathlib/OIBridge/KTokenMaxCone.lean` | blob `14bb9fc0`, frozen |
| `verification/lean/ktoken_maxcone1_probe.py` | blob `04580c51`, frozen |
| `round-ktoken-maxcone-1/checks/KTokenPairCheck.lean` | blob `354bd7ce`, frozen |
| `round-ktoken-maxcone-1/checks/run_checks.py` | blob `dc6c77d1`, frozen |
| `round-ktoken-maxcone-1/controls.py` | blob `00a081de`, frozen |
| `round-ktoken-maxcone-1/preregistration.md` | the `F` candidate's text, pins pending |
| `.github/workflows/verify.yml` | six splices, checked by W |
| `verification/lean-mathlib/OIBridge.lean` | +1 line |
| `verification/lean-manuscript-census.json` | +1 family |

**The W1 step stays.** It is part of the round's frozen control:
- the preregistration names it (Q-PAIR rule, invariants table);
- `controls.py` W requires it, exactly as spliced, at `E`.

`if: ${{ !cancelled() }}` is frozen with it. Dropping that line is an owner choice, and must be made before run 2,
because it changes `verify.yml`, the W splice and the `controls.py` blob.

**SHA.** Run 2's head will be `814621265a70aa301199276d4338d2c88bbd9283` once pushed. The real `E` will differ, because
it is built `F` → stage 1 → stage 2 → stage 3 with the evidence files. C2, W, I and J check that `E`'s content equals
what run 2 exercises.

## (e) Owner decisions before F

1. **Approve the push of `dev-equivalence/ktoken-maxcone-r2` (`81462126`) and the run-2 dispatch.** This is the last
   design run under the cap.
2. **Retained evidence (§A.42).** The run-1 log (jobs 117428550018 and 117428550439) and the run-2 log must be turned
   into `evidence/run1-39043849411.json` and `evidence/run2.json`, and pinned by sha256 in the preregistration before
   `F`.
   - These logs can be retrieved only through the browser or the evidence-retention archiver (`reproduce evidence`
     workflow).
   - Until then the pins are pending, and `check` and `verdict` fail on P and R.
3. **Keep or drop `if: ${{ !cancelled() }}`** on the A3 step (before run 2).
4. **A drafting PR at `D` = `b96662e6`.** Open a new one, or reset PR #829's branch, which is at `D` = `dee3b5ae`.
5. **Landing order against #821–#825.** All of them splice after the same import line, census tail and aggregate lines.
   The W, I and J controls anchor on text, not on line numbers.
6. **Confirm the port scope and the scoped instance.** The port covers three modules; FiniteWalsh and FiniteCircuit
   are not ported.
7. **`F` designation:** after run 2 is accepted and the pins are filled, on `F`'s exact-head `check-run` (§A.39).
