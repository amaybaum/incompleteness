#!/usr/bin/env python3
"""controls.py -- round K1-SHARP-TESTS-1's own contracts, FROZEN with the preregistration beside it.

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
  S1  predicate   `HasTwoSharpTests` is the frozen definition whole: two sharp seeds, each separated on a state of the
                  body from the other and from its complement
  S2  classified  the classification theorems have exactly the frozen explicit binders and conclusions and their
                  prints; the seed classification names `sharp_eq_of_certain`; the equivalence names its three
                  directional witnesses (the d = 0 case, the d = 1 case, the axis witness); the cell's verdict has its
                  frozen conclusion
  S3  not implied the d = 1 control and the non-implication have their frozen conclusions; the non-implication's chain of
                  hypotheses is, type for type and in order, the explicit hypotheses other than `2 ≤ d` of the landed
                  relative selector `three_of_nativeGateOf_of_two_le` read from D, and its proof names the control
  S4  scope       no declaration mentions `Entangling` or `EntanglingOf`; `HasTwoSharpTests` is applied in a theorem only
                  to `eball _`; no theorem concludes `2 ≤ d` alone
  S5  reuse       no declaration shares a name with a landed object it reads; the only import is `OIBridge.K1Bridge`
  S6  neutral     no complex, conjugate-transpose, positive-semidefinite, qubit, Bloch, Pauli, density, flow, limit,
                  closure, density-of-subgroup, tensor-product or Hilbert token
  S7  phrases     the module header (and, at a commit carrying it, the result note) contains none of the frozen phrases
  S8  separation  §A-§C and the classification verdict mention none of the selector's objects; §D and the
                  non-implication verdict do not mention `HasTwoSharpTests`; `2 ≤ d` occurs only in §C, §D and the
                  verdicts
  S9  count       exactly the frozen `#print axioms` lines, in order, distinct, each naming a declaration of the module
  V   verdicts    each cell is computed from the module's statements by its own frozen rule, independently of the
                  other; at a commit carrying the result note, the note states exactly the computed tokens and no other
  I   imports     OIBridge.lean is D's with exactly the frozen import line after `import OIBridge.K2Guard`
  C   census      the census is D's with exactly the frozen family inserted after the K2-GUARD-1 family, byte for byte
  F   freeze      (with --freeze) the preregistration at the commit equals F's, and delta(D, F) is the preregistration
"""
import io, json, re, subprocess, sys

D = '@@D@@'
RDIR = 'verification/programmes/oi-qm/reconstruction/round-k1-sharp-tests-1/'
PREREG = RDIR + 'preregistration.md'
RESULT = RDIR + 'result.md'
MOD = 'verification/lean-mathlib/OIBridge/SharpTests.lean'
IMPORTS = 'verification/lean-mathlib/OIBridge.lean'
CENSUS = 'verification/lean-manuscript-census.json'
SELECTOR_SRC = 'verification/lean-mathlib/OIBridge/K2Guard.lean'
SELECTOR_NAME = 'three_of_nativeGateOf_of_two_le'
GOVERNED = {MOD: 'A', IMPORTS: 'M', CENSUS: 'M'}
RECORD_FILES = {RDIR + 'preregistration.md', RDIR + 'controls.py', RDIR + 'result.md'}
MOD_REFERENCE_BLOB = '@@BLOB@@'
ANCHOR_IMPORT = 'import OIBridge.K2Guard\n'
NEW_IMPORT = 'import OIBridge.SharpTests\n'
PREV_FAMILY_MODULES = ['K2Guard']
CENSUS_FAMILY = json.loads(r'''@@CENSUS_FAMILY@@''')
DECLS = json.loads(r'''@@DECLS@@''')
TEXTS = json.loads(r'''@@TEXTS@@''')
PRINTS = json.loads(r'''@@PRINTS@@''')
PREAMBLE = json.loads(r'''@@PREAMBLE@@''')
CONTEXT = json.loads(r'''@@CONTEXT@@''')
SEL_TYPES = json.loads(r'''@@SELTYPES@@''')
N_PRINTS = @@NPRINTS@@
