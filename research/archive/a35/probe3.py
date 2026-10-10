"""probe3: which part of act 33's group is induced by matrix operations (relabellings, conjugation,
transpose) and therefore extends to N16; the wreath action on the strata (orbits on tori, shared
circles, vertex pairs); and the stabilizers of Σ points and of off-locus classes under the group
of product relabellings, factor swap, conjugation and transpose acting on N16."""
import numpy as np, itertools, sys, time
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from lib35 import *
from sympy.combinatorics import Permutation, PermutationGroup
rng = np.random.default_rng(353)
t0 = time.time()

# ---- the grid: 9 circles x 8 eighth roots; a map of N4 acting by z -> ±z, ±z̄ permutes it
K = 8
def key(r, k):
    """the class of the grid point (r, k): the vertices z = ±1 are shared (z = 1 is v1 r, z = -1 is v2 r)."""
    if k == 0: return ('v', V1[r])
    if k == K // 2: return ('v', V2[r])
    return (r, k)
grid = sorted({key(r, k) for r in range(9) for k in range(K)}, key=str)
gidx = {g: n for n, g in enumerate(grid)}
zk = lambda k: np.exp(2j * np.pi * k / K)
def U_of_key(g):
    if g[0] == 'v':
        r = V1.index(g[1]) if g[1] in V1 else None
        return U_circle(r, 1) if r is not None else U_circle(V2.index(g[1]), -1)
    return U_circle(g[0], zk(g[1]))
Ugrid = {g: U_of_key(g) for g in grid}
print('grid classes:', len(grid), '(72 pairs less 12 shared-vertex identifications = 60)')
# consistency: every (r,k) lands on its key's class
for r in range(9):
    for k in range(K):
        assert dist2_U(U_circle(r, zk(k)), Ugrid[key(r, k)]) < 1e-9

def locate(U):
    """the grid class whose point is U's (distance 0), or None."""
    for g, Ug in Ugrid.items():
        if dist2_U(U, Ug) < 1e-8: return g
    return None

def perm_of(op):
    img = []
    for g in grid:
        h = locate(op(Ugrid[g]))
        assert h is not None, ('not on the grid', g)
        img.append(gidx[h])
    return Permutation(img)

def relabel(pi, tau): return lambda U: U[np.ix_(pi, tau)]
ops = {}
for name, pi in (('pi=(01)', swap(0, 1)), ('pi=(0123)', (1, 2, 3, 0))):
    ops[name] = relabel(pi, ID4)
for name, tau in (('tau=(01)', swap(0, 1)), ('tau=(0123)', (1, 2, 3, 0))):
    ops[name] = relabel(ID4, tau)
ops['conj'] = lambda U: np.conj(U)
ops['transpose'] = lambda U: U.T
perms = {n: perm_of(op) for n, op in ops.items()}
G_mat = PermutationGroup(list(perms.values()))
G_rel = PermutationGroup([perms[n] for n in perms if n.startswith('pi') or n.startswith('tau')])
G_relc = PermutationGroup([perms[n] for n in perms if n != 'transpose'])
print('matrix-induced subgroup of A33 on the grid: relabellings %d, +conj %d, +transpose %d' % (G_rel.order(), G_relc.order(), G_mat.order()))

# ---- the full A33 group on the grid: (nu, eps) with nu an automorphism of the K3,3 with edges (V1[r],V2[r])
edges = [(V1[r], V2[r]) for r in range(9)]
def circle_of(u, v):
    for s in range(9):
        if {V1[s], V2[s]} == {u, v}: return s
autos = []
for nu in itertools.permutations(range(6)):
    if all(circle_of(nu[u], nu[v]) is not None for u, v in edges): autos.append(nu)
print('automorphisms of K3,3 on the six vertices:', len(autos))
def a33_perm(nu, eps):
    img = []
    for g in grid:
        if g[0] == 'v':
            img.append(gidx[('v', nu[g[1]])]); continue
        r, k = g
        s = circle_of(nu[V1[r]], nu[V2[r]])
        kk = k if eps[r] else (-k) % K
        if nu[V1[r]] == V1[s]: img.append(gidx[key(s, kk)])
        else: img.append(gidx[key(s, (kk + K // 2) % K)])
    return Permutation(img)
gens = [a33_perm(nu, (True,) * 9) for nu in autos[:12]] + [a33_perm(tuple(range(6)), tuple(r == j for r in range(9))) for j in range(9)]
G33 = PermutationGroup(gens)
print('A33 on the grid: order %d (expected 36864); matrix-induced subgroup contained: %s; index %d' % (G33.order(), all(G33.contains(g) for g in G_mat.generators), G33.order() // G_mat.order()))
# is a single-circle conjugation bit matrix-induced?  is global conjugation-of-all-bits?  which (nu,eps) are?
single = a33_perm(tuple(range(6)), tuple(r == 0 for r in range(9)))
allbits = a33_perm(tuple(range(6)), (False,) * 9)
print('single-circle bit in matrix-induced subgroup:', G_mat.contains(single), '; all-bits flip:', G_mat.contains(allbits))
# the kernel bits reachable by matrix operations: elements of G_mat with nu = identity
ker_bits = set()
for nu in [tuple(range(6))]:
    for eps in itertools.product([True, False], repeat=9):
        if G_mat.contains(a33_perm(nu, eps)): ker_bits.add(eps)
print('bit patterns in the matrix-induced kernel:', len(ker_bits), sorted(ker_bits)[:4], '...')
# image of G_mat in Aut(K3,3): count automorphisms nu realized with some eps
realized = sum(1 for nu in autos if any(G_mat.contains(a33_perm(nu, eps)) for eps in [(True,) * 9] + [tuple(e) for e in itertools.product([True, False], repeat=9)][:64]))
print('automorphisms of K3,3 realized by matrix operations (partial search over 65 bit patterns):', realized)
print('(%.0fs)' % (time.time() - t0))

# ---- the wreath action on the strata: transitivity on tori / shared circles / vertex pairs (exact from Aut(K3,3))
edge_orbit = set()
for nu in autos:
    edge_orbit.add(circle_of(nu[V1[0]], nu[V2[0]]))
print('Aut(K3,3) transitive on the nine circles:', len(edge_orbit) == 9, '; stabilizer of a circle', len(autos) // 9)
print('=> A33 ≀ S2 transitive on the 81 tori, stabilizer order 2*36864^2/81 = %d; on the 36 vertex pairs (36 = 6^2), 108 shared circles (9*6*2)' % (2 * 36864 ** 2 // 81))

# ---- stabilizers on N16 under G_ext = <product relabellings (pi1 x pi2, tau1 x tau2), swap, conj, transpose>
def canon(H):
    D = dephase(H); return np.round(D * 4, 6).tobytes()
S4 = list(itertools.permutations(range(4)))
def prod_perm(p, q): return [4 * p[a] + q[b] for a in range(4) for b in range(4)]
SW = [4 * b + a for a in range(4) for b in range(4)]
def stabilizer_order(H, verbose=False):
    """|{g in G_ext : g.H ~ H}| by exhaustive search over 576*576*8 elements (batched over tau)."""
    c0 = canon(H)
    count = 0
    col_perms = np.array([prod_perm(t1, t2) for t1 in S4 for t2 in S4])  # 576 x 16
    for sw in (False, True):
        for cj in (False, True):
            for tr in (False, True):
                H1 = H.copy()
                if sw: H1 = H1[np.ix_(SW, SW)]
                if cj: H1 = np.conj(H1)
                if tr: H1 = H1.T
                for p1 in S4:
                    for p2 in S4:
                        rp = prod_perm(p1, p2)
                        H2 = H1[rp, :]
                        B = H2[:, col_perms]            # 16 x 576 x 16
                        B = np.transpose(B, (1, 0, 2))  # 576 x 16 x 16
                        B = B / (B[:, :, :1] / np.abs(B[:, :, :1]))
                        B = B / (B[:, :1, :] / np.abs(B[:, :1, :]))
                        Bc = np.round(B * 4, 6)
                        for m in range(576):
                            if Bc[m].tobytes() == c0: count += 1
    return count

pts = []
z, w = np.exp(1j * rng.uniform(0, 2 * np.pi, 2))
pts.append(('Σ generic (circle 0 × circle 0)', kron(U_circle(0, z), U_circle(0, w))))
pts.append(('Σ generic (circle 2 × circle 5)', kron(U_circle(2, z), U_circle(5, w))))
pts.append(('F4⊗F4', kron(U_circle(0, 1j), U_circle(0, 1j))))
pts.append(('H4⊗H4 (vertex × vertex)', kron(U_circle(0, 1), U_circle(0, 1))))
Fi = F4(1j); Dw = np.ones((4, 4), dtype=complex); Dw[1, :] = [1, 1j, 1, -1j]
pts.append(('Diţă witness', dita(Fi, [Fi] * 4, Dw)))
D = np.exp(1j * rng.uniform(0, 2 * np.pi, (4, 4)))
pts.append(('Diţă generic', dita(U_circle(0, z), [U_circle(0, w)] * 4, D)))
for name, H in pts:
    t1 = time.time()
    st = stabilizer_order(H)
    print('  stabilizer in G_ext (order %d) of %-32s: %6d   orbit size %d   (%.0fs)' % (576 * 576 * 8, name, st, 576 * 576 * 8 // st, time.time() - t1))
print('(%.0fs)' % (time.time() - t0))
