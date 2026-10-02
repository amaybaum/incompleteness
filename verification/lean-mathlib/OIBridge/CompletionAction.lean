/-
  OIBridge/CompletionAction.lean — round OPACT-1: completion-valued operation data and the affine
  automorphisms of the completed body they induce.

  An operation is given on the stage preparations of a directed system, with values in the
  completed body of `StageCompletion`. Two respect conditions are named:
    * `StateRespect`: preparations with the same preparation vector have the same image;
    * `AffineRespect`: every finite affine relation among preparation vectors holds among the images.
  `AffineRespect` implies `StateRespect`; the converse fails (§E).

  Proved here, in the chart of a body of finite rank (`CompletionChart`, which a nonempty body of
  `FiniteRank` admits):
    §A  the two respect conditions, and `AffineRespect → StateRespect`;
    §B  an affine map exists that carries a family to a family respecting all of its finite
        affine relations (`exists_affine_of_relations`);
    §C  the chart body is contained in the closed convex hull of the chart generators, and the
        generators affinely span the chart (`chartBody_subset`, `affineSpan_gen`);
    §D  under `AffineRespect` there is exactly one affine map of the chart extending the datum
        (`existsUnique_induced`), and an affine extension forces `AffineRespect`
        (`affineRespect_of_induced`); the map carries the chart body into itself
        (`induced_mem`); composition is respected (`induced_after`); an operation with an inverse
        datum induces an affine equivalence that preserves the chart body
        (`preservesBody_inducedEquiv`); stage effects pulled back along it are effects
        (`isEffectOn_pullback`);
    §E  the countermodel: a datum on a one-stage system that respects states and does not
        respect affine relations (`midOp_stateRespect`, `midOp_not_affineRespect`).

  Nothing here supplies an operation datum, a flow, transitivity, an invariant inner product, a
  dimension or a ball, and nothing uses SC∞.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.StageCompletion
import Mathlib.LinearAlgebra.Isomorphisms
import Mathlib.LinearAlgebra.Finsupp.LinearCombination

namespace OIBridge
namespace CompletionAction

open Set Topology KInfFoundations OrbitGeneration OrbitNormalization StageCompletion

/-! ### §A — completion-valued operation data and the two respect conditions -/

/-- A completion-valued operation datum: the completed state each stage preparation is carried
to. -/
structure OpDatum (D : DirectedStages) where
  τ : Prep D → CSpace D
  mem_body : ∀ x, τ x ∈ body D

variable {D : DirectedStages}

/-- **StateRespect**: preparations with the same preparation vector have the same image. -/
def StateRespect (T : OpDatum D) : Prop :=
  ∀ x y, prepVec D x = prepVec D y → T.τ x = T.τ y

/-- **AffineRespect**: every finite affine relation among preparation vectors holds among the
images. -/
def AffineRespect (T : OpDatum D) : Prop :=
  ∀ (s : Finset (Prep D)) (c : Prep D → ℝ), ∑ x ∈ s, c x = 0 →
    ∑ x ∈ s, c x • prepVec D x = 0 → ∑ x ∈ s, c x • T.τ x = 0

/-- `AffineRespect` implies `StateRespect`, by the relation `1 • x + (-1) • y`. -/
theorem stateRespect_of_affineRespect {T : OpDatum D} (hT : AffineRespect T) : StateRespect T := by
  classical
  intro x y hxy
  by_cases h : x = y
  · rw [h]
  · let c : Prep D → ℝ := fun z => if z = x then 1 else -1
    have hcx : c x = 1 := if_pos rfl
    have hcy : c y = -1 := if_neg (Ne.symm h)
    have hs := hT {x, y} c
      (by rw [Finset.sum_pair h, hcx, hcy]; norm_num)
      (by rw [Finset.sum_pair h, hcx, hcy, one_smul, neg_one_smul, hxy, add_neg_cancel])
    rw [Finset.sum_pair h, hcx, hcy, one_smul, neg_one_smul] at hs
    exact add_neg_eq_zero.mp hs

/-! ### §B — affine maps from relation-respecting values -/

section Generic

variable {ι E F : Type*} [AddCommGroup E] [Module ℝ E] [AddCommGroup F] [Module ℝ F]

/-- An affine map carries a combination of total weight zero through its linear part. -/
theorem sum_smul_affine (f : E →ᵃ[ℝ] F) (s : Finset ι) (c : ι → ℝ) (v : ι → E)
    (hc : ∑ i ∈ s, c i = 0) :
    ∑ i ∈ s, c i • f (v i) = f.linear (∑ i ∈ s, c i • v i) := by
  have h : ∀ i, f (v i) = f.linear (v i) + f 0 := fun i => congrFun (AffineMap.decomp f) (v i)
  simp only [h, smul_add, Finset.sum_add_distrib, ← Finset.sum_smul, hc, zero_smul, add_zero,
    map_sum, map_smul]

/-- **An affine map exists carrying `v` to `u`** whenever `u` satisfies every finite affine
relation that `v` satisfies. -/
theorem exists_affine_of_relations (v : ι → E) (u : ι → F)
    (h : ∀ (s : Finset ι) (c : ι → ℝ), ∑ i ∈ s, c i = 0 → ∑ i ∈ s, c i • v i = 0 →
      ∑ i ∈ s, c i • u i = 0) :
    ∃ Φ : E →ᵃ[ℝ] F, ∀ i, Φ (v i) = u i := by
  classical
  set A : (ι →₀ ℝ) →ₗ[ℝ] ℝ × E :=
    (Finsupp.linearCombination ℝ fun _ => (1 : ℝ)).prod (Finsupp.linearCombination ℝ v) with hA
  set B : (ι →₀ ℝ) →ₗ[ℝ] ℝ × F :=
    (Finsupp.linearCombination ℝ fun _ => (1 : ℝ)).prod (Finsupp.linearCombination ℝ u) with hB
  have hker : LinearMap.ker A ≤ LinearMap.ker B := by
    intro l hl
    rw [LinearMap.mem_ker] at hl ⊢
    have h1 : Finsupp.linearCombination ℝ (fun _ => (1 : ℝ)) l = 0 := congrArg Prod.fst hl
    have h2 : Finsupp.linearCombination ℝ v l = 0 := congrArg Prod.snd hl
    have s1 : ∑ i ∈ l.support, l i = 0 := by
      have h1' := h1
      rw [Finsupp.linearCombination_apply, Finsupp.sum] at h1'
      simpa using h1'
    have s2 : ∑ i ∈ l.support, l i • v i = 0 := by
      have h2' := h2
      rw [Finsupp.linearCombination_apply, Finsupp.sum] at h2'
      exact h2'
    have h4 : Finsupp.linearCombination ℝ u l = 0 := by
      rw [Finsupp.linearCombination_apply, Finsupp.sum]
      exact h l.support l s1 s2
    exact Prod.ext h1 h4
  obtain ⟨g, hg⟩ := LinearMap.exists_extend
    (((LinearMap.ker A).liftQ B hker).comp A.quotKerEquivRange.symm.toLinearMap)
  have hgA : ∀ l, g (A l) = B l := by
    intro l
    have h1 : g (A l) = (((LinearMap.ker A).liftQ B hker).comp
        A.quotKerEquivRange.symm.toLinearMap) ⟨A l, LinearMap.mem_range_self A l⟩ :=
      LinearMap.congr_fun hg ⟨A l, LinearMap.mem_range_self A l⟩
    rw [h1]
    simp
  have hAs : ∀ i, A (Finsupp.single i 1) = ((1 : ℝ), v i) := fun i => by simp [hA]
  have hBs : ∀ i, B (Finsupp.single i 1) = ((1 : ℝ), u i) := fun i => by simp [hB]
  refine ⟨((LinearMap.snd ℝ ℝ F).comp (g.comp (LinearMap.inr ℝ ℝ E))).toAffineMap +
      AffineMap.const ℝ E (g ((1 : ℝ), (0 : E))).2, fun i => ?_⟩
  have h1 : g ((1 : ℝ), v i) = ((1 : ℝ), u i) := by
    have := hgA (Finsupp.single i 1)
    rwa [hAs i, hBs i] at this
  show (g ((0 : ℝ), v i)).2 + (g ((1 : ℝ), (0 : E))).2 = u i
  rw [← Prod.snd_add, ← map_add, Prod.mk_add_mk, zero_add, add_zero, h1]

end Generic

/-! ### §C — the chart of a completed body of finite rank -/

/-- The chart data of a completed body: an injective affine chart of its affine span, with a
left inverse of the chart's linear part. -/
structure CompletionChart (D : DirectedStages) where
  d : ℕ
  L : (Fin d → ℝ) →ₗ[ℝ] CSpace D
  p0 : CSpace D
  Lg : CSpace D →ₗ[ℝ] (Fin d → ℝ)
  hL : LinearMap.ker L = ⊥
  hLg : ∀ w, Lg (L w) = w
  hspan : ∀ v, v ∈ affineSpan ℝ (body D) ↔ v ∈ Set.range (chart L p0)

/-- A nonempty completed body of finite rank has a chart. -/
theorem exists_completionChart (hne : (body D).Nonempty) (hfr : FiniteRank (body D)) :
    Nonempty (CompletionChart D) := by
  obtain ⟨d, L, p0, hL, hspan⟩ := exists_chart_of_finiteRank hne hfr
  obtain ⟨Lg, hLg⟩ := exists_chart_leftInverse hL
  exact ⟨⟨d, L, p0, Lg, hL, hLg, hspan⟩⟩

variable (C : CompletionChart D)

/-- Chart coordinates of a point of the completion space. -/
noncomputable def coordsOf (v : CSpace D) : Fin C.d → ℝ := chartRetract C.Lg C.p0 v

/-- The completed body read in the chart. -/
def chartBody : Set (Fin C.d → ℝ) := bodyR C.L C.p0 (body D)

/-- The chart coordinates of the preparation vectors. -/
noncomputable def gen (x : Prep D) : Fin C.d → ℝ := coordsOf C (prepVec D x)

theorem mem_range_of_mem_body {v : CSpace D} (hv : v ∈ body D) :
    v ∈ Set.range (chart C.L C.p0) :=
  (C.hspan v).1 (subset_affineSpan ℝ _ hv)

theorem chart_coordsOf {v : CSpace D} (hv : v ∈ body D) : chart C.L C.p0 (coordsOf C v) = v :=
  chart_chartRetract C.hLg (mem_range_of_mem_body C hv)

theorem coordsOf_chart (w : Fin C.d → ℝ) : coordsOf C (chart C.L C.p0 w) = w :=
  chartRetract_chart C.hLg C.p0 w

theorem chart_gen (x : Prep D) : chart C.L C.p0 (gen C x) = prepVec D x :=
  chart_coordsOf C (prepVec_mem_body D x)

theorem coordsOf_mem_chartBody {v : CSpace D} (hv : v ∈ body D) : coordsOf C v ∈ chartBody C := by
  show chart C.L C.p0 (coordsOf C v) ∈ body D
  rw [chart_coordsOf C hv]
  exact hv

theorem isClosedEmbedding_chart : IsClosedEmbedding (chart C.L C.p0) := by
  have h1 : IsClosedEmbedding (C.L : (Fin C.d → ℝ) → CSpace D) :=
    LinearMap.isClosedEmbedding_of_injective C.hL
  have h2 : IsClosedEmbedding (fun v : CSpace D => v + C.p0) :=
    (Homeomorph.addRight C.p0).isClosedEmbedding
  have h3 : (chart C.L C.p0 : (Fin C.d → ℝ) → CSpace D) = (fun v => v + C.p0) ∘ C.L := by
    funext w
    exact chart_apply C.L C.p0 w
  rw [h3]
  exact h2.comp h1

theorem body_convex : Convex ℝ (body D) := (convex_convexHull ℝ _).closure

theorem body_isClosed : IsClosed (body D) := isClosed_closure

/-- **The chart body lies in the closed convex hull of the generators.** -/
theorem chartBody_subset : chartBody C ⊆ closure (convexHull ℝ (Set.range (gen C))) := by
  intro w hw
  have hcomp : (chart C.L C.p0 ∘ gen C) = prepVec D := funext (chart_gen C)
  have himg : chart C.L C.p0 '' closure (convexHull ℝ (Set.range (gen C))) = body D := by
    rw [← (isClosedEmbedding_chart C).closure_image_eq, AffineMap.image_convexHull,
      ← Set.range_comp, hcomp]
    rfl
  have hw' : chart C.L C.p0 w ∈ body D := hw
  rw [← himg] at hw'
  obtain ⟨u, hu, huw⟩ := hw'
  rwa [← chart_injective C.hL C.p0 huw]

/-- **The generators affinely span the chart.** -/
theorem affineSpan_gen : affineSpan ℝ (Set.range (gen C)) = ⊤ := by
  rw [eq_top_iff]
  intro w _
  have hcw : chart C.L C.p0 w ∈ affineSpan ℝ (body D) := (C.hspan _).2 ⟨w, rfl⟩
  have hle : affineSpan ℝ (body D) ≤ (affineSpan ℝ (Set.range (gen C))).map (chart C.L C.p0) := by
    rw [affineSpan_le]
    intro v hv
    obtain ⟨u, rfl⟩ := mem_range_of_mem_body C hv
    refine ⟨u, ?_, rfl⟩
    have hu : u ∈ closure (convexHull ℝ (Set.range (gen C))) := chartBody_subset C hv
    exact (AffineSubspace.closed_of_finiteDimensional _).closure_subset_iff.2
      (convexHull_subset_affineSpan _) hu
  obtain ⟨u, hu, huw⟩ := hle hcw
  rwa [← chart_injective C.hL C.p0 huw]

/-! ### §D — the induced affine map -/

/-- Relations among the generators transfer to the image coordinates. -/
theorem gen_relation {T : OpDatum D} (hT : AffineRespect T) (s : Finset (Prep D))
    (c : Prep D → ℝ) (hc : ∑ x ∈ s, c x = 0) (hv : ∑ x ∈ s, c x • gen C x = 0) :
    ∑ x ∈ s, c x • coordsOf C (T.τ x) = 0 := by
  have h1 : ∑ x ∈ s, c x • prepVec D x = 0 := by
    have := sum_smul_affine (chart C.L C.p0) s c (gen C) hc
    simp only [chart_gen] at this
    rw [this, hv, map_zero]
  have h2 := hT s c hc h1
  have := sum_smul_affine (chartRetract C.Lg C.p0) s c T.τ hc
  show ∑ x ∈ s, c x • chartRetract C.Lg C.p0 (T.τ x) = 0
  rw [this, h2, map_zero]

/-- **Existence.** Under `AffineRespect` an affine map of the chart extends the datum. -/
theorem exists_induced {T : OpDatum D} (hT : AffineRespect T) :
    ∃ Φ : (Fin C.d → ℝ) →ᵃ[ℝ] (Fin C.d → ℝ), ∀ x, Φ (gen C x) = coordsOf C (T.τ x) :=
  exists_affine_of_relations (gen C) (fun x => coordsOf C (T.τ x)) (gen_relation C hT)

/-- **Uniqueness.** Two affine maps of the chart that agree on the generators are equal. -/
theorem induced_unique {Φ Ψ : (Fin C.d → ℝ) →ᵃ[ℝ] (Fin C.d → ℝ)}
    (h : ∀ x, Φ (gen C x) = Ψ (gen C x)) : Φ = Ψ :=
  AffineMap.ext_on (affineSpan_gen C) (by rintro _ ⟨x, rfl⟩; exact h x)

theorem existsUnique_induced {T : OpDatum D} (hT : AffineRespect T) :
    ∃! Φ : (Fin C.d → ℝ) →ᵃ[ℝ] (Fin C.d → ℝ), ∀ x, Φ (gen C x) = coordsOf C (T.τ x) := by
  obtain ⟨Φ, hΦ⟩ := exists_induced C hT
  exact ⟨Φ, hΦ, fun Ψ hΨ => induced_unique C (fun x => by rw [hΦ, hΨ])⟩

/-- **Necessity.** An affine extension of the datum forces `AffineRespect`. -/
theorem affineRespect_of_induced {T : OpDatum D} (Φ : (Fin C.d → ℝ) →ᵃ[ℝ] (Fin C.d → ℝ))
    (hΦ : ∀ x, Φ (gen C x) = coordsOf C (T.τ x)) : AffineRespect T := by
  intro s c hc hv
  have hg : ∑ x ∈ s, c x • gen C x = 0 := by
    have := sum_smul_affine (chartRetract C.Lg C.p0) s c (prepVec D) hc
    rw [hv, map_zero] at this
    exact this
  have hτ : ∀ x, T.τ x = ((chart C.L C.p0).comp Φ) (gen C x) := fun x => by
    rw [AffineMap.comp_apply, hΦ, chart_coordsOf C (T.mem_body x)]
  simp only [hτ]
  rw [sum_smul_affine _ s c (gen C) hc, hg, map_zero]

/-- The affine map of the chart induced by a datum respecting affine relations. -/
noncomputable def induced (T : OpDatum D) (hT : AffineRespect T) :
    (Fin C.d → ℝ) →ᵃ[ℝ] (Fin C.d → ℝ) :=
  Classical.choose (exists_induced C hT)

theorem induced_gen {T : OpDatum D} (hT : AffineRespect T) (x : Prep D) :
    induced C T hT (gen C x) = coordsOf C (T.τ x) :=
  Classical.choose_spec (exists_induced C hT) x

/-- Any affine extension of a datum maps the chart body into itself. -/
theorem mapsTo_chartBody {T : OpDatum D} (Φ : (Fin C.d → ℝ) →ᵃ[ℝ] (Fin C.d → ℝ))
    (hΦ : ∀ x, Φ (gen C x) = coordsOf C (T.τ x)) :
    ∀ w ∈ chartBody C, Φ w ∈ chartBody C := by
  have hS : closure (convexHull ℝ (Set.range (gen C))) ⊆ ((chart C.L C.p0).comp Φ) ⁻¹' body D := by
    refine closure_minimal (convexHull_min ?_ (body_convex.affine_preimage _)) ?_
    · rintro _ ⟨x, rfl⟩
      show chart C.L C.p0 (Φ (gen C x)) ∈ body D
      rw [hΦ, chart_coordsOf C (T.mem_body x)]
      exact T.mem_body x
    · exact body_isClosed.preimage (AffineMap.continuous_of_finiteDimensional _)
  intro w hw
  exact hS (chartBody_subset C hw)

/-- **The completed body is preserved.** -/
theorem induced_mem {T : OpDatum D} (hT : AffineRespect T) :
    ∀ w ∈ chartBody C, induced C T hT w ∈ chartBody C :=
  mapsTo_chartBody C _ (induced_gen C hT)

/-- The datum `S` after the datum `T`. -/
noncomputable def after (S T : OpDatum D) (hS : AffineRespect S) : OpDatum D where
  τ x := chart C.L C.p0 (induced C S hS (coordsOf C (T.τ x)))
  mem_body x := induced_mem C hS _ (coordsOf_mem_chartBody C (T.mem_body x))

theorem comp_gen {S T : OpDatum D} (hS : AffineRespect S) (hT : AffineRespect T) (x : Prep D) :
    ((induced C S hS).comp (induced C T hT)) (gen C x) = coordsOf C ((after C S T hS).τ x) := by
  rw [AffineMap.comp_apply, induced_gen C hT]
  exact (coordsOf_chart C _).symm

theorem affineRespect_after {S T : OpDatum D} (hS : AffineRespect S) (hT : AffineRespect T) :
    AffineRespect (after C S T hS) :=
  affineRespect_of_induced C _ (comp_gen C hS hT)

/-- **Composition.** The map induced by `S` after `T` is the composite of the induced maps. -/
theorem induced_after {S T : OpDatum D} (hS : AffineRespect S) (hT : AffineRespect T) :
    induced C (after C S T hS) (affineRespect_after C hS hT) =
      (induced C S hS).comp (induced C T hT) :=
  induced_unique C fun x => by rw [induced_gen, comp_gen C hS hT]

/-- `S` undoes `T`: `S` after `T` returns every stage preparation. -/
def Undoes (S T : OpDatum D) (hS : AffineRespect S) : Prop :=
  ∀ x, (after C S T hS).τ x = prepVec D x

theorem comp_eq_id {S T : OpDatum D} (hS : AffineRespect S) (hT : AffineRespect T)
    (h : Undoes C S T hS) : (induced C S hS).comp (induced C T hT) = AffineMap.id ℝ _ :=
  induced_unique C fun x => by rw [comp_gen C hS hT, h x, AffineMap.id_apply]; try rfl

/-- **Reversibility.** A datum with an inverse datum induces an affine equivalence of the chart. -/
noncomputable def inducedEquiv {S T : OpDatum D} (hS : AffineRespect S) (hT : AffineRespect T)
    (hST : Undoes C S T hS) (hTS : Undoes C T S hT) : (Fin C.d → ℝ) ≃ᵃ[ℝ] (Fin C.d → ℝ) :=
  AffineEquiv.ofBijective (φ := induced C T hT)
    ⟨Function.LeftInverse.injective (g := induced C S hS)
        (fun w => congrFun (congrArg DFunLike.coe (comp_eq_id C hS hT hST)) w),
      Function.RightInverse.surjective (g := induced C S hS)
        (fun w => congrFun (congrArg DFunLike.coe (comp_eq_id C hT hS hTS)) w)⟩

theorem inducedEquiv_apply {S T : OpDatum D} (hS : AffineRespect S) (hT : AffineRespect T)
    (hST : Undoes C S T hS) (hTS : Undoes C T S hT) (w : Fin C.d → ℝ) :
    inducedEquiv C hS hT hST hTS w = induced C T hT w := rfl

theorem inducedEquiv_symm_apply {S T : OpDatum D} (hS : AffineRespect S) (hT : AffineRespect T)
    (hST : Undoes C S T hS) (hTS : Undoes C T S hT) (w : Fin C.d → ℝ) :
    (inducedEquiv C hS hT hST hTS).symm w = induced C S hS w := by
  rw [AffineEquiv.symm_apply_eq, inducedEquiv_apply]
  exact (congrFun (congrArg DFunLike.coe (comp_eq_id C hT hS hTS)) w).symm

/-- **The induced equivalence preserves the completed body**, in the sense of `OrbitGeneration`. -/
theorem preservesBody_inducedEquiv {S T : OpDatum D} (hS : AffineRespect S)
    (hT : AffineRespect T) (hST : Undoes C S T hS) (hTS : Undoes C T S hT) :
    PreservesBody (chartBody C) {inducedEquiv C hS hT hST hTS} := by
  rintro e rfl w hw
  refine ⟨?_, ?_⟩
  · rw [inducedEquiv_apply]
    exact induced_mem C hT w hw
  · rw [inducedEquiv_symm_apply]
    exact induced_mem C hS w hw

/-- **Effect pullback.** A stage effect read after the induced map is an effect on the chart
body. -/
theorem isEffectOn_pullback {T : OpDatum D} (hT : AffineRespect T) (a : Label D) :
    IsEffectOn (chartBody C) ((effR C.L C.p0 (coord D a)).comp (induced C T hT)) := by
  intro w hw
  exact coord_isEffectOn D a _ (induced_mem C hT w hw)

/-! ### §E — `StateRespect` does not give `AffineRespect` -/

/-- A stage with three preparations reading `0`, `1/2` and `1` on its one non-unit effect: the
second is the midpoint of the first and the third. -/
noncomputable def midStage : FiniteStage where
  P := Fin 3
  E := Bool
  p e x := if e then 1 else ((x : ℕ) : ℝ) / 2
  unit := true
  nonneg e x := by
    split_ifs
    · norm_num
    · positivity
  le_one e x := by
    split_ifs
    · norm_num
    · have hx : (x : ℕ) ≤ 2 := Nat.lt_succ_iff.mp x.isLt
      have hx' : ((x : ℕ) : ℝ) ≤ 2 := by exact_mod_cast hx
      linarith
  unit_eq _ := rfl

theorem midStage_true (k : Fin 3) : midStage.p true k = 1 := rfl

theorem midStage_false (k : Fin 3) : midStage.p false k = ((k : ℕ) : ℝ) / 2 := rfl

theorem midStage_false0 : midStage.p false (0 : Fin 3) = 0 := by
  rw [midStage_false]; norm_num

theorem midStage_false1 : midStage.p false (1 : Fin 3) = 1 / 2 := by
  rw [midStage_false]; norm_num

theorem midStage_false2 : midStage.p false (2 : Fin 3) = 1 := by
  rw [midStage_false]; norm_num

/-- The constant directed system of the midpoint stage. -/
noncomputable def midD : DirectedStages where
  ι := Bool
  directed _ _ := ⟨true, le_top, le_top⟩
  stage _ := midStage
  map _ := ⟨id, id, rfl⟩
  comp_E _ _ _ := rfl
  comp_P _ _ _ := rfl

theorem prepVec_midD_apply (x : Prep midD) (a : Label midD) :
    prepVec midD x a = midStage.p a.2 x.2 := rfl

/-- The exchange of the first preparation and the midpoint. -/
def midSwap : Fin 3 → Fin 3 := ![1, 0, 2]

/-- The datum carrying each preparation to the preparation vector of its exchange. -/
noncomputable def midOp : OpDatum midD where
  τ x := prepVec midD ⟨x.1, midSwap x.2⟩
  mem_body x := prepVec_mem_body midD _

theorem sum_smul_apply {D : DirectedStages} (s : Finset (Prep D)) (c : Prep D → ℝ)
    (f : Prep D → CSpace D) (a : Label D) :
    (∑ x ∈ s, c x • f x) a = ∑ x ∈ s, c x * f x a := by
  rw [lp.coeFn_sum, Finset.sum_apply]
  refine Finset.sum_congr rfl fun x _ => ?_
  rw [lp.coeFn_smul, Pi.smul_apply, smul_eq_mul]

/-- The datum respects states: distinct preparations have distinct preparation vectors. -/
theorem midOp_stateRespect : StateRespect midOp := by
  intro x y hxy
  have hrow : (((x.2 : Fin 3) : ℕ) : ℝ) / 2 = (((y.2 : Fin 3) : ℕ) : ℝ) / 2 :=
    congrArg (fun f : CSpace midD => f ⟨true, false⟩) hxy
  rw [div_left_inj' two_ne_zero] at hrow
  have h2 : (x.2 : Fin 3) = y.2 := Fin.ext (by exact_mod_cast hrow)
  apply lp.ext
  funext a
  show midStage.p a.2 (midSwap x.2) = midStage.p a.2 (midSwap y.2)
  rw [h2]

/-- The preparation of index `k` at the stage `false`. -/
def midPrep (k : Fin 3) : Prep midD := ⟨false, k⟩

theorem midPrep_injective : Function.Injective midPrep := fun a b hab =>
  eq_of_heq (Sigma.mk.inj hab).2

/-- The coefficients of the midpoint relation. -/
def midCoef : Fin 3 → ℝ := ![1, -2, 1]

theorem midCoef0 : midCoef 0 = 1 := rfl

theorem midCoef1 : midCoef 1 = -2 := rfl

theorem midCoef2 : midCoef 2 = 1 := rfl

/-- The datum does not respect the midpoint relation `x₀ - 2 x_m + x₂ = 0`. -/
theorem midOp_not_affineRespect : ¬ AffineRespect midOp := by
  intro h
  let c : Prep midD → ℝ := fun x => midCoef x.2
  have hc : ∑ x ∈ Finset.univ.map ⟨midPrep, midPrep_injective⟩, c x = 0 := by
    rw [Finset.sum_map, Fin.sum_univ_three]
    show midCoef 0 + midCoef 1 + midCoef 2 = 0
    rw [midCoef0, midCoef1, midCoef2]
    norm_num
  have key : ∀ e : Bool, midCoef 0 * midStage.p e (0 : Fin 3) +
      midCoef 1 * midStage.p e (1 : Fin 3) + midCoef 2 * midStage.p e (2 : Fin 3) = 0 := by
    intro e
    rw [midCoef0, midCoef1, midCoef2]
    cases e
    · rw [midStage_false0, midStage_false1, midStage_false2]; norm_num
    · rw [midStage_true, midStage_true, midStage_true]; norm_num
  have hv : ∑ x ∈ Finset.univ.map ⟨midPrep, midPrep_injective⟩, c x • prepVec midD x = 0 := by
    apply lp.ext
    funext a
    rw [sum_smul_apply, Finset.sum_map, Fin.sum_univ_three, lp.coeFn_zero, Pi.zero_apply]
    exact key a.2
  have key2 : midCoef 0 * midStage.p false (1 : Fin 3) +
      midCoef 1 * midStage.p false (0 : Fin 3) + midCoef 2 * midStage.p false (2 : Fin 3) ≠ 0 := by
    rw [midCoef0, midCoef1, midCoef2, midStage_false0, midStage_false1, midStage_false2]
    norm_num
  have hs := h _ c hc hv
  have h3 := congrArg (fun f : CSpace midD => f ⟨false, false⟩) hs
  simp only at h3
  rw [sum_smul_apply, Finset.sum_map, Fin.sum_univ_three, lp.coeFn_zero, Pi.zero_apply] at h3
  exact key2 h3

/-! ### §F — the verdict -/

/-- **Round OPACT-1.** `AffineRespect` implies `StateRespect` and not conversely; under
`AffineRespect` a completion-valued datum induces exactly one affine map of the chart of a body of
finite rank, that map preserves the completed body and composes, an affine extension forces
`AffineRespect`, and a datum with an inverse datum induces an affine equivalence preserving the
completed body. -/
theorem opact1_core :
    (∀ (D : DirectedStages) (T : OpDatum D), AffineRespect T → StateRespect T) ∧
    (StateRespect midOp ∧ ¬ AffineRespect midOp) ∧
    (∀ (D : DirectedStages), (body D).Nonempty → FiniteRank (body D) →
      Nonempty (CompletionChart D)) ∧
    (∀ (D : DirectedStages) (C : CompletionChart D) (T : OpDatum D), AffineRespect T →
      ∃! Φ : (Fin C.d → ℝ) →ᵃ[ℝ] (Fin C.d → ℝ), ∀ x, Φ (gen C x) = coordsOf C (T.τ x)) ∧
    (∀ (D : DirectedStages) (C : CompletionChart D) (T : OpDatum D)
      (Φ : (Fin C.d → ℝ) →ᵃ[ℝ] (Fin C.d → ℝ)), (∀ x, Φ (gen C x) = coordsOf C (T.τ x)) →
        AffineRespect T) ∧
    (∀ (D : DirectedStages) (C : CompletionChart D) (T : OpDatum D) (hT : AffineRespect T),
      ∀ w ∈ chartBody C, induced C T hT w ∈ chartBody C) ∧
    (∀ (D : DirectedStages) (C : CompletionChart D) (S T : OpDatum D) (hS : AffineRespect S)
      (hT : AffineRespect T) (hST : Undoes C S T hS) (hTS : Undoes C T S hT),
        PreservesBody (chartBody C) {inducedEquiv C hS hT hST hTS}) :=
  ⟨fun _ _ hT => stateRespect_of_affineRespect hT,
    ⟨midOp_stateRespect, midOp_not_affineRespect⟩,
    fun _ hne hfr => exists_completionChart hne hfr,
    fun _ C _ hT => existsUnique_induced C hT,
    fun _ C _ Φ hΦ => affineRespect_of_induced C Φ hΦ,
    fun _ C _ hT => induced_mem C hT,
    fun _ C _ _ hS hT hST hTS => preservesBody_inducedEquiv C hS hT hST hTS⟩

end CompletionAction
end OIBridge

#print axioms OIBridge.CompletionAction.stateRespect_of_affineRespect
#print axioms OIBridge.CompletionAction.sum_smul_affine
#print axioms OIBridge.CompletionAction.exists_affine_of_relations
#print axioms OIBridge.CompletionAction.exists_completionChart
#print axioms OIBridge.CompletionAction.chartBody_subset
#print axioms OIBridge.CompletionAction.affineSpan_gen
#print axioms OIBridge.CompletionAction.existsUnique_induced
#print axioms OIBridge.CompletionAction.affineRespect_of_induced
#print axioms OIBridge.CompletionAction.induced_mem
#print axioms OIBridge.CompletionAction.induced_after
#print axioms OIBridge.CompletionAction.comp_eq_id
#print axioms OIBridge.CompletionAction.preservesBody_inducedEquiv
#print axioms OIBridge.CompletionAction.isEffectOn_pullback
#print axioms OIBridge.CompletionAction.midOp_stateRespect
#print axioms OIBridge.CompletionAction.midOp_not_affineRespect
#print axioms OIBridge.CompletionAction.opact1_core
