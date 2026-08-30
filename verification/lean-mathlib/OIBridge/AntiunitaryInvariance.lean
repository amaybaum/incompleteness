/-
  OIBridge/AntiunitaryInvariance.lean — no operational data distinguish the two branches.

  PHASE TWO, ITEM ONE. The two-branch theorem leaves exactly one non-gauge ambiguity, the
  antiunitary branch H ↦ −H̄. This file proves that NO enlargement of the operational data —
  arbitrary preparations, channels, adaptive multi-time instrument sequences, and effects —
  can remove it: transposing every object in a circuit simultaneously,

      ρ ↦ ρᵀ,   E ↦ Eᵀ,   𝒢 ↦ T ∘ 𝒢 ∘ T,

  preserves every circuit probability. The proof is two lines of structure: interior transposes
  cancel in composition (`run_transposeMap`), and the trace pairing is transpose-invariant
  (`pairing_transpose`). Adaptive sequences are covered in full generality because
  `circuit_invariance` quantifies over ARBITRARY functions on matrices and arbitrary lists —
  each fixed outcome branch of an adaptive strategy is one such list — and the outcome-string
  form is made explicit for instrument sequences (`string_invariance`).

  The transformation is not an artifact of allowing arbitrary maps: it sends legitimate quantum
  operations to legitimate quantum operations. On a Kraus channel `X ↦ Σ_k A_k X A_k†` it acts
  by conjugating every Kraus operator (`transposeMap_kraus`), preserving complete positivity by
  construction, and it preserves the normalization Σ_k A_k†A_k = 1 (`kraus_normalization`).
  Restricted to unitary evolution it is EXACTLY the second branch: the transpose-conjugated
  channel of `e^{−iHt}` is the channel of `e^{−i(−H̄)t}` (`unitary_channel_transpose` together
  with `BohrFrequency.reflect_conj`). So the antiunitary ambiguity is a global symmetry of the
  entire operational formalism — self-consistent gate-set tomography of any length sees
  nothing — and anything that removes it must be MORE than circuit data. The thermal
  orientation that does remove it is OIBridge/ThermalOrientation.lean.
-/
import OIBridge.BohrFrequency
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.LinearAlgebra.FiniteDimensional.Basic

namespace OIBridge
namespace AntiunitaryInvariance

open Matrix

variable {n : Type*} [Fintype n] [DecidableEq n]

/-- The transpose conjugation of a matrix map: `T ∘ 𝒢 ∘ T`. -/
def transposeMap (g : Matrix n n ℂ → Matrix n n ℂ) : Matrix n n ℂ → Matrix n n ℂ :=
  fun X => (g Xᵀ)ᵀ

/-- Running a circuit: apply the channels in order. -/
def run (gs : List (Matrix n n ℂ → Matrix n n ℂ)) (ρ : Matrix n n ℂ) : Matrix n n ℂ :=
  gs.foldl (fun X g => g X) ρ

omit [Fintype n] [DecidableEq n] in
/-- Interior transposes cancel: the transposed circuit run on the transposed state is the
transpose of the original run. -/
theorem run_transposeMap (gs : List (Matrix n n ℂ → Matrix n n ℂ)) (ρ : Matrix n n ℂ) :
    run (gs.map transposeMap) ρᵀ = (run gs ρ)ᵀ := by
  induction gs generalizing ρ with
  | nil => rfl
  | cons g gs ih =>
      show run (gs.map transposeMap) (transposeMap g ρᵀ) = (run gs (g ρ))ᵀ
      rw [show transposeMap g ρᵀ = (g ρ)ᵀ by rw [transposeMap, Matrix.transpose_transpose]]
      exact ih (g ρ)

omit [DecidableEq n] in
/-- The trace pairing of effect and state is transpose-invariant. -/
theorem pairing_transpose (Ef X : Matrix n n ℂ) :
    Matrix.trace (Efᵀ * Xᵀ) = Matrix.trace (Ef * X) := by
  rw [← Matrix.transpose_mul, Matrix.trace_transpose, Matrix.trace_mul_comm]

omit [DecidableEq n] in
/-- **NO CIRCUIT DISTINGUISHES THE BRANCHES.** Transposing the preparation, every channel, and
the effect simultaneously preserves every circuit probability — for ARBITRARY matrix maps and
arbitrary finite sequences, hence for every fixed outcome branch of any adaptive multi-time
strategy. More operational data of this kind cannot remove the antiunitary ambiguity. -/
theorem circuit_invariance (gs : List (Matrix n n ℂ → Matrix n n ℂ))
    (ρ Ef : Matrix n n ℂ) :
    Matrix.trace (Efᵀ * run (gs.map transposeMap) ρᵀ) = Matrix.trace (Ef * run gs ρ) := by
  rw [run_transposeMap, pairing_transpose]

/-- Entrywise conjugation, the operator form the transformed channels take. -/
def conjOp (M : Matrix n n ℂ) : Matrix n n ℂ := M.map (starRingEnd ℂ)

omit [Fintype n] [DecidableEq n] in
lemma transpose_conjTranspose_eq (M : Matrix n n ℂ) : (Mᴴ)ᵀ = conjOp M := by
  ext i j
  simp [conjOp, Matrix.conjTranspose_apply, Matrix.transpose_apply, Matrix.map_apply]

omit [Fintype n] [DecidableEq n] in
lemma conjOp_conjTranspose (M : Matrix n n ℂ) : (conjOp M)ᴴ = Mᵀ := by
  ext i j
  simp [conjOp, Matrix.conjTranspose_apply, Matrix.transpose_apply, Matrix.map_apply]

/-- A Kraus channel. -/
def krausMap {κ : Type*} [Fintype κ] (A : κ → Matrix n n ℂ) :
    Matrix n n ℂ → Matrix n n ℂ :=
  fun X => ∑ k, A k * X * (A k)ᴴ

omit [DecidableEq n] in
/-- The transpose conjugation of a Kraus channel is the Kraus channel of the entrywise
conjugates: the transformed operation is again completely positive by construction. -/
theorem transposeMap_kraus {κ : Type*} [Fintype κ] (A : κ → Matrix n n ℂ) :
    transposeMap (krausMap A) = krausMap (fun k => conjOp (A k)) := by
  funext X
  rw [transposeMap, krausMap]
  rw [Matrix.transpose_sum]
  refine Finset.sum_congr rfl fun k _ => ?_
  rw [Matrix.transpose_mul, Matrix.transpose_mul, Matrix.transpose_transpose,
    transpose_conjTranspose_eq, ← conjOp_conjTranspose, Matrix.mul_assoc]

/-- Conjugating the Kraus operators preserves the trace-preservation normalization. -/
theorem kraus_normalization {κ : Type*} [Fintype κ] (A : κ → Matrix n n ℂ)
    (h : ∑ k, (A k)ᴴ * A k = 1) :
    ∑ k, (conjOp (A k))ᴴ * conjOp (A k) = 1 := by
  have h1 : ∀ k, (conjOp (A k))ᴴ * conjOp (A k) = ((A k)ᴴ * A k)ᵀ := by
    intro k
    rw [conjOp_conjTranspose, ← transpose_conjTranspose_eq, ← Matrix.transpose_mul]
  rw [Finset.sum_congr rfl fun k _ => h1 k, ← Matrix.transpose_sum, h, Matrix.transpose_one]

omit [DecidableEq n] in
/-- The outcome-string form for instrument sequences: the probability of any fixed outcome
string of any adaptive instrument sequence is a single Kraus-string sandwich, and it is
invariant under conjugating every operator and transposing state and effect. -/
theorem string_invariance (As : List (Matrix n n ℂ)) (ρ Ef : Matrix n n ℂ) :
    Matrix.trace (Efᵀ * ((As.map conjOp).foldl (fun X A => A * X * Aᴴ) ρᵀ))
      = Matrix.trace (Ef * (As.foldl (fun X A => A * X * Aᴴ) ρ)) := by
  have key : ∀ (As : List (Matrix n n ℂ)) (ρ : Matrix n n ℂ),
      (As.map conjOp).foldl (fun X A => A * X * Aᴴ) ρᵀ
        = (As.foldl (fun X A => A * X * Aᴴ) ρ)ᵀ := by
    intro As
    induction As with
    | nil => intro ρ; rfl
    | cons A As ih =>
        intro ρ
        show (As.map conjOp).foldl (fun X A => A * X * Aᴴ) (conjOp A * ρᵀ * (conjOp A)ᴴ)
          = (As.foldl (fun X A => A * X * Aᴴ) (A * ρ * Aᴴ))ᵀ
        rw [show conjOp A * ρᵀ * (conjOp A)ᴴ = (A * ρ * Aᴴ)ᵀ by
          rw [conjOp_conjTranspose, ← transpose_conjTranspose_eq,
            Matrix.transpose_mul, Matrix.transpose_mul, Matrix.mul_assoc]]
        exact ih (A * ρ * Aᴴ)
  rw [key, pairing_transpose]

omit [DecidableEq n] in
/-- The transpose conjugation of the unitary channel of `U` is the unitary channel of `Ū`.
With `BohrFrequency.reflect_conj` — `Ū(t)` is the propagator of the reflected model
`(V̄, −E)` — this identifies the circuit symmetry, restricted to unitary evolution, as
exactly the second branch `H ↦ −H̄`. -/
theorem unitary_channel_transpose (U : Matrix n n ℂ) :
    transposeMap (fun X => U * X * Uᴴ) = fun X => conjOp U * X * (conjOp U)ᴴ := by
  funext X
  rw [transposeMap]
  rw [Matrix.transpose_mul, Matrix.transpose_mul, Matrix.transpose_transpose,
    transpose_conjTranspose_eq, ← conjOp_conjTranspose, Matrix.mul_assoc]

/-! ### Unitary-channel rigidity: exact channel equality has no antiunitary branch

The two lemmas below back the exact-unitary regime of Appendix A's Hamiltonian-consistency
corollary: equality of the CONJUGATION ACTIONS of two unitaries forces them to agree up to a
unimodular scalar (`ad_eq_scalar` — the commutant of the full matrix algebra is scalar), and a
family-of-phases identity `e^{−iE_a t} = c(t)·e^{−iE'_a t}` forces the spectra to differ by one
common shift (`phase_families_shift`). Exact channel equality therefore leaves only
`H' = H + E₀·1` — no antiunitary branch and no nontrivial diagonal: transition probabilities
discard the coherence information, exact channels keep it. -/

/-- A matrix commuting with every matrix is scalar. -/
theorem commute_all_scalar (Z : Matrix n n ℂ)
    (h : ∀ X : Matrix n n ℂ, Z * X = X * Z) :
    ∀ i j p : n, (i ≠ p → Z i p = 0) ∧ Z i i = Z j j := by
  classical
  have key : ∀ p q i j : n,
      (if j = q then Z i p else 0) = (if i = p then Z q j else 0) := by
    intro p q i j
    have hX := h (Matrix.of fun k l => if k = p ∧ l = q then 1 else 0)
    have h1 := congrFun (congrFun hX i) j
    rw [Matrix.mul_apply, Matrix.mul_apply] at h1
    have hL : (∑ k, Z i k * Matrix.of (fun k l => if k = p ∧ l = q then (1 : ℂ) else 0) k j)
        = if j = q then Z i p else 0 := by
      rw [Finset.sum_eq_single p]
      · by_cases hj : j = q
        · simp [Matrix.of_apply, hj]
        · simp [Matrix.of_apply, hj]
      · intro k _ hk
        simp [Matrix.of_apply, hk]
      · intro hp
        exact absurd (Finset.mem_univ p) hp
    have hR : (∑ k, Matrix.of (fun k l => if k = p ∧ l = q then (1 : ℂ) else 0) i k * Z k j)
        = if i = p then Z q j else 0 := by
      rw [Finset.sum_eq_single q]
      · by_cases hi : i = p
        · simp [Matrix.of_apply, hi]
        · simp [Matrix.of_apply, hi]
      · intro k _ hk
        simp [Matrix.of_apply, hk]
      · intro hq
        exact absurd (Finset.mem_univ q) hq
    rw [hL, hR] at h1
    exact h1
  intro i j p
  constructor
  · intro hip
    simpa [hip] using key p i i i
  · simpa using key i j i j

/-- **EQUAL CONJUGATION ACTIONS FORCE A SCALAR.** Two unitaries with the same channel differ by
a unimodular scalar: the relative operator lies in the commutant of the full matrix algebra. -/
theorem ad_eq_scalar {hm : Nonempty n} (U W : Matrix n n ℂ)
    (hU : U * Uᴴ = 1) (hW : W * Wᴴ = 1)
    (h : ∀ X : Matrix n n ℂ, U * X * Uᴴ = W * X * Wᴴ) :
    ∃ c : ℂ, c * (starRingEnd ℂ) c = 1 ∧ U = c • W := by
  classical
  obtain ⟨i0⟩ := hm
  have hU' : Uᴴ * U = 1 := mul_eq_one_comm.mp hU
  have hW' : Wᴴ * W = 1 := mul_eq_one_comm.mp hW
  set Z : Matrix n n ℂ := Wᴴ * U with hZ
  have hcomm : ∀ X : Matrix n n ℂ, Z * X = X * Z := by
    intro X
    have h1 := h X
    have h2 : Wᴴ * (U * X * Uᴴ) * U = Wᴴ * (W * X * Wᴴ) * U := by rw [h1]
    calc Z * X = Wᴴ * U * X * (Uᴴ * U) := by rw [hU', Matrix.mul_one]
      _ = Wᴴ * (U * X * Uᴴ) * U := by noncomm_ring
      _ = Wᴴ * (W * X * Wᴴ) * U := h2
      _ = (Wᴴ * W) * X * (Wᴴ * U) := by noncomm_ring
      _ = X * Z := by rw [hW', Matrix.one_mul]
  have hsc := commute_all_scalar Z hcomm
  set c : ℂ := Z i0 i0 with hc
  have hZs : Z = c • (1 : Matrix n n ℂ) := by
    ext i j
    by_cases hij : i = j
    · subst hij
      rw [(hsc i i0 i0).2]
      simpa using hc.symm
    · rw [(hsc i i0 j).1 hij]
      simp [hij]
  have hUW : U = c • W := by
    calc U = (W * Wᴴ) * U := by rw [hW, Matrix.one_mul]
      _ = W * Z := by rw [hZ, Matrix.mul_assoc]
      _ = W * (c • (1 : Matrix n n ℂ)) := by rw [hZs]
      _ = c • W := by rw [Matrix.mul_smul, Matrix.mul_one]
  refine ⟨c, ?_, hUW⟩
  have h1 : (c • W) * (c • W)ᴴ = 1 := by rw [← hUW]; exact hU
  rw [Matrix.conjTranspose_smul, Matrix.smul_mul, Matrix.mul_smul, hW] at h1
  have h2 := congrFun (congrFun h1 i0) i0
  simp only [Matrix.smul_apply, Matrix.one_apply_eq, smul_eq_mul, mul_one] at h2
  simpa [Complex.star_def] using h2

/-- **PHASE FAMILIES DIFFERING BY A SCALAR ARE SHIFTED SPECTRA.** If for every time the two
phase families `e^{−iE_a t}` and `e^{−iE'_a t}` differ by one common scalar, the spectral
differences `E_a − E'_a` are `a`-independent: the scalar is `e^{−iE₀t}` and `E = E' + E₀`. -/
theorem phase_families_shift {m : ℕ} (E E' : Fin m → ℝ)
    (h : ∀ t : ℝ, ∃ c : ℂ, ∀ a : Fin m,
      Complex.exp (-(Complex.I * (E a : ℂ) * (t : ℂ)))
        = c * Complex.exp (-(Complex.I * (E' a : ℂ) * (t : ℂ))))
    (a b : Fin m) : E a - E' a = E b - E' b := by
  by_contra hne
  have hδ : (E a - E' a) - (E b - E' b) ≠ 0 := sub_ne_zero.mpr hne
  obtain ⟨c, hc⟩ := h (Real.pi / ((E a - E' a) - (E b - E' b)))
  have hval : ∀ x : Fin m, Complex.exp (-(Complex.I * (E x : ℂ)
        * ((Real.pi / ((E a - E' a) - (E b - E' b)) : ℝ) : ℂ)))
      * Complex.exp (Complex.I * (E' x : ℂ)
        * ((Real.pi / ((E a - E' a) - (E b - E' b)) : ℝ) : ℂ)) = c := by
    intro x
    rw [hc x, mul_assoc, ← Complex.exp_add]
    rw [show -(Complex.I * (E' x : ℂ) * ((Real.pi / ((E a - E' a) - (E b - E' b)) : ℝ) : ℂ))
      + Complex.I * (E' x : ℂ) * ((Real.pi / ((E a - E' a) - (E b - E' b)) : ℝ) : ℂ)
      = 0 by ring]
    rw [Complex.exp_zero, mul_one]
  have hab2 := (hval a).trans (hval b).symm
  rw [← Complex.exp_add, ← Complex.exp_add] at hab2
  have harg : (-(Complex.I * (E a : ℂ) * ((Real.pi / ((E a - E' a) - (E b - E' b)) : ℝ) : ℂ))
        + Complex.I * (E' a : ℂ) * ((Real.pi / ((E a - E' a) - (E b - E' b)) : ℝ) : ℂ))
      - (-(Complex.I * (E b : ℂ) * ((Real.pi / ((E a - E' a) - (E b - E' b)) : ℝ) : ℂ))
        + Complex.I * (E' b : ℂ) * ((Real.pi / ((E a - E' a) - (E b - E' b)) : ℝ) : ℂ))
      = -(Real.pi : ℂ) * Complex.I := by
    have hreal : ((E a - E' a) - (E b - E' b))
        * (Real.pi / ((E a - E' a) - (E b - E' b))) = Real.pi := by
      field_simp
    push_cast
    have hrealC : (((E a : ℂ) - E' a) - ((E b : ℂ) - E' b))
        * ((Real.pi : ℂ) / (((E a : ℂ) - E' a) - ((E b : ℂ) - E' b))) = (Real.pi : ℂ) := by
      exact_mod_cast congrArg (fun x : ℝ => (x : ℂ)) hreal
    linear_combination (-Complex.I) * hrealC
  have hquot : Complex.exp (-(Real.pi : ℂ) * Complex.I) = 1 := by
    rw [← harg, Complex.exp_sub, hab2, div_self (Complex.exp_ne_zero _)]
  rw [show (-(Real.pi : ℂ) * Complex.I) = -((Real.pi : ℂ) * Complex.I) by ring,
    Complex.exp_neg, Complex.exp_pi_mul_I] at hquot
  norm_num at hquot

/-- Packaged form: a common scalar between the phase families at every time is a single energy
shift `E = E' + E₀`. -/
theorem phase_families_shift' {m : ℕ} (hm : 0 < m) (E E' : Fin m → ℝ)
    (h : ∀ t : ℝ, ∃ c : ℂ, ∀ a : Fin m,
      Complex.exp (-(Complex.I * (E a : ℂ) * (t : ℂ)))
        = c * Complex.exp (-(Complex.I * (E' a : ℂ) * (t : ℂ)))) :
    ∃ E₀ : ℝ, ∀ a, E a = E' a + E₀ := by
  refine ⟨E ⟨0, hm⟩ - E' ⟨0, hm⟩, fun a => ?_⟩
  have := phase_families_shift E E' h a ⟨0, hm⟩
  linarith

#print axioms run_transposeMap
#print axioms pairing_transpose
#print axioms circuit_invariance
#print axioms transposeMap_kraus
#print axioms kraus_normalization
#print axioms string_invariance
#print axioms unitary_channel_transpose
#print axioms commute_all_scalar
#print axioms ad_eq_scalar
#print axioms phase_families_shift
#print axioms phase_families_shift'

end AntiunitaryInvariance
end OIBridge
