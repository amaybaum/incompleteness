#!/usr/bin/env python3
"""controls.py -- round KINF-SEED-1's own contracts, to be frozen with the preregistration beside it.

Imports nothing from the repository and changes nothing in it. Reads D and the commit under check through git, and
embeds every frozen text it compares against: the predicted module (and the header of the design blob it was split
from, so that the link to the built blob is checked from this file alone), the effective statements, the resolution
map of every identifier at D, the landed controls' statements at D, the import line, the census family, the
round and governed-path blocks, the earned reading, the non-inference rule and the phrase list.

  controls.py freeze <F>                                  F mode: the frozen control plane
  controls.py check <commit> --freeze <F> [--axioms X]    a stage commit (C1, S1 or E) against D and F; at E the note
                                                          must state the token computed with the axiom expected
                                                          result X (for a commit with the same module blob)
  controls.py verdict <commit> [--axioms X]               the Q-SEED token from the measurements; X must be the
                                                          expected result of the exact-head run at <commit>
  controls.py axioms-from-log <log> <commit> [--run N --job N]
                                                          the expected result (AGENTS §A.42 item 1) from a build log
  controls.py --self-test                                 positive controls, the frozen mutations, countercontrols and
                                                          an end-to-end run of the real modes on fixture commits

Codes: F freeze; K controls blob; G governed paths and stage shape; R record directory; L linear execution from F;
N1-N3 declarations, frozen texts, hygiene; S1 surface; S2 resolution; S3 landed controls at D; S4 phrases; V verdict
and note; I import line; C census; T self-test assertion; M mutation or countercontrol outcome.
Every mode passes only if every code it requires was recorded and every record passed; a check that did not run
counts as failed. Unknown modes are refused. Exit 1 on any failure, 2 on a refused invocation.
"""
import hashlib, io, json, os, re, shutil, subprocess, sys, tempfile

D = 'dee3b5ae6fd3fb20fa1bad3337963e5af947f3a4'
RDIR = 'verification/programmes/oi-qm/reconstruction/round-kinf-seed-1-stage-sharp-test/'
PREREG = 'verification/programmes/oi-qm/reconstruction/round-kinf-seed-1-stage-sharp-test/preregistration.md'
CONTROLS = 'verification/programmes/oi-qm/reconstruction/round-kinf-seed-1-stage-sharp-test/controls.py'
RESULT = 'verification/programmes/oi-qm/reconstruction/round-kinf-seed-1-stage-sharp-test/result.md'
RECEIPT = 'verification/receipts/KINF-SEED-1.json'
LEAN = 'verification/lean-mathlib/OIBridge/'
MOD = 'verification/lean-mathlib/OIBridge/StageSeed.lean'
IMPORTS = 'verification/lean-mathlib/OIBridge.lean'
CENSUS = 'verification/lean-manuscript-census.json'
EXEC_PATHS = {'verification/lean-mathlib/OIBridge/StageSeed.lean': 'A', 'verification/lean-mathlib/OIBridge.lean': 'M', 'verification/lean-manuscript-census.json': 'M'}
ROUND_BLOCK = ['round KINF-SEED-1', 'kind non-sealing', 'record-directory verification/programmes/oi-qm/reconstruction/round-kinf-seed-1-stage-sharp-test/']
GOVERNED_BLOCK = ['record AM verification/programmes/oi-qm/reconstruction/round-kinf-seed-1-stage-sharp-test/', 'record AM verification/receipts/KINF-SEED-1.json', 'execution A verification/lean-mathlib/OIBridge/StageSeed.lean', 'execution M verification/lean-mathlib/OIBridge.lean', 'execution M verification/lean-manuscript-census.json']
ANCHOR_IMPORT = 'import OIBridge.EqvK2MaxCone\n'
NEW_IMPORT = 'import OIBridge.StageSeed\n'
IMPORT_ONLY = 'import OIBridge.DenseOrbit'
PREFIX = 'OIBridge.StageSeed.'
CENSUS_FAMILY = {'name': 'the sharp seed of the ball from a sharp stage test: under SC∞ a stage effect certain at one stage preparation and zero at another is a sharp seed of eball along the completion chart and any affine identification of the chart body with the ball (round KINF-SEED-1, reconstruction)', 'modules': ['StageSeed'], 'status': 'kernel-only', 'manuscript': []}
PRINTS = ['OIBridge.StageSeed.sharpSeed_eball_of_stage', 'OIBridge.StageSeed.exists_sharpSeed_eball_of_stage', 'OIBridge.StageSeed.exists_sharpSeed_eball_of_stage_dense']
DECLS = [['theorem', 'sharpSeed_eball_of_stage'], ['theorem', 'exists_sharpSeed_eball_of_stage'], ['theorem', 'exists_sharpSeed_eball_of_stage_dense']]
TEXTS = {'sharpSeed_eball_of_stage': "theorem sharpSeed_eball_of_stage {D : DirectedStages} (C : CompletionChart D) (hSC : SCInf D)\n    {i : D.ι} {e : (D.stage i).E} {x1 x0 : (D.stage i).P}\n    (h1 : (D.stage i).p e x1 = 1) (h0 : (D.stage i).p e x0 = 0)\n    (A : (Fin C.d → ℝ) ≃ᵃ[ℝ] (Fin C.d → ℝ)) (hA : A '' chartBody C = eball C.d) :\n    SharpSeed (eball C.d) (effTr A (effR C.L C.p0 (coord D ⟨i, e⟩)))", 'exists_sharpSeed_eball_of_stage': 'theorem exists_sharpSeed_eball_of_stage {D : DirectedStages} (C : CompletionChart D)\n    (hd : 0 < C.d) (hSC : SCInf D) {i : D.ι} {e : (D.stage i).E} {x1 x0 : (D.stage i).P}\n    (h1 : (D.stage i).p e x1 = 1) (h0 : (D.stage i).p e x0 = 0)\n    {G : Set ((Fin C.d → ℝ) ≃ᵃ[ℝ] (Fin C.d → ℝ))}\n    (hG : PreservesBody (chartBody C) G) (hT : BoundaryTransitive (chartBody C) G) :\n    ∃ r, SharpSeed (eball C.d) r', 'exists_sharpSeed_eball_of_stage_dense': 'theorem exists_sharpSeed_eball_of_stage_dense {D : DirectedStages} (C : CompletionChart D)\n    (hd : 0 < C.d) (hSC : SCInf D) {i : D.ι} {e : (D.stage i).E} {x1 x0 : (D.stage i).P}\n    (h1 : (D.stage i).p e x1 = 1) (h0 : (D.stage i).p e x0 = 0)\n    {G : Set ((Fin C.d → ℝ) ≃ᵃ[ℝ] (Fin C.d → ℝ))}\n    (hG : PreservesBody (chartBody C) G) (hT : DenseBoundaryOrbit (chartBody C) G) :\n    ∃ r, SharpSeed (eball C.d) r'}
EFFECTIVE = {'sharpSeed_eball_of_stage': "{D : DirectedStages} (C : CompletionChart D) (hSC : SCInf D) {i : D.ι} {e : (D.stage i).E} {x1 x0 : (D.stage i).P} (h1 : (D.stage i).p e x1 = 1) (h0 : (D.stage i).p e x0 = 0) (A : (Fin C.d → ℝ) ≃ᵃ[ℝ] (Fin C.d → ℝ)) (hA : A '' chartBody C = eball C.d) : SharpSeed (eball C.d) (effTr A (effR C.L C.p0 (coord D ⟨i, e⟩)))", 'exists_sharpSeed_eball_of_stage': '{D : DirectedStages} (C : CompletionChart D) (hd : 0 < C.d) (hSC : SCInf D) {i : D.ι} {e : (D.stage i).E} {x1 x0 : (D.stage i).P} (h1 : (D.stage i).p e x1 = 1) (h0 : (D.stage i).p e x0 = 0) {G : Set ((Fin C.d → ℝ) ≃ᵃ[ℝ] (Fin C.d → ℝ))} (hG : PreservesBody (chartBody C) G) (hT : BoundaryTransitive (chartBody C) G) : ∃ r, SharpSeed (eball C.d) r', 'exists_sharpSeed_eball_of_stage_dense': '{D : DirectedStages} (C : CompletionChart D) (hd : 0 < C.d) (hSC : SCInf D) {i : D.ι} {e : (D.stage i).E} {x1 x0 : (D.stage i).P} (h1 : (D.stage i).p e x1 = 1) (h0 : (D.stage i).p e x0 = 0) {G : Set ((Fin C.d → ℝ) ≃ᵃ[ℝ] (Fin C.d → ℝ))} (hG : PreservesBody (chartBody C) G) (hT : DenseBoundaryOrbit (chartBody C) G) : ∃ r, SharpSeed (eball C.d) r'}
PREAMBLE = 'import OIBridge.DenseOrbit\n\nnamespace OIBridge\nnamespace StageSeed\n\nopen Set KInfFoundations OrbitGeneration OrbitNormalization StageCompletion CompletionAction\nopen TransitiveBody CompositeDimension K2Guard DenseOrbit\n\nnoncomputable section\n'
CONTEXT = ['namespace OIBridge', 'namespace StageSeed', 'open Set KInfFoundations OrbitGeneration OrbitNormalization StageCompletion CompletionAction', 'open TransitiveBody CompositeDimension K2Guard DenseOrbit', 'noncomputable section', 'end', 'end StageSeed', 'end OIBridge']
RESOLVED = {'exists_sharpSeed_eball_of_stage|BoundaryTransitive': ['OIBridge.OrbitGeneration.BoundaryTransitive'], 'exists_sharpSeed_eball_of_stage|CompletionChart': ['OIBridge.CompletionAction.CompletionChart'], 'exists_sharpSeed_eball_of_stage|DirectedStages': ['OIBridge.StageCompletion.DirectedStages'], 'exists_sharpSeed_eball_of_stage|PreservesBody': ['OIBridge.OrbitGeneration.PreservesBody'], 'exists_sharpSeed_eball_of_stage|SCInf': ['OIBridge.StageCompletion.SCInf'], 'exists_sharpSeed_eball_of_stage|SharpSeed': ['OIBridge.OrbitGeneration.SharpSeed'], 'exists_sharpSeed_eball_of_stage|chartBody': ['OIBridge.CompletionAction.chartBody'], 'exists_sharpSeed_eball_of_stage|eball': ['OIBridge.TransitiveBody.eball'], 'exists_sharpSeed_eball_of_stage_dense|CompletionChart': ['OIBridge.CompletionAction.CompletionChart'], 'exists_sharpSeed_eball_of_stage_dense|DenseBoundaryOrbit': ['OIBridge.DenseOrbit.DenseBoundaryOrbit'], 'exists_sharpSeed_eball_of_stage_dense|DirectedStages': ['OIBridge.StageCompletion.DirectedStages'], 'exists_sharpSeed_eball_of_stage_dense|PreservesBody': ['OIBridge.OrbitGeneration.PreservesBody'], 'exists_sharpSeed_eball_of_stage_dense|SCInf': ['OIBridge.StageCompletion.SCInf'], 'exists_sharpSeed_eball_of_stage_dense|SharpSeed': ['OIBridge.OrbitGeneration.SharpSeed'], 'exists_sharpSeed_eball_of_stage_dense|chartBody': ['OIBridge.CompletionAction.chartBody'], 'exists_sharpSeed_eball_of_stage_dense|eball': ['OIBridge.TransitiveBody.eball'], 'sharpSeed_eball_of_stage|CompletionChart': ['OIBridge.CompletionAction.CompletionChart'], 'sharpSeed_eball_of_stage|DirectedStages': ['OIBridge.StageCompletion.DirectedStages'], 'sharpSeed_eball_of_stage|SCInf': ['OIBridge.StageCompletion.SCInf'], 'sharpSeed_eball_of_stage|SharpSeed': ['OIBridge.OrbitGeneration.SharpSeed'], 'sharpSeed_eball_of_stage|chartBody': ['OIBridge.CompletionAction.chartBody'], 'sharpSeed_eball_of_stage|coord': ['OIBridge.StageCompletion.coord'], 'sharpSeed_eball_of_stage|eball': ['OIBridge.TransitiveBody.eball'], 'sharpSeed_eball_of_stage|effR': ['OIBridge.OrbitNormalization.effR'], 'sharpSeed_eball_of_stage|effTr': ['OIBridge.OrbitNormalization.effTr']}
PINNED = {'SharpSeed': 'OIBridge.OrbitGeneration.SharpSeed', 'SCInf': 'OIBridge.StageCompletion.SCInf', 'CompletionChart': 'OIBridge.CompletionAction.CompletionChart', 'chartBody': 'OIBridge.CompletionAction.chartBody', 'eball': 'OIBridge.TransitiveBody.eball', 'effTr': 'OIBridge.OrbitNormalization.effTr', 'effR': 'OIBridge.OrbitNormalization.effR', 'coord': 'OIBridge.StageCompletion.coord', 'PreservesBody': 'OIBridge.OrbitGeneration.PreservesBody', 'BoundaryTransitive': 'OIBridge.OrbitGeneration.BoundaryTransitive', 'DenseBoundaryOrbit': 'OIBridge.DenseOrbit.DenseBoundaryOrbit'}
LANDED_CONTROLS = {'bitTower_scInf': ['StageCompletion', ': SCInf bitTower'], 'bitTower_sharpSeed': ['StageCompletion', ': SharpSeed (body bitTower) (coord bitTower ⟨(0 : ℕ), some false⟩)'], 'cmp1_core': ['StageCompletion', '(D : DirectedStages) {V : Type} [NormedAddCommGroup V] [NormedSpace ℝ V] : (∀ D : DirectedStages, ∀ e ∈ stageEffects D, IsEffectOn (body D) e) ∧ (∀ D : DirectedStages, SCInf D → ∀ (i : D.ι) (e : (D.stage i).E) (x1 x0 : (D.stage i).P), (D.stage i).p e x1 = 1 → (D.stage i).p e x0 = 0 → SharpSeed (body D) (coord D ⟨i, e⟩)) ∧ (∀ (D : DirectedStages) (E : BinaryVisible D) (i : D.ι), ∀ f ∈ body D, coord D ⟨i, E.v0 i⟩ f + coord D ⟨i, E.v1 i⟩ f = 1) ∧ (∀ (Ω : Set V), Ω.Nonempty → FiniteRank Ω → ∃ (d : ℕ) (L : (Fin d → ℝ) →ₗ[ℝ] V) (p0 : V), LinearMap.ker L = ⊥ ∧ ∀ x, x ∈ affineSpan ℝ Ω ↔ x ∈ Set.range (chart L p0)) ∧ ¬ SCInf badD ∧ (SCInf bitTower ∧ SharpSeed (body bitTower) (coord bitTower ⟨(0 : ℕ), some false⟩))'], 'not_scInf_bad': ['StageCompletion', ': ¬ SCInf badD'], 'not_sharpSeed_unsharp': ['OrbitGeneration', ': ¬ SharpSeed ball3 unsharpSeed']}
EARNED = "inside K1's hypothesis list the seed is not an independent seam; it is carried to the ball by the chart and the ball identification from one finite-stage fact, a *sharp stage test*."
NONINF = 'This round does not show that OI, StageCompletion or the observer architecture supplies a sharp stage test, a completion chart, SC∞, finite rank, boundary transitivity, a dense boundary orbit or any identification of the chart body with the ball; adopts no premise; and makes no manuscript claim. The sharp stage test — one stage effect with the value one at one stage preparation and zero at another — is a premise about a finite stage and is not sourced here. Every hypothesis of the three theorems is a hypothesis.'
PREREG_TEXTS = {'earned reading': "inside K1's hypothesis list the seed is not an independent seam; it is carried to the ball by the chart and the ball identification from one finite-stage fact, a *sharp stage test*.", 'non-inference rule': 'This round does not show that OI, StageCompletion or the observer architecture supplies a sharp stage test, a completion chart, SC∞, finite rank, boundary transitivity, a dense boundary orbit or any identification of the chart body with the ball; adopts no premise; and makes no manuscript claim. The sharp stage test — one stage effect with the value one at one stage preparation and zero at another — is a premise about a finite stage and is not sourced here. Every hypothesis of the three theorems is a hypothesis.', 'statement sharpSeed_eball_of_stage': "theorem sharpSeed_eball_of_stage {D : DirectedStages} (C : CompletionChart D) (hSC : SCInf D)\n    {i : D.ι} {e : (D.stage i).E} {x1 x0 : (D.stage i).P}\n    (h1 : (D.stage i).p e x1 = 1) (h0 : (D.stage i).p e x0 = 0)\n    (A : (Fin C.d → ℝ) ≃ᵃ[ℝ] (Fin C.d → ℝ)) (hA : A '' chartBody C = eball C.d) :\n    SharpSeed (eball C.d) (effTr A (effR C.L C.p0 (coord D ⟨i, e⟩)))", 'statement exists_sharpSeed_eball_of_stage': 'theorem exists_sharpSeed_eball_of_stage {D : DirectedStages} (C : CompletionChart D)\n    (hd : 0 < C.d) (hSC : SCInf D) {i : D.ι} {e : (D.stage i).E} {x1 x0 : (D.stage i).P}\n    (h1 : (D.stage i).p e x1 = 1) (h0 : (D.stage i).p e x0 = 0)\n    {G : Set ((Fin C.d → ℝ) ≃ᵃ[ℝ] (Fin C.d → ℝ))}\n    (hG : PreservesBody (chartBody C) G) (hT : BoundaryTransitive (chartBody C) G) :\n    ∃ r, SharpSeed (eball C.d) r', 'statement exists_sharpSeed_eball_of_stage_dense': 'theorem exists_sharpSeed_eball_of_stage_dense {D : DirectedStages} (C : CompletionChart D)\n    (hd : 0 < C.d) (hSC : SCInf D) {i : D.ι} {e : (D.stage i).E} {x1 x0 : (D.stage i).P}\n    (h1 : (D.stage i).p e x1 = 1) (h0 : (D.stage i).p e x0 = 0)\n    {G : Set ((Fin C.d → ℝ) ≃ᵃ[ℝ] (Fin C.d → ℝ))}\n    (hG : PreservesBody (chartBody C) G) (hT : DenseBoundaryOrbit (chartBody C) G) :\n    ∃ r, SharpSeed (eball C.d) r'}
DESIGN_HEADER = "/-\n  OIBridge/StageSeed.lean — design module of the research thread `research/equivalence` (node E8,\n  draft S1): the predicted module of round KINF-SEED-1, split from the design module `EqvSeams`\n  (§A, built in run 38083519826) with no statement changed. Not adopted, not certified, not a\n  round.\n\n  Under SC∞, a stage effect with the value one at one stage preparation and the value zero at\n  another gives a sharp seed of `eball C.d` along any affine equivalence carrying the chart body onto\n  the ball (`sharpSeed_eball_of_stage`); with TRB-1's identification (`exists_sharpSeed_eball_of_stage`)\n  or KTRANS-DENSE-1's (`exists_sharpSeed_eball_of_stage_dense`) the equivalence exists. Every\n  hypothesis is a premise; nothing here sources a stage test, a chart or a ball identification.\n\n  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build\n-/"
PRED_HEADER = "/-\n  OIBridge/StageSeed.lean — round KINF-SEED-1: the sharp seed of the ball from a sharp stage test.\n\n  Under SC∞, a stage effect with the value one at one stage preparation and the value zero at\n  another gives a sharp seed of `eball C.d` along any affine equivalence carrying the chart body onto\n  the ball (`sharpSeed_eball_of_stage`); with TRB-1's identification (`exists_sharpSeed_eball_of_stage`)\n  or KTRANS-DENSE-1's (`exists_sharpSeed_eball_of_stage_dense`) the equivalence exists. Every\n  hypothesis is a premise; nothing here sources a stage test, a chart or a ball identification.\n\n  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build\n-/"
BODY = "\nimport OIBridge.DenseOrbit\n\nnamespace OIBridge\nnamespace StageSeed\n\nopen Set KInfFoundations OrbitGeneration OrbitNormalization StageCompletion CompletionAction\nopen TransitiveBody CompositeDimension K2Guard DenseOrbit\n\nnoncomputable section\n\n/-! ### §A — K∞-Seed from K∞-Stage -/\n\n/-- **The seed of the ball from a sharp stage test.** Under SC∞, a stage effect certain at one stage\npreparation and zero at another, read through the completion chart and an affine equivalence of the\nchart body onto `eball C.d`, is a sharp seed of the ball. -/\ntheorem sharpSeed_eball_of_stage {D : DirectedStages} (C : CompletionChart D) (hSC : SCInf D)\n    {i : D.ι} {e : (D.stage i).E} {x1 x0 : (D.stage i).P}\n    (h1 : (D.stage i).p e x1 = 1) (h0 : (D.stage i).p e x0 = 0)\n    (A : (Fin C.d → ℝ) ≃ᵃ[ℝ] (Fin C.d → ℝ)) (hA : A '' chartBody C = eball C.d) :\n    SharpSeed (eball C.d) (effTr A (effR C.L C.p0 (coord D ⟨i, e⟩))) := by\n  have h2 : SharpSeed (chartBody C) (effR C.L C.p0 (coord D ⟨i, e⟩)) :=\n    sharpSeed_restrict C.L (fun v hv => mem_range_of_mem_body C hv)\n      (sharpSeed_completion D hSC h1 h0)\n  have h3 := sharpSeed_tr A h2\n  rw [hA] at h3\n  exact h3\n\n/-- With TRB-1's ball identification of the chart body (K∞-Trans on the chart body). -/\ntheorem exists_sharpSeed_eball_of_stage {D : DirectedStages} (C : CompletionChart D)\n    (hd : 0 < C.d) (hSC : SCInf D) {i : D.ι} {e : (D.stage i).E} {x1 x0 : (D.stage i).P}\n    (h1 : (D.stage i).p e x1 = 1) (h0 : (D.stage i).p e x0 = 0)\n    {G : Set ((Fin C.d → ℝ) ≃ᵃ[ℝ] (Fin C.d → ℝ))}\n    (hG : PreservesBody (chartBody C) G) (hT : BoundaryTransitive (chartBody C) G) :\n    ∃ r, SharpSeed (eball C.d) r := by\n  obtain ⟨A, hA⟩ := chartBody_eq_eball C hd hG hT\n  exact ⟨_, sharpSeed_eball_of_stage C hSC h1 h0 A hA⟩\n\n/-- With KTRANS-DENSE-1's ball identification (a dense boundary orbit on the chart body). -/\ntheorem exists_sharpSeed_eball_of_stage_dense {D : DirectedStages} (C : CompletionChart D)\n    (hd : 0 < C.d) (hSC : SCInf D) {i : D.ι} {e : (D.stage i).E} {x1 x0 : (D.stage i).P}\n    (h1 : (D.stage i).p e x1 = 1) (h0 : (D.stage i).p e x0 = 0)\n    {G : Set ((Fin C.d → ℝ) ≃ᵃ[ℝ] (Fin C.d → ℝ))}\n    (hG : PreservesBody (chartBody C) G) (hT : DenseBoundaryOrbit (chartBody C) G) :\n    ∃ r, SharpSeed (eball C.d) r := by\n  obtain ⟨A, hA⟩ := chartBody_eq_eball_of_dense C hd hG hT\n  exact ⟨_, sharpSeed_eball_of_stage C hSC h1 h0 A hA⟩\n\nend\n\nend StageSeed\nend OIBridge\n\n#print axioms OIBridge.StageSeed.sharpSeed_eball_of_stage\n#print axioms OIBridge.StageSeed.exists_sharpSeed_eball_of_stage\n#print axioms OIBridge.StageSeed.exists_sharpSeed_eball_of_stage_dense\n"
DESIGN_BLOB = 'b63691530db65a97c3e78195cb49b78039e596c2'
PRED_BLOB = '8e1098205f10c541a557efa66c40521038292b4b'
SELF_TEST_RECORDS = 56

# ===================================================================================================== core
# Shared mechanics. Every frozen text the rules compare against is embedded above; this part only reads git.

ALLOWED_AXIOMS = ('propext', 'Classical.choice', 'Quot.sound')
DECL = re.compile(r'^(?:@\[[^\]\n]*\]\s+)?(theorem|lemma|def|noncomputable def|abbrev|noncomputable abbrev|structure'
                  r'|instance)\s+(\S+)', re.M)
CTX = re.compile(r'^(variable|open|namespace|section|end|attribute|universe|set_option|noncomputable section)\b.*$',
                 re.M)
IDENT = re.compile(r'(?<![\w.\'@])[A-Za-z_][\w\'.]*')
BINDER_OPEN, BINDER_CLOSE = '({[⦃', ')}]⦄'
HEX40 = re.compile(r'^[0-9a-f]{40}$')

# --------------------------------------------------------------------------------------- the outcome registry
# Every check records its outcome as it runs. A mode passes only if every code the mode requires was recorded and
# every recorded outcome is True: a check that did not run counts as failed.
RESULTS = []


def check(code, name, cond):
    ok = cond is True
    RESULTS.append((code, ok))
    print(('  PASS  ' if ok else '  FAIL  ') + code + ' ' + name, flush=True)
    return ok


def finalize(required, results=None):
    """(ok, failed codes, codes required but never recorded)."""
    res = RESULTS if results is None else results
    seen = {c for c, _ in res}
    failed = sorted({c for c, ok in res if not ok})
    missing = sorted(set(required) - seen)
    return (not failed and not missing), failed, missing


# ------------------------------------------------------------------------------------------------------- git
GIT_ENV = [None]   # replaced by the self-test's fixture with a temporary object directory


def git_run(*args, data=None):
    return subprocess.run(['git'] + list(args), capture_output=True, input=data, env=GIT_ENV[0])


def git(*args, data=None):
    r = git_run(*args, data=data)
    if r.returncode != 0:
        raise RuntimeError('git %s: %s' % (' '.join(args), r.stderr.decode('utf-8', 'replace').strip()))
    return r.stdout.decode('utf-8')


def show(commit, path):
    r = git_run('show', '%s:%s' % (commit, path))
    return r.stdout.decode('utf-8') if r.returncode == 0 else None


def blob_of(commit, path):
    r = git_run('rev-parse', '--verify', '-q', '%s:%s' % (commit, path))
    return r.stdout.decode('utf-8').strip() if r.returncode == 0 else None


def rev(commit):
    r = git_run('rev-parse', '--verify', '-q', commit + '^{commit}')
    return r.stdout.decode('utf-8').strip() if r.returncode == 0 else None


def parents(commit):
    return git('rev-list', '--parents', '-n', '1', commit).split()[1:]


def name_status(a, b):
    out = git('diff', '--no-renames', '--name-status', a, b)
    rows = []
    for line in out.splitlines():
        if line:
            s, p = line.split('\t', 1)
            rows.append((s, p))
    return rows


def is_ancestor(a, b):
    return git_run('merge-base', '--is-ancestor', a, b).returncode == 0


def git_blob_id(text):
    """The git blob id of a text, computed without git."""
    data = text.encode('utf-8')
    return hashlib.sha1(b'blob %d\0' % len(data) + data).hexdigest()


def own_text():
    with open(os.path.abspath(__file__), 'rb') as f:
        return f.read().decode('utf-8')


# ------------------------------------------------------------------------------------------------ Lean surface
def norm(s):
    return ' '.join(s.split())


def header(text):
    i = text.find('\nimport ')
    return text[:i] if i != -1 else text


def preamble(text):
    """From the first import to the first section marker."""
    i = text.find('\nimport ')
    j = text.find('\n/-! ### ')
    return text[i + 1:j] if i != -1 and j != -1 else None


def context_lines(text):
    lines = text.split('\n')
    out = []
    for k, line in enumerate(lines):
        if CTX.match(line):
            block = [line]
            j = k + 1
            while j < len(lines) and lines[j].startswith('  ') and (line.startswith('variable') or
                                                                    line.startswith('open ')):
                block.append(lines[j])
                j += 1
            out.append('\n'.join(block))
    return out


def decls(text):
    return [[m.group(1), m.group(2)] for m in DECL.finditer(text)]


def stmt_end(chunk):
    ends = [j for j in (chunk.find(' :='),) if j != -1]
    m = re.search(r' where\n', chunk)
    if m:
        ends.append(m.start())
    return min(ends) if ends else -1


def spans(text):
    out = []
    ms = list(DECL.finditer(text))
    for k, m in enumerate(ms):
        start = m.start()
        nxt = ms[k + 1].start() if k + 1 < len(ms) else len(text)
        chunk = text[start:nxt]
        for stop in ('\n/--', '\n/-!', '\n#print', '\nend ', '\nend\n', '\nvariable', '\nopen ', '\nattribute'):
            j = chunk.find(stop)
            if j != -1:
                chunk = chunk[:j]
        chunk = chunk.rstrip()
        se = -1
        if m.group(1) in ('theorem', 'lemma'):
            j = stmt_end(chunk)
            if j != -1:
                se = start + j
        out.append((m.group(1), m.group(2), start, se if se != -1 else start + len(chunk), start + len(chunk)))
    return out


def decl_chunks(text):
    """name -> (kind, statement (theorems) or whole text (definitions), proof text (theorems))."""
    out = {}
    for kind, name, start, se, cend in spans(text):
        if kind in ('theorem', 'lemma'):
            out[name] = (kind, text[start:se], text[se:cend])
        else:
            out[name] = (kind, text[start:cend], '')
    return out


def colon_index(stmt):
    m = DECL.match(stmt)
    i = m.end() if m else 0
    depth = 0
    for j in range(i, len(stmt)):
        c = stmt[j]
        if c in BINDER_OPEN:
            depth += 1
        elif c in BINDER_CLOSE:
            depth -= 1
        elif c == ':' and depth == 0 and stmt[j:j + 2] != ':=':
            return j
    return -1


def split_statement(stmt):
    m = DECL.match(stmt)
    i = m.end() if m else 0
    j = colon_index(stmt)
    if j == -1:
        return stmt[i:], ''
    return stmt[i:j], stmt[j + 1:]


def code_only(text):
    text = re.sub(r'/-.*?-/', ' ', text, flags=re.S)
    return re.sub(r'--[^\n]*', ' ', text)


def token(name, text):
    return re.search(r'(?<![\w.\'])%s(?![\w\'])' % re.escape(name), text) is not None


def groups(b):
    out, depth, start = [], 0, None
    for i, c in enumerate(b):
        if c in BINDER_OPEN:
            if depth == 0:
                start = i
            depth += 1
        elif c in BINDER_CLOSE:
            depth -= 1
            if depth == 0 and start is not None:
                out.append(norm(b[start:i + 1]))
                start = None
    return out


def group_names(g):
    inner = g[1:-1]
    j = inner.find(' : ')
    if j == -1:
        return []
    return inner[:j].split()


def scopes_at(text):
    """name -> (variable groups in scope, namespaces in scope, opened namespaces in scope) at each declaration."""
    stack = [([], [], [])]
    out = {}
    lines = text.split('\n')
    pos = 0
    k = 0
    decl_at = {m.start(): m.group(2) for m in DECL.finditer(text)}
    while k < len(lines):
        line = lines[k]
        block = [line]
        j = k + 1
        if line.startswith('variable') or line.startswith('open '):
            while j < len(lines) and lines[j].startswith('  '):
                block.append(lines[j])
                j += 1
        whole = '\n'.join(block)
        m = re.match(r'^(namespace|section|noncomputable section)\b\s*(\S*)', line)
        if m:
            stack.append(([], [m.group(2)] if m.group(1) == 'namespace' else [], []))
        elif re.match(r'^end\b', line):
            if len(stack) > 1:
                stack.pop()
        elif line.startswith('variable'):
            stack[-1][0].extend(groups(whole[len('variable'):]))
        elif line.startswith('open '):
            stack[-1][2].extend(whole[len('open '):].split())
        if pos in decl_at:
            out[decl_at[pos]] = ([g for s in stack for g in s[0]], [n for s in stack for n in s[1]],
                                 [o for s in stack for o in s[2]])
        for ln in block:
            pos += len(ln) + 1
        k = j
    return out


def effective(text, name):
    """The section variables a declaration's statement uses, in declared order, then its binders and conclusion."""
    chunks = decl_chunks(text)
    if name not in chunks:
        return None
    stmt = chunks[name][1]
    if chunks[name][0] not in ('theorem', 'lemma'):
        j = stmt_end(stmt)
        stmt = stmt[:j] if j != -1 else stmt
    vs = scopes_at(text).get(name, ([], [], []))[0]
    b, c = split_statement(stmt)
    used = norm(b) + ' : ' + norm(c)
    inc = [False] * len(vs)
    changed = True
    while changed:
        changed = False
        hay = used + ' ' + ' '.join(g for g, i in zip(vs, inc) if i)
        for n, g in enumerate(vs):
            if inc[n]:
                continue
            names = group_names(g)
            if names and any(token(x, hay) for x in names):
                inc[n] = True
                changed = True
            elif not names and g.startswith('[') and any(token(x, g) for gg, i in zip(vs, inc) if i
                                                          for x in group_names(gg)):
                inc[n] = True
                changed = True
    pre = ' '.join(g for g, i in zip(vs, inc) if i)
    return norm(pre + ' ' + norm(b) + ' : ' + norm(c))


_INV_CACHE = {}


def inventory_one(text):
    if text in _INV_CACHE:
        return _INV_CACHE[text]
    names, spaces = set(), set()
    sc = scopes_at(text)
    for kind, name in decls(text):
        nss = sc.get(name, ([], [], []))[1]
        prefix = '.'.join(nss)
        names.add((prefix + '.' if prefix else '') + name)
        for i in range(1, len(nss) + 1):
            spaces.add('.'.join(nss[:i]))
    _INV_CACHE[text] = (names, spaces)
    return names, spaces


def inventory(files):
    names, spaces = set(), set()
    for t in files:
        n, s = inventory_one(t)
        names |= n
        spaces |= s
    return names, spaces


def visible(nss, ops, spaces):
    out = [''] + ['.'.join(nss[:i]) for i in range(1, len(nss) + 1)]
    for o in ops:
        hit = [p + '.' + o for p in ['.'.join(nss[:i]) for i in range(len(nss), 0, -1)] if p + '.' + o in spaces]
        out.append(hit[0] if hit else o)
    return out


def resolve(tok, vis, names):
    return sorted({(v + '.' if v else '') + tok for v in vis} & names)


def top_colon(s):
    depth = 0
    for j, c in enumerate(s):
        if c in BINDER_OPEN:
            depth += 1
        elif c in BINDER_CLOSE:
            depth -= 1
        elif c == ':' and depth == 0 and s[j:j + 2] != ':=':
            return j
    return len(s)


def strip_binders(eff):
    k = top_colon(eff)
    bound = set()
    for g in groups(eff[:k]):
        bound.update(group_names(g))
    for m in re.finditer(r'(?:∃|∀|fun|λ)\s+([^,:=]+?)\s*(?::|,|=>)', eff[k:]):
        bound.update(x for x in m.group(1).split() if re.match(r"^[A-Za-zΩ_][\w']*$", x))
    return [t for t in IDENT.findall(eff) if t not in bound]


def resolution_map(mod, names_of_interest, inv_files, proof_tokens=()):
    """{(declaration, identifier): [fully qualified OIBridge names it resolves to]} for every identifier of every
    named declaration's effective statement (and, for the (declaration, identifier) pairs of proof_tokens, of its
    proof), resolved in the module's namespace context against the inventory of inv_files and the module."""
    names, spaces = inventory(inv_files + [mod])
    sc = scopes_at(mod)
    chunks = decl_chunks(mod)
    out = {}
    for dn in names_of_interest:
        eff = effective(mod, dn)
        if eff is None:
            out[(dn, '<absent>')] = []
            continue
        s = sc.get(dn, ([], [], []))
        vis = visible(s[1], s[2], spaces)
        toks = set(strip_binders(eff))
        kind, whole, _ = chunks[dn]
        if kind not in ('theorem', 'lemma'):
            j = stmt_end(whole)
            body = whole[j:] if j != -1 else ''
            fields = set(re.findall(r'^  ([A-Za-zΩ_][\w\']*) :', body, re.M))
            toks |= {t for t in IDENT.findall(code_only(body)) if t not in fields}
        for t in sorted(toks):
            hits = resolve(t, vis, names)
            if hits:
                out[(dn, t)] = hits
    for dn, t in proof_tokens:
        s = sc.get(dn, ([], [], []))
        vis = visible(s[1], s[2], spaces)
        proof = chunks.get(dn, ('', '', ''))[2]
        out[(dn, t + '#proof')] = resolve(t, vis, names) if token(t, code_only(proof)) else []
    return out


def print_lines(mod):
    return re.findall(r'^#print axioms (\S+)', mod, re.M)


# ------------------------------------------------------------------------------------- governed paths and F
def fenced_block(text, tag):
    """The lines of the one fenced block opened by exactly ```tag, or None unless there is exactly one."""
    if text is None:
        return None
    ms = list(re.finditer(r'^```%s\n(.*?)^```\n' % re.escape(tag), text, re.M | re.S))
    if len(ms) != 1:
        return None
    return [l for l in ms[0].group(1).split('\n') if l]


def governed_rows(lines):
    rows = []
    for l in lines or []:
        p = l.split(' ')
        if len(p) != 3 or p[0] not in ('record', 'execution') or not set(p[1]) <= set('AMD'):
            return None
        rows.append((p[0], p[1], p[2]))
    return rows


def row_covers(row, status, path):
    cls, letters, p = row
    if status not in letters:
        return False
    return path.startswith(p) if p.endswith('/') else path == p


def delta_bad(rows, ns):
    """The (status, path) entries of a name-status list no governed row covers."""
    return [(s, p) for s, p in ns if not any(row_covers(r, s, p) for r in rows)]


def control_plane(path):
    return path == PREREG or path.startswith(RDIR + 'amendments/')


def freeze_checks(F):
    """F mode: the frozen control plane. F is a descendant of D along single-parent commits that change only
    control-plane files; delta(D, F) is the preregistration (and amendments); the round and governed-path blocks are
    the frozen ones; the preregistration states the frozen texts these controls compare against and pins this
    controls.py's blob."""
    Fc = rev(F)
    check('F', 'F resolves to a commit', Fc is not None)
    if Fc is None:
        return
    chain = git('rev-list', '--reverse', '%s..%s' % (D, Fc)).split() if is_ancestor(D, Fc) else []
    check('F', 'D is an ancestor of F', is_ancestor(D, Fc))
    bad = []
    for c in chain:
        ps = parents(c)
        ch = [p for _, p in name_status(ps[0], c)] if len(ps) == 1 else ['<merge>']
        if len(ps) != 1 or not all(control_plane(p) for p in ch):
            bad.append(c[:12])
    check('F', 'every commit of D..F has one parent and changes only control-plane files%s'
          % ((' (bad: %s)' % bad[:3]) if bad else ''), bool(chain) and not bad)
    ns = name_status(D, Fc)
    check('F', 'delta(D, F) is the preregistration and amendments only, the preregistration among them',
          all(control_plane(p) for _, p in ns) and ('A', PREREG) in ns)
    pre = show(Fc, PREREG) or ''
    check('F', 'the v3-round block at F is the frozen one', fenced_block(pre, 'v3-round') == ROUND_BLOCK)
    check('F', 'the v3-governed-paths block at F is the frozen one', fenced_block(pre, 'v3-governed-paths') ==
          GOVERNED_BLOCK and governed_rows(GOVERNED_BLOCK) is not None)
    missing = [k for k, t in PREREG_TEXTS.items() if norm(t) not in norm(unquote(pre))]
    check('F', 'the preregistration at F states every frozen text these controls compare against%s'
          % ((' (missing: %s)' % missing[:3]) if missing else ''), not missing)
    own = git_blob_id(own_text())
    check('K', 'the preregistration at F pins this controls.py blob %s' % own, own in pre)


def unquote(note):
    return '\n'.join(re.sub(r'^\s*>\s?', '', line) for line in note.split('\n'))


def stage_of(ns):
    """C1, S1 or E from delta(D, commit); None for any other shape (refused)."""
    rec = {p for s, p in ns if p.startswith(RDIR) and not control_plane(p)}
    exe = {p for s, p in ns if not p.startswith(RDIR)}
    if exe == set() and rec == {CONTROLS}:
        return 'C1'
    if exe == set(EXEC_PATHS) and rec == {CONTROLS}:
        return 'S1'
    if exe == set(EXEC_PATHS) and rec == {CONTROLS, RESULT}:
        return 'E'
    return None


def path_checks(commit, F):
    """G, R, L and K at a stage commit after F."""
    ns = name_status(D, commit)
    rows = governed_rows(fenced_block(show(commit, PREREG), 'v3-governed-paths'))
    check('G', 'the governed-path block at the commit is the frozen one', rows is not None and
          fenced_block(show(commit, PREREG), 'v3-governed-paths') == GOVERNED_BLOCK)
    bad = delta_bad(governed_rows(GOVERNED_BLOCK), ns)
    check('G', 'every path of delta(D, commit) is covered by a governed row with its status%s'
          % ((' (uncovered: %s)' % bad[:3]) if bad else ''), not bad)
    exe = {p: s for s, p in ns if not p.startswith(RDIR)}
    stage = stage_of(ns)
    check('G', 'the commit is a recognized stage (C1, S1 or E): %s' % stage, stage is not None)
    if stage in ('S1', 'E'):
        check('G', 'delta(D, commit) carries exactly the governed execution paths with their frozen statuses',
              exe == EXEC_PATHS)
    check('G', 'the receipt is absent before the receipt commit', blob_of(commit, RECEIPT) is None)
    files = set(git('ls-tree', '-r', '--name-only', commit, '--', RDIR).split())
    want = {PREREG, CONTROLS} | ({RESULT} if stage == 'E' else set())
    allowed_am = {p for p in files if p.startswith(RDIR + 'amendments/')}
    check('R', 'the record directory holds exactly %s (and amendments)' % sorted(os.path.basename(p) for p in want),
          files - allowed_am == want)
    check('K', 'controls.py at the commit is this file', show(commit, CONTROLS) == own_text())
    # linear execution from F
    Fc = rev(F)
    okF = Fc is not None and is_ancestor(Fc, commit)
    check('L', 'F is an ancestor of the commit', okF)
    chain = git('rev-list', '--reverse', '%s..%s' % (Fc, commit)).split() if okF else []
    shape = []
    for k, c in enumerate(chain):
        ps = parents(c)
        if len(ps) != 1 or (k == 0 and ps[0] != Fc) or (k > 0 and ps[0] != chain[k - 1]):
            shape.append('nonlinear ' + c[:12])
            continue
        ch = name_status(ps[0], c)
        if k == 0:
            if ch != [('A', CONTROLS)]:
                shape.append('C1 is not the controls.py addition alone')
        elif any(p.startswith(RDIR) for _, p in ch) and not (ch == [('A', RESULT)] and k == len(chain) - 1):
            shape.append('record change outside C1 and the final note ' + c[:12])
        elif any(p.startswith(RDIR) for _, p in ch) is False and not all(p in EXEC_PATHS for _, p in ch):
            shape.append('a stage commit leaves the execution paths ' + c[:12])
    check('L', 'F..commit is linear: C1 adds controls.py alone, stage commits change execution paths only, the note '
               'comes last%s' % ((' (%s)' % shape[:2]) if shape else ''), bool(chain) and not shape)
    check('F', 'the preregistration is unchanged from F', okF and blob_of(commit, PREREG) == blob_of(Fc, PREREG))
    amend_ok = okF and [p for p in files if p.startswith(RDIR + 'amendments/')] == \
        [p for p in git('ls-tree', '-r', '--name-only', Fc, '--', RDIR + 'amendments/').split()]
    check('F', 'the amendments are unchanged from F', amend_ok)
    return stage


def imports_ok(d_text, e_text):
    return d_text is not None and e_text is not None and d_text.count(ANCHOR_IMPORT) == 1 and \
        e_text == d_text.replace(ANCHOR_IMPORT, ANCHOR_IMPORT + NEW_IMPORT, 1)


def census_want(d_text):
    d = json.loads(d_text)
    want = dict(d)
    want['families'] = list(d['families']) + [CENSUS_FAMILY]
    return json.dumps(want, indent=2, ensure_ascii=False) + '\n'


def census_ok(d_text, e_text):
    try:
        return d_text is not None and json.dumps(json.loads(d_text), indent=2, ensure_ascii=False) + '\n' == d_text \
            and e_text == census_want(d_text)
    except Exception:
        return False


# ------------------------------------------------------------------------------------------ axiom expected results
def axioms_from_log(text, commit, run=None, job=None):
    """An expected result (AGENTS §A.42 item 1) from a Lean build log: the module's `#print axioms` reports."""
    out = {}
    for m in re.finditer(r"'(%s[^']+)' depends on axioms: \[([^\]]*)\]" % re.escape(PREFIX), text):
        out[m.group(1)] = [a.strip() for a in m.group(2).split(',') if a.strip()]
    for m in re.finditer(r"'(%s[^']+)' does not depend on any axioms" % re.escape(PREFIX), text):
        out[m.group(1)] = []
    return {'commit': commit, 'recipe': 'workflow_dispatch of .github/workflows/verify.yml at commit; Mathlib bridge '
            'job; the module\'s #print axioms reports', 'run': run, 'job': job,
            'source_digest': 'sha256:' + hashlib.sha256(text.encode('utf-8')).hexdigest(),
            'build': 'success' if re.search(r'Build completed successfully', text) else 'not-observed',
            'axioms': out}


def axioms_status(ax, commit, exact=True):
    """(within, reason): every frozen print reported within the three axioms, by a well-formed expected result for
    this commit (exact) or for a commit whose module blob is this commit's (not exact)."""
    if ax is None:
        return False, 'no axiom expected result supplied'
    if not isinstance(ax, dict) or not HEX40.match(str(ax.get('commit', ''))) or ax.get('build') != 'success' or \
            not isinstance(ax.get('axioms'), dict) or not ax.get('recipe') or 'source_digest' not in ax:
        return False, 'the axiom expected result is malformed or reports no successful build'
    c = rev(commit)
    if exact and ax['commit'] != c:
        return False, 'the axiom expected result is for %s, not the commit under check' % ax['commit'][:12]
    if not exact and (rev(ax['commit']) is None or blob_of(ax['commit'], MOD) != blob_of(commit, MOD)):
        return False, 'the axiom expected result is for a commit with another module blob'
    rep = ax['axioms']
    if sorted(rep) != sorted(PRINTS):
        return False, 'the reports are not exactly the frozen prints'
    bad = [n for n in PRINTS if not isinstance(rep[n], list) or not set(rep[n]) <= set(ALLOWED_AXIOMS)]
    return (not bad), ('outside the three axioms: %s' % bad[:3]) if bad else 'within the three axioms'


def load_axioms(path):
    if path is None:
        return None
    try:
        with open(path, encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return {'malformed': True}


# --------------------------------------------------------------------------------------------- fixture (self-test)
class Fixture:
    """Real commits D -> F -> C1 -> S1 -> E built in a temporary object directory that borrows the repository's
    objects as an alternate; nothing is written to the repository."""

    def __init__(self):
        self.td = tempfile.mkdtemp(prefix='controls-fixture-')
        objs = os.path.abspath(git('rev-parse', '--git-path', 'objects').strip())
        os.makedirs(os.path.join(self.td, 'objects', 'info'))
        env = dict(os.environ)
        env.update({'GIT_OBJECT_DIRECTORY': os.path.join(self.td, 'objects'),
                    'GIT_ALTERNATE_OBJECT_DIRECTORIES': objs, 'GIT_INDEX_FILE': os.path.join(self.td, 'index'),
                    'GIT_AUTHOR_NAME': 'fixture', 'GIT_AUTHOR_EMAIL': 'fixture',
                    'GIT_COMMITTER_NAME': 'fixture', 'GIT_COMMITTER_EMAIL': 'fixture',
                    'GIT_AUTHOR_DATE': '2026-01-01T00:00:00Z', 'GIT_COMMITTER_DATE': '2026-01-01T00:00:00Z'})
        self.env = env
        self.saved = GIT_ENV[0]
        GIT_ENV[0] = env

    def close(self):
        GIT_ENV[0] = self.saved
        shutil.rmtree(self.td, ignore_errors=True)

    def commit(self, parent_list, base_tree_commit, changes, msg='fixture'):
        """changes: {path: text or None (delete)} applied to base_tree_commit's tree."""
        git('read-tree', base_tree_commit + '^{tree}')
        for p, t in sorted(changes.items()):
            if t is None:
                git('update-index', '--force-remove', p)
            else:
                b = git('hash-object', '-w', '--stdin', data=t.encode('utf-8')).strip()
                git('update-index', '--add', '--cacheinfo', '100644,%s,%s' % (b, p))
        tree = git('write-tree').strip()
        args = ['commit-tree', tree, '-m', msg]
        for p in parent_list:
            args += ['-p', p]
        return git(*args).strip()


def quiet(fn, *a, **k):
    """Run a mode with its output captured; return (ok, failed codes, missing codes) from its own records."""
    start = len(RESULTS)
    saved = sys.stdout
    sys.stdout = io.StringIO()
    try:
        req = fn(*a, **k)
    except Exception as e:
        sys.stdout = saved
        del RESULTS[start:]
        return False, ['EXC:%s' % type(e).__name__], []
    finally:
        sys.stdout = saved
    mine = RESULTS[start:]
    del RESULTS[start:]
    return finalize(req or [], mine)


def expect(label, cond):
    """A self-test assertion, recorded under code T."""
    return check('T', label, cond)

# =========================================================================================== round KINF-SEED-1
TOKENS = ('KINF-SEED-PROVED', 'KINF-SEED-NOT-ESTABLISHED')
PHRASES = ('OI supplies', 'OI provides', 'derived from OI', 'sourced from OI', 'K∞-Seed is discharged',
           'K∞-Seed is derived', 'no longer needed', 'premise adopted', 'design module', 'not for merge')
THEOREMS = [n for k, n in DECLS if k == 'theorem']
REQUIRED_BASE = ['G', 'R', 'K', 'L', 'F']
REQUIRED_MODULE = ['N1', 'N2', 'N3', 'S1', 'S2', 'S3', 'S4', 'I', 'C']


def phrase_hits(text):
    t = norm(unquote(text)).lower()
    for frozen in (EARNED, NONINF):
        t = t.replace(norm(frozen).lower(), ' ')
    return [p for p in PHRASES if norm(p).lower() in t]


def note_tokens(note):
    return sorted(t for t in TOKENS if re.search(r'(?<![\w-])%s(?![\w-])' % re.escape(t), note))


def landed_controls(show_d):
    """S3: the landed controls' effective statements read at D."""
    out = {}
    for name, (m, _) in sorted(LANDED_CONTROLS.items()):
        t = show_d(LEAN + m + '.lean')
        out[name] = [m, effective(t, name) if t else None]
    return out


def s1_ok(mod):
    eff = {n: effective(mod, n) for n in THEOREMS}
    imports = re.findall(r'^import .*$', mod, re.M)
    return eff == EFFECTIVE and print_lines(mod) == PRINTS and imports == [IMPORT_ONLY] and \
        preamble(mod) == PREAMBLE


def s2_bad(mod, inv_files):
    rm = resolution_map(mod, THEOREMS, inv_files)
    bad = sorted('%s:%s' % k for k, v in rm.items() if len(v) != 1)
    for (dn, t), v in rm.items():
        if t in PINNED and v != [PINNED[t]]:
            bad.append('%s:%s->%s' % (dn, t, v))
    if {'%s|%s' % k: v for k, v in rm.items()} != RESOLVED:
        bad.append('resolution differs from the frozen map at D')
    return bad


def seed_cell(mod, landed, ax_within, inv_files):
    """KINF-SEED-PROVED iff the three theorems have exactly the frozen effective statements (S1), every identifier
    they name resolves to the landed declaration it resolves to at D (S2), the module builds with each frozen print
    within the three axioms (measured, from the axiom expected result), and the landed controls of S3 read at D have
    their frozen statements. Otherwise KINF-SEED-NOT-ESTABLISHED."""
    ok = mod is not None and s1_ok(mod) and not s2_bad(mod, inv_files) and ax_within is True and \
        landed == LANDED_CONTROLS
    return TOKENS[0] if ok else TOKENS[1]


_INV = []


def d_inventory_files():
    if not _INV:
        out = git('ls-tree', '--name-only', D, LEAN)
        _INV.extend(show(D, p) for p in out.split() if p.endswith('.lean'))
    return list(_INV)


def module_checks(mod, tag='', landed=None, inv_files=None):
    if landed is None:
        landed = landed_controls(lambda p: show(D, p))
    if inv_files is None:
        inv_files = d_inventory_files()
    if mod is None:
        check('N1', 'module present' + tag, False)
        return
    check('N1', 'the module declares exactly the three frozen theorems, in order' + tag, decls(mod) == DECLS)
    check('N2', 'the preamble is the frozen one' + tag, preamble(mod) == PREAMBLE)
    check('N2', 'every context line is the frozen one, in order' + tag, context_lines(mod) == CONTEXT)
    chunks = decl_chunks(mod)
    bad = sorted(n for n in TEXTS if chunks.get(n, ('', None))[1] != TEXTS[n])
    check('N2', 'every frozen statement unchanged%s' % ((' (changed: %s)' % bad) if bad else '') + tag, not bad)
    c = code_only(mod)
    check('N3', 'no sorry, admit, axiom declaration or native_decide' + tag,
          not re.search(r'\bsorry\b|\badmit\b|^\s*axiom\b|native_decide', c, re.M))
    check('S1', 'the three effective statements, the three prints in order and the single import are the frozen '
                'ones' + tag, s1_ok(mod))
    bad2 = s2_bad(mod, inv_files)
    check('S2', 'every identifier resolves uniquely, to the landed declaration it resolves to at D%s'
          % ((' %s' % bad2[:3]) if bad2 else '') + tag, not bad2)
    badl = sorted(n for n in LANDED_CONTROLS if landed.get(n) != LANDED_CONTROLS[n])
    check('S3', 'the landed controls read at D have their frozen statements%s' % ((' %s' % badl) if badl else '') + tag,
          not badl)
    ph = phrase_hits(header(mod))
    check('S4', 'the module header carries none of the frozen phrases%s' % ((' %s' % ph) if ph else '') + tag, not ph)


def note_checks(note, token):
    ph = phrase_hits(note)
    check('S4', 'the result note carries none of the frozen phrases%s' % ((' %s' % ph) if ph else ''), not ph)
    toks = note_tokens(note)
    check('V', 'the result note states exactly the computed token %s (found %s)' % (token, toks), toks == [token])
    n = norm(unquote(note))
    check('V', 'the non-inference rule is stated in its frozen words', norm(NONINF) in n)
    has = norm(EARNED) in n
    check('V', 'the earned reading is stated exactly when the cell is positive', has == (token == TOKENS[0]))


def run_freeze(F):
    freeze_checks(F)
    return ['F', 'K']


def run_check(commit, F, axioms_path=None, axioms=None):
    c = rev(commit)
    check('G', 'the commit resolves', c is not None)
    if c is None:
        return REQUIRED_BASE + REQUIRED_MODULE
    freeze_checks(F)
    stage = path_checks(c, F)
    if stage in ('S1', 'E'):
        module_checks(show(c, MOD))
        check('I', 'OIBridge.lean is D\'s with exactly the frozen import line', imports_ok(show(D, IMPORTS),
                                                                                        show(c, IMPORTS)))
        check('C', 'the census is D\'s with exactly the frozen family at the end, in D\'s two-space layout',
              census_ok(show(D, CENSUS), show(c, CENSUS)))
    note = show(c, RESULT)
    if stage == 'E':
        ax = axioms if axioms is not None else load_axioms(axioms_path)
        within, why = axioms_status(ax, c, exact=False)
        check('V', 'the axiom expected result is well formed and covers this module blob: %s' % why, within)
        token = seed_cell(show(c, MOD), landed_controls(lambda p: show(D, p)), within, d_inventory_files())
        note_checks(note, token)
    return REQUIRED_BASE + ([] if stage == 'C1' else REQUIRED_MODULE) + (['V'] if stage == 'E' else [])


def run_verdict(commit, axioms_path=None, axioms=None):
    c = rev(commit)
    ax = axioms if axioms is not None else load_axioms(axioms_path)
    within, why = axioms_status(ax, c, exact=True) if c else (False, 'no commit')
    landed = landed_controls(lambda p: show(D, p))
    token = seed_cell(show(c, MOD) if c else None, landed, within, d_inventory_files())
    print('VERDICT  Q-SEED  %s' % token)
    print('  axioms: %s' % why)
    check('V', 'exactly one token for Q-SEED, generated from the measurements', token in TOKENS)
    check('V', 'the landed controls read at D are the frozen ones', landed == LANDED_CONTROLS)
    return ['V']


# ------------------------------------------------------------------------------------------------------ self-test
def must_fail(code, label, mod2):
    ok, failed, missing = quiet(lambda: (module_checks(mod2), [])[1])
    check('M', 'mutation %s fails with %s' % (label, code), code in failed)


def replace_once(text, a, b):
    assert text.count(a) == 1, a
    return text.replace(a, b, 1)


def std_axioms(commit, extra=None):
    ax = {n: list(ALLOWED_AXIOMS) for n in PRINTS}
    if extra:
        ax.update(extra)
    return {'commit': commit, 'recipe': 'fixture', 'run': None, 'job': None, 'source_digest': 'sha256:0',
            'build': 'success', 'axioms': ax}


def fixture_note(token):
    body = '# KINF-SEED-1: RESULT (fixture)\n\n**Q-SEED: %s.**\n\n' % token
    if token == TOKENS[0]:
        body += EARNED + '\n\n'
    return body + '> ' + NONINF + '\n'


FIRST = 'theorem sharpSeed_eball_of_stage {D : DirectedStages} (C : CompletionChart D) (hSC : SCInf D)\n'
SEED_CONCL = '    SharpSeed (eball C.d) (effTr A (effR C.L C.p0 (coord D ⟨i, e⟩))) := by'
H0 = '    (h1 : (D.stage i).p e x1 = 1) (h0 : (D.stage i).p e x0 = 0)\n    (A :'
HT = '(hG : PreservesBody (chartBody C) G) (hT : BoundaryTransitive (chartBody C) G) :'
LAST_PRINT = '#print axioms OIBridge.StageSeed.exists_sharpSeed_eball_of_stage_dense\n'
OPEN2 = 'open TransitiveBody CompositeDimension K2Guard DenseOrbit\n'


def self_test():
    mod = PRED_HEADER + BODY
    expect('the embedded predicted module has the frozen blob id %s' % PRED_BLOB[:12], git_blob_id(mod) == PRED_BLOB)
    expect('the embedded design header with the same body is design blob %s (built in run 3)' % DESIGN_BLOB[:12],
           git_blob_id(DESIGN_HEADER + BODY) == DESIGN_BLOB)
    expect('the predicted module differs from the design blob in its header comment alone',
           header(mod) == PRED_HEADER and header(DESIGN_HEADER + BODY) == DESIGN_HEADER)
    landed = landed_controls(lambda p: show(D, p))
    expect('the landed controls read at D are the frozen ones', landed == LANDED_CONTROLS)
    inv = d_inventory_files()
    expect('D\'s inventory is readable (%d modules)' % len(inv), len(inv) > 100)
    ok, failed, missing = quiet(lambda: (module_checks(mod), [])[1])
    expect('the predicted module passes every module check (failed: %s)' % failed, ok)
    ok, failed, missing = quiet(lambda: (module_checks(DESIGN_HEADER + BODY), [])[1])
    expect('countercontrol: the design blob itself fails S4 only (its header says "design module"): %s' % failed,
           failed == ['S4'])
    # S1 -- the prereg's mutations
    must_fail('S1', 'hSC dropped', replace_once(mod, FIRST, FIRST.replace(' (hSC : SCInf D)', '')))
    must_fail('S1', 'h0 dropped (the seed becomes certain-only)', replace_once(mod, H0, H0.replace(
        ' (h0 : (D.stage i).p e x0 = 0)', '')))
    must_fail('S1', 'eball C.d replaced by chartBody C in the first conclusion',
              replace_once(mod, SEED_CONCL, SEED_CONCL.replace('SharpSeed (eball C.d)', 'SharpSeed (chartBody C)')))
    must_fail('S1', 'hT replaced by True', replace_once(mod, HT, HT.replace('(hT : BoundaryTransitive (chartBody C) G)',
                                                                            '(hT : True)')))
    must_fail('S1', 'a fourth #print axioms line', replace_once(mod, LAST_PRINT, LAST_PRINT +
                                                                 '#print axioms OIBridge.StageSeed.sharpSeed_eball_of_stage\n'))
    must_fail('S1', 'a second import', replace_once(mod, IMPORT_ONLY + '\n', IMPORT_ONLY + '\nimport OIBridge.SharpTests\n'))
    must_fail('N3', 'a sorry', replace_once(mod, '  exact h3\n', '  sorry\n'))
    must_fail('N1', 'a local lemma added (the proofs compose landed theorems only)',
              replace_once(mod, '\nend\n\nend StageSeed', '\ntheorem aux : True := trivial\n\nend\n\nend StageSeed'))
    # S2
    must_fail('S2', 'a local eball shadowing the landed one',
              replace_once(mod, '/-! ### §A', 'def eball (d : ℕ) : Set (Fin d → ℝ) := Set.univ\n\n/-! ### §A'))
    must_fail('S2', 'CompositeInterface opened, so coord becomes ambiguous',
              replace_once(mod, OPEN2, OPEN2.rstrip('\n') + ' CompositeInterface\n'))
    must_fail('S2', 'StageCompletion no longer opened (coord, SCInf no longer resolve)',
              replace_once(mod, 'OrbitNormalization StageCompletion CompletionAction',
                           'OrbitNormalization CompletionAction'))
    # S4
    must_fail('S4', 'K∞-Seed is discharged. in the header',
              replace_once(mod, '  hypothesis is a premise;', '  hypothesis is a premise; K∞-Seed is discharged.'))
    check('M', 'note phrases: a neutral note passes and one claiming OI supplies the test fails',
          not phrase_hits(fixture_note(TOKENS[0])) and phrase_hits('OI supplies the sharp stage test.') == ['OI supplies'])
    # V -- the decision rule
    c0 = rev(D)
    check('M', 'decision rule: the predicted module with standard axioms and the landed controls reads PROVED',
          seed_cell(mod, landed, True, inv) == TOKENS[0])
    check('M', 'decision rule: a broken signature reads NOT-ESTABLISHED',
          seed_cell(replace_once(mod, FIRST, FIRST.replace(' (hSC : SCInf D)', '')), landed, True, inv) == TOKENS[1])
    lm = dict(landed)
    lm['not_scInf_bad'] = [lm['not_scInf_bad'][0], (lm['not_scInf_bad'][1] or '') + ' ∧ True']
    check('M', 'decision rule: a landed control differing at D reads NOT-ESTABLISHED',
          seed_cell(mod, lm, True, inv) == TOKENS[1])
    check('M', 'decision rule: axioms not measured, or outside the three, read NOT-ESTABLISHED',
          seed_cell(mod, landed, False, inv) == TOKENS[1] and seed_cell(mod, landed, None, inv) == TOKENS[1])
    check('M', 'note tokens: exactly the stated token is found',
          note_tokens('Q-SEED: KINF-SEED-PROVED. Outcome KINF-SEED-1-READ.') == ['KINF-SEED-PROVED'] and
          note_tokens('KINF-SEED-NOT-ESTABLISHED') == ['KINF-SEED-NOT-ESTABLISHED'] and
          note_tokens('KINF-SEED-1-READ') == [])
    # axiom expected results (§A.42 item 1)
    log = '\n'.join("'%s' depends on axioms: [propext, Classical.choice, Quot.sound]" % n for n in PRINTS) + \
        '\nBuild completed successfully (3646 jobs).\n'
    ax = axioms_from_log(log, c0)
    check('M', 'axioms: a log with the three standard reports gives a well-formed expected result within the axioms',
          axioms_status(ax, c0)[0] is True)
    check('M', 'axioms: a sorryAx report is outside the three axioms',
          axioms_status(axioms_from_log(log.replace('Quot.sound]', 'Quot.sound, sorryAx]', 1), c0), c0)[0] is False)
    check('M', 'axioms: a missing report fails', axioms_status(axioms_from_log(log.split('\n', 1)[1], c0), c0)[0]
          is False)
    check('M', 'axioms: a log without a successful build fails',
          axioms_status(axioms_from_log(log.replace('Build completed successfully', 'error'), c0), c0)[0] is False)
    check('M', 'axioms: an expected result for another commit fails in exact mode',
          axioms_status(std_axioms('0' * 40), c0)[0] is False and axioms_status(None, c0)[0] is False)
    # outcome registry
    check('M', 'registry: a required check that never ran fails the mode, and a False outcome fails it',
          finalize(['A', 'B'], [('A', True)])[0] is False and finalize(['A'], [('A', False)])[0] is False and
          finalize(['A'], [('A', True)])[0] is True)
    # I, C
    d_imp = show(D, IMPORTS)
    good_imp = d_imp.replace(ANCHOR_IMPORT, ANCHOR_IMPORT + NEW_IMPORT, 1)
    check('M', 'imports: the frozen edit passes; the unchanged file and the line at the end fail',
          imports_ok(d_imp, good_imp) and not imports_ok(d_imp, d_imp) and
          not imports_ok(d_imp, d_imp.rstrip('\n') + '\n' + NEW_IMPORT))
    d_cen = show(D, CENSUS)
    good = census_want(d_cen)
    bad_status = json.loads(good)
    bad_status['families'][-1]['status'] = 'carried'
    check('M', 'census: the frozen edit passes; a changed status, a whitespace change and the unchanged file fail',
          census_ok(d_cen, good) and not census_ok(d_cen, json.dumps(bad_status, indent=2, ensure_ascii=False) + '\n')
          and not census_ok(d_cen, good.replace('\n', '\n ', 1)) and not census_ok(d_cen, d_cen))
    end_to_end(mod)


def end_to_end(mod):
    """The real F, check and verdict modes on real commits D -> F -> C1 -> S1 -> E."""
    here = os.path.dirname(os.path.abspath(__file__))
    try:
        with open(os.path.join(here, 'preregistration.md'), encoding='utf-8') as f:
            prereg = f.read()
    except OSError:
        prereg = None
    expect('the preregistration beside this file is readable', prereg is not None)
    if prereg is None:
        return
    own = own_text()
    pin = git_blob_id(own)
    print('  NOTE  the preregistration beside this file %s this controls.py blob %s'
          % ('pins' if pin in prereg else 'does not yet pin', pin))
    pre_f = prereg if pin in prereg else prereg + '\ncontrols.py blob `%s`\n' % pin
    fx = Fixture()
    try:
        d_imp, d_cen = show(D, IMPORTS), show(D, CENSUS)
        F = fx.commit([D], D, {PREREG: pre_f})
        C1 = fx.commit([F], F, {CONTROLS: own})
        S1 = fx.commit([C1], C1, {MOD: mod, IMPORTS: d_imp.replace(ANCHOR_IMPORT, ANCHOR_IMPORT + NEW_IMPORT, 1),
                                  CENSUS: census_want(d_cen)})
        E = fx.commit([S1], S1, {RESULT: fixture_note(TOKENS[0])})
        print('  NOTE  predicted trees: F %s, S1 %s, E %s' % (git('rev-parse', F + '^{tree}').strip(),
                                                              git('rev-parse', S1 + '^{tree}').strip(),
                                                              git('rev-parse', E + '^{tree}').strip()))
        ax_s1 = std_axioms(S1)
        r = quiet(run_freeze, F)
        expect('end to end: F mode passes on the fixture F (%s %s)' % (r[1], r[2]), r[0])
        r = quiet(run_check, C1, F)
        expect('end to end: check passes at C1 (%s %s)' % (r[1], r[2]), r[0])
        r = quiet(run_check, S1, F)
        expect('end to end: check passes at S1 (%s %s)' % (r[1], r[2]), r[0])
        r = quiet(run_check, E, F, axioms=ax_s1)
        expect('end to end: check passes at E with the S1 axiom expected result (%s %s)' % (r[1], r[2]), r[0])
        r = quiet(run_check, E, F)
        check('M', 'end to end: check at E without an axiom expected result fails V (%s)' % r[1], 'V' in r[1])
        start = len(RESULTS)
        saved = sys.stdout
        sys.stdout = io.StringIO()
        try:
            run_verdict(E, axioms=std_axioms(E))
            out_pos = sys.stdout.getvalue()
            run_verdict(E, axioms=ax_s1)
            out_s1 = sys.stdout.getvalue()
        finally:
            sys.stdout = saved
            del RESULTS[start:]
        check('M', 'end to end: verdict at E with E\'s own standard axioms prints PROVED',
              'VERDICT  Q-SEED  KINF-SEED-PROVED' in out_pos)
        check('M', 'end to end: verdict at E with S1\'s expected result (not exact-head) prints NOT-ESTABLISHED',
              out_s1.count('VERDICT  Q-SEED  KINF-SEED-NOT-ESTABLISHED') == 1)
        # negative fixtures through the real modes
        Fm = fx.commit([D], D, {PREREG: pre_f, CONTROLS: own})
        check('M', 'end to end: an F that also adds controls.py fails F', 'F' in quiet(run_freeze, Fm)[1])
        Fx = fx.commit([D, rev(D + '^')], D, {PREREG: pre_f})
        check('M', 'end to end: an F with two parents fails F', 'F' in quiet(run_freeze, Fx)[1])
        Fu = fx.commit([D], D, {PREREG: prereg.replace(pin, '')}) if pin in prereg else \
            fx.commit([D], D, {PREREG: prereg})
        check('M', 'end to end: an F that does not pin this controls.py fails K', 'K' in quiet(run_freeze, Fu)[1])
        Fg = fx.commit([D], D, {PREREG: pre_f.replace('execution M verification/lean-manuscript-census.json\n', '')})
        check('M', 'end to end: an F with a governed path dropped fails F', 'F' in quiet(run_freeze, Fg)[1])
        Ee = fx.commit([E], E, {RDIR + 'evidence/axioms.json': '{}\n'})
        check('M', 'end to end: an evidence file in the record directory fails R (the record control as frozen; see '
                   'AGENTS §A.42 item 2)', 'R' in quiet(run_check, Ee, F, axioms=ax_s1)[1])
        Em = fx.commit([E], E, {'papers/Main.md': (show(D, 'papers/Main.md') or '') + '\nx\n'})
        check('M', 'end to end: a manuscript change fails G', 'G' in quiet(run_check, Em, F, axioms=ax_s1)[1])
        Er = fx.commit([E], E, {RECEIPT: '{}\n'})
        check('M', 'end to end: a receipt before Q fails G', 'G' in quiet(run_check, Er, F, axioms=ax_s1)[1])
        Ep = fx.commit([E], E, {PREREG: pre_f + '\nlate edit\n'})
        check('M', 'end to end: a preregistration changed after F fails F', 'F' in quiet(run_check, Ep, F,
                                                                                         axioms=ax_s1)[1])
        En = fx.commit([S1, D], S1, {RESULT: fixture_note(TOKENS[0])})
        check('M', 'end to end: a merge between S1 and E fails L', 'L' in quiet(run_check, En, F, axioms=ax_s1)[1])
        Ec = fx.commit([E], E, {CONTROLS: own + '\n# edited\n'})
        check('M', 'end to end: controls.py changed after C1 fails K', 'K' in quiet(run_check, Ec, F,
                                                                                    axioms=ax_s1)[1])
        Ew = fx.commit([S1], S1, {RESULT: fixture_note(TOKENS[1])})
        check('M', 'end to end: a note stating the other token fails V', 'V' in quiet(run_check, Ew, F,
                                                                                      axioms=ax_s1)[1])
        Ex = fx.commit([S1], S1, {RESULT: fixture_note(TOKENS[0]).replace(NONINF, 'Nothing is claimed.')})
        check('M', 'end to end: a note without the frozen non-inference rule fails V',
              'V' in quiet(run_check, Ex, F, axioms=ax_s1)[1])
        Ea = fx.commit([S1], S1, {RESULT: fixture_note(TOKENS[0]) + '\nK∞-Seed is discharged.\n'})
        check('M', 'end to end: a note with a frozen phrase fails S4', 'S4' in quiet(run_check, Ea, F,
                                                                                     axioms=ax_s1)[1])
        S1b = fx.commit([C1], C1, {MOD: replace_once(mod, FIRST, FIRST.replace(' (hSC : SCInf D)', '')),
                                   IMPORTS: d_imp.replace(ANCHOR_IMPORT, ANCHOR_IMPORT + NEW_IMPORT, 1),
                                   CENSUS: census_want(d_cen)})
        check('M', 'end to end: a broken signature at S1 fails S1', 'S1' in quiet(run_check, S1b, F)[1])
        S1i = fx.commit([C1], C1, {MOD: mod, IMPORTS: d_imp, CENSUS: census_want(d_cen)})
        check('M', 'end to end: an S1 without the import line is refused as a stage (G)',
              'G' in quiet(run_check, S1i, F)[1])
    finally:
        fx.close()


def main(argv):
    if argv == ['--self-test']:
        self_test()
        n = len(RESULTS)
        req = ['T', 'M']
        expect('the self-test recorded the frozen number of checks (%d of %d)' % (n, SELF_TEST_RECORDS),
               n == SELF_TEST_RECORDS)
    elif len(argv) == 2 and argv[0] == 'freeze':
        req = run_freeze(argv[1])
    elif len(argv) in (4, 6) and argv[0] == 'check' and argv[2] == '--freeze' and \
            (len(argv) == 4 or argv[4] == '--axioms'):
        req = run_check(argv[1], argv[3], argv[5] if len(argv) == 6 else None)
    elif len(argv) in (2, 4) and argv[0] == 'verdict' and (len(argv) == 2 or argv[2] == '--axioms'):
        req = run_verdict(argv[1], argv[3] if len(argv) == 4 else None)
    elif len(argv) in (3, 7) and argv[0] == 'axioms-from-log':
        with open(argv[1], encoding='utf-8') as f:
            text = f.read()
        run = job = None
        if len(argv) == 7 and argv[3] == '--run' and argv[5] == '--job':
            run, job = int(argv[4]), int(argv[6])
        elif len(argv) == 7:
            print(__doc__)
            return 2
        print(json.dumps(axioms_from_log(text, argv[2], run, job), indent=2, sort_keys=True))
        return 0
    else:
        print(__doc__)
        print('controls: refused -- unknown mode or arguments: %s' % ' '.join(argv))
        return 2
    ok, failed, missing = finalize(req)
    if not ok:
        print('controls: FAILED (%d records; failed %s; never ran %s)' % (len(RESULTS), failed, missing))
        return 1
    print('controls: OK -- %d checks' % len(RESULTS))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
