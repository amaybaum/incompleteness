/-
  OIBridge/CompositeDimension.lean — round DIM-1: the composite dimension selector.

  Two identical copies of the coordinate Euclidean ball `eball d` of `TransitiveBody`, joined on the
  bilinear carrier `W d` (a real function of two homogenized indices), carry one common NOT `N` and a
  reversible gate `G` with the classical CNOT action on the corners `±z`, the target relation
  `(I⊗N) G (I⊗N) = G`, the control relation `(N⊗I) G (N⊗I) = (I⊗N) G`, and two-sided positivity on the
  maximal cone. Local tomography, the common NOT, the reversible CNOT-frame action, two-sided
  positivity and the entangling clause are named premises; no complex structure, no
  nonlocal-correlation inequality, no drive, no flow and no order statement is used or claimed.

  Proved here:
    §A  the carrier: homogenization, the homogenized action of a map on one copy, product states,
        product-effect values, the maximal cone, the joint states, the two actions of `N`, the corners;
    §B  the frozen hypotheses `IsNot`, `NativeGate`, `Entangling`;
    §C  the eigenspace adapter: a linear involution of a finite-dimensional space splits it into its
        `+1` and `−1` eigenspaces (`finrank_ker_sub_add_finrank_ker_add`); for the homogenized NOT the
        two eigenspaces of the control space have dimensions summing to `d + 1`, each at least one;
    §D  the parity count: equal eigenspace dimensions exclude every even `d`;
    §E  a linear NOT of the ball is an isometry and self-adjoint for the dot product;
    §F  joint vectors as operators on the control space; the two actions of `N` become left and
        right composition with its homogenized form;
    §G  the gate in operator form and the two relations transported;
    §H  the projection onto the `−1` eigenspace;
    §I  parity from the frozen hypotheses: on operators from the `−1` eigenspace the gate
        anticommutes with the control action of `N` and is injective, so by
        `NativeGateBall.parity` the two eigenspaces have equal dimension
        (`finrank_plus_eq_finrank_minus`);
    §J  the exclusions: no even `d` (`not_even_of_nativeGate`, with `d = 2`, `d = 4`); given the
        block data of the written S1–S2–S4 reduction (`BlockData`, the hypothesis of
        `NativeGateBall.p_le_one`, a named premise here), `d = 1 ∨ d = 3` (`dim_of_nativeGate`),
        with `d = 5` and `d = 7` as instances.

  Not proved here: the reduction from `NativeGate` to `BlockData` (the controlled form S1, the block
  structure S2 and the value identity S4), which remains the written proof of round NB-1.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.TransitiveBody
import OIBridge.NativeGateBall
import Mathlib.LinearAlgebra.FiniteDimensional.Lemmas
import Mathlib.LinearAlgebra.FreeModule.Finite.Matrix
import Mathlib.LinearAlgebra.Matrix.ToLin

namespace OIBridge
namespace CompositeDimension

open KInfFoundations TransitiveBody NativeGateBall Finset

variable {d : ℕ}

/-! ### §A — the carrier -/

/-- Homogenized coordinates of one copy: index `0` carries the unit, `j.succ` the coordinate `j`. -/
abbrev HVec (d : ℕ) := Fin (d + 1) → ℝ

/-- The joint bilinear carrier of two copies: a real function of a control index and a target index.
Local tomography is the premise this carrier encodes. -/
abbrev W (d : ℕ) := Fin (d + 1) → Fin (d + 1) → ℝ

/-- Homogenization `x ↦ (1, x)`. -/
def hom (x : Fin d → ℝ) : HVec d := Matrix.vecCons 1 x

@[simp] theorem hom_zero (x : Fin d → ℝ) : hom x 0 = 1 := rfl

@[simp] theorem hom_succ (x : Fin d → ℝ) (j : Fin d) : hom x j.succ = x j :=
  Matrix.cons_val_succ _ _ _

theorem vecTail_add (u v : HVec d) : Matrix.vecTail (u + v) = Matrix.vecTail u + Matrix.vecTail v := rfl

theorem vecTail_smul (c : ℝ) (v : HVec d) : Matrix.vecTail (c • v) = c • Matrix.vecTail v := rfl

/-- The homogenized action of a linear map of one copy: the unit coordinate is fixed. -/
def homMap (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) : HVec d →ₗ[ℝ] HVec d where
  toFun v := Matrix.vecCons (v 0) (N (Matrix.vecTail v))
  map_add' u v := by
    funext i
    refine Fin.cases ?_ (fun j => ?_) i
    · simp
    · simp only [Matrix.cons_val_succ, Pi.add_apply]
      rw [vecTail_add, map_add]
      rfl
  map_smul' c v := by
    funext i
    refine Fin.cases ?_ (fun j => ?_) i
    · simp
    · simp only [Matrix.cons_val_succ, Pi.smul_apply, RingHom.id_apply]
      rw [vecTail_smul, map_smul]
      rfl

@[simp] theorem homMap_zero (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (v : HVec d) :
    homMap N v 0 = v 0 := rfl

@[simp] theorem homMap_succ (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (v : HVec d) (j : Fin d) :
    homMap N v j.succ = N (Matrix.vecTail v) j := by
  show Matrix.vecCons (v 0) (N (Matrix.vecTail v)) j.succ = N (Matrix.vecTail v) j
  exact Matrix.cons_val_succ (v 0) (N (Matrix.vecTail v)) j

theorem vecTail_homMap (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (v : HVec d) :
    Matrix.vecTail (homMap N v) = N (Matrix.vecTail v) :=
  Matrix.tail_cons _ _

theorem vecTail_hom (x : Fin d → ℝ) : Matrix.vecTail (hom x) = x := Matrix.tail_cons _ _

/-- The homogenized action carries `hom x` to `hom (N x)`. -/
theorem homMap_hom (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (x : Fin d → ℝ) :
    homMap N (hom x) = hom (N x) := by
  funext i
  refine Fin.cases ?_ (fun j => ?_) i
  · rfl
  · rw [homMap_succ, hom_succ, vecTail_hom]

/-- The homogenized action of an involution is an involution. -/
theorem homMap_homMap {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} (hN : ∀ x, N (N x) = x) (v : HVec d) :
    homMap N (homMap N v) = v := by
  funext i
  refine Fin.cases ?_ (fun j => ?_) i
  · rfl
  · rw [homMap_succ, vecTail_homMap, hN]
    rfl

/-- The product state of two copies. -/
def prodState (x y : Fin d → ℝ) : W d := fun μ ν => hom x μ * hom y ν

/-- The pairing of two homogenized functionals with a joint vector. -/
def pairVal (a b : HVec d) (ω : W d) : ℝ := ∑ μ, ∑ ν, a μ * ω μ ν * b ν

/-- The homogenized coefficients of an affine functional: `e x = ∑ μ, ehom e μ * hom x μ`. -/
noncomputable def ehom (e : (Fin d → ℝ) →ᵃ[ℝ] ℝ) : HVec d :=
  Matrix.vecCons (e 0) fun j => e.linear fun i => if j = i then (1 : ℝ) else 0

theorem ehom_dot (e : (Fin d → ℝ) →ᵃ[ℝ] ℝ) (x : Fin d → ℝ) :
    e x = ∑ μ, ehom e μ * hom x μ := by
  rw [Fin.sum_univ_succ]
  have hd := congrFun (AffineMap.decomp e) x
  simp only [Pi.add_apply] at hd
  rw [hd, LinearMap.pi_apply_eq_sum_univ e.linear x]
  simp only [ehom, hom, Matrix.cons_val_zero, Matrix.cons_val_succ, smul_eq_mul, mul_one]
  rw [add_comm]
  congr 1
  exact Finset.sum_congr rfl fun j _ => mul_comm _ _

/-- The value of the product effect `e ⊗ f` on a joint vector. -/
noncomputable def prodEffVal (e f : (Fin d → ℝ) →ᵃ[ℝ] ℝ) (ω : W d) : ℝ :=
  pairVal (ehom e) (ehom f) ω

/-- The maximal cone of two copies of `Ω`: nonnegative on every product of effects on `Ω`. -/
def maxCone (Ω : Set (Fin d → ℝ)) : Set (W d) :=
  {ω | ∀ e f, IsEffectOn Ω e → IsEffectOn Ω f → 0 ≤ prodEffVal e f ω}

/-- The joint states: the normalized vectors of the maximal cone. -/
def jointStates (Ω : Set (Fin d → ℝ)) : Set (W d) :=
  {ω | ω ∈ maxCone Ω ∧ ω 0 0 = 1}

/-- A joint vector is a product state of `Ω`. -/
def IsProduct (Ω : Set (Fin d → ℝ)) (ω : W d) : Prop :=
  ∃ x ∈ Ω, ∃ y ∈ Ω, ω = prodState x y

/-- `N` acting on the target index. -/
def actT (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (ω : W d) : W d := fun μ => homMap N (ω μ)

/-- `N` acting on the control index. -/
def actC (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (ω : W d) : W d :=
  fun μ ν => homMap N (fun κ => ω κ ν) μ

/-- The corners `corner z 0 = z`, `corner z 1 = −z`. -/
def corner (z : Fin d → ℝ) : Fin 2 → (Fin d → ℝ) := ![z, -z]

/-! ### §B — the frozen hypotheses -/

/-- The NOT of one copy: a linear involution preserving the body and inverting the corner axis. -/
structure IsNot (Ω : Set (Fin d → ℝ)) (z : Fin d → ℝ) (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) :
    Prop where
  unit : ∑ j, z j ^ 2 = 1
  invol : ∀ x, N (N x) = x
  preserves : ∀ x ∈ Ω, N x ∈ Ω
  flips : N z = -z

/-- The native-gate hypotheses on two identical copies of `Ω`, with one `N` in both relations. -/
structure NativeGate (Ω : Set (Fin d → ℝ)) (z : Fin d → ℝ) (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ))
    (G : W d ≃ₗ[ℝ] W d) : Prop where
  frame : ∀ a b : Fin 2,
    G (prodState (corner z a) (corner z b)) = prodState (corner z a) (corner z (a + b))
  posFwd : ∀ x ∈ Ω, ∀ y ∈ Ω, G (prodState x y) ∈ maxCone Ω
  posInv : ∀ x ∈ Ω, ∀ y ∈ Ω, G.symm (prodState x y) ∈ maxCone Ω
  relT : ∀ ω, actT N (G (actT N ω)) = G ω
  relC : ∀ ω, actC N (G (actC N ω)) = actT N (G ω)

/-- The entangling clause: some pure product input has an image that is an extreme joint state
and is not a product state. -/
def Entangling (Ω : Set (Fin d → ℝ)) (G : W d ≃ₗ[ℝ] W d) : Prop :=
  ∃ x ∈ Ω.extremePoints ℝ, ∃ y ∈ Ω.extremePoints ℝ,
    G (prodState x y) ∈ (jointStates Ω).extremePoints ℝ ∧ ¬ IsProduct Ω (G (prodState x y))

/-! ### §C — the eigenspace adapter -/

/-- A linear involution of a finite-dimensional space splits it into its `+1` and `−1` eigenspaces:
the dimensions add up to the dimension of the space. -/
theorem finrank_ker_sub_add_finrank_ker_add {V : Type*} [AddCommGroup V] [Module ℝ V]
    [FiniteDimensional ℝ V] (P : V →ₗ[ℝ] V) (hP : ∀ v, P (P v) = v) :
    Module.finrank ℝ (LinearMap.ker (P - LinearMap.id))
      + Module.finrank ℝ (LinearMap.ker (P + LinearMap.id)) = Module.finrank ℝ V := by
  have h := LinearMap.finrank_range_add_finrank_ker (P + LinearMap.id)
  have hr : LinearMap.range (P + LinearMap.id) = LinearMap.ker (P - LinearMap.id) := by
    ext v
    simp only [LinearMap.mem_range, LinearMap.mem_ker, LinearMap.sub_apply, LinearMap.add_apply,
      LinearMap.id_apply, sub_eq_zero]
    constructor
    · rintro ⟨w, rfl⟩
      rw [map_add, hP, add_comm]
    · intro hv
      refine ⟨(1 / 2 : ℝ) • v, ?_⟩
      rw [map_smul, hv, ← add_smul]
      norm_num
  rw [hr] at h
  omega

/-- The `+1` eigenspace of the homogenized NOT on the control space. -/
def plusSpace (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) : Submodule ℝ (HVec d) :=
  LinearMap.ker (homMap N - LinearMap.id)

/-- The `−1` eigenspace of the homogenized NOT on the control space. -/
def minusSpace (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) : Submodule ℝ (HVec d) :=
  LinearMap.ker (homMap N + LinearMap.id)

theorem mem_plusSpace {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {v : HVec d} :
    v ∈ plusSpace N ↔ homMap N v = v := by
  simp only [plusSpace, LinearMap.mem_ker, LinearMap.sub_apply, LinearMap.id_apply, sub_eq_zero]

theorem mem_minusSpace {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {v : HVec d} :
    v ∈ minusSpace N ↔ homMap N v = -v := by
  simp only [minusSpace, LinearMap.mem_ker, LinearMap.add_apply, LinearMap.id_apply,
    add_eq_zero_iff_eq_neg]

/-- The two eigenspaces of the homogenized NOT have dimensions summing to `d + 1`. -/
theorem finrank_plus_add_finrank_minus {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}
    (hN : ∀ x, N (N x) = x) :
    Module.finrank ℝ (plusSpace N) + Module.finrank ℝ (minusSpace N) = d + 1 := by
  have h := finrank_ker_sub_add_finrank_ker_add (homMap N) (homMap_homMap hN)
  rw [Module.finrank_fin_fun] at h
  exact h

/-- The unit vector `(1, 0)` lies in the `+1` eigenspace. -/
theorem hom_zero_mem_plusSpace (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) :
    hom (0 : Fin d → ℝ) ∈ plusSpace N := by
  rw [mem_plusSpace, homMap_hom, map_zero]

/-- The lifted corner `(0, z)` lies in the `−1` eigenspace. -/
theorem lift_corner_mem_minusSpace {Ω : Set (Fin d → ℝ)} {z : Fin d → ℝ}
    {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} (hN : IsNot Ω z N) :
    Matrix.vecCons (0 : ℝ) z ∈ minusSpace N := by
  rw [mem_minusSpace]
  funext i
  refine Fin.cases ?_ (fun j => ?_) i
  · simp
  · rw [homMap_succ, Matrix.tail_cons, hN.flips]
    simp

theorem one_le_finrank_plusSpace (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) :
    1 ≤ Module.finrank ℝ (plusSpace N) := by
  have hne : plusSpace N ≠ ⊥ := (Submodule.ne_bot_iff _).mpr
    ⟨hom 0, hom_zero_mem_plusSpace N, fun h0 => by
      have := congrFun h0 0
      simp at this⟩
  have : Module.finrank ℝ (plusSpace N) ≠ 0 := fun h0 => hne (Submodule.finrank_eq_zero.mp h0)
  omega

theorem one_le_finrank_minusSpace {Ω : Set (Fin d → ℝ)} {z : Fin d → ℝ}
    {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} (hN : IsNot Ω z N) :
    1 ≤ Module.finrank ℝ (minusSpace N) := by
  have hz : z ≠ 0 := by
    intro h0
    have := hN.unit
    simp [h0] at this
  have hne : minusSpace N ≠ ⊥ := (Submodule.ne_bot_iff _).mpr
    ⟨Matrix.vecCons 0 z, lift_corner_mem_minusSpace hN, fun h0 => hz (by
      funext j
      have := congrFun h0 j.succ
      simpa using this)⟩
  have : Module.finrank ℝ (minusSpace N) ≠ 0 := fun h0 => hne (Submodule.finrank_eq_zero.mp h0)
  omega

/-! ### §D — the parity count -/

/-- Equal eigenspace dimensions summing to `d + 1` exclude every even `d`. -/
theorem not_even_of_balanced {a b : ℕ} (hsum : a + b = d + 1) (hbal : a = b) : ¬ Even d := by
  rintro ⟨k, hk⟩
  omega

/-- The count in the form of `NativeGateBall.dim_of_bounds`: with `p + 1` and `q + 1` the two
eigenspace dimensions, `p = q` and `p + q + 1 = d`. -/
theorem split_of_balanced {a b : ℕ} (hsum : a + b = d + 1) (hbal : a = b) :
    (a - 1) = (b - 1) ∧ (a - 1) + (b - 1) + 1 = d := by
  omega

/-! ### §E — a NOT of the ball is an isometry and is self-adjoint -/

theorem sumsq_smul (c : ℝ) (x : Fin d → ℝ) : ∑ j, (c • x) j ^ 2 = c ^ 2 * ∑ j, x j ^ 2 := by
  simp only [Pi.smul_apply, smul_eq_mul, mul_pow, Finset.mul_sum]

theorem sumsq_apply_le_of_preserves {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}
    (hN : IsNot (eball d) z N) (x : Fin d → ℝ) : ∑ j, (N x) j ^ 2 ≤ ∑ j, x j ^ 2 := by
  have hs0 : 0 ≤ ∑ j, x j ^ 2 := Finset.sum_nonneg fun j _ => sq_nonneg _
  rcases eq_or_lt_of_le hs0 with h0 | hpos
  · have hx : x = 0 := by
      funext j
      have := (Finset.sum_eq_zero_iff_of_nonneg (fun j _ => sq_nonneg (x j))).1 h0.symm j
        (Finset.mem_univ _)
      exact (pow_eq_zero_iff two_ne_zero).mp this
    rw [hx, map_zero]
  · have hsq : Real.sqrt (∑ j, x j ^ 2) ^ 2 = ∑ j, x j ^ 2 := Real.sq_sqrt hs0
    have hsqpos : 0 < Real.sqrt (∑ j, x j ^ 2) := Real.sqrt_pos.2 hpos
    set c : ℝ := 1 / Real.sqrt (∑ j, x j ^ 2) with hc
    have hcpos : 0 < c := by rw [hc]; exact div_pos one_pos hsqpos
    have hc2 : c ^ 2 * ∑ j, x j ^ 2 = 1 := by
      rw [hc, div_pow, one_pow, hsq]
      exact one_div_mul_cancel (ne_of_gt hpos)
    have hmem : c • x ∈ eball d := by
      rw [mem_eball, sumsq_smul, hc2]
    have h1 := hN.preserves _ hmem
    rw [mem_eball, map_smul, sumsq_smul] at h1
    by_contra hlt
    have hlt' := not_le.mp hlt
    have := mul_lt_mul_of_pos_left hlt' (pow_pos hcpos 2)
    linarith

/-- A NOT of the ball preserves the sum of squares. -/
theorem sumsq_apply_eq {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}
    (hN : IsNot (eball d) z N) (x : Fin d → ℝ) : ∑ j, (N x) j ^ 2 = ∑ j, x j ^ 2 := by
  refine le_antisymm (sumsq_apply_le_of_preserves hN x) ?_
  have := sumsq_apply_le_of_preserves hN (N x)
  rwa [hN.invol] at this

theorem sumsq_add (u v : Fin d → ℝ) :
    ∑ j, (u + v) j ^ 2 = ∑ j, u j ^ 2 + 2 * ∑ j, u j * v j + ∑ j, v j ^ 2 := by
  rw [Finset.mul_sum, ← Finset.sum_add_distrib, ← Finset.sum_add_distrib]
  exact Finset.sum_congr rfl fun j _ => by simp only [Pi.add_apply]; ring

/-- Polarization: a NOT of the ball preserves the dot product. -/
theorem dot_apply_apply {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}
    (hN : IsNot (eball d) z N) (x y : Fin d → ℝ) :
    ∑ j, (N x) j * (N y) j = ∑ j, x j * y j := by
  have h := sumsq_apply_eq hN (x + y)
  have hx := sumsq_apply_eq hN x
  have hy := sumsq_apply_eq hN y
  rw [map_add, sumsq_add, sumsq_add] at h
  linarith

/-- A NOT of the ball is self-adjoint for the dot product. -/
theorem dot_apply {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}
    (hN : IsNot (eball d) z N) (x y : Fin d → ℝ) :
    ∑ j, (N x) j * y j = ∑ j, x j * (N y) j := by
  have := dot_apply_apply hN x (N y)
  rwa [hN.invol] at this

/-- The homogenized NOT is self-adjoint for the dot product of the control space. -/
theorem homMap_dot {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}
    (hN : IsNot (eball d) z N) (u v : HVec d) :
    ∑ μ, homMap N u μ * v μ = ∑ μ, u μ * homMap N v μ := by
  rw [Fin.sum_univ_succ, Fin.sum_univ_succ, homMap_zero, homMap_zero]
  congr 1
  simp only [homMap_succ]
  exact dot_apply hN (Matrix.vecTail u) (Matrix.vecTail v)

/-! ### §F — joint vectors as operators on the control space -/

/-- A joint vector as the operator `v ↦ ω *ᵥ v` on the control space. -/
def toOp (ω : W d) : HVec d →ₗ[ℝ] HVec d := Matrix.toLin' (Matrix.of ω)

/-- The joint vector of an operator (its matrix). -/
def fromOp (F : HVec d →ₗ[ℝ] HVec d) : W d := Matrix.of.symm (Matrix.toLin'.symm F)

theorem toOp_fromOp (F : HVec d →ₗ[ℝ] HVec d) : toOp (fromOp F) = F := by
  simp only [toOp, fromOp, Equiv.apply_symm_apply, LinearEquiv.apply_symm_apply]

theorem fromOp_toOp (ω : W d) : fromOp (toOp ω) = ω := by
  simp only [toOp, fromOp, LinearEquiv.symm_apply_apply, Equiv.symm_apply_apply]

theorem toOp_injective : Function.Injective (toOp : W d → HVec d →ₗ[ℝ] HVec d) :=
  fun ω₁ ω₂ h => by rw [← fromOp_toOp ω₁, h, fromOp_toOp]

theorem toOp_apply (ω : W d) (v : HVec d) (μ : Fin (d + 1)) :
    toOp ω v μ = ∑ ν, ω μ ν * v ν := by
  simp only [toOp, Matrix.toLin'_apply, Matrix.mulVec, dotProduct, Matrix.of_apply]

/-- `toOp` as a linear map. -/
def toOpLin : W d →ₗ[ℝ] (HVec d →ₗ[ℝ] HVec d) where
  toFun := toOp
  map_add' ω₁ ω₂ := by
    apply LinearMap.ext; intro v; funext μ
    simp only [toOp_apply, LinearMap.add_apply, Pi.add_apply, add_mul, Finset.sum_add_distrib]
  map_smul' c ω := by
    apply LinearMap.ext; intro v; funext μ
    simp only [toOp_apply, LinearMap.smul_apply, Pi.smul_apply, smul_eq_mul, RingHom.id_apply,
      Finset.mul_sum, mul_assoc]

theorem toOpLin_apply (ω : W d) : toOpLin ω = toOp ω := rfl

/-- `fromOp` as a linear map. -/
def fromOpLin : (HVec d →ₗ[ℝ] HVec d) →ₗ[ℝ] W d where
  toFun := fromOp
  map_add' F₁ F₂ := by
    apply toOp_injective
    rw [toOp_fromOp, ← toOpLin_apply, map_add, toOpLin_apply, toOpLin_apply, toOp_fromOp,
      toOp_fromOp]
  map_smul' c F := by
    apply toOp_injective
    rw [toOp_fromOp, ← toOpLin_apply, map_smul, toOpLin_apply, toOp_fromOp, RingHom.id_apply]

theorem fromOpLin_apply (F : HVec d →ₗ[ℝ] HVec d) : fromOpLin F = fromOp F := rfl

/-- The control action in operator form: left composition with the homogenized NOT. -/
theorem toOp_actC (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (ω : W d) :
    toOp (actC N ω) = homMap N ∘ₗ toOp ω := by
  apply LinearMap.ext; intro v
  have hcol : toOp ω v = ∑ ν, v ν • (fun κ => ω κ ν) := by
    funext κ
    simp only [toOp_apply, Finset.sum_apply, Pi.smul_apply, smul_eq_mul]
    exact Finset.sum_congr rfl fun ν _ => mul_comm _ _
  rw [LinearMap.comp_apply, hcol, map_sum]
  funext μ
  simp only [toOp_apply, actC, Finset.sum_apply, map_smul, Pi.smul_apply, smul_eq_mul]
  exact Finset.sum_congr rfl fun ν _ => mul_comm _ _

/-- The target action in operator form: right composition with the homogenized NOT. -/
theorem toOp_actT {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}
    (hN : IsNot (eball d) z N) (ω : W d) : toOp (actT N ω) = toOp ω ∘ₗ homMap N := by
  apply LinearMap.ext; intro v
  funext μ
  simp only [toOp_apply, LinearMap.comp_apply, actT]
  exact homMap_dot hN (ω μ) v

theorem actT_actT {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} (hN : ∀ x, N (N x) = x) (ω : W d) :
    actT N (actT N ω) = ω := by
  funext μ
  simp only [actT, homMap_homMap hN]

theorem actC_actC {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} (hN : ∀ x, N (N x) = x) (ω : W d) :
    actC N (actC N ω) = ω := by
  funext μ ν
  have : (fun κ => actC N ω κ ν) = homMap N (fun κ => ω κ ν) := rfl
  simp only [actC]
  rw [this, homMap_homMap hN]

/-! ### §G — the gate in operator form -/

/-- The gate transported to operators on the control space. -/
def opGate (G : W d ≃ₗ[ℝ] W d) : (HVec d →ₗ[ℝ] HVec d) →ₗ[ℝ] (HVec d →ₗ[ℝ] HVec d) :=
  toOpLin ∘ₗ G.toLinearMap ∘ₗ fromOpLin

theorem opGate_toOp (G : W d ≃ₗ[ℝ] W d) (ω : W d) : opGate G (toOp ω) = toOp (G ω) := by
  simp only [opGate, LinearMap.comp_apply, fromOpLin_apply, fromOp_toOp, toOpLin_apply,
    LinearEquiv.coe_coe]

/-- The target relation in operator form. -/
theorem opGate_comp_homMap {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}
    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G)
    (F : HVec d →ₗ[ℝ] HVec d) : opGate G (F ∘ₗ homMap N) = opGate G F ∘ₗ homMap N := by
  obtain ⟨ω, rfl⟩ : ∃ ω, F = toOp ω := ⟨fromOp F, (toOp_fromOp F).symm⟩
  have h : G (actT N ω) = actT N (G ω) := by
    rw [← hG.relT ω, actT_actT hN.invol]
  rw [← toOp_actT hN, opGate_toOp, opGate_toOp, h, toOp_actT hN]

/-- The control relation in operator form. -/
theorem opGate_homMap_comp {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}
    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G)
    (F : HVec d →ₗ[ℝ] HVec d) :
    opGate G (homMap N ∘ₗ F) = homMap N ∘ₗ opGate G F ∘ₗ homMap N := by
  obtain ⟨ω, rfl⟩ : ∃ ω, F = toOp ω := ⟨fromOp F, (toOp_fromOp F).symm⟩
  have h : G (actC N ω) = actC N (actT N (G ω)) := by
    rw [← hG.relC ω, actC_actC hN.invol]
  rw [← toOp_actC, opGate_toOp, opGate_toOp, h, toOp_actC, toOp_actT hN]

/-! ### §H — the projection onto the `−1` eigenspace -/

/-- The projection `v ↦ (v − N v)/2` onto the `−1` eigenspace. -/
def projMinus {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} (hN : ∀ x, N (N x) = x) :
    HVec d →ₗ[ℝ] minusSpace N :=
  LinearMap.codRestrict (minusSpace N) ((1 / 2 : ℝ) • (LinearMap.id - homMap N)) fun v => by
    rw [mem_minusSpace]
    simp only [LinearMap.smul_apply, LinearMap.sub_apply, LinearMap.id_apply, map_smul, map_sub,
      homMap_homMap hN]
    module

theorem projMinus_apply {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} (hN : ∀ x, N (N x) = x) (v : HVec d) :
    (projMinus hN v : HVec d) = (1 / 2 : ℝ) • (v - homMap N v) := rfl

theorem projMinus_of_mem {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} (hN : ∀ x, N (N x) = x) {u : HVec d}
    (hu : u ∈ minusSpace N) : (projMinus hN u : HVec d) = u := by
  rw [projMinus_apply, mem_minusSpace.mp hu, sub_neg_eq_add, ← two_smul ℝ u, smul_smul]
  norm_num

theorem projMinus_homMap {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} (hN : ∀ x, N (N x) = x)
    (v : HVec d) : projMinus hN (homMap N v) = - projMinus hN v := by
  apply Subtype.ext
  simp only [Submodule.coe_neg, projMinus_apply, homMap_homMap hN]
  module

/-! ### §I — parity: the eigenspaces of the common NOT are balanced -/

/-- Operators from the `−1` eigenspace to the control space. -/
abbrev OpSpace (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) := minusSpace N →ₗ[ℝ] HVec d

/-- Left composition with the homogenized NOT. -/
def Pop (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) : OpSpace N →ₗ[ℝ] OpSpace N :=
  LinearMap.llcomp ℝ (minusSpace N) (HVec d) (HVec d) (homMap N)

theorem Pop_apply (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (f : OpSpace N) (u : minusSpace N) :
    Pop N f u = homMap N (f u) :=
  LinearMap.llcomp_apply _ _ _

/-- The gate read on operators from the `−1` eigenspace: extend by the projection, apply the gate,
restrict to the eigenspace. -/
def Lop (G : W d ≃ₗ[ℝ] W d) {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} (hN : ∀ x, N (N x) = x) :
    OpSpace N →ₗ[ℝ] OpSpace N :=
  LinearMap.lcomp ℝ (HVec d) (minusSpace N).subtype ∘ₗ opGate G ∘ₗ
    LinearMap.lcomp ℝ (HVec d) (projMinus hN)

theorem Lop_apply (G : W d ≃ₗ[ℝ] W d) {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} (hN : ∀ x, N (N x) = x)
    (f : OpSpace N) (u : minusSpace N) :
    Lop G hN f u = opGate G (f ∘ₗ projMinus hN) u := rfl

theorem Lop_anti {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}
    (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) (f : OpSpace N) :
    Lop G hN.invol (Pop N f) = - Pop N (Lop G hN.invol f) := by
  apply LinearMap.ext; intro u
  rw [LinearMap.neg_apply, Lop_apply, Pop_apply, Lop_apply]
  have hcomp : Pop N f ∘ₗ projMinus hN.invol = homMap N ∘ₗ (f ∘ₗ projMinus hN.invol) := by
    apply LinearMap.ext; intro v
    simp only [LinearMap.comp_apply, Pop_apply]
  rw [hcomp, opGate_homMap_comp hN hG, LinearMap.comp_apply, LinearMap.comp_apply,
    mem_minusSpace.mp u.2]
  simp only [map_neg]

theorem Lop_eq_zero {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}
    (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) (f : OpSpace N)
    (hf : Lop G hN.invol f = 0) : f = 0 := by
  set F : HVec d →ₗ[ℝ] HVec d := f ∘ₗ projMinus hN.invol with hF
  have hminus : ∀ u ∈ minusSpace N, opGate G F u = 0 := by
    intro u hu
    have := LinearMap.congr_fun hf ⟨u, hu⟩
    rwa [Lop_apply, LinearMap.zero_apply] at this
  have hFN : F ∘ₗ homMap N = -F := by
    apply LinearMap.ext; intro v
    simp only [hF, LinearMap.comp_apply, LinearMap.neg_apply, projMinus_homMap, map_neg]
  have hplus : ∀ v ∈ plusSpace N, opGate G F v = 0 := by
    intro v hv
    have h1 := LinearMap.congr_fun (opGate_comp_homMap hN hG F) v
    rw [hFN, map_neg, LinearMap.neg_apply, LinearMap.comp_apply, mem_plusSpace.mp hv] at h1
    have h2 : (2 : ℝ) • opGate G F v = 0 := by
      rw [two_smul]
      nth_rewrite 1 [← h1]
      exact neg_add_cancel _
    exact (smul_eq_zero.mp h2).resolve_left two_ne_zero
  have hall : opGate G F = 0 := by
    apply LinearMap.ext; intro v
    have hdecomp : v = (1 / 2 : ℝ) • (v + homMap N v) + (1 / 2 : ℝ) • (v - homMap N v) := by
      module
    have hp : (1 / 2 : ℝ) • (v + homMap N v) ∈ plusSpace N := by
      rw [mem_plusSpace, map_smul, map_add, homMap_homMap hN.invol, add_comm]
    have hm : (1 / 2 : ℝ) • (v - homMap N v) ∈ minusSpace N := (projMinus hN.invol v).2
    rw [LinearMap.zero_apply, hdecomp, map_add, hplus _ hp, hminus _ hm, add_zero]
  have hGF : G (fromOp F) = 0 := by
    apply toOp_injective
    rw [← opGate_toOp, toOp_fromOp, hall, ← toOpLin_apply, map_zero]
  have hF0 : F = 0 := by
    have h0 : fromOp F = 0 := G.injective (by rw [hGF, map_zero])
    rw [← toOp_fromOp F, h0, ← toOpLin_apply, map_zero]
  apply LinearMap.ext; intro u
  have := LinearMap.congr_fun hF0 u
  rw [hF, LinearMap.comp_apply, LinearMap.zero_apply] at this
  rw [LinearMap.zero_apply, ← this]
  congr 1
  exact Subtype.ext (projMinus_of_mem hN.invol u.2).symm

theorem Lop_injective {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}
    (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) :
    Function.Injective (Lop G hN.invol) :=
  LinearMap.ker_eq_bot.mp (LinearMap.ker_eq_bot'.mpr fun f hf => Lop_eq_zero hN hG f hf)

/-- Operators with values in a subspace: the kernel of a pointwise test has the dimension of the
operator space into the subspace. -/
theorem finrank_ker_eq_of_pointwise {M E : Type*} [AddCommGroup M] [Module ℝ M]
    [FiniteDimensional ℝ M] [AddCommGroup E] [Module ℝ E] [FiniteDimensional ℝ E]
    (S : Submodule ℝ E) (T : (M →ₗ[ℝ] E) →ₗ[ℝ] (M →ₗ[ℝ] E))
    (hT : ∀ f, T f = 0 ↔ ∀ u, f u ∈ S) :
    Module.finrank ℝ (LinearMap.ker T) = Module.finrank ℝ M * Module.finrank ℝ S := by
  let A : LinearMap.ker T →ₗ[ℝ] (M →ₗ[ℝ] S) :=
    { toFun := fun f => LinearMap.codRestrict S f.1 ((hT f.1).1 (LinearMap.mem_ker.mp f.2))
      map_add' := fun f g => LinearMap.ext fun u => rfl
      map_smul' := fun c f => LinearMap.ext fun u => rfl }
  let B : (M →ₗ[ℝ] S) →ₗ[ℝ] LinearMap.ker T :=
    { toFun := fun g => ⟨S.subtype ∘ₗ g, LinearMap.mem_ker.mpr ((hT _).2 fun u => (g u).2)⟩
      map_add' := fun g h => Subtype.ext (LinearMap.ext fun u => rfl)
      map_smul' := fun c g => Subtype.ext (LinearMap.ext fun u => rfl) }
  have hA : Function.Injective A := by
    intro f g hfg
    apply Subtype.ext; apply LinearMap.ext; intro u
    exact congrArg Subtype.val (LinearMap.congr_fun hfg u)
  have hB : Function.Injective B := by
    intro g h hgh
    apply LinearMap.ext; intro u; apply Subtype.ext
    exact LinearMap.congr_fun (congrArg Subtype.val hgh) u
  calc Module.finrank ℝ (LinearMap.ker T) = Module.finrank ℝ (M →ₗ[ℝ] S) :=
        le_antisymm (LinearMap.finrank_le_finrank_of_injective hA)
          (LinearMap.finrank_le_finrank_of_injective hB)
    _ = Module.finrank ℝ M * Module.finrank ℝ S := Module.finrank_linearMap

theorem finrank_ker_Pop_sub (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) :
    Module.finrank ℝ (LinearMap.ker (Pop N - LinearMap.id))
      = Module.finrank ℝ (minusSpace N) * Module.finrank ℝ (plusSpace N) :=
  finrank_ker_eq_of_pointwise (plusSpace N) (Pop N - LinearMap.id) fun f => by
    constructor
    · intro h u
      rw [mem_plusSpace]
      have := LinearMap.congr_fun h u
      simpa only [LinearMap.sub_apply, LinearMap.id_apply, Pop_apply, LinearMap.zero_apply,
        sub_eq_zero] using this
    · intro h
      apply LinearMap.ext; intro u
      simp only [LinearMap.sub_apply, LinearMap.id_apply, Pop_apply, LinearMap.zero_apply,
        sub_eq_zero]
      exact mem_plusSpace.mp (h u)

theorem finrank_ker_Pop_add (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) :
    Module.finrank ℝ (LinearMap.ker (Pop N + LinearMap.id))
      = Module.finrank ℝ (minusSpace N) * Module.finrank ℝ (minusSpace N) :=
  finrank_ker_eq_of_pointwise (minusSpace N) (Pop N + LinearMap.id) fun f => by
    constructor
    · intro h u
      rw [mem_minusSpace]
      have := LinearMap.congr_fun h u
      simpa only [LinearMap.add_apply, LinearMap.id_apply, Pop_apply, LinearMap.zero_apply,
        add_eq_zero_iff_eq_neg] using this
    · intro h
      apply LinearMap.ext; intro u
      simp only [LinearMap.add_apply, LinearMap.id_apply, Pop_apply, LinearMap.zero_apply,
        add_eq_zero_iff_eq_neg]
      exact mem_minusSpace.mp (h u)

/-- **Parity (S5) from the frozen hypotheses.** The `+1` and `−1` eigenspaces of the homogenized
common NOT on the control space have the same dimension. -/
theorem finrank_plus_eq_finrank_minus {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}
    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) :
    Module.finrank ℝ (plusSpace N) = Module.finrank ℝ (minusSpace N) := by
  have hpar := NativeGateBall.parity (Pop N) (Lop G hN.invol) (Lop_injective hN hG)
    (Lop_anti hN hG)
  rw [finrank_ker_Pop_sub, finrank_ker_Pop_add] at hpar
  exact Nat.eq_of_mul_eq_mul_left (one_le_finrank_minusSpace hN) hpar

/-! ### §J — the exclusions -/

/-- No even dimension carries a native gate. -/
theorem not_even_of_nativeGate {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}
    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) :
    ¬ Even d :=
  not_even_of_balanced (finrank_plus_add_finrank_minus hN.invol)
    (finrank_plus_eq_finrank_minus hN hG)

theorem ne_two_of_nativeGate {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}
    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) : d ≠ 2 :=
  fun h => not_even_of_nativeGate hN hG ⟨1, by omega⟩

theorem ne_four_of_nativeGate {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}
    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) : d ≠ 4 :=
  fun h => not_even_of_nativeGate hN hG ⟨2, by omega⟩

/-- The data the written S1–S2–S4 reduction extracts from a native gate whose `+1` eigenspace has
tangent dimension `p`: the `E₊` blocks `A`, `B` on a target index set of size `m`, antisymmetric
in the pair index, with the Lorentz positivity of `I + Γ` at `t = ±eᵢ` against every unit effect
and one nonzero entry. The reduction from `NativeGate` to this data is a written proof and is not
certified in this module; the data is the hypothesis of `NativeGateBall.p_le_one`. -/
structure BlockData (p : ℕ) : Prop where
  blocks : ∃ (m : ℕ) (A : Fin p → Matrix (Fin m) (Fin m) ℝ)
      (B : Fin p → Fin p → Matrix (Fin m) (Fin m) ℝ),
    (∀ r s, B r s = - B s r) ∧
    (∀ k l : Fin m, ∀ i : Fin p, ∀ s : ℝ, (s = 1 ∨ s = -1) →
      ∀ b : Fin p → ℝ, (∑ j, b j ^ 2) = 1 →
        0 ≤ (1 + s * A i k l)
          + ∑ j, b j * (A j k l + s * ((if j = i then (1:ℝ) else 0) + B j i k l))) ∧
    (∃ r k l, A r k l ≠ 0)

theorem p_le_one_of_blockData {p : ℕ} (h : BlockData p) : p ≤ 1 := by
  obtain ⟨m, A, B, hB, hpos, hne⟩ := h.blocks
  exact NativeGateBall.p_le_one p m A B hB hpos hne

/-- The tangent dimension of the `+1` eigenspace: its dimension less the unit direction. -/
noncomputable def tangentPlus (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) : ℕ :=
  Module.finrank ℝ (plusSpace N) - 1

/-- **The selector, conditional on the block reduction.** Two identical copies of the Euclidean
ball with a native gate whose block data is as the written reduction states have dimension one or
three. Parity is proved from the frozen hypotheses; the block data is the named premise. -/
theorem dim_of_nativeGate {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}
    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G)
    (hB : BlockData (tangentPlus N)) : d = 1 ∨ d = 3 := by
  have hsum := finrank_plus_add_finrank_minus hN.invol
  have hbal := finrank_plus_eq_finrank_minus hN hG
  have hp := one_le_finrank_plusSpace N
  have hle := p_le_one_of_blockData hB
  exact NativeGateBall.dim_of_bounds (tangentPlus N) (Module.finrank ℝ (minusSpace N) - 1) d hle
    (by unfold tangentPlus; omega) (by unfold tangentPlus; omega)

theorem ne_five_of_nativeGate {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}
    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G)
    (hB : BlockData (tangentPlus N)) : d ≠ 5 := by
  intro h
  rcases dim_of_nativeGate hN hG hB with h1 | h2 <;> omega

theorem ne_seven_of_nativeGate {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}
    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G)
    (hB : BlockData (tangentPlus N)) : d ≠ 7 := by
  intro h
  rcases dim_of_nativeGate hN hG hB with h1 | h2 <;> omega

end CompositeDimension
end OIBridge

#print axioms OIBridge.CompositeDimension.ehom_dot
#print axioms OIBridge.CompositeDimension.homMap_homMap
#print axioms OIBridge.CompositeDimension.finrank_ker_sub_add_finrank_ker_add
#print axioms OIBridge.CompositeDimension.finrank_plus_add_finrank_minus
#print axioms OIBridge.CompositeDimension.one_le_finrank_plusSpace
#print axioms OIBridge.CompositeDimension.one_le_finrank_minusSpace
#print axioms OIBridge.CompositeDimension.not_even_of_balanced
#print axioms OIBridge.CompositeDimension.split_of_balanced
#print axioms OIBridge.CompositeDimension.sumsq_apply_eq
#print axioms OIBridge.CompositeDimension.homMap_dot
#print axioms OIBridge.CompositeDimension.toOp_actC
#print axioms OIBridge.CompositeDimension.toOp_actT
#print axioms OIBridge.CompositeDimension.opGate_comp_homMap
#print axioms OIBridge.CompositeDimension.opGate_homMap_comp
#print axioms OIBridge.CompositeDimension.Lop_anti
#print axioms OIBridge.CompositeDimension.Lop_injective
#print axioms OIBridge.CompositeDimension.finrank_ker_eq_of_pointwise
#print axioms OIBridge.CompositeDimension.finrank_plus_eq_finrank_minus
#print axioms OIBridge.CompositeDimension.not_even_of_nativeGate
#print axioms OIBridge.CompositeDimension.ne_two_of_nativeGate
#print axioms OIBridge.CompositeDimension.ne_four_of_nativeGate
#print axioms OIBridge.CompositeDimension.p_le_one_of_blockData
#print axioms OIBridge.CompositeDimension.dim_of_nativeGate
#print axioms OIBridge.CompositeDimension.ne_five_of_nativeGate
#print axioms OIBridge.CompositeDimension.ne_seven_of_nativeGate
