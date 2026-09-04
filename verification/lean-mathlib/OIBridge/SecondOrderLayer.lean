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

end OIBridge.SecondOrderLayer
