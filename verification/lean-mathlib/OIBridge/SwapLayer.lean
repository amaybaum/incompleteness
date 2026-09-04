import OIBridge.SecondOrderLayer

/-!
# The swap layer

The second layer of the depth-two circuit. Its gates are the on-site exchanges of a site's two
components, so a gate occupies a **single site**. That makes the whole development shorter than the
shear layer's: a region feels only the gates inside it, the affected set of a region is the region
itself, commutation is disjointness of distinct singletons, and blindness is non-membership. No
dependency region, influence set or gate span appears.

The layer-independent machinery — `qGate` and its self-adjoint-unitary lemma, the commutation of a
gate's unitary with a disjoint region's observables, the stage-range family — is reused from
`SecondOrderLayer` rather than repeated.

The alphabet is an explicit argument of the definitions whose type mentions it only in the result:
a swap gate has no argument to infer it from.
-/

namespace OIBridge.SwapLayer

open OIBridge.QuasilocalAlgebra OIBridge.RegionTower OIBridge.SecondOrderCircuit
open OIBridge.QuasilocalCharacterization OIBridge.SecondOrderLayer
open Matrix

set_option maxHeartbeats 1200000

variable {ι : Type} [DecidableEq ι]

/-! ### The gate -/

section Gate

variable {V : Type} [Fintype V] [DecidableEq V] [Nonempty V]

/-- The on-site exchange of the two components at one site. -/
def swapConf (i : ι) (x : Conf ({i} : Finset ι) (V × V)) : Conf ({i} : Finset ι) (V × V) :=
  fun u => ((x u).2, (x u).1)

theorem swapConf_involutive (i : ι) (x : Conf ({i} : Finset ι) (V × V)) :
    swapConf i (swapConf i x) = x := by
  funext u
  rfl

end Gate

/-- The swap gate at a site, as a permutation of that site's configurations. The alphabet is
explicit: nothing in the statement determines it otherwise. -/
def swapEquivAt (V : Type) [Fintype V] [DecidableEq V] [Nonempty V] (i : ι) :
    Conf ({i} : Finset ι) (V × V) ≃ Conf ({i} : Finset ι) (V × V) where
  toFun := swapConf i
  invFun := swapConf i
  left_inv := swapConf_involutive i
  right_inv := swapConf_involutive i

/-- **THE SWAP GATE IN THE QUASILOCAL ALGEBRA.** -/
noncomputable def swapGate (V : Type) [Fintype V] [DecidableEq V] [Nonempty V] (i : ι) :
    Quasilocal ι (V × V) :=
  qGate {i} (swapEquivAt V i)

variable (V : Type) [Fintype V] [DecidableEq V] [Nonempty V] [AddCommGroup V]

theorem swapGate_isGate (i : ι) :
    swapGate V i * swapGate V i = 1 ∧ star (swapGate V i) = swapGate V i :=
  qGate_isGate (swapConf_involutive i)

/-- **THE SWAP GATES COMMUTE**, by disjointness of single sites. -/
theorem swapGate_comm (i j : ι) : swapGate V i * swapGate V j = swapGate V j * swapGate V i := by
  by_cases h : i = j
  · subst h; rfl
  · exact stage_comm_of_disjoint (by simpa using h) _ _

theorem unit_swapGate_comm (i j : ι) (t s : ℝ) :
    unit (swapGate V i) t * unit (swapGate V j) s
      = unit (swapGate V j) s * unit (swapGate V i) t :=
  unit_comm (swapGate_comm V i j) t s

/-- **A GATE OUTSIDE THE REGION IS BLIND TO IT.** For the swap layer this is immediate: a gate
occupies one site, so it is blind exactly when that site lies outside. -/
theorem unit_swapGate_comm_stage {Λ : Finset ι} {i : ι} (hi : i ∉ Λ)
    (Y : Matrix (Conf Λ (V × V)) (Conf Λ (V × V)) ℂ) (t : ℝ) :
    unit (swapGate V i) t * stage Λ Y = stage Λ Y * unit (swapGate V i) t :=
  unit_qGate_comm_stage_of_disjoint (by simpa using hi) _ Y t

theorem unit_swapGate_mem_range (i : ι) (t : ℝ) :
    unit (swapGate V i) t ∈ Set.range (stage ({i} : Finset ι)) := by
  rw [unit, proj]
  refine mem_range_stage_add (mem_range_stage_one _) (mem_range_stage_smul _ ?_)
  exact mem_range_stage_smul _ (mem_range_stage_sub (mem_range_stage_one _) ⟨_, rfl⟩)

end OIBridge.SwapLayer

namespace OIBridge.SwapLayer

#print axioms swapConf_involutive
#print axioms swapGate_isGate
#print axioms swapGate_comm
#print axioms unit_swapGate_comm
#print axioms unit_swapGate_comm_stage
#print axioms unit_swapGate_mem_range

end OIBridge.SwapLayer
