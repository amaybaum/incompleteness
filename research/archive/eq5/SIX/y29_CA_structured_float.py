"""EQ4-SIX exploration y29 -- FLOATING POINT, EXPLORATION ONLY.  NOT EVIDENCE.  Never cited as a certificate.

Question (lead only).  y20 (random filters exp(H) with large H) let overflowed values into its minima (y28: its t1
W3 value -0.333 is an artifact; its countercontrols -5.0 are suspect), so its claims about the C_A boundary points
X_t are re-done here with y26's well-conditioned structured starts (one-qubit Cliffords times exp(eps H),
eps in {0, 0.02, 0.1, 0.3, 1}), non-finite values discarded.  For X_t = (d_t, phi_A(u(d_t))) at
t1 = (4,1,1,1), t3 = (1,1,2,2), t5 = (1,2,1,1):
  (i)  min over k of <X_t, Ad(k) g>/tr(Ad(k) g), g in {W3, kappa, omega}   (X_t in Lift(K_A)*?)
  (ii) min over k of <X_t, Ad(k) X_t>/tr(Ad(k) X_t)                       (self-positive orbit?)
Countercontrol: X_t with the coherence scaled by 1.05 must give a negative value in (i).
DECISION RULE (fixed before the first run; lead only): "X_t in Lift(K_A)* with a self-positive orbit (lead)" iff
every minimum is >= -1e-7 and the countercontrol is negative; "X_t excluded" iff some minimum < -1e-5.
"""

import sys

import numpy as np
from scipy.linalg import expm
from scipy.optimize import minimize

rng = np.random.default_rng(2026100929 + sum(map(ord, sys.argv[1])))
I8 = np.eye(8)
WT = np.array([bin(a).count("1") for a in range(8)])
BIN = np.array([1, 3, 3, 1])


def ghz_proj(b, t):
    b1, b2 = b >> 1, b & 1
    v = np.zeros(8)
    v[2 * b1 + b2] = 1
    v[4 + 2 * (1 - b1) + (1 - b2)] = 1 if t == 0 else -1
    return np.outer(v, v) / 2


P0p, P0m, P1p = ghz_proj(0, 0), ghz_proj(0, 1), ghz_proj(1, 0)
GENS = {"W3": 0.5 * I8 - P0p, "kappa": 0.5 * I8 + P0p - P0m, "omega": 0.5 * I8 - P0p + P1p}
TARGETS = {"t1": (4.0, 1.0, 1.0, 1.0), "t3": (1.0, 1.0, 2.0, 2.0), "t5": (1.0, 2.0, 1.0, 1.0)}
d_t = np.array(TARGETS[sys.argv[1]])
u0, u1 = np.sqrt(d_t[0] * d_t[3]), np.sqrt(d_t[1] * d_t[2])
phit = min(u0 + u1, 3 * u1, (u0 + 3 * u1) / 2)


def make_Y(cscale):
    Y = np.diag(d_t[WT]).astype(complex)
    Y[0, 7] = Y[7, 0] = phit * cscale
    return Y


H2 = np.array([[1, 1], [1, -1]], dtype=complex) / np.sqrt(2)
S2 = np.array([[1, 0], [0, 1j]], dtype=complex)
cliff = [np.eye(2, dtype=complex)]
frontier = list(cliff)
while frontier:
    nf = []
    for U in frontier:
        for Gm in (H2, S2):
            V = Gm @ U
            if not any(abs(abs(np.trace(W.conj().T @ V)) - 2) < 1e-9 for W in cliff):
                cliff.append(V)
                nf.append(V)
    frontier = nf


def gl2(p):
    return (p[0:4] + 1j * p[4:8]).reshape(2, 2)


def kmat(p):
    return np.kron(np.kron(gl2(p[0:8]), gl2(p[8:16])), gl2(p[16:24]))


def start(eps):
    out = []
    for _ in range(3):
        M = cliff[rng.integers(len(cliff))] @ expm(eps * (rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))))
        out += list(M.real.reshape(4)) + list(M.imag.reshape(4))
    return np.array(out)


def ratio(p, Y, g):
    k = kmat(p)
    X = k @ g @ k.conj().T
    v = np.real(np.trace(Y @ X)) / np.real(np.trace(X))
    return v if np.isfinite(v) else 1e6


def min_orbit(Y, g):
    best = np.inf
    for eps in (0.0, 0.02, 0.1, 0.3, 1.0):
        for _ in range(24 if eps == 0 else 40):
            r = minimize(ratio, start(eps), args=(Y, g), method="BFGS", options={"maxiter": 4000, "gtol": 1e-12})
            best = min(best, r.fun)
    return best


Y = make_Y(1.0)
print("target %s: X_t = (d = %s, c = %.10f)" % (sys.argv[1], d_t, phit), flush=True)
for name, g in GENS.items():
    print("(i)  min over filters of <X_t, Ad(k) %s>/tr = %.4e" % (name, min_orbit(Y, g)), flush=True)
print("(ii) min over filters of <X_t, Ad(k) X_t>/tr = %.4e" % min_orbit(Y, Y), flush=True)
Yc = make_Y(1.05)
print("countercontrol (coherence x 1.05): %.4e" % min(min_orbit(Yc, g) for g in GENS.values()), flush=True)
print("done", file=sys.stderr)
