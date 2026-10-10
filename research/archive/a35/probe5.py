"""probe5: do defect directions at a generic Σ point beyond the two Diţă constructions integrate?
Take a random first-order direction R in the defect space orthogonal to (Σ tangent + both Diţă
tangents + gauge), step H_ε = H∘e^{iεR}, project back onto the flat-unitary variety by Gauss–Newton
on the phases, and measure: distance of the projected point from H_ε (should scale like ε² if a
curve tangent to R exists), its Σ residual, its column- and row-Diţă residuals (fixed pairing), and
its defect."""
import numpy as np, itertools, sys, time
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from lib35 import *
rng = np.random.default_rng(355)
t0 = time.time()

def phase_tangent(f, p0, eps=1e-6):
    Hp, Hm = f(p0 + eps), f(p0 - eps)
    return np.angle(Hp / Hm) / (2 * eps)

def unit_residual(Phi, H):
    Hp = H * np.exp(1j * Phi)
    E = Hp @ np.conj(Hp).T - np.eye(16)
    iu = np.triu_indices(16, 1)
    return np.r_[E[iu].real, E[iu].imag]

def jac(Phi, H):
    """derivative of [Re E, Im E] (E = Hp Hp^H - I, i<j) wrt phase increments: dE_ij = i sum_k (δ_ik - δ_jk) c_k,
    so Re-rows are -Im(c), Im-rows are Re(c), in the residual's order (all Re rows, then all Im rows)."""
    Hp = H * np.exp(1j * Phi)
    n = 16
    re_rows, im_rows = [], []
    for i in range(n):
        for j in range(i + 1, n):
            c = Hp[i] * np.conj(Hp[j])
            row = np.zeros(n * n, dtype=complex)
            row[i * n:(i + 1) * n] += c
            row[j * n:(j + 1) * n] -= c
            re_rows.append(-row.imag); im_rows.append(row.real)
    return np.array(re_rows + im_rows)

def project(H, Phi0, iters=40):
    Phi = Phi0.copy()
    for it in range(iters):
        r = unit_residual(Phi, H)
        if np.linalg.norm(r) < 1e-13: break
        J = jac(Phi, H)
        step, *_ = np.linalg.lstsq(J, -r, rcond=1e-10)
        Phi = Phi + step.reshape(16, 16)
    return Phi, np.linalg.norm(unit_residual(Phi, H))

def dita_col_residual(H):
    """max deviation of within-column-block cross ratios from independence of the row block."""
    Hn = H / np.abs(H); H4 = Hn.reshape(4, 4, 4, 4)  # [a,b,c,d]
    worst = 0
    for c in range(4):
        for (b, bp) in itertools.combinations(range(4), 2):
            for (d, dp) in itertools.combinations(range(4), 2):
                cr = H4[:, b, c, d] * H4[:, bp, c, dp] / (H4[:, b, c, dp] * H4[:, bp, c, d])
                worst = max(worst, np.max(np.abs(cr - cr[0])))
    return worst
def dita_row_residual(H):
    return dita_col_residual(H.T)

z, w = np.exp(1j * rng.uniform(0, 2 * np.pi, 2))
X, Y = U_circle(0, z), U_circle(0, w)
H = kron(X, Y)
print('base Σ point: Σ residual %.1e, col-Diţă residual %.1e, row-Diţă residual %.1e' % (sigma_residual(H), dita_col_residual(H), dita_row_residual(H)))
# known tangents (gauge, Σ, both Diţă constructions)
known = []
for i in range(16):
    v = np.zeros((16, 16)); v[i, :] = 1; known.append(v)
    v = np.zeros((16, 16)); v[:, i] = 1; known.append(v)
known.append(phase_tangent(lambda t: kron(U_circle(0, z * np.exp(1j * t)), Y), 0.0))
known.append(phase_tangent(lambda t: kron(X, U_circle(0, w * np.exp(1j * t))), 0.0))
for c in range(4):
    for b in range(4):
        v = np.zeros((16, 16)); v[b::4, c * 4:(c + 1) * 4] = 1; known.append(v)
        v = np.zeros((16, 16)); v[c * 4:(c + 1) * 4, b::4] = 1; known.append(v)
for c in range(4):
    known.append(phase_tangent(lambda t, c=c: dita(X, [Y if k != c else U_circle(0, w * np.exp(1j * t)) for k in range(4)], np.ones((4, 4))), 0.0))
    known.append(phase_tangent(lambda t, c=c: dita_T(X, [Y if k != c else U_circle(0, w * np.exp(1j * t)) for k in range(4)], np.ones((4, 4))), 0.0))
Kmat = np.array([v.ravel() for v in known])
print('known tangent span rank (incl. gauge 31):', np.linalg.matrix_rank(Kmat, tol=1e-8))
# defect space: null space of the linearized unitarity
M = defect_system(H)
u, s, vt = np.linalg.svd(M)
null = vt[np.sum(s > 1e-8 * s[0]):]           # rows: basis of the defect space (incl. gauge)
print('null space dim (defect + 31):', null.shape[0])
# component orthogonal to the known span
Q, _ = np.linalg.qr(Kmat.T)
Nperp = null - (null @ Q) @ Q.T
sv = np.linalg.svd(Nperp, compute_uv=False)
print('dimension of defect directions beyond the known span:', int(np.sum(sv > 1e-8)))
u2, s2, vt2 = np.linalg.svd(Nperp)
basis_perp = vt2[:int(np.sum(sv > 1e-8))]

results = []
for trial in range(4):
    coeff = rng.normal(size=basis_perp.shape[0])
    R = (coeff @ basis_perp).reshape(16, 16); R /= np.linalg.norm(R)
    row = []
    for eps in (0.2, 0.1, 0.05, 0.025):
        Phi, res = project(H, eps * R)
        dev = np.linalg.norm(Phi - eps * R - np.mean(Phi - eps * R))  # crude: distance from the first-order point
        # distance in the ambient feature metric between the projected point and the first-order point, via gauge-invariant dist
        Hp = H * np.exp(1j * Phi)
        d_to_base = np.sqrt(max(dist2_U(Hp, H), 0))
        row.append((eps, res, d_to_base, sigma_residual(Hp), dita_col_residual(Hp), dita_row_residual(Hp), defect_numeric(Hp)[0]))
    results.append(row)
    print('direction %d:' % trial)
    for eps, res, d, sr, dc, dr, df in row:
        print('   ε=%.3f  unitarity residual %.1e  feature-dist to base %.4f (ratio to ε %.3f)  Σ-res %.3f  colDiţă-res %.3f  rowDiţă-res %.3f  defect %d' % (eps, res, d, d / eps, sr, dc, dr, df))
# control: the same projection started along a Diţă direction must land in the Diţă hull
Rd = np.zeros((16, 16)); Rd[1::4, 4:8] = 1.0
Phi, res = project(H, 0.3 * Rd)
Hp = H * np.exp(1j * Phi)
print('control (column-Diţă direction, ε=0.3): unitarity residual %.1e, Σ-res %.3f, colDiţă-res %.1e, rowDiţă-res %.3f, defect %d' % (res, sigma_residual(Hp), dita_col_residual(Hp), dita_row_residual(Hp), defect_numeric(Hp)[0]))
# control 2: a random direction *inside* the known span but off Σ: mixed row+column Diţă direction
Rm = np.zeros((16, 16)); Rm[1::4, 4:8] = 1.0; Rm[8:12, 2::4] += 1.3
Phi, res = project(H, 0.3 * Rm)
Hp = H * np.exp(1j * Phi)
print('control (row+column mixed, ε=0.3): unitarity residual %.1e, Σ-res %.3f, colDiţă-res %.3f, rowDiţă-res %.3f, defect %d' % (res, sigma_residual(Hp), dita_col_residual(Hp), dita_row_residual(Hp), defect_numeric(Hp)[0]))
print('(%.0fs)' % (time.time() - t0))
