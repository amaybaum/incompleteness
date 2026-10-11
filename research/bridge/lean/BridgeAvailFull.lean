/-
  OIBridge/BridgeAvailFull.lean — design module of the research thread `research/bridge`
  (round 4, node B14, the coordinator's third addendum). Not certified. Built on a disposable dev
  branch only; not for merge.

  The full-model check for B14's verdict. Every statement here is about operational availability
  in the kernel's protocols (`InstAvail`); none is about the invariance of a pair cone.

    §A  the fourth-root lattice class `latticeClass`: every submonomial operator any two of whose
        nonzero entries have equal fourth powers. It is an architecture, context-stable,
        label-invariant, dagger-stable, unitary-ray saturated, structurally closed and
        configuration-level; it contains the stated access (`permClass`), the stated access with
        the quarter phase (`MixR ∅`) and every quarter phase; it lies in the monomial interface;
    §B  the rows its theory satisfies, each by the kernel's own derivation: `DerivedOI` on every
        carrier; the sealed core and `DerivedOICore` on the two-state carrier; implementation
        locality, plain and reversible; embedded observation; parallel and qutrit reference
        extension; both forms of observational independence; inert spectators; validity; iterated
        ancilla closure; observer recursion; the level-one seam; well-formedness; inverse
        accessibility;
    §C  the decision in the lattice theory: neither `R_z(θ₀)` nor `J` is available on the pair or on
        the token at any positive level; the quarter phase is available on the pair (positive
        control); the monomial interface contains the class and supplies `R_z(θ₀)` (countercontrol);
    §D  the rows it fails, each of which supplies the operations: composite unitary control gives
        both pair operators at every level (`pairAvail_of_control`); quantum mechanics, phase-free
        richness, layer-flow executability, elementary drivability and the quantum architecture
        fail;
    §E  level H: for every kernel substratum, whatever its rule, an operator diagonal in the
        configurations with the values `1` and `w` at two configurations, and an operator with two
        nonzero entries in one row, are unavailable in its observer theory at every level.

  Nothing here sources an operation, a pair cone, (A) or the transfer clause.

  Kernel check (dev branch):  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.BridgeAvail
import OIBridge.LiftAudit
import OIBridge.ManuscriptAxioms
import OIBridge.EmbeddedObservation
import OIBridge.MinimalRepertoire
import OIBridge.CompletedOI
import OIBridge.CarrierGeneralOIPlus
import OIBridge.ReferenceExtension
import OIBridge.SpectatorBridge
import OIBridge.PhysicalCharacterization
import OIBridge.GeneralCarrier
import OIBridge.LevelOneSeam
import OIBridge.OperationalValidity
import OIBridge.AncillaClosure
import OIBridge.ReadWriteControl
import OIBridge.SubstratumSource
import OIBridge.LieRankSource

namespace OIBridge
namespace BridgeAvailFull

open Matrix MonoidalCompletion InterventionLocality StructuralClosure SubstratumInterface
  SubstratumInterfaceAudit StateMixingCoupling RouteB OIRealization MicroReversibility BridgeAvail
  OperationalAssembly ReferenceExtension

/-! ### §A — the fourth-root lattice class -/

/-- **THE FOURTH-ROOT LATTICE CLASS**: every submonomial operator any two of whose nonzero entries
have equal fourth powers. -/
abbrev latticeClass : ImplementationClass := fun _ _ _ K => IsSubmonomial K ∧ QuartEq K

theorem lq_mul {T : Type} [Fintype T] {K L : Matrix T T ℂ} (hKs : IsSubmonomial K)
    (hK : QuartEq K) (hL : QuartEq L) : QuartEq (K * L) := by
  intro i j k l h1 h2
  obtain ⟨m, hm1, hm2⟩ := mul_entry_ne_zero h1
  obtain ⟨m', hm1', hm2'⟩ := mul_entry_ne_zero h2
  rw [submonomial_mul_apply hKs hm1, submonomial_mul_apply hKs hm1', mul_pow, mul_pow,
    hK i m k m' hm1 hm1', hL m j m' l hm2 hm2']

theorem lq_smul {T : Type} (a : ℂ) {K : Matrix T T ℂ} (hK : QuartEq K) : QuartEq (a • K) := by
  intro i j k l h1 h2
  simp only [Matrix.smul_apply, smul_eq_mul] at h1 h2 ⊢
  rw [mul_pow, mul_pow, hK i j k l (mul_ne_zero_iff.mp h1).2 (mul_ne_zero_iff.mp h2).2]

theorem lq_block {T : Type} [Fintype T] [DecidableEq T] {m : ℕ}
    {K : Matrix (T × Fin m) (T × Fin m) ℂ} (hK : QuartEq K) (f e : Fin m) :
    QuartEq (AncillaClosure.ancBlock K f e) :=
  fun i j k l h1 h2 => hK (i, f) (j, e) (k, f) (l, e) h1 h2

theorem lq_reindex {T T' : Type} (e : T ≃ T') {K : Matrix T T ℂ} (hK : QuartEq K) :
    QuartEq (Matrix.reindex e e K) := by
  intro i j k l h1 h2
  simp only [Matrix.reindex_apply, Matrix.submatrix_apply] at h1 h2 ⊢
  exact hK _ _ _ _ h1 h2

theorem lq_conjTranspose {T : Type} {K : Matrix T T ℂ} (hK : QuartEq K) : QuartEq Kᴴ := by
  intro i j k l h1 h2
  simp only [Matrix.conjTranspose_apply] at h1 h2 ⊢
  rw [← star_pow, ← star_pow, hK j i l k (star_ne_zero.mp h1) (star_ne_zero.mp h2)]

/-- **(1) ARCHITECTURE.** -/
theorem latticeClass_arch : Architecture latticeClass where
  one := fun _ _ _ => ⟨submonomial_one, quart_of_ones one_entries_one⟩
  mul := fun _ _ _ _ _ hK hL => ⟨submonomial_mul hK.1 hL.1, lq_mul hK.1 hK.2 hL.2⟩
  smul := fun _ _ _ a _ _ hK => ⟨submonomial_smul a hK.1, lq_smul a hK.2⟩
  proj := fun _ _ _ _ _ => ⟨submonomial_diagonal _, quart_of_scaled (scaled_diagonal_indicator _)⟩
  block := fun _ _ _ _ _ f e hK => ⟨submonomial_block hK.1 f e, lq_block hK.2 f e⟩

/-- **(2) CONTEXT STABILITY.** -/
theorem latticeClass_contextStable : ContextStable latticeClass :=
  fun _ _ _ _ _ _ _ hK =>
    ⟨submonomial_tensor_one hK.1, quart_tensorOf (quart_of_ones one_entries_one) hK.2⟩

/-- **(3) LABEL INVARIANCE.** -/
theorem latticeClass_labelInvariant : LabelInvariant latticeClass :=
  fun _ _ _ _ _ _ e _ hK => ⟨submonomial_reindex e hK.1, lq_reindex e hK.2⟩

/-- **(4) DAGGER STABILITY.** -/
theorem latticeClass_daggerStable : DaggerStable latticeClass :=
  fun _ _ _ _ hK => ⟨submonomial_conjTranspose hK.1, lq_conjTranspose hK.2⟩

/-- **UNITARY-RAY SATURATION**: both conditions are invariant under a nonzero rescaling. -/
theorem latticeClass_unitaryRaySaturated : UnitaryRaySaturated latticeClass := by
  intro S _ _ c V hc _ h
  have h1 := submonomial_smul c⁻¹ h.1
  have h2 := lq_smul c⁻¹ h.2
  rw [smul_smul, inv_mul_cancel₀ hc, one_smul] at h1 h2
  exact ⟨h1, h2⟩

theorem latticeClass_structurallyClosed : StructurallyClosed latticeClass :=
  ⟨latticeClass_arch, latticeClass_contextStable, latticeClass_labelInvariant,
    latticeClass_daggerStable⟩

theorem latticeClass_quartLattice : QuartLattice latticeClass := fun _ _ _ _ h => h

/-- **CONFIGURATION LEVEL**: every member is monomial. -/
theorem latticeClass_configurationLevel : ManuscriptAxioms.ConfigurationLevel latticeClass :=
  fun _ _ _ _ h => submonomial_monomial h.1

/-- The stated access lies in the class. -/
theorem permClass_le_lattice :
    ∀ (S : Type) [Fintype S] [DecidableEq S] (K : Matrix S S ℂ), permClass S K → latticeClass S K :=
  fun S _ _ K h => permClass_quartLattice S K h

/-- The stated access with the quarter phase lies in the class. -/
theorem mixEmpty_le_lattice :
    ∀ (S : Type) [Fintype S] [DecidableEq S] (K : Matrix S S ℂ),
      MixR (∅ : Set ℝ) S K → latticeClass S K :=
  fun S _ _ K h => mixEmpty_quartLattice S K h

/-- The class lies in the monomial interface. -/
theorem lattice_le_substratum :
    ∀ (S : Type) [Fintype S] [DecidableEq S] (K : Matrix S S ℂ),
      latticeClass S K → substratumClass S K :=
  fun _ _ _ _ h => submonomial_monomial h.1

/-- Every quarter phase, at every carrier, lies in the class. -/
theorem phaseGate_lattice {S : Type} [Fintype S] [DecidableEq S] (p : S) :
    latticeClass S (LieRankSource.phaseGate p) := by
  refine ⟨?_, phaseGate_quart p⟩
  unfold LieRankSource.phaseGate
  exact submonomial_diagonal _

/-! ### §B — the theory of the class and the rows it satisfies -/

/-- **THE LATTICE THEORY** on a carrier. -/
noncomputable abbrev latticeTheory (A : Type) [Fintype A] [DecidableEq A] :
    FiniteOperationalTheory A :=
  genTheory latticeClass latticeClass_arch A

section Rows

variable (A : Type) [Fintype A] [DecidableEq A]

/-- **`DerivedOI` ON EVERY CARRIER**: the kernel's derivation of `derivedOI_of_stated`
(StateMixingCoupling.lean:463), with the quarter phases of the class at every carrier. -/
theorem latticeTheory_derivedOI : DerivedOI (latticeTheory A) :=
  ⟨genTheory_reversibleImplementationLocality latticeClass latticeClass_arch
      latticeClass_contextStable latticeClass_labelInvariant latticeClass_daggerStable,
    genTheory_embeddedObservation latticeClass latticeClass_arch latticeClass_labelInvariant,
    fun _ a b => SubstratumSource.genTheory_avail_conj latticeClass_arch
      (permClass_le_lattice _ _ (permClass_permMatrix (Equiv.swap a b)))
      (SpectatorBridge.permMatrix_isometry _),
    fun _ a => SubstratumSource.genTheory_avail_conj latticeClass_arch (phaseGate_lattice a)
      (LieRankSource.phaseGate_unitary a),
    fun _ _ _ F l => by
      rw [ReadWriteControl.readWriteOperator_eq_perm]
      exact SubstratumSource.genTheory_avail_conj latticeClass_arch
        (permClass_le_lattice _ _ (permClass_permMatrix (F.couple l)))
        (SpectatorBridge.permMatrix_isometry _)⟩

theorem latticeTheory_implementationLocality : ImplementationLocality (latticeTheory A) :=
  genTheory_implementationLocality latticeClass latticeClass_arch latticeClass_contextStable
    latticeClass_labelInvariant

theorem latticeTheory_reversibleImplementationLocality :
    ReversibleImplementationLocality (latticeTheory A) :=
  genTheory_reversibleImplementationLocality latticeClass latticeClass_arch
    latticeClass_contextStable latticeClass_labelInvariant latticeClass_daggerStable

theorem latticeTheory_embeddedObservation : PrimitiveSource.EmbeddedObservation (latticeTheory A) :=
  genTheory_embeddedObservation latticeClass latticeClass_arch latticeClass_labelInvariant

theorem latticeTheory_closure : AncillaClosure.IteratedAncillaClosure (latticeTheory A) :=
  PrimitiveSource.closure_of_embeddedObservation (latticeTheory_embeddedObservation A)

theorem latticeTheory_observerRecursion : OIHierarchy.ObserverRecursion (latticeTheory A) :=
  PrimitiveSource.observerRecursion_of_embeddedObservation (latticeTheory_embeddedObservation A)

theorem latticeTheory_systemToLevelOne : LevelOneSeam.SystemToLevelOne (latticeTheory A) :=
  PrimitiveSource.systemToLevelOne_of_embeddedObservation (latticeTheory_embeddedObservation A)

variable [Nonempty A]

theorem latticeTheory_parallel : HasParallelReferenceExtension (latticeTheory A) :=
  parallel_of_implementationLocal (genTheory_generated latticeClass latticeClass_arch)
    latticeClass_contextStable latticeClass_labelInvariant

theorem latticeTheory_observationalIndependence :
    OIHierarchyGeneral.ObservationalIndependence (latticeTheory A) :=
  observationalIndependence_of_implementationLocality (latticeTheory_implementationLocality A)

theorem latticeTheory_inert : SpectatorBridge.InertSpectatorCompositionality (latticeTheory A) :=
  (SpectatorBridge.inertSpectator_iff_parallelReferenceExtension (latticeTheory A)).mpr
    (latticeTheory_parallel A)

theorem latticeTheory_validity :
    OperationalValidity.CompositeOperationalValidity (latticeTheory A) :=
  validity_of_implementationLocality (latticeTheory_implementationLocality A)

theorem latticeTheory_wellFormed : GeneralCarrier.WellFormed (latticeTheory A) :=
  ⟨latticeTheory_validity A, latticeTheory_systemToLevelOne A⟩

/-- **INVERSE ACCESSIBILITY**, from dagger stability under unitary-ray saturation
(MicroscopicReversibility.lean:283). -/
theorem latticeTheory_inverseAccessibility : InverseAccessibility (latticeTheory A) :=
  inverseAccessibility_of_generated_daggerStable latticeClass_arch
    (genTheory_generated latticeClass latticeClass_arch) latticeClass_daggerStable
    latticeClass_unitaryRaySaturated

end Rows

/-- **THE SEALED CORE** on the two-state carrier, carried from the stated access
(`permTheory_realizesSealedOICore`, SubstratumInterfaceAudit.lean:740) along the class inclusion. -/
theorem latticeTheory_realizesSealedOICore : RealizesSealedOICore (latticeTheory (Fin 2)) := by
  obtain ⟨h1, h2, h3, h4, h5, h6⟩ := permTheory_realizesSealedOICore
  refine ⟨h1, genTheory_mono permClass permClass_arch latticeClass_arch permClass_le_lattice 4 _ h2,
    genTheory_mono permClass permClass_arch latticeClass_arch permClass_le_lattice 4 _ h3, ?_,
    genTheory_mono permClass permClass_arch latticeClass_arch permClass_le_lattice 4 _ h5, h6⟩
  first
  | exact h4
  | exact fun r => by rw [readVisible_eq_localLuders, readout_is_localLuders]

theorem latticeTheory_oiCore : OIHierarchy.OICore (latticeTheory (Fin 2)) :=
  latticeTheory_realizesSealedOICore

/-- **THE CLOSURE WITH THE CORE**, `DerivedOICore`, on the two-state carrier. -/
theorem latticeTheory_derivedOICore : DerivedOICore (latticeTheory (Fin 2)) :=
  ⟨latticeTheory_derivedOI (Fin 2), latticeTheory_realizesSealedOICore⟩

theorem latticeTheory_qubitObservationalIndependence :
    OIHierarchy.ObservationalIndependence (latticeTheory (Fin 2)) :=
  latticeTheory_parallel (Fin 2)

theorem latticeTheory_qutrit : HasQutritReferenceExtension (latticeTheory (Fin 2)) :=
  qutrit_of_parallel (latticeTheory (Fin 2)) (latticeTheory_parallel (Fin 2))

/-! ### §C — the decision in the lattice theory, with its controls -/

/-- **THE LATTICE THEORY REFUTES BOTH**, on the pair and on the token, at every positive level. -/
theorem lattice_refutes {n : ℕ} (hn : 0 < n) :
    ¬ PairAvailAt latticeClass latticeClass_arch zPh n
      ∧ ¬ PairAvailAt latticeClass latticeClass_arch uJ n
      ∧ ¬ TokenAvailAt latticeClass latticeClass_arch zPh n
      ∧ ¬ TokenAvailAt latticeClass latticeClass_arch uJ n :=
  ⟨not_pairAvail_zPh_of_lattice latticeClass_arch latticeClass_quartLattice hn,
    not_pairAvail_uJ_of_submonomial latticeClass_arch (fun _ _ _ _ h => h.1) hn,
    not_tokenAvail_zPh_of_lattice latticeClass_arch latticeClass_quartLattice hn,
    not_tokenAvail_uJ_of_submonomial latticeClass_arch (fun _ _ _ _ h => h.1) hn⟩

theorem sPh_unitary : sPhᴴ * sPh = 1 := by
  unfold sPh
  rw [Matrix.diagonal_conjTranspose, Matrix.diagonal_mul_diagonal, ← Matrix.diagonal_one]
  refine congrArg Matrix.diagonal (funext fun i => ?_)
  fin_cases i
  · show star (1 : ℂ) * 1 = 1
    rw [star_one, one_mul]
  · show star Complex.I * Complex.I = 1
    rw [Complex.star_def, Complex.conj_I, neg_mul, Complex.I_mul_I, neg_neg]

/-- **POSITIVE CONTROL**: the quarter phase is available on the pair in the lattice theory at every
level, so the refutation of `R_z(θ₀)` is by its angle. -/
theorem lattice_pairAvail_quarter (n : ℕ) : PairAvailAt latticeClass latticeClass_arch sPh n := by
  unfold PairAvailAt
  exact SubstratumSource.genTheory_avail_conj latticeClass_arch (quarter_on_lattice n)
    (pairOp_isometry sPh_unitary n)

/-- **COUNTERCONTROL**: the monomial interface contains the class and supplies `R_z(θ₀)` on the pair
at every level; the inclusion is strict at that operator. -/
theorem lattice_strict_in_substratum (n : ℕ) (hn : 0 < n) :
    PairAvailAt substratumClass substratumClass_arch zPh n
      ∧ ¬ PairAvailAt latticeClass latticeClass_arch zPh n :=
  ⟨substratum_pairAvail_zPh n, (lattice_refutes hn).1⟩

/-! ### §D — the rows the lattice theory fails, each of which supplies the operations -/

/-- **CONTROL SUPPLIES BOTH**: composite unitary control on the pair carrier makes both pair operators
available at every level, for every architecture. -/
theorem pairAvail_of_control {𝓘 : ImplementationClass} {arch : Architecture 𝓘}
    (h : HasCompositeUnitaryControl (genTheory 𝓘 arch (Fin 2 × Fin 2))) (n : ℕ) :
    PairAvailAt 𝓘 arch zPh n ∧ PairAvailAt 𝓘 arch uJ n :=
  ⟨h n _ (pairOp_isometry zPh_unitary n), h n _ (pairOp_isometry uJ_unitary n)⟩

theorem latticeTheory_pair_not_control :
    ¬ HasCompositeUnitaryControl (latticeTheory (Fin 2 × Fin 2)) :=
  fun h => (lattice_refutes Nat.one_pos).1 (pairAvail_of_control h 1).1

theorem latticeTheory_token_not_control : ¬ HasCompositeUnitaryControl (latticeTheory (Fin 2)) :=
  fun h => (lattice_refutes Nat.one_pos).2.2.1 (h 1 _ (tokOp_isometry zPh_unitary 1))

theorem latticeTheory_not_qm :
    ¬ LevelOneSeam.ExactAllFiniteEndomorphicQuantumOps (latticeTheory (Fin 2)) :=
  fun h => latticeTheory_token_not_control (PhysicalCharacterization.physical_of_exactAll _ h).2.2.1

theorem latticeTheory_pair_not_qm :
    ¬ LevelOneSeam.ExactAllFiniteEndomorphicQuantumOps (latticeTheory (Fin 2 × Fin 2)) :=
  fun h => latticeTheory_pair_not_control (PhysicalCharacterization.physical_of_exactAll _ h).2.2.1

theorem latticeTheory_not_phaseFree :
    ¬ MinimalRepertoire.PhaseFreeRichness (latticeTheory (Fin 2)) :=
  fun h => latticeTheory_token_not_control
    (MinimalRepertoire.control_of_phaseFree _ (latticeTheory_closure (Fin 2)) h)

theorem latticeTheory_not_layerFlowExecutable {S : Type} [Fintype S] [DecidableEq S]
    {σ : Equiv.Perm S} {x : S} (hx : σ x ≠ x) :
    ¬ LiftAudit.LayerFlowExecutable (latticeTheory S) σ :=
  LiftAudit.configurationLevel_not_layerFlowExecutable latticeClass_arch
    latticeClass_configurationLevel hx

theorem latticeClass_not_drivesElementary : ¬ SubstratumSource.DrivesElementary latticeClass :=
  fun h => substratumClass_not_drivesElementary
    ⟨fun S _ _ a b t => lattice_le_substratum S _ (h.1 S a b t),
      fun S _ _ a b => lattice_le_substratum S _ (h.2.1 S a b),
      fun S _ _ a => lattice_le_substratum S _ (h.2.2 S a)⟩

theorem latticeClass_not_quantumArchitecture :
    ¬ SubstratumSource.QuantumArchitecture latticeClass :=
  fun h => latticeClass_not_drivesElementary h.drives

/-! ### §E — level H: every substratum's observer theory -/

section Observer

variable (𝒮 : Substratum) [Fintype 𝒮.ι] [Fintype 𝒮.V] [DecidableEq 𝒮.V]

/-- **A CONFIGURATION PHASE AT THE 3-4-5 ANGLE IS UNAVAILABLE TO EVERY OBSERVER**: for every kernel
substratum, whatever its rule, every level and every operator diagonal in the configurations with
the value `1` at one configuration and `w` at another, its conjugation is unavailable in the observer
theory (I1.59: `obsTheory 𝒮 = permTheory 𝒮.Conf`). -/
theorem obs_zPhase_unavailable {n : ℕ} {d : 𝒮.Conf × Fin n → ℂ} {p q : 𝒮.Conf × Fin n}
    (hp : d p = 1) (hq : d q = w345) :
    ¬ (obsTheory 𝒮).availExt n Unit (fun _ => conjChannel (Matrix.diagonal d)) := by
  intro hav
  haveI : Nonempty (𝒮.Conf × Fin n) := ⟨p⟩
  have h' : InstAvail permClass (𝒮.Conf × Fin n) Unit
      (fun _ => conjChannel (Matrix.diagonal d)) := hav
  obtain ⟨a, ha, hmem⟩ := exists_scaled_mem_of_instAvail_unitary permClass_arch h'
  have h14 : (1 : ℂ) ^ 4 ≠ w345 ^ 4 := by
    rw [one_pow]
    exact fun h => w345_pow_four_ne_one h.symm
  exact not_quart_smul (p := p) (q := q) (by rw [Matrix.diagonal_apply_eq, hp])
    (by rw [Matrix.diagonal_apply_eq, hq]) one_ne_zero w345_ne_zero h14 ha
    (permClass_quartLattice _ _ hmem).2

/-- **AN OPERATOR WITH TWO NONZERO ENTRIES IN ONE ROW IS UNAVAILABLE TO EVERY OBSERVER**, at every
level, whatever the rule. -/
theorem obs_twoInRow_unavailable {n : ℕ} {V : Matrix (𝒮.Conf × Fin n) (𝒮.Conf × Fin n) ℂ}
    {p q q' : 𝒮.Conf × Fin n} (hqq : q ≠ q') (h1 : V p q ≠ 0) (h2 : V p q' ≠ 0) :
    ¬ (obsTheory 𝒮).availExt n Unit (fun _ => conjChannel V) := by
  intro hav
  haveI : Nonempty (𝒮.Conf × Fin n) := ⟨p⟩
  have h' : InstAvail permClass (𝒮.Conf × Fin n) Unit (fun _ => conjChannel V) := hav
  obtain ⟨a, ha, hmem⟩ := exists_scaled_mem_of_instAvail_unitary permClass_arch h'
  exact not_submonomial_smul hqq h1 h2 ha (permClass_quartLattice _ _ hmem).1

end Observer

#print axioms lq_mul
#print axioms lq_smul
#print axioms lq_block
#print axioms lq_reindex
#print axioms lq_conjTranspose
#print axioms latticeClass_arch
#print axioms latticeClass_contextStable
#print axioms latticeClass_labelInvariant
#print axioms latticeClass_daggerStable
#print axioms latticeClass_unitaryRaySaturated
#print axioms latticeClass_structurallyClosed
#print axioms latticeClass_quartLattice
#print axioms latticeClass_configurationLevel
#print axioms permClass_le_lattice
#print axioms mixEmpty_le_lattice
#print axioms lattice_le_substratum
#print axioms phaseGate_lattice
#print axioms latticeTheory_derivedOI
#print axioms latticeTheory_implementationLocality
#print axioms latticeTheory_reversibleImplementationLocality
#print axioms latticeTheory_embeddedObservation
#print axioms latticeTheory_closure
#print axioms latticeTheory_observerRecursion
#print axioms latticeTheory_systemToLevelOne
#print axioms latticeTheory_parallel
#print axioms latticeTheory_observationalIndependence
#print axioms latticeTheory_inert
#print axioms latticeTheory_validity
#print axioms latticeTheory_wellFormed
#print axioms latticeTheory_inverseAccessibility
#print axioms latticeTheory_realizesSealedOICore
#print axioms latticeTheory_oiCore
#print axioms latticeTheory_derivedOICore
#print axioms latticeTheory_qubitObservationalIndependence
#print axioms latticeTheory_qutrit
#print axioms lattice_refutes
#print axioms sPh_unitary
#print axioms lattice_pairAvail_quarter
#print axioms lattice_strict_in_substratum
#print axioms pairAvail_of_control
#print axioms latticeTheory_pair_not_control
#print axioms latticeTheory_token_not_control
#print axioms latticeTheory_not_qm
#print axioms latticeTheory_pair_not_qm
#print axioms latticeTheory_not_phaseFree
#print axioms latticeTheory_not_layerFlowExecutable
#print axioms latticeClass_not_drivesElementary
#print axioms latticeClass_not_quantumArchitecture
#print axioms obs_zPhase_unavailable
#print axioms obs_twoInRow_unavailable

end BridgeAvailFull
end OIBridge
