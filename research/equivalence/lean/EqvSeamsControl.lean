/-
  OIBridge/EqvSeamsControl.lean — design module of the research thread `research/equivalence`
  (node E2), not adopted, not certified: the satisfiability control of `EqvSeams` §D at `d = 3`.

  Conjugating DIM-1's `cnot` on the target copy by the exchange `swap01` of the first two axes,
  which fixes the corner axis `z3` and preserves the ball, gives two-NOT native-gate data
  (`swapped_nativeGate2`) whose target NOT `swap01 ∘ nflip ∘ swap01` differs from the control NOT
  `nflip` (`swapped_not_ne`). Type covariance therefore admits two-NOT data that the one-NOT
  hypothesis does not, and `EqvSeams.nativeGate_of_conj` carries them back to a native gate with
  one NOT (`swapped_nativeGate`).

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.EqvSeams

namespace OIBridge
namespace EqvSeamsControl

open Set KInfFoundations TransitiveBody CompositeDimension EqvSeams

noncomputable section

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

end EqvSeamsControl
end OIBridge

#print axioms OIBridge.EqvSeamsControl.swapped_nativeGate2
#print axioms OIBridge.EqvSeamsControl.swapped_not_ne
#print axioms OIBridge.EqvSeamsControl.swapped_nativeGate
