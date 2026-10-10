#!/usr/bin/env python3
"""controls.py -- round PARITY-NOT-1's own contracts, FROZEN with the preregistration beside it.

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
  S1  relations   `GateRel` is a structure with exactly the two fields `relT` and `relC`, each the landed
                  `NativeGate` field read from D, and the frozen header
  S2  parity      each of the two parity theorems is its landed `NativeGate` partner read from D with the hypothesis
                  `(hG : NativeGate (eball d) z N G)` replaced by `(hR : GateRel N G)` and nothing else; every
                  OIBridge identifier of the pair resolves to the same unique declaration in both contexts; no
                  declaration of §A except `gateRel_of_nativeGate` mentions the native gate, the frame or positivity
  S3  the NOT     the four `d = 3` theorems take exactly `IsNot (eball 3) z N` and `GateRel N G` and have their frozen
                  conclusions; no declaration of §B except the three `NativeGate` corollaries mentions the native gate,
                  the frame or positivity, and each corollary is its `GateRel` theorem with the hypothesis
                  `(hG : NativeGate (eball 3) z N G)` and is proved through `gateRel_of_nativeGate`
  S4  controls    `refl3` and `negId3` are the frozen diagonal maps, NOTs of `eball 3` with axis `z3`, of
                  determinant `-1`, for which no gate satisfies the relations; `cnot` with `nflip` satisfies them,
                  through the landed `cnot_relT` and `cnot_relC` read from D
  S5  separation  for `d = 3` and `d = 5`: the gate and the witness are the frozen definitions; the frame theorem is the
                  landed `NativeGate` frame field read from D at the gate; the gate satisfies `GateRel`; the image of
                  the frozen product pairs to `-1 / 10` with the two frozen sharp effects; the forward-positivity
                  failure is the negation of the landed `posFwd` field at the gate, proved through that value; no
                  declaration of §D-§F names a landed dimension corollary of the native gate
  S6  scope       no declaration mentions a complex field, the landed `d = 1` gate or a landed dimension selector, no
                  statement mentions the landed `d = 1` NOT or axis, and no theorem concludes an equation or inequation
                  on `d`
  S7  reuse       no declaration of the module shares its name with an OIBridge declaration visible to it; the only
                  import is `OIBridge.EffectSpace`
  S8  phrases     the module header (and, at a commit carrying it, the result note) contains none of the frozen phrases
  S9  count       exactly the frozen `#print axioms` lines, in order, distinct, each naming a declaration of the module
  V   verdicts    each cell is computed from the module's statements and the landed statements at D by its own frozen
                  rule, independently of the others; at a commit carrying the result note, the note states exactly the
                  computed tokens and no other
  I   imports     OIBridge.lean is D's with exactly the frozen import line after `import OIBridge.DenseOrbit`
  C   census      the census is D's with exactly the frozen family inserted after the KTRANS-DENSE-1 family, byte for
                  byte
  F   freeze      (with --freeze) the preregistration at the commit equals F's, and delta(D, F) is the preregistration
"""
import io, json, re, subprocess, sys

D = '@@D@@'
RDIR = 'verification/programmes/oi-qm/reconstruction/round-parity-not-1/'
PREREG = RDIR + 'preregistration.md'
RESULT = RDIR + 'result.md'
LEAN = 'verification/lean-mathlib/OIBridge/'
MOD = LEAN + 'ParityNot.lean'
IMPORTS = 'verification/lean-mathlib/OIBridge.lean'
CENSUS = 'verification/lean-manuscript-census.json'
GOVERNED = {MOD: 'A', IMPORTS: 'M', CENSUS: 'M'}
RECORD_FILES = {RDIR + 'preregistration.md', RDIR + 'controls.py', RDIR + 'result.md'}
MOD_REFERENCE_BLOB = '@@BLOB@@'
ANCHOR_IMPORT = 'import OIBridge.DenseOrbit\n'
NEW_IMPORT = 'import OIBridge.ParityNot\n'
PREV_FAMILY_MODULES = ['DenseOrbit']
CENSUS_FAMILY = json.loads(r'''@@CENSUS_FAMILY@@''')
DECLS = json.loads(r'''@@DECLS@@''')
TEXTS = json.loads(r'''@@TEXTS@@''')
PRINTS = json.loads(r'''@@PRINTS@@''')
PREAMBLE = json.loads(r'''@@PREAMBLE@@''')
CONTEXT = json.loads(r'''@@CONTEXT@@''')
LANDED = json.loads(r'''@@LANDED@@''')
N_PRINTS = @@NPRINTS@@
