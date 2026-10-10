"""u1_kstar_cc.py -- thread U: countercontrols for the surgery construction, and the level-(ii) group.

Decision rule (fixed before the first run):
- PASS/FAIL per check. A countercontrol PASSES only when the deliberately altered construction FAILS the property
  that the construction K* = (Q3 ∩ E0*) + R+ E0 has (self-duality, cnot-invariance).
- `VERDICT KSTAR-CONTROLS-EXACT` prints only if every check passes; else `VERDICT KSTAR-CONTROLS-FAILED`.
- Exact arithmetic only.
Sections:
  C1 the projection lemma is load-bearing: z = (psi psi^H)^Gamma (psi = 2|00> + |11>) is in maxCone with one negative
     eigenvalue, but a cap state's projection is not PSD, so K_z = (Q3 ∩ z*) + R+ z is NOT self-dual;
  C2 cnot-invariance of the surgery vector is load-bearing: for z = Y1 = E00 + E13 + E22 (= E0's partial transpose)
     and for z = F, the cone K_z contains z but not cnot z;
  C3 the level-(ii) group: the 8 (even, even) gates G(D, D', R0) = actC D o cnot o actC D' o actT R0 satisfy the
     landed frame, relT and relC clauses exactly; they generate a group of order 16 containing actC diag(-1,-1,1);
     <E0, actC diag(-1,-1,1) E0> = -1, so no level-(ii) cone contains E0 and K* is not level-(ii) invariant.
"""
import itertools
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


def Eunit(m, n):
    E = sp.zeros(4, 4)
    E[m, n] = 1
    return E


def homMap(N):
    H = sp.zeros(4, 4)
    H[0, 0] = 1
    H[1:4, 1:4] = N
    return H


def actC(N, w):
    return homMap(N) * w


def actT(N, w):
    return w * homMap(N).T


RES = []


def check(cid, kind, ok, detail=""):
    ok = bool(ok)
    RES.append(ok)
    print(("PASS " if ok else "FAIL ") + cid + "  [" + kind + "] " + detail)


E00 = Eunit(0, 0)
E0 = E00 + Eunit(1, 3) - Eunit(2, 2)

print("== C1  PL is load-bearing: z = (psi psi^H)^Gamma, psi = 2|00> + |11>")
Wz = sp.Matrix([[4, 0, 0, 0], [0, 0, 2, 0], [0, 2, 0, 0], [0, 0, 0, 1]])   # partial transpose on token 1
z = table(Wz)
check("C1a", "exact", sp.Matrix(sorted(Wz.eigenvals().keys())) == sp.Matrix([-2, 1, 2, 4]),
      "spectrum of (psi psi^H)^Gamma is {-2, 1, 2, 4}: one negative eigenvalue (like E0)")
xs = sp.symbols("x1:4", real=True)
ys = sp.symbols("y1:4", real=True)
xm = (sp.eye(2) + xs[0] * S[1] + xs[1] * S[2] + xs[2] * S[3]) / 2
yb = (sp.eye(2) + ys[0] * S[1] - ys[1] * S[2] + ys[2] * S[3]) / 2          # transpose of rho(y)
pr = sp.Matrix([2, 0, 0, 1])
val = sp.expand((pr.H * kron(xm, yb) * pr)[0])
check("C1b", "identity", sp.expand(ipW(table(kron(xm, (sp.eye(2) + ys[0] * S[1] + ys[1] * S[2] + ys[2] * S[3]) / 2)),
                                       z) - 4 * val) == 0,
      "<prodState x y, z> = 4 <psi| rho(x) (x) rho(y)^T |psi> >= 0, so z ∈ maxCone (H1 holds for K_z)")
psp = sp.Matrix([0, 1, -1, 1])
Bz = (psp.H * Wz * psp)[0]
nz = (Wz * Wz).trace()
rho_pp = psp * psp.H - (Bz / nz) * Wz
check("C1c", "exact", Bz < 0 and rho_pp.det() < 0,
      "cap state psi' = |01> - |10> + |11>: <psi'|W|psi'> = %s < 0, det(projection) = %s < 0 (not PSD)" %
      (Bz, rho_pp.det()))
yv = table(rho_pp)
check("C1d", "countercontrol", ipW(yv, z) == 0,
      "y := Pi(q) lies in (Q3 + R+ z) ∩ z-perp ⊆ K_z*, and <y, z> = 0 forces y ∈ K_z ⇒ y ∈ Q3; y ∉ Q3 (C1c), "
      "so K_z ≠ K_z*: the surgery is NOT self-dual without PL")

print("== C2  cnot-invariance of the surgery vector is load-bearing for H2")
Y1 = E00 + Eunit(1, 3) + Eunit(2, 2)
check("C2a", "exact", cnot(Y1) != Y1 and ipW(Y1, cnot(Y1)) == -1 and table(pauliW(Y1)) == Y1,
      "Y1 = E00 + E13 + E22 (E0 with the YY sign flipped): <Y1, cnot Y1> = -1 < 0, so the self-positive cone "
      "K_Y1 = (Q3 ∩ Y1*) + R+ Y1 contains Y1 but not cnot Y1")
RH = sp.Matrix([[0, 0, 1], [0, -1, 0], [1, 0, 0]])
phiW = sp.diag(1, 1, -1, 1)
Tpsi = actT(RH, phiW)
F = E00 / 2 - Tpsi / 4
g3 = sp.Matrix([1, 1, -1, 1]) / 2
Pe3 = table(g3 * g3.T)
check("C2b", "exact", Tpsi == E00 + Eunit(1, 3) + Eunit(2, 2) + Eunit(3, 1) and ipW(Pe3, F) == sp.Rational(1, 2)
      and ipW(Pe3, cnot(F)) == sp.Rational(-1, 2),
      "T_psi = E00+E13+E22+E31; P = |e3><e3| has <P, F> = 1/2 (P ∈ Q3 ∩ F* ⊆ K_F) and <P, cnot F> = -1/2, "
      "so cnot F ∉ K_F: K_F is not cnot-invariant")
check("C2c", "exact", cnot(E0) == E0 and ipW(E0, cnot(E0)) == 3,
      "control: the actual surgery vector E0 is cnot-fixed (<E0, cnot E0> = 3 >= 0)")

print("== C3  the level-(ii) group: (even, even) native gates and their closure")
N = sp.diag(1, -1, -1)                       # nflip
z3 = [0, 0, 1]
diag3 = [sp.diag(s1, s2, 1) for s1 in (1, -1) for s2 in (1, -1)]


def mat(f):
    M = sp.zeros(16, 16)
    for j in range(16):
        e = sp.zeros(4, 4)
        e[j // 4, j % 4] = 1
        r = f(e)
        for i in range(16):
            M[i, j] = r[i // 4, i % 4]
    return M


Cm = mat(cnot)
TN, CN = mat(lambda w: actT(N, w)), mat(lambda w: actC(N, w))


def prodS(x, y):
    hx, hy = [1] + list(x), [1] + list(y)
    return sp.Matrix(4, 4, lambda m, n: hx[m] * hy[n])


def vec(w):
    return sp.Matrix([w[i // 4, i % 4] for i in range(16)])


corner = {0: z3, 1: [0, 0, -1]}
gates = []
for D in (sp.eye(3), sp.diag(-1, -1, 1)):
    for Dp in diag3:
        for R0 in diag3:
            if Dp.det() * R0.det() != 1:
                continue
            Gm = mat(lambda w, D=D, Dp=Dp, R0=R0: actC(D, cnot(actC(Dp, actT(R0, w)))))
            frame = all(Gm * vec(prodS(corner[a], corner[b])) == vec(prodS(corner[a], corner[(a + b) % 2]))
                        for a in (0, 1) for b in (0, 1))
            relT = TN * Gm * TN == Gm
            relC = CN * Gm * CN == TN * Gm
            gates.append((Gm, frame and relT and relC))
distinct = []
for Gm, ok in gates:
    if all(Gm != H for H in distinct):
        distinct.append(Gm)
check("G1", "exact", all(ok for _, ok in gates),
      "all %d (even, even) dressings satisfy the landed frame, relT, relC clauses (N = nflip, z = z3); "
      "distinct gates: %d" % (len(gates), len(distinct)))
group = [sp.eye(16)]
frontier = [sp.eye(16)]
while frontier:
    new = []
    for A in frontier:
        for Gm in distinct:
            B = Gm * A
            if all(B != H for H in group):
                group.append(B)
                new.append(B)
    frontier = new
Zc = mat(lambda w: actC(sp.diag(-1, -1, 1), w))
Zt = mat(lambda w: actT(sp.diag(-1, -1, 1), w))
Tg = mat(lambda w: actC(sp.diag(1, -1, 1), actT(sp.diag(1, -1, 1), w)))
check("G2", "exact", len(group) == 16 and any(Zc == H for H in group) and any(Zt == H for H in group)
      and any(Tg == H for H in group) and any(Cm == H for H in group),
      "the even native class generates a group of order %d containing cnot, Z_c = actC diag(-1,-1,1), "
      "Z_t = actT diag(-1,-1,1) and the global transpose" % len(group))
ZcE0 = actC(sp.diag(-1, -1, 1), E0)
check("G3", "exact", ipW(E0, ZcE0) == -1,
      "<E0, Z_c E0> = -1: no level-(ii) cone contains E0 (it would contain Z_c E0 and pair negatively), "
      "and K* is not level-(ii) invariant")
fix = (sp.Matrix.vstack(*[H - sp.eye(16) for H in group])).nullspace()
diag_ok = all(sp.simplify(pauliW(sp.Matrix(4, 4, list(v))) - sp.diag(*[pauliW(sp.Matrix(4, 4, list(v)))[i, i]
                                                                      for i in range(4)])) == sp.zeros(4, 4)
              for v in fix)
check("G4", "exact", len(fix) == 3 and diag_ok,
      "the level-(ii) fixed space has dimension %d and consists of computational-basis-diagonal tables, whose "
      "maxCone members are PSD: a single fixed surgery vector cannot leave Q3" % len(fix))

print()
nfail = RES.count(False)
print("checks: %d, failed: %d" % (len(RES), nfail))
print("VERDICT " + ("KSTAR-CONTROLS-EXACT" if nfail == 0 else "KSTAR-CONTROLS-FAILED") + " -- %d checks" % len(RES))
