/-
  OIBridge/TransitiveBody.lean — round TRB-1 (architectural round 2): the completed-chart adapter, the
  boundary-state bridge, boundary purity, and the invariant-inner-product ball of a boundary-transitive
  body. TRANS alone: no order predicate of any kind is defined or used here (the order side, ORD∞, is
  round ORD-1's), so the module carries no edge from transitivity to order.

  Everything here is stated for a compact convex body `Ω` with nonempty interior in coordinates
  `Fin d → ℝ`, or for the chart body of a completion chart (`CompletionAction.chartBody`), which §A
  shows is such a body. The inputs are the landed vocabulary of `KInfFoundations` (boundary states),
  `OrbitGeneration` (`PreservesBody`, `BoundaryTransitive`), `InvariantInnerProduct` (centroid and
  `invMatrix`) and `CompletionAction` (charts). No flow, no drive, no sharp seed, no availability and
  no dimension other than the body's own enter any statement.

    §A  the chart body is compact, convex and has nonempty interior, with no finite-dimensionality of
        the completion space (`chartBody_isCompact`, `chartBody_convex`, `chartBody_interior_nonempty`);
    §B  the boundary-state bridge, one theorem per direction: a boundary state is a frontier point
        (`frontier_of_isBoundaryState`), and a point of a convex set with interior that is not interior
        is a boundary state (`isBoundaryState_of_frontier`); the ray from an interior point meets the
        boundary in a boundary state (`exists_boundary_ray`);
    §C  TRANS: `IsBodyGroup` (identity, composition, inverses, body preservation) and `TransBody` (a body
        group acting transitively on every boundary state); nothing about the order of any member;
    §D  boundary purity: under a body-preserving boundary-transitive family every boundary state is an
        extreme point; a body with a non-extreme boundary state is boundary transitive for no
        body-preserving family (`not_boundaryTransitive_of_nonextreme_boundary`);
    §E  the invariant-inner-product ball: the centroid lies in the body and, under transitivity, in its
        interior; every boundary state lies on one `Q`-sphere about the centroid (`boundary_qnorm_const`),
        and the body is the closed `Q`-ball (`eq_qBall_of_boundaryTransitive`); only body preservation,
        all-boundary transitivity and the invariant inner product are used — no composition closure;
    §F  the normalization adapter, frozen as statements: `invMatrix Ω` factors as `Bᵀ * B`
        (`exists_factor_invMatrix`), the invariant form is a sum of squares in linear coordinates
        (`qnorm_eq_sum_sq`), and the body is an affine image of the coordinate Euclidean ball of its
        dimension (`exists_affine_image_eq_eball`); the chart-body and `TransBody` forms are corollaries;
    §G  controls, the transitivity side only: on `ball3`, all automorphisms form a transitive body group;
        the Householder reflections are boundary transitive as a set; the rotation flow is not
        transitive; and the square and the octahedron are boundary transitive for no body-preserving
        family.

  The ball theorem (§E) is proved in the invariant quadratic form by the ray argument of §B; the
  ambient-norm lemma `KInfFoundations.eq_closedBall_of_frontier_subset_sphere` is not used.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.CompletionAction
import OIBridge.InvariantInnerProduct
import Mathlib.Analysis.Convex.KreinMilman
import Mathlib.Analysis.Convex.Topology
import Mathlib.Analysis.Normed.Module.FiniteDimension
import Mathlib.LinearAlgebra.Matrix.PosDef
import Mathlib.Analysis.Matrix.LDL

namespace OIBridge
namespace TransitiveBody

open Set Topology Matrix MeasureTheory KInfFoundations OrbitGeneration OrbitNormalization
  StageCompletion CompletionAction InvariantInnerProduct

/-! ### §A — the completed-chart adapter -/

section Chart

variable {D : DirectedStages} (C : CompletionChart D)

/-- The preparation vectors have sup norm at most one. -/
theorem norm_prepVec_le_one (x : Prep D) : ‖prepVec D x‖ ≤ 1 :=
  lp.norm_le_of_forall_le zero_le_one fun a => by
    rw [show (prepVec D x) a = val D a x from coord_prepVec D a x]
    exact norm_val_le_one D a x

/-- The completed body lies in the closed unit ball of the completion space. -/
theorem body_subset_closedBall : body D ⊆ Metric.closedBall (0 : CSpace D) 1 :=
  body_subset D (convex_closedBall 0 1) Metric.isClosed_closedBall fun x => by
    rw [Metric.mem_closedBall, dist_zero_right]
    exact norm_prepVec_le_one x

/-- The chart is continuous: its linear part is a linear map from a finite-dimensional space. -/
theorem continuous_chart : Continuous (chart C.L C.p0) :=
  (chart C.L C.p0).continuous_of_finiteDimensional

/-- The chart body is convex. -/
theorem chartBody_convex : Convex ℝ (chartBody C) :=
  (body_convex (D := D)).affine_preimage (chart C.L C.p0)

/-- The chart body is closed. -/
theorem chartBody_isClosed : IsClosed (chartBody C) :=
  (body_isClosed (D := D)).preimage (continuous_chart C)

/-- The chart body is bounded: the chart's linear part is injective from a finite-dimensional space,
hence antilipschitz, and the body lies in the unit ball. -/
theorem chartBody_isBounded : Bornology.IsBounded (chartBody C) := by
  obtain ⟨K, -, hK⟩ := C.L.exists_antilipschitzWith C.hL
  refine (Metric.isBounded_closedBall (x := (0 : Fin C.d → ℝ))
    (r := (K : ℝ) * (1 + ‖C.p0‖))).subset ?_
  intro w hw
  have hw' : chart C.L C.p0 w ∈ body D := hw
  rw [Metric.mem_closedBall, dist_zero_right]
  have h1 : ‖chart C.L C.p0 w‖ ≤ 1 := by
    have := body_subset_closedBall (D := D) hw'
    rwa [Metric.mem_closedBall, dist_zero_right] at this
  have h2 : ‖C.L w‖ ≤ 1 + ‖C.p0‖ := by
    have hEq : C.L w = chart C.L C.p0 w - C.p0 := by rw [chart_apply]; abel
    rw [hEq]
    exact (norm_sub_le _ _).trans (add_le_add h1 le_rfl)
  calc ‖w‖ = dist w 0 := (dist_zero_right w).symm
    _ ≤ (K : ℝ) * dist (C.L w) (C.L 0) := hK.le_mul_dist w 0
    _ = (K : ℝ) * ‖C.L w‖ := by rw [map_zero, dist_zero_right]
    _ ≤ (K : ℝ) * (1 + ‖C.p0‖) := mul_le_mul_of_nonneg_left h2 (NNReal.coe_nonneg K)

/-- **The chart body is compact.** No finite-dimensionality of the completion space is used. -/
theorem chartBody_isCompact : IsCompact (chartBody C) :=
  Metric.isCompact_of_isClosed_isBounded (chartBody_isClosed C) (chartBody_isBounded C)

/-- The chart body affinely spans the chart. -/
theorem affineSpan_chartBody : affineSpan ℝ (chartBody C) = ⊤ := by
  refine le_antisymm le_top ?_
  rw [← affineSpan_gen C]
  refine affineSpan_mono ℝ ?_
  rintro _ ⟨x, rfl⟩
  exact coordsOf_mem_chartBody C (prepVec_mem_body D x)

/-- **The chart body has nonempty interior.** -/
theorem chartBody_interior_nonempty : (interior (chartBody C)).Nonempty :=
  (chartBody_convex C).interior_nonempty_iff_affineSpan_eq_top.mpr (affineSpan_chartBody C)

end Chart

/-! ### §B — the boundary-state bridge and the ray lemma -/

section Bridge

variable {V : Type} [NormedAddCommGroup V] [NormedSpace ℝ V]

/-- **Bridge (→).** A boundary state is a frontier point. -/
theorem frontier_of_isBoundaryState {Ω : Set V} {x : V} (hx : IsBoundaryState Ω x) :
    x ∈ frontier Ω :=
  ⟨subset_closure hx.1, fun hint => not_isBoundaryState_of_mem_interior hint hx⟩

/-- **Bridge (←).** In a convex set with an interior point, a point of the set that is not interior is
a boundary state. -/
theorem isBoundaryState_of_frontier {Ω : Set V} (hconv : Convex ℝ Ω) (hi : (interior Ω).Nonempty)
    {x : V} (hxΩ : x ∈ Ω) (hx : x ∉ interior Ω) : IsBoundaryState Ω x := by
  obtain ⟨y, hy⟩ := hi
  refine ⟨hxΩ, y, interior_subset hy, fun ε hε hmem => hx ?_⟩
  have h1 : (0 : ℝ) < 1 + ε := by linarith
  have key : x ∈ openSegment ℝ y (x + ε • (x - y)) := by
    refine ⟨ε / (1 + ε), 1 / (1 + ε), div_pos hε h1, div_pos one_pos h1, ?_, ?_⟩
    · field_simp
      ring
    · match_scalars <;> field_simp <;> ring
  exact hconv.openSegment_interior_self_subset_interior hy hmem key

/-- **The ray lemma.** The ray from an interior point `c` in a nonzero direction `u` stays in a compact
convex body up to a last parameter `t > 0`, leaves it beyond `t`, and its point at `t` is a boundary
state. -/
theorem exists_boundary_ray {Ω : Set V} (hc : IsCompact Ω) (hconv : Convex ℝ Ω) {c : V}
    (hci : c ∈ interior Ω) {u : V} (hu : u ≠ 0) :
    ∃ t : ℝ, 0 < t ∧ c + t • u ∈ Ω ∧ (∀ s, t < s → c + s • u ∉ Ω) ∧
      (∀ s, 0 ≤ s → s ≤ t → c + s • u ∈ Ω) ∧ IsBoundaryState Ω (c + t • u) := by
  have hcΩ : c ∈ Ω := interior_subset hci
  have hun : 0 < ‖u‖ := norm_pos_iff.mpr hu
  set S : Set ℝ := Ici (0 : ℝ) ∩ (fun t : ℝ => c + t • u) ⁻¹' Ω with hSdef
  have hmemS : ∀ t, t ∈ S ↔ 0 ≤ t ∧ c + t • u ∈ Ω := fun t => Iff.rfl
  have hcont : Continuous fun t : ℝ => c + t • u :=
    continuous_const.add (continuous_id.smul continuous_const)
  have hSclosed : IsClosed S := isClosed_Ici.inter (hc.isClosed.preimage hcont)
  obtain ⟨R, hR⟩ := hc.isBounded.subset_closedBall (0 : V)
  have hSbdd : S ⊆ Icc 0 ((R + ‖c‖) / ‖u‖) := by
    intro t ht
    obtain ⟨ht0, htΩ⟩ := (hmemS t).mp ht
    refine ⟨ht0, ?_⟩
    rw [le_div_iff₀ hun]
    have h1 : ‖c + t • u‖ ≤ R := by
      have := hR htΩ
      rwa [Metric.mem_closedBall, dist_zero_right] at this
    have h2 : ‖t • u‖ ≤ ‖c + t • u‖ + ‖c‖ := by
      calc ‖t • u‖ = ‖(c + t • u) - c‖ := by congr 1; abel
        _ ≤ ‖c + t • u‖ + ‖c‖ := norm_sub_le _ _
    rw [norm_smul, Real.norm_of_nonneg ht0] at h2
    linarith
  have hScomp : IsCompact S :=
    Metric.isCompact_of_isClosed_isBounded hSclosed ((Metric.isBounded_Icc 0 _).subset hSbdd)
  have h0S : (0 : ℝ) ∈ S := (hmemS 0).mpr ⟨le_rfl, by simpa using hcΩ⟩
  have hne : S.Nonempty := ⟨0, h0S⟩
  set t := sSup S with ht
  have htS : t ∈ S := hScomp.sSup_mem hne
  obtain ⟨ht0, htΩ⟩ := (hmemS t).mp htS
  have hbdd : BddAbove S := hScomp.isBounded.bddAbove
  -- t is positive: a small step along u stays in the interior ball
  obtain ⟨ε, hε, hball⟩ := Metric.mem_nhds_iff.mp (mem_interior_iff_mem_nhds.mp hci)
  have htpos : 0 < t := by
    have ht₀ : ε / (2 * ‖u‖) ∈ S := by
      refine (hmemS _).mpr ⟨by positivity, hball ?_⟩
      rw [Metric.mem_ball, dist_eq_norm, add_sub_cancel_left, norm_smul,
        Real.norm_of_nonneg (by positivity)]
      have hhalf : ε / (2 * ‖u‖) * ‖u‖ = ε / 2 := by field_simp
      rw [hhalf]
      linarith
    exact lt_of_lt_of_le (by positivity) (le_csSup hbdd ht₀)
  refine ⟨t, htpos, htΩ, fun s hs hsΩ => ?_, fun s hs0 hst => ?_, ⟨htΩ, c, hcΩ, fun ε' hε' hbad => ?_⟩⟩
  · have hsS : s ∈ S := (hmemS s).mpr ⟨by linarith, hsΩ⟩
    exact absurd (le_csSup hbdd hsS) (not_le.mpr hs)
  · -- convexity along the segment from c to c + t • u
    have hst' : s / t ≤ 1 := (div_le_one htpos).mpr hst
    have hEq : c + s • u = (1 - s / t) • c + (s / t) • (c + t • u) := by
      match_scalars <;> field_simp <;> ring
    rw [hEq]
    exact hconv hcΩ htΩ (by linarith) (by positivity) (by ring)
  · have hEq : c + t • u + ε' • (c + t • u - c) = c + ((1 + ε') * t) • u := by module
    rw [hEq] at hbad
    have hgt : t < (1 + ε') * t := by nlinarith
    have hsS : (1 + ε') * t ∈ S := (hmemS _).mpr ⟨by positivity, hbad⟩
    exact absurd (le_csSup hbdd hsS) (not_le.mpr hgt)

end Bridge

/-! ### §C — TRANS -/

section Predicates

variable {V : Type} [NormedAddCommGroup V] [NormedSpace ℝ V]

/-- **TRANS, the group clause.** `G` contains the identity, is closed under composition and
inversion, and every member maps `Ω` into `Ω`. -/
structure IsBodyGroup (Ω : Set V) (G : Set (V ≃ᵃ[ℝ] V)) : Prop where
  one_mem : AffineEquiv.refl ℝ V ∈ G
  mul_mem : ∀ g ∈ G, ∀ h ∈ G, g.trans h ∈ G
  inv_mem : ∀ g ∈ G, g.symm ∈ G
  preserves : ∀ g ∈ G, ∀ x ∈ Ω, g x ∈ Ω

/-- A body group preserves the body in the sense of `OrbitGeneration`. -/
theorem IsBodyGroup.preservesBody {Ω : Set V} {G : Set (V ≃ᵃ[ℝ] V)} (h : IsBodyGroup Ω G) :
    PreservesBody Ω G := fun g hg x hx =>
  ⟨h.preserves g hg x hx, h.preserves g.symm (h.inv_mem g hg) x hx⟩

/-- **TRANS.** A body group acting transitively on every boundary state of `Ω`. -/
def TransBody (Ω : Set V) (G : Set (V ≃ᵃ[ℝ] V)) : Prop := IsBodyGroup Ω G ∧ BoundaryTransitive Ω G

end Predicates

/-! ### §D — boundary purity and polytope exclusion -/

section Purity

variable {V : Type} [NormedAddCommGroup V] [NormedSpace ℝ V]

/-- An affine automorphism of `Ω` carries extreme points to extreme points. -/
theorem extreme_image {Ω : Set V} {g : V ≃ᵃ[ℝ] V} (hg : ∀ x ∈ Ω, g x ∈ Ω ∧ g.symm x ∈ Ω) {x : V}
    (hx : x ∈ Ω.extremePoints ℝ) : g x ∈ Ω.extremePoints ℝ := by
  refine ⟨(hg x hx.1).1, ?_⟩
  intro y₁ hy₁ y₂ hy₂ hseg
  have himg := image_openSegment ℝ g.symm.toAffineMap y₁ y₂
  rw [AffineEquiv.coe_toAffineMap] at himg
  have hmem : g.symm (g x) ∈ (⇑g.symm) '' openSegment ℝ y₁ y₂ := Set.mem_image_of_mem _ hseg
  rw [himg, AffineEquiv.symm_apply_apply] at hmem
  have hh := hx.2 (hg y₁ hy₁).2 (hg y₂ hy₂).2 hmem
  rw [← hh, AffineEquiv.apply_symm_apply]

/-- An extreme point is not an interior point. -/
theorem not_mem_interior_of_extreme [Nontrivial V] {Ω : Set V} {x : V}
    (hx : x ∈ Ω.extremePoints ℝ) : x ∉ interior Ω := by
  intro hint
  obtain ⟨ε, hε, hball⟩ := Metric.mem_nhds_iff.mp (mem_interior_iff_mem_nhds.mp hint)
  obtain ⟨u, hu⟩ := exists_ne (0 : V)
  have hun : 0 < ‖u‖ := norm_pos_iff.mpr hu
  set v : V := (ε / (2 * ‖u‖)) • u with hv
  have hvn : ‖v‖ = ε / 2 := by
    rw [hv, norm_smul, Real.norm_of_nonneg (by positivity)]
    field_simp
  have hv0 : v ≠ 0 := by
    intro h0
    rw [h0, norm_zero] at hvn
    linarith
  have hmem₁ : x - v ∈ Ω := hball (by
    rw [Metric.mem_ball, dist_eq_norm, sub_sub_cancel_left, norm_neg, hvn]; linarith)
  have hmem₂ : x + v ∈ Ω := hball (by
    rw [Metric.mem_ball, dist_eq_norm, add_sub_cancel_left, hvn]; linarith)
  have hseg : x ∈ openSegment ℝ (x - v) (x + v) :=
    ⟨1 / 2, 1 / 2, by norm_num, by norm_num, by norm_num, by module⟩
  have h1 := hx.2 hmem₁ hmem₂ hseg
  apply hv0
  have : x - v = x - 0 := by rw [sub_zero]; exact h1
  exact sub_right_injective this

/-- An extreme point of a convex body with interior is a boundary state. -/
theorem isBoundaryState_of_extreme [Nontrivial V] {Ω : Set V} (hconv : Convex ℝ Ω)
    (hi : (interior Ω).Nonempty) {x : V} (hx : x ∈ Ω.extremePoints ℝ) : IsBoundaryState Ω x :=
  isBoundaryState_of_frontier hconv hi hx.1 (not_mem_interior_of_extreme hx)

/-- **Boundary purity.** Under a body-preserving boundary-transitive family, every boundary state of a
compact convex body with interior is an extreme point. -/
theorem extreme_of_isBoundaryState_of_transitive [Nontrivial V] {Ω : Set V} (hc : IsCompact Ω)
    (hconv : Convex ℝ Ω) (hi : (interior Ω).Nonempty) {G : Set (V ≃ᵃ[ℝ] V)}
    (hG : PreservesBody Ω G) (hT : BoundaryTransitive Ω G) {x : V} (hx : IsBoundaryState Ω x) :
    x ∈ Ω.extremePoints ℝ := by
  obtain ⟨x₀, hx₀⟩ := hc.extremePoints_nonempty ⟨x, hx.1⟩
  obtain ⟨g, hg, hgx⟩ := hT x₀ x (isBoundaryState_of_extreme hconv hi hx₀) hx
  rw [← hgx]
  exact extreme_image (hG g hg) hx₀

/-- **Polytope exclusion.** A body with a boundary state that is not extreme is boundary transitive for
no body-preserving family. -/
theorem not_boundaryTransitive_of_nonextreme_boundary [Nontrivial V] {Ω : Set V} (hc : IsCompact Ω)
    (hconv : Convex ℝ Ω) (hi : (interior Ω).Nonempty) {x : V} (hx : IsBoundaryState Ω x)
    (hne : x ∉ Ω.extremePoints ℝ) (G : Set (V ≃ᵃ[ℝ] V)) (hG : PreservesBody Ω G) :
    ¬ BoundaryTransitive Ω G :=
  fun hT => hne (extreme_of_isBoundaryState_of_transitive hc hconv hi hG hT hx)

end Purity

/-! ### §E — the invariant-inner-product ball -/

section QBall

variable {d : ℕ}

/-- The invariant quadratic form of `InvariantInnerProduct`: `Q(v) = v ⬝ᵥ (invMatrix Ω *ᵥ v)`. -/
noncomputable def qnorm (Ω : Set (Fin d → ℝ)) (v : Fin d → ℝ) : ℝ := v ⬝ᵥ (invMatrix Ω *ᵥ v)

/-- The closed `Q`-ball of radius `R` about the centroid. -/
def qBall (Ω : Set (Fin d → ℝ)) (R : ℝ) : Set (Fin d → ℝ) :=
  {x | qnorm Ω (x - centroid Ω) ≤ R ^ 2}

theorem mem_qBall {Ω : Set (Fin d → ℝ)} {R : ℝ} {x : Fin d → ℝ} :
    x ∈ qBall Ω R ↔ qnorm Ω (x - centroid Ω) ≤ R ^ 2 := Iff.rfl

theorem qnorm_smul (Ω : Set (Fin d → ℝ)) (t : ℝ) (v : Fin d → ℝ) :
    qnorm Ω (t • v) = t ^ 2 * qnorm Ω v := by
  unfold qnorm
  rw [Matrix.mulVec_smul, dotProduct_smul, smul_dotProduct, smul_eq_mul, smul_eq_mul]
  ring

theorem qnorm_zero (Ω : Set (Fin d → ℝ)) : qnorm Ω 0 = 0 := by
  unfold qnorm
  rw [Matrix.mulVec_zero, dotProduct_zero]

theorem qnorm_pos {Ω : Set (Fin d → ℝ)} (hc : IsCompact Ω) (hi : (interior Ω).Nonempty)
    {v : Fin d → ℝ} (hv : v ≠ 0) : 0 < qnorm Ω v :=
  invMatrix_pos hc hi hv

theorem qnorm_nonneg {Ω : Set (Fin d → ℝ)} (hc : IsCompact Ω) (hi : (interior Ω).Nonempty)
    (v : Fin d → ℝ) : 0 ≤ qnorm Ω v := by
  by_cases hv : v = 0
  · rw [hv, qnorm_zero]
  · exact (qnorm_pos hc hi hv).le

/-- `PreservesBody` in the image form that `InvariantInnerProduct` uses. -/
theorem image_eq_of_preservesBody {V : Type} [NormedAddCommGroup V] [NormedSpace ℝ V] {Ω : Set V}
    {G : Set (V ≃ᵃ[ℝ] V)} (hG : PreservesBody Ω G) {g : V ≃ᵃ[ℝ] V} (hg : g ∈ G) : g '' Ω = Ω := by
  ext y
  constructor
  · rintro ⟨x, hx, rfl⟩
    exact (hG g hg x hx).1
  · intro hy
    exact ⟨g.symm y, (hG g hg y hy).2, g.apply_symm_apply y⟩

/-- Every member of a body-preserving family fixes the centroid. -/
theorem centroid_fixed_of_preservesBody {Ω : Set (Fin d → ℝ)} (hc : IsCompact Ω)
    (hi : (interior Ω).Nonempty) {G : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ))} (hG : PreservesBody Ω G)
    {g : (Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ)} (hg : g ∈ G) : g (centroid Ω) = centroid Ω :=
  ((invariant_inner_product hc hi).2.2 g (image_eq_of_preservesBody hG hg)).1

/-- The invariant form of the displacement from the centroid is preserved by every member. -/
theorem qnorm_sub_centroid_apply {Ω : Set (Fin d → ℝ)} (hc : IsCompact Ω)
    (hi : (interior Ω).Nonempty) {G : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ))} (hG : PreservesBody Ω G)
    {g : (Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ)} (hg : g ∈ G) (x : Fin d → ℝ) :
    qnorm Ω (g x - centroid Ω) = qnorm Ω (x - centroid Ω) := by
  obtain ⟨hfix, hinv⟩ := (invariant_inner_product hc hi).2.2 g (image_eq_of_preservesBody hG hg)
  have h : g x - centroid Ω = linMatrix g *ᵥ (x - centroid Ω) := by
    conv_lhs => rw [← hfix]
    exact affine_sub_eq g x (centroid Ω)
  unfold qnorm
  rw [h]
  exact hinv _ _

/-- **Every boundary state lies on one `Q`-sphere about the centroid.** -/
theorem boundary_qnorm_const {Ω : Set (Fin d → ℝ)} (hc : IsCompact Ω) (hi : (interior Ω).Nonempty)
    {G : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ))} (hG : PreservesBody Ω G) (hT : BoundaryTransitive Ω G) :
    ∃ R : ℝ, 0 ≤ R ∧ ∀ x, IsBoundaryState Ω x → qnorm Ω (x - centroid Ω) = R ^ 2 := by
  by_cases h : ∃ x₀, IsBoundaryState Ω x₀
  · obtain ⟨x₀, hx₀⟩ := h
    refine ⟨Real.sqrt (qnorm Ω (x₀ - centroid Ω)), Real.sqrt_nonneg _, fun x hx => ?_⟩
    obtain ⟨g, hg, hgx⟩ := hT x₀ x hx₀ hx
    rw [Real.sq_sqrt (qnorm_nonneg hc hi _), ← hgx]
    exact qnorm_sub_centroid_apply hc hi hG hg x₀
  · exact ⟨0, le_rfl, fun x hx => absurd ⟨x, hx⟩ h⟩

/-- The centroid lies in the body: a point outside a closed convex body is separated from it by a
continuous linear functional, whose average over the body is its value at the centroid. -/
theorem centroid_mem {Ω : Set (Fin d → ℝ)} (hc : IsCompact Ω) (hconv : Convex ℝ Ω)
    (hi : (interior Ω).Nonempty) : centroid Ω ∈ Ω := by
  by_contra hnot
  obtain ⟨f, u, hfu, hu⟩ := geometric_hahn_banach_closed_point hconv hc.isClosed hnot
  have hpos : 0 < volume.real Ω := by
    obtain ⟨p, hp⟩ := hi
    have h1 : 0 < volume (interior Ω) := isOpen_interior.measure_pos volume ⟨p, hp⟩
    have h2 : 0 < volume Ω := h1.trans_le (measure_mono interior_subset)
    exact ENNReal.toReal_pos h2.ne' hc.measure_lt_top.ne
  set a : Fin d → ℝ := fun i => f (fun j => if i = j then 1 else 0) with ha
  have hf : ∀ x : Fin d → ℝ, f x = ∑ i, x i * a i := fun x => by
    have := LinearMap.pi_apply_eq_sum_univ (f : (Fin d → ℝ) →ₗ[ℝ] ℝ) x
    simpa [ha, smul_eq_mul] using this
  have hint : ∫ x in Ω, f x = ∑ i, (∫ x in Ω, x i) * a i := by
    simp_rw [hf]
    rw [integral_finsetSum]
    · exact Finset.sum_congr rfl fun i _ => integral_mul_const (a i) _
    · intro i _
      exact (integrableOn_coord hc i).mul_const (a i)
  have hcen : f (centroid Ω) = (volume.real Ω)⁻¹ * ∫ x in Ω, f x := by
    rw [hf, hint, Finset.mul_sum]
    refine Finset.sum_congr rfl fun i _ => ?_
    simp only [centroid]
    ring
  have hle : ∫ x in Ω, f x ≤ ∫ _x in Ω, u := by
    refine setIntegral_mono_on (f.continuous.continuousOn.integrableOn_compact hc)
      (continuous_const.continuousOn.integrableOn_compact hc) hc.measurableSet fun x hx => (hfu x hx).le
  rw [setIntegral_const, smul_eq_mul] at hle
  have : f (centroid Ω) ≤ u := by
    rw [hcen]
    calc (volume.real Ω)⁻¹ * ∫ x in Ω, f x ≤ (volume.real Ω)⁻¹ * ((volume Ω).toReal * u) :=
          mul_le_mul_of_nonneg_left hle (inv_nonneg.mpr hpos.le)
      _ = u := by
          rw [show (volume Ω).toReal = volume.real Ω from rfl, ← mul_assoc, inv_mul_cancel₀ hpos.ne',
            one_mul]
  exact absurd hu (not_lt.mpr this)

/-- Under a body-preserving boundary-transitive family, the centroid is an interior point: were it a
boundary state, every boundary state would equal it, while the ray lemma gives two distinct ones. -/
theorem centroid_mem_interior (hd : 0 < d) {Ω : Set (Fin d → ℝ)} (hc : IsCompact Ω)
    (hconv : Convex ℝ Ω) (hi : (interior Ω).Nonempty) {G : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ))}
    (hG : PreservesBody Ω G) (hT : BoundaryTransitive Ω G) : centroid Ω ∈ interior Ω := by
  by_contra hnot
  have hb : IsBoundaryState Ω (centroid Ω) :=
    isBoundaryState_of_frontier hconv hi (centroid_mem hc hconv hi) hnot
  have hall : ∀ y, IsBoundaryState Ω y → y = centroid Ω := fun y hy => by
    obtain ⟨g, hg, hgy⟩ := hT (centroid Ω) y hb hy
    rw [← hgy]
    exact centroid_fixed_of_preservesBody hc hi hG hg
  obtain ⟨p, hp⟩ := hi
  set e : Fin d → ℝ := Pi.single ⟨0, hd⟩ 1 with he
  have hu : e ≠ 0 := by
    intro h0
    have := congrFun h0 ⟨0, hd⟩
    simp [he] at this
  obtain ⟨t₁, ht₁, -, -, -, hb₁⟩ := exists_boundary_ray hc hconv hp hu
  obtain ⟨t₂, ht₂, -, -, -, hb₂⟩ := exists_boundary_ray hc hconv hp (neg_ne_zero.mpr hu)
  have h₁ := hall _ hb₁
  have h₂ := hall _ hb₂
  have hEq : p + t₁ • e = p + t₂ • (-e) := by rw [h₁, h₂]
  have : (t₁ + t₂) • e = 0 := by
    calc (t₁ + t₂) • e = (p + t₁ • e) - (p + t₂ • (-e)) := by module
      _ = 0 := sub_eq_zero.mpr hEq
  rcases smul_eq_zero.mp this with h | h
  · linarith
  · exact hu h

/-- **The body is the closed `Q`-ball about its centroid.** Only body preservation, all-boundary
transitivity and the invariant inner product enter; no composition closure. -/
theorem eq_qBall_of_boundaryTransitive (hd : 0 < d) {Ω : Set (Fin d → ℝ)} (hc : IsCompact Ω)
    (hconv : Convex ℝ Ω) (hi : (interior Ω).Nonempty) {G : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ))}
    (hG : PreservesBody Ω G) (hT : BoundaryTransitive Ω G) : ∃ R : ℝ, 0 < R ∧ Ω = qBall Ω R := by
  obtain ⟨R, hR0, hR⟩ := boundary_qnorm_const hc hi hG hT
  have hci := centroid_mem_interior hd hc hconv hi hG hT
  set c := centroid Ω with hcdef
  -- the ray from the centroid in any nonzero direction: its boundary state has `Q = R²`
  have ray : ∀ u : Fin d → ℝ, u ≠ 0 → ∃ t : ℝ, 0 < t ∧ c + t • u ∈ Ω ∧ (∀ s, t < s → c + s • u ∉ Ω) ∧
      (∀ s, 0 ≤ s → s ≤ t → c + s • u ∈ Ω) ∧ t ^ 2 * qnorm Ω u = R ^ 2 := by
    intro u hu
    obtain ⟨t, ht, hmem, hout, hseg, hb⟩ := exists_boundary_ray hc hconv hci hu
    refine ⟨t, ht, hmem, hout, hseg, ?_⟩
    have := hR _ hb
    rwa [add_sub_cancel_left, qnorm_smul] at this
  -- R is positive: the ray in a nonzero direction gives a boundary state away from the centroid
  have hRpos : 0 < R := by
    set e : Fin d → ℝ := Pi.single ⟨0, hd⟩ 1 with he
    have hu : e ≠ 0 := by
      intro h0
      have := congrFun h0 ⟨0, hd⟩
      simp [he] at this
    obtain ⟨t, ht, -, -, -, hQ⟩ := ray e hu
    have : 0 < R ^ 2 := by rw [← hQ]; exact mul_pos (by positivity) (qnorm_pos hc hi hu)
    exact lt_of_le_of_ne hR0 fun h0 => by rw [← h0] at this; simp at this
  refine ⟨R, hRpos, Set.ext fun x => ?_⟩
  rw [mem_qBall, ← hcdef]
  by_cases hxc : x = c
  · subst hxc
    simp only [sub_self, qnorm_zero]
    exact ⟨fun _ => by positivity, fun _ => interior_subset hci⟩
  · have hu : x - c ≠ 0 := sub_ne_zero.mpr hxc
    obtain ⟨t, ht, hmem, hout, hseg, hQ⟩ := ray (x - c) hu
    have hQpos := qnorm_pos hc hi hu
    constructor
    · intro hx
      -- `x = c + 1 • (x - c)` lies in the body, so `1 ≤ t`, and `Q(x - c) = R² / t² ≤ R²`
      have h1 : 1 ≤ t := by
        by_contra hlt
        exact hout 1 (not_le.mp hlt) (by simpa using hx)
      have : qnorm Ω (x - c) ≤ t ^ 2 * qnorm Ω (x - c) :=
        le_mul_of_one_le_left hQpos.le (one_le_pow₀ h1)
      linarith
    · intro hx
      by_contra hxΩ
      -- `x` outside the body forces `t < 1`, hence `R² = t² Q(x - c) < Q(x - c) ≤ R²`
      have hlt : t < 1 := by
        by_contra hge
        exact hxΩ (by simpa using hseg 1 zero_le_one (not_lt.mp hge))
      have h2 : t ^ 2 < 1 := pow_lt_one₀ ht.le hlt two_ne_zero
      have : t ^ 2 * qnorm Ω (x - c) < qnorm Ω (x - c) := mul_lt_of_lt_one_left hQpos h2
      linarith

end QBall

/-! ### §F — the normalization adapter and the coordinate Euclidean ball -/

section Normalization

variable {d : ℕ}

/-- The coordinate Euclidean ball of dimension `d` (the `d`-dimensional form of `ball3`). -/
def eball (d : ℕ) : Set (Fin d → ℝ) := {x | ∑ j, x j ^ 2 ≤ 1}

theorem mem_eball {x : Fin d → ℝ} : x ∈ eball d ↔ ∑ j, x j ^ 2 ≤ 1 := Iff.rfl

/-- The Finsupp double sum of `Matrix.PosDef` equals the dot-product form. -/
theorem finsuppSum_eq_dot (M : Matrix (Fin d) (Fin d) ℝ) (x : Fin d →₀ ℝ) :
    (x.sum fun i xi => x.sum fun j xj => star xi * M i j * xj) = (⇑x) ⬝ᵥ (M *ᵥ ⇑x) := by
  rw [Finsupp.sum_fintype _ _ (fun i => by simp), dotProduct]
  refine Finset.sum_congr rfl fun i _ => ?_
  rw [Finsupp.sum_fintype _ _ (fun j => by simp), mulVec_apply_eq, Finset.mul_sum]
  refine Finset.sum_congr rfl fun j _ => ?_
  rw [star_trivial]
  ring

/-- The invariant form's matrix is positive definite. -/
theorem invMatrix_posDef {Ω : Set (Fin d → ℝ)} (hc : IsCompact Ω) (hi : (interior Ω).Nonempty) :
    (invMatrix Ω).PosDef := by
  refine ⟨?_, fun x hx => ?_⟩
  · rw [Matrix.IsHermitian, Matrix.conjTranspose_eq_transpose_of_trivial, invMatrix_transpose]
  · rw [finsuppSum_eq_dot]
    exact invMatrix_pos hc hi fun h0 => hx (Finsupp.coe_eq_zero.mp h0)

/-- **Normalization adapter, matrix form.** `invMatrix Ω` factors as `Bᵀ * B`. -/
theorem exists_factor_invMatrix {Ω : Set (Fin d → ℝ)} (hc : IsCompact Ω)
    (hi : (interior Ω).Nonempty) : ∃ B : Matrix (Fin d) (Fin d) ℝ, Bᵀ * B = invMatrix Ω := by
  have hS : (invMatrix Ω).PosDef := invMatrix_posDef hc hi
  -- The LDL decomposition `S = L * diagonal D * Lᴴ`; its diagonal entries are positive.
  have hpos : ∀ i, 0 < LDL.diagEntries hS i := by
    intro i
    have hrow : LDL.lowerInv hS i ≠ 0 := by
      intro h0
      have hdet : (LDL.lowerInv hS).det = 0 :=
        Matrix.det_eq_zero_of_row_eq_zero i fun j => congrFun h0 j
      exact (Matrix.isUnit_det_of_invertible (LDL.lowerInv hS)).ne_zero hdet
    have hx : star (LDL.lowerInv hS i) ≠ 0 := by rwa [star_trivial]
    have h := hS.dotProduct_mulVec_pos hx
    rw [star_trivial, star_trivial] at h
    unfold LDL.diagEntries
    rw [EuclideanSpace.inner_toLp_toLp, star_trivial, star_trivial, dotProduct_comm]
    exact h
  set L := LDL.lower hS with hL
  set D := LDL.diagEntries hS with hD
  have hLDL : L * Matrix.diagonal D * Lᴴ = invMatrix Ω := by
    have := LDL.lower_conj_diag hS
    rwa [LDL.diag] at this
  set s : Fin d → ℝ := fun i => Real.sqrt (D i) with hs
  have hsq : Matrix.diagonal s * Matrix.diagonal s = Matrix.diagonal D := by
    rw [Matrix.diagonal_mul_diagonal]
    congr 1
    funext i
    exact Real.mul_self_sqrt (hpos i).le
  have hLt : (Lᴴ)ᵀ = L := by
    rw [Matrix.conjTranspose_eq_transpose_of_trivial, Matrix.transpose_transpose]
  refine ⟨Matrix.diagonal s * Lᴴ, ?_⟩
  calc (Matrix.diagonal s * Lᴴ)ᵀ * (Matrix.diagonal s * Lᴴ)
      = L * (Matrix.diagonal s * Matrix.diagonal s) * Lᴴ := by
        rw [Matrix.transpose_mul, Matrix.diagonal_transpose, hLt]
        simp only [Matrix.mul_assoc]
    _ = L * Matrix.diagonal D * Lᴴ := by rw [hsq]
    _ = invMatrix Ω := hLDL

/-- **Normalization adapter.** In suitable linear coordinates the invariant form is the sum of
squares: a linear automorphism `T` of the chart coordinates with `Q(v) = ∑ j, (T v) j ^ 2`. -/
theorem qnorm_eq_sum_sq {Ω : Set (Fin d → ℝ)} (hc : IsCompact Ω) (hi : (interior Ω).Nonempty) :
    ∃ T : (Fin d → ℝ) ≃ₗ[ℝ] (Fin d → ℝ), ∀ v, qnorm Ω v = ∑ j, (T v) j ^ 2 := by
  obtain ⟨B, hB⟩ := exists_factor_invMatrix hc hi
  have hq : ∀ v, qnorm Ω v = ∑ j, (B *ᵥ v) j ^ 2 := fun v => by
    unfold qnorm
    rw [← hB, ← Matrix.mulVec_mulVec, Matrix.dotProduct_mulVec, ← Matrix.mulVec_transpose,
      Matrix.transpose_transpose]
    simp only [dotProduct, pow_two]
  have hinj : Function.Injective (Matrix.toLin' B) := by
    intro v w hvw
    rw [Matrix.toLin'_apply, Matrix.toLin'_apply] at hvw
    by_contra hne
    have hpos := qnorm_pos hc hi (sub_ne_zero.mpr hne)
    rw [hq, Matrix.mulVec_sub, hvw, sub_self] at hpos
    simp at hpos
  refine ⟨LinearEquiv.ofInjectiveEndo (Matrix.toLin' B) hinj, fun v => ?_⟩
  rw [hq]
  rfl

/-- **The coordinate Euclidean ball.** A compact convex body with interior that is boundary transitive
under a body-preserving family is an affine image of the coordinate Euclidean ball of its dimension. -/
theorem exists_affine_image_eq_eball (hd : 0 < d) {Ω : Set (Fin d → ℝ)} (hc : IsCompact Ω)
    (hconv : Convex ℝ Ω) (hi : (interior Ω).Nonempty) {G : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ))}
    (hG : PreservesBody Ω G) (hT : BoundaryTransitive Ω G) :
    ∃ A : (Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ), A '' Ω = eball d := by
  obtain ⟨R, hR, hΩ⟩ := eq_qBall_of_boundaryTransitive hd hc hconv hi hG hT
  obtain ⟨T, hTq⟩ := qnorm_eq_sum_sq hc hi
  set c := centroid Ω with hcdef
  let S : (Fin d → ℝ) ≃ₗ[ℝ] (Fin d → ℝ) :=
    T.trans (LinearEquiv.smulOfNeZero ℝ (Fin d → ℝ) R⁻¹ (inv_ne_zero hR.ne'))
  let A : (Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ) := (AffineEquiv.vaddConst ℝ (-c)).trans S.toAffineEquiv
  have hA : ∀ x, A x = R⁻¹ • T (x - c) := fun x => by
    simp only [A, S, AffineEquiv.trans_apply, AffineEquiv.vaddConst_apply, vadd_eq_add,
      LinearEquiv.coe_toAffineEquiv, LinearEquiv.trans_apply, LinearEquiv.smulOfNeZero_apply]
    rw [sub_eq_add_neg]
  have hR' : R ≠ 0 := hR.ne'
  have key : ∀ z, qnorm Ω (z - c) = R ^ 2 * ∑ j, (A z) j ^ 2 := fun z => by
    rw [hTq, hA, Finset.mul_sum]
    refine Finset.sum_congr rfl fun j _ => ?_
    rw [Pi.smul_apply, smul_eq_mul]
    field_simp
  refine ⟨A, Set.ext fun y => ?_⟩
  constructor
  · rintro ⟨x, hx, rfl⟩
    have hx' : x ∈ qBall Ω R := by rw [← hΩ]; exact hx
    rw [mem_qBall, key] at hx'
    rw [mem_eball]
    exact le_of_mul_le_mul_left (hx'.trans_eq (mul_one _).symm) (by positivity)
  · intro hy
    refine ⟨A.symm y, ?_, A.apply_symm_apply y⟩
    rw [hΩ, mem_qBall, key, A.apply_symm_apply]
    exact mul_le_of_le_one_right (by positivity) hy

end Normalization

/-! ### §F′ — the completed-body and `TransBody` forms -/

section Corollaries

variable {D : DirectedStages} (C : CompletionChart D)

/-- The chart body of a completion chart is the closed `Q`-ball about its centroid whenever a
body-preserving family acts transitively on its boundary states. -/
theorem chartBody_eq_qBall (hd : 0 < C.d) {G : Set ((Fin C.d → ℝ) ≃ᵃ[ℝ] (Fin C.d → ℝ))}
    (hG : PreservesBody (chartBody C) G) (hT : BoundaryTransitive (chartBody C) G) :
    ∃ R : ℝ, 0 < R ∧ chartBody C = qBall (chartBody C) R :=
  eq_qBall_of_boundaryTransitive hd (chartBody_isCompact C) (chartBody_convex C)
    (chartBody_interior_nonempty C) hG hT

/-- The chart body is an affine image of the coordinate Euclidean ball of its dimension. -/
theorem chartBody_eq_eball (hd : 0 < C.d) {G : Set ((Fin C.d → ℝ) ≃ᵃ[ℝ] (Fin C.d → ℝ))}
    (hG : PreservesBody (chartBody C) G) (hT : BoundaryTransitive (chartBody C) G) :
    ∃ A : (Fin C.d → ℝ) ≃ᵃ[ℝ] (Fin C.d → ℝ), A '' chartBody C = eball C.d :=
  exists_affine_image_eq_eball hd (chartBody_isCompact C) (chartBody_convex C)
    (chartBody_interior_nonempty C) hG hT

variable {d : ℕ}

/-- The `TransBody` form: the architectural interface, strictly stronger than what the ball needs. -/
theorem eq_qBall_of_transBody (hd : 0 < d) {Ω : Set (Fin d → ℝ)} (hc : IsCompact Ω) (hconv : Convex ℝ Ω)
    (hi : (interior Ω).Nonempty) {G : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ))} (hT : TransBody Ω G) :
    ∃ R : ℝ, 0 < R ∧ Ω = qBall Ω R :=
  eq_qBall_of_boundaryTransitive hd hc hconv hi hT.1.preservesBody hT.2

theorem exists_affine_image_eq_eball_of_transBody (hd : 0 < d) {Ω : Set (Fin d → ℝ)} (hc : IsCompact Ω)
    (hconv : Convex ℝ Ω) (hi : (interior Ω).Nonempty) {G : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ))}
    (hT : TransBody Ω G) : ∃ A : (Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ), A '' Ω = eball d :=
  exists_affine_image_eq_eball hd hc hconv hi hT.1.preservesBody hT.2

/-- At `d = 3` the coordinate Euclidean ball is `KInfFoundations.ball3`. -/
theorem eball_three : eball 3 = ball3 := by
  ext x
  rw [mem_eball, mem_ball3, Fin.sum_univ_three]

end Corollaries

/-! ### §G — controls -/

section Controls

/-- All affine automorphisms of the ball form a body group. -/
theorem isBodyGroup_fullAut3 : IsBodyGroup ball3 fullAut3 where
  one_mem := refl_mem_fullAut3
  mul_mem g hg h hh x hx := by
    refine ⟨?_, ?_⟩
    · rw [AffineEquiv.trans_apply]
      exact (hh _ (hg x hx).1).1
    · show g.symm (h.symm x) ∈ ball3
      exact (hg _ (hh x hx).2).2
  inv_mem g hg x hx := ⟨(hg x hx).2, show g x ∈ ball3 from (hg x hx).1⟩
  preserves g hg x hx := (hg x hx).1

/-- **Control (TRANS holds): the ball with all its affine automorphisms.** -/
theorem transBody_fullAut3 : TransBody ball3 fullAut3 := ⟨isBodyGroup_fullAut3, boundaryTransitive_fullAut3⟩

/-- **Control (TRANS fails): the rotation flow alone is not boundary transitive.** -/
theorem not_transBody_flow : ¬ TransBody ball3 (Set.range rot3) := fun h => not_boundaryTransitive_flow h.2

/-- The Householder reflections of the ball, with the identity. -/
def refls3 : Set ((Fin 3 → ℝ) ≃ᵃ[ℝ] (Fin 3 → ℝ)) :=
  {g | ∃ (dv : Fin 3 → ℝ) (k : ℝ) (hk : (dv 0 ^ 2 + dv 1 ^ 2 + dv 2 ^ 2) * k = 1), g = hh3 dv k hk} ∪
    {AffineEquiv.refl ℝ (Fin 3 → ℝ)}

theorem preservesBody_refls3 : PreservesBody ball3 refls3 := by
  rintro g (⟨dv, k, hk, rfl⟩ | rfl)
  · exact hh3_mem_fullAut3 dv k hk
  · exact refl_mem_fullAut3

/-- **Control (boundary transitivity as a set property).** The reflections alone carry any boundary
state to any other; no group structure of the family is claimed. -/
theorem boundaryTransitive_refls3 : BoundaryTransitive ball3 refls3 := by
  intro u w hu hw
  have hu1 := sphere_of_isBoundaryState_ball3 hu
  have hw1 := sphere_of_isBoundaryState_ball3 hw
  by_cases huw : u = w
  · exact ⟨AffineEquiv.refl ℝ _, Or.inr rfl, by rw [AffineEquiv.refl_apply, huw]⟩
  · have hq : (u 0 - w 0) ^ 2 + (u 1 - w 1) ^ 2 + (u 2 - w 2) ^ 2 ≠ 0 := by
      intro h0
      apply huw
      have q0 := sq_nonneg (u 0 - w 0)
      have q1 := sq_nonneg (u 1 - w 1)
      have q2 := sq_nonneg (u 2 - w 2)
      have z0 : u 0 - w 0 = 0 := (pow_eq_zero_iff two_ne_zero).mp (by linarith)
      have z1 : u 1 - w 1 = 0 := (pow_eq_zero_iff two_ne_zero).mp (by linarith)
      have z2 : u 2 - w 2 = 0 := (pow_eq_zero_iff two_ne_zero).mp (by linarith)
      exact vec3_ext (by linarith) (by linarith) (by linarith)
    obtain ⟨k, hk⟩ : ∃ k : ℝ, ((u 0 - w 0) ^ 2 + (u 1 - w 1) ^ 2 + (u 2 - w 2) ^ 2) * k = 1 :=
      ⟨_, mul_inv_cancel₀ hq⟩
    refine ⟨hh3 (fun i => u i - w i) k hk, Or.inl ⟨_, _, hk, rfl⟩, ?_⟩
    rw [hh3_apply]
    exact hhFun_swap u w k hu1 hw1 hk

-- Composition closure of the reflection family is not claimed; the control records only that
-- boundary transitivity is a property a family can have without being a body group.

/-- The square: the kernel's `Metric.closedBall (0 : Fin 2 → ℝ) 1` in the sup norm. -/
def square2 : Set (Fin 2 → ℝ) := Metric.closedBall (0 : Fin 2 → ℝ) 1

theorem mem_square2 {x : Fin 2 → ℝ} : x ∈ square2 ↔ ∀ i, |x i| ≤ 1 := by
  rw [square2, Metric.mem_closedBall, dist_zero_right, pi_norm_le_iff_of_nonneg zero_le_one]
  simp only [Real.norm_eq_abs]

theorem edgeMid_mem_square2 : (![1, 0] : Fin 2 → ℝ) ∈ square2 := by
  rw [mem_square2]
  intro i
  fin_cases i <;> simp

/-- The midpoint of an edge of the square is a boundary state. -/
theorem isBoundaryState_square2_edgeMid : IsBoundaryState square2 ![1, 0] := by
  refine ⟨edgeMid_mem_square2, 0, by rw [mem_square2]; intro i; simp, fun ε hε h => ?_⟩
  rw [mem_square2] at h
  have := h 0
  simp only [sub_zero, Pi.add_apply, Pi.smul_apply, Matrix.cons_val_zero, smul_eq_mul, mul_one] at this
  rw [abs_of_pos (by linarith)] at this
  linarith

/-- The midpoint of an edge of the square is not an extreme point. -/
theorem edgeMid_not_extreme_square2 : (![1, 0] : Fin 2 → ℝ) ∉ square2.extremePoints ℝ := by
  intro hx
  have h1 : (![1, 1] : Fin 2 → ℝ) ∈ square2 := by rw [mem_square2]; intro i; fin_cases i <;> simp
  have h2 : (![1, -1] : Fin 2 → ℝ) ∈ square2 := by rw [mem_square2]; intro i; fin_cases i <;> simp
  have hseg : (![1, 0] : Fin 2 → ℝ) ∈ openSegment ℝ ![1, 1] ![1, -1] := by
    refine ⟨1 / 2, 1 / 2, by norm_num, by norm_num, by norm_num, ?_⟩
    funext i
    fin_cases i <;> simp <;> norm_num
  have h := hx.2 h1 h2 hseg
  have := congrFun h 1
  exact absurd (this : (1 : ℝ) = 0) one_ne_zero

/-- **Polytope control (the square).** No body-preserving family is boundary transitive on the
square: the edge midpoint is a boundary state that is not extreme. -/
theorem not_boundaryTransitive_square2 (G : Set ((Fin 2 → ℝ) ≃ᵃ[ℝ] (Fin 2 → ℝ)))
    (hG : PreservesBody square2 G) : ¬ BoundaryTransitive square2 G :=
  not_boundaryTransitive_of_nonextreme_boundary (isCompact_closedBall 0 1) (convex_closedBall 0 1)
    ⟨0, mem_interior_iff_mem_nhds.mpr (Metric.closedBall_mem_nhds 0 one_pos)⟩
    isBoundaryState_square2_edgeMid edgeMid_not_extreme_square2 G hG

/-- The octahedron `{|x₀| + |x₁| + |x₂| ≤ 1}`, the convex hull of the six vertices of Level 3A. -/
def oct3 : Set (Fin 3 → ℝ) := {x | |x 0| + |x 1| + |x 2| ≤ 1}

theorem mem_oct3 {x : Fin 3 → ℝ} : x ∈ oct3 ↔ |x 0| + |x 1| + |x 2| ≤ 1 := Iff.rfl

theorem oct3_convex : Convex ℝ oct3 := by
  intro x hx y hy a b ha hb hab
  rw [mem_oct3] at hx hy ⊢
  simp only [Pi.add_apply, Pi.smul_apply, smul_eq_mul]
  have e0 := abs_add_le (a * x 0) (b * y 0)
  have e1 := abs_add_le (a * x 1) (b * y 1)
  have e2 := abs_add_le (a * x 2) (b * y 2)
  rw [abs_mul, abs_mul, abs_of_nonneg ha, abs_of_nonneg hb] at e0 e1 e2
  nlinarith [abs_nonneg (x 0), abs_nonneg (x 1), abs_nonneg (x 2), abs_nonneg (y 0),
    abs_nonneg (y 1), abs_nonneg (y 2)]

theorem oct3_isClosed : IsClosed oct3 :=
  isClosed_le (by fun_prop) continuous_const

theorem oct3_subset_closedBall : oct3 ⊆ Metric.closedBall (0 : Fin 3 → ℝ) 1 := by
  intro x hx
  rw [mem_oct3] at hx
  rw [Metric.mem_closedBall, dist_zero_right, pi_norm_le_iff_of_nonneg zero_le_one]
  intro i
  rw [Real.norm_eq_abs]
  fin_cases i <;> simp <;> linarith [abs_nonneg (x 0), abs_nonneg (x 1), abs_nonneg (x 2)]

theorem oct3_isCompact : IsCompact oct3 :=
  Metric.isCompact_of_isClosed_isBounded oct3_isClosed
    (Metric.isBounded_closedBall.subset oct3_subset_closedBall)

theorem zero_mem_interior_oct3 : (0 : Fin 3 → ℝ) ∈ interior oct3 := by
  rw [mem_interior_iff_mem_nhds, Metric.mem_nhds_iff]
  refine ⟨1 / 3, by norm_num, fun x hx => ?_⟩
  rw [Metric.mem_ball, dist_zero_right] at hx
  rw [mem_oct3]
  have h0 := norm_le_pi_norm x 0
  have h1 := norm_le_pi_norm x 1
  have h2 := norm_le_pi_norm x 2
  rw [Real.norm_eq_abs] at h0 h1 h2
  linarith

theorem edgeMid_mem_oct3 : (![1 / 2, 1 / 2, 0] : Fin 3 → ℝ) ∈ oct3 := by
  show |(1 / 2 : ℝ)| + |(1 / 2 : ℝ)| + |(0 : ℝ)| ≤ 1
  norm_num

/-- The midpoint of an edge of the octahedron is a boundary state. -/
theorem isBoundaryState_oct3_edgeMid : IsBoundaryState oct3 ![1 / 2, 1 / 2, 0] := by
  refine ⟨edgeMid_mem_oct3, 0, by show |(0 : ℝ)| + |(0 : ℝ)| + |(0 : ℝ)| ≤ 1; norm_num,
    fun ε hε h => ?_⟩
  rw [mem_oct3] at h
  have e0 : (![1 / 2, 1 / 2, 0] + ε • (![1 / 2, 1 / 2, 0] - 0) : Fin 3 → ℝ) 0 =
      1 / 2 + ε * (1 / 2) := by
    show (1 / 2 : ℝ) + ε * (1 / 2 - 0) = 1 / 2 + ε * (1 / 2)
    ring
  have e1 : (![1 / 2, 1 / 2, 0] + ε • (![1 / 2, 1 / 2, 0] - 0) : Fin 3 → ℝ) 1 =
      1 / 2 + ε * (1 / 2) := by
    show (1 / 2 : ℝ) + ε * (1 / 2 - 0) = 1 / 2 + ε * (1 / 2)
    ring
  have e2 : (![1 / 2, 1 / 2, 0] + ε • (![1 / 2, 1 / 2, 0] - 0) : Fin 3 → ℝ) 2 = 0 := by
    show (0 : ℝ) + ε * (0 - 0) = 0
    ring
  rw [e0, e1, e2, abs_zero, abs_of_pos (by linarith)] at h
  linarith

/-- The midpoint of an edge of the octahedron is not an extreme point. -/
theorem edgeMid_not_extreme_oct3 : (![1 / 2, 1 / 2, 0] : Fin 3 → ℝ) ∉ oct3.extremePoints ℝ := by
  intro hx
  have h1 : (![1, 0, 0] : Fin 3 → ℝ) ∈ oct3 := by
    show |(1 : ℝ)| + |(0 : ℝ)| + |(0 : ℝ)| ≤ 1; norm_num
  have h2 : (![0, 1, 0] : Fin 3 → ℝ) ∈ oct3 := by
    show |(0 : ℝ)| + |(1 : ℝ)| + |(0 : ℝ)| ≤ 1; norm_num
  have hseg : (![1 / 2, 1 / 2, 0] : Fin 3 → ℝ) ∈ openSegment ℝ ![1, 0, 0] ![0, 1, 0] := by
    refine ⟨1 / 2, 1 / 2, by norm_num, by norm_num, by norm_num, ?_⟩
    exact vec3_ext (show (1 / 2 : ℝ) * 1 + 1 / 2 * 0 = 1 / 2 by norm_num)
      (show (1 / 2 : ℝ) * 0 + 1 / 2 * 1 = 1 / 2 by norm_num)
      (show (1 / 2 : ℝ) * 0 + 1 / 2 * 0 = 0 by norm_num)
  have h := hx.2 h1 h2 hseg
  have := congrFun h 1
  have h' : (0 : ℝ) = 1 / 2 := this
  norm_num at h'

/-- **Polytope control (the octahedron of Level 3A).** No body-preserving family is boundary
transitive on the octahedron: vertex transitivity is not all-boundary transitivity. -/
theorem not_boundaryTransitive_oct3 (G : Set ((Fin 3 → ℝ) ≃ᵃ[ℝ] (Fin 3 → ℝ)))
    (hG : PreservesBody oct3 G) : ¬ BoundaryTransitive oct3 G :=
  not_boundaryTransitive_of_nonextreme_boundary oct3_isCompact oct3_convex
    ⟨0, zero_mem_interior_oct3⟩ isBoundaryState_oct3_edgeMid edgeMid_not_extreme_oct3 G hG

end Controls

/-! ### The verdict -/

/-- Round TRB-1, together: the chart adapter, the two bridge directions, boundary purity, the
`Q`-ball, the normalization adapter, the Euclidean ball, and the controls. -/
theorem trb1_core :
    (∀ (D : DirectedStages) (C : CompletionChart D),
      IsCompact (chartBody C) ∧ Convex ℝ (chartBody C) ∧ (interior (chartBody C)).Nonempty) ∧
    (∀ (d : ℕ) (Ω : Set (Fin d → ℝ)) (x : Fin d → ℝ), IsBoundaryState Ω x → x ∈ frontier Ω) ∧
    (∀ (d : ℕ) (Ω : Set (Fin d → ℝ)), Convex ℝ Ω → (interior Ω).Nonempty →
      ∀ x, x ∈ Ω → x ∉ interior Ω → IsBoundaryState Ω x) ∧
    (∀ (d : ℕ), 0 < d → ∀ (Ω : Set (Fin d → ℝ)), IsCompact Ω → Convex ℝ Ω → (interior Ω).Nonempty →
      ∀ G : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ)), PreservesBody Ω G → BoundaryTransitive Ω G →
        ∃ R : ℝ, 0 < R ∧ Ω = qBall Ω R) ∧
    (∀ (d : ℕ), 0 < d → ∀ (Ω : Set (Fin d → ℝ)), IsCompact Ω → Convex ℝ Ω → (interior Ω).Nonempty →
      ∀ G : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ)), PreservesBody Ω G → BoundaryTransitive Ω G →
        ∃ A : (Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ), A '' Ω = eball d) ∧
    TransBody ball3 fullAut3 ∧ BoundaryTransitive ball3 refls3 ∧ ¬ TransBody ball3 (Set.range rot3) ∧
    (∀ G, PreservesBody square2 G → ¬ BoundaryTransitive square2 G) ∧
    (∀ G, PreservesBody oct3 G → ¬ BoundaryTransitive oct3 G) :=
  ⟨fun _ C => ⟨chartBody_isCompact C, chartBody_convex C, chartBody_interior_nonempty C⟩,
    fun _ _ _ hx => frontier_of_isBoundaryState hx,
    fun _ _ hconv hi _ hxΩ hx => isBoundaryState_of_frontier hconv hi hxΩ hx,
    fun _ hd _ hc hconv hi _ hG hT => eq_qBall_of_boundaryTransitive hd hc hconv hi hG hT,
    fun _ hd _ hc hconv hi _ hG hT => exists_affine_image_eq_eball hd hc hconv hi hG hT,
    transBody_fullAut3, boundaryTransitive_refls3, not_transBody_flow,
    not_boundaryTransitive_square2, not_boundaryTransitive_oct3⟩

end TransitiveBody
end OIBridge

#print axioms OIBridge.TransitiveBody.chartBody_isCompact
#print axioms OIBridge.TransitiveBody.chartBody_convex
#print axioms OIBridge.TransitiveBody.chartBody_interior_nonempty
#print axioms OIBridge.TransitiveBody.frontier_of_isBoundaryState
#print axioms OIBridge.TransitiveBody.isBoundaryState_of_frontier
#print axioms OIBridge.TransitiveBody.exists_boundary_ray
#print axioms OIBridge.TransitiveBody.extreme_of_isBoundaryState_of_transitive
#print axioms OIBridge.TransitiveBody.not_boundaryTransitive_of_nonextreme_boundary
#print axioms OIBridge.TransitiveBody.boundary_qnorm_const
#print axioms OIBridge.TransitiveBody.centroid_mem
#print axioms OIBridge.TransitiveBody.centroid_mem_interior
#print axioms OIBridge.TransitiveBody.eq_qBall_of_boundaryTransitive
#print axioms OIBridge.TransitiveBody.exists_factor_invMatrix
#print axioms OIBridge.TransitiveBody.qnorm_eq_sum_sq
#print axioms OIBridge.TransitiveBody.exists_affine_image_eq_eball
#print axioms OIBridge.TransitiveBody.chartBody_eq_qBall
#print axioms OIBridge.TransitiveBody.chartBody_eq_eball
#print axioms OIBridge.TransitiveBody.eq_qBall_of_transBody
#print axioms OIBridge.TransitiveBody.exists_affine_image_eq_eball_of_transBody
#print axioms OIBridge.TransitiveBody.eball_three
#print axioms OIBridge.TransitiveBody.transBody_fullAut3
#print axioms OIBridge.TransitiveBody.boundaryTransitive_refls3
#print axioms OIBridge.TransitiveBody.not_transBody_flow
#print axioms OIBridge.TransitiveBody.not_boundaryTransitive_square2
#print axioms OIBridge.TransitiveBody.not_boundaryTransitive_oct3
#print axioms OIBridge.TransitiveBody.trb1_core
