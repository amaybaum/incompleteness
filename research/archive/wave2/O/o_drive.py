"""Thread O (DRIVE) -- exact checks.

Exact arithmetic only: sympy symbolic trigonometry, rationals, exact radicals. No floats.
Run:  PYTHONDONTWRITEBYTECODE=1 python3 o_drive.py
Every check prints PASS/FAIL; the last line is `OK -- N checks, 0 failed` or a failure count.

Conventions.  Pauli X, Y, Z.  The Bloch image of a unitary U is the 3x3 real matrix
    R(U)_{ij} = (1/2) tr(s_i U s_j U^dagger),   s = (X, Y, Z),
so that U rho U^dagger has Bloch vector R(U) r when rho = (1 + r.s)/2.
"""
from sympy import (Matrix, I, pi, exp, cos, sin, Rational, symbols, simplify, eye, zeros,
                   expand, sqrt, nsimplify, trigsimp, expand_complex, re, im)

checks = []


def check(name, cond):
    ok = bool(cond)
    checks.append((name, ok))
    print(("PASS " if ok else "FAIL ") + name)


def zero(M):
    M = Matrix(M)
    return all(simplify(expand_complex(trigsimp(expand_complex(e)))) == 0 for e in M)


X = Matrix([[0, 1], [1, 0]])
Y = Matrix([[0, -I], [I, 0]])
Z = Matrix([[1, 0], [0, -1]])
SIG = [X, Y, Z]


def bloch(U):
    Ud = U.H
    R = zeros(3, 3)
    for i in range(3):
        for j in range(3):
            R[i, j] = simplify(expand_complex((SIG[i] * U * SIG[j] * Ud).trace() / 2))
    return R


def Rx(a):
    return Matrix([[1, 0, 0], [0, cos(a), -sin(a)], [0, sin(a), cos(a)]])


def Ry(a):
    return Matrix([[cos(a), 0, sin(a)], [0, 1, 0], [-sin(a), 0, cos(a)]])


def Rz(a):
    return Matrix([[cos(a), -sin(a), 0], [sin(a), cos(a), 0], [0, 0, 1]])


t, s, phi, th = symbols('t s phi theta', real=True)

# ---------------------------------------------------------------------------------------
# A. The CT2 gate flow (LiftAudit.gateFlow = SecondOrderCircuit.unit (permMat swap) t)
# ---------------------------------------------------------------------------------------
p = (eye(2) - X) / 2                      # proj g = (1 - g)/2, SecondOrderCircuit:351


def unit(tt, k=0):
    return eye(2) + (exp(pi * I * (2 * k + 1) * tt) - 1) * p


G = unit(t)
check("A1 gateFlow(t) unitary (symbolic t)", zero(G.H * G - eye(2)))
check("A2 gateFlow group law gateFlow(s) gateFlow(t) = gateFlow(s+t)", zero(unit(s) * unit(t) - unit(s + t)))
check("A3 gateFlow(1) = X (the substratum's visible swap)", zero(unit(1) - X))
Gh = unit(Rational(1, 2))
check("A4 gateFlow(1/2) entries (1+i)/2, (1-i)/2: two nonzero entries in a column (non-monomial)",
      simplify(Gh[0, 0] - (1 + I) / 2) == 0 and simplify(Gh[1, 0] - (1 - I) / 2) == 0)
BG = bloch(G)
check("A5 Bloch(gateFlow(t)) = Rx(pi t)  (symbolic t)", zero(BG - Rx(pi * t)))
check("A6 Bloch(X) = diag(1,-1,-1) = Rx(pi)", zero(bloch(X) - Rx(pi)))
for k in (1, 2, -1):
    check(f"A7 branch k={k}: unit_k(1) = X and Bloch(unit_k(t)) = Rx((2k+1) pi t)  (drive not unique)",
          zero(unit(1, k) - X) and zero(bloch(unit(t, k)) - Rx((2 * k + 1) * pi * t)))

# ---------------------------------------------------------------------------------------
# B. Phases and the off-axis clause D9 (KF:275 J_off_axis) for monomial J on Fin 2
# ---------------------------------------------------------------------------------------
Dphi = Matrix([[1, 0], [0, exp(I * phi)]])
BD = bloch(Dphi)
check("B1 Bloch(diag(1,e^{i phi})) = Rz(phi): D X D^dagger = cos(phi) X + sin(phi) Y", zero(BD - Rz(phi)))
S = Matrix([[1, 0], [0, I]])                # LieRankSource.phaseGate on the second state
check("B2 quarter phase acts as Rz(pi/2)", zero(bloch(S) - Rz(pi / 2)))
ex = Matrix([1, 0, 0])
# J Rx(t) J^{-1} e_x - e_x for J = Rz(-phi): every flow member Rx(s) fixes e_x.
v = (BD * Rx(t) * BD.T) * ex - ex
vs = [simplify(trigsimp(e)) for e in v]
# at t = pi/2 the displacement is (-(sin phi)^2, -sin phi cos phi, -sin phi)-type; vanishes iff sin phi = 0
vh = [simplify(e.subs(t, pi / 2)) for e in v]
check("B3 J=diag(1,e^{i phi}): J Rx(pi/2) J^-1 moves e_x exactly when sin(phi) != 0 (third coord = +-sin phi)",
      simplify(vh[2] ** 2 - sin(phi) ** 2) == 0 and all(simplify(e.subs(phi, 0)) == 0 for e in vh)
      and all(simplify(e.subs(phi, pi)) == 0 for e in vh))
# with J = X * diag(1, e^{i phi}) (the other monomial unitaries)
BXD = bloch(X * Dphi)
w = (BXD * Rx(t) * BXD.T) * ex - ex
wh = [simplify(e.subs(t, pi / 2)) for e in w]
check("B4 J=X diag(1,e^{i phi}): same criterion, D9 iff sin(phi) != 0",
      simplify(wh[2] ** 2 - sin(phi) ** 2) == 0 and all(simplify(e.subs(phi, 0)) == 0 for e in wh)
      and all(simplify(e.subs(phi, pi)) == 0 for e in wh))
# real monomials (phi in {0, pi}) normalize the flow: J Rx(t) J^-1 = Rx(+-t)
for name, J in (("Z", Z), ("X", X), ("XZ", X * Z), ("1", eye(2))):
    BJ = bloch(J)
    c1 = zero(BJ * Rx(t) * BJ.T - Rx(t))
    c2 = zero(BJ * Rx(t) * BJ.T - Rx(-t))
    check(f"B5 real monomial J={name}: J Rx(t) J^-1 is the flow member Rx(+-t) (D9 fails)", c1 or c2)
BS = bloch(S)
check("B6 quarter phase: S Rx(t) S^-1 = Ry(-t)-type rotation (not a flow member: moves e_x at t=pi/2)",
      zero(BS * Rx(t) * BS.T - Ry(t)) or zero(BS * Rx(t) * BS.T - Ry(-t)))
check("B7 ... and Ry(pi/2) e_x != e_x", Ry(pi / 2) * ex != ex)

# ---------------------------------------------------------------------------------------
# C. The real pair flow (RealPairFlow.PairFlow, rotFlow) and the NOT alignment
# ---------------------------------------------------------------------------------------
rot = Matrix([[cos(th), -sin(th)], [sin(th), cos(th)]])   # StateMixingCoupling.rot, rotR
Brot = bloch(rot)
check("C1 Bloch(rot theta) = Ry(-2 theta)-type rotation about y", zero(Brot - Ry(-2 * th)) or zero(Brot - Ry(2 * th)))
Nr = rot.subs(th, pi / 2)
check("C2 rot(pi/2) = [[0,-1],[1,0]] is monomial (signed permutation), maps |0> to |1>",
      Nr == Matrix([[0, -1], [1, 0]]))
check("C3 Bloch(rot(pi/2)) = diag(-1,1,-1) != Bloch(X) = diag(1,-1,-1): pair-flow NOT is not the visible swap off the z-axis",
      zero(bloch(Nr) - Matrix([[-1, 0, 0], [0, 1, 0], [0, 0, -1]])) and bloch(Nr) != bloch(X))
check("C4 both agree on the classical pair: z -> -z", bloch(Nr)[2, 2] == -1 and bloch(X)[2, 2] == -1)

# Rebit: real symmetric states, Bloch disk in (x, z). Real orthogonal ops act in O(2) on (x, z).
def disk(U):
    B = bloch(U)
    return Matrix([[B[0, 0], B[0, 2]], [B[2, 0], B[2, 2]]])


def R2(a):
    return Matrix([[cos(a), -sin(a)], [sin(a), cos(a)]])


Fx = Matrix([[1, 0], [0, -1]])
check("C5 rebit: rot theta acts on the (x,z) disk as a rotation by +-2 theta",
      zero(disk(rot) - R2(2 * th)) or zero(disk(rot) - R2(-2 * th)))
check("C6 rebit: real monomials act on the disk as O(2) elements (X: (x,z)->(x,-z); Z: (x,z)->(-x,z))",
      zero(disk(X) - Fx) and zero(disk(Z) + Fx))
a = symbols('a', real=True)
check("C7 rebit: every reflection F conjugates the rotation flow to its inverse, F R(a) F^-1 = R(-a); "
      "rotations commute with it  => D9 fails for every J in O(2)",
      zero(Fx * R2(a) * Fx - R2(-a)) and zero(R2(s) * R2(a) * R2(-s) - R2(a))
      and zero((R2(s) * Fx) * R2(a) * (R2(s) * Fx).inv() - R2(-a)))

# ---------------------------------------------------------------------------------------
# D. The ones-fixing theory (FlowEndpoint.onesTheory): flow without an off-axis J
# ---------------------------------------------------------------------------------------
u = symbols('u', real=True)
b = (1 - u ** 2 + 2 * I * u) / (1 + u ** 2)          # |b| = 1, rational parametrization
Pp = Matrix([[1, 1], [1, 1]]) / 2
Pm = Matrix([[1, -1], [-1, 1]]) / 2
W = Pp + b * Pm                                       # general unitary fixing (1,1)^T, up to the dense u-chart
check("D1 W = P+ + b P- is unitary and fixes the all-ones vector",
      zero(W.H * W - eye(2)) and zero(W * Matrix([1, 1]) - Matrix([1, 1])))
BW = bloch(W)
check("D2 Bloch(W) fixes e_x (ones ray = Bloch +x point)", zero(BW * ex - ex))
check("D3 Bloch(W) commutes with the gate-flow image Rx(t): no ones-fixing J satisfies D9",
      zero(BW * Rx(t) - Rx(t) * BW))
check("D4 the gate flow itself is ones-fixing (InstrumentRealization.gateFlow_mulVec_ones)",
      zero(G * Matrix([1, 1]) - Matrix([1, 1])))
check("D5 the quarter phase is not ones-fixing (PhaseSource.phaseGate_moves_ones)",
      S * Matrix([1, 1]) != Matrix([1, 1]))

# ---------------------------------------------------------------------------------------
# E. The ambient l^inf(E) typing: the induced dual action is not norm-continuous
# ---------------------------------------------------------------------------------------
# Effect e0 = (1+Z)/2 has Bloch vector (0,0,1). A rotation about x by angle th_n with
# tan(th_n/2) = 1/n is rational: cos = (n^2-1)/(n^2+1), sin = 2n/(n^2+1). It tends to the identity,
# yet it moves e0, so for f = indicator of {e0} in l^inf(E), ||g_n.f - f||_inf = 1 for every n.
allmove = True
for n in range(1, 61):
    c = Rational(n * n - 1, n * n + 1)
    sn = Rational(2 * n, n * n + 1)
    Rn = Matrix([[1, 0, 0], [0, c, -sn], [0, sn, c]])
    img = Rn * Matrix([0, 0, 1])
    if img == Matrix([0, 0, 1]):
        allmove = False
    if not (Rn.T * Rn == eye(3) and Rn.det() == 1):
        allmove = False
check("E1 rational rotations R_n -> id (n=1..60) each move the effect e0: the indicator of {e0} is "
      "displaced by 1 in sup norm, so the induced action on l^inf(E) violates flow_continuous", allmove)
n = 60
c = Rational(n * n - 1, n * n + 1)
check("E2 ... while ||R_60 - 1|| entries are O(1/n): 1 - cos = 2/(n^2+1)", 1 - c == Rational(2, n * n + 1))

# ---------------------------------------------------------------------------------------
# F. Drive in dimension 4 (DRIVE does not import DIM3): Rz (+) 1 with J = cyc3 (+) 1
# ---------------------------------------------------------------------------------------
def blk(M):
    B = zeros(4, 4)
    B[:3, :3] = M
    B[3, 3] = 1
    return B


cyc = Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])     # KF cyc3: (x,y,z) -> (z,x,y)
F4 = blk(Rz(t))
J4 = blk(cyc)
check("F1 B^4 drive: flow orthogonal, group law, N = flow(pi) involutive and moves e_1",
      zero(F4.T * F4 - eye(4)) and zero(blk(Rz(s)) * blk(Rz(t)) - blk(Rz(s + t)))
      and zero(blk(Rz(pi)) * blk(Rz(pi)) - eye(4)) and blk(Rz(pi)) * Matrix([1, 0, 0, 0]) != Matrix([1, 0, 0, 0]))
e3 = Matrix([0, 0, 1, 0])
conj = J4 * blk(Rz(pi / 2)) * J4.T
check("F2 B^4 drive: J flow(pi/2) J^-1 moves e_3 (= e_z), every flow member fixes e_3 (D9 holds)",
      conj * e3 != e3 and all(zero(blk(Rz(s)) * e3 - e3) for _ in [0]))
check("F3 B^4 drive: every generator fixes e_4, so the drive group is not boundary-transitive (K 3.11)",
      F4 * Matrix([0, 0, 0, 1]) == Matrix([0, 0, 0, 1]) and J4 * Matrix([0, 0, 0, 1]) == Matrix([0, 0, 0, 1]))

# ---------------------------------------------------------------------------------------
# G. Qubit assembly (consistency control): gate flow + quarter phase is a drive on ball3
# ---------------------------------------------------------------------------------------
check("G1 qubit: N = Bloch(gateFlow(1)) involutive, moves e_z", zero(Rx(pi) * Rx(pi) - eye(3)) and Rx(pi) * Matrix([0, 0, 1]) != Matrix([0, 0, 1]))
check("G2 qubit: J = Bloch(S) satisfies D9 against the gate flow (B6 + B7)", True and Ry(pi / 2) * ex != ex)
# The drive group <Rx, Rz(pi/2)> contains Ry(t) = Rz(pi/2) Rx(t) Rz(-pi/2) up to sign; Euler words reach e_z -> any b.
check("G3 qubit: Rz(-pi/2) Rx(t) Rz(pi/2) is a rotation about the y-axis",
      zero(Rz(-pi / 2) * Rx(t) * Rz(pi / 2) - Ry(t)) or zero(Rz(-pi / 2) * Rx(t) * Rz(pi / 2) - Ry(-t)))

# ---------------------------------------------------------------------------------------
# H. Toy: a composite of two non-commuting involution flows is a path, not a group
#    (SecondOrderDrive header: driveQ is a continuous path; no group law is claimed)
# ---------------------------------------------------------------------------------------
def unitg(g, tt):
    return eye(2) + (exp(pi * I * tt) - 1) * (eye(2) - g) / 2


def comp(tt):
    return unitg(Z, tt) * unitg(X, tt)        # second layer after the first, toy involutions X, Z


lhs = comp(Rational(1, 2)) * comp(Rational(1, 2))
rhs = comp(1)
# compare as conjugation channels: proportional up to a unit scalar?
ratio_ok = False
for (i, j) in ((0, 0), (0, 1), (1, 0), (1, 1)):
    if simplify(rhs[i, j]) != 0:
        lam = simplify(lhs[i, j] / rhs[i, j])
        ratio_ok = zero(lhs - lam * rhs)
        break
check("H1 toy: D(t) = U_Z(t) U_X(t) has D(1/2)^2 not proportional to D(1) (no group law for the composite)",
      not ratio_ok)
check("H2 toy: D(1) = Z X, the composite of the two involutions (endpoint is the update)", zero(rhs - Z * X))

# ---------------------------------------------------------------------------------------
# I. Relocating the continuum: under SubstratumAvail (every diagonal unitary available),
#    ONE fixed gate gives the whole gate flow.  gateFlow(levelPerm swap n, t)
#      = M (D_t (x) 1_n) M^7,  M = mixImage n (pi/4) = rot(pi/4) (x) 1_n,  D_t = diag(1, e^{i pi t}),
#    and likewise with the Hadamard image H (x) 1_n (C5Discovery.siteSwapImage n).
# ---------------------------------------------------------------------------------------
def kron(A, B):
    r, c = A.shape
    rb, cb = B.shape
    K = zeros(r * rb, c * cb)
    for i in range(r):
        for j in range(c):
            for k in range(rb):
                for l in range(cb):
                    K[i * rb + k, j * cb + l] = A[i, j] * B[k, l]
    return K


Mq = rot.subs(th, pi / 4)
check("I0 rot(pi/4)^8 = 1 and rot(pi/4)^7 = rot(-pi/4) = rot(pi/4)^dagger (inverse is a word in the gate)",
      zero(Mq ** 8 - eye(2)) and zero(Mq ** 7 - rot.subs(th, -pi / 4)) and zero(Mq ** 7 - Mq.H))
Dt = Matrix([[1, 0], [0, exp(I * pi * t)]])
hc = 1 / sqrt(2)
Had = Matrix([[hc, hc], [hc, -hc]])               # C5Discovery.hadamard
for nn in (1, 2, 3):
    one = eye(nn)
    Xn = kron(X, one)
    GF = eye(2 * nn) + (exp(pi * I * t) - 1) * (eye(2 * nn) - Xn) / 2     # gateFlow (levelPerm swap n) t
    Mn = kron(Mq, one)
    Hn = kron(Had, one)
    Dn = kron(Dt, one)
    check(f"I1 level n={nn}: gateFlow(t) = M D_t M^7 with M = mixImage n (pi/4)  (symbolic t)",
          zero(GF - Mn * Dn * Mn ** 7))
    check(f"I2 level n={nn}: gateFlow(t) = H D_t H with H = siteSwapImage n  (symbolic t)",
          zero(GF - Hn * Dn * Hn))
check("I3 the fixed gate rot(pi/4) is a Clifford angle: Bloch(rot(pi/4)) maps e_z to +-e_x",
      bloch(Mq) * Matrix([0, 0, 1]) in (Matrix([1, 0, 0]), Matrix([-1, 0, 0])))


# Lie rank: span_R{ iZ, i J Z J^dagger, [iZ, i J Z J^dagger] } inside su(2), exact over Q(i).
def lie_dim(J):
    A = I * Z
    B = I * (J * Z * J.H)
    C = A * B - B * A
    rows = []
    for Mx in (A, B, C):
        vec = []
        for e in Mx:
            e = nsimplify(expand_complex(e))
            vec += [re(e), im(e)]
        rows.append(vec)
    return Matrix(rows).rank(simplify=True)


Jc = Matrix([[Rational(3, 5), Rational(-4, 5)], [Rational(4, 5), Rational(3, 5)]])  # rational rotation, non-monomial
Jc2 = Matrix([[Rational(3, 5), Rational(4, 5) * I], [Rational(4, 5) * I, Rational(3, 5)]])
check("I4 a generic fixed non-monomial gate (Cayley rotation 3/5,4/5) with the phase generator iZ spans su(2) (rank 3)",
      lie_dim(Jc) == 3)
check("I5 ... also for a complex non-monomial gate [[3/5, 4i/5],[4i/5, 3/5]] (rank 3)", lie_dim(Jc2) == 3)
check("I6 control: every monomial J (X, diag(1,i), X diag(1,i)) gives rank 1 (J Z J^dagger = +-Z)",
      lie_dim(X) == 1 and lie_dim(S) == 1 and lie_dim(X * S) == 1)

nf = sum(1 for _, ok in checks if not ok)
print(f"OK -- {len(checks)} checks, {nf} failed" if nf == 0 else f"FAILED -- {nf} of {len(checks)} checks failed")
