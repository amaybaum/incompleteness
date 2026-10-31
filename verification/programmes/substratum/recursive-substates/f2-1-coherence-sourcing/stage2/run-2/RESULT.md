# SUBSTATE-2 unit F2-1 — stage 2, run-2 (controls only)

**Status: research-only; a separate stage-2 attempt.**

The earlier attempt at `05ecc8732160736b538b422114a5a1738d682c16` remains `INCONCLUSIVE (void)`:
its ordinary PR CI run 41220197866 failed the `Build` step. That attempt and its files in
`stage2/` are preserved unchanged.

This run follows the owner's bounded recovery (PR #1011 comment 6546214912) under amendment A★-1
(accepted at `fdeeb2d5`).
- **Frozen inputs, unchanged:** the preregistration (`66eb48ca`), A★ (`b86f0547`), A★-1 and the
  stage-1 log.
- **Scope, unchanged:** only the preregistered controls C1–C10, the mutations M1–M10, the
  decision-function self-test and the 19 fixed-statement Lean declarations. No `R`, `R†`, `P`,
  Gate 4 or Gate 5 quantity is computed on any candidate; none exists.

## Files

| File | Content |
|---|---|
| `run-2/controls.py` | A copy of `stage2/controls.py`. Its only diffs are those A★-1.4 permits: `UNIT` re-anchored to the run directory, the constant `ASTAR1_SHA256` and its term in the freeze check, and run metadata (`amendment_1`, `run`). |
| `run-2/results.json` | The run's results. Against the preserved `stage2/results.json`, the only differences are two added metadata fields, `amendment_1` and `run`. Every control value, mutation, self-test row, statement digest, kernel field and the withheld token are identical. |
| `run-2/PROOF-REPAIRS.md` | Each Lean change, with the defect it traces to. |
| `verification/lean-mathlib/OIBridge/F2CoherenceControls.lean` | The `open Matrix` context, and the two authorized proof repairs. |

## Outcome rule for this run

- **Kernel steps.** The kernel declarations enter only through the `Mathlib bridge` job's `Build`
  and `Release gate` step conclusions at the exact head of this run. The gate's `lean_axiom_check`
  requires every `#print axioms` report to be present, free of `sorryAx`, and within `propext`,
  `Classical.choice` and `Quot.sound`.
- **Both steps succeed:** the frozen rule gives `INCONCLUSIVE (gap)` (clause 1).
- **Either step fails:** the result is `INCONCLUSIVE (void)` (clause 0(v)). Any repair then needs
  separate owner authorization.
- **Any other void reason** would be a failure of a frozen requirement, and is reported as such.
  "Other" means anything besides 0(v) from build status: a control, mutation or self-test, the
  freeze, the measure, floats, pre-A★ computation, or probe coupling.
- **Until CI,** the token is withheld (`verdict_status`: awaiting CI step conclusions).

## Controls: actual against expected

All controls give the same values as the preserved run:

| Control | Row |
|---|---|
| C1 | 8 |
| C2 | 8; G4d returns 1 with and without readout |
| C3 | 3(a) |
| C4 | 8 |
| C5 | pass |
| C6 | 3(b), exhibits verified exactly |
| C7 | 3(a); values 1, 337/625, 16/25, 576/625, 0 |
| C8 | 3(a) |
| C9 | mutant backflow detected, none under the α=1 rule |
| C10 | 8 |

Every mutation M1–M10 is caught, and every self-test row routes correctly. The values are in
`run-2/results.json`.

## Labelling

- **Control records are set in code.** The `R`, `P`, `N`, `O` and screen values of each control
  are entered by `control_records` in `controls.py`. The code does not read them from the kernel.
  The kernel declarations they correspond to are cited below. CI builds them, but the
  correspondence between a code value and a declaration is not machine-checked.

  | Control | Values and their kernel source |
  |---|---|
  | C1, C2, C10 | `¬R`: `permTheory_falsifierUnavailable`, or `falsifierUnavailable_of_nonnegBounded` with `nonnegClass_nonnegBounded`. `¬P`: `permTheory_phase_ceiling`, `nonnegBounded_not_phasesAvailable`. `N`: `permTheory_nonnegBounded`, `nonnegClass_nonnegBounded`. `O`: `permTheory_onesBounded`, `onesBounded_of_onesFixing` with `nonnegClass_onesFixing`. |
  | C3 | `¬R`: `substratumTheory_falsifierUnavailable`. `P`: `substratumTheory_derivedOI`. |
  | C4 | `¬R`: `onesTheory_falsifierUnavailable`. `¬P`: `onesTheory_not_phasesAvailable`. `O`: `onesBounded_of_onesFixing`, `isometry_fixes_ones`. |
  | C7 | `fullTheory_rot`, `fullTheory_rotDagger`, `fullTheory_phases`. |
  | C8 | `realTheory_rot`, `realTheory_not_phases`. |

  The class containment of each model is exact for C1 and C2, and a paper step for C10.
- **C10 cites, it does not derive.** C10 uses the published Kochen–Specker (1967) single-qubit
  marginal, outcome probability `(1 + n·a)/2`, with the published state-dependent hidden density.
  It does not derive that marginal. The run reproduces the C7 numbers from it and records its
  scope: the model separates Gate 4 only from non-invasive classical models. That scope is recorded,
  not tested.
- **XOR truncation.** The infinite-XOR model is run as this unit's cyclic truncation with 3 and 4
  blocks, as in the preserved run.

## Reproduction

From the repository root:

    python3 -I -B verification/programmes/substratum/recursive-substates/f2-1-coherence-sourcing/stage2/run-2/controls.py
    python3 -I -B -O verification/programmes/substratum/recursive-substates/f2-1-coherence-sourcing/stage2/run-2/controls.py
    python3 -I -B verification/programmes/substratum/recursive-substates/f2-1-coherence-sourcing/stage2/run-2/controls.py --kernel KERNEL.json

## Record for the exact-head run

To be completed from the host's records, not from logs:
- the exact head SHA;
- the 19 statement checksums of A★-1.3 (`statement_sha256` in `results.json`);
- the axiom-output evidence, through the `Release gate` step;
- the `Build` and `Release gate` step conclusions;
- an independent exact-head review.

Ordinary draft-PR CI only; no special dispatch.

## What this result does not establish

No admissible access rule exists among the 13 candidates screened in stage 1. That is the extent of
the result. It is not a no-go for observer-level extensions, and it is not an equivalence. L3 and
the F2 obligation of #914 remain open, and no manuscript, axiom or graded claim changes.
