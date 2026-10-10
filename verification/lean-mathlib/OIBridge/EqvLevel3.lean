/-
  OIBridge/EqvLevel3.lean — design module of the research thread `research/equivalence` (node E9).
  Not adopted, not certified, not a round: the Level III converse, stated and bounded.

  Level III (`QuasilocalCharacterization`) proves uniqueness among systems of the target class: the
  canonical map is the unique continuous stage-compatible map (`canon_unique`), and two OI systems
  with the same substratum dynamics are isomorphic compatibly with their automorphisms
  (`systemEquiv_dyn`). This module states three facts about the converse direction.

  (A) THE NAIVE DYNAMICAL CONVERSE FAILS. `NaiveConverseDyn ι Q`: every locality-preserving star
  automorphism of every system of the target class acts on the stages as the transport of some
  reversible finite-range substratum dynamics. It is false (`not_naiveConverseDyn`): on the OI region
  completion the phase automorphism preserves locality and agrees with no OI-induced dynamics on the
  stages (`phase_not_oiInduced`, from the landed `phaseQ_ne_heisQ` by continuity and density).

  (B) THE TARGET CLASS CARRIES THE QUANTUM KINEMATICS IN ITS DEFINITION. Every system of the class
  with at least two states per site has a noncommutative algebra (`not_comm_of_system`), so no
  commutative quasilocal net — a classical lattice — is a member, whatever its locality and density.

  (C) THE PER-REGION CONVERSE IS TRANSFER ALONG THE STAGE MAP. For every system of the class and
  every region, a family of stage elements is Kraus-normalized in the algebra exactly when the
  matrices are Kraus-normalized (`kraus_iff_of_member`): the finite-support instruments of any member
  on a region are the Kraus instruments of the region's matrix algebra.

  Nothing here derives the matrix-algebra stages, a dynamics, or any OI_Q condition from anything
  weaker than the class's definition.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.QuasilocalCharacterization

namespace OIBridge
namespace EqvLevel3

open Complex Matrix RegionTower QuasilocalAlgebra QuasilocalCharacterization
open scoped ComplexOrder Matrix.Norms.L2Operator

set_option linter.unusedSectionVars false
set_option maxHeartbeats 1000000

variable {ι Q : Type} [DecidableEq ι] [Fintype Q] [DecidableEq Q] [Nonempty Q]

/-! ### §A — the naive dynamical converse -/

/-- **The phase automorphism is OI-induced by no substratum dynamics, already on the stages.** -/
theorem phase_not_oiInduced [Nontrivial Q] (i₀ : ι) (Φ : ReversibleDynamics ι Q) :
    ¬ ∀ (Λ : Finset ι) (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ),
        phaseEquiv i₀ (stage Λ X) = stage (hat Φ Λ) (transported Φ Λ X) := by
  intro h
  apply phaseQ_ne_heisQ i₀ Φ
  funext x
  refine UniformSpace.Completion.induction_on x
    (isClosed_eq (continuous_phaseQ i₀) (continuous_heisQ Φ)) fun a => ?_
  obtain ⟨Λ, X, rfl⟩ := exists_ofM a
  rw [← stage_apply, ← phaseEquiv_apply, h, heisQ_stage]

/-- The naive dynamical converse of Level III: every locality-preserving star automorphism of a
system of the target class is the transport of a reversible finite-range substratum dynamics. -/
def NaiveConverseDyn (ι Q : Type) [DecidableEq ι] [Fintype Q] [DecidableEq Q] [Nonempty Q] :
    Prop :=
  ∀ (S : QuasilocalSystem ι Q) (α : S.A ≃⋆ₐ[ℂ] S.A), LocalityPreserving S α →
    ∃ Φ : ReversibleDynamics ι Q, ∀ (Λ : Finset ι) (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ),
      α (S.st Λ X) = S.st (hat Φ Λ) (transported Φ Λ X)

/-- **The naive dynamical converse is false** as soon as there is a site and two states. -/
theorem not_naiveConverseDyn [Nontrivial Q] (i₀ : ι) : ¬ NaiveConverseDyn ι Q := by
  intro h
  obtain ⟨Φ, hΦ⟩ := h oiSystem (phaseEquiv i₀) (phase_localityPreserving i₀)
  exact phase_not_oiInduced i₀ Φ hΦ

/-! ### §B — the class carries noncommutative stages -/

/-- **Every system of the target class is noncommutative** when a site has two states. -/
theorem not_comm_of_system [Nontrivial Q] (S : QuasilocalSystem ι Q) (i₀ : ι) :
    ∃ a b : S.A, a * b ≠ b * a := by
  obtain ⟨q₀, q₁, hq⟩ := exists_pair_ne Q
  let Λ₀ : Finset ι := {i₀}
  let f₀ : Conf Λ₀ Q := fun _ => q₀
  let f₁ : Conf Λ₀ Q := fun _ => q₁
  have hf : f₀ ≠ f₁ := fun h => hq (congrFun h ⟨i₀, Finset.mem_singleton_self i₀⟩)
  refine ⟨S.st Λ₀ (Matrix.single f₀ f₁ 1), S.st Λ₀ (Matrix.single f₁ f₀ 1), fun h => ?_⟩
  rw [← map_mul, ← map_mul] at h
  have h2 := S.injective Λ₀ h
  rw [Matrix.single_mul_single_same, Matrix.single_mul_single_same] at h2
  have h3 := congrArg (fun M : Matrix (Conf Λ₀ Q) (Conf Λ₀ Q) ℂ => M f₀ f₀) h2
  simp [Matrix.single_apply, hf.symm] at h3

/-! ### §C — the per-region converse is transfer along the stage map -/

/-- **Kraus normalization transfers along any member's stage map, in both directions.** -/
theorem kraus_iff_of_member (S : QuasilocalSystem ι Q) {n : ℕ} (Λ : Finset ι)
    (K : Fin n → Matrix (Conf Λ Q) (Conf Λ Q) ℂ) :
    (∑ k, star (S.st Λ (K k)) * S.st Λ (K k) = 1) ↔ ∑ k, (K k)ᴴ * K k = 1 := by
  have h : ∀ k, S.st Λ ((K k)ᴴ * K k) = star (S.st Λ (K k)) * S.st Λ (K k) := by
    intro k
    rw [map_mul, ← Matrix.star_eq_conjTranspose, map_star]
  have hsum : S.st Λ (∑ k, (K k)ᴴ * K k) = ∑ k, star (S.st Λ (K k)) * S.st Λ (K k) := by
    rw [map_sum]
    exact Finset.sum_congr rfl fun k _ => h k
  constructor
  · intro h1
    apply S.injective Λ
    rw [hsum, h1, map_one]
  · intro h1
    rw [← hsum, h1, map_one]

end EqvLevel3
end OIBridge

#print axioms OIBridge.EqvLevel3.phase_not_oiInduced
#print axioms OIBridge.EqvLevel3.not_naiveConverseDyn
#print axioms OIBridge.EqvLevel3.not_comm_of_system
#print axioms OIBridge.EqvLevel3.kraus_iff_of_member
