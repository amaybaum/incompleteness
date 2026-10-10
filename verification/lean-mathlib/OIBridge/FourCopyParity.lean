/-
  OIBridge/FourCopyParity.lean — design preflight (EQ4-F), not adopted: the completed cheap layer
  of the four-copy package. Every proof in this file is complete.

  * Gate-supplied effects (`gate_sharp_mem_dualW`): for an aligned gate preserving a candidate
    cone, the gate image of a product of sharp effects is an effect table of that cone.
  * Dual action of an inverse gate (`dualW_of_inv`): where inverse-gate preservation enters.
  * The two inclusions in inequality form (`incl_I`, `incl_II`), and their aligned forms with the
    `cnot` Bell table as link (`incl_I_aligned`, `incl_II_aligned`); no closedness is used.
  * Lemma P (`kt4_parity_aligned`): if four candidate cones are each preserved by the aligned gate
    of their twist bit and satisfy the four-copy interface, the twist bits have even parity. The
    proof uses one instance of `famI` with explicit witnesses whose value is `-1/8` at every odd
    pattern. It uses no closedness, no convexity and no complex structure.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.FourCopyDefs

namespace OIBridge
namespace FourCopy

open Set CompositeDimension K2Guard EffectSpace KInfFoundations TransitiveBody

noncomputable section

variable {K01 K23 K02 K13 : Set (W 3)}

/-! ### §A — table calculus -/

theorem ipW_comm (E X : W 3) : ipW E X = ipW X E := by
  unfold ipW
  exact Finset.sum_congr rfl fun μ _ => Finset.sum_congr rfl fun ν _ => mul_comm _ _

/-- Product-effect tables pair as `pairVal`. -/
theorem ipW_tens (a b : HVec 3) (ω : W 3) : ipW (tens a b) ω = pairVal a b ω := by
  simp only [ipW, tens_apply, pairVal]
  exact Finset.sum_congr rfl fun μ _ => Finset.sum_congr rfl fun ν _ => by ring

theorem ipW_transposeW (E X : W 3) : ipW (transposeW E) X = ipW E (transposeW X) := by
  simp only [ipW, transposeW]
  exact Finset.sum_congr rfl fun μ _ => Finset.sum_congr rfl fun ν _ => by ring

theorem sgnY_mul_self (i : Fin 4) : sgnY i * sgnY i = 1 := by
  fin_cases i <;> norm_num [sgnY]

theorem transposeW_transposeW (ω : W 3) : transposeW (transposeW ω) = ω := by
  funext μ ν
  have hμ := sgnY_mul_self μ
  have hν := sgnY_mul_self ν
  simp only [transposeW]
  linear_combination (sgnY ν * sgnY ν * ω μ ν) * hμ + ω μ ν * hν

/-! ### §B — diagonal tables -/

/-- The diagonal table with entries `p, q, r, s`. -/
def dg (p q r s : ℝ) : W 3 := ![![p, 0, 0, 0], ![0, q, 0, 0], ![0, 0, r, 0], ![0, 0, 0, s]]

/-- The sign of a twist bit: `-1` for `false`, `1` for `true`. -/
def sgnB : Bool → ℝ
  | false => -1
  | true => 1

theorem phiW_eq_dg : phiW = dg 1 1 (-1) 1 := by
  funext μ ν
  fin_cases μ <;> fin_cases ν <;> simp +decide [phiW, dg]

theorem idW_eq_dg : idW = dg 1 1 1 1 := rfl

theorem smul_dg (k p q r s : ℝ) : k • dg p q r s = dg (k * p) (k * q) (k * r) (k * s) := by
  funext μ ν
  fin_cases μ <;> fin_cases ν <;> simp [dg]

set_option maxHeartbeats 1000000 in
/-- The contraction of four diagonal tables. -/
theorem ipW_dg (a0 a1 a2 a3 b0 b1 b2 b3 c0 c1 c2 c3 f0 f1 f2 f3 : ℝ) :
    ipW (dg a0 a1 a2 a3)
        (tabMul (tabMul (dg b0 b1 b2 b3) (dg c0 c1 c2 c3)) (tabT (dg f0 f1 f2 f3))) =
      a0 * b0 * c0 * f0 + a1 * b1 * c1 * f1 + a2 * b2 * c2 * f2 + a3 * b3 * c3 * f3 := by
  simp [ipW, tabMul, tabT, dg, sum_univ_four'] <;> ring

theorem ipW_dg_smul (a0 a1 a2 a3 b0 b1 b2 b3 c0 c1 c2 c3 f0 f1 f2 f3 k k' : ℝ) :
    ipW (dg a0 a1 a2 a3)
        (tabMul (tabMul (k • dg b0 b1 b2 b3) (dg c0 c1 c2 c3)) (tabT (k' • dg f0 f1 f2 f3))) =
      k * k' * (a0 * b0 * c0 * f0 + a1 * b1 * c1 * f1 + a2 * b2 * c2 * f2 + a3 * b3 * c3 * f3) := by
  rw [smul_dg, smul_dg, ipW_dg]
  ring

theorem actT_reflY_dg (p q r s : ℝ) : actT reflY (dg p q r s) = dg p q (-r) s := by
  funext μ ν
  fin_cases μ <;> fin_cases ν <;> simp +decide [actT_apply, dg]

set_option maxHeartbeats 1000000 in
theorem phiW_tabMul (f : W 3) : tabMul (tabMul phiW f) (tabT phiW) = transposeW f := by
  rw [phiW_eq_dg]
  funext μ ν
  fin_cases μ <;> fin_cases ν <;> simp [tabMul, tabT, dg, transposeW, sgnY, sum_univ_four']

/-! ### §C — the aligned gates are self-adjoint for the pairing -/

theorem ipW_cnot (E X : W 3) : ipW (cnot E) X = ipW E (cnot X) := by
  simp only [ipW, cnot_apply, cnotFun_apply, sum_univ_four']
  simp +decide [sgn, pc, pt] <;> ring

theorem ipW_actT_reflY (E X : W 3) : ipW (actT reflY E) X = ipW E (actT reflY X) := by
  simp only [ipW, actT_apply, sum_univ_four', homMap_reflY_zero, homMap_reflY_one,
    homMap_reflY_two, homMap_reflY_three]
  ring

theorem ipW_gateOf (τ : Bool) (E X : W 3) : ipW (gateOf τ E) X = ipW E (gateOf τ X) := by
  cases τ
  · exact ipW_cnot E X
  · rw [gateOf_true, cnotTw_apply, cnotTw_apply, ipW_actT_reflY, ipW_cnot, ipW_actT_reflY]

/-! ### §D — gate-supplied effects and the dual action of an inverse gate -/

theorem tens_sharpVec (b c : Fin 3 → ℝ) :
    tens (sharpVec b) (sharpVec c) = (1 / 4 : ℝ) • prodState b c := by
  funext μ ν
  fin_cases μ <;> fin_cases ν <;> simp [tens_apply, sharpVec, prodState_apply] <;> ring

theorem gateOf_sharp (τ : Bool) (b c : Fin 3 → ℝ) :
    gateOf τ (tens (sharpVec b) (sharpVec c)) = (1 / 4 : ℝ) • gateOf τ (prodState b c) := by
  rw [tens_sharpVec]
  exact (gateOf τ).map_smul _ _

/-- **Gate-supplied effects (aligned).** The image under an aligned gate of a product of sharp
effects is an effect table of every candidate cone the gate preserves. -/
theorem gate_sharp_mem_dualW {τ : Bool} {K : Set (W 3)} (hK : CandidateCone K)
    (hG : ∀ ω ∈ K, gateOf τ ω ∈ K) {b c : Fin 3 → ℝ} (hb : ∑ j, b j ^ 2 = 1)
    (hc : ∑ j, c j ^ 2 = 1) : gateOf τ (tens (sharpVec b) (sharpVec c)) ∈ dualW K := by
  refine mem_dualW.2 fun X hX => ?_
  rw [ipW_gateOf, ipW_tens, ← prodEffVal_sharp]
  exact hK.2 (hG X hX) _ _ (sharpEff_isEffectOn hb) (sharpEff_isEffectOn hc)

/-- **Dual action of an inverse gate.** For a gate orthogonal for the pairing whose inverse
preserves `K`, the gate image of an effect table of `K` is an effect table of `K`. -/
theorem dualW_of_inv {N : W 3 ≃ₗ[ℝ] W 3} (hNo : ∀ E X, ipW (N E) (N X) = ipW E X)
    {K : Set (W 3)} (hinv : ∀ ω ∈ K, N.symm ω ∈ K) {E : W 3} (hE : E ∈ dualW K) :
    N E ∈ dualW K := by
  refine mem_dualW.2 fun X hX => ?_
  have h := mem_dualW.1 hE (N.symm X) (hinv X hX)
  rwa [← hNo E (N.symm X), N.apply_symm_apply] at h

/-! ### §E — the two inclusions (no closedness) -/

/-- **Inclusion (I), inequality form.** Link states in `K02`, `K13` send `K23*` into `K01**`. -/
theorem incl_I (h : FourCopyCoherent K01 K23 K02 K13) {β02 β13 : W 3} (h02 : β02 ∈ K02)
    (h13 : β13 ∈ K13) {f : W 3} (hf : f ∈ dualW K23) :
    tabMul (tabMul β02 f) (tabT β13) ∈ dualW (dualW K01) := by
  refine mem_dualW.2 fun e he => ?_
  rw [ipW_comm]
  exact h.famII β02 h02 β13 h13 e he f hf

/-- **Inclusion (II).** Link effects in `K02*`, `K13*` bound `K01` by the dual of the linked image
of `K23`. -/
theorem incl_II (h : FourCopyCoherent K01 K23 K02 K13) {ε02 ε13 : W 3} (h02 : ε02 ∈ dualW K02)
    (h13 : ε13 ∈ dualW K13) {X : W 3} (hX : X ∈ K01) :
    X ∈ dualW ((fun Y => tabMul (tabMul ε02 Y) (tabT ε13)) '' K23) := by
  refine mem_dualW.2 ?_
  rintro _ ⟨Y, hY, rfl⟩
  exact h.famI X hX Y hY ε02 h02 ε13 h13

/-- Aligned (I) with the `cnot` Bell table as link state: `T(K23*) ⊆ K01**`. -/
theorem incl_I_aligned (h : FourCopyCoherent K01 K23 K02 K13) (h02 : phiW ∈ K02)
    (h13 : phiW ∈ K13) : transposeW '' dualW K23 ⊆ dualW (dualW K01) := by
  rintro _ ⟨f, hf, rfl⟩
  rw [← phiW_tabMul]
  exact incl_I h h02 h13 hf

/-- Aligned (II) with the `cnot` Bell table as link effect: `K01 ⊆ T(K23*)`. -/
theorem incl_II_aligned (h : FourCopyCoherent K01 K23 K02 K13) (h02 : phiW ∈ dualW K02)
    (h13 : phiW ∈ dualW K13) : K01 ⊆ transposeW '' dualW K23 := by
  intro X hX
  refine ⟨transposeW X, mem_dualW.2 fun Y hY => ?_, transposeW_transposeW X⟩
  have h1 := mem_dualW.1 (incl_II h h02 h13 hX) (tabMul (tabMul phiW Y) (tabT phiW))
    ⟨Y, hY, rfl⟩
  rwa [phiW_tabMul, ← ipW_transposeW] at h1

/-! ### §F — Lemma P: aligned parity -/

theorem reflY_z3 : reflY z3 = z3 := by
  funext i
  fin_cases i <;> simp [z3]

theorem reflY_neg_z3 : reflY (-z3) = -z3 := by
  rw [map_neg, reflY_z3]

/-- The twin Bell table. -/
theorem cnotTw_prodState_xplus_z3 : cnotTw (prodState xplus z3) = idW := by
  rw [cnotTw_apply, actT_prodState, reflY_z3, cnot_prodState_xplus_z3, actT_reflY_phiW]

theorem cnot_prodState_neg : cnot (prodState (-xplus) (-z3)) = dg 1 (-1) (-1) (-1) := by
  funext μ ν
  fin_cases μ <;> fin_cases ν <;>
    simp +decide [cnot_apply, cnotFun_apply, sgn, pc, pt, prodState_apply, dg]

theorem cnotTw_prodState_neg : cnotTw (prodState (-xplus) (-z3)) = dg 1 (-1) 1 (-1) := by
  rw [cnotTw_apply, actT_prodState, reflY_neg_z3, cnot_prodState_neg, actT_reflY_dg, neg_neg]

theorem gateOf_prodState_xplus_z3 (τ : Bool) :
    gateOf τ (prodState xplus z3) = dg 1 1 (sgnB τ) 1 := by
  cases τ
  · show cnot (prodState xplus z3) = dg 1 1 (-1) 1
    rw [cnot_prodState_xplus_z3, phiW_eq_dg]
  · show cnotTw (prodState xplus z3) = dg 1 1 1 1
    rw [cnotTw_prodState_xplus_z3, idW_eq_dg]

theorem gateOf_prodState_neg (τ : Bool) :
    gateOf τ (prodState (-xplus) (-z3)) = dg 1 (-1) (sgnB τ) (-1) := by
  cases τ
  · show cnot (prodState (-xplus) (-z3)) = dg 1 (-1) (-1) (-1)
    exact cnot_prodState_neg
  · show cnotTw (prodState (-xplus) (-z3)) = dg 1 (-1) 1 (-1)
    exact cnotTw_prodState_neg

theorem xplus_sq : ∑ j, xplus j ^ 2 = 1 := by simp [Fin.sum_univ_three]

theorem z3_sq : ∑ j, z3 j ^ 2 = 1 := by simp [Fin.sum_univ_three]

set_option maxHeartbeats 1000000 in
/-- **Lemma P (aligned parity).** Four candidate cones, each preserved by the aligned gate of its
twist bit, that satisfy the four-copy interface have twist bits of even parity. Witnesses: the
states `gateOf τ01 (prodState xplus z3)`, `gateOf τ23 (prodState xplus z3)` and the gate-supplied
effects of `(xplus, z3)` on pair `02` and of `(-xplus, -z3)` on pair `13`; the value of `famI` on
them is `(1/16)(σ01 σ02 σ23 σ13 - 1)`, which is `-1/8` at every odd pattern. -/
theorem kt4_parity_aligned {τ01 τ23 τ02 τ13 : Bool}
    (c01 : CandidateCone K01) (c23 : CandidateCone K23) (c02 : CandidateCone K02)
    (c13 : CandidateCone K13)
    (g01 : ∀ ω ∈ K01, gateOf τ01 ω ∈ K01) (g23 : ∀ ω ∈ K23, gateOf τ23 ω ∈ K23)
    (g02 : ∀ ω ∈ K02, gateOf τ02 ω ∈ K02) (g13 : ∀ ω ∈ K13, gateOf τ13 ω ∈ K13)
    (h : FourCopyCoherent K01 K23 K02 K13) : EvenCycle4 τ01 τ23 τ02 τ13 := by
  have hX := g01 _ (c01.1 xplus xplus_mem z3 z3_mem)
  have hY := g23 _ (c23.1 xplus xplus_mem z3 z3_mem)
  have hE := gate_sharp_mem_dualW c02 g02 xplus_sq z3_sq
  have hF := gate_sharp_mem_dualW c13 g13 ((sum_neg_sq xplus).trans xplus_sq)
    ((sum_neg_sq z3).trans z3_sq)
  have hv := h.famI _ hX _ hY _ hE _ hF
  simp only [gateOf_sharp, gateOf_prodState_xplus_z3, gateOf_prodState_neg, ipW_dg_smul] at hv
  revert hv
  cases τ01 <;> cases τ23 <;> cases τ02 <;> cases τ13 <;> norm_num [sgnB, EvenCycle4, Bool.toNat]

end

end FourCopy
end OIBridge

#print axioms OIBridge.FourCopy.ipW_comm
#print axioms OIBridge.FourCopy.ipW_tens
#print axioms OIBridge.FourCopy.transposeW_transposeW
#print axioms OIBridge.FourCopy.ipW_dg_smul
#print axioms OIBridge.FourCopy.phiW_tabMul
#print axioms OIBridge.FourCopy.ipW_gateOf
#print axioms OIBridge.FourCopy.gateOf_sharp
#print axioms OIBridge.FourCopy.gate_sharp_mem_dualW
#print axioms OIBridge.FourCopy.dualW_of_inv
#print axioms OIBridge.FourCopy.incl_I
#print axioms OIBridge.FourCopy.incl_II
#print axioms OIBridge.FourCopy.incl_I_aligned
#print axioms OIBridge.FourCopy.incl_II_aligned
#print axioms OIBridge.FourCopy.cnotTw_prodState_xplus_z3
#print axioms OIBridge.FourCopy.gateOf_prodState_xplus_z3
#print axioms OIBridge.FourCopy.gateOf_prodState_neg
#print axioms OIBridge.FourCopy.kt4_parity_aligned
