import OIBridge.CompositionOrder
import OIBridge.TransitiveBody

/-!
# Origin passive — design module of the research thread `research/origin` (round 2, O5 and O6)

A design artifact on a disposable branch; it is not part of any governed round and asserts no
status. It records the kernel content of the thread's sharpened Lemma P and of the finite-order
step of its passive-tower exclusion.

* **Lemma P, abstract** (`lemmaP_extreme`). If an extreme point `ω` of a set `K` is the
  `r ω`-weighted mixture of a state of `K` on which the readout `r` reads `1` and another state of
  `K` — the native observation of `r` is passive and repeatable at `ω` — then `r ω` is `0` or `1`.
* **Classical carrier** (`extreme_cellMass_det`, `extreme_not_balanced`, `pointMass_of_cells`,
  `extreme_pointMass_of_passive`). For a body of probability vectors over a finite configuration
  set and readouts given by cells, passive repeatable cell readouts make every extreme point
  outcome-deterministic for every cell, so no extreme point is balanced; when the cells separate
  the configurations, every extreme point is a point mass.
* **Finite order** (`extremePoints_finite_of_binary`, `finiteOrderOn_of_finite_extremePoints`,
  `finiteOrderOn_of_binary`, `not_infiniteOrderOn_of_binary`). Extreme points whose values under
  a map injective on them are all `0` or `1` are finitely many; an affine automorphism preserving
  a compact convex body with finitely many extreme points has finite order on it (`FiniteOrderOn`
  of `CompositionOrder`), so it does not have infinite order there.
-/

namespace OIBridge
namespace OriginPassive

/-! ### Section A — Lemma P -/

section Abstract

variable {E : Type*} [AddCommGroup E] [Module ℝ E]

/-- **Lemma P (abstract).** At an extreme point, a passive repeatable readout is deterministic:
if `ω` is the `r ω`-weighted mixture of a state `ω₀` of `K` with `r ω₀ = 1` and a state `ω₁` of
`K`, and `0 ≤ r ω ≤ 1`, then `r ω` is `0` or `1`. -/
theorem lemmaP_extreme {K : Set E} (r : E → ℝ) {ω ω₀ ω₁ : E}
    (hω : ω ∈ K.extremePoints ℝ) (h₀ : ω₀ ∈ K) (h₁ : ω₁ ∈ K) (hr₀ : r ω₀ = 1)
    (hrange : 0 ≤ r ω ∧ r ω ≤ 1) (hpass : r ω • ω₀ + (1 - r ω) • ω₁ = ω) :
    r ω = 0 ∨ r ω = 1 := by
  by_contra hne
  have hne0 : r ω ≠ 0 := fun h => hne (Or.inl h)
  have hne1 : r ω ≠ 1 := fun h => hne (Or.inr h)
  have hpos : 0 < r ω := lt_of_le_of_ne hrange.1 (Ne.symm hne0)
  have hlt : r ω < 1 := lt_of_le_of_ne hrange.2 hne1
  have hseg : ω ∈ openSegment ℝ ω₀ ω₁ :=
    ⟨r ω, 1 - r ω, hpos, by linarith, by ring, hpass⟩
  have heq : ω₀ = ω := hω.2 h₀ h₁ hseg
  rw [heq] at hr₀
  exact hne1 hr₀

end Abstract

/-! ### Section B — the classical carrier -/

section Classical

variable {Ω : Type*} [Fintype Ω] [DecidableEq Ω]

/-- The mass a distribution puts on a cell: the probability of the cell's outcome. -/
def cellMass (C : Finset Ω) (ω : Ω → ℝ) : ℝ := ∑ x ∈ C, ω x

theorem cellMass_nonneg (C : Finset Ω) {ω : Ω → ℝ} (hnn : ∀ x, 0 ≤ ω x) :
    0 ≤ cellMass C ω :=
  Finset.sum_nonneg fun x _ => hnn x

theorem cellMass_le_one (C : Finset Ω) {ω : Ω → ℝ} (hnn : ∀ x, 0 ≤ ω x)
    (hsum : ∑ x, ω x = 1) : cellMass C ω ≤ 1 := by
  rw [← hsum]
  exact Finset.sum_le_sum_of_subset_of_nonneg (Finset.subset_univ C) fun x _ _ => hnn x

/-- **Passive repeatable cell readouts are deterministic at extreme points.** The passivity
hypothesis asks, at every state of the body whose cell mass is strictly between `0` and `1`, for
the observe-and-forget decomposition into a state with cell mass `1` and another state of the
body, weighted by the cell mass. -/
theorem extreme_cellMass_det {ι : Type*} (C : ι → Finset Ω)
    {K : Set (Ω → ℝ)} (hK : ∀ ω ∈ K, (∀ x, 0 ≤ ω x) ∧ ∑ x, ω x = 1)
    (hpass : ∀ i, ∀ ω ∈ K, 0 < cellMass (C i) ω → cellMass (C i) ω < 1 →
      ∃ ω₀ ∈ K, ∃ ω₁ ∈ K, cellMass (C i) ω₀ = 1 ∧
        cellMass (C i) ω • ω₀ + (1 - cellMass (C i) ω) • ω₁ = ω)
    {ω : Ω → ℝ} (hω : ω ∈ K.extremePoints ℝ) (i : ι) :
    cellMass (C i) ω = 0 ∨ cellMass (C i) ω = 1 := by
  obtain ⟨hnn, hsum⟩ := hK ω hω.1
  by_contra hne
  have hne0 : cellMass (C i) ω ≠ 0 := fun h => hne (Or.inl h)
  have hne1 : cellMass (C i) ω ≠ 1 := fun h => hne (Or.inr h)
  have hpos : 0 < cellMass (C i) ω := lt_of_le_of_ne (cellMass_nonneg _ hnn) (Ne.symm hne0)
  have hlt : cellMass (C i) ω < 1 := lt_of_le_of_ne (cellMass_le_one _ hnn hsum) hne1
  obtain ⟨ω₀, h₀, ω₁, h₁, hm₀, hdec⟩ := hpass i ω hω.1 hpos hlt
  rcases lemmaP_extreme (cellMass (C i)) hω h₀ h₁ hm₀ ⟨le_of_lt hpos, le_of_lt hlt⟩ hdec
    with h | h
  · exact hne0 h
  · exact hne1 h

/-- **No balanced extreme point.** Under the same passivity hypothesis no extreme point of the
body gives any cell the probability `1 / 2`. -/
theorem extreme_not_balanced {ι : Type*} (C : ι → Finset Ω)
    {K : Set (Ω → ℝ)} (hK : ∀ ω ∈ K, (∀ x, 0 ≤ ω x) ∧ ∑ x, ω x = 1)
    (hpass : ∀ i, ∀ ω ∈ K, 0 < cellMass (C i) ω → cellMass (C i) ω < 1 →
      ∃ ω₀ ∈ K, ∃ ω₁ ∈ K, cellMass (C i) ω₀ = 1 ∧
        cellMass (C i) ω • ω₀ + (1 - cellMass (C i) ω) • ω₁ = ω)
    {ω : Ω → ℝ} (hω : ω ∈ K.extremePoints ℝ) (i : ι) :
    cellMass (C i) ω ≠ 1 / 2 := by
  intro h
  rcases extreme_cellMass_det C hK hpass hω i with h' | h'
  · rw [h'] at h
    norm_num at h
  · rw [h'] at h
    norm_num at h

/-- **Deterministic separating cells pin a point mass.** A probability vector whose mass on every
cell of a family separating the configurations is `0` or `1` is a point mass. -/
theorem pointMass_of_cells {ι : Type*} (C : ι → Finset Ω)
    (hsep : ∀ x y : Ω, x ≠ y → ∃ i, x ∈ C i ∧ y ∉ C i)
    {ω : Ω → ℝ} (hnn : ∀ x, 0 ≤ ω x) (hsum : ∑ x, ω x = 1)
    (hdet : ∀ i, cellMass (C i) ω = 0 ∨ cellMass (C i) ω = 1) :
    ∃ x₀, ∀ x, ω x = if x = x₀ then 1 else 0 := by
  have hex : ∃ x₀, 0 < ω x₀ := by
    by_contra h
    have hle : ∀ x, ω x ≤ 0 := fun x => not_lt.mp fun hx => h ⟨x, hx⟩
    have hz : ∑ x, ω x = 0 := Finset.sum_eq_zero fun x _ => le_antisymm (hle x) (hnn x)
    rw [hsum] at hz
    exact one_ne_zero hz
  obtain ⟨x₀, hx₀⟩ := hex
  have hzero : ∀ y, y ≠ x₀ → ω y = 0 := by
    intro y hy
    by_contra hy0
    have hypos : 0 < ω y := lt_of_le_of_ne (hnn y) (Ne.symm hy0)
    obtain ⟨i, hxi, hyi⟩ := hsep x₀ y (Ne.symm hy)
    have hmpos : 0 < cellMass (C i) ω :=
      lt_of_lt_of_le hx₀ (Finset.single_le_sum (fun x _ => hnn x) hxi)
    have hm1 : cellMass (C i) ω = 1 := by
      rcases hdet i with h | h
      · rw [h] at hmpos
        exact absurd hmpos (lt_irrefl 0)
      · exact h
    have hsplit := Finset.sum_add_sum_compl (C i) ω
    have hm1' : ∑ x ∈ C i, ω x = 1 := hm1
    have hcompl : ∑ x ∈ (C i)ᶜ, ω x = 0 := by linarith
    have hyc : y ∈ (C i)ᶜ := Finset.mem_compl.mpr hyi
    have hle : ω y ≤ ∑ x ∈ (C i)ᶜ, ω x := Finset.single_le_sum (fun x _ => hnn x) hyc
    linarith
  have hone : ω x₀ = 1 := by
    rw [← hsum]
    exact (Finset.sum_eq_single x₀ (fun b _ hb => hzero b hb)
      (fun h => absurd (Finset.mem_univ x₀) h)).symm
  refine ⟨x₀, fun x => ?_⟩
  by_cases h : x = x₀
  · rw [if_pos h, h, hone]
  · rw [if_neg h]
    exact hzero x h

/-- **Passive repeatable separating cell readouts make every extreme point a point mass.** -/
theorem extreme_pointMass_of_passive {ι : Type*} (C : ι → Finset Ω)
    (hsep : ∀ x y : Ω, x ≠ y → ∃ i, x ∈ C i ∧ y ∉ C i)
    {K : Set (Ω → ℝ)} (hK : ∀ ω ∈ K, (∀ x, 0 ≤ ω x) ∧ ∑ x, ω x = 1)
    (hpass : ∀ i, ∀ ω ∈ K, 0 < cellMass (C i) ω → cellMass (C i) ω < 1 →
      ∃ ω₀ ∈ K, ∃ ω₁ ∈ K, cellMass (C i) ω₀ = 1 ∧
        cellMass (C i) ω • ω₀ + (1 - cellMass (C i) ω) • ω₁ = ω)
    {ω : Ω → ℝ} (hω : ω ∈ K.extremePoints ℝ) :
    ∃ x₀, ∀ x, ω x = if x = x₀ then 1 else 0 :=
  pointMass_of_cells C hsep (hK ω hω.1).1 (hK ω hω.1).2 (extreme_cellMass_det C hK hpass hω)

end Classical

/-! ### Section C — finitely many extreme points, finite order -/

section FiniteOrder

/-- **Binary values give finitely many extreme points.** If a map `L` into `Fin d → ℝ` is
injective on the extreme points of `K` and takes only the values `0` and `1` on them, the extreme
points are finitely many. -/
theorem extremePoints_finite_of_binary {E : Type*} [AddCommGroup E] [Module ℝ E] {d : ℕ}
    {K : Set E} (L : E → (Fin d → ℝ)) (hinj : Set.InjOn L (K.extremePoints ℝ))
    (hbin : ∀ ω ∈ K.extremePoints ℝ, ∀ j, L ω j = 0 ∨ L ω j = 1) :
    (K.extremePoints ℝ).Finite := by
  refine Set.Finite.of_finite_image ?_ hinj
  have hfin : (Set.pi Set.univ fun _ : Fin d => ({0, 1} : Set ℝ)).Finite :=
    Set.Finite.pi fun _ => Set.toFinite _
  apply hfin.subset
  rintro v ⟨ω, hω, rfl⟩
  refine fun j _ => ?_
  rcases hbin ω hω j with h | h
  · rw [h]
    exact Set.mem_insert 0 {1}
  · rw [h]
    exact Set.mem_insert_of_mem 0 (Set.mem_singleton 1)

variable {V : Type} [NormedAddCommGroup V] [NormedSpace ℝ V] [FiniteDimensional ℝ V]

/-- **Finitely many extreme points give finite order.** An affine automorphism carrying a compact
convex body `K` onto itself, when `K` has finitely many extreme points, has a positive power that
fixes every point of `K`: it permutes the extreme points, a common period fixes all of them, and
the fixed set of that power is convex and closed, so by Krein–Milman it contains `K`. -/
theorem finiteOrderOn_of_finite_extremePoints {K : Set V} (hc : IsCompact K)
    (hconv : Convex ℝ K) (hfin : (K.extremePoints ℝ).Finite) {g : V ≃ᵃ[ℝ] V}
    (hg : ∀ x ∈ K, g x ∈ K ∧ g.symm x ∈ K) : CompositionOrder.FiniteOrderOn K g := by
  classical
  have hper : ∀ w ∈ hfin.toFinset, ∃ p : ℕ, 0 < p ∧ (⇑g)^[p] w = w := by
    intro w hw
    exact CompositionOrder.exists_return g.injective
      (fun u hu => (Set.Finite.mem_toFinset hfin).2
        (TransitiveBody.extreme_image hg ((Set.Finite.mem_toFinset hfin).1 hu))) hw
  obtain ⟨N, hN, hNE⟩ := CompositionOrder.exists_common_period hfin.toFinset hper
  obtain ⟨h, hh⟩ : ∃ h : V →ᵃ[ℝ] V, ⇑h = (⇑g)^[N] :=
    ⟨CompositionOrder.affPow g.toAffineMap N, by
      rw [CompositionOrder.coe_affPow, AffineEquiv.coe_toAffineMap]⟩
  have hconvF : Convex ℝ {x : V | h x = x} := by
    intro x hx y hy a b _ _ hab
    have hx' : h x = x := hx
    have hy' : h y = y := hy
    show h (a • x + b • y) = a • x + b • y
    rw [Convex.combo_affine_apply hab, hx', hy']
  have hclosedF : IsClosed {x : V | h x = x} :=
    isClosed_eq h.continuous_of_finiteDimensional continuous_id
  have hsub : K.extremePoints ℝ ⊆ {x : V | h x = x} := by
    intro w hw
    show h w = w
    rw [hh]
    exact hNE w ((Set.Finite.mem_toFinset hfin).2 hw)
  refine ⟨N, hN, fun x hx => ?_⟩
  have hx' : x ∈ closure (convexHull ℝ (K.extremePoints ℝ)) := by
    rw [closure_convexHull_extremePoints hc hconv]
    exact hx
  have hfix : h x = x := closure_minimal (convexHull_min hsub hconvF) hclosedF hx'
  rw [hh] at hfix
  exact hfix

/-- **Binary extreme points give finite order.** -/
theorem finiteOrderOn_of_binary {d : ℕ} {K : Set V} (hc : IsCompact K) (hconv : Convex ℝ K)
    (L : V → (Fin d → ℝ)) (hinj : Set.InjOn L (K.extremePoints ℝ))
    (hbin : ∀ ω ∈ K.extremePoints ℝ, ∀ j, L ω j = 0 ∨ L ω j = 1)
    {g : V ≃ᵃ[ℝ] V} (hg : ∀ x ∈ K, g x ∈ K ∧ g.symm x ∈ K) :
    CompositionOrder.FiniteOrderOn K g :=
  finiteOrderOn_of_finite_extremePoints hc hconv (extremePoints_finite_of_binary L hinj hbin) hg

/-- **No infinite-order automorphism when the extreme points are binary.** -/
theorem not_infiniteOrderOn_of_binary {d : ℕ} {K : Set V} (hc : IsCompact K)
    (hconv : Convex ℝ K) (L : V → (Fin d → ℝ)) (hinj : Set.InjOn L (K.extremePoints ℝ))
    (hbin : ∀ ω ∈ K.extremePoints ℝ, ∀ j, L ω j = 0 ∨ L ω j = 1)
    {g : V ≃ᵃ[ℝ] V} (hg : ∀ x ∈ K, g x ∈ K ∧ g.symm x ∈ K) :
    ¬ CompositionOrder.InfiniteOrderOn K g :=
  CompositionOrder.not_infiniteOrderOn_of_finiteOrderOn
    (finiteOrderOn_of_binary hc hconv L hinj hbin hg)

end FiniteOrder

#print axioms lemmaP_extreme
#print axioms cellMass_nonneg
#print axioms cellMass_le_one
#print axioms extreme_cellMass_det
#print axioms extreme_not_balanced
#print axioms pointMass_of_cells
#print axioms extreme_pointMass_of_passive
#print axioms extremePoints_finite_of_binary
#print axioms finiteOrderOn_of_finite_extremePoints
#print axioms finiteOrderOn_of_binary
#print axioms not_infiniteOrderOn_of_binary

end OriginPassive
end OIBridge
