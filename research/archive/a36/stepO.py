"""Step O: frozen constants for the named point P = SIG ∘ u60^W_rs: cross-ratio values at violation sites (Gaussian rationals),
the 2x8 block structure, the counts at SIG and P for all three sizes (col/row), and u60 arithmetic."""
import time
from lib36 import *
src = open('stepK.py', encoding='utf-8').read()
exec(src[src.index('def is_unitary(M, s)'):src.index("for label, H in (")])
def unit_n(n): return G(Fr(n * n - 1, n * n + 1), Fr(2 * n, n * n + 1))
def gpow(u, k):
    r = ONE
    for _ in range(abs(k)): r = r * (u if k > 0 else u.conj())
    return r
u = unit_n(60); print('u60 =', u.a, '+', u.b, 'i ; |u|^2 =', u.norm2())
W = [((1 if (i % 4) == 1 else 0) + (1 if (j % 4) == 1 else 0)) if ((i // 4) % 2 == 0 and (j // 4) % 2 == 0) else 0 for i in range(16) for j in range(16)]
P = [[SIG[i][j] * gpow(u, W[i * 16 + j]) for j in range(16)] for i in range(16)]
# gram P i j k = star (P i j) * P i k (scaled: entries of P here are 4x the frozen ones; frozen gram = (1/16) * this)
def gram(H, i, j, k): return H[i][j].conj() * H[i][k]
sites = []
for a in range(4):
    for b in range(4):
        for b2 in range(4):
            if b2 == b: continue
            for c in range(4):
                for c2 in range(4):
                    if c2 == c: continue
                    for d in range(4):
                        i1, i2, j1, j2 = 4 * a + b, 4 * a + b2, 4 * c + d, 4 * c2 + d
                        v = gram(P, i1, j1, j2) * gram(P, i2, j2, j1)     # scaled by 16*16 = 256 relative to frozen (1/256 at product points)
                        if v != G(1): sites.append(((a, b, b2, c, c2, d), v))
print('violation sites (ordered, all (b,b\'),(c,c\') ordered pairs):', len(sites))
from collections import Counter
print('distinct values (scaled by 256):', Counter(str((s[1].a, s[1].b)) for s in sites).most_common(6))
print('first sites:', [(s[0], (str(s[1].a), str(s[1].b))) for s in sites[:4]])
# nicest value: u^2? u^-2? compare
for k in (-2, -1, 1, 2):
    v = gpow(u, k); print('  u^%d = (%s, %s)' % (k, v.a, v.b))
# counts at SIG and P
for label, H in (('SIG', SIG), ('P', P)):
    HT = [list(c) for c in zip(*H)]
    for (m, n) in ((2, 8), (8, 2), (4, 4)):
        out = []
        for kind, HH in (('col', H), ('row', HT)):
            ng, ors = dita_orientations(HH, m, n); out.append('%s cand %d exact %d' % (kind, len(ors), sum(1 for o in ors if o[2])))
            if label == 'P' and (m, n) == (2, 8):
                for cp, rws, ok, fl in ors: print('     %s 2x8 blocks %s classes %s exact %s' % (kind, cp, rws, ok))
        print('%s %dx%d: %s' % (label, m, n, ' | '.join(out)))
print('defect P:', 256 - rank(df_rows(cvals(P)[0]), 256) - 31)
