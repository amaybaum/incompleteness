/-
  OIBridge/OrientationClosure.lean — the orientation question closed at its exact boundary:
  SRC is transpose-stable, the universal orientation no-go, and the properly named oriented
  conditions.

  PHASE THREE, ROUND NINE — the final audit before the phase-three synthesis. Round eight
  drew the boundary of C3c: unoriented data select QM only up to antiunitary equivalence,
  and an oriented reference O with O(ΘR) = −O(R), O(R) > 0 resolves the fork. What remained
  was an asymmetry the naming had not yet made explicit: the two named premises are NOT
  symmetric remaining obligations.

  §A — SRC IS AN EXISTENCE CONDITION, NOT AN ORIENTATION SELECTOR.
  `shellRepresentation_transpose_stable`: `ShellRepresentationConsistency` holds for a
  model iff it holds for its transpose/reflected partner `(V̄, −E)` — transpose the
  represented state and reflect the Hamiltonian, and PSD, trace one, stationarity
  (`umat_reflect_conjM`: the reflected propagator IS the conjugated propagator, phase
  two's `reflect_conj`; `conjM_sandwich_transpose`: conjugated sandwiches transpose), and
  the visible diagonal all survive. So SRC alone cannot choose the antiunitary branch.
  `OperationalTransitionIdentification` is different: it is genuinely orientation-
  sensitive (`transitionIdentification_orientation_sensitive` — OTI for the labels and
  for their reflection forces every Bohr frequency equal, by injectivity of `exp`).

  §B — THE STATE-SIDE ORIENTED CONDITION, NAMED. What orients on the state side is
  `OrientedShellRepresentation`: the SRC clauses PLUS spectral passivity aligned with the
  energy order PLUS nonuniformity. Under the carrier nondegeneracies — unitary model,
  distinct energies, and `ReadoutSeparating` (the visible readout pins the spectral
  populations: injectivity of the moduli mixture `p = B·q`, exactly the comb-mixture map
  of the CoherentLift audit) — it is orientation-sensitive
  (`orientedShellRepresentation_orientation_sensitive`): the two members of a reflection
  pair share one spectral profile, which cannot be passive for both orientations without
  being uniform (`passive_antipassive_const`'s squeeze, run inline).

  §C — THE UNIVERSAL ORIENTATION NO-GO. `no_universal_oriented_property`: if an
  admissible class is closed under Θ and inhabited, no property with P(R) ⟹ ¬P(ΘR) can
  hold throughout the class. Specialized to both oriented conditions
  (`no_symmetric_condition_forces_transitionIdentification`,
  `no_symmetric_condition_forces_orientedShell`):

      ┌────────────────────────────────────────────────────────────────────────┐
      │  Bare transpose-symmetric coherent-completion conditions cannot force  │
      │  an orientation.                                                       │
      └────────────────────────────────────────────────────────────────────────┘

  Not merely "not yet derived": IMPOSSIBLE from any condition that is itself
  transpose-symmetric — and phase two proved the bare conditions are (all circuit data
  Θ-invariant, the native primitives Θ-fixed, and now SRC itself Θ-stable).

  THE RESULTING MAP. The classification problem and the existence problem are separate.
  C3b/C3c classify every completion that exists; `twoByTwo_no_local_lift` shows some
  nominal carriers admit none. There is no larger free family of coherent theories left:
  existing completions are ordinary complex QM modulo a single global antiunitary ℤ₂, and
  the terminal forms are

      OI + existence of an OI-compatible coherent completion   ⟹  QM / ℤ₂ᵃⁿᵗⁱ
      OI + coherent completion + oriented thermodynamic bridge ⟹  QM

  (the first for every existing completion satisfying the established genericity and
  alignment conditions; the second up to ordinary unitary gauge, the bridge being OTI or
  OrientedShellRepresentation). The remaining substantive questions are exactly two:
  does the actual OI substratum land in the existence class of an OI-compatible coherent
  completion, and does its classical thermodynamic arrow enter that completion through an
  oriented bridge? Every other status is now settled as "proved", "impossible from
  unoriented data", or "conditional on coherent-completion existence" — with no
  ambiguity between the three.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.OrientationSelection

namespace OIBridge
namespace OrientationClosure

open Complex Matrix CongruentReconstruction ThermalOrientation ShellAssignment
open scoped ComplexOrder

local notation "conj'" => (starRingEnd ℂ)

variable {m : ℕ}

/-! ### Section A — SRC is transpose-stable -/

/-- Entrywise conjugation is an involution. -/
theorem conjM_conjM (M : Matrix (Fin m) (Fin m) ℂ) : conjM (conjM M) = M := by
  ext i j
  rw [conjM_apply, conjM_apply, Complex.conj_conj]

/-- A conjugated sandwich is the transposed sandwich: `V̄ ρᵀ V̄ᴴ = (V ρ Vᴴ)ᵀ` — the
channel-level identity behind phase two's `string_invariance`, extracted. -/
theorem conjM_sandwich_transpose (A ρ : Matrix (Fin m) (Fin m) ℂ) :
    conjM A * ρᵀ * (conjM A)ᴴ = (A * ρ * Aᴴ)ᵀ := by
  have h1 : (conjM A)ᴴ = Aᵀ := AntiunitaryInvariance.conjOp_conjTranspose A
  rw [h1, Matrix.transpose_mul, Matrix.transpose_mul]
  rw [show (Aᴴ)ᵀ = conjM A from AntiunitaryInvariance.transpose_conjTranspose_eq A]
  rw [Matrix.mul_assoc]

/-- The propagator of the reflected model `(V̄, −E)` is the conjugated propagator — phase
two's `reflect_conj` in the matrix form the SRC clauses use. -/
theorem umat_reflect_conjM (Vm : Matrix (Fin m) (Fin m) ℂ) (E : Fin m → ℝ) (t : ℝ) :
    Matrix.of (BohrFrequency.Umat (conjM Vm) (fun a => -E a) t)
      = conjM (Matrix.of (BohrFrequency.Umat Vm E t)) := by
  ext i j
  exact BohrFrequency.reflect_conj (fun i a => Vm i a) E t i j

/-- **SRC IS AN EXISTENCE CONDITION, NOT AN ORIENTATION SELECTOR.**
`ShellRepresentationConsistency` holds for a model iff it holds for the
transpose/reflected partner `(V̄, −E)`: transposing the represented state preserves PSD,
trace, the visible diagonal, and stationarity under the reflected propagator. SRC alone
cannot choose between the two branches. -/
theorem shellRepresentation_transpose_stable (Vm : Matrix (Fin m) (Fin m) ℂ)
    (E : Fin m → ℝ) (p : Fin m → ℝ) :
    ShellRepresentationConsistency Vm E p
      ↔ ShellRepresentationConsistency (conjM Vm) (fun a => -E a) p := by
  have fwd : ∀ (W : Matrix (Fin m) (Fin m) ℂ) (F : Fin m → ℝ),
      ShellRepresentationConsistency W F p
        → ShellRepresentationConsistency (conjM W) (fun a => -F a) p := by
    rintro W F ⟨ρ, hpsd, htr, hstat, hread⟩
    refine ⟨ρᵀ, hpsd.transpose, by rw [Matrix.trace_transpose]; exact htr,
      fun t => ?_, fun i => ?_⟩
    · rw [umat_reflect_conjM W F t, conjM_sandwich_transpose, hstat t]
    · rw [Matrix.transpose_apply]
      exact hread i
  constructor
  · exact fwd Vm E
  · intro h
    have h2 := fwd (conjM Vm) (fun a => -E a) h
    simpa [conjM_conjM] using h2

/-! ### Section B — the oriented conditions, properly named -/

/-- **THE RATE-ROUTE PREMISE IS GENUINELY ORIENTATION-SENSITIVE.** The identification
cannot hold for the Bohr labels and for their reflection at once, unless the two named
frequencies coincide: equal exponentials transport through `exp`'s injectivity to
`τ_K·Δω = −τ_K·Δω`. OTI, unlike SRC, is an oriented condition. -/
theorem transitionIdentification_orientation_sensitive {βE τK : ℝ} (hτ : 0 < τK)
    {ε ω : Fin m → ℝ} {E₀ : ℝ} {a b : Fin m} (hab : ω a ≠ ω b)
    (h : OperationalTransitionIdentification βE τK ε ω) :
    ¬ OperationalTransitionIdentification βE τK ε (fun c => -ω c + E₀) := by
  intro h'
  have h2 := Real.exp_injective ((h a b).symm.trans (h' a b))
  have hlin : τK * (ω b - ω a) = 0 := by
    have h3 : -(τK * (ω b - ω a)) = -(τK * ((-ω b + E₀) - (-ω a + E₀))) := h2
    nlinarith [h3]
  rcases mul_eq_zero.mp hlin with h0 | h0
  · exact absurd h0 (ne_of_gt hτ)
  · exact hab (by linarith)

/-- **THE STATE-SIDE ORIENTED CONDITION, NAMED.** The SRC clauses PLUS spectral passivity
aligned with the energy order PLUS nonuniformity: a genuine state, stationary, with the
classical visible readout, whose spectral populations strictly know which way energy
runs. This — not SRC — is what the state route feeds the classification. -/
def OrientedShellRepresentation (Vm : Matrix (Fin m) (Fin m) ℂ)
    (E : Fin m → ℝ) (p : Fin m → ℝ) : Prop :=
  ∃ ρ : Matrix (Fin m) (Fin m) ℂ,
    ρ.PosSemidef ∧ Matrix.trace ρ = 1
    ∧ (∀ t : ℝ, Matrix.of (BohrFrequency.Umat Vm E t) * ρ
        * (Matrix.of (BohrFrequency.Umat Vm E t))ᴴ = ρ)
    ∧ (∀ i, ρ i i = ((p i : ℝ) : ℂ))
    ∧ Passive E (fun a => ((Vmᴴ * ρ * Vm) a a).re)
    ∧ ∃ a b : Fin m, ((Vmᴴ * ρ * Vm) a a).re ≠ ((Vmᴴ * ρ * Vm) b b).re

/-- **THE READOUT PINS THE SPECTRAL POPULATIONS.** Injectivity of the moduli mixture
`p_i = Σ_a |V_ia|² q_a` — exactly the comb-mixture map of the CoherentLift audit
(`shell_representation_from_comb`). The carrier nondegeneracy under which the visible
diagonal determines the stationary state's spectral profile. -/
def ReadoutSeparating (Vm : Matrix (Fin m) (Fin m) ℂ) : Prop :=
  ∀ z w : Fin m → ℂ,
    (∀ i, ∑ a, Vm i a * z a * conj' (Vm i a) = ∑ a, Vm i a * w a * conj' (Vm i a))
      → z = w

/-- The visible diagonal of a stationary state, in spectral-profile form. -/
theorem stationary_readout (Vm ρ : Matrix (Fin m) (Fin m) ℂ) (E : Fin m → ℝ)
    (hV : Vm * Vmᴴ = 1) (hE : Function.Injective E)
    (hstat : ∀ t : ℝ, Matrix.of (BohrFrequency.Umat Vm E t) * ρ
      * (Matrix.of (BohrFrequency.Umat Vm E t))ᴴ = ρ) (i : Fin m) :
    ∑ c, Vm i c * ((Vmᴴ * ρ * Vm) c c) * conj' (Vm i c) = ρ i i := by
  conv_rhs => rw [stationary_spectral_form Vm ρ E hV hE hstat]
  rw [spectral_apply]

/-- **THE ORIENTED SHELL CONDITION IS ORIENTATION-SENSITIVE.** Under the carrier
nondegeneracies — unitary model, distinct energies, separating readout — the oriented
condition cannot hold for a model and for its transpose/reflected partner at once: the
shared visible readout pins one spectral profile for both, and a nonuniform profile
cannot be passive for both energy orientations. -/
theorem orientedShellRepresentation_orientation_sensitive
    {Vm : Matrix (Fin m) (Fin m) ℂ} {E : Fin m → ℝ} {p : Fin m → ℝ}
    (hV : Vm * Vmᴴ = 1) (hdist : ∀ a b : Fin m, a ≠ b → E a ≠ E b)
    (hB : ReadoutSeparating Vm)
    (h1 : OrientedShellRepresentation Vm E p) :
    ¬ OrientedShellRepresentation (conjM Vm) (fun a => -E a) p := by
  rintro ⟨ρ', hpsd', htr', hstat', hread', hpass', a₂, b₂, hne₂⟩
  obtain ⟨ρ, hpsd, htr, hstat, hread, hpass, a₁, b₁, hne₁⟩ := h1
  have hE : Function.Injective E := fun x y hxy => by
    by_contra hne
    exact hdist x y hne hxy
  have hEneg : Function.Injective (fun a => -E a) := fun x y hxy => hE (neg_injective hxy)
  have hV' : conjM Vm * (conjM Vm)ᴴ = 1 := conjM_unitary hV
  -- both readouts are the same p, so the separating readout pins one shared profile
  have hro : ∀ i, ∑ c, Vm i c * ((Vmᴴ * ρ * Vm) c c) * conj' (Vm i c) = ((p i : ℝ) : ℂ) := by
    intro i
    rw [stationary_readout Vm ρ E hV hE hstat i]
    exact hread i
  have hro' : ∀ i, ∑ c, Vm i c * (((conjM Vm)ᴴ * ρ' * conjM Vm) c c) * conj' (Vm i c)
      = ((p i : ℝ) : ℂ) := by
    intro i
    have h0 := stationary_readout (conjM Vm) ρ' (fun a => -E a) hV' hEneg hstat' i
    have hconv : ∑ c, conjM Vm i c * (((conjM Vm)ᴴ * ρ' * conjM Vm) c c)
          * conj' (conjM Vm i c)
        = ∑ c, Vm i c * (((conjM Vm)ᴴ * ρ' * conjM Vm) c c) * conj' (Vm i c) := by
      refine Finset.sum_congr rfl fun c _ => ?_
      simp only [conjM_apply, Complex.conj_conj]
      ring
    rw [hconv] at h0
    rw [h0]
    exact hread' i
  have hd : (fun c => (Vmᴴ * ρ * Vm) c c)
      = fun c => ((conjM Vm)ᴴ * ρ' * conjM Vm) c c := by
    apply hB
    intro i
    rw [hro i, hro' i]
  -- the shared profile is passive for E and for −E, yet nonuniform: the squeeze closes
  have hpassR : ∀ x y : Fin m, -E x < -E y
      → ((Vmᴴ * ρ * Vm) y y).re ≤ ((Vmᴴ * ρ * Vm) x x).re := by
    intro x y hxy
    have u : (((conjM Vm)ᴴ * ρ' * conjM Vm) y y).re
        ≤ (((conjM Vm)ᴴ * ρ' * conjM Vm) x x).re := hpass' x y hxy
    have ex : ((Vmᴴ * ρ * Vm) x x).re = (((conjM Vm)ᴴ * ρ' * conjM Vm) x x).re :=
      congrArg Complex.re (congrFun hd x)
    have ey : ((Vmᴴ * ρ * Vm) y y).re = (((conjM Vm)ᴴ * ρ' * conjM Vm) y y).re :=
      congrArg Complex.re (congrFun hd y)
    linarith
  have hne : ((Vmᴴ * ρ * Vm) a₁ a₁).re ≠ ((Vmᴴ * ρ * Vm) b₁ b₁).re := hne₁
  have hab : a₁ ≠ b₁ := fun h => hne (by rw [h])
  rcases lt_or_gt_of_ne (hdist a₁ b₁ hab) with hlt | hgt
  · have u1 : ((Vmᴴ * ρ * Vm) b₁ b₁).re ≤ ((Vmᴴ * ρ * Vm) a₁ a₁).re := hpass a₁ b₁ hlt
    have u2 : ((Vmᴴ * ρ * Vm) a₁ a₁).re ≤ ((Vmᴴ * ρ * Vm) b₁ b₁).re :=
      hpassR b₁ a₁ (by linarith)
    exact hne (le_antisymm u2 u1)
  · have u1 : ((Vmᴴ * ρ * Vm) a₁ a₁).re ≤ ((Vmᴴ * ρ * Vm) b₁ b₁).re := hpass b₁ a₁ hgt
    have u2 : ((Vmᴴ * ρ * Vm) b₁ b₁).re ≤ ((Vmᴴ * ρ * Vm) a₁ a₁).re :=
      hpassR a₁ b₁ (by linarith)
    exact hne (le_antisymm u1 u2)

/-! ### Section C — the universal orientation no-go -/

/-- **`no_universal_oriented_property` — the boxed no-go.** If the admissible class is
closed under Θ and inhabited, no property with `P(R) ⟹ ¬P(ΘR)` on the class can hold
throughout it: bare transpose-symmetric coherent-completion conditions cannot force an
orientation. -/
theorem no_universal_oriented_property {α : Type*} (Θ : α → α) (C P : α → Prop)
    (hC : ∀ R, C R → C (Θ R)) (hP : ∀ R, C R → P R → ¬ P (Θ R))
    {R : α} (hR : C R) : ¬ ∀ R', C R' → P R' := by
  intro hforce
  exact hP R hR (hforce R hR) (hforce (Θ R) (hC R hR))

/-- **No transpose-symmetric condition forces the rate-route identification.** Any class
of Bohr-label assignments closed under the reflection `ω ↦ −ω + E₀` and inhabited cannot
uniformly satisfy a nondegenerate `OperationalTransitionIdentification`: OTI must come
from outside the transpose-symmetric conditions. -/
theorem no_symmetric_condition_forces_transitionIdentification
    {βE τK : ℝ} (hτ : 0 < τK) (ε : Fin m → ℝ) (E₀ : ℝ)
    (C : (Fin m → ℝ) → Prop) (hC : ∀ ω, C ω → C (fun a => -ω a + E₀))
    {ω₀ : Fin m → ℝ} (hω₀ : C ω₀) :
    ¬ ∀ ω, C ω →
      OperationalTransitionIdentification βE τK ε ω ∧ ∃ a b : Fin m, ω a ≠ ω b :=
  no_universal_oriented_property (fun ω a => -ω a + E₀) C _ hC
    (fun ω _ hP hPΘ => by
      obtain ⟨hOTI, a, b, hab⟩ := hP
      exact transitionIdentification_orientation_sensitive hτ hab hOTI hPΘ.1)
    hω₀

/-- **No transpose-symmetric condition forces the oriented shell condition.** Any class
of models `(V, E)` closed under the reflection `(V, E) ↦ (V̄, −E)`, inhabited, and
carrying the nondegeneracies (unitary model, distinct energies, separating readout)
cannot uniformly satisfy `OrientedShellRepresentation`: the state-side orientation must
also come from outside the transpose-symmetric conditions. -/
theorem no_symmetric_condition_forces_orientedShell (p : Fin m → ℝ)
    (C : Matrix (Fin m) (Fin m) ℂ × (Fin m → ℝ) → Prop)
    (hC : ∀ R, C R → C (conjM R.1, fun a => -R.2 a))
    (hreg : ∀ R, C R → R.1 * R.1ᴴ = 1
      ∧ (∀ a b : Fin m, a ≠ b → R.2 a ≠ R.2 b) ∧ ReadoutSeparating R.1)
    {R₀ : Matrix (Fin m) (Fin m) ℂ × (Fin m → ℝ)} (hR₀ : C R₀) :
    ¬ ∀ R, C R → OrientedShellRepresentation R.1 R.2 p :=
  no_universal_oriented_property
    (fun R : Matrix (Fin m) (Fin m) ℂ × (Fin m → ℝ) => (conjM R.1, fun a => -R.2 a)) C
    (fun R => OrientedShellRepresentation R.1 R.2 p) hC
    (fun R hR hP => orientedShellRepresentation_orientation_sensitive
      (hreg R hR).1 (hreg R hR).2.1 (hreg R hR).2.2 hP)
    hR₀

#print axioms conjM_conjM
#print axioms conjM_sandwich_transpose
#print axioms umat_reflect_conjM
#print axioms shellRepresentation_transpose_stable
#print axioms transitionIdentification_orientation_sensitive
#print axioms stationary_readout
#print axioms orientedShellRepresentation_orientation_sensitive
#print axioms no_universal_oriented_property
#print axioms no_symmetric_condition_forces_transitionIdentification
#print axioms no_symmetric_condition_forces_orientedShell

end OrientationClosure
end OIBridge
