"""EQ4-SIX exploration y24 -- FLOATING POINT, EXPLORATION ONLY.  NOT EVIDENCE.  Never cited as a certificate.

Question (lead only).  y23 showed that random-start BFGS on the normalized glue network converges to ~0 even when a
negative value is reachable from identity filters (X_t, Y_t, (1/2) (x) Phi+ twice: -2.2e-3 from identity, ~0 from 10
random starts).  So the earlier float minima over filters (y1 self-positivity; y3, y9 glue network; y22) may be
optimizer-limited.  Redo the decisive ones with structured starts: every start is k = (U_1 (x) U_2 (x) U_3) exp(eps H)
with U_j random one-qubit Cliffords (24 elements mod phase) and H a random complex 2 x 2 per token, eps in
{0.02, 0.1, 0.3, 1}, plus the Clifford points themselves.
 (i)  T-self-positivity of Lift(K_A): min over k of tr(g' Ad(k) g)/(|g'| |Ad(k) g|) for g, g' in {kappa, omega} (the
      pairs not settled exactly by Z and BS*); control pair (W3, W3) (>= 0, exact via Z).
 (ii) (A4) on Lift(K_A) nodes: min of the normalized crossing-split glue network over four filters, nodes from the 64
      non-PSD generators of K_A (states g, effects g^T), 40 random quadruples.
Countercontrols (must be negative): (i) the pair (W3, GHZ) (GHZ not in K_A*: <W3, GHZ> = -1/2); (ii) the PN
quadruple ((1/2) (x) Phi+, (1/2) (x) Phi+, GHZ, W3) (exact -1/64 unfiltered) and the y23 quadruple
(X_t, Y_t, (1/2) (x) Phi+, (1/2) (x) Phi+).
DECISION RULE (fixed before the first run; lead only): a "violation lead" is a minimum < -1e-6 in (i) or (ii) with
both countercontrols negative; then the minimizing filters are printed for an exact follow-up.  Otherwise "no
violation found with structured starts".
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
rng = np.random.default_rng(2026100924)
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


print("one-qubit Cliffords (mod phase): %d" % len(cliff), flush=True)
cc1 = min_pair(W3, GHZ, 10)[0]
print("(i) countercontrol (W3, GHZ): %.4e" % cc1, flush=True)
print("(i) control (W3, W3): %.4e" % min_pair(W3, W3, 10)[0], flush=True)
for (n1, g1), (n2, g2) in [(("kappa", KAP), ("kappa", KAP)), (("kappa", KAP), ("omega", OME)),
                           (("omega", OME), ("kappa", KAP)), (("omega", OME), ("omega", OME))]:
    v, p = min_pair(g1, g2)
    print("(i) min over filters of tr(%s Ad(k) %s)/norms = %.4e" % (n2, n1, v), flush=True)
    if v < -1e-6:
        print("    minimizing filter parameters:", [float(t) for t in p], flush=True)
PHI = np.zeros((4, 4))
PHI[0, 0] = PHI[0, 3] = PHI[3, 0] = PHI[3, 3] = 0.5
BE = np.kron(0.5 * np.eye(2), PHI)
cc2 = min_net([BE, BE, GHZ, W3])[0]
print("(ii) countercontrol PN quadruple: %.4e" % cc2, flush=True)
WT = np.array([bin(a).count("1") for a in range(8)])
BIN = np.array([1, 3, 3, 1])
X_t = np.diag(np.array([1.0, 1.0, 2.0, 2.0])[WT]).astype(complex)
X_t[0, 7] = X_t[7, 0] = 2 * np.sqrt(2)
yd = np.array([0.35628263794720455, 1.2133877116503091, 0.20603472212519652, 0.31186223417779774])
Y_t = np.diag((yd / BIN)[WT]).astype(complex)
Y_t[0, 7] = Y_t[7, 0] = -0.5
cc3 = min_net([X_t, Y_t, BE, BE])[0]
print("(ii) countercontrol y23 quadruple: %.4e" % cc3, flush=True)
worst = (np.inf, None, None)
for trial in range(40):
    ii = rng.integers(len(NEG), size=4)
    gs = [NEG[ii[0]], NEG[ii[1]], NEG[ii[2]].T, NEG[ii[3]].T]
    v, p = min_net(gs, 3)
    if v < worst[0]:
        worst = (v, tuple(NEGNAME[i] for i in ii), p)
print("(ii) Lift(K_A) nodes, 40 random generator quadruples: worst normalized min %.4e at %s" % (worst[0], worst[1]),
      flush=True)
if worst[0] < -1e-6:
    print("    minimizing filter parameters:", [float(t) for t in worst[2]], flush=True)
lead = (cc1 < 0 and cc2 < 0 and cc3 < 0)
print("countercontrols negative: %s" % lead, flush=True)
print("done", file=sys.stderr)
