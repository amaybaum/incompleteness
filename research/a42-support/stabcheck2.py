import numpy as np, math, time, collections
from fractions import Fraction as Fr
from lib42 import *
from linalg42 import nullspace
def intv(v):
    den = 1
    for x in v: den = den * Fr(x).denominator // math.gcd(den, Fr(x).denominator)
    return [int(Fr(x) * den) for x in v]
KEYS = [(nm, tr) for nm, tr, s in STRUCTS]
NSB = {k: np.array([intv(v) for v in nullspace(SMAT[(k[0], k[1], True)].tolist(), 256)], dtype=np.int64) for k in KEYS}
print('max basis entry', max(np.abs(b).max() for b in NSB.values()))
res = collections.Counter(); fails = []
for n, (p, s_) in enumerate(elems):
    img = {}
    for a in KEYS:
        T = np.zeros_like(NSB[a]); T[:, list(p)] = NSB[a] * s_
        img[a] = [b for b in KEYS if len(NSB[b]) == len(NSB[a]) and not (SMAT[(b[0], b[1], True)] @ T.T).any()]
    ok = all(len(v) == 1 for v in img.values()) and len(set(v[0] for v in img.values())) == 18
    res[ok] += 1
    if not ok and len(fails) < 3: fails.append((n, p[:20], s_, {a: v for a, v in img.items() if len(v) != 1}))
print(res); print(fails)
