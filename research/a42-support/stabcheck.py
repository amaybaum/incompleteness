"""Exact check: every stabilizer element maps each relaxed census subspace L_S onto some L_S' (equal dimension,
containment), and the induced map on the 18 structures is a bijection."""
import numpy as np, math, time
from fractions import Fraction as Fr
from lib42 import *
from linalg42 import nullspace
t0 = time.time()
def intv(v):
    den = 1
    for x in v: den = den * Fr(x).denominator // math.gcd(den, Fr(x).denominator)
    return [int(Fr(x) * den) for x in v]
KEYS = [(nm, tr) for nm, tr, s in STRUCTS]
NSB = {k: np.array([intv(v) for v in nullspace(SMAT[(k[0], k[1], True)].tolist(), 256)], dtype=object) for k in KEYS}
DIM = {k: len(v) for k, v in NSB.items()}
print('dims', DIM, '%.0fs' % (time.time() - t0), flush=True)
# containments among census subspaces
cont = [(a, b) for a in KEYS for b in KEYS if a != b and not (SMAT[(b[0], b[1], True)].astype(object).dot(NSB[a].T) != 0).any()]
print('containments L_a <= L_b among the 18:', cont, flush=True)
bad = 0; perms = set()
for n, (p, s_) in enumerate(elems):
    img = {}
    for a in KEYS:
        B = NSB[a]
        # transport each basis vector: out[p[t]] = s * v[t]
        T = np.zeros_like(B)
        T[:, list(p)] = B * s_
        tg = [b for b in KEYS if DIM[b] == DIM[a] and not (SMAT[(b[0], b[1], True)].astype(object).dot(T.T) != 0).any()]
        img[a] = tg
    ok = all(len(v) == 1 for v in img.values()) and len(set(v[0] for v in img.values())) == 18
    if not ok: bad += 1
    else: perms.add(tuple(img[a][0] for a in KEYS))
print('elements failing', bad, 'of', len(elems), '; distinct induced permutations', len(perms), '%.0fs' % (time.time() - t0))
