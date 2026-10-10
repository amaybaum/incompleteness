#!/usr/bin/env python3
"""Thread X (EXOT) -- [N, numerical] cross-checks and guidance. Nothing printed here certifies anything.

Run (cwd pt/X/): python3 -I -B x7_numeric.py > x7_numeric.out 2> x7_numeric.err

Every section is [N, numerical] (floating point, numpy/scipy); seeds are fixed and printed; printed numbers are
rounded so the output is reproducible on this machine. Sections:
  N1  K1 by definition only (no lemma): sample y = z + s E0 in K1^* (z random PSD, alternately unbiased and biased
      toward the negative eigenvector g, s >= max(0, -<z,E0>/3)); test y in K1 = (Q3 n E0^*) + R_+ E0 by maximizing the concave function
      lam -> lambda_min(y - lam E0) over lam in [0, <y,E0>/<E0,E0>] (ternary search). Report the worst margin.
  N2  K4: random z; the SD2 candidate q = z + sum_s t_s e_s; report the worst lambda_min(q).
  N3  the spectral characterization (NOTES N8): random Hermitian e with exactly one negative eigenvalue; (GL) tested
      on the constructive witness z = (g + f)(g + f)^* (f the second eigenvector) and on 200 random biased z.
  N4  guidance for the torus direction: two non-orthogonal Bell-type defects e1 = (I - 2 P_psi)/8,
      e2 = (I - 2 P_phi)/8 with |<psi|phi>|^2 = c; is K({e1, e2}) self-dual? Sample y in K^* and test membership by
      maximizing the concave function lam -> min(lambda_min(y - lam.e), <y - lam.e, e1>, <y - lam.e, e2>) over
      lam in R_+^2 (grid + Nelder-Mead). Report the worst margin per c.
Controls (must behave as stated, else 'X7-NUMERIC: CONTROL FAILED' and exit 1):
  K1c N1 run with e_c (c = 3/2) in place of E0 must show a clearly negative worst margin (< -1e-3);
  N3c the constructive witness must violate (GL) for every sampled e with lambda_2 < -lambda_1;
  N4c c = 0 (orthogonal defects, lemma SD2) must show no margin below -1e-7.

DECISION RULE (fixed before the first run): print 'SUMMARY [N, numerical]' lines only; no VERDICT line; tolerances
1e-9 (N1, N2), 1e-7 (N4) for 'no violation found'; a control failing its stated behaviour stops the script (exit 1).
Seeds: N1 2026101001, N2 2026101002, N3 2026101003, N4 2026101004.
"""
import sys

import numpy as np
from scipy.optimize import minimize

np.set_printoptions(precision=3)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]])
Z = np.diag([1.0, -1.0]).astype(complex)
I2 = np.eye(2, dtype=complex)
XZ, YY = np.kron(X, Z), np.kron(Y, Y)
I4 = np.eye(4, dtype=complex)
E0 = (I4 + XZ - YY) / 4
ECB = (I4 + 1.5 * (XZ - YY)) / 4
G = np.array([1, -1, -1, -1], dtype=complex) / 2
PSI = {s: np.array([1, s[0] * s[1], s[0], -s[1]], dtype=complex) / 2 for s in [(1, 1), (1, -1), (-1, 1), (-1, -1)]}
EX4 = {s: (I4 - 2 * np.outer(v, v.conj())) / 8 for s, v in PSI.items()}
FAILS = []


def ip(a, b):
    return float(np.real(np.trace(a @ b)))


def lmin(M):
    return float(np.linalg.eigvalsh((M + M.conj().T) / 2)[0])


def rand_psd(rng, bias=None):
    k = rng.integers(1, 5)
    V = rng.normal(size=(4, k)) + 1j * rng.normal(size=(4, k))
    if bias is not None:
        V[:, 0] += 3.0 * bias
    return V @ V.conj().T


def k1_margin(y, e):
    hi = ip(y, e) / ip(e, e)
    if hi < 0:
        return None
    lo = 0.0
    for _ in range(200):
        m1, m2 = lo + (hi - lo) / 3, hi - (hi - lo) / 3
        if lmin(y - m1 * e) < lmin(y - m2 * e):
            lo = m1
        else:
            hi = m2
    return max(lmin(y - lo * e), lmin(y - hi * e))


def n1(e, seed, n):
    rng = np.random.default_rng(seed)
    worst, nontriv = np.inf, 0
    for i in range(n):
        z = rand_psd(rng, bias=G if i % 2 else None)       # alternate unbiased and g-biased samples
        z = z / np.real(np.trace(z))
        s0 = max(0.0, -ip(z, e) / ip(e, e))
        nontriv += s0 > 0
        y = z + (s0 + rng.exponential(0.05)) * e
        m = k1_margin(y, e)
        if m is not None:
            worst = min(worst, m)
    return worst, nontriv


print('== N1  [N, numerical] K1 membership of sampled K1^* elements, by definition (seed 2026101001)')
w, nt = n1(E0, 2026101001, 3000)
print(f"N1  samples 3000, with <z,E0> < 0: {nt}; worst margin max_lam lambda_min(y - lam E0) = {w:.2e}")
print(f"SUMMARY [N, numerical] N1: {'no violation found' if w > -1e-9 else 'VIOLATION FOUND'} (tolerance 1e-9)")
w, nt = n1(ECB, 2026101001, 3000)
print(f"K1c samples 3000 with e_c (c = 3/2): with <z,e> < 0: {nt}; worst margin = {w:.2e}")
if not w < -1e-3:
    FAILS.append('K1c')

print()
print('== N2  [N, numerical] K4: the SD2 candidate on random states (seed 2026101002)')
rng = np.random.default_rng(2026101002)
worst, nontriv = np.inf, 0
for _ in range(5000):
    z = rand_psd(rng, bias=PSI[(1, -1)] if rng.random() < 0.5 else None)
    z = z / np.real(np.trace(z))
    t = {s: max(0.0, -ip(z, e) / ip(e, e)) for s, e in EX4.items()}
    nontriv += any(v > 0 for v in t.values())
    q = z + sum(t[s] * EX4[s] for s in EX4)
    worst = min(worst, lmin(q))
print(f"N2  samples 5000, with a negative pairing: {nontriv}; worst lambda_min(q) = {worst:.2e}")
print(f"SUMMARY [N, numerical] N2: {'no violation found' if worst > -1e-9 else 'VIOLATION FOUND'} (tolerance 1e-9)")

print()
print('== N3  [N, numerical] the spectral characterization of self-dual single-defect cones (seed 2026101003)')
rng = np.random.default_rng(2026101003)
A = violA = B = witB = randB = 0
for _ in range(1500):
    Q_, _r = np.linalg.qr(rng.normal(size=(4, 4)) + 1j * rng.normal(size=(4, 4)))
    lam = np.concatenate([[-rng.uniform(0.05, 1.0)], np.sort(rng.uniform(0.05, 2.0, size=3))])
    e = Q_ @ np.diag(lam) @ Q_.conj().T
    g, f = Q_[:, 0], Q_[:, 1]
    cond = lam[1] >= -lam[0]

    def gl_viol(z):
        c0 = ip(z, e)
        return c0 < 0 and lmin(z - c0 / ip(e, e) * e) < -1e-9

    u = (g + f) / np.sqrt(2)
    wit = gl_viol(np.outer(u, u.conj()))
    rnd = any(gl_viol(rand_psd(rng)) for _ in range(200))
    if cond:
        A += 1
        violA += wit or rnd
    else:
        B += 1
        witB += wit
        randB += rnd
print(f"N3  e with lambda_2 >= -lambda_1: {A}, of which with a (GL) violation found: {violA}")
print(f"N3  e with lambda_2 < -lambda_1: {B}; constructive witness violates (GL): {witB}; random z found one: {randB}")
print(f"SUMMARY [N, numerical] N3: {'consistent with the characterization' if violA == 0 and witB == B else 'INCONSISTENT'}")
if witB != B:
    FAILS.append('N3c')

print()
print('== N4  [N, numerical] guidance: two non-orthogonal Bell-type defects (seed 2026101004)')
rng = np.random.default_rng(2026101004)
psi = np.array([1, 0, 0, 1], dtype=complex) / np.sqrt(2)


def margin_two(y, es):
    trs = [np.real(np.trace(e)) for e in es]
    L = [np.real(np.trace(y)) / t for t in trs]

    def h(lmb):
        lmb = np.maximum(lmb, 0.0)
        r = y - lmb[0] * es[0] - lmb[1] * es[1]
        return min(lmin(r), ip(r, es[0]), ip(r, es[1]))

    best, arg = -np.inf, None
    for a in np.linspace(0, L[0], 41):
        for b in np.linspace(0, L[1], 41):
            v = h(np.array([a, b]))
            if v > best:
                best, arg = v, np.array([a, b])
    res = minimize(lambda l: -h(l), arg, method='Nelder-Mead', options={'xatol': 1e-12, 'fatol': 1e-14,
                                                                         'maxiter': 4000})
    return max(best, -res.fun)


for cval in (0.0, 0.25, 0.5, 0.75):
    th = np.arccos(np.sqrt(cval))
    phi = np.kron(np.diag([np.exp(1j * th), np.exp(-1j * th)]), I2) @ psi
    es = [(I4 - 2 * np.outer(v, v.conj())) / 8 for v in (psi, phi)]
    Gm = np.array([[ip(a, b) for b in es] for a in es])
    worst = np.inf
    for i in range(120):
        z = rand_psd(rng, bias=[None, psi, phi][i % 3])
        z = z / np.real(np.trace(z))
        b = np.array([ip(z, e) for e in es])
        sv = np.zeros(2)
        for _ in range(60):
            for j in range(2):
                r = b[j] + Gm[j] @ sv
                if r < 0:
                    sv[j] += -r / Gm[j, j]
        y = z + sv[0] * es[0] + sv[1] * es[1]
        worst = min(worst, margin_two(y, es))
    print(f"N4  |<psi|phi>|^2 = {cval:.2f}: samples 120; worst membership margin = {worst:.2e}")
    if cval == 0.0 and worst < -1e-7:
        FAILS.append('N4c')

print()
if FAILS:
    print(f"X7-NUMERIC: CONTROL FAILED -- {', '.join(FAILS)}")
    sys.exit(1)
print('SUMMARY [N, numerical] controls K1c, N3c, N4c behaved as stated; nothing above is a certificate')
