"""EQ4-SIX exploration y25 -- FLOATING POINT, EXPLORATION ONLY.  NOT EVIDENCE.  Never cited as a certificate.

c = 1 counterpart of y24 (structured starts; y23 showed random-start BFGS minima of normalized networks are not
informative, so y9's c = 1 minima are re-done here).  Code for K_tw, the twin-link glue network and the filters is
y9's (exec of its definitions); starts are k = (U_1 (x) U_2 (x) U_3) exp(eps H), U_j one-qubit Cliffords,
eps in {0, 0.02, 0.1, 0.3, 1}.
 (i)  self-positivity of Lift(K_tw) (Euclidean pairing, K3 = K3*): min over k of tr(g' Ad(k) k0)/norms, g' over the 8
      generators of the k0 orbit (pairs with the twin-hull part are settled exactly: K_tw <= S_tw*, EQ4-P p13);
      countercontrol: (k0, GHZ+) with <k0, GHZ+> = -1 at identity.
 (ii) twin-link glue network on Lift(K_tw) nodes, 10 random generator quadruples (run 2; run 1, with 20 and a single
      final print, was stopped by hand as too slow); countercontrol: states GHZ+ and k0
      with effects (1/2) 1 (x) SWAP/2 (the twin theta value (1/8) tr(x y) up to positive factors, tr(GHZ+ k0) = -1).
DECISION RULE (fixed before the first run; lead only): "violation lead" iff a minimum < -1e-6 in (i) or (ii) with both
countercontrols negative; else "no violation found with structured starts".
"""
import sys

import numpy as np
from scipy.linalg import expm
from scipy.optimize import minimize

sys.argv = [sys.argv[0]]
src = open(__file__.rsplit("/", 1)[0] + "/y9_c1_float.py").read()
cut1 = src.index("worst = (np.inf, None)\nfor (nm, g) in REPS.items():")
cut2 = src.index("def t6(M):")
cut3 = src.index("worst = (np.inf, None)\nfor trial in range(120):")
ns = {}
exec(compile(src[:cut1] + src[cut2:cut3], "y9_defs", "exec"), ns)
P, GEN, GOPS, kmat, val, gval, gd, orbit = (ns[k] for k in ("P", "GEN", "GOPS", "kmat", "val", "gval", "gd", "orbit"))
rng = np.random.default_rng(2026100925)
K0 = gd((-1, 3, 1, 1, 1, 1, 1, 1))
KORB = [gd(v) for v in orbit((-1, 3, 1, 1, 1, 1, 1, 1))]
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


def structured_start(eps):
    out = []
    for _ in range(3):
        U = cliff[rng.integers(len(cliff))]
        Hm = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
        M = U @ expm(eps * Hm)
        out += list(M.real.reshape(4)) + list(M.imag.reshape(4))
    return np.array(out)


def min_pair(g, gp, n_per_eps=30):
    best = np.inf
    for eps in (0.0, 0.02, 0.1, 0.3, 1.0):
        for _ in range(n_per_eps if eps > 0 else 24):
            r = minimize(val, structured_start(eps), args=(g, gp), method="BFGS", options={"maxiter": 4000, "gtol": 1e-12})
            best = min(best, r.fun)
    return best


def min_net(gs, n_per_eps=3):
    best = np.inf
    for eps in (0.0, 0.02, 0.1, 0.3, 1.0):
        for _ in range(n_per_eps):
            p0 = np.concatenate([structured_start(eps) for _ in range(4)])
            r = minimize(gval, p0, args=(gs,), method="L-BFGS-B", options={"maxiter": 1500})
            best = min(best, r.fun)
    return best


cc1 = min_pair(K0, GHZ, 8)
print("(i) countercontrol (k0, GHZ+): %.4e" % cc1, flush=True)
worst = np.inf
for gp in KORB:
    worst = min(worst, min_pair(K0, gp, 12))
print("(i) min over filters of tr(g' Ad(k) k0)/norms, g' over the k0 orbit (%d): %.4e" % (len(KORB), worst), flush=True)
SWm = np.zeros((4, 4))
for a in range(2):
    for b in range(2):
        SWm[2 * a + b, 2 * b + a] = 0.5
TE = np.kron(0.5 * np.eye(2), SWm)
cc2 = min_net([GHZ, K0, TE, TE], 4)
print("(ii) countercontrol (GHZ+, k0; (1/2) (x) SWAP/2 effects): %.4e" % cc2, flush=True)
w2 = np.inf
for trial in range(10):
    ii = rng.integers(len(GOPS), size=4)
    w2 = min(w2, min_net([GOPS[i] for i in ii]))
    print("(ii) after quadruple %d: worst normalized min %.4e" % (trial + 1, w2), flush=True)
print("(ii) Lift(K_tw) nodes, 10 random generator quadruples: worst normalized min %.4e" % w2, flush=True)
print("countercontrols negative: %s" % (cc1 < 0 and cc2 < 0), flush=True)
print("done", file=sys.stderr)
