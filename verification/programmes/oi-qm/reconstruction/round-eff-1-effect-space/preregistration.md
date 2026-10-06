# Reconstruction round EFF-1 — the effect set and the product-test cone of the ball: PREREGISTRATION

**Status: candidate freeze.** This file is the control plane of a native round under `AGENTS.md` §A.39. It is drafted
on its pull request from `D` and is final only at the commit `F` the owner designates; no commit after `F` changes it.
The two questions, the decision rule, the non-inference rule, the frozen surface, the controls, the evidence ledger,
the stages and the outcomes below are fixed; the predicted execution tree is recorded before `F`.

```v3-round
round EFF-1
kind non-sealing
record-directory verification/programmes/oi-qm/reconstruction/round-eff-1-effect-space/
```

```v3-governed-paths
record AM verification/programmes/oi-qm/reconstruction/round-eff-1-effect-space/
record AM verification/receipts/EFF-1.json
execution A verification/lean-mathlib/OIBridge/EffectSpace.lean
execution M verification/lean-mathlib/OIBridge.lean
execution M verification/lean-manuscript-census.json
```

The record directory holds this preregistration, the round's frozen controls `controls.py` and the result note. The
receipt path is `verification/receipts/EFF-1.json`. Every other path the round changes is an execution path listed
above. **No manuscript, no built artifact, `verification/ROADMAP.md`, the workflow, no probe and no other round's
record change under any outcome.**

## The objects

- **`D`** = `e9882f968522c178b6ed55f954535ce77305d2e6`, the head of `main` after the roadmap and audit change #794
  landed (merge of `bbddfe18`; its exact-head `workflow_dispatch` run 37411380245 had all 32 jobs succeed, and the
  push run 37412609474 at `D` succeeded, the act 42 exclusion matrix skipped on push).
- **`F`** — the commit carrying this file, which the owner designates; `delta(D, F)` is this file.
- **`E`** — the certified execution head, which the owner designates.
- **`Λ`**, **`Q`** — the reconciliation and the receipt commit, as §A.39 defines them.

## What the round is

Round DIM-1's selector consumes its effect set only through the maximal product cone
`maxCone (eball d) = {ω | ∀ e f, IsEffectOn (eball d) e → IsEffectOn (eball d) f → 0 ≤ prodEffVal e f ω}` (in
`NativeGate.posFwd`, `NativeGate.posInv` and, through `jointStates`, `Entangling`), at every `d`. This round asks two
separate questions about that premise, on the coordinate Euclidean ball `eball d` of `TransitiveBody`, for every
`d ≥ 1`, and answers each by a frozen decision rule read from the kernel statements.

- **Q-CONE.** Do OG-1's named hypotheses on `eball d`, with no mixing closure, make available a family of test
  functionals whose products determine exactly DIM-1's `maxCone (eball d)`?
- **Q-SET.** Do OG-1's named hypotheses on `eball d` make every affine effect of `eball d` available, and if only with
  an added resource, which?

OG-1's named hypotheses are `PreservesBody (eball d) G` (body preservation), `SharpSeed (eball d) r` (K∞-Seed),
`BoundaryTransitive (eball d) G` (K∞-Trans) and `SeedOrbitAvailable G r avail` (K∞-V4), in the labels of
`verification/ROADMAP.md` and `verification/audits/foundations/kinf-seams-audit.md` at `D`. All four are named,
unsourced premises. The named mixing closure is `unitEff d ∈ avail` together with `MixingClosed avail` (closure under
sub-convex binary combinations `α • e + β • f`, `α, β ≥ 0`, `α + β ≤ 1`).

**Convention for DERIVED.** A verdict ending in DERIVED means: derived in the kernel from the named hypotheses already
carried by the certified corpus — the four above — without adding the mixing closure. It is a theorem relative to
those hypotheses. It never means derived from OI, and never that the physical completion has the effects in
question.

### The decision rule (frozen; implemented by `controls.py verdicts`)

Each question's outcome is read from the theorem statements of the module at `E`, independently of the other
question. A question with no outcome, or with more than one, has no verdict, and the round halts.

| Question | Outcome | Rule |
|---|---|---|
| Q-CONE | `CONE-DERIVED` | a theorem whose explicit binders are exactly `(hd : 0 < d)` and the four hypotheses, with conclusion `sharpFamily d ⊆ avail ∧ maxConeOf (sharpFamily d) = maxCone (eball d)`, and the two inclusions `maxCone (eball d) ⊆ maxConeOf (sharpFamily d)` and `maxConeOf (sharpFamily d) ⊆ maxCone (eball d)` (the latter under `0 < d`) as theorems |
| Q-CONE | `CONE-CONDITIONAL` | the same conclusion and inclusions, with the binders the four hypotheses, `0 < d`, `unitEff d ∈ avail` and `MixingClosed avail` |
| Q-CONE | `CONE-INSUFFICIENT` | a theorem concluding a family with the four hypotheses, `unitEff d ∈ avail`, `MixingClosed avail` and `EffectsOn (eball d) avail` whose cone `maxConeOf avail` is not `maxCone (eball d)` |
| Q-SET | `DERIVED-FULL-EFFECTS` | a theorem whose explicit binders are exactly `(hd : 0 < d)` and the four hypotheses, with conclusion `fullEffects (eball d) ⊆ avail` |
| Q-SET | `CONDITIONAL-FULL-EFFECTS` | that conclusion with the binders the four hypotheses, `0 < d`, `unitEff d ∈ avail` and `MixingClosed avail`, **and** the countermodel `not_fullEffects_of_orbit` with its frozen conclusion: for every `0 < d` a family satisfying the four hypotheses under the full automorphism family, containing the unit and consisting of effects, that is neither mixing closed nor the full effect set |
| Q-SET | `INSUFFICIENT-EVEN-WITH-MIXING` | a theorem concluding a family with the four hypotheses, `unitEff d ∈ avail` and `MixingClosed avail` from which some effect is missing |

Under `CONDITIONAL-FULL-EFFECTS` the round records the mixing closure (the unit and `MixingClosed`) as an unsourced
OPEN premise and does not mark DIM-1's effect premise discharged. The design runs below already exhibit a module read
by this rule as `CONE-DERIVED` and `CONDITIONAL-FULL-EFFECTS`; the rule, not that reading, is what this file freezes,
and the verdicts at `E` are those `controls.py verdict E` prints.

### The non-inference rule (frozen)

> Q-CONE is about which test functionals determine the dual product cone; it does not assert that every affine effect
> is operationally available. Q-SET is about operational availability; it does not by itself establish the cone
> equality unless the corresponding coverage theorem is proved.

The result note states each verdict separately, in the words of its row above, and states neither as a consequence of
the other. Under `CONE-DERIVED` with `CONDITIONAL-FULL-EFFECTS` it may say exactly: availability of the full affine
effect set is not needed for DIM-1's cone, relative to body preservation, K∞-Seed, K∞-Trans and K∞-V4, which the round
does not source; obtaining every individual affine effect still requires the named mixing closure, which remains
OPEN; and neither verdict bears on K∞-Stage or K∞-Act, upstream of the ball.

### In scope
- the module `OIBridge/EffectSpace.lean` with the statement surface of §"The frozen surface";
- its import line in `OIBridge.lean` and its family in `lean-manuscript-census.json`;
- `controls.py` and the result note.

### Frozen out
- any source of body preservation, K∞-Seed, K∞-Trans, K∞-V4, the unit or the mixing closure, and any statement that OI
  supplies them; anything about K∞-Stage, K∞-Act, K∞-Drive, K∞-Copy or K∞-Geom;
- a limit closure, a drive or flow, a complex or matrix representation, the qubit's operator effects;
- the unbiased family `{(1 + b · r)/2 : |b| ≤ 1}` of the earlier design, which the round does not state;
- any edit to `CompositeDimension`, `OrbitGeneration`, `TransitiveBody`, `CompositeInterface`, a manuscript,
  `verification/ROADMAP.md` or any other round's record.

## The frozen surface

**Design-run rule:** compilation failures may cause implementation repairs, but no repair may strengthen or weaken a
frozen theorem statement, definition or hypothesis without a new preregistration revision and new design theorem
identity.

The design theorem identity is the statement surface of `EffectSpace` embedded in `controls.py` (blob `2ed4dab5d3ffd813850980243fd1c7e620dbec35`):
the preamble (imports, namespaces, `open`, `variable {d : ℕ}`), the context blocks in order, the 78 declarations in
order and by kind, every theorem's signature up to `:=`, every definition whole, and the 31 `#print axioms` lines. The
reference module is blob `5fad51a773310ac053e4c1952e72a9c941daa8c2`. A repair may change theorem proofs only. `OIBridge.lean` is `D`'s with `import
OIBridge.EffectSpace` inserted directly after `import OIBridge.CompositeDimension`. The census is `D`'s with one
family, embedded in `controls.py`, inserted directly after the DIM-1 family (modules `["CompositeDimension"]`), in
`D`'s two-space JSON layout.

### The principal statements

| Row | Identifier | Statement |
|---|---|---|
| SHARP | `sharpVec`, `sharpEff`, `sharpFamily` | `sharpEff b x = 1/2 + ∑ j, b j / 2 * x j` (`affOf (sharpVec b)`); `sharpFamily d := {e \| ∃ b, ∑ j, b j ^ 2 = 1 ∧ e = sharpEff b}` |
| SPHERE | `isBoundaryState_eball_of_sphere`, `sphere_of_isBoundaryState_eball` | the boundary states of `eball d` are the unit vectors, one theorem per direction |
| NORM | `sharp_eq_of_certain` | `IsEffectOn (eball d) r → u ∈ eball d → w ∈ eball d → r u = 1 → r w = 0 → ∑ j, u j ^ 2 = 1 ∧ r = sharpEff u` |
| GEN | `sharpFamily_subset_avail`, `seedOrbit_eq_sharpFamily` | the four hypotheses `⟹ sharpFamily d ⊆ avail`; with the first three, `seedOrbit G r = sharpFamily d` (two inclusions by name) |
| CONE | `maxConeOf`, `maxCone_subset_maxConeOf_sharp`, `maxConeOf_sharp_subset_maxCone`, `maxConeOf_sharpFamily` | `maxConeOf A := {ω \| ∀ e ∈ A, ∀ f ∈ A, 0 ≤ prodEffVal e f ω}`; `maxCone (eball d) ⊆ maxConeOf (sharpFamily d)`; `(hd : 0 < d) : maxConeOf (sharpFamily d) ⊆ maxCone (eball d)`; the equality from both by name |
| Q-CONE | `cone_of_orbit`, `maxConeOf_avail_eq` | `(hd : 0 < d)` and the four hypotheses `⟹ sharpFamily d ⊆ avail ∧ maxConeOf (sharpFamily d) = maxCone (eball d)`; with `EffectsOn (eball d) avail` as well, `maxConeOf avail = maxCone (eball d)` |
| UPPER | `effect_eq_affine`, `isEffectOn_of_affine` | `IsEffectOn (eball d) e ↔`-free pair: an effect is `x ↦ a + ∑ j, v j * x j` with `√(∑ j, v j ^ 2) ≤ min a (1 − a)`, and conversely |
| DECOMP | `unitSpan`, `fullEffects_subset_unitSpan`, `unitSpan_subset_fullEffects`, `fullEffects_eq_unitSpan` | `(hd : 0 < d) : fullEffects (eball d) ⊆ unitSpan (sharpFamily d)`; the converse; the equality from both by name |
| Q-SET | `MixingClosed`, `fullEffects_subset_avail`, `avail_eq_fullEffects`, `not_fullEffects_of_orbit` | `(hd)`, the four hypotheses, `(hU : unitEff d ∈ avail) (hM : MixingClosed avail) ⟹ fullEffects (eball d) ⊆ avail`; with `EffectsOn` the equality; the countermodel of the rule's `CONDITIONAL-FULL-EFFECTS` row, on `fullAut d` with `sharpUnitFamily d` |
| AUT | `fullAut`, `reflLin`, `reflAff`, `boundaryTransitive_fullAut` | the full automorphism family of `eball d` and the reflection exchanging two unit vectors; `BoundaryTransitive (eball d) (fullAut d)` |
| CTL | `maxConeOf_sharpFamily_zero_ne`, `axisFamily`, `maxConeOf_axis_ne`, `not_boundaryTransitive_of_countable` | at `d = 0` the sharp family is empty and its cone is not `maxCone (eball 0)`; at `d = 3` the effects of one axis with the unit give a strictly larger cone (directional coverage is load-bearing; at `d = 1` one axis is the whole sharp family); a countable family is never boundary transitive on `eball 3` |
| core | `eff1_core` | the cone equality, `cone_of_orbit`, the upper bound, the decomposition, the conditional generation, the countermodel for every `0 < d`, and the three controls |

### Semantic guards (in `controls.py`)

Each lists the mutation controls `--self-test` drives through it, every one of which must fail with the named code.

- **S1 Q-CONE.** The two inclusions are theorems with their frozen statements and prints; `maxConeOf_sharpFamily` is
  proved from both by name (§A.34); `cone_of_orbit` has exactly `(hd : 0 < d)` and the four hypotheses;
  `sharpFamily_subset_avail` has exactly the four hypotheses; neither contains `MixingClosed`, `unitEff` or
  `EffectsOn`. Mutations: the mixing closure added to the cone theorem; one inclusion dropped from the equality's
  proof; an effect premise on the generation theorem; `0 < d` added to the free inclusion.
- **S2 Q-SET.** The upper bound and the decomposition in both directions with their frozen statements and prints; the
  equality proved from both inclusions by name; `fullEffects_subset_avail` with exactly `0 < d`, the four hypotheses,
  the unit and `MixingClosed`; `not_fullEffects_of_orbit` with its frozen conclusion and print. Mutations: the mixing
  closure dropped from the set generation; the countermodel weakened to leave `MixingClosed` unrefuted; the upper bound
  with a weaker radius.
- **S3 definitions.** `maxConeOf`, `MixingClosed`, `EffectsOn`, `unitSpan`, `sharpFamily`, `sharpEff`, `sharpVec`,
  `fullAut`, `sharpUnitFamily` are the frozen texts whole; `maxConeOf` quantifies over the given family; `MixingClosed`
  is sub-convex. Mutations: the cone restricted to normalized effects; the mixing closure made convex.
- **S4 premises.** No theorem concludes `SharpSeed`, `PreservesBody`, `BoundaryTransitive`, `SeedOrbitAvailable`,
  `MixingClosed` or `EffectsOn` except the named witness theorems (`sharpEff_sharpSeed`, `preservesBody_fullAut`,
  `boundaryTransitive_fullAut`, `not_fullEffects_of_orbit`) with their frozen conclusions and prints, the verdict,
  where `MixingClosed` occurs only negated or as an antecedent, and the negated control
  `¬ BoundaryTransitive (eball 3) G`. Mutations: the mixing closure concluded from the seed orbit; seed-orbit
  availability concluded for a hypothesis-bound family.
- **S5 reuse.** No declaration has the name of a landed object it reads (`maxCone`, `Lor`, `ehom`, `affOf`,
  `IsEffectOn`, `fullEffects`, `eball`, `mem_eball`, the OG-1 predicates, `seedTransport`, `seedOrbit`, `unitEff`,
  `prodEffVal`, `pairVal`, `ballEffect`, `directionalFamily`, `lor_ehom`, `lor_pair_bound`); every import is
  `OIBridge.CompositeDimension`, `OIBridge.CompositeInterface` or a Mathlib module. Mutations: `maxCone` re-declared;
  an import of `OIBridge.SubstratumSource`.
- **S6 neutral.** No complex, conjugate-transpose, positive-semidefinite, trace, qubit, Bloch, Pauli, density, drive,
  flow, limit-closure, tensor-product or Hilbert token in the module's code. Mutations: a complex scalar; a limit
  closure.
- **S7 phrases.** The module header and, at a commit carrying it, the result note contain none of "OI supplies",
  "derived from OI", "sourced from OI", "mixing closure is derived", "full effect set is derived", "effect premise is
  discharged", "qubit effect space" (case-insensitive, whitespace-normalized). Mutation: "OI supplies the effects." in
  the header; a note string with "mixing closure is derived" (and a neutral note passes).
- **S8 dimension.** `0 < d` occurs in exactly the frozen set of statements (`axisVec`, `axisVec_sq`, `lor_decomp`,
  `nonneg_of_sharp`, `maxConeOf_sharp_subset_maxCone`, `maxConeOf_sharpFamily`, `cone_of_orbit`,
  `maxConeOf_avail_eq`, `fullEffects_subset_unitSpan`, `fullEffects_eq_unitSpan`, `fullEffects_subset_avail`,
  `avail_eq_fullEffects`, `not_fullEffects_of_orbit`, `eff1_core`); outside §F and the verdict no dimension-three object
  (`Fin 3`, `eball 3`, `W 3`, `HVec 3`, `ball3`, `eball_three`) occurs. Mutations: `0 < d` added to the generation
  theorem; a dimension-three object in the generation section.
- **S9 count.** Exactly the 31 frozen `#print axioms` lines, in order and distinct, each naming a declaration of the
  module. Mutations: an extra print; a duplicated print.
- **V verdicts.** The decision rule yields exactly one outcome per question; at a commit carrying the result note, the
  note contains exactly the two computed outcome tokens and no other. Controls: the cone theorem with the mixing
  closure reads `CONE-CONDITIONAL`; the set theorem without the unit and the mixing closure reads
  `DERIVED-FULL-EFFECTS`; without the frozen countermodel Q-SET has no verdict; a countermodel with the mixing closure
  reads `INSUFFICIENT-EVEN-WITH-MIXING` and two outcomes fail V; a cone countermodel with the mixing closure reads
  `CONE-INSUFFICIENT`; a derived set theorem beside the conditional one fails V; the note-token reader finds exactly
  the stated tokens.
- **N1–N3** as DIM-1: declaration list and kinds, preamble and context blocks, statements and definitions, no `sorry`,
  `admit`, `axiom` or `native_decide`, every frozen print present. Mutations: a renamed declaration; a changed
  `variable` block; a changed `open` line; a changed hypothesis of `sharpEff_self`; a `sorry`; a removed print.
- **I, C.** `OIBridge.lean` and the census as above, compared byte for byte. Controls: the frozen import edit passes
  and an unchanged file fails; the frozen census passes and a changed status, a moved family, a whitespace change and
  the unchanged file fail.

`controls.py`:
- is blob `2ed4dab5d3ffd813850980243fd1c7e620dbec35` (1269 lines), generated from the reference tree by `gen_controls_eff1.py`;
- was frozen, and this revision committed, before any outcome of the predicted execution tree was read;
- `--self-test` passes 55 checks: the blob read, the 16 checks of the reference module and its reading by the decision
  rule (`CONDITIONAL-FULL-EFFECTS`, `CONE-DERIVED`), 26 module mutation controls each failing with its named code, the
  result-note phrase control, eight decision-rule controls (two of them mutations that must fail V), and the import and
  census controls.

### Count facts

- the module carries **31** frozen `#print axioms` lines (S9);
- `tools/lean_axiom_check.py` counts distinct short names (`declared_prints`); none of the 31 short names occurs at
  `D`, so the prints add 31 names;
- the release gate's `lean-axioms` step printed **5733** named results on design run 1 (37413453969) on `ec3cfa5a`; at `D` it
  reports 5702.

## Evidence ledger

Each row is discharged at `E` by the exact-head run at `E` and by `controls.py check E --freeze F`.

| Row | Kernel identifiers | Evidence required at `E` | Control |
|---|---|---|---|
| sharp effects | `sharpEff_isEffectOn`, `sharpEff_sharpSeed`, `isBoundaryState_eball_of_sphere`, `sphere_of_isBoundaryState_eball`, `sharp_eq_of_certain` | built; axioms within `[propext, Classical.choice, Quot.sound]` | N2, S3 |
| automorphisms | `preservesBody_fullAut`, `reflLin_swap`, `boundaryTransitive_fullAut` | as above | S4 |
| generation | `seedTransport_mem_sharpFamily`, `sharpFamily_subset_avail`, `seedOrbit_eq_sharpFamily` | as above | S1 |
| cone | `maxConeOf_fullEffects`, `lor_decomp`, `nonneg_of_sharp`, `maxCone_subset_maxConeOf_sharp`, `maxConeOf_sharp_subset_maxCone`, `maxConeOf_sharpFamily`, `cone_of_orbit`, `maxConeOf_avail_eq` | as above | S1, V |
| set | `effect_eq_affine`, `isEffectOn_of_affine`, `fullEffects_subset_unitSpan`, `unitSpan_subset_fullEffects`, `fullEffects_eq_unitSpan`, `fullEffects_subset_avail`, `avail_eq_fullEffects`, `not_fullEffects_of_orbit` | as above | S2, V |
| controls | `maxConeOf_sharpFamily_zero_ne`, `maxConeOf_axis_ne`, `not_boundaryTransitive_of_countable` | as above | S8 |
| verdict | `eff1_core` | as above | S4, V |
| count | the 31 prints | each within the three axioms; `lean-axioms` passes | S9 |

## Design evidence

Design runs (`workflow_dispatch`; the Mathlib bridge job and the release gate read):

| Run | Branch, commit | Workflow run | Result |
|---|---|---|---|
| history | `claude/eff1-gen-dev`, from `bd5de8f5` (#793's landing), commits `ac3d8a5e`, `2a4381a0` | 37360536874, 37361193865 | repair history only: the first failed on four proof errors; the second built the module with its bridge green while hosted-runner assignment cancelled its aggregate probe job |
| 1 | `claude/eff1-dev2` `ec3cfa5a` (from `D`: the module, blob `5fad51a773310ac053e4c1952e72a9c941daa8c2`; the import after `CompositeDimension`; the census family after DIM-1's) | 37413453969 | **green**: all 32 jobs `success`; the Mathlib bridge (job 112106791785) built the module with each of the 31 `#print axioms` lines within `[propext, Classical.choice, Quot.sound]`; release gate PASS (`lean-axioms` 5733 named results, no `sorryAx`; `lean-manuscript` OK; 303 legacy records intact; 34 receipts hold) |

The runs on `claude/eff1-gen-dev` were made from `bd5de8f5`, before `D`; they are repair history and anchor nothing
in this freeze. Run 1 is the design evidence on `D`, and the execution blobs of §"The frozen surface" are those of run 1.

Statement-level choices recorded as frozen, relative to the design study: the geometry is stated on `eball d` for
every `d`, with `0 < d` where the cone and the decomposition need a unit vector, not on `ball3`; the sharp effects are
`affOf (sharpVec b)`, DIM-1's affine functional, not OG-1's `ballEffect`; the full automorphism family `fullAut d` and
its reflections are new, so that the countermodel holds at every `0 < d`; the unbiased family is not stated; the
directional-coverage control is at `d = 3`, since at `d = 1` one axis is the whole sharp family; no limit closure.

### The predicted execution tree

- **`20968f52e8ded2b3e6c05ddb5f6447526206abaf`** (`claude/eff1-predicted`, a single-parent child of `D`) is the execution
  tree less the result note. Its files and blobs:
  - this preregistration in its drafting revision, blob `3bbb3b7f49985d98b7b7b49b97bd0f6239443f54`, which differs from the revision at `F`
    only in this section;
  - `controls.py`, blob `2ed4dab5d3ffd813850980243fd1c7e620dbec35`;
  - `EffectSpace.lean`, blob `5fad51a773310ac053e4c1952e72a9c941daa8c2`;
  - `OIBridge.lean`, blob `4d0cf54b8f5dba8d1168bf3cbe2b34d62c5a99dc`;
  - the census, blob `b3e63cf6d2aaba652806a58674629c943e0b11c0`.
- `delta(D, 20968f52)` is exactly those five paths: the record directory's two files and the three execution paths.
- At that commit `controls.py check 20968f52`, run from the tree's own frozen `controls.py`, passes all 19 checks, and
  `controls.py verdict 20968f52` prints `CONDITIONAL-FULL-EFFECTS` and `CONE-DERIVED`.
- **Run 37415025699** (`workflow_dispatch` on `20968f52`) completed with conclusion success; every one of its 32 jobs
  succeeded. The Mathlib bridge (job 112111649908) built `OIBridge.EffectSpace` with every frozen `#print axioms` line
  within `[propext, Classical.choice, Quot.sound]`, and its release gate passed every step (`lean-axioms` 5733 named
  results, no `sorryAx`; `lean-manuscript` OK; 303 legacy records intact; 34 receipts hold); the Lean kernel check
  (job 112111649978) and the probe aggregate (job 112115795752) succeeded. Its facts agree with design run 1 at
  `ec3cfa5a`.

The predicted tree is a sibling of `F` on `D`, not an ancestor of `F`; it and these runs are design evidence, not
attestations.

## Stages

1. **C1** adds `controls.py`, blob `2ed4dab5d3ffd813850980243fd1c7e620dbec35`, to the record directory. Acceptance: the blob is the frozen blob.
2. **S1** adds the module, the import line and the census family in one commit. Acceptance:
   - `controls.py check S1 --freeze F` passes;
   - the exact-head run at S1 has every job green, the Mathlib bridge building the module with every printed axiom set
     within `[propext, Classical.choice, Quot.sound]` and the release gate passing.
3. **Repairs**, if the build at S1 fails, change theorem proofs only; each passes `controls.py check` at its commit. A
   failure that a proof-only repair cannot fix halts the round.
4. **S2** adds the result note `result.md`; this is candidate `E`. Acceptance: `controls.py check E --freeze F` passes
   (the result note included in S7 and V) and the exact-head run at `E` has every job green.

## Outcomes

- **`EFF-1-READ`** — `controls.py check E --freeze F` prints `controls: OK`, `controls.py verdict E` prints exactly one
  Q-SET outcome and exactly one Q-CONE outcome, and the exact-head run at `E` is green on every job, the Mathlib bridge
  building `EffectSpace` with every frozen `#print axioms` reporting a subset of `[propext, Classical.choice,
  Quot.sound]` and the release gate passing. The result note states the two verdicts separately, as their rows of the
  decision rule word them, under the convention for DERIVED and the non-inference rule; under
  `CONDITIONAL-FULL-EFFECTS` it records the unit and `MixingClosed` as an unsourced OPEN premise and does not mark
  DIM-1's effect premise discharged; it states that body preservation, K∞-Seed, K∞-Trans and K∞-V4 are named premises
  the round does not source, and that neither verdict bears on K∞-Stage or K∞-Act.
- **`EFF-1-HALTED`** — anything else; the round halts under the specification's `S12`, and the result note names the
  failing check or job.

No outcome sources body preservation, K∞-Seed, K∞-Trans, K∞-V4, the unit or the mixing closure, edits the ROADMAP, or
identifies the ball's effects with the qubit's operator effects. Correctness bands are unchanged by either outcome: the
round is consistency-axis work, every hypothesis being a named, unsourced premise.
