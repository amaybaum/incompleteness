/-
  EqBDraft.lean — EQ thread B candidate statements.  UNBUILT: never compiled (no local toolchain).
  Every `sorry` is a written or exact-computation claim of scratchpad/eq/B/RESULT.md, not a kernel fact.
  Vocabulary is that of OIBridge.CompositeDimension and OIBridge.RelcSelect at bcbc516f.
-/
import OIBridge.RelcSelectBlock
import OIBridge.RelcSelectC5

namespace OIBridge
namespace EqB

open KInfFoundations TransitiveBody NativeGateBall CompositeDimension EffectSpace ParityNot RelcSelect

variable {d : ℕ}

/-! ### T1 — the control relation splits into a corner half and a tangent half -/

/-- CI: the −z-corner identity, the only form in which DIM-1's block reduction reads relC
(`gate_corner_neg`, CompositeDimension.lean:1965; `gate_corner_neg_ctrl`, RelcSelectBlock.lean:99). -/
def CornerId (z : Fin d → ℝ) (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (G : W d ≃ₗ[ℝ] W d) : Prop :=
  ∀ Y : HVec d, G (tens (hom (-z)) Y) = tens (hom (-z)) (homMap N (Mfwd z G Y))

/-- TR: the control relation on the tangent control sector. -/
def TangentRel (z : Fin d → ℝ) (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (G : W d ≃ₗ[ℝ] W d) : Prop :=
  ∀ c : Fin d → ℝ, ∑ j, z j * c j = 0 → ∀ Y : HVec d,
    G (tens (lift (N c)) Y) = actC N (actT N (G (tens (lift c) Y)))

/-- T1 (written + exact b1 C2): under `IsNot`, the frame and forward positivity, relC ↔ CI ∧ TR. -/
theorem relC_iff_corner_and_tangent {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}
    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N)
    (hframe : ∀ a b : Fin 2,
      G (prodState (corner z a) (corner z b)) = prodState (corner z a) (corner z (a + b)))
    (hpos : ∀ x ∈ eball d, ∀ y ∈ eball d, G (prodState x y) ∈ maxCone (eball d)) :
    (∀ ω, actC N (G (actC N ω)) = actT N (G ω)) ↔ (CornerId z N G ∧ TangentRel z N G) := by
  sorry

/-- The hypotheses of the block reduction: `CtrlGate` with relC replaced by CI. -/
structure CornerGate (Ω : Set (Fin d → ℝ)) (z : Fin d → ℝ) (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ))
    (G : W d ≃ₗ[ℝ] W d) : Prop where
  frame : ∀ a b : Fin 2,
    G (prodState (corner z a) (corner z b)) = prodState (corner z a) (corner z (a + b))
  posFwd : ∀ x ∈ Ω, ∀ y ∈ Ω, G (prodState x y) ∈ maxCone Ω
  posInv : ∀ x ∈ Ω, ∀ y ∈ Ω, G.symm (prodState x y) ∈ maxCone Ω
  corner : CornerId z N G

/-- T2 (reading of RelcSelectBlock: `hG.relC` is read at :95 only for `gate_corner_neg_ctrl`, and at :746
for parity): the block data, hence `tangentPlus N ≤ 1`, from a corner gate. -/
theorem blockData_of_cornerGate {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}
    {G : W d ≃ₗ[ℝ] W d} (hd : 2 ≤ d) (hN : IsNot (eball d) z N) (hG : CornerGate (eball d) z N G) :
    BlockData (tangentPlus N) := by
  sorry

/-! ### T3 — conditioning: the slices of the kernel's d = 5 gate -/

/-- COND(N): conditioning the NOT of the target on the outcome of the z-test of the control. -/
def Cond (z : Fin d → ℝ) (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (G : W d ≃ₗ[ℝ] W d) : Prop :=
  (∀ Y : HVec d, G (tens (hom z) Y) = tens (hom z) Y) ∧
    (∀ Y : HVec d, G (tens (hom (-z)) Y) = tens (hom (-z)) (homMap N Y))

/-- T3 (exact b1 C1; decide-style like `gC5_frame`). -/
theorem cond_gC5 : Cond z5 nC5 gC5 := by
  sorry

/-- Corollary (from T3 and landed `isNot_nC5`, `gC5_posFwd`, `gC5_posInv`, `gC5_not_relC`): conditioning with
two-sided positivity gives neither relC nor `d = 1 ∨ d = 3`. -/
theorem cond_not_dimension_selecting :
    ¬ (∀ (z : Fin 5 → ℝ) (N : (Fin 5 → ℝ) →ₗ[ℝ] (Fin 5 → ℝ)) (G : W 5 ≃ₗ[ℝ] W 5),
        IsNot (eball 5) z N → Cond z N G →
        (∀ x ∈ eball 5, ∀ y ∈ eball 5, G (prodState x y) ∈ maxCone (eball 5)) →
        (∀ x ∈ eball 5, ∀ y ∈ eball 5, G.symm (prodState x y) ∈ maxCone (eball 5)) →
        (5 = 1 ∨ 5 = 3)) := by
  sorry

/-! ### T4 — two different NOTs: the kernel gate satisfies the two-NOT control relation -/

/-- The balanced NOT `diag(1, −1, 1, −1, −1)` of `eball 5` with axis `z5`. -/
def nA5 : (Fin 5 → ℝ) →ₗ[ℝ] (Fin 5 → ℝ) := diagSign ![1, -1, 1, -1, -1]

theorem isNot_nA5 : IsNot (eball 5) z5 nA5 := by
  sorry

/-- T4 (exact b1 C5): `Rc(nA5, nC5)`: `actC nA5 (gC5 (actC nA5 ω)) = actT nC5 (gC5 ω)`. -/
theorem gC5_relC_two (ω : W 5) : actC nA5 (gC5 (actC nA5 ω)) = actT nC5 (gC5 ω) := by
  sorry

/-! ### T5 — natural conditioning derives the control relation -/

/-- A conditioning assignment on the tests `±z` (index `Bool`, `true = +z`) and the target actions
`I, N` (index `Bool`, `true = N`), with the three naturality laws. -/
structure NaturalCond (z : Fin d → ℝ) (NA NB : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ))
    (C : Bool → Bool → Bool → (W d ≃ₗ[ℝ] W d)) : Prop where
  cov : ∀ a b ω, actC NA (C true a b (actC NA ω)) = C false a b ω
  rel : ∀ a b, C false a b = C true b a
  post : ∀ t a b ω, actT NB (C t a b ω) = C t (!a) (!b) ω

/-- T5 (written, three lines): `Cov ∘ Rel = Post` is the two-NOT control relation for `C true false true`. -/
theorem relC_of_naturalCond {z : Fin d → ℝ} {NA NB : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}
    {C : Bool → Bool → Bool → (W d ≃ₗ[ℝ] W d)} (h : NaturalCond z NA NB C) (ω : W d) :
    actC NA (C true false true (actC NA ω)) = actT NB (C true false true ω) := by
  sorry

/-! ### T6, T7 — the J/K flow at d = 5 and its incompatibility with a local rotation -/

/-- T6 (exact b4 F1–F4 + written positivity with exact identities S1–S3): a one-parameter group of
linear automorphisms of `W 5` through `gC5`, two-sided positive at every time. -/
theorem exists_jkFlow5 :
    ∃ G : ℝ → (W 5 ≃ₗ[ℝ] W 5),
      (∀ s t, G (s + t) = (G t).trans (G s)) ∧ G Real.pi = gC5 ∧
      (∀ t, ∀ x ∈ eball 5, ∀ y ∈ eball 5, G t (prodState x y) ∈ maxCone (eball 5)) ∧
      Continuous (fun p : ℝ × W 5 => G p.1 p.2) := by
  sorry

/-- T7 (exact b5 W5): with `L` the quarter turn of the coordinate plane (2, 4) of `eball 5`, the word
`gC5 ∘ (I ⊗ L) ∘ gC5` maps some product state outside the maximal cone. -/
theorem not_maxCone_gC5_rot :
    ∃ L : (Fin 5 → ℝ) →ₗ[ℝ] (Fin 5 → ℝ), (∀ x, ∑ j, (L x) j ^ 2 = ∑ j, x j ^ 2) ∧
      ∃ x ∈ eball 5, ∃ y ∈ eball 5,
        gC5 (actT L (gC5 (prodState x y))) ∉ maxCone (eball 5) := by
  sorry

end EqB
end OIBridge
