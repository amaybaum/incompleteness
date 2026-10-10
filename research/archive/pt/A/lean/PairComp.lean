/-
  UNBUILT. There is no Lean toolchain in this environment: this text has never been elaborated or
  kernel-checked, and every proof below is a sketch that may need elaboration work. Thread A (PAIR-COMP)
  design text; nothing here is adopted, frozen or proposed for `main`.

  It states, in the vocabulary of `main` at L = 9f9f8257 and of the design modules at ff9c3a35, the three
  objects thread A uses:

  §1  the narrow stage-level product of two `DirectedStages` (node A1): product preparations, product
      labels, the multiplicative table, product stage maps; and its stage consistency (`scInf_prod`);
  §2  the closure form of the audited theorem (node A0): with `hcl` dropped, the remaining hypotheses pass
      to the closures, and `kt4_general_ie1` applied to the closures gives IE1 for every `closure (K p)`
      together with `EvenCycle` (`kt4_forward_ie1_closure`);
  §3  shadow closedness (node A3): a completed body of finite rank is compact, and the cone over a compact
      set inside the slice `ω 0 0 = 1` is closed (`isCompact_body_of_finiteRank`,
      `isClosed_cone_of_isCompact_slice`).

  §2 rests on the design-run lemmas `fourCopyCoherent_of_kt4Core` and `kt4_general_ie1` ([D], not certified).
-/
import OIBridge.CompletionAction
import OIBridge.FourCopyHeadline

namespace OIBridge
namespace PairComp

open Set StageCompletion CompletionAction KInfFoundations CompositeDimension K2Guard FourCopy

/-! ### §1 — the narrow stage-level product -/

/-- The product of two finite stages: product preparations, product labels, product table. -/
noncomputable def FiniteStage.prod (S T : FiniteStage) : FiniteStage where
  P := S.P × T.P
  E := S.E × T.E
  p e x := S.p e.1 x.1 * T.p e.2 x.2
  unit := (S.unit, T.unit)
  nonneg e x := mul_nonneg (S.nonneg _ _) (T.nonneg _ _)
  le_one e x := mul_le_one₀ (S.le_one _ _) (T.nonneg _ _) (T.le_one _ _)
  unit_eq x := by simp only [S.unit_eq, T.unit_eq, mul_one]

/-- The product of two stage maps. -/
def StageMap.prod {S S' T T' : FiniteStage} (f : StageMap S T) (g : StageMap S' T') :
    StageMap (FiniteStage.prod S S') (FiniteStage.prod T T') where
  onE := Prod.map f.onE g.onE
  onP := Prod.map f.onP g.onP
  unit_map := by simp only [FiniteStage.prod, Prod.map, f.unit_map, g.unit_map]

/-- **The narrow stage-level product** of two directed systems (index: the product preorder). -/
noncomputable def DirectedStages.prod (D D' : DirectedStages) : DirectedStages where
  ι := D.ι × D'.ι
  directed i j := by
    obtain ⟨k, hik, hjk⟩ := D.directed i.1 j.1
    obtain ⟨k', hik', hjk'⟩ := D'.directed i.2 j.2
    exact ⟨(k, k'), ⟨hik, hik'⟩, ⟨hjk, hjk'⟩⟩
  stage i := FiniteStage.prod (D.stage i.1) (D'.stage i.2)
  map h := StageMap.prod (D.map h.1) (D'.map h.2)
  comp_E hij hjk e := by
    simp only [StageMap.prod, Prod.map]
    rw [D.comp_E, D'.comp_E]
  comp_P hij hjk x := by
    simp only [StageMap.prod, Prod.map]
    rw [D.comp_P, D'.comp_P]

/-- Stage consistency passes to the product. -/
theorem scInf_prod {D D' : DirectedStages} (h : SCInf D) (h' : SCInf D') :
    SCInf (DirectedStages.prod D D') := by
  intro i j hij e x
  show (D.stage j.1).p ((D.map hij.1).onE e.1) ((D.map hij.1).onP x.1) *
      (D'.stage j.2).p ((D'.map hij.2).onE e.2) ((D'.map hij.2).onP x.2) =
    (D.stage i.1).p e.1 x.1 * (D'.stage i.2).p e.2 x.2
  rw [h i.1 j.1 hij.1 e.1 x.1, h' i.2 j.2 hij.2 e.2 x.2]

/- Remarks (not formalized here). With one-ball stages whose preparations are points of `eball 3` and
whose labels are effects of it, every product label reads `prodEffVal e f (prodState x y)` on a product
preparation (`K2Guard.prodEffVal_prodState`), and 16 product labels whose homogenized coefficient vectors
span `HVec 3 ⊗ HVec 3` read the table out (thread A, a1_stage_product.py, A1.10). The completed body is
then the image of the normalized slice of the product cone `SEP` under an injective linear map
`W 3 → CSpace`, closed, of finite rank 15 (A1.11). Closing the preparations under `cnot` keeps every table
entry in `[0, 1]` (`cnot_prodState_mem_maxCone`; A1.7); closing them under `actT reflY ∘ cnot` does not
(value `-1/2`, A1.9). -/

/-! ### §2 — the closure form of the audited theorem (no `hcl`) -/

theorem isClosed_maxCone : IsClosed (maxCone (eball 3)) := by
  -- maxCone = ⋂ over pairs of effects of the closed half-spaces {ω | 0 ≤ prodEffVal e f ω};
  -- prodEffVal e f is a finite sum of products of constants with coordinates of ω.
  sorry

theorem pairAdm_closure {K : Set (W 3)} (h : PairAdm K) : PairAdm (closure K) := by
  -- products: subset_closure; maxCone bound: closure_minimal h.1.2 isClosed_maxCone;
  -- convex cone: continuity of addition and of scalar multiplication.
  sorry

theorem gate_closure {N : W 3 ≃ₗ[ℝ] W 3} {K : Set (W 3)} (h : ∀ ω ∈ K, N ω ∈ K) :
    ∀ ω ∈ closure K, N ω ∈ closure K := by
  -- N is continuous (finite dimension): N '' closure K ⊆ closure (N '' K) ⊆ closure K.
  sorry

theorem dualW_closure (K : Set (W 3)) : dualW (closure K) = dualW K := by
  -- ⊆: K ⊆ closure K; ⊇: X ↦ ipW E X is continuous, so its nonnegativity on K passes to closure K.
  sorry

theorem fcc_closure {K01 K23 K02 K13 : Set (W 3)} (h : FourCopyCoherent K01 K23 K02 K13) :
    FourCopyCoherent (closure K01) (closure K23) (closure K02) (closure K13) := by
  -- the dual cones are unchanged (dualW_closure); the famI and famII values are continuous in the
  -- state slots, and closure K01 ×ˢ closure K23 = closure (K01 ×ˢ K23).
  sorry

/-- **The closure form of `kt4_forward_ie1`.** Without `hcl`, the other hypotheses give IE1 for the
closure of every pair cone and the orientation parity. `hcl` is consumed by the audited theorem only to
pass from `closure (K p)` to `K p` (through `bidual_of_adm` and `inv_mem_of_orth`). -/
theorem kt4_forward_ie1_closure (K : Pr → Set (W 3)) (N : Pr → W 3 ≃ₗ[ℝ] W 3)
    (A B A' B' : Pr → (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ))
    (hcls : ∀ p, NClass (N p) (A p) (B p) (A' p) (B' p)) (hadm : ∀ p, PairAdm (K p))
    (hgate : ∀ p, ∀ ω ∈ K p, N p ω ∈ K p)
    {V : Type} [NormedAddCommGroup V] [NormedSpace ℝ V]
    (H : KT4Core (K .p01) (K .p23) (K .p02) (K .p13) V) :
    (∀ p, IE1 (closure (K p))) ∧ EvenCycle (fun p => orient (A p) (B p)) := by
  have hF : FCC K := fourCopyCoherent_of_kt4Core (hadm .p01).1.2 (hadm .p23).1.2
    (hadm .p02).1.2 (hadm .p13).1.2 (hadm .p01).2.2 (hadm .p23).2.2 (hadm .p02).2.2
    (hadm .p13).2.2 H
  obtain ⟨-, hIE, hpar⟩ := kt4_general_ie1 (fun p => closure (K p)) N A B A' B' hcls
    (fun p => pairAdm_closure (hadm p)) (fun _ => isClosed_closure)
    (fun p => gate_closure (hgate p)) (fcc_closure hF)
  exact ⟨hIE, hpar⟩

/-! ### §3 — shadow closedness -/

/-- A completed body of finite rank is compact (through the landed chart: `exists_completionChart`,
`isClosedEmbedding_chart`; the chart body is closed and bounded in `Fin d → ℝ`, and the body is its
image). -/
theorem isCompact_body_of_finiteRank (D : DirectedStages) (hne : (body D).Nonempty)
    (hfr : FiniteRank (body D)) : IsCompact (body D) := by
  sorry

/-- The cone over a compact set inside the slice `ω 0 0 = 1` is closed. -/
theorem isClosed_cone_of_isCompact_slice {S : Set (W 3)} (hS : IsCompact S)
    (h1 : ∀ ω ∈ S, ω 0 0 = 1) :
    IsClosed {ω : W 3 | ∃ t : ℝ, 0 ≤ t ∧ ∃ s ∈ S, ω = t • s} := by
  -- a limit of t_n • s_n has t_n = (t_n • s_n) 0 0 convergent; extract a convergent subsequence of s_n.
  sorry

/- The shadow route (node A3). For a pair directed system `D`, a read-out `T : CSpace D →L[ℝ] W 3` that is
a finite linear combination of label coordinates (16 product labels suffice) with `T '' body D` in the
slice, finite rank of `body D` gives: `T '' body D` is compact (`isCompact_body_of_finiteRank`, continuity
of `T`), so the cone over it is closed (`isClosed_cone_of_isCompact_slice`). Injectivity of `T` on the body,
which is local tomography of the completed pair system, is not used. Without finite rank the conclusion
fails: thread A's system `D_cl` (a3_shadow_countermodel.py and the written argument W-A3) has the landed
closedness foil `K_cl` as the cone over its shadow. -/

end PairComp
end OIBridge
