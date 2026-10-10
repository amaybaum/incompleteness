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

theorem gate_corner_ctrl {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}
    (hN : IsNot (eball d) z N) (hG : CtrlGate (eball d) z N G) (Y : HVec d) :
    G (tens (hom z) Y) = tens (hom z) (Mfwd z G Y) :=
  corner_form hN.unit
    (fun b => by
      have h := hG.frame 0 b
      rw [corner_zero, zero_add] at h
      exact h)
    (fun x hx y hy => hG.posFwd x hx y hy) Y

theorem gate_corner_symm_ctrl {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}
    (hN : IsNot (eball d) z N) (hG : CtrlGate (eball d) z N G) (Y : HVec d) :
    G.symm (tens (hom z) Y) = tens (hom z) (Minv z G Y) :=
  corner_form hN.unit
    (fun b => by
      have h := hG.frame 0 b
      rw [corner_zero, zero_add] at h
      calc G.symm (prodState z (corner z b)) = G.symm (G (prodState z (corner z b))) := by rw [h]
        _ = prodState z (corner z b) := G.symm_apply_apply _)
    (fun x hx y hy => hG.posInv x hx y hy) Y

theorem Mfwd_Minv_ctrl {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}
    (hN : IsNot (eball d) z N) (hG : CtrlGate (eball d) z N G) (Y : HVec d) :
    Mfwd z G (Minv z G Y) = Y := by
  apply tens_hom_inj (x := z)
  rw [← gate_corner_ctrl hN hG, ← gate_corner_symm_ctrl hN hG, G.apply_symm_apply]

theorem lor_Minv_ctrl {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}
    (hN : IsNot (eball d) z N) (hG : CtrlGate (eball d) z N G) {Y : HVec d} (hY : Lor Y) :
    Lor (Minv z G Y) :=
  lor_cornerMap hN.unit (fun x hx y hy => hG.posInv x hx y hy) hY

theorem gate_actC_ctrl {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}
    (hN : IsNot (eball d) z N) (hG : CtrlGate (eball d) z N G) (ω : W d) :
    G (actC N ω) = actC N (actT N (G ω)) := by
  have h2 := congrArg (actC N) (hG.relC ω)
  rwa [actC_actC hN.invol] at h2

/-- Rc on the corner `−z` slice: the target map there is `N M₀`. -/
theorem gate_corner_neg_ctrl {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}
    (hN : IsNot (eball d) z N) (hG : CtrlGate (eball d) z N G) (Y : HVec d) :
    G (tens (hom (-z)) Y) = tens (hom (-z)) (homMap N (Mfwd z G Y)) := by
  have hz' : homMap N (hom z) = hom (-z) := by rw [homMap_hom, hN.flips]
  rw [← hz', ← actC_tens N (hom z) Y, gate_actC_ctrl hN hG (tens (hom z) Y), gate_corner_ctrl hN hG Y,
    actT_tens N (hom z) (Mfwd z G Y), actC_tens N (hom z) (homMap N (Mfwd z G Y))]

/-- The normalized gate `G (I ⊗ M₀⁻¹)` on the corner `z` slice is the identity. -/
theorem gt_corner_ctrl {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}
    (hN : IsNot (eball d) z N) (hG : CtrlGate (eball d) z N G) (t : HVec d) :
    G (tens (hom z) (Minv z G t)) = tens (hom z) t := by
  rw [gate_corner_ctrl hN hG, Mfwd_Minv_ctrl hN hG]

/-- The normalized gate on the corner `−z` slice is `I ⊗ N`. -/
theorem gt_corner_neg_ctrl {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}
    (hN : IsNot (eball d) z N) (hG : CtrlGate (eball d) z N G) (t : HVec d) :
    G (tens (hom (-z)) (Minv z G t)) = tens (hom (-z)) (homMap N t) := by
  rw [gate_corner_neg_ctrl hN hG, Mfwd_Minv_ctrl hN hG]

/-- The normalized gate on the centre slice fixes every `+1` eigenvector of the target. -/
theorem gt_center_ctrl {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}
    (hN : IsNot (eball d) z N) (hG : CtrlGate (eball d) z N G) {t : HVec d}
    (ht : homMap N t = t) : G (tens (hom 0) (Minv z G t)) = tens (hom 0) t := by
  apply eq_of_two_smul_eq
  rw [← map_smul, ← tens_smul_left 2 (hom 0) (Minv z G t), ← hom_add_hom_neg z, tens_add_left,
    map_add, gt_corner_ctrl hN hG,
    gt_corner_neg_ctrl hN hG, ht, ← tens_add_left, hom_add_hom_neg z, tens_smul_left]

/-- On a tangent control slice the normalized gate's control output is orthogonal to both
corners, for cone-valued target data. -/
theorem gt_tangent_corners_ctrl {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}
    (hN : IsNot (eball d) z N) (hG : CtrlGate (eball d) z N G) {c : Fin d → ℝ}
    (hc : ∑ j, c j ^ 2 ≤ 1) (hzc : ∑ j, z j * c j = 0) {f t : HVec d} (hf : Lor f) (ht : Lor t) :
    pairVal (hom (-z)) f (G (tens (lift c) (Minv z G t))) = 0 ∧
    pairVal (hom z) f (G (tens (lift c) (Minv z G t))) = 0 := by
  have hzl : Lor (hom z) := lor_hom_of_unit hN.unit
  have hz' : ∑ j, (-z) j ^ 2 = 1 := by simpa [neg_sq] using hN.unit
  have hzc' : ∑ j, (-z) j * c j = 0 := by
    simp only [Pi.neg_apply, neg_mul, Finset.sum_neg_distrib, hzc, neg_zero]
  have hzl' : Lor (hom (-z)) := lor_hom_of_unit hz'
  have hMt : Lor (Minv z G t) := lor_Minv_ctrl hN hG ht
  have hpos : ∀ x ∈ eball d, ∀ y ∈ eball d,
      (G : W d →ₗ[ℝ] W d) (prodState x y) ∈ maxCone (eball d) :=
    fun x hx y hy => hG.posFwd x hx y hy
  constructor
  · let F : HVec d →ₗ[ℝ] ℝ := pvOmega (hom (-z)) f ∘ₗ (G : W d →ₗ[ℝ] W d) ∘ₗ tensR (Minv z G t)
    have hF : ∀ X, F X = pairVal (hom (-z)) f (G (tens X (Minv z G t))) := fun X => rfl
    have hFpos : ∀ X, Lor X → 0 ≤ F X := fun X hX => by
      rw [hF]; exact gate_pairVal_nonneg hpos hzl' hX hf hMt
    have h0 : F (hom z) = 0 := by
      rw [hF, gt_corner_ctrl hN hG, pairVal_tens, dot_hom_neg_hom hN.unit, zero_mul]
    rw [← hF]
    exact tangent_vanish F hFpos hN.unit hc hzc h0
  · let F : HVec d →ₗ[ℝ] ℝ := pvOmega (hom z) f ∘ₗ (G : W d →ₗ[ℝ] W d) ∘ₗ tensR (Minv z G t)
    have hF : ∀ X, F X = pairVal (hom z) f (G (tens X (Minv z G t))) := fun X => rfl
    have hFpos : ∀ X, Lor X → 0 ≤ F X := fun X hX => by
      rw [hF]; exact gate_pairVal_nonneg hpos hzl hX hf hMt
    have h0 : F (hom (-z)) = 0 := by
      rw [hF, gt_corner_neg_ctrl hN hG, pairVal_tens, dot_hom_hom_neg hN.unit, zero_mul]
    rw [← hF]
    exact tangent_vanish F hFpos hz' hc hzc' h0

/-- The sphere identity at the corner `z`. -/
theorem gt_sphere_ctrl {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}
    (hN : IsNot (eball d) z N) (hG : CtrlGate (eball d) z N G) {c : Fin d → ℝ}
    (hc : ∑ j, c j ^ 2 ≤ 1) (hzc : ∑ j, z j * c j = 0) {a : HVec d} (ha : Lor a) {u : HVec d}
    (hu0 : u 0 = 0) (hu : ∑ μ, u μ ^ 2 = 1) :
    pairVal a (hom 0 - u) (G (tens (lift c) (Minv z G (hom 0 + u)))) = 0 := by
  have hτ : ∑ j, Matrix.vecTail u j ^ 2 = 1 := by
    rw [Fin.sum_univ_succ, hu0, zero_pow two_ne_zero, zero_add] at hu
    exact hu
  have hτ' : ∑ j, (-Matrix.vecTail u) j ^ 2 = 1 := by simpa [neg_sq] using hτ
  have h1 : hom 0 + u = hom (Matrix.vecTail u) := by
    rw [hom_eq_add_lift (Matrix.vecTail u), lift_vecTail hu0]
  have h2 : hom 0 - u = hom (-Matrix.vecTail u) := by
    rw [hom_eq_add_lift (-Matrix.vecTail u), lift_neg, lift_vecTail hu0, sub_eq_add_neg]
  rw [h1, h2]
  have hpos : ∀ x ∈ eball d, ∀ y ∈ eball d,
      (G : W d →ₗ[ℝ] W d) (prodState x y) ∈ maxCone (eball d) :=
    fun x hx y hy => hG.posFwd x hx y hy
  let F : HVec d →ₗ[ℝ] ℝ := pvOmega a (hom (-Matrix.vecTail u)) ∘ₗ (G : W d →ₗ[ℝ] W d) ∘ₗ
    tensR (Minv z G (hom (Matrix.vecTail u)))
  have hF : ∀ X, F X = pairVal a (hom (-Matrix.vecTail u))
      (G (tens X (Minv z G (hom (Matrix.vecTail u))))) := fun X => rfl
  have hFpos : ∀ X, Lor X → 0 ≤ F X := fun X hX => by
    rw [hF]
    exact gate_pairVal_nonneg hpos ha hX (lor_hom_of_unit hτ') (lor_Minv_ctrl hN hG (lor_hom_of_unit hτ))
  have h0 : F (hom z) = 0 := by
    rw [hF, gt_corner_ctrl hN hG, pairVal_tens, dot_hom_hom_neg hτ, mul_zero]
  rw [← hF]
  exact tangent_vanish F hFpos hN.unit hc hzc h0

/-- The sphere identity at the corner `−z`, evaluated at the two corner target states. -/
theorem gt_sphere_corner_ctrl {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}
    (hN : IsNot (eball d) z N) (hG : CtrlGate (eball d) z N G) {c : Fin d → ℝ}
    (hc : ∑ j, c j ^ 2 ≤ 1) (hzc : ∑ j, z j * c j = 0) {a : HVec d} (ha : Lor a) :
    pairVal a (hom z) (G (tens (lift c) (Minv z G (hom z)))) = 0 ∧
    pairVal a (hom (-z)) (G (tens (lift c) (Minv z G (hom (-z))))) = 0 := by
  have hz' : ∑ j, (-z) j ^ 2 = 1 := by simpa [neg_sq] using hN.unit
  have hzc' : ∑ j, (-z) j * c j = 0 := by
    simp only [Pi.neg_apply, neg_mul, Finset.sum_neg_distrib, hzc, neg_zero]
  have hNz : homMap N (hom z) = hom (-z) := by rw [homMap_hom, hN.flips]
  have hNz' : homMap N (hom (-z)) = hom z := by rw [homMap_hom, map_neg, hN.flips, neg_neg]
  have hpos : ∀ x ∈ eball d, ∀ y ∈ eball d,
      (G : W d →ₗ[ℝ] W d) (prodState x y) ∈ maxCone (eball d) :=
    fun x hx y hy => hG.posFwd x hx y hy
  constructor
  · let F : HVec d →ₗ[ℝ] ℝ := pvOmega a (hom z) ∘ₗ (G : W d →ₗ[ℝ] W d) ∘ₗ tensR (Minv z G (hom z))
    have hF : ∀ X, F X = pairVal a (hom z) (G (tens X (Minv z G (hom z)))) := fun X => rfl
    have hFpos : ∀ X, Lor X → 0 ≤ F X := fun X hX => by
      rw [hF]
      exact gate_pairVal_nonneg hpos ha hX (lor_hom_of_unit hN.unit)
        (lor_Minv_ctrl hN hG (lor_hom_of_unit hN.unit))
    have h0 : F (hom (-z)) = 0 := by
      rw [hF, gt_corner_neg_ctrl hN hG, hNz, pairVal_tens, dot_hom_neg_hom hN.unit, mul_zero]
    rw [← hF]
    exact tangent_vanish F hFpos hz' hc hzc' h0
  · let F : HVec d →ₗ[ℝ] ℝ := pvOmega a (hom (-z)) ∘ₗ (G : W d →ₗ[ℝ] W d) ∘ₗ
      tensR (Minv z G (hom (-z)))
    have hF : ∀ X, F X = pairVal a (hom (-z)) (G (tens X (Minv z G (hom (-z))))) := fun X => rfl
    have hFpos : ∀ X, Lor X → 0 ≤ F X := fun X hX => by
      rw [hF]
      exact gate_pairVal_nonneg hpos ha hX (lor_hom_of_unit hz') (lor_Minv_ctrl hN hG (lor_hom_of_unit hz'))
    have h0 : F (hom (-z)) = 0 := by
      rw [hF, gt_corner_neg_ctrl hN hG, hNz', pairVal_tens, dot_hom_hom_neg hN.unit, mul_zero]
    rw [← hF]
    exact tangent_vanish F hFpos hz' hc hzc' h0

/-- The two sphere identities in block form. -/
theorem Phi_sphere_ctrl {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}
    (hN : IsNot (eball d) z N) (hG : CtrlGate (eball d) z N G) {c : Fin d → ℝ}
    (hc : ∑ j, c j ^ 2 ≤ 1) (hzc : ∑ j, z j * c j = 0) {a : HVec d} (ha : Lor a) {u : HVec d}
    (hu0 : u 0 = 0) (hu : ∑ μ, u μ ^ 2 = 1) :
    Phi z G a c u u = Phi z G a c (hom 0) (hom 0) ∧
    Phi z G a c (hom 0) u = Phi z G a c u (hom 0) := by
  have h1 : Phi z G a c (hom 0 - u) (hom 0 + u) = 0 := gt_sphere_ctrl hN hG hc hzc ha hu0 hu
  have hu0' : (-u) 0 = 0 := by rw [Pi.neg_apply, hu0, neg_zero]
  have hu' : ∑ μ, (-u) μ ^ 2 = 1 := by simpa [neg_sq] using hu
  have h2 : Phi z G a c (hom 0 - -u) (hom 0 + -u) = 0 := gt_sphere_ctrl hN hG hc hzc ha hu0' hu'
  rw [sub_neg_eq_add, ← sub_eq_add_neg] at h2
  simp only [map_add, map_sub, LinearMap.add_apply, LinearMap.sub_apply] at h1 h2
  constructor <;> linarith

/-- The centre value of the block form vanishes. -/
theorem Phi_center_ctrl {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}
    (hN : IsNot (eball d) z N) (hG : CtrlGate (eball d) z N G) {c : Fin d → ℝ}
    (hc : ∑ j, c j ^ 2 ≤ 1) (hzc : ∑ j, z j * c j = 0) {a : HVec d} (ha : Lor a) :
    Phi z G a c (hom 0) (hom 0) = 0 := by
  have hz0 : lift z 0 = 0 := lift_zero z
  have hz1 : ∑ μ, lift z μ ^ 2 = 1 := by
    rw [Fin.sum_univ_succ, lift_zero, zero_pow two_ne_zero, zero_add]
    simpa using hN.unit
  obtain ⟨ha1, hb1⟩ := Phi_sphere_ctrl hN hG hc hzc ha hz0 hz1
  have hc0 : Phi z G a c (hom z) (hom z) = 0 := (gt_sphere_corner_ctrl hN hG hc hzc ha).1
  have hc1 : Phi z G a c (hom (-z)) (hom (-z)) = 0 := (gt_sphere_corner_ctrl hN hG hc hzc ha).2
  rw [hom_eq_add_lift z] at hc0
  rw [hom_eq_add_lift (-z), lift_neg, ← sub_eq_add_neg] at hc1
  simp only [map_add, map_sub, LinearMap.add_apply, LinearMap.sub_apply] at hc0 hc1
  linarith

/-- The centre value vanishes for every control effect. -/
theorem Phi_center_all_ctrl {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}
    (hN : IsNot (eball d) z N) (hG : CtrlGate (eball d) z N G) {c : Fin d → ℝ}
    (hc : ∑ j, c j ^ 2 ≤ 1) (hzc : ∑ j, z j * c j = 0) (a : HVec d) :
    Phi z G a c (hom 0) (hom 0) = 0 := by
  have h := linearMap_eq_zero_of_lor (pvLeft (hom 0) (G (tens (lift c) (Minv z G (hom 0)))))
    (fun a ha => Phi_center_ctrl hN hG hc hzc ha)
  have := LinearMap.congr_fun h a
  rw [LinearMap.zero_apply] at this
  exact this

/-- The block form against the unit control effect vanishes identically. -/
theorem Phi_hom_zero_eq_zero_ctrl {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}
    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hG : CtrlGate (eball d) z N G)
    {c : Fin d → ℝ} (hc : ∑ j, c j ^ 2 ≤ 1) (hzc : ∑ j, z j * c j = 0) (f t : HVec d) :
    Phi z G (hom 0) c f t = 0 := by
  have key : ∀ f t, Lor f → Lor t → Phi z G (hom 0) c f t = 0 := by
    intro f t hf ht
    obtain ⟨h1, h2⟩ := gt_tangent_corners_ctrl hN hG hc hzc hf ht
    have hboth : pairVal (hom z + hom (-z)) f (G (tens (lift c) (Minv z G t))) = 0 := by
      rw [pairVal_add_left, h1, h2, add_zero]
    rw [hom_add_hom_neg, pairVal_smul_left] at hboth
    rw [Phi_apply]
    linarith
  have hT : ∀ f, Lor f → Phi z G (hom 0) c f = 0 := fun f hf =>
    linearMap_eq_zero_of_lor _ (fun t ht => key f t hf ht)
  have hF : Phi z G (hom 0) c = 0 := linearMap_eq_zero_of_lor _ hT
  rw [hF, LinearMap.zero_apply, LinearMap.zero_apply]

/-- The block form against the lifted corner axis vanishes identically. -/
theorem Phi_lift_z_eq_zero_ctrl {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}
    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hG : CtrlGate (eball d) z N G)
    {c : Fin d → ℝ} (hc : ∑ j, c j ^ 2 ≤ 1) (hzc : ∑ j, z j * c j = 0) (f t : HVec d) :
    Phi z G (lift z) c f t = 0 := by
  have key : ∀ f t, Lor f → Lor t → Phi z G (lift z) c f t = 0 := by
    intro f t hf ht
    have h2 := (gt_tangent_corners_ctrl hN hG hc hzc hf ht).2
    have h0 := Phi_hom_zero_eq_zero_ctrl hN hG hc hzc f t
    rw [hom_eq_add_lift z, pairVal_add_left] at h2
    rw [Phi_apply] at h0
    rw [Phi_apply]
    linarith
  have hT : ∀ f, Lor f → Phi z G (lift z) c f = 0 := fun f hf =>
    linearMap_eq_zero_of_lor _ (fun t ht => key f t hf ht)
  have hF : Phi z G (lift z) c = 0 := linearMap_eq_zero_of_lor _ hT
  rw [hF, LinearMap.zero_apply, LinearMap.zero_apply]

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
theorem blockData_of_orthonormal_ctrl {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}
    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hG : CtrlGate (eball d) z N G) (hd : 2 ≤ d)
    {q : ℕ} (v : Fin q → HVec d) (hvS : ∀ r, v r ∈ tangentSpace N)
    (hvv : ∀ r s, ∑ μ, v r μ * v s μ = if r = s then 1 else 0)
    (hspan : ∀ u ∈ tangentSpace N, (∀ r, ∑ μ, v r μ * u μ = 0) → u = 0) : BlockData q := by
  have hz := hN.unit
  have hv0 : ∀ r, v r 0 = 0 := fun r => (mem_tangentSpace.mp (hvS r)).2
  have hvN : ∀ r, homMap N (v r) = v r := fun r => (mem_tangentSpace.mp (hvS r)).1
  have hvu : ∀ r, ∑ μ, v r μ ^ 2 = 1 := fun r => by
    have := hvv r r
    rw [if_pos rfl] at this
    rw [← this]
    exact Finset.sum_congr rfl fun μ _ => sq _
  have hpos : ∀ x ∈ eball d, ∀ y ∈ eball d,
      (G : W d →ₗ[ℝ] W d) (prodState x y) ∈ maxCone (eball d) :=
    fun x hx y hy => hG.posFwd x hx y hy
  have hsym : ∀ k l r, Phi z G (hom (tperp z k)) (tperp z l) (hom 0) (v r)
      = Phi z G (hom (tperp z k)) (tperp z l) (v r) (hom 0) := fun k l r =>
    (Phi_sphere_ctrl hN hG (tperp_le_one hz l) (tperp_dot_z hz l) (lor_hom (tperp_mem hz k)) (hv0 r)
      (hvu r)).2
  have hdiag : ∀ k l r, Phi z G (hom (tperp z k)) (tperp z l) (v r) (v r) = 0 := fun k l r => by
    rw [(Phi_sphere_ctrl hN hG (tperp_le_one hz l) (tperp_dot_z hz l) (lor_hom (tperp_mem hz k)) (hv0 r)
      (hvu r)).1]
    exact Phi_center_ctrl hN hG (tperp_le_one hz l) (tperp_dot_z hz l) (lor_hom (tperp_mem hz k))
  have hanti : ∀ k l r s, Phi z G (hom (tperp z k)) (tperp z l) (v r) (v s)
      + Phi z G (hom (tperp z k)) (tperp z l) (v s) (v r) = 0 := by
    intro k l r s
    by_cases hrs : r = s
    · subst hrs; rw [hdiag, add_zero]
    · obtain ⟨w, hw⟩ : ∃ w : HVec d, w = (8 / 17 : ℝ) • v r + (15 / 17 : ℝ) • v s := ⟨_, rfl⟩
      have hw0 : w 0 = 0 := by
        rw [hw, Pi.add_apply, Pi.smul_apply, Pi.smul_apply, hv0, hv0, smul_zero, smul_zero,
          add_zero]
      have hwu : ∑ μ, w μ ^ 2 = 1 := by
        have e : ∀ μ, w μ ^ 2 = (8 / 17 : ℝ) ^ 2 * (v r μ * v r μ)
            + 2 * ((8 / 17 : ℝ) * (15 / 17 : ℝ)) * (v r μ * v s μ)
            + (15 / 17 : ℝ) ^ 2 * (v s μ * v s μ) := fun μ => by
          rw [hw, Pi.add_apply, Pi.smul_apply, Pi.smul_apply, smul_eq_mul, smul_eq_mul]; ring
        rw [Finset.sum_congr rfl fun μ _ => e μ, Finset.sum_add_distrib, Finset.sum_add_distrib,
          ← Finset.mul_sum, ← Finset.mul_sum, ← Finset.mul_sum, hvv r r, hvv r s, hvv s s,
          if_pos rfl, if_pos rfl, if_neg hrs]
        norm_num
      have hww : Phi z G (hom (tperp z k)) (tperp z l) w w = 0 := by
        rw [(Phi_sphere_ctrl hN hG (tperp_le_one hz l) (tperp_dot_z hz l) (lor_hom (tperp_mem hz k)) hw0
          hwu).1]
        exact Phi_center_ctrl hN hG (tperp_le_one hz l) (tperp_dot_z hz l) (lor_hom (tperp_mem hz k))
      rw [hw] at hww
      simp only [map_add, map_smul, LinearMap.add_apply, LinearMap.smul_apply, smul_eq_mul,
        hdiag] at hww
      linarith
  refine ⟨d, fun r => Matrix.of fun k l => Phi z G (hom (tperp z k)) (tperp z l) (hom 0) (v r),
    fun r s => Matrix.of fun k l => Phi z G (hom (tperp z k)) (tperp z l) (v r) (v s), ?_, ?_, ?_⟩
  · intro r s
    ext k l
    simp only [Matrix.of_apply, Matrix.neg_apply]
    exact eq_neg_of_add_eq_zero_left (hanti k l r s)
  · intro k l i s hs b hb
    simp only [Matrix.of_apply]
    have hcl := tperp_le_one hz l
    have hzl := tperp_dot_z hz l
    have hak : Lor (hom (tperp z k)) := lor_hom (tperp_mem hz k)
    obtain ⟨f, hf⟩ : ∃ f : HVec d, f = hom 0 + ∑ j, b j • v j := ⟨_, rfl⟩
    obtain ⟨t, ht⟩ : ∃ t : HVec d, t = hom 0 + s • v i := ⟨_, rfl⟩
    have hs2 : s ^ 2 = 1 := by rcases hs with h | h <;> rw [h] <;> norm_num
    have hd00 : dotB (hom 0) (hom 0) = 1 := dot_hom_hom_zero (0 : Fin d → ℝ)
    have hd0 : ∀ r, dotB (hom 0) (v r) = 0 := fun r => by
      rw [dotB_apply, Fin.sum_univ_succ, hom_zero, one_mul, hv0 r]; simp [hom_succ]
    have hd0' : ∀ r, dotB (v r) (hom 0) = 0 := fun r => by
      rw [dotB_apply, Fin.sum_univ_succ, hom_zero, mul_one, hv0 r]; simp [hom_succ]
    have hvv' : ∀ r s, dotB (v r) (v s) = if r = s then 1 else 0 := hvv
    have hS0 : dotB (∑ j, b j • v j) (hom 0) = 0 := by
      rw [LinearMap.map_sum₂]
      exact Finset.sum_eq_zero fun j _ => by rw [LinearMap.map_smul₂, hd0', smul_zero]
    have hS0' : dotB (hom 0) (∑ j, b j • v j) = 0 := by
      rw [map_sum]
      exact Finset.sum_eq_zero fun j _ => by rw [map_smul, hd0, smul_zero]
    have hS1' : ∀ j, dotB (v j) (∑ j', b j' • v j') = b j := fun j => by
      rw [map_sum]
      simp only [map_smul, smul_eq_mul, hvv', mul_ite, mul_one, mul_zero]
      rw [Finset.sum_ite_eq]
      simp
    have hSS : dotB (∑ j, b j • v j) (∑ j, b j • v j) = 1 := by
      rw [LinearMap.map_sum₂, Finset.sum_congr rfl fun j _ =>
        LinearMap.map_smul₂ dotB (b j) (v j) (∑ j', b j' • v j')]
      simp only [smul_eq_mul, hS1']
      rw [← hb]
      exact Finset.sum_congr rfl fun j _ => (sq _).symm
    have hf0 : f 0 = 1 := by
      rw [hf, Pi.add_apply, hom_zero, Finset.sum_apply]
      simp only [Pi.smul_apply, hv0, smul_zero, Finset.sum_const_zero, add_zero]
    have ht0 : t 0 = 1 := by
      rw [ht, Pi.add_apply, hom_zero, Pi.smul_apply, hv0, smul_zero, add_zero]
    have hfL : Lor f := by
      apply lor_of_dotB
      · rw [hf0]; exact zero_le_one
      · rw [hf0, hf, LinearMap.map_add₂, map_add, map_add, hd00, hS0', hS0, hSS]; norm_num
    have htL : Lor t := by
      apply lor_of_dotB
      · rw [ht0]; exact zero_le_one
      · rw [ht0]
        simp only [ht, LinearMap.map_add₂, map_add, LinearMap.map_smul₂, map_smul,
          LinearMap.add_apply, LinearMap.smul_apply, smul_eq_mul, hd00, hd0, hd0', hvv',
          eq_self_iff_true, if_true]
        nlinarith [hs2]
    have htN : homMap N t = t := by
      rw [ht, map_add, map_smul, homMap_hom, map_zero, hvN]
    have hR : 0 ≤ pairVal (hom (tperp z k)) f (G (tens (hom (tperp z l)) (Minv z G t))) :=
      gate_pairVal_nonneg hpos hak (lor_hom (tperp_mem hz l)) hfL (lor_Minv_ctrl hN hG htL)
    have hsplit : pairVal (hom (tperp z k)) f (G (tens (hom (tperp z l)) (Minv z G t)))
        = ∑ ν, t ν * f ν
          + pairVal (hom (tperp z k)) f (G (tens (lift (tperp z l)) (Minv z G t))) := by
      rw [hom_eq_add_lift (tperp z l), tens_add_left, map_add, pairVal_add_omega,
        gt_center_ctrl hN hG htN, pairVal_tens, dot_hom_hom_zero, one_mul]
    rw [hsplit] at hR
    change 0 ≤ dotB t f + Phi z G (hom (tperp z k)) (tperp z l) f t at hR
    have hft : dotB t f = 1 + s * b i := by
      simp only [ht, hf, LinearMap.map_add₂, map_add, LinearMap.map_smul₂, map_smul,
        LinearMap.add_apply, LinearMap.smul_apply, smul_eq_mul, hd00, hd0, hd0', hS0', hS1'] <;> ring
    have hΦ : Phi z G (hom (tperp z k)) (tperp z l) f t
        = Phi z G (hom (tperp z k)) (tperp z l) (hom 0) (hom 0)
          + s * Phi z G (hom (tperp z k)) (tperp z l) (hom 0) (v i)
          + (∑ j, b j * Phi z G (hom (tperp z k)) (tperp z l) (v j) (hom 0)
            + s * ∑ j, b j * Phi z G (hom (tperp z k)) (tperp z l) (v j) (v i)) := by
      rw [hf, ht, LinearMap.map_add₂, map_add, map_add, map_smul, map_smul, LinearMap.map_sum₂,
        LinearMap.map_sum₂,
        Finset.sum_congr rfl fun j _ =>
          LinearMap.map_smul₂ (Phi z G (hom (tperp z k)) (tperp z l)) (b j) (v j) (hom 0),
        Finset.sum_congr rfl fun j _ =>
          LinearMap.map_smul₂ (Phi z G (hom (tperp z k)) (tperp z l)) (b j) (v j) (v i)]
      simp only [smul_eq_mul]
    have hΦ00 := Phi_center_all_ctrl hN hG hcl hzl (hom (tperp z k))
    have hsumsplit : ∑ j, b j * (Phi z G (hom (tperp z k)) (tperp z l) (hom 0) (v j)
          + s * ((if j = i then (1 : ℝ) else 0) + Phi z G (hom (tperp z k)) (tperp z l) (v j) (v i)))
        = ∑ j, b j * Phi z G (hom (tperp z k)) (tperp z l) (v j) (hom 0) + s * b i
          + s * ∑ j, b j * Phi z G (hom (tperp z k)) (tperp z l) (v j) (v i) := by
      have e : ∀ j, b j * (Phi z G (hom (tperp z k)) (tperp z l) (hom 0) (v j)
          + s * ((if j = i then (1 : ℝ) else 0) + Phi z G (hom (tperp z k)) (tperp z l) (v j) (v i)))
          = b j * Phi z G (hom (tperp z k)) (tperp z l) (v j) (hom 0)
            + (if j = i then s * b j else 0)
            + s * (b j * Phi z G (hom (tperp z k)) (tperp z l) (v j) (v i)) := by
        intro j; rw [hsym k l j]; split_ifs <;> ring
      rw [Finset.sum_congr rfl fun j _ => e j, Finset.sum_add_distrib, Finset.sum_add_distrib,
        Finset.sum_ite_eq', ← Finset.mul_sum]
      simp only [Finset.mem_univ, if_true]
    rw [hsumsplit]
    rw [hft, hΦ, hΦ00] at hR
    linarith
  · by_contra hcon
    have hzero : ∀ r k l, Phi z G (hom (tperp z k)) (tperp z l) (hom 0) (v r) = 0 := by
      intro r k l
      by_contra h
      exact hcon ⟨r, k, l, by simp only [Matrix.of_apply]; exact h⟩
    obtain ⟨l, hl⟩ := exists_tperp_ne_zero hz hd
    have hcl := tperp_le_one hz l
    have hzl := tperp_dot_z hz l
    obtain ⟨ω, hω⟩ : ∃ ω : W d, ω = G (tens (lift (tperp z l)) (Minv z G (hom 0))) := ⟨_, rfl⟩
    have hMi0 : Minv z G (hom (0 : Fin d → ℝ)) ≠ 0 := by
      intro h
      have := Mfwd_Minv_ctrl hN hG (hom (0 : Fin d → ℝ))
      rw [h, map_zero] at this
      exact hom_zero_ne_zero this.symm
    have hlift : lift (tperp z l) ≠ 0 := by
      intro h
      apply hl
      funext j
      have := congrFun h j.succ
      rwa [lift_succ, Pi.zero_apply] at this
    have hωne : ω ≠ 0 := by
      rw [hω]
      intro h
      exact tens_ne_zero hlift hMi0 (G.map_eq_zero_iff.mp h)
    have hrow : ∀ μ, ω μ = 0 := by
      intro μ
      apply hspan (ω μ)
      · rw [mem_tangentSpace]
        constructor
        · have h1 : actT N ω = ω := by
            rw [hω]; exact actT_slice_ctrl hN hG hcl hzl
          exact congrFun h1 μ
        · have h := Phi_center_all_ctrl hN hG hcl hzl (bvec μ)
          rw [Phi_apply, ← hω, pairVal_bvec, sum_row_hom_zero] at h
          exact h
      · intro r
        have hk : ∀ k, pairVal (hom (tperp z k)) (v r) ω = 0 := by
          intro k
          have := hzero r k l
          rw [hsym k l r, Phi_apply, ← hω] at this
          exact this
        have h0 : pairVal (hom 0) (v r) ω = 0 := by
          have := Phi_hom_zero_eq_zero_ctrl hN hG hcl hzl (v r) (hom 0)
          rwa [Phi_apply, ← hω] at this
        have hz' : pairVal (lift z) (v r) ω = 0 := by
          have := Phi_lift_z_eq_zero_ctrl hN hG hcl hzl (v r) (hom 0)
          rwa [Phi_apply, ← hω] at this
        have hb : ∀ μ', pairVal (bvec μ') (v r) ω = 0 := by
          intro μ'
          refine Fin.cases ?_ (fun k => ?_) μ'
          · rw [bvec_zero_eq]; exact h0
          · have hk' := hk k
            rw [hom_eq_add_lift (tperp z k), lift_tperp, pairVal_add_left, h0, zero_add,
              pairVal_sub_left, pairVal_smul_left, hz', mul_zero, sub_zero] at hk'
            exact hk'
        have := hb μ
        rw [pairVal_bvec] at this
        calc ∑ μ', v r μ' * ω μ μ' = ∑ ν, ω μ ν * v r ν :=
              Finset.sum_congr rfl fun ν _ => mul_comm _ _
          _ = 0 := this
    exact hωne (funext hrow)

/-- **The block reduction (S1, S2, S4)** without the target relation. -/
theorem blockData_of_ctrlGate {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}
    {G : W d ≃ₗ[ℝ] W d} (hd : 2 ≤ d) (hN : IsNot (eball d) z N) (hG : CtrlGate (eball d) z N G) :
    BlockData (tangentPlus N) := by
  obtain ⟨q, v, hq, hvS, hvv, hspan⟩ := exists_orthonormal_basis (tangentSpace N)
  rw [finrank_tangentSpace] at hq
  rw [← hq]
  exact blockData_of_orthonormal_ctrl hN hG hd v hvS hvv hspan

/-- No gate of two intervals with the frame is entangling. -/
theorem not_entangling_one_ctrl {z : Fin 1 → ℝ} {N : (Fin 1 → ℝ) →ₗ[ℝ] (Fin 1 → ℝ)}
    {G : W 1 ≃ₗ[ℝ] W 1} (hN : IsNot (eball 1) z N) (hG : CtrlGate (eball 1) z N G) :
    ¬ Entangling (eball 1) G := by
  rintro ⟨x, hx, y, hy, -, hnp⟩
  have hz : z 0 ^ 2 = 1 := by have := hN.unit; rwa [Fin.sum_univ_one] at this
  obtain ⟨a, rfl⟩ := eq_corner_of_extreme hz hx
  obtain ⟨b, rfl⟩ := eq_corner_of_extreme hz hy
  apply hnp
  rw [hG.frame a b]
  exact ⟨corner z a, corner_mem_one hz a, corner z (a + b), corner_mem_one hz _, rfl⟩

/-- **The selector without the target relation.** Two identical copies of the Euclidean ball with
a gate satisfying the frame, two-sided positivity and the control relation have dimension one or
three. -/
theorem dim_of_ctrlGate {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}
    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hG : CtrlGate (eball d) z N G) :
    d = 1 ∨ d = 3 := by
  have hpos := pos_of_isNot hN
  rcases Nat.lt_or_ge d 2 with h | h
  · left; omega
  · have hsum := finrank_plus_add_finrank_minus hN.invol
    have hbal := finrank_plus_eq_finrank_minus_relC hN hG.relC
    have hp := one_le_finrank_plusSpace N
    have hle := p_le_one_of_blockData (blockData_of_ctrlGate h hN hG)
    exact NativeGateBall.dim_of_bounds (tangentPlus N) (Module.finrank ℝ (minusSpace N) - 1) d hle
      (by unfold tangentPlus; omega) (by unfold tangentPlus; omega)

/-- **The selector under the entangling clause, without the target relation.** -/
theorem three_of_ctrlGate {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}
    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hG : CtrlGate (eball d) z N G)
    (hE : Entangling (eball d) G) : d = 3 := by
  rcases dim_of_ctrlGate hN hG with hone | hthree
  · exfalso
    subst hone
    exact not_entangling_one_ctrl hN hG hE
  · exact hthree

end RelcSelect
end OIBridge

#print axioms OIBridge.RelcSelect.ctrlGate_of_nativeGate
#print axioms OIBridge.RelcSelect.actT_slice_ctrl
#print axioms OIBridge.RelcSelect.blockData_of_ctrlGate
#print axioms OIBridge.RelcSelect.dim_of_ctrlGate
#print axioms OIBridge.RelcSelect.three_of_ctrlGate
