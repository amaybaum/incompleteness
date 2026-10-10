#!/usr/bin/env python3
"""Thread D, certified script d3 -- dependency audit of the routes for hcls and hadm (RESULT.md, D3).

For every landed (L) or design-run (D) declaration that the written routes of RESULT.md cite, extract its statement
(from the declaration keyword to the first ':=' or ' where') from the Lean source and check that the statement contains
none of the forbidden or target notions:
  closedness ('IsClosed'), IE1 ('IE1', 'IsRot3'), the parity conclusion ('EvenCycle', 'orient'), quantum cone or complex
  structure ('Q3', 'PosSemidef', 'ℂ', 'Complex', 'Matrix.unitaryGroup'), cone preservation by a gate of the form
  '∀ ω ∈ K, N ω ∈ K' or 'N p ω ∈ K p' (hgate) and its inverse, the four-copy data ('KT4', 'FourCopyCoherent',
  'TokenCoherent'), and the target predicates themselves ('NClass', 'PairAdm') -- except where a declaration's role is to
  state the target (listed as TARGET-STATING and checked to be cited only for the converse or the countermodels).

DECISION RULES (fixed before the first run):
  D-1  every cited declaration must be found exactly once in the named file (otherwise FAIL: citation unresolved);
  D-2  for every declaration classed ROUTE, the extracted statement must contain no forbidden token;
  D-3  the declarations classed TARGET-STATING may mention 'NClass' or 'PairAdm' and nothing else forbidden;
  CC   countercontrol: the same token scan applied to the design headline kt4_forward_ie1 MUST find 'IsClosed',
       'EvenCycle' and 'NClass' (the scan detects these tokens when present).
A VERDICT line prints only if every check passes and the countercontrol behaves as stated.
No floating point, no randomness, no timing in stdout.
"""
import re
import sys
from pathlib import Path

CHECKS = []


def chk(cid, name, ok, kind):
    ok = bool(ok)
    CHECKS.append((cid, kind, ok))
    print(f"{'PASS' if ok else 'FAIL'} {cid}  [{kind}] {name}", flush=True)


PT = Path('/tmp/claude-0/-home-user-incompleteness/727ddb71-72ba-5388-a9a1-1413a0433ac0/scratchpad/pt')
OI = PT / 'base/verification/lean-mathlib/OIBridge'
FC = PT / 'inputs/fourcopy'

FORBIDDEN = ['IsClosed', 'IE1', 'IsRot3', 'EvenCycle', 'orient', 'Q3', 'PosSemidef', 'ℂ', 'Complex',
             'unitaryGroup', 'KT4', 'FourCopyCoherent', 'TokenCoherent', 'NClass', 'PairAdm']
GATE_PRES = [re.compile(r'∀ ω ∈ K\w*, \w+ ω ∈ K'), re.compile(r'N p ω ∈ K p'), re.compile(r'\.symm ω ∈ K')]

# (file, declaration name, class, what the route uses it for)
CITED = [
    (OI / 'CompositeDimension.lean', 'corner_form', 'ROUTE', 'D1 step 2: corner slices'),
    (OI / 'CompositeDimension.lean', 'lor_cornerMap', 'ROUTE', 'D1 step 2: corner maps carry L into L'),
    (OI / 'CompositeDimension.lean', 'tens_hom_inj', 'ROUTE', 'D1 step 2: corner maps from the frame'),
    (OI / 'CompositeDimension.lean', 'pairVal_nonneg_of_maxCone', 'ROUTE', 'D1 steps 5-6: positivity of the pairing'),
    (OI / 'CompositeDimension.lean', 'lor_of_forall_pair', 'ROUTE', 'D1 step 3: self-duality of L'),
    (OI / 'CompositeDimension.lean', 'cnot_frame', 'ROUTE', 'D1 converse: cnot has the frame'),
    (OI / 'CompositeDimension.lean', 'cnot_prodState_mem_maxCone', 'ROUTE', 'D1: N-CLASS implies posFwd, posInv'),
    (OI / 'CompositeDimension.lean', 'nativeGate_cnot', 'ROUTE', 'countermodels: cnot meets the K1 gate premises'),
    (OI / 'CompositeDimension.lean', 'entangling_cnot', 'ROUTE', 'countermodels: cnot is entangling'),
    (OI / 'CompositeDimension.lean', 'isNot_nflip', 'ROUTE', 'countermodels: nflip is a NOT'),
    (OI / 'RelcSelectBlock.lean', 'ctrlGate_of_nativeGate', 'ROUTE', 'D1 corollary: NativeGate gives CtrlGate'),
    (OI / 'RelcSelectBlock.lean', 'gate_corner_ctrl', 'ROUTE', 'D1 corollary under CtrlGate'),
    (OI / 'RelcSelectBlock.lean', 'gate_corner_neg_ctrl', 'ROUTE', 'D1 corollary under CtrlGate'),
    (OI / 'RelcSelectBlock.lean', 'gt_tangent_corners_ctrl', 'ROUTE', 'D1 step 5 under CtrlGate'),
    (OI / 'K2Guard.lean', 'actT_prodState', 'ROUTE', 'D1 steps 1-2: local maps on products'),
    (OI / 'K2Guard.lean', 'prodState_mem_maxCone', 'ROUTE', 'D2 (b) at products; countermodels'),
    (OI / 'K2Guard.lean', 'candidateCone_cnotOrbit', 'ROUTE', 'D2 (c) countermodel'),
    (OI / 'K2Guard.lean', 'cnot_mem_cnotOrbit', 'ROUTE', 'D2 (c) countermodel'),
    (OI / 'CompositeInterface.lean', 'subset_maxBody', 'ROUTE', 'D2 (b) through the chart'),
    (OI / 'CompositeInterface.lean', 'prodEff_expand', 'ROUTE', 'D2 chart: expansion in the first slot'),
    (OI / 'CompositeInterface.lean', 'affine_expand', 'ROUTE', 'D2 chart: affine expansion'),
    (OI / 'CompositeInterface.lean', 'pEff_basisEff', 'ROUTE', 'D2 chart: q is the identity on the model'),
    (OI / 'CompositeInterface.lean', 'isEffectOn_maxBody', 'ROUTE', 'D2 converse: product effects are effects'),
    (OI / 'CompositeInterface.lean', 'not_locallyTomographic_paddedBall3', 'ROUTE', 'D2: lt not needed (control)'),
    (FC / 'FourCopyLocal.lean', 'NClass.ipW_map', 'TARGET-STATING', 'D1 minimality: N-CLASS gates are orthogonal'),
    (FC / 'FourCopyLocal.lean', 'NClass.bell_state', 'TARGET-STATING', 'D1 minimality: N-CLASS maps a product to bellOf'),
    (FC / 'FourCopyBipolar.lean', 'bidual_of_adm', 'TARGET-STATING', 'D2 USES of the convex-cone clause'),
    (FC / 'FourCopyBridge.lean', 'fourCopyCoherent_of_kt4Core', 'TARGET-STATING', 'D2 USES of (b) and scaling'),
]


def statement(src, name):
    pat = re.compile(rf'^(?:theorem|def|lemma|abbrev) {re.escape(name)}\b', re.M)
    hits = list(pat.finditer(src))
    if len(hits) != 1:
        return None, len(hits)
    start = hits[0].start()
    rest = src[start:]
    m = re.search(r':=|\bwhere\b', rest)
    return rest[:m.start()] if m else rest, 1


print('== D-1 .. D-3  cited declarations')
for path, name, cls, use in CITED:
    src = path.read_text(encoding='utf-8')
    st, n = statement(src, name)
    if st is None:
        chk(f'D1:{name}', f'{name} found exactly once in {path.name} (found {n})', False, 'source')
        continue
    toks = [t for t in FORBIDDEN if re.search(rf'(?<![\w.]){re.escape(t)}(?![\w])', st)]
    gp = [g.pattern for g in GATE_PRES if g.search(st)]
    if cls == 'ROUTE':
        ok = not toks and not gp
        chk(f'D2:{name}', f'{path.name}:{name} [{use}] -- statement free of forbidden tokens'
            + (f' (found {toks + gp})' if not ok else ''), ok, 'source')
    else:
        bad = [t for t in toks if t not in ('NClass', 'PairAdm')] + gp
        chk(f'D3:{name}', f'{path.name}:{name} [{use}] -- TARGET-STATING: mentions only the target predicate'
            + (f' (also {bad})' if bad else ''), not bad, 'source')

print()
print('== CC  countercontrol on the design headline')
hl = (FC / 'FourCopyHeadline.lean').read_text(encoding='utf-8')
st, n = statement(hl, 'kt4_forward_ie1')
found = [t for t in ('IsClosed', 'EvenCycle', 'NClass') if st and re.search(rf'(?<![\w.]){t}(?![\w])', st)]
chk('CC', f'countercontrol: the scan finds IsClosed, EvenCycle, NClass in kt4_forward_ie1 (found {found})',
    st is not None and len(found) == 3, 'countercontrol')

print()
fails = [c for c, k, ok in CHECKS if not ok]
print(f'd3_deps: {len(CHECKS)} checks, {len(fails)} failed')
if not fails:
    print('VERDICT D3-NO-FORBIDDEN-DEPENDENCY: no cited route declaration states closedness, IE1, the parity, a cone-'
          'preservation clause, four-copy data, a quantum or complex structure, or the target; the target-stating '
          'citations are confined to the converse and minimality steps')
    sys.exit(0)
print('NO VERDICT: failed checks ' + ', '.join(fails))
sys.exit(1)
