# Reconstruction round TRB-1 — the completed-chart adapter, the boundary-state bridge, boundary purity and the invariant-inner-product ball of a boundary-transitive body: PREREGISTRATION

**Status: candidate freeze.** This file is the control plane of a native round under `AGENTS.md` §A.39. It is drafted
on its pull request from `D` and is final only at the commit `F` the owner designates; no commit after `F` changes it.
The frozen surface, the controls, the evidence ledger, the stages and the outcomes below are fixed; the predicted
execution tree is recorded before `F`.

```v3-round
round TRB-1
kind non-sealing
record-directory verification/programmes/oi-qm/reconstruction/round-trb-1-transitive-body/
```

```v3-governed-paths
record AM verification/programmes/oi-qm/reconstruction/round-trb-1-transitive-body/
record AM verification/receipts/TRB-1.json
execution A verification/lean-mathlib/OIBridge/TransitiveBody.lean
execution M verification/lean-mathlib/OIBridge.lean
execution M verification/lean-manuscript-census.json
```

The record directory holds this preregistration, the round's frozen controls `controls.py` and the result note. The
receipt path is `verification/receipts/TRB-1.json`. Every other path the round changes is an execution path listed
above. **No manuscript, no built artifact, `verification/ROADMAP.md`, the workflow, no probe, and no other round's
record change under any outcome.**

## The objects

- **`D`** = `7c821261e2537a97b85ab78ae50c6998600bc019`, the head of `main` after round L3B landed (push run
  37216282113, every job green; the act 42 exclusion matrix skipped on push). The owner designated it as the drafting
  snapshot of architectural round 2.
- **`F`** — the commit carrying this file, which the owner designates; `delta(D, F)` is this file.
- **`E`** — the certified execution head, which the owner designates.
- **`Λ`**, **`Q`** — the reconciliation and the receipt commit, as §A.39 defines them.

## What the round is

Four landed rounds supply the pieces of a single-system geometry statement and leave them disconnected:
CMP-1 gives the completed body of a directed stage system and its chart (`StageCompletion`, `CompletionAction`),
OPACT-1 gives the affine automorphisms of the chart body that reversible operation data induce, IIP-1 gives every
automorphism of a compact body with interior a common fixed point and an invariant inner product, and OG-1 states
boundary transitivity (`BoundaryTransitive`) and body preservation (`PreservesBody`) as named hypotheses. This round
connects them, in one module and with no new physical premise:

1. **The completed-chart adapter.** The chart body of any completion chart is compact, convex and has nonempty
   interior in `Fin d → ℝ`, proved without finite-dimensionality of the completion space `ℓ^∞`, so IIP-1's
   `Fin n` theorem applies to it directly.
2. **The boundary-state bridge.** The kernel's relative boundary states (`IsBoundaryState`, segment-based) and the
   topological frontier coincide in a convex body with interior, one theorem per direction (§A.34).
3. **TRANS, frozen.** `TransBody Ω G := IsBodyGroup Ω G ∧ BoundaryTransitive Ω G`: a set of affine automorphisms
   containing the identity, closed under composition and inversion, each member mapping the body into itself, and
   carrying every boundary state to every boundary state. Continuity is definitional in the chart (finite dimension)
   and is not a field.
4. **Boundary purity.** Under a body-preserving boundary-transitive family every boundary state is an extreme
   point, so a body with a non-extreme boundary state admits no such family: the finite-stage polytopes (the
   square, the Level-3A octahedron) fail TRANS by theorem.
5. **The invariant-inner-product ball (principal).** A compact convex body with interior in `Fin d → ℝ` that is
   boundary transitive under a body-preserving family is the closed ball of its invariant inner product about its
   centroid: `Ω = {x | (x − c) ⬝ᵥ (invMatrix Ω *ᵥ (x − c)) ≤ R²}`. Only body preservation, all-boundary
   transitivity and IIP-1 enter; composition closure is not used. The `TransBody` form is a corollary.
6. **The normalization adapter (frozen as statements).** `invMatrix Ω` factors as `Bᵀ * B`; in the linear
   coordinates `B` defines the invariant form is a sum of squares; hence the body is an affine image of
   the coordinate Euclidean ball `eball d = {x | ∑ j, x j ^ 2 ≤ 1}` of its own dimension `d`, and at `d = 3` of
   `KInfFoundations.ball3`.
7. **No order predicate.** The module defines and uses no notion of the order of a map: no `InfiniteOrderOn`,
   `FiniteOrderOn`, `OrdInf`, `MulClosed`, iterated operation data or iterate `g^[m]` occurs in it. The order side
   of the architecture — ORD∞, composition closure, finite order of stage-preserving data, and the open question
   whether a composition-closed transitive family in dimension ≥ 2 has a member of infinite order (whose known
   proofs pass through Jordan–Schur or Cartan's closed-subgroup theorem, neither in Mathlib `v4.33.0`) — is round
   ORD-1's, on its own spine from OPACT composition. This round therefore carries **no edge from transitivity to
   order**, by construction and by guard S2. Its controls are the transitivity side only: on `ball3`, all
   automorphisms (a transitive body group), the Householder reflections (boundary transitive as a set), the
   rotation flow (not transitive), and the polytope exclusions.

The dependency picture the round freezes:

```
chart completion (CMP-1, OPACT-1) → §1 adapter → §2 bridge → all-boundary transitivity + IIP-1 → §5 Q-ball → §6 eball d
                      no order predicate in the module; ORD∞ is ORD-1's object, with no edge from TRANS here
```

### In scope
- the module `OIBridge/TransitiveBody.lean` with the statement surface of §"The frozen surface";
- its import line in `OIBridge.lean` and its family in `lean-manuscript-census.json`;
- `controls.py` and the result note.

### Frozen out
- any order predicate (`InfiniteOrderOn`, `FiniteOrderOn`, `OrdInf`, `MulClosed`, `iterAfter`, iterates) and any
  derivation of ORD∞ from TRANS: round ORD-1's, not reported here beyond the sentence in §7;
- the ambient-norm route to the ball through `KInfFoundations.eq_closedBall_of_frontier_subset_sphere`: the ball
  theorem is proved in the invariant quadratic form by the ray argument (guard S9);
- any statement with `3`, `ball3`, `Fin 3` or `finrank … = 3` in a principal conclusion (the `d = 3` corollary
  `eball_three` and the `ball3` controls are the only `Fin 3` statements);
- energy observability, DIM3, any flow or `ElementaryDrivability`, `SharpSeed`, `SeedOrbitAvailable`, SC∞,
  `BinaryVisible`, any OI sourcing of `FiniteRank`, stage consistency or operation data;
- anything from round L3B: its outcome is cited in §0 of the result note only as the selector evidence that
  motivates which operation families a later round packages as `OpDatum` sources; no premise, hypothesis,
  control or theorem here refers to it;
- 3A banking, the EO countermodel round, manuscript follow-ups.

## The frozen surface

**Design-run rule:** compilation failures may cause implementation repairs, but no repair may strengthen or weaken a
frozen theorem statement or hypothesis without a new preregistration revision and new design theorem identity.

The design theorem identity is the statement surface of `TransitiveBody` embedded in `controls.py` (blob
`0451651b5d407cfc3651b627cb68b84c4a0965fa`): the preamble, every context line in order, the 70 declarations in order
and by kind, every theorem's signature up to `:=`, every definition and the structure whole, and the 26
`#print axioms` lines. The reference module is blob `31f63583ec1b6451f77cc519b19914e4bd3ebb51` (`claude/trb1-dev` at
`7de2d549`). A repair may change proofs only. `OIBridge.lean` is `D`'s with `import OIBridge.TransitiveBody` inserted
directly after `import OIBridge.CompletionAction` (blob `e5394fe8ee055d275f4968302ea834bffd1ac8a0`). The census is
`D`'s with one family, embedded in `controls.py`, inserted directly after the OPACT-1 family (blob
`2b709fcbe6989da411829e06ad5675b1499a43eb`).

### The principal statements

| Row | Identifier | Statement |
|---|---|---|
| ADP | `chartBody_isCompact`, `chartBody_convex`, `chartBody_interior_nonempty` | for every `C : CompletionChart D`: `chartBody C` is compact, convex, with nonempty interior; no `[FiniteDimensional ℝ (CSpace D)]` |
| BR→ | `frontier_of_isBoundaryState` | `IsBoundaryState Ω x → x ∈ frontier Ω` |
| BR← | `isBoundaryState_of_frontier` | `Convex ℝ Ω → (interior Ω).Nonempty → x ∈ Ω → x ∉ interior Ω → IsBoundaryState Ω x` |
| RAY | `exists_boundary_ray` | from an interior point in a nonzero direction, a last parameter `t > 0` whose point is a boundary state, the segment up to it inside, the ray beyond it outside |
| PUR | `extreme_of_isBoundaryState_of_transitive` | compact, convex, interior, `PreservesBody Ω G`, `BoundaryTransitive Ω G` ⟹ every boundary state is in `Ω.extremePoints ℝ` |
| EXC | `not_boundaryTransitive_of_nonextreme_boundary` | a boundary state that is not extreme ⟹ `¬ BoundaryTransitive Ω G` for every body-preserving `G` |
| CEN | `centroid_mem`, `centroid_mem_interior` | the centroid is in the body; under a body-preserving boundary-transitive family (and `0 < d`) in its interior |
| SPH | `boundary_qnorm_const` | `∃ R ≥ 0, ∀ x, IsBoundaryState Ω x → qnorm Ω (x − centroid Ω) = R ^ 2` |
| **QB** | `eq_qBall_of_boundaryTransitive` | `0 < d → IsCompact Ω → Convex ℝ Ω → (interior Ω).Nonempty → PreservesBody Ω G → BoundaryTransitive Ω G → ∃ R, 0 < R ∧ Ω = qBall Ω R` |
| FAC | `exists_factor_invMatrix` | `IsCompact Ω → (interior Ω).Nonempty → ∃ B : Matrix (Fin d) (Fin d) ℝ, Bᵀ * B = invMatrix Ω` |
| NRM | `qnorm_eq_sum_sq` | `∃ T : (Fin d → ℝ) ≃ₗ[ℝ] (Fin d → ℝ), ∀ v, qnorm Ω v = ∑ j, (T v) j ^ 2` — **the frozen connection between chart coordinates and the invariant norm** |
| EB | `exists_affine_image_eq_eball` | the hypotheses of QB ⟹ `∃ A : (Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ), A '' Ω = eball d` |
| CH | `chartBody_eq_qBall`, `chartBody_eq_eball` | QB and EB for `chartBody C` with `0 < C.d`, through ADP |
| TB | `eq_qBall_of_transBody`, `exists_affine_image_eq_eball_of_transBody` | QB and EB with `TransBody Ω G` in place of the two clauses |
| D3 | `eball_three` | `eball 3 = ball3` |
| C1 | `transBody_fullAut3` | the ball with all its affine automorphisms: `TransBody ball3 fullAut3` |
| C2 | `boundaryTransitive_refls3` | the Householder reflections with the identity: `BoundaryTransitive ball3 refls3`, no group structure claimed |
| C3 | `not_transBody_flow` | the rotation flow: `¬ TransBody ball3 (Set.range rot3)` |
| C4 | `not_boundaryTransitive_square2`, `not_boundaryTransitive_oct3` | the square and the octahedron: boundary transitive for no body-preserving family |
| core | `trb1_core` | ADP, BR→, BR←, QB, EB and C1–C4 together |

### Semantic guards (in `controls.py`)

- **S1 dimension.** No theorem of rows ADP–TB has `3`, `ball3`, `Fin 3` or `finrank` in its statement; `Fin 3`
  appears only in D3 and C1–C4. Mutation: a `3` in QB's conclusion.
- **S2 no order predicate, no TRANS → ORD∞ edge.** `TransBody` unfolds to `IsBodyGroup ∧ BoundaryTransitive`;
  none of the tokens `InfiniteOrderOn`, `FiniteOrderOn`, `OrdInf`, `MulClosed`, `iterAfter`, `orderOf`,
  `Function.iterate`, `^[` occurs anywhere in the module; the import `Mathlib.Analysis.Real.Pi.Irrational` is
  absent. Mutation: a definition `OrdInf` and a theorem `TransBody Ω G → OrdInf Ω G` appended.
- **S3 ball hypotheses.** QB and EB have exactly the hypotheses `0 < d`, `IsCompact`, `Convex ℝ`,
  `(interior Ω).Nonempty`, `PreservesBody`, `BoundaryTransitive`; neither names `IsBodyGroup`, `OrdInf`, a flow,
  `SharpSeed` or `SeedOrbitAvailable`. Mutation: `IsBodyGroup` added to QB.
- **S4 directional bridge.** BR→ and BR← are two theorems; no `↔` between `IsBoundaryState` and `frontier` appears
  without both names in its proof. Mutation: BR← removed.
- **S5 all-boundary transitivity.** The only transitivity predicate is `BoundaryTransitive`, quantifying over
  `IsBoundaryState`; no statement is about transitivity on `extremePoints` or a finite set. Mutation:
  `BoundaryTransitive` replaced by a vertex predicate in `TransBody`.
- **S6 normalization frozen.** NRM is a kernel theorem with its axiom print, with exactly the conclusion
  `∀ v, qnorm Ω v = ∑ j, (T v) j ^ 2`, and EB's proof-independent statement names `eball d`. Mutation: NRM's
  conclusion weakened to an inequality.
- **S7 controls present.** C1–C4 are kernel theorems with axiom prints. Mutation: C2 removed.
- **S8 no L3B.** No identifier, docstring or header text names L3B, a rule, a rank, edge-permutivity or a hidden
  law.
- **S9 ray route.** The identifier `eq_closedBall_of_frontier_subset_sphere` occurs nowhere in the module, and the
  proofs of QB's chain reference `exists_boundary_ray` and `boundary_qnorm_const` (the proof body of
  `eq_qBall_of_boundaryTransitive` names both). Mutation: the identifier inserted in a comment of the module.
- **N1–N3** as IIP-1: declaration list and kinds, binder contexts, no `sorryAx`; every `#print axioms` within
  `[propext, Classical.choice, Quot.sound]`.

`controls.py`:
- is blob `0451651b5d407cfc3651b627cb68b84c4a0965fa` (SHA-256
  `448d8b52b4604957134fe119c856632e0faf42b34882e0fdc240c1d0522a9265`, 805 lines), carried by the predicted
  execution tree on the disposable branch `claude/trb1-predicted`;
- was frozen, and this revision committed, before any outcome of the predicted execution tree was read;
- `--self-test` passes 31 checks. Its 13 module mutation controls each fail with their named code: a removed
  declaration (N1), a changed binder context (N2), a changed statement (N2), a `sorry` (N3), a `3` in the ball
  theorem (S1), an order predicate with a `TransBody → OrdInf` theorem (S2), a group hypothesis on the ball theorem
  (S3), the frontier-to-boundary direction removed (S4), transitivity quantified over extreme points (S5), the
  normalization weakened to an inequality (S6), a control print removed (S7), L3B named (S8), the ambient-norm
  identifier mentioned (S9); the import and census controls each pass the frozen edit and fail a dropped line or a
  changed status.

## Evidence ledger

Each row is discharged at `E` by the exact-head run at `E` and by `controls.py check E --freeze F`.

| Row | Kernel identifiers | Evidence required at `E` | Control |
|---|---|---|---|
| adapter | `norm_prepVec_le_one`, `body_subset_closedBall`, `chartBody_isClosed`, `chartBody_isBounded`, `chartBody_isCompact`, `affineSpan_chartBody`, `chartBody_interior_nonempty` | built; axioms standard | N2 |
| bridge | `frontier_of_isBoundaryState`, `isBoundaryState_of_frontier`, `exists_boundary_ray` | as above | S4 |
| purity | `extreme_image`, `not_mem_interior_of_extreme`, `isBoundaryState_of_extreme`, `extreme_of_isBoundaryState_of_transitive`, `not_boundaryTransitive_of_nonextreme_boundary` | as above | S5 |
| ball | `qnorm_smul`, `image_eq_of_preservesBody`, `centroid_fixed_of_preservesBody`, `qnorm_sub_centroid_apply`, `boundary_qnorm_const`, `centroid_mem`, `centroid_mem_interior`, `eq_qBall_of_boundaryTransitive` | as above | S3 |
| normalization | `finsuppSum_eq_dot`, `invMatrix_posDef`, `exists_factor_invMatrix`, `qnorm_eq_sum_sq`, `exists_affine_image_eq_eball` | as above | S6 |
| forms | `chartBody_eq_qBall`, `chartBody_eq_eball`, `eq_qBall_of_transBody`, `exists_affine_image_eq_eball_of_transBody`, `eball_three` | as above | S1 |
| controls | C1–C4 identifiers | as above | S7 |
| verdict | `trb1_core` | as above | S1–S3 |

## Design evidence

Design runs on `claude/trb1-dev` (disposable branch from `D`; Mathlib bridge job read only):

| Run | Commit | Workflow run | Bridge result |
|---|---|---|---|
| 1 | `099dc4bc` | 37219863930 | red: Mathlib names at `v4.33.0` (`image_openSegment`, `integral_finsetSum`, `abs_add_le`), strict-implicit binders of `extremePoints`, `Matrix.PosDef` in its Finsupp form, vector-literal evaluation |
| 2 | `0e871775` | 37220522515 | red: `Matrix.PosSemidef.sqrt` and `Matrix.PosDef.det_pos` absent; `image_openSegment` field argument; the geometric chain ADP, BR→, BR←, RAY, CEN, SPH, QB and the `ball3` controls built with standard axioms |
| 3 | `f85075c1` | 37220860270 | red: `Matrix.posSemidef_iff_eq_conjTranspose_mul_self` absent; `extremePoints` membership yields `x₁ = x` alone |
| 4 | `9224fd0a` | 37221543291 | red on one name only (`LDL.*` is in the root namespace, not `Matrix.LDL`); every declaration outside the normalization adapter built with standard axioms, PUR, EXC and C4 included |
| 5 | `6932516f` | 37221769686 | **green**: `OIBridge.TransitiveBody` built; every `#print axioms` line of the module `[propext, Classical.choice, Quot.sound]`; release gate PASS in the bridge job (lean-axioms 5520 named results, no sorry; lean-manuscript OK with the provisional TRB-1 census family; 29 receipts hold; legacy 303) |
| 6 | `6027be54` | 37223131863 | **green** after the scope cut: `InfiniteOrderOn`, `OrdInf`, `rot3_mem_fullAut3`, `iterate_rot3_one`, `infiniteOrderOn_rot3_one`, `ordInf_fullAut3`, `ordInf_flow`, `refls3_involutive`, `not_ordInf_refls3` and the import `Mathlib.Analysis.Real.Pi.Irrational` removed (kept for ORD-1); `trb1_core` and the axiom prints reduced accordingly; the module built with each of its 26 `#print axioms` lines reporting exactly `[propext, Classical.choice, Quot.sound]`; release gate PASS (lean-axioms 5517, no sorry; lean-manuscript OK; 29 receipts; legacy 303). The reference blob `31f63583` (`7de2d549`) differs from this commit's module only in two header sentences (no identifier of an ambient-norm lemma, S9) |

Across the six commits no frozen statement changed except the adapter row recorded above (SQR → FAC); the scope cut
removed declarations and changed no surviving one.

Names the normalization adapter needed at `v4.33.0`: `Matrix.LDL.lower_conj_diag` (`L * diag * Lᴴ = S` for
`S.PosDef`), `Matrix.LDL.diagEntries`, `Matrix.LDL.invertibleLowerInv`, `Matrix.PosDef.dotProduct_mulVec_pos`,
`EuclideanSpace.inner_toLp_toLp`, `Matrix.det_eq_zero_of_row_eq_zero`, `Matrix.isUnit_det_of_invertible`,
`Real.mul_self_sqrt`; the factor is `B = diagonal (√ diagEntries) * Lᴴ`. Names the chart/frontier transport needed:
`CompletionAction.isClosedEmbedding_chart`, `coordsOf_mem_chartBody`, `affineSpan_gen`,
`Convex.interior_nonempty_iff_affineSpan_eq_top`, `Convex.openSegment_interior_self_subset_interior`,
`geometric_hahn_banach_closed_point`.

Statement changes forced by the design runs: **none to NRM, EB, QB, CH or TB.** The matrix-form row of the
adapter was drafted as a symmetric square root (`∃ P, Pᵀ = P ∧ P * P = invMatrix Ω ∧ IsUnit P.det`) and is
frozen as the factorization `∃ B, Bᵀ * B = invMatrix Ω` (row FAC): the square-root lemmas are not in the pinned
Mathlib, the factorization is what NRM consumes, and no later row reads the symmetry or the determinant. The
drafted route to QB through `KInfFoundations.eq_closedBall_of_frontier_subset_sphere` (stated in the ambient sup
norm) is not used; QB is proved by the ray argument (RAY) and `boundary_qnorm_const` directly.

### The predicted execution tree

- **`9e9a00fde9019fb2a2bc5a2db0df48ba475bfa14`** (`claude/trb1-predicted`, a single-parent child of `D`) is the
  execution tree less the result note. Its files and blobs:
  - this preregistration in its drafting revision `2980b90e`, blob `6182ddd9`;
  - `controls.py`, blob `0451651b`;
  - `TransitiveBody.lean`, blob `31f63583`;
  - `OIBridge.lean`, blob `e5394fe8`;
  - the census, blob `2b709fcb`.
- `delta(D, 9e9a00fd)` is exactly those five paths: the record directory's two files and the three execution paths.
  It adds no order, flow or drive module, and no file other than these.
- At that commit `controls.py check 9e9a00fd`, run from the tree's own frozen `controls.py`, passes all 18 checks.
- **Run 37223640106** (`workflow_dispatch` on `9e9a00fd`) completed with conclusion success; every one of its 32 jobs
  succeeded. The Mathlib bridge (job 111498763237) built `OIBridge.TransitiveBody` with each of the 26 frozen
  `#print axioms` lines reporting exactly `[propext, Classical.choice, Quot.sound]`, and its release gate passed every
  step (`lean-axioms` 5517 named results, no `sorryAx`; `lean-manuscript` OK; 303 legacy records intact; 29 receipts
  hold). Design run 6 (37223131863, the same module less two header sentences) likewise completed with all 32 jobs
  green.

These runs are design evidence, not attestations.

## Stages

1. **C1** adds `controls.py`, blob `0451651b`, to the record directory. Acceptance: the blob is the frozen blob.
2. **S1** adds the module, the import line and the census family in one commit. Acceptance:
   - `controls.py check S1 --freeze F` passes;
   - the exact-head run at S1 has every job green, the Mathlib bridge building the module with every printed axiom
     set within `[propext, Classical.choice, Quot.sound]` and the release gate passing.
3. **Repairs**, if the build at S1 fails, change proofs only; each passes `controls.py check` at its commit. A failure
   that a proof-only repair cannot fix halts the round.
4. **S2** adds the result note `result.md`; this is candidate `E`. Acceptance: `controls.py check E --freeze F` passes
   and the exact-head run at `E` has every job green.

## Outcomes

- **`TRB-1-BALL-PROVED`** — `controls.py check E --freeze F` prints `controls: OK`, and the exact-head run at `E` is
  green on every job, the Mathlib bridge building `TransitiveBody` with every frozen `#print axioms` reporting a
  subset of `[propext, Classical.choice, Quot.sound]` and the release gate passing. The result note states: the
  adapter, the bridge, boundary purity, the invariant-inner-product ball and its Euclidean normalization in dimension
  `d`, the transitivity controls and the polytope exclusions — and nothing about dimension 3, EO, a drive, the order
  of any map, ORD∞, or OI sourcing.
- **`TRB-1-HALTED`** — anything else; the round halts under the specification's `S12`, and the result note names the
  failing check or job.

No outcome sources an operation, a flow or a drive, claims the order of any map or an implication from transitivity
to order, claims dimension 3 for any body other than `eball 3`, or reads anything from round L3B.
