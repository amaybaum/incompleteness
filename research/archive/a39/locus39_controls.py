"""Controls on the exact Dita-locus measurement (read-only). Independent check: act 36's numeric exhaustive structure search
with factor unitarity (dita_orientations), run directly on the exact Gaussian-rational matrix H3(u1, u2, u3), compared with the
structures the flat calculus predicts at that point."""
import pickle, sys, time, os
from fractions import Fraction as Fr
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from flats import Flat, TORUS, V0
src = open('probe38_landed.py', encoding='utf-8').read()
NS = {'__name__': 'h'}; exec(compile(src[:src.index("print('== 1. realizability")], 'h', 'exec'), NS)
G, ONE, I_, z, w, SIG, EA, EB, EC, SHAPES = [NS[k] for k in ('G', 'ONE', 'I_', 'z', 'w', 'SIG', 'EA', 'EB', 'EC', 'SHAPES')]
dita_orientations = NS['dita_orientations']
res = pickle.load(open('locus39.pkl', 'rb'))['res']
t0 = time.time()
def val(v):
    p, q, r = v; out = ONE
    for _ in range(p % 4): out = out * I_
    for _ in range(abs(q)): out = out * (z if q > 0 else z.conj())
    for _ in range(abs(r)): out = out * (w if r > 0 else w.conj())
    return out
def upow(u, k):
    out = ONE
    for x, e in zip(u, k):
        for _ in range(abs(e)): out = out * (x if e > 0 else x.conj())
    return out
def on(B, u): return B is not None and all(upow(u, k) == val(v) for k, v in B)
def H3(u):
    def gp(x, k): return x if k else ONE
    return [[SIG[i][j] * gp(u[0], EA(i, j)) * gp(u[1], EB(i, j)) * gp(u[2], EC(i, j)) for j in range(16)] for i in range(16)]
fails = []
def check(name, got, want):
    ok = got == want; print('  %s %s: %s' % ('PASS' if ok else 'FAIL', name, got))
    if not ok: fails.append(name)

# 1. the union of the loci is five coordinate 2-tori
two = sorted(set(Flat.of(Bs).describe() for c, Bs, Br in res if Bs is not None and Flat.of(Bs).dim() == 2))
print('\n'.join('    ' + x for x in two))
check('strict and relaxed loci coincide for every candidate', all(Bs == Br for c, Bs, Br in res), True)
cover = [Flat.of(Bs) for c, Bs, Br in res if Bs is not None and Flat.of(Bs).dim() == 2]
check('every nonempty locus lies in one of the 2-dimensional ones', all(any(F.contains(Flat.of(Bs)) for F in cover) for c, Bs, Br in res if Bs is not None), True)
# 2. diagonal restriction
diag = set()
for c, Bs, Br in res:
    if Bs is None: continue
    try:
        F = Flat.of(Bs).meet(Flat().add((1, -1, 0), V0).add((0, 1, -1), V0))
        diag.add(F.describe())
    except Exception as e:
        pass
check('restricted to the diagonal u1 = u2 = u3, the loci are the points u = 1 and u = -1 (act 38)', sorted(diag), sorted(set(['dim 0, 1 component(s), equations %s' % x for x in (["u^(1, 0, 0) = 1", "u^(0, 1, 0) = 1", "u^(0, 0, 1) = 1"], ["u^(1, 0, 0) = i^2", "u^(0, 1, 0) = i^2", "u^(0, 0, 1) = i^2"])])))
# 3. structures at the base point and at -1
P1, PM = (ONE, ONE, ONE), (G(-1), G(-1), G(-1))
check('structures at (1, 1, 1) (act 38: 18, the census)', sum(on(Bs, P1) for c, Bs, Br in res), 18)
atm = sorted((c[0], c[1]) for c, Bs, Br in res if on(Bs, PM))
check('structures at (-1, -1, -1) (act 38: one 2 x 8 in each orientation)', atm, [('column', (2, 8)), ('row', (2, 8))])
# 4. independent numeric exhaustive search at exact points
U5, U17, U29, U25 = G(Fr(3, 5), Fr(4, 5)), G(Fr(8, 17), Fr(15, 17)), G(Fr(20, 29), Fr(21, 29)), G(Fr(7, 25), Fr(24, 25))
M1 = G(-1)
PTS = [('generic', (U5, U17, U29)), ('generic2', (U25, I_, U5)), ('u1=1', (ONE, U5, U17)), ('u1=-1', (M1, U5, U17)), ('u2=1', (U5, ONE, U17)),
       ('u2=-1 (not in the locus)', (U5, M1, U17)), ('u3=1', (U5, U17, ONE)), ('u3=-1', (U5, U17, M1)), ('u1=i (not)', (I_, U5, U17)),
       ('u1=1,u3=-1', (ONE, U29, M1)), ('u2=1,u3=1', (U29, ONE, ONE)), ('u1=-1,u2=1', (M1, ONE, U25)), ('(1,1,1)', P1), ('(-1,-1,-1)', PM),
       ('(-1,1,1)', (M1, ONE, ONE)), ('(1,1,-1)', (ONE, ONE, M1)), ('(1,-1,1)', (ONE, M1, ONE))]
bad = []
for nm, u in PTS:
    H = H3(u); HT = [list(c) for c in zip(*H)]
    got = set()
    for form, M in (('column', H), ('row', HT)):
        for mn in SHAPES:
            for cp, rows, ok, X, Y in dita_orientations(M, *mn):
                if ok: got.add((form, mn, tuple(cp), tuple(rows)))
    pred = set((c[0], c[1], tuple(c[2]), tuple(c[3])) for c, Bs, Br in res if on(Bs, u))
    print('    %-26s numeric %2d  predicted %2d  %s  (%.0fs)' % (nm, len(got), len(pred), 'agree' if got == pred else 'DISAGREE', time.time() - t0), flush=True)
    if got != pred: bad.append(nm)
check('the numeric exhaustive search agrees with the flat calculus at every test point', bad, [])
print('locus39_controls:', 'FAILED %s' % fails if fails else 'OK')
