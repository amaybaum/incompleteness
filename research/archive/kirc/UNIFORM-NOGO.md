# Native NOT/CNOT algebra selects d = 3 among balls — read-only, from L42

Baseline `fdebc6e3`. This supersedes the dimension-by-dimension treatment in `BALL5-FINITE.md`. Its §1 countermodel
(no control relation) stands; its §2 theorem is recovered here as a special case.
- Exact checks: `uniform_nogo.py` (8 PASS, 0 FAIL, log `uniform_nogo.log`).
- Supporting checks: `ball5_nogo.py` and `ball7.py`.
- Nothing is committed.

## Theorem

Setting:
- **Local systems.** Unit d-balls, with classical corners `u ± z`.
- **Composite.** Locally tomographic, with a closed cone `min ⊆ C ⊆ max`.
- **The native NOT.** A ball involution `N` with `Nz = −z`, acting on both systems.
- **The map.** A linear `G` with `G(C) = C` that acts as CNOT on the corners and satisfies both native relations:
  - `(I⊗N) G (I⊗N) = G`;
  - `(N⊗I) G (N⊗I) = (I⊗N) G`.

Then **d = 3** (or d = 1, the classical bit).

Not used:
- `G² = I`: reversibility is enough, i.e. both `G` and `G⁻¹` map `min` into `max`.
- Any continuous local group.
- Any local symmetry beyond NOT.

## Proof

Notation: `p` and `q` are the dimensions of N's `+1` and `−1` eigenspaces in the transverse space `T` (`p + q = d − 1`),
`V₊ ⊂ T` is the `+1` space, `E₊ = ⟨u⟩ ⊕ V₊`, and `V₋ = (N's −1 space in T) ⊕ ⟨z⟩`.

- **S1 — controlled form** (depth-1 positivity for `G` and `G⁻¹`).
  - `G(|a⟩⊗t) = |a⟩⊗M_a t`, with `M_a` isometries (each a contraction whose inverse is a contraction).
  - `M₁ = N M₀` and `N M₀ = M₀ N`.
- **S2 — first order at the control corners.** Let `c` range over the control's transverse space `T_A`. For every pure
  `t`, the target part of `G(c⊗t)` lies in `ker g⊥(M₀t) ∩ ker g⊥(NM₀t)`. Separating parity and degree gives, for
  `G̃ = G(I⊗M₀⁻¹)`:
  - on `T_A⊗E₊`, the operator-valued matrix `[[0, A_r],[A_r, B_rs]]`, with `B` antisymmetric in `(r, s)`;
  - `T_A⊗V₋` is mapped into itself, antisymmetrically in the `V₋` indices.
- **S3 — the averaging bound.**
  - A target form `[[1, gᵀ],[g, I + K]]` with `K` antisymmetric is Lorentz-positive only if
    `|g|²(1 − 1/p) + ‖K‖²_F/p ≤ 0`. Proof: average `(1 + g·t)² ≥ |g + (I+K)t|²` over the unit sphere of `V₊`.
  - For `p ≥ 2` this forces `g = 0` and `K = 0`. [identity checked symbolically, p = 2…5]
- **S4 — the E₊ block vanishes.**
  - For the state `s = u + c` and the effect `f = u + a`, with any unit `a, c ∈ T_A` and target in `E₊`, the value is
    `gᵀ(I + Γ_{ac})M₀t`, where `Γ_{ac} = [[0, gᵀ],[g, K]]`, `g_r = a·A_r c`, and `K = (a·B_rs c)` is antisymmetric.
  - `M₀` is a Lorentz automorphism, so `I + Γ_{ac}` must be Lorentz-positive.
  - By S3, for `p ≥ 2` all `a·A_r c` and `a·B_rs c` vanish. So `G̃ = 0` on `T_A⊗E₊`, and `G` is singular.
  - **Hence `p ≤ 1`.** [form checked on the complex CNOT and on the d = 5 J/K map]
- **S5 — parity.** On `T_A⊗V₋`, `G` is invertible, and by the control relation it anticommutes with `N_A⊗I`. So it
  exchanges `T₊⊗V₋` and `T₋⊗V₋`, and `p = q`.

**Conclusion.** `p = q ≤ 1` gives `d − 1 = p + q ∈ {0, 2}`. ∎

## Controls and consistency

| check | result |
| --- | --- |
| d = 3, `p = q = 1` | S3 is vacuous at `p = 1`; the complex CNOT satisfies S1–S5 |
| d = 1 | the classical bit, where CNOT is a permutation |
| d = 2 | excluded: `p = q` is impossible with `p + q = 1`, consistent with the disc theorem |
| d = 5 J/K countermodel (`p = 1`, `q = 3`, control relation fails) | allowed by S4, excluded only by S5; it exists, as the theorem requires |
| d = 5 two-pair completions (`p = q = 2`) | all 288 fail positivity |
| d = 7 algebraic candidate (`p = q = 3`: frame, `G² = I`, both relations) | fails positivity; exact witness `s = f = u + x`, `t = u + v₃`, value `1 − √3` |

## Answer to the Clifford question

The selecting constraint is **not** a Clifford or Hurwitz–Radon condition.
- The d = 7 candidate satisfies every algebraic relation. The quaternionic structure on the 4-dimensional `V₋` block is
  not the obstacle.
- It fails on the `E₊` side, by **convex geometry**: the averaging bound S3 allows at most one N-fixed transverse
  direction.
- The native control relation then forces `p = q`.
- So the selector is: *positivity* (S3–S4) forces `p ≤ 1`; the *native NOT/CNOT algebra* (S5) forces `p = q`.
  Neither alone selects d = 3: the J/K countermodel meets S4 with `p = 1` and fails only S5.

## Scope

- **Assumed:**
  - local systems are balls;
  - local tomography, with `min ⊆ C ⊆ max`;
  - `G` is reversible on `C` (`G(C) = C`);
  - both native NOT relations hold. The swap relation is not used.
- **Not decided:** the case where both NOTs act on `C` but the native relations are not imposed. The orbit then need
  not reduce to `{local·G^e}`. The J/K map is a failed instance of this case, not a proof.
- **Outside the ball class:** non-ball local systems, which is Barnum–Wilce territory.
- **Provenance of the steps.** S1 and S2 are hand derivations, supported by the controls above and by the earlier disc
  and d = 5 checks. They are not machine-proved. An exact symbolic re-derivation of S2 in general d would be the next
  verification step.
- **A superseded computation.** An intermediate E₊ solvability scan used the transposed block form `[[0, A_rᵀ],…]`,
  which is incorrect. Its "d = 7 algebraically solvable" output is void and is not cited anywhere above.
