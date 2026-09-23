import OIBridge.PhaseSource

/-!
# The Q3 round — phase-free richness from the closure and one executable layer flow

The preregistered pass of `DERIVED-Q3-AUDIT.md`: the lift audit's Q3 at its own hypothesis, with
`PhasesAvailable` an explicit extra hypothesis of the closure `DerivedOI` and not a consequence of
the stated substratum.

* **T1, the sign-flip identity** (`gateFlow_isolation_flip`): for an involution `τ`, a moved
  configuration `a` with `b = τ a`, and `D` the diagonal with `−1` at `b`,
  `gateFlow τ t · (D · gateFlow τ (−t) · D) = flow (transition a b) (π t)`. Time reversal replaces
  the continuous phase of the lift audit's isolation identity: on the chosen pair the sign
  conjugation reverses the rotation of the time-reversed flow and leaves its scalar, so the two
  rotations add and the scalars cancel; on every other moved pair the flow meets its inverse; on
  the fixed configurations nothing moves.
* **T2, the diagonal from the quarter phases** (`phaseGate_mul_self`, `flip_avail`): `D` is the
  square of the quarter phase on `b`, available at every level under `PhasesAvailable`. This is
  the step at which the phase hypothesis is consumed.
* **T3, Q3** (`phaseFree_of_phases_layerFlowExecutable`,
  `phaseFree_of_derivedOI_layerFlowExecutable`): from the phases, the exchanges, an involution
  with a moved configuration and the executability of its layer flow, phase-free richness; from
  `DerivedOI` the same.
* **T4, the endpoint** (`derivedOI_qm_iff_layerFlowExecutable'`, `qm_of_derivedOI_layerFlowExecutable`,
  the swap-layer instances): under `DerivedOI` alone, exact finite endomorphic operational quantum
  mechanics is exactly the executability of one layer flow of an involution with a moved
  configuration.
* **T5, the countercontrols**: the moved-configuration hypothesis is necessary, the gate flow of
  the identity being the identity at every time, so the substratum theory on two states satisfies
  `DerivedOI`, executes the identity's layer flow and fails phase-free richness
  (`derivedOI_layerFlowExecutable_one_not_phaseFree`); quantum mechanics satisfies both
  hypotheses (`derivedOI_layerFlowExecutable_of_qm`). The necessity of the phase hypothesis is the
  flow-endpoint theorem `flow_endpoint_refuted`, cited and not re-proved.

Not claimed: that `PhasesAvailable` is derivable from the stated substratum, which the
phase-source audit decided negatively; that relative phase or the layer flow is the unique or
minimal resource; anything about the observer-level lift, Route A or a manuscript.
-/

namespace OIBridge
namespace DerivedQ3

open Complex Matrix CoherentLift SpectatorBridge OperationalAssembly AncillaClosure
open MonoidalCompletion InterventionLocality MicroReversibility PrimitiveSource LieRankSource
open DiagonalTheory SubstratumInterface StructuralClosure MinimalRepertoire LevelOneSeam
open PhysicalCharacterization RouteB LiftAudit

/-! ### Section A — T1: the sign-flip identity -/

section Flip

variable {S : Type} [Fintype S] [DecidableEq S]

/-- The sign flip at one configuration: `−1` there, `1` elsewhere. -/
def flipAt (b z : S) : ℂ := if z = b then -1 else 1

omit [Fintype S] in
theorem flipAt_self (b : S) : flipAt b b = -1 := by
  unfold flipAt; rw [if_pos rfl]

omit [Fintype S] in
theorem flipAt_of_ne {b z : S} (h : z ≠ b) : flipAt b z = 1 := by
  unfold flipAt; rw [if_neg h]

/-- **T2 — THE SQUARE OF THE QUARTER PHASE IS THE SIGN FLIP.** -/
theorem phaseGate_mul_self (b : S) : phaseGate b * phaseGate b = Matrix.diagonal (flipAt b) := by
  rw [phaseGate, Matrix.diagonal_mul_diagonal]
  congr 1
  funext z
  unfold flipAt
  by_cases h : b = z
  · rw [if_pos h, if_pos h.symm]
    exact Complex.I_mul_I
  · rw [if_neg h, if_neg (Ne.symm h), mul_one]

/-- **T1 — THE SIGN-FLIP IDENTITY.** The gate flow, times the time-reversed gate flow conjugated
by the sign flip at the image of the chosen configuration, is the transition flow on the chosen
pair at angle `π t`: on that pair the sign reverses the rotation of the reversed flow and leaves
its scalar, so the rotations add and the scalars cancel; on every other moved pair the flow meets
its inverse; on the fixed configurations nothing moves. No continuous phase enters. -/
theorem gateFlow_isolation_flip {τ : Equiv.Perm S} (hτ : ∀ z, τ (τ z) = z) {a : S} (ha : τ a ≠ a)
    (t : ℝ) :
    gateFlow τ t * (Matrix.diagonal (flipAt (τ a)) * gateFlow τ (-t) * Matrix.diagonal (flipAt (τ a)))
      = ReachabilitySeam.flow (transition a (τ a)) (Real.pi * t) := by
  rw [gateFlow_eq_orb τ t, gateFlow_eq_orb τ (-t), diagonal_mul_orb_mul_diagonal, orb_mul τ hτ,
    flow_transition_eq_orb τ ha hτ]
  set e₁ := Complex.exp ((Real.pi : ℂ) * Complex.I * (t : ℂ)) with he₁
  set e₂ := Complex.exp ((Real.pi : ℂ) * Complex.I * ((-t : ℝ) : ℂ)) with he₂
  have he : e₁ * e₂ = 1 := by
    rw [he₁, he₂, ← Complex.exp_add]
    rw [show (Real.pi : ℂ) * Complex.I * (t : ℂ) + (Real.pi : ℂ) * Complex.I * ((-t : ℝ) : ℂ) = 0 by
      push_cast; ring, Complex.exp_zero]
  have h1 : e₁ = (Real.cos (Real.pi * t) : ℂ) + (Real.sin (Real.pi * t) : ℂ) * Complex.I := by
    rw [he₁, show (Real.pi : ℂ) * Complex.I * (t : ℂ) = ((Real.pi * t : ℝ) : ℂ) * Complex.I by
      push_cast; ring, Complex.exp_mul_I, ← Complex.ofReal_cos, ← Complex.ofReal_sin]
  have h2 : e₂ = (Real.cos (Real.pi * t) : ℂ) - (Real.sin (Real.pi * t) : ℂ) * Complex.I := by
    rw [he₂, show (Real.pi : ℂ) * Complex.I * ((-t : ℝ) : ℂ) = ((-(Real.pi * t) : ℝ) : ℂ) * Complex.I by
      push_cast; ring, Complex.exp_mul_I, ← Complex.ofReal_cos, ← Complex.ofReal_sin, Real.cos_neg,
      Real.sin_neg]
    push_cast
    ring
  have hcos : (Real.cos (Real.pi * t) : ℂ) = (e₁ + e₂) * (2 : ℂ)⁻¹ := by rw [h1, h2]; ring
  have hsin : (Real.sin (Real.pi * t) : ℂ) * Complex.I = (e₁ - e₂) * (2 : ℂ)⁻¹ := by
    rw [h1, h2]; ring
  have hab : a ≠ τ a := Ne.symm ha
  refine orb_ext τ (fun z => ?_) (fun z hz => ?_)
  · -- the diagonal coefficient
    by_cases hz : τ z = z
    · have hza : z ≠ a := fun h => ha (by rw [← h]; exact hz)
      have hzb : z ≠ τ a := fun h => ha ((hτ a).symm.trans (by rw [← h]; exact hz)).symm
      have hc : ¬ (z = a ∨ z = τ a) := fun h => h.elim hza hzb
      have hd : flipAt (τ a) z = 1 := flipAt_of_ne hzb
      simp only [hz, hc, hd, if_true, if_false, ne_eq, not_true_eq_false, mul_one, one_mul, add_zero]
    · have hz' : ¬ τ z = z := hz
      by_cases hza : z = a
      · have hd1 : flipAt (τ a) z = 1 := by rw [hza]; exact flipAt_of_ne hab
        have hd2 : flipAt (τ a) (τ z) = -1 := by rw [hza]; exact flipAt_self _
        have hc : z = a ∨ z = τ a := Or.inl hza
        simp only [hd1, hd2]
        rw [if_neg hz', if_neg hz', if_pos hz', if_pos hc, hcos]
        ring
      · by_cases hzb : z = τ a
        · have hd1 : flipAt (τ a) z = -1 := by rw [hzb]; exact flipAt_self _
          have hd2 : flipAt (τ a) (τ z) = 1 := by rw [hzb, hτ]; exact flipAt_of_ne hab
          have hc : z = a ∨ z = τ a := Or.inr hzb
          simp only [hd1, hd2]
          rw [if_neg hz', if_neg hz', if_pos hz', if_pos hc, hcos]
          ring
        · have hc : ¬ (z = a ∨ z = τ a) := fun h => h.elim hza hzb
          have hd1 : flipAt (τ a) z = 1 := flipAt_of_ne hzb
          have hd2 : flipAt (τ a) (τ z) = 1 :=
            flipAt_of_ne (fun h => hza (by rw [← hτ z, h, hτ]))
          simp only [hd1, hd2]
          rw [if_neg hz', if_neg hz', if_pos hz', if_neg hc]
          linear_combination ((2 : ℂ)⁻¹) * he
  · -- the antidiagonal coefficient, on a moved configuration
    have hz' : ¬ τ z = z := hz
    have hz2 : ¬ z = τ z := fun h => hz h.symm
    by_cases hza : z = a
    · have hd1 : flipAt (τ a) z = 1 := by rw [hza]; exact flipAt_of_ne hab
      have hd2 : flipAt (τ a) (τ z) = -1 := by rw [hza]; exact flipAt_self _
      have hc : z = a ∨ z = τ a := Or.inl hza
      simp only [hd1, hd2, hτ]
      rw [if_neg hz', if_neg hz2, if_pos hc, hsin]
      ring
    · by_cases hzb : z = τ a
      · have hd1 : flipAt (τ a) z = -1 := by rw [hzb]; exact flipAt_self _
        have hd2 : flipAt (τ a) (τ z) = 1 := by rw [hzb, hτ]; exact flipAt_of_ne hab
        have hc : z = a ∨ z = τ a := Or.inr hzb
        simp only [hd1, hd2, hτ]
        rw [if_neg hz', if_neg hz2, if_pos hc, hsin]
        ring
      · have hc : ¬ (z = a ∨ z = τ a) := fun h => h.elim hza hzb
        have hd1 : flipAt (τ a) z = 1 := flipAt_of_ne hzb
        have hd2 : flipAt (τ a) (τ z) = 1 :=
          flipAt_of_ne (fun h => hza (by rw [← hτ z, h, hτ]))
        simp only [hd1, hd2, hτ]
        rw [if_neg hz', if_neg hz2, if_neg hc]
        linear_combination (-(2 : ℂ)⁻¹) * he

end Flip

/-! ### Section B — T2, T3, T4: availability, Q3 and the endpoint -/

section Bridge

variable {S : Type} [Fintype S] [DecidableEq S]

/-- **T2 — THE SIGN FLIP IS AVAILABLE** at every level under the phases: it is the composition
of the quarter phase with itself. -/
theorem flip_avail (T : FiniteOperationalTheory S) (hph : PhasesAvailable T) (n : ℕ)
    (b : S × Fin n) : T.availExt n Unit (fun _ => conjChannel (Matrix.diagonal (flipAt b))) := by
  rw [← phaseGate_mul_self]
  exact avail_conj_mul T n (hph n b) (hph n b)

/-- **T3 — Q3, FROM THE PHASES AND THE EXCHANGES.** In a theory with the quarter phases and the
exchanges at every level, executability of the layer flow of an involution with a moved
configuration supplies, at every level, the transition flow between a moved configuration and its
image at every angle: the sign-flip identity writes that flow as a product of the gate flow, the
sign flip, the time-reversed gate flow and the sign flip, each available. -/
theorem phaseFree_of_phases_layerFlowExecutable (T : FiniteOperationalTheory S)
    (hph : PhasesAvailable T) (hexch : ExchangesAvailable T) {σ : Equiv.Perm S}
    (hσ : ∀ x, σ (σ x) = x) {x : S} (hx : σ x ≠ x) (hex : LayerFlowExecutable T σ) :
    PhaseFreeRichness T := by
  intro n hn
  have hn0 : 0 < n := by
    rcases Nat.eq_zero_or_pos n with h | h
    · subst h
      simp at hn
    · exact h
  set τ := levelPerm σ n with hτdef
  have hτ : ∀ p, τ (τ p) = p := levelPerm_involutive hσ n
  have ha : τ (x, ⟨0, hn0⟩) ≠ (x, ⟨0, hn0⟩) := by
    rw [hτdef, levelPerm_apply]
    intro h
    exact hx (Prod.mk.inj h).1
  refine ⟨⟨(x, ⟨0, hn0⟩), τ (x, ⟨0, hn0⟩), ha.symm, fun t => ?_⟩, fun a b _ => hexch n a b⟩
  have hπ : Real.pi * (t / Real.pi) = t := mul_div_cancel₀ _ Real.pi_ne_zero
  rw [← hπ, ← gateFlow_isolation_flip hτ ha (t / Real.pi)]
  have hD := flip_avail T hph n (τ (x, ⟨0, hn0⟩))
  exact avail_conj_mul T n (hex n (t / Real.pi))
    (avail_conj_mul T n (avail_conj_mul T n hD (hex n (-(t / Real.pi)))) hD)

/-- **T3 — Q3, AS PREREGISTERED**: from `DerivedOI` and the executability of one layer flow of an
involution with a moved configuration, phase-free richness. The closure supplies the phases and
the exchanges; nothing else of it is used. -/
theorem phaseFree_of_derivedOI_layerFlowExecutable (T : FiniteOperationalTheory S)
    (hd : DerivedOI T) {σ : Equiv.Perm S} (hσ : ∀ x, σ (σ x) = x) {x : S} (hx : σ x ≠ x)
    (hex : LayerFlowExecutable T σ) : PhaseFreeRichness T :=
  phaseFree_of_phases_layerFlowExecutable T hd.2.2.2.1 hd.2.2.1 hσ hx hex

/-- **T4 — THE ENDPOINT, ONE WAY**: under the closure, one executable layer flow gives exact
finite endomorphic operational quantum mechanics. -/
theorem qm_of_derivedOI_layerFlowExecutable [Nonempty S] (T : FiniteOperationalTheory S)
    (hd : DerivedOI T) {σ : Equiv.Perm S} (hσ : ∀ x, σ (σ x) = x) {x : S} (hx : σ x ≠ x)
    (hex : LayerFlowExecutable T σ) : ExactAllFiniteEndomorphicQuantumOps T :=
  (derivedOI_qm_iff_phaseFree hd).mpr (phaseFree_of_derivedOI_layerFlowExecutable T hd hσ hx hex)

/-- **T4 — THE ENDPOINT, UNDER THE CLOSURE ALONE**: the lift audit's preregistered Q4 at its own
hypothesis. Under `DerivedOI`, exact finite endomorphic operational quantum mechanics is exactly
the executability of one layer flow of an involution with a moved configuration. -/
theorem derivedOI_qm_iff_layerFlowExecutable' [Nonempty S] (T : FiniteOperationalTheory S)
    (hd : DerivedOI T) {σ : Equiv.Perm S} (hσ : ∀ x, σ (σ x) = x) {x : S} (hx : σ x ≠ x) :
    ExactAllFiniteEndomorphicQuantumOps T ↔ LayerFlowExecutable T σ :=
  ⟨fun hqm => layerFlowExecutable_of_control T (physical_of_exactAll T hqm).2.2.1 hσ,
    fun hex => qm_of_derivedOI_layerFlowExecutable T hd hσ hx hex⟩

/-- **C4 — CONSISTENCY**: quantum mechanics satisfies both hypotheses. -/
theorem derivedOI_layerFlowExecutable_of_qm [Nonempty S] (T : FiniteOperationalTheory S)
    (h : ExactAllFiniteEndomorphicQuantumOps T) {σ : Equiv.Perm S} (hσ : ∀ x, σ (σ x) = x) :
    DerivedOI T ∧ LayerFlowExecutable T σ :=
  ⟨derivedOI_of_qm T h, layerFlowExecutable_of_control T (physical_of_exactAll T h).2.2.1 hσ⟩

end Bridge

/-! ### Section C — the swap layer of the second-order form, on a region -/

section SwapLayer

open OIBridge.SecondOrderDrive OIBridge.RegionTower

variable {ι : Type} [DecidableEq ι] {V : Type} [Fintype V] [DecidableEq V] [Nonempty V]
  [AddCommGroup V]

/-- **Q3 FOR THE SWAP LAYER**, under the closure alone. -/
theorem phaseFree_of_derivedOI_layerFlowExecutable_swap (Λ : Finset ι) (hΛ : Λ.Nonempty)
    [Nontrivial V] (T : FiniteOperationalTheory (Conf Λ (V × V))) (hd : DerivedOI T)
    (hex : LayerFlowExecutable T (regionSwap V Λ)) : PhaseFreeRichness T := by
  obtain ⟨f, hf⟩ := regionSwap_moves Λ hΛ (V := V)
  exact phaseFree_of_derivedOI_layerFlowExecutable T hd (regionSwap_involutive' Λ) hf hex

/-- **THE ENDPOINT FOR THE SWAP LAYER**, under the closure alone. -/
theorem derivedOI_qm_iff_layerFlowExecutable_swap' (Λ : Finset ι) (hΛ : Λ.Nonempty) [Nontrivial V]
    (T : FiniteOperationalTheory (Conf Λ (V × V))) (hd : DerivedOI T) :
    ExactAllFiniteEndomorphicQuantumOps T ↔ LayerFlowExecutable T (regionSwap V Λ) := by
  obtain ⟨f, hf⟩ := regionSwap_moves Λ hΛ (V := V)
  exact derivedOI_qm_iff_layerFlowExecutable' T hd (regionSwap_involutive' Λ) hf

end SwapLayer

/-! ### Section D — C2: the moved-configuration hypothesis is necessary -/

section Identity

variable {S : Type} [Fintype S] [DecidableEq S]

/-- The gate flow of the identity is the identity at every time. -/
theorem gateFlow_one_eq_one (t : ℝ) : gateFlow (1 : Equiv.Perm S) t = 1 := by
  rw [gateFlow_eq_orb, one_eq_orb (1 : Equiv.Perm S)]
  refine orb_ext _ (fun z => ?_) (fun z hz => absurd rfl hz)
  simp

omit [Fintype S] [DecidableEq S] in
theorem levelPerm_one (n : ℕ) : levelPerm (1 : Equiv.Perm S) n = 1 :=
  Equiv.ext fun _ => rfl

/-- The identity's layer flow is executable wherever the identity operation is available. -/
theorem layerFlowExecutable_one (T : FiniteOperationalTheory S)
    (h1 : ∀ n, T.availExt n Unit (fun _ => conjChannel (1 : Matrix (S × Fin n) (S × Fin n) ℂ))) :
    LayerFlowExecutable T 1 := by
  intro n t
  rw [levelPerm_one, gateFlow_one_eq_one]
  exact h1 n

/-- The substratum theory executes the identity's layer flow. -/
theorem substratumTheory_layerFlowExecutable_one : LayerFlowExecutable (substratumTheory S) 1 := by
  refine layerFlowExecutable_one _ fun n => ?_
  have h := substratumTheory_avail_conj (A := S) (n := n) (monomial_diagonal fun _ => (1 : ℂ))
    (by rw [Matrix.diagonal_one, Matrix.conjTranspose_one, Matrix.one_mul])
  rwa [Matrix.diagonal_one] at h

/-- **C2 — THE MOVED-CONFIGURATION HYPOTHESIS IS NECESSARY**: a theory satisfying `DerivedOI`,
executing the layer flow of the identity, and failing phase-free richness. -/
theorem derivedOI_layerFlowExecutable_one_not_phaseFree :
    ∃ T : FiniteOperationalTheory (Fin 2),
      DerivedOI T ∧ LayerFlowExecutable T 1 ∧ ¬ PhaseFreeRichness T :=
  ⟨substratumTheory (Fin 2), substratumTheory_derivedOI, substratumTheory_layerFlowExecutable_one,
    substratumTheory_not_phaseFree⟩

end Identity

#print axioms flipAt_self
#print axioms flipAt_of_ne
#print axioms phaseGate_mul_self
#print axioms gateFlow_isolation_flip
#print axioms flip_avail
#print axioms phaseFree_of_phases_layerFlowExecutable
#print axioms phaseFree_of_derivedOI_layerFlowExecutable
#print axioms qm_of_derivedOI_layerFlowExecutable
#print axioms derivedOI_qm_iff_layerFlowExecutable'
#print axioms derivedOI_layerFlowExecutable_of_qm
#print axioms phaseFree_of_derivedOI_layerFlowExecutable_swap
#print axioms derivedOI_qm_iff_layerFlowExecutable_swap'
#print axioms gateFlow_one_eq_one
#print axioms levelPerm_one
#print axioms layerFlowExecutable_one
#print axioms substratumTheory_layerFlowExecutable_one
#print axioms derivedOI_layerFlowExecutable_one_not_phaseFree

end DerivedQ3
end OIBridge
