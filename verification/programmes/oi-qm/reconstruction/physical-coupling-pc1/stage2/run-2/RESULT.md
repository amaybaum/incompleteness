# PC-1 — stage 2, run-2 (controls only): result

**Status: research-only; a separate stage-2 run.**
- **Authority.** Owner option A, PR #1022 comment 6547861508: bounded proof repairs, proof bodies
  only.
- **Frozen scope, unchanged.** PC-S2 (`4d2c4d56`) and PC-S2-C13 (`895e5c5b`): C1–C15 (C13 at row
  9), M1–M17, the 37 + 5 self-test cases, the 33 fixed kernel statements, the decision function,
  the schema and every expected value.
- **Not computed.** Nothing was computed on any candidate, and nothing was re-screened.

## Run 1 stays as it is: INCONCLUSIVE (void)

- **The run.** Commit `f14b59b2855ca4eace64df64f59fc0d434c9f0cd`; ordinary draft-PR CI run
  41231679739, job 124627021904.
- **The steps.** `Build` failed and `Release gate` was skipped.
- **The token.** `INCONCLUSIVE (void)`, with void reasons `0(vi)` (stage 1, owner Decision 1) and
  `0(v)` (kernel build).
- **Its files.** `stage2/controls.py`, `stage2/results.json` and `stage2/RESULT.md` are preserved
  unchanged. Their regeneration check still passes at this commit.
- **The cause.** The build errors were in `OIBridge/PC1Controls.lean`. `PROOF-REPAIRS.md` gives
  each defect and its repair. The run-1 version of the module is preserved at `f14b59b2`.

## Run-2 files

| File | Content |
|---|---|
| `run-2/controls.py` | A copy of `stage2/controls.py`. Its only differences are permitted ones: `UNIT = HERE.parent.parent` and `VENDOR = HERE.parent / "vendor/recursive-substates"` (path re-anchoring), and run metadata in the `run` field (`id`, `preserved_run_1`, `authority`). No freeze input, control, mutation, self-test, expected value or decision logic changes |
| `run-2/results.json` | The run's results. Normal and `-O` runs are byte-identical. Against `stage2/results.json`, the only difference is the `run` field: `script_sha256` and the three metadata entries. Every control, mutation, self-test, statement digest, kernel field, token, void reason and finding is identical |
| `run-2/PROOF-REPAIRS.md` | Each Lean change, with its line and traced defect |
| `verification/lean-mathlib/OIBridge/PC1Controls.lean` | Edited in place: proof bodies only (R1–R8) |

## Result, in two tracks (unchanged from the frozen design)

- **Strict token: `INCONCLUSIVE (void)`**, `void_reasons = ["0(vi)"]` before CI. Run-2 cannot
  remove 0(vi). A failed CI step adds `0(v)`.
- **Scientific finding**, carried only under the owner's one-time exception (PR #1022 comment
  6547077354):
  - **Statement.** No admissible candidate among the 25 screened. The obstruction is G★ item 3 for
    native couplings: A★2 premise (ii) is broken by no native source.
  - **Scope.** As PC★ §PC★4. **It is not a no-go.**
  - **Status: `pending exact-head review`.** It becomes `carried under exception` only when both
    kernel steps succeed at run-2's exact head and the independent exact-head review is recorded.
- **Not a clean result.** The unit's token is never the gap token.

**Controls, mutations and self-test: actual equals expected.** These are identical to run 1:
- C1–C15 return their references, C13 at row 9 per PC-S2-C13;
- C5 and C9 pass;
- M1–M17 are caught;
- the `decide_row` self-test passes 37/37, and `unit_token` passes U1–U5.

## Disclosure: an implementation-aid Python check (owner's requirement)

- **What it computed.** While implementing stage 2, before commit `f14b59b2`, one `python3 -I`
  script was run in the session scratchpad, outside the repository. It checked, with exact
  Gaussian-rational arithmetic at random points, the polynomial identities behind three
  `linear_combination` steps in `scaled_rot_not_gauge_nonneg`:
  - `hzero`;
  - `hcc`;
  - the `c * 3/5 = 0` step inside `ha`.
- **Why.** To make sure the coefficients written into those proof steps were right before the CI
  build.
- **What it did not compute.** No control or candidate outcome: no `R`, `P`, `P₁`, `Gauge`, §7 value
  or held-out quantity on any candidate, and no control result.
- **What depends on it.** Nothing. The proof does not depend on it: `linear_combination`
  re-verifies each identity in the kernel through `ring`.
- **What is retained.** Its script and output are not retained in the repository.
- **Status.** It is recorded here as a disclosed implementation aid. It is not evidence.

## Local checks at this commit

- `python3 -I -B stage2/run-2/controls.py` and the same with `-O`: byte-identical to
  `run-2/results.json`. Run 1's `stage2/controls.py` still regenerates its own `results.json`.
- `tools/lean_manuscript_census.py`: OK. `tools/artifact_placement_check.py`: OK.
  `verification/lean/edge_rigidity_probe.py`: all checks pass.
- The frozen files are unchanged: the preregistration, PC★, `stage1-log.json`, the disposition,
  PC-S2 and PC-S2-C13.
- No Lean was built locally.

## Reproduction

From the PC-1 unit directory:

    python3 -I -B stage2/run-2/controls.py
    python3 -I -B -O stage2/run-2/controls.py
    python3 -I -B stage2/run-2/controls.py --kernel stage2/run-2/kernel-steps.json [--review stage2/run-2/review.json]

## Exact-head record for run-2 (to be completed from the host's records; ordinary draft-PR CI only)

| Item | Value |
|---|---|
| Exact head SHA | *pending* (the PR run tests a synthetic merge with `main`) |
| CI run id / job id | *pending* |
| `Mathlib bridge` → `Build` | *pending* |
| `Mathlib bridge` → `Release gate` (`lean_axiom_check`) | *pending* |
| `run-2/kernel-steps.json`, `run-2/kernel-decision.json` | *pending* |
| Independent exact-head review (`run-2/review.json`) | *pending* |

A failure is recorded here as it occurred and is not repaired. A further substantive defect stops
the run for a new owner decision.

## What this result does not establish

It does not establish:
- that OI, or an extension of it, makes a relative phase available, or that none can;
- a QM equivalence;
- any change to a manuscript, a ROADMAP row or a #914 status.

L1, L2 and L3 are not attempted, because no candidate exists.
