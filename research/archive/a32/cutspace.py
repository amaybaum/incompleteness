"""Exploration only: the family's pure sign-flip subgroup H ∩ K as edge sets of the marked-point
graph (6 marked classes, 9 circles as edges), compared with the graph's cut space."""
import cmath, itertools
import numpy as np
from circles import R, circle_vectors
import members as Mm   # builds the 42-point sample and all 2304 member maps
g = Mm.g
# graph: vertices = marked classes, edge r joins the classes at z=+1 and z=-1 of circle r
V = [circle_vectors(*r) for r in R]
cen = [np.array(c) for c, _, _ in V]; cos_ = [np.array(A)+np.array(B) for _, A, B in V]
vid = {}
edges = []
for k in range(9):
    ends = []
    for s in (1, -1):
        key = tuple(cen[k] + s*cos_[k]); vid.setdefault(key, len(vid)); ends.append(vid[key])
    edges.append(tuple(ends))
print("edges:", edges)
deg = [sum(v in e for e in edges) for v in range(6)]
# bipartite check
col = {0: 0}; stack = [0]
while stack:
    u = stack.pop()
    for a, b in edges:
        for x, y in ((a, b), (b, a)):
            if x == u and y not in col: col[y] = 1 - col[u]; stack.append(y)
print("degrees", deg, "bipartite:", all(col[a] != col[b] for a, b in edges), "=> K33" )
# flip-type members: fix each circle's generic sample points up to conj
t0 = Mm.t0
def pidx(r, z): return Mm.index[g.key(g.feature(r, z))]
flipsets = set()
for key, m in Mm.members.items():
    S = []
    ok = True
    for r in range(9):
        a, b = pidx(r, cmath.exp(1j*t0)), pidx(r, cmath.exp(-1j*t0))
        if m[a] == a: continue
        if m[a] == b: S.append(r); continue
        ok = False; break
    if ok and all(m[pidx(r, s)] == pidx(r, s) for r in range(9) for s in (1, -1)):
        flipsets.add(tuple(S))
print("flip subgroup size", len(flipsets))
cuts = set()
for sub in itertools.product((0, 1), repeat=6):
    cuts.add(tuple(r for r, (a, b) in enumerate(edges) if sub[a] != sub[b]))
print("cut space size", len(cuts), "equal:", flipsets == cuts)
print(sorted(flipsets, key=len))
full = tuple(range(9))
comp = set(tuple(r for r in range(9) if r not in c) for c in cuts)
print("flip == complements of cuts:", flipsets == comp)
# test: is flipsets a linear subspace containing full set?
fs = [frozenset(s) for s in flipsets]
print("closed under symmetric difference:", all(tuple(sorted(a ^ b)) in flipsets for a in fs for b in fs), "contains all:", full in flipsets)
# cycle space: orthogonal complement of cuts
def dotp(a, b): return len(set(a) & set(b)) % 2
cyc = [s for s in (tuple(r for r in range(9) if (m >> r) & 1) for m in range(512)) if all(dotp(s, c) == 0 for c in cuts)]
print("cycle space size", len(cyc))
print("flip ∩ cuts:", len(flipsets & cuts), " flip ⊥ cycles:", all(dotp(s, c) == 0 for s in flipsets for c in cyc))
