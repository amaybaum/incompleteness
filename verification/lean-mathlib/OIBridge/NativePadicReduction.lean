import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.Group.Hom.Defs

/-!
# SUBSTATE-2 NATIVE-PADIC-1: additive quotient bridge for cubic wave stencils

Research only. This theorem is about the exact six-neighbor
integer-coefficient wave update, at any alphabet additive groups.
Any additive homomorphism from a fine to coarse alphabet commutes
with the one-step and inverse two-slice wave update *provided the
same finite neighbor stencil is used*. Hence compatible modular
reductions cannot carry high-to-low digit feedback through this
unchanged native linear update.

No theorem here constructs a physical OI p-adic state space,
selects a gauge field, derives a quantum operation, or proves
continuity-to-finite-stage factorization. This is a mathematical
source obstruction for passive congruence readout only.
-/

namespace OIBridge.NativePadicReduction

universe u v w
variable {I : Type u} {D : Type v} [Fintype D]
variable {A : Type w} [AddCommGroup A]

def neighborSum (neighbors : I → D → I) (field : I → A) (i : I) : A :=
  ∑ d : D, field (neighbors i d)

/-- A reversible two-slice update with the native linear neighbor stencil. -/
def waveStep (neighbors : I → D → I)
    (s : (I → A) × (I → A)) : (I → A) × (I → A) :=
  ((fun i => neighborSum neighbors s.1 i - s.2 i), s.1)

/-- The exact backward update, not a probabilistic inverse. -/
def waveUnstep (neighbors : I → D → I)
    (s : (I → A) × (I → A)) : (I → A) × (I → A) :=
  (s.2, (fun i => neighborSum neighbors s.2 i - s.1 i))

variable {B : Type*} [AddCommGroup B]

/-- Reduce both time slices pointwise using an additive group hom. -/
def projectState (p : A →+ B) (s : (I → A) × (I → A)) :
    (I → B) × (I → B) :=
  ((fun i => p (s.1 i)), (fun i => p (s.2 i)))

theorem neighborSum_map (p : A →+ B) (neighbors : I → D → I)
    (field : I → A) (i : I) :
    p (neighborSum neighbors field i) =
      neighborSum neighbors (fun j => p (field j)) i := by
  simp [neighborSum, map_sum]

/-- Exact one-step source test; applies to each residue quotient. -/
theorem project_waveStep (p : A →+ B)
    (neighbors : I → D → I) (s : (I → A) × (I → A)) :
    projectState p (waveStep neighbors s) =
      waveStep neighbors (projectState p s) := by
  apply Prod.ext
  · funext i
    simp [projectState, waveStep, neighborSum, map_sub, map_sum]
  · rfl

/-- The same quotient also commutes with the inverse. -/
theorem project_waveUnstep (p : A →+ B)
    (neighbors : I → D → I) (s : (I → A) × (I → A)) :
    projectState p (waveUnstep neighbors s) =
      waveUnstep neighbors (projectState p s) := by
  apply Prod.ext
  · rfl
  · funext i
    simp [projectState, waveUnstep, neighborSum, map_sub, map_sum]

#print axioms neighborSum_map
#print axioms project_waveStep
#print axioms project_waveUnstep

end OIBridge.NativePadicReduction
