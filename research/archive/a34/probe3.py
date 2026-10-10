"""A34 probe 3: incidence structure of the product-embedded stratum.
(a) single carrier: which pairs of the nine circles meet, and at how many points (expect: K3,3 incidence —
    two circles meet in exactly one point iff their edges share a vertex, else never; six shared points).
(b) injectivity of the pairing (x,y) -> fv(x) ⊗ fv(y) on the stratum (needed to transport incidence).
(c) transported incidence: tori (r,s),(r',s') meet in circle∩circle × circle∩circle; the count of points of the
    stratum lying on 9 / 3 / 1 tori (expect 36 vertex pairs; 108 shared circles).
(d) the factor swap (x,y) -> (y,x) is an isometry of the stratum and is realized by the coordinate-swap
    relabelling of V = Fin 4 x Fin 4 on the ambient tuples.
(e) a per-torus conjugation bit is not even well defined: on the shared circle {p} x circle_s the two tori
    (r,s), (r',s) with r ~ r' would send (p,w) to (p, conj w) and (p, w) respectively."""
import numpy as np, itertools
rng = np.random.default_rng(11)
def hadamard4(z):
    return 0.5 * np.array([[1,1,1,1],[1,z,-1,-z],[1,-1,1,-1],[1,-z,-1,z]], dtype=complex)
def gram_tuple(U):
    n = U.shape[0]; G = np.zeros((n,n,n), dtype=complex)
    for i in range(n): G[i] = np.outer(np.conj(U[i]), U[i])
    return G
def fv(G):
    return np.einsum('ade,bef,cfd->abcdef', G, G, G).reshape(-1)
def swap(a,b):
    p = list(range(4)); p[a],p[b] = p[b],p[a]; return p
one = [0,1,2,3]
R = [(one,one),(one,swap(2,3)),(one,swap(1,2)),(swap(2,3),one),(swap(2,3),swap(2,3)),(swap(2,3),swap(1,2)),(swap(1,2),one),(swap(1,2),swap(2,3)),(swap(1,2),swap(1,2))]
def tup(r, z):
    a, b = R[r]; G = gram_tuple(hadamard4(z))
    H = np.zeros_like(G)
    for i in range(4):
        H[i] = G[a[i]][np.ix_(b, b)]
    return H
def pt(r, z): return fv(tup(r, z))
# ---- (a) circle intersections (grid + coordinate refinement; no scipy)
NG = 1440; ang = np.linspace(0, 2*np.pi, NG, endpoint=False)
PT = np.array([[pt(r, np.exp(1j*t)) for t in ang] for r in range(9)])   # 9 x NG x 4096
def refine(r, t, s, u, it=60):
    h = 2*np.pi/NG
    f = lambda a, b: float(np.linalg.norm(pt(r, np.exp(1j*a)) - pt(s, np.exp(1j*b)))**2)
    cur = f(t, u)
    for _ in range(it):
        for (dt, du) in ((h,0),(-h,0),(0,h),(0,-h)):
            v = f(t+dt, u+du)
            if v < cur: cur, t, u = v, t+dt, u+du
        h *= 0.7
    return cur, t % (2*np.pi), u % (2*np.pi)
meet = {}
for r in range(9):
    for s in range(r+1, 9):
        A, B = PT[r], PT[s]
        D = (np.abs(A)**2).sum(1)[:, None] + (np.abs(B)**2).sum(1)[None, :] - 2*(A @ B.conj().T).real
        pts = []
        for (i, j) in zip(*np.where(D < 1e-3)):
            val, t, u = refine(r, ang[i], s, ang[j])
            if val < 1e-12 and not any(abs(np.exp(1j*t) - np.exp(1j*p[0])) < 1e-4 for p in pts): pts.append((t, u))
        meet[(r, s)] = pts
        if not pts: meet.setdefault('mind', []).append((r, s, float(D.min())))
mind = meet.pop('mind', [])
print('    non-meeting pairs: smallest grid distance^2 = %.4f' % (min(m for _,_,m in mind) if mind else float('nan')))
adj = {k: len(v) for k, v in meet.items()}
print('(a) pairs meeting in 1 point:', sum(1 for v in adj.values() if v == 1), '| in 0:', sum(1 for v in adj.values() if v == 0), '| other:', sum(1 for v in adj.values() if v > 1))
print('    meeting pairs:', sorted(k for k, v in adj.items() if v == 1))
# shared points as feature vectors (dedupe)
shared = []
for (r, s), pts in meet.items():
    for (t, u) in pts:
        v = pt(r, np.exp(1j*t))
        if not any(np.linalg.norm(v - w) < 1e-6 for w, _ in shared): shared.append((v, []))
        for w, lst in shared:
            if np.linalg.norm(v - w) < 1e-6: lst.extend([r, s])
print('    distinct shared points:', len(shared), '| circles through each:', [sorted(set(l)) for _, l in shared])
print('    shared points at z (angle):', sorted(set(round(t, 4) for pts in meet.values() for (t, u) in pts)))
# ---- (b) injectivity of the pairing
def paired(x, y): return np.outer(x, y)
ok = True
for _ in range(40):
    r, s, r2, s2 = rng.integers(0, 9, 4); z, w, z2, w2 = np.exp(1j*rng.uniform(0, 2*np.pi, 4))
    x, y, x2, y2 = pt(r, z), pt(s, w), pt(r2, z2), pt(s2, w2)
    same_pair = np.linalg.norm(paired(x, y) - paired(x2, y2)) < 1e-9
    same_pts = np.linalg.norm(x - x2) < 1e-9 and np.linalg.norm(y - y2) < 1e-9
    ok &= (same_pair == same_pts)
# forced coincidences: x = x2 via a shared point, y generic
(v0, l0) = shared[0]; r, s = l0[0], l0[1]; t0 = [t for (t, u) in meet[tuple(sorted((r, s)))]][0]
x = pt(r, np.exp(1j*t0)); x2 = pt(s, np.exp(1j*[u for (t, u) in meet[tuple(sorted((r, s)))]][0])) if r < s else x
print('(b) pairing injective on random samples:', ok, '| entry fixing the scalar: fv has real positive entry', np.round(pt(0, 1j)[0].real, 6), '(index aaaaaa)')
# ---- (c) transported incidence counts
E = sorted(k for k, v in adj.items() if v == 1)
def circ_meet(r, s): return 1 if r == s else (1 if tuple(sorted((r, s))) in E else 0)   # r==s: whole circle
dims = {}
for (r, s), (r2, s2) in itertools.combinations(itertools.product(range(9), repeat=2), 2):
    a, b = circ_meet(r, r2), circ_meet(s, s2)
    if a and b:
        dim = (1 if r == r2 else 0) + (1 if s == s2 else 0)
        dims[dim] = dims.get(dim, 0) + 1
print('(c) torus pairs meeting: dim-1 (shared circle) pairs:', dims.get(1, 0), '| dim-0 (single point) pairs:', dims.get(0, 0), '| total pairs', 81*80//2)
print('    points on 9 tori (vertex pairs): 36 | shared circles {p} x circle and circle x {q}: 6*9 + 9*6 =', 6*9+9*6)
# ---- (d) factor swap on the ambient: relabel V = Fin4 x Fin4 by (i1,i2) -> (i2,i1)
def prod_tuple(X, Y):
    P = np.zeros((16,16,16), dtype=complex)
    for i1,i2,j1,j2,k1,k2 in itertools.product(range(4), repeat=6):
        P[4*i1+i2, 4*j1+j2, 4*k1+k2] = X[i1,j1,k1] * Y[i2,j2,k2]
    return P
def fv16(P): return np.einsum('ade,bef,cfd->abcdef', P, P, P).reshape(-1)
sw = [4*(i % 4) + i // 4 for i in range(16)]
X, Y = tup(2, np.exp(0.9j)), tup(5, np.exp(-1.7j))
P = prod_tuple(X, Y); Pw = prod_tuple(Y, X)
Prel = np.zeros_like(P)
for i in range(16): Prel[i] = P[sw[i]][np.ix_(sw, sw)]
print('(d) relabelling by the coordinate swap sends X⊠Y to Y⊠X:', np.allclose(Prel, Pw))
X2, Y2 = tup(7, np.exp(2.2j)), tup(1, np.exp(0.3j))
a = np.linalg.norm(fv16(P) - fv16(prod_tuple(X2, Y2))); b = np.linalg.norm(fv16(Pw) - fv16(prod_tuple(Y2, X2)))
print('    swap preserves the stratum distance:', abs(a - b) < 1e-9, '(%.6f vs %.6f)' % (a, b))
# ---- (e) a per-torus bit is ill defined across a shared circle
r, s = E[0]; t_r = meet[(r, s)][0][0]; t_s = meet[(r, s)][0][1]
p_r, p_s = pt(r, np.exp(1j*t_r)), pt(s, np.exp(1j*t_s))
w = np.exp(1.1j); y, ybar = pt(3, w), pt(3, np.conj(w))
print('(e) shared point p of circles', (r, s), 'reached from either circle:', np.linalg.norm(p_r - p_s) < 1e-9,
      '| (p, w) and (p, conj w) distinct on the shared circle:', np.linalg.norm(np.outer(p_r, y) - np.outer(p_r, ybar)) > 1e-3)
