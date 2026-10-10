"""EQ4-SIX exploration y21 -- FLOATING POINT, EXPLORATION ONLY.  NOT EVIDENCE.  Never cited as a certificate.

Question (lead only).  For the y16 run-2 dual Y at (1,1,2,2) (moduli u0 ~ 1/3, u1 ~ 1/6, |c| = 1/2, rho ~ 5.6e-3):
is the diagonal-filter bound psi_diag(Y) = inf over diagonal filters D of phi_S10(arithmetic pair means of Ad(D) Y) /
sqrt(mu1 mu2 mu3) equal to |c| = 1/2 (i.e. tight), and which piece of phi_S10 binds at the optimum?
Also: the same quantity for Y moved to rho = 1 with the same moduli (expected below 1/2: there Y is not in Lift*).
DECISION RULE (fixed before the first run; lead only): report psi_diag, the binding piece and the optimal filter.
"""
import sys

import numpy as np
from scipy.optimize import minimize

rng = np.random.default_rng(2026100921)
WT = np.array([bin(a).count("1") for a in range(8)])
BIN = np.array([1, 3, 3, 1])
y = np.array([0.35628263794720455, 1.2133877116503091, 0.20603472212519652, 0.31186223417779774])
dY = y / BIN


def pieces(x, lm):
    mu = np.exp(lm)
    m = np.array([np.prod([mu[q] if (a >> (2 - q)) & 1 else 1.0 for q in range(3)]) for a in range(8)])
    z = x * m
    s = np.sqrt(np.prod(mu))
    P0 = (z[0] + z[7]) / 2 / s
    Pb = [(z[1] + z[6]) / 2 / s, (z[2] + z[5]) / 2 / s, (z[4] + z[3]) / 2 / s]
    return [P0 + min(Pb), sum(Pb), (P0 + sum(Pb)) / 2]


def psi(d):
    x = np.array([d[WT[a]] for a in range(8)])
    best = (np.inf, None)
    for _ in range(200):
        r = minimize(lambda lm: min(pieces(x, lm)), rng.normal(size=3) * 2, method="Nelder-Mead",
                     options={"maxiter": 20000, "xatol": 1e-13, "fatol": 1e-16})
        if r.fun < best[0]:
            best = (r.fun, r.x)
    return best


u0, u1 = np.sqrt(dY[0] * dY[3]), np.sqrt(dY[1] * dY[2])
rho = dY[0] * dY[2] ** 3 / (dY[3] * dY[1] ** 3)
val, lm = psi(dY)
x = np.array([dY[WT[a]] for a in range(8)])
print("Y: u0 = %.12f, u1 = %.12f, rho = %.6e" % (u0, u1, rho))
print("psi_diag(Y) = %.12f (|c| = 0.5); pieces at the optimum: %s; optimal log mu = %s"
      % (val, np.round(pieces(x, lm), 10).tolist(), np.round(lm, 6).tolist()))
d1 = np.array([u0, u1, u1, u0])
val1, lm1 = psi(d1)
print("same moduli at rho = 1: psi_diag = %.12f; pieces %s" % (val1, np.round(pieces(np.array([d1[WT[a]] for a in range(8)]),
                                                                                      lm1), 10).tolist()))
print("done", file=sys.stderr)
