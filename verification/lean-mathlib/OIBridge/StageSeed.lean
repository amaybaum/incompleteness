/-
  OIBridge/StageSeed.lean — design module of the research thread `research/equivalence` (node E8,
  draft S1): the predicted module of round KINF-SEED-1, split from the design module `EqvSeams`
  (§A, built in run 38083519826) with no statement changed. Not adopted, not certified, not a
  round.

  Under SC∞, a stage effect with the value one at one stage preparation and the value zero at
  another gives a sharp seed of `eball C.d` along any affine equivalence carrying the chart body onto
  the ball (`sharpSeed_eball_of_stage`); with TRB-1's identification (`exists_sharpSeed_eball_of_stage`)
  or KTRANS-DENSE-1's (`exists_sharpSeed_eball_of_stage_dense`) the equivalence exists. Every
  hypothesis is a premise; nothing here sources a stage test, a chart or a ball identification.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.DenseOrbit

namespace OIBridge
namespace StageSeed

open Set KInfFoundations OrbitGeneration OrbitNormalization StageCompletion CompletionAction
open TransitiveBody CompositeDimension K2Guard DenseOrbit

noncomputable section

/-! ### §A — K∞-Seed from K∞-Stage -/

/-- **The seed of the ball from a sharp stage test.** Under SC∞, a stage effect certain at one stage
preparation and zero at another, read through the completion chart and an affine equivalence of the
chart body onto `eball C.d`, is a sharp seed of the ball. -/
theorem sharpSeed_eball_of_stage {D : DirectedStages} (C : CompletionChart D) (hSC : SCInf D)
    {i : D.ι} {e : (D.stage i).E} {x1 x0 : (D.stage i).P}
    (h1 : (D.stage i).p e x1 = 1) (h0 : (D.stage i).p e x0 = 0)
    (A : (Fin C.d → ℝ) ≃ᵃ[ℝ] (Fin C.d → ℝ)) (hA : A '' chartBody C = eball C.d) :
    SharpSeed (eball C.d) (effTr A (effR C.L C.p0 (coord D ⟨i, e⟩))) := by
  have h2 : SharpSeed (chartBody C) (effR C.L C.p0 (coord D ⟨i, e⟩)) :=
    sharpSeed_restrict C.L (fun v hv => mem_range_of_mem_body C hv)
      (sharpSeed_completion D hSC h1 h0)
  have h3 := sharpSeed_tr A h2
  rw [hA] at h3
  exact h3

/-- With TRB-1's ball identification of the chart body (K∞-Trans on the chart body). -/
theorem exists_sharpSeed_eball_of_stage {D : DirectedStages} (C : CompletionChart D)
    (hd : 0 < C.d) (hSC : SCInf D) {i : D.ι} {e : (D.stage i).E} {x1 x0 : (D.stage i).P}
    (h1 : (D.stage i).p e x1 = 1) (h0 : (D.stage i).p e x0 = 0)
    {G : Set ((Fin C.d → ℝ) ≃ᵃ[ℝ] (Fin C.d → ℝ))}
    (hG : PreservesBody (chartBody C) G) (hT : BoundaryTransitive (chartBody C) G) :
    ∃ r, SharpSeed (eball C.d) r := by
  obtain ⟨A, hA⟩ := chartBody_eq_eball C hd hG hT
  exact ⟨_, sharpSeed_eball_of_stage C hSC h1 h0 A hA⟩

/-- With KTRANS-DENSE-1's ball identification (a dense boundary orbit on the chart body). -/
theorem exists_sharpSeed_eball_of_stage_dense {D : DirectedStages} (C : CompletionChart D)
    (hd : 0 < C.d) (hSC : SCInf D) {i : D.ι} {e : (D.stage i).E} {x1 x0 : (D.stage i).P}
    (h1 : (D.stage i).p e x1 = 1) (h0 : (D.stage i).p e x0 = 0)
    {G : Set ((Fin C.d → ℝ) ≃ᵃ[ℝ] (Fin C.d → ℝ))}
    (hG : PreservesBody (chartBody C) G) (hT : DenseBoundaryOrbit (chartBody C) G) :
    ∃ r, SharpSeed (eball C.d) r := by
  obtain ⟨A, hA⟩ := chartBody_eq_eball_of_dense C hd hG hT
  exact ⟨_, sharpSeed_eball_of_stage C hSC h1 h0 A hA⟩

end

end StageSeed
end OIBridge

#print axioms OIBridge.StageSeed.sharpSeed_eball_of_stage
#print axioms OIBridge.StageSeed.exists_sharpSeed_eball_of_stage
#print axioms OIBridge.StageSeed.exists_sharpSeed_eball_of_stage_dense
