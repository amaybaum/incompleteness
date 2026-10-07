/-
  OIBridge/DenseOrbit.lean — round KTRANS-DENSE-1: the ball, cone and selector consumers of
  K∞-Trans under a dense boundary orbit in place of exact boundary transitivity.

  `DenseBoundaryOrbit Ω G`: for any two boundary states `x`, `y` of `Ω`, the state `y` lies in the
  closure of the orbit `{g x : g ∈ G}`. Boundary transitivity implies it
  (`denseBoundaryOrbit_of_boundaryTransitive`).

  (A) The ball. TRB-1 reads boundary transitivity in two places: the invariant form of the
  displacement from the centroid is constant on the boundary, and the centroid is interior. Both
  hold under a dense boundary orbit, because the invariant form is continuous and the centroid's
  orbit is a point (`boundary_qnorm_const_of_dense`, `centroid_mem_interior_of_dense`). Hence a
  compact convex body with interior is the closed invariant-form ball about its centroid and an
  affine image of `eball d` (`eq_qBall_of_dense`, `exists_affine_image_eq_eball_of_dense`,
  `chartBody_eq_eball_of_dense`).

  (B) The cone. EFF-1 reads boundary transitivity only to make every sharp effect available. Under a
  dense boundary orbit the available sharp directions are dense in the sphere, and the pairing of a
  joint vector with two sharp effects is continuous in the two directions, so the available family
  still determines `maxCone (eball d)` (`maxConeOf_avail_eq_of_dense`). K1-BRIDGE-1 reads boundary
  transitivity only through that cone equality, so its transports and relative selectors follow
  (`nativeGate_of_avail_dense`, `entangling_of_avail_dense`, `dim_of_nativeGateOf_dense`,
  `three_of_nativeGateOf_dense`), as does the relative selector with `2 ≤ d`
  (`three_of_nativeGateOf_of_two_le_dense`).

  (C) Strictness. Boundary transitivity implies a dense boundary orbit
  (`denseBoundaryOrbit_of_boundaryTransitive`). The identity with the reflections in hyperplanes
  orthogonal to rational vectors is a countable body-preserving family with a dense boundary orbit
  on `eball d`
  (`denseBoundaryOrbit_ratRefl`); at `d = 3` it is not boundary transitive
  (`not_boundaryTransitive_ratRefl`, through EFF-1's countable no-go), and its seed orbit, a
  countable family of tests, determines `maxCone (eball 3)` (`countable_seedOrbit_cone`).

  Not covered: statements that need a specific effect to exist exactly keep exact boundary
  transitivity (EFF-1's availability of every sharp effect and of the full effect set, OG-1's
  supporting-effect completeness and seed-orbit identification), as do OG-1's Lorentz-cone bridge
  (`lorentz_of_seedOrbit`, `lorentz_of_available`) and TRB-1's boundary purity
  (`extreme_of_isBoundaryState_of_transitive`). The rational reflections are a control, not a
  family of operations. Nothing here sources a dense boundary orbit or any other hypothesis.
-/
import OIBridge.K2Guard

namespace OIBridge
namespace DenseOrbit

open Set Topology Matrix KInfFoundations OrbitGeneration OrbitNormalization StageCompletion
  CompletionAction InvariantInnerProduct TransitiveBody CompositeDimension CompositeInterface
open EffectSpace K1Bridge K2Guard

/-! ### §A — the dense boundary orbit -/

/-- Every boundary state lies in the closure of the orbit of every boundary state. -/
def DenseBoundaryOrbit {V : Type} [NormedAddCommGroup V] [NormedSpace ℝ V] (Ω : Set V)
    (G : Set (V ≃ᵃ[ℝ] V)) : Prop :=
  ∀ x y, IsBoundaryState Ω x → IsBoundaryState Ω y → y ∈ closure ((fun g : V ≃ᵃ[ℝ] V => g x) '' G)

theorem denseBoundaryOrbit_of_boundaryTransitive {V : Type} [NormedAddCommGroup V] [NormedSpace ℝ V]
    {Ω : Set V} {G : Set (V ≃ᵃ[ℝ] V)} (hT : BoundaryTransitive Ω G) : DenseBoundaryOrbit Ω G := by
  intro x y hx hy
  obtain ⟨g, hg, hgx⟩ := hT x y hx hy
  exact subset_closure ⟨g, hg, hgx⟩

/-! ### §B — the ball under a dense boundary orbit -/

section Ball

variable {d : ℕ}

theorem continuous_qnorm_sub (Ω : Set (Fin d → ℝ)) (c : Fin d → ℝ) :
    Continuous fun z : Fin d → ℝ => qnorm Ω (z - c) := by
  unfold qnorm
  exact (continuous_id.sub continuous_const).dotProduct
    (continuous_const.matrix_mulVec (continuous_id.sub continuous_const))

/-- **Every boundary state lies on one invariant-form sphere about the centroid.** -/
theorem boundary_qnorm_const_of_dense {Ω : Set (Fin d → ℝ)} (hc : IsCompact Ω)
    (hi : (interior Ω).Nonempty) {G : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ))}
    (hG : PreservesBody Ω G) (hT : DenseBoundaryOrbit Ω G) :
    ∃ R : ℝ, 0 ≤ R ∧ ∀ x, IsBoundaryState Ω x → qnorm Ω (x - centroid Ω) = R ^ 2 := by
  by_cases h : ∃ x₀, IsBoundaryState Ω x₀
  · obtain ⟨x₀, hx₀⟩ := h
    refine ⟨Real.sqrt (qnorm Ω (x₀ - centroid Ω)), Real.sqrt_nonneg _, fun x hx => ?_⟩
    rw [Real.sq_sqrt (qnorm_nonneg hc hi _)]
    have hclosed : IsClosed {z : Fin d → ℝ | qnorm Ω (z - centroid Ω) = qnorm Ω (x₀ - centroid Ω)} :=
      isClosed_eq (continuous_qnorm_sub Ω _) continuous_const
    have hsub : (fun g : (Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ) => g x₀) '' G ⊆
        {z : Fin d → ℝ | qnorm Ω (z - centroid Ω) = qnorm Ω (x₀ - centroid Ω)} := by
      rintro _ ⟨g, hg, rfl⟩
      exact qnorm_sub_centroid_apply hc hi hG hg x₀
    exact hclosed.closure_subset_iff.mpr hsub (hT x₀ x hx₀ hx)
  · exact ⟨0, le_rfl, fun x hx => absurd ⟨x, hx⟩ h⟩

/-- Under a body-preserving family with a dense boundary orbit, the centroid is interior. -/
theorem centroid_mem_interior_of_dense (hd : 0 < d) {Ω : Set (Fin d → ℝ)} (hc : IsCompact Ω)
    (hconv : Convex ℝ Ω) (hi : (interior Ω).Nonempty) {G : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ))}
    (hG : PreservesBody Ω G) (hT : DenseBoundaryOrbit Ω G) : centroid Ω ∈ interior Ω := by
  by_contra hnot
  have hb : IsBoundaryState Ω (centroid Ω) :=
    isBoundaryState_of_frontier hconv hi (centroid_mem hc hconv hi) hnot
  have hall : ∀ y, IsBoundaryState Ω y → y = centroid Ω := fun y hy => by
    have hsub : (fun g : (Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ) => g (centroid Ω)) '' G ⊆ {centroid Ω} := by
      rintro _ ⟨g, hg, rfl⟩
      exact centroid_fixed_of_preservesBody hc hi hG hg
    have hy' := closure_mono hsub (hT (centroid Ω) y hb hy)
    rwa [closure_singleton, Set.mem_singleton_iff] at hy'
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

/-- **The body is the closed invariant-form ball about its centroid** under a dense boundary orbit. -/
theorem eq_qBall_of_dense (hd : 0 < d) {Ω : Set (Fin d → ℝ)} (hc : IsCompact Ω)
    (hconv : Convex ℝ Ω) (hi : (interior Ω).Nonempty) {G : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ))}
    (hG : PreservesBody Ω G) (hT : DenseBoundaryOrbit Ω G) : ∃ R : ℝ, 0 < R ∧ Ω = qBall Ω R := by
  obtain ⟨R, hR0, hR⟩ := boundary_qnorm_const_of_dense hc hi hG hT
  have hci := centroid_mem_interior_of_dense hd hc hconv hi hG hT
  set c := centroid Ω with hcdef
  have ray : ∀ u : Fin d → ℝ, u ≠ 0 → ∃ t : ℝ, 0 < t ∧ c + t • u ∈ Ω ∧ (∀ s, t < s → c + s • u ∉ Ω) ∧
      (∀ s, 0 ≤ s → s ≤ t → c + s • u ∈ Ω) ∧ t ^ 2 * qnorm Ω u = R ^ 2 := by
    intro u hu
    obtain ⟨t, ht, hmem, hout, hseg, hb⟩ := exists_boundary_ray hc hconv hci hu
    refine ⟨t, ht, hmem, hout, hseg, ?_⟩
    have := hR _ hb
    rwa [add_sub_cancel_left, qnorm_smul] at this
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
      have h1 : 1 ≤ t := by
        by_contra hlt
        exact hout 1 (not_le.mp hlt) (by simpa using hx)
      have : qnorm Ω (x - c) ≤ t ^ 2 * qnorm Ω (x - c) :=
        le_mul_of_one_le_left hQpos.le (one_le_pow₀ h1)
      linarith
    · intro hx
      by_contra hxΩ
      have hlt : t < 1 := by
        by_contra hge
        exact hxΩ (by simpa using hseg 1 zero_le_one (not_lt.mp hge))
      have h2 : t ^ 2 < 1 := pow_lt_one₀ ht.le hlt two_ne_zero
      have : t ^ 2 * qnorm Ω (x - c) < qnorm Ω (x - c) := mul_lt_of_lt_one_left hQpos h2
      linarith

/-- **The coordinate Euclidean ball** under a dense boundary orbit. -/
theorem exists_affine_image_eq_eball_of_dense (hd : 0 < d) {Ω : Set (Fin d → ℝ)} (hc : IsCompact Ω)
    (hconv : Convex ℝ Ω) (hi : (interior Ω).Nonempty) {G : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ))}
    (hG : PreservesBody Ω G) (hT : DenseBoundaryOrbit Ω G) :
    ∃ A : (Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ), A '' Ω = eball d := by
  obtain ⟨R, hR, hΩ⟩ := eq_qBall_of_dense hd hc hconv hi hG hT
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

end Ball

/-- The chart body of a completion chart is an affine image of `eball` under a dense boundary orbit. -/
theorem chartBody_eq_eball_of_dense {D : DirectedStages} (C : CompletionChart D) (hd : 0 < C.d)
    {G : Set ((Fin C.d → ℝ) ≃ᵃ[ℝ] (Fin C.d → ℝ))}
    (hG : PreservesBody (chartBody C) G) (hT : DenseBoundaryOrbit (chartBody C) G) :
    ∃ A : (Fin C.d → ℝ) ≃ᵃ[ℝ] (Fin C.d → ℝ), A '' chartBody C = eball C.d :=
  exists_affine_image_eq_eball_of_dense hd (chartBody_isCompact C) (chartBody_convex C)
    (chartBody_interior_nonempty C) hG hT

/-! ### §C — the product-test cone under a dense boundary orbit -/

section Cone

variable {d : ℕ}

theorem continuous_sharpVec_apply (μ : Fin (d + 1)) :
    Continuous fun x : Fin d → ℝ => sharpVec x μ := by
  induction μ using Fin.cases with
  | zero =>
    simp only [sharpVec_zero]
    exact continuous_const
  | succ j =>
    simp only [sharpVec_succ]
    exact (continuous_apply j).div_const 2

theorem continuous_pairVal_sharp (ω : W d) :
    Continuous fun p : (Fin d → ℝ) × (Fin d → ℝ) => pairVal (sharpVec p.1) (sharpVec p.2) ω := by
  unfold pairVal
  refine continuous_finsetSum _ fun μ _ => continuous_finsetSum _ fun ν _ => ?_
  exact (((continuous_sharpVec_apply μ).comp continuous_fst).mul continuous_const).mul
    ((continuous_sharpVec_apply ν).comp continuous_snd)

variable {G : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ))} {r : (Fin d → ℝ) →ᵃ[ℝ] ℝ}
  {avail : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ)}

/-- **The available family determines DIM-1's maximal cone** under a dense boundary orbit. -/
theorem maxConeOf_avail_eq_of_dense (hd : 0 < d) (hG : PreservesBody (eball d) G)
    (hP1 : SharpSeed (eball d) r) (hK : DenseBoundaryOrbit (eball d) G)
    (hV4 : SeedOrbitAvailable G r avail) (hE : EffectsOn (eball d) avail) :
    maxConeOf avail = maxCone (eball d) := by
  refine Set.Subset.antisymm ?_ ?_
  · intro ω hω
    apply maxConeOf_sharp_subset_maxCone hd
    obtain ⟨he, ⟨u, hu, h1⟩, ⟨w, hw, h0⟩⟩ := hP1
    have hbu : IsBoundaryState (eball d) u :=
      sharpSeed_certain_isBoundaryState ⟨he, ⟨u, hu, h1⟩, ⟨w, hw, h0⟩⟩ hu h1
    have htr : ∀ g ∈ G, seedTransport r g = sharpEff (g u) := fun g hg => by
      have ht := isEffectOn_seedTransport he fun x hx => (hG g hg x hx).2
      exact (sharp_eq_of_certain ht (hG g hg u hu).1 (hG g hg w hw).1
        (by rw [seedTransport_apply_apply, h1]) (by rw [seedTransport_apply_apply, h0])).2
    have hav : ∀ g ∈ G, sharpEff (g u) ∈ avail := fun g hg => by
      rw [← htr g hg]
      exact hV4 g hg
    have hS : IsClosed {p : (Fin d → ℝ) × (Fin d → ℝ) | 0 ≤ pairVal (sharpVec p.1) (sharpVec p.2) ω} :=
      isClosed_le continuous_const (continuous_pairVal_sharp ω)
    have hsub : ((fun g : (Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ) => g u) '' G) ×ˢ
        ((fun g : (Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ) => g u) '' G) ⊆
        {p : (Fin d → ℝ) × (Fin d → ℝ) | 0 ≤ pairVal (sharpVec p.1) (sharpVec p.2) ω} := by
      rintro ⟨_, _⟩ ⟨⟨g, hg, rfl⟩, ⟨g', hg', rfl⟩⟩
      have h := hω _ (hav g hg) _ (hav g' hg')
      rw [prodEffVal_sharp] at h
      show 0 ≤ pairVal (sharpVec (g u)) (sharpVec (g' u)) ω
      exact h
    show ∀ e ∈ sharpFamily d, ∀ f ∈ sharpFamily d, 0 ≤ prodEffVal e f ω
    rintro e ⟨x, hx, rfl⟩ f ⟨y, hy, rfl⟩
    have hxy : (x, y) ∈ closure (((fun g : (Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ) => g u) '' G) ×ˢ
        ((fun g : (Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ) => g u) '' G)) := by
      rw [closure_prod_eq]
      exact ⟨hK u x hbu (isBoundaryState_eball_of_sphere hx),
        hK u y hbu (isBoundaryState_eball_of_sphere hy)⟩
    have hmem := hS.closure_subset_iff.mpr hsub hxy
    rw [prodEffVal_sharp]
    exact hmem
  · rw [← maxConeOf_fullEffects]
    exact maxConeOf_anti fun e he => hE e he

/-- K1-BRIDGE-1's native-gate transport under a dense boundary orbit. -/
theorem nativeGate_of_avail_dense (hd : 0 < d) (hE : EffectsOn (eball d) avail)
    (hG : PreservesBody (eball d) G) (hP1 : SharpSeed (eball d) r)
    (hK : DenseBoundaryOrbit (eball d) G) (hV4 : SeedOrbitAvailable G r avail)
    {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {T : W d ≃ₗ[ℝ] W d}
    (hT : NativeGateOf (eball d) avail z N T) : NativeGate (eball d) z N T :=
  nativeGate_of_cone_eq (maxConeOf_avail_eq_of_dense hd hG hP1 hK hV4 hE) hT

/-- K1-BRIDGE-1's entangling transport under a dense boundary orbit. -/
theorem entangling_of_avail_dense (hd : 0 < d) (hE : EffectsOn (eball d) avail)
    (hG : PreservesBody (eball d) G) (hP1 : SharpSeed (eball d) r)
    (hK : DenseBoundaryOrbit (eball d) G) (hV4 : SeedOrbitAvailable G r avail)
    {T : W d ≃ₗ[ℝ] W d} (hEnt : EntanglingOf (eball d) avail T) : Entangling (eball d) T :=
  entangling_of_cone_eq (maxConeOf_avail_eq_of_dense hd hG hP1 hK hV4 hE) hEnt

/-- **The dimension, relative to the available family,** under a dense boundary orbit. -/
theorem dim_of_nativeGateOf_dense (hd : 0 < d) (hE : EffectsOn (eball d) avail)
    (hG : PreservesBody (eball d) G) (hP1 : SharpSeed (eball d) r)
    (hK : DenseBoundaryOrbit (eball d) G) (hV4 : SeedOrbitAvailable G r avail)
    {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {T : W d ≃ₗ[ℝ] W d}
    (hN : IsNot (eball d) z N) (hT : NativeGateOf (eball d) avail z N T) : d = 1 ∨ d = 3 :=
  dim_of_nativeGate hN (nativeGate_of_avail_dense hd hE hG hP1 hK hV4 hT)

/-- **Three, relative to the available family,** under a dense boundary orbit. -/
theorem three_of_nativeGateOf_dense (hd : 0 < d) (hE : EffectsOn (eball d) avail)
    (hG : PreservesBody (eball d) G) (hP1 : SharpSeed (eball d) r)
    (hK : DenseBoundaryOrbit (eball d) G) (hV4 : SeedOrbitAvailable G r avail)
    {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {T : W d ≃ₗ[ℝ] W d}
    (hN : IsNot (eball d) z N) (hT : NativeGateOf (eball d) avail z N T)
    (hEnt : EntanglingOf (eball d) avail T) : d = 3 :=
  three_of_nativeGate hN (nativeGate_of_avail_dense hd hE hG hP1 hK hV4 hT)
    (entangling_of_avail_dense hd hE hG hP1 hK hV4 hEnt)

/-- **The relative selector with `2 ≤ d`** under a dense boundary orbit. -/
theorem three_of_nativeGateOf_of_two_le_dense (hd : 2 ≤ d) (hE : EffectsOn (eball d) avail)
    (hG : PreservesBody (eball d) G) (hP1 : SharpSeed (eball d) r)
    (hK : DenseBoundaryOrbit (eball d) G) (hV4 : SeedOrbitAvailable G r avail)
    {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {T : W d ≃ₗ[ℝ] W d}
    (hN : IsNot (eball d) z N) (hT : NativeGateOf (eball d) avail z N T) : d = 3 :=
  three_of_nativeGate_of_two_le hd hN
    (nativeGate_of_cone_eq (maxConeOf_avail_eq_of_dense (by omega) hG hP1 hK hV4 hE) hT)

end Cone

/-! ### §D — strictness: a countable family with a dense boundary orbit -/

section Strict

variable {d : ℕ}

theorem exists_rat_near (m : Fin d → ℝ) {δ : ℝ} (hδ : 0 < δ) :
    ∃ q : Fin d → ℚ, dist (fun j => (q j : ℝ)) m < δ := by
  have h : ∀ j, ∃ s : ℚ, m j < s ∧ (s : ℝ) < m j + δ := fun j => exists_rat_btwn (by linarith)
  choose q hq using h
  refine ⟨q, (dist_pi_lt_iff hδ).2 fun j => ?_⟩
  rw [Real.dist_eq, abs_lt]
  constructor <;> linarith [(hq j).1, (hq j).2]

/-- The identity and the reflections in hyperplanes orthogonal to nonzero rational vectors. -/
noncomputable def ratRefl (d : ℕ) : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ)) :=
  insert (AffineEquiv.refl ℝ (Fin d → ℝ))
    (Set.range fun q : {q : Fin d → ℚ // ∑ j, ((q j : ℝ)) ^ 2 ≠ 0} =>
      @reflAff d (fun j => (q.1 j : ℝ)) q.2)

theorem countable_ratRefl : (ratRefl d).Countable :=
  (Set.countable_range _).insert _

theorem ratRefl_subset_fullAut : ratRefl d ⊆ fullAut d := by
  rintro g (rfl | ⟨q, rfl⟩)
  · exact refl_mem_fullAut
  · exact reflAff_mem_fullAut q.2

theorem preservesBody_ratRefl : PreservesBody (eball d) (ratRefl d) := fun g hg =>
  preservesBody_fullAut g (ratRefl_subset_fullAut hg)

/-- **The rational reflections have a dense boundary orbit** on `eball d`. -/
theorem denseBoundaryOrbit_ratRefl : DenseBoundaryOrbit (eball d) (ratRefl d) := by
  intro u v hu hv
  have hu1 := sphere_of_isBoundaryState_eball hu
  have hv1 := sphere_of_isBoundaryState_eball hv
  by_cases huv : u = v
  · exact subset_closure ⟨AffineEquiv.refl ℝ (Fin d → ℝ), Set.mem_insert _ _, by rw [huv]; rfl⟩
  · have hm0 : ∑ j, (u - v) j ^ 2 ≠ 0 := by
      intro h0
      apply huv
      funext j
      have hj := (Finset.sum_eq_zero_iff_of_nonneg (fun j _ => sq_nonneg ((u - v) j))).1 h0 j
        (Finset.mem_univ j)
      have := pow_eq_zero_iff (n := 2) (by norm_num) |>.1 hj
      rw [Pi.sub_apply] at this
      linarith
    have hF : reflLin (u - v) u = v := reflLin_swap hu1 hv1 hm0
    have hs2 : Continuous fun m : Fin d → ℝ => ∑ j, m j ^ 2 :=
      continuous_finsetSum _ fun j _ => (continuous_apply j).pow 2
    have hc : ContinuousAt (fun m : Fin d → ℝ => reflLin m u) (u - v) := by
      show ContinuousAt (fun m : Fin d → ℝ => u - (2 * (∑ j, u j * m j) / ∑ j, m j ^ 2) • m) (u - v)
      have hs1 : Continuous fun m : Fin d → ℝ => ∑ j, u j * m j :=
        continuous_finsetSum _ fun j _ => continuous_const.mul (continuous_apply j)
      exact continuousAt_const.sub
        (((continuous_const.mul hs1).continuousAt.div hs2.continuousAt hm0).smul continuousAt_id)
    rw [Metric.mem_closure_iff]
    intro ε hε
    have h1 : ∀ᶠ m in 𝓝 (u - v), ∑ j, m j ^ 2 ≠ 0 := hs2.continuousAt.eventually_ne hm0
    have h2 : ∀ᶠ m in 𝓝 (u - v), dist (reflLin m u) v < ε := by
      have := hc.eventually (Metric.ball_mem_nhds (reflLin (u - v) u) hε)
      rw [hF] at this
      exact this
    obtain ⟨δ, hδ, hball⟩ := Metric.eventually_nhds_iff.mp (h1.and h2)
    obtain ⟨q, hq⟩ := exists_rat_near (u - v) hδ
    obtain ⟨hqne, hqd⟩ := hball hq
    refine ⟨reflAff hqne u, ⟨reflAff hqne, Set.mem_insert_of_mem _ ⟨⟨q, hqne⟩, rfl⟩, rfl⟩, ?_⟩
    rw [reflAff_apply, dist_comm]
    exact hqd

/-- At `d = 3` the rational reflections are not boundary transitive. -/
theorem not_boundaryTransitive_ratRefl : ¬ BoundaryTransitive (eball 3) (ratRefl 3) :=
  not_boundaryTransitive_of_countable countable_ratRefl

/-- **A countable family of tests determines the product-test cone.** The seed orbit of the axis
test under the rational reflections is countable and determines `maxCone (eball 3)`. -/
theorem countable_seedOrbit_cone :
    (seedOrbit (ratRefl 3) (sharpEff (axisVec (by norm_num : 0 < 3)))).Countable ∧
      maxConeOf (seedOrbit (ratRefl 3) (sharpEff (axisVec (by norm_num : 0 < 3)))) =
        maxCone (eball 3) := by
  have hseed := sharpEff_sharpSeed (axisVec_sq (by norm_num : 0 < 3))
  refine ⟨?_, maxConeOf_avail_eq_of_dense (by norm_num) preservesBody_ratRefl hseed
    denseBoundaryOrbit_ratRefl (seedOrbitAvailable_self _ _) ?_⟩
  · refine (countable_ratRefl.image fun g => seedTransport (sharpEff (axisVec (by norm_num : 0 < 3))) g).mono ?_
    rintro f ⟨g, hg, rfl⟩
    exact ⟨g, hg, rfl⟩
  · rintro f ⟨g, hg, rfl⟩
    exact isEffectOn_seedTransport hseed.1 fun x hx => (preservesBody_ratRefl g hg x hx).2

end Strict

end DenseOrbit
end OIBridge

#print axioms OIBridge.DenseOrbit.denseBoundaryOrbit_of_boundaryTransitive
#print axioms OIBridge.DenseOrbit.boundary_qnorm_const_of_dense
#print axioms OIBridge.DenseOrbit.centroid_mem_interior_of_dense
#print axioms OIBridge.DenseOrbit.eq_qBall_of_dense
#print axioms OIBridge.DenseOrbit.exists_affine_image_eq_eball_of_dense
#print axioms OIBridge.DenseOrbit.chartBody_eq_eball_of_dense
#print axioms OIBridge.DenseOrbit.maxConeOf_avail_eq_of_dense
#print axioms OIBridge.DenseOrbit.nativeGate_of_avail_dense
#print axioms OIBridge.DenseOrbit.entangling_of_avail_dense
#print axioms OIBridge.DenseOrbit.dim_of_nativeGateOf_dense
#print axioms OIBridge.DenseOrbit.three_of_nativeGateOf_dense
#print axioms OIBridge.DenseOrbit.three_of_nativeGateOf_of_two_le_dense
#print axioms OIBridge.DenseOrbit.denseBoundaryOrbit_ratRefl
#print axioms OIBridge.DenseOrbit.not_boundaryTransitive_ratRefl
#print axioms OIBridge.DenseOrbit.countable_seedOrbit_cone
