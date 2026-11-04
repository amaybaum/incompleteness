# SUBSTATE-2 unit F2-1 — stage 2 result (controls only)

**Status: research-only.** This is stage 2 of the unit preregistered in `../preregistration.md`
(frozen at `66eb48ca`), with stage 1 recorded in `../amendments/A-star.md` (`b86f0547`).

The owner authorized this stage in PR #1011, comment 6545904226 (amaybaum, OWNER,
2026-10-31T16:12:50Z). The authorization covers:
- the reference controls C1–C10;
- the mutations M1–M10;
- the decision-function self-test;
- the fixed-statement Lean declarations of A★ §A★5.

No `R`, `R†`, `P`, Gate 4 or Gate 5 quantity was computed on any candidate, because stage 1 fixed
none. Nothing in the frozen preregistration, A★, the stage-1 log or the SUBSTATE-2 records at
`c811e876` was changed. Issue #1010 (host PR #1011) tracks the unit, and its governing gate is
#914 (F2; rows 8, 9, 11, 12; L3).

## Files

| File | Content |
|---|---|
| `controls.py` | Exact controls, mutations, self-test and decision function. It uses the standard library only and exact arithmetic: fractions, Gaussian rationals and `ℚ(√−3)`. |
| `results.json` | The results file, schema `f2-1-results/1`, with sorted keys and no timestamps. |
| `verification/lean-mathlib/OIBridge/F2CoherenceControls.lean` | The 19 fixed statements of A★ (3 definitions, 16 theorems), copied verbatim, with proofs and 16 `#print axioms` lines. It adds 7 auxiliary declarations: four `rot` entry lemmas, a conjugation lemma for the nonnegative class, a complexification lemma, and the real matrix `rotR`. |
| `verification/lean-mathlib/OIBridge.lean` | Imports the module, so CI builds it. |
| `verification/lean-manuscript-census.json` | Adds the family "SUBSTATE-2 unit F2-1 stage-2 kernel controls (research)": kernel-only, no manuscript anchor. |

## Controls: actual against expected

Each control's token is computed by the frozen decision rule from the control's record. The record
cites the kernel declarations its `R`, `P`, `N` and `O` values rest on.

| Control | Exact checks (actual) | Expected | Actual |
|---|---|---|---|
| C1, odometer through Θ-A and Θ-K | At depths 1–6 (computed at depth +2), the compressions are 0/1 permutation matrices: nonnegative, rows and columns summing to 1. Haar measure is invariant. | row 8, `COUNTEREXAMPLE` | row 8 |
| C2, non-invasive hidden-memory models | All are bijective at their finite stages. Return to the initial visible value is 1 with and without an intermediate readout (G4d) for: B1 at depths 1, 2, 3, 5, 7; B2 at cycles 3–9; FIXED-SCALE at tapes 3–9; infinite-XOR truncated to 3 and 4 blocks. | row 8 | row 8 |
| C3, `substratumTheory` with P1 as a generator | `diag(i, 1)` has a non-real ratio, and the screen flags it. | row 3(a), `REPRESENTATION-ONLY` | row 3(a) |
| C4, `onesTheory` | Kernel only. | row 8 | row 8 |
| C5, obstructions | No record has `R` together with `N` or `O`. | pass | pass |
| C6, representation exhibits | The odometer's Koopman operator on `ℤ/4` in the character basis is `diag(1, i, −1, −i)`. The α=1 two-slice wave map on the periodic cubic lattice `L = 6`, mode `k = (1, 1, 4)`, has `a_k = 1` and eigenvalues `(1 ± √−3)/2`, whose ratio `(−1 + √−3)/2` is non-real. Both were checked site by site. | row 3(b), `REPRESENTATION-ONLY` | row 3(b) |
| C7, exact QM (full class) | G4a = 1; G4b = 337/625; frequencies 16/25 (`rot`), 576/625 (`rot²`) and 0 (`rot·phaseGate·phaseGate·rot`). The screen flags `fullClass`. | row 3(a) | row 3(a) |
| C8, real-amplitude class | Kernel only. The screen flags `rot` as a stipulated generator. | row 3(a) | row 3(a) |
| C9, NATIVE-PADIC-1 bit-1 mutant | At `q = 4` and `8`, through the read-only `c811e876` probe: no backflow under the α=1 rule, backflow for the mutant, and the mutant is reversible. | detected | detected |
| C10, Kochen–Specker 1967 model | Reproduces G4a = 1, G4b = 337/625 and the C7 frequencies through exact Bloch rotations. Its Θ-K containment is a paper step. | row 8 | row 8 |

G4d passes: the non-invasive models (C2) return 1 with and without readout. The disturbing-readout
model (C10) reproduces 1 and 337/625.

## Mutations

Every mutation is caught by its named control:

| Mutation | Result |
|---|---|
| M1, swap in place of `rot` | Coherent and dephased returns are both 1, so there is no discrimination. |
| M2, `phaseGate` added to the C3 generator set | The screen flags it. |
| M3, non-invariant measure on the depth-3 odometer stage | The invariance check fails. |
| M4, a float in a decision path | Clause 0(iv). |
| M5, a C2 model in place of a candidate | Not row 4. |
| M6, inserted dephasing labelled `sourced` | The label check fails. |
| M7, `p = 1` encoding | Frequencies 4/7 and 24/31 against 16/25 and 576/625, giving row 2(b). |
| M8, `R†` assumed | Not row 4: row 6. |
| M9, hardcoded success | The self-test fails. |
| M10, constant rule `:= rot` | The screen flags it (row 3(a)), and as a probe it gives row 2(a). |

## Decision-function self-test

Every case returns its preregistered row:
- row 0, each of (i)–(vii);
- rows 1, 2(a), 2(b) through Gate 5a and through G4a, 3(a) and 3(b);
- row 4, both grades, with the grade read from `review.grade`;
- rows 5 and 6;
- row 7, through one of `R`, `P` and through a non-transplantable probe;
- row 8, both plain and with a non-transplantable coupling;
- row 9;
- the pending-kernel case, which withholds the token.

## Kernel predicates and the token

The kernel declarations enter the results only as CI step conclusions (§9; §A.44). These are the
`Mathlib bridge` job's `Build` step and its `Release gate` step, which runs `lean_axiom_check`:
every `#print axioms` report must be present, contain no `sorryAx`, and use no axiom outside
`propext`, `Classical.choice` and `Quot.sound`.

The 19 A★ declarations carry statement digests, and the script checks that each A★ statement occurs
verbatim in the module. The 11 cited existing declarations are listed beside them. No local Lean
build was run, so `results.json` records every conclusion as `pending`.

**Token.** None yet. `verdict_status` is "awaiting CI step conclusions for the kernel
declarations".
- **If both steps succeed** at the exact head, the frozen rule gives `INCONCLUSIVE (gap)` (clause 1).
  The script records this as `token_if_kernel_steps_succeed`.
- **If either step fails,** the rule gives `INCONCLUSIVE (void)` (clause 0(v)). That outcome is
  reported, and the test is not redefined.
  - A proof repair that leaves every A★ statement unchanged is not a test change.
  - A statement change needs a further reviewed amendment (A★ §A★5).

## Reproduction

From the repository root:

    python3 -I -B verification/programmes/substratum/recursive-substates/f2-1-coherence-sourcing/stage2/controls.py
    python3 -I -B -O verification/programmes/substratum/recursive-substates/f2-1-coherence-sourcing/stage2/controls.py
    python3 -I -B verification/programmes/substratum/recursive-substates/f2-1-coherence-sourcing/stage2/controls.py --kernel KERNEL.json

The first two runs regenerate the results and require byte equality with `results.json`; this
held in both. The third run takes a JSON file `{head_sha, run_url, build_step, axiom_check_step}`
read from the host's step records and prints the unit decision. Runtime is under one second.

## Judgment calls

- **XOR truncation.** SUBSTATE-1's infinite-XOR model has no pinned finite stage. It is run here as
  a cyclic truncation with 3 and 4 blocks, labelled as this unit's truncation.
- **What carries the classification.** C2, C4, C8 and the class parts of C1 and C10 rest on kernel
  facts about classes (`permTheory`, `nonnegClass`, `onesTheory`, `realClass`). The containment of
  each model in its class is exact (C1, C2), or a paper step for the continuum models (C10).
- **Granularity of the CI evidence.** The two step conclusions are shared by all declarations. A
  release-gate failure for an unrelated reason would therefore read as clause 0(v) until it is
  diagnosed against the exact-head run.

## What this result does not establish

No admissible access rule exists among the 13 candidates screened in stage 1. That is the extent of
the result. It is not a no-go for observer-level extensions, it is not an equivalence, and it
sources neither `rot` nor the phases. L3 and the F2 obligation of #914 remain open, and no
manuscript, axiom or graded claim changes.
