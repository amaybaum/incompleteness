/-
  OIBridge/K2Guard.lean — round K2-GUARD-1: two interface facts of the composite route at the
  elementary ball, each with its own verdict.

  (A) The candidate-cone family of two copies of `eball 3` is the family of sets `K` of joint
  vectors that contain every product state of the ball and lie inside DIM-1's maximal cone
  `maxCone (eball 3)` (`CandidateCone`). No member of that family is invariant under both DIM-1's
  gate `cnot` and the reflection `reflY = diag(1, −1, 1)` acting on the second copy alone
  (`no_candidateCone_cnot_reflY`). The proof is one exact chain: the product state
  `prodState xplus z3`, then `cnot`, then `actT reflY`, then `cnot`, lands on a joint vector on
  which the product of the sharp effects along `−e₁` and `−e₃` takes the value `−1/2`
  (`chain_eq`, `chain_value`), so it is outside `maxCone (eball 3)`. Controls: `cnot` satisfies
  DIM-1's native-gate hypotheses; `reflY` maps the ball onto itself and has determinant `−1`; the
  products together with their `cnot` images form a candidate cone invariant under `cnot`
  (`cnotOrbit`); the products alone form a candidate cone invariant under `actT reflY`
  (`productSet`); with the rotation `nflip` (determinant `1`) in place of `reflY` the same chain
  takes the value `0` on the same pair of effects. The obstruction comes from the joint
  invariance requirement and concerns only the named gate, the named reflection and this family.

  (B) DIM-1's selector consumes its entangling clause only to exclude `d = 1`. With `2 ≤ d` in
  place of the clause, `IsNot` and `NativeGate` give `d = 3` (`three_of_nativeGate_of_two_le`),
  and the same holds for the relative hypotheses of round K1-BRIDGE-1
  (`three_of_nativeGateOf_of_two_le`). The entangling clause implies `2 ≤ d` under DIM-1's
  hypotheses (`two_le_of_entangling`); no converse is stated. Control: the interval with its
  classical gate satisfies `IsNot` and `NativeGate` at `d = 1`, where `2 ≤ d` fails.

  Every hypothesis is a premise. Nothing here sources a cone, a local action, a dense or
  continuous family of reversible operations, the product form of the composite tests, or `2 ≤ d`.
  No limit closure, no complex structure and no matrix representation is used.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.K1Bridge

namespace OIBridge
namespace K2Guard

open Set KInfFoundations OrbitGeneration TransitiveBody CompositeDimension CompositeInterface
open EffectSpace K1Bridge

variable {d : ℕ}

/-! ### §A — the one-copy reflection and the candidate-cone family -/

/-- The reflection of one copy of `eball 3` inverting the second coordinate. -/
def reflY : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ) where
  toFun x := fun i => (![1, -1, 1] : Fin 3 → ℝ) i * x i
  map_add' x y := by funext i; simp only [Pi.add_apply, mul_add]
  map_smul' c x := by funext i; simp only [Pi.smul_apply, smul_eq_mul, RingHom.id_apply]; ring

theorem reflY_apply (x : Fin 3 → ℝ) (i : Fin 3) : reflY x i = (![1, -1, 1] : Fin 3 → ℝ) i * x i :=
  rfl

@[simp] theorem reflY_zero' (x : Fin 3 → ℝ) : reflY x 0 = x 0 := by show 1 * x 0 = x 0; ring
@[simp] theorem reflY_one (x : Fin 3 → ℝ) : reflY x 1 = -x 1 := by show -1 * x 1 = -x 1; ring
@[simp] theorem reflY_two (x : Fin 3 → ℝ) : reflY x 2 = x 2 := by show 1 * x 2 = x 2; ring

@[simp] theorem homMap_reflY_zero (v : HVec 3) : homMap reflY v 0 = v 0 := rfl
@[simp] theorem homMap_reflY_one (v : HVec 3) : homMap reflY v 1 = v 1 := by
  show 1 * v 1 = v 1; ring
@[simp] theorem homMap_reflY_two (v : HVec 3) : homMap reflY v 2 = -v 2 := by
  show -1 * v 2 = -v 2; ring
@[simp] theorem homMap_reflY_three (v : HVec 3) : homMap reflY v 3 = v 3 := by
  show 1 * v 3 = v 3; ring

/-- `reflY` maps the ball into itself. -/
theorem reflY_mem_eball {x : Fin 3 → ℝ} (hx : x ∈ eball 3) : reflY x ∈ eball 3 := by
  rw [mem_eball, Fin.sum_univ_three] at hx ⊢
  rw [reflY_zero', reflY_one, reflY_two, neg_sq]
  exact hx

/-- `reflY` is an involution. -/
theorem reflY_reflY (x : Fin 3 → ℝ) : reflY (reflY x) = x := by
  funext i
  fin_cases i <;> simp

/-- `reflY` is a reflection: its determinant is `−1`. -/
theorem det_reflY : LinearMap.det reflY = -1 := by
  have h : reflY = Matrix.toLin' (Matrix.diagonal (![1, -1, 1] : Fin 3 → ℝ)) := by
    refine LinearMap.ext fun x => funext fun i => ?_
    rw [Matrix.toLin'_apply, Matrix.mulVec_diagonal, reflY_apply]
  rw [h, LinearMap.det_toLin', Matrix.det_diagonal, Fin.prod_univ_three]
  first | (norm_num; done) | (simp; done) | (simp; norm_num; done)

/-- `nflip`, DIM-1's NOT, is a rotation: its determinant is `1`. -/
theorem det_nflip : LinearMap.det nflip = 1 := by
  have h : nflip = Matrix.toLin' (Matrix.diagonal (![1, -1, -1] : Fin 3 → ℝ)) := by
    refine LinearMap.ext fun x => funext fun i => ?_
    rw [Matrix.toLin'_apply, Matrix.mulVec_diagonal, nflip_apply]
  rw [h, LinearMap.det_toLin', Matrix.det_diagonal, Fin.prod_univ_three]
  first | (norm_num; done) | (simp; done) | (simp; norm_num; done)

/-- The candidate-cone family of two copies of `eball 3`: the sets of joint vectors containing
every product state of the ball and contained in DIM-1's maximal cone. -/
def CandidateCone (K : Set (W 3)) : Prop :=
  (∀ x ∈ eball 3, ∀ y ∈ eball 3, prodState x y ∈ K) ∧ K ⊆ maxCone (eball 3)

/-! ### §B — the chain -/

/-- The joint vector `actT reflY phiW`: the identity table. -/
def idW : W 3 := ![![1, 0, 0, 0], ![0, 1, 0, 0], ![0, 0, 1, 0], ![0, 0, 0, 1]]

/-- The end of the chain: `cnot idW`. -/
def chainW : W 3 := ![![1, 0, 0, 1], ![1, 0, 0, -1], ![0, 0, 0, 0], ![0, 0, 0, 0]]

theorem actT_reflY_phiW : actT reflY phiW = idW := by
  funext μ ν
  fin_cases μ <;> fin_cases ν <;> simp +decide [actT_apply, phiW, idW]

theorem cnot_idW : cnot idW = chainW := by
  funext μ ν
  fin_cases μ <;> fin_cases ν <;>
    simp +decide [cnot_apply, cnotFun_apply, sgn, pc, pt, idW, chainW]

/-- The chain from the product state `prodState xplus z3`. -/
theorem chain_eq : cnot (actT reflY (cnot (prodState xplus z3))) = chainW := by
  rw [cnot_prodState_xplus_z3, actT_reflY_phiW, cnot_idW]

theorem sharpVec_negX : sharpVec (![-1, 0, 0] : Fin 3 → ℝ) = ![1 / 2, -1 / 2, 0, 0] := by
  funext i
  fin_cases i <;> first | rfl | (simp [sharpVec]; done) | (simp [sharpVec]; norm_num; done) |
    (norm_num [sharpVec]; done)

theorem sharpVec_negZ : sharpVec (![0, 0, -1] : Fin 3 → ℝ) = ![1 / 2, 0, 0, -1 / 2] := by
  funext i
  fin_cases i <;> first | rfl | (simp [sharpVec]; done) | (simp [sharpVec]; norm_num; done) |
    (norm_num [sharpVec]; done)

theorem sharpEff_negX_isEffectOn : IsEffectOn (eball 3) (sharpEff ![-1, 0, 0]) :=
  sharpEff_isEffectOn (by simp [Fin.sum_univ_three])

theorem sharpEff_negZ_isEffectOn : IsEffectOn (eball 3) (sharpEff ![0, 0, -1]) :=
  sharpEff_isEffectOn (by simp [Fin.sum_univ_three])

/-- The product of the sharp effects along `−e₁` and `−e₃` on the end of the chain. -/
theorem chain_value :
    prodEffVal (sharpEff ![-1, 0, 0]) (sharpEff ![0, 0, -1]) chainW = -1 / 2 := by
  simp only [prodEffVal, sharpEff, ehom_affOf, sharpVec_negX, sharpVec_negZ]
  first | (simp [pairVal, sum_univ_four', chainW]; done) |
    (simp [pairVal, sum_univ_four', chainW]; norm_num; done) |
    (norm_num [pairVal, sum_univ_four', chainW]; done)

/-! ### §C — the orientation obstruction -/

/-- **No candidate cone is invariant under `cnot` and the one-copy reflection.** -/
theorem no_candidateCone_cnot_reflY {K : Set (W 3)} (hK : CandidateCone K)
    (hC : ∀ ω ∈ K, cnot ω ∈ K) (hR : ∀ ω ∈ K, actT reflY ω ∈ K) : False := by
  have h1 : prodState xplus z3 ∈ K := hK.1 xplus xplus_mem z3 z3_mem
  have h2 : cnot (actT reflY (cnot (prodState xplus z3))) ∈ K := hC _ (hR _ (hC _ h1))
  have hmem : chainW ∈ maxCone (eball 3) := by rw [← chain_eq]; exact hK.2 h2
  have hv : 0 ≤ prodEffVal (sharpEff ![-1, 0, 0]) (sharpEff ![0, 0, -1]) chainW :=
    hmem _ _ sharpEff_negX_isEffectOn sharpEff_negZ_isEffectOn
  rw [chain_value] at hv
  norm_num at hv

/-! ### §D — controls for the obstruction -/

/-- The product of two effects on a product state. -/
theorem prodEffVal_prodState (e f : (Fin d → ℝ) →ᵃ[ℝ] ℝ) (x y : Fin d → ℝ) :
    prodEffVal e f (prodState x y) = e x * f y := by
  rw [ehom_dot e x, ehom_dot f y]
  show pairVal (ehom e) (ehom f) (tens (hom x) (hom y)) = _
  rw [pairVal_tens]
  congr 1
  exact Finset.sum_congr rfl fun ν _ => mul_comm _ _

/-- Product states of `Ω` lie in the maximal cone of `Ω`. -/
theorem prodState_mem_maxCone {Ω : Set (Fin d → ℝ)} {x y : Fin d → ℝ} (hx : x ∈ Ω) (hy : y ∈ Ω) :
    prodState x y ∈ maxCone Ω := by
  show ∀ e f, IsEffectOn Ω e → IsEffectOn Ω f → 0 ≤ prodEffVal e f (prodState x y)
  intro e f he hf
  rw [prodEffVal_prodState]
  exact mul_nonneg (he x hx).1 (hf y hy).1

/-- A local linear map of the second copy carries a product state to a product state. -/
theorem actT_prodState (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (x y : Fin d → ℝ) :
    actT N (prodState x y) = prodState x (N y) := by
  show actT N (tens (hom x) (hom y)) = tens (hom x) (hom (N y))
  rw [actT_tens, homMap_hom]

/-- The product states of the ball. -/
def productSet : Set (W 3) := {ω | ∃ x ∈ eball 3, ∃ y ∈ eball 3, ω = prodState x y}

/-- The product states of the ball together with their `cnot` images. -/
def cnotOrbit : Set (W 3) :=
  {ω | ∃ x ∈ eball 3, ∃ y ∈ eball 3, ω = prodState x y ∨ ω = cnot (prodState x y)}

theorem candidateCone_productSet : CandidateCone productSet := by
  refine ⟨fun x hx y hy => ⟨x, hx, y, hy, rfl⟩, ?_⟩
  rintro ω ⟨x, hx, y, hy, rfl⟩
  exact prodState_mem_maxCone hx hy

theorem reflY_mem_productSet {ω : W 3} (hω : ω ∈ productSet) : actT reflY ω ∈ productSet := by
  obtain ⟨x, hx, y, hy, rfl⟩ := hω
  exact ⟨x, hx, reflY y, reflY_mem_eball hy, actT_prodState reflY x y⟩

theorem candidateCone_cnotOrbit : CandidateCone cnotOrbit := by
  refine ⟨fun x hx y hy => ⟨x, hx, y, hy, Or.inl rfl⟩, ?_⟩
  rintro ω ⟨x, hx, y, hy, rfl | rfl⟩
  · exact prodState_mem_maxCone hx hy
  · exact cnot_prodState_mem_maxCone hx hy

theorem cnot_mem_cnotOrbit {ω : W 3} (hω : ω ∈ cnotOrbit) : cnot ω ∈ cnotOrbit := by
  obtain ⟨x, hx, y, hy, rfl | rfl⟩ := hω
  · exact ⟨x, hx, y, hy, Or.inr rfl⟩
  · refine ⟨x, hx, y, hy, Or.inl ?_⟩
    rw [cnot_apply, cnot_apply, cnotFun_cnotFun]

/-- The joint vector `actT nflip phiW`. -/
def rotW : W 3 := ![![1, 0, 0, 0], ![0, 1, 0, 0], ![0, 0, 1, 0], ![0, 0, 0, -1]]

/-- The end of the chain with the rotation `nflip`: `cnot rotW`. -/
def rotChainW : W 3 := ![![1, 0, 0, -1], ![1, 0, 0, -1], ![0, 0, 0, 0], ![0, 0, 0, 0]]

theorem actT_nflip_phiW : actT nflip phiW = rotW := by
  funext μ ν
  fin_cases μ <;> fin_cases ν <;> simp +decide [actT_apply, phiW, rotW]

theorem cnot_rotW : cnot rotW = rotChainW := by
  funext μ ν
  fin_cases μ <;> fin_cases ν <;>
    simp +decide [cnot_apply, cnotFun_apply, sgn, pc, pt, rotW, rotChainW]

/-- With the rotation `nflip` in place of `reflY`, the chain takes the value `0` on the same pair
of effects. -/
theorem rotation_chain_value :
    prodEffVal (sharpEff ![-1, 0, 0]) (sharpEff ![0, 0, -1])
      (cnot (actT nflip (cnot (prodState xplus z3)))) = 0 := by
  rw [cnot_prodState_xplus_z3, actT_nflip_phiW, cnot_rotW]
  simp only [prodEffVal, sharpEff, ehom_affOf, sharpVec_negX, sharpVec_negZ]
  first | (simp [pairVal, sum_univ_four', rotChainW]; done) |
    (simp [pairVal, sum_univ_four', rotChainW]; norm_num; done) |
    (norm_num [pairVal, sum_univ_four', rotChainW]; done)

/-! ### §E — the dimension selector with `2 ≤ d` -/

/-- **`2 ≤ d` in place of the entangling clause.** DIM-1's `dim_of_nativeGate` and `2 ≤ d`. -/
theorem three_of_nativeGate_of_two_le {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}
    {G : W d ≃ₗ[ℝ] W d} (hd : 2 ≤ d) (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) :
    d = 3 := by
  rcases dim_of_nativeGate hN hG with h | h <;> omega

/-- Under DIM-1's hypotheses the entangling clause gives `2 ≤ d`. -/
theorem two_le_of_entangling {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}
    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G)
    (hE : Entangling (eball d) G) : 2 ≤ d := by
  have h := three_of_nativeGate hN hG hE
  omega

section Relative

variable {G : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ))} {r : (Fin d → ℝ) →ᵃ[ℝ] ℝ}
  {avail : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ)}

/-- **`2 ≤ d` in place of the entangling clause, relative to the available family.**
K1-BRIDGE-1's `dim_of_nativeGateOf` and `2 ≤ d`. -/
theorem three_of_nativeGateOf_of_two_le (hd : 2 ≤ d) (hE : EffectsOn (eball d) avail)
    (hG : PreservesBody (eball d) G) (hP1 : SharpSeed (eball d) r)
    (hK : BoundaryTransitive (eball d) G) (hV4 : SeedOrbitAvailable G r avail)
    {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {T : W d ≃ₗ[ℝ] W d}
    (hN : IsNot (eball d) z N) (hT : NativeGateOf (eball d) avail z N T) : d = 3 := by
  rcases dim_of_nativeGateOf (by omega) hE hG hP1 hK hV4 hN hT with h | h <;> omega

end Relative

/-! ### §F — controls for the selector -/

/-- The interval with its classical gate satisfies DIM-1's NOT and native-gate hypotheses at
`d = 1`, where `2 ≤ d` fails. -/
theorem two_le_load_bearing :
    IsNot (eball 1) z1 neg1 ∧ NativeGate (eball 1) z1 neg1 cnot1 ∧ ¬ (2 ≤ 1) :=
  ⟨isNot_neg1, nativeGate_cnot1, by norm_num⟩

/-- At `d = 3` the hypotheses of `three_of_nativeGate_of_two_le` are satisfied by DIM-1's gate. -/
theorem two_le_satisfiable : 2 ≤ 3 ∧ IsNot (eball 3) z3 nflip ∧ NativeGate (eball 3) z3 nflip cnot :=
  ⟨by norm_num, isNot_nflip, nativeGate_cnot⟩

/-! ### The verdicts -/

/-- Target A with its controls. -/
theorem k2guard_orientation :
    (∀ K : Set (W 3), CandidateCone K → (∀ ω ∈ K, cnot ω ∈ K) →
        (∀ ω ∈ K, actT reflY ω ∈ K) → False) ∧
    NativeGate (eball 3) z3 nflip cnot ∧
    (∀ x ∈ eball 3, reflY x ∈ eball 3) ∧ LinearMap.det reflY = -1 ∧ LinearMap.det nflip = 1 ∧
    (CandidateCone cnotOrbit ∧ ∀ ω ∈ cnotOrbit, cnot ω ∈ cnotOrbit) ∧
    (CandidateCone productSet ∧ ∀ ω ∈ productSet, actT reflY ω ∈ productSet) ∧
    prodEffVal (sharpEff ![-1, 0, 0]) (sharpEff ![0, 0, -1])
      (cnot (actT reflY (cnot (prodState xplus z3)))) = -1 / 2 ∧
    prodEffVal (sharpEff ![-1, 0, 0]) (sharpEff ![0, 0, -1])
      (cnot (actT nflip (cnot (prodState xplus z3)))) = 0 :=
  ⟨fun _ hK hC hR => no_candidateCone_cnot_reflY hK hC hR,
    nativeGate_cnot,
    fun _ hx => reflY_mem_eball hx, det_reflY, det_nflip,
    ⟨candidateCone_cnotOrbit, fun _ hω => cnot_mem_cnotOrbit hω⟩,
    ⟨candidateCone_productSet, fun _ hω => reflY_mem_productSet hω⟩,
    by rw [chain_eq, chain_value],
    rotation_chain_value⟩

/-- Target B with its controls. -/
theorem k2guard_entangling :
    (∀ (d : ℕ) (z : Fin d → ℝ) (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (G : W d ≃ₗ[ℝ] W d),
        2 ≤ d → IsNot (eball d) z N → NativeGate (eball d) z N G → d = 3) ∧
    (∀ (d : ℕ) (G : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ))) (r : (Fin d → ℝ) →ᵃ[ℝ] ℝ)
        (avail : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ)) (z : Fin d → ℝ) (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ))
        (T : W d ≃ₗ[ℝ] W d), 2 ≤ d → EffectsOn (eball d) avail → PreservesBody (eball d) G →
        SharpSeed (eball d) r → BoundaryTransitive (eball d) G → SeedOrbitAvailable G r avail →
        IsNot (eball d) z N → NativeGateOf (eball d) avail z N T → d = 3) ∧
    (∀ (d : ℕ) (z : Fin d → ℝ) (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (G : W d ≃ₗ[ℝ] W d),
        IsNot (eball d) z N → NativeGate (eball d) z N G → Entangling (eball d) G → 2 ≤ d) ∧
    (IsNot (eball 1) z1 neg1 ∧ NativeGate (eball 1) z1 neg1 cnot1 ∧ ¬ (2 ≤ 1)) ∧
    (2 ≤ 3 ∧ IsNot (eball 3) z3 nflip ∧ NativeGate (eball 3) z3 nflip cnot) :=
  ⟨fun _ _ _ _ hd hN hG => three_of_nativeGate_of_two_le hd hN hG,
    fun _ _ _ _ _ _ _ hd hE hG hP1 hK hV4 hN hT =>
      three_of_nativeGateOf_of_two_le hd hE hG hP1 hK hV4 hN hT,
    fun _ _ _ _ hN hG hE => two_le_of_entangling hN hG hE,
    two_le_load_bearing,
    two_le_satisfiable⟩

end K2Guard
end OIBridge

#print axioms OIBridge.K2Guard.reflY_mem_eball
#print axioms OIBridge.K2Guard.det_reflY
#print axioms OIBridge.K2Guard.det_nflip
#print axioms OIBridge.K2Guard.chain_eq
#print axioms OIBridge.K2Guard.chain_value
#print axioms OIBridge.K2Guard.no_candidateCone_cnot_reflY
#print axioms OIBridge.K2Guard.prodState_mem_maxCone
#print axioms OIBridge.K2Guard.candidateCone_productSet
#print axioms OIBridge.K2Guard.reflY_mem_productSet
#print axioms OIBridge.K2Guard.candidateCone_cnotOrbit
#print axioms OIBridge.K2Guard.cnot_mem_cnotOrbit
#print axioms OIBridge.K2Guard.rotation_chain_value
#print axioms OIBridge.K2Guard.three_of_nativeGate_of_two_le
#print axioms OIBridge.K2Guard.two_le_of_entangling
#print axioms OIBridge.K2Guard.three_of_nativeGateOf_of_two_le
#print axioms OIBridge.K2Guard.two_le_load_bearing
#print axioms OIBridge.K2Guard.two_le_satisfiable
#print axioms OIBridge.K2Guard.k2guard_orientation
#print axioms OIBridge.K2Guard.k2guard_entangling
