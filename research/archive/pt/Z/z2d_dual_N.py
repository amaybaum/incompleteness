"""z2d_dual_N.py -- thread Z, node S2, [N, numerical] search ONLY (guidance; certifies nothing).

For the exact candidate y of NOTES N6 (basis e1, e2 = poles of circle 1, e3, e4 = poles of circle 2):
  y = [[1, 1, c1, 0], [1, 1, c2, 0], [conj c1, conj c2, 1, 0], [0, 0, 0, 1]], c1 = (1+2i)/5, c2 = (2-i)/5,
search a dual witness w in K'* n L2* (K'* = (PSD + L1) n L1*; L1* = {2|w12| <= w33 + w44}; L2* = {2|w34| <= w11 + w22})
with <y, w> < 0, w = B B^* + l1(u, Lam), Lam = max(|u|, |W12 - u| - (W33 + W44)/2), B in C^{4x4}; L2* enforced by a
penalty. Objective <y, w>/tr w, Nelder-Mead and Powell from random starts (fixed seed 20261030).
Control C1: the same search with y replaced by a member of K' (y0 = q + l1 with q PSD in L1* n L2*) must not go below
-1e-9 (no dual witness can exist for a member).
DECISION RULE (fixed before the first run): 'SUMMARY [N, numerical]' lines only, no VERDICT; print the best value and
the best w rounded to 3 decimals (candidate for exact verification in z2c).
"""
import sys
import numpy as np
from scipy.optimize import minimize

c1, c2 = (1 + 2j) / 5, (2 - 1j) / 5
Y = np.array([[1, 1, c1, 0], [1, 1, c2, 0], [np.conj(c1), np.conj(c2), 1, 0], [0, 0, 0, 1]], dtype=complex)


def ell1(u, lam):
    m = np.zeros((4, 4), dtype=complex)
    m[0, 1], m[1, 0] = -u, -np.conj(u)
    m[2, 2] = m[3, 3] = lam
    return m


def make_w(p):
    B = (p[:16] + 1j * p[16:32]).reshape(4, 4)
    W = B @ B.conj().T
    u = p[32] + 1j * p[33]
    lam = max(abs(u), abs(W[0, 1] - u) - np.real(W[2, 2] + W[3, 3]) / 2)
    return W + ell1(u, lam)


def obj(p, y):
    w = make_w(p)
    t = np.real(np.trace(w))
    pen = max(0.0, 2 * abs(w[2, 3]) - np.real(w[0, 0] + w[1, 1]))
    return float(np.real(np.trace(y @ w))) / t + 10.0 * pen / t


def search(y, seed, restarts):
    rng = np.random.default_rng(seed)
    best, bp = np.inf, None
    for r in range(restarts):
        p0 = rng.normal(size=34)
        for meth in ('Nelder-Mead', 'Powell'):
            res = minimize(obj, p0, args=(y,), method=meth, options={'maxiter': 40000})
            if res.fun < best:
                best, bp = res.fun, res.x
            p0 = res.x
    return best, bp


# control C1: a member of K' n (L2*-compatible)
q = np.array([[2, 0.5, 0.3, 0], [0.5, 2, 0, 0.2], [0.3, 0, 1, 0], [0, 0.2, 0, 1]], dtype=complex)
y0 = q + ell1(0.3 + 0.2j, 0.5)
b0, _ = search(y0, 20261031, 6)
print('C1  member y0: best normalized <y0, w> =', f'{b0:.2e}', '(must be >= -1e-9)')
if b0 < -1e-9:
    print('CONTROL FAILED: C1')
    sys.exit(1)

best, bp = search(Y, 20261030, 12)
print('N1  candidate y: best normalized <y, w> =', f'{best:.3e}')
w = make_w(bp)
w = w / np.real(np.trace(w))
print('N1  best w (trace-normalized, rounded):')
for row in np.round(w, 3):
    print('     ', [complex(round(z.real, 3), round(z.imag, 3)) for z in row])
ev = np.linalg.eigvalsh(w)
print('N1  eigenvalues of w (rounded):', [round(float(e), 3) for e in ev])
print('SUMMARY [N, numerical] search only; an exact dual witness, if any, is certified in z2c')
