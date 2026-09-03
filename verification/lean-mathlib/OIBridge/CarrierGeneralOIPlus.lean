/-
  OIBridge/CarrierGeneralOIPlus.lean — the carrier-general OI⁺ audit: the three principles of
  round fifty-three and their equivalence with finite operational QM on every nonempty finite
  carrier.

  ROUND FIFTY-FIVE. Round fifty-three stated OI⁺ on the qubit carrier and the five-condition
  characterization holds on every nonempty finite carrier. This file removes the asymmetry
  where it can be removed and says exactly where it cannot.

  THE AUDIT. Which of the round-53 pieces genuinely use the qubit?

      · The OI core. `RealizesSealedOICore` is a statement about the sealed qubit process (a
        two-level visible system with its four-level hidden sector realized at ancilla level
        four); there is no carrier-general sealed core in the kernel, and none is invented
        here. On the qubit the core conjunct of OI⁺ is logically redundant
        (`completedOI_iff_physical`): full control realizes the core. So the carrier-general
        OI⁺ is stated WITHOUT the core conjunct — well-formedness plus the three principles —
        and on the qubit it is provably the round-53 OI⁺ (`oiPlus_qubit_iff`).
      · Observational independence: generic. The parallel reference extension is defined for
        every carrier, and so is the joint performability of independent observations.
      · Reversible richness: generic in both directions. The forward direction is the
        round-50 reachability theorem, which is carrier-general; the converse needs one
        nonempty-carrier base point for the rank-one drift, in place of the qubit's `(0, 0)`.
        The word closure of conjugations is proved on a general carrier.
      · Observer recursion: generic already — the round-53 definition and the weakened
        shifted-theory construction were written for an arbitrary carrier.
      · OI⁺ ⟹ QM and QM ⟹ OI⁺: generic once the principles are, through
        `exactAll_iff_substantive` and `physical_of_exactAll`, both carrier-general.

      ┌──────────────────────────────────────────────────────────────────────────────┐
      │  `oiPlus_iff_qm`: for every nonempty finite carrier `A` and every theory on   │
      │      it, OI⁺ ⟺ exact finite endomorphic operational QM.                       │
      │  `carrier_general_oiPlus`: the same, quantified over the carrier.             │
      │  `oiPlus_qubit_iff`: on the qubit, the round-53 OI⁺ (with the core conjunct)  │
      │      is the carrier-general OI⁺.                                              │
      │  `oiPlus_independence`: each principle fails on a qubit theory with            │
      │      well-formedness and the other two — the round-53 witnesses, unchanged.   │
      └──────────────────────────────────────────────────────────────────────────────┘

  WHAT IS AND IS NOT CLAIMED. Proved: everything above, with the usual axiom footprint. NOT
  claimed: a carrier-general sealed OI core; that the independence witnesses are needed on
  every carrier (the qubit witnesses settle logical independence); that any principle follows
  from bare OI. The round-53 file is unchanged. No structure field is added.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.CompletedOI

namespace OIBridge
namespace OIHierarchyGeneral

open Complex Matrix CoherentExtension MonoidalCompletion CoherentLift IndependenceCensus
open OperationalAssembly StinespringAssembly KrausSoundness CompositeSoundness
open DimensionalObstruction DimensionalCountermodel ReferenceExtension ReferenceSufficiency
open BoundaryAudit SpectatorBridge AncillaClosure ClosureObstruction CompositionalIndependence
open OIRealization OperationalValidity LevelOneSeam PhysicalCharacterization DiagonalTheory
open HiddenCoherence RankGapTheory GeneralCarrier ControlLie ReachabilitySeam OrbitReachability
open SubstantiveCensus OperationalRigidity OIHierarchy

open scoped ComplexOrder Kronecker Matrix.Norms.L2Operator

attribute [local instance 100] LieRing.ofAssociativeRing

variable {A : Type} [Fintype A] [DecidableEq A]

/-! ### Section A — observational independence, on any carrier -/

section Independence

variable (T : FiniteOperationalTheory A)

/-- **OBSERVATIONAL INDEPENDENCE** on a carrier `A`. -/
def ObservationalIndependence : Prop := HasParallelReferenceExtension T

theorem observationalIndependence_iff_inert :
    ObservationalIndependence T ↔ InertSpectatorCompositionality T :=
  (inertSpectator_iff_parallelReferenceExtension T).symm

/-- Two operations on disjoint composites, performed jointly. -/
def parallelPair {n k m : ℕ} (e : (A × Fin k) × (A × Fin n) ≃ A × Fin m) {O O' : Type}
    (F : O → Matrix (A × Fin n) (A × Fin n) ℂ →ₗ[ℂ] Matrix (A × Fin n) (A × Fin n) ℂ)
    (G : O' → Matrix (A × Fin k) (A × Fin k) ℂ →ₗ[ℂ] Matrix (A × Fin k) (A × Fin k) ℂ) :
    O' × O → Matrix (A × Fin m) (A × Fin m) ℂ →ₗ[ℂ] Matrix (A × Fin m) (A × Fin m) ℂ :=
  fun c => (withSpectator (A × Fin k) e (F c.2)).comp
    (withSpectator (A × Fin n) ((Equiv.prodComm _ _).trans e) (G c.1))

theorem parallel_of_observationalIndependence (h : ObservationalIndependence T) {n k m : ℕ}
    (e : (A × Fin k) × (A × Fin n) ≃ A × Fin m) {O O' : Type} [Fintype O] [DecidableEq O]
    [Fintype O'] [DecidableEq O']
    {F : O → Matrix (A × Fin n) (A × Fin n) ℂ →ₗ[ℂ] Matrix (A × Fin n) (A × Fin n) ℂ}
    {G : O' → Matrix (A × Fin k) (A × Fin k) ℂ →ₗ[ℂ] Matrix (A × Fin k) (A × Fin k) ℂ}
    (hF : T.availExt n O F) (hG : T.availExt k O' G) :
    T.availExt m (O' × O) (parallelPair e F G) := by
  have hF' := h (A × Fin k) n m e O F hF
  have hG' := h (A × Fin n) k m ((Equiv.prodComm _ _).trans e) O' G hG
  have := T.availExt_bind m O' O
    (fun b => withSpectator (A × Fin n) ((Equiv.prodComm _ _).trans e) (G b))
    (fun _ a => withSpectator (A × Fin k) e (F a)) hG' (fun _ => hF')
  exact this

end Independence

/-! ### Section B — reversible richness, on any carrier -/

section Richness

variable (T : FiniteOperationalTheory A)

/-- **REVERSIBLE RICHNESS** on a carrier `A`. -/
def ReversibleRichness : Prop :=
  (∀ (n : ℕ) (V : Matrix (A × Fin n) (A × Fin n) ℂ),
    T.availExt n Unit (fun _ => conjChannel V) → T.availExt n Unit (fun _ => conjChannel Vᴴ))
  ∧ ∀ n : ℕ, ∃ (G : Type) (H : Matrix (A × Fin n) (A × Fin n) ℂ)
      (U : G → Matrix (A × Fin n) (A × Fin n) ℂ),
      Hᴴ = H ∧ (∀ g, (U g)ᴴ * U g = 1) ∧ HControl H U
        ∧ (∀ t : ℝ, T.availExt n Unit (fun _ => conjChannel (flow H t)))
        ∧ (∀ g, T.availExt n Unit (fun _ => conjChannel (U g)))

theorem conjChannel_mul_general {l : Type} [Fintype l] [DecidableEq l] (V W : Matrix l l ℂ) :
    (conjChannel V).comp (conjChannel W) = conjChannel (V * W) := by
  refine LinearMap.ext fun X => ?_
  show V * (W * X * Wᴴ) * Vᴴ = V * W * X * (V * W)ᴴ
  rw [Matrix.conjTranspose_mul]
  simp only [Matrix.mul_assoc]

/-- **REVERSIBLE RICHNESS GIVES FULL COMPOSITE UNITARY CONTROL** on any carrier. -/
theorem control_of_reversibleRichness (h : ReversibleRichness T) :
    HasCompositeUnitaryControl T := by
  intro n V hV
  obtain ⟨G, H, U, hH, hU, hLie, hflow, hctrl⟩ := h.2 n
  let avail : ∀ m : ℕ, (Fin m → Matrix (A × Fin n) (A × Fin n) ℂ →ₗ[ℂ]
      Matrix (A × Fin n) (A × Fin n) ℂ) → Prop :=
    fun m F => ∀ i : Fin m, T.availExt n Unit (fun _ => F i)
  have hreach : UniversalUnitaryReachability avail :=
    universalReachability_of_lieRank_unconditional H U hH hU hLie avail
      (fun V W hV hW i => by
        have := availExt_comp_unit T n _ _ (hW i) (hV i)
        rwa [conjChannel_mul_general] at this)
      (fun V hV i => h.1 n V (hV i))
      (fun _ => by
        have := hflow 0
        rwa [flow_zero] at this)
      (fun t _ => hflow t) (fun g _ => hctrl g)
  exact hreach V hV 0

/-- **FULL CONTROL ON A WELL-FORMED THEORY IS REVERSIBLY RICH**, on any nonempty carrier: the
rank-one matrix unit at a base point is the drift, all unitaries are the controls. -/
theorem reversibleRichness_of_control [Nonempty A] (hwf : WellFormed T)
    (hctrl : HasCompositeUnitaryControl T) : ReversibleRichness T := by
  refine ⟨fun n V hV => ?_, fun n => ?_⟩
  · have htr := (hwf.1 n Unit _ hV).2
    have hV1 : Vᴴ * V = 1 := by
      have h := sum_conjTranspose_mul_eq_one_of_trace (fun _ : Unit => V) fun X => htr X
      rwa [Fintype.sum_unique] at h
    exact hctrl n Vᴴ (by rw [Matrix.conjTranspose_conjTranspose]; exact mul_eq_one_comm.mp hV1)
  · rcases Nat.eq_zero_or_pos n with rfl | hn
    · refine ⟨Unit, 0, fun _ => 1, by simp, fun _ => by simp, fun B _ => ?_, fun t => ?_,
        fun _ => ?_⟩
      · have hB0 : B = 0 := by
          ext i _
          exact isEmptyElim i
        rw [hB0]
        exact (controlLie (0 : Matrix (A × Fin 0) (A × Fin 0) ℂ)
          (fun _ : Unit => (1 : Matrix (A × Fin 0) (A × Fin 0) ℂ))).zero_mem
      · exact hctrl 0 _ (flow_isometry (0 : Matrix (A × Fin 0) (A × Fin 0) ℂ) (by simp) t)
      · exact hctrl 0 1 (by simp)
    · let i₀ : A × Fin n := (Classical.arbitrary A, ⟨0, hn⟩)
      refine ⟨{W : Matrix (A × Fin n) (A × Fin n) ℂ // Wᴴ * W = 1},
        Matrix.single i₀ i₀ (1 : ℂ), fun W => W.1, OIHierarchy.single_diag_hermitian' i₀, fun W => W.2,
        hControl_single_all i₀, fun t => hctrl n _ (flow_isometry _ (OIHierarchy.single_diag_hermitian' i₀) t),
        fun W => hctrl n W.1 W.2⟩

end Richness

/-! ### Section C — carrier-general OI⁺ -/

section OIPlus

variable (T : FiniteOperationalTheory A)

/-- **OI⁺ ON A CARRIER**: well-formedness, observational independence, reversible richness,
observer recursion. The sealed qubit core is not a statement about a general carrier; on the
qubit its conjunct is redundant (`completedOI_iff_physical`) and `oiPlus_qubit_iff` below
identifies this definition with the round-53 one. -/
def OIPlus : Prop :=
  WellFormed T ∧ ObservationalIndependence T ∧ ReversibleRichness T ∧ ObserverRecursion T

variable [Nonempty A]

/-- **OI⁺ IMPLIES FINITE OPERATIONAL QM**, on any nonempty finite carrier. -/
theorem qm_of_oiPlus (h : OIPlus T) : ExactAllFiniteEndomorphicQuantumOps T := by
  obtain ⟨hwf, hind, hrich, hrec⟩ := h
  rw [exactAll_iff_substantive T hwf]
  exact ⟨(observationalIndependence_iff_inert T).mp hind, control_of_reversibleRichness T hrich,
    closure_of_observerRecursion hrec⟩

/-- **FINITE OPERATIONAL QM SATISFIES OI⁺**, on any nonempty finite carrier. -/
theorem oiPlus_of_qm (h : ExactAllFiniteEndomorphicQuantumOps T) : OIPlus T := by
  have hp := physical_of_exactAll T h
  have hwf : WellFormed T := ⟨hp.1, hp.2.2.2.2⟩
  exact ⟨hwf, (observationalIndependence_iff_inert T).mpr hp.2.1,
    reversibleRichness_of_control T hwf hp.2.2.1,
    observerRecursion_of_closure T (availExt_id_of_control T hp.2.2.1)
      (availExt_relativeReadout T hp.2.1) hp.2.2.2.1⟩

/-- **OI⁺ ⟺ FINITE OPERATIONAL QM**, on any nonempty finite carrier. -/
theorem oiPlus_iff_qm : OIPlus T ↔ ExactAllFiniteEndomorphicQuantumOps T :=
  ⟨qm_of_oiPlus T, oiPlus_of_qm T⟩

end OIPlus

/-- **THE CARRIER-GENERAL STATEMENT**, quantified over the carrier. -/
theorem carrier_general_oiPlus :
    ∀ (A : Type) [Fintype A] [DecidableEq A] [Nonempty A] (T : FiniteOperationalTheory A),
      OIPlus T ↔ ExactAllFiniteEndomorphicQuantumOps T :=
  fun _ _ _ _ T => oiPlus_iff_qm T

/-! ### Section D — the qubit specialization and the independence witnesses -/

section Qubit

/-- On the qubit, the round-53 OI⁺ (with the OI-core conjunct) is the carrier-general OI⁺:
the core conjunct is redundant given the rest. -/
theorem oiPlus_qubit_iff (T : FiniteOperationalTheory (Fin 2)) :
    OIHierarchy.OIPlus T ↔ OIPlus T := by
  rw [OIHierarchy.oiPlus_iff_qm, oiPlus_iff_qm]

/-- **THE THREE PRINCIPLES OF CARRIER-GENERAL OI⁺ ARE INDEPENDENT**, witnessed on the qubit:
each fails on a well-formed theory carrying the sealed core and the other two. -/
theorem oiPlus_independence :
    (∃ T : FiniteOperationalTheory (Fin 2), WellFormed T ∧ ReversibleRichness T
      ∧ ObserverRecursion T ∧ ¬ ObservationalIndependence T)
    ∧ (∃ T : FiniteOperationalTheory (Fin 2), WellFormed T ∧ ObservationalIndependence T
      ∧ ObserverRecursion T ∧ ¬ ReversibleRichness T)
    ∧ (∃ T : FiniteOperationalTheory (Fin 2), WellFormed T ∧ ObservationalIndependence T
      ∧ ReversibleRichness T ∧ ¬ ObserverRecursion T) := by
  obtain ⟨⟨T₁, -, hw₁, hr₁, hk₁, hi₁⟩, ⟨T₂, -, hw₂, hi₂, hk₂, hr₂⟩, ⟨T₃, -, hw₃, hi₃, hr₃, hk₃⟩⟩ :=
    OIHierarchy.oiPlus_independence
  exact ⟨⟨T₁, hw₁, hr₁, hk₁, hi₁⟩, ⟨T₂, hw₂, hi₂, hk₂, hr₂⟩, ⟨T₃, hw₃, hi₃, hr₃, hk₃⟩⟩

end Qubit

#print axioms observationalIndependence_iff_inert
#print axioms parallel_of_observationalIndependence
#print axioms conjChannel_mul_general
#print axioms control_of_reversibleRichness
#print axioms reversibleRichness_of_control
#print axioms qm_of_oiPlus
#print axioms oiPlus_of_qm
#print axioms oiPlus_iff_qm
#print axioms carrier_general_oiPlus
#print axioms oiPlus_qubit_iff
#print axioms oiPlus_independence

end OIHierarchyGeneral
end OIBridge
