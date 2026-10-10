"""u1_struct.py -- thread U, node U1: the cnot eigenspace structure, exactly.

Decision rule (fixed before the first run):
- Every check prints PASS or FAIL with its id and kind. Countercontrols are phrased so that PASS means the
  deliberately wrong object FAILS the property (a countercontrol that does not fail prints FAIL).
- The VERDICT line `U1-STRUCT-EXACT` prints only if every check, countercontrols included, is PASS;
  otherwise `VERDICT U1-STRUCT-FAILED`.
- Exact arithmetic only (sympy rationals / Gaussian rationals / sqrt(2) symbolic). No floats.
Objects (re-implemented here): cnot from the landed sgn/pc/pt tables [K CompositeDimension.lean:741-786];
pauliW w = (1/4) sum w_mn s_m (x) s_n [D FourCopyPackage.lean:176]; ipW = Euclidean sum [D FourCopyDefs:31].
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


def vec(w):
    return sp.Matrix([w[i] for i in range(16)])


def unvec(c):
    return sp.Matrix(4, 4, lambda m, n: c[4 * m + n])


UC = sp.Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])   # control = first token
UC2 = sp.Matrix([[1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0]])  # control = second token
RES = []


def check(cid, kind, ok, detail=""):
    ok = bool(ok)
    RES.append(ok)
    print(("PASS " if ok else "FAIL ") + cid + "  [" + kind + "] " + detail)


wsym = sp.Matrix(4, 4, lambda m, n: sp.Symbol("w%d%d" % (m, n), real=True))
vsym = sp.Matrix(4, 4, lambda m, n: sp.Symbol("v%d%d" % (m, n), real=True))

print("== S1  cnot is CNOT conjugation (control on token 0)")
lhs = cnot(wsym)
rhs = table(UC * pauliW(wsym) * UC)
check("C1", "identity", sp.simplify(lhs - rhs) == sp.zeros(4, 4),
      "landed signed permutation = Ad(CNOT) on a generic symbolic table")
rhs2 = table(UC2 * pauliW(wsym) * UC2)
check("C1c", "countercontrol", sp.simplify(lhs - rhs2) != sp.zeros(4, 4),
      "Ad(CNOT with control on token 1) differs from the landed gate")
check("C2", "identity", sp.expand(ipW(wsym, vsym) - 4 * (pauliW(wsym) * pauliW(vsym)).trace()) == 0,
      "ipW w v = 4 tr(pauliW w pauliW v), generic")

print("== S2  cnot as a 16x16 matrix: orthogonal involution, eigenspace dimensions")
C = sp.zeros(16, 16)
for j in range(16):
    e = sp.zeros(16, 1)
    e[j] = 1
    C[:, j] = vec(cnot(unvec(e)))
check("C3a", "exact", C * C == sp.eye(16) and C.T * C == sp.eye(16), "cnot^2 = I and cnot^T cnot = I")
rp, rm = (C + sp.eye(16)).rank(), (C - sp.eye(16)).rank()
check("C3b", "exact", rp == 10 and rm == 6 and C.trace() == 4,
      "dim V+ = rank(C+I) = %d, dim V- = rank(C-I) = %d, trace = %s" % (rp, rm, C.trace()))
Pp = (sp.eye(16) + C) / 2
Pm = (sp.eye(16) - C) / 2
check("C3c", "exact", Pp * Pp == Pp and Pp.T == Pp and Pp * Pm == sp.zeros(16, 16),
      "P+ = (I + cnot)/2 is the orthogonal projector onto V+, P+ P- = 0")

print("== S3  V+ is the Pauli image of the Hermitian commutant of CNOT (independent route)")
xs = sp.symbols("x0:16", real=True)
M = sp.zeros(4, 4)
k = 0
for i in range(4):
    M[i, i] = xs[k]
    k += 1
for i in range(4):
    for j in range(i + 1, 4):
        M[i, j] = xs[k] + I * xs[k + 1]
        M[j, i] = xs[k] - I * xs[k + 1]
        k += 2
eqs = []
for z in (M * UC - UC * M):
    z = sp.expand(z)
    eqs += [sp.re(z), sp.im(z)]
A_eq = sp.Matrix([[sp.diff(q, x) for x in xs] for q in eqs])
null = A_eq.nullspace()
check("C4a", "exact", len(null) == 10, "real dimension of {M Hermitian : M CNOT = CNOT M} = %d" % len(null))
tabs = []
for nv in null:
    Mn = M.subs({xs[t]: nv[t] for t in range(16)})
    tabs.append(vec(table(Mn)))
T = sp.Matrix.hstack(*tabs)
check("C4b", "exact", (C * T - T) == sp.zeros(16, 10) and T.rank() == 10,
      "the 10 commutant tables lie in V+ and span it (rank 10)")
Mbad = sp.zeros(4, 4)
Mbad[0, 3] = 1
Mbad[3, 0] = 1
check("C4c", "countercontrol", (C * vec(table(Mbad)) - vec(table(Mbad))) != sp.zeros(16, 1),
      "|00><11| + h.c. (not in the commutant) is not in V+")

print("== S4  block form in the CNOT eigenbasis |00>, |01>, |1+>, |1->")
r2 = sp.sqrt(2)
B = sp.Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1 / r2, 1 / r2], [0, 0, 1 / r2, -1 / r2]])
check("C5a", "exact", sp.simplify(B.H * B) == sp.eye(4) and
      sp.simplify(B.H * UC * B) == sp.diag(1, 1, 1, -1), "B unitary; B^H CNOT B = diag(1,1,1,-1)")
wp = unvec(Pp * vec(wsym))
wm = unvec(Pm * vec(wsym))
Rp = sp.simplify(B.H * pauliW(wp) * B)
Rm = sp.simplify(B.H * pauliW(wm) * B)
offp = [Rp[i, 3] for i in range(3)] + [Rp[3, i] for i in range(3)]
check("C5b", "exact", all(sp.simplify(z) == 0 for z in offp),
      "every V+ element is block diagonal Herm(3) + R in this basis (generic symbolic)")
diagm = [Rm[i, j] for i in range(3) for j in range(3)] + [Rm[3, 3]]
check("C5c", "exact", all(sp.simplify(z) == 0 for z in diagm),
      "every V- element is purely off-diagonal (beta in C^3, 6 real dims) in this basis")
blk = sp.simplify(Rp[0:3, 0:3])
check("C5d", "exact", blk.H == blk and sp.im(sp.simplify(Rp[3, 3])) == 0,
      "the V+ blocks are Hermitian 3x3 and a real scalar (Herm(3) + R, 9 + 1 = 10)")

print("== S5  the overlap identity <w, cnot w> = |w+|^2 - |w-|^2 and its value on pure products")
nw = sp.expand(ipW(wsym, cnot(wsym)))
check("C6a", "identity", sp.expand(nw - (ipW(wp, wp) - ipW(wm, wm))) == 0,
      "<w, cnot w> = |P+ w|^2 - |P- w|^2, generic")
check("C6b", "identity", sp.expand(nw - 4 * (pauliW(wsym) * UC * pauliW(wsym) * UC).trace()) == 0,
      "<w, cnot w> = 4 tr(rho U rho U), U = CNOT, generic")
s, t, u, v = sp.symbols("s t u v", real=True)


def stereo(a, b):
    d = a ** 2 + b ** 2 + 1
    return [2 * a / d, 2 * b / d, (a ** 2 + b ** 2 - 1) / d]


def hom(x):
    return [sp.Integer(1)] + list(x)


def prod(x, y):
    hx, hy = hom(x), hom(y)
    return sp.Matrix(4, 4, lambda m, n: hx[m] * hy[n])


xu, yu = stereo(s, t), stereo(u, v)
pu = prod(xu, yu)
check("C7a", "identity", sp.simplify(ipW(pu, pu) - 4) == 0, "|p|^2 = 4 for every pure product (unit x, y)")
form = (1 + xu[2] + yu[0] - xu[2] * yu[0]) ** 2
check("C7b", "identity", sp.simplify(ipW(pu, cnot(pu)) - form) == 0,
      "<p, cnot p> = (1 + x3 + y1 - x3*y1)^2 = 4 <ab|CNOT|ab>^2 for unit x, y (exact rational identity)")
xf = sp.symbols("x1:4", real=True)
yf = sp.symbols("y1:4", real=True)
pf = prod(xf, yf)
check("C7c", "countercontrol", sp.expand(ipW(pf, cnot(pf)) - (1 + xf[2] + yf[0] - xf[2] * yf[0]) ** 2) != 0,
      "the C7b formula is not a polynomial identity off the unit spheres (unit length is load-bearing)")
axes = []
for i in range(3):
    for sg in (1, -1):
        e = [0, 0, 0]
        e[i] = sg
        axes.append(e)
vals, accp = [], sp.zeros(16, 1)
for x in axes:
    for y in axes:
        p = prod(x, y)
        vals.append(ipW(p, cnot(p)))
        accp += Pp * vec(p)
E00 = sp.zeros(4, 4)
E00[0, 0] = 1
check("C8a", "enumerate", all(z >= 0 for z in vals),
      "36 axis products: <p, cnot p> in %s; zeros (|p-| = |p+|): %d" % (sorted(set(vals)), vals.count(0)))
check("C8b", "enumerate", unvec(accp / 36) == E00,
      "the average of P+ p over the 36 axis products is E00 (so is the average of p)")
nplus = [sp.Rational(4 + z, 2) for z in vals]
check("C8c", "identity", min(nplus) >= 2, "|P+ p|^2 = (4 + <p, cnot p>)/2 >= 2 on the 36 axis products")

print()
nfail = RES.count(False)
print("checks: %d, failed: %d" % (len(RES), nfail))
print("VERDICT " + ("U1-STRUCT-EXACT" if nfail == 0 else "U1-STRUCT-FAILED") + " -- %d checks" % len(RES))
