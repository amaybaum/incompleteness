# Reconstruction round K1-SHARP-TESTS-1 — the premise `2 ≤ d` as sharp-test multiplicity: PREREGISTRATION

**Status: candidate freeze.** This file is the control plane of a native round under `AGENTS.md` §A.39. It is drafted
on its pull request from `D` and is final only at the commit `F` the owner designates; no commit after `F` changes it.
The two questions, the two decision rules, the non-inference rule, the frozen surface, the controls, the evidence
ledger, the stages and the outcomes below are fixed; the predicted execution tree is recorded before `F`.

```v3-round
round K1-SHARP-TESTS-1
kind non-sealing
record-directory verification/programmes/oi-qm/reconstruction/round-k1-sharp-tests-1/
```

```v3-governed-paths
record AM verification/programmes/oi-qm/reconstruction/round-k1-sharp-tests-1/
record AM verification/receipts/K1-SHARP-TESTS-1.json
execution A verification/lean-mathlib/OIBridge/SharpTests.lean
execution M verification/lean-mathlib/OIBridge.lean
execution M verification/lean-manuscript-census.json
```

The record directory holds this preregistration, the round's frozen controls `controls.py` and the result note. The
receipt path is `verification/receipts/K1-SHARP-TESTS-1.json`. Every other path the round changes is an execution path
listed above. **No manuscript, no built artifact, `verification/ROADMAP.md`, the workflow, no probe and no other
round's record change under any outcome.**

## The objects

- **`D`** = `68b6df0651f14b2c8ab082635b8d2051918617a2`, the head of `main` after round K2-GUARD-1 landed (merge of `Q`
  `d8e8b900`; the push run 37492686024 at `D` succeeded, the act 42 exclusion matrix skipped on push).
- **`F`** — the commit carrying this file, which the owner designates; `delta(D, F)` is this file.
- **`E`** — the certified execution head, which the owner designates.
- **`Λ`**, **`Q`** — the reconciliation and the receipt commit, as §A.39 defines them.

## What the round is

K2-GUARD-1 reduced the premise of the relative dimension selector `three_of_nativeGateOf_of_two_le` to `2 ≤ d` beside
effect soundness, body preservation, K∞-Seed, K∞-Trans, K∞-V4, `IsNot` and `NativeGateOf`. This round asks two
independent questions about that premise, each read from the kernel statements by its own frozen decision rule.
Neither rule reads the other's statements, and neither outcome depends on the other.

The predicate is `HasTwoSharpTests Ω`: there are two sharp seeds `e`, `f` of `Ω` (OG-1's `SharpSeed`: an effect on `Ω`
with a certain state and a zero state) such that some state of `Ω` separates `f` from `e` and some state separates `f`
from the complement `1 − e`. A binary test is identified with the pair `{e, 1 − e}`, and two tests are identified when
they agree on every state of `Ω`; the predicate says there are at least two tests after that identification.

- **Q-CLASSIFIED.** On the coordinate ball `eball d`, does `HasTwoSharpTests (eball d) ↔ 2 ≤ d` hold, through the
  complement identity for opposite directions, the classification of sharp seeds by EFF-1's `sharp_eq_of_certain`, the
  exclusion at `d = 0`, the equal-or-complementary alternative at `d = 1`, and the two-axis witness for `2 ≤ d`?
- **Q-NOT-IMPLIED.** Do the relative selector's hypotheses other than `2 ≤ d` hold together at `d = 1` for one explicit
  instance — the full effect family `fullEffects (eball 1)`, the full automorphism family `fullAut 1`, the sharp seed
  `sharpEff z1`, DIM-1's NOT `neg1` and the gate `cnot1` — so that they do not imply `2 ≤ d`?

The earned reading of the two positive cells together is only this: on the coordinate ball `eball d`, the elementary
body of the reconstruction, the remaining premise `2 ≤ d` of the dimension selector is equivalent to the existence of
two sharp binary tests distinct modulo complementation, and the selector's other relative hypotheses do not imply that
condition. The `d = 1` instance is one countermodel; it does not classify the instances at `d = 1`.

### The decision rules (frozen; implemented by `controls.py verdict`)

| Cell | Outcome | Rule |
|---|---|---|
| Q-CLASSIFIED | `K1-SHARP-TEST-MULTIPLICITY-CLASSIFIED` | all of: `HasTwoSharpTests Ω` is defined as `∃ e f : V →ᵃ[ℝ] ℝ, SharpSeed Ω e ∧ SharpSeed Ω f ∧ (∃ x ∈ Ω, f x ≠ e x) ∧ (∃ x ∈ Ω, f x ≠ 1 - e x)`; every classification theorem of the table below has exactly its frozen explicit binders and conclusion and names its frozen proof dependencies; the equivalence `hasTwoSharpTests_iff` names its three directional witnesses `not_hasTwoSharpTests_zero`, `not_hasTwoSharpTests_one` and `hasTwoSharpTests_of_two_le`; and the verdict `k1sharp_classified` has its frozen conclusion |
| Q-CLASSIFIED | `K1-SHARP-TEST-MULTIPLICITY-NOT-CLASSIFIED` | otherwise |
| Q-NOT-IMPLIED | `K1-TWO-LE-NOT-IMPLIED` | all of: `two_le_load_bearing_relative`, `nativeGateOf_cnot1`, `two_le_not_implied` and the verdict `k1sharp_two_le_not_implied` are theorems without explicit binders with their frozen conclusions; the hypothesis chain of `two_le_not_implied` is, type for type and in order, the explicit hypotheses other than `2 ≤ d` of the landed `three_of_nativeGateOf_of_two_le`, read from `D`; and the proof of `two_le_not_implied` names `two_le_load_bearing_relative` |
| Q-NOT-IMPLIED | `K1-TWO-LE-NON-IMPLICATION-NOT-ESTABLISHED` | otherwise |

The round's outcome is `K1-SHARP-TESTS-1-READ` when both cells are assigned, each by its own rule. The design run below
already exhibits a module read by these rules as `K1-SHARP-TEST-MULTIPLICITY-CLASSIFIED` and `K1-TWO-LE-NOT-IMPLIED`;
the rules, not that reading, are what this file freezes, and the cells at `E` are those `controls.py verdict E` prints.

### The classification (frozen statements)

| Item | Theorem | Explicit binders | Frozen conclusion | Proof names |
|---|---|---|---|---|
| complement | `sharpEff_neg_apply` | `(b x : Fin d → ℝ)` | `sharpEff (-b) x = 1 - sharpEff b x` | — |
| seeds | `sharpSeed_eq_sharpEff` | `(h : SharpSeed (eball d) e)` | `∃ u : Fin d → ℝ, ∑ j, u j ^ 2 = 1 ∧ e = sharpEff u` | `sharp_eq_of_certain` |
| seeds | `sharpSeed_iff` | `(e : (Fin d → ℝ) →ᵃ[ℝ] ℝ)` | `SharpSeed (eball d) e ↔ ∃ u : Fin d → ℝ, ∑ j, u j ^ 2 = 1 ∧ e = sharpEff u` | `sharpSeed_eq_sharpEff`, `sharpEff_sharpSeed` |
| `d = 0` | `not_sharpSeed_zero`, `not_hasTwoSharpTests_zero` | `(e : (Fin 0 → ℝ) →ᵃ[ℝ] ℝ)`; none | `¬ SharpSeed (eball 0) e`; `¬ HasTwoSharpTests (eball 0)` | —; `not_sharpSeed_zero` |
| `d = 1` | `eq_or_compl_one`, `not_hasTwoSharpTests_one` | `(he : SharpSeed (eball 1) e) (hf : SharpSeed (eball 1) f)`; none | `(∀ x ∈ eball 1, f x = e x) ∨ (∀ x ∈ eball 1, f x = 1 - e x)`; `¬ HasTwoSharpTests (eball 1)` | `sharpSeed_eq_sharpEff`; `eq_or_compl_one` |
| witness | `hasTwoSharpTests_of_two_le` | `(hd : 2 ≤ d)` | `HasTwoSharpTests (eball d)` | `sharpEff_sharpSeed` |
| equivalence | `hasTwoSharpTests_iff` | none | `HasTwoSharpTests (eball d) ↔ 2 ≤ d` | `not_hasTwoSharpTests_zero`, `not_hasTwoSharpTests_one`, `hasTwoSharpTests_of_two_le` |

The two directions of the equivalence have separate witnesses (§A.34): the forward direction is the `d = 0` and `d = 1`
cases, the converse is the axis witness at `e₀`, where the axis tests take the values `1`, `1/2` and `0` for `e`, `f`
and `1 − e`.

### The non-implication (frozen statements)

| Item | Theorem | Frozen conclusion |
|---|---|---|
| gate | `nativeGateOf_cnot1` | `NativeGateOf (eball 1) (fullEffects (eball 1)) z1 neg1 cnot1`, from DIM-1's `nativeGate_cnot1` and EFF-1's `maxConeOf_fullEffects` |
| control | `two_le_load_bearing_relative` | `EffectsOn (eball 1) (fullEffects (eball 1)) ∧ PreservesBody (eball 1) (fullAut 1) ∧ SharpSeed (eball 1) (sharpEff z1) ∧ BoundaryTransitive (eball 1) (fullAut 1) ∧ SeedOrbitAvailable (fullAut 1) (sharpEff z1) (fullEffects (eball 1)) ∧ IsNot (eball 1) z1 neg1 ∧ NativeGateOf (eball 1) (fullEffects (eball 1)) z1 neg1 cnot1 ∧ ¬ (2 ≤ 1)` |
| non-implication | `two_le_not_implied` | `¬ (∀ d avail G r z N T, EffectsOn (eball d) avail → PreservesBody (eball d) G → SharpSeed (eball d) r → BoundaryTransitive (eball d) G → SeedOrbitAvailable G r avail → IsNot (eball d) z N → NativeGateOf (eball d) avail z N T → 2 ≤ d)`, with the binder types of the landed relative selector |

### The non-inference rule (frozen)

> This round does not show that OI provides two sharp binary tests; does not derive them from StageCompletion or from
> the observer architecture; does not establish incompatibility, noncommutativity or complementarity in a
> quantum-mechanical sense; does not characterize sharp-test multiplicity on bodies other than `eball d`; does not
> state that a classical theory has a single binary test; does not affect K2 or H-Bell; and does not relate
> `HasTwoSharpTests` to entanglement, in either direction. The `d = 1` instance is one countermodel and does not
> classify the instances at `d = 1`.

The result note states each cell in the words of its row, the earned reading above, and nothing stronger.

### In scope
- the module `OIBridge/SharpTests.lean` with the statement surface of §"The frozen surface";
- its import line in `OIBridge.lean` and its family in `lean-manuscript-census.json`;
- `controls.py` and the result note.

### Frozen out
- any statement of `HasTwoSharpTests` about a body other than `eball _`; any source of the predicate or of `2 ≤ d`;
- any statement relating the predicate to `Entangling`, `EntanglingOf` or any composite;
- a limit closure, a flow, a complex or matrix representation of the state space;
- any edit to `EffectSpace`, `K1Bridge`, `K2Guard`, `CompositeDimension`, a manuscript, `verification/ROADMAP.md`, the
  EFF-1, K1-BRIDGE-1 or K2-GUARD-1 records, or any other round's record.

## The frozen surface

**Design-run rule:** compilation failures may cause implementation repairs, but no repair may strengthen or weaken a
frozen theorem statement, definition or hypothesis without a new preregistration revision and new design theorem
identity.

The design theorem identity is the statement surface of `SharpTests` embedded in `controls.py` (blob
`8e7b8e03b427445a316cb334437c29a1a336896b`): the preamble (the import, namespaces, `open` lines and
`variable {V : Type} [NormedAddCommGroup V] [NormedSpace ℝ V] {d : ℕ}`), the context blocks in order, the 18
declarations in order and by kind, every theorem's signature up to `:=` (for `nativeGateOf_cnot1`, up to `where`),
every definition whole, and the 13 `#print axioms` lines. The reference module is blob `fd725b5e1a7296a4114a336419bf7e0d00f2d774`.
A repair may change theorem proofs only. `OIBridge.lean` is `D`'s with `import OIBridge.SharpTests` inserted directly
after `import OIBridge.K2Guard`. The census is `D`'s with one family, embedded in `controls.py`, inserted directly
after the K2-GUARD-1 family (modules `["K2Guard"]`), in `D`'s two-space JSON layout.

### Semantic guards (in `controls.py`)

Each lists the mutation controls `--self-test` drives through it, every one of which must fail with the named code.

- **S1 predicate.** `HasTwoSharpTests` is the frozen definition whole. Mutations: the complement clause dropped; test
  identity as equality of maps (`f ≠ e`) in place of separation on a state.
- **S2 classified.** Every classification theorem with its frozen explicit binders, conclusion, proof dependencies and
  print; the cell's verdict with its frozen conclusion. Mutations: the witness requiring `3 ≤ d`; the equivalence
  weakened to one direction; the complement identity changed; the equivalence proved without the `d = 1` case; the
  seed classification proved without `sharp_eq_of_certain`.
- **S3 not implied.** The control, the gate instance, the non-implication and the cell's verdict with their frozen
  conclusions and prints; the non-implication's proof naming the control; and, at check time, the landed relative
  selector at `D` yielding exactly the frozen hypothesis types. Mutations: a hypothesis dropped from the control; a
  hypothesis dropped from the non-implication; the non-implication proved without the control; a landed selector with
  a hypothesis dropped does not yield the frozen types.
- **S4 scope.** No declaration mentions `Entangling` or `EntanglingOf`; `HasTwoSharpTests` is applied in a theorem
  only to `eball _`; no theorem concludes `2 ≤ d` alone. Mutations: an entangling object mentioned; the predicate
  concluded of a general body; a theorem concluding `2 ≤ d`.
- **S5 reuse.** No declaration has the name of a landed object it reads; the only import is `OIBridge.K1Bridge`.
  Mutations: `fullAut` re-declared; a second import.
- **S6 neutral.** No complex, conjugate-transpose, positive-semidefinite, trace, qubit, Bloch, Pauli, density, flow,
  limit, closure, dense-subgroup, tensor-product, Hilbert, mixing-closure or commutator token. Mutations: a complex
  scalar; a closure.
- **S7 phrases.** The module header and, at a commit carrying it, the result note contain none of the frozen phrases
  (among them "OI supplies", "supplied by OI", "derived from OI", "StageCompletion supplies", "the observer
  architecture supplies", "establishes complementarity", "quantumness", "nonclassicality", "every classical theory
  has", "equivalent to entanglement", "implies entanglement", "on every convex body", "derives 2 ≤ d", "qubit";
  case-insensitive, whitespace-normalized). Mutation: "This is quantumness." in the header; a note with "OI supplies"
  (and a neutral note passes).
- **S8 separation.** §A–§C and the classification verdict mention none of the selector's objects (`NativeGateOf`,
  `IsNot`, `EffectsOn`, `PreservesBody`, `BoundaryTransitive`, `SeedOrbitAvailable`, `fullAut`, `fullEffects`,
  `cnot1`, `neg1`, `z1`, `W`); §D and the non-implication verdict do not mention `HasTwoSharpTests`; `2 ≤ d` occurs
  only in §C, §D and the verdicts. Mutations: `fullAut` in §B; the predicate in §D; `2 ≤ d` in §A.
- **S9 count.** Exactly the 13 frozen `#print axioms` lines, in order and distinct. Mutations: an extra print; a
  duplicated print.
- **V verdicts.** Each cell yields one outcome by its own rule; at a commit carrying the result note, the note contains
  exactly the two computed tokens and no other. Controls: the predicate without the complement clause reads
  `K1-SHARP-TEST-MULTIPLICITY-NOT-CLASSIFIED` and leaves the other cell `K1-TWO-LE-NOT-IMPLIED`; a hypothesis dropped
  from the control reads `K1-TWO-LE-NON-IMPLICATION-NOT-ESTABLISHED` and leaves the other cell
  `K1-SHARP-TEST-MULTIPLICITY-CLASSIFIED`; the equivalence weakened to one direction reads
  `K1-SHARP-TEST-MULTIPLICITY-NOT-CLASSIFIED`; the non-implication proved without the control reads
  `K1-TWO-LE-NON-IMPLICATION-NOT-ESTABLISHED`; the note-token reader finds exactly the stated tokens.
- **N1–N3** as K2-GUARD-1. **I, C** as K2-GUARD-1, with the import after `OIBridge.K2Guard` and the family after
  K2-GUARD-1's.

`controls.py`:
- is blob `8e7b8e03b427445a316cb334437c29a1a336896b` (895 lines), generated from the reference tree by `gen_controls.py`;
- was frozen, and this revision committed, before any outcome of the predicted execution tree was read;
- `--self-test` passes 57 checks.

### Count facts

- the module carries **13** frozen `#print axioms` lines (S9) and 18 declarations;
- none of the 13 short names occurs in a `#print axioms` line at `D`, so the prints add 13 names to
  `lean_axiom_check`'s count;
- at `D` the release gate's `lean-axioms` step reports 5762 named results.

## Evidence ledger

Each row is discharged at `E` by the exact-head run at `E` and by `controls.py check E --freeze F`.

| Row | Kernel identifiers | Evidence required at `E` | Control |
|---|---|---|---|
| predicate | `HasTwoSharpTests` | the frozen definition | S1, V |
| complement and seeds | `sharpEff_neg_apply`, `sharpSeed_iff` | built; axioms within `[propext, Classical.choice, Quot.sound]` | S2 |
| `d = 0`, `d = 1` | `not_sharpSeed_zero`, `not_hasTwoSharpTests_zero`, `eq_or_compl_one`, `not_hasTwoSharpTests_one` | as above | S2 |
| witness and equivalence | `hasTwoSharpTests_of_two_le`, `hasTwoSharpTests_iff` | as above | S2, V |
| `d = 1` instance | `nativeGateOf_cnot1`, `two_le_load_bearing_relative` | as above | S3 |
| non-implication | `two_le_not_implied` | as above | S3, V |
| verdicts | `k1sharp_classified`, `k1sharp_two_le_not_implied` | as above | S2, S3, V |
| count | the 13 prints | each within the three axioms; `lean-axioms` passes | S9 |

## Design evidence

Pre-round evidence (`workflow_dispatch` on the disposable branch `claude/twole-design` from `8daf2bc0`, before
K2-GUARD-1 landed; the predicate named `TwoSharpTests`, without the non-implication theorem or the verdicts):

| Run | Commit | Workflow run | Result |
|---|---|---|---|
| a | `92a09a1c` | 37492945459 | **failed**: the definition was declared over `Type*` with `AddCommGroup`/`Module`, a context in which OG-1's `SharpSeed` (declared over `Type` with `NormedAddCommGroup`/`NormedSpace`) does not apply; the four theorems reading the predicate carried `sorryAx`; repair history only |
| b | `0850281a` | 37494787556 | **green**: all 32 jobs `success`; the only change from run a was that `variable` line; the ten prints within `[propext, Classical.choice, Quot.sound]`; release gate PASS (`lean-axioms` 5753) |

Design run on the certified base `D` (`workflow_dispatch`; the Mathlib bridge job and the release gate read):

| Run | Branch, commit | Workflow run | Result |
|---|---|---|---|
| 1 | `claude/k1st-dev` `ece1aa89` (from `D`: the module, blob `fd725b5e`; the import after `K2Guard`; the census family after K2-GUARD-1's) | 37498896443 | **green**: all 32 jobs `success`; the Mathlib bridge (job 112390484286) built `OIBridge.SharpTests` with each of the 13 `#print axioms` lines within `[propext, Classical.choice, Quot.sound]` and no warning in the module; release gate PASS (`lean-axioms` 5775, no `sorryAx`; `lean-manuscript` OK; 303 legacy records intact; 37 receipts hold); the Lean kernel check (job 112390484303) and the probe aggregate (job 112398278760) succeeded |

Run 1 is the design evidence for the frozen implementation; no repair was needed, and the execution blobs of
§"The frozen surface" are those of run 1. Pre-round runs a and b are supporting history only.

Statement-level choices recorded as frozen: test identity is agreement on the states of the body, not equality of
affine maps; the predicate is stated over OG-1's carrier context and proved about `eball d` only; the `d = 1` instance
is the full effect family, the full automorphism family, the seed along `z1`, `neg1` and `cnot1`; the non-implication
is stated over the binder types of the landed `three_of_nativeGateOf_of_two_le`.

### The predicted execution tree

- **`2f386e5e5f56e76fb1320f7583ecbd3d9f371c07`** (`claude/k1st-predicted`, a single-parent child of `D`) is the execution tree less the result
  note. Its files and blobs:
  - this preregistration in its drafting revision, blob `4a1dd702583deccf9c313598b9823278bc4f681b`, which differs from the revision at `F`
    only in this section;
  - `controls.py`, blob `8e7b8e03b427445a316cb334437c29a1a336896b`;
  - `SharpTests.lean`, blob `fd725b5e1a7296a4114a336419bf7e0d00f2d774`;
  - `OIBridge.lean`, blob `42959e8f27978fe85c50fe93ae7401ee180956b9`;
  - the census, blob `2349b962456b8decaef4870fb02889e859de97e0`.
- `delta(D, 2f386e5e)` is exactly those five paths: the record directory's two files and the three execution
  paths. The three execution paths are byte-identical to design run 1's commit `ece1aa89`.
- At that commit `controls.py check 2f386e5e`, run from the tree's own frozen `controls.py`, passes all 20
  checks, and `controls.py verdict 2f386e5e` prints exactly `K1-SHARP-TEST-MULTIPLICITY-CLASSIFIED` for the
  classification cell and `K1-TWO-LE-NOT-IMPLIED` for the non-implication cell.
- **Run 37501311098** (`workflow_dispatch` on `2f386e5e`, attempt 1) completed with conclusion success; every one of
  its 32 jobs succeeded. The Mathlib bridge (job 112398743722) built `OIBridge.SharpTests` with each of the 13 frozen
  `#print axioms` lines within `[propext, Classical.choice, Quot.sound]` and no warning in the module, and its release
  gate passed every step (`lean-axioms` 5775 named results, no `sorryAx`; `lean-manuscript` OK; 303 legacy records
  intact; 37 receipts hold); the Lean kernel check (job 112398743261) and the probe aggregate (job 112405061418)
  succeeded. Its facts agree with design run 1 at `ece1aa89`.

The predicted tree is a sibling of `F` on `D`, not an ancestor of `F`; it and these runs are design evidence, not
attestations.

## Stages

1. **C1** adds `controls.py`, blob `8e7b8e03b427445a316cb334437c29a1a336896b`, to the record directory. Acceptance: the blob is the
   frozen blob.
2. **S1** adds the module, the import line and the census family in one commit. Acceptance:
   - `controls.py check S1 --freeze F` passes;
   - the exact-head run at S1 has every job green, the Mathlib bridge building the module with every printed axiom set
     within `[propext, Classical.choice, Quot.sound]` and the release gate passing.
3. **Repairs**, if the build at S1 fails, change theorem proofs only; each passes `controls.py check` at its commit. A
   failure that a proof-only repair cannot fix halts the round.
4. **S2** adds the result note `result.md`; this is candidate `E`. Acceptance: `controls.py check E --freeze F` passes
   (the result note included in S7 and V) and the exact-head run at `E` has every job green.

## Outcomes

- **`K1-SHARP-TESTS-1-READ`** — `controls.py check E --freeze F` prints `controls: OK`, `controls.py verdict E` prints
  exactly one outcome for each cell, and the exact-head run at `E` is green on every job, the Mathlib bridge building
  `SharpTests` with every frozen `#print axioms` reporting a subset of `[propext, Classical.choice, Quot.sound]` and the
  release gate passing. The result note states each cell as its row words it, the earned reading, and the
  non-inference rule.
- **`K1-SHARP-TESTS-1-HALTED`** — anything else; the round halts under the specification's `S12`, and the result note
  names the failing check or job.

No outcome sources the predicate or `2 ≤ d`, adopts the predicate as a premise, or edits the ROADMAP. Correctness bands
are unchanged by either outcome: the round is consistency-axis work.
