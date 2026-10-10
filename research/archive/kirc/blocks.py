"""Algebraic solvability of the two blocks forced by the controlled-form lemma + native NOT relations + G^2 = I.
Evidence (least squares, many restarts); a residual bounded away from 0 is evidence of no solution, a residual ~0
yields a candidate to be made exact.  p = q = (d-1)/2.
 E+ block (per N_A-parity sector, W = R^p): G = [[0, A_r^T],[A_r, B_rs]] on W (x) (u + V+), V+ = R^p, B antisym in r,s;
     twisted by D = diag(1, mu_1..mu_p): (G D)^2 = I.
 V- block (W = T+ + T- = R^2p, V- = R^(p+1)): B antisym in V- indices, B anticommutes with N_A (x) I,
     twisted by diag(mu_1..mu_p, 1): (B D)^2 = I."""
import sys, itertools, numpy as np
from scipy.optimize import least_squares
rng = np.random.default_rng(1)

def eplus(p, mu, restarts=30):
    k = p + 1; best = np.inf
    nA = p * p * p; pairs = [(r, s) for r in range(p) for s in range(r + 1, p)]; nB = len(pairs) * p * p
    Dm = np.kron(np.diag([1.] + list(mu)), np.eye(p))
    def build(x):
        A = x[:nA].reshape(p, p, p); Bv = x[nA:].reshape(len(pairs), p, p) if pairs else np.zeros((0, p, p))
        G = np.zeros((k * p, k * p))
        for r in range(p):
            G[(r + 1) * p:(r + 2) * p, 0:p] = A[r]; G[0:p, (r + 1) * p:(r + 2) * p] = A[r].T
        for i, (r, s) in enumerate(pairs):
            G[(r + 1) * p:(r + 2) * p, (s + 1) * p:(s + 2) * p] = Bv[i]
            G[(s + 1) * p:(s + 2) * p, (r + 1) * p:(r + 2) * p] = -Bv[i]
        return G
    f = lambda x: ((build(x) @ Dm) @ (build(x) @ Dm) - np.eye(k * p)).ravel()
    for _ in range(restarts):
        r = least_squares(f, rng.normal(size=nA + nB), xtol=1e-14, ftol=1e-14, gtol=1e-14, max_nfev=4000)
        best = min(best, np.sqrt(2 * r.cost))
    return best

def vminus(p, mu, restarts=30):
    m = p + 1; W = 2 * p; pairs = [(l, e) for l in range(m) for e in range(l + 1, m)]
    NA = np.diag([1.] * p + [-1.] * p)
    # entries anticommute with N_A: off-diagonal in the (T+, T-) split
    def ent(v):
        M = np.zeros((W, W)); M[:p, p:] = v[:p * p].reshape(p, p); M[p:, :p] = v[p * p:].reshape(p, p); return M
    Dm = np.kron(np.eye(W), np.diag(list(mu) + [1.]))
    def build(x):
        B = np.zeros((W * m, W * m)); x = x.reshape(len(pairs), 2 * p * p)
        for i, (l, e) in enumerate(pairs):
            E = np.zeros((m, m)); E[l, e] = 1; E[e, l] = -1
            B += np.kron(ent(x[i]), E)
        return B
    f = lambda x: ((build(x) @ Dm) @ (build(x) @ Dm) - np.eye(W * m)).ravel()
    best = np.inf
    for _ in range(restarts):
        r = least_squares(f, rng.normal(size=len(pairs) * 2 * p * p), xtol=1e-14, ftol=1e-14, gtol=1e-14, max_nfev=4000)
        best = min(best, np.sqrt(2 * r.cost))
    return best

for p in (1, 2, 3, 4):
    d = 2 * p + 1
    em = min((eplus(p, mu, restarts=12), mu) for mu in {tuple(sorted(m)) for m in itertools.product((1., -1.), repeat=p)})
    vm = min((vminus(p, mu, restarts=12), mu) for mu in {tuple(sorted(m)) for m in itertools.product((1., -1.), repeat=p)})
    print('d=%d (p=%d): E+ block best residual %.2e (mu %s);  V- block best residual %.2e (mu %s)' % (d, p, em[0], em[1], vm[0], vm[1]), flush=True)
