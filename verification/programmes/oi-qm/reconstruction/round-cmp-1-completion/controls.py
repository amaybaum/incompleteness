#!/usr/bin/env python3
"""controls.py -- round CMP-1's own contracts, FROZEN with the preregistration beside it.

Imports nothing from the repository and changes nothing. Reads D and the commit under check through git, and embeds
every frozen text it compares against.

  controls.py check <commit> [--freeze F]   the execution at <commit> against D (and, with F, the preregistration
                                            unchanged from F, and F = D plus the preregistration alone)
  controls.py --self-test                   the frozen surfaces against the reference module; mutation controls that
                                            must fail with their named codes

Checks (each prints PASS or FAIL with its code):
  P   paths       delta(D, commit) is exactly the governed execution paths plus the record directory
  N1  decls       the module declares exactly the frozen declarations, in order, with their kinds
  N2  statements  every theorem statement (signature up to `:=`) is the frozen text; every definition, abbreviation
                  and structure is the frozen text whole; the preamble and every context line (`variable`, `open`,
                  `namespace`, `section`, `end`, `attribute`) is the frozen text, in order -- a proof may change, a
                  statement, definition or binder context may not
  N3  hygiene     no sorry, admit, axiom declaration or native_decide; every frozen `#print axioms` line present
  S1  no ELEM     no declaration is named bare `ELEM` (or `Elem`, `elem`)
  S2  ELEM-bin    `BinaryVisible` is a structure, the formal notion this round provides; its docstring and the module
                  header state that it is necessary, not sufficient, for the elementary-system scope; the header
                  states that the visible-factor requirement is not formalized here and that the name ELEM is
                  reserved
  S3  ELEM-vis    no declaration formalizes the visible-factor requirement (`ElemVis`, `VisibleFactor`, `NoAncilla`,
                  ...)
  S4  SC∞         `SCInf` is a named predicate (`def`), `DirectedStages` carries no consistency field, and no theorem
                  concludes `SCInf`, `BinaryVisible` or `FiniteRank` without it among its hypotheses, except the
                  named controls on `bitTower` and `badD`
  S5  scope       no declaration name, theorem conclusion or header claim of a ball, ellipsoid, transitivity, drive,
                  dimension or V4′; the header disclaimer is present
  I   imports     OIBridge.lean is D's with exactly the frozen import line after `import OIBridge.OrbitNormalization`
  C   census      the census is D's with exactly the frozen family inserted after the OG-1 family
  F   freeze      (with --freeze) the preregistration at the commit equals F's, and delta(D, F) is the preregistration
"""
import hashlib, io, json, re, subprocess, sys

D = 'f7f5c3b0c621cc3e4b57e3709d11d9d580c81149'
RDIR = 'verification/programmes/oi-qm/reconstruction/round-cmp-1-completion/'
PREREG = RDIR + 'preregistration.md'
MOD = 'verification/lean-mathlib/OIBridge/StageCompletion.lean'
IMPORTS = 'verification/lean-mathlib/OIBridge.lean'
CENSUS = 'verification/lean-manuscript-census.json'
GOVERNED = {MOD: 'A', IMPORTS: 'M', CENSUS: 'M'}
RECORD_FILES = {RDIR + 'preregistration.md', RDIR + 'controls.py', RDIR + 'result.md'}
MOD_REFERENCE_BLOB = '4df7bc6da9d6294128a99913eab7f8cf80d17202'
ANCHOR_IMPORT = 'import OIBridge.OrbitNormalization\n'
NEW_IMPORT = 'import OIBridge.StageCompletion\n'
OG1_FAMILY_PREFIX = 'conditional orbit-generation infrastructure'
CENSUS_FAMILY = json.loads(r'''{
 "name": "the stage completion — directed finite stages, stage consistency (SC∞), the completion body and its stage-effect interface, the binary-visible condition (ELEM-bin) and the affine-span chart of a body of finite rank (round CMP-1, reconstruction)",
 "modules": [
  "StageCompletion"
 ],
 "status": "kernel-only",
 "manuscript": [],
 "note": "Round CMP-1, a native round under AGENTS.md §A.39, executed under the frozen control plane programmes/oi-qm/reconstruction/round-cmp-1-completion/preregistration.md. The kernel layer defines directed systems of finite stages, stage consistency SC∞ as a named predicate, the completion body as the closed convex hull of the preparation vectors in ℓ^∞ over the stage effects, the stage-effect family, the binary-visible condition BinaryVisible (ELEM-bin) and finite rank; it proves with no premise that every stage effect is an effect on the completion body (stageEffects_isEffectOn), under SC∞ that the completion value is well defined (val_eq_at) and that a sharp stage pair is a sharp seed on the completion (sharpSeed_completion), under BinaryVisible that the visible test is a test on the completion (visible_test_completion), and that a nonempty body of finite rank has an injective affine chart of its span (exists_chart_of_finiteRank); controls show SC∞ failing with ill-defined values and all premises holding on the constant bit tower. Carried by no manuscript. Nothing here derives SC∞, BinaryVisible or finite rank from an OI construction. BinaryVisible is necessary, not sufficient, for the elementary-system scope: the visible-factor requirement is a deferred operational requirement, not formalized here, and the full scope is not defined by this round."
}''')
DECLS = json.loads(r'''[
 [
  "structure",
  "StageMap"
 ],
 [
  "def",
  "StageMap.Consistent"
 ],
 [
  "structure",
  "DirectedStages"
 ],
 [
  "def",
  "SCInf"
 ],
 [
  "abbrev",
  "Label"
 ],
 [
  "abbrev",
  "Prep"
 ],
 [
  "noncomputable def",
  "ub"
 ],
 [
  "theorem",
  "le_ub_left"
 ],
 [
  "theorem",
  "le_ub_right"
 ],
 [
  "noncomputable def",
  "val"
 ],
 [
  "theorem",
  "val_nonneg"
 ],
 [
  "theorem",
  "val_le_one"
 ],
 [
  "theorem",
  "read_later"
 ],
 [
  "theorem",
  "val_eq_at"
 ],
 [
  "abbrev",
  "CSpace"
 ],
 [
  "theorem",
  "norm_val_le_one"
 ],
 [
  "noncomputable def",
  "prepVec"
 ],
 [
  "def",
  "body"
 ],
 [
  "noncomputable def",
  "evalLin"
 ],
 [
  "noncomputable def",
  "evalCLM"
 ],
 [
  "noncomputable def",
  "coord"
 ],
 [
  "theorem",
  "coord_apply"
 ],
 [
  "theorem",
  "coord_prepVec"
 ],
 [
  "theorem",
  "continuous_coord"
 ],
 [
  "theorem",
  "prepVec_mem_body"
 ],
 [
  "theorem",
  "body_subset"
 ],
 [
  "def",
  "stageEffects"
 ],
 [
  "theorem",
  "coord_isEffectOn"
 ],
 [
  "theorem",
  "stageEffects_isEffectOn"
 ],
 [
  "theorem",
  "val_unit"
 ],
 [
  "theorem",
  "coord_unit_eq_one"
 ],
 [
  "theorem",
  "val_same_stage"
 ],
 [
  "theorem",
  "sharpSeed_completion"
 ],
 [
  "theorem",
  "boundary_completion"
 ],
 [
  "structure",
  "BinaryVisible"
 ],
 [
  "theorem",
  "val_visible_sum"
 ],
 [
  "theorem",
  "visible_test_completion"
 ],
 [
  "theorem",
  "perfectlyDistinguishable_visible"
 ],
 [
  "def",
  "FiniteRank"
 ],
 [
  "theorem",
  "exists_chart_of_finiteRank"
 ],
 [
  "noncomputable def",
  "badStage"
 ],
 [
  "noncomputable def",
  "badD"
 ],
 [
  "theorem",
  "not_scInf_bad"
 ],
 [
  "theorem",
  "bad_values_differ"
 ],
 [
  "noncomputable def",
  "bitStage"
 ],
 [
  "theorem",
  "bitStage_test"
 ],
 [
  "theorem",
  "bitStage_one"
 ],
 [
  "theorem",
  "bitStage_zero"
 ],
 [
  "noncomputable def",
  "bitTower"
 ],
 [
  "theorem",
  "bitTower_scInf"
 ],
 [
  "noncomputable def",
  "bitTower_binaryVisible"
 ],
 [
  "theorem",
  "bitTower_sharpSeed"
 ],
 [
  "theorem",
  "cmp1_core"
 ]
]''')
TEXTS = json.loads(r'''{
 "StageMap": "structure StageMap (S T : FiniteStage) where\n  onE : S.E → T.E\n  onP : S.P → T.P\n  unit_map : onE S.unit = T.unit",
 "StageMap.Consistent": "def StageMap.Consistent {S T : FiniteStage} (f : StageMap S T) : Prop :=\n  ∀ e x, T.p (f.onE e) (f.onP x) = S.p e x",
 "DirectedStages": "structure DirectedStages where\n  ι : Type\n  [pre : Preorder ι]\n  [ne : Nonempty ι]\n  directed : ∀ i j : ι, ∃ k, i ≤ k ∧ j ≤ k\n  stage : ι → FiniteStage\n  map : ∀ {i j : ι}, i ≤ j → StageMap (stage i) (stage j)\n  comp_E : ∀ {i j k : ι} (hij : i ≤ j) (hjk : j ≤ k) (e : (stage i).E),\n    (map hjk).onE ((map hij).onE e) = (map (hij.trans hjk)).onE e\n  comp_P : ∀ {i j k : ι} (hij : i ≤ j) (hjk : j ≤ k) (x : (stage i).P),\n    (map hjk).onP ((map hij).onP x) = (map (hij.trans hjk)).onP x",
 "SCInf": "def SCInf (D : DirectedStages) : Prop :=\n  ∀ (i j : D.ι) (h : i ≤ j), (D.map h).Consistent",
 "Label": "abbrev Label : Type := Σ i : D.ι, (D.stage i).E",
 "Prep": "abbrev Prep : Type := Σ i : D.ι, (D.stage i).P",
 "ub": "noncomputable def ub (i j : D.ι) : D.ι := Classical.choose (D.directed i j)",
 "le_ub_left": "theorem le_ub_left (i j : D.ι) : i ≤ ub D i j",
 "le_ub_right": "theorem le_ub_right (i j : D.ι) : j ≤ ub D i j",
 "val": "noncomputable def val (a : Label D) (x : Prep D) : ℝ :=\n  (D.stage (ub D x.1 a.1)).p ((D.map (le_ub_right D x.1 a.1)).onE a.2)\n    ((D.map (le_ub_left D x.1 a.1)).onP x.2)",
 "val_nonneg": "theorem val_nonneg (a : Label D) (x : Prep D) : 0 ≤ val D a x",
 "val_le_one": "theorem val_le_one (a : Label D) (x : Prep D) : val D a x ≤ 1",
 "read_later": "theorem read_later (hSC : SCInf D) {i j k n : D.ι} (hi : i ≤ k) (hj : j ≤ k) (hk : k ≤ n)\n    (e : (D.stage j).E) (x : (D.stage i).P) :\n    (D.stage k).p ((D.map hj).onE e) ((D.map hi).onP x) =\n      (D.stage n).p ((D.map (hj.trans hk)).onE e) ((D.map (hi.trans hk)).onP x)",
 "val_eq_at": "theorem val_eq_at (hSC : SCInf D) (a : Label D) (x : Prep D) {k : D.ι} (hx : x.1 ≤ k)\n    (ha : a.1 ≤ k) :\n    val D a x = (D.stage k).p ((D.map ha).onE a.2) ((D.map hx).onP x.2)",
 "CSpace": "abbrev CSpace : Type := lp (fun _ : Label D => ℝ) ∞",
 "norm_val_le_one": "theorem norm_val_le_one (a : Label D) (x : Prep D) : ‖val D a x‖ ≤ 1",
 "prepVec": "noncomputable def prepVec (x : Prep D) : CSpace D :=\n  ⟨fun a => val D a x, memℓp_infty ⟨1, by\n    rintro _ ⟨a, rfl⟩\n    exact norm_val_le_one D a x⟩⟩",
 "body": "def body : Set (CSpace D) :=\n  closure (convexHull ℝ (Set.range (prepVec D)))",
 "evalLin": "noncomputable def evalLin (a : Label D) : CSpace D →ₗ[ℝ] ℝ where\n  toFun f := f a\n  map_add' f g := by rw [lp.coeFn_add]; rfl\n  map_smul' c f := by rw [lp.coeFn_smul]; rfl",
 "evalCLM": "noncomputable def evalCLM (a : Label D) : CSpace D →L[ℝ] ℝ :=\n  (evalLin D a).mkContinuous 1 fun f => by\n    rw [one_mul]\n    exact lp.norm_apply_le_norm ENNReal.top_ne_zero f a",
 "coord": "noncomputable def coord (a : Label D) : CSpace D →ᵃ[ℝ] ℝ :=\n  (evalLin D a).toAffineMap",
 "coord_apply": "theorem coord_apply (a : Label D) (f : CSpace D) : coord D a f = f a",
 "coord_prepVec": "theorem coord_prepVec (a : Label D) (x : Prep D) : coord D a (prepVec D x) = val D a x",
 "continuous_coord": "theorem continuous_coord (a : Label D) : Continuous (coord D a)",
 "prepVec_mem_body": "theorem prepVec_mem_body (x : Prep D) : prepVec D x ∈ body D",
 "body_subset": "theorem body_subset {S : Set (CSpace D)} (hc : Convex ℝ S) (hcl : IsClosed S)\n    (hp : ∀ x, prepVec D x ∈ S) : body D ⊆ S",
 "stageEffects": "def stageEffects : Set (CSpace D →ᵃ[ℝ] ℝ) :=\n  Set.range (coord D)",
 "coord_isEffectOn": "theorem coord_isEffectOn (a : Label D) : IsEffectOn (body D) (coord D a)",
 "stageEffects_isEffectOn": "theorem stageEffects_isEffectOn : ∀ e ∈ stageEffects D, IsEffectOn (body D) e",
 "val_unit": "theorem val_unit (i : D.ι) (x : Prep D) : val D ⟨i, (D.stage i).unit⟩ x = 1",
 "coord_unit_eq_one": "theorem coord_unit_eq_one (i : D.ι) : ∀ f ∈ body D, coord D ⟨i, (D.stage i).unit⟩ f = 1",
 "val_same_stage": "theorem val_same_stage (hSC : SCInf D) (i : D.ι) (e : (D.stage i).E) (x : (D.stage i).P) :\n    val D ⟨i, e⟩ ⟨i, x⟩ = (D.stage i).p e x",
 "sharpSeed_completion": "theorem sharpSeed_completion (hSC : SCInf D) {i : D.ι} {e : (D.stage i).E}\n    {x1 x0 : (D.stage i).P} (h1 : (D.stage i).p e x1 = 1) (h0 : (D.stage i).p e x0 = 0) :\n    SharpSeed (body D) (coord D ⟨i, e⟩)",
 "boundary_completion": "theorem boundary_completion (hSC : SCInf D) {i : D.ι} {e : (D.stage i).E}\n    {x1 x0 : (D.stage i).P} (h1 : (D.stage i).p e x1 = 1) (h0 : (D.stage i).p e x0 = 0) :\n    IsBoundaryState (body D) (prepVec D ⟨i, x1⟩)",
 "BinaryVisible": "structure BinaryVisible where\n  v0 : ∀ i, (D.stage i).E\n  v1 : ∀ i, (D.stage i).E\n  test : ∀ i x, (D.stage i).p (v0 i) x + (D.stage i).p (v1 i) x = 1\n  carried0 : ∀ {i j : D.ι} (h : i ≤ j), (D.map h).onE (v0 i) = v0 j\n  carried1 : ∀ {i j : D.ι} (h : i ≤ j), (D.map h).onE (v1 i) = v1 j",
 "val_visible_sum": "theorem val_visible_sum (E : BinaryVisible D) (i : D.ι) (x : Prep D) :\n    val D ⟨i, E.v0 i⟩ x + val D ⟨i, E.v1 i⟩ x = 1",
 "visible_test_completion": "theorem visible_test_completion (E : BinaryVisible D) (i : D.ι) :\n    ∀ f ∈ body D, coord D ⟨i, E.v0 i⟩ f + coord D ⟨i, E.v1 i⟩ f = 1",
 "perfectlyDistinguishable_visible": "theorem perfectlyDistinguishable_visible (hSC : SCInf D) (E : BinaryVisible D) {i : D.ι}\n    {x0 x1 : (D.stage i).P} (h0 : (D.stage i).p (E.v0 i) x0 = 1)\n    (h1 : (D.stage i).p (E.v1 i) x1 = 1) :\n    PerfectlyDistinguishable (body D) ![prepVec D ⟨i, x0⟩, prepVec D ⟨i, x1⟩]\n      ![coord D ⟨i, E.v0 i⟩, coord D ⟨i, E.v1 i⟩]",
 "FiniteRank": "def FiniteRank (Ω : Set V) : Prop :=\n  FiniteDimensional ℝ (affineSpan ℝ Ω).direction",
 "exists_chart_of_finiteRank": "theorem exists_chart_of_finiteRank {Ω : Set V} (hne : Ω.Nonempty) (hfr : FiniteRank Ω) :\n    ∃ (d : ℕ) (L : (Fin d → ℝ) →ₗ[ℝ] V) (p0 : V), LinearMap.ker L = ⊥ ∧\n      ∀ x, x ∈ affineSpan ℝ Ω ↔ x ∈ Set.range (chart L p0)",
 "badStage": "noncomputable def badStage (b : Bool) : FiniteStage where\n  P := Unit\n  E := Bool\n  p e _ := if e then 1 else if b then 1 / 2 else 1\n  unit := true\n  nonneg e _ := by split_ifs <;> norm_num\n  le_one e _ := by split_ifs <;> norm_num\n  unit_eq _ := rfl",
 "badD": "noncomputable def badD : DirectedStages where\n  ι := Bool\n  directed i j := ⟨true, le_top, le_top⟩\n  stage := badStage\n  map _ := ⟨id, id, rfl⟩\n  comp_E _ _ _ := rfl\n  comp_P _ _ _ := rfl",
 "not_scInf_bad": "theorem not_scInf_bad : ¬ SCInf badD",
 "bad_values_differ": "theorem bad_values_differ :\n    (badD.stage false).p ((badD.map (le_refl false)).onE false)\n        ((badD.map (le_refl false)).onP ()) = 1 ∧\n      (badD.stage true).p ((badD.map (Bool.false_le true)).onE false)\n        ((badD.map (Bool.false_le true)).onP ()) = 1 / 2",
 "bitStage": "noncomputable def bitStage : FiniteStage where\n  P := Bool\n  E := Option Bool\n  p e x := match e with\n    | none => 1\n    | some b => if b = x then 1 else 0\n  unit := none\n  nonneg e x := by cases e <;> simp only <;> (try split_ifs) <;> norm_num\n  le_one e x := by cases e <;> simp only <;> (try split_ifs) <;> norm_num\n  unit_eq _ := rfl",
 "bitStage_test": "theorem bitStage_test (x : Bool) :\n    bitStage.p (some false) x + bitStage.p (some true) x = 1",
 "bitStage_one": "theorem bitStage_one : bitStage.p (some false) false = 1",
 "bitStage_zero": "theorem bitStage_zero : bitStage.p (some false) true = 0",
 "bitTower": "noncomputable def bitTower : DirectedStages where\n  ι := ℕ\n  directed i j := ⟨max i j, le_max_left i j, le_max_right i j⟩\n  stage _ := bitStage\n  map _ := ⟨id, id, rfl⟩\n  comp_E _ _ _ := rfl\n  comp_P _ _ _ := rfl",
 "bitTower_scInf": "theorem bitTower_scInf : SCInf bitTower",
 "bitTower_binaryVisible": "noncomputable def bitTower_binaryVisible : BinaryVisible bitTower where\n  v0 _ := some false\n  v1 _ := some true\n  test _ x := bitStage_test x\n  carried0 _ := rfl\n  carried1 _ := rfl",
 "bitTower_sharpSeed": "theorem bitTower_sharpSeed :\n    SharpSeed (body bitTower) (coord bitTower ⟨(0 : ℕ), some false⟩)",
 "cmp1_core": "theorem cmp1_core :\n    (∀ D : DirectedStages, ∀ e ∈ stageEffects D, IsEffectOn (body D) e) ∧\n    (∀ D : DirectedStages, SCInf D → ∀ (i : D.ι) (e : (D.stage i).E) (x1 x0 : (D.stage i).P),\n      (D.stage i).p e x1 = 1 → (D.stage i).p e x0 = 0 → SharpSeed (body D) (coord D ⟨i, e⟩)) ∧\n    (∀ (D : DirectedStages) (E : BinaryVisible D) (i : D.ι),\n      ∀ f ∈ body D, coord D ⟨i, E.v0 i⟩ f + coord D ⟨i, E.v1 i⟩ f = 1) ∧\n    (∀ (Ω : Set V), Ω.Nonempty → FiniteRank Ω →\n      ∃ (d : ℕ) (L : (Fin d → ℝ) →ₗ[ℝ] V) (p0 : V), LinearMap.ker L = ⊥ ∧\n        ∀ x, x ∈ affineSpan ℝ Ω ↔ x ∈ Set.range (chart L p0)) ∧\n    ¬ SCInf badD ∧\n    (SCInf bitTower ∧ SharpSeed (body bitTower) (coord bitTower ⟨(0 : ℕ), some false⟩))"
}''')
PRINTS = json.loads(r'''[
 "OIBridge.StageCompletion.val_eq_at",
 "OIBridge.StageCompletion.coord_isEffectOn",
 "OIBridge.StageCompletion.stageEffects_isEffectOn",
 "OIBridge.StageCompletion.coord_unit_eq_one",
 "OIBridge.StageCompletion.val_same_stage",
 "OIBridge.StageCompletion.sharpSeed_completion",
 "OIBridge.StageCompletion.boundary_completion",
 "OIBridge.StageCompletion.visible_test_completion",
 "OIBridge.StageCompletion.perfectlyDistinguishable_visible",
 "OIBridge.StageCompletion.exists_chart_of_finiteRank",
 "OIBridge.StageCompletion.not_scInf_bad",
 "OIBridge.StageCompletion.bad_values_differ",
 "OIBridge.StageCompletion.bitTower_scInf",
 "OIBridge.StageCompletion.bitTower_sharpSeed",
 "OIBridge.StageCompletion.cmp1_core"
]''')
PREAMBLE = json.loads(r'''"import OIBridge.OrbitNormalization\nimport Mathlib.Analysis.Normed.Lp.lpSpace\n\nnamespace OIBridge\nnamespace StageCompletion\n\nopen Set KInfFoundations OrbitGeneration OrbitNormalization\nopen scoped ENNReal\n"''')
CONTEXT = json.loads(r'''[
 "namespace OIBridge",
 "namespace StageCompletion",
 "open Set KInfFoundations OrbitGeneration OrbitNormalization",
 "open scoped ENNReal",
 "attribute [instance] DirectedStages.pre DirectedStages.ne",
 "variable (D : DirectedStages)",
 "variable {D}",
 "variable {V : Type} [NormedAddCommGroup V] [NormedSpace ℝ V]",
 "end StageCompletion",
 "end OIBridge"
]''')

DECL = re.compile(r'^(theorem|lemma|def|noncomputable def|abbrev|noncomputable abbrev|structure|instance)\s+(\S+)',
                  re.M)
CTX = re.compile(r'^(variable|open|namespace|section|end|attribute|universe|set_option|noncomputable section)\b.*$',
                 re.M)
FAILS, COUNT = [], [0]


def check(code, name, cond):
    COUNT[0] += 1
    print(('  PASS  ' if cond else '  FAIL  ') + code + ' ' + name, flush=True)
    if not cond:
        FAILS.append(code)


def git(*a):
    return subprocess.run(['git'] + list(a), capture_output=True, text=True)


def show(commit, path):
    r = git('show', '%s:%s' % (commit, path))
    return r.stdout if r.returncode == 0 else None


def preamble(text):
    i = text.index('\nimport ') + 1
    j = text.index('\n/-! ### §A')
    return text[i:j]


def context_lines(text):
    return [m.group(0) for m in CTX.finditer(text)]


def decls(text):
    return [(m.group(1), m.group(2)) for m in DECL.finditer(text)]


def decl_texts(text):
    """theorem/lemma: signature up to the first ' :=' ; others: the declaration whole, up to the next doc comment,
    section marker, declaration, '#print', context line or 'end'."""
    out = {}
    ms = list(DECL.finditer(text))
    for k, m in enumerate(ms):
        start = m.start()
        nxt = ms[k + 1].start() if k + 1 < len(ms) else len(text)
        chunk = text[start:nxt]
        for stop in ('\n/--', '\n/-!', '\n#print', '\nend ', '\nvariable', '\nopen ', '\nattribute'):
            j = chunk.find(stop)
            if j != -1:
                chunk = chunk[:j]
        chunk = chunk.rstrip()
        if m.group(1) in ('theorem', 'lemma'):
            j = chunk.find(' :=')
            chunk = chunk[:j] if j != -1 else chunk
        out[m.group(2)] = chunk
    return out


def split_statement(stmt):
    """(binders, conclusion) at the first colon at bracket depth 0 after the name."""
    parts = stmt.split(None, 2)
    i = len(parts[0]) + 1 + len(parts[1])
    depth = 0
    for j in range(i, len(stmt)):
        c = stmt[j]
        if c in '({[⦃':
            depth += 1
        elif c in ')}]⦄':
            depth -= 1
        elif c == ':' and depth == 0 and stmt[j:j + 2] != ':=':
            return stmt[i:j], stmt[j + 1:]
    return stmt[i:], ''


def code_only(text):
    text = re.sub(r'/-.*?-/', ' ', text, flags=re.S)
    return re.sub(r'--[^\n]*', ' ', text)


def header(text):
    return text[:text.index('-/')]


def norm(s):
    return ' '.join(s.split())


VERDICT = 'cmp1_core'
CONTROLS_SC = {'bitTower_scInf', 'not_scInf_bad'}
FORBIDDEN_NAME = re.compile(r'(llipsoid|ransitiv|ball3|finrank|rive|dim3|Dim3|V4)')
FORBIDDEN_CONCL = ('BoundaryTransitive', 'ElementaryDrivability', 'ball3', 'finrank', 'SeedOrbitAvailable')
VIS_NAME = re.compile(r'(ElemVis|ELEM_vis|ElemVisible|VisibleFactor|visibleFactor|NoAncilla|noAncilla|ElemFull|ELEM_full)')
DISCLAIMER = 'nothing defines the full elementary-system scope'


def semantic_checks(mod, texts, kinds, prints, tag):
    names = [n for _, n in decls(mod)]
    check('S1', 'no declaration named bare ELEM' + tag,
          not any(re.fullmatch(r'(ELEM|Elem|elem)', n.split('.')[-1]) for n in names))
    hdr = norm(header(mod))
    i = mod.find('structure BinaryVisible')
    doc = norm(mod[mod.rindex('/--', 0, i):i]) if i != -1 else ''
    check('S2', 'BinaryVisible is the formal notion, necessary, not sufficient; ELEM reserved' + tag,
          kinds.get('BinaryVisible') == 'structure' and 'necessary, not sufficient' in doc
          and 'necessary, not sufficient' in hdr and 'not formalized here' in hdr
          and 'the name ELEM is reserved' in hdr)
    check('S3', 'the visible-factor requirement is not formalized' + tag, not any(VIS_NAME.search(n) for n in names))
    viol = []
    for n, t in texts.items():
        if kinds.get(n) not in ('theorem', 'lemma') or n == VERDICT or n in CONTROLS_SC:
            continue
        bb, cc = split_statement(t)
        for p in ('SCInf', 'BinaryVisible', 'FiniteRank'):
            if p in cc and p not in bb:
                viol.append((n, p))
    vt = texts.get(VERDICT, '')
    check('S4', 'SC∞ is a named predicate and is not sourced%s%s' % (tag, (' %s' % viol[:3]) if viol else ''),
          kinds.get('SCInf') == 'def' and 'Consistent' not in texts.get('DirectedStages', '') and not viol
          and set(re.findall(r'SCInf \w+', vt)) <= {'SCInf D', 'SCInf badD', 'SCInf bitTower'}
          and 'SCInf D →' in vt)
    concl = [split_statement(t)[1] for n, t in texts.items() if kinds.get(n) in ('theorem', 'lemma')]
    check('S5', 'no ball, ellipsoid, transitivity, drive, dimension or V4′ claim' + tag,
          not any(FORBIDDEN_NAME.search(n) for n in names)
          and not any(f in cc for cc in concl for f in FORBIDDEN_CONCL) and DISCLAIMER in hdr)


def module_checks(mod, tag=''):
    if mod is None:
        check('N1', 'module present' + tag, False)
        return
    check('N1', 'the module declares exactly the frozen declarations' + tag, [list(x) for x in decls(mod)] == DECLS)
    check('N2', 'the preamble unchanged' + tag,
          '\n/-! ### §A' in mod and '\nimport ' in mod and preamble(mod) == PREAMBLE)
    check('N2', 'every context line unchanged and in order' + tag, context_lines(mod) == CONTEXT)
    texts = decl_texts(mod)
    bad = sorted(n for n in TEXTS if texts.get(n) != TEXTS[n])
    check('N2', 'every frozen statement and definition unchanged%s%s' % (tag, (' (changed: %s)' % ', '.join(bad[:4]))
                                                                        if bad else ''), not bad)
    c = code_only(mod)
    check('N3', 'no sorry, admit, axiom or native_decide' + tag,
          not re.search(r'\bsorry\b|\badmit\b|^\s*axiom\b|native_decide', c, re.M))
    prints = re.findall(r'^#print axioms (\S+)', mod, re.M)
    check('N3', 'every frozen #print axioms line present' + tag, all(p in prints for p in PRINTS))
    semantic_checks(mod, texts, dict((n, k) for k, n in decls(mod)), prints, tag)


def imports_ok(d_text, e_text):
    return d_text is not None and e_text is not None and d_text.count(ANCHOR_IMPORT) == 1 and \
        e_text == d_text.replace(ANCHOR_IMPORT, ANCHOR_IMPORT + NEW_IMPORT, 1)


def census_ok(d_text, e_text):
    try:
        d, e = json.loads(d_text), json.loads(e_text)
    except Exception:
        return False
    fam = d['families']
    k = [i for i, f in enumerate(fam) if f['name'].startswith(OG1_FAMILY_PREFIX)]
    if len(k) != 1:
        return False
    want = dict(d)
    want['families'] = fam[:k[0] + 1] + [CENSUS_FAMILY] + fam[k[0] + 1:]
    return e == want


def run_check(commit, freeze):
    r = git('diff', '--name-status', '--no-renames', D, commit)
    rows = [l.split('\t') for l in r.stdout.splitlines() if l]
    exec_rows = {p: s for s, p in rows if not p.startswith(RDIR)}
    rec = {p for s, p in rows if p.startswith(RDIR)}
    check('P', 'delta(D, commit) is exactly the governed execution paths plus the record directory',
          exec_rows == GOVERNED and rec <= RECORD_FILES and PREREG in rec)
    module_checks(show(commit, MOD))
    check('I', 'OIBridge.lean is D\'s with exactly the frozen import line', imports_ok(show(D, IMPORTS),
                                                                                    show(commit, IMPORTS)))
    check('C', 'the census is D\'s with exactly the frozen family', census_ok(show(D, CENSUS), show(commit, CENSUS)))
    if freeze:
        check('F', 'the preregistration is unchanged from F', show(commit, PREREG) == show(freeze, PREREG))
        r = git('diff', '--name-only', D, freeze)
        check('F', 'delta(D, F) is the preregistration alone', r.stdout.split() == [PREREG])


def must_fail(code, label, mod2):
    before, count = list(FAILS), COUNT[0]
    saved = sys.stdout
    sys.stdout = io.StringIO()
    try:
        module_checks(mod2)
    finally:
        sys.stdout = saved
    new = FAILS[len(before):]
    del FAILS[len(before):]
    COUNT[0] = count
    check('M', 'mutation %s fails with %s' % (label, code), code in new)


def replace_once(text, a, b):
    assert text.count(a) >= 1, a
    return text.replace(a, b, 1)


def append_decl(text, decl):
    i = text.rindex('\nend ')
    i = text.rindex('\nend ', 0, i)
    return text[:i] + '\n' + decl + '\n' + text[i:]


def self_test():
    mod = git('cat-file', '-p', MOD_REFERENCE_BLOB).stdout
    check('T', 'the reference module blob is readable', bool(mod))
    module_checks(mod, ' [reference]')
    must_fail('N1', 'a removed declaration', replace_once(mod, '\n' + DECLS[-1][0] + ' ' + DECLS[-1][1],
                                                          '\n' + DECLS[-1][0] + ' ' + DECLS[-1][1] + 'X'))
    must_fail('N2', 'a changed binder context', replace_once(mod, CONTEXT[-3], CONTEXT[-3] + ' -- x\nopen Real'))
    must_fail('N3', 'a sorry', append_decl(mod, 'theorem extra_sorry : (1 : ℕ) = 1 := sorry'))
    must_fail('S1', 'a bare ELEM declaration', append_decl(mod, 'def ELEM (D : DirectedStages) : Prop := SCInf D'))
    must_fail('S2', 'the not-sufficient qualifier dropped',
              replace_once(mod, 'necessary, not sufficient; it says nothing', 'sufficient; it says nothing'))
    must_fail('S3', 'a visible-factor definition', append_decl(mod, 'def ElemVis (D : DirectedStages) : Prop := True'))
    must_fail('S4', 'SC∞ made a structure field',
              replace_once(mod, '  comp_P : ∀ {i j k : ι}',
                           '  consistent : ∀ {i j : ι} (h : i ≤ j), (map h).Consistent\n  comp_P : ∀ {i j k : ι}'))
    must_fail('S4', 'SC∞ concluded for every system',
              append_decl(mod, 'theorem scInf_all (D : DirectedStages) : SCInf D := by\n  exact absurd rfl rfl'))
    must_fail('S5', 'a ball claim', append_decl(mod, 'theorem ball3_of_completion : True := trivial'))
    d_imp = show(D, IMPORTS)
    good_imp = d_imp.replace(ANCHOR_IMPORT, ANCHOR_IMPORT + NEW_IMPORT, 1)
    check('M', 'imports: the frozen edit passes and a dropped line fails',
          imports_ok(d_imp, good_imp) and not imports_ok(d_imp, d_imp))
    d_cen = show(D, CENSUS)
    dd = json.loads(d_cen)
    k = [i for i, f in enumerate(dd['families']) if f['name'].startswith(OG1_FAMILY_PREFIX)][0]
    good = dict(dd)
    good['families'] = dd['families'][:k + 1] + [CENSUS_FAMILY] + dd['families'][k + 1:]
    bad = json.loads(json.dumps(good))
    bad['families'][k + 1]['status'] = 'carried'
    check('M', 'census: the frozen family passes and a changed status fails',
          census_ok(d_cen, json.dumps(good)) and not census_ok(d_cen, json.dumps(bad)))


def main(argv):
    if argv == ['--self-test']:
        self_test()
    elif len(argv) >= 2 and argv[0] == 'check':
        freeze = argv[3] if len(argv) == 4 and argv[2] == '--freeze' else None
        run_check(argv[1], freeze)
    else:
        print(__doc__)
        return 2
    if FAILS:
        print('controls: FAILED (%d of %d): %s' % (len(FAILS), COUNT[0], ' '.join(FAILS)))
        return 1
    print('controls: OK -- %d checks' % COUNT[0])
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
