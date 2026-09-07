import OIBridge.DenseInstrumentBridge

/-!
# The frozen substratum nonclassical-resource sourcing audit — the ceilings of the stated architecture

The preregistered pass of `FROZEN-SUBSTRATUM-SOURCING-AUDIT.md`. The substratum axioms, the
observer architecture, the implementation semantics and the availability rules are frozen exactly
as they stand: nothing here adds an axiom, an operation, a carrier map, a coupling or a class
enrichment, and nothing added anywhere is reported as sourced. The round audits two obligations
separately — the phase structure and dense unitary control — through one invariant of the frozen
source class, and only then asks the combined question. Nothing here is named "C5"; no continuous
pair flow enters any route; `PhasesAvailable` is never identified with `DenseUnitaryControl`; and
sufficiency for dense quantum mechanics is never identified with sourcing by the substratum.
-/

namespace OIBridge
namespace FrozenSourcing

open Complex Matrix CoherentLift OperationalAssembly InterventionLocality MonoidalCompletion
open RouteB SubstratumInterface SubstratumInterfaceAudit StateMixingCoupling
open DiscreteCompletion DenseInstrumentBridge LieRankSource ReadWriteControl LiftAudit
open AncillaClosure SecondOrderLayer PairFlowEquivalence
open scoped Matrix.Norms.L2Operator ComplexOrder

/-! ### Section A — the entrywise bound the limit argument needs -/

section Entry

/-- **AN ENTRY IS BOUNDED BY THE OPERATOR NORM**: the `(p, q)` entry is the `p`-th coordinate of
the image of the `q`-th basis vector. -/
theorem norm_entry_le_l2_opNorm {m n : Type*} [Fintype m] [Fintype n] [DecidableEq n]
    (M : Matrix m n ℂ) (p : m) (q : n) : ‖M p q‖ ≤ ‖M‖ := by
  have hx : ‖(EuclideanSpace.single q (1 : ℂ) : EuclideanSpace ℂ n)‖ = 1 := by simp
  have h := Matrix.l2_opNorm_mulVec M (EuclideanSpace.single q (1 : ℂ))
  rw [hx, mul_one] at h
  refine le_trans (le_of_eq ?_) (le_trans (PiLp.norm_apply_le _ p) h)
  congr 1
  show M p q = (M *ᵥ (EuclideanSpace.single q (1 : ℂ)).ofLp) p
  simp [Matrix.mulVec, dotProduct]

/-- A real number below every positive number is at most zero. -/
theorem le_zero_of_forall_pos {x : ℝ} (h : ∀ ε : ℝ, 0 < ε → x ≤ ε) : x ≤ 0 := by
  by_contra hx
  have hx' : 0 < x := not_le.mp hx
  exact absurd (h (x / 2) (by linarith)) (by linarith)

/-- A real number above every negative number is at least zero. -/
theorem nonneg_of_forall_pos {x : ℝ} (h : ∀ ε : ℝ, 0 < ε → -ε ≤ x) : 0 ≤ x := by
  by_contra hx
  have hx' : x < 0 := not_le.mp hx
  exact absurd (h (-x / 2) (by linarith)) (by linarith)

end Entry

/-! ### Section B — the invariant of the frozen source class -/

section Invariant

variable {A : Type} [Fintype A] [DecidableEq A]

/-- **A NONNEGATIVITY-BOUNDED THEORY**: every available composite one-outcome operation preserves
nonnegative entries. This is the characterized class the round works with — a property of the
theory's availability, not of any single matrix, and the form in which the frozen source class's
ceiling is stated. -/
def NonnegBounded (T : FiniteOperationalTheory A) : Prop :=
  ∀ (n : ℕ) (Φ : Matrix (A × Fin n) (A × Fin n) ℂ →ₗ[ℂ] Matrix (A × Fin n) (A × Fin n) ℂ),
    T.availExt n Unit (fun _ => Φ) → PreservesNonneg Φ

/-- **THE THEORY OF A BIJECTION-LEVEL CLASS IS NONNEGATIVITY-BOUNDED.** Every available branch is
realized by the class (`realized_of_instAvail`), and every operation realized by a bijection-level
class preserves nonnegative entries (`preservesNonneg_of_realized`). The statement passes through
the implementation class and the realization theorem, never through a claim that a single available
channel is itself a scaled partial permutation. -/
theorem nonnegBounded_of_bijectionLevel {𝓘 : ImplementationClass} (arch : Architecture 𝓘)
    (hb : BijectionLevel 𝓘) : NonnegBounded (genTheory 𝓘 arch A) :=
  fun _ _ hav => preservesNonneg_of_realized hb (realized_of_instAvail arch hav ())

/-- **THE SOURCED THEORY IS NONNEGATIVITY-BOUNDED.** -/
theorem permTheory_nonnegBounded : NonnegBounded (permTheory A) :=
  nonnegBounded_of_bijectionLevel permClass_arch permClass_bijectionLevel

/-- **THE OBSERVER THEORY OF ANY SUBSTRATUM IS NONNEGATIVITY-BOUNDED**, at every substratum
satisfying the finiteness A1 supplies. -/
theorem obsTheory_nonnegBounded (𝒮 : Substratum) [Fintype 𝒮.ι] [Fintype 𝒮.V] [DecidableEq 𝒮.V] :
    NonnegBounded (obsTheory 𝒮) :=
  permTheory_nonnegBounded

end Invariant

/-! ### Section C — T3: the phase ceiling, at class level -/

section PhaseCeiling

variable {A : Type} [Fintype A] [DecidableEq A]

/-- **A NONNEGATIVITY-BOUNDED THEORY HAS NO PHASES**: the quarter phase at the second level is a
one-outcome composite conjugation whose channel does not preserve nonnegative entries. The ceiling
is stated of the invariant, so it holds of every theory carrying it and not merely of one class. -/
theorem nonnegBounded_not_phasesAvailable [Nonempty A] {T : FiniteOperationalTheory A}
    (h : NonnegBounded T) : ¬ PhasesAvailable T := by
  intro hp
  exact phaseGate_not_preservesNonneg (Classical.arbitrary A)
    (h 2 _ (hp 2 (Classical.arbitrary A, 0)))

/-- **THE PHASE CEILING FOR THE SOURCED THEORY.** -/
theorem permTheory_phase_ceiling [Nonempty A] : ¬ PhasesAvailable (permTheory A) :=
  nonnegBounded_not_phasesAvailable permTheory_nonnegBounded

/-- **A NONNEGATIVITY-BOUNDED THEORY IS NOT THE CONSEQUENCE CLOSURE**, since the closure carries
the phases as one of its conjuncts. -/
theorem nonnegBounded_not_derivedOI [Nonempty A] {T : FiniteOperationalTheory A}
    (h : NonnegBounded T) : ¬ DerivedOI T :=
  fun hd => nonnegBounded_not_phasesAvailable h hd.2.2.2.1

end PhaseCeiling

/-! ### Section D — T4: the dense-control ceiling -/

section DenseCeiling

variable {S : Type} [Fintype S] [DecidableEq S]

/-- **THE INVARIANT PASSES TO LIMITS**: a unitary approximated in the operator norm by unitaries
whose conjugations preserve nonnegative entries has a conjugation that preserves them. Entries are
bounded by the operator norm and the bridge `conj_within` controls the channel difference, so each
entry of the limit is a limit of nonnegative numbers. -/
theorem preservesNonneg_of_approx [Nonempty S] {U : Matrix S S ℂ} (hU : Uᴴ * U = 1)
    (happ : ∀ ε : ℝ, 0 < ε → ∃ W : Matrix S S ℂ,
      Wᴴ * W = 1 ∧ PreservesNonneg (conjChannel W) ∧ ‖U - W‖ < ε) :
    PreservesNonneg (conjChannel U) := by
  intro X hX p q
  set a := conjChannel U X p q with ha
  -- every positive tolerance bounds the real part from below and the imaginary part in modulus
  have key : ∀ δ : ℝ, 0 < δ → -δ ≤ a.re ∧ |a.im| ≤ δ := by
    intro δ hδ
    have hXpos : (0 : ℝ) < ‖X‖ + 1 := by positivity
    obtain ⟨W, hW, hWn, hUW⟩ := happ (δ / (2 * (‖X‖ + 1))) (by positivity)
    have hb : 0 ≤ conjChannel W X p q := hWn X hX p q
    have hbre : 0 ≤ (conjChannel W X p q).re := (Complex.nonneg_iff.mp hb).1
    have hbim : (conjChannel W X p q).im = 0 := (Complex.nonneg_iff.mp hb).2.symm
    have hchan := conj_within hU hW hUW.le X
    have hentry : ‖a - conjChannel W X p q‖
        ≤ 2 * (δ / (2 * (‖X‖ + 1))) * ‖X‖ := by
      refine le_trans (le_of_eq ?_) (le_trans (norm_entry_le_l2_opNorm _ p q) hchan)
      rw [Matrix.sub_apply]
    have hsmall : 2 * (δ / (2 * (‖X‖ + 1))) * ‖X‖ ≤ δ := by
      have heq : 2 * (δ / (2 * (‖X‖ + 1))) * ‖X‖ = δ * ‖X‖ / (‖X‖ + 1) := by
        field_simp
      rw [heq, div_le_iff₀ hXpos]
      nlinarith [norm_nonneg X, hδ.le]
    have hle : ‖a - conjChannel W X p q‖ ≤ δ := hentry.trans hsmall
    constructor
    · have := (Complex.abs_re_le_norm (a - conjChannel W X p q)).trans hle
      rw [Complex.sub_re] at this
      have := abs_le.mp this
      linarith [this.1, hbre]
    · have := (Complex.abs_im_le_norm (a - conjChannel W X p q)).trans hle
      rw [Complex.sub_im, hbim, sub_zero] at this
      exact this
  refine Complex.nonneg_iff.mpr ⟨nonneg_of_forall_pos fun ε hε => (key ε hε).1, ?_⟩
  have := le_zero_of_forall_pos fun ε hε => (key ε hε).2
  exact (abs_eq_zero.mp (le_antisymm this (abs_nonneg _))).symm

end DenseCeiling

section Ceiling

/-- **THE DENSE-CONTROL CEILING**: a nonnegativity-bounded theory has no dense unitary control.
Dense control would put, next to every unitary, an exactly available conjugation carrying the
invariant; the invariant passes to limits, so every unitary's conjugation would preserve
nonnegative entries, which the quarter phase refutes. The ceiling is a property of the class, not
a statement about one gate. -/
theorem nonnegBounded_not_denseUnitaryControl {T : FiniteOperationalTheory (Fin 2)}
    (h : NonnegBounded T) : ¬ DenseUnitaryControl T := by
  intro hdense
  set a : Fin 2 × Fin 2 := ((0 : Fin 2), (0 : Fin 2)) with hadef
  refine phaseGate_not_preservesNonneg (S := Fin 2) 0 ?_
  refine preservesNonneg_of_approx (phaseGate_unitary a) ?_
  intro ε hε
  obtain ⟨V, c, hV, hc, hav, hclose⟩ := hdense 2 (phaseGate a) (phaseGate_unitary a) ε hε
  refine ⟨c • V, unitary_unit_smul hc hV, ?_, hclose⟩
  rw [PairFlowEquivalence.conjChannel_unit_smul hc]
  exact h 2 _ hav

/-- **THE DENSE-CONTROL CEILING FOR THE SOURCED THEORY** on the two-valued carrier, the carrier at
which `DenseUnitaryControl` is stated. -/
theorem permTheory_dense_ceiling : ¬ DenseUnitaryControl (permTheory (Fin 2)) :=
  nonnegBounded_not_denseUnitaryControl permTheory_nonnegBounded

end Ceiling

/-! ### Section E — the independent countercontrol: the pair rotation -/

section Rotation

/-- **THE PAIR ROTATION AT A QUARTER TURN DOES NOT PRESERVE NONNEGATIVE ENTRIES**: on the matrix
unit at the second site its `(0, 1)` entry is `− sin θ cos θ`. This separates the dense-control
ceiling from the phase ceiling: the rotation carries no phase and is still excluded. -/
theorem mixImage_not_preservesNonneg {n : ℕ} (k : Fin n) {θ : ℝ}
    (hs : 0 < Real.sin θ) (hc : 0 < Real.cos θ) :
    ¬ PreservesNonneg (conjChannel (mixImage n θ)) := by
  intro h
  have hX : ∀ i j, (0 : ℂ) ≤ Matrix.single ((1 : Fin 2), k) ((1 : Fin 2), k) (1 : ℂ) i j := by
    intro i j
    by_cases hij : ((1 : Fin 2), k) = i ∧ ((1 : Fin 2), k) = j
    · obtain ⟨rfl, rfl⟩ := hij
      rw [Matrix.single_apply_same]
      exact zero_le_one
    · rw [Matrix.single_apply_of_ne _ _ _ _ _ hij]
  have hval := h _ hX ((0 : Fin 2), k) ((1 : Fin 2), k)
  have hcalc : conjChannel (mixImage n θ)
      (Matrix.single ((1 : Fin 2), k) ((1 : Fin 2), k) (1 : ℂ)) ((0 : Fin 2), k) ((1 : Fin 2), k)
      = ((-(Real.sin θ) * Real.cos θ : ℝ) : ℂ) := by
    rw [conjChannel_apply, Matrix.mul_apply]
    rw [Finset.sum_eq_single ((1 : Fin 2), k)]
    · rw [Matrix.mul_apply, Finset.sum_eq_single ((1 : Fin 2), k)]
      · rw [Matrix.single_apply_same, mul_one, Matrix.conjTranspose_apply]
        show mixImage n θ ((0 : Fin 2), k) ((1 : Fin 2), k)
          * star (mixImage n θ ((1 : Fin 2), k) ((1 : Fin 2), k)) = _
        rw [mixImage_apply, mixImage_apply, if_pos rfl, if_pos rfl]
        show (StateMixingCoupling.rot θ 0 1) * star (StateMixingCoupling.rot θ 1 1) = _
        rw [show StateMixingCoupling.rot θ 0 1 = (-(Real.sin θ) : ℂ) from rfl,
          show StateMixingCoupling.rot θ 1 1 = (Real.cos θ : ℂ) from rfl]
        rw [Complex.star_def, Complex.conj_ofReal, Complex.ofReal_mul, Complex.ofReal_neg]
      · intro b _ hb
        rw [Matrix.single_apply_of_ne _ _ _ _ _ (by simp [hb.symm]), mul_zero]
      · intro hcon; exact absurd (Finset.mem_univ _) hcon
    · intro b _ hb
      rw [Matrix.mul_apply, Finset.sum_eq_zero, zero_mul]
      intro d _
      rw [Matrix.single_apply_of_ne _ _ _ _ _ (by simp [hb.symm]), mul_zero]
    · intro hcon; exact absurd (Finset.mem_univ _) hcon
  rw [hcalc, Complex.nonneg_iff] at hval
  have h1 : (0 : ℝ) ≤ -(Real.sin θ) * Real.cos θ := by
    have := hval.1
    rwa [Complex.ofReal_re] at this
  nlinarith [hs, hc]

/-- **THE DENSE-CONTROL CEILING THROUGH THE ROTATION**, with no phase in the witness. -/
theorem nonnegBounded_not_denseUnitaryControl_rot {T : FiniteOperationalTheory (Fin 2)}
    (h : NonnegBounded T) : ¬ DenseUnitaryControl T := by
  intro hdense
  refine mixImage_not_preservesNonneg (n := 1) 0
    (θ := Real.pi / 4) (by rw [Real.sin_pi_div_four]; positivity)
    (by rw [Real.cos_pi_div_four]; positivity) ?_
  refine preservesNonneg_of_approx (mixImage_unitary 1 (Real.pi / 4)) ?_
  intro ε hε
  obtain ⟨V, c, hV, hc, hav, hclose⟩ :=
    hdense 1 (mixImage 1 (Real.pi / 4)) (mixImage_unitary 1 (Real.pi / 4)) ε hε
  refine ⟨c • V, unitary_unit_smul hc hV, ?_, hclose⟩
  rw [PairFlowEquivalence.conjChannel_unit_smul hc]
  exact h 1 _ hav

end Rotation

/-! ### Section F — T1 and T5: the census and the rule -/

section Census

variable {A : Type} [Fintype A] [DecidableEq A]

/-- **THE SOURCED OPERATIONS CARRY THE INVARIANT**: every configuration bijection put into
availability by the interface is inside the ceiling. The substrate's own update, its inverse, the
shear layer and every exchange are of this shape. -/
theorem permMatrix_preservesNonneg {S : Type} [Fintype S] [DecidableEq S] (σ : Equiv.Perm S) :
    PreservesNonneg (conjChannel (permMatrix σ)) :=
  preservesNonneg_conj_of_scaled (permClass_permMatrix σ)

/-- **THE READ-WRITE OPERATORS CARRY THE INVARIANT.** -/
theorem readWrite_preservesNonneg {S : Type} [Fintype S] [DecidableEq S] {a b : S}
    (F : ReadWriteFamily a b) (l : ℝ) :
    PreservesNonneg (conjChannel (readWriteOperator F l)) :=
  preservesNonneg_conj_of_scaled (permClass_readWrite F l)

/-- **THE SUBSTRATE'S OWN UPDATE CARRIES THE INVARIANT**, at every level: the sourcing theorem
`obs_dynamics_avail` lands inside the ceiling rather than above it. -/
theorem obs_dynamics_preservesNonneg (𝒮 : Substratum) [Fintype 𝒮.ι] [Fintype 𝒮.V]
    [DecidableEq 𝒮.V] (n : ℕ) :
    PreservesNonneg (conjChannel (permMatrix (levelPerm 𝒮.φ n))) :=
  permMatrix_preservesNonneg _

/-- **THE PHASE OPERATOR IS REPRESENTED AND NOT SOURCED**: a diagonal with a genuine relative
phase is a matrix the kernel writes down, and its conjugation is outside the ceiling, so no
sourcing theorem can place it into the availability of a nonnegativity-bounded theory. -/
theorem phaseOperator_outside_ceiling {S : Type} [Fintype S] [DecidableEq S] (a : S) :
    ¬ PreservesNonneg (conjChannel (phaseOperator
      (fun p => if ((a, (0 : Fin 2)) : S × Fin 2) = p then Complex.I else 1))) :=
  phaseGate_not_preservesNonneg a

/-- **THE SOURCING VERDICT DOES NOT SEE THE RULE.** Two substrata on the same sites and alphabet
have the same observer theory (`obsTheory_rule_independent`), so every property of that theory —
the two obligations of this round among them — takes the same value whatever the rule. Changing
the microscopic dynamics while holding the configuration space fixed cannot move either ceiling
under the present interface. -/
theorem sourcing_rule_independent (ι V : Type) [DecidableEq ι] [AddCommGroup ι] [AddCommGroup V]
    [Fintype ι] [Fintype V] [DecidableEq V] (R R' : Rule ι V)
    (P : FiniteOperationalTheory (ι → V × V) → Prop) :
    P (obsTheory { ι := ι, V := V, R := R }) ↔ P (obsTheory { ι := ι, V := V, R := R' }) :=
  Iff.rfl

/-- The phase ceiling is rule-independent, as an instance. -/
theorem phase_ceiling_rule_independent (ι V : Type) [DecidableEq ι] [AddCommGroup ι]
    [AddCommGroup V] [Fintype ι] [Fintype V] [DecidableEq V] [Nonempty (ι → V × V)]
    (R : Rule ι V) : ¬ PhasesAvailable (obsTheory { ι := ι, V := V, R := R }) :=
  nonnegBounded_not_phasesAvailable (obsTheory_nonnegBounded _)

end Census

/-! ### Section G — T6: the combined verdict -/

section Verdict

/-- **THE COMBINED SOURCING VERDICT ON THE TWO-VALUED CARRIER.** The theory the frozen
architecture sources supplies neither obligation: no phase structure, no dense unitary control,
and therefore not the consequence closure either. The two are established separately and then
stated together; neither is derived from the other, and nothing here says how many independent
additions an extension would need. -/
theorem frozen_sourcing_verdict :
    ¬ PhasesAvailable (permTheory (Fin 2))
      ∧ ¬ DenseUnitaryControl (permTheory (Fin 2))
      ∧ ¬ DerivedOI (permTheory (Fin 2)) :=
  ⟨permTheory_phase_ceiling, permTheory_dense_ceiling,
    nonnegBounded_not_derivedOI permTheory_nonnegBounded⟩

/-- **THE VERDICT FOR ANY THEORY INSIDE THE CEILING**, stated of the invariant so that it covers
every architecture whose sourced class is bijection-level, not only the one class. -/
theorem nonnegBounded_verdict {T : FiniteOperationalTheory (Fin 2)} (h : NonnegBounded T) :
    ¬ PhasesAvailable T ∧ ¬ DenseUnitaryControl T ∧ ¬ DerivedOI T :=
  ⟨nonnegBounded_not_phasesAvailable h, nonnegBounded_not_denseUnitaryControl h,
    nonnegBounded_not_derivedOI h⟩

/-- **THE DENSITY SIDE IS DOWNSTREAM AND UNTOUCHED**: the canonical fixed-gate theory of the
discrete completion audit does have dense unitary control, so it is not inside the ceiling. The
sourcing verdict says that the frozen architecture does not reach that theory, not that the theory
fails to exist. -/
theorem fixedGateTheory_outside_ceiling {α : ℝ} (hα : Irrational (α / Real.pi)) :
    ¬ NonnegBounded (fixedGateTheory α) :=
  fun h => nonnegBounded_not_denseUnitaryControl h (fixedGateTheory_denseUnitaryControl hα)

end Verdict

end FrozenSourcing
end OIBridge

#print axioms OIBridge.FrozenSourcing.norm_entry_le_l2_opNorm
#print axioms OIBridge.FrozenSourcing.le_zero_of_forall_pos
#print axioms OIBridge.FrozenSourcing.nonneg_of_forall_pos
#print axioms OIBridge.FrozenSourcing.nonnegBounded_of_bijectionLevel
#print axioms OIBridge.FrozenSourcing.permTheory_nonnegBounded
#print axioms OIBridge.FrozenSourcing.obsTheory_nonnegBounded
#print axioms OIBridge.FrozenSourcing.nonnegBounded_not_phasesAvailable
#print axioms OIBridge.FrozenSourcing.permTheory_phase_ceiling
#print axioms OIBridge.FrozenSourcing.nonnegBounded_not_derivedOI
#print axioms OIBridge.FrozenSourcing.preservesNonneg_of_approx
#print axioms OIBridge.FrozenSourcing.nonnegBounded_not_denseUnitaryControl
#print axioms OIBridge.FrozenSourcing.permTheory_dense_ceiling
#print axioms OIBridge.FrozenSourcing.mixImage_not_preservesNonneg
#print axioms OIBridge.FrozenSourcing.nonnegBounded_not_denseUnitaryControl_rot
#print axioms OIBridge.FrozenSourcing.permMatrix_preservesNonneg
#print axioms OIBridge.FrozenSourcing.readWrite_preservesNonneg
#print axioms OIBridge.FrozenSourcing.obs_dynamics_preservesNonneg
#print axioms OIBridge.FrozenSourcing.phaseOperator_outside_ceiling
#print axioms OIBridge.FrozenSourcing.sourcing_rule_independent
#print axioms OIBridge.FrozenSourcing.phase_ceiling_rule_independent
#print axioms OIBridge.FrozenSourcing.frozen_sourcing_verdict
#print axioms OIBridge.FrozenSourcing.nonnegBounded_verdict
#print axioms OIBridge.FrozenSourcing.fixedGateTheory_outside_ceiling
