"""A34 probe 2: does the A33 group act on the product-embedded stratum through f ⊗ g?
On the stratum, <fv(X⊠Y), fv(X'⊠Y')> = <fvX,fvX'><fvY,fvY'>, so dist is determined by the single-carrier
inner products. A33's isometries act on the nine circles by normal forms (ν, ε): pt r z ↦ pt σ(r) (λ (z or z̄)).
We test, for representative pairs (f,g), whether (x,y) ↦ f(x)⊗g(y) preserves distances on the stratum."""
import numpy as np, itertools, json
rng = np.random.default_rng(7)
def hadamard4(z):
    return 0.5 * np.array([[1,1,1,1],[1,z,-1,-z],[1,-1,1,-1],[1,-z,-1,z]], dtype=complex)
def gram_tuple(U):
    n = U.shape[0]; G = np.zeros((n,n,n), dtype=complex)
    for i in range(n): G[i] = np.outer(np.conj(U[i]), U[i])
    return G
def fv(G):
    return np.einsum('ade,bef,cfd->abcdef', G, G, G).reshape(-1)
I4 = np.eye(4, dtype=int)
def swap(a,b):
    p = list(range(4)); p[a],p[b] = p[b],p[a]; return p
one = [0,1,2,3]
R = [(one,one),(one,swap(2,3)),(one,swap(1,2)),(swap(2,3),one),(swap(2,3),swap(2,3)),(swap(2,3),swap(1,2)),(swap(1,2),one),(swap(1,2),swap(2,3)),(swap(1,2),swap(1,2))]
def pt(r, z):
    a, b = R[r]; G = gram_tuple(hadamard4(z))
    H = np.zeros_like(G)
    for i in range(4):
        H[i] = G[a[i]][np.ix_(b, b)]
    return fv(H)
# single-carrier inner-product function on circle points
def ip(r, z, s, w):
    return np.vdot(pt(r, z), pt(s, w))
# check: are single-carrier inner products real?
vals = [ip(r, np.exp(1j*rng.uniform(0,2*np.pi)), s, np.exp(1j*rng.uniform(0,2*np.pi))) for r in range(9) for s in range(9)]
print('max |Im <pt r z, pt s w>| over 81 random pairs:', max(abs(v.imag) for v in vals))
print('example values:', [np.round(v, 4) for v in vals[:4]])
# --- product stratum distances: d((x,y),(x',y'))^2 = 2 - 2 Re(<x,x'><y,y'>)  (all norms 1)
def dist2(ixx, iyy):
    return 2 - 2 * (ixx * iyy).real
# actions on circle points: a normal form (sigma, lam, eps): pt r z -> pt sigma[r] (lam[r] * (z if eps[r] else conj z))
def act(nf, r, z):
    sigma, lam, eps = nf
    return sigma[r], lam[r] * (z if eps[r] else np.conj(z))
ID = (list(range(9)), [1]*9, [True]*9)
CONJ = (list(range(9)), [1]*9, [False]*9)            # global conjugation
C0 = (list(range(9)), [1]*9, [False] + [True]*8)     # conjugate circle 0 only (kernel element outside the family)
ROWDBL = (list(range(9)), [1]*9, [False]*6 + [True]*3) # a family kernel element (row-DBL pattern)
# a relabelling automorphism: R1 = (1, s23): sigma from gen8 tables: [1,0,2,4,3,5,7,6,8], eps all true, lam? need the sign lam: read from A33's data if available
try:
    g8 = json.load(open('../a33/gen8.json'))['gens']
    R1 = (g8['0']['sigma'], g8['0']['lam'], [bool(x) for x in g8['0']['eps']])
    T = (g8['2']['sigma'], g8['2']['lam'], [bool(x) for x in g8['2']['eps']])
except Exception as e:
    R1 = None; T = None; print('gen8 tables unavailable', e)
def test(f, g, name, n=60):
    worst = 0.0
    for _ in range(n):
        r, s, r2, s2 = rng.integers(0, 9, 4)
        z, w, z2, w2 = [np.exp(1j*t) for t in rng.uniform(0, 2*np.pi, 4)]
        d_before = dist2(ip(r, z, r2, z2), ip(s, w, s2, w2))
        fr, fz = act(f, r, z); fr2, fz2 = act(f, r2, z2); gs, gw = act(g, s, w); gs2, gw2 = act(g, s2, w2)
        d_after = dist2(ip(fr, fz, fr2, fz2), ip(gs, gw, gs2, gw2))
        worst = max(worst, abs(d_after - d_before))
    print('%-28s max |Δ dist²| = %.3e  -> %s' % (name, worst, 'isometry of the stratum' if worst < 1e-9 else 'NOT an isometry'))
test(ID, ID, 'id ⊗ id')
test(CONJ, CONJ, 'conj ⊗ conj')
test(CONJ, ID, 'conj ⊗ id')
test(C0, ID, 'c0 ⊗ id')
test(C0, C0, 'c0 ⊗ c0')
test(ROWDBL, ID, 'rowDBL ⊗ id')
test(ROWDBL, ROWDBL, 'rowDBL ⊗ rowDBL')
if R1: test(R1, ID, 'R1 ⊗ id'); test(T, ID, 'T ⊗ id'); test(R1, T, 'R1 ⊗ T'); test(C0, R1, 'c0 ⊗ R1')
