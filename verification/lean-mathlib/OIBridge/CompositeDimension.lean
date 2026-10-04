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
    §D  the parity count: equal eigenspace dimensions exclude every even `d`.

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
    homMap N v j.succ = N (Matrix.vecTail v) j :=
  Matrix.cons_val_succ _ _ _

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
  have hne : plusSpace N ≠ ⊥ := Submodule.ne_bot_iff.mpr
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
  have hne : minusSpace N ≠ ⊥ := Submodule.ne_bot_iff.mpr
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
theorem split_of_balanced {a b : ℕ} (hsum : a + b = d + 1) (hbal : a = b) (ha : 1 ≤ a) :
    (a - 1) = (b - 1) ∧ (a - 1) + (b - 1) + 1 = d := by
  omega

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
