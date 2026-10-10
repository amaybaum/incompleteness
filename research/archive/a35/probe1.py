"""probe1: the landed geometry rebuilt, and the Σ-membership criterion.
(a) trace formula for feature inner products == the definition (single carrier, exact vector)
(b) the nine circles: distinct, six vertices at z = ±1 are the real Hadamard points, K3,3 incidence
(c) inner product on a circle depends on z̄z' only; the Laurent coefficients
(d) Σ-membership: dephased Kronecker test == rank-one paired feature test on products, and on the
    Diţă witness (column twists (i,-i,i,-i) at F4(i) ⊗ F4(i)); the exact violating cross ratios."""
import numpy as np, itertools, sys
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from lib35 import *
rng = np.random.default_rng(35)

# (a)
for _ in range(3):
    z, zp = np.exp(1j * rng.uniform(0, 2 * np.pi, 2))
    r, rp = rng.integers(0, 9, 2)
    U, Up = U_circle(r, z), U_circle(rp, zp)
    M, Mp = mixed_triple(tuple_of_U(U)), mixed_triple(tuple_of_U(Up))
    ip_def = np.sum(np.conj(M) * Mp)
    print('(a) inner def %.12f%+.12fi  trace %.12f%+.12fi' % (ip_def.real, ip_def.imag, inner_U(U, Up).real, inner_U(U, Up).imag))
print('(a) norm^2 of a point', inner_U(U, U).real)

# (b)
zs = np.exp(1j * np.linspace(0, 2 * np.pi, 24, endpoint=False))
def circle_pts(r): return [U_circle(r, z) for z in zs]
def min_d2(r, s):
    return min(dist2_U(a, b) for a in circle_pts(r) for b in circle_pts(s))
print('(b) pairwise min squared distance between circles (0 = meet on the grid):')
meet = {}
for r in range(9):
    print('   ', ' '.join('%5.2f' % min_d2(r, s) for s in range(9)))
# vertices: z = ±1 real Hadamards; which circles share the point?
def same_class(U, Up): return dist2_U(U, Up) < 1e-9
verts = {}
for r in range(9):
    for z in (1, -1):
        U = U_circle(r, z)
        key = None
        for k, Uk in verts.items():
            if same_class(U, Uk): key = k; break
        if key is None: verts[(r, z)] = U; key = (r, z)
        print('    circle %d z=%+d -> vertex %s  (real matrix: %s)' % (r, z, key, np.allclose(U.imag, 0)))
print('(b) number of distinct vertices', len(verts))

# (c)
r = 0
z0 = 1.0
ts = np.linspace(0, 2 * np.pi, 8, endpoint=False)
c = np.array([inner_U(U_circle(r, z0), U_circle(r, z0 * np.exp(1j * t))) for t in ts])
print('(c) inner product along circle 0 vs parameter difference t (imag parts):', np.max(np.abs(c.imag)))
# Laurent coefficients via FFT on 8 samples: c(t) = sum_k n_k e^{ikt}
coef = np.fft.fft(c.real) / 8
print('(c) coefficients k=0..7 (k>4 are negative frequencies):', np.round(coef.real, 6))
# same for other circles and rotation invariance
for r in range(1, 9):
    c2 = np.array([inner_U(U_circle(r, np.exp(1j * 0.7)), U_circle(r, np.exp(1j * (0.7 + t)))) for t in ts]).real
    assert np.allclose(c2, c.real, atol=1e-12)
print('(c) same function on all nine circles, at a shifted base point: yes')

# (d)
X, Y = U_circle(2, np.exp(0.3j)), U_circle(5, np.exp(1.1j))
H = kron(X, Y)
print('(d) product: unitary %s flat %s sigma_residual %.2e' % (is_unitary(H), is_flat(H), sigma_residual(H)))
# the A34 witness: F4(i) ⊗ F4(i) with column twists (i,-i,i,-i) on block column c: D[c, b] = i^{?}
Fi = F4(1j)
D = np.array([[1j if b % 2 == 0 else -1j for b in range(4)] for c in range(4)])  # the twist (i,-i,i,-i) per row-within-block
# A34's PROPER text: `(if j.1.val % 2 = 0 then Complex.I else -Complex.I)` -- twist indexed by j.1 (the block row of the
# column index?) — both readings are tested:
Hw1 = dita(Fi, [Fi] * 4, D)                       # twist depends on b (row within block) — a left gauge? no: D[c,b] here is constant in c
Hw2 = np.kron(Fi, Fi) * np.array([[1j if (j // 4) % 2 == 0 else -1j for j in range(16)] for i in range(16)])
Hw3 = np.kron(Fi, Fi) * np.array([[(1j if ((i % 4) % 2 == 0) else -1j) if (j // 4) % 2 == 1 else 1 for j in range(16)] for i in range(16)])
for name, Hw in (('twist by row-in-block only', Hw1), ('twist by column block only', Hw2), ('twist by (column block, row in block)', Hw3)):
    print('(d) %-40s unitary %s flat %s sigma_residual %.3f' % (name, is_unitary(Hw), is_flat(Hw), sigma_residual(Hw)))
# a genuine Diţă twist: D[c,b] with c- and b-dependence
Dg = np.ones((4, 4), dtype=complex); Dg[1, :] = [1, 1j, 1, -1j]
Hd = dita(Fi, [Fi] * 4, Dg)
print('(d) Diţă twist D[1,:]=(1,i,1,-i): unitary %s flat %s sigma_residual %.3f' % (is_unitary(Hd), is_flat(Hd), sigma_residual(Hd)))
# where does it fail: list the violated (a,b,c,d) entries of the dephased Kronecker test
Dd = dephase(Hd).reshape(4, 4, 4, 4)
P = np.einsum('ac,bd->abcd', Dd[:, 0, :, 0], Dd[0, :, 0, :]) / dephase(Hd)[0, 0]
bad = [(a, b, c, d, np.round(Dd[a, b, c, d] * 4, 6), np.round(P[a, b, c, d] * 4, 6)) for a, b, c, d in itertools.product(range(4), repeat=4) if abs(Dd[a, b, c, d] - P[a, b, c, d]) > 1e-9]
print('(d) violated entries (a,b,c,d, 4*value, 4*predicted):', len(bad)); [print('     ', x) for x in bad[:8]]
# the exact obstruction as a cross ratio with equal first row-index and equal second column-index
def cross(H, r1, r2, c1, c2):
    return H[r1, c1] * H[r2, c2] / (H[r1, c2] * H[r2, c1])
vals = set()
for a, b, bp, c, cp, d in itertools.product(range(4), repeat=6):
    if b == bp or c == cp: continue
    v = cross(Hd, 4 * a + b, 4 * a + bp, 4 * c + d, 4 * cp + d)
    vals.add((round(v.real, 6), round(v.imag, 6)))
print('(d) cross ratios rows (a,b),(a,b\') cols (c,d),(c\',d) on the twisted matrix:', sorted(vals))
vals = set()
for a, b, bp, c, cp, d in itertools.product(range(4), repeat=6):
    if b == bp or c == cp: continue
    v = cross(H, 4 * a + b, 4 * a + bp, 4 * c + d, 4 * cp + d)
    vals.add((round(v.real, 6), round(v.imag, 6)))
print('(d) the same cross ratios on a product:', sorted(vals))
