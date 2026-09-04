import Mathlib.Analysis.Matrix.Order
import OIBridge.AncillaClosure
import OIBridge.CompositeSoundness
import OIBridge.ClosureObstruction
import OIBridge.ReferenceSufficiency

/-!
# Passive observation on a matrix algebra, and its commutative control (OI-N1, OI-N2)

The exploratory OI-N thread asks whether quantum noncommutativity is exactly the obstruction to
**complete passive observation**: learning the state while leaving every state unchanged on
average. This file settles the two easy ends of that question in the matrix algebra, and fixes
the definitions the rest of the thread depends on.

* A **passive instrument** is a finite family of completely positive maps whose nonselective
  channel is the identity, `∑ a, F a = id`.
* An instrument is **state-separating** when distinct density matrices produce distinct outcome
  laws.

**OI-N1** (`passive_branch_scalar`, `no_complete_passive_observation`). Every branch of a passive
instrument on `Matrix S S ℂ` is a scalar multiple of the identity, so its outcome law is the same
for every state; when `S` has at least two elements no passive instrument separates states. The
proof is the Choi argument: the identity has a rank-one Choi matrix `ω ω†`, the branches' Choi
matrices are positive semidefinite and sum to it, and a positive semidefinite summand of a rank-one
positive semidefinite matrix is a scalar multiple of it (`psd_summand_of_rankOne`, proved here from
`PosSemidef.dotProduct_mulVec_zero_iff` and an elementary double-orthogonal-complement step).

**OI-N2** (`pinching_passive_on_diagonal`, `pinching_separates_diagonal`). On the commutative
subalgebra of diagonal matrices, the pinching instrument `X ↦ E_aa X E_aa` is completely positive,
acts as the identity on every diagonal matrix, and separates diagonal states. On the full matrix
algebra its nonselective channel is the dephasing map, not the identity (`pinching_sum_apply`,
`pinching_not_passive`), so it is not a passive instrument there — exactly as N1 requires. That is the
control. N1 excludes complete passive observation on a full matrix algebra and N2 supplies the
diagonal commutative control; their contrast identifies noncommutativity as the *candidate*
obstruction, whose exact finite-dimensional boundary is N3 and is not proved here.

**Not claimed.** The exact boundary for a general finite-dimensional C*-algebra `⊕ M_{d_i}`
(OI-N3) is not proved here; the commutative direction is the control above, and the converse needs
the direct-sum case handled explicitly. Nothing here says a passive instrument's silence is an
observer, and nothing here relates passive incompleteness to `OICore` (OI-N4).
-/

namespace OIBridge
namespace PassiveObservation

open Matrix CoherentExtension MonoidalCompletion DimensionalCountermodel
open CompositeSoundness AncillaClosure ClosureObstruction ReferenceSufficiency
open scoped ComplexOrder

/-! ### Section A — a positive semidefinite summand of a rank-one matrix is a multiple of it -/

section RankOne

variable {n : Type*} [Fintype n] [DecidableEq n]

omit [DecidableEq n] in
/-- The action of `v v†` on a vector: `(v v†) w = ⟨v, w⟩ v`. -/
theorem vecMulVec_star_mulVec (v w : n → ℂ) :
    vecMulVec v (star v) *ᵥ w = (star v ⬝ᵥ w) • v := by
  ext i
  simp [mulVec, dotProduct, vecMulVec, Finset.mul_sum, mul_comm, mul_left_comm, mul_assoc]

/-- The quadratic form of `v v†`: `w† (v v†) w = |⟨v, w⟩|²`, so it vanishes on `v^⊥`. -/
theorem vecMulVec_star_mulVec_orth (v w : n → ℂ) (h : star v ⬝ᵥ w = 0) :
    vecMulVec v (star v) *ᵥ w = 0 := by
  rw [vecMulVec_star_mulVec, h, zero_smul]

/-- `w ⊥ v` with `⟨v, w⟩` written on the other side. -/
theorem star_dotProduct_comm_zero (v w : n → ℂ) (h : star v ⬝ᵥ w = 0) : star w ⬝ᵥ v = 0 := by
  have : star w ⬝ᵥ v = star (star v ⬝ᵥ w) := by
    simp [dotProduct, star_sum, star_mul', mul_comm]
  rw [this, h, star_zero]

/-- **The double orthogonal complement, by hand.** If `y` is orthogonal to every vector orthogonal
to `v ≠ 0`, then `y` is a multiple of `v`. The witness is `c = ⟨v, y⟩ / ⟨v, v⟩`, and the argument is
that `w = y - c v` is orthogonal to `v`, hence to `y`, hence to itself. -/
theorem exists_smul_of_orth (v y : n → ℂ) (hv : v ≠ 0)
    (h : ∀ w, star v ⬝ᵥ w = 0 → star w ⬝ᵥ y = 0) : ∃ c : ℂ, y = c • v := by
  have hvv : star v ⬝ᵥ v ≠ 0 := by
    intro h0
    exact hv (dotProduct_star_self_eq_zero.mp h0)
  set c : ℂ := (star v ⬝ᵥ y) / (star v ⬝ᵥ v) with hc
  set w : n → ℂ := y - c • v with hw
  have hwv : star v ⬝ᵥ w = 0 := by
    rw [hw, dotProduct_sub, dotProduct_smul, hc, smul_eq_mul, div_mul_cancel₀ _ hvv, sub_self]
  have hwy : star w ⬝ᵥ y = 0 := h w hwv
  have hww : star w ⬝ᵥ w = 0 := by
    rw [hw, dotProduct_sub, dotProduct_smul, ← hw, hwy, smul_eq_mul,
      star_dotProduct_comm_zero v w hwv, mul_zero, sub_zero]
  have : w = 0 := dotProduct_star_self_eq_zero.mp hww
  refine ⟨c, ?_⟩
  rw [hw] at this
  exact (sub_eq_zero.mp this)

omit [DecidableEq n] in
/-- `w† A v = (A w)† v` for Hermitian `A`. -/
theorem star_dotProduct_mulVec_hermitian {A : Matrix n n ℂ} (hA : A.IsHermitian) (w v : n → ℂ) :
    star w ⬝ᵥ A *ᵥ v = star (A *ᵥ w) ⬝ᵥ v := by
  rw [star_mulVec, hA.eq, dotProduct_mulVec]

/-- Real parts: two nonnegative complex numbers summing to zero are both zero. -/
theorem eq_zero_of_add_eq_zero_of_nonneg {a b : ℂ} (ha : 0 ≤ a) (hb : 0 ≤ b) (h : a + b = 0) :
    a = 0 := by
  rw [Complex.nonneg_iff] at ha hb
  apply Complex.ext
  · have h1 : a.re + b.re = 0 := by simpa using congrArg Complex.re h
    simp only [Complex.zero_re]
    linarith [ha.1, hb.1]
  · simp only [Complex.zero_im]
    exact ha.2.symm

/-- **A positive semidefinite summand of a rank-one positive semidefinite matrix is a multiple of
it.** If `A + B = v v†` with `A, B ⪰ 0`, then `A = c · v v†`. -/
theorem psd_summand_of_rankOne {A B : Matrix n n ℂ} (hA : A.PosSemidef) (hB : B.PosSemidef)
    (v : n → ℂ) (h : A + B = vecMulVec v (star v)) :
    ∃ c : ℂ, A = c • vecMulVec v (star v) := by
  -- Step 1: `A` kills `v^⊥`.
  have kill : ∀ w, star v ⬝ᵥ w = 0 → A *ᵥ w = 0 := by
    intro w hw
    have hsum : star w ⬝ᵥ A *ᵥ w + star w ⬝ᵥ B *ᵥ w = 0 := by
      rw [← dotProduct_add, ← add_mulVec, h, vecMulVec_star_mulVec_orth v w hw, dotProduct_zero]
    have hz : star w ⬝ᵥ A *ᵥ w = 0 :=
      eq_zero_of_add_eq_zero_of_nonneg (hA.dotProduct_mulVec_nonneg w)
        (hB.dotProduct_mulVec_nonneg w) hsum
    exact (hA.dotProduct_mulVec_zero_iff w).mp hz
  by_cases hv : v = 0
  · -- degenerate: `v v† = 0`, so `A` kills everything.
    refine ⟨0, ?_⟩
    have hall : ∀ w, A *ᵥ w = 0 := fun w => kill w (by simp [hv])
    ext i j
    have := congrFun (hall (Pi.single j 1)) i
    rw [mulVec_single_one] at this
    simpa [zero_smul, Matrix.zero_apply] using this
  -- Step 2: `A v` is a multiple of `v`, because `A v ⊥ v^⊥` by hermiticity.
  obtain ⟨lam, hlam⟩ := exists_smul_of_orth v (A *ᵥ v) hv (fun w hw => by
    rw [star_dotProduct_mulVec_hermitian hA.1, kill w hw, star_zero, zero_dotProduct])
  have hvv : star v ⬝ᵥ v ≠ 0 := fun h0 => hv (dotProduct_star_self_eq_zero.mp h0)
  refine ⟨lam / (star v ⬝ᵥ v), ?_⟩
  -- Step 3: compare the two matrices on every vector, decomposing `x = α v + w`.
  apply mulVec_injective
  funext x
  set α : ℂ := (star v ⬝ᵥ x) / (star v ⬝ᵥ v) with hα
  have hw : star v ⬝ᵥ (x - α • v) = 0 := by
    rw [dotProduct_sub, dotProduct_smul, hα, smul_eq_mul, div_mul_cancel₀ _ hvv, sub_self]
  have hx : x = α • v + (x - α • v) := by abel
  calc A *ᵥ x = A *ᵥ (α • v + (x - α • v)) := by rw [← hx]
    _ = α • (A *ᵥ v) + A *ᵥ (x - α • v) := by rw [mulVec_add, mulVec_smul]
    _ = α • (lam • v) := by rw [kill _ hw, add_zero, hlam]
    _ = (lam / (star v ⬝ᵥ v)) • (vecMulVec v (star v) *ᵥ x) := by
      rw [vecMulVec_star_mulVec, smul_smul, smul_smul]
      congr 1
      rw [hα]
      field_simp
    _ = ((lam / (star v ⬝ᵥ v)) • vecMulVec v (star v)) *ᵥ x := by rw [smul_mulVec]

end RankOne

/-! ### Section B — the identity channel has a rank-one Choi matrix -/

section Choi

variable {S : Type*} [Fintype S] [DecidableEq S]

/-- The vectorized identity, `ω (s, a) = [s = a]`. -/
def vecId : S × S → ℂ := fun p => (1 : Matrix S S ℂ) p.2 p.1

omit [Fintype S] in
theorem vecId_apply (p : S × S) : vecId p = (1 : Matrix S S ℂ) p.2 p.1 := rfl

/-- Conjugation by the identity matrix is the identity channel. -/
theorem conjChannel_one : conjChannel (1 : Matrix S S ℂ) = LinearMap.id := by
  apply LinearMap.ext
  intro X
  rw [conjChannel_apply, conjTranspose_one, Matrix.one_mul, Matrix.mul_one]
  rfl

/-- **The Choi matrix of the identity is rank one**: `ω ω†`. -/
theorem choiMatrix_id :
    choiMatrix (LinearMap.id : Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ)
      = vecMulVec (vecId (S := S)) (star vecId) := by
  rw [← conjChannel_one, choiMatrix_conjChannel]
  rfl

omit [Fintype S] in
theorem vecId_ne_zero [Nonempty S] : (vecId : S × S → ℂ) ≠ 0 := by
  intro h
  obtain ⟨s⟩ := ‹Nonempty S›
  have := congrFun h (s, s)
  simp [vecId_apply] at this

end Choi

/-! ### Section C — OI-N1: a passive instrument sees nothing -/

section N1

variable {S : Type*} [Fintype S] [DecidableEq S]
variable {O : Type*} [Fintype O] [DecidableEq O]

/-- **A passive instrument**: finitely many completely positive branches whose nonselective
channel is the identity. Passive because, averaged over outcomes, no state is changed. -/
def IsPassiveInstrument (F : O → Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ) : Prop :=
  (∀ a, IsCompletelyPositive (F a)) ∧ ∑ a, F a = LinearMap.id

/-- **State-separating** (informationally complete): distinct density matrices produce distinct
outcome laws. -/
def SeparatesStates (F : O → Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ) : Prop :=
  ∀ ρ σ : Matrix S S ℂ, ρ.PosSemidef → σ.PosSemidef → ρ.trace = 1 → σ.trace = 1 →
    (∀ a, ((F a) ρ).trace = ((F a) σ).trace) → ρ = σ

/-- **OI-N1, the branch form.** Every branch of a passive instrument is a scalar multiple of the
identity. The Choi matrices of the branches are positive semidefinite and sum to the rank-one
Choi matrix of the identity, so each is a multiple of it; Choi injectivity finishes. -/
theorem passive_branch_scalar {F : O → Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ}
    (h : IsPassiveInstrument F) (a : O) : ∃ c : ℂ, F a = c • LinearMap.id := by
  classical
  have hsum : choiMatrix (F a) + ∑ b ∈ Finset.univ.erase a, choiMatrix (F b)
      = vecMulVec (vecId (S := S)) (star vecId) := by
    rw [← choiMatrix_finsum, ← choiMatrix_add, ← Finset.sum_insert (Finset.notMem_erase a _),
      Finset.insert_erase (Finset.mem_univ a), h.2, choiMatrix_id]
  have hB : (∑ b ∈ Finset.univ.erase a, choiMatrix (F b)).PosSemidef := by
    rw [← choiMatrix_finsum]
    exact cp_sum _ _ fun b _ => h.1 b
  obtain ⟨c, hc⟩ := psd_summand_of_rankOne (h.1 a) hB vecId hsum
  refine ⟨c, choiMatrix_injective ?_⟩
  rw [hc, choiMatrix_smul, choiMatrix_id]

/-- **OI-N1, the outcome law.** The probability of each outcome of a passive instrument is the
same for every state of unit trace. -/
theorem passive_outcome_state_independent {F : O → Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ}
    (h : IsPassiveInstrument F) (a : O) :
    ∃ c : ℂ, ∀ ρ : Matrix S S ℂ, ((F a) ρ).trace = c * ρ.trace := by
  obtain ⟨c, hc⟩ := passive_branch_scalar h a
  refine ⟨c, fun ρ => ?_⟩
  rw [hc, LinearMap.smul_apply, LinearMap.id_apply, trace_smul, smul_eq_mul]

/-- The pure state `|s⟩⟨s|`, as the rank-one matrix `e_s e_s†`. -/
def pureState (s : S) : Matrix S S ℂ := vecMulVec (Pi.single s 1) (star (Pi.single s 1))

theorem pureState_apply (s i j : S) :
    pureState s i j = (if i = s then 1 else 0) * star (if j = s then (1 : ℂ) else 0) := by
  simp [pureState, vecMulVec_apply, Pi.single_apply]

/-- A pure state is a density matrix. -/
theorem pure_posSemidef (s : S) : (pureState s).PosSemidef :=
  posSemidef_vecMulVec_self_star _

theorem pure_trace (s : S) : (pureState s).trace = 1 := by
  simp [Matrix.trace, Matrix.diag, pureState_apply]

theorem pure_ne (s t : S) (hst : s ≠ t) : pureState s ≠ pureState t := by
  intro heq
  have := congrFun (congrFun heq s) s
  simp [pureState_apply, hst] at this

/-- **OI-N1.** When the algebra has at least two states to tell apart, no passive instrument
separates states: two distinct pure states receive the identical outcome law. -/
theorem no_complete_passive_observation {F : O → Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ}
    (h : IsPassiveInstrument F) (hS : 1 < Fintype.card S) : ¬ SeparatesStates F := by
  intro hsep
  obtain ⟨s, t, hst⟩ := Fintype.exists_pair_of_one_lt_card hS
  apply pure_ne s t hst
  apply hsep _ _ (pure_posSemidef s) (pure_posSemidef t) (pure_trace s) (pure_trace t)
  intro a
  obtain ⟨c, hc⟩ := passive_outcome_state_independent h a
  rw [hc, hc, pure_trace, pure_trace]

end N1

/-! ### Section D — OI-N2: the commutative control -/

section N2

variable {S : Type*} [Fintype S] [DecidableEq S]

/-- The pinching branch at the atom `a`: `X ↦ E_aa X E_aa`. -/
def pinching (a : S) : Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ :=
  conjChannel (Matrix.single a a 1)

/-- Each pinching branch is completely positive: it is a conjugation. -/
theorem pinching_cp (a : S) : IsCompletelyPositive (pinching a) := by
  show (choiMatrix (conjChannel _)).PosSemidef
  rw [choiMatrix_conjChannel]
  exact posSemidef_vecMulVec_self_star _

/-- A matrix is diagonal when its off-diagonal entries vanish. -/
def IsDiagonal (X : Matrix S S ℂ) : Prop := ∀ i j, i ≠ j → X i j = 0

theorem pinching_apply (a : S) (X : Matrix S S ℂ) (i j : S) :
    pinching a X i j = if i = a ∧ j = a then X a a else 0 := by
  simp only [pinching, conjChannel_apply]
  by_cases hi : i = a <;> by_cases hj : j = a <;>
    simp [Matrix.mul_apply, Matrix.single, Finset.sum_ite_eq, Finset.sum_ite_eq', hi, hj] <;>
    simp_all [eq_comm]

/-- **OI-N2, passivity on the commutative algebra.** On every diagonal matrix the pinching
instrument's nonselective channel is the identity. -/
theorem pinching_passive_on_diagonal (X : Matrix S S ℂ) (hX : IsDiagonal X) :
    ∑ a, pinching a X = X := by
  ext i j
  rw [Matrix.sum_apply]
  simp only [pinching_apply]
  by_cases hij : i = j
  · subst hij
    simp
  · rw [hX i j hij]
    refine Finset.sum_eq_zero fun a _ => ?_
    have : ¬ (i = a ∧ j = a) := fun ⟨h1, h2⟩ => hij (h1.trans h2.symm)
    simp [this]

/-- The outcome law of the pinching instrument reads the diagonal. -/
theorem pinching_trace (a : S) (X : Matrix S S ℂ) : (pinching a X).trace = X a a := by
  simp [Matrix.trace, Matrix.diag, pinching_apply]

/-- **OI-N2, completeness on the commutative algebra.** Two diagonal matrices with the same
pinching outcome law are equal: the classical state is read off without disturbance. -/
theorem pinching_separates_diagonal (ρ σ : Matrix S S ℂ) (hρ : IsDiagonal ρ) (hσ : IsDiagonal σ)
    (h : ∀ a, (pinching a ρ).trace = (pinching a σ).trace) : ρ = σ := by
  ext i j
  by_cases hij : i = j
  · subst hij
    have := h i
    rwa [pinching_trace, pinching_trace] at this
  · rw [hρ i j hij, hσ i j hij]

/-- **Where passivity stops.** On the full matrix algebra the nonselective pinching channel is the
dephasing map: it keeps the diagonal and kills every off-diagonal entry. -/
theorem pinching_sum_apply (X : Matrix S S ℂ) (i j : S) :
    (∑ a, pinching a X) i j = if i = j then X i j else 0 := by
  rw [Matrix.sum_apply]
  simp only [pinching_apply]
  by_cases hij : i = j
  · subst hij
    simp
  · have : ∀ a, ¬ (i = a ∧ j = a) := fun a ⟨h1, h2⟩ => hij (h1.trans h2.symm)
    simp [this, hij]

/-- **The pinching instrument is not passive on the full algebra** once there are two atoms: the
matrix unit `E_{st}`, `s ≠ t`, is sent to zero. So N2's passivity is the commutative algebra's, and
the full algebra is exactly where N1 applies. -/
theorem pinching_not_passive (hS : 1 < Fintype.card S) :
    ¬ IsPassiveInstrument (pinching (S := S)) := by
  intro h
  obtain ⟨s, t, hst⟩ := Fintype.exists_pair_of_one_lt_card hS
  have hX := congrFun (congrFun (congrArg (fun Φ => Φ (Matrix.single s t (1 : ℂ))) h.2) s) t
  simp only [LinearMap.id_apply] at hX
  rw [LinearMap.sum_apply, pinching_sum_apply, if_neg hst] at hX
  simp [Matrix.single] at hX

end N2

#print axioms psd_summand_of_rankOne
#print axioms choiMatrix_id
#print axioms passive_branch_scalar
#print axioms passive_outcome_state_independent
#print axioms no_complete_passive_observation
#print axioms pinching_cp
#print axioms pinching_passive_on_diagonal
#print axioms pinching_separates_diagonal
#print axioms pinching_sum_apply
#print axioms pinching_not_passive

end PassiveObservation
end OIBridge
