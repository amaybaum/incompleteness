"""R1 and R2 path A: the support-40 witness through L41's landed production probe.

The landed probe verification/lean/dita_index_map_probe.py is executed whole, unmodified, with its own __file__, so it
replays L41's measurements.json (control C0) before any of its functions is used here. Then, for an exponent matrix E,
its arc machinery -- orientations(E, 0, 0), enumerate_candidates, A41Family, a41_arc_summary -- gives the partition
structures holding identically on the arc SIG o u^E and its exceptional points, strictly and up to diagonal equivalence.
Writes r2a.json.
"""
import contextlib, io, json, os, random, sys, time
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
PROBE = os.path.join(REPO, 'verification', 'lean', 'dita_index_map_probe.py')
t0 = time.time()
NS = {'__name__': 'landed_production', '__file__': PROBE}
buf = io.StringIO()
try:
    with contextlib.redirect_stdout(buf):
        exec(compile(open(PROBE, encoding='utf-8').read(), PROBE, 'exec'), NS)
    exit_code = 0
except SystemExit as e:
    exit_code = e.code
last = [l for l in buf.getvalue().splitlines() if l.startswith('dita_index_map_probe:')]
C0 = exit_code in (0, None) and len(last) == 1 and ' OK -- REPLAYED' in last[0]
print('C0 landed production probe:', last, 'exit', exit_code, '(%.0fs)' % (time.time() - t0), flush=True)
g = NS
G, ONE, ZERO, SIG, gpow = g['G'], g['ONE'], g['ZERO'], g['SIG'], g['gpow']
Fr = g['Fr']
Z16 = g['Z16']

# ---- the witness, from its formula --------------------------------------------------------------
def E40_entry(i, j):
    a, b, c, d = i // 4, i % 4, j // 4, j % 4
    return -int(b == 0 and c == 0) + int(a == 2 and b % 2 == 1 and d % 2 == 0) - int(a % 2 == 0 and c % 2 == 1 and d == 0)
E40 = [[E40_entry(i, j) for j in range(16)] for i in range(16)]
def piece(f): return [[f(i // 4, i % 4, j // 4, j % 4) for j in range(16)] for i in range(16)]
P = piece(lambda a, b, c, d: int(b == 0 and c == 0))
Q = piece(lambda a, b, c, d: int(a == 2 and b % 2 == 1 and d % 2 == 0))
T = piece(lambda a, b, c, d: int(a % 2 == 0 and c % 2 == 1 and d == 0))
PA, PB, PC = g['PA'], g['PB'], g['PC']
EE = g['EE']
def support(E): return sum(1 for r in E for x in r if x)
def add(*Ms, coef=None):
    coef = coef or [1] * len(Ms)
    return [[sum(c * M[i][j] for c, M in zip(coef, Ms)) for j in range(16)] for i in range(16)]

out = {'C0': C0, 'probe_last_line': last}
# R1: straightness, two exact methods
def straight_levels(E):
    for i in range(16):
        for i2 in range(i + 1, 16):
            acc = {}
            for k in range(16):
                dd = E[i][k] - E[i2][k]; acc[dd] = acc.get(dd, ZERO) + SIG[i][k] * SIG[i2][k].conj()
            if any(v != ZERO for v in acc.values()): return False
    return True
UNITS = [G(Fr(3, 5), Fr(4, 5)), G(Fr(5, 13), Fr(12, 13)), G(Fr(8, 17), Fr(15, 17)), G(0, 1), G(-1)]
def unitary_at(E, u):
    H = [[SIG[i][j] * gpow(u, E[i][j]) for j in range(16)] for i in range(16)]
    return g['is_unitary16'](H)
def straight_points(E): return all(unitary_at(E, u) for u in UNITS)
E40_formula_check = (E40 == add(P, Q, T, coef=[-1, 1, -1]))
overlap = sorted((i, j) for i in range(16) for j in range(16) if Q[i][j] and T[i][j])
out['R1'] = {'support': support(E40), 'entries': sorted(set(x for r in E40 for x in r)), 'sum': sum(map(sum, E40)),
             'formula_equals_-P+Q-T': E40_formula_check, 'pieces_support': [support(P), support(Q), support(T)],
             'QT_overlap_cells': overlap, 'straight_levels': straight_levels(E40), 'straight_points': straight_points(E40)}
Ebad = [r[:] for r in E40]; Ebad[0][0] += 1
out['C5_one_entry_changed'] = {'straight_levels': straight_levels(Ebad), 'straight_points': straight_points(Ebad)}
print('R1', out['R1'], 'C5', out['C5_one_entry_changed'], '(%.0fs)' % (time.time() - t0), flush=True)

# ---- R2 path A ---------------------------------------------------------------------------------------
orientations, enumerate_candidates, A41Family = g['orientations'], g['enumerate_candidates'], g['A41Family']
a41_arc_summary, a41_norm, a41_pt1 = g['a41_arc_summary'], g['a41_norm'], g['a41_pt1']
def arc(E, with_at1=False):
    OR = orientations(E, Z16, Z16); cands, stats = enumerate_candidates(OR); fam = A41Family(OR, cands)
    res = {'candidates': len(cands)}
    for relaxed in (False, True):
        idn, pts = a41_arc_summary(fam, relaxed)
        r = {'identically': idn, 'exceptional': pts}
        pf = []
        for k in fam.cands:
            for F in fam.locus(k, relaxed):
                if F.dim() != 3: pf.append((F.show(), [[list(kk), list(v)] for kk, v in F.B]))
        r['exceptional_flats'] = sorted(set((s, json.dumps(b)) for s, b in pf))
        r['atm1'] = a41_norm(fam.at(a41_pt1(G(-1)), relaxed))
        if with_at1:
            at1 = a41_norm(fam.at(a41_pt1(ONE), relaxed)); r['at1'] = [len(at1), sum(x[4] for x in at1)]
        res['relaxed' if relaxed else 'strict'] = r
    return res
t1 = time.time()
out['R2A_E40'] = arc(E40, with_at1=True)
print('R2A E40:', {k: (v['identically'], v['exceptional'], v.get('at1')) for k, v in out['R2A_E40'].items() if k != 'candidates'}, 'candidates', out['R2A_E40']['candidates'], '(%.0fs)' % (time.time() - t1), flush=True)
# C1b: act 38's E through the same call path equals L41's recorded values
rec = json.load(open(os.path.join(REPO, 'verification', 'programmes', 'oi-qm', 'track-b', 'act-41-index-map-semantics', 'measurements.json')))
ee = arc(EE)
recE = rec['production']['e']
out['C1b'] = all(ee[n]['identically'] == recE[n]['identically'] and ee[n]['exceptional'] == recE[n]['exceptional'] and ee[n]['atm1'] == recE[n]['atm1'] for n in ('strict', 'relaxed'))
print('C1b act 38 arc reproduces L41:', out['C1b'], {n: ee[n]['exceptional'] for n in ('strict', 'relaxed')}, flush=True)
# C2: known Dita low-support lines are accepted (a structure holds identically)
out['C2'] = {}
for nm, M in (('A', PA), ('P', P), ('Q', Q), ('T', T)):
    r = arc(M); out['C2'][nm] = {'support': support(M), 'identically_strict': len(r['strict']['identically']), 'identically_relaxed': len(r['relaxed']['identically'])}
print('C2', out['C2'], flush=True)
# C3: gauge
rng = random.Random(4242)
al = [rng.randint(-3, 3) for _ in range(16)]; be = [rng.randint(-3, 3) for _ in range(16)]
Eg = [[E40[i][j] + al[i] + be[j] for j in range(16)] for i in range(16)]
rg = arc(Eg)
out['C3_gauge'] = {'straight': straight_levels(Eg), 'same': all(rg[n]['identically'] == out['R2A_E40'][n]['identically'] and rg[n]['exceptional'] == out['R2A_E40'][n]['exceptional'] for n in ('strict', 'relaxed')), 'alpha': al, 'beta': be}
print('C3', out['C3_gauge']['straight'], out['C3_gauge']['same'], flush=True)
# the pairwise sums of the pieces, for the record
out['pieces_pairs'] = {}
for nm, M in (('-P+Q', add(P, Q, coef=[-1, 1])), ('-P-T', add(P, T, coef=[-1, -1])), ('Q-T', add(Q, T, coef=[1, -1]))):
    r = arc(M); out['pieces_pairs'][nm] = {'straight': straight_levels(M), 'identically_strict': r['strict']['identically'], 'identically_relaxed': r['relaxed']['identically']}
print('pairs', {k: (v['straight'], len(v['identically_strict']), len(v['identically_relaxed'])) for k, v in out['pieces_pairs'].items()}, flush=True)
json.dump(out, open(os.path.join(HERE, 'r2a.json'), 'w'), indent=1, sort_keys=True)
print('done (%.0fs)' % (time.time() - t0))
