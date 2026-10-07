# Reconstruction round ODD-CHAR-1 — the dimensions that carry a NOT, the frame and the gate relations, and forward positivity at every odd dimension above one: PREREGISTRATION

**Status: candidate freeze.** This file is the control plane of a native round under `AGENTS.md` §A.39. It is drafted
on its pull request from `D` and is final only at the commit `F` the owner designates; no commit after `F` changes it.
The three questions, the three decision rules, the earned reading, the non-inference rule, the frozen surface, the
controls, the evidence ledger, the stages and the outcomes below are fixed; the predicted execution tree is recorded
before `F`.

```v3-round
round ODD-CHAR-1
kind non-sealing
record-directory verification/programmes/oi-qm/reconstruction/round-odd-char-1/
```

```v3-governed-paths
record AM verification/programmes/oi-qm/reconstruction/round-odd-char-1/
record AM verification/receipts/ODD-CHAR-1.json
execution A verification/lean-mathlib/OIBridge/OddChar.lean
execution M verification/lean-mathlib/OIBridge.lean
execution M verification/lean-manuscript-census.json
```

The record directory holds this preregistration, the round's frozen controls `controls.py` and the result note. The
receipt path is `verification/receipts/ODD-CHAR-1.json`. Every other path the round changes is an execution path
listed above. **No manuscript, no built artifact, `verification/ROADMAP.md`, the workflow, no probe, no landed kernel
module and no other round's record change under any outcome.**

## The objects

- **`D`** = `3c92d16b2f33d6a6acd32e96922a1f66ee735220`, the head of `main` after round PARITY-NOT-1 landed (merge of
  `Q` `15f044a2`; the push run 37631392533 at `D` succeeded, the act 42 exclusion matrix skipped on push).
- **`F`** — the commit carrying this file, which the owner designates; `delta(D, F)` is this file.
- **`E`** — the certified execution head, which the owner designates.
- **`Λ`**, **`Q`** — the reconciliation and the receipt commit, as §A.39 defines them.

## What the round is

DIM-1's `NativeGate Ω z N G` has five clauses: the frame `frame`, forward and inverse positivity `posFwd` and `posInv`,
the target relation `relT` and the control relation `relC`. With `IsNot (eball d) z N`, all five together give DIM-1's
`dim_of_nativeGate` (`d = 1 ∨ d = 3`). PARITY-NOT-1 showed that `relT` and `relC` alone (its `GateRel N G`) give the
parity count and `¬ Even d` (`not_even_of_gateRel`), and that at `d = 3` and `d = 5` an explicit gate with the frame
and the relations fails forward positivity. ODD-CHAR-1 asks which dimensions carry a NOT, the frame and the two
relations, and whether forward positivity fails for an explicit gate of that kind at every odd dimension above one. It
leaves every landed statement unchanged.

The family: for `k : ℕ` and `d = 2k + 1`, the homogeneous indices `0, …, k` have sign `+1` and `k + 1, …, 2k + 1` sign
`−1` (`oddK k`); the reversal `Fin.rev` of the `2k + 2` homogeneous indices exchanges the two classes. `nK k` is the
diagonal map with those signs on the `2k + 1` coordinates, `zK k` the last coordinate axis, and `gRev k` PARITY-NOT-1's
sign-free permutation gate `sgateEquiv` for `oddK k` and `Fin.rev`. At `k = 1` it has PARITY-NOT-1's `gJ3`'s sign classes and
involution of the four homogeneous indices.

The round asks three questions, each read from the kernel statements and the landed statements at `D` by its own frozen
decision rule. No rule reads another cell's outcome.

- **Q-FAM.** For every `k`, is `nK k` a NOT of `eball (2k + 1)` with axis `zK k`, and does `gRev k` satisfy
  `NativeGate`'s frame and `GateRel (nK k) (gRev k)`, without reading either positivity clause?
- **Q-ODD.** Do some `z`, `N`, `G` with `IsNot (eball d) z N`, `NativeGate`'s frame and `GateRel N G` exist exactly when
  `d` is odd — one direction PARITY-NOT-1's `not_even_of_gateRel`, the other DIM-1's `cnot1` at `d = 1` and `gRev k` at
  `d = 2k + 1`, `k ≥ 1`?
- **Q-POS.** For every `k ≥ 1`, does `gRev k`, with its frame and its relations, fail forward positivity on
  `eball (2k + 1)` through an explicit product state and two sharp effects with a rational negative value?

### The earned reading (frozen)

> The frame and both relations admit exactly the odd dimensions. For every odd dimension at least 3, an explicit member
> of this family fails forward positivity. Combined with DIM-1, the positivity assumptions are therefore collectively
> load-bearing for excluding the higher odd dimensions.

"Admit" is Q-ODD's existential: some NOT, frame and pair of relations on `eball d`. "The higher odd dimensions" are the
odd `d ≥ 5`. "Combined with DIM-1" is the composition of two landed theorems: at each odd `d ≥ 5` Q-ODD supplies `z`,
`N`, `G` with `IsNot`, the frame, `relT` and `relC`, while DIM-1's `dim_of_nativeGate` excludes every `z`, `N`, `G`
satisfying all five clauses; so at those `d` the two positivity clauses together are what the exclusion reads. The
round adds no kernel statement of this composition and needs none: it is the two cited statements side by side.

**The stronger claim frozen out.** The round does not show that `posFwd` alone, or `posInv` alone, is needed to exclude
any odd `d ≥ 5`: it exhibits no gate on `eball d`, `d ≥ 5`, with the frame, both relations and one positivity clause
that fails the other. `sgateEquiv`'s `invFun` is the same map `sgate odd p` as its `toFun`, so each gate of the family
is its own inverse and the family does not separate the two clauses. Whether either clause is needed without the other
is open after this round.

### The decision rules (frozen; implemented by `controls.py verdict`)

The **effective statement** of a landed theorem is the bracketed binder groups of its section `variable` lines that the
statement uses (closed under use by the groups already included; an instance group is included with a variable it
mentions), in declared order, followed by its own binders and conclusion, whitespace-normalized. The landed texts the
rules read — `NativeGate`'s fields `frame`, `posFwd`, `relT`, `relC`; `GateRel`'s field list and fields; `sgate`;
`diagSign`'s map; the effective statements of `sgate_relT`, `sgate_relC`, `not_even_of_gateRel`, `isNot_neg1`,
`cnot1_frame`, `nativeGate_cnot1`, `cnot1_relT` and `cnot1_relC` — are read from `D` and embedded in `controls.py`.

| Cell | Outcome | Rule |
|---|---|---|
| Q-FAM | `ODD-FAMILY-PROVED` | all of: the family definitions are the frozen ones; each row of the family table has its frozen binders and conclusion, the frame row's conclusion being `NativeGate`'s `frame` field read from `D` with `G` and `z` instantiated at `gRev k` and `zK k`; `gateRel_gRev` is proved through the landed `sgate_relT`, `sgate_relC` and `oddK_rev`; `GateRel`'s fields at `D` are exactly `relT` and `relC`, each textually `NativeGate`'s field at `D`; the landed `sgate`, `diagSign` map, `sgate_relT` and `sgate_relC` are the frozen ones; and no declaration of §A mentions `NativeGate`, `posFwd`, `posInv`, `maxCone`, `prodEffVal`, `IsEffectOn` or `sharpEff` |
| Q-FAM | `ODD-FAMILY-NOT-ESTABLISHED` | otherwise |
| Q-ODD | `ODD-CHARACTERIZATION-PROVED` | all of: `exists_frame_gateRel_iff_odd` has the binder `(d : ℕ)` and the conclusion `(∃ (z : Fin d → ℝ) (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (G : W d ≃ₗ[ℝ] W d), IsNot (eball d) z N ∧ (FRAME) ∧ GateRel N G) ↔ Odd d`, with `FRAME` `NativeGate`'s `frame` field read from `D`; its proof names `not_even_of_gateRel`, `cnot1`, `isNot_neg1`, `cnot1_frame` and either `nativeGate_cnot1` or both `cnot1_relT` and `cnot1_relC`, and `gRev`, `isNot_nK`, `gRev_frame` and `gateRel_gRev`; `GateRel` at `D` is as in Q-FAM; the landed `not_even_of_gateRel`, `isNot_neg1`, `nativeGate_cnot1`, `cnot1_relT` and `cnot1_relC` are the frozen ones and the landed `cnot1_frame` is `NativeGate`'s `frame` field at `D` with `G` and `z` instantiated at `cnot1` and `z1`; and no declaration of §B mentions the Q-FAM list |
| Q-ODD | `ODD-CHARACTERIZATION-NOT-ESTABLISHED` | otherwise |
| Q-POS | `HIGHER-ODD-POSFWD-FAILURE-PROVED` | all of: `oddK`, `zK`, `nK`, `gRev` and the witness definitions are the frozen ones; each row of the positivity table has its frozen binders and conclusion, the positivity row's conclusion being `¬` of `NativeGate`'s `posFwd` field read from `D` with `Ω` and `G` instantiated at `eball (2 * k + 1)` and `gRev k`; the non-membership row is proved through `gRev_value`, `sharpEff_isEffectOn`, `sum_wK_sq` and `sum_zK_sq`, the positivity row through the non-membership row, and the native-gate row through the positivity row; `gRev_frame` and `gateRel_gRev` have their frozen statements and `GateRel` at `D` is as in Q-FAM; and no declaration of §C names a landed dimension corollary of the native gate (`*_of_nativeGate*`, `three_of_*`, `dim_of_*`) or `posInv` |
| Q-POS | `HIGHER-ODD-POSFWD-FAILURE-NOT-ESTABLISHED` | otherwise |

The round's outcome is `ODD-CHAR-1-READ` when all three cells are assigned, each by its own rule. The design runs below
already exhibit a module read by these rules as `ODD-FAMILY-PROVED`, `ODD-CHARACTERIZATION-PROVED` and
`HIGHER-ODD-POSFWD-FAILURE-PROVED`; the rules, not that reading, are what this file freezes, and the cells at `E` are
those `controls.py verdict E` prints.

Q-FAM and Q-POS both read the family's definitions and `gRev k`'s frame and relation statements, since Q-POS concerns
a member of the family; Q-ODD reads only its own statement, the names its proof cites and the landed texts. A change to
the family's frame therefore reads not-established in Q-FAM and Q-POS and leaves Q-ODD, whose statement is the claim.

### The family table (frozen)

| Declaration | Frozen statement | Proof names |
|---|---|---|
| `oddK` | `def oddK (k : ℕ) (μ : Fin (2 * k + 1 + 1)) : Bool := decide (k < (μ : ℕ))` | — |
| `cK` | `def cK (k : ℕ) (j : Fin (2 * k + 1)) : ℝ := if oddK k j.succ then -1 else 1` | — |
| `nK` | `def nK (k : ℕ) : (Fin (2 * k + 1) → ℝ) →ₗ[ℝ] (Fin (2 * k + 1) → ℝ) := diagSign (cK k)` | — |
| `zK` | `def zK (k : ℕ) : Fin (2 * k + 1) → ℝ := fun i => if (i : ℕ) = 2 * k then 1 else 0` | — |
| `gRev` | `def gRev (k : ℕ) : W (2 * k + 1) ≃ₗ[ℝ] W (2 * k + 1) := sgateEquiv (oddK k) Fin.rev Fin.rev_rev` | — |
| `oddK_rev` | `(k : ℕ) (μ : Fin (2 * k + 1 + 1)) : oddK k (Fin.rev μ) = !oddK k μ` | — |
| `isNot_nK` | `(k : ℕ) : IsNot (eball (2 * k + 1)) (zK k) (nK k)` | — |
| `gRev_frame` | `(k : ℕ) (a b : Fin 2) : gRev k (prodState (corner (zK k) a) (corner (zK k) b)) = prodState (corner (zK k) a) (corner (zK k) (a + b))` | — |
| `gateRel_gRev` | `(k : ℕ) : GateRel (nK k) (gRev k)` | `sgate_relT`, `sgate_relC`, `oddK_rev` |
| `finrank_plus_eq_finrank_minus_nK` | `(k : ℕ) : Module.finrank ℝ (plusSpace (nK k)) = Module.finrank ℝ (minusSpace (nK k))` | `finrank_plus_eq_finrank_minus_rel` |

The mathematical content: `nK k` changes the sign of the coordinates `k, …, 2k` (the homogeneous indices `k + 1, …,
2k + 1`), so it is an involutive isometry of the ball that negates the last axis, and its two eigenspaces on the
homogeneous indices have `k + 1` elements each. The gate fixes the target columns of sign `+1` and applies `Fin.rev` to
the control index of the columns of sign `−1`; the two relations are PARITY-NOT-1's `sgate_relT` and `sgate_relC`, the
second reading that `Fin.rev` exchanges the two sign classes (`oddK_rev`). On the corners the only target column of
sign `−1` that is occupied is the last, where `Fin.rev` exchanges the control rows `0` and `2k + 1`; this multiplies the
target corner by the control's sign, which is the frame.

### The characterization (frozen)

`exists_frame_gateRel_iff_odd (d : ℕ)` with the conclusion of the Q-ODD row. Forward: `not_even_of_gateRel` from the
NOT and the relations, the frame unused. Reverse: for `d = 2k + 1`, `k = 0` gives `d = 1`, DIM-1's `cnot1` with `neg1`
and `z1` (`isNot_neg1`, `cnot1_frame`, the relations of `nativeGate_cnot1` through `gateRel_of_nativeGate`); `k ≥ 1`
gives `gRev k` with `nK k` and `zK k` (`isNot_nK`, `gRev_frame`, `gateRel_gRev`). Each direction is witnessed by a
separately named theorem, as §A.34 requires of a displayed equivalence.

### The positivity table (frozen)

| Declaration | Frozen statement | Proof names |
|---|---|---|
| `xK` | `def xK (k : ℕ) : Fin (2 * k + 1) → ℝ := fun i => if (i : ℕ) = 0 then 1 else 0` | — |
| `wK` | `noncomputable def wK (k : ℕ) : Fin (2 * k + 1) → ℝ := fun i => if (i : ℕ) = 2 * k - 1 then -3 / 5 else if (i : ℕ) = 2 * k then -4 / 5 else 0` | — |
| `entW` | `def entW (p q : Fin (d + 1)) : W d := fun μ ν => if μ = p then (if ν = q then 1 else 0) else 0` | — |
| `sum_wK_sq` | `(k : ℕ) (hk : 1 ≤ k) : ∑ j, wK k j ^ 2 = 1` | — |
| `pairVal_entW` | `(a b : HVec d) (p q : Fin (d + 1)) : pairVal a b (entW p q) = a p * b q` | — |
| `gRev_value` | `(k : ℕ) (hk : 1 ≤ k) : prodEffVal (sharpEff (wK k)) (sharpEff (zK k)) (gRev k (prodState (xK k) (zK k))) = -1 / 10` | — |
| `gRev_not_mem_maxCone` | `(k : ℕ) (hk : 1 ≤ k) : gRev k (prodState (xK k) (zK k)) ∉ maxCone (eball (2 * k + 1))` | `gRev_value`, `sharpEff_isEffectOn`, `sum_wK_sq`, `sum_zK_sq` |
| `not_posFwd_gRev` | `(k : ℕ) (hk : 1 ≤ k) : ¬ ∀ x ∈ eball (2 * k + 1), ∀ y ∈ eball (2 * k + 1), gRev k (prodState x y) ∈ maxCone (eball (2 * k + 1))` | `gRev_not_mem_maxCone` |
| `not_nativeGate_gRev` | `(k : ℕ) (hk : 1 ≤ k) : ¬ NativeGate (eball (2 * k + 1)) (zK k) (nK k) (gRev k)` | `not_posFwd_gRev` |

The values: with `c = 2k + 1` the corner's homogeneous index, the product of the first axis with the corner has entries
`1` at `(0, 0)`, `(1, 0)`, `(0, c)` and `(1, c)`. The gate fixes column `0` and moves column `c` to the rows `Fin.rev 0
= 2k + 1` and `Fin.rev 1 = 2k`. The sharp vectors are `(1/2, w/2)` and `(1/2, z/2)`; for `k ≥ 1` the first coordinate of
`wK k` is `0`, and its coordinates `2k − 1` and `2k` (homogeneous indices `2k` and `2k + 1`) are `−3/5` and `−4/5`, so
the pairing is `1/4 − 3/20 − 4/20 = −1/10`. The witness is rational, so the value is exact. At `k = 0` the round makes no
positivity claim: DIM-1's `cnot1` is a native gate at `d = 1`.

### The non-inference rule (frozen)

> This round does not show that `posFwd` or `posInv` is individually necessary for excluding any odd dimension: it
> exhibits no gate with the frame, both relations and one positivity clause that fails the other, and each gate of its
> family is its own inverse. It does not select a dimension from positivity alone and neither restates nor extends
> DIM-1's `dim_of_nativeGate`. It does not classify the gates with the frame, the relations and positivity in any
> dimension, and it does not show that the frame, `relT` or `relC` is needed for oddness or for any exclusion. It
> concerns no complex structure, gives no interpretation of `J²`, and concerns no NOT or gate carried or realized by a
> physical theory: `nK`, `gRev`, `xK` and `wK` are mathematical witnesses. It adopts no premise, and makes no manuscript
> claim and no ROADMAP claim.

The result note states each cell in the words of its row, the earned reading in its frozen words, and nothing stronger.

### In scope
- the module `OIBridge/OddChar.lean` with the statement surface of §"The frozen surface";
- its import line in `OIBridge.lean` and its family in `lean-manuscript-census.json`;
- `controls.py` and the result note.

### Frozen out
- any claim that `posFwd` or `posInv` alone excludes a dimension, any gate separating the two clauses, any statement
  mentioning `posInv`;
- any classification of positive gates, any selector of `d` from positivity, any statement concluding an equation or
  inequation on `d`, any use of a landed dimension corollary of the native gate in §C;
- any necessity statement for the frame, `relT` or `relC`;
- any complex structure, any statement about `J`, `Entangling`;
- any edit to `CompositeDimension`, `ParityNot`, `EffectSpace` or any other landed module, a manuscript,
  `verification/ROADMAP.md`, or any other round's record.

## The frozen surface

**Design-run rule:** compilation failures may cause implementation repairs, but no repair may strengthen or weaken a
frozen theorem statement, definition or hypothesis without a new preregistration revision and new design theorem
identity. A statement mismatch found by a control returns the round to design; it is never repaired during execution.

The design theorem identity is the statement surface of `OddChar` embedded in `controls.py` (blob
``957819380643ff7690a6125d54b011f61aec403d``): the preamble (the import, the namespaces and the `open` line), the context blocks in order, the 30
declarations in order and by kind, every theorem's signature up to `:=`, every definition whole, and the 12 `#print
axioms` lines. The reference module is blob `bbb8a63229870f61445d5dbb3fe9102b826d9208`. A repair may change theorem
proofs only. `OIBridge.lean` is `D`'s with `import OIBridge.OddChar` inserted directly after
`import OIBridge.ParityNot`. The census is `D`'s with one family, embedded in `controls.py`, inserted directly after the
PARITY-NOT-1 family (modules `["ParityNot"]`), in `D`'s two-space JSON layout.

### Semantic guards (in `controls.py`)

Each lists the mutation controls `--self-test` drives through it, every one of which must fail with the named code.

- **L landed.** The landed texts read from `D` are the frozen ones.
- **S1 family** (Q-FAM). Mutations: the sign classes changed (`k <` to `k ≤`); the frame's target corner changed; the
  relations weakened to the target relation; the NOT stated with another axis; a §A proof reading the maximal cone.
  Rule controls: a broken family frame reads not-established in Q-FAM and Q-POS and leaves Q-ODD; a broken NOT reads
  not-established in Q-FAM alone; a landed `GateRel` that differs from `NativeGate`'s relations fails all three cells; a
  landed `sgate_relC` that differs fails Q-FAM alone.
- **S2 characterization** (Q-ODD). Mutations: the frame dropped from the existential; forward positivity added to it;
  the equivalence weakened to one direction; the right side strengthened to `Odd d ∧ 3 ≤ d`; `d = 1` through `gRev 0`
  instead of DIM-1's `cnot1`; the forward direction not through `not_even_of_gateRel`. Rule controls: a one-directional
  statement reads not-established in Q-ODD alone; a landed `not_even_of_gateRel` that differs, and a landed
  `cnot1_frame` that differs, each fail Q-ODD alone.
- **S3 positivity** (Q-POS). Mutations: the value changed to `< 0`; the witness direction changed; the failure weakened
  to one input; the range `1 ≤ k` dropped; the native-gate failure read from `dim_of_nativeGate`. Rule controls: a broken
  value reads not-established in Q-POS alone; a landed `posFwd` that differs fails Q-POS alone; a landed `frame` that
  differs fails all three cells.
- **S6 scope.** No declaration mentions `Complex`, `ℂ`, `posInv` (also as a projection), `Entangling` or a landed
  dimension selector (`dim_of_nativeGate`, `ne_five_of_nativeGate`, `three_of_nativeGate`, `dim_of_nativeGateOf`,
  `three_of_nativeGateOf`, `three_of_nativeGateOf_of_two_le`); no theorem concludes an equation or inequation on `d`;
  no theorem concludes `NativeGate`, the maximal cone or `posFwd` without a leading `¬` or a `∉`. Mutations: `posInv`
  read as a projection; a conclusion `d ≠ 2`; a positive native gate at `k = 1`; a complex field.
- **S7 reuse.** No declaration of the module shares its name with an OIBridge declaration visible to it; the only
  import is `OIBridge.ParityNot`. Mutations: `sgate` re-declared; a second import.
- **S8 phrases.** The module header and, at a commit carrying it, the result note contain none of the frozen phrases
  (among them "individually necessary", "individually load-bearing", "posFwd is necessary", "posInv is necessary",
  "forward positivity alone", "inverse positivity alone", "forward positivity excludes", "positivity selects",
  "selects d = 3", "dimension selection", "classifies the positive", "only positive gate", "relT is necessary", "relC is
  necessary", "the frame is necessary", "complex structure is", "J² = −1", "physical NOT", "physically realizable",
  "OI supplies", "premise adopted", "qubit", "all odd dimensions", "design (round", "not for landing";
  case-insensitive, whitespace-normalized). Mutations: "Forward positivity is individually necessary." in the header;
  the design header; the frozen earned reading passes, and "posFwd is necessary", "inverse positivity alone" and
  "individually necessary" each fail.
- **S9 count.** Exactly the 12 frozen `#print axioms` lines, in order and distinct. Mutations: an extra print; a
  duplicated print.
- **V verdicts.** Each cell yields one outcome by its own rule; at a commit carrying the result note, the note contains
  exactly the three computed tokens and no other. Control: the note-token reader finds exactly the stated tokens.
- **N1–N3** as PARITY-NOT-1. **I, C** as PARITY-NOT-1, with the import after `OIBridge.ParityNot` and the family after
  PARITY-NOT-1's.

`controls.py`:
- is blob ``957819380643ff7690a6125d54b011f61aec403d`` (1325 lines), generated from the reference module, the frozen family and `D`
  by the round's generator;
- was frozen, and this revision committed, before any outcome of the predicted execution tree was read;
- `--self-test` passes 62 checks.

### Count facts

- the module carries **12** frozen `#print axioms` lines (S9) and 30 declarations;
- none of the 12 short names occurs in a `#print axioms` line at `D`, so the prints add 12 names to
  `lean_axiom_check`'s count;
- at `D` the release gate's `lean-axioms` step reports 5814 named results.

## Evidence ledger

Each row is discharged at `E` by the exact-head run at `E` and by `controls.py check E --freeze F`.

| Row | Kernel identifiers | Evidence required at `E` | Control |
|---|---|---|---|
| family | `oddK_rev`, `isNot_nK`, `gRev_frame`, `gateRel_gRev`, `finrank_plus_eq_finrank_minus_nK` | built, axioms within `[propext, Classical.choice, Quot.sound]` | S1, V |
| characterization | `exists_frame_gateRel_iff_odd` | as above | S2, V |
| positivity at `k ≥ 1` | `sum_wK_sq`, `pairVal_entW`, `gRev_value`, `gRev_not_mem_maxCone`, `not_posFwd_gRev`, `not_nativeGate_gRev` | as above | S3, V |
| scope | the module's statements and proofs | no `posInv`, selector, complex field or positive gate conclusion | S6 |
| count | the 12 prints | each within the three axioms; `lean-axioms` passes | S9 |

## Design evidence

Design runs on the certified base `D` (`workflow_dispatch` on the disposable branch `claude/oddchar-dev`; the Mathlib
bridge job and the release gate read):

| Run | Commit (module blob) | Workflow run | Result |
|---|---|---|---|
| 1 | `dbdb4662` (`733a1f38`) | 37643178804 | **green**: all 32 jobs `success`; the Mathlib bridge (job 112867031508) built `OIBridge.OddChar` with each of the 12 `#print axioms` lines within `[propext, Classical.choice, Quot.sound]` (`oddK_rev` within `[propext, Quot.sound]`); release gate PASS (`lean-axioms` 5826, no `sorryAx`; 303 legacy records intact; 40 receipts hold); linter warnings in the module only: seven redundant `done`, one unreachable `ring` alternative and two unused `simp` arguments |
| 2 | `6977ee04` (`d61a6c49`) | 37646141082 | **green**: all 32 jobs `success`; the Mathlib bridge (job 112877295405) built `OIBridge.OddChar` with each of the 12 `#print axioms` lines within `[propext, Classical.choice, Quot.sound]` (`oddK_rev` within `[propext, Quot.sound]`) and no warning in the module; release gate PASS (`lean-axioms` 5826, no `sorryAx`; 303 legacy records intact; 40 receipts hold); the Lean kernel check (job 112877295130) and the probe aggregate (job 112885299495) succeeded |

Run 2 changes nine proof lines of run 1 and nothing else: the seven redundant `done` and the unreachable `ring`
alternative removed, and the two unused `simp` arguments dropped. No theorem statement, definition or context block
changed between runs 1 and 2 (all 30 declarations compared). Run 2 is the design evidence for the frozen statement
surface. The reference module differs from run 2's only in the header comment (the round's name and the final
wording); the census family differs from run 1's design family only in its text. The predicted execution tree below is
the evidence for the frozen blobs.

Statement-level choices recorded as frozen: the family is indexed by `k` with `d = 2 * k + 1` written out, so every
statement is about `eball (2 * k + 1)`; the frame clause of the characterization is `NativeGate`'s `frame` field
verbatim; the characterization's reverse direction at `d = 1` uses DIM-1's `cnot1`, not `gRev 0`; the positivity
witness is rational, so the value is exact.

### The predicted execution tree

Recorded at `F` from the run on the predicted tree; this drafting revision differs from the revision at `F` only in this section.

## Stages

1. **C1** adds `controls.py`, blob ``957819380643ff7690a6125d54b011f61aec403d``, to the record directory. Acceptance: the blob is the frozen
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

- **`ODD-CHAR-1-READ`** — `controls.py check E --freeze F` prints `controls: OK`, `controls.py verdict E` prints
  exactly one outcome for each cell, and the exact-head run at `E` is green on every job, the Mathlib bridge building
  `OddChar` with every frozen `#print axioms` reporting a subset of `[propext, Classical.choice, Quot.sound]` and the
  release gate passing. The result note states each cell as its row words it, the earned reading in its frozen words and
  the non-inference rule.
- **`ODD-CHAR-1-HALTED`** — anything else; the round halts under the specification's `S12`, and the result note names
  the failing check or job.

No outcome selects a dimension, adopts a premise, or edits the ROADMAP. Correctness bands are unchanged by either
outcome: the round is consistency-axis work.
