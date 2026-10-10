"""Coordinator's independent check of thread D's key claims (audit; exact arithmetic; no thread code used).

Definitions re-typed from the landed sources (CompositeDimension.lean: sgn/pc/pt/cnotFun :741-759, hom :100,
homMap :112, prodState :161, actT :198, actC :201, phiW :1220; K2Guard.lean: reflY :46, idW :101) and from the
normalized family G(a, b) as defined in prose in thread D's RESULT.md §1 (notation paragraph):
  G(hom z3 (x) Y) = hom z3 (x) Y;  G(hom(-z3) (x) Y) = hom(-z3) (x) HN Y;
  G(e_j (x) Y) = sum_{i=1,2} e_i (x) (a_ij S Y + b_ij T Y),
  HN = diag(1,1,-1,-1), S Y = (Y1, Y0, 0, 0), T Y = (0, 0, -Y3, Y2), J' = [[0,-1],[1,0]];
  u (x) Y is the table u Y^T (control index first). The four control vectors hom z3, hom(-z3), e_1, e_2 form a basis.

DECISION RULE (fixed before the first run). Each check prints CONFIRMED or MISMATCH; countercontrols (ids ending
in 'c') are CONFIRMED exactly when the mutated object gives the opposite verdict. 'AUDIT-D ALL CONFIRMED' is
printed iff every check is CONFIRMED. No timing in stdout.
"""
import sympy as sp
from itertools import product

Q = sp.Rational
R4 = range(4)
ok_all = True


def report(cid, ok, detail):
    global ok_all
    ok = bool(ok)
    ok_all = ok_all and ok
    print(f"{'CONFIRMED' if ok else 'MISMATCH '} {cid}: {detail}", flush=True)


def section(t):
    print(f"\n== {t}", flush=True)


PC = [[0, 0, 3, 3], [1, 1, 2, 2], [2, 2, 1, 1], [3, 3, 0, 0]]
PT = [[0, 1, 2, 3], [1, 0, 3, 2], [1, 0, 3, 2], [0, 1, 2, 3]]


def sgn(m, n):
    return -1 if (m, n) in ((1, 3), (2, 2)) else 1


def cnot(w):
    return sp.Matrix(4, 4, lambda m, n: sgn(m, n) * w[PC[m][n], PT[m][n]])


def hom(x):
    return sp.Matrix([1] + list(x))


def homMap(Rm):
    M = sp.zeros(4, 4)
    M[0, 0] = 1
    M[1:4, 1:4] = Rm
    return M


def actT(Rm, w):
    return w * homMap(Rm).T


def actC(Rm, w):
    return homMap(Rm) * w


def prodState(x, y):
    return hom(x) * hom(y).T


def ipW(E, X):
    return sp.expand(sum(E[m, n] * X[m, n] for m in R4 for n in R4))


def zero4(M):
    return all(sp.expand(M[i, j]) == 0 for i in R4 for j in R4)


reflY = sp.diag(1, -1, 1)
phiW = sp.diag(1, 1, -1, 1)
idW = sp.eye(4)
xplus, z3, mz3 = [1, 0, 0], [0, 0, 1], [0, 0, -1]
HN = sp.diag(1, 1, -1, -1)
Jp = sp.Matrix([[0, -1], [1, 0]])
I2 = sp.eye(2)


def S_(Y):
    return sp.Matrix([Y[1], Y[0], 0, 0])


def T_(Y):
    return sp.Matrix([0, 0, -Y[3], Y[2]])


cz, cmz = hom(z3), hom(mz3)
e1 = sp.Matrix([0, 1, 0, 0])
e2 = sp.Matrix([0, 0, 1, 0])
BASIS = sp.Matrix.hstack(cz, cmz, e1, e2)  # columns: control basis


def G(a, b, w):
    """Apply G(a, b) to a table w by expanding the control index in the basis (hom z3, hom -z3, e1, e2)."""
    coeffs = BASIS.inv() * w  # row k of coeffs = the column-vector Y_k paired with basis control vector k
    out = sp.zeros(4, 4)
    Yz, Ymz, Y1, Y2 = [coeffs[k, :].T for k in range(4)]
    out += cz * Yz.T
    out += cmz * (HN * Ymz).T
    for j, Yj in ((0, Y1), (1, Y2)):
        for i, ei in ((0, e1), (1, e2)):
            out += ei * (a[i, j] * S_(Yj) + b[i, j] * T_(Yj)).T
    return out


ws = sp.Matrix(4, 4, sp.symbols('w0:16', real=True))

# ---------------------------------------------------------------- F: the family
section('F  the normalized family G(a, b)')
report('F1', zero4(G(I2, Jp, ws) - cnot(ws)), 'G(I, J\') = landed cnot (symbolic table)')
a11, a12, a21, a22, b11, b12, b21, b22 = sp.symbols('a11 a12 a21 a22 b11 b12 b21 b22')
A = sp.Matrix([[a11, a12], [a21, a22]])
B = sp.Matrix([[b11, b12], [b21, b22]])
comp = G(A.inv(), -B.inv(), G(A, B, ws))
report('F2', zero4(sp.simplify(comp - ws)), 'G(a^-1, -b^-1) . G(a, b) = id (symbolic invertible a, b)')
report('F3', zero4(G(A, A * Jp, ws) - actC(sp.diag(A, 1), G(I2, Jp, ws)))
       and zero4(G(A, -A * Jp, ws) - actC(sp.diag(A, 1), G(I2, -Jp, ws)))
       and zero4(G(I2, -Jp, ws) - actC(reflY, cnot(actC(reflY, ws)))),
       'G(a, +-a J\') = actC(diag(a, 1)) . G(I, +-J\') (symbolic a) and G(I, -J\') = actC reflY . cnot . actC reflY')

# ---------------------------------------------------------------- P: the positivity steps
section('P  the bounds and the mixing step')
u1, u2, x1, x2 = sp.symbols('u1 u2 x1 x2', real=True)
hu, hx = hom([u1, u2, 0]), hom([x1, x2, 0])
up, xp = sp.Matrix([u1, u2]), sp.Matrix([x1, x2])
bv1, Y1v = sp.Matrix([1, 1, 0, 0]), sp.Matrix([1, 1, 0, 0])
bv2, Y2v = sp.Matrix([1, 0, 1, 0]), hom(z3)


def pair(uvec, bvec, w):
    return sp.expand((uvec.T * w * bvec)[0, 0])


# prodState(x, y) with hom y = Y: hom x Y^T
p1 = pair(hu, bv1, G(A, B, hx * Y1v.T))
p2 = pair(hu, bv2, G(A, B, hx * Y2v.T))
report('P1', p1 == sp.expand(2 + 2 * (up.T * A * xp)[0]) and p2 == sp.expand(1 - (up.T * B * xp)[0]),
       'equatorial pairings: at effect (1,1,0,0) and Y = (1,1,0,0): 2 + 2 u\'^T a x\'; at effect (1,0,1,0) and '
       'Y = hom z3: 1 - u\'^T b x\' (symbolic): posFwd forces sigma_max(a), sigma_max(b) <= 1, and posInv (by F2) '
       'the same for a^-1, b^-1, so a, b are orthogonal')
bb = sp.symbols('bb0:4', real=True)
yy = sp.symbols('yy0:4', real=True)
bvec, Yvec = sp.Matrix(bb), sp.Matrix(yy)
sig = (bvec.T * S_(Yvec))[0]
tau = (bvec.T * T_(Yvec))[0]
lhs = sp.expand((bvec.T * Yvec)[0] * (bvec.T * HN * Yvec)[0] - sig ** 2 - tau ** 2)
Nb = bb[0] ** 2 - bb[1] ** 2 - bb[2] ** 2 - bb[3] ** 2
Ny = yy[0] ** 2 - yy[1] ** 2 - yy[2] ** 2 - yy[3] ** 2
ideal = sp.expand(Nb * (yy[0] ** 2 - yy[1] ** 2) + (bb[2] ** 2 + bb[3] ** 2) * Ny)
report('P2', sp.expand(lhs - ideal) == 0,
       '<b,Y><b,HN Y> - sigma^2 - tau^2 = N(b) (Y0^2 - Y1^2) + (b2^2 + b3^2) N(Y) with N the Lorentz form '
       '(symbolic): on null b, Y the right side of the mixing bound squared is sigma^2 + tau^2')
c, s, sg, tg = sp.symbols('c s sigma tau', real=True)
Urot = sp.Matrix([[c, -s], [s, c]])
Uref = sp.Matrix([[c, s], [s, -c]])
okU = True
for U in (Urot, Uref):
    M = (sg * I2 + tg * U).T * (sg * I2 + tg * U)
    tgt = (sg ** 2 + tg ** 2) * I2 + sg * tg * (U + U.T)
    okU = okU and all(sp.expand((M - tgt)[i, j]).subs(s ** 2, 1 - c ** 2).expand() == 0 for i in range(2) for j in range(2))
report('P3', okU and sp.simplify((Urot + Urot.T) - 2 * c * I2) == sp.zeros(2, 2)
       and sorted((Uref + Uref.T).subs(s, sp.sqrt(1 - c ** 2)).eigenvals().keys(), key=str) == [-2, 2],
       '(sigma I + tau U)^T (sigma I + tau U) = (sigma^2 + tau^2) I + sigma tau (U + U^T) for O(2) (mod c^2 + s^2 = 1); '
       'U + U^T = 2c I for rotations, eigenvalues +-2 for reflections: the bound for sigma tau of both signs forces '
       'U + U^T = 0, i.e. U = +-J\' (c = 0 rotations), so b = +-a J\'')

# ---------------------------------------------------------------- T: orientation (thread D T2) and M_refl
section('T  orientation is a gate invariant; M_refl')
xs = sp.symbols('p0:3', real=True)
ys = sp.symbols('q0:3', real=True)
dcp = sp.factor(cnot(prodState(xs, ys)).det())
tgt = -(xs[0] ** 2 + xs[1] ** 2) * (1 - xs[2] ** 2) * (1 - ys[0] ** 2) * (ys[1] ** 2 + ys[2] ** 2)
report('T1', sp.expand(dcp - tgt) == 0,
       f'det cnot(prodState x y) = -(x0^2+x1^2)(1-x2^2)(1-y0^2)(y1^2+y2^2) (symbolic): <= 0 on ball x ball')
unit = {xs[0]: sp.sqrt(1 - xs[1] ** 2 - xs[2] ** 2), ys[1]: sp.sqrt(1 - ys[0] ** 2 - ys[2] ** 2)}
dunit = sp.expand(tgt.subs(unit))
report('T2', sp.expand(dunit + (1 - xs[2] ** 2) ** 2 * (1 - ys[0] ** 2) ** 2) == 0,
       'for unit x, y: det cnot(prodState x y) = -(1-x2^2)^2 (1-y0^2)^2, in [-1, 0]. In T2\'s argument '
       '-det A det B = det A~ det B~ * d with |det| = 1 on both sides, so |d| = 1, d = -1, and the orientations agree')
Am = sp.Matrix(3, 3, sp.symbols('m0:9'))
Bm = sp.Matrix(3, 3, sp.symbols('n0:9'))
report('T3', sp.expand(actC(Am, actT(Bm, ws)).det() - Am.det() * Bm.det() * ws.det()) == 0 and phiW.det() == -1,
       'det(actC A (actT B w)) = det A det B det w (symbolic) and det phiW = -1')
report('T4', cnot(prodState(xplus, z3)) == phiW and actC(reflY, phiW) == idW and idW.det() == 1,
       'M_refl: cnot sends prodState xplus z3 to phiW, while the claimed form with post-local reflY gives actC reflY phiW '
       '= idW of determinant +1 > 0; since every cnot image of a product of ball states has det <= 0 (T1) and '
       'pre-locals map products of ball states to products of ball states, (reflY, I) is the post-local pair of no '
       'decomposition of cnot')

# ---------------------------------------------------------------- C: deletion countermodels
section('C  deletion countermodels for T1')
half = G(I2 / 2, Jp / 2, ws)
deph = sp.diag(1, 1, 0, 0)  # on the control basis coordinates (hom z3, hom -z3, e1, e2): keep hom(+-z3), kill e1, e2
Pkeep = BASIS * deph * BASIS.inv()  # projection of the control index onto span(hom z3, hom -z3)
report('C1', zero4(half - (cnot(ws) / 2 + cnot(Pkeep * ws) / 2)),
       'G(I/2, J\'/2) = (1/2) cnot + (1/2) cnot . (control dephasing onto span(hom z3, hom -z3)) (symbolic)')
x1_, x2_, x3_ = sp.symbols('r1 r2 r3', real=True)
y1_, y2_, y3_ = sp.symbols('s1 s2 s3', real=True)
P = prodState([x1_, x2_, x3_], [y1_, y2_, y3_])
pz, qz = (1 + x3_) / 2, (1 - x3_) / 2
deph_img = cnot(Pkeep * P)
want = pz * prodState(z3, [y1_, y2_, y3_]) + qz * prodState(mz3, [y1_, -y2_, -y3_])
report('C2', zero4(deph_img - want),
       'the dephased part maps prodState x y to p_x prodState(z3, y) + q_x prodState(-z3, (y1, -y2, -y3)) with '
       'p_x, q_x >= 0 on the ball: a positive combination of products, so G(I/2, J\'/2) satisfies posFwd '
       '(landed cnot_prodState_mem_maxCone, prodState_mem_maxCone)')
e10 = sp.zeros(4, 4)
e10[1, 0] = 1
Ge = G(I2 / 2, Jp / 2, e10)
inv_img = G(2 * I2, 2 * Jp, prodState(xplus, z3))
val = pair(hom([-1, 0, 0]), sp.Matrix([1, 1, 0, 0]), inv_img)
report('C3', ipW(Ge, Ge) == Q(1, 4) and zero4(G(2 * I2, 2 * Jp, G(I2 / 2, Jp / 2, ws)) - ws) and val == -1,
       f'ipW(G e10, G e10) = {ipW(Ge, Ge)} != 1 (N-CLASS gates are ipW-orthogonal); G(2I, 2J\') is the inverse and '
       f'pairs prodState(xplus, z3) with hom(-1,0,0), (1,1,0,0) to {val} < 0: posInv fails')
report('C3c', ipW(cnot(e10), cnot(e10)) == 1, 'countercontrol: cnot itself is ipW-orthogonal on e10')

# ---------------------------------------------------------------- A: hadm clause (c) countermodel
section('A  hadm (c): the scaled cnot orbit is not a convex cone')
E00 = prodState([0, 0, 0], [0, 0, 0])
summ = E00 + phiW
c_summ = cnot(summ)
report('A1', E00.rank() == 1 and phiW == cnot(prodState(xplus, z3)) and summ.rank() == 4 and c_summ.rank() == 2,
       'E00 = prodState 0 0 (a product) and phiW = cnot(prodState xplus z3) lie in the scaled cnot orbit; their sum has '
       'rank 4 and its cnot image rank 2, while products are rank 1: the sum is neither a scaled product nor a scaled '
       'cnot image of one (cnot is an involution), so additivity fails')
report('A1c', cnot(cnot(summ)) == summ and cnot(E00) == E00, 'countercontrol bookkeeping: cnot is an involution and fixes E00')

print('\nAUDIT-D', 'ALL CONFIRMED' if ok_all else 'MISMATCH FOUND')
