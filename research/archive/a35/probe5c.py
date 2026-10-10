"""probe5b: second-order integrability of the defect directions at a generic Σ point, and where
alternating projections land when started off Σ along an extra direction."""
import numpy as np, itertools, sys, time
sys.path.insert(0, '.')
from lib35 import *
src = open('probe5.py').read()
exec(src[src.index('def phase_tangent'):src.index('z, w = np.exp')])
rng = np.random.default_rng(356)
z, w = np.exp(1j * rng.uniform(0, 2 * np.pi, 2))
X, Y = U_circle(0, z), U_circle(0, w); H = kron(X, Y)
exec(src[src.index('# known tangents'):src.index('results = []')])
# second-order obstruction: L(S) = -(1/2) Q(R) with Q(R)_ij = sum_k c_k (R_ik - R_jk)^2 ; solvable iff Q(R) in range(L)
n = 16
def Lmat_and_Q(R):
    rows = []; q = []
    for i in range(n):
        for j in range(i + 1, n):
            c = H[i] * np.conj(H[j])
            row = np.zeros(n * n, dtype=complex); row[i * n:(i + 1) * n] += c; row[j * n:(j + 1) * n] -= c
            rows.append(row); q.append(np.sum(c * (R[i] - R[j]) ** 2))
    L = np.array(rows); q = np.array(q)
    # complex system i*L S = q/2  ->  real: [Re; Im] of (i L) S = [Re; Im] of q/2
    A = np.vstack([(1j * L).real, (1j * L).imag]); b = np.r_[(q / 2).real, (q / 2).imag]
    return A, b
def obstruction(R):
    R = R / np.linalg.norm(R)
    A, b = Lmat_and_Q(R)
    S, *_ = np.linalg.lstsq(A, b, rcond=1e-10)
    return np.linalg.norm(A @ S - b)   # absolute, R normalised to unit Frobenius norm by the callers
# controls: directions in the known span (Σ tangent, Diţă tangents) must be unobstructed
print('obstruction, Σ tangent:            %.1e' % obstruction(known[32]))
print('obstruction, a column-Diţă phase:  %.1e' % obstruction(known[34]))
print('obstruction, a row-Diţă phase:     %.1e' % obstruction(known[35]))
Rmix = known[34] + 0.7 * known[36]; print('obstruction, two column-Diţă phases: %.1e' % obstruction(Rmix))
Rmix2 = known[34] + 0.7 * known[35]; print('obstruction, column + row Diţă phase: %.1e (expected nonzero: the two constructions do not combine)' % obstruction(Rmix2))
# extra directions
Kmat = np.array([v.ravel() for v in known])
M = defect_system(H); u, s, vt = np.linalg.svd(M); null = vt[np.sum(s > 1e-8 * s[0]):]
Q, _ = np.linalg.qr(Kmat.T); Nperp = null - (null @ Q) @ Q.T
u2, s2, vt2 = np.linalg.svd(Nperp); basis_perp = vt2[:int(np.sum(s2 > 1e-8))]
print('extra directions:', basis_perp.shape[0])
obs = [obstruction((rng.normal(size=basis_perp.shape[0]) @ basis_perp).reshape(16, 16)) for _ in range(5)]
print('|b| for a random extra direction: %.3f' % np.linalg.norm(Lmat_and_Q((rng.normal(size=basis_perp.shape[0]) @ basis_perp).reshape(16,16) / 1.0)[1]))
print('obstruction of 5 random extra directions: %s' % np.round(obs, 4))
obs = [obstruction((rng.normal(size=null.shape[0]) @ null).reshape(16, 16)) for _ in range(5)]
print('obstruction of 5 random directions in the whole defect space: %s' % np.round(obs, 4))
# minimize the obstruction over the unit sphere of the extra directions (random restarts, Nelder–Mead-free: coordinate descent)
def obs_of(coef):
    R = (coef @ basis_perp).reshape(16, 16); return obstruction(R / np.linalg.norm(R))
best = []
for trial in range(6):
    coef = rng.normal(size=basis_perp.shape[0]); val = obs_of(coef); step = 0.5
    for it in range(400):
        cand = coef + step * rng.normal(size=coef.shape); v = obs_of(cand)
        if v < val: coef, val = cand, v
        else: step *= 0.97
    best.append(val)
print('minimal obstruction found over the extra-direction sphere (6 restarts): %s' % np.round(best, 4))
# combined: extra + Diţă mixtures
def obs_of2(coef):
    R = (coef[:basis_perp.shape[0]] @ basis_perp + coef[basis_perp.shape[0]:] @ Kmat[31:]).reshape(16, 16); return obstruction(R / np.linalg.norm(R))
best = []
for trial in range(4):
    coef = rng.normal(size=basis_perp.shape[0] + Kmat.shape[0] - 31); coef[:basis_perp.shape[0]] *= 1.0; val = obs_of2(coef); step = 0.5
    for it in range(400):
        cand = coef + step * rng.normal(size=coef.shape); v = obs_of2(cand)
        if v < val: coef, val = cand, v
        else: step *= 0.97
    R = (coef[:basis_perp.shape[0]] @ basis_perp).reshape(16, 16)
    best.append((round(val, 4), round(np.linalg.norm(R) / np.linalg.norm((coef[:basis_perp.shape[0]] @ basis_perp + coef[basis_perp.shape[0]:] @ Kmat[31:])), 3)))
print('minimal obstruction over mixed directions (value, extra-component fraction): %s' % best)
