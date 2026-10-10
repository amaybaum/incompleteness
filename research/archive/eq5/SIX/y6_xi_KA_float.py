"""EQ4-SIX exploration y6 -- FLOATING POINT, EXPLORATION ONLY.  NOT EVIDENCE.  Never cited as a certificate.

Sector Xi (see y5).  K_A fixes the Xi-profile on the rho = 1 locus (rho = d0 d2^3 / (d3 d1^3)) to
phi_A(u0, u1) = min(u0 + u1, 3 u1, u0/2 + 3 u1/2)  (u0 = sqrt(d0 d3), u1 = sqrt(d1 d2)),
self-dual there (NOTES).  Candidate rho-independent extension C_A = {|c| <= phi_A(u0, u1)}: self-dual in Xi, contains
Tw_Xi(BS), W3 and kappa, GHZ-free, invariant under all diagonal filters.  Question (lead only): is C_A invariant under
the twirled non-diagonal filters M_k = Tw_Xi o Ad(k)?  Random boundary points and random k; then BFGS maximization of
the violation ratio |c'| / phi_A(d') over k for the worst boundary points.  Same for QM as a control (ratio <= 1).
"""
import sys

import numpy as np
from scipy.optimize import minimize

rng = np.random.default_rng(2026100906)
W = np.array([bin(a).count("1") for a in range(8)])


def xi_op(d, c):
    X = np.diag(d[W]).astype(complex)
    X[0, 7] = c
    X[7, 0] = np.conj(c)
    return X


def tw(X):
    d = np.array([np.real(np.mean([X[a, a] for a in range(8) if W[a] == w])) for w in range(4)])
    return d, X[0, 7]


def phiA(d):
    if np.any(d < -1e-14):
        return -np.inf
    d = np.maximum(d, 0)
    u0 = np.sqrt(d[0] * d[3])
    u1 = np.sqrt(d[1] * d[2])
    return min(u0 + u1, 3 * u1, 0.5 * u0 + 1.5 * u1)


def phiQ(d):
    return np.sqrt(max(d[0], 0) * max(d[3], 0))


def kmat(p):
    Ms = [(p[8 * i:8 * i + 4] + 1j * p[8 * i + 4:8 * i + 8]).reshape(2, 2) for i in range(3)]
    return np.kron(np.kron(Ms[0], Ms[1]), Ms[2])


def ratio(p, d, c, phi):
    k = kmat(p)
    d2, c2 = tw(k @ xi_op(d, c) @ k.conj().T)
    ph = phi(d2)
    if ph <= 0:
        return 0.0 if abs(c2) < 1e-12 else 1e6
    return abs(c2) / ph


for name, phi in (("QM", phiQ), ("C_A", phiA)):
    pts = []
    worst = 0.0
    for _ in range(6000):
        d = np.exp(rng.normal(size=4) * 1.5)
        c = phi(d) * np.exp(2j * np.pi * rng.random())
        p = rng.normal(size=24)
        v = ratio(p, d, c, phi)
        pts.append((v, d, c))
        worst = max(worst, v)
    pts.sort(key=lambda t: -t[0])
    best = 0.0
    for v, d, c in pts[:40]:
        for _ in range(3):
            r = minimize(lambda p: -ratio(p, d, c, phi), rng.normal(size=24), method="Nelder-Mead",
                         options={"maxiter": 6000, "xatol": 1e-10, "fatol": 1e-12})
            best = max(best, -r.fun)
    print("%s: random max ratio %.4f; optimized max ratio %.4f (<= 1 means invariant)" % (name, worst, best), flush=True)
# special points: W3 and kappa under optimized filters
for nm, d, c in (("W3", np.array([0, .5, .5, 0]), .5), ("kappa", np.array([.5, .5, .5, .5]), 1.0)):
    best = 0.0
    for _ in range(20):
        r = minimize(lambda p: -ratio(p, d, c, phiA), rng.normal(size=24), method="Nelder-Mead",
                     options={"maxiter": 6000})
        best = max(best, -r.fun)
    print("C_A, %s orbit: optimized max ratio %.4f" % (nm, best), flush=True)
print("done", file=sys.stderr)
