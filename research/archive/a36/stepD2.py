"""Step D2: every column-Diţă and row-Diţă orientation through the point, verified as an exact factorization with flat unitary
factors, with its tangent space at the point; the span of all orientations' tangents; the residual beyond them."""
import pickle, time, itertools
from lib36 import *
t0 = time.time()
A = pickle.load(open('stepA.pkl', 'rb')); K, LN = A['K'], A['LN']
B2 = pickle.load(open('stepB2.pkl', 'rb')); Tc, Tr = B2['Tc'], B2['Tr']
def prop_partition(H, S):
    keys = {}
    for i in range(16):
        base = H[i][S[0]]
        keys.setdefault(tuple((H[i][s] * base.conj()).key() for s in S), []).append(i)
    return sorted(tuple(v) for v in keys.values())
def orientations_of(H):
    good = {}
    for S in itertools.combinations(range(16), 4):
        P = prop_partition(H, S)
        if all(len(cl) == 4 for cl in P): good[S] = P
    parts = []
    def rec(rem, chosen):
        if not rem: parts.append(tuple(chosen)); return
        first = min(rem)
        for S in good:
            if first in S and set(S) <= rem: rec(rem - set(S), chosen + [S])
    rec(set(range(16)), [])
    out = []
    for cp in parts:
        cls = {i: tuple(next(ci for ci, cl in enumerate(good[S]) if i in cl) for S in cp) for i in range(16)}
        groups = {}
        for i in range(16): groups.setdefault(cls[i], []).append(i)
        rows = sorted(tuple(v) for v in groups.values())
        if all(len(g) == 4 for g in rows): out.append((cp, rows))
    return out
def is_hadamard4(M):
    for i in range(4):
        for j in range(4):
            s = ZERO
            for k in range(4): s = s + M[i][k] * M[j][k].conj()
            if s != (G(4) if i == j else ZERO): return False
    return all(x.norm2() == 1 for r in M for x in r)
def ker4(M):
    rows = []
    for i in range(4):
        for j in range(i + 1, 4):
            re = [Fr(0)] * 16; im = [Fr(0)] * 16
            for k in range(4):
                c = M[i][k] * M[j][k].conj()
                re[i * 4 + k] -= c.b; re[j * 4 + k] += c.b; im[i * 4 + k] += c.a; im[j * 4 + k] -= c.a
            rows.append(intvec(re)); rows.append(intvec(im))
    return nullspace(rows, 16)
def factor_and_tangent(H, cp, rows, transposed=False):
    col = {(c, d): cp[c][d] for c in range(4) for d in range(4)}
    row = {(a, b): rows[b][a] for a in range(4) for b in range(4)}
    Y = []; lam = {}
    for c in range(4):
        Yc = []
        for b in range(4):
            i0 = row[(0, b)]
            base = [H[i0][col[(c, d)]] for d in range(4)]
            Yc.append(base)
            for a in range(4):
                i = row[(a, b)]
                ratios = set((H[i][col[(c, d)]] * base[d].conj()).key() for d in range(4))
                assert len(ratios) == 1, 'rows not proportional'
                lam[(a, b, c)] = H[i][col[(c, 0)]] * base[0].conj()
        Y.append(Yc)
    ok_rank1 = all(lam[(a, b, c)] == lam[(a, 0, c)] * lam[(0, b, c)] for a in range(4) for b in range(4) for c in range(4))
    X = [[lam[(a, 0, c)] for c in range(4)] for a in range(4)]
    D = [[lam[(0, b, c)] for b in range(4)] for c in range(4)]
    okX = is_hadamard4(X); okY = all(is_hadamard4(Yc) for Yc in Y)
    okH = all(H[row[(a, b)]][col[(c, d)]] == X[a][c] * D[c][b] * Y[c][b][d] for a in range(4) for b in range(4) for c in range(4) for d in range(4))
    vecs = []
    for xi in ker4(X):
        v = [0] * 256
        for a in range(4):
            for b in range(4):
                for c in range(4):
                    for d in range(4): v[row[(a, b)] * 16 + col[(c, d)]] = xi[a * 4 + c]
        vecs.append(v)
    for c in range(4):
        for b in range(4):
            v = [0] * 256
            for a in range(4):
                for d in range(4): v[row[(a, b)] * 16 + col[(c, d)]] = 1
            vecs.append(v)
    for c in range(4):
        for eta in ker4(Y[c]):
            v = [0] * 256
            for a in range(4):
                for b in range(4):
                    for d in range(4): v[row[(a, b)] * 16 + col[(c, d)]] = eta[b * 4 + d]
            vecs.append(v)
    if transposed:
        vecs = [[v[(m % 16) * 16 + m // 16] for m in range(256)] for v in vecs]
    return ok_rank1 and okX and okY and okH, vecs, (ok_rank1, okX, okY, okH)
HT = [list(c) for c in zip(*SIG)]
results = []
for kind, H, tr in (('column', SIG, False), ('row', HT, True)):
    ors = orientations_of(H)
    print('%s-Diţă candidate orientations through the point: %d' % (kind, len(ors)))
    for cp, rows in ors:
        ok, vecs, flags = factor_and_tangent(H, cp, rows, transposed=tr)
        rk = rank(GAUGE + vecs) - 31
        indf = all(dot(r, v) == 0 for r in DF for v in vecs)
        print('  blocks %s rows %s | factorization %s %s | tangent rank mod gauge %d | in ker DF %s' % (cp, rows, 'OK' if ok else 'FAILS', flags, rk, indf))
        results.append((kind, cp, rows, ok, vecs))
allv = [v for (_, _, _, ok, vecs) in results if ok for v in vecs]
print('standard column orientation reproduces T_c: %s' % (rank(GAUGE + results[0][4] + Tc) - 31 == rank(GAUGE + Tc) - 31 == rank(GAUGE + results[0][4]) - 31))
print('span of all verified orientations mod gauge: %d of 49; residual beyond all known Diţă orientations through the point: %d' % (rank(GAUGE + allv) - 31, 49 - (rank(GAUGE + allv) - 31)))
pickle.dump({'results': results}, open('stepD2.pkl', 'wb'))
print('done (%.0fs)' % (time.time() - t0))
