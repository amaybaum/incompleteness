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
    * the passivity layer — the general version needing no Gibbs law. The WEAK selector
      (`passivity_selector_nonuniform`) is the sharp form: with distinct energies, ONE
      passive, NON-UNIFORM state excludes the reflection — passivity for both orientations
      squeezes every pair of populations equal (`passive_antipassive_const`). Strictness is
      not needed; `passivity_selector` (strict) and `gibbs_strictlyPassive` (positive-β Gibbs
      states are strictly passive) are retained as the sufficient special cases.
    * `counting_passive` / `counting_strictlyPassive` — LAYER ONE of the H-orientation
      transport programme: exact finite-bath counting with a monotone bath count `Ω`
      (`β_E = ∂S_H/∂E ≥ 0`) makes the counting-selected profile passive for the classical
      energies. No Gibbs approximation, no thermodynamic limit, no common temperature.

  WHAT THIS DOES AND DOES NOT ESTABLISH. Together with AntiunitaryInvariance the honest
  structure is: operational data determine `H` up to unitary gauge AND the antiunitary
  reflection — two antiunitarily related reconstructions of the same complete circuit
  statistics, physically distinct only once an oriented structure is fixed; operational data
  PLUS one passive, non-maximally-mixed state determine `H` up to unitary gauge only. Whether
  the substratum DERIVES that state is the H-orientation transport programme: layer one
  (classical counting orients classically) is proved here; layer two (stationarity of the
  counting state under the reconstructed evolution diagonalizes it in the energy basis) and
  layer three (`energyOrder_transport`: the classical exchange ordering agrees with one of the
  two orientations of the reconstructed Bohr spectrum — sign only) are the named open targets,
  the third being the fork-deciding lemma.
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

/-- Double passivity forces equal populations on every energy-distinguished pair: passivity
for the reflected energies reverses every comparison. -/
theorem passive_antipassive_const {E p : Fin m → ℝ} {E₀ : ℝ}
    (hp : Passive E p) (hp' : Passive (fun c => -E c + E₀) p)
    {a b : Fin m} (hab : E a ≠ E b) : p a = p b := by
  rcases lt_or_gt_of_ne hab with h | h
  · have h1 := hp a b h
    have h2 := hp' b a (by simp only; linarith)
    linarith
  · have h1 := hp b a h
    have h2 := hp' a b (by simp only; linarith)
    linarith

/-- **THE WEAK ORIENTATION SELECTOR.** With distinct energies, ONE passive, non-uniform state
excludes the reflection — strictness is not needed: if the state stayed passive for the
reflected energies, every pair of populations would be squeezed equal. This is the minimal
physical requirement the H-orientation transport programme must meet: passive + not maximally
mixed, nothing more. -/
theorem passivity_selector_nonuniform {E p : Fin m → ℝ} {E₀ : ℝ}
    (hdist : ∀ a b : Fin m, a ≠ b → E a ≠ E b)
    (hp : Passive E p) {a b : Fin m} (hpab : p a ≠ p b) :
    ¬ Passive (fun c => -E c + E₀) p := by
  intro hp'
  exact hpab (passive_antipassive_const hp hp'
    (hdist a b fun h => hpab (congrArg p h)))

/-- **H-ORIENTATION TRANSPORT, LAYER ONE: counting orients classically.** If configuration `a`
carries classical energy `ε a` and receives weight proportional to the bath count
`Ω(E_tot − ε a)` with `Ω` monotone — that is, `β_E = ∂S_H/∂E ≥ 0` — the resulting profile is
passive for `ε`. Exact finite-bath counting: no Gibbs approximation, no thermodynamic limit,
no common temperature, no complete passivity. Layers two (stationarity of the counting state
under the reconstructed evolution diagonalizes it in the energy eigenbasis) and three
(`energyOrder_transport`: the classical exchange ordering agrees with one of the two
orientations of the reconstructed Bohr spectrum — sign only, no magnitudes) are the named open
targets; layer three is the fork-deciding lemma. -/
theorem counting_passive {Ω : ℝ → ℝ} (hΩ : Monotone Ω) (Etot : ℝ) (ε : Fin m → ℝ)
    (Z : ℝ) (hZ : 0 < Z) :
    Passive ε (fun a => Ω (Etot - ε a) / Z) := by
  intro a b hab
  have h1 : Ω (Etot - ε b) ≤ Ω (Etot - ε a) := hΩ (by linarith)
  exact (div_le_div_iff_of_pos_right hZ).mpr h1

/-- Strictly increasing bath counts give strict passivity. -/
theorem counting_strictlyPassive {Ω : ℝ → ℝ} (hΩ : StrictMono Ω) (Etot : ℝ)
    (ε : Fin m → ℝ) (Z : ℝ) (hZ : 0 < Z) :
    StrictlyPassive ε (fun a => Ω (Etot - ε a) / Z) := by
  intro a b hab
  exact div_lt_div_of_pos_right (hΩ (by linarith)) hZ

/-! ### Layer two, the mathematical half: stationarity diagonalizes

`stationary_diagonal` is the purely algebraic implication layer two of the H-orientation
transport programme needs: a state fixed by the evolution at every time, with a nondegenerate
spectrum, is diagonal in the energy eigenbasis — so it HAS a population profile for the
selectors above to test. Whether the counting-selected marginal IS stationary
(`counting_state_stationary`) is the physical half, audited separately: it does not follow
from the current substratum construction without new work, because the shell-counting state
is a correlated visible–hidden ensemble while the reconstructed channel is built on a fixed
product prior (GR §3.2's H-shell caveat). -/

/-- A matrix commuting with a nondegenerate diagonal is diagonal. -/
theorem commutant_diagonal (M : Matrix (Fin m) (Fin m) ℂ) (E : Fin m → ℝ)
    (hcomm : M * Matrix.diagonal (fun a => (E a : ℂ))
      = Matrix.diagonal (fun a => (E a : ℂ)) * M)
    (hE : Function.Injective E) {a b : Fin m} (hab : a ≠ b) : M a b = 0 := by
  have h := congrFun (congrFun hcomm a) b
  rw [Matrix.mul_diagonal, Matrix.diagonal_mul] at h
  have h2 : ((E b : ℂ) - (E a : ℂ)) * M a b = 0 := by linear_combination h
  rcases mul_eq_zero.mp h2 with h' | h'
  · exfalso
    apply hab
    apply hE
    have : (E a : ℂ) = (E b : ℂ) := by linear_combination -h'
    exact_mod_cast this
  · exact h'

/-- The propagator in matrix form is the spectral sandwich. -/
lemma umat_spectral (V : Matrix (Fin m) (Fin m) ℂ) (E : Fin m → ℝ) (t : ℝ) :
    Matrix.of (BohrFrequency.Umat V E t)
      = V * Matrix.diagonal (fun a => Complex.exp (-(Complex.I * (E a : ℂ) * (t : ℂ)))) * Vᴴ := by
  ext i j
  rw [Matrix.of_apply, spectral_apply]
  show (∑ a, V i a * Complex.exp (-(Complex.I * (E a : ℂ) * (t : ℂ))) * star (V j a)) = _
  exact Finset.sum_congr rfl fun a _ => by rw [Complex.star_def]

/-- **STATIONARITY DIAGONALIZES.** A state fixed by the evolution at every time, with all
energies distinct, has vanishing off-diagonal matrix elements in the energy eigenbasis: the
phase `e^{−i(E_a−E_b)t}` evaluated at `t = π/(E_a−E_b)` is `−1`. -/
theorem stationary_offdiag (V ρ : Matrix (Fin m) (Fin m) ℂ) (E : Fin m → ℝ)
    (hV : V * Vᴴ = 1) (hE : Function.Injective E)
    (hstat : ∀ t : ℝ, Matrix.of (BohrFrequency.Umat V E t) * ρ
      * (Matrix.of (BohrFrequency.Umat V E t))ᴴ = ρ)
    {a b : Fin m} (hab : a ≠ b) : (Vᴴ * ρ * V) a b = 0 := by
  have hV' : Vᴴ * V = 1 := mul_eq_one_comm.mp hV
  have hEab : E a - E b ≠ 0 := sub_ne_zero.mpr (fun h => hab (hE h))
  set t : ℝ := Real.pi / (E a - E b) with ht
  have h1 := hstat t
  rw [umat_spectral] at h1
  -- conjugate by Vᴴ … V to land in the eigenbasis
  have h2 : Matrix.diagonal (fun c => Complex.exp (-(Complex.I * (E c : ℂ) * (t : ℂ))))
      * (Vᴴ * ρ * V)
      * (Matrix.diagonal (fun c => Complex.exp (-(Complex.I * (E c : ℂ) * (t : ℂ)))))ᴴ
      = Vᴴ * ρ * V := by
    calc Matrix.diagonal (fun c => Complex.exp (-(Complex.I * (E c : ℂ) * (t : ℂ))))
          * (Vᴴ * ρ * V)
          * (Matrix.diagonal (fun c => Complex.exp (-(Complex.I * (E c : ℂ) * (t : ℂ)))))ᴴ
        = (Vᴴ * V) * Matrix.diagonal (fun c => Complex.exp (-(Complex.I * (E c : ℂ) * (t : ℂ))))
          * (Vᴴ * ρ * V)
          * (Matrix.diagonal (fun c => Complex.exp (-(Complex.I * (E c : ℂ) * (t : ℂ)))))ᴴ
          * (Vᴴ * V) := by rw [hV']; noncomm_ring
      _ = Vᴴ * (V * Matrix.diagonal (fun c => Complex.exp (-(Complex.I * (E c : ℂ) * (t : ℂ))))
          * Vᴴ * ρ
          * (V * (Matrix.diagonal (fun c => Complex.exp (-(Complex.I * (E c : ℂ) * (t : ℂ)))))ᴴ
            * Vᴴ)) * V := by noncomm_ring
      _ = Vᴴ * (V * Matrix.diagonal (fun c => Complex.exp (-(Complex.I * (E c : ℂ) * (t : ℂ))))
          * Vᴴ * ρ
          * (V * Matrix.diagonal (fun c => Complex.exp (-(Complex.I * (E c : ℂ) * (t : ℂ))))
            * Vᴴ)ᴴ) * V := by
            rw [Matrix.conjTranspose_mul, Matrix.conjTranspose_mul,
              Matrix.conjTranspose_conjTranspose]
            noncomm_ring
      _ = Vᴴ * ρ * V := by rw [show V * Matrix.diagonal (fun c => Complex.exp
            (-(Complex.I * (E c : ℂ) * (t : ℂ)))) * Vᴴ * ρ
            * (V * Matrix.diagonal (fun c => Complex.exp (-(Complex.I * (E c : ℂ) * (t : ℂ))))
              * Vᴴ)ᴴ = ρ from h1]
  have h3 := congrFun (congrFun h2 a) b
  rw [Matrix.diagonal_conjTranspose, Matrix.mul_diagonal, Matrix.diagonal_mul] at h3
  -- the phase at t = π/(E_a − E_b) is −1
  have hphase : Complex.exp (-(Complex.I * (E a : ℂ) * (t : ℂ)))
      * star (Complex.exp (-(Complex.I * (E b : ℂ) * (t : ℂ)))) = -1 := by
    rw [Complex.star_def, ← Complex.exp_conj]
    rw [show (starRingEnd ℂ) (-(Complex.I * (E b : ℂ) * (t : ℂ)))
      = Complex.I * (E b : ℂ) * (t : ℂ) by
        simp only [map_neg, map_mul, Complex.conj_I, Complex.conj_ofReal]
        ring]
    rw [← Complex.exp_add]
    have hreal : (E a - E b) * t = Real.pi := by
      rw [ht]
      field_simp
    have hrealC : ((E a : ℂ) - (E b : ℂ)) * (t : ℂ) = (Real.pi : ℂ) := by
      exact_mod_cast congrArg (fun x : ℝ => (x : ℂ)) hreal
    rw [show -(Complex.I * (E a : ℂ) * (t : ℂ)) + Complex.I * (E b : ℂ) * (t : ℂ)
      = -(((E a : ℂ) - (E b : ℂ)) * (t : ℂ)) * Complex.I by ring]
    rw [hrealC, show (-(Real.pi : ℂ)) * Complex.I = -((Real.pi : ℂ) * Complex.I) by ring,
      Complex.exp_neg, Complex.exp_pi_mul_I]
    norm_num
  rw [Pi.star_apply] at h3
  have h4 : (Vᴴ * ρ * V) a b
      * (Complex.exp (-(Complex.I * (E a : ℂ) * (t : ℂ)))
        * star (Complex.exp (-(Complex.I * (E b : ℂ) * (t : ℂ))))) = (Vᴴ * ρ * V) a b := by
    linear_combination h3
  rw [hphase] at h4
  have h5 : (2 : ℂ) * (Vᴴ * ρ * V) a b = 0 := by linear_combination -h4
  exact (mul_eq_zero.mp h5).resolve_left (by norm_num)

/-- Packaged: a stationary state with nondegenerate spectrum IS a population profile on the
energy eigenbasis — the object the orientation selectors test. -/
theorem stationary_spectral_form (V ρ : Matrix (Fin m) (Fin m) ℂ) (E : Fin m → ℝ)
    (hV : V * Vᴴ = 1) (hE : Function.Injective E)
    (hstat : ∀ t : ℝ, Matrix.of (BohrFrequency.Umat V E t) * ρ
      * (Matrix.of (BohrFrequency.Umat V E t))ᴴ = ρ) :
    ρ = V * Matrix.diagonal (fun a => (Vᴴ * ρ * V) a a) * Vᴴ := by
  have hM : Vᴴ * ρ * V = Matrix.diagonal (fun a => (Vᴴ * ρ * V) a a) := by
    ext i j
    by_cases hij : i = j
    · subst hij
      rw [Matrix.diagonal_apply_eq]
    · rw [Matrix.diagonal_apply_ne _ hij]
      exact stationary_offdiag V ρ E hV hE hstat hij
  calc ρ = (V * Vᴴ) * ρ * (V * Vᴴ) := by rw [hV]; noncomm_ring
    _ = V * (Vᴴ * ρ * V) * Vᴴ := by noncomm_ring
    _ = V * Matrix.diagonal (fun a => (Vᴴ * ρ * V) a a) * Vᴴ := by
        rw [hM]
        simp [Matrix.diagonal_apply_eq]

#print axioms gibbs_reflection
#print axioms gibbs_reflection_perm
#print axioms gibbs_orientation
#print axioms transported_gibbs
#print axioms orientation_excludes_reflection
#print axioms gibbs_strictlyPassive
#print axioms passivity_selector
#print axioms passive_antipassive_const
#print axioms passivity_selector_nonuniform
#print axioms counting_passive
#print axioms counting_strictlyPassive
#print axioms commutant_diagonal
#print axioms umat_spectral
#print axioms stationary_offdiag
#print axioms stationary_spectral_form

end ThermalOrientation
end OIBridge
