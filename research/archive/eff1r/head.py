#!/usr/bin/env python3
"""controls.py -- round EFF-1's own contracts, FROZEN with the preregistration beside it.

Imports nothing from the repository and changes nothing. Reads D and the commit under check through git, and embeds
every frozen text it compares against.

  controls.py check <commit> [--freeze F]   the execution at <commit> against D (and, with F, the preregistration
                                            unchanged from F, and F = D plus the preregistration alone)
  controls.py --self-test                   the frozen surfaces against the reference module; mutation controls that
                                            must fail with their named codes
  controls.py verdict <commit>              the two verdicts computed from the module's statements at <commit>

Checks (each prints PASS or FAIL with its code):
  P   paths       delta(D, commit) is exactly the governed execution paths plus the record directory
  N1  decls       the module declares exactly the frozen declarations, in order, with their kinds
  N2  statements  every theorem statement (signature up to `:=`) is the frozen text; every definition is the frozen
                  text whole; the preamble and every context block is the frozen text, in order -- a proof may change,
                  a statement, definition or binder context may not
  N3  hygiene     no sorry, admit, axiom declaration or native_decide; every frozen `#print axioms` line present
  S1  cone        the two inclusions of Q-CONE are theorems with their frozen statements; the equality is proved from
                  both by name; `cone_of_orbit` and `sharpFamily_subset_avail` carry exactly OG-1's four hypotheses
                  (and `0 < d` for the former), with no unit, mixing or effect premise
  S2  set         the upper bound in both directions, the decomposition in both directions with the equality proved
                  from both by name, `fullEffects_subset_avail` with exactly OG-1's four hypotheses, the unit and
                  `MixingClosed`, and the countermodel `not_fullEffects_of_orbit` with its frozen conclusion
  S3  definitions `maxConeOf`, `MixingClosed`, `EffectsOn`, `unitSpan`, `sharpFamily` are the frozen texts whole;
                  `maxConeOf` quantifies over the family it is given and nothing else
  S4  premises    no theorem concludes `SharpSeed`, `PreservesBody`, `BoundaryTransitive`, `SeedOrbitAvailable`,
                  `MixingClosed` or `EffectsOn` of a hypothesis-bound family, map or seed; those predicates are concluded
                  only of the named witnesses (`fullAut d`, `sharpEff`, `sharpUnitFamily d`) by the named control
                  theorems and the verdict; `MixingClosed` is never concluded positively
  S5  reuse       no declaration shares a name with a landed object it reads; every import is
                  `OIBridge.CompositeDimension`, `OIBridge.CompositeInterface` or a Mathlib module
  S6  neutral     no complex, matrix-trace, qubit, Bloch, Pauli, density, drive, flow or limit-closure token
  S7  phrases     the module header (and, at a commit carrying it, the result note) contains none of the frozen phrases
  S8  dimension   `0 < d` occurs in exactly the frozen set of statements; outside the control section and the verdict no
                  numeral 3 occurs
  S9  count       exactly the frozen `#print axioms` lines, in order, distinct, each naming a declaration of the module
  V   verdicts    each question's verdict is computed from the module's statements by the frozen rule, and exactly one
                  outcome holds per question; at a commit carrying the result note, the note states exactly the
                  computed verdicts and no other outcome token
  I   imports     OIBridge.lean is D's with exactly the frozen import line after `import OIBridge.CompositeDimension`
  C   census      the census is D's with exactly the frozen family inserted after the DIM-1 family, byte for byte
  F   freeze      (with --freeze) the preregistration at the commit equals F's, and delta(D, F) is the preregistration
"""
import io, json, re, subprocess, sys

D = '@@D@@'
RDIR = 'verification/programmes/oi-qm/reconstruction/round-eff-1-effect-space/'
PREREG = RDIR + 'preregistration.md'
RESULT = RDIR + 'result.md'
MOD = 'verification/lean-mathlib/OIBridge/EffectSpace.lean'
IMPORTS = 'verification/lean-mathlib/OIBridge.lean'
CENSUS = 'verification/lean-manuscript-census.json'
GOVERNED = {MOD: 'A', IMPORTS: 'M', CENSUS: 'M'}
RECORD_FILES = {RDIR + 'preregistration.md', RDIR + 'controls.py', RDIR + 'result.md'}
MOD_REFERENCE_BLOB = '@@BLOB@@'
ANCHOR_IMPORT = 'import OIBridge.CompositeDimension\n'
NEW_IMPORT = 'import OIBridge.EffectSpace\n'
PREV_FAMILY_MODULES = ['CompositeDimension']
CENSUS_FAMILY = json.loads(r'''@@CENSUS_FAMILY@@''')
DECLS = json.loads(r'''@@DECLS@@''')
TEXTS = json.loads(r'''@@TEXTS@@''')
PRINTS = json.loads(r'''@@PRINTS@@''')
PREAMBLE = json.loads(r'''@@PREAMBLE@@''')
CONTEXT = json.loads(r'''@@CONTEXT@@''')
N_PRINTS = @@NPRINTS@@

