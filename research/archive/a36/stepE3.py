"""Step E3: the space of quadrics on Def vanishing on every hull tangent (true hull list), mod two primes via numpy elimination,
against the 47 B-quadrics; and the rank of B-quadrics restricted to Sym^2 of each sector."""
import pickle, time, random
import numpy as np
from lib36 import *
random.seed(364); t0 = time.time()
B = pickle.load(open('stepB.pkl', 'rb')); Gb, Tb, Rb = B['Gb'], B['Tb'], B['Rb']
E = pickle.load(open('stepE.pkl', 'rb')); BB = E['BB']
F = pickle.load(open('stepF.pkl', 'rb')); hulls = F['hulls']
basis = Gb + Tb + Rb
Rr, piv = rref(basis, 256); PIV = piv[:80]
Msub = [[Fr(basis[j][p]) for j in range(80)] for p in PIV]
aug = [Msub[i] + [Fr(1) if k == i else Fr(0) for k in range(80)] for i in range(80)]
Ri, pv = rref(aug, 160); INV = [r[80:] for r in Ri]
def coords_def(v): return [sum(INV[j][i] * v[PIV[i]] for i in range(80)) for j in range(80)][31:]
idx = {}; n = 0
for i in range(49):
    for j in range(i, 49): idx[(i, j)] = n; n += 1
def modrank_np(rows, p):
    M = np.array(rows, dtype=np.int64) % p; r = 0; nr, nc = M.shape
    for c in range(nc):
        nz = np.nonzero(M[r:, c])[0]
        if len(nz) == 0: continue
        pr = r + nz[0]; M[[r, pr]] = M[[pr, r]]
        inv = pow(int(M[r, c]), p - 2, p); M[r] = (M[r] * inv) % p
        col = M[:, c].copy(); col[r] = 0
        nzr = np.nonzero(col)[0]
        if len(nzr): M[nzr] = (M[nzr] - np.outer(col[nzr], M[r])) % p
        r += 1
        if r == nr: break
    return r
def hull_constraints(vecs, p):
    cs = []
    for v in vecs:
        c = coords_def(v); den = 1
        for x in c: den = den * x.denominator // gcd(den, x.denominator)
        cs.append([int(x * den) % p for x in c])
    rows = []
    for a in range(len(cs)):
        for b in range(a, len(cs)):
            ca, cb = cs[a], cs[b]; row = [0] * 1225
            for i in range(49):
                if ca[i] == 0 and cb[i] == 0: continue
                for j in range(i, 49):
                    row[idx[(i, j)]] = (ca[i] * cb[j] + ca[j] * cb[i]) % p          # polarization: 2 c_a[i] c_b[i] on the diagonal
            rows.append(row)
    return rows
P = 2**31 - 1
uniq = [h for h in hulls if not h[0].startswith('column ((0, 2, 8, 10)') and not h[0].startswith('row ((0, 2, 8, 10)')]
par = [h for h in hulls if h not in uniq]
sample = uniq + random.sample(par, 24)
print('hulls used for the vanishing conditions: %d (6 unique orientations + 24 parity hulls)' % len(sample))
rows = []
for nm, vecs in sample: rows += hull_constraints(vecs, P)
print('constraint rows', len(rows), '(%.0fs)' % (time.time() - t0))
r1 = modrank_np(rows, P)
print('rank of the conditions mod p: %d -> quadrics vanishing on these hulls: at most %d (exactly, over F_p, for this subset)' % (r1, 1225 - r1), '(%.0fs)' % (time.time() - t0))
Bq = [[(BB[(i, j)][l] * (2 if i != j else 1)) for i in range(49) for j in range(i, 49)] for l in range(64)]
print('rank of the B-quadrics mod p:', modrank_np(Bq, P))
print('rank of conditions + B-quadrics mod p (equal to the conditions rank iff every B-quadric vanishes on the hulls):', modrank_np(rows + Bq, P))
print('done (%.0fs)' % (time.time() - t0))
