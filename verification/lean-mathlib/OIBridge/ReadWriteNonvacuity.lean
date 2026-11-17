import OIBridge.ReadWriteControl

/-!
# KERNEL-VAC-1: the original read/write source predicate is empty on `Fin 2`

The compulsory defect control uses the original `ReadWriteSourced` unchanged.
Level-one identity availability follows from the actual theory's readout and
coarse-graining fields. Its globally phased representative `I • 1` has the same
channel but is not an exact permutation matrix. This is a defect of that
predicate, not a physical impossibility theorem about read/write interaction.

Checkpoint 1 contains only the defect control. The sole preregistered
`MonomialSource (permTheory (Fin 2))` witness remains a separate obligation.
-/

namespace OIBridge
namespace ReadWriteNonvacuity

open Complex Matrix MonoidalCompletion CoherentLift OperationalAssembly
open ReadWriteControl

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

#print axioms localLuders_one_eq_id
#print axioms levelOne_id_available
#print axioms quarterPhase_conjChannel
#print axioms quarterPhase_not_perm
#print axioms readWriteSourced_fin2_impossible

end ReadWriteNonvacuity
end OIBridge
