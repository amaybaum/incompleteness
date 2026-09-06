import OIBridge.PolarizationClosure

/-!
# The coherent-continuum source audit — the strengthened necessary condition

The preregistered pass of `COHERENT-CONTINUUM-SOURCE-AUDIT.md`. Nothing here is named "C5", and
nothing here places `gateFlow` in an implementation class or defines a coupling.

* T1: every intermediate-time point of the layer flow of a moved involution, at `0 < t < 1`, is
  non-monomial (`gateFlow_not_monomial`): its diagonal and moved off-diagonal entries at the moved
  configuration both have nonzero imaginary part.
* T2: the strengthened necessary condition. `NonMonomialCountablyCovered 𝓘 T` says one countable
  set of representatives covers, up to scalar, every non-monomial operator of `𝓘` at `T`;
  `UncountableNonMonomialRays 𝓘 T` is its negation. A class whose generated theory executes a
  layer flow of a moved involution has uncountably many pairwise non-proportional non-monomial
  rays at level one (`uncountableNonMonomialRays_of_layerFlowExecutable`), through T1,
  `gateFlow_not_proportional` and the one-way Kraus bridge. The older condition
  `uncountable_of_layerFlowExecutable` is a consequence (`nonMonomialCountablyCovered_of_countable`)
  and is not superseded.
* T3: the two known failures are orthogonal. Every operator of `substratumClass` is monomial while
  the class is not countably covered up to scalar (`substratumClass_not_countablyCovered`, by the
  real diagonal weights); `PolC` has non-monomial operators and is countably covered
  (`polC_nonMonomialCountablyCovered`); packaged as `known_failures_orthogonal`.
* T4: a real-valued read-write knob has finite operational image
  (`readWriteOperator_range_finite`), with no continuity assumed.
* T5: the canonical gate path has the coherent continuum mathematically
  (`gateFlow_path_coherent_continuum`) and is not sourced by the substratum theory or by any
  configuration-level class (`coherent_continuum_not_sourced`).
* S9: the consistency control — a class whose generated theory is quantum mechanics has the
  uncountable non-monomial rays (`uncountableNonMonomialRays_of_qm`).
-/

namespace OIBridge
namespace CoherentContinuumSource

open Complex Matrix CoherentLift SpectatorBridge OperationalAssembly AncillaClosure
open MonoidalCompletion InterventionLocality MicroReversibility PrimitiveSource LieRankSource
open DiagonalTheory SubstratumInterface StructuralClosure MinimalRepertoire LevelOneSeam
open PhysicalCharacterization RouteB ManuscriptAxioms LiftAudit SubstratumInterfaceAudit
open InstrumentRealization SecondOrderCircuit ExecSource FlowEndpoint DerivedQ3 C5Discovery
open PolarizationClosure Set

/-! ### Section A — T1: intermediate layer-flow points are non-monomial -/

section NonMonomial

variable {S : Type} [Fintype S] [DecidableEq S]

/-- The imaginary part of `exp (π i t)` is `sin (π t)`, positive on `(0, 1)`. -/
theorem exp_im_pos_of_Ioo {t : ℝ} (ht : t ∈ Ioo (0 : ℝ) 1) :
    0 < (Complex.exp (Real.pi * Complex.I * t)).im := by
  have h : (Real.pi : ℂ) * Complex.I * t = ((Real.pi * t : ℝ) : ℂ) * Complex.I := by
    push_cast; ring
  rw [h, Complex.exp_ofReal_mul_I_im]
  exact Real.sin_pos_of_pos_of_lt_pi (mul_pos Real.pi_pos ht.1)
    (mul_lt_of_lt_one_right Real.pi_pos ht.2)

/-- At a moved configuration and an intermediate time, the diagonal and the moved off-diagonal
entries of the gate flow both have nonzero imaginary part. -/
theorem gateFlow_entries_im {σ : Equiv.Perm S} {a : S} (ha : σ a ≠ a) {t : ℝ}
    (ht : t ∈ Ioo (0 : ℝ) 1) :
    (gateFlow σ t a a).im ≠ 0 ∧ (gateFlow σ t (σ a) a).im ≠ 0 := by
  obtain ⟨h1, h2⟩ := gateFlow_entries ha t
  have hpos := exp_im_pos_of_Ioo ht
  rw [h1, h2]
  constructor
  · rw [Complex.div_ofNat_im, Complex.add_im, Complex.one_im, zero_add]
    exact div_ne_zero (ne_of_gt hpos) (by norm_num)
  · rw [Complex.div_ofNat_im, Complex.sub_im, Complex.one_im, zero_sub]
    exact div_ne_zero (neg_ne_zero.mpr (ne_of_gt hpos)) (by norm_num)

/-- **T1 — EVERY INTERMEDIATE-TIME POINT OF THE LAYER FLOW IS NON-MONOMIAL**: for `0 < t < 1`,
one column of `gateFlow σ t` has two nonzero entries. -/
theorem gateFlow_not_monomial {σ : Equiv.Perm S} {a : S} (ha : σ a ≠ a) {t : ℝ}
    (ht : t ∈ Ioo (0 : ℝ) 1) : ¬ IsMonomial (gateFlow σ t) := by
  rintro ⟨τ, d, hK⟩
  obtain ⟨h1, h2⟩ := gateFlow_entries_im ha ht
  rw [hK, monomial_entry] at h1 h2
  by_cases hτ : τ a = a
  · rw [if_neg (by rw [hτ]; exact Ne.symm ha), Complex.zero_im] at h2
    exact h2 rfl
  · rw [if_neg hτ, Complex.zero_im] at h1
    exact h1 rfl

/-- A nonzero scalar multiple of a matrix is monomial only if the matrix is. -/
theorem isMonomial_of_smul {c : ℂ} (hc : c ≠ 0) {K : Matrix S S ℂ} (h : IsMonomial (c • K)) :
    IsMonomial K := by
  obtain ⟨σ, d, hK⟩ := h
  refine ⟨σ, c⁻¹ • d, ?_⟩
  have : K = c⁻¹ • (c • K) := by rw [smul_smul, inv_mul_cancel₀ hc, one_smul]
  rw [this, hK, ← Matrix.mul_smul, Matrix.diagonal_smul]

/-- **THE CANONICAL PATH IS NOT COUNTABLY COVERED UP TO SCALAR ON `(0, 1)`**: no countable set of
matrices carries, up to scalar, the gate flow of a moved involution at every intermediate time. -/
theorem gateFlow_not_countablyCovered {σ : Equiv.Perm S} {a : S} (ha : σ a ≠ a)
    (D : Set (Matrix S S ℂ)) (hD : D.Countable) :
    ¬ ∀ t ∈ Ioo (0 : ℝ) 1, ∃ (c : ℂ) (M : Matrix S S ℂ), M ∈ D ∧ gateFlow σ t = c • M := by
  intro hcov
  have hray : ∀ t : ℝ, ∃ M : Matrix S S ℂ,
      t ∈ Ioo (0 : ℝ) 1 → M ∈ D ∧ ∃ d : ℂ, gateFlow σ t = d • M := by
    intro t
    by_cases ht : t ∈ Ioo (0 : ℝ) 1
    · obtain ⟨c, M, hM, hcM⟩ := hcov t ht
      exact ⟨M, fun _ => ⟨hM, c, hcM⟩⟩
    · exact ⟨0, fun h => absurd h ht⟩
  choose f hf using hray
  have hinj : InjOn f (Ioo (0 : ℝ) 1) := by
    intro t ht t' ht' hft
    by_contra hne
    obtain ⟨-, d, hd⟩ := hf t ht
    obtain ⟨-, d', hd'⟩ := hf t' ht'
    have hd'0 : d' ≠ 0 := by
      rintro rfl
      have := (gateFlow_entries_im ha ht').1
      rw [hd', zero_smul, Matrix.zero_apply, Complex.zero_im] at this
      exact this rfl
    have ht2 : t ∈ Ico (0 : ℝ) 2 := ⟨le_of_lt ht.1, by linarith [ht.2]⟩
    have ht2' : t' ∈ Ico (0 : ℝ) 2 := ⟨le_of_lt ht'.1, by linarith [ht'.2]⟩
    apply gateFlow_not_proportional ha ht2 ht2' hne (d * d'⁻¹)
    rw [hd, hft, hd', smul_smul, mul_assoc, inv_mul_cancel₀ hd'0, mul_one]
  have hmaps : MapsTo f (Ioo (0 : ℝ) 1) D := fun t ht => (hf t ht).1
  have hcount : (Ioo (0 : ℝ) 1).Countable := hmaps.countable_of_injOn hinj hD
  have := Cardinal.le_aleph0_iff_set_countable.mpr hcount
  rw [Cardinal.mk_Ioo_real (by norm_num : (0 : ℝ) < 1)] at this
  exact absurd this (not_le.mpr Cardinal.aleph0_lt_continuum)

end NonMonomial

/-! ### Section B — T2: the strengthened necessary condition -/

section Strengthened

/-- **COUNTABLE COVER OF THE NON-MONOMIAL SECTOR**: one countable set of representatives carries,
up to scalar, every non-monomial operator of the class at the carrier. -/
def NonMonomialCountablyCovered (𝓘 : ImplementationClass) (T : Type) [Fintype T] [DecidableEq T] :
    Prop :=
  ∃ D : Set (Matrix T T ℂ), D.Countable ∧
    ∀ K : Matrix T T ℂ, 𝓘 T K → ¬ IsMonomial K →
      ∃ (c : ℂ) (M : Matrix T T ℂ), M ∈ D ∧ K = c • M

/-- **UNCOUNTABLY MANY NON-MONOMIAL RAYS**: the non-monomial sector of the class at the carrier is
not countably covered up to scalar. -/
def UncountableNonMonomialRays (𝓘 : ImplementationClass) (T : Type) [Fintype T] [DecidableEq T] :
    Prop :=
  ¬ NonMonomialCountablyCovered 𝓘 T

/-- A countable cover of the whole class covers its non-monomial sector: the strengthened
condition implies the condition of the closure audit, which is therefore not superseded. -/
theorem nonMonomialCountablyCovered_of_countable {𝓘 : ImplementationClass} {T : Type} [Fintype T]
    [DecidableEq T]
    (h : ∃ D : Set (Matrix T T ℂ), D.Countable ∧
      ∀ K : Matrix T T ℂ, 𝓘 T K → ∃ (c : ℂ) (M : Matrix T T ℂ), M ∈ D ∧ K = c • M) :
    NonMonomialCountablyCovered 𝓘 T := by
  obtain ⟨D, hD, hmem⟩ := h
  exact ⟨D, hD, fun K hK _ => hmem K hK⟩

variable {S : Type} [Fintype S] [DecidableEq S]

/-- **T2 — LAYER-FLOW EXECUTABILITY FORCES UNCOUNTABLY MANY NON-MONOMIAL RAYS AT LEVEL ONE**: for
a moved involution, the intermediate-time points of its flow are non-monomial (T1), pairwise
non-proportional, and, by the one-way bridge, present in the class up to nonzero scalar; a
countable cover of the non-monomial sector would then cover the path. -/
theorem uncountableNonMonomialRays_of_layerFlowExecutable {𝓘 : ImplementationClass}
    (arch : Architecture 𝓘) {σ : Equiv.Perm S} {x : S} (hx : σ x ≠ x)
    (hex : LayerFlowExecutable (genTheory 𝓘 arch S) σ) :
    UncountableNonMonomialRays 𝓘 (S × Fin 1) := by
  rintro ⟨D, hD, hmem⟩
  have : Nonempty S := ⟨x⟩
  have hx' : levelPerm σ 1 (x, 0) ≠ (x, 0) := by
    rw [levelPerm_apply]
    intro hc
    exact hx (Prod.mk.inj hc).1
  apply gateFlow_not_countablyCovered hx' D hD
  intro t ht
  obtain ⟨c, hc0, hcK⟩ := exists_scaled_mem_of_instAvail_unitary arch (hex 1 t)
  have hnm : ¬ IsMonomial (c • gateFlow (levelPerm σ 1) t) :=
    fun h => gateFlow_not_monomial hx' ht (isMonomial_of_smul hc0 h)
  obtain ⟨c', M, hM, hKM⟩ := hmem _ hcK hnm
  refine ⟨c⁻¹ * c', M, hM, ?_⟩
  calc gateFlow (levelPerm σ 1) t = c⁻¹ • (c • gateFlow (levelPerm σ 1) t) := by
        rw [smul_smul, inv_mul_cancel₀ hc0, one_smul]
    _ = c⁻¹ • (c' • M) := by rw [hKM]
    _ = (c⁻¹ * c') • M := by rw [smul_smul]

/-- **THE CONTRAPOSITIVE**: a class whose non-monomial sector at level one is countably covered
generates no theory executing a layer flow of a moved involution. -/
theorem not_layerFlowExecutable_of_nonMonomialCountablyCovered {𝓘 : ImplementationClass}
    (arch : Architecture 𝓘) {σ : Equiv.Perm S} {x : S} (hx : σ x ≠ x)
    (h : NonMonomialCountablyCovered 𝓘 (S × Fin 1)) :
    ¬ LayerFlowExecutable (genTheory 𝓘 arch S) σ :=
  fun hex => uncountableNonMonomialRays_of_layerFlowExecutable arch hx hex h

/-- **S9, THE CONSISTENCY CONTROL**: a class whose generated theory on two configurations is exact
finite operational quantum mechanics has uncountably many non-monomial rays at level one. -/
theorem uncountableNonMonomialRays_of_qm {𝓘 : ImplementationClass} (arch : Architecture 𝓘)
    (h : ExactAllFiniteEndomorphicQuantumOps (genTheory 𝓘 arch (Fin 2))) :
    UncountableNonMonomialRays 𝓘 (Fin 2 × Fin 1) := by
  have hσ : ∀ x : Fin 2, Equiv.swap (0 : Fin 2) 1 (Equiv.swap 0 1 x) = x :=
    fun x => Equiv.swap_apply_self _ _ _
  exact uncountableNonMonomialRays_of_layerFlowExecutable arch (x := (0 : Fin 2)) (by simp)
    (derivedOI_layerFlowExecutable_of_qm _ h hσ).2

end Strengthened

/-! ### Section C — T3: the two known failures are orthogonal -/

section Orthogonal

variable {T : Type} [Fintype T] [DecidableEq T]

/-- Every operator of the substratum class is monomial: the coherent part fails maximally. -/
theorem substratumClass_monomial (K : Matrix T T ℂ) (h : substratumClass T K) : IsMonomial K := h

/-- A diagonal weight on one configuration: real weight `r` at `a`, weight one elsewhere. -/
noncomputable def weightGate (a : T) (r : ℝ) : Matrix T T ℂ :=
  Matrix.diagonal fun s => if s = a then (r : ℂ) else 1

theorem weightGate_mem (a : T) (r : ℝ) : substratumClass T (weightGate a r) :=
  monomial_diagonal _

omit [Fintype T] in
/-- Distinct weights at `a` are never proportional, given a second configuration `b`. -/
theorem weightGate_not_proportional {a b : T} (hab : a ≠ b) {r r' : ℝ} (hrr : r ≠ r') (c : ℂ) :
    weightGate a r ≠ c • weightGate a r' := by
  intro h
  have e1 := congrFun (congrFun h b) b
  have e2 := congrFun (congrFun h a) a
  simp only [weightGate, Matrix.smul_apply, Matrix.diagonal_apply_eq, if_neg (Ne.symm hab),
    if_true, smul_eq_mul, mul_one] at e1 e2
  rw [← e1, one_mul] at e2
  exact hrr (Complex.ofReal_injective e2)

/-- **T3 — THE SUBSTRATUM CLASS IS NOT COUNTABLY COVERED UP TO SCALAR**, on any carrier with two
configurations: its diagonal weights already range over a continuum. -/
theorem substratumClass_not_countablyCovered {a b : T} (hab : a ≠ b) :
    ¬ ∃ D : Set (Matrix T T ℂ), D.Countable ∧
      ∀ K : Matrix T T ℂ, substratumClass T K →
        ∃ (c : ℂ) (M : Matrix T T ℂ), M ∈ D ∧ K = c • M := by
  rintro ⟨D, hD, hmem⟩
  have hray : ∀ r : ℝ, ∃ M ∈ D, ∃ d : ℂ, weightGate a r = d • M := by
    intro r
    obtain ⟨c, M, hM, hcM⟩ := hmem _ (weightGate_mem a r)
    exact ⟨M, hM, c, hcM⟩
  choose f hfD hf using hray
  have hinj : InjOn f (Ioo (0 : ℝ) 1) := by
    intro r _ r' _ hfr
    by_contra hne
    obtain ⟨d, hd⟩ := hf r
    obtain ⟨d', hd'⟩ := hf r'
    have hd'0 : d' ≠ 0 := by
      rintro rfl
      have := congrFun (congrFun hd' b) b
      simp [weightGate, Ne.symm hab] at this
    apply weightGate_not_proportional hab hne (d * d'⁻¹)
    rw [hd, hfr, hd', smul_smul, mul_assoc, inv_mul_cancel₀ hd'0, mul_one]
  have hmaps : MapsTo f (Ioo (0 : ℝ) 1) D := fun r _ => hfD r
  have hcount : (Ioo (0 : ℝ) 1).Countable := hmaps.countable_of_injOn hinj hD
  have := Cardinal.le_aleph0_iff_set_countable.mpr hcount
  rw [Cardinal.mk_Ioo_real (by norm_num : (0 : ℝ) < 1)] at this
  exact absurd this (not_le.mpr Cardinal.aleph0_lt_continuum)

/-- **T3 — THE LABEL-INVARIANT POLARIZED CLASS IS COUNTABLY COVERED**, its non-monomial sector
included: the cardinality part fails. -/
theorem polC_nonMonomialCountablyCovered : NonMonomialCountablyCovered PolC T :=
  nonMonomialCountablyCovered_of_countable (polC_countable_upToScalar T)

/-- **T3 — THE TWO KNOWN FAILURES ARE ORTHOGONAL**, on the level-one carrier of two
configurations: the substratum class is all monomial and not countably covered; the polarized
class has a non-monomial operator and is countably covered. -/
theorem known_failures_orthogonal :
    (∀ K : Matrix (Fin 2 × Fin 1) (Fin 2 × Fin 1) ℂ, substratumClass (Fin 2 × Fin 1) K → IsMonomial K)
    ∧ (¬ ∃ D : Set (Matrix (Fin 2 × Fin 1) (Fin 2 × Fin 1) ℂ), D.Countable ∧
        ∀ K : Matrix (Fin 2 × Fin 1) (Fin 2 × Fin 1) ℂ, substratumClass (Fin 2 × Fin 1) K →
          ∃ (c : ℂ) (M : Matrix (Fin 2 × Fin 1) (Fin 2 × Fin 1) ℂ), M ∈ D ∧ K = c • M)
    ∧ (∃ K : Matrix (Fin 2 × Fin 1) (Fin 2 × Fin 1) ℂ, PolC (Fin 2 × Fin 1) K ∧ ¬ IsMonomial K)
    ∧ NonMonomialCountablyCovered PolC (Fin 2 × Fin 1) :=
  ⟨fun K h => substratumClass_monomial K h,
    substratumClass_not_countablyCovered (a := ((0 : Fin 2), (0 : Fin 1))) (b := (1, 0)) (by decide),
    ⟨siteSwapImage 1, PolC.swap 1, siteSwapImage_not_monomial 1 0⟩,
    polC_nonMonomialCountablyCovered⟩

end Orthogonal

/-! ### Section D — T4: a real-valued read-write knob has finite operational image -/

section ReadWrite

variable {S : Type} [Fintype S] [DecidableEq S]

/-- **T4 — THE READ-WRITE OPERATOR HAS FINITE RANGE**: every value of the real parameter is a
permutation matrix of the finite carrier; no continuity of the family is assumed. -/
theorem readWriteOperator_range_finite {a b : S} (F : ReadWriteControl.ReadWriteFamily a b) :
    (Set.range (ReadWriteControl.readWriteOperator F)).Finite := by
  refine (Set.finite_range (permMatrix : Equiv.Perm S → Matrix S S ℂ)).subset ?_
  rintro _ ⟨l, rfl⟩
  exact ⟨F.couple l, (ReadWriteControl.readWriteOperator_eq_perm F l).symm⟩

/-- **UNCOUNTABLE PARAMETER DOMAIN, FINITE OPERATIONAL IMAGE, MONOMIAL THROUGHOUT.** -/
theorem readWrite_parameter_uncountable_image_finite {a b : S}
    (F : ReadWriteControl.ReadWriteFamily a b) :
    ¬ (Set.univ : Set ℝ).Countable
    ∧ (Set.range (ReadWriteControl.readWriteOperator F)).Finite
    ∧ ∀ l : ℝ, IsMonomial (ReadWriteControl.readWriteOperator F l) :=
  ⟨Cardinal.not_countable_real, readWriteOperator_range_finite F,
    fun l => ReadWriteControl.readWriteOperator_monomial F l⟩

end ReadWrite

/-! ### Section E — T5: the canonical path has the coherent continuum and is not sourced -/

section Path

variable {S : Type} [Fintype S] [DecidableEq S]

/-- **T5 — THE CANONICAL GATE PATH HAS THE COHERENT CONTINUUM, MATHEMATICALLY**: every
intermediate-time point is non-monomial and the path is not countably covered up to scalar. This
is a statement about `gateFlow`, not about availability. -/
theorem gateFlow_path_coherent_continuum {σ : Equiv.Perm S} {a : S} (ha : σ a ≠ a) :
    (∀ t ∈ Ioo (0 : ℝ) 1, ¬ IsMonomial (gateFlow σ t))
    ∧ ¬ ∃ D : Set (Matrix S S ℂ), D.Countable ∧
        ∀ t ∈ Ioo (0 : ℝ) 1, ∃ (c : ℂ) (M : Matrix S S ℂ), M ∈ D ∧ gateFlow σ t = c • M :=
  ⟨fun _ ht => gateFlow_not_monomial ha ht,
    fun ⟨D, hD, hcov⟩ => gateFlow_not_countablyCovered ha D hD hcov⟩

/-- **T5 — THE CONTINUUM EXISTS AND IS NOT SOURCED**: the level-one path of a moved involution
has the coherent continuum, the substratum theory executes no layer flow of it, and no
configuration-level class makes even its half-time point available. -/
theorem coherent_continuum_not_sourced {σ : Equiv.Perm S} {x : S} (hx : σ x ≠ x) :
    ((∀ t ∈ Ioo (0 : ℝ) 1, ¬ IsMonomial (gateFlow (levelPerm σ 1) t))
      ∧ ¬ ∃ D : Set (Matrix (S × Fin 1) (S × Fin 1) ℂ), D.Countable ∧
          ∀ t ∈ Ioo (0 : ℝ) 1, ∃ (c : ℂ) (M : Matrix (S × Fin 1) (S × Fin 1) ℂ),
            M ∈ D ∧ gateFlow (levelPerm σ 1) t = c • M)
    ∧ ¬ LayerFlowExecutable (substratumTheory S) σ
    ∧ ∀ (𝓘 : ImplementationClass) (arch : Architecture 𝓘), ConfigurationLevel 𝓘 →
        ¬ (genTheory 𝓘 arch S).availExt 1 Unit
          (fun _ => conjChannel (gateFlow (levelPerm σ 1) (1 / 2 : ℝ))) := by
  have hx' : levelPerm σ 1 (x, 0) ≠ (x, 0) := by
    rw [levelPerm_apply]
    intro hc
    exact hx (Prod.mk.inj hc).1
  exact ⟨gateFlow_path_coherent_continuum hx', substratumTheory_not_layerFlowExecutable hx,
    fun 𝓘 arch h => configurationLevel_not_avail_gateFlow_half arch h hx⟩

end Path

end CoherentContinuumSource
end OIBridge

#print axioms OIBridge.CoherentContinuumSource.gateFlow_entries_im
#print axioms OIBridge.CoherentContinuumSource.gateFlow_not_monomial
#print axioms OIBridge.CoherentContinuumSource.isMonomial_of_smul
#print axioms OIBridge.CoherentContinuumSource.gateFlow_not_countablyCovered
#print axioms OIBridge.CoherentContinuumSource.nonMonomialCountablyCovered_of_countable
#print axioms OIBridge.CoherentContinuumSource.uncountableNonMonomialRays_of_layerFlowExecutable
#print axioms OIBridge.CoherentContinuumSource.not_layerFlowExecutable_of_nonMonomialCountablyCovered
#print axioms OIBridge.CoherentContinuumSource.uncountableNonMonomialRays_of_qm
#print axioms OIBridge.CoherentContinuumSource.substratumClass_monomial
#print axioms OIBridge.CoherentContinuumSource.weightGate_not_proportional
#print axioms OIBridge.CoherentContinuumSource.substratumClass_not_countablyCovered
#print axioms OIBridge.CoherentContinuumSource.polC_nonMonomialCountablyCovered
#print axioms OIBridge.CoherentContinuumSource.known_failures_orthogonal
#print axioms OIBridge.CoherentContinuumSource.readWriteOperator_range_finite
#print axioms OIBridge.CoherentContinuumSource.readWrite_parameter_uncountable_image_finite
#print axioms OIBridge.CoherentContinuumSource.gateFlow_path_coherent_continuum
#print axioms OIBridge.CoherentContinuumSource.coherent_continuum_not_sourced
