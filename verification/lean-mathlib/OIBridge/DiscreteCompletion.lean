import OIBridge.PairFlowEquivalence
import Mathlib.Topology.Algebra.Order.Archimedean
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Bounds
import Mathlib.NumberTheory.Real.Irrational
import Mathlib.LinearAlgebra.Matrix.SchurComplement
import Mathlib.Analysis.Real.Pi.Irrational

/-!
# The discrete completion audit — one fixed discrete mixing gate and density in finite quantum mechanics

The preregistered pass of `DISCRETE-COMPLETION-AUDIT.md`, read under its scope amendment. Nothing
here is named "C5"; no continuous pair flow enters any constructive route; no irrationality
condition is a physical principle; dense availability is never identified with exact availability.
-/

namespace OIBridge
namespace DiscreteCompletion

open Complex Matrix CoherentLift SpectatorBridge OperationalAssembly AncillaClosure
open MonoidalCompletion InterventionLocality MicroReversibility PrimitiveSource LieRankSource
open DiagonalTheory SubstratumInterface StructuralClosure MinimalRepertoire LevelOneSeam
open PhysicalCharacterization RouteB ManuscriptAxioms LiftAudit SubstratumInterfaceAudit
open InstrumentRealization SecondOrderCircuit ExecSource FlowEndpoint DerivedQ3 C5Discovery
open PolarizationClosure CoherentContinuumSource StateMixingCoupling RealPairFlow
open PairFlowEquivalence CompositeSoundness KrausSoundness Set
open scoped Matrix.Norms.L2Operator

/-! ### Section A — T1: the predicates and the metric -/

section Predicates

/-- **THE FIXED GATE, SOURCED**: the conjugation channel of `mixImage n α` is available at every
level, at the one fixed angle `α`; no parameter. -/
def FixedGateSourced (α : ℝ) (T : FiniteOperationalTheory (Fin 2)) : Prop :=
  ∀ n : ℕ, T.availExt n Unit (fun _ => conjChannel (mixImage n α))

/-- **THE CHANNEL METRIC, AS A QUANTITATIVE PREDICATE**: `Φ` and `Ψ` are within `ε` when the
operator norm of their difference, matrices normed by the operator norm, is at most `ε`. -/
def ChanWithin {S : Type} [Fintype S] [DecidableEq S] (ε : ℝ)
    (Φ Ψ : Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ) : Prop :=
  ∀ X : Matrix S S ℂ, ‖Φ X - Ψ X‖ ≤ ε * ‖X‖

/-- **D1, DENSE UNITARY CONTROL**: at every level every unitary is approximated, up to a unit
scalar and in the operator norm, by a unitary whose conjugation channel is available. -/
def DenseUnitaryControl (T : FiniteOperationalTheory (Fin 2)) : Prop :=
  ∀ (n : ℕ) (U : Matrix (Fin 2 × Fin n) (Fin 2 × Fin n) ℂ), Uᴴ * U = 1 →
    ∀ ε : ℝ, 0 < ε → ∃ (V : Matrix (Fin 2 × Fin n) (Fin 2 × Fin n) ℂ) (c : ℂ),
      Vᴴ * V = 1 ∧ ‖c‖ = 1 ∧ T.availExt n Unit (fun _ => conjChannel V) ∧ ‖U - c • V‖ < ε

/-- **THE DENSITY HALF OF D2**: every finite endomorphic Kraus instrument at every positive level
is approximated, outcome by outcome in the channel metric, by an available family. -/
def KrausDense (T : FiniteOperationalTheory (Fin 2)) : Prop :=
  ∀ (k m : ℕ) (F : Fin m → Matrix (Fin 2 × Fin (k + 1)) (Fin 2 × Fin (k + 1)) ℂ →ₗ[ℂ]
      Matrix (Fin 2 × Fin (k + 1)) (Fin 2 × Fin (k + 1)) ℂ),
    IsFiniteEndomorphicKrausInstrument F → ∀ ε : ℝ, 0 < ε →
      ∃ G, T.availExt (k + 1) (Fin m) G ∧ ∀ a, ChanWithin ε (F a) (G a)

/-- **D2, DENSE FINITE QUANTUM MECHANICS**: contained in quantum mechanics and dense in it. -/
def DenseFiniteQM (T : FiniteOperationalTheory (Fin 2)) : Prop :=
  KrausSoundExt T ∧ KrausDense T

/-- **THE CLOSURE OF AVAILABILITY OF D3**, outcome-wise at a positive level. -/
def ClosureAvail (T : FiniteOperationalTheory (Fin 2)) (k m : ℕ)
    (F : Fin m → Matrix (Fin 2 × Fin (k + 1)) (Fin 2 × Fin (k + 1)) ℂ →ₗ[ℂ]
      Matrix (Fin 2 × Fin (k + 1)) (Fin 2 × Fin (k + 1)) ℂ) : Prop :=
  ∀ ε : ℝ, 0 < ε → ∃ G, T.availExt (k + 1) (Fin m) G ∧ ∀ a, ChanWithin ε (F a) (G a)

end Predicates

/-! ### Section B — T2: the bridge -/

section Bridge

variable {S : Type} [Fintype S] [DecidableEq S]

theorem mem_unitary_of_conjTranspose_mul {U : Matrix S S ℂ} (hU : Uᴴ * U = 1) :
    U ∈ unitary (Matrix S S ℂ) := by
  refine Unitary.mem_iff.mpr ⟨?_, ?_⟩
  · rw [Matrix.star_eq_conjTranspose]; exact hU
  · rw [Matrix.star_eq_conjTranspose]; exact mul_eq_one_comm.mp hU

/-- **A UNITARY HAS OPERATOR NORM ONE.** -/
theorem norm_eq_one_of_unitary [Nonempty S] {U : Matrix S S ℂ} (hU : Uᴴ * U = 1) : ‖U‖ = 1 :=
  CStarRing.norm_of_mem_unitary (mem_unitary_of_conjTranspose_mul hU)

theorem norm_mul_unitary_left [Nonempty S] {U : Matrix S S ℂ} (hU : Uᴴ * U = 1)
    (A : Matrix S S ℂ) : ‖U * A‖ = ‖A‖ :=
  CStarRing.norm_mem_unitary_mul A (mem_unitary_of_conjTranspose_mul hU)

theorem norm_mul_unitary_right [Nonempty S] {U : Matrix S S ℂ} (hU : Uᴴ * U = 1)
    (A : Matrix S S ℂ) : ‖A * U‖ = ‖A‖ :=
  CStarRing.norm_mul_mem_unitary A (mem_unitary_of_conjTranspose_mul hU)

/-- **THE BRIDGE**: unitaries within `ε` in the operator norm have conjugation channels within
`2 ε` in the channel metric, since `U X Uᴴ − V X Vᴴ = (U − V) X Uᴴ + V X (U − V)ᴴ`. -/
theorem conj_within [Nonempty S] {U V : Matrix S S ℂ} (hU : Uᴴ * U = 1) (hV : Vᴴ * V = 1)
    {ε : ℝ} (h : ‖U - V‖ ≤ ε) : ChanWithin (2 * ε) (conjChannel U) (conjChannel V) := by
  intro X
  have hdecomp : U * X * Uᴴ - V * X * Vᴴ = (U - V) * X * Uᴴ + V * X * (U - V)ᴴ := by
    rw [Matrix.conjTranspose_sub]
    simp only [Matrix.sub_mul, Matrix.mul_sub]
    abel
  show ‖U * X * Uᴴ - V * X * Vᴴ‖ ≤ 2 * ε * ‖X‖
  rw [hdecomp]
  have hUn : ‖Uᴴ‖ = 1 := by rw [Matrix.l2_opNorm_conjTranspose]; exact norm_eq_one_of_unitary hU
  have hVn : ‖V‖ = 1 := norm_eq_one_of_unitary hV
  have hdn : ‖(U - V)ᴴ‖ ≤ ε := by rw [Matrix.l2_opNorm_conjTranspose]; exact h
  have h1 : ‖(U - V) * X * Uᴴ‖ ≤ ε * ‖X‖ := by
    calc ‖(U - V) * X * Uᴴ‖ ≤ ‖(U - V) * X‖ * ‖Uᴴ‖ := norm_mul_le _ _
      _ ≤ ‖U - V‖ * ‖X‖ * ‖Uᴴ‖ := by gcongr; exact norm_mul_le _ _
      _ = ‖U - V‖ * ‖X‖ := by rw [hUn, mul_one]
      _ ≤ ε * ‖X‖ := by gcongr
  have h2 : ‖V * X * (U - V)ᴴ‖ ≤ ε * ‖X‖ := by
    calc ‖V * X * (U - V)ᴴ‖ ≤ ‖V * X‖ * ‖(U - V)ᴴ‖ := norm_mul_le _ _
      _ ≤ ‖V‖ * ‖X‖ * ‖(U - V)ᴴ‖ := by gcongr; exact norm_mul_le _ _
      _ = ‖X‖ * ‖(U - V)ᴴ‖ := by rw [hVn, one_mul]
      _ ≤ ‖X‖ * ε := by gcongr
      _ = ε * ‖X‖ := mul_comm _ _
  calc ‖(U - V) * X * Uᴴ + V * X * (U - V)ᴴ‖
      ≤ ‖(U - V) * X * Uᴴ‖ + ‖V * X * (U - V)ᴴ‖ := norm_add_le _ _
    _ ≤ ε * ‖X‖ + ε * ‖X‖ := add_le_add h1 h2
    _ = 2 * ε * ‖X‖ := by ring

/-- Products of unitaries: the error of a product is at most the sum of the errors. -/
theorem norm_mul_sub_mul_le [Nonempty S] {A A' B B' : Matrix S S ℂ}
    (hA : Aᴴ * A = 1) (hB' : B'ᴴ * B' = 1) :
    ‖A * B - A' * B'‖ ≤ ‖A - A'‖ + ‖B - B'‖ := by
  have h : A * B - A' * B' = A * (B - B') + (A - A') * B' := by
    simp only [Matrix.mul_sub, Matrix.sub_mul]; abel
  rw [h]
  calc ‖A * (B - B') + (A - A') * B'‖ ≤ ‖A * (B - B')‖ + ‖(A - A') * B'‖ := norm_add_le _ _
    _ = ‖B - B'‖ + ‖A - A'‖ := by
        rw [norm_mul_unitary_left hA, norm_mul_unitary_right hB']
    _ = ‖A - A'‖ + ‖B - B'‖ := add_comm _ _

end Bridge

/-! ### Section C — the block algebra on `Fin 2 × Fin n`: one site pair addressed -/

section Blocks

variable {n : ℕ}

/-- The ancilla projector onto the value `k₀`. -/
def anc (k₀ : Fin n) : Matrix (Fin n) (Fin n) ℂ :=
  Matrix.of fun i j => if i = k₀ ∧ j = k₀ then 1 else 0

/-- Its complement. -/
def ancC (k₀ : Fin n) : Matrix (Fin n) (Fin n) ℂ := 1 - anc k₀

theorem anc_apply (k₀ i j : Fin n) : anc k₀ i j = if i = k₀ ∧ j = k₀ then 1 else 0 := rfl

theorem anc_mul_anc (k₀ : Fin n) : anc k₀ * anc k₀ = anc k₀ := by
  ext i j
  simp only [Matrix.mul_apply, anc_apply]
  rw [Finset.sum_eq_single k₀]
  · by_cases hi : i = k₀ <;> by_cases hj : j = k₀ <;> simp [hi, hj]
  · intro m _ hm; simp [hm]
  · intro h; exact absurd (Finset.mem_univ _) h

theorem anc_conjTranspose (k₀ : Fin n) : (anc k₀)ᴴ = anc k₀ := by
  ext i j
  simp only [Matrix.conjTranspose_apply, anc_apply]
  by_cases hi : i = k₀ <;> by_cases hj : j = k₀ <;> simp [hi, hj]

theorem anc_add_ancC (k₀ : Fin n) : anc k₀ + ancC k₀ = 1 := by
  simp [ancC]

theorem anc_mul_ancC (k₀ : Fin n) : anc k₀ * ancC k₀ = 0 := by
  rw [ancC, Matrix.mul_sub, Matrix.mul_one, anc_mul_anc, sub_self]

theorem ancC_mul_anc (k₀ : Fin n) : ancC k₀ * anc k₀ = 0 := by
  rw [ancC, Matrix.sub_mul, Matrix.one_mul, anc_mul_anc, sub_self]

theorem ancC_mul_ancC (k₀ : Fin n) : ancC k₀ * ancC k₀ = ancC k₀ := by
  rw [ancC, Matrix.sub_mul, Matrix.one_mul, Matrix.mul_sub, Matrix.mul_one, anc_mul_anc]
  abel

theorem ancC_conjTranspose (k₀ : Fin n) : (ancC k₀)ᴴ = ancC k₀ := by
  rw [ancC, Matrix.conjTranspose_sub, Matrix.conjTranspose_one, anc_conjTranspose]

theorem tensorOf_zero_right {R S : Type} [Fintype R] [DecidableEq R] [Fintype S] [DecidableEq S]
    (A : Matrix R R ℂ) : tensorOf A (0 : Matrix S S ℂ) = 0 := by
  ext p q; simp [tensorOf_apply]

theorem tensorOf_add_right {R S : Type} [Fintype R] [DecidableEq R] [Fintype S] [DecidableEq S]
    (A : Matrix R R ℂ) (B C : Matrix S S ℂ) : tensorOf A (B + C) = tensorOf A B + tensorOf A C := by
  ext p q; simp [tensorOf_apply, mul_add]

theorem tensorOf_sub_left {R S : Type} [Fintype R] [DecidableEq R] [Fintype S] [DecidableEq S]
    (A B : Matrix R R ℂ) (C : Matrix S S ℂ) : tensorOf (A - B) C = tensorOf A C - tensorOf B C := by
  ext p q; simp [tensorOf_apply, sub_mul]

/-- **THE BLOCK-ONLY EMBEDDING**: `M` on the site pair with ancilla value `k₀`, zero elsewhere. -/
def blockOnly (k₀ : Fin n) (M : Matrix (Fin 2) (Fin 2) ℂ) :
    Matrix (Fin 2 × Fin n) (Fin 2 × Fin n) ℂ :=
  tensorOf M (anc k₀)

/-- **THE ADDRESSED GATE**: `M` on the site pair with ancilla value `k₀`, the identity elsewhere. -/
def blockOf (k₀ : Fin n) (M : Matrix (Fin 2) (Fin 2) ℂ) :
    Matrix (Fin 2 × Fin n) (Fin 2 × Fin n) ℂ :=
  tensorOf M (anc k₀) + tensorOf 1 (ancC k₀)

theorem blockOnly_mul (k₀ : Fin n) (M N : Matrix (Fin 2) (Fin 2) ℂ) :
    blockOnly k₀ M * blockOnly k₀ N = blockOnly k₀ (M * N) := by
  simp only [blockOnly, tensorOf_mul', anc_mul_anc]

theorem blockOnly_conjTranspose (k₀ : Fin n) (M : Matrix (Fin 2) (Fin 2) ℂ) :
    (blockOnly k₀ M)ᴴ = blockOnly k₀ Mᴴ := by
  simp only [blockOnly, tensorOf_conjTranspose, anc_conjTranspose]

theorem blockOnly_smul (k₀ : Fin n) (c : ℂ) (M : Matrix (Fin 2) (Fin 2) ℂ) :
    blockOnly k₀ (c • M) = c • blockOnly k₀ M := by
  simp only [blockOnly, tensorOf_smul_left]

theorem blockOf_mul (k₀ : Fin n) (M N : Matrix (Fin 2) (Fin 2) ℂ) :
    blockOf k₀ M * blockOf k₀ N = blockOf k₀ (M * N) := by
  simp only [blockOf, Matrix.add_mul, Matrix.mul_add, tensorOf_mul', anc_mul_anc, anc_mul_ancC,
    ancC_mul_anc, ancC_mul_ancC, tensorOf_zero_right, Matrix.mul_one, Matrix.one_mul, add_zero,
    zero_add]

theorem blockOf_one (k₀ : Fin n) : blockOf k₀ (1 : Matrix (Fin 2) (Fin 2) ℂ) = 1 := by
  rw [blockOf, ← tensorOf_add_right, anc_add_ancC, ReferenceExtension.tensorOf_one_one]

theorem blockOf_conjTranspose (k₀ : Fin n) (M : Matrix (Fin 2) (Fin 2) ℂ) :
    (blockOf k₀ M)ᴴ = blockOf k₀ Mᴴ := by
  simp only [blockOf, Matrix.conjTranspose_add, tensorOf_conjTranspose, anc_conjTranspose,
    ancC_conjTranspose, Matrix.conjTranspose_one]

theorem blockOf_unitary (k₀ : Fin n) {M : Matrix (Fin 2) (Fin 2) ℂ} (hM : Mᴴ * M = 1) :
    (blockOf k₀ M)ᴴ * blockOf k₀ M = 1 := by
  rw [blockOf_conjTranspose, blockOf_mul, hM, blockOf_one]

theorem blockOf_sub (k₀ : Fin n) (M N : Matrix (Fin 2) (Fin 2) ℂ) :
    blockOf k₀ M - blockOf k₀ N = blockOnly k₀ (M - N) := by
  simp only [blockOf, blockOnly, tensorOf_sub_left]
  abel

theorem blockOnly_one_eq_diagonal (k₀ : Fin n) :
    blockOnly k₀ (1 : Matrix (Fin 2) (Fin 2) ℂ)
      = Matrix.diagonal (fun p : Fin 2 × Fin n => if p.2 = k₀ then 1 else 0) := by
  ext ⟨x, k⟩ ⟨y, l⟩
  simp only [blockOnly, tensorOf_apply, anc_apply, Matrix.one_apply, Matrix.diagonal_apply,
    Prod.mk.injEq]
  by_cases hx : x = y
  · subst hx
    by_cases hk : k = l
    · subst hk; simp
    · simp [hk]
      intro h1 h2; exact hk (h1.trans h2.symm)
  · simp [hx]

/-- The projector onto the block has operator norm at most one. -/
theorem blockOnly_one_norm_le (k₀ : Fin n) :
    ‖blockOnly k₀ (1 : Matrix (Fin 2) (Fin 2) ℂ)‖ ≤ 1 := by
  rw [blockOnly_one_eq_diagonal, Matrix.l2_opNorm_diagonal]
  refine (pi_norm_le_iff_of_nonneg
    (x := fun p : Fin 2 × Fin n => if p.2 = k₀ then (1 : ℂ) else 0) zero_le_one).mpr fun p => ?_
  split_ifs <;> simp

theorem rot_unitary (θ : ℝ) : (StateMixingCoupling.rot θ)ᴴ * StateMixingCoupling.rot θ = 1 := by
  rw [rot_conjTranspose, rot_mul, neg_add_cancel, rot_zero]

/-- **THE GRAM MATRIX OF `StateMixingCoupling.rot δ − 1`** is the scalar `2 − 2 cos δ`. -/
theorem rot_sub_one_gram (δ : ℝ) :
    (StateMixingCoupling.rot δ - 1)ᴴ * (StateMixingCoupling.rot δ - 1) = ((2 - 2 * Real.cos δ : ℝ) : ℂ) • (1 : Matrix (Fin 2) (Fin 2) ℂ) := by
  have hcs := Real.cos_sq_add_sin_sq δ
  ext i j
  fin_cases i <;> fin_cases j <;>
    (simp [Matrix.mul_apply, Fin.sum_univ_two, StateMixingCoupling.rot, Matrix.conjTranspose_apply,
      Matrix.sub_apply, Matrix.one_apply, Complex.conj_ofReal, -Complex.ofReal_cos,
      -Complex.ofReal_sin]
     apply Complex.ext <;> simp [-Complex.ofReal_cos, -Complex.ofReal_sin]
     all_goals nlinarith [hcs])

/-- **THE BLOCK ROTATION IS `|δ|`-CLOSE TO THE IDENTITY**: by the C*-identity,
`‖blockOnly (StateMixingCoupling.rot δ − 1)‖² = ‖(2 − 2 cos δ) • P‖ ≤ 2 − 2 cos δ ≤ δ²`. -/
theorem blockOnly_rot_sub_one_norm_le (k₀ : Fin n) (δ : ℝ) :
    ‖blockOnly k₀ (StateMixingCoupling.rot δ - 1)‖ ≤ |δ| := by
  have hsq : ‖blockOnly k₀ (StateMixingCoupling.rot δ - 1)‖ * ‖blockOnly k₀ (StateMixingCoupling.rot δ - 1)‖ ≤ |δ| * |δ| := by
    rw [← Matrix.l2_opNorm_conjTranspose_mul_self, blockOnly_conjTranspose, blockOnly_mul,
      rot_sub_one_gram, blockOnly_smul, norm_smul]
    have hc : 1 - δ ^ 2 / 2 ≤ Real.cos δ := Real.one_sub_sq_div_two_le_cos
    have h0 : (0 : ℝ) ≤ 2 - 2 * Real.cos δ := by linarith [Real.cos_le_one δ]
    have hn : ‖((2 - 2 * Real.cos δ : ℝ) : ℂ)‖ = 2 - 2 * Real.cos δ := by
      rw [Complex.norm_real, Real.norm_of_nonneg h0]
    rw [hn]
    calc (2 - 2 * Real.cos δ) * ‖blockOnly k₀ (1 : Matrix (Fin 2) (Fin 2) ℂ)‖
        ≤ (2 - 2 * Real.cos δ) * 1 := by gcongr; exact blockOnly_one_norm_le k₀
      _ ≤ |δ| * |δ| := by rw [← sq, sq_abs]; linarith
  exact (mul_self_le_mul_self_iff (norm_nonneg _) (abs_nonneg _)).mpr hsq

/-- The two block rotations at angles `θ` and `θ'` are `|θ − θ'|`-close. -/
theorem blockOf_rot_dist_le (k₀ : Fin n) (θ θ' : ℝ) :
    ‖blockOf k₀ (StateMixingCoupling.rot θ) - blockOf k₀ (StateMixingCoupling.rot θ')‖ ≤ |θ - θ'| := by
  have h : blockOf k₀ (StateMixingCoupling.rot θ) - blockOf k₀ (StateMixingCoupling.rot θ')
      = blockOf k₀ (StateMixingCoupling.rot θ') * blockOnly k₀ (StateMixingCoupling.rot (θ - θ') - 1) := by
    rw [← blockOf_sub, Matrix.mul_sub, blockOf_one, Matrix.mul_one, blockOf_mul, rot_mul,
      show θ' + (θ - θ') = θ by ring]
  rw [h]
  rcases Nat.eq_zero_or_pos n with rfl | hn
  · exact k₀.elim0
  · have : Nonempty (Fin 2 × Fin n) := ⟨(0, k₀)⟩
    rw [norm_mul_unitary_left (blockOf_unitary k₀ (rot_unitary θ'))]
    exact blockOnly_rot_sub_one_norm_le k₀ _

end Blocks

/-! ### Section D — the two-by-two gates and the Euler decomposition -/

section Euler

/-- The quarter phase on the second value of the pair. -/
def S2 : Matrix (Fin 2) (Fin 2) ℂ := !![1, 0; 0, Complex.I]

/-- The exchange of the pair. -/
def X2 : Matrix (Fin 2) (Fin 2) ℂ := !![0, 1; 1, 0]

/-- The rotation about the perpendicular axis, the quarter-phase conjugate of `rot`. -/
noncomputable def rx (θ : ℝ) : Matrix (Fin 2) (Fin 2) ℂ :=
  !![(Real.cos θ : ℂ), Complex.I * Real.sin θ; Complex.I * Real.sin θ, (Real.cos θ : ℂ)]

theorem S2_unitary : S2ᴴ * S2 = 1 := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [S2, Matrix.mul_apply, Fin.sum_univ_two, Matrix.conjTranspose_apply, Complex.conj_I]

theorem X2_unitary : X2ᴴ * X2 = 1 := by
  ext i j
  fin_cases i <;> fin_cases j <;> simp [X2, Matrix.mul_apply, Fin.sum_univ_two, Matrix.conjTranspose_apply]

/-- **THE PERPENDICULAR ROTATION IS THE QUARTER-PHASE CONJUGATE** of the real rotation. -/
theorem rx_eq_conj (θ : ℝ) : S2 * StateMixingCoupling.rot θ * S2ᴴ = rx θ := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [S2, rx, StateMixingCoupling.rot, Matrix.mul_apply, Fin.sum_univ_two,
      Matrix.conjTranspose_apply, Complex.conj_I] <;> ring_nf
  all_goals simp [Complex.I_sq]

theorem rx_unitary (θ : ℝ) : (rx θ)ᴴ * rx θ = 1 := by
  have hcs := Real.cos_sq_add_sin_sq θ
  ext i j
  fin_cases i <;> fin_cases j <;>
    (simp [rx, Matrix.mul_apply, Fin.sum_univ_two, Matrix.conjTranspose_apply, Complex.conj_I,
      Complex.conj_ofReal, -Complex.ofReal_cos, -Complex.ofReal_sin]
     apply Complex.ext <;> simp [-Complex.ofReal_cos, -Complex.ofReal_sin]
     all_goals nlinarith [hcs])

/-- **THE EXCHANGE REVERSES THE ROTATION.** -/
theorem X2_rot_X2 (θ : ℝ) : X2 * StateMixingCoupling.rot θ * X2 = StateMixingCoupling.rot (-θ) := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [X2, StateMixingCoupling.rot, Matrix.mul_apply, Fin.sum_univ_two, Real.cos_neg, Real.sin_neg]

theorem rot_pow (θ : ℝ) : ∀ k : ℕ, StateMixingCoupling.rot θ ^ k = StateMixingCoupling.rot (k * θ)
  | 0 => by simp [rot_zero]
  | k + 1 => by rw [pow_succ, rot_pow θ k, rot_mul]; push_cast; ring_nf

theorem rot_add_int_mul_two_pi (θ : ℝ) (m : ℤ) :
    StateMixingCoupling.rot (θ + m * (2 * Real.pi)) = StateMixingCoupling.rot θ := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [StateMixingCoupling.rot, Real.cos_add_int_mul_two_pi, Real.sin_add_int_mul_two_pi]

/-- **THE PRODUCT FORMULA** for the rotation, the perpendicular rotation and the rotation. -/
theorem rot_rx_rot (a b c : ℝ) :
    StateMixingCoupling.rot a * rx b * StateMixingCoupling.rot c
      = !![(Real.cos b * Real.cos (a + c) : ℂ) + Complex.I * (Real.sin b * Real.sin (c - a)),
            -(Real.cos b * Real.sin (a + c) : ℂ) + Complex.I * (Real.sin b * Real.cos (a - c));
          (Real.cos b * Real.sin (a + c) : ℂ) + Complex.I * (Real.sin b * Real.cos (a - c)),
            (Real.cos b * Real.cos (a + c) : ℂ) + Complex.I * (Real.sin b * Real.sin (a - c))] := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [StateMixingCoupling.rot, rx, Matrix.mul_apply, Fin.sum_univ_two, Real.cos_add,
      Real.sin_add, Real.cos_sub, Real.sin_sub] <;> ring

/-- **THE SPECIAL-UNITARY FORM**: a two-by-two unitary of determinant one has second column
`(−q̄, p̄)` when its first column is `(p, q)`. -/
theorem su2_form {M : Matrix (Fin 2) (Fin 2) ℂ} (hM : Mᴴ * M = 1) (hdet : M.det = 1) :
    M 1 1 = (starRingEnd ℂ) (M 0 0) ∧ M 0 1 = -(starRingEnd ℂ) (M 1 0) := by
  have e1 := congrFun (congrFun hM 0) 0
  have e2 := congrFun (congrFun hM 0) 1
  simp only [Matrix.mul_apply, Fin.sum_univ_two, Matrix.conjTranspose_apply, Matrix.one_apply,
    Fin.isValue, if_true, Fin.zero_eq_one_iff, OfNat.ofNat_ne_one, if_false, Complex.star_def] at e1 e2
  rw [Matrix.det_fin_two] at hdet
  have hs : M 1 1 = (starRingEnd ℂ) (M 0 0) := by
    linear_combination (-(M 1 1)) * e1 + (M 1 0) * e2 + (starRingEnd ℂ) (M 0 0) * hdet
  refine ⟨hs, ?_⟩
  rw [hs] at e2 hdet
  linear_combination (M 0 0) * e2 + (starRingEnd ℂ) (M 1 0) * (e1 - hdet)
    - (M 0 1 + (starRingEnd ℂ) (M 1 0)) * e1

theorem det_norm_one {M : Matrix (Fin 2) (Fin 2) ℂ} (hM : Mᴴ * M = 1) : ‖M.det‖ = 1 := by
  have h := congrArg Matrix.det hM
  rw [Matrix.det_mul, Matrix.det_conjTranspose, Matrix.det_one, Complex.star_def, mul_comm,
    Complex.mul_conj, Complex.normSq_eq_norm_sq] at h
  have h' : ‖M.det‖ ^ 2 = 1 := by exact_mod_cast h
  nlinarith [norm_nonneg M.det]

/-- **EVERY TWO-BY-TWO UNITARY IS A UNIT SCALAR TIMES A SPECIAL UNITARY.** -/
theorem exists_unit_scalar_su2 {M : Matrix (Fin 2) (Fin 2) ℂ} (hM : Mᴴ * M = 1) :
    ∃ s : ℂ, ‖s‖ = 1 ∧ ((s⁻¹ • M)ᴴ * (s⁻¹ • M) = 1) ∧ (s⁻¹ • M).det = 1 := by
  set s : ℂ := Complex.exp (((Complex.arg M.det / 2 : ℝ) : ℂ) * Complex.I) with hs
  have hsn : ‖s‖ = 1 := Complex.norm_exp_ofReal_mul_I _
  have hss : s * s = M.det := by
    rw [hs, ← Complex.exp_add, ← add_mul]
    have : ((Complex.arg M.det / 2 : ℝ) : ℂ) + ((Complex.arg M.det / 2 : ℝ) : ℂ)
        = ((Complex.arg M.det : ℝ) : ℂ) := by push_cast; ring
    rw [this]
    have h := Complex.norm_mul_exp_arg_mul_I M.det
    rwa [det_norm_one hM, Complex.ofReal_one, one_mul] at h
  have hs0 : s ≠ 0 := by
    intro h; rw [h, norm_zero] at hsn; exact zero_ne_one hsn
  refine ⟨s, hsn, ?_, ?_⟩
  · rw [Matrix.conjTranspose_smul, Matrix.smul_mul, Matrix.mul_smul, smul_smul, hM]
    have : star s⁻¹ * s⁻¹ = 1 := by
      rw [Complex.star_def, map_inv₀, ← mul_inv, mul_comm, Complex.mul_conj,
        Complex.normSq_eq_norm_sq, hsn]
      norm_num
    rw [this, one_smul]
  · rw [Matrix.det_smul, Fintype.card_fin, ← hss]
    field_simp

/-- **THE EULER DECOMPOSITION** of the special-unitary form: for `|p|² + |q|² = 1`, the matrix
`[[p, −q̄], [q, p̄]]` is `rot a · rx b · rot c` for real angles. -/
theorem euler_of_su2 (p q : ℂ) (h : ‖p‖ ^ 2 + ‖q‖ ^ 2 = 1) :
    ∃ a b c : ℝ, StateMixingCoupling.rot a * rx b * StateMixingCoupling.rot c
      = !![p, -(starRingEnd ℂ) q; q, (starRingEnd ℂ) p] := by
  have hsum : p.re ^ 2 + q.re ^ 2 + (p.im ^ 2 + q.im ^ 2) = 1 := by
    have hp := Complex.sq_norm p
    have hq := Complex.sq_norm q
    rw [Complex.normSq_apply] at hp hq
    nlinarith [hp, hq, h]
  set r1 : ℝ := Real.sqrt (p.re ^ 2 + q.re ^ 2) with hr1
  set r2 : ℝ := Real.sqrt (p.im ^ 2 + q.im ^ 2) with hr2
  have hr1sq : r1 ^ 2 = p.re ^ 2 + q.re ^ 2 := Real.sq_sqrt (by positivity)
  have hr2sq : r2 ^ 2 = p.im ^ 2 + q.im ^ 2 := Real.sq_sqrt (by positivity)
  have hr1nn : 0 ≤ r1 := Real.sqrt_nonneg _
  have hr2nn : 0 ≤ r2 := Real.sqrt_nonneg _
  have hr2le : r2 ≤ 1 := by nlinarith
  set b := Real.arcsin r2 with hb
  have hsinb : Real.sin b = r2 := Real.sin_arcsin (by linarith) hr2le
  have hcosb : Real.cos b = r1 := by
    rw [hb, Real.cos_arcsin]
    have : 1 - r2 ^ 2 = r1 ^ 2 := by linarith
    rw [this, Real.sqrt_sq hr1nn]
  -- the two planar angles
  have hangle : ∀ x y : ℝ, ∃ u : ℝ, Real.sqrt (x ^ 2 + y ^ 2) * Real.cos u = x
      ∧ Real.sqrt (x ^ 2 + y ^ 2) * Real.sin u = y := by
    intro x y
    set z : ℂ := ⟨x, y⟩ with hz
    have hn : ‖z‖ = Real.sqrt (x ^ 2 + y ^ 2) := by
      have : ‖z‖ ^ 2 = x ^ 2 + y ^ 2 := by
        rw [Complex.sq_norm, Complex.normSq_apply]; simp [hz]; ring
      rw [← this, Real.sqrt_sq (norm_nonneg _)]
    have hzre : z.re = x := rfl
    have hzim : z.im = y := rfl
    have hexp := Complex.norm_mul_exp_arg_mul_I z
    refine ⟨Complex.arg z, ?_, ?_⟩
    · have hre := congrArg Complex.re hexp
      rw [Complex.mul_re, Complex.exp_ofReal_mul_I_re, Complex.exp_ofReal_mul_I_im,
        Complex.ofReal_re, Complex.ofReal_im, zero_mul, sub_zero, hn, hzre] at hre
      exact hre
    · have him := congrArg Complex.im hexp
      rw [Complex.mul_im, Complex.exp_ofReal_mul_I_re, Complex.exp_ofReal_mul_I_im,
        Complex.ofReal_re, Complex.ofReal_im, zero_mul, add_zero, hn, hzim] at him
      exact him
  obtain ⟨u, hu1, hu2⟩ := hangle p.re q.re
  obtain ⟨v, hv1, hv2⟩ := hangle q.im p.im
  rw [← hr1] at hu1 hu2
  rw [add_comm, ← hr2] at hv1 hv2
  refine ⟨(u - v) / 2, b, (u + v) / 2, ?_⟩
  rw [rot_rx_rot]
  have e1 : (u - v) / 2 + (u + v) / 2 = u := by ring
  have e2 : (u + v) / 2 - (u - v) / 2 = v := by ring
  have e3 : (u - v) / 2 - (u + v) / 2 = -v := by ring
  rw [e1, e2, e3, Real.cos_neg, Real.sin_neg, hcosb, hsinb]
  ext i j
  fin_cases i <;> fin_cases j <;>
    apply Complex.ext <;>
    simp [Complex.mul_re, Complex.mul_im, Complex.conj_re, Complex.conj_im, hu1, hu2, hv1, hv2,
      -Complex.ofReal_cos, -Complex.ofReal_sin]

/-- **EVERY TWO-BY-TWO UNITARY IS A UNIT SCALAR TIMES `rot a · rx b · rot c`.** -/
theorem euler_of_unitary {M : Matrix (Fin 2) (Fin 2) ℂ} (hM : Mᴴ * M = 1) :
    ∃ (s : ℂ) (a b c : ℝ), ‖s‖ = 1
      ∧ M = s • (StateMixingCoupling.rot a * rx b * StateMixingCoupling.rot c) := by
  obtain ⟨s, hsn, hN, hdet⟩ := exists_unit_scalar_su2 hM
  set N := s⁻¹ • M with hNdef
  obtain ⟨h11, h01⟩ := su2_form hN hdet
  have e1 := congrFun (congrFun hN 0) 0
  simp only [Matrix.mul_apply, Fin.sum_univ_two, Matrix.conjTranspose_apply, Matrix.one_apply,
    Fin.isValue, if_true, Complex.star_def] at e1
  have hpq : ‖N 0 0‖ ^ 2 + ‖N 1 0‖ ^ 2 = 1 := by
    have := e1
    rw [mul_comm ((starRingEnd ℂ) (N 0 0)), mul_comm ((starRingEnd ℂ) (N 1 0)), Complex.mul_conj,
      Complex.mul_conj, Complex.normSq_eq_norm_sq, Complex.normSq_eq_norm_sq] at this
    exact_mod_cast this
  obtain ⟨a, b, c, habc⟩ := euler_of_su2 (N 0 0) (N 1 0) hpq
  refine ⟨s, a, b, c, hsn, ?_⟩
  have hs0 : s ≠ 0 := by
    intro h; rw [h, norm_zero] at hsn; exact zero_ne_one hsn
  have hMN : M = s • N := by
    rw [hNdef, smul_smul, mul_inv_cancel₀ hs0, one_smul]
  rw [hMN, habc]
  congr 1
  ext i j
  fin_cases i <;> fin_cases j <;> simp [h11, h01]

end Euler

/-! ### Section E — T4: density of the special-unitary block from one irrational angle -/

section Density

/-- **THE ANGLES ARE DENSE**: when `β/π` is irrational, the integer combinations of `β` and `2π`
come within any `δ` of any `θ`, by the dense-or-cyclic dichotomy for subgroups of the line. -/
theorem dense_angles {β : ℝ} (hβ : Irrational (β / Real.pi)) (θ δ : ℝ) (hδ : 0 < δ) :
    ∃ k m : ℤ, |(k : ℝ) * β + m * (2 * Real.pi) - θ| < δ := by
  have hd : Dense ((AddSubgroup.closure ({β, 2 * Real.pi} : Set ℝ) : AddSubgroup ℝ) : Set ℝ) := by
    rcases AddSubgroup.dense_or_cyclic (AddSubgroup.closure ({β, 2 * Real.pi} : Set ℝ)) with
      h | ⟨c, hc⟩
    · exact h
    · exfalso
      have hβ' : β ∈ AddSubgroup.closure ({β, 2 * Real.pi} : Set ℝ) :=
        AddSubgroup.subset_closure (by simp)
      have hπ' : 2 * Real.pi ∈ AddSubgroup.closure ({β, 2 * Real.pi} : Set ℝ) :=
        AddSubgroup.subset_closure (by simp)
      rw [hc, AddSubgroup.mem_closure_singleton] at hβ' hπ'
      obtain ⟨a, ha⟩ := hβ'
      obtain ⟨b, hb⟩ := hπ'
      rw [zsmul_eq_mul] at ha hb
      have hb0 : (b : ℝ) ≠ 0 := by
        rintro h0; rw [h0, zero_mul] at hb; linarith [Real.pi_pos]
      apply hβ
      refine ⟨(2 * a / b : ℚ), ?_⟩
      have hπ0 : Real.pi ≠ 0 := Real.pi_ne_zero
      push_cast
      field_simp
      linear_combination b * ha - a * hb
  obtain ⟨x, hx1, hx2⟩ := Metric.dense_iff.mp hd θ δ hδ
  obtain ⟨k, m, hkm⟩ := AddSubgroup.mem_closure_pair.mp hx2
  refine ⟨k, m, ?_⟩
  rw [Metric.mem_ball, Real.dist_eq] at hx1
  rw [zsmul_eq_mul, zsmul_eq_mul] at hkm
  rw [hkm]; exact hx1

variable {n : ℕ}

theorem unitary_mul {S : Type} [Fintype S] [DecidableEq S] {A B : Matrix S S ℂ}
    (hA : Aᴴ * A = 1) (hB : Bᴴ * B = 1) : (A * B)ᴴ * (A * B) = 1 := by
  rw [Matrix.conjTranspose_mul, Matrix.mul_assoc, ← Matrix.mul_assoc Aᴴ, hA, Matrix.one_mul, hB]

theorem S2_conjTranspose_eq_cube : S2ᴴ = S2 * S2 * S2 := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [S2, Matrix.mul_apply, Fin.sum_univ_two, Matrix.conjTranspose_apply, Complex.conj_I]

/-- **A BLOCK REPERTOIRE**: a set of matrices at level `n` containing the identity, closed under
products, and containing the addressed rotation by `β`, the addressed quarter phase and the
addressed exchange on the block `k₀`. -/
structure BlockRepertoire (k₀ : Fin n) (β : ℝ)
    (A : Set (Matrix (Fin 2 × Fin n) (Fin 2 × Fin n) ℂ)) : Prop where
  one_mem : (1 : Matrix (Fin 2 × Fin n) (Fin 2 × Fin n) ℂ) ∈ A
  mul_mem : ∀ {V W}, V ∈ A → W ∈ A → V * W ∈ A
  rot_mem : blockOf k₀ (StateMixingCoupling.rot β) ∈ A
  phase_mem : blockOf k₀ S2 ∈ A
  swap_mem : blockOf k₀ X2 ∈ A

namespace BlockRepertoire

variable {k₀ : Fin n} {β : ℝ} {A : Set (Matrix (Fin 2 × Fin n) (Fin 2 × Fin n) ℂ)}

theorem rot_nat_mem (h : BlockRepertoire k₀ β A) :
    ∀ k : ℕ, blockOf k₀ (StateMixingCoupling.rot (k * β)) ∈ A
  | 0 => by simpa [rot_zero, blockOf_one] using h.one_mem
  | k + 1 => by
      have := h.mul_mem (h.rot_nat_mem k) h.rot_mem
      rwa [blockOf_mul, rot_mul, show (k : ℝ) * β + β = ((k + 1 : ℕ) : ℝ) * β by push_cast; ring]
        at this

theorem rot_neg_mem (h : BlockRepertoire k₀ β A) {θ : ℝ}
    (hθ : blockOf k₀ (StateMixingCoupling.rot θ) ∈ A) :
    blockOf k₀ (StateMixingCoupling.rot (-θ)) ∈ A := by
  have := h.mul_mem (h.mul_mem h.swap_mem hθ) h.swap_mem
  rwa [blockOf_mul, blockOf_mul, X2_rot_X2] at this

theorem rot_int_mem (h : BlockRepertoire k₀ β A) (k : ℤ) :
    blockOf k₀ (StateMixingCoupling.rot (k * β)) ∈ A := by
  obtain ⟨m, hm | hm⟩ := Int.eq_nat_or_neg k
  · subst hm; exact_mod_cast h.rot_nat_mem m
  · subst hm
    have := h.rot_neg_mem (h.rot_nat_mem m)
    rw [Int.cast_neg, Int.cast_natCast, neg_mul]; exact this

/-- **THE ROTATIONS ARE APPROXIMATED** at every angle, within any `δ`, by the repertoire. -/
theorem rot_approx (h : BlockRepertoire k₀ β A) (hβ : Irrational (β / Real.pi)) (θ δ : ℝ)
    (hδ : 0 < δ) : ∃ V ∈ A, Vᴴ * V = 1 ∧ ‖blockOf k₀ (StateMixingCoupling.rot θ) - V‖ < δ := by
  obtain ⟨k, m, hkm⟩ := dense_angles hβ θ δ hδ
  refine ⟨blockOf k₀ (StateMixingCoupling.rot (k * β)), h.rot_int_mem k,
    blockOf_unitary k₀ (rot_unitary _), ?_⟩
  calc ‖blockOf k₀ (StateMixingCoupling.rot θ) - blockOf k₀ (StateMixingCoupling.rot (k * β))‖
      = ‖blockOf k₀ (StateMixingCoupling.rot θ)
          - blockOf k₀ (StateMixingCoupling.rot (k * β + m * (2 * Real.pi)))‖ := by
        rw [rot_add_int_mul_two_pi]
    _ ≤ |θ - (k * β + m * (2 * Real.pi))| := blockOf_rot_dist_le k₀ _ _
    _ < δ := by rw [abs_sub_comm]; exact hkm

theorem phase_conj_mem (h : BlockRepertoire k₀ β A) : blockOf k₀ S2ᴴ ∈ A := by
  rw [S2_conjTranspose_eq_cube, ← blockOf_mul, ← blockOf_mul]
  exact h.mul_mem (h.mul_mem h.phase_mem h.phase_mem) h.phase_mem

/-- **THE PERPENDICULAR ROTATIONS ARE APPROXIMATED** too, by quarter-phase conjugation. -/
theorem rx_approx (h : BlockRepertoire k₀ β A) (hβ : Irrational (β / Real.pi)) (θ δ : ℝ)
    (hδ : 0 < δ) : ∃ V ∈ A, Vᴴ * V = 1 ∧ ‖blockOf k₀ (rx θ) - V‖ < δ := by
  have : Nonempty (Fin 2 × Fin n) := ⟨(0, k₀)⟩
  obtain ⟨V, hVA, hVu, hV⟩ := h.rot_approx hβ θ δ hδ
  have hS : (blockOf k₀ S2)ᴴ * blockOf k₀ S2 = 1 := blockOf_unitary k₀ S2_unitary
  have hS' : (blockOf k₀ S2ᴴ)ᴴ * blockOf k₀ S2ᴴ = 1 := by
    rw [blockOf_conjTranspose, Matrix.conjTranspose_conjTranspose, blockOf_mul,
      mul_eq_one_comm.mp S2_unitary, blockOf_one]
  refine ⟨blockOf k₀ S2 * V * blockOf k₀ S2ᴴ, h.mul_mem (h.mul_mem h.phase_mem hVA) h.phase_conj_mem,
    unitary_mul (unitary_mul hS hVu) hS', ?_⟩
  rw [← rx_eq_conj, ← blockOf_mul, ← blockOf_mul]
  have e : blockOf k₀ S2 * blockOf k₀ (StateMixingCoupling.rot θ) * blockOf k₀ S2ᴴ
      - blockOf k₀ S2 * V * blockOf k₀ S2ᴴ
      = blockOf k₀ S2 * (blockOf k₀ (StateMixingCoupling.rot θ) - V) * blockOf k₀ S2ᴴ := by
    simp only [Matrix.mul_sub, Matrix.sub_mul]
  rw [e, norm_mul_unitary_right hS', norm_mul_unitary_left hS]
  exact hV

/-- **DENSITY OF THE SPECIAL-UNITARY BLOCK**: every addressed special unitary is within any `ε`
of a unitary of the repertoire, through the Euler decomposition and three approximations. -/
theorem dense_block_su2 (h : BlockRepertoire k₀ β A) (hβ : Irrational (β / Real.pi))
    {M : Matrix (Fin 2) (Fin 2) ℂ} (hM : Mᴴ * M = 1) (hdet : M.det = 1) (ε : ℝ) (hε : 0 < ε) :
    ∃ V ∈ A, Vᴴ * V = 1 ∧ ‖blockOf k₀ M - V‖ < ε := by
  have : Nonempty (Fin 2 × Fin n) := ⟨(0, k₀)⟩
  obtain ⟨h11, h01⟩ := su2_form hM hdet
  have e1 := congrFun (congrFun hM 0) 0
  simp only [Matrix.mul_apply, Fin.sum_univ_two, Matrix.conjTranspose_apply, Matrix.one_apply,
    Fin.isValue, if_true, Complex.star_def] at e1
  have hpq : ‖M 0 0‖ ^ 2 + ‖M 1 0‖ ^ 2 = 1 := by
    rw [mul_comm ((starRingEnd ℂ) (M 0 0)), mul_comm ((starRingEnd ℂ) (M 1 0)), Complex.mul_conj,
      Complex.mul_conj, Complex.normSq_eq_norm_sq, Complex.normSq_eq_norm_sq] at e1
    exact_mod_cast e1
  obtain ⟨a, b, c, habc⟩ := euler_of_su2 (M 0 0) (M 1 0) hpq
  have hMabc : M = StateMixingCoupling.rot a * rx b * StateMixingCoupling.rot c := by
    rw [habc]; ext i j; fin_cases i <;> fin_cases j <;> simp [h11, h01]
  have hε3 : 0 < ε / 3 := by positivity
  obtain ⟨Va, hVaA, hVau, hVa⟩ := h.rot_approx hβ a (ε / 3) hε3
  obtain ⟨Vb, hVbA, hVbu, hVb⟩ := h.rx_approx hβ b (ε / 3) hε3
  obtain ⟨Vc, hVcA, hVcu, hVc⟩ := h.rot_approx hβ c (ε / 3) hε3
  refine ⟨Va * Vb * Vc, h.mul_mem (h.mul_mem hVaA hVbA) hVcA, unitary_mul (unitary_mul hVau hVbu) hVcu,
    ?_⟩
  rw [hMabc, ← blockOf_mul, ← blockOf_mul]
  have hra : (blockOf k₀ (StateMixingCoupling.rot a))ᴴ * blockOf k₀ (StateMixingCoupling.rot a) = 1 :=
    blockOf_unitary k₀ (rot_unitary a)
  have hrb : (blockOf k₀ (rx b))ᴴ * blockOf k₀ (rx b) = 1 := blockOf_unitary k₀ (rx_unitary b)
  calc ‖blockOf k₀ (StateMixingCoupling.rot a) * blockOf k₀ (rx b) * blockOf k₀ (StateMixingCoupling.rot c)
        - Va * Vb * Vc‖
      ≤ ‖blockOf k₀ (StateMixingCoupling.rot a) * blockOf k₀ (rx b) - Va * Vb‖
          + ‖blockOf k₀ (StateMixingCoupling.rot c) - Vc‖ :=
        norm_mul_sub_mul_le (unitary_mul hra hrb) hVcu
    _ ≤ ‖blockOf k₀ (StateMixingCoupling.rot a) - Va‖ + ‖blockOf k₀ (rx b) - Vb‖
          + ‖blockOf k₀ (StateMixingCoupling.rot c) - Vc‖ := by
        gcongr; exact norm_mul_sub_mul_le hra hVbu
    _ < ε / 3 + ε / 3 + ε / 3 := by gcongr
    _ = ε := by ring

end BlockRepertoire

end Density

/-! ### Section F — the available repertoire of a theory, and level one -/

section Theory

variable (T : FiniteOperationalTheory (Fin 2))

/-- **THE AVAILABLE UNIT CONJUGATIONS AT LEVEL `n`**, as a set of matrices. -/
def availSet (n : ℕ) : Set (Matrix (Fin 2 × Fin n) (Fin 2 × Fin n) ℂ) :=
  {V | T.availExt n Unit (fun _ => conjChannel V)}

theorem mem_availSet {n : ℕ} {V : Matrix (Fin 2 × Fin n) (Fin 2 × Fin n) ℂ} :
    V ∈ availSet T n ↔ T.availExt n Unit (fun _ => conjChannel V) := Iff.rfl

/-- The identity is available at every level: at level zero trivially, above it as the exchange
of a configuration with itself. -/
theorem one_mem_availSet (hd : DerivedOI T) (n : ℕ) :
    (1 : Matrix (Fin 2 × Fin n) (Fin 2 × Fin n) ℂ) ∈ availSet T n := by
  rcases Nat.eq_zero_or_pos n with rfl | hn
  · exact availExt_zero T _
  · have h := hd.2.2.1 n (0, ⟨0, hn⟩) (0, ⟨0, hn⟩)
    have h1 : permMatrix (Equiv.swap ((0 : Fin 2), (⟨0, hn⟩ : Fin n)) (0, ⟨0, hn⟩)) = 1 := by
      rw [Equiv.swap_self]; exact permMatrix_one'
    rw [h1] at h
    exact h

theorem mul_mem_availSet {n : ℕ} {V W : Matrix (Fin 2 × Fin n) (Fin 2 × Fin n) ℂ}
    (hV : V ∈ availSet T n) (hW : W ∈ availSet T n) : V * W ∈ availSet T n :=
  avail_conj_mul T n hV hW

variable {n : ℕ}

/-- **THE STATED QUARTER PHASE ON `(1, k₀)` IS THE ADDRESSED QUARTER PHASE.** -/
theorem phaseGate_eq_blockOf (k₀ : Fin n) : phaseGate ((1 : Fin 2), k₀) = blockOf k₀ S2 := by
  ext ⟨x, k⟩ ⟨y, l⟩
  simp only [phaseGate, Matrix.diagonal_apply, blockOf, Matrix.add_apply, tensorOf_apply, S2,
    anc_apply, ancC, Matrix.sub_apply, Matrix.one_apply, Prod.mk.injEq]
  fin_cases x <;> fin_cases y <;> by_cases hkl : k = l <;> by_cases hk : k = k₀ <;>
    by_cases hl : l = k₀ <;> simp_all [eq_comm]

/-- **THE STATED EXCHANGE OF `(0, k₀)` AND `(1, k₀)` IS THE ADDRESSED EXCHANGE.** -/
theorem swapMatrix_eq_blockOf (k₀ : Fin n) :
    permMatrix (Equiv.swap ((0 : Fin 2), k₀) (1, k₀)) = blockOf k₀ X2 := by
  ext ⟨x, k⟩ ⟨y, l⟩
  simp only [permMatrix, Equiv.swap_apply_def, blockOf, Matrix.add_apply, tensorOf_apply, X2,
    anc_apply, ancC, Matrix.sub_apply, Matrix.one_apply, Prod.mk.injEq]
  fin_cases x <;> fin_cases y <;> by_cases hkl : k = l <;> by_cases hk : k = k₀ <;>
    by_cases hl : l = k₀ <;> simp_all [eq_comm]

theorem anc_fin_one : anc (0 : Fin 1) = 1 := by
  ext i j; fin_cases i; fin_cases j; simp [anc_apply]

theorem blockOf_fin_one (M : Matrix (Fin 2) (Fin 2) ℂ) :
    blockOf (0 : Fin 1) M = tensorOf M (1 : Matrix (Fin 1) (Fin 1) ℂ) := by
  rw [blockOf, anc_fin_one, ancC, anc_fin_one, sub_self, tensorOf_zero_right, add_zero]

/-- At level one the fixed gate is the addressed rotation. -/
theorem mixImage_one_eq_blockOf (α : ℝ) :
    mixImage 1 α = blockOf (0 : Fin 1) (StateMixingCoupling.rot α) := by
  rw [blockOf_fin_one, mixImage_eq_tensorOf]

/-- **THE LEVEL-ONE REPERTOIRE**: under the closure and the fixed gate, the available set at
level one is a block repertoire at the fixed angle. -/
theorem blockRepertoire_levelOne (hd : DerivedOI T) {α : ℝ} (hg : FixedGateSourced α T) :
    BlockRepertoire (0 : Fin 1) α (availSet T 1) where
  one_mem := one_mem_availSet T hd 1
  mul_mem := fun hV hW => mul_mem_availSet T hV hW
  rot_mem := by rw [← mixImage_one_eq_blockOf]; exact hg 1
  phase_mem := by rw [← phaseGate_eq_blockOf]; exact hd.2.2.2.1 1 (1, 0)
  swap_mem := by rw [← swapMatrix_eq_blockOf]; exact hd.2.2.1 1 (0, 0) (1, 0)

theorem levelOne_eq_tensorOf (U : Matrix (Fin 2 × Fin 1) (Fin 2 × Fin 1) ℂ) :
    U = tensorOf (Matrix.of fun i j => U (i, 0) (j, 0)) (1 : Matrix (Fin 1) (Fin 1) ℂ) := by
  ext ⟨x, k⟩ ⟨y, l⟩
  have hk : k = 0 := Subsingleton.elim _ _
  have hl : l = 0 := Subsingleton.elim _ _
  subst hk hl
  simp [tensorOf_apply]

theorem levelOne_restrict_unitary {U : Matrix (Fin 2 × Fin 1) (Fin 2 × Fin 1) ℂ} (hU : Uᴴ * U = 1) :
    (Matrix.of fun i j => U (i, 0) (j, 0))ᴴ * (Matrix.of fun i j => U (i, 0) (j, 0)) = 1 := by
  ext i j
  have h := congrFun (congrFun hU (i, 0)) (j, 0)
  simp only [Matrix.mul_apply, Matrix.conjTranspose_apply, Fintype.sum_prod_type,
    Fin.sum_univ_one, Matrix.one_apply, Prod.mk.injEq, and_true] at h
  simpa [Matrix.mul_apply, Matrix.conjTranspose_apply, Matrix.one_apply] using h

/-- **T4, LEVEL ONE**: under the closure and one fixed gate at an angle with `α/π` irrational,
every unitary at level one is approximated up to a unit scalar by an available unitary. -/
theorem levelOne_dense (hd : DerivedOI T) {α : ℝ} (hα : Irrational (α / Real.pi))
    (hg : FixedGateSourced α T) (U : Matrix (Fin 2 × Fin 1) (Fin 2 × Fin 1) ℂ) (hU : Uᴴ * U = 1)
    (ε : ℝ) (hε : 0 < ε) :
    ∃ (V : Matrix (Fin 2 × Fin 1) (Fin 2 × Fin 1) ℂ) (c : ℂ), Vᴴ * V = 1 ∧ ‖c‖ = 1
      ∧ T.availExt 1 Unit (fun _ => conjChannel V) ∧ ‖U - c • V‖ < ε := by
  set M := Matrix.of fun i j => U (i, 0) (j, 0) with hM
  have hMU : U = tensorOf M 1 := levelOne_eq_tensorOf U
  have hMu : Mᴴ * M = 1 := levelOne_restrict_unitary hU
  obtain ⟨s, hs, hN, hdet⟩ := exists_unit_scalar_su2 hMu
  obtain ⟨V, hVA, hVu, hV⟩ := (blockRepertoire_levelOne T hd hg).dense_block_su2 hα hN hdet ε hε
  refine ⟨V, s, hVu, hs, hVA, ?_⟩
  have hs0 : s ≠ 0 := by
    intro h; rw [h, norm_zero] at hs; exact zero_ne_one hs
  have hU' : U = s • blockOf (0 : Fin 1) (s⁻¹ • M) := by
    rw [blockOf_fin_one, tensorOf_smul_left, smul_smul, mul_inv_cancel₀ hs0, one_smul, hMU]
  rw [hU', ← smul_sub, norm_smul, hs, one_mul]
  exact hV

end Theory

/-! ### Section G — T6: isolation by the sign echo, relocation by the exchanges -/

section AllLevels

variable (T : FiniteOperationalTheory (Fin 2)) {n : ℕ}

/-- The product of the sign flips over a finite set of configurations. -/
def flipSet (s : Finset (Fin 2 × Fin n)) : Matrix (Fin 2 × Fin n) (Fin 2 × Fin n) ℂ :=
  Matrix.diagonal fun p => if p ∈ s then -1 else 1

theorem flipSet_avail (hd : DerivedOI T) (s : Finset (Fin 2 × Fin n)) :
    flipSet s ∈ availSet T n := by
  induction s using Finset.induction_on with
  | empty =>
    have : flipSet (∅ : Finset (Fin 2 × Fin n)) = 1 := by
      ext i j
      by_cases h : i = j
      · subst h; simp [flipSet]
      · simp [flipSet, Matrix.diagonal_apply_ne _ h, Matrix.one_apply_ne h]
    rw [this]
    exact one_mem_availSet T hd n
  | insert a s ha ih =>
    have : flipSet (insert a s) = Matrix.diagonal (flipAt a) * flipSet s := by
      rw [flipSet, flipSet, Matrix.diagonal_mul_diagonal]
      congr 1
      funext p
      by_cases hp : p = a
      · subst hp; simp [flipAt, ha]
      · simp [flipAt, hp]
    rw [this]
    exact mul_mem_availSet T (flip_avail T hd.2.2.2.1 n a) ih

/-- The sign flip on the second value. -/
def Z2 : Matrix (Fin 2) (Fin 2) ℂ := !![1, 0; 0, -1]

theorem Z2_rot_Z2 (θ : ℝ) : Z2 * StateMixingCoupling.rot θ * Z2 = StateMixingCoupling.rot (-θ) := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [Z2, StateMixingCoupling.rot, Matrix.mul_apply, Fin.sum_univ_two, Real.cos_neg, Real.sin_neg]

/-- The echo flips: the sign flip on every configuration with site value one and ancilla value
other than `k₀`. -/
def echoSet (k₀ : Fin n) : Finset (Fin 2 × Fin n) :=
  Finset.univ.filter fun p => p.1 = 1 ∧ p.2 ≠ k₀

theorem flipSet_echoSet (k₀ : Fin n) :
    flipSet (echoSet k₀) = tensorOf Z2 (ancC k₀) + tensorOf 1 (anc k₀) := by
  ext ⟨x, k⟩ ⟨y, l⟩
  simp only [flipSet, echoSet, Matrix.diagonal_apply, Finset.mem_filter, Finset.mem_univ, true_and,
    Matrix.add_apply, tensorOf_apply, Z2, anc_apply, ancC, Matrix.sub_apply, Matrix.one_apply,
    Prod.mk.injEq]
  fin_cases x <;> fin_cases y <;> by_cases hkl : k = l <;> by_cases hk : k = k₀ <;>
    by_cases hl : l = k₀ <;> simp_all [eq_comm]

theorem mixImage_eq_blocks (α : ℝ) (k₀ : Fin n) :
    mixImage n α = tensorOf (StateMixingCoupling.rot α) (anc k₀)
      + tensorOf (StateMixingCoupling.rot α) (ancC k₀) := by
  rw [mixImage_eq_tensorOf, ← tensorOf_add_right, anc_add_ancC]

/-- **THE ECHO IDENTITY**: conjugating the parallel gate by the echo flips and multiplying by the
parallel gate again cancels every unselected block and leaves the rotation by `2α` on block
`k₀`. -/
theorem echo_identity (α : ℝ) (k₀ : Fin n) :
    flipSet (echoSet k₀) * mixImage n α * flipSet (echoSet k₀) * mixImage n α
      = blockOf k₀ (StateMixingCoupling.rot (2 * α)) := by
  rw [flipSet_echoSet, mixImage_eq_blocks α k₀]
  simp only [Matrix.add_mul, Matrix.mul_add, tensorOf_mul', anc_mul_anc, anc_mul_ancC,
    ancC_mul_anc, ancC_mul_ancC, tensorOf_zero_right, add_zero, zero_add, Matrix.mul_one,
    Matrix.one_mul]
  rw [Z2_rot_Z2, rot_mul, rot_mul, neg_add_cancel, rot_zero, show α + α = 2 * α by ring]
  rfl

/-- **THE ISOLATED GATE IS AVAILABLE** at every level, on every block. -/
theorem isolated_mem_availSet (hd : DerivedOI T) {α : ℝ} (hg : FixedGateSourced α T) (k₀ : Fin n) :
    blockOf k₀ (StateMixingCoupling.rot (2 * α)) ∈ availSet T n := by
  rw [← echo_identity]
  have hF := flipSet_avail T hd (echoSet k₀)
  exact mul_mem_availSet T (mul_mem_availSet T (mul_mem_availSet T hF (hg n)) hF) (hg n)

/-- **THE REPERTOIRE ON EVERY BLOCK** at the doubled angle. -/
theorem blockRepertoire_level (hd : DerivedOI T) {α : ℝ} (hg : FixedGateSourced α T) (k₀ : Fin n) :
    BlockRepertoire k₀ (2 * α) (availSet T n) where
  one_mem := one_mem_availSet T hd n
  mul_mem := fun hV hW => mul_mem_availSet T hV hW
  rot_mem := isolated_mem_availSet T hd hg k₀
  phase_mem := by rw [← phaseGate_eq_blockOf]; exact hd.2.2.2.1 n (1, k₀)
  swap_mem := by rw [← swapMatrix_eq_blockOf]; exact hd.2.2.1 n (0, k₀) (1, k₀)

theorem irrational_two_mul {α : ℝ} (hα : Irrational (α / Real.pi)) :
    Irrational (2 * α / Real.pi) := by
  have : 2 * α / Real.pi = α / Real.pi * ((2 : ℤ) : ℝ) := by push_cast; ring
  rw [this]
  exact (irrational_mul_intCast_iff).mpr ⟨by norm_num, hα⟩

/-- **A PERMUTATION CARRYING ONE PAIR TO ANOTHER.** -/
theorem exists_perm_pair_map {S : Type} [DecidableEq S] {p₀ p₁ a b : S} (h01 : p₀ ≠ p₁)
    (hab : a ≠ b) : ∃ σ : Equiv.Perm S, σ p₀ = a ∧ σ p₁ = b := by
  have h1 : Equiv.swap p₀ a p₁ ≠ a := by
    intro h
    apply h01
    apply (Equiv.swap p₀ a).injective
    rw [Equiv.swap_apply_left, h]
  refine ⟨Equiv.swap (Equiv.swap p₀ a p₁) b * Equiv.swap p₀ a, ?_, ?_⟩
  · rw [Equiv.Perm.mul_apply, Equiv.swap_apply_left]
    exact Equiv.swap_apply_of_ne_of_ne h1.symm hab
  · rw [Equiv.Perm.mul_apply, Equiv.swap_apply_left]

/-- **THE RELOCATED GATE**: the addressed gate carried by a permutation of the configurations. -/
def relocated (σ : Equiv.Perm (Fin 2 × Fin n)) (k₀ : Fin n) (M : Matrix (Fin 2) (Fin 2) ℂ) :
    Matrix (Fin 2 × Fin n) (Fin 2 × Fin n) ℂ :=
  permMatrix σ * blockOf k₀ M * (permMatrix σ)ᴴ

theorem permMatrix_mem_availSet (hd : DerivedOI T) (hn : 0 < n) (σ : Equiv.Perm (Fin 2 × Fin n)) :
    permMatrix σ ∈ availSet T n := by
  refine avail_perm_of_ne T n ?_ (fun a b _ => hd.2.2.1 n a b) σ
  rw [Fintype.card_prod, Fintype.card_fin, Fintype.card_fin]; omega

theorem relocated_unitary (σ : Equiv.Perm (Fin 2 × Fin n)) (k₀ : Fin n)
    {M : Matrix (Fin 2) (Fin 2) ℂ} (hM : Mᴴ * M = 1) :
    (relocated σ k₀ M)ᴴ * relocated σ k₀ M = 1 := by
  have hP : (permMatrix σ)ᴴ * permMatrix σ = 1 := permMatrix_isometry σ
  have hP' : ((permMatrix σ)ᴴ)ᴴ * (permMatrix σ)ᴴ = 1 := by
    rw [Matrix.conjTranspose_conjTranspose]; exact mul_eq_one_comm.mp hP
  exact unitary_mul (unitary_mul hP (blockOf_unitary k₀ hM)) hP'

/-- **T6, TWO-LEVEL DENSITY ON EVERY PAIR**: at every positive level, every special unitary on
any pair of configurations, carried there by a permutation, is within any `ε` of an available
unitary. -/
theorem relocated_dense (hd : DerivedOI T) {α : ℝ} (hα : Irrational (α / Real.pi))
    (hg : FixedGateSourced α T) (hn : 0 < n) (σ : Equiv.Perm (Fin 2 × Fin n)) (k₀ : Fin n)
    {M : Matrix (Fin 2) (Fin 2) ℂ} (hM : Mᴴ * M = 1) (hdet : M.det = 1) (ε : ℝ) (hε : 0 < ε) :
    ∃ V ∈ availSet T n, Vᴴ * V = 1 ∧ ‖relocated σ k₀ M - V‖ < ε := by
  have : Nonempty (Fin 2 × Fin n) := ⟨(0, k₀)⟩
  obtain ⟨V₀, hV₀A, hV₀u, hV₀⟩ :=
    (blockRepertoire_level T hd hg k₀).dense_block_su2 (irrational_two_mul hα) hM hdet ε hε
  have hP : (permMatrix σ)ᴴ * permMatrix σ = 1 := permMatrix_isometry σ
  have hP' : ((permMatrix σ)ᴴ)ᴴ * (permMatrix σ)ᴴ = 1 := by
    rw [Matrix.conjTranspose_conjTranspose]; exact mul_eq_one_comm.mp hP
  have hPA : permMatrix σ ∈ availSet T n := permMatrix_mem_availSet T hd hn σ
  have hPA' : (permMatrix σ)ᴴ ∈ availSet T n := by
    rw [permMatrix_conjTranspose]; exact permMatrix_mem_availSet T hd hn σ.symm
  refine ⟨permMatrix σ * V₀ * (permMatrix σ)ᴴ, mul_mem_availSet T (mul_mem_availSet T hPA hV₀A) hPA',
    unitary_mul (unitary_mul hP hV₀u) hP', ?_⟩
  have e : relocated σ k₀ M - permMatrix σ * V₀ * (permMatrix σ)ᴴ
      = permMatrix σ * (blockOf k₀ M - V₀) * (permMatrix σ)ᴴ := by
    simp only [relocated, Matrix.mul_sub, Matrix.sub_mul]
  rw [e, norm_mul_unitary_right hP', norm_mul_unitary_left hP]
  exact hV₀

end AllLevels

/-! ### Section H — the two-level unitaries on any finite carrier, and the Givens decomposition -/

section TwoLevel

variable {S : Type} [Fintype S] [DecidableEq S]

/-- **THE INCLUSION OF THE PAIR** `(a, b)`: the two columns `e_a`, `e_b`. -/
def incl (a b : S) : Matrix S (Fin 2) ℂ :=
  Matrix.of fun s t => if (t = 0 ∧ s = a) ∨ (t = 1 ∧ s = b) then 1 else 0

omit [Fintype S] in
theorem incl_apply (a b s : S) (t : Fin 2) :
    incl a b s t = if (t = 0 ∧ s = a) ∨ (t = 1 ∧ s = b) then 1 else 0 := rfl

theorem transpose_incl_mul_incl {a b : S} (hab : a ≠ b) : (incl a b)ᵀ * incl a b = 1 := by
  ext t t'
  simp only [Matrix.mul_apply, Matrix.transpose_apply, incl_apply, Matrix.one_apply]
  fin_cases t <;> fin_cases t' <;> simp [Finset.sum_ite_eq', hab, hab.symm]

omit [Fintype S] in
theorem incl_conjTranspose (a b : S) : (incl a b)ᴴ = (incl a b)ᵀ := by
  ext t s
  simp only [Matrix.conjTranspose_apply, Matrix.transpose_apply, incl_apply]
  split_ifs <;> simp

/-- **THE TWO-LEVEL MATRIX**: `M` on the pair `(a, b)`, the identity elsewhere, in the form
`1 + ι (M − 1) ιᵀ`. -/
def twoLevel (a b : S) (M : Matrix (Fin 2) (Fin 2) ℂ) : Matrix S S ℂ :=
  1 + incl a b * (M - 1) * (incl a b)ᵀ

omit [Fintype S] in
theorem twoLevel_one (a b : S) : twoLevel a b 1 = 1 := by
  simp [twoLevel]

theorem twoLevel_mul {a b : S} (hab : a ≠ b) (M N : Matrix (Fin 2) (Fin 2) ℂ) :
    twoLevel a b M * twoLevel a b N = twoLevel a b (M * N) := by
  simp only [twoLevel]
  have key : incl a b * (M - 1) * (incl a b)ᵀ * (incl a b * (N - 1) * (incl a b)ᵀ)
      = incl a b * ((M - 1) * (N - 1)) * (incl a b)ᵀ := by
    calc incl a b * (M - 1) * (incl a b)ᵀ * (incl a b * (N - 1) * (incl a b)ᵀ)
        = incl a b * (M - 1) * ((incl a b)ᵀ * incl a b) * (N - 1) * (incl a b)ᵀ := by
          simp only [Matrix.mul_assoc]
      _ = incl a b * ((M - 1) * (N - 1)) * (incl a b)ᵀ := by
          rw [transpose_incl_mul_incl hab, Matrix.mul_one, Matrix.mul_assoc (incl a b)]
  rw [Matrix.add_mul, Matrix.mul_add, Matrix.mul_add]
  simp only [Matrix.one_mul, Matrix.mul_one]
  rw [key]
  have e : (M - 1) + (N - 1) + (M - 1) * (N - 1) = M * N - 1 := by noncomm_ring
  rw [← e]
  simp only [Matrix.mul_add, Matrix.add_mul]
  abel

omit [Fintype S] in
theorem twoLevel_conjTranspose (a b : S) (M : Matrix (Fin 2) (Fin 2) ℂ) :
    (twoLevel a b M)ᴴ = twoLevel a b Mᴴ := by
  have hι : ((incl a b)ᵀ)ᴴ = incl a b := by
    ext i j
    simp only [Matrix.conjTranspose_apply, Matrix.transpose_apply, incl_apply]
    split_ifs <;> simp
  simp only [twoLevel, Matrix.conjTranspose_add, Matrix.conjTranspose_one, Matrix.conjTranspose_mul,
    Matrix.conjTranspose_sub, incl_conjTranspose, hι, Matrix.mul_assoc]

theorem twoLevel_unitary {a b : S} (hab : a ≠ b) {M : Matrix (Fin 2) (Fin 2) ℂ} (hM : Mᴴ * M = 1) :
    (twoLevel a b M)ᴴ * twoLevel a b M = 1 := by
  rw [twoLevel_conjTranspose, twoLevel_mul hab, hM, twoLevel_one]

/-- **THE DETERMINANT OF A TWO-LEVEL MATRIX** is the determinant of its block, by Sylvester's
identity `det (1 + A B) = det (1 + B A)`. -/
theorem det_twoLevel {a b : S} (hab : a ≠ b) (M : Matrix (Fin 2) (Fin 2) ℂ) :
    (twoLevel a b M).det = M.det := by
  rw [twoLevel, Matrix.mul_assoc, Matrix.det_one_add_mul_comm, Matrix.mul_assoc (M - 1),
    transpose_incl_mul_incl hab, Matrix.mul_one, add_sub_cancel]

omit [Fintype S] in
theorem incl_mul_apply {ι : Type} {a b : S} (hab : a ≠ b) (X : Matrix (Fin 2) ι ℂ) (i : S) (j : ι) :
    (incl a b * X) i j = if i = a then X 0 j else if i = b then X 1 j else 0 := by
  simp only [Matrix.mul_apply, Fin.sum_univ_two, incl_apply]
  by_cases hia : i = a
  · subst hia; simp [hab]
  · by_cases hib : i = b
    · subst hib; simp [hia]
    · simp [hia, hib]

omit [Fintype S] in
theorem mul_transpose_incl_apply {ι : Type} {a b : S} (hab : a ≠ b) (X : Matrix ι (Fin 2) ℂ) (i : ι)
    (j : S) :
    (X * (incl a b)ᵀ) i j = if j = a then X i 0 else if j = b then X i 1 else 0 := by
  simp only [Matrix.mul_apply, Fin.sum_univ_two, Matrix.transpose_apply, incl_apply]
  by_cases hja : j = a
  · subst hja; simp [hab]
  · by_cases hjb : j = b
    · subst hjb; simp [hja]
    · simp [hja, hjb]

theorem transpose_incl_mul_apply (a b : S) (W : Matrix S S ℂ) (t : Fin 2) (j : S) :
    ((incl a b)ᵀ * W) t j = if t = 0 then W a j else W b j := by
  simp only [Matrix.mul_apply, Matrix.transpose_apply, incl_apply]
  fin_cases t <;> simp [Finset.sum_ite_eq']

/-- **THE ROW ACTION OF A TWO-LEVEL MATRIX**: rows `a` and `b` are mixed by `M`, others fixed. -/
theorem twoLevel_mul_apply {a b : S} (hab : a ≠ b) (M : Matrix (Fin 2) (Fin 2) ℂ) (W : Matrix S S ℂ)
    (i j : S) :
    (twoLevel a b M * W) i j =
      if i = a then M 0 0 * W a j + M 0 1 * W b j
      else if i = b then M 1 0 * W a j + M 1 1 * W b j else W i j := by
  rw [twoLevel, Matrix.add_mul, Matrix.one_mul, Matrix.add_apply, Matrix.mul_assoc, Matrix.mul_assoc,
    incl_mul_apply hab]
  have h0 : (((M - 1) * ((incl a b)ᵀ * W) : Matrix (Fin 2) S ℂ)) 0 j
      = (M 0 0 - 1) * W a j + M 0 1 * W b j := by
    rw [Matrix.mul_apply, Fin.sum_univ_two, transpose_incl_mul_apply, transpose_incl_mul_apply]
    simp [Matrix.sub_apply]
  have h1 : (((M - 1) * ((incl a b)ᵀ * W) : Matrix (Fin 2) S ℂ)) 1 j
      = M 1 0 * W a j + (M 1 1 - 1) * W b j := by
    rw [Matrix.mul_apply, Fin.sum_univ_two, transpose_incl_mul_apply, transpose_incl_mul_apply]
    simp [Matrix.sub_apply]
  by_cases hia : i = a
  · subst hia; rw [if_pos rfl, if_pos rfl, h0]; ring
  · by_cases hib : i = b
    · subst hib; rw [if_neg hia, if_neg hia, if_pos rfl, if_pos rfl, h1]; ring
    · rw [if_neg hia, if_neg hib, if_neg hia, if_neg hib, add_zero]

/-- **SUPPORT ON A FINITE SET**: the identity outside `R`. -/
def SuppOn (R : Finset S) (W : Matrix S S ℂ) : Prop :=
  ∀ i j, (i ∉ R ∨ j ∉ R) → W i j = (1 : Matrix S S ℂ) i j

omit [Fintype S] in
theorem suppOn_one (R : Finset S) : SuppOn R (1 : Matrix S S ℂ) := fun _ _ _ => rfl

theorem suppOn_mul {R : Finset S} {A B : Matrix S S ℂ} (hA : SuppOn R A) (hB : SuppOn R B) :
    SuppOn R (A * B) := by
  intro i j hij
  rcases hij with hi | hj
  · have hrow : ∀ k, A i k = (1 : Matrix S S ℂ) i k := fun k => hA i k (Or.inl hi)
    rw [Matrix.mul_apply, Finset.sum_congr rfl (fun k _ => by rw [hrow k])]
    simp only [Matrix.one_apply, ite_mul, one_mul, zero_mul, Finset.sum_ite_eq, Finset.mem_univ,
      if_true]
    exact hB i j (Or.inl hi)
  · have hcol : ∀ k, B k j = (1 : Matrix S S ℂ) k j := fun k => hB k j (Or.inr hj)
    rw [Matrix.mul_apply, Finset.sum_congr rfl (fun k _ => by rw [hcol k])]
    simp only [Matrix.one_apply, mul_ite, mul_one, mul_zero, Finset.sum_ite_eq', Finset.mem_univ,
      if_true]
    exact hA i j (Or.inr hj)

omit [Fintype S] in
theorem suppOn_twoLevel {R : Finset S} {a b : S} (hab : a ≠ b) (ha : a ∈ R) (hb : b ∈ R)
    (M : Matrix (Fin 2) (Fin 2) ℂ) : SuppOn R (twoLevel a b M) := by
  intro i j hij
  rw [twoLevel, Matrix.add_apply, Matrix.mul_assoc, incl_mul_apply hab]
  rcases hij with hi | hj
  · have hia : i ≠ a := fun h => hi (h ▸ ha)
    have hib : i ≠ b := fun h => hi (h ▸ hb)
    rw [if_neg hia, if_neg hib, add_zero]
  · have hja : j ≠ a := fun h => hj (h ▸ ha)
    have hjb : j ≠ b := fun h => hj (h ▸ hb)
    have h0 : ∀ t, (((M - 1) * (incl a b)ᵀ : Matrix (Fin 2) S ℂ)) t j = 0 := by
      intro t; rw [mul_transpose_incl_apply hab, if_neg hja, if_neg hjb]
    split_ifs <;> simp [h0]

omit [Fintype S] in
theorem suppOn_mono {R R' : Finset S} (h : R ⊆ R') {W : Matrix S S ℂ} (hW : SuppOn R W) :
    SuppOn R' W := by
  intro i j hij
  apply hW
  rcases hij with hi | hj
  · exact Or.inl fun h' => hi (h h')
  · exact Or.inr fun h' => hj (h h')

/-- **THE GIVENS BLOCK** carrying `(x, y)` to `(r, 0)`, with `r = √(|x|² + |y|²)`. -/
noncomputable def givens (x y : ℂ) : Matrix (Fin 2) (Fin 2) ℂ :=
  if ‖x‖ ^ 2 + ‖y‖ ^ 2 = 0 then 1
  else (((Real.sqrt (‖x‖ ^ 2 + ‖y‖ ^ 2))⁻¹ : ℝ) : ℂ) • !![(starRingEnd ℂ) x, (starRingEnd ℂ) y; -y, x]

/-- The Gram matrix of the unnormalized Givens block is the scalar `|x|² + |y|²`. -/
theorem givens_block_gram (x y : ℂ) :
    (!![(starRingEnd ℂ) x, (starRingEnd ℂ) y; -y, x])ᴴ * !![(starRingEnd ℂ) x, (starRingEnd ℂ) y; -y, x]
      = ((‖x‖ ^ 2 + ‖y‖ ^ 2 : ℝ) : ℂ) • (1 : Matrix (Fin 2) (Fin 2) ℂ) := by
  have hx : (starRingEnd ℂ) x * x = (‖x‖ : ℂ) ^ 2 := by
    rw [mul_comm, Complex.mul_conj, Complex.normSq_eq_norm_sq, Complex.ofReal_pow]
  have hy : (starRingEnd ℂ) y * y = (‖y‖ : ℂ) ^ 2 := by
    rw [mul_comm, Complex.mul_conj, Complex.normSq_eq_norm_sq, Complex.ofReal_pow]
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [Matrix.mul_apply, Fin.sum_univ_two, Matrix.conjTranspose_apply] <;>
    first | linear_combination hx + hy | ring

theorem givens_kill (x y : ℂ) : givens x y 1 0 * x + givens x y 1 1 * y = 0 := by
  unfold givens
  split_ifs with h
  · have hy : y = 0 := by
      have := norm_nonneg x; have := norm_nonneg y
      have hy2 : ‖y‖ ^ 2 = 0 := by nlinarith
      simpa using hy2
    simp [hy]
  · simp only [Matrix.smul_apply, Matrix.of_apply, Matrix.cons_val', Matrix.cons_val_one,
      Matrix.cons_val_zero, Matrix.empty_val', Matrix.cons_val_fin_one, smul_eq_mul, Fin.isValue]
    ring

theorem givens_scalar_sq (x y : ℂ) (h : ¬ ‖x‖ ^ 2 + ‖y‖ ^ 2 = 0) :
    (((Real.sqrt (‖x‖ ^ 2 + ‖y‖ ^ 2))⁻¹ : ℝ) : ℂ) * (((Real.sqrt (‖x‖ ^ 2 + ‖y‖ ^ 2))⁻¹ : ℝ) : ℂ)
      * ((‖x‖ ^ 2 + ‖y‖ ^ 2 : ℝ) : ℂ) = 1 := by
  have hpos : 0 < ‖x‖ ^ 2 + ‖y‖ ^ 2 := lt_of_le_of_ne (by positivity) (Ne.symm h)
  have hs : Real.sqrt (‖x‖ ^ 2 + ‖y‖ ^ 2) ^ 2 = ‖x‖ ^ 2 + ‖y‖ ^ 2 := Real.sq_sqrt hpos.le
  rw [← Complex.ofReal_mul, ← Complex.ofReal_mul, ← Complex.ofReal_one]
  congr 1
  rw [← sq, inv_pow, hs, inv_mul_cancel₀ hpos.ne']

theorem givens_unitary (x y : ℂ) : (givens x y)ᴴ * givens x y = 1 := by
  unfold givens
  split_ifs with h
  · simp
  · rw [Matrix.conjTranspose_smul, Matrix.smul_mul, Matrix.mul_smul, smul_smul, givens_block_gram,
      smul_smul, Complex.star_def, Complex.conj_ofReal, givens_scalar_sq x y h, one_smul]

theorem det_givens (x y : ℂ) : (givens x y).det = 1 := by
  unfold givens
  split_ifs with h
  · simp
  · have hx : (starRingEnd ℂ) x * x = (‖x‖ : ℂ) ^ 2 := by
      rw [mul_comm, Complex.mul_conj, Complex.normSq_eq_norm_sq, Complex.ofReal_pow]
    have hy : (starRingEnd ℂ) y * y = (‖y‖ : ℂ) ^ 2 := by
      rw [mul_comm, Complex.mul_conj, Complex.normSq_eq_norm_sq, Complex.ofReal_pow]
    rw [Matrix.det_smul, Fintype.card_fin, Matrix.det_fin_two_of]
    have e : (starRingEnd ℂ) x * x - (starRingEnd ℂ) y * -y = ((‖x‖ ^ 2 + ‖y‖ ^ 2 : ℝ) : ℂ) := by
      push_cast; linear_combination hx + hy
    rw [e, sq, givens_scalar_sq x y h]

/-- **THE TWO-LEVEL SPECIAL UNITARIES** on a carrier. -/
def TwoLevelSU (V : Matrix S S ℂ) : Prop :=
  ∃ (a b : S) (M : Matrix (Fin 2) (Fin 2) ℂ), a ≠ b ∧ Mᴴ * M = 1 ∧ M.det = 1 ∧ V = twoLevel a b M

omit [Fintype S] in
theorem twoLevelSU_conjTranspose {V : Matrix S S ℂ} (h : TwoLevelSU V) : TwoLevelSU Vᴴ := by
  obtain ⟨a, b, M, hab, hM, hdet, rfl⟩ := h
  refine ⟨a, b, Mᴴ, hab, ?_, ?_, twoLevel_conjTranspose a b M⟩
  · rw [Matrix.conjTranspose_conjTranspose]; exact mul_eq_one_comm.mp hM
  · rw [Matrix.det_conjTranspose, hdet, star_one]

theorem conjTranspose_mem_closure {Q : Matrix S S ℂ}
    (hQ : Q ∈ Submonoid.closure {V : Matrix S S ℂ | TwoLevelSU V}) :
    Qᴴ ∈ Submonoid.closure {V : Matrix S S ℂ | TwoLevelSU V} := by
  induction hQ using Submonoid.closure_induction with
  | mem x hx => exact Submonoid.subset_closure (twoLevelSU_conjTranspose hx)
  | one => rw [Matrix.conjTranspose_one]; exact Submonoid.one_mem _
  | mul x y _ _ hx hy => rw [Matrix.conjTranspose_mul]; exact Submonoid.mul_mem _ hy hx

/-- **A UNITARY WHOSE COLUMN `a` IS SUPPORTED AT `a` HAS ROW `a` SUPPORTED AT `a`.** -/
theorem row_zero_of_col_zero {W : Matrix S S ℂ} (hW : Wᴴ * W = 1) (a : S)
    (hcol : ∀ i, i ≠ a → W i a = 0) : ∀ j, j ≠ a → W a j = 0 := by
  have hWW : W * Wᴴ = 1 := mul_eq_one_comm.mp hW
  have hnorm : W a a * (starRingEnd ℂ) (W a a) = 1 := by
    have h := congrFun (congrFun hW a) a
    simp only [Matrix.mul_apply, Matrix.conjTranspose_apply, Matrix.one_apply, if_true,
      Complex.star_def] at h
    rw [Finset.sum_eq_single a] at h
    · rw [mul_comm] at h; exact h
    · intro i _ hi; rw [hcol i hi]; simp
    · intro h'; exact absurd (Finset.mem_univ _) h'
  have hrow := congrFun (congrFun hWW a) a
  simp only [Matrix.mul_apply, Matrix.conjTranspose_apply, Matrix.one_apply, if_true,
    Complex.star_def] at hrow
  rw [← Finset.add_sum_erase _ _ (Finset.mem_univ a), hnorm] at hrow
  have hsum : ∑ j ∈ Finset.univ.erase a, W a j * (starRingEnd ℂ) (W a j) = 0 := by
    linear_combination hrow
  have hsum' : ∑ j ∈ Finset.univ.erase a, Complex.normSq (W a j) = 0 := by
    have h := congrArg Complex.re hsum
    simpa [Complex.mul_conj, Complex.re_sum] using h
  intro j hj
  have := (Finset.sum_eq_zero_iff_of_nonneg fun j _ => Complex.normSq_nonneg (W a j)).mp hsum' j
    (Finset.mem_erase.mpr ⟨hj, Finset.mem_univ _⟩)
  exact Complex.normSq_eq_zero.mp this

/-- The unit modulus of the single column entry. -/
theorem col_entry_unit {W : Matrix S S ℂ} (hW : Wᴴ * W = 1) (a : S)
    (hcol : ∀ i, i ≠ a → W i a = 0) : (starRingEnd ℂ) (W a a) * W a a = 1 := by
  have h := congrFun (congrFun hW a) a
  simp only [Matrix.mul_apply, Matrix.conjTranspose_apply, Matrix.one_apply, if_true,
    Complex.star_def] at h
  rw [Finset.sum_eq_single a] at h
  · exact h
  · intro i _ hi; rw [hcol i hi]; simp
  · intro h'; exact absurd (Finset.mem_univ _) h'

/-- The special-unitary diagonal block pushing a unit phase from `a` to `b`. -/
def phaseBlock (u : ℂ) : Matrix (Fin 2) (Fin 2) ℂ := !![(starRingEnd ℂ) u, 0; 0, u]

theorem phaseBlock_unitary {u : ℂ} (hu : (starRingEnd ℂ) u * u = 1) :
    (phaseBlock u)ᴴ * phaseBlock u = 1 := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [phaseBlock, Matrix.mul_apply, Fin.sum_univ_two, Matrix.conjTranspose_apply] <;>
    first | (rw [mul_comm]; exact hu) | exact hu

theorem det_phaseBlock {u : ℂ} (hu : (starRingEnd ℂ) u * u = 1) : (phaseBlock u).det = 1 := by
  rw [phaseBlock, Matrix.det_fin_two_of, mul_zero, sub_zero]; exact hu

/-- **THE GIVENS DECOMPOSITION**: a special unitary supported on `R` is a product of two-level
special unitaries, by induction on `R`: the column of one index is cleared by Givens blocks, the
remaining unit phase is pushed onto another index by a diagonal special-unitary block, and the
matrix that remains is supported on the rest. -/
theorem su_mem_closure_of_suppOn (R : Finset S) :
    ∀ W : Matrix S S ℂ, Wᴴ * W = 1 → W.det = 1 → SuppOn R W →
      W ∈ Submonoid.closure {V : Matrix S S ℂ | TwoLevelSU V} := by
  induction R using Finset.induction_on with
  | empty =>
    intro W _ _ hsupp
    have : W = 1 := by
      ext i j; exact hsupp i j (Or.inl (by simp))
    rw [this]; exact Submonoid.one_mem _
  | insert a R' haR' ih =>
    intro W hW hdet hsupp
    -- clear column `a` below the diagonal, one Givens block per index of `R'`
    have inner : ∀ P : Finset S, P ⊆ R' →
        ∃ Q : Matrix S S ℂ, Q ∈ Submonoid.closure {V : Matrix S S ℂ | TwoLevelSU V}
          ∧ Qᴴ * Q = 1 ∧ Q.det = 1 ∧ SuppOn (insert a R') Q ∧ ∀ b ∈ P, (Q * W) b a = 0 := by
      intro P
      induction P using Finset.induction_on with
      | empty =>
        intro _
        exact ⟨1, Submonoid.one_mem _, by simp, Matrix.det_one, suppOn_one _,
          fun b hb => absurd hb (by simp)⟩
      | insert b P hbP ihP =>
        intro hPR
        obtain ⟨Q, hQc, hQu, hQd, hQs, hQz⟩ := ihP fun x hx => hPR (Finset.mem_insert_of_mem hx)
        have hbR : b ∈ R' := hPR (Finset.mem_insert_self b P)
        have hab : a ≠ b := fun h => haR' (h ▸ hbR)
        set M := givens ((Q * W) a a) ((Q * W) b a) with hMdef
        have hMmem : TwoLevelSU (twoLevel a b M) :=
          ⟨a, b, M, hab, givens_unitary _ _, det_givens _ _, rfl⟩
        refine ⟨twoLevel a b M * Q,
          Submonoid.mul_mem _ (Submonoid.subset_closure hMmem) hQc,
          unitary_mul (twoLevel_unitary hab (givens_unitary _ _)) hQu,
          by rw [Matrix.det_mul, det_twoLevel hab, det_givens, hQd, one_mul],
          suppOn_mul (suppOn_twoLevel hab (Finset.mem_insert_self a R')
            (Finset.mem_insert_of_mem hbR) M) hQs, ?_⟩
        intro b' hb'
        rw [Matrix.mul_assoc, twoLevel_mul_apply hab]
        rcases Finset.mem_insert.mp hb' with rfl | hb'P
        · rw [if_neg hab.symm, if_pos rfl]; exact givens_kill _ _
        · have hb'a : b' ≠ a := fun h => haR' (h ▸ hPR (Finset.mem_insert_of_mem hb'P))
          have hb'b : b' ≠ b := fun h => hbP (h ▸ hb'P)
          rw [if_neg hb'a, if_neg hb'b]; exact hQz b' hb'P
    obtain ⟨Q, hQc, hQu, hQd, hQs, hQz⟩ := inner R' (Finset.Subset.refl _)
    set W₂ := Q * W with hW₂
    have hW₂u : W₂ᴴ * W₂ = 1 := unitary_mul hQu hW
    have hW₂d : W₂.det = 1 := by rw [hW₂, Matrix.det_mul, hQd, hdet, one_mul]
    have hW₂s : SuppOn (insert a R') W₂ := suppOn_mul hQs hsupp
    have hcol : ∀ i, i ≠ a → W₂ i a = 0 := by
      intro i hi
      by_cases hiR : i ∈ R'
      · exact hQz i hiR
      · have hi' : i ∉ insert a R' := by simp [hi, hiR]
        rw [hW₂s i a (Or.inl hi'), Matrix.one_apply_ne hi]
    have hrow : ∀ j, j ≠ a → W₂ a j = 0 := row_zero_of_col_zero hW₂u a hcol
    have hQc' : Qᴴ ∈ Submonoid.closure {V : Matrix S S ℂ | TwoLevelSU V} :=
      conjTranspose_mem_closure hQc
    have hWQ : W = Qᴴ * W₂ := by
      rw [hW₂, ← Matrix.mul_assoc, hQu, Matrix.one_mul]
    rcases Finset.eq_empty_or_nonempty R' with hR' | ⟨b₀, hb₀⟩
    · -- only the index `a` remains: the matrix is a single phase, and the determinant fixes it
      have hdiag : W₂ = Matrix.diagonal fun i => if i = a then W₂ a a else 1 := by
        ext i j
        by_cases hij : i = j
        · subst hij
          by_cases hia : i = a
          · subst hia; simp
          · rw [Matrix.diagonal_apply_eq, if_neg hia]
            have hi' : i ∉ insert a R' := by simp [hia, hR']
            rw [hW₂s i i (Or.inl hi'), Matrix.one_apply_eq]
        · rw [Matrix.diagonal_apply_ne _ hij]
          by_cases hia : i = a
          · subst hia; exact hrow j (Ne.symm hij)
          · by_cases hja : j = a
            · subst hja; exact hcol i hij
            · have hi' : i ∉ insert a R' := by simp [hia, hR']
              rw [hW₂s i j (Or.inl hi'), Matrix.one_apply_ne hij]
      have hu : W₂ a a = 1 := by
        have h := hW₂d
        rw [hdiag, Matrix.det_diagonal, Finset.prod_ite_eq' Finset.univ a] at h
        simpa using h
      have hW₂1 : W₂ = 1 := by
        rw [hdiag, hu]
        ext i j
        by_cases hij : i = j
        · subst hij; simp
        · rw [Matrix.diagonal_apply_ne _ hij, Matrix.one_apply_ne hij]
      rw [hWQ, hW₂1, Matrix.mul_one]
      exact hQc'
    · -- push the remaining phase from `a` onto `b₀`
      have hab₀ : a ≠ b₀ := fun h => haR' (h ▸ hb₀)
      have hu : (starRingEnd ℂ) (W₂ a a) * W₂ a a = 1 := col_entry_unit hW₂u a hcol
      set D := phaseBlock (W₂ a a) with hDdef
      have hDu : Dᴴ * D = 1 := phaseBlock_unitary hu
      have hDd : D.det = 1 := det_phaseBlock hu
      have hTmem : TwoLevelSU (twoLevel a b₀ D) := ⟨a, b₀, D, hab₀, hDu, hDd, rfl⟩
      have hTu : (twoLevel a b₀ D)ᴴ * twoLevel a b₀ D = 1 := twoLevel_unitary hab₀ hDu
      set W₃ := twoLevel a b₀ D * W₂ with hW₃
      have hW₃u : W₃ᴴ * W₃ = 1 := unitary_mul hTu hW₂u
      have hW₃d : W₃.det = 1 := by rw [hW₃, Matrix.det_mul, det_twoLevel hab₀, hDd, hW₂d, one_mul]
      have hD00 : D 0 0 = (starRingEnd ℂ) (W₂ a a) := rfl
      have hD01 : D 0 1 = 0 := rfl
      have hD10 : D 1 0 = 0 := rfl
      have hD11 : D 1 1 = W₂ a a := rfl
      have hW₃s : SuppOn R' W₃ := by
        intro i j hij
        rw [hW₃, twoLevel_mul_apply hab₀]
        by_cases hia : i = a
        · subst hia
          rw [if_pos rfl, hD00, hD01, zero_mul, add_zero]
          by_cases hja : j = i
          · subst hja; rw [hu, Matrix.one_apply_eq]
          · rw [hrow j hja, mul_zero, Matrix.one_apply_ne (Ne.symm hja)]
        · rw [if_neg hia]
          by_cases hib : i = b₀
          · subst hib
            rw [if_pos rfl, hD10, hD11, zero_mul, zero_add]
            rcases hij with hi | hj
            · exact absurd hb₀ hi
            · by_cases hja : j = a
              · subst hja; rw [hcol i hia, mul_zero, Matrix.one_apply_ne hia]
              · have hj' : j ∉ insert a R' := by simp [hja, hj]
                have hne : i ≠ j := by rintro rfl; exact hj hb₀
                rw [hW₂s i j (Or.inr hj'), Matrix.one_apply_ne hne, mul_zero]
          · rw [if_neg hib]
            rcases hij with hi | hj
            · have hi' : i ∉ insert a R' := by simp [hia, hi]
              exact hW₂s i j (Or.inl hi')
            · by_cases hja : j = a
              · subst hja; rw [hcol i hia, Matrix.one_apply_ne hia]
              · have hj' : j ∉ insert a R' := by simp [hja, hj]
                exact hW₂s i j (Or.inr hj')
      have hW₃c := ih W₃ hW₃u hW₃d hW₃s
      have hTc' : (twoLevel a b₀ D)ᴴ ∈ Submonoid.closure {V : Matrix S S ℂ | TwoLevelSU V} :=
        Submonoid.subset_closure (twoLevelSU_conjTranspose hTmem)
      have hWfinal : W = Qᴴ * ((twoLevel a b₀ D)ᴴ * W₃) := by
        rw [hW₃, ← Matrix.mul_assoc (twoLevel a b₀ D)ᴴ, hTu, Matrix.one_mul, hWQ]
      rw [hWfinal]
      exact Submonoid.mul_mem _ hQc' (Submonoid.mul_mem _ hTc' hW₃c)

/-- **EVERY SPECIAL UNITARY IS A PRODUCT OF TWO-LEVEL SPECIAL UNITARIES.** -/
theorem su_mem_closure_twoLevel (W : Matrix S S ℂ) (hW : Wᴴ * W = 1) (hdet : W.det = 1) :
    W ∈ Submonoid.closure {V : Matrix S S ℂ | TwoLevelSU V} :=
  su_mem_closure_of_suppOn Finset.univ W hW hdet fun i _ h => by
    rcases h with h | h <;> exact absurd (Finset.mem_univ _) h

end TwoLevel

/-! ### Section I — T6: dense unitary control at every level -/

section DenseControl

variable (T : FiniteOperationalTheory (Fin 2)) {n : ℕ}

theorem tensorOf_anc_eq_incl (k₀ : Fin n) (X : Matrix (Fin 2) (Fin 2) ℂ) :
    tensorOf X (anc k₀) = incl ((0 : Fin 2), k₀) (1, k₀) * X * (incl ((0 : Fin 2), k₀) (1, k₀))ᵀ := by
  have hne : ((0 : Fin 2), k₀) ≠ (1, k₀) := by simp
  ext ⟨x, k⟩ ⟨y, l⟩
  rw [Matrix.mul_assoc, incl_mul_apply hne, mul_transpose_incl_apply hne, mul_transpose_incl_apply hne]
  simp only [tensorOf_apply, anc_apply, Prod.mk.injEq]
  fin_cases x <;> fin_cases y <;> by_cases hk : k = k₀ <;> by_cases hl : l = k₀ <;> simp [hk, hl]

theorem blockOf_eq_twoLevel (k₀ : Fin n) (M : Matrix (Fin 2) (Fin 2) ℂ) :
    blockOf k₀ M = twoLevel ((0 : Fin 2), k₀) (1, k₀) M := by
  have h : blockOf k₀ M = 1 + blockOnly k₀ (M - 1) := by
    rw [← blockOf_sub, blockOf_one, add_sub_cancel]
  rw [h, twoLevel, blockOnly, tensorOf_anc_eq_incl]

theorem permMatrix_mul_incl (σ : Equiv.Perm (Fin 2 × Fin n)) (a b : Fin 2 × Fin n) :
    permMatrix σ * incl a b = incl (σ a) (σ b) := by
  ext i t
  simp only [Matrix.mul_apply, permMatrix, incl_apply]
  rw [Finset.sum_eq_single (σ.symm i)]
  · simp only [Equiv.apply_symm_apply, if_true, one_mul]
    congr 1
    simp only [eq_iff_iff]
    constructor
    · rintro (⟨ht, hs⟩ | ⟨ht, hs⟩)
      · left; exact ⟨ht, by rw [← hs, Equiv.apply_symm_apply]⟩
      · right; exact ⟨ht, by rw [← hs, Equiv.apply_symm_apply]⟩
    · rintro (⟨ht, hs⟩ | ⟨ht, hs⟩)
      · left; exact ⟨ht, by rw [hs, Equiv.symm_apply_apply]⟩
      · right; exact ⟨ht, by rw [hs, Equiv.symm_apply_apply]⟩
  · intro k _ hk
    have : σ k ≠ i := fun h => hk (by rw [← h, Equiv.symm_apply_apply])
    simp [this]
  · intro h; exact absurd (Finset.mem_univ _) h

theorem permMatrix_conjTranspose_eq_transpose (σ : Equiv.Perm (Fin 2 × Fin n)) :
    (permMatrix σ)ᴴ = (permMatrix σ)ᵀ := by
  ext i j
  simp only [Matrix.conjTranspose_apply, Matrix.transpose_apply, permMatrix]
  split_ifs <;> simp

/-- **THE RELOCATED GATE IS THE TWO-LEVEL MATRIX** on the carried pair. -/
theorem relocated_eq_twoLevel (σ : Equiv.Perm (Fin 2 × Fin n)) (k₀ : Fin n)
    (M : Matrix (Fin 2) (Fin 2) ℂ) :
    relocated σ k₀ M = twoLevel (σ (0, k₀)) (σ (1, k₀)) M := by
  have hP : permMatrix σ * (permMatrix σ)ᴴ = 1 := mul_eq_one_comm.mp (permMatrix_isometry σ)
  rw [relocated, blockOf_eq_twoLevel, twoLevel, twoLevel, Matrix.mul_add, Matrix.add_mul,
    Matrix.mul_one, hP, permMatrix_conjTranspose_eq_transpose]
  congr 1
  calc permMatrix σ * (incl ((0 : Fin 2), k₀) (1, k₀) * (M - 1) * (incl ((0 : Fin 2), k₀) (1, k₀))ᵀ)
        * (permMatrix σ)ᵀ
      = (permMatrix σ * incl ((0 : Fin 2), k₀) (1, k₀)) * (M - 1)
          * ((incl ((0 : Fin 2), k₀) (1, k₀))ᵀ * (permMatrix σ)ᵀ) := by
        simp only [Matrix.mul_assoc]
    _ = incl (σ (0, k₀)) (σ (1, k₀)) * (M - 1) * (incl (σ (0, k₀)) (σ (1, k₀)))ᵀ := by
        rw [← Matrix.transpose_mul, permMatrix_mul_incl]

/-- Every two-level special unitary is approximated by the available set. -/
theorem twoLevelSU_approx (hd : DerivedOI T) {α : ℝ} (hα : Irrational (α / Real.pi))
    (hg : FixedGateSourced α T) (hn : 0 < n) {V : Matrix (Fin 2 × Fin n) (Fin 2 × Fin n) ℂ}
    (hV : TwoLevelSU V) (ε : ℝ) (hε : 0 < ε) :
    ∃ V' ∈ availSet T n, V'ᴴ * V' = 1 ∧ ‖V - V'‖ < ε := by
  obtain ⟨a, b, M, hab, hM, hdet, rfl⟩ := hV
  obtain ⟨σ, hσa, hσb⟩ := exists_perm_pair_map (p₀ := ((0 : Fin 2), (⟨0, hn⟩ : Fin n)))
    (p₁ := (1, ⟨0, hn⟩)) (by simp) hab
  have h : twoLevel a b M = relocated σ ⟨0, hn⟩ M := by
    rw [relocated_eq_twoLevel, hσa, hσb]
  rw [h]
  exact relocated_dense T hd hα hg hn σ ⟨0, hn⟩ hM hdet ε hε

/-- Products of two-level special unitaries are approximated by the available set. -/
theorem closure_approx (hd : DerivedOI T) {α : ℝ} (hα : Irrational (α / Real.pi))
    (hg : FixedGateSourced α T) (hn : 0 < n) {W : Matrix (Fin 2 × Fin n) (Fin 2 × Fin n) ℂ}
    (hW : W ∈ Submonoid.closure {V : Matrix (Fin 2 × Fin n) (Fin 2 × Fin n) ℂ | TwoLevelSU V}) :
    Wᴴ * W = 1 ∧ ∀ ε : ℝ, 0 < ε → ∃ V ∈ availSet T n, Vᴴ * V = 1 ∧ ‖W - V‖ < ε := by
  have : Nonempty (Fin 2 × Fin n) := ⟨(0, ⟨0, hn⟩)⟩
  induction hW using Submonoid.closure_induction with
  | mem x hx =>
    refine ⟨?_, fun ε hε => twoLevelSU_approx T hd hα hg hn hx ε hε⟩
    obtain ⟨a, b, M, hab, hM, _, rfl⟩ := hx
    exact twoLevel_unitary hab hM
  | one =>
    refine ⟨by simp, fun ε hε => ⟨1, one_mem_availSet T hd n, by simp, ?_⟩⟩
    simpa using hε
  | mul x y _ _ hx hy =>
    refine ⟨unitary_mul hx.1 hy.1, fun ε hε => ?_⟩
    obtain ⟨V₁, hV₁A, hV₁u, hV₁⟩ := hx.2 (ε / 2) (by positivity)
    obtain ⟨V₂, hV₂A, hV₂u, hV₂⟩ := hy.2 (ε / 2) (by positivity)
    refine ⟨V₁ * V₂, mul_mem_availSet T hV₁A hV₂A, unitary_mul hV₁u hV₂u, ?_⟩
    calc ‖x * y - V₁ * V₂‖ ≤ ‖x - V₁‖ + ‖y - V₂‖ := norm_mul_sub_mul_le hx.1 hV₂u
      _ < ε / 2 + ε / 2 := by gcongr
      _ = ε := by ring

/-- **DENSITY OF THE SPECIAL UNITARIES** at every positive level. -/
theorem su_dense (hd : DerivedOI T) {α : ℝ} (hα : Irrational (α / Real.pi))
    (hg : FixedGateSourced α T) (hn : 0 < n) (W : Matrix (Fin 2 × Fin n) (Fin 2 × Fin n) ℂ)
    (hW : Wᴴ * W = 1) (hdet : W.det = 1) (ε : ℝ) (hε : 0 < ε) :
    ∃ V ∈ availSet T n, Vᴴ * V = 1 ∧ ‖W - V‖ < ε :=
  (closure_approx T hd hα hg hn (su_mem_closure_twoLevel W hW hdet)).2 ε hε

theorem det_norm_one' {S : Type} [Fintype S] [DecidableEq S] {U : Matrix S S ℂ} (hU : Uᴴ * U = 1) :
    ‖U.det‖ = 1 := by
  have h := congrArg Matrix.det hU
  rw [Matrix.det_mul, Matrix.det_conjTranspose, Matrix.det_one, Complex.star_def, mul_comm,
    Complex.mul_conj, Complex.normSq_eq_norm_sq] at h
  have h' : ‖U.det‖ ^ 2 = 1 := by exact_mod_cast h
  nlinarith [norm_nonneg U.det]

/-- **EVERY UNITARY IS A UNIT SCALAR TIMES A SPECIAL UNITARY**, on any finite carrier. -/
theorem exists_unit_scalar_su' {S : Type} [Fintype S] [DecidableEq S] (hS : 0 < Fintype.card S)
    {U : Matrix S S ℂ} (hU : Uᴴ * U = 1) :
    ∃ s : ℂ, ‖s‖ = 1 ∧ ((s⁻¹ • U)ᴴ * (s⁻¹ • U) = 1) ∧ (s⁻¹ • U).det = 1 := by
  set N : ℕ := Fintype.card S with hN
  set s : ℂ := Complex.exp (((Complex.arg U.det / N : ℝ) : ℂ) * Complex.I) with hs
  have hsn : ‖s‖ = 1 := Complex.norm_exp_ofReal_mul_I _
  have hsN : s ^ N = U.det := by
    rw [hs, ← Complex.exp_nat_mul]
    have hN0 : (N : ℂ) ≠ 0 := by exact_mod_cast hS.ne'
    have : (N : ℂ) * (((Complex.arg U.det / N : ℝ) : ℂ) * Complex.I)
        = ((Complex.arg U.det : ℝ) : ℂ) * Complex.I := by
      push_cast; field_simp
    rw [this]
    have h := Complex.norm_mul_exp_arg_mul_I U.det
    rwa [det_norm_one' hU, Complex.ofReal_one, one_mul] at h
  have hs0 : s ≠ 0 := by
    intro h; rw [h, norm_zero] at hsn; exact zero_ne_one hsn
  refine ⟨s, hsn, ?_, ?_⟩
  · rw [Matrix.conjTranspose_smul, Matrix.smul_mul, Matrix.mul_smul, smul_smul, hU]
    have : star s⁻¹ * s⁻¹ = 1 := by
      rw [Complex.star_def, map_inv₀, ← mul_inv, mul_comm, Complex.mul_conj,
        Complex.normSq_eq_norm_sq, hsn]
      norm_num
    rw [this, one_smul]
  · rw [Matrix.det_smul, ← hN, ← hsN, inv_pow]
    exact inv_mul_cancel₀ (pow_ne_zero _ hs0)

/-- **T6, D1**: under the closure and one fixed gate at an angle with `α/π` irrational, the theory
has dense unitary control at every level. -/
theorem denseUnitaryControl_of_fixedGate (hd : DerivedOI T) {α : ℝ} (hα : Irrational (α / Real.pi))
    (hg : FixedGateSourced α T) : DenseUnitaryControl T := by
  intro n U hU ε hε
  rcases Nat.eq_zero_or_pos n with rfl | hn
  · refine ⟨1, 1, by simp, by simp, availExt_zero T _, ?_⟩
    have : U - (1 : ℂ) • (1 : Matrix (Fin 2 × Fin 0) (Fin 2 × Fin 0) ℂ) = 0 := Subsingleton.elim _ _
    rw [this, norm_zero]; exact hε
  · have hcard : 0 < Fintype.card (Fin 2 × Fin n) := by
      rw [Fintype.card_prod, Fintype.card_fin, Fintype.card_fin]; omega
    obtain ⟨s, hs, hNu, hNd⟩ := exists_unit_scalar_su' hcard hU
    obtain ⟨V, hVA, hVu, hV⟩ := su_dense T hd hα hg hn (s⁻¹ • U) hNu hNd ε hε
    refine ⟨V, s, hVu, hs, hVA, ?_⟩
    have hs0 : s ≠ 0 := by
      intro h; rw [h, norm_zero] at hs; exact zero_ne_one hs
    have hU' : U = s • (s⁻¹ • U) := by rw [smul_smul, mul_inv_cancel₀ hs0, one_smul]
    rw [hU', ← smul_sub, norm_smul, hs, one_mul]
    exact hV

end DenseControl

/-! ### Section J — T3: the finite countercontrols at multiples of `π/4` -/

section Finite

/-- **THE LEVEL-ONE GROUP** generated by the fixed gate, the quarter phase and the exchange, as
two-by-two matrices. -/
inductive Gen2 (β : ℝ) : Matrix (Fin 2) (Fin 2) ℂ → Prop
  | one : Gen2 β 1
  | rot : Gen2 β (StateMixingCoupling.rot β)
  | phase : Gen2 β S2
  | swap : Gen2 β X2
  | mul {A B : Matrix (Fin 2) (Fin 2) ℂ} : Gen2 β A → Gen2 β B → Gen2 β (A * B)

theorem Gen2.unitary {β : ℝ} {A : Matrix (Fin 2) (Fin 2) ℂ} (h : Gen2 β A) : Aᴴ * A = 1 := by
  induction h with
  | one => simp
  | rot => exact rot_unitary β
  | phase => exact S2_unitary
  | swap => exact X2_unitary
  | mul _ _ hA hB => exact unitary_mul hA hB

/-- The generated group is monotone in the generator. -/
theorem Gen2.mono {β β' : ℝ} (hβ : Gen2 β' (StateMixingCoupling.rot β)) {A : Matrix (Fin 2) (Fin 2) ℂ}
    (h : Gen2 β A) : Gen2 β' A := by
  induction h with
  | one => exact Gen2.one
  | rot => exact hβ
  | phase => exact Gen2.phase
  | swap => exact Gen2.swap
  | mul _ _ hA hB => exact Gen2.mul hA hB

theorem Gen2.rot_nat (β : ℝ) : ∀ k : ℕ, Gen2 β (StateMixingCoupling.rot (k * β))
  | 0 => by simpa [rot_zero] using Gen2.one
  | k + 1 => by
      have := Gen2.mul (Gen2.rot_nat β k) Gen2.rot
      rwa [rot_mul, show (k : ℝ) * β + β = ((k + 1 : ℕ) : ℝ) * β by push_cast; ring] at this

theorem Gen2.rot_neg {β θ : ℝ} (h : Gen2 β (StateMixingCoupling.rot θ)) :
    Gen2 β (StateMixingCoupling.rot (-θ)) := by
  have := Gen2.mul (Gen2.mul Gen2.swap h) Gen2.swap
  rwa [X2_rot_X2] at this

theorem Gen2.rot_int (β : ℝ) (k : ℤ) : Gen2 β (StateMixingCoupling.rot (k * β)) := by
  obtain ⟨m, hm | hm⟩ := Int.eq_nat_or_neg k
  · subst hm; exact_mod_cast Gen2.rot_nat β m
  · subst hm
    have := Gen2.rot_neg (Gen2.rot_nat β m)
    rw [Int.cast_neg, Int.cast_natCast, neg_mul]; exact this

/-- The group at `k π / 4` sits inside the group at `π / 4`. -/
theorem Gen2.subset_pi_div_four (k : ℤ) {A : Matrix (Fin 2) (Fin 2) ℂ}
    (h : Gen2 (k * (Real.pi / 4)) A) : Gen2 (Real.pi / 4) A :=
  Gen2.mono (Gen2.rot_int (Real.pi / 4) k) h

/-- The third Pauli matrix. -/
def Y2 : Matrix (Fin 2) (Fin 2) ℂ := !![0, -Complex.I; Complex.I, 0]

/-- The four base Paulis, indexed. -/
def pauliBase : Fin 4 → Matrix (Fin 2) (Fin 2) ℂ := ![1, X2, Y2, Z2]

/-- **THE PAULI SET**: the base Paulis times the fourth roots of unity, sixteen matrices. -/
def Pauli : Set (Matrix (Fin 2) (Fin 2) ℂ) :=
  Set.range fun p : Fin 4 × Fin 4 => Complex.I ^ (p.1 : ℕ) • pauliBase p.2

theorem pauli_finite : Pauli.Finite := Set.finite_range _

theorem mem_pauli {P : Matrix (Fin 2) (Fin 2) ℂ} :
    P ∈ Pauli ↔ ∃ (k : Fin 4) (q : Fin 4), P = Complex.I ^ (k : ℕ) • pauliBase q := by
  constructor
  · rintro ⟨⟨k, q⟩, rfl⟩; exact ⟨k, q, rfl⟩
  · rintro ⟨k, q, rfl⟩; exact ⟨(k, q), rfl⟩

theorem I_pow_four : Complex.I ^ 4 = 1 := by
  rw [show (4 : ℕ) = 2 * 2 from rfl, pow_mul, Complex.I_sq]; norm_num

theorem I_pow_mod (m : ℕ) : Complex.I ^ m = Complex.I ^ (m % 4) := by
  conv_lhs => rw [← Nat.mod_add_div m 4, pow_add, pow_mul, I_pow_four, one_pow, mul_one]

theorem pauli_smul_I_pow (m : ℕ) {P : Matrix (Fin 2) (Fin 2) ℂ} (h : P ∈ Pauli) :
    Complex.I ^ m • P ∈ Pauli := by
  obtain ⟨k, q, rfl⟩ := mem_pauli.mp h
  refine mem_pauli.mpr ⟨⟨(m + k) % 4, Nat.mod_lt _ (by norm_num)⟩, q, ?_⟩
  rw [smul_smul, ← pow_add, I_pow_mod (m + k)]

/-- The Pauli product table: `(phase exponent, base index)`. -/
def pmul : Fin 4 → Fin 4 → ℕ × Fin 4 :=
  ![![(0, 0), (0, 1), (0, 2), (0, 3)],
    ![(0, 1), (0, 0), (1, 3), (3, 2)],
    ![(0, 2), (3, 3), (0, 0), (1, 1)],
    ![(0, 3), (1, 2), (3, 1), (0, 0)]]

/-- **THE PAULI PRODUCT TABLE**: base Paulis multiply to a fourth root of unity times a base
Pauli. -/
theorem pauliBase_mul_table (q q' : Fin 4) :
    pauliBase q * pauliBase q' = Complex.I ^ (pmul q q').1 • pauliBase (pmul q q').2 := by
  fin_cases q <;> fin_cases q' <;>
    (ext i j; fin_cases i <;> fin_cases j <;>
      simp [pmul, pauliBase, X2, Y2, Z2, Matrix.mul_apply, Fin.sum_univ_two, pow_succ])

theorem pauliBase_mul (q q' : Fin 4) :
    ∃ (m : ℕ) (q'' : Fin 4), pauliBase q * pauliBase q' = Complex.I ^ m • pauliBase q'' :=
  ⟨(pmul q q').1, (pmul q q').2, pauliBase_mul_table q q'⟩

theorem pauli_mul {P Q : Matrix (Fin 2) (Fin 2) ℂ} (hP : P ∈ Pauli) (hQ : Q ∈ Pauli) :
    P * Q ∈ Pauli := by
  obtain ⟨k, q, rfl⟩ := mem_pauli.mp hP
  obtain ⟨k', q', rfl⟩ := mem_pauli.mp hQ
  obtain ⟨m, q'', h⟩ := pauliBase_mul q q'
  rw [Matrix.smul_mul, Matrix.mul_smul, h, smul_smul, smul_smul, ← pow_add, ← pow_add]
  exact pauli_smul_I_pow _ (mem_pauli.mpr ⟨⟨0, by norm_num⟩, q'', by simp⟩)

theorem X2_mem_pauli : X2 ∈ Pauli := mem_pauli.mpr ⟨⟨0, by norm_num⟩, 1, by simp [pauliBase]⟩
theorem Z2_mem_pauli : Z2 ∈ Pauli := mem_pauli.mpr ⟨⟨0, by norm_num⟩, 3, by simp [pauliBase]⟩
theorem neg_Z2_mem_pauli : -Z2 ∈ Pauli := by
  have := pauli_smul_I_pow 2 Z2_mem_pauli
  rwa [Complex.I_sq, neg_one_smul] at this
theorem Y2_mem_pauli : Y2 ∈ Pauli := mem_pauli.mpr ⟨⟨0, by norm_num⟩, 2, by simp [pauliBase]⟩

/-- `Y = i X Z`. -/
theorem Y2_eq : Y2 = Complex.I • (X2 * Z2) := by
  ext i j; fin_cases i <;> fin_cases j <;> simp [X2, Y2, Z2]

/-- **CONJUGATION INVARIANCE**: a unitary carrying `X` and `Z` into the Pauli set carries every
Pauli into the Pauli set. -/
theorem pauli_conj_of_XZ {A : Matrix (Fin 2) (Fin 2) ℂ} (hA : Aᴴ * A = 1)
    (hX : A * X2 * Aᴴ ∈ Pauli) (hZ : A * Z2 * Aᴴ ∈ Pauli) :
    ∀ P ∈ Pauli, A * P * Aᴴ ∈ Pauli := by
  have hAA : A * Aᴴ = 1 := mul_eq_one_comm.mp hA
  intro P hP
  obtain ⟨k, q, rfl⟩ := mem_pauli.mp hP
  rw [Matrix.mul_smul, Matrix.smul_mul]
  apply pauli_smul_I_pow
  fin_cases q
  · change A * 1 * Aᴴ ∈ Pauli
    rw [Matrix.mul_one, hAA]
    exact mem_pauli.mpr ⟨⟨0, by norm_num⟩, 0, by simp [pauliBase]⟩
  · change A * X2 * Aᴴ ∈ Pauli
    exact hX
  · change A * Y2 * Aᴴ ∈ Pauli
    rw [Y2_eq, Matrix.mul_smul, Matrix.smul_mul]
    have key : A * (X2 * Z2) * Aᴴ ∈ Pauli := by
      have : A * (X2 * Z2) * Aᴴ = (A * X2 * Aᴴ) * (A * Z2 * Aᴴ) := by
        calc A * (X2 * Z2) * Aᴴ = A * X2 * (Aᴴ * A) * Z2 * Aᴴ := by
              rw [hA, Matrix.mul_one]; simp only [Matrix.mul_assoc]
          _ = (A * X2 * Aᴴ) * (A * Z2 * Aᴴ) := by simp only [Matrix.mul_assoc]
      rw [this]
      exact pauli_mul hX hZ
    simpa using pauli_smul_I_pow 1 key
  · change A * Z2 * Aᴴ ∈ Pauli
    exact hZ

theorem sqrt_two_div_two_sq : (((Real.sqrt 2 / 2 : ℝ)) : ℂ) ^ 2 = 1 / 2 := by
  rw [← Complex.ofReal_pow, div_pow, Real.sq_sqrt (by norm_num)]; push_cast; ring

/-- The rotation by `π/4` carries `X` to `−Z` and `Z` to `X`. -/
theorem rot_pi_div_four_X :
    StateMixingCoupling.rot (Real.pi / 4) * X2 * (StateMixingCoupling.rot (Real.pi / 4))ᴴ = -Z2 := by
  have hq := sqrt_two_div_two_sq
  rw [rot_conjTranspose]
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [StateMixingCoupling.rot, X2, Z2, Matrix.mul_apply, Fin.sum_univ_two, Real.cos_pi_div_four,
      Real.sin_pi_div_four, Real.cos_neg, Real.sin_neg, -Complex.ofReal_div] <;>
    first | linear_combination (-2) * hq | linear_combination 2 * hq

theorem rot_pi_div_four_Z :
    StateMixingCoupling.rot (Real.pi / 4) * Z2 * (StateMixingCoupling.rot (Real.pi / 4))ᴴ = X2 := by
  have hq := sqrt_two_div_two_sq
  rw [rot_conjTranspose]
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [StateMixingCoupling.rot, X2, Z2, Matrix.mul_apply, Fin.sum_univ_two, Real.cos_pi_div_four,
      Real.sin_pi_div_four, Real.cos_neg, Real.sin_neg, -Complex.ofReal_div] <;>
    linear_combination 2 * hq

theorem S2_X2 : S2 * X2 * S2ᴴ = Y2 := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [S2, X2, Y2, Matrix.mul_apply, Fin.sum_univ_two, Matrix.conjTranspose_apply, Complex.conj_I]

theorem S2_Z2 : S2 * Z2 * S2ᴴ = Z2 := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [S2, Z2, Matrix.mul_apply, Fin.sum_univ_two, Matrix.conjTranspose_apply, Complex.conj_I]

theorem X2_X2 : X2 * X2 * X2ᴴ = X2 := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [X2, Matrix.mul_apply, Fin.sum_univ_two, Matrix.conjTranspose_apply]

theorem X2_Z2 : X2 * Z2 * X2ᴴ = -Z2 := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [X2, Z2, Matrix.mul_apply, Fin.sum_univ_two, Matrix.conjTranspose_apply]

/-- **EVERY ELEMENT OF THE GROUP AT `π/4` NORMALIZES THE PAULI SET.** -/
theorem Gen2.pauli_conj {A : Matrix (Fin 2) (Fin 2) ℂ} (h : Gen2 (Real.pi / 4) A) :
    ∀ P ∈ Pauli, A * P * Aᴴ ∈ Pauli := by
  induction h with
  | one => intro P hP; simpa using hP
  | rot =>
    exact pauli_conj_of_XZ (rot_unitary _) (by rw [rot_pi_div_four_X]; exact neg_Z2_mem_pauli)
      (by rw [rot_pi_div_four_Z]; exact X2_mem_pauli)
  | phase =>
    exact pauli_conj_of_XZ S2_unitary (by rw [S2_X2]; exact Y2_mem_pauli)
      (by rw [S2_Z2]; exact Z2_mem_pauli)
  | swap =>
    exact pauli_conj_of_XZ X2_unitary (by rw [X2_X2]; exact X2_mem_pauli)
      (by rw [X2_Z2]; exact neg_Z2_mem_pauli)
  | @mul A B _ _ ihA ihB =>
    intro P hP
    have h := ihA _ (ihB P hP)
    rw [Matrix.conjTranspose_mul]
    have e : A * B * P * (Bᴴ * Aᴴ) = A * (B * P * Bᴴ) * Aᴴ := by simp only [Matrix.mul_assoc]
    rw [e]; exact h

/-- **THE COMMUTANT OF `X` AND `Z` IS THE SCALARS.** -/
theorem scalar_of_comm_XZ {W : Matrix (Fin 2) (Fin 2) ℂ} (hX : W * X2 = X2 * W) (hZ : W * Z2 = Z2 * W) :
    W = W 0 0 • (1 : Matrix (Fin 2) (Fin 2) ℂ) := by
  have e1 := congrFun (congrFun hZ 0) 1
  have e2 := congrFun (congrFun hZ 1) 0
  have e3 := congrFun (congrFun hX 0) 1
  simp [Z2, X2, Matrix.mul_apply, Fin.sum_univ_two] at e1 e2 e3
  ext i j
  fin_cases i <;> fin_cases j <;> simp [Matrix.smul_apply]
  · linear_combination (-1/2 : ℂ) * e1
  · linear_combination (1/2 : ℂ) * e2
  · exact e3.symm

/-- **TWO GROUP ELEMENTS WITH THE SAME PAULI ACTION ARE PROPORTIONAL.** -/
theorem proportional_of_same_conj {G G' : Matrix (Fin 2) (Fin 2) ℂ} (hG : Gᴴ * G = 1)
    (hG' : G'ᴴ * G' = 1) (hX : G * X2 * Gᴴ = G' * X2 * G'ᴴ) (hZ : G * Z2 * Gᴴ = G' * Z2 * G'ᴴ) :
    ∃ c : ℂ, G' = c • G := by
  set W := Gᴴ * G' with hW
  have hGG : G * Gᴴ = 1 := mul_eq_one_comm.mp hG
  have hG'G' : G' * G'ᴴ = 1 := mul_eq_one_comm.mp hG'
  have hWX : W * X2 = X2 * W := by
    have h1 : W * X2 * Wᴴ = X2 := by
      rw [hW, Matrix.conjTranspose_mul, Matrix.conjTranspose_conjTranspose]
      calc Gᴴ * G' * X2 * (G'ᴴ * G) = Gᴴ * (G' * X2 * G'ᴴ) * G := by simp only [Matrix.mul_assoc]
        _ = Gᴴ * (G * X2 * Gᴴ) * G := by rw [hX]
        _ = X2 := by
          calc Gᴴ * (G * X2 * Gᴴ) * G = (Gᴴ * G) * X2 * (Gᴴ * G) := by simp only [Matrix.mul_assoc]
            _ = X2 := by rw [hG, Matrix.one_mul, Matrix.mul_one]
    have hWW : Wᴴ * W = 1 := by
      rw [hW, Matrix.conjTranspose_mul, Matrix.conjTranspose_conjTranspose]
      calc G'ᴴ * G * (Gᴴ * G') = G'ᴴ * (G * Gᴴ) * G' := by simp only [Matrix.mul_assoc]
        _ = 1 := by rw [hGG, Matrix.mul_one, hG']
    calc W * X2 = W * X2 * (Wᴴ * W) := by rw [hWW, Matrix.mul_one]
      _ = (W * X2 * Wᴴ) * W := by simp only [Matrix.mul_assoc]
      _ = X2 * W := by rw [h1]
  have hWZ : W * Z2 = Z2 * W := by
    have h1 : W * Z2 * Wᴴ = Z2 := by
      rw [hW, Matrix.conjTranspose_mul, Matrix.conjTranspose_conjTranspose]
      calc Gᴴ * G' * Z2 * (G'ᴴ * G) = Gᴴ * (G' * Z2 * G'ᴴ) * G := by simp only [Matrix.mul_assoc]
        _ = Gᴴ * (G * Z2 * Gᴴ) * G := by rw [hZ]
        _ = Z2 := by
          calc Gᴴ * (G * Z2 * Gᴴ) * G = (Gᴴ * G) * Z2 * (Gᴴ * G) := by simp only [Matrix.mul_assoc]
            _ = Z2 := by rw [hG, Matrix.one_mul, Matrix.mul_one]
    have hWW : Wᴴ * W = 1 := by
      rw [hW, Matrix.conjTranspose_mul, Matrix.conjTranspose_conjTranspose]
      calc G'ᴴ * G * (Gᴴ * G') = G'ᴴ * (G * Gᴴ) * G' := by simp only [Matrix.mul_assoc]
        _ = 1 := by rw [hGG, Matrix.mul_one, hG']
    calc W * Z2 = W * Z2 * (Wᴴ * W) := by rw [hWW, Matrix.mul_one]
      _ = (W * Z2 * Wᴴ) * W := by simp only [Matrix.mul_assoc]
      _ = Z2 * W := by rw [h1]
  refine ⟨W 0 0, ?_⟩
  have hWs := scalar_of_comm_XZ hWX hWZ
  have h1 : G' = G * W := by rw [hW, ← Matrix.mul_assoc, hGG, Matrix.one_mul]
  rw [h1]
  conv_lhs => rw [hWs]
  rw [Matrix.mul_smul, Matrix.mul_one]

/-- **T3 — THE GROUP AT `π/4` IS FINITE UP TO SCALAR**: its elements are determined up to a
scalar by their action on `X` and `Z`, which takes values in the finite Pauli set. -/
theorem gen2_pi_div_four_finite_upToScalar :
    ∃ D : Set (Matrix (Fin 2) (Fin 2) ℂ), D.Finite ∧
      ∀ G, Gen2 (Real.pi / 4) G → ∃ (c : ℂ) (M : Matrix (Fin 2) (Fin 2) ℂ), M ∈ D ∧ G = c • M := by
  classical
  let F : Set (Matrix (Fin 2) (Fin 2) ℂ × Matrix (Fin 2) (Fin 2) ℂ) :=
    {x | x ∈ Pauli ×ˢ Pauli ∧ ∃ G, Gen2 (Real.pi / 4) G ∧ (G * X2 * Gᴴ, G * Z2 * Gᴴ) = x}
  have hF : F.Finite := (pauli_finite.prod pauli_finite).subset fun x hx => hx.1
  have : Finite F := hF.to_subtype
  let rep : F → Matrix (Fin 2) (Fin 2) ℂ := fun x => Classical.choose x.2.2
  refine ⟨Set.range rep, Set.finite_range rep, fun G hG => ?_⟩
  have hx : ((G * X2 * Gᴴ, G * Z2 * Gᴴ) : _ × _) ∈ F :=
    ⟨Set.mk_mem_prod (hG.pauli_conj _ X2_mem_pauli) (hG.pauli_conj _ Z2_mem_pauli), G, hG, rfl⟩
  set x : F := ⟨_, hx⟩
  have hspec := Classical.choose_spec x.2.2
  obtain ⟨hM, hMx⟩ := hspec
  have hXeq : G * X2 * Gᴴ = rep x * X2 * (rep x)ᴴ := (congrArg Prod.fst hMx).symm
  have hZeq : G * Z2 * Gᴴ = rep x * Z2 * (rep x)ᴴ := (congrArg Prod.snd hMx).symm
  obtain ⟨c, hc⟩ := proportional_of_same_conj hM.unitary hG.unitary hXeq.symm hZeq.symm
  exact ⟨c, rep x, ⟨x, rfl⟩, hc⟩

/-- **T3, UNIFORMLY**: the group at every multiple of `π/4` is finite up to scalar. -/
theorem gen2_multiple_finite_upToScalar (k : ℤ) :
    ∃ D : Set (Matrix (Fin 2) (Fin 2) ℂ), D.Finite ∧
      ∀ G, Gen2 (k * (Real.pi / 4)) G → ∃ (c : ℂ) (M : Matrix (Fin 2) (Fin 2) ℂ), M ∈ D ∧ G = c • M := by
  obtain ⟨D, hD, h⟩ := gen2_pi_div_four_finite_upToScalar
  exact ⟨D, hD, fun G hG => h G (Gen2.subset_pi_div_four k hG)⟩

end Finite

/-! ### Section K — the canonical fixed-gate theory -/

section Canonical

theorem permMatrix_levelPerm_swap (n : ℕ) :
    permMatrix (levelPerm (Equiv.swap (0 : Fin 2) 1) n) = tensorOf X2 (1 : Matrix (Fin n) (Fin n) ℂ) := by
  ext ⟨x, k⟩ ⟨y, l⟩
  simp only [permMatrix, levelPerm_apply, tensorOf_apply, X2, Matrix.one_apply, Prod.mk.injEq]
  fin_cases x <;> fin_cases y <;> by_cases hkl : k = l <;> simp_all [eq_comm]

/-- The site exchange at every level reverses the fixed gate. -/
theorem mixImage_neg_eq_conj (n : ℕ) (α : ℝ) :
    permMatrix (levelPerm (Equiv.swap (0 : Fin 2) 1) n) * mixImage n α
      * permMatrix (levelPerm (Equiv.swap (0 : Fin 2) 1) n) = mixImage n (-α) := by
  rw [permMatrix_levelPerm_swap, mixImage_eq_tensorOf, mixImage_eq_tensorOf, tensorOf_mul',
    tensorOf_mul', X2_rot_X2, Matrix.one_mul, Matrix.one_mul]

/-- **THE FIXED-ANGLE CLASS IS DAGGER-STABLE**: the adjoint of the gate is its exchange
conjugate. -/
theorem mixR_singleton_daggerStable (α : ℝ) : DaggerStable (MixR {α}) := by
  intro T _ _ K h
  induction h with
  | perm K h => exact MixR.perm _ (scaled_conjTranspose h)
  | phase n p =>
    rw [phaseGate_conjTranspose']
    exact MixR.mul _ _ (MixR.mul _ _ (MixR.phase n p) (MixR.phase n p)) (MixR.phase n p)
  | mix n θ hθ =>
    rw [mixImage_conjTranspose, ← mixImage_neg_eq_conj]
    have hP : MixR {α} (Fin 2 × Fin n) (permMatrix (levelPerm (Equiv.swap (0 : Fin 2) 1) n)) :=
      MixR.perm _ (permClass_permMatrix _)
    exact MixR.mul _ _ (MixR.mul _ _ hP (MixR.mix n θ hθ)) hP
  | mul K L _ _ ihK ihL => rw [Matrix.conjTranspose_mul]; exact MixR.mul _ _ ihL ihK
  | smul a K ha _ ih =>
    rw [Matrix.conjTranspose_smul]
    exact MixR.smul _ _ (by simpa using ha) ih
  | proj m k =>
    rw [Matrix.diagonal_conjTranspose]
    have key : ∀ (U : Type) [Fintype U] [DecidableEq U],
        (star fun r : U × Fin m => if r.2 = k then (1 : ℂ) else 0)
          = fun r => if r.2 = k then (1 : ℂ) else 0 := by
      intro U _ _
      funext r; simp only [Pi.star_apply]; split_ifs <;> simp
    rw [key]
    exact MixR.proj m k
  | block m K f e _ ih => rw [ancBlock_conjTranspose']; exact MixR.block m _ e f ih
  | relabel e K _ ih => rw [Matrix.conjTranspose_reindex]; exact MixR.relabel e _ ih

/-- **THE FIXED-ANGLE CLASS IS CONTEXT-STABLE.** -/
theorem mixR_singleton_contextStable (α : ℝ) : ContextStable (MixR {α}) := by
  intro R T _ _ _ _ K h
  induction h with
  | perm K h => exact MixR.perm _ (scaled_tensor_one h)
  | phase n p =>
    have := tensorOf_one_phaseGate_mem R n p
    rw [phaseGate, tensorOf_one_diagonal]
    set e := ctxRelabel R n
    have hmem := phaseIndicator_mem (mixR_arch {α}) (fun n p => MixR.phase n p) (Fintype.card R * n)
      (Finset.univ.filter fun x : Fin 2 × Fin (Fintype.card R * n) => p = (e x).2)
    have heq : (Matrix.diagonal fun q : R × (Fin 2 × Fin n) => if p = q.2 then Complex.I else 1)
        = Matrix.reindex e e (Matrix.diagonal fun x : Fin 2 × Fin (Fintype.card R * n) =>
            if x ∈ (Finset.univ.filter fun x : Fin 2 × Fin (Fintype.card R * n) => p = (e x).2)
            then Complex.I else 1) := by
      rw [Matrix.reindex_apply, Matrix.submatrix_diagonal_equiv]
      congr 1
      funext q
      simp
    rw [heq]
    exact MixR.relabel e _ hmem
  | mix n θ hθ => rw [tensorOf_one_mixImage]; exact MixR.relabel _ _ (MixR.mix _ _ hθ)
  | mul K L _ _ ihK ihL =>
    have key := tensorOf_mul' (1 : Matrix R R ℂ) (1 : Matrix R R ℂ) K L
    rw [Matrix.one_mul] at key
    rw [← key]
    exact MixR.mul _ _ ihK ihL
  | smul a K ha _ ih => rw [tensorOf_smul_right]; exact MixR.smul _ _ ha ih
  | proj m k =>
    rw [tensorOf_one_diagonal]
    exact MixR.perm _ (scaled_diagonal_indicator _)
  | block m K f e _ ih =>
    rw [tensorOf_one_ancBlock]
    exact MixR.block m _ f e (MixR.relabel _ _ ih)
  | relabel e K _ ih => rw [tensorOf_one_reindex]; exact MixR.relabel _ _ ih

/-- **THE CANONICAL FIXED-GATE THEORY**: the stated access with the datum at one angle. -/
noncomputable abbrev fixedGateTheory (α : ℝ) : FiniteOperationalTheory (Fin 2) :=
  mixTheoryR {α} (Fin 2)

theorem fixedGateTheory_derivedOI (α : ℝ) : DerivedOI (fixedGateTheory α) :=
  derivedOI_of_stated (mixR_arch _) (mixR_labelInvariant _) (mixR_singleton_daggerStable α)
    (mixR_singleton_contextStable α) (fun _ _ _ K h => MixR.perm K h) (fun n p => MixR.phase n p)

theorem fixedGateTheory_fixedGateSourced (α : ℝ) : FixedGateSourced α (fixedGateTheory α) :=
  fun n => SubstratumSource.genTheory_avail_conj (mixR_arch _)
    (MixR.mix n α (Set.mem_singleton α)) (mixImage_unitary n α)

/-- **THE CANONICAL THEORY IS KRAUS-SOUND**, as every implementation-generated theory is. -/
theorem fixedGateTheory_krausSoundExt (α : ℝ) : KrausSoundExt (fixedGateTheory α) :=
  krausSoundExt_of_implementationGenerated (genTheory_generated (MixR {α}) (mixR_arch {α}))

/-- **THE CANONICAL THEORY HAS DENSE UNITARY CONTROL** at every angle with `α/π` irrational. -/
theorem fixedGateTheory_denseUnitaryControl {α : ℝ} (hα : Irrational (α / Real.pi)) :
    DenseUnitaryControl (fixedGateTheory α) :=
  denseUnitaryControl_of_fixedGate _ (fixedGateTheory_derivedOI α) hα
    (fixedGateTheory_fixedGateSourced α)

/-- **AND IT IS NOT EXACT QUANTUM MECHANICS**: density is not exactness. -/
theorem fixedGateTheory_not_qm (α : ℝ) : ¬ ExactAllFiniteEndomorphicQuantumOps (fixedGateTheory α) :=
  mixTheoryR_not_qm (Set.countable_singleton α)

/-- **A CONCRETE WITNESS**: the angle one radian, `1/π` irrational since `π` is. -/
theorem fixedGateTheory_one_denseUnitaryControl : DenseUnitaryControl (fixedGateTheory 1) :=
  fixedGateTheory_denseUnitaryControl (by rw [one_div]; exact irrational_inv_iff.mpr irrational_pi)

end Canonical

end DiscreteCompletion
end OIBridge

#print axioms OIBridge.DiscreteCompletion.conj_within
#print axioms OIBridge.DiscreteCompletion.norm_mul_sub_mul_le
#print axioms OIBridge.DiscreteCompletion.blockOf_mul
#print axioms OIBridge.DiscreteCompletion.blockOf_unitary
#print axioms OIBridge.DiscreteCompletion.blockOnly_rot_sub_one_norm_le
#print axioms OIBridge.DiscreteCompletion.blockOf_rot_dist_le
#print axioms OIBridge.DiscreteCompletion.rx_eq_conj
#print axioms OIBridge.DiscreteCompletion.rot_rx_rot
#print axioms OIBridge.DiscreteCompletion.su2_form
#print axioms OIBridge.DiscreteCompletion.exists_unit_scalar_su2
#print axioms OIBridge.DiscreteCompletion.euler_of_su2
#print axioms OIBridge.DiscreteCompletion.euler_of_unitary
#print axioms OIBridge.DiscreteCompletion.dense_angles
#print axioms OIBridge.DiscreteCompletion.BlockRepertoire.rot_approx
#print axioms OIBridge.DiscreteCompletion.BlockRepertoire.rx_approx
#print axioms OIBridge.DiscreteCompletion.BlockRepertoire.dense_block_su2
#print axioms OIBridge.DiscreteCompletion.blockRepertoire_levelOne
#print axioms OIBridge.DiscreteCompletion.levelOne_dense
#print axioms OIBridge.DiscreteCompletion.flipSet_avail
#print axioms OIBridge.DiscreteCompletion.echo_identity
#print axioms OIBridge.DiscreteCompletion.isolated_mem_availSet
#print axioms OIBridge.DiscreteCompletion.blockRepertoire_level
#print axioms OIBridge.DiscreteCompletion.exists_perm_pair_map
#print axioms OIBridge.DiscreteCompletion.relocated_dense
#print axioms OIBridge.DiscreteCompletion.twoLevel_mul
#print axioms OIBridge.DiscreteCompletion.det_twoLevel
#print axioms OIBridge.DiscreteCompletion.twoLevel_mul_apply
#print axioms OIBridge.DiscreteCompletion.givens_unitary
#print axioms OIBridge.DiscreteCompletion.det_givens
#print axioms OIBridge.DiscreteCompletion.row_zero_of_col_zero
#print axioms OIBridge.DiscreteCompletion.su_mem_closure_of_suppOn
#print axioms OIBridge.DiscreteCompletion.su_mem_closure_twoLevel
#print axioms OIBridge.DiscreteCompletion.relocated_eq_twoLevel
#print axioms OIBridge.DiscreteCompletion.twoLevelSU_approx
#print axioms OIBridge.DiscreteCompletion.closure_approx
#print axioms OIBridge.DiscreteCompletion.su_dense
#print axioms OIBridge.DiscreteCompletion.exists_unit_scalar_su'
#print axioms OIBridge.DiscreteCompletion.denseUnitaryControl_of_fixedGate
#print axioms OIBridge.DiscreteCompletion.Gen2.pauli_conj
#print axioms OIBridge.DiscreteCompletion.scalar_of_comm_XZ
#print axioms OIBridge.DiscreteCompletion.proportional_of_same_conj
#print axioms OIBridge.DiscreteCompletion.gen2_pi_div_four_finite_upToScalar
#print axioms OIBridge.DiscreteCompletion.gen2_multiple_finite_upToScalar
#print axioms OIBridge.DiscreteCompletion.mixR_singleton_daggerStable
#print axioms OIBridge.DiscreteCompletion.mixR_singleton_contextStable
#print axioms OIBridge.DiscreteCompletion.fixedGateTheory_derivedOI
#print axioms OIBridge.DiscreteCompletion.fixedGateTheory_fixedGateSourced
#print axioms OIBridge.DiscreteCompletion.fixedGateTheory_krausSoundExt
#print axioms OIBridge.DiscreteCompletion.fixedGateTheory_denseUnitaryControl
#print axioms OIBridge.DiscreteCompletion.fixedGateTheory_not_qm
#print axioms OIBridge.DiscreteCompletion.fixedGateTheory_one_denseUnitaryControl
