"""EQ4-SIX exploration y28 -- FLOATING POINT, EXPLORATION ONLY.  NOT EVIDENCE.  Never cited as a certificate.

Question (sign control, §A.21).  y20 at t1 (X_t = ((4,1,1,1), c = 5/2)) reported min over filters of
<X_t, Ad(k) W3>/tr = -0.333 together with overflow warnings.  A written argument says the true value is >= 0:
X_t is in Z* (Z* cap Xi = {|c| <= 3 u1}, and 5/2 <= 3) while every Ad(k) W3 is in Z (W3 in Z, Z filter-invariant).
Control: repeat y20's search (random filters exp(H), H ~ N(0, s^2), s in {0.3, 1, 2}; Nelder-Mead from the best 30)
recording the minimizing filter; re-evaluate the value there (a) in float64, (b) in exact rational arithmetic after
rounding the filter entries to rationals (denominator <= 10^6), and report the filter's condition number.  Then the
same minimization with well-conditioned structured starts (Cliffords times exp(eps H), eps <= 1).
DECISION RULE (fixed before the first run): if the exact value at the reported minimizer is >= 0 while float64 says
< 0, the y20 t1 W3 value is a numerical artifact (cancellation with ill-conditioned filters) and y20 t1 is void as
evidence; otherwise the written argument has an error and must be re-examined.
"""
import sys
from fractions import Fraction as Fr

import numpy as np
from scipy.linalg import expm
from scipy.optimize import minimize

rng = np.random.default_rng(2026100928)
I8 = np.eye(8)
WT = np.array([bin(a).count("1") for a in range(8)])
GHZ = np.zeros((8, 8))
GHZ[0, 0] = GHZ[0, 7] = GHZ[7, 0] = GHZ[7, 7] = 0.5
W3 = 0.5 * I8 - GHZ
X_t = np.diag(np.array([4.0, 1.0, 1.0, 1.0])[WT]).astype(complex)
X_t[0, 7] = X_t[7, 0] = 2.5


def filt(q):
    ks = [expm((q[8 * j:8 * j + 4] + 1j * q[8 * j + 4:8 * j + 8]).reshape(2, 2)) for j in range(3)]
    return ks, np.kron(np.kron(ks[0], ks[1]), ks[2])


def ratio_q(q):
    _, k = filt(q)
    X = k @ W3 @ k.conj().T
    return np.real(np.trace(X_t @ X)) / np.real(np.trace(X))


samples = []
with np.errstate(all="ignore"):
    for _ in range(20000):
        q = rng.normal(size=24) * rng.choice([0.3, 1.0, 2.0])
        v = ratio_q(q)
        if np.isfinite(v):
            samples.append((v, q))
    samples.sort(key=lambda t: t[0])
    best = (np.inf, None)
    for v, q in samples[:30]:
        r = minimize(ratio_q, q, method="Nelder-Mead", options={"maxiter": 20000, "maxfev": 20000, "xatol": 1e-10,
                                                                 "fatol": 1e-14})
        if np.isfinite(r.fun) and r.fun < best[0]:
            best = (r.fun, r.x)
print("random-search minimum (float64): %.4e" % best[0])
ks, k = filt(best[1])
print("condition numbers of the three one-token filters: %s" % [float("%.3e" % np.linalg.cond(m)) for m in ks])


def to_fr(z):
    return (Fr(float(z.real)).limit_denominator(10 ** 6), Fr(float(z.imag)).limit_denominator(10 ** 6))


def cmul(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def cadd(a, b):
    return (a[0] + b[0], a[1] + b[1])


# exact: K = kron of rationalized one-token filters; value = tr(X_t K W3 K^dag), trace = tr(K W3 K^dag)
kr = [[[to_fr(m[i, j]) for j in range(2)] for i in range(2)] for m in ks]
K = [[(Fr(0), Fr(0))] * 8 for _ in range(8)]
for r_ in range(8):
    for c_ in range(8):
        acc = (Fr(1), Fr(0))
        for t in range(3):
            acc = cmul(acc, kr[t][(r_ >> (2 - t)) & 1][(c_ >> (2 - t)) & 1])
        K[r_][c_] = acc
W3e = [[Fr(0)] * 8 for _ in range(8)]
for a in range(8):
    W3e[a][a] = Fr(1, 2)
W3e[0][0] -= Fr(1, 2)
W3e[7][7] -= Fr(1, 2)
W3e[0][7] -= Fr(1, 2)
W3e[7][0] -= Fr(1, 2)
Xe = [[Fr(0)] * 8 for _ in range(8)]
for a in range(8):
    Xe[a][a] = [Fr(4), Fr(1), Fr(1), Fr(1)][WT[a]]
Xe[0][7] = Xe[7][0] = Fr(5, 2)
# M = K W3 K^dag (exact)
KW = [[(Fr(0), Fr(0))] * 8 for _ in range(8)]
for i in range(8):
    for j in range(8):
        s = (Fr(0), Fr(0))
        for m in range(8):
            if W3e[m][j] != 0:
                s = cadd(s, cmul(K[i][m], (W3e[m][j], Fr(0))))
        KW[i][j] = s
M = [[(Fr(0), Fr(0))] * 8 for _ in range(8)]
for i in range(8):
    for j in range(8):
        s = (Fr(0), Fr(0))
        for m in range(8):
            s = cadd(s, cmul(KW[i][m], (K[j][m][0], -K[j][m][1])))
        M[i][j] = s
num = sum((Xe[i][j] * M[j][i][0] for i in range(8) for j in range(8)), Fr(0))
den = sum((M[i][i][0] for i in range(8)), Fr(0))
print("exact value at the rationalized minimizer: numerator sign %d, trace sign %d, ratio = %.6e"
      % ((num > 0) - (num < 0), (den > 0) - (den < 0), float(num / den) if den != 0 else float("nan")))
with np.errstate(all="ignore"):
    kf = np.kron(np.kron(np.array([[complex(*map(float, e)) for e in row] for row in kr[0]]),
                         np.array([[complex(*map(float, e)) for e in row] for row in kr[1]])),
                 np.array([[complex(*map(float, e)) for e in row] for row in kr[2]]))
    Xf = kf @ W3 @ kf.conj().T
    print("float64 value at the same rationalized filter: %.6e" % (np.real(np.trace(X_t @ Xf)) / np.real(np.trace(Xf))))
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


def ratio_p(p):
    ks_ = [(p[8 * j:8 * j + 4] + 1j * p[8 * j + 4:8 * j + 8]).reshape(2, 2) for j in range(3)]
    k_ = np.kron(np.kron(ks_[0], ks_[1]), ks_[2])
    X = k_ @ W3 @ k_.conj().T
    return np.real(np.trace(X_t @ X)) / np.real(np.trace(X))


bs = np.inf
for eps in (0.0, 0.02, 0.1, 0.3, 1.0):
    for _ in range(24 if eps == 0 else 40):
        p0 = []
        for _t in range(3):
            Mm = cliff[rng.integers(len(cliff))] @ expm(eps * (rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))))
            p0 += list(Mm.real.reshape(4)) + list(Mm.imag.reshape(4))
        r = minimize(ratio_p, np.array(p0), method="BFGS", options={"maxiter": 4000, "gtol": 1e-12})
        bs = min(bs, r.fun)
print("structured-start minimum: %.4e" % bs)
print("done", file=sys.stderr)
