/-
  OIBridge/FourCopyCore.lean — design (EQ4-F), not adopted: the Pauli-free vocabulary of the
  four-copy package KT(4; 01|23, 02|13) → IE₁ ∧ parity. Definitions only: every proof obligation
  of the package lives in another module. No complex number, Pauli matrix or PSD cone appears.

  * the four-copy contraction `fourVal` and Lemma R's interface form `PairLinked`;
  * the COMP-1 chart of a pair body (`flatW`, `pairBody`, `tabCoord`, `tabEff`);
  * KT(4) as COMP-1 data (`KT4`, `KT4LT`) and the core the proof consumes (`KT4Core`);
  * N-CLASS gates, Bell tables, the Bell-link map Θ, rotations, IE₁, the orientation bit;
  * the instance: the pairs `01, 23, 02, 13` and the twist parity of the four-cycle.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.FourCopyParity
import Mathlib.LinearAlgebra.UnitaryGroup

namespace OIBridge
namespace FourCopy

open Set CompositeDimension K2Guard EffectSpace KInfFoundations TransitiveBody CompositeInterface
open OrbitNormalization
open scoped Matrix

noncomputable section

/-! ### §A — the four-copy contraction and Lemma R -/

/-- The four-copy contraction: `X` on tokens `01`, `Y` on `23`, `E` on `02`, `F` on `13`. -/
def fourVal (X Y E F : W 3) : ℝ := ∑ a, ∑ b, ∑ c, ∑ d, X a b * Y c d * E a c * F b d

/-- The two families read from one target pair `K`, with partner `K'` and link pairs `La`, `Lb`. -/
structure PairLinked (K K' La Lb : Set (W 3)) : Prop where
  upper : ∀ X ∈ K, ∀ Y ∈ K', ∀ E ∈ dualW La, ∀ F ∈ dualW Lb,
    0 ≤ ipW X (tabMul (tabMul E Y) (tabT F))
  lower : ∀ L ∈ La, ∀ L' ∈ Lb, ∀ e ∈ dualW K, ∀ f ∈ dualW K',
    0 ≤ ipW e (tabMul (tabMul L f) (tabT L'))

/-- Lemma R, target `01`. -/
theorem FourCopyCoherent.target01 {K01 K23 K02 K13 : Set (W 3)}
    (h : FourCopyCoherent K01 K23 K02 K13) : PairLinked K01 K23 K02 K13 :=
  ⟨h.famI, h.famII⟩

/-! ### §B — the COMP-1 chart of a pair body -/

/-- The flattening of a pair table to the chart `Fin 16 → ℝ`. -/
def flatW (ω : W 3) : Fin 16 → ℝ := fun i =>
  ω ((@finProdFinEquiv 4 4).symm i).1 ((@finProdFinEquiv 4 4).symm i).2

/-- The normalized body of a pair cone in the flat chart. -/
def pairBody (K : Set (W 3)) : Set (Fin 16 → ℝ) := flatW '' {ω | ω ∈ K ∧ ω 0 0 = 1}

/-- The table-entry functional `ω ↦ ω μ ν` on the flat chart (COMP-1's `coord`). -/
def tabCoord (μ ν : Fin 4) : (Fin 16 → ℝ) →ᵃ[ℝ] ℝ := coord (@finProdFinEquiv 4 4 (μ, ν))

/-- The affine functional of the flat chart with coefficient table `E`. -/
def tabEff (E : W 3) : (Fin 16 → ℝ) →ᵃ[ℝ] ℝ := ∑ μ, ∑ ν, E μ ν • tabCoord μ ν

/-! ### §C — KT(4) -/

/-- **The four-token coherence clause.** On the common body, the product of the coordinate
effects `(a, b)` on pair `01` and `(c, d)` on pair `23` equals the product of the coordinate
effects `(a, c)` on pair `02` and `(b, d)` on pair `13`. -/
def TokenCoherent {V : Type} [NormedAddCommGroup V] [NormedSpace ℝ V]
    {Ω01 Ω23 Ω02 Ω13 : Set (Fin 16 → ℝ)} (PA : PreComposite Ω01 Ω23 V)
    (PB : PreComposite Ω02 Ω13 V) : Prop :=
  ∀ a b c d : Fin 4, ∀ ω ∈ PA.Ω,
    PA.prodEff (tabCoord a b) (tabCoord c d) ω = PB.prodEff (tabCoord a c) (tabCoord b d) ω

/-- **KT(4; 01|23, 02|13).** Two COMP-1 pre-composites of the normalized pair bodies, one per
grouping, with one body and the four-token coherence clause. Local tomography of the four-copy
composite is not a field. -/
structure KT4 (K01 K23 K02 K13 : Set (W 3)) (V : Type) [NormedAddCommGroup V]
    [NormedSpace ℝ V] where
  PA : PreComposite (pairBody K01) (pairBody K23) V
  PB : PreComposite (pairBody K02) (pairBody K13) V
  one_body : PA.Ω = PB.Ω
  tok : TokenCoherent PA PB

/-- **KT(4) with local tomography.** The same data with COMP-1 `Composite`s, whose field `lt` is
local tomography of each grouping. -/
structure KT4LT (K01 K23 K02 K13 : Set (W 3)) (V : Type) [NormedAddCommGroup V]
    [NormedSpace ℝ V] where
  CA : Composite (pairBody K01) (pairBody K23) V
  CB : Composite (pairBody K02) (pairBody K13) V
  one_body : CA.Ω = CB.Ω
  tok : TokenCoherent CA.toPreComposite CB.toPreComposite

/-- The form with local tomography gives `KT4` by forgetting `lt`. -/
def KT4LT.toKT4 {K01 K23 K02 K13 : Set (W 3)} {V : Type} [NormedAddCommGroup V]
    [NormedSpace ℝ V] (H : KT4LT K01 K23 K02 K13 V) : KT4 K01 K23 K02 K13 V :=
  ⟨H.CA.toPreComposite, H.CB.toPreComposite, H.one_body, H.tok⟩

/-- **The core of KT(4) that Lemma B1 reads.** Product states of each grouping in one carrier,
bilinear product effects with their evaluation laws, positivity of each grouping's product
effects on the other grouping's product states, and token coherence on the product states of
each grouping. Each field is a consequence of the corresponding `KT4` fields (`KT4.toCore`); no
body, convexity, normalization, combination law or local tomography is a field. -/
structure KT4Core (K01 K23 K02 K13 : Set (W 3)) (V : Type) [NormedAddCommGroup V]
    [NormedSpace ℝ V] where
  stA : (Fin 16 → ℝ) → (Fin 16 → ℝ) → V
  stB : (Fin 16 → ℝ) → (Fin 16 → ℝ) → V
  effA : ((Fin 16 → ℝ) →ᵃ[ℝ] ℝ) →ₗ[ℝ] ((Fin 16 → ℝ) →ᵃ[ℝ] ℝ) →ₗ[ℝ] (V →ᵃ[ℝ] ℝ)
  effB : ((Fin 16 → ℝ) →ᵃ[ℝ] ℝ) →ₗ[ℝ] ((Fin 16 → ℝ) →ᵃ[ℝ] ℝ) →ₗ[ℝ] (V →ᵃ[ℝ] ℝ)
  effA_apply : ∀ (e f : (Fin 16 → ℝ) →ᵃ[ℝ] ℝ) (x y : Fin 16 → ℝ), effA e f (stA x y) = e x * f y
  effB_apply : ∀ (e f : (Fin 16 → ℝ) →ᵃ[ℝ] ℝ) (x y : Fin 16 → ℝ), effB e f (stB x y) = e x * f y
  posBA : ∀ e f : (Fin 16 → ℝ) →ᵃ[ℝ] ℝ, IsEffectOn (pairBody K02) e →
    IsEffectOn (pairBody K13) f → ∀ x ∈ pairBody K01, ∀ y ∈ pairBody K23, 0 ≤ effB e f (stA x y)
  posAB : ∀ e f : (Fin 16 → ℝ) →ᵃ[ℝ] ℝ, IsEffectOn (pairBody K01) e →
    IsEffectOn (pairBody K23) f → ∀ x ∈ pairBody K02, ∀ y ∈ pairBody K13, 0 ≤ effA e f (stB x y)
  tokA : ∀ a b c d : Fin 4, ∀ x ∈ pairBody K01, ∀ y ∈ pairBody K23,
    effA (tabCoord a b) (tabCoord c d) (stA x y) = effB (tabCoord a c) (tabCoord b d) (stA x y)
  tokB : ∀ a b c d : Fin 4, ∀ x ∈ pairBody K02, ∀ y ∈ pairBody K13,
    effA (tabCoord a b) (tabCoord c d) (stB x y) = effB (tabCoord a c) (tabCoord b d) (stB x y)

/-! ### §D — local maps, N-CLASS gates, Bell tables, rotations -/

/-- Orthogonality of a one-copy linear map. -/
def IsOrth3 (A : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) : Prop :=
  LinearMap.toMatrix' A ∈ Matrix.orthogonalGroup (Fin 3) ℝ

/-- Rotations of one ball. -/
def IsRot3 (R : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) : Prop :=
  LinearMap.toMatrix' R ∈ Matrix.specialOrthogonalGroup (Fin 3) ℝ

/-- The transpose of a one-copy linear map: its adjoint for the Euclidean pairing of one ball. -/
def trn (A : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ) :=
  Matrix.toLin' (LinearMap.toMatrix' A)ᵀ

/-- **N-CLASS**: the gate is `cnot` between orthogonal local maps, post-locals `(A, B)` and
pre-locals `(A', B')`. -/
def NClass (N : W 3 ≃ₗ[ℝ] W 3) (A B A' B' : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) : Prop :=
  IsOrth3 A ∧ IsOrth3 B ∧ IsOrth3 A' ∧ IsOrth3 B' ∧
    ∀ ω, N ω = actC A (actT B (cnot (actC A' (actT B' ω))))

/-- The post-local Bell table `H_R`, `R = A · reflY · Bᵀ`. -/
def bellOf (A B : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) : W 3 := actC A (actT B phiW)

/-- The chart of a Bell table: `R = A · reflY · Bᵀ`. -/
def chartOf (A B : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ) :=
  A ∘ₗ reflY ∘ₗ trn B

/-- The Bell-link map in general charts: `Θ g = H_{R02} · g · H_{R13}ᵀ`. -/
def Theta (A02 B02 A13 B13 : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) (g : W 3) : W 3 :=
  tabMul (tabMul (bellOf A02 B02) g) (tabT (bellOf A13 B13))

/-- The inverse of Θ for orthogonal locals. -/
def ThetaInv (A02 B02 A13 B13 : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) (g : W 3) : W 3 :=
  actC (trn (chartOf A02 B02)) (actT (trn (chartOf A13 B13)) g)

/-- The orientation bit of a pair of local maps: their determinant product is `-1`. -/
def orient (A B : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) : Bool :=
  decide (LinearMap.det A * LinearMap.det B = -1)

/-- **IE₁** for one pair cone: invariance under every local rotation of either token. -/
def IE1 (K : Set (W 3)) : Prop :=
  ∀ R, IsRot3 R → actC R '' K = K ∧ actT R '' K = K

/-- The rotation word `rot3 a ∘ rotX b`. -/
def rotWord (a b : ℝ) : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ) :=
  ((rot3 a).linear : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) ∘ₗ
    ((rotX b).linear : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ))

/-- The reversed word `rotX b ∘ rot3 a`. -/
def rotWord' (a b : ℝ) : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ) :=
  ((rotX b).linear : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) ∘ₗ
    ((rot3 a).linear : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ))

/-! ### §E — the instance -/

/-- The four pairs of the instance: the groups of the groupings `01|23` and `02|13`. -/
inductive Pr
  | p01 | p23 | p02 | p13
  deriving DecidableEq

/-- The interface predicate for a family of pair cones. -/
abbrev FCC (K : Pr → Set (W 3)) : Prop := FourCopyCoherent (K .p01) (K .p23) (K .p02) (K .p13)

/-- Twist parity of the four-cycle. -/
def EvenCycle (τ : Pr → Bool) : Prop := EvenCycle4 (τ .p01) (τ .p23) (τ .p02) (τ .p13)

end

end FourCopy
end OIBridge

#print axioms OIBridge.FourCopy.FourCopyCoherent.target01
