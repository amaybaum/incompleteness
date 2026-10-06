# Reconstruction round K1-BRIDGE-1 — DIM-1's selectors relative to the available test family: PREREGISTRATION

**Status: candidate freeze.** This file is the control plane of a native round under `AGENTS.md` §A.39. It is drafted
on its pull request from `D` and is final only at the commit `F` the owner designates; no commit after `F` changes it.
The question, the decision rule, the non-inference rule, the frozen surface, the controls, the evidence ledger, the
stages and the outcomes below are fixed; the predicted execution tree is recorded before `F`.

```v3-round
round K1-BRIDGE-1
kind non-sealing
record-directory verification/programmes/oi-qm/reconstruction/round-k1-bridge-1-effect-availability/
```

```v3-governed-paths
record AM verification/programmes/oi-qm/reconstruction/round-k1-bridge-1-effect-availability/
record AM verification/receipts/K1-BRIDGE-1.json
execution A verification/lean-mathlib/OIBridge/K1Bridge.lean
execution M verification/lean-mathlib/OIBridge.lean
execution M verification/lean-manuscript-census.json
```

The record directory holds this preregistration, the round's frozen controls `controls.py` and the result note. The
receipt path is `verification/receipts/K1-BRIDGE-1.json`. Every other path the round changes is an execution path
listed above. **No manuscript, no built artifact, `verification/ROADMAP.md`, the workflow, no probe and no other
round's record change under any outcome.** The K1 status wording in `verification/ROADMAP.md` is not part of this
round; it is updated, if at all, by a separate change after the round's landing is certified, against the theorem
this round lands.

## The objects

- **`D`** = `20aa54803df5d74e6c67a1341ca022dee340a65b`, the head of `main` after the README change #797 landed (merge
  of `5ceee783`; the push run 37428463888 at `D` succeeded, the act 42 exclusion matrix skipped on push).
- **`F`** — the commit carrying this file, which the owner designates; `delta(D, F)` is this file.
- **`E`** — the certified execution head, which the owner designates.
- **`Λ`**, **`Q`** — the reconciliation and the receipt commit, as §A.39 defines them.

## What the round is

Round DIM-1's selectors `dim_of_nativeGate` and `three_of_nativeGate` take the native-gate hypotheses `NativeGate`,
whose two positivity clauses are stated on the maximal product cone `maxCone Ω`, the cone of joint vectors
nonnegative on every product of two effects of `Ω`, and the entangling clause `Entangling`, stated on the joint
states of that cone. Read operationally, positivity on `maxCone Ω` is positivity against every product of two affine
effects, available or not: the full affine effect set enters K1 there. Round EFF-1 proved, on the coordinate ball
`eball d` for `0 < d`, that the cone of the products of any family `avail` of available functionals is
`maxCone (eball d)` once every available functional is an effect and the family satisfies OG-1's four named
hypotheses (`maxConeOf_avail_eq`).

This round asks one question and answers it by a frozen decision rule read from the kernel statements.

- **Q-BRIDGE.** With DIM-1's two positivity clauses restated on the cone `maxConeOf avail` of the available family,
  and the entangling clause on the joint states of that cone, do `0 < d`, effect soundness and OG-1's four named
  hypotheses give DIM-1's two selectors, by the cone equality alone?

OG-1's named hypotheses are `PreservesBody (eball d) G` (body preservation), `SharpSeed (eball d) r` (K∞-Seed),
`BoundaryTransitive (eball d) G` (K∞-Trans) and `SeedOrbitAvailable G r avail` (K∞-V4), in the labels of
`verification/ROADMAP.md` and `verification/audits/foundations/kinf-seams-audit.md` at `D`. Effect soundness is
`EffectsOn (eball d) avail`: every available functional is an effect on the ball. All five are named, unsourced
premises, as are DIM-1's `IsNot` and the relative native-gate and entangling hypotheses below. The round uses no
mixing closure (`MixingClosed`) and no unit premise (`unitEff d ∈ avail`).

**Convention for DISCHARGED.** The verdict `K1-EFFECT-AVAILABILITY-DISCHARGED` means: DIM-1's selectors hold with the
operational availability of the full affine effect set replaced, in their hypotheses, by effect soundness and OG-1's
four named hypotheses, through EFF-1's cone equality, with no new dimension argument. It never means that any of those
hypotheses is derived from OI, and never that the composite structure DIM-1's carrier `W d` encodes — local
tomography, the product form of the composite tests — is derived: that structure is a premise of DIM-1, of EFF-1 and
of this round alike.

### The decision rule (frozen; implemented by `controls.py verdict`)

The outcome is read from the statements of the module at `E`.

| Outcome | Rule |
|---|---|
| `K1-EFFECT-AVAILABILITY-DISCHARGED` | all of: (i) `NativeGateOf` is DIM-1's `NativeGate` at `D` with `maxConeOf avail` in place of `maxCone Ω` in exactly the two positivity clauses, the gate renamed, and the frame and the two NOT relations unchanged; `jointStatesOf` is DIM-1's `jointStates` with `maxConeOf avail`; `EntanglingOf` is DIM-1's `Entangling` with `jointStatesOf avail` (S1); (ii) a theorem whose explicit binders are exactly `(hd : 0 < d) (hE : EffectsOn (eball d) avail)`, the four hypotheses, `(hN : IsNot (eball d) z N)` and `(hT : NativeGateOf (eball d) avail z N T)`, with conclusion `d = 1 ∨ d = 3`; (iii) a theorem with those binders and `(hEnt : EntanglingOf (eball d) avail T)`, with conclusion `d = 3`; (iv) the controls `cone_eq_fails_zero : maxConeOf (sharpFamily 0) ≠ maxCone (eball 0)` and `cone_eq_fails_axis : EffectsOn (eball 3) axisFamily ∧ maxConeOf axisFamily ≠ maxCone (eball 3)` as theorems with exactly those statements |
| `K1-BRIDGE-NOT-ESTABLISHED` | otherwise |

The design runs below already exhibit a module read by this rule as `K1-EFFECT-AVAILABILITY-DISCHARGED`; the rule,
not that reading, is what this file freezes, and the verdict at `E` is the one `controls.py verdict E` prints.

### The non-inference rule (frozen)

> The verdict removes the operational availability of the full affine effect set from K1's hypotheses. It does not
> derive local tomography, the product form of the composite tests, or any other composite structure of K2; it does
> not source `0 < d`, effect soundness, body preservation, K∞-Seed, K∞-Trans, K∞-V4, `IsNot`, the relative
> native-gate hypotheses or the relative entangling clause; and it says nothing about K∞-Stage, K∞-Act, K∞-Drive,
> K∞-Copy, K∞-Geom, Kₙ or K3 beyond naming which premises remain.

The result note states the verdict in the words of its row above, states that `0 < d` and effect soundness remain
explicit hypotheses, that body preservation, K∞-Seed, K∞-Trans and K∞-V4 remain unsourced premises, that no mixing
closure and no unit premise is used, and that the round attributes none of those hypotheses to OI. It
leaves the frozen DIM-1 preregistration and result note as they stand.

### In scope
- the module `OIBridge/K1Bridge.lean` with the statement surface of §"The frozen surface";
- its import line in `OIBridge.lean` and its family in `lean-manuscript-census.json`;
- `controls.py` and the result note.

### Frozen out
- any source of `0 < d`, effect soundness, body preservation, K∞-Seed, K∞-Trans, K∞-V4, `IsNot`, the relative
  native-gate or entangling hypotheses, and any statement that OI supplies them; anything about K2, K∞-Stage, K∞-Act,
  K∞-Drive, K∞-Copy, K∞-Geom, Kₙ or K3 beyond dependency bookkeeping;
- the mixing closure and the unit premise, in any statement of the module;
- a new dimension argument: no eigenspace, parity, rank, block or tangent reasoning; the selectors compose the cone
  equality, the transport and DIM-1's landed selectors;
- a limit closure, a drive or flow, a complex or matrix representation, the qubit's operator effects;
- any edit to `CompositeDimension`, `EffectSpace`, `OrbitGeneration`, `TransitiveBody`, `CompositeInterface`, a
  manuscript, `verification/ROADMAP.md`, the frozen DIM-1 or EFF-1 records, or any other round's record.

## The frozen surface

**Design-run rule:** compilation failures may cause implementation repairs, but no repair may strengthen or weaken a
frozen theorem statement, definition, structure or hypothesis without a new preregistration revision and new design
theorem identity.

The design theorem identity is the statement surface of `K1Bridge` embedded in `controls.py` (blob
`5cbb445e3f85fe28d513b7d1d90fa7358d70054b`): the preamble (the import, namespaces, `open` lines, `variable {d : ℕ}`), the context blocks in
order, the 13 declarations in order and by kind, every theorem's signature up to `:=`, every definition and structure
whole, and the 10 `#print axioms` lines. The reference module is blob `835e801dd8a49635f152dac4b0f65abaa6fcfef9`. A
repair may change theorem proofs only. `OIBridge.lean` is `D`'s with `import OIBridge.K1Bridge` inserted directly
after `import OIBridge.EffectSpace`. The census is `D`'s with one family, embedded in `controls.py`, inserted
directly after the EFF-1 family (modules `["EffectSpace"]`), in `D`'s two-space JSON layout.

### The principal statements

| Row | Identifier | Statement |
|---|---|---|
| REL | `NativeGateOf`, `jointStatesOf`, `EntanglingOf` | `NativeGateOf Ω avail z N T`: DIM-1's five fields with `T (prodState x y) ∈ maxConeOf avail` and `T.symm (prodState x y) ∈ maxConeOf avail` in place of membership in `maxCone Ω`; `jointStatesOf avail := {ω \| ω ∈ maxConeOf avail ∧ ω 0 0 = 1}`; `EntanglingOf Ω avail T`: DIM-1's clause on `(jointStatesOf avail).extremePoints ℝ` |
| TRANSPORT | `nativeGate_of_cone_eq`, `jointStatesOf_eq`, `entangling_of_cone_eq` | `maxConeOf avail = maxCone Ω → NativeGateOf Ω avail z N T → NativeGate Ω z N T`; `maxConeOf avail = maxCone Ω → jointStatesOf avail = jointStates Ω`; `maxConeOf avail = maxCone Ω → EntanglingOf Ω avail T → Entangling Ω T` |
| AVAIL | `nativeGate_of_avail`, `entangling_of_avail` | `(hd : 0 < d) (hE : EffectsOn (eball d) avail)` and the four hypotheses carry `NativeGateOf (eball d) avail z N T` to `NativeGate (eball d) z N T`, and `EntanglingOf (eball d) avail T` to `Entangling (eball d) T`, each by `maxConeOf_avail_eq` and the transport |
| Q-BRIDGE | `dim_of_nativeGateOf`, `three_of_nativeGateOf` | `(hd : 0 < d) (hE : EffectsOn (eball d) avail)`, the four hypotheses, `(hN : IsNot (eball d) z N) (hT : NativeGateOf (eball d) avail z N T) ⟹ d = 1 ∨ d = 3`; with `(hEnt : EntanglingOf (eball d) avail T)` as well, `d = 3`; each proved by name from `nativeGate_of_avail` (and `entangling_of_avail`) and DIM-1's `dim_of_nativeGate` (`three_of_nativeGate`) |
| CTL | `cone_eq_fails_zero`, `cone_eq_fails_axis` | `maxConeOf (sharpFamily 0) ≠ maxCone (eball 0)` (EFF-1's `maxConeOf_sharpFamily_zero_ne`); `EffectsOn (eball 3) axisFamily ∧ maxConeOf axisFamily ≠ maxCone (eball 3)` (the one-axis family with the unit consists of effects, by `isEffectOn_unitEff` and `sharpEff_isEffectOn`, and EFF-1's `maxConeOf_axis_ne`) |
| core | `k1b_core` | the two relative selectors universally quantified, and the two controls |

### Semantic guards (in `controls.py`)

Each lists the mutation controls `--self-test` drives through it, every one of which must fail with the named code.

- **S1 relative.** `NativeGateOf`'s fields are `frame`, `posFwd`, `posInv`, `relT`, `relC`, each equal to DIM-1's
  field at `D` with the gate renamed `T` and, in the two positivity clauses only, `maxConeOf avail` for `maxCone Ω`;
  its header carries the family and the gate; `jointStatesOf` and `EntanglingOf` are DIM-1's bodies with the family's
  cone and joint states. DIM-1's three texts at `D` are embedded in `controls.py` and compared against `D` by the
  self-test. Mutations: a positivity clause returned to `maxCone Ω`; the frame weakened; a NOT relation dropped; the
  entangling clause on DIM-1's joint states.
- **S2 selectors.** `dim_of_nativeGateOf` and `three_of_nativeGateOf` are theorems with exactly the binders and
  conclusions of the decision rule, each printed, and no `MixingClosed`, `unitEff`, `fullEffects`, `sharpFamily` or
  `unitSpan` token in their statements. Mutations: the mixing closure added; `0 < d` dropped; effect soundness dropped;
  `IsNot` dropped; the entangling clause dropped from the three selector.
- **S3 transparent.** The proof of `nativeGate_of_avail` names `maxConeOf_avail_eq` and `nativeGate_of_cone_eq`; of
  `entangling_of_avail`, `maxConeOf_avail_eq` and `entangling_of_cone_eq`; of `dim_of_nativeGateOf`,
  `dim_of_nativeGate` and `nativeGate_of_avail`; of `three_of_nativeGateOf`, `three_of_nativeGate`,
  `nativeGate_of_avail` and `entangling_of_avail`. No `finrank`, `plusSpace`, `minusSpace`, `tangentPlus`, `BlockData`,
  `Even`, `Odd`, `lor_face`, `corner_form`, `gate_corner`, `gt_corner`, `Phi`, `NativeGateBall`, `eigenspace`,
  `parity`, `not_entangling_one` or `omega` token in the module's code. Mutations: the dimension selector proved
  without DIM-1's selector; a rank token.
- **S4 premises.** No theorem concludes `SharpSeed`, `PreservesBody`, `BoundaryTransitive`, `SeedOrbitAvailable`,
  `EffectsOn`, `IsNot`, `NativeGateOf`, `EntanglingOf` or `MixingClosed` of a hypothesis-bound object; `EffectsOn` is
  concluded only of `axisFamily` by `cone_eq_fails_axis` (its frozen conclusion, printed) and in the verdict, where
  every other premise occurs as an antecedent; `NativeGate` and `Entangling` are concluded only by the transport and
  availability theorems, from `NativeGateOf` and `EntanglingOf` in their binders. Mutations: `NativeGateOf` concluded
  from the seed orbit; `EffectsOn` concluded for a hypothesis-bound family; `NativeGate` concluded without the relative
  form.
- **S5 reuse.** No declaration has the name of a landed object it reads (`maxCone`, `maxConeOf`, `EffectsOn`,
  `NativeGate`, `Entangling`, `jointStates`, `IsProduct`, `IsNot`, `prodState`, `corner`, `actT`, `actC`, `W`,
  `eball`, `sharpFamily`, `axisFamily`, the two DIM-1 selectors, `maxConeOf_avail_eq`, the two EFF-1 controls,
  `unitEff`, the OG-1 predicates, and others listed in `controls.py`); the only import is `OIBridge.EffectSpace`.
  Mutations: `maxCone` re-declared; a second import.
- **S6 neutral.** No complex, conjugate-transpose, positive-semidefinite, trace, qubit, Bloch, Pauli, density, drive,
  flow, limit-closure, tensor-product or Hilbert token, and no `MixingClosed` or `unitSpan` token, in the module's
  code. Mutations: a complex scalar; a mixing-closure token.
- **S7 phrases.** The module header and, at a commit carrying it, the result note contain none of "OI supplies",
  "derived from OI", "sourced from OI", "mixing closure is derived", "local tomography is derived", "product form is
  derived", "product-test completeness is derived", "composite premise is discharged", "K2 is discharged", "qubit
  effect space", "selects d = 3 from OI" (case-insensitive, whitespace-normalized). Mutation: "OI supplies the
  effects." in the header; a note string with "local tomography is derived" (and a neutral note passes).
- **S8 dimension.** `0 < d` occurs in exactly the frozen set of statements (`nativeGate_of_avail`,
  `entangling_of_avail`, `dim_of_nativeGateOf`, `three_of_nativeGateOf`, `k1b_core`); outside §D and the verdict no
  dimension-three object (`Fin 3`, `eball 3`, `W 3`, `HVec 3`, `maxCone 3`, `ball3`, `eball_three`) and none of
  `unitEff`, `axisFamily`, `isEffectOn_unitEff`, `sharpEff_isEffectOn`, `sharpFamily` occurs. Mutations: `0 < d`
  added to the transport; a dimension-three object in §C; the control family in §C.
- **S9 count.** Exactly the 10 frozen `#print axioms` lines, in order and distinct, each naming a declaration of the
  module. Mutations: an extra print; a duplicated print.
- **V verdict.** The decision rule yields one outcome; at a commit carrying the result note, the note contains
  exactly the computed outcome token and no other. Controls: the dimension selector with the mixing closure reads
  `K1-BRIDGE-NOT-ESTABLISHED`; the `d = 0` control weakened reads `K1-BRIDGE-NOT-ESTABLISHED`; the one-axis control
  weakened reads `K1-BRIDGE-NOT-ESTABLISHED`; a positivity clause returned to `maxCone Ω` reads
  `K1-BRIDGE-NOT-ESTABLISHED`; the note-token reader finds exactly the stated tokens.
- **N1–N3** as EFF-1: declaration list and kinds, preamble and context blocks, statements, definitions and
  structures, no `sorry`, `admit`, `axiom` or `native_decide`, every frozen print present. Mutations: a renamed
  declaration; a changed `variable` block; a changed `open` line; a changed hypothesis of `jointStatesOf_eq`; a
  `sorry`; a removed print.
- **I, C.** `OIBridge.lean` and the census as above, compared byte for byte. Controls: the frozen import edit passes
  and an unchanged file fails; the frozen census passes and a changed status, a moved family, a whitespace change and
  the unchanged file fail.

`controls.py`:
- is blob `5cbb445e3f85fe28d513b7d1d90fa7358d70054b` (895 lines), generated from the reference tree by `gen_controls.py`;
- was frozen, and this revision committed, before any outcome of the predicted execution tree was read;
- `--self-test` passes 57 checks: the blob read, the 16 checks of the reference module and its reading by the
  decision rule (`K1-EFFECT-AVAILABILITY-DISCHARGED`), the embedded DIM-1 texts against `D`, 30 module mutation
  controls each failing with its named code, the result-note phrase control, four decision-rule controls, the
  note-token control, and the import and census controls.

### Count facts

- the module carries **10** frozen `#print axioms` lines (S9) and 13 declarations;
- `tools/lean_axiom_check.py` counts distinct short names (`declared_prints`); none of the 10 short names occurs at
  `D`, so the prints add 10 names;
- the release gate's `lean-axioms` step printed **5743** named results on design run 2
  (37434770553); at `D` it reports 5733.

## Evidence ledger

Each row is discharged at `E` by the exact-head run at `E` and by `controls.py check E --freeze F`.

| Row | Kernel identifiers | Evidence required at `E` | Control |
|---|---|---|---|
| relative forms | `NativeGateOf`, `jointStatesOf`, `EntanglingOf` | built; the frozen texts | S1 |
| transport | `nativeGate_of_cone_eq`, `jointStatesOf_eq`, `entangling_of_cone_eq` | built; axioms within `[propext, Classical.choice, Quot.sound]` | S4, S8 |
| availability | `nativeGate_of_avail`, `entangling_of_avail` | as above | S3, S4 |
| selectors | `dim_of_nativeGateOf`, `three_of_nativeGateOf` | as above | S2, S3, V |
| controls | `cone_eq_fails_zero`, `cone_eq_fails_axis` | as above | S4, S8, V |
| verdict | `k1b_core` | as above | S4, V |
| count | the 10 prints | each within the three axioms; `lean-axioms` passes | S9 |

## Design evidence

Design runs (`workflow_dispatch`; the Mathlib bridge job and the release gate read):

| Run | Branch, commit | Workflow run | Result |
|---|---|---|---|
| 1 | `claude/k1b-dev` `300fcb83` (from `D`: the module with its `open` line in one two-line form; the import after `EffectSpace`; the census family after EFF-1's) | 37434227020 | **green**: all 32 jobs `success`; the Mathlib bridge (job 112171981433) built the module with each of the 10 `#print axioms` lines within `[propext, Classical.choice, Quot.sound]`, no error; release gate PASS (`lean-axioms` 5743 named results, no `sorryAx`); repair history for the `open` line layout only |
| 2 | `claude/k1b-dev` `7577e5eb` (from `D`: the module, blob `835e801dd8a49635f152dac4b0f65abaa6fcfef9`, the same text with the `open` line split in two; the import, blob `09cc2a2bd8b3d45687de7986ae6eb82af3d848dd`; the census, blob `fdca248245907eafcb2a77a383cdbb98eeb75120`) | 37434770553 | **green**: all 32 jobs `success`; the Mathlib bridge (job 112173790986) built the module with each of the 10 `#print axioms` lines within `[propext, Classical.choice, Quot.sound]`, no error and no warning; release gate PASS (`lean-axioms` 5743 named results, no `sorryAx`; `lean-manuscript` OK; 303 legacy records intact; 35 receipts hold); the Lean kernel check (job 112173790899) and the probe aggregate (job 112182155219) succeeded |

Both runs on `claude/k1b-dev` are made from `D`. Run 1 built an earlier text of the module, which differs from the
frozen module only in the layout of its `open` line; it is repair history and anchors nothing in this freeze. Run 2
is the design evidence for the frozen implementation, and the execution blobs of §"The frozen surface" are those of
run 2.

Statement-level choices recorded as frozen, relative to the design study: the relative forms are DIM-1's structures
and definitions with the cone replaced and nothing else changed, so that the bridge is a transport and not a
re-derivation; the gate is named `T` to keep OG-1's `G` for the automorphism family; the selectors carry the same
implicit binders as DIM-1's (`z`, `N`, `T`) and the explicit hypotheses of the decision rule, in that order; the two
EFF-1 controls are restated under the round's own names, the one-axis control strengthened by the effect-soundness
conjunct so that it exhibits a family satisfying effect soundness whose cone is not the maximal cone; no further
control is stated, since the bridge adds no dimension argument to control.

### The predicted execution tree

- **`cf432cfb6c5b47a968a9f252d1028b8f52843568`** (`claude/k1b-predicted`, a single-parent child of `D`) is the execution tree less the result
  note. Its files and blobs:
  - this preregistration in its drafting revision, blob `779db9d76369728fd13cd93b381141f500e09697`, which differs from the revision at `F`
    only in this section;
  - `controls.py`, blob `5cbb445e3f85fe28d513b7d1d90fa7358d70054b`;
  - `K1Bridge.lean`, blob `835e801dd8a49635f152dac4b0f65abaa6fcfef9`;
  - `OIBridge.lean`, blob `09cc2a2bd8b3d45687de7986ae6eb82af3d848dd`;
  - the census, blob `fdca248245907eafcb2a77a383cdbb98eeb75120`.
- `delta(D, cf432cfb)` is exactly those five paths: the record directory's two files and the three execution
  paths.
- At that commit `controls.py check cf432cfb`, run from the tree's own frozen `controls.py`, passes all 19
  checks, and `controls.py verdict cf432cfb` prints `K1-EFFECT-AVAILABILITY-DISCHARGED`.
- **Run 37437438347** (`workflow_dispatch` on `cf432cfb`) completed with conclusion success; every one of its 32 jobs
  succeeded. The Mathlib bridge (job 112182618820) built `OIBridge.K1Bridge` with every frozen `#print axioms` line
  within `[propext, Classical.choice, Quot.sound]`, and its release gate passed every step (`lean-axioms` 5743 named
  results, no `sorryAx`; `lean-manuscript` OK; 303 legacy records intact; 35 receipts hold); the Lean kernel check
  (job 112182618777) and the probe aggregate (job 112188706766) succeeded. Its facts agree with design run 2 at
  `7577e5eb`.

The predicted tree is a sibling of `F` on `D`, not an ancestor of `F`; it and these runs are design evidence, not
attestations.

## Stages

1. **C1** adds `controls.py`, blob `5cbb445e3f85fe28d513b7d1d90fa7358d70054b`, to the record directory. Acceptance: the blob is the frozen
   blob.
2. **S1** adds the module, the import line and the census family in one commit. Acceptance:
   - `controls.py check S1 --freeze F` passes;
   - the exact-head run at S1 has every job green, the Mathlib bridge building the module with every printed axiom set
     within `[propext, Classical.choice, Quot.sound]` and the release gate passing.
3. **Repairs**, if the build at S1 fails, change theorem proofs only; each passes `controls.py check` at its commit. A
   failure that a proof-only repair cannot fix halts the round.
4. **S2** adds the result note `result.md`; this is candidate `E`. Acceptance: `controls.py check E --freeze F` passes
   (the result note included in S7 and V) and the exact-head run at `E` has every job green.

## Outcomes

- **`K1-BRIDGE-1-READ`** — `controls.py check E --freeze F` prints `controls: OK`, `controls.py verdict E` prints
  exactly one outcome, and the exact-head run at `E` is green on every job, the Mathlib bridge building `K1Bridge`
  with every frozen `#print axioms` reporting a subset of `[propext, Classical.choice, Quot.sound]` and the release
  gate passing. The result note states the verdict as its row of the decision rule words it, under the convention for
  DISCHARGED and the non-inference rule; it states that `0 < d` and effect soundness remain explicit hypotheses, that
  body preservation, K∞-Seed, K∞-Trans and K∞-V4 remain unsourced premises, that no mixing closure and no unit premise
  is used, that the verdict does not derive local tomography, product-test completeness or any other composite
  structure of K2, and that no hypothesis is attributed to OI; it leaves the DIM-1 and EFF-1 records as they
  stand.
- **`K1-BRIDGE-1-HALTED`** — anything else; the round halts under the specification's `S12`, and the result note
  names the failing check or job.

No outcome sources any hypothesis, edits the ROADMAP, or identifies the ball's effects with the qubit's operator
effects. Correctness bands are unchanged by either outcome: the round is consistency-axis work, every hypothesis
being a named, unsourced premise.
