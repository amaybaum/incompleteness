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
gens = [a33_perm(nu, (True,) * 9) for nu in autos] + [a33_perm(tuple(range(6)), tuple(r == j for r in range(9))) for j in range(9)]
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
print('automorphisms of K3,3 realized by matrix operations (search over 65 bit patterns):', realized)
print('(%.0fs)' % (time.time() - t0))


# the matrix-induced subgroup's image in Aut(K3,3) and its kernel, exactly
img = set(); ker = set()
for nu in autos:
    for eps in itertools.product([True, False], repeat=9):
        if G_mat.contains(a33_perm(nu, eps)):
            img.add(nu)
            if nu == tuple(range(6)): ker.add(eps)
print('matrix-induced subgroup: image in Aut(K3,3) has order %d, kernel %d bit patterns, product %d = order %d' % (len(img), len(ker), len(img) * len(ker), G_mat.order()))
# the kernel patterns as subsets of circles flipped
print('kernel bit patterns (circles conjugated):', sorted(tuple(r for r in range(9) if not e[r]) for e in ker))
# which A33 elements extend to N16 at all? those induced by matrix operations; index
print('index of the matrix-induced subgroup in A33:', G33.order() // G_mat.order())
