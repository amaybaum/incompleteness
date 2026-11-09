"""p6_r3rev_qx3 -- independent r3 reviewer probe for QX-3 A3.1 (no p1-p5 imports). Exact, exhaustive.
(a) alpha over every coset of F_2^4 and every pair of affine functionals: case count and value set; the
    alpha=0 <=> f_B = f_A + 1 (f_A non-constant) equivalence, each direction counted separately.
(b) L(s,c1,c2) = (s, s+c1, s+c2): routing on the ready support, alpha = 0, weight conservation there; L = Fredkin on
    c1+c2 = 1; count of affine bijections of F_2^3 that route on the ready support with weight conserved there.
(c) affine bijections of F_2^3 preserving total Hamming weight everywhere; all globally weight-preserving routing
    bijections and whether any is affine; robustness: same questions with FIELD-ONLY weight (c1+c2), the
    control/supply cell s not counted.
"""
import itertools
from fractions import Fraction as Fr

def vecs(n): return list(itertools.product((0, 1), repeat=n))
def add(u, v): return tuple((a + b) % 2 for a, b in zip(u, v))
def dot(u, v): return sum(a * b for a, b in zip(u, v)) % 2

# (a)
n = 4
subspaces = set()
for k in range(n + 1):
    for gens in itertools.combinations(vecs(n), k):
        span = {tuple([0] * n)}
        for g in gens:
            span |= {add(s, g) for s in span}
        subspaces.add(frozenset(span))
cosets = set()
for W in subspaces:
    for t in vecs(n):
        cosets.add(frozenset(add(w, t) for w in W))
funcs = [(a, c) for a in vecs(n) for c in (0, 1)]
values = set(); cases = 0; fwd_ok = True; bwd_ok = True
for C in cosets:
    for (a, ca), (b, cb) in itertools.product(funcs, repeat=2):
        cases += 1
        fA = {s: (dot(a, s) + ca) % 2 for s in C}; fB = {s: (dot(b, s) + cb) % 2 for s in C}
        N = len(C)
        PA = Fr(sum(fA.values()), N); PB = Fr(sum(fB.values()), N)
        PAB = Fr(sum(fA[s] * fB[s] for s in C), N)
        alpha = None if PA * PB == 0 else PAB / (PA * PB)
        values.add(alpha)
        nonconst = len(set(fA.values())) == 2
        comp = all(fB[s] == (fA[s] + 1) % 2 for s in C)
        if comp and nonconst and alpha != 0: fwd_ok = False
        if alpha == 0 and not (comp and nonconst): bwd_ok = False
print('(a) cosets of F_2^4:', len(cosets), '; cases:', cases, '; alpha values:', values)
print('    (<=) f_B=f_A+1, f_A non-constant => alpha=0:', fwd_ok, '; (=>) alpha=0 => f_B=f_A+1, f_A non-constant:', bwd_ok)

# (b),(c) on F_2^3, coordinates (s, c1, c2)
V3 = vecs(3)
L = lambda v: (v[0], (v[0] + v[1]) % 2, (v[0] + v[2]) % 2)
fred = lambda v: (v[0], v[2], v[1]) if v[0] else v
ready = [(0, 1, 0), (1, 1, 0)]
print('(b) L on ready support:', [L(v) for v in ready], '; L = Fredkin on c1+c2=1:',
      all(L(v) == fred(v) for v in V3 if (v[1] + v[2]) % 2 == 1), '; L bijective:', len({L(v) for v in V3}) == 8)
w = lambda v: sum(v); wf = lambda v: v[1] + v[2]
def routes(T):
    outs = [(T(v)[1], T(v)[2]) for v in ready]
    return set(outs) == {(1, 0), (0, 1)}
# affine bijections of F_2^3
mats = []
for bits in itertools.product((0, 1), repeat=9):
    M = [bits[0:3], bits[3:6], bits[6:9]]
    f = lambda v, M=M: tuple(dot(M[r], v) for r in range(3))
    if len({f(v) for v in V3}) == 8: mats.append(M)
aff = []
for M in mats:
    for t in V3:
        aff.append(lambda v, M=M, t=t: add(tuple(dot(M[r], v) for r in range(3)), t))
print('    |GL(3,2)| =', len(mats), '; affine bijections:', len(aff))
r_tot = sum(1 for T in aff if routes(T) and all(w(T(v)) == w(v) for v in ready))
r_fld = sum(1 for T in aff if routes(T) and all(wf(T(v)) == wf(v) for v in ready))
r_any = sum(1 for T in aff if routes(T))
print('    affine bijections routing on the ready support: total-weight conserved there:', r_tot,
      '; field-weight conserved there:', r_fld, '; routing, no weight condition:', r_any)
glob_tot = [T for T in aff if all(w(T(v)) == w(v) for v in V3)]
print('(c) affine bijections preserving total weight everywhere:', len(glob_tot),
      '; all coordinate permutations:', all(sorted(T(v) for v in [(1,0,0),(0,1,0),(0,0,1)]) == [(0,0,1),(0,1,0),(1,0,0)] and T((0,0,0)) == (0,0,0) for T in glob_tot))
# all bijections of F_2^3 preserving total weight, routing
perms = itertools.permutations(V3)
def is_affine(table):
    t = table[(0, 0, 0)]
    lin = {v: add(table[v], t) for v in V3}
    return all(lin[add(u, v)] == add(lin[u], lin[v]) for u in V3 for v in V3)
gw_route = []; gw_route_field = []
for img in perms:
    table = dict(zip(V3, img))
    T = table.__getitem__
    if routes(T):
        if all(w(table[v]) == w(v) for v in V3): gw_route.append(is_affine(table))
        if all(wf(table[v]) == wf(v) for v in V3): gw_route_field.append(is_affine(table))
print('    total-weight-preserving routing bijections:', len(gw_route), '; affine among them:', sum(gw_route))
print('    field-weight-preserving (s not counted) routing bijections:', len(gw_route_field), '; affine among them:', sum(gw_route_field))
print('QX3 PROBE DONE')
