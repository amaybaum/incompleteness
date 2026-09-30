"""Exact checks of the finite ingredients of the pruning lemmas (see NOTE.md).
 L1 minimal vanishing sets of every row pair have size 2 or 6 (so no level set of a pair difference is a singleton).
 L2 (Lemma U ingredient) msize[i][Z] >= ceil(16 / (16 - |Z|)) for every row i and every row set Z not containing i
    (the Donoho-Stark bound, proved in the note, checked here against the exact tables).
 L3 the sign-transported stabilizer preserves SIG up to dephasing (all 1024 elements), and maps straight lines to
    straight lines (checked on A, B, C, the act-38 witness under all elements).
 L4 Lemma P on given {0,1} straight matrices: support = 16 rank(SIG o E), exact rank over Q(i)."""
import numpy as np, math, itertools, sys
from lib42 import *
from dfs42 import VT, PC
ok = True
def rep(name, cond):
    global ok
    print(('PASS ' if cond else 'FAIL ') + name, flush=True); ok &= bool(cond)
# L1
sizes = set()
for i in range(16):
    for i2 in range(i + 1, 16):
        V = VT[i, i2]; ms = sorted(np.flatnonzero(V)[1:].tolist(), key=lambda x: PC[x]); mins = []
        for m in ms:
            if not any((mm & m) == mm for mm in mins): mins.append(m)
        sizes |= set(int(PC[m]) for m in mins)
rep('L1 minimal vanishing set sizes over all 120 pairs = {2, 6}: %s' % sorted(sizes), sizes == {2, 6})
# L2
msize = np.load('msize.npy'); bad = 0
for i in range(16):
    for Z in range(1 << 16):
        if (Z >> i) & 1: continue
        r = 16 - bin(Z).count('1')
        if msize[i, Z] < math.ceil(16 / r): bad += 1
rep('L2 msize >= ceil(16/r) for all 16 x 2^15 (row, zero set) pairs; violations %d' % bad, bad == 0)
# L3
def deph16(M):
    M = [[M[i][j] * M[i][0].conj() for j in range(16)] for i in range(16)]
    return [[M[i][j] * M[0][j].conj() for j in range(16)] for i in range(16)]
def key16(M): return tuple(x.key() for r in M for x in r)
K0 = key16(deph16(SIG)); good = 0
for p, s_ in elems:
    out = [[None] * 16 for _ in range(16)]
    for t in range(256):
        i, j = divmod(t, 16); i2, j2 = divmod(p[t], 16); out[i2][j2] = SIG[i][j] if s_ == 1 else SIG[i][j].conj()
    good += key16(deph16(out)) == K0
rep('L3a all %d stabilizer elements fix SIG up to dephasing (sign -1 with conjugation): %d' % (len(elems), good), good == len(elems))
cnt = sum(straight(stab_apply(e, E)) for e in elems for E in (A38, B38, C38, WIT38))
rep('L3b images of A, B, C, witness under all elements straight: %d / %d' % (cnt, 4 * len(elems)), cnt == 4 * len(elems))
# L4
def rank_gauss(M):
    M = [r[:] for r in M]; rk = 0; n = len(M)
    for c in range(n):
        p = next((i for i in range(rk, n) if M[i][c] != ZERO), None)
        if p is None: continue
        M[rk], M[p] = M[p], M[rk]
        pv = M[rk][c]; inv = G(pv.a / pv.norm2(), -pv.b / pv.norm2())
        for i in range(n):
            if i != rk and M[i][c] != ZERO:
                f = M[i][c] * inv; M[i] = [x - f * y for x, y in zip(M[i], M[rk])]
        rk += 1
    return rk
def lemmaP(E):
    return support(E) == 16 * rank_gauss([[SIG[i][j] if E[i][j] else ZERO for j in range(16)] for i in range(16)])
rep('L4 Lemma P on A, B, C, witness (ranks 1,1,1,3)', all(lemmaP(E) for E in (A38, B38, C38, WIT38)))
if len(sys.argv) > 1:
    import pickle
    for f in sys.argv[1:]:
        d = pickle.load(open(f, 'rb')); X = d['X']
        good = sum(lemmaP(X[k].reshape(16, 16).tolist()) for k in range(len(X)))
        rep('L4 Lemma P on all %d leaves of %s: %d' % (len(X), f, good), good == len(X))
print('ALL PASS' if ok else 'SOME FAIL')
