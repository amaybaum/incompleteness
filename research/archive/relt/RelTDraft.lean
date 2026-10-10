/-
  UNBUILT DRAFT — REL-T research thread. NOT compiled, NOT part of any round, NOT governed.
  No local Lean toolchain was available; nothing here has been checked by the kernel. The statements are
  design sketches for what a later round could state; the proofs indicated are the routes the thread's
  written proofs and exact computations (relt/*.py) suggest, nothing more.

  Context at L = e2426ba4: OIBridge.CompositeDimension (DIM-1), OIBridge.ParityNot (PARITY-NOT-1).
-/
import OIBridge.ParityNot

namespace OIBridge
namespace RelTDraft

open CompositeDimension ParityNot TransitiveBody

variable {d : ℕ}

/-! ### §A — the controlled-`N` gate (relT and the frame, every `d`, every NOT) -/

/-- The corner projector `Π_a = ½ hom z hom zᵀ` and its complement, as matrices on `HVec d`. -/
noncomputable def piA (z : Fin d → ℝ) (μ κ : Fin (d + 1)) : ℝ := hom z μ * hom z κ / 2

noncomputable def piB (z : Fin d → ℝ) (μ κ : Fin (d + 1)) : ℝ :=
  (if μ = κ then 1 else 0) - piA z μ κ

/-- `G ω = Π_a ω + Π_b ω (homMap N)ᵀ`: control-corner `z` passes, everything else gets `N` on the target. -/
noncomputable def ctrlNFun (z : Fin d → ℝ) (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (ω : W d) : W d :=
  fun μ ν => ∑ κ, piA z μ κ * ω κ ν + ∑ κ, piB z μ κ * homMap N (ω κ) ν

-- DESIGN: `ctrlNFun z N (ctrlNFun z N ω) = ω` from `hN.invol` and `Π_a² = Π_a` (needs `hN.unit`);
-- packaged as `ctrlN z N hN : W d ≃ₗ[ℝ] W d`.

-- theorem ctrlN_frame (hN : IsNot (eball d) z N) (a b : Fin 2) :
--     ctrlN z N hN (prodState (corner z a) (corner z b)) = prodState (corner z a) (corner z (a + b))
--   route: `Π_a (hom z) = hom z`, `Π_a (hom (-z)) = 0` from `hN.unit`; `homMap N (hom (±z)) = hom (∓z)`.

-- theorem ctrlN_relT (hN : IsNot (eball d) z N) (ω : W d) :
--     actT N (ctrlN z N hN (actT N ω)) = ctrlN z N hN ω
--   route: `homMap N ∘ homMap N = id` (`homMap_homMap`), row by row.

-- theorem not_relC_ctrlN (hN : IsNot (eball d) z N) (h2 : 2 ≤ d) :
--     ¬ ∀ ω, actC N (ctrlN z N hN (actC N ω)) = actT N (ctrlN z N hN ω)
--   route: relC forces `homMap N ∘ Π_a ∘ homMap N = Π_b`; ranks 1 and d differ for d ≥ 2.

/-- The target relation alone does not give parity: at `d = 2` there are a NOT and a gate with the frame
and the target relation (the controlled-`N` gate with `N = diag(1, −1)`, `z = e₂`). Exact evidence:
`relt_q1q2q3_exact.py`, rows CM2r, CM2n, CM4r, CM4m, CM4n. -/
-- theorem exists_frame_relT_two : ∃ (z : Fin 2 → ℝ) (N : (Fin 2 → ℝ) →ₗ[ℝ] (Fin 2 → ℝ))
--     (G : W 2 ≃ₗ[ℝ] W 2), IsNot (eball 2) z N ∧ (∀ a b : Fin 2,
--       G (prodState (corner z a) (corner z b)) = prodState (corner z a) (corner z (a + b))) ∧
--     (∀ ω, actT N (G (actT N ω)) = G ω)

/-! ### §B — where relC enters the landed parity argument (reading of L, no new proof) -/

-- `ParityNot.Lop_eq_zero_rel` reads only `hR.relT` (through `opGate_comp_homMap_rel`), so injectivity of
-- `Lop` holds from `IsNot` and relT alone; `ParityNot.Lop_anti_rel` reads `hR.relC` (through
-- `opGate_homMap_comp_rel`). A later round could restate:
-- theorem Lop_injective_relT (hN : IsNot (eball d) z N) (hT : ∀ ω, actT N (G (actT N ω)) = G ω) :
--     Function.Injective (Lop G hN.invol)
--   (the body of `Lop_eq_zero_rel` with `opGate_comp_homMap_rel hN hR` replaced by its relT-only proof).

-- In DIM-1 §Q the control relation enters only through `gate_actC`, used only by `gate_corner_neg`.
-- DESIGN: a hypothesis `hneg : ∀ Y, G (tens (hom (-z)) Y) = tens (hom (-z)) (homMap N (Mfwd z G Y))` in place
-- of `relC` would carry `blockData_of_nativeGate` through unchanged.

/-! ### §C — relation-free even exclusions (written proofs + exact algebra; statements only) -/

-- theorem no_frame_pos_two : ¬ ∃ (z : Fin 2 → ℝ) (G : W 2 ≃ₗ[ℝ] W 2), ∑ j, z j ^ 2 = 1 ∧
--     (∀ a b : Fin 2, G (prodState (corner z a) (corner z b)) = prodState (corner z a) (corner z (a + b))) ∧
--     (∀ x ∈ eball 2, ∀ y ∈ eball 2, G (prodState x y) ∈ maxCone (eball 2)) ∧
--     (∀ x ∈ eball 2, ∀ y ∈ eball 2, G.symm (prodState x y) ∈ maxCone (eball 2))
--   route (LEDGER N2.3): `corner_form` at `z` and, for `(I ⊗ ρ_z) ∘ G`, at `−z`; the corner maps are cone
--   automorphisms (`lor_cornerMap` both ways) fixing `e₀`, so `S = M₁ M₀⁻¹ = 1 ⊕ σ`, σ orthogonal, σ z = −z;
--   `tangent_vanish` at both corners puts the tangent slice in `T ⊗ H`; `tangent_vanish` with the target effects
--   `(1, −y)` and `(1, −σ y)` puts the single block `L` in `Lsig`; at `d = 2` every element of `Lsig` is singular.

-- theorem no_frame_pos_four : (same statement at d = 4)
--   route (LEDGER N5): σ-classification; rotation planes and σ = ±I die in the linear core; p_σ = 2 dies by the
--   perturbation identity; p_σ = 1 reduces to: no invertible M ∈ S₃ with M⁻¹ ∈ S₃ (trace/rank argument).

/-! ### §D — the J/K family: relT, the frame and two-sided positivity at every odd `d ≥ 3` -/

-- theorem jk_nativeGate_but_relC (k : ℕ) (hk : 1 ≤ k) : ∃ z N G, IsNot (eball (2*k+1)) z N ∧ frame ∧
--     posFwd ∧ posInv ∧ relT ∧ (k ≥ 2 → ¬ relC)
--   route (LEDGER N4): value decomposition (exact identity) + AM–GM + Bessel for the orthogonal complex
--   structures J on T and K on V₋; posInv from G² = I.

end RelTDraft
end OIBridge
