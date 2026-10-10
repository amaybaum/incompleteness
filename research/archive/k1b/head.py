#!/usr/bin/env python3
"""controls.py -- round K1-BRIDGE-1's own contracts, FROZEN with the preregistration beside it.

Imports nothing from the repository and changes nothing. Reads D and the commit under check through git, and embeds
every frozen text it compares against.

  controls.py check <commit> [--freeze F]   the execution at <commit> against D (and, with F, the preregistration
                                            unchanged from F, and F = D plus the preregistration alone)
  controls.py --self-test                   the frozen surfaces against the reference module; mutation controls that
                                            must fail with their named codes
  controls.py verdict <commit>              the verdict computed from the module's statements at <commit>

Checks (each prints PASS or FAIL with its code):
  P   paths       delta(D, commit) is exactly the governed execution paths plus the record directory
  N1  decls       the module declares exactly the frozen declarations, in order, with their kinds
  N2  statements  every theorem statement (signature up to `:=`) is the frozen text; every definition and structure
                  is the frozen text whole; the preamble and every context block is the frozen text, in order -- a
                  proof may change, a statement, definition or binder context may not
  N3  hygiene     no sorry, admit, axiom declaration or native_decide; every frozen `#print axioms` line present
  S1  relative    `NativeGateOf` is DIM-1's `NativeGate` with `maxConeOf avail` in exactly the two positivity clauses
                  and the frame and the two NOT relations unchanged; `jointStatesOf` and `EntanglingOf` are DIM-1's
                  `jointStates` and `Entangling` with the family's cone; the three are the frozen texts whole
  S2  selectors   `dim_of_nativeGateOf` and `three_of_nativeGateOf` are theorems whose explicit binders are exactly
                  `0 < d`, effect soundness, the four hypotheses, `IsNot` and `NativeGateOf` (and `EntanglingOf` for
                  the second), with the frozen conclusions, and no `MixingClosed`, `unitEff`, `fullEffects` or
                  `sharpFamily` token in their statements
  S3  transparent each selector's proof names EFF-1's `maxConeOf_avail_eq` (through `nativeGate_of_avail`) and DIM-1's
                  landed selector by name; no declaration of the module mentions an eigenspace, a parity, a finrank,
                  a block, a tangent or a corner slice: no new dimension argument
  S4  premises    no theorem concludes `SharpSeed`, `PreservesBody`, `BoundaryTransitive`, `SeedOrbitAvailable`,
                  `EffectsOn`, `IsNot`, `NativeGateOf`, `EntanglingOf` or `MixingClosed` of a hypothesis-bound object;
                  `EffectsOn` is concluded only of the named control family `axisFamily` by `cone_eq_fails_axis` and
                  the verdict; `NativeGate` and `Entangling` are concluded only from `NativeGateOf` and `EntanglingOf`
  S5  reuse       no declaration shares a name with a landed object it reads; the only import is `OIBridge.EffectSpace`
  S6  neutral     no complex, matrix-trace, qubit, Bloch, Pauli, density, drive, flow, limit-closure or tensor-product
                  token; no `MixingClosed` or `unitSpan` token anywhere in the module's code
  S7  phrases     the module header (and, at a commit carrying it, the result note) contains none of the frozen phrases
  S8  dimension   `0 < d` occurs in exactly the frozen set of statements; outside the control section and the verdict
                  no dimension-three object occurs
  S9  count       exactly the frozen `#print axioms` lines, in order, distinct, each naming a declaration of the module
  V   verdict     the verdict is computed from the module's statements by the frozen rule; at a commit carrying the
                  result note, the note states exactly the computed outcome token and no other
  I   imports     OIBridge.lean is D's with exactly the frozen import line after `import OIBridge.EffectSpace`
  C   census      the census is D's with exactly the frozen family inserted after the EFF-1 family, byte for byte
  F   freeze      (with --freeze) the preregistration at the commit equals F's, and delta(D, F) is the preregistration
"""
import io, json, re, subprocess, sys

D = '@@D@@'
RDIR = 'verification/programmes/oi-qm/reconstruction/round-k1-bridge-1-effect-availability/'
PREREG = RDIR + 'preregistration.md'
RESULT = RDIR + 'result.md'
MOD = 'verification/lean-mathlib/OIBridge/K1Bridge.lean'
IMPORTS = 'verification/lean-mathlib/OIBridge.lean'
CENSUS = 'verification/lean-manuscript-census.json'
GOVERNED = {MOD: 'A', IMPORTS: 'M', CENSUS: 'M'}
RECORD_FILES = {RDIR + 'preregistration.md', RDIR + 'controls.py', RDIR + 'result.md'}
MOD_REFERENCE_BLOB = '@@BLOB@@'
ANCHOR_IMPORT = 'import OIBridge.EffectSpace\n'
NEW_IMPORT = 'import OIBridge.K1Bridge\n'
PREV_FAMILY_MODULES = ['EffectSpace']
CENSUS_FAMILY = json.loads(r'''@@CENSUS_FAMILY@@''')
DECLS = json.loads(r'''@@DECLS@@''')
TEXTS = json.loads(r'''@@TEXTS@@''')
PRINTS = json.loads(r'''@@PRINTS@@''')
PREAMBLE = json.loads(r'''@@PREAMBLE@@''')
CONTEXT = json.loads(r'''@@CONTEXT@@''')
N_PRINTS = @@NPRINTS@@
# DIM-1's `NativeGate` and `Entangling` at D, the texts the relative forms are compared against (S1)
DIM1_NATIVEGATE = json.loads(r'''@@DIM1_NATIVEGATE@@''')
DIM1_ENTANGLING = json.loads(r'''@@DIM1_ENTANGLING@@''')
DIM1_JOINTSTATES = json.loads(r'''@@DIM1_JOINTSTATES@@''')

