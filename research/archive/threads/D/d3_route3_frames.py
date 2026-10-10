#!/usr/bin/env python3
"""Thread D, route 3 (tests on maximal frames + transitivity on frames).  EXACT arithmetic only:
Fractions for the square / torus / Stiefel / ball; an exact Q(sqrt5) class for the pentagon.

Bodies, all with FULL effects (every affine e with 0 <= e <= 1 on the body):
  square gbit [-1,1]^2;  torus orbitope conv(S^1 x S^1) = D x D (D the unit disk);
  Stiefel orbitope conv V_2(R^3) = {X in R^{3x2} : ||X||_op <= 1};  3-ball;  regular pentagon.
Checks:
  (1) frames (ordered perfectly distinguishable pairs of pure states) of two kinds per body,
      witnessed by an exact effect; the midpoint of a frame is interior or boundary — an affine
      invariant, so frames of both kinds => Aut(body) is NOT transitive on frames (strong symmetry fails);
  (2) Lemma I (ideal-test obstruction): if a frame's distinguishing effect e is unique and
      lin cone(F) ∩ lin cone(Z) != 0  (F = {e = 1}, Z = {e = 0}), no positive linear T with
      u∘T = e and T|F = id exists.  Computed: dim of the intersection of the two spans;
  (3) pentagon countercontrol: pure states, distinguishable pairs, automorphisms (all 60 vertex
      triples), strong symmetry on pairs, failure of spectrality at the centre, ideal frame tests,
      SF failure, self-duality (Gram criterion), and the ideal-compression test for an edge effect.
"""
from fractions import Fraction as Fr
from itertools import permutations
from exact_la import rank, nullspace

def span_intersection_dim(U, W):
    return rank(U) + rank(W) - rank(U + W)

out = []
def say(s): print(s); out.append(s)

# ---------------- square gbit, cone coords (t, x, y), body |x|,|y| <= t
say("== square gbit")
e_adj = lambda p: Fr(1, 2) + p[0] / 2                       # distinguishes (1,1) from (-1,1)
verts = [(1, 1), (-1, 1), (-1, -1), (1, -1)]
assert all(0 <= e_adj(v) <= 1 for v in verts) and e_adj((1, 1)) == 1 and e_adj((-1, 1)) == 0
e_diag = lambda p: Fr(1, 2) + (p[0] + p[1]) / 4             # distinguishes (1,1) from (-1,-1)
assert all(0 <= e_diag(v) <= 1 for v in verts) and e_diag((1, 1)) == 1 and e_diag((-1, -1)) == 0
say("  frames: adjacent ((1,1),(-1,1)) midpoint (0,1) on the boundary; diagonal ((1,1),(-1,-1)) midpoint (0,0) interior"
    " -> Aut not transitive on frames")
# uniqueness of the adjacent-frame effect: e = a + b x + c y, a+b+c = 1, a-b+c = 0, 0<=e<=1 at all vertices
# => b = 1/2, a + c = 1/2; e(1,-1) = 1 - 2c <= 1 => c >= 0; e(-1,-1) = -2c >= 0 => c <= 0  => c = 0.
F = [[1, 1, 1], [1, 1, -1]]; Z = [[1, -1, 1], [1, -1, -1]]
say(f"  adjacent frame: unique effect (1+x)/2; dim(lin cone F ∩ lin cone Z) = {span_intersection_dim(F, Z)}"
    " -> no ideal test (Lemma I)")
say("  spectrality: (1/2,1/4) lies on no segment between two distinguishable vertices (edges x=±1, y=±1; diagonals y=±x) -> fails")

# ---------------- torus D x D, cone coords (t, x1, x2, y1, y2)
say("== torus orbitope D x D")
# effect e = a + <b,x> + <c,y> is valid iff a - |b| - |c| >= 0 and a + |b| + |c| <= 1.
p1 = (1, 0, 1, 0); p2 = (-1, 0, 1, 0)      # x antipodal, y equal
q2 = (-1, 0, -1, 0)                        # fully antipodal partner of p1
e1 = lambda p: Fr(1, 2) + Fr(1, 2) * p[0]                      # b = (1/2,0), c = 0
e2 = lambda p: Fr(1, 2) + Fr(1, 4) * p[0] + Fr(1, 4) * p[2]    # b = (1/4,0), c = (1/4,0)
assert (e1(p1), e1(p2), e2(p1), e2(q2)) == (1, 0, 1, 0)
say("  frames: (p1,p2) = ((1,0;1,0),(-1,0;1,0)) midpoint (0,0;1,0) on the boundary (|y|=1);"
    " (p1,-p1) midpoint 0 interior -> Aut not transitive on frames")
# uniqueness for (p1,p2): if c != 0, e(p1) = 1 forces y1 = c/|c| and e(p2) = 0 forces y2 = -c/|c|; y1 = y2 contradicts.
F = [[1, 1, 0, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]      # lin cone({x=(1,0)} x D)
Z = [[1, -1, 0, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]     # lin cone({x=(-1,0)} x D)
say(f"  frame (p1,p2): unique effect (1+x_1)/2; dim(lin cone F ∩ lin cone Z) = {span_intersection_dim(F, Z)}"
    " -> no ideal test (Lemma I)")

# ---------------- Stiefel: X in R^{3x2}, vec row-major, cone coords (t, vec X)
say("== Stiefel orbitope conv V_2(R^3)")
V1 = [[1, 0], [0, 1], [0, 0]]; V2 = [[1, 0], [0, -1], [0, 0]]
eS = lambda X: Fr(1, 2) + Fr(1, 2) * X[1][1]                 # Y = (1/2) e2 e2^T, nuclear norm 1/2
assert eS(V1) == 1 and eS(V2) == 0
mid = [[Fr(a + b, 2) for a, b in zip(r1, r2)] for r1, r2 in zip(V1, V2)]
MtM = [[sum(mid[k][i] * mid[k][j] for k in range(3)) for j in range(2)] for i in range(2)]
say(f"  frames: ([e1,e2],[e1,-e2]) midpoint M = [e1,0], M^T M = {[[str(v) for v in r] for r in MtM]} -> ||M||_op = 1 boundary;"
    " (V,-V) midpoint 0 interior -> Aut not transitive on frames")
# uniqueness: <Y, V1 - V2> = 2 Y_22 = 1 with ||Y||_nuc = 1/2 forces Y = (1/2) e2 e2^T (|Y_22| <= sigma_1 <= ||Y||_nuc,
# equality in both forces rank one with that singular pair).
def vecc(t, X): return [t] + [X[i][j] for i in range(3) for j in range(2)]
E = lambda i, j: [[1 if (r, c) == (i, j) else 0 for c in range(2)] for r in range(3)]
add = lambda A, B: [[a + b for a, b in zip(r, s)] for r, s in zip(A, B)]
neg = lambda A: [[-a for a in r] for r in A]
F = [vecc(1, E(1, 1)), vecc(0, E(0, 0)), vecc(0, E(2, 0))]   # face {X e2 = e2} = e2e2^T + disk in span{E00, E20}
Z = [vecc(1, neg(E(1, 1))), vecc(0, E(0, 0)), vecc(0, E(2, 0))]
say(f"  frame (V1,V2): unique effect (1+X_22)/2; dim(lin cone F ∩ lin cone Z) = {span_intersection_dim(F, Z)}"
    " -> no ideal test (Lemma I)")

# ---------------- 3-ball control
say("== 3-ball (control)")
# frames: e(p1)=1, e(p2)=0 with e = 1/2 + <b,x>, |b| = 1/2 forces p1 = b/|b|, p2 = -b/|b|: only antipodal frames,
# SO(3) is transitive on ordered antipodal pairs.  Ideal test T(t,x) = e(t,x) (1,n): positive (e >= 0 on the cone),
# fixes F = {n}, kills Z = {-n}.
F = [[1, 0, 0, 1]]; Z = [[1, 0, 0, -1]]
say(f"  frame (n,-n): dim(lin cone F ∩ lin cone Z) = {span_intersection_dim(F, Z)}; T = e(.)(1,n) is an ideal test;"
    " SO(3) transitive on ordered antipodal pairs")

# ---------------- pentagon countercontrol in Q(sqrt5)
class Q5:
    """a + b*sqrt5, a,b rational; exact sign."""
    __slots__ = ('a', 'b')
    def __init__(s, a, b=0): s.a, s.b = Fr(a), Fr(b)
    def __add__(s, o): o = o if isinstance(o, Q5) else Q5(o); return Q5(s.a + o.a, s.b + o.b)
    __radd__ = __add__
    def __neg__(s): return Q5(-s.a, -s.b)
    def __sub__(s, o): return s + (-(o if isinstance(o, Q5) else Q5(o)))
    def __rsub__(s, o): return Q5(o) - s
    def __mul__(s, o): o = o if isinstance(o, Q5) else Q5(o); return Q5(s.a*o.a + 5*s.b*o.b, s.a*o.b + s.b*o.a)
    __rmul__ = __mul__
    def inv(s):
        d = s.a*s.a - 5*s.b*s.b; return Q5(s.a / d, -s.b / d)
    def __truediv__(s, o): o = o if isinstance(o, Q5) else Q5(o); return s * o.inv()
    def sign(s):
        a, b = s.a, s.b
        if b == 0: return (a > 0) - (a < 0)
        if a == 0: return (b > 0) - (b < 0)
        if (a > 0) == (b > 0): return 1 if a > 0 else -1
        return ((a*a > 5*b*b) - (a*a < 5*b*b)) * (1 if a > 0 else -1)
    def __eq__(s, o): o = o if isinstance(o, Q5) else Q5(o); return s.a == o.a and s.b == o.b
    def __hash__(s): return hash((s.a, s.b))
    def __repr__(s): return f"({s.a}{'+' if s.b >= 0 else '-'}{abs(s.b)}√5)"

say("== pentagon gbit (countercontrol, exact Q(√5))")
c1 = Q5(Fr(-1, 4), Fr(1, 4)); c2 = Q5(Fr(-1, 4), Fr(-1, 4))      # cos 72°, cos 144°
s2r = Q5(Fr(-1, 2), Fr(1, 2))                                   # sin144°/sin72° = 2cos72°
P = [(Q5(1), Q5(0)), (c1, Q5(1)), (c2, s2r), (c2, -s2r), (c1, Q5(-1))]   # affine-regular pentagon
def det3(r0, r1, r2):
    return (r0[0]*(r1[1]*r2[2]-r1[2]*r2[1]) - r0[1]*(r1[0]*r2[2]-r1[2]*r2[0]) + r0[2]*(r1[0]*r2[1]-r1[1]*r2[0]))
def solve3(A, bvec):
    d = det3(*A)
    cols = []
    for k in range(3):
        Ak = [[bvec[i] if j == k else A[i][j] for j in range(3)] for i in range(3)]
        cols.append(det3(*Ak) / d)
    return cols
# convex position: every vertex is extreme (strict turn orientation)
turn = [det3([1, *P[i]], [1, *P[(i+1) % 5]], [1, *P[(i+2) % 5]]).sign() for i in range(5)]
assert len(set(turn)) == 1 and turn[0] != 0
# distinguishable pairs: affine e with e(v_i)=1, e(v_j)=0, 0 <= e(v_k) <= 1 for all k.
def dist_interval(i, j):
    # e = c0 + c1 x + c2 y; param: e = e_part + s * e_null where e_null vanishes at v_i and v_j
    k = next(m for m in range(5) if m not in (i, j))
    A = [[1, *P[i]], [1, *P[j]], [1, *P[k]]]
    base = solve3(A, [Q5(1), Q5(0), Q5(0)]); null = solve3(A, [Q5(0), Q5(0), Q5(1)])
    ev = lambda c, v: c[0] + c[1]*v[0] + c[2]*v[1]
    lo, hi = None, None     # constraints 0 <= ev(base,v) + s ev(null,v) <= 1
    for v in P:
        b0, n0 = ev(base, v), ev(null, v)
        if n0.sign() == 0:
            if (b0.sign() < 0) or ((b0 - 1).sign() > 0): return None
            continue
        bounds = [(-b0) / n0, (1 - b0) / n0]
        l, h = (bounds if n0.sign() > 0 else bounds[::-1])
        lo = l if lo is None or (l - lo).sign() > 0 else lo
        hi = h if hi is None or (h - hi).sign() < 0 else hi
    if (hi - lo).sign() < 0: return None
    return (lo, hi, base, null)
frames = [(i, j) for i in range(5) for j in range(5) if i != j and dist_interval(i, j)]
say(f"  ordered distinguishable vertex pairs: {frames}")
assert all((j - i) % 5 in (2, 3) for i, j in frames) and len(frames) == 10
def strict_mid(i, j):
    lo, hi, base, null = dist_interval(i, j); s = (lo + hi) / 2
    ev = lambda v: base[0] + s*null[0] + (base[1] + s*null[1])*v[0] + (base[2] + s*null[2])*v[1]
    return all(ev(P[k]).sign() > 0 and (ev(P[k]) - 1).sign() < 0 for k in range(5) if k not in (i, j))
interior = all((dist_interval(i, j)[1] - dist_interval(i, j)[0]).sign() > 0 and strict_mid(i, j) for i, j in frames)
say(f"  every frame's feasible effect interval has nonempty interior: {interior}"
    " -> a distinguishing effect with singleton certain and zero faces exists; measure-and-prepare"
    " T(w) = e(w) v_i is then an ideal test (fixes F = {v_i})")
# automorphisms: affine maps sending (v0,v1,v2) to an ordered triple of vertices and permuting the vertex set
def aff_from(src, dst):
    A = [[1, *p] for p in src]
    cx = solve3(A, [d[0] for d in dst]); cy = solve3(A, [d[1] for d in dst])
    return lambda p: (cx[0] + cx[1]*p[0] + cx[2]*p[1], cy[0] + cy[1]*p[0] + cy[2]*p[1])
auts = []
for tri in permutations(range(5), 3):
    f = aff_from(P[:3], [P[t] for t in tri])
    img = [f(p) for p in P]
    if all(any(q == p for p in P) for q in img):
        auts.append(tuple(next(m for m in range(5) if P[m] == q) for q in img))
say(f"  affine automorphisms: {len(auts)} (dihedral D5)")
orbit = {(a[0], a[2]) for a in auts}            # images of the frame (0,2)
say(f"  orbit of the ordered frame (0,2) under Aut: {len(orbit)} of {len(frames)} ordered frames"
    f" -> strong symmetry on pairs holds: {orbit == set(frames)};"
    f" pure transitivity: {len({a[0] for a in auts}) == 5}")
# capacity: written proof (three perfectly distinguishable states need three pairwise-adjacent edges => triangle).
# spectrality: centre (average of vertices) on no frame segment
cen = (sum((p[0] for p in P), Q5(0)) / 5, sum((p[1] for p in P), Q5(0)) / 5)
oncol = [det3([1, *P[i]], [1, *P[j]], [1, *cen]).sign() == 0 for i, j in frames]
say(f"  spectrality at the maximally mixed state (centroid): lies on a frame segment for {sum(oncol)} of 10 frames -> fails")
# SF: the edge effect
i, j, k = 0, 1, 3
A = [[1, *P[i]], [1, *P[j]], [1, *P[k]]]
ce = solve3(A, [Q5(1), Q5(1), Q5(0)])
vals = [ce[0] + ce[1]*v[0] + ce[2]*v[1] for v in P]
assert all(v.sign() >= 0 and (v - 1).sign() <= 0 for v in vals)
say(f"  edge effect e = 1 on [v0,v1], 0 at v3: values {vals} -> valid; certain face is an edge: SF fails")
# self-duality: Gram criterion with <x,y>_G = a x0 y0 + <x',y'>, a = cos 36° = (1+√5)/4, regular coordinates:
# M_ij = a + cos(72°(i-j)).  K ⊆ K^G iff M >= 0; K^G ⊆ K iff each adjacent pair (j,j+1) has a ray i with M_ij = M_i,j+1 = 0.
a = Q5(Fr(1, 4), Fr(1, 4)); cosd = {0: Q5(1), 1: c1, 2: c2, 3: c2, 4: c1}
M = [[a + cosd[(i - j) % 5] for j in range(5)] for i in range(5)]
nonneg = all(M[i][j].sign() >= 0 for i in range(5) for j in range(5))
cover = all(any(M[i][j] == 0 and M[i][(j+1) % 5] == 0 for i in range(5)) for j in range(5))
say(f"  self-duality (G = diag((1+√5)/4,1,1), regular coords): M >= 0: {nonneg}; adjacent-pair cover: {cover}"
    f" -> strongly self-dual: {nonneg and cover}")
# ideal compression for the edge effect: T fixes lin cone F = span{(1,v0),(1,v1)}, kills (1,v3).
basis = [[Q5(1), *P[0]], [Q5(1), *P[1]], [Q5(1), *P[3]]]
def coords(w):          # w = α b0 + β b1 + γ b2
    Bt = [[basis[c][r] for c in range(3)] for r in range(3)]
    return solve3(Bt, w)
res = {}
for m in (2, 4):
    al, be, ga = coords([Q5(1), *P[m]])
    res[m] = (al, be)
pos = all(al.sign() >= 0 and be.sign() >= 0 for al, be in res.values())
say(f"  edge-effect ideal compression: T(1,v2) = {res[2][0]}(1,v0)+{res[2][1]}(1,v1), T(1,v4) = {res[4][0]}(1,v0)+{res[4][1]}(1,v1)"
    f" -> positive: {pos}")
open('d3_route3_frames.out', 'w').write("\n".join(out) + "\n")
