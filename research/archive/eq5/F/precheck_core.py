"""EQ4-F proof-completion design: exact pre-checks for the Pauli-free core and the Pauli layer of the IE1-first
route, and for the exact parts of three insufficiency foils (research only; nothing here is kernel-checked).

Usage:  python3 -I -B precheck_core.py <base>/verification/lean-mathlib/OIBridge <path to FourCopyPackage.lean>

Conventions are read from the sources (K0-K3) and then used: tables are 4x4 (row = first token); actC N om = H(N).om,
actT N om = om.H(N)^T, H(N) = diag(1, N); cnot = the kernel's signed permutation; pauliW om = (1/4) sum om_mn
sigma_m (x) sigma_n with tensorOf's index order; pureTab C = Re tr(C^H sigma_m C sigma_n^T).

DECISION RULE (fixed before the first run; rules, not expected numbers).  Print `VERDICT IE1FIRST-CORE-EXACT` iff every
check below passes; otherwise `VERDICT NOT RENDERED`.  Exact arithmetic only (Fractions; sympy Rational and I).
  K0  sgn, pc, pt parsed from CompositeDimension.lean equal the transcription used here.
  K1  pauli1, pauliW, pureTab parsed from the package equal the transcription; tensorOf parsed from the base.
  K2  rotFun and cycEquiv parsed from KInfFoundations.lean equal the transcription (rotX = cyc3 . rot3 . cyc3^-1).
  K3  nflip and reflY parsed from the base equal diag(1,-1,-1) and diag(1,-1,1).
  -- Pauli-free core --
  N1  right link, control side: with L' = actC A13 (actT B13 (actC R phiW)), Bell02 . g . L'^T =
      actT (A13 R A13^T) (Theta g) on all 16 units (4 draws); countercontrol actT (A13^T R A13) fails somewhere.
  N2  right link, target side: with L' = actC A13 (actT B13 (actT R phiW)), Bell02 . g . L'^T =
      Theta (actT (B13 R^T B13^T) g) on all units (4 draws).
  N3  actT R phiW = actC (reflY R^T reflY) phiW for 6 rational rotations R.
  N4  Lean-level control family: cnot (prodState (rot3 a xplus) (rotX b z3)) = actC (rot3 a . rotX b) phiW for 36
      rational angle pairs (rational cos/sin).
  N5  Lean-level target family: actT (rotX b . rot3 a) phiW = actC (rot3 a . rotX b) phiW for the same 36 pairs.
  N6  adjoints: ipW E (actC M X) = ipW (actC M^T E) X and ipW E (actT M X) = ipW (actT M^T E) X, 6 random rational
      M (not orthogonal), E, X.
  N7  reflection charts: on all units, actC reflY (cnot w) = cnotTw (actC reflY w) and
      actC reflY (actT reflY (cnot w)) = cnot (actC reflY (actT reflY w)).
  N8  witness reduction for the generalized Lemma P: for (eA, eB) in {I, reflY}^2,
      actC eA (actT eB (cnot (prodState s xplus s z3))) = gateOf (eA != eB) (prodState s xplus s z3), s = +-1, and
      the same for tens (sharpVec (s xplus)) (sharpVec (s z3)).
  N9  Theta inverse: actC R02^T (actT R13^T (Theta g)) = g on all units (4 draws).
  -- Pauli layer --
  S0  pauliW (cnot w) = CNOT . pauliW w . CNOT^H on all units (CNOT controlled on the first token).
  S1  Schmidt forms: pureTab (diag (a, b (p + i q))) = cnot (prodState (2abp, 2abq, a^2 - b^2) z3) for rational
      a^2 + b^2 = 1, p^2 + q^2 = 1 (12 cases); countercontrol with the conjugate phase fails for q != 0.
  S2  pauliW (pureTab C) = v v^H with v = (C00, C01, C10, C11), 6 random Gaussian-rational C.
  S3  ipW E X = 4 Re tr (pauliW E . pauliW X), 6 random rational E, X.
  S4  spin lift: for 5 rational unit quaternions, U = q0 1 - i (q1 X + q2 Y + q3 Z) has det 1 and U U^H = 1;
      R_U[j][k] = (1/2) Re tr (sigma_j U sigma_k U^H) is in SO(3); U^H sigma_j U = sum_k R_U[j][k] sigma_k; and
      pureTab (U C V^T) = actC R_U (actT R_V (pureTab C)) for random C (5 x 5 pairs); countercontrol with R_U^T fails.
  S5  transpose: pauliW (transposeW w) = (pauliW w)^T, actC reflY (actT reflY w) = transposeW w, and transposeW
      commutes with actT reflY, on all units.
  S6  pauliW phiW = v v^H with v = (1, 0, 0, 1)/sqrt2; s^H pauliW(idW) s < 0 for s = (0, 1, -1, 0).
  -- exact parts of insufficiency foils --
  F1  convexity: sigma = (3/4) prodState xplus z3 + (1/4) prodState z3 z3 (separable), rho = cnot sigma,
      rho' = actT R_H rho with R_H = [[0,0,1],[0,-1,0],[1,0,0]] in SO(3): rho' is PSD (15 principal minors >= 0), has
      rank 2, det pauliW (actT reflY rho') < 0, det pauliW (actT reflY (cnot rho')) < 0; control: the same tests on
      sigma give PSD and det >= 0.
  F2  closedness and coherence: psi1 = actT R_H phiW is pure (rank 1, det 0); the first-token Bloch vector of every
      g(psi1), g in the closure H of <cnot, actC nflip, actT nflip>, has norm^2 < 1, and |H| = 8; control: a product
      state has norm^2 = 1.
"""
import random
import re
import sys
from fractions import Fraction as Fr

import sympy as sp
from sympy import I, Matrix, Rational as Q

BASE, PKG = sys.argv[1], sys.argv[2]
rng = random.Random(20261009 + 1)
RES = []


def check(name, ok, detail=""):
    RES.append(bool(ok))
    print("%s %s%s" % ("PASS" if ok else "FAIL", name, (" -- " + detail) if detail else ""), flush=True)


src_cd = open(BASE + "/CompositeDimension.lean").read()
src_kf = open(BASE + "/KInfFoundations.lean").read()
src_k2 = open(BASE + "/K2Guard.lean").read()
src_mc = open(BASE + "/MonoidalCompletion.lean").read()
src_pk = open(PKG).read()

# ------------------------------------------------------------------------------------------------ transcriptions
SGN = lambda m, n: -1 if (m == 1 and n == 3) or (m == 2 and n == 2) else 1  # noqa: E731
PC = [[0, 0, 3, 3], [1, 1, 2, 2], [2, 2, 1, 1], [3, 3, 0, 0]]
PT = [[0, 1, 2, 3], [1, 0, 3, 2], [1, 0, 3, 2], [0, 1, 2, 3]]


def parse_table(name):
    m = re.search(r"def %s : Fin 4 → Fin 4 → Fin 4\n((?:  \|.*\n){4})" % name, src_cd)
    return [[int(v) for v in re.findall(r"=> (\d)", ln)] for ln in m.group(1).strip().splitlines()]


sgn_line = re.search(r"def sgn \(μ ν : Fin 4\) : ℝ := (.*)", src_cd).group(1).strip()
check("K0 sgn, pc, pt transcription", parse_table("pc") == PC and parse_table("pt") == PT
      and sgn_line == "if (μ = 1 ∧ ν = 3) ∨ (μ = 2 ∧ ν = 2) then -1 else 1")
k1 = ("![1, !![0, 1; 1, 0], !![0, -Complex.I; Complex.I, 0], !![1, 0; 0, -1]]" in src_pk
      and "(1 / 4 : ℂ) • ∑ μ, ∑ ν, ((ω μ ν : ℝ) : ℂ) • MonoidalCompletion.tensorOf (pauli1 μ) (pauli1 ν)" in src_pk
      and "fun μ ν => (Matrix.trace (Cᴴ * pauli1 μ * C * (pauli1 ν)ᵀ)).re" in src_pk
      and "Matrix.of fun p q => XA p.1 q.1 * XB p.2 q.2" in src_mc)
check("K1 pauli1, pauliW, pureTab (package) and tensorOf (base) transcription", k1)
k2 = ("![Real.cos t * v 0 - Real.sin t * v 1, Real.sin t * v 0 + Real.cos t * v 1, v 2]" in src_kf
      and "toFun v := ![v 2, v 0, v 1]" in src_kf
      and "noncomputable def rotX (θ : ℝ) : (Fin 3 → ℝ) ≃ᵃ[ℝ] (Fin 3 → ℝ) := cyc3 * rot3 θ * cyc3⁻¹"
      in open(BASE + "/OrbitNormalization.lean").read())
check("K2 rotFun, cycEquiv, rotX transcription", k2)
k3 = ("toFun x := fun i => (![1, -1, -1] : Fin 3 → ℝ) i * x i" in src_cd
      and "toFun x := fun i => (![1, -1, 1] : Fin 3 → ℝ) i * x i" in src_k2)
check("K3 nflip, reflY transcription", k3)


# ------------------------------------------------------------------------------------------------ real tables
def M3(rows):
    return Matrix(3, 3, lambda i, j: Q(rows[i][j]))


def H(N):
    out = sp.zeros(4, 4)
    out[0, 0] = 1
    out[1:, 1:] = N
    return out


def actC(N, om):
    return H(N) * om


def actT(N, om):
    return om * H(N).T


def hom(x):
    return Matrix([1] + list(x))


def prodState(x, y):
    return hom(x) * hom(y).T


def sharpVec(b):
    return Matrix([Q(1, 2)] + [Q(v) / 2 for v in b])


def tens(a, b):
    return a * b.T


def ipW(E, X):
    return sum(E[m, n] * X[m, n] for m in range(4) for n in range(4))


def unit(i, j):
    U = sp.zeros(4, 4)
    U[i, j] = 1
    return U


UNITS = [unit(i, j) for i in range(4) for j in range(4)]
reflY = M3([[1, 0, 0], [0, -1, 0], [0, 0, 1]])
nflip = M3([[1, 0, 0], [0, -1, 0], [0, 0, -1]])
I3 = sp.eye(3)
phiW = H(reflY)
idW = sp.eye(4)
xplus, z3 = [1, 0, 0], [0, 0, 1]


def cnot(om):
    return Matrix(4, 4, lambda m, n: SGN(m, n) * om[PC[m][n], PT[m][n]])


def cnotTw(om):
    return actT(reflY, cnot(actT(reflY, om)))


def gateOf(tau, om):
    return cnotTw(om) if tau else cnot(om)


def transposeW(om):
    s = [1, 1, -1, 1]
    return Matrix(4, 4, lambda m, n: s[m] * s[n] * om[m, n])


def cayley(a, b, c):
    S = Matrix([[0, -c, b], [c, 0, -a], [-b, a, 0]])
    return (I3 - S) * (I3 + S).inv()


def rq():
    return Q(rng.randint(-4, 4), rng.randint(1, 3))


def rand_rot():
    return cayley(rq(), rq(), rq())


def rand_orth():
    R = rand_rot()
    return R * reflY if rng.random() < 0.5 else R


def bellOf(A, B):
    return actC(A, actT(B, phiW))


def rot3(c, s):
    return Matrix([[c, -s, 0], [s, c, 0], [0, 0, 1]])


CYC = Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])  # cyc3 v = (v2, v0, v1)


def rotX(c, s):
    return CYC * rot3(c, s) * CYC.inv()


def circ(u):
    u = Q(u)
    return (1 - u * u) / (1 + u * u), 2 * u / (1 + u * u)


US = [Q(1, 2), Q(1, 3), Q(2), Q(-3, 4), Q(5, 7), Q(-1, 5)]

# N1, N2, N9
ok1, cc1, ok2, ok9 = True, 0, True, True
for trial in range(4):
    A02, B02, A13, B13 = rand_orth(), rand_orth(), rand_orth(), rand_orth()
    b02, b13 = bellOf(A02, B02), bellOf(A13, B13)
    R02, R13 = A02 * reflY * B02.T, A13 * reflY * B13.T
    R = rand_rot()

    def Theta(g):
        return b02 * g * b13.T

    Lc = actC(A13, actT(B13, actC(R, phiW)))
    Lt = actC(A13, actT(B13, actT(R, phiW)))
    for g in UNITS:
        lhs = b02 * g * Lc.T
        ok1 &= lhs == actT(A13 * R * A13.T, Theta(g))
        cc1 += lhs != actT(A13.T * R * A13, Theta(g))
        ok2 &= b02 * g * Lt.T == Theta(actT(B13 * R.T * B13.T, g))
        ok9 &= actC(R02.T, actT(R13.T, Theta(g))) == g
check("N1 right link, control side: Bell02 . g . L'^T = actT (A13 R A13^T) (Theta g); other order fails",
      ok1 and cc1 > 0, "%d unit failures for the countercontrol" % cc1)
check("N2 right link, target side: Bell02 . g . L'^T = Theta (actT (B13 R^T B13^T) g)", ok2)
# N3
ok3 = all(actT(R, phiW) == actC(reflY * R.T * reflY, phiW) for R in [rand_rot() for _ in range(6)])
check("N3 actT R phiW = actC (reflY R^T reflY) phiW", ok3)
# N4, N5
ok4, ok5 = True, True
for ua in US:
    ca, sa = circ(ua)
    for ub in US:
        cb, sb = circ(ub)
        x = list(rot3(ca, sa) * Matrix(xplus))
        y = list(rotX(cb, sb) * Matrix(z3))
        ok4 &= cnot(prodState(x, y)) == actC(rot3(ca, sa) * rotX(cb, sb), phiW)
        ok5 &= actT(rotX(cb, sb) * rot3(ca, sa), phiW) == actC(rot3(ca, sa) * rotX(cb, sb), phiW)
check("N4 cnot (prodState (rot3 a xplus) (rotX b z3)) = actC (rot3 a . rotX b) phiW, 36 pairs", ok4)
check("N5 actT (rotX b . rot3 a) phiW = actC (rot3 a . rotX b) phiW, 36 pairs", ok5)
# N6
ok6 = True
for _ in range(6):
    Mm = Matrix(3, 3, lambda i, j: rq())
    E = Matrix(4, 4, lambda i, j: rq())
    X = Matrix(4, 4, lambda i, j: rq())
    ok6 &= ipW(E, actC(Mm, X)) == ipW(actC(Mm.T, E), X) and ipW(E, actT(Mm, X)) == ipW(actT(Mm.T, E), X)
check("N6 actC and actT adjoints for ipW (6 random non-orthogonal M)", ok6)
# N7
ok7 = all(actC(reflY, cnot(w)) == cnotTw(actC(reflY, w))
          and actC(reflY, actT(reflY, cnot(w))) == cnot(actC(reflY, actT(reflY, w))) for w in UNITS)
check("N7 actC reflY . cnot = cnotTw . actC reflY and actC reflY . actT reflY . cnot = cnot . actC reflY . actT reflY",
      ok7)
# N8
ok8 = True
for s in (1, -1):
    xs, zs = [s * v for v in xplus], [s * v for v in z3]
    for eA in (False, True):
        for eB in (False, True):
            NA, NB = (reflY if eA else I3), (reflY if eB else I3)
            ok8 &= actC(NA, actT(NB, cnot(prodState(xs, zs)))) == gateOf(eA != eB, prodState(xs, zs))
            ok8 &= (actC(NA, actT(NB, cnot(tens(sharpVec(xs), sharpVec(zs)))))
                    == gateOf(eA != eB, tens(sharpVec(xs), sharpVec(zs))))
check("N8 witness reduction: actC eA (actT eB (cnot P)) = gateOf (eA != eB) P on the Lemma P witnesses", ok8)
check("N9 Theta inverse: actC R02^T (actT R13^T (Theta g)) = g on all units (4 draws)", ok9)

# ------------------------------------------------------------------------------------------------ Pauli layer
S0m = sp.eye(2)
SX = Matrix([[0, 1], [1, 0]])
SY = Matrix([[0, -I], [I, 0]])
SZ = Matrix([[1, 0], [0, -1]])
SIG = [S0m, SX, SY, SZ]


def kron(A, B):
    return Matrix(4, 4, lambda r, c: A[r // 2, c // 2] * B[r % 2, c % 2])


KR = [[kron(SIG[m], SIG[n]) for n in range(4)] for m in range(4)]


def pauliW(om):
    out = sp.zeros(4, 4)
    for m in range(4):
        for n in range(4):
            if om[m, n] != 0:
                out += om[m, n] * KR[m][n]
    return (out / 4).applyfunc(sp.expand)


def pureTab(C):
    return Matrix(4, 4, lambda m, n: sp.re(sp.expand((C.H * SIG[m] * C * SIG[n].T).trace())))


def vecC(C):
    return Matrix([C[0, 0], C[0, 1], C[1, 0], C[1, 1]])


def zero(Mx):
    return all(sp.simplify(sp.expand(v)) == 0 for v in Mx)


CNOTU = Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
ok_s0 = all(zero(pauliW(cnot(w)) - CNOTU * pauliW(w) * CNOTU.H) for w in UNITS)
check("S0 pauliW (cnot w) = CNOT pauliW(w) CNOT^H on all units", ok_s0)
# S1
pts = [(Q(3, 5), Q(4, 5)), (Q(5, 13), Q(12, 13)), (Q(1), Q(0)), (Q(8, 17), Q(-15, 17))]
phs = [(Q(1), Q(0)), (Q(3, 5), Q(4, 5)), (Q(-7, 25), Q(24, 25))]
ok_s1, cc_s1 = True, True
for (a, b) in pts:
    for (p, q) in phs:
        D = Matrix([[a, 0], [0, b * (p + I * q)]])
        x = [2 * a * b * p, 2 * a * b * q, a * a - b * b]
        target = cnot(prodState(x, z3))
        ok_s1 &= zero(pureTab(D) - target)
        if q != 0 and a * b != 0:
            Dc = Matrix([[a, 0], [0, b * (p - I * q)]])
            cc_s1 &= not zero(pureTab(Dc) - target)
check("S1 pureTab (diag (a, b e^{i phi})) = cnot (prodState (2ab cos, 2ab sin, a^2 - b^2) z3); conjugate phase fails",
      ok_s1 and cc_s1)


def rgauss():
    return Q(rng.randint(-3, 3), rng.randint(1, 2)) + I * Q(rng.randint(-3, 3), rng.randint(1, 2))


ok_s2 = True
for _ in range(6):
    C = Matrix(2, 2, lambda i, j: rgauss())
    v = vecC(C)
    ok_s2 &= zero(pauliW(pureTab(C)) - v * v.H)
check("S2 pauliW (pureTab C) = v v^H, v = (C00, C01, C10, C11)", ok_s2)
ok_s3 = True
for _ in range(6):
    E = Matrix(4, 4, lambda i, j: rq())
    X = Matrix(4, 4, lambda i, j: rq())
    ok_s3 &= sp.simplify(4 * sp.re((pauliW(E) * pauliW(X)).trace()) - ipW(E, X)) == 0
check("S3 ipW E X = 4 Re tr (pauliW E pauliW X)", ok_s3)
# S4
quats = [(Q(1, 2), Q(1, 2), Q(1, 2), Q(1, 2)), (Q(1, 5), Q(2, 5), Q(2, 5), Q(4, 5)), (Q(2, 7), Q(3, 7), Q(6, 7), 0),
         (Q(1, 3), Q(2, 3), 0, Q(2, 3)), (Q(0), Q(2, 11), Q(6, 11), Q(9, 11))]


def su2(q):
    q0, q1, q2, q3 = q
    return (q0 * sp.eye(2) - I * (q1 * SX + q2 * SY + q3 * SZ)).applyfunc(sp.expand)


def spinR(U):
    return Matrix(3, 3, lambda j, k: sp.re(sp.expand((SIG[j + 1] * U * SIG[k + 1] * U.H).trace())) / 2)


ok_s4a, ok_s4b, ok_s4c, cc_s4 = True, True, True, 0
Us = [su2(q) for q in quats]
Rs = [spinR(U) for U in Us]
for U, R in zip(Us, Rs):
    ok_s4a &= sp.expand(U.det()) == 1 and zero(U * U.H - sp.eye(2)) and R * R.T == I3 and R.det() == 1
    for j in range(3):
        ok_s4b &= zero(U.H * SIG[j + 1] * U - sum((R[j, k] * SIG[k + 1] for k in range(3)), sp.zeros(2, 2)))
Cs = [Matrix(2, 2, lambda i, j: rgauss()) for _ in range(2)]
for iu in range(len(Us)):
    for iv in range(len(Us)):
        C = Cs[(iu + iv) % 2]
        lhs = pureTab((Us[iu] * C * Us[iv].T).applyfunc(sp.expand))
        P = pureTab(C)
        ok_s4c &= zero(lhs - actC(Rs[iu], actT(Rs[iv], P)))
        cc_s4 += not zero(lhs - actC(Rs[iu].T, actT(Rs[iv], P)))
check("S4a five rational SU(2) elements: det 1, unitary; R_U in SO(3)", ok_s4a)
check("S4b U^H sigma_j U = sum_k R_U[j][k] sigma_k", ok_s4b)
check("S4c pureTab (U C V^T) = actC R_U (actT R_V (pureTab C)), 25 pairs; with R_U^T it fails",
      ok_s4c and cc_s4 > 0, "%d pair failures for the countercontrol" % cc_s4)
# S5
ok_s5 = all(zero(pauliW(transposeW(w)) - pauliW(w).T) and actC(reflY, actT(reflY, w)) == transposeW(w)
            and actT(reflY, transposeW(w)) == transposeW(actT(reflY, w)) for w in UNITS)
check("S5 pauliW . transposeW = transpose . pauliW; actC reflY . actT reflY = transposeW; commutation", ok_s5)
# S6
v = Matrix([1, 0, 0, 1])
s = Matrix([0, 1, -1, 0])
neg = sp.simplify((s.H * pauliW(idW) * s)[0, 0])
check("S6 pauliW phiW = v v^H, v = (1,0,0,1)/sqrt2; singlet expectation of pauliW idW < 0",
      zero(pauliW(phiW) - v * v.H / 2) and neg < 0, "singlet value %s" % neg)


# ------------------------------------------------------------------------------------------------ foils
def psd_minors(Hm):
    idx = range(4)
    from itertools import combinations
    vals = []
    for r in range(1, 5):
        for sub in combinations(idx, r):
            vals.append(sp.simplify(Hm.extract(list(sub), list(sub)).det()))
    return all(sp.re(val) >= 0 and sp.im(val) == 0 for val in vals)


RH = M3([[0, 0, 1], [0, -1, 0], [1, 0, 0]])
sigma = Q(3, 4) * prodState(xplus, z3) + Q(1, 4) * prodState(z3, z3)
rho = cnot(sigma)
rhop = actT(RH, rho)
det_a = sp.simplify(pauliW(actT(reflY, rhop)).det())
det_b = sp.simplify(pauliW(actT(reflY, cnot(rhop))).det())
det_c = sp.simplify(pauliW(actT(reflY, sigma)).det())
f1 = (RH * RH.T == I3 and RH.det() == 1 and psd_minors(pauliW(rhop)) and pauliW(rhop).rank() == 2
      and det_a < 0 and det_b < 0 and psd_minors(pauliW(actT(reflY, sigma))) and det_c >= 0)
check("F1 convexity foil: rho' = actT R_H (cnot sigma) is PSD, rank 2, and neither rho' nor cnot rho' is PPT;"
      " control sigma is PPT", f1, "dets %s, %s; control %s" % (det_a, det_b, det_c))


def as_map(fn):
    return [fn(u) for u in UNITS]


def apply_map(imgs, om):
    out = sp.zeros(4, 4)
    for k, u in enumerate(UNITS):
        c = om[k // 4, k % 4]
        if c != 0:
            out += c * imgs[k]
    return out


gens = [as_map(cnot), as_map(lambda w: actC(nflip, w)), as_map(lambda w: actT(nflip, w))]
group = [as_map(lambda w: w)]
frontier = list(group)
while frontier:
    new = []
    for g in frontier:
        for h in gens:
            comp = [apply_map(h, gi) for gi in g]
            if all(comp != e for e in group):
                group.append(comp)
                new.append(comp)
    frontier = new
psi1 = actT(RH, phiW)
pure = pauliW(psi1).rank() == 1 and sp.simplify(pauliW(psi1).det()) == 0
norms = [sum(apply_map(g, psi1)[i, 0] ** 2 for i in range(1, 4)) for g in group]
ctrl = sum(prodState([Q(3, 5), 0, Q(4, 5)], z3)[i, 0] ** 2 for i in range(1, 4))
f2 = pure and len(group) == 8 and all(n < 1 for n in norms) and ctrl == 1
check("F2 psi1 = actT R_H phiW is pure; every g(psi1), g in H (|H| = 8), has marginal norm^2 < 1; control product = 1",
      f2, "|H| = %d, norms %s" % (len(group), sorted(set(str(n) for n in norms))))
print("--- precheck_core: %d/%d checks pass" % (sum(RES), len(RES)))
print("VERDICT IE1FIRST-CORE-EXACT" if all(RES) else "VERDICT NOT RENDERED")
