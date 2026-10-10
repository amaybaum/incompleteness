"""EQ4-P exploration x16 -- FLOATING POINT, EXPLORATION ONLY.  NOT EVIDENCE.  Never cited as a certificate.
Copy of x9 for the c = 1 cone K_tw (p13): generators e_{+b} + e_{-b}, the t-orbit (PT images), k_j = I - 2P_j + 2P_j'.
For c = 1 the condition is Euclidean self-positivity of the filter orbits: tr(W' Ad(k) W) >= 0 (same form as x9).

Question (lead-finding only).  x8 found (exact DD; hand proof in NOTES) the S_8-invariant self-dual cone
K_A = cone{ P_j + P_k (j != k),  I - 2 P_j,  I - 2 P_j + 2 P_p (p != j) } in the GHZ-diagonal sector.  If K_A were the
GHZ-diagonal section of an admissible K3, every local filter image Ad(k) W of a generator would lie in K3, and
co-self-duality (T fixes the sector) would require tr( W' Ad(k) W ) >= 0 for all generators W, W' and all local k;
equivalently the twirled filter maps preserve K_A.  Also for K_B (x8's second cone; generators P_j + P_k,
I - 2P_j + 2P_p (p in another fibre), I - 2P_j + 2P_j' (partner), I + 8 P_j).
Method: for every generator W (all G-images) against each orbit representative W', random starts + BFGS over complex
A, B, C of tr(W' Ad(A (x) B (x) C) W) / (||W'|| ||Ad(k) W||).  A clearly negative minimum is a lead only.
"""
import itertools

import numpy as np
from scipy.optimize import minimize

rng = np.random.default_rng(2026100909)


def idx(x, y, z):
    return 4 * x + 2 * y + z


P = []
for b in range(4):
    b1, b2 = b >> 1, b & 1
    for t in range(2):
        v = np.zeros(8)
        v[idx(0, b1, b2)] = 1
        v[idx(1, 1 - b1, 1 - b2)] = 1 if t == 0 else -1
        P.append(np.outer(v, v) / 2)
I8 = np.eye(8)


def gl2(p):
    return (p[0:4] + 1j * p[4:8]).reshape(2, 2)


def val(p, W, Wp):
    k = np.kron(np.kron(gl2(p[0:8]), gl2(p[8:16])), gl2(p[16:24]))
    Y = k @ W @ k.conj().T
    return np.real(np.trace(Wp @ Y)) / max(np.linalg.norm(Wp) * np.linalg.norm(Y), 1e-300)


def run(name, gens, reps, starts=6):
    worst = (np.inf, None)
    for i, W in enumerate(gens):
        for jr, Wp in reps:
            best = np.inf
            for s in range(starts):
                r = minimize(val, rng.normal(size=24), args=(W, Wp), method="BFGS",
                             options={"maxiter": 2000, "gtol": 1e-10})
                best = min(best, r.fun)
            if best < worst[0]:
                worst = (best, (i, jr))
    print("%s: %d generators x %d reps; worst normalized min tr(W' Ad(k) W) = %.6e at %s"
          % (name, len(gens), len(reps), worst[0], worst[1]), flush=True)


import itertools as _it
from itertools import permutations as _perms, product as _prod


def _act(g, v):
    w = [0] * 8
    for i in range(8):
        w[g[i]] = v[i]
    return tuple(w)


_GR = []
for _perm in _perms(range(4)):
    for _eps in _prod((0, 1), repeat=4):
        if sum(_eps) % 2 == 0:
            _GR.append(tuple(2 * _perm[b] + (t ^ _eps[b]) for b in range(4) for t in range(2)))
tvecs = sorted(set(_act(g, (1, 1, 1, 1, 1, -1, 1, -1)) for g in _GR))
kvecs = sorted(set(_act(g, (-1, 3, 1, 1, 1, 1, 1, 1)) for g in _GR))


def op_of(lam):
    return sum(lam[m] * P[m] for m in range(8))


negs = [op_of(v) for v in tvecs + kvecs]
reps = [("t", op_of((1, 1, 1, 1, 1, -1, 1, -1))), ("k", op_of((-1, 3, 1, 1, 1, 1, 1, 1))), ("p", P[0] + P[1])]
run("K_tw", negs, reps)
