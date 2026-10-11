/-
  OIBridge/EqvPowerCone.lean — design module of the research thread `research/equivalence` (node E18).
  Not adopted, not certified, not a round: the self-duality of the state cone of the token Ω⋆
  (R-E13.1, NOTES-E13 §1), in polynomial form.

  In the coordinates `u = T + S`, `v = T − S` the cone is the power cone `u^{1/3} v^{2/3} ≥ ‖X‖`, here
  `PC = {(u, v, X) : 0 ≤ u, 0 ≤ v, (Σ X_i²)³ ≤ u² v⁴}` (no real powers, no square roots), and the form
  `TT' + SS' − (TS' + ST')/3 + X·X'` is `B = uu'/3 + 2vv'/3 + X·X'` (`form_eq`).

  §A  Self-positivity (`B_nonneg`): weighted AM–GM as the identity `(a + 2b)³ − 27ab² = (a − b)²(a + 8b)`,
      Cauchy–Schwarz in Lagrange form, and cube monotonicity on `[0, ∞)`.
  §B  The converse (`mem_PC_of_dual`): the poles give `u', v' ≥ 0`; outside `PC` an explicit point of `PC`
      pairs negatively — `(v's, u's, −X')` with `s = θS'/(u'v')`, `θ = (5 + ρ)/6`, `ρ = u'²v'⁴/S'³` when
      `u', v' > 0` (Bernoulli), and simpler points when `u' = 0` or `v' = 0`.
  §C  `PC` equals its dual for `B` (`PC_selfDual`).

  Nothing here has OI content: the statements are about an explicit cone and form.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.LinearCombination

namespace OIBridge
namespace EqvPowerCone

noncomputable section

/-- The squared Euclidean norm of a vector of `ℝ³`. -/
def sq3 (X : Fin 3 → ℝ) : ℝ := X 0 ^ 2 + X 1 ^ 2 + X 2 ^ 2

/-- The Euclidean pairing of `ℝ³`. -/
def dot3 (X Y : Fin 3 → ℝ) : ℝ := X 0 * Y 0 + X 1 * Y 1 + X 2 * Y 2

/-- The power cone, in polynomial form. -/
def PC : Set (ℝ × ℝ × (Fin 3 → ℝ)) :=
  {z | 0 ≤ z.1 ∧ 0 ≤ z.2.1 ∧ sq3 z.2.2 ^ 3 ≤ z.1 ^ 2 * z.2.1 ^ 4}

/-- The self-dualizing form in the coordinates `(u, v, X)`. -/
def B (z w : ℝ × ℝ × (Fin 3 → ℝ)) : ℝ := z.1 * w.1 / 3 + 2 * z.2.1 * w.2.1 / 3 + dot3 z.2.2 w.2.2

/-- The form of NOTES-E13 in the coordinates `(T, S, X)` is `B` in `(u, v, X) = (T + S, T − S, X)`. -/
theorem form_eq (T Sg T' Sg' : ℝ) (X X' : Fin 3 → ℝ) :
    T * T' + Sg * Sg' - (T * Sg' + Sg * T') / 3 + dot3 X X' =
      B (T + Sg, T - Sg, X) (T' + Sg', T' - Sg', X') := by
  simp only [B]
  ring

theorem sq3_nonneg (X : Fin 3 → ℝ) : 0 ≤ sq3 X := by
  simp only [sq3]
  positivity

/-- Cauchy–Schwarz on `ℝ³`, in Lagrange form. -/
theorem dot3_sq_le (X Y : Fin 3 → ℝ) : dot3 X Y ^ 2 ≤ sq3 X * sq3 Y := by
  simp only [dot3, sq3]
  nlinarith [sq_nonneg (X 0 * Y 1 - X 1 * Y 0), sq_nonneg (X 0 * Y 2 - X 2 * Y 0),
    sq_nonneg (X 1 * Y 2 - X 2 * Y 1)]

theorem dot3_neg_self (X : Fin 3 → ℝ) : dot3 (fun i => -X i) X = -sq3 X := by
  simp only [dot3, sq3]
  ring

theorem sq3_neg (X : Fin 3 → ℝ) : sq3 (fun i => -X i) = sq3 X := by
  simp only [sq3]
  ring

/-- Cubes are monotone on `[0, ∞)`. -/
theorem cube_le_cube {x y : ℝ} (hx : 0 ≤ x) (h : x ≤ y) : x ^ 3 ≤ y ^ 3 := by
  have hy : 0 ≤ y := hx.trans h
  nlinarith [mul_nonneg (sub_nonneg.mpr h)
    (add_nonneg (add_nonneg (sq_nonneg x) (mul_nonneg hx hy)) (sq_nonneg y))]

/-- Cubes reflect the order on `[0, ∞)`. -/
theorem le_of_cube_le {x y : ℝ} (hy : 0 ≤ y) (h : x ^ 3 ≤ y ^ 3) : x ≤ y := by
  by_contra hxy
  push_neg at hxy
  have hx : 0 < x := lt_of_le_of_lt hy hxy
  have hpos : 0 < x ^ 2 + x * y + y ^ 2 := by
    nlinarith [mul_pos hx hx, mul_nonneg hx.le hy, sq_nonneg y]
  nlinarith [mul_pos (sub_pos.mpr hxy) hpos]

/-! ### §A — self-positivity -/

/-- Weighted AM–GM, `a b² ≤ ((a + 2b)/3)³` for `a, b ≥ 0`, through
`(a + 2b)³ − 27ab² = (a − b)²(a + 8b)`. -/
theorem amgm (a b : ℝ) (ha : 0 ≤ a) (hb : 0 ≤ b) : a * b ^ 2 ≤ ((a + 2 * b) / 3) ^ 3 := by
  have h8 : 0 ≤ a + 8 * b := by linarith
  nlinarith [mul_nonneg (sq_nonneg (a - b)) h8]

/-- **Self-positivity**: the form is nonnegative on pairs of points of the power cone. -/
theorem B_nonneg {z w : ℝ × ℝ × (Fin 3 → ℝ)} (hz : z ∈ PC) (hw : w ∈ PC) : 0 ≤ B z w := by
  obtain ⟨u, v, X⟩ := z
  obtain ⟨u', v', X'⟩ := w
  obtain ⟨hu, hv, hX⟩ := hz
  obtain ⟨hu', hv', hX'⟩ := hw
  have hu0 : 0 ≤ u := hu
  have hv0 : 0 ≤ v := hv
  have hu'0 : 0 ≤ u' := hu'
  have hv'0 : 0 ≤ v' := hv'
  have hXc : sq3 X ^ 3 ≤ u ^ 2 * v ^ 4 := hX
  have hX'c : sq3 X' ^ 3 ≤ u' ^ 2 * v' ^ 4 := hX'
  have ha : 0 ≤ u * u' := mul_nonneg hu0 hu'0
  have hb : 0 ≤ v * v' := mul_nonneg hv0 hv'0
  have hm : 0 ≤ (u * u' + 2 * (v * v')) / 3 := by linarith
  have hS := sq3_nonneg X
  have hS' := sq3_nonneg X'
  -- the product of the two cube conditions
  have hprod : (sq3 X * sq3 X') ^ 3 ≤ (u * u' * (v * v') ^ 2) ^ 2 := by
    have h1 : (sq3 X * sq3 X') ^ 3 = sq3 X ^ 3 * sq3 X' ^ 3 := by ring
    have h2 : (u * u' * (v * v') ^ 2) ^ 2 = (u ^ 2 * v ^ 4) * (u' ^ 2 * v' ^ 4) := by ring
    rw [h1, h2]
    exact mul_le_mul hXc hX'c (pow_nonneg hS' 3) (le_trans (pow_nonneg hS 3) hXc)
  -- weighted AM–GM, squared
  have hAM := amgm (u * u') (v * v') ha hb
  have hX0 : 0 ≤ u * u' * (v * v') ^ 2 := mul_nonneg ha (sq_nonneg _)
  have hAM2 : (u * u' * (v * v') ^ 2) ^ 2 ≤ (((u * u' + 2 * (v * v')) / 3) ^ 3) ^ 2 := by
    nlinarith [mul_nonneg (sub_nonneg.mpr hAM) (add_nonneg hX0 (hX0.trans hAM))]
  -- Cauchy–Schwarz, cubed
  have hCS := dot3_sq_le X X'
  have hCS3 : (dot3 X X' ^ 2) ^ 3 ≤ (sq3 X * sq3 X') ^ 3 := cube_le_cube (sq_nonneg _) hCS
  -- so the square of the pairing of `X` with `X'` is at most `m²`
  have hD : dot3 X X' ^ 2 ≤ ((u * u' + 2 * (v * v')) / 3) ^ 2 := by
    apply le_of_cube_le (sq_nonneg _)
    calc (dot3 X X' ^ 2) ^ 3 ≤ (sq3 X * sq3 X') ^ 3 := hCS3
      _ ≤ (u * u' * (v * v') ^ 2) ^ 2 := hprod
      _ ≤ (((u * u' + 2 * (v * v')) / 3) ^ 3) ^ 2 := hAM2
      _ = (((u * u' + 2 * (v * v')) / 3) ^ 2) ^ 3 := by ring
  have hBe : B (u, v, X) (u', v', X') = (u * u' + 2 * (v * v')) / 3 + dot3 X X' := by
    simp only [B]
    ring
  rw [hBe]
  nlinarith [hD, hm]

/-! ### §B — the converse -/

theorem pole_u_mem : ((1 : ℝ), (0 : ℝ), (0 : Fin 3 → ℝ)) ∈ PC := by
  show (0 : ℝ) ≤ 1 ∧ (0 : ℝ) ≤ 0 ∧ sq3 (0 : Fin 3 → ℝ) ^ 3 ≤ (1 : ℝ) ^ 2 * (0 : ℝ) ^ 4
  exact ⟨zero_le_one, le_refl 0, by simp [sq3]⟩

theorem pole_v_mem : ((0 : ℝ), (1 : ℝ), (0 : Fin 3 → ℝ)) ∈ PC := by
  show (0 : ℝ) ≤ 0 ∧ (0 : ℝ) ≤ 1 ∧ sq3 (0 : Fin 3 → ℝ) ^ 3 ≤ (0 : ℝ) ^ 2 * (1 : ℝ) ^ 4
  exact ⟨le_refl 0, zero_le_one, by simp [sq3]⟩

/-- Bernoulli at exponent six, `ρ ≤ ((5 + ρ)/6)⁶` for `0 ≤ ρ`, through
`θ⁶ − (6θ − 5) = (θ − 1)²(θ⁴ + 2θ³ + 3θ² + 4θ + 5)`. -/
theorem bernoulli6 (ρ : ℝ) (h0 : 0 ≤ ρ) : ρ ≤ ((5 + ρ) / 6) ^ 6 := by
  obtain ⟨θ, hθ⟩ : ∃ θ : ℝ, θ = (5 + ρ) / 6 := ⟨_, rfl⟩
  rw [← hθ]
  have hθ0 : 0 ≤ θ := by rw [hθ]; linarith
  have hρ : ρ = 6 * θ - 5 := by rw [hθ]; ring
  have hq : 0 ≤ θ ^ 4 + 2 * θ ^ 3 + 3 * θ ^ 2 + 4 * θ + 5 := by
    nlinarith [pow_nonneg hθ0 2, pow_nonneg hθ0 3, pow_nonneg hθ0 4]
  have hfac : θ ^ 6 - (6 * θ - 5) = (θ - 1) ^ 2 * (θ ^ 4 + 2 * θ ^ 3 + 3 * θ ^ 2 + 4 * θ + 5) := by
    ring
  nlinarith [mul_nonneg (sq_nonneg (θ - 1)) hq, hfac, hρ]

/-- **The converse**: a point pairing nonnegatively with the whole power cone lies in it. -/
theorem mem_PC_of_dual {w : ℝ × ℝ × (Fin 3 → ℝ)} (hw : ∀ z ∈ PC, 0 ≤ B z w) : w ∈ PC := by
  obtain ⟨u', v', X'⟩ := w
  have hu' : 0 ≤ u' := by
    have h := hw _ pole_u_mem
    simp [B, dot3] at h
    linarith
  have hv' : 0 ≤ v' := by
    have h := hw _ pole_v_mem
    simp [B, dot3] at h
    linarith
  show 0 ≤ u' ∧ 0 ≤ v' ∧ sq3 X' ^ 3 ≤ u' ^ 2 * v' ^ 4
  refine ⟨hu', hv', ?_⟩
  by_contra hcon
  push_neg at hcon
  have hS0 := sq3_nonneg X'
  have hS : 0 < sq3 X' := by
    rcases eq_or_lt_of_le hS0 with h | h
    · rw [← h] at hcon
      nlinarith [mul_nonneg (pow_nonneg hu' 2) (pow_nonneg hv' 4)]
    · exact h
  have hSne : sq3 X' ≠ 0 := ne_of_gt hS
  rcases eq_or_lt_of_le hu' with hu0 | hupos
  · -- `u' = 0`: the point `((v' + 1)² (S' + 1)/S', S'/(v' + 1), −X')`
    have hv1 : 0 < v' + 1 := by linarith
    have hv1ne : v' + 1 ≠ 0 := ne_of_gt hv1
    have hzmem : (((v' + 1) ^ 2 * (sq3 X' + 1) / sq3 X'), (sq3 X' / (v' + 1)),
        (fun i => -X' i)) ∈ PC := by
      show 0 ≤ (v' + 1) ^ 2 * (sq3 X' + 1) / sq3 X' ∧ 0 ≤ sq3 X' / (v' + 1) ∧
        sq3 (fun i => -X' i) ^ 3 ≤ ((v' + 1) ^ 2 * (sq3 X' + 1) / sq3 X') ^ 2 * (sq3 X' / (v' + 1)) ^ 4
      refine ⟨div_nonneg (mul_nonneg (sq_nonneg _) (by linarith)) hS0, div_nonneg hS0 hv1.le, ?_⟩
      rw [sq3_neg]
      have hid : ((v' + 1) ^ 2 * (sq3 X' + 1) / sq3 X') ^ 2 * (sq3 X' / (v' + 1)) ^ 4 =
          (sq3 X' + 1) ^ 2 * sq3 X' ^ 2 := by
        first
          | (field_simp; done)
          | (field_simp; ring)
      rw [hid]
      have hq : 0 ≤ sq3 X' ^ 2 + sq3 X' + 1 := by nlinarith
      nlinarith [mul_nonneg (sq_nonneg (sq3 X')) hq]
    have hBz := hw _ hzmem
    have hval : B (((v' + 1) ^ 2 * (sq3 X' + 1) / sq3 X'), (sq3 X' / (v' + 1)), (fun i => -X' i))
        (u', v', X') * (3 * (v' + 1)) = -(sq3 X' * (v' + 3)) := by
      simp only [B, dot3_neg_self, ← hu0]
      first
        | (field_simp; ring)
        | (field_simp; done)
    nlinarith [mul_nonneg hBz (show (0 : ℝ) ≤ 3 * (v' + 1) by linarith),
      mul_pos hS (show (0 : ℝ) < v' + 3 by linarith)]
  rcases eq_or_lt_of_le hv' with hv0 | hvpos
  · -- `v' = 0`, `u' > 0`: the point `(S'/(u' + 1), S' + (u' + 1)² + 1, −X')`
    have hu1 : 0 < u' + 1 := by linarith
    have hu1ne : u' + 1 ≠ 0 := ne_of_gt hu1
    obtain ⟨b, hbdef⟩ : ∃ b : ℝ, b = sq3 X' + (u' + 1) ^ 2 + 1 := ⟨_, rfl⟩
    have hb1 : 1 ≤ b := by rw [hbdef]; nlinarith [sq_nonneg (u' + 1)]
    have hbS : sq3 X' ≤ b := by rw [hbdef]; nlinarith [sq_nonneg (u' + 1)]
    have hbU : (u' + 1) ^ 2 ≤ b := by rw [hbdef]; linarith
    have hzmem : ((sq3 X' / (u' + 1)), b, (fun i => -X' i)) ∈ PC := by
      show 0 ≤ sq3 X' / (u' + 1) ∧ 0 ≤ b ∧
        sq3 (fun i => -X' i) ^ 3 ≤ (sq3 X' / (u' + 1)) ^ 2 * b ^ 4
      refine ⟨div_nonneg hS0 hu1.le, by linarith, ?_⟩
      rw [sq3_neg]
      have hid : (sq3 X' / (u' + 1)) ^ 2 * b ^ 4 * (u' + 1) ^ 2 = sq3 X' ^ 2 * b ^ 4 := by
        first
          | (field_simp; done)
          | (field_simp; ring)
      have hb2 : sq3 X' * (u' + 1) ^ 2 ≤ b ^ 2 := by
        have h := mul_le_mul hbS hbU (sq_nonneg _) (by linarith)
        nlinarith [h]
      have hbsq : 1 ≤ b ^ 2 := by
        nlinarith [mul_nonneg (sub_nonneg.mpr hb1) (show (0 : ℝ) ≤ b + 1 by linarith)]
      have hb4 : b ^ 2 ≤ b ^ 4 := by
        nlinarith [mul_nonneg (sq_nonneg b) (sub_nonneg.mpr hbsq)]
      have hkey : sq3 X' ^ 3 * (u' + 1) ^ 2 ≤ sq3 X' ^ 2 * b ^ 4 := by
        have h1 : sq3 X' ^ 3 * (u' + 1) ^ 2 = sq3 X' ^ 2 * (sq3 X' * (u' + 1) ^ 2) := by ring
        rw [h1]
        exact mul_le_mul_of_nonneg_left (hb2.trans hb4) (sq_nonneg _)
      rw [← hid] at hkey
      exact le_of_mul_le_mul_right hkey (pow_pos hu1 2)
    have hBz := hw _ hzmem
    have hval : B ((sq3 X' / (u' + 1)), b, (fun i => -X' i)) (u', v', X') * (3 * (u' + 1)) =
        -(sq3 X' * (2 * u' + 3)) := by
      simp only [B, dot3_neg_self, ← hv0]
      first
        | (field_simp; ring)
        | (field_simp; done)
    nlinarith [mul_nonneg hBz (show (0 : ℝ) ≤ 3 * (u' + 1) by linarith),
      mul_pos hS (show (0 : ℝ) < 2 * u' + 3 by linarith)]
  · -- `u', v' > 0`: the point `(v' s, u' s, −X')`, `s = θ S'/(u' v')`
    have hu'ne : u' ≠ 0 := ne_of_gt hupos
    have hv'ne : v' ≠ 0 := ne_of_gt hvpos
    have huv : 0 < u' * v' := mul_pos hupos hvpos
    obtain ⟨ρ, hρdef⟩ : ∃ ρ : ℝ, ρ = u' ^ 2 * v' ^ 4 / sq3 X' ^ 3 := ⟨_, rfl⟩
    have hρ0 : 0 ≤ ρ := by
      rw [hρdef]
      exact div_nonneg (by positivity) (pow_nonneg hS0 3)
    have hρS : ρ * sq3 X' ^ 3 = u' ^ 2 * v' ^ 4 := by
      rw [hρdef]
      first
        | (field_simp; done)
        | (field_simp; ring)
    have hρ1 : ρ < 1 := by
      by_contra hge
      push_neg at hge
      nlinarith [mul_le_mul_of_nonneg_right hge (pow_nonneg hS0 3)]
    obtain ⟨θ, hθdef⟩ : ∃ θ : ℝ, θ = (5 + ρ) / 6 := ⟨_, rfl⟩
    have hθ0 : 0 < θ := by rw [hθdef]; linarith
    have hθ1 : θ < 1 := by rw [hθdef]; linarith
    have hbern : ρ ≤ θ ^ 6 := by rw [hθdef]; exact bernoulli6 ρ hρ0
    obtain ⟨s, hsdef⟩ : ∃ s : ℝ, s = θ * sq3 X' / (u' * v') := ⟨_, rfl⟩
    have hs0 : 0 ≤ s := by
      rw [hsdef]
      exact div_nonneg (mul_nonneg hθ0.le hS0) huv.le
    have hus : u' * v' * s = θ * sq3 X' := by
      rw [hsdef]
      first
        | (field_simp; done)
        | (field_simp; ring)
    have hzmem : ((v' * s), (u' * s), (fun i => -X' i)) ∈ PC := by
      show 0 ≤ v' * s ∧ 0 ≤ u' * s ∧ sq3 (fun i => -X' i) ^ 3 ≤ (v' * s) ^ 2 * (u' * s) ^ 4
      refine ⟨mul_nonneg hv' hs0, mul_nonneg hu' hs0, ?_⟩
      rw [sq3_neg]
      have hid : (v' * s) ^ 2 * (u' * s) ^ 4 * (u' ^ 2 * v' ^ 4) = (θ * sq3 X') ^ 6 := by
        rw [← hus]
        ring
      have hkey : sq3 X' ^ 3 * (u' ^ 2 * v' ^ 4) ≤ (θ * sq3 X') ^ 6 := by
        have h1 : (θ * sq3 X') ^ 6 = sq3 X' ^ 3 * (θ ^ 6 * sq3 X' ^ 3) := by ring
        rw [h1]
        refine mul_le_mul_of_nonneg_left ?_ (pow_nonneg hS0 3)
        rw [← hρS]
        exact mul_le_mul_of_nonneg_right hbern (pow_nonneg hS0 3)
      rw [← hid] at hkey
      exact le_of_mul_le_mul_right hkey (mul_pos (pow_pos hupos 2) (pow_pos hvpos 4))
    have hBz := hw _ hzmem
    have hval : B ((v' * s), (u' * s), (fun i => -X' i)) (u', v', X') = (θ - 1) * sq3 X' := by
      simp only [B, dot3_neg_self]
      linear_combination hus
    rw [hval] at hBz
    nlinarith [mul_pos (sub_pos.mpr hθ1) hS]

/-! ### §C — self-duality -/

/-- **The power cone equals its dual for `B`.** -/
theorem PC_selfDual : PC = {w | ∀ z ∈ PC, 0 ≤ B z w} := by
  ext w
  simp only [Set.mem_setOf_eq]
  exact ⟨fun hw z hz => B_nonneg hz hw, mem_PC_of_dual⟩

end

end EqvPowerCone
end OIBridge

#print axioms OIBridge.EqvPowerCone.form_eq
#print axioms OIBridge.EqvPowerCone.dot3_sq_le
#print axioms OIBridge.EqvPowerCone.amgm
#print axioms OIBridge.EqvPowerCone.B_nonneg
#print axioms OIBridge.EqvPowerCone.bernoulli6
#print axioms OIBridge.EqvPowerCone.mem_PC_of_dual
#print axioms OIBridge.EqvPowerCone.PC_selfDual
