#!/usr/bin/env python3
"""Thread D, route 1 (homogeneity + self-duality).  EXACT arithmetic only (Fractions; sympy only for
one symbolic determinant).

(A) Homogeneity test by an exact upper bound on dim Lie(Aut K).
    If K is a closed pointed cone whose set of extreme rays Ext is a smooth embedded manifold,
    every one-parameter subgroup exp(tA) of Aut(K) maps Ext into Ext, so A x lies in T_x Ext for
    every x in Ext.  Imposing  N_x^T A x = 0  (N_x a basis of the orthogonal complement of T_x)
    at finitely many EXACT rational points of Ext gives linear equations on the n^2 entries of A
    which every element of Lie(Aut K) satisfies; the nullity of the stacked system is therefore an
    exact UPPER BOUND on dim Lie(Aut K).  A homogeneous cone of dimension n needs dim Aut K >= n
    (Aut K acts transitively on the open n-dimensional interior).
    Control: the Lorentz cone L^4 (3-ball), true dim Lie(Aut) = 1 + dim so(3,1) = 7: the bound
    must come out >= 7 (it is tight if it equals 7).
(B) Square cone: not self-dual for ANY inner product (exact enumeration of ray bijections).
(C) Ishi-form rank-2 control (block [[x1 I2, A^T],[A, x2 I2]] is the Lorentz cone L^4), and the
    Vinberg cone (rank 3): capacity >= 3.
"""
from fractions import Fraction as Fr
from itertools import permutations
from exact_la import rank, nullspace, matmul, T

def pyth(k):
    k = Fr(k); return ((1 - k*k)/(1 + k*k), 2*k/(1 + k*k))

def lie_bound(points_with_tangents, n):
    rows = []
    for x, tans in points_with_tangents:
        Tm = [list(map(Fr, x))] + [list(map(Fr, t)) for t in tans]     # rows span T_x Ext
        for nv in nullspace(Tm, n):                                     # orthogonal complement
            rows.append([nv[i]*Fr(x[j]) for i in range(n) for j in range(n)])
    return n*n - rank(rows)

results = {}
# torus orbitope D x D = conv(S^1 x S^1): cone in R^5, Ext = R_{>0} x T^2
ks = [0, Fr(1,2), Fr(1,3), 2, Fr(2,5), 3, Fr(3,7), Fr(-1,2), Fr(5,3)]
pts = []
for a in ks:
    for b in ks:
        c1, s1 = pyth(a); c2, s2 = pyth(b)
        pts.append(([1, c1, s1, c2, s2], [[0, -s1, c1, 0, 0], [0, 0, 0, -s2, c2]]))
results['torus orbitope cone (R^5)'] = (lie_bound(pts, 5), 5)
TORUS_PTS = pts

# Stiefel orbitope conv V_2(R^3): cone in R^7, Ext = R_{>0} x V_2(R^3)
def inv3(M):
    a,b,c = M[0]; d,e,f = M[1]; g,h,i = M[2]
    det = a*(e*i-f*h) - b*(d*i-f*g) + c*(d*h-e*g)
    adj = [[e*i-f*h, c*h-b*i, b*f-c*e],[f*g-d*i, a*i-c*g, c*d-a*f],[d*h-e*g, b*g-a*h, a*e-b*d]]
    return [[x/det for x in r] for r in adj]
def cayley(a, b, c):
    a, b, c = Fr(a), Fr(b), Fr(c)
    S = [[0, -c, b], [c, 0, -a], [-b, a, 0]]
    I = [[Fr(int(i == j)) for j in range(3)] for i in range(3)]
    return matmul([[I[i][j] - S[i][j] for j in range(3)] for i in range(3)],
                  inv3([[I[i][j] + S[i][j] for j in range(3)] for i in range(3)]))
so3 = [[[0,0,0],[0,0,-1],[0,1,0]], [[0,0,1],[0,0,0],[-1,0,0]], [[0,-1,0],[1,0,0],[0,0,0]]]
pts = []
import itertools
STIEFEL_PARAMS = list(itertools.product([0, Fr(1,2), -2, Fr(3,5)], [0, Fr(1,3), 1, Fr(-3,2)], [0, 2, Fr(-1,4)]))
for (a, b, c) in STIEFEL_PARAMS:
    Q = cayley(a, b, c)
    assert matmul(T(Q), Q) == [[Fr(int(i == j)) for j in range(3)] for i in range(3)]
    V = [row[:2] for row in Q]
    vec = lambda X: [X[i][j] for i in range(3) for j in range(2)]
    pts.append(([1] + vec(V), [[0] + vec(matmul(W, V)) for W in so3]))
results['Stiefel orbitope cone (R^7)'] = (lie_bound(pts, 7), 7)

# Caratheodory orbitope C_2: cone in R^5, Ext = R_{>0} x S^1
pts = []
for a in [0, Fr(1,2), Fr(1,3), 2, Fr(2,5), 3, Fr(3,7), Fr(5,2), Fr(-1,4), Fr(-3,2), Fr(7,3)]:
    c, s = pyth(a); c2, s2 = c*c - s*s, 2*c*s
    pts.append(([1, c, s, c2, s2], [[0, -s, c, -2*s2, 2*c2]]))
results['Caratheodory orbitope cone (R^5)'] = (lie_bound(pts, 5), 5)

# control: Lorentz cone L^4 (3-ball), Ext = R_{>0} x S^2
def cross(u, v): return [u[1]*v[2]-u[2]*v[1], u[2]*v[0]-u[0]*v[2], u[0]*v[1]-u[1]*v[0]]
pts = []
for (a, b) in [(p, q) for p in [0, Fr(1,2), 2, Fr(-3,4), 3] for q in [0, Fr(1,3), -1, Fr(2,5)]]:
    a, b = Fr(a), Fr(b); d = 1 + a*a + b*b
    nv = [2*a/d, 2*b/d, (a*a + b*b - 1)/d]
    tans = [[0] + cross(nv, e) for e in ([1,0,0],[0,1,0],[0,0,1])]
    pts.append(([1] + nv, tans))
results['Lorentz cone L^4 = 3-ball (control)'] = (lie_bound(pts, 4), 4)

# square cone: Ext = 4 rays, tangency A x in span(x)
SQ = [[1,1,1],[1,-1,1],[1,-1,-1],[1,1,-1]]
results['square gbit cone (R^3)'] = (lie_bound([(x, []) for x in SQ], 3), 3)

print("(A) exact upper bound on dim Lie(Aut K); homogeneity needs bound >= dim K")
for k, (bd, n) in results.items():
    print(f"   {k:38s} dim Lie(Aut K) <= {bd:2d}   dim K = {n}   ->",
          "NOT homogeneous" if bd < n else "not excluded")

# (B) square cone, self-duality for an arbitrary inner product x^T G y (G sym. pos. def.):
#     K^G = G^{-1} K*_std, so K^G = K iff G K = K*_std iff G maps each ray v_i to a positive
#     multiple of a ray (facet normal) n_pi(i) of K*_std, for some bijection pi.
#     v4 = v1 - v2 + v3, so G v4 = l1 n1' - l2 n2' + l3 n3' must equal l4 n4'  (3 linear eqs in l),
#     plus symmetry of G = [l1 n1', l2 n2', l3 n3'] B^{-1} (3 linear eqs in l).
V = [list(map(Fr, v)) for v in SQ]
def dot(u, v): return sum(a*b for a, b in zip(u, v))
normals = []
for i in range(4):
    nrm = cross(V[i], V[(i+1) % 4])
    if any(dot(nrm, V[j]) < 0 for j in range(4)): nrm = [-x for x in nrm]
    normals.append(nrm)
assert all(dot(normals[k], V[j]) >= 0 for k in range(4) for j in range(4))
Binv = inv3(T([V[0], V[1], V[2]]))
hits = 0
for pi in permutations(range(4)):
    N = [normals[pi[i]] for i in range(4)]
    # G(l) = sum_k l_k * (N_k e_k^T) Binv  -> linear in l; build coefficient matrices
    Gk = []
    for k in range(3):
        Ek = [[N[k][r] if c == k else Fr(0) for c in range(3)] for r in range(3)]
        Gk.append(matmul(Ek, Binv))
    eqs = []
    for r in range(3):     # G v4 - l4 N4 = 0  (unknowns l1..l4)
        eqs.append([sum(Gk[k][r][c]*V[3][c] for c in range(3)) for k in range(3)] + [-N[3][r]])
    for (r, c) in [(0,1),(0,2),(1,2)]:
        eqs.append([Gk[k][r][c] - Gk[k][c][r] for k in range(3)] + [Fr(0)])
    for l in nullspace(eqs, 4):
        for sgn in (1, -1):
            lv = [sgn*x for x in l]
            if all(x > 0 for x in lv):
                G = [[sum(lv[k]*Gk[k][r][c] for k in range(3)) for c in range(3)] for r in range(3)]
                m1 = G[0][0]; m2 = G[0][0]*G[1][1]-G[0][1]*G[1][0]
                m3 = (G[0][0]*(G[1][1]*G[2][2]-G[1][2]*G[2][1]) - G[0][1]*(G[1][0]*G[2][2]-G[1][2]*G[2][0])
                      + G[0][2]*(G[1][0]*G[2][1]-G[1][1]*G[2][0]))
                if m1 > 0 and m2 > 0 and m3 > 0: hits += 1
    # (the solution space is at most 1-dimensional for every pi; checked below)
    assert len(nullspace(eqs, 4)) <= 1
print(f"(B) square cone: ray bijections admitting a symmetric positive-definite G with G K = K* : {hits} of 24"
      "  -> self-dual for some inner product:", hits > 0)

# (C) Ishi-form rank-2 control and the Vinberg cone
from sympy import symbols, Matrix, eye, factor
x1, x2, a, b = symbols('x1 x2 a b', real=True)
A = Matrix([[a, -b], [b, a]])
X = Matrix.vstack(Matrix.hstack(x1*eye(2), A.T), Matrix.hstack(A, x2*eye(2)))
print("(C) A^T A =", (A.T*A).applyfunc(factor).tolist(), "; det =", factor(X.det()),
      "-> PSD iff x1,x2 >= 0 and x1 x2 >= a^2+b^2: Lorentz cone L^4, base = 3-ball")
E = [[[Fr(int(i == j == k)) for j in range(3)] for i in range(3)] for k in range(3)]
pair = [[sum(matmul(E[i], E[j])[r][r] for r in range(3)) for j in range(3)] for i in range(3)]
print("    Vinberg cone {[[x1,x4,x5],[x4,x2,0],[x5,0,x3]] >= 0}: tr(E_i E_j) =",
      [[int(v) for v in r] for r in pair], "with sum E_i = I -> capacity >= 3 (not a bit)")
