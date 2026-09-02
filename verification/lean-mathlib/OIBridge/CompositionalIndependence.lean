/-
  OIBridge/CompositionalIndependence.lean — the two compositional principles are mutually
  independent, `H_comp` supplies neither, and the conditional classification is frozen.

  ROUND THIRTY-NINE. Round thirty-eight established that composite soundness, control and
  inert-spectator compositionality do not give iterated ancilla closure. Full mutual
  independence needs the other direction as well, and it is supplied by the round-34
  dimensional countermodel: its composite sector is the 2-positive aggregate-trace-preserving
  instruments, and 2-positivity survives transport along a reindexing, uniform attachment
  and discard (`discardWith_uniform_twoPositive`), so that theory HAS iterated ancilla
  closure — while it refutes inert-spectator compositionality (round thirty-seven).

      ┌──────────────────────────────────────────────────────────────────────────────┐
      │                       │ inert spectators │ iterated ancilla closure           │
      │  round-34 countermodel│       No         │       Yes  (`countermodel_iteratedAncillaClosure`) │
      │  round-38 admissible  │       Yes        │       No                           │
      │  fullQuantum          │       Yes        │       Yes                          │
      │  `independence_matrix`: the three rows as one statement, each with system     │
      │    Kraus soundness and full composite unitary control.                        │
      │  `hcompRealized_inert_not_implies_closure`,                                   │
      │  `hcompRealized_closure_not_implies_inert`: realized `H_comp` (with control)   │
      │    supplies NEITHER existence principle.                                       │
      │  `inert_not_deletable`, `closure_not_deletable`: the endpoint fails when either │
      │    compositional clause is dropped.                                            │
      │  `conditional_classification`: the frozen operational result — the endpoint    │
      │    implication together with the three witnesses.                              │
      └──────────────────────────────────────────────────────────────────────────────┘

  WHAT THIS DOES AND DOES NOT SAY ABOUT OI. Every countermodel here is a
  `FiniteOperationalTheory`: it satisfies the operational closure rules as formalized in
  this project (identity, coarse-graining, feed-forward, uniform attachment, spectator-
  independent readout, discard to the system), together with exact system quantum mechanics
  and full composite unitary control, and — where stated — realized `H_comp`. The theorems
  therefore show that THOSE axioms do not imply the two compositional principles. They do
  NOT show that observer independence itself fails to imply them: that would require the
  countermodels to be exhibited as models of the bare OI axioms, which is not done here and
  is not claimed. The research question is stated in exactly that form. [CAVEAT RETIRED IN
  ROUND FORTY, `OIRealization.lean`: the sealed C1–C4 core is audited against the
  manuscript's finite-observation definition, Lemmas 1–3, Axioms 1–2 and C1–C4
  (`sealedCore_is_finiteOI`), and the same core is realized with its actual visible readout
  in both countermodels (`sameCore_both_sides`); the statement that survives is that bare
  finite OI, as formalized by the sealed core, does not imply either principle.]

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.ClosureObstruction

namespace OIBridge
namespace CompositionalIndependence

open Complex Matrix CoherentExtension MonoidalCompletion CoherentLift
open OperationalAssembly StinespringAssembly KrausSoundness CompositeSoundness
open DimensionalObstruction DimensionalCountermodel ReferenceExtension ReferenceSufficiency
open BoundaryAudit SpectatorBridge AncillaClosure ClosureObstruction

open scoped ComplexOrder

/-! ### Section A — 2-positivity through transport, attachment and discard -/

section TwoPositive

variable {S : Type*} [Fintype S] [DecidableEq S]

/-- The amplification of a transported map is the transported amplification (the reference
slot untouched). -/
theorem amplR_transport {l l' : Type*} [Fintype l] [Fintype l'] [DecidableEq l] [DecidableEq l']
    (e : l ≃ l') (Φ : Matrix l l ℂ →ₗ[ℂ] Matrix l l ℂ) (M : Matrix (Fin 2 × l') (Fin 2 × l') ℂ) :
    amplR (transport e Φ) M
      = Matrix.reindex (Equiv.prodCongr (Equiv.refl (Fin 2)) e) (Equiv.prodCongr (Equiv.refl (Fin 2)) e)
          (amplR Φ (Matrix.reindex (Equiv.prodCongr (Equiv.refl (Fin 2)) e).symm
            (Equiv.prodCongr (Equiv.refl (Fin 2)) e).symm M)) := by
  ext ⟨r, p⟩ ⟨r', q⟩
  rfl

theorem twoPositive_transport {l l' : Type*} [Fintype l] [Fintype l'] [DecidableEq l]
    [DecidableEq l'] (e : l ≃ l') {Φ : Matrix l l ℂ →ₗ[ℂ] Matrix l l ℂ} (h : IsTwoPositive Φ) :
    IsTwoPositive (transport e Φ) := by
  intro M hM
  rw [← amplR_eq_ampl2, amplR_transport]
  exact posSemidef_reindex _ (h _ (posSemidef_reindex _ hM))

theorem twoPositive_of_transport {l l' : Type*} [Fintype l] [Fintype l'] [DecidableEq l]
    [DecidableEq l'] (e : l ≃ l') {Φ : Matrix l l ℂ →ₗ[ℂ] Matrix l l ℂ}
    (h : IsTwoPositive (transport e Φ)) : IsTwoPositive Φ := by
  have := twoPositive_transport e.symm h
  rwa [transport_symm_transport] at this

/-- The amplified partial trace is a sum of principal submatrices. -/
theorem amplR_ptraceAncL_eq_sum (m : ℕ) (N : Matrix (Fin 2 × (S × Fin m)) (Fin 2 × (S × Fin m)) ℂ) :
    amplR (ptraceAncL (A := S) m) N
      = ∑ e : Fin m, N.submatrix (fun q : Fin 2 × S => (q.1, (q.2, e)))
          (fun q : Fin 2 × S => (q.1, (q.2, e))) := by
  ext ⟨r, s⟩ ⟨r', t⟩
  show ptraceAnc m (refBlock N r r') s t = _
  rw [ptraceAnc_apply, Matrix.sum_apply]
  rfl

/-- The fresh-ancilla embedding at value `e`, with the reference slot untouched. -/
def embR (m : ℕ) (e : Fin m) : Matrix (Fin 2 × (S × Fin m)) (Fin 2 × S) ℂ :=
  Matrix.of fun p x => if x = (p.1, p.2.1) ∧ p.2.2 = e then 1 else 0

theorem embR_conjTranspose_apply (m : ℕ) (e : Fin m) (x : Fin 2 × S) (p : Fin 2 × (S × Fin m)) :
    (embR (S := S) m e)ᴴ x p = if x = (p.1, p.2.1) ∧ p.2.2 = e then 1 else 0 := by
  rw [Matrix.conjTranspose_apply, embR, Matrix.of_apply, star_ite_one_zero]

/-- The amplified uniform attachment is a scaled sum of congruences. -/
theorem amplR_uniformAttach_eq_sum (m : ℕ) (M : Matrix (Fin 2 × S) (Fin 2 × S) ℂ) :
    amplR (uniformAttach (A := S) m) M
      = ((m : ℂ))⁻¹ • ∑ e : Fin m, embR m e * M * (embR m e)ᴴ := by
  ext ⟨r, s, e₁⟩ ⟨r', t, e₂⟩
  show uniformAttach m (refBlock M r r') (s, e₁) (t, e₂) = _
  simp only [uniformAttach_apply, tensorOf_apply, Matrix.smul_apply, Matrix.sum_apply,
    Matrix.one_apply, smul_eq_mul, Matrix.mul_apply, embR, Matrix.of_apply,
    Matrix.conjTranspose_apply, star_ite_one_zero, ite_and, ite_mul, one_mul, zero_mul,
    mul_ite, mul_one, mul_zero,
    Finset.sum_ite_eq', Finset.mem_univ, if_true, refBlock]
  by_cases h : e₁ = e₂
  · subst h
    rw [if_pos rfl, Finset.sum_eq_single e₁]
    · simp [mul_comm]
    · intro b _ hb
      simp [Ne.symm hb]
    · intro h
      exact absurd (Finset.mem_univ _) h
  · rw [if_neg h, Finset.sum_eq_zero]
    · ring
    · intro b _
      by_cases hb : e₁ = b
      · subst hb
        simp [Ne.symm h]
      · simp [hb]

/-- **ATTACH-RUN-DISCARD PRESERVES 2-POSITIVITY.** -/
theorem discardWith_uniform_twoPositive {m : ℕ}
    {Φ : Matrix (S × Fin m) (S × Fin m) ℂ →ₗ[ℂ] Matrix (S × Fin m) (S × Fin m) ℂ}
    (h : IsTwoPositive Φ) :
    IsTwoPositive (discardWith (A := S) m (uniformAttach m) Φ) := by
  intro M hM
  rw [← amplR_eq_ampl2, discardWith, amplR_comp, amplR_comp, amplR_ptraceAncL_eq_sum]
  refine CompositeSoundness.posSemidef_sum _ _ fun e _ => Matrix.PosSemidef.submatrix ?_ _
  have h1 : (amplR (uniformAttach (A := S) m) M).PosSemidef := by
    rw [amplR_uniformAttach_eq_sum]
    exact (CompositeSoundness.posSemidef_sum _ _ fun e _ =>
      hM.mul_mul_conjTranspose_same _).smul (natInv_nonneg m)
  exact h _ h1

end TwoPositive

/-! ### Section B — the round-34 countermodel has iterated ancilla closure -/

/-- **THE DIMENSIONAL COUNTERMODEL HAS ITERATED ANCILLA CLOSURE.** -/
theorem countermodel_iteratedAncillaClosure : IteratedAncillaClosure countermodel := by
  intro n m O _ _ F ⟨h2, htr⟩
  refine ⟨fun a => discardWith_uniform_twoPositive (twoPositive_of_transport _ (h2 a)),
    fun X => ?_⟩
  rw [Finset.sum_congr rfl fun a _ => discardWith_trace (m + 1) _ (F a) X]
  have h := htr (Matrix.reindex (shiftIdx (Fin 2) n (m + 1)) (shiftIdx (Fin 2) n (m + 1))
    (uniformAttach (m + 1) X))
  simp only [transport_reindex, trace_reindex] at h
  rw [h, uniformAttach_trace (m + 1) m.succ_ne_zero]

theorem countermodel_krausSound : KrausSound countermodel :=
  ((exact_iff_sound_and_full _).mp countermodel_exact).1

theorem admissible_krausSound : KrausSound admissibleTheory :=
  ((exact_iff_sound_and_full _).mp admissible_exact).1

/-- The level-two witness is available with a `Fin 1` outcome type. -/
theorem countermodel_reduction2_available_fin1 :
    countermodel.availExt 2 (Fin 1) (fun _ => reduction2 (Fin 2 × Fin 2)) := by
  have h := countermodel.availExt_coarse 2 Unit (Fin 1) _ (fun _ => 0)
    countermodel_reduction2_available
  have hfun : (fun a : Fin 1 => ∑ j ∈ Finset.univ.filter (fun _ : Unit => (0 : Fin 1) = a),
      reduction2 (Fin 2 × Fin 2)) = fun _ => reduction2 (Fin 2 × Fin 2) := by
    funext a
    rw [Finset.filter_true_of_mem (fun _ _ => Subsingleton.elim _ _), Fintype.sum_unique]
  rw [hfun] at h
  exact h

/-- The countermodel is not exactly quantum on composites: its available `Φ₂` is not CP. -/
theorem countermodel_not_exactComposite : ¬ ExactCompositeQuantumOps countermodel := by
  intro h
  have hk := (h 1 1 _).mp countermodel_reduction2_available_fin1
  exact reduction2_not_cp (krausFamily_cp ((isKrausFamily_iff _).mpr hk) 0)

/-! ### Section C — the independence matrix -/

/-- **CLOSURE DOES NOT GIVE INERT SPECTATORS.** -/
theorem closure_not_implies_inert :
    ∃ T : FiniteOperationalTheory (Fin 2),
      KrausSound T ∧ HasCompositeUnitaryControl T ∧ IteratedAncillaClosure T
        ∧ ¬ InertSpectatorCompositionality T :=
  ⟨countermodel, countermodel_krausSound, countermodel_control,
    countermodel_iteratedAncillaClosure, countermodel_not_inert⟩

/-- **INERT SPECTATORS DO NOT GIVE CLOSURE** (round thirty-eight, restated in the matrix
form). -/
theorem inert_not_implies_closure :
    ∃ T : FiniteOperationalTheory (Fin 2),
      KrausSound T ∧ HasCompositeUnitaryControl T ∧ InertSpectatorCompositionality T
        ∧ ¬ IteratedAncillaClosure T :=
  ⟨admissibleTheory, admissible_krausSound, admissible_control, admissible_inert,
    admissible_not_iteratedAncillaClosure⟩

/-- **BOTH TOGETHER ARE SATISFIABLE.** -/
theorem both_satisfiable :
    ∃ T : FiniteOperationalTheory (Fin 2),
      KrausSound T ∧ HasCompositeUnitaryControl T ∧ InertSpectatorCompositionality T
        ∧ IteratedAncillaClosure T :=
  ⟨fullQuantum, ((exact_iff_sound_and_full _).mp fullQuantum_exact).1, fullQuantum_control,
    fullQuantum_inert, fullQuantum_iteratedAncillaClosure⟩

/-- **THE 2 × 2 INDEPENDENCE MATRIX**, in one statement. -/
theorem independence_matrix :
    (∃ T : FiniteOperationalTheory (Fin 2),
      KrausSound T ∧ HasCompositeUnitaryControl T ∧ IteratedAncillaClosure T
        ∧ ¬ InertSpectatorCompositionality T)
    ∧ (∃ T : FiniteOperationalTheory (Fin 2),
      KrausSound T ∧ HasCompositeUnitaryControl T ∧ InertSpectatorCompositionality T
        ∧ ¬ IteratedAncillaClosure T)
    ∧ (∃ T : FiniteOperationalTheory (Fin 2),
      KrausSound T ∧ HasCompositeUnitaryControl T ∧ InertSpectatorCompositionality T
        ∧ IteratedAncillaClosure T) :=
  ⟨closure_not_implies_inert, inert_not_implies_closure, both_satisfiable⟩

/-! ### Section D — realized `H_comp` supplies neither existence principle -/

/-- **REALIZED `H_comp` + CONTROL + INERT SPECTATORS DO NOT GIVE CLOSURE.** -/
theorem hcompRealized_inert_not_implies_closure :
    ∃ T : FiniteOperationalTheory (Fin 2),
      HCompRealized T qutritIdx (id : Equiv.Perm (Fin 3 × (Fin 2 × Fin 2)) → _)
          (fun _ => onesCorr _) (fun _ => onesCorr _) (fun _ => onesCorr _)
        ∧ HasCompositeUnitaryControl T ∧ InertSpectatorCompositionality T
        ∧ ¬ IteratedAncillaClosure T :=
  ⟨admissibleTheory, hCompRealized_ones_of_control admissibleTheory admissible_control qutritIdx id,
    admissible_control, admissible_inert, admissible_not_iteratedAncillaClosure⟩

/-- **REALIZED `H_comp` + CONTROL + CLOSURE DO NOT GIVE INERT SPECTATORS.** -/
theorem hcompRealized_closure_not_implies_inert :
    ∃ T : FiniteOperationalTheory (Fin 2),
      HCompRealized T qutritIdx (id : Equiv.Perm (Fin 3 × (Fin 2 × Fin 2)) → _)
          (fun _ => onesCorr _) (fun _ => onesCorr _) (fun _ => onesCorr _)
        ∧ HasCompositeUnitaryControl T ∧ IteratedAncillaClosure T
        ∧ ¬ InertSpectatorCompositionality T :=
  ⟨countermodel, countermodel_hCompRealized_ones qutritIdx id, countermodel_control,
    countermodel_iteratedAncillaClosure, countermodel_not_inert⟩

/-! ### Section E — neither clause of the endpoint can be deleted -/

/-- Without inert-spectator compositionality the endpoint fails (unconditionally: no isometry
hypothesis is needed to refute an implication). -/
theorem inert_not_deletable :
    ¬ ∀ T : FiniteOperationalTheory (Fin 2),
      KrausSound T → HasCompositeUnitaryControl T → IteratedAncillaClosure T
        → ExactCompositeQuantumOps T :=
  fun h => countermodel_not_exactComposite
    (h countermodel countermodel_krausSound countermodel_control
      countermodel_iteratedAncillaClosure)

/-- Without iterated ancilla closure the endpoint fails. -/
theorem closure_not_deletable :
    ¬ ∀ T : FiniteOperationalTheory (Fin 2),
      KrausSound T → HasCompositeUnitaryControl T → InertSpectatorCompositionality T
        → ExactCompositeQuantumOps T :=
  fun h => admissible_not_exactComposite
    (h admissibleTheory admissible_krausSound admissible_control admissible_inert)

/-! ### Section F — the frozen conditional classification -/

/-- **THE CONDITIONAL CLASSIFICATION.** For a qubit system: system Kraus soundness, full
composite unitary control, inert-spectator compositionality and iterated ancilla closure
give exact finite Kraus operations on every positive composite, against finite isometry
extension (boundary item 2, discharged in round forty-five: `IsometryExtension.lean`) at
`Unit` and at the composite carriers; and the three
witnesses show the two compositional clauses are independent of each other and of the
rest, and jointly satisfiable. -/
theorem conditional_classification :
    (∀ T : FiniteOperationalTheory (Fin 2),
      FiniteIsometryExtensionSF Unit → (∀ k : ℕ, FiniteIsometryExtensionSF (Fin 2 × Fin (k + 1)))
        → KrausSound T → HasCompositeUnitaryControl T → InertSpectatorCompositionality T
        → IteratedAncillaClosure T → ExactCompositeQuantumOps T)
    ∧ (∃ T : FiniteOperationalTheory (Fin 2),
      KrausSound T ∧ HasCompositeUnitaryControl T ∧ IteratedAncillaClosure T
        ∧ ¬ InertSpectatorCompositionality T)
    ∧ (∃ T : FiniteOperationalTheory (Fin 2),
      KrausSound T ∧ HasCompositeUnitaryControl T ∧ InertSpectatorCompositionality T
        ∧ ¬ IteratedAncillaClosure T)
    ∧ (∃ T : FiniteOperationalTheory (Fin 2),
      KrausSound T ∧ HasCompositeUnitaryControl T ∧ InertSpectatorCompositionality T
        ∧ IteratedAncillaClosure T) :=
  ⟨fun T hextU hext hsound hctrl hin hclos =>
      exactComposite_of_conditions T hextU hext hsound hctrl hin hclos,
    closure_not_implies_inert, inert_not_implies_closure, both_satisfiable⟩

#print axioms amplR_transport
#print axioms twoPositive_transport
#print axioms twoPositive_of_transport
#print axioms amplR_ptraceAncL_eq_sum
#print axioms embR_conjTranspose_apply
#print axioms amplR_uniformAttach_eq_sum
#print axioms discardWith_uniform_twoPositive
#print axioms countermodel_iteratedAncillaClosure
#print axioms countermodel_krausSound
#print axioms admissible_krausSound
#print axioms countermodel_reduction2_available_fin1
#print axioms countermodel_not_exactComposite
#print axioms closure_not_implies_inert
#print axioms inert_not_implies_closure
#print axioms both_satisfiable
#print axioms independence_matrix
#print axioms hcompRealized_inert_not_implies_closure
#print axioms hcompRealized_closure_not_implies_inert
#print axioms inert_not_deletable
#print axioms closure_not_deletable
#print axioms conditional_classification

end CompositionalIndependence
end OIBridge
