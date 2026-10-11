/-
  OIBridge/EqvK2Generation.lean — design module of the research thread `research/equivalence` (node
  E19, draft S6 §H.6). Not adopted, not certified, not a round: the generation step of the full-flow
  form. Invariance under the gate and under the clause's two operations at every angle gives block
  invariance, through exact finite words in those operations — no closure, no density, no
  reachability hypothesis. Hence S6's reachability statement `ReachPure` is a theorem about the
  drive words, and the pair-level K2 schema holds without it.

  §I.1  Conjugation invariance `ConjInv K M` — `K` carried into itself by `ω ↦ coordOf (M dict ω Mᴴ)` —
        closed under products and unit scalars; the block product law `blockMat_mul`.
  §I.2  The generators: the phase circle (the flow at every angle; every point of the unit circle
        through `Complex.arg`), the cyclic lift and its inverse (`cycMatᴴ = −cycMat²`), the gate
        (`cnotMat = blockMat 1 X`, `dict_cnot`).
  §I.3  One token: every special unitary is `dUnit a · rotRe c s · dUnit b` (`su_euler`), with
        `rotRe c s = cycMatᴴ · dUnit (c − i s) · cycMat` (`rotRe_eq`); hence idle invariance under every
        special unitary (`conjInv_idle`).
  §I.4  The controlled half: `blockMat 1 (dUnit (r̄²))` is the word `gate · (1 ⊗ dUnit r) · gate ·
        (1 ⊗ dUnit r̄)` (`rtrick`); `blockMat 1 (rotRe c s)` is its conjugate by an idle word; hence
        controlled invariance under every special unitary (`conjInv_ctrl`).
  §I.5  Block invariance from the gate and the clause (`blockInvariant_of_drive`); `ReachPure` as a
        theorem (`reachPure`); the forcing without it (`pairCone_eq_Q3_of_drive_exact`); `Q3` is
        invariant under the gate (`Q3_cnot`); given H1 and H3, `K = Q3` exactly when `K` is invariant
        under the gate and the clause's two operations (`pairCone_eq_Q3_iff_drive_exact`: the direction
        `→` is `Q3_cnot` with `EqvK2Converse.Q3_aMiss`, the direction `←` is
        `pairCone_eq_Q3_of_drive_exact`).

  Every hypothesis is a premise; nothing here sources H1, H2, H3 or the clause, and every invariance
  statement is cone invariance, not availability.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.EqvK2Block
import OIBridge.BridgeConverge
import Mathlib.Analysis.SpecialFunctions.Complex.Arg
import Mathlib.Analysis.SpecialFunctions.Pow.Complex

namespace OIBridge
namespace EqvK2Generation

open Matrix CompositeDimension MonoidalCompletion EqvK2Schema EqvK2Converse EqvK2Block
open scoped ComplexOrder

noncomputable section

/-! ### §I.1 — conjugation invariance and the block product law -/

/-- `K` is carried into itself by conjugation with `M`, read back through the coordinates. -/
def ConjInv (K : Set (W 3)) (M : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ) : Prop :=
  ∀ ω ∈ K, coordOf (M * dict ω * Mᴴ) ∈ K

theorem dict_coordOf_conj (M : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ) (ω : W 3) :
    dict (coordOf (M * dict ω * Mᴴ)) = M * dict ω * Mᴴ :=
  dict_coordOf _ (Matrix.isHermitian_mul_mul_conjTranspose _ (dict_isHermitian ω))

theorem conjInv_mul {K : Set (W 3)} {A B : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ}
    (hA : ConjInv K A) (hB : ConjInv K B) : ConjInv K (A * B) := by
  intro ω hω
  have h := hA _ (hB ω hω)
  rw [dict_coordOf_conj] at h
  have e : A * (B * dict ω * Bᴴ) * Aᴴ = A * B * dict ω * (A * B)ᴴ := by
    rw [Matrix.conjTranspose_mul]
    simp only [Matrix.mul_assoc]
  rwa [e] at h

theorem conjInv_smul {K : Set (W 3)} {A : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ} (z : ℂ)
    (hz : star z * z = 1) (hA : ConjInv K A) : ConjInv K (z • A) := by
  intro ω hω
  rw [conj_smul z hz]
  exact hA ω hω

theorem P0_mul_P0 : P0 * P0 = P0 := by
  ext i j
  fin_cases i <;> fin_cases j <;> simp [P0, Matrix.mul_apply, Fin.sum_univ_two]

theorem P0_mul_P1 : P0 * P1 = 0 := by
  ext i j
  fin_cases i <;> fin_cases j <;> simp [P0, P1, Matrix.mul_apply, Fin.sum_univ_two]

theorem P1_mul_P0 : P1 * P0 = 0 := by
  ext i j
  fin_cases i <;> fin_cases j <;> simp [P0, P1, Matrix.mul_apply, Fin.sum_univ_two]

theorem P1_mul_P1 : P1 * P1 = P1 := by
  ext i j
  fin_cases i <;> fin_cases j <;> simp [P1, Matrix.mul_apply, Fin.sum_univ_two]

theorem tensorOf_zero_left (B : Matrix (Fin 2) (Fin 2) ℂ) :
    tensorOf (0 : Matrix (Fin 2) (Fin 2) ℂ) B = 0 := by
  ext p q
  simp [tensorOf_apply]

/-- **The block product law.** -/
theorem blockMat_mul (A B C D : Matrix (Fin 2) (Fin 2) ℂ) :
    blockMat A B * blockMat C D = blockMat (A * C) (B * D) := by
  simp only [blockMat, Matrix.add_mul, Matrix.mul_add, tensorOf_mul, P0_mul_P0, P0_mul_P1,
    P1_mul_P0, P1_mul_P1, tensorOf_zero_left, add_zero, zero_add]

theorem tensorOf_one_mul (A B : Matrix (Fin 2) (Fin 2) ℂ) :
    tensorOf (1 : Matrix (Fin 2) (Fin 2) ℂ) (A * B) = tensorOf 1 A * tensorOf 1 B := by
  rw [tensorOf_mul, Matrix.one_mul]

theorem isSU_mul {A B : Matrix (Fin 2) (Fin 2) ℂ} (hA : IsSU A) (hB : IsSU B) : IsSU (A * B) :=
  ⟨Submonoid.mul_mem _ hA.1 hB.1, by rw [Matrix.det_mul, hA.2, hB.2, one_mul]⟩

theorem isSU_unitary {U : Matrix (Fin 2) (Fin 2) ℂ} (hU : IsSU U) : Uᴴ * U = 1 := by
  rw [← Matrix.star_eq_conjTranspose]
  exact Matrix.mem_unitaryGroup_iff'.mp hU.1

/-! ### §I.2 — the generators -/

/-- Every point of the unit circle is `(cos t, sin t)` for some `t`. -/
theorem exists_angle (c s : ℝ) (h : c ^ 2 + s ^ 2 = 1) :
    ∃ t : ℝ, Real.cos t = c ∧ Real.sin t = s := by
  have hre : (Complex.mk c s).re = c := rfl
  have him : (Complex.mk c s).im = s := rfl
  have hsq : ‖Complex.mk c s‖ ^ 2 = 1 := by
    rw [← Complex.normSq_eq_norm_sq, Complex.normSq_apply, hre, him]
    nlinarith [h]
  have hn : ‖Complex.mk c s‖ = 1 := by
    have h0 := norm_nonneg (Complex.mk c s)
    nlinarith [hsq, h0]
  have hz0 : Complex.mk c s ≠ 0 := by
    intro h0
    rw [h0, norm_zero] at hn
    exact zero_ne_one hn
  refine ⟨Complex.arg (Complex.mk c s), ?_, ?_⟩
  · simp only [Complex.cos_arg hz0, hn, div_one, hre]
  · simp only [Complex.sin_arg, hn, div_one, him]

/-- The flow at one angle. -/
theorem conjInv_phase {K : Set (W 3)}
    (hflow : ∀ t : ℝ, ∀ ω ∈ K, actT (KInfFoundations.rotLin t) ω ∈ K) (t : ℝ) :
    ConjInv K (tensorOf 1 (phaseMat (Real.cos t) (Real.sin t))) := by
  intro ω hω
  rw [← dict_actT_rotLin, coordOf_dict]
  exact hflow t ω hω

/-- The flow at every point of the unit circle. -/
theorem conjInv_phase_circle {K : Set (W 3)}
    (hflow : ∀ t : ℝ, ∀ ω ∈ K, actT (KInfFoundations.rotLin t) ω ∈ K) (c s : ℝ)
    (h : c ^ 2 + s ^ 2 = 1) : ConjInv K (tensorOf 1 (phaseMat c s)) := by
  obtain ⟨t, hc, hs⟩ := exists_angle c s h
  rw [← hc, ← hs]
  exact conjInv_phase hflow t

/-- The diagonal special unitary `diag(z, z̄)` (special unitary when `|z| = 1`). -/
def dUnit (z : ℂ) : Matrix (Fin 2) (Fin 2) ℂ := !![z, 0; 0, star z]

theorem dUnit_eq_smul (z : ℂ) (hz : star z * z = 1) :
    dUnit z = z • phaseMat (star z ^ 2).re (star z ^ 2).im := by
  have hre : (((star z ^ 2).re : ℝ) : ℂ) + (((star z ^ 2).im : ℝ) : ℂ) * Complex.I = star z ^ 2 :=
    Complex.re_add_im _
  have key : z * star z ^ 2 = star z := by linear_combination (star z) * hz
  rw [Matrix.eta_fin_two (z • phaseMat (star z ^ 2).re (star z ^ 2).im)]
  simp only [dUnit, phaseMat, Matrix.smul_apply, Matrix.of_apply, Matrix.cons_val_zero,
    Matrix.cons_val_one, smul_eq_mul, mul_one, mul_zero, hre, key]

/-- The diagonal unit pairs, from the flow. -/
theorem conjInv_dUnit {K : Set (W 3)}
    (hflow : ∀ t : ℝ, ∀ ω ∈ K, actT (KInfFoundations.rotLin t) ω ∈ K) (z : ℂ)
    (hz : star z * z = 1) : ConjInv K (tensorOf 1 (dUnit z)) := by
  have hw : (star z ^ 2).re ^ 2 + (star z ^ 2).im ^ 2 = 1 := by
    have h1 : star (star z ^ 2) * star z ^ 2 = 1 := by
      rw [star_pow, star_star]
      linear_combination (star z * z + 1) * hz
    have h2 : ((Complex.normSq (star z ^ 2) : ℝ) : ℂ) = 1 := by
      rw [Complex.normSq_eq_conj_mul_self, ← Complex.star_def]
      exact h1
    have h3 : Complex.normSq (star z ^ 2) = 1 := by exact_mod_cast h2
    rw [Complex.normSq_apply] at h3
    nlinarith [h3]
  rw [dUnit_eq_smul z hz, tensorOf_smul_right]
  exact conjInv_smul z hz (conjInv_phase_circle hflow _ _ hw)

/-- The cyclic lift. -/
theorem conjInv_cyc {K : Set (W 3)}
    (hcyc : ∀ ω ∈ K, actT (KInfFoundations.cycEquiv : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) ω ∈ K) :
    ConjInv K (tensorOf 1 cycMat) := by
  intro ω hω
  rw [← dict_actT_cyc, coordOf_dict]
  exact hcyc ω hω

/-- The cyclic lift has order three up to sign: `cycMatᴴ = −cycMat²`. -/
theorem cycMat_conjTranspose_eq : cycMatᴴ = (-1 : ℂ) • (cycMat * cycMat) := by
  rw [cycMat_conjTranspose, Matrix.eta_fin_two ((-1 : ℂ) • (cycMat * cycMat))]
  simp only [cycMatH, cycMat, Matrix.mul_fin_two, Matrix.smul_apply, Matrix.of_apply,
    Matrix.cons_val_zero, Matrix.cons_val_one, smul_eq_mul]
  refine mat2_ext ?_ ?_ ?_ ?_ <;>
    first
      | ring1
      | linear_combination (1 / 2 : ℂ) * Complex.I_sq
      | linear_combination (-1 / 2 : ℂ) * Complex.I_sq

/-- The inverse of the cyclic lift, as the square of the lift up to sign. -/
theorem conjInv_cycH {K : Set (W 3)}
    (hcyc : ∀ ω ∈ K, actT (KInfFoundations.cycEquiv : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) ω ∈ K) :
    ConjInv K (tensorOf 1 cycMatᴴ) := by
  rw [cycMat_conjTranspose_eq, tensorOf_smul_right, tensorOf_one_mul]
  exact conjInv_smul (-1) (by simp) (conjInv_mul (conjInv_cyc hcyc) (conjInv_cyc hcyc))

/-- The flip `X`. -/
def Xm : Matrix (Fin 2) (Fin 2) ℂ := !![0, 1; 1, 0]

/-- The bridge's controlled NOT is the block pair `(1, X)`. -/
theorem cnotMat_eq : BridgeDictionary.cnotMat = blockMat 1 Xm := by
  ext ⟨i, j⟩ ⟨k, l⟩
  fin_cases i <;> fin_cases j <;> fin_cases k <;> fin_cases l <;>
    simp [BridgeDictionary.cnotMat, BridgeDictionary.projZero, BridgeDictionary.projOne,
      BridgeDictionary.pauli, blockMat, P0, P1, Xm, tensorOf_apply, Matrix.add_apply,
      Matrix.diagonal_apply, Matrix.one_apply]

theorem cnotMat_conjTranspose : (blockMat 1 Xm)ᴴ = blockMat 1 Xm := by
  ext ⟨i, j⟩ ⟨k, l⟩
  fin_cases i <;> fin_cases j <;> fin_cases k <;> fin_cases l <;>
    simp [blockMat, P0, P1, Xm, tensorOf_apply, Matrix.add_apply, Matrix.conjTranspose_apply,
      Matrix.one_apply]

/-- The gate, through the bridge's `dict_cnot` on the one dictionary. -/
theorem dict_cnot_block (ω : W 3) :
    dict (cnot ω) = blockMat 1 Xm * dict ω * (blockMat 1 Xm)ᴴ := by
  rw [cnotMat_conjTranspose, ← cnotMat_eq, ← BridgeConverge.dict_converge,
    BridgeDictionary.dict_cnot]

theorem conjInv_cnot {K : Set (W 3)} (hH2 : ∀ ω ∈ K, cnot ω ∈ K) :
    ConjInv K (blockMat 1 Xm) := by
  intro ω hω
  rw [← dict_cnot_block, coordOf_dict]
  exact hH2 ω hω

/-! ### §I.3 — one token: Euler factors and idle invariance -/

/-- The real rotation `[[c, −s], [s, c]]`. -/
def rotRe (c s : ℝ) : Matrix (Fin 2) (Fin 2) ℂ := !![(c : ℂ), -(s : ℂ); (s : ℂ), (c : ℂ)]

/-- The real rotation is the inverse cyclic conjugate of a diagonal unit pair. -/
theorem rotRe_eq (c s : ℝ) :
    rotRe c s = cycMatᴴ * dUnit ((c : ℂ) - (s : ℂ) * Complex.I) * cycMat := by
  have hst : star ((c : ℂ) - (s : ℂ) * Complex.I) = (c : ℂ) + (s : ℂ) * Complex.I := by
    simp
  rw [cycMat_conjTranspose]
  simp only [rotRe, dUnit, hst, cycMatH, cycMat, Matrix.mul_fin_two]
  refine mat2_ext ?_ ?_ ?_ ?_
  · linear_combination ((c : ℂ) / 2) * Complex.I_sq
  · linear_combination (-(s : ℂ) * (Complex.I + 2) / 2) * Complex.I_sq
  · linear_combination (-(s : ℂ) * (Complex.I - 2) / 2) * Complex.I_sq
  · linear_combination ((c : ℂ) / 2) * Complex.I_sq

/-- A special unitary of `ℂ²`: `[[p, −q̄], [q, p̄]]` with `|p|² + |q|² = 1`. -/
theorem su_form {U : Matrix (Fin 2) (Fin 2) ℂ} (hU : IsSU U) :
    U = !![U 0 0, -star (U 1 0); U 1 0, star (U 0 0)] ∧
      star (U 0 0) * U 0 0 + star (U 1 0) * U 1 0 = 1 := by
  have hu : star U * U = 1 := Matrix.mem_unitaryGroup_iff'.mp hU.1
  have h1 : U * Matrix.adjugate U = 1 := by rw [Matrix.mul_adjugate, hU.2, one_smul]
  have hadj : star U = Matrix.adjugate U := by
    calc star U = star U * (U * Matrix.adjugate U) := by rw [h1, Matrix.mul_one]
      _ = star U * U * Matrix.adjugate U := by rw [Matrix.mul_assoc]
      _ = Matrix.adjugate U := by rw [hu, Matrix.one_mul]
  rw [Matrix.adjugate_fin_two] at hadj
  have e00 : star (U 0 0) = U 1 1 := by
    have h := congrFun (congrFun hadj 0) 0
    simpa [Matrix.star_apply] using h
  have e10 : star (U 0 1) = -U 1 0 := by
    have h := congrFun (congrFun hadj 1) 0
    simpa [Matrix.star_apply] using h
  have e01 : U 0 1 = -star (U 1 0) := by
    have h := congrArg star e10
    rwa [star_star, star_neg] at h
  refine ⟨?_, ?_⟩
  · conv_lhs => rw [Matrix.eta_fin_two U]
    rw [e01, ← e00]
  · have h := congrFun (congrFun hu 0) 0
    simpa [Matrix.mul_apply, Fin.sum_univ_two, Matrix.star_apply] using h

/-- Polar form. -/
theorem polar_unit (p : ℂ) : ∃ u : ℂ, star u * u = 1 ∧ p = ((‖p‖ : ℝ) : ℂ) * u := by
  by_cases hp : p = 0
  · exact ⟨1, by simp, by simp [hp]⟩
  · have hn : ((‖p‖ : ℝ) : ℂ) ≠ 0 := by
      rw [Complex.ofReal_ne_zero]
      exact norm_ne_zero_iff.mpr hp
    refine ⟨p / ((‖p‖ : ℝ) : ℂ), ?_, (mul_div_cancel₀ p hn).symm⟩
    have h1 : star p * p = ((‖p‖ : ℝ) : ℂ) ^ 2 := by
      rw [Complex.star_def]
      exact_mod_cast Complex.conj_mul' p
    have h2 : star (p / ((‖p‖ : ℝ) : ℂ)) = star p / ((‖p‖ : ℝ) : ℂ) := by
      rw [star_div₀]
      congr 1
      rw [Complex.star_def, Complex.conj_ofReal]
    rw [h2, div_mul_div_comm, h1, sq, div_self (mul_ne_zero hn hn)]

/-- A square root of a unit complex number is a unit. -/
theorem exists_unit_sqrt {w : ℂ} (hw : star w * w = 1) : ∃ b : ℂ, star b * b = 1 ∧ b ^ 2 = w := by
  obtain ⟨b, hb⟩ : ∃ b : ℂ, b ^ 2 = w :=
    ⟨w ^ (((2 : ℕ) : ℂ)⁻¹), Complex.cpow_nat_inv_pow w (by norm_num)⟩
  have hw' : (starRingEnd ℂ) w * w = 1 := by
    rw [← Complex.star_def]
    exact hw
  have hn : Complex.normSq b = 1 := by
    have h2 : ((Complex.normSq b : ℝ) : ℂ) ^ 2 = 1 := by
      rw [Complex.normSq_eq_conj_mul_self, mul_pow, ← map_pow, hb]
      exact hw'
    have h2' : Complex.normSq b ^ 2 = 1 := by exact_mod_cast h2
    have hnn := Complex.normSq_nonneg b
    nlinarith [h2', hnn]
  refine ⟨b, ?_, hb⟩
  rw [Complex.star_def, ← Complex.normSq_eq_conj_mul_self, hn, Complex.ofReal_one]

/-- The Euler factorisation, as an identity of `2 × 2` literals. -/
theorem euler_core (p q u₁ u₂ b : ℂ) (c s : ℝ)
    (hp : p = (c : ℂ) * u₁) (hq : q = (s : ℂ) * u₂) (hb : star b * b = 1)
    (hb2 : b ^ 2 = u₁ * u₂) (hu₁ : star u₁ * u₁ = 1) :
    !![p, -star q; q, star p] = dUnit (u₁ * star b) * rotRe c s * dUnit b := by
  have hps : star p = (c : ℂ) * star u₁ := by
    rw [hp]
    simp
  have hqs : star q = (s : ℂ) * star u₂ := by
    rw [hq]
    simp
  have hb2s : star b ^ 2 = star u₁ * star u₂ := by
    rw [← star_pow, hb2, star_mul']
  simp only [dUnit, rotRe, Matrix.mul_fin_two, star_mul', star_star]
  refine mat2_ext ?_ ?_ ?_ ?_
  · linear_combination hp - ((c : ℂ) * u₁) * hb
  · linear_combination (-1 : ℂ) * hqs + ((s : ℂ) * u₁) * hb2s + ((s : ℂ) * star u₂) * hu₁
  · linear_combination hq - ((s : ℂ) * star u₁) * hb2 - ((s : ℂ) * u₂) * hu₁
  · linear_combination hps - ((c : ℂ) * star u₁) * hb

/-- **Every special unitary of `ℂ²` is a product of a diagonal unit pair, a real rotation and a
diagonal unit pair** (exact, no angle beyond the polar forms and one square root). -/
theorem su_euler {U : Matrix (Fin 2) (Fin 2) ℂ} (hU : IsSU U) :
    ∃ a b : ℂ, star a * a = 1 ∧ star b * b = 1 ∧ ∃ c s : ℝ, c ^ 2 + s ^ 2 = 1 ∧
      U = dUnit a * rotRe c s * dUnit b := by
  obtain ⟨hform, hnorm⟩ := su_form hU
  obtain ⟨u₁, hu₁, hp⟩ := polar_unit (U 0 0)
  obtain ⟨u₂, hu₂, hq⟩ := polar_unit (U 1 0)
  have hw : star (u₁ * u₂) * (u₁ * u₂) = 1 := by
    rw [star_mul']
    linear_combination (star u₂ * u₂) * hu₁ + hu₂
  obtain ⟨b, hb, hb2⟩ := exists_unit_sqrt hw
  refine ⟨u₁ * star b, b, ?_, hb, ‖U 0 0‖, ‖U 1 0‖, ?_, ?_⟩
  · rw [star_mul', star_star]
    linear_combination (b * star b) * hu₁ + hb
  · have h1 : star (U 0 0) * U 0 0 = ((‖U 0 0‖ : ℝ) : ℂ) ^ 2 := by
      rw [Complex.star_def]
      exact_mod_cast Complex.conj_mul' (U 0 0)
    have h2 : star (U 1 0) * U 1 0 = ((‖U 1 0‖ : ℝ) : ℂ) ^ 2 := by
      rw [Complex.star_def]
      exact_mod_cast Complex.conj_mul' (U 1 0)
    rw [h1, h2] at hnorm
    exact_mod_cast hnorm
  · exact hform.trans (euler_core (U 0 0) (U 1 0) u₁ u₂ b ‖U 0 0‖ ‖U 1 0‖ hp hq hb hb2 hu₁)

/-- **Idle invariance under every special unitary**, from the flow and the cyclic lift. -/
theorem conjInv_idle {K : Set (W 3)}
    (hflow : ∀ t : ℝ, ∀ ω ∈ K, actT (KInfFoundations.rotLin t) ω ∈ K)
    (hcyc : ∀ ω ∈ K, actT (KInfFoundations.cycEquiv : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) ω ∈ K)
    {U : Matrix (Fin 2) (Fin 2) ℂ} (hU : IsSU U) : ConjInv K (tensorOf 1 U) := by
  obtain ⟨a, b, ha, hb, c, s, hcs, hUe⟩ := su_euler hU
  rw [hUe, tensorOf_one_mul, tensorOf_one_mul, rotRe_eq, tensorOf_one_mul, tensorOf_one_mul]
  exact conjInv_mul (conjInv_mul (conjInv_dUnit hflow a ha)
    (conjInv_mul (conjInv_mul (conjInv_cycH hcyc) (conjInv_dUnit hflow _ (dphase_unit c s hcs)))
      (conjInv_cyc hcyc))) (conjInv_dUnit hflow b hb)

/-! ### §I.4 — the controlled half -/

/-- **The controlled phase as a word in the gate and the flow.** -/
theorem rtrick (r : ℂ) (hr : star r * r = 1) :
    blockMat 1 Xm * blockMat (dUnit r) (dUnit r) * blockMat 1 Xm *
        blockMat (dUnit (star r)) (dUnit (star r)) = blockMat 1 (dUnit (star r ^ 2)) := by
  rw [blockMat_mul, blockMat_mul, blockMat_mul]
  congr 1
  · simp only [Matrix.one_mul, Matrix.mul_one, dUnit, Matrix.mul_fin_two, star_star,
      Matrix.one_fin_two]
    refine mat2_ext ?_ ?_ ?_ ?_ <;>
      first
        | ring1
        | linear_combination hr
  · simp only [dUnit, Xm, Matrix.mul_fin_two, star_star, star_pow]
    refine mat2_ext ?_ ?_ ?_ ?_ <;> ring1

/-- The controlled diagonal unit pairs. -/
theorem conjInv_ctrl_dUnit {K : Set (W 3)} (hc : ConjInv K (blockMat 1 Xm))
    (hflow : ∀ t : ℝ, ∀ ω ∈ K, actT (KInfFoundations.rotLin t) ω ∈ K) (a : ℂ)
    (ha : star a * a = 1) : ConjInv K (blockMat 1 (dUnit a)) := by
  have hw : star (star a) * star a = 1 := by
    rw [star_star]
    linear_combination ha
  obtain ⟨r, hr, hr2⟩ := exists_unit_sqrt hw
  have e : dUnit a = dUnit (star r ^ 2) := by
    rw [← star_pow, hr2, star_star]
  have hsr : star (star r) * star r = 1 := by
    rw [star_star]
    linear_combination hr
  rw [e, ← rtrick r hr]
  refine conjInv_mul (conjInv_mul (conjInv_mul hc ?_) hc) ?_
  · rw [blockMat_same]
    exact conjInv_dUnit hflow r hr
  · rw [blockMat_same]
    exact conjInv_dUnit hflow (star r) hsr

/-- The controlled real rotations, conjugates of controlled diagonal pairs by idle cyclic lifts. -/
theorem conjInv_ctrl_rotRe {K : Set (W 3)} (hc : ConjInv K (blockMat 1 Xm))
    (hflow : ∀ t : ℝ, ∀ ω ∈ K, actT (KInfFoundations.rotLin t) ω ∈ K)
    (hcyc : ∀ ω ∈ K, actT (KInfFoundations.cycEquiv : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) ω ∈ K)
    (c s : ℝ) (h : c ^ 2 + s ^ 2 = 1) : ConjInv K (blockMat 1 (rotRe c s)) := by
  have hCu : cycMatᴴ * cycMat = 1 := isSU_unitary cycMat_isSU
  have e : blockMat 1 (rotRe c s) = blockMat cycMatᴴ cycMatᴴ *
      blockMat 1 (dUnit ((c : ℂ) - (s : ℂ) * Complex.I)) * blockMat cycMat cycMat := by
    rw [blockMat_mul, blockMat_mul, Matrix.mul_one, hCu, ← rotRe_eq]
  rw [e]
  refine conjInv_mul (conjInv_mul ?_ (conjInv_ctrl_dUnit hc hflow _ (dphase_unit c s h))) ?_
  · rw [blockMat_same]
    exact conjInv_cycH hcyc
  · rw [blockMat_same]
    exact conjInv_cyc hcyc

/-- **Controlled invariance under every special unitary.** -/
theorem conjInv_ctrl {K : Set (W 3)} (hc : ConjInv K (blockMat 1 Xm))
    (hflow : ∀ t : ℝ, ∀ ω ∈ K, actT (KInfFoundations.rotLin t) ω ∈ K)
    (hcyc : ∀ ω ∈ K, actT (KInfFoundations.cycEquiv : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) ω ∈ K)
    {V : Matrix (Fin 2) (Fin 2) ℂ} (hV : IsSU V) : ConjInv K (blockMat 1 V) := by
  obtain ⟨a, b, ha, hb, c, s, hcs, hVe⟩ := su_euler hV
  have e : blockMat 1 V = blockMat 1 (dUnit a) * blockMat 1 (rotRe c s) * blockMat 1 (dUnit b) := by
    rw [blockMat_mul, blockMat_mul, Matrix.one_mul, Matrix.one_mul, ← hVe]
  rw [e]
  exact conjInv_mul (conjInv_mul (conjInv_ctrl_dUnit hc hflow a ha)
    (conjInv_ctrl_rotRe hc hflow hcyc c s hcs)) (conjInv_ctrl_dUnit hc hflow b hb)

/-! ### §I.5 — block invariance, `ReachPure`, and the schema without it -/

/-- **Block invariance from the gate and the clause's two operations at every angle** — exact finite
words, no closure. -/
theorem blockInvariant_of_drive {K : Set (W 3)} (hH2 : ∀ ω ∈ K, cnot ω ∈ K)
    (hA : ∀ t : ℝ, ∀ ω ∈ K, actT (KInfFoundations.rotLin t) ω ∈ K ∧
      actT (KInfFoundations.cycEquiv : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) ω ∈ K) :
    BlockInvariant K := by
  have hflow : ∀ t : ℝ, ∀ ω ∈ K, actT (KInfFoundations.rotLin t) ω ∈ K :=
    fun t ω hω => (hA t ω hω).1
  have hcyc : ∀ ω ∈ K, actT (KInfFoundations.cycEquiv : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) ω ∈ K :=
    fun ω hω => (hA 0 ω hω).2
  have hc : ConjInv K (blockMat 1 Xm) := conjInv_cnot hH2
  intro U₀ U₁ hU₀ hU₁ ω hω
  have hu : U₀ᴴ * U₀ = 1 := isSU_unitary hU₀
  have e : blockMat U₀ U₁ = blockMat 1 (U₁ * U₀ᴴ) * blockMat U₀ U₀ := by
    rw [blockMat_mul, Matrix.one_mul, Matrix.mul_assoc, hu, Matrix.mul_one]
  have hW : IsSU (U₁ * U₀ᴴ) := isSU_mul hU₁ (isSU_conjTranspose hU₀)
  have hI : ConjInv K (blockMat U₀ U₀) := by
    rw [blockMat_same]
    exact conjInv_idle hflow hcyc hU₀
  show coordOf (blockMat U₀ U₁ * dict ω * (blockMat U₀ U₁)ᴴ) ∈ K
  rw [e]
  exact conjInv_mul (conjInv_ctrl hc hflow hcyc hW) hI ω hω

theorem cnot_mem_driveWords : (cnot : W 3 →ₗ[ℝ] W 3) ∈ driveWords :=
  Submonoid.subset_closure (Set.mem_union_left _ (Set.mem_union_left _ (Set.mem_singleton _)))

theorem rot_mem_driveWords (t : ℝ) : actTLin (KInfFoundations.rotLin t) ∈ driveWords :=
  Submonoid.subset_closure (Set.mem_union_left _ (Set.mem_union_right _ (Set.mem_range_self t)))

theorem cyc_mem_driveWords :
    actTLin (KInfFoundations.cycEquiv : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) ∈ driveWords :=
  Submonoid.subset_closure (Set.mem_union_right _ (Set.mem_singleton _))

/-- The scaled drive images of product states of the ball. -/
def driveOrbit : Set (W 3) :=
  {ω | ∃ g ∈ driveWords, ∃ x₀ ∈ TransitiveBody.eball 3, ∃ y₀ ∈ TransitiveBody.eball 3,
    ∃ c : ℝ, 0 ≤ c ∧ ω = c • g (prodState x₀ y₀)}

theorem driveOrbit_gen {g' : Module.End ℝ (W 3)} (hg' : g' ∈ driveWords) :
    ∀ ω ∈ driveOrbit, g' ω ∈ driveOrbit := by
  rintro ω ⟨g, hg, x₀, hx₀, y₀, hy₀, c, hc, rfl⟩
  exact ⟨g' * g, driveWords.mul_mem hg' hg, x₀, hx₀, y₀, hy₀, c, hc, by rw [map_smul]; rfl⟩

/-- **`ReachPure` is a theorem**: every pure two-token state is, up to a nonnegative scale, a drive
word applied to a product state of the ball (S6's lemma L4, no longer a hypothesis). -/
theorem reachPure : ReachPure := by
  intro x
  have hH2 : ∀ ω ∈ driveOrbit, cnot ω ∈ driveOrbit :=
    fun ω hω => driveOrbit_gen cnot_mem_driveWords ω hω
  have hA : ∀ t : ℝ, ∀ ω ∈ driveOrbit, actT (KInfFoundations.rotLin t) ω ∈ driveOrbit ∧
      actT (KInfFoundations.cycEquiv : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) ω ∈ driveOrbit :=
    fun t ω hω => ⟨driveOrbit_gen (rot_mem_driveWords t) ω hω,
      driveOrbit_gen cyc_mem_driveWords ω hω⟩
  have hB : BlockInvariant driveOrbit := blockInvariant_of_drive hH2 hA
  obtain ⟨U₀, U₁, hU₀, hU₁, x₀, hx₀, c, hc, h⟩ := reach_block x
  have hmem : c • prodState x₀ z3 ∈ driveOrbit :=
    ⟨1, driveWords.one_mem, x₀, hx₀, z3, z3_mem_eball, c, hc, rfl⟩
  obtain ⟨g, hg, x₁, hx₁, y₁, hy₁, c₁, hc₁, he⟩ := hB U₀ U₁ hU₀ hU₁ _ hmem
  refine ⟨g, hg, x₁, hx₁, y₁, hy₁, c₁, hc₁, ?_⟩
  rw [← he, dict_blockAct, h]

/-- **The pair-level K2 schema without `ReachPure`**: products (H1), the gate (H2), self-duality
(H3) and the clause's two operations at every angle (A_miss) force `K = Q3`. -/
theorem pairCone_eq_Q3_of_drive_exact {K : Set (W 3)}
    (hH1 : ∀ x ∈ TransitiveBody.eball 3, ∀ y ∈ TransitiveBody.eball 3, prodState x y ∈ K)
    (hH2 : ∀ ω ∈ K, cnot ω ∈ K) (hH3 : K = dualW K)
    (hA : ∀ t : ℝ, ∀ ω ∈ K, actT (KInfFoundations.rotLin t) ω ∈ K ∧
      actT (KInfFoundations.cycEquiv : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) ω ∈ K) : K = Q3 :=
  pairCone_eq_Q3_of_block hH1 hH3 (blockInvariant_of_drive hH2 hA)

/-- **`Q3` is invariant under the gate** (the necessity of H2, invariance only). -/
theorem Q3_cnot : ∀ ω ∈ Q3, cnot ω ∈ Q3 := by
  intro ω hω
  have hω' : (dict ω).PosSemidef := hω
  show (dict (cnot ω)).PosSemidef
  rw [dict_cnot_block]
  exact hω'.mul_mul_conjTranspose_same _

/-- **The full-flow form as an equivalence.** Given H1 and H3, the pair cone is `Q3` exactly when it
is invariant under the gate and under the clause's two operations at every angle. The direction `→`
is `Q3_cnot` with `Q3_aMiss`; the direction `←` is `pairCone_eq_Q3_of_drive_exact`. -/
theorem pairCone_eq_Q3_iff_drive_exact {K : Set (W 3)}
    (hH1 : ∀ x ∈ TransitiveBody.eball 3, ∀ y ∈ TransitiveBody.eball 3, prodState x y ∈ K)
    (hH3 : K = dualW K) :
    K = Q3 ↔ ((∀ ω ∈ K, cnot ω ∈ K) ∧ ∀ t : ℝ, ∀ ω ∈ K, actT (KInfFoundations.rotLin t) ω ∈ K ∧
      actT (KInfFoundations.cycEquiv : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) ω ∈ K) := by
  constructor
  · rintro rfl
    exact ⟨Q3_cnot, Q3_aMiss⟩
  · rintro ⟨hH2, hA⟩
    exact pairCone_eq_Q3_of_drive_exact hH1 hH2 hH3 hA

end

end EqvK2Generation
end OIBridge

#print axioms OIBridge.EqvK2Generation.blockMat_mul
#print axioms OIBridge.EqvK2Generation.cycMat_conjTranspose_eq
#print axioms OIBridge.EqvK2Generation.rotRe_eq
#print axioms OIBridge.EqvK2Generation.su_euler
#print axioms OIBridge.EqvK2Generation.conjInv_idle
#print axioms OIBridge.EqvK2Generation.rtrick
#print axioms OIBridge.EqvK2Generation.conjInv_ctrl
#print axioms OIBridge.EqvK2Generation.blockInvariant_of_drive
#print axioms OIBridge.EqvK2Generation.reachPure
#print axioms OIBridge.EqvK2Generation.pairCone_eq_Q3_of_drive_exact
#print axioms OIBridge.EqvK2Generation.Q3_cnot
#print axioms OIBridge.EqvK2Generation.pairCone_eq_Q3_iff_drive_exact
