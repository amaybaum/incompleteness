# Reconstruction round KTRANS-DENSE-1 — the consumers of K∞-Trans under a dense boundary orbit: PREREGISTRATION

**Status: candidate freeze.** This file is the control plane of a native round under `AGENTS.md` §A.39. It is drafted
on its pull request from `D` and is final only at the commit `F` the owner designates; no commit after `F` changes it.
The three questions, the three decision rules, the non-inference rule, the frozen surface, the controls, the evidence
ledger, the stages and the outcomes below are fixed; the predicted execution tree is recorded before `F`.

```v3-round
round KTRANS-DENSE-1
kind non-sealing
record-directory verification/programmes/oi-qm/reconstruction/round-ktrans-dense-1/
```

```v3-governed-paths
record AM verification/programmes/oi-qm/reconstruction/round-ktrans-dense-1/
record AM verification/receipts/KTRANS-DENSE-1.json
execution A verification/lean-mathlib/OIBridge/DenseOrbit.lean
execution M verification/lean-mathlib/OIBridge.lean
execution M verification/lean-manuscript-census.json
```

The record directory holds this preregistration, the round's frozen controls `controls.py` and the result note. The
receipt path is `verification/receipts/KTRANS-DENSE-1.json`. Every other path the round changes is an execution path
listed above. **No manuscript, no built artifact, `verification/ROADMAP.md`, the workflow, no probe, no landed kernel
module and no other round's record change under any outcome.**

## The objects

- **`D`** = `06b6f94e479bc19a28979c72316823cbdd0fb62b`, the head of `main` after round K1-SHARP-TESTS-1 landed (merge
  of `Q` `e0cf9151`; the push run 37517953987 at `D` succeeded, the act 42 exclusion matrix skipped on push).
- **`F`** — the commit carrying this file, which the owner designates; `delta(D, F)` is this file.
- **`E`** — the certified execution head, which the owner designates.
- **`Λ`**, **`Q`** — the reconciliation and the receipt commit, as §A.39 defines them.

## What the round is

OG-1's `BoundaryTransitive Ω G` (K∞-Trans) asks that a member of `G` carry any boundary state of `Ω` to any other. The
round weakens that operational hypothesis for the consumers that read it only through a closed condition, and leaves
the ontology, the other hypotheses and every landed statement unchanged.

`DenseBoundaryOrbit Ω G` is `BoundaryTransitive Ω G` with its last clause `∃ g ∈ G, g x = y` replaced by
`y ∈ closure ((fun g => g x) '' G)`: every boundary state lies in the closure of the orbit of every boundary state. It
is stated over OG-1's carrier context (`{V : Type} [NormedAddCommGroup V] [NormedSpace ℝ V]`). The round asks three
independent questions, each read from the kernel statements (and, for the pairing, the landed statements at `D`) by
its own frozen decision rule. No rule reads another cell's statements, and no outcome depends on another.

- **Q-BALL.** Do TRB-1's ball theorems — the invariant form constant on the boundary, the centroid interior, the body
  the closed invariant-form ball, the body an affine image of `eball d`, and the completion chart's body an affine image
  of `eball d` — hold with `DenseBoundaryOrbit` in place of `BoundaryTransitive` and no other change to their effective
  statements?
- **Q-CONE.** Do EFF-1's cone equality `maxConeOf avail = maxCone (eball d)`, K1-BRIDGE-1's two transports and two
  relative selectors, and K2-GUARD-1's relative selector with `2 ≤ d` hold with the same single replacement?
- **Q-STRICT.** Is `DenseBoundaryOrbit` strictly weaker than `BoundaryTransitive`: does boundary transitivity imply a
  dense boundary orbit, and is there a body-preserving family on `eball 3` with a dense boundary orbit that is not
  boundary transitive?

The earned reading of the three positive cells together is only this: on the consumers listed, a dense boundary orbit
suffices wherever boundary transitivity was assumed, and it is a strictly weaker hypothesis. The dense route is
sufficient only for the eleven consumers of the pairing table; every other statement that takes boundary transitivity
keeps it.

### The decision rules (frozen; implemented by `controls.py verdict`)

The **effective statement** of a theorem is the bracketed binder groups of its section `variable` lines that the
statement uses (closed under use by the groups already included; an instance group is included with a variable it
mentions), in declared order, followed by its own binders and conclusion, whitespace-normalized.

| Cell | Outcome | Rule |
|---|---|---|
| Q-BALL | `KTRANS-DENSE-BALL-PROVED` | all of: `DenseBoundaryOrbit` passes S1; `denseBoundaryOrbit_of_boundaryTransitive` has exactly the binders `{V : Type} [NormedAddCommGroup V] [NormedSpace ℝ V] {Ω : Set V} {G : Set (V ≃ᵃ[ℝ] V)} (hT : BoundaryTransitive Ω G)` and the conclusion `DenseBoundaryOrbit Ω G`; and each of the five ball rows of the pairing table is a theorem whose effective statement is the effective statement of its landed partner, read from `D`, with its single `BoundaryTransitive` replaced by `DenseBoundaryOrbit` and nothing else |
| Q-BALL | `KTRANS-DENSE-BALL-NOT-ESTABLISHED` | otherwise |
| Q-CONE | `KTRANS-DENSE-CONE-PROVED` | all of: `DenseBoundaryOrbit` passes S1; and each of the six cone and selector rows of the pairing table pairs with its landed partner read from `D` as above |
| Q-CONE | `KTRANS-DENSE-CONE-NOT-ESTABLISHED` | otherwise |
| Q-STRICT | `KTRANS-DENSE-STRICTLY-WEAKER` | all of: `DenseBoundaryOrbit` passes S1; the weakening `denseBoundaryOrbit_of_boundaryTransitive` has the binders and conclusion of the Q-BALL row; `ratRefl` is the frozen definition; each theorem of the strictness table has its frozen conclusion, no explicit binders, and names its frozen proof dependencies; and EFF-1's `not_boundaryTransitive_of_countable` at `D` has the effective statement `{G : Set ((Fin 3 → ℝ) ≃ᵃ[ℝ] (Fin 3 → ℝ))} (hG : G.Countable) : ¬ BoundaryTransitive (eball 3) G` |
| Q-STRICT | `KTRANS-DENSE-STRICTLY-WEAKER-NOT-ESTABLISHED` | otherwise |

S1 is shared by all three cells, and the weakening by Q-BALL and Q-STRICT; each cell reads them itself, so no cell's
outcome depends on another's. Q-STRICT reads the weakening as well as the strictness witness, so the cell by itself
establishes both directions of the strict relation: boundary transitivity implies a dense boundary orbit, and the
rational reflections give a dense boundary orbit on `eball 3` without boundary transitivity.

The round's outcome is `KTRANS-DENSE-1-READ` when all three cells are assigned, each by its own rule. The design run
below already exhibits a module read by these rules as `KTRANS-DENSE-BALL-PROVED`, `KTRANS-DENSE-CONE-PROVED` and
`KTRANS-DENSE-STRICTLY-WEAKER`; the rules, not that reading, are what this file freezes, and the cells at `E` are those
`controls.py verdict E` prints.

### The pairing table (frozen)

Each dense theorem's effective statement is its landed partner's with the single replacement. The landed effective
statements read from `D` are embedded in `controls.py` and compared at every check.

| Cell | Dense theorem | Landed partner at `D` |
|---|---|---|
| Q-BALL | `boundary_qnorm_const_of_dense` | TRB-1 `TransitiveBody.boundary_qnorm_const` |
| Q-BALL | `centroid_mem_interior_of_dense` | TRB-1 `TransitiveBody.centroid_mem_interior` |
| Q-BALL | `eq_qBall_of_dense` | TRB-1 `TransitiveBody.eq_qBall_of_boundaryTransitive` |
| Q-BALL | `exists_affine_image_eq_eball_of_dense` | TRB-1 `TransitiveBody.exists_affine_image_eq_eball` |
| Q-BALL | `chartBody_eq_eball_of_dense` | TRB-1 `TransitiveBody.chartBody_eq_eball` |
| Q-CONE | `maxConeOf_avail_eq_of_dense` | EFF-1 `EffectSpace.maxConeOf_avail_eq` |
| Q-CONE | `nativeGate_of_avail_dense` | K1-BRIDGE-1 `K1Bridge.nativeGate_of_avail` |
| Q-CONE | `entangling_of_avail_dense` | K1-BRIDGE-1 `K1Bridge.entangling_of_avail` |
| Q-CONE | `dim_of_nativeGateOf_dense` | K1-BRIDGE-1 `K1Bridge.dim_of_nativeGateOf` |
| Q-CONE | `three_of_nativeGateOf_dense` | K1-BRIDGE-1 `K1Bridge.three_of_nativeGateOf` |
| Q-CONE | `three_of_nativeGateOf_of_two_le_dense` | K2-GUARD-1 `K2Guard.three_of_nativeGateOf_of_two_le` |

The mathematical content: TRB-1 reads boundary transitivity to make the invariant form of the displacement from the
centroid constant on the boundary and to put the centroid in the interior; both hold under a dense boundary orbit
because the invariant form is continuous and the centroid's orbit is a single point. EFF-1 reads it to make every sharp
effect available; under a dense boundary orbit the available sharp directions are dense in the sphere and the pairing of
a joint vector with two sharp effects is continuous in the two directions, so the available family still determines
`maxCone (eball d)`. K1-BRIDGE-1 and K2-GUARD-1 read boundary transitivity only through that cone equality.

### The strictness (frozen statements)

| Item | Theorem or definition | Frozen statement | Proof names |
|---|---|---|---|
| weakening | `denseBoundaryOrbit_of_boundaryTransitive` | binders and conclusion of the Q-BALL row | — |
| family | `ratRefl d` | `insert (AffineEquiv.refl ℝ (Fin d → ℝ)) (Set.range fun q : {q : Fin d → ℚ // ∑ j, ((q j : ℝ)) ^ 2 ≠ 0} => @reflAff d (fun j => (q.1 j : ℝ)) q.2)` | — |
| countable | `countable_ratRefl` | `(ratRefl d).Countable` | — |
| automorphisms | `ratRefl_subset_fullAut`, `preservesBody_ratRefl` | `ratRefl d ⊆ fullAut d`; `PreservesBody (eball d) (ratRefl d)` | — |
| dense orbit | `denseBoundaryOrbit_ratRefl` | `DenseBoundaryOrbit (eball d) (ratRefl d)` | — |
| not transitive | `not_boundaryTransitive_ratRefl` | `¬ BoundaryTransitive (eball 3) (ratRefl 3)` | `not_boundaryTransitive_of_countable`, `countable_ratRefl` |
| countable tests | `countable_seedOrbit_cone` | `(seedOrbit (ratRefl 3) (sharpEff (axisVec _))).Countable ∧ maxConeOf (seedOrbit (ratRefl 3) (sharpEff (axisVec _))) = maxCone (eball 3)` | `countable_ratRefl`, `denseBoundaryOrbit_ratRefl` |

`ratRefl d` is the identity with the reflections `reflAff` in the hyperplanes orthogonal to nonzero rational vectors.
The non-transitivity is EFF-1's countable no-go applied to it. `countable_seedOrbit_cone` shows the weakening is not
only topological: a countable family of tests, the seed orbit of the axis test under `ratRefl 3`, already determines
the product-test cone.

### The non-inference rule (frozen)

> This round does not show that OI, StageCompletion or the observer architecture yields a dense boundary orbit or
> boundary transitivity; adopts no premise; introduces no principle of closure of the operations; does not concern
> whether the composite cone is closed. The statements that need a specific effect to exist exactly keep exact boundary transitivity:
> EFF-1's `sharpFamily_subset_avail`, `sharpFamily_subset_seedOrbit`, `seedOrbit_eq_sharpFamily`, the first
> conjunct of `cone_of_orbit`, `fullEffects_subset_avail` and `avail_eq_fullEffects`; OG-1's
> `coversBoundaryFrom_of_transitive`, `supportingEffectComplete_of_sharp_transitive`, `seedOrbit_ball3_eq`,
> `ballEffect_mem_avail`, `supportingEffectComplete_ball3_of_orbit` and `kInf1_ball3_of_orbit`; and
> `OrbitNormalization.seedOrbit_eq_of_normalization`. Three statements are not covered and keep exact boundary
> transitivity: OG-1's `lorentz_of_seedOrbit` and `lorentz_of_available`, and TRB-1's
> `extreme_of_isBoundaryState_of_transitive`. `ratRefl` is a mathematical control, not an adopted family of
> operations. The round makes no manuscript claim and no ROADMAP claim.

The result note states each cell in the words of its row, the earned reading above, the uncovered statements by name,
and nothing stronger.

### In scope
- the module `OIBridge/DenseOrbit.lean` with the statement surface of §"The frozen surface";
- its import line in `OIBridge.lean` and its family in `lean-manuscript-census.json`;
- `controls.py` and the result note.

### Frozen out
- any dense form of an exact-existence statement or of the three uncovered statements;
- any source of `DenseBoundaryOrbit` or `BoundaryTransitive`; any operation-closure principle; any statement that the
  composite cone is closed;
- any edit to `TransitiveBody`, `EffectSpace`, `OrbitGeneration`, `K1Bridge`, `K2Guard` or any other landed module, a
  manuscript, `verification/ROADMAP.md`, or any other round's record.

## The frozen surface

**Design-run rule:** compilation failures may cause implementation repairs, but no repair may strengthen or weaken a
frozen theorem statement, definition or hypothesis without a new preregistration revision and new design theorem
identity. A statement mismatch found by a control returns the round to design; it is never repaired during execution.

The design theorem identity is the statement surface of `DenseOrbit` embedded in `controls.py` (blob
`62d66fd6bb08668b2389b682965bda9589575a10`): the preamble (the import, the namespaces and the two `open` lines), the
context blocks in order, the 24 declarations in order and by kind, every theorem's signature up to `:=`, every
definition whole, and the 15 `#print axioms` lines. The reference module is blob
`466a80f7ec2fa8089be59760f5c26e5d37a09973`. A repair may change theorem proofs only. `OIBridge.lean` is `D`'s with
`import OIBridge.DenseOrbit` inserted directly after `import OIBridge.SharpTests`. The census is `D`'s with one family,
embedded in `controls.py`, inserted directly after the K1-SHARP-TESTS-1 family (modules `["SharpTests"]`), in `D`'s
two-space JSON layout.

### Semantic guards (in `controls.py`)

Each lists the mutation controls `--self-test` drives through it, every one of which must fail with the named code.

- **S1 definition.** `DenseBoundaryOrbit` has the effective header of the landed `OrbitGeneration.BoundaryTransitive`
  read from `D`, and its body is the landed body with exactly the last clause replaced. Mutations: the orbit closure
  replaced by the orbit itself; by the orbit's interior.
- **S2 pairing** (load-bearing). For each of the eleven rows of the pairing table, the landed partner at `D` has
  exactly one `BoundaryTransitive` in its effective statement, the dense theorem's effective statement equals that text
  with the replacement and nothing else, and the dense statement does not mention `BoundaryTransitive`; at check time,
  the landed effective statements read from `D` equal the embedded ones. Mutations: a ball conclusion changed
  (`0 ≤ R` to `0 < R`); a ball hypothesis added; a dense theorem keeping exact transitivity; both hypotheses carried; a
  cone hypothesis dropped; the cone conclusion weakened to an inclusion; a selector conclusion changed; a section
  variable added under the cone theorems; the chart theorem's completion data made implicit; a landed statement that
  differs from the dense one fails the pair (and only the cone cell); a landed statement differing outside the
  hypothesis fails the pair.
- **S3 resolution.** Every identifier of a paired effective statement that names an OIBridge declaration resolves, in
  the dense module's namespace context (its namespaces and `open` lines), to the same unique declaration as in the
  landed partner's context; `DenseBoundaryOrbit` resolves to the module's own definition, and the landed
  `BoundaryTransitive` to OG-1's. The inventory is every OIBridge module at `D` together with the module under check.
  Mutations: `InvariantInnerProduct` and `TransitiveBody` dropped from the `open` line (`qnorm`, `centroid` and
  `qBall` no longer resolve as in TRB-1); a local `eball` shadowing the landed one. Identifiers that name no OIBridge
  declaration (Mathlib and core: `Set`, `Fin`, `IsCompact`, `Convex`, `interior`) are compared as text and resolved by
  the Lean build; the controls do not resolve them.
- **S4 strict.** The weakening and the strictness table with their frozen statements and proof names; EFF-1's no-go at
  `D` with its frozen statement. Mutations: the weakening reversed; the non-transitivity proved without EFF-1's no-go;
  the family enlarged; the witness moved to `d = 2`; a different landed no-go fails only the strictness cell.
- **S5 scope.** No statement of the module mentions an exact-existence or uncovered object (`sharpFamily`,
  `sharpUnitFamily`, `fullEffects`, `MixingClosed`, `unitEff`, `SupportingEffectComplete`, `KInf1`,
  `CoversBoundaryFrom`, `conePair`, `ballEffect`, `ball3`, `extremePoints`, `Lorentz`, `lorentz_of_effects`,
  `lorentz_of_seedOrbit`, `lorentz_of_available`, `extreme_of_isBoundaryState_of_transitive`); `ratRefl` occurs only in
  §D. Mutations: a sharp-family statement; a Lorentz-bridge statement; `ratRefl` in §C.
- **S6 reuse.** No declaration of the module shares its name with an OIBridge declaration visible to it; the only
  import is `OIBridge.K2Guard`. Mutations: `fullAut` re-declared; a second import.
- **S7 phrases.** The module header and, at a commit carrying it, the result note contain none of the frozen phrases
  (among them "closure of operations", "operation closure", "closed under operations", "operationally closed", "OI
  supplies", "OI provides", "derived from OI", "sourced from OI", "K∞-Trans is derived", "replaces K∞-Trans", "K∞-Trans
  is not needed", "every consumer", "all consumers", "composite closedness", "adopted operation", "physical
  operations", "premise adopted", "design (round", "not for landing"; case-insensitive, whitespace-normalized).
  Mutations: "This replaces K∞-Trans." in the header; the design header; a note with "closed under operations" (and a
  neutral note passes).
- **S8 separation.** No declaration of §B (the ball) mentions a cone or selector object; no declaration of §A–§C
  mentions `ratRefl`. Mutation: `maxCone` in §B.
- **S9 count.** Exactly the 15 frozen `#print axioms` lines, in order and distinct. Mutations: an extra print; a
  duplicated print.
- **V verdicts.** Each cell yields one outcome by its own rule; at a commit carrying the result note, the note contains
  exactly the three computed tokens and no other. Controls: a broken ball pair reads `KTRANS-DENSE-BALL-NOT-ESTABLISHED`
  and leaves the other cells positive; a broken cone pair reads `KTRANS-DENSE-CONE-NOT-ESTABLISHED` and leaves the
  others positive; a broken strictness witness reads `KTRANS-DENSE-STRICTLY-WEAKER-NOT-ESTABLISHED` and leaves the
  others positive; the weakening broken reads not-established in Q-BALL and Q-STRICT and leaves Q-CONE positive; the
  definition broken reads not-established in all three; the note-token reader finds exactly the stated tokens.
- **N1–N3** as K1-SHARP-TESTS-1. **I, C** as K1-SHARP-TESTS-1, with the import after `OIBridge.SharpTests` and the
  family after K1-SHARP-TESTS-1's.

`controls.py`:
- is blob `62d66fd6bb08668b2389b682965bda9589575a10` (1223 lines), generated from the reference module, the frozen
  family and `D` by the round's generator;
- was frozen, and this revision committed, before any outcome of the predicted execution tree was read;
- `--self-test` passes 63 checks.

### Count facts

- the module carries **15** frozen `#print axioms` lines (S9) and 24 declarations;
- none of the 15 short names occurs in a `#print axioms` line at `D`, so the prints add 15 names to
  `lean_axiom_check`'s count;
- at `D` the release gate's `lean-axioms` step reports 5775 named results.

## Evidence ledger

Each row is discharged at `E` by the exact-head run at `E` and by `controls.py check E --freeze F`.

| Row | Kernel identifiers | Evidence required at `E` | Control |
|---|---|---|---|
| definition and weakening | `DenseBoundaryOrbit`, `denseBoundaryOrbit_of_boundaryTransitive` | the frozen definition; built, axioms within `[propext, Classical.choice, Quot.sound]` | S1, S4, V |
| ball | the five Q-BALL rows | as above | S2, S3, V |
| cone and selectors | the six Q-CONE rows | as above | S2, S3, V |
| strictness | `denseBoundaryOrbit_ratRefl`, `not_boundaryTransitive_ratRefl`, `countable_seedOrbit_cone` | as above | S4, V |
| scope | the module's statements | no exact-existence or uncovered object | S5, S8 |
| count | the 15 prints | each within the three axioms; `lean-axioms` passes | S9 |

## Design evidence

Design runs on the certified base `D` (`workflow_dispatch` on the disposable branch `claude/kdense-dev`; the Mathlib
bridge job and the release gate read):

| Run | Commit (module blob) | Workflow run | Result |
|---|---|---|---|
| 1 | `302d393d` (`e67a72fd`) | 37550951482 | **failed**: heartbeat timeout in `maxConeOf_avail_eq_of_dense`; repaired in proof only (a `set` abbreviation removed, an explicit `show`, a lemma renamed to `continuous_finsetSum`) |
| 2 | `e2f7b3a3` (`ebf9edaf`) | 37552392804 | **failed**: a `dsimp` made no progress in one proof; removed (proof only) |
| 3 | `bdbaabb9` (`7ca88387`) | 37553717564 | **green**: all 32 jobs `success`; the eleven prints of that revision within `[propext, Classical.choice, Quot.sound]`; release gate PASS (`lean-axioms` 5786) |
| 4 | `7d53f82b` (`91f5aa50`) | 37555310752 | **green**: all 32 jobs `success`; adds the four K1-BRIDGE-1 rows (`nativeGate_of_avail_dense`, `entangling_of_avail_dense`, `dim_of_nativeGateOf_dense`, `three_of_nativeGateOf_dense`), one-line theorems through `maxConeOf_avail_eq_of_dense`; the Mathlib bridge (job 112580071653) built `OIBridge.DenseOrbit` with each of the 15 `#print axioms` lines within `[propext, Classical.choice, Quot.sound]` and no warning in the module; release gate PASS (`lean-axioms` 5790, no `sorryAx`; `lean-manuscript` OK; 303 legacy records intact; 38 receipts hold); the Lean kernel check (job 112580071664) and the probe aggregate (job 112584267287) succeeded |

No statement changed across runs 1–4; run 4 added four statements. Run 4 is the design evidence for the frozen
statement surface. The reference module differs from run 4's only in the header comment (the round's name, the
weakening named under (C), and the uncovered statements named), and the census family differs from run 4's design
family only in its text; the predicted execution tree below is the evidence for the frozen blobs.

Statement-level choices recorded as frozen: `DenseBoundaryOrbit` is stated over OG-1's carrier context and is
`BoundaryTransitive` with its last clause replaced; each dense theorem keeps its landed partner's binder names; the
chart theorem states its completion data explicitly where TRB-1 takes them from a section `variable`, which leaves the
effective statement unchanged; the strictness witness is at `d = 3`, where EFF-1's countable no-go is stated.

### The predicted execution tree

@@PREDICTED@@

The predicted tree is a sibling of `F` on `D`, not an ancestor of `F`; it and these runs are design evidence, not
attestations.

## Stages

1. **C1** adds `controls.py`, blob `62d66fd6bb08668b2389b682965bda9589575a10`, to the record directory. Acceptance: the
   blob is the frozen blob.
2. **S1** adds the module, the import line and the census family in one commit. Acceptance:
   - `controls.py check S1 --freeze F` passes;
   - the exact-head run at S1 has every job green, the Mathlib bridge building the module with every printed axiom set
     within `[propext, Classical.choice, Quot.sound]` and the release gate passing.
3. **Repairs**, if the build at S1 fails, change theorem proofs only; each passes `controls.py check` at its commit. A
   failure that a proof-only repair cannot fix halts the round.
4. **S2** adds the result note `result.md`; this is candidate `E`. Acceptance: `controls.py check E --freeze F` passes
   (the result note included in S7 and V) and the exact-head run at `E` has every job green.

## Outcomes

- **`KTRANS-DENSE-1-READ`** — `controls.py check E --freeze F` prints `controls: OK`, `controls.py verdict E` prints
  exactly one outcome for each cell, and the exact-head run at `E` is green on every job, the Mathlib bridge building
  `DenseOrbit` with every frozen `#print axioms` reporting a subset of `[propext, Classical.choice, Quot.sound]` and the
  release gate passing. The result note states each cell as its row words it, the earned reading, the uncovered
  statements, and the non-inference rule.
- **`KTRANS-DENSE-1-HALTED`** — anything else; the round halts under the specification's `S12`, and the result note
  names the failing check or job.

No outcome sources a dense boundary orbit or boundary transitivity, adopts either as a premise, or edits the ROADMAP.
Correctness bands are unchanged by either outcome: the round is consistency-axis work.
