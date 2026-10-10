#!/usr/bin/env python3
"""controls.py -- round ODD-CHAR-1's own contracts, FROZEN with the preregistration beside it.

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
  L   landed      the landed texts the rules read, read from D, are the frozen ones
  N1  decls       the module declares exactly the frozen declarations, in order, with their kinds
  N2  statements  every theorem statement (signature up to `:=`) is the frozen text; every definition is the frozen
                  text whole; the preamble and every context block is the frozen text, in order -- a proof may change,
                  a statement, definition or binder context may not
  N3  hygiene     no sorry, admit, axiom declaration or native_decide; every frozen `#print axioms` line present
  S1  family      the family definitions are the frozen ones; for every `k`, `nK k` is a NOT of `eball (2k+1)` with
                  axis `zK k`, `gRev k` satisfies the landed `NativeGate` frame field read from D at the gate and the
                  axis, and `GateRel (nK k) (gRev k)` holds through the landed `sgate_relT` and `sgate_relC`; the landed
                  `GateRel` fields are the landed `NativeGate` relation fields; no declaration of §A mentions the native
                  gate or positivity
  S2  odd         the characterization's statement is the frozen existential -- `IsNot`, the landed frame field and
                  `GateRel` -- equivalent to `Odd d`; its proof reads the landed `not_even_of_gateRel`, the landed
                  `d = 1` objects `cnot1`, `isNot_neg1` and `cnot1_frame` with the landed relations of `cnot1`, and the
                  family; the landed statements it reads are the frozen ones; §B mentions neither the native gate nor
                  positivity
  S3  positivity  for `k ≥ 1`: the witness definitions are the frozen ones; the image of the frozen product pairs to
                  `-1 / 10` with the two frozen sharp effects; the forward-positivity failure is the negation of the
                  landed `posFwd` field at the body and the gate, proved through that value; the gate is the family's,
                  with its frame and its relations; no declaration of §C names a landed dimension corollary of the
                  native gate or inverse positivity
  S6  scope       no declaration mentions a complex field, a landed dimension selector, inverse positivity or
                  `Entangling`; no theorem concludes an equation or inequation on `d`; no theorem concludes the native
                  gate, the maximal cone or forward positivity without negation
  S7  reuse       no declaration of the module shares its name with an OIBridge declaration visible to it; the only
                  import is `OIBridge.ParityNot`
  S8  phrases     the module header (and, at a commit carrying it, the result note) contains none of the frozen phrases
  S9  count       exactly the frozen `#print axioms` lines, in order, distinct, each naming a declaration of the module
  V   verdicts    each cell is computed from the module's statements and the landed statements at D by its own frozen
                  rule, independently of the others; at a commit carrying the result note, the note states exactly the
                  computed tokens and no other
  I   imports     OIBridge.lean is D's with exactly the frozen import line after `import OIBridge.ParityNot`
  C   census      the census is D's with exactly the frozen family inserted after the PARITY-NOT-1 family, byte for
                  byte
  F   freeze      (with --freeze) the preregistration at the commit equals F's, and delta(D, F) is the preregistration
"""
import io, json, re, subprocess, sys

D = '@@D@@'
RDIR = 'verification/programmes/oi-qm/reconstruction/round-odd-char-1/'
PREREG = RDIR + 'preregistration.md'
RESULT = RDIR + 'result.md'
LEAN = 'verification/lean-mathlib/OIBridge/'
MOD = LEAN + 'OddChar.lean'
IMPORTS = 'verification/lean-mathlib/OIBridge.lean'
CENSUS = 'verification/lean-manuscript-census.json'
GOVERNED = {MOD: 'A', IMPORTS: 'M', CENSUS: 'M'}
RECORD_FILES = {RDIR + 'preregistration.md', RDIR + 'controls.py', RDIR + 'result.md'}
MOD_REFERENCE_BLOB = '@@BLOB@@'
ANCHOR_IMPORT = 'import OIBridge.ParityNot\n'
NEW_IMPORT = 'import OIBridge.OddChar\n'
PREV_FAMILY_MODULES = ['ParityNot']
CENSUS_FAMILY = json.loads(r'''@@CENSUS_FAMILY@@''')
DECLS = json.loads(r'''@@DECLS@@''')
TEXTS = json.loads(r'''@@TEXTS@@''')
PRINTS = json.loads(r'''@@PRINTS@@''')
PREAMBLE = json.loads(r'''@@PREAMBLE@@''')
CONTEXT = json.loads(r'''@@CONTEXT@@''')
LANDED = json.loads(r'''@@LANDED@@''')
N_PRINTS = @@NPRINTS@@
