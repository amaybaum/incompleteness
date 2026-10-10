"""Step L: the frozen line candidate W' = [a even][c even][b odd][d odd] (the inner circle direction on the even-even blocks):
exact straight line; its 2x8 factorization at the named point; the named point's defect, 4x4 / 8x2 / 2x8 searches, cross-ratio
violations; its residual class in R and sector projection."""
import pickle, time, itertools
from lib36 import *
t0 = time.time()
src = open('stepK.py', encoding='utf-8').read()
exec(src[src.index('def is_unitary(M, s)'):src.index("for label, H in (")])
def unit_n(n): return G(Fr(n * n - 1, n * n + 1), Fr(2 * n, n * n + 1))
def gpow(u, k):
    r = ONE
    for _ in range(abs(k)): r = r * (u if k > 0 else u.conj())
    return r
U5 = G(Fr(3, 5), Fr(4, 5))
Wp = [1 if ((i // 4) % 2 == 0 and (j // 4) % 2 == 0 and (i % 4) % 2 == 1 and (j % 4) % 2 == 1) else 0 for i in range(16) for j in range(16)]
def straight_line_exact(w):
    for (i, j) in PAIRS:
        sums = {}
        for k in range(16):
            d = w[i * 16 + k] - w[j * 16 + k]; a, b = C_SIG[(i, j)][k]
            s = sums.get(d, (0, 0)); sums[d] = (s[0] + a, s[1] + b)
        if any(s != (0, 0) for s in sums.values()): return False
    return True
print("W' exact straight line:", straight_line_exact(Wp), '| in ker DF:', all(dot(r, Wp) == 0 for r in DF))
u = unit_n(60)
P = [[SIG[i][j] * gpow(u, Wp[i * 16 + j]) for j in range(16)] for i in range(16)]
print('P = SIG ∘ u^W\' Hadamard:', is_unitary(P, 16))
C, den = cvals(P); rows = df_rows(C); print('defect of P:', 256 - rank(rows, 256) - 31)
PT = [list(c) for c in zip(*P)]
for (m, n) in ((2, 8), (8, 2), (4, 4)):
    for kind, HH in (('column', P), ('row', PT)):
        ng, ors = dita_orientations(HH, m, n)
        print('   %s-Diţă %dx%d at P: admissible blocks %d | orientations %d | exact factorizations %d' % (kind, m, n, ng, len(ors), sum(1 for o in ors if o[2])))
        if (m, n) == (2, 8) and kind == 'column':
            for cp, rws, ok, flags in ors:
                if ok: print('      blocks', cp, '\n      row classes', rws)
viol = [(a, b, b2, c, c2, d) for a in range(4) for b in range(4) for b2 in range(b + 1, 4) for c in range(4) for c2 in range(c + 1, 4) for d in range(4)
        if P[4 * a + b][4 * c + d] * P[4 * a + b2][4 * c2 + d] != P[4 * a + b][4 * c2 + d] * P[4 * a + b2][4 * c + d]]
print('fixed-pairing cross-ratio violations at P: %d of 576; first: %s' % (len(viol), viol[:3]))
# the same at u = (3+4i)/5 for a small-denominator named point alternative
P5 = [[SIG[i][j] * gpow(U5, Wp[i * 16 + j]) for j in range(16)] for i in range(16)]
C5, _ = cvals(P5); print('P5 (u=(3+4i)/5): Hadamard %s, defect %d' % (is_unitary(P5, 16), 256 - rank(df_rows(C5), 256) - 31))
for (m, n) in ((2, 8), (8, 2), (4, 4)):
    for kind, HH in (('column', P5), ('row', [list(c) for c in zip(*P5)])):
        ng, ors = dita_orientations(HH, m, n)
        print('   %s-Diţă %dx%d at P5: orientations %d | exact factorizations %d' % (kind, m, n, len(ors), sum(1 for o in ors if o[2])))
# residual class of W' in R and its sector projection
B = pickle.load(open('stepB.pkl', 'rb')); Gb, Tb, Rb = B['Gb'], B['Tb'], B['Rb']
C2 = pickle.load(open('stepC2.pkl', 'rb')); spaces = C2['spaces']
basis = Gb + Tb + Rb
Rr, piv = rref(basis, 256); PIV = piv[:80]
Msub = [[Fr(basis[j][p]) for j in range(80)] for p in PIV]
aug = [Msub[i] + [Fr(1) if k == i else Fr(0) for k in range(80)] for i in range(80)]
Ri, pv = rref(aug, 160); INV = [r[80:] for r in Ri]
x = [sum(INV[j][i] * Wp[PIV[i]] for i in range(80)) for j in range(80)]
assert all(sum(x[j] * basis[j][m] for j in range(80)) == Wp[m] for m in range(256))
xR = x[57:]
print("W' coordinates: gauge part nonzero %s, T part nonzero %s, R part nonzero %s" % (any(v != 0 for v in x[:31]), any(v != 0 for v in x[31:57]), any(v != 0 for v in xR)))
for si, V in enumerate(spaces):
    d = len(V) + 1 - rank([list(a) for a in V] + [list(xR)], 23) if any(v != 0 for v in xR) else 0
    print('   R-part of W\' lies in sector %d: %s' % (si, d == 1))
# 2x8 factors at P explicitly (the first exact column factorization): X, D, Y_0, Y_1
ng, ors = dita_orientations(P, 2, 8)
for cp, rws, ok, flags in ors:
    if not ok: continue
    m, n = 2, 8
    col = {(c, d): cp[c][d] for c in range(m) for d in range(n)}; row = {(a, b): rws[b][a] for a in range(m) for b in range(n)}
    lam = {}; Y = []
    for c in range(m):
        Yc = []
        for b in range(n):
            i0 = row[(0, b)]; base = [P[i0][col[(c, d)]] for d in range(n)]; Yc.append(base)
            for a in range(m): lam[(a, b, c)] = P[row[(a, b)]][col[(c, 0)]] * base[0].conj()
        Y.append(Yc)
    X = [[lam[(a, 0, c)] for c in range(m)] for a in range(m)]; D = [[lam[(0, b, c)] for b in range(n)] for c in range(m)]
    def show(g):
        return '%s%s' % (g.a, ('+%si' % g.b) if g.b >= 0 else ('%si' % g.b))
    print('2x8 factorization at P: X =', [[show(x) for x in r] for r in X]); print('   D =', [[show(x) for x in r] for r in D])
    for c in range(2):
        print('   Y_%d:' % c)
        for r in Y[c]: print('      ', ' '.join('%18s' % show(x) for x in r))
    break
print('done (%.0fs)' % (time.time() - t0))
