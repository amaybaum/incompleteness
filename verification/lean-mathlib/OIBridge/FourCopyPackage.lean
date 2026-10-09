/-
  OIBridge/FourCopyPackage.lean — design preflight (EQ4-F), not adopted: the Pauli-dictionary stage
  of the package KT(4; 01|23, 02|13) → IE₁: the identification of each pair cone with `Q3` or its
  twin, and the realization witnesses.

  Every `sorry` here is an open proof obligation and is the whole proof of its theorem. No
  FourCopy module imports this file (only the library root `OIBridge.lean` does), so no proof of
  the Pauli-free route (`FourCopyCore` through `FourCopyHeadline`) depends on it. A theorem below
  whose proof is written out composes other statements and inherits their open obligations;
  `#print axioms` at the end reports `sorryAx` for each such theorem that still rests on one.

  `kt4_forward` takes the four-copy data as `KT4`: two COMP-1 pre-composites (`PreComposite`: the
  interface fields other than local tomography), one body, and the four-token coherence clause
  `TokenCoherent` as an explicit field. Inverse-gate preservation is not a hypothesis: the
  recurrence lemma `inv_mem_of_orth` derives it from orthogonality, closedness and forward
  preservation. `kt4_forward_lt` is the form for COMP-1 `Composite`s, which carry the
  local-tomography field `lt`; it is proved from `kt4_forward` by forgetting `lt`. The pair cones
  are read in DIM-1's two-copy table carrier `W 3`.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.FourCopyHeadline
import OIBridge.MonoidalCompletion
import Mathlib.LinearAlgebra.Matrix.PosDef
import Mathlib.LinearAlgebra.UnitaryGroup
import Mathlib.LinearAlgebra.Matrix.ToLin
import Mathlib.Topology.Instances.Matrix

namespace OIBridge
namespace FourCopy

open Set CompositeDimension K2Guard EffectSpace KInfFoundations TransitiveBody CompositeInterface
open OrbitNormalization
open scoped ComplexOrder Matrix

noncomputable section

variable {K01 K23 K02 K13 : Set (W 3)}

/-! ## Part A — open cheap obligations -/

/-! ### A.1 The four readings of the four-copy contraction (Lemma R) -/

/-- Open. -/
theorem fourVal_eq_23 (X Y E F : W 3) :
    fourVal X Y E F = ipW Y (tabMul (tabMul (tabT E) X) F) := by
  sorry

/-- Open. -/
theorem fourVal_eq_13 (X Y E F : W 3) :
    fourVal X Y E F = ipW F (tabMul (tabMul (tabT X) E) Y) := by
  sorry

/-- Lemma R, target `23` (links read through the token exchange). Open. -/
theorem FourCopyCoherent.target23 (h : FourCopyCoherent K01 K23 K02 K13) :
    PairLinked K23 K01 (tabT '' K02) (tabT '' K13) := by
  sorry

/-- Lemma R, target `13`. Open. -/
theorem FourCopyCoherent.target13 (h : FourCopyCoherent K01 K23 K02 K13) :
    PairLinked K13 K02 (tabT '' K01) (tabT '' K23) := by
  sorry

/-! ### A.2 The cone-level four-copy carrier (Lemma B2; faithfulness, not used by the package) -/

/-- The four-copy table carrier, tokens `0, 1, 2, 3`. It builds in four-copy local tomography and
appears only in Lemma B2, which shows the interface predicate is realized by such a body. -/
abbrev W4 := Fin 4 → Fin 4 → Fin 4 → Fin 4 → ℝ

/-- Product of pair tables across `01|23`. -/
def prodA (X Y : W 3) : W4 := fun a b c d => X a b * Y c d

/-- Product of pair tables across `02|13`. -/
def prodB (L L' : W 3) : W4 := fun a b c d => L a c * L' b d

/-- Product effect across `01|23`. -/
def effA (e f : W 3) (Ω : W4) : ℝ := ∑ a, ∑ b, ∑ c, ∑ d, e a b * f c d * Ω a b c d

/-- Product effect across `02|13`. -/
def effB (E F : W 3) (Ω : W4) : ℝ := ∑ a, ∑ b, ∑ c, ∑ d, E a c * F b d * Ω a b c d

/-- Cone-level KT(4; 01|23, 02|13). -/
structure KT4Cone (K01 K23 K02 K13 : Set (W 3)) (K4 : Set W4) : Prop where
  prodA_mem : ∀ X ∈ K01, ∀ Y ∈ K23, prodA X Y ∈ K4
  prodB_mem : ∀ L ∈ K02, ∀ L' ∈ K13, prodB L L' ∈ K4
  effA_nonneg : ∀ e ∈ dualW K01, ∀ f ∈ dualW K23, ∀ Ω ∈ K4, 0 ≤ effA e f Ω
  effB_nonneg : ∀ E ∈ dualW K02, ∀ F ∈ dualW K13, ∀ Ω ∈ K4, 0 ≤ effB E F Ω

/-- Open. -/
theorem effA_prodA (e f X Y : W 3) : effA e f (prodA X Y) = ipW e X * ipW f Y := by
  sorry

/-- Open. -/
theorem effB_prodB (E F L L' : W 3) : effB E F (prodB L L') = ipW E L * ipW F L' := by
  sorry

/-- Open. -/
theorem effB_prodA (E F X Y : W 3) : effB E F (prodA X Y) = fourVal X Y E F := by
  sorry

/-- Open. -/
theorem effA_prodB (e f L L' : W 3) : effA e f (prodB L L') = fourVal e f L L' := by
  sorry

/-- Token coherence holds in the table model. Open. -/
theorem effA_tens_eq_effB (a b c d : HVec 3) (Ω : W4) :
    effA (tens a b) (tens c d) Ω = effB (tens a c) (tens b d) Ω := by
  sorry

/-- Lemma B2, (⇐): a cone-level four-copy body gives the interface. -/
theorem fourCopyCoherent_of_kt4Cone {K4 : Set W4} (h : KT4Cone K01 K23 K02 K13 K4) :
    FourCopyCoherent K01 K23 K02 K13 where
  famI X hX Y hY E hE F hF := by
    rw [← fourVal_eq_01, ← effB_prodA]
    exact h.effB_nonneg E hE F hF _ (h.prodA_mem X hX Y hY)
  famII L hL L' hL' e he f hf := by
    rw [← fourVal_eq_01, ← effA_prodB]
    exact h.effA_nonneg e he f hf _ (h.prodB_mem L hL L' hL')

/-- Lemma B2, (⇒): the interface is realized by a cone-level four-copy body. -/
theorem exists_kt4Cone_of_fourCopyCoherent (h : FourCopyCoherent K01 K23 K02 K13) :
    ∃ K4 : Set W4, KT4Cone K01 K23 K02 K13 K4 := by
  refine ⟨{Ω | (∀ e ∈ dualW K01, ∀ f ∈ dualW K23, 0 ≤ effA e f Ω) ∧
      (∀ E ∈ dualW K02, ∀ F ∈ dualW K13, 0 ≤ effB E F Ω)}, ⟨?_, ?_, ?_, ?_⟩⟩
  · intro X hX Y hY
    refine ⟨fun e he f hf => ?_, fun E hE F hF => ?_⟩
    · rw [effA_prodA]
      exact mul_nonneg (mem_dualW.1 he X hX) (mem_dualW.1 hf Y hY)
    · rw [effB_prodA, fourVal_eq_01]
      exact h.famI X hX Y hY E hE F hF
  · intro L hL L' hL'
    refine ⟨fun e he f hf => ?_, fun E hE F hF => ?_⟩
    · rw [effA_prodB, fourVal_eq_01]
      exact h.famII L hL L' hL' e he f hf
    · rw [effB_prodB]
      exact mul_nonneg (mem_dualW.1 hE L hL) (mem_dualW.1 hF L' hL')
  · exact fun e he f hf Ω hΩ => hΩ.1 e he f hf
  · exact fun E hE F hF Ω hΩ => hΩ.2 E hE F hF

/-! ### A.3 Aligned gates -/

/-- Open. -/
theorem gateOf_symm_apply (τ : Bool) (ω : W 3) : (gateOf τ).symm ω = gateOf τ ω := by
  sorry

/-- `cnotTw` satisfies DIM-1's native-gate hypotheses with `nflip` and `z3`. Open. -/
theorem nativeGate_cnotTw : NativeGate (eball 3) z3 nflip cnotTw := by
  sorry

/-! ### A.4 Per-token reflection charts -/

/-- The per-token reflection chart on a pair. -/
def chartR (εi εj : Bool) (ω : W 3) : W 3 :=
  (if εi then actC reflY else id) ((if εj then actT reflY else id) ω)

/-- Coboundary twists are removed by per-token reflection charts. Open. -/
theorem chartR_gateOf (εi εj : Bool) (ω : W 3) :
    chartR εi εj (gateOf (εi != εj) (chartR εi εj ω)) = cnot ω := by
  sorry

/-- The interface predicate is transported by per-token reflection charts. Open. -/
theorem fourCopyCoherent_chart (ε : Fin 4 → Bool) (h : FourCopyCoherent K01 K23 K02 K13) :
    FourCopyCoherent (chartR (ε 0) (ε 1) '' K01) (chartR (ε 2) (ε 3) '' K23)
      (chartR (ε 0) (ε 2) '' K02) (chartR (ε 1) (ε 3) '' K13) := by
  sorry

/-! ## Part B — heavy layer (statements; proofs open) -/

/-! ### B.1 Pauli dictionary -/

/-- Pauli matrices in the coordinate order `1, X, Y, Z`. -/
def pauli1 : Fin 4 → Matrix (Fin 2) (Fin 2) ℂ :=
  ![1, !![0, 1; 1, 0], !![0, -Complex.I; Complex.I, 0], !![1, 0; 0, -1]]

/-- The Pauli presentation of a pair table (first index on the first token). -/
def pauliW (ω : W 3) : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ :=
  (1 / 4 : ℂ) • ∑ μ, ∑ ν, ((ω μ ν : ℝ) : ℂ) • MonoidalCompletion.tensorOf (pauli1 μ) (pauli1 ν)

/-- The quantum pair cone. -/
def Q3 : Set (W 3) := {ω | (pauliW ω).PosSemidef}

/-- The twin cone `actT reflY '' Q3`. -/
def twin : Set (W 3) := actT reflY '' Q3

/-- The pair cone of twist bit `τ`. -/
def twistQ3 : Bool → Set (W 3)
  | false => Q3
  | true => twin

/-- Open. -/
theorem phiW_mem_Q3 : phiW ∈ Q3 := by
  sorry

/-- Open. -/
theorem phiW_not_mem_twin : phiW ∉ twin := by
  sorry

theorem idW_mem_twin : idW ∈ twin := ⟨phiW, phiW_mem_Q3, actT_reflY_phiW⟩

/-- Open. -/
theorem idW_not_mem_Q3 : idW ∉ Q3 := by
  sorry

/-- Open. -/
theorem candidateCone_Q3 : CandidateCone Q3 := by
  sorry

/-- Open. -/
theorem isConvexCone_Q3 : IsConvexCone Q3 := by
  sorry

/-- Self-duality of `Q3` for the Euclidean pairing. Open. -/
theorem dualW_Q3 : dualW Q3 = Q3 := by
  sorry

/-- Open. -/
theorem dualW_twin : dualW twin = twin := by
  sorry

theorem isClosed_Q3 : IsClosed Q3 := by
  rw [← dualW_Q3]
  exact isClosed_dualW Q3

/-- The chart rule. Open. -/
theorem chart_rule {A B : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)} (hA : IsOrth3 A) (hB : IsOrth3 B) :
    (fun ω => actC A (actT B ω)) '' Q3 = twistQ3 (orient A B) := by
  sorry

/-- Open. -/
theorem bellOf_mem_twistQ3 {A B : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)} (hA : IsOrth3 A)
    (hB : IsOrth3 B) : bellOf A B ∈ twistQ3 (orient A B) := by
  sorry

/-! ### B.2 Link filters and the pure-state supply -/

/-- The table of the pure state with coefficient matrix `C` (row index on the first token). -/
def pureTab (C : Matrix (Fin 2) (Fin 2) ℂ) : W 3 :=
  fun μ ν => (Matrix.trace (Cᴴ * pauli1 μ * C * (pauli1 ν)ᵀ)).re

/-- Open. -/
theorem pureTab_mem_Q3 (C : Matrix (Fin 2) (Fin 2) ℂ) : pureTab C ∈ Q3 := by
  sorry

/-- The Bloch vector of a nonzero qubit vector. -/
def blochOf (a : Fin 2 → ℂ) : Fin 3 → ℝ :=
  fun j => (Matrix.trace (Matrix.vecMulVec a (star a) * pauli1 j.succ)).re /
    (Matrix.trace (Matrix.vecMulVec a (star a))).re

/-- The filtered conditional of a partner gate effect through Schmidt-diagonal links is a positive
multiple of a pure table with coefficient `diag(1, u) · conj(Circ b) · diag(1, u')`. Open. -/
theorem link_conditional (u u' : ℂ) (b : Fin 2 → ℂ) (hb : b ≠ 0) :
    ∃ c : ℝ, 0 < c ∧
      tabMul (tabMul (cnot (prodState (blochOf ![1, u]) z3))
          (cnot (tens (sharpVec xplus) (sharpVec (blochOf b)))))
        (tabT (cnot (prodState (blochOf ![1, u']) z3))) =
      c • pureTab (Matrix.diagonal ![1, u] * (Matrix.of ![![b 0, b 1], ![b 1, b 0]]).map star *
        Matrix.diagonal ![1, u']) := by
  sorry

/-- Coverage: every coefficient matrix with four nonzero entries has the link form. Open. -/
theorem coverage {C : Matrix (Fin 2) (Fin 2) ℂ} (hC : ∀ i j, C i j ≠ 0) :
    ∃ (u u' : ℂ) (b : Fin 2 → ℂ) (s : ℂ), b ≠ 0 ∧ s ≠ 0 ∧
      C = s • (Matrix.diagonal ![1, u] * (Matrix.of ![![b 0, b 1], ![b 1, b 0]]).map star *
        Matrix.diagonal ![1, u']) := by
  sorry

/-- Density of the coefficient matrices with four nonzero entries. Open. -/
theorem dense_generic : Dense {C : Matrix (Fin 2) (Fin 2) ℂ | ∀ i j, C i j ≠ 0} := by
  sorry

/-- A closed convex cone containing every generic pure table contains `Q3`. Open. -/
theorem Q3_subset_of_generic {K : Set (W 3)} (hK : IsConvexCone K) (hcl : IsClosed K)
    (hpure : ∀ C : Matrix (Fin 2) (Fin 2) ℂ, (∀ i j, C i j ≠ 0) → pureTab C ∈ K) : Q3 ⊆ K := by
  sorry

/-! ### B.3 IE₁ of the Pauli cones -/

/-- IE₁ in the drive form: invariance under the local lifts of the landed drive words. -/
def IE1Drive (K : Set (W 3)) : Prop :=
  ∀ g ∈ driveWords3, actC (g.linear : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) '' K = K ∧
    actT (g.linear : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) '' K = K

/-- Open. -/
theorem ie1_Q3 : IE1 Q3 := by
  sorry

/-- Open. -/
theorem ie1_twin : IE1 twin := by
  sorry

/-- The drive words are rotations, so IE₁ gives the drive form. Open. -/
theorem ie1Drive_of_ie1 {K : Set (W 3)} (h : IE1 K) : IE1Drive K := by
  sorry

/-! ## Part C — the package -/

/-- **Theorem B (aligned charts).** Gates exactly `cnot` or `cnotTw`. Open. -/
theorem kt4_aligned (K : Pr → Set (W 3)) (τ : Pr → Bool)
    (hadm : ∀ p, PairAdm (K p)) (hcl : ∀ p, IsClosed (K p))
    (hgate : ∀ p, ∀ ω ∈ K p, gateOf (τ p) ω ∈ K p) (h : FCC K) :
    (∀ p, K p = twistQ3 (τ p)) ∧ (∀ p, IE1 (K p)) ∧ EvenCycle τ := by
  sorry

/-- **Theorem C (general charts).** N-CLASS gates; inclusion (II) through the dual action of the
inverse gate. Open. -/
theorem kt4_general (K : Pr → Set (W 3)) (N : Pr → W 3 ≃ₗ[ℝ] W 3)
    (A B A' B' : Pr → (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ))
    (hcls : ∀ p, NClass (N p) (A p) (B p) (A' p) (B' p))
    (hadm : ∀ p, PairAdm (K p)) (hcl : ∀ p, IsClosed (K p))
    (hgate : ∀ p, ∀ ω ∈ K p, N p ω ∈ K p) (hinv : ∀ p, ∀ ω ∈ K p, (N p).symm ω ∈ K p)
    (h : FCC K) :
    K .p01 = Theta (A .p02) (B .p02) (A .p13) (B .p13) '' dualW (K .p23) ∧
      (∀ p, K p = twistQ3 (orient (A p) (B p))) ∧ (∀ p, IE1 (K p)) ∧
      EvenCycle (fun p => orient (A p) (B p)) := by
  sorry

/-- **Theorem D (closure level; no closedness).** Open. -/
theorem kt4_closure (K : Pr → Set (W 3)) (N : Pr → W 3 ≃ₗ[ℝ] W 3)
    (A B A' B' : Pr → (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ))
    (hcls : ∀ p, NClass (N p) (A p) (B p) (A' p) (B' p)) (hadm : ∀ p, PairAdm (K p))
    (hgate : ∀ p, ∀ ω ∈ K p, N p ω ∈ K p) (hinv : ∀ p, ∀ ω ∈ K p, (N p).symm ω ∈ K p)
    (h : FCC K) :
    closure (K .p01) = Theta (A .p02) (B .p02) (A .p13) (B .p13) '' dualW (K .p23) ∧
      (∀ p, closure (K p) = twistQ3 (orient (A p) (B p))) ∧ (∀ p, IE1 (closure (K p))) ∧
      EvenCycle (fun p => orient (A p) (B p)) ∧ (∀ p, interior (closure (K p)) ⊆ K p) := by
  sorry

/-- **Theorem A (headline, minimal form).** From KT(4) as two COMP-1 pre-composites with one body
and the four-token coherence clause (Lemma B1), admissible and closed pair cones, and N-CLASS gates
preserving them: every pair cone is `Q3` or its twin in its token charts, IE₁ holds for every pair,
and the twist bits of the four-cycle have even parity. Inverse-gate preservation is derived by the
recurrence lemma. No local tomography of the four-copy composite is a hypothesis. -/
theorem kt4_forward (K : Pr → Set (W 3)) (N : Pr → W 3 ≃ₗ[ℝ] W 3)
    (A B A' B' : Pr → (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ))
    (hcls : ∀ p, NClass (N p) (A p) (B p) (A' p) (B' p))
    (hadm : ∀ p, PairAdm (K p)) (hcl : ∀ p, IsClosed (K p))
    (hgate : ∀ p, ∀ ω ∈ K p, N p ω ∈ K p)
    {V : Type} [NormedAddCommGroup V] [NormedSpace ℝ V]
    (H : KT4 (K .p01) (K .p23) (K .p02) (K .p13) V) :
    (∃ τ : Pr → Bool, (∀ p, K p = twistQ3 (τ p)) ∧ EvenCycle τ) ∧ (∀ p, IE1 (K p)) := by
  have h : FCC K := fourCopyCoherent_of_kt4 (hadm .p01) (hadm .p23) (hadm .p02) (hadm .p13) H
  have hinv : ∀ p, ∀ ω ∈ K p, (N p).symm ω ∈ K p := fun p =>
    inv_mem_of_orth (hcls p).ipW_map (hcl p) (hgate p)
  obtain ⟨-, hK, hIE, hpar⟩ := kt4_general K N A B A' B' hcls hadm hcl hgate hinv h
  exact ⟨⟨fun p => orient (A p) (B p), hK, hpar⟩, hIE⟩

/-- **Theorem A, form with local tomography.** The same conclusion for COMP-1 `Composite`s; it
follows from the minimal form by forgetting `lt`. -/
theorem kt4_forward_lt (K : Pr → Set (W 3)) (N : Pr → W 3 ≃ₗ[ℝ] W 3)
    (A B A' B' : Pr → (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ))
    (hcls : ∀ p, NClass (N p) (A p) (B p) (A' p) (B' p))
    (hadm : ∀ p, PairAdm (K p)) (hcl : ∀ p, IsClosed (K p))
    (hgate : ∀ p, ∀ ω ∈ K p, N p ω ∈ K p)
    {V : Type} [NormedAddCommGroup V] [NormedSpace ℝ V]
    (H : KT4LT (K .p01) (K .p23) (K .p02) (K .p13) V) :
    (∃ τ : Pr → Bool, (∀ p, K p = twistQ3 (τ p)) ∧ EvenCycle τ) ∧ (∀ p, IE1 (K p)) :=
  kt4_forward K N A B A' B' hcls hadm hcl hgate H.toKT4

/-- **Corollary (IE₁ in the drive form).** -/
theorem kt4_forward_drive (K : Pr → Set (W 3)) (hIE : ∀ p, IE1 (K p)) : ∀ p, IE1Drive (K p) :=
  fun p => ie1Drive_of_ie1 (hIE p)

/-! ## Part D — remark, kept apart from the package -/

/-- Realization witness, uniform quantum configuration. Open. -/
theorem fcc_uniform_Q3 : FourCopyCoherent Q3 Q3 Q3 Q3 := by
  sorry

/-- Realization witness, uniform twin configuration. Open. -/
theorem fcc_uniform_twin : FourCopyCoherent twin twin twin twin := by
  sorry

/-- IE₁ without parity does not give the instance: `Q3` on `01`, `23`, `02` and the twin on `13`.
Open. -/
theorem not_fcc_odd : ¬ FourCopyCoherent Q3 Q3 Q3 twin := by
  sorry

end

end FourCopy
end OIBridge

#print axioms OIBridge.FourCopy.fourCopyCoherent_of_kt4Cone
#print axioms OIBridge.FourCopy.kt4_forward
#print axioms OIBridge.FourCopy.kt4_forward_lt
