"""Step M: frozen-line candidates in the nested family [a even][c even]·(r_b + s_d + λ·ex(b,d)): exact line, point at u60, defect,
4x4 / 2x8 / 8x2 searches, cross-ratio violations, residual sector."""
import pickle, time
from lib36 import *
t0 = time.time()
src = open('stepK.py', encoding='utf-8').read()
exec(src[src.index('def is_unitary(M, s)'):src.index("for label, H in (")])
def unit_n(n): return G(Fr(n * n - 1, n * n + 1), Fr(2 * n, n * n + 1))
def gpow(u, k):
    r = ONE
    for _ in range(abs(k)): r = r * (u if k > 0 else u.conj())
    return r
def straight_line_exact(w):
    for (i, j) in PAIRS:
        sums = {}
        for k in range(16):
            d = w[i * 16 + k] - w[j * 16 + k]; a, b = C_SIG[(i, j)][k]
            s = sums.get(d, (0, 0)); sums[d] = (s[0] + a, s[1] + b)
        if any(s != (0, 0) for s in sums.values()): return False
    return True
def mk(f): return [f(i // 4, i % 4, j // 4, j % 4) for i in range(16) for j in range(16)]
ee = lambda a, c: a % 2 == 0 and c % 2 == 0
cands = {
 'W_s: [a,c even][d=1]': mk(lambda a, b, c, d: 1 if ee(a, c) and d == 1 else 0),
 'W_r: [a,c even][b=1]': mk(lambda a, b, c, d: 1 if ee(a, c) and b == 1 else 0),
 'W_rs: [a,c even]([b=1]+[d=1])': mk(lambda a, b, c, d: (1 if b == 1 else 0) + (1 if d == 1 else 0) if ee(a, c) else 0),
 'W_sx: [a,c even]([d=1]+[b,d odd])': mk(lambda a, b, c, d: (1 if d == 1 else 0) + (1 if b % 2 == 1 and d % 2 == 1 else 0) if ee(a, c) else 0),
 'W_rx: [a,c even]([b=1]+[b,d odd])': mk(lambda a, b, c, d: (1 if b == 1 else 0) + (1 if b % 2 == 1 and d % 2 == 1 else 0) if ee(a, c) else 0),
}
B = pickle.load(open('stepB.pkl', 'rb')); Gb, Tb, Rb = B['Gb'], B['Tb'], B['Rb']
C2 = pickle.load(open('stepC2.pkl', 'rb')); spaces = C2['spaces']
basis = Gb + Tb + Rb
Rr, piv = rref(basis, 256); PIV = piv[:80]
Msub = [[Fr(basis[j][p]) for j in range(80)] for p in PIV]
aug = [Msub[i] + [Fr(1) if k == i else Fr(0) for k in range(80)] for i in range(80)]
Ri, pv = rref(aug, 160); INV = [r[80:] for r in Ri]
u = unit_n(60)
for name, W in cands.items():
    sl = straight_line_exact(W); ink = all(dot(r, W) == 0 for r in DF)
    print('== %s: exact line %s, in ker DF %s' % (name, sl, ink))
    if not sl: continue
    x = [sum(INV[j][i] * W[PIV[i]] for i in range(80)) for j in range(80)]; xR = x[57:]
    sec = [si for si, V in enumerate(spaces) if any(v != 0 for v in xR) and len(V) + 1 - rank([list(a) for a in V] + [list(xR)], 23) == 1]
    print('   residual part nonzero: %s; lies in sector: %s' % (any(v != 0 for v in xR), sec))
    P = [[SIG[i][j] * gpow(u, W[i * 16 + j]) for j in range(16)] for i in range(16)]
    C, den = cvals(P); print('   P at u60: Hadamard %s, defect %d' % (is_unitary(P, 16), 256 - rank(df_rows(C), 256) - 31))
    PT = [list(c) for c in zip(*P)]
    for (m, n) in ((4, 4), (2, 8), (8, 2)):
        res = []
        for kind, HH in (('col', P), ('row', PT)):
            ng, ors = dita_orientations(HH, m, n); res.append('%s %d/%d' % (kind, sum(1 for o in ors if o[2]), len(ors)))
        print('   %dx%d exact/candidates: %s' % (m, n, ', '.join(res)))
    viol = [(a, b, b2, c, c2, d) for a in range(4) for b in range(4) for b2 in range(b + 1, 4) for c in range(4) for c2 in range(c + 1, 4) for d in range(4)
            if P[4 * a + b][4 * c + d] * P[4 * a + b2][4 * c2 + d] != P[4 * a + b][4 * c2 + d] * P[4 * a + b2][4 * c + d]]
    print('   cross-ratio violations: %d; first %s (%.0fs)' % (len(viol), viol[:2], time.time() - t0))
