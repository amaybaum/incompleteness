"""EQ3-P probe p4 -- milestone 2 ladder: what the two-copy SHADOWS of the four-copy instance select (exact
ingredients).  Research only; base bcbc516f.  Usage: python3 -I -B p4_cone_ladder.py

Shadows (two-copy statements, no four-copy filters):
  (S-tw)  admissible (SEP <= K <= max) + K = K*      (Euclidean self-duality; what twin links give)
  (S-cn)  admissible + K = T(K*)                     (B-self-duality, B(X,Y) = <X, T Y>; what Bell links give)
CLAIMS:
  L1 the element y = diag(1, 1, 0, 1) (a table) lies in max \ (Q3 u Tw): its value on products is
     pairVal(hom x, hom x', y) = 1 + x0 x0' + x2 x2' (symbolic; >= 0 on the ball by Cauchy-Schwarz, written); pauliW(y)
     has the eigenvector |01> - |10>... with eigenvalue -1/4 (exact), and PT_2 pauliW(y) = pauliW(y) (y has no Y index), so
     y is in neither Q3 nor Tw.  With y, C0 = SEP + R+ y is Euclidean self-positive (<y, y> = 3 > 0, <y, SEP> >= 0 since
     y in max).  [Written: in a Euclidean space a maximal self-positive closed cone is self-dual (if z in K* \ K then
     K + R+ z is self-positive because <z, z> >= 0); Zorn gives a self-dual K >= C0, admissible (K = K* <= SEP* = max),
     containing y, so K is neither Q3 nor Tw: (S-tw) does NOT select the quantum cone or the twin.]
  L2 isotropic sector (U (x) conj U twirl; commutes with T, B-self-adjoint): in the plane span{1, Phi+} with the
     pairing <(a,b),(a',b')> = 4aa' + ab' + ba' + bb', the sectors of Q3, Tw, SEP are the wedges
     [1 - Phi+, Phi+] (90 deg), [1 + 2Phi+, 1 - 2Phi+] (90 deg), [1 - Phi+, 1 + 2Phi+] (60 deg), and the 90-degree
     wedges W_s = cone((s, 1), (1, -(4s+1)/(s+1))) contain the SEP wedge for every s in [0, 1/2] (exact, symbolic s):
     the sector-level necessary condition of (S-cn) leaves a one-parameter family (Q3 at s = 0, Tw at s = 1/2).
  L3 spin factors excluded for (S-cn): the B-null pure products (one factor a Y-eigenstate, B(p,p) = 0) span a
     12-dimensional subspace of tables (exact rank), while for K = Q^-1(L_a) (Q a T-isometry, L_a a round Lorentz cone
     with T-even unit axis a) B-null products must map into R a + V_- (dimension 1 + 6 = 7); 12 > 7, so no admissible
     co-self-dual cone is of that form.  The written step: for v = Q p in L_a, 2 |v_{V+ minus axis}|^2 <= B(p,p).
     Control: the T-signature is (10, 6) (exact count).
  L4 first-order rigidity ingredient: (1/16) sum_{a,b in {0,1,+,-}} |ab><ab| = 1/4 (exact), so for Xi in o(B)
     (tr Xi(1) = 0) the trace of Xi on real products averages to 0; with B(Xi p, p) = 0 for real products the
     admissible-tangent condition forces the complement block of Xi(p) to vanish at real products (written).
DECISION RULE (fixed before the first run): verdict `P4-LADDER-INGREDIENTS-EXACT` iff all pass.  Exact arithmetic only.
"""
import itertools
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sympy as sp  # noqa: E402
from sympy import I, Matrix, Rational as R, eye, zeros  # noqa: E402

import eq3_lib as L  # noqa: E402

check = L.check
DEL = L.DELTA
y = sp.diag(1, 1, 0, 1)
xs, xps = sp.symbols("x0:3", real=True), sp.symbols("z0:3", real=True)
yop = L.pauliW(y)
v = Matrix([0, 1, -1, 0])
check("L1 y = diag(1,1,0,1): value on products 1 + x0 x0' + x2 x2' (symbolic; >= 0 on the ball, written)",
      sp.expand(L.pair_val(L.hom(xs), L.hom(xps), y) - (1 + xs[0] * xps[0] + xs[2] * xps[2])) == 0)
check("L1 pauliW(y) has eigenvalue -1/4 on |01> - |10> (y not in Q3) and PT_2 pauliW(y) = pauliW(y) (y not in Tw)",
      L.zero(yop * v + v / 4) and L.zero(L.pt_copy(yop, 1, 2) - yop) and L.zero(y * DEL - y))
check("L1 <y, y> = 3 > 0 (Euclidean self-pairing; C0 = SEP + R+ y is self-positive given y in max)", L.eucl(y, y) == 3)

# ---------------------------------------------------------------- L2 isotropic sector
phip = Matrix([1, 0, 0, 1]) * Matrix([1, 0, 0, 1]).T / 2
one = eye(4)


def vec(a, b):
    return L.coordsW(a * one + b * phip)


def ip(p1, p2):
    return L.eucl(vec(*p1), vec(*p2)) / 4          # = tr of the operators' product


check("L2 the sector pairing is tr((a 1 + b Phi+)(a' 1 + b' Phi+)) = 4aa' + ab' + ba' + bb' (symbolic a, b, a', b')",
      sp.expand(ip(sp.symbols("a b"), sp.symbols("c d")) - (4 * sp.Symbol("a") * sp.Symbol("c") + sp.Symbol("a")
                                                               * sp.Symbol("d") + sp.Symbol("b") * sp.Symbol("c")
                                                               + sp.Symbol("b") * sp.Symbol("d"))) == 0)
check("L2 Q3 wedge [1 - Phi+, Phi+] and Tw wedge [1 + 2Phi+, 1 - 2Phi+] are right angles; SEP wedge [1 - Phi+, "
      "1 + 2Phi+] has cos = 1/2 (60 deg)",
      ip((1, -1), (0, 1)) == 0 and ip((1, 2), (1, -2)) == 0
      and sp.simplify(ip((1, -1), (1, 2)) / sp.sqrt(ip((1, -1), (1, -1)) * ip((1, 2), (1, 2)))) == R(1, 2))
s = sp.Symbol("s", nonnegative=True)
e1, e2 = (s, 1), (1, -(4 * s + 1) / (s + 1))
# containment of the SEP wedge: 1 - Phi+ and 1 + 2 Phi+ are nonnegative combinations of e1, e2 for s in [0, 1/2]
def cramer(t):
    # solve al*e1 + be*e2 = t (2x2, Cramer's rule; no solver call)
    det = e1[0] * e2[1] - e2[0] * e1[1]
    return sp.simplify((t[0] * e2[1] - e2[0] * t[1]) / det), sp.simplify((e1[0] * t[1] - t[0] * e1[1]) / det)


a1, b1 = cramer((1, -1))
a2, b2 = cramer((1, 2))
okcr = all(sp.simplify(a * e1[k] + b * e2[k] - t[k]) == 0 for (a, b, t) in ((a1, b1, (1, -1)), (a2, b2, (1, 2)))
           for k in (0, 1))
okc = True
for sv in (R(0), R(1, 10), R(1, 4), R(2, 5), R(1, 2)):
    okc = okc and all(sp.simplify(t.subs(s, sv)) >= 0 for t in (a1, b1, a2, b2))
check("L2 W_s = cone((s,1), (1, -(4s+1)/(s+1))) is a right angle for symbolic s, equals the Q3 wedge at s = 0 and the "
      "Tw wedge at s = 1/2, and contains the SEP wedge (nonnegative coefficients, exact at s = 0, 1/10, 1/4, 2/5, 1/2)",
      sp.simplify(ip(e1, e2)) == 0 and okc and okcr
      and sp.simplify(e2[1].subs(s, 0)) == -1 and sp.simplify(e2[1].subs(s, R(1, 2))) == -2)
L.note(f"L2 closed forms: 1 - Phi+ = ({a1}) e1 + ({b1}) e2 ; 1 + 2Phi+ = ({a2}) e1 + ({b2}) e2")

# ---------------------------------------------------------------- L3 spin factors
tsig = [L.SGNY[m] * L.SGNY[n] for m in range(4) for n in range(4)]
check("L3 control: the T-signature on tables is (10, 6)", (tsig.count(1), tsig.count(-1)) == (10, 6))
rows = []
for yk in ([0, 1, 0], [0, -1, 0]):
    for other in ([1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1], [R(3, 5), R(4, 5), 0],
                  [0, R(3, 5), R(4, 5)]):
        for p in (L.prod_state(yk, other), L.prod_state(other, yk)):
            rows.append([p[m, n] for m in range(4) for n in range(4)])
Mspan = Matrix(rows)
Bnull = all(L.eucl(Matrix(4, 4, r), L.transposeW(Matrix(4, 4, r))) == 0 for r in rows)
check("L3 every listed product with a Y-eigenstate factor is B-null (B(p,p) = 0), and these products span a "
      "12-dimensional subspace of tables (exact rank)", Bnull and Mspan.rank() == 12, Mspan.rank())

# ---------------------------------------------------------------- L4 real-product design
kets = {"0": Matrix([1, 0]), "1": Matrix([0, 1]), "+": Matrix([1, 1]) / sp.sqrt(2), "-": Matrix([1, -1]) / sp.sqrt(2)}
avg = zeros(4, 4)
for a, b in itertools.product(kets, repeat=2):
    w = L.kron(kets[a], kets[b])
    avg += w * w.T
check("L4 (1/16) sum over a, b in {0, 1, +, -} of |ab><ab| = 1/4 (exact)", L.zero(avg / 16 - eye(4) / 4))

ok = L.summary("p4_cone_ladder")
print("VERDICT " + ("P4-LADDER-INGREDIENTS-EXACT" if ok else "NOT RENDERED"))
sys.exit(0 if ok else 1)
