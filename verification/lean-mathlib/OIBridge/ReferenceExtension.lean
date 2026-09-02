/-
  OIBridge/ReferenceExtension.lean — the dimensional threshold is a theorem, and composite
  unitary control does not give parallel reference extension.

  ROUND THIRTY-FIVE, PART TWO. Round thirty-four showed that exact system QM plus every
  composite unitary does not force composite quantum soundness. "More control" is formally
  dead as the missing condition. This round makes the reference dimension itself a kernel
  object and identifies, as a PROPERTY of `FiniteOperationalTheory` and not a new structure
  field, the compositional principle the countermodel lacks.

  §A — GENERIC REFERENCE AMPLIFICATION.  `amplRef R Φ` is `id_R ⊗ Φ` for an arbitrary finite
  reference `R`, and `IsReferencePositive R Φ` says it carries positive semidefinite inputs
  to positive semidefinite outputs. Round thirty-three's `IsTwoPositive` is the `R = Fin 2`
  specialization, definitionally (`isTwoPositive_iff_referencePositive`), and
  `IsThreePositive` is `R = Fin 3`. Conjugations are reference-positive for every `R`
  (`conjChannel_referencePositive`).

  §B — THE THRESHOLD, KERNELIZED.  `reduction2_not_threePositive`: the rank-three maximally
  entangled input `Σ_{i<3} |i⟩|e_i⟩` gives the amplified form exactly `−3/7`. With round
  thirty-three, `reduction2_threshold`: `Φ₂` is 2-positive and not 3-positive. Round
  thirty-three's probe-only clue is now a theorem. A QUALIFICATION, so it is not misread:
  a qutrit reference detects THIS `Φ₂`; it is not, in general, enough to characterize
  complete positivity of an arbitrary map on a four-level carrier. That is §D's business.

  §C — THE MISSING COMPOSITIONAL PROPERTY.  `withSpectator R e Φ` is `Φ` with an untouched
  finite spectator `R` appended, carried back to the theory's own carriers by an EXPLICIT
  reindexing `e : R × (A × Fin n) ≃ A × Fin m` — the associativity nuisance is an equivalence
  handed in as data, not a cardinality `simp`. `HasParallelReferenceExtension T` says every
  available composite family stays available with any such spectator appended;
  `HasQutritReferenceExtension T` is the one instance the countermodel test needs, with
  `qutritIdx : Fin 3 × (Fin 2 × Fin 2) ≃ Fin 2 × Fin 6` built from `prodAssoc`, `prodComm`
  and `finProdFinEquiv`, keeping the system qubit in the system slot (`qutritIdx_apply`).
  Then:

      ┌────────────────────────────────────────────────────────────────────────────┐
      │  `countermodel_not_qutritReferenceExtension`,                               │
      │  `countermodel_not_parallelReferenceExtension`:                             │
      │      the round-34 countermodel violates both;                               │
      │  `control_not_implies_parallelReferenceExtension`:                          │
      │      HasCompositeUnitaryControl ⇏ HasParallelReferenceExtension.            │
      └────────────────────────────────────────────────────────────────────────────┘

  The mechanism is the one round thirty-four exposed: extended availability in the
  countermodel means 2-positivity on the larger carrier, 2-positivity implies plain
  positivity (`positive_of_twoPositive`, by a padding congruence), and the qutrit extension of
  `Φ₂` fails plain positivity on the reindexed rank-three input. Arbitrary control WITHIN a
  carrier is a different thing from the ability to APPEND an untouched spectator.

  §D — THE CHOI-SIZED TARGET, both directions.  `referencePositive_self_cp`: for an
  operation on `S`, reference-positivity against a reference of size `|S|` — here `S`
  itself — forces complete positivity, because `(id_S ⊗ Φ)(|Ω_S⟩⟨Ω_S|)` IS the Choi matrix
  (`choiMatrix_eq_amplRef`). Conversely `cp_referencePositive`: a completely positive map is
  reference-positive against EVERY finite reference, by the Kraus form that round thirty-four's
  now-internal factorization supplies. So `isCompletelyPositive_iff_referencePositive_self`.
  The algebra is free. What is NOT free, and NOT claimed here, is the operational question:
  which closure or preparation rules make the size-`|S|` reference test physically available
  inside `FiniteOperationalTheory`. That is round thirty-six's question.

  NOT CLAIMED, and the lint holds the file to it. No sufficiency: nothing here says exact QM
  plus full control plus qutrit (or any) reference extension implies `KrausSoundExt`; the
  qutrit principle kills the current `Φ₂`, which is not the same as characterizing every
  non-CP map. No structure field is added. `HasParallelReferenceExtension` is not shown to be
  satisfiable by any theory here; only that control does not deliver it.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.BoundaryAudit

namespace OIBridge
namespace ReferenceExtension

open Complex Matrix CoherentExtension MonoidalCompletion
open OperationalAssembly StinespringAssembly KrausSoundness CompositeSoundness
open OperationalRigidity DimensionalObstruction DimensionalCountermodel HiddenCoherence

open scoped ComplexOrder

/-! ### Section A — generic reference amplification -/

section Generic

variable {R S S' : Type*} [Fintype R] [DecidableEq R] [Fintype S] [DecidableEq S]
  [Fintype S'] [DecidableEq S']

/-- The `(i, j)` reference block of a matrix on `R × S`. -/
def refBlockR (M : Matrix (R × S) (R × S) ℂ) (i j : R) : Matrix S S ℂ :=
  Matrix.of fun k l => M (i, k) (j, l)

variable (R) in
/-- **GENERIC REFERENCE AMPLIFICATION** `id_R ⊗ Φ`, for a map between any two carriers. -/
def amplRef (Φ : Matrix S S ℂ →ₗ[ℂ] Matrix S' S' ℂ) (M : Matrix (R × S) (R × S) ℂ) :
    Matrix (R × S') (R × S') ℂ :=
  Matrix.of fun p q => Φ (refBlockR M p.1 q.1) p.2 q.2

variable (R) in
/-- **REFERENCE POSITIVITY**: `id_R ⊗ Φ` carries positive semidefinite matrices to positive
semidefinite matrices — every test whose untouched quantum reference is `R` passes. -/
def IsReferencePositive (Φ : Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ) : Prop :=
  ∀ M : Matrix (R × S) (R × S) ℂ, M.PosSemidef → (amplRef R Φ M).PosSemidef

/-- Round thirty-three's 2-positivity is the `R = Fin 2` case, definitionally. -/
theorem isTwoPositive_iff_referencePositive (Φ : Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ) :
    IsTwoPositive Φ ↔ IsReferencePositive (Fin 2) Φ := Iff.rfl

/-- 3-positivity: a qutrit reference. -/
def IsThreePositive (Φ : Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ) : Prop :=
  IsReferencePositive (Fin 3) Φ

theorem refBlockR_add (M N : Matrix (R × S) (R × S) ℂ) (i j : R) :
    refBlockR (M + N) i j = refBlockR M i j + refBlockR N i j := by
  ext k l
  rfl

theorem refBlockR_smul (c : ℂ) (M : Matrix (R × S) (R × S) ℂ) (i j : R) :
    refBlockR (c • M) i j = c • refBlockR M i j := by
  ext k l
  rfl

theorem amplRef_add (Φ : Matrix S S ℂ →ₗ[ℂ] Matrix S' S' ℂ) (M N : Matrix (R × S) (R × S) ℂ) :
    amplRef R Φ (M + N) = amplRef R Φ M + amplRef R Φ N := by
  ext p q
  simp only [amplRef, Matrix.of_apply, refBlockR_add, map_add, Matrix.add_apply]

theorem amplRef_smul (Φ : Matrix S S ℂ →ₗ[ℂ] Matrix S' S' ℂ) (c : ℂ)
    (M : Matrix (R × S) (R × S) ℂ) : amplRef R Φ (c • M) = c • amplRef R Φ M := by
  ext p q
  simp only [amplRef, Matrix.of_apply, refBlockR_smul, map_smul, Matrix.smul_apply]

variable (R) in
/-- The amplification as a linear map. -/
def amplRefL (Φ : Matrix S S ℂ →ₗ[ℂ] Matrix S' S' ℂ) :
    Matrix (R × S) (R × S) ℂ →ₗ[ℂ] Matrix (R × S') (R × S') ℂ where
  toFun := amplRef R Φ
  map_add' := amplRef_add Φ
  map_smul' c M := amplRef_smul Φ c M

theorem amplRefL_apply (Φ : Matrix S S ℂ →ₗ[ℂ] Matrix S' S' ℂ) (M : Matrix (R × S) (R × S) ℂ) :
    amplRefL R Φ M = amplRef R Φ M := rfl

theorem amplRef_sum_map {ι : Type*} (s : Finset ι) (Φ : ι → Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ)
    (M : Matrix (R × S) (R × S) ℂ) :
    amplRef R (∑ i ∈ s, Φ i) M = ∑ i ∈ s, amplRef R (Φ i) M := by
  ext p q
  simp only [amplRef, Matrix.of_apply, LinearMap.sum_apply, Matrix.sum_apply]

theorem tensor_one_mul_apply' (V : Matrix S S ℂ) (M : Matrix (R × S) (R × S) ℂ) (p q : R × S) :
    (tensorOf (1 : Matrix R R ℂ) V * M) p q = ∑ a, V p.2 a * M (p.1, a) q := by
  simp only [Matrix.mul_apply, tensorOf_apply, Fintype.sum_prod_type, Matrix.one_apply,
    ite_mul, one_mul, zero_mul]
  rw [Finset.sum_eq_single p.1]
  · exact Finset.sum_congr rfl fun a _ => if_pos rfl
  · intro x _ hx
    exact Finset.sum_eq_zero fun a _ => if_neg (Ne.symm hx)
  · intro h
    exact absurd (Finset.mem_univ _) h

theorem mul_tensor_one_conjTranspose_apply' (V : Matrix S S ℂ) (X : Matrix (R × S) (R × S) ℂ)
    (r q : R × S) :
    (X * (tensorOf (1 : Matrix R R ℂ) V)ᴴ) r q = ∑ b, X r (q.1, b) * star (V q.2 b) := by
  simp only [Matrix.mul_apply, Matrix.conjTranspose_apply, tensorOf_apply,
    Fintype.sum_prod_type, Matrix.one_apply, star_mul', star_ite_one_zero]
  rw [Finset.sum_eq_single q.1]
  · exact Finset.sum_congr rfl fun b _ => by rw [if_pos rfl, one_mul]
  · intro x _ hx
    exact Finset.sum_eq_zero fun b _ => by rw [if_neg (Ne.symm hx), zero_mul, mul_zero]
  · intro h
    exact absurd (Finset.mem_univ _) h

/-- Amplified conjugation is conjugation by `1_R ⊗ V`. -/
theorem amplRef_conjChannel (V : Matrix S S ℂ) (M : Matrix (R × S) (R × S) ℂ) :
    amplRef R (conjChannel V) M
      = tensorOf (1 : Matrix R R ℂ) V * M * (tensorOf (1 : Matrix R R ℂ) V)ᴴ := by
  ext ⟨i, k⟩ ⟨j, l⟩
  show (V * refBlockR M i j * Vᴴ) k l = _
  rw [mul_tensor_one_conjTranspose_apply', Matrix.mul_apply]
  refine Finset.sum_congr rfl fun b _ => ?_
  rw [tensor_one_mul_apply', Matrix.mul_apply, Matrix.conjTranspose_apply]
  rfl

variable (R) in
/-- **CONJUGATIONS ARE REFERENCE-POSITIVE FOR EVERY REFERENCE.** -/
theorem conjChannel_referencePositive (V : Matrix S S ℂ) :
    IsReferencePositive R (conjChannel V) := by
  intro M hM
  rw [amplRef_conjChannel]
  exact hM.mul_mul_conjTranspose_same _

/-- The reference marginal `tr_S M`, for any reference. -/
def refMarginalR (M : Matrix (R × S) (R × S) ℂ) : Matrix R R ℂ :=
  Matrix.of fun i j => ∑ m, M (i, m) (j, m)

/-- The amplified reduction map, for any reference. -/
theorem amplRef_reduction2 (M : Matrix (R × S) (R × S) ℂ) :
    amplRef R (reduction2 S) M
      = (7 : ℂ)⁻¹ • ((2 : ℂ) • tensorOf (refMarginalR M) (1 : Matrix S S ℂ) - M) := by
  ext p q
  obtain ⟨i, k⟩ := p
  obtain ⟨j, l⟩ := q
  simp only [amplRef, Matrix.of_apply, reduction2_apply, Matrix.smul_apply, Matrix.sub_apply,
    smul_eq_mul, tensorOf_apply, refMarginalR, refBlockR, Matrix.trace, Matrix.diag_apply]
  ring

/-- The reference blocks of `|Ω_S⟩⟨Ω_S|` are the matrix units, on any carrier. -/
theorem refBlockR_maxEnt (i j : S) :
    refBlockR (Matrix.vecMulVec (maxEntVec (S := S)) (star maxEntVec)) i j
      = Matrix.single i j 1 := by
  ext k l
  simp only [refBlockR, Matrix.of_apply, Matrix.vecMulVec_apply, Pi.star_apply, maxEntVec,
    single_entry]
  by_cases h1 : i = k <;> by_cases h2 : j = l <;> simp [h1, h2]

/-- **THE CHOI IDENTITY, ANY CARRIER**: `J(Φ) = (id_S ⊗ Φ)(|Ω_S⟩⟨Ω_S|)`. -/
theorem choiMatrix_eq_amplRef (Φ : Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ) :
    choiMatrix Φ = amplRef S Φ (Matrix.vecMulVec maxEntVec (star maxEntVec)) := by
  ext p q
  show Φ (Matrix.single p.1 q.1 1) p.2 q.2 = Φ (refBlockR _ p.1 q.1) p.2 q.2
  rw [refBlockR_maxEnt]

/-- **A REFERENCE OF THE CARRIER'S OWN SIZE FORCES CP**: reference-positivity against `S`
itself is complete positivity, because the amplified maximally entangled input IS the Choi
matrix. -/
theorem referencePositive_self_cp (Φ : Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ)
    (h : IsReferencePositive S Φ) : IsCompletelyPositive Φ := by
  show (choiMatrix Φ).PosSemidef
  rw [choiMatrix_eq_amplRef]
  exact h _ (Matrix.posSemidef_vecMulVec_self_star _)

variable (R) in
/-- **CP IS STABLE AGAINST EVERY REFERENCE**, by the Kraus form the now-internal factorization
supplies. -/
theorem cp_referencePositive (Φ : Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ)
    (h : IsCompletelyPositive Φ) : IsReferencePositive R Φ := by
  have h' : (choiMatrix Φ).PosSemidef := h
  obtain ⟨B, hB⟩ := BoundaryAudit.psdFactorization_discharged (S × S) _ h'
  rw [kraus_of_choi_factor Φ B hB]
  intro M hM
  rw [amplRef_sum_map]
  exact CompositeSoundness.posSemidef_sum _ _ fun i _ => conjChannel_referencePositive R _ M hM

/-- **THE CHOI-SIZED TARGET, both directions.** -/
theorem isCompletelyPositive_iff_referencePositive_self (Φ : Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ) :
    IsCompletelyPositive Φ ↔ IsReferencePositive S Φ :=
  ⟨cp_referencePositive S Φ, referencePositive_self_cp Φ⟩

end Generic

/-! ### Section B — the threshold: `Φ₂` is 2-positive and not 3-positive -/

section Threshold

/-- Three of the four levels of the two-qubit composite. -/
def emb3 : Fin 3 → Fin 2 × Fin 2 := ![(0, 0), (0, 1), (1, 0)]

theorem emb3_injective : Function.Injective emb3 := by decide

/-- The rank-three maximally entangled vector `Σ_{i<3} |i⟩|e_i⟩` on `Fin 3 × (Fin 2 × Fin 2)`. -/
def maxEnt3 : Fin 3 × (Fin 2 × Fin 2) → ℂ := fun p => if emb3 p.1 = p.2 then 1 else 0

theorem maxEnt3_star : star maxEnt3 = maxEnt3 := by
  funext p
  simp only [Pi.star_apply, maxEnt3]
  split_ifs <;> simp

theorem maxEnt3_norm : star maxEnt3 ⬝ᵥ maxEnt3 = 3 := by
  rw [maxEnt3_star]
  have hterm : ∀ p : Fin 3 × (Fin 2 × Fin 2),
      maxEnt3 p * maxEnt3 p = if emb3 p.1 = p.2 then (1 : ℂ) else 0 := by
    intro p
    simp only [maxEnt3]
    split_ifs <;> simp
  simp only [dotProduct, hterm, Fintype.sum_prod_type, Finset.sum_ite_eq, Finset.mem_univ,
    if_true, Finset.sum_const, Finset.card_univ, Fintype.card_fin, nsmul_eq_mul, mul_one]
  norm_num

/-- Its reference marginal is the identity: the three levels are distinct. -/
theorem refMarginalR_maxEnt3 :
    refMarginalR (Matrix.vecMulVec maxEnt3 (star maxEnt3)) = 1 := by
  ext i j
  rw [maxEnt3_star]
  simp only [refMarginalR, Matrix.of_apply, Matrix.vecMulVec_apply, maxEnt3]
  rw [Finset.sum_eq_single (emb3 i)]
  · rw [if_pos rfl, one_mul, Matrix.one_apply]
    by_cases h : i = j
    · rw [if_pos (by rw [h]), if_pos h]
    · rw [if_neg (fun hh => h (emb3_injective hh).symm), if_neg h]
  · intro m _ hm
    rw [if_neg (Ne.symm hm), zero_mul]
  · intro h
    exact absurd (Finset.mem_univ _) h

theorem tensorOf_one_one {R S : Type*} [Fintype R] [DecidableEq R] [Fintype S] [DecidableEq S] :
    tensorOf (1 : Matrix R R ℂ) (1 : Matrix S S ℂ) = 1 := by
  ext ⟨i, k⟩ ⟨j, l⟩
  simp only [tensorOf_apply, Matrix.one_apply, Prod.mk.injEq, ite_and_one_zero]

/-- The qutrit amplification of `Φ₂` on the rank-three input. -/
theorem amplRef_reduction2_maxEnt3 :
    amplRef (Fin 3) (reduction2 (Fin 2 × Fin 2)) (Matrix.vecMulVec maxEnt3 (star maxEnt3))
      = (7 : ℂ)⁻¹ • ((2 : ℂ) • (1 : Matrix (Fin 3 × (Fin 2 × Fin 2)) (Fin 3 × (Fin 2 × Fin 2)) ℂ)
          - Matrix.vecMulVec maxEnt3 (star maxEnt3)) := by
  rw [amplRef_reduction2, refMarginalR_maxEnt3, tensorOf_one_one]

/-- **THE QUTRIT WITNESS**: exactly `−3/7`. -/
theorem amplRef_reduction2_maxEnt3_form :
    star maxEnt3 ⬝ᵥ (amplRef (Fin 3) (reduction2 (Fin 2 × Fin 2))
      (Matrix.vecMulVec maxEnt3 (star maxEnt3)) *ᵥ maxEnt3) = -3 / 7 := by
  have hN := maxEnt3_norm
  rw [amplRef_reduction2_maxEnt3, Matrix.smul_mulVec, Matrix.sub_mulVec, Matrix.smul_mulVec,
    Matrix.one_mulVec, vecMulVec_mulVec', dotProduct_smul, dotProduct_sub, dotProduct_smul,
    dotProduct_smul, hN, smul_eq_mul, smul_eq_mul, smul_eq_mul]
  ring

theorem amplRef_reduction2_maxEnt3_not_posSemidef :
    ¬ (amplRef (Fin 3) (reduction2 (Fin 2 × Fin 2))
        (Matrix.vecMulVec maxEnt3 (star maxEnt3))).PosSemidef := by
  intro h
  have hq := h.dotProduct_mulVec_nonneg maxEnt3
  rw [amplRef_reduction2_maxEnt3_form] at hq
  have hcast : ((-3 / 7 : ℝ) : ℂ) = -3 / 7 := by push_cast; ring
  rw [← hcast, ← Complex.ofReal_zero, Complex.real_le_real] at hq
  norm_num at hq

/-- **Φ₂ IS NOT 3-POSITIVE.** -/
theorem reduction2_not_threePositive : ¬ IsThreePositive (reduction2 (Fin 2 × Fin 2)) :=
  fun h => amplRef_reduction2_maxEnt3_not_posSemidef
    (h _ (Matrix.posSemidef_vecMulVec_self_star _))

/-- **THE DIMENSIONAL THRESHOLD, AS A THEOREM**: 2-positive, not 3-positive. -/
theorem reduction2_threshold :
    IsTwoPositive (reduction2 (Fin 2 × Fin 2)) ∧ ¬ IsThreePositive (reduction2 (Fin 2 × Fin 2)) :=
  ⟨reduction2_twoPositive, reduction2_not_threePositive⟩

end Threshold

/-! ### Section C — 2-positivity gives positivity; parallel reference extension -/

section Padding

variable {S : Type*} [Fintype S] [DecidableEq S]

/-- The embedding of `S` into the `0` reference slot of `Fin 2 × S`. -/
def padEmbed (S : Type*) [Fintype S] [DecidableEq S] : Matrix (Fin 2 × S) S ℂ :=
  Matrix.of fun p k => if p.1 = 0 ∧ p.2 = k then 1 else 0

theorem padEmbed_apply (p : Fin 2 × S) (k : S) :
    padEmbed S p k = if p.1 = 0 ∧ p.2 = k then 1 else 0 := rfl

theorem padEmbed_conjTranspose_apply (k : S) (p : Fin 2 × S) :
    (padEmbed S)ᴴ k p = if p.1 = 0 ∧ p.2 = k then 1 else 0 := by
  rw [Matrix.conjTranspose_apply, padEmbed_apply, star_ite_one_zero]

theorem padEmbed_mul_apply (M : Matrix S S ℂ) (p : Fin 2 × S) (b : S) :
    (padEmbed S * M) p b = if p.1 = 0 then M p.2 b else 0 := by
  simp only [Matrix.mul_apply, padEmbed_apply, ite_and, ite_mul, one_mul, zero_mul]
  by_cases h : p.1 = 0
  · simp [h]
  · simp [h]

theorem mul_padEmbed_conjTranspose_apply (X : Matrix (Fin 2 × S) S ℂ) (r q : Fin 2 × S) :
    (X * (padEmbed S)ᴴ) r q = if q.1 = 0 then X r q.2 else 0 := by
  simp only [Matrix.mul_apply, padEmbed_conjTranspose_apply, ite_and, mul_ite, mul_one,
    mul_zero]
  by_cases h : q.1 = 0
  · simp [h]
  · simp [h]

theorem sum_sum_ite_eq' {α β γ : Type*} [Fintype α] [Fintype β] [DecidableEq α] [DecidableEq β]
    [AddCommMonoid γ] (i : α) (k : β) (g : α → β → γ) :
    (∑ x, ∑ y, if x = i then (if y = k then g x y else 0) else 0) = g i k := by
  rw [Finset.sum_eq_single i]
  · rw [Finset.sum_eq_single k]
    · rw [if_pos rfl, if_pos rfl]
    · intro y _ hy
      rw [if_pos rfl, if_neg hy]
    · intro h
      exact absurd (Finset.mem_univ _) h
  · intro x _ hx
    exact Finset.sum_eq_zero fun y _ => if_neg hx
  · intro h
    exact absurd (Finset.mem_univ _) h

theorem padEmbed_conjTranspose_mul_apply (N : Matrix (Fin 2 × S) (Fin 2 × S) ℂ) (k : S)
    (q : Fin 2 × S) : ((padEmbed S)ᴴ * N) k q = N (0, k) q := by
  simp only [Matrix.mul_apply, padEmbed_conjTranspose_apply, Fintype.sum_prod_type, ite_and,
    ite_mul, one_mul, zero_mul]
  exact sum_sum_ite_eq' 0 k fun x y => N (x, y) q

theorem mul_padEmbed_apply (X : Matrix S (Fin 2 × S) ℂ) (a : S) (l : S) :
    (X * padEmbed S) a l = X a (0, l) := by
  simp only [Matrix.mul_apply, padEmbed_apply, Fintype.sum_prod_type, ite_and, mul_ite,
    mul_one, mul_zero]
  exact sum_sum_ite_eq' 0 l fun x y => X a (x, y)

theorem refBlock_pad (M : Matrix S S ℂ) :
    refBlock (padEmbed S * M * (padEmbed S)ᴴ) 0 0 = M := by
  ext k l
  show (padEmbed S * M * (padEmbed S)ᴴ) (0, k) (0, l) = M k l
  rw [mul_padEmbed_conjTranspose_apply, if_pos rfl, padEmbed_mul_apply, if_pos rfl]

/-- A map's action is a corner of its qubit amplification: `Ψ M = Eᴴ (id₂ ⊗ Ψ)(E M Eᴴ) E`. -/
theorem apply_eq_pad_ampl2 (Ψ : Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ) (M : Matrix S S ℂ) :
    Ψ M = (padEmbed S)ᴴ * ampl2 Ψ (padEmbed S * M * (padEmbed S)ᴴ) * padEmbed S := by
  ext k l
  rw [mul_padEmbed_apply, padEmbed_conjTranspose_mul_apply]
  show Ψ M k l = Ψ (refBlock (padEmbed S * M * (padEmbed S)ᴴ) 0 0) k l
  rw [refBlock_pad]

/-- **2-POSITIVE IMPLIES POSITIVE**, by the padding congruence. -/
theorem positive_of_twoPositive {Ψ : Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ} (h : IsTwoPositive Ψ)
    {M : Matrix S S ℂ} (hM : M.PosSemidef) : (Ψ M).PosSemidef := by
  rw [apply_eq_pad_ampl2]
  exact (h _ (hM.mul_mul_conjTranspose_same _)).conjTranspose_mul_mul_same _

end Padding

section Spectator

variable {A : Type*} [Fintype A] [DecidableEq A]

/-- **AN OPERATION WITH AN UNTOUCHED SPECTATOR APPENDED**, carried back to the theory's own
carriers by an explicit reindexing `e`. -/
def withSpectator (R : Type*) [Fintype R] [DecidableEq R] {n m : ℕ}
    (e : R × (A × Fin n) ≃ A × Fin m)
    (Φ : Matrix (A × Fin n) (A × Fin n) ℂ →ₗ[ℂ] Matrix (A × Fin n) (A × Fin n) ℂ) :
    Matrix (A × Fin m) (A × Fin m) ℂ →ₗ[ℂ] Matrix (A × Fin m) (A × Fin m) ℂ :=
  (Matrix.reindexLinearEquiv ℂ ℂ e e).toLinearMap ∘ₗ amplRefL R Φ
    ∘ₗ (Matrix.reindexLinearEquiv ℂ ℂ e.symm e.symm).toLinearMap

theorem withSpectator_apply (R : Type*) [Fintype R] [DecidableEq R] {n m : ℕ}
    (e : R × (A × Fin n) ≃ A × Fin m)
    (Φ : Matrix (A × Fin n) (A × Fin n) ℂ →ₗ[ℂ] Matrix (A × Fin n) (A × Fin n) ℂ)
    (N : Matrix (A × Fin m) (A × Fin m) ℂ) :
    withSpectator R e Φ N = Matrix.reindex e e (amplRef R Φ (Matrix.reindex e.symm e.symm N)) :=
  rfl

/-- On a reindexed input the spectator extension is the reindexed amplification. -/
theorem withSpectator_reindex (R : Type*) [Fintype R] [DecidableEq R] {n m : ℕ}
    (e : R × (A × Fin n) ≃ A × Fin m)
    (Φ : Matrix (A × Fin n) (A × Fin n) ℂ →ₗ[ℂ] Matrix (A × Fin n) (A × Fin n) ℂ)
    (X : Matrix (R × (A × Fin n)) (R × (A × Fin n)) ℂ) :
    withSpectator R e Φ (Matrix.reindex e e X) = Matrix.reindex e e (amplRef R Φ X) := by
  rw [withSpectator_apply, ← Matrix.reindex_symm, Equiv.symm_apply_apply]

/-- **PARALLEL REFERENCE EXTENSION**, as a property of a theory and not a structure field:
every available composite family stays available with any untouched finite spectator
appended, after the explicit reindexing. -/
def HasParallelReferenceExtension (T : FiniteOperationalTheory A) : Prop :=
  ∀ (R : Type) [Fintype R] [DecidableEq R] (n m : ℕ) (e : R × (A × Fin n) ≃ A × Fin m)
    (O : Type) [Fintype O] [DecidableEq O]
    (F : O → Matrix (A × Fin n) (A × Fin n) ℂ →ₗ[ℂ] Matrix (A × Fin n) (A × Fin n) ℂ),
    T.availExt n O F → T.availExt m O (fun a => withSpectator R e (F a))

end Spectator

/-- The explicit reindexing `Fin 3 × (Fin 2 × Fin 2) ≃ Fin 2 × Fin 6`: associate, move the
spectator past the SYSTEM qubit (which stays in the system slot), re-associate, and pack the
spectator with the ancilla qubit into `Fin 6`. -/
def qutritIdx : Fin 3 × (Fin 2 × Fin 2) ≃ Fin 2 × Fin 6 :=
  (Equiv.prodAssoc _ _ _).symm.trans
    ((Equiv.prodCongr (Equiv.prodComm _ _) (Equiv.refl _)).trans
      ((Equiv.prodAssoc _ _ _).trans (Equiv.prodCongr (Equiv.refl _) finProdFinEquiv)))

/-- The system index is preserved by the reindexing; the spectator and ancilla are packed. -/
theorem qutritIdx_apply (r : Fin 3) (a e : Fin 2) :
    qutritIdx (r, (a, e)) = (a, finProdFinEquiv (r, e)) := rfl

/-- **QUTRIT REFERENCE EXTENSION** on the two-qubit operations: the one instance the
countermodel test needs. -/
def HasQutritReferenceExtension (T : FiniteOperationalTheory (Fin 2)) : Prop :=
  ∀ (O : Type) [Fintype O] [DecidableEq O]
    (F : O → Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ →ₗ[ℂ] Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ),
    T.availExt 2 O F → T.availExt 6 O (fun a => withSpectator (Fin 3) qutritIdx (F a))

theorem qutrit_of_parallel (T : FiniteOperationalTheory (Fin 2))
    (h : HasParallelReferenceExtension T) : HasQutritReferenceExtension T :=
  fun O _ _ F hF => h (Fin 3) 2 6 qutritIdx O F hF

theorem posSemidef_of_reindex {m n : Type*} [Fintype m] [Fintype n] (e : m ≃ n)
    {Y : Matrix m m ℂ} (h : (Matrix.reindex e e Y).PosSemidef) : Y.PosSemidef := by
  have := h.submatrix e
  rwa [Matrix.reindex_apply, Matrix.submatrix_submatrix, Equiv.symm_comp_self,
    Matrix.submatrix_id_id] at this

theorem posSemidef_reindex {m n : Type*} [Fintype m] [Fintype n] (e : m ≃ n)
    {Y : Matrix m m ℂ} (h : Y.PosSemidef) : (Matrix.reindex e e Y).PosSemidef := by
  rw [Matrix.reindex_apply]
  exact h.submatrix _

/-- **THE ROUND-34 COUNTERMODEL HAS NO QUTRIT REFERENCE EXTENSION.** Its available `Φ₂`,
extended by an untouched qutrit, would have to be 2-positive, hence positive, on the larger
carrier; on the reindexed rank-three input it is not. -/
theorem countermodel_not_qutritReferenceExtension :
    ¬ HasQutritReferenceExtension countermodel := by
  intro h
  obtain ⟨h2, -⟩ := h Unit (fun _ => reduction2 (Fin 2 × Fin 2)) countermodel_reduction2_available
  have hpos := positive_of_twoPositive (h2 ())
    (posSemidef_reindex qutritIdx (Matrix.posSemidef_vecMulVec_self_star maxEnt3))
  rw [withSpectator_reindex] at hpos
  exact amplRef_reduction2_maxEnt3_not_posSemidef (posSemidef_of_reindex qutritIdx hpos)

theorem countermodel_not_parallelReferenceExtension :
    ¬ HasParallelReferenceExtension countermodel :=
  fun h => countermodel_not_qutritReferenceExtension (qutrit_of_parallel _ h)

/-- **CONTROL DOES NOT GIVE REFERENCE EXTENSION.** Arbitrary unitary control within a carrier
is a different thing from the ability to append an untouched spectator. -/
theorem control_not_implies_parallelReferenceExtension :
    ∃ T : FiniteOperationalTheory (Fin 2),
      HasCompositeUnitaryControl T ∧ ¬ HasParallelReferenceExtension T :=
  ⟨countermodel, countermodel_control, countermodel_not_parallelReferenceExtension⟩

/-- The same with exactness on the system, for the qutrit instance. -/
theorem exactControl_not_implies_qutritReferenceExtension :
    ∃ T : FiniteOperationalTheory (Fin 2),
      ExactFiniteEndomorphicQuantumOps T ∧ HasCompositeUnitaryControl T
        ∧ ¬ HasQutritReferenceExtension T :=
  ⟨countermodel, countermodel_exact, countermodel_control,
    countermodel_not_qutritReferenceExtension⟩

#print axioms isTwoPositive_iff_referencePositive
#print axioms amplRef_sum_map
#print axioms amplRef_conjChannel
#print axioms conjChannel_referencePositive
#print axioms amplRef_reduction2
#print axioms choiMatrix_eq_amplRef
#print axioms referencePositive_self_cp
#print axioms cp_referencePositive
#print axioms isCompletelyPositive_iff_referencePositive_self
#print axioms emb3_injective
#print axioms maxEnt3_norm
#print axioms refMarginalR_maxEnt3
#print axioms tensorOf_one_one
#print axioms amplRef_reduction2_maxEnt3
#print axioms amplRef_reduction2_maxEnt3_form
#print axioms amplRef_reduction2_maxEnt3_not_posSemidef
#print axioms reduction2_not_threePositive
#print axioms reduction2_threshold
#print axioms refBlock_pad
#print axioms apply_eq_pad_ampl2
#print axioms positive_of_twoPositive
#print axioms withSpectator_reindex
#print axioms qutrit_of_parallel
#print axioms qutritIdx_apply
#print axioms posSemidef_of_reindex
#print axioms posSemidef_reindex
#print axioms countermodel_not_qutritReferenceExtension
#print axioms countermodel_not_parallelReferenceExtension
#print axioms control_not_implies_parallelReferenceExtension
#print axioms exactControl_not_implies_qutritReferenceExtension

end ReferenceExtension
end OIBridge
