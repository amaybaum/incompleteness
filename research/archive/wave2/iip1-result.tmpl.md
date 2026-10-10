# Reconstruction round IIP-1 — the invariant inner product of a convex body's affine automorphisms: RESULT

Run under `AGENTS.md` §A.39 as a native round, in one pull request, #781.

- **`D`** — `f7f5c3b0c621cc3e4b57e3709d11d9d580c81149`, the head of `main` after `OG-1` landed, certified by push
  run 36973928206.
- **`F`** — `722b3470d7cb7767e00331de455d5e2f90e10d26`, parent `f0bdb6b3766f98f3856f1b4dd72dfa24049b10d2`;
  `delta(D, F)` is the preregistration alone, blob `7bfc863974b3bad6123fa9bece4ac8f700f8452f`. Its exact-head
  `workflow_dispatch` run 36983538236 concluded `success` with all 32 jobs succeeded, its `check-run` attestation; the
  owner designated `F`. That run attests the control plane only.
- **Shape** — non-sealing; stages C1 and S1 and this note (S2).

**Outcome:** `IIP-1-INVARIANT-INNER-PRODUCT-PROVED`

In the kernel, with Lebesgue measure on coordinates `Fin n → ℝ`, and with no group, no compactness of a group and no
Haar measure:

- **change of variables** (`abs_det_eq_one`, `setIntegral_comp_eq`): for a measurable body `Ω` of positive volume and
  an affine automorphism `g` with `g '' Ω = Ω`, the linear part of `g` has `|det| = 1` and `∫_Ω h ∘ g = ∫_Ω h`;
- **the common fixed point** (`centroid_fixed`): for a compact body of positive volume, every such `g` fixes the
  centroid of `Ω`;
- **the second moment** (`moment_pos`, `momentMatrix_conj`): the second-moment form of `Ω` about its centroid is
  positive definite when `Ω` has nonempty interior, and its matrix `S` satisfies `A S Aᵀ = S` for the linear part `A`
  of every such `g`;
- **the invariant inner product** (`invariant_inner_product`): for a compact `Ω` with nonempty interior, `S⁻¹` is
  symmetric and positive definite, and every such `g` fixes the centroid and preserves `⟨u, v⟩ = uᵀ S⁻¹ v` through its
  linear part;
- **on the affine span** (`invariant_inner_product_span`): for a compact convex body in a finite-dimensional real
  vector space and an injective affine chart of its affine span, the body read in the chart is compact with nonempty
  interior, its `S⁻¹` is symmetric and positive definite, and the restriction of every affine automorphism of the
  body fixes the restricted centroid and preserves the restricted inner product;
- **ambient nullity** (`momentMatrix_eq_zero_of_subset`, `segment2_moment`): a body contained in a proper affine
  subspace of the coordinate space has a vanishing ambient second-moment matrix, as the segment on the first axis of
  the plane shows, so the positive-definite form exists on the translation space of the affine span and not on the
  ambient space;

joined in the verdict `iip1_core`.

The lemma is premise-free and makes no hypothesis about OI. It claims no ellipsoid, no dimension, no generation or
closure of a rotation group, no compactness of the automorphism group and no boundary transitivity, and it edits no
manuscript and no roadmap row.

***

## The execution

| commit | content | exact-head run on that commit | conclusion |
| --- | --- | --- | --- |
| `F` = `722b3470` | the preregistration | 36983538236 | `success`, all 32 jobs; release gate 21 of 21, `lean-axioms` 5439, as at `D` |
| `C1` = `1ae5a4e2` | stage C1: `controls.py`, blob `e3ab7c64` | none required | `controls.py --self-test`: `controls: OK -- 23 checks` |
| `S1` = `02545b304ce9497d33e203b649fc5e678a32dfcd` | stage S1: `InvariantInnerProduct` blob `282b32f8`, the import line, the census family | @@S1RUN@@ | @@S1CONC@@ |

Each commit has one parent, the row above it. `S1`'s tree equals that of the predicted execution tree `c3359237`
outside the preregistration, and contains nothing of the sibling round `CMP-1`. `controls.py check S1 --freeze F`
prints `controls: OK -- 15 checks`.

@@S1DETAIL@@

## The evidence ledger at `S1`

| row | kernel identifiers | status |
| --- | --- | --- |
| change of variables | `affine_apply_eq`, `setIntegral_comp`, `abs_det_eq_one`, `setIntegral_comp_eq` | proved; control N2 |
| centroid | `centroid_fixed` | proved; control N2 |
| second moment | `moment_eq_dotProduct`, `moment_pos`, `momentMatrix_det_ne_zero`, `moment_transpose_invariant`, `momentMatrix_conj` | proved; controls N2, S2 |
| invariant inner product | `invMatrix_pos`, `invariant_inner_product` | proved; controls N2, S2 |
| affine span | `interior_bodyR_nonempty`, `isCompact_bodyR`, `image_bodyR_eq`, `invariant_inner_product_span` | proved; control S1 |
| ambient nullity | `momentMatrix_eq_zero_of_null`, `momentMatrix_eq_zero_of_subset`, `volume_segment2`, `segment2_moment` | proved; control S3 |
| verdict | `iip1_core` | proved; controls S2, S3, S4 |

## A misattributed identifier in the preregistration

The preregistration's paragraph on the predicted execution tree lists its contents as "this preregistration in its
frozen revision `f0bdb6b3`, `controls.py` blob `e3ab7c64`, the module blob `282b32f8`, `OIBridge.lean` blob
`46e9c1b5` and the census family". Blob `46e9c1b5` is the preregistration at `f0bdb6b3`, not `OIBridge.lean`; the
`OIBridge.lean` of the predicted execution tree, and of `S1`, is blob `d966846a`, which is `D`'s with exactly the
frozen import line (control I). The sentence is descriptive design evidence, and no stage acceptance reads it; the
preregistration is left as frozen.

## Design evidence

The design runs before `F` are recorded in the preregistration: run 36975944833 (five errors), the proof-only repair
`dd06c1f3` with run 36976365427, the owner-directed scoping of the lower-dimensional control with run 36978265025
(reference blob `282b32f8`) and the predicted execution tree `c3359237` with run 36980768233 (all 32 jobs `success`).
They are design evidence, not attestations, and the pull-request runs on this branch are not attestations.

## What stays open

The ellipsoid normalization, boundary transitivity and K∞-R, dimension three, the drive and its source, V4′, and SC∞
and the completion body to which the lemma would be applied.
