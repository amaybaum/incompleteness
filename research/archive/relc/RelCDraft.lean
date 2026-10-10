/-
  UNBUILT DESIGN DRAFT — REL-C research thread. Not compiled (no local toolchain), not part of the
  repository, not frozen, not preregistered, not governed. Every `sorry` below is an open
  obligation; the comment above it gives the written proof from relc/LEDGER.md. Names of landed
  declarations are those of OIBridge at L = e2426ba4; any Mathlib name not already used by the
  landed OIBridge modules is a guess and must be checked against Mathlib v4.33.0.

  Content: DIM-1's selector with the target relation `relT` removed from the hypotheses.
-/
import OIBridge.ParityNot

namespace OIBridge
namespace RelCDraft

open KInfFoundations TransitiveBody NativeGateBall CompositeDimension ParityNot

variable {d : ℕ}

/-- `NativeGate` without `relT`. -/
structure CtrlGate (Ω : Set (Fin d → ℝ)) (z : Fin d → ℝ) (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ))
    (G : W d ≃ₗ[ℝ] W d) : Prop where
  frame : ∀ a b : Fin 2,
    G (prodState (corner z a) (corner z b)) = prodState (corner z a) (corner z (a + b))
  posFwd : ∀ x ∈ Ω, ∀ y ∈ Ω, G (prodState x y) ∈ maxCone Ω
  posInv : ∀ x ∈ Ω, ∀ y ∈ Ω, G.symm (prodState x y) ∈ maxCone Ω
  relC : ∀ ω, actC N (G (actC N ω)) = actT N (G ω)

theorem ctrlGate_of_nativeGate {Ω : Set (Fin d → ℝ)} {z N} {G : W d ≃ₗ[ℝ] W d}
    (h : NativeGate Ω z N G) : CtrlGate Ω z N G :=
  ⟨h.frame, h.posFwd, h.posInv, h.relC⟩

/-! ### §1 parity from `relC` alone (written proof: LEDGER N1) -/

/- OPEN DESIGN POINT: `actC N` and `actT N` must first be packaged as linear maps of `W d` so that
`{ω | actC N ω = ω}` and `{ω | actC N (actT N ω) = ω}` are kernels (submodules); the two subtypes
below stand for those kernels. -/

/-- `relC` sends `{ω | actC N ω = ω}` into `{ω | actC N (actT N ω) = ω}`, and `G.symm` sends it back. -/
theorem relC_maps_fix {z N} {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N)
    (hC : ∀ ω, actC N (G (actC N ω)) = actT N (G ω)) (ω : W d) (hω : actC N ω = ω) :
    actC N (actT N (G ω)) = G ω := by
  -- from relC: G (actC ω) = actC (actT (G ω)) (landed `gate_actC` argument, relC only)
  have h := congrArg (actC N) (hC ω)
  rw [actC_actC hN.invol, hω] at h
  exact h.symm

/-- Dimension of the control-fixed joint vectors: `(d+1) · dim E₊`.
Written proof: `toOp` identifies them with operators with values in `plusSpace N`;
landed `finrank_ker_eq_of_pointwise` with `M = HVec d`, `S = plusSpace N`. -/
theorem finrank_fixC {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} (hN : ∀ x, N (N x) = x) :
    Module.finrank ℝ {ω : W d // actC N ω = ω} = (d + 1) * Module.finrank ℝ (plusSpace N) := by
  sorry -- UNBUILT; also needs the subtype packaged as a submodule

/-- Dimension of the joint vectors fixed by both actions: `P² + Q²`.
Written proof: through `toOp`, `F` with `H F H = F` commutes with `H = homMap N`, hence maps
`E₊ → E₊` and `E₋ → E₋`; restriction is a linear iso onto `Hom(E₊,E₊) × Hom(E₋,E₋)`
(inverse: `F = f₊ ∘ projPlus + f₋ ∘ projMinus`); each factor by `finrank_ker_eq_of_pointwise`. -/
theorem finrank_fixCT {z N} (hN : IsNot (eball d) z N) :
    Module.finrank ℝ {ω : W d // actC N (actT N ω) = ω}
      = Module.finrank ℝ (plusSpace N) ^ 2 + Module.finrank ℝ (minusSpace N) ^ 2 := by
  sorry -- UNBUILT

/-- **Parity from the control relation alone.** -/
theorem finrank_plus_eq_finrank_minus_relC {z N} {G : W d ≃ₗ[ℝ] W d}
    (hN : IsNot (eball d) z N) (hC : ∀ ω, actC N (G (actC N ω)) = actT N (G ω)) :
    Module.finrank ℝ (plusSpace N) = Module.finrank ℝ (minusSpace N) := by
  -- G restricts to a linear equivalence fixC ≃ fixCT (relC_maps_fix and its converse for G.symm);
  -- so (d+1)·P = P² + Q² with P + Q = d + 1 (landed finrank_plus_add_finrank_minus);
  -- hence Q·(P − Q) = 0 and Q ≥ 1 (landed one_le_finrank_minusSpace): P = Q.
  sorry -- UNBUILT

theorem not_even_of_relC {z N} {G : W d ≃ₗ[ℝ] W d}
    (hN : IsNot (eball d) z N) (hC : ∀ ω, actC N (G (actC N ω)) = actT N (G ω)) : ¬ Even d :=
  not_even_of_balanced (finrank_plus_add_finrank_minus hN.invol)
    (finrank_plus_eq_finrank_minus_relC hN hC)

/-! ### §2 the replacement for DIM-1's single `relT` step (LEDGER N4.2) -/

/- Every §Q lemma of CompositeDimension that blockData_of_orthonormal uses, other than `gate_actT`,
`Mfwd_homMap`, `Minv_homMap`, reads only `frame`, `posFwd`, `posInv`, `relC` (relc/dep_audit.py).
A governed round would restate them over `CtrlGate` (the proofs are unchanged); below they are
cited by their landed names as if so restated. -/

/-- **The new lemma.** For a tangent control slice `c ⊥ z`, `|c| ≤ 1`, the image of the centre
target has no component along `minusSpace N` on the target side.
Written proof (eigen-sign + mixed symmetry): split `c = c₊ + c₋` into `N`-eigencomponents (both ⊥ z).
By relC, `ω± := G (tens (lift c±) (Minv z G t))` satisfies `H ω± H = ± ω±` for every `t`.
For `u ∈ E₋`, `a ↦ Φ(a; u, hom 0)` vanishes on `E_{±}` and `a ↦ Φ(a; hom 0, u)` on `E_{∓}`
(parity of the two pairings under `H`), and `Phi_sphere.2` (extended from `Lor a` to all `a` by
`linearMap_eq_zero_of_lor`) equates them; so both vanish. -/
theorem phi_minus_eq_zero {z N} {G : W d ≃ₗ[ℝ] W d}
    (hN : IsNot (eball d) z N) (hG : CtrlGate (eball d) z N G)
    {c : Fin d → ℝ} (hc : ∑ j, c j ^ 2 ≤ 1) (hzc : ∑ j, z j * c j = 0)
    (a : HVec d) {u : HVec d} (hu : u ∈ minusSpace N) :
    Phi z G a c u (hom 0) = 0 := by
  sorry -- UNBUILT

/-- Replaces L2668 of CompositeDimension: the rows of `G (lift c ⊗ Minv (hom 0))` are fixed by the
homogenized NOT. Written proof: each row is orthogonal to `minusSpace N` (`phi_minus_eq_zero` with
`a = bvec μ`), and `homMap N` is a self-adjoint involution (landed `homMap_dot`). -/
theorem rows_mem_plus {z N} {G : W d ≃ₗ[ℝ] W d}
    (hN : IsNot (eball d) z N) (hG : CtrlGate (eball d) z N G)
    {c : Fin d → ℝ} (hc : ∑ j, c j ^ 2 ≤ 1) (hzc : ∑ j, z j * c j = 0) (μ : Fin (d + 1)) :
    homMap N (G (tens (lift c) (Minv z G (hom 0))) μ) = G (tens (lift c) (Minv z G (hom 0))) μ := by
  sorry -- UNBUILT

/-! ### §3 the selector without `relT` -/

theorem blockData_of_ctrlGate {z N} {G : W d ≃ₗ[ℝ] W d} (hd : 2 ≤ d)
    (hN : IsNot (eball d) z N) (hG : CtrlGate (eball d) z N G) : BlockData (tangentPlus N) := by
  sorry -- UNBUILT: blockData_of_orthonormal verbatim, with `rows_mem_plus` at L2668

theorem dim_of_ctrlGate {z N} {G : W d ≃ₗ[ℝ] W d}
    (hN : IsNot (eball d) z N) (hG : CtrlGate (eball d) z N G) : d = 1 ∨ d = 3 := by
  sorry -- UNBUILT: dim_of_nativeGate verbatim, balance from finrank_plus_eq_finrank_minus_relC

/-! ### §4 `relT` is not implied (d = 3) -/

/-- The rotation of the first two coordinates by `(3/5, 4/5)`; it fixes `z3` and does not commute
with `nflip`. -/
noncomputable def rot3 : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ) := sorry -- UNBUILT: Matrix.toLin' of R3

/-- `cnot ∘ (I ⊗ rot3)`; `I ⊗ M` is `actT M` (the target action of any linear map). -/
noncomputable def cnotR : W 3 ≃ₗ[ℝ] W 3 := sorry -- UNBUILT

theorem ctrlGate_cnotR : CtrlGate (eball 3) z3 nflip cnotR := by
  -- frame, relC: finite evaluation (relc_probe.py C3.1, C3.2);
  -- posFwd: cnotR (prodState x y) = cnot (prodState x (rot3 y)), rot3 y ∈ eball 3, landed
  --   nativeGate_cnot.posFwd;  posInv: cnotR.symm = actT rot3ᵀ ∘ cnot, and pairVal a b (actT M ω)
  --   = pairVal a (homMap Mᵀ b) ω with homMap Mᵀ preserving Lor for orthogonal M.
  sorry -- UNBUILT

theorem not_relT_cnotR : ¬ ∀ ω, actT nflip (cnotR (actT nflip ω)) = cnotR ω := by
  sorry -- UNBUILT: one matrix unit (relc_probe.py C3.3)

end RelCDraft
end OIBridge
