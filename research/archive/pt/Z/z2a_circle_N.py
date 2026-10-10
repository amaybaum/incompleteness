"""z2a_circle_N.py -- thread Z, node S2, [N, numerical] exploration ONLY (guidance; certifies nothing).

Question explored: is the circle surgery K' = (PSD4 n L*) + L self-dual, where (basis e1 = p, e2 = p', e3, e4 of C^4;
V1 = span(e1, e2), V2 = span(e3, e4)) the defects are d_g = I - 2 phi_g phi_g^*, phi_g = (e1 + e^{ig} e2)/sqrt2
(the equator of V1), and L = cone{d_g} = { l(w, Lam) = -w E12 - conj(w) E21 + Lam (E33 + E44) : |w| <= Lam }?
Pairing <A, B> = tr(AB). L* = { y : 2|y12| <= y33 + y44 }. K'* = (PSD + L) n L*.
Membership y in K'  <=>  exists (x, Lam): Y(x, Lam) := y - l(x - y12, Lam) >= 0, Lam >= |x - y12|, |x| + Lam <= b/2,
b = y33 + y44. Test: maximize the concave h = min(lmin(Y), Lam - |x - a|, b/2 - |x| - Lam) (grid + Nelder-Mead);
margin = max h (>= 0 means member, up to tolerance).

Sections:
  N1  K': random y in K'* (y = z + l(w0, Lam0), Lam0 raised until y in L*), z random PSD of rank 1..4.
  N2  K': adversarial y = z + s d_beta with z near a pure cap state phi_alpha (alpha != beta), s minimal for L*.
  N3  K': adversarial y with V1-V2 coupling: z = v v^*, v = cos t phi_alpha + sin t u (u in V2), + s d_beta.
  N4  finite subsets of the circle (plain surgery with finitely many defects): the square {0, pi/2, pi, 3pi/2}
      and the triangle {0, 2pi/3, 4pi/3}, adversarial y = P_{phi_j} + s d_k (s minimal for Z*), and random y.
Controls (must behave as stated, else 'CONTROL FAILED' and exit 1):
  C1  pair {0, delta} with |<phi_0|phi_delta>|^2 = 1/4: y = P_0 + d_delta/(4c) is in K* and must show a clearly
      negative margin (< -1e-3) (the exact pair obstruction, see NOTES).
  C2  antipodal pair {0, pi} (orthogonal defects, lemma SD2): adversarial and random y must show no margin below -1e-7.
  C3  K' membership of y = q + l(w, Lam) with q in PSD n L* (constructed members) must show margin >= -1e-9.
DECISION RULE (fixed before the first run): print 'SUMMARY [N, numerical]' lines only, never a VERDICT; tolerance
1e-7 for 'no violation found'; seeds fixed (20261010 + section); printed numbers rounded to 3 significant digits.
"""
import sys
import numpy as np
from scipy.optimize import minimize

I4 = np.eye(4, dtype=complex)
FAILS = []


def lmin(m):
    return float(np.linalg.eigvalsh((m + m.conj().T) / 2)[0])


def phi(g):
    v = np.zeros(4, dtype=complex)
    v[0], v[1] = 1 / np.sqrt(2), np.exp(1j * g) / np.sqrt(2)
    return v


def dmat(g):
    v = phi(g)
    return I4 - 2 * np.outer(v, v.conj())


def ell(w, lam):
    m = np.zeros((4, 4), dtype=complex)
    m[0, 1], m[1, 0] = -w, -np.conj(w)
    m[2, 2] = m[3, 3] = lam
    return m


def rand_psd(rng, rank):
    a = rng.normal(size=(4, rank)) + 1j * rng.normal(size=(4, rank))
    m = a @ a.conj().T
    return m / np.real(np.trace(m))


def margin_circle(y):
    """max over (x, Lam) of min(lmin(Y), Lam - |x - a|, b/2 - |x| - Lam), y scaled to trace 1."""
    y = y / np.real(np.trace(y))
    a, b = y[0, 1], np.real(y[2, 2] + y[3, 3])

    def h(p):
        x = p[0] + 1j * p[1]
        lam = p[2]
        Y = y.copy()
        Y[0, 1], Y[1, 0] = x, np.conj(x)
        Y[2, 2] -= lam
        Y[3, 3] -= lam
        return min(lmin(Y), lam - abs(x - a), b / 2 - abs(x) - lam)

    R = abs(a) + b
    best, arg = -np.inf, None
    for xr in np.linspace(-R, R, 17):
        for xi in np.linspace(-R, R, 17):
            for lam in np.linspace(0, b / 2, 9):
                v = h((xr, xi, lam))
                if v > best:
                    best, arg = v, np.array([xr, xi, lam])
    res = minimize(lambda p: -h(p), arg, method='Nelder-Mead',
                   options={'xatol': 1e-12, 'fatol': 1e-14, 'maxiter': 6000})
    return max(best, -res.fun)


def margin_finite(y, gs):
    """plain surgery with defects d_g, g in gs: max over tau >= 0 of min(lmin(y - sum tau d), <y - sum tau d, d_g>)."""
    y = y / np.real(np.trace(y))
    ds = [dmat(g) for g in gs]

    def h(t):
        t = np.maximum(t, 0.0)
        r = y - sum(ti * d for ti, d in zip(t, ds))
        return min([lmin(r)] + [float(np.real(np.trace(r @ d))) for d in ds])

    best, arg = -np.inf, None
    grids = np.linspace(0, 1.0, 9)
    import itertools
    for t in itertools.product(grids, repeat=len(ds)):
        v = h(np.array(t))
        if v > best:
            best, arg = v, np.array(t)
    res = minimize(lambda t: -h(t), arg, method='Nelder-Mead',
                   options={'xatol': 1e-12, 'fatol': 1e-14, 'maxiter': 8000})
    return max(best, -res.fun)


def in_Lstar(y):
    return 2 * abs(y[0, 1]) <= np.real(y[2, 2] + y[3, 3]) + 1e-15


def raise_to_Lstar(z, w, lam):
    y = z + ell(w, lam)
    gap = 2 * abs(y[0, 1]) - np.real(y[2, 2] + y[3, 3])
    if gap > 0:
        lam = lam + gap / 2 + 1e-12
        y = z + ell(w, lam)
    return y


def minimal_s_finite(z, gk, gs):
    """smallest s >= 0 with z + s d_gk pairing >= 0 with every d_g, g in gs (bisection)."""
    dk = dmat(gk)

    def ok(s):
        y = z + s * dk
        return all(np.real(np.trace(y @ dmat(g))) >= -1e-14 for g in gs)
    lo, hi = 0.0, 1.0
    while not ok(hi):
        hi *= 2
    for _ in range(80):
        mid = (lo + hi) / 2
        lo, hi = (lo, mid) if ok(mid) else (mid, hi)
    return hi


def minimal_s_circle(z, gk):
    dk = dmat(gk)
    lo, hi = 0.0, 1.0
    while not in_Lstar(z + hi * dk):
        hi *= 2
    for _ in range(80):
        mid = (lo + hi) / 2
        lo, hi = (lo, mid) if in_Lstar(z + mid * dk) else (mid, hi)
    return hi


def r3(v):
    return f"{v:.2e}"


# ---- controls first
print('== C1 control: pair {0, delta}, c = 1/4, y = P_0 + d_delta/(4c)')
delta = 2 * np.arccos(0.5)          # cos^2(delta/2) = 1/4
c = 0.25
y = np.outer(phi(0), phi(0).conj()) + dmat(delta) / (4 * c)
mC1 = margin_finite(y, [0.0, delta])
print('C1  margin =', r3(mC1))
if not mC1 < -1e-3:
    FAILS.append('C1')

print('== C2 control: antipodal pair {0, pi} (SD2)')
rng = np.random.default_rng(20261010)
worst = np.inf
for i in range(60):
    if i % 2 == 0:
        z = rand_psd(rng, 1 + i % 4)
        gk = [0.0, np.pi][i % 4 // 2]
    else:
        al = rng.uniform(-0.6, 0.6)
        z = np.outer(phi(al), phi(al).conj()) + 0.05 * rand_psd(rng, 2)
        gk = np.pi
    s = minimal_s_finite(z, gk, [0.0, np.pi])
    worst = min(worst, margin_finite(z + s * dmat(gk), [0.0, np.pi]))
print('C2  samples 60; worst margin =', r3(worst))
if worst < -1e-7:
    FAILS.append('C2')

print('== C3 control: constructed members of K\'')
worst = np.inf
for i in range(40):
    q = rand_psd(rng, 1 + i % 4)
    gap = 2 * abs(q[0, 1]) - np.real(q[2, 2] + q[3, 3])
    if gap > 0:   # push q into L* by adding PSD weight on V2
        q = q + (gap / 2 + 1e-9) * np.diag([0, 0, 1, 1]).astype(complex)
    lam = rng.uniform(0, 1)
    w = lam * rng.uniform(0, 1) * np.exp(1j * rng.uniform(0, 2 * np.pi))
    worst = min(worst, margin_circle(q + ell(w, lam)))
print('C3  samples 40; worst margin =', r3(worst))
if worst < -1e-9:
    FAILS.append('C3')

if FAILS:
    print('CONTROL FAILED:', FAILS)
    sys.exit(1)

# ---- N1 random y in K'*
print('== N1  K\': random y in K\'* (seed 20261011)')
rng = np.random.default_rng(20261011)
worst, cnt = np.inf, 0
for i in range(150):
    z = rand_psd(rng, 1 + i % 4)
    lam = rng.uniform(0, 0.8)
    w = lam * rng.uniform(0, 1) * np.exp(1j * rng.uniform(0, 2 * np.pi))
    y = raise_to_Lstar(z, w, lam)
    m = margin_circle(y)
    cnt += 1
    worst = min(worst, m)
print('N1  samples', cnt, '; worst margin =', r3(worst))

# ---- N2 adversarial: cap state at alpha, single defect at beta
print('== N2  K\': adversarial y = z + s d_beta, z near the cap centre phi_alpha (seed 20261012)')
rng = np.random.default_rng(20261012)
worst, worst_ab = np.inf, None
for i in range(160):
    al = rng.uniform(0, 2 * np.pi)
    be = al + rng.uniform(0.05, np.pi)
    z = np.outer(phi(al), phi(al).conj())
    if i % 2 == 1:
        z = z + rng.uniform(0, 0.3) * rand_psd(rng, 1 + i % 3)
    s = minimal_s_circle(z, be)
    m = margin_circle(z + s * dmat(be))
    if m < worst:
        worst, worst_ab = m, (round(float((be - al) % (2 * np.pi)), 3))
print('N2  samples 160; worst margin =', r3(worst), '; at beta - alpha =', worst_ab)

# ---- N3 adversarial with V1-V2 coupling
print('== N3  K\': adversarial y with V1-V2 coupling (seed 20261013)')
rng = np.random.default_rng(20261013)
worst = np.inf
for i in range(160):
    al = rng.uniform(0, 2 * np.pi)
    be = al + rng.uniform(0.05, np.pi)
    t = rng.uniform(0.05, 1.2)
    u = np.zeros(4, dtype=complex)
    u[2:] = rng.normal(size=2) + 1j * rng.normal(size=2)
    u /= np.linalg.norm(u)
    v = np.cos(t) * phi(al) + np.sin(t) * u
    z = np.outer(v, v.conj())
    if i % 3 == 2:
        z = z + rng.uniform(0, 0.2) * rand_psd(rng, 2)
    s = minimal_s_circle(z, be)
    worst = min(worst, margin_circle(z + s * dmat(be)))
print('N3  samples 160; worst margin =', r3(worst))

# ---- N4 finite subsets of the circle
for name, gs in (('square', [0.0, np.pi / 2, np.pi, 3 * np.pi / 2]),
                 ('triangle', [0.0, 2 * np.pi / 3, 4 * np.pi / 3])):
    print(f'== N4  finite subset of the circle: {name} (seed 20261014)')
    rng = np.random.default_rng(20261014)
    worst = np.inf
    for j in range(len(gs)):
        for k in range(len(gs)):
            if j == k:
                continue
            z = np.outer(phi(gs[j]), phi(gs[j]).conj())
            s = minimal_s_finite(z, gs[k], gs)
            worst = min(worst, margin_finite(z + s * dmat(gs[k]), gs))
    print(f'N4  {name}: adversarial pairs (j, k): worst margin =', r3(worst))
    worst = np.inf
    for i in range(24):
        z = rand_psd(rng, 1 + i % 4)
        if i % 2 == 0:
            al = gs[i % len(gs)] + rng.uniform(-0.3, 0.3)
            z = np.outer(phi(al), phi(al).conj()) + 0.1 * z
        gk = gs[(i + 1) % len(gs)]
        s = minimal_s_finite(z, gk, gs)
        worst = min(worst, margin_finite(z + s * dmat(gk), gs))
    print(f'N4  {name}: random/biased samples 24: worst margin =', r3(worst))

print('SUMMARY [N, numerical] controls C1, C2, C3 behaved as stated; nothing above is a certificate')
