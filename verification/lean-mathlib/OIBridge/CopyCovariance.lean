/-
  OIBridge/CopyCovariance.lean — design module of the research thread `research/equivalence`
  (node E8, draft S2): the predicted module of round KINF-COPY-1, split from the design modules
  `EqvSeams` (§B–§D) and `EqvSeamsControl`, built in run 38083519826, with no statement changed.
  Not adopted, not certified, not a round.

  `NativeGate2` is DIM-1's `NativeGate` with two NOTs, `NC` on the control copy and `NT` on the
  target copy. Conjugating such data on the target copy by a linear automorphism of the body fixing
  the corner axis gives two-NOT data with the target NOT conjugated (`nativeGate2_conj`); when `NT`
  is the conjugate of `NC` by such an automorphism (type covariance), the conjugated gate is a native
  gate with the single NOT `NC` (`nativeGate_of_conj`) and DIM-1's selector applies
  (`dim_of_nativeGate2_conj`, `three_of_nativeGate2_conj_of_two_le`, `dim_of_nativeGate2_conj_neg`).
  §E: the swapped `cnot` at `d = 3` is two-NOT data with distinct NOTs (`swapped_nativeGate2`,
  `swapped_not_ne`); it is also a one-NOT native gate with the target NOT (`swapped_nativeGate`).
  Every hypothesis is a premise; nothing here sources a conjugator, a NOT or a gate.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.DenseOrbit

namespace OIBridge
namespace CopyCovariance

open Set KInfFoundations OrbitGeneration OrbitNormalization StageCompletion CompletionAction
open TransitiveBody CompositeDimension K2Guard DenseOrbit

noncomputable section

/-! ### §B — the token-action calculus at every dimension -/

variable {d : ℕ}

theorem homMap_comp' (M N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (v : HVec d) :
    homMap (M ∘ₗ N) v = homMap M (homMap N v) := by
  funext μ
  refine Fin.cases ?_ (fun j => ?_) μ
  · rfl
  · rw [homMap_succ, homMap_succ, vecTail_homMap, LinearMap.comp_apply]

theorem homMap_id' (v : HVec d) : homMap LinearMap.id v = v := by
  funext μ
  refine Fin.cases ?_ (fun j => ?_) μ
  · rfl
  · rw [homMap_succ, LinearMap.id_apply]; rfl

theorem actT_comp' (M N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (ω : W d) :
    actT M (actT N ω) = actT (M ∘ₗ N) ω := by
  funext μ
  show homMap M (homMap N (ω μ)) = homMap (M ∘ₗ N) (ω μ)
  rw [homMap_comp']

theorem actT_id' (ω : W d) : actT LinearMap.id ω = ω := by
  funext μ
  exact homMap_id' (ω μ)

theorem actT_congr {M N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} (h : ∀ x, M x = N x) (ω : W d) :
    actT M ω = actT N ω := by
  rw [LinearMap.ext h]

theorem lin_apply_eq_sum' (M : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (x : Fin d → ℝ) (i : Fin d) :
    M x i = ∑ k, LinearMap.toMatrix' M i k * x k :=
  (congrFun (LinearMap.toMatrix'_mulVec M x) i).symm

theorem lin_lin_comm' (M N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (Ω' : Fin d → Fin d → ℝ)
    (i j : Fin d) :
    M (fun i' => N (Ω' i') j) i = N (fun j' => M (fun i' => Ω' i' j') i) j := by
  simp only [lin_apply_eq_sum' M, lin_apply_eq_sum' N, Finset.mul_sum]
  rw [Finset.sum_comm]
  refine Finset.sum_congr rfl fun l _ => Finset.sum_congr rfl fun k _ => ?_
  ring

/-- The two token actions commute, at every dimension. -/
theorem actC_actT_comm' (M N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (ω : W d) :
    actC M (actT N ω) = actT N (actC M ω) := by
  funext μ ν
  refine Fin.cases ?_ (fun i => ?_) μ <;> refine Fin.cases ?_ (fun j => ?_) ν
  · rfl
  · rfl
  · rfl
  · simp only [actC_apply, actT_apply, homMap_succ, Matrix.vecTail, Function.comp_def]
    exact lin_lin_comm' M N (fun i' j' => ω i'.succ j'.succ) i j

/-- The target action of a linear map with a two-sided inverse, as a linear equivalence. -/
def actTEq (g h : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (hgh : ∀ x, g (h x) = x)
    (hhg : ∀ x, h (g x) = x) : W d ≃ₗ[ℝ] W d where
  toFun := actT g
  invFun := actT h
  map_add' ω₁ ω₂ := by
    funext μ ν
    simp only [actT_apply, Pi.add_apply, map_add]
  map_smul' c ω := by
    funext μ ν
    simp only [actT_apply, Pi.smul_apply, map_smul, smul_eq_mul, RingHom.id_apply]
  left_inv ω := by
    show actT h (actT g ω) = ω
    rw [actT_comp', actT_congr (M := h ∘ₗ g) (N := LinearMap.id)
      (fun x => by simp only [LinearMap.comp_apply, LinearMap.id_apply]; exact hhg x), actT_id']
  right_inv ω := by
    show actT g (actT h ω) = ω
    rw [actT_comp', actT_congr (M := g ∘ₗ h) (N := LinearMap.id)
      (fun x => by simp only [LinearMap.comp_apply, LinearMap.id_apply]; exact hgh x), actT_id']

/-! ### §C — the maximal cone under a body-preserving map of one copy -/

/-- The homogenized pairing of a vector with the coefficients of an affine functional. -/
theorem sum_mul_ehom (e : (Fin d → ℝ) →ᵃ[ℝ] ℝ) (v : HVec d) :
    ∑ ν, v ν * ehom e ν = v 0 * e 0 + e.linear (Matrix.vecTail v) := by
  rw [Fin.sum_univ_succ, LinearMap.pi_apply_eq_sum_univ e.linear (Matrix.vecTail v)]
  congr 1
  all_goals first
    | rfl
    | (refine Finset.sum_congr rfl fun j _ => ?_
       simp only [ehom, Matrix.cons_val_succ, smul_eq_mul, Matrix.vecTail, Function.comp_apply])

theorem affine_linear_apply (f : (Fin d → ℝ) →ᵃ[ℝ] ℝ) (x : Fin d → ℝ) :
    f.linear x = f x - f 0 := by
  have hd := congrFun (AffineMap.decomp f) x
  simp only [Pi.add_apply] at hd
  linarith

theorem sum_homMap_mul_ehom (g : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (f : (Fin d → ℝ) →ᵃ[ℝ] ℝ)
    (v : HVec d) :
    ∑ ν, homMap g v ν * ehom f ν = ∑ ν, v ν * ehom (f.comp g.toAffineMap) ν := by
  rw [sum_mul_ehom, sum_mul_ehom, homMap_zero, vecTail_homMap, affine_linear_apply f,
    affine_linear_apply (f.comp g.toAffineMap)]
  simp only [AffineMap.comp_apply, LinearMap.coe_toAffineMap, map_zero]

/-- A product effect read after a target-side map is the product effect with the target factor
pulled back. -/
theorem prodEffVal_actT (g : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (e f : (Fin d → ℝ) →ᵃ[ℝ] ℝ)
    (ω : W d) : prodEffVal e f (actT g ω) = prodEffVal e (f.comp g.toAffineMap) ω := by
  unfold prodEffVal pairVal
  refine Finset.sum_congr rfl fun μ _ => ?_
  calc ∑ ν, ehom e μ * actT g ω μ ν * ehom f ν
      = ehom e μ * ∑ ν, homMap g (ω μ) ν * ehom f ν := by
        rw [Finset.mul_sum]
        refine Finset.sum_congr rfl fun ν _ => ?_
        rw [actT_apply]
        ring
    _ = ehom e μ * ∑ ν, ω μ ν * ehom (f.comp g.toAffineMap) ν := by
        rw [sum_homMap_mul_ehom]
    _ = ∑ ν, ehom e μ * ω μ ν * ehom (f.comp g.toAffineMap) ν := by
        rw [Finset.mul_sum]
        refine Finset.sum_congr rfl fun ν _ => ?_
        ring

theorem isEffectOn_comp {Ω : Set (Fin d → ℝ)} {f : (Fin d → ℝ) →ᵃ[ℝ] ℝ} (hf : IsEffectOn Ω f)
    {g : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} (hg : ∀ x ∈ Ω, g x ∈ Ω) :
    IsEffectOn Ω (f.comp g.toAffineMap) := by
  intro x hx
  simpa only [AffineMap.comp_apply, LinearMap.coe_toAffineMap] using hf (g x) (hg x hx)

/-- A target-side linear map carrying the body into itself preserves the maximal cone. -/
theorem actT_mem_maxCone {Ω : Set (Fin d → ℝ)} {g : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}
    (hg : ∀ x ∈ Ω, g x ∈ Ω) {ω : W d} (hω : ω ∈ maxCone Ω) : actT g ω ∈ maxCone Ω := by
  intro e f he hf
  rw [prodEffVal_actT]
  exact hω e _ he (isEffectOn_comp hf hg)

/-! ### §D — two NOTs, and the conjugation reduction -/

/-- DIM-1's native-gate hypotheses with two NOTs: `NC` on the control copy, `NT` on the target
copy. With `NC = NT` it is `NativeGate` (`nativeGate2_of_nativeGate`, `nativeGate_of_nativeGate2`). -/
structure NativeGate2 (Ω : Set (Fin d → ℝ)) (z : Fin d → ℝ)
    (NC NT : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (G : W d ≃ₗ[ℝ] W d) : Prop where
  frame : ∀ a b : Fin 2,
    G (prodState (corner z a) (corner z b)) = prodState (corner z a) (corner z (a + b))
  posFwd : ∀ x ∈ Ω, ∀ y ∈ Ω, G (prodState x y) ∈ maxCone Ω
  posInv : ∀ x ∈ Ω, ∀ y ∈ Ω, G.symm (prodState x y) ∈ maxCone Ω
  relT : ∀ ω, actT NT (G (actT NT ω)) = G ω
  relC : ∀ ω, actC NC (G (actC NC ω)) = actT NT (G ω)

theorem nativeGate2_of_nativeGate {Ω : Set (Fin d → ℝ)} {z : Fin d → ℝ}
    {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d} (h : NativeGate Ω z N G) :
    NativeGate2 Ω z N N G :=
  ⟨h.frame, h.posFwd, h.posInv, h.relT, h.relC⟩

theorem nativeGate_of_nativeGate2 {Ω : Set (Fin d → ℝ)} {z : Fin d → ℝ}
    {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d} (h : NativeGate2 Ω z N N G) :
    NativeGate Ω z N G :=
  ⟨h.frame, h.posFwd, h.posInv, h.relT, h.relC⟩

theorem map_corner_of_fix {g : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {z : Fin d → ℝ} (hgz : g z = z)
    (b : Fin 2) : g (corner z b) = corner z b := by
  fin_cases b
  · first
      | exact hgz
      | simp [corner, hgz]
  · first
      | (show g (-z) = -z; rw [map_neg, hgz])
      | simp [corner, hgz]

/-- The conjugated gate applied: `actT h ∘ G ∘ actT g`. -/
theorem conjGate_apply (g h : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (hgh : ∀ x, g (h x) = x)
    (hhg : ∀ x, h (g x) = x) (G : W d ≃ₗ[ℝ] W d) (ω : W d) :
    (actTEq g h hgh hhg ≪≫ₗ G ≪≫ₗ actTEq h g hhg hgh) ω = actT h (G (actT g ω)) := rfl

theorem conjGate_symm_apply (g h : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (hgh : ∀ x, g (h x) = x)
    (hhg : ∀ x, h (g x) = x) (G : W d ≃ₗ[ℝ] W d) (ω : W d) :
    (actTEq g h hgh hhg ≪≫ₗ G ≪≫ₗ actTEq h g hhg hgh).symm ω = actT h (G.symm (actT g ω)) :=
  rfl

/-- **Conjugation on the target copy.** Two-NOT native-gate data, conjugated on the target copy by
a linear automorphism of the body fixing the corner axis, are two-NOT native-gate data with the
target NOT conjugated. -/
theorem nativeGate2_conj {Ω : Set (Fin d → ℝ)} {z : Fin d → ℝ}
    {NC NT : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}
    (hG : NativeGate2 Ω z NC NT G) {g h : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}
    (hgh : ∀ x, g (h x) = x) (hhg : ∀ x, h (g x) = x)
    (hgΩ : ∀ x ∈ Ω, g x ∈ Ω) (hhΩ : ∀ x ∈ Ω, h x ∈ Ω) (hgz : g z = z) :
    NativeGate2 Ω z NC (h ∘ₗ NT ∘ₗ g) (actTEq g h hgh hhg ≪≫ₗ G ≪≫ₗ actTEq h g hhg hgh) := by
  have hhz : h z = z := by
    have hz := hhg z
    rwa [hgz] at hz
  have eT1 : ∀ X : W d, actT (h ∘ₗ NT ∘ₗ g) (actT h X) = actT h (actT NT X) := fun X => by
    rw [actT_comp', actT_comp']
    exact actT_congr (fun x => by simp only [LinearMap.comp_apply, hgh]) X
  have eT2 : ∀ X : W d, actT g (actT (h ∘ₗ NT ∘ₗ g) X) = actT NT (actT g X) := fun X => by
    rw [actT_comp', actT_comp']
    exact actT_congr (fun x => by simp only [LinearMap.comp_apply, hgh]) X
  refine ⟨fun a b => ?_, fun x hx y hy => ?_, fun x hx y hy => ?_, fun ω => ?_, fun ω => ?_⟩
  · rw [conjGate_apply, actT_prodState, map_corner_of_fix hgz, hG.frame, actT_prodState,
      map_corner_of_fix hhz]
  · rw [conjGate_apply, actT_prodState]
    exact actT_mem_maxCone hhΩ (hG.posFwd x hx (g y) (hgΩ y hy))
  · rw [conjGate_symm_apply, actT_prodState]
    exact actT_mem_maxCone hhΩ (hG.posInv x hx (g y) (hgΩ y hy))
  · rw [conjGate_apply, conjGate_apply, eT1, eT2, hG.relT]
  · rw [conjGate_apply, conjGate_apply, ← actC_actT_comm' NC g ω, actC_actT_comm' NC h, hG.relC, eT1]

/-- **Type covariance of native inversion suffices.** If the target NOT is the conjugate of the
control NOT by a linear automorphism of the body fixing the corner axis, the conjugated gate is a
native gate with the single NOT `NC`. -/
theorem nativeGate_of_conj {Ω : Set (Fin d → ℝ)} {z : Fin d → ℝ}
    {NC NT : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}
    (hG : NativeGate2 Ω z NC NT G) {g h : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}
    (hgh : ∀ x, g (h x) = x) (hhg : ∀ x, h (g x) = x)
    (hgΩ : ∀ x ∈ Ω, g x ∈ Ω) (hhΩ : ∀ x ∈ Ω, h x ∈ Ω) (hgz : g z = z)
    (hcov : ∀ x, NT (g x) = g (NC x)) :
    NativeGate Ω z NC (actTEq g h hgh hhg ≪≫ₗ G ≪≫ₗ actTEq h g hhg hgh) := by
  have h2 := nativeGate2_conj hG hgh hhg hgΩ hhΩ hgz
  have hN : h ∘ₗ NT ∘ₗ g = NC := LinearMap.ext fun x => by
    simp only [LinearMap.comp_apply, hcov, hhg]
  rw [hN] at h2
  exact nativeGate_of_nativeGate2 h2

/-- **The selector under type covariance.** DIM-1's `dim_of_nativeGate` through the reduction. -/
theorem dim_of_nativeGate2_conj {z : Fin d → ℝ} {NC NT : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}
    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z NC) (hG : NativeGate2 (eball d) z NC NT G)
    {g h : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} (hgh : ∀ x, g (h x) = x) (hhg : ∀ x, h (g x) = x)
    (hgΩ : ∀ x ∈ eball d, g x ∈ eball d) (hhΩ : ∀ x ∈ eball d, h x ∈ eball d)
    (hgz : g z = z) (hcov : ∀ x, NT (g x) = g (NC x)) : d = 1 ∨ d = 3 :=
  dim_of_nativeGate hN (nativeGate_of_conj hG hgh hhg hgΩ hhΩ hgz hcov)

/-- **Three under type covariance and `2 ≤ d`.** K2-GUARD-1's selector through the reduction. -/
theorem three_of_nativeGate2_conj_of_two_le (hd : 2 ≤ d) {z : Fin d → ℝ}
    {NC NT : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}
    (hN : IsNot (eball d) z NC) (hG : NativeGate2 (eball d) z NC NT G)
    {g h : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} (hgh : ∀ x, g (h x) = x) (hhg : ∀ x, h (g x) = x)
    (hgΩ : ∀ x ∈ eball d, g x ∈ eball d) (hhΩ : ∀ x ∈ eball d, h x ∈ eball d)
    (hgz : g z = z) (hcov : ∀ x, NT (g x) = g (NC x)) : d = 3 :=
  three_of_nativeGate_of_two_le hd hN (nativeGate_of_conj hG hgh hhg hgΩ hhΩ hgz hcov)

/-- **A conjugator reversing the corner axis.** Composed with `NC` it fixes the axis and still
conjugates `NC` to `NT`, so the selector applies. -/
theorem dim_of_nativeGate2_conj_neg {z : Fin d → ℝ} {NC NT : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}
    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z NC) (hG : NativeGate2 (eball d) z NC NT G)
    {g h : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} (hgh : ∀ x, g (h x) = x) (hhg : ∀ x, h (g x) = x)
    (hgΩ : ∀ x ∈ eball d, g x ∈ eball d) (hhΩ : ∀ x ∈ eball d, h x ∈ eball d)
    (hgz : g z = -z) (hcov : ∀ x, NT (g x) = g (NC x)) : d = 1 ∨ d = 3 := by
  refine dim_of_nativeGate2_conj (g := g ∘ₗ NC) (h := NC ∘ₗ h) hN hG ?_ ?_ ?_ ?_ ?_ ?_
  · intro x
    simp only [LinearMap.comp_apply, hN.invol, hgh]
  · intro x
    simp only [LinearMap.comp_apply, hhg, hN.invol]
  · intro x hx
    simp only [LinearMap.comp_apply]
    exact hgΩ _ (hN.preserves x hx)
  · intro x hx
    simp only [LinearMap.comp_apply]
    exact hN.preserves _ (hhΩ x hx)
  · simp only [LinearMap.comp_apply, hN.flips, map_neg, hgz, neg_neg]
  · intro x
    simp only [LinearMap.comp_apply, hcov, hN.invol]

/-! ### §E — the positive control at `d = 3` -/

/-- The exchange of the first two axes of one copy. -/
def swap01 : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ) where
  toFun v := ![v 1, v 0, v 2]
  map_add' v w := by apply vec3_ext <;> rfl
  map_smul' r v := by apply vec3_ext <;> rfl

theorem swap01_swap01 (v : Fin 3 → ℝ) : swap01 (swap01 v) = v := by
  apply vec3_ext <;> rfl

theorem swap01_mem {v : Fin 3 → ℝ} (hv : v ∈ eball 3) : swap01 v ∈ eball 3 := by
  rw [eball_three] at hv ⊢
  rw [mem_ball3] at hv ⊢
  show v 1 ^ 2 + v 0 ^ 2 + v 2 ^ 2 ≤ 1
  linarith

theorem swap01_z3 : swap01 z3 = z3 := by
  apply vec3_ext <;> rfl

/-- **Two-NOT data with distinct NOTs.** -/
theorem swapped_nativeGate2 :
    NativeGate2 (eball 3) z3 nflip (swap01 ∘ₗ nflip ∘ₗ swap01)
      (actTEq swap01 swap01 swap01_swap01 swap01_swap01 ≪≫ₗ cnot ≪≫ₗ
        actTEq swap01 swap01 swap01_swap01 swap01_swap01) :=
  nativeGate2_conj (nativeGate2_of_nativeGate nativeGate_cnot) swap01_swap01 swap01_swap01
    (fun _ hx => swap01_mem hx) (fun _ hx => swap01_mem hx) swap01_z3

/-- The two NOTs of `swapped_nativeGate2` differ: at the first axis the target NOT is `−1` and the
control NOT is `1`. -/
theorem swapped_not_ne : swap01 ∘ₗ nflip ∘ₗ swap01 ≠ nflip := by
  intro h
  have h0 := congrArg (fun L : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ) => L ![1, 0, 0] 0) h
  have hl : (swap01 ∘ₗ nflip ∘ₗ swap01) ![1, 0, 0] 0 = -1 := by
    show nflip (swap01 ![1, 0, 0]) 1 = -1
    rw [nflip_one]
    show -((![1, 0, 0] : Fin 3 → ℝ) 0) = -1
    norm_num
  have hr : nflip ![1, 0, 0] 0 = 1 := by
    rw [nflip_zero']
    rfl
  have h1 : (swap01 ∘ₗ nflip ∘ₗ swap01) ![1, 0, 0] 0 = nflip ![1, 0, 0] 0 := h0
  rw [hl, hr] at h1
  norm_num at h1

/-- The reduction carries the swapped data back to a native gate with the single NOT `nflip`. -/
theorem swapped_nativeGate :
    NativeGate (eball 3) z3 nflip
      (actTEq swap01 swap01 swap01_swap01 swap01_swap01 ≪≫ₗ
        (actTEq swap01 swap01 swap01_swap01 swap01_swap01 ≪≫ₗ cnot ≪≫ₗ
          actTEq swap01 swap01 swap01_swap01 swap01_swap01) ≪≫ₗ
        actTEq swap01 swap01 swap01_swap01 swap01_swap01) :=
  nativeGate_of_conj swapped_nativeGate2 swap01_swap01 swap01_swap01
    (fun _ hx => swap01_mem hx) (fun _ hx => swap01_mem hx) swap01_z3
    (fun x => by simp only [LinearMap.comp_apply, swap01_swap01])

end

end CopyCovariance
end OIBridge

#print axioms OIBridge.CopyCovariance.actC_actT_comm'
#print axioms OIBridge.CopyCovariance.actTEq
#print axioms OIBridge.CopyCovariance.prodEffVal_actT
#print axioms OIBridge.CopyCovariance.actT_mem_maxCone
#print axioms OIBridge.CopyCovariance.nativeGate2_conj
#print axioms OIBridge.CopyCovariance.nativeGate_of_conj
#print axioms OIBridge.CopyCovariance.dim_of_nativeGate2_conj
#print axioms OIBridge.CopyCovariance.three_of_nativeGate2_conj_of_two_le
#print axioms OIBridge.CopyCovariance.dim_of_nativeGate2_conj_neg
#print axioms OIBridge.CopyCovariance.swapped_nativeGate2
#print axioms OIBridge.CopyCovariance.swapped_not_ne
#print axioms OIBridge.CopyCovariance.swapped_nativeGate
