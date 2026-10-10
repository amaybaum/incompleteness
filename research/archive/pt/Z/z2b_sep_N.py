"""z2b_sep_N.py -- thread Z, node S2, [N, numerical] search ONLY (guidance; certifies nothing).

Goal: find y, w in K'* with <y, w> < 0, where K' is the circle surgery of z2a (basis e1 = p, e2 = p', e3, e4;
defects d_g = I - 2 phi_g phi_g^*, phi_g = (e1 + e^{ig} e2)/sqrt2; L = {l(u, Lam) = -u E12 - conj(u) E21 +
Lam (E33 + E44) : |u| <= Lam}; L* = {y : 2|y12| <= y33 + y44}; K'* = (PSD + L) n L*). Such a pair shows K'* is not
self-positive, i.e. K' is not self-dual; it is a candidate for the exact certificate of z2c.
Families (minimal Lam keeps y in L* and in PSD + L: Lam = max(|u|, |Z12 - u| - (Z33 + Z44)/2)):
  F1  y = A A^* + l(u, Lam), A in C^{4x2}; same for w.  (general rank <= 2 part)
  F2  y = P_v + s d_beta, v in C^4 unit, s minimal with y in L*  (pure part + one defect); same for w.
Objective: <y, w> / (tr y tr w), minimized by Nelder-Mead from random starts (fixed seeds).
Control: C1  F2 restricted to v, u on the circle with the defect of w at the cap centre of y and vice versa
  (the pair family of NOTES N5, with the full circle's constraints) is reported; the plain pair value c - 1/(4c)
  at c = 1/4 (-3/4 in this normalization) is recomputed for the finite pair as a harness check (must be -0.75).
DECISION RULE (fixed before the first run): print 'SUMMARY [N, numerical]' lines only, never a VERDICT; report the
best value per family and its parameters rounded to 3 decimals; seeds fixed (20261020 + family).
"""
import sys
import numpy as np
from scipy.optimize import minimize

FAILS = []


def ell(u, lam):
    m = np.zeros((4, 4), dtype=complex)
    m[0, 1], m[1, 0] = -u, -np.conj(u)
    m[2, 2] = m[3, 3] = lam
    return m


def phi(g):
    v = np.zeros(4, dtype=complex)
    v[0], v[1] = 1 / np.sqrt(2), np.exp(1j * g) / np.sqrt(2)
    return v


def dmat(g):
    v = phi(g)
    return np.eye(4) - 2 * np.outer(v, v.conj())


def lam_min(Z, u):
    return max(abs(u), abs(Z[0, 1] - u) - np.real(Z[2, 2] + Z[3, 3]) / 2)


def ip(a, b):
    return float(np.real(np.trace(a @ b)))


def from_F1(p):
    A = (p[:8] + 1j * p[8:16]).reshape(4, 2)
    Z = A @ A.conj().T
    u = p[16] + 1j * p[17]
    return Z + ell(u, lam_min(Z, u))


def s_min_circle(Z, beta):
    # smallest s >= 0 with 2|Z12 - s e^{-i beta}| <= Z33 + Z44 + 2 s  (solve the quadratic exactly in floats)
    a, b0 = Z[0, 1], np.real(Z[2, 2] + Z[3, 3])
    e = np.exp(-1j * beta)
    # |a - s e|^2 <= (b0/2 + s)^2  <=>  |a|^2 - 2 s Re(a conj e) <= b0^2/4 + b0 s
    num = abs(a) ** 2 - b0 ** 2 / 4
    den = 2 * np.real(a * np.conj(e)) + b0
    if num <= 0:
        return 0.0
    if den <= 0:
        return np.inf
    return num / den


def from_F2(p):
    v = p[:4] + 1j * p[4:8]
    v = v / np.linalg.norm(v)
    Z = np.outer(v, v.conj())
    s = s_min_circle(Z, p[8])
    return Z + s * dmat(p[8]) if np.isfinite(s) else None


def obj(p, maker, n):
    y, w = maker(p[:n]), maker(p[n:])
    if y is None or w is None:
        return 10.0
    return ip(y, w) / (np.real(np.trace(y)) * np.real(np.trace(w)))


# harness check: plain pair at c = 1/4 in matrix normalization: <y, w> = c - 1/(4c) = -0.75
c = 0.25
delta = 2 * np.arccos(0.5)
Pl, Pj = np.outer(phi(0), phi(0).conj()), np.outer(phi(delta), phi(delta).conj())
yv, wv = Pl + dmat(delta) / (4 * c), Pj + dmat(0) / (4 * c)
hv = ip(yv, wv)
print('C1  plain pair c = 1/4: <y, w> =', f'{hv:.6f}', '(expected -0.750000)')
if abs(hv + 0.75) > 1e-12:
    FAILS.append('C1')
if FAILS:
    print('CONTROL FAILED:', FAILS)
    sys.exit(1)

for fam, maker, n in (('F1', from_F1, 18), ('F2', from_F2, 9)):
    rng = np.random.default_rng(20261020 + int(fam[1]))
    best, bestp = np.inf, None
    for r in range(40):
        p0 = rng.normal(size=2 * n)
        res = minimize(obj, p0, args=(maker, n), method='Nelder-Mead',
                       options={'maxiter': 20000, 'xatol': 1e-10, 'fatol': 1e-12})
        if res.fun < best:
            best, bestp = res.fun, res.x
    print(f'{fam}  restarts 40; best normalized <y, w> = {best:.3e}')
    if fam == 'F2':
        for half, name in ((bestp[:n], 'y'), (bestp[n:], 'w')):
            v = half[:4] + 1j * half[4:8]
            v = v / np.linalg.norm(v)
            ph = np.exp(-1j * np.angle(v[0])) if abs(v[0]) > 1e-9 else 1.0
            v = v * ph
            print(f'F2  {name}: v = {np.round(v, 3).tolist()}, beta mod 2pi = {round(float(half[8] % (2 * np.pi)), 3)}')
    else:
        for half, name in ((bestp[:n], 'y'), (bestp[n:], 'w')):
            M = from_F1(half)
            M = M / np.real(np.trace(M))
            print(f'F1  {name} (trace-normalized, rounded):')
            for row in np.round(M, 3):
                print('     ', [complex(round(z.real, 3), round(z.imag, 3)) for z in row])
print('SUMMARY [N, numerical] search only; candidates are certified, if at all, in z2c')
