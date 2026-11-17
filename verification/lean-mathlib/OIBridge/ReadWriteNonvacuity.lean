import OIBridge.ReadWriteControl
import OIBridge.SubstratumInterfaceAudit

/-!
# KERNEL-VAC-1: the original read/write source predicate is empty on `Fin 2`

The compulsory defect control uses the original `ReadWriteSourced` unchanged.
Level-one identity availability follows from the actual theory's readout and
coarse-graining fields. Its globally phased representative `I • 1` has the same
channel but is not an exact permutation matrix. This is a defect of that
predicate, not a physical impossibility theorem about read/write interaction.

The sole preregistered witness uses the existing `permTheory (Fin 2)`.
Its available branches are finite sums of conjugations by scaled partial
permutations. Evaluating an equality of channels on matrix units transfers
their row and column sparsity to every single-matrix representative. No
isometry or nonempty-carrier assumption is imposed on that representative.
-/

namespace OIBridge
namespace ReadWriteNonvacuity

open Complex Matrix MonoidalCompletion CoherentLift OperationalAssembly
open ReadWriteControl
open AncillaClosure InterventionLocality StructuralClosure SubstratumInterface
open SubstratumInterfaceAudit

variable {A : Type} [Fintype A] [DecidableEq A]

/-- The one-outcome native selector is identity, including on an empty system. -/
theorem localLuders_one_eq_id :
    localLuders (A := A) (0 : Fin 1) = LinearMap.id := by
  apply LinearMap.ext
  intro X
  ext ⟨a, i⟩ ⟨b, j⟩
  have hi : i = (0 : Fin 1) := Subsingleton.elim _ _
  have hj : j = (0 : Fin 1) := Subsingleton.elim _ _
  subst i
  subst j
  simp [localLuders_apply]

/-- Identity availability is derived from native readout and coarse-graining;
matrix admissibility is not used as an availability premise. -/
theorem levelOne_id_available (T : FiniteOperationalTheory A) :
    T.availExt 1 Unit (fun _ => LinearMap.id) := by
  have hav := T.availExt_coarse 1 (Fin 1) Unit (T.readout 1)
    (fun _ => (() : Unit)) (T.readout_avail 1)
  convert hav using 1
  funext a
  cases a
  simp [readout_is_localLuders, Fintype.sum_unique, localLuders_one_eq_id]

/-- Global quarter phase does not change the identity conjugation channel. -/
theorem quarterPhase_conjChannel :
    conjChannel (Complex.I • (1 : Matrix (Fin 2 × Fin 1) (Fin 2 × Fin 1) ℂ)) =
      LinearMap.id := by
  rw [ReachabilitySeam.conjChannel_smul (by simp : ‖Complex.I‖ = 1)]
  apply LinearMap.ext
  intro X
  simp [conjChannel]

/-- At a concrete diagonal entry, the phased identity has imaginary part one;
every entry of an exact permutation matrix has imaginary part zero. -/
theorem quarterPhase_not_perm (σ : Equiv.Perm (Fin 2 × Fin 1)) :
    Complex.I • (1 : Matrix (Fin 2 × Fin 1) (Fin 2 × Fin 1) ℂ) ≠ permMatrix σ := by
  intro h
  have he := congrArg (fun K : Matrix (Fin 2 × Fin 1) (Fin 2 × Fin 1) ℂ =>
    (K (0, 0) (0, 0)).im) h
  by_cases hs : σ (0, 0) = (0, 0)
  · norm_num [permMatrix, hs, Matrix.smul_apply, smul_eq_mul] at he
  · norm_num [permMatrix, hs, Matrix.smul_apply, smul_eq_mul] at he

/-- **COMPULSORY DEFECT CONTROL.** No `Fin 2` theory satisfies the original
representative-sensitive source predicate. No statement about the empty carrier
or the `n = 0` extension is inferred from this nonempty level-one contradiction. -/
theorem readWriteSourced_fin2_impossible :
    ∀ T : FiniteOperationalTheory (Fin 2), ¬ ReadWriteSourced T := by
  intro T h
  have hav : T.availExt 1 Unit (fun _ =>
      conjChannel (Complex.I • (1 : Matrix (Fin 2 × Fin 1) (Fin 2 × Fin 1) ℂ))) := by
    rw [quarterPhase_conjChannel]
    exact levelOne_id_available T
  obtain ⟨σ, hσ⟩ := h 1 _ hav
  exact quarterPhase_not_perm σ hσ

section Witness

variable {S : Type} [Fintype S] [DecidableEq S]

/-- Matrix-unit evaluation exposes the coefficient of a single conjugation. -/
theorem conjChannel_single_entry (K : Matrix S S ℂ) (a b c d : S) :
    conjChannel K (Matrix.single b d 1) a c = K a b * star (K c d) := by
  rw [conjChannel_apply, Matrix.mul_apply, Finset.sum_eq_single d]
  · rw [Matrix.mul_single_apply_same, Matrix.conjTranspose_apply]
    simp
  · intro x _ hx
    simp [Matrix.mul_apply, Matrix.single, Ne.symm hx]
  · intro hd
    exact absurd (Finset.mem_univ d) hd

/-- A single-matrix representative of a branch realized by `permClass` is
monomial. The proof uses all representatives, not just the chosen Kraus family;
it also covers the zero matrix, rank-deficient matrices and the empty carrier. -/
theorem monomial_of_realized_permClass {V : Matrix S S ℂ}
    (h : Realized permClass S (conjChannel V)) : IsMonomial V := by
  classical
  obtain ⟨ι, inst, K, hEq, hK⟩ := h
  letI : Fintype ι := inst
  have he : ∀ a b c d : S,
      V a b * star (V c d) = ∑ k, K k a b * star (K k c d) := by
    intro a b c d
    have hentry := congrArg
      (fun Φ : Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ => Φ (Matrix.single b d 1) a c) hEq
    simpa only [LinearMap.sum_apply, Matrix.sum_apply, conjChannel_single_entry] using hentry
  apply submonomial_monomial
  constructor
  · intro i j j' hj hj'
    by_contra hne
    have hz : V i j * star (V i j') = 0 := by
      rw [he]
      apply Finset.sum_eq_zero
      intro k _
      by_cases hp : K k i j = 0
      · simp [hp]
      · have hq : K k i j' = 0 := by
          by_contra hq
          exact hne ((hK k).1.1 i j j' hp hq)
        simp [hq]
    exact (mul_ne_zero hj (star_ne_zero.mpr hj')) hz
  · intro i i' j hi hi'
    by_contra hne
    have hz : V i j * star (V i' j) = 0 := by
      rw [he]
      apply Finset.sum_eq_zero
      intro k _
      by_cases hp : K k i j = 0
      · simp [hp]
      · have hq : K k i' j = 0 := by
          by_contra hq
          exact hne ((hK k).1.2 i i' j hp hq)
        simp [hq]
    exact (mul_ne_zero hi (star_ne_zero.mpr hi')) hz

end Witness

/-- **SOLE PREREGISTERED WITNESS.** The existing generated theory inhabits
`MonomialSource` on `Fin 2`, at every extension level (including zero), for
every matrix representative of an available conjugation. Its availability,
coarse-graining, composition and preparation fields are the unchanged fields
of `genTheory permClass permClass_arch`; this is a mathematical theory witness,
not a derivation of native physical availability. -/
theorem permTheory_fin2_monomialSource :
    SubstratumInterface.MonomialSource (SubstratumInterfaceAudit.permTheory (Fin 2)) := by
  intro n V hav
  exact monomial_of_realized_permClass (realized_of_instAvail permClass_arch hav ())

#print axioms localLuders_one_eq_id
#print axioms levelOne_id_available
#print axioms quarterPhase_conjChannel
#print axioms quarterPhase_not_perm
#print axioms readWriteSourced_fin2_impossible
#print axioms conjChannel_single_entry
#print axioms monomial_of_realized_permClass
#print axioms permTheory_fin2_monomialSource

end ReadWriteNonvacuity
end OIBridge
