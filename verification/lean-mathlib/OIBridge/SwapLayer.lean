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

/-! ### The layer's action, and its stabilization -/

/-- **THE SWAP LAYER'S ACTION ON A REGION'S OBSERVABLES.** -/
noncomputable def swapAct (S : Finset ι) (t : ℝ) (a : Quasilocal ι (V × V)) :
    Quasilocal ι (V × V) :=
  swapU V S t * a * star (swapU V S t)

/-- **STABILIZATION.** Enlarging the set of gates beyond the observable's own region changes
nothing: the extra gates sit on sites outside it, so they commute with it and cancel. For the swap
layer the affected set of a region is the region itself, which is why the hypothesis here is plain
inclusion rather than an inclusion of affected sets. -/
theorem swapAct_stabilizes {Λ S : Finset ι} (hS : Λ ⊆ S)
    (X : Matrix (Conf Λ (V × V)) (Conf Λ (V × V)) ℂ) (t : ℝ) :
    swapAct V S t (stage Λ X) = swapAct V Λ t (stage Λ X) := by
  classical
  set W := S \ Λ with hW
  have hdis : Disjoint Λ W := Finset.disjoint_sdiff
  have hSU : S = Λ ∪ W := by rw [hW, Finset.union_sdiff_of_subset hS]
  have hcw : swapU V W t * stage Λ X = stage Λ X * swapU V W t := by
    rw [swapU]
    refine (Finset.noncommProd_commute W _ _ _ fun j hj => ?_).symm
    have hjn : j ∉ Λ := (Finset.mem_sdiff.mp (hW ▸ hj)).2
    exact (unit_swapGate_comm_stage V hjn X t).symm
  rw [swapAct, swapAct, hSU, swapU_union V hdis, star_mul]
  calc swapU V Λ t * swapU V W t * stage Λ X * (star (swapU V W t) * star (swapU V Λ t))
      = swapU V Λ t * (swapU V W t * stage Λ X * star (swapU V W t)) * star (swapU V Λ t) := by
        simp only [mul_assoc]
    _ = swapU V Λ t * stage Λ X * star (swapU V Λ t) := by
        rw [conj_eq_self_of_commute (swapU_star V W t) hcw]

/-- **THE LAYER KEEPS A LOCAL OBSERVABLE LOCAL.** -/
theorem swapAct_mem_range (S Λ : Finset ι) (t : ℝ)
    (X : Matrix (Conf Λ (V × V)) (Conf Λ (V × V)) ℂ) :
    swapAct V S t (stage Λ X) ∈ Set.range (stage (Λ ∪ S)) := by
  have hU : swapU V S t ∈ Set.range (stage (Λ ∪ S)) :=
    mem_range_stage_le Finset.subset_union_right (swapU_mem_range V S t)
  have hX : stage Λ X ∈ Set.range (stage (Λ ∪ S)) :=
    mem_range_stage_le Finset.subset_union_left ⟨X, rfl⟩
  exact mem_range_stage_mul (mem_range_stage_mul hU hX) (mem_range_stage_star hU)

/-- **THE SWAP LAYER KEEPS AN OBSERVABLE IN ITS OWN REGION.** Unlike the shear layer, whose gates
reach outside the region they act on, a swap gate occupies one site, so no enlargement occurs. -/
theorem swapAct_mem_range_self (Λ : Finset ι) (t : ℝ)
    (X : Matrix (Conf Λ (V × V)) (Conf Λ (V × V)) ℂ) :
    swapAct V Λ t (stage Λ X) ∈ Set.range (stage Λ) := by
  have hU : swapU V Λ t ∈ Set.range (stage Λ) := swapU_mem_range V Λ t
  exact mem_range_stage_mul (mem_range_stage_mul hU ⟨X, rfl⟩) (mem_range_stage_star hU)

/-! ### The layer as a map on the local algebra -/

/-- **THE SWAP LAYER ON A LOCAL OBSERVABLE.** -/
noncomputable def swapLoc (t : ℝ) (a : localAlg ι (V × V)) : Quasilocal ι (V × V) :=
  swapAct V (rep a).1 t (a : Quasilocal ι (V × V))

/-- Two regions carrying the same observable give the same action. As in the shear layer, the
*element* is rewritten rather than the region, which sits in a dependent type. -/
theorem swapAct_eq_of_stage_eq {Λ Λ' : Finset ι}
    (X : Matrix (Conf Λ (V × V)) (Conf Λ (V × V)) ℂ)
    (X' : Matrix (Conf Λ' (V × V)) (Conf Λ' (V × V)) ℂ)
    (h : stage Λ X = stage Λ' X') (t : ℝ) :
    swapAct V Λ t (stage Λ X) = swapAct V Λ' t (stage Λ' X') := by
  have e1 := swapAct_stabilizes V (Finset.subset_union_left (s₂ := Λ')) X t
  have e2 := swapAct_stabilizes V (Finset.subset_union_right (s₁ := Λ)) X' t
  rw [← e1, ← e2, h]

/-- **INDEPENDENCE OF THE REPRESENTATIVE.** -/
theorem swapLoc_ofM (t : ℝ) (Λ : Finset ι)
    (X : Matrix (Conf Λ (V × V)) (Conf Λ (V × V)) ℂ) :
    swapLoc V t (ofM Λ X) = swapAct V Λ t (stage Λ X) := by
  classical
  have h : stage (rep (ofM Λ X)).1 (rep (ofM Λ X)).2 = stage Λ X := by
    rw [stage_apply, stage_apply, ofM_rep]
  have hL : swapLoc V t (ofM Λ X)
      = swapAct V (rep (ofM Λ X)).1 t (stage (rep (ofM Λ X)).1 (rep (ofM Λ X)).2) := by
    rw [swapLoc, h]
    rfl
  rw [hL]
  exact swapAct_eq_of_stage_eq V _ X h t

theorem swapLoc_mul (t : ℝ) (a b : localAlg ι (V × V)) :
    swapLoc V t (a * b) = swapLoc V t a * swapLoc V t b := by
  classical
  obtain ⟨Λ, X, Y, rfl, rfl⟩ := exists_ofM₂ a b
  rw [← ofM_mul, swapLoc_ofM, swapLoc_ofM, swapLoc_ofM, swapAct, swapAct, swapAct, map_mul]
  calc swapU V Λ t * (stage Λ X * stage Λ Y) * star (swapU V Λ t)
      = swapU V Λ t * stage Λ X * (star (swapU V Λ t) * swapU V Λ t)
          * stage Λ Y * star (swapU V Λ t) := by
        rw [star_swapU_mul]
        simp only [mul_one, mul_assoc]
    _ = swapU V Λ t * stage Λ X * star (swapU V Λ t)
          * (swapU V Λ t * stage Λ Y * star (swapU V Λ t)) := by simp only [mul_assoc]

theorem swapLoc_add (t : ℝ) (a b : localAlg ι (V × V)) :
    swapLoc V t (a + b) = swapLoc V t a + swapLoc V t b := by
  classical
  obtain ⟨Λ, X, Y, rfl, rfl⟩ := exists_ofM₂ a b
  rw [← ofM_add, swapLoc_ofM, swapLoc_ofM, swapLoc_ofM, swapAct, swapAct, swapAct, map_add]
  simp only [mul_add, add_mul]

theorem swapLoc_smul (t : ℝ) (c : ℂ) (a : localAlg ι (V × V)) :
    swapLoc V t (c • a) = c • swapLoc V t a := by
  classical
  obtain ⟨Λ, X, rfl⟩ := exists_ofM a
  rw [← ofM_smul, swapLoc_ofM, swapLoc_ofM, swapAct, swapAct, map_smul]
  simp only [mul_smul_comm, smul_mul_assoc]

theorem swapLoc_sub (t : ℝ) (a b : localAlg ι (V × V)) :
    swapLoc V t (a - b) = swapLoc V t a - swapLoc V t b := by
  rw [sub_eq_add_neg, swapLoc_add, ← neg_one_smul ℂ b, swapLoc_smul, neg_one_smul,
    ← sub_eq_add_neg]

theorem swapLoc_one (t : ℝ) : swapLoc V t (1 : localAlg ι (V × V)) = 1 := by
  classical
  have h1 : (1 : localAlg ι (V × V)) = ofM (∅ : Finset ι) 1 := (ofM_one _).symm
  rw [h1, swapLoc_ofM, swapAct, map_one, mul_one, swapU_star]

theorem swapLoc_star (t : ℝ) (a : localAlg ι (V × V)) :
    swapLoc V t (star a) = star (swapLoc V t a) := by
  classical
  obtain ⟨Λ, X, rfl⟩ := exists_ofM a
  rw [star_ofM, swapLoc_ofM, swapLoc_ofM, swapAct, swapAct,
    ← Matrix.star_eq_conjTranspose, map_star]
  simp only [star_mul, star_star, mul_assoc]

theorem swapLoc_zero (a : localAlg ι (V × V)) :
    swapLoc V 0 a = (a : Quasilocal ι (V × V)) := by
  classical
  obtain ⟨Λ, X, rfl⟩ := exists_ofM a
  rw [swapLoc_ofM, swapAct, swapU_zero, star_one, one_mul, mul_one]
  rfl

/-- **THE LAYER IS ISOMETRIC.** -/
theorem norm_swapLoc (t : ℝ) (a : localAlg ι (V × V)) :
    ‖swapLoc V t a‖ = ‖(a : Quasilocal ι (V × V))‖ := by
  classical
  obtain ⟨Λ, X, rfl⟩ := exists_ofM a
  rw [swapLoc_ofM, swapAct]
  have hU := swapU_mem_unitary V Λ t
  rw [CStarRing.norm_mul_mem_unitary _ (Unitary.star_mem hU),
    CStarRing.norm_mem_unitary_mul _ hU]
  rfl

theorem isometry_swapLoc (t : ℝ) :
    Isometry (fun a : localAlg ι (V × V) => swapLoc V t a) := by
  refine Isometry.of_dist_eq fun a b => ?_
  rw [dist_eq_norm, dist_eq_norm, ← swapLoc_sub, norm_swapLoc,
    UniformSpace.Completion.norm_coe]

theorem continuous_swapLoc (a : localAlg ι (V × V)) :
    Continuous fun t : ℝ => swapLoc V t a := by
  classical
  obtain ⟨Λ, X, rfl⟩ := exists_ofM a
  simp only [fun t => swapLoc_ofM V t Λ X, swapAct]
  exact ((continuous_swapU V Λ).mul continuous_const).mul
    (continuous_star.comp (continuous_swapU V Λ))

/-! ### The layer on the quasilocal algebra -/

/-- **THE SWAP LAYER ON THE QUASILOCAL ALGEBRA.** -/
noncomputable def swapQ (t : ℝ) : Quasilocal ι (V × V) → Quasilocal ι (V × V) :=
  UniformSpace.Completion.extension (swapLoc V t)

theorem swapQ_coe (t : ℝ) (a : localAlg ι (V × V)) :
    swapQ V t (a : Quasilocal ι (V × V)) = swapLoc V t a :=
  UniformSpace.Completion.extension_coe (isometry_swapLoc V t).uniformContinuous a

theorem continuous_swapQ (t : ℝ) :
    Continuous (fun x : Quasilocal ι (V × V) => swapQ V t x) := by
  unfold swapQ
  exact UniformSpace.Completion.continuous_extension

theorem swapQ_stage (t : ℝ) (Λ : Finset ι)
    (X : Matrix (Conf Λ (V × V)) (Conf Λ (V × V)) ℂ) :
    swapQ V t (stage Λ X) = swapAct V Λ t (stage Λ X) := by
  rw [stage_apply, swapQ_coe, swapLoc_ofM]
  rfl

theorem norm_swapQ (t : ℝ) (x : Quasilocal ι (V × V)) : ‖swapQ V t x‖ = ‖x‖ := by
  refine UniformSpace.Completion.induction_on x ?_ fun a => ?_
  · exact isClosed_eq (continuous_norm.comp (continuous_swapQ V t)) continuous_norm
  · rw [swapQ_coe, norm_swapLoc]

theorem swapQ_mul (t : ℝ) (x y : Quasilocal ι (V × V)) :
    swapQ V t (x * y) = swapQ V t x * swapQ V t y := by
  refine UniformSpace.Completion.induction_on₂ x y ?_ fun a b => ?_
  · exact isClosed_eq ((continuous_swapQ V t).comp continuous_mul)
      (((continuous_swapQ V t).comp continuous_fst).mul
        ((continuous_swapQ V t).comp continuous_snd))
  · rw [← UniformSpace.Completion.coe_mul, swapQ_coe, swapQ_coe, swapQ_coe, swapLoc_mul]

theorem swapQ_add (t : ℝ) (x y : Quasilocal ι (V × V)) :
    swapQ V t (x + y) = swapQ V t x + swapQ V t y := by
  refine UniformSpace.Completion.induction_on₂ x y ?_ fun a b => ?_
  · exact isClosed_eq ((continuous_swapQ V t).comp continuous_add)
      (((continuous_swapQ V t).comp continuous_fst).add
        ((continuous_swapQ V t).comp continuous_snd))
  · rw [← UniformSpace.Completion.coe_add, swapQ_coe, swapQ_coe, swapQ_coe, swapLoc_add]

theorem swapQ_smul (t : ℝ) (c : ℂ) (x : Quasilocal ι (V × V)) :
    swapQ V t (c • x) = c • swapQ V t x := by
  refine UniformSpace.Completion.induction_on x ?_ fun a => ?_
  · exact isClosed_eq ((continuous_swapQ V t).comp (continuous_id.const_smul c))
      ((continuous_swapQ V t).const_smul c)
  · rw [← UniformSpace.Completion.coe_smul, swapQ_coe, swapQ_coe, swapLoc_smul]

theorem swapQ_star (t : ℝ) (x : Quasilocal ι (V × V)) :
    swapQ V t (star x) = star (swapQ V t x) := by
  refine UniformSpace.Completion.induction_on x ?_ fun a => ?_
  · exact isClosed_eq ((continuous_swapQ V t).comp continuous_star)
      (continuous_star.comp (continuous_swapQ V t))
  · rw [star_coe, swapQ_coe, swapQ_coe, swapLoc_star]

theorem swapQ_sub (t : ℝ) (x y : Quasilocal ι (V × V)) :
    swapQ V t (x - y) = swapQ V t x - swapQ V t y := by
  rw [sub_eq_add_neg, swapQ_add, ← neg_one_smul ℂ y, swapQ_smul, neg_one_smul, ← sub_eq_add_neg]

theorem swapQ_one (t : ℝ) : swapQ V t (1 : Quasilocal ι (V × V)) = 1 := by
  calc swapQ V t (1 : Quasilocal ι (V × V))
      = swapQ V t ((1 : localAlg ι (V × V)) : Quasilocal ι (V × V)) := by
        rw [UniformSpace.Completion.coe_one]
    _ = swapLoc V t 1 := swapQ_coe V t 1
    _ = 1 := swapLoc_one V t

theorem swapQ_zero_time (x : Quasilocal ι (V × V)) : swapQ V 0 x = x := by
  refine UniformSpace.Completion.induction_on x ?_ fun a => ?_
  · exact isClosed_eq (continuous_swapQ V 0) continuous_id
  · rw [swapQ_coe, swapLoc_zero]

theorem dist_swapQ (t : ℝ) (x y : Quasilocal ι (V × V)) :
    dist (swapQ V t x) (swapQ V t y) = dist x y := by
  rw [dist_eq_norm, dist_eq_norm, ← swapQ_sub, norm_swapQ]

/-- **STRONG CONTINUITY.** -/
theorem continuous_swapQ_time (x : Quasilocal ι (V × V)) :
    Continuous fun t : ℝ => swapQ V t x := by
  refine continuous_iff_continuousAt.mpr fun t₀ => Metric.continuousAt_iff.mpr fun ε hε => ?_
  have hx : x ∈ closure (Set.range ((↑) : localAlg ι (V × V) → Quasilocal ι (V × V))) := by
    rw [UniformSpace.Completion.denseRange_coe.closure_eq]
    trivial
  obtain ⟨a, ha⟩ := Metric.mem_closure_range_iff.mp hx (ε / 3) (by positivity)
  obtain ⟨δ, hδ, hball⟩ :=
    Metric.continuousAt_iff.mp ((continuous_swapLoc V a).continuousAt (x := t₀))
      (ε / 3) (by positivity)
  refine ⟨δ, hδ, fun {t} ht => ?_⟩
  have h1 : dist (swapQ V t x) (swapQ V t (a : Quasilocal ι (V × V))) < ε / 3 := by
    rw [dist_swapQ]; exact ha
  have h2 : dist (swapQ V t₀ (a : Quasilocal ι (V × V))) (swapQ V t₀ x) < ε / 3 := by
    rw [dist_swapQ, dist_comm]; exact ha
  have h3 : dist (swapQ V t (a : Quasilocal ι (V × V)))
      (swapQ V t₀ (a : Quasilocal ι (V × V))) < ε / 3 := by
    rw [swapQ_coe, swapQ_coe]; exact hball ht
  calc dist (swapQ V t x) (swapQ V t₀ x)
      ≤ dist (swapQ V t x) (swapQ V t (a : Quasilocal ι (V × V)))
        + dist (swapQ V t (a : Quasilocal ι (V × V))) (swapQ V t₀ x) := dist_triangle _ _ _
    _ ≤ dist (swapQ V t x) (swapQ V t (a : Quasilocal ι (V × V)))
        + (dist (swapQ V t (a : Quasilocal ι (V × V))) (swapQ V t₀ (a : Quasilocal ι (V × V)))
          + dist (swapQ V t₀ (a : Quasilocal ι (V × V))) (swapQ V t₀ x)) := by
        gcongr
        exact dist_triangle _ _ _
    _ < ε / 3 + (ε / 3 + ε / 3) := by gcongr
    _ = ε := by ring

/-- **THE GROUP LAW ON LOCAL OBSERVABLES.** Because the layer keeps a region's observables in that
region, both applications run on the same finite gate set and no stabilization step is needed. -/
theorem swapQ_add_time_stage (t s : ℝ) (Λ : Finset ι)
    (X : Matrix (Conf Λ (V × V)) (Conf Λ (V × V)) ℂ) :
    swapQ V t (swapQ V s (stage Λ X)) = swapQ V (t + s) (stage Λ X) := by
  classical
  obtain ⟨Y, hY⟩ := swapAct_mem_range_self V Λ s X
  have e1 : swapQ V s (stage Λ X) = stage Λ Y := by
    rw [swapQ_stage]
    exact hY.symm
  rw [e1, swapQ_stage, swapQ_stage, hY]
  simp only [swapAct]
  calc swapU V Λ t * (swapU V Λ s * stage Λ X * star (swapU V Λ s)) * star (swapU V Λ t)
      = swapU V Λ t * swapU V Λ s * stage Λ X
          * (star (swapU V Λ s) * star (swapU V Λ t)) := by simp only [mul_assoc]
    _ = swapU V Λ (t + s) * stage Λ X * star (swapU V Λ (t + s)) := by
        rw [swapU_add, ← star_mul, swapU_add]

/-- **THE GROUP LAW.** -/
theorem swapQ_add_time (t s : ℝ) (x : Quasilocal ι (V × V)) :
    swapQ V t (swapQ V s x) = swapQ V (t + s) x := by
  refine UniformSpace.Completion.induction_on x ?_ fun a => ?_
  · exact isClosed_eq ((continuous_swapQ V t).comp (continuous_swapQ V s))
      (continuous_swapQ V (t + s))
  · obtain ⟨Λ, X, rfl⟩ := exists_ofM a
    exact swapQ_add_time_stage V t s Λ X

theorem swapQ_left_inverse (t : ℝ) (x : Quasilocal ι (V × V)) :
    swapQ V (-t) (swapQ V t x) = x := by
  rw [swapQ_add_time, neg_add_cancel, swapQ_zero_time]

theorem swapQ_right_inverse (t : ℝ) (x : Quasilocal ι (V × V)) :
    swapQ V t (swapQ V (-t) x) = x := by
  rw [swapQ_add_time, add_neg_cancel, swapQ_zero_time]

/-- **THE SWAP LAYER IS A ONE-PARAMETER AUTOMORPHISM GROUP.** -/
theorem swapQ_bijective (t : ℝ) :
    Function.Bijective (swapQ V t : Quasilocal ι (V × V) → Quasilocal ι (V × V)) :=
  Function.bijective_iff_has_inverse.mpr
    ⟨swapQ V (-t), swapQ_left_inverse V t, swapQ_right_inverse V t⟩

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
#print axioms swapAct_stabilizes
#print axioms swapAct_mem_range
#print axioms swapAct_mem_range_self
#print axioms swapLoc_ofM
#print axioms swapLoc_mul
#print axioms swapLoc_add
#print axioms swapLoc_smul
#print axioms swapLoc_one
#print axioms swapLoc_star
#print axioms swapLoc_zero
#print axioms norm_swapLoc
#print axioms isometry_swapLoc
#print axioms continuous_swapLoc
#print axioms swapQ_coe
#print axioms swapQ_stage
#print axioms norm_swapQ
#print axioms swapQ_mul
#print axioms swapQ_add
#print axioms swapQ_smul
#print axioms swapQ_star
#print axioms swapQ_one
#print axioms swapQ_zero_time
#print axioms continuous_swapQ_time
#print axioms swapQ_add_time
#print axioms swapQ_bijective

end OIBridge.SwapLayer
