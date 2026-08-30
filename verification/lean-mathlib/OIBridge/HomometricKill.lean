/-
  OIBridge/HomometricKill.lean — the six-mode analytic middle, closed in the kernel.

  HomometricSix.lean proved the two ENDPOINTS of the n = 6 kill chain: `flat_locus` (only flat
  moduli survive the pulled-back four-cycle identities) and `no_six_orthogonal` (the clique
  obstruction over the eight common mask zeros). This file closes the ANALYTIC MIDDLE that
  connects them, in the three pieces of the programme:

    1. `line_forcing` — coefficient-line forcing: equality of a rank-one coefficient matrix
       z' z'^† = z z^† with a nonvanishing reference entry forces z' = λ z with λ unimodular.

    2. `monomial_relations` — the multiplicative phase theorem, replacing the Smith-normal-form
       discovery computation by its actual consequence: every nonvanishing solution of the four
       pulled-back triangle relations satisfies the cleared monomial identities
           h₃ h₀³ = h₁² h₂²,   h₄ h₀⁵ = h₁⁴ h₂²,   h₅ h₀⁷ = h₁⁵ h₂³,
       i.e. h_a = h₀ s^{u2 a} t^{u3 a} with s = h₁/h₀, t = h₂/h₀. The proof is explicit
       elimination: each identity is a `linear_combination` of at most three relation instances
       with coefficients built from monomials, followed by cancellation of a nonvanishing
       monomial. No torsion can hide because no roots are ever extracted.

    3. `torus_zeros` — the torus-zero bridge: unimodular x, y with both masks vanishing lie in
       eight explicit points. The probe's resultant collapses in the kernel to one line — the
       two cofactors differ by y (1 − x)(1 + x²) — so common zeros need x ∈ {1, i, −i} where the
       quadratics in y factor by inspection; the shared factor 1 + x + x²y forces x² + x + 1 = 0
       on the torus and then y = 1.

  Plus the modulus stage (`flat_of_products`: the multiplicative K4 identities push through
  `Real.log` into the field-generic `flat_locus`). Unimodularity is carried everywhere in the
  algebraic form x · conj x = 1 — the form the flat moduli actually produce — so no norm API
  enters the chain. The assembly `homometricSix_unrealizable` follows in this file after the
  exponent identification of the eight points.
-/
import OIBridge.HomometricSix
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Data.Matrix.Basic
import Mathlib.LinearAlgebra.Matrix.ConjTranspose
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.IntervalCases

namespace OIBridge
namespace HomometricSix

open Complex

local notation "conj'" => (starRingEnd ℂ)

/-- PIECE 1: coefficient-line forcing. A rank-one coefficient matrix equality with one
nonvanishing reference entry forces the two lines to agree up to a unimodular scalar. -/
theorem line_forcing {ι : Type*} (z z' : ι → ℂ) (i₀ : ι) (h0 : z i₀ ≠ 0)
    (hC : ∀ i j, z' i * conj' (z' j) = z i * conj' (z j)) :
    ∃ lam : ℂ, lam * conj' lam = 1 ∧ ∀ i, z' i = lam * z i := by
  have hmc := hC i₀ i₀
  have hcz : conj' (z i₀) ≠ 0 := by simpa using h0
  have hz0 : z i₀ * conj' (z i₀) ≠ 0 := mul_ne_zero h0 hcz
  have h0' : z' i₀ ≠ 0 := by
    intro h
    rw [h, zero_mul] at hmc
    exact hz0 hmc.symm
  refine ⟨z' i₀ / z i₀, ?_, ?_⟩
  · rw [map_div₀]
    rw [div_mul_div_comm, div_eq_one_iff_eq (by exact mul_ne_zero h0 hcz)]
    exact hmc
  · intro i
    have hi := hC i i₀
    rw [div_mul_eq_mul_div, eq_div_iff h0]
    have hcz' : conj' (z' i₀) ≠ 0 := by simpa using h0'
    apply mul_right_cancel₀ hcz'
    calc z' i * z i₀ * conj' (z' i₀)
        = z' i * conj' (z' i₀) * z i₀ := by ring
      _ = z i * conj' (z i₀) * z i₀ := by rw [hi]
      _ = z i * (z i₀ * conj' (z i₀)) := by ring
      _ = z i * (z' i₀ * conj' (z' i₀)) := by rw [← hmc]
      _ = z' i₀ * z i * conj' (z' i₀) := by ring

/-- MODULUS STAGE: positive edge products satisfying the pulled-back multiplicative identities
force a flat source row, through `Real.log` and the field-generic `flat_locus`. -/
theorem flat_of_products (p q : Fin 6 → ℝ) (hp : ∀ a, 0 < p a) (hq : ∀ c, 0 < q c)
    (hrel : ∀ a b : Fin 6, a < b → q (mu a b).1 * q (mu a b).2 = p a * p b) :
    ∀ a, p a = p 0 := by
  have hinv : ∀ c d : Fin 6, c < d →
      p (muInv c d).1 * p (muInv c d).2 = q c * q d := by
    intro c d hcd
    obtain ⟨hasc, hmm⟩ := mu_muInv c d hcd
    have := hrel (muInv c d).1 (muInv c d).2 hasc
    rw [hmm] at this
    linarith
  have hSL : ∀ c d : Fin 6, c < d →
      SL (fun a => Real.log (p a)) (muInv c d) = Real.log (q c) + Real.log (q d) := by
    intro c d hcd
    have h1 : Real.log (p (muInv c d).1 * p (muInv c d).2)
        = Real.log (q c * q d) := by rw [hinv c d hcd]
    rw [Real.log_mul (ne_of_gt (hp _)) (ne_of_gt (hp _)),
      Real.log_mul (ne_of_gt (hq _)) (ne_of_gt (hq _))] at h1
    simpa [SL] using h1
  have hPR : PulledRel (fun a => Real.log (p a)) := by
    intro c d e f hcd hde hef
    constructor
    · rw [hSL c d hcd, hSL e f hef, hSL c e (lt_trans hcd hde), hSL d f (lt_trans hde hef)]
      ring
    · rw [hSL c d hcd, hSL e f hef,
        hSL c f (lt_trans (lt_trans hcd hde) hef), hSL d e hde]
      ring
  have hconst := (flat_locus (fun a => Real.log (p a))).mp hPR
  intro a
  have hla : Real.log (p a) = Real.log (p 0) := hconst a
  calc p a = Real.exp (Real.log (p a)) := (Real.exp_log (hp a)).symm
    _ = Real.exp (Real.log (p 0)) := by rw [hla]
    _ = p 0 := Real.exp_log (hp 0)

/-- PIECE 2: the multiplicative phase theorem, by explicit elimination. The four hypotheses are
the pulled-back triangle identities of the target triangles (0,1,2), (0,1,3), (0,1,4), (3,4,5)
in cleared form; the conclusions are the cleared monomial identities
`h_a h₀^{u2 a + u3 a − 1} = h₁^{u2 a} h₂^{u3 a}` for a = 3, 4, 5. -/
theorem monomial_relations (h : Fin 6 → ℂ) (hnz : ∀ a, h a ≠ 0)
    (r1 : h 0 * h 3 * h 4 = h 1 * h 5 * h 2)
    (r2 : h 0 * h 0 * h 4 = h 1 * h 1 * h 3)
    (r3 : h 0 * h 0 * h 5 = h 1 * h 4 * h 2)
    (r4 : h 3 * h 0 * h 3 = h 4 * h 2 * h 2) :
    h 3 * h 0 ^ 3 = h 1 ^ 2 * h 2 ^ 2
    ∧ h 4 * h 0 ^ 5 = h 1 ^ 4 * h 2 ^ 2
    ∧ h 5 * h 0 ^ 7 = h 1 ^ 5 * h 2 ^ 3 := by
  have c3 : h 3 * h 0 ^ 3 * (h 4 * h 5) = h 1 ^ 2 * h 2 ^ 2 * (h 4 * h 5) := by
    linear_combination (h 0 ^ 2 * h 5) * r1 + (h 1 * h 5 * h 2) * r3
  have c4 : h 4 * h 0 ^ 5 * (h 3 ^ 2 * h 4) = h 1 ^ 4 * h 2 ^ 2 * (h 3 ^ 2 * h 4) := by
    linear_combination (h 0 ^ 2 * h 4) ^ 2 * r4
      + (h 4 * h 2 ^ 2) * ((h 0 ^ 2 * h 4) + (h 1 ^ 2 * h 3)) * r2
  have c5 : h 5 * h 0 ^ 7 * (h 3 * h 4 ^ 2 * h 5)
      = h 1 ^ 5 * h 2 ^ 3 * (h 3 * h 4 ^ 2 * h 5) := by
    linear_combination (h 0 ^ 2 * h 4) * (h 0 ^ 2 * h 5) ^ 2 * r1
      + (h 1 * h 5 * h 2) * (h 0 ^ 2 * h 5) ^ 2 * r2
      + (h 1 * h 5 * h 2) * (h 1 ^ 2 * h 3) * ((h 0 ^ 2 * h 5) + (h 1 * h 4 * h 2)) * r3
  exact ⟨mul_right_cancel₀ (mul_ne_zero (hnz 4) (hnz 5)) c3,
    mul_right_cancel₀ (mul_ne_zero (pow_ne_zero 2 (hnz 3)) (hnz 4)) c4,
    mul_right_cancel₀
      (mul_ne_zero (mul_ne_zero (hnz 3) (pow_ne_zero 2 (hnz 4))) (hnz 5)) c5⟩

/-- The primitive cube root of unity, as a radical. -/
noncomputable def om : ℂ := ⟨-1/2, Real.sqrt 3 / 2⟩

lemma om_quad : om ^ 2 + om + 1 = 0 := by
  have h3 : Real.sqrt 3 * Real.sqrt 3 = 3 := Real.mul_self_sqrt (by norm_num)
  apply Complex.ext <;>
    simp [om, pow_two, Complex.mul_re, Complex.mul_im, Complex.add_re, Complex.add_im] <;>
    nlinarith [h3]

lemma om_cube : om ^ 3 = 1 := by
  linear_combination (om - 1) * om_quad

/-- PIECE 3: the torus-zero bridge, with unimodularity in the form `x * conj x = 1`. -/
theorem torus_zeros (x y : ℂ) (hxc : x * conj' x = 1) (hyc : y * conj' y = 1)
    (hF : 1 + x + y + x^2*y^2 + x^4*y^2 + x^5*y^3 = 0)
    (hFt : 1 + x + x^4*y + x^3*y^2 + x^5*y^2 + x^5*y^3 = 0) :
    (x = om ∧ y = 1) ∨ (x = om ^ 2 ∧ y = 1)
    ∨ (x = 1 ∧ y = I) ∨ (x = 1 ∧ y = -I)
    ∨ (x = I ∧ y = -1) ∨ (x = I ∧ y = -I)
    ∨ (x = -I ∧ y = -1) ∨ (x = -I ∧ y = I) := by
  have hyne : y ≠ 0 := by
    intro h; rw [h, zero_mul] at hyc; exact zero_ne_one hyc
  by_cases hG : 1 + x + x^2*y = 0
  · -- the shared factor: |1 + x| = 1 forces x² + x + 1 = 0, then y = 1
    have hGe : x^2*y = -(1+x) := by linear_combination hG
    have h1 : (1 + x) * (1 + conj' x) = 1 := by
      have step : (1 + x) * conj' (1 + x) = (x^2*y) * conj' (x^2*y) := by
        rw [hGe, map_neg]; ring
      rw [map_add, map_one] at step
      rw [step]
      calc (x^2*y) * conj' (x^2*y)
          = (x * conj' x)^2 * (y * conj' y) := by
            simp only [map_mul, map_pow]; ring
        _ = 1 := by rw [hxc, hyc]; ring
    have hsum : x + conj' x = -1 := by
      linear_combination h1 - hxc
    have hquad : x ^ 2 + x + 1 = 0 := by
      linear_combination x * hsum - hxc + x * conj' x * (1:ℂ) * 0 + (hxc - hxc)
    have hfac : (x - om) * (x - om ^ 2) = 0 := by
      linear_combination hquad - x * om_quad + om_cube
    have hx1 : x + 1 ≠ 0 := by
      intro hcontr
      have hxm : x = -1 := by linear_combination hcontr
      rw [hxm] at hquad
      norm_num at hquad
    have hy1 : y = 1 := by
      have hstep : (x + 1) * y = (x + 1) * 1 := by
        linear_combination y * hquad - hG
      exact mul_left_cancel₀ hx1 hstep
    rcases mul_eq_zero.mp hfac with hcase | hcase
    · exact Or.inl ⟨by linear_combination hcase, hy1⟩
    · exact Or.inr (Or.inl ⟨by linear_combination hcase, hy1⟩)
  · -- the cofactors: common zeros need x ∈ {1, i, −i}, then the quadratics factor
    have hH : 1 + y - x*y + x^3*y^2 = 0 := by
      rcases mul_eq_zero.mp (show (1 + x + x^2*y) * (1 + y - x*y + x^3*y^2) = 0 by
        linear_combination hF) with hcase | hcase
      · exact absurd hcase hG
      · exact hcase
    have hHt : 1 - x^2*y + x^3*y + x^3*y^2 = 0 := by
      rcases mul_eq_zero.mp (show (1 + x + x^2*y) * (1 - x^2*y + x^3*y + x^3*y^2) = 0 by
        linear_combination hFt) with hcase | hcase
      · exact absurd hcase hG
      · exact hcase
    have hxcase : (1 - x) * (1 + x^2) = 0 := by
      have hdiff : y * ((1 - x) * (1 + x^2)) = 0 := by linear_combination hH - hHt
      rcases mul_eq_zero.mp hdiff with hcase | hcase
      · exact absurd hcase hyne
      · exact hcase
    rcases mul_eq_zero.mp hxcase with hcase | hcase
    · -- x = 1: y² + 1 = 0
      have hx1 : x = 1 := by linear_combination -hcase
      rw [hx1] at hH
      have hyfac : (y - I) * (y + I) = 0 := by
        linear_combination hH - Complex.I_sq
      rcases mul_eq_zero.mp hyfac with hyc' | hyc'
      · exact Or.inr (Or.inr (Or.inl ⟨hx1, by linear_combination hyc'⟩))
      · exact Or.inr (Or.inr (Or.inr (Or.inl ⟨hx1, by linear_combination hyc'⟩)))
    · -- x² = −1: x = i or x = −i
      have hxfac : (x - I) * (x + I) = 0 := by
        linear_combination hcase - Complex.I_sq
      rcases mul_eq_zero.mp hxfac with hxc' | hxc'
      · -- x = i: (y + 1)(y + i) = 0
        have hxI : x = I := by linear_combination hxc'
        rw [hxI] at hH
        have hyfac : (y + 1) * (y + I) = 0 := by
          linear_combination I * hH + (y - y^2*(I^2 - 1)) * Complex.I_sq
        rcases mul_eq_zero.mp hyfac with hyc' | hyc'
        · exact Or.inr (Or.inr (Or.inr (Or.inr (Or.inl ⟨hxI, by linear_combination hyc'⟩))))
        · exact Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inl
            ⟨hxI, by linear_combination hyc'⟩)))))
      · -- x = −i: (y + 1)(y − i) = 0
        have hxI : x = -I := by linear_combination hxc'
        rw [hxI] at hH
        have hyfac : (y + 1) * (y - I) = 0 := by
          linear_combination (-I) * hH + (y - y^2*(I^2 - 1)) * Complex.I_sq
        rcases mul_eq_zero.mp hyfac with hyc' | hyc'
        · exact Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inl
            ⟨hxI, by linear_combination hyc'⟩))))))
        · exact Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr
            ⟨hxI, by linear_combination hyc'⟩))))))

/-- The primitive twelfth root of unity, born from the radicals already in play:
ζ = e^{iπ/6} = (−i)·ω. All its power identities follow from `om_cube` and `I² = −1` by ring. -/
noncomputable def zeta : ℂ := -I * om

lemma om_unit : om * conj' om = 1 := by
  have h3 : Real.sqrt 3 * Real.sqrt 3 = 3 := Real.mul_self_sqrt (by norm_num)
  apply Complex.ext <;>
    simp [om, Complex.mul_re, Complex.mul_im, Complex.conj_re, Complex.conj_im] <;>
    nlinarith [h3]

lemma om_ne_one : om ≠ 1 := by
  intro h
  have him := congrArg Complex.im h
  simp [om] at him

lemma zeta_ne_zero : zeta ≠ 0 := by
  intro h
  have : om = 0 := by
    rcases mul_eq_zero.mp h with hcase | hcase
    · exfalso
      apply Complex.I_ne_zero
      linear_combination -hcase
    · exact hcase
  have := congrArg Complex.im this
  simp [om] at this

lemma zeta_pow3 : zeta ^ 3 = I := by
  show (-I * om) ^ 3 = I
  rw [mul_pow, om_cube, mul_one]
  linear_combination (-I) * Complex.I_sq

lemma zeta_pow4 : zeta ^ 4 = om := by
  show (-I * om) ^ 4 = om
  rw [mul_pow]
  have h4 : (-I) ^ 4 = 1 := by
    linear_combination (I^2 - 1) * Complex.I_sq
  have hom4 : om ^ 4 = om := by
    calc om ^ 4 = om ^ 3 * om := by ring
      _ = om := by rw [om_cube, one_mul]
  rw [h4, hom4, one_mul]

lemma zeta_pow6 : zeta ^ 6 = -1 := by
  calc zeta ^ 6 = (zeta ^ 3) ^ 2 := by ring
    _ = I ^ 2 := by rw [zeta_pow3]
    _ = -1 := Complex.I_sq

lemma zeta_pow8 : zeta ^ 8 = om ^ 2 := by
  calc zeta ^ 8 = (zeta ^ 4) ^ 2 := by ring
    _ = om ^ 2 := by rw [zeta_pow4]

lemma zeta_pow9 : zeta ^ 9 = -I := by
  calc zeta ^ 9 = zeta ^ 6 * zeta ^ 3 := by ring
    _ = -1 * I := by rw [zeta_pow6, zeta_pow3]
    _ = -I := by ring

lemma zeta_pow12 : zeta ^ 12 = 1 := by
  calc zeta ^ 12 = (zeta ^ 6) ^ 2 := by ring
    _ = (-1) ^ 2 := by rw [zeta_pow6]
    _ = 1 := by ring

lemma zeta_unit : zeta * conj' zeta = 1 := by
  show (-I * om) * conj' (-I * om) = 1
  rw [map_mul, map_neg, Complex.conj_I]
  calc -I * om * (- -I * conj' om) = (-I * - -I) * (om * conj' om) := by ring
    _ = (-I * - -I) * 1 := by rw [om_unit]
    _ = 1 := by linear_combination -Complex.I_sq

lemma neg_one_ne_one' : (-1 : ℂ) ≠ 1 := by
  intro hcontr
  have := congrArg Complex.re hcontr
  norm_num at this

lemma orderOf_zeta : orderOf zeta = 12 := by
  apply orderOf_eq_of_pow_and_pow_div_prime (by norm_num) zeta_pow12
  intro p hp hdvd
  have hp23 : p = 2 ∨ p = 3 := by
    have h1 := hp.two_le
    have h2 : p ≤ 12 := Nat.le_of_dvd (by norm_num) hdvd
    interval_cases p <;> revert hdvd <;> revert hp <;> decide
  rcases hp23 with hcase | hcase
  · rw [hcase, show (12/2 : ℕ) = 6 from rfl, zeta_pow6]
    exact neg_one_ne_one'
  · rw [hcase, show (12/3 : ℕ) = 4 from rfl, zeta_pow4]
    exact om_ne_one

lemma orderOf_I : orderOf (I : ℂ) = 4 := by
  apply orderOf_eq_of_pow_and_pow_div_prime (by norm_num) (by
    linear_combination (I^2 - 1) * Complex.I_sq)
  intro p hp hdvd
  have hp2 : p = 2 := by
    have h1 := hp.two_le
    have h2 : p ≤ 4 := Nat.le_of_dvd (by norm_num) hdvd
    interval_cases p <;> revert hdvd <;> revert hp <;> decide
  rw [hp2, show (4/2 : ℕ) = 2 from rfl, Complex.I_sq]
  exact neg_one_ne_one'

lemma I_unit : (I:ℂ) * conj' I = 1 := by
  rw [Complex.conj_I]
  linear_combination -Complex.I_sq

/-- Each of the eight torus-zero points is an exponent pair from the connection set. -/
lemma point_to_exponent {x y : ℂ}
    (hd : (x = om ∧ y = 1) ∨ (x = om ^ 2 ∧ y = 1)
      ∨ (x = 1 ∧ y = I) ∨ (x = 1 ∧ y = -I)
      ∨ (x = I ∧ y = -1) ∨ (x = I ∧ y = -I)
      ∨ (x = -I ∧ y = -1) ∨ (x = -I ∧ y = I)) :
    ∃ pq : ZMod 12 × ZMod 4, pq ∈ conn
      ∧ x = zeta ^ (pq.1.val) ∧ y = I ^ (pq.2.val) := by
  have hI2 : (I:ℂ) ^ 2 = -1 := Complex.I_sq
  have hI3 : (I:ℂ) ^ 3 = -I := by linear_combination I * Complex.I_sq
  rcases hd with ⟨hx, hy⟩ | ⟨hx, hy⟩ | ⟨hx, hy⟩ | ⟨hx, hy⟩
    | ⟨hx, hy⟩ | ⟨hx, hy⟩ | ⟨hx, hy⟩ | ⟨hx, hy⟩
  · refine ⟨(4, 0), by decide, ?_, ?_⟩
    · rw [hx, show (((4:ZMod 12), (0:ZMod 4)).1).val = 4 from rfl, zeta_pow4]
    · rw [hy, show (((4:ZMod 12), (0:ZMod 4)).2).val = 0 from rfl, pow_zero]
  · refine ⟨(8, 0), by decide, ?_, ?_⟩
    · rw [hx, show (((8:ZMod 12), (0:ZMod 4)).1).val = 8 from rfl, zeta_pow8]
    · rw [hy, show (((8:ZMod 12), (0:ZMod 4)).2).val = 0 from rfl, pow_zero]
  · refine ⟨(0, 1), by decide, ?_, ?_⟩
    · rw [hx, show (((0:ZMod 12), (1:ZMod 4)).1).val = 0 from rfl, pow_zero]
    · rw [hy, show (((0:ZMod 12), (1:ZMod 4)).2).val = 1 from rfl, pow_one]
  · refine ⟨(0, 3), by decide, ?_, ?_⟩
    · rw [hx, show (((0:ZMod 12), (3:ZMod 4)).1).val = 0 from rfl, pow_zero]
    · rw [hy, show (((0:ZMod 12), (3:ZMod 4)).2).val = 3 from rfl, hI3]
  · refine ⟨(3, 2), by decide, ?_, ?_⟩
    · rw [hx, show (((3:ZMod 12), (2:ZMod 4)).1).val = 3 from rfl, zeta_pow3]
    · rw [hy, show (((3:ZMod 12), (2:ZMod 4)).2).val = 2 from rfl, hI2]
  · refine ⟨(3, 3), by decide, ?_, ?_⟩
    · rw [hx, show (((3:ZMod 12), (3:ZMod 4)).1).val = 3 from rfl, zeta_pow3]
    · rw [hy, show (((3:ZMod 12), (3:ZMod 4)).2).val = 3 from rfl, hI3]
  · refine ⟨(9, 2), by decide, ?_, ?_⟩
    · rw [hx, show (((9:ZMod 12), (2:ZMod 4)).1).val = 9 from rfl, zeta_pow9]
    · rw [hy, show (((9:ZMod 12), (2:ZMod 4)).2).val = 2 from rfl, hI2]
  · refine ⟨(9, 1), by decide, ?_, ?_⟩
    · rw [hx, show (((9:ZMod 12), (1:ZMod 4)).1).val = 9 from rfl, zeta_pow9]
    · rw [hy, show (((9:ZMod 12), (1:ZMod 4)).2).val = 1 from rfl, pow_one]

/-- Chained pair ratios collapse along a middle index with unit modulus. -/
lemma pair_chain (k : Fin 6 → ℂ) (hu : ∀ c, k c * conj' (k c) = 1) (c d e : Fin 6) :
    k c * conj' (k d) * (k d * conj' (k e)) = k c * conj' (k e) := by
  linear_combination (k c * conj' (k e)) * hu d

/-- Cleared form of a transported triangle relation: multiply through by the units. -/
lemma triangle_clear (h : Fin 6 → ℂ) (hu : ∀ a, h a * conj' (h a) = 1)
    (p1 q1 p2 q2 p3 q3 : Fin 6)
    (T : h p1 * conj' (h q1) * (h p2 * conj' (h q2)) = h p3 * conj' (h q3)) :
    h p1 * h p2 * h q3 = h q1 * h q2 * h p3 := by
  linear_combination (h q1 * h q2 * h q3) * T
    - (h p1 * h p2 * h q3) * hu q1
    - (h p1 * h p2 * h q3) * (h q1 * conj' (h q1)) * hu q2
    + (h q1 * h q2 * h p3) * hu q3

/-- Balanced unimodular monomials with matching exponent excess agree. -/
lemma pow_shift {u v : ℂ} (huv : u * v = 1) {m1 m2 n1 n2 : ℕ} (hmn : m1 + n2 = n1 + m2) :
    u ^ m1 * v ^ m2 = u ^ n1 * v ^ n2 := by
  have hu : u ≠ 0 := left_ne_zero_of_mul_eq_one huv
  have hv : v ≠ 0 := right_ne_zero_of_mul_eq_one huv
  apply mul_right_cancel₀ (mul_ne_zero (pow_ne_zero n2 hu) (pow_ne_zero n1 hv))
  calc u ^ m1 * v ^ m2 * (u ^ n2 * v ^ n1)
      = u ^ (m1 + n2) * v ^ (m2 + n1) := by rw [pow_add, pow_add]; ring
    _ = (u * v) ^ (n1 + m2) := by rw [hmn, add_comm m2 n1, mul_pow]
    _ = (u * v) ^ (n1 + n2) := by rw [huv, one_pow, one_pow]
    _ = u ^ (n1 + n2) * v ^ (n1 + n2) := mul_pow u v _
    _ = u ^ n1 * v ^ n2 * (u ^ n2 * v ^ n1) := by rw [pow_add, pow_add]; ring

/-- A monomial in unimodular elements is unimodular. -/
lemma unit_monomial {S T : ℂ} (hS : S * conj' S = 1) (hT : T * conj' T = 1) (m n : ℕ) :
    (S ^ m * T ^ n) * conj' (S ^ m * T ^ n) = 1 := by
  rw [map_mul, map_pow, map_pow]
  calc S ^ m * T ^ n * (conj' S ^ m * conj' T ^ n)
      = (S * conj' S) ^ m * (T * conj' T) ^ n := by rw [mul_pow, mul_pow]; ring
    _ = 1 := by rw [hS, hT, one_pow, one_pow, mul_one]

/-- Reconstruct a potential from a unit pair ratio. -/
lemma potential_step {k0 kc w : ℂ} (huc : kc * conj' kc = 1) (huw : w * conj' w = 1)
    (hrel : k0 * conj' kc = conj' w) : kc = k0 * w := by
  linear_combination (-(w * kc)) * hrel + (k0 * w) * huc + (-kc) * huw

/-- Equal powers of an element of known finite order have equal exponents mod that order. -/
lemma pow_eq_pow_zmod {g : ℂ} (hg : g ≠ 0) {n : ℕ} (hn : orderOf g = n)
    {m k : ℕ} (hmk : g ^ m = g ^ k) : (m : ZMod n) = (k : ZMod n) := by
  have hu : (Units.mk0 g hg) ^ m = (Units.mk0 g hg) ^ k := by
    ext
    push_cast
    exact hmk
  have horder : orderOf (Units.mk0 g hg) = n := by
    rw [← orderOf_units]
    exact hn
  have hmod : m ≡ k [MOD n] := by
    rw [← horder]
    exact pow_eq_pow_iff_modEq.mp hu
  exact (ZMod.natCast_eq_natCast_iff m k n).mpr hmod

section Assembly

variable (V W : Matrix (Fin 6) (Fin 6) ℂ)

/-- THE ASSEMBLED KILL. The forced non-two-branch six-mode correspondence μ admits NO pair of
unitary eigenbases with all overlaps nonzero: if every coefficient line of W over the μ-image
pair matches that of V over the source pair, the hypotheses are contradictory. Combined with the
one-orbit census, this closes the coefficient reconstruction for the entire continuous
two-parameter Piccard family. -/
theorem homometricSix_unrealizable
    (hV : V * V.conjTranspose = 1) (hW : W * W.conjTranspose = 1)
    (hVnz : ∀ i a, V i a ≠ 0) (hWnz : ∀ i c, W i c ≠ 0)
    (hC : ∀ a b : Fin 6, a < b → ∀ i j : Fin 6,
      (W i (mu a b).1 * conj' (W i (mu a b).2))
        * conj' (W j (mu a b).1 * conj' (W j (mu a b).2))
      = (V i a * conj' (V i b)) * conj' (V j a * conj' (V j b))) :
    False := by
  -- ROW ORTHONORMALITY
  have hVrow : ∀ i j : Fin 6, (∑ a, V i a * conj' (V j a)) = if i = j then 1 else 0 := by
    intro i j
    have hmulapp := congrFun (congrFun hV i) j
    rw [Matrix.mul_apply] at hmulapp
    simp only [Matrix.conjTranspose_apply, Complex.star_def] at hmulapp
    rw [hmulapp, Matrix.one_apply]
  have hWrow : ∀ i j : Fin 6, (∑ c, W i c * conj' (W j c)) = if i = j then 1 else 0 := by
    intro i j
    have hmulapp := congrFun (congrFun hW i) j
    rw [Matrix.mul_apply] at hmulapp
    simp only [Matrix.conjTranspose_apply, Complex.star_def] at hmulapp
    rw [hmulapp, Matrix.one_apply]
  -- MODULUS STAGE: the diagonal coefficient lines force flat moduli
  have key2 : ∀ z w : ℂ, (z * conj' w) * conj' (z * conj' w)
      = ((normSq z * normSq w : ℝ) : ℂ) := by
    intro z w
    rw [map_mul, Complex.conj_conj]
    push_cast
    rw [← Complex.mul_conj, ← Complex.mul_conj]
    ring
  have hCdiag : ∀ i, ∀ a b : Fin 6, a < b →
      normSq (W i (mu a b).1) * normSq (W i (mu a b).2)
        = normSq (V i a) * normSq (V i b) := by
    intro i a b hab
    have hcd := hC a b hab i i
    rw [key2, key2] at hcd
    exact_mod_cast hcd
  have hPflat : ∀ i a, normSq (V i a) = 1/6 := by
    intro i a
    have hflat := flat_of_products (fun a => normSq (V i a)) (fun c => normSq (W i c))
      (fun a => normSq_pos.mpr (hVnz i a)) (fun c => normSq_pos.mpr (hWnz i c))
      (fun a b hab => hCdiag i a b hab)
    have hsum : (∑ a, normSq (V i a)) = 1 := by
      have hd := hVrow i i
      rw [if_pos rfl] at hd
      have hc : (∑ a, ((normSq (V i a) : ℝ) : ℂ)) = 1 := by
        rw [← hd]
        exact Finset.sum_congr rfl (fun a _ => (Complex.mul_conj (V i a)).symm)
      exact_mod_cast hc
    have h6 : normSq (V i 0) * 6 = 1 := by
      rw [← hsum, Fin.sum_univ_six, hflat 1, hflat 2, hflat 3, hflat 4, hflat 5]
      ring
    rw [hflat a]
    linarith
  have hQflat : ∀ i c, normSq (W i c) = 1/6 := by
    intro i c
    have hpair : ∀ c d : Fin 6, c < d → normSq (W i c) * normSq (W i d) = 1/36 := by
      intro c d hcd
      obtain ⟨hasc, hmm⟩ := mu_muInv c d hcd
      have hcc := hCdiag i (muInv c d).1 (muInv c d).2 hasc
      rw [hmm] at hcc
      rw [hcc, hPflat, hPflat]
      norm_num
    have hQpos : ∀ c, 0 < normSq (W i c) := fun c => normSq_pos.mpr (hWnz i c)
    have h01 := hpair 0 1 (by decide)
    have h12 := hpair 1 2 (by decide)
    have h02 := hpair 0 2 (by decide)
    have h0eq2 : normSq (W i 0) = normSq (W i 2) := by
      apply mul_left_cancel₀ (ne_of_gt (hQpos 1))
      calc normSq (W i 1) * normSq (W i 0) = 1/36 := by rw [mul_comm]; exact h01
        _ = normSq (W i 1) * normSq (W i 2) := h12.symm
    have h0 : normSq (W i 0) = 1/6 := by
      have hsq : normSq (W i 0) * normSq (W i 0) = 1/36 := by
        rw [← h0eq2] at h02
        exact h02
      have hfac : (normSq (W i 0) - 1/6) * (normSq (W i 0) + 1/6) = 0 := by
        linear_combination hsq
      rcases mul_eq_zero.mp hfac with hcase | hcase
      · linarith
      · exfalso
        have := hQpos 0
        linarith
    by_cases hc0 : c = 0
    · rw [hc0]
      exact h0
    · have hlt : (0 : Fin 6) < c := Fin.pos_of_ne_zero hc0
      have hpc := hpair 0 c hlt
      rw [h0] at hpc
      have := hQpos c
      nlinarith [hpc]
  -- UNIT FACTS at the entry level
  have hVc : ∀ i a, V i a * conj' (V i a) = ((1/6 : ℝ) : ℂ) := by
    intro i a
    rw [Complex.mul_conj, hPflat]
  have hWc : ∀ i c, W i c * conj' (W i c) = ((1/6 : ℝ) : ℂ) := by
    intro i c
    rw [Complex.mul_conj, hQflat]
  -- THE ROW-RATIO VECTORS
  set h : Fin 6 → Fin 6 → ℂ := fun i a => 6 * (V i a * conj' (V 0 a)) with hdef
  set hW' : Fin 6 → Fin 6 → ℂ := fun i c => 6 * (W i c * conj' (W 0 c)) with hdefW
  have hnzh : ∀ i a, h i a ≠ 0 := by
    intro i a
    simp only [hdef]
    exact mul_ne_zero (by norm_num)
      (mul_ne_zero (hVnz i a) (by simpa using hVnz 0 a))
  have hnzW : ∀ i c, hW' i c ≠ 0 := by
    intro i c
    simp only [hdefW]
    exact mul_ne_zero (by norm_num)
      (mul_ne_zero (hWnz i c) (by simpa using hWnz 0 c))
  have hunit : ∀ i a, h i a * conj' (h i a) = 1 := by
    intro i a
    simp only [hdef, map_mul, Complex.conj_conj, map_ofNat]
    have e1 := hVc i a
    have e2 := hVc 0 a
    have : (36 : ℂ) * ((1/6 : ℝ) : ℂ) * ((1/6 : ℝ) : ℂ) = 1 := by
      push_cast
      norm_num
    linear_combination (36 * (V 0 a * conj' (V 0 a))) * e1 + 36 * ((1/6:ℝ):ℂ) * e2 + this
  have hunitW : ∀ i c, hW' i c * conj' (hW' i c) = 1 := by
    intro i c
    simp only [hdefW, map_mul, Complex.conj_conj, map_ofNat]
    have e1 := hWc i c
    have e2 := hWc 0 c
    have : (36 : ℂ) * ((1/6 : ℝ) : ℂ) * ((1/6 : ℝ) : ℂ) = 1 := by
      push_cast
      norm_num
    linear_combination (36 * (W 0 c * conj' (W 0 c))) * e1 + 36 * ((1/6:ℝ):ℂ) * e2 + this
  -- THE TRANSPORT: coefficient lines identify target pair ratios with source pair ratios
  have hk : ∀ a b : Fin 6, a < b → ∀ i,
      hW' i (mu a b).1 * conj' (hW' i (mu a b).2) = h i a * conj' (h i b) := by
    intro a b hab i
    have hc := hC a b hab i 0
    simp only [map_mul, Complex.conj_conj] at hc
    simp only [hdef, hdefW, map_mul, Complex.conj_conj, map_ofNat]
    linear_combination 36 * hc
  -- FOUR TRANSPORTED TRIANGLES, CLEARED
  have T012 : h 1 1 * conj' (h 1 1) = h 1 1 * conj' (h 1 1) := rfl
  clear T012
  have mkT : ∀ i, ∀ p1 q1 p2 q2 p3 q3 : Fin 6, ∀ c d e : Fin 6,
      (hW' i c * conj' (hW' i d) = h i p1 * conj' (h i q1)) →
      (hW' i d * conj' (hW' i e) = h i p2 * conj' (h i q2)) →
      (hW' i c * conj' (hW' i e) = h i p3 * conj' (h i q3)) →
      h i p1 * h i p2 * h i q3 = h i q1 * h i q2 * h i p3 := by
    intro i p1 q1 p2 q2 p3 q3 c d e e1 e2 e3
    apply triangle_clear (h i) (hunit i)
    have chain := pair_chain (hW' i) (hunitW i) c d e
    linear_combination chain + e3 - (hW' i c * conj' (hW' i d)) * e2
      - (h i p2 * conj' (h i q2)) * e1
  have r1 : ∀ i, h i 0 * h i 3 * h i 4 = h i 1 * h i 5 * h i 2 := by
    intro i
    have hmk := mkT i 0 1 3 5 2 4 0 1 2
      (hk 0 1 (by decide) i) (hk 3 5 (by decide) i) (hk 2 4 (by decide) i)
    linear_combination hmk
  have r2 : ∀ i, h i 0 * h i 0 * h i 4 = h i 1 * h i 1 * h i 3 := by
    intro i
    have hmk := mkT i 0 1 0 3 1 4 0 1 3
      (hk 0 1 (by decide) i) (hk 0 3 (by decide) i) (hk 1 4 (by decide) i)
    linear_combination hmk
  have r3 : ∀ i, h i 0 * h i 0 * h i 5 = h i 1 * h i 4 * h i 2 := by
    intro i
    have hmk := mkT i 0 1 0 4 2 5 0 1 4
      (hk 0 1 (by decide) i) (hk 0 4 (by decide) i) (hk 2 5 (by decide) i)
    linear_combination hmk
  have r4 : ∀ i, h i 3 * h i 0 * h i 3 = h i 4 * h i 2 * h i 2 := by
    intro i
    have hmk := mkT i 3 4 0 2 2 3 3 4 5
      (hk 3 4 (by decide) i) (hk 0 2 (by decide) i) (hk 2 3 (by decide) i)
    linear_combination hmk
  -- MONOMIAL FORM per row
  set s : Fin 6 → ℂ := fun i => h i 1 * conj' (h i 0) with hsdef
  set t : Fin 6 → ℂ := fun i => h i 2 * conj' (h i 0) with htdef
  have hsu : ∀ i, s i * conj' (s i) = 1 := by
    intro i
    simp only [hsdef, map_mul, Complex.conj_conj]
    linear_combination (h i 1 * conj' (h i 1)) * hunit i 0 + hunit i 1
  have htu : ∀ i, t i * conj' (t i) = 1 := by
    intro i
    simp only [htdef, map_mul, Complex.conj_conj]
    linear_combination (h i 2 * conj' (h i 2)) * hunit i 0 + hunit i 2
  have hsnz : ∀ i, s i ≠ 0 := fun i => left_ne_zero_of_mul_eq_one (hsu i)
  have htnz : ∀ i, t i ≠ 0 := fun i => left_ne_zero_of_mul_eq_one (htu i)
  have hmono : ∀ i a, h i a = h i 0 * (s i) ^ (u2 a) * (t i) ^ (u3 a) := by
    intro i a
    obtain ⟨m3, m4, m5⟩ := monomial_relations (h i) (hnzh i) (r1 i) (r2 i) (r3 i) (r4 i)
    fin_cases a
    · show h i 0 = h i 0 * s i ^ (u2 0) * t i ^ (u3 0)
      norm_num [u2, u3]
    · show h i 1 = h i 0 * s i ^ (u2 1) * t i ^ (u3 1)
      norm_num [u2, u3, hsdef]
      linear_combination (-(h i 1)) * hunit i 0
    · show h i 2 = h i 0 * s i ^ (u2 2) * t i ^ (u3 2)
      norm_num [u2, u3, htdef]
      linear_combination (-(h i 2)) * hunit i 0
    · show h i 3 = h i 0 * s i ^ (u2 3) * t i ^ (u3 3)
      norm_num [u2, u3, hsdef, htdef]
      linear_combination (h i 0 * conj' (h i 0) ^ 4) * m3
        - (h i 3 * ((h i 0 * conj' (h i 0))^3 + (h i 0 * conj' (h i 0))^2
            + (h i 0 * conj' (h i 0)) + 1)) * hunit i 0
    · show h i 4 = h i 0 * s i ^ (u2 4) * t i ^ (u3 4)
      norm_num [u2, u3, hsdef, htdef]
      linear_combination (h i 0 * conj' (h i 0) ^ 6) * m4
        - (h i 4 * ((h i 0 * conj' (h i 0))^5 + (h i 0 * conj' (h i 0))^4
            + (h i 0 * conj' (h i 0))^3 + (h i 0 * conj' (h i 0))^2
            + (h i 0 * conj' (h i 0)) + 1)) * hunit i 0
    · show h i 5 = h i 0 * s i ^ (u2 5) * t i ^ (u3 5)
      norm_num [u2, u3, hsdef, htdef]
      linear_combination (h i 0 * conj' (h i 0) ^ 8) * m5
        - (h i 5 * ((h i 0 * conj' (h i 0))^7 + (h i 0 * conj' (h i 0))^6
            + (h i 0 * conj' (h i 0))^5 + (h i 0 * conj' (h i 0))^4
            + (h i 0 * conj' (h i 0))^3 + (h i 0 * conj' (h i 0))^2
            + (h i 0 * conj' (h i 0)) + 1)) * hunit i 0
  -- W-SIDE MONOMIAL FORM through the linkage
  have hmono' : ∀ i c, hW' i c = hW' i 0 * (s i) ^ (wp2 c) * (t i) ^ (u3 c) := by
    intro i c
    by_cases hc0 : c = 0
    · rw [hc0]
      show hW' i 0 = hW' i 0 * s i ^ (wp2 0) * t i ^ (u3 0)
      norm_num [wp2, u3]
    · have hlt : (0 : Fin 6) < c := Fin.pos_of_ne_zero hc0
      obtain ⟨hasc, hmm⟩ := mu_muInv 0 c hlt
      have hkc := hk (muInv 0 c).1 (muInv 0 c).2 hasc i
      rw [hmm] at hkc
      -- hkc : hW' i 0 * conj' (hW' i c) = h i p * conj' (h i q)
      have hlink := linkage' (muInv 0 c).1 (muInv 0 c).2 hasc
      rw [hmm] at hlink
      simp only at hlink
      -- exponent bookkeeping over ℕ from the ℤ identities
      have hm2 : u2 (muInv 0 c).1 + wp2 c = wp2 0 + u2 (muInv 0 c).2 := by
        have := hlink.1
        omega
      have hm3 : u3 (muInv 0 c).1 + u3 c = u3 0 + u3 (muInv 0 c).2 := by
        have := hlink.2
        omega
      -- rewrite the transported ratio into the pure conjugate-monomial
      have hratio : hW' i 0 * conj' (hW' i c)
          = conj' ((s i) ^ (wp2 c) * (t i) ^ (u3 c)) := by
        rw [hkc, hmono i (muInv 0 c).1, hmono i (muInv 0 c).2]
        simp only [map_mul, map_pow]
        have hs' := pow_shift (hsu i) hm2
        have ht' := pow_shift (htu i) hm3
        calc h i 0 * s i ^ u2 (muInv 0 c).1 * t i ^ u3 (muInv 0 c).1
              * (conj' (h i 0) * conj' (s i) ^ u2 (muInv 0 c).2
                * conj' (t i) ^ u3 (muInv 0 c).2)
            = (h i 0 * conj' (h i 0))
              * (s i ^ u2 (muInv 0 c).1 * conj' (s i) ^ u2 (muInv 0 c).2)
              * (t i ^ u3 (muInv 0 c).1 * conj' (t i) ^ u3 (muInv 0 c).2) := by ring
          _ = 1 * (s i ^ (wp2 0) * conj' (s i) ^ (wp2 c))
              * (t i ^ (u3 0) * conj' (t i) ^ (u3 c)) := by
                rw [hunit i 0, hs', ht']
          _ = conj' (s i) ^ (wp2 c) * conj' (t i) ^ (u3 c) := by
                norm_num [wp2, u3]
      have hps := potential_step (w := s i ^ wp2 c * t i ^ u3 c) (hunitW i c)
        (unit_monomial (hsu i) (htu i) (wp2 c) (u3 c)) hratio
      rw [hps]
      ring
  -- THE MASK CONDITIONS for every off-diagonal row pair
  have hmaskV : ∀ i j : Fin 6, i ≠ j →
      1 + (s i * conj' (s j)) + (t i * conj' (t j))
        + (s i * conj' (s j))^2*(t i * conj' (t j))^2
        + (s i * conj' (s j))^4*(t i * conj' (t j))^2
        + (s i * conj' (s j))^5*(t i * conj' (t j))^3 = 0 := by
    intro i j hij
    have horth : (∑ a, V i a * conj' (V j a)) = 0 := by
      rw [hVrow i j, if_neg hij]
    have hstep : ∀ a : Fin 6, h i a * conj' (h j a) = 6 * (V i a * conj' (V j a)) := by
      intro a
      simp only [hdef, map_mul, Complex.conj_conj, map_ofNat]
      have e2 := hVc 0 a
      have h36 : (36 : ℂ) * ((1/6 : ℝ) : ℂ) = 6 := by push_cast; norm_num
      linear_combination (36 * (V i a * conj' (V j a))) * e2
        + (V i a * conj' (V j a)) * h36
    have hsum0 : (∑ a, h i a * conj' (h j a)) = 0 := by
      calc (∑ a, h i a * conj' (h j a)) = ∑ a, 6 * (V i a * conj' (V j a)) := by
            exact Finset.sum_congr rfl (fun a _ => hstep a)
        _ = 6 * ∑ a, V i a * conj' (V j a) := by rw [Finset.mul_sum]
        _ = 0 := by rw [horth, mul_zero]
    have hterm : ∀ a : Fin 6, h i a * conj' (h j a)
        = (h i 0 * conj' (h j 0))
          * ((s i * conj' (s j)) ^ (u2 a) * (t i * conj' (t j)) ^ (u3 a)) := by
      intro a
      rw [hmono i a, hmono j a]
      simp only [map_mul, map_pow]
      rw [mul_pow, mul_pow]
      ring
    have hfact : (h i 0 * conj' (h j 0))
        * (∑ a, (s i * conj' (s j)) ^ (u2 a) * (t i * conj' (t j)) ^ (u3 a)) = 0 := by
      rw [Finset.mul_sum, ← hsum0]
      exact Finset.sum_congr rfl (fun a _ => (hterm a).symm)
    have hpre : h i 0 * conj' (h j 0) ≠ 0 :=
      mul_ne_zero (hnzh i 0) (by simpa using hnzh j 0)
    have hzero := (mul_eq_zero.mp hfact).resolve_left hpre
    rw [maskV_eq_sum] at hzero
    linear_combination hzero
  have hmaskW : ∀ i j : Fin 6, i ≠ j →
      1 + (s i * conj' (s j)) + (s i * conj' (s j))^4*(t i * conj' (t j))
        + (s i * conj' (s j))^3*(t i * conj' (t j))^2
        + (s i * conj' (s j))^5*(t i * conj' (t j))^2
        + (s i * conj' (s j))^5*(t i * conj' (t j))^3 = 0 := by
    intro i j hij
    have horth : (∑ c, W i c * conj' (W j c)) = 0 := by
      rw [hWrow i j, if_neg hij]
    have hstep : ∀ c : Fin 6, hW' i c * conj' (hW' j c) = 6 * (W i c * conj' (W j c)) := by
      intro c
      simp only [hdefW, map_mul, Complex.conj_conj, map_ofNat]
      have e2 := hWc 0 c
      have h36 : (36 : ℂ) * ((1/6 : ℝ) : ℂ) = 6 := by push_cast; norm_num
      linear_combination (36 * (W i c * conj' (W j c))) * e2
        + (W i c * conj' (W j c)) * h36
    have hsum0 : (∑ c, hW' i c * conj' (hW' j c)) = 0 := by
      calc (∑ c, hW' i c * conj' (hW' j c)) = ∑ c, 6 * (W i c * conj' (W j c)) := by
            exact Finset.sum_congr rfl (fun c _ => hstep c)
        _ = 6 * ∑ c, W i c * conj' (W j c) := by rw [Finset.mul_sum]
        _ = 0 := by rw [horth, mul_zero]
    have hterm : ∀ c : Fin 6, hW' i c * conj' (hW' j c)
        = (hW' i 0 * conj' (hW' j 0))
          * ((s i * conj' (s j)) ^ (wp2 c) * (t i * conj' (t j)) ^ (u3 c)) := by
      intro c
      rw [hmono' i c, hmono' j c]
      simp only [map_mul, map_pow]
      rw [mul_pow, mul_pow]
      ring
    have hfact : (hW' i 0 * conj' (hW' j 0))
        * (∑ c, (s i * conj' (s j)) ^ (wp2 c) * (t i * conj' (t j)) ^ (u3 c)) = 0 := by
      rw [Finset.mul_sum, ← hsum0]
      exact Finset.sum_congr rfl (fun c _ => (hterm c).symm)
    have hpre : hW' i 0 * conj' (hW' j 0) ≠ 0 :=
      mul_ne_zero (hnzW i 0) (by simpa using hnzW j 0)
    have hzero := (mul_eq_zero.mp hfact).resolve_left hpre
    rw [maskW_eq_sum] at hzero
    linear_combination hzero
  -- EVERY PAIRWISE RATIO IS ONE OF THE EIGHT POINTS, IN EXPONENT FORM
  have hpq : ∀ i j : Fin 6, i ≠ j → ∃ pq : ZMod 12 × ZMod 4, pq ∈ conn
      ∧ s i * conj' (s j) = zeta ^ (pq.1.val) ∧ t i * conj' (t j) = I ^ (pq.2.val) := by
    intro i j hij
    have hxu : (s i * conj' (s j)) * conj' (s i * conj' (s j)) = 1 := by
      simp only [map_mul, Complex.conj_conj]
      linear_combination (s i * conj' (s i)) * hsu j + hsu i
    have hyu : (t i * conj' (t j)) * conj' (t i * conj' (t j)) = 1 := by
      simp only [map_mul, Complex.conj_conj]
      linear_combination (t i * conj' (t i)) * htu j + htu i
    have hd := torus_zeros (s i * conj' (s j)) (t i * conj' (t j)) hxu hyu
      (by linear_combination hmaskV i j hij) (by linear_combination hmaskW i j hij)
    exact point_to_exponent hd
  choose F hFmem hFs hFt using hpq
  -- EXPONENT MAPS AND THE CLIQUE CONTRADICTION
  have hA : ∃ A : Fin 6 → ZMod 12, ∃ B : Fin 6 → ZMod 4,
      (∀ i, s i * conj' (s 0) = zeta ^ (A i).val)
      ∧ (∀ i, t i * conj' (t 0) = I ^ (B i).val)
      ∧ A 0 = 0 ∧ B 0 = 0 := by
    refine ⟨fun i => if hi : i = 0 then 0 else (F i 0 hi).1,
      fun i => if hi : i = 0 then 0 else (F i 0 hi).2, ?_, ?_,
      dif_pos rfl, dif_pos rfl⟩
    · intro i
      by_cases hi : i = 0
      · rw [hi]
        dsimp only
        rw [dif_pos rfl, show ((0 : ZMod 12)).val = 0 from rfl, pow_zero]
        exact hsu 0
      · dsimp only
        rw [dif_neg hi]
        exact hFs i 0 hi
    · intro i
      by_cases hi : i = 0
      · rw [hi]
        dsimp only
        rw [dif_pos rfl, show ((0 : ZMod 4)).val = 0 from rfl, pow_zero]
        exact htu 0
      · dsimp only
        rw [dif_neg hi]
        exact hFt i 0 hi
  obtain ⟨A, B, hAs, hBs, hA0, hB0⟩ := hA
  have hconsist : ∀ i j : Fin 6, ∀ (hij : i ≠ j),
      A i - A j = (F i j hij).1 ∧ B i - B j = (F i j hij).2 := by
    intro i j hij
    constructor
    · -- ζ^{A i} = ζ^{c + A j}
      have hchain : zeta ^ (A i).val = zeta ^ ((F i j hij).1.val + (A j).val) := by
        rw [pow_add]
        rw [← hAs i, ← hFs i j hij]
        -- (s i conj s 0) = (s i conj s j)(s j conj s 0) after multiplying: use units of s j? 
        have hexp : s i * conj' (s 0)
            = (s i * conj' (s j)) * (s j * conj' (s 0)) := by
          have := hsu j
          linear_combination (s i * conj' (s 0)) * (Eq.symm this)
        rw [hexp, hAs j]
      have hcast := pow_eq_pow_zmod zeta_ne_zero orderOf_zeta hchain
      have hAi : ((A i).val : ZMod 12) = A i := ZMod.natCast_rightInverse (A i)
      have hAj : ((A j).val : ZMod 12) = A j := ZMod.natCast_rightInverse (A j)
      have hFc : (((F i j hij).1.val : ℕ) : ZMod 12) = (F i j hij).1 :=
        ZMod.natCast_rightInverse _
      rw [Nat.cast_add, hAi, hAj, hFc] at hcast
      linear_combination hcast
    · have hchain : (I:ℂ) ^ (B i).val = I ^ ((F i j hij).2.val + (B j).val) := by
        rw [pow_add]
        rw [← hBs i, ← hFt i j hij]
        have hexp : t i * conj' (t 0)
            = (t i * conj' (t j)) * (t j * conj' (t 0)) := by
          have := htu j
          linear_combination (t i * conj' (t 0)) * (Eq.symm this)
        rw [hexp, hBs j]
      have hcast := pow_eq_pow_zmod Complex.I_ne_zero orderOf_I hchain
      have hBi : ((B i).val : ZMod 4) = B i := ZMod.natCast_rightInverse (B i)
      have hBj : ((B j).val : ZMod 4) = B j := ZMod.natCast_rightInverse (B j)
      have hFc : (((F i j hij).2.val : ℕ) : ZMod 4) = (F i j hij).2 :=
        ZMod.natCast_rightInverse _
      rw [Nat.cast_add, hBi, hBj, hFc] at hcast
      linear_combination hcast
  -- the clique obstruction fires
  apply no_six_orthogonal
  refine ⟨fun i => (A i, B i), ?_⟩
  intro i j hij
  have hc := hconsist i j hij
  have : ((A i, B i) : ZMod 12 × ZMod 4) - (A j, B j) = (F i j hij) := by
    rw [Prod.mk_sub_mk, hc.1, hc.2]
  rw [this]
  exact hFmem i j hij

end Assembly

#print axioms line_forcing
#print axioms flat_of_products
#print axioms monomial_relations
#print axioms torus_zeros
#print axioms point_to_exponent
#print axioms orderOf_zeta
#print axioms orderOf_I
#print axioms homometricSix_unrealizable

end HomometricSix
end OIBridge
