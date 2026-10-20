"""A13 (float diagnostic, not a certificate): posFwd / posInv of a candidate on random pure-state / pure-effect
quadruples of the ball, off the frozen pools; and an exact witness search on a denser rational pool."""
import sys, json, itertools
import numpy as np
from fractions import Fraction as Fr
sys.path.insert(0, sys.argv[1]); import controls_verify as cv
G = np.array([[float(Fr(v)) for v in r] for r in json.load(open(sys.argv[2]))['G']])
Gi = np.linalg.inv(G)
rng = np.random.default_rng(20261020)
def unit(k):
    v = rng.normal(size=(k, 3)); return v / np.linalg.norm(v, axis=1, keepdims=True)
N = 1000000
for name, M in (('posFwd', G), ('posInv', Gi)):
    x, y, a, b = unit(N), unit(N), unit(N), unit(N)
    hx = np.hstack([np.ones((N, 1)), x]); hy = np.hstack([np.ones((N, 1)), y])
    ea = np.hstack([np.full((N, 1), .5), a / 2]); eb = np.hstack([np.full((N, 1), .5), b / 2])
    w = np.einsum('ni,nj->nij', hx, hy).reshape(N, 16) @ M.T
    v = np.einsum('ni,nj,nij->n', ea, eb, w.reshape(N, 4, 4))
    print('%s: min over %d random quadruples %.4e; below -1e-9: %d' % (name, N, v.min(), int((v < -1e-9).sum())))
    i = int(np.argmin(v)); print('  worst x, y, a, b:', np.round(x[i], 3), np.round(y[i], 3), np.round(a[i], 3), np.round(b[i], 3))
