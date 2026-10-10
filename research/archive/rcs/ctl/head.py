#!/usr/bin/env python3
"""controls.py -- round RELC-SELECT-1's own contracts, FROZEN with the preregistration beside it.

Imports nothing from the repository and changes nothing. Reads D and the commit under check through git, and embeds
every frozen text it compares against.

  controls.py check <commit> [--freeze F]   the execution at <commit> against D (and, with F, the preregistration
                                            unchanged from F, and F = D plus the preregistration alone)
  controls.py --self-test                   the frozen surfaces against the reference modules; mutation controls that
                                            must fail with their named codes
  controls.py verdict <commit>              the four cells computed from the modules' statements at <commit> and the
                                            landed statements at D

Checks (each prints PASS or FAIL with its code):
  P   paths       delta(D, commit) is exactly the governed execution paths plus the record directory
  L   landed      the landed texts the rules read, read from D, are the frozen ones
  N1  decls       each module declares exactly its frozen declarations, in order, with their kinds
  N2  statements  every theorem statement (signature up to `:=`) is the frozen text; every definition and structure
                  is the frozen text whole; the preamble and every context block is the frozen text, in order -- a
                  proof may change, a statement, definition or binder context may not
  N3  hygiene     no sorry, admit, axiom declaration or native_decide; every frozen `#print axioms` line present
  S1  parity      (RelcSelectParity) from `IsNot (eball d) z N` and the landed `relC` field alone, the two eigenspaces
                  of the homogenized NOT have equal dimension and `d` is not even; the module reads neither `relT`, the
                  frame, positivity, `GateRel` nor any landed statement over `NativeGate`
  S2  selector    (RelcSelectBlock) `CtrlGate` is the landed `NativeGate` with its `relT` field removed, field for
                  field; `IsNot` and `CtrlGate` give the landed selector's conclusion `d = 1 ∨ d = 3`, and with the
                  landed `Entangling` clause `d = 3` through the frame-only exclusion of `d = 1`; every copied
                  declaration is the landed one under the frozen renaming, except the two frozen line edits; the
                  parity step is S1's theorem; nothing in the module or in the parity module reads `relT`
  S3  positivity  (RelcSelectSqueeze) at `d = 5` with the landed `n5` and `z5`: `gSq` has the landed frame, `GateRel`
                  and the landed `posFwd` field and fails the landed `posInv` field through the value `-1 / 2`;
                  `gSq.symm` has the frame, `GateRel`, the landed `posInv` field (stated through
                  `gSq.symm.symm = gSq`) and fails the landed `posFwd` field; the transfer of `relC` to the inverse
                  takes `relT`
  S4  relation    (RelcSelectC5) at `d = 5` with the witness NOT `nC5` and the landed `z5`: `gC5` has the landed
                  frame, `relT`, `posFwd` and `posInv` fields and fails the landed `relC` field, so `IsNot` and those
                  four fields do not give the landed selector's conclusion
  S6  scope       no declaration mentions a complex field or a landed dimension selector of the native gate; only the
                  frozen selector theorems conclude an equation on `d`; no theorem concludes the native gate
  S7  reuse       no declaration shares its name with an OIBridge declaration visible to it or with a declaration of
                  another module of the round; each module's imports are the frozen ones
  S8  phrases     the comments of each module (and, at a commit carrying it, the result note less the frozen earned
                  reading and the frozen non-inference rule) contain none of the frozen phrases
  S9  count       exactly the frozen `#print axioms` lines of each module, in order, distinct, each naming a
                  declaration of that module
  V   verdicts    each cell is computed from the modules' statements and the landed statements at D by its own frozen
                  rule; at a commit carrying the result note, the note states exactly the computed tokens and no
                  other, states the frozen earned reading exactly when all four cells are proved, and states the
                  frozen non-inference rule
  I   imports     OIBridge.lean is D's with exactly the four frozen import lines after `import OIBridge.OddChar`
  C   census      the census is D's with exactly the frozen family inserted after the ODD-CHAR-1 family, byte for byte
  F   freeze      (with --freeze) the preregistration at the commit equals F's, and delta(D, F) is the preregistration
"""
import hashlib, io, json, re, subprocess, sys

D = '@@D@@'
RDIR = 'verification/programmes/oi-qm/reconstruction/round-relc-select-1/'
PREREG = RDIR + 'preregistration.md'
RESULT = RDIR + 'result.md'
LEAN = 'verification/lean-mathlib/OIBridge/'
MODULES = ['RelcSelectParity', 'RelcSelectBlock', 'RelcSelectSqueeze', 'RelcSelectC5']
MODPATH = {m: LEAN + m + '.lean' for m in MODULES}
IMPORTS = 'verification/lean-mathlib/OIBridge.lean'
CENSUS = 'verification/lean-manuscript-census.json'
GOVERNED = dict([(MODPATH[m], 'A') for m in MODULES] + [(IMPORTS, 'M'), (CENSUS, 'M')])
RECORD_FILES = {RDIR + 'preregistration.md', RDIR + 'controls.py', RDIR + 'result.md'}
MOD_REFERENCE_BLOBS = json.loads(r'''@@BLOBS@@''')
ANCHOR_IMPORT = 'import OIBridge.OddChar\n'
NEW_IMPORTS = ''.join('import OIBridge.%s\n' % m for m in MODULES)
PREV_FAMILY_MODULES = ['OddChar']
CENSUS_FAMILY = json.loads(r'''@@CENSUS_FAMILY@@''')
DECLS = json.loads(r'''@@DECLS@@''')
TEXTS = json.loads(r'''@@TEXTS@@''')
PRINTS = json.loads(r'''@@PRINTS@@''')
PREAMBLE = json.loads(r'''@@PREAMBLE@@''')
CONTEXT = json.loads(r'''@@CONTEXT@@''')
LANDED = json.loads(r'''@@LANDED@@''')
N_PRINTS = json.loads(r'''@@NPRINTS@@''')
EARNED = json.loads(r'''@@EARNED@@''')
NONINF = json.loads(r'''@@NONINF@@''')
