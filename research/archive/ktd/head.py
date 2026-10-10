#!/usr/bin/env python3
"""controls.py -- round KTRANS-DENSE-1's own contracts, FROZEN with the preregistration beside it.

Imports nothing from the repository and changes nothing. Reads D and the commit under check through git, and embeds
every frozen text it compares against.

  controls.py check <commit> [--freeze F]   the execution at <commit> against D (and, with F, the preregistration
                                            unchanged from F, and F = D plus the preregistration alone)
  controls.py --self-test                   the frozen surfaces against the reference module; mutation controls that
                                            must fail with their named codes
  controls.py verdict <commit>              the three cells computed from the module's statements at <commit> and the
                                            landed statements at D

Checks (each prints PASS or FAIL with its code):
  P   paths       delta(D, commit) is exactly the governed execution paths plus the record directory
  N1  decls       the module declares exactly the frozen declarations, in order, with their kinds
  N2  statements  every theorem statement (signature up to `:=`) is the frozen text; every definition is the frozen
                  text whole; the preamble and every context block is the frozen text, in order -- a proof may change,
                  a statement, definition or binder context may not
  N3  hygiene     no sorry, admit, axiom declaration or native_decide; every frozen `#print axioms` line present
  S1  definition  `DenseBoundaryOrbit` has the effective header of the landed `BoundaryTransitive` read from D and the
                  same body with exactly its last clause `∃ g ∈ G, g x = y` replaced by membership of `y` in the
                  closure of the orbit `(fun g => g x) '' G`
  S2  pairing     for each of the eleven frozen pairs, the landed theorem read from D has exactly one
                  `BoundaryTransitive` in its effective statement (its section variables that the statement uses,
                  then its own binders and conclusion), and the dense theorem's effective statement is that text with
                  `BoundaryTransitive` replaced by `DenseBoundaryOrbit` and nothing else; the dense statement does not
                  mention `BoundaryTransitive`
  S3  resolution  every identifier of a paired effective statement that names an OIBridge declaration resolves, in
                  the dense module's namespace context, to the same unique declaration as in the landed module's
                  context (inventory read from D and the module under check)
  S4  strict      the weakening `denseBoundaryOrbit_of_boundaryTransitive` and the strictness witness have their
                  frozen binders and conclusions; `ratRefl` is the frozen definition; the non-transitivity is proved
                  through EFF-1's `not_boundaryTransitive_of_countable`, read from D with its frozen statement
  S5  scope       no statement mentions an exact-existence or uncovered object (the sharp family, the full effect set,
                  the mixing closure, supporting-effect completeness, K-infinity-1, the Lorentz bridge, extreme points);
                  `ratRefl` occurs only in §D
  S6  reuse       no declaration of the module shares its name with an OIBridge declaration visible to it; the only
                  import is `OIBridge.K2Guard`
  S7  phrases     the module header (and, at a commit carrying it, the result note) contains none of the frozen phrases
  S8  separation  no declaration of §B mentions a cone or selector object; no declaration of §B or §C mentions
                  `ratRefl`
  S9  count       exactly the frozen `#print axioms` lines, in order, distinct, each naming a declaration of the module
  V   verdicts    each cell is computed from the module's statements and the landed statements at D by its own frozen
                  rule, independently of the others; at a commit carrying the result note, the note states exactly the
                  computed tokens and no other
  I   imports     OIBridge.lean is D's with exactly the frozen import line after `import OIBridge.SharpTests`
  C   census      the census is D's with exactly the frozen family inserted after the K1-SHARP-TESTS-1 family, byte for
                  byte
  F   freeze      (with --freeze) the preregistration at the commit equals F's, and delta(D, F) is the preregistration
"""
import io, json, re, subprocess, sys

D = '@@D@@'
RDIR = 'verification/programmes/oi-qm/reconstruction/round-ktrans-dense-1/'
PREREG = RDIR + 'preregistration.md'
RESULT = RDIR + 'result.md'
LEAN = 'verification/lean-mathlib/OIBridge/'
MOD = LEAN + 'DenseOrbit.lean'
IMPORTS = 'verification/lean-mathlib/OIBridge.lean'
CENSUS = 'verification/lean-manuscript-census.json'
GOVERNED = {MOD: 'A', IMPORTS: 'M', CENSUS: 'M'}
RECORD_FILES = {RDIR + 'preregistration.md', RDIR + 'controls.py', RDIR + 'result.md'}
MOD_REFERENCE_BLOB = '@@BLOB@@'
ANCHOR_IMPORT = 'import OIBridge.SharpTests\n'
NEW_IMPORT = 'import OIBridge.DenseOrbit\n'
PREV_FAMILY_MODULES = ['SharpTests']
CENSUS_FAMILY = json.loads(r'''@@CENSUS_FAMILY@@''')
DECLS = json.loads(r'''@@DECLS@@''')
TEXTS = json.loads(r'''@@TEXTS@@''')
PRINTS = json.loads(r'''@@PRINTS@@''')
PREAMBLE = json.loads(r'''@@PREAMBLE@@''')
CONTEXT = json.loads(r'''@@CONTEXT@@''')
LANDED = json.loads(r'''@@LANDED@@''')
N_PRINTS = @@NPRINTS@@
DECL = re.compile(r'^(?:@\[[^\]\n]*\]\s+)?(theorem|lemma|def|noncomputable def|abbrev|noncomputable abbrev|structure'
                  r'|instance)\s+(\S+)', re.M)
CTX = re.compile(r'^(variable|open|namespace|section|end|attribute|universe|set_option|noncomputable section)\b.*$',
                 re.M)
FAILS, COUNT = [], [0]
