import ResearchDesign.PreservationInduction
import OIBridge.StructuralClosure

/-!
Research-only positive instances of the five-constructor preservation theorem.
Compile after copying PreservationInduction.lean to ResearchDesign/ and building it.
The preparation sets are given independently of protocol reachability.
-/

namespace OIBridge.PreservationInductionDesign

open Matrix InterventionLocality OperationalAssembly MonoidalCompletion
open CompositeSoundness DimensionalCountermodel SubstratumInterface StructuralClosure
open scoped ComplexOrder

abbrev quantumCone : CarrierConeFamily := fun _ _ _ => {X | X.PosSemidef}

abbrev classicalCone : CarrierConeFamily := fun _ _ _ =>
  {X | X.PosSemidef ∧ ∃ d, X = Matrix.diagonal d}

/-- The existing all-carrier monomial inventory, including zero weights and projectors. -/
abbrev classicalClass : ImplementationClass := substratumClass

theorem classicalCone_iff {S : Type} [Fintype S] [DecidableEq S]
    (X : Matrix S S ℂ) :
    X ∈ classicalCone S ↔ ∃ d, (∀ i, 0 ≤ d i) ∧ X = Matrix.diagonal d := by
  constructor
  · rintro ⟨hX, d, rfl⟩
    exact ⟨d, Matrix.posSemidef_diagonal_iff.mp hX, rfl⟩
  · rintro ⟨d, hd, rfl⟩
    exact ⟨Matrix.posSemidef_diagonal_iff.mpr hd, ⟨d, rfl⟩⟩

theorem quantum_additive : AdditiveClosure quantumCone where
  zero_mem := fun _ _ _ => Matrix.PosSemidef.zero
  add_mem := fun _ _ _ _ _ hX hY => hX.add hY

theorem quantum_conj {S : Type} [Fintype S] [DecidableEq S] (K : Matrix S S ℂ) :
    PreservesCarrier quantumCone S (conjChannel K) := by
  intro X hX
  change (K * X * Kᴴ).PosSemidef
  exact hX.mul_mul_conjTranspose_same K

theorem quantum_primitive (𝓘 : ImplementationClass) :
    PrimitivePreservation 𝓘 quantumCone where
  op := fun _ _ _ K _ _ => quantum_conj K
  readout := fun _ _ _ _ _ _ _ _ _ _k => quantum_conj _

/-- Copy X into one coordinate ancilla block, using a diagonal compression. -/
def attachBlock {S : Type} [Fintype S] [DecidableEq S] (m : ℕ)
    (e : Fin m) (X : Matrix S S ℂ) : Matrix (S × Fin m) (S × Fin m) ℂ :=
  let P := Matrix.diagonal (fun p : S × Fin m => if p.2 = e then (1 : ℂ) else 0)
  P * X.submatrix Prod.fst Prod.fst * Pᴴ

theorem attachBlock_apply {S : Type} [Fintype S] [DecidableEq S] (m : ℕ)
    (e : Fin m) (X : Matrix S S ℂ) (p q : S × Fin m) :
    attachBlock m e X p q = if p.2 = e ∧ q.2 = e then X p.1 q.1 else 0 := by
  rw [attachBlock, Matrix.diagonal_conjTranspose, Matrix.mul_diagonal, Matrix.diagonal_mul]
  by_cases hp : p.2 = e <;> by_cases hq : q.2 = e <;>
    simp [hp, hq, Matrix.submatrix, Pi.star_apply]

theorem uniformAttach_eq_blocks {S : Type} [Fintype S] [DecidableEq S]
    (m : ℕ) (X : Matrix S S ℂ) :
    uniformAttach m X = (m : ℂ)⁻¹ • ∑ e : Fin m, attachBlock m e X := by
  ext p q
  rw [uniformAttach_apply, tensorOf_apply, Matrix.smul_apply, Matrix.one_apply,
    Matrix.smul_apply, Matrix.sum_apply]
  simp only [smul_eq_mul, attachBlock_apply]
  by_cases h : p.2 = q.2
  · simp [h, mul_comm]
  · have hz : (∑ e : Fin m,
        if p.2 = e ∧ q.2 = e then X p.1 q.1 else 0) = 0 := by
      apply Finset.sum_eq_zero
      intro e _
      apply if_neg
      rintro ⟨hp, hq⟩
      exact h (hp.trans hq.symm)
    simp [h, hz]

theorem quantum_attach : UniformAttachPreservation quantumCone := by
  intro S _ _ m _ X hX
  change (uniformAttach m X).PosSemidef
  rw [uniformAttach_eq_blocks]
  apply Matrix.PosSemidef.smul _ (natInv_nonneg m)
  exact CompositeSoundness.posSemidef_sum _ _ fun e _ =>
    (hX.submatrix Prod.fst).mul_mul_conjTranspose_same _

theorem ptraceAnc_eq_blocks {S : Type} [Fintype S] [DecidableEq S]
    (m : ℕ) (X : Matrix (S × Fin m) (S × Fin m) ℂ) :
    ptraceAnc m X = ∑ e : Fin m, X.submatrix (fun s => (s, e)) (fun s => (s, e)) := by
  ext s t
  simp only [ptraceAnc_apply, Matrix.sum_apply, Matrix.submatrix_apply]

theorem quantum_discard : AncillaDiscardPreservation quantumCone := by
  intro S _ _ m _ X hX
  change (ptraceAnc m X).PosSemidef
  rw [ptraceAnc_eq_blocks]
  exact CompositeSoundness.posSemidef_sum _ _ fun e _ => hX.submatrix (fun s => (s, e))

/-- Uniform over every inventory; fullClass is a particular explicit comparison. -/
theorem quantum_instAvail {𝓘 : ImplementationClass}
    {S : Type} [Fintype S] [DecidableEq S] {O : Type} [Fintype O] [DecidableEq O]
    {F : O → Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ} (h : InstAvail 𝓘 S O F) :
    ∀ a, PreservesCarrier quantumCone S (F a) :=
  instAvail_preserves quantumCone quantum_additive (quantum_primitive 𝓘)
    quantum_attach quantum_discard h

theorem quantum_fullClass
    {S : Type} [Fintype S] [DecidableEq S] {O : Type} [Fintype O] [DecidableEq O]
    {F : O → Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ} (h : InstAvail fullClass S O F) :
    ∀ a, PreservesCarrier quantumCone S (F a) := quantum_instAvail h

theorem classical_additive : AdditiveClosure classicalCone where
  zero_mem := fun _ _ _ => ⟨Matrix.PosSemidef.zero, ⟨0, by simp⟩⟩
  add_mem := by
    intro S _ _ X Y hX hY
    rcases hX with ⟨hX, d, rfl⟩
    rcases hY with ⟨hY, e, rfl⟩
    exact ⟨hX.add hY, ⟨d + e, by simp⟩⟩

theorem classical_conj {S : Type} [Fintype S] [DecidableEq S]
    (K : Matrix S S ℂ) (hK : classicalClass S K) :
    PreservesCarrier classicalCone S (conjChannel K) := by
  rintro X ⟨hX, d, rfl⟩
  obtain ⟨e, he⟩ := preservesDiag_conj_of_monomial hK d
  exact ⟨quantum_conj K _ hX, ⟨e, he⟩⟩

theorem classical_primitive : PrimitivePreservation classicalClass classicalCone where
  op := fun _ _ _ K hK _ => classical_conj K hK
  readout := fun _ _ _ _ _ _ _ _ hP k => classical_conj _ (hP k)

theorem classical_attach : UniformAttachPreservation classicalCone := by
  rintro S _ _ m hm X ⟨hX, d, rfl⟩
  refine ⟨quantum_attach S m hm _ hX, ⟨fun p => (m : ℂ)⁻¹ * d p.1, ?_⟩⟩
  ext p q
  by_cases hs : p.1 = q.1 <;> by_cases he : p.2 = q.2 <;>
    simp [uniformAttach_apply, tensorOf_apply, Matrix.diagonal,
      Matrix.smul_apply, hs, he, Prod.ext_iff, mul_comm]

theorem classical_discard : AncillaDiscardPreservation classicalCone := by
  rintro S _ _ m hm X ⟨hX, d, rfl⟩
  refine ⟨quantum_discard S m hm _ hX, ⟨fun s => ∑ e : Fin m, d (s, e), ?_⟩⟩
  ext s t
  by_cases h : s = t <;> simp [ptraceAnc_apply, Matrix.diagonal, h]

/-- Every native coordinate readout is actually admitted by the classical inventory. -/
theorem classical_readProj {S T : Type} [Fintype S] [DecidableEq S]
    [Fintype T] [DecidableEq T] (m : ℕ) (e : T × Fin m ≃ S) (k : Fin m) :
    classicalClass S (Matrix.reindex e e (readProj T m k)) := by
  exact substratumClass_labelInvariant _ _ e _ (monomial_diagonal _)

theorem classical_instAvail
    {S : Type} [Fintype S] [DecidableEq S] {O : Type} [Fintype O] [DecidableEq O]
    {F : O → Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ} (h : InstAvail classicalClass S O F) :
    ∀ a, PreservesCarrier classicalCone S (F a) :=
  instAvail_preserves classicalCone classical_additive classical_primitive
    classical_attach classical_discard h

/-- A concrete native-register family; admission is proved rather than assumed. -/
theorem classical_native_readout {S T : Type} [Fintype S] [DecidableEq S]
    [Fintype T] [DecidableEq T] (m : ℕ) (e : T × Fin m ≃ S) :
    ∀ k, PreservesCarrier classicalCone S
      (conjChannel (Matrix.reindex e e (readProj T m k))) := by
  apply classical_instAvail
  exact InstAvail.readout e (classical_readProj m e)

-- The existing classical inventory also supplies the spectator/transport premises.
example : ContextStable classicalClass := substratumClass_contextStable
example : LabelInvariant classicalClass := substratumClass_labelInvariant

#print axioms quantum_instAvail
#print axioms classical_instAvail
#print axioms quantum_attach
#print axioms quantum_discard
#print axioms classical_readProj
#print axioms classical_native_readout

end OIBridge.PreservationInductionDesign
