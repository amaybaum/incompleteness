/-
  OIBridge/RelcSelectBlock.lean — DIM-1's block reduction and selector without the target relation.

  `CtrlGate` is `CompositeDimension.NativeGate` without its field `relT`: the frame, two-sided
  positivity and the control relation `relC`. Over it this module restates the block reduction of
  `CompositeDimension` §Q and the selector.

  Proved here:
    §A  `CtrlGate`, and `ctrlGate_of_nativeGate`;
    §B  the §Q lemmas from `gate_corner` to `Phi_lift_z_eq_zero` that the block reduction reads,
        restated over `CtrlGate` with the landed proofs (suffix `_ctrl`); the three §Q lemmas that read
        `relT` (`gate_actT`, `Mfwd_homMap`, `Minv_homMap`) are not restated;
    §C  the replacement for the single `relT` step of `blockData_of_orthonormal`: on a tangent control
        slice `c` the joint vector `G (lift c ⊗ Minv (hom 0))` is fixed by the target action of `N`
        (`actT_slice_ctrl`). Route: for a unit `u` in the `−1` eigenspace of the homogenized NOT, the
        functional `a ↦ pairVal a (hom 0 − u) (G (hom c ⊗ Minv (hom 0 − u)))` is nonnegative on the
        cone, equals `a ↦ a·hom z − 2 Φ(a; u, hom 0)`, and vanishes at `hom (−z)`; the tangent
        argument (`tangent_vanish`) then gives `Φ(a; u, hom 0) = 0` for every control effect, so each
        row is orthogonal to the `−1` eigenspace and is fixed by the self-adjoint involution;
    §D  `blockData_of_ctrlGate`, and the selector `dim_of_ctrlGate` (`d = 1 ∨ d = 3`) with parity
        from `finrank_plus_eq_finrank_minus_relC`; `three_of_ctrlGate` under the entangling clause.

  The declarations of §B and §D other than the new lemmas of §C carry the landed proofs of
  `CompositeDimension` with declaration names renamed and `NativeGate` replaced by `CtrlGate`; the
  two further edits are the `rw` line of `blockData_of_orthonormal` that read `gate_actT` and
  `Minv_homMap`, and the parity line of `dim_of_nativeGate`.
-/
import OIBridge.RelcSelectParity
import OIBridge.ParityNot

namespace OIBridge
namespace RelcSelect

open KInfFoundations TransitiveBody NativeGateBall CompositeDimension EffectSpace ParityNot

variable {d : ℕ}

/-! ### §A — the hypotheses without the target relation -/

/-- `NativeGate` without the target relation `relT`. -/
structure CtrlGate (Ω : Set (Fin d → ℝ)) (z : Fin d → ℝ) (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ))
    (G : W d ≃ₗ[ℝ] W d) : Prop where
  frame : ∀ a b : Fin 2,
    G (prodState (corner z a) (corner z b)) = prodState (corner z a) (corner z (a + b))
  posFwd : ∀ x ∈ Ω, ∀ y ∈ Ω, G (prodState x y) ∈ maxCone Ω
  posInv : ∀ x ∈ Ω, ∀ y ∈ Ω, G.symm (prodState x y) ∈ maxCone Ω
  relC : ∀ ω, actC N (G (actC N ω)) = actT N (G ω)

theorem ctrlGate_of_nativeGate {Ω : Set (Fin d → ℝ)} {z : Fin d → ℝ}
    {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d} (hG : NativeGate Ω z N G) :
    CtrlGate Ω z N G :=
  ⟨hG.frame, hG.posFwd, hG.posInv, hG.relC⟩

/-! ### §B — the block-reduction lemmas over `CtrlGate` (landed proofs) -/

-- @@COPY gate_corner

-- @@COPY gate_corner_symm

-- @@COPY Mfwd_Minv

-- @@COPY lor_Minv

-- @@COPY gate_actC

/-- Rc on the corner `−z` slice: the target map there is `N M₀`. -/
-- @@COPY gate_corner_neg

/-- The normalized gate `G (I ⊗ M₀⁻¹)` on the corner `z` slice is the identity. -/
-- @@COPY gt_corner

/-- The normalized gate on the corner `−z` slice is `I ⊗ N`. -/
-- @@COPY gt_corner_neg

/-- The normalized gate on the centre slice fixes every `+1` eigenvector of the target. -/
-- @@COPY gt_center

/-- On a tangent control slice the normalized gate's control output is orthogonal to both
corners, for cone-valued target data. -/
-- @@COPY gt_tangent_corners

/-- The sphere identity at the corner `z`. -/
-- @@COPY gt_sphere

/-- The sphere identity at the corner `−z`, evaluated at the two corner target states. -/
-- @@COPY gt_sphere_corner

/-- The two sphere identities in block form. -/
-- @@COPY Phi_sphere

/-- The centre value of the block form vanishes. -/
-- @@COPY Phi_center

/-- The centre value vanishes for every control effect. -/
-- @@COPY Phi_center_all

/-- The block form against the unit control effect vanishes identically. -/
-- @@COPY Phi_hom_zero_eq_zero

/-- The block form against the lifted corner axis vanishes identically. -/
-- @@COPY Phi_lift_z_eq_zero

/-! ### §C — the tangent slice is fixed by the target action, without `relT` -/

/-- The normalized gate on the centre slice for an arbitrary target vector: twice its value is
`hom z ⊗ t + hom (−z) ⊗ N t`. -/
theorem gt_center_two_ctrl {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}
    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hG : CtrlGate (eball d) z N G) (t : HVec d) :
    (2 : ℝ) • G (tens (hom 0) (Minv z G t)) = tens (hom z) t + tens (hom (-z)) (homMap N t) := by
  rw [← map_smul, ← tens_smul_left 2 (hom 0) (Minv z G t), ← hom_add_hom_neg z, tens_add_left,
    map_add, gt_corner_ctrl hN hG, gt_corner_neg_ctrl hN hG]

/-- **The tangent argument on the `−1` eigenspace.** For a unit `u` of head zero in the `−1`
eigenspace of the homogenized NOT, the block form `Φ(·; u, hom 0)` of the tangent slice `c`
vanishes on every lifted control tangent direction `c'`. -/
theorem phi_lift_minus_ctrl {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}
    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hG : CtrlGate (eball d) z N G)
    {c : Fin d → ℝ} (hc : ∑ j, c j ^ 2 ≤ 1) (hzc : ∑ j, z j * c j = 0) {u : HVec d}
    (hu0 : u 0 = 0) (hu : ∑ μ, u μ ^ 2 = 1) (hNu : homMap N u = -u) {c' : Fin d → ℝ}
    (hc' : ∑ j, c' j ^ 2 ≤ 1) (hzc' : ∑ j, z j * c' j = 0) :
    Phi z G (lift c') c u (hom 0) = 0 := by
  -- the target vector `hom 0 − u` is the boundary cone vector `hom (−τ)`
  have hτ : ∑ j, Matrix.vecTail u j ^ 2 = 1 := by
    rw [Fin.sum_univ_succ, hu0, zero_pow two_ne_zero, zero_add] at hu
    exact hu
  have hτ' : ∑ j, (-Matrix.vecTail u) j ^ 2 = 1 := by simpa [neg_sq] using hτ
  have hfdef : hom 0 - u = hom (-Matrix.vecTail u) := by
    rw [hom_eq_add_lift (-Matrix.vecTail u), lift_neg, lift_vecTail hu0, sub_eq_add_neg]
  have hfL : Lor (hom 0 - u) := by
    rw [hfdef]
    exact lor_hom_of_unit hτ'
  have hHf : homMap N (hom 0 - u) = hom 0 + u := by
    rw [map_sub, homMap_hom, map_zero, hNu, sub_neg_eq_add]
  -- the dot products of the target data
  have hh0u : ∑ ν, hom (0 : Fin d → ℝ) ν * u ν = 0 := by
    rw [Fin.sum_univ_succ, hom_zero, one_mul, hu0]; simp [hom_succ]
  have huu : ∑ ν, u ν * u ν = 1 := by
    rw [← hu]
    exact Finset.sum_congr rfl fun ν _ => (sq _).symm
  have hS1 : ∑ ν, (hom (0 : Fin d → ℝ) - u) ν * (hom 0 - u) ν = 2 := by
    have e : ∀ ν, (hom (0 : Fin d → ℝ) - u) ν * (hom 0 - u) ν
        = hom (0 : Fin d → ℝ) ν * hom 0 ν - 2 * (hom (0 : Fin d → ℝ) ν * u ν) + u ν * u ν :=
      fun ν => by rw [Pi.sub_apply]; ring
    rw [Finset.sum_congr rfl fun ν _ => e ν, Finset.sum_add_distrib, Finset.sum_sub_distrib,
      ← Finset.mul_sum, dot_hom_hom_zero, hh0u, huu]
    norm_num
  have hS2 : ∑ ν, (hom (0 : Fin d → ℝ) + u) ν * (hom 0 - u) ν = 0 := by
    have e : ∀ ν, (hom (0 : Fin d → ℝ) + u) ν * (hom 0 - u) ν
        = hom (0 : Fin d → ℝ) ν * hom 0 ν - u ν * u ν :=
      fun ν => by rw [Pi.add_apply, Pi.sub_apply]; ring
    rw [Finset.sum_congr rfl fun ν _ => e ν, Finset.sum_sub_distrib, dot_hom_hom_zero, huu,
      sub_self]
  -- the centre slice reads the corner `z`
  have hcen : ∀ a : HVec d, pairVal a (hom 0 - u) (G (tens (hom 0) (Minv z G (hom 0 - u))))
      = ∑ μ, a μ * hom z μ := by
    intro a
    have h2 := congrArg (pairVal a (hom 0 - u)) (gt_center_two_ctrl hN hG (hom 0 - u))
    rw [pairVal_smul_omega, pairVal_add_omega, pairVal_tens, pairVal_tens, hHf, hS1, hS2] at h2
    linarith
  -- the positive functional of the control effect at the control input `hom c`
  have hcL : Lor (hom c) := lor_hom (mem_eball.mpr hc)
  have hpos : ∀ x ∈ eball d, ∀ y ∈ eball d,
      (G : W d →ₗ[ℝ] W d) (prodState x y) ∈ maxCone (eball d) :=
    fun x hx y hy => hG.posFwd x hx y hy
  let F : HVec d →ₗ[ℝ] ℝ := pvLeft (hom 0 - u) (G (tens (hom c) (Minv z G (hom 0 - u))))
  have hF : ∀ X, F X = pairVal X (hom 0 - u) (G (tens (hom c) (Minv z G (hom 0 - u)))) :=
    fun X => rfl
  have hFpos : ∀ X, Lor X → 0 ≤ F X := fun X hX => by
    rw [hF]
    exact gate_pairVal_nonneg hpos hX hcL hfL (lor_Minv_ctrl hN hG hfL)
  have hsplit : ∀ X, F X = ∑ μ, X μ * hom z μ + Phi z G X c (hom 0 - u) (hom 0 - u) := by
    intro X
    rw [hF, hom_eq_add_lift c, tens_add_left, map_add, pairVal_add_omega, hcen, Phi_apply]
  -- on the cone, `Φ(a; hom 0 − u, hom 0 − u) = −2 Φ(a; u, hom 0)`; by linearity, everywhere
  have hext : ∀ X, Phi z G X c (hom 0 - u) (hom 0 - u) = -2 * Phi z G X c u (hom 0) := by
    have hL := linearMap_eq_zero_of_lor
      (pvLeft (hom 0 - u) (G (tens (lift c) (Minv z G (hom 0 - u))))
        + (2 : ℝ) • pvLeft u (G (tens (lift c) (Minv z G (hom 0)))))
      (fun a ha => by
        rw [LinearMap.add_apply, LinearMap.smul_apply, pvLeft_apply, pvLeft_apply, smul_eq_mul]
        change Phi z G a c (hom 0 - u) (hom 0 - u) + 2 * Phi z G a c u (hom 0) = 0
        have hs := Phi_sphere_ctrl hN hG hc hzc ha hu0 hu
        have h00 := Phi_center_ctrl hN hG hc hzc ha
        simp only [map_sub, LinearMap.sub_apply]
        linarith [hs.1, hs.2])
    intro X
    have hX := LinearMap.congr_fun hL X
    rw [LinearMap.add_apply, LinearMap.smul_apply, pvLeft_apply, pvLeft_apply, smul_eq_mul,
      LinearMap.zero_apply] at hX
    change Phi z G X c (hom 0 - u) (hom 0 - u) + 2 * Phi z G X c u (hom 0) = 0 at hX
    linarith
  -- the functional vanishes at the antipodal corner
  have h0 : F (hom (-z)) = 0 := by
    rw [hsplit, dot_hom_neg_hom hN.unit, zero_add, Phi_apply]
    exact (gt_tangent_corners_ctrl hN hG hc hzc hfL hfL).1
  have hz' : ∑ j, (-z) j ^ 2 = 1 := by simpa [neg_sq] using hN.unit
  have hzc'' : ∑ j, (-z) j * c' j = 0 := by
    simp only [Pi.neg_apply, neg_mul, Finset.sum_neg_distrib, hzc', neg_zero]
  have hT := tangent_vanish F hFpos hz' hc' hzc'' h0
  rw [hsplit, hext] at hT
  have hlz : ∑ μ, lift c' μ * hom z μ = 0 := by
    rw [Fin.sum_univ_succ, lift_zero, zero_mul, zero_add]
    simp only [lift_succ, hom_succ]
    calc ∑ j, c' j * z j = ∑ j, z j * c' j := Finset.sum_congr rfl fun j _ => mul_comm _ _
      _ = 0 := hzc'
  linarith [hT, hlz]

/-- For a unit `u` of head zero in the `−1` eigenspace, `Φ(a; u, hom 0)` vanishes at every basis
control effect. -/
theorem phi_bvec_minus_unit_ctrl {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}
    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hG : CtrlGate (eball d) z N G)
    {c : Fin d → ℝ} (hc : ∑ j, c j ^ 2 ≤ 1) (hzc : ∑ j, z j * c j = 0) {u : HVec d}
    (hu0 : u 0 = 0) (hu : ∑ μ, u μ ^ 2 = 1) (hNu : homMap N u = -u) (μ : Fin (d + 1)) :
    Phi z G (bvec μ) c u (hom 0) = 0 := by
  have hz := hN.unit
  refine Fin.cases ?_ (fun k => ?_) μ
  · rw [bvec_zero_eq]
    exact Phi_hom_zero_eq_zero_ctrl hN hG hc hzc u (hom 0)
  · have hk := phi_lift_minus_ctrl hN hG hc hzc hu0 hu hNu (tperp_le_one hz k) (tperp_dot_z hz k)
    have hlz := Phi_lift_z_eq_zero_ctrl hN hG hc hzc u (hom 0)
    rw [Phi_apply, lift_tperp, pairVal_sub_left, pairVal_smul_left] at hk
    rw [Phi_apply] at hlz
    rw [hlz, mul_zero, sub_zero] at hk
    rw [Phi_apply]
    exact hk

/-- **No `−1` component.** For every `w` in the `−1` eigenspace of the homogenized NOT,
`Φ(bvec μ; w, hom 0) = 0` on a tangent control slice. -/
theorem phi_minusSpace_ctrl {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}
    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hG : CtrlGate (eball d) z N G)
    {c : Fin d → ℝ} (hc : ∑ j, c j ^ 2 ≤ 1) (hzc : ∑ j, z j * c j = 0) {w : HVec d}
    (hw : w ∈ minusSpace N) (μ : Fin (d + 1)) :
    Phi z G (bvec μ) c w (hom 0) = 0 := by
  have hw0 : w 0 = 0 := by
    have h := congrFun (mem_minusSpace.mp hw) 0
    rw [homMap_zero, Pi.neg_apply] at h
    linarith
  have hs0 : 0 ≤ ∑ ν, w ν ^ 2 := Finset.sum_nonneg fun j _ => sq_nonneg _
  rcases eq_or_lt_of_le hs0 with h0 | hpos
  · have hwz : w = 0 := by
      funext j
      have := (Finset.sum_eq_zero_iff_of_nonneg (fun j _ => sq_nonneg (w j))).1 h0.symm j
        (Finset.mem_univ _)
      exact (pow_eq_zero_iff two_ne_zero).mp this
    rw [hwz, map_zero, LinearMap.zero_apply]
  · have hsq : Real.sqrt (∑ ν, w ν ^ 2) ^ 2 = ∑ ν, w ν ^ 2 := Real.sq_sqrt hs0
    have hsqpos : 0 < Real.sqrt (∑ ν, w ν ^ 2) := Real.sqrt_pos.2 hpos
    set s : ℝ := 1 / Real.sqrt (∑ ν, w ν ^ 2) with hs
    have hspos : 0 < s := by rw [hs]; exact div_pos one_pos hsqpos
    have hs2 : s ^ 2 * ∑ ν, w ν ^ 2 = 1 := by
      rw [hs, div_pow, one_pow, hsq]
      exact one_div_mul_cancel (ne_of_gt hpos)
    have hu : ∑ ν, (s • w) ν ^ 2 = 1 := by rw [sumsq_smul, hs2]
    have hu0 : (s • w) 0 = 0 := by rw [Pi.smul_apply, hw0, smul_zero]
    have hNu : homMap N (s • w) = -(s • w) := by rw [map_smul, mem_minusSpace.mp hw, smul_neg]
    have h := phi_bvec_minus_unit_ctrl hN hG hc hzc hu0 hu hNu μ
    rw [map_smul, LinearMap.smul_apply, smul_eq_mul] at h
    exact (mul_eq_zero.mp h).resolve_left hspos.ne'

/-- A vector orthogonal to the `−1` eigenspace of the homogenized NOT is fixed by it. -/
theorem homMap_eq_self_of_orth_minusSpace {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}
    (hN : IsNot (eball d) z N) {v : HVec d} (h : ∀ w ∈ minusSpace N, ∑ ν, v ν * w ν = 0) :
    homMap N v = v := by
  have hwm : v - homMap N v ∈ minusSpace N := by
    rw [mem_minusSpace, map_sub, homMap_homMap hN.invol, neg_sub]
  have h1 := h _ hwm
  have h2 : ∑ ν, homMap N v ν * (v - homMap N v) ν = 0 := by
    rw [homMap_dot hN v (v - homMap N v), mem_minusSpace.mp hwm]
    have e : ∑ ν, v ν * (-(v - homMap N v)) ν = -∑ ν, v ν * (v - homMap N v) ν := by
      rw [← Finset.sum_neg_distrib]
      exact Finset.sum_congr rfl fun ν _ => by rw [Pi.neg_apply]; ring
    rw [e, h1, neg_zero]
  have h3 : ∑ ν, (v - homMap N v) ν * (v - homMap N v) ν = 0 := by
    have e : ∀ ν, (v - homMap N v) ν * (v - homMap N v) ν
        = v ν * (v - homMap N v) ν - homMap N v ν * (v - homMap N v) ν :=
      fun ν => by rw [Pi.sub_apply]; ring
    rw [Finset.sum_congr rfl fun ν _ => e ν, Finset.sum_sub_distrib, h1, h2, sub_zero]
  have hw0 : v - homMap N v = 0 := by
    funext ν
    have := (Finset.sum_eq_zero_iff_of_nonneg
      (fun j _ => mul_self_nonneg ((v - homMap N v) j))).1 h3 ν (Finset.mem_univ _)
    exact mul_self_eq_zero.mp this
  exact (sub_eq_zero.mp hw0).symm

/-- **The replacement for the target relation in the block reduction.** On a tangent control slice
`c`, the image of the centre target is fixed by the target action of the NOT. This is the fact
`blockData_of_orthonormal` derives from `relT`; here it follows from the frame, two-sided
positivity and `relC`. -/
theorem actT_slice_ctrl {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}
    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hG : CtrlGate (eball d) z N G)
    {c : Fin d → ℝ} (hc : ∑ j, c j ^ 2 ≤ 1) (hzc : ∑ j, z j * c j = 0) :
    actT N (G (tens (lift c) (Minv z G (hom 0)))) = G (tens (lift c) (Minv z G (hom 0))) := by
  funext μ
  show homMap N (G (tens (lift c) (Minv z G (hom 0))) μ) = G (tens (lift c) (Minv z G (hom 0))) μ
  apply homMap_eq_self_of_orth_minusSpace hN
  intro w hw
  have h := phi_minusSpace_ctrl hN hG hc hzc hw μ
  rwa [Phi_apply, pairVal_bvec] at h

/-! ### §D — the block reduction and the selector over `CtrlGate` -/

/-- **The assembly (S2 and S4)**, over `CtrlGate`. -/
-- @@COPY blockData_of_orthonormal

/-- **The block reduction (S1, S2, S4)** without the target relation. -/
-- @@COPY blockData_of_nativeGate

/-- No gate of two intervals with the frame is entangling. -/
-- @@COPY not_entangling_one

/-- **The selector without the target relation.** Two identical copies of the Euclidean ball with
a gate satisfying the frame, two-sided positivity and the control relation have dimension one or
three. -/
-- @@COPY dim_of_nativeGate

/-- **The selector under the entangling clause, without the target relation.** -/
-- @@COPY three_of_nativeGate

end RelcSelect
end OIBridge

#print axioms OIBridge.RelcSelect.ctrlGate_of_nativeGate
#print axioms OIBridge.RelcSelect.actT_slice_ctrl
#print axioms OIBridge.RelcSelect.blockData_of_ctrlGate
#print axioms OIBridge.RelcSelect.dim_of_ctrlGate
#print axioms OIBridge.RelcSelect.three_of_ctrlGate
