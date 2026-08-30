/-
  OIBridge/ShellAssignment.lean — route (a): the correlated-shell assignment, its exact
  classical stationarity, and the named stopping point of the H-orientation transport.

  THE SETTING. The counting-selected physical state of GR §3.2 is the uniform ensemble on an
  invariant total-energy shell of the joint visible×hidden configuration space. Its hidden
  conditional μ_H(h|i) ∝ 𝟙[E_H(h) = E − e_i] depends on the visible configuration — a
  CORRELATED preparation — whereas the reconstructed channel of [Main] is built on a fixed
  product prior. This is exactly the classic correlated system–environment situation: once the
  environment assignment depends on the system state, a single reduced dynamics on the whole
  state space is not automatic; one needs an explicit ASSIGNMENT MAP, defined initially only on
  the compatible (here: classical diagonal) sector,

      𝒜_shell(|i⟩⟨i|) = |i⟩⟨i| ⊗ μ_H(·|i),

  and extensions off that domain need not be unique.

  WHAT IS PROVED HERE — the classical half of route (a), exact:
    * `shellWeight_invariant` / `joint_stationary` — uniform counting on a dynamics-invariant
      shell is invariant under the reversible joint dynamics, as an identity of weights.
    * `marginal_stationary` — the visible marginal of the evolved ensemble equals the marginal
      of the ensemble, under the ACTUAL correlated joint state: no product substitution, no
      approximation. Together with `counting_passive` (ThermalOrientation) the classical
      counting state is stationary and passive for the classical energies.
    * `shellConditional_sum` — the diagonal-sector assignment is a genuine conditional
      probability; probe F12 exhibits its i-dependence on an explicit shell, which is
      precisely what blocks substituting the fixed prior.

  THE STOPPING POINT — recorded, not assumed. Extending 𝒜_shell into the coherent
  reconstructed theory — producing a density operator ρ*, evolving by conjugation under the
  reconstructed U(t), stationary, whose energy-eigenbasis populations are the classical
  marginal — is the first step that REQUIRES A NEW ASSUMPTION. It is stated below as the
  named Prop `ShellRepresentationConsistency` and deliberately not axiomatized. The
  obligation it names is the coherent operational lift: representing the classically defined,
  i-dependent hidden assignment inside the coherent instrument algebra whose "unique
  selection" [Main] leaves open. GR §3.2's RATE route stops at the same wall from the other
  side: transporting the classically oriented transition rate to the frequency-resolved
  detector transition needs "the ancilla-carrying Q_fb form together with a detector gap, an
  interaction and an identification of excitation and de-excitation channels — exactly the
  structures the composite and coherent instrument lift leaves open." Both routes therefore
  converge on one obligation: whether the classical energy-oriented structure and the coherent
  quantum representation are the SAME operational structure, not merely two representations
  reproducing selected probabilities. The antiunitary-orientation problem is, on this
  evidence, not an independent gap but another face of the single remaining coherent
  operational completion problem in OI → QM.
-/
import OIBridge.BohrFrequency
import Mathlib.Algebra.BigOperators.Field

namespace OIBridge
namespace ShellAssignment

open Matrix

variable {V H : Type*} [Fintype V] [Fintype H] [DecidableEq V] [DecidableEq H]

/-- Uniform counting weight on a shell. -/
def shellWeight (shell : Finset (V × H)) (x : V × H) : ℚ :=
  if x ∈ shell then 1 / shell.card else 0

omit [Fintype V] [Fintype H] in
/-- Invariance of the shell transports membership through the dynamics. -/
theorem shellWeight_invariant (φ : (V × H) ≃ (V × H)) (shell : Finset (V × H))
    (hshell : shell.image φ = shell) (x : V × H) :
    shellWeight shell (φ x) = shellWeight shell x := by
  have hmem : φ x ∈ shell ↔ x ∈ shell := by
    constructor
    · intro h
      rw [← hshell] at h
      obtain ⟨y, _, hxy⟩ := Finset.mem_image.mp h
      rename_i hy
      rwa [← φ.injective hxy]
    · intro h
      rw [← hshell]
      exact Finset.mem_image_of_mem _ h
  rw [shellWeight, shellWeight]
  by_cases h : x ∈ shell
  · rw [if_pos (hmem.mpr h), if_pos h]
  · rw [if_neg (fun h' => h (hmem.mp h')), if_neg h]

omit [Fintype V] [Fintype H] in
/-- **JOINT STATIONARITY, exact.** The uniform shell ensemble is invariant under the
reversible joint dynamics: the evolved weight IS the weight. -/
theorem joint_stationary (φ : (V × H) ≃ (V × H)) (shell : Finset (V × H))
    (hshell : shell.image φ = shell) :
    (fun x => shellWeight shell (φ.symm x)) = shellWeight shell := by
  funext x
  rw [← shellWeight_invariant φ shell hshell (φ.symm x), Equiv.apply_symm_apply]

/-- The visible marginal of the shell ensemble. -/
def marginal (shell : Finset (V × H)) (i : V) : ℚ :=
  ∑ h : H, shellWeight shell (i, h)

omit [Fintype V] in
/-- **MARGINAL STATIONARITY, exact.** The visible marginal of the evolved ensemble equals the
marginal of the ensemble — computed on the ACTUAL correlated joint state, with no product
substitution and no approximation. The classical half of route (a) closes here. -/
theorem marginal_stationary (φ : (V × H) ≃ (V × H)) (shell : Finset (V × H))
    (hshell : shell.image φ = shell) (i : V) :
    (∑ h : H, shellWeight shell (φ.symm (i, h))) = marginal shell i := by
  rw [marginal]
  exact Finset.sum_congr rfl fun h _ => congrFun (joint_stationary φ shell hshell) (i, h)

/-- The correlated hidden assignment `μ_H(h|i)` — the diagonal-sector assignment map. Its
`i`-dependence (probe F12 exhibits it) is exactly what blocks substituting the fixed product
prior of the reconstructed channel. -/
def shellConditional (shell : Finset (V × H)) (i : V) (h : H) : ℚ :=
  shellWeight shell (i, h) / marginal shell i

omit [Fintype V] in
/-- On visible configurations the shell reaches, the assignment is a genuine conditional
probability. -/
theorem shellConditional_sum (shell : Finset (V × H)) (i : V)
    (hpos : marginal shell i ≠ 0) :
    ∑ h : H, shellConditional shell i h = 1 := by
  rw [show (∑ h : H, shellConditional shell i h)
    = (∑ h : H, shellWeight shell (i, h)) / marginal shell i from
      (Finset.sum_congr rfl fun h _ => rfl).trans (Finset.sum_div _ _ _).symm]
  rw [← marginal, div_self hpos]

/-- **THE STOPPING POINT — the named open target of route (a), stated and not assumed.**
The correlated shell preparation is represented inside the coherent reconstructed theory:
there is a density operator, evolving by conjugation under the reconstructed propagator,
stationary at every time, whose energy-eigenbasis populations are the classical marginal
profile. Everything after this Prop is already kernel-proved (`stationary_spectral_form`
turns it into spectral populations; the selectors of ThermalOrientation operate on them).
Everything before it is proved above, classically and exactly. Proving THIS Prop from the
substratum is the coherent-lift obligation both transport routes converge on. -/
def ShellRepresentationConsistency {m : ℕ} (Vm : Matrix (Fin m) (Fin m) ℂ)
    (E : Fin m → ℝ) (p : Fin m → ℝ) : Prop :=
  ∃ ρ : Matrix (Fin m) (Fin m) ℂ,
    (∀ t : ℝ, Matrix.of (BohrFrequency.Umat Vm E t) * ρ
      * (Matrix.of (BohrFrequency.Umat Vm E t))ᴴ = ρ)
    ∧ ∀ a, (Vmᴴ * ρ * Vm) a a = ((p a : ℝ) : ℂ)

#print axioms shellWeight_invariant
#print axioms joint_stationary
#print axioms marginal_stationary
#print axioms shellConditional_sum

end ShellAssignment
end OIBridge
