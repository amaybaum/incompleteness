# c10_b3c_case.py -- research/countermodels optional node (round 2): Conjecture B3.C of HO-2 v1, one new case.
# DECISION RULE (fixed before the first run, 2026-10-10T23:09:07Z by date -u; predictions in NOTES-C10 S0):
#  Exact arithmetic (sympy; guard EX: no Float). Computational basis |00>,|01>,|10>,|11>; |0+-> = |0>(x)|+->, etc.
#  Basis b1 = C2(1) = (|0-> + |1+>)/sqrt2, b2 = C2(-1), b3 = |0+>, b4 = |1->; H0 = {u(al, be) = e^{i al} P1 + e^{i be} P2 +
#  e^{i(al+be)} P3 + P4}; z = (I - 2 P_{b1})/8 (pauliW image); tables via the Pauli decomposition of c2_structure.py.
#  CHECK lines (PASS/FAIL), COUNTERCONTROL lines (must pass as stated); VERDICT C10-B3C-CASE-EXACT iff all pass, else
#  NO VERDICT; verdict text generated from the measured values.
#  K0  b1..b4 orthonormal; b1, b2 maximally entangled (coefficient matrix M with M M^dag = I/2); b3, b4 products (det M = 0).
#  K1  CNOT = I - 2 b4 b4^dag; u(al, be) unitary and commuting with CNOT (symbolic); the six weight differences of H0 are
#      nonzero linear forms (simple spectrum: the commutant of H0 is the diagonal algebra in {b_k}).
#  K2  z is fixed by H0 (symbolic) and by CNOT; the table of z reproduces pauliW(z) = (I - 2P_{b1})/8; z in maxCone:
#      for every product x (x) y, |<b1|x (x) y>|^2 <= |x|^2 |y|^2 / 2 because M M^dag = I/2 ([W] operator norm 1/sqrt2).
#  K3  X's single-defect characterization applies: 8 pauliW(z) has eigenvalues (-1, 1, 1, 1) (one negative, lambda_2 =
#      -lambda_1), so K({z}) = (Q3 n z*) + R+ z is closed and self-dual ([A] AUDIT-X); K({z}) != Q3 (P_{b1} in Q3 pairs
#      -1/8 with z).
#  K4  the slice: C = cone{e2, e3, e4, e1+e2, e1+e3, e1+e4, f}, f = (-1, 1, 1, 1): facets enumerated exactly; the set of
#      facet normals (as rays) equals the set of extreme rays of C, so C* = C; C != R^4_+ (f in C).
#  CC1 the product basis {|00>, |01>, |1+>, |1->} (a case covered by HO-2): every basis vector is a product.
#  CC2 scaling c = 5/2 > 2: eigenvalues (-3/2, 1, 1, 1) violate X's condition lambda_2 >= -lambda_1, and the defect leaves
#      maxCone (1 - (5/2)(1/2) < 0 at a best product).
import itertools
import sympy as sp
from sympy import Matrix, Rational as Q, I, eye, zeros, sqrt, expand, exp, symbols, kronecker_product as kron

R_ = []
def rec(kind, cid, ok, text, detail=""):
    ok = bool(ok); R_.append(ok)
    print(f"{kind} {cid:<4} {'PASS' if ok else 'FAIL'} {text}" + (f" -- {detail}" if detail else ""))

I2 = eye(2); SX = Matrix([[0, 1], [1, 0]]); SY = Matrix([[0, -I], [I, 0]]); SZ = Matrix([[1, 0], [0, -1]])
SG = [I2, SX, SY, SZ]; KR = {(m, n): kron(SG[m], SG[n]) for m in range(4) for n in range(4)}
def pauliW(w): return sum((w[m, n] * KR[(m, n)] for m in range(4) for n in range(4) if w[m, n] != 0), zeros(4, 4)) / 4
def tab(Mx): return Matrix(4, 4, lambda m, n: sp.nsimplify(sp.simplify(expand((KR[(m, n)] * Mx).trace()))))

s2 = sqrt(2)
k0p = Matrix([1, 1, 0, 0]) / s2; k0m = Matrix([1, -1, 0, 0]) / s2; k1p = Matrix([0, 0, 1, 1]) / s2; k1m = Matrix([0, 0, 1, -1]) / s2
B = [(k0m + k1p) / s2, (k0m - k1p) / s2, k0p, k1m]
def coef(v): return Matrix([[v[0], v[1]], [v[2], v[3]]])
on = all(sp.simplify((B[i].H * B[j])[0] - (1 if i == j else 0)) == 0 for i in range(4) for j in range(4))
me = all(sp.simplify(coef(B[k]) * coef(B[k]).H - eye(2) / 2) == zeros(2, 2) for k in (0, 1))
pr = all(sp.simplify(coef(B[k]).det()) == 0 for k in (2, 3))
rec("CHECK", "K0", on and me and pr, "b1..b4 orthonormal; b1 = C2(1), b2 = C2(-1) maximally entangled; b3 = |0+>, b4 = |1-> products")

P = [B[k] * B[k].H for k in range(4)]
CNOT = Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
al, be = symbols('al be', real=True)
u = exp(I * al) * P[0] + exp(I * be) * P[1] + exp(I * (al + be)) * P[2] + P[3]
unit = sp.simplify(expand(u * u.H)) == eye(4)
comm = sp.simplify(expand(u * CNOT - CNOT * u)) == zeros(4, 4)
wts = [Matrix([1, 0]), Matrix([0, 1]), Matrix([1, 1]), Matrix([0, 0])]
simple = all(wts[i] != wts[j] for i in range(4) for j in range(i + 1, 4))
rec("CHECK", "K1", sp.simplify(CNOT - (eye(4) - 2 * P[3])) == zeros(4, 4) and unit and comm and simple,
    "CNOT = I - 2|1-><1-|; u(al, be) unitary, commutes with CNOT; weights (al, be, al+be, 0) pairwise distinct (simple spectrum)")

zM = (eye(4) - 2 * P[0]) / 8
fixH = sp.simplify(expand(u * zM * u.H - zM)) == zeros(4, 4)
fixC = sp.simplify(CNOT * zM * CNOT - zM) == zeros(4, 4)
zt = tab(zM)
back = sp.simplify(pauliW(zt) - zM) == zeros(4, 4)
Mb = coef(B[0])
opn = sp.simplify(Mb * Mb.H - eye(2) / 2) == zeros(2, 2)
rec("CHECK", "K2", fixH and fixC and back and opn,
    "z = (I - 2P_{b1})/8 fixed by H0 and CNOT; its table reproduces it; M(b1) M(b1)^dag = I/2, so |<b1|x(x)y>|^2 <= 1/2 and z in maxCone",
    "table of z: %s" % [list(zt.row(i)) for i in range(4)])

ev = (8 * zM).eigenvals()
evl = sorted(sum(([sp.nsimplify(k)] * m for k, m in ev.items()), []))
pair = sp.simplify(expand((P[0] * zM).trace()))
rec("CHECK", "K3", evl == [-1, 1, 1, 1] and pair == Q(-1, 8),
    "8 pauliW(z) has eigenvalues (-1, 1, 1, 1): one negative, lambda_2 = -lambda_1 (X's condition, boundary); tr(P_b1 z) = -1/8 (K != Q3)",
    "eigenvalues %s" % evl)

e = [Matrix([1 if i == k else 0 for i in range(4)]) for k in range(4)]
f = Matrix([-1, 1, 1, 1])
gens = [e[1], e[2], e[3], e[0] + e[1], e[0] + e[2], e[0] + e[3], f]
facets = set()
for tri in itertools.combinations(range(len(gens)), 3):
    Mt = Matrix.hstack(*[gens[i] for i in tri]).T
    ns = Mt.nullspace()
    if len(ns) != 1: continue
    n = ns[0]
    vals = [(n.T * g)[0] for g in gens]
    if all(v >= 0 for v in vals): pass
    elif all(v <= 0 for v in vals): n = -n
    else: continue
    den = sp.ilcm(*[sp.fraction(sp.nsimplify(x))[1] for x in n]); n = n * den
    g_ = sp.igcd(*[int(x) for x in n if x != 0]); n = n / g_
    facets.add(tuple(n))
def is_extreme(i):
    others = [gens[j] for j in range(len(gens)) if j != i]
    # extreme iff not in the cone of the others: test via the facets it lies on (rank 3 of active normals)
    act = [Matrix(fc) for fc in facets if (Matrix(fc).T * gens[i])[0] == 0]
    return len(act) > 0 and Matrix.hstack(*act).rank() == 3
ext = set()
for i, g in enumerate(gens):
    if is_extreme(i):
        g2 = g * sp.ilcm(*[sp.fraction(x)[1] for x in g]); g2 = g2 / sp.igcd(*[int(x) for x in g2 if x != 0]); ext.add(tuple(g2))
selfpos = all((a.T * b)[0] >= 0 for a in gens for b in gens)
rec("CHECK", "K4", facets == ext and selfpos and f not in [e[0], e[1], e[2], e[3]],
    "the slice C: facet normals = extreme rays (%d each), generators pairwise >= 0: C* = C; f = (-1,1,1,1) in C, so C != R^4_+" % len(ext),
    "extreme rays %s" % sorted(ext))

PB = [Matrix([1, 0, 0, 0]), Matrix([0, 1, 0, 0]), k1p, k1m]
rec("COUNTERCONTROL", "CC1", all(sp.simplify(coef(v).det()) == 0 for v in PB),
    "the product basis {|00>, |01>, |1+>, |1->}: every basis vector is a product (no entangled fixed ray)")
ev2 = sorted(sum(([sp.nsimplify(k)] * m for k, m in (eye(4) - Q(5, 2) * P[0]).eigenvals().items()), []))
rec("COUNTERCONTROL", "CC2", ev2 == [Q(-3, 2), 1, 1, 1] and 1 < Q(3, 2) and 1 - Q(5, 2) * Q(1, 2) < 0,
    "c = 5/2: eigenvalues (-3/2, 1, 1, 1) violate lambda_2 >= -lambda_1; 1 - (5/2)(1/2) < 0 at a best product", "eigenvalues %s" % ev2)

recorded = list(zt) + evl + ev2 + [pair] + [x for fc in facets for x in fc]
rec("CHECK", "EX", not any(sp.sympify(t).has(sp.Float) for t in recorded), "no Float in any recorded value")

nfail = R_.count(False)
print("summary: %d checks, %d failed" % (len(R_), nfail))
if nfail == 0:
    print("VERDICT C10-B3C-CASE-EXACT: for H0 = the 2-torus with weights (al, be, al+be, 0) on {C2(1), C2(-1), |0+>, |1->} "
          "(two product lines, simple spectrum) and G = H0 x <cnot>, the single-defect cone K({z_C2(1)}) is an explicit "
          "G-invariant exotic cone; its H0-slice is the self-dual cone with extreme rays %s" % sorted(ext))
else:
    print("NO VERDICT")
