"""EQ4-SIX exploration y23 -- FLOATING POINT, EXPLORATION ONLY.  NOT EVIDENCE.  Never cited as a certificate.

Harness check of the y3/y22 glue-network code (lead only).  y22's countercontrol (X_t, Y_t states, (1/2) (x) Phi+
effects) returned a minimum ~ -3e-18 although s3 B predicts the unfiltered value (1/32) tr(X_t T(Y_t)) < 0.
Checks: (1) the y3 contraction at identity filters against (1/32) tr(x T y) for X_t, Y_t and for the s3 PN control
(x = y = (1/2) (x) Phi+, e = GHZ, f = W3: -1/64 expected); (2) the normalized objective at identity filters and the
BFGS minimum started from identity filters versus from random filters.
DECISION RULE (fixed before the first run): report the numbers; if (1) disagrees with s3, the y3 contraction is wrong;
if (1) agrees but random starts miss a negative value reachable from identity, the y3/y22 minima are optimizer-limited.
"""
import sys

import numpy as np
from scipy.optimize import minimize

sys.argv = [sys.argv[0]]
src = open(__file__.rsplit("/", 1)[0] + "/y3_k4net_float.py").read()
src = src[:src.index("# gradient sanity check")]
ns = {}
exec(compile(src, "y3_defs", "exec"), ns)
net, fval, P = ns["net"], ns["fval"], ns["P"]
rng = np.random.default_rng(2026100923)
WT = np.array([bin(a).count("1") for a in range(8)])
BIN = np.array([1, 3, 3, 1])
X_t = np.diag(np.array([1.0, 1.0, 2.0, 2.0])[WT]).astype(complex)
X_t[0, 7] = X_t[7, 0] = 2 * np.sqrt(2)
yd = np.array([0.35628263794720455, 1.2133877116503091, 0.20603472212519652, 0.31186223417779774])
Y_t = np.diag((yd / BIN)[WT]).astype(complex)
Y_t[0, 7] = Y_t[7, 0] = -0.5
PHI = np.zeros((4, 4))
PHI[0, 0] = PHI[0, 3] = PHI[3, 0] = PHI[3, 3] = 0.5
BE = np.kron(0.5 * np.eye(2), PHI)
print("(1) net(X_t, Y_t, BE, BE) = %.8f ; (1/32) tr(X_t Y_t^T) = %.8f" % (net(X_t, Y_t, BE, BE),
                                                                         np.real(np.trace(X_t @ Y_t.T)) / 32))
xs = np.kron(0.5 * np.eye(2), PHI)
GHZ = P[0]
W3 = 0.5 * np.eye(8) - P[0]
print("(1) PN control net(1/2 (x) Phi+, 1/2 (x) Phi+, GHZ, W3) = %.8f (s3: -1/64 = %.8f)" % (net(xs, xs, GHZ, W3),
                                                                                         -1 / 64))
ident = np.concatenate([np.array([1, 0, 0, 1, 0, 0, 0, 0] * 3, dtype=float)] * 4)
gs = [X_t, Y_t, BE, BE]
v0, _ = fval(ident, gs)
print("(2) normalized objective at identity filters: %.6e" % v0)
r = minimize(fval, ident + 1e-3 * rng.normal(size=96), args=(gs,), jac=True, method="BFGS",
             options={"maxiter": 5000, "gtol": 1e-11})
print("(2) BFGS from identity: %.6e" % r.fun)
vals = []
for _ in range(10):
    r = minimize(fval, rng.normal(size=96), args=(gs,), jac=True, method="BFGS", options={"maxiter": 5000, "gtol": 1e-11})
    vals.append(r.fun)
print("(2) BFGS from 10 random starts: min %.6e, max %.6e" % (min(vals), max(vals)))
print("done", file=sys.stderr)
