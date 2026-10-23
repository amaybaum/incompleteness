#!/usr/bin/env python3
"""controls.py -- round KTRANS-SEP-2's own controls, frozen with the preregistration beside it.

Imports nothing from the repository and changes nothing. It reads D and the commits it is given through read-only git
commands, embeds every frozen text it compares against, and runs the frozen probe from a temporary copy of its blob.
Standard library only; the probe it runs needs sympy 1.14.0.

    python3 -I -B controls.py check <commit> [--freeze F] [--stage S1] [--log LOG [--log-meta META]]
    python3 -I -B controls.py verdict <commit> --freeze F --log LOG --log-meta META
    python3 -I -B controls.py exact
    python3 -I -B controls.py axioms STEP_OUTPUT
    python3 -I -B controls.py derive-run --log LOG --log-meta META --run-api RUN --jobs-api JOBS
    python3 -I -B controls.py mock-s1 <candidate F> --f-run FILE --predicted P --log LOG --log-meta META
                                      --run-api RUN --jobs-api JOBS [--evidence REL=FILE ...]
    python3 -I -B controls.py --self-test

`check` runs every control below at <commit>. With --freeze it adds T and the retention checks that need F; without
it (the predicted execution tree) those are skipped and a pending pin is allowed. --stage S1 is the commit before the
result note; the default stage is E, at which the result note is required when --freeze is given. LOG is the served
text of the Mathlib bridge job of the exact-head run at <commit>; it is required at a commit carrying the result note.
META is a JSON object {"original_lines": N, "served_lines": M} for that text: N is the serving tool's line count of
the whole log (the job-log tool's original_length), M the number of lines of the text as served, which ends without
a newline. LOG is saved as served (the tool's logs_content, JSON-decoded), and every reader reads it as bytes
decoded as UTF-8 with a leading byte-order mark dropped and no newline translation. Its jobs answer must list every
job of the run in one answer (per_page 100).

`verdict` runs `check` first and prints the three cell tokens only when every control of `check` ran and passed and
the evidence the cells read is complete; otherwise it prints `VERDICT  VOID` with the reason, prints no token and exits
1. VOID is not an outcome: a tooling failure or incomplete evidence never yields a NOT-ESTABLISHED token.
`exact` runs the independent exact layer (X, CX) alone.
`derive-run` is the frozen recipe for a run result (the predicted tree's run and F's run): it reads the served text
of the run's Mathlib bridge job (LOG, exactly as served), META for it, and the runs and jobs API answers for the run
(RUN, JOBS; a jobs answer is either {"total_count", "jobs"} or that object under "jobs"), and prints the result.
The result is a function of those four inputs alone, and records their digests.
`mock-s1` is the pre-freeze safeguard. It first requires FILE to be exactly derive-run's output over LOG, META, RUN
and JOBS, which are the served bridge log and the API answers of candidate F's ACTUAL exact-head run, and P to be the
predicted tree candidate F's preregistration names. It then builds, in a temporary object directory and with no ref,
a mock stage-1 commit on the candidate F: candidate F's tree plus the predicted tree P's record and execution files,
each --evidence file at its record path (the pinned files stage 1 adds that P cannot carry, such as P's own run
result), and FILE as evidence/f-run/results.json, and runs `check <mock> --freeze <candidate F> --stage S1` on it,
so that a control F's own run can never satisfy fails before F is designated rather than after.

Controls (each prints PASS or FAIL with its code):
  G   governed   delta(D, commit) is exactly the five execution paths, with their statuses, plus record files
  R   record     the record directory holds only the preregistration, controls.py, the pinned evidence, F's run
                 (required with --freeze), amendments/ and, at E, the result note
  P   pins       every evidence file the preregistration's retained-evidence table pins is present with its sha256;
                 the table names at least the five required files; with --freeze no pin is pending; each pinned
                 file is a structured result with its form stated and no timestamp or duration field. Each run
                 result is checked for what its stage validates: the predicted tree's run (the proposed
                 implementation) names the predicted tree, is green and places the release gate and then the final
                 step's block for it inside the served window; its second run, on the same branch, does the same
                 after restoring the build cache (no `Built` line for the module) and is another run. With --freeze the
                 predicted-tree section names its commit in the frozen form. At F (the control plane) the module's
                 absence is read from F's tree through git (F's two Lean directories are D's, which carry no module;
                 neither the module's nor the probe's path; no import line), and F's run evidence establishes its
                 identity (F, verify.yml, the Mathlib bridge job, workflow_dispatch, run and job ids, attempt), every
                 job success, exactly the predicted tree's jobs less the round's shard, and the release gate PASS on
                 exactly the predicted tree's steps; that the log has no module lines is checked for consistency
                 only. E's run (the actual execution) is read by `verdict`, which is VOID without the module's
                 evidence
  T   chain      (with --freeze) D..commit is one chain of single-parent commits through F; delta(D, F) is the
                 preregistration and amendments only; the preregistration at commit is F's
  B   blobs      the probe is the frozen blob; controls.py at commit is the file running, and its blob is the one
                 the preregistration pins (with --freeze the pin may not be pending)
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
  I   imports    OIBridge.lean is D's with the frozen import line after `import OIBridge.KTokenMaxCone`
  C   census     the census is D's with the frozen family directly before KTOKEN-MAXCONE-1's family, which stays
                 last, in D's layout
  W   workflow   verify.yml is D's with exactly the six frozen splices (the shard, its four aggregate lines, and the
                 final bridge step after KTOKEN-MAXCONE-1's check A3)
  V   note       at a commit carrying the result note: exactly the computed tokens, the earned reading exactly when
                 all three cells are positive, the non-inference rule always

Cells (verdict), read only when every control passed. The kernel cells read only the final bridge step's block
(the step the sixth splice adds, the job's last: a marker line naming the commit, the module's fifteen reports from
`lake env lean`, and one OK or FAILED line from `controls.py axioms`), and the build-success line and the release-gate
block before it; on a build-cache hit the build output replays every module and lies mostly outside a served tail.
  VOID      the log is empty or its metadata does not describe it; no final-step marker, two, or one naming another
            commit; in the block a report that does not parse, the fifteen prints not each reported once in print
            order, or not exactly one OK or FAILED line after the last report; evidence neither positive nor negative;
            sympy 1.14.0 is absent; the probe did not run to completion, or its output differs from the frozen output
            without a failing check. No token is printed.
  Q-NONELL  KTRANS-SEP-NONELLIPSOID-PROVED   the build-success line and the gate's PASS verdict before the block, and
            in the block every frozen report within [propext, Classical.choice, Quot.sound], the OK line, no error
            line and no forbidden token, with S1 holding for not_affine_eball_omega4
  Q-CEX     KTRANS-SEP-COUNTEREXAMPLE-PROVED  the same, with S1 holding for the four statements and omega4
            Both kernel cells read NOT-ESTABLISHED only from complete evidence of a failure in the module: a complete
            block with a report outside the three axioms and the FAILED line, and a module error line in the block or
            the gate failing at lean-axioms alone
  Q-EXACT   KTRANS-SEP-INSTANCES-EXACT       the probe blob at <commit>, run under sympy 1.14.0 with python3 -I -B,
            prints exactly the frozen output (sha256 below), whose lines include the twelve PASS lines, both COUNTER
            lines, the summary and the verdict; NOT-ESTABLISHED from a complete run in which a check failed
No cell reads another cell's outcome.
"""
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from fractions import Fraction as Fr
from itertools import product

D = '48b18ac54e39920a4fc4bbb8ee1d1b6cebea2c29'
RDIR = 'verification/programmes/oi-qm/reconstruction/round-ktrans-sep-2-omega4/'
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
                     'evidence/predicted-tree-run.json', 'evidence/predicted-tree-replay-run.json']
ALLOWED_AXIOMS = {'propext', 'Classical.choice', 'Quot.sound'}
LEAN_DIRS = ('verification/lean-mathlib', 'verification/lean')
SHARD_JOB = 'Numerical probes / KTRANS-SEP-2 Omega4 counterexample'
ANCHOR_IMPORT = 'import OIBridge.KTokenMaxCone\n'
NEW_IMPORT = 'import OIBridge.TransSeparation\n'
PREV_FAMILY_MODULES = ['KTokenMaxCone']
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
  "name": "Ω₄, the ℓ⁴-sum of the Euclidean 3-ball and the segment, is compact, convex, with interior, drivable, with a sharp seed, relatively strictly convex and centrally symmetric, is no affine image of the Euclidean ball, and admits no body-preserving family that is boundary transitive or has a dense boundary orbit (round KTRANS-SEP-2, reconstruction)",
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
CENSUS_FAMILY = {k: GEN['census_family'][k] for k in ('name', 'modules', 'status', 'manuscript')}  # D's key order
PROBE_LINES = GEN['probe_lines']
# KTRANS-SEP-1's F-run result (run 39940836089, head 7e9aef69), derived from its served log: the module absent.
KTSEP1_FRUN_SHA256 = 'd2ac295647dfb593a09026de51ad145102645dcc98dee1bd7d25988c6623ca8f'
# KTRANS-SEP-1's predicted tree's run result (run 39173554213), the reference its real F run is compared with; read by
# blob id from main, where that round's record directory carries it.
KTSEP1_PTR_BLOB = '458753c8ec14a43bc8a86a5c0aec1d1175935b66'
KTSEP1_PTR_SHA256 = '58fcf6fec66e8c695c923810b67d20040d801f5c8b71adfad561b42855e21ef7'
KTSEP1_SHARD_JOB = 'Numerical probes / KTRANS-SEP-1 Omega4 counterexample'
KTSEP1_FRUN = r'''{
 "schema": "oi-evidence-result",
 "version": 1,
 "form": "derived",
 "kind": "exact-head-run",
 "scope": "what F's exact-head run logged at F (7e9aef69), whose tree is D plus the preregistration alone; nothing about any later tree",
 "run": {
  "workflow": "verify.yml",
  "id": 39940836089,
  "attempt": 1,
  "event": "workflow_dispatch",
  "conclusion": "success",
  "head_branch": "staging/ktrans-sep-824-candF-20261018",
  "head_sha": "7e9aef691f47edaec9111ef5923ed9e946854737",
  "job_id": 120371576458,
  "job_name": "Mathlib bridge",
  "job_conclusion": "success",
  "job_steps": [
   {
    "name": "Set up job",
    "conclusion": "success"
   },
   {
    "name": "Run actions/checkout@v4",
    "conclusion": "success"
   },
   {
    "name": "Install elan",
    "conclusion": "success"
   },
   {
    "name": "Restore the OIBridge build cache",
    "conclusion": "success"
   },
   {
    "name": "Build",
    "conclusion": "success"
   },
   {
    "name": "Release gate",
    "conclusion": "success"
   },
   {
    "name": "Post Restore the OIBridge build cache",
    "conclusion": "success"
   },
   {
    "name": "Post Run actions/checkout@v4",
    "conclusion": "success"
   },
   {
    "name": "Complete job",
    "conclusion": "success"
   }
  ]
 },
 "jobs": [
  {
   "name": "Lean kernel check",
   "conclusion": "success"
  },
  {
   "name": "Mathlib bridge",
   "conclusion": "success"
  },
  {
   "name": "Numerical probes",
   "conclusion": "success"
  },
  {
   "name": "Numerical probes / A36 hierarchy",
   "conclusion": "success"
  },
  {
   "name": "Numerical probes / A38 escape",
   "conclusion": "success"
  },
  {
   "name": "Numerical probes / A40 locus",
   "conclusion": "success"
  },
  {
   "name": "Numerical probes / A41 hulls",
   "conclusion": "success"
  },
  {
   "name": "Numerical probes / A41 independent",
   "conclusion": "success"
  },
  {
   "name": "Numerical probes / A41 production",
   "conclusion": "success"
  },
  {
   "name": "Numerical probes / A42 census01",
   "conclusion": "success"
  },
  {
   "name": "Numerical probes / A42 exclusion (cubes:0)",
   "conclusion": "success"
  },
  {
   "name": "Numerical probes / A42 exclusion (cubes:1)",
   "conclusion": "success"
  },
  {
   "name": "Numerical probes / A42 exclusion (cubes:2)",
   "conclusion": "success"
  },
  {
   "name": "Numerical probes / A42 exclusion (dfs:0)",
   "conclusion": "success"
  },
  {
   "name": "Numerical probes / A42 exclusion (dfs:1)",
   "conclusion": "success"
  },
  {
   "name": "Numerical probes / A42 exclusion (dfs:2)",
   "conclusion": "success"
  },
  {
   "name": "Numerical probes / A42 exclusion (dfs:3)",
   "conclusion": "success"
  },
  {
   "name": "Numerical probes / A42 exclusion (dfs:4)",
   "conclusion": "success"
  },
  {
   "name": "Numerical probes / A42 exclusion (dfs:5)",
   "conclusion": "success"
  },
  {
   "name": "Numerical probes / A42 exclusion (n18:0)",
   "conclusion": "success"
  },
  {
   "name": "Numerical probes / A42 exclusion (n18:1)",
   "conclusion": "success"
  },
  {
   "name": "Numerical probes / A42 exclusion (n18:2)",
   "conclusion": "success"
  },
  {
   "name": "Numerical probes / A42 exclusion (paths)",
   "conclusion": "success"
  },
  {
   "name": "Numerical probes / A42 exclusion (r5)",
   "conclusion": "success"
  },
  {
   "name": "Numerical probes / A42 exclusion (sathr)",
   "conclusion": "success"
  },
  {
   "name": "Numerical probes / A42 witness",
   "conclusion": "success"
  },
  {
   "name": "Numerical probes / A45 ancilla",
   "conclusion": "success"
  },
  {
   "name": "Numerical probes / BG-2 premise orientation",
   "conclusion": "success"
  },
  {
   "name": "Numerical probes / KINF-2 foundations",
   "conclusion": "success"
  },
  {
   "name": "Numerical probes / KT4-PREM-1 premise audit",
   "conclusion": "success"
  },
  {
   "name": "Numerical probes / NB-1 native-gate ball",
   "conclusion": "success"
  },
  {
   "name": "Numerical probes / OI channel protocol",
   "conclusion": "success"
  },
  {
   "name": "Numerical probes / OI finite protocol",
   "conclusion": "success"
  },
  {
   "name": "Numerical probes / OI pair maxCone",
   "conclusion": "success"
  },
  {
   "name": "Numerical probes / core A",
   "conclusion": "success"
  },
  {
   "name": "Numerical probes / core B",
   "conclusion": "success"
  },
  {
   "name": "Numerical probes / foundations",
   "conclusion": "success"
  }
 ],
 "expected": {
  "build_success": true,
  "build_errors": [],
  "gate": {
   "steps": [
    {
     "name": "toolchain",
     "status": "PASS",
     "summary": "toolchain_check: OK (build entry present, unicode-fix.tex co"
    },
    {
     "name": "staleness",
     "status": "PASS",
     "summary": "staleness_check: OK (13 matched, 0 unstamped)"
    },
    {
     "name": "baseline-label",
     "status": "PASS",
     "summary": "baseline_label_check: OK (no baseline archives named)"
    },
    {
     "name": "voice",
     "status": "PASS",
     "summary": "voice_check: OK (no manuscript-voice history narration; 40 m"
    },
    {
     "name": "voice-scope",
     "status": "PASS",
     "summary": "voice_scope_test: OK (6 scope case(s); the checker scans the"
    },
    {
     "name": "ci-gate-presence",
     "status": "PASS",
     "summary": "ci_gate_presence_test: OK (CI runs the real release gate)"
    },
    {
     "name": "artifact-placement",
     "status": "PASS",
     "summary": "artifact_placement_check: OK (no unaccounted root artifact;"
    },
    {
     "name": "manifest-drift",
     "status": "PASS",
     "summary": "build_migration_manifest --check: OK (91 artifacts; both gen"
    },
    {
     "name": "claims",
     "status": "PASS",
     "summary": "claims_check: OK (no withdrawn result asserted unconditional"
    },
    {
     "name": "duplicate",
     "status": "PASS",
     "summary": "duplicate_check: OK (no paragraph repeated within a file)"
    },
    {
     "name": "mirror",
     "status": "PASS",
     "summary": "mirror_check: 0 chapter line(s) absent from FULL.md"
    },
    {
     "name": "citation",
     "status": "PASS",
     "summary": "citation_check: 112 citation(s), 0 broken, 0 duplicate bib n"
    },
    {
     "name": "architecture",
     "status": "PASS",
     "summary": "architecture_check: 259 invariant(s), 0 violation(s), 0 self"
    },
    {
     "name": "dependency-label",
     "status": "PASS",
     "summary": "dependency_label_check: OK (no stale dependency label, 41 fi"
    },
    {
     "name": "coverage",
     "status": "PASS",
     "summary": "coverage_check: OK (128 canonical statements, 19 unattached"
    },
    {
     "name": "lean-axioms",
     "status": "PASS",
     "summary": "lean_axiom_check: OK (5989 named result(s) reported, no sorr"
    },
    {
     "name": "lean-manuscript",
     "status": "PASS",
     "summary": "lean_manuscript_census: OK (every cited identifier and path"
    },
    {
     "name": "legacy-records",
     "status": "PASS",
     "summary": "LEGACY  303 record(s) in 75 closed namespace(s), all intact"
    },
    {
     "name": "v3-self-test",
     "status": "PASS",
     "summary": "v3_verifier: self-test OK"
    },
    {
     "name": "v3-corpus",
     "status": "PASS",
     "summary": "CORPUS  140 vector(s), exact and as expected"
    },
    {
     "name": "v3-receipts",
     "status": "PASS",
     "summary": "RECEIPTS  48 receipt(s), all hold"
    },
    {
     "name": "evidence-retention",
     "status": "PASS",
     "summary": "EVIDENCE-RETENTION  HOLDS (history mode: 0 failure(s); self-"
    }
   ],
   "steps_pass": 22,
   "steps_total": 22,
   "verdict": "PASS  (note: --label bNNN not given, so the baseline check ran in relative mode only)"
  },
  "markers": {
   "Lean.ofReduceBool": 0,
   "declaration uses 'sorry'": 0,
   "error:": 0,
   "sorryAx": 0
  },
  "modules": {
   "OIBridge/TransSeparation.lean": {
    "status": "absent",
    "prints": 0,
    "reports": [],
    "print_lines": [],
    "note": "F's tree has no OIBridge/TransSeparation.lean (the module is added at S1); the served text holds no line naming it"
   }
  },
  "permitted_axioms": [
   "propext",
   "Classical.choice",
   "Quot.sound"
  ]
 },
 "observed": {
  "build_line": "Build completed successfully (3652 jobs).",
  "transseparation_window": {
   "served_lines": 5000,
   "built_line": null,
   "report_lines": {},
   "gate_start": null,
   "gate_end": null,
   "note": "no TransSeparation build line or report exists in this run"
  }
 },
 "source": {
  "extractor": "verification/audits/evidence-retention/extract_result.py",
  "extractor_blob": "05c41bce610b8d02ccbaca8e69377b771bef4a35",
  "form_note": "derived: read from the served job log (served_sha256) and the runs and jobs APIs (their answers' digests)",
  "kind": "GitHub Actions job log, read on 2026-10-23 through the session's job-log tool, which returns at most the last 5000 lines",
  "markers_scope": "the failure markers are counted over the served text only",
  "original_lines": 38742,
  "served_lines": 5000,
  "served_sha256": "ea778de6e61fbb224d822ddcd096465ae7f564dab362a2dd30745da89ae3f630",
  "jobs_api_sha256": "d780edef46d7e01d125254f6b9811de56bf37c144a7013b1c7a90d37e1e952dd",
  "runs_api_sha256": "c8edd649a918bdbd4e67efa7d604053c78a19b9d807d5296a6b5a70c83203308",
  "runs_api_note": "digest of the selected fields of the runs API answer, serialized with sorted keys",
  "missing": "lines 1-33742 of 38742 were not served; the build-success line, the release-gate block and the axiom reports lie in the served window",
  "note": "the digest identifies the text this result was read from: it is provenance of the extraction, not independent proof of the result, which reproduction at the commit supplies; the text is not retained"
 }
}
'''

SHARD = '''  probes_ktranssep2:
    name: Numerical probes / KTRANS-SEP-2 Omega4 counterexample
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

      - name: KTRANS-SEP-2 exact probe
        working-directory: verification/lean
        run: |
          echo "=== ktrans_sep1_probe.py ==="
          python3 -I -B ktrans_sep1_probe.py | tee "$RUNNER_TEMP/ktrans_sep1_probe.out"
          grep -qx 'VERDICT DRIVE-SEED-GEOM-SEC-CAP2-NOT-TRANS' "$RUNNER_TEMP/ktrans_sep1_probe.out"

      - name: KTRANS-SEP-2 independent exact layer and countercontrols
        run: python3 -I -B verification/programmes/oi-qm/reconstruction/round-ktrans-sep-2-omega4/controls.py exact

      - name: KTRANS-SEP-2 control mutation tests
        run: python3 -I -B verification/programmes/oi-qm/reconstruction/round-ktrans-sep-2-omega4/controls.py --self-test

'''
A3_RUN = ('        run: lake env python3 -I -B ../programmes/oi-qm/reconstruction/round-ktoken-maxcone-1/checks/'
          'run_checks.py run\n')
FINAL_STEP = '''
      # KTRANS-SEP-2: the module's fifteen axiom reports again, as the bridge job's last output, so that they lie in
      # any served tail of its log whatever the build cache replayed. The step fails unless each of the fifteen is
      # reported exactly once, in print order, within propext, Classical.choice and Quot.sound, with no other report,
      # no error line and none of the forbidden tokens (controls.py axioms).
      - name: KTRANS-SEP-2 axiom reports
        if: ${{ !cancelled() }}
        working-directory: verification/lean-mathlib
        run: |
          set -euo pipefail
          echo "ktrans_sep2 axioms: step at $(git rev-parse HEAD)"
          log="$RUNNER_TEMP/ktrans-sep2-axioms.log"
          rc=0
          lake env lean OIBridge/TransSeparation.lean > "$log" 2>&1 || rc=$?
          cat "$log"
          echo "ktrans_sep2 axioms: lean exited ${rc}"
          python3 -I -B ../programmes/oi-qm/reconstruction/round-ktrans-sep-2-omega4/controls.py axioms "$log"
          exit "$rc"
'''
# KTOKEN-MAXCONE-1's self-test, which runs in its shard on every build, reads the live workflow, root and census and
# requires each of its own splices verbatim and its census family last. The edits above keep each of these intact.
KTOKEN_LIVE_WORKFLOW = [
    '      - name: Release gate\n        run: python3 tools/release_gate.py\n\n      - name: KTOKEN-MAXCONE-1 check A3',
    'reconstruction/round-bg-2-premise-orientation/controls.py --self-test\n\n  probes_ktokenmaxcone1:\n',
    'probes_bg2, probes_ktokenmaxcone1, probes_a42_witness',
    '          BG2_RESULT: ${{ needs.probes_bg2.result }}\n          KTOKENMAXCONE1_RESULT: ${{ needs.probes_ktokenmaxcone1.result }}\n',
    '          echo "bg2=${BG2_RESULT}"\n          echo "ktokenmaxcone1=${KTOKENMAXCONE1_RESULT}"\n',
    '          test "${BG2_RESULT}" = success\n          test "${KTOKENMAXCONE1_RESULT}" = success\n',
]
KTOKEN_LIVE_ROOT = 'import OIBridge.TurnpikePremiseOrientation\nimport OIBridge.KTokenMaxCone\n'


def ktoken_live_ok(wf, root, census):
    """KTOKEN-MAXCONE-1's live self-test still holds on these files: each of its workflow splices once, its root line
    after its anchor, its census family last."""
    try:
        return (all(wf.count(x) == 1 for x in KTOKEN_LIVE_WORKFLOW) and root.count(KTOKEN_LIVE_ROOT) == 1
                and json.loads(census)['families'][-1]['modules'] == PREV_FAMILY_MODULES)
    except (AttributeError, ValueError, KeyError, IndexError, TypeError):
        return False


SPLICES = [
    (A3_RUN, A3_RUN + FINAL_STEP),
    ('  # Act 42. Two shards run on every event', SHARD + '  # Act 42. Two shards run on every event'),
    ('probes_a42_witness, probes_a42_census01', 'probes_a42_witness, probes_ktranssep2, probes_a42_census01'),
    ('          KTOKENMAXCONE1_RESULT: ${{ needs.probes_ktokenmaxcone1.result }}\n',
     '          KTOKENMAXCONE1_RESULT: ${{ needs.probes_ktokenmaxcone1.result }}\n'
     '          KTRANSSEP2_RESULT: ${{ needs.probes_ktranssep2.result }}\n'),
    ('          echo "ktokenmaxcone1=${KTOKENMAXCONE1_RESULT}"\n',
     '          echo "ktokenmaxcone1=${KTOKENMAXCONE1_RESULT}"\n          echo "ktranssep2=${KTRANSSEP2_RESULT}"\n'),
    ('          test "${KTOKENMAXCONE1_RESULT}" = success\n',
     '          test "${KTOKENMAXCONE1_RESULT}" = success\n          test "${KTRANSSEP2_RESULT}" = success\n'),
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


def full_sha(commit):
    """The full object id of commit, or None."""
    r = git('rev-parse', '--verify', '--quiet', '%s^{commit}' % commit)
    return r.stdout.strip() if r.returncode == 0 else None


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
# The module's build-status line. The bridge job restores a build cache keyed on the toolchain, the dependency
# manifest, the lakefile and every OIBridge source, and runs `lake --rehash build`, which re-hashes each source
# against the restored trace: a module whose inputs are byte-identical to a cached build is replayed, its stored
# messages (the #print axioms reports among them) printed under `Replayed`, and any other module is built.
BUILT = re.compile(r'(?:Built|Replayed) OIBridge\.TransSeparation\b')
GATE_STEP = re.compile(r'^  (PASS|FAIL|SKIP)  (\S+)')


def log_facts(text, mod):
    """What the served text shows about the module, with the served line of each item (1-based)."""
    lines = [TS.sub('', l, count=1) for l in (text or '').split('\n')] if text else []
    f = {'served_lines': len(lines), 'reports': {}, 'unparsed': [], 'built': None, 'built_word': None, 'build': False,
         'build_line': None, 'cache_hit': False,
         'gate_start': None, 'gate_end': None, 'gate_pass': False, 'gate_fail': [], 'mod_errors': 0}
    for n, l in enumerate(lines, 1):
        m = REPORT.match(l)
        if m:
            ax = {a.strip() for a in (m.group(3) or '').split(',') if a.strip()}
            f['reports'].setdefault(m.group(2), []).append((int(m.group(1)), ax, n))
        elif REPORT_HEAD.match(l):
            f['unparsed'].append(n)
        if f['built'] is None and BUILT.search(l):
            f['built'], f['built_word'] = n, BUILT.search(l).group(0).split()[0]
        if re.match(r'^Build completed successfully \(\d+ jobs\)\.', l):
            f['build'], f['build_line'] = True, f['build_line'] or n
        if l.startswith('Cache hit occurred on the primary key '):
            f['cache_hit'] = True
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


# The final bridge step (the sixth workflow splice): after every other step of the Mathlib bridge job it prints one
# line 'ktrans_sep2 axioms: step at <commit>', elaborates the module alone (`lake env lean`), which prints its fifteen
# reports again (without file positions, and wrapped by Lean when long), prints one line 'ktrans_sep2 axioms: lean
# exited <status>', and runs `controls.py axioms` on that output, which ends the block with exactly one OK or FAILED
# line. Being the job's last output, the block lies in any served
# tail of the log, whatever the build cache replayed earlier in it.
STEP_MARK = re.compile(r'^ktrans_sep2 axioms: step at (\S*)$', re.M)
STEP_OK = 'ktrans_sep2 axioms: OK -- %d reports' % len(PRINTS)
STEP_FAILED = re.compile(r'^ktrans_sep2 axioms: FAILED\b', re.M)
STEP_EXIT = re.compile(r'^ktrans_sep2 axioms: lean exited (\d+)$', re.M)
STEP_END = re.compile(r'^(?:##\[group\]Run |Post job cleanup\.)', re.M)
BLOCK_REPORT = re.compile(r"^'" + re.escape(NS) + r"([A-Za-z0-9_']+)' (?:depends on axioms: \[([^\]]*)\]|does not "
                          r"depend on any axioms)", re.M)
BLOCK_HEAD = re.compile(r"^'" + re.escape(NS), re.M)
BAD_TOKENS = ('sorryAx', 'Lean.ofReduceBool', 'Lean.trustCompiler')
STEP_ERROR = re.compile(r'^\S+\.lean:\d+:\d+: error\b', re.M)
STEP_MOD_ERROR = re.compile(r'^OIBridge/TransSeparation\.lean:\d+:\d+: error\b', re.M)


def plain(text):
    """The text with each line's leading timestamp removed, so that a report Lean wraps across lines reads whole."""
    return '\n'.join(TS.sub('', l, count=1) for l in (text or '').split('\n'))


def parse_reports(text):
    """[(name, axioms, offset)] of every report of the module's namespace in text, and the number of report
    starts that do not parse."""
    reps = [(m.group(1), frozenset(a.strip() for a in (m.group(2) or '').split(',') if a.strip()), m.start())
            for m in BLOCK_REPORT.finditer(text)]
    return reps, len(BLOCK_HEAD.findall(text)) - len(reps)


def step_facts(text):
    """What the final bridge step shows, with served line numbers (1-based). Its block runs from the step's one
    marker line to the next step header or the job's cleanup."""
    t = plain(text)
    ln = lambda off: t.count('\n', 0, off) + 1
    marks = list(STEP_MARK.finditer(t))
    s = {'marks': len(marks), 'commit': None, 'marker_line': None, 'reports': {}, 'order': [], 'report_lines': {},
         'unparsed': 0, 'ok_lines': [], 'failed_lines': [], 'exit_lines': [], 'exit': None, 'errors': 0,
         'mod_errors': 0, 'bad': []}
    if len(marks) != 1:
        return s
    m0 = marks[0]
    s['commit'], s['marker_line'] = m0.group(1), ln(m0.start())
    rest = t[m0.end():]
    end = STEP_END.search(rest)
    block, base = (rest[:end.start()] if end else rest), m0.end()
    reps, s['unparsed'] = parse_reports(block)
    for n, ax, off in reps:
        s['reports'].setdefault(n, []).append(ax)
        s['order'].append(n)
        s['report_lines'].setdefault(n, ln(base + off))
    s['ok_lines'] = [ln(base + m.start()) for m in re.finditer(r'^%s$' % re.escape(STEP_OK), block, re.M)]
    s['failed_lines'] = [ln(base + m.start()) for m in STEP_FAILED.finditer(block)]
    exits = list(STEP_EXIT.finditer(block))
    s['exit_lines'] = [ln(base + m.start()) for m in exits]
    s['exit'] = int(exits[0].group(1)) if len(exits) == 1 else None
    s['errors'] = len(STEP_ERROR.findall(block))
    s['mod_errors'] = len(STEP_MOD_ERROR.findall(block))
    s['bad'] = [b for b in BAD_TOKENS if b in block]
    return s


def block_problem(s, sha):
    """None when the final step's block is complete evidence for the commit sha, else the reason it is not."""
    if s['marks'] != 1:
        return '%d final-step marker line(s) in the served text, not one' % s['marks']
    if not re.fullmatch(r'[0-9a-f]{40}', sha or '') or s['commit'] != sha:
        return 'the final step ran at %s, not at the commit under check' % ((s['commit'] or '?')[:12])
    if s['unparsed']:
        return 'a report in the final step does not parse'
    if sorted(s['reports']) != sorted(PRINTS) or any(len(v) != 1 for v in s['reports'].values()):
        return 'the final step does not report each of the fifteen prints exactly once'
    if s['order'] != list(PRINTS):
        return 'the final step\'s reports are not in the module\'s print order'
    ends = s['ok_lines'] + s['failed_lines']
    if len(ends) != 1 or ends[0] < max(s['report_lines'].values()):
        return 'the final step\'s gate line is missing, repeated, or not after its last report'
    if len(s['exit_lines']) != 1 or not max(s['report_lines'].values()) < s['exit_lines'][0] < ends[0]:
        return 'the final step\'s lean exit line is missing, repeated, or not between its last report and its gate line'
    return None


def meta_problem(f, meta):
    if not f['served_lines']:
        return 'the log is empty or absent'
    if meta is not None:
        try:
            o, m = int(meta['original_lines']), int(meta['served_lines'])
        except (KeyError, TypeError, ValueError):
            return 'the log metadata names no original and served line counts'
        if m != f['served_lines'] or not 1 <= m <= o:
            return 'the log metadata (%s of %s lines) does not describe this text (%d lines)' % (m, o, f['served_lines'])
    return None


def kernel_state(f, s, meta, sha):
    """('void', reason), or (nonell_ok, cex_ok) from complete evidence: the final step's block for sha, and the
    build and release-gate lines before it."""
    p = meta_problem(f, meta) or block_problem(s, sha)
    if p:
        return ('void', p)
    bad = {n for n in PRINTS if not s['reports'][n][0] <= ALLOWED_AXIOMS}
    gate_done = f['gate_start'] is not None and f['gate_end'] is not None
    if (s['ok_lines'] and s['exit'] == 0 and not bad and not s['bad'] and not s['errors'] and f['build'] and gate_done
            and f['gate_pass'] and f['build_line'] < f['gate_start'] and f['gate_end'] < s['marker_line']):
        return (True, True)
    if s['failed_lines'] and bad and (s['mod_errors'] or (gate_done and f['gate_fail'] == ['lean-axioms'])):
        return (False, False)
    return ('void', 'the final step, build and gate evidence is inconsistent or fails for a reason outside the module '
                    '(step %s, lean exit %s, build %s, gate %s, failing steps %s, module errors in the step %d)'
            % ('OK' if s['ok_lines'] else 'FAILED', s['exit'], f['build'], 'complete' if gate_done else 'incomplete',
               f['gate_fail'] or 'none', s['mod_errors']))


def cells(mod, good_key, log, exact_ok, probe_run, meta=None, sha=None):
    """The three tokens, or ('void', reason): a tooling failure or incomplete evidence never yields a token."""
    if not exact_ok:
        return ('void', 'an exact control failed')
    ks = kernel_state(log_facts(log, mod), step_facts(log), meta, sha)
    if ks[0] == 'void':
        return ks
    ps = probe_state(probe_run)
    if isinstance(ps, tuple):
        return ps
    nonell = ks[0] and set(NONELL_KEY) <= good_key
    cex = ks[1] and set(KEY) <= good_key
    return [TOK_NONELL[0 if nonell else 1], TOK_CEX[0 if cex else 1], TOK_EXACT[0 if ps == 'exact' else 1]]


def window_facts(f, s=None):
    pos = {n: f['reports'][n][0][2] for n in PRINTS if len(f['reports'].get(n, [])) == 1}
    out = {'served_lines': f['served_lines'], 'built_line': f['built'], 'report_lines': pos,
           'gate_start': f['gate_start'], 'gate_end': f['gate_end']}
    if s is not None:
        out['axioms_step'] = {'marker_line': s['marker_line'], 'commit': s['commit'], 'report_lines': s['report_lines'],
                              'ok_lines': s['ok_lines'], 'failed_lines': s['failed_lines'],
                              'exit_lines': s['exit_lines'], 'exit': s['exit']}
    return out


def axioms_gate(text):
    """The final bridge step's fail-closed gate over the module's own `lake env lean` output: [(label, ok, detail)].
    Each of the fifteen prints is reported exactly once, in print order, within the three axioms; no other report
    of the namespace; no report that does not parse; no error line; none of the forbidden tokens. Labels name no
    forbidden token, since this output lands in the job log the verdict reads."""
    t = plain(text)
    if not t.strip():
        return [('the output is not empty', False, '')]
    reps, unparsed = parse_reports(t)
    seen = {}
    for n, ax, _ in reps:
        seen.setdefault(n, []).append(ax)
    out = []
    for n in PRINTS:
        r = seen.get(n, [])
        extra = sorted(set().union(*r) - ALLOWED_AXIOMS) if r else []
        out.append((n, len(r) == 1 and not extra, '%d report(s)%s' % (len(r), (', %d other axiom(s)' % len(extra))
                                                                       if extra else '')))
    out.append(('no other report', not (set(seen) - set(PRINTS)), ''))
    out.append(('the reports in print order', [n for n, _, _ in reps] == list(PRINTS), ''))
    out.append(('every report parses', not unparsed, ''))
    out.append(('no error line', not STEP_ERROR.search(t), ''))
    out.append(('no forbidden log token', not any(b in t for b in BAD_TOKENS), ''))
    return out


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
REPLAY_EVIDENCE = 'evidence/predicted-tree-replay-run.json'
GATE_PASS = re.compile(r'PASS(?:\s.*)?', re.S)


def gate_passed(v):
    """The release gate's verdict text is PASS, alone or followed by whitespace and a note; never a longer word."""
    return isinstance(v, str) and GATE_PASS.fullmatch(v) is not None


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


def other_run(a, b):
    """Two run results name the same head and branch and different runs."""
    try:
        x, y = json.loads(a)['run'], json.loads(b)['run']
        return x['head_sha'] == y['head_sha'] and x['head_branch'] == y['head_branch'] and x['id'] != y['id']
    except (ValueError, KeyError, TypeError):
        return False


def run_window_ok(data, head, replayed=False):
    """A run's retained result names head, is a green workflow_dispatch run, and records the final bridge step's
    block for head inside the served window, after the release gate: its marker, the fifteen reports in print order
    within the three axioms, one lean exit line with status 0 after the last report and one OK line after it, with
    no FAILED line. With replayed, the module's
    status line in the window is not `Built` (the run restored the build cache of an earlier run of the same tree)."""
    try:
        d = json.loads(data)
        r, s, w, b = d['run'], d['source'], d['observed']['transseparation_window'], d['observed']['axioms_step']
        o, m = s['original_lines'], s['served_lines']
        mods = d['expected']['modules']['OIBridge/TransSeparation.lean']
        rl = b['report_lines']
        ints = [o, m, w['served_lines'], w['gate_start'], w['gate_end'], b['marker_line']] + list(rl.values()) + \
            list(b['ok_lines']) + list(b['exit_lines'])
        if not all(type(x) is int for x in ints):
            return False
        return bool(evidence_ok(data) and r['head_sha'] == head and r['event'] == 'workflow_dispatch'
                and r['conclusion'] == 'success' and d['jobs']
                and all(j['conclusion'] == 'success' for j in d['jobs']) and 1 <= m <= o and w['served_lines'] == m
                and b['commit'] == head and sorted(rl) == sorted(PRINTS) and len(b['ok_lines']) == 1
                and b['failed_lines'] == []
                and w['gate_start'] < w['gate_end'] < b['marker_line'] < min(rl.values())
                and b['exit'] == 0 and len(b['exit_lines']) == 1
                and max(rl.values()) < b['exit_lines'][0] < b['ok_lines'][0] <= m
                and d['expected']['build_success'] is True and gate_passed(d['expected']['gate']['verdict'])
                and mods['status'] == 'complete'
                and [x['name'] for x in mods['reports']] == [NS + n for n in PRINTS]
                and all(set(x['axioms']) <= ALLOWED_AXIOMS for x in mods['reports'])
                and (not replayed or (w['status_word'] != 'Built' and w['cache_hit'] is True)))
    except (ValueError, KeyError, TypeError, AttributeError):
        return False


IMPORT_RE = re.compile(r'^[ \t]*import\b[^\n]*?(?<![A-Za-z0-9_.])OIBridge\.TransSeparation(?![A-Za-z0-9_.])', re.M)


def ftree_at(commit):
    """Read through git at commit: which of the module's and the probe's paths exist, OIBridge.lean's text, and the
    tree ids of the two Lean directories. (None, None, None) when the commit cannot be read."""
    r = git('ls-tree', '-r', '--name-only', commit, '--', MOD, PROBE)
    if r.returncode:
        return None, None, None
    trees = []
    for d in LEAN_DIRS:
        t = git('rev-parse', '--verify', '--quiet', '%s:%s' % (commit, d))
        trees.append(t.stdout.strip() if t.returncode == 0 else None)
    return {p for p in r.stdout.split('\n') if p}, show(commit, IMPORTS), tuple(trees)


def ftree_ok(paths, imports, trees, d_trees):
    """That F carries no module, from F's actual tree: F's two Lean directories are exactly D's (so F's Lean content
    is D's, which carries no module), neither the module's nor the probe's path exists at F, and F's OIBridge.lean
    (which must be readable) has no import line naming OIBridge.TransSeparation, alone or beside other modules. A
    run's log never establishes absence; it is checked for consistency only (frun_log_consistent)."""
    return paths is not None and imports is not None and trees is not None and d_trees is not None \
        and None not in trees and tuple(trees) == tuple(d_trees) and MOD not in paths and PROBE not in paths \
        and not IMPORT_RE.search(imports)


def frun_ok(data, head, ref, shard=SHARD_JOB):
    """F's retained run result, read for what a run can establish: its identity (head_sha is F; the workflow is
    verify.yml; a workflow_dispatch run with a positive integer run id and attempt and conclusion success; the job is
    the Mathlib bridge, with a positive integer job id), its success (every job and the bridge job success, build
    success) and its release-gate result (verdict PASS, every gate step PASS, steps_pass = steps_total). ref is the
    predicted tree's retained run, a workflow_dispatch run of D's workflow plus the round's shard: F's run must have
    exactly its jobs less that one shard job, each once, and exactly its gate steps, in order. It says nothing about
    whether the module is absent; ftree_ok establishes that from F's tree."""
    try:
        d, p = json.loads(data), json.loads(ref)
        r, g = d['run'], d['expected']['gate']
        steps = g['steps']
        names = [j['name'] for j in d['jobs']]
        want = sorted(j['name'] for j in p['jobs'] if j['name'] != shard)
        return bool(evidence_ok(data) and r['head_sha'] == head and r['workflow'] == 'verify.yml'
                    and r['event'] == 'workflow_dispatch' and type(r['id']) is int and r['id'] >= 1
                    and type(r['attempt']) is int and r['attempt'] >= 1 and r['conclusion'] == 'success'
                    and r['job_name'] == 'Mathlib bridge' and type(r['job_id']) is int and r['job_id'] >= 1
                    and r['job_conclusion'] == 'success' and d['jobs']
                    and all(j['conclusion'] == 'success' for j in d['jobs'])
                    and len(want) == len(p['jobs']) - 1 and len(set(names)) == len(names) and sorted(names) == want
                    and d['expected']['build_success'] is True and gate_passed(g['verdict'])
                    and steps and all(s['status'] == 'PASS' for s in steps)
                    and [s['name'] for s in steps] == [s['name'] for s in p['expected']['gate']['steps']]
                    and g['steps_pass'] == g['steps_total'] == len(steps))
    except (ValueError, KeyError, TypeError, AttributeError):
        return False


def frun_log_consistent(data):
    """Consistency only, not the proof of absence: F's run evidence records no module build line, no report and the
    module's status absent, and no final-step marker, as a run of a tree without the module must. Where the release
    gate falls in the log is not module evidence and is not read."""
    try:
        d = json.loads(data)
        w = d['observed']['transseparation_window']
        m = d['expected']['modules'][MOD[len('verification/lean-mathlib/'):]]
        b = d['observed'].get('axioms_step', {})
        return bool(m['status'] == 'absent' and m['reports'] == [] and w['built_line'] is None
                    and w['report_lines'] == {} and b.get('marker_line') is None and not b.get('report_lines'))
    except (ValueError, KeyError, TypeError, AttributeError):
        return False


def fstage_ok(data, head, f, ref, shard=SHARD_JOB):
    """The F-stage requirement: absence from F's tree, and identity, success and gate from F's run evidence against
    the predicted tree's run, with the log consistent. Returns (tree, run, consistent)."""
    return (ftree_ok(*ftree_at(f), ftree_at(D)[2]), frun_ok(data, head, ref, shard), frun_log_consistent(data))


def predicted_head(prereg):
    """The predicted tree's commit: the section's first line must be `- **`<40 hex>`**`, directly after its heading."""
    m = re.search(r'^### The predicted execution tree\n\n- \*\*`([0-9a-f]{40})`\*\*', prereg or '', re.M)
    return m.group(1) if m else None


CONTROLS_PIN = re.compile(r'^\*\*The frozen `controls\.py`:\*\* blob (?:`([0-9a-f]{40})`|pending)\.$', re.M)


def controls_pin(prereg):
    """('pinned', blob), ('pending', None) or ('absent', None): the preregistration's one pin of this file's blob."""
    ms = CONTROLS_PIN.findall(prereg or '')
    if len(ms) != 1:
        return ('absent', None)
    return ('pinned', ms[0]) if ms[0] else ('pending', None)


def gate_steps(lines, start, end):
    return [{'name': m.group(2), 'status': m.group(1)} for m in
            (GATE_STEP.match(l) for l in lines[start:end - 1]) if m] if start and end else []


def read_log(path):
    """LOG as every reader reads it: bytes, decoded as UTF-8 with a leading byte-order mark dropped and no newline
    translation; '' when the file is absent."""
    return open(path, 'rb').read().decode('utf-8-sig', errors='replace') if path and os.path.isfile(path) else ''


def derive_run(log, meta, run_api, jobs_api):
    """The frozen recipe for a run result: a function of the served bridge-job text (bytes, exactly as served), its
    metadata {"original_lines", "served_lines"} and the runs and jobs API answers (bytes). Raises ValueError when the
    inputs do not describe one complete run with one Mathlib bridge job."""
    text = log.decode('utf-8-sig')
    run = json.loads(run_api)
    jobs = json.loads(jobs_api)
    if isinstance(jobs.get('jobs'), dict):
        jobs = jobs['jobs']
    js = jobs['jobs']
    if jobs.get('total_count') != len(js) or len({j['name'] for j in js}) != len(js):
        raise ValueError('the jobs answer is not one complete list of distinct jobs')
    bridge = [j for j in js if j['name'] == 'Mathlib bridge']
    if len(bridge) != 1:
        raise ValueError('the jobs answer has no single Mathlib bridge job')
    b = bridge[0]
    f = log_facts(text, '')
    o, m = int(meta['original_lines']), int(meta['served_lines'])
    if m != f['served_lines'] or not 1 <= m <= o:
        raise ValueError('the metadata (%s of %s lines) does not describe the text (%d lines)' % (m, o, f['served_lines']))
    lines = [TS.sub('', l, count=1) for l in text.split('\n')]
    steps = gate_steps(lines, f['gate_start'], f['gate_end'])
    verdict = lines[f['gate_end'] - 1][len('release gate: '):] if f['gate_end'] else None
    first = {n: v[0][2] for n, v in f['reports'].items()}
    st = step_facts(text)
    if (not f['reports'] and not f['unparsed'] and f['built'] is None and not f['mod_errors'] and not st['marks']
            and not parse_reports(plain(text))[0]):
        status = 'absent'
    elif block_problem(st, run['head_sha']) is None and st['ok_lines'] and st['exit'] == 0:
        status = 'complete'
    else:
        status = 'incomplete'
    sha = lambda b_: hashlib.sha256(b_).hexdigest()
    res = {
        'schema': 'oi-evidence-result', 'version': 1, 'form': 'derived', 'kind': 'exact-head-run',
        'recipe': 'controls.py derive-run --log LOG --log-meta META --run-api RUN --jobs-api JOBS (round '
                  'KTRANS-SEP-2, at the controls.py blob its preregistration pins)',
        'run': {'workflow': os.path.basename(run['path']), 'id': int(run['id']), 'attempt': int(run['run_attempt']),
                'event': run['event'], 'conclusion': run['conclusion'], 'head_branch': run.get('head_branch'),
                'head_sha': run['head_sha'], 'job_id': int(b['id']), 'job_name': b['name'],
                'job_conclusion': b['conclusion'],
                'job_steps': [{'name': s['name'], 'conclusion': s['conclusion']} for s in b.get('steps') or []]},
        'jobs': sorted(({'name': j['name'], 'conclusion': j['conclusion']} for j in js), key=lambda j: j['name']),
        'expected': {
            'build_success': f['build'],
            'gate': {'verdict': verdict, 'steps': steps, 'steps_pass': sum(s['status'] == 'PASS' for s in steps),
                     'steps_total': len(steps)},
            'modules': {MOD[len('verification/lean-mathlib/'):]: {
                'status': status,
                'reports': [{'name': NS + n, 'axioms': sorted(st['reports'][n][0])} for n in st['order']]}}},
        'observed': {
            'transseparation_window': {
                'served_lines': m, 'built_line': f['built'], 'status_word': f['built_word'], 'report_lines': first,
                'cache_hit': f['cache_hit'],
                'gate_start': f['gate_start'], 'gate_end': f['gate_end']},
            'axioms_step': {'marker_line': st['marker_line'], 'commit': st['commit'], 'report_lines': st['report_lines'],
                            'ok_lines': st['ok_lines'], 'failed_lines': st['failed_lines'],
                            'exit_lines': st['exit_lines'], 'exit': st['exit']}},
        'source': {'served_sha256': sha(log), 'original_lines': o, 'served_lines': m, 'runs_api_sha256': sha(run_api),
                   'jobs_api_sha256': sha(jobs_api),
                   'note': 'the digests identify the inputs this result was derived from; the inputs are not retained'}}
    return json.dumps(res, indent=1, sort_keys=True, ensure_ascii=False) + '\n'


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
    check('P', 'the pinned evidence is present with its digests; the five required files are pinned%s'
          % ('; no pin is pending' if freeze else ''), pins_ok(table, files, bool(freeze)))
    bad_ev = sorted(p for p, b in files.items() if not evidence_ok(b.decode('utf-8', 'replace')))
    check('P', 'every pinned evidence file is a structured expected result with its form stated and no run-varying '
               'field%s' % (' (fails: %s)' % ', '.join(bad_ev) if bad_ev else ''), not bad_ev)
    ref = files[RUN_EVIDENCE].decode('utf-8', 'replace') if RUN_EVIDENCE in files else None
    if freeze:
        check('P', 'the predicted-tree section names its commit in the frozen form (its first line `- **`<sha>`**`)',
              predicted_head(prereg) is not None)
    if ref is not None:
        check('P', 'the predicted tree\'s retained run names the predicted tree, is green, and places the release gate '
                   'and then the final step\'s block for it inside its served window', run_window_ok(ref, predicted_head(prereg)))
    if REPLAY_EVIDENCE in files:
        rep_ = files[REPLAY_EVIDENCE].decode('utf-8', 'replace')
        check('P', 'the predicted tree\'s second run, on the same branch, restored the build cache (the module is not '
                   '`Built` in its window) and still places the final step\'s block for it inside its served window; it '
                   'is another run than the first', run_window_ok(rep_, predicted_head(prereg), replayed=True)
              and ref is not None and other_run(rep_, ref))
    if freeze:
        rv = git('rev-list', '--parents', '%s..%s' % (D, commit))
        revs = [(l.split()[0], l.split()[1:]) for l in rv.stdout.split('\n') if l]
        ddf = git('diff', '--name-only', '--no-renames', D, freeze).stdout.split()
        check('T', 'D..commit is one chain of single-parent commits through F; delta(D, F) is the control plane; the '
                   'preregistration is F\'s', rv.returncode == 0 and chain_ok(revs, D, freeze, commit, ddf, prereg,
                                                                              show(freeze, PREREG)))
        fr = show(commit, FRUN) or ''
        t_ok, r_ok, c_ok = fstage_ok(fr, freeze, freeze, ref)
        check('P', 'F has no module, read through git at F: F\'s Lean directories are D\'s, neither the module\'s nor '
                   'the probe\'s path exists, and OIBridge.lean imports no OIBridge.TransSeparation', t_ok)
        check('P', 'F\'s exact-head run is retained and its evidence names F as a workflow_dispatch run of verify.yml '
                   '(its Mathlib bridge job, run id, job id and attempt), every job success and exactly the predicted '
                   'tree\'s jobs less the round\'s shard, build success, and the release gate PASS on exactly the '
                   'predicted tree\'s steps', r_ok)
        check('P', 'consistency, not the proof of absence: F\'s run evidence records no module build line or report',
              c_ok)
    me = open(os.path.abspath(__file__), encoding='utf-8').read()
    pin = controls_pin(prereg)
    check('B', 'the probe is the frozen blob; controls.py at commit is the file running, and its blob is the one the '
               'preregistration pins%s' % (' (not pending)' if freeze else ''),
          git('rev-parse', '%s:%s' % (commit, PROBE)).stdout.strip() == PROBE_BLOB and show(commit, CONTROLS) == me
          and (pin == ('pinned', blob_id(me)) or (not freeze and pin[0] == 'pending')))
    mod = show(commit, MOD)
    landed = landed_texts(lambda p: show(D, p))
    good = module_checks(mod, landed_d=landed, closure_names=closure_names_at_d())
    ball_check(landed)
    exact_checks(mod)
    d_imp, d_cen, d_wf = show(D, IMPORTS), show(D, CENSUS), show(D, WORKFLOW)
    check('I', 'OIBridge.lean is D\'s with exactly the frozen import line', imports_want(d_imp) == show(commit, IMPORTS))
    check('C', 'the census is D\'s with exactly the frozen family before KTOKEN-MAXCONE-1\'s', census_want(d_cen) == show(commit, CENSUS))
    check('W', 'verify.yml is D\'s with exactly the six frozen splices', workflow_want(d_wf) == show(commit, WORKFLOW))
    note = show(commit, RESULT)
    if note is not None:
        if log is None:
            check('V', 'the result note is read against the exact-head bridge log (--log required)', False)
        else:
            toks = cells(mod, good, log, all(CODES_RUN.get(c) for c in EXACT_CODES), run_probe(show(commit, PROBE) or ''),
                         meta, full_sha(commit))
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
    dd['families'].insert(ks[0], CENSUS_FAMILY)
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
    log = read_log(logpath)
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
    print('LOG  %s' % json.dumps(window_facts(f, step_facts(log)), sort_keys=True))
    toks = cells(mod, good, log, True, run_probe(show(commit, PROBE) or ''), meta, full_sha(commit))
    if isinstance(toks, tuple):
        print('VERDICT  VOID  (%s)' % toks[1])
        FAILS.append('VOID')
        return
    for cell, tok in zip(('Q-NONELL', 'Q-CEX', 'Q-EXACT'), toks):
        print('VERDICT  %-8s  %s' % (cell, tok))


class Scratch:
    """A temporary object directory with the repository's object store as an alternate: blobs, trees and commits
    are written there, nothing is written to the repository and no ref is created. Within `with`, git reads it too."""

    def __init__(self, prefix='ktsep2-scratch-'):
        common = git('rev-parse', '--git-common-dir').stdout.strip()
        self.objects = os.path.join(os.path.abspath(common), 'objects')
        self.tmp = tempfile.mkdtemp(prefix=prefix)
        self.env = dict(os.environ, GIT_OBJECT_DIRECTORY=self.tmp, GIT_ALTERNATE_OBJECT_DIRECTORIES=self.objects)

    def g(self, *a, inp=None, env=None):
        r = subprocess.run(['git', *a], capture_output=True, input=inp, env=env or self.env)
        if r.returncode:
            raise RuntimeError('git %s: %s' % (' '.join(a), r.stderr.decode('utf-8', 'replace')))
        return r.stdout.decode().strip()

    def blob(self, data):
        return self.g('hash-object', '-w', '--stdin', inp=data.encode('utf-8') if isinstance(data, str) else data)

    def commit(self, base, files, msg):
        """A single-parent child of base whose tree is base's with files ({path: blob id}) set."""
        e2 = dict(self.env, GIT_INDEX_FILE=os.path.join(self.tmp, 'index'))
        self.g('read-tree', base, env=e2)
        for p, b in sorted(files.items()):
            self.g('update-index', '--add', '--cacheinfo', '100644,%s,%s' % (b, p), env=e2)
        t = self.g('write-tree', env=e2)
        os.remove(e2['GIT_INDEX_FILE'])
        return self.g('-c', 'user.name=mock', '-c', 'user.email=mock@invalid', 'commit-tree', t, '-p', base, '-m', msg)

    def __enter__(self):
        self.old = {k: os.environ.get(k) for k in ('GIT_OBJECT_DIRECTORY', 'GIT_ALTERNATE_OBJECT_DIRECTORIES')}
        os.environ.update(GIT_OBJECT_DIRECTORY=self.tmp, GIT_ALTERNATE_OBJECT_DIRECTORIES=self.objects)
        return self

    def __exit__(self, *exc):
        for k, v in self.old.items():
            if v is None:
                os.environ.pop(k, None)
            else:
                os.environ[k] = v
        shutil.rmtree(self.tmp, ignore_errors=True)


def mock_s1(candf, frun, predicted, extra, log, meta, run_api, jobs_api, s=None):
    """The pre-freeze safeguard. FILE (frun, bytes) must be derive-run's output over the served bridge log, its
    metadata and the runs and jobs answers of candidate F's actual exact-head run, and predicted must be the tree
    candidate F's preregistration names. Then, in a Scratch object directory (no ref written), build mock C1 =
    candidate F + the predicted tree's record files + each --evidence file (extra: [(rel, bytes)]) + FILE as
    evidence/f-run/results.json, and mock S1 = mock C1 + the predicted tree's execution files, and run
    check(mock S1, freeze=candidate F, stage S1). With s given, its objects are used and it stays open."""
    own = s is None
    if own:
        s = Scratch('ktsep2-mock-').__enter__()
    try:
        try:
            derived = derive_run(log, meta, run_api, jobs_api).encode('utf-8')
        except (ValueError, KeyError, TypeError, AttributeError, UnicodeDecodeError):
            derived = None
        check('P', 'the f-run file (sha256 %s) is derive-run\'s output over the served log, its metadata and the runs '
                   'and jobs answers given' % hashlib.sha256(frun).hexdigest(), derived is not None and derived == frun)
        named = predicted_head(show(candf, PREREG))
        check('P', 'the predicted tree given is the one candidate F\'s preregistration names (%s)' % named,
              named is not None and named == predicted)
        rec = {}
        for p in git('ls-tree', '-r', '--name-only', predicted, '--', RDIR).stdout.split():
            if p != PREREG:
                rec[p] = git('rev-parse', '%s:%s' % (predicted, p)).stdout.strip()
        for rel, data in extra:
            rec[RDIR + rel] = s.blob(data)
        rec[FRUN] = s.blob(frun)
        c1 = s.commit(candf, rec, 'mock C1 (safeguard; no ref)')
        exe = {p: git('rev-parse', '--verify', '--quiet', '%s:%s' % (predicted, p)).stdout.strip() for p in EXEC}
        if not all(exe.values()):
            check('P', 'the predicted tree given carries the five execution paths', False)
            return
        s1 = s.commit(c1, exe, 'mock S1 (safeguard; no ref)')
        print('MOCK  C1 %s  S1 %s  (temporary objects, no ref)' % (c1, s1))
        run_check(s1, candf, 'S1')
    finally:
        if own:
            s.__exit__(None, None, None)


# ---- self-test ---------------------------------------------------------------------------------------------------
LAST_OUT = ['']


def capture(fn):
    """Run fn with fresh failure state; return (codes failed, codes run). Its output is kept in LAST_OUT."""
    saved = (list(FAILS), COUNT[0], dict(CODES_RUN))
    del FAILS[:]
    CODES_RUN.clear()
    import io
    old, sys.stdout = sys.stdout, io.StringIO()
    try:
        fn()
    finally:
        LAST_OUT[0] = sys.stdout.getvalue()
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


def must_fail_at(label, code, fn, at, only=False):
    """fn fails code, and the failing check is the one whose text begins with `at`."""
    failed, _ = capture(fn)
    hit = any(l.startswith('  FAIL  %-4s %s' % (code, at)) for l in LAST_OUT[0].split('\n'))
    check('M', '%s fails %s%s at "%s"' % (label, code, ' alone' if only else '', at),
          code in failed and hit and (not only or failed == {code}))


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
    # the log and the cells: the final bridge step's block, after the build and the release gate
    std = '[propext, Classical.choice, Quot.sound]'
    blk = lambda n, ax=std: "'%s%s' depends on axioms: %s" % (NS, n, ax)
    wrapped = lambda n: "'%s%s' depends on axioms: [propext,\n Classical.choice,\n Quot.sound]" % (NS, n)
    sha_e = 'e' * 40
    head = '2026-10-10T23:54:47.9382674Z '
    gate = 'release gate\n  PASS  lean-axioms  ok\n  PASS  lean-manuscript  ok\nrelease gate: PASS\n'
    pre = 'ℹ [3652/3653] Replayed OIBridge\nBuild completed successfully (3653 jobs).\n' + gate + \
        '##[group]Run lake env python3 -I -B ../programmes/oi-qm/reconstruction/round-ktoken-maxcone-1/checks/run_checks.py run\nA3 ok\n' + \
        '##[group]Run set -euo pipefail\n'

    def mk(reports=None, mark=None, end=STEP_OK, extra='', before=pre, after='Post job cleanup.', rc='0'):
        reports = [blk(n) if n != 'conv_core' else wrapped(n) for n in PRINTS] if reports is None else reports
        body = ['ktrans_sep2 axioms: step at %s' % (mark or sha_e)] + reports + \
            (['ktrans_sep2 axioms: lean exited %s' % rc] if rc is not None else []) + ['PASS axioms: no other report'] + \
            ([end] if end else []) + ([extra] if extra else []) + [after]
        return '\n'.join(head + l for l in (before + '\n'.join(body)).split('\n'))
    log_ok = mk()
    good = set(KEY)
    P_, N_ = [TOK_NONELL[0], TOK_CEX[0], TOK_EXACT[0]], [TOK_NONELL[1], TOK_CEX[1], TOK_EXACT[1]]
    c = lambda lg, ex=True, pr=prun, meta=None, gk=good, sha=sha_e: cells(mod, gk, lg, ex, pr, meta, sha)
    sorry = lambda n: blk(n, '[propext, sorryAx, Classical.choice, Quot.sound]')
    with_sorry = [blk(n) if n != 'omega4_strictConvex' else sorry(n) for n in PRINTS]
    failed = 'ktrans_sep2 axioms: FAILED (1 check(s))'
    check('M', 'a complete log whose final step reports all fifteen within the three axioms, after a passing gate, '
               'gives the three positive tokens, a wrapped report read whole', c(log_ok) == P_)
    check('M', 'the cells do not depend on the build output: a log with the module built and reported there, or '
               'with neither, reads the same from the final step',
          c(log_ok.replace(head + 'ℹ [3652/3653] Replayed OIBridge', head + '✔ [3650/3653] Built OIBridge.TransSeparation'))
          == P_)
    check('M', 'the window facts place the release gate before the final step and its OK line after its last report',
          (lambda w: w['gate_end'] < w['axioms_step']['marker_line'] < min(w['axioms_step']['report_lines'].values())
           and max(w['axioms_step']['report_lines'].values()) < w['axioms_step']['ok_lines'][0])
          (window_facts(log_facts(log_ok, mod), step_facts(log_ok))))
    check('M', 'an empty log is VOID', isvoid(c('')))
    check('M', 'negative control at E: a complete, green, gate-passing log with no final step (the shape of a run '
               'whose workflow lacks the step, or whose tree lacks the module, as F\'s did) is VOID, never a token',
          isvoid(c(log_ok.split(head + 'ktrans_sep2 axioms: step at')[0] + head + 'Post job cleanup.')))
    check('M', 'a final step run at another commit, or two markers, is VOID',
          isvoid(c(mk(mark='f' * 40))) and isvoid(c(log_ok, sha='f' * 40)) and isvoid(c(log_ok, sha=None))
          and isvoid(c(log_ok.replace(head + 'Post job cleanup.', head + 'ktrans_sep2 axioms: step at %s\n' % sha_e
                                      + head + 'Post job cleanup.'))))
    check('M', 'a final step cut before its gate line, or with its OK line before its last report, or with both an '
               'OK and a FAILED line, is VOID',
          isvoid(c(mk(end=None)))
          and isvoid(c(mk(reports=[blk(n) for n in PRINTS[:-1]] + [STEP_OK, blk(PRINTS[-1])], end=None)))
          and isvoid(c(mk(extra=failed))))
    check('M', 'the block ends at the next step header: lines a later step prints after it are not read',
          c(log_ok.replace(head + 'Post job cleanup.', head + '##[group]Run another step\n' + head + blk(PRINTS[0]) + '\n'
                           + head + failed + '\n' + head + 'Post job cleanup.')) == P_)
    check('M', 'a missing, duplicated, extra or reordered report is VOID',
          isvoid(c(mk(reports=[blk(n) for n in PRINTS[:-1]])))
          and isvoid(c(mk(reports=[blk(n) for n in PRINTS] + [blk(PRINTS[0])])))
          and isvoid(c(mk(reports=[blk(n) for n in PRINTS] + [blk('extra_t')])))
          and isvoid(c(mk(reports=[blk(n) for n in PRINTS[1:]] + [blk(PRINTS[0])]))))
    check('M', 'a report that does not parse (a wrapped axiom list cut short) is VOID',
          isvoid(c(mk(reports=[blk(n) for n in PRINTS[:-1]] + ["'%s%s' depends on axioms: [propext," % (NS, PRINTS[-1])]))))
    check('M', 'a log without the release gate\'s verdict line, or with the gate after the final step, is VOID',
          isvoid(c(log_ok.replace('release gate: PASS', 'release gate (no verdict)')))
          and isvoid(c(mk(before='Build completed successfully (3653 jobs).\n', after=gate + 'Post job cleanup.'))))
    check('M', 'a gate failing at a step outside the module, with clean reports, is VOID',
          isvoid(c(log_ok.replace('  PASS  lean-manuscript', '  FAIL  legacy-records')
                   .replace('release gate: PASS', 'release gate: FAILED -> legacy-records'))))
    check('M', 'a build that did not complete, without module errors, is VOID',
          isvoid(c(log_ok.replace('Build completed successfully (3653 jobs).', 'Build halted'))))
    check('M', 'sorryAx in the final step with its OK line (inconsistent evidence) is VOID, and so is an error line '
               'in a step that printed OK',
          isvoid(c(mk(reports=with_sorry))) and isvoid(c(mk(extra='OIBridge/TransSeparation.lean:157:16: error: x'))))
    sci = mk(reports=with_sorry, end=failed).replace('  PASS  lean-axioms', '  FAIL  lean-axioms') \
        .replace('release gate: PASS', 'release gate: FAILED -> lean-axioms')
    check('M', 'sorryAx in a final-step report, the step FAILED and the gate failing at lean-axioms alone, is negative '
               'in both kernel cells', c(sci) == [N_[0], N_[1], P_[2]])
    brk = mk(reports=['OIBridge/TransSeparation.lean:157:16: error: Type mismatch'] + with_sorry, end=failed, rc='1',
             before='error: build failed\n##[group]Run set -euo pipefail\n')
    check('M', 'sorryAx with a module error in the final step and no gate is negative in both kernel cells; the same '
               'with the step printing OK is VOID',
          c(brk) == [N_[0], N_[1], P_[2]] and isvoid(c(brk.replace(failed, STEP_OK))))
    check('M', 'an OK line beside a non-zero lean exit (lean crashing after its output, an uncaught exception, an '
               'error line without a position) is VOID, and so is an OK line with no exit line, two exit lines, an '
               'exit line before the last report or after the gate line, or an exit line that is not whole',
          all(isvoid(c(mk(rc=v))) for v in ('1', '139', '2'))
          and isvoid(c(mk(extra='uncaught exception: x', rc='1'))) and isvoid(c(mk(extra='error: x', rc='1')))
          and isvoid(c(mk(rc=None))) and isvoid(c(mk(extra='ktrans_sep2 axioms: lean exited 0')))
          and 'lean exit line' in c(mk(extra='ktrans_sep2 axioms: lean exited 0'))[1]
          and step_facts(mk(extra='ktrans_sep2 axioms: lean exited 0'))['exit'] is None
          and step_facts(mk(rc='139'))['exit'] == 139
          and isvoid(c(mk(reports=[blk(n) for n in PRINTS[:-1]] + ['ktrans_sep2 axioms: lean exited 0', blk(PRINTS[-1])],
                          rc=None)))
          and isvoid(c(mk(rc=None, extra='ktrans_sep2 axioms: lean exited 0')))
          and isvoid(c(mk(rc='0 (and more)'))) and isvoid(c(mk(rc='')))
          and c(mk(rc='0')) == P_)
    check('M', 'a negative reading does not depend on lean\'s exit status: a module error with lean exiting 1, or a '
               'non-standard axiom with lean exiting 0, reads negative; the same with no exit line is VOID',
          c(brk) == [N_[0], N_[1], P_[2]] and c(sci) == [N_[0], N_[1], P_[2]]
          and isvoid(c(brk.replace(head + 'ktrans_sep2 axioms: lean exited 1\n', ''))))
    check('M', 'a failed final step with every report standard and no module error is VOID, and so is one with a '
               'module error but every report standard',
          isvoid(c(mk(end=failed)))
          and isvoid(c(mk(reports=['OIBridge/TransSeparation.lean:157:16: error: x'] + [blk(n) for n in PRINTS],
                          end=failed, before='error: build failed\n##[group]Run set -euo pipefail\n'))))
    other_err = mk(reports=['OIBridge/DenseOrbit.lean:1:1: error: x'] + with_sorry, end=failed,
                   before='error: build failed\n##[group]Run set -euo pipefail\n')
    two_fail = sci.replace('  PASS  lean-manuscript', '  FAIL  lean-manuscript')
    check('M', 'the negative route needs a module error in the block (an error in another file is VOID) or the gate '
               'failing at lean-axioms alone (failing at another step too is VOID)',
          isvoid(c(other_err)) and isvoid(c(two_fail)))
    check('M', 'each forbidden token, an error line in another file, or a report outside the three axioms that '
               'names no forbidden token, beside an OK line, is VOID; a report of no axioms is standard',
          all(isvoid(c(mk(extra='uses %s' % t))) for t in ('sorryAx', 'Lean.ofReduceBool', 'Lean.trustCompiler'))
          and isvoid(c(mk(extra='OIBridge/DenseOrbit.lean:1:1: error: x')))
          and isvoid(c(mk(reports=[blk(n) if n != 'omega4_convex' else blk(n, '[propext, Foo.ax]') for n in PRINTS])))
          and c(mk(reports=[blk(n) if n != 'conv_core' else "'%s%s' does not depend on any axioms" % (NS, n)
                            for n in PRINTS])) == P_)
    check('M', 'a report head that does not parse beside the fifteen reports is VOID; the build-success line after the '
               'gate is VOID',
          isvoid(c(mk(reports=[blk(n) for n in PRINTS] + ["'%sconv_core' reports something else" % NS])))
          and isvoid(c(log_ok.replace(head + 'Build completed successfully (3653 jobs).\n', '')
                       .replace(head + 'release gate: PASS', head + 'release gate: PASS\n' + head
                                + 'Build completed successfully (3653 jobs).'))))
    check('M', 'the marker counts only as a whole line, and the block ends at the job\'s cleanup: an indented or '
               'extended marker is no marker, and a gate line after the cleanup is not read',
          isvoid(c(mk(mark=sha_e + ' (and more)')))
          and isvoid(c(log_ok.replace(head + 'ktrans_sep2 axioms: step at', head + '  ktrans_sep2 axioms: step at')))
          and isvoid(c(mk(end=None, after='Post job cleanup.\n' + STEP_OK)))
          and c(mk(after='Post job cleanup.\n' + failed)) == P_)
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
    with tempfile.TemporaryDirectory() as td:
        lp = os.path.join(td, 'log')
        open(lp, 'wb').write(b'\xef\xbb\xbf' + log_ok.replace('\n', '\r\n', 1).encode('utf-8'))
        rl = read_log(lp)
    check('M', 'the verdict reads LOG as bytes: a leading byte-order mark is dropped and a carriage return is kept, '
               'not translated',
          rl.startswith(head) and '\r\n' in rl and rl.count('\n') == log_ok.count('\n') and c(rl) == P_)
    # the final step's own gate (controls.py axioms), over the module's `lake env lean` output
    lean_out = '\n'.join(blk(n) if n != 'conv_core' else wrapped(n) for n in PRINTS) + '\n'
    ag = lambda t: all(ok for _, ok, _ in axioms_gate(t))
    check('M', 'the final step\'s gate passes the fifteen standard reports (one wrapped) and fails an empty output, a '
               'missing, duplicated, extra or reordered report, a non-standard axiom, a report that does not parse, an '
               'error line and a forbidden token',
          ag(lean_out) and not ag('') and not ag('\n'.join(blk(n) for n in PRINTS[1:]))
          and not ag(lean_out + blk(PRINTS[0])) and not ag(lean_out + blk('extra_t'))
          and not ag('\n'.join(blk(n) for n in PRINTS[1:] + PRINTS[:1]))
          and not ag(lean_out.replace(blk('omega4_convex'), sorry('omega4_convex')))
          and not ag(lean_out.replace(blk('omega4_convex'), "'%somega4_convex' depends on axioms: [propext," % NS))
          and not ag(lean_out + 'OIBridge/TransSeparation.lean:1:1: error: x\n')
          and not ag(lean_out + 'uses Lean.ofReduceBool\n'))
    fails = lambda t: sorted(lbl for lbl, ok, _ in axioms_gate(t) if not ok)
    check('M', 'the final step\'s gate fails each clause alone: a duplicated report (the report and the order), an '
               'extra report (other report), a report cut short (parse), an empty output',
          fails(lean_out + blk(PRINTS[-1])) == sorted([PRINTS[-1], 'the reports in print order'])
          and fails(lean_out + blk('extra_t')) == sorted(['no other report', 'the reports in print order'])
          and fails(lean_out + "'%sconv_core' depends on axioms: [propext," % NS) == ['every report parses']
          and fails('') == ['the output is not empty']
          and fails(lean_out.replace(blk('omega4_convex'), blk('omega4_convex', '[propext, Foo.ax]'))) == ['omega4_convex'])
    rcs = []
    with tempfile.TemporaryDirectory() as td:
        for name, text in (('ok', lean_out), ('bad', lean_out.replace(blk('omega4_convex'), sorry('omega4_convex')))):
            fp = os.path.join(td, name)
            open(fp, 'w').write(text)
            capture(lambda: rcs.append(main(['axioms', fp])))
            rcs.append(LAST_OUT[0].rstrip('\n').split('\n')[-1])
    check('M', 'the axioms command exits 0 and ends with the OK line on the fifteen standard reports, and exits 1 and '
               'ends with the FAILED line on a non-standard one',
          rcs[0] == 0 and rcs[1] == STEP_OK and rcs[2] == 1 and STEP_FAILED.match(rcs[3]) is not None)
    check('M', 'the final step\'s gate labels name no forbidden token and no report, since they land in the log',
          not any(b in label + detail for label, _, detail in axioms_gate(lean_out + 'sorryAx\n') for b in BAD_TOKENS)
          and not any(BLOCK_HEAD.search(label) for label, _, _ in axioms_gate(lean_out)))
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
    check('M', 'census: the family is inserted once directly before KTOKEN-MAXCONE-1\'s, which stays last; a changed '
               'status, a moved family and a whitespace change differ from the frozen edit',
          len(k) == 1 and dd['families'][k[0] + 1]['modules'] == PREV_FAMILY_MODULES
          and k[0] + 2 == len(dd['families'])
          and json.dumps(bad, indent=2, ensure_ascii=False) + '\n' != gc and gc.replace('\n', '\n ', 1) != gc
          and gc != d_cen)
    gw = workflow_want(d_wf)
    check('M', 'workflow: the six splices apply once each; without the aggregate test line, the shard or the final '
               'step it differs',
          gw is not None and gw.replace('          test "${KTRANSSEP2_RESULT}" = success\n', '') != gw
          and gw.replace(SHARD, '') != gw and gw.replace(FINAL_STEP, '') != gw and gw.count('probes_ktranssep2') == 3
          and workflow_want(gw) is None)
    check('M', 'KTOKEN-MAXCONE-1\'s live self-test still holds on D\'s files with the frozen edits (each of its splices '
               'once, its root line, its census family last), as it does on D; the edits of the first draft broke it',
          ktoken_live_ok(gw, gi, gc) and ktoken_live_ok(d_wf, d_imp, d_cen)
          and not ktoken_live_ok(d_wf.replace('probes_ktokenmaxcone1, probes_a42_witness',
                                              'probes_ktokenmaxcone1, probes_ktranssep2, probes_a42_witness'), gi, gc)
          and not ktoken_live_ok(gw, gi, json.dumps(dict(json.loads(gc), families=json.loads(gc)['families'][:-2] + [
              json.loads(gc)['families'][-1], json.loads(gc)['families'][-2]]))))
    tail = gw.split(FINAL_STEP, 1)[1].split('\n  # Probe shards run independently', 1)[0] if gw else ''
    check('M', 'workflow: the final step is the bridge job\'s last step, after KTOKEN-MAXCONE-1\'s check A3, runs when '
               'an earlier step failed, prints the marker the verdict reads and runs this file\'s axioms gate',
          gw is not None and gw.count(FINAL_STEP) == 1 and gw.index(A3_RUN) < gw.index(FINAL_STEP)
          and '      - name:' not in tail and gw.index(FINAL_STEP) < gw.index('\n  probes_core_a:')
          and "if: ${{ !cancelled() }}" in FINAL_STEP
          and 'echo "ktrans_sep2 axioms: step at $(git rev-parse HEAD)"' in FINAL_STEP
          and (CONTROLS[len('verification/'):] + ' axioms') in FINAL_STEP)
    body = FINAL_STEP.split('run: |\n', 1)[1].split('\n')
    cmds = [l.strip() for l in body if l.strip()]
    check('M', 'workflow: the final step elaborates the module itself, keeps lean\'s exit status, prints the output, '
               'runs the gate as a plain command and exits with lean\'s status; nothing in it continues on error',
          'lake env lean OIBridge/TransSeparation.lean > "$log" 2>&1 || rc=$?' in cmds and 'cat "$log"' in cmds
          and cmds[-1] == 'exit "$rc"' and cmds[-2].endswith('controls.py axioms "$log"')
          and '||' not in cmds[-2] and 'continue-on-error' not in FINAL_STEP
          and cmds.index('cat "$log"') < len(cmds) - 2)
    check('M', 'workflow: the final step sets -e itself rather than relying on the runner\'s default, initialises the '
               'status before lean runs, and prints lean\'s status after its output and before the gate',
          cmds[0] == 'set -euo pipefail' and cmds.count('rc=0') == 1
          and cmds.index('rc=0') < cmds.index('lake env lean OIBridge/TransSeparation.lean > "$log" 2>&1 || rc=$?')
          and cmds.count('echo "ktrans_sep2 axioms: lean exited ${rc}"') == 1
          and cmds.index('cat "$log"') < cmds.index('echo "ktrans_sep2 axioms: lean exited ${rc}"') == len(cmds) - 3
          and not any(re.match(r'set\s+\+', x) for x in cmds) and 'shell:' not in FINAL_STEP)
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
    rl = {n: 4900 + i for i, n in enumerate(PRINTS)}
    run_ev = dict(ev, run={'head_sha': f_, 'head_branch': 'b', 'id': 1, 'event': 'workflow_dispatch',
                           'conclusion': 'success'},
                  jobs=[{'name': 'a', 'conclusion': 'success'}],
                  source={'served_sha256': 'a' * 64, 'original_lines': 9000, 'served_lines': 5000},
                  observed={'transseparation_window': {'served_lines': 5000, 'built_line': None, 'status_word': None,
                                                        'cache_hit': True, 'report_lines': {}, 'gate_start': 2000,
                                                        'gate_end': 2030},
                            'axioms_step': {'marker_line': 4899, 'commit': f_, 'report_lines': rl,
                                            'ok_lines': [4920], 'failed_lines': [], 'exit_lines': [4916],
                                            'exit': 0}},
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
    ax_ = 'observed__axioms_step__'
    check('M', 'a run result naming its head, green, with the gate and then the final step\'s block for it inside the '
               'window passes; another head, a push event, a failed run conclusion, a failed job, no jobs, the step run '
               'at another commit, a report past the window, a missing report, the block before the gate, the OK line '
               'before a report or missing or doubled, a FAILED line, a non-zero, missing, doubled or misplaced lean '
               'exit line, a non-standard axiom and a failed gate fail',
          run_window_ok(json.dumps(run_ev), f_) and not run_window_ok(json.dumps(run_ev), e_)
          and not run_window_ok(rw(run__event='push'), f_) and not run_window_ok(rw(run__conclusion='failure'), f_)
          and not run_window_ok(rw(jobs=[{'name': 'a', 'conclusion': 'failure'}]), f_)
          and not run_window_ok(rw(jobs=[]), f_)
          and not run_window_ok(rw(**{ax_ + 'commit': e_}), f_)
          and not run_window_ok(rw(**{ax_ + 'report_lines': dict(rl, conv_core=5001)}), f_)
          and not run_window_ok(rw(**{ax_ + 'report_lines': {k: v for k, v in rl.items() if k != 'conv_core'}}), f_)
          and not run_window_ok(rw(**{ax_ + 'marker_line': 1999}), f_)
          and not run_window_ok(rw(**{ax_ + 'ok_lines': [4910]}), f_) and not run_window_ok(rw(**{ax_ + 'ok_lines': []}), f_)
          and not run_window_ok(rw(**{ax_ + 'ok_lines': [4920, 4921]}), f_)
          and not run_window_ok(rw(**{ax_ + 'failed_lines': [4921]}), f_)
          and not run_window_ok(rw(**{ax_ + 'exit': 1}), f_) and not run_window_ok(rw(**{ax_ + 'exit': None}), f_)
          and not run_window_ok(rw(**{ax_ + 'exit_lines': []}), f_)
          and not run_window_ok(rw(**{ax_ + 'exit_lines': [4916, 4917]}), f_)
          and not run_window_ok(rw(**{ax_ + 'exit_lines': [4921]}), f_)
          and not run_window_ok(rw(**{ax_ + 'exit_lines': [4910]}), f_)
          and not run_window_ok(rw(expected__modules={'OIBridge/TransSeparation.lean': {
              'status': 'complete', 'reports': [{'name': NS + n, 'axioms': ['sorryAx']} for n in PRINTS]}}), f_)
          and not run_window_ok(rw(expected__gate={'verdict': 'FAILED -> lean-axioms'}), f_)
          and not run_window_ok(rw(expected__gate={'verdict': 'PASSING'}), f_)
          and not run_window_ok('not json', f_))
    check('M', 'a replay run result passes only when its window shows the primary-key cache hit and no `Built` line '
               'for the module; two run results are other runs only with the same head and branch and different run '
               'ids; the OK line past the window fails',
          run_window_ok(json.dumps(run_ev), f_, replayed=True)
          and not run_window_ok(rw(observed__transseparation_window__cache_hit=False), f_, replayed=True)
          and run_window_ok(rw(observed__transseparation_window__cache_hit=False), f_)
          and not run_window_ok(rw(**{ax_ + 'ok_lines': [5001]}), f_)
          and not other_run(rw(run__id=2, run__head_sha=e_), json.dumps(run_ev))
          and run_window_ok(rw(observed__transseparation_window__status_word='Replayed'), f_, replayed=True)
          and not run_window_ok(rw(observed__transseparation_window__status_word='Built'), f_, replayed=True)
          and run_window_ok(rw(observed__transseparation_window__status_word='Built'), f_)
          and other_run(rw(run__id=2), json.dumps(run_ev)) and not other_run(json.dumps(run_ev), json.dumps(run_ev))
          and not other_run(rw(run__id=2, run__head_branch='c'), json.dumps(run_ev)))
    check('M', 'the gate verdict is PASS alone or with a note, never a longer word or another status',
          gate_passed('PASS') and gate_passed('PASS  (note: --label bNNN not given)') and not gate_passed('PASSED')
          and not gate_passed('PASSING (note)') and not gate_passed('FAILED -> x') and not gate_passed(None))
    # F's run shows D's workflow and gate passing on D plus the control plane: the corrected rule on KTRANS-SEP-1's
    # real F run (module absent), and the
    # negative controls. The fixture is that run's derived result, embedded verbatim (sha256 KTSEP1_FRUN_SHA256).
    real_f = KTSEP1_FRUN
    real_head = json.loads(real_f)['run']['head_sha']
    ref1 = cat_blob(KTSEP1_PTR_BLOB)
    check('M', 'the real F-run fixture is KTRANS-SEP-1\'s derived result, byte for byte, and its reference is '
               'KTRANS-SEP-1\'s predicted tree\'s run result, read by blob id',
          hashlib.sha256(real_f.encode()).hexdigest() == KTSEP1_FRUN_SHA256 and ref1 is not None
          and hashlib.sha256(ref1.encode()).hexdigest() == KTSEP1_PTR_SHA256)
    fok = lambda data, head, ref=ref1: frun_ok(data, head, ref, KTSEP1_SHARD_JOB)
    check('M', 'F\'s run rule accepts the real F run of KTRANS-SEP-1 (identity, every job success, exactly the '
               'predicted run\'s jobs less its shard, gate PASS on exactly its steps) and its log is consistent with '
               'no module; the halted round\'s rule, which demanded the module window of F\'s run, rejects it',
          fok(real_f, real_head) and frun_log_consistent(real_f) and not run_window_ok(real_f, real_head))
    fr = json.loads(real_f)

    def fw(**kw):
        d = json.loads(json.dumps(fr))
        for path, v in kw.items():
            x = d
            ks = path.split('__')
            for k in ks[:-1]:
                x = x[k]
            x[ks[-1]] = v
        return json.dumps(d)
    steps = fr['expected']['gate']['steps']
    ref_j = json.loads(ref1)
    check('M', 'F\'s run rule rejects a failed or misidentified run: another head, another workflow, another job, '
               'no run id, no job id, a push event, no attempt or attempt 0, a failed run conclusion, a failed bridge '
               'job, a failed job, no jobs, a job list cut to one entry, a job dropped, a job added, a job listed '
               'twice, a failed build, a failed gate verdict, a verdict that only begins with PASS, a failed gate '
               'step, a gate missing a step, a gate step renamed, a pass count short of the steps, a reference without the shard, '
               'and non-JSON',
          not fok(real_f, f_) and not fok(fw(run__workflow='reproduce-evidence.yml'), real_head)
          and not fok(fw(run__job_name='Lean kernel check'), real_head)
          and not fok(fw(run__id=None), real_head) and not fok(fw(run__job_id=None), real_head)
          and not fok(fw(run__event='push'), real_head)
          and not fok(fw(run__attempt=None), real_head) and not fok(fw(run__attempt=0), real_head)
          and not fok(fw(run__conclusion='failure'), real_head)
          and not fok(fw(run__job_conclusion='failure'), real_head)
          and not fok(fw(jobs=fr['jobs'][:-1] + [dict(fr['jobs'][-1], conclusion='failure')]), real_head)
          and not fok(fw(jobs=[]), real_head) and not fok(fw(jobs=fr['jobs'][:1]), real_head)
          and not fok(fw(jobs=fr['jobs'][:-1]), real_head)
          and not fok(fw(jobs=fr['jobs'] + [{'name': 'Numerical probes / extra', 'conclusion': 'success'}]), real_head)
          and not fok(fw(jobs=fr['jobs'][:-1] + [fr['jobs'][0]]), real_head)
          and not fok(fw(expected__build_success=False), real_head)
          and not fok(fw(expected__gate__verdict='FAILED -> lean-axioms'), real_head)
          and not fok(fw(expected__gate__verdict='PASSING'), real_head)
          and not fok(fw(expected__gate__steps=steps[:-1] + [dict(steps[-1], status='FAIL')]), real_head)
          and not fok(fw(expected__gate__steps=steps[:-1], expected__gate__steps_pass=len(steps) - 1,
                         expected__gate__steps_total=len(steps) - 1), real_head)
          and not fok(fw(expected__gate__steps=steps[:-1] + [dict(steps[-1], name='renamed')]), real_head)
          and not fok(fw(expected__gate__steps_pass=len(steps) - 1), real_head)
          and not fok(real_f, real_head, json.dumps(dict(ref_j, jobs=[j for j in ref_j['jobs']
                                                                     if j['name'] != KTSEP1_SHARD_JOB])))
          and not fok('not json', real_head))
    check('M', 'the log consistency check flags module evidence (a build line, a report, the module complete), and '
               'the run rule does not read it: absence is never proved from a log',
          not frun_log_consistent(fw(observed__transseparation_window__built_line=4896))
          and not frun_log_consistent(fw(observed__transseparation_window__report_lines={'conv_core': 4910}))
          and not frun_log_consistent(fw(expected__modules={'OIBridge/TransSeparation.lean': {'status': 'complete',
                                                                                            'reports': []}}))
          and fok(fw(observed__transseparation_window__built_line=4896), real_head)
          and not frun_log_consistent(fw(observed__axioms_step={'marker_line': 4900})))
    # The proof of absence is F's tree. Scratch commits on D (temporary objects, no ref): one that adds only a
    # control-plane file, one that adds the module, one that adds only the import line, one that adds the import beside
    # another module on one line, one that adds the probe, and one that adds the module at another path.
    other = 'verification/lean-mathlib/OIBridge/Elsewhere.lean'
    same_line = d_imp.replace(ANCHOR_IMPORT, ANCHOR_IMPORT.rstrip('\n') + ' OIBridge.TransSeparation\n', 1)
    with Scratch() as s:
        ctl = s.commit(D, {PREREG: s.blob('x\n')}, 'scratch: control plane only')
        cases = [s.commit(D, {MOD: MOD_BLOB}, 'scratch: the module'),
                 s.commit(D, {IMPORTS: s.blob(gi)}, 'scratch: the import line'),
                 s.commit(D, {IMPORTS: s.blob(same_line)}, 'scratch: the import beside another module'),
                 s.commit(D, {PROBE: PROBE_BLOB}, 'scratch: the probe'),
                 s.commit(D, {other: MOD_BLOB}, 'scratch: the module at another path')]
        verdicts = {c: fstage_ok(fw(run__head_sha=c), c, c, ref1, KTSEP1_SHARD_JOB) for c in [ctl] + cases}
        unreadable = ftree_at('0' * 40)
        d_tree = ftree_at(D)
    check('M', 'F\'s tree rule accepts a control-plane-only tree on D and reads D\'s Lean directories and its '
               'OIBridge.lean as carrying no module; an unreadable commit fails',
          verdicts[ctl] == (True, True, True) and ftree_ok(*d_tree, d_tree[2]) and None not in d_tree[2]
          and not ftree_ok(*unreadable, d_tree[2]))
    dp, di, dt = d_tree
    check('M', 'F\'s tree rule fails on each clause alone, with the Lean directories equal to D\'s: the probe\'s path, '
               'the module\'s path, an import line (alone or beside another module), an unreadable OIBridge.lean, and '
               'unequal or unreadable directory trees',
          not ftree_ok(dp | {PROBE}, di, dt, dt) and not ftree_ok(dp | {MOD}, di, dt, dt)
          and not ftree_ok(dp, gi, dt, dt) and not ftree_ok(dp, same_line, dt, dt) and not ftree_ok(dp, None, dt, dt)
          and not ftree_ok(dp, di, (dt[0], 'f' * 40), dt) and not ftree_ok(dp, di, (dt[0], None), dt)
          and not ftree_ok(dp, di, None, dt) and not ftree_ok(dp, di, dt, None) and ftree_ok(dp, di, dt, dt))
    check('M', 'negative control, the proof of absence is the tree: a tree containing the module (at its path or '
               'another), the import line (alone or beside another module) or the probe fails the F-stage check '
               'although its run evidence names it, is green, passes the gate and its log has no module lines',
          all(verdicts[c] == (False, True, True) for c in cases))
    check('M', 'the import rule matches the import line however indented and beside other modules, and not a longer '
               'module name, a commented-out line or a qualified name',
          IMPORT_RE.search('  import OIBridge.TransSeparation\n') is not None
          and IMPORT_RE.search('import OIBridge.KTokenMaxCone OIBridge.TransSeparation\n') is not None
          and IMPORT_RE.search('import OIBridge.TransSeparationX\n') is None
          and IMPORT_RE.search('-- import OIBridge.TransSeparation\n') is None
          and IMPORT_RE.search('import X.OIBridge.TransSeparation\n') is None)
    check('M', 'negative control, missing module evidence where the module is required: the real F run, offered as a '
               'module-bearing run result (the predicted tree\'s or E\'s), is rejected',
          not run_window_ok(real_f, real_head) and not run_window_ok(real_f, f_))
    sec = '### The predicted execution tree\n\n'
    check('M', 'the predicted head is read from the predicted-tree section\'s first line and nowhere else; the '
               'section as KTRANS-SEP-2\'s first draft wrote it (a paragraph, then a bullet naming another round\'s '
               'tree) names none',
          predicted_head('x\n%s- **`%s`** (a child of D)\n' % (sec, f_)) == f_
          and predicted_head('- **`%s`**\n' % f_) is None
          and predicted_head('%sThis round\'s predicted tree is built on this `D`.\n\n- **`%s`**\n' % (sec, f_)) is None
          and predicted_head('%s- **KTRANS-SEP-1\'s predicted tree, provenance: `%s`**\n' % (sec, f_)) is None)
    check('M', 'the controls pin reads one pinned or pending row; two rows, none, or a short id are absent',
          controls_pin('**The frozen `controls.py`:** blob `%s`.\n' % ('a' * 40)) == ('pinned', 'a' * 40)
          and controls_pin('**The frozen `controls.py`:** blob pending.\n') == ('pending', None)
          and controls_pin('') == ('absent', None)
          and controls_pin('**The frozen `controls.py`:** blob `%s`.\n' % ('a' * 39)) == ('absent', None)
          and controls_pin('**The frozen `controls.py`:** blob pending.\n' * 2) == ('absent', None))
    self_test_e2e(d_imp, d_cen, d_wf, [s_['name'] for s_ in steps])


# ---- the end-to-end self-test: derive-run, check and mock-s1 on scratch commits ---------------------------------
def synth_log(module, steps, verdict='PASS  (note: scratch)', cut=None, word='Built', reports=True, head=None,
              step_end=None, cache_hit=False, lean_rc=0):
    """A served bridge log in a simplified form of the real layout (timestamped lines, as served, with no final
    newline): the build, with the module's status line (word: Built, or Replayed when restored from the build cache)
    and, when reports is true, its fifteen reports, when module is true; the release-gate block with the given
    steps; with head, the final bridge step's block for head (one report wrapped as Lean wraps it); and a closing
    line."""
    mod = cat_blob(MOD_BLOB)
    ts = '2026-01-01T00:00:00.0000000Z '
    L = ['Run lake build', 'info: building']
    if module:
        L.append('✔ [3650/3653] %s OIBridge.TransSeparation' % word)
    if module and reports:
        L += ["info: OIBridge/TransSeparation.lean:%d:0: '%s%s' depends on axioms: [propext, Classical.choice, "
              "Quot.sound]" % (n, NS, l[len('#print axioms ' + NS):].strip()) for n, l in print_lines(mod)]
    L += ['ℹ [3652/3653] %s OIBridge' % word, 'Build completed successfully (3653 jobs).', 'release gate', '']
    L += ['  %s  %-16s %s: OK' % (st, n, n) for n, st in steps]
    L += ['', 'release gate: %s' % verdict]
    if head:
        L += ['##[group]Run set -euo pipefail', 'ktrans_sep2 axioms: step at %s' % head]
        for n in PRINTS:
            L += (["'%s%s' depends on axioms: [propext," % (NS, n), ' Classical.choice,', ' Quot.sound]']
                  if n == 'conv_core' else ["'%s%s' depends on axioms: [propext, Classical.choice, Quot.sound]" % (NS, n)])
        L += ['ktrans_sep2 axioms: lean exited %s' % lean_rc, 'PASS axioms: no other report', step_end or STEP_OK]
    L += ['Post job cleanup.']
    L += ['Cache hit occurred on the primary key oibridge-Linux-scratch, not saving cache.' if cache_hit
          else 'Cache saved with key: oibridge-Linux-scratch', 'Post job cleanup.']
    if cut:
        L = L[:cut]
    return '\n'.join(ts + l for l in L).encode('utf-8')


def synth_api(head, names, mcp=False, conclusion='success', failed=(), run_id=4242):
    run = {'id': run_id, 'head_sha': head, 'event': 'workflow_dispatch', 'conclusion': conclusion, 'run_attempt': 1,
           'path': '.github/workflows/verify.yml', 'head_branch': 'scratch', 'created_at': '2026-01-01T00:00:00Z'}
    js = [{'id': 1000 + i, 'name': n, 'conclusion': 'failure' if n in failed else 'success',
           'started_at': '2026-01-01T00:00:00Z',
           'steps': [{'name': 'Build', 'conclusion': 'success', 'number': 1}]} for i, n in enumerate(names)]
    jobs = {'total_count': len(js), 'jobs': js}
    return json.dumps(run).encode(), json.dumps({'jobs': jobs} if mcp else jobs).encode()


def synth_prereg(pred, pins, ctl, section=None):
    rows = '\n'.join('| `%s` | %s |' % (p, '`%s`' % d if d else 'pending') for p, d in sorted(pins.items()))
    sec = section if section is not None else '- **`%s`** (scratch predicted tree)\n' % pred
    return ('# scratch preregistration\n\n| path | sha256 |\n| --- | --- |\n%s\n\n**The frozen `controls.py`:** blob %s.\n'
            '\n### The predicted execution tree\n\n%s' % (rows, '`%s`' % ctl if ctl else 'pending', sec))


def self_test_e2e(d_imp, d_cen, d_wf, step_names):
    me = open(os.path.abspath(__file__), encoding='utf-8').read()
    steps = [(n, 'PASS') for n in step_names]
    base_jobs = ['Lean kernel check', 'Mathlib bridge', 'Numerical probes', 'Numerical probes / core A']
    meta = lambda b_: {'original_lines': b_.decode('utf-8').count('\n') + 1 + 30000,
                       'served_lines': b_.decode('utf-8').count('\n') + 1}
    ml = lambda h, **kw: synth_log(True, steps, head=h, **kw)
    replay_log = lambda h: synth_log(False, steps, head=h, word='Replayed', cache_hit=True)
    # derive-run, alone
    a40, b40 = 'a' * 40, 'b' * 40
    fl = synth_log(False, steps)
    ra, ja = synth_api(a40, base_jobs)
    absent = json.loads(derive_run(fl, meta(fl), ra, ja))
    present = json.loads(derive_run(ml(b40), meta(ml(b40)), *synth_api(b40, base_jobs + [SHARD_JOB], mcp=True)))
    mstat = lambda d: d['expected']['modules']['OIBridge/TransSeparation.lean']

    def refused(*a):
        try:
            derive_run(*a)
            return False
        except (ValueError, KeyError, TypeError):
            return True
    check('M', 'derive-run: a log without the module or the final step gives status absent and the gate steps; a log '
               'with the final step for the run\'s head gives status complete with its fifteen reports in print order '
               '(one wrapped); both are structured results without run-varying fields, and the same inputs give the '
               'same bytes',
          mstat(absent) == {'status': 'absent', 'reports': []}
          and absent['observed']['transseparation_window']['built_line'] is None
          and absent['observed']['axioms_step']['marker_line'] is None
          and [x['name'] for x in absent['expected']['gate']['steps']] == step_names
          and absent['expected']['gate']['steps_pass'] == len(step_names) and gate_passed(absent['expected']['gate']['verdict'])
          and mstat(present)['status'] == 'complete'
          and [x['name'] for x in mstat(present)['reports']] == [NS + n for n in PRINTS]
          and run_window_ok(json.dumps(present), b40)
          and evidence_ok(json.dumps(absent)) and evidence_ok(json.dumps(present))
          and derive_run(fl, meta(fl), ra, ja) == derive_run(fl, meta(fl), ra, ja))
    st = lambda lg: mstat(json.loads(derive_run(lg, meta(lg), ra, ja)))['status']
    rep_ = json.loads(derive_run(replay_log(a40), meta(replay_log(a40)), ra, ja))
    bom = json.loads(derive_run(b'\xef\xbb\xbf' + fl, meta(fl), ra, ja))
    check('M', 'derive-run: with the module replayed and its build lines outside the window, the final step still '
               'gives status complete and the window shows no `Built`; build lines without the final step, the step '
               'for another commit, or the step cut before its gate line, are incomplete; a byte-order mark changes '
               'only the text\'s digest',
          mstat(rep_)['status'] == 'complete' and run_window_ok(json.dumps(rep_), a40, replayed=True)
          and st(ml(None)) == 'incomplete' and st(ml(b40)) == 'incomplete' and st(ml(a40, cut=-5)) == 'incomplete'
          and st(ml(a40, step_end='ktrans_sep2 axioms: FAILED (1 check(s))')) == 'incomplete'
          and st(ml(a40)) == 'complete'
          and st(synth_log(False, steps, head=a40, step_end='x')) == 'incomplete'
          and st(fl + b'\n2026-01-01T00:00:00.0000000Z ktrans_sep2 axioms: step at ' + a40.encode()) == 'incomplete'
          and dict(bom, source=None) == dict(absent, source=None)
          and bom['source']['served_sha256'] != absent['source']['served_sha256'])
    fresh = synth_log(False, steps, head=a40, word='Replayed')
    fresh_ = json.loads(derive_run(fresh, meta(fresh), ra, ja))
    crash = ml(a40, lean_rc=139)
    crash_ = json.loads(derive_run(crash, meta(crash), ra, ja))
    check('M', 'derive-run reads the cache line and the lean exit line from the log: a run whose post step saved the '
               'cache records no hit and fails the replay requirement while passing the plain one; a run whose lean '
               'exited non-zero beside an OK line records that status, is incomplete and fails the window check',
          rep_['observed']['transseparation_window']['cache_hit'] is True
          and fresh_['observed']['transseparation_window']['cache_hit'] is False
          and run_window_ok(json.dumps(fresh_), a40) and not run_window_ok(json.dumps(fresh_), a40, replayed=True)
          and rep_['observed']['axioms_step']['exit'] == 0 and crash_['observed']['axioms_step']['exit'] == 139
          and mstat(crash_)['status'] == 'incomplete' and not run_window_ok(json.dumps(crash_), a40))
    blk_only = b'\n'.join(l for l in ml(a40).split(b'\n') if b'info:' not in l and (
        b'ktrans_sep2' in l or b"'OIBridge" in l or l.endswith((b'Classical.choice,', b'Quot.sound]'))))
    bom_blk = json.loads(derive_run(b'\xef\xbb\xbf' + blk_only, meta(blk_only), ra, ja))
    red_bridge = json.loads(derive_run(fl, meta(fl), *synth_api(a40, base_jobs, failed=['Mathlib bridge'])))
    check('M', 'derive-run reads the final step\'s marker on the first line behind a byte-order mark, records the '
               'bridge job\'s own failed conclusion, and reads a gate step on the line directly after the gate\'s heading',
          bom_blk['observed']['axioms_step']['marker_line'] == 1
          and len(bom_blk['observed']['axioms_step']['report_lines']) == len(PRINTS)
          and red_bridge['run']['job_conclusion'] == 'failure'
          and gate_steps(['release gate', '  PASS  a  x', 'release gate: PASS'], 1, 3) == [{'name': 'a', 'status': 'PASS'}])
    check('M', 'derive-run refuses metadata that does not describe the text, an incomplete jobs answer, no bridge job '
               'and a job listed twice',
          refused(fl, dict(meta(fl), served_lines=5), ra, ja)
          and refused(fl, meta(fl), ra, json.dumps({'total_count': 9, 'jobs': json.loads(ja)['jobs']}).encode())
          and refused(fl, meta(fl), *synth_api(a40, ['Lean kernel check']))
          and refused(fl, meta(fl), *synth_api(a40, base_jobs + ['Mathlib bridge'])))
    # Scratch commits (temporary objects, no ref): the predicted tree P and candidate F, as the round builds them.
    runs = (RUN_EVIDENCE, REPLAY_EVIDENCE)
    ev = {p: json.dumps({'schema': 'oi-evidence-result', 'version': 1, 'form': 'complete', 'kind': p}).encode()
          for p in REQUIRED_EVIDENCE if p not in runs}
    with Scratch() as s:
        exe = {MOD: MOD_BLOB, PROBE: PROBE_BLOB, IMPORTS: s.blob(imports_want(d_imp)),
               CENSUS: s.blob(census_want(d_cen)), WORKFLOW: s.blob(workflow_want(d_wf))}
        draft = synth_prereg(None, dict({p: hashlib.sha256(b).hexdigest() for p, b in ev.items()},
                                        **{p: None for p in runs}),
                             blob_id(me), section='This revision is the drafting revision.\n')
        rec = {PREREG: s.blob(draft), CONTROLS: s.blob(me)}
        rec.update({RDIR + p: s.blob(b) for p, b in ev.items()})
        P = s.commit(D, dict(rec, **exe), 'scratch predicted tree')
        jobs_p = base_jobs + [SHARD_JOB]
        pair = lambda h: (derive_run(ml(h), meta(ml(h)), *synth_api(h, jobs_p)).encode(),
                          derive_run(replay_log(h), meta(replay_log(h)), *synth_api(h, jobs_p, run_id=4243)).encode())
        ptr, ptr_rep = pair(P)
        pins_of = lambda a, b: dict({p: hashlib.sha256(x).hexdigest() for p, x in ev.items()},
                                    **{RUN_EVIDENCE: hashlib.sha256(a).hexdigest(),
                                       REPLAY_EVIDENCE: hashlib.sha256(b).hexdigest()})
        pin = pins_of(ptr, ptr_rep)

        def cand(pins=pin, ctl=blob_id(me), section=None, extra=None, pred=P):
            return s.commit(D, dict({PREREG: s.blob(synth_prereg(pred, pins, ctl, section))}, **(extra or {})),
                            'scratch candidate F')
        F_ = cand()
        frun_in = lambda head, log=fl, names=base_jobs: (log, meta(log)) + synth_api(head, names)

        def mock(candf, inputs, frun=None, extra_ev=((RUN_EVIDENCE, ptr), (REPLAY_EVIDENCE, ptr_rep)), predicted=P):
            frun = frun if frun is not None else derive_run(*inputs).encode()
            return lambda: mock_s1(candf, frun, predicted, list(extra_ev), *inputs, s=s)
        check('M', 'the predicted tree P passes check without --freeze (its run results pending)',
              not capture(lambda: run_check(P))[0])
        failed, ran = capture(mock(F_, frun_in(F_)))
        out = LAST_OUT[0]
        check('M', 'mock-s1 on a candidate F with its own derived run result passes, running every required control, '
                   'the three F-stage checks of P and both predicted-tree run checks (failed: %s)' % (sorted(failed) or 'none'),
              not failed and REQUIRED_CODES <= set(ran) and 'P    F has no module' in out
              and 'P    F\'s exact-head run is retained' in out and 'P    consistency, not the proof' in out
              and 'P    the f-run file' in out and 'P    the predicted tree given' in out
              and 'P    the predicted tree\'s retained run' in out and 'P    the predicted tree\'s second run' in out)
        A_RUN, A_CONS, A_FILE = 'F\'s exact-head run is retained', 'consistency, not the proof', 'the f-run file'
        A_NAMED, A_SEC, A_PIN = 'the predicted tree given is the one', 'the predicted-tree section names', 'the pinned evidence'
        A_PTR, A_TREE, A_B = 'the predicted tree\'s retained run', 'F has no module', 'the probe is the frozen blob'
        A_REP = 'the predicted tree\'s second run'
        must_fail_at('mock-s1 with a run result naming another head', 'P', mock(F_, frun_in(P)), A_RUN, only=True)
        must_fail_at('mock-s1 with a run result whose log carries the module', 'P', mock(F_, frun_in(F_, log=ml(F_))),
                     A_CONS, only=True)
        must_fail_at('mock-s1 with a run result missing a job of the predicted run', 'P',
                     mock(F_, frun_in(F_, names=base_jobs[:-1])), A_RUN, only=True)
        must_fail_at('mock-s1 with a run result that is not derive-run\'s output over the inputs given', 'P',
                     mock(F_, frun_in(F_), frun=json.dumps(json.loads(derive_run(*frun_in(F_))), indent=2).encode()),
                     A_FILE, only=True)
        P2 = s.commit(D, dict(rec, **exe), 'scratch predicted tree, a second commit of the same tree')
        must_fail_at('mock-s1 given a predicted tree, of the same content, other than the one candidate F names', 'P',
                     mock(F_, frun_in(F_), predicted=P2), A_NAMED, only=True)
        must_fail_at('mock-s1 given a commit without the execution files as the predicted tree', 'P',
                     mock(F_, frun_in(F_), predicted=D), A_NAMED)
        f_sep1 = cand(section='This round\'s predicted tree is built on this `D`.\n\n- **KTRANS-SEP-1\'s predicted '
                              'tree, provenance: `%s`**\n' % P)
        must_fail_at('mock-s1 on a candidate F whose predicted-tree section is in the first draft\'s form', 'P',
                     mock(f_sep1, frun_in(f_sep1)), A_SEC, only=True)
        f_mod = cand(extra={MOD: MOD_BLOB})
        failed, _ = capture(mock(f_mod, frun_in(f_mod)))
        check('M', 'mock-s1 on a candidate F carrying the module fails T and P at the tree check (failed: %s)'
              % sorted(failed), {'T', 'P'} <= failed and '  FAIL  P    ' + A_TREE in LAST_OUT[0])
        red = [('a failed run conclusion', frun_in(F_)[:2] + synth_api(F_, base_jobs, conclusion='failure')),
               ('a failed job', frun_in(F_)[:2] + synth_api(F_, base_jobs, failed=['Numerical probes / core A'])),
               ('a failed Mathlib bridge job', frun_in(F_)[:2] + synth_api(F_, base_jobs, failed=['Mathlib bridge'])),
               ('a failed gate step', (lambda lg: (lg, meta(lg)) + synth_api(F_, base_jobs))(
                   synth_log(False, steps[:-1] + [(steps[-1][0], 'FAIL')], verdict='FAILED -> ' + steps[-1][0])))]
        for label, inputs in red:
            must_fail_at('mock-s1 with %s in candidate F\'s run, carried through derive-run' % label, 'P',
                         mock(F_, inputs), A_RUN, only=True)
        alt = me + '\n# another controls.py\n'
        P_alt = s.commit(D, dict(rec, **dict(exe, **{CONTROLS: s.blob(alt)})), 'scratch predicted tree, another controls.py')
        alt_pair = pair(P_alt)
        f_alt = cand(pins=pins_of(*alt_pair), pred=P_alt)
        must_fail_at('mock-s1 whose stage-1 controls.py is not the file running, though the pin names the running file',
                     'B', mock(f_alt, frun_in(f_alt), extra_ev=tuple(zip(runs, alt_pair)), predicted=P_alt), A_B,
                     only=True)
        f_ctl = cand(ctl='0' * 40)
        must_fail_at('mock-s1 on a candidate F pinning another controls.py blob', 'B', mock(f_ctl, frun_in(f_ctl)),
                     A_B, only=True)
        f_pend = cand(ctl=None)
        must_fail_at('mock-s1 on a candidate F with the controls.py pin pending', 'B', mock(f_pend, frun_in(f_pend)),
                     A_B, only=True)
        must_fail_at('mock-s1 with a pinned evidence file that differs from its pin', 'P',
                     mock(F_, frun_in(F_), extra_ev=((RUN_EVIDENCE, ptr + b'\n'), (REPLAY_EVIDENCE, ptr_rep))), A_PIN,
                     only=True)
        ptr_other = derive_run(ml(D), meta(ml(D)), *synth_api(D, jobs_p)).encode()
        f_po = cand(pins=pins_of(ptr_other, ptr_rep))
        must_fail_at('mock-s1 with a predicted-tree run result naming another commit', 'P',
                     mock(f_po, frun_in(f_po), extra_ev=((RUN_EVIDENCE, ptr_other), (REPLAY_EVIDENCE, ptr_rep))), A_PTR,
                     only=True)
        same = ptr
        f_same = cand(pins=pins_of(ptr, same))
        must_fail_at('mock-s1 with the predicted tree\'s first run offered as its replay run', 'P',
                     mock(f_same, frun_in(f_same), extra_ev=((RUN_EVIDENCE, ptr), (REPLAY_EVIDENCE, same))), A_REP,
                     only=True)
        rep_same = derive_run(replay_log(P), meta(replay_log(P)), *synth_api(P, jobs_p)).encode()
        f_rs = cand(pins=pins_of(ptr, rep_same))
        must_fail_at('mock-s1 with a replay run result that names the first run\'s run id', 'P',
                     mock(f_rs, frun_in(f_rs), extra_ev=((RUN_EVIDENCE, ptr), (REPLAY_EVIDENCE, rep_same))), A_REP,
                     only=True)
        fresh2 = derive_run(ml(P), meta(ml(P)), *synth_api(P, jobs_p, run_id=4243)).encode()
        f_fresh = cand(pins=pins_of(ptr, fresh2))
        must_fail_at('mock-s1 with a second run that built the module fresh (no cache restored)', 'P',
                     mock(f_fresh, frun_in(f_fresh), extra_ev=((RUN_EVIDENCE, ptr), (REPLAY_EVIDENCE, fresh2))), A_REP,
                     only=True)

def main(argv):
    if argv == ['--self-test']:
        self_test()
    elif len(argv) == 2 and argv[0] == 'axioms':
        try:
            text = read_log(argv[1]) if os.path.isfile(argv[1]) else ''
        except OSError:
            text = ''
        rows = axioms_gate(text)
        for label, ok, detail in rows:
            print('%s axioms: %s%s' % ('PASS' if ok else 'FAIL', label, ('  ' + detail) if detail else ''))
        bad = [label for label, ok, _ in rows if not ok]
        print(STEP_OK if not bad else 'ktrans_sep2 axioms: FAILED (%d check(s))' % len(bad))
        return 1 if bad else 0
    elif argv[:1] == ['derive-run']:
        opts = dict(zip(argv[1::2], argv[2::2]))
        if len(argv) != 9 or set(opts) != {'--log', '--log-meta', '--run-api', '--jobs-api'}:
            print(__doc__)
            return 2
        rd = lambda k: open(opts[k], 'rb').read()
        sys.stdout.write(derive_run(rd('--log'), json.loads(rd('--log-meta')), rd('--run-api'), rd('--jobs-api')))
        return 0
    elif len(argv) >= 14 and argv[0] == 'mock-s1' and len(argv) % 2 == 0:
        pairs = list(zip(argv[2::2], argv[3::2]))
        opts = {k: v for k, v in pairs if k != '--evidence'}
        extra = [tuple(v.split('=', 1)) for k, v in pairs if k == '--evidence' and '=' in v]
        if len(opts) != sum(k != '--evidence' for k, _ in pairs) or \
                set(opts) != {'--f-run', '--predicted', '--log', '--log-meta', '--run-api', '--jobs-api'} or \
                len(extra) != sum(k == '--evidence' for k, _ in pairs):
            print(__doc__)
            return 2
        rd = lambda p: open(p, 'rb').read()
        mock_s1(argv[1], rd(opts['--f-run']), opts['--predicted'], [(r, rd(p)) for r, p in extra], rd(opts['--log']),
                json.loads(rd(opts['--log-meta'])), rd(opts['--run-api']), rd(opts['--jobs-api']))
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
                log = read_log(opts['--log'])
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
