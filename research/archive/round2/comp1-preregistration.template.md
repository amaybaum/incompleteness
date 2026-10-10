# Reconstruction round COMP-1 — the weak field-neutral composite interface: PREREGISTRATION

**Status: candidate freeze.** This file is the control plane of a native round under `AGENTS.md` §A.39. It is drafted
on its pull request from `D` and is final only at the commit `F` the owner designates; no commit after `F` changes it.
The frozen surface, the controls, the evidence ledger, the stages and the outcomes below are fixed; the predicted
execution tree is recorded before `F`.

```v3-round
round COMP-1
kind non-sealing
record-directory verification/programmes/oi-qm/reconstruction/round-comp-1-composite-interface/
```

```v3-governed-paths
record AM verification/programmes/oi-qm/reconstruction/round-comp-1-composite-interface/
record AM verification/receipts/COMP-1.json
execution A verification/lean-mathlib/OIBridge/CompositeInterface.lean
execution M verification/lean-mathlib/OIBridge.lean
execution M verification/lean-manuscript-census.json
```

The record directory holds this preregistration, the round's frozen controls `controls.py` and the result note. The
receipt path is `verification/receipts/COMP-1.json`. Every other path the round changes is an execution path listed
above. **No manuscript, no built artifact, `verification/ROADMAP.md`, the workflow, no probe, and no other round's
record change under any outcome.**

## The objects

- **`D`** = `00ee70a60cf59d421c0056619709459d704fae99`, the head of `main` after round ORD-1 landed (push run 37260494801, every job green; the act 42
  exclusion matrix skipped on push).
- **`F`** — the commit carrying this file, which the owner designates; `delta(D, F)` is this file.
- **`E`** — the certified execution head, which the owner designates.
- **`Λ`**, **`Q`** — the reconciliation and the receipt commit, as §A.39 defines them.

## What the round is

No field-neutral notion of a composite system exists at `D`: every composite, register, discard or marginal in the
kernel is typed over `ℂ`, a matrix algebra or a Kronecker product, and the field-neutral modules (`KInfFoundations`,
`OrbitGeneration`, `OrbitNormalization`, `StageCompletion`, `CompletionAction`, `InvariantInnerProduct`,
`TransitiveBody`, `CompositionOrder`) carry one body at a time. This round types the composite of two bodies as a
structure over an arbitrary real carrier, with local tomography as a named premise, and proves the laws of register
attachment, discard, joint reversible action, sharp readout and no-signalling on products from the structure alone:

```
two chart bodies ΩA ⊆ (Fin dA → ℝ), ΩB ⊆ (Fin dB → ℝ) → ProductData on a carrier V → PreComposite (body laws)
  → Composite (one further field: local tomography) → attach, discard, readout, conditional state as definitions
```

1. **Three layers, so that the premise is visible as a premise.** `ProductData dA dB V`: a bi-affine product-state
   map `prodState` and a bilinear product-effect pairing `prodEff` of affine functionals of the two charts into affine
   functionals of `V`, with the evaluation law `prodEff e f (prodState x y) = e x * f y`. `PreComposite ΩA ΩB V`
   extends it by a convex body `Ω ⊆ V` containing the product states, on which every product of effects is an effect
   and the unit pairing is one. `Composite ΩA ΩB V` extends it by the single field `lt`: two states of the body that
   agree on every product of effects are equal. `LocallyTomographic P` is the same proposition as a predicate on a
   pre-composite, so that it can be asserted of one structure as a field and refuted of another as a control.
2. **The operations are definitions, not fields.** Attachment `attach r₀ x := prodState x r₀`; discard
   `margA ω i := prodEff (coord i) 1 ω` in chart coordinates; the conditional state `condA f ω`; the sharp register
   readout `readout f k := prodEff 1 (f k)`; joint reversible action `JointReversible G := PreservesBody Ω G`; the
   minimal body `minBody := convexHull (image2 prodState ΩA ΩB)` and the maximal body `maxBody` of normalized points
   nonnegative on every product of effects.
3. **The laws L1–L11 are theorems of `PreComposite`** (or of `ProductData` where no body enters), so none consumes
   `lt`: the marginal of a product is its factor and attach-then-discard is the identity (L1, L2); pairing with the
   marginal is the unit pairing (L3); the marginal and the conditional state of a composite state are states of a
   compact convex factor body (L4, L8); a sharp readout is a two-outcome test, reads the register on products and is
   certain after attaching the matching register state (L5–L7); no signalling on products (L9); reversible actions
   compose and transport readouts to effects (L10); the body lies between the minimal and the maximal body (L11). The
   one statement that consumes `lt` is the separation clause of L11: on a `Composite` the table of product-effect
   values determines the state (`Composite.pairing_injective`).
4. **The extremal bodies of any product data are pre-composites** (`minPre`, `maxPre`), so every `ProductData` has a
   smallest and a largest body; which body between them is physical is not decided here.
5. **Local tomography is a premise, never a conclusion.** No theorem concludes `LocallyTomographic` of any
   pre-composite or the existence of a `Composite`, except the verdict's two non-vacuity clauses for the named
   instances. The padding control makes the independence explicit: for any pre-composite `P` with nonempty body,
   `paddedPre P` on `V × ℝ` satisfies every field of `PreComposite` and is not locally tomographic, so no `Composite`
   extends it. The eight other fields do not determine `lt`. **This status is binding on later rounds:** a strong
   composite bridge, which would exhibit a composite built from the observer's own stage towers, must prove `lt` for
   its instance or carry it as an explicit hypothesis of every theorem that needs it; nothing in this round licenses
   citing `lt` as established of any composite other than those this module constructs.
6. **Instances.** The classical bit and bit (`bitComposite`, on two copies of `simplex 2`) and two copies of `ball3`
   with the minimal and with the maximal body (`ball3MinComposite`, `ball3MaxComposite`), all on the coordinate model
   `Fin (dA + 1) → Fin (dB + 1) → ℝ`, in which the product pairing separates points and local tomography is a theorem
   of that model (`modelData_ext`, `prodEff_eq_of_eff_eq`). The coordinate model is a function space on index pairs
   and realizes a tensor product; it is confined to the instance sections and enters no statement about the
   interface.
7. **Not stated.** No composite larger than the minimal body is constructed from any source; no local tomography is
   sourced; no nonlocal reversible action, common NOT, gate relation, dimension, drive, transitivity or order
   statement; no availability of any operation; no readout with state update; no stage-level product of two towers;
   no `ℂ`, matrix, Kronecker or tensor-product primitive. The quantum composite is not identified.

### In scope
- the module `OIBridge/CompositeInterface.lean` with the statement surface of §"The frozen surface";
- its import line in `OIBridge.lean` and its family in `lean-manuscript-census.json`;
- `controls.py` and the result note.

### Frozen out
- any theorem concluding local tomography of a pre-composite, or the existence of a composite, beyond the named
  instances; any source of a body strictly between the minimal and the maximal body;
- any statement about a nonlocal gate, a common NOT, the selector `d ∈ {1, 3}`, transitivity, order, a drive, a flow
  or availability (these are rounds DIM-1, TRB-1, ORD-1 and later rounds);
- readout with state update, the stage-level product of two `DirectedStages`, the bridge from completed product
  towers to this interface (a later strong-bridge round);
- any edit to a `ℂ`-typed module, to `NativeGateBall`, to manuscripts or to `verification/ROADMAP.md`;
- anything from round L3B; 3A banking, the EO countermodel round, manuscript follow-ups.

## The frozen surface

**Design-run rule:** compilation failures may cause implementation repairs, but no repair may strengthen or weaken a
frozen theorem statement, structure field or hypothesis without a new preregistration revision and new design theorem
identity.

The design theorem identity is the statement surface of `CompositeInterface` embedded in `controls.py` (blob
`38f1898a82a4ffcacc39383bcb64f8116bbbeeb8`): the preamble, every context block in order, the 101 declarations in order and by kind, every
theorem's signature up to `:=`, every definition and structure whole, and the 64 `#print axioms` lines. The reference
module is blob `91567f53dbaefd847a5017d3562f536ea5ca47fa` (`claude/comp1-dev3` at `d8e6d384`, from `D`: the module of
`claude/comp1-dev` at `cb37b45b` with one header sentence reworded and no declaration changed). A repair may change
proofs only. `OIBridge.lean` is `D`'s with `import OIBridge.CompositeInterface` inserted directly after
`import OIBridge.CompositionOrder` (blob `b1a8b89a6e18969bf1840fdc5b3ce330e1e843fb`). The census is `D`'s with one family, embedded in
`controls.py`, inserted directly after the ORD-1 family (blob `ba36fdd4a6ad64a1fe77aafe21f569e64028a633`).

### The principal statements

| Row | Identifier | Statement |
|---|---|---|
| ST | `ProductData`, `PreComposite`, `Composite`, `LocallyTomographic`, `SharpReadout` | the structures and the predicate of §1 and §3, whole: `ProductData` with fields `prodState`, `prodState_combo_left`, `prodState_combo_right`, `prodEff`, `prodEff_apply`; `PreComposite extends ProductData` with `Ω`, `convex`, `prod_mem`, `prodEff_effect`, `prodEff_unit`; `Composite extends PreComposite` with `lt` alone; `SharpReadout` with `y`, `f`, `pd`, `sum_eq` |
| OP | `attach`, `margA`, `condA`, `readout`, `JointReversible`, `minBody`, `maxBody` | the definitions of §2, whole |
| L1–L2 | `margA_prodState`, `margA_attach` | `D.margA (D.prodState x y) = x`; `D.margA (D.attach r₀ x) = x` |
| L3 | `eff_margA` | `(hω : ω ∈ P.Ω) (e) : e (P.margA ω) = P.prodEff e (unitEff dB) ω` |
| L4 | `margA_mem` | `(hcA : IsCompact ΩA) (hconvA : Convex ℝ ΩA) {ω : V} (hω : ω ∈ P.Ω) : P.margA ω ∈ ΩA` |
| L5 | `readout_sum`, `isEffectOn_readout`, `sum_eq_unitEff_of_affineSpan` | `(R : SharpReadout ΩB) (hω : ω ∈ P.Ω) : P.readout R.f 0 ω + P.readout R.f 1 ω = 1`; each readout of a pair of register effects is an effect on the body; `f 0 + f 1 = unitEff dB` follows from perfect distinguishability when the register body affinely spans its chart |
| L6 | `readout_prodState` | `D.readout f k (D.prodState x y) = f k y` |
| L7 | `readout_attach` | `(R : SharpReadout ΩB) (k) (x) : P.readout R.f k (P.attach (R.y k) x) = 1` |
| L8 | `condA_mem` | `(hcA : IsCompact ΩA) (hconvA : Convex ℝ ΩA) (hf : IsEffectOn ΩB f) (hω : ω ∈ P.Ω) (hne : P.prodEff (unitEff dA) f ω ≠ 0) : P.condA f ω ∈ ΩA` |
| L9 | `condA_prodState` | `(hy : f y ≠ 0) (x) : D.condA f (D.prodState x y) = x` |
| L10 | `jointReversible_words`, `isEffectOn_readout_seedTransport` | `P.JointReversible G → P.JointReversible (words G)`; a readout transported along a member of a joint reversible family is an effect on the body |
| L11 | `minBody_subset`, `subset_maxBody`, `Composite.pairing_injective` | `P.toProductData.minBody ΩA ΩB ⊆ P.Ω`; `P.Ω ⊆ P.toProductData.maxBody ΩA ΩB`; on a `Composite`, `ω ↦ (e, f) ↦ C.prodEff e f ω` is injective on `C.Ω` |
| EXT | `minPre`, `maxPre` | the minimal and the maximal body of any product data are pre-composites |
| MOD | `Model.modelData`, `Model.modelData_ext`, `prodEff_eq_of_eff_eq`, `Model.minComposite`, `Model.maxComposite` | the coordinate model; its pairing separates points; agreement on effect pairs extends to all pairs over factor bodies on which affine functionals are bounded; the minimal and maximal composites of two compact factor bodies in the model |
| INST | `bitComposite`, `ball3MinComposite`, `ball3MaxComposite`, `bitComposite_nonempty`, `ball3MinComposite_nonempty`, `ball3Min_subset_ball3Max` | the three instances, their nonemptiness, and L11 on the ball pair |
| PAD | `paddedPre`, `not_locallyTomographic_paddedPre`, `no_composite_over_paddedPre`, `paddedBall3`, `not_locallyTomographic_paddedBall3`, `no_composite_over_paddedBall3` | the padding control of §5 on any pre-composite with nonempty body, and on the ball pair |
| core | `comp1_core` | L1–L11 for every product datum, pre-composite or composite; the two instance non-vacuity clauses; L11 on the ball pair; the two padding negatives |

Supporting declarations frozen with the surface: `unitEff`, `unitEff_apply`, `unitEff_linear`, `coord`,
`coord_apply`, `coord_linear`, `isEffectOn_unitEff`, `isEffectOn_unitEff_sub`, `evalAddHom`, `affine_sum_apply`,
`affine_eval`, `affine_expand`, `BoundedAffine`, `boundedAffine_of_isCompact`, `exists_effect_rescale`,
`exists_effect_neg`, `attach_combo`, `margA_combo`, `prodEff_expand`, `eff_condA`, `nonempty_of`,
`isEffectOn_minBody`, `unit_eq_one_minBody`, `maxBody_convex`, `isEffectOn_maxBody`, the coordinate-model
vocabulary `Carrier`, `hom`, `coeff`, `pState`, `pEffLin`, `pEff`, `basisEff` with their lemmas,
`simplex_isCompact`, `zero_mem_ball3`, `vec10_mem_simplex`, `padEff`, `padEff_apply`.

### Semantic guards (in `controls.py`)

- **S1 field-neutral.** None of the tokens `ℂ`, `Complex`, `TensorProduct`, `⊗`, `kronecker`, `Kronecker`,
  `Matrix`, `Hilbert`, `InnerProductSpace`, `Bell` occurs in the module; every `import` line is
  `OIBridge.CompletionAction` or a `Mathlib.*` module; the header carries "Local tomography is a premise field of the
  structure, not a theorem". Mutations: a `TensorProduct` import; a declaration over `ℂ`.
- **S2 the premise is never concluded.** No theorem's conclusion contains `LocallyTomographic` other than negated,
  `Nonempty (Composite …)` or `∃ C : Composite …` other than negated — except `comp1_core`, whose conclusion carries
  exactly the two clauses `Nonempty (Composite (simplex 2) (simplex 2) (Carrier 2 2))` and
  `Nonempty (Composite ball3 ball3 (Carrier 3 3))`; the field `lt` is assigned only in `Model.minComposite` and
  `Model.maxComposite`. Mutations: `theorem lt_of_pre (P : PreComposite …) : LocallyTomographic P`; `lt` assigned in
  `paddedPre`.
- **S3 abstract carrier, bodies from the fields.** `Composite` is a `structure` over `(V : Type)` extending
  `PreComposite ΩA ΩB V` and names no `Carrier`; `minBody` is `convexHull ℝ (Set.image2 D.prodState ΩA ΩB)`;
  `maxBody` is the set-builder `{ω | D.prodEff (unitEff dA) (unitEff dB) ω = 1 ∧ … 0 ≤ D.prodEff e f ω}`;
  `prodState` and `prodEff` are assigned only in `Model.modelData` and `paddedPre`. Mutation: `Composite` fixed to
  the carrier `Fin (dA + 1) → Fin (dB + 1) → ℝ`.
- **S4 scope.** Outside the model, instance and padding sections (§E to the verdict) no statement names `Carrier`,
  `pState`, `pEff`, `pEffLin`, `hom`, `coeff`, `modelData`, `basisEff`, `Fin 3`, `ball3`, `simplex` or `paddedBall3`;
  none of the tokens `CNOT`, `NativeGate`, `Entangling`, `BlockData`, `BoundaryTransitive`, `TransBody`, `OrdInf`,
  `InfiniteOrderOn`, `FiniteOrderOn`, `invMatrix`, `ElementaryDrivability`, `CopyNatural`, `finrank`, `SCInf`,
  `FiniteRank`, `LocalExt`, `Drive`, `avail`, `CompletionChart`, `chartBody`, `OpDatum` occurs in the code; the
  verdict's first clause is L1. Mutations: `Fin 3` in a §C law; a declaration named `NativeGate`.
- **S5 operations are definitions; laws are theorems.** `attach`, `margA`, `condA`, `readout`, `minBody`,
  `maxBody` are `def`s and `JointReversible` an `abbrev`; none is a field of the three structures; each of the
  fourteen law theorems of rows L1–L11 is a `theorem` with its `#print axioms` line. Mutation: `margA` made a field
  of `PreComposite`.
- **S6 the structures carry exactly their fields.** `ProductData` has the five fields of row ST, `PreComposite`
  the five, `Composite` the one field `lt` with the frozen body, and `LocallyTomographic` is that body as a predicate
  on `P`. Mutation: a second field beside `lt`.
- **S7 layering.** Every law of rows L1–L11 except `Composite.pairing_injective` is stated over `ProductData` or
  `PreComposite`, with no `Composite` in its statement. Mutation: `eff_margA` restated with `(C : Composite ΩA ΩB V)`.
- **S8 the conditional laws carry their conditions.** `margA_mem` carries `(hcA : IsCompact ΩA)` and
  `(hconvA : Convex ℝ ΩA)` with conclusion `P.margA ω ∈ ΩA`; `condA_mem` carries the same two, `(hf : IsEffectOn ΩB f)`
  and `(hne : P.prodEff (unitEff dA) f ω ≠ 0)` with conclusion `P.condA f ω ∈ ΩA`; `readout_sum` takes
  `(R : SharpReadout ΩB)`, and `SharpReadout` has the field `sum_eq : f 0 + f 1 = unitEff dB`. Mutation: `IsCompact`
  dropped from `margA_mem`.
- **S9 the padding control and the instances.** `paddedPre` is a `def` with `prodState x y := (P.prodState x y, 0)`
  and `Ω := P.Ω ×ˢ Set.Icc (0 : ℝ) 1`; `not_locallyTomographic_paddedPre (hne : P.Ω.Nonempty) : ¬ LocallyTomographic
  (paddedPre P)` and `no_composite_over_paddedPre (hne : P.Ω.Nonempty) : ¬ ∃ C : Composite ΩA ΩB (V × ℝ),
  C.toPreComposite = paddedPre P` are theorems; the three instances are `def`s; these and the ball-pair padding
  theorems and the two `_nonempty` theorems carry prints. Mutations: the padding print removed; the padded body
  collapsed to `Set.Icc (0 : ℝ) 0`.
- **N1–N3** as ORD-1: declaration list and kinds, binder contexts (a `variable` block with its continuation lines),
  statements, definitions and structures, no `sorryAx`; every `#print axioms` within
  `[propext, Classical.choice, Quot.sound]`.

`controls.py`:
- is blob `38f1898a82a4ffcacc39383bcb64f8116bbbeeb8` (SHA-256 `a8ec9c36f4a1bedbdf97ea38aa8f8d5d8326ffbb935e0303a9735e8180f11b73`, 1084 lines), carried by the predicted
  execution tree on the disposable branch `claude/comp1-predicted`;
- was frozen, and this revision committed, before any outcome of the predicted execution tree was read;
- `--self-test` passes 36 checks; its 18 module mutation controls each fail with their named code, and the import and
  census controls each pass the frozen edit and fail a dropped line or a changed status.

## Evidence ledger

Each row is discharged at `E` by the exact-head run at `E` and by `controls.py check E --freeze F`.

| Row | Kernel identifiers | Evidence required at `E` | Control |
|---|---|---|---|
| chart vocabulary | `isEffectOn_unitEff`, `isEffectOn_unitEff_sub`, `affine_sum_apply`, `affine_eval`, `affine_expand`, `boundedAffine_of_isCompact`, `exists_effect_rescale`, `exists_effect_neg` | built; axioms standard | N2 |
| structures | `ProductData`, `PreComposite`, `Composite`, `LocallyTomographic`, `SharpReadout` | elaborate; frozen fields | S3, S6 |
| operations | `attach`, `margA`, `condA`, `readout`, `JointReversible`, `minBody`, `maxBody`, `attach_combo`, `margA_combo`, `prodEff_expand`, `eff_condA` | built; axioms standard | S5 |
| laws | `margA_prodState`, `margA_attach`, `eff_margA`, `margA_mem`, `readout_sum`, `isEffectOn_readout`, `sum_eq_unitEff_of_affineSpan`, `readout_prodState`, `readout_attach`, `condA_mem`, `condA_prodState`, `jointReversible_words`, `isEffectOn_readout_seedTransport`, `minBody_subset`, `subset_maxBody`, `nonempty_of` | as above | S5, S7, S8 |
| separation | `Composite.pairing_injective` | as above | S2, S7 |
| extremal bodies | `isEffectOn_minBody`, `unit_eq_one_minBody`, `minPre`, `maxBody_convex`, `isEffectOn_maxBody`, `maxPre` | as above | S3 |
| model | `Model.hom_zero` … `Model.modelData_ext` (18 prints), `prodEff_eq_of_eff_eq`, `Model.minComposite`, `Model.maxComposite` | as above | S2, S4 |
| instances | `simplex_isCompact`, `zero_mem_ball3`, `vec10_mem_simplex`, `bitComposite`, `ball3MinComposite`, `ball3MaxComposite`, `bitComposite_nonempty`, `ball3MinComposite_nonempty`, `ball3Min_subset_ball3Max` | as above | S9 |
| padding | `padEff_apply`, `paddedPre`, `not_locallyTomographic_paddedPre`, `no_composite_over_paddedPre`, `paddedBall3`, `not_locallyTomographic_paddedBall3`, `no_composite_over_paddedBall3` | as above | S2, S9 |
| verdict | `comp1_core` | as above | S2, S4 |

## Design evidence

Design runs (Mathlib bridge job read only):

| Run | Branch, commit | Workflow run | Bridge result |
|---|---|---|---|
| 1 | `claude/comp1-dev` `35fffce5` (from `afa66d16`, TRB-1's landing) | 37234667174 | red: the section needed `noncomputable`; `ext` on a Pi-domain affine map resolved to `pi_ext_nonempty'` and was replaced by explicit `AffineMap.ext`; the `basisEff` case split needed its motive; several `congrArg` forms |
| 2 | `claude/comp1-dev` `42ea6713` | 37235206086 | red on one error: `Set.ext` form in `simplex_isCompact` |
| 3 | `claude/comp1-dev` `cb37b45b` | 37236372977 | **green**: built; every `#print axioms` line of the module `[propext, Classical.choice, Quot.sound]`; release gate PASS; all 32 jobs `success` (bridge job 111536178282, kernel check 111536178258) |
| 4 | `claude/comp1-dev3` `d8e6d384` (from `D`; the module of run 3 with the header sentence reworded, blob `91567f53`; import after `CompositionOrder`; census family after ORD-1's) | 37261154814 | **green**: built (3631 jobs); each of the 64 `#print axioms` lines of the module `[propext, Classical.choice, Quot.sound]`; release gate PASS (lean-axioms 5616 named results, the 5552 at `D` and the 64 new prints, no sorry; lean-manuscript OK with the COMP-1 family after ORD-1's; 31 receipts hold; legacy 303); all 32 jobs `success` (bridge job 111608482263, kernel check 111608482252, probe aggregate 111611746399) |

Runs 1–3 were made on TRB-1's landing `afa66d16`, before round ORD-1 landed; they are the module's repair history
and carry no evidence for this freeze. Run 4 is the design evidence on `D`.

Mathlib names at `v4.33.0` the module relies on, settled by the design runs: `AffineMap.ext` must be named explicitly (the `ext` tactic on
`(Fin d → ℝ) →ᵃ[ℝ] ℝ` picks `pi_ext_nonempty'`); `Set.mem_ofPred_eq` for set-builder membership;
`geometric_hahn_banach_closed_point` for the separation of a point from a compact convex set;
`Convex.combo_affine_apply` for affine maps on convex combinations; `continuous_finsetSum`;
`Metric.isCompact_of_isClosed_isBounded`; `LinearMap.mk₂` for the bilinear pairing; `Fin.cons`, `Fin.cases`,
`Fin.sum_univ_succ` for the homogeneous coordinates.

Statement-level differences from the design document (`COMP-1-DESIGN.md`), all made before any design run and
recorded here as the frozen choices: the carrier `V` is a parameter with `NormedAddCommGroup`/`NormedSpace ℝ`
instances rather than a structure field with `AddCommGroup`/`Module` (the separation theorem for L4 and L8 and the
padding carrier `V × ℝ` need the normed structure); the structure is layered in three (`ProductData`,
`PreComposite`, `Composite`) so that every law is stated without `lt`; L5 takes a `SharpReadout` carrying the
functional identity `sum_eq`, derived separately from a spanning register body (`sum_eq_unitEff_of_affineSpan`);
L4 and L8 carry `IsCompact ΩA` and `Convex ℝ ΩA`; agreement on effect pairs extends to all pairs under
`BoundedAffine` of the factor bodies (`prodEff_eq_of_eff_eq`); the stage-level product of two `DirectedStages` and
the attach `StageMap` are not in this round. Statement changes forced by the design runs: none. The header's
disclaimer named a nonlocal-correlation inequality by a proper name in runs 1–3; the reference module names it
descriptively, so that the proper name can be a forbidden token of S1.

### The predicted execution tree

- **`@@PRED@@`** (`claude/comp1-predicted`, a single-parent child of `D`) is the execution tree less the result
  note. Its files and blobs:
  - this preregistration in its drafting revision `@@PREREG_DRAFT_COMMIT@@`, blob `@@PREREG_DRAFT_BLOB@@`;
  - `controls.py`, blob `38f1898a82a4ffcacc39383bcb64f8116bbbeeb8`;
  - `CompositeInterface.lean`, blob `91567f53`;
  - `OIBridge.lean`, blob `b1a8b89a6e18969bf1840fdc5b3ce330e1e843fb`;
  - the census, blob `ba36fdd4a6ad64a1fe77aafe21f569e64028a633`.
- `delta(D, @@PRED@@)` is exactly those five paths: the record directory's two files and the three execution paths.
  It adds no gate, selector, transitivity, order, drive or flow module, and no file other than these.
- At that commit `controls.py check @@PRED@@`, run from the tree's own frozen `controls.py`, passes all 18 checks.
- **Run @@PRED_RUN@@** (`workflow_dispatch` on `@@PRED@@`) @@PRED_RESULT@@

These runs are design evidence, not attestations.

## Stages

1. **C1** adds `controls.py`, blob `38f1898a82a4ffcacc39383bcb64f8116bbbeeb8`, to the record directory. Acceptance: the blob is the frozen
   blob.
2. **S1** adds the module, the import line and the census family in one commit. Acceptance:
   - `controls.py check S1 --freeze F` passes;
   - the exact-head run at S1 has every job green, the Mathlib bridge building the module with every printed axiom
     set within `[propext, Classical.choice, Quot.sound]` and the release gate passing.
3. **Repairs**, if the build at S1 fails, change proofs only; each passes `controls.py check` at its commit. A failure
   that a proof-only repair cannot fix halts the round.
4. **S2** adds the result note `result.md`; this is candidate `E`. Acceptance: `controls.py check E --freeze F` passes
   and the exact-head run at `E` has every job green.

## Outcomes

- **`COMP-1-INTERFACE-PROVED`** — `controls.py check E --freeze F` prints `controls: OK`, and the exact-head run
  at `E` is green on every job, the Mathlib bridge building `CompositeInterface` with every frozen `#print axioms`
  reporting a subset of `[propext, Classical.choice, Quot.sound]` and the release gate passing. The result note
  states: the three-layer structure with local tomography as its one premise field; the operations as definitions;
  L1–L11 as theorems of the pre-composite, with the separation clause the only consumer of `lt`; the extremal
  pre-composites; the three instances on the coordinate model; the padding control, so that `lt` is independent of
  the other eight fields — and that no composite larger than the minimal body is constructed, no local tomography is
  sourced, and the quantum composite is not identified. It states, for later rounds, that `lt` is a hypothesis to
  prove or carry, never an established fact of a composite this module did not construct.
- **`COMP-1-HALTED`** — anything else; the round halts under the specification's `S12`, and the result note names the
  failing check or job.

No outcome sources local tomography or a composite beyond the minimal body, states a gate, a selector, a dimension,
transitivity, order, a drive or availability, or identifies the quantum composite.
