#!/usr/bin/env python3
"""b18_reclass.py -- node B18 of research/bridge (round 5): the re-classification of FM's rows I4.56 and I2.34
(HO-33's correction item; the round-4 audit's finding F1), under the owner's round-5 requirement (1): a chain whose
every link's side hypotheses FM satisfies -- the quarter phase from DerivedOI, avail_conj_mul, the exchange's layer
flow -- never LiftAudit.lean:812 or :783 for FM.

DECISION RULE (fixed 2026-10-11T08:06:00Z, from `date -u` immediately before writing; before run 1).

The row table ROWS of b14_fullmodel.py (round 4) is loaded unchanged by executing that file's text before
`def main():` (the round-4 script, its output and its replay stay the round-4 record; nothing in them is edited).
Two rows are re-classed, the rest untouched:
  I4.56 (M, fails in FM): chain = the DerivedOI chain of lean/BridgeToken.lean section B --
      LayerFlowExecutable (the exchange, fixed-point-free) with DerivedOI (I4.241; [D] latticeTheory_derivedOI)
      => PhaseFreeRichness (I4.118) [D] phaseFree_of_layerFlowExecutable_derivedOI, whose links are the kernel's
         gateFlow_isolation (LiftAudit.lean:660), conjChannel_smul (ImplementationLocality.lean:395) and
         avail_conj_mul (LiftAudit.lean:770) with the quarter phases and exchanges of DerivedOI (RouteB.lean:123, :128)
      => HasCompositeUnitaryControl (I4.67) [K] control_of_phaseFree (MinimalRepertoire.lean:529), side hypothesis
         IteratedAncillaClosure (I4.68) [D] latticeTheory_closure (kernel closure_of_embeddedObservation,
         EmbeddedObservation.lean:211)
      => both token operators at every level [D] layerFlow_supplies_token; both pair operators [D]
         layerFlow_supplies_pair (pairAvail_of_control); and QM [K] derivedOI_qm_iff_phaseFree (RouteB.lean:161).
  I2.34 (G, fails in FM -- its assumed part, executability): chain = QM <-> LayerFlowExecutable for FM on Fin 2 and on
      Fin 2 x Fin 2, [D] latticeTheory_token_qm_iff_layerFlow / latticeTheory_pair_qm_iff_layerFlow (the DerivedOI
      chain above; the converse direction [K] layerFlowExecutable_of_control, LiftAudit.lean:117, with
      physical_of_exactAll, PhysicalCharacterization.lean:301) => QM.
The design links carry the tag [D] iff DESIGN_BUILT is True, which is set only after this round's dispatch has built
lean/BridgeToken.lean green with every `#print axioms` line standard; run 1 is made before the dispatch with
DESIGN_BUILT = False, is kept as b18_reclass.run1.*, and tags the design links [W] (the round-4 audit's disposition:
HARMLESS by a written argument). The classifier and the controls C1-C5 of b14_fullmodel.py are re-run on the amended
table. New controls:
  C6  every kernel name the new chains cite exists in the kernel at L at the cited line (the declaration line of
      the file in this tree, identical to L).
  C7  countercontrol: LiftAudit.lean:812 (the replaced chain) carries the hypothesis `hsub : SubstratumAvail T`, FM
      fails it ([D] lattice_strict_in_substratum, recorded), and the new chains' texts cite neither LiftAudit.lean:812
      nor :783.
  C8  exact (Gaussian integers): on Fin 2 x Fin n, n = 1, 2, 3, every diagonal with entries +-1 equals the product over
      its -1 positions of phaseGate(p)^2, phaseGate p = diag(1, ..., i, ..., 1) (LieRankSource.lean:209), and
      phaseGate(p)^4 = 1 (the sign diagonals of the chain are products of quarter phases, so no phase at a general
      angle enters).
Scope sentence, generated from the measured counts: of the 29 control-or-QM rows, how many rest on a kernel chain at L
whose side hypotheses FM satisfies, how many on the design chain, how many on a written argument.

VERDICT B18-RECLASS-OK iff the tally is SAT 34 / HARMLESS 29 / NA 5 / HARMFUL 0 and C1-C8 all PASS; otherwise
VERDICT B18-RECLASS-FAILED followed by the failing ids.
Run from experiments/:  python3 -I -B b18_reclass.py > b18_reclass.out 2> b18_reclass.err

Post-run edit after run 1 (2026-10-11T08:32:20Z; run 1 kept as b18_reclass.run1.*; rule text unchanged): DESIGN_BUILT
set to True, as the rule provides, after dispatch 2 of 3 (run 38124442150, dev-bridge/r5-bridge2 @ 16e75fbe, job
114425761656) built lean/BridgeToken.lean (dev blob dda95f6b, sha256 23e3dcde...) green: "Built OIBridge.BridgeToken
(3.2s)", 36/36 `#print axioms` lines standard (34 on [propext, Classical.choice, Quot.sound], 2 on [Quot.sound]), no
sorryAx anywhere in the build, lean-axioms PASS (6096 named results). Run 2 tags the design links [D].
"""
import itertools
import os
import re
import sys

DESIGN_BUILT = True    # set to True only after the dispatch builds BridgeToken.lean green with standard axioms (run 38124442150)

HERE = os.path.dirname(os.path.abspath(__file__))
KERNEL = os.path.join(HERE, '..', '..', '..', 'verification', 'lean-mathlib', 'OIBridge')

# ---------------------------------------------------------------- the round-4 table, unchanged
src = open(os.path.join(HERE, 'b14_fullmodel.py'), encoding='utf-8').read()
prefix = src[:src.index('\ndef main():')]
ns = {'__name__': 'b14_rows'}
cwd = os.getcwd()
os.chdir(HERE)
try:
    exec(compile(prefix, 'b14_fullmodel.py', 'exec'), ns)
finally:
    os.chdir(cwd)
ROWS = dict(ns['ROWS'])
ROWS_PERM = dict(ns['ROWS_PERM'])
classify = ns['classify']
table_a2_notreached = ns['table_a2_notreached']
i4_status = ns['i4_status']
sha = ns['sha']
R6, R4T, I4 = ns['R6'], ns['R4T'], ns['I4']

TAG = '[D]' if DESIGN_BUILT else '[W]'
D = '[D] BridgeAvailFull'
OLD = {k: ROWS[k] for k in ('I4.56', 'I2.34')}
NEW = {
    'I4.56': ('M', 'fails', 'LayerFlowExecutable; ' + D + ' latticeTheory_not_layerFlowExecutable',
              ['with DerivedOI (I4.241, ' + D + ' latticeTheory_derivedOI): LayerFlowExecutable (exchange) => '
               'PhaseFreeRichness ' + TAG + ' BridgeToken phaseFree_of_layerFlowExecutable_derivedOI '
               '(gateFlow_isolation [K] LiftAudit.lean:660, conjChannel_smul [K] ImplementationLocality.lean:395, '
               'avail_conj_mul [K] LiftAudit.lean:770, quarter phases and exchanges of DerivedOI [K] RouteB.lean:128, :123)',
               'PhaseFreeRichness => control [K] control_of_phaseFree MinimalRepertoire.lean:529 '
               '(IteratedAncillaClosure ' + D + ' latticeTheory_closure, closure_of_embeddedObservation [K] '
               'EmbeddedObservation.lean:211)',
               'control => both token and pair operators ' + TAG + ' layerFlow_supplies_token / layerFlow_supplies_pair',
               'control']),
    'I2.34': ('G', 'fails', 'layer-flow form: FM lacks executability',
              ['QM <-> LayerFlowExecutable for FM on Fin 2 and Fin 2 x Fin 2 ' + TAG +
               ' BridgeToken latticeTheory_token_qm_iff_layerFlow / latticeTheory_pair_qm_iff_layerFlow '
               '(derivedOI_qm_iff_phaseFree [K] RouteB.lean:161; layerFlowExecutable_of_control [K] LiftAudit.lean:117; '
               'physical_of_exactAll [K] PhysicalCharacterization.lean:301)',
               'QM']),
}
ROWS.update(NEW)
ROWS_PERM.update(NEW)

PASS, FAIL = [], []


def check(name, ok, msg=''):
    (PASS if ok else FAIL).append(name)
    print(('PASS ' if ok else 'FAIL ') + name + ((': ' + msg) if msg else ''))


def kernel_line(fname, line):
    with open(os.path.join(KERNEL, fname), encoding='utf-8') as f:
        lines = f.read().split('\n')
    return lines[line - 1] if 0 < line <= len(lines) else ''


def main():
    print('inputs:')
    for p in (R6, R4T, I4):
        print('  ', p, sha(os.path.join(HERE, p)))
    print('  b14_fullmodel.py', sha(os.path.join(HERE, 'b14_fullmodel.py')))
    print('DESIGN_BUILT =', DESIGN_BUILT, ' (design links tagged', TAG + ')')
    print('\nrows re-classed (old -> new):')
    for k in ('I4.56', 'I2.34'):
        print('  ', k, 'OLD chain:', ' -> '.join(OLD[k][3]))
        print('  ', k, 'NEW chain:', ' -> '.join(NEW[k][3]))
    cwd = os.getcwd()
    os.chdir(HERE)
    try:
        ids, a2 = table_a2_notreached()
    finally:
        os.chdir(cwd)
    print('Table A2 rows parsed:', len(a2), ' NOT REACHED:', len(ids))
    cls = classify(ROWS)
    tally = {}
    for k in ids:
        tally[cls.get(k, 'MISSING')] = tally.get(cls.get(k, 'MISSING'), 0) + 1
    print('\nFM classification of the 68 NOT REACHED rows (round 5, the two rows re-classed)')
    print('| row | level at FM | class | evidence | chain |')
    print('|---|---|---|---|---|')
    for k in ids:
        lev, st, ev, chain = ROWS[k]
        print('| %s | %s | %s | %s | %s |' % (k, lev, cls[k], ev, ' -> '.join(chain) if chain else '-'))
    print('\nTALLY FM', dict(sorted(tally.items())))
    # the chain kinds of the HARMLESS rows
    harmless = [k for k in ids if cls[k] == 'HARMLESS']
    design = [k for k in harmless if 'BridgeToken' in ' '.join(ROWS[k][3])]
    written = [k for k in harmless if '[W]' in ' '.join(ROWS[k][3])]
    kernel = [k for k in harmless if k not in design and k not in written]
    print('\nHARMLESS rows by chain kind: kernel chain at L (side hypotheses FM satisfies) %d %s; design chain %d %s; '
          'written %d %s' % (len(kernel), kernel, len(design), design, len(written), written))
    if DESIGN_BUILT:
        scope = ('Of the 29 control-or-QM rows, %d rest on a kernel chain at L whose side hypotheses FM satisfies and %d '
                 '(%s) on the design chain of BridgeToken.lean [D] with kernel theorems [K]; none rests on a written '
                 'argument.' % (len(kernel), len(design), ', '.join(design)))
    else:
        scope = ('Of the 29 control-or-QM rows, %d rest on a kernel chain at L whose side hypotheses FM satisfies and %d '
                 '(%s) on a written chain [W] (the design module not yet built).' % (len(kernel), len(written), ', '.join(written)))
    print('SCOPE SENTENCE:', scope)

    checks = []
    checks.append(('C1 ids = Table A2 NOT REACHED (68)', set(ids) == set(ROWS) and len(ids) == 68))
    c2 = all(ROWS[k][3] and ROWS[k][3][-1] in ('control', 'QM') for k in ids if cls[k] == 'HARMLESS')
    checks.append(('C2 every HARMLESS chain ends in control or QM', c2))
    nums = [int(k.split('.')[1]) for k in ids if k.startswith('I4.')]
    cwd = os.getcwd()
    os.chdir(HERE)
    try:
        st = i4_status(nums)
    finally:
        os.chdir(cwd)
    harm_t = ('equivalent to exact finite operational QM', '⟺ exact finite operational QM', '⟺ (with DerivedOI) exact QM',
              'gives HasCompositeUnitaryControl', 'gives control', 'implies PhaseFreeRichness')
    sat_t = ('derived from ImplementationLocality', 'derived from EmbeddedObservation', 'implied by ImplementationLocality',
             'implied by HasParallelReferenceExtension', 'equivalent to HasParallelReferenceExtension',
             'dagger-stable, unitary-ray-saturated generating class', 'generated by a label-invariant architecture', 'proved [K]')
    forced, bad = {}, []
    for n, s in st.items():
        k = 'I4.%d' % n
        h = any(t in s for t in harm_t)
        sa = any(t in s for t in sat_t)
        if h and sa:
            forced[k] = 'BOTH'
            bad.append(k)
        elif h:
            forced[k] = 'HARMLESS'
            if cls[k] != 'HARMLESS':
                bad.append(k)
        elif sa:
            forced[k] = 'SAT'
            if cls[k] != 'SAT':
                bad.append(k)
    checks.append(('C3 inventory status text agrees (%d forced rows; disagreements %s)' % (len(forced), bad),
                   not bad and len(forced) >= 20))
    t = open(os.path.join(HERE, R4T), encoding='utf-8').read()
    m = re.search(r"TALLY Q3\s+\{'NOT': (\d+), 'SATISFIES': (\d+)\}", t)
    checks.append(('C4 R6 Q3 tally 131 SATISFIES / 68 NOT, no FAILS', bool(m) and m.group(1) == '68' and m.group(2) == '131'
                   and 'CHECK (2) Q3 column has no FAILS PASS' in t))
    cp = classify(ROWS_PERM)
    harmful_perm = sorted(k for k in ids if cp[k] == 'HARMFUL')
    checks.append(('C5 countercontrol: permTheory has DerivedOI HARMFUL (%s)' % harmful_perm, harmful_perm == ['I4.241']))
    # C6: the cited kernel declarations exist at the cited lines
    cites = [('LiftAudit.lean', 660, 'theorem gateFlow_isolation'),
             ('ImplementationLocality.lean', 395, 'theorem conjChannel_smul'),
             ('LiftAudit.lean', 770, 'theorem avail_conj_mul'),
             ('RouteB.lean', 128, 'def PhasesAvailable'),
             ('RouteB.lean', 123, 'def ExchangesAvailable'),
             ('MinimalRepertoire.lean', 529, 'theorem control_of_phaseFree'),
             ('EmbeddedObservation.lean', 211, 'theorem closure_of_embeddedObservation'),
             ('RouteB.lean', 161, 'theorem derivedOI_qm_iff_phaseFree'),
             ('LiftAudit.lean', 117, 'theorem layerFlowExecutable_of_control'),
             ('PhysicalCharacterization.lean', 301, 'theorem physical_of_exactAll'),
             ('LieRankSource.lean', 209, 'def phaseGate')]
    c6 = []
    for fname, line, decl in cites:
        txt = kernel_line(fname, line)
        ok = decl in txt
        c6.append(ok)
        print('  C6 %s:%d %s -> %s' % (fname, line, decl, 'found' if ok else 'NOT FOUND: ' + txt.strip()[:60]))
    checks.append(('C6 every cited kernel declaration at its line (%d/%d)' % (sum(c6), len(c6)), all(c6)))
    # C7: the replaced chain's hypothesis, and no citation of :812/:783 in the new chains
    l812 = kernel_line('LiftAudit.lean', 812) + kernel_line('LiftAudit.lean', 813)
    has_sub = 'derivedOI_qm_iff_layerFlowExecutable' in l812 and 'hsub : SubstratumAvail T' in l812
    newtxt = ' '.join(' '.join(NEW[k][3]) + ' ' + NEW[k][2] for k in NEW)
    no_cite = ('LiftAudit.lean:812' not in newtxt) and ('LiftAudit.lean:783' not in newtxt)
    print('  C7 LiftAudit.lean:812 carries hsub : SubstratumAvail T ->', has_sub,
          '; FM fails it ([D] BridgeAvailFull lattice_strict_in_substratum); new chains cite neither :812 nor :783 ->', no_cite)
    checks.append(('C7 countercontrol: the replaced chain needs SubstratumAvail, the new chains cite neither :812 nor :783',
                   has_sub and no_cite))
    # C8: exact, the sign diagonals as products of quarter-phase squares (Gaussian integers as (re, im) pairs)
    def gmul(a, b):
        return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])
    ONE, IM, NEG = (1, 0), (0, 1), (-1, 0)
    c8 = True
    for n in (1, 2, 3):
        conf = [(s, k) for s in (0, 1) for k in range(n)]
        N = len(conf)
        # phaseGate p = diag(1, ..., i at p, ..., 1); diagonals represented by their entry lists
        def phase(p):
            return [IM if q == p else ONE for q in conf]
        def dmul(d1, d2):
            return [gmul(x, y) for x, y in zip(d1, d2)]
        for signs in itertools.product((1, -1), repeat=N):
            target = [ONE if s == 1 else NEG for s in signs]
            prod = [ONE] * N
            for p, s in zip(conf, signs):
                if s == -1:
                    prod = dmul(prod, dmul(phase(p), phase(p)))
            if prod != target:
                c8 = False
        for p in conf:
            if dmul(dmul(phase(p), phase(p)), dmul(phase(p), phase(p))) != [ONE] * N:
                c8 = False
    checks.append(('C8 exact: every +-1 diagonal on Fin 2 x Fin n (n = 1, 2, 3) is the product of quarter-phase squares '
                   'over its -1 positions; phaseGate^4 = 1', c8))

    print('\nCHECKS')
    for name, ok in checks:
        check(name, ok)
    allok = all(ok for _, ok in checks)
    tally_ok = (tally.get('SAT', 0), tally.get('HARMLESS', 0), tally.get('NA', 0), tally.get('HARMFUL', 0)) == (34, 29, 5, 0)
    print('tally as predicted (34/29/5/0):', tally_ok)
    if allok and tally_ok:
        print('VERDICT B18-RECLASS-OK: I4.56 and I2.34 HARMLESS by the DerivedOI chain %s; %s' % (TAG, scope))
    else:
        print('VERDICT B18-RECLASS-FAILED ' + ' '.join([n for n, ok in checks if not ok] + ([] if tally_ok else ['TALLY'])))


if __name__ == '__main__':
    main()
    sys.exit(0)
