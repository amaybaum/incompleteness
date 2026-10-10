"""EQ4-SIX exploration y26 -- FLOATING POINT, EXPLORATION ONLY.  NOT EVIDENCE.  Never cited as a certificate.

Question (lead only).  Third check of "Y in Lift(K_A)*" for the y16 dual Y at (1,1,2,2), now with the structured
starts of y24 (products of one-qubit Cliffords times exp(eps H), eps in {0, 0.02, 0.1, 0.3, 1}), since y23 showed that
random-start minima can miss negative values: min over k of <Y, Ad(k) g>/tr(Ad(k) g) for g in {W3, kappa, omega}
(BFGS, 24 + 4 x 40 starts each).
Countercontrol: the same search on Y with the coherence scaled by 1.05 must find a negative value.
DECISION RULE (fixed before the first run; lead only): the lead survives iff every minimum is >= -1e-7 and the
countercontrol is negative.
"""
import sys

import numpy as np
from scipy.linalg import expm
from scipy.optimize import minimize

rng = np.random.default_rng(2026100926)
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
yd = np.array([0.35628263794720455, 1.2133877116503091, 0.20603472212519652, 0.31186223417779774])


def make_Y(cscale):
    Y = np.diag((yd / BIN)[WT]).astype(complex)
    Y[0, 7] = Y[7, 0] = -0.5 * cscale
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
    return np.real(np.trace(Y @ X)) / np.real(np.trace(X))


def min_orbit(Y, g):
    best = np.inf
    for eps in (0.0, 0.02, 0.1, 0.3, 1.0):
        for _ in range(24 if eps == 0 else 40):
            r = minimize(ratio, start(eps), args=(Y, g), method="BFGS", options={"maxiter": 4000, "gtol": 1e-12})
            best = min(best, r.fun)
    return best


Y = make_Y(1.0)
for name, g in GENS.items():
    print("min over filters of <Y, Ad(k) %s>/tr = %.4e" % (name, min_orbit(Y, g)), flush=True)
Yc = make_Y(1.05)
print("countercontrol (coherence x 1.05): %.4e" % min(min_orbit(Yc, g) for g in GENS.values()), flush=True)
print("done", file=sys.stderr)
