"""u2_wigner.py -- thread U, node U2: exact checks of the lemmas of the local Wigner theorem and of U2(c).

Decision rule (fixed before the first run):
- PASS/FAIL per check; countercontrols PASS only when the altered object FAILS the property.
- `VERDICT U2-LEMMAS-EXACT` prints only if every check passes; else `VERDICT U2-LEMMAS-FAILED`. Exact arithmetic.
The written proof (RESULT.md §1, U2) uses: W1 Bloch dictionary; W2 conjugation = reflY on Bloch vectors;
W3 Ad(exp(-i t Z/2)), Ad(exp(-i t Y/2)) are Rz(t), Ry(t) (so SO(3) = Ad(SU(2)) via Euler angles);
W4 the cross-ratio function k(b) is constant iff the two slice maps have the same (anti)linearity;
W5 det of the coefficient matrix of lam u(x)v + mu u'(x)v' = lam mu det[u u'] det[v v'];
W6 an instance of the theorem's conclusion (a local Wigner map preserves all transition probabilities);
W6c countercontrol: slice-wise preservation does not imply the global identity;
O1-O3 for U2(c): pure products span W 3; actT reflY is the partial transpose; twin is not cnot-invariant.
"""
import sympy as sp

I = sp.I
S = [sp.eye(2), sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -I], [I, 0]]), sp.Matrix([[1, 0], [0, -1]])]
X, Y, Z = S[1], S[2], S[3]
RES = []


def check(cid, kind, ok, detail=""):
    ok = bool(ok)
    RES.append(ok)
    print(("PASS " if ok else "FAIL ") + cid + "  [" + kind + "] " + detail)


def kron(A, B):
    return sp.Matrix(A.rows * B.rows, A.cols * B.cols,
                     lambda i, j: A[i // B.rows, j // B.cols] * B[i % B.rows, j % B.cols])


def bloch(v):
    r = v * v.H
    t = r.trace()
    return [sp.simplify((r * S[k]).trace() / t) for k in (1, 2, 3)]


a0, a1, b0, b1 = sp.symbols("a0 a1 b0 b1", real=True)
c0, c1, d0, d1 = sp.symbols("c0 c1 d0 d1", real=True)
u = sp.Matrix([a0 + I * a1, b0 + I * b1])
v = sp.Matrix([c0 + I * c1, d0 + I * d1])
print("== W  qubit lemmas")
nu, nv = bloch(u), bloch(v)
lhs = sp.simplify(sp.Abs((u.H * v)[0]) ** 2 / ((u.H * u)[0] * (v.H * v)[0]))
rhs = sp.simplify((1 + sum(nu[k] * nv[k] for k in range(3))) / 2)
check("W1", "identity", sp.simplify(sp.expand(sp.expand_complex(lhs - rhs))) == 0,
      "|<u|v>|^2/(|u|^2|v|^2) = (1 + n_u . n_v)/2 (Bloch dictionary)")
nc = bloch(u.conjugate())
check("W2", "identity", all(sp.simplify(nc[k] - [nu[0], -nu[1], nu[2]][k]) == 0 for k in range(3)),
      "complex conjugation acts on Bloch vectors as reflY = diag(1,-1,1) (antiunitary <-> det -1)")
cs, sn = sp.symbols("c s", real=True)
UZ = cs * sp.eye(2) - I * sn * Z
UY = cs * sp.eye(2) - I * sn * Y
nr = sp.symbols("n1:4", real=True)
rho = (sp.eye(2) + nr[0] * X + nr[1] * Y + nr[2] * Z) / 2


def bl(R):
    return [sp.expand((R * S[k]).trace()) for k in (1, 2, 3)]


rz = bl(UZ * rho * UZ.H)
ry = bl(UY * rho * UY.H)
C2, S2 = cs ** 2 - sn ** 2, 2 * cs * sn


def modc(e):
    return sp.rem(sp.expand(e), cs ** 2 + sn ** 2 - 1, cs) == 0


okz = all(modc(rz[k] - [C2 * nr[0] - S2 * nr[1], S2 * nr[0] + C2 * nr[1], nr[2]][k]) for k in range(3))
oky = all(modc(ry[k] - [C2 * nr[0] + S2 * nr[2], nr[1], -S2 * nr[0] + C2 * nr[2]][k]) for k in range(3))
check("W3", "identity", okz and oky, "Ad(cI - isZ) = rotation about z by 2t, Ad(cI - isY) = rotation about y by 2t "
      "(c = cos t, s = sin t); Euler angles then give every rotation as Ad of a unitary")

print("== W4  cross-ratio constancy (diagonal slice maps, phases p0, p1)")
p0, p1 = sp.symbols("p0 p1", nonzero=True)
be = sp.Matrix([b0 + I * b1, c0 + I * c1])


def slice_map(p, eps, b):
    bb = b.conjugate() if eps else b
    return sp.Matrix([bb[0], p * bb[1]])


def kfun(e0, e1, b):
    w0, w1 = slice_map(p0, e0, b), slice_map(p1, e1, b)
    return sp.simplify(w0[0] * w1[1] / (w0[1] * w1[0]))


same = all(sp.simplify(kfun(e, e, be) - p1 / p0) == 0 for e in (0, 1))
bA, bB = sp.Matrix([1, 1]), sp.Matrix([1, I])
mixed = all(sp.simplify(kfun(e0, e1, bA) - kfun(e0, e1, bB)) != 0 for (e0, e1) in ((0, 1), (1, 0)))
check("W4", "exact", same and mixed, "k(b) = p1/p0 is constant when both slices are unitary or both antiunitary; "
      "with mixed types k(1,1) != k(1,i), so a constant cross ratio forces equal types")

print("== W5  the Segre step")
lam, mu = sp.symbols("lam mu")
uu = sp.symbols("u0 u1 u2 u3")
vv = sp.symbols("v0 v1 v2 v3")
Cm = sp.Matrix(2, 2, lambda i, j: lam * uu[i] * vv[j] + mu * uu[2 + i] * vv[2 + j])
check("W5", "identity", sp.expand(Cm.det() - lam * mu * (uu[0] * uu[3] - uu[1] * uu[2]) *
                                  (vv[0] * vv[3] - vv[1] * vv[2])) == 0,
      "det coeff(lam u(x)v + mu u'(x)v') = lam mu det[u u'] det[v v']: a combination of two product vectors with "
      "non-parallel factors is entangled")

print("== W6  an instance of the conclusion, and the countercontrol")
UC = sp.Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
V2 = sp.Matrix([[1, 1], [1, -1]])


def tp(x, y):
    return sp.Abs((x.H * y)[0]) ** 2 / ((x.H * x)[0] * (y.H * y)[0])


vecs = [sp.Matrix([1, 0]), sp.Matrix([1, I]), sp.Matrix([2, 1 - I]), sp.Matrix([1, -3])]
pairs = [(x, y) for x in vecs for y in vecs]
psi = {i: UC * kron(pairs[i][0].conjugate(), V2 * pairs[i][1]) for i in range(len(pairs))}
inst = all(sp.simplify(tp(psi[i], psi[j]) - tp(pairs[i][0], pairs[j][0]) * tp(pairs[i][1], pairs[j][1])) == 0
           for i in range(len(pairs)) for j in range(len(pairs)))
check("W6", "instance", inst, "psi_ab = CNOT(conj(a) (x) H b) preserves all %d transition probabilities" %
      (len(pairs) ** 2))


def nflag(x):
    return 1 if sp.Abs(x[0]) < sp.Abs(x[1]) else 0


def phi(x, y):
    return kron(x, (Z ** nflag(x)) * y)


aa, ab = sp.Matrix([2, 1]), sp.Matrix([1, 2])
bb = sp.Matrix([1, 1])
slice_ok = all(sp.simplify(tp(phi(aa, y1), phi(aa, y2)) - tp(y1, y2)) == 0 for y1 in vecs for y2 in vecs)
glob = sp.simplify(tp(phi(aa, bb), phi(ab, bb)) - tp(aa, ab) * tp(bb, bb))
check("W6c", "countercontrol", slice_ok and glob != 0,
      "psi_ab = a (x) Z^[|a0|<|a1|] b preserves each slice but not the global identity (defect %s): the "
      "all-pairs hypothesis is load-bearing" % glob)

print("== O  U2(c): from transition probabilities to the cone")
SS = [[kron(S[m], S[n]) for n in range(4)] for m in range(4)]


def table(R):
    return sp.Matrix(4, 4, lambda m, n: sp.expand((R * SS[m][n]).trace()))


def pauliW(w):
    R = sp.zeros(4, 4)
    for m in range(4):
        for n in range(4):
            R += w[m, n] * SS[m][n]
    return R / 4


axes = []
for k in range(3):
    for sg in (1, -1):
        e = [0, 0, 0]
        e[k] = sg
        axes.append(e)
rows = []
for x in axes:
    for y in axes:
        hx, hy = [1] + x, [1] + y
        rows.append([hx[m] * hy[n] for m in range(4) for n in range(4)])
check("O1", "exact", sp.Matrix(rows).rank() == 16,
      "the 36 axis products span W 3 (rank 16): linear maps agreeing on pure products agree everywhere")
wsym = sp.Matrix(4, 4, lambda m, n: sp.Symbol("w%d%d" % (m, n), real=True))


def ptrans2(M):
    return sp.Matrix(4, 4, lambda r, c: M[2 * (r // 2) + (c % 2), 2 * (c // 2) + (r % 2)])


actTy = sp.Matrix(4, 4, lambda m, n: wsym[m, n] * (-1 if n == 2 else 1))
check("O2", "identity", sp.expand(table(ptrans2(pauliW(wsym))) - actTy) == sp.zeros(4, 4),
      "actT reflY = partial transpose on token 1 (so twin = PT(Q3); actC reflY = PT on token 0 = T o actT reflY)")
idW = sp.eye(4)
chainW = sp.Matrix([[1, 0, 0, 1], [1, 0, 0, -1], [0, 0, 0, 0], [0, 0, 0, 0]])
phiW = sp.diag(1, 1, -1, 1)
Rphi = pauliW(phiW)
val = sum(([1, -1, 0, 0])[m] * chainW[m, n] * ([1, 0, 0, -1])[n] for m in range(4) for n in range(4))
check("O3", "exact", actTy.subs({wsym[m, n]: idW[m, n] for m in range(4) for n in range(4)}) == phiW and
      Rphi * Rphi == Rphi and Rphi.trace() == 1 and val < 0,
      "idW = actT reflY phiW ∈ twin (phiW pure), cnot idW = chainW [K K2Guard:101-104], and chainW pairs to %s with "
      "the product a = -e1, b = -e3: twin is not cnot-invariant" % val)

print()
nfail = RES.count(False)
print("checks: %d, failed: %d" % (len(RES), nfail))
print("VERDICT " + ("U2-LEMMAS-EXACT" if nfail == 0 else "U2-LEMMAS-FAILED") + " -- %d checks" % len(RES))
