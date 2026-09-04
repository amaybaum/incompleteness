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

/-! ### The layer unitary -/

/-- **THE SWAP LAYER'S UNITARY FOR A REGION**: the product over that region's gates, taken without
choosing an order because they commute. -/
noncomputable def swapU (S : Finset ι) (t : ℝ) : Quasilocal ι (V × V) :=
  S.noncommProd (fun i => unit (swapGate V i) t)
    (fun i _ j _ _ => unit_swapGate_comm V i j t t)

@[simp] theorem swapU_empty (t : ℝ) : swapU V (∅ : Finset ι) t = 1 :=
  Finset.noncommProd_empty _ _

theorem swapU_union {S T : Finset ι} (h : Disjoint S T) (t : ℝ) :
    swapU V (S ∪ T) t = swapU V S t * swapU V T t :=
  Finset.noncommProd_union_of_disjoint h _ _

theorem swapU_singleton (i : ι) (t : ℝ) :
    swapU V ({i} : Finset ι) t = unit (swapGate V i) t := by
  rw [swapU, Finset.noncommProd_singleton]

theorem swapU_star (S : Finset ι) (t : ℝ) : swapU V S t * star (swapU V S t) = 1 := by
  classical
  induction S using Finset.induction_on with
  | empty => simp
  | insert i s hi ih =>
      have hdis : Disjoint ({i} : Finset ι) s := by simpa using hi
      have hins : (insert i s : Finset ι) = {i} ∪ s := by rw [Finset.insert_eq]
      rw [hins, swapU_union V hdis, star_mul]
      calc swapU V ({i}) t * swapU V s t * (star (swapU V s t) * star (swapU V ({i}) t))
          = swapU V ({i}) t * (swapU V s t * star (swapU V s t)) * star (swapU V ({i}) t) := by
            simp only [mul_assoc]
        _ = swapU V ({i}) t * star (swapU V ({i}) t) := by rw [ih, mul_one]
        _ = 1 := by
            rw [swapU_singleton]
            exact unit_mul_star_unit (swapGate_isGate V i).1 (swapGate_isGate V i).2 t

theorem star_swapU_mul (S : Finset ι) (t : ℝ) : star (swapU V S t) * swapU V S t = 1 := by
  classical
  induction S using Finset.induction_on with
  | empty => simp
  | insert i s hi ih =>
      have hdis : Disjoint ({i} : Finset ι) s := by simpa using hi
      have hins : (insert i s : Finset ι) = {i} ∪ s := by rw [Finset.insert_eq]
      rw [hins, swapU_union V hdis, star_mul]
      calc star (swapU V s t) * star (swapU V ({i}) t) * (swapU V ({i}) t * swapU V s t)
          = star (swapU V s t) * (star (swapU V ({i}) t) * swapU V ({i}) t) * swapU V s t := by
            simp only [mul_assoc]
        _ = star (swapU V s t) * swapU V s t := by
            rw [swapU_singleton,
              star_unit_mul_unit (swapGate_isGate V i).1 (swapGate_isGate V i).2 t, mul_one]
        _ = 1 := ih

theorem swapU_mem_unitary (S : Finset ι) (t : ℝ) :
    swapU V S t ∈ unitary (Quasilocal ι (V × V)) :=
  Unitary.mem_iff.mpr ⟨star_swapU_mul V S t, swapU_star V S t⟩

theorem swapU_zero (S : Finset ι) : swapU V S 0 = 1 := by
  classical
  induction S using Finset.induction_on with
  | empty => simp
  | insert i s hi ih =>
      have hdis : Disjoint ({i} : Finset ι) s := by simpa using hi
      have hins : (insert i s : Finset ι) = {i} ∪ s := by rw [Finset.insert_eq]
      rw [hins, swapU_union V hdis, swapU_singleton, unit_zero, one_mul, ih]

/-- **THE LAYER UNITARIES COMPOSE BY ADDING TIMES.** -/
theorem swapU_add (S : Finset ι) (t s : ℝ) : swapU V S t * swapU V S s = swapU V S (t + s) := by
  classical
  induction S using Finset.induction_on with
  | empty => simp
  | insert i r hi ih =>
      have hdis : Disjoint ({i} : Finset ι) r := by simpa using hi
      have hins : (insert i r : Finset ι) = {i} ∪ r := by rw [Finset.insert_eq]
      have hcross : swapU V r t * unit (swapGate V i) s = unit (swapGate V i) s * swapU V r t := by
        rw [swapU]
        exact (Finset.noncommProd_commute r _ _ _
          fun j _ => unit_swapGate_comm V i j s t).symm
      rw [hins, swapU_union V hdis, swapU_union V hdis, swapU_union V hdis,
        swapU_singleton, swapU_singleton, swapU_singleton]
      calc unit (swapGate V i) t * swapU V r t * (unit (swapGate V i) s * swapU V r s)
          = unit (swapGate V i) t * (swapU V r t * unit (swapGate V i) s) * swapU V r s := by
            simp only [mul_assoc]
        _ = unit (swapGate V i) t * (unit (swapGate V i) s * swapU V r t) * swapU V r s := by
            rw [hcross]
        _ = (unit (swapGate V i) t * unit (swapGate V i) s) * (swapU V r t * swapU V r s) := by
            simp only [mul_assoc]
        _ = unit (swapGate V i) (t + s) * swapU V r (t + s) := by
            rw [unit_mul_unit (swapGate_isGate V i).1, ih]

/-- **THE LAYER UNITARY IS SUPPORTED IN ITS REGION.** For the swap layer the gates' span is the
region itself, since each gate occupies one site. -/
theorem swapU_mem_range (S : Finset ι) (t : ℝ) :
    swapU V S t ∈ Set.range (stage S) := by
  classical
  induction S using Finset.induction_on with
  | empty =>
      rw [swapU_empty]
      exact mem_range_stage_one _
  | insert i s hi ih =>
      have hdis : Disjoint ({i} : Finset ι) s := by simpa using hi
      have hins : (insert i s : Finset ι) = {i} ∪ s := by rw [Finset.insert_eq]
      have h1 : ({i} : Finset ι) ⊆ insert i s := by simpa using Finset.mem_insert_self i s
      have h2 : s ⊆ insert i s := Finset.subset_insert i s
      rw [hins, swapU_union V hdis, swapU_singleton]
      exact mem_range_stage_mul
        (mem_range_stage_le h1 (unit_swapGate_mem_range V i t))
        (mem_range_stage_le h2 ih)

theorem continuous_unit_swapGate (i : ι) :
    Continuous fun t : ℝ => unit (swapGate V i) t := by
  unfold unit
  fun_prop

theorem continuous_swapU (S : Finset ι) : Continuous fun t : ℝ => swapU V S t := by
  classical
  induction S using Finset.induction_on with
  | empty => simpa using continuous_const
  | insert i s hi ih =>
      have hdis : Disjoint ({i} : Finset ι) s := by simpa using hi
      have hins : (insert i s : Finset ι) = {i} ∪ s := by rw [Finset.insert_eq]
      simp only [hins, fun t => swapU_union V hdis t, fun t => swapU_singleton V i t]
      exact (continuous_unit_swapGate V i).mul ih

end OIBridge.SwapLayer

namespace OIBridge.SwapLayer

#print axioms swapConf_involutive
#print axioms swapGate_isGate
#print axioms swapGate_comm
#print axioms unit_swapGate_comm
#print axioms unit_swapGate_comm_stage
#print axioms unit_swapGate_mem_range
#print axioms swapU_union
#print axioms swapU_singleton
#print axioms swapU_star
#print axioms star_swapU_mul
#print axioms swapU_mem_unitary
#print axioms swapU_zero
#print axioms swapU_add
#print axioms swapU_mem_range
#print axioms continuous_swapU

end OIBridge.SwapLayer
