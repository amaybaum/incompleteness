"""Step E4: quadrics on Def vanishing on the tangent of every one of the 492 hulls, incrementally over F_p (p = 2^25 - 39), against the 47 B-quadrics.
rank_Fp <= rank_Q, so the count is an upper bound on the number over Q; the B-quadrics are checked to vanish exactly (over Q) on all hulls."""
import pickle, time, random
import numpy as np
from lib36 import *
t0 = time.time()
B = pickle.load(open('stepB.pkl', 'rb')); Gb, Tb, Rb = B['Gb'], B['Tb'], B['Rb']
E = pickle.load(open('stepE.pkl', 'rb')); BB = E['BB']
F = pickle.load(open('stepF.pkl', 'rb')); hulls = F['hulls']
basis = Gb + Tb + Rb
Rr, piv = rref(basis, 256); PIV = piv[:80]
Msub = [[Fr(basis[j][p]) for j in range(80)] for p in PIV]
aug = [Msub[i] + [Fr(1) if k == i else Fr(0) for k in range(80)] for i in range(80)]
Ri, pv = rref(aug, 160); INV = [r[80:] for r in Ri]
def coords_def(v): return [sum(INV[j][i] * v[PIV[i]] for i in range(80)) for j in range(80)][31:]
p = 2**25 - 39
idx = {}; n = 0
for i in range(49):
    for j in range(i, 49): idx[(i, j)] = n; n += 1
def hull_rows(vecs):
    cs = []
    for v in vecs:
        c = coords_def(v); den = 1
        for x in c: den = den * x.denominator // gcd(den, x.denominator)
        cs.append([int(x * den) % p for x in c])
    C = np.array(cs, dtype=np.int64)                          # m x 49
    rows = []
    for a in range(len(cs)):
        for b in range(a, len(cs)):
            outer = (np.outer(C[a], C[b]) + np.outer(C[b], C[a])) % p     # 49x49 symmetric, diagonal doubled
            rows.append([int(outer[i, j]) for i in range(49) for j in range(i, 49)])
    return np.array(rows, dtype=np.int64) % p
def nullspace_mod(M):
    """basis of {x : M x = 0} over F_p, rows as numpy int64"""
    M = M.copy() % p; nr, nc = M.shape; r = 0; pivs = []
    for c in range(nc):
        if r >= nr: break
        nz = np.nonzero(M[r:, c])[0]
        if len(nz) == 0: continue
        pr = r + nz[0]; M[[r, pr]] = M[[pr, r]]
        inv = pow(int(M[r, c]), p - 2, p); M[r] = (M[r] * inv) % p
        col = M[:, c].copy(); col[r] = 0
        nzr = np.nonzero(col)[0]
        if len(nzr): M[nzr] = (M[nzr] - np.outer(col[nzr], M[r])) % p
        pivs.append(c); r += 1
    free = [c for c in range(nc) if c not in pivs]
    basis_ = []
    for f in free:
        x = np.zeros(nc, dtype=np.int64); x[f] = 1
        for i, pc in enumerate(pivs): x[pc] = (-M[i, f]) % p
        basis_.append(x)
    return np.array(basis_, dtype=np.int64) if basis_ else np.zeros((0, nc), dtype=np.int64)
V = None
for k, (nm, vecs) in enumerate(hulls):
    R_ = hull_rows(vecs)
    if V is None:
        V = nullspace_mod(R_)                                 # rows: basis of vanishing quadrics
    else:
        M = (R_ @ V.T) % p                                    # conditions restricted to V: rows x dimV
        Nn = nullspace_mod(M)                                 # combos of V's basis
        V = (Nn @ V) % p if len(Nn) else np.zeros((0, 1225), dtype=np.int64)
    if k % 50 == 0 or k == len(hulls) - 1: print('after %d hulls: vanishing quadrics (mod p) = %d (%.0fs)' % (k + 1, len(V), time.time() - t0))
print('quadrics vanishing on every hull tangent (mod p, upper bound over Q):', len(V))
# B-quadrics: vanish exactly on every hull over Q? (polarized: B(t,t') = 0 exactly, already verified in step F as D^2F = 0); their span mod p
Bq = np.array([[(BB[(i, j)][l] * (2 if i != j else 1)) % p for i in range(49) for j in range(i, 49)] for l in range(64)], dtype=np.int64)
rB = 1225 - len(nullspace_mod(Bq.T.copy() if False else Bq)) if False else None
# rank of Bq mod p
def rank_mod(M):
    return M.shape[1] - len(nullspace_mod(M))
print('rank of B-quadrics mod p:', rank_mod(Bq))
# are the B-quadrics inside V? check each: Bq row in row-span of V  <=>  rank([V; Bq]) == rank(V)
VB = np.vstack([V, Bq]) % p
print('rank(V) = %d, rank([V; B]) = %d -> B-quadrics inside the vanishing space: %s' % (rank_mod(V), rank_mod(VB), rank_mod(VB) == rank_mod(V)))
print('done (%.0fs)' % (time.time() - t0))
