"""b14_fullmodel.py — research/bridge, round 4, node B14 (third addendum): the full-model row check.

S0 (written 2026-10-11T05:25:38Z, NOTES-B14 §8.0, before this script's first run). Decision rules fixed there:
each of the 68 NOT REACHED rows of R6's Table A2 is classed SAT / HARMLESS / HARMFUL / NA for the model FM
(H: sealed core + wave substratum; M: the lattice theory; O: the ball with its effects; P: Q3). The class is
computed, not entered: a row FM satisfies is SAT; a row FM fails is HARMLESS iff its implication chain (given rows
FM satisfies) ends in composite unitary control or QM, HARMFUL otherwise; a scope statement is NA.

Controls: (C1) the 68 ids are exactly Table A2's NOT REACHED rows; (C2) every HARMLESS row's chain ends in control
or QM; (C3) the I4 inventory's own status text forces the class of the rows it speaks to (QM-equivalence or a
derivation of control => HARMLESS; derivation from implementation locality / embedded observation / parallel
reference extension / a dagger-stable saturated class, or a kernel theorem => SAT); (C4) R6's Q3 tally is 131
SATISFIES and 68 NOT, with no FAILS; (C5) countercontrol: the same rule applied to the observer theory alone
(permTheory) puts DerivedOI (I4.241) in HARMFUL. Exact checks X1–X4 on the lattice (Gaussian integers / rationals).
Run from experiments/:  python3 -I -B b14_fullmodel.py > b14_fullmodel.out 2> b14_fullmodel.err
"""
import hashlib
import re
from fractions import Fraction as Fr

ARCH = '../../archive/pt'
R6 = ARCH + '/R6/REASSESSMENT.md'
R4T = ARCH + '/R6/r4_tables.out'
I4 = ARCH + '/I4/INVENTORY.md'


def sha(p):
    with open(p, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


# ---------------------------------------------------------------- the model's row classification
# fields: level at FM, status in {holds, fails, scope}, evidence, chain (for fails: kernel implication chain,
# last element 'control' or 'QM' when the row gives the operations; empty when no implication is known)
D = '[D] BridgeAvailFull'
ROWS = {
    # I4 — the 44 do-not-assume records (level M unless stated)
    'I4.3': ('M', 'holds', D + ' latticeTheory_parallel (kernel parallel_of_implementationLocal, ImplementationLocality.lean:943)', []),
    'I4.4': ('M', 'holds', D + ' latticeTheory_qutrit (kernel qutrit_of_parallel, ReferenceExtension.lean:474)', []),
    'I4.14': ('M', 'holds', D + ' latticeTheory_inert (kernel inertSpectator_iff_parallelReferenceExtension, SpectatorBridge.lean:233)', []),
    'I4.29': ('M', 'holds', D + ' latticeClass_contextStable (for permClass [K] SubstratumInterfaceAudit.lean:358)', []),
    'I4.31': ('M', 'holds', D + ' latticeTheory_implementationLocality (kernel genTheory_implementationLocality)', []),
    'I4.42': ('M', 'fails', 'OIPlusLocal', ['OIPlusLocal <-> QM [K] ImplementationLocality.lean:1070', 'QM']),
    'I4.45': ('M', 'holds', D + ' latticeClass_structurallyClosed', []),
    'I4.56': ('M', 'fails', 'LayerFlowExecutable; ' + D + ' latticeTheory_not_layerFlowExecutable',
              ['with DerivedOI: QM <-> LayerFlowExecutable [K] LiftAudit.lean:812', 'QM']),
    'I4.65': ('M', 'fails', 'PhysicalCompletionConditions', ['third conjunct HasCompositeUnitaryControl (definition)', 'control']),
    'I4.66': ('M', 'holds', D + ' latticeTheory_validity (kernel validity_of_implementationLocality, :971)', []),
    'I4.67': ('M', 'fails', 'HasCompositeUnitaryControl; ' + D + ' latticeTheory_pair_not_control', ['control']),
    'I4.68': ('M', 'holds', D + ' latticeTheory_closure (kernel closure_of_embeddedObservation, EmbeddedObservation.lean:211)', []),
    'I4.69': ('M', 'holds', D + ' latticeTheory_systemToLevelOne (kernel, EmbeddedObservation.lean:223)', []),
    'I4.70': ('M', 'fails', 'ExactAllFiniteEndomorphicQuantumOps; ' + D + ' latticeTheory_not_qm', ['QM']),
    'I4.73': ('M', 'holds', D + ' latticeTheory_wellFormed', []),
    'I4.74': ('M', 'fails', 'SubstantiveCompletion', ['second conjunct HasCompositeUnitaryControl (definition)', 'control']),
    'I4.80': ('M', 'fails', 'CompletedOI', ['<-> PhysicalCompletionConditions [K] CompletedOI.lean:110', 'third conjunct control', 'control']),
    'I4.82': ('M', 'holds', D + ' latticeTheory_qubitObservationalIndependence', []),
    'I4.85': ('M', 'fails', 'ReversibleRichness (qubit)', ['control_of_reversibleRichness [K] CompletedOI.lean:200', 'control']),
    'I4.87': ('M', 'holds', D + ' latticeTheory_observerRecursion (kernel, EmbeddedObservation.lean:217)', []),
    'I4.88': ('M', 'fails', 'OIPlus (qubit)', ['oiPlus_iff_qm [K] CompletedOI.lean:440', 'QM']),
    'I4.96': ('M', 'holds', D + ' latticeTheory_observationalIndependence (kernel, ImplementationLocality.lean:957)', []),
    'I4.99': ('M', 'fails', 'ReversibleRichness', ['control_of_reversibleRichness [K] CarrierGeneralOIPlus.lean:127', 'control']),
    'I4.102': ('M', 'fails', 'OIPlus', ['oiPlus_iff_qm [K] CarrierGeneralOIPlus.lean:207', 'QM']),
    'I4.110': ('M', 'holds', D + ' latticeTheory_embeddedObservation (kernel genTheory_embeddedObservation)', []),
    'I4.115': ('M', 'fails', 'OIPlusEmbedded', ['oiPlusEmbedded_iff_oiPlus [K] EmbeddedObservation.lean:388', 'oiPlus_iff_qm', 'QM']),
    'I4.118': ('M', 'fails', 'PhaseFreeRichness; ' + D + ' latticeTheory_not_phaseFree',
               ['with IteratedAncillaClosure: control_of_phaseFree [K] MinimalRepertoire.lean:529', 'control']),
    'I4.120': ('M', 'fails', 'OIPlusMin', ['oiPlusMin_iff_qm [K] MinimalRepertoire.lean:569', 'QM']),
    'I4.123': ('M', 'fails', 'CyclicRichness', ['phaseFree_of_cyclic [K] MinimalRepertoire.lean:642', 'control_of_phaseFree', 'control']),
    'I4.124': ('M', 'fails', 'OIPlusPos', ['oiPlusPos_iff_qm [K] PositivePackage.lean:55', 'QM']),
    'I4.127': ('M', 'holds', D + ' latticeTheory_inverseAccessibility (kernel, MicroscopicReversibility.lean:283)', []),
    'I4.128': ('M', 'fails', 'LieRankRichness', ['control_of_lieRank [K] MicroscopicReversibility.lean:114', 'control']),
    'I4.133': ('M', 'holds', D + ' latticeTheory_reversibleImplementationLocality', []),
    'I4.137': ('M', 'fails', 'OIPlusMicro', ['oiPlusMicro_iff_qm [K] MicroscopicReversibility.lean:357', 'QM']),
    'I4.143': ('M', 'fails', 'DrivesElementary; ' + D + ' latticeClass_not_drivesElementary',
               ['genTheory_elementary [K] SubstratumSource.lean:109', 'phaseFree_of_elementary [K] MinimalRepertoire.lean:430',
                'control_of_phaseFree', 'control']),
    'I4.144': ('M', 'fails', 'QuantumArchitecture; ' + D + ' latticeClass_not_quantumArchitecture',
               ['field drives: DrivesElementary', 'genTheory_elementary', 'phaseFree_of_elementary', 'control_of_phaseFree', 'control']),
    'I4.179': ('M', 'fails', 'PairFlowSourced', ['with DerivedOI: qm_of_derivedOI_pairFlowSourced [K] PairFlowEquivalence.lean:190', 'QM']),
    'I4.187': ('G', 'fails', 'ShadowQuantum (the shadow of FM is the lattice theory, not QM)', ['QM on every carrier (definition)', 'QM']),
    'I4.210': ('M', 'holds', '[K] theorem (PSD duality; FM states are PSD)', []),
    'I4.215': ('M', 'holds', '[K] theorem (PSD pairing; FM states are PSD)', []),
    'I4.216': ('M', 'holds', '[K] theorem (accessible cone; FM states are PSD)', []),
    'I4.241': ('M', 'holds', D + ' latticeTheory_derivedOI (kernel derivation of derivedOI_of_stated, StateMixingCoupling.lean:463)', []),
    'I4.244': ('M', 'fails', 'ElementaryTransitionRichness', ['phaseFree_of_elementary [K] MinimalRepertoire.lean:430', 'control_of_phaseFree', 'control']),
    'I4.245': ('M', 'fails', 'OIPlusElem', ['oiPlusElem_iff_qm [K] LieRankSource.lean:543', 'QM']),
    # I2 — the 11 do-not-assume records, and I1.17
    'I1.17': ('H/M/G', 'scope', 'layered theorem statement (Main.md:82): a scope statement', []),
    'I2.3': ('G', 'scope', 'operational-extension boundary: a scope statement', []),
    'I2.29': ('G', 'holds', '[K] theorem (exactAll_iff_physical_general); FM fails (iv) and is not QM, as the theorem requires', []),
    'I2.30': ('G', 'holds', '[K] theorem (oi_alone_not_qm); FM instantiates "bare finite OI does not imply QM"', []),
    'I2.31': ('G', 'fails', 'OI+ package: FM has (1) and (3), fails (2) reversible richness', ['oiPlus_iff_qm', 'QM']),
    'I2.32': ('G', 'fails', 'primitive-source form: FM has locality and embedded observation, fails phase-free richness',
              ['oiPlusMin_iff_qm', 'QM']),
    'I2.33': ('G/H', 'fails', 'substratum-source form: FM lacks the phase intervention at general angles and the controllability resource',
              ['phase intervention at theta0 supplies zPh: substratum_pairAvail_zPh [D B14]', 'controllability: substratum_plus_control_qm [K]', 'QM']),
    'I2.34': ('G', 'fails', 'layer-flow form: FM lacks executability', ['with DerivedOI: QM <-> LayerFlowExecutable [K]', 'QM']),
    'I2.35': ('G', 'fails', 'typed form: its resource is the substratum-source form\'s', ['as I2.33', 'QM']),
    'I2.62': ('M/G', 'scope', 'comparison of routes: a scope statement', []),
    'I2.63': ('G/O', 'scope', 'operational-reconstruction route: a scope statement', []),
    'I2.69': ('H/M/G', 'scope', 'the claim structure: a scope statement', []),
    # I3 — the 12 nr rows (P, O)
    'I3.96': ('O', 'holds', '[A]/[W] FM token body eball 3 has finite rank (dimension 3), as for Q3', []),
    'I3.99': ('O', 'holds', '[W] an operation datum with affine respect and an inverse: the NOT, available in FM', []),
    'I3.104': ('O', 'holds', '[K] theorem body_isClosed', []),
    'I3.105': ('O', 'holds', '[K] theorem preservesBody_inducedEquiv', []),
    'I3.134': ('P4', 'holds', '[W] token coherence of the Kronecker/PSD four-token composite', []),
    'I3.136': ('P4', 'holds', '[W] Lemma R interface families hold for Q3 on every pair (quantum four-copy composite)', []),
    'I3.141': ('P4', 'holds', '[W] KT4Cone with K4 the four-qubit PSD cone: products in, product effects nonnegative', []),
    'I3.145': ('P', 'holds', '[W] P-STAGE2: FM pair completion is the PSD slice, charted onto W 3 by the dictionary (B15)', []),
    'I3.146': ('P', 'holds', '[W]+[D] P-ACT2: the CNOT is a permutation matrix available in FM; dict_cnot (B11)', []),
    'I3.154': ('P4', 'holds', '[W] IE2 in both readings: Q3-type cones invariant; FM pair operations extend idly (ContextStable)', []),
    'I3.157': ('P4', 'holds', '[W] SDC: P3, OVL4, CSD2 for the PSD composites (self-duality of the PSD cone)', []),
    'I3.158': ('P4', 'holds', '[W] N0-N2: regrouping invariance of the Kronecker composite', []),
}

# the observer theory alone (permTheory): identical except DerivedOI fails with no implication chain
ROWS_PERM = dict(ROWS)
ROWS_PERM['I4.241'] = ('M', 'fails', '[K] permTheory_not_derivedOI (SubstratumInterfaceAudit.lean:686): the quarter phase', [])
ROWS_PERM['I4.127'] = ('M', 'holds', '[K] inverseAccessibility_of_generated_daggerStable with permClass_unitaryRaySaturated', [])


def classify(rows):
    out = {}
    for k, (lev, st, ev, chain) in rows.items():
        if st == 'holds':
            c = 'SAT'
        elif st == 'scope':
            c = 'NA'
        elif chain and chain[-1] in ('control', 'QM'):
            c = 'HARMLESS'
        else:
            c = 'HARMFUL'
        out[k] = c
    return out


def table_a2_notreached():
    lines = open(R6).read().split('\n')
    s = next(i for i, l in enumerate(lines) if l.startswith('### Table A2'))
    e = next(i for i in range(s + 1, len(lines)) if lines[i].startswith('### Table A3'))
    ids, cls = [], {}
    for l in lines[s:e]:
        m = re.match(r'\| (I\d\.\d+) \|.*\| (\w+) \| (NOT REACHED|SATISFIES[^|]*|FAILS[^|]*|UNDECIDED) \|', l)
        if m:
            cls[m.group(1)] = m.group(3).split()[0]
            if m.group(3) == 'NOT REACHED':
                ids.append(m.group(1))
    return ids, cls


def i4_status(nums):
    txt = open(I4).read().split('\n')
    starts = {}
    for i, l in enumerate(txt):
        m = re.match(r'### I4\.(\d+) ', l)
        if m:
            starts[int(m.group(1))] = i
    st = {}
    for k in nums:
        j = starts[k] + 1
        while not txt[j].startswith('- **status:**'):
            j += 1
        st[k] = txt[j]
    return st


def gauss_mul(a, b):  # Gaussian rationals as pairs (re, im) of Fractions
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def mat_mul(A, B):
    n = len(A)
    Z = (Fr(0), Fr(0))
    C = [[Z] * n for _ in range(n)]
    for i in range(n):
        for k in range(n):
            if A[i][k] != Z:
                for j in range(n):
                    if B[k][j] != Z:
                        p = gauss_mul(A[i][k], B[k][j])
                        C[i][j] = (C[i][j][0] + p[0], C[i][j][1] + p[1])
    return C


def on_lattice(A):
    Z = (Fr(0), Fr(0))
    n = len(A)
    for i in range(n):
        if sum(1 for j in range(n) if A[i][j] != Z) > 1:
            return False
    for j in range(n):
        if sum(1 for i in range(n) if A[i][j] != Z) > 1:
            return False
    f = set()
    for i in range(n):
        for j in range(n):
            if A[i][j] != Z:
                x = A[i][j]
                x2 = gauss_mul(x, x)
                f.add(gauss_mul(x2, x2))
    return len(f) <= 1


def main():
    print('inputs:')
    for p in (R6, R4T, I4):
        print('  ', p, sha(p))
    ids, a2 = table_a2_notreached()
    print('Table A2 rows parsed:', len(a2), ' NOT REACHED:', len(ids))
    cls = classify(ROWS)
    tally = {}
    for k in ids:
        tally[cls.get(k, 'MISSING')] = tally.get(cls.get(k, 'MISSING'), 0) + 1
    by_inv = {}
    for k in ids:
        inv = k.split('.')[0]
        by_inv.setdefault(inv, {}).setdefault(cls[k], 0)
        by_inv[inv][cls[k]] += 1
    print('\nFM classification of the 68 NOT REACHED rows')
    print('| row | level at FM | class | evidence | chain |')
    print('|---|---|---|---|---|')
    for k in ids:
        lev, st, ev, chain = ROWS[k]
        print('| %s | %s | %s | %s | %s |' % (k, lev, cls[k], ev, ' -> '.join(chain) if chain else '-'))
    print('\nTALLY FM', dict(sorted(tally.items())))
    for inv in sorted(by_inv):
        print('TALLY FM', inv, dict(sorted(by_inv[inv].items())))
    checks = []
    # C1
    checks.append(('C1 ids = Table A2 NOT REACHED (68)', set(ids) == set(ROWS) and len(ids) == 68))
    # C2
    c2 = all(ROWS[k][3] and ROWS[k][3][-1] in ('control', 'QM') for k in ids if cls[k] == 'HARMLESS')
    checks.append(('C2 every HARMLESS chain ends in control or QM', c2))
    # C3
    nums = [int(k.split('.')[1]) for k in ids if k.startswith('I4.')]
    st = i4_status(nums)
    harm_t = ('equivalent to exact finite operational QM', '⟺ exact finite operational QM', '⟺ (with DerivedOI) exact QM',
              'gives HasCompositeUnitaryControl', 'gives control', 'implies PhaseFreeRichness')
    sat_t = ('derived from ImplementationLocality', 'derived from EmbeddedObservation', 'implied by ImplementationLocality',
             'implied by HasParallelReferenceExtension', 'equivalent to HasParallelReferenceExtension',
             'dagger-stable, unitary-ray-saturated generating class', 'generated by a label-invariant architecture', 'proved [K]')
    forced = {}
    bad = []
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
    print('\nC3 rows the inventory text forces:', len(forced), dict(sorted(forced.items(), key=lambda x: int(x[0].split('.')[1]))))
    checks.append(('C3 inventory status text agrees (%d forced rows; disagreements %s)' % (len(forced), bad), not bad and len(forced) >= 20))
    # C4
    t = open(R4T).read()
    m = re.search(r"TALLY Q3\s+\{'NOT': (\d+), 'SATISFIES': (\d+)\}", t)
    checks.append(('C4 R6 Q3 tally 131 SATISFIES / 68 NOT, no FAILS', bool(m) and m.group(1) == '68' and m.group(2) == '131'
                   and 'CHECK (2) Q3 column has no FAILS PASS' in t))
    # C5
    cp = classify(ROWS_PERM)
    harmful_perm = sorted(k for k in ids if cp[k] == 'HARMFUL')
    print('\nC5 countercontrol, the observer theory alone: HARMFUL rows', harmful_perm)
    checks.append(('C5 countercontrol: permTheory has DerivedOI HARMFUL', harmful_perm == ['I4.241']))
    # exact checks on the lattice
    one, I, w = (Fr(1), Fr(0)), (Fr(0), Fr(1)), (Fr(3, 5), Fr(4, 5))
    Z = (Fr(0), Fr(0))
    w2 = gauss_mul(w, w)
    w4 = gauss_mul(w2, w2)
    checks.append(('X1 w^4 = (-527 - 336 i)/625, not 1', w4 == (Fr(-527, 625), Fr(-336, 625)) and w4 != one))
    # generators on two tokens (index 2a + b): X on B, S on B, X on A, S on A, CNOT (A controls B), SWAP
    def perm(p):
        return [[one if p[i] == j else Z for j in range(4)] for i in range(4)]
    def diag(d):
        return [[d[i] if i == j else Z for j in range(4)] for i in range(4)]
    gens = [perm([1, 0, 3, 2]), diag([one, I, one, I]), perm([2, 3, 0, 1]), diag([one, one, I, I]),
            perm([0, 1, 3, 2]), perm([0, 2, 1, 3])]
    key = lambda A: tuple(tuple(x for x in row) for row in A)
    seen = {key(g): g for g in gens}
    frontier = list(gens)
    while frontier:
        nxt = []
        for A in frontier:
            for g in gens:
                B = mat_mul(A, g)
                kB = key(B)
                if kB not in seen:
                    seen[kB] = B
                    nxt.append(B)
        frontier = nxt
    grp = list(seen.values())
    all_lat = all(on_lattice(A) for A in grp)
    zph = diag([one, w, one, w])                        # 1 (x) diag(1, w)
    def ray_equal(A, B):  # A = c B for some nonzero c (exact)
        c = None
        for i in range(4):
            for j in range(4):
                a, b = A[i][j], B[i][j]
                if (a == Z) != (b == Z):
                    return False
                if b != Z:
                    # c = a / b
                    den = b[0] * b[0] + b[1] * b[1]
                    q = gauss_mul(a, (b[0] / den, -b[1] / den))
                    if c is None:
                        c = q
                    elif q != c:
                        return False
        return True
    h = Fr(1, 2)
    uj1 = [[(h, -h), (-h, -h)], [(h, -h), (h, h)]]      # (1 - i(X+Y+Z))/2
    ujB = [[Z] * 4 for _ in range(4)]
    for a in range(2):
        for b in range(2):
            for b2 in range(2):
                ujB[2 * a + b][2 * a + b2] = uj1[b][b2]
    no_zph = not any(ray_equal(A, zph) for A in grp)
    no_uj = not any(ray_equal(A, ujB) for A in grp)
    print('\nX2 group generated by X_B, S_B, X_A, S_A, CNOT, SWAP: order', len(grp))
    checks.append(('X2 every element on the fourth-root lattice', all_lat))
    checks.append(('X3 no element on the ray of 1 (x) diag(1, w) or of 1 (x) U_J', no_zph and no_uj))
    # X4 H-level: a configuration-diagonal operator with entries 1 and w on 8 configurations is no scaled partial permutation
    d8 = [one] * 7 + [w]
    checks.append(('X4 diag(1,...,1,w) has two distinct nonzero entries (no nonzero multiple has all entries equal)',
                   len(set(d8)) == 2))
    print('\nCHECKS')
    for name, ok in checks:
        print(('PASS ' if ok else 'FAIL ') + name)
    allok = all(ok for _, ok in checks)
    harmful = [k for k in ids if cls[k] == 'HARMFUL']
    if allok and not harmful:
        print('VERDICT B14-FULL: no HARMFUL row; SAT %d, HARMLESS %d, NA %d over 68 NOT REACHED rows; controls green'
              % (tally.get('SAT', 0), tally.get('HARMLESS', 0), tally.get('NA', 0)))
    elif allok:
        print('VERDICT B14-FULL: HARMFUL rows', harmful)
    else:
        print('VERDICT VOID: a control failed')


main()
