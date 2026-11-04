# PC-1 — stage 2, controls only: result

**Status: research-only.** This run executes exactly what two frozen records fix:
`amendments/PC-S2.md` (`4d2c4d56`) and the C13 correction `amendments/PC-S2-C13.md` (`895e5c5b`).

**Authority.** PR #1022 comments 6547077354 (Decision 2) and 6547368529 (the C13 decision).

**What was not run.** No candidate is frozen (PC★), so:
- no probe was run;
- no `R`, `P`, `P₁`, `Gauge`, §7 or held-out quantity was computed on a new or previously rejected
  candidate;
- nothing was re-screened.

The §7 values were computed only for the controls C7 (exact QM) and C10 (Kochen–Specker).

**Unchanged.** The preregistration (`948b30c1`), PC★, `stage1-log.json` with its SC-1 to SC-3
disclosure, the two-track disposition, PC-S2 and PC-S2-C13. `controls.py` checks each by blob and
sha256.

## The result, in two tracks

- **Strict token: `INCONCLUSIVE (void)`**, `void_reasons = ["0(vi)"]`.
  - Clause 0(vi) fires because of the stage-1 SC-1 to SC-3 Python checks (owner Decision 1,
    `amendments/PC-star-disposition.md`).
  - No stage-2 control can change this token.
  - This run adds no further void reason before CI: every control, mutation and self-test returns
    its reference.
- **Scientific finding, carried only under the owner's one-time exception (PR #1022 comment
  6547077354).**
  - **Statement.** No admissible candidate among the 25 screened (F2-1's 13 rules and Q1–Q12). The
    obstruction is G★ item 3 for native couplings: A★2 premise (ii) is broken by no native source.
  - **Scope (PC★ §PC★4).** Couplings whose joint process is a classical measurable bijection with
    function-valued records; the sources at `5914c17c` and the named branches. **It is not a
    no-go.**
  - **Status in `results.json`: `pending exact-head review`.** It becomes `carried under exception`
    only when both kernel steps succeed at the exact head and the independent exact-head review is
    recorded. Any failure makes it `withheld`.
- **Not a clean result.** This is not a compliant clean result, and the unit's token is never the
  gap token.

## Files

| File | Content |
|---|---|
| `stage2/controls.py` | The run: freeze, vendor and statement checks; C1–C15; M1–M17; the frozen §6 self-test; U1–U5; the `pc1-stage2-results/1` schema |
| `stage2/results.json` | Its output, before CI (kernel fields `pending`). Normal and `-O` runs are byte-identical |
| `stage2/vendor/recursive-substates/…` | F2-1's `run-2/controls.py` and two probes, byte-identical to `4e7ddb70` (blob ids checked at run time) |
| `verification/lean-mathlib/OIBridge/F2CoherenceControls.lean` | Vendored byte-identical (blob `fbf47504`): F2-1's 19 statements |
| `verification/lean-mathlib/OIBridge/PC1Controls.lean` | PC-S2's header and 14 fixed statements verbatim, with proofs. Auxiliary lemmas are named `aux_*` |
| `verification/lean-mathlib/OIBridge.lean` | Two import lines |
| `verification/lean-manuscript-census.json` | F2-1's entry, byte-identical to `05ecc873`, and the PC-1 entry (both kernel-only) |

## Controls: actual against expected

| Control | Expected row | Actual | Notes |
|---|---|---|---|
| C1 odometer | 9 | 9 | compressions are permutations and nonnegative (exact, `m ≤ 6`) |
| C2 hidden memory | 9 | 9 | coherent and dephased returns both 1 |
| C3 Route B | 3(a) | 3(a) | `phaseOperator` flagged |
| C4 ones-fixing | 9 | 9 | |
| C5 obstructions | pass | pass | no record with `R ∧ N` or `R ∧ O`; the lemmas are built in CI |
| C6 Koopman/Fourier | 3(b) | 3(b) | exhibits verified |
| C7 exact QM | 3(a) | 3(a) | 1, 337/625, 16/25, 576/625, 0 |
| C8 real class | 3(a) | 3(a) | `R`, `¬P`, `¬P₁` |
| C9 bit-1 mutant | pass | pass | backflow under the mutant only |
| C10 Kochen–Specker | 9 | 9 | reproduces 1, 337/625 and the C7 frequencies |
| C11a noncommuting permutations (`S₃`, Spekkens `S₄`) | 9 | 9 | permutation generators; nonnegative compressions; the identity gauge suffices |
| C11b exhibits | 3(b) | 3(b) | the `diag(ω, ω²)` Fourier exhibit is verified. The standard-representation rotation passes its checks but is not an exhibit under the inherited definition |
| C12 phase gauge | 9 (`Gauge_N` obstruction) | 9 | `D·swap·D† = [[0, −i], [i, 0]]`; the detector finds `D†` |
| C13 polar factor | **9, per PC-S2-C13** | 9 | `K = [[0, 2/3], [2/3, 5/9]]`, `U = [[−5/13, 12/13], [12/13, 5/13]]`; `UᵀU = 1` and `UᵀK` symmetric positive semidefinite; `exhibit_verified: false`; screen item 11 flags it. `R`: paper (PC-S2-C13 §3); `P₁`: kernel (`realSubclass_not_p1`) |
| C14 controlled lift | 9 | 9 | `s` conserved, so screen item 8 fails; noncommuting `T₀`, `T₂` |
| C15 class of `rot` | 3(a) | 3(a) | cycle ratio −16/9 (`Gauge_N` holds); `D†·rot·D` fixes the all-ones vector with eigenvalue `3/5 + 4i/5` (`Gauge_O` fails, PC-F1) |

**Mutations.** M1–M17 are all caught as stated.

**Self-test.** `decide_row`: 37 of 37 cases route as frozen. They cover every row and sub-row of
§6 and every listed case, including:
- 6(d) when not transplantable;
- 7 with an exhibit;
- 7 with `S` varying;
- `Φ_min` without `P`;
- C15's shape.

`unit_token`: U1–U5 all pass. U1, a clean pass, gives VOID with `["0(vi)"]` and the finding
carried, with no gap token.

**Evidence labels.** The control records are set in `control_records` with their sources:
- `kernel:<declaration>`, for statements built in CI;
- `paper`, for C12's transport lemma, C15's minimality and C13's `¬R`;
- `exact`, for the computed checks.

The correspondence between a record and its declaration is cited, not machine-checked.

## Local checks at this commit

- `python3 -I -B stage2/controls.py` and the same with `-O`: byte-identical to `results.json`.
- `--kernel` (with a scratch input, not committed): byte-identical in normal and `-O` modes.
- `tools/lean_manuscript_census.py`: OK. `tools/artifact_placement_check.py`: OK.
  `verification/lean/edge_rigidity_probe.py`: all checks pass.
- No Lean was built locally. The 33 kernel statements enter only through CI step conclusions.

## Reproduction

From the PC-1 unit directory:

    python3 -I -B stage2/controls.py
    python3 -I -B -O stage2/controls.py
    python3 -I -B stage2/controls.py --kernel stage2/kernel-steps.json [--review stage2/review.json]

## Exact-head record (to be completed from the host's records; ordinary draft-PR CI only)

| Item | Value |
|---|---|
| Exact head SHA | *pending* (the PR run tests a synthetic merge with `main`) |
| CI run id / job id | *pending* |
| `Mathlib bridge` → `Build` | *pending* |
| `Mathlib bridge` → `Release gate` (`lean_axiom_check`) | *pending* |
| `stage2/kernel-steps.json`, `stage2/kernel-decision.json` | *pending* |
| Independent exact-head review (`stage2/review.json`) | *pending* |

A failure at any step is recorded here as it occurred and is not repaired. A substantive defect
stops the run for a new owner decision.

## What this result does not establish

It does not establish:
- that OI, or any extension of it, makes a relative phase available, or that none can;
- a QM equivalence;
- any change to a manuscript, a ROADMAP row or a #914 status.

L1, L2 and L3 are not attempted, because no candidate exists.
