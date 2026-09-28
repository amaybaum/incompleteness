"""Orbit closure of the 18 relaxed census subspaces under the stabilizer (transport of E: out[p[t]] = s*E[t]).
Subspaces are deduplicated by the reduced row echelon form of their equation row space modulo two primes;
each family member keeps an exact integer equation matrix (a transported census matrix)."""
import numpy as np, time, pickle, collections
from lib42 import *
t0 = time.time()
def rref_mod(M, p):
    M = M.copy() % p; r = 0; rows, cols = M.shape
    for c in range(cols):
        if r == rows: break
        nz = np.flatnonzero(M[r:, c])
        if len(nz) == 0: continue
        k = r + nz[0]; M[[r, k]] = M[[k, r]]
        M[r] = (M[r] * pow(int(M[r, c]), p - 2, p)) % p
        others = np.flatnonzero(M[:, c]); others = others[others != r]
        if len(others): M[others] = (M[others] - np.outer(M[others, c], M[r])) % p
        r += 1
    return M[:r]
def key(M): return tuple(rref_mod(M.astype(np.int64), p).tobytes() for p in (32749, 32719))
KEYS = [(nm, tr) for nm, tr, s in STRUCTS]
fam = {}
for k in KEYS:
    fam[key(SMAT[(k[0], k[1], True)])] = (k, None, SMAT[(k[0], k[1], True)])
print('18 distinct:', len(fam), '%.0fs' % (time.time() - t0), flush=True)
for n, (p, s_) in enumerate(elems):
    for k in KEYS:
        M = SMAT[(k[0], k[1], True)]
        M2 = np.zeros_like(M); M2[:, list(p)] = M     # eq'(sigma E) = eq(E)
        kk = key(M2)
        if kk not in fam: fam[kk] = (k, n, M2)
    if n % 128 == 0: print(n, 'family size', len(fam), '%.0fs' % (time.time() - t0), flush=True)
print('closure size', len(fam), flush=True)
pickle.dump([v for v in fam.values()], open('closure.pkl', 'wb'))
print(collections.Counter(v[0] for v in fam.values()))
