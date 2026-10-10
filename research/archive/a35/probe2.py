"""probe2: the defect (linearized dimension of N16 modulo phases) at points of Σ and off it, exact
where the entries are fourth roots of unity, numerical elsewhere; and the tangent rank of the two
Diţă constructions (column-block twists and row-block twists) against it."""
import numpy as np, itertools, sys, time
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from lib35 import *
from sympy.polys.matrices import DomainMatrix
from sympy import QQ
rng = np.random.default_rng(352)

def defect_exact(H):
    """H with entries in {±1, ±i}/4 (or /2): integer system, exact rank over QQ."""
    n = H.shape[0]
    Hn = np.round(H * np.sqrt(n)).astype(complex)  # entries in {±1, ±i}
    assert np.allclose(Hn, H * np.sqrt(n)) and np.allclose(np.abs(Hn), 1)
    rows = []
    for i in range(n):
        for j in range(i + 1, n):
            c = Hn[i] * np.conj(Hn[j])
            row = np.zeros(n * n, dtype=complex)
            row[i * n:(i + 1) * n] += c
            row[j * n:(j + 1) * n] -= c
            rows.append([int(round(x)) for x in row.real]); rows.append([int(round(x)) for x in row.imag])
    M = DomainMatrix([[QQ(x) for x in r] for r in rows], (len(rows), n * n), QQ)
    rank = M.rank()
    return n * n - rank - (2 * n - 1)

def phase_tangent(f, p0, eps=1e-6):
    """R = d arg H / dp at p0 for a family f(p) of flat matrices, by a symmetric difference of args."""
    Hp, Hm = f(p0 + eps), f(p0 - eps)
    return np.angle(Hp / Hm) / (2 * eps)

def dita_tangents(X, Ys, D, include_T=True, Es=None, E=None):
    """tangent vectors at H = dita(X, Ys, D): X's circle parameter (X assumed F4(z)-relabelled: we move z),
    each Ys[c]'s parameter, each D[c,b] phase; optionally the transposed construction's E phases and
    its own Ys (only meaningful where both constructions pass through H, i.e. at D = E = 1)."""
    vs = []
    n = X.shape[0]
    # D phases
    for c in range(n):
        for b in range(n):
            R = np.zeros((16, 16)); R[b::4, c * 4:(c + 1) * 4] = 1  # rows (a,b) for all a; columns (c,d)
            vs.append(R)
    if include_T:
        for a in range(n):
            for d in range(n):
                R = np.zeros((16, 16)); R[a * 4:(a + 1) * 4, d::4] = 1
                vs.append(R)
    return vs

def circle_param_tangent(H_of_t, t0):
    return phase_tangent(H_of_t, t0)

t0 = time.time()
print('== exact defects at fourth-root points of Σ (X = circle r at z, Y = circle s at w) ==')
pts = [('H4⊗H4 (vertex,vertex) z=w=1', 0, 1, 0, 1), ('F4⊗F4  z=w=i', 0, 1j, 0, 1j), ('H4⊗F4  z=1,w=i', 0, 1, 0, 1j),
       ('circles 2,5 z=w=i', 2, 1j, 5, 1j), ('circles 2,5 z=1,w=i', 2, 1, 5, 1j)]
for name, r, z, s, w in pts:
    H = kron(U_circle(r, z), U_circle(s, w))
    print('  %-32s defect %3d' % (name, defect_exact(H)))
print('  (%.0fs)' % (time.time() - t0))

print('== numeric defects at generic points ==')
for k in range(3):
    z, w = np.exp(1j * rng.uniform(0, 2 * np.pi, 2)); r, s = rng.integers(0, 9, 2)
    H = kron(U_circle(r, z), U_circle(s, w))
    d, sv = defect_numeric(H)
    print('  Σ generic (r=%d,s=%d)      defect %3d   (singular gap %.1e / %.1e)' % (r, s, d, sv[256 - (2 * 16 - 1) - d - 1], sv[256 - (2 * 16 - 1) - d]))
# the A34 witness (fourth roots) and a generic Diţă point
Fi = F4(1j)
Dw = np.ones((4, 4), dtype=complex); Dw[1, :] = [1, 1j, 1, -1j]
Hw = dita(Fi, [Fi] * 4, Dw)
print('  Diţă witness (fourth roots)  exact defect %3d   sigma_residual %.3f' % (defect_exact(Hw), sigma_residual(Hw)))
for k in range(3):
    zx = np.exp(1j * rng.uniform(0, 2 * np.pi)); ws = np.exp(1j * rng.uniform(0, 2 * np.pi, 4))
    D = np.exp(1j * rng.uniform(0, 2 * np.pi, (4, 4)))
    Hd = dita(U_circle(rng.integers(0, 9), zx), [U_circle(rng.integers(0, 9), w) for w in ws], D)
    d, sv = defect_numeric(Hd)
    print('  Diţă generic (4 distinct Ys) defect %3d   unitary %s sigma_residual %.3f' % (d, is_unitary(Hd), sigma_residual(Hd)))
    Hd1 = dita(U_circle(0, zx), [U_circle(0, ws[0])] * 4, D)
    d1, _ = defect_numeric(Hd1)
    print('  Diţă generic (equal Ys)      defect %3d' % d1)

print('== tangent rank of the Diţă constructions modulo phases ==')
# at a generic Σ point: column-twist family (D: 16 phases, Ys: 4 params, X: 1) and row-twist family (E, Ys', X)
z, w = np.exp(1j * rng.uniform(0, 2 * np.pi, 2))
X, Y = U_circle(0, z), U_circle(0, w)
H0 = kron(X, Y)
vs_col = dita_tangents(X, [Y] * 4, None, include_T=False)
vs_row = dita_tangents(X, [Y] * 4, None, include_T=True)[16:]
# parameter directions: X's z, and each Y_c's w (column construction) / each Y_a's w (row construction)
def fam_col(c):
    def f(t):
        Ys = [Y] * 4; Ys = list(Ys); Ys[c] = U_circle(0, w * np.exp(1j * t)); return dita(X, Ys, np.ones((4, 4)))
    return f
def fam_row(a):
    def f(t):
        Ys = list([Y] * 4); Ys[a] = U_circle(0, w * np.exp(1j * t)); return dita_T(X, Ys, np.ones((4, 4)))
    return f
vX = [phase_tangent(lambda t: kron(U_circle(0, z * np.exp(1j * t)), Y), 0.0)]
vYc = [phase_tangent(fam_col(c), 0.0) for c in range(4)]
vYa = [phase_tangent(fam_row(a), 0.0) for a in range(4)]
print('  column construction (X, Y_c, D):     rank', tangent_rank(vX + vYc + vs_col, 16))
print('  row construction    (X, Y_a, E):     rank', tangent_rank(vX + vYa + vs_row, 16))
print('  both together at the Σ point:         rank', tangent_rank(vX + vYc + vYa + vs_col + vs_row, 16))
print('  Σ itself (X, Y):                      rank', tangent_rank(vX + [phase_tangent(lambda t: kron(X, U_circle(0, w * np.exp(1j * t))), 0.0)], 16))
d0, _ = defect_numeric(H0)
print('  defect at this Σ point:               ', d0)
# at F4⊗F4 exactly
X, Y = U_circle(0, 1j), U_circle(0, 1j); H0 = kron(X, Y); z = w = 1j
vX = [phase_tangent(lambda t: kron(U_circle(0, z * np.exp(1j * t)), Y), 0.0)]
vYc = [phase_tangent(fam_col(c), 0.0) for c in range(4)]
vYa = [phase_tangent(fam_row(a), 0.0) for a in range(4)]
print('  at F4⊗F4: both constructions rank', tangent_rank(vX + vYc + vYa + vs_col + vs_row, 16), ' exact defect', defect_exact(H0))
X, Y = U_circle(0, 1), U_circle(0, 1); H0 = kron(X, Y); z = w = 1
vX = [phase_tangent(lambda t: kron(U_circle(0, z * np.exp(1j * t)), Y), 0.0)]
vYc = [phase_tangent(fam_col(c), 0.0) for c in range(4)]
vYa = [phase_tangent(fam_row(a), 0.0) for a in range(4)]
print('  at H4⊗H4: both constructions rank', tangent_rank(vX + vYc + vYa + vs_col + vs_row, 16), ' exact defect', defect_exact(H0))
# at a generic Diţă point: the column construction's own tangent (X, Y_c, D) vs the defect there
zx = np.exp(1j * rng.uniform(0, 2 * np.pi)); ws = np.exp(1j * rng.uniform(0, 2 * np.pi, 4)); D = np.exp(1j * rng.uniform(0, 2 * np.pi, (4, 4)))
X = U_circle(0, zx); Ys = [U_circle(0, w) for w in ws]; Hd = dita(X, Ys, D)
vX = [phase_tangent(lambda t: dita(U_circle(0, zx * np.exp(1j * t)), Ys, D), 0.0)]
vY = [phase_tangent((lambda c: (lambda t: dita(X, [Ys[k] if k != c else U_circle(0, ws[c] * np.exp(1j * t)) for k in range(4)], D)))(c), 0.0) for c in range(4)]
print('  generic Diţă point: own tangent rank', tangent_rank(vX + vY + vs_col, 16), ' numeric defect', defect_numeric(Hd)[0])
print('(%.0fs)' % (time.time() - t0))
