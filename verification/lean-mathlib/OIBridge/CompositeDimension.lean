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
    §J  the exclusions: no even `d` (`not_even_of_nativeGate`, with `d = 2`, `d = 4`); the block
        data (`BlockData`, the hypothesis of `NativeGateBall.p_le_one`, derived in §Q) and its
        consequence `p ≤ 1` (`p_le_one_of_blockData`);
    §K  survival, the `d = 3` gate: a signed permutation `cnot` of the sixteen entries of `W 3`,
        the reflection `nflip` as the common NOT with axis `z3`, `IsNot` (`isNot_nflip`), the frame
        (`cnot_frame`) and the two relations (`cnot_relT`, `cnot_relC`) by exact evaluation;
    §L  the cone `Lor` of homogenized effect vectors of the ball: every effect of the ball has its
        coefficients in the cone (`lor_ehom`), every cone vector of head at most one half is an
        effect (`isEffectOn_affOf`), and a maximal-cone vector read as an operator carries the cone
        into itself (`lor_toOp_of_maxCone`);
    §M  two-sided positivity of the `d = 3` gate on every product state of the ball, by the exact
        inequality `cnot_core` (`cnot_prodEffVal_nonneg`), so `NativeGate (eball 3) z3 nflip cnot`
        (`nativeGate_cnot`);
    §N  the entangling clause for the `d = 3` gate: the pure product input `(xplus, z3)` has the
        image `phiW`, which is a joint state, not a product state, and an extreme joint state by the
        extreme-ray argument on the cone (`lor_ray`, `phiW_eq_of_segment`), so
        `Entangling (eball 3) cnot` (`entangling_cnot`);
    §O  `d = 1` is not entangling: an extreme point of the interval is a corner, and the frame
        carries every pure product input to a product (`not_entangling_one`);
    §Q  the block reduction, S1–S2–S4 of round NB-1, in the kernel for `2 ≤ d`: positivity on
        every product of cone vectors (`tens_mem_maxCone`); a linear functional nonnegative on
        the cone and zero at the centre is zero (`linearMap_eq_zero_of_nonneg_lor`); the corner
        face of the cone (`lor_face`); S1, the controlled form on a corner slice (`corner_form`,
        `gate_corner`, `gate_corner_symm`), the target maps `Mfwd`, `Minv`, inverse to each other,
        commuting with the NOT by Rt, and the `−z` slice by Rc (`gate_corner_neg`); the normalized
        gate on the corner and centre slices (`gt_corner`, `gt_corner_neg`, `gt_center`); the
        tangent argument along the boundary curve through a corner (`lor_curve`,
        `tangent_vanish`); S2, the control output of a tangent slice is orthogonal to both
        corners (`gt_tangent_corners`) and the two sphere identities (`gt_sphere`,
        `gt_sphere_corner`), hence for the block form `Phi` the centre value vanishes, the mixed
        values agree and the diagonal values vanish on unit tangent directions (`Phi_sphere`,
        `Phi_center`); the tangent `+1` eigenspace has dimension `tangentPlus N`
        (`finrank_tangentSpace`) and an orthonormal basis (`exists_orthonormal_basis`); S4, the
        value identity and the nonzero entry, assembled into the block data
        (`blockData_of_orthonormal`, `blockData_of_nativeGate`); the selectors from the frozen
        hypotheses alone, `dim_of_nativeGate : IsNot … → NativeGate … → d = 1 ∨ d = 3` and
        `three_of_nativeGate : … → Entangling … → d = 3`, with `d = 0` excluded by the unit clause
        (`pos_of_isNot`) and `d = 1` handled directly, with `d = 5` and `d = 7` as instances
        (`ne_five_of_nativeGate`, `ne_seven_of_nativeGate`);
    §P  controls: the classical gate `cnot1` of two intervals satisfies every hypothesis
        (`nativeGate_cnot1`) except the entangling clause (`not_entangling_cnot1`), and creates
        correlations from the mixed input `(0, z1)` (`not_product_cnot1_mixed`); `eball 4` carries
        no gate (`no_gate_four`); the verdict `dim1_core`.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.TransitiveBody
import OIBridge.NativeGateBall
import Mathlib.LinearAlgebra.FiniteDimensional.Lemmas
import Mathlib.LinearAlgebra.FreeModule.Finite.Matrix
import Mathlib.LinearAlgebra.Matrix.ToLin
import Mathlib.Analysis.InnerProductSpace.PiL2

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

/-- The data the S1–S2–S4 reduction extracts from a native gate whose `+1` eigenspace has tangent
dimension `p`: the `E₊` blocks `A`, `B` on a target index set of size `m`, antisymmetric in the
pair index, with the Lorentz positivity of `I + Γ` at `t = ±eᵢ` against every unit effect and one
nonzero entry. For `2 ≤ d` the data is derived from the frozen hypotheses in §Q
(`blockData_of_nativeGate`); it is the hypothesis of `NativeGateBall.p_le_one`. -/
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

/-- `Fin.sum_univ_four` at the index type of `W 3`, which is `Fin (3 + 1)` syntactically. -/
theorem sum_univ_four' (f : Fin (3 + 1) → ℝ) : ∑ i, f i = f 0 + f 1 + f 2 + f 3 :=
  Fin.sum_univ_four f

/-- `Fin.sum_univ_two` at the index type of `W 1`, which is `Fin (1 + 1)` syntactically. -/
theorem sum_univ_two' (f : Fin (1 + 1) → ℝ) : ∑ i, f i = f 0 + f 1 :=
  Fin.sum_univ_two f

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

theorem corner_zero (z : Fin d → ℝ) : corner z 0 = z := rfl
theorem corner_one (z : Fin d → ℝ) : corner z 1 = -z := rfl

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
def Lor (v : HVec d) : Prop := 0 ≤ v 0 ∧ ∑ j : Fin d, v j.succ ^ 2 ≤ v 0 ^ 2

theorem lor_smul {v : HVec d} (hv : Lor v) {c : ℝ} (hc : 0 ≤ c) : Lor (c • v) := by
  refine ⟨mul_nonneg hc hv.1, ?_⟩
  simp only [Pi.smul_apply, smul_eq_mul, mul_pow, ← Finset.mul_sum]
  exact mul_le_mul_of_nonneg_left hv.2 (sq_nonneg c)

/-- A vector of the cone paired with a unit-ball point: the tail pairing is bounded by the head. -/
theorem lor_pair_bound {v : HVec d} (hv : Lor v) {x : Fin d → ℝ} (hx : x ∈ eball d) :
    -v 0 ≤ ∑ j : Fin d, v j.succ * x j ∧ ∑ j : Fin d, v j.succ * x j ≤ v 0 := by
  have hcs := Finset.sum_mul_sq_le_sq_mul_sq Finset.univ (fun j : Fin d => v j.succ) x
  rw [mem_eball] at hx
  have h1 : (∑ j : Fin d, v j.succ * x j) ^ 2 ≤ v 0 ^ 2 := by
    refine le_trans hcs ?_
    calc (∑ j : Fin d, v j.succ ^ 2) * ∑ j : Fin d, x j ^ 2 ≤ v 0 ^ 2 * 1 :=
          mul_le_mul hv.2 hx (Finset.sum_nonneg fun j _ => sq_nonneg _) (sq_nonneg _)
      _ = v 0 ^ 2 := mul_one _
  exact abs_le_of_sq_le_sq' h1 hv.1

/-- The affine functional with the given homogenized coefficients. -/
noncomputable def affOf (v : HVec d) : (Fin d → ℝ) →ᵃ[ℝ] ℝ where
  toFun x := v 0 + ∑ j : Fin d, v j.succ * x j
  linear := ∑ j : Fin d, v j.succ • (LinearMap.proj j : (Fin d → ℝ) →ₗ[ℝ] ℝ)
  map_vadd' p w := by
    simp only [vadd_eq_add, Pi.add_apply, mul_add, Finset.sum_add_distrib, LinearMap.sum_apply,
      LinearMap.smul_apply, LinearMap.proj_apply, smul_eq_mul]
    ring

theorem affOf_apply (v : HVec d) (x : Fin d → ℝ) : affOf v x = v 0 + ∑ j : Fin d, v j.succ * x j := rfl

theorem affOf_linear (v : HVec d) :
    (affOf v).linear = ∑ j : Fin d, v j.succ • (LinearMap.proj j : (Fin d → ℝ) →ₗ[ℝ] ℝ) := rfl

/-- The homogenized coefficients of `affOf v` are `v`. -/
theorem ehom_affOf (v : HVec d) : ehom (affOf v) = v := by
  funext μ
  refine Fin.cases ?_ (fun j => ?_) μ
  · show v 0 + ∑ j : Fin d, v j.succ * (0 : Fin d → ℝ) j = v 0
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
  obtain ⟨s, hs⟩ : ∃ s : ℝ, s = ∑ j : Fin d, ehom e j.succ ^ 2 := ⟨_, rfl⟩
  rw [← hs]
  have hs0 : 0 ≤ s := hs ▸ Finset.sum_nonneg fun j _ => sq_nonneg _
  rcases eq_or_lt_of_le hs0 with h0 | hpos
  · rw [← h0]; exact sq_nonneg _
  · have hsq : Real.sqrt s * Real.sqrt s = s := Real.mul_self_sqrt hs0
    have hne : Real.sqrt s ≠ 0 := ne_of_gt (Real.sqrt_pos.2 hpos)
    have hxmem : (fun j : Fin d => -(1 / Real.sqrt s) * ehom e j.succ) ∈ eball d := by
      rw [mem_eball]
      calc ∑ j : Fin d, (-(1 / Real.sqrt s) * ehom e j.succ) ^ 2
          = ∑ j : Fin d, (1 / Real.sqrt s) ^ 2 * ehom e j.succ ^ 2 :=
            Finset.sum_congr rfl fun j _ => by ring
        _ = (1 / Real.sqrt s) ^ 2 * ∑ j : Fin d, ehom e j.succ ^ 2 := (Finset.mul_sum _ _ _).symm
        _ = (1 / Real.sqrt s) ^ 2 * s := by rw [hs]
        _ = (1 / Real.sqrt s) ^ 2 * (Real.sqrt s * Real.sqrt s) := by rw [hsq]
        _ = (1 / Real.sqrt s * Real.sqrt s) ^ 2 := by ring
        _ = 1 := by rw [one_div_mul_cancel hne, one_pow]
        _ ≤ 1 := le_refl 1
    have hval := ehom_dot e (fun j : Fin d => -(1 / Real.sqrt s) * ehom e j.succ)
    rw [Fin.sum_univ_succ, hom_zero, mul_one] at hval
    simp only [hom_succ] at hval
    have hsum : ∑ j : Fin d, ehom e j.succ * (-(1 / Real.sqrt s) * ehom e j.succ) = -Real.sqrt s := by
      calc ∑ j : Fin d, ehom e j.succ * (-(1 / Real.sqrt s) * ehom e j.succ)
          = ∑ j : Fin d, -(1 / Real.sqrt s) * ehom e j.succ ^ 2 :=
            Finset.sum_congr rfl fun j _ => by ring
        _ = -(1 / Real.sqrt s) * ∑ j : Fin d, ehom e j.succ ^ 2 := (Finset.mul_sum _ _ _).symm
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
  obtain ⟨t, ht⟩ : ∃ t : ℝ, t = ∑ j : Fin d, g j.succ ^ 2 := ⟨_, rfl⟩
  rw [← ht]
  have ht0 : 0 ≤ t := ht ▸ Finset.sum_nonneg fun j _ => sq_nonneg _
  have hsq : Real.sqrt t ^ 2 = t := Real.sq_sqrt ht0
  have hlor : Lor (Matrix.vecCons (Real.sqrt t) fun j : Fin d => -g j.succ) := by
    refine ⟨Real.sqrt_nonneg t, ?_⟩
    show ∑ j : Fin d, (-g j.succ) ^ 2 ≤ Real.sqrt t ^ 2
    rw [hsq, ht]
    exact le_of_eq (Finset.sum_congr rfl fun j _ => neg_sq _)
  have hpair := h _ hlor
  rw [Fin.sum_univ_succ] at hpair
  simp only [Matrix.cons_val_zero, Matrix.cons_val_succ] at hpair
  have hsum : ∑ j : Fin d, -g j.succ * g j.succ = -t := by
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
  simp only [prodEffVal, pairVal, cnot_apply, cnotFun_apply, prodState_apply, sum_univ_four']
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
  rw [toOp_apply, sum_univ_four']; simp +decide [phiW]
@[simp] theorem toOp_phiW_one (t : HVec 3) : toOp phiW t 1 = t 1 := by
  rw [toOp_apply, sum_univ_four']; simp +decide [phiW]
@[simp] theorem toOp_phiW_two (t : HVec 3) : toOp phiW t 2 = -t 2 := by
  rw [toOp_apply, sum_univ_four']; simp +decide [phiW]
@[simp] theorem toOp_phiW_three (t : HVec 3) : toOp phiW t 3 = t 3 := by
  rw [toOp_apply, sum_univ_four']; simp +decide [phiW]

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
  have q1 := sq_nonneg (f 0 * g 1 - g 0 * f 1)
  have q2 := sq_nonneg (f 0 * g 2 - g 0 * f 2)
  have q3 := sq_nonneg (f 0 * g 3 - g 0 * f 3)
  have s1 : f 0 * g 1 - g 0 * f 1 = 0 :=
    (pow_eq_zero_iff two_ne_zero).mp (le_antisymm (by linarith) q1)
  have s2 : f 0 * g 2 - g 0 * f 2 = 0 :=
    (pow_eq_zero_iff two_ne_zero).mp (le_antisymm (by linarith) q2)
  have s3 : f 0 * g 3 - g 0 * f 3 = 0 :=
    (pow_eq_zero_iff two_ne_zero).mp (le_antisymm (by linarith) q3)
  exact ⟨by linarith, by linarith, by linarith⟩

/-- The test vectors `(1, s eᵢ)` of the control space. -/
def tv (i : Fin 4) (s : ℝ) : HVec 3 := fun μ => if μ = 0 then 1 else if μ = i then s else 0

theorem toOp_tv1 (ω : W 3) (s : ℝ) (μ : Fin 4) : toOp ω (tv 1 s) μ = ω μ 0 + ω μ 1 * s := by
  rw [toOp_apply, sum_univ_four']; simp +decide [tv]

theorem toOp_tv2 (ω : W 3) (s : ℝ) (μ : Fin 4) : toOp ω (tv 2 s) μ = ω μ 0 + ω μ 2 * s := by
  rw [toOp_apply, sum_univ_four']; simp +decide [tv]

theorem toOp_tv3 (ω : W 3) (s : ℝ) (μ : Fin 4) : toOp ω (tv 3 s) μ = ω μ 0 + ω μ 3 * s := by
  rw [toOp_apply, sum_univ_four']; simp +decide [tv]

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
  simp +decide [toOp_tv1, tv] at a1 a2 a3 b1 b2 b3
  simp +decide [toOp_tv2, tv] at c1 c2 c3 d1 d2 d3
  simp +decide [toOp_tv3, tv] at f1 f2 f3 g1 g2 g3
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

/-! ### §O — `d = 1` is not entangling: the frame maps every pure product to a product -/

theorem fin1_ext {x y : Fin 1 → ℝ} (h : x 0 = y 0) : x = y :=
  funext fun i => by rw [Fin.fin_one_eq_zero i]; exact h

theorem corner_mem_one {z : Fin 1 → ℝ} (hz : z 0 ^ 2 = 1) : ∀ a : Fin 2, corner z a ∈ eball 1 := by
  rw [Fin.forall_fin_two]
  constructor
  · rw [corner_zero, mem_eball, Fin.sum_univ_one, hz]
  · rw [corner_one, mem_eball, Fin.sum_univ_one, Pi.neg_apply, neg_sq, hz]

/-- An extreme point of the interval is a corner. -/
theorem eq_corner_of_extreme {z : Fin 1 → ℝ} (hz : z 0 ^ 2 = 1) {x : Fin 1 → ℝ}
    (hx : x ∈ (eball 1).extremePoints ℝ) : ∃ a : Fin 2, x = corner z a := by
  have hxb : x 0 ^ 2 ≤ 1 ^ 2 := by
    have := hx.1; rw [mem_eball, Fin.sum_univ_one] at this; rwa [one_pow]
  obtain ⟨hge, hle⟩ := abs_le_of_sq_le_sq' hxb zero_le_one
  have hz' : z 0 = 1 ∨ z 0 = -1 := by
    have : (z 0 - 1) * (z 0 + 1) = 0 := by linear_combination hz
    rcases mul_eq_zero.mp this with h | h
    · left; linarith
    · right; linarith
  have hx' : x 0 = 1 ∨ x 0 = -1 := by
    rcases eq_or_lt_of_le hle with h1 | hlt
    · left; exact h1
    rcases eq_or_lt_of_le hge with h2 | hgt
    · right; exact h2.symm
    exfalso
    have hm1 : (fun _ : Fin 1 => (1 : ℝ)) ∈ eball 1 := by
      rw [mem_eball, Fin.sum_univ_one]; norm_num
    have hm2 : (fun _ : Fin 1 => (-1 : ℝ)) ∈ eball 1 := by
      rw [mem_eball, Fin.sum_univ_one]; norm_num
    have hseg : x ∈ openSegment ℝ (fun _ : Fin 1 => (1 : ℝ)) (fun _ => -1) := by
      refine ⟨(1 + x 0) / 2, (1 - x 0) / 2, by linarith, by linarith, by ring, ?_⟩
      apply fin1_ext
      simp only [Pi.add_apply, Pi.smul_apply, smul_eq_mul]
      ring
    have h1 := hx.2 hm1 hm2 hseg
    have h2 : (1 : ℝ) = x 0 := congrFun h1 0
    linarith
  rcases hx' with h | h <;> rcases hz' with hz1 | hz1
  · exact ⟨0, fin1_ext (by rw [corner_zero]; linarith)⟩
  · exact ⟨1, fin1_ext (by rw [corner_one, Pi.neg_apply]; linarith)⟩
  · exact ⟨1, fin1_ext (by rw [corner_one, Pi.neg_apply]; linarith)⟩
  · exact ⟨0, fin1_ext (by rw [corner_zero]; linarith)⟩

/-- No gate of two intervals is entangling: the frame carries every pure product input to a
product state. -/
theorem not_entangling_one {z : Fin 1 → ℝ} {N : (Fin 1 → ℝ) →ₗ[ℝ] (Fin 1 → ℝ)}
    {G : W 1 ≃ₗ[ℝ] W 1} (hN : IsNot (eball 1) z N) (hG : NativeGate (eball 1) z N G) :
    ¬ Entangling (eball 1) G := by
  rintro ⟨x, hx, y, hy, -, hnp⟩
  have hz : z 0 ^ 2 = 1 := by have := hN.unit; rwa [Fin.sum_univ_one] at this
  obtain ⟨a, rfl⟩ := eq_corner_of_extreme hz hx
  obtain ⟨b, rfl⟩ := eq_corner_of_extreme hz hy
  apply hnp
  rw [hG.frame a b]
  exact ⟨corner z a, corner_mem_one hz a, corner z (a + b), corner_mem_one hz _, rfl⟩

/-! ### §Q — the block reduction: from `NativeGate` to `BlockData` (S1, S2, S4) -/

/-- The product of two homogenized vectors as a joint vector. -/
def tens (X Y : HVec d) : W d := fun μ ν => X μ * Y ν

theorem tens_apply (X Y : HVec d) (μ ν : Fin (d + 1)) : tens X Y μ ν = X μ * Y ν := rfl

theorem prodState_eq_tens (x y : Fin d → ℝ) : prodState x y = tens (hom x) (hom y) := rfl

theorem tens_add_left (X X' Y : HVec d) : tens (X + X') Y = tens X Y + tens X' Y := by
  funext μ ν; simp only [tens_apply, Pi.add_apply]; ring

theorem tens_add_right (X Y Y' : HVec d) : tens X (Y + Y') = tens X Y + tens X Y' := by
  funext μ ν; simp only [tens_apply, Pi.add_apply]; ring

theorem tens_smul_left (c : ℝ) (X Y : HVec d) : tens (c • X) Y = c • tens X Y := by
  funext μ ν; simp only [tens_apply, Pi.smul_apply, smul_eq_mul]; ring

theorem tens_smul_right (c : ℝ) (X Y : HVec d) : tens X (c • Y) = c • tens X Y := by
  funext μ ν; simp only [tens_apply, Pi.smul_apply, smul_eq_mul]; ring

theorem tens_zero_left (Y : HVec d) : tens 0 Y = 0 := by
  funext μ ν; simp only [tens_apply, Pi.zero_apply, zero_mul]

theorem tens_zero_right (X : HVec d) : tens X 0 = 0 := by
  funext μ ν; simp only [tens_apply, Pi.zero_apply, mul_zero]

/-- The product with a fixed left factor, as a linear map in the right factor. -/
def tensL (X : HVec d) : HVec d →ₗ[ℝ] W d where
  toFun Y := tens X Y
  map_add' Y Y' := tens_add_right X Y Y'
  map_smul' c Y := tens_smul_right c X Y

theorem tensL_apply (X Y : HVec d) : tensL X Y = tens X Y := rfl

/-- The product with a fixed right factor, as a linear map in the left factor. -/
def tensR (Y : HVec d) : HVec d →ₗ[ℝ] W d where
  toFun X := tens X Y
  map_add' X X' := tens_add_left X X' Y
  map_smul' c X := tens_smul_left c X Y

theorem tensR_apply (X Y : HVec d) : tensR Y X = tens X Y := rfl

theorem pairVal_add_omega (a b : HVec d) (ω ω' : W d) :
    pairVal a b (ω + ω') = pairVal a b ω + pairVal a b ω' := by
  unfold pairVal
  rw [← Finset.sum_add_distrib]
  refine Finset.sum_congr rfl fun μ _ => ?_
  rw [← Finset.sum_add_distrib]
  refine Finset.sum_congr rfl fun ν _ => ?_
  simp only [Pi.add_apply]; ring

theorem pairVal_smul_omega (c : ℝ) (a b : HVec d) (ω : W d) :
    pairVal a b (c • ω) = c * pairVal a b ω := by
  unfold pairVal
  rw [Finset.mul_sum]
  refine Finset.sum_congr rfl fun μ _ => ?_
  rw [Finset.mul_sum]
  refine Finset.sum_congr rfl fun ν _ => ?_
  simp only [Pi.smul_apply, smul_eq_mul]; ring

theorem pairVal_zero_omega (a b : HVec d) : pairVal a b (0 : W d) = 0 := by
  unfold pairVal; simp

theorem pairVal_add_left (a a' b : HVec d) (ω : W d) :
    pairVal (a + a') b ω = pairVal a b ω + pairVal a' b ω := by
  unfold pairVal
  rw [← Finset.sum_add_distrib]
  refine Finset.sum_congr rfl fun μ _ => ?_
  rw [← Finset.sum_add_distrib]
  refine Finset.sum_congr rfl fun ν _ => ?_
  simp only [Pi.add_apply]; ring

theorem pairVal_add_right (a b b' : HVec d) (ω : W d) :
    pairVal a (b + b') ω = pairVal a b ω + pairVal a b' ω := by
  unfold pairVal
  rw [← Finset.sum_add_distrib]
  refine Finset.sum_congr rfl fun μ _ => ?_
  rw [← Finset.sum_add_distrib]
  refine Finset.sum_congr rfl fun ν _ => ?_
  simp only [Pi.add_apply]; ring

/-- The pairing with a product: the two dot products. -/
theorem pairVal_tens (a b X Y : HVec d) :
    pairVal a b (tens X Y) = (∑ μ, a μ * X μ) * ∑ ν, Y ν * b ν := by
  simp only [pairVal, tens_apply]
  rw [Finset.sum_mul_sum]
  exact Finset.sum_congr rfl fun μ _ => Finset.sum_congr rfl fun ν _ => by ring

/-- The pairing as a linear functional of the joint vector. -/
def pvOmega (a b : HVec d) : W d →ₗ[ℝ] ℝ where
  toFun ω := pairVal a b ω
  map_add' ω ω' := pairVal_add_omega a b ω ω'
  map_smul' c ω := pairVal_smul_omega c a b ω

theorem pvOmega_apply (a b : HVec d) (ω : W d) : pvOmega a b ω = pairVal a b ω := rfl

/-- The pairing as a linear functional of the left (control) effect. -/
def pvLeft (b : HVec d) (ω : W d) : HVec d →ₗ[ℝ] ℝ where
  toFun a := pairVal a b ω
  map_add' a a' := pairVal_add_left a a' b ω
  map_smul' c a := pairVal_smul_left c a b ω

theorem pvLeft_apply (a b : HVec d) (ω : W d) : pvLeft b ω a = pairVal a b ω := rfl

/-- The pairing with the unit control effect reads the first row. -/
theorem pairVal_hom_zero_left (b : HVec d) (ω : W d) :
    pairVal (hom (0 : Fin d → ℝ)) b ω = ∑ ν, b ν * ω 0 ν := by
  unfold pairVal
  rw [Fin.sum_univ_succ, hom_zero]
  simp only [hom_succ, Pi.zero_apply, zero_mul, Finset.sum_const_zero, add_zero, one_mul]
  exact Finset.sum_congr rfl fun ν _ => mul_comm _ _

theorem smul_mem_maxCone {ω : W d} (hω : ω ∈ maxCone (eball d)) {c : ℝ} (hc : 0 ≤ c) :
    c • ω ∈ maxCone (eball d) := by
  show ∀ e f, IsEffectOn (eball d) e → IsEffectOn (eball d) f → 0 ≤ prodEffVal e f (c • ω)
  intro e f he hf
  have := hω e f he hf
  unfold prodEffVal at this ⊢
  rw [pairVal_smul_omega]
  exact mul_nonneg hc this

theorem zero_mem_maxCone : (0 : W d) ∈ maxCone (eball d) := by
  show ∀ e f, IsEffectOn (eball d) e → IsEffectOn (eball d) f → 0 ≤ prodEffVal e f (0 : W d)
  intro e f _ _
  unfold prodEffVal
  rw [pairVal_zero_omega]

/-- A cone vector with vanishing head is zero. -/
theorem lor_eq_zero_of_head {X : HVec d} (hX : Lor X) (h0 : X 0 = 0) : X = 0 := by
  have hs : ∑ j : Fin d, X j.succ ^ 2 ≤ 0 := by
    have := hX.2; rw [h0, zero_pow two_ne_zero] at this; exact this
  have hz : ∀ j : Fin d, X j.succ = 0 := by
    intro j
    have := (Finset.sum_eq_zero_iff_of_nonneg (fun j _ => sq_nonneg (X j.succ))).1
      (le_antisymm hs (Finset.sum_nonneg fun j _ => sq_nonneg _)) j (Finset.mem_univ _)
    exact (pow_eq_zero_iff two_ne_zero).mp this
  funext μ
  refine Fin.cases ?_ (fun j => ?_) μ
  · exact h0
  · exact hz j

/-- A cone vector with positive head is a positive multiple of a ball point. -/
theorem lor_eq_smul_hom {X : HVec d} (hX : Lor X) (hpos : 0 < X 0) :
    X = X 0 • hom (fun j => (X 0)⁻¹ * X j.succ) ∧ (fun j => (X 0)⁻¹ * X j.succ) ∈ eball d := by
  constructor
  · funext μ
    refine Fin.cases ?_ (fun j => ?_) μ
    · rw [Pi.smul_apply, hom_zero, smul_eq_mul, mul_one]
    · simp only [Pi.smul_apply, hom_succ, smul_eq_mul]
      rw [← mul_assoc, mul_inv_cancel₀ hpos.ne', one_mul]
  · rw [mem_eball]
    have h1 : ∑ j : Fin d, ((X 0)⁻¹ * X j.succ) ^ 2 = (X 0)⁻¹ ^ 2 * ∑ j : Fin d, X j.succ ^ 2 := by
      rw [Finset.mul_sum]; exact Finset.sum_congr rfl fun j _ => by ring
    rw [h1]
    calc (X 0)⁻¹ ^ 2 * ∑ j : Fin d, X j.succ ^ 2 ≤ (X 0)⁻¹ ^ 2 * X 0 ^ 2 :=
          mul_le_mul_of_nonneg_left hX.2 (sq_nonneg _)
      _ = 1 := by rw [← mul_pow, inv_mul_cancel₀ hpos.ne', one_pow]

/-- **Positivity transfer.** A linear map sending product states of the ball into the maximal
cone sends every product of two cone vectors into the maximal cone. -/
theorem tens_mem_maxCone {G' : W d →ₗ[ℝ] W d}
    (hpos : ∀ x ∈ eball d, ∀ y ∈ eball d, G' (prodState x y) ∈ maxCone (eball d))
    {X Y : HVec d} (hX : Lor X) (hY : Lor Y) : G' (tens X Y) ∈ maxCone (eball d) := by
  rcases eq_or_lt_of_le hX.1 with hx0 | hxpos
  · rw [lor_eq_zero_of_head hX hx0.symm, tens_zero_left, map_zero]; exact zero_mem_maxCone
  rcases eq_or_lt_of_le hY.1 with hy0 | hypos
  · rw [lor_eq_zero_of_head hY hy0.symm, tens_zero_right, map_zero]; exact zero_mem_maxCone
  obtain ⟨hXe, hxm⟩ := lor_eq_smul_hom hX hxpos
  obtain ⟨hYe, hym⟩ := lor_eq_smul_hom hY hypos
  rw [hXe, hYe, tens_smul_left, tens_smul_right, smul_smul, ← prodState_eq_tens, map_smul]
  exact smul_mem_maxCone (hpos _ hxm _ hym) (mul_nonneg hxpos.le hypos.le)

/-- Positivity of the gate on four cone vectors. -/
theorem gate_pairVal_nonneg {G' : W d →ₗ[ℝ] W d}
    (hpos : ∀ x ∈ eball d, ∀ y ∈ eball d, G' (prodState x y) ∈ maxCone (eball d))
    {a X b Y : HVec d} (ha : Lor a) (hX : Lor X) (hb : Lor b) (hY : Lor Y) :
    0 ≤ pairVal a b (G' (tens X Y)) :=
  pairVal_nonneg_of_maxCone (tens_mem_maxCone hpos hX hY) ha hb

/-- The standard basis vector of the homogenized space. -/
def bvec (i : Fin (d + 1)) : HVec d := fun k => if i = k then 1 else 0

theorem bvec_apply (i k : Fin (d + 1)) : bvec i k = if i = k then (1 : ℝ) else 0 := rfl

theorem bvec_zero_eq : bvec (0 : Fin (d + 1)) = hom (0 : Fin d → ℝ) := by
  funext μ
  refine Fin.cases ?_ (fun j => ?_) μ
  · rw [bvec_apply, if_pos rfl, hom_zero]
  · rw [bvec_apply, if_neg (Fin.succ_ne_zero j).symm, hom_succ, Pi.zero_apply]

/-- The tangent lift `(0, c)`. -/
def lift (c : Fin d → ℝ) : HVec d := Matrix.vecCons 0 c

@[simp] theorem lift_zero (c : Fin d → ℝ) : lift c 0 = 0 := rfl

@[simp] theorem lift_succ (c : Fin d → ℝ) (j : Fin d) : lift c j.succ = c j :=
  Matrix.cons_val_succ _ _ _

theorem hom_eq_add_lift (x : Fin d → ℝ) : hom x = hom 0 + lift x := by
  funext μ
  refine Fin.cases ?_ (fun j => ?_) μ
  · rw [Pi.add_apply, hom_zero, hom_zero, lift_zero, add_zero]
  · rw [Pi.add_apply, hom_succ, hom_succ, lift_succ, Pi.zero_apply, zero_add]

theorem lift_add (c c' : Fin d → ℝ) : lift (c + c') = lift c + lift c' := by
  funext μ
  refine Fin.cases ?_ (fun j => ?_) μ
  · rw [Pi.add_apply, lift_zero, lift_zero, lift_zero, add_zero]
  · rw [Pi.add_apply, lift_succ, lift_succ, lift_succ, Pi.add_apply]

theorem lift_smul (c : ℝ) (x : Fin d → ℝ) : lift (c • x) = c • lift x := by
  funext μ
  refine Fin.cases ?_ (fun j => ?_) μ
  · rw [Pi.smul_apply, lift_zero, lift_zero, smul_zero]
  · rw [Pi.smul_apply, lift_succ, lift_succ, Pi.smul_apply]

theorem lift_neg (x : Fin d → ℝ) : lift (-x) = -lift x := by
  funext μ
  refine Fin.cases ?_ (fun j => ?_) μ
  · rw [Pi.neg_apply, lift_zero, lift_zero, neg_zero]
  · rw [Pi.neg_apply, lift_succ, lift_succ, Pi.neg_apply]

theorem lift_vecTail {u : HVec d} (h : u 0 = 0) : lift (Matrix.vecTail u) = u := by
  funext μ
  refine Fin.cases ?_ (fun j => ?_) μ
  · rw [lift_zero, h]
  · rw [lift_succ]; rfl

theorem lor_hom_zero : Lor (hom (0 : Fin d → ℝ)) :=
  ⟨by rw [hom_zero]; exact zero_le_one, by simp [hom_succ]⟩

theorem lor_hom {x : Fin d → ℝ} (hx : x ∈ eball d) : Lor (hom x) := by
  refine ⟨by rw [hom_zero]; exact zero_le_one, ?_⟩
  rw [hom_zero, one_pow]
  simp only [hom_succ]
  exact mem_eball.mp hx

theorem lor_hom_of_unit {x : Fin d → ℝ} (hx : ∑ j, x j ^ 2 = 1) : Lor (hom x) :=
  lor_hom (mem_eball.mpr hx.le)

theorem lor_hom_zero_add_smul_bvec (j : Fin d) {s : ℝ} (hs : s ^ 2 ≤ 1) :
    Lor (hom (0 : Fin d → ℝ) + s • bvec j.succ) := by
  have h0 : (hom (0 : Fin d → ℝ) + s • bvec j.succ) 0 = 1 := by
    rw [Pi.add_apply, hom_zero, Pi.smul_apply, bvec_apply, if_neg (Fin.succ_ne_zero j),
      smul_zero, add_zero]
  have ht : ∀ k : Fin d,
      (hom (0 : Fin d → ℝ) + s • bvec j.succ) k.succ ^ 2 = if j = k then s ^ 2 else 0 := by
    intro k
    rw [Pi.add_apply, hom_succ, Pi.zero_apply, zero_add, Pi.smul_apply, smul_eq_mul, bvec_apply]
    by_cases hjk : j = k
    · subst hjk; rw [if_pos rfl, if_pos rfl, mul_one]
    · rw [if_neg (fun h => hjk (Fin.succ_inj.mp h)), if_neg hjk, mul_zero, zero_pow two_ne_zero]
  refine ⟨by rw [h0]; exact zero_le_one, ?_⟩
  rw [h0, one_pow, Finset.sum_congr rfl fun k _ => ht k, Finset.sum_ite_eq]
  simpa using hs

/-- A linear functional nonnegative on the cone and vanishing at the centre vanishes. -/
theorem linearMap_eq_zero_of_nonneg_lor (F : HVec d →ₗ[ℝ] ℝ) (hpos : ∀ X, Lor X → 0 ≤ F X)
    (h0 : F (hom 0) = 0) : F = 0 := by
  have hb : ∀ i : Fin (d + 1), F (bvec i) = 0 := by
    intro i
    refine Fin.cases ?_ (fun j => ?_) i
    · rw [bvec_zero_eq]; exact h0
    · have h1 := hpos _ (lor_hom_zero_add_smul_bvec j (s := 1) (by norm_num))
      have h2 := hpos _ (lor_hom_zero_add_smul_bvec j (s := -1) (by norm_num))
      rw [map_add, map_smul, h0, zero_add, one_smul] at h1
      rw [map_add, map_smul, h0, zero_add, smul_eq_mul] at h2
      linarith
  apply LinearMap.ext; intro X
  rw [LinearMap.pi_apply_eq_sum_univ F X, LinearMap.zero_apply]
  exact Finset.sum_eq_zero fun i _ => by
    rw [show (fun j => if i = j then (1 : ℝ) else 0) = bvec i from rfl, hb i, smul_zero]

/-- A linear map vanishing on the cone vanishes. -/
theorem linearMap_eq_zero_of_lor {E : Type*} [AddCommGroup E] [Module ℝ E] (F : HVec d →ₗ[ℝ] E)
    (h : ∀ X, Lor X → F X = 0) : F = 0 := by
  have hb : ∀ i : Fin (d + 1), F (bvec i) = 0 := by
    intro i
    refine Fin.cases ?_ (fun j => ?_) i
    · rw [bvec_zero_eq]; exact h _ lor_hom_zero
    · have h1 := h _ (lor_hom_zero_add_smul_bvec j (s := 1) (by norm_num))
      rwa [map_add, map_smul, h _ lor_hom_zero, zero_add, one_smul] at h1
  apply LinearMap.ext; intro X
  rw [LinearMap.pi_apply_eq_sum_univ F X, LinearMap.zero_apply]
  exact Finset.sum_eq_zero fun i _ => by
    rw [show (fun j => if i = j then (1 : ℝ) else 0) = bvec i from rfl, hb i, smul_zero]

theorem hom_add_hom_neg (z : Fin d → ℝ) : hom z + hom (-z) = (2 : ℝ) • hom 0 := by
  funext μ
  refine Fin.cases ?_ (fun j => ?_) μ
  · simp only [Pi.add_apply, Pi.smul_apply, hom_zero, smul_eq_mul]; norm_num
  · simp only [Pi.add_apply, Pi.smul_apply, hom_succ, Pi.neg_apply, Pi.zero_apply, smul_eq_mul]
    ring

/-- The two corners are orthogonal as homogenized vectors. -/
theorem dot_hom_neg_hom {z : Fin d → ℝ} (hz : ∑ j, z j ^ 2 = 1) :
    ∑ μ, hom (-z) μ * hom z μ = 0 := by
  rw [Fin.sum_univ_succ, hom_zero, hom_zero, one_mul]
  simp only [hom_succ, Pi.neg_apply]
  have : ∑ j, -z j * z j = -∑ j, z j ^ 2 := by
    rw [← Finset.sum_neg_distrib]; exact Finset.sum_congr rfl fun j _ => by ring
  rw [this, hz]; ring

theorem dot_hom_hom_neg {z : Fin d → ℝ} (hz : ∑ j, z j ^ 2 = 1) :
    ∑ μ, hom z μ * hom (-z) μ = 0 := by
  rw [← dot_hom_neg_hom hz]; exact Finset.sum_congr rfl fun μ _ => mul_comm _ _

/-- **The corner face.** A cone vector annihilated by the antipodal corner effect lies on the
corner ray. -/
theorem lor_face {z : Fin d → ℝ} (hz : ∑ j, z j ^ 2 = 1) {m : HVec d} (hm : Lor m)
    (h : ∑ μ, hom (-z) μ * m μ = 0) : m = m 0 • hom z := by
  have hdot : ∑ j, z j * m j.succ = m 0 := by
    rw [Fin.sum_univ_succ, hom_zero, one_mul] at h
    simp only [hom_succ, Pi.neg_apply] at h
    have : ∑ j, -z j * m j.succ = -∑ j, z j * m j.succ := by
      rw [← Finset.sum_neg_distrib]; exact Finset.sum_congr rfl fun j _ => by ring
    linarith
  have hcs : (∑ j, z j * m j.succ) ^ 2 ≤ (∑ j, z j ^ 2) * ∑ j : Fin d, m j.succ ^ 2 :=
    Finset.sum_mul_sq_le_sq_mul_sq Finset.univ z (fun j : Fin d => m j.succ)
  rw [hdot, hz, one_mul] at hcs
  have hsq : ∑ j : Fin d, m j.succ ^ 2 = m 0 ^ 2 := le_antisymm hm.2 hcs
  have hzero : ∑ j : Fin d, (m j.succ - m 0 * z j) ^ 2 = 0 := by
    have : ∀ j : Fin d, (m j.succ - m 0 * z j) ^ 2
        = m j.succ ^ 2 - 2 * m 0 * (z j * m j.succ) + m 0 ^ 2 * z j ^ 2 := fun j => by ring
    rw [Finset.sum_congr rfl fun j _ => this j, Finset.sum_add_distrib, Finset.sum_sub_distrib,
      ← Finset.mul_sum, ← Finset.mul_sum, hdot, hz, hsq]
    ring
  funext μ
  refine Fin.cases ?_ (fun j => ?_) μ
  · rw [Pi.smul_apply, hom_zero, smul_eq_mul, mul_one]
  · have := (Finset.sum_eq_zero_iff_of_nonneg (fun j _ => sq_nonneg (m j.succ - m 0 * z j))).1
      hzero j (Finset.mem_univ _)
    have h2 := (pow_eq_zero_iff two_ne_zero).mp this
    rw [Pi.smul_apply, hom_succ, smul_eq_mul]
    linarith

theorem tens_hom_inj {x : Fin d → ℝ} {Y Y' : HVec d} (h : tens (hom x) Y = tens (hom x) Y') :
    Y = Y' := by
  funext ν
  have := congrFun (congrFun h 0) ν
  rwa [tens_apply, tens_apply, hom_zero, one_mul, one_mul] at this

theorem toOp_bvec (ω : W d) (ν μ : Fin (d + 1)) : toOp ω (bvec ν) μ = ω μ ν := by
  rw [toOp_apply]
  simp only [bvec_apply, mul_ite, mul_one, mul_zero]
  rw [Finset.sum_ite_eq]
  simp

/-- The target map on a corner slice: the first row of `G' (hom z ⊗ Y)`. -/
def cornerMap (z : Fin d → ℝ) (G' : W d →ₗ[ℝ] W d) : HVec d →ₗ[ℝ] HVec d :=
  (LinearMap.proj (0 : Fin (d + 1)) : W d →ₗ[ℝ] HVec d) ∘ₗ G' ∘ₗ tensL (hom z)

theorem cornerMap_apply (z : Fin d → ℝ) (G' : W d →ₗ[ℝ] W d) (Y : HVec d) :
    cornerMap z G' Y = G' (tens (hom z) Y) 0 := rfl

/-- **S1, the controlled form.** A linear map with the frame on the corner `z` slice and product
positivity acts on that slice as `hom z ⊗ (·)`: the control output is the corner itself. -/
theorem corner_form {z : Fin d → ℝ} (hz : ∑ j, z j ^ 2 = 1) {G' : W d →ₗ[ℝ] W d}
    (hframe : ∀ b : Fin 2, G' (prodState z (corner z b)) = prodState z (corner z b))
    (hpos : ∀ x ∈ eball d, ∀ y ∈ eball d, G' (prodState x y) ∈ maxCone (eball d)) (Y : HVec d) :
    G' (tens (hom z) Y) = tens (hom z) (cornerMap z G' Y) := by
  have hzl : Lor (hom z) := lor_hom_of_unit hz
  have hzl' : Lor (hom (-z)) := lor_hom_of_unit (by simpa [neg_sq] using hz)
  have hA : ∀ f, Lor f → ∀ Y, pairVal (hom (-z)) f (G' (tens (hom z) Y)) = 0 := by
    intro f hf
    let F : HVec d →ₗ[ℝ] ℝ := pvOmega (hom (-z)) f ∘ₗ G' ∘ₗ tensL (hom z)
    have hF : ∀ Y, F Y = pairVal (hom (-z)) f (G' (tens (hom z) Y)) := fun Y => rfl
    have hFpos : ∀ X, Lor X → 0 ≤ F X := fun X hX => by
      rw [hF]; exact gate_pairVal_nonneg hpos hzl' hzl hf hX
    have hk : ∀ b : Fin 2, F (hom (corner z b)) = 0 := by
      intro b
      rw [hF, ← prodState_eq_tens, hframe b, prodState_eq_tens, pairVal_tens, dot_hom_neg_hom hz,
        zero_mul]
    have h0 : F (hom 0) = 0 := by
      have h2 : F ((2 : ℝ) • hom 0) = 0 := by
        rw [← hom_add_hom_neg, map_add]
        have hk0 := hk 0
        have hk1 := hk 1
        rw [corner_zero] at hk0
        rw [corner_one] at hk1
        rw [hk0, hk1, add_zero]
      rw [map_smul, smul_eq_mul] at h2
      linarith
    have hF0 := linearMap_eq_zero_of_nonneg_lor F hFpos h0
    intro Y
    rw [← hF, hF0, LinearMap.zero_apply]
  have hB : ∀ Y, Lor Y → ∀ f, Lor f →
      toOp (G' (tens (hom z) Y)) f = (toOp (G' (tens (hom z) Y)) f 0) • hom z := by
    intro Y hY f hf
    apply lor_face hz (lor_toOp_of_maxCone (tens_mem_maxCone hpos hzl hY) hf)
    rw [← pairVal_eq_sum_toOp]
    exact hA f hf Y
  have hC : ∀ Y, Lor Y → ∀ f,
      toOp (G' (tens (hom z) Y)) f = (toOp (G' (tens (hom z) Y)) f 0) • hom z := by
    intro Y hY
    have hD := linearMap_eq_zero_of_lor
      (toOp (G' (tens (hom z) Y))
        - ((LinearMap.proj (0 : Fin (d + 1)) : HVec d →ₗ[ℝ] ℝ) ∘ₗ
            toOp (G' (tens (hom z) Y))).smulRight (hom z))
      (fun f hf => by
        rw [LinearMap.sub_apply, LinearMap.smulRight_apply, LinearMap.comp_apply,
          LinearMap.proj_apply]
        exact sub_eq_zero.mpr (hB Y hY f hf))
    intro f
    have := LinearMap.congr_fun hD f
    rwa [LinearMap.sub_apply, LinearMap.smulRight_apply, LinearMap.comp_apply,
      LinearMap.proj_apply, LinearMap.zero_apply, sub_eq_zero] at this
  have hE : ∀ Y, Lor Y → G' (tens (hom z) Y) = tens (hom z) (cornerMap z G' Y) := by
    intro Y hY
    funext μ ν
    have := congrFun (hC Y hY (bvec ν)) μ
    rw [toOp_bvec, Pi.smul_apply, toOp_bvec, smul_eq_mul] at this
    rw [this, tens_apply, cornerMap_apply, mul_comm]
  have hF := linearMap_eq_zero_of_lor (G' ∘ₗ tensL (hom z) - tensL (hom z) ∘ₗ cornerMap z G')
    (fun Y hY => by
      rw [LinearMap.sub_apply, LinearMap.comp_apply, LinearMap.comp_apply, tensL_apply,
        tensL_apply, hE Y hY, sub_self])
  have := LinearMap.congr_fun hF Y
  rwa [LinearMap.sub_apply, LinearMap.comp_apply, LinearMap.comp_apply, tensL_apply, tensL_apply,
    LinearMap.zero_apply, sub_eq_zero] at this

/-- The corner map carries the cone into itself. -/
theorem lor_cornerMap {z : Fin d → ℝ} (hz : ∑ j, z j ^ 2 = 1) {G' : W d →ₗ[ℝ] W d}
    (hpos : ∀ x ∈ eball d, ∀ y ∈ eball d, G' (prodState x y) ∈ maxCone (eball d))
    {Y : HVec d} (hY : Lor Y) : Lor (cornerMap z G' Y) :=
  lor_of_forall_pair fun a ha => by
    rw [cornerMap_apply, ← pairVal_hom_zero_left]
    exact pairVal_nonneg_of_maxCone (tens_mem_maxCone hpos (lor_hom_of_unit hz) hY) lor_hom_zero ha

/-- The forward target map `M₀` of the gate on the corner `z` slice. -/
def Mfwd (z : Fin d → ℝ) (G : W d ≃ₗ[ℝ] W d) : HVec d →ₗ[ℝ] HVec d :=
  cornerMap z (G : W d →ₗ[ℝ] W d)

/-- The target map of the inverse gate on the corner `z` slice. -/
def Minv (z : Fin d → ℝ) (G : W d ≃ₗ[ℝ] W d) : HVec d →ₗ[ℝ] HVec d :=
  cornerMap z (G.symm : W d →ₗ[ℝ] W d)

theorem gate_corner {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}
    (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) (Y : HVec d) :
    G (tens (hom z) Y) = tens (hom z) (Mfwd z G Y) :=
  corner_form hN.unit
    (fun b => by
      have h := hG.frame 0 b
      rw [corner_zero, zero_add] at h
      exact h)
    (fun x hx y hy => hG.posFwd x hx y hy) Y

theorem gate_corner_symm {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}
    (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) (Y : HVec d) :
    G.symm (tens (hom z) Y) = tens (hom z) (Minv z G Y) :=
  corner_form hN.unit
    (fun b => by
      have h := hG.frame 0 b
      rw [corner_zero, zero_add] at h
      calc G.symm (prodState z (corner z b)) = G.symm (G (prodState z (corner z b))) := by rw [h]
        _ = prodState z (corner z b) := G.symm_apply_apply _)
    (fun x hx y hy => hG.posInv x hx y hy) Y

theorem Mfwd_Minv {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}
    (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) (Y : HVec d) :
    Mfwd z G (Minv z G Y) = Y := by
  apply tens_hom_inj (x := z)
  rw [← gate_corner hN hG, ← gate_corner_symm hN hG, G.apply_symm_apply]

theorem Minv_Mfwd {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}
    (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) (Y : HVec d) :
    Minv z G (Mfwd z G Y) = Y := by
  apply tens_hom_inj (x := z)
  rw [← gate_corner_symm hN hG, ← gate_corner hN hG, G.symm_apply_apply]

theorem lor_Minv {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}
    (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) {Y : HVec d} (hY : Lor Y) :
    Lor (Minv z G Y) :=
  lor_cornerMap hN.unit (fun x hx y hy => hG.posInv x hx y hy) hY

theorem actT_tens (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (X Y : HVec d) :
    actT N (tens X Y) = tens X (homMap N Y) := by
  funext μ ν
  show homMap N (fun ν => X μ * Y ν) ν = X μ * homMap N Y ν
  have : (fun ν => X μ * Y ν) = X μ • Y := rfl
  rw [this, map_smul, Pi.smul_apply, smul_eq_mul]

theorem actC_tens (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (X Y : HVec d) :
    actC N (tens X Y) = tens (homMap N X) Y := by
  funext μ ν
  show homMap N (fun κ => tens X Y κ ν) μ = homMap N X μ * Y ν
  have : (fun κ => tens X Y κ ν) = Y ν • X := by
    funext κ; simp only [tens_apply, Pi.smul_apply, smul_eq_mul]; ring
  rw [this, map_smul, Pi.smul_apply, smul_eq_mul, mul_comm]

theorem gate_actT {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}
    (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) (ω : W d) :
    G (actT N ω) = actT N (G ω) := by
  have h := hG.relT (actT N ω)
  rw [actT_actT hN.invol] at h
  exact h.symm

theorem gate_actC {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}
    (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) (ω : W d) :
    G (actC N ω) = actC N (actT N (G ω)) := by
  have h2 := congrArg (actC N) (hG.relC ω)
  rwa [actC_actC hN.invol] at h2

/-- Rt on the corner map: `M₀` commutes with the homogenized NOT. -/
theorem Mfwd_homMap {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}
    (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) (Y : HVec d) :
    Mfwd z G (homMap N Y) = homMap N (Mfwd z G Y) := by
  apply tens_hom_inj (x := z)
  rw [← gate_corner hN hG, ← actT_tens N (hom z) Y, gate_actT hN hG (tens (hom z) Y),
    gate_corner hN hG Y, actT_tens N (hom z) (Mfwd z G Y)]

theorem Minv_homMap {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}
    (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) (Y : HVec d) :
    Minv z G (homMap N Y) = homMap N (Minv z G Y) := by
  conv_lhs => rw [← Mfwd_Minv hN hG Y, ← Mfwd_homMap hN hG, Minv_Mfwd hN hG]

/-- Rc on the corner `−z` slice: the target map there is `N M₀`. -/
theorem gate_corner_neg {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}
    (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) (Y : HVec d) :
    G (tens (hom (-z)) Y) = tens (hom (-z)) (homMap N (Mfwd z G Y)) := by
  have hz' : homMap N (hom z) = hom (-z) := by rw [homMap_hom, hN.flips]
  rw [← hz', ← actC_tens N (hom z) Y, gate_actC hN hG (tens (hom z) Y), gate_corner hN hG Y,
    actT_tens N (hom z) (Mfwd z G Y), actC_tens N (hom z) (homMap N (Mfwd z G Y))]

/-- The normalized gate `G (I ⊗ M₀⁻¹)` on the corner `z` slice is the identity. -/
theorem gt_corner {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}
    (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) (t : HVec d) :
    G (tens (hom z) (Minv z G t)) = tens (hom z) t := by
  rw [gate_corner hN hG, Mfwd_Minv hN hG]

/-- The normalized gate on the corner `−z` slice is `I ⊗ N`. -/
theorem gt_corner_neg {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}
    (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) (t : HVec d) :
    G (tens (hom (-z)) (Minv z G t)) = tens (hom (-z)) (homMap N t) := by
  rw [gate_corner_neg hN hG, Mfwd_Minv hN hG]

theorem eq_of_two_smul_eq {A B : W d} (h : (2 : ℝ) • A = (2 : ℝ) • B) : A = B := by
  have hA : ((1 / 2 : ℝ) * 2) • A = A := by norm_num
  have hB : ((1 / 2 : ℝ) * 2) • B = B := by norm_num
  rw [← hA, ← hB, ← smul_smul, ← smul_smul, h]

/-- The normalized gate on the centre slice fixes every `+1` eigenvector of the target. -/
theorem gt_center {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}
    (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) {t : HVec d}
    (ht : homMap N t = t) : G (tens (hom 0) (Minv z G t)) = tens (hom 0) t := by
  apply eq_of_two_smul_eq
  rw [← map_smul, ← tens_smul_left 2 (hom 0) (Minv z G t), ← hom_add_hom_neg z, tens_add_left,
    map_add, gt_corner hN hG,
    gt_corner_neg hN hG, ht, ← tens_add_left, hom_add_hom_neg z, tens_smul_left]

/-- `0 ≤ α s² + β s` for every `s`, with `0 ≤ α`, forces `β = 0`. -/
theorem eq_zero_of_quadratic_nonneg {α β : ℝ} (hα : 0 ≤ α)
    (h : ∀ s : ℝ, 0 ≤ α * s ^ 2 + β * s) : β = 0 := by
  by_contra hβ
  have hpos : 0 < α + 1 := by linarith
  have hne : α + 1 ≠ 0 := hpos.ne'
  have hs1 : (α + 1) * (-β / (α + 1)) = -β := by field_simp
  have key := h (-β / (α + 1))
  obtain ⟨s, hs⟩ : ∃ s : ℝ, s = -β / (α + 1) := ⟨_, rfl⟩
  rw [← hs] at hs1 key
  have hαs : α * s = -β - s := by
    have h' : α * s + s = -β := by rw [← hs1]; ring
    linarith
  have hval : α * s ^ 2 + β * s = -(s ^ 2) := by
    calc α * s ^ 2 + β * s = s * (α * s + β) := by ring
      _ = -(s ^ 2) := by rw [hαs]; ring
  rw [hval] at key
  have hs2 : s ^ 2 = 0 := le_antisymm (by linarith) (sq_nonneg s)
  have hs0 : s = 0 := (pow_eq_zero_iff two_ne_zero).mp hs2
  rw [hs0, mul_zero] at hs1
  exact hβ (neg_eq_zero.mp hs1.symm)

/-- The boundary curve through the corner `w` in a tangent direction `c` of norm at most one:
every point is a cone vector. -/
theorem lor_curve {w c : Fin d → ℝ} (hw : ∑ j, w j ^ 2 = 1) (hc : ∑ j, c j ^ 2 ≤ 1)
    (hwc : ∑ j, w j * c j = 0) (s : ℝ) :
    Lor ((1 + s ^ 2) • hom (0 : Fin d → ℝ) + (1 - s ^ 2) • lift w + (2 * s) • lift c) := by
  set X : HVec d := (1 + s ^ 2) • hom (0 : Fin d → ℝ) + (1 - s ^ 2) • lift w + (2 * s) • lift c
    with hX
  have hhead : X 0 = 1 + s ^ 2 := by
    rw [hX]
    simp only [Pi.add_apply, Pi.smul_apply, hom_zero, lift_zero, smul_eq_mul]
    ring
  have htail : ∀ j : Fin d, X j.succ = (1 - s ^ 2) * w j + 2 * s * c j := by
    intro j
    rw [hX]
    simp only [Pi.add_apply, Pi.smul_apply, hom_succ, lift_succ, Pi.zero_apply, smul_eq_mul]
    ring
  have hsum : ∑ j : Fin d, X j.succ ^ 2 = ∑ j : Fin d, ((1 - s ^ 2) * w j + 2 * s * c j) ^ 2 :=
    Finset.sum_congr rfl fun j _ => by rw [htail j]
  have hexp : ∑ j : Fin d, ((1 - s ^ 2) * w j + 2 * s * c j) ^ 2
      = (1 - s ^ 2) ^ 2 * ∑ j, w j ^ 2 + 2 * ((1 - s ^ 2) * (2 * s)) * ∑ j, w j * c j
        + (2 * s) ^ 2 * ∑ j, c j ^ 2 := by
    rw [Finset.mul_sum, Finset.mul_sum, Finset.mul_sum, ← Finset.sum_add_distrib,
      ← Finset.sum_add_distrib]
    exact Finset.sum_congr rfl fun j _ => by ring
  refine ⟨by rw [hhead]; positivity, ?_⟩
  rw [hhead, hsum, hexp, hw, hwc]
  have hid : (1 - s ^ 2) ^ 2 + (2 * s) ^ 2 = (1 + s ^ 2) ^ 2 := by ring
  nlinarith [hid, mul_le_mul_of_nonneg_left hc (sq_nonneg (2 * s))]

/-- **The tangent argument.** A linear functional nonnegative on the cone and vanishing at the
boundary point `hom w` vanishes on every tangent direction at `w`. -/
theorem tangent_vanish (F : HVec d →ₗ[ℝ] ℝ) (hpos : ∀ X, Lor X → 0 ≤ F X) {w c : Fin d → ℝ}
    (hw : ∑ j, w j ^ 2 = 1) (hc : ∑ j, c j ^ 2 ≤ 1) (hwc : ∑ j, w j * c j = 0)
    (h0 : F (hom w) = 0) : F (lift c) = 0 := by
  have hF0 : 0 ≤ F (hom 0) := hpos _ lor_hom_zero
  have hsum : F (hom 0) + F (lift w) = 0 := by rw [← map_add, ← hom_eq_add_lift w]; exact h0
  have hq : ∀ s : ℝ, 0 ≤ (2 * F (hom 0)) * s ^ 2 + (2 * F (lift c)) * s := by
    intro s
    have h := hpos _ (lor_curve hw hc hwc s)
    simp only [map_add, map_smul, smul_eq_mul] at h
    have hid : (1 + s ^ 2) * F (hom 0) + (1 - s ^ 2) * F (lift w) + 2 * s * F (lift c)
        = (2 * F (hom 0)) * s ^ 2 + (2 * F (lift c)) * s
          + (F (hom 0) + F (lift w)) * (1 - s ^ 2) := by ring
    rw [hid, hsum, zero_mul, add_zero] at h
    exact h
  have := eq_zero_of_quadratic_nonneg (by linarith) hq
  linarith

/-- **S2, first step.** On a tangent control slice the normalized gate's control output is
orthogonal to both corners, for cone-valued target data. -/
theorem gt_tangent_corners {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}
    (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) {c : Fin d → ℝ}
    (hc : ∑ j, c j ^ 2 ≤ 1) (hzc : ∑ j, z j * c j = 0) {f t : HVec d} (hf : Lor f) (ht : Lor t) :
    pairVal (hom (-z)) f (G (tens (lift c) (Minv z G t))) = 0 ∧
    pairVal (hom z) f (G (tens (lift c) (Minv z G t))) = 0 := by
  have hzl : Lor (hom z) := lor_hom_of_unit hN.unit
  have hz' : ∑ j, (-z) j ^ 2 = 1 := by simpa [neg_sq] using hN.unit
  have hzc' : ∑ j, (-z) j * c j = 0 := by
    simp only [Pi.neg_apply, neg_mul, Finset.sum_neg_distrib, hzc, neg_zero]
  have hzl' : Lor (hom (-z)) := lor_hom_of_unit hz'
  have hMt : Lor (Minv z G t) := lor_Minv hN hG ht
  have hpos : ∀ x ∈ eball d, ∀ y ∈ eball d,
      (G : W d →ₗ[ℝ] W d) (prodState x y) ∈ maxCone (eball d) :=
    fun x hx y hy => hG.posFwd x hx y hy
  constructor
  · let F : HVec d →ₗ[ℝ] ℝ := pvOmega (hom (-z)) f ∘ₗ (G : W d →ₗ[ℝ] W d) ∘ₗ tensR (Minv z G t)
    have hF : ∀ X, F X = pairVal (hom (-z)) f (G (tens X (Minv z G t))) := fun X => rfl
    have hFpos : ∀ X, Lor X → 0 ≤ F X := fun X hX => by
      rw [hF]; exact gate_pairVal_nonneg hpos hzl' hX hf hMt
    have h0 : F (hom z) = 0 := by
      rw [hF, gt_corner hN hG, pairVal_tens, dot_hom_neg_hom hN.unit, zero_mul]
    rw [← hF]
    exact tangent_vanish F hFpos hN.unit hc hzc h0
  · let F : HVec d →ₗ[ℝ] ℝ := pvOmega (hom z) f ∘ₗ (G : W d →ₗ[ℝ] W d) ∘ₗ tensR (Minv z G t)
    have hF : ∀ X, F X = pairVal (hom z) f (G (tens X (Minv z G t))) := fun X => rfl
    have hFpos : ∀ X, Lor X → 0 ≤ F X := fun X hX => by
      rw [hF]; exact gate_pairVal_nonneg hpos hzl hX hf hMt
    have h0 : F (hom (-z)) = 0 := by
      rw [hF, gt_corner_neg hN hG, pairVal_tens, dot_hom_hom_neg hN.unit, zero_mul]
    rw [← hF]
    exact tangent_vanish F hFpos hz' hc hzc' h0

/-- **S2, the sphere identity at the corner `z`.** For a unit tangent target direction `u`, the
antipodal target effect annihilates the normalized gate's image of the tangent slice. -/
theorem gt_sphere {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}
    (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) {c : Fin d → ℝ}
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
    exact gate_pairVal_nonneg hpos ha hX (lor_hom_of_unit hτ') (lor_Minv hN hG (lor_hom_of_unit hτ))
  have h0 : F (hom z) = 0 := by
    rw [hF, gt_corner hN hG, pairVal_tens, dot_hom_hom_neg hτ, mul_zero]
  rw [← hF]
  exact tangent_vanish F hFpos hN.unit hc hzc h0

/-- **S2, the sphere identity at the corner `−z`**, evaluated at the two corner target states. -/
theorem gt_sphere_corner {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}
    (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) {c : Fin d → ℝ}
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
        (lor_Minv hN hG (lor_hom_of_unit hN.unit))
    have h0 : F (hom (-z)) = 0 := by
      rw [hF, gt_corner_neg hN hG, hNz, pairVal_tens, dot_hom_neg_hom hN.unit, mul_zero]
    rw [← hF]
    exact tangent_vanish F hFpos hz' hc hzc' h0
  · let F : HVec d →ₗ[ℝ] ℝ := pvOmega a (hom (-z)) ∘ₗ (G : W d →ₗ[ℝ] W d) ∘ₗ
      tensR (Minv z G (hom (-z)))
    have hF : ∀ X, F X = pairVal a (hom (-z)) (G (tens X (Minv z G (hom (-z))))) := fun X => rfl
    have hFpos : ∀ X, Lor X → 0 ≤ F X := fun X hX => by
      rw [hF]
      exact gate_pairVal_nonneg hpos ha hX (lor_hom_of_unit hz') (lor_Minv hN hG (lor_hom_of_unit hz'))
    have h0 : F (hom (-z)) = 0 := by
      rw [hF, gt_corner_neg hN hG, hNz', pairVal_tens, dot_hom_hom_neg hN.unit, mul_zero]
    rw [← hF]
    exact tangent_vanish F hFpos hz' hc hzc' h0

/-- The dot product of the homogenized space as a bilinear map. -/
def dotB : HVec d →ₗ[ℝ] HVec d →ₗ[ℝ] ℝ :=
  LinearMap.mk₂ ℝ (fun u w => ∑ μ, u μ * w μ)
    (fun u u' w => by
      show ∑ μ, (u + u') μ * w μ = ∑ μ, u μ * w μ + ∑ μ, u' μ * w μ
      rw [← Finset.sum_add_distrib]
      exact Finset.sum_congr rfl fun μ _ => by rw [Pi.add_apply]; ring)
    (fun r u w => by
      show ∑ μ, (r • u) μ * w μ = r • ∑ μ, u μ * w μ
      simp only [Pi.smul_apply, smul_eq_mul, Finset.mul_sum]
      exact Finset.sum_congr rfl fun μ _ => by ring)
    (fun u w w' => by
      show ∑ μ, u μ * (w + w') μ = ∑ μ, u μ * w μ + ∑ μ, u μ * w' μ
      rw [← Finset.sum_add_distrib]
      exact Finset.sum_congr rfl fun μ _ => by rw [Pi.add_apply]; ring)
    (fun r u w => by
      show ∑ μ, u μ * (r • w) μ = r • ∑ μ, u μ * w μ
      simp only [Pi.smul_apply, smul_eq_mul, Finset.mul_sum]
      exact Finset.sum_congr rfl fun μ _ => by ring)

theorem dotB_apply (u w : HVec d) : dotB u w = ∑ μ, u μ * w μ := rfl

/-- A vector whose dot square is at most twice its head square is a cone vector. -/
theorem lor_of_dotB {X : HVec d} (h0 : 0 ≤ X 0) (h : dotB X X ≤ 2 * X 0 ^ 2) : Lor X := by
  refine ⟨h0, ?_⟩
  rw [dotB_apply, Fin.sum_univ_succ] at h
  have e : ∑ j : Fin d, X j.succ * X j.succ = ∑ j : Fin d, X j.succ ^ 2 :=
    Finset.sum_congr rfl fun j _ => (sq _).symm
  rw [e] at h
  nlinarith [h]

/-- **The block form.** The target bilinear form of the normalized gate on the tangent control
slice `c`, read against the control effect `a`. -/
noncomputable def Phi (z : Fin d → ℝ) (G : W d ≃ₗ[ℝ] W d) (a : HVec d) (c : Fin d → ℝ) :
    HVec d →ₗ[ℝ] HVec d →ₗ[ℝ] ℝ :=
  LinearMap.mk₂ ℝ (fun f t => pairVal a f (G (tens (lift c) (Minv z G t))))
    (fun f f' t => pairVal_add_right a f f' _)
    (fun r f t => by
      show pairVal a (r • f) (G (tens (lift c) (Minv z G t)))
        = r • pairVal a f (G (tens (lift c) (Minv z G t)))
      rw [pairVal_smul_right, smul_eq_mul])
    (fun f t t' => by
      show pairVal a f (G (tens (lift c) (Minv z G (t + t'))))
        = pairVal a f (G (tens (lift c) (Minv z G t))) + pairVal a f (G (tens (lift c) (Minv z G t')))
      rw [map_add, tens_add_right, map_add, pairVal_add_omega])
    (fun r f t => by
      show pairVal a f (G (tens (lift c) (Minv z G (r • t))))
        = r • pairVal a f (G (tens (lift c) (Minv z G t)))
      rw [map_smul, tens_smul_right, map_smul, pairVal_smul_omega, smul_eq_mul])

theorem Phi_apply (z : Fin d → ℝ) (G : W d ≃ₗ[ℝ] W d) (a : HVec d) (c : Fin d → ℝ)
    (f t : HVec d) : Phi z G a c f t = pairVal a f (G (tens (lift c) (Minv z G t))) := rfl

/-- The two sphere identities in block form: on a unit tangent target direction `u`, the diagonal
value equals the centre value and the two mixed values agree. -/
theorem Phi_sphere {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}
    (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) {c : Fin d → ℝ}
    (hc : ∑ j, c j ^ 2 ≤ 1) (hzc : ∑ j, z j * c j = 0) {a : HVec d} (ha : Lor a) {u : HVec d}
    (hu0 : u 0 = 0) (hu : ∑ μ, u μ ^ 2 = 1) :
    Phi z G a c u u = Phi z G a c (hom 0) (hom 0) ∧
    Phi z G a c (hom 0) u = Phi z G a c u (hom 0) := by
  have h1 : Phi z G a c (hom 0 - u) (hom 0 + u) = 0 := gt_sphere hN hG hc hzc ha hu0 hu
  have hu0' : (-u) 0 = 0 := by rw [Pi.neg_apply, hu0, neg_zero]
  have hu' : ∑ μ, (-u) μ ^ 2 = 1 := by simpa [neg_sq] using hu
  have h2 : Phi z G a c (hom 0 - -u) (hom 0 + -u) = 0 := gt_sphere hN hG hc hzc ha hu0' hu'
  rw [sub_neg_eq_add, ← sub_eq_add_neg] at h2
  simp only [map_add, map_sub, LinearMap.add_apply, LinearMap.sub_apply] at h1 h2
  constructor <;> linarith

/-- The centre value of the block form vanishes. -/
theorem Phi_center {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}
    (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) {c : Fin d → ℝ}
    (hc : ∑ j, c j ^ 2 ≤ 1) (hzc : ∑ j, z j * c j = 0) {a : HVec d} (ha : Lor a) :
    Phi z G a c (hom 0) (hom 0) = 0 := by
  have hz0 : lift z 0 = 0 := lift_zero z
  have hz1 : ∑ μ, lift z μ ^ 2 = 1 := by
    rw [Fin.sum_univ_succ, lift_zero, zero_pow two_ne_zero, zero_add]
    simpa using hN.unit
  obtain ⟨ha1, hb1⟩ := Phi_sphere hN hG hc hzc ha hz0 hz1
  have hc0 : Phi z G a c (hom z) (hom z) = 0 := (gt_sphere_corner hN hG hc hzc ha).1
  have hc1 : Phi z G a c (hom (-z)) (hom (-z)) = 0 := (gt_sphere_corner hN hG hc hzc ha).2
  rw [hom_eq_add_lift z] at hc0
  rw [hom_eq_add_lift (-z), lift_neg, ← sub_eq_add_neg] at hc1
  simp only [map_add, map_sub, LinearMap.add_apply, LinearMap.sub_apply] at hc0 hc1
  linarith

/-- The centre value vanishes for every control effect. -/
theorem Phi_center_all {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}
    (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) {c : Fin d → ℝ}
    (hc : ∑ j, c j ^ 2 ≤ 1) (hzc : ∑ j, z j * c j = 0) (a : HVec d) :
    Phi z G a c (hom 0) (hom 0) = 0 := by
  have h := linearMap_eq_zero_of_lor (pvLeft (hom 0) (G (tens (lift c) (Minv z G (hom 0)))))
    (fun a ha => Phi_center hN hG hc hzc ha)
  have := LinearMap.congr_fun h a
  rw [LinearMap.zero_apply] at this
  exact this

/-- The block form against the unit control effect vanishes identically. -/
theorem Phi_hom_zero_eq_zero {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}
    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G)
    {c : Fin d → ℝ} (hc : ∑ j, c j ^ 2 ≤ 1) (hzc : ∑ j, z j * c j = 0) (f t : HVec d) :
    Phi z G (hom 0) c f t = 0 := by
  have key : ∀ f t, Lor f → Lor t → Phi z G (hom 0) c f t = 0 := by
    intro f t hf ht
    obtain ⟨h1, h2⟩ := gt_tangent_corners hN hG hc hzc hf ht
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
theorem Phi_lift_z_eq_zero {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}
    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G)
    {c : Fin d → ℝ} (hc : ∑ j, c j ^ 2 ≤ 1) (hzc : ∑ j, z j * c j = 0) (f t : HVec d) :
    Phi z G (lift z) c f t = 0 := by
  have key : ∀ f t, Lor f → Lor t → Phi z G (lift z) c f t = 0 := by
    intro f t hf ht
    have h2 := (gt_tangent_corners hN hG hc hzc hf ht).2
    have h0 := Phi_hom_zero_eq_zero hN hG hc hzc f t
    rw [hom_eq_add_lift z, pairVal_add_left] at h2
    rw [Phi_apply] at h0
    rw [Phi_apply]
    linarith
  have hT : ∀ f, Lor f → Phi z G (lift z) c f = 0 := fun f hf =>
    linearMap_eq_zero_of_lor _ (fun t ht => key f t hf ht)
  have hF : Phi z G (lift z) c = 0 := linearMap_eq_zero_of_lor _ hT
  rw [hF, LinearMap.zero_apply, LinearMap.zero_apply]

/-- The tangent part of the `+1` eigenspace: the `+1` eigenvectors with vanishing head. -/
def tangentSpace (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) : Submodule ℝ (HVec d) :=
  plusSpace N ⊓ LinearMap.ker (LinearMap.proj (0 : Fin (d + 1)) : HVec d →ₗ[ℝ] ℝ)

theorem mem_tangentSpace {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {v : HVec d} :
    v ∈ tangentSpace N ↔ homMap N v = v ∧ v 0 = 0 := by
  rw [tangentSpace, Submodule.mem_inf, mem_plusSpace, LinearMap.mem_ker, LinearMap.proj_apply]

theorem hom_zero_ne_zero : hom (0 : Fin d → ℝ) ≠ 0 := fun h => by
  have := congrFun h 0
  rw [hom_zero, Pi.zero_apply] at this
  exact one_ne_zero this

/-- The tangent part of the `+1` eigenspace has dimension `tangentPlus N`. -/
theorem finrank_tangentSpace (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) :
    Module.finrank ℝ (tangentSpace N) = tangentPlus N := by
  have hsup : tangentSpace N ⊔ Submodule.span ℝ {hom (0 : Fin d → ℝ)} = plusSpace N := by
    apply le_antisymm
    · exact sup_le inf_le_left
        ((Submodule.span_singleton_le_iff_mem _ _).mpr (hom_zero_mem_plusSpace N))
    · intro v hv
      rw [Submodule.mem_sup]
      refine ⟨v - v 0 • hom 0, ?_, v 0 • hom 0, Submodule.mem_span_singleton.mpr ⟨v 0, rfl⟩,
        sub_add_cancel _ _⟩
      rw [mem_tangentSpace]
      refine ⟨?_, ?_⟩
      · rw [map_sub, map_smul, mem_plusSpace.mp hv, mem_plusSpace.mp (hom_zero_mem_plusSpace N)]
      · rw [Pi.sub_apply, Pi.smul_apply, hom_zero, smul_eq_mul, mul_one, sub_self]
  have hinf : tangentSpace N ⊓ Submodule.span ℝ {hom (0 : Fin d → ℝ)} = ⊥ := by
    rw [Submodule.eq_bot_iff]
    intro v hv
    obtain ⟨hv1, hv2⟩ := Submodule.mem_inf.mp hv
    obtain ⟨r, rfl⟩ := Submodule.mem_span_singleton.mp hv2
    have := (mem_tangentSpace.mp hv1).2
    rw [Pi.smul_apply, hom_zero, smul_eq_mul, mul_one] at this
    rw [this, zero_smul]
  have h := Submodule.finrank_sup_add_finrank_inf_eq (tangentSpace N)
    (Submodule.span ℝ {hom (0 : Fin d → ℝ)})
  rw [hsup, hinf, finrank_bot, finrank_span_singleton hom_zero_ne_zero] at h
  unfold tangentPlus
  omega

/-- Every subspace of the homogenized space has an orthonormal basis for the dot product, in sum
form: a family of its dimension, orthonormal, and separating the subspace. -/
theorem exists_orthonormal_basis (S : Submodule ℝ (HVec d)) :
    ∃ (q : ℕ) (v : Fin q → HVec d), q = Module.finrank ℝ S ∧ (∀ r, v r ∈ S) ∧
      (∀ r s, ∑ μ, v r μ * v s μ = if r = s then 1 else 0) ∧
      (∀ u ∈ S, (∀ r, ∑ μ, v r μ * u μ = 0) → u = 0) := by
  let e : EuclideanSpace ℝ (Fin (d + 1)) ≃ₗ[ℝ] HVec d :=
    WithLp.linearEquiv 2 ℝ (Fin (d + 1) → ℝ)
  let K : Submodule ℝ (EuclideanSpace ℝ (Fin (d + 1))) :=
    S.map (e.symm : HVec d →ₗ[ℝ] EuclideanSpace ℝ (Fin (d + 1)))
  have hK : Module.finrank ℝ K = Module.finrank ℝ S := LinearEquiv.finrank_map_eq e.symm S
  let b := stdOrthonormalBasis ℝ K
  have hinner : ∀ x y : EuclideanSpace ℝ (Fin (d + 1)), inner ℝ x y = ∑ μ, e x μ * e y μ := by
    intro x y
    rw [PiLp.inner_apply]
    exact Finset.sum_congr rfl fun μ _ =>
      (by rw [RCLike.inner_apply, conj_trivial, mul_comm] : inner ℝ (x μ) (y μ) = x μ * y μ)
  have hmem : ∀ x : K, e (x : EuclideanSpace ℝ (Fin (d + 1))) ∈ S := by
    intro x
    obtain ⟨y, hy, hyeq⟩ := Submodule.mem_map.mp x.2
    have : e (x : EuclideanSpace ℝ (Fin (d + 1))) = y := by
      rw [← hyeq]; exact e.apply_symm_apply y
    rw [this]; exact hy
  refine ⟨Module.finrank ℝ K, fun r => e (b r : EuclideanSpace ℝ (Fin (d + 1))), hK,
    fun r => hmem (b r), ?_, ?_⟩
  · intro r s
    have h := orthonormal_iff_ite.mp b.orthonormal r s
    rw [Submodule.coe_inner, hinner] at h
    exact h
  · intro u hu hperp
    have huK : e.symm u ∈ K := Submodule.mem_map_of_mem hu
    have hrepr := b.sum_repr' ⟨e.symm u, huK⟩
    have hzero : ∀ r, inner ℝ (b r) (⟨e.symm u, huK⟩ : K) = 0 := by
      intro r
      rw [Submodule.coe_inner, hinner]
      have := hperp r
      simpa [e.apply_symm_apply] using this
    rw [Finset.sum_eq_zero (fun r _ => by rw [hzero r, zero_smul])] at hrepr
    have h0 : e.symm u = 0 := by
      have := congrArg Subtype.val hrepr
      simpa using this.symm
    rw [← e.apply_symm_apply u, h0, map_zero]

/-- The control tangent directions: the coordinate vector `e_k` with its `z`-component removed. -/
def tperp (z : Fin d → ℝ) (k : Fin d) : Fin d → ℝ := fun j => (if k = j then 1 else 0) - z k * z j

theorem tperp_apply (z : Fin d → ℝ) (k j : Fin d) :
    tperp z k j = (if k = j then (1 : ℝ) else 0) - z k * z j := rfl

theorem sum_ite_mul (k : Fin d) (f : Fin d → ℝ) :
    ∑ j, (if k = j then (1 : ℝ) else 0) * f j = f k := by
  simp only [ite_mul, one_mul, zero_mul]
  rw [Finset.sum_ite_eq]
  simp

theorem tperp_sq {z : Fin d → ℝ} (hz : ∑ j, z j ^ 2 = 1) (k : Fin d) :
    ∑ j, tperp z k j ^ 2 = 1 - z k ^ 2 := by
  have e1 : ∀ j, tperp z k j ^ 2 = (if k = j then (1 : ℝ) else 0) * (if k = j then (1 : ℝ) else 0)
      - 2 * z k * ((if k = j then (1 : ℝ) else 0) * z j) + z k ^ 2 * z j ^ 2 := fun j => by
    rw [tperp_apply]; ring
  rw [Finset.sum_congr rfl fun j _ => e1 j, Finset.sum_add_distrib, Finset.sum_sub_distrib,
    ← Finset.mul_sum, ← Finset.mul_sum, sum_ite_mul, sum_ite_mul, hz, if_pos rfl]
  ring

theorem tperp_le_one {z : Fin d → ℝ} (hz : ∑ j, z j ^ 2 = 1) (k : Fin d) :
    ∑ j, tperp z k j ^ 2 ≤ 1 := by
  rw [tperp_sq hz k]; nlinarith [sq_nonneg (z k)]

theorem tperp_dot_z {z : Fin d → ℝ} (hz : ∑ j, z j ^ 2 = 1) (k : Fin d) :
    ∑ j, z j * tperp z k j = 0 := by
  have e1 : ∀ j, z j * tperp z k j = (if k = j then (1 : ℝ) else 0) * z j - z k * z j ^ 2 :=
    fun j => by rw [tperp_apply]; ring
  rw [Finset.sum_congr rfl fun j _ => e1 j, Finset.sum_sub_distrib, sum_ite_mul, ← Finset.mul_sum,
    hz]
  ring

theorem tperp_mem {z : Fin d → ℝ} (hz : ∑ j, z j ^ 2 = 1) (k : Fin d) : tperp z k ∈ eball d :=
  mem_eball.mpr (tperp_le_one hz k)

/-- The lifted tangent direction is the basis vector less its `z`-component. -/
theorem lift_tperp (z : Fin d → ℝ) (k : Fin d) :
    lift (tperp z k) = bvec k.succ - z k • lift z := by
  funext μ
  refine Fin.cases ?_ (fun j => ?_) μ
  · rw [lift_zero, Pi.sub_apply, bvec_apply, if_neg (Fin.succ_ne_zero k), Pi.smul_apply, lift_zero,
      smul_zero, sub_zero]
  · rw [lift_succ, tperp_apply, Pi.sub_apply, bvec_apply, Pi.smul_apply, lift_succ, smul_eq_mul]
    simp only [Fin.succ_inj]

/-- Some control tangent direction is nonzero when `2 ≤ d`. -/
theorem exists_tperp_ne_zero {z : Fin d → ℝ} (hz : ∑ j, z j ^ 2 = 1) (hd : 2 ≤ d) :
    ∃ l, tperp z l ≠ 0 := by
  by_contra hcon
  have hall : ∀ l, z l ^ 2 = 1 := by
    intro l
    have h0 : tperp z l = 0 := by
      by_contra h; exact hcon ⟨l, h⟩
    have := tperp_sq hz l
    rw [h0] at this
    simp at this
    linarith
  have hsum := hz
  rw [Finset.sum_congr rfl fun l _ => hall l] at hsum
  simp at hsum
  omega

theorem dot_hom_hom_zero (x : Fin d → ℝ) : ∑ μ, hom x μ * hom (0 : Fin d → ℝ) μ = 1 := by
  rw [Fin.sum_univ_succ, hom_zero, hom_zero, one_mul]
  simp [hom_succ]

theorem sum_bvec_mul (μ : Fin (d + 1)) (g : HVec d) : ∑ μ', bvec μ μ' * g μ' = g μ := by
  simp only [bvec_apply, ite_mul, one_mul, zero_mul]
  rw [Finset.sum_ite_eq]
  simp

/-- The pairing against a basis control effect reads a row. -/
theorem pairVal_bvec (μ : Fin (d + 1)) (b : HVec d) (ω : W d) :
    pairVal (bvec μ) b ω = ∑ ν, ω μ ν * b ν := by
  rw [pairVal_eq_sum_toOp, sum_bvec_mul, toOp_apply]

theorem sum_row_hom_zero (ω : W d) (μ : Fin (d + 1)) :
    ∑ ν, ω μ ν * hom (0 : Fin d → ℝ) ν = ω μ 0 := by
  rw [Fin.sum_univ_succ, hom_zero, mul_one]
  simp [hom_succ]

theorem tens_ne_zero {X Y : HVec d} (hX : X ≠ 0) (hY : Y ≠ 0) : tens X Y ≠ 0 := by
  obtain ⟨μ, hμ⟩ := Function.ne_iff.mp hX
  obtain ⟨ν, hν⟩ := Function.ne_iff.mp hY
  intro h
  have := congrFun (congrFun h μ) ν
  rw [tens_apply, Pi.zero_apply, Pi.zero_apply] at this
  exact mul_ne_zero (by simpa using hμ) (by simpa using hν) this

theorem pairVal_sub_left (a a' b : HVec d) (ω : W d) :
    pairVal (a - a') b ω = pairVal a b ω - pairVal a' b ω := by
  unfold pairVal
  rw [← Finset.sum_sub_distrib]
  refine Finset.sum_congr rfl fun μ _ => ?_
  rw [← Finset.sum_sub_distrib]
  refine Finset.sum_congr rfl fun ν _ => ?_
  simp only [Pi.sub_apply]; ring

/-- **The assembly (S2 and S4).** An orthonormal basis of the tangent `+1` eigenspace yields the
block data: the matrices are indexed by the control tangent directions `tperp`, `B` is
antisymmetric by the sphere identities, the Lorentz positivity is the gate's positivity on the
product of the control data with the target data `(1, b)`, `(1, ±eᵢ)`, and some entry of `A` is
nonzero because the gate is injective. -/
theorem blockData_of_orthonormal {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}
    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) (hd : 2 ≤ d)
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
    (Phi_sphere hN hG (tperp_le_one hz l) (tperp_dot_z hz l) (lor_hom (tperp_mem hz k)) (hv0 r)
      (hvu r)).2
  have hdiag : ∀ k l r, Phi z G (hom (tperp z k)) (tperp z l) (v r) (v r) = 0 := fun k l r => by
    rw [(Phi_sphere hN hG (tperp_le_one hz l) (tperp_dot_z hz l) (lor_hom (tperp_mem hz k)) (hv0 r)
      (hvu r)).1]
    exact Phi_center hN hG (tperp_le_one hz l) (tperp_dot_z hz l) (lor_hom (tperp_mem hz k))
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
        rw [(Phi_sphere hN hG (tperp_le_one hz l) (tperp_dot_z hz l) (lor_hom (tperp_mem hz k)) hw0
          hwu).1]
        exact Phi_center hN hG (tperp_le_one hz l) (tperp_dot_z hz l) (lor_hom (tperp_mem hz k))
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
      gate_pairVal_nonneg hpos hak (lor_hom (tperp_mem hz l)) hfL (lor_Minv hN hG htL)
    have hsplit : pairVal (hom (tperp z k)) f (G (tens (hom (tperp z l)) (Minv z G t)))
        = ∑ ν, t ν * f ν
          + pairVal (hom (tperp z k)) f (G (tens (lift (tperp z l)) (Minv z G t))) := by
      rw [hom_eq_add_lift (tperp z l), tens_add_left, map_add, pairVal_add_omega,
        gt_center hN hG htN, pairVal_tens, dot_hom_hom_zero, one_mul]
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
    have hΦ00 := Phi_center_all hN hG hcl hzl (hom (tperp z k))
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
      have := Mfwd_Minv hN hG (hom (0 : Fin d → ℝ))
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
            rw [hω, ← gate_actT hN hG, actT_tens, ← Minv_homMap hN hG, homMap_hom, map_zero]
          exact congrFun h1 μ
        · have h := Phi_center_all hN hG hcl hzl (bvec μ)
          rw [Phi_apply, ← hω, pairVal_bvec, sum_row_hom_zero] at h
          exact h
      · intro r
        have hk : ∀ k, pairVal (hom (tperp z k)) (v r) ω = 0 := by
          intro k
          have := hzero r k l
          rw [hsym k l r, Phi_apply, ← hω] at this
          exact this
        have h0 : pairVal (hom 0) (v r) ω = 0 := by
          have := Phi_hom_zero_eq_zero hN hG hcl hzl (v r) (hom 0)
          rwa [Phi_apply, ← hω] at this
        have hz' : pairVal (lift z) (v r) ω = 0 := by
          have := Phi_lift_z_eq_zero hN hG hcl hzl (v r) (hom 0)
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

/-- **The block reduction (S1, S2, S4).** Two identical copies of the Euclidean ball of
dimension at least two with a native gate carry the block data of the `+1` eigenspace's tangent
dimension. -/
theorem blockData_of_nativeGate {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}
    {G : W d ≃ₗ[ℝ] W d} (hd : 2 ≤ d) (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) :
    BlockData (tangentPlus N) := by
  obtain ⟨q, v, hq, hvS, hvv, hspan⟩ := exists_orthonormal_basis (tangentSpace N)
  rw [finrank_tangentSpace] at hq
  rw [← hq]
  exact blockData_of_orthonormal hN hG hd v hvS hvv hspan

/-- The unit clause of the NOT excludes `d = 0`. -/
theorem pos_of_isNot {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}
    (hN : IsNot (eball d) z N) : 0 < d := by
  rcases Nat.eq_zero_or_pos d with h | h
  · exfalso
    subst h
    have := hN.unit
    simp at this
  · exact h

/-- **The selector.** Two identical copies of the Euclidean ball with a native gate have
dimension one or three. -/
theorem dim_of_nativeGate {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}
    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) :
    d = 1 ∨ d = 3 := by
  have hpos := pos_of_isNot hN
  rcases Nat.lt_or_ge d 2 with h | h
  · left; omega
  · have hsum := finrank_plus_add_finrank_minus hN.invol
    have hbal := finrank_plus_eq_finrank_minus hN hG
    have hp := one_le_finrank_plusSpace N
    have hle := p_le_one_of_blockData (blockData_of_nativeGate h hN hG)
    exact NativeGateBall.dim_of_bounds (tangentPlus N) (Module.finrank ℝ (minusSpace N) - 1) d hle
      (by unfold tangentPlus; omega) (by unfold tangentPlus; omega)

theorem ne_five_of_nativeGate {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}
    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) : d ≠ 5 := by
  intro h
  rcases dim_of_nativeGate hN hG with hone | hthree <;> omega

theorem ne_seven_of_nativeGate {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}
    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) : d ≠ 7 := by
  intro h
  rcases dim_of_nativeGate hN hG with hone | hthree <;> omega

/-- **The selector under the entangling clause.** Two identical copies of the Euclidean ball with
an entangling native gate have dimension three. -/
theorem three_of_nativeGate {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}
    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G)
    (hE : Entangling (eball d) G) : d = 3 := by
  rcases dim_of_nativeGate hN hG with hone | hthree
  · exfalso
    subst hone
    exact not_entangling_one hN hG hE
  · exact hthree

/-! ### §P — controls: the classical gate of two intervals, and `eball 4` -/

/-- The classical gate of two intervals: the control index is added to the target index. -/
def cnot1Fun (ω : W 1) : W 1 := fun μ ν => ω (μ + ν) ν

theorem add_add_self_fin2 : ∀ μ ν : Fin 2, μ + ν + ν = μ := by decide

/-- The classical gate as a linear equivalence. -/
def cnot1 : W 1 ≃ₗ[ℝ] W 1 where
  toFun := cnot1Fun
  invFun := cnot1Fun
  map_add' ω₁ ω₂ := by funext μ ν; rfl
  map_smul' c ω := by funext μ ν; rfl
  left_inv ω := by
    funext μ ν
    show ω (μ + ν + ν) ν = ω μ ν
    rw [add_add_self_fin2]
  right_inv ω := by
    funext μ ν
    show ω (μ + ν + ν) ν = ω μ ν
    rw [add_add_self_fin2]

theorem cnot1_apply (ω : W 1) (μ ν : Fin 2) : cnot1 ω μ ν = ω (μ + ν) ν := rfl

/-- The corner axis of the interval. -/
def z1 : Fin 1 → ℝ := fun _ => 1

/-- The NOT of the interval: negation. -/
def neg1 : (Fin 1 → ℝ) →ₗ[ℝ] (Fin 1 → ℝ) := -LinearMap.id

theorem neg1_apply (x : Fin 1 → ℝ) (i : Fin 1) : neg1 x i = -x i := rfl

@[simp] theorem z1_zero : z1 0 = 1 := rfl
@[simp] theorem hom_one1 (x : Fin 1 → ℝ) : hom x 1 = x 0 := rfl
@[simp] theorem homMap_neg1_zero (v : HVec 1) : homMap neg1 v 0 = v 0 := rfl
@[simp] theorem homMap_neg1_one (v : HVec 1) : homMap neg1 v 1 = -v 1 := rfl

theorem isNot_neg1 : IsNot (eball 1) z1 neg1 where
  unit := by rw [Fin.sum_univ_one]; simp
  invol x := by funext i; rw [neg1_apply, neg1_apply, neg_neg]
  preserves x hx := by
    rw [mem_eball, Fin.sum_univ_one] at hx ⊢
    rw [neg1_apply, neg_sq]; exact hx
  flips := by funext i; rfl

theorem cnot1_frame (a b : Fin 2) :
    cnot1 (prodState (corner z1 a) (corner z1 b)) = prodState (corner z1 a) (corner z1 (a + b)) := by
  fin_cases a <;> fin_cases b <;> funext μ ν <;> fin_cases μ <;> fin_cases ν <;>
    simp +decide [cnot1_apply, prodState_apply, corner_zero, corner_one]

theorem cnot1_relT (ω : W 1) : actT neg1 (cnot1 (actT neg1 ω)) = cnot1 ω := by
  funext μ ν
  fin_cases μ <;> fin_cases ν <;> simp +decide [actT_apply, cnot1_apply]

theorem cnot1_relC (ω : W 1) : actC neg1 (cnot1 (actC neg1 ω)) = actT neg1 (cnot1 ω) := by
  funext μ ν
  fin_cases μ <;> fin_cases ν <;> simp +decide [actC_apply, actT_apply, cnot1_apply]

theorem lor_one {v : HVec 1} (hv : Lor v) : 0 ≤ v 0 ∧ v 1 ^ 2 ≤ v 0 ^ 2 := by
  obtain ⟨h0, h⟩ := hv
  rw [Fin.sum_univ_one] at h
  exact ⟨h0, h⟩

/-- The core inequality of the classical gate. -/
theorem cnot1_core (e0 a1 f0 b1 x y : ℝ) (he0 : 0 ≤ e0) (ha : a1 ^ 2 ≤ e0 ^ 2) (hf0 : 0 ≤ f0)
    (hb : b1 ^ 2 ≤ f0 ^ 2) (hx : x ^ 2 ≤ 1) (hy : y ^ 2 ≤ 1) :
    0 ≤ (e0 + a1 * x) * f0 + y * (e0 * x + a1) * b1 := by
  have hA : 0 ≤ e0 + a1 * x := by
    have h : (a1 * x) ^ 2 ≤ e0 ^ 2 := by
      rw [mul_pow]
      calc a1 ^ 2 * x ^ 2 ≤ e0 ^ 2 * 1 := mul_le_mul ha hx (sq_nonneg _) (sq_nonneg _)
        _ = e0 ^ 2 := mul_one _
    linarith [(abs_le_of_sq_le_sq' h he0).1]
  have hid : (e0 + a1 * x) ^ 2 - (e0 * x + a1) ^ 2 = (e0 ^ 2 - a1 ^ 2) * (1 - x ^ 2) := by ring
  have hB : (e0 * x + a1) ^ 2 ≤ (e0 + a1 * x) ^ 2 := by
    have := mul_nonneg (sub_nonneg.mpr ha) (sub_nonneg.mpr hx)
    linarith
  have h2 : (y * (e0 * x + a1) * b1) ^ 2 ≤ ((e0 + a1 * x) * f0) ^ 2 := by
    rw [mul_pow, mul_pow, mul_pow]
    calc y ^ 2 * (e0 * x + a1) ^ 2 * b1 ^ 2 ≤ 1 * (e0 + a1 * x) ^ 2 * f0 ^ 2 :=
          mul_le_mul (mul_le_mul hy hB (sq_nonneg _) zero_le_one) hb (sq_nonneg _)
            (by positivity)
      _ = (e0 + a1 * x) ^ 2 * f0 ^ 2 := by rw [one_mul]
  linarith [(abs_le_of_sq_le_sq' h2 (mul_nonneg hA hf0)).1]

theorem prodEffVal_cnot1_prodState (e f : (Fin 1 → ℝ) →ᵃ[ℝ] ℝ) (x y : Fin 1 → ℝ) :
    prodEffVal e f (cnot1 (prodState x y))
      = (ehom e 0 + ehom e 1 * x 0) * ehom f 0 + y 0 * (ehom e 0 * x 0 + ehom e 1) * ehom f 1 := by
  simp only [prodEffVal, pairVal, cnot1_apply, prodState_apply, sum_univ_two']
  simp +decide
  ring

theorem cnot1_prodState_mem_maxCone {x y : Fin 1 → ℝ} (hx : x ∈ eball 1) (hy : y ∈ eball 1) :
    cnot1 (prodState x y) ∈ maxCone (eball 1) := by
  show ∀ e f, IsEffectOn (eball 1) e → IsEffectOn (eball 1) f →
    0 ≤ prodEffVal e f (cnot1 (prodState x y))
  intro e f he hf
  obtain ⟨he0, ha⟩ := lor_one (lor_ehom he)
  obtain ⟨hf0, hb⟩ := lor_one (lor_ehom hf)
  rw [mem_eball, Fin.sum_univ_one] at hx hy
  rw [prodEffVal_cnot1_prodState]
  exact cnot1_core _ _ _ _ _ _ he0 ha hf0 hb hx hy

/-- The classical gate satisfies every native-gate hypothesis. -/
theorem nativeGate_cnot1 : NativeGate (eball 1) z1 neg1 cnot1 where
  frame := cnot1_frame
  posFwd x hx y hy := cnot1_prodState_mem_maxCone hx hy
  posInv x hx y hy := cnot1_prodState_mem_maxCone hx hy
  relT := cnot1_relT
  relC := cnot1_relC

/-- The classical gate is not entangling. -/
theorem not_entangling_cnot1 : ¬ Entangling (eball 1) cnot1 :=
  not_entangling_one isNot_neg1 nativeGate_cnot1

/-- The classical gate creates correlations from the mixed product input `(0, z1)`: the image is
not a product state. The entangling clause is not met, so correlation alone does not qualify. -/
theorem not_product_cnot1_mixed : ¬ IsProduct (eball 1) (cnot1 (prodState 0 z1)) := by
  rintro ⟨x', -, y', -, h⟩
  have h01 : y' 0 = 0 := by
    have := congrFun (congrFun h 0) 1
    simp +decide [cnot1_apply, prodState_apply] at this
    linarith
  have h11 : x' 0 * y' 0 = 1 := by
    have := congrFun (congrFun h 1) 1
    simp +decide [cnot1_apply, prodState_apply] at this
    linarith
  rw [h01, mul_zero] at h11
  exact zero_ne_one h11

/-- `eball 4` carries no native gate. -/
theorem no_gate_four : ¬ ∃ (z : Fin 4 → ℝ) (N : (Fin 4 → ℝ) →ₗ[ℝ] (Fin 4 → ℝ))
    (G : W 4 ≃ₗ[ℝ] W 4), IsNot (eball 4) z N ∧ NativeGate (eball 4) z N G := by
  rintro ⟨z, N, G, hN, hG⟩
  exact ne_four_of_nativeGate hN hG rfl

/-! ### The verdict -/

/-- The kernel layer's verdict: the parity exclusion, the selector, the selector under the
entangling clause, the `d = 3` witness, the classical controls and the `eball 4` exclusion. -/
theorem dim1_core :
    (∀ (d : ℕ) (z : Fin d → ℝ) (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (G : W d ≃ₗ[ℝ] W d),
      IsNot (eball d) z N → NativeGate (eball d) z N G → ¬ Even d) ∧
    (∀ (d : ℕ) (z : Fin d → ℝ) (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (G : W d ≃ₗ[ℝ] W d),
      IsNot (eball d) z N → NativeGate (eball d) z N G → d = 1 ∨ d = 3) ∧
    (∀ (d : ℕ) (z : Fin d → ℝ) (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (G : W d ≃ₗ[ℝ] W d),
      IsNot (eball d) z N → NativeGate (eball d) z N G → Entangling (eball d) G → d = 3) ∧
    (IsNot (eball 3) z3 nflip ∧ NativeGate (eball 3) z3 nflip cnot ∧ Entangling (eball 3) cnot) ∧
    (IsNot (eball 1) z1 neg1 ∧ NativeGate (eball 1) z1 neg1 cnot1 ∧
      ¬ Entangling (eball 1) cnot1 ∧ ¬ IsProduct (eball 1) (cnot1 (prodState 0 z1))) ∧
    ¬ ∃ (z : Fin 4 → ℝ) (N : (Fin 4 → ℝ) →ₗ[ℝ] (Fin 4 → ℝ)) (G : W 4 ≃ₗ[ℝ] W 4),
      IsNot (eball 4) z N ∧ NativeGate (eball 4) z N G :=
  ⟨fun _ _ _ _ hN hG => not_even_of_nativeGate hN hG,
    fun _ _ _ _ hN hG => dim_of_nativeGate hN hG,
    fun _ _ _ _ hN hG hE => three_of_nativeGate hN hG hE,
    ⟨isNot_nflip, nativeGate_cnot, entangling_cnot⟩,
    ⟨isNot_neg1, nativeGate_cnot1, not_entangling_cnot1, not_product_cnot1_mixed⟩,
    no_gate_four⟩

end CompositeDimension
end OIBridge

#print axioms OIBridge.CompositeDimension.isNot_nflip
#print axioms OIBridge.CompositeDimension.cnot_frame
#print axioms OIBridge.CompositeDimension.cnot_relT
#print axioms OIBridge.CompositeDimension.cnot_relC
#print axioms OIBridge.CompositeDimension.lor_ehom
#print axioms OIBridge.CompositeDimension.isEffectOn_affOf
#print axioms OIBridge.CompositeDimension.lor_toOp_of_maxCone
#print axioms OIBridge.CompositeDimension.cnot_core
#print axioms OIBridge.CompositeDimension.cnot_prodEffVal_nonneg
#print axioms OIBridge.CompositeDimension.nativeGate_cnot
#print axioms OIBridge.CompositeDimension.extreme_of_unit
#print axioms OIBridge.CompositeDimension.phiW_not_product
#print axioms OIBridge.CompositeDimension.phiW_mem_jointStates
#print axioms OIBridge.CompositeDimension.lor_ray
#print axioms OIBridge.CompositeDimension.phiW_eq_of_segment
#print axioms OIBridge.CompositeDimension.entangling_cnot
#print axioms OIBridge.CompositeDimension.eq_corner_of_extreme
#print axioms OIBridge.CompositeDimension.not_entangling_one
#print axioms OIBridge.CompositeDimension.isNot_neg1
#print axioms OIBridge.CompositeDimension.nativeGate_cnot1
#print axioms OIBridge.CompositeDimension.not_entangling_cnot1
#print axioms OIBridge.CompositeDimension.not_product_cnot1_mixed
#print axioms OIBridge.CompositeDimension.no_gate_four
#print axioms OIBridge.CompositeDimension.dim1_core

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
#print axioms OIBridge.CompositeDimension.ne_five_of_nativeGate
#print axioms OIBridge.CompositeDimension.ne_seven_of_nativeGate

#print axioms OIBridge.CompositeDimension.tens_mem_maxCone
#print axioms OIBridge.CompositeDimension.linearMap_eq_zero_of_nonneg_lor
#print axioms OIBridge.CompositeDimension.linearMap_eq_zero_of_lor
#print axioms OIBridge.CompositeDimension.lor_face
#print axioms OIBridge.CompositeDimension.corner_form
#print axioms OIBridge.CompositeDimension.gate_corner
#print axioms OIBridge.CompositeDimension.gate_corner_symm
#print axioms OIBridge.CompositeDimension.Mfwd_Minv
#print axioms OIBridge.CompositeDimension.Minv_Mfwd
#print axioms OIBridge.CompositeDimension.lor_Minv
#print axioms OIBridge.CompositeDimension.Mfwd_homMap
#print axioms OIBridge.CompositeDimension.Minv_homMap
#print axioms OIBridge.CompositeDimension.gate_corner_neg
#print axioms OIBridge.CompositeDimension.gt_corner
#print axioms OIBridge.CompositeDimension.gt_corner_neg
#print axioms OIBridge.CompositeDimension.gt_center
#print axioms OIBridge.CompositeDimension.eq_zero_of_quadratic_nonneg
#print axioms OIBridge.CompositeDimension.lor_curve
#print axioms OIBridge.CompositeDimension.tangent_vanish
#print axioms OIBridge.CompositeDimension.gt_tangent_corners
#print axioms OIBridge.CompositeDimension.gt_sphere
#print axioms OIBridge.CompositeDimension.gt_sphere_corner
#print axioms OIBridge.CompositeDimension.lor_of_dotB
#print axioms OIBridge.CompositeDimension.Phi_sphere
#print axioms OIBridge.CompositeDimension.Phi_center
#print axioms OIBridge.CompositeDimension.Phi_center_all
#print axioms OIBridge.CompositeDimension.Phi_hom_zero_eq_zero
#print axioms OIBridge.CompositeDimension.Phi_lift_z_eq_zero
#print axioms OIBridge.CompositeDimension.finrank_tangentSpace
#print axioms OIBridge.CompositeDimension.exists_orthonormal_basis
#print axioms OIBridge.CompositeDimension.tperp_sq
#print axioms OIBridge.CompositeDimension.tperp_dot_z
#print axioms OIBridge.CompositeDimension.lift_tperp
#print axioms OIBridge.CompositeDimension.exists_tperp_ne_zero
#print axioms OIBridge.CompositeDimension.blockData_of_orthonormal
#print axioms OIBridge.CompositeDimension.blockData_of_nativeGate
#print axioms OIBridge.CompositeDimension.pos_of_isNot
#print axioms OIBridge.CompositeDimension.dim_of_nativeGate
#print axioms OIBridge.CompositeDimension.three_of_nativeGate
