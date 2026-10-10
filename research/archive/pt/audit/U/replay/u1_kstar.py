"""u1_kstar.py -- thread U: the surgery cone K* = (Q3 ∩ E0*) + R+ E0, its exact ingredients for H1-H3.

Decision rule (fixed before the first run):
- PASS/FAIL per check; countercontrols PASS only when the deliberately wrong object FAILS the property.
- `VERDICT KSTAR-INGREDIENTS-EXACT` prints only if every check passes; else `VERDICT KSTAR-INGREDIENTS-FAILED`.
- Exact arithmetic only (sympy rationals, Gaussian rationals, symbolic polynomials). No floats.
What is checked here (the written proof that uses these ingredients is RESULT.md §1, Theorem E):
  S1 data of E0 (cnot E0 = E0, <E0,E0> = 3, rational orthonormal eigenbasis, spectrum, maxCone, not PSD);
  S2 H1: products are PSD and pair >= 0 with E0, by symbolic identities (an SOS certificate on the ball);
  S3 H2: <cnot w, E0> = <w, E0> for generic w;
  S4 H3: the projection-lemma determinant identity and its sign for <q,E0> < 0, with a countercontrol;
  S5 instance checks of the projection lemma by exact LDL pivots;
  S6 distinctness: E0 ∈ K* \\ Q3 and G ∈ Q3 \\ K*.
"""
import sympy as sp

I = sp.I
S = [sp.eye(2), sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -I], [I, 0]]), sp.Matrix([[1, 0], [0, -1]])]


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


def ipW(w, v):
    return sp.expand(sum(w[i] * v[i] for i in range(16)))


def pairval(w, x, y):
    hx, hy = [1] + list(x), [1] + list(y)
    return sp.expand(sum(hx[m] * w[m, n] * hy[n] for m in range(4) for n in range(4)))


def Eunit(m, n):
    E = sp.zeros(4, 4)
    E[m, n] = 1
    return E


RES = []


def check(cid, kind, ok, detail=""):
    ok = bool(ok)
    RES.append(ok)
    print(("PASS " if ok else "FAIL ") + cid + "  [" + kind + "] " + detail)


def ldl_pivots(R):
    """Exact LDL^H pivots of a Hermitian matrix (no pivoting); None if a zero pivot is met first."""
    A = sp.Matrix(R)
    n = A.rows
    piv = []
    for k in range(n):
        p = sp.nsimplify(sp.simplify(A[k, k]))
        if p == 0:
            return None
        piv.append(p)
        for i in range(k + 1, n):
            f = A[i, k] / p
            for j in range(k + 1, n):
                A[i, j] = sp.simplify(A[i, j] - f * A[k, j])
    return piv


E00 = Eunit(0, 0)
E0 = Eunit(0, 0) + Eunit(1, 3) - Eunit(2, 2)
RE = pauliW(E0)
print("== S1  data of E0")
check("D1", "exact", cnot(E0) == E0 and ipW(E0, E0) == 3, "cnot E0 = E0; <E0, E0> = 3")
X, Y, Z = S[1], S[2], S[3]
check("D2", "identity", RE == (sp.eye(4) + kron(X, Z) - kron(Y, Y)) / 4, "pauliW E0 = (I + X(x)Z - Y(x)Y)/4")
e1 = sp.Matrix([-1, 1, -1, -1]) / 2
e2 = sp.Matrix([1, 1, 1, -1]) / 2
e3 = sp.Matrix([1, 1, -1, 1]) / 2
g = sp.Matrix([-1, 1, 1, 1]) / 2
V = sp.Matrix.hstack(e1, e2, e3, g)
lam = [sp.Rational(3, 4), sp.Rational(1, 4), sp.Rational(1, 4), sp.Rational(-1, 4)]
check("D3", "exact", V.T * V == sp.eye(4) and V.T * RE * V == sp.diag(*lam),
      "rational orthonormal eigenbasis (e1, e2, e3, g) with spectrum 3/4, 1/4, 1/4, -1/4")
r2 = sp.sqrt(2)
v1m = sp.Matrix([0, 0, 1, -1]) / r2
check("D4", "exact", sp.simplify((v1m.T * RE * v1m)[0] - sp.Rational(1, 4)) == 0 and
      sp.simplify(RE * v1m - v1m / 4) == sp.zeros(4, 1), "|1-> is an eigenvector of pauliW E0, eigenvalue 1/4")
Mb = sp.Matrix(3, 3, lambda j, k: E0[j + 1, k + 1])
loc = [E0[0, k] for k in range(1, 4)] + [E0[k, 0] for k in range(1, 4)]
ev = (Mb.T * Mb).eigenvals()
smax2 = max(ev.keys())
check("D5", "exact", all(z == 0 for z in loc) and smax2 <= E0[0, 0] ** 2 and E0[0, 0] > 0,
      "E0 has no local part and sigma_max(M)^2 = %s <= E0_00^2 = 1, so E0 ∈ maxCone (lemma MC)" % smax2)
Mbad = 2 * Mb
wbad = E00 + 2 * (Eunit(1, 3) - Eunit(2, 2))
wit = pairval(wbad, [1, 0, 0], [0, 0, -1])
check("D5c", "countercontrol", max((Mbad.T * Mbad).eigenvals().keys()) > 1 and wit < 0,
      "E00 + 2(E13 - E22): sigma_max^2 = 4 > 1 and the product a = e1, b = -e3 pairs to %s < 0" % wit)
check("D6", "exact", (g.T * RE * g)[0] == sp.Rational(-1, 4), "E0 ∉ Q3: g^T pauliW(E0) g = -1/4")

print("== S2  H1: every product state lies in Q3 ∩ E0*")
xs = sp.symbols("x1:4", real=True)
ys = sp.symbols("y1:4", real=True)
P = sp.Matrix(4, 4, lambda m, n: ([1] + list(xs))[m] * ([1] + list(ys))[n])
nx2 = sum(t ** 2 for t in xs)
ny2 = sum(t ** 2 for t in ys)
sos = ((1 - nx2) + (1 - ny2) + (xs[0] + ys[2]) ** 2 + (xs[1] - ys[1]) ** 2 + xs[2] ** 2 + ys[0] ** 2) / 2
check("H1a", "identity", sp.expand(ipW(P, E0) - sos) == 0,
      "<prodState x y, E0> = 1 + x1 y3 - x2 y2 = (1/2)[(1-|x|^2) + (1-|y|^2) + (x1+y3)^2 + (x2-y2)^2 + x3^2 + y1^2]")
rx = (sp.eye(2) + xs[0] * X + xs[1] * Y + xs[2] * Z) / 2
ry = (sp.eye(2) + ys[0] * X + ys[1] * Y + ys[2] * Z) / 2
check("H1b", "identity", sp.expand(pauliW(P) - kron(rx, ry)) == sp.zeros(4, 4) and
      sp.expand(rx.det() - (1 - nx2) / 4) == 0 and rx.trace() == 1,
      "pauliW(prodState x y) = rho(x) (x) rho(y); det rho(x) = (1-|x|^2)/4, tr = 1 (PSD on the ball)")
wb = E00 + 2 * Eunit(1, 3)
check("H1c", "countercontrol", pairval(wb, [1, 0, 0], [0, 0, -1]) < 0,
      "a surgery vector outside maxCone (E00 + 2 E13) has a product with negative pairing: H1 needs E0 ∈ maxCone")

print("== S3  H2: cnot fixes E0 and preserves pairings with it")
wsym = sp.Matrix(4, 4, lambda m, n: sp.Symbol("w%d%d" % (m, n), real=True))
check("H2a", "identity", sp.expand(ipW(cnot(wsym), E0) - ipW(wsym, E0)) == 0,
      "<cnot w, E0> = <w, E0> for generic w (cnot symmetric orthogonal, cnot E0 = E0)")

print("== S4  H3: the projection lemma (PL) for pure states in the E0-cap")
cs = [sp.Symbol("a%d" % j, real=True) + I * sp.Symbol("b%d" % j, real=True) for j in range(4)]
nn = [sp.expand(c * sp.conjugate(c)) for c in cs]
cvec = sp.Matrix(cs)
psi = V * cvec
rq = psi * psi.H
Bq = sp.expand(4 * (RE * rq).trace())
check("P1", "identity", sp.expand(Bq - (3 * nn[0] + nn[1] + nn[2] - nn[3])) == 0,
      "B := <q, E0> = 3 n1 + n2 + n3 - ng for q = |psi><psi|, psi = c1 e1 + c2 e2 + c3 e3 + cg g")
q = table(rq)
Piq = q - (ipW(q, E0) / 3) * E0
rp = sp.expand(pauliW(Piq))
check("P2", "identity", sp.expand(rp - (rq - (Bq / 3) * RE)) == sp.zeros(4, 4),
      "pauliW(Pi q) = |psi><psi| - (B/3) pauliW(E0), Pi = orthogonal projection onto E0-perp")
Dm = V.T * rp * V
det = sp.expand(Dm.det())
r23 = nn[1] + nn[2]
target = sp.expand(-Bq ** 3 * (11 * nn[3] - nn[0] - 11 * r23) / 6912)
check("P3", "identity", sp.expand(det - target) == 0,
      "det pauliW(Pi q) = -B^3 (11 ng - n1 - 11(n2+n3)) / 6912 (generic complex coordinates)")
check("P4", "identity", sp.expand((11 * nn[3] - nn[0] - 11 * r23) - (-11 * Bq + 32 * nn[0])) == 0,
      "11 ng - n1 - 11(n2+n3) = -11 B + 32 n1, so for B < 0 the determinant is > 0")
kk = -Bq / 12
A3 = sp.expand(Dm[0:3, 0:3] - (kk * sp.diag(3, 1, 1) + cvec[0:3, 0] * cvec[0:3, 0].H))
check("P5", "identity", A3 == sp.zeros(3, 3),
      "the principal block on (e1, e2, e3) is k diag(3,1,1) + c c^H with k = -B/12 (positive definite if B < 0)")
qb = table(e1 * e1.T)
rb = pauliW(qb - (ipW(qb, E0) / 3) * E0)
check("P6", "countercontrol", ipW(qb, E0) > 0 and (e2.T * rb * e2)[0] < 0,
      "outside the cap (psi = e1, B = %s > 0) the projection is not PSD: e2^T rho' e2 = %s" %
      (ipW(qb, E0), (e2.T * rb * e2)[0]))

print("== S5  PL instances in the cap: exact LDL pivots of pauliW(Pi q) are all positive")
R = sp.Rational
inst = [(0, 0, 0, 1), (R(1, 2), 0, 0, 1), (0, 1, I, 2), (R(1, 3), 0, 1, 1 + I), (0, R(9, 10), 0, 1),
        (0, 1, 0, 1 + R(1, 100)), (R(1, 2), R(1, 2), R(1, 2), R(3, 2))]
for t, cc in enumerate(inst):
    ps = V * sp.Matrix(cc)
    rq_ = ps * ps.H
    B_ = sp.nsimplify(sp.expand(4 * (RE * rq_).trace()))
    rp_ = sp.expand(rq_ - (B_ / 3) * RE)
    piv = ldl_pivots(rp_)
    ok = B_ < 0 and piv is not None and all(sp.nsimplify(p) > 0 for p in piv)
    check("L%d" % (t + 1), "instance", ok, "c = %s: B = %s, pivots %s" % (str(cc), B_, piv))

print("== S6  distinctness and the closedness ingredient")
G = table(g * g.T)
check("X1", "exact", ipW(G, E0) == -1 and (pauliW(G) * pauliW(G) - pauliW(G)) == sp.zeros(4, 4),
      "G = table(g g^T) is a pure state with <G, E0> = -1: G ∈ Q3, and G ∉ K* (K* ⊆ K** forces <G,E0> >= 0)")
check("X2", "exact", pauliW(-E0).trace() == -1, "tr pauliW(-E0) = -1 < 0, so -E0 ∉ Q3 (Q3 + R+ E0 is closed)")
check("X3", "exact", ipW(E0, E00) == 1 and ipW(G, E00) == 1,
      "E0 and G lie on the trace-one slice <., E00> = 1 (K* has a compact base there)")

print()
nfail = RES.count(False)
print("checks: %d, failed: %d" % (len(RES), nfail))
print("VERDICT " + ("KSTAR-INGREDIENTS-EXACT" if nfail == 0 else "KSTAR-INGREDIENTS-FAILED") +
      " -- %d checks" % len(RES))
