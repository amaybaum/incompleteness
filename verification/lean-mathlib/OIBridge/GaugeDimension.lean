/-
  OIBridge/GaugeDimension.lean — [SM] Theorem 16 (the Yang–Mills coupling dimension).

      [g] = (3 − d)/2,     dimensionless  ⟺  d = 3.

  NOT FORMALIZED BY DEFINING [g] := (3 − d)/2 — that would kernel-check the notation and nothing
  else. The physical input is stated as the hypothesis instead: the action `S = (1/4g²)∫d^{d+1}x F²`
  is dimensionless, so in mass dimensions

      −2[g] + 2[F] − (d + 1) = 0,

  and with `[F] = 2` the theorem follows. What the kernel certifies is the passage from that
  balance to the printed formula and the printed iff, with the balance itself visible in the
  statement — the measure's `d + 1` and the field strength's `2` are there to be read, and each
  gets a countercontrol: `[F]` left general gives `[g] = [F] − (d+1)/2`, and mistaking the measure
  for `d` dimensions gives `(4 − d)/2`, which agrees with the right answer at NO dimension.

  Dimensions live in `ℚ` and `d` in `ℕ`; everything is exact arithmetic.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import Mathlib.Data.Rat.Defs
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Data.Nat.Cast.Order.Ring

namespace OIBridge

namespace GaugeDimension

set_option autoImplicit false

/-- **The dimension balance** of `S = (1/4g²) ∫ d^{d+1}x F²`: the action is dimensionless, the
measure contributes `−(d+1)`, the field strength enters squared, the coupling inversely squared.
This is the physical content; everything below is arithmetic from it. -/
def Balance (d : ℕ) (g F : ℚ) : Prop := -2 * g + 2 * F - (d + 1) = 0

/-- **The general formula**: with `[F]` left arbitrary, `[g] = [F] − (d+1)/2`. The specialization
below is `[F] = 2` and nothing else. -/
theorem coupling_dim_general {d : ℕ} {g F : ℚ} (h : Balance d g F) :
    g = F - (d + 1) / 2 := by
  rw [Balance] at h
  linarith

/-- **[SM] THEOREM 16.** From the balance with `[F] = 2`: the coupling has mass dimension
`(3 − d)/2`, and it is dimensionless exactly in `d = 3`. -/
theorem theorem_16 {d : ℕ} {g : ℚ} (h : Balance d g 2) :
    g = (3 - d) / 2 ∧ (g = 0 ↔ d = 3) := by
  have hg : g = (3 - (d : ℚ)) / 2 := by
    have := coupling_dim_general h
    linarith
  refine ⟨hg, ?_⟩
  rw [hg]
  constructor
  · intro h0
    have hd : (d : ℚ) = 3 := by linarith [h0]
    exact_mod_cast hd
  · intro hd
    subst hd
    norm_num

/-- **COUNTERCONTROL: the off-by-one.** Balancing against a `d`-dimensional measure instead of the
`(d+1)`-dimensional one gives `(4 − d)/2`. -/
theorem off_by_one {d : ℕ} {g : ℚ} (h : -2 * g + 2 * 2 - d = 0) :
    g = (4 - d) / 2 := by
  linarith

/-- **And the off-by-one is never right**: `(4 − d)/2` and `(3 − d)/2` agree at no dimension, so
the measure's `d + 1` is load-bearing in the balance, not decoration. -/
theorem off_by_one_never_agrees (d : ℕ) : (4 - (d : ℚ)) / 2 ≠ (3 - (d : ℚ)) / 2 := by
  intro hc
  have : (4 : ℚ) = 3 := by linarith
  norm_num at this

/-- The `d = 3` instance, concretely: the balance forces `g = 0`. -/
theorem dimensionless_at_three {g : ℚ} (h : Balance 3 g 2) : g = 0 := by
  have := (theorem_16 h).1
  rw [this]
  norm_num

/-- And one step off, concretely: at `d = 4` the coupling has dimension `−1/2`, not zero. -/
theorem not_dimensionless_at_four {g : ℚ} (h : Balance 4 g 2) : g = -(1 / 2) ∧ g ≠ 0 := by
  have hg := (theorem_16 h).1
  constructor
  · rw [hg]; norm_num
  · rw [hg]; norm_num

/-! ### What these proofs rest on -/

#print axioms coupling_dim_general
#print axioms theorem_16
#print axioms off_by_one
#print axioms off_by_one_never_agrees
#print axioms dimensionless_at_three
#print axioms not_dimensionless_at_four

end GaugeDimension

end OIBridge
