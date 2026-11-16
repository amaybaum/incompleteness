import Mathlib.MeasureTheory.Measure.Count
import Mathlib.MeasureTheory.Measure.ProbabilityMeasure
import Mathlib.MeasureTheory.Measure.Prod
import OIBridge.Reciprocity

/-!
# P6 reciprocity under a fixed probability law

The accepted P6 paper, §§2–4, pairs measurable two-endpoint events at every lag
under one law that is invariant under the dynamics and reversal. The conditional
probabilities divide those masses by separate positive root masses. No Markov
assumption is used. The finite product calculation connects to the existing
counting interface. Selection of a physical law remains open (Q6).
-/

open MeasureTheory Set
open scoped ENNReal

namespace OIBridge.MeasuredReciprocity

noncomputable section

set_option autoImplicit false

variable {S V H : Type*}

/-- Starting at label i and ending at label j after n steps. -/
def endpointEvent (X : S → V) (φ : Equiv.Perm S) (n : ℕ) (i j : V) : Set S :=
  X ⁻¹' {i} ∩ (fun x => X ((φ ^ n) x)) ⁻¹' {j}

variable [MeasurableSpace S]

def rootMass (μ : ProbabilityMeasure S) (X : S → V) (i : V) : ℝ :=
  ((μ : Measure S) (X ⁻¹' {i})).toReal

def flux (μ : ProbabilityMeasure S) (X : S → V) (φ : Equiv.Perm S)
    (n : ℕ) (i j : V) : ℝ :=
  ((μ : Measure S) (endpointEvent X φ n i j)).toReal

/-- The quotient is exposed as a conditional probability only at a positive root. -/
def transition (μ : ProbabilityMeasure S) (X : S → V) (φ : Equiv.Perm S)
    (n : ℕ) (i j : V) (_hroot : 0 < rootMass μ X i) : ℝ :=
  flux μ X φ n i j / rootMass μ X i

private theorem preserving_pow {φ : Equiv.Perm S} {μ : Measure S}
    (hφ : MeasurePreserving φ μ μ) (n : ℕ) :
    MeasurePreserving (⇑(φ ^ n)) μ μ := by
  simpa only [Equiv.Perm.coe_pow] using hφ.iterate n

omit [MeasurableSpace S] in
private theorem reverse_pow (φ : Equiv.Perm S) (Θ : S → S)
    (hΘ : Function.Involutive Θ) (hrev : ∀ x, φ.symm x = Θ (φ (Θ x))) :
    ∀ (n : ℕ) (x : S), (φ ^ n) (Θ ((φ ^ n) x)) = Θ x := by
  have hstep (x : S) : φ (Θ (φ x)) = Θ x := by
    calc
      φ (Θ (φ x)) = Θ (Θ (φ (Θ (φ x)))) := (hΘ _).symm
      _ = Θ x := by rw [← hrev (φ x), Equiv.symm_apply_apply]
  intro n
  induction n with
  | zero =>
    intro x
    simp
  | succ n ih =>
    intro x
    have hleft (y : S) : (φ ^ (n + 1)) y = φ ((φ ^ n) y) := by
      rw [pow_succ']
      rfl
    have hright (y : S) : (φ ^ (n + 1)) y = (φ ^ n) (φ y) := by
      rw [pow_succ]
      rfl
    rw [hleft (Θ ((φ ^ (n + 1)) x)), hright x, ih (φ x), hstep x]

omit [MeasurableSpace S] in
private theorem reverse_event_preimage
    (X : S → V) (φ : Equiv.Perm S) (Θ : S → S) (θ : V → V)
    (hΘ : Function.Involutive Θ) (hθ : Function.Involutive θ)
    (hrev : ∀ x, φ.symm x = Θ (φ (Θ x))) (hread : ∀ x, X (Θ x) = θ (X x))
    (n : ℕ) (i j : V) :
    (Θ ∘ ⇑(φ ^ n)) ⁻¹' endpointEvent X φ n (θ j) (θ i) = endpointEvent X φ n i j := by
  ext x
  change
    (X (Θ ((φ ^ n) x)) = θ j ∧ X ((φ ^ n) (Θ ((φ ^ n) x))) = θ i) ↔
      (X x = i ∧ X ((φ ^ n) x) = j)
  rw [hread ((φ ^ n) x), reverse_pow φ Θ hΘ hrev n x, hread x]
  exact ⟨fun h => ⟨hθ.injective h.2, hθ.injective h.1⟩,
    fun h => ⟨congrArg θ h.2, congrArg θ h.1⟩⟩

/-- P6 equal flux for every lag, including zero. The same normalized law is
preserved by the forward step and by the cut-compatible time reversal. -/
theorem reciprocal_flux [MeasurableSpace V] [MeasurableSingletonClass V]
    [Fintype V] [Nonempty V]
    (μ : ProbabilityMeasure S) (X : S → V) (φ : Equiv.Perm S) (Θ : S → S) (θ : V → V)
    (hX : Measurable X) (_hφInv : Measurable (⇑φ.symm))
    (hφ : MeasurePreserving φ (μ : Measure S) μ)
    (hμΘ : MeasurePreserving Θ (μ : Measure S) μ)
    (hΘ : Function.Involutive Θ) (hθ : Function.Involutive θ)
    (hrev : ∀ x, φ.symm x = Θ (φ (Θ x))) (hread : ∀ x, X (Θ x) = θ (X x))
    (n : ℕ) (i j : V) :
    flux μ X φ n i j = flux μ X φ n (θ j) (θ i) := by
  have hφn := preserving_pow hφ n
  have hR := hμΘ.comp hφn
  have hevent : MeasurableSet (endpointEvent X φ n (θ j) (θ i)) :=
    ((measurableSet_singleton _).preimage hX).inter
      ((measurableSet_singleton _).preimage (hX.comp hφn.measurable))
  have hpre := reverse_event_preimage X φ Θ θ hΘ hθ hrev hread n i j
  unfold flux
  apply congrArg ENNReal.toReal
  rw [← hpre, ← Measure.map_apply hR.measurable hevent, hR.map_eq]

section Conditional

variable {μ : ProbabilityMeasure S} {X : S → V} {φ : Equiv.Perm S}
variable {θ : V → V} {n : ℕ} {i j : V}
variable {hi : 0 < rootMass μ X i} {hj : 0 < rootMass μ X (θ j)}

private theorem root_mul_transition (hi : 0 < rootMass μ X i) :
    rootMass μ X i * transition μ X φ n i j hi = flux μ X φ n i j := by
  rw [mul_comm, transition, div_mul_cancel₀ _ (ne_of_gt hi)]

/-- Both sides are the paired endpoint masses, even when the positive root weights differ. -/
theorem weighted_transition_reciprocity
    (hflux : flux μ X φ n i j = flux μ X φ n (θ j) (θ i)) :
    rootMass μ X i * transition μ X φ n i j hi =
      rootMass μ X (θ j) * transition μ X φ n (θ j) (θ i) hj := by
  simpa only [root_mul_transition] using hflux

/-- The unweighted comparison follows when the two roots have equal positive weight. -/
theorem transition_reciprocity_of_equal_roots
    (hflux : flux μ X φ n i j = flux μ X φ n (θ j) (θ i))
    (hroots : rootMass μ X i = rootMass μ X (θ j)) :
    transition μ X φ n i j hi = transition μ X φ n (θ j) (θ i) hj := by
  unfold transition
  rw [hflux, hroots]

/-- For positive paired flux, unweighted reciprocity is equivalent to equal positive roots. -/
theorem transition_reciprocity_iff_of_pos_flux
    (hflux : flux μ X φ n i j = flux μ X φ n (θ j) (θ i))
    (hpos : 0 < flux μ X φ n i j) :
    transition μ X φ n i j hi = transition μ X φ n (θ j) (θ i) hj ↔
      rootMass μ X i = rootMass μ X (θ j) := by
  constructor
  · intro heq
    have hne : transition μ X φ n i j hi ≠ 0 :=
      div_ne_zero (ne_of_gt hpos) (ne_of_gt hi)
    have hweighted := weighted_transition_reciprocity (hi := hi) (hj := hj) hflux
    rw [← heq] at hweighted
    exact mul_right_cancel₀ hne hweighted
  · exact transition_reciprocity_of_equal_roots hflux

/-- At zero paired flux both quotients are zero when the two roots are positive.
A zero-mass root cannot supply the witness required by transition. -/
theorem transitions_eq_zero_of_zero_flux
    (hflux : flux μ X φ n i j = flux μ X φ n (θ j) (θ i))
    (hzero : flux μ X φ n i j = 0) :
    transition μ X φ n i j hi = 0 ∧ transition μ X φ n (θ j) (θ i) hj = 0 := by
  simp [transition, hzero, hflux.symm.trans hzero]

end Conditional

section CountingLaw

/-- Normalized counting on a finite nonempty discrete space. -/
def uniformCountingLaw (A : Type*) [MeasurableSpace A] [MeasurableSingletonClass A]
    [Fintype A] [Nonempty A] : ProbabilityMeasure A :=
  ⟨(Fintype.card A : ℝ≥0∞)⁻¹ • Measure.count, by
    constructor
    have huniv : (Measure.count : Measure A) univ = Fintype.card A := by
      rw [← Finset.coe_univ, Measure.count_apply_finset, Finset.card_univ]
    rw [Measure.smul_apply, smul_eq_mul, huniv]
    exact ENNReal.inv_mul_cancel (by simp [Fintype.card_ne_zero]) (by simp)⟩

private theorem uniform_singleton {A : Type*} [MeasurableSpace A] [MeasurableSingletonClass A]
    [Fintype A] [Nonempty A] (a : A) :
    (uniformCountingLaw A : Measure A) {a} = (Fintype.card A : ℝ≥0∞)⁻¹ := by
  change ((Fintype.card A : ℝ≥0∞)⁻¹ • Measure.count) {a} = _
  rw [Measure.smul_apply, smul_eq_mul, Measure.count_singleton, mul_one]

private theorem uniform_preserving {A : Type*} [MeasurableSpace A] [MeasurableSingletonClass A]
    [Fintype A] [Nonempty A] (f : Equiv.Perm A) :
    MeasurePreserving f (uniformCountingLaw A : Measure A) (uniformCountingLaw A : Measure A) := by
  have hm : Measurable (⇑f) := measurable_of_countable _
  refine ⟨hm, Measure.ext_of_singleton fun a => ?_⟩
  have hpre : (⇑f) ⁻¹' ({a} : Set A) = {f.symm a} := by
    ext x
    change f x = a ↔ x = f.symm a
    constructor
    · intro h
      exact f.injective (h.trans (f.apply_symm_apply a).symm)
    · intro h
      rw [h, f.apply_symm_apply]
  rw [Measure.map_apply hm (measurableSet_singleton a), hpre, uniform_singleton,
    uniform_singleton]

end CountingLaw

section Product

variable [MeasurableSpace V] [MeasurableSingletonClass V] [Fintype V] [Nonempty V]
variable [MeasurableSpace H]

/-- One uniform visible law times one normalized hidden law, shared by all roots and lags. -/
def commonHiddenLaw (ν : ProbabilityMeasure H) : ProbabilityMeasure (V × H) :=
  ⟨(uniformCountingLaw V : Measure V).prod (ν : Measure H), inferInstance⟩

theorem common_hidden_root_mass (ν : ProbabilityMeasure H) (i : V) :
    rootMass (commonHiddenLaw ν) Prod.fst i = (Fintype.card V : ℝ)⁻¹ := by
  have hroot : Prod.fst ⁻¹' ({i} : Set V) = ({i} : Set V) ×ˢ (univ : Set H) := by
    ext p
    simp
  change (((uniformCountingLaw V : Measure V).prod (ν : Measure H))
    (Prod.fst ⁻¹' ({i} : Set V))).toReal = _
  rw [hroot, Measure.prod_prod, measure_univ, mul_one, uniform_singleton,
    ENNReal.toReal_inv, ENNReal.toReal_natCast]

theorem common_hidden_root_pos (ν : ProbabilityMeasure H) (i : V) :
    0 < rootMass (commonHiddenLaw ν) Prod.fst i := by
  rw [common_hidden_root_mass]
  exact inv_pos.mpr (Nat.cast_pos.mpr Fintype.card_pos)

/-- Product reversal preserves the shared law, while preservation by the
substratum permutation is a separate hypothesis. -/
theorem common_hidden_law_reciprocity (ν : ProbabilityMeasure H)
    (φ : Equiv.Perm (V × H)) (θ : Equiv.Perm V) (θH : H → H)
    (hφInv : Measurable (⇑φ.symm))
    (hφ : MeasurePreserving φ (commonHiddenLaw (V := V) ν).toMeasure
      (commonHiddenLaw (V := V) ν).toMeasure)
    (hν : MeasurePreserving θH (ν : Measure H) ν)
    (hθ : Function.Involutive θ) (hθH : Function.Involutive θH)
    (hrev : ∀ x, φ.symm x = Prod.map θ θH (φ (Prod.map θ θH x)))
    (n : ℕ) (i j : V) :
    transition (commonHiddenLaw ν) Prod.fst φ n i j (common_hidden_root_pos ν i) =
      transition (commonHiddenLaw ν) Prod.fst φ n (θ j) (θ i)
        (common_hidden_root_pos ν (θ j)) := by
  have hΘ : Function.Involutive (Prod.map θ θH) := by
    rintro ⟨v, h⟩
    change (θ (θ v), θH (θH h)) = (v, h)
    rw [hθ v, hθH h]
  have hμΘ : MeasurePreserving (Prod.map θ θH)
      (commonHiddenLaw (V := V) ν).toMeasure (commonHiddenLaw (V := V) ν).toMeasure :=
    (uniform_preserving θ).prod hν
  have hflux := reciprocal_flux (commonHiddenLaw ν) Prod.fst φ (Prod.map θ θH) θ
    measurable_fst hφInv hφ hμΘ hΘ hθ hrev (fun _ => rfl) n i j
  exact transition_reciprocity_of_equal_roots hflux
    ((common_hidden_root_mass ν i).trans (common_hidden_root_mass ν (θ j)).symm)

private def transitionFiber (φ : Equiv.Perm (V × H)) (n : ℕ) (i j : V) : Set H :=
  {h | ((φ ^ n) (i, h)).1 = j}

omit [MeasurableSpace V] [MeasurableSingletonClass V] [Fintype V] [Nonempty V]
  [MeasurableSpace H] in
private theorem endpoint_event_product (φ : Equiv.Perm (V × H)) (n : ℕ) (i j : V) :
    endpointEvent Prod.fst φ n i j = ({i} : Set V) ×ˢ transitionFiber φ n i j := by
  ext p
  rcases p with ⟨v, h⟩
  change (v = i ∧ ((φ ^ n) (v, h)).1 = j) ↔ (v = i ∧ ((φ ^ n) (i, h)).1 = j)
  constructor <;> rintro ⟨rfl, hstep⟩ <;> exact ⟨rfl, hstep⟩

private theorem common_hidden_transition_eq_mass (ν : ProbabilityMeasure H)
    (φ : Equiv.Perm (V × H)) (n : ℕ) (i j : V) :
    transition (commonHiddenLaw ν) Prod.fst φ n i j (common_hidden_root_pos ν i) =
      ((ν : Measure H) (transitionFiber φ n i j)).toReal := by
  unfold transition flux
  rw [common_hidden_root_mass, endpoint_event_product]
  change (((uniformCountingLaw V : Measure V).prod (ν : Measure H))
    (({i} : Set V) ×ˢ transitionFiber φ n i j)).toReal / (Fintype.card V : ℝ)⁻¹ = _
  rw [Measure.prod_prod, uniform_singleton, ENNReal.toReal_mul, ENNReal.toReal_inv,
    ENNReal.toReal_natCast, mul_comm]
  exact mul_div_cancel_right₀ _ (inv_ne_zero (by
    exact_mod_cast (Fintype.card_ne_zero : Fintype.card V ≠ 0)))

end Product

section FiniteSpecialization

variable [MeasurableSpace V] [MeasurableSingletonClass V] [Fintype V] [Nonempty V]
variable [MeasurableSpace H] [MeasurableSingletonClass H] [Fintype H] [Nonempty H]

private theorem uniform_product_eq_uniform :
    (commonHiddenLaw (V := V) (uniformCountingLaw H) : Measure (V × H)) =
      (uniformCountingLaw (V × H) : Measure (V × H)) := by
  apply Measure.ext_of_singleton
  rintro ⟨v, h⟩
  change ((uniformCountingLaw V : Measure V).prod (uniformCountingLaw H : Measure H))
    {(v, h)} = _
  calc
    _ = (Fintype.card V : ℝ≥0∞)⁻¹ * (Fintype.card H : ℝ≥0∞)⁻¹ := by
      rw [← singleton_prod_singleton, Measure.prod_prod, uniform_singleton, uniform_singleton]
    _ = _ := by
      rw [uniform_singleton, Fintype.card_prod, Nat.cast_mul, ENNReal.mul_inv (by simp) (by simp)]

variable [DecidableEq V]

/-- The measured conditional under the finite uniform law is exactly the
existing transition-fibre count divided by the size of the hidden space. -/
theorem finite_uniform_transition_eq_count (φ : Equiv.Perm (V × H)) (n : ℕ) (i j : V) :
    transition (commonHiddenLaw (uniformCountingLaw H)) Prod.fst φ n i j
      (common_hidden_root_pos (uniformCountingLaw H) i) =
      (Reciprocity.N (φ ^ n) i j : ℝ) / Fintype.card H := by
  rw [common_hidden_transition_eq_mass]
  have hf : transitionFiber φ n i j =
      (↑(Finset.univ.filter fun h : H => ((φ ^ n) (i, h)).1 = j) : Set H) := by
    ext h
    simp [transitionFiber]
  change (((Fintype.card H : ℝ≥0∞)⁻¹ • Measure.count) (transitionFiber φ n i j)).toReal = _
  rw [hf, Measure.smul_apply, smul_eq_mul, Measure.count_apply_finset, ENNReal.toReal_mul,
    ENNReal.toReal_inv, ENNReal.toReal_natCast, ENNReal.toReal_natCast, div_eq_mul_inv, mul_comm]
  rfl

/-- Finite uniform counting recovers the count equality of Reciprocity.theorem_19
from the measured theorem, with the same time-reversal condition. -/
theorem finite_uniform_reciprocity (φ : Equiv.Perm (V × H))
    (θ : Equiv.Perm V) (θH : Equiv.Perm H)
    (hθ : Function.Involutive θ) (hθH : Function.Involutive θH)
    (hrev : ∀ x, φ.symm x = Reciprocity.Tm θ θH (φ (Reciprocity.Tm θ θH x)))
    (n : ℕ) (i j : V) :
    Reciprocity.N (φ ^ n) i j = Reciprocity.N (φ ^ n) (θ j) (θ i) := by
  have hφ : MeasurePreserving φ
      (commonHiddenLaw (V := V) (uniformCountingLaw H)).toMeasure
      (commonHiddenLaw (V := V) (uniformCountingLaw H)).toMeasure := by
    rw [uniform_product_eq_uniform]
    exact uniform_preserving φ
  have h := common_hidden_law_reciprocity (uniformCountingLaw H) φ θ θH
    (measurable_of_countable _) hφ (uniform_preserving θH) hθ hθH hrev n i j
  rw [finite_uniform_transition_eq_count, finite_uniform_transition_eq_count] at h
  have hcard : (Fintype.card H : ℝ) ≠ 0 := by
    exact_mod_cast (Fintype.card_ne_zero : Fintype.card H ≠ 0)
  have hmul := congrArg (fun x : ℝ => x * (Fintype.card H : ℝ)) h
  simp only [div_mul_cancel₀ _ hcard] at hmul
  exact_mod_cast hmul

end FiniteSpecialization

#print axioms reciprocal_flux
#print axioms weighted_transition_reciprocity
#print axioms transition_reciprocity_of_equal_roots
#print axioms transition_reciprocity_iff_of_pos_flux
#print axioms transitions_eq_zero_of_zero_flux
#print axioms common_hidden_law_reciprocity
#print axioms finite_uniform_transition_eq_count
#print axioms finite_uniform_reciprocity

end

end OIBridge.MeasuredReciprocity
