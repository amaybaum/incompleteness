/-
  OIBridge/DimensionalCountermodel.lean — exact system QM plus full composite unitary
  control does not force composite quantum soundness.

  PHASE THREE, ROUND THIRTY-FOUR. Round thirty-three established the mathematics: on the
  two-qubit composite there is a trace-preserving, unital, 2-positive map `Φ₂` that is not
  completely positive. This round builds the operational theory around it.

      ┌──────────────────────────────────────────────────────────────────────────────┐
      │  `exactControl_not_implies_krausSoundExt`:                                    │
      │  ∃ T : FiniteOperationalTheory (Fin 2),                                       │
      │      ExactFiniteEndomorphicQuantumOps T ∧ HasCompositeUnitaryControl T        │
      │        ∧ ¬ KrausSoundExt T.                                                    │
      └──────────────────────────────────────────────────────────────────────────────┘

  Round twenty-eight's countermodel had to WITHHOLD composite unitary control. This one grants
  every composite unitary and is still not composite-sound. The missing condition is
  therefore not control richness.

  THE COMPOSITE SECTOR (`IsTwoPositiveInstrument`): every branch is 2-positive and the
  family preserves the trace in aggregate. It is closed under everything the structure needs:
  coarse-graining (sums of 2-positive maps are 2-positive), feed-forward (compositions are
  2-positive), every unitary channel (a congruence), and the native Lüders readout (a
  diagonal compression). `Φ₂` belongs to it; so does every composite unitary, and by round
  thirty-three's covariance no amount of control rotates the surplus away.

  THE KEY LEMMA (`twoPositive_qubit_cp`): a 2-positive map ON A QUBIT is completely
  positive. Its Choi matrix is `(id₂ ⊗ Φ)(|Ω₂⟩⟨Ω₂|)`, that input is positive semidefinite,
  and 2-positivity does the rest — no factorization, no classification. This is why the
  theory stays exactly quantum whenever a composite process is squeezed back through the
  visible qubit.

  PREPARATIONS (`RefTestedPrep`): trace preserving, and positive semidefinite on the qubit
  Choi input under amplification. Uniform attachment satisfies it; post-composition by an
  available deterministic map preserves it; an available branch keeps the amplified Choi
  state positive; the partial trace keeps it positive; so the discarded qubit branch has a
  positive Choi matrix and is completely positive. The reindexing between
  `Fin 2 × (Fin 2 × Fin n)` and `(Fin 2 × Fin 2) × Fin n` is done by an explicit embedding
  matrix `ancEmbed` and two congruences, not buried in `simp`.

  THE ONE EXTERNAL STEP, ISOLATED. `IsKrausFamily` is representation-level. Passing from
  "completely positive, trace preserving in aggregate" to a normalized Kraus family is where
  finite PSD factorization enters, and it is stated as the explicit hypothesis
  `PSDFactorization (Fin 2 × Fin 2)` — a specialization of boundary item 3, the same
  factorization `Purification.lean` isolates. Nothing new is added to the external boundary.
  The architecture is therefore

      countermodel structure and all 2-positive closure   — kernel-internal,
      2-positive qubit ⟹ CP                                 — kernel-internal,
      CP instrument ⟹ Kraus representation                  — boundary item 3 only,

  and the conditional capstone is `countermodel_of_factorization`.

  THE HYPOTHESIS IS ALSO DISCHARGED, LOUDLY. `psdFactorization_of_spectral` proves
  `PSDFactorization` for every finite carrier from the rank-one spectral resolution
  (Mathlib's spectral theorem, kernel-internal since the Kadison round) and the real square
  root of the eigenvalues — the same two ingredients `scalarAvail_isKraus` already used. That
  gives the unconditional `countermodel` and `exactControl_not_implies_krausSoundExt`. THIS
  DOES NOT RETIRE BOUNDARY ITEM 3: the boundary ledger is unchanged here, `Purification.lean`
  still isolates the factorization as a hypothesis, and whether the item should now be
  reclassified is a separate boundary audit, not something this file decides.

  WHAT THIS ROUND DOES NOT DO. It does not identify the principle that WOULD force composite
  soundness; it shows control is not it. The probe records, without kernelizing, that a
  qutrit reference already detects `Φ₂`, which points at a reference-extension or
  parallel-composition principle for the next round. That principle is not added here.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.DimensionalObstruction
import OIBridge.HiddenCoherence

namespace OIBridge
namespace DimensionalCountermodel

open Complex Matrix CoherentExtension MonoidalCompletion
open OperationalAssembly StinespringAssembly KrausSoundness CompositeSoundness
open OperationalRigidity DimensionalObstruction HiddenCoherence AncillaInterference
open FactorExchange

open scoped ComplexOrder

/-! ### Section A — the rectangular amplification and the qubit Choi identity -/

section Amplification

variable {S S' S'' : Type*} [Fintype S] [DecidableEq S] [Fintype S'] [DecidableEq S']
  [Fintype S''] [DecidableEq S'']

/-- `id₂ ⊗ Φ` for a map between different carriers. -/
def amplR (Φ : Matrix S S ℂ →ₗ[ℂ] Matrix S' S' ℂ) (M : Matrix (Fin 2 × S) (Fin 2 × S) ℂ) :
    Matrix (Fin 2 × S') (Fin 2 × S') ℂ :=
  Matrix.of fun p q => Φ (refBlock M p.1 q.1) p.2 q.2

theorem amplR_eq_ampl2 (Φ : Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ)
    (M : Matrix (Fin 2 × S) (Fin 2 × S) ℂ) : amplR Φ M = ampl2 Φ M := rfl

theorem refBlock_amplR (Φ : Matrix S S ℂ →ₗ[ℂ] Matrix S' S' ℂ)
    (M : Matrix (Fin 2 × S) (Fin 2 × S) ℂ) (i j : Fin 2) :
    refBlock (amplR Φ M) i j = Φ (refBlock M i j) := by
  ext k l
  rfl

/-- **AMPLIFICATION IS FUNCTORIAL**: `id₂ ⊗ (Φ ∘ Ψ) = (id₂ ⊗ Φ) ∘ (id₂ ⊗ Ψ)`. -/
theorem amplR_comp (Φ : Matrix S' S' ℂ →ₗ[ℂ] Matrix S'' S'' ℂ)
    (Ψ : Matrix S S ℂ →ₗ[ℂ] Matrix S' S' ℂ) (M : Matrix (Fin 2 × S) (Fin 2 × S) ℂ) :
    amplR (Φ.comp Ψ) M = amplR Φ (amplR Ψ M) := by
  ext p q
  show Φ (Ψ (refBlock M p.1 q.1)) p.2 q.2 = Φ (refBlock (amplR Ψ M) p.1 q.1) p.2 q.2
  rw [refBlock_amplR]

theorem ampl2_sum_map {ι : Type*} (s : Finset ι) (Φ : ι → Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ)
    (M : Matrix (Fin 2 × S) (Fin 2 × S) ℂ) :
    ampl2 (∑ i ∈ s, Φ i) M = ∑ i ∈ s, ampl2 (Φ i) M := by
  ext p q
  simp only [ampl2, Matrix.of_apply, LinearMap.sum_apply, Matrix.sum_apply]

/-- The reference blocks of `|Ω₂⟩⟨Ω₂|` are exactly the matrix units. -/
theorem refBlock_maxEnt (i j : Fin 2) :
    refBlock (Matrix.vecMulVec (maxEntVec (S := Fin 2)) (star maxEntVec)) i j
      = Matrix.single i j 1 := by
  ext k l
  simp only [refBlock, Matrix.of_apply, Matrix.vecMulVec_apply, Pi.star_apply, maxEntVec,
    single_entry]
  by_cases h1 : i = k <;> by_cases h2 : j = l <;> simp [h1, h2]

/-- **THE QUBIT CHOI IDENTITY**: `J(Φ) = (id₂ ⊗ Φ)(|Ω₂⟩⟨Ω₂|)`. -/
theorem choiMatrix_eq_ampl2 (Φ : Matrix (Fin 2) (Fin 2) ℂ →ₗ[ℂ] Matrix (Fin 2) (Fin 2) ℂ) :
    choiMatrix Φ = ampl2 Φ (Matrix.vecMulVec maxEntVec (star maxEntVec)) := by
  ext p q
  show Φ (Matrix.single p.1 q.1 1) p.2 q.2 = Φ (refBlock _ p.1 q.1) p.2 q.2
  rw [refBlock_maxEnt]

/-- **THE KEY LEMMA: A 2-POSITIVE MAP ON A QUBIT IS COMPLETELY POSITIVE.** Its Choi matrix
is the amplification of a positive semidefinite input. No factorization, no classification. -/
theorem twoPositive_qubit_cp (Φ : Matrix (Fin 2) (Fin 2) ℂ →ₗ[ℂ] Matrix (Fin 2) (Fin 2) ℂ)
    (h : IsTwoPositive Φ) : IsCompletelyPositive Φ := by
  show (choiMatrix Φ).PosSemidef
  rw [choiMatrix_eq_ampl2]
  exact h _ (Matrix.posSemidef_vecMulVec_self_star _)

end Amplification

/-! ### Section B — 2-positivity is closed under what the structure needs -/

section Closure

variable {S : Type*} [Fintype S] [DecidableEq S]

theorem isTwoPositive_comp {Φ Ψ : Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ} (hΦ : IsTwoPositive Φ)
    (hΨ : IsTwoPositive Ψ) : IsTwoPositive (Φ.comp Ψ) := by
  intro M hM
  rw [← amplR_eq_ampl2, amplR_comp, amplR_eq_ampl2, amplR_eq_ampl2]
  exact hΦ _ (hΨ _ hM)

theorem isTwoPositive_sum {ι : Type*} (s : Finset ι) (Φ : ι → Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ)
    (h : ∀ i ∈ s, IsTwoPositive (Φ i)) : IsTwoPositive (∑ i ∈ s, Φ i) := by
  intro M hM
  rw [ampl2_sum_map]
  exact CompositeSoundness.posSemidef_sum _ _ fun i hi => h i hi M hM

theorem star_ite_one_zero (c : Prop) [Decidable c] :
    star (if c then (1 : ℂ) else 0) = if c then 1 else 0 := by
  split_ifs <;> simp

theorem tensor_one_mul_apply (V : Matrix S S ℂ) (M : Matrix (Fin 2 × S) (Fin 2 × S) ℂ)
    (p q : Fin 2 × S) :
    (tensorOf (1 : Matrix (Fin 2) (Fin 2) ℂ) V * M) p q = ∑ a, V p.2 a * M (p.1, a) q := by
  simp only [Matrix.mul_apply, tensorOf_apply, Fintype.sum_prod_type, Matrix.one_apply,
    ite_mul, one_mul, zero_mul]
  rw [Finset.sum_eq_single p.1]
  · exact Finset.sum_congr rfl fun a _ => if_pos rfl
  · intro x _ hx
    exact Finset.sum_eq_zero fun a _ => if_neg (Ne.symm hx)
  · intro h
    exact absurd (Finset.mem_univ _) h

theorem mul_tensor_one_conjTranspose_apply (V : Matrix S S ℂ)
    (X : Matrix (Fin 2 × S) (Fin 2 × S) ℂ) (r q : Fin 2 × S) :
    (X * (tensorOf (1 : Matrix (Fin 2) (Fin 2) ℂ) V)ᴴ) r q
      = ∑ b, X r (q.1, b) * star (V q.2 b) := by
  simp only [Matrix.mul_apply, Matrix.conjTranspose_apply, tensorOf_apply,
    Fintype.sum_prod_type, Matrix.one_apply, star_mul', star_ite_one_zero]
  rw [Finset.sum_eq_single q.1]
  · exact Finset.sum_congr rfl fun b _ => by rw [if_pos rfl, one_mul]
  · intro x _ hx
    exact Finset.sum_eq_zero fun b _ => by rw [if_neg (Ne.symm hx), zero_mul, mul_zero]
  · intro h
    exact absurd (Finset.mem_univ _) h

/-- Amplified conjugation is conjugation by `1 ⊗ V`. -/
theorem ampl2_conjChannel (V : Matrix S S ℂ) (M : Matrix (Fin 2 × S) (Fin 2 × S) ℂ) :
    ampl2 (conjChannel V) M
      = tensorOf (1 : Matrix (Fin 2) (Fin 2) ℂ) V * M
          * (tensorOf (1 : Matrix (Fin 2) (Fin 2) ℂ) V)ᴴ := by
  ext ⟨i, k⟩ ⟨j, l⟩
  show (V * refBlock M i j * Vᴴ) k l = _
  rw [mul_tensor_one_conjTranspose_apply, Matrix.mul_apply]
  refine Finset.sum_congr rfl fun b _ => ?_
  rw [tensor_one_mul_apply, Matrix.mul_apply, Matrix.conjTranspose_apply]
  rfl

/-- **EVERY UNITARY CHANNEL IS 2-POSITIVE** (indeed every conjugation is). -/
theorem conjChannel_twoPositive (V : Matrix S S ℂ) : IsTwoPositive (conjChannel V) := by
  intro M hM
  rw [ampl2_conjChannel]
  exact hM.mul_mul_conjTranspose_same _

theorem conjChannel_trace (U : Matrix S S ℂ) (hU : Uᴴ * U = 1) (X : Matrix S S ℂ) :
    (conjChannel U X).trace = X.trace := by
  show (U * X * Uᴴ).trace = _
  rw [Matrix.trace_mul_cycle, hU, Matrix.one_mul]

end Closure

section Readout

variable {A B : Type*} [Fintype A] [DecidableEq A] [Fintype B] [DecidableEq B]

/-- The amplified Lüders readout is a diagonal compression. -/
theorem ampl2_localLuders (k : B) (M : Matrix (Fin 2 × (A × B)) (Fin 2 × (A × B)) ℂ) :
    ampl2 (localLuders (A := A) k) M
      = Matrix.diagonal (fun r : Fin 2 × (A × B) => if r.2.2 = k then (1 : ℂ) else 0) * M
          * (Matrix.diagonal (fun r : Fin 2 × (A × B) => if r.2.2 = k then (1 : ℂ) else 0))ᴴ := by
  ext ⟨i, a, b⟩ ⟨j, c, d⟩
  show localLuders k (refBlock M i j) (a, b) (c, d) = _
  rw [localLuders_apply, Matrix.diagonal_conjTranspose, Matrix.mul_diagonal,
    Matrix.diagonal_mul, Pi.star_apply, star_ite_one_zero]
  simp only [refBlock, Matrix.of_apply]
  by_cases hb : b = k <;> by_cases hd : d = k <;> simp [hb, hd]

/-- **THE NATIVE READOUT IS 2-POSITIVE.** -/
theorem localLuders_twoPositive (k : B) : IsTwoPositive (localLuders (A := A) k) := by
  intro M hM
  rw [ampl2_localLuders]
  exact hM.mul_mul_conjTranspose_same _

/-- **THE READOUT PRESERVES THE TRACE IN AGGREGATE.** -/
theorem localLuders_trace_sum (X : Matrix (A × B) (A × B) ℂ) :
    ∑ k : B, ((localLuders (A := A) k) X).trace = X.trace := by
  simp only [Matrix.trace, Matrix.diag_apply, localLuders_apply, and_self,
    Fintype.sum_prod_type, Finset.sum_ite_eq', Finset.mem_univ, if_true]
  exact Finset.sum_comm

end Readout

/-! ### Section C — the composite sector and the reference-tested preparations -/

section Sector

variable {S : Type*} [Fintype S] [DecidableEq S]

/-- **THE COMPOSITE AVAILABILITY CLASS**: every branch 2-positive, trace preserved in
aggregate. -/
def IsTwoPositiveInstrument {O : Type} [Fintype O] [DecidableEq O]
    (F : O → Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ) : Prop :=
  (∀ a, IsTwoPositive (F a)) ∧ ∀ X, ∑ a, ((F a) X).trace = X.trace

end Sector

section Prep

variable {n : ℕ}

/-- **REFERENCE-TESTED PREPARATIONS**: trace preserving, and positive semidefinite on the
qubit Choi input under amplification. -/
def RefTestedPrep (n : ℕ)
    (P : Matrix (Fin 2) (Fin 2) ℂ →ₗ[ℂ] Matrix (Fin 2 × Fin n) (Fin 2 × Fin n) ℂ) : Prop :=
  (∀ ρ, (P ρ).trace = ρ.trace)
    ∧ (amplR P (Matrix.vecMulVec (maxEntVec (S := Fin 2)) (star maxEntVec))).PosSemidef

/-- The embedding of `Fin 2 × Fin 2` at ancilla level `e` of `Fin 2 × (Fin 2 × Fin n)`. This
is the reindexing between `Fin 2 × (Fin 2 × Fin n)` and `(Fin 2 × Fin 2) × Fin n`, made an
explicit matrix. -/
def ancEmbed (n : ℕ) (e : Fin n) : Matrix (Fin 2 × (Fin 2 × Fin n)) (Fin 2 × Fin 2) ℂ :=
  Matrix.of fun p q => if p = (q.1, (q.2, e)) then 1 else 0

theorem ancEmbed_apply (e : Fin n) (p : Fin 2 × (Fin 2 × Fin n)) (q : Fin 2 × Fin 2) :
    ancEmbed n e p q = if p = (q.1, (q.2, e)) then 1 else 0 := rfl

theorem ancEmbed_conjTranspose_apply (e : Fin n) (q : Fin 2 × Fin 2)
    (p : Fin 2 × (Fin 2 × Fin n)) :
    (ancEmbed n e)ᴴ q p = if p = (q.1, (q.2, e)) then 1 else 0 := by
  rw [Matrix.conjTranspose_apply, ancEmbed_apply, star_ite_one_zero]

theorem sum_sum_ite_eq {α β γ : Type*} [Fintype α] [Fintype β] [DecidableEq α] [DecidableEq β]
    [AddCommMonoid γ] (i : α) (k : β) (g : α → β → γ) :
    (∑ x, ∑ y, if i = x then (if k = y then g x y else 0) else 0) = g i k := by
  rw [Finset.sum_eq_single i]
  · rw [Finset.sum_eq_single k]
    · rw [if_pos rfl, if_pos rfl]
    · intro y _ hy
      rw [if_pos rfl, if_neg (Ne.symm hy)]
    · intro h
      exact absurd (Finset.mem_univ _) h
  · intro x _ hx
    exact Finset.sum_eq_zero fun y _ => if_neg (Ne.symm hx)
  · intro h
    exact absurd (Finset.mem_univ _) h

/-- Left multiplication by the embedding selects the ancilla level. -/
theorem ancEmbed_mul_apply (e : Fin n) (M : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ)
    (p : Fin 2 × (Fin 2 × Fin n)) (b : Fin 2 × Fin 2) :
    (ancEmbed n e * M) p b = if p.2.2 = e then M (p.1, p.2.1) b else 0 := by
  obtain ⟨i, k, f⟩ := p
  simp only [Matrix.mul_apply, ancEmbed_apply, Prod.mk.injEq, Fintype.sum_prod_type,
    ite_and, ite_mul, one_mul, zero_mul]
  exact sum_sum_ite_eq i k fun x y => if f = e then M (x, y) b else 0

theorem mul_ancEmbed_conjTranspose_apply (e : Fin n)
    (X : Matrix (Fin 2 × (Fin 2 × Fin n)) (Fin 2 × Fin 2) ℂ)
    (r : Fin 2 × (Fin 2 × Fin n)) (q : Fin 2 × (Fin 2 × Fin n)) :
    (X * (ancEmbed n e)ᴴ) r q = if q.2.2 = e then X r (q.1, q.2.1) else 0 := by
  obtain ⟨j, l, g⟩ := q
  simp only [Matrix.mul_apply, ancEmbed_conjTranspose_apply, Prod.mk.injEq,
    Fintype.sum_prod_type, ite_and, mul_ite, mul_one, mul_zero]
  exact sum_sum_ite_eq j l fun x y => if g = e then X r (x, y) else 0

theorem ancEmbed_conjTranspose_mul_apply (e : Fin n)
    (N : Matrix (Fin 2 × (Fin 2 × Fin n)) (Fin 2 × (Fin 2 × Fin n)) ℂ) (a : Fin 2 × Fin 2)
    (q : Fin 2 × (Fin 2 × Fin n)) :
    ((ancEmbed n e)ᴴ * N) a q = N (a.1, (a.2, e)) q := by
  simp only [Matrix.mul_apply, ancEmbed_conjTranspose_apply, ite_mul, one_mul, zero_mul,
    Finset.sum_ite_eq', Finset.mem_univ, if_true]

theorem mul_ancEmbed_apply (e : Fin n)
    (X : Matrix (Fin 2 × Fin 2) (Fin 2 × (Fin 2 × Fin n)) ℂ) (a : Fin 2 × Fin 2)
    (b : Fin 2 × Fin 2) :
    (X * ancEmbed n e) a b = X a (b.1, (b.2, e)) := by
  simp only [Matrix.mul_apply, ancEmbed_apply, mul_ite, mul_one, mul_zero,
    Finset.sum_ite_eq', Finset.mem_univ, if_true]

/-- **THE AMPLIFIED PARTIAL TRACE IS A SUM OF CONGRUENCES**, one per ancilla level. -/
theorem amplR_ptraceAncL_eq
    (N : Matrix (Fin 2 × (Fin 2 × Fin n)) (Fin 2 × (Fin 2 × Fin n)) ℂ) :
    amplR (ptraceAncL (A := Fin 2) n) N = ∑ e, (ancEmbed n e)ᴴ * N * ancEmbed n e := by
  ext a b
  show ptraceAnc n (refBlock N a.1 b.1) a.2 b.2 = _
  rw [ptraceAnc_apply, Matrix.sum_apply]
  refine Finset.sum_congr rfl fun e _ => ?_
  rw [mul_ancEmbed_apply, ancEmbed_conjTranspose_mul_apply]
  rfl

/-- **THE AMPLIFIED UNIFORM ATTACHMENT IS A SCALED SUM OF CONGRUENCES.** -/
theorem amplR_uniformAttach_eq (M : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ) :
    amplR (uniformAttach (A := Fin 2) n) M
      = ((n : ℂ))⁻¹ • ∑ e, ancEmbed n e * M * (ancEmbed n e)ᴴ := by
  ext p q
  show uniformAttach n (refBlock M p.1 q.1) p.2 q.2
    = (((n : ℂ))⁻¹ • ∑ e, ancEmbed n e * M * (ancEmbed n e)ᴴ) p q
  rw [Matrix.smul_apply, Matrix.sum_apply, uniformAttach_apply, tensorOf_apply,
    Matrix.smul_apply, Matrix.one_apply,
    Finset.sum_congr rfl fun e _ => mul_ancEmbed_conjTranspose_apply e _ p q]
  simp only [ancEmbed_mul_apply, refBlock, Matrix.of_apply, smul_eq_mul]
  rw [Finset.sum_eq_single q.2.2]
  · rw [if_pos rfl]
    by_cases h : p.2.2 = q.2.2
    · rw [if_pos h, if_pos h]
      ring
    · rw [if_neg h, if_neg h]
      ring
  · intro e _ he
    rw [if_neg (Ne.symm he)]
  · intro he
    exact absurd (Finset.mem_univ _) he

theorem amplR_ptraceAncL_posSemidef
    {N : Matrix (Fin 2 × (Fin 2 × Fin n)) (Fin 2 × (Fin 2 × Fin n)) ℂ} (hN : N.PosSemidef) :
    (amplR (ptraceAncL (A := Fin 2) n) N).PosSemidef := by
  rw [amplR_ptraceAncL_eq]
  exact CompositeSoundness.posSemidef_sum _ _ fun e _ => hN.conjTranspose_mul_mul_same _

theorem natInv_nonneg (n : ℕ) : (0 : ℂ) ≤ ((n : ℂ))⁻¹ := by
  rw [show ((n : ℂ))⁻¹ = (((n : ℝ)⁻¹ : ℝ) : ℂ) by push_cast; rfl]
  exact Complex.zero_le_real.mpr (inv_nonneg.mpr (Nat.cast_nonneg n))

theorem amplR_uniformAttach_posSemidef {M : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ}
    (hM : M.PosSemidef) (n : ℕ) : (amplR (uniformAttach (A := Fin 2) n) M).PosSemidef := by
  rw [amplR_uniformAttach_eq]
  exact (CompositeSoundness.posSemidef_sum _ _ fun e _ => hM.mul_mul_conjTranspose_same _).smul
    (natInv_nonneg n)

theorem uniformAttach_trace {A : Type*} [Fintype A] [DecidableEq A] (n : ℕ) (hn : n ≠ 0)
    (ρ : Matrix A A ℂ) : (uniformAttach n ρ).trace = ρ.trace := by
  have hn' : (n : ℂ) ≠ 0 := Nat.cast_ne_zero.mpr hn
  simp only [Matrix.trace, Matrix.diag_apply, uniformAttach_apply, tensorOf_apply,
    Fintype.sum_prod_type, Matrix.smul_apply, Matrix.one_apply_eq, smul_eq_mul, mul_one,
    Finset.sum_const, Finset.card_univ, Fintype.card_fin, nsmul_eq_mul]
  refine Finset.sum_congr rfl fun s _ => ?_
  rw [mul_comm, mul_assoc, inv_mul_cancel₀ hn', mul_one]

end Prep

/-! ### Section D — the one external step, isolated: CP instrument ⟹ Kraus family -/

section KrausStep

variable {S : Type*} [Fintype S] [DecidableEq S]

/-- **BOUNDARY ITEM 3, stated for the carrier where it is consumed**: every positive
semidefinite matrix factorizes as `B Bᴴ`. -/
def PSDFactorization (R : Type*) [Fintype R] [DecidableEq R] : Prop :=
  ∀ ρ : Matrix R R ℂ, ρ.PosSemidef → ∃ B : Matrix R R ℂ, ρ = B * Bᴴ

/-- The Choi matrix of a conjugation, as a dyad — round twenty-seven's computation, exported. -/
theorem choiMatrix_conjChannel (V : Matrix S S ℂ) :
    choiMatrix (conjChannel V)
      = Matrix.vecMulVec (fun p : S × S => V p.2 p.1) (star fun p : S × S => V p.2 p.1) := by
  ext p q
  show ((V * Matrix.single p.1 q.1 1 * Vᴴ : Matrix S S ℂ)) p.2 q.2 = _
  rw [Matrix.mul_assoc, Matrix.mul_apply, Finset.sum_eq_single p.1]
  · rw [Matrix.mul_apply, Finset.sum_eq_single q.1]
    · rw [single_entry, if_pos ⟨rfl, rfl⟩, one_mul, Matrix.conjTranspose_apply]
      rfl
    · intro y _ hy
      rw [single_entry, if_neg (fun hh => hy hh.2.symm), zero_mul]
    · intro hc
      exact absurd (Finset.mem_univ _) hc
  · intro x _ hx
    rw [Matrix.mul_apply, Finset.sum_eq_zero fun y _ => by
      rw [single_entry, if_neg (fun hh => hx hh.1.symm), zero_mul], mul_zero]
  · intro hc
    exact absurd (Finset.mem_univ _) hc

/-- **THE CHOI MATRIX DETERMINES THE MAP.** -/
theorem choiMatrix_injective {Φ Ψ : Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ}
    (h : choiMatrix Φ = choiMatrix Ψ) : Φ = Ψ := by
  have hunit : ∀ s t : S, Φ (Matrix.single s t 1) = Ψ (Matrix.single s t 1) := by
    intro s t
    ext a b
    exact congrFun (congrFun h (s, a)) (t, b)
  refine LinearMap.ext fun X => ?_
  conv_lhs => rw [Matrix.matrix_eq_sum_single X]
  conv_rhs => rw [Matrix.matrix_eq_sum_single X]
  rw [map_sum, map_sum]
  refine Finset.sum_congr rfl fun s _ => ?_
  rw [map_sum, map_sum]
  refine Finset.sum_congr rfl fun t _ => ?_
  rw [single_eq_smul, map_smul, map_smul, hunit]

/-- **A FACTORIZED CHOI MATRIX GIVES A KRAUS FORM**: the columns of `B` are the Kraus
operators, `K_i(a, s) = B((s, a), i)`. -/
theorem kraus_of_choi_factor (Φ : Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ)
    (B : Matrix (S × S) (S × S) ℂ) (hB : choiMatrix Φ = B * Bᴴ) :
    Φ = ∑ i : S × S, conjChannel (Matrix.of fun a s => B (s, a) i) := by
  apply choiMatrix_injective
  rw [choiMatrix_finsum, hB]
  ext p q
  rw [Matrix.sum_apply, Matrix.mul_apply]
  refine Finset.sum_congr rfl fun i _ => ?_
  rw [choiMatrix_conjChannel, Matrix.vecMulVec_apply, Matrix.conjTranspose_apply,
    Pi.star_apply]
  rfl

/-- **TRACE PRESERVATION IN AGGREGATE IS THE KRAUS NORMALIZATION.** -/
theorem sum_conjTranspose_mul_eq_one_of_trace {ι : Type*} [Fintype ι] (K : ι → Matrix S S ℂ)
    (h : ∀ X : Matrix S S ℂ, ∑ i, (K i * X * (K i)ᴴ).trace = X.trace) :
    ∑ i, (K i)ᴴ * K i = 1 := by
  ext s t
  have hX := h (Matrix.single t s 1)
  have hterm : ∀ i, (K i * Matrix.single t s 1 * (K i)ᴴ).trace = ((K i)ᴴ * K i) s t := by
    intro i
    rw [Matrix.trace_mul_cycle, Matrix.trace_mul_single, MulOpposite.op_one, one_smul]
  rw [Finset.sum_congr rfl fun i _ => hterm i, trace_single_one] at hX
  rw [Matrix.sum_apply, hX, Matrix.one_apply]
  by_cases hst : s = t
  · rw [if_pos hst, if_pos hst.symm]
  · rw [if_neg hst, if_neg (Ne.symm hst)]

/-- **CP INSTRUMENT ⟹ KRAUS FAMILY, against boundary item 3.** A family of completely
positive maps preserving the trace in aggregate has a normalized Kraus representation, given
PSD factorization on the Choi carrier. -/
theorem isKrausFamily_of_cp_of_factorization [Nonempty S] (hfac : PSDFactorization (S × S))
    {O : Type} [Fintype O] [DecidableEq O] (F : O → Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ)
    (hcp : ∀ a, IsCompletelyPositive (F a))
    (htr : ∀ X, ∑ a, ((F a) X).trace = X.trace) : IsKrausFamily F := by
  have hcp' : ∀ a, (choiMatrix (F a)).PosSemidef := hcp
  choose B hB using fun a => hfac _ (hcp' a)
  obtain ⟨K, hK⟩ : ∃ K : O × (S × S) → Matrix S S ℂ,
      ∀ c, K c = Matrix.of fun a s => B c.1 (s, a) c.2 := ⟨_, fun _ => rfl⟩
  have hF : ∀ a, F a = ∑ i : S × S, conjChannel (K (a, i)) := by
    intro a
    rw [kraus_of_choi_factor _ _ (hB a)]
    exact Finset.sum_congr rfl fun i _ => by rw [hK]
  have hne : Nonempty O := by
    by_contra hc
    rw [not_nonempty_iff] at hc
    have h1 := htr 1
    rw [Finset.sum_of_isEmpty, Matrix.trace_one] at h1
    exact absurd h1.symm (Nat.cast_ne_zero.mpr (Fintype.card_ne_zero (α := S)))
  obtain ⟨m, hm⟩ := Nat.exists_eq_succ_of_ne_zero (Fintype.card_ne_zero (α := O × (S × S)))
  let e : Fin (m + 1) ≃ O × (S × S) := (Fintype.equivFinOfCardEq hm).symm
  refine ⟨m, fun k => K (e k), fun k => (e k).1, ?_, ?_⟩
  · rw [Fintype.sum_equiv e (fun k => (K (e k))ᴴ * K (e k)) (fun c => (K c)ᴴ * K c)
      (fun _ => rfl)]
    apply sum_conjTranspose_mul_eq_one_of_trace
    intro X
    rw [Fintype.sum_prod_type, ← htr X]
    refine Finset.sum_congr rfl fun a _ => ?_
    rw [hF a, LinearMap.sum_apply, Matrix.trace_sum]
    exact Finset.sum_congr rfl fun i _ => rfl
  · intro a
    rw [hF a, Finset.sum_filter,
      Fintype.sum_equiv e (fun k => if (e k).1 = a then conjChannel (K (e k)) else 0)
        (fun c => if c.1 = a then conjChannel (K c) else 0) (fun _ => rfl)]
    symm
    rw [Fintype.sum_prod_type, Finset.sum_eq_single a]
    · exact Finset.sum_congr rfl fun i _ => if_pos rfl
    · intro a' _ ha'
      exact Finset.sum_eq_zero fun i _ => if_neg ha'
    · intro ha
      exact absurd (Finset.mem_univ _) ha

/-- **THE FACTORIZATION IS DISCHARGED FROM THE SPECTRAL RESOLUTION**, loudly: Mathlib's
spectral theorem (kernel-internal since the Kadison round) and the real square root of the
eigenvalues — the same two ingredients `scalarAvail_isKraus` uses. This does NOT retire
boundary item 3; that reclassification is a separate audit. -/
theorem psdFactorization_of_spectral (R : Type*) [Fintype R] [DecidableEq R] :
    PSDFactorization R := by
  intro ρ hρ
  obtain ⟨U, -, hspec⟩ := hermitian_spectral_edyad hρ.1
  refine ⟨U * Matrix.diagonal (fun i => ((Real.sqrt (hρ.1.eigenvalues i) : ℝ) : ℂ)), ?_⟩
  rw [Matrix.conjTranspose_mul, Matrix.diagonal_conjTranspose, Matrix.mul_assoc,
    ← Matrix.mul_assoc (Matrix.diagonal _), Matrix.diagonal_mul_diagonal, ← Matrix.mul_assoc,
    conj_diagonal_eq_sum_edyad]
  conv_lhs => rw [hspec]
  refine Finset.sum_congr rfl fun i _ => ?_
  have hs : ∀ r : ℝ, star ((r : ℝ) : ℂ) = ((r : ℝ) : ℂ) := fun r => by simp
  ext x y
  rw [Matrix.smul_apply, Matrix.smul_apply, smul_eq_mul, Complex.real_smul, Pi.star_apply, hs,
    ← Complex.ofReal_mul, Real.mul_self_sqrt (hρ.eigenvalues_nonneg i)]

end KrausStep

/-! ### Section E — the theory -/

section Theory

/-- **THE COUNTERMODEL, against boundary item 3.** Exactly quantum on the visible qubit;
2-positive-instrument on every composite; reference-tested preparations. -/
noncomputable def countermodelOf (hfac : PSDFactorization (Fin 2 × Fin 2)) :
    FiniteOperationalTheory (Fin 2) where
  avail := fun _ _ _ F => IsKrausFamily F
  availExt := fun _ _ _ _ F => IsTwoPositiveInstrument F
  avail_id := scalarAvail_isKraus
    ⟨fun _ => 1, fun _ => zero_le_one, by simp, fun _ => by
      rw [Complex.ofReal_one, one_smul]⟩
  avail_coarse := by
    rintro O O' _ _ _ _ F f hF
    exact isKrausFamily_coarse hF f
  availExt_coarse := by
    rintro n O O' _ _ _ _ F f ⟨h2, htr⟩
    refine ⟨fun a' => isTwoPositive_sum _ _ fun j _ => h2 j, fun X => ?_⟩
    rw [Finset.sum_congr rfl fun a' _ => by rw [LinearMap.sum_apply, Matrix.trace_sum],
      Finset.sum_fiberwise_of_maps_to (fun x _ => Finset.mem_univ (f x))
        (fun j => ((F j) X).trace)]
    exact htr X
  availExt_bind := by
    rintro n O O' _ _ _ _ F G ⟨hF2, hFtr⟩ hG
    refine ⟨fun c => isTwoPositive_comp ((hG c.1).1 c.2) (hF2 c.1), fun X => ?_⟩
    rw [Fintype.sum_prod_type]
    show ∑ a, ∑ b, ((G a b) ((F a) X)).trace = X.trace
    rw [Finset.sum_congr rfl fun a _ => (hG a).2 ((F a) X)]
    exact hFtr X
  prepAvail := fun n P => RefTestedPrep n P
  prepAvail_uniform := fun n =>
    ⟨uniformAttach_trace (n + 1) n.succ_ne_zero,
      amplR_uniformAttach_posSemidef (Matrix.posSemidef_vecMulVec_self_star _) _⟩
  prepAvail_post := by
    rintro n P Φ ⟨hPtr, hPpsd⟩ ⟨hΦ2, hΦtr⟩
    refine ⟨fun ρ => ?_, ?_⟩
    · show (Φ (P ρ)).trace = ρ.trace
      have h := hΦtr (P ρ)
      rw [Fintype.sum_unique] at h
      rw [h, hPtr]
    · rw [amplR_comp]
      exact hΦ2 () _ hPpsd
  readout := fun _ k => localLuders k
  readout_avail := fun n => ⟨fun k => localLuders_twoPositive k, localLuders_trace_sum⟩
  readout_local := fun _ k => localLuders_mapSpectatorIndependent k
  prepAvail_discard := by
    rintro n P O _ _ F ⟨hPtr, hPpsd⟩ ⟨hF2, hFtr⟩
    refine isKrausFamily_of_cp_of_factorization hfac _ (fun a => ?_) (fun X => ?_)
    · show (choiMatrix (discardWith n P (F a))).PosSemidef
      rw [choiMatrix_eq_ampl2, ← amplR_eq_ampl2, discardWith, amplR_comp, amplR_comp]
      exact amplR_ptraceAncL_posSemidef (hF2 a _ hPpsd)
    · rw [Finset.sum_congr rfl fun a _ => discardWith_trace n P (F a) X, hFtr (P X), hPtr X]

variable (hfac : PSDFactorization (Fin 2 × Fin 2))

/-- **EXACTLY QUANTUM ON THE VISIBLE QUBIT.** -/
theorem countermodelOf_exact : ExactFiniteEndomorphicQuantumOps (countermodelOf hfac) :=
  fun _ F => isKrausFamily_iff F

/-- **EVERY COMPOSITE UNITARY IS AVAILABLE.** -/
theorem countermodelOf_control : HasCompositeUnitaryControl (countermodelOf hfac) :=
  fun _ U hU => ⟨fun _ => conjChannel_twoPositive U, fun X => by
    rw [Fintype.sum_unique]
    exact conjChannel_trace U hU X⟩

/-- **THE REDUCTION MAP IS AVAILABLE** on the two-qubit composite. -/
theorem countermodelOf_reduction2_available :
    (countermodelOf hfac).availExt 2 Unit (fun _ => reduction2 (Fin 2 × Fin 2)) :=
  ⟨fun _ => reduction2_twoPositive, fun X => by
    rw [Fintype.sum_unique]
    exact reduction2_trace X⟩

/-- **NOT COMPOSITE-SOUND**: the available reduction map has no Kraus form. -/
theorem countermodelOf_not_krausSoundExt : ¬ KrausSoundExt (countermodelOf hfac) := fun h =>
  reduction2_not_cp (krausFamily_cp (h 2 Unit _ (countermodelOf_reduction2_available hfac)) ())

/-- **THE CONDITIONAL CAPSTONE**, against boundary item 3 only. -/
theorem countermodel_of_factorization (hfac : PSDFactorization (Fin 2 × Fin 2)) :
    ∃ T : FiniteOperationalTheory (Fin 2),
      ExactFiniteEndomorphicQuantumOps T ∧ HasCompositeUnitaryControl T ∧ ¬ KrausSoundExt T :=
  ⟨countermodelOf hfac, countermodelOf_exact hfac, countermodelOf_control hfac,
    countermodelOf_not_krausSoundExt hfac⟩

/-- **THE COUNTERMODEL, unconditional**: the factorization discharged by the spectral
resolution. -/
noncomputable def countermodel : FiniteOperationalTheory (Fin 2) :=
  countermodelOf (psdFactorization_of_spectral _)

theorem countermodel_exact : ExactFiniteEndomorphicQuantumOps countermodel :=
  countermodelOf_exact _

theorem countermodel_control : HasCompositeUnitaryControl countermodel :=
  countermodelOf_control _

theorem countermodel_reduction2_available :
    countermodel.availExt 2 Unit (fun _ => reduction2 (Fin 2 × Fin 2)) :=
  countermodelOf_reduction2_available _

theorem countermodel_not_krausSoundExt : ¬ KrausSoundExt countermodel :=
  countermodelOf_not_krausSoundExt _

/-- It has factor exchange and interference control too, since it has every composite
unitary. -/
theorem countermodel_hasFactorExchange : HasQubitFactorExchange countermodel :=
  compositeControl_hasFactorExchange _ countermodel_control

theorem countermodel_hasInterferenceControl :
    HasAncillaQubitInterferenceControl countermodel :=
  compositeControl_hasInterferenceControl _ countermodel_control

/-- **THE CAPSTONE.** Exact system QM plus full composite unitary control does NOT force
composite quantum soundness: the missing condition is not control richness. -/
theorem exactControl_not_implies_krausSoundExt :
    ∃ T : FiniteOperationalTheory (Fin 2),
      ExactFiniteEndomorphicQuantumOps T ∧ HasCompositeUnitaryControl T ∧ ¬ KrausSoundExt T :=
  ⟨countermodel, countermodel_exact, countermodel_control, countermodel_not_krausSoundExt⟩

end Theory

#print axioms amplR_comp
#print axioms choiMatrix_eq_ampl2
#print axioms twoPositive_qubit_cp
#print axioms isTwoPositive_comp
#print axioms isTwoPositive_sum
#print axioms ampl2_conjChannel
#print axioms conjChannel_twoPositive
#print axioms ampl2_localLuders
#print axioms localLuders_twoPositive
#print axioms localLuders_trace_sum
#print axioms amplR_ptraceAncL_eq
#print axioms amplR_uniformAttach_eq
#print axioms amplR_ptraceAncL_posSemidef
#print axioms amplR_uniformAttach_posSemidef
#print axioms uniformAttach_trace
#print axioms choiMatrix_conjChannel
#print axioms choiMatrix_injective
#print axioms kraus_of_choi_factor
#print axioms sum_conjTranspose_mul_eq_one_of_trace
#print axioms isKrausFamily_of_cp_of_factorization
#print axioms psdFactorization_of_spectral
#print axioms countermodelOf_exact
#print axioms countermodelOf_control
#print axioms countermodelOf_reduction2_available
#print axioms countermodelOf_not_krausSoundExt
#print axioms countermodel_of_factorization
#print axioms countermodel_exact
#print axioms countermodel_control
#print axioms countermodel_reduction2_available
#print axioms countermodel_not_krausSoundExt
#print axioms countermodel_hasFactorExchange
#print axioms countermodel_hasInterferenceControl
#print axioms exactControl_not_implies_krausSoundExt

end DimensionalCountermodel
end OIBridge
