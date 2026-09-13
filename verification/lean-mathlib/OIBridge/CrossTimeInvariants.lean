import OIBridge.TwoSidedGauge

/-!
# Act 13 — cross-time invariants of the relative evolution

Executed under the frozen control plane
`verification/programmes/oi-qm/track-b/act-13-cross-time-invariants/preregistration.md`, blob
`5d8bee2c616d12c53234c54bfa7efae19dc1dcc1`, from `main` at
`d019718696fd12e4719b5ed5b7d8dfab45544a8c` — the merge commit of that control plane, which the
freeze fixes as this round's mandated base.

## What this round is

A **bounding round**, not a fork and not a classification of a gauge. Act 12 classified the
per-slice quotient exactly; act 11's `GL2` shows the cross-time threading is not fixed even by the
full per-time Gram trajectory. This module freezes **one** family of cross-time data — the two-time
Gram data of the dilation columns, at three resolutions — proves exactly which quotient of the lift
each member computes, and bounds the family from both sides: the anchored-column members are blind
to every strong-right threading by a universal theorem, and the finest member is blind to a
constant left move by an explicit pair.

**The structural point, frozen before anything else.** The two-sided action of act 12 does not act
on relative evolutions: it is time-dependent on both sides, and a time-dependent factor on either
side changes relative objects (`GL2`, `RO1`). The quotient in which the relative evolution lives is
the lift modulo a **constant right** unitary — any unitary, not a gauge class — and that is `CT1`.
Every "determines the relative evolution" here means "determines the lift modulo constant right
unitaries", and every "determines up to" names the exact quotient it means.

## The four budget slots

* `CrossGram` — `Ξ^{(t,s)}(U) = U_tᴴ U_s`, the Gram matrix of the two column families; anchor-free.
* `FibreCrossGram` — `Ξ_i^{(t,s)}(U) = X_i(U_t)ᴴ X_i(U_s)` for the fibre block `X_i` of act 12;
  carries the anchor, and its `(t,t)` slice is act 12's `FibreGram` definitionally.
* `ConstRightRelated` — `U' ≈_R U ⟺ ∃ K unitary, ∀ t, U'_t = U_t K`; the constant unrestricted.
* `ConstLeftRelated` — `U' ≈_L U ⟺ ∃ W unitary, ∀ t, U'_t = W U_t`; likewise.

The two conditional slots are unused: no cross-time phase-equivalence predicate and no
relative-object abbreviation is introduced.

## The targets

* **`CT1`** — `ct1_relative_iff_constRight`: the relative evolution is exactly the lift modulo a
  constant right unitary. Forward by the forced element `K = U_0ᴴ U'_0` (`ct1_forward`); backward
  consumed from act 11's `gl3_constant_gauge_preserves_relative` (`ct1_backward`).
* **`CT2` (a)** — `ct2a_crossGram_iff_constLeft`: the column cross-Gram determines the lift up to
  one constant left unitary, both directions; hence the relative evolution up to conjugation by
  one constant unitary (`ct2a_relative_conj`), which is **not** the identity on relative
  candidates — `CT4` is the certificate.
* **`CT2` (b)** — `ct2b_fibreCrossGram_iff`: the fibre cross-Gram trajectory determines the lift up
  to one constant in-fibre left move and one time-dependent strong right gauge, both directions.
  The forward direction rides on the infinite-family Gram-isometry lemma
  `exists_unitary_of_inner_eq`, stated for an arbitrary index type, and on act 11's orbit theorem.
* **`CT3` (G)** — `ct3g_fibreCrossGram_strong_right`: levels 0, 1 and 2 are invariant under every
  strong-right family, universally.
* **`CT3` (a)** — `ct3a_gl2_pair_separated_by_crossGram`: `GL2`'s pair shares every fibre
  cross-Gram datum and is separated by the entry `((0,1),(1,1))` of `Ξ^{(0,1)}`, values `0` and
  `1`, an off-anchor row.
* **`CT3` (b)** — `ct3b_hadamard_trajectory_control`: act 12's Hadamard pair, whose per-time Gram
  data are inequivalent at `t ≥ 1`, is separated at the smallest level; it is the trajectory-type
  control, not a threading witness.
* **`CT3` (c)** — `ct3c_constant_lift_variant`: the constant-lift variant of `GL2`, whose
  cross-Grams agree on every anchored column at every `t, s`, is separated only at the
  off-anchor × off-anchor entry `((0,1),(0,1))`, values `1` and `0`, with relative candidates `0`
  and `1/4` at `(0,1)`.
* **`CT4`** with **`CL1`** — `ct4_constant_left_obstruction`,
  `cl1_constant_left_moves_relative_candidate`: two coherent lifts of the identity family on
  `V = Fin 2`, `A = Fin 2`, with equal column cross-Grams at every `t, s`, related by the constant
  in-fibre swap `W = P(swap((0,0),(0,1))) ∈ 𝒢_L`, whose relative candidates differ at `(0,0)`: `1`
  against `0`. So no member of the frozen family determines the relative candidate.

## What none of this licenses

No selection principle is named, endorsed or excluded. No connection and no gauge-fixing
mechanism is asserted, in either direction. `P0` is not closed by a characterization: it remains
OPEN and two-part. Nothing here says OI and QM are inequivalent. The cross-Gram data are
coordinates on the lift space, not physical quantities. Nothing is imported from the substratum
Lemma 24.1 round, and nothing here is about Track I. `GL2`, `GL3`, `GI2`, `TG2`, `TG3` and `RO1`
are consumed and none is revised. Level 0 raw equality and level 0 modulo anchored phases are kept
apart: the raw datum is moved by the weak-right action (`fibreCrossGram_mul_weak_apply`), so raw
equality is a stronger, representative-level equality and does not itself compute act 12's
per-slice quotient.
-/

namespace OIBridge
namespace CrossTimeInvariants

open Finset Matrix CausalReadback RootedClassification TransposeBridge BarandesTupleRound
  ContinuousExtension DilationChoice ReadbackRobustness AnchorRobustness CoherentLiftGauge
  TwoSidedGauge

open scoped ComplexOrder

variable {V A : Type} [Fintype V] [DecidableEq V] [Fintype A] [DecidableEq A]

/-! ### Section A — the budget slots -/

/-- **THE COLUMN CROSS-GRAM `Ξ^{(t,s)}`** (act 13's budget slot 1) — `U_tᴴ · U_s`, the Gram matrix
of the two column families `{U_t e_p}_p` and `{U_s e_q}_q`, entrywise `⟨U_t e_p, U_s e_q⟩`.
**Anchor-independent.** Its `(t,t)` slice is the identity for every unitary lift
(`crossGram_self`). -/
def CrossGram (U : ℕ → Matrix (V × A) (V × A) ℂ) (t s : ℕ) : Matrix (V × A) (V × A) ℂ :=
  (U t)ᴴ * U s

/-- **THE FIBRE CROSS-GRAM `Ξ_i^{(t,s)}`** (slot 2) — `X_i(U_t)ᴴ · X_i(U_s)` for act 12's fibre
block `X_i(U) = U.submatrix (i,·) (·,a₀)`, entrywise `⟨P_i U_t e_{(j,a₀)}, P_i U_s e_{(k,a₀)}⟩`.
**Carries the anchor.** Its `(t,t)` slice is act 12's `FibreGram a₀ (U t) i` definitionally
(`fibreCrossGram_diag`), so the per-time Gram trajectory is the diagonal `t = s` of this datum.
Its fibre sum is the anchored block of `CrossGram` (`sum_fibreCrossGram`). -/
def FibreCrossGram (a₀ : A) (U : ℕ → Matrix (V × A) (V × A) ℂ) (i : V) (t s : ℕ) :
    Matrix V V ℂ :=
  ((U t).submatrix (fun a : A => (i, a)) (fun j : V => (j, a₀)))ᴴ
    * (U s).submatrix (fun a : A => (i, a)) (fun j : V => (j, a₀))

/-- **CONSTANT-RIGHT RELATEDNESS `≈_R`** (slot 3) — `∃ K ∈ U(V × A), ∀ t, U'_t = U_t K`. The
constant is **not** restricted to a gauge class: `CT1` is false with it restricted, since `GI2`'s
pair has identical relative objects with a constant relating element outside `𝒢ʷ_{a₀}`. The
relating element is forced, `K = U_0ᴴ U'_0` (`constRight_forced`). -/
def ConstRightRelated (U U' : ℕ → Matrix (V × A) (V × A) ℂ) : Prop :=
  ∃ K : Matrix (V × A) (V × A) ℂ, K ∈ Matrix.unitaryGroup (V × A) ℂ ∧ ∀ t, U' t = U t * K

/-- **CONSTANT-LEFT RELATEDNESS `≈_L`** (slot 4) — `∃ W ∈ U(V × A), ∀ t, U'_t = W U_t`. Likewise
unrestricted; forced, `W = U'_0 U_0ᴴ` (`constLeft_forced`). -/
def ConstLeftRelated (U U' : ℕ → Matrix (V × A) (V × A) ℂ) : Prop :=
  ∃ W : Matrix (V × A) (V × A) ℂ, W ∈ Matrix.unitaryGroup (V × A) ℂ ∧ ∀ t, U' t = W * U t

/-! ### Section B — the data: entries, the diagonal slice, the anchored block -/

omit [DecidableEq V] [DecidableEq A] in
theorem crossGram_apply (U : ℕ → Matrix (V × A) (V × A) ℂ) (t s : ℕ) (p q : V × A) :
    CrossGram U t s p q = ∑ r : V × A, star (U t r p) * U s r q := by
  simp [CrossGram, Matrix.mul_apply, Matrix.conjTranspose_apply]

/-- The `(t,t)` slice of the column cross-Gram is the identity, for every unitary lift. -/
theorem crossGram_self {U : ℕ → Matrix (V × A) (V × A) ℂ}
    (hU : ∀ t, U t ∈ Matrix.unitaryGroup (V × A) ℂ) (t : ℕ) : CrossGram U t t = 1 := by
  have h := Matrix.mem_unitaryGroup_iff'.1 (hU t)
  rwa [Matrix.star_eq_conjTranspose] at h

omit [Fintype V] [DecidableEq V] [DecidableEq A] in
theorem fibreCrossGram_apply (a₀ : A) (U : ℕ → Matrix (V × A) (V × A) ℂ) (i : V) (t s : ℕ)
    (j k : V) :
    FibreCrossGram a₀ U i t s j k = ∑ a : A, star (U t (i, a) (j, a₀)) * U s (i, a) (k, a₀) := by
  simp [FibreCrossGram, Matrix.mul_apply, Matrix.conjTranspose_apply, Matrix.submatrix_apply]

omit [Fintype V] [DecidableEq V] [DecidableEq A] in
/-- The same entry, as the Euclidean inner product of the two anchored fibre columns: the form the
Gram-isometry step consumes. -/
theorem fibreCrossGram_apply_dotProduct (a₀ : A) (U : ℕ → Matrix (V × A) (V × A) ℂ) (i : V)
    (t s : ℕ) (j k : V) :
    FibreCrossGram a₀ U i t s j k
      = (fun a : A => U s (i, a) (k, a₀)) ⬝ᵥ star (fun a : A => U t (i, a) (j, a₀)) := by
  rw [fibreCrossGram_apply]
  simp only [dotProduct, Pi.star_apply]
  exact Finset.sum_congr rfl fun a _ => mul_comm _ _

omit [Fintype V] [DecidableEq V] [DecidableEq A] in
/-- **LEVEL 0 IS THE DIAGONAL OF LEVEL 2, DEFINITIONALLY.** -/
theorem fibreCrossGram_diag (a₀ : A) (U : ℕ → Matrix (V × A) (V × A) ℂ) (i : V) (t : ℕ) :
    FibreCrossGram a₀ U i t t = FibreGram a₀ (U t) i := rfl

omit [DecidableEq V] [DecidableEq A] in
/-- **LEVEL 1 IS THE FIBRE SUM OF LEVEL 2 AND THE ANCHORED BLOCK OF LEVEL 3.** The anchored block
is a submatrix expression, not a definition. -/
theorem sum_fibreCrossGram (a₀ : A) (U : ℕ → Matrix (V × A) (V × A) ℂ) (t s : ℕ) :
    ∑ i, FibreCrossGram a₀ U i t s
      = (CrossGram U t s).submatrix (fun j : V => (j, a₀)) (fun k : V => (k, a₀)) := by
  ext j k
  rw [Matrix.sum_apply, Matrix.submatrix_apply, crossGram_apply, Fintype.sum_prod_type]
  exact Finset.sum_congr rfl fun i _ => by rw [fibreCrossGram_apply]

/-! ### Section C — the transformation laws -/

omit [DecidableEq V] [DecidableEq A] in
/-- **THE TWO-SIDED TRANSFORMATION LAW**: under `U_t ↦ L_t U_t K_t`,
`Ξ^{(t,s)} ↦ K_tᴴ (U_tᴴ L_tᴴ L_s U_s) K_s`. A time-dependent left factor survives as `L_tᴴ L_s`. -/
theorem crossGram_two_sided (L U K : ℕ → Matrix (V × A) (V × A) ℂ) (t s : ℕ) :
    CrossGram (fun t => L t * U t * K t) t s
      = (K t)ᴴ * ((U t)ᴴ * ((L t)ᴴ * L s) * U s) * K s := by
  simp only [CrossGram, Matrix.conjTranspose_mul, Matrix.mul_assoc]

/-- **THE FIRST TRANSFORMATION LAW**: `Ξ` is invariant under a constant left unitary,
`(W U_t)ᴴ (W U_s) = U_tᴴ U_s`. This is the reason the frozen family is bounded from above. -/
theorem crossGram_left_mul {W : Matrix (V × A) (V × A) ℂ} (hW : W ∈ Matrix.unitaryGroup (V × A) ℂ)
    (U : ℕ → Matrix (V × A) (V × A) ℂ) (t s : ℕ) :
    CrossGram (fun t => W * U t) t s = CrossGram U t s := by
  have h : Wᴴ * W = 1 := by
    have hh := Matrix.mem_unitaryGroup_iff'.1 hW
    rwa [Matrix.star_eq_conjTranspose] at hh
  simp only [CrossGram, Matrix.conjTranspose_mul, Matrix.mul_assoc]
  rw [← Matrix.mul_assoc Wᴴ, h, Matrix.one_mul]

omit [DecidableEq V] [DecidableEq A] in
/-- Under a right family, `Ξ ↦ K_tᴴ Ξ K_s`. -/
theorem crossGram_mul_right (U K : ℕ → Matrix (V × A) (V × A) ℂ) (t s : ℕ) :
    CrossGram (fun t => U t * K t) t s = (K t)ᴴ * CrossGram U t s * K s := by
  simp only [CrossGram, Matrix.conjTranspose_mul, Matrix.mul_assoc]

/-- The anchored column of `U * K` for strong `K` is the anchored column of `U`: the coefficient
`c ≡ 1` case of act 12's `mul_weak_anchor_col`. -/
theorem mul_strong_anchor_col {a₀ : A} {K : Matrix (V × A) (V × A) ℂ}
    (hK : StrongAnchorStabilizer a₀ K) (U : Matrix (V × A) (V × A) ℂ) (p : V × A) (j : V) :
    (U * K) p (j, a₀) = U p (j, a₀) := by
  rw [mul_weak_anchor_col (c := fun _ => 1) hK.2]
  simp

/-- The anchored fibre block of `U * K` for strong `K` is the anchored fibre block of `U`. -/
theorem mul_strong_submatrix {a₀ : A} {K : Matrix (V × A) (V × A) ℂ}
    (hK : StrongAnchorStabilizer a₀ K) (U : Matrix (V × A) (V × A) ℂ) (i : V) :
    (U * K).submatrix (fun a : A => (i, a)) (fun j : V => (j, a₀))
      = U.submatrix (fun a : A => (i, a)) (fun j : V => (j, a₀)) := by
  ext a j
  simp only [Matrix.submatrix_apply]
  exact mul_strong_anchor_col hK U _ j

/-- **THE WEAK TRANSFORMATION LAW, CROSS-TIME** — the cross-time form of act 12's
`fibreGram_mul_weak_apply`: a weak right family with anchored phases `c^t_j` carries
`(Ξ_i^{(t,s)})_{jk}` to `conj(c^t_j) (Ξ_i^{(t,s)})_{jk} c^s_k`. **So raw level-0 equality is not
invariant under the weak-right action**, and does not itself compute act 12's per-slice quotient:
that is computed by the phase-equivalence class of the level-0 datum (`TG2`). -/
theorem fibreCrossGram_mul_weak_apply {a₀ : A} {K : ℕ → Matrix (V × A) (V × A) ℂ} {c : ℕ → V → ℂ}
    (hc : ∀ t p j, K t p (j, a₀) = if p = (j, a₀) then c t j else 0)
    (U : ℕ → Matrix (V × A) (V × A) ℂ) (i : V) (t s : ℕ) (j k : V) :
    FibreCrossGram a₀ (fun t => U t * K t) i t s j k
      = star (c t j) * FibreCrossGram a₀ U i t s j k * c s k := by
  rw [fibreCrossGram_apply, fibreCrossGram_apply, Finset.mul_sum, Finset.sum_mul]
  refine Finset.sum_congr rfl fun a _ => ?_
  rw [mul_weak_anchor_col (hc t), mul_weak_anchor_col (hc s), star_mul']
  ring

/-! ### Section D — `CT3` (G): universal blindness of levels 0–2 to strong-right threading -/

/-- **`CT3` (G) — THE SECOND TRANSFORMATION LAW AS A THEOREM.** For every lift, every strong-right
family and every `i, t, s`, `Ξ_i^{(t,s)}(U·K) = Ξ_i^{(t,s)}(U)`. No function of the anchored-column
data at any resolution separates any strong-right-related pair, so **the least separating
column-Gram datum for `GL2`-type pairs lies outside the anchored block.** -/
theorem ct3g_fibreCrossGram_strong_right {a₀ : A} (U K : ℕ → Matrix (V × A) (V × A) ℂ)
    (hK : ∀ t, StrongAnchorStabilizer a₀ (K t)) (i : V) (t s : ℕ) :
    FibreCrossGram a₀ (fun t => U t * K t) i t s = FibreCrossGram a₀ U i t s := by
  show ((U t * K t).submatrix (fun a : A => (i, a)) (fun j : V => (j, a₀)))ᴴ
      * (U s * K s).submatrix (fun a : A => (i, a)) (fun j : V => (j, a₀)) = _
  rw [mul_strong_submatrix (hK t), mul_strong_submatrix (hK s)]
  rfl

/-- **`CT3` (G) AT LEVEL 0** — the per-time fibre-Gram trajectory is strong-right invariant. -/
theorem ct3g_fibreGram_strong_right {a₀ : A} (U K : ℕ → Matrix (V × A) (V × A) ℂ)
    (hK : ∀ t, StrongAnchorStabilizer a₀ (K t)) (i : V) (t : ℕ) :
    FibreGram a₀ (U t * K t) i = FibreGram a₀ (U t) i :=
  ct3g_fibreCrossGram_strong_right U K hK i t t

/-- **`CT3` (G) AT LEVEL 1** — the anchored block of `Ξ` is strong-right invariant. -/
theorem ct3g_anchored_block_strong_right {a₀ : A} (U K : ℕ → Matrix (V × A) (V × A) ℂ)
    (hK : ∀ t, StrongAnchorStabilizer a₀ (K t)) (t s : ℕ) :
    (CrossGram (fun t => U t * K t) t s).submatrix (fun j : V => (j, a₀)) (fun k : V => (k, a₀))
      = (CrossGram U t s).submatrix (fun j : V => (j, a₀)) (fun k : V => (k, a₀)) := by
  rw [← sum_fibreCrossGram, ← sum_fibreCrossGram]
  exact Finset.sum_congr rfl fun i _ => ct3g_fibreCrossGram_strong_right U K hK i t s

/-! ### Section E — `CT1`: the exact quotient of the relative evolution -/

/-- The constant-right relating element is forced: `K = U_0ᴴ U'_0`. Membership is a computation. -/
theorem constRight_forced {U U' : ℕ → Matrix (V × A) (V × A) ℂ}
    (hU : ∀ t, U t ∈ Matrix.unitaryGroup (V × A) ℂ) {K : Matrix (V × A) (V × A) ℂ}
    (hfac : ∀ t, U' t = U t * K) : K = (U 0)ᴴ * U' 0 := by
  have h1 : (U 0)ᴴ * U 0 = 1 := by
    have h := Matrix.mem_unitaryGroup_iff'.1 (hU 0)
    rwa [Matrix.star_eq_conjTranspose] at h
  rw [hfac 0, ← Matrix.mul_assoc, h1, Matrix.one_mul]

/-- The constant-left relating element is forced: `W = U'_0 U_0ᴴ`. -/
theorem constLeft_forced {U U' : ℕ → Matrix (V × A) (V × A) ℂ}
    (hU : ∀ t, U t ∈ Matrix.unitaryGroup (V × A) ℂ) {W : Matrix (V × A) (V × A) ℂ}
    (hfac : ∀ t, U' t = W * U t) : W = U' 0 * (U 0)ᴴ := by
  have h1 : U 0 * (U 0)ᴴ = 1 := by
    have h := Matrix.mem_unitaryGroup_iff.1 (hU 0)
    rwa [Matrix.star_eq_conjTranspose] at h
  rw [hfac 0, Matrix.mul_assoc, h1, Matrix.mul_one]

/-- **`CT1`, FORWARD** — equal relative objects at every `t, s` force `U'_t = U_t K` with the one
constant unitary `K = U_0ᴴ U'_0`: `U'_t = U'_t U'_0ᴴ U'_0 = U_t U_0ᴴ U'_0`. This round's. -/
theorem ct1_forward {U U' : ℕ → Matrix (V × A) (V × A) ℂ}
    (hU : ∀ t, U t ∈ Matrix.unitaryGroup (V × A) ℂ)
    (hU' : ∀ t, U' t ∈ Matrix.unitaryGroup (V × A) ℂ)
    (h : ∀ t s, U' t * (U' s)ᴴ = U t * (U s)ᴴ) :
    (U 0)ᴴ * U' 0 ∈ Matrix.unitaryGroup (V × A) ℂ ∧ ∀ t, U' t = U t * ((U 0)ᴴ * U' 0) := by
  refine ⟨conjTranspose_mul_mem_unitaryGroup (hU 0) (hU' 0), fun t => ?_⟩
  have h1 : (U' 0)ᴴ * U' 0 = 1 := by
    have hh := Matrix.mem_unitaryGroup_iff'.1 (hU' 0)
    rwa [Matrix.star_eq_conjTranspose] at hh
  calc U' t = U' t * ((U' 0)ᴴ * U' 0) := by rw [h1, Matrix.mul_one]
    _ = (U' t * (U' 0)ᴴ) * U' 0 := by rw [Matrix.mul_assoc]
    _ = (U t * (U 0)ᴴ) * U' 0 := by rw [h t 0]
    _ = U t * ((U 0)ᴴ * U' 0) := by rw [Matrix.mul_assoc]

/-- **`CT1`, BACKWARD** — consumed from act 11's `GL3`: a constant right unitary leaves every
relative object unchanged. Named separately, as §A.34 requires. -/
theorem ct1_backward {K : Matrix (V × A) (V × A) ℂ} (hK : K ∈ Matrix.unitaryGroup (V × A) ℂ)
    (U : ℕ → Matrix (V × A) (V × A) ℂ) (t s : ℕ) :
    (U t * K) * ((U s * K))ᴴ = U t * (U s)ᴴ :=
  gl3_constant_gauge_preserves_relative hK U t s

/-- **`CT1` — THE EXACT QUOTIENT OF THE RELATIVE EVOLUTION.** For unitary lifts,
`(∀ t s, U'_t U'_sᴴ = U_t U_sᴴ) ⟺ U' ≈_R U`. **Bounded reading:** the relative evolution is the lift
modulo constant right unitaries, and the threading question of `P0` is exactly the question of what
pins a lift modulo constant right unitaries. `CT1` does not say what pins it. -/
theorem ct1_relative_iff_constRight {U U' : ℕ → Matrix (V × A) (V × A) ℂ}
    (hU : ∀ t, U t ∈ Matrix.unitaryGroup (V × A) ℂ)
    (hU' : ∀ t, U' t ∈ Matrix.unitaryGroup (V × A) ℂ) :
    (∀ t s, U' t * (U' s)ᴴ = U t * (U s)ᴴ) ↔ ConstRightRelated U U' := by
  constructor
  · intro h
    exact ⟨_, (ct1_forward hU hU' h).1, (ct1_forward hU hU' h).2⟩
  · rintro ⟨K, hK, hfac⟩ t s
    rw [hfac t, hfac s]
    exact ct1_backward hK U t s

/-! ### Section F — `CT2` (a): level 3 determines the lift up to a constant left unitary -/

/-- **`CT2` (a), FORWARD** — equal column cross-Grams at every `t, s` force `U'_t = W U_t` with the
one constant unitary `W = U'_0 U_0ᴴ`: from `U'_tᴴ U'_0 = U_tᴴ U_0`, conjugate-transpose and multiply
on the left by `U'_0`. -/
theorem ct2a_forward {U U' : ℕ → Matrix (V × A) (V × A) ℂ}
    (hU : ∀ t, U t ∈ Matrix.unitaryGroup (V × A) ℂ)
    (hU' : ∀ t, U' t ∈ Matrix.unitaryGroup (V × A) ℂ)
    (h : ∀ t s, CrossGram U' t s = CrossGram U t s) :
    U' 0 * (U 0)ᴴ ∈ Matrix.unitaryGroup (V × A) ℂ ∧ ∀ t, U' t = (U' 0 * (U 0)ᴴ) * U t := by
  refine ⟨?_, fun t => ?_⟩
  · have hs := conjTranspose_mul_mem_unitaryGroup (hU 0) (one_mem _)
    rw [Matrix.mul_one] at hs
    exact mul_mem (hU' 0) hs
  · have h0 : (U' 0)ᴴ * U' t = (U 0)ᴴ * U t := by
      have := congrArg Matrix.conjTranspose (h t 0)
      simpa only [CrossGram, Matrix.conjTranspose_mul, Matrix.conjTranspose_conjTranspose]
        using this
    have h2 : U' 0 * (U' 0)ᴴ = 1 := by
      have hh := Matrix.mem_unitaryGroup_iff.1 (hU' 0)
      rwa [Matrix.star_eq_conjTranspose] at hh
    calc U' t = (U' 0 * (U' 0)ᴴ) * U' t := by rw [h2, Matrix.one_mul]
      _ = U' 0 * ((U' 0)ᴴ * U' t) := by rw [Matrix.mul_assoc]
      _ = U' 0 * ((U 0)ᴴ * U t) := by rw [h0]
      _ = (U' 0 * (U 0)ᴴ) * U t := by rw [Matrix.mul_assoc]

/-- **`CT2` (a), BACKWARD** — the first transformation law. -/
theorem ct2a_backward {W : Matrix (V × A) (V × A) ℂ} (hW : W ∈ Matrix.unitaryGroup (V × A) ℂ)
    (U : ℕ → Matrix (V × A) (V × A) ℂ) (t s : ℕ) :
    CrossGram (fun t => W * U t) t s = CrossGram U t s :=
  crossGram_left_mul hW U t s

/-- **`CT2` (a) — LEVEL 3 DETERMINES THE LIFT UP TO ONE CONSTANT LEFT UNITARY.** For unitary lifts,
`(∀ t s, Ξ^{(t,s)}(U') = Ξ^{(t,s)}(U)) ⟺ U' ≈_L U`, both directions. -/
theorem ct2a_crossGram_iff_constLeft {U U' : ℕ → Matrix (V × A) (V × A) ℂ}
    (hU : ∀ t, U t ∈ Matrix.unitaryGroup (V × A) ℂ)
    (hU' : ∀ t, U' t ∈ Matrix.unitaryGroup (V × A) ℂ) :
    (∀ t s, CrossGram U' t s = CrossGram U t s) ↔ ConstLeftRelated U U' := by
  constructor
  · intro h
    exact ⟨_, (ct2a_forward hU hU' h).1, (ct2a_forward hU hU' h).2⟩
  · rintro ⟨W, hW, hfac⟩ t s
    have hU'eq : U' = fun t => W * U t := funext hfac
    rw [hU'eq]
    exact ct2a_backward hW U t s

omit [DecidableEq V] [DecidableEq A] in
/-- **THE CONSEQUENCE OF `CT2` (a), STATED EXACTLY**: a constant left move conjugates every relative
object, `U'_t U'_sᴴ = W (U_t U_sᴴ) Wᴴ`. So the column cross-Gram determines the relative evolution
up to **conjugation by one constant unitary** — a quotient finer than act 12's two-sided one, and
**not** the identity on relative candidates: `CT4` is the certificate, and "determines the lift up
to `≈_L`" is the only claim made. -/
theorem ct2a_relative_conj {U U' : ℕ → Matrix (V × A) (V × A) ℂ}
    {W : Matrix (V × A) (V × A) ℂ} (hfac : ∀ t, U' t = W * U t) (t s : ℕ) :
    U' t * (U' s)ᴴ = W * (U t * (U s)ᴴ) * Wᴴ := by
  rw [hfac t, hfac s, Matrix.conjTranspose_mul]
  simp only [Matrix.mul_assoc]

/-! ### Section G — `CT2` (b), backward: the second transformation law -/

/-- **`CT2` (b), BACKWARD** — a constant in-fibre left move followed by a time-dependent strong
right gauge leaves every fibre cross-Gram datum unchanged: the anchored fibre columns of
`W U_t K_t` are `W_i` times those of `U_t`, and `W_iᴴ W_i = 1`. -/
theorem ct2b_backward {a₀ : A} {U U' : ℕ → Matrix (V × A) (V × A) ℂ}
    (h : ∃ W : Matrix (V × A) (V × A) ℂ, LeftFibreGroup W
      ∧ GaugeRelated (StrongAnchorStabilizer a₀) (fun t => W * U t) U') (i : V) (t s : ℕ) :
    FibreCrossGram a₀ U' i t s = FibreCrossGram a₀ U i t s := by
  obtain ⟨W, hW, K, hK, hfac⟩ := h
  have hfac' : ∀ t, U' t = W * U t * K t := hfac
  have hsub : ∀ t, (U' t).submatrix (fun a : A => (i, a)) (fun j : V => (j, a₀))
      = W.submatrix (fun a : A => (i, a)) (fun a : A => (i, a))
          * (U t).submatrix (fun a : A => (i, a)) (fun j : V => (j, a₀)) := by
    intro t
    rw [hfac' t, mul_strong_submatrix (hK t), left_mul_submatrix hW]
  unfold FibreCrossGram
  rw [hsub t, hsub s, Matrix.conjTranspose_mul, Matrix.mul_assoc,
    ← Matrix.mul_assoc (W.submatrix (fun a : A => (i, a)) (fun a : A => (i, a)))ᴴ,
    left_block_unitary hW, Matrix.one_mul]

/-! ### Section H — the infinite-family Gram-isometry lemma and `CT2` (b), forward -/

/-- **THE GRAM-ISOMETRY LEMMA FOR AN ARBITRARY INDEX TYPE** — the round's load-bearing technical
step, act 12's `exists_unitary_of_gram_eq` freed from its finite index set. Two families of
vectors in `ℂ^A`, indexed by any type `ι` — here `ℕ × V`, infinite — with the same inner products
are related by one unitary `M` on `ℂ^A`.

The map `∑ cₚ xₚ ↦ ∑ cₚ yₚ` is well defined on `span {xₚ}` and isometric there, because every inner
product of finite linear combinations is a finite sum of the agreeing pairwise inner products; the
span is a subspace of the finite-dimensional `ℂ^A`, and Mathlib's `LinearIsometry.extend` extends
the isometry to all of `ℂ^A`. `M` is that extension's matrix. **Nothing here assumes the family is
finite, spanning or independent.** -/
theorem exists_unitary_of_inner_eq {ι : Type} (x y : ι → EuclideanSpace ℂ A)
    (h : ∀ p q, inner ℂ (x p) (x q) = inner ℂ (y p) (y q)) :
    ∃ M : Matrix A A ℂ, M ∈ Matrix.unitaryGroup A ℂ
      ∧ ∀ p, M *ᵥ WithLp.ofLp (x p) = WithLp.ofLp (y p) := by
  classical
  set T : (ι →₀ ℂ) →ₗ[ℂ] EuclideanSpace ℂ A := Finsupp.linearCombination ℂ x with hT
  set T' : (ι →₀ ℂ) →ₗ[ℂ] EuclideanSpace ℂ A := Finsupp.linearCombination ℂ y with hT'
  have hTapp : ∀ v : ι →₀ ℂ, T v = ∑ p ∈ v.support, v p • x p := fun v => by
    rw [hT, Finsupp.linearCombination_apply, Finsupp.sum]
  have hT'app : ∀ v : ι →₀ ℂ, T' v = ∑ p ∈ v.support, v p • y p := fun v => by
    rw [hT', Finsupp.linearCombination_apply, Finsupp.sum]
  have hinner : ∀ v w, inner ℂ (T v) (T w) = inner ℂ (T' v) (T' w) := by
    intro v w
    rw [hTapp, hTapp, hT'app, hT'app, sum_inner, sum_inner]
    refine Finset.sum_congr rfl fun p _ => ?_
    rw [inner_sum, inner_sum]
    refine Finset.sum_congr rfl fun q _ => ?_
    rw [inner_smul_left, inner_smul_left, inner_smul_right, inner_smul_right, h]
  have hnorm : ∀ v, ‖T v‖ = ‖T' v‖ := fun v => by
    rw [norm_eq_sqrt_re_inner (𝕜 := ℂ), norm_eq_sqrt_re_inner (𝕜 := ℂ), hinner]
  have hker : LinearMap.ker T ≤ LinearMap.ker T' := by
    intro v hv
    rw [LinearMap.mem_ker] at hv ⊢
    rw [← norm_eq_zero, ← hnorm, norm_eq_zero]
    exact hv
  -- the isometry `∑ cₚ xₚ ↦ ∑ cₚ yₚ` on the span of the family
  let g₀ : LinearMap.range T →ₗ[ℂ] EuclideanSpace ℂ A :=
    ((LinearMap.ker T).liftQ T' hker).comp T.quotKerEquivRange.symm.toLinearMap
  have hg₀ : ∀ v, g₀ ⟨T v, LinearMap.mem_range_self T v⟩ = T' v := by
    intro v
    show ((LinearMap.ker T).liftQ T' hker) (T.quotKerEquivRange.symm ⟨T v, _⟩) = T' v
    rw [LinearMap.quotKerEquivRange_symm_apply_image, Submodule.mkQ_apply, Submodule.liftQ_apply]
  have hgnorm : ∀ s : LinearMap.range T, ‖g₀ s‖ = ‖s‖ := by
    rintro ⟨s, hs⟩
    obtain ⟨v, rfl⟩ := LinearMap.mem_range.1 hs
    show ‖g₀ ⟨T v, LinearMap.mem_range_self T v⟩‖ = ‖T v‖
    rw [hg₀, hnorm]
  let g : LinearMap.range T →ₗᵢ[ℂ] EuclideanSpace ℂ A := ⟨g₀, hgnorm⟩
  -- its extension to all of `ℂ^A`, and the extension's matrix
  let b := EuclideanSpace.basisFun A ℂ
  let M : Matrix A A ℂ := LinearMap.toMatrix b.toBasis b.toBasis g.extend.toLinearMap
  have hrepr : ∀ z : EuclideanSpace ℂ A, (⇑(b.toBasis.repr z) : A → ℂ) = WithLp.ofLp z := by
    intro z
    funext a
    simp [b, OrthonormalBasis.coe_toBasis_repr_apply, EuclideanSpace.basisFun_repr]
  have hM : ∀ z : EuclideanSpace ℂ A, M *ᵥ WithLp.ofLp z = WithLp.ofLp (g.extend z) := by
    intro z
    have := LinearMap.toMatrix_mulVec_repr b.toBasis b.toBasis g.extend.toLinearMap z
    rwa [hrepr, hrepr] at this
  have hMapply : ∀ c a, M c a = WithLp.ofLp (g.extend (EuclideanSpace.single a (1 : ℂ))) c := by
    intro c a
    simp [M, LinearMap.toMatrix_apply, b, OrthonormalBasis.coe_toBasis_repr_apply,
      EuclideanSpace.basisFun_repr, OrthonormalBasis.coe_toBasis, EuclideanSpace.basisFun_apply]
  have hMunit : M ∈ Matrix.unitaryGroup A ℂ := by
    rw [Matrix.mem_unitaryGroup_iff', Matrix.star_eq_conjTranspose]
    ext a c
    rw [Matrix.mul_apply, Matrix.one_apply]
    simp only [Matrix.conjTranspose_apply, hMapply]
    have hsum : ∀ z w : EuclideanSpace ℂ A,
        inner ℂ z w = ∑ i, star (WithLp.ofLp z i) * WithLp.ofLp w i := by
      intro z w
      rw [PiLp.inner_apply]
      exact Finset.sum_congr rfl fun i _ => by rw [RCLike.inner_apply, RCLike.star_def, mul_comm]
    have := g.extend.inner_map_map (EuclideanSpace.single a (1 : ℂ)) (EuclideanSpace.single c 1)
    rw [EuclideanSpace.inner_single_left, hsum] at this
    simp only [map_one, one_mul, PiLp.single_apply] at this
    exact this
  refine ⟨M, hMunit, fun p => ?_⟩
  have hx : x p = T (Finsupp.single p 1) := by
    rw [hT, Finsupp.linearCombination_single, one_smul]
  have hy : y p = T' (Finsupp.single p 1) := by
    rw [hT', Finsupp.linearCombination_single, one_smul]
  have h2 : g.extend (x p) = y p := by
    rw [hx, hy, ← hg₀ (Finsupp.single p 1)]
    exact LinearIsometry.extend_apply g ⟨T _, LinearMap.mem_range_self T _⟩
  rw [hM, h2]

/-- **`CT2` (b), FORWARD** — equal fibre cross-Gram data at every `i, t, s` force a constant
`W ∈ 𝒢_L` and a time-dependent strong right gauge with `U'_t = W U_t K_t`. For each fibre `i` the
two `ℕ × V`-indexed families `{P_i U_t e_{(j,a₀)}}` and `{P_i U'_t e_{(j,a₀)}}` in `ℂ^A` have the
same inner products, so `exists_unitary_of_inner_eq` supplies one unitary `W_i` on the fibre; the
`W_i` assemble into `W ∈ 𝒢_L` with `U'_t e_{(j,a₀)} = W U_t e_{(j,a₀)}` for every `t` and `j`, and
act 11's `gaugeRelated_strong_iff_agree_on_anchor` absorbs the off-anchor freedom into a
time-dependent strong element. **Reached at kernel level**: the frozen fallback is not used. -/
theorem ct2b_forward {a₀ : A} {U U' : ℕ → Matrix (V × A) (V × A) ℂ}
    (hU : ∀ t, U t ∈ Matrix.unitaryGroup (V × A) ℂ)
    (hU' : ∀ t, U' t ∈ Matrix.unitaryGroup (V × A) ℂ)
    (h : ∀ i t s, FibreCrossGram a₀ U' i t s = FibreCrossGram a₀ U i t s) :
    ∃ W : Matrix (V × A) (V × A) ℂ, LeftFibreGroup W
      ∧ GaugeRelated (StrongAnchorStabilizer a₀) (fun t => W * U t) U' := by
  classical
  -- one fibre unitary per fibre, from the infinite-family Gram-isometry lemma
  have hblock : ∀ i : V, ∃ M : Matrix A A ℂ, M ∈ Matrix.unitaryGroup A ℂ
      ∧ ∀ t j, M *ᵥ (fun a => U t (i, a) (j, a₀)) = fun a => U' t (i, a) (j, a₀) := by
    intro i
    obtain ⟨M, hM, hMx⟩ := exists_unitary_of_inner_eq
      (fun p : ℕ × V => WithLp.toLp 2 (fun a => U p.1 (i, a) (p.2, a₀)))
      (fun p : ℕ × V => WithLp.toLp 2 (fun a => U' p.1 (i, a) (p.2, a₀))) (by
        rintro ⟨t, j⟩ ⟨s, k⟩
        rw [EuclideanSpace.inner_toLp_toLp, EuclideanSpace.inner_toLp_toLp,
          ← fibreCrossGram_apply_dotProduct, ← fibreCrossGram_apply_dotProduct, h])
    exact ⟨M, hM, fun t j => by simpa using hMx (t, j)⟩
  choose M hMunit hMX using hblock
  -- the fibre unitaries assembled into a fibre-block unitary
  set W : Matrix (V × A) (V × A) ℂ :=
    Matrix.of fun p q => if p.1 = q.1 then M p.1 p.2 q.2 else 0 with hWdef
  have hWblock : ∀ i, W.submatrix (fun a : A => (i, a)) (fun a : A => (i, a)) = M i := by
    intro i
    ext a b
    simp [hWdef]
  have hWzero : ∀ p q : V × A, p.1 ≠ q.1 → W p q = 0 := by
    intro p q hpq
    simp [hWdef, hpq]
  have hW : LeftFibreGroup W := by
    refine ⟨?_, hWzero⟩
    rw [Matrix.mem_unitaryGroup_iff', Matrix.star_eq_conjTranspose]
    ext p q
    rw [Matrix.mul_apply, Fintype.sum_prod_type]
    obtain ⟨i, a⟩ := p
    obtain ⟨k, b⟩ := q
    by_cases hik : i = k
    · subst hik
      rw [Finset.sum_eq_single i (fun i' _ hi' => Finset.sum_eq_zero fun c' _ => by
          rw [Matrix.conjTranspose_apply, hWzero (i', c') (i, a) hi', star_zero, zero_mul])
        (fun hcon => absurd (Finset.mem_univ _) hcon)]
      have hMi : (M i)ᴴ * M i = 1 := by
        have hh := Matrix.mem_unitaryGroup_iff'.1 (hMunit i)
        rwa [Matrix.star_eq_conjTranspose] at hh
      have := congrFun (congrFun hMi a) b
      rw [Matrix.mul_apply] at this
      simp only [Matrix.conjTranspose_apply] at this ⊢
      simp only [hWdef, Matrix.of_apply, if_true]
      rw [this, Matrix.one_apply, Matrix.one_apply]
      simp [Prod.ext_iff]
    · rw [Matrix.one_apply_ne (fun hcon => hik (Prod.ext_iff.1 hcon).1)]
      refine Finset.sum_eq_zero fun i' _ => Finset.sum_eq_zero fun c' _ => ?_
      by_cases hi' : i' = i
      · rw [hWzero (i', c') (k, b) (by rw [hi']; exact hik), mul_zero]
      · rw [Matrix.conjTranspose_apply, hWzero (i', c') (i, a) hi', star_zero, zero_mul]
  -- `W U_t` agrees with `U'_t` on every anchored column, at every time
  have hagree : ∀ t (p : V × A) (j : V), (W * U t) p (j, a₀) = U' t p (j, a₀) := by
    intro t p j
    obtain ⟨i, a⟩ := p
    have hsub := congrFun (congrFun (left_mul_submatrix hW (U t) a₀ i) a) j
    rw [hWblock] at hsub
    simp only [Matrix.submatrix_apply] at hsub
    rw [hsub, Matrix.mul_apply]
    have hcol := congrFun (hMX i t j) a
    simp only [Matrix.mulVec, dotProduct] at hcol
    simpa only [Matrix.submatrix_apply] using hcol
  have hWU : ∀ t, W * U t ∈ Matrix.unitaryGroup (V × A) ℂ := fun t => mul_mem hW.1 (hU t)
  exact ⟨W, hW, (gaugeRelated_strong_iff_agree_on_anchor (a₀ := a₀) (U := fun t => W * U t)
    (U' := U') hWU hU').2 (fun t p j => (hagree t p j).symm)⟩

/-- **`CT2` (b) — LEVEL 2 DETERMINES THE LIFT UP TO A CONSTANT IN-FIBRE LEFT MOVE AND A
TIME-DEPENDENT STRONG RIGHT GAUGE**, both directions. **Consequence, stated exactly:** the residual
of the fibre cross-Gram trajectory is exactly `GL2`'s mechanism together with one constant `𝒢_L`
conjugation, and nothing else. With `CT1`: relative to the level-2 data, the threading freedom of
`P0` is exactly a strong-right family `K_t` modulo a constant, together with one constant in-fibre
frame. Nothing here selects either. -/
theorem ct2b_fibreCrossGram_iff {a₀ : A} {U U' : ℕ → Matrix (V × A) (V × A) ℂ}
    (hU : ∀ t, U t ∈ Matrix.unitaryGroup (V × A) ℂ)
    (hU' : ∀ t, U' t ∈ Matrix.unitaryGroup (V × A) ℂ) :
    (∀ i t s, FibreCrossGram a₀ U' i t s = FibreCrossGram a₀ U i t s)
      ↔ ∃ W : Matrix (V × A) (V × A) ℂ, LeftFibreGroup W
          ∧ GaugeRelated (StrongAnchorStabilizer a₀) (fun t => W * U t) U' :=
  ⟨ct2b_forward hU hU', fun h i t s => ct2b_backward h i t s⟩

/-! ### Section I — the anchored rows of a strong element, for `CT3` (c) -/

/-- A strong element has anchored **rows** equal to the standard basis vectors too: the anchored
entries by definition, the off-anchor entries by act 11's `strong_column_offAnchor_eq_zero`. -/
theorem strong_anchored_row {a₀ : A} {K : Matrix (V × A) (V × A) ℂ}
    (hK : StrongAnchorStabilizer a₀ K) (j : V) (p : V × A) :
    K (j, a₀) p = if p = (j, a₀) then 1 else 0 := by
  obtain ⟨k, b⟩ := p
  by_cases hb : b = a₀
  · rw [hb, hK.2 (j, a₀) k]
    exact if_congr eq_comm rfl rfl
  · rw [if_neg (fun hcon => hb (Prod.ext_iff.1 hcon).2),
      strong_column_offAnchor_eq_zero hK j (k, b) hb]

/-- **THE ANCHORED COLUMNS OF `K₁ᴴ K₂` FOR STRONG `K₁, K₂` ARE THE STANDARD BASIS VECTORS.** This
is why the constant-lift variant's cross-Grams agree on every anchored column. -/
theorem strong_pair_anchored_col {a₀ : A} {K₁ K₂ : Matrix (V × A) (V × A) ℂ}
    (h₁ : StrongAnchorStabilizer a₀ K₁) (h₂ : StrongAnchorStabilizer a₀ K₂) (p : V × A) (j : V) :
    (K₁ᴴ * K₂) p (j, a₀) = if p = (j, a₀) then 1 else 0 := by
  rw [Matrix.mul_apply, Finset.sum_eq_single (j, a₀)
    (fun q _ hq => by rw [h₂.2 q j, if_neg hq, mul_zero])
    (fun hcon => absurd (Finset.mem_univ _) hcon), h₂.2 (j, a₀) j, if_pos rfl, mul_one,
    Matrix.conjTranspose_apply, strong_anchored_row h₁ j p]
  split_ifs <;> simp

/-! ### Section J — `CT3` (a): `GL2`'s pair, separated by level 3 at an off-anchor row -/

/-- **`CT3` (a) — `GL2`'s PAIR IS SEPARATED BY LEVEL 3, AT AN OFF-ANCHOR ROW.** Act 11's `GL2` pair
on `V = Fin 2`, `A = Fin 2`, `a₀ = 0` — `U_0 = U_B`, `U_1 = 𝟙`, `U'_0 = U_B P(ρ)`, `U'_1 = 𝟙` with
`ρ = swap((0,1),(1,1))` — re-exhibited with its matrices pinned by equations: two coherent lifts of
one family, related by a time-dependent element of the **strong** class, sharing **every** fibre
cross-Gram datum (`CT3` (G)), hence every per-time Gram matrix and every level-1 datum, and
separated by the single entry `((0,1),(1,1))` of `Ξ^{(0,1)}`: `0` for `U`, `1` for `U'`. The row
`(0,1)` is off-anchor. The relative candidates differ at `(0,1)`: `1/2` against `0`.

**The permutation convention is act 7's**, and the entry is computed, not read off. -/
theorem ct3a_gl2_pair_separated_by_crossGram :
    ∃ (Γ : ℕ → Matrix (Fin 2) (Fin 2) ℝ)
      (U U' K : ℕ → Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ),
      U 0 = Matrix.of (fun p q : Fin 2 × Fin 2 =>
          if p = (0, 0) then (if q = (0, 0) then 1 else 0)
          else if p = (0, 1) then
            (if q = (0, 1) then ((Real.sqrt (1 / 2) : ℝ) : ℂ)
              else if q = (1, 0) then ((Real.sqrt (1 / 2) : ℝ) : ℂ) else 0)
          else if p = (1, 0) then
            (if q = (0, 1) then -((Real.sqrt (1 / 2) : ℝ) : ℂ)
              else if q = (1, 0) then ((Real.sqrt (1 / 2) : ℝ) : ℂ) else 0)
          else (if q = (1, 1) then 1 else 0))
        ∧ (∀ t, t ≠ 0 → U t = 1)
        ∧ U' 0 = U 0 * (Equiv.swap ((0 : Fin 2), (1 : Fin 2)) ((1 : Fin 2), (1 : Fin 2))
            : Equiv.Perm (Fin 2 × Fin 2)).permMatrix ℂ
        ∧ (∀ t, t ≠ 0 → U' t = 1)
        ∧ CoherentLift (0 : Fin 2) Γ U ∧ CoherentLift (0 : Fin 2) Γ U'
        ∧ (∀ t, StrongAnchorStabilizer (0 : Fin 2) (K t))
        ∧ (∀ t, U' t = U t * K t)
        ∧ (∃ t s : ℕ, K t ≠ K s)
        ∧ (∀ i t s, FibreCrossGram (0 : Fin 2) U' i t s = FibreCrossGram (0 : Fin 2) U i t s)
        ∧ CrossGram U 0 1 ((0 : Fin 2), (1 : Fin 2)) ((1 : Fin 2), (1 : Fin 2)) = 0
        ∧ CrossGram U' 0 1 ((0 : Fin 2), (1 : Fin 2)) ((1 : Fin 2), (1 : Fin 2)) = 1
        ∧ readback (0 : Fin 2) (Matrix.of fun p q => ‖(U 1 * (U 0)ᴴ) p q‖ ^ 2) 0 1 = 1 / 2
        ∧ readback (0 : Fin 2) (Matrix.of fun p q => ‖(U' 1 * (U' 0)ᴴ) p q‖ ^ 2) 0 1 = 0 := by
  classical
  obtain ⟨s, hsdef⟩ : ∃ s : ℝ, s = Real.sqrt (1 / 2) := ⟨_, rfl⟩
  have hs : s * s = 1 / 2 := by rw [hsdef]; exact Real.mul_self_sqrt (by norm_num)
  have hs2 : s ^ 2 = 1 / 2 := by rw [sq]; exact hs
  have hsC : ((s : ℝ) : ℂ) * ((s : ℝ) : ℂ) = ((1 / 2 : ℝ) : ℂ) := by
    rw [← Complex.ofReal_mul, hs]
  obtain ⟨UB, hUB⟩ : ∃ UB : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ,
      UB = Matrix.of fun p q =>
        if p = (0, 0) then (if q = (0, 0) then 1 else 0)
        else if p = (0, 1) then
          (if q = (0, 1) then ((s : ℝ) : ℂ) else if q = (1, 0) then ((s : ℝ) : ℂ) else 0)
        else if p = (1, 0) then
          (if q = (0, 1) then -((s : ℝ) : ℂ) else if q = (1, 0) then ((s : ℝ) : ℂ) else 0)
        else (if q = (1, 1) then 1 else 0) := ⟨_, rfl⟩
  obtain ⟨ρ, hρ⟩ : ∃ ρ : Equiv.Perm (Fin 2 × Fin 2),
      ρ = Equiv.swap ((0 : Fin 2), (1 : Fin 2)) ((1 : Fin 2), (1 : Fin 2)) := ⟨_, rfl⟩
  have hUBunit : UB ∈ Matrix.unitaryGroup (Fin 2 × Fin 2) ℂ := by
    rw [Matrix.mem_unitaryGroup_iff, Matrix.star_eq_conjTranspose]
    ext p q
    obtain ⟨x, y⟩ := p
    obtain ⟨u, v⟩ := q
    fin_cases x <;> fin_cases y <;> fin_cases u <;> fin_cases v <;>
      simp [hUB, Matrix.mul_apply, Fintype.sum_prod_type, Fin.sum_univ_two,
        Matrix.conjTranspose_apply, Complex.conj_ofReal, hsC] <;>
      ring_nf
  have hBT : AdmissibleDilationAt
      ((Matrix.of fun i j => if i = 0 then (if j = 0 then (1 : ℝ) else 0) else 1 / 2 :
        Matrix (Fin 2) (Fin 2) ℝ))ᵀ (0 : Fin 2) UB := by
    refine ⟨hUBunit, fun i j => ?_⟩
    fin_cases i <;> fin_cases j <;> simp [hUB, Fin.sum_univ_two, Matrix.transpose_apply, hs2]
  have hfix : ∀ p j, (ρ.permMatrix ℂ) p (j, (0 : Fin 2))
      = if p = (j, (0 : Fin 2)) then 1 else 0 := by
    intro p j
    obtain ⟨x, y⟩ := p
    fin_cases x <;> fin_cases y <;> fin_cases j <;> simp +decide [hρ]
  have hρstrong : StrongAnchorStabilizer (0 : Fin 2) (ρ.permMatrix ℂ) :=
    ⟨permMatrix_mem_unitaryGroup ρ, hfix⟩
  have hone : StrongAnchorStabilizer (0 : Fin 2) (1 : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ) :=
    ⟨one_mem _, fun p j => by rw [Matrix.one_apply]⟩
  refine ⟨fun t => if t = 0 then
      ((Matrix.of fun i j => if i = 0 then (if j = 0 then (1 : ℝ) else 0) else 1 / 2 :
        Matrix (Fin 2) (Fin 2) ℝ))ᵀ else 1,
    fun t => if t = 0 then UB else 1,
    fun t => (if t = 0 then UB else 1) * (if t = 0 then ρ.permMatrix ℂ else 1),
    fun t => if t = 0 then ρ.permMatrix ℂ else 1,
    ?_, ?_, ?_, ?_, ?_, ?_, ?_, fun _ => rfl, ?_, ?_, ?_, ?_, ?_, ?_⟩
  · simp only [↓reduceIte]
    rw [hUB, hsdef]
  · intro t ht
    simp only [if_neg ht]
  · simp only [↓reduceIte, hρ]
  · intro t ht
    simp only [if_neg ht, Matrix.mul_one]
  · intro t
    by_cases ht : t = 0
    · subst ht
      show AdmissibleDilationAt
        ((Matrix.of fun i j => if i = 0 then (if j = 0 then (1 : ℝ) else 0) else 1 / 2 :
          Matrix (Fin 2) (Fin 2) ℝ))ᵀ (0 : Fin 2) UB
      exact hBT
    · simp only [if_neg ht]; exact one_admissible_at_every_anchor _
  · intro t
    by_cases ht : t = 0
    · subst ht
      show AdmissibleDilationAt
        ((Matrix.of fun i j => if i = 0 then (if j = 0 then (1 : ℝ) else 0) else 1 / 2 :
          Matrix (Fin 2) (Fin 2) ℝ))ᵀ (0 : Fin 2) (UB * ρ.permMatrix ℂ)
      exact admissible_mul_of_fixes_anchor hBT (permMatrix_mem_unitaryGroup ρ) hfix
    · simp only [if_neg ht, Matrix.mul_one]; exact one_admissible_at_every_anchor _
  · intro t
    by_cases ht : t = 0
    · subst ht
      show StrongAnchorStabilizer (0 : Fin 2) (ρ.permMatrix ℂ)
      exact hρstrong
    · simp only [if_neg ht]
      exact hone
  · refine ⟨0, 1, ?_⟩
    show ρ.permMatrix ℂ ≠ (1 : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ)
    intro hcon
    have h01 := congrFun (congrFun hcon ((0 : Fin 2), (1 : Fin 2))) ((1 : Fin 2), (1 : Fin 2))
    rw [permMatrix_apply_eq, Matrix.one_apply] at h01
    simp +decide [hρ] at h01
  · intro i t s
    exact ct3g_fibreCrossGram_strong_right (fun t => if t = 0 then UB else 1)
      (fun t => if t = 0 then ρ.permMatrix ℂ else 1)
      (fun t => by
        by_cases ht : t = 0
        · simp only [if_pos ht]; exact hρstrong
        · simp only [if_neg ht]; exact hone) i t s
  · show ((if (0 : ℕ) = 0 then UB else 1)ᴴ * if (1 : ℕ) = 0 then UB else 1)
      ((0 : Fin 2), (1 : Fin 2)) ((1 : Fin 2), (1 : Fin 2)) = 0
    simp only [↓reduceIte]
    simp +decide [hUB]
  · show (((if (0 : ℕ) = 0 then UB else 1) * (if (0 : ℕ) = 0 then ρ.permMatrix ℂ else 1))ᴴ
      * ((if (1 : ℕ) = 0 then UB else 1) * (if (1 : ℕ) = 0 then ρ.permMatrix ℂ else 1)))
      ((0 : Fin 2), (1 : Fin 2)) ((1 : Fin 2), (1 : Fin 2)) = 1
    simp only [↓reduceIte, Matrix.conjTranspose_mul, Matrix.conjTranspose_permMatrix]
    simp +decide [hρ, hUB, permMatrix_mul_apply, Matrix.conjTranspose_apply]
  · show (∑ a : Fin 2, ‖((1 : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ) * UBᴴ)
      ((0 : Fin 2), a) ((1 : Fin 2), (0 : Fin 2))‖ ^ 2) = 1 / 2
    simp [one_mul, Matrix.conjTranspose_apply, hUB, Fin.sum_univ_two, hs2]
  · show (∑ a : Fin 2, ‖(((1 : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ)
          * (1 : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ))
        * (UB * ρ.permMatrix ℂ)ᴴ)
      ((0 : Fin 2), a) ((1 : Fin 2), (0 : Fin 2))‖ ^ 2) = 0
    simp only [Matrix.one_mul, Matrix.conjTranspose_apply, mul_permMatrix_apply]
    simp +decide [hρ, hUB, Fin.sum_univ_two, Equiv.swap_apply_def]

/-! ### Section K — `CT3` (b): the Hadamard pair as the trajectory-type control -/

/-- **`CT3` (b) — THE HADAMARD PAIR IS THE TRAJECTORY-TYPE CONTROL, NOT A THREADING WITNESS.** Act
12's `TG3` pair — `U_t = H(1)`, `U'_0 = H(1)`, `U'_t = H(i)` for `t ≥ 1` — consumed from
`hadamard_lifts_not_twoSided` with its matrices pinned by the same equations: two coherent lifts of
one visible family whose per-time Gram data are already **inequivalent** at `t = 1`
(`hadamard_slices_not_twoSided`, consumed), so **not** a pair sharing every per-time Gram matrix. At
`|A| = 1` every column is anchored and the three levels coincide; the pair is separated at the
smallest level: `Ξ^{(t,s)}(U) = 𝟙` for every `t, s`, while `Ξ^{(0,1)}(U') = H(1)ᴴ H(i) ≠ 𝟙`. The
certificate is the identity `H(1)ᴴ H(i) = 𝟙 ⟹ H(i) = H(1)`, refuted at the entry `(1,1)`. -/
theorem ct3b_hadamard_trajectory_control :
    ∃ (Γ : ℕ → Matrix (Fin 4) (Fin 4) ℝ) (U U' : ℕ → Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ),
      (∀ t, U t = Matrix.of (fun p q : Fin 4 × Fin 1 =>
          (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, 1, -1; 1, -1, -1, 1] p.1 q.1))
        ∧ U' 0 = U 0
        ∧ (∀ t, t ≠ 0 → U' t = Matrix.of (fun p q : Fin 4 × Fin 1 =>
            (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1;
              1, -Complex.I, -1, Complex.I] p.1 q.1))
        ∧ CoherentLift (0 : Fin 1) Γ U ∧ CoherentLift (0 : Fin 1) Γ U'
        ∧ ¬ GramPhaseEquiv (FibreGram (0 : Fin 1) (U 1)) (FibreGram (0 : Fin 1) (U' 1))
        ∧ (∀ t s, CrossGram U t s = 1)
        ∧ CrossGram U' 0 1 ≠ 1 := by
  classical
  obtain ⟨Γ, H₁, Hᵢ, -, hH₁, hHᵢ, -, -, hnotG, -⟩ := hadamard_slices_not_twoSided
  obtain ⟨Γ', U, U', hU, hU'0, hU't, hcohU, hcohU', -, -⟩ := hadamard_lifts_not_twoSided
  refine ⟨Γ', U, U', hU, hU'0, hU't, hcohU, hcohU', ?_, ?_, ?_⟩
  · rw [hU 1, hU't 1 one_ne_zero, ← hH₁, ← hHᵢ]
    exact hnotG
  · intro t s
    have hunit : ∀ t, U t ∈ Matrix.unitaryGroup (Fin 4 × Fin 1) ℂ := fun t => (hcohU t).1
    have hconst : U s = U t := by rw [hU s, hU t]
    rw [CrossGram, hconst]
    have h := Matrix.mem_unitaryGroup_iff'.1 (hunit t)
    rwa [Matrix.star_eq_conjTranspose] at h
  · intro hcon
    have h1 : U' 0 * (U' 0)ᴴ = 1 := by
      have h := Matrix.mem_unitaryGroup_iff.1 (hcohU' 0).1
      rwa [Matrix.star_eq_conjTranspose] at h
    have heq : U' 1 = U' 0 := by
      calc U' 1 = (U' 0 * (U' 0)ᴴ) * U' 1 := by rw [h1, Matrix.one_mul]
        _ = U' 0 * CrossGram U' 0 1 := by rw [Matrix.mul_assoc]; rfl
        _ = U' 0 := by rw [hcon, Matrix.mul_one]
    rw [hU't 1 one_ne_zero, hU'0, hU 0] at heq
    have h11 := congrFun (congrFun heq ((1 : Fin 4), (0 : Fin 1))) ((1 : Fin 4), (0 : Fin 1))
    simp at h11
    norm_num [Complex.ext_iff] at h11

/-! ### Section L — `CT3` (c): the constant-lift variant of `GL2` -/

/-- **`CT3` (c) — THE ANCHORED COLUMNS OF `Ξ` DO NOT SEPARATE EVERY `GL2`-TYPE PAIR.** The
constant-lift variant: `U_t = U_B` for every `t`; `U'_0 = U_B P(ρ)`, `U'_t = U_B` for `t ≥ 1`, with
`ρ = swap((0,1),(1,1))`. Both are coherent lifts of the constant family `Bᵀ`; the relating element
`K_0 = P(ρ)`, `K_t = 𝟙` is strong and time-dependent, exactly as in `GL2`. Because the lift `U` is
constant, `Ξ^{(t,s)}(U) = 𝟙` and `Ξ^{(t,s)}(U') = K_tᴴ K_s`, whose **every anchored column** equals
the corresponding column of `𝟙` (`strong_pair_anchored_col`) — so every level-2 datum and every
off-anchor-row × anchored-column entry agree. The two cross-Grams differ only on the
**off-anchor × off-anchor** block: `Ξ^{(0,1)}(U') = P(ρ)ᴴ ≠ 𝟙` at the entry `((0,1),(0,1))`,
values `1` for `U` and `0` for `U'`. The relative objects are `U_1 U_0ᴴ = 𝟙` and
`U'_1 U'_0ᴴ = U_B P(ρ)ᴴ U_Bᴴ`, and the relative candidates differ at `(0,1)`: `0` against `1/4`.

**So the least column-Gram datum separating all `GL2`-type pairs is not the anchored-column block
of `Ξ`**; whether it is `Ξ` itself is the fork `CT3` (d), which this round leaves UNDECIDED. -/
theorem ct3c_constant_lift_variant :
    ∃ (Γ : ℕ → Matrix (Fin 2) (Fin 2) ℝ)
      (U U' K : ℕ → Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ),
      (∀ t, U t = Matrix.of (fun p q : Fin 2 × Fin 2 =>
          if p = (0, 0) then (if q = (0, 0) then 1 else 0)
          else if p = (0, 1) then
            (if q = (0, 1) then ((Real.sqrt (1 / 2) : ℝ) : ℂ)
              else if q = (1, 0) then ((Real.sqrt (1 / 2) : ℝ) : ℂ) else 0)
          else if p = (1, 0) then
            (if q = (0, 1) then -((Real.sqrt (1 / 2) : ℝ) : ℂ)
              else if q = (1, 0) then ((Real.sqrt (1 / 2) : ℝ) : ℂ) else 0)
          else (if q = (1, 1) then 1 else 0)))
        ∧ U' 0 = U 0 * (Equiv.swap ((0 : Fin 2), (1 : Fin 2)) ((1 : Fin 2), (1 : Fin 2))
            : Equiv.Perm (Fin 2 × Fin 2)).permMatrix ℂ
        ∧ (∀ t, t ≠ 0 → U' t = U 0)
        ∧ CoherentLift (0 : Fin 2) Γ U ∧ CoherentLift (0 : Fin 2) Γ U'
        ∧ (∀ t, StrongAnchorStabilizer (0 : Fin 2) (K t))
        ∧ (∀ t, U' t = U t * K t)
        ∧ (∃ t s : ℕ, K t ≠ K s)
        ∧ (∀ t s (p : Fin 2 × Fin 2) (j : Fin 2),
            CrossGram U' t s p (j, 0) = CrossGram U t s p (j, 0))
        ∧ (∀ i t s, FibreCrossGram (0 : Fin 2) U' i t s = FibreCrossGram (0 : Fin 2) U i t s)
        ∧ CrossGram U 0 1 ((0 : Fin 2), (1 : Fin 2)) ((0 : Fin 2), (1 : Fin 2)) = 1
        ∧ CrossGram U' 0 1 ((0 : Fin 2), (1 : Fin 2)) ((0 : Fin 2), (1 : Fin 2)) = 0
        ∧ readback (0 : Fin 2) (Matrix.of fun p q => ‖(U 1 * (U 0)ᴴ) p q‖ ^ 2) 0 1 = 0
        ∧ readback (0 : Fin 2) (Matrix.of fun p q => ‖(U' 1 * (U' 0)ᴴ) p q‖ ^ 2) 0 1 = 1 / 4 := by
  classical
  obtain ⟨s, hsdef⟩ : ∃ s : ℝ, s = Real.sqrt (1 / 2) := ⟨_, rfl⟩
  have hs : s * s = 1 / 2 := by rw [hsdef]; exact Real.mul_self_sqrt (by norm_num)
  have hs2 : s ^ 2 = 1 / 2 := by rw [sq]; exact hs
  have hsC : ((s : ℝ) : ℂ) * ((s : ℝ) : ℂ) = ((1 / 2 : ℝ) : ℂ) := by
    rw [← Complex.ofReal_mul, hs]
  obtain ⟨UB, hUB⟩ : ∃ UB : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ,
      UB = Matrix.of fun p q =>
        if p = (0, 0) then (if q = (0, 0) then 1 else 0)
        else if p = (0, 1) then
          (if q = (0, 1) then ((s : ℝ) : ℂ) else if q = (1, 0) then ((s : ℝ) : ℂ) else 0)
        else if p = (1, 0) then
          (if q = (0, 1) then -((s : ℝ) : ℂ) else if q = (1, 0) then ((s : ℝ) : ℂ) else 0)
        else (if q = (1, 1) then 1 else 0) := ⟨_, rfl⟩
  obtain ⟨ρ, hρ⟩ : ∃ ρ : Equiv.Perm (Fin 2 × Fin 2),
      ρ = Equiv.swap ((0 : Fin 2), (1 : Fin 2)) ((1 : Fin 2), (1 : Fin 2)) := ⟨_, rfl⟩
  have hUBunit : UB ∈ Matrix.unitaryGroup (Fin 2 × Fin 2) ℂ := by
    rw [Matrix.mem_unitaryGroup_iff, Matrix.star_eq_conjTranspose]
    ext p q
    obtain ⟨x, y⟩ := p
    obtain ⟨u, v⟩ := q
    fin_cases x <;> fin_cases y <;> fin_cases u <;> fin_cases v <;>
      simp [hUB, Matrix.mul_apply, Fintype.sum_prod_type, Fin.sum_univ_two,
        Matrix.conjTranspose_apply, Complex.conj_ofReal, hsC] <;>
      ring_nf
  have hUBUB : UB * UBᴴ = 1 := by
    have h := Matrix.mem_unitaryGroup_iff.1 hUBunit
    rwa [Matrix.star_eq_conjTranspose] at h
  have hBT : AdmissibleDilationAt
      ((Matrix.of fun i j => if i = 0 then (if j = 0 then (1 : ℝ) else 0) else 1 / 2 :
        Matrix (Fin 2) (Fin 2) ℝ))ᵀ (0 : Fin 2) UB := by
    refine ⟨hUBunit, fun i j => ?_⟩
    fin_cases i <;> fin_cases j <;> simp [hUB, Fin.sum_univ_two, Matrix.transpose_apply, hs2]
  have hfix : ∀ p j, (ρ.permMatrix ℂ) p (j, (0 : Fin 2))
      = if p = (j, (0 : Fin 2)) then 1 else 0 := by
    intro p j
    obtain ⟨x, y⟩ := p
    fin_cases x <;> fin_cases y <;> fin_cases j <;> simp +decide [hρ]
  have hρstrong : StrongAnchorStabilizer (0 : Fin 2) (ρ.permMatrix ℂ) :=
    ⟨permMatrix_mem_unitaryGroup ρ, hfix⟩
  have hone : StrongAnchorStabilizer (0 : Fin 2) (1 : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ) :=
    ⟨one_mem _, fun p j => by rw [Matrix.one_apply]⟩
  have hK : ∀ t, StrongAnchorStabilizer (0 : Fin 2)
      (if t = 0 then ρ.permMatrix ℂ else (1 : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ)) := by
    intro t
    by_cases ht : t = 0
    · simp only [if_pos ht]; exact hρstrong
    · simp only [if_neg ht]; exact hone
  have hcrossU : ∀ t s, CrossGram (fun _ => UB) t s = 1 := fun t _ =>
    crossGram_self (fun _ => hUBunit) t
  have hcrossU' : ∀ t s, CrossGram (fun t => UB * if t = 0 then ρ.permMatrix ℂ else 1) t s
      = (if t = 0 then ρ.permMatrix ℂ else 1)ᴴ * (if s = 0 then ρ.permMatrix ℂ else 1) := by
    intro t s
    rw [crossGram_mul_right (fun _ => UB) (fun t => if t = 0 then ρ.permMatrix ℂ else 1),
      hcrossU, Matrix.mul_one]
  refine ⟨fun _ =>
      ((Matrix.of fun i j => if i = 0 then (if j = 0 then (1 : ℝ) else 0) else 1 / 2 :
        Matrix (Fin 2) (Fin 2) ℝ))ᵀ,
    fun _ => UB,
    fun t => UB * if t = 0 then ρ.permMatrix ℂ else 1,
    fun t => if t = 0 then ρ.permMatrix ℂ else 1,
    ?_, ?_, ?_, fun _ => hBT, ?_, hK, fun _ => rfl, ?_, ?_, ?_, ?_, ?_, ?_, ?_⟩
  · intro t
    rw [hUB, hsdef]
  · simp only [↓reduceIte, hρ]
  · intro t ht
    simp only [if_neg ht, Matrix.mul_one]
  · intro t
    by_cases ht : t = 0
    · subst ht
      simp only [↓reduceIte]
      exact admissible_mul_of_fixes_anchor hBT (permMatrix_mem_unitaryGroup ρ) hfix
    · simp only [if_neg ht, Matrix.mul_one]; exact hBT
  · refine ⟨0, 1, ?_⟩
    show ρ.permMatrix ℂ ≠ (1 : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ)
    intro hcon
    have h01 := congrFun (congrFun hcon ((0 : Fin 2), (1 : Fin 2))) ((1 : Fin 2), (1 : Fin 2))
    rw [permMatrix_apply_eq, Matrix.one_apply] at h01
    simp +decide [hρ] at h01
  · intro t s p j
    rw [hcrossU', hcrossU, strong_pair_anchored_col (hK t) (hK s), Matrix.one_apply]
  · intro i t s
    exact ct3g_fibreCrossGram_strong_right (fun _ => UB)
      (fun t => if t = 0 then ρ.permMatrix ℂ else 1) hK i t s
  · rw [hcrossU, Matrix.one_apply_eq]
  · rw [hcrossU']
    simp only [↓reduceIte]
    simp +decide [hρ]
  · show (∑ a : Fin 2, ‖(UB * UBᴴ) ((0 : Fin 2), a) ((1 : Fin 2), (0 : Fin 2))‖ ^ 2) = 0
    rw [hUBUB]
    simp +decide
  · -- the relative object `U'_1 U'_0ᴴ = U_B P(ρ)ᴴ U_Bᴴ`, bound so that its entries can be rewritten
    obtain ⟨R, hR⟩ : ∃ R : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ,
        R = UB * (UB * ρ.permMatrix ℂ)ᴴ := ⟨_, rfl⟩
    have hrel : (UB * (1 : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ)) * (UB * ρ.permMatrix ℂ)ᴴ
        = R := by rw [Matrix.mul_one, hR]
    have e0 : R ((0 : Fin 2), (0 : Fin 2)) ((1 : Fin 2), (0 : Fin 2)) = 0 := by
      rw [hR]
      simp only [Matrix.mul_apply, Matrix.conjTranspose_apply, Fintype.sum_prod_type,
        Fin.sum_univ_two]
      simp +decide [hρ, hUB]
    have e1 : R ((0 : Fin 2), (1 : Fin 2)) ((1 : Fin 2), (0 : Fin 2)) = ((1 / 2 : ℝ) : ℂ) := by
      rw [hR]
      simp only [Matrix.mul_apply, Matrix.conjTranspose_apply, Fintype.sum_prod_type,
        Fin.sum_univ_two]
      simp +decide [hρ, hUB, Complex.conj_ofReal]
      rw [hsC]
      norm_num
    show (∑ a : Fin 2, ‖((UB * (1 : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ))
        * (UB * ρ.permMatrix ℂ)ᴴ) ((0 : Fin 2), a) ((1 : Fin 2), (0 : Fin 2))‖ ^ 2) = 1 / 4
    rw [hrel, Fin.sum_univ_two, e0, e1]
    simp
    norm_num

/-! ### Section M — `CT4` and `CL1`: the constant-left obstruction -/

/-- **`CT4` — INSUFFICIENCY OF THE WHOLE FAMILY, BY THE CONSTANT-LEFT OBSTRUCTION.** On
`V = Fin 2`, `A = Fin 2`, `a₀ = 0`, with the constant identity law: the lifts `U_0 = 𝟙`,
`U_t = X := P(swap((0,1),(1,1)))` for `t ≥ 1`, and `U'_t = W U_t` with the **constant** in-fibre
swap `W = P(swap((0,0),(0,1))) ∈ 𝒢_L`. Both are coherent (`𝟙` and `X` are admissible for the
identity slice, `X` fixing both anchored columns; `W` is invisible by act 12's
`left_preserves_admissible`); `U' ≈_L U`; the column cross-Grams agree at **every** `t, s`
(`CT2` (a) backward), hence every level-2, level-1 and per-time Gram datum agrees (`CT2` (b)
backward, with `K ≡ 𝟙`); and the relative candidates differ at the entry `(0,0)`: `U_1 U_0ᴴ = X`
fixes `e_{(0,0)}`, so the readback is `1`, while `U'_1 U'_0ᴴ = W X Wᴴ` carries `e_{(0,0)}` to
`e_{(1,1)}`, in the other visible fibre, so the readback is `0`.

**Bounded reading:** no member of the frozen family, up to and including the full column
cross-Gram, determines the relative candidate; any datum that does must fail to be constant-left
invariant, hence must depend on the dilation's rows, not only its columns. That is a statement
about the **shape** of a sufficient datum, not the naming of one. **`|A| ≥ 2` is part of the
statement** — its first conjunct — because at `|A| = 1` the in-fibre group is the diagonal phases,
conjugation by which preserves every entrywise modulus, and the obstruction is absent. -/
theorem ct4_constant_left_obstruction :
    ∃ (Γ : ℕ → Matrix (Fin 2) (Fin 2) ℝ) (U U' : ℕ → Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ)
      (W : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ),
      (∀ a : Fin 2, ∃ a' : Fin 2, a' ≠ a)
        ∧ (∀ t, Γ t = 1)
        ∧ U 0 = 1
        ∧ (∀ t, t ≠ 0 → U t = (Equiv.swap ((0 : Fin 2), (1 : Fin 2)) ((1 : Fin 2), (1 : Fin 2))
            : Equiv.Perm (Fin 2 × Fin 2)).permMatrix ℂ)
        ∧ W = (Equiv.swap ((0 : Fin 2), (0 : Fin 2)) ((0 : Fin 2), (1 : Fin 2))
            : Equiv.Perm (Fin 2 × Fin 2)).permMatrix ℂ
        ∧ (∀ t, U' t = W * U t)
        ∧ LeftFibreGroup W
        ∧ CoherentLift (0 : Fin 2) Γ U ∧ CoherentLift (0 : Fin 2) Γ U'
        ∧ ConstLeftRelated U U'
        ∧ (∀ t s, CrossGram U' t s = CrossGram U t s)
        ∧ (∀ i t s, FibreCrossGram (0 : Fin 2) U' i t s = FibreCrossGram (0 : Fin 2) U i t s)
        ∧ readback (0 : Fin 2) (Matrix.of fun p q => ‖(U 1 * (U 0)ᴴ) p q‖ ^ 2) 0 0 = 1
        ∧ readback (0 : Fin 2) (Matrix.of fun p q => ‖(U' 1 * (U' 0)ᴴ) p q‖ ^ 2) 0 0 = 0 := by
  classical
  obtain ⟨σ, hσ⟩ : ∃ σ : Equiv.Perm (Fin 2 × Fin 2),
      σ = Equiv.swap ((0 : Fin 2), (1 : Fin 2)) ((1 : Fin 2), (1 : Fin 2)) := ⟨_, rfl⟩
  obtain ⟨τ, hτ⟩ : ∃ τ : Equiv.Perm (Fin 2 × Fin 2),
      τ = Equiv.swap ((0 : Fin 2), (0 : Fin 2)) ((0 : Fin 2), (1 : Fin 2)) := ⟨_, rfl⟩
  have hadmσ : AdmissibleDilationAt (1 : Matrix (Fin 2) (Fin 2) ℝ) (0 : Fin 2) (σ.permMatrix ℂ) := by
    refine admissible_permMatrix _ σ fun i j => ?_
    fin_cases i <;> fin_cases j <;> simp +decide [hσ, Equiv.swap_apply_def]
  have hτleft : LeftFibreGroup (τ.permMatrix ℂ) := by
    rw [hτ]; exact inFibreSwap_leftFibreGroup
  have hcohU : CoherentLift (0 : Fin 2) (fun _ => (1 : Matrix (Fin 2) (Fin 2) ℝ))
      (fun t => if t = 0 then 1 else σ.permMatrix ℂ) := by
    intro t
    by_cases ht : t = 0
    · simp only [if_pos ht]; exact one_admissible_at_every_anchor _
    · simp only [if_neg ht]; exact hadmσ
  refine ⟨fun _ => 1, fun t => if t = 0 then 1 else σ.permMatrix ℂ,
    fun t => τ.permMatrix ℂ * if t = 0 then 1 else σ.permMatrix ℂ, τ.permMatrix ℂ,
    ?_, fun _ => rfl, by simp, ?_, by rw [hτ], fun _ => rfl, hτleft, hcohU,
    fun t => left_preserves_admissible hτleft (hcohU t),
    ⟨τ.permMatrix ℂ, permMatrix_mem_unitaryGroup τ, fun _ => rfl⟩,
    fun t s => ct2a_backward (permMatrix_mem_unitaryGroup τ) _ t s,
    fun i t s => ct2b_backward ⟨τ.permMatrix ℂ, hτleft, fun _ => 1,
      fun _ => ⟨one_mem _, fun p j => Matrix.one_apply⟩,
      fun _ => (Matrix.mul_one _).symm⟩ i t s, ?_, ?_⟩
  · intro a
    fin_cases a
    · exact ⟨1, by decide⟩
    · exact ⟨0, by decide⟩
  · intro t ht
    simp only [if_neg ht, hσ]
  · show (∑ a : Fin 2, ‖((if (1 : ℕ) = 0 then 1 else σ.permMatrix ℂ)
        * (if (0 : ℕ) = 0 then (1 : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ) else σ.permMatrix ℂ)ᴴ)
      ((0 : Fin 2), a) ((0 : Fin 2), (0 : Fin 2))‖ ^ 2) = 1
    simp only [↓reduceIte, Matrix.conjTranspose_one, Matrix.mul_one]
    simp +decide [Fin.sum_univ_two, hσ, Equiv.swap_apply_def]
  · show (∑ a : Fin 2, ‖((τ.permMatrix ℂ * if (1 : ℕ) = 0 then 1 else σ.permMatrix ℂ)
        * (τ.permMatrix ℂ
            * if (0 : ℕ) = 0 then (1 : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ)
              else σ.permMatrix ℂ)ᴴ)
      ((0 : Fin 2), a) ((0 : Fin 2), (0 : Fin 2))‖ ^ 2) = 0
    simp only [↓reduceIte, Matrix.mul_one, Matrix.conjTranspose_permMatrix]
    simp +decide [Fin.sum_univ_two, Matrix.mul_apply, Fintype.sum_prod_type, hσ, hτ,
      Equiv.swap_apply_def]

/-- **`CL1` — A CONSTANT LEFT `𝒢_L` MOVE CAN CHANGE THE RELATIVE CANDIDATE.** The left counterpart
of `GL3` failing: `GL3` says a constant right gauge preserves every relative object; no analogue
holds on the left, even for the invisible group, because the readback of `W R Wᴴ` sees `Wᴴ` on the
input side. **Existential**: it says nothing about every constant left move. `GI2`'s pair, a
constant left move with identical relative objects, is not a counterexample and is not revised:
its lifts are constant in time, so `W R Wᴴ = W Wᴴ = 𝟙 = R` there. The `|A| ≥ 2` conjunct is the
scoping. -/
theorem cl1_constant_left_moves_relative_candidate :
    ∃ (Γ : ℕ → Matrix (Fin 2) (Fin 2) ℝ) (U : ℕ → Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ)
      (W : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ),
      (∀ a : Fin 2, ∃ a' : Fin 2, a' ≠ a)
        ∧ LeftFibreGroup W
        ∧ CoherentLift (0 : Fin 2) Γ U ∧ CoherentLift (0 : Fin 2) Γ (fun t => W * U t)
        ∧ readback (0 : Fin 2) (Matrix.of fun p q => ‖(U 1 * (U 0)ᴴ) p q‖ ^ 2)
            ≠ readback (0 : Fin 2)
                (Matrix.of fun p q => ‖((W * U 1) * (W * U 0)ᴴ) p q‖ ^ 2) := by
  obtain ⟨Γ, U, U', W, htwo, -, -, -, -, hU', hW, hcoh, hcoh', -, -, -, h1, h0⟩ :=
    ct4_constant_left_obstruction
  have hU'eq : (fun t => W * U t) = U' := funext fun t => (hU' t).symm
  refine ⟨Γ, U, W, htwo, hW, hcoh, by rw [hU'eq]; exact hcoh', fun hcon => ?_⟩
  have h := congrFun (congrFun hcon 0) 0
  rw [h1, ← hU' 1, ← hU' 0, h0] at h
  norm_num at h

end CrossTimeInvariants
end OIBridge

/-! ### Axiom report — one line per named result -/

#print axioms OIBridge.CrossTimeInvariants.crossGram_apply
#print axioms OIBridge.CrossTimeInvariants.crossGram_self
#print axioms OIBridge.CrossTimeInvariants.fibreCrossGram_apply
#print axioms OIBridge.CrossTimeInvariants.fibreCrossGram_apply_dotProduct
#print axioms OIBridge.CrossTimeInvariants.fibreCrossGram_diag
#print axioms OIBridge.CrossTimeInvariants.sum_fibreCrossGram
#print axioms OIBridge.CrossTimeInvariants.crossGram_two_sided
#print axioms OIBridge.CrossTimeInvariants.crossGram_left_mul
#print axioms OIBridge.CrossTimeInvariants.crossGram_mul_right
#print axioms OIBridge.CrossTimeInvariants.mul_strong_anchor_col
#print axioms OIBridge.CrossTimeInvariants.mul_strong_submatrix
#print axioms OIBridge.CrossTimeInvariants.fibreCrossGram_mul_weak_apply
#print axioms OIBridge.CrossTimeInvariants.ct3g_fibreCrossGram_strong_right
#print axioms OIBridge.CrossTimeInvariants.ct3g_fibreGram_strong_right
#print axioms OIBridge.CrossTimeInvariants.ct3g_anchored_block_strong_right
#print axioms OIBridge.CrossTimeInvariants.constRight_forced
#print axioms OIBridge.CrossTimeInvariants.constLeft_forced
#print axioms OIBridge.CrossTimeInvariants.ct1_forward
#print axioms OIBridge.CrossTimeInvariants.ct1_backward
#print axioms OIBridge.CrossTimeInvariants.ct1_relative_iff_constRight
#print axioms OIBridge.CrossTimeInvariants.ct2a_forward
#print axioms OIBridge.CrossTimeInvariants.ct2a_backward
#print axioms OIBridge.CrossTimeInvariants.ct2a_crossGram_iff_constLeft
#print axioms OIBridge.CrossTimeInvariants.ct2a_relative_conj
#print axioms OIBridge.CrossTimeInvariants.ct2b_backward
#print axioms OIBridge.CrossTimeInvariants.exists_unitary_of_inner_eq
#print axioms OIBridge.CrossTimeInvariants.ct2b_forward
#print axioms OIBridge.CrossTimeInvariants.ct2b_fibreCrossGram_iff
#print axioms OIBridge.CrossTimeInvariants.strong_anchored_row
#print axioms OIBridge.CrossTimeInvariants.strong_pair_anchored_col
#print axioms OIBridge.CrossTimeInvariants.ct3a_gl2_pair_separated_by_crossGram
#print axioms OIBridge.CrossTimeInvariants.ct3b_hadamard_trajectory_control
#print axioms OIBridge.CrossTimeInvariants.ct3c_constant_lift_variant
#print axioms OIBridge.CrossTimeInvariants.ct4_constant_left_obstruction
#print axioms OIBridge.CrossTimeInvariants.cl1_constant_left_moves_relative_candidate
