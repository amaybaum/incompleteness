# Reconstruction round PARITY-NOT-1 — DIM-1's parity count from the gate relations, the NOT at d = 3, and forward positivity as a separate condition: PREREGISTRATION

**Status: candidate freeze.** This file is the control plane of a native round under `AGENTS.md` §A.39. It is drafted
on its pull request from `D` and is final only at the commit `F` the owner designates; no commit after `F` changes it.
The three questions, the three decision rules, the non-inference rule, the frozen surface, the controls, the evidence
ledger, the stages and the outcomes below are fixed; the predicted execution tree is recorded before `F`.

```v3-round
round PARITY-NOT-1
kind non-sealing
record-directory verification/programmes/oi-qm/reconstruction/round-parity-not-1/
```

```v3-governed-paths
record AM verification/programmes/oi-qm/reconstruction/round-parity-not-1/
record AM verification/receipts/PARITY-NOT-1.json
execution A verification/lean-mathlib/OIBridge/ParityNot.lean
execution M verification/lean-mathlib/OIBridge.lean
execution M verification/lean-manuscript-census.json
```

The record directory holds this preregistration, the round's frozen controls `controls.py` and the result note. The
receipt path is `verification/receipts/PARITY-NOT-1.json`. Every other path the round changes is an execution path
listed above. **No manuscript, no built artifact, `verification/ROADMAP.md`, the workflow, no probe, no landed kernel
module and no other round's record change under any outcome.**

## The objects

- **`D`** = `e26493394f388a891c2dd03be2696286a89293f7`, the head of `main` after round KTRANS-DENSE-1 landed (merge of
  `Q` `3b966b5d`; the push run 37584359361 at `D` succeeded, the act 42 exclusion matrix skipped on push).
- **`F`** — the commit carrying this file, which the owner designates; `delta(D, F)` is this file.
- **`E`** — the certified execution head, which the owner designates.
- **`Λ`**, **`Q`** — the reconciliation and the receipt commit, as §A.39 defines them.

## What the round is

DIM-1's `NativeGate Ω z N G` has five clauses: the frame `frame`, forward and inverse positivity `posFwd` and `posInv`,
the target relation `relT` and the control relation `relC`. From all five together with `IsNot (eball d) z N`, DIM-1
proves the parity count `finrank_plus_eq_finrank_minus`, the exclusion of even `d` (`not_even_of_nativeGate`) and the
selector `dim_of_nativeGate` (`d = 1 ∨ d = 3`). The round separates the clauses those conclusions read, and leaves
every landed statement unchanged.

`GateRel N G` is the structure whose fields are exactly `NativeGate`'s `relT` and `relC`, read from `D`. The round asks
three independent questions, each read from the kernel statements (and, for the pairings, the landed statements at `D`)
by its own frozen decision rule. No rule reads another cell's statements, and no outcome depends on another.

- **Q-REL.** Do DIM-1's parity count and its exclusion of even `d` hold from `IsNot (eball d) z N` and `GateRel N G`
  alone?
- **Q-NOT.** At `d = 3`, do `IsNot (eball 3) z N` and `GateRel N G` alone determine the NOT: both eigenspaces of the
  homogenized NOT of dimension two, the fixed space of `N` of dimension one, `N` the rotation by `π` about a unit axis,
  and `det N = 1` — with the reflection `diag(1, 1, −1)` and `−id` excluded and DIM-1's `cnot` with `nflip` a positive
  control?
- **Q-SEP.** Is forward positivity a condition the frame and the two relations do not supply: at `d = 3` and at `d = 5`,
  is there a gate satisfying `NativeGate`'s frame and `GateRel` whose image of an explicit pure product pairs negatively
  with two sharp effects?

The earned reading of the three positive cells together is only this: the two relations give the parity count and the
oddness of `d`, and at `d = 3` they determine the NOT as a rotation by `π` of determinant one; forward positivity is not
supplied by the frame and the relations, at `d = 3` and at `d = 5`. The round does not show that the relations together
with positivity select `d = 3` among odd dimensions; DIM-1's `dim_of_nativeGate` is the landed selector and the round
neither restates nor extends it.

### The decision rules (frozen; implemented by `controls.py verdict`)

The **effective statement** of a theorem is the bracketed binder groups of its section `variable` lines that the
statement uses (closed under use by the groups already included; an instance group is included with a variable it
mentions), in declared order, followed by its own binders and conclusion, whitespace-normalized.

| Cell | Outcome | Rule |
|---|---|---|
| Q-REL | `PARITY-FROM-RELATIONS-PROVED` | all of: `GateRel` passes S1; each row of the parity table is a theorem whose effective statement is its landed partner's, read from `D`, with the hypothesis `(hG : NativeGate (eball d) z N G)` replaced by `(hR : GateRel N G)` and nothing else; and no declaration of §A other than `GateRel` and `gateRel_of_nativeGate` mentions `NativeGate`, `posFwd`, `posInv`, `frame`, `maxCone`, `prodEffVal`, `IsEffectOn`, `prodState` or `corner` in its statement or proof |
| Q-REL | `PARITY-FROM-RELATIONS-NOT-ESTABLISHED` | otherwise |
| Q-NOT | `D3-NOT-PI-ROTATION-PROVED` | all of: `GateRel` passes S1; each row of the `d = 3` table has exactly the binders `{z : Fin 3 → ℝ} {N : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)} {G : W 3 ≃ₗ[ℝ] W 3} (hN : IsNot (eball 3) z N) (hR : GateRel N G)` and its frozen conclusion; `det_eq_one_of_piRotation` has its frozen statement and `det_three` is proved through it and `piRotation_three`; each `NativeGate` corollary has the same binders with `(hG : NativeGate (eball 3) z N G)` in place of `hR`, the conclusion of its `GateRel` theorem, and is proved through `gateRel_of_nativeGate` and that theorem; no declaration of §B other than the three corollaries mentions any object of the Q-REL list; and every row of the control table holds |
| Q-NOT | `D3-NOT-PI-ROTATION-NOT-ESTABLISHED` | otherwise |
| Q-SEP | `POSITIVITY-SEPARATION-PROVED` | all of: `GateRel` passes S1; the definitions of the separation table are the frozen ones; and for each of `d = 3` and `d = 5`: the frame theorem has the binders `(a b : Fin 2)` and the conclusion of `NativeGate`'s `frame` field read from `D` with `G` and `z` instantiated at the gate and the axis; the relation theorem concludes `GateRel` of the NOT and the gate; the value theorem concludes the frozen pairing `= -1 / 10`; the non-membership theorem is proved through the value theorem and `sharpEff_isEffectOn`; the positivity theorem concludes `¬` of `NativeGate`'s `posFwd` field read from `D` with `Ω` and `G` instantiated at the body and the gate, and is proved through the non-membership theorem; and no declaration of §D–§F names a landed dimension corollary of the native gate (`*_of_nativeGate*`, `three_of_*`, `dim_of_*`) |
| Q-SEP | `POSITIVITY-SEPARATION-NOT-ESTABLISHED` | otherwise |

S1 is shared by all three cells, and each cell reads it itself, so no cell's outcome depends on another's. The Q-SEP
rule reads the `d = 5` witness directly: a positivity failure at `d = 5` derived from DIM-1's `ne_five_of_nativeGate`
or any other landed dimension corollary does not satisfy it.

The round's outcome is `PARITY-NOT-1-READ` when all three cells are assigned, each by its own rule. The design runs
below already exhibit a module read by these rules as `PARITY-FROM-RELATIONS-PROVED`, `D3-NOT-PI-ROTATION-PROVED` and
`POSITIVITY-SEPARATION-PROVED`; the rules, not that reading, are what this file freezes, and the cells at `E` are those
`controls.py verdict E` prints.

### The parity table (frozen)

| Theorem | Landed partner at `D` |
|---|---|
| `finrank_plus_eq_finrank_minus_rel` | DIM-1 `CompositeDimension.finrank_plus_eq_finrank_minus` |
| `not_even_of_gateRel` | DIM-1 `CompositeDimension.not_even_of_nativeGate` |

The landed effective statements read from `D` are embedded in `controls.py` and compared at every check. Every
OIBridge identifier of a paired statement resolves to the same unique declaration in the module's namespace context as
in DIM-1's (S2). `GateRel N G` has the header `(N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (G : W d ≃ₗ[ℝ] W d) : Prop` and
exactly the fields `relT : ∀ ω, actT N (G (actT N ω)) = G ω` and `relC : ∀ ω, actC N (G (actC N ω)) = actT N (G ω)`,
each textually `NativeGate`'s field at `D`; `gateRel_of_nativeGate` projects them.

The mathematical content: DIM-1's parity argument builds an injective linear map between operator spaces that
anticommutes with the homogenized NOT. Its commutation with the NOT on the right reads only `relT`, and on the left only
`relC`; the frame and positivity are not read. The map then makes the `+1` and `−1` eigenspaces of the homogenized NOT
equal in dimension, and since they sum to `d + 1`, `d` is odd.

### The `d = 3` table (frozen)

| Theorem | Frozen conclusion |
|---|---|
| `finrank_plus_minus_three` | `Module.finrank ℝ (plusSpace N) = 2 ∧ Module.finrank ℝ (minusSpace N) = 2` |
| `tangentPlus_three` | `tangentPlus N = 1` |
| `piRotation_three` | `∃ u : Fin 3 → ℝ, ∑ j, u j ^ 2 = 1 ∧ ∀ x, N x = (2 * ∑ j, u j * x j) • u - x` |
| `det_three` | `LinearMap.det N = 1` |
| `det_eq_one_of_piRotation` | binders `{N : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)} {u : Fin 3 → ℝ} (hu : ∑ j, u j ^ 2 = 1) (hN : ∀ x, N x = (2 * ∑ j, u j * x j) • u - x)`; conclusion `LinearMap.det N = 1` |
| `tangentPlus_of_nativeGate_three`, `piRotation_of_nativeGate_three`, `det_of_nativeGate_three` | the conclusions of `tangentPlus_three`, `piRotation_three`, `det_three` |

The mathematical content: at `d = 3` the parity count makes both eigenspaces of the homogenized NOT two-dimensional, so
the fixed space of `N` is a line. `N` is an involutive isometry of the ball (DIM-1's `dot_apply`), so `x + N x` lies on
that line for every `x`, which gives `N x = 2 (u · x) u − x` for a unit vector `u` on it, a rotation by `π`, and its
determinant is one.

### The control table (frozen)

| Item | Declaration | Frozen statement | Proof names |
|---|---|---|---|
| diagonal map | `diagSign` | `toFun x := fun i => c i * x i` | — |
| reflection | `refl3` | `diagSign ![1, 1, -1]` | — |
| minus identity | `negId3` | `diagSign ![-1, -1, -1]`; `negId3_eq : negId3 = -LinearMap.id` | — |
| both are NOTs | `isNot_refl3`, `isNot_negId3` | `IsNot (eball 3) z3 refl3`; `IsNot (eball 3) z3 negId3` | — |
| no relations | `not_gateRel_refl3`, `not_gateRel_negId3` | `(G : W 3 ≃ₗ[ℝ] W 3) : ¬ GateRel refl3 G`; `(G : W 3 ≃ₗ[ℝ] W 3) : ¬ GateRel negId3 G` | `finrank_plus_minus_three` |
| determinants | `det_refl3`, `det_negId3` | `LinearMap.det refl3 = -1`; `LinearMap.det negId3 = -1` | — |
| positive control | `gateRel_cnot` | `GateRel nflip cnot` | `cnot_relT`, `cnot_relC` |

DIM-1's `cnot_relT` and `cnot_relC` at `D` have the effective statements `(ω : W 3) : actT nflip (cnot (actT nflip ω))
= cnot ω` and `(ω : W 3) : actC nflip (cnot (actC nflip ω)) = actT nflip (cnot ω)`. The reflection has a one-dimensional
`−1` eigenspace and `−id` a one-dimensional `+1` eigenspace, so neither meets the count of `finrank_plus_minus_three`.

### The separation table (frozen)

| Item | `d = 3` | `d = 5` |
|---|---|---|
| gate | `gJ3 := sgateEquiv odd3 perm3 perm3_perm3` | `gJ5 := sgateEquiv odd5 perm5 perm5_perm5` |
| NOT, axis | `nflip`, `z3` (DIM-1) | `n5 := diagSign c5`, `c5 j := if odd5 j.succ then -1 else 1`, `z5 := fun i => if i = 4 then 1 else 0`; `isNot_n5 : IsNot (eball 5) z5 n5` |
| first state | `xplus` (DIM-1) | `x5 := fun i => if i = 0 then 1 else 0` |
| first effect direction | `w3 := ![0, -3 / 5, -4 / 5]` | `w5 := fun i => if i = 2 then -3 / 5 else if i = 4 then -4 / 5 else 0` |
| frame | `gJ3_frame (a b : Fin 2)` | `gJ5_frame (a b : Fin 2)` |
| relations | `gateRel_gJ3 : GateRel nflip gJ3` | `gateRel_gJ5 : GateRel n5 gJ5` |
| value | `gJ3_value : prodEffVal (sharpEff w3) (sharpEff z3) (gJ3 (prodState xplus z3)) = -1 / 10` | `gJ5_value : prodEffVal (sharpEff w5) (sharpEff z5) (gJ5 (prodState x5 z5)) = -1 / 10` |
| positivity fails | `not_posFwd_gJ3 : ¬ ∀ x ∈ eball 3, ∀ y ∈ eball 3, gJ3 (prodState x y) ∈ maxCone (eball 3)` | `not_posFwd_gJ5 : ¬ ∀ x ∈ eball 5, ∀ y ∈ eball 5, gJ5 (prodState x y) ∈ maxCone (eball 5)` |
| not native | `not_nativeGate_gJ3 : ¬ NativeGate (eball 3) z3 nflip gJ3` | `not_nativeGate_gJ5 : ¬ NativeGate (eball 5) z5 n5 gJ5` |

`sgate odd p ω` is `fun μ ν => if odd ν then ω (p μ) ν else ω μ ν`: the identity on the target columns of even sign and
the involution `p` of the control index on the others. `odd3` is `false, false, true, true` and `perm3` exchanges `0 ↔ 3`
and `1 ↔ 2`; `odd5` is `false, false, false, true, true, true` and `perm5` exchanges `0 ↔ 5`, `1 ↔ 3`, `2 ↔ 4`. Each
involution exchanges the two signs, which is what the control relation needs. At `d = 5` the balanced count
`finrank_plus_eq_finrank_minus_n5` follows from `GateRel n5 gJ5` through `finrank_plus_eq_finrank_minus_rel`.

The values: the image of the product of the first axis with the corner has the joint entries `1/4` at `(0, 0)` and at
`(first, 0)`, and `1/4` at `(odd row, corner)` and `(corner, corner)`, the sign-free gate moving the corner column; the
sharp effect vectors are `(1/2, w/2)` and `(1/2, z/2)`, and the pairing is `1/4 − 3/20 − 4/20 = −1/10`.

### The non-inference rule (frozen)

> This round does not select a dimension: it does not show that the relations, alone or with positivity, give `d = 3`
> among odd dimensions, and it neither restates nor extends DIM-1's `dim_of_nativeGate`. It concerns no complex
> structure and gives no interpretation of `J²`; `J² = −1` holds for DIM-1's classical `d = 1` gate as well and does not
> discriminate. It concerns no NOT carried by a physical theory: `refl3`, `negId3`, `gJ3`, `gJ5` and `n5` are
> mathematical controls and witnesses. It does not claim that `d = 5` is the only dimension above three at which the
> relations hold without positivity, nor that every odd dimension carries such a gate. It adopts no premise, and makes
> no manuscript claim and no ROADMAP claim.

The result note states each cell in the words of its row, the earned reading above, and nothing stronger.

### In scope
- the module `OIBridge/ParityNot.lean` with the statement surface of §"The frozen surface";
- its import line in `OIBridge.lean` and its family in `lean-manuscript-census.json`;
- `controls.py` and the result note.

### Frozen out
- any selector of `d`, any statement concluding an equation or inequation on `d`, any use of a landed dimension
  corollary of the native gate in §D–§F;
- any complex structure, any statement about `J`, the landed `d = 1` objects;
- any edit to `CompositeDimension`, `EffectSpace` or any other landed module, a manuscript, `verification/ROADMAP.md`,
  or any other round's record.

## The frozen surface

**Design-run rule:** compilation failures may cause implementation repairs, but no repair may strengthen or weaken a
frozen theorem statement, definition or hypothesis without a new preregistration revision and new design theorem
identity. A statement mismatch found by a control returns the round to design; it is never repaired during execution.

The design theorem identity is the statement surface of `ParityNot` embedded in `controls.py` (blob
`@@CONTROLS_BLOB@@`): the preamble (the import, the namespaces and the `open` line), the context blocks in order, the 92
declarations in order and by kind, every theorem's signature up to `:=`, every definition whole, and the 24 `#print
axioms` lines. The reference module is blob `44b30d27dcd388e001fbee9adec589b602130a59`. A repair may change theorem
proofs only. `OIBridge.lean` is `D`'s with `import OIBridge.ParityNot` inserted directly after
`import OIBridge.DenseOrbit`. The census is `D`'s with one family, embedded in `controls.py`, inserted directly after the
KTRANS-DENSE-1 family (modules `["DenseOrbit"]`), in `D`'s two-space JSON layout.

### Semantic guards (in `controls.py`)

Each lists the mutation controls `--self-test` drives through it, every one of which must fail with the named code.

- **S1 relations.** `GateRel` is a structure with the frozen header and exactly the fields `relT` and `relC`, each
  textually `NativeGate`'s field at `D`. Mutations: the frame added as a third field; the control relation changed; a
  landed `relC` that differs fails S1 and all three cells.
- **S2 parity** (load-bearing). Each row of the parity table pairs with its landed partner at `D` by the single
  replacement; every OIBridge identifier of the pair resolves to the same unique declaration in both namespace contexts
  (inventory: every OIBridge module at `D` and the module under check); §A outside `GateRel` and
  `gateRel_of_nativeGate` mentions none of the Q-REL list. Mutations: the parity theorem with the native gate kept; with
  positivity added; its conclusion weakened to an inequality; the oddness theorem with the frame added; a §A proof
  reading positivity; a local `eball` shadowing the landed one; a landed parity statement that differs fails the pair
  and only the Q-REL cell.
- **S3 the NOT.** The `d = 3` table with its frozen binders and conclusions, the determinant route, the three
  corollaries through `gateRel_of_nativeGate`, and §B free of the Q-REL list outside the corollaries. Mutations: the
  `π`-rotation with the native gate in place of `GateRel`; with the frame added; its unit axis dropped; the determinant
  weakened to `±1`; a §B proof reading positivity; a corollary proved without `gateRel_of_nativeGate`.
- **S4 controls.** The control table, with DIM-1's `cnot_relT` and `cnot_relC` at `D`. Mutations: the reflection
  replaced by a rotation `diag(−1, −1, 1)`; the positive control proved from `nativeGate_cnot` instead of the landed
  relations; a different landed `cnot` relation fails only the Q-NOT cell.
- **S5 separation.** The separation table, with `NativeGate`'s `frame` and `posFwd` fields at `D`. Mutations: the
  `d = 5` failure derived from `ne_five_of_nativeGate`; the `d = 5` value changed to `< 0`; the `d = 3` value changed;
  the `d = 5` witness direction changed; the `d = 5` positivity failure weakened to one input; the `d = 5` frame
  changed; the `d = 5` gate changed; a landed `posFwd` that differs fails only the Q-SEP cell.
- **S6 scope.** No declaration mentions `Complex`, `ℂ`, DIM-1's `cnot1` or `nativeGate_cnot1`, or a landed dimension
  selector (`dim_of_nativeGate`, `ne_five_of_nativeGate`, `dim_of_nativeGateOf`, `three_of_nativeGateOf`,
  `three_of_nativeGateOf_of_two_le`); no statement mentions DIM-1's `neg1` or `z1`; no theorem concludes an equation or
  inequation on `d`. Mutations: a conclusion `d ≠ 2`; a complex field; the landed `d = 1` gate.
- **S7 reuse.** No declaration of the module shares its name with an OIBridge declaration visible to it; the only
  import is `OIBridge.EffectSpace`. Mutations: `nflip` re-declared; a second import.
- **S8 phrases.** The module header and, at a commit carrying it, the result note contain none of the frozen phrases
  (among them "selects d = 3", "forces d = 3", "dimension selection", "the relations select", "positivity selects",
  "complex structure is", "yields a complex structure", "reconstructs ℂ", "J² = −1", "only higher-dimensional", "only
  obstruction", "every odd dimension", "all odd dimensions", "physically carried", "physical NOT", "positivity follows
  from", "implies positivity", "OI supplies", "OI provides", "derived from OI", "premise adopted", "qubit", "design
  (round", "not for landing"; case-insensitive, whitespace-normalized). Mutations: "The relations select d = 3." in the
  header; the design header; a note with "J² = −1" (and a neutral note passes).
- **S9 count.** Exactly the 24 frozen `#print axioms` lines, in order and distinct. Mutations: an extra print; a
  duplicated print.
- **V verdicts.** Each cell yields one outcome by its own rule; at a commit carrying the result note, the note contains
  exactly the three computed tokens and no other. Controls: a broken parity pair reads
  `PARITY-FROM-RELATIONS-NOT-ESTABLISHED` and leaves the other cells positive; a broken `π`-rotation reads
  `D3-NOT-PI-ROTATION-NOT-ESTABLISHED` and leaves the others positive; a broken `d = 5` witness reads
  `POSITIVITY-SEPARATION-NOT-ESTABLISHED` and leaves the others positive; `GateRel` broken reads not-established in all
  three; the note-token reader finds exactly the stated tokens.
- **N1–N3** as KTRANS-DENSE-1. **I, C** as KTRANS-DENSE-1, with the import after `OIBridge.DenseOrbit` and the family
  after KTRANS-DENSE-1's.

`controls.py`:
- is blob `@@CONTROLS_BLOB@@` (@@CONTROLS_LINES@@ lines), generated from the reference module, the frozen family and `D`
  by the round's generator;
- was frozen, and this revision committed, before any outcome of the predicted execution tree was read;
- `--self-test` passes 68 checks.

### Count facts

- the module carries **24** frozen `#print axioms` lines (S9) and 92 declarations;
- none of the 24 short names occurs in a `#print axioms` line at `D`, so the prints add 24 names to
  `lean_axiom_check`'s count;
- at `D` the release gate's `lean-axioms` step reports 5790 named results.

## Evidence ledger

Each row is discharged at `E` by the exact-head run at `E` and by `controls.py check E --freeze F`.

| Row | Kernel identifiers | Evidence required at `E` | Control |
|---|---|---|---|
| relations | `GateRel`, `gateRel_of_nativeGate` | the frozen structure; built | S1, V |
| parity | `finrank_plus_eq_finrank_minus_rel`, `not_even_of_gateRel` | built, axioms within `[propext, Classical.choice, Quot.sound]` | S2, V |
| the NOT at `d = 3` | `finrank_plus_minus_three`, `tangentPlus_three`, `piRotation_three`, `det_three`, `piRotation_of_nativeGate_three`, `det_of_nativeGate_three` | as above | S3, V |
| controls | `not_gateRel_refl3`, `not_gateRel_negId3`, `det_refl3`, `det_negId3`, `gateRel_cnot`, `det_nflip_rel` | as above | S4, V |
| separation at `d = 3` | `gJ3_frame`, `gateRel_gJ3`, `gJ3_value`, `not_posFwd_gJ3` | as above | S5, V |
| separation at `d = 5` | `isNot_n5`, `gJ5_frame`, `gateRel_gJ5`, `finrank_plus_eq_finrank_minus_n5`, `gJ5_value`, `not_posFwd_gJ5` | as above | S5, V |
| scope | the module's statements and proofs | no selector, complex field or `d = 1` object | S6 |
| count | the 24 prints | each within the three axioms; `lean-axioms` passes | S9 |

## Design evidence

Design runs on the certified base `D` (`workflow_dispatch` on the disposable branch `claude/pnot-dev`; the Mathlib bridge
job and the release gate read):

| Run | Commit (module blob) | Workflow run | Result |
|---|---|---|---|
| 1 | `ad871556` (`3f7e9c58`) | 37594392508 | **failed** in the Mathlib bridge only (31 other jobs `success`): unreduced literal-vector entries and `Fin` numeral comparisons in nine proofs, and two real-valued witness definitions needing `noncomputable`; the parity theorems, `piRotation_three`, `gateRel_cnot`, both frames and both `GateRel` theorems built within the three axioms |
| 2 | `2b80bbe7` (`5546e03c`) | 37595568691 | **green**: all 32 jobs `success`; repairs in proofs only (entry values by definitional unfolding, the determinant through explicit matrix-entry lemmas) and `noncomputable` on `w3` and `w5`; the Mathlib bridge (job 112707242858) built `OIBridge.ParityNot` with each of the 24 `#print axioms` lines within `[propext, Classical.choice, Quot.sound]`; release gate PASS (`lean-axioms` 5814, no `sorryAx`; `lean-manuscript` OK; 303 legacy records intact; 39 receipts hold); the Lean kernel check (job 112707242921) and the probe aggregate (job 112713747918) succeeded |

No theorem statement changed between runs 1 and 2 (all 88 statements compared). Run 2 is the design evidence for the
frozen statement surface. The reference module differs from run 2's only in the header comment (the round's name and
the final wording) and in three `simp` argument lists from which an argument the linter reported unused is removed; the
census family differs from run 2's design family only in its text. The predicted execution tree below is the evidence
for the frozen blobs.

Statement-level choices recorded as frozen: `GateRel` carries `NativeGate`'s two relation fields textually, with the
binder names `N` and `G`; the parity theorems keep their landed partners' binder names except the relation hypothesis,
named `hR`; the `d = 3` theorems state `N` explicitly as `(Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)` and the `π`-rotation with the
coordinate dot product; the separation witnesses are rational, so the two values are exact.

### The predicted execution tree

@@PREDICTED@@

## Stages

1. **C1** adds `controls.py`, blob `@@CONTROLS_BLOB@@`, to the record directory. Acceptance: the blob is the frozen
   blob.
2. **S1** adds the module, the import line and the census family in one commit. Acceptance:
   - `controls.py check S1 --freeze F` passes;
   - the exact-head run at S1 has every job green, the Mathlib bridge building the module with every printed axiom set
     within `[propext, Classical.choice, Quot.sound]` and the release gate passing.
3. **Repairs**, if the build at S1 fails, change theorem proofs only; each passes `controls.py check` at its commit. A
   failure that a proof-only repair cannot fix halts the round.
4. **S2** adds the result note `result.md`; this is candidate `E`. Acceptance: `controls.py check E --freeze F` passes
   (the result note included in S8 and V) and the exact-head run at `E` has every job green.

## Outcomes

- **`PARITY-NOT-1-READ`** — `controls.py check E --freeze F` prints `controls: OK`, `controls.py verdict E` prints
  exactly one outcome for each cell, and the exact-head run at `E` is green on every job, the Mathlib bridge building
  `ParityNot` with every frozen `#print axioms` reporting a subset of `[propext, Classical.choice, Quot.sound]` and the
  release gate passing. The result note states each cell as its row words it, the earned reading and the non-inference
  rule.
- **`PARITY-NOT-1-HALTED`** — anything else; the round halts under the specification's `S12`, and the result note names
  the failing check or job.

No outcome selects a dimension, adopts a premise, or edits the ROADMAP. Correctness bands are unchanged by either
outcome: the round is consistency-axis work.
