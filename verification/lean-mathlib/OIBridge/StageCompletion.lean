/-
  OIBridge/StageCompletion.lean — round CMP-1: directed finite stages, stage consistency (SC∞),
  the completion body and its effect-family interface, the binary visible scope (ELEM-bin), and
  the affine-span chart of a body of finite rank.

  Named hypotheses, stated as propositions and proved for no OI construction:
    * SC∞, `SCInf D`: every forward map of the directed system carries the probability table;
    * ELEM-bin, `ElemBinary D`: every stage carries a binary visible test, and the forward maps
      carry the visible outcomes to the visible outcomes;
    * finite rank, `FiniteRank Ω`: the affine span of the body is finite-dimensional.
  The visible-factor clause of the elementary scope (no ancilla or hidden readout) needs available
  transformations and is not defined here.

  Proved here.
    §A  directed stages; the completion value of a stage effect at a stage preparation, read at a
        chosen common upper stage; under SC∞ it equals the value read at any common upper stage
        (`val_eq_at`);
    §B  the completion space `ℓ^∞` over the stage effects, the preparation vectors, the completion
        body (closed convex hull), and the coordinate functionals of stage effects; every
        coordinate functional is an effect on the body and the unit coordinates equal one on it
        (`stageEffects_isEffectOn`, `coord_unit_eq_one`) — with no premise;
    §C  under SC∞, a stage effect certain at one stage preparation and zero at another is a sharp
        seed on the completion body (`sharpSeed_completion`), and its certain state is a boundary
        state (`boundary_completion`);
    §D  under ELEM-bin, the visible test is a test on the whole completion body
        (`visible_test_completion`); with SC∞ a sharp visible pair is perfectly distinguishable by
        the two visible coordinates (`perfectlyDistinguishable_visible`);
    §E  a nonempty body of finite rank admits an injective affine chart whose range is its affine
        span (`exists_chart_of_finiteRank`), the input of `OrbitNormalization.hypotheses_restrict`;
    §F  controls: without SC∞ two common upper stages give different values (`bad_values_differ`);
        the hypotheses are jointly satisfiable on the constant classical-bit tower
        (`bitTower_scInf`, `bitTower_elem`, `bitTower_sharpSeed`).

  Nothing here derives SC∞, ELEM-bin or finite rank from an OI construction, and nothing claims
  a ball, a dimension, a drive or V4′.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.OrbitNormalization
import Mathlib.Analysis.Normed.Lp.lpSpace

namespace OIBridge
namespace StageCompletion

open Set KInfFoundations OrbitGeneration OrbitNormalization
open scoped ENNReal

/-! ### §A — directed stages and the completion value -/

/-- A map of finite stages: effects and preparations carried forward, unit to unit. -/
structure StageMap (S T : FiniteStage) where
  onE : S.E → T.E
  onP : S.P → T.P
  unit_map : onE S.unit = T.unit

/-- Table consistency of a stage map. -/
def StageMap.Consistent {S T : FiniteStage} (f : StageMap S T) : Prop :=
  ∀ e x, T.p (f.onE e) (f.onP x) = S.p e x

/-- A directed system of finite stages with functorial forward maps. -/
structure DirectedStages where
  ι : Type
  [pre : Preorder ι]
  [ne : Nonempty ι]
  directed : ∀ i j : ι, ∃ k, i ≤ k ∧ j ≤ k
  stage : ι → FiniteStage
  map : ∀ {i j : ι}, i ≤ j → StageMap (stage i) (stage j)
  comp_E : ∀ {i j k : ι} (hij : i ≤ j) (hjk : j ≤ k) (e : (stage i).E),
    (map hjk).onE ((map hij).onE e) = (map (hij.trans hjk)).onE e
  comp_P : ∀ {i j k : ι} (hij : i ≤ j) (hjk : j ≤ k) (x : (stage i).P),
    (map hjk).onP ((map hij).onP x) = (map (hij.trans hjk)).onP x

attribute [instance] DirectedStages.pre DirectedStages.ne

/-- **SC∞, stage consistency**: every forward map carries the probability table. -/
def SCInf (D : DirectedStages) : Prop :=
  ∀ (i j : D.ι) (h : i ≤ j), (D.map h).Consistent

variable (D : DirectedStages)

/-- The effect labels of all stages. -/
abbrev Label : Type := Σ i : D.ι, (D.stage i).E

/-- The preparations of all stages. -/
abbrev Prep : Type := Σ i : D.ι, (D.stage i).P

/-- A chosen common upper stage. -/
noncomputable def ub (i j : D.ι) : D.ι := Classical.choose (D.directed i j)

theorem le_ub_left (i j : D.ι) : i ≤ ub D i j := (Classical.choose_spec (D.directed i j)).1

theorem le_ub_right (i j : D.ι) : j ≤ ub D i j := (Classical.choose_spec (D.directed i j)).2

/-- The completion value of the stage effect `a` at the stage preparation `x`, read at the chosen
common upper stage. -/
noncomputable def val (a : Label D) (x : Prep D) : ℝ :=
  (D.stage (ub D x.1 a.1)).p ((D.map (le_ub_right D x.1 a.1)).onE a.2)
    ((D.map (le_ub_left D x.1 a.1)).onP x.2)

theorem val_nonneg (a : Label D) (x : Prep D) : 0 ≤ val D a x :=
  (D.stage _).nonneg _ _

theorem val_le_one (a : Label D) (x : Prep D) : val D a x ≤ 1 :=
  (D.stage _).le_one _ _

/-- Reading through a later stage, under SC∞. -/
theorem read_later (hSC : SCInf D) {i j k n : D.ι} (hi : i ≤ k) (hj : j ≤ k) (hk : k ≤ n)
    (e : (D.stage j).E) (x : (D.stage i).P) :
    (D.stage k).p ((D.map hj).onE e) ((D.map hi).onP x) =
      (D.stage n).p ((D.map (hj.trans hk)).onE e) ((D.map (hi.trans hk)).onP x) := by
  rw [← hSC k n hk, D.comp_E, D.comp_P]

/-- **Well-definedness under SC∞**: the completion value is the value read at any common upper
stage. -/
theorem val_eq_at (hSC : SCInf D) (a : Label D) (x : Prep D) {k : D.ι} (hx : x.1 ≤ k)
    (ha : a.1 ≤ k) :
    val D a x = (D.stage k).p ((D.map ha).onE a.2) ((D.map hx).onP x.2) := by
  obtain ⟨n, hmn, hkn⟩ := D.directed (ub D x.1 a.1) k
  unfold val
  rw [read_later D hSC (le_ub_left D x.1 a.1) (le_ub_right D x.1 a.1) hmn,
    read_later D hSC hx ha hkn]

/-! ### §B — the completion body and the stage effects -/

/-- The completion space: bounded real functions of the stage effects. -/
abbrev CSpace : Type := lp (fun _ : Label D => ℝ) ∞

theorem norm_val_le_one (a : Label D) (x : Prep D) : ‖val D a x‖ ≤ 1 := by
  rw [Real.norm_eq_abs, abs_le]
  exact ⟨by linarith [val_nonneg D a x], val_le_one D a x⟩

/-- The vector of a stage preparation in the completion space. -/
noncomputable def prepVec (x : Prep D) : CSpace D :=
  ⟨fun a => val D a x, memℓp_infty ⟨1, by
    rintro _ ⟨a, rfl⟩
    exact norm_val_le_one D a x⟩⟩

/-- **The completion body**: the closed convex hull of the preparation vectors. -/
def body : Set (CSpace D) :=
  closure (convexHull ℝ (Set.range (prepVec D)))

/-- Evaluation at a stage effect, as a linear functional. -/
noncomputable def evalLin (a : Label D) : CSpace D →ₗ[ℝ] ℝ where
  toFun f := f a
  map_add' f g := by rw [lp.coeFn_add]; rfl
  map_smul' c f := by rw [lp.coeFn_smul]; rfl

/-- Evaluation is continuous. -/
noncomputable def evalCLM (a : Label D) : CSpace D →L[ℝ] ℝ :=
  (evalLin D a).mkContinuous 1 fun f => by
    rw [one_mul]
    exact lp.norm_apply_le_norm ENNReal.top_ne_zero f a

/-- The coordinate functional of a stage effect, as an affine functional. -/
noncomputable def coord (a : Label D) : CSpace D →ᵃ[ℝ] ℝ :=
  (evalLin D a).toAffineMap

theorem coord_apply (a : Label D) (f : CSpace D) : coord D a f = f a := rfl

theorem coord_prepVec (a : Label D) (x : Prep D) : coord D a (prepVec D x) = val D a x := rfl

theorem continuous_coord (a : Label D) : Continuous (coord D a) :=
  (evalCLM D a).continuous

theorem prepVec_mem_body (x : Prep D) : prepVec D x ∈ body D :=
  subset_closure (subset_convexHull ℝ _ ⟨x, rfl⟩)

/-- A closed convex condition that holds on the preparation vectors holds on the body. -/
theorem body_subset {S : Set (CSpace D)} (hc : Convex ℝ S) (hcl : IsClosed S)
    (hp : ∀ x, prepVec D x ∈ S) : body D ⊆ S :=
  closure_minimal (convexHull_min (by rintro _ ⟨x, rfl⟩; exact hp x) hc) hcl

/-- **The effect-family interface**: the coordinate functionals of all stage effects. -/
def stageEffects : Set (CSpace D →ᵃ[ℝ] ℝ) :=
  Set.range (coord D)

/-- Every stage effect is an effect on the completion body. No premise. -/
theorem coord_isEffectOn (a : Label D) : IsEffectOn (body D) (coord D a) := by
  have hc : Convex ℝ {f : CSpace D | 0 ≤ coord D a f ∧ coord D a f ≤ 1} := by
    intro f hf g hg s t hs ht hst
    simp only [Set.mem_setOf_eq] at hf hg ⊢
    rw [Convex.combo_affine_apply hst, smul_eq_mul, smul_eq_mul]
    constructor
    · nlinarith [hf.1, hg.1]
    · nlinarith [hf.2, hg.2]
  have hcl : IsClosed {f : CSpace D | 0 ≤ coord D a f ∧ coord D a f ≤ 1} :=
    (isClosed_le continuous_const (continuous_coord D a)).inter
      (isClosed_le (continuous_coord D a) continuous_const)
  exact fun f hf => body_subset D hc hcl (fun x => ⟨val_nonneg D a x, val_le_one D a x⟩) hf

theorem stageEffects_isEffectOn : ∀ e ∈ stageEffects D, IsEffectOn (body D) e := by
  rintro _ ⟨a, rfl⟩
  exact coord_isEffectOn D a

/-- The unit of any stage reads one at every preparation of the completion. No premise. -/
theorem val_unit (i : D.ι) (x : Prep D) : val D ⟨i, (D.stage i).unit⟩ x = 1 := by
  unfold val
  rw [(D.map _).unit_map]
  exact (D.stage _).unit_eq _

/-- The unit coordinates equal one on the completion body. No premise. -/
theorem coord_unit_eq_one (i : D.ι) : ∀ f ∈ body D, coord D ⟨i, (D.stage i).unit⟩ f = 1 := by
  have hc : Convex ℝ {f : CSpace D | coord D ⟨i, (D.stage i).unit⟩ f = 1} := by
    intro f hf g hg s t hs ht hst
    simp only [Set.mem_setOf_eq] at hf hg ⊢
    rw [Convex.combo_affine_apply hst, hf, hg, smul_eq_mul, smul_eq_mul, mul_one, mul_one, hst]
  have hcl : IsClosed {f : CSpace D | coord D ⟨i, (D.stage i).unit⟩ f = 1} :=
    isClosed_eq (continuous_coord D _) continuous_const
  exact fun f hf => body_subset D hc hcl (fun x => val_unit D i x) hf

/-! ### §C — the sharp seed on the completion, under SC∞ -/

/-- Under SC∞ the completion value of a stage effect at a preparation of the same stage is the
stage's own table entry. -/
theorem val_same_stage (hSC : SCInf D) (i : D.ι) (e : (D.stage i).E) (x : (D.stage i).P) :
    val D ⟨i, e⟩ ⟨i, x⟩ = (D.stage i).p e x := by
  rw [val_eq_at D hSC ⟨i, e⟩ ⟨i, x⟩ (le_refl i) (le_refl i)]
  exact hSC i i (le_refl i) e x

/-- **The sharp seed survives the completion under SC∞.** A stage effect certain at one stage
preparation and zero at another is a sharp seed on the completion body. -/
theorem sharpSeed_completion (hSC : SCInf D) {i : D.ι} {e : (D.stage i).E}
    {x1 x0 : (D.stage i).P} (h1 : (D.stage i).p e x1 = 1) (h0 : (D.stage i).p e x0 = 0) :
    SharpSeed (body D) (coord D ⟨i, e⟩) :=
  ⟨coord_isEffectOn D _,
    ⟨prepVec D ⟨i, x1⟩, prepVec_mem_body D _, by rw [coord_prepVec, val_same_stage D hSC, h1]⟩,
    ⟨prepVec D ⟨i, x0⟩, prepVec_mem_body D _, by rw [coord_prepVec, val_same_stage D hSC, h0]⟩⟩

/-- The certain state of the completion seed is a boundary state of the completion body. -/
theorem boundary_completion (hSC : SCInf D) {i : D.ι} {e : (D.stage i).E}
    {x1 x0 : (D.stage i).P} (h1 : (D.stage i).p e x1 = 1) (h0 : (D.stage i).p e x0 = 0) :
    IsBoundaryState (body D) (prepVec D ⟨i, x1⟩) :=
  sharpSeed_certain_isBoundaryState (sharpSeed_completion D hSC h1 h0) (prepVec_mem_body D _)
    (by rw [coord_prepVec, val_same_stage D hSC, h1])

/-! ### §D — the binary visible scope, ELEM-bin -/

/-- **ELEM-bin**: every stage carries a binary visible test, and the forward maps carry the
visible outcomes to the visible outcomes. -/
structure ElemBinary where
  v0 : ∀ i, (D.stage i).E
  v1 : ∀ i, (D.stage i).E
  test : ∀ i x, (D.stage i).p (v0 i) x + (D.stage i).p (v1 i) x = 1
  carried0 : ∀ {i j : D.ι} (h : i ≤ j), (D.map h).onE (v0 i) = v0 j
  carried1 : ∀ {i j : D.ι} (h : i ≤ j), (D.map h).onE (v1 i) = v1 j

variable {D}

theorem val_visible_sum (E : ElemBinary D) (i : D.ι) (x : Prep D) :
    val D ⟨i, E.v0 i⟩ x + val D ⟨i, E.v1 i⟩ x = 1 := by
  unfold val
  rw [E.carried0, E.carried1]
  exact E.test _ _

/-- **The visible test is a test on the whole completion body** under ELEM-bin. No SC∞. -/
theorem visible_test_completion (E : ElemBinary D) (i : D.ι) :
    ∀ f ∈ body D, coord D ⟨i, E.v0 i⟩ f + coord D ⟨i, E.v1 i⟩ f = 1 := by
  have hc : Convex ℝ {f : CSpace D | coord D ⟨i, E.v0 i⟩ f + coord D ⟨i, E.v1 i⟩ f = 1} := by
    intro f hf g hg s t hs ht hst
    simp only [Set.mem_setOf_eq] at hf hg ⊢
    rw [Convex.combo_affine_apply hst, Convex.combo_affine_apply hst]
    simp only [smul_eq_mul]
    linear_combination s * hf + t * hg + hst
  have hcl : IsClosed {f : CSpace D | coord D ⟨i, E.v0 i⟩ f + coord D ⟨i, E.v1 i⟩ f = 1} :=
    isClosed_eq ((continuous_coord D _).add (continuous_coord D _)) continuous_const
  exact fun f hf => body_subset D hc hcl (fun x => val_visible_sum E i x) hf

/-- With SC∞ and ELEM-bin, a sharp visible pair at some stage is perfectly distinguishable on the
completion body by the two visible coordinates. -/
theorem perfectlyDistinguishable_visible (hSC : SCInf D) (E : ElemBinary D) {i : D.ι}
    {x0 x1 : (D.stage i).P} (h0 : (D.stage i).p (E.v0 i) x0 = 1)
    (h1 : (D.stage i).p (E.v1 i) x1 = 1) :
    PerfectlyDistinguishable (body D) ![prepVec D ⟨i, x0⟩, prepVec D ⟨i, x1⟩]
      ![coord D ⟨i, E.v0 i⟩, coord D ⟨i, E.v1 i⟩] := by
  refine ⟨?_, ?_, ?_, ?_⟩
  · intro k
    fin_cases k <;> exact prepVec_mem_body D _
  · intro k
    fin_cases k <;> exact coord_isEffectOn D _
  · intro y hy
    rw [Fin.sum_univ_two]
    exact visible_test_completion E i y hy
  · intro k
    fin_cases k
    · show coord D ⟨i, E.v0 i⟩ (prepVec D ⟨i, x0⟩) = 1
      rw [coord_prepVec, val_same_stage D hSC, h0]
    · show coord D ⟨i, E.v1 i⟩ (prepVec D ⟨i, x1⟩) = 1
      rw [coord_prepVec, val_same_stage D hSC, h1]

/-! ### §E — finite rank and the chart of the affine span -/

variable {V : Type} [NormedAddCommGroup V] [NormedSpace ℝ V]

/-- **Finite rank**: the affine span of the body is finite-dimensional. -/
def FiniteRank (Ω : Set V) : Prop :=
  FiniteDimensional ℝ (affineSpan ℝ Ω).direction

/-- A nonempty body of finite rank admits an injective affine chart `w ↦ L w + p0` from
coordinates whose range is its affine span. -/
theorem exists_chart_of_finiteRank {Ω : Set V} (hne : Ω.Nonempty) (hfr : FiniteRank Ω) :
    ∃ (d : ℕ) (L : (Fin d → ℝ) →ₗ[ℝ] V) (p0 : V), LinearMap.ker L = ⊥ ∧
      ∀ x, x ∈ affineSpan ℝ Ω ↔ x ∈ Set.range (chart L p0) := by
  haveI : FiniteDimensional ℝ (affineSpan ℝ Ω).direction := hfr
  obtain ⟨p0, hp0⟩ := hne
  let b := Module.finBasis ℝ (affineSpan ℝ Ω).direction
  let L : (Fin (Module.finrank ℝ (affineSpan ℝ Ω).direction) → ℝ) →ₗ[ℝ] V :=
    (affineSpan ℝ Ω).direction.subtype ∘ₗ b.equivFun.symm.toLinearMap
  have hp0s : p0 ∈ affineSpan ℝ Ω := subset_affineSpan ℝ Ω hp0
  refine ⟨Module.finrank ℝ (affineSpan ℝ Ω).direction, L, p0, ?_, fun x => ?_⟩
  · rw [LinearMap.ker_eq_bot]
    exact Subtype.val_injective.comp b.equivFun.symm.injective
  · rw [← AffineSubspace.vsub_right_mem_direction_iff_mem hp0s x, vsub_eq_sub]
    constructor
    · intro hx
      refine ⟨b.equivFun ⟨x - p0, hx⟩, ?_⟩
      rw [chart_apply]
      show (b.equivFun.symm (b.equivFun ⟨x - p0, hx⟩) : V) + p0 = x
      rw [LinearEquiv.symm_apply_apply]
      simp
    · rintro ⟨w, rfl⟩
      rw [chart_apply, add_sub_cancel_right]
      exact (b.equivFun.symm w).2

/-! ### §F — controls -/

/-- A two-stage system that violates SC∞: the effect `false` is certain at stage `false` and reads
`1/2` at stage `true`. -/
noncomputable def badStage (b : Bool) : FiniteStage where
  P := Unit
  E := Bool
  p e _ := if e then 1 else if b then 1 / 2 else 1
  unit := true
  nonneg e _ := by split_ifs <;> norm_num
  le_one e _ := by split_ifs <;> norm_num
  unit_eq _ := rfl

/-- The directed system of the two bad stages. -/
noncomputable def badD : DirectedStages where
  ι := Bool
  directed i j := ⟨true, le_top, le_top⟩
  stage := badStage
  map _ := ⟨id, id, rfl⟩
  comp_E _ _ _ := rfl
  comp_P _ _ _ := rfl

theorem not_scInf_bad : ¬ SCInf badD := by
  intro h
  have := h false true (Bool.false_le true) false ()
  change (if false then (1 : ℝ) else if true then 1 / 2 else 1) =
    (if false then (1 : ℝ) else if false then 1 / 2 else 1) at this
  norm_num at this

/-- **Without SC∞ the completion value is not well defined**: the effect `false` of stage
`false`, at the preparation of stage `false`, reads `1` at the common upper stage `false` and
`1/2` at the common upper stage `true`. -/
theorem bad_values_differ :
    (badD.stage false).p ((badD.map (le_refl false)).onE false)
        ((badD.map (le_refl false)).onP ()) = 1 ∧
      (badD.stage true).p ((badD.map (Bool.false_le true)).onE false)
        ((badD.map (Bool.false_le true)).onP ()) = 1 / 2 := by
  constructor
  · show (if false then (1 : ℝ) else if false then 1 / 2 else 1) = 1
    norm_num
  · show (if false then (1 : ℝ) else if true then 1 / 2 else 1) = 1 / 2
    norm_num

/-- The classical bit as a finite stage: preparations `Bool`, effects the unit and the two
outcomes. -/
noncomputable def bitStage : FiniteStage where
  P := Bool
  E := Option Bool
  p e x := match e with
    | none => 1
    | some b => if b = x then 1 else 0
  unit := none
  nonneg e x := by cases e <;> simp only <;> (try split_ifs) <;> norm_num
  le_one e x := by cases e <;> simp only <;> (try split_ifs) <;> norm_num
  unit_eq _ := rfl

theorem bitStage_test (x : Bool) :
    bitStage.p (some false) x + bitStage.p (some true) x = 1 := by
  cases x <;> simp [bitStage]

theorem bitStage_one : bitStage.p (some false) false = 1 := by simp [bitStage]

theorem bitStage_zero : bitStage.p (some false) true = 0 := by simp [bitStage]

/-- The constant classical-bit tower. -/
noncomputable def bitTower : DirectedStages where
  ι := ℕ
  directed i j := ⟨max i j, le_max_left i j, le_max_right i j⟩
  stage _ := bitStage
  map _ := ⟨id, id, rfl⟩
  comp_E _ _ _ := rfl
  comp_P _ _ _ := rfl

theorem bitTower_scInf : SCInf bitTower := fun _ _ _ _ _ => rfl

/-- The visible test of the bit tower. -/
noncomputable def bitTower_elem : ElemBinary bitTower where
  v0 _ := some false
  v1 _ := some true
  test _ x := bitStage_test x
  carried0 _ := rfl
  carried1 _ := rfl

/-- On the bit tower every premise holds and the visible outcome is a sharp seed on the
completion body. -/
theorem bitTower_sharpSeed :
    SharpSeed (body bitTower) (coord bitTower ⟨(0 : ℕ), some false⟩) :=
  sharpSeed_completion bitTower bitTower_scInf (i := (0 : ℕ)) (e := some false) (x1 := false)
    (x0 := true) bitStage_one bitStage_zero

/-! ### §G — the verdict -/

/-- **Round CMP-1.** The completion interface: every stage effect is an effect on the completion
body with no premise; under SC∞ a sharp stage pair is a sharp seed on the completion; under
ELEM-bin the visible test is a test on the completion; a body of finite rank has an affine chart of
its span; without SC∞ the completion value is not well defined; and the premises are jointly
satisfiable. -/
theorem cmp1_core :
    (∀ D : DirectedStages, ∀ e ∈ stageEffects D, IsEffectOn (body D) e) ∧
    (∀ D : DirectedStages, SCInf D → ∀ (i : D.ι) (e : (D.stage i).E) (x1 x0 : (D.stage i).P),
      (D.stage i).p e x1 = 1 → (D.stage i).p e x0 = 0 → SharpSeed (body D) (coord D ⟨i, e⟩)) ∧
    (∀ (D : DirectedStages) (E : ElemBinary D) (i : D.ι),
      ∀ f ∈ body D, coord D ⟨i, E.v0 i⟩ f + coord D ⟨i, E.v1 i⟩ f = 1) ∧
    (∀ (Ω : Set V), Ω.Nonempty → FiniteRank Ω →
      ∃ (d : ℕ) (L : (Fin d → ℝ) →ₗ[ℝ] V) (p0 : V), LinearMap.ker L = ⊥ ∧
        ∀ x, x ∈ affineSpan ℝ Ω ↔ x ∈ Set.range (chart L p0)) ∧
    ¬ SCInf badD ∧
    (SCInf bitTower ∧ SharpSeed (body bitTower) (coord bitTower ⟨(0 : ℕ), some false⟩)) :=
  ⟨fun D => stageEffects_isEffectOn D,
    fun D hSC _ _ _ _ h1 h0 => sharpSeed_completion D hSC h1 h0,
    fun _ E i => visible_test_completion E i,
    fun _ hne hfr => exists_chart_of_finiteRank hne hfr,
    not_scInf_bad,
    ⟨bitTower_scInf, bitTower_sharpSeed⟩⟩

end StageCompletion
end OIBridge

#print axioms OIBridge.StageCompletion.val_eq_at
#print axioms OIBridge.StageCompletion.coord_isEffectOn
#print axioms OIBridge.StageCompletion.stageEffects_isEffectOn
#print axioms OIBridge.StageCompletion.coord_unit_eq_one
#print axioms OIBridge.StageCompletion.val_same_stage
#print axioms OIBridge.StageCompletion.sharpSeed_completion
#print axioms OIBridge.StageCompletion.boundary_completion
#print axioms OIBridge.StageCompletion.visible_test_completion
#print axioms OIBridge.StageCompletion.perfectlyDistinguishable_visible
#print axioms OIBridge.StageCompletion.exists_chart_of_finiteRank
#print axioms OIBridge.StageCompletion.not_scInf_bad
#print axioms OIBridge.StageCompletion.bad_values_differ
#print axioms OIBridge.StageCompletion.bitTower_scInf
#print axioms OIBridge.StageCompletion.bitTower_sharpSeed
#print axioms OIBridge.StageCompletion.cmp1_core
