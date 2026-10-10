"""u3_vplus.py -- thread U, node U3 (and U1 supplements): the V+ sub-problem, exactly.

Decision rule (fixed before the first run):
- PASS/FAIL per check; countercontrols PASS only when the altered object FAILS the property.
- `VERDICT U3-VPLUS-EXACT` prints only if every check passes; else `VERDICT U3-VPLUS-FAILED`. Exact arithmetic.
Checked: V1 P+ of a pure product is the pinching (|v_ab><v_ab|, |<1-|ab>|^2) with v_ab = Pi+|ab> and the explicit
coordinates; V2 K_gen+ misses the cnot-invariant entangled pure state (|00> + |1+>)/sqrt2 of Q3+; V3 E0 ∈ V+ with
block data A0 (spectrum 3/4, 1/4, -1/4) and c0 = 1/4, so K*+ = (Q3+ ∩ E0*) + R+ E0 differs from Q3+;
V4 the cnot-fixed members of Z_F lie in V+ and outside Q3 (K_F ∩ V+ also differs from Q3+);
V5 (U1) the excluded pure states P_g (for E0) and P_t (for F) are entangled and so are their CNOT images.
"""
import sympy as sp

I = sp.I
S = [sp.eye(2), sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -I], [I, 0]]), sp.Matrix([[1, 0], [0, -1]])]
RES = []


def check(cid, kind, ok, detail=""):
    ok = bool(ok)
    RES.append(ok)
    print(("PASS " if ok else "FAIL ") + cid + "  [" + kind + "] " + detail)


def kron(A, B):
    return sp.Matrix(A.rows * B.rows, A.cols * B.cols,
                     lambda i, j: A[i // B.rows, j // B.cols] * B[i % B.rows, j % B.cols])


SS = [[kron(S[m], S[n]) for n in range(4)] for m in range(4)]
PC = [[0, 0, 3, 3], [1, 1, 2, 2], [2, 2, 1, 1], [3, 3, 0, 0]]
PT = [[0, 1, 2, 3], [1, 0, 3, 2], [1, 0, 3, 2], [0, 1, 2, 3]]


def sgn(m, n):
    return -1 if (m, n) in ((1, 3), (2, 2)) else 1


def cnot(w):
    return sp.Matrix(4, 4, lambda m, n: sgn(m, n) * w[PC[m][n], PT[m][n]])


def pauliW(w):
    R = sp.zeros(4, 4)
    for m in range(4):
        for n in range(4):
            R += w[m, n] * SS[m][n]
    return R / 4


def table(R):
    return sp.Matrix(4, 4, lambda m, n: sp.expand((R * SS[m][n]).trace()))


def Eunit(m, n):
    E = sp.zeros(4, 4)
    E[m, n] = 1
    return E


UC = sp.Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
r2 = sp.sqrt(2)
B = sp.Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1 / r2, 1 / r2], [0, 0, 1 / r2, -1 / r2]])   # |00>,|01>,|1+>,|1->
Pp = sp.diag(1, 1, 1, 0)
Pm = sp.diag(0, 0, 0, 1)
print("== V1  K_gen+ = cone of pinched products")
x0, x1, y0, y1 = [sp.Symbol(n, real=True) + I * sp.Symbol(n + "i", real=True) for n in ("x0", "x1", "y0", "y1")]
ab = kron(sp.Matrix([x0, x1]), sp.Matrix([y0, y1]))
p = table(ab * ab.H)
pplus = (p + cnot(p)) / 2
Rb = sp.simplify(B.H * pauliW(pplus) * B)
vab = (B.H * ab)[0:3, 0]
gam = (B.H * ab)[3, 0]
pin = sp.diag(1, 1, 1, 1) * 0
pin[0:3, 0:3] = vab * vab.H
pin[3, 3] = gam * sp.conjugate(gam)
check("V1a", "identity", sp.simplify(sp.expand(Rb - pin)) == sp.zeros(4, 4),
      "B^H pauliW(P+ p) B = (|v_ab><v_ab|, |<1-|ab>|^2) with (v_ab, <1-|ab>) = B^H |ab> (generic complex a, b)")
explicit = sp.Matrix([x0 * y0, x0 * y1, x1 * (y0 + y1) / r2, x1 * (y0 - y1) / r2])
check("V1b", "identity", sp.simplify(B.H * ab - explicit) == sp.zeros(4, 1),
      "v_ab = (a0 b0, a0 b1, a1 (b0 + b1)/sqrt2) and <1-|ab> = a1 (b0 - b1)/sqrt2")
offd = [Rb[i, 3] for i in range(3)]
check("V1c", "exact", all(sp.simplify(z) == 0 for z in offd), "P+ p has no V- block (pinching)")

print("== V2  K_gen+ is strictly smaller than Q3+")
w = sp.Matrix([1, 0, 1 / r2, 1 / r2])          # |00> + |1+> in the computational basis
coef = sp.Matrix([[w[0], w[1]], [w[2], w[3]]])
check("V2", "exact", UC * w == w and sp.simplify(coef.det()) != 0 and sp.simplify((B.H * w)[3]) == 0,
      "w = |00> + |1+> is CNOT-invariant, lies in the + space and is entangled (det = %s): its pure state is an "
      "extreme ray of Q3+ = PSD(3) + R+ that no pinched product reaches (a pure element of K_gen+ is a product "
      "in the + space)" % sp.simplify(coef.det()))

print("== V3  E0 ∈ V+ and the V+ part of K*")
E00 = Eunit(0, 0)
E0 = E00 + Eunit(1, 3) - Eunit(2, 2)
RE = sp.simplify(B.H * pauliW(E0) * B)
A0 = RE[0:3, 0:3]
lamA = sp.symbols("lamA")
cp = sp.factor((A0 - lamA * sp.eye(3)).det())
check("V3", "exact", cnot(E0) == E0 and all(sp.simplify(RE[i, 3]) == 0 for i in range(3)) and RE[3, 3] == sp.Rational(1, 4)
      and sp.expand(cp + (lamA - sp.Rational(3, 4)) * (lamA - sp.Rational(1, 4)) * (lamA + sp.Rational(1, 4))) == 0,
      "E0 = (A0, 1/4) ∈ V+ with spec A0 = {3/4, 1/4, -1/4}: K*+ = (Q3+ ∩ E0*) + R+ E0 contains E0 ∉ Q3+")

print("== V4  the cnot-fixed members of Z_F")


def zF(s1, s2):
    return (E00 + s1 * Eunit(1, 3) + s2 * Eunit(2, 2) - s1 * s2 * Eunit(3, 1)) / 4


ok4 = True
for s in ((1, -1), (-1, 1)):
    zz = zF(*s)
    ev = pauliW(zz).eigenvals()
    ok4 = ok4 and cnot(zz) == zz and min(ev.keys()) == sp.Rational(-1, 8)
check("V4", "exact", ok4, "z_(1,-1), z_(-1,1) are cnot-fixed (∈ V+) with eigenvalue -1/8: K_F ∩ V+ ≠ Q3+ as well")

print("== V5  (U1) the excluded pure states are entangled, and so are their CNOT images")
gv = sp.Matrix([-1, 1, 1, 1]) / 2
tv = sp.Matrix([1, 1, 1, -1]) / 2


def det2(v):
    return sp.Matrix([[v[0], v[1]], [v[2], v[3]]]).det()


vals = [det2(gv), det2(UC * gv), det2(tv), det2(UC * tv)]
check("V5", "exact", all(z != 0 for z in vals),
      "coefficient determinants of g, CNOT g, t, CNOT t: %s (all nonzero): P_g, P_t ∉ SEP ∪ cnot SEP" % vals)
pr = kron(sp.Matrix([1, 2]), sp.Matrix([3, -1]))
check("V5c", "countercontrol", det2(pr) == 0, "a product vector has coefficient determinant 0 (the test detects products)")

print()
nfail = RES.count(False)
print("checks: %d, failed: %d" % (len(RES), nfail))
print("VERDICT " + ("U3-VPLUS-EXACT" if nfail == 0 else "U3-VPLUS-FAILED") + " -- %d checks" % len(RES))
