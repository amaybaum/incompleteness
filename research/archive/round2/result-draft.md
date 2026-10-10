# Reconstruction round TRB-1 — the completed-chart adapter, the boundary-state bridge, boundary purity and the invariant-inner-product ball of a boundary-transitive body: RESULT

Run under `AGENTS.md` §A.39 as a native round, in one pull request, #787.

- **`D`** — `7c821261e2537a97b85ab78ae50c6998600bc019`, the head of `main` after round L3B landed, certified by push
  run 37216282113.
- **`F`** — `30fb26f89c24f72f189f97401fc6ca3d08fa7105`, parent `2980b90eedda1f6fb18ef651f60a11982c9ce3ea`;
  `delta(D, F)` is the preregistration alone, blob `70c3c34447b5e3caf6bea97682bd840631e732ff`. Its exact-head
  `workflow_dispatch` run 37224683945 concluded `success` with all 32 jobs succeeded, its `check-run` attestation; the
  owner designated `F` (comment 5983275605). That run attests the control plane only.
- **Shape** — non-sealing; stages C1 and S1 and this note (S2).

**Outcome:** `TRB-1-BALL-PROVED`

The round proves that a compact convex body with nonempty interior, boundary transitive under a body-preserving
family of affine automorphisms, is the closed ball of its invariant inner product about its centroid, and an affine
image of the coordinate Euclidean ball of its own dimension. It defines no notion of the order of a map and states no
implication from transitivity to order.

In the kernel, in coordinates `Fin d → ℝ` and for the chart body of a completion chart (`CompletionAction`):

- **the completed-chart adapter** (`chartBody_isCompact`, `chartBody_convex`, `chartBody_interior_nonempty`): the
  chart body of every completion chart is compact, convex and has nonempty interior, with no finite-dimensionality
  of the completion space;
- **the boundary-state bridge**, one theorem per direction (`frontier_of_isBoundaryState`,
  `isBoundaryState_of_frontier`): a boundary state in the kernel's segment sense is a frontier point, and a point of
  a convex body with interior that is not interior is a boundary state; the ray from an interior point in any
  nonzero direction meets the boundary in a boundary state (`exists_boundary_ray`);
- **TRANS** (`IsBodyGroup`, `TransBody`): a set of affine automorphisms containing the identity, closed under
  composition and inversion, each member mapping the body into itself, and carrying every boundary state to every
  boundary state;
- **boundary purity** (`extreme_of_isBoundaryState_of_transitive`, `not_boundaryTransitive_of_nonextreme_boundary`):
  under a body-preserving boundary-transitive family every boundary state is an extreme point, so a body with a
  non-extreme boundary state is boundary transitive for no body-preserving family;
- **the invariant-inner-product ball** (`centroid_mem`, `centroid_mem_interior`, `boundary_qnorm_const`,
  `eq_qBall_of_boundaryTransitive`): the centroid lies in the body and, under a body-preserving boundary-transitive
  family in dimension `d ≥ 1`, in its interior; every boundary state lies on one sphere of the invariant form
  `Q(v) = v ⬝ᵥ (invMatrix Ω *ᵥ v)` about the centroid; and the body is the closed `Q`-ball
  `{x | Q(x − centroid Ω) ≤ R²}` for some `R > 0`. Only body preservation, all-boundary transitivity and the
  invariant inner product of IIP-1 enter; composition closure is not used, and the proof runs through the ray lemma
  and the sphere lemma, not through any closed-ball lemma stated in the ambient norm;
- **the normalization adapter** (`exists_factor_invMatrix`, `qnorm_eq_sum_sq`, `exists_affine_image_eq_eball`):
  `invMatrix Ω` factors as `Bᵀ * B`; in the linear coordinates `B` defines the invariant form is a sum of squares;
  the body is the image of the coordinate Euclidean ball `eball d` under an affine automorphism of `Fin d → ℝ`;
- **the completed-body and `TransBody` forms** (`chartBody_eq_qBall`, `chartBody_eq_eball`, `eq_qBall_of_transBody`,
  `exists_affine_image_eq_eball_of_transBody`) and `eball_three : eball 3 = ball3`;
- **the controls**: on `ball3`, all affine automorphisms form a transitive body group (`transBody_fullAut3`); the
  Householder reflections with the identity are boundary transitive as a set (`boundaryTransitive_refls3`), with no
  group structure claimed; the rotation family `Set.range rot3` is not transitive (`not_transBody_flow`); the square
  and the octahedron are boundary transitive for no body-preserving family (`not_boundaryTransitive_square2`,
  `not_boundaryTransitive_oct3`);

joined, for the adapter, the two bridge directions, the `Q`-ball, the Euclidean ball and the controls, in the verdict
`trb1_core`.

The ball theorems carry exactly the hypotheses compact, convex, nonempty interior, `0 < d`, `PreservesBody` and
`BoundaryTransitive`; no group, order, flow, seed or drivability hypothesis. The only transitivity predicate is
`BoundaryTransitive`, over all boundary states. The module contains no order predicate, so it carries no edge from
transitivity to order; the order side — ORD∞, composition closure, finite order of stage-preserving data, and whether a
composition-closed transitive family in dimension `≥ 2` has a member of infinite order — is round ORD-1's. The round
supplies no operation, flow or drive, claims no dimension for any body other than `eball 3`, and reads nothing from
round L3B: L3B's outcome is selector evidence for which operation families a later round packages as `OpDatum`
sources, and no premise, hypothesis, control or theorem here refers to it. It edits no manuscript and no roadmap row.

***

## The execution

| commit | content | exact-head run on that commit | conclusion |
| --- | --- | --- | --- |
| `F` = `30fb26f8` | the preregistration | 37224683945 | `success`, all 32 jobs; release gate PASS, `lean-axioms` 5491, as at `D` |
| `C1` = `823e3496` | stage C1: `controls.py`, blob `0451651b` | none required | `controls.py --self-test`: `controls: OK -- 31 checks` |
| `S1` = `9f6468a698f2d855d81f9445f0340af47cc9f724` | stage S1: `TransitiveBody` blob `31f63583`, the import line (`OIBridge.lean` blob `e5394fe8`), the census family (blob `2b709fcb`) | 37226256441 | `success`, all 32 jobs |

Each commit has one parent, the row above it. `S1`'s tree equals that of the predicted execution tree `9e9a00fd`
outside the preregistration. `controls.py check S1 --freeze F` prints `controls: OK -- 20 checks`.

Run 37226256441 is a `workflow_dispatch` run whose `head_sha` is `S1`, run to completion with no job cancelled:

- the Lean kernel check (job 111506414185), the Mathlib bridge (job 111506414328), the 29 numerical-probe shards (act
  42's dispatch-only exclusion shards included) and the probe aggregate (job 111512280510) each concluded `success`;
- the Mathlib bridge built `OIBridge.TransitiveBody` (3629 build jobs);
- each of the 26 frozen `#print axioms` lines of `TransitiveBody` reports `[propext, Classical.choice, Quot.sound]`;
- the release gate passed every step: `lean-axioms` 5517 named results, the 5491 at `D` and the 26 new prints, no
  `sorryAx`; `lean-manuscript` OK with the new census family; 303 legacy records intact; 29 receipts holding.

## The evidence ledger at `S1`

| row | kernel identifiers | status |
| --- | --- | --- |
| adapter | `norm_prepVec_le_one`, `body_subset_closedBall`, `chartBody_isClosed`, `chartBody_isBounded`, `chartBody_isCompact`, `affineSpan_chartBody`, `chartBody_interior_nonempty` | proved; control N2 |
| bridge | `frontier_of_isBoundaryState`, `isBoundaryState_of_frontier`, `exists_boundary_ray` | proved; controls N2, S4 |
| purity | `extreme_image`, `not_mem_interior_of_extreme`, `isBoundaryState_of_extreme`, `extreme_of_isBoundaryState_of_transitive`, `not_boundaryTransitive_of_nonextreme_boundary` | proved; controls N2, S5 |
| ball | `qnorm_smul`, `image_eq_of_preservesBody`, `centroid_fixed_of_preservesBody`, `qnorm_sub_centroid_apply`, `boundary_qnorm_const`, `centroid_mem`, `centroid_mem_interior`, `eq_qBall_of_boundaryTransitive` | proved; controls N2, S3, S9 |
| normalization | `finsuppSum_eq_dot`, `invMatrix_posDef`, `exists_factor_invMatrix`, `qnorm_eq_sum_sq`, `exists_affine_image_eq_eball` | proved; controls N2, S6 |
| forms | `chartBody_eq_qBall`, `chartBody_eq_eball`, `eq_qBall_of_transBody`, `exists_affine_image_eq_eball_of_transBody`, `eball_three` | proved; controls N2, S1 |
| controls | `transBody_fullAut3`, `boundaryTransitive_refls3`, `not_transBody_flow`, `not_boundaryTransitive_square2`, `not_boundaryTransitive_oct3` | proved; controls N2, S7 |
| verdict | `trb1_core` | proved; controls S1–S3 |

## Design evidence

The design runs before `F` are recorded in the preregistration: runs 37219863930, 37220522515, 37220860270 and
37221543291 with proof-only repairs and the one statement-level change (the adapter's matrix row frozen as the
factorization `∃ B, Bᵀ * B = invMatrix Ω`), run 37221769686 on the pre-cut module and run 37223131863 after the
removal of every order predicate (all 32 jobs `success` in each), and the predicted execution tree `9e9a00fd` with run
37223640106 (all 32 jobs `success`). They are design evidence, not attestations, and the pull-request runs on this
branch are not attestations.

## What stays open

Whether a composition-closed boundary-transitive family in dimension `≥ 2` has a member of infinite order (its known
proofs pass through Jordan–Schur or Cartan's closed-subgroup theorem, neither in the pinned Mathlib); the order side of
the architecture, which is round ORD-1's; a source of a body-preserving boundary-transitive family, of reversible
operation data, or of finite rank in an OI construction; dimension three for any body other than `eball 3`; energy
observability, a drive and its continuity; the composite interface.
