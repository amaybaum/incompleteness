/-
  OIBridge/ThermalOrientation.lean — thermodynamic orientation distinguishes the two branches.

  PHASE TWO, ITEM TWO. AntiunitaryInvariance proves that no circuit data separate `H` from the
  reflected `−D H̄ D† + E₀`: the antiunitary conjugation is a global symmetry of the whole
  operational formalism. This file proves that ORIENTED THERMAL STRUCTURE is exactly what that
  symmetry fails to preserve:

    * `gibbs_reflection` / `transported_gibbs` — the antiunitary image of the positive-
      temperature Gibbs state of `H` is the NEGATIVE-temperature Gibbs state of the reflected
      Hamiltonian: `D ρ̄_β(H) D† = ρ_{−β}(H')`, stated in spectral form with the coboundary
      data `W_{i,τa} = d_i β_a V̄_{ia}` of the reflection branch.
    * `gibbs_orientation` — for `β ≠ 0` and any two distinct energies, the `+β` and `−β`
      Gibbs states differ: temperature orientation is not reflection-invariant.
    * `orientation_excludes_reflection` — assembled: under the reflected alignment
      `E'∘τ = −E + E₀` with two distinct energies, the transported thermal state is never a
      positive-temperature Gibbs state of the new model. A physically fixed `β > 0` KMS/Gibbs
      structure therefore excludes the antiunitary branch outright.
    * the passivity layer (`StrictlyPassive`, `gibbs_strictlyPassive`, `passivity_selector`) —
      the more general version needing no Gibbs law: a strictly passive population profile
      (higher energy, strictly lower population) cannot remain passive after energy reflection
      unless all compared energies coincide; positive-temperature Gibbs states are strictly
      passive.

  WHAT THIS DOES AND DOES NOT ESTABLISH. Together with AntiunitaryInvariance the honest
  structure is: operational data determine `H` up to unitary gauge AND the antiunitary
  reflection; operational data PLUS an independently oriented positive KMS/passive state
  determine `H` up to unitary gauge only. Whether the substratum DERIVES the positive
  orientation rather than assuming it is the open Level-3 question recorded in the ledger —
  these theorems make the alternatives exact, they do not decide them.
-/
import OIBridge.CongruentReconstruction

namespace OIBridge
namespace ThermalOrientation

open Complex Matrix CongruentReconstruction

local notation "conj'" => (starRingEnd ℂ)

variable {m : ℕ}

/-- The Gibbs population profile at inverse temperature `β`. -/
noncomputable def gibbs (β : ℝ) (E : Fin m → ℝ) (a : Fin m) : ℝ :=
  Real.exp (-β * E a) / ∑ c, Real.exp (-β * E c)

lemma gibbs_pos (β : ℝ) (E : Fin m → ℝ) (a : Fin m) : 0 < gibbs β E a :=
  div_pos (Real.exp_pos _)
    (Finset.sum_pos (fun _ _ => Real.exp_pos _) ⟨a, Finset.mem_univ a⟩)

/-- **REFLECTION REVERSES TEMPERATURE, scalar form.** The `−β` Gibbs profile of the reflected
energies is the `+β` Gibbs profile of the original energies: the shift `E₀` cancels in the
normalization, and the sign flip of the energies is absorbed by the sign flip of `β`. -/
theorem gibbs_reflection (β E₀ : ℝ) (E : Fin m → ℝ) :
    gibbs (-β) (fun a => -E a + E₀) = gibbs β E := by
  funext a
  rw [gibbs, gibbs]
  have hnum : ∀ c : Fin m, Real.exp (-(-β) * (-E c + E₀))
      = Real.exp (-β * E c) * Real.exp (β * E₀) := by
    intro c
    rw [← Real.exp_add]
    ring_nf
  rw [hnum a, Finset.sum_congr rfl fun c _ => hnum c, ← Finset.sum_mul]
  rw [mul_div_mul_right _ _ (Real.exp_ne_zero _)]

/-- The permutation-aligned form: with `E'(τa) = −E a + E₀`, the `−β` Gibbs population of the
reflected model at mode `τa` is the `+β` Gibbs population of the original at mode `a`. -/
theorem gibbs_reflection_perm (β E₀ : ℝ) (E E' : Fin m → ℝ) (τ : Equiv.Perm (Fin m))
    (halign : ∀ a, E' (τ a) = -E a + E₀) (a : Fin m) :
    gibbs (-β) E' (τ a) = gibbs β E a := by
  have hsum : (∑ c, Real.exp (-(-β) * E' c)) = ∑ c, Real.exp (-(-β) * (-E c + E₀)) := by
    rw [← Equiv.sum_comp τ (fun c => Real.exp (-(-β) * E' c))]
    exact Finset.sum_congr rfl fun c _ => by rw [halign c]
  rw [gibbs, halign a, hsum]
  have := congrFun (gibbs_reflection (m := m) β E₀ E) a
  rw [gibbs, gibbs] at this
  exact this

/-- **TEMPERATURE ORIENTATION IS NOT REFLECTION-INVARIANT.** For `β ≠ 0` and any two distinct
energies, the `+β` and `−β` Gibbs profiles differ. (With all energies equal they coincide —
the degenerate exception is exactly the maximally mixed case.) -/
theorem gibbs_orientation (β : ℝ) (hβ : β ≠ 0) (E : Fin m → ℝ)
    {a b : Fin m} (hab : E a ≠ E b) :
    gibbs β E ≠ gibbs (-β) E := by
  intro h
  have Zp : (0 : ℝ) < ∑ c, Real.exp (-β * E c) :=
    Finset.sum_pos (fun c _ => Real.exp_pos _) ⟨a, Finset.mem_univ a⟩
  have Zm : (0 : ℝ) < ∑ c, Real.exp (-(-β) * E c) :=
    Finset.sum_pos (fun c _ => Real.exp_pos _) ⟨a, Finset.mem_univ a⟩
  have ha := congrFun h a
  have hb := congrFun h b
  rw [gibbs, gibbs, div_eq_div_iff (ne_of_gt Zp) (ne_of_gt Zm)] at ha hb
  -- cross-multiply the two identities and cancel the positive partition sums
  have hcross : Real.exp (-β * E a) * Real.exp (-(-β) * E b)
      = Real.exp (-(-β) * E a) * Real.exp (-β * E b) := by
    have hmul : (0 : ℝ) < (∑ c, Real.exp (-β * E c)) * ∑ c, Real.exp (-(-β) * E c) :=
      mul_pos Zp Zm
    have hstep : Real.exp (-β * E a) * Real.exp (-(-β) * E b)
          * ((∑ c, Real.exp (-β * E c)) * ∑ c, Real.exp (-(-β) * E c))
        = Real.exp (-(-β) * E a) * Real.exp (-β * E b)
          * ((∑ c, Real.exp (-β * E c)) * ∑ c, Real.exp (-(-β) * E c)) := by
      calc Real.exp (-β * E a) * Real.exp (-(-β) * E b)
            * ((∑ c, Real.exp (-β * E c)) * ∑ c, Real.exp (-(-β) * E c))
          = (Real.exp (-β * E a) * ∑ c, Real.exp (-(-β) * E c))
            * (Real.exp (-(-β) * E b) * ∑ c, Real.exp (-β * E c)) := by ring
        _ = (Real.exp (-(-β) * E a) * ∑ c, Real.exp (-β * E c))
            * (Real.exp (-β * E b) * ∑ c, Real.exp (-(-β) * E c)) := by rw [ha, ← hb]
        _ = Real.exp (-(-β) * E a) * Real.exp (-β * E b)
            * ((∑ c, Real.exp (-β * E c)) * ∑ c, Real.exp (-(-β) * E c)) := by ring
    exact mul_right_cancel₀ (ne_of_gt hmul) hstep
  rw [← Real.exp_add, ← Real.exp_add] at hcross
  have := Real.exp_injective hcross
  apply hab
  have : -β * E a + -(-β) * E b = -(-β) * E a + -β * E b := this
  have h2 : 2 * β * (E b - E a) = 0 := by linarith
  have h3 : E b - E a = 0 := by
    rcases mul_eq_zero.mp h2 with h | h
    · rcases mul_eq_zero.mp h with h | h
      · norm_num at h
      · exact absurd h hβ
    · exact h
  linarith

/-! ### The matrix form: the antiunitary image of a positive-temperature Gibbs state is the
negative-temperature Gibbs state of the reflected model -/

/-- **`D ρ̄_β(H) D† = ρ_{−β}(H')`, spectral form.** With the reflection-branch coboundary
`W_{i,τa} = d_i β_a V̄_{ia}` (β unimodular) and the reflected alignment `E'∘τ = −E + E₀`, the
`−β` Gibbs state of the new model IS the conjugated, `D`-dressed image of the `+β` Gibbs state
of the original. Temperature orientation is the entire difference between the branches. -/
theorem transported_gibbs (V W : Matrix (Fin m) (Fin m) ℂ) (τ : Equiv.Perm (Fin m))
    (E E' : Fin m → ℝ) (E₀ β : ℝ) (d bc : Fin m → ℂ)
    (halign : ∀ a, E' (τ a) = -E a + E₀)
    (hbc : ∀ a, bc a * conj' (bc a) = 1)
    (hcob : ∀ i a, W i (τ a) = d i * bc a * conj' (V i a)) :
    W * Matrix.diagonal (fun c => ((gibbs (-β) E' c : ℝ) : ℂ)) * Wᴴ
      = Matrix.diagonal d
          * conjM (V * Matrix.diagonal (fun a => ((gibbs β E a : ℝ) : ℂ)) * Vᴴ)
          * (Matrix.diagonal d)ᴴ := by
  ext i j
  rw [Matrix.diagonal_conjTranspose, Matrix.mul_diagonal, Matrix.diagonal_mul]
  rw [conjM_apply, spectral_apply W _ i j, spectral_apply V _ i j]
  rw [← Equiv.sum_comp τ
    (fun c => W i c * ((gibbs (-β) E' c : ℝ) : ℂ) * conj' (W j c))]
  rw [map_sum, Finset.mul_sum, Finset.sum_mul]
  refine Finset.sum_congr rfl fun a _ => ?_
  rw [hcob i a, hcob j a, gibbs_reflection_perm β E₀ E E' τ halign a]
  rw [Pi.star_apply, Complex.star_def]
  simp only [map_mul, Complex.conj_conj, Complex.conj_ofReal]
  linear_combination (d i * conj' (V i a) * ((gibbs β E a : ℝ) : ℂ) * V j a
    * conj' (d j)) * hbc a

/-- **THE ORIENTATION SELECTOR, assembled.** Under the reflected alignment with two distinct
energies and `β ≠ 0`, the transported thermal state — which is the `−β` Gibbs state of the new
model — is NOT the `+β` Gibbs state of the new model. A physically fixed positive-temperature
Gibbs structure therefore excludes the antiunitary branch. -/
theorem orientation_excludes_reflection (β : ℝ) (hβ : β ≠ 0)
    (E E' : Fin m → ℝ) (τ : Equiv.Perm (Fin m)) (E₀ : ℝ)
    (halign : ∀ a, E' (τ a) = -E a + E₀) {a b : Fin m} (hab : E a ≠ E b) :
    gibbs (-β) E' ≠ gibbs β E' := by
  have hne : E' (τ a) ≠ E' (τ b) := by
    rw [halign a, halign b]
    intro h
    exact hab (by linarith)
  exact fun h => gibbs_orientation β hβ E' hne h.symm

/-! ### The passivity layer: orientation without the Gibbs law -/

/-- Strict passivity: strictly higher energy, strictly lower population. -/
def StrictlyPassive (E p : Fin m → ℝ) : Prop := ∀ a b, E a < E b → p b < p a

/-- Passivity: higher energy, no higher population. -/
def Passive (E p : Fin m → ℝ) : Prop := ∀ a b, E a < E b → p b ≤ p a

/-- Positive-temperature Gibbs profiles are strictly passive. -/
theorem gibbs_strictlyPassive {β : ℝ} (hβ : 0 < β) (E : Fin m → ℝ) :
    StrictlyPassive E (gibbs β E) := by
  intro a b hab
  have Z : (0 : ℝ) < ∑ c, Real.exp (-β * E c) :=
    Finset.sum_pos (fun c _ => Real.exp_pos _) ⟨a, Finset.mem_univ a⟩
  apply div_lt_div_of_pos_right ?_ Z
  exact Real.exp_lt_exp.mpr (by nlinarith)

/-- **PASSIVITY ORIENTS THE HAMILTONIAN.** A strictly passive population profile cannot remain
even weakly passive after reflecting the energies, unless the compared energies coincide: the
reflection turns strict passivity into strict activity. No Gibbs law is needed. -/
theorem passivity_selector {E p : Fin m → ℝ} {E₀ : ℝ}
    (hsp : StrictlyPassive E p) {a b : Fin m} (hab : E a ≠ E b) :
    ¬ Passive (fun c => -E c + E₀) p := by
  intro hpass
  rcases lt_or_gt_of_ne hab with h | h
  · have h1 := hsp a b h
    have h2 := hpass b a (by simp only; linarith)
    linarith
  · have h1 := hsp b a h
    have h2 := hpass a b (by simp only; linarith)
    linarith

#print axioms gibbs_reflection
#print axioms gibbs_reflection_perm
#print axioms gibbs_orientation
#print axioms transported_gibbs
#print axioms orientation_excludes_reflection
#print axioms gibbs_strictlyPassive
#print axioms passivity_selector

end ThermalOrientation
end OIBridge
