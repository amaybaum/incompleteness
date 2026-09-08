import OIBridge.RecurrenceHorizon
import OIBridge.RootedClassification

/-!
# Symmetric binary rooted families and tightness uniform in the horizon

The abstract half of target S1 of `RECURRENCE-SCALING-AUDIT.md`: everything here is a statement
about a family of matrices, quantified over the horizon `N`, and none of it is a check at
particular values of `N`.

A symmetric binary channel `B p` has rows `(p, 1-p)` and `(1-p, p)`. Two facts drive the round.
Composition stays inside the family, `B p * B q = B (2pq - p - q + 1)`, and the rooted-row
total-variation distance is exactly `|2p - 1|`. Together they make a strictly decreasing `p` on
`[0, N-1]` with `p N = 1` P-divisible on every horizon below `N` and P-indivisible at `N`: the
explicit factor `(pt + ps - 1) / (2 ps - 1)` is stochastic exactly when `1/2 <= pt <= ps`, and the
return to the identity at `N` revives distinguishability from `|2 p (N-1) - 1| < 1` to `1`.

The indivisibility half is not reproved here: it is the merged `c4r_implies_pIndivisible` applied
to the revival witness, exactly as the horizon route of `RecurrenceHorizon.lean` does.

Nothing in this module constructs a realization, defines a readback parent, or fixes a horizon
symbol; it supplies the family-level tightness that a realization-layer construction must exhibit.
No claim is made about physical accessibility of any horizon.
-/

namespace OIBridge
namespace ScalingFamily

open Finset Matrix HiddenMemory CausalReadback RecurrenceHorizon

/-! ### The symmetric binary channel -/

/-- **THE SYMMETRIC BINARY CHANNEL** with retention probability `p`. -/
def Bmat (p : ℝ) : Matrix (Fin 2) (Fin 2) ℝ := !![p, 1 - p; 1 - p, p]

@[simp] theorem Bmat_zero_zero (p : ℝ) : Bmat p 0 0 = p := rfl
@[simp] theorem Bmat_zero_one (p : ℝ) : Bmat p 0 1 = 1 - p := rfl
@[simp] theorem Bmat_one_zero (p : ℝ) : Bmat p 1 0 = 1 - p := rfl
@[simp] theorem Bmat_one_one (p : ℝ) : Bmat p 1 1 = p := rfl

/-- **THE CHANNEL AT `p = 1` IS THE IDENTITY**, which is what a visible return supplies. -/
theorem Bmat_one_eq : Bmat 1 = (1 : Matrix (Fin 2) (Fin 2) ℝ) := by
  ext i j
  fin_cases i <;> fin_cases j <;> simp [Bmat]

/-- **STOCHASTICITY** on the unit interval. -/
theorem Bmat_isRowStochastic {p : ℝ} (h0 : 0 ≤ p) (h1 : p ≤ 1) : IsRowStochastic (Bmat p) := by
  constructor
  · intro i j
    fin_cases i <;> fin_cases j <;> simp [Bmat] <;> linarith
  · intro i
    fin_cases i <;> simp [Bmat, Fin.sum_univ_two]

/-- **THE FAMILY IS CLOSED UNDER COMPOSITION.** -/
theorem Bmat_mul (p q : ℝ) : Bmat p * Bmat q = Bmat (2 * p * q - p - q + 1) := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [Bmat, Matrix.mul_apply, Fin.sum_univ_two] <;> ring

/-- **THE EXPLICIT STOCHASTIC FACTOR.** For `1/2 <= pt <= ps` with `1/2 < ps`, the channel at `ps`
carries to the channel at `pt` through a channel of the same family, and that factor is stochastic
exactly under those inequalities: it is at least `1/2` because `pt >= 1/2`, and at most `1` because
`pt <= ps`. -/
theorem Bmat_factor {ps pt : ℝ} (hs : 1 / 2 < ps) (ht : 1 / 2 ≤ pt) (hle : pt ≤ ps) :
    IsRowStochastic (Bmat ((pt + ps - 1) / (2 * ps - 1))) ∧
      Bmat ps * Bmat ((pt + ps - 1) / (2 * ps - 1)) = Bmat pt := by
  have hden : (0 : ℝ) < 2 * ps - 1 := by linarith
  have hne : (2 * ps - 1) ≠ 0 := ne_of_gt hden
  have hq0 : 0 ≤ (pt + ps - 1) / (2 * ps - 1) := div_nonneg (by linarith) (le_of_lt hden)
  have hq1 : (pt + ps - 1) / (2 * ps - 1) ≤ 1 := by rw [div_le_one hden]; linarith
  refine ⟨Bmat_isRowStochastic hq0 hq1, ?_⟩
  rw [Bmat_mul]
  congr 1
  field_simp
  ring

/-! ### Distinguishability of the two rooted rows -/

/-- **THE ROOTED-ROW DISTANCE IS `|2p - 1|`. -/
theorem tv_Bmat (p : ℝ) : tv (Bmat p 0) (Bmat p 1) = |2 * p - 1| := by
  have h : ∀ x : ℝ, |x| + |x| = 2 * |x| := by intro x; ring
  unfold tv
  rw [Fin.sum_univ_two]
  simp only [Bmat_zero_zero, Bmat_one_zero, Bmat_zero_one, Bmat_one_one]
  have e1 : p - (1 - p) = 2 * p - 1 := by ring
  have e2 : (1 - p) - p = -(2 * p - 1) := by ring
  rw [e1, e2, abs_neg, h]
  ring

/-- **AT `p = 1` THE ROWS ARE MAXIMALLY DISTINGUISHABLE.** -/
theorem tv_Bmat_one : tv (Bmat 1 0) (Bmat 1 1) = 1 := by
  rw [tv_Bmat]; norm_num

/-- **BELOW ONE THE ROWS ARE NOT MAXIMALLY DISTINGUISHABLE.** -/
theorem tv_Bmat_lt_one {p : ℝ} (h0 : 1 / 2 ≤ p) (h1 : p < 1) :
    tv (Bmat p 0) (Bmat p 1) < 1 := by
  rw [tv_Bmat, abs_of_nonneg (by linarith : (0:ℝ) ≤ 2 * p - 1)]
  linarith

/-! ### Tightness, uniform in the horizon

Both statements are quantified over `N` and over the retention sequence; neither is a check at any
particular horizon. -/

/-- **DIVISIBILITY BELOW THE RETURN.** A retention sequence that stays strictly above `1/2` and is
antitone below `N` gives a P-divisible family on every horizon `K < N`. The propagator is the
explicit factor, so no existence argument is left implicit. -/
theorem pDivisible_below {N : ℕ} {p : ℕ → ℝ}
    (hhalf : ∀ t, t < N → 1 / 2 < p t)
    (hanti : ∀ s t, s ≤ t → t < N → p t ≤ p s)
    {K : ℕ} (hK : K < N) :
    PDivisible K (fun t => Bmat (p t)) := by
  intro s t hst htK
  have htN : t < N := lt_of_le_of_lt htK hK
  have hsN : s < N := lt_trans hst htN
  have hs : 1 / 2 < p s := hhalf s hsN
  have ht : 1 / 2 ≤ p t := le_of_lt (hhalf t htN)
  have hle : p t ≤ p s := hanti s t (le_of_lt hst) htN
  obtain ⟨hstoch, hfac⟩ := Bmat_factor hs ht hle
  exact ⟨_, hstoch, hfac.symm⟩

/-- **REVIVAL AT THE RETURN.** If the retention sequence sits in `[1/2, 1)` at `N - 1` and returns
to `1` at `N`, the pair `(N-1, N)` is a `C4r N` witness. -/
theorem c4r_at_return {N : ℕ} {p : ℕ → ℝ} (hN : 0 < N)
    (hhalf : 1 / 2 ≤ p (N - 1)) (hlt : p (N - 1) < 1) (hpN : p N = 1) :
    C4r N (fun t => Bmat (p t)) := by
  refine ⟨0, 1, N - 1, N, by decide, ?_, le_rfl, ?_⟩
  · omega
  · simp only [hpN]
    rw [tv_Bmat_one]
    exact tv_Bmat_lt_one hhalf hlt

/-- **INDIVISIBILITY AT THE RETURN**, by the merged revival no-go rather than a new argument. -/
theorem pIndivisible_at_return {N : ℕ} {p : ℕ → ℝ} (hN : 0 < N)
    (hhalf : 1 / 2 ≤ p (N - 1)) (hlt : p (N - 1) < 1) (hpN : p N = 1) :
    PIndivisibleWithin N (fun t => Bmat (p t)) :=
  c4r_implies_pIndivisible N _ (c4r_at_return hN hhalf hlt hpN)

/-- **TIGHTNESS AT EVERY HORIZON, UNIFORM IN `N`.** For every `N > 0` and every retention sequence
that is antitone and strictly above `1/2` below `N`, sits strictly below `1` at `N - 1`, and
returns to `1` at `N`: the family is P-divisible on every horizon `K < N` and P-indivisible at `N`.

This is the family-level content a realization-layer construction has to exhibit. It fixes no
particular `N`, so a construction meeting these hypotheses for every `N` in an unbounded set yields
tight families at unboundedly many horizons. Nothing here asserts that such a construction exists,
and nothing here concerns physical accessibility. -/
theorem tight_at {N : ℕ} {p : ℕ → ℝ} (hN : 0 < N)
    (hhalf : ∀ t, t < N → 1 / 2 < p t)
    (hanti : ∀ s t, s ≤ t → t < N → p t ≤ p s)
    (hlt : p (N - 1) < 1) (hpN : p N = 1) :
    (∀ K, K < N → PDivisible K (fun t => Bmat (p t))) ∧
      PIndivisibleWithin N (fun t => Bmat (p t)) :=
  ⟨fun _ hK => pDivisible_below hhalf hanti hK,
    pIndivisible_at_return hN (le_of_lt (hhalf (N - 1) (by omega))) hlt hpN⟩

end ScalingFamily
end OIBridge

#print axioms OIBridge.ScalingFamily.Bmat_one_eq
#print axioms OIBridge.ScalingFamily.Bmat_isRowStochastic
#print axioms OIBridge.ScalingFamily.Bmat_mul
#print axioms OIBridge.ScalingFamily.Bmat_factor
#print axioms OIBridge.ScalingFamily.tv_Bmat
#print axioms OIBridge.ScalingFamily.tv_Bmat_one
#print axioms OIBridge.ScalingFamily.tv_Bmat_lt_one
#print axioms OIBridge.ScalingFamily.pDivisible_below
#print axioms OIBridge.ScalingFamily.c4r_at_return
#print axioms OIBridge.ScalingFamily.pIndivisible_at_return
#print axioms OIBridge.ScalingFamily.tight_at
