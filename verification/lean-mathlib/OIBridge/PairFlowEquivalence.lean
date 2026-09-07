import OIBridge.RealPairFlow

/-!
# The operational pair-flow equivalence audit — quantum mechanics is exactly the closure with one sourced pair flow

The preregistered pass of `PAIR-FLOW-EQUIVALENCE-AUDIT.md`, read under its scope amendment.
Nothing here is named "C5"; nothing here generalizes beyond the two-valued carrier; nothing here
sources the pair flow from any realization-level structure.

* T1, the predicate: `PairFlowSourced T` says that some real pair flow has the conjugation channel
  of its transport available in `T` at every level and time, the theory-level analogue of
  `LayerFlowExecutable`, stated on availability and not on class membership.
* T2, the canonical flow: the rate-one real rotation is a pair flow (`rotFlow`), its matrix at
  time `t` the rotation `rotR t` (`rotFlow_A`).
* T3, the forward direction: exact finite operational quantum mechanics has the closure and a
  sourced pair flow (`pairFlowSourced_of_qm`, `derivedOI_pairFlowSourced_of_qm`), through composite
  unitary control and the unitarity of the transported rotation; canonical, not new physics.
* T4, the backward direction, at the theory level: the datum's conjugation is available at every
  angle (`mixAvail_of_pairFlowSourced`); the identity is available at every level from the flow at
  time zero (`identity_avail_of_pairFlowSourced`); the products of the phases over any finite set
  and the site shear are available (`phaseIndicator_avail`, `siteShear_avail`); the lifted site
  exchange's layer flow is executable (`layerFlowExecutable_of_derivedOI_pairFlowSourced`); and the
  existing Q3 gives quantum mechanics (`qm_of_derivedOI_pairFlowSourced`).
* T5, the central theorem: `qm_iff_derivedOI_pairFlowSourced`.
* T6, the countercontrols: the polarization closure satisfies the closure and is not sourced
  (`polarizedTheoryC_not_pairFlowSourced`); a theory whose available unit conjugations at level one
  are countable up to scalar is not sourced (`countable_not_pairFlowSourced`), a necessary
  condition and nothing more.
-/

namespace OIBridge
namespace PairFlowEquivalence

open Complex Matrix CoherentLift SpectatorBridge OperationalAssembly AncillaClosure
open MonoidalCompletion InterventionLocality MicroReversibility PrimitiveSource LieRankSource
open DiagonalTheory SubstratumInterface StructuralClosure MinimalRepertoire LevelOneSeam
open PhysicalCharacterization RouteB ManuscriptAxioms LiftAudit SubstratumInterfaceAudit
open InstrumentRealization SecondOrderCircuit ExecSource FlowEndpoint DerivedQ3 C5Discovery
open PolarizationClosure CoherentContinuumSource StateMixingCoupling RealPairFlow Set

/-! ### Section A — T1, T2: the predicate and the canonical flow -/

section Predicate

/-- **THE PREDICATE**: some real pair flow has the conjugation channel of its transport available
in the theory at every level and time. It asserts availability in the theory, not membership of
the matrices in an implementation class. -/
def PairFlowSourced (T : FiniteOperationalTheory (Fin 2)) : Prop :=
  ∃ F : PairFlow, ∀ (n : ℕ) (t : ℝ),
    T.availExt n Unit (fun _ => conjChannel (transport n (F.A t)))

theorem rotR_orth (θ : ℝ) : (rotR θ)ᵀ * rotR θ = 1 := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [rotR, Matrix.mul_apply, Fin.sum_univ_two] <;> linarith [Real.cos_sq_add_sin_sq θ]

theorem rotR_continuous : Continuous rotR := by
  refine continuous_matrix fun i j => ?_
  fin_cases i <;> fin_cases j <;> simp [rotR] <;> fun_prop

theorem rotR_pi_ne_one : rotR Real.pi ≠ 1 := by
  intro h
  have := congrFun (congrFun h 0) 0
  norm_num [rotR, Real.cos_pi] at this

/-- **THE CANONICAL FLOW**: the rate-one real rotation, a pair flow. -/
noncomputable def rotFlow : PairFlow where
  A := rotR
  zero := rotR_zero
  add := fun s t => (rotR_mul s t).symm
  cont := rotR_continuous
  orth := rotR_orth
  nontrivial := ⟨Real.pi, rotR_pi_ne_one⟩

theorem rotFlow_A (t : ℝ) : rotFlow.A t = rotR t := rfl

end Predicate

/-! ### Section B — T3: the forward direction, canonical -/

section Forward

/-- **QUANTUM MECHANICS HAS A SOURCED PAIR FLOW**: the canonical rotation's transport is the
datum, unitary, so composite unitary control makes its conjugation available at every level. -/
theorem pairFlowSourced_of_qm (T : FiniteOperationalTheory (Fin 2))
    (h : ExactAllFiniteEndomorphicQuantumOps T) : PairFlowSourced T := by
  have hctrl : HasCompositeUnitaryControl T := (physical_of_exactAll T h).2.2.1
  refine ⟨rotFlow, fun n t => ?_⟩
  rw [rotFlow_A, transport_rotR]
  exact hctrl n _ (mixImage_unitary n t)

/-- **QUANTUM MECHANICS HAS THE CLOSURE AND A SOURCED PAIR FLOW.** -/
theorem derivedOI_pairFlowSourced_of_qm (T : FiniteOperationalTheory (Fin 2))
    (h : ExactAllFiniteEndomorphicQuantumOps T) : DerivedOI T ∧ PairFlowSourced T :=
  ⟨derivedOI_of_qm T h, pairFlowSourced_of_qm T h⟩

end Forward

/-! ### Section C — T4, T5: the backward direction at the theory level, and the theorem -/

section Backward

variable {T : FiniteOperationalTheory (Fin 2)}

/-- **THE DATUM'S CONJUGATION IS AVAILABLE** at every level and angle: the reduction audit's
supply gives a time whose transport is the datum. -/
theorem mixAvail_of_pairFlowSourced (hs : PairFlowSourced T) (n : ℕ) (θ : ℝ) :
    T.availExt n Unit (fun _ => conjChannel (mixImage n θ)) := by
  obtain ⟨F, hF⟩ := hs
  obtain ⟨t, ht⟩ := F.pairFlow_supplies_mixImage n θ
  rw [← ht]
  exact hF n t

/-- **THE IDENTITY IS AVAILABLE AT EVERY LEVEL**, from the sourced flow at time zero: the flow's
identity field and the transport of the identity matrix. -/
theorem identity_avail_of_pairFlowSourced (hs : PairFlowSourced T) (n : ℕ) :
    T.availExt n Unit (fun _ => conjChannel (1 : Matrix (Fin 2 × Fin n) (Fin 2 × Fin n) ℂ)) := by
  obtain ⟨F, hF⟩ := hs
  have h1 : transport n (1 : Matrix (Fin 2) (Fin 2) ℝ) = 1 := constFlow_transport n 0
  have := hF n 0
  rwa [F.zero, h1] at this

/-- **THE PRODUCT OF THE PHASES OVER ANY FINITE SET OF CONFIGURATIONS IS AVAILABLE**, by finite
composition from the phases, the base case the identity supplied by the sourced flow. -/
theorem phaseIndicator_avail (hph : PhasesAvailable T) (hs : PairFlowSourced T) (n : ℕ)
    (s : Finset (Fin 2 × Fin n)) :
    T.availExt n Unit (fun _ =>
      conjChannel (Matrix.diagonal fun p => if p ∈ s then Complex.I else 1)) := by
  induction s using Finset.induction_on with
  | empty =>
    have : (Matrix.diagonal fun p : Fin 2 × Fin n =>
        if p ∈ (∅ : Finset (Fin 2 × Fin n)) then Complex.I else 1) = 1 := by
      ext i j
      by_cases h : i = j
      · subst h; simp
      · simp [Matrix.diagonal_apply_ne _ h, Matrix.one_apply_ne h]
    rw [this]
    exact identity_avail_of_pairFlowSourced hs n
  | insert a s ha ih =>
    have : (Matrix.diagonal fun p : Fin 2 × Fin n => if p ∈ insert a s then Complex.I else 1)
        = phaseGate a * Matrix.diagonal fun p => if p ∈ s then Complex.I else 1 := by
      rw [phaseGate, Matrix.diagonal_mul_diagonal]
      congr 1
      funext p
      by_cases hp : p = a
      · subst hp; simp [ha]
      · simp [hp, Ne.symm hp]
    rw [this]
    exact avail_conj_mul T n (hph n a) ih

/-- **THE SITE SHEAR IS AVAILABLE**: the product of the phases over the configurations with site
value one. -/
theorem siteShear_avail (hph : PhasesAvailable T) (hs : PairFlowSourced T) (n : ℕ) :
    T.availExt n Unit (fun _ => conjChannel (siteShearImage n)) := by
  have := phaseIndicator_avail hph hs n (Finset.univ.filter fun p : Fin 2 × Fin n => p.1 = 1)
  have heq : siteShearImage n
      = Matrix.diagonal fun p : Fin 2 × Fin n =>
          if p ∈ (Finset.univ.filter fun p : Fin 2 × Fin n => p.1 = 1) then Complex.I else 1 := by
    rw [siteShearImage]; congr 1; funext p; simp
  rw [heq]
  exact this

/-- A unit scalar does not change a conjugation channel. -/
theorem conjChannel_unit_smul {l : Type} [Fintype l] [DecidableEq l] {a : ℂ} (ha : ‖a‖ = 1)
    (V : Matrix l l ℂ) : conjChannel (a • V) = conjChannel V := by
  refine LinearMap.ext fun X => ?_
  show a • V * X * (a • V)ᴴ = V * X * Vᴴ
  have h1 : star a * a = 1 := by
    rw [Complex.star_def, mul_comm, Complex.mul_conj, Complex.normSq_eq_norm_sq, ha]
    norm_num
  rw [Matrix.conjTranspose_smul, Matrix.smul_mul, Matrix.mul_smul, Matrix.smul_mul, smul_smul, h1,
    one_smul]

/-- **THE LAYER FLOW OF THE SITE EXCHANGE IS EXECUTABLE** under the closure with a sourced pair
flow: the construction audit's identity writes it as a unit scalar times the site shear, the datum
and the adjoint site shear, each conjugation available and their product available. -/
theorem layerFlowExecutable_of_derivedOI_pairFlowSourced (hd : DerivedOI T)
    (hs : PairFlowSourced T) : LayerFlowExecutable T (Equiv.swap 0 1) := by
  intro n t
  have hph : PhasesAvailable T := hd.2.2.2.1
  have hS := siteShear_avail hph hs n
  have hS' : T.availExt n Unit (fun _ => conjChannel (siteShearImage n)ᴴ) := by
    rw [siteShearImage_conjTranspose]
    exact avail_conj_mul T n (avail_conj_mul T n hS hS) hS
  rw [gateFlow_eq_shear_mix, conjChannel_unit_smul (Complex.norm_exp_ofReal_mul_I _)]
  exact avail_conj_mul T n (avail_conj_mul T n hS (mixAvail_of_pairFlowSourced hs n _)) hS'

/-- **THE BACKWARD DIRECTION**: the closure with a sourced pair flow is exact finite endomorphic
operational quantum mechanics, by the existing Q3 at the site exchange, which moves `0`. -/
theorem qm_of_derivedOI_pairFlowSourced (hd : DerivedOI T) (hs : PairFlowSourced T) :
    ExactAllFiniteEndomorphicQuantumOps T :=
  have hσ : ∀ x : Fin 2, Equiv.swap (0 : Fin 2) 1 (Equiv.swap 0 1 x) = x :=
    fun x => Equiv.swap_apply_self _ _ _
  qm_of_derivedOI_layerFlowExecutable T hd hσ (x := (0 : Fin 2)) (by simp)
    (layerFlowExecutable_of_derivedOI_pairFlowSourced hd hs)

/-- **THE CENTRAL THEOREM**: on the two-valued carrier, exact finite endomorphic operational
quantum mechanics is exactly the consequence closure together with one sourced real pair flow. -/
theorem qm_iff_derivedOI_pairFlowSourced (T : FiniteOperationalTheory (Fin 2)) :
    ExactAllFiniteEndomorphicQuantumOps T ↔ DerivedOI T ∧ PairFlowSourced T :=
  ⟨derivedOI_pairFlowSourced_of_qm T, fun ⟨hd, hs⟩ => qm_of_derivedOI_pairFlowSourced hd hs⟩

end Backward

/-! ### Section D — T6: the countercontrols -/

section Countercontrols

/-- **THE POLARIZATION CLOSURE IS NOT SOURCED**: it satisfies the closure and is not quantum
mechanics, so by the backward direction it carries no sourced pair flow. -/
theorem polarizedTheoryC_not_pairFlowSourced : ¬ PairFlowSourced (polarizedTheoryC (Fin 2)) :=
  fun hs => polarizedTheoryC_not_qm (qm_of_derivedOI_pairFlowSourced polarizedTheoryC_derivedOI hs)

/-- **THE CARDINALITY NECESSITY AT THE THEORY LEVEL**: a theory whose available unit conjugations
at level one are countable up to scalar carries no sourced pair flow, since the datum's images at
distinct angles in `(0, π/2)` are pairwise non-proportional. A necessary condition; nothing here
exhibits a non-quantum theory with a coherent continuum. -/
theorem countable_not_pairFlowSourced (T : FiniteOperationalTheory (Fin 2))
    (D : Set (Matrix (Fin 2 × Fin 1) (Fin 2 × Fin 1) ℂ)) (hD : D.Countable)
    (hmem : ∀ V : Matrix (Fin 2 × Fin 1) (Fin 2 × Fin 1) ℂ,
      T.availExt 1 Unit (fun _ => conjChannel V) →
        ∃ (c : ℂ) (M : Matrix (Fin 2 × Fin 1) (Fin 2 × Fin 1) ℂ), M ∈ D ∧ V = c • M) :
    ¬ PairFlowSourced T := by
  intro hs
  have hray : ∀ θ : ℝ, ∃ M : Matrix (Fin 2 × Fin 1) (Fin 2 × Fin 1) ℂ,
      θ ∈ Ioo (0 : ℝ) (Real.pi / 2) → M ∈ D ∧ ∃ d : ℂ, mixImage 1 θ = d • M := by
    intro θ
    by_cases hθ : θ ∈ Ioo (0 : ℝ) (Real.pi / 2)
    · obtain ⟨c, M, hM, hcM⟩ := hmem _ (mixAvail_of_pairFlowSourced hs 1 θ)
      exact ⟨M, fun _ => ⟨hM, c, hcM⟩⟩
    · exact ⟨0, fun h => absurd h hθ⟩
  choose f hf using hray
  have hinj : InjOn f (Ioo (0 : ℝ) (Real.pi / 2)) := by
    intro θ hθ θ' hθ' hfθ
    by_contra hne
    obtain ⟨-, d, hd⟩ := hf θ hθ
    obtain ⟨-, d', hd'⟩ := hf θ' hθ'
    have hd'0 : d' ≠ 0 := by
      rintro rfl
      have := congrFun (congrFun hd' (0, 0)) (0, 0)
      simp only [zero_smul, Matrix.zero_apply, mixImage_apply, if_true, rot_apply_00] at this
      have hc : (Real.cos θ' : ℂ) ≠ 0 := by
        exact_mod_cast (Real.cos_pos_of_mem_Ioo ⟨by linarith [hθ'.1, Real.pi_pos], hθ'.2⟩).ne'
      exact hc this
    apply mixImage_not_proportional (0 : Fin 1) hθ hθ' hne (d * d'⁻¹)
    rw [hd, hfθ, hd', smul_smul, mul_assoc, inv_mul_cancel₀ hd'0, mul_one]
  have hmaps : MapsTo f (Ioo (0 : ℝ) (Real.pi / 2)) D := fun θ hθ => (hf θ hθ).1
  have hcount : (Ioo (0 : ℝ) (Real.pi / 2)).Countable := hmaps.countable_of_injOn hinj hD
  have := Cardinal.le_aleph0_iff_set_countable.mpr hcount
  rw [Cardinal.mk_Ioo_real (by positivity : (0 : ℝ) < Real.pi / 2)] at this
  exact absurd this (not_le.mpr Cardinal.aleph0_lt_continuum)

end Countercontrols

end PairFlowEquivalence
end OIBridge

#print axioms OIBridge.PairFlowEquivalence.rotR_orth
#print axioms OIBridge.PairFlowEquivalence.rotR_continuous
#print axioms OIBridge.PairFlowEquivalence.rotFlow_A
#print axioms OIBridge.PairFlowEquivalence.pairFlowSourced_of_qm
#print axioms OIBridge.PairFlowEquivalence.derivedOI_pairFlowSourced_of_qm
#print axioms OIBridge.PairFlowEquivalence.mixAvail_of_pairFlowSourced
#print axioms OIBridge.PairFlowEquivalence.identity_avail_of_pairFlowSourced
#print axioms OIBridge.PairFlowEquivalence.phaseIndicator_avail
#print axioms OIBridge.PairFlowEquivalence.siteShear_avail
#print axioms OIBridge.PairFlowEquivalence.conjChannel_unit_smul
#print axioms OIBridge.PairFlowEquivalence.layerFlowExecutable_of_derivedOI_pairFlowSourced
#print axioms OIBridge.PairFlowEquivalence.qm_of_derivedOI_pairFlowSourced
#print axioms OIBridge.PairFlowEquivalence.qm_iff_derivedOI_pairFlowSourced
#print axioms OIBridge.PairFlowEquivalence.polarizedTheoryC_not_pairFlowSourced
#print axioms OIBridge.PairFlowEquivalence.countable_not_pairFlowSourced
