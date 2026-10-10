/-
  UNBUILT DRAFT — POS-SEP research thread.  NEVER COMPILED: no Lean toolchain was available.
  Not part of the repository, not adopted, not frozen.  Every `sorry` is an open obligation; the
  non-`sorry` proofs are written against the landed statements at L = e2426ba4 but have not been
  checked by the kernel and may need tactic repairs.

  Contents
    §1 (N1)  frame, relT and relC transfer from `G` to `G.symm`; hence the two positivity clauses are
             exchanged by `G ↦ G.symm`.
    §2       the clause bundle without `posInv`, and the swap lemma.
    §3       the d = 5 squeezed gate (eps = 1/10, lam = 1/2) and the statements a later round would
             prove: frame, GateRel, posFwd (by the written proof in LEDGER.md §N3.3), ¬ posInv
             (exact witness, value −1/2).
-/
import OIBridge.OddChar

namespace OIBridge
namespace PosSepDraft

open CompositeDimension ParityNot OddChar EffectSpace

variable {d : ℕ}

/-! ### §1 — N1: the algebraic clauses transfer to the inverse -/

theorem add_add_fin2 : ∀ a b : Fin 2, a + (a + b) = b := by decide

theorem frame_symm {z : Fin d → ℝ} {G : W d ≃ₗ[ℝ] W d}
    (hF : ∀ a b : Fin 2,
      G (prodState (corner z a) (corner z b)) = prodState (corner z a) (corner z (a + b))) :
    ∀ a b : Fin 2,
      G.symm (prodState (corner z a) (corner z b)) = prodState (corner z a) (corner z (a + b)) := by
  intro a b
  have h := hF a (a + b)
  rw [add_add_fin2] at h
  rw [← h, G.symm_apply_apply]

theorem gateRel_symm {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}
    (hN : IsNot (eball d) z N) (hR : GateRel N G) : GateRel N G.symm := by
  have hT : ∀ ω, G (actT N ω) = actT N (G ω) := fun ω => by
    have h := hR.relT (actT N ω)
    rw [actT_actT hN.invol] at h
    exact h.symm
  have hC : ∀ ω, G (actC N ω) = actC N (actT N (G ω)) := fun ω => by
    have h := congrArg (actC N) (hR.relC ω)
    rwa [actC_actC hN.invol] at h
  refine ⟨fun ω => ?_, fun ω => ?_⟩
  · apply G.injective
    rw [hT, G.apply_symm_apply, G.apply_symm_apply, actT_actT hN.invol]
  · have key : G.symm (actC N ω) = actC N (actT N (G.symm ω)) := by
      rw [LinearEquiv.symm_apply_eq, hC, hT, G.apply_symm_apply, actT_actT hN.invol]
    rw [key, actC_actC hN.invol]

/-! ### §2 — the bundle without inverse positivity -/

/-- `NativeGate` with `posInv` removed. -/
structure FwdGate (Ω : Set (Fin d → ℝ)) (z : Fin d → ℝ) (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ))
    (G : W d ≃ₗ[ℝ] W d) : Prop where
  frame : ∀ a b : Fin 2,
    G (prodState (corner z a) (corner z b)) = prodState (corner z a) (corner z (a + b))
  posFwd : ∀ x ∈ Ω, ∀ y ∈ Ω, G (prodState x y) ∈ maxCone Ω
  relT : ∀ ω, actT N (G (actT N ω)) = G ω
  relC : ∀ ω, actC N (G (actC N ω)) = actT N (G ω)

/-- The swap: `G` has frame, relations and `posInv` iff `G.symm` is a `FwdGate`.  One direction
shown; the other is the same with `G.symm.symm = G`. -/
theorem fwdGate_symm {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}
    (hN : IsNot (eball d) z N)
    (hF : ∀ a b : Fin 2,
      G (prodState (corner z a) (corner z b)) = prodState (corner z a) (corner z (a + b)))
    (hR : GateRel N G)
    (hInv : ∀ x ∈ eball d, ∀ y ∈ eball d, G.symm (prodState x y) ∈ maxCone (eball d)) :
    FwdGate (eball d) z N G.symm :=
  ⟨frame_symm hF, hInv, (gateRel_symm hN hR).relT, (gateRel_symm hN hR).relC⟩

/-- N2.2 (statement only): with the forward corner map a cone automorphism, forward positivity
alone selects `d ∈ {1, 3}`.  Proof plan: DIM-1's §Q verbatim, with `Minv` replaced by the inverse
of `Mfwd` (bijective because `G` is injective and `tens_hom_inj`), `gate_corner_symm` derived from
`gate_corner`, and `lor_Minv` supplied by the hypothesis `hAut`. -/
theorem dim_of_fwdGate_aut {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}
    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hG : FwdGate (eball d) z N G)
    (hAut : ∀ t : HVec d, Lor t → ∃ Y, Lor Y ∧ Mfwd z G Y = t) : d = 1 ∨ d = 3 := by
  sorry

/-! ### §3 — the d = 5 squeezed gate -/

/-- Classical control indices `0` and `5`; tangent control indices `1..4`. -/
def permT5 : Fin 6 → Fin 6
  | 1 => 3 | 2 => 4 | 3 => 1 | 4 => 2 | μ => μ

def sigma5 : Fin 6 → Fin 6
  | 0 => 1 | 1 => 0 | 5 => 3 | 3 => 5 | ν => ν

/-- `K_lam` with `lam = 1/2`, as a column weight. -/
noncomputable def kw (ν : Fin 6) : ℝ := if ν = 0 ∨ ν = 5 then 1 else 1 / 2

/-- The squeezed gate as a function: the entry of the image at `(m, n)`.
  Classical rows `m ∈ {0,5}`: `ω' m n = kw n * ω (if odd5 n then 5 - m else m) n`.
  Tangent rows `m ∈ {1..4}`: `ω' m n = (1/10) * kw (sigma5 n) * ω (if odd5 n then permT5 m else m) (sigma5 n)`.
  (sigma5 is an involution preserving `odd5`, permT5 an involution exchanging `odd5`.) -/
noncomputable def sqzFun (ω : W 5) : W 5 := fun m n =>
  if m = 0 ∨ m = 5 then kw n * ω (if odd5 n then (if m = 0 then 5 else 0) else m) n
  else (1 / 10) * kw (sigma5 n) * ω (if odd5 n then permT5 m else m) (sigma5 n)

-- The linear equivalence (inverse: the same index map with weights inverted) — to be written.
noncomputable def sqz : W 5 ≃ₗ[ℝ] W 5 := sorry

theorem sqz_frame (a b : Fin 2) :
    sqz (prodState (corner z5 a) (corner z5 b)) = prodState (corner z5 a) (corner z5 (a + b)) := by
  sorry

theorem gateRel_sqz : GateRel n5 sqz := sorry

/-- Forward positivity: LEDGER.md §N3.3 (decomposition identity, AM–GM, Cauchy–Schwarz, key lemma
`ε (|S_e| + |S_o|) ≤ √(AB)`).  For the kernel, square both sides to avoid `Real.sqrt`. -/
theorem sqz_posFwd : ∀ x ∈ eball 5, ∀ y ∈ eball 5, sqz (prodState x y) ∈ maxCone (eball 5) := sorry

/-- Inverse positivity fails: the exact value is `−1/2`. -/
theorem sqz_symm_value :
    prodEffVal (sharpEff z5) (sharpEff (-x5)) (sqz.symm (prodState z5 x5)) = -1 / 2 := sorry

theorem not_posInv_sqz :
    ¬ ∀ x ∈ eball 5, ∀ y ∈ eball 5, sqz.symm (prodState x y) ∈ maxCone (eball 5) := sorry

/-- The headline (would follow): forward positivity without inverse positivity does not exclude
`d = 5`. -/
theorem fwdGate_five : FwdGate (eball 5) z5 n5 sqz :=
  ⟨sqz_frame, sqz_posFwd, gateRel_sqz.relT, gateRel_sqz.relC⟩

end PosSepDraft
end OIBridge
