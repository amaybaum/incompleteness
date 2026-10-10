"""A34 probe 7 (the P0-facing target): fixing one tensor factor reduces the stratum distance to the
single-carrier distance exactly, so a factorized map (f1, f2) preserving stratum distances has each factor
an isometry of N4; countercontrol: f1 = (z -> z^2 on circle 0), f2 = id fails on the stratum."""
import numpy as np
rng = np.random.default_rng(21)
def hadamard4(z):
    return 0.5 * np.array([[1,1,1,1],[1,z,-1,-z],[1,-1,1,-1],[1,-z,-1,z]], dtype=complex)
def gram_tuple(U):
    n = U.shape[0]; G = np.zeros((n,n,n), dtype=complex)
    for i in range(n): G[i] = np.outer(np.conj(U[i]), U[i])
    return G
def fv(G): return np.einsum('ade,bef,cfd->abcdef', G, G, G).reshape(-1)
def swap(a,b):
    p = list(range(4)); p[a],p[b] = p[b],p[a]; return p
one = [0,1,2,3]
R = [(one,one),(one,swap(2,3)),(one,swap(1,2)),(swap(2,3),one),(swap(2,3),swap(2,3)),(swap(2,3),swap(1,2)),(swap(1,2),one),(swap(1,2),swap(2,3)),(swap(1,2),swap(1,2))]
def pt(r, z):
    a, b = R[r]; G = gram_tuple(hadamard4(z)); H = np.zeros_like(G)
    for i in range(4): H[i] = G[a[i]][np.ix_(b, b)]
    return fv(H)
def d1(x, x2): return np.linalg.norm(x - x2)
def dS(x, y, x2, y2): return np.sqrt(max(0.0, 2 - 2*(np.vdot(x, x2)*np.vdot(y, y2)).real))
worst = 0.0
for _ in range(100):
    r, r2, s = rng.integers(0, 9, 3); z, z2, w = np.exp(1j*rng.uniform(0, 2*np.pi, 3))
    x, x2, y = pt(r, z), pt(r2, z2), pt(s, w)
    worst = max(worst, abs(dS(x, y, x2, y) - d1(x, x2)))
print('fixing the second factor: |d_Σ((x,y),(x\',y)) - d_N4(x,x\')| max = %.2e' % worst)
# countercontrol: the factor map z -> z^2 on circle 0, identity elsewhere, tensored with the identity
def f1(r, z): return (r, z*z if r == 0 else z)
worst2 = 0.0
for _ in range(100):
    z, z2, w = np.exp(1j*rng.uniform(0, 2*np.pi, 3)); s = rng.integers(0, 9)
    before = dS(pt(0, z), pt(s, w), pt(0, z2), pt(s, w))
    after = dS(pt(*f1(0, z)), pt(s, w), pt(*f1(0, z2)), pt(s, w))
    worst2 = max(worst2, abs(after - before))
print('countercontrol (z -> z^2 on circle 0) ⊗ id: max |Δ d_Σ| = %.3f (nonzero: not an isometry of Σ)' % worst2)
