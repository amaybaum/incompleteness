import OIBridge.SecondOrderCircuit
import OIBridge.QuasilocalCharacterization

/-!
# The all-sites layer as an automorphism of the quasilocal algebra

`SecondOrderCircuit` proves that the reversible second-order update is a depth-two circuit of
commuting local gate involutions, and that a **finite list** of commuting gate involutions in any
star algebra is driven exactly by a one-parameter group. That leaves a gap this file closes: a
layer runs over **all** sites of an infinite lattice, and a finite list is not that layer.

The bridge is that only finitely many gates can move a given local observable. Fix a finite region
`Λ`. A gate at site `i` is supported in `Δ i = insert i (N i)`, and if `Δ i` is disjoint from `Λ`
then that gate's unitary commutes with every observable of `Λ` at every time. So conjugating by the
product over the finitely many gates that *can* reach `Λ` gives the same answer as conjugating by
any larger finite product — the construction **stabilizes**, and the stable value is the layer.

## The range hypothesis

`SecondOrderCircuit`'s factorization is stated for an arbitrary neighbourhood function, which is
correct there: it uses only the `- p` that reversibility leaves. **This file cannot be that
general.** If `F c i` may depend on arbitrarily distant sites then the gate at `i` has no finite
region, there is nothing to put in a stage, and no locality statement is available. The substratum
rule is finite range, so the hypothesis is carried explicitly rather than avoided.

## A word on the generator

On an infinite lattice `Σ_i h_i` is **not an element** of the quasilocal algebra. It is a formal
sum defining a densely-defined derivation: on each local observable only finitely many terms act,
which is exactly the stabilization above. What is bounded and local is each individual `h_i`.
Nothing here exhibits a bounded global Hamiltonian, and nothing here should be read as doing so.
-/

namespace OIBridge.SecondOrderLayer

open OIBridge.QuasilocalAlgebra OIBridge.RegionTower OIBridge.SecondOrderCircuit
open OIBridge.QuasilocalCharacterization
open Matrix

variable {ι : Type} [DecidableEq ι] {Q : Type} [Fintype Q] [DecidableEq Q] [Nonempty Q]

/-! ### Section A — extending a region's permutation to a larger region -/

section Extend

variable {Λ Λ' : Finset ι} (h : Λ ⊆ Λ')

/-- Extend a permutation of a region's configurations to a larger region, acting as the identity
on the adjoined sites. -/
def extConf (σ : Conf Λ Q ≃ Conf Λ Q) (G : Conf Λ' Q) : Conf Λ' Q :=
  fun u => if hu : (u : ι) ∈ Λ then σ (confRestrict h G) ⟨u, hu⟩ else G u

theorem extConf_apply (σ : Conf Λ Q ≃ Conf Λ Q) (G : Conf Λ' Q) (u : ↥Λ') :
    extConf h σ G u = if hu : (u : ι) ∈ Λ then σ (confRestrict h G) ⟨u, hu⟩ else G u := rfl

/-- The extension agrees with the original off the region. -/
theorem agreeOff_extConf (σ : Conf Λ Q ≃ Conf Λ Q) (G : Conf Λ' Q) :
    AgreeOff h (extConf h σ G) G := by
  intro u hu
  rw [extConf_apply, dif_neg hu]

/-- The extension restricts to the original permutation. -/
theorem confRestrict_extConf (σ : Conf Λ Q ≃ Conf Λ Q) (G : Conf Λ' Q) :
    confRestrict h (extConf h σ G) = σ (confRestrict h G) := by
  funext v
  show extConf h σ G ⟨(v : ι), h v.2⟩ = _
  rw [extConf_apply, dif_pos v.2]

/-- Extension is functorial on composites. -/
theorem extConf_comp (σ τ : Conf Λ Q ≃ Conf Λ Q) (G : Conf Λ' Q) :
    extConf h σ (extConf h τ G) = extConf h (τ.trans σ) G := by
  funext u
  by_cases hu : (u : ι) ∈ Λ
  · rw [extConf_apply, dif_pos hu, confRestrict_extConf, extConf_apply, dif_pos hu]
    rfl
  · rw [extConf_apply, dif_neg hu, extConf_apply, dif_neg hu, extConf_apply, dif_neg hu]

theorem extConf_refl (G : Conf Λ' Q) : extConf h (Equiv.refl (Conf Λ Q)) G = G := by
  funext u
  rw [extConf_apply]
  by_cases hu : (u : ι) ∈ Λ
  · rw [dif_pos hu]
    rfl
  · rw [dif_neg hu]

/-- The extension of a permutation, as a permutation. -/
def extPerm (σ : Conf Λ Q ≃ Conf Λ Q) : Conf Λ' Q ≃ Conf Λ' Q where
  toFun := extConf h σ
  invFun := extConf h σ.symm
  left_inv G := by rw [extConf_comp, Equiv.self_trans_symm, extConf_refl]
  right_inv G := by rw [extConf_comp, Equiv.symm_trans_self, extConf_refl]

@[simp] theorem extPerm_apply (σ : Conf Λ Q ≃ Conf Λ Q) (G : Conf Λ' Q) :
    extPerm h σ G = extConf h σ G := rfl

/-- **THE EXTENSION OF AN INVOLUTION IS AN INVOLUTION.** -/
theorem extPerm_involutive {σ : Conf Λ Q ≃ Conf Λ Q} (hσ : ∀ x, σ (σ x) = x) (G : Conf Λ' Q) :
    extPerm h σ (extPerm h σ G) = G := by
  have hs : σ.trans σ = Equiv.refl _ := Equiv.ext hσ
  rw [extPerm_apply, extPerm_apply, extConf_comp, hs, extConf_refl]

/-- **THE INCLUSION OF A PERMUTATION MATRIX IS THE PERMUTATION MATRIX OF THE EXTENSION.** This is
what lets a gate defined on its own region be compared with, and multiplied against, gates on
other regions: both are read inside a common region as permutation matrices there. -/
theorem inclObs_permMat (σ : Conf Λ Q ≃ Conf Λ Q) :
    inclObs h (permMat σ) = permMat (extPerm h σ) := by
  funext F G
  rw [inclObs, permMat_apply]
  by_cases hag : AgreeOff h F G
  · rw [if_pos hag, permMat_apply]
    by_cases hres : σ (confRestrict h G) = confRestrict h F
    · have hEF : extPerm h σ G = F := by
        funext u
        by_cases hu : (u : ι) ∈ Λ
        · rw [extPerm_apply, extConf_apply, dif_pos hu, hres]
          rfl
        · rw [extPerm_apply, extConf_apply, dif_neg hu]
          exact (hag u hu).symm
      rw [if_pos hres, if_pos hEF]
    · have hne : ¬ (extPerm h σ G = F) := by
        intro hc
        apply hres
        rw [← confRestrict_extConf h σ G]
        exact congrArg (confRestrict h) hc
      rw [if_neg hres, if_neg hne]
  · have hne : ¬ (extPerm h σ G = F) := by
      intro hc
      apply hag
      rw [← hc]
      exact agreeOff_extConf h σ G
    rw [if_neg hag, permMat_apply, if_neg hne]

end Extend

/-! ### Section B — a gate as an element of the quasilocal algebra, and commutation -/

section Gate

/-- A gate of the quasilocal algebra: an involutive permutation of a finite region's
configurations, read inside the completion. -/
noncomputable def qGate (Λ : Finset ι) (σ : Conf Λ Q ≃ Conf Λ Q) : Quasilocal ι Q :=
  stage Λ (permMat σ)

theorem qGate_eq_localGate (Λ : Finset ι) (σ : Conf Λ Q ≃ Conf Λ Q) :
    qGate Λ σ = localGate Λ σ := rfl

/-- **A GATE READ IN A LARGER REGION.** The same element of the quasilocal algebra is the
permutation matrix of the extended permutation on any region containing its own. -/
theorem qGate_extPerm {Λ Λ' : Finset ι} (h : Λ ⊆ Λ') (σ : Conf Λ Q ≃ Conf Λ Q) :
    qGate Λ σ = qGate Λ' (extPerm h σ) := by
  rw [qGate, qGate, ← inclObs_permMat h σ, stage_inclObs h]

/-- **GATES COMMUTE WHEN THEIR EXTENSIONS TO A COMMON REGION COMMUTE.** Everything about
overlapping gate regions reduces to this: read both inside a region containing them, where the
question is a question about two permutations of one finite configuration space. -/
theorem qGate_comm_of_extComm {Λ₁ Λ₂ Λ : Finset ι} (h₁ : Λ₁ ⊆ Λ) (h₂ : Λ₂ ⊆ Λ)
    {σ₁ : Conf Λ₁ Q ≃ Conf Λ₁ Q} {σ₂ : Conf Λ₂ Q ≃ Conf Λ₂ Q}
    (hc : ∀ G, extPerm h₁ σ₁ (extPerm h₂ σ₂ G) = extPerm h₂ σ₂ (extPerm h₁ σ₁ G)) :
    qGate Λ₁ σ₁ * qGate Λ₂ σ₂ = qGate Λ₂ σ₂ * qGate Λ₁ σ₁ := by
  rw [qGate_extPerm h₁ σ₁, qGate_extPerm h₂ σ₂, qGate, qGate, ← map_mul, ← map_mul,
    permMat_mul, permMat_mul]
  congr 2
  exact Equiv.ext fun G => hc G

/-- A gate is a self-adjoint unitary of the quasilocal algebra. -/
theorem qGate_isGate {Λ : Finset ι} {σ : Conf Λ Q ≃ Conf Λ Q} (hσ : ∀ x, σ (σ x) = x) :
    qGate Λ σ * qGate Λ σ = 1 ∧ star (qGate Λ σ) = qGate Λ σ :=
  localGate_isGate hσ

/-- **A GATE COMMUTES WITH THE OBSERVABLES OF A DISJOINT REGION.** -/
theorem qGate_comm_stage_of_disjoint {Λ Λ' : Finset ι} (hd : Disjoint Λ Λ')
    (σ : Conf Λ Q ≃ Conf Λ Q) (Y : Matrix (Conf Λ' Q) (Conf Λ' Q) ℂ) :
    qGate Λ σ * stage Λ' Y = stage Λ' Y * qGate Λ σ :=
  stage_comm_of_disjoint hd (permMat σ) Y

/-- **THE GATE'S UNITARY COMMUTES WITH THE OBSERVABLES OF A DISJOINT REGION**, at every time.
This is the fact that makes the layer construction stabilize: a gate that cannot reach a region
does nothing to that region's observables, whatever the time. -/
theorem unit_qGate_comm_stage_of_disjoint {Λ Λ' : Finset ι} (hd : Disjoint Λ Λ')
    (σ : Conf Λ Q ≃ Conf Λ Q) (Y : Matrix (Conf Λ' Q) (Conf Λ' Q) ℂ) (t : ℝ) :
    unit (qGate Λ σ) t * stage Λ' Y = stage Λ' Y * unit (qGate Λ σ) t := by
  have hg := qGate_comm_stage_of_disjoint hd σ Y
  simp only [unit, proj, add_mul, mul_add, one_mul, mul_one, smul_mul_assoc, mul_smul_comm,
    sub_mul, mul_sub, hg]

end Gate

/-! ### Section C — a finite-range rule, its gates, and the sites a region can feel -/

section Rule

variable {V : Type} [Fintype V] [DecidableEq V] [Nonempty V] [AddCommGroup V]

/-- **A FINITE-RANGE SECOND-ORDER RULE.** `F` is the neighbourhood function of the update
`(p, c) ↦ (c, F c - p)`; `N i` is the finite set of sites `F _ i` may read; `infl j` collects the
sites that may read `j`. The two finiteness data are what `SecondOrderCircuit` deliberately does
without, and what any locality statement needs. -/
structure Rule (ι V : Type) [DecidableEq ι] where
  F : (ι → V) → (ι → V)
  N : ι → Finset ι
  infl : ι → Finset ι
  dep : ∀ i (c c' : ι → V), (∀ j ∈ N i, c j = c' j) → F c i = F c' i
  mem_infl : ∀ i j, j ∈ N i → i ∈ infl j

variable (R : Rule ι V)

/-- The region a gate occupies: its own site together with what it reads. -/
def gateRegion (i : ι) : Finset ι := insert i (R.N i)

theorem self_mem_gateRegion (i : ι) : i ∈ gateRegion R i := Finset.mem_insert_self _ _

theorem nbhd_subset_gateRegion (i : ι) : R.N i ⊆ gateRegion R i := Finset.subset_insert _ _

/-- The current slice of a region's configuration, extended arbitrarily off the region. Only its
values on `N i` are ever consumed, which is what `Rule.dep` guarantees. -/
noncomputable def curOn (Λ : Finset ι) (x : Conf Λ (V × V)) : ι → V :=
  fun j => if hj : j ∈ Λ then (x ⟨j, hj⟩).2 else Classical.arbitrary V

/-- The value the rule writes at a site, computed inside a region. -/
noncomputable def rhs (Λ : Finset ι) (i : ι) (x : Conf Λ (V × V)) : V :=
  R.F (curOn Λ x) i

/-- **THE SHEAR GATE INSIDE A REGION**: write that site's previous component, read only current
components. -/
noncomputable def gateOn (Λ : Finset ι) (i : ι) (x : Conf Λ (V × V)) : Conf Λ (V × V) :=
  fun u => if (u : ι) = i then (rhs R Λ i x - (x u).1, (x u).2) else x u

variable {R}

theorem gateOn_apply (Λ : Finset ι) (i : ι) (x : Conf Λ (V × V)) (u : ↥Λ) :
    gateOn R Λ i x u = if (u : ι) = i then (rhs R Λ i x - (x u).1, (x u).2) else x u := rfl

/-- **A GATE DOES NOT TOUCH THE CURRENT SLICE.** Every commutation fact rests on this. -/
theorem curOn_gateOn (Λ : Finset ι) (i : ι) (x : Conf Λ (V × V)) :
    curOn Λ (gateOn R Λ i x) = curOn Λ x := by
  funext j
  rw [curOn, curOn]
  by_cases hj : j ∈ Λ
  · rw [dif_pos hj, dif_pos hj, gateOn_apply]
    by_cases hji : (⟨j, hj⟩ : ↥Λ).1 = i
    · rw [if_pos hji]
    · rw [if_neg hji]
  · rw [dif_neg hj, dif_neg hj]

/-- Hence the written value is unchanged by any gate. -/
theorem rhs_gateOn (Λ : Finset ι) (i j : ι) (x : Conf Λ (V × V)) :
    rhs R Λ i (gateOn R Λ j x) = rhs R Λ i x := by
  rw [rhs, rhs, curOn_gateOn]

/-- **EACH GATE IS AN INVOLUTION.** -/
theorem gateOn_involutive (Λ : Finset ι) (i : ι) (x : Conf Λ (V × V)) :
    gateOn R Λ i (gateOn R Λ i x) = x := by
  funext u
  rw [gateOn_apply]
  by_cases hu : (u : ι) = i
  · rw [if_pos hu, rhs_gateOn, gateOn_apply, if_pos hu]
    exact Prod.ext (by ring_nf; abel) rfl
  · rw [if_neg hu, gateOn_apply, if_neg hu]

/-- **THE GATES COMMUTE.** A gate writes only its own site's previous component and reads only
current components, which no gate writes. -/
theorem gateOn_comm (Λ : Finset ι) (i j : ι) (x : Conf Λ (V × V)) :
    gateOn R Λ i (gateOn R Λ j x) = gateOn R Λ j (gateOn R Λ i x) := by
  funext u
  by_cases hui : (u : ι) = i
  · by_cases huj : (u : ι) = j
    · have : i = j := hui ▸ huj ▸ rfl
      subst this
      rfl
    · rw [gateOn_apply, if_pos hui, rhs_gateOn, gateOn_apply, if_neg huj,
        gateOn_apply, if_neg huj, gateOn_apply, if_pos hui]
  · by_cases huj : (u : ι) = j
    · rw [gateOn_apply, if_neg hui, gateOn_apply, if_pos huj, gateOn_apply, if_pos huj,
        rhs_gateOn, gateOn_apply, if_neg hui]
    · rw [gateOn_apply, if_neg hui, gateOn_apply, if_neg huj, gateOn_apply, if_neg huj,
        gateOn_apply, if_neg hui]

/-- The gate inside a region, as a permutation. -/
noncomputable def gateEquiv (R : Rule ι V) (Λ : Finset ι) (i : ι) :
    Conf Λ (V × V) ≃ Conf Λ (V × V) where
  toFun := gateOn R Λ i
  invFun := gateOn R Λ i
  left_inv := gateOn_involutive Λ i
  right_inv := gateOn_involutive Λ i

@[simp] theorem gateEquiv_apply (Λ : Finset ι) (i : ι) (x : Conf Λ (V × V)) :
    gateEquiv R Λ i x = gateOn R Λ i x := rfl

/-- **THE WRITTEN VALUE DOES NOT DEPEND ON THE REGION IT IS COMPUTED IN**, provided the region
contains what the rule reads. This is where `Rule.dep` is consumed, and it is the reason a gate
defined on its own region is the same operator as the gate defined on any larger one. -/
theorem rhs_restrict {Λ : Finset ι} {i : ι} (h : gateRegion R i ⊆ Λ) (G : Conf Λ (V × V)) :
    rhs R Λ i G = rhs R (gateRegion R i) i (confRestrict h G) := by
  refine R.dep i _ _ fun j hj => ?_
  have hjΔ : j ∈ gateRegion R i := nbhd_subset_gateRegion R i hj
  have hjΛ : j ∈ Λ := h hjΔ
  rw [curOn, curOn, dif_pos hjΛ, dif_pos hjΔ]
  rfl

/-- **THE GATE ON ITS OWN REGION EXTENDS TO THE GATE ON ANY LARGER REGION.** -/
theorem extPerm_gateEquiv {Λ : Finset ι} {i : ι} (h : gateRegion R i ⊆ Λ) :
    extPerm h (gateEquiv R (gateRegion R i) i) = gateEquiv R Λ i := by
  refine Equiv.ext fun G => ?_
  funext u
  rw [extPerm_apply, extConf_apply]
  by_cases hu : (u : ι) ∈ gateRegion R i
  · rw [dif_pos hu]
    simp only [gateEquiv_apply, gateOn_apply]
    by_cases hui : (u : ι) = i
    · rw [if_pos hui, if_pos hui, ← rhs_restrict h G]
      rfl
    · rw [if_neg hui, if_neg hui]
      rfl
  · rw [dif_neg hu]
    simp only [gateEquiv_apply, gateOn_apply]
    rw [if_neg]
    intro hc
    exact hu (hc ▸ self_mem_gateRegion R i)

end Rule

/-! ### Section D — the sites a region can feel, and gates as commuting quasilocal elements -/

section Affected

variable {V : Type} [Fintype V] [DecidableEq V] [Nonempty V] [AddCommGroup V]
variable (R : Rule ι V)

/-- **THE GATES A REGION CAN FEEL.** A superset of the sites whose gate region meets `Λ`, and
finite because the rule is finite range in both directions. -/
def affected (Λ : Finset ι) : Finset ι := Λ ∪ Λ.biUnion R.infl

theorem subset_affected (Λ : Finset ι) : Λ ⊆ affected R Λ := Finset.subset_union_left

theorem affected_mono {Λ Λ' : Finset ι} (h : Λ ⊆ Λ') : affected R Λ ⊆ affected R Λ' := by
  refine Finset.union_subset_union h ?_
  intro k hk
  obtain ⟨j, hj, hk⟩ := Finset.mem_biUnion.mp hk
  exact Finset.mem_biUnion.mpr ⟨j, h hj, hk⟩

/-- **EVERY OTHER GATE IS BLIND TO THE REGION.** A site outside the affected set has a gate region
disjoint from `Λ`, so its gate cannot move any observable of `Λ`. This is the finiteness that makes
an infinite layer act locally. -/
theorem disjoint_gateRegion_of_notMem_affected {Λ : Finset ι} {i : ι} (hi : i ∉ affected R Λ) :
    Disjoint (gateRegion R i) Λ := by
  rw [Finset.disjoint_left]
  intro k hk hkΛ
  rcases Finset.mem_insert.mp hk with rfl | hkN
  · exact hi (Finset.mem_union_left _ hkΛ)
  · exact hi (Finset.mem_union_right _
      (Finset.mem_biUnion.mpr ⟨k, hkΛ, R.mem_infl i k hkN⟩))

/-- **THE SHEAR GATE AS AN ELEMENT OF THE QUASILOCAL ALGEBRA.** -/
noncomputable def shearGate (i : ι) : Quasilocal ι (V × V) :=
  qGate (gateRegion R i) (gateEquiv R (gateRegion R i) i)

/-- Each shear gate is a self-adjoint unitary. -/
theorem shearGate_isGate (i : ι) :
    shearGate R i * shearGate R i = 1 ∧ star (shearGate R i) = shearGate R i :=
  qGate_isGate (gateOn_involutive (gateRegion R i) i)

/-- **THE SHEAR GATES COMMUTE IN THE QUASILOCAL ALGEBRA.** Overlapping gate regions are handled by
reading both gates inside their union, where the question is `gateOn_comm`. -/
theorem shearGate_comm (i j : ι) :
    shearGate R i * shearGate R j = shearGate R j * shearGate R i := by
  have hi : gateRegion R i ⊆ gateRegion R i ∪ gateRegion R j := Finset.subset_union_left
  have hj : gateRegion R j ⊆ gateRegion R i ∪ gateRegion R j := Finset.subset_union_right
  refine qGate_comm_of_extComm hi hj fun G => ?_
  rw [extPerm_gateEquiv hi, extPerm_gateEquiv hj]
  exact gateOn_comm _ i j G

/-- **A BLIND GATE'S UNITARY COMMUTES WITH THE REGION'S OBSERVABLES**, at every time. -/
theorem unit_shearGate_comm_stage {Λ : Finset ι} {i : ι} (hi : i ∉ affected R Λ)
    (X : Matrix (Conf Λ (V × V)) (Conf Λ (V × V)) ℂ) (t : ℝ) :
    unit (shearGate R i) t * stage Λ X = stage Λ X * unit (shearGate R i) t :=
  unit_qGate_comm_stage_of_disjoint (disjoint_gateRegion_of_notMem_affected R hi) _ X t

/-- The gates a region can feel, as a list. -/
noncomputable def shearGateList (Λ : Finset ι) : List (Quasilocal ι (V × V)) :=
  (affected R Λ).toList.map (shearGate R)

/-- **THE LIST IS A GATE LIST**: self-adjoint unitaries that commute, which is what the drive
machinery consumes. -/
theorem isGateList_shearGateList (Λ : Finset ι) : IsGateList (shearGateList R Λ) := by
  constructor
  · intro g hg
    obtain ⟨i, _, rfl⟩ := List.mem_map.mp hg
    exact (shearGate_isGate R i).1
  · intro g hg
    obtain ⟨i, _, rfl⟩ := List.mem_map.mp hg
    exact (shearGate_isGate R i).2
  · intro g hg k hk
    obtain ⟨i, _, rfl⟩ := List.mem_map.mp hg
    obtain ⟨j, _, rfl⟩ := List.mem_map.mp hk
    exact shearGate_comm R i j

end Affected

/-! ### Section E — the layer flow, and its stabilization

The gates a region can feel form a finite set, and their unitaries commute, so their product is
well defined without choosing an order (`Finset.noncommProd`). Conjugating an observable of `Λ` by
that product is the layer's action on it. **Stabilization** is the statement that enlarging the
region beyond what `Λ` can feel changes nothing: the extra factors commute with the observable and
cancel against their own adjoints. That is what turns a family of finite products into one map.
-/

section Layer

variable {V : Type} [Fintype V] [DecidableEq V] [Nonempty V] [AddCommGroup V]
variable (R : Rule ι V)

/-- The unitary of a gate is a self-adjoint-unitary's one-parameter unitary. -/
theorem unit_shearGate_comm (i j : ι) (t s : ℝ) :
    unit (shearGate R i) t * unit (shearGate R j) s
      = unit (shearGate R j) s * unit (shearGate R i) t :=
  unit_comm (shearGate_comm R i j) t s

/-- **THE LAYER'S UNITARY FOR A REGION**: the product over the gates that region can feel, taken
without choosing an order because they commute. -/
noncomputable def layerU (S : Finset ι) (t : ℝ) : Quasilocal ι (V × V) :=
  S.noncommProd (fun i => unit (shearGate R i) t)
    (fun i _ j _ _ => unit_shearGate_comm R i j t t)

@[simp] theorem layerU_empty (t : ℝ) : layerU R (∅ : Finset ι) t = 1 :=
  Finset.noncommProd_empty _ _

/-- Splitting the product over a disjoint union. -/
theorem layerU_union {S T : Finset ι} (h : Disjoint S T) (t : ℝ) :
    layerU R (S ∪ T) t = layerU R S t * layerU R T t :=
  Finset.noncommProd_union_of_disjoint h _ _

/-- A unitary commuting with an observable leaves it fixed under conjugation. -/
theorem conj_eq_self_of_commute {A : Type*} [Ring A] [StarRing A] {u a : A}
    (hu : u * star u = 1) (hc : u * a = a * u) : u * a * star u = a := by
  rw [hc, mul_assoc, hu, mul_one]

set_option maxHeartbeats 1200000 in
/-- The layer unitary is unitary. -/
theorem layerU_star (S : Finset ι) (t : ℝ) :
    layerU R S t * star (layerU R S t) = 1 := by
  classical
  induction S using Finset.induction_on with
  | empty => simp
  | insert i s hi ih =>
      have hdis : Disjoint ({i} : Finset ι) s := by
        simpa using hi
      have hins : (insert i s : Finset ι) = {i} ∪ s := by
        rw [Finset.insert_eq]
      have hsing : layerU R ({i} : Finset ι) t = unit (shearGate R i) t := by
        rw [layerU, Finset.noncommProd_singleton]
      rw [hins, layerU_union R hdis, star_mul]
      calc layerU R ({i}) t * layerU R s t * (star (layerU R s t) * star (layerU R ({i}) t))
          = layerU R ({i}) t * (layerU R s t * star (layerU R s t)) * star (layerU R ({i}) t) := by
            simp only [mul_assoc]
        _ = layerU R ({i}) t * star (layerU R ({i}) t) := by rw [ih, mul_one]
        _ = 1 := by
            rw [hsing]
            exact unit_mul_star_unit (shearGate_isGate R i).1 (shearGate_isGate R i).2 t

/-- **THE LAYER'S ACTION ON A REGION'S OBSERVABLES.** -/
noncomputable def layerAct (S : Finset ι) (t : ℝ) (a : Quasilocal ι (V × V)) :
    Quasilocal ι (V × V) :=
  layerU R S t * a * star (layerU R S t)

set_option maxHeartbeats 1200000 in
/-- **STABILIZATION.** Enlarging the set of gates beyond what the observable's region can feel does
not change the answer: the extra gates commute with the observable and cancel. So the finite
products over growing regions all agree, and the layer is one map rather than a family. -/
theorem layerAct_stabilizes {Λ : Finset ι} {S : Finset ι} (hS : affected R Λ ⊆ S)
    (X : Matrix (Conf Λ (V × V)) (Conf Λ (V × V)) ℂ) (t : ℝ) :
    layerAct R S t (stage Λ X) = layerAct R (affected R Λ) t (stage Λ X) := by
  classical
  set A := affected R Λ with hA
  set W := S \ A with hW
  have hdis : Disjoint A W := Finset.disjoint_sdiff
  have hSU : S = A ∪ W := by
    rw [hW, Finset.union_sdiff_of_subset hS]
  have hcw : layerU R W t * stage Λ X = stage Λ X * layerU R W t := by
    rw [layerU]
    refine (Finset.noncommProd_commute W _ _ _ fun j hj => ?_).symm
    have hjn : j ∉ A := (Finset.mem_sdiff.mp (hW ▸ hj)).2
    exact (unit_shearGate_comm_stage R (hA ▸ hjn) X t).symm
  have hwu : layerU R W t * star (layerU R W t) = 1 := layerU_star R W t
  rw [layerAct, layerAct, hSU, layerU_union R hdis, star_mul]
  calc layerU R A t * layerU R W t * stage Λ X * (star (layerU R W t) * star (layerU R A t))
      = layerU R A t * (layerU R W t * stage Λ X * star (layerU R W t)) * star (layerU R A t) := by
        simp only [mul_assoc]
    _ = layerU R A t * stage Λ X * star (layerU R A t) := by
        rw [conj_eq_self_of_commute hwu hcw]

end Layer

/-! ### Section F — the layer as a map on the local algebra, independent of any cutoff

Stabilization says every sufficiently large finite product agrees on a given local observable. That
makes the following definition sound: take *a* representative region of the observable, and use the
gates that region can feel. Any other representative gives the same answer, because both agree
with the product over the union of the two affected sets.
-/

section LocalMap

set_option maxHeartbeats 1200000

variable {V : Type} [Fintype V] [DecidableEq V] [Nonempty V] [AddCommGroup V]
variable (R : Rule ι V)

theorem star_layerU_mul (S : Finset ι) (t : ℝ) :
    star (layerU R S t) * layerU R S t = 1 := by
  classical
  induction S using Finset.induction_on with
  | empty => simp
  | insert i s hi ih =>
      have hdis : Disjoint ({i} : Finset ι) s := by simpa using hi
      have hins : (insert i s : Finset ι) = {i} ∪ s := by rw [Finset.insert_eq]
      have hsing : layerU R ({i} : Finset ι) t = unit (shearGate R i) t := by
        rw [layerU, Finset.noncommProd_singleton]
      rw [hins, layerU_union R hdis, star_mul]
      calc star (layerU R s t) * star (layerU R ({i}) t) * (layerU R ({i}) t * layerU R s t)
          = star (layerU R s t)
              * (star (layerU R ({i}) t) * layerU R ({i}) t) * layerU R s t := by
            simp only [mul_assoc]
        _ = star (layerU R s t) * layerU R s t := by
            rw [hsing,
              star_unit_mul_unit (shearGate_isGate R i).1 (shearGate_isGate R i).2 t, mul_one]
        _ = 1 := ih

theorem layerU_zero (S : Finset ι) : layerU R S 0 = 1 := by
  classical
  induction S using Finset.induction_on with
  | empty => simp
  | insert i s hi ih =>
      have hdis : Disjoint ({i} : Finset ι) s := by simpa using hi
      have hins : (insert i s : Finset ι) = {i} ∪ s := by rw [Finset.insert_eq]
      have hsing : layerU R ({i} : Finset ι) 0 = unit (shearGate R i) 0 := by
        rw [layerU, Finset.noncommProd_singleton]
      rw [hins, layerU_union R hdis, hsing, unit_zero, one_mul, ih]

/-- **THE LAYER ON A LOCAL OBSERVABLE.** -/
noncomputable def layerLoc (t : ℝ) (a : localAlg ι (V × V)) : Quasilocal ι (V × V) :=
  layerAct R (affected R (rep a).1) t (a : Quasilocal ι (V × V))

/-- Two regions carrying the same observable give the same layer action. Rewriting the *element*
rather than the region is what keeps this type-correct, the regions sitting in dependent types. -/
theorem layerAct_eq_of_stage_eq {Λ Λ' : Finset ι}
    (X : Matrix (Conf Λ (V × V)) (Conf Λ (V × V)) ℂ)
    (X' : Matrix (Conf Λ' (V × V)) (Conf Λ' (V × V)) ℂ)
    (h : stage Λ X = stage Λ' X') (t : ℝ) :
    layerAct R (affected R Λ) t (stage Λ X) = layerAct R (affected R Λ') t (stage Λ' X') := by
  have hsub : affected R Λ ⊆ affected R Λ ∪ affected R Λ' := Finset.subset_union_left
  have hsub' : affected R Λ' ⊆ affected R Λ ∪ affected R Λ' := Finset.subset_union_right
  have e1 := layerAct_stabilizes R hsub X t
  have e2 := layerAct_stabilizes R hsub' X' t
  rw [← e1, ← e2, h]

/-- **INDEPENDENCE OF THE REPRESENTATIVE.** Any region carrying the observable gives the same
answer, so the definition above is a definition of the layer and not of a cutoff. -/
theorem layerLoc_ofM (t : ℝ) (Λ : Finset ι) (X : Matrix (Conf Λ (V × V)) (Conf Λ (V × V)) ℂ) :
    layerLoc R t (ofM Λ X) = layerAct R (affected R Λ) t (stage Λ X) := by
  classical
  have h : stage (rep (ofM Λ X)).1 (rep (ofM Λ X)).2 = stage Λ X := by
    rw [stage_apply, stage_apply, ofM_rep]
  have hL : layerLoc R t (ofM Λ X)
      = layerAct R (affected R (rep (ofM Λ X)).1) t
          (stage (rep (ofM Λ X)).1 (rep (ofM Λ X)).2) := by
    rw [layerLoc, h]
    rfl
  rw [hL]
  exact layerAct_eq_of_stage_eq R _ X h t

/-- **THE LAYER IS MULTIPLICATIVE.** -/
theorem layerLoc_mul (t : ℝ) (a b : localAlg ι (V × V)) :
    layerLoc R t (a * b) = layerLoc R t a * layerLoc R t b := by
  classical
  obtain ⟨Λ, X, Y, rfl, rfl⟩ := exists_ofM₂ a b
  set S := affected R Λ with hS
  have hu : layerU R S t * star (layerU R S t) = 1 := layerU_star R S t
  rw [← ofM_mul, layerLoc_ofM, layerLoc_ofM, layerLoc_ofM, layerAct, layerAct, layerAct,
    map_mul]
  calc layerU R S t * (stage Λ X * stage Λ Y) * star (layerU R S t)
      = layerU R S t * stage Λ X * (star (layerU R S t) * layerU R S t)
          * stage Λ Y * star (layerU R S t) := by
        rw [star_layerU_mul]
        simp only [mul_one, mul_assoc]
    _ = layerU R S t * stage Λ X * star (layerU R S t)
          * (layerU R S t * stage Λ Y * star (layerU R S t)) := by
        simp only [mul_assoc]

/-- **THE LAYER IS ADDITIVE.** -/
theorem layerLoc_add (t : ℝ) (a b : localAlg ι (V × V)) :
    layerLoc R t (a + b) = layerLoc R t a + layerLoc R t b := by
  classical
  obtain ⟨Λ, X, Y, rfl, rfl⟩ := exists_ofM₂ a b
  rw [← ofM_add, layerLoc_ofM, layerLoc_ofM, layerLoc_ofM, layerAct, layerAct, layerAct,
    map_add]
  simp only [mul_add, add_mul]

/-- **THE LAYER IS UNITAL.** -/
theorem layerLoc_one (t : ℝ) : layerLoc R t (1 : localAlg ι (V × V)) = 1 := by
  classical
  have h1 : (1 : localAlg ι (V × V)) = ofM (∅ : Finset ι) 1 := (ofM_one _).symm
  rw [h1, layerLoc_ofM, layerAct, map_one, mul_one, layerU_star]

/-- **THE LAYER PRESERVES THE INVOLUTION.** -/
theorem layerLoc_star (t : ℝ) (a : localAlg ι (V × V)) :
    layerLoc R t (star a) = star (layerLoc R t a) := by
  classical
  obtain ⟨Λ, X, rfl⟩ := exists_ofM a
  rw [star_ofM, layerLoc_ofM, layerLoc_ofM, layerAct, layerAct]
  rw [← Matrix.star_eq_conjTranspose, map_star]
  simp only [star_mul, star_star, mul_assoc]

/-- **AT TIME ZERO THE LAYER IS THE IDENTITY.** -/
theorem layerLoc_zero (a : localAlg ι (V × V)) :
    layerLoc R 0 a = (a : Quasilocal ι (V × V)) := by
  classical
  obtain ⟨Λ, X, rfl⟩ := exists_ofM a
  rw [layerLoc_ofM, layerAct, layerU_zero, star_one, one_mul, mul_one]
  rfl

end LocalMap

/-! ### Section G — scalars, norm, and the extension to the quasilocal algebra

Conjugation by a unitary is isometric in a C\*-algebra, so the layer extends from the dense local
algebra to the completion by the same route Level III used for the discrete dynamics.
-/

section Extend

set_option maxHeartbeats 1200000

variable {V : Type} [Fintype V] [DecidableEq V] [Nonempty V] [AddCommGroup V]
variable (R : Rule ι V)

/-- **THE LAYER IS ℂ-LINEAR.** Without this the layer would be a star-ring homomorphism only; with
it the extension below is a `ℂ`-linear `*`-automorphism of a C\*-algebra. -/
theorem layerLoc_smul (t : ℝ) (c : ℂ) (a : localAlg ι (V × V)) :
    layerLoc R t (c • a) = c • layerLoc R t a := by
  classical
  obtain ⟨Λ, X, rfl⟩ := exists_ofM a
  rw [← ofM_smul, layerLoc_ofM, layerLoc_ofM, layerAct, layerAct, map_smul]
  simp only [mul_smul_comm, smul_mul_assoc]

theorem layerLoc_sub (t : ℝ) (a b : localAlg ι (V × V)) :
    layerLoc R t (a - b) = layerLoc R t a - layerLoc R t b := by
  rw [sub_eq_add_neg, layerLoc_add, ← neg_one_smul ℂ b, layerLoc_smul, neg_one_smul,
    ← sub_eq_add_neg]

/-- The layer unitary is a unitary in the C\*-algebra's sense. -/
theorem layerU_mem_unitary (S : Finset ι) (t : ℝ) :
    layerU R S t ∈ unitary (Quasilocal ι (V × V)) :=
  Unitary.mem_iff.mpr ⟨star_layerU_mul R S t, layerU_star R S t⟩

/-- **THE LAYER IS ISOMETRIC.** Conjugation by a unitary cannot change a norm. -/
theorem norm_layerLoc (t : ℝ) (a : localAlg ι (V × V)) :
    ‖layerLoc R t a‖ = ‖(a : Quasilocal ι (V × V))‖ := by
  classical
  obtain ⟨Λ, X, rfl⟩ := exists_ofM a
  rw [layerLoc_ofM, layerAct]
  have hU := layerU_mem_unitary R (affected R Λ) t
  rw [CStarRing.norm_mul_mem_unitary _ (Unitary.star_mem hU),
    CStarRing.norm_mem_unitary_mul _ hU]
  rfl

theorem isometry_layerLoc (t : ℝ) :
    Isometry (fun a : localAlg ι (V × V) => layerLoc R t a) := by
  refine Isometry.of_dist_eq fun a b => ?_
  rw [dist_eq_norm, dist_eq_norm, ← layerLoc_sub, norm_layerLoc,
    UniformSpace.Completion.norm_coe]

/-- **THE LAYER ON THE QUASILOCAL ALGEBRA.** The continuous extension of the layer from the dense
local algebra. -/
noncomputable def layerQ (t : ℝ) : Quasilocal ι (V × V) → Quasilocal ι (V × V) :=
  UniformSpace.Completion.extension (layerLoc R t)

theorem layerQ_coe (t : ℝ) (a : localAlg ι (V × V)) :
    layerQ R t (a : Quasilocal ι (V × V)) = layerLoc R t a :=
  UniformSpace.Completion.extension_coe (isometry_layerLoc R t).uniformContinuous a

theorem continuous_layerQ (t : ℝ) : Continuous (layerQ R t) :=
  UniformSpace.Completion.continuous_extension

theorem layerQ_stage (t : ℝ) (Λ : Finset ι)
    (X : Matrix (Conf Λ (V × V)) (Conf Λ (V × V)) ℂ) :
    layerQ R t (stage Λ X) = layerAct R (affected R Λ) t (stage Λ X) := by
  rw [stage_apply, layerQ_coe, layerLoc_ofM]
  rfl

theorem norm_layerQ (t : ℝ) (x : Quasilocal ι (V × V)) : ‖layerQ R t x‖ = ‖x‖ := by
  refine UniformSpace.Completion.induction_on x ?_ fun a => ?_
  · exact isClosed_eq (continuous_norm.comp (continuous_layerQ R t)) continuous_norm
  · rw [layerQ_coe, norm_layerLoc]

theorem layerQ_mul (t : ℝ) (x y : Quasilocal ι (V × V)) :
    layerQ R t (x * y) = layerQ R t x * layerQ R t y := by
  refine UniformSpace.Completion.induction_on₂ x y ?_ fun a b => ?_
  · exact isClosed_eq ((continuous_layerQ R t).comp continuous_mul)
      (((continuous_layerQ R t).comp continuous_fst).mul
        ((continuous_layerQ R t).comp continuous_snd))
  · rw [← UniformSpace.Completion.coe_mul, layerQ_coe, layerQ_coe, layerQ_coe, layerLoc_mul]

theorem layerQ_add (t : ℝ) (x y : Quasilocal ι (V × V)) :
    layerQ R t (x + y) = layerQ R t x + layerQ R t y := by
  refine UniformSpace.Completion.induction_on₂ x y ?_ fun a b => ?_
  · exact isClosed_eq ((continuous_layerQ R t).comp continuous_add)
      (((continuous_layerQ R t).comp continuous_fst).add
        ((continuous_layerQ R t).comp continuous_snd))
  · rw [← UniformSpace.Completion.coe_add, layerQ_coe, layerQ_coe, layerQ_coe, layerLoc_add]

theorem layerQ_one (t : ℝ) : layerQ R t (1 : Quasilocal ι (V × V)) = 1 := by
  calc layerQ R t (1 : Quasilocal ι (V × V))
      = layerQ R t ((1 : localAlg ι (V × V)) : Quasilocal ι (V × V)) := by
        rw [UniformSpace.Completion.coe_one]
    _ = layerLoc R t 1 := layerQ_coe R t 1
    _ = 1 := layerLoc_one R t

theorem layerQ_zero_time (x : Quasilocal ι (V × V)) : layerQ R 0 x = x := by
  refine UniformSpace.Completion.induction_on x ?_ fun a => ?_
  · exact isClosed_eq (continuous_layerQ R 0) continuous_id
  · rw [layerQ_coe, layerLoc_zero]


/-! #### Strong continuity

A C\*-dynamics needs more than continuity in the observable at each fixed time: it needs
`t ↦ α_t(A)` continuous for every `A`. For a local observable only finitely many gate exponentials
occur, and each is an explicit polynomial in `t` through `Complex.exp`, so continuity is immediate.
The uniform isometry bound then lifts it to the whole quasilocal algebra.
-/

theorem continuous_unit_shearGate (i : ι) :
    Continuous fun t : ℝ => unit (shearGate R i) t := by
  unfold unit
  fun_prop

theorem continuous_layerU (S : Finset ι) :
    Continuous fun t : ℝ => layerU R S t := by
  classical
  induction S using Finset.induction_on with
  | empty =>
      simpa using continuous_const
  | insert i s hi ih =>
      have hdis : Disjoint ({i} : Finset ι) s := by simpa using hi
      have hins : (insert i s : Finset ι) = {i} ∪ s := by rw [Finset.insert_eq]
      have hsing : ∀ t : ℝ, layerU R ({i} : Finset ι) t = unit (shearGate R i) t := fun t => by
        rw [layerU, Finset.noncommProd_singleton]
      simp only [hins, fun t => layerU_union R hdis t, hsing]
      exact (continuous_unit_shearGate R i).mul ih

/-- **STRONG CONTINUITY ON LOCAL OBSERVABLES.** -/
theorem continuous_layerLoc (a : localAlg ι (V × V)) :
    Continuous fun t : ℝ => layerLoc R t a := by
  classical
  obtain ⟨Λ, X, rfl⟩ := exists_ofM a
  simp only [fun t => layerLoc_ofM R t Λ X, layerAct]
  exact ((continuous_layerU R (affected R Λ)).mul continuous_const).mul
    (continuous_star.comp (continuous_layerU R (affected R Λ)))

theorem layerQ_smul (t : ℝ) (c : ℂ) (x : Quasilocal ι (V × V)) :
    layerQ R t (c • x) = c • layerQ R t x := by
  refine UniformSpace.Completion.induction_on x ?_ fun a => ?_
  · exact isClosed_eq ((continuous_layerQ R t).comp (continuous_id.const_smul c))
      ((continuous_layerQ R t).const_smul c)
  · rw [← UniformSpace.Completion.coe_smul, layerQ_coe, layerQ_coe, layerLoc_smul]

theorem layerQ_star (t : ℝ) (x : Quasilocal ι (V × V)) :
    layerQ R t (star x) = star (layerQ R t x) := by
  refine UniformSpace.Completion.induction_on x ?_ fun a => ?_
  · exact isClosed_eq ((continuous_layerQ R t).comp continuous_star)
      (continuous_star.comp (continuous_layerQ R t))
  · rw [star_coe, layerQ_coe, layerQ_coe, layerLoc_star]

theorem layerQ_sub (t : ℝ) (x y : Quasilocal ι (V × V)) :
    layerQ R t (x - y) = layerQ R t x - layerQ R t y := by
  rw [sub_eq_add_neg, layerQ_add, ← neg_one_smul ℂ y, layerQ_smul, neg_one_smul,
    ← sub_eq_add_neg]

/-- The layer maps are uniformly isometric in the time parameter, which is what lets strong
continuity pass from the dense local algebra to the whole completion. -/
theorem dist_layerQ (t : ℝ) (x y : Quasilocal ι (V × V)) :
    dist (layerQ R t x) (layerQ R t y) = dist x y := by
  rw [dist_eq_norm, dist_eq_norm, ← layerQ_sub, norm_layerQ]

/-- **STRONG CONTINUITY.** `t ↦ α_t(A)` is continuous for every quasilocal `A`, not only for local
ones: the maps are uniformly isometric, so continuity passes to the completion. -/
theorem continuous_layerQ_time (x : Quasilocal ι (V × V)) :
    Continuous fun t : ℝ => layerQ R t x := by
  refine continuous_iff_continuousAt.mpr fun t₀ => Metric.continuousAt_iff.mpr fun ε hε => ?_
  have hx : x ∈ closure (Set.range ((↑) : localAlg ι (V × V) → Quasilocal ι (V × V))) := by
    rw [UniformSpace.Completion.denseRange_coe.closure_eq]
    trivial
  obtain ⟨a, ha⟩ := Metric.mem_closure_range_iff.mp hx (ε / 3) (by positivity)
  obtain ⟨δ, hδ, hball⟩ :=
    Metric.continuousAt_iff.mp ((continuous_layerLoc R a).continuousAt (x := t₀))
      (ε / 3) (by positivity)
  refine ⟨δ, hδ, fun {t} ht => ?_⟩
  have h1 : dist (layerQ R t x) (layerQ R t (a : Quasilocal ι (V × V))) < ε / 3 := by
    rw [dist_layerQ]; exact ha
  have h2 : dist (layerQ R t₀ (a : Quasilocal ι (V × V))) (layerQ R t₀ x) < ε / 3 := by
    rw [dist_layerQ, dist_comm]; exact ha
  have h3 : dist (layerQ R t (a : Quasilocal ι (V × V))) (layerQ R t₀ (a : Quasilocal ι (V × V)))
      < ε / 3 := by
    rw [layerQ_coe, layerQ_coe]; exact hball ht
  calc dist (layerQ R t x) (layerQ R t₀ x)
      ≤ dist (layerQ R t x) (layerQ R t (a : Quasilocal ι (V × V)))
        + dist (layerQ R t (a : Quasilocal ι (V × V))) (layerQ R t₀ x) := dist_triangle _ _ _
    _ ≤ dist (layerQ R t x) (layerQ R t (a : Quasilocal ι (V × V)))
        + (dist (layerQ R t (a : Quasilocal ι (V × V))) (layerQ R t₀ (a : Quasilocal ι (V × V)))
          + dist (layerQ R t₀ (a : Quasilocal ι (V × V))) (layerQ R t₀ x)) := by
        gcongr
        exact dist_triangle _ _ _
    _ < ε / 3 + (ε / 3 + ε / 3) := by gcongr
    _ = ε := by ring


/-! #### The group law

Two applications of the layer can be made to use *one* finite gate set, by stabilization. On that
common set the gates' unitaries compose by adding times, so the composite is the layer at the sum.
The one thing that needs care is that the intermediate observable is still local: it is, in the
region `Λ` enlarged by the gate regions used, which is what the range lemmas below record.
-/

theorem mem_range_stage_le {Λ Λ' : Finset ι} (h : Λ ⊆ Λ') {z : Quasilocal ι (V × V)}
    (hz : z ∈ Set.range (stage Λ)) : z ∈ Set.range (stage Λ') := by
  obtain ⟨X, rfl⟩ := hz
  exact ⟨inclObs h X, stage_inclObs h X⟩

theorem mem_range_stage_one (Λ : Finset ι) :
    (1 : Quasilocal ι (V × V)) ∈ Set.range (stage Λ) := ⟨1, map_one _⟩

theorem mem_range_stage_mul {Λ : Finset ι} {x y : Quasilocal ι (V × V)}
    (hx : x ∈ Set.range (stage Λ)) (hy : y ∈ Set.range (stage Λ)) :
    x * y ∈ Set.range (stage Λ) := by
  obtain ⟨X, rfl⟩ := hx; obtain ⟨Y, rfl⟩ := hy
  exact ⟨X * Y, map_mul _ _ _⟩

theorem mem_range_stage_sub {Λ : Finset ι} {x y : Quasilocal ι (V × V)}
    (hx : x ∈ Set.range (stage Λ)) (hy : y ∈ Set.range (stage Λ)) :
    x - y ∈ Set.range (stage Λ) := by
  obtain ⟨X, rfl⟩ := hx; obtain ⟨Y, rfl⟩ := hy
  exact ⟨X - Y, map_sub _ _ _⟩

theorem mem_range_stage_add {Λ : Finset ι} {x y : Quasilocal ι (V × V)}
    (hx : x ∈ Set.range (stage Λ)) (hy : y ∈ Set.range (stage Λ)) :
    x + y ∈ Set.range (stage Λ) := by
  obtain ⟨X, rfl⟩ := hx; obtain ⟨Y, rfl⟩ := hy
  exact ⟨X + Y, map_add _ _ _⟩

theorem mem_range_stage_smul {Λ : Finset ι} {x : Quasilocal ι (V × V)} (c : ℂ)
    (hx : x ∈ Set.range (stage Λ)) : c • x ∈ Set.range (stage Λ) := by
  obtain ⟨X, rfl⟩ := hx
  exact ⟨c • X, map_smul _ _ _⟩

theorem mem_range_stage_star {Λ : Finset ι} {x : Quasilocal ι (V × V)}
    (hx : x ∈ Set.range (stage Λ)) : star x ∈ Set.range (stage Λ) := by
  obtain ⟨X, rfl⟩ := hx
  exact ⟨star X, map_star _ _⟩

/-- A gate's unitary is supported in the gate's region, at every time. -/
theorem unit_shearGate_mem_range (i : ι) (t : ℝ) :
    unit (shearGate R i) t ∈ Set.range (stage (gateRegion R i)) := by
  rw [unit, proj]
  refine mem_range_stage_add (mem_range_stage_one _) (mem_range_stage_smul _ ?_)
  exact mem_range_stage_smul _ (mem_range_stage_sub (mem_range_stage_one _) ⟨_, rfl⟩)

/-- The region a set of gates occupies. -/
def gateSpan (S : Finset ι) : Finset ι := S.biUnion (gateRegion R)

theorem gateRegion_subset_gateSpan {S : Finset ι} {i : ι} (hi : i ∈ S) :
    gateRegion R i ⊆ gateSpan R S := Finset.subset_biUnion_of_mem _ hi

/-- **THE LAYER UNITARY IS SUPPORTED IN THE GATES' SPAN.** -/
theorem layerU_mem_range (S : Finset ι) (t : ℝ) :
    layerU R S t ∈ Set.range (stage (gateSpan R S)) := by
  classical
  induction S using Finset.induction_on with
  | empty =>
      rw [layerU_empty]
      exact mem_range_stage_one _
  | insert i s hi ih =>
      have hdis : Disjoint ({i} : Finset ι) s := by simpa using hi
      have hins : (insert i s : Finset ι) = {i} ∪ s := by rw [Finset.insert_eq]
      have hsing : layerU R ({i} : Finset ι) t = unit (shearGate R i) t := by
        rw [layerU, Finset.noncommProd_singleton]
      have hsub1 : gateRegion R i ⊆ gateSpan R (insert i s) :=
        gateRegion_subset_gateSpan R (Finset.mem_insert_self i s)
      have hsub2 : gateSpan R s ⊆ gateSpan R (insert i s) := by
        refine Finset.biUnion_subset_biUnion_of_subset_left _ ?_
        exact Finset.subset_insert i s
      rw [hins, layerU_union R hdis, hsing]
      exact mem_range_stage_mul
        (mem_range_stage_le hsub1 (unit_shearGate_mem_range R i t))
        (mem_range_stage_le hsub2 ih)

/-- **THE LAYER KEEPS A LOCAL OBSERVABLE LOCAL**, in its region enlarged by the gates' span. -/
theorem layerAct_mem_range (S Λ : Finset ι) (t : ℝ)
    (X : Matrix (Conf Λ (V × V)) (Conf Λ (V × V)) ℂ) :
    layerAct R S t (stage Λ X) ∈ Set.range (stage (Λ ∪ gateSpan R S)) := by
  have hU : layerU R S t ∈ Set.range (stage (Λ ∪ gateSpan R S)) :=
    mem_range_stage_le Finset.subset_union_right (layerU_mem_range R S t)
  have hX : stage Λ X ∈ Set.range (stage (Λ ∪ gateSpan R S)) :=
    mem_range_stage_le Finset.subset_union_left ⟨X, rfl⟩
  exact mem_range_stage_mul (mem_range_stage_mul hU hX) (mem_range_stage_star hU)

/-- **THE LAYER UNITARIES COMPOSE BY ADDING TIMES.** -/
theorem layerU_add (S : Finset ι) (t s : ℝ) :
    layerU R S t * layerU R S s = layerU R S (t + s) := by
  classical
  induction S using Finset.induction_on with
  | empty => simp
  | insert i r hi ih =>
      have hdis : Disjoint ({i} : Finset ι) r := by simpa using hi
      have hins : (insert i r : Finset ι) = {i} ∪ r := by rw [Finset.insert_eq]
      have hsing : ∀ u : ℝ, layerU R ({i} : Finset ι) u = unit (shearGate R i) u := fun u => by
        rw [layerU, Finset.noncommProd_singleton]
      have hcross : layerU R r t * unit (shearGate R i) s
          = unit (shearGate R i) s * layerU R r t := by
        rw [layerU]
        exact (Finset.noncommProd_commute r _ _ _
          fun j _ => unit_shearGate_comm R i j s t).symm
      rw [hins, layerU_union R hdis, layerU_union R hdis, layerU_union R hdis,
        hsing, hsing, hsing]
      calc unit (shearGate R i) t * layerU R r t * (unit (shearGate R i) s * layerU R r s)
          = unit (shearGate R i) t * (layerU R r t * unit (shearGate R i) s) * layerU R r s := by
            simp only [mul_assoc]
        _ = unit (shearGate R i) t * (unit (shearGate R i) s * layerU R r t) * layerU R r s := by
            rw [hcross]
        _ = (unit (shearGate R i) t * unit (shearGate R i) s) * (layerU R r t * layerU R r s) := by
            simp only [mul_assoc]
        _ = unit (shearGate R i) (t + s) * layerU R r (t + s) := by
            rw [unit_mul_unit (shearGate_isGate R i).1, ih]

/-- **THE GROUP LAW ON LOCAL OBSERVABLES.** -/
theorem layerQ_add_time_stage (t s : ℝ) (Λ : Finset ι)
    (X : Matrix (Conf Λ (V × V)) (Conf Λ (V × V)) ℂ) :
    layerQ R t (layerQ R s (stage Λ X)) = layerQ R (t + s) (stage Λ X) := by
  classical
  set Λ₁ := Λ ∪ gateSpan R (affected R Λ) with hΛ₁
  obtain ⟨Y, hY⟩ := layerAct_mem_range R (affected R Λ) Λ s X
  set S := affected R Λ ∪ affected R Λ₁ with hS
  have hsub₀ : affected R Λ ⊆ S := Finset.subset_union_left
  have hsub₁ : affected R Λ₁ ⊆ S := Finset.subset_union_right
  have hmid : layerAct R S s (stage Λ X) = stage Λ₁ Y := by
    rw [layerAct_stabilizes R hsub₀ X s]
    exact hY.symm
  have e1 : layerQ R s (stage Λ X) = stage Λ₁ Y := by
    rw [layerQ_stage]
    exact hY.symm
  have e2 : layerQ R t (stage Λ₁ Y) = layerAct R S t (stage Λ₁ Y) := by
    rw [layerQ_stage, ← layerAct_stabilizes R hsub₁ Y t]
  have e3 : layerQ R (t + s) (stage Λ X) = layerAct R S (t + s) (stage Λ X) := by
    rw [layerQ_stage, ← layerAct_stabilizes R hsub₀ X (t + s)]
  rw [e1, e2, e3, ← hmid]
  simp only [layerAct]
  calc layerU R S t * (layerU R S s * stage Λ X * star (layerU R S s)) * star (layerU R S t)
      = layerU R S t * layerU R S s * stage Λ X
          * (star (layerU R S s) * star (layerU R S t)) := by simp only [mul_assoc]
    _ = layerU R S (t + s) * stage Λ X * star (layerU R S (t + s)) := by
        rw [layerU_add, ← star_mul, layerU_add]

/-- **THE GROUP LAW.** With it the family is a one-parameter group of `*`-automorphisms, not
merely a strongly continuous family of endomorphisms. -/
theorem layerQ_add_time (t s : ℝ) (x : Quasilocal ι (V × V)) :
    layerQ R t (layerQ R s x) = layerQ R (t + s) x := by
  refine UniformSpace.Completion.induction_on x ?_ fun a => ?_
  · exact isClosed_eq ((continuous_layerQ R t).comp (continuous_layerQ R s))
      (continuous_layerQ R (t + s))
  · obtain ⟨Λ, X, rfl⟩ := exists_ofM a
    exact layerQ_add_time_stage R t s Λ X

/-- **EVERY LAYER MAP IS INVERTIBLE**, with the reverse-time map as its inverse. So each is a
`*`-automorphism of the quasilocal algebra and the family is a genuine one-parameter group. -/
theorem layerQ_left_inverse (t : ℝ) (x : Quasilocal ι (V × V)) :
    layerQ R (-t) (layerQ R t x) = x := by
  rw [layerQ_add_time, neg_add_cancel, layerQ_zero_time]

theorem layerQ_right_inverse (t : ℝ) (x : Quasilocal ι (V × V)) :
    layerQ R t (layerQ R (-t) x) = x := by
  rw [layerQ_add_time, add_neg_cancel, layerQ_zero_time]

theorem layerQ_bijective (t : ℝ) : Function.Bijective (layerQ R t) :=
  Function.bijective_iff_has_inverse.mpr
    ⟨layerQ R (-t), layerQ_left_inverse R t, layerQ_right_inverse R t⟩


/-! ### Section H — the swap layer

The second layer of the circuit. Its gates are the on-site exchanges of the two components, so a
gate's region is a single site: a region feels only the gates inside it, commutation is by
disjointness alone, and no neighbourhood or influence data appears. The development mirrors the
shear layer's, and is shorter for exactly that reason.
-/

section Swap

set_option maxHeartbeats 1200000

variable {V : Type} [Fintype V] [DecidableEq V] [Nonempty V] [AddCommGroup V]

/-- The on-site exchange of the two components at one site. -/
def swapConf (i : ι) (x : Conf ({i} : Finset ι) (V × V)) : Conf ({i} : Finset ι) (V × V) :=
  fun u => ((x u).2, (x u).1)

theorem swapConf_involutive (i : ι) (x : Conf ({i} : Finset ι) (V × V)) :
    swapConf i (swapConf i x) = x := by
  funext u
  rfl

/-- The swap gate at a site, as a permutation of that site's configurations. -/
def swapEquivAt (i : ι) :
    Conf ({i} : Finset ι) (V × V) ≃ Conf ({i} : Finset ι) (V × V) where
  toFun := swapConf i
  invFun := swapConf i
  left_inv := swapConf_involutive i
  right_inv := swapConf_involutive i

/-- **THE SWAP GATE IN THE QUASILOCAL ALGEBRA.** -/
noncomputable def swapGateQ (i : ι) : Quasilocal ι (V × V) := qGate {i} (swapEquivAt i)

theorem swapGateQ_isGate (i : ι) :
    swapGateQ (V := V) i * swapGateQ i = 1 ∧ star (swapGateQ (V := V) i) = swapGateQ i :=
  qGate_isGate (swapConf_involutive i)

/-- **THE SWAP GATES COMMUTE**, by disjointness of single sites. -/
theorem swapGateQ_comm (i j : ι) :
    swapGateQ (V := V) i * swapGateQ j = swapGateQ j * swapGateQ i := by
  by_cases h : i = j
  · subst h; rfl
  · exact stage_comm_of_disjoint (by simpa using h) _ _

theorem unit_swapGateQ_comm (i j : ι) (t s : ℝ) :
    unit (swapGateQ (V := V) i) t * unit (swapGateQ j) s
      = unit (swapGateQ j) s * unit (swapGateQ (V := V) i) t :=
  unit_comm (swapGateQ_comm i j) t s

/-- **A GATE OUTSIDE THE REGION IS BLIND TO IT.** For the swap layer this is immediate: the gate
occupies one site, so it is blind exactly when that site lies outside. -/
theorem unit_swapGateQ_comm_stage {Λ : Finset ι} {i : ι} (hi : i ∉ Λ)
    (Y : Matrix (Conf Λ (V × V)) (Conf Λ (V × V)) ℂ) (t : ℝ) :
    unit (swapGateQ (V := V) i) t * stage Λ Y = stage Λ Y * unit (swapGateQ (V := V) i) t :=
  unit_qGate_comm_stage_of_disjoint (by simpa using hi) _ Y t

theorem unit_swapGateQ_mem_range (i : ι) (t : ℝ) :
    unit (swapGateQ (V := V) i) t ∈ Set.range (stage ({i} : Finset ι)) := by
  rw [unit, proj]
  refine mem_range_stage_add (mem_range_stage_one _) (mem_range_stage_smul _ ?_)
  exact mem_range_stage_smul _ (mem_range_stage_sub (mem_range_stage_one _) ⟨_, rfl⟩)

/-- **THE SWAP LAYER'S UNITARY FOR A REGION.** -/
noncomputable def swapU (S : Finset ι) (t : ℝ) : Quasilocal ι (V × V) :=
  S.noncommProd (fun i => unit (swapGateQ i) t)
    (fun i _ j _ _ => unit_swapGateQ_comm i j t t)

@[simp] theorem swapU_empty (t : ℝ) : swapU (V := V) (∅ : Finset ι) t = 1 :=
  Finset.noncommProd_empty _ _

theorem swapU_union {S T : Finset ι} (h : Disjoint S T) (t : ℝ) :
    swapU (V := V) (S ∪ T) t = swapU S t * swapU T t :=
  Finset.noncommProd_union_of_disjoint h _ _

theorem swapU_singleton (i : ι) (t : ℝ) :
    swapU (V := V) ({i} : Finset ι) t = unit (swapGateQ i) t := by
  rw [swapU, Finset.noncommProd_singleton]

theorem swapU_star (S : Finset ι) (t : ℝ) :
    swapU (V := V) S t * star (swapU S t) = 1 := by
  classical
  induction S using Finset.induction_on with
  | empty => simp
  | insert i s hi ih =>
      have hdis : Disjoint ({i} : Finset ι) s := by simpa using hi
      have hins : (insert i s : Finset ι) = {i} ∪ s := by rw [Finset.insert_eq]
      rw [hins, swapU_union hdis, star_mul]
      calc swapU ({i}) t * swapU s t * (star (swapU s t) * star (swapU ({i}) t))
          = swapU ({i}) t * (swapU s t * star (swapU s t)) * star (swapU ({i}) t) := by
            simp only [mul_assoc]
        _ = swapU ({i}) t * star (swapU ({i}) t) := by rw [ih, mul_one]
        _ = 1 := by
            rw [swapU_singleton]
            exact unit_mul_star_unit (swapGateQ_isGate i).1 (swapGateQ_isGate i).2 t

theorem star_swapU_mul (S : Finset ι) (t : ℝ) :
    star (swapU (V := V) S t) * swapU S t = 1 := by
  classical
  induction S using Finset.induction_on with
  | empty => simp
  | insert i s hi ih =>
      have hdis : Disjoint ({i} : Finset ι) s := by simpa using hi
      have hins : (insert i s : Finset ι) = {i} ∪ s := by rw [Finset.insert_eq]
      rw [hins, swapU_union hdis, star_mul]
      calc star (swapU s t) * star (swapU ({i}) t) * (swapU ({i}) t * swapU s t)
          = star (swapU s t) * (star (swapU ({i}) t) * swapU ({i}) t) * swapU s t := by
            simp only [mul_assoc]
        _ = star (swapU s t) * swapU s t := by
            rw [swapU_singleton,
              star_unit_mul_unit (swapGateQ_isGate i).1 (swapGateQ_isGate i).2 t, mul_one]
        _ = 1 := ih

theorem swapU_mem_unitary (S : Finset ι) (t : ℝ) :
    swapU (V := V) S t ∈ unitary (Quasilocal ι (V × V)) :=
  Unitary.mem_iff.mpr ⟨star_swapU_mul S t, swapU_star S t⟩

theorem swapU_zero (S : Finset ι) : swapU (V := V) S 0 = 1 := by
  classical
  induction S using Finset.induction_on with
  | empty => simp
  | insert i s hi ih =>
      have hdis : Disjoint ({i} : Finset ι) s := by simpa using hi
      have hins : (insert i s : Finset ι) = {i} ∪ s := by rw [Finset.insert_eq]
      rw [hins, swapU_union hdis, swapU_singleton, unit_zero, one_mul, ih]

theorem swapU_add (S : Finset ι) (t s : ℝ) :
    swapU (V := V) S t * swapU S s = swapU S (t + s) := by
  classical
  induction S using Finset.induction_on with
  | empty => simp
  | insert i r hi ih =>
      have hdis : Disjoint ({i} : Finset ι) r := by simpa using hi
      have hins : (insert i r : Finset ι) = {i} ∪ r := by rw [Finset.insert_eq]
      have hcross : swapU (V := V) r t * unit (swapGateQ i) s
          = unit (swapGateQ i) s * swapU r t := by
        rw [swapU]
        exact (Finset.noncommProd_commute r _ _ _
          fun j _ => unit_swapGateQ_comm i j s t).symm
      rw [hins, swapU_union hdis, swapU_union hdis, swapU_union hdis,
        swapU_singleton, swapU_singleton, swapU_singleton]
      calc unit (swapGateQ i) t * swapU r t * (unit (swapGateQ i) s * swapU r s)
          = unit (swapGateQ i) t * (swapU r t * unit (swapGateQ i) s) * swapU r s := by
            simp only [mul_assoc]
        _ = unit (swapGateQ i) t * (unit (swapGateQ i) s * swapU r t) * swapU r s := by
            rw [hcross]
        _ = (unit (swapGateQ i) t * unit (swapGateQ i) s) * (swapU r t * swapU r s) := by
            simp only [mul_assoc]
        _ = unit (swapGateQ i) (t + s) * swapU r (t + s) := by
            rw [unit_mul_unit (swapGateQ_isGate i).1, ih]

theorem swapU_mem_range (S : Finset ι) (t : ℝ) :
    swapU (V := V) S t ∈ Set.range (stage S) := by
  classical
  induction S using Finset.induction_on with
  | empty =>
      rw [swapU_empty]
      exact mem_range_stage_one _
  | insert i s hi ih =>
      have hdis : Disjoint ({i} : Finset ι) s := by simpa using hi
      have hins : (insert i s : Finset ι) = {i} ∪ s := by rw [Finset.insert_eq]
      have h1 : ({i} : Finset ι) ⊆ insert i s := by
        simpa using Finset.mem_insert_self i s
      have h2 : s ⊆ insert i s := Finset.subset_insert i s
      rw [hins, swapU_union hdis, swapU_singleton]
      exact mem_range_stage_mul
        (mem_range_stage_le h1 (unit_swapGateQ_mem_range i t))
        (mem_range_stage_le h2 ih)

/-- **THE SWAP LAYER'S ACTION ON A REGION'S OBSERVABLES.** -/
noncomputable def swapAct (S : Finset ι) (t : ℝ) (a : Quasilocal ι (V × V)) :
    Quasilocal ι (V × V) :=
  swapU S t * a * star (swapU S t)

/-- **STABILIZATION.** For the swap layer the affected set of a region is the region itself. -/
theorem swapAct_stabilizes {Λ S : Finset ι} (hS : Λ ⊆ S)
    (X : Matrix (Conf Λ (V × V)) (Conf Λ (V × V)) ℂ) (t : ℝ) :
    swapAct S t (stage Λ X) = swapAct Λ t (stage Λ X) := by
  classical
  set W := S \ Λ with hW
  have hdis : Disjoint Λ W := Finset.disjoint_sdiff
  have hSU : S = Λ ∪ W := by rw [hW, Finset.union_sdiff_of_subset hS]
  have hcw : swapU (V := V) W t * stage Λ X = stage Λ X * swapU W t := by
    rw [swapU]
    refine (Finset.noncommProd_commute W _ _ _ fun j hj => ?_).symm
    have hjn : j ∉ Λ := (Finset.mem_sdiff.mp (hW ▸ hj)).2
    exact (unit_swapGateQ_comm_stage hjn X t).symm
  rw [swapAct, swapAct, hSU, swapU_union hdis, star_mul]
  calc swapU Λ t * swapU W t * stage Λ X * (star (swapU W t) * star (swapU Λ t))
      = swapU Λ t * (swapU W t * stage Λ X * star (swapU W t)) * star (swapU Λ t) := by
        simp only [mul_assoc]
    _ = swapU Λ t * stage Λ X * star (swapU Λ t) := by
        rw [conj_eq_self_of_commute (swapU_star W t) hcw]

theorem swapAct_mem_range (S Λ : Finset ι) (t : ℝ)
    (X : Matrix (Conf Λ (V × V)) (Conf Λ (V × V)) ℂ) :
    swapAct S t (stage Λ X) ∈ Set.range (stage (Λ ∪ S)) := by
  have hU : swapU (V := V) S t ∈ Set.range (stage (Λ ∪ S)) :=
    mem_range_stage_le Finset.subset_union_right (swapU_mem_range S t)
  have hX : stage Λ X ∈ Set.range (stage (Λ ∪ S)) :=
    mem_range_stage_le Finset.subset_union_left ⟨X, rfl⟩
  exact mem_range_stage_mul (mem_range_stage_mul hU hX) (mem_range_stage_star hU)

/-- **THE SWAP LAYER ON A LOCAL OBSERVABLE.** -/
noncomputable def swapLoc (t : ℝ) (a : localAlg ι (V × V)) : Quasilocal ι (V × V) :=
  swapAct (rep a).1 t (a : Quasilocal ι (V × V))

theorem swapAct_eq_of_stage_eq {Λ Λ' : Finset ι}
    (X : Matrix (Conf Λ (V × V)) (Conf Λ (V × V)) ℂ)
    (X' : Matrix (Conf Λ' (V × V)) (Conf Λ' (V × V)) ℂ)
    (h : stage Λ X = stage Λ' X') (t : ℝ) :
    swapAct Λ t (stage Λ X) = swapAct Λ' t (stage Λ' X') := by
  have e1 := swapAct_stabilizes (Finset.subset_union_left (s₂ := Λ')) X t
  have e2 := swapAct_stabilizes (Finset.subset_union_right (s₁ := Λ)) X' t
  rw [← e1, ← e2, h]

theorem swapLoc_ofM (t : ℝ) (Λ : Finset ι)
    (X : Matrix (Conf Λ (V × V)) (Conf Λ (V × V)) ℂ) :
    swapLoc t (ofM Λ X) = swapAct Λ t (stage Λ X) := by
  classical
  have h : stage (rep (ofM Λ X)).1 (rep (ofM Λ X)).2 = stage Λ X := by
    rw [stage_apply, stage_apply, ofM_rep]
  have hL : swapLoc t (ofM Λ X)
      = swapAct (rep (ofM Λ X)).1 t (stage (rep (ofM Λ X)).1 (rep (ofM Λ X)).2) := by
    rw [swapLoc, h]
    rfl
  rw [hL]
  exact swapAct_eq_of_stage_eq _ X h t

theorem swapLoc_mul (t : ℝ) (a b : localAlg ι (V × V)) :
    swapLoc t (a * b) = swapLoc t a * swapLoc t b := by
  classical
  obtain ⟨Λ, X, Y, rfl, rfl⟩ := exists_ofM₂ a b
  rw [← ofM_mul, swapLoc_ofM, swapLoc_ofM, swapLoc_ofM, swapAct, swapAct, swapAct, map_mul]
  calc swapU Λ t * (stage Λ X * stage Λ Y) * star (swapU Λ t)
      = swapU Λ t * stage Λ X * (star (swapU Λ t) * swapU Λ t)
          * stage Λ Y * star (swapU Λ t) := by
        rw [star_swapU_mul]
        simp only [mul_one, mul_assoc]
    _ = swapU Λ t * stage Λ X * star (swapU Λ t)
          * (swapU Λ t * stage Λ Y * star (swapU Λ t)) := by simp only [mul_assoc]

theorem swapLoc_add (t : ℝ) (a b : localAlg ι (V × V)) :
    swapLoc t (a + b) = swapLoc t a + swapLoc t b := by
  classical
  obtain ⟨Λ, X, Y, rfl, rfl⟩ := exists_ofM₂ a b
  rw [← ofM_add, swapLoc_ofM, swapLoc_ofM, swapLoc_ofM, swapAct, swapAct, swapAct, map_add]
  simp only [mul_add, add_mul]

theorem swapLoc_smul (t : ℝ) (c : ℂ) (a : localAlg ι (V × V)) :
    swapLoc t (c • a) = c • swapLoc t a := by
  classical
  obtain ⟨Λ, X, rfl⟩ := exists_ofM a
  rw [← ofM_smul, swapLoc_ofM, swapLoc_ofM, swapAct, swapAct, map_smul]
  simp only [mul_smul_comm, smul_mul_assoc]

theorem swapLoc_sub (t : ℝ) (a b : localAlg ι (V × V)) :
    swapLoc t (a - b) = swapLoc t a - swapLoc t b := by
  rw [sub_eq_add_neg, swapLoc_add, ← neg_one_smul ℂ b, swapLoc_smul, neg_one_smul,
    ← sub_eq_add_neg]

theorem swapLoc_one (t : ℝ) : swapLoc t (1 : localAlg ι (V × V)) = 1 := by
  classical
  have h1 : (1 : localAlg ι (V × V)) = ofM (∅ : Finset ι) 1 := (ofM_one _).symm
  rw [h1, swapLoc_ofM, swapAct, map_one, mul_one, swapU_star]

theorem swapLoc_star (t : ℝ) (a : localAlg ι (V × V)) :
    swapLoc t (star a) = star (swapLoc t a) := by
  classical
  obtain ⟨Λ, X, rfl⟩ := exists_ofM a
  rw [star_ofM, swapLoc_ofM, swapLoc_ofM, swapAct, swapAct,
    ← Matrix.star_eq_conjTranspose, map_star]
  simp only [star_mul, star_star, mul_assoc]

theorem swapLoc_zero (a : localAlg ι (V × V)) :
    swapLoc 0 a = (a : Quasilocal ι (V × V)) := by
  classical
  obtain ⟨Λ, X, rfl⟩ := exists_ofM a
  rw [swapLoc_ofM, swapAct, swapU_zero, star_one, one_mul, mul_one]
  rfl

theorem norm_swapLoc (t : ℝ) (a : localAlg ι (V × V)) :
    ‖swapLoc t a‖ = ‖(a : Quasilocal ι (V × V))‖ := by
  classical
  obtain ⟨Λ, X, rfl⟩ := exists_ofM a
  rw [swapLoc_ofM, swapAct]
  have hU := swapU_mem_unitary (V := V) Λ t
  rw [CStarRing.norm_mul_mem_unitary _ (Unitary.star_mem hU),
    CStarRing.norm_mem_unitary_mul _ hU]
  rfl

theorem isometry_swapLoc (t : ℝ) :
    Isometry (fun a : localAlg ι (V × V) => swapLoc t a) := by
  refine Isometry.of_dist_eq fun a b => ?_
  rw [dist_eq_norm, dist_eq_norm, ← swapLoc_sub, norm_swapLoc,
    UniformSpace.Completion.norm_coe]

/-- **THE SWAP LAYER ON THE QUASILOCAL ALGEBRA.** -/
noncomputable def swapQ (t : ℝ) : Quasilocal ι (V × V) → Quasilocal ι (V × V) :=
  UniformSpace.Completion.extension (swapLoc t)

theorem swapQ_coe (t : ℝ) (a : localAlg ι (V × V)) :
    swapQ t (a : Quasilocal ι (V × V)) = swapLoc t a :=
  UniformSpace.Completion.extension_coe (isometry_swapLoc t).uniformContinuous a

theorem continuous_swapQ (t : ℝ) : Continuous (swapQ (V := V) t) :=
  UniformSpace.Completion.continuous_extension

theorem swapQ_stage (t : ℝ) (Λ : Finset ι)
    (X : Matrix (Conf Λ (V × V)) (Conf Λ (V × V)) ℂ) :
    swapQ t (stage Λ X) = swapAct Λ t (stage Λ X) := by
  rw [stage_apply, swapQ_coe, swapLoc_ofM]
  rfl

theorem norm_swapQ (t : ℝ) (x : Quasilocal ι (V × V)) : ‖swapQ t x‖ = ‖x‖ := by
  refine UniformSpace.Completion.induction_on x ?_ fun a => ?_
  · exact isClosed_eq (continuous_norm.comp (continuous_swapQ t)) continuous_norm
  · rw [swapQ_coe, norm_swapLoc]

theorem swapQ_mul (t : ℝ) (x y : Quasilocal ι (V × V)) :
    swapQ t (x * y) = swapQ t x * swapQ t y := by
  refine UniformSpace.Completion.induction_on₂ x y ?_ fun a b => ?_
  · exact isClosed_eq ((continuous_swapQ t).comp continuous_mul)
      (((continuous_swapQ t).comp continuous_fst).mul ((continuous_swapQ t).comp continuous_snd))
  · rw [← UniformSpace.Completion.coe_mul, swapQ_coe, swapQ_coe, swapQ_coe, swapLoc_mul]

theorem swapQ_add (t : ℝ) (x y : Quasilocal ι (V × V)) :
    swapQ t (x + y) = swapQ t x + swapQ t y := by
  refine UniformSpace.Completion.induction_on₂ x y ?_ fun a b => ?_
  · exact isClosed_eq ((continuous_swapQ t).comp continuous_add)
      (((continuous_swapQ t).comp continuous_fst).add ((continuous_swapQ t).comp continuous_snd))
  · rw [← UniformSpace.Completion.coe_add, swapQ_coe, swapQ_coe, swapQ_coe, swapLoc_add]

theorem swapQ_smul (t : ℝ) (c : ℂ) (x : Quasilocal ι (V × V)) :
    swapQ t (c • x) = c • swapQ t x := by
  refine UniformSpace.Completion.induction_on x ?_ fun a => ?_
  · exact isClosed_eq ((continuous_swapQ t).comp (continuous_id.const_smul c))
      ((continuous_swapQ t).const_smul c)
  · rw [← UniformSpace.Completion.coe_smul, swapQ_coe, swapQ_coe, swapLoc_smul]

theorem swapQ_star (t : ℝ) (x : Quasilocal ι (V × V)) :
    swapQ t (star x) = star (swapQ t x) := by
  refine UniformSpace.Completion.induction_on x ?_ fun a => ?_
  · exact isClosed_eq ((continuous_swapQ t).comp continuous_star)
      (continuous_star.comp (continuous_swapQ t))
  · rw [star_coe, swapQ_coe, swapQ_coe, swapLoc_star]

theorem swapQ_sub (t : ℝ) (x y : Quasilocal ι (V × V)) :
    swapQ t (x - y) = swapQ t x - swapQ t y := by
  rw [sub_eq_add_neg, swapQ_add, ← neg_one_smul ℂ y, swapQ_smul, neg_one_smul, ← sub_eq_add_neg]

theorem swapQ_one (t : ℝ) : swapQ t (1 : Quasilocal ι (V × V)) = 1 := by
  calc swapQ t (1 : Quasilocal ι (V × V))
      = swapQ t ((1 : localAlg ι (V × V)) : Quasilocal ι (V × V)) := by
        rw [UniformSpace.Completion.coe_one]
    _ = swapLoc t 1 := swapQ_coe t 1
    _ = 1 := swapLoc_one t

theorem swapQ_zero_time (x : Quasilocal ι (V × V)) : swapQ 0 x = x := by
  refine UniformSpace.Completion.induction_on x ?_ fun a => ?_
  · exact isClosed_eq (continuous_swapQ 0) continuous_id
  · rw [swapQ_coe, swapLoc_zero]

theorem dist_swapQ (t : ℝ) (x y : Quasilocal ι (V × V)) :
    dist (swapQ t x) (swapQ t y) = dist x y := by
  rw [dist_eq_norm, dist_eq_norm, ← swapQ_sub, norm_swapQ]

theorem continuous_unit_swapGateQ (i : ι) :
    Continuous fun t : ℝ => unit (swapGateQ (V := V) i) t := by
  unfold unit
  fun_prop

theorem continuous_swapU (S : Finset ι) :
    Continuous fun t : ℝ => swapU (V := V) S t := by
  classical
  induction S using Finset.induction_on with
  | empty => simpa using continuous_const
  | insert i s hi ih =>
      have hdis : Disjoint ({i} : Finset ι) s := by simpa using hi
      have hins : (insert i s : Finset ι) = {i} ∪ s := by rw [Finset.insert_eq]
      simp only [hins, fun t => swapU_union (V := V) hdis t, fun t => swapU_singleton (V := V) i t]
      exact (continuous_unit_swapGateQ i).mul ih

theorem continuous_swapLoc (a : localAlg ι (V × V)) :
    Continuous fun t : ℝ => swapLoc t a := by
  classical
  obtain ⟨Λ, X, rfl⟩ := exists_ofM a
  simp only [fun t => swapLoc_ofM t Λ X, swapAct]
  exact ((continuous_swapU Λ).mul continuous_const).mul
    (continuous_star.comp (continuous_swapU Λ))

theorem continuous_swapQ_time (x : Quasilocal ι (V × V)) :
    Continuous fun t : ℝ => swapQ t x := by
  refine continuous_iff_continuousAt.mpr fun t₀ => Metric.continuousAt_iff.mpr fun ε hε => ?_
  have hx : x ∈ closure (Set.range ((↑) : localAlg ι (V × V) → Quasilocal ι (V × V))) := by
    rw [UniformSpace.Completion.denseRange_coe.closure_eq]
    trivial
  obtain ⟨a, ha⟩ := Metric.mem_closure_range_iff.mp hx (ε / 3) (by positivity)
  obtain ⟨δ, hδ, hball⟩ :=
    Metric.continuousAt_iff.mp ((continuous_swapLoc a).continuousAt (x := t₀))
      (ε / 3) (by positivity)
  refine ⟨δ, hδ, fun {t} ht => ?_⟩
  have h1 : dist (swapQ t x) (swapQ t (a : Quasilocal ι (V × V))) < ε / 3 := by
    rw [dist_swapQ]; exact ha
  have h2 : dist (swapQ t₀ (a : Quasilocal ι (V × V))) (swapQ t₀ x) < ε / 3 := by
    rw [dist_swapQ, dist_comm]; exact ha
  have h3 : dist (swapQ t (a : Quasilocal ι (V × V))) (swapQ t₀ (a : Quasilocal ι (V × V)))
      < ε / 3 := by
    rw [swapQ_coe, swapQ_coe]; exact hball ht
  calc dist (swapQ t x) (swapQ t₀ x)
      ≤ dist (swapQ t x) (swapQ t (a : Quasilocal ι (V × V)))
        + dist (swapQ t (a : Quasilocal ι (V × V))) (swapQ t₀ x) := dist_triangle _ _ _
    _ ≤ dist (swapQ t x) (swapQ t (a : Quasilocal ι (V × V)))
        + (dist (swapQ t (a : Quasilocal ι (V × V))) (swapQ t₀ (a : Quasilocal ι (V × V)))
          + dist (swapQ t₀ (a : Quasilocal ι (V × V))) (swapQ t₀ x)) := by
        gcongr
        exact dist_triangle _ _ _
    _ < ε / 3 + (ε / 3 + ε / 3) := by gcongr
    _ = ε := by ring

/-- **THE GROUP LAW FOR THE SWAP LAYER.** -/
theorem swapQ_add_time_stage (t s : ℝ) (Λ : Finset ι)
    (X : Matrix (Conf Λ (V × V)) (Conf Λ (V × V)) ℂ) :
    swapQ t (swapQ s (stage Λ X)) = swapQ (t + s) (stage Λ X) := by
  classical
  obtain ⟨Y, hY⟩ := swapAct_mem_range Λ Λ s X
  set Λ₁ := Λ ∪ Λ with hΛ₁
  set S := Λ ∪ Λ₁ with hS
  have hsub₀ : Λ ⊆ S := Finset.subset_union_left
  have hsub₁ : Λ₁ ⊆ S := Finset.subset_union_right
  have hmid : swapAct S s (stage Λ X) = stage Λ₁ Y := by
    rw [swapAct_stabilizes hsub₀ X s]
    exact hY.symm
  have e1 : swapQ s (stage Λ X) = stage Λ₁ Y := by
    rw [swapQ_stage]
    exact hY.symm
  have e2 : swapQ t (stage Λ₁ Y) = swapAct S t (stage Λ₁ Y) := by
    rw [swapQ_stage, ← swapAct_stabilizes hsub₁ Y t]
  have e3 : swapQ (t + s) (stage Λ X) = swapAct S (t + s) (stage Λ X) := by
    rw [swapQ_stage, ← swapAct_stabilizes hsub₀ X (t + s)]
  rw [e1, e2, e3, ← hmid]
  simp only [swapAct]
  calc swapU S t * (swapU S s * stage Λ X * star (swapU S s)) * star (swapU S t)
      = swapU S t * swapU S s * stage Λ X * (star (swapU S s) * star (swapU S t)) := by
        simp only [mul_assoc]
    _ = swapU S (t + s) * stage Λ X * star (swapU S (t + s)) := by
        rw [swapU_add, ← star_mul, swapU_add]

theorem swapQ_add_time (t s : ℝ) (x : Quasilocal ι (V × V)) :
    swapQ t (swapQ s x) = swapQ (t + s) x := by
  refine UniformSpace.Completion.induction_on x ?_ fun a => ?_
  · exact isClosed_eq ((continuous_swapQ t).comp (continuous_swapQ s)) (continuous_swapQ (t + s))
  · obtain ⟨Λ, X, rfl⟩ := exists_ofM a
    exact swapQ_add_time_stage t s Λ X

theorem swapQ_left_inverse (t : ℝ) (x : Quasilocal ι (V × V)) :
    swapQ (-t) (swapQ t x) = x := by
  rw [swapQ_add_time, neg_add_cancel, swapQ_zero_time]

theorem swapQ_right_inverse (t : ℝ) (x : Quasilocal ι (V × V)) :
    swapQ t (swapQ (-t) x) = x := by
  rw [swapQ_add_time, add_neg_cancel, swapQ_zero_time]

theorem swapQ_bijective (t : ℝ) : Function.Bijective (swapQ (V := V) t) :=
  Function.bijective_iff_has_inverse.mpr
    ⟨swapQ (-t), swapQ_left_inverse t, swapQ_right_inverse t⟩

end Swap

end Extend

end OIBridge.SecondOrderLayer

namespace OIBridge.SecondOrderLayer

#print axioms extConf_comp
#print axioms extConf_refl
#print axioms extPerm_involutive
#print axioms inclObs_permMat
#print axioms qGate_extPerm
#print axioms qGate_comm_of_extComm
#print axioms qGate_isGate
#print axioms qGate_comm_stage_of_disjoint
#print axioms unit_qGate_comm_stage_of_disjoint
#print axioms curOn_gateOn
#print axioms rhs_gateOn
#print axioms gateOn_involutive
#print axioms gateOn_comm
#print axioms rhs_restrict
#print axioms extPerm_gateEquiv
#print axioms disjoint_gateRegion_of_notMem_affected
#print axioms shearGate_isGate
#print axioms shearGate_comm
#print axioms unit_shearGate_comm_stage
#print axioms isGateList_shearGateList
#print axioms layerU_union
#print axioms conj_eq_self_of_commute
#print axioms layerU_star
#print axioms layerAct_stabilizes
#print axioms star_layerU_mul
#print axioms layerU_zero
#print axioms layerAct_eq_of_stage_eq
#print axioms layerLoc_ofM
#print axioms layerLoc_mul
#print axioms layerLoc_add
#print axioms layerLoc_one
#print axioms layerLoc_star
#print axioms layerLoc_zero
#print axioms layerLoc_smul
#print axioms layerLoc_sub
#print axioms layerU_mem_unitary
#print axioms norm_layerLoc
#print axioms isometry_layerLoc
#print axioms layerQ_coe
#print axioms layerQ_stage
#print axioms norm_layerQ
#print axioms layerQ_mul
#print axioms layerQ_add
#print axioms layerQ_one
#print axioms layerQ_zero_time
#print axioms continuous_unit_shearGate
#print axioms continuous_layerU
#print axioms continuous_layerLoc
#print axioms layerQ_smul
#print axioms layerQ_star
#print axioms layerQ_sub
#print axioms dist_layerQ
#print axioms continuous_layerQ_time
#print axioms mem_range_stage_le
#print axioms unit_shearGate_mem_range
#print axioms layerU_mem_range
#print axioms layerAct_mem_range
#print axioms layerU_add
#print axioms layerQ_add_time_stage
#print axioms layerQ_add_time
#print axioms layerQ_left_inverse
#print axioms layerQ_bijective
#print axioms swapGateQ_isGate
#print axioms swapGateQ_comm
#print axioms swapU_add
#print axioms swapAct_stabilizes
#print axioms swapLoc_ofM
#print axioms norm_swapLoc
#print axioms swapQ_coe
#print axioms swapQ_mul
#print axioms swapQ_star
#print axioms swapQ_zero_time
#print axioms continuous_swapQ_time
#print axioms swapQ_add_time
#print axioms swapQ_bijective

end OIBridge.SecondOrderLayer
