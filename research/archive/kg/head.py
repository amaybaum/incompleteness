#!/usr/bin/env python3
"""controls.py -- round K2-GUARD-1's own contracts, FROZEN with the preregistration beside it.

Imports nothing from the repository and changes nothing. Reads D and the commit under check through git, and embeds
every frozen text it compares against.

  controls.py check <commit> [--freeze F]   the execution at <commit> against D (and, with F, the preregistration
                                            unchanged from F, and F = D plus the preregistration alone)
  controls.py --self-test                   the frozen surfaces against the reference module; mutation controls that
                                            must fail with their named codes
  controls.py verdict <commit>              the two cells computed from the module's statements at <commit>

Checks (each prints PASS or FAIL with its code):
  P   paths       delta(D, commit) is exactly the governed execution paths plus the record directory
  N1  decls       the module declares exactly the frozen declarations, in order, with their kinds
  N2  statements  every theorem statement (signature up to `:=`) is the frozen text; every definition is the frozen
                  text whole; the preamble and every context block is the frozen text, in order -- a proof may change,
                  a statement, definition or binder context may not
  N3  hygiene     no sorry, admit, axiom declaration or native_decide; every frozen `#print axioms` line present
  S1  obstruction `reflY`, `CandidateCone`, `productSet`, `cnotOrbit` are the frozen texts whole; the obstruction theorem
                  has exactly the frozen binders and conclusion `False`, and its proof names `chain_eq` and `chain_value`
  S2  controls    the orientation controls are theorems with their frozen conclusions and prints: the native gate, the
                  ball map and the two determinants, the two non-vacuity families, the chain value and the rotation
                  value
  S3  selectors   the two `2 ≤ d` selectors have exactly the frozen explicit binders and conclusion `d = 3`, their proofs
                  name `dim_of_nativeGate` / `dim_of_nativeGateOf`, and neither statement mentions `Entangling`;
                  `two_le_of_entangling` concludes `2 ≤ d` from the entangling clause and nothing else does
  S4  premises    no theorem concludes `Entangling`, `NativeGateOf`, `EffectsOn`, `SharpSeed`, `PreservesBody`,
                  `BoundaryTransitive` or `SeedOrbitAvailable`; `NativeGate`, `IsNot` and `CandidateCone` are concluded
                  only of the named witnesses by the named control theorems and the verdicts
  S5  reuse       no declaration shares a name with a landed object it reads; the only import is `OIBridge.K1Bridge`
  S6  neutral     no complex, conjugate-transpose, positive-semidefinite, trace, qubit, Bloch, Pauli, density, drive,
                  flow, limit, closure, density-of-subgroup, tensor-product or Hilbert token
  S7  phrases     the module header (and, at a commit carrying it, the result note) contains none of the frozen phrases
  S8  scope       the selector section (§E) mentions no dimension-three object; `2 ≤ d` occurs only in §E, §F and the
                  verdicts
  S9  count       exactly the frozen `#print axioms` lines, in order, distinct, each naming a declaration of the module
  V   verdicts    each cell is computed from the module's statements by its own frozen rule, independently of the
                  other; at a commit carrying the result note, the note states exactly the computed tokens and no other
  I   imports     OIBridge.lean is D's with exactly the frozen import line after `import OIBridge.K1Bridge`
  C   census      the census is D's with exactly the frozen family inserted after the K1-BRIDGE-1 family, byte for byte
  F   freeze      (with --freeze) the preregistration at the commit equals F's, and delta(D, F) is the preregistration
"""
import io, json, re, subprocess, sys

D = '@@D@@'
RDIR = 'verification/programmes/oi-qm/reconstruction/round-k2-guard-1-interface/'
PREREG = RDIR + 'preregistration.md'
RESULT = RDIR + 'result.md'
MOD = 'verification/lean-mathlib/OIBridge/K2Guard.lean'
IMPORTS = 'verification/lean-mathlib/OIBridge.lean'
CENSUS = 'verification/lean-manuscript-census.json'
GOVERNED = {MOD: 'A', IMPORTS: 'M', CENSUS: 'M'}
RECORD_FILES = {RDIR + 'preregistration.md', RDIR + 'controls.py', RDIR + 'result.md'}
MOD_REFERENCE_BLOB = '@@BLOB@@'
ANCHOR_IMPORT = 'import OIBridge.K1Bridge\n'
NEW_IMPORT = 'import OIBridge.K2Guard\n'
PREV_FAMILY_MODULES = ['K1Bridge']
CENSUS_FAMILY = json.loads(r'''@@CENSUS_FAMILY@@''')
DECLS = json.loads(r'''@@DECLS@@''')
TEXTS = json.loads(r'''@@TEXTS@@''')
PRINTS = json.loads(r'''@@PRINTS@@''')
PREAMBLE = json.loads(r'''@@PREAMBLE@@''')
CONTEXT = json.loads(r'''@@CONTEXT@@''')
N_PRINTS = @@NPRINTS@@

