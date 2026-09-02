/-
  OIBridge/IsometryExtension.lean — boundary item 2 DISCHARGED: finite isometry extension is
  kernel-internal, and the characterization of exact finite operational quantum mechanics by
  the five physical completion conditions becomes UNCONDITIONAL.

  ROUND FORTY-FIVE. Since round twenty-five the Stinespring assembly has consumed one
  external fact, stated in exactly the form used (`FiniteIsometryExtensionSF A`): every
  system-first isometry `V : A → A × Fin (n+1)` with `Vᴴ V = 1` extends to a unitary `U`
  with `U E_{k₀} = V`. This file proves it for every finite carrier, from Mathlib's
  kernel-checked finite orthonormal-basis extension theorem
  `Orthonormal.exists_orthonormalBasis_extension_of_card_eq`, in four small steps:

      1. Gram ⇒ orthonormal columns: the columns `v_a(p) = V p a` of an isometry are an
         orthonormal family in the Euclidean space on `A × Fin (n+1)` (`inner_colVec`).
      2. Seed placement: index those columns by the seed positions `S = {(a, k₀)}`
         (`seed_orthonormal`).
      3. Extension: the seed-indexed family extends to an orthonormal basis of the whole
         space, indexed by `A × Fin (n+1)` itself (`finrank_euclideanSpace` gives the
         cardinality equation).
      4. The matrix: `U`'s `q`-th column is the `q`-th basis vector; `Uᴴ U = 1` is the
         orthonormality of the basis, entry by entry, and `U E_{k₀} = V` is the agreement on
         the seed, entry by entry (`finiteIsometryExtensionSF_discharged`).

  Both matrix identities are proved as explicit entrywise computations, not by simp chains.

      ┌──────────────────────────────────────────────────────────────────────────────┐
      │  `finiteIsometryExtensionSF_discharged A : FiniteIsometryExtensionSF A`.       │
      │  `exactAll_iff_physical_unconditional (T : FiniteOperationalTheory (Fin 2)) :   │
      │      ExactAllFiniteEndomorphicQuantumOps T ↔ PhysicalCompletionConditions T.   │
      │    No isometry hypothesis. No boundary item enters the characterization.       │
      │    [GENERALIZED TO EVERY NONEMPTY FINITE SYSTEM IN ROUND FORTY-SIX: `GeneralCarrier`.]│
      │  The conditional theorems of rounds 25–44 are KEPT as written (they expose the │
      │    historical dependency); each acquires an `_unconditional` corollary here.   │
      └──────────────────────────────────────────────────────────────────────────────┘

  THE BOUNDARY AUDIT, UPDATED (superseding the round-35 three-item statement in
  `BoundaryAudit.lean`, which is preserved and labelled). THE CURRENT UNRESOLVED EXTERNAL
  BOUNDARY: TWO ITEMS — (1) compact Lie integration / reachability; (2) finite Uhlmann /
  Schmidt / right-unitary uniqueness. DISCHARGED INTERNALLY: PSD square-root /
  factorization (round thirty-four, `psdFactorization_discharged`); finite isometry
  extension (this round, `finiteIsometryExtensionSF_discharged`). Neither remaining item is
  a dependency of the OI → finite-QM characterization; neither is claimed dischargeable here.

  WHAT IS AND IS NOT CLAIMED. Proved: everything above, with the usual axiom footprint
  (`propext`, `Classical.choice`, `Quot.sound`; the spectral/orthonormal-basis machinery of
  Mathlib is kernel-internal by the project's standing convention since the Kadison round).
  NOT claimed: anything about the two remaining boundary items; that any completion
  condition follows from OI; OI ⟺ QM. No structure field is added.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.RankGapTheory

namespace OIBridge
namespace IsometryExtension

open Complex Matrix CoherentExtension MonoidalCompletion CoherentLift
open OperationalAssembly StinespringAssembly KrausSoundness CompositeSoundness
open DimensionalObstruction DimensionalCountermodel ReferenceExtension ReferenceSufficiency
open BoundaryAudit SpectatorBridge AncillaClosure ClosureObstruction CompositionalIndependence
open OIRealization OperationalValidity LevelOneSeam PhysicalCharacterization DiagonalTheory
open RankGapTheory HiddenCoherence

open scoped ComplexOrder

/-! ### Section A — the discharge -/

section Discharge

variable {A : Type*} [Fintype A] [DecidableEq A]

/-- The columns of `V` as vectors of the Euclidean space on `A × Fin (n+1)`. -/
noncomputable def colVec {n : ℕ} (V : Matrix (A × Fin (n + 1)) A ℂ) (a : A) :
    EuclideanSpace ℂ (A × Fin (n + 1)) :=
  WithLp.toLp 2 (fun p => V p a)

omit [DecidableEq A] in
/-- **STEP 1 — GRAM ⇒ INNER PRODUCTS**: the inner product of two columns is the Gram entry. -/
theorem inner_colVec {n : ℕ} (V : Matrix (A × Fin (n + 1)) A ℂ) (a b : A) :
    inner ℂ (colVec V a) (colVec V b) = (Vᴴ * V) a b := by
  rw [EuclideanSpace.inner_eq_star_dotProduct, Matrix.mul_apply, dotProduct]
  simp only [colVec, WithLp.ofLp_toLp, Matrix.conjTranspose_apply, Pi.star_apply]
  exact Finset.sum_congr rfl fun p _ => mul_comm _ _

/-- **STEP 2 — SEED PLACEMENT**: the columns of an isometry, indexed by the seed positions
`(a, k₀)`, form an orthonormal family. -/
theorem seed_orthonormal {n : ℕ} (k₀ : Fin (n + 1)) (V : Matrix (A × Fin (n + 1)) A ℂ)
    (hV : Vᴴ * V = 1) :
    Orthonormal ℂ (({q : A × Fin (n + 1) | q.2 = k₀} : Set (A × Fin (n + 1))).domRestrict
      (fun q => colVec V q.1)) := by
  rw [orthonormal_iff_ite]
  rintro ⟨i, hi⟩ ⟨j, hj⟩
  simp only [Set.domRestrict_apply, inner_colVec, hV, Matrix.one_apply, Subtype.mk.injEq]
  simp only [Set.mem_ofPred_eq] at hi hj
  congr 1
  apply propext
  constructor
  · intro h
    exact Prod.ext h (hi.trans hj.symm)
  · intro h
    exact congrArg Prod.fst h

end Discharge

/-- **BOUNDARY ITEM 2, DISCHARGED**: finite isometry extension holds for every finite
carrier. Steps 3 and 4: extend the seed-indexed orthonormal family to an orthonormal basis
indexed by `A × Fin (n+1)` (Mathlib's `Orthonormal.exists_orthonormalBasis_extension_of_card_eq`,
with `finrank_euclideanSpace` supplying the cardinality equation), take `U`'s columns to be the
basis vectors, and check `Uᴴ U = 1` and `U E_{k₀} = V` entry by entry. -/
theorem finiteIsometryExtensionSF_discharged (A : Type*) [Fintype A] [DecidableEq A] :
    FiniteIsometryExtensionSF A := by
  intro n k₀ V hV
  obtain ⟨b, hb⟩ := Orthonormal.exists_orthonormalBasis_extension_of_card_eq
    (𝕜 := ℂ) (E := EuclideanSpace ℂ (A × Fin (n + 1))) (ι := A × Fin (n + 1))
    finrank_euclideanSpace (seed_orthonormal k₀ V hV)
  refine ⟨Matrix.of fun p q => (b q).ofLp p, ?_, ?_⟩
  · -- `Uᴴ U = 1`: orthonormality of the basis, entrywise
    ext q q'
    have h := (orthonormal_iff_ite.mp b.orthonormal) q q'
    rw [EuclideanSpace.inner_eq_star_dotProduct] at h
    rw [Matrix.mul_apply, Matrix.one_apply, ← h, dotProduct]
    simp only [Matrix.conjTranspose_apply, Matrix.of_apply, Pi.star_apply]
    exact Finset.sum_congr rfl fun p _ => mul_comm _ _
  · -- `U E_{k₀} = V`: agreement on the seed, entrywise
    ext p a
    rw [Matrix.mul_apply]
    rw [Finset.sum_eq_single (a, k₀)]
    · simp only [Matrix.of_apply, Esf, if_true, mul_one]
      rw [hb (a, k₀) rfl]
      rfl
    · intro q _ hq
      simp only [Esf, Matrix.of_apply]
      by_cases h2 : q.2 = k₀
      · have h1 : q.1 ≠ a := fun h1 => hq (Prod.ext h1 h2)
        simp [h2, h1]
      · simp [h2]
    · intro h
      exact absurd (Finset.mem_univ _) h

/-- The two instances the development consumes: at `Unit` and at every composite carrier. -/
theorem isometryExtension_unit : FiniteIsometryExtensionSF Unit :=
  finiteIsometryExtensionSF_discharged Unit

theorem isometryExtension_composite : ∀ k : ℕ, FiniteIsometryExtensionSF (Fin 2 × Fin (k + 1)) :=
  fun k => finiteIsometryExtensionSF_discharged (Fin 2 × Fin (k + 1))

/-- **THE TWO DISCHARGED ITEMS**, as one statement: PSD factorization (round thirty-four) and
finite isometry extension (this round), for every finite carrier. -/
theorem discharged_items :
    (∀ (R : Type) [Fintype R] [DecidableEq R] (ρ : Matrix R R ℂ), ρ.PosSemidef →
      ∃ B : Matrix R R ℂ, ρ = B * Bᴴ)
    ∧ ∀ (A : Type) [Fintype A] [DecidableEq A], FiniteIsometryExtensionSF A :=
  ⟨fun R _ _ => psdFactorization_discharged R, fun A _ _ => finiteIsometryExtensionSF_discharged A⟩

/-! ### Section B — the conditional theorems, unconditional -/

section Unconditional

variable {A : Type*} [Fintype A] [DecidableEq A]

/-- Round twenty-five's capstone without its hypothesis. -/
theorem fullInstruments_of_control_unconditional (T : FiniteOperationalTheory A)
    (hctrl : HasCompositeUnitaryControl T) : HasFullFiniteEndomorphicInstruments T :=
  fullInstruments_of_control T (finiteIsometryExtensionSF_discharged A) hctrl

/-- Round twenty-six's endpoint without its hypothesis. -/
theorem exact_of_sound_control_unconditional (T : FiniteOperationalTheory A)
    (hsound : KrausSound T) (hctrl : HasCompositeUnitaryControl T) :
    ExactFiniteEndomorphicQuantumOps T :=
  exact_of_sound_control T hsound (finiteIsometryExtensionSF_discharged A) hctrl

/-- Round thirty-six's composite Stinespring assembly without its hypothesis. -/
theorem compositeCompleteness_unconditional (T : FiniteOperationalTheory A)
    (hctrl : HasCompositeUnitaryControl T) (hin : InertSpectatorCompositionality T)
    (hclos : IteratedAncillaClosure T) : HasFullCompositeInstruments T :=
  compositeCompleteness T (fun k => finiteIsometryExtensionSF_discharged (A × Fin (k + 1)))
    hctrl hin hclos

end Unconditional

/-- Every unit vector on a composite carrier is a column of some unitary — round
thirty-seven's rotation lemma without its hypothesis. -/
theorem unitVectorRotation_unconditional (n : ℕ) : UnitVectorRotation (Fin 2 × Fin (n + 1)) :=
  unitVectorRotation_of_isometryExtension isometryExtension_unit n

theorem krausSoundExt_of_sound_control_inert_unconditional (T : FiniteOperationalTheory (Fin 2))
    (hsound : KrausSound T) (hctrl : HasCompositeUnitaryControl T)
    (hin : InertSpectatorCompositionality T) : KrausSoundExt T :=
  krausSoundExt_of_sound_control_inert T isometryExtension_unit hsound hctrl hin

theorem exactComposite_of_conditions_unconditional (T : FiniteOperationalTheory (Fin 2))
    (hsound : KrausSound T) (hctrl : HasCompositeUnitaryControl T)
    (hin : InertSpectatorCompositionality T) (hclos : IteratedAncillaClosure T) :
    ExactCompositeQuantumOps T :=
  exactComposite_of_conditions T isometryExtension_unit isometryExtension_composite hsound hctrl
    hin hclos

theorem exactComposite_of_validity_unconditional (T : FiniteOperationalTheory (Fin 2))
    (hval : CompositeOperationalValidity T) (hin : InertSpectatorCompositionality T)
    (hctrl : HasCompositeUnitaryControl T) (hclos : IteratedAncillaClosure T) :
    ExactCompositeQuantumOps T :=
  exactComposite_of_validity T isometryExtension_composite hval hin hctrl hclos

theorem exactAll_of_conditions_unconditional (T : FiniteOperationalTheory (Fin 2))
    (hval : CompositeOperationalValidity T) (hin : InertSpectatorCompositionality T)
    (hctrl : HasCompositeUnitaryControl T) (hclos : IteratedAncillaClosure T)
    (h1 : SystemToLevelOne T) : ExactAllFiniteEndomorphicQuantumOps T :=
  exactAll_of_conditions T isometryExtension_composite hval hin hctrl hclos h1

theorem exactAll_of_physical_unconditional (T : FiniteOperationalTheory (Fin 2))
    (h : PhysicalCompletionConditions T) : ExactAllFiniteEndomorphicQuantumOps T :=
  exactAll_of_physical T isometryExtension_composite h

/-- **THE CHARACTERIZATION, UNCONDITIONAL.** For a qubit system, exact finite endomorphic
quantum operations on the system and every positive composite hold if and only if the five
physical completion conditions hold. No isometry hypothesis; no external boundary item
enters either direction. -/
theorem exactAll_iff_physical_unconditional (T : FiniteOperationalTheory (Fin 2)) :
    ExactAllFiniteEndomorphicQuantumOps T ↔ PhysicalCompletionConditions T :=
  exactAll_iff_physical T isometryExtension_composite

theorem fullQuantum_exactComposite_unconditional : ExactCompositeQuantumOps fullQuantum :=
  fullQuantum_exactComposite isometryExtension_unit isometryExtension_composite

theorem fullQuantum_exactAll : ExactAllFiniteEndomorphicQuantumOps fullQuantum :=
  exactAll_of_conditions_unconditional fullQuantum fullQuantum_validity fullQuantum_inert
    fullQuantum_control fullQuantum_iteratedAncillaClosure fullQuantum_systemToLevelOne

theorem systemLoose_exactComposite_unconditional : ExactCompositeQuantumOps systemLoose :=
  systemLoose_exactComposite isometryExtension_composite

/-- **THE FINAL CLASSIFICATION, UNCONDITIONAL**: `final_classification` with the isometry
hypothesis removed from its first clause. -/
theorem final_classification_unconditional :
    (∀ T : FiniteOperationalTheory (Fin 2),
      CompositeOperationalValidity T → InertSpectatorCompositionality T
        → HasCompositeUnitaryControl T → IteratedAncillaClosure T → SystemToLevelOne T
        → ExactAllFiniteEndomorphicQuantumOps T)
    ∧ (∃ T : FiniteOperationalTheory (Fin 2),
      CompositeOperationalValidity T ∧ InertSpectatorCompositionality T
        ∧ HasCompositeUnitaryControl T ∧ IteratedAncillaClosure T ∧ SystemToLevelOne T)
    ∧ (∃ T : FiniteOperationalTheory (Fin 2),
      CompositeOperationalValidity T ∧ InertSpectatorCompositionality T
        ∧ HasCompositeUnitaryControl T ∧ IteratedAncillaClosure T
        ∧ ¬ SystemToLevelOne T ∧ ¬ ExactFiniteEndomorphicQuantumOps T) :=
  ⟨fun T hval hin hctrl hclos h1 => exactAll_of_conditions_unconditional T hval hin hctrl hclos h1,
    final_classification.2.1, final_classification.2.2⟩

/-- **THE OPERATIONAL CLASSIFICATION, FROZEN AND UNCONDITIONAL**: the characterization iff,
the five-way minimality audit, and joint satisfiability, with no boundary item anywhere. -/
theorem operational_classification :
    (∀ T : FiniteOperationalTheory (Fin 2),
      ExactAllFiniteEndomorphicQuantumOps T ↔ PhysicalCompletionConditions T)
    ∧ (∃ T : FiniteOperationalTheory (Fin 2), PhysicalCompletionConditions T)
    ∧ (∃ T : FiniteOperationalTheory (Fin 2),
      InertSpectatorCompositionality T ∧ HasCompositeUnitaryControl T
        ∧ IteratedAncillaClosure T ∧ SystemToLevelOne T ∧ RealizesSealedOICore T
        ∧ ¬ CompositeOperationalValidity T)
    ∧ (∃ T : FiniteOperationalTheory (Fin 2),
      CompositeOperationalValidity T ∧ HasCompositeUnitaryControl T
        ∧ IteratedAncillaClosure T ∧ SystemToLevelOne T ∧ RealizesSealedOICore T
        ∧ ¬ InertSpectatorCompositionality T)
    ∧ (∃ T : FiniteOperationalTheory (Fin 2),
      CompositeOperationalValidity T ∧ InertSpectatorCompositionality T
        ∧ IteratedAncillaClosure T ∧ SystemToLevelOne T ∧ RealizesSealedOICore T
        ∧ ¬ HasCompositeUnitaryControl T)
    ∧ (∃ T : FiniteOperationalTheory (Fin 2),
      CompositeOperationalValidity T ∧ InertSpectatorCompositionality T
        ∧ HasCompositeUnitaryControl T ∧ SystemToLevelOne T ∧ RealizesSealedOICore T
        ∧ ¬ IteratedAncillaClosure T)
    ∧ (∃ T : FiniteOperationalTheory (Fin 2),
      CompositeOperationalValidity T ∧ InertSpectatorCompositionality T
        ∧ HasCompositeUnitaryControl T ∧ IteratedAncillaClosure T ∧ RealizesSealedOICore T
        ∧ ¬ SystemToLevelOne T) :=
  ⟨exactAll_iff_physical_unconditional,
    ⟨fullQuantum, physical_of_exactAll fullQuantum fullQuantum_exactAll⟩,
    five_way_minimality.1, five_way_minimality.2.1, five_way_minimality.2.2.1,
    five_way_minimality.2.2.2.1, five_way_minimality.2.2.2.2⟩

#print axioms inner_colVec
#print axioms seed_orthonormal
#print axioms finiteIsometryExtensionSF_discharged
#print axioms isometryExtension_unit
#print axioms isometryExtension_composite
#print axioms discharged_items
#print axioms fullInstruments_of_control_unconditional
#print axioms exact_of_sound_control_unconditional
#print axioms compositeCompleteness_unconditional
#print axioms unitVectorRotation_unconditional
#print axioms krausSoundExt_of_sound_control_inert_unconditional
#print axioms exactComposite_of_conditions_unconditional
#print axioms exactComposite_of_validity_unconditional
#print axioms exactAll_of_conditions_unconditional
#print axioms exactAll_of_physical_unconditional
#print axioms exactAll_iff_physical_unconditional
#print axioms fullQuantum_exactComposite_unconditional
#print axioms fullQuantum_exactAll
#print axioms systemLoose_exactComposite_unconditional
#print axioms final_classification_unconditional
#print axioms operational_classification

end IsometryExtension
end OIBridge
