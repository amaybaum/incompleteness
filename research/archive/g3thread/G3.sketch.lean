/-
  G3.sketch.lean -- UNCOMPILED SKETCH (no Lean toolchain in this session). Off-repo research only:
  nothing here is proposed as ROADMAP or manuscript wording. Landed names are reused from
  OIBridge/CompositeDimension.lean at 06b6f94e (`IsNot` :210, `NativeGate` :218, `plusSpace`,
  `minusSpace`, `finrank_plus_add_finrank_minus` :274, `finrank_plus_eq_finrank_minus` :682,
  `tangentPlus` :727, `actT` :198, `actC` :201, `nflip` :797, `z3` :793, `cnot1`, `neg1`).
  `sorry` marks every step not checked by a kernel; the Mathlib cost is noted per item.
-/
import OIBridge.CompositeDimension

namespace OIBridge
namespace G3Sketch

open CompositeDimension NativeGateBall

/-! ### (1) At d = 3 the native NOT is a π-rotation (the Bloch image of a unitary NOT).
Kernel-cheap: two landed lemmas and `omega`. Direction: NativeGate ⇒ split (2, 2). -/

theorem finrank_plusSpace_eq_two {z : Fin 3 → ℝ} {N : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)}
    {G : W 3 ≃ₗ[ℝ] W 3} (hN : IsNot (eball 3) z N) (hG : NativeGate (eball 3) z N G) :
    Module.finrank ℝ (plusSpace N) = 2 ∧ Module.finrank ℝ (minusSpace N) = 2 := by
  have h1 := finrank_plus_add_finrank_minus hN.invol
  have h2 := finrank_plus_eq_finrank_minus hN hG
  omega

theorem tangentPlus_eq_one_of_nativeGate_three {z : Fin 3 → ℝ}
    {N : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)} {G : W 3 ≃ₗ[ℝ] W 3}
    (hN : IsNot (eball 3) z N) (hG : NativeGate (eball 3) z N G) : tangentPlus N = 1 := by
  unfold tangentPlus
  rw [(finrank_plusSpace_eq_two hN hG).1]

/-! ### (2) The two antiunitary z-flipping NOTs of the ball admit no native gate.
`refl3 = diag(1, 1, -1)` (transpose-type, split (3,1)) and `-id` (universal NOT, split (1,3)).
Cost: the two `finrank` evaluations of explicit diagonal kernels (medium; `Module.finrank` of
`LinearMap.ker` of a diagonal map, e.g. via `Pi.basisFun` and `Submodule.span` of coordinate vectors). -/

def refl3 : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ) where
  toFun x := fun i => (![1, 1, -1] : Fin 3 → ℝ) i * x i
  map_add' x y := by funext i; simp only [Pi.add_apply, mul_add]
  map_smul' c x := by funext i; simp only [Pi.smul_apply, smul_eq_mul, RingHom.id_apply]; ring

theorem isNot_refl3 : IsNot (eball 3) z3 refl3 := sorry          -- as `isNot_nflip` (:838)
theorem finrank_plusSpace_refl3 : Module.finrank ℝ (plusSpace refl3) = 3 := sorry

theorem no_nativeGate_refl3 (G : W 3 ≃ₗ[ℝ] W 3) : ¬ NativeGate (eball 3) z3 refl3 G := fun hG => by
  have := (finrank_plusSpace_eq_two isNot_refl3 hG).1
  rw [finrank_plusSpace_refl3] at this
  omega

theorem isNot_neg3 : IsNot (eball 3) z3 (-LinearMap.id) := sorry
theorem finrank_plusSpace_neg3 :
    Module.finrank ℝ (plusSpace (-LinearMap.id : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ))) = 1 := sorry

theorem no_nativeGate_neg3 (G : W 3 ≃ₗ[ℝ] W 3) :
    ¬ NativeGate (eball 3) z3 (-LinearMap.id) G := fun hG => by
  have := (finrank_plusSpace_eq_two isNot_neg3 hG).1
  rw [finrank_plusSpace_neg3] at this
  omega

/-! ### (3) The algebraic half of `NativeGate` is equivalent to parity balance.
(→) is the landed proof with `NativeGate` weakened to its two relations: `Lop_anti` consumes only
`relC` (through `opGate_homMap_comp`), `Lop_eq_zero` only `relT` (through `opGate_comp_homMap`) and
injectivity of `G`; neither reads `frame`, `posFwd`, `posInv`. The refactor duplicates those two
lemmas with `AlgGate` in place of `NativeGate` (cheap, mechanical).
(←) is the explicit `G_J` of probe P2 (identity on the target-even sector; on the target-odd sector
a control-index map swapping the two eigenspaces, unit ↦ (0, z)); exact at d ≤ 9 for diagonal `N`,
written in general (diagonalize `N` orthogonally with `z` as a basis vector; the relations are
covariant under `actC g ∘ actT g`). Cost: medium (an explicit linear equivalence from a basis
pairing). -/

structure AlgGate {d : ℕ} (z : Fin d → ℝ) (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ))
    (G : W d ≃ₗ[ℝ] W d) : Prop where
  frame : ∀ a b : Fin 2,
    G (prodState (corner z a) (corner z b)) = prodState (corner z a) (corner z (a + b))
  relT : ∀ ω, actT N (G (actT N ω)) = G ω
  relC : ∀ ω, actC N (G (actC N ω)) = actT N (G ω)

theorem algGate_of_nativeGate {d : ℕ} {Ω : Set (Fin d → ℝ)} {z N} {G : W d ≃ₗ[ℝ] W d}
    (hG : NativeGate Ω z N G) : AlgGate z N G := ⟨hG.frame, hG.relT, hG.relC⟩

theorem finrank_plus_eq_finrank_minus_alg {d : ℕ} {z : Fin d → ℝ}
    {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}
    (hN : IsNot (eball d) z N) (hG : AlgGate z N G) :
    Module.finrank ℝ (plusSpace N) = Module.finrank ℝ (minusSpace N) := sorry
    -- the landed proof of `finrank_plus_eq_finrank_minus` (:682), verbatim, after the refactor

theorem exists_algGate_of_balanced {d : ℕ} {z : Fin d → ℝ}
    {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} (hN : IsNot (eball d) z N)
    (hbal : Module.finrank ℝ (plusSpace N) = Module.finrank ℝ (minusSpace N)) :
    ∃ G : W d ≃ₗ[ℝ] W d, AlgGate z N G := sorry

/-- Countercontrol carried as a statement: the algebraic half alone does not select d = 3
(exact witnesses at d = 5, 7, 9 in probe P2; positivity fails there, value −2/5). -/
theorem algGate_five : ∃ (z : Fin 5 → ℝ) (N : (Fin 5 → ℝ) →ₗ[ℝ] (Fin 5 → ℝ)) (G : W 5 ≃ₗ[ℝ] W 5),
    IsNot (eball 5) z N ∧ AlgGate z N G := sorry

/-! ### (4) The gate's Clifford pair. `J := actC N ∘ G` squares to `actT N ∘ G²` by `relC` at `G ω`.
With `G² = id` this is `J² = -1` on the target-odd sector. It holds for the classical `cnot1`
(probe P2, J-row), so it is not a fingerprint of ℂ. Kernel-trivial. -/

theorem gateJ_sq {d : ℕ} {Ω : Set (Fin d → ℝ)} {z N} {G : W d ≃ₗ[ℝ] W d}
    (hG : NativeGate Ω z N G) (ω : W d) :
    actC N (G (actC N (G ω))) = actT N (G (G ω)) :=
  hG.relC (G ω)

/-! ### (5) The Hurwitz reading, stated on the ball family only (no field object in the kernel).
`leNot k` on `Fin (k + 1)`: coordinate 0 (the real off-diagonal axis) fixed, every other coordinate
negated, `z` = the last coordinate. Its split is (2, k) for `k ≥ 1` (probe P1, row B, exact for
k = 1, 2, 4, 8). With it, parity alone (no block bound) gives `k = 2`.
Cost: the `finrank` evaluation (medium). -/

def leNot (k : ℕ) : (Fin (k + 1) → ℝ) →ₗ[ℝ] (Fin (k + 1) → ℝ) where
  toFun x := fun i => (if i = 0 then 1 else -1) * x i
  map_add' x y := by funext i; simp only [Pi.add_apply, mul_add]
  map_smul' c x := by funext i; simp only [Pi.smul_apply, smul_eq_mul, RingHom.id_apply]; ring

def zLast (k : ℕ) : Fin (k + 1) → ℝ := fun i => if i = Fin.last k then 1 else 0

theorem finrank_plusSpace_leNot (k : ℕ) (hk : 1 ≤ k) :
    Module.finrank ℝ (plusSpace (leNot k)) = 2 := sorry
theorem isNot_leNot (k : ℕ) (hk : 1 ≤ k) : IsNot (eball (k + 1)) (zLast k) (leNot k) := sorry

theorem two_of_nativeGate_leNot (k : ℕ) (hk : 1 ≤ k) {G : W (k + 1) ≃ₗ[ℝ] W (k + 1)}
    (hG : NativeGate (eball (k + 1)) (zLast k) (leNot k) G) : k = 2 := by
  have hN := isNot_leNot k hk
  have h1 := finrank_plus_add_finrank_minus hN.invol
  have h2 := finrank_plus_eq_finrank_minus hN hG
  have h3 := finrank_plusSpace_leNot k hk
  omega

end G3Sketch
end OIBridge
