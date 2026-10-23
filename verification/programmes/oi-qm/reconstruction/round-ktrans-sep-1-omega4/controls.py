#!/usr/bin/env python3
"""controls.py -- round KTRANS-SEP-1's own controls, frozen with the preregistration beside it.

Imports nothing from the repository and changes nothing. It reads D and the commits it is given through read-only git
commands, embeds every frozen text it compares against, and runs the frozen probe from a temporary copy of its blob.
Standard library only; the probe it runs needs sympy 1.14.0.

    python3 -I -B controls.py check <commit> [--freeze F] [--stage S1] [--log LOG [--log-meta META]]
    python3 -I -B controls.py verdict <commit> --freeze F --log LOG [--log-meta META]
    python3 -I -B controls.py exact
    python3 -I -B controls.py --self-test

`check` runs every control below at <commit>. With --freeze it adds T and the retention checks that need F; without
it (the predicted execution tree) those are skipped and a pending pin is allowed. --stage S1 is the commit before the
result note; the default stage is E, at which the result note is required when --freeze is given. LOG is the served
text of the Mathlib bridge job of the exact-head run at <commit>; it is required at a commit carrying the result note.
META is a JSON object {"original_lines": N, "served_lines": M} for that text, from the tool that served it.

`verdict` runs `check` first and prints the three cell tokens only when every control of `check` ran and passed and
the evidence the cells read is complete; otherwise it prints `VERDICT  VOID` with the reason, prints no token and exits
1. VOID is not an outcome: a tooling failure or incomplete evidence never yields a NOT-ESTABLISHED token.
`exact` runs the independent exact layer (X, CX) alone.

Controls (each prints PASS or FAIL with its code):
  G   governed   delta(D, commit) is exactly the five execution paths, with their statuses, plus record files
  R   record     the record directory holds only the preregistration, controls.py, the pinned evidence, F's run
                 (required with --freeze), amendments/ and, at E, the result note
  P   pins       every evidence file the preregistration's retained-evidence table pins is present with its sha256;
                 the table names at least the four required files; with --freeze no pin is pending; each pinned
                 file is a structured result with its form stated and no timestamp or duration field; the predicted
                 tree's run result and F's run result name their heads, are green and place the module's build
                 line, its fifteen reports and the gate inside the served window, in that order
  T   chain      (with --freeze) D..commit is one chain of single-parent commits through F; delta(D, F) is the
                 preregistration and amendments only; the preregistration at commit is F's
  B   blobs      the probe is the frozen blob; controls.py at commit is the file running
  N1  decls      the module declares exactly the 36 frozen declarations, in order and by kind
  N2  surface    the module, with each theorem's proof elided, is the frozen skeleton: preamble, docstrings,
                 every definition whole, every theorem statement up to `:=`, the context lines and the prints
  N3  hygiene    no sorry, admit, axiom or opaque declaration, native_decide, implemented_by, extern or unsafe
  S1  statements omega4, not_affine_eball_omega4, not_boundaryTransitive_omega4, not_denseBoundaryOrbit_omega4 and
                 kinfTrans_separation have their frozen texts (the cells' load-bearing statements)
  S2  resolution the landed declarations the module uses have their frozen texts at D, each declared exactly once in
                 the module's import closure; the module imports only OIBridge.DenseOrbit, opens the frozen
                 namespaces, and declares no name that its import closure declares
  S3  ball       the kernel's support for CX1 at D: sharpEff_sharpSeed, fullAut, preservesBody_fullAut and
                 boundaryTransitive_fullAut have their frozen texts (on eball d a sharp seed and a body-preserving
                 boundary-transitive family)
  S4  phrases    the module header and, at a commit carrying it, the result note outside its two frozen texts
                 contain none of the frozen phrases (case-insensitive, backticks removed, whitespace-normalized)
  S5  prints     exactly the 15 frozen `#print axioms` lines, in order and distinct, each naming a module theorem
  X1  points     the eight states of the module's non-ellipsoid argument lie in Omega4 and the eight points lie
                 outside it, exactly
  X2  certificate the sixteen inequalities are infeasible: the frozen positive weights cancel every coefficient and
                 the constant, exactly (a Farkas certificate)
  X3  transcription the sixteen points X1 and X2 use are the ones the module's proof of not_affine_eball_omega4 states
  CX1 ball       countercontrol, non-ellipsoidality dropped: on the Euclidean 4-ball the named properties hold at
                 exact instances, the same system with the ball's states is feasible, and S3's landed family is
                 boundary transitive
  CX2 preserve   countercontrol, PreservesBody dropped: translations carry each boundary point of a list to each
                 other, and each nonzero one moves a state of Omega4 out of Omega4
  CX3 compact    countercontrol, IsCompact dropped: the half-space {s <= 1} with its boundary translations
  CX4 interior   countercontrol, nonempty interior dropped: the segment [-e0, e0] with {id, -id}
  I   imports    OIBridge.lean is D's with the frozen import line after `import OIBridge.TurnpikePremiseOrientation`
  C   census     the census is D's with the frozen family after BG-2's family, in D's layout
  W   workflow   verify.yml is D's with exactly the five frozen splices
  V   note       at a commit carrying the result note: exactly the computed tokens, the earned reading exactly when
                 all three cells are positive, the non-inference rule always

Cells (verdict), read only when every control passed:
  VOID      the log is empty or its metadata does not describe it; a frozen report is missing, duplicated, at another
            line or unparsable; the module's build line is not in the served window before its reports; the build or
            gate evidence is incomplete or fails outside the module; sympy 1.14.0 is absent; the probe did not run to
            completion, or its output differs from the frozen output without a failing check. No token is printed.
  Q-NONELL  KTRANS-SEP-NONELLIPSOID-PROVED   the build line, the gate's PASS verdict, and every frozen report within
            [propext, Classical.choice, Quot.sound], with S1 holding for not_affine_eball_omega4
  Q-CEX     KTRANS-SEP-COUNTEREXAMPLE-PROVED  the same, with S1 holding for the four statements and omega4
            Both kernel cells read NOT-ESTABLISHED only from complete evidence of a failure in the module: a report
            outside the three axioms with the gate failing at lean-axioms alone, or with a build error in the module
  Q-EXACT   KTRANS-SEP-INSTANCES-EXACT       the probe blob at <commit>, run under sympy 1.14.0 with python3 -I -B,
            prints exactly the frozen output (sha256 below), whose lines include the twelve PASS lines, both COUNTER
            lines, the summary and the verdict; NOT-ESTABLISHED from a complete run in which a check failed
No cell reads another cell's outcome.
"""
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
from fractions import Fraction as Fr
from itertools import product

D = 'ec36234cb98a30ecb4681e118ff9ccb82e19aa6d'
RDIR = 'verification/programmes/oi-qm/reconstruction/round-ktrans-sep-1-omega4/'
PREREG = RDIR + 'preregistration.md'
CONTROLS = RDIR + 'controls.py'
RESULT = RDIR + 'result.md'
FRUN = RDIR + 'evidence/f-run/results.json'
MOD = 'verification/lean-mathlib/OIBridge/TransSeparation.lean'
PROBE = 'verification/lean/ktrans_sep1_probe.py'
IMPORTS = 'verification/lean-mathlib/OIBridge.lean'
CENSUS = 'verification/lean-manuscript-census.json'
WORKFLOW = '.github/workflows/verify.yml'
EXEC = {MOD: 'A', PROBE: 'A', IMPORTS: 'M', CENSUS: 'M', WORKFLOW: 'M'}
REQUIRED_EVIDENCE = ['evidence/design-run-1.json', 'evidence/design-run-2.json', 'evidence/exact-replay.json',
                     'evidence/predicted-tree-run.json']
ALLOWED_AXIOMS = {'propext', 'Classical.choice', 'Quot.sound'}
ANCHOR_IMPORT = 'import OIBridge.TurnpikePremiseOrientation\n'
NEW_IMPORT = 'import OIBridge.TransSeparation\n'
PREV_FAMILY_MODULES = ['TurnpikePremiseOrientation']
NS = 'OIBridge.TransSeparation.'
KEY = ('omega4', 'not_affine_eball_omega4', 'not_boundaryTransitive_omega4', 'not_denseBoundaryOrbit_omega4',
       'kinfTrans_separation')
NONELL_KEY = ('not_affine_eball_omega4',)
TOK_NONELL = ('KTRANS-SEP-NONELLIPSOID-PROVED', 'KTRANS-SEP-NONELLIPSOID-NOT-ESTABLISHED')
TOK_CEX = ('KTRANS-SEP-COUNTEREXAMPLE-PROVED', 'KTRANS-SEP-COUNTEREXAMPLE-NOT-ESTABLISHED')
TOK_EXACT = ('KTRANS-SEP-INSTANCES-EXACT', 'KTRANS-SEP-INSTANCES-NOT-ESTABLISHED')
ALL_TOKENS = TOK_NONELL + TOK_CEX + TOK_EXACT
PREAMBLE_IMPORTS = ['import OIBridge.DenseOrbit']
OPEN_LINE = 'open Set KInfFoundations OrbitGeneration TransitiveBody DenseOrbit'
HYGIENE = re.compile(r'\bsorry\b|\badmit\b|^\s*(?:private |protected )?(?:axiom|opaque)\s|native_decide|'
                     r'implemented_by|@\[extern|\bunsafe\b', re.M)
PHRASES = ('other single-system seams', 'single-system', 'chart dimension 4', 'every compact convex body', 'all compact convex bodies',
           'every body', 'all bodies', 'any compact convex body', 'is not implied by', 'are not implied by',
           'oi supplies', 'oi provides', 'k∞-trans is false', 'transitivity fails for oi', 'replaces k∞-trans',
           'k∞-trans is not needed', 'k∞-trans is independent', 'independent of k∞-trans', 'k∞-stage', 'k∞-act',
           'k∞-v4', 'chart dimension 3', 'in dimension three', 'kernel proof of', 'design module', 'not for merge',
           'not adopted', 'disposable branch', ' iff ', 'if and only if', 'is equivalent to', 'are equivalent',
           'exactly when')
EARNED = ('Earned reading: Omega4 = {(x, s) in R^3 x R : |x|^4 + s^4 <= 1} is compact, convex and has nonempty '
          'interior, satisfies ElementaryDrivability, carries the sharp seed seed4, and is RelStrictConvex and '
          'CentrallySymmetric about 0; no body-preserving family of affine equivalences of R^4 is BoundaryTransitive '
          'or has a DenseBoundaryOrbit on Omega4 (kinfTrans_separation). Omega4 is therefore a counterexample to the '
          'implication from these properties, for body-preserving families, to BoundaryTransitive and to '
          'DenseBoundaryOrbit.')
NONINF = ('Non-inference rule: the round concerns Omega4 alone, in R^4. It states nothing about other compact convex '
          'bodies, about chart dimension 3, about K-infinity-Stage, K-infinity-Act, K-infinity-V4 or K-infinity-Copy, '
          'about the composite, or about which bodies OI supplies. The Euclidean 4-ball is countercontrol CX1: the '
          'kernel gives it a sharp seed (sharpEff_sharpSeed) and a body-preserving boundary-transitive family '
          '(preservesBody_fullAut, boundaryTransitive_fullAut), and CX1 checks its drive maps, central symmetry and '
          'strict midpoints at finitely many exact states; the kernel has no ElementaryDrivability (eball 4) or '
          'RelStrictConvex (eball 4) theorem, so CX1 is a finite exact check, not a theorem. Drivability fails on the '
          'interval [-1, 1] (not_drivable_Icc), and nothing is stated for dimension 2. RelStrictConvex is the form in '
          'which the kernel gives singleton faces for every effect family; it is not a frozen statement of '
          'K-infinity-Geom. Supporting-effect completeness of the full effects on Omega4 is an exact identity with a '
          'written step, not a kernel theorem of this round. The exact layer is an exact computation, not a Lean '
          'kernel proof.')

# ---- generated from the frozen module, the frozen probe and D (see the preregistration) --------------------------
GEN = json.loads(r'''{
 "ball": {
  "boundaryTransitive_fullAut": {
   "module": "EffectSpace",
   "text": "theorem boundaryTransitive_fullAut : BoundaryTransitive (eball d) (fullAut d)"
  },
  "fullAut": {
   "module": "EffectSpace",
   "text": "def fullAut (d : ℕ) : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ)) :=\n  {g | ∀ x ∈ eball d, g x ∈ eball d ∧ g.symm x ∈ eball d}"
  },
  "preservesBody_fullAut": {
   "module": "EffectSpace",
   "text": "theorem preservesBody_fullAut : PreservesBody (eball d) (fullAut d)"
  },
  "sharpEff_sharpSeed": {
   "module": "EffectSpace",
   "text": "theorem sharpEff_sharpSeed {b : Fin d → ℝ} (hb : ∑ j, b j ^ 2 = 1) :\n    SharpSeed (eball d) (sharpEff b)"
  }
 },
 "census_family": {
  "manuscript": [],
  "modules": [
   "TransSeparation"
  ],
  "name": "Ω₄, the ℓ⁴-sum of the Euclidean 3-ball and the segment, is compact, convex, with interior, drivable, with a sharp seed, relatively strictly convex and centrally symmetric, is no affine image of the Euclidean ball, and admits no body-preserving family that is boundary transitive or has a dense boundary orbit (round KTRANS-SEP-1, reconstruction)",
  "status": "kernel-only"
 },
 "closure_modules": [
  "AntiunitaryInvariance",
  "BohrFrequency",
  "CoherentExtension",
  "CoherentLift",
  "CompletionAction",
  "CompositeDimension",
  "CompositeInterface",
  "CongruentReconstruction",
  "ControlledQuotient",
  "CycleFibreHull",
  "DenseOrbit",
  "DomainGlue",
  "DynamicsGlue",
  "EdgeRigidity",
  "EffectSpace",
  "FrequencyMatching",
  "HomometricKill",
  "HomometricSix",
  "InvariantInnerProduct",
  "K1Bridge",
  "K2Guard",
  "KInfFoundations",
  "NativeGateBall",
  "ObservabilityQuotient",
  "OrbitGeneration",
  "OrbitNormalization",
  "PassiveQuotient",
  "ShellAssignment",
  "StageCompletion",
  "ThermalOrientation",
  "TransitiveBody"
 ],
 "decls": [
  [
   "def",
   "omega4"
  ],
  [
   "theorem",
   "mem_omega4"
  ],
  [
   "theorem",
   "vec4_ext"
  ],
  [
   "theorem",
   "omega4_isCompact"
  ],
  [
   "theorem",
   "conv_core"
  ],
  [
   "theorem",
   "omega4_convex"
  ],
  [
   "theorem",
   "abstract_strict"
  ],
  [
   "theorem",
   "omega4_strictConvex"
  ],
  [
   "theorem",
   "relStrictConvex_omega4"
  ],
  [
   "theorem",
   "singletonFaces_omega4"
  ],
  [
   "theorem",
   "omega4_interior_nonempty"
  ],
  [
   "theorem",
   "omega4_centrallySymmetric"
  ],
  [
   "def",
   "seed4"
  ],
  [
   "theorem",
   "seed4_apply"
  ],
  [
   "theorem",
   "sharpSeed_omega4"
  ],
  [
   "def",
   "rotFun4"
  ],
  [
   "theorem",
   "rotFun4_apply"
  ],
  [
   "theorem",
   "rotFun4_zero"
  ],
  [
   "theorem",
   "rotFun4_add"
  ],
  [
   "theorem",
   "rotFun4_mem_omega4"
  ],
  [
   "def",
   "rotLin4"
  ],
  [
   "def",
   "rotEquiv4"
  ],
  [
   "def",
   "rot4"
  ],
  [
   "theorem",
   "rot4_apply"
  ],
  [
   "def",
   "cycEquiv4"
  ],
  [
   "def",
   "cyc4"
  ],
  [
   "theorem",
   "cyc4_apply"
  ],
  [
   "theorem",
   "cyc4_symm_apply"
  ],
  [
   "theorem",
   "cyc4_mem_omega4"
  ],
  [
   "theorem",
   "cyc4_symm_mem_omega4"
  ],
  [
   "def",
   "omega4Drive"
  ],
  [
   "theorem",
   "omega4_drivable"
  ],
  [
   "theorem",
   "not_affine_eball_omega4"
  ],
  [
   "theorem",
   "not_boundaryTransitive_omega4"
  ],
  [
   "theorem",
   "not_denseBoundaryOrbit_omega4"
  ],
  [
   "theorem",
   "kinfTrans_separation"
  ]
 ],
 "keytext": {
  "kinfTrans_separation": "theorem kinfTrans_separation :\n    IsCompact omega4 ∧ Convex ℝ omega4 ∧ (interior omega4).Nonempty\n      ∧ Nonempty (ElementaryDrivability omega4) ∧ SharpSeed omega4 seed4\n      ∧ RelStrictConvex omega4 ∧ CentrallySymmetric omega4 0\n      ∧ ∀ G : Set ((Fin 4 → ℝ) ≃ᵃ[ℝ] (Fin 4 → ℝ)), PreservesBody omega4 G →\n          ¬ BoundaryTransitive omega4 G ∧ ¬ DenseBoundaryOrbit omega4 G",
  "not_affine_eball_omega4": "theorem not_affine_eball_omega4 :\n    ¬ ∃ A : (Fin 4 → ℝ) ≃ᵃ[ℝ] (Fin 4 → ℝ), A '' omega4 = eball 4",
  "not_boundaryTransitive_omega4": "theorem not_boundaryTransitive_omega4 {G : Set ((Fin 4 → ℝ) ≃ᵃ[ℝ] (Fin 4 → ℝ))}\n    (hG : PreservesBody omega4 G) : ¬ BoundaryTransitive omega4 G",
  "not_denseBoundaryOrbit_omega4": "theorem not_denseBoundaryOrbit_omega4 {G : Set ((Fin 4 → ℝ) ≃ᵃ[ℝ] (Fin 4 → ℝ))}\n    (hG : PreservesBody omega4 G) : ¬ DenseBoundaryOrbit omega4 G",
  "omega4": "def omega4 : Set (Fin 4 → ℝ) := {v | (v 0 ^ 2 + v 1 ^ 2 + v 2 ^ 2) ^ 2 + v 3 ^ 4 ≤ 1}"
 },
 "landed": {
  "BoundaryTransitive": {
   "module": "OrbitGeneration",
   "text": "def BoundaryTransitive (Ω : Set V) (G : Set (V ≃ᵃ[ℝ] V)) : Prop :=\n  ∀ x y, IsBoundaryState Ω x → IsBoundaryState Ω y → ∃ g ∈ G, g x = y"
  },
  "CentrallySymmetric": {
   "module": "KInfFoundations",
   "text": "def CentrallySymmetric (Ω : Set V) (c : V) : Prop :=\n  ∀ x ∈ Ω, c + (c - x) ∈ Ω"
  },
  "DenseBoundaryOrbit": {
   "module": "DenseOrbit",
   "text": "def DenseBoundaryOrbit {V : Type} [NormedAddCommGroup V] [NormedSpace ℝ V] (Ω : Set V)\n    (G : Set (V ≃ᵃ[ℝ] V)) : Prop :=\n  ∀ x y, IsBoundaryState Ω x → IsBoundaryState Ω y → y ∈ closure ((fun g : V ≃ᵃ[ℝ] V => g x) '' G)"
  },
  "ElementaryDrivability": {
   "module": "KInfFoundations",
   "text": "structure ElementaryDrivability (Ω : Set V) where\n  flow : ℝ → V ≃ᵃ[ℝ] V\n  flow_zero : flow 0 = AffineEquiv.refl ℝ V\n  flow_add : ∀ s t, flow (s + t) = (flow t).trans (flow s)\n  flow_continuous : Continuous fun q : ℝ × V => flow q.1 q.2\n  flow_preserves : ∀ t, ∀ x ∈ Ω, flow t x ∈ Ω\n  t₀ : ℝ\n  N_involutive : ∀ x ∈ Ω, flow t₀ (flow t₀ x) = x\n  N_moves : ∃ x ∈ Ω, flow t₀ x ≠ x\n  J : V ≃ᵃ[ℝ] V\n  J_preserves : ∀ x ∈ Ω, J x ∈ Ω\n  J_symm_preserves : ∀ x ∈ Ω, J.symm x ∈ Ω\n  J_off_axis : ∃ t, ∀ s, ∃ x ∈ Ω, J (flow t (J.symm x)) ≠ flow s x"
  },
  "IsBoundaryState": {
   "module": "KInfFoundations",
   "text": "def IsBoundaryState (Ω : Set V) (x : V) : Prop :=\n  x ∈ Ω ∧ ∃ y ∈ Ω, ∀ ε : ℝ, 0 < ε → x + ε • (x - y) ∉ Ω"
  },
  "PreservesBody": {
   "module": "OrbitGeneration",
   "text": "def PreservesBody (Ω : Set V) (G : Set (V ≃ᵃ[ℝ] V)) : Prop :=\n  ∀ g ∈ G, ∀ x ∈ Ω, g x ∈ Ω ∧ g.symm x ∈ Ω"
  },
  "RelStrictConvex": {
   "module": "KInfFoundations",
   "text": "def RelStrictConvex (Ω : Set V) : Prop :=\n  ∀ x ∈ Ω, ∀ y ∈ Ω, x ≠ y → ∀ a b : ℝ, 0 < a → 0 < b → a + b = 1 →\n    a • x + b • y ∈ Ω ∧ ¬ IsBoundaryState Ω (a • x + b • y)"
  },
  "SharpSeed": {
   "module": "OrbitGeneration",
   "text": "def SharpSeed (Ω : Set V) (r : V →ᵃ[ℝ] ℝ) : Prop :=\n  IsEffectOn Ω r ∧ (∃ x ∈ Ω, r x = 1) ∧ (∃ y ∈ Ω, r y = 0)"
  },
  "SingletonFaces": {
   "module": "KInfFoundations",
   "text": "def SingletonFaces (Ω : Set V) (avail : Set (V →ᵃ[ℝ] ℝ)) : Prop :=\n  ∀ e ∈ avail, IsEffectOn Ω e → IsProperOn Ω e → (certainFace Ω e).Subsingleton"
  },
  "eball": {
   "module": "TransitiveBody",
   "text": "def eball (d : ℕ) : Set (Fin d → ℝ) := {x | ∑ j, x j ^ 2 ≤ 1}"
  },
  "exists_affine_image_eq_eball": {
   "module": "TransitiveBody",
   "text": "theorem exists_affine_image_eq_eball (hd : 0 < d) {Ω : Set (Fin d → ℝ)} (hc : IsCompact Ω)\n    (hconv : Convex ℝ Ω) (hi : (interior Ω).Nonempty) {G : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ))}\n    (hG : PreservesBody Ω G) (hT : BoundaryTransitive Ω G) :\n    ∃ A : (Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ), A '' Ω = eball d"
  },
  "exists_affine_image_eq_eball_of_dense": {
   "module": "DenseOrbit",
   "text": "theorem exists_affine_image_eq_eball_of_dense (hd : 0 < d) {Ω : Set (Fin d → ℝ)} (hc : IsCompact Ω)\n    (hconv : Convex ℝ Ω) (hi : (interior Ω).Nonempty) {G : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ))}\n    (hG : PreservesBody Ω G) (hT : DenseBoundaryOrbit Ω G) :\n    ∃ A : (Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ), A '' Ω = eball d"
  },
  "relStrictConvex_of_strictConvex": {
   "module": "KInfFoundations",
   "text": "theorem relStrictConvex_of_strictConvex {Ω : Set V} (h : StrictConvex ℝ Ω) :\n    RelStrictConvex Ω"
  },
  "singletonFaces_of_relStrictConvex": {
   "module": "KInfFoundations",
   "text": "theorem singletonFaces_of_relStrictConvex {Ω : Set V} (avail : Set (V →ᵃ[ℝ] ℝ))\n    (h : RelStrictConvex Ω) : SingletonFaces Ω avail"
  }
 },
 "mod_blob": "ba7431915e7ab6e8f7bdfb6ab980f16067e9331b",
 "prints": [
  "omega4_isCompact",
  "conv_core",
  "omega4_convex",
  "abstract_strict",
  "omega4_strictConvex",
  "relStrictConvex_omega4",
  "singletonFaces_omega4",
  "omega4_interior_nonempty",
  "omega4_centrallySymmetric",
  "sharpSeed_omega4",
  "omega4_drivable",
  "not_affine_eball_omega4",
  "not_boundaryTransitive_omega4",
  "not_denseBoundaryOrbit_omega4",
  "kinfTrans_separation"
 ],
 "probe_blob": "19e19f28fa7644de0bcc3089a354317310de3e41",
 "probe_lines": [
  "PASS D1 the flow preserves F identically",
  "PASS D2 flow_zero and flow_add (R_z(t) R_z(u) = R_z(t+u))",
  "PASS D3 N = flow(pi) is an involution and moves e0 in Omega4",
  "PASS D4 J and J^-1 preserve F identically",
  "PASS D5 J_off_axis at t = pi/2, x = e1: J flow(pi/2) J^-1 e1 = e2, flow(s) e1 has zero third coordinate",
  "PASS D6 seed (1+s)/2: s^4 <= F gives |s| <= 1 on Omega4; values 1 and 0 at (0,0,0,+-1) in Omega4",
  "PASS D7 F(-v) = F(v) (central symmetry; capacity <= 2 by Lemma D)",
  "PASS D8 9 exact boundary points; every midpoint of a distinct pair has F < 1 (max 169/225)",
  "PASS D9 the section {u^4 + v^4 <= 1} is not {A u^2 + 2 B u v + C v^2 <= 1}: the boundary-point system has no solution",
  "PASS C1 ball4: D1-D5 hold and the section system is consistent (B = 0) -- solution [{A: 1, B: 0, C: 1, tau: 1/2}]",
  "PASS W5 SEC for the full effects: Euler identity, gradient gap = explicit sum of squares, 11 exact boundary points, grid of 1669 states -- euler True, sos True, points True, grid True",
  "PASS C2 ball4: grad F(p).p = 2 F(p) and the gradient gap is |y - p|^2",
  "COUNTER XW1 fails as stated -- the sum of squares without 2|p_x|^2|y_x - p_x|^2 is not an identity",
  "COUNTER XW2 fails as stated -- |p1|^2 = 7/5, F(y*) = 388962/390625, e'(p1) = 1: True, p1.y*/|p1|^2 = 3*sqrt(15)/25 + 6*sqrt(5)/25 > 1 (3 b^2 = 3888/15625 > a^2 = 3844/15625)",
  "checks: 12, failures: 0",
  "VERDICT DRIVE-SEED-GEOM-SEC-CAP2-NOT-TRANS"
 ],
 "probe_out_sha256": "d6f6d298d3ed57081f4e81bef267771fc81d8083a111c0414a69216c772a2940",
 "skeleton": [
  "/-\n  OIBridge/TransSeparation.lean — round KTRANS-SEP-1 (reconstruction): a convex body in ℝ⁴ with\n  the named kernel properties on which no body-preserving family is boundary transitive.\n\n  Ω₄ = {(x, s) ∈ ℝ³ × ℝ : ‖x‖⁴ + s⁴ ≤ 1}, written on `Fin 4 → ℝ` with `s` the last coordinate\n  (`omega4`). It is compact, convex and has interior; it is centrally symmetric about `0`; it is\n  strictly convex, hence relatively strictly convex (`relStrictConvex_of_strictConvex`), hence has\n  singleton faces for every effect family; it carries the sharp seed `v ↦ (1 + v 3)/2` and an\n  elementary drive: the rotations of the first two coordinates as the flow, the half-turn as the NOT,\n  the cyclic permutation of the first three coordinates as `J` (`omega4Drive`).\n\n  Ω₄ is not an affine image of the Euclidean ball (`not_affine_eball_omega4`): in the plane of the\n  first and last axes, no quadric contains the eight states `(±1, 0)`, `(0, ±1)`, `(±5/6, ±5/6)` and\n  excludes the eight points `(±1, ±1/2)`, `(±1/2, ±1)`. By TRB-1's `exists_affine_image_eq_eball` and\n  KTRANS-DENSE-1's `exists_affine_image_eq_eball_of_dense`, no body-preserving family on Ω₄ is\n  boundary transitive or has a dense boundary orbit (`not_boundaryTransitive_omega4`,\n  `not_denseBoundaryOrbit_omega4`). `kinfTrans_separation` collects these facts: Ω₄ is a\n  counterexample to the implication from `IsCompact`, `Convex`, nonempty interior,\n  `ElementaryDrivability`, `SharpSeed`, `RelStrictConvex` and `CentrallySymmetric` to\n  `BoundaryTransitive` and to `DenseBoundaryOrbit` for body-preserving families. The statements\n  concern Ω₄ alone, in ℝ⁴.\n\n  Supporting-effect completeness of the full effects on Ω₄ is not proved here.\n\n  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build\n-/",
  "import OIBridge.DenseOrbit",
  "namespace OIBridge",
  "namespace TransSeparation",
  "open Set KInfFoundations OrbitGeneration TransitiveBody DenseOrbit",
  "noncomputable section",
  "/-! ### §A — the body -/",
  "/-- Ω₄: the ℓ⁴-sum of the Euclidean 3-ball and the segment. -/",
  "def omega4 : Set (Fin 4 → ℝ) := {v | (v 0 ^ 2 + v 1 ^ 2 + v 2 ^ 2) ^ 2 + v 3 ^ 4 ≤ 1}",
  "theorem mem_omega4 (v : Fin 4 → ℝ) :\n    v ∈ omega4 ↔ (v 0 ^ 2 + v 1 ^ 2 + v 2 ^ 2) ^ 2 + v 3 ^ 4 ≤ 1 := <proof>",
  "theorem vec4_ext {v w : Fin 4 → ℝ} (h0 : v 0 = w 0) (h1 : v 1 = w 1) (h2 : v 2 = w 2)\n    (h3 : v 3 = w 3) : v = w := <proof>",
  "theorem omega4_isCompact : IsCompact omega4 := <proof>",
  "/-- The convexity inequality on reals, with `b = 1 - a`. -/",
  "theorem conv_core (a x0 x1 x2 s y0 y1 y2 t : ℝ) (ha : 0 ≤ a) (hb : 0 ≤ 1 - a)\n    (hx : (x0 ^ 2 + x1 ^ 2 + x2 ^ 2) ^ 2 + s ^ 4 ≤ 1)\n    (hy : (y0 ^ 2 + y1 ^ 2 + y2 ^ 2) ^ 2 + t ^ 4 ≤ 1) :\n    ((a * x0 + (1 - a) * y0) ^ 2 + (a * x1 + (1 - a) * y1) ^ 2 + (a * x2 + (1 - a) * y2) ^ 2) ^ 2\n      + (a * s + (1 - a) * t) ^ 4 ≤ 1 := <proof>",
  "theorem omega4_convex : Convex ℝ omega4 := <proof>",
  "/-- The strict inequality behind strict convexity, on abstract reals. -/",
  "theorem abstract_strict (a X Y S T D E : ℝ) (ha : 0 < a) (hb : 0 < 1 - a)\n    (hz : 0 ≤ a * X + (1 - a) * Y - a * (1 - a) * D)\n    (hw : 0 ≤ a * S + (1 - a) * T - a * (1 - a) * E)\n    (hD : 0 ≤ D) (hE : 0 ≤ E) (hDE : 0 < D + E)\n    (hx : X ^ 2 + S ^ 2 ≤ 1) (hy : Y ^ 2 + T ^ 2 ≤ 1) :\n    (a * X + (1 - a) * Y - a * (1 - a) * D) ^ 2 + (a * S + (1 - a) * T - a * (1 - a) * E) ^ 2\n      < 1 := <proof>",
  "/-- **Ω₄ is strictly convex.** -/",
  "theorem omega4_strictConvex : StrictConvex ℝ omega4 := <proof>",
  "theorem relStrictConvex_omega4 : RelStrictConvex omega4 := <proof>",
  "theorem singletonFaces_omega4 (avail : Set ((Fin 4 → ℝ) →ᵃ[ℝ] ℝ)) :\n    SingletonFaces omega4 avail := <proof>",
  "theorem omega4_interior_nonempty : (interior omega4).Nonempty := <proof>",
  "theorem omega4_centrallySymmetric : CentrallySymmetric omega4 0 := <proof>",
  "/-! ### §B — the seed -/",
  "/-- The effect `v ↦ (1 + v 3)/2`. -/",
  "noncomputable def seed4 : (Fin 4 → ℝ) →ᵃ[ℝ] ℝ :=\n  AffineMap.const ℝ (Fin 4 → ℝ) (1 / 2 : ℝ) +\n    ((1 / 2 : ℝ) • (LinearMap.proj 3 : (Fin 4 → ℝ) →ₗ[ℝ] ℝ)).toAffineMap",
  "theorem seed4_apply (v : Fin 4 → ℝ) : seed4 v = 1 / 2 + v 3 / 2 := <proof>",
  "theorem sharpSeed_omega4 : SharpSeed omega4 seed4 := <proof>",
  "/-! ### §C — the drive -/",
  "/-- The rotation of the first two coordinates by the angle `t`. -/",
  "noncomputable def rotFun4 (t : ℝ) (v : Fin 4 → ℝ) : Fin 4 → ℝ :=\n  ![Real.cos t * v 0 - Real.sin t * v 1, Real.sin t * v 0 + Real.cos t * v 1, v 2, v 3]",
  "theorem rotFun4_apply (t : ℝ) (v : Fin 4 → ℝ) :\n    rotFun4 t v 0 = Real.cos t * v 0 - Real.sin t * v 1 ∧\n      rotFun4 t v 1 = Real.sin t * v 0 + Real.cos t * v 1 ∧ rotFun4 t v 2 = v 2 ∧\n        rotFun4 t v 3 = v 3 := <proof>",
  "theorem rotFun4_zero (v : Fin 4 → ℝ) : rotFun4 0 v = v := <proof>",
  "theorem rotFun4_add (s t : ℝ) (v : Fin 4 → ℝ) : rotFun4 s (rotFun4 t v) = rotFun4 (s + t) v := <proof>",
  "theorem rotFun4_mem_omega4 (t : ℝ) {v : Fin 4 → ℝ} (hv : v ∈ omega4) : rotFun4 t v ∈ omega4 := <proof>",
  "noncomputable def rotLin4 (t : ℝ) : (Fin 4 → ℝ) →ₗ[ℝ] (Fin 4 → ℝ) where\n  toFun := rotFun4 t\n  map_add' v w := by\n    obtain ⟨a0, a1, a2, a3⟩ := rotFun4_apply t (v + w)\n    obtain ⟨b0, b1, b2, b3⟩ := rotFun4_apply t v\n    obtain ⟨c0, c1, c2, c3⟩ := rotFun4_apply t w\n    apply vec4_ext <;>\n      simp only [Pi.add_apply, a0, a1, a2, a3, b0, b1, b2, b3, c0, c1, c2, c3] <;> ring\n  map_smul' r v := by\n    obtain ⟨a0, a1, a2, a3⟩ := rotFun4_apply t (r • v)\n    obtain ⟨b0, b1, b2, b3⟩ := rotFun4_apply t v\n    apply vec4_ext <;>\n      simp only [Pi.smul_apply, smul_eq_mul, RingHom.id_apply, a0, a1, a2, a3, b0, b1, b2, b3] <;>\n      ring",
  "noncomputable def rotEquiv4 (t : ℝ) : (Fin 4 → ℝ) ≃ₗ[ℝ] (Fin 4 → ℝ) :=\n  { rotLin4 t with\n    invFun := rotFun4 (-t)\n    left_inv := fun v => by\n      show rotFun4 (-t) (rotFun4 t v) = v\n      rw [rotFun4_add, neg_add_cancel, rotFun4_zero]\n    right_inv := fun v => by\n      show rotFun4 t (rotFun4 (-t) v) = v\n      rw [rotFun4_add, add_neg_cancel, rotFun4_zero] }",
  "noncomputable def rot4 (t : ℝ) : (Fin 4 → ℝ) ≃ᵃ[ℝ] (Fin 4 → ℝ) := (rotEquiv4 t).toAffineEquiv",
  "theorem rot4_apply (t : ℝ) (v : Fin 4 → ℝ) : rot4 t v = rotFun4 t v := <proof>",
  "/-- The cyclic permutation of the first three coordinates, `(x, y, z, s) ↦ (z, x, y, s)`. -/",
  "noncomputable def cycEquiv4 : (Fin 4 → ℝ) ≃ₗ[ℝ] (Fin 4 → ℝ) where\n  toFun v := ![v 2, v 0, v 1, v 3]\n  invFun v := ![v 1, v 2, v 0, v 3]\n  map_add' v w := by apply vec4_ext <;> rfl\n  map_smul' r v := by apply vec4_ext <;> rfl\n  left_inv v := by apply vec4_ext <;> rfl\n  right_inv v := by apply vec4_ext <;> rfl",
  "noncomputable def cyc4 : (Fin 4 → ℝ) ≃ᵃ[ℝ] (Fin 4 → ℝ) := cycEquiv4.toAffineEquiv",
  "theorem cyc4_apply (v : Fin 4 → ℝ) :\n    cyc4 v 0 = v 2 ∧ cyc4 v 1 = v 0 ∧ cyc4 v 2 = v 1 ∧ cyc4 v 3 = v 3 := <proof>",
  "theorem cyc4_symm_apply (v : Fin 4 → ℝ) :\n    cyc4.symm v 0 = v 1 ∧ cyc4.symm v 1 = v 2 ∧ cyc4.symm v 2 = v 0 ∧ cyc4.symm v 3 = v 3 := <proof>",
  "theorem cyc4_mem_omega4 {v : Fin 4 → ℝ} (hv : v ∈ omega4) : cyc4 v ∈ omega4 := <proof>",
  "theorem cyc4_symm_mem_omega4 {v : Fin 4 → ℝ} (hv : v ∈ omega4) : cyc4.symm v ∈ omega4 := <proof>",
  "/-- **Ω₄ is drivable.** -/",
  "noncomputable def omega4Drive : ElementaryDrivability omega4 where\n  flow := rot4\n  flow_zero := AffineEquiv.ext fun v => by rw [rot4_apply, rotFun4_zero, AffineEquiv.refl_apply]\n  flow_add s t := AffineEquiv.ext fun v => by\n    simp only [AffineEquiv.trans_apply, rot4_apply, rotFun4_add]\n  flow_continuous := by\n    refine continuous_pi fun i => ?_\n    fin_cases i\n    · show Continuous fun q : ℝ × (Fin 4 → ℝ) => Real.cos q.1 * q.2 0 - Real.sin q.1 * q.2 1\n      fun_prop\n    · show Continuous fun q : ℝ × (Fin 4 → ℝ) => Real.sin q.1 * q.2 0 + Real.cos q.1 * q.2 1\n      fun_prop\n    · show Continuous fun q : ℝ × (Fin 4 → ℝ) => q.2 2\n      fun_prop\n    · show Continuous fun q : ℝ × (Fin 4 → ℝ) => q.2 3\n      fun_prop\n  flow_preserves t _ hv := rotFun4_mem_omega4 t hv\n  t₀ := Real.pi\n  N_involutive x _ := by\n    simp only [rot4_apply]\n    obtain ⟨a0, a1, a2, a3⟩ := rotFun4_apply Real.pi (rotFun4 Real.pi x)\n    obtain ⟨b0, b1, b2, b3⟩ := rotFun4_apply Real.pi x\n    apply vec4_ext\n    · rw [a0, b0, b1, Real.cos_pi, Real.sin_pi]; ring\n    · rw [a1, b0, b1, Real.cos_pi, Real.sin_pi]; ring\n    · rw [a2, b2]\n    · rw [a3, b3]\n  N_moves := ⟨![1, 0, 0, 0], by show ((1 : ℝ) ^ 2 + 0 ^ 2 + 0 ^ 2) ^ 2 + (0 : ℝ) ^ 4 ≤ 1; norm_num,\n    fun h => by\n      have h0 : rot4 Real.pi ![1, 0, 0, 0] 0 = (![1, 0, 0, 0] : Fin 4 → ℝ) 0 := congrFun h 0\n      change Real.cos Real.pi * 1 - Real.sin Real.pi * 0 = 1 at h0\n      rw [Real.cos_pi, Real.sin_pi] at h0\n      norm_num at h0⟩\n  J := cyc4\n  J_preserves _ hv := cyc4_mem_omega4 hv\n  J_symm_preserves _ hv := cyc4_symm_mem_omega4 hv\n  J_off_axis := ⟨Real.pi, fun s => ⟨![0, 0, 1, 0],\n    by show ((0 : ℝ) ^ 2 + 0 ^ 2 + 1 ^ 2) ^ 2 + (0 : ℝ) ^ 4 ≤ 1; norm_num, fun h => by\n      have h2 : cyc4 (rot4 Real.pi (cyc4.symm ![0, 0, 1, 0])) 2 = rot4 s ![0, 0, 1, 0] 2 :=\n        congrFun h 2\n      change Real.sin Real.pi * 0 + Real.cos Real.pi * 1 = 1 at h2\n      rw [Real.sin_pi, Real.cos_pi] at h2\n      norm_num at h2⟩⟩",
  "theorem omega4_drivable : Nonempty (ElementaryDrivability omega4) := <proof>",
  "/-! ### §D — Ω₄ is no affine image of the ball -/",
  "/-- **Ω₄ is not an ellipsoid.** In the plane of the first and last axes, no quadric contains the\neight states `(±1, 0)`, `(0, ±1)`, `(±5/6, ±5/6)` and excludes the eight points `(±1, ±1/2)`,\n`(±1/2, ±1)`; the affine image of a ball cut by that plane would be such a quadric. -/",
  "theorem not_affine_eball_omega4 :\n    ¬ ∃ A : (Fin 4 → ℝ) ≃ᵃ[ℝ] (Fin 4 → ℝ), A '' omega4 = eball 4 := <proof>",
  "/-! ### §E — the separation -/",
  "theorem not_boundaryTransitive_omega4 {G : Set ((Fin 4 → ℝ) ≃ᵃ[ℝ] (Fin 4 → ℝ))}\n    (hG : PreservesBody omega4 G) : ¬ BoundaryTransitive omega4 G := <proof>",
  "theorem not_denseBoundaryOrbit_omega4 {G : Set ((Fin 4 → ℝ) ≃ᵃ[ℝ] (Fin 4 → ℝ))}\n    (hG : PreservesBody omega4 G) : ¬ DenseBoundaryOrbit omega4 G := <proof>",
  "/-- **Ω₄ is a counterexample.** Ω₄ is a compact convex body with interior that is drivable,\ncarries a sharp seed, is relatively strictly convex and centrally symmetric, and on which no\nbody-preserving family is boundary transitive or has a dense boundary orbit. -/",
  "theorem kinfTrans_separation :\n    IsCompact omega4 ∧ Convex ℝ omega4 ∧ (interior omega4).Nonempty\n      ∧ Nonempty (ElementaryDrivability omega4) ∧ SharpSeed omega4 seed4\n      ∧ RelStrictConvex omega4 ∧ CentrallySymmetric omega4 0\n      ∧ ∀ G : Set ((Fin 4 → ℝ) ≃ᵃ[ℝ] (Fin 4 → ℝ)), PreservesBody omega4 G →\n          ¬ BoundaryTransitive omega4 G ∧ ¬ DenseBoundaryOrbit omega4 G := <proof>",
  "end",
  "end TransSeparation",
  "end OIBridge",
  "#print axioms OIBridge.TransSeparation.omega4_isCompact",
  "#print axioms OIBridge.TransSeparation.conv_core",
  "#print axioms OIBridge.TransSeparation.omega4_convex",
  "#print axioms OIBridge.TransSeparation.abstract_strict",
  "#print axioms OIBridge.TransSeparation.omega4_strictConvex",
  "#print axioms OIBridge.TransSeparation.relStrictConvex_omega4",
  "#print axioms OIBridge.TransSeparation.singletonFaces_omega4",
  "#print axioms OIBridge.TransSeparation.omega4_interior_nonempty",
  "#print axioms OIBridge.TransSeparation.omega4_centrallySymmetric",
  "#print axioms OIBridge.TransSeparation.sharpSeed_omega4",
  "#print axioms OIBridge.TransSeparation.omega4_drivable",
  "#print axioms OIBridge.TransSeparation.not_affine_eball_omega4",
  "#print axioms OIBridge.TransSeparation.not_boundaryTransitive_omega4",
  "#print axioms OIBridge.TransSeparation.not_denseBoundaryOrbit_omega4",
  "#print axioms OIBridge.TransSeparation.kinfTrans_separation"
 ]
}''')
MOD_BLOB = GEN['mod_blob']
PROBE_BLOB = GEN['probe_blob']
PROBE_OUT_SHA256 = GEN['probe_out_sha256']
SKELETON = GEN['skeleton']
DECLS = [tuple(x) for x in GEN['decls']]
KEYTEXT = GEN['keytext']
PRINTS = GEN['prints']
LANDED = GEN['landed']
BALL = GEN['ball']
CENSUS_FAMILY = GEN['census_family']
PROBE_LINES = GEN['probe_lines']

SHARD = '''  probes_ktranssep1:
    name: Numerical probes / KTRANS-SEP-1 Omega4 counterexample
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install the exact-algebra dependency
        run: pip install sympy==1.14.0

      - name: KTRANS-SEP-1 exact probe
        working-directory: verification/lean
        run: |
          echo "=== ktrans_sep1_probe.py ==="
          python3 -I -B ktrans_sep1_probe.py | tee "$RUNNER_TEMP/ktrans_sep1_probe.out"
          grep -qx 'VERDICT DRIVE-SEED-GEOM-SEC-CAP2-NOT-TRANS' "$RUNNER_TEMP/ktrans_sep1_probe.out"

      - name: KTRANS-SEP-1 independent exact layer and countercontrols
        run: python3 -I -B verification/programmes/oi-qm/reconstruction/round-ktrans-sep-1-omega4/controls.py exact

      - name: KTRANS-SEP-1 control mutation tests
        run: python3 -I -B verification/programmes/oi-qm/reconstruction/round-ktrans-sep-1-omega4/controls.py --self-test

'''
SPLICES = [
    ('  # Act 42. Two shards run on every event', SHARD + '  # Act 42. Two shards run on every event'),
    ('probes_bg2, probes_a42_witness', 'probes_bg2, probes_ktranssep1, probes_a42_witness'),
    ('          BG2_RESULT: ${{ needs.probes_bg2.result }}\n',
     '          BG2_RESULT: ${{ needs.probes_bg2.result }}\n'
     '          KTRANSSEP1_RESULT: ${{ needs.probes_ktranssep1.result }}\n'),
    ('          echo "bg2=${BG2_RESULT}"\n', '          echo "bg2=${BG2_RESULT}"\n          echo "ktranssep1=${KTRANSSEP1_RESULT}"\n'),
    ('          test "${BG2_RESULT}" = success\n',
     '          test "${BG2_RESULT}" = success\n          test "${KTRANSSEP1_RESULT}" = success\n'),
]

FAILS, COUNT, CODES_RUN = [], [0], {}


def check(code, name, cond):
    COUNT[0] += 1
    ok = bool(cond)
    CODES_RUN.setdefault(code, True)
    if not ok:
        CODES_RUN[code] = False
        FAILS.append(code)
    print('  %s  %-4s %s' % ('PASS' if ok else 'FAIL', code, name))
    return ok


def git(*a):
    return subprocess.run(['git'] + list(a), capture_output=True, text=True)


def show(commit, path):
    r = subprocess.run(['git', 'show', '%s:%s' % (commit, path)], capture_output=True)
    return r.stdout.decode('utf-8') if r.returncode == 0 else None


def cat_blob(oid):
    r = subprocess.run(['git', 'cat-file', 'blob', oid], capture_output=True)
    return r.stdout.decode('utf-8') if r.returncode == 0 else None


def blob_id(text):
    b = text.encode('utf-8')
    return hashlib.sha1(b'blob %d\0' % len(b) + b).hexdigest()


def norm(s):
    return re.sub(r'\s+', ' ', s.replace('`', '')).strip().lower()


# ---- the Lean surface -------------------------------------------------------------------------------------------
DECL_RE = re.compile(r'^(?:@\[[^\]\n]*\]\s*)?(?:private |protected )?(?:noncomputable |partial )?'
                     r'(theorem|lemma|def|abbrev|structure|class|inductive|instance|axiom|opaque)\s+([^\s(:{\[⦃]+)', re.M)
TOP_RE = re.compile(r'^(?:/--|/-!|/-|#print|#eval|namespace |end\b|open |noncomputable section|section\b|variable |'
                    r'import |set_option |attribute |universe |(?:@\[[^\]\n]*\]\s*)?(?:private |protected )?'
                    r'(?:noncomputable |partial )?(?:theorem|lemma|def|abbrev|structure|class|inductive|instance|'
                    r'axiom|opaque)\s)')
OPEN_BR, CLOSE_BR = '([{⟨⦃', ')]}⟩⦄'


def chunks(text):
    """Top-level chunks: a new chunk starts at a column-0 command line outside a block comment."""
    out, cur = [], []
    for line in text.split('\n'):
        if TOP_RE.match(line) and cur and '\n'.join(cur).count('/-') <= '\n'.join(cur).count('-/'):
            out.append('\n'.join(cur))
            cur = []
        cur.append(line)
    if cur:
        out.append('\n'.join(cur))
    return out


def stmt_end(chunk):
    """Index of the first `:=` at bracket depth 0, or -1."""
    depth = 0
    for i, ch in enumerate(chunk):
        if ch in OPEN_BR:
            depth += 1
        elif ch in CLOSE_BR:
            depth -= 1
        elif ch == ':' and depth == 0 and chunk[i:i + 2] == ':=':
            return i
    return -1


def skeleton(text):
    sk = []
    for c in chunks(text):
        m = DECL_RE.match(c)
        if m and m.group(1) in ('theorem', 'lemma'):
            k = stmt_end(c)
            sk.append((c[:k].rstrip() + ' := <proof>') if k >= 0 else c)
        else:
            sk.append(c.rstrip())
    return sk


def decls(text):
    return [(m.group(1), m.group(2)) for m in DECL_RE.finditer(text)]


def decl_text(text, name):
    """A declaration's frozen text: a theorem's statement up to `:=`, any other declaration whole."""
    for c in chunks(text):
        m = DECL_RE.match(c)
        if m and m.group(2) == name:
            if m.group(1) in ('theorem', 'lemma'):
                k = stmt_end(c)
                return c[:k].rstrip() if k >= 0 else None
            return c.rstrip()
    return None


def header_comment(text):
    m = re.match(r'\s*/-(?!-)(.*?)-/', text, re.S)
    return m.group(1) if m else ''


def print_lines(text):
    return [(n, l) for n, l in enumerate(text.split('\n'), 1) if l.startswith('#print axioms')]


def module_checks(mod, landed_d=None, closure_names=None):
    """N1-N3 and S1-S5 on the module text; returns the set of KEY statements that hold (for the cells)."""
    if mod is None:
        for code in ('N1', 'N2', 'N3', 'S1', 'S2', 'S4', 'S5'):
            check(code, 'the module is present', False)
        return set()
    check('N1', 'the module declares exactly the frozen declarations, in order and by kind', decls(mod) == DECLS)
    sk = skeleton(mod)
    bad = [i for i, (a, b) in enumerate(zip(sk, SKELETON)) if a != b]
    check('N2', 'the module with proofs elided is the frozen skeleton (%d chunks%s)'
          % (len(SKELETON), '' if sk == SKELETON else '; first difference at chunk %s' % (bad[:1] or len(sk))),
          sk == SKELETON)
    check('N3', 'no sorry, admit, axiom or opaque declaration, native_decide, implemented_by, extern or unsafe',
          not HYGIENE.search(re.sub(r'/-.*?-/', '', mod, flags=re.S)))
    good = {n for n in KEY if decl_text(mod, n) == KEYTEXT[n]}
    check('S1', 'the load-bearing statements have their frozen texts%s'
          % ('' if good == set(KEY) else ' (differ: %s)' % ', '.join(sorted(set(KEY) - good))), good == set(KEY))
    lines = mod.split('\n')
    imps = [l for l in lines if l.startswith('import ')]
    opens = [l for l in lines if l.startswith('open ')]
    own = {n for _, n in decls(mod)}
    clash = sorted(own & (closure_names if closure_names is not None else closure_names_at_d()))
    check('S2', 'the module imports only OIBridge.DenseOrbit, opens the frozen namespaces, and shadows no name of its '
                'import closure%s' % (' (shadows %s)' % ', '.join(clash) if clash else ''),
          imps == PREAMBLE_IMPORTS and opens == [OPEN_LINE] and not clash)
    if landed_d is not None:
        diff = sorted(n for n in LANDED if landed_d.get(n) != LANDED[n]['text'])
        check('S2', 'the landed declarations the module uses have their frozen texts at D, each declared once in the '
                    'closure%s' % (' (differ: %s)' % ', '.join(diff) if diff else ''), not diff)
    ph = [p for p in PHRASES if p in ' %s ' % norm(header_comment(mod))]
    check('S4', 'the module header carries none of the frozen phrases%s' % (' %s' % ph if ph else ''), not ph)
    pl = [l for _, l in print_lines(mod)]
    names = [l[len('#print axioms '):].strip() for l in pl]
    thms = {n for k, n in decls(mod) if k in ('theorem', 'lemma')}
    check('S5', 'exactly the 15 frozen #print axioms lines, in order and distinct, each naming a module theorem',
          pl == ['#print axioms ' + NS + p for p in PRINTS] and len(set(names)) == len(names) == 15
          and all(n.startswith(NS) and n[len(NS):] in thms for n in names))
    return good


def landed_texts(reader):
    """The landed declarations' texts read through reader(path), and how often each name is declared in the closure."""
    out, cache = {}, {}
    for name, info in list(LANDED.items()) + list(BALL.items()):
        path = 'verification/lean-mathlib/OIBridge/%s.lean' % info['module']
        if path not in cache:
            cache[path] = reader(path)
        t = cache[path]
        out[name] = decl_text(t, name) if t is not None else None
    counts = {}
    for m in CLOSURE_MODULES():
        t = reader('verification/lean-mathlib/OIBridge/%s.lean' % m)
        for _, n in decls(t or ''):
            counts[n] = counts.get(n, 0) + 1
    for name in list(LANDED) + list(BALL):
        if counts.get(name) != 1:
            out[name] = None
    return out


def CLOSURE_MODULES():
    return GEN['closure_modules']


def closure_names_at_d():
    names = set()
    for m in CLOSURE_MODULES():
        names |= {n for _, n in decls(show(D, 'verification/lean-mathlib/OIBridge/%s.lean' % m) or '')}
    return names


def ball_check(landed):
    diff = sorted(n for n in BALL if landed.get(n) != BALL[n]['text'])
    check('S3', 'at D, sharpEff_sharpSeed, fullAut, preservesBody_fullAut and boundaryTransitive_fullAut have their frozen texts%s'
          % (' (differ: %s)' % ', '.join(diff) if diff else ''), not diff)


# ---- the independent exact layer (rationals only; shares no code with the probe) ---------------------------------
def F4(v):
    return (v[0] ** 2 + v[1] ** 2 + v[2] ** 2) ** 2 + v[3] ** 4


def FB(v):
    return v[0] ** 2 + v[1] ** 2 + v[2] ** 2 + v[3] ** 2


def us(u, s):
    return (Fr(u), Fr(0), Fr(0), Fr(s))


h, f6 = Fr(1, 2), Fr(5, 6)
INNER = [us(1, 0), us(-1, 0), us(0, 1), us(0, -1), us(f6, f6), us(f6, -f6), us(-f6, f6), us(-f6, -f6)]
OUTER = [us(1, h), us(1, -h), us(-1, h), us(-1, -h), us(h, 1), us(h, -1), us(-h, 1), us(-h, -1)]
W_INNER = [Fr(10, 9)] * 4 + [Fr(2)] * 4
W_OUTER = [Fr(14, 9)] * 8


def row(v):
    """Coefficients of (alpha, beta, gamma, b0, b3, P) in sum_j (A v)_j^2 at v = (u, 0, 0, s)."""
    u, s = v[0], v[3]
    return [u * u, s * s, 2 * u * s, 2 * u, 2 * s, Fr(1)]


def farkas(inner, outer, wi, wo):
    """True iff the weights certify that no (alpha..P) has row.x <= 1 on inner and row.x > 1 on outer."""
    if len(wi) != len(inner) or len(wo) != len(outer) or not all(w > 0 for w in wi + wo):
        return False
    comb = [sum(w * row(v)[k] for w, v in zip(wo, outer)) - sum(w * row(v)[k] for w, v in zip(wi, inner))
            for k in range(6)]
    return all(c == 0 for c in comb) and sum(wo) - sum(wi) == 0


def feasible_witness(x, inner, outer):
    val = lambda v: sum(a * b for a, b in zip(row(v), x))
    return all(val(v) <= 1 for v in inner) and all(val(v) > 1 for v in outer)


def lean_num(s):
    s = s.strip()
    neg = s.startswith('-')
    s = s[1:].strip() if neg else s
    s = s.strip('()').strip()
    m = re.fullmatch(r'(\d+)\s*(?:/\s*(\d+))?', s)
    if not m:
        return None
    v = Fr(int(m.group(1)), int(m.group(2) or 1))
    return -v if neg else v


def module_points(mod):
    """The vectors `hin ![..]` and `hout ![..]` of the module's proof of not_affine_eball_omega4."""
    body = None
    for c in chunks(mod or ''):
        m = DECL_RE.match(c)
        if m and m.group(2) == 'not_affine_eball_omega4':
            body = c
    if body is None:
        return None, None
    get = lambda kw: [tuple(lean_num(x) for x in vec.split(','))
                      for vec in re.findall(r'\b%s !\[([^\]]*)\]' % kw, body)]
    return get('hin'), get('hout')


def bd_points():
    """Rational boundary points of Omega4 (F4 = 1)."""
    t = Fr
    return [(t(1), t(0), t(0), t(0)), (t(-1), t(0), t(0), t(0)), (t(0), t(1), t(0), t(0)),
            (t(1, 3), t(2, 3), t(2, 3), t(0)), (t(-2, 3), t(1, 3), t(2, 3), t(0)), (t(3, 5), t(0), t(4, 5), t(0)),
            (t(0), t(0), t(0), t(1)), (t(0), t(0), t(0), t(-1)), (t(0), t(0), t(-1), t(0))]


def grid(Fn, step=4):
    ax = [Fr(k, step) for k in range(-step, step + 1)]
    return [w for w in product(ax, repeat=4) if Fn(w) <= 1]


def exact_checks(mod, inner=None, outer=None, wi=None, wo=None, ball_x=None, translate=None, h_last=0, seg_map=None):
    inner, outer = inner or INNER, outer or OUTER
    wi, wo = wi or W_INNER, wo or W_OUTER
    check('X1', 'the eight states lie in Omega4 and the eight points outside it, exactly',
          all(F4(v) <= 1 for v in inner) and all(F4(v) > 1 for v in outer) and len(inner) == len(outer) == 8)
    check('X2', 'the frozen positive weights cancel every coefficient and the constant: the system is infeasible',
          farkas(inner, outer, wi, wo))
    mi, mo = module_points(mod)
    check('X3', 'the module\'s proof of not_affine_eball_omega4 states exactly these sixteen points, in order',
          mi == inner and mo == outer)
    # CX1: the ball
    g = grid(FB)
    bin_ = [us(1, 0), us(-1, 0), us(0, 1), us(0, -1)] + [us(a, b) for a in (Fr(3, 5), Fr(-3, 5))
                                                         for b in (Fr(4, 5), Fr(-4, 5))]
    x = ball_x or [Fr(1), Fr(1), Fr(0), Fr(0), Fr(0), Fr(0)]
    seed = lambda v: (1 + v[3]) / 2
    rot = lambda v: (Fr(3, 5) * v[0] - Fr(4, 5) * v[1], Fr(4, 5) * v[0] + Fr(3, 5) * v[1], v[2], v[3])
    cyc = lambda v: (v[2], v[0], v[1], v[3])
    bbd = [w for w in g if FB(w) == 1]
    named = (all(0 <= seed(w) <= 1 for w in g) and seed((0, 0, 0, 1)) == 1 and seed((0, 0, 0, -1)) == 0
             and all(FB(tuple(-c for c in w)) == FB(w) for w in g)
             and all(FB(rot(w)) == FB(w) and FB(cyc(w)) == FB(w) for w in g)
             and all(FB(tuple((a + b) / 2 for a, b in zip(p, q))) < 1 for i, p in enumerate(bbd) for q in bbd[i + 1:]))
    check('CX1', 'the 4-ball: seed, central symmetry, the drive\'s maps and strict midpoints hold at %d exact states; '
                 'the ball\'s system is feasible; a state of the certificate is not a ball state' % len(g),
          named and len(bbd) > 1 and feasible_witness(x, bin_, outer) and not all(FB(v) <= 1 for v in inner))
    # CX2: PreservesBody dropped
    bd = bd_points()
    tr = translate or (lambda x_, y_: tuple(b - a for a, b in zip(x_, y_)))
    g4 = grid(F4)
    ok2 = all(F4(p) == 1 for p in bd)
    for p in bd:
        for q in bd:
            t = tr(p, q)
            ok2 = ok2 and tuple(a + b for a, b in zip(p, t)) == q
            if p != q:
                ok2 = ok2 and any(F4(tuple(a + b for a, b in zip(z, t))) > 1 for z in g4)
    check('CX2', 'translations carry each of %d boundary points to each other; each nonzero one moves a state of '
                 'Omega4 out of it (so the translations are boundary transitive and not body-preserving)' % len(bd), ok2)
    # CX3: compactness dropped -- the half-space {s <= 1}
    H = lambda v: v[3] <= 1
    hb = [(Fr(a), Fr(b), Fr(0), Fr(1)) for a in range(-2, 3) for b in range(-2, 3)]
    ok3 = all(H(p) for p in hb) and H((Fr(10) ** 6, 0, 0, 0)) and not H((0, 0, 0, Fr(1) + Fr(1, 10 ** 6)))
    for p in hb:
        for q in hb:
            t = tuple(b - a for a, b in zip(p, q))[:3] + (Fr(h_last),)
            ok3 = ok3 and tuple(a + b for a, b in zip(p, t)) == q and t[3] == 0 and all(H(tuple(a + b for a, b in zip(z, t))) for z in hb + [(0, 0, 0, Fr(-5))])
    check('CX3', 'the half-space {s <= 1}: translations with zero last coordinate preserve it and carry each of %d '
                 'boundary points to each other; it contains (10^6, 0, 0, 0)' % len(hb), ok3)
    # CX4: nonempty interior dropped -- the segment [-e0, e0]
    S = lambda v: v[1] == v[2] == v[3] == 0 and -1 <= v[0] <= 1
    seg = [(Fr(k, 4), Fr(0), Fr(0), Fr(0)) for k in range(-4, 5)]
    neg = seg_map or (lambda v: tuple(-c for c in v))
    ok4 = (all(S(neg(v)) for v in seg) and neg(seg[0]) == seg[-1] and neg(seg[-1]) == seg[0]
           and not any(S((Fr(0), Fr(1, 10 ** k), Fr(0), Fr(0))) for k in range(1, 7)))
    check('CX4', 'the segment [-e0, e0]: -id preserves it and swaps its two endpoints; (0, 10^-k, 0, 0) is outside it '
                 'for k = 1..6', ok4)


# ---- the probe ---------------------------------------------------------------------------------------------------
SYMPY_VERSION = '1.14.0'


def run_probe(text):
    """(sympy version or None, exit status, stdout, stderr) of the probe text run with python3 -I -B."""
    v = subprocess.run([sys.executable, '-I', '-c', 'import sympy, sys; sys.stdout.write(sympy.__version__)'],
                       capture_output=True, text=True)
    ver = v.stdout.strip() if v.returncode == 0 else None
    with tempfile.TemporaryDirectory() as td:
        p = os.path.join(td, 'probe.py')
        with open(p, 'w', encoding='utf-8') as fh:
            fh.write(text or '')
        try:
            r = subprocess.run([sys.executable, '-I', '-B', p], capture_output=True, text=True, cwd=td, timeout=600)
            rc, out, err = r.returncode, r.stdout, r.stderr
        except subprocess.TimeoutExpired:
            rc, out, err = None, '', 'timeout'
    return ver, rc, out, err


def probe_state(run):
    """'exact' (the frozen output), 'negative' (a complete run in which a check failed), or ('void', reason)."""
    ver, rc, out, err = run
    if ver != SYMPY_VERSION:
        return ('void', 'sympy %s is not available (found %s)' % (SYMPY_VERSION, ver))
    lines = [l for l in (out or '').split('\n') if l]
    if rc != 0 or not lines or not lines[-1].startswith('VERDICT') or not any(l.startswith('checks: ') for l in lines):
        return ('void', 'the probe did not run to completion (exit %s%s)' % (rc, '; stderr: ' + err.strip()[-120:]
                                                                            if err and err.strip() else ''))
    if hashlib.sha256(out.encode('utf-8')).hexdigest() == PROBE_OUT_SHA256 and all(l in lines for l in PROBE_LINES):
        return 'exact'
    if any(l.startswith('FAIL ') or 'DID NOT FAIL' in l or 'NOT RENDERED' in l for l in lines):
        return 'negative'
    return ('void', 'the probe output differs from the frozen output without a failing check')


def probe_ok(out):
    """The frozen output, read as a complete run under the pinned sympy."""
    return out is not None and probe_state((SYMPY_VERSION, 0, out, '')) == 'exact'


# ---- the bridge log ----------------------------------------------------------------------------------------------
TS = re.compile(r'^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d\.\d+Z ')
REPORT = re.compile(r"^info: OIBridge/TransSeparation\.lean:(\d+):\d+: '" + re.escape(NS) +
                    r"([A-Za-z0-9_']+)' (?:depends on axioms: \[([^\]]*)\]|does not depend on any axioms)\s*$")
REPORT_HEAD = re.compile(r'^info: OIBridge/TransSeparation\.lean:\d+:\d+: ')
BUILT = re.compile(r'Built OIBridge\.TransSeparation\b')
GATE_STEP = re.compile(r'^  (PASS|FAIL|SKIP)  (\S+)')


def log_facts(text, mod):
    """What the served text shows about the module, with the served line of each item (1-based)."""
    lines = [TS.sub('', l, count=1) for l in (text or '').split('\n')] if text else []
    f = {'served_lines': len(lines), 'reports': {}, 'unparsed': [], 'built': None, 'build': False,
         'gate_start': None, 'gate_end': None, 'gate_pass': False, 'gate_fail': [], 'mod_errors': 0}
    for n, l in enumerate(lines, 1):
        m = REPORT.match(l)
        if m:
            ax = {a.strip() for a in (m.group(3) or '').split(',') if a.strip()}
            f['reports'].setdefault(m.group(2), []).append((int(m.group(1)), ax, n))
        elif REPORT_HEAD.match(l):
            f['unparsed'].append(n)
        if f['built'] is None and BUILT.search(l):
            f['built'] = n
        if re.match(r'^Build completed successfully \(\d+ jobs\)\.', l):
            f['build'] = True
        if l.startswith('error: OIBridge/TransSeparation.lean:'):
            f['mod_errors'] += 1
        if l == 'release gate' and f['gate_start'] is None:
            f['gate_start'] = n
        if l.startswith('release gate: ') and f['gate_start'] is not None and f['gate_end'] is None:
            f['gate_end'] = n
            f['gate_pass'] = l.startswith('release gate: PASS')
        m = GATE_STEP.match(l)
        if m and f['gate_start'] is not None and f['gate_end'] is None and m.group(1) == 'FAIL':
            f['gate_fail'].append(m.group(2))
    f['at'] = {l[len('#print axioms ' + NS):].strip(): n for n, l in print_lines(mod or '')}
    return f


def window(f, meta=None):
    """None when the served text is complete for the module's reports, else the reason it is not."""
    if not f['served_lines']:
        return 'the log is empty or absent'
    if meta is not None:
        try:
            o, m = int(meta['original_lines']), int(meta['served_lines'])
        except (KeyError, TypeError, ValueError):
            return 'the log metadata names no original and served line counts'
        if m != f['served_lines'] or not 1 <= m <= o:
            return 'the log metadata (%s of %s lines) does not describe this text (%d lines)' % (m, o, f['served_lines'])
    bad = [n for n in PRINTS if len(f['reports'].get(n, [])) != 1 or f['reports'][n][0][0] != f['at'].get(n)]
    if bad:
        return 'frozen reports missing, duplicated or at another line: %s' % ', '.join(bad)
    if f['unparsed']:
        return 'a TransSeparation report line does not parse (served line %d)' % f['unparsed'][0]
    first = min(f['reports'][n][0][2] for n in PRINTS)
    if f['built'] is None or f['built'] > first:
        return 'the module\'s build line is not in the served window before its reports (the window may be truncated)'
    return None


def kernel_state(f, meta=None):
    """('void', reason), or (nonell_ok, cex_ok) from complete evidence."""
    w = window(f, meta)
    if w:
        return ('void', w)
    bad = {n for n in PRINTS if not f['reports'][n][0][1] <= ALLOWED_AXIOMS}
    gate_done = f['gate_start'] is not None and f['gate_end'] is not None
    if f['build'] and gate_done and f['gate_pass'] and not bad and not f['mod_errors']:
        return (True, True)
    if bad and ((not f['build'] and f['mod_errors']) or (gate_done and f['gate_fail'] == ['lean-axioms'])):
        return (False, False)
    return ('void', 'the build and gate evidence is incomplete or fails for a reason outside the module '
                    '(build %s, gate %s, failing steps %s, module errors %d)'
            % (f['build'], 'complete' if gate_done else 'incomplete', f['gate_fail'] or 'none', f['mod_errors']))


def cells(mod, good_key, log, exact_ok, probe_run, meta=None):
    """The three tokens, or ('void', reason): a tooling failure or incomplete evidence never yields a token."""
    if not exact_ok:
        return ('void', 'an exact control failed')
    ks = kernel_state(log_facts(log, mod), meta)
    if ks[0] == 'void':
        return ks
    ps = probe_state(probe_run)
    if isinstance(ps, tuple):
        return ps
    nonell = ks[0] and set(NONELL_KEY) <= good_key
    cex = ks[1] and set(KEY) <= good_key
    return [TOK_NONELL[0 if nonell else 1], TOK_CEX[0 if cex else 1], TOK_EXACT[0 if ps == 'exact' else 1]]


def window_facts(f):
    pos = {n: f['reports'][n][0][2] for n in PRINTS if len(f['reports'].get(n, [])) == 1}
    return {'served_lines': f['served_lines'], 'built_line': f['built'], 'report_lines': pos,
            'gate_start': f['gate_start'], 'gate_end': f['gate_end']}


# ---- the record, the pins, the chain, the governed paths ---------------------------------------------------------
PIN_ROW = re.compile(r'^\| `(evidence/[A-Za-z0-9_./-]+)` \| (?:`([0-9a-f]{64})`|pending) \|\s*$')


def pins(prereg):
    out = {}
    for l in (prereg or '').split('\n'):
        m = PIN_ROW.match(l)
        if m:
            out[m.group(1)] = m.group(2)
    return out


def pins_ok(table, files, frozen):
    """files: {relative path under RDIR: bytes}."""
    if not set(REQUIRED_EVIDENCE) <= set(table):
        return False
    for p, dig in table.items():
        if dig is None:
            if frozen:
                return False
            continue
        if p not in files or hashlib.sha256(files[p]).hexdigest() != dig:
            return False
    return True


def record_ok(rel, table, frozen, stage):
    allowed = {'preregistration.md', 'controls.py', 'result.md', 'evidence/f-run/results.json'} | set(table)
    extra = [p for p in rel if p not in allowed and not re.fullmatch(r'amendments/[A-Za-z0-9_.-]+\.md', p)]
    need = {'preregistration.md', 'controls.py'}
    if frozen:
        need.add('evidence/f-run/results.json')
        if stage == 'E':
            need.add('result.md')
    return not extra and need <= set(rel) and not (stage == 'S1' and 'result.md' in rel)


TS_KEY = re.compile(r'(?:^|_)(?:at|time|times|timestamp|date|duration|seconds)$')
RUN_EVIDENCE = 'evidence/predicted-tree-run.json'


def walk(x):
    if isinstance(x, dict):
        for k, v in x.items():
            yield k, v
            yield from walk(v)
    elif isinstance(x, list):
        for v in x:
            yield from walk(v)


def evidence_ok(data):
    """A structured expected result of AGENTS 4.42 item 1: schema, a stated form, a source digest when derived, and
    no field that varies between runs (timestamps, durations)."""
    try:
        d = json.loads(data)
    except (ValueError, TypeError):
        return False
    if not isinstance(d, dict) or d.get('schema') != 'oi-evidence-result' or d.get('version') != 1 or \
            d.get('form') not in ('complete', 'derived'):
        return False
    if d['form'] == 'derived' and not any(k.endswith('sha256') and isinstance(v, str) and re.fullmatch(r'[0-9a-f]{64}', v)
                                          for k, v in walk(d.get('source', {}))):
        return False
    return not any(TS_KEY.search(k) for k, _ in walk(d))


def run_window_ok(data, head):
    """A run's retained result names head, is a green workflow_dispatch run, and records where the module's build
    line, its fifteen reports and the release gate fall in the served window, all inside it and in that order."""
    try:
        d = json.loads(data)
        r, s, w = d['run'], d['source'], d['observed']['transseparation_window']
        o, m = s['original_lines'], s['served_lines']
        mods = d['expected']['modules']['OIBridge/TransSeparation.lean']
        rl = w['report_lines']
        ints = [o, m, w['served_lines'], w['built_line'], w['gate_start'], w['gate_end']] + list(rl.values())
        if not all(type(x) is int for x in ints):
            return False
        return bool(evidence_ok(data) and r['head_sha'] == head and r['event'] == 'workflow_dispatch' and d['jobs']
                and all(j['conclusion'] == 'success' for j in d['jobs']) and 1 <= m <= o and w['served_lines'] == m
                and sorted(rl) == sorted(PRINTS) and 1 <= w['built_line'] < min(rl.values())
                and max(rl.values()) < w['gate_start'] < w['gate_end'] <= m
                and d['expected']['build_success'] is True and str(d['expected']['gate']['verdict']).startswith('PASS')
                and mods['status'] == 'complete'
                and [x['name'] for x in mods['reports']] == [NS + n for n in PRINTS]
                and all(set(x['axioms']) <= ALLOWED_AXIOMS for x in mods['reports']))
    except (ValueError, KeyError, TypeError, AttributeError):
        return False


def predicted_head(prereg):
    m = re.search(r'^### The predicted execution tree\n\n- \*\*`([0-9a-f]{40})`\*\*', prereg or '', re.M)
    return m.group(1) if m else None


def governed_ok(rows):
    """rows: [(status, path)] of `git diff --name-status --no-renames D commit`."""
    ex = {p: s for s, p in rows if not p.startswith(RDIR)}
    return ex == EXEC and all(s in ('A', 'M') for s, p in rows if p.startswith(RDIR))


def chain_ok(revs, d, f, head, delta_df, prereg_head, prereg_f):
    """revs: [(commit, [parents])] of `git rev-list --parents d..head`."""
    par = {c: ps for c, ps in revs}
    if any(len(ps) != 1 for ps in par.values()) or f not in par:
        return False
    walk, c = [], head
    while c in par:
        walk.append(c)
        c = par[c][0]
    ctl = all(p == PREREG or re.fullmatch(re.escape(RDIR) + r'amendments/[A-Za-z0-9_.-]+\.md', p) for p in delta_df)
    return c == d and set(walk) == set(par) and f in walk and PREREG in delta_df and ctl and prereg_head == prereg_f


# ---- the result note ---------------------------------------------------------------------------------------------
def note_tokens(note):
    return re.findall(r'KTRANS-SEP-(?:NONELLIPSOID-PROVED|NONELLIPSOID-NOT-ESTABLISHED|COUNTEREXAMPLE-PROVED|'
                      r'COUNTEREXAMPLE-NOT-ESTABLISHED|INSTANCES-EXACT|INSTANCES-NOT-ESTABLISHED)(?![A-Z-])', note)


def note_ok(note, toks):
    n = norm(note)
    positive = toks == [TOK_NONELL[0], TOK_CEX[0], TOK_EXACT[0]]
    rest = n.replace(norm(EARNED), ' ').replace(norm(NONINF), ' ')
    ph = [p for p in PHRASES if p in ' %s ' % rest]
    return (sorted(note_tokens(note)) == sorted(toks) and (norm(EARNED) in n) == positive and norm(NONINF) in n
            and not ph), ph


# ---- check and verdict -------------------------------------------------------------------------------------------
def tree_files(commit, prefix):
    r = git('ls-tree', '-r', '--name-only', commit, '--', prefix)
    return [p for p in r.stdout.split('\n') if p] if r.returncode == 0 else []


def run_check(commit, freeze=None, stage='E', log=None, meta=None):
    r = git('diff', '--name-status', '--no-renames', D, commit)
    rows = [tuple(l.split('\t')) for l in r.stdout.splitlines() if l]
    check('G', 'delta(D, commit) is exactly the governed execution paths plus record files',
          r.returncode == 0 and governed_ok(rows))
    prereg = show(commit, PREREG)
    rel = [p[len(RDIR):] for p in tree_files(commit, RDIR)]
    table = pins(prereg)
    check('R', 'the record directory holds only its permitted files', record_ok(rel, table, bool(freeze), stage))
    files = {}
    for p in table:
        b = subprocess.run(['git', 'show', '%s:%s%s' % (commit, RDIR, p)], capture_output=True)
        if b.returncode == 0:
            files[p] = b.stdout
    check('P', 'the pinned evidence is present with its digests; the four required files are pinned%s'
          % ('; no pin is pending' if freeze else ''), pins_ok(table, files, bool(freeze)))
    bad_ev = sorted(p for p, b in files.items() if not evidence_ok(b.decode('utf-8', 'replace')))
    check('P', 'every pinned evidence file is a structured expected result with its form stated and no run-varying '
               'field%s' % (' (fails: %s)' % ', '.join(bad_ev) if bad_ev else ''), not bad_ev)
    if RUN_EVIDENCE in files:
        check('P', 'the predicted tree\'s retained run names the predicted tree, is green, and places the module\'s '
                   'build line, reports and gate inside its served window',
              run_window_ok(files[RUN_EVIDENCE].decode('utf-8', 'replace'), predicted_head(prereg)))
    if freeze:
        rv = git('rev-list', '--parents', '%s..%s' % (D, commit))
        revs = [(l.split()[0], l.split()[1:]) for l in rv.stdout.split('\n') if l]
        ddf = git('diff', '--name-only', '--no-renames', D, freeze).stdout.split()
        check('T', 'D..commit is one chain of single-parent commits through F; delta(D, F) is the control plane; the '
                   'preregistration is F\'s', rv.returncode == 0 and chain_ok(revs, D, freeze, commit, ddf, prereg,
                                                                              show(freeze, PREREG)))
        check('P', 'F\'s exact-head run is retained, names F, is green on every job and places the module\'s build '
                   'line, reports and gate inside its served window', run_window_ok(show(commit, FRUN) or '', freeze))
    me = open(os.path.abspath(__file__), encoding='utf-8').read()
    check('B', 'the probe is the frozen blob and controls.py at commit is the file running',
          git('rev-parse', '%s:%s' % (commit, PROBE)).stdout.strip() == PROBE_BLOB and show(commit, CONTROLS) == me)
    mod = show(commit, MOD)
    landed = landed_texts(lambda p: show(D, p))
    good = module_checks(mod, landed_d=landed, closure_names=closure_names_at_d())
    ball_check(landed)
    exact_checks(mod)
    d_imp, d_cen, d_wf = show(D, IMPORTS), show(D, CENSUS), show(D, WORKFLOW)
    check('I', 'OIBridge.lean is D\'s with exactly the frozen import line', imports_want(d_imp) == show(commit, IMPORTS))
    check('C', 'the census is D\'s with exactly the frozen family after BG-2\'s', census_want(d_cen) == show(commit, CENSUS))
    check('W', 'verify.yml is D\'s with exactly the five frozen splices', workflow_want(d_wf) == show(commit, WORKFLOW))
    note = show(commit, RESULT)
    if note is not None:
        if log is None:
            check('V', 'the result note is read against the exact-head bridge log (--log required)', False)
        else:
            toks = cells(mod, good, log, all(CODES_RUN.get(c) for c in EXACT_CODES), run_probe(show(commit, PROBE) or ''),
                         meta)
            if isinstance(toks, tuple):
                check('V', 'the cells are read from complete evidence (VOID: %s)' % toks[1], False)
            else:
                ok, ph = note_ok(note, toks)
                check('V', 'the result note states exactly %s, the earned reading iff all are positive, the '
                           'non-inference rule, and no frozen phrase%s' % (toks, (' (found %s)' % ph) if ph else ''), ok)
    return mod, good


EXACT_CODES = ('X1', 'X2', 'X3', 'CX1', 'CX2', 'CX3', 'CX4')
REQUIRED_CODES = {'G', 'R', 'P', 'T', 'B', 'N1', 'N2', 'N3', 'S1', 'S2', 'S3', 'S4', 'S5', 'I', 'C', 'W'} | set(EXACT_CODES)


def gate_verdict(codes_run, fails):
    """Tokens may be printed only when every required control ran and none failed."""
    return not fails and REQUIRED_CODES <= {c for c, ok in codes_run.items() if ok}


def imports_want(d):
    return d.replace(ANCHOR_IMPORT, ANCHOR_IMPORT + NEW_IMPORT, 1) if d and d.count(ANCHOR_IMPORT) == 1 else None


def census_want(d):
    if not d:
        return None
    dd = json.loads(d)
    ks = [i for i, f in enumerate(dd['families']) if f['modules'] == PREV_FAMILY_MODULES]
    if len(ks) != 1:
        return None
    dd['families'].insert(ks[0] + 1, CENSUS_FAMILY)
    return json.dumps(dd, indent=2, ensure_ascii=False) + '\n'


def workflow_want(d):
    if not d:
        return None
    for a, b in SPLICES:
        if d.count(a) != 1:
            return None
        d = d.replace(a, b)
    return d


def print_verdict(commit, freeze, logpath, metapath=None):
    log = open(logpath, encoding='utf-8', errors='replace').read() if logpath and os.path.isfile(logpath) else ''
    meta = None
    if metapath:
        try:
            meta = json.load(open(metapath, encoding='utf-8'))
        except (OSError, ValueError):
            meta = {}
    mod, good = run_check(commit, freeze, 'E', log, meta)
    if not gate_verdict(CODES_RUN, FAILS):
        print('VERDICT  VOID  (a required control failed or did not run: %s)'
              % ' '.join(sorted(set(FAILS) | (REQUIRED_CODES - set(CODES_RUN)))))
        FAILS.append('VOID')
        return
    f = log_facts(log, mod)
    print('LOG  %s' % json.dumps(window_facts(f), sort_keys=True))
    toks = cells(mod, good, log, True, run_probe(show(commit, PROBE) or ''), meta)
    if isinstance(toks, tuple):
        print('VERDICT  VOID  (%s)' % toks[1])
        FAILS.append('VOID')
        return
    for cell, tok in zip(('Q-NONELL', 'Q-CEX', 'Q-EXACT'), toks):
        print('VERDICT  %-8s  %s' % (cell, tok))


# ---- self-test ---------------------------------------------------------------------------------------------------
def capture(fn):
    """Run fn with fresh failure state; return (codes failed, codes run)."""
    saved = (list(FAILS), COUNT[0], dict(CODES_RUN))
    del FAILS[:]
    CODES_RUN.clear()
    import io
    old, sys.stdout = sys.stdout, io.StringIO()
    try:
        fn()
    finally:
        sys.stdout = old
    got = (set(FAILS), dict(CODES_RUN))
    FAILS[:] = saved[0]
    COUNT[0] = saved[1]
    CODES_RUN.clear()
    CODES_RUN.update(saved[2])
    return got


def must_fail(label, code, fn, only=False):
    failed, _ = capture(fn)
    check('M', '%s fails %s%s' % (label, code, ' alone' if only else ''),
          code in failed and (not only or failed == {code}))


def must_pass(label, fn):
    failed, _ = capture(fn)
    check('M', '%s passes (failed: %s)' % (label, sorted(failed) or 'none'), not failed)


def replace_once(text, a, b):
    assert text.count(a) == 1, a
    return text.replace(a, b)


def self_test():
    mod = cat_blob(MOD_BLOB)
    probe = cat_blob(PROBE_BLOB)
    check('ST', 'the frozen module and probe are readable by blob id', mod is not None and probe is not None)
    if mod is None or probe is None:
        return
    check('ST', 'the frozen texts are the frozen blobs', blob_id(mod) == MOD_BLOB and blob_id(probe) == PROBE_BLOB)
    landed = landed_texts(lambda p: show(D, p))
    cn = closure_names_at_d()
    mc = lambda m, ld=landed: (lambda: module_checks(m, landed_d=ld, closure_names=cn))
    must_pass('the frozen module', mc(mod))
    must_pass('the landed ball control', lambda: ball_check(landed))
    # N1-N3, S1, S2, S4, S5
    must_fail('an extra declaration', 'N1', mc(replace_once(mod, '/-! ### §B — the seed -/',
                                                            'theorem extra_t : True := trivial\n\n/-! ### §B — the seed -/')))
    must_fail('a changed hypothesis of conv_core', 'N2', mc(replace_once(mod, '(ha : 0 ≤ a) (hb : 0 ≤ 1 - a)',
                                                                       '(ha : 0 < a) (hb : 0 ≤ 1 - a)')), only=True)
    must_fail('a changed seed4 constant', 'N2', mc(replace_once(mod, 'AffineMap.const ℝ (Fin 4 → ℝ) (1 / 2 : ℝ)',
                                                               'AffineMap.const ℝ (Fin 4 → ℝ) (1 / 3 : ℝ)')))
    must_fail('J replaced by a rotation in omega4Drive', 'N2', mc(replace_once(mod, '  J := cyc4\n',
                                                                              '  J := rot4 (Real.pi / 2)\n')))
    must_pass('a proof-only repair', mc(replace_once(mod, '    omega4_convex omega4_interior_nonempty hG hT)\n\n'
                                                          'theorem not_denseBoundaryOrbit_omega4',
                                                     '    omega4_convex (omega4_interior_nonempty) hG hT)\n\n'
                                                     'theorem not_denseBoundaryOrbit_omega4')))
    must_fail('a sorry in a proof', 'N3', mc(replace_once(mod, 'relStrictConvex_of_strictConvex omega4_strictConvex',
                                                         'sorry')), only=True)
    must_fail('native_decide in a proof', 'N3', mc(replace_once(mod, '  exacts [h0, h1, h2, h3]',
                                                               '  exacts [h0, h1, h2, h3] <;> native_decide')))
    must_fail('the exponent of the last coordinate 4 -> 2 in omega4 (the body becomes the ball)', 'S1',
              mc(replace_once(mod, 'def omega4 : Set (Fin 4 → ℝ) := {v | (v 0 ^ 2 + v 1 ^ 2 + v 2 ^ 2) ^ 2 + v 3 ^ 4 ≤ 1}',
                              'def omega4 : Set (Fin 4 → ℝ) := {v | (v 0 ^ 2 + v 1 ^ 2 + v 2 ^ 2) ^ 2 + v 3 ^ 2 ≤ 1}')))
    must_fail('RelStrictConvex dropped from kinfTrans_separation', 'S1',
              mc(replace_once(mod, '      ∧ RelStrictConvex omega4 ∧ CentrallySymmetric omega4 0\n',
                              '      ∧ CentrallySymmetric omega4 0\n')))
    must_fail('nonempty interior dropped from kinfTrans_separation', 'S1',
              mc(replace_once(mod, 'IsCompact omega4 ∧ Convex ℝ omega4 ∧ (interior omega4).Nonempty\n',
                              'IsCompact omega4 ∧ Convex ℝ omega4\n')))
    must_fail('PreservesBody dropped from not_boundaryTransitive_omega4', 'S1',
              mc(replace_once(mod, '    (hG : PreservesBody omega4 G) : ¬ BoundaryTransitive omega4 G := fun hT =>',
                              '    : ¬ BoundaryTransitive omega4 G := fun hT =>')))
    must_fail('not_affine_eball_omega4 stated against eball 3', 'S1',
              mc(replace_once(mod, "A '' omega4 = eball 4 := by", "A '' omega4 = eball 3 := by")))
    must_fail('a local eball shadowing the landed one', 'S2',
              mc(replace_once(mod, '/-! ### §D — Ω₄ is no affine image of the ball -/',
                              'def eball (d : ℕ) : Set (Fin d → ℝ) := Set.univ\n\n'
                              '/-! ### §D — Ω₄ is no affine image of the ball -/')))
    must_fail('DenseOrbit dropped from the open line', 'S2',
              mc(replace_once(mod, OPEN_LINE + '\n', OPEN_LINE[:-len(' DenseOrbit')] + '\n')))
    must_fail('a second import', 'S2', mc(replace_once(mod, 'import OIBridge.DenseOrbit\n',
                                                       'import OIBridge.DenseOrbit\nimport OIBridge.K2Guard\n')))
    bad_landed = dict(landed)
    bad_landed['exists_affine_image_eq_eball'] = (landed['exists_affine_image_eq_eball'] or '') + ' '
    must_fail('a landed statement that differs at D', 'S2', mc(mod, bad_landed), only=True)
    bad_ball = dict(landed)
    bad_ball['boundaryTransitive_fullAut'] = 'theorem boundaryTransitive_fullAut : True'
    must_fail('a landed ball control that differs at D', 'S3', lambda: ball_check(bad_ball), only=True)
    must_fail('"replaces K∞-Trans" in the header', 'S4',
              mc(replace_once(mod, 'The statements\n  concern Ω₄ alone', 'This replaces K∞-Trans. The statements\n'
                                                                        '  concern Ω₄ alone')))
    must_fail('"for every body" in the header', 'S4',
              mc(replace_once(mod, 'concern Ω₄ alone, in ℝ⁴.', 'concern every body.')))
    must_fail('"if and only if" in the header', 'S4',
              mc(replace_once(mod, 'concern Ω₄ alone, in ℝ⁴.',
                              'concern Ω₄ alone, if and only if in ℝ⁴.')))
    last = '#print axioms OIBridge.TransSeparation.kinfTrans_separation\n'
    must_fail('a sixteenth print', 'S5', mc(replace_once(mod, last, last + '#print axioms OIBridge.TransSeparation.vec4_ext\n')))
    must_fail('a duplicated print', 'S5', mc(replace_once(mod, last, last + last)))
    # the exact layer
    must_pass('the exact layer', lambda: exact_checks(mod))
    must_fail('an outer point moved inside Omega4', 'X1',
              lambda: exact_checks(mod, outer=[us(Fr(1, 2), Fr(1, 2))] + OUTER[1:]))
    must_fail('a certificate weight changed', 'X2', lambda: exact_checks(mod, wo=[Fr(3, 2)] + W_OUTER[1:]), only=True)
    must_fail('a zero weight (no certificate)', 'X2',
              lambda: exact_checks(mod, wi=[Fr(0)] + W_INNER[1:], wo=W_OUTER), only=True)
    must_fail('a module point changed (5/6 -> 4/5)', 'X3',
              lambda: exact_checks(replace_once(mod, 'have i5 := hin ![5 / 6, 0, 0, 5 / 6]',
                                                'have i5 := hin ![4 / 5, 0, 0, 5 / 6]')), only=True)
    must_fail('the ball\'s witness replaced by the zero form', 'CX1',
              lambda: exact_checks(mod, ball_x=[Fr(0)] * 6), only=True)
    must_fail('the translations replaced by the identity', 'CX2',
              lambda: exact_checks(mod, translate=lambda a, b: (0, 0, 0, 0)), only=True)
    must_fail('the half-space translations given a nonzero last coordinate', 'CX3',
              lambda: exact_checks(mod, h_last=Fr(1, 2)), only=True)
    must_fail('the segment family {id, -id} replaced by {id}', 'CX4',
              lambda: exact_checks(mod, seg_map=lambda v: v), only=True)
    check('M', 'the ball certificate premise: the Omega4 weights do not certify infeasibility on the ball\'s states',
          not farkas([us(1, 0), us(-1, 0), us(0, 1), us(0, -1)] + [us(a, b) for a in (Fr(3, 5), Fr(-3, 5))
                                                                    for b in (Fr(4, 5), Fr(-4, 5))],
                     OUTER, W_INNER, W_OUTER))
    # the probe: a tooling failure is VOID, a complete run with a failing check is negative
    prun = run_probe(probe)
    ver, out = prun[0], prun[2]
    check('M', 'the frozen probe, run under sympy %s, prints the frozen output' % SYMPY_VERSION,
          probe_state(prun) == 'exact' and probe_ok(out))
    isvoid = lambda x: isinstance(x, tuple) and x[0] == 'void'
    check('M', 'a probe that crashes is VOID', isvoid(probe_state(run_probe('print("PASS D1")\nraise SystemExit(3)\n'))))
    check('M', 'a probe whose import fails is VOID', isvoid(probe_state(run_probe('import no_such_module_ktrans_sep\n'))))
    check('M', 'sympy absent, or another sympy version, is VOID',
          isvoid(probe_state((None, 0, out, ''))) and isvoid(probe_state(('1.13.0', 0, out, ''))))
    check('M', 'a complete run with one PASS turned FAIL is negative, not VOID',
          probe_state((ver, 0, out.replace('PASS D9', 'FAIL D9', 1), '')) == 'negative')
    check('M', 'a complete run with a countercontrol that did not fail is negative',
          probe_state((ver, 0, out.replace('COUNTER XW2 fails as stated', 'COUNTER XW2 DID NOT FAIL', 1), '')) == 'negative')
    summary = '\n'.join(l for l in out.split('\n') if l.startswith(('checks:', 'VERDICT'))) + '\n'
    check('M', 'the summary and verdict lines alone are VOID (no vacuous exact cell)',
          isvoid(probe_state((ver, 0, summary, ''))) and not probe_ok(summary))
    check('M', 'an empty output, or one cut before its verdict, is VOID',
          isvoid(probe_state((ver, 0, '', ''))) and isvoid(probe_state((ver, 0, out.split('checks:')[0], '')))
          and not probe_ok('') and not probe_ok(None))
    check('M', 'an output that differs in a non-check line is VOID',
          isvoid(probe_state((ver, 0, out.replace('grid: 1669', 'grid: 1670', 1), ''))))
    # the log and the cells
    pl = {l[len('#print axioms ' + NS):].strip(): n for n, l in print_lines(mod)}
    std = '[propext, Classical.choice, Quot.sound]'
    rep = lambda n, ax=std: "info: OIBridge/TransSeparation.lean:%d:0: '%s%s' depends on axioms: %s" % (pl[n], NS, n, ax)
    built = 'ℹ [3642/3644] Built OIBridge.TransSeparation (12s)'
    gate = 'release gate\n  PASS  lean-axioms  ok\n  PASS  lean-manuscript  ok\nrelease gate: PASS\n'
    head = '2026-10-10T23:54:47.9382674Z '
    log_ok = head + built + '\n' + '\n'.join(head + rep(n) for n in PRINTS) + \
        '\nBuild completed successfully (3644 jobs).\n' + gate
    good = set(KEY)
    P_, N_ = [TOK_NONELL[0], TOK_CEX[0], TOK_EXACT[0]], [TOK_NONELL[1], TOK_CEX[1], TOK_EXACT[1]]
    c = lambda lg, ex=True, pr=prun, meta=None, gk=good: cells(mod, gk, lg, ex, pr, meta)
    sorry = lambda n: rep(n, '[propext, sorryAx, Classical.choice, Quot.sound]')
    check('M', 'a complete log with every frozen report standard gives the three positive tokens', c(log_ok) == P_)
    check('M', 'the window facts place the build line before the fifteen reports and the gate after them',
          (lambda w: w['built_line'] == 1 and sorted(w['report_lines'].values()) == list(range(2, 17))
           and w['gate_start'] == 18 and w['gate_end'] == 21)(window_facts(log_facts(log_ok, mod))))
    check('M', 'an empty log is VOID', isvoid(c('')))
    check('M', 'a log truncated before the module\'s build line is VOID',
          isvoid(c(log_ok.replace(head + built + '\n', ''))))
    check('M', 'a log truncated inside the report block is VOID',
          isvoid(c('\n'.join(log_ok.split('\n')[6:]))))
    check('M', 'a missing report is VOID', isvoid(c(log_ok.replace(head + rep('kinfTrans_separation') + '\n', ''))))
    check('M', 'a duplicated report is VOID', isvoid(c(log_ok.replace(head + rep('conv_core'),
                                                                      head + rep('conv_core') + '\n' + rep('conv_core')))))
    check('M', 'a report at another line is VOID',
          isvoid(c(log_ok.replace(rep('conv_core'), rep('conv_core').replace(':%d:0' % pl['conv_core'], ':1:0')))))
    check('M', 'a report line that does not parse (a wrapped axiom list) is VOID',
          isvoid(c(log_ok.replace(rep('conv_core'), rep('conv_core')[:-1]))))
    check('M', 'a log without the gate\'s verdict line is VOID', isvoid(c(log_ok.replace('release gate: PASS\n', ''))))
    check('M', 'a gate failing at a step outside the module, with clean reports, is VOID',
          isvoid(c(log_ok.replace('  PASS  lean-manuscript', '  FAIL  legacy-records')
                   .replace('release gate: PASS', 'release gate: FAILED -> legacy-records'))))
    check('M', 'a build that did not complete, without module errors, is VOID',
          isvoid(c(log_ok.replace('Build completed successfully (3644 jobs).', ''))))
    check('M', 'sorryAx with a passing gate (inconsistent evidence) is VOID',
          isvoid(c(log_ok.replace(rep('omega4_strictConvex'), sorry('omega4_strictConvex')))))
    sci = log_ok.replace(rep('omega4_strictConvex'), sorry('omega4_strictConvex')) \
        .replace('  PASS  lean-axioms', '  FAIL  lean-axioms').replace('release gate: PASS', 'release gate: FAILED -> lean-axioms')
    check('M', 'sorryAx in a report with the gate failing at lean-axioms alone is negative in both kernel cells',
          c(sci) == [N_[0], N_[1], P_[2]])
    brk = log_ok.replace(rep('omega4_strictConvex'), sorry('omega4_strictConvex')) \
        .replace('Build completed successfully (3644 jobs).', 'error: OIBridge/TransSeparation.lean:157:16: Type mismatch') \
        .split('release gate\n')[0]
    check('M', 'sorryAx with a module build error and no gate is negative in both kernel cells',
          c(brk) == [N_[0], N_[1], P_[2]])
    check('M', 'a failed load-bearing statement reads the cells that rest on it negative',
          c(log_ok, gk=good - {'kinfTrans_separation'}) == [P_[0], N_[1], P_[2]]
          and c(log_ok, gk=good - {'not_affine_eball_omega4'}) == [N_[0], N_[1], P_[2]])
    check('M', 'a failed exact control is VOID', isvoid(c(log_ok, ex=False)))
    check('M', 'a probe crash is VOID and a complete failing probe run is negative in Q-EXACT alone',
          isvoid(c(log_ok, pr=(ver, 1, '', 'Traceback'))) and
          c(log_ok, pr=(ver, 0, out.replace('PASS D9', 'FAIL D9', 1), '')) == [P_[0], P_[1], N_[2]])
    nl = len(log_ok.split('\n'))
    check('M', 'log metadata: a full-length window passes; a count that does not match the text, or a served count '
               'above the original, is VOID',
          c(log_ok, meta={'original_lines': nl, 'served_lines': nl}) == P_
          and c(log_ok, meta={'original_lines': nl + 100, 'served_lines': nl}) == P_
          and isvoid(c(log_ok, meta={'original_lines': nl, 'served_lines': nl - 1}))
          and isvoid(c(log_ok, meta={'original_lines': nl - 1, 'served_lines': nl})) and isvoid(c(log_ok, meta={})))
    # the verdict gate (no tokens over a failed or missing control)
    full = {c: True for c in REQUIRED_CODES}
    check('M', 'every required control green: tokens may be printed', gate_verdict(full, []))
    check('M', 'one required control failed: no token', all(not gate_verdict(dict(full, **{c: False}), [c])
                                                            for c in REQUIRED_CODES))
    check('M', 'one required control never ran: no token',
          all(not gate_verdict({k: v for k, v in full.items() if k != c}, []) for c in REQUIRED_CODES))
    # the note
    note = 'Q-NONELL %s\nQ-CEX %s\nQ-EXACT %s\n\n%s\n\n%s\n' % (P_[0], P_[1], P_[2], EARNED, NONINF)
    check('M', 'a note with the three tokens, the earned reading and the rule passes', note_ok(note, P_)[0])
    check('M', 'a note with an extra token fails', not note_ok(note + TOK_EXACT[1] + '\n', P_)[0])
    check('M', 'a note with the earned reading altered fails', not note_ok(note.replace('counterexample', 'example'), P_)[0])
    check('M', 'a note without the non-inference rule fails', not note_ok(note.replace(NONINF, ''), P_)[0])
    check('M', 'a note stating the earned reading under a negative cell fails',
          not note_ok(note.replace(P_[1], N_[1]), [P_[0], N_[1], P_[2]])[0])
    check('M', 'a note with "every compact convex body" outside the frozen texts fails',
          not note_ok(note + 'This holds for every compact convex body.\n', P_)[0])
    check('M', 'a neutral addition passes', note_ok(note + 'The exact-head run was green on every job.\n', P_)[0])
    # imports, census, workflow
    d_imp, d_cen, d_wf = show(D, IMPORTS), show(D, CENSUS), show(D, WORKFLOW)
    gi = imports_want(d_imp)
    check('M', 'imports: the frozen edit is well defined, and the unchanged file and a moved line differ from it',
          gi is not None and gi != d_imp and gi != d_imp.replace('import OIBridge.DenseOrbit\n',
                                                                 'import OIBridge.DenseOrbit\n' + NEW_IMPORT, 1))
    gc = census_want(d_cen)
    dd = json.loads(gc)
    k = [i for i, fm in enumerate(dd['families']) if fm['modules'] == ['TransSeparation']]
    bad = json.loads(gc)
    bad['families'][k[0]]['status'] = 'carried'
    check('M', 'census: the family is inserted once after BG-2\'s; a changed status, a moved family and a whitespace '
               'change differ from the frozen edit',
          len(k) == 1 and dd['families'][k[0] - 1]['modules'] == PREV_FAMILY_MODULES
          and json.dumps(bad, indent=2, ensure_ascii=False) + '\n' != gc and gc.replace('\n', '\n ', 1) != gc
          and gc != d_cen)
    gw = workflow_want(d_wf)
    check('M', 'workflow: the five splices apply once each; without the aggregate test line or the shard it differs',
          gw is not None and gw.replace('          test "${KTRANSSEP1_RESULT}" = success\n', '') != gw
          and gw.replace(SHARD, '') != gw and gw.count('probes_ktranssep1') == 3 and
          workflow_want(gw) is None)
    # governed paths, record, pins, chain, F's run
    rows = [('A', p) for p in (MOD, PROBE)] + [('M', p) for p in (IMPORTS, CENSUS, WORKFLOW)] + \
        [('A', PREREG), ('A', CONTROLS)]
    check('M', 'governed: the frozen paths pass; an extra path, a missing path and a deletion fail',
          governed_ok(rows) and not governed_ok(rows + [('M', 'verification/ROADMAP.md')])
          and not governed_ok(rows[1:]) and not governed_ok(rows + [('D', RDIR + 'evidence/design-run-1.json')]))
    table = {p: '0' * 64 for p in REQUIRED_EVIDENCE}
    base = ['preregistration.md', 'controls.py'] + REQUIRED_EVIDENCE
    check('M', 'record: the predicted tree passes; with --freeze, F\'s run and at E the note are required; an extra file '
               'fails; the note at S1 fails',
          record_ok(base, table, False, 'E') and not record_ok(base, table, True, 'S1')
          and record_ok(base + ['evidence/f-run/results.json'], table, True, 'S1')
          and not record_ok(base + ['evidence/f-run/results.json'], table, True, 'E')
          and record_ok(base + ['evidence/f-run/results.json', 'result.md'], table, True, 'E')
          and not record_ok(base + ['notes.txt'], table, False, 'E')
          and not record_ok(base + ['evidence/f-run/results.json', 'result.md'], table, True, 'S1'))
    files = {p: p.encode() for p in REQUIRED_EVIDENCE}
    tab = {p: hashlib.sha256(p.encode()).hexdigest() for p in REQUIRED_EVIDENCE}
    check('M', 'pins: matching digests pass; a changed file, a missing file, a dropped required row fail; a pending pin '
               'passes without --freeze and fails with it',
          pins_ok(tab, files, True) and not pins_ok(tab, dict(files, **{REQUIRED_EVIDENCE[0]: b'x'}), True)
          and not pins_ok(tab, {k: v for k, v in files.items() if k != REQUIRED_EVIDENCE[1]}, True)
          and not pins_ok({k: v for k, v in tab.items() if k != REQUIRED_EVIDENCE[3]}, files, False)
          and pins_ok(dict(tab, **{REQUIRED_EVIDENCE[3]: None}), files, False)
          and not pins_ok(dict(tab, **{REQUIRED_EVIDENCE[3]: None}), files, True))
    check('M', 'pins: the table reader reads a pinned row and a pending row and nothing else',
          pins('| `evidence/a.json` | `%s` |\n| `evidence/b.json` | pending |\n| `x` | `y` |' % ('a' * 64))
          == {'evidence/a.json': 'a' * 64, 'evidence/b.json': None})
    d_, f_, s_, e_ = 'd' * 40, 'f' * 40, '5' * 40, 'e' * 40
    revs = [(e_, [s_]), (s_, [f_]), (f_, [d_])]
    dl = [PREREG]
    check('M', 'chain: a linear D-F-S1-E chain passes; a merge, a re-cut F off the chain, an F not on D, a control-plane '
               'change after F and a non-control-plane path in delta(D, F) fail',
          chain_ok(revs, d_, f_, e_, dl, 'p', 'p')
          and not chain_ok([(e_, [s_, d_]), (s_, [f_]), (f_, [d_])], d_, f_, e_, dl, 'p', 'p')
          and not chain_ok(revs, d_, 'a' * 40, e_, dl, 'p', 'p')
          and not chain_ok([(e_, [s_]), (s_, [f_]), (f_, ['b' * 40])], d_, f_, e_, dl, 'p', 'p')
          and not chain_ok(revs, d_, f_, e_, dl, 'p', 'q')
          and not chain_ok(revs, d_, f_, e_, dl + [MOD], 'p', 'p')
          and chain_ok(revs, d_, f_, e_, dl + [RDIR + 'amendments/A1.md'], 'p', 'p'))
    # the retained results: form, no run-varying field, and the served window of a run's result
    ev = {'schema': 'oi-evidence-result', 'version': 1, 'form': 'derived', 'source': {'served_sha256': 'a' * 64}}
    check('M', 'evidence: a derived result with a source digest passes; no form, an unknown form, a derived result '
               'without a digest, a timestamp field and a duration field fail',
          evidence_ok(json.dumps(ev)) and evidence_ok(json.dumps(dict(ev, form='complete', source={})))
          and not evidence_ok(json.dumps({k: v for k, v in ev.items() if k != 'form'}))
          and not evidence_ok(json.dumps(dict(ev, form='copied')))
          and not evidence_ok(json.dumps(dict(ev, source={'kind': 'x'})))
          and not evidence_ok(json.dumps(dict(ev, run={'created_at': '2026-10-18T00:00:00Z'})))
          and not evidence_ok(json.dumps(dict(ev, run={'duration': 3}))) and not evidence_ok('not json'))
    rl = {n: 100 + i for i, n in enumerate(PRINTS)}
    run_ev = dict(ev, run={'head_sha': f_, 'event': 'workflow_dispatch'}, jobs=[{'name': 'a', 'conclusion': 'success'}],
                  source={'served_sha256': 'a' * 64, 'original_lines': 9000, 'served_lines': 5000},
                  observed={'transseparation_window': {'served_lines': 5000, 'built_line': 99, 'report_lines': rl,
                                                        'gate_start': 200, 'gate_end': 230}},
                  expected={'build_success': True, 'gate': {'verdict': 'PASS'},
                            'modules': {'OIBridge/TransSeparation.lean': {
                                'status': 'complete', 'reports': [{'name': NS + n, 'axioms': sorted(ALLOWED_AXIOMS)}
                                                                  for n in PRINTS]}}})

    def rw(**kw):
        d = json.loads(json.dumps(run_ev))
        for path, v in kw.items():
            x = d
            ks = path.split('__')
            for k in ks[:-1]:
                x = x[k]
            x[ks[-1]] = v
        return json.dumps(d)
    check('M', 'a run result naming its head, green, with the window in order passes; another head, a push event, a '
               'failed job, no jobs, a report past the window, the build line after a report, a missing report, the '
               'gate inside the reports, a gate past the window, a non-standard axiom and a failed gate fail',
          run_window_ok(json.dumps(run_ev), f_) and not run_window_ok(json.dumps(run_ev), e_)
          and not run_window_ok(rw(run__event='push'), f_)
          and not run_window_ok(rw(jobs=[{'name': 'a', 'conclusion': 'failure'}]), f_)
          and not run_window_ok(rw(jobs=[]), f_)
          and not run_window_ok(rw(observed__transseparation_window__report_lines=dict(rl, conv_core=5001)), f_)
          and not run_window_ok(rw(observed__transseparation_window__built_line=150), f_)
          and not run_window_ok(rw(observed__transseparation_window__report_lines={k: v for k, v in rl.items()
                                                                                    if k != 'conv_core'}), f_)
          and not run_window_ok(rw(observed__transseparation_window__gate_start=105), f_)
          and not run_window_ok(rw(observed__transseparation_window__gate_end=5001), f_)
          and not run_window_ok(rw(expected__modules={'OIBridge/TransSeparation.lean': {
              'status': 'complete', 'reports': [{'name': NS + n, 'axioms': ['sorryAx']} for n in PRINTS]}}), f_)
          and not run_window_ok(rw(expected__gate={'verdict': 'FAILED -> lean-axioms'}), f_)
          and not run_window_ok('not json', f_))
    check('M', 'the predicted head is read from the predicted-tree section and nowhere else',
          predicted_head('x\n### The predicted execution tree\n\n- **`%s`** (a child of D)\n' % f_) == f_
          and predicted_head('- **`%s`**\n' % f_) is None)


def main(argv):
    if argv == ['--self-test']:
        self_test()
    elif argv == ['exact']:
        mod = show('HEAD', MOD) or cat_blob(MOD_BLOB)
        exact_checks(mod)
        print('EXACT  %s' % ('AS STATED' if not FAILS else 'NOT AS STATED'))
    elif len(argv) >= 2 and argv[0] in ('check', 'verdict'):
        opts = dict(zip(argv[2::2], argv[3::2]))
        if len(argv) % 2 or not set(opts) <= {'--freeze', '--stage', '--log', '--log-meta'} or \
                opts.get('--stage', 'E') not in ('E', 'S1'):
            print(__doc__)
            return 2
        if argv[0] == 'check':
            log, meta = None, None
            if '--log' in opts:
                log = open(opts['--log'], encoding='utf-8', errors='replace').read()
            if '--log-meta' in opts:
                meta = json.load(open(opts['--log-meta'], encoding='utf-8'))
            run_check(argv[1], opts.get('--freeze'), opts.get('--stage', 'E'), log, meta)
        else:
            if '--freeze' not in opts or '--log' not in opts:
                print(__doc__)
                return 2
            print_verdict(argv[1], opts['--freeze'], opts['--log'], opts.get('--log-meta'))
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
