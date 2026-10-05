/-
  OIBridge/CompositeDimension.lean — round DIM-1: the composite dimension selector.

  Two identical copies of the coordinate Euclidean ball `eball d` of `TransitiveBody`, joined on the
  bilinear carrier `W d` (a real function of two homogenized indices), carry one common NOT `N` and a
  reversible gate `G` with the classical CNOT action on the corners `±z`, the target relation
  `(I⊗N) G (I⊗N) = G`, the control relation `(N⊗I) G (N⊗I) = (I⊗N) G`, and two-sided positivity on the
  maximal cone. Local tomography, the common NOT, the reversible CNOT-frame action, two-sided
  positivity and the entangling clause are named premises; no complex structure, no
  nonlocal-correlation inequality, no drive, no one-parameter motion and no order statement is used
  or claimed.

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
  show homMap N (fun κ => actC N ω κ ν) μ = ω μ ν
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
noncomputable def projMinus {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} (hN : ∀ x, N (N x) = x) :
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
noncomputable def Lop (G : W d ≃ₗ[ℝ] W d) {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}
    (hN : ∀ x, N (N x) = x) :
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
      rw [mem_plusSpace, map_smul, map_add, homMap_homMap hN.invol, add_comm (homMap N v) v]
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
    _ = Module.finrank ℝ M * Module.finrank ℝ S := Module.finrank_linearMap ℝ ℝ M S

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

/-! ### §K — survival: the `d = 3` gate -/

/-- The sign of the `d = 3` gate on the homogenized index pair: `−1` at `(1, 3)` and `(2, 2)`. -/
def sgn (μ ν : Fin 4) : ℝ := if (μ = 1 ∧ ν = 3) ∨ (μ = 2 ∧ ν = 2) then -1 else 1

/-- The control index read by the `d = 3` gate at an index pair. -/
def pc : Fin 4 → Fin 4 → Fin 4
  | 0, 0 => 0 | 0, 1 => 0 | 0, 2 => 3 | 0, 3 => 3
  | 1, 0 => 1 | 1, 1 => 1 | 1, 2 => 2 | 1, 3 => 2
  | 2, 0 => 2 | 2, 1 => 2 | 2, 2 => 1 | 2, 3 => 1
  | 3, 0 => 3 | 3, 1 => 3 | 3, 2 => 0 | 3, 3 => 0

/-- The target index read by the `d = 3` gate at an index pair. -/
def pt : Fin 4 → Fin 4 → Fin 4
  | 0, 0 => 0 | 0, 1 => 1 | 0, 2 => 2 | 0, 3 => 3
  | 1, 0 => 1 | 1, 1 => 0 | 1, 2 => 3 | 1, 3 => 2
  | 2, 0 => 1 | 2, 1 => 0 | 2, 2 => 3 | 2, 3 => 2
  | 3, 0 => 0 | 3, 1 => 1 | 3, 2 => 2 | 3, 3 => 3

/-- The `d = 3` gate as a function: a signed permutation of the sixteen entries. -/
def cnotFun (ω : W 3) : W 3 := fun μ ν => sgn μ ν * ω (pc μ ν) (pt μ ν)

theorem cnotFun_apply (ω : W 3) (μ ν : Fin 4) : cnotFun ω μ ν = sgn μ ν * ω (pc μ ν) (pt μ ν) := rfl

theorem pc_pc : ∀ μ ν : Fin 4, pc (pc μ ν) (pt μ ν) = μ := by decide

theorem pt_pt : ∀ μ ν : Fin 4, pt (pc μ ν) (pt μ ν) = ν := by decide

theorem sgn_mul_sgn : ∀ μ ν : Fin 4, sgn μ ν * sgn (pc μ ν) (pt μ ν) = 1 := by
  intro μ ν
  fin_cases μ <;> fin_cases ν <;> simp +decide [sgn, pc, pt]

theorem cnotFun_cnotFun (ω : W 3) : cnotFun (cnotFun ω) = ω := by
  funext μ ν
  rw [cnotFun_apply, cnotFun_apply, pc_pc, pt_pt, ← mul_assoc, sgn_mul_sgn, one_mul]

/-- The `d = 3` gate as a linear equivalence of the joint carrier. -/
def cnot : W 3 ≃ₗ[ℝ] W 3 where
  toFun := cnotFun
  invFun := cnotFun
  map_add' ω₁ ω₂ := by
    funext μ ν
    simp only [cnotFun_apply, Pi.add_apply, mul_add]
  map_smul' c ω := by
    funext μ ν
    simp only [cnotFun_apply, Pi.smul_apply, smul_eq_mul, RingHom.id_apply]
    ring
  left_inv := cnotFun_cnotFun
  right_inv := cnotFun_cnotFun

theorem cnot_apply (ω : W 3) : cnot ω = cnotFun ω := rfl

theorem cnot_symm_apply (ω : W 3) : cnot.symm ω = cnotFun ω := rfl

/-- The corner axis of the `d = 3` witness. -/
def z3 : Fin 3 → ℝ := ![0, 0, 1]

/-- The common NOT of the `d = 3` witness: the reflection fixing the first coordinate and
inverting the other two. -/
def nflip : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ) where
  toFun x := fun i => (![1, -1, -1] : Fin 3 → ℝ) i * x i
  map_add' x y := by funext i; simp only [Pi.add_apply, mul_add]
  map_smul' c x := by funext i; simp only [Pi.smul_apply, smul_eq_mul, RingHom.id_apply]; ring

theorem nflip_apply (x : Fin 3 → ℝ) (i : Fin 3) : nflip x i = (![1, -1, -1] : Fin 3 → ℝ) i * x i :=
  rfl

@[simp] theorem nflip_zero' (x : Fin 3 → ℝ) : nflip x 0 = x 0 := by show 1 * x 0 = x 0; ring
@[simp] theorem nflip_one (x : Fin 3 → ℝ) : nflip x 1 = -x 1 := by show -1 * x 1 = -x 1; ring
@[simp] theorem nflip_two (x : Fin 3 → ℝ) : nflip x 2 = -x 2 := by show -1 * x 2 = -x 2; ring

@[simp] theorem homMap_nflip_zero (v : HVec 3) : homMap nflip v 0 = v 0 := rfl
@[simp] theorem homMap_nflip_one (v : HVec 3) : homMap nflip v 1 = v 1 := by
  show 1 * v 1 = v 1; ring
@[simp] theorem homMap_nflip_two (v : HVec 3) : homMap nflip v 2 = -v 2 := by
  show -1 * v 2 = -v 2; ring
@[simp] theorem homMap_nflip_three (v : HVec 3) : homMap nflip v 3 = -v 3 := by
  show -1 * v 3 = -v 3; ring

@[simp] theorem hom_one' (x : Fin 3 → ℝ) : hom x 1 = x 0 := rfl
@[simp] theorem hom_two' (x : Fin 3 → ℝ) : hom x 2 = x 1 := rfl
@[simp] theorem hom_three' (x : Fin 3 → ℝ) : hom x 3 = x 2 := rfl

@[simp] theorem z3_zero : z3 0 = 0 := rfl
@[simp] theorem z3_one : z3 1 = 0 := rfl
@[simp] theorem z3_two : z3 2 = 1 := rfl

theorem corner_zero (z : Fin 3 → ℝ) : corner z 0 = z := rfl
theorem corner_one (z : Fin 3 → ℝ) : corner z 1 = -z := rfl

theorem actT_apply (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (ω : W d) (μ ν : Fin (d + 1)) :
    actT N ω μ ν = homMap N (ω μ) ν := rfl

theorem actC_apply (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (ω : W d) (μ ν : Fin (d + 1)) :
    actC N ω μ ν = homMap N (fun κ => ω κ ν) μ := rfl

theorem prodState_apply (x y : Fin d → ℝ) (μ ν : Fin (d + 1)) :
    prodState x y μ ν = hom x μ * hom y ν := rfl

/-- `nflip` is a NOT of the ball with axis `z3`. -/
theorem isNot_nflip : IsNot (eball 3) z3 nflip where
  unit := by simp [Fin.sum_univ_three]
  invol x := by funext i; fin_cases i <;> simp
  preserves x hx := by
    rw [mem_eball, Fin.sum_univ_three] at hx ⊢
    simp only [nflip_zero', nflip_one, nflip_two, neg_sq]
    exact hx
  flips := by funext i; fin_cases i <;> simp

/-- The frame condition of the `d = 3` gate. -/
theorem cnot_frame (a b : Fin 2) :
    cnot (prodState (corner z3 a) (corner z3 b)) = prodState (corner z3 a) (corner z3 (a + b)) := by
  fin_cases a <;> fin_cases b <;> funext μ ν <;> fin_cases μ <;> fin_cases ν <;>
    simp +decide [cnot_apply, cnotFun_apply, sgn, pc, pt, prodState_apply, corner_zero, corner_one]

/-- The target relation of the `d = 3` gate. -/
theorem cnot_relT (ω : W 3) : actT nflip (cnot (actT nflip ω)) = cnot ω := by
  funext μ ν
  fin_cases μ <;> fin_cases ν <;>
    simp +decide [actT_apply, cnot_apply, cnotFun_apply, sgn, pc, pt]

/-- The control relation of the `d = 3` gate. -/
theorem cnot_relC (ω : W 3) : actC nflip (cnot (actC nflip ω)) = actT nflip (cnot ω) := by
  funext μ ν
  fin_cases μ <;> fin_cases ν <;>
    simp +decide [actC_apply, actT_apply, cnot_apply, cnotFun_apply, sgn, pc, pt]

/-! ### §L — the cone of homogenized effect vectors of the ball -/

/-- The cone of homogenized vectors whose unit coordinate dominates the norm of the rest: the
homogenized coefficients of the effects of the ball, up to scale. -/
def Lor (v : HVec d) : Prop := 0 ≤ v 0 ∧ ∑ j, v j.succ ^ 2 ≤ v 0 ^ 2

theorem lor_smul {v : HVec d} (hv : Lor v) {c : ℝ} (hc : 0 ≤ c) : Lor (c • v) := by
  refine ⟨mul_nonneg hc hv.1, ?_⟩
  simp only [Pi.smul_apply, smul_eq_mul, mul_pow, ← Finset.mul_sum]
  exact mul_le_mul_of_nonneg_left hv.2 (sq_nonneg c)

/-- A vector of the cone paired with a unit-ball point: the tail pairing is bounded by the head. -/
theorem lor_pair_bound {v : HVec d} (hv : Lor v) {x : Fin d → ℝ} (hx : x ∈ eball d) :
    -v 0 ≤ ∑ j, v j.succ * x j ∧ ∑ j, v j.succ * x j ≤ v 0 := by
  have hcs := Finset.sum_mul_sq_le_sq_mul_sq Finset.univ (fun j => v j.succ) x
  rw [mem_eball] at hx
  have h1 : (∑ j, v j.succ * x j) ^ 2 ≤ v 0 ^ 2 := by
    refine le_trans hcs ?_
    calc (∑ j, v j.succ ^ 2) * ∑ j, x j ^ 2 ≤ v 0 ^ 2 * 1 :=
          mul_le_mul hv.2 hx (Finset.sum_nonneg fun j _ => sq_nonneg _) (sq_nonneg _)
      _ = v 0 ^ 2 := mul_one _
  exact abs_le_of_sq_le_sq' h1 hv.1

/-- The affine functional with the given homogenized coefficients. -/
noncomputable def affOf (v : HVec d) : (Fin d → ℝ) →ᵃ[ℝ] ℝ where
  toFun x := v 0 + ∑ j, v j.succ * x j
  linear := ∑ j, v j.succ • (LinearMap.proj j : (Fin d → ℝ) →ₗ[ℝ] ℝ)
  map_vadd' p w := by
    simp only [vadd_eq_add, Pi.add_apply, mul_add, Finset.sum_add_distrib, LinearMap.sum_apply,
      LinearMap.smul_apply, LinearMap.proj_apply, smul_eq_mul]
    ring

theorem affOf_apply (v : HVec d) (x : Fin d → ℝ) : affOf v x = v 0 + ∑ j, v j.succ * x j := rfl

theorem affOf_linear (v : HVec d) :
    (affOf v).linear = ∑ j, v j.succ • (LinearMap.proj j : (Fin d → ℝ) →ₗ[ℝ] ℝ) := rfl

/-- The homogenized coefficients of `affOf v` are `v`. -/
theorem ehom_affOf (v : HVec d) : ehom (affOf v) = v := by
  funext μ
  refine Fin.cases ?_ (fun j => ?_) μ
  · show v 0 + ∑ j, v j.succ * (0 : Fin d → ℝ) j = v 0
    simp
  · show (affOf v).linear (fun i => if j = i then (1 : ℝ) else 0) = v j.succ
    rw [affOf_linear]
    simp only [LinearMap.sum_apply, LinearMap.smul_apply, LinearMap.proj_apply, smul_eq_mul,
      mul_ite, mul_one, mul_zero]
    rw [Finset.sum_ite_eq]
    simp

/-- A cone vector with head at most one half is the coefficient vector of an effect of the ball. -/
theorem isEffectOn_affOf {v : HVec d} (hv : Lor v) (hv0 : v 0 ≤ 1 / 2) :
    IsEffectOn (eball d) (affOf v) := by
  intro x hx
  obtain ⟨h1, h2⟩ := lor_pair_bound hv hx
  rw [affOf_apply]
  constructor <;> linarith

theorem ehom_zero_eq (e : (Fin d → ℝ) →ᵃ[ℝ] ℝ) : ehom e 0 = e 0 := by
  have h := ehom_dot e 0
  rw [Fin.sum_univ_succ, hom_zero, mul_one] at h
  simp only [hom_succ, Pi.zero_apply, mul_zero, Finset.sum_const_zero, add_zero] at h
  exact h.symm

/-- The homogenized coefficients of an effect of the ball lie in the cone. -/
theorem lor_ehom {e : (Fin d → ℝ) →ᵃ[ℝ] ℝ} (he : IsEffectOn (eball d) e) : Lor (ehom e) := by
  have h0mem : (0 : Fin d → ℝ) ∈ eball d := by rw [mem_eball]; simp
  have he0 : 0 ≤ ehom e 0 := by rw [ehom_zero_eq]; exact (he 0 h0mem).1
  refine ⟨he0, ?_⟩
  obtain ⟨s, hs⟩ : ∃ s : ℝ, s = ∑ j, ehom e j.succ ^ 2 := ⟨_, rfl⟩
  rw [← hs]
  have hs0 : 0 ≤ s := hs ▸ Finset.sum_nonneg fun j _ => sq_nonneg _
  rcases eq_or_lt_of_le hs0 with h0 | hpos
  · rw [← h0]; exact sq_nonneg _
  · have hsq : Real.sqrt s * Real.sqrt s = s := Real.mul_self_sqrt hs0
    have hne : Real.sqrt s ≠ 0 := ne_of_gt (Real.sqrt_pos.2 hpos)
    have hxmem : (fun j => -(1 / Real.sqrt s) * ehom e j.succ) ∈ eball d := by
      rw [mem_eball]
      calc ∑ j, (-(1 / Real.sqrt s) * ehom e j.succ) ^ 2
          = ∑ j, (1 / Real.sqrt s) ^ 2 * ehom e j.succ ^ 2 :=
            Finset.sum_congr rfl fun j _ => by ring
        _ = (1 / Real.sqrt s) ^ 2 * ∑ j, ehom e j.succ ^ 2 := (Finset.mul_sum _ _ _).symm
        _ = (1 / Real.sqrt s) ^ 2 * s := by rw [hs]
        _ = (1 / Real.sqrt s) ^ 2 * (Real.sqrt s * Real.sqrt s) := by rw [hsq]
        _ = (1 / Real.sqrt s * Real.sqrt s) ^ 2 := by ring
        _ = 1 := by rw [one_div_mul_cancel hne, one_pow]
        _ ≤ 1 := le_refl 1
    have hval := ehom_dot e (fun j => -(1 / Real.sqrt s) * ehom e j.succ)
    rw [Fin.sum_univ_succ, hom_zero, mul_one] at hval
    simp only [hom_succ] at hval
    have hsum : ∑ j, ehom e j.succ * (-(1 / Real.sqrt s) * ehom e j.succ) = -Real.sqrt s := by
      calc ∑ j, ehom e j.succ * (-(1 / Real.sqrt s) * ehom e j.succ)
          = ∑ j, -(1 / Real.sqrt s) * ehom e j.succ ^ 2 :=
            Finset.sum_congr rfl fun j _ => by ring
        _ = -(1 / Real.sqrt s) * ∑ j, ehom e j.succ ^ 2 := (Finset.mul_sum _ _ _).symm
        _ = -(1 / Real.sqrt s) * s := by rw [hs]
        _ = -Real.sqrt s := by
            rw [neg_mul, neg_inj, div_mul_eq_mul_div, one_mul, div_eq_iff hne, hsq]
    rw [hsum] at hval
    have hpos' := (he _ hxmem).1
    have hle : Real.sqrt s ≤ ehom e 0 := by linarith
    calc s = Real.sqrt s ^ 2 := (Real.sq_sqrt hs0).symm
      _ ≤ ehom e 0 ^ 2 := pow_le_pow_left₀ (Real.sqrt_nonneg s) hle 2

theorem pairVal_eq_sum_toOp (a b : HVec d) (ω : W d) :
    pairVal a b ω = ∑ μ, a μ * toOp ω b μ := by
  unfold pairVal
  refine Finset.sum_congr rfl fun μ _ => ?_
  rw [toOp_apply, Finset.mul_sum]
  exact Finset.sum_congr rfl fun ν _ => by ring

theorem pairVal_smul_left (c : ℝ) (a b : HVec d) (ω : W d) :
    pairVal (c • a) b ω = c * pairVal a b ω := by
  unfold pairVal
  rw [Finset.mul_sum]
  refine Finset.sum_congr rfl fun μ _ => ?_
  rw [Finset.mul_sum]
  exact Finset.sum_congr rfl fun ν _ => by simp only [Pi.smul_apply, smul_eq_mul]; ring

theorem pairVal_smul_right (c : ℝ) (a b : HVec d) (ω : W d) :
    pairVal a (c • b) ω = c * pairVal a b ω := by
  unfold pairVal
  rw [Finset.mul_sum]
  refine Finset.sum_congr rfl fun μ _ => ?_
  rw [Finset.mul_sum]
  exact Finset.sum_congr rfl fun ν _ => by simp only [Pi.smul_apply, smul_eq_mul]; ring

/-- A maximal-cone vector pairs nonnegatively with every two cone vectors. -/
theorem pairVal_nonneg_of_maxCone {ω : W d} (hω : ω ∈ maxCone (eball d)) {a b : HVec d}
    (ha : Lor a) (hb : Lor b) : 0 ≤ pairVal a b ω := by
  have hpa : 0 < 2 * (a 0 + 1) := by linarith [ha.1]
  have hpb : 0 < 2 * (b 0 + 1) := by linarith [hb.1]
  have hca : 0 < 1 / (2 * (a 0 + 1)) := div_pos one_pos hpa
  have hcb : 0 < 1 / (2 * (b 0 + 1)) := div_pos one_pos hpb
  have ha1 : 1 / (2 * (a 0 + 1)) * (2 * (a 0 + 1)) = 1 := one_div_mul_cancel (ne_of_gt hpa)
  have hb1 : 1 / (2 * (b 0 + 1)) * (2 * (b 0 + 1)) = 1 := one_div_mul_cancel (ne_of_gt hpb)
  have ha0 : ((1 / (2 * (a 0 + 1))) • a) 0 ≤ 1 / 2 := by
    simp only [Pi.smul_apply, smul_eq_mul]; linarith
  have hb0 : ((1 / (2 * (b 0 + 1))) • b) 0 ≤ 1 / 2 := by
    simp only [Pi.smul_apply, smul_eq_mul]; linarith
  have hpos := hω (affOf ((1 / (2 * (a 0 + 1))) • a)) (affOf ((1 / (2 * (b 0 + 1))) • b))
    (isEffectOn_affOf (lor_smul ha hca.le) ha0) (isEffectOn_affOf (lor_smul hb hcb.le) hb0)
  rw [prodEffVal, ehom_affOf, ehom_affOf, pairVal_smul_left, pairVal_smul_right, ← mul_assoc]
    at hpos
  have h2 : (1 / (2 * (a 0 + 1)) * (1 / (2 * (b 0 + 1)))) * 0
      ≤ (1 / (2 * (a 0 + 1)) * (1 / (2 * (b 0 + 1)))) * pairVal a b ω := by
    rw [mul_zero]; exact hpos
  exact le_of_mul_le_mul_left h2 (mul_pos hca hcb)

/-- A vector pairing nonnegatively with every cone vector lies in the cone. -/
theorem lor_of_forall_pair {g : HVec d} (h : ∀ a : HVec d, Lor a → 0 ≤ ∑ μ, a μ * g μ) :
    Lor g := by
  have hg0 : 0 ≤ g 0 := by
    have := h (hom 0) ⟨by rw [hom_zero]; exact zero_le_one, by simp [hom_succ]⟩
    rw [Fin.sum_univ_succ, hom_zero, one_mul] at this
    simpa [hom_succ] using this
  refine ⟨hg0, ?_⟩
  obtain ⟨t, ht⟩ : ∃ t : ℝ, t = ∑ j, g j.succ ^ 2 := ⟨_, rfl⟩
  rw [← ht]
  have ht0 : 0 ≤ t := ht ▸ Finset.sum_nonneg fun j _ => sq_nonneg _
  have hsq : Real.sqrt t ^ 2 = t := Real.sq_sqrt ht0
  have hlor : Lor (Matrix.vecCons (Real.sqrt t) fun j => -g j.succ) := by
    refine ⟨Real.sqrt_nonneg t, ?_⟩
    show ∑ j, (-g j.succ) ^ 2 ≤ Real.sqrt t ^ 2
    rw [hsq, ht]
    exact le_of_eq (Finset.sum_congr rfl fun j _ => neg_sq _)
  have hpair := h _ hlor
  rw [Fin.sum_univ_succ] at hpair
  simp only [Matrix.cons_val_zero, Matrix.cons_val_succ] at hpair
  have hsum : ∑ j, -g j.succ * g j.succ = -t := by
    rw [ht, ← Finset.sum_neg_distrib]
    exact Finset.sum_congr rfl fun j _ => by ring
  rw [hsum] at hpair
  rcases eq_or_lt_of_le ht0 with h0 | hpos
  · rw [← h0]; exact sq_nonneg _
  · have hsqpos : 0 < Real.sqrt t := Real.sqrt_pos.2 hpos
    have hle : Real.sqrt t ≤ g 0 := by
      have h2 : Real.sqrt t * Real.sqrt t ≤ Real.sqrt t * g 0 := by
        rw [Real.mul_self_sqrt ht0]; linarith
      exact le_of_mul_le_mul_left h2 hsqpos
    calc t = Real.sqrt t ^ 2 := hsq.symm
      _ ≤ g 0 ^ 2 := pow_le_pow_left₀ (Real.sqrt_nonneg t) hle 2

/-- A maximal-cone vector, read as an operator, carries the cone into itself. -/
theorem lor_toOp_of_maxCone {ω : W d} (hω : ω ∈ maxCone (eball d)) {f : HVec d} (hf : Lor f) :
    Lor (toOp ω f) :=
  lor_of_forall_pair fun a ha => by
    rw [← pairVal_eq_sum_toOp]
    exact pairVal_nonneg_of_maxCone hω ha hf

theorem lor_three {v : HVec 3} (hv : Lor v) : 0 ≤ v 0 ∧ v 1 ^ 2 + v 2 ^ 2 + v 3 ^ 2 ≤ v 0 ^ 2 := by
  obtain ⟨h0, h⟩ := hv
  rw [Fin.sum_univ_three] at h
  exact ⟨h0, h⟩

theorem lor_of_three {v : HVec 3} (h0 : 0 ≤ v 0) (h : v 1 ^ 2 + v 2 ^ 2 + v 3 ^ 2 ≤ v 0 ^ 2) :
    Lor v := ⟨h0, by rw [Fin.sum_univ_three]; exact h⟩

/-! ### §M — two-sided positivity of the `d = 3` gate -/

/-- The core inequality: the image of a product state under the gate, paired with two cone
vectors, in the variables `P Q R S` of the target side. -/
theorem cnot_core (e0 a1 a2 a3 x1 x2 x3 P Q R S : ℝ) (he0 : 0 ≤ e0)
    (ha : a1 ^ 2 + a2 ^ 2 + a3 ^ 2 ≤ e0 ^ 2) (hx : x1 ^ 2 + x2 ^ 2 + x3 ^ 2 ≤ 1)
    (hP : 0 ≤ P) (hPQ : R ^ 2 + S ^ 2 ≤ P ^ 2 - Q ^ 2) :
    0 ≤ e0 * (P + x3 * Q) + a1 * (x1 * R - x2 * S) + a2 * (x2 * R + x1 * S)
      + a3 * (x3 * P + Q) := by
  have hx3 : x3 ^ 2 ≤ 1 := by linarith [sq_nonneg x1, sq_nonneg x2]
  have hQ2 : Q ^ 2 ≤ P ^ 2 := by linarith [sq_nonneg R, sq_nonneg S]
  have hg0 : 0 ≤ P + x3 * Q := by
    have h : (x3 * Q) ^ 2 ≤ P ^ 2 := by
      rw [mul_pow]
      calc x3 ^ 2 * Q ^ 2 ≤ 1 * P ^ 2 := mul_le_mul hx3 hQ2 (sq_nonneg _) zero_le_one
        _ = P ^ 2 := one_mul _
    linarith [(abs_le_of_sq_le_sq' h hP).1]
  have hgid : (P + x3 * Q) ^ 2
      - ((x1 * R - x2 * S) ^ 2 + (x2 * R + x1 * S) ^ 2 + (x3 * P + Q) ^ 2)
      = (1 - x3 ^ 2) * (P ^ 2 - Q ^ 2) - (x1 ^ 2 + x2 ^ 2) * (R ^ 2 + S ^ 2) := by ring
  have h3 : (x1 ^ 2 + x2 ^ 2) * (R ^ 2 + S ^ 2) ≤ (1 - x3 ^ 2) * (P ^ 2 - Q ^ 2) :=
    mul_le_mul (by linarith) hPQ (by positivity) (by linarith)
  have hg : (x1 * R - x2 * S) ^ 2 + (x2 * R + x1 * S) ^ 2 + (x3 * P + Q) ^ 2
      ≤ (P + x3 * Q) ^ 2 := by linarith
  have hcsid : (a1 ^ 2 + a2 ^ 2 + a3 ^ 2)
        * ((x1 * R - x2 * S) ^ 2 + (x2 * R + x1 * S) ^ 2 + (x3 * P + Q) ^ 2)
      - (a1 * (x1 * R - x2 * S) + a2 * (x2 * R + x1 * S) + a3 * (x3 * P + Q)) ^ 2
      = (a1 * (x2 * R + x1 * S) - a2 * (x1 * R - x2 * S)) ^ 2
        + (a1 * (x3 * P + Q) - a3 * (x1 * R - x2 * S)) ^ 2
        + (a2 * (x3 * P + Q) - a3 * (x2 * R + x1 * S)) ^ 2 := by ring
  have hcs : (a1 * (x1 * R - x2 * S) + a2 * (x2 * R + x1 * S) + a3 * (x3 * P + Q)) ^ 2
      ≤ (e0 * (P + x3 * Q)) ^ 2 := by
    rw [mul_pow]
    calc (a1 * (x1 * R - x2 * S) + a2 * (x2 * R + x1 * S) + a3 * (x3 * P + Q)) ^ 2
        ≤ (a1 ^ 2 + a2 ^ 2 + a3 ^ 2)
          * ((x1 * R - x2 * S) ^ 2 + (x2 * R + x1 * S) ^ 2 + (x3 * P + Q) ^ 2) := by
          linarith [sq_nonneg (a1 * (x2 * R + x1 * S) - a2 * (x1 * R - x2 * S)),
            sq_nonneg (a1 * (x3 * P + Q) - a3 * (x1 * R - x2 * S)),
            sq_nonneg (a2 * (x3 * P + Q) - a3 * (x2 * R + x1 * S))]
      _ ≤ e0 ^ 2 * (P + x3 * Q) ^ 2 := mul_le_mul ha hg (by positivity) (sq_nonneg _)
  have := (abs_le_of_sq_le_sq' hcs (mul_nonneg he0 hg0)).1
  linarith

/-- The target-side quantities of the core inequality from the coefficient bounds. -/
theorem cnot_target (f0 b1 b2 b3 y1 y2 y3 : ℝ) (hf0 : 0 ≤ f0)
    (hb : b1 ^ 2 + b2 ^ 2 + b3 ^ 2 ≤ f0 ^ 2) (hy : y1 ^ 2 + y2 ^ 2 + y3 ^ 2 ≤ 1) :
    0 ≤ f0 + b1 * y1 ∧
      (b1 + f0 * y1) ^ 2 + (b3 * y2 - b2 * y3) ^ 2
        ≤ (f0 + b1 * y1) ^ 2 - (b2 * y2 + b3 * y3) ^ 2 := by
  constructor
  · have h : (b1 * y1) ^ 2 ≤ f0 ^ 2 := by
      rw [mul_pow]
      calc b1 ^ 2 * y1 ^ 2 ≤ f0 ^ 2 * 1 :=
            mul_le_mul (by linarith [sq_nonneg b2, sq_nonneg b3])
              (by linarith [sq_nonneg y2, sq_nonneg y3]) (sq_nonneg _) (sq_nonneg _)
        _ = f0 ^ 2 := mul_one _
    linarith [(abs_le_of_sq_le_sq' h hf0).1]
  · have hid : (f0 + b1 * y1) ^ 2 - (b2 * y2 + b3 * y3) ^ 2 - (b1 + f0 * y1) ^ 2
        - (b3 * y2 - b2 * y3) ^ 2
        = (f0 ^ 2 - b1 ^ 2) * (1 - y1 ^ 2) - (b2 ^ 2 + b3 ^ 2) * (y2 ^ 2 + y3 ^ 2) := by ring
    have h1 : (b2 ^ 2 + b3 ^ 2) * (y2 ^ 2 + y3 ^ 2) ≤ (f0 ^ 2 - b1 ^ 2) * (1 - y1 ^ 2) :=
      mul_le_mul (by linarith) (by linarith) (by positivity)
        (by linarith [sq_nonneg b2, sq_nonneg b3])
    linarith

/-- The pairing of two effects with the gate image of a product state, in coordinates. -/
theorem prodEffVal_cnot_prodState (e f : (Fin 3 → ℝ) →ᵃ[ℝ] ℝ) (x y : Fin 3 → ℝ) :
    prodEffVal e f (cnot (prodState x y))
      = ehom e 0 * ((ehom f 0 + ehom f 1 * y 0) + x 2 * (ehom f 2 * y 1 + ehom f 3 * y 2))
        + ehom e 1 * (x 0 * (ehom f 1 + ehom f 0 * y 0) - x 1 * (ehom f 3 * y 1 - ehom f 2 * y 2))
        + ehom e 2 * (x 1 * (ehom f 1 + ehom f 0 * y 0) + x 0 * (ehom f 3 * y 1 - ehom f 2 * y 2))
        + ehom e 3 * (x 2 * (ehom f 0 + ehom f 1 * y 0) + (ehom f 2 * y 1 + ehom f 3 * y 2)) := by
  simp only [prodEffVal, pairVal, cnot_apply, cnotFun_apply, prodState_apply, Fin.sum_univ_four]
  simp +decide [sgn, pc, pt]
  ring

/-- Two-sided positivity of the `d = 3` gate on product states of the ball. -/
theorem cnot_prodEffVal_nonneg {e f : (Fin 3 → ℝ) →ᵃ[ℝ] ℝ} (he : IsEffectOn (eball 3) e)
    (hf : IsEffectOn (eball 3) f) {x y : Fin 3 → ℝ} (hx : x ∈ eball 3) (hy : y ∈ eball 3) :
    0 ≤ prodEffVal e f (cnot (prodState x y)) := by
  obtain ⟨he0, ha⟩ := lor_three (lor_ehom he)
  obtain ⟨hf0, hb⟩ := lor_three (lor_ehom hf)
  rw [mem_eball, Fin.sum_univ_three] at hx hy
  obtain ⟨hP, hPQ⟩ := cnot_target (ehom f 0) (ehom f 1) (ehom f 2) (ehom f 3) (y 0) (y 1) (y 2)
    hf0 hb hy
  rw [prodEffVal_cnot_prodState]
  exact cnot_core (ehom e 0) (ehom e 1) (ehom e 2) (ehom e 3) (x 0) (x 1) (x 2) _ _ _ _ he0 ha hx
    hP hPQ

theorem cnot_prodState_mem_maxCone {x y : Fin 3 → ℝ} (hx : x ∈ eball 3) (hy : y ∈ eball 3) :
    cnot (prodState x y) ∈ maxCone (eball 3) := by
  show ∀ e f, IsEffectOn (eball 3) e → IsEffectOn (eball 3) f →
    0 ≤ prodEffVal e f (cnot (prodState x y))
  intro e f he hf
  exact cnot_prodEffVal_nonneg he hf hx hy

/-- The `d = 3` gate satisfies every native-gate hypothesis. -/
theorem nativeGate_cnot : NativeGate (eball 3) z3 nflip cnot where
  frame := cnot_frame
  posFwd x hx y hy := cnot_prodState_mem_maxCone hx hy
  posInv x hx y hy := cnot_prodState_mem_maxCone hx hy
  relT := cnot_relT
  relC := cnot_relC

/-! ### §N — the entangling clause for the `d = 3` gate -/

/-- A unit vector is an extreme point of the ball. -/
theorem extreme_of_unit {x : Fin 3 → ℝ} (hx : x 0 ^ 2 + x 1 ^ 2 + x 2 ^ 2 = 1) :
    x ∈ (eball 3).extremePoints ℝ := by
  refine ⟨by rw [mem_eball, Fin.sum_univ_three]; exact hx.le, ?_⟩
  intro u hu v hv hseg
  obtain ⟨a, b, ha, hb, hab, hz⟩ := hseg
  rw [mem_eball, Fin.sum_univ_three] at hu hv
  obtain rfl : b = 1 - a := by linarith
  have e0 := congrFun hz 0
  have e1 := congrFun hz 1
  have e2 := congrFun hz 2
  simp only [Pi.add_apply, Pi.smul_apply, smul_eq_mul] at e0 e1 e2
  rw [← e0, ← e1, ← e2] at hx
  have hid : a * (u 0 ^ 2 + u 1 ^ 2 + u 2 ^ 2) + (1 - a) * (v 0 ^ 2 + v 1 ^ 2 + v 2 ^ 2)
      - ((a * u 0 + (1 - a) * v 0) ^ 2 + (a * u 1 + (1 - a) * v 1) ^ 2
        + (a * u 2 + (1 - a) * v 2) ^ 2)
      = a * (1 - a) * ((u 0 - v 0) ^ 2 + (u 1 - v 1) ^ 2 + (u 2 - v 2) ^ 2) := by ring
  have h1 := mul_le_mul_of_nonneg_left hu ha.le
  have h2 := mul_le_mul_of_nonneg_left hv hb.le
  have hw : a * (1 - a) * ((u 0 - v 0) ^ 2 + (u 1 - v 1) ^ 2 + (u 2 - v 2) ^ 2)
      ≤ a * (1 - a) * 0 := by rw [mul_zero]; linarith
  have hw' := le_of_mul_le_mul_left hw (mul_pos ha hb)
  have d0 : u 0 - v 0 = 0 := (pow_eq_zero_iff two_ne_zero).mp
    (le_antisymm (by linarith [sq_nonneg (u 1 - v 1), sq_nonneg (u 2 - v 2)]) (sq_nonneg _))
  have d1 : u 1 - v 1 = 0 := (pow_eq_zero_iff two_ne_zero).mp
    (le_antisymm (by linarith [sq_nonneg (u 0 - v 0), sq_nonneg (u 2 - v 2)]) (sq_nonneg _))
  have d2 : u 2 - v 2 = 0 := (pow_eq_zero_iff two_ne_zero).mp
    (le_antisymm (by linarith [sq_nonneg (u 0 - v 0), sq_nonneg (u 1 - v 1)]) (sq_nonneg _))
  have hu0 : u 0 = x 0 := by
    have hv : v 0 = u 0 := by linarith
    rw [hv] at e0; linarith
  have hu1 : u 1 = x 1 := by
    have hv : v 1 = u 1 := by linarith
    rw [hv] at e1; linarith
  have hu2 : u 2 = x 2 := by
    have hv : v 2 = u 2 := by linarith
    rw [hv] at e2; linarith
  funext i
  fin_cases i
  · exact hu0
  · exact hu1
  · exact hu2

/-- The pure input of the entangling witness: the unit vector of the first coordinate. -/
def xplus : Fin 3 → ℝ := ![1, 0, 0]

@[simp] theorem xplus_zero : xplus 0 = 1 := rfl
@[simp] theorem xplus_one : xplus 1 = 0 := rfl
@[simp] theorem xplus_two : xplus 2 = 0 := rfl

/-- The entangled image: the diagonal joint vector with entries `1, 1, −1, 1`. -/
def phiW : W 3 := fun μ ν => if μ = ν then (if μ = 2 then -1 else 1) else 0

theorem cnot_prodState_xplus_z3 : cnot (prodState xplus z3) = phiW := by
  funext μ ν
  fin_cases μ <;> fin_cases ν <;>
    simp +decide [cnot_apply, cnotFun_apply, sgn, pc, pt, prodState_apply, phiW]

theorem xplus_mem : xplus ∈ eball 3 := by rw [mem_eball, Fin.sum_univ_three]; simp

theorem z3_mem : z3 ∈ eball 3 := by rw [mem_eball, Fin.sum_univ_three]; simp

/-- The entangled image is not a product state. -/
theorem phiW_not_product : ¬ IsProduct (eball 3) phiW := by
  rintro ⟨x', -, y', -, h⟩
  have h10 : x' 0 = 0 := by
    have := congrFun (congrFun h 1) 0
    simp +decide [phiW, prodState_apply] at this
    linarith
  have h11 : x' 0 * y' 0 = 1 := by
    have := congrFun (congrFun h 1) 1
    simp +decide [phiW, prodState_apply] at this
    linarith
  rw [h10, zero_mul] at h11
  exact zero_ne_one h11

/-- The entangled image is a joint state. -/
theorem phiW_mem_jointStates : phiW ∈ jointStates (eball 3) := by
  refine ⟨?_, by simp +decide [phiW]⟩
  rw [← cnot_prodState_xplus_z3]
  exact cnot_prodState_mem_maxCone xplus_mem z3_mem

@[simp] theorem toOp_phiW_zero (t : HVec 3) : toOp phiW t 0 = t 0 := by
  rw [toOp_apply, Fin.sum_univ_four]; simp +decide [phiW]
@[simp] theorem toOp_phiW_one (t : HVec 3) : toOp phiW t 1 = t 1 := by
  rw [toOp_apply, Fin.sum_univ_four]; simp +decide [phiW]
@[simp] theorem toOp_phiW_two (t : HVec 3) : toOp phiW t 2 = -t 2 := by
  rw [toOp_apply, Fin.sum_univ_four]; simp +decide [phiW]
@[simp] theorem toOp_phiW_three (t : HVec 3) : toOp phiW t 3 = t 3 := by
  rw [toOp_apply, Fin.sum_univ_four]; simp +decide [phiW]

/-- The extreme rays of the cone: a boundary vector that is a positive combination of two cone
vectors is proportional to each of them. -/
theorem lor_ray {f g h : HVec 3} (hf : f 1 ^ 2 + f 2 ^ 2 + f 3 ^ 2 = f 0 ^ 2)
    (hg : Lor g) (hh : Lor h) {a b : ℝ} (ha : 0 < a) (hb : 0 < b)
    (hsum : a • g + b • h = f) :
    f 0 * g 1 = g 0 * f 1 ∧ f 0 * g 2 = g 0 * f 2 ∧ f 0 * g 3 = g 0 * f 3 := by
  obtain ⟨hg0, hg'⟩ := lor_three hg
  obtain ⟨hh0, hh'⟩ := lor_three hh
  have e0 := congrFun hsum 0
  have e1 := congrFun hsum 1
  have e2 := congrFun hsum 2
  have e3 := congrFun hsum 3
  simp only [Pi.add_apply, Pi.smul_apply, smul_eq_mul] at e0 e1 e2 e3
  have hM : g 1 * h 1 + g 2 * h 2 + g 3 * h 3 ≤ g 0 * h 0 := by
    have hcs : (g 1 * h 1 + g 2 * h 2 + g 3 * h 3) ^ 2 ≤ (g 0 * h 0) ^ 2 := by
      rw [mul_pow]
      calc (g 1 * h 1 + g 2 * h 2 + g 3 * h 3) ^ 2
          ≤ (g 1 ^ 2 + g 2 ^ 2 + g 3 ^ 2) * (h 1 ^ 2 + h 2 ^ 2 + h 3 ^ 2) := by
            nlinarith [sq_nonneg (g 1 * h 2 - g 2 * h 1), sq_nonneg (g 1 * h 3 - g 3 * h 1),
              sq_nonneg (g 2 * h 3 - g 3 * h 2)]
        _ ≤ g 0 ^ 2 * h 0 ^ 2 := mul_le_mul hg' hh' (by positivity) (sq_nonneg _)
    exact (abs_le_of_sq_le_sq' hcs (mul_nonneg hg0 hh0)).2
  have hQ : a ^ 2 * (g 0 ^ 2 - (g 1 ^ 2 + g 2 ^ 2 + g 3 ^ 2))
      + 2 * a * b * (g 0 * h 0 - (g 1 * h 1 + g 2 * h 2 + g 3 * h 3))
      + b ^ 2 * (h 0 ^ 2 - (h 1 ^ 2 + h 2 ^ 2 + h 3 ^ 2)) = 0 := by
    have hf2 := hf
    rw [← e0, ← e1, ← e2, ← e3] at hf2
    linear_combination (-1 : ℝ) * hf2
  have t1 : 0 ≤ a ^ 2 * (g 0 ^ 2 - (g 1 ^ 2 + g 2 ^ 2 + g 3 ^ 2)) :=
    mul_nonneg (sq_nonneg a) (by linarith)
  have t2 : 0 ≤ 2 * a * b * (g 0 * h 0 - (g 1 * h 1 + g 2 * h 2 + g 3 * h 3)) :=
    mul_nonneg (mul_nonneg (mul_nonneg (by norm_num) ha.le) hb.le) (by linarith)
  have t3 : 0 ≤ b ^ 2 * (h 0 ^ 2 - (h 1 ^ 2 + h 2 ^ 2 + h 3 ^ 2)) :=
    mul_nonneg (sq_nonneg b) (by linarith)
  have hQg : g 0 ^ 2 - (g 1 ^ 2 + g 2 ^ 2 + g 3 ^ 2) = 0 := by
    have h4 : a ^ 2 * (g 0 ^ 2 - (g 1 ^ 2 + g 2 ^ 2 + g 3 ^ 2)) = 0 := by linarith
    rcases mul_eq_zero.mp h4 with h | h
    · exact absurd h (pow_ne_zero 2 ha.ne')
    · exact h
  have hMgh : g 0 * h 0 - (g 1 * h 1 + g 2 * h 2 + g 3 * h 3) = 0 := by
    have h4 : 2 * a * b * (g 0 * h 0 - (g 1 * h 1 + g 2 * h 2 + g 3 * h 3)) = 0 := by linarith
    rcases mul_eq_zero.mp h4 with h | h
    · exact absurd h (mul_pos (mul_pos two_pos ha) hb).ne'
    · exact h
  have hMgf : g 0 * f 0 - (g 1 * f 1 + g 2 * f 2 + g 3 * f 3) = 0 := by
    rw [← e0, ← e1, ← e2, ← e3]
    linear_combination a * hQg + b * hMgh
  have hzero : (f 0 * g 1 - g 0 * f 1) ^ 2 + (f 0 * g 2 - g 0 * f 2) ^ 2
      + (f 0 * g 3 - g 0 * f 3) ^ 2 = 0 := by
    linear_combination (-(f 0 ^ 2)) * hQg + (2 * f 0 * g 0) * hMgf + (g 0 ^ 2) * hf
  have s1 : f 0 * g 1 - g 0 * f 1 = 0 := (pow_eq_zero_iff two_ne_zero).mp
    (le_antisymm (by linarith [sq_nonneg (f 0 * g 2 - g 0 * f 2),
      sq_nonneg (f 0 * g 3 - g 0 * f 3)]) (sq_nonneg _))
  have s2 : f 0 * g 2 - g 0 * f 2 = 0 := (pow_eq_zero_iff two_ne_zero).mp
    (le_antisymm (by linarith [sq_nonneg (f 0 * g 1 - g 0 * f 1),
      sq_nonneg (f 0 * g 3 - g 0 * f 3)]) (sq_nonneg _))
  have s3 : f 0 * g 3 - g 0 * f 3 = 0 := (pow_eq_zero_iff two_ne_zero).mp
    (le_antisymm (by linarith [sq_nonneg (f 0 * g 1 - g 0 * f 1),
      sq_nonneg (f 0 * g 2 - g 0 * f 2)]) (sq_nonneg _))
  exact ⟨by linarith, by linarith, by linarith⟩

/-- The test vectors `(1, s eᵢ)` of the control space. -/
def tv (i : Fin 4) (s : ℝ) : HVec 3 := fun μ => if μ = 0 then 1 else if μ = i then s else 0

theorem toOp_tv1 (ω : W 3) (s : ℝ) (μ : Fin 4) : toOp ω (tv 1 s) μ = ω μ 0 + ω μ 1 * s := by
  rw [toOp_apply, Fin.sum_univ_four]; simp +decide [tv]

theorem toOp_tv2 (ω : W 3) (s : ℝ) (μ : Fin 4) : toOp ω (tv 2 s) μ = ω μ 0 + ω μ 2 * s := by
  rw [toOp_apply, Fin.sum_univ_four]; simp +decide [tv]

theorem toOp_tv3 (ω : W 3) (s : ℝ) (μ : Fin 4) : toOp ω (tv 3 s) μ = ω μ 0 + ω μ 3 * s := by
  rw [toOp_apply, Fin.sum_univ_four]; simp +decide [tv]

/-- The ray equations of a segment through the entangled image, read on a boundary test vector. -/
theorem ray_eqs {ω₁ ω₂ : W 3} (h₁ : ω₁ ∈ maxCone (eball 3)) (h₂ : ω₂ ∈ maxCone (eball 3))
    {a b : ℝ} (ha : 0 < a) (hb : 0 < b) (hsum : a • ω₁ + b • ω₂ = phiW) {t : HVec 3}
    (ht0 : t 0 = 1) (ht : t 1 ^ 2 + t 2 ^ 2 + t 3 ^ 2 = 1) :
    toOp ω₁ t 1 = toOp ω₁ t 0 * t 1 ∧ toOp ω₁ t 2 = toOp ω₁ t 0 * (-t 2) ∧
      toOp ω₁ t 3 = toOp ω₁ t 0 * t 3 := by
  have htl : Lor t := lor_of_three (by rw [ht0]; exact zero_le_one) (by rw [ht0, ht, one_pow])
  have hg := lor_toOp_of_maxCone h₁ htl
  have hh := lor_toOp_of_maxCone h₂ htl
  have hlin : toOp (a • ω₁ + b • ω₂) = a • toOp ω₁ + b • toOp ω₂ := by
    rw [← toOpLin_apply, map_add, map_smul, map_smul]; rfl
  have hsum' : a • toOp ω₁ t + b • toOp ω₂ t = toOp phiW t := by
    rw [← hsum, hlin, LinearMap.add_apply, LinearMap.smul_apply, LinearMap.smul_apply]
  have hf : toOp phiW t 1 ^ 2 + toOp phiW t 2 ^ 2 + toOp phiW t 3 ^ 2 = toOp phiW t 0 ^ 2 := by
    rw [toOp_phiW_zero, toOp_phiW_one, toOp_phiW_two, toOp_phiW_three, neg_sq, ht0, ht, one_pow]
  obtain ⟨e1, e2, e3⟩ := lor_ray hf hg hh ha hb hsum'
  rw [toOp_phiW_zero, ht0, one_mul] at e1 e2 e3
  rw [toOp_phiW_one] at e1
  rw [toOp_phiW_two] at e2
  rw [toOp_phiW_three] at e3
  exact ⟨e1, e2, e3⟩

/-- A joint state on an open segment through the entangled image is the entangled image. -/
theorem phiW_eq_of_segment {ω₁ ω₂ : W 3} (h₁ : ω₁ ∈ jointStates (eball 3))
    (h₂ : ω₂ ∈ jointStates (eball 3)) {a b : ℝ} (ha : 0 < a) (hb : 0 < b)
    (hsum : a • ω₁ + b • ω₂ = phiW) : ω₁ = phiW := by
  have h00 : ω₁ 0 0 = 1 := h₁.2
  have hp : ∀ (i : Fin 4) (s : ℝ), tv i s 0 = 1 →
      tv i s 1 ^ 2 + tv i s 2 ^ 2 + tv i s 3 ^ 2 = 1 →
      toOp ω₁ (tv i s) 1 = toOp ω₁ (tv i s) 0 * tv i s 1 ∧
        toOp ω₁ (tv i s) 2 = toOp ω₁ (tv i s) 0 * (-tv i s 2) ∧
        toOp ω₁ (tv i s) 3 = toOp ω₁ (tv i s) 0 * tv i s 3 :=
    fun i s hi0 hn => ray_eqs h₁.1 h₂.1 ha hb hsum hi0 hn
  obtain ⟨a1, a2, a3⟩ := hp 1 1 (by simp +decide [tv]) (by simp +decide [tv])
  obtain ⟨b1, b2, b3⟩ := hp 1 (-1) (by simp +decide [tv]) (by simp +decide [tv])
  obtain ⟨c1, c2, c3⟩ := hp 2 1 (by simp +decide [tv]) (by simp +decide [tv])
  obtain ⟨d1, d2, d3⟩ := hp 2 (-1) (by simp +decide [tv]) (by simp +decide [tv])
  obtain ⟨f1, f2, f3⟩ := hp 3 1 (by simp +decide [tv]) (by simp +decide [tv])
  obtain ⟨g1, g2, g3⟩ := hp 3 (-1) (by simp +decide [tv]) (by simp +decide [tv])
  simp +decide [toOp_tv1, toOp_tv2, toOp_tv3, tv] at a1 a2 a3 b1 b2 b3 c1 c2 c3 d1 d2 d3 f1 f2 f3
    g1 g2 g3
  funext μ ν
  fin_cases μ <;> fin_cases ν <;> simp +decide [phiW] <;> linarith

/-- The `d = 3` gate is entangling: the pure product input `(xplus, z3)` has an extreme joint
image that is not a product state. -/
theorem entangling_cnot : Entangling (eball 3) cnot :=
  ⟨xplus, extreme_of_unit (by simp), z3, extreme_of_unit (by simp), by
    rw [cnot_prodState_xplus_z3]
    refine ⟨⟨phiW_mem_jointStates, ?_⟩, phiW_not_product⟩
    intro ω₁ h₁ ω₂ h₂ hseg
    obtain ⟨a, b, ha, hb, -, hsum⟩ := hseg
    exact phiW_eq_of_segment h₁ h₂ ha hb hsum⟩

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
