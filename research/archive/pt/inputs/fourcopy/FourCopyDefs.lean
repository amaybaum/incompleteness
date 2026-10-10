/-
  OIBridge/FourCopyDefs.lean — design preflight (EQ4-F), not adopted: the shared vocabulary of the
  four-copy package KT(4; 01|23, 02|13) → IE₁. Definitions and definitional lemmas only.

  Four copies of the elementary ball, tokens 0, 1, 2, 3. A pair cone `K ⊆ W 3` is read in DIM-1's
  two-copy table carrier, which encodes two-copy local tomography (CompositeDimension.lean, `W`);
  no four-copy carrier is assumed here. The interface predicate `FourCopyCoherent` is the
  cone-level form of KT(4) with the full Euclidean dual cones as effect families.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.K2Guard

namespace OIBridge
namespace FourCopy

open Set CompositeDimension K2Guard

noncomputable section

/-! ### §A — the table calculus on `W 3` -/

/-- The table product, row index on the first token. On `W 3` the operator `*` is the pointwise
product, so the contraction is written out. -/
def tabMul (A B : W 3) : W 3 := fun μ ν => ∑ κ, A μ κ * B κ ν

/-- The token exchange of a table. -/
def tabT (A : W 3) : W 3 := fun μ ν => A ν μ

/-- The Euclidean pairing of an effect table with a state table. -/
def ipW (E X : W 3) : ℝ := ∑ μ, ∑ ν, E μ ν * X μ ν

/-- The Euclidean dual cone: the tables nonnegative on `K`. -/
def dualW (K : Set (W 3)) : Set (W 3) := {E | ∀ X ∈ K, 0 ≤ ipW E X}

theorem mem_dualW {K : Set (W 3)} {E : W 3} : E ∈ dualW K ↔ ∀ X ∈ K, 0 ≤ ipW E X := Iff.rfl

/-- A convex cone of tables. -/
def IsConvexCone (K : Set (W 3)) : Prop :=
  (∀ ω ∈ K, ∀ ω' ∈ K, ω + ω' ∈ K) ∧ ∀ c : ℝ, 0 ≤ c → ∀ ω ∈ K, c • ω ∈ K

/-- Admissibility of one pair cone: a candidate cone of K2-GUARD-1 that is a convex cone. -/
def PairAdm (K : Set (W 3)) : Prop := CandidateCone K ∧ IsConvexCone K

/-- Signs of the global transpose in the coordinate order `1, X, Y, Z`. -/
def sgnY : Fin 4 → ℝ := ![1, 1, -1, 1]

/-- The global transpose on tables. -/
def transposeW (ω : W 3) : W 3 := fun μ ν => sgnY μ * sgnY ν * ω μ ν

/-! ### §B — the interface predicate -/

/-- The cone-level four-copy interface. `famI`: products of states across `01|23` against
products of effects across `02|13`; `famII`: products of states across `02|13` against products of
effects across `01|23`. The effect factors range over the full Euclidean dual cones. -/
structure FourCopyCoherent (K01 K23 K02 K13 : Set (W 3)) : Prop where
  famI : ∀ X ∈ K01, ∀ Y ∈ K23, ∀ E ∈ dualW K02, ∀ F ∈ dualW K13,
    0 ≤ ipW X (tabMul (tabMul E Y) (tabT F))
  famII : ∀ L ∈ K02, ∀ L' ∈ K13, ∀ e ∈ dualW K01, ∀ f ∈ dualW K23,
    0 ≤ ipW e (tabMul (tabMul L f) (tabT L'))

/-! ### §C — the aligned gates and the twist parity -/

/-- The target action of an involution of one copy, as a linear equivalence of `W 3`. -/
def actTEquiv (N : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) (hN : ∀ x, N (N x) = x) : W 3 ≃ₗ[ℝ] W 3 where
  toFun := actT N
  invFun := actT N
  map_add' ω₁ ω₂ := by
    funext μ ν
    simp only [actT_apply, Pi.add_apply, map_add]
  map_smul' c ω := by
    funext μ ν
    simp only [actT_apply, Pi.smul_apply, map_smul, smul_eq_mul, RingHom.id_apply]
  left_inv := actT_actT hN
  right_inv := actT_actT hN

theorem actTEquiv_apply (N : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) (hN : ∀ x, N (N x) = x) (ω : W 3) :
    actTEquiv N hN ω = actT N ω := rfl

/-- The twin-oriented gate `actT reflY ∘ cnot ∘ actT reflY`. -/
def cnotTw : W 3 ≃ₗ[ℝ] W 3 :=
  actTEquiv reflY reflY_reflY ≪≫ₗ cnot ≪≫ₗ actTEquiv reflY reflY_reflY

theorem cnotTw_apply (ω : W 3) : cnotTw ω = actT reflY (cnot (actT reflY ω)) := rfl

/-- The aligned gate of twist bit `τ`: `cnot` for `false`, `cnotTw` for `true`. -/
def gateOf : Bool → (W 3 ≃ₗ[ℝ] W 3)
  | false => cnot
  | true => cnotTw

theorem gateOf_false : gateOf false = cnot := rfl

theorem gateOf_true : gateOf true = cnotTw := rfl

/-- The twist parity of the four-cycle `0–1–3–2–0`, pairs in the order `01, 23, 02, 13`: the number
of twisted pairs is even. -/
def EvenCycle4 (τ01 τ23 τ02 τ13 : Bool) : Prop :=
  (τ01.toNat + τ23.toNat + τ02.toNat + τ13.toNat) % 2 = 0

end

end FourCopy
end OIBridge

#print axioms OIBridge.FourCopy.actTEquiv
#print axioms OIBridge.FourCopy.cnotTw
