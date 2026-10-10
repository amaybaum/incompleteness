"""EQ4-SIX exploration y27 -- FLOATING POINT, EXPLORATION ONLY.  NOT EVIDENCE.  Never cited as a certificate.

Question (lead only).  y22 (void: random starts) redone with the structured starts of y24.  Lift(K_A)* contains the
C_A boundary point X_t (d = (1,1,2,2), c = 2 sqrt 2) and the y16 dual Y (moduli (1/3, 1/6, 1/2)), with <X_t, Y> < 0,
so a K_A-lift contains at most one of them.  Does (A4) exclude either choice?  Glue network (crossing split, Bell
links; y3 code), nodes Ad(k) g with g from the 64 non-PSD K_A generators and the candidate C in {X_t, Y} (both real,
so T(C) = C serves as an effect):
  (a) C in all four positions; (b) C in one random position, K_A generators elsewhere (16 quadruples);
  (c) C as both states, K_A generators as effects (16 quadruples); (d) C as both effects, K_A generators as states.
Countercontrols (must be negative): the PN quadruple; (X_t, Y; (1/2) (x) Phi+ twice).
DECISION RULE (fixed before the first run; lead only): "C excluded by (A4) (lead)" iff some minimum < -1e-6 with the
countercontrols negative; "C not excluded (lead)" iff every minimum >= -1e-9.
"""
import sys

import numpy as np
from scipy.linalg import expm
from scipy.optimize import minimize

sys.argv = [sys.argv[0]]
src = open(__file__.rsplit("/", 1)[0] + "/y3_k4net_float.py").read()
src = src[:src.index("# gradient sanity check")]
ns = {}
exec(compile(src, "y3_defs", "exec"), ns)
fval, P, NEG, NEGNAME, kmat = ns["fval"], ns["P"], ns["NEG"], ns["NEGNAME"], ns["kmat"]
rng = np.random.default_rng(2026100927)
I8 = np.eye(8)
W3 = 0.5 * I8 - P[0]
KAP = 0.5 * I8 + P[0] - P[1]
OME = 0.5 * I8 - P[0] + P[2]
GHZ = P[0]
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


def to_params(ks):
    out = []
    for M in ks:
        out += list(M.real.reshape(4)) + list(M.imag.reshape(4))
    return np.array(out)


def structured_start(eps):
    ks = []
    for _ in range(3):
        U = cliff[rng.integers(len(cliff))]
        Hm = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
        ks.append(U @ expm(eps * Hm))
    return to_params(ks)


def pair_val(p, g, gp):
    k = kmat(p)
    Y = k @ g @ k.conj().T
    return np.real(np.trace(gp @ Y)) / (np.linalg.norm(gp) * np.linalg.norm(Y))


def min_pair(g, gp, n_per_eps=40):
    best = (np.inf, None)
    for eps in (0.0, 0.02, 0.1, 0.3, 1.0):
        for _ in range(n_per_eps if eps > 0 else 24):
            p0 = structured_start(eps)
            r = minimize(pair_val, p0, args=(g, gp), method="BFGS", options={"maxiter": 4000, "gtol": 1e-12})
            if r.fun < best[0]:
                best = (r.fun, r.x)
    return best


def min_net(gs, n_per_eps=6):
    best = (np.inf, None)
    for eps in (0.0, 0.02, 0.1, 0.3, 1.0):
        for _ in range(n_per_eps):
            p0 = np.concatenate([structured_start(eps) for _ in range(4)])
            r = minimize(fval, p0, args=(gs,), jac=True, method="BFGS", options={"maxiter": 5000, "gtol": 1e-11})
            if r.fun < best[0]:
                best = (r.fun, r.x)
    return best


PHI = np.zeros((4, 4))
PHI[0, 0] = PHI[0, 3] = PHI[3, 0] = PHI[3, 3] = 0.5
BE = np.kron(0.5 * np.eye(2), PHI)
WT = np.array([bin(a).count("1") for a in range(8)])
BIN = np.array([1, 3, 3, 1])
X_t = np.diag(np.array([1.0, 1.0, 2.0, 2.0])[WT]).astype(complex)
X_t[0, 7] = X_t[7, 0] = 2 * np.sqrt(2)
yd = np.array([0.35628263794720455, 1.2133877116503091, 0.20603472212519652, 0.31186223417779774])
Y_t = np.diag((yd / BIN)[WT]).astype(complex)
Y_t[0, 7] = Y_t[7, 0] = -0.5
print("countercontrol PN quadruple: %.4e" % min_net([BE, BE, GHZ, W3], 3)[0], flush=True)
print("countercontrol (X_t, Y; (1/2) (x) Phi+ twice): %.4e" % min_net([X_t, Y_t, BE, BE], 3)[0], flush=True)
for C, nm in ((X_t, "X_t"), (Y_t, "Y")):
    print("(a) %s in all four positions: %.4e" % (nm, min_net([C, C, C, C], 4)[0]), flush=True)
    for label, maker in (("(b) %s in one random position" % nm, "one"), ("(c) %s as both states" % nm, "states"),
                         ("(d) %s as both effects" % nm, "effects")):
        worst = np.inf
        for _ in range(16):
            ii = rng.integers(len(NEG), size=4)
            gs = [NEG[ii[0]], NEG[ii[1]], NEG[ii[2]].T, NEG[ii[3]].T]
            if maker == "one":
                gs[rng.integers(4)] = C
            elif maker == "states":
                gs[0] = gs[1] = C
            else:
                gs[2] = gs[3] = C
            worst = min(worst, min_net(gs, 2)[0])
        print("%s: worst normalized min over 16 quadruples %.4e" % (label, worst), flush=True)
print("done", file=sys.stderr)
