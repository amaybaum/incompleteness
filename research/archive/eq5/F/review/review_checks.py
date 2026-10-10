"""EQ5-F DEPGRAPH review: independent exact checks of the IE1-first route (research only; nothing is kernel-checked).

Usage:  python3 -I -B review_checks.py <base>/verification/lean-mathlib/OIBridge <package dir> <mathlib root>

Independence from the note's pre-checks: definitions are implemented LITERALLY from the Lean sources (homMap, actT,
actC entrywise, rot3/rotX/cyc3 as maps applied to basis vectors, tensorOf as Matrix.of on index pairs), complex
numbers are Gaussian rationals built from fractions.Fraction (no sympy except the symbolic identities B1), orthogonal
matrices come from integer quaternions (Euler-Rodrigues), not from the Cayley transform, and the random seed differs.

DECISION RULE (fixed before the first run; rules, not expected numbers).  Print `VERDICT REVIEW-CHECKS-EXACT` iff every
check below passes; a check that names a countercontrol passes only if that countercontrol fails as required.
Otherwise print `VERDICT NOT RENDERED`.  Exact arithmetic only.
  T0  transcription: the Lean source strings of every definition used here are found verbatim (base, package, Mathlib).
  T1  matrix-model control: literal actC/actT equal H(N).om and om.H(N)^T for random NON-orthogonal N.
  C1  G1: Theta g = actC R02 (actT R13 g), R = A reflY B^T, all 16 units + random tables, all four det classes of
      (A02, B02); countercontrol: R = A B^T fails.
  C2  G2 incl. the note's N9: Theta is ipW-orthogonal (all unit pairs) and actC R02^T (actT R13^T (Theta g)) = g;
      countercontrol: actC R02 (actT R13 (Theta g)) = g fails for some draw.
  C3  G7(i): N (prodState (A'^T x) (B'^T y)) = actC A (actT B (cnot (prodState x y))) for general rational unit x, y
      (stereographic points), A'^T x unit; countercontrol: A' x in place of A'^T x fails.
  C4  G7(ii, iii) with literal rot3/rotX: cnot (prodState (rot3 a xplus) (rotX b z3)) = actC (rot3 a . rotX b) phiW and
      actT (rotX b . rot3 a) phiW = actC (rot3 a . rotX b) phiW; base euler_apply_pole formula reproduced;
      countercontrol: actT (rot3 a . rotX b) phiW = actC (rot3 a . rotX b) phiW fails for some (a, b).
  C5  G8, all four rotated-link identities with the links BUILT as gate images N02(product), N13(product) with general
      orthogonal pre-locals; countercontrols: conjugation A^T M A in place of A M A^T fails; B M' B^T without the
      transpose of M' fails.
  C6  target 02 (Lemma R): fourVal = ipW X (E Y F^T) = ipW E (X F Y^T) (O1, O3); target02.upper and .lower values equal
      the famII and famI values; countercontrol: dropping the transposes changes the value.
  C7  G14 witness reduction: for all four det classes of (A, B), general pre-locals and s = +-1:
      actC R_A^T (actT R_B^T (N P)) = gateOf (orient A B) P for P the Lemma P product states and sharp-effect tables
      (N applied to the pre-local-corrected inputs), R_A = A eps_A in SO(3), orient A B = (eps_A != eps_B);
      countercontrol: gateOf (not orient) fails.
  C8  G14 end to end: for all 16 orientation patterns, realized by general-chart data, the four reduced witnesses give a
      famI value < 0 exactly at the odd patterns.
  C9  G3 adjoints (literal ops, random non-orthogonal M) and O14 on all units.
  P1  L1, L2: ipW E X = 4 Re tr (pauliW E pauliW X); pauliW (pureTab C) = v v^H, v = (C00, C01, C10, C11).
  P2  L11(i): transposeW (pureTab C) = pureTab (C.map star); countercontrol: pureTab (C^T) differs for some C.
  P3  L11(ii)/L12 cases: actC reflY (pureTab C) = actT reflY (pureTab (C.map star));
      actT reflY (actC reflY (pureTab C)) = pureTab (C.map star); pauliW (actT reflY w) = PT_2 (pauliW w) on all units;
      countercontrol: idW = actT reflY phiW has a negative expectation (not in Q3).
  P4  L8 with complex diagonal: pureTab (diag (d0, d1)) = n . cnot (prodState x z3), x the Bloch vector of (d0, d1),
      n = |d0|^2 + |d1|^2, Gaussian-rational d0, d1; countercontrol: conjugate phase fails.
  P5  L6 recheck: pureTab (U C V^T) = actC R_U (actT R_V (pureTab C)) for quaternion SU(2) elements; countercontrol R_U^T.
  F1  C_H exclusion, independent linear-witness route: |H| = 8; each h ipW-orthogonal and fixing entry (0,0); each
      h(psi1) has zero local parts and an orthogonal 3x3 correlation block; psi1_00 = 1, ipW psi1 psi1 = 4; spot values
      of W = 2 e00 - psi1 >= 0 on generators h(prodState x y); countercontrol: the certificate fails for phiW (which
      lies in C_H) and for a product state.
  F2  convexity foil recheck with an index-swap partial transpose: rho' PSD (all 15 principal minors), rank 2,
      det PT_2 pauliW rho' < 0, det PT_2 pauliW (cnot rho') < 0; control: sigma PPT.
  F3  closedness foil: det pauliW psi1 = 0 (psi1 not in int Q3); phiW = cnot (prodState xplus z3).
  B1  Lemma B1a: the four sharp-effect combinations give (1/2)(w00 +- w_ik) and (1/2)(w00 +- w_i0) symbolically.
  B2  Lemma B1e: the tok-converted expansions equal fourVal and O1 for famI and famII; countercontrol: reading tok in the
      wrong direction changes the value.
"""
import random
import re
import sys
from fractions import Fraction as Fr

BASE, PKG, ML = sys.argv[1], sys.argv[2], sys.argv[3]
rng = random.Random(4242)
RES = []


def check(name, ok, detail=""):
    RES.append(bool(ok))
    print("%s %s%s" % ("PASS" if ok else "FAIL", name, (" -- " + detail) if detail else ""), flush=True)


def read(p):
    with open(p, encoding="utf-8") as fh:
        return fh.read()


CD = read(BASE + "/CompositeDimension.lean")
K2 = read(BASE + "/K2Guard.lean")
KF = read(BASE + "/KInfFoundations.lean")
ON = read(BASE + "/OrbitNormalization.lean")
ES = read(BASE + "/EffectSpace.lean")
MC = read(BASE + "/MonoidalCompletion.lean")
DF = read(PKG + "/FourCopyDefs.lean")
PK = read(PKG + "/FourCopyPackage.lean")
AE = read(ML + "/Mathlib/LinearAlgebra/AffineSpace/AffineEquiv.lean")

# ------------------------------------------------------------------------------------------------ T0 transcription
needles = [
    (CD, "def hom (x : Fin d → ℝ) : HVec d := Matrix.vecCons 1 x"),
    (CD, "toFun v := Matrix.vecCons (v 0) (N (Matrix.vecTail v))"),
    (CD, "def actT (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (ω : W d) : W d := fun μ => homMap N (ω μ)"),
    (CD, "fun μ ν => homMap N (fun κ => ω κ ν) μ"),
    (CD, "def prodState (x y : Fin d → ℝ) : W d := fun μ ν => hom x μ * hom y ν"),
    (CD, "def tens (X Y : HVec d) : W d := fun μ ν => X μ * Y ν"),
    (CD, "def cnotFun (ω : W 3) : W 3 := fun μ ν => sgn μ ν * ω (pc μ ν) (pt μ ν)"),
    (CD, "def xplus : Fin 3 → ℝ := ![1, 0, 0]"),
    (CD, "def z3 : Fin 3 → ℝ := ![0, 0, 1]"),
    (CD, "def phiW : W 3 := fun μ ν => if μ = ν then (if μ = 2 then -1 else 1) else 0"),
    (CD, "toFun x := fun i => (![1, -1, -1] : Fin 3 → ℝ) i * x i"),
    (K2, "toFun x := fun i => (![1, -1, 1] : Fin 3 → ℝ) i * x i"),
    (K2, "def idW : W 3 := ![![1, 0, 0, 0], ![0, 1, 0, 0], ![0, 0, 1, 0], ![0, 0, 0, 1]]"),
    (ES, "noncomputable def sharpVec (b : Fin d → ℝ) : HVec d := Matrix.vecCons (1 / 2) fun j => b j / 2"),
    (KF, "![Real.cos t * v 0 - Real.sin t * v 1, Real.sin t * v 0 + Real.cos t * v 1, v 2]"),
    (KF, "toFun v := ![v 2, v 0, v 1]"),
    (KF, "invFun v := ![v 1, v 2, v 0]"),
    (ON, "noncomputable def rotX (θ : ℝ) : (Fin 3 → ℝ) ≃ᵃ[ℝ] (Fin 3 → ℝ) := cyc3 * rot3 θ * cyc3⁻¹"),
    (ON, "![Real.sin ψ * Real.sin θ, -(Real.cos ψ * Real.sin θ), Real.cos θ]"),
    (AE, "theorem coe_mul (e e' : P₁ ≃ᵃ[k] P₁) : ⇑(e * e') = e ∘ e' :="),
    (MC, "Matrix.of fun p q => XA p.1 q.1 * XB p.2 q.2"),
    (DF, "def tabMul (A B : W 3) : W 3 := fun μ ν => ∑ κ, A μ κ * B κ ν"),
    (DF, "def tabT (A : W 3) : W 3 := fun μ ν => A ν μ"),
    (DF, "def ipW (E X : W 3) : ℝ := ∑ μ, ∑ ν, E μ ν * X μ ν"),
    (DF, "def sgnY : Fin 4 → ℝ := ![1, 1, -1, 1]"),
    (DF, "def transposeW (ω : W 3) : W 3 := fun μ ν => sgnY μ * sgnY ν * ω μ ν"),
    (DF, "actTEquiv reflY reflY_reflY ≪≫ₗ cnot ≪≫ₗ actTEquiv reflY reflY_reflY"),
    (DF, "0 ≤ ipW X (tabMul (tabMul E Y) (tabT F))"),
    (DF, "0 ≤ ipW e (tabMul (tabMul L f) (tabT L'))"),
    (PK, "def fourVal (X Y E F : W 3) : ℝ := ∑ a, ∑ b, ∑ c, ∑ d, X a b * Y c d * E a c * F b d"),
    (PK, "∀ ω, N ω = actC A (actT B (cnot (actC A' (actT B' ω))))"),
    (PK, "def bellOf (A B : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) : W 3 := actC A (actT B phiW)"),
    (PK, "tabMul (tabMul (bellOf A02 B02) g) (tabT (bellOf A13 B13))"),
    (PK, "![1, !![0, 1; 1, 0], !![0, -Complex.I; Complex.I, 0], !![1, 0; 0, -1]]"),
    (PK, "(1 / 4 : ℂ) • ∑ μ, ∑ ν, ((ω μ ν : ℝ) : ℂ) • MonoidalCompletion.tensorOf (pauli1 μ) (pauli1 ν)"),
    (PK, "fun μ ν => (Matrix.trace (Cᴴ * pauli1 μ * C * (pauli1 ν)ᵀ)).re"),
    (PK, "decide (LinearMap.det A * LinearMap.det B = -1)"),
]
missing = [n for (s, n) in needles if n not in s]


def parse_table(name):
    m = re.search(r"def %s : Fin 4 → Fin 4 → Fin 4\n((?:  \|.*\n){4})" % name, CD)
    out = {}
    for (a, b, v) in re.findall(r"(\d), (\d) => (\d)", m.group(1)):
        out[(int(a), int(b))] = int(v)
    return out


PCd, PTd = parse_table("pc"), parse_table("pt")
sgn_src = re.search(r"def sgn \(μ ν : Fin 4\) : ℝ := if (.*) then -1 else 1", CD).group(1)
NEG = {(int(a), int(b)) for (a, b) in re.findall(r"μ = (\d) ∧ ν = (\d)", sgn_src)}
check("T0 transcription of %d definitions (base, package, Mathlib AffineEquiv.coe_mul) and of sgn/pc/pt"
      % len(needles), not missing and len(PCd) == 16 and len(PTd) == 16 and NEG == {(1, 3), (2, 2)},
      "missing: %s" % missing if missing else "")

# ------------------------------------------------------------------------------------------------ real tables
R4 = range(4)
R3 = range(3)


def zeros4():
    return [[Fr(0)] * 4 for _ in R4]


def mat3(rows):
    return [[Fr(v) for v in r] for r in rows]


def apply3(N, x):
    return [sum(N[i][j] * x[j] for j in R3) for i in R3]


def homMap(N, v):                       # Matrix.vecCons (v 0) (N (Matrix.vecTail v))
    return [v[0]] + apply3(N, v[1:])


def actT(N, om):                        # fun μ => homMap N (ω μ)
    return [homMap(N, om[m]) for m in R4]


def actC(N, om):                        # fun μ ν => homMap N (fun κ => ω κ ν) μ
    cols = [homMap(N, [om[k][n] for k in R4]) for n in R4]
    return [[cols[n][m] for n in R4] for m in R4]


def hom(x):
    return [Fr(1)] + [Fr(v) for v in x]


def prodState(x, y):
    hx, hy = hom(x), hom(y)
    return [[hx[m] * hy[n] for n in R4] for m in R4]


def tens(a, b):
    return [[a[m] * b[n] for n in R4] for m in R4]


def sharpVec(b):
    return [Fr(1, 2)] + [Fr(v) / 2 for v in b]


def cnot(om):
    return [[(Fr(-1) if (m, n) in NEG else Fr(1)) * om[PCd[(m, n)]][PTd[(m, n)]] for n in R4] for m in R4]


def tabMul(A, B):
    return [[sum(A[m][k] * B[k][n] for k in R4) for n in R4] for m in R4]


def tabT(A):
    return [[A[n][m] for n in R4] for m in R4]


def ipW(E, X):
    return sum(E[m][n] * X[m][n] for m in R4 for n in R4)


def add(A, B):
    return [[A[m][n] + B[m][n] for n in R4] for m in R4]


def smul(c, A):
    return [[c * A[m][n] for n in R4] for m in R4]


SGNY = [Fr(1), Fr(1), Fr(-1), Fr(1)]


def transposeW(om):
    return [[SGNY[m] * SGNY[n] * om[m][n] for n in R4] for m in R4]


def fourVal(X, Y, E, F):
    return sum(X[a][b] * Y[c][d] * E[a][c] * F[b][d] for a in R4 for b in R4 for c in R4 for d in R4)


REFLY = mat3([[1, 0, 0], [0, -1, 0], [0, 0, 1]])
NFLIP = mat3([[1, 0, 0], [0, -1, 0], [0, 0, -1]])
I3 = mat3([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
XPLUS, Z3 = [Fr(1), Fr(0), Fr(0)], [Fr(0), Fr(0), Fr(1)]
PHIW = [[(Fr(-1) if m == 2 else Fr(1)) if m == n else Fr(0) for n in R4] for m in R4]
IDW = [[Fr(int(m == n)) for n in R4] for m in R4]


def mm3(A, B):
    return [[sum(A[i][k] * B[k][j] for k in R3) for j in R3] for i in R3]


def tr3(A):
    return [[A[j][i] for j in R3] for i in R3]


def det3(M):
    return (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1]) - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
            + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))


def is_orth(M):
    return mm3(M, tr3(M)) == I3


def cnotTw(om):                          # actTEquiv reflY ≪≫ cnot ≪≫ actTEquiv reflY
    return actT(REFLY, cnot(actT(REFLY, om)))


def gateOf(tau, om):
    return cnotTw(om) if tau else cnot(om)


def bellOf(A, B):
    return actC(A, actT(B, PHIW))


def Theta(A02, B02, A13, B13, g):
    return tabMul(tabMul(bellOf(A02, B02), g), tabT(bellOf(A13, B13)))


def Ngate(A, B, A1, B1, om):             # NClass form
    return actC(A, actT(B, cnot(actC(A1, actT(B1, om)))))


def unit(i, j):
    U = zeros4()
    U[i][j] = Fr(1)
    return U


UNITS = [unit(i, j) for i in R4 for j in R4]


def rq():
    return Fr(rng.randint(-5, 5), rng.randint(1, 4))


def rtab():
    return [[rq() for _ in R4] for _ in R4]


def quat_rot(a, b, c, d):                # Euler-Rodrigues, det 1
    n = Fr(a * a + b * b + c * c + d * d)
    return [[Fr(a * a + b * b - c * c - d * d) / n, Fr(2 * (b * c - a * d)) / n, Fr(2 * (b * d + a * c)) / n],
            [Fr(2 * (b * c + a * d)) / n, Fr(a * a - b * b + c * c - d * d) / n, Fr(2 * (c * d - a * b)) / n],
            [Fr(2 * (b * d - a * c)) / n, Fr(2 * (c * d + a * b)) / n, Fr(a * a - b * b - c * c + d * d) / n]]


def rand_rot():
    while True:
        q = [rng.randint(-4, 4) for _ in range(4)]
        if any(q):
            return quat_rot(*q)


def with_det(R, sign):                   # sign -1: compose with a reflection (not reflY, to vary)
    return R if sign == 1 else mm3(R, mat3([[1, 0, 0], [0, 1, 0], [0, 0, -1]]))


def sphere_pt(u, v):                     # inverse stereographic projection: rational unit vector
    u, v = Fr(u), Fr(v)
    n = 1 + u * u + v * v
    return [2 * u / n, 2 * v / n, (u * u + v * v - 1) / n]


def norm2(x):
    return sum(t * t for t in x)


def H4(N):
    out = zeros4()
    out[0][0] = Fr(1)
    for i in R3:
        for j in R3:
            out[i + 1][j + 1] = Fr(N[i][j])
    return out


# T1 matrix-model control
okT1 = True
for _ in range(4):
    Nm = [[rq() for _ in R3] for _ in R3]
    om = rtab()
    okT1 &= actC(Nm, om) == tabMul(H4(Nm), om) and actT(Nm, om) == tabMul(om, tabT(H4(Nm)))
check("T1 literal actC/actT equal H(N).om and om.H(N)^T (random non-orthogonal N)", okT1)

# ------------------------------------------------------------------------------------------------ C1, C2
okC1, ccC1, okC2o, okC2i, ccC2 = True, 0, True, True, 0
detclasses = set()
for trial in range(8):
    sA, sB = (1, -1)[trial % 2], (1, -1)[(trial // 2) % 2]
    A02, B02 = with_det(rand_rot(), sA), with_det(rand_rot(), sB)
    A13, B13 = with_det(rand_rot(), -sB), with_det(rand_rot(), sA)
    detclasses.add((det3(A02), det3(B02)))
    R02, R13 = mm3(mm3(A02, REFLY), tr3(B02)), mm3(mm3(A13, REFLY), tr3(B13))
    tests = UNITS + [rtab() for _ in range(3)]
    for g in tests:
        th = Theta(A02, B02, A13, B13, g)
        okC1 &= th == actC(R02, actT(R13, g))
        ccC1 += th != actC(mm3(A02, tr3(B02)), actT(mm3(A13, tr3(B13)), g))
        okC2i &= actC(tr3(R02), actT(tr3(R13), th)) == g
        ccC2 += actC(R02, actT(R13, th)) != g
    for g in UNITS:
        for h in UNITS:
            okC2o &= ipW(Theta(A02, B02, A13, B13, g), Theta(A02, B02, A13, B13, h)) == ipW(g, h)
check("C1 (G1) Theta = actC (A02 reflY B02^T) . actT (A13 reflY B13^T); det classes of (A02,B02) seen: %d"
      % len(detclasses), okC1 and ccC1 > 0 and len(detclasses) == 4,
      "countercontrol (no reflY) failures: %d" % ccC1)
check("C2 (G2, the note's N9) Theta ipW-orthogonal on all unit pairs and Theta^-1 = actC R02^T . actT R13^T",
      okC2o and okC2i and ccC2 > 0, "countercontrol (R in place of R^T) failures: %d" % ccC2)

# ------------------------------------------------------------------------------------------------ C3 link family
okC3, ccC3 = True, 0
pts = [sphere_pt(*p) for p in [(1, 2), (Fr(1, 3), -1), (-2, Fr(1, 2)), (0, Fr(3, 4)), (5, -3)]]
for trial in range(4):
    A, B = with_det(rand_rot(), (1, -1)[trial % 2]), with_det(rand_rot(), (1, -1)[trial // 2])
    A1, B1 = with_det(rand_rot(), -1), with_det(rand_rot(), 1)
    for x in pts:
        for y in pts[:3]:
            okC3 &= norm2(x) == 1 and norm2(apply3(tr3(A1), x)) == 1
            lhs = Ngate(A, B, A1, B1, prodState(apply3(tr3(A1), x), apply3(tr3(B1), y)))
            okC3 &= lhs == actC(A, actT(B, cnot(prodState(x, y))))
            ccC3 += Ngate(A, B, A1, B1, prodState(apply3(A1, x), apply3(B1, y))) != actC(A, actT(B, cnot(prodState(x, y))))
check("C3 (G7 i) N (prodState (A'^T x) (B'^T y)) = actC A (actT B (cnot (prodState x y))), general unit x, y",
      okC3 and ccC3 > 0, "countercontrol (A' x) failures: %d" % ccC3)


# ------------------------------------------------------------------------------------------------ C4 rotations
def mat_of(f):                           # matrix of a linear map given as a function on vectors
    cols = [f([Fr(int(i == j)) for i in R3]) for j in R3]
    return [[cols[j][i] for j in R3] for i in R3]


def rotFun(c, s, v):                     # ![cos t * v0 - sin t * v1, sin t * v0 + cos t * v1, v2]
    return [c * v[0] - s * v[1], s * v[0] + c * v[1], v[2]]


def cyc(v):
    return [v[2], v[0], v[1]]


def cyc_inv(v):
    return [v[1], v[2], v[0]]


def rot3m(c, s):
    return mat_of(lambda v: rotFun(c, s, v))


def rotXm(c, s):                         # cyc3 * rot3 θ * cyc3⁻¹ ; (e * e') = e ∘ e'
    return mat_of(lambda v: cyc(rotFun(c, s, cyc_inv(v))))


def circ(u):
    u = Fr(u)
    return (1 - u * u) / (1 + u * u), 2 * u / (1 + u * u)


ANG = [circ(u) for u in [Fr(1, 2), Fr(2, 3), Fr(-3), Fr(4, 7), Fr(-1, 6), Fr(0)]]
okC4a, okC4b, okC4p, ccC4 = True, True, True, 0
for (ca, sa) in ANG:
    for (cb, sb) in ANG:
        Ra, Rb = rot3m(ca, sa), rotXm(cb, sb)
        M = mm3(Ra, Rb)
        x, y = apply3(Ra, XPLUS), apply3(Rb, Z3)
        okC4a &= cnot(prodState(x, y)) == actC(M, PHIW)
        okC4b &= actT(mm3(Rb, Ra), PHIW) == actC(M, PHIW)
        okC4p &= apply3(M, Z3) == [sa * sb, -(ca * sb), cb]
        ccC4 += actT(M, PHIW) != actC(M, PHIW)
check("C4 (G7 ii, iii) cnot (prodState (rot3 a xplus) (rotX b z3)) = actC (rot3 a . rotX b) phiW and "
      "actT (rotX b . rot3 a) phiW = actC (rot3 a . rotX b) phiW, 36 pairs; euler_apply_pole reproduced",
      okC4a and okC4b and okC4p and ccC4 > 0, "countercontrol (same order on both sides) failures: %d" % ccC4)

# ------------------------------------------------------------------------------------------------ C5 G8
okC5 = [True] * 4
ccC5a, ccC5b = 0, 0
for trial in range(4):
    sg = [(1, -1)[(trial >> k) & 1] for k in range(2)]
    A02, B02 = with_det(rand_rot(), sg[0]), with_det(rand_rot(), sg[1])
    A13, B13 = with_det(rand_rot(), -sg[1]), with_det(rand_rot(), -sg[0])
    P02, Q02, P13, Q13 = rand_rot(), with_det(rand_rot(), -1), with_det(rand_rot(), -1), rand_rot()  # pre-locals
    b02, b13 = bellOf(A02, B02), bellOf(A13, B13)
    for (ca, sa), (cb, sb) in [(ANG[0], ANG[1]), (ANG[2], ANG[3]), (ANG[4], ANG[1])]:
        Ra, Rb = rot3m(ca, sa), rotXm(cb, sb)
        M, Mp = mm3(Ra, Rb), mm3(Rb, Ra)
        x, y = apply3(Ra, XPLUS), apply3(Rb, Z3)
        L = Ngate(A02, B02, P02, Q02, prodState(apply3(tr3(P02), x), apply3(tr3(Q02), y)))   # in K02 (gate image)
        Lp = Ngate(A13, B13, P13, Q13, prodState(apply3(tr3(P13), x), apply3(tr3(Q13), y)))  # in K13
        for g in UNITS + [rtab()]:
            th = Theta(A02, B02, A13, B13, g)
            left = tabMul(tabMul(L, g), tabT(b13))
            right = tabMul(tabMul(b02, g), tabT(Lp))
            okC5[0] &= left == actC(mm3(mm3(A02, M), tr3(A02)), th)
            okC5[1] &= left == Theta(A02, B02, A13, B13, actC(mm3(mm3(B02, tr3(Mp)), tr3(B02)), g))
            okC5[2] &= right == actT(mm3(mm3(A13, M), tr3(A13)), th)
            okC5[3] &= right == Theta(A02, B02, A13, B13, actT(mm3(mm3(B13, tr3(Mp)), tr3(B13)), g))
            ccC5a += left != actC(mm3(mm3(tr3(A02), M), A02), th)
            ccC5b += left != Theta(A02, B02, A13, B13, actC(mm3(mm3(B02, Mp), tr3(B02)), g))
check("C5 (G8) the four rotated-link identities with links built as gate images of product states "
      "(left/right x control/target side)", all(okC5) and ccC5a > 0 and ccC5b > 0,
      "per identity %s; countercontrol failures %d, %d" % (okC5, ccC5a, ccC5b))

# ------------------------------------------------------------------------------------------------ C6 Lemma R at 02
okC6, ccC6 = True, 0
for _ in range(5):
    X, Y, E, F = rtab(), rtab(), rtab(), rtab()
    fv = fourVal(X, Y, E, F)
    okC6 &= fv == ipW(X, tabMul(tabMul(E, Y), tabT(F))) and fv == ipW(E, tabMul(tabMul(X, F), tabT(Y)))
    # target02.upper (X in K02, Y in K13, E in K01*, F in K23*) is famII (L = X, L' = Y, e = E, f = F)
    okC6 &= ipW(X, tabMul(tabMul(E, Y), tabT(F))) == ipW(E, tabMul(tabMul(X, F), tabT(Y)))
    # target02.lower (L in K01, L' in K23, e in K02*, f in K13*) is famI (X = L, Y = L', E = e, F = f)
    okC6 &= ipW(E, tabMul(tabMul(X, F), tabT(Y))) == ipW(X, tabMul(tabMul(E, Y), tabT(F)))
    ccC6 += fv != ipW(X, tabMul(tabMul(E, Y), F))
check("C6 (O1, O3, target02) fourVal = ipW X (E Y F^T) = ipW E (X F Y^T); target02 fields are famII/famI",
      okC6 and ccC6 > 0, "countercontrol (no transpose) failures: %d" % ccC6)


# ------------------------------------------------------------------------------------------------ C7, C8 parity
def eps_split(A):
    """A = R_A eps_A with eps_A in {I, reflY}, R_A = A eps_A (eps_A is an involution)."""
    eps = REFLY if det3(A) == -1 else I3
    return mm3(A, eps), eps, det3(A) == -1


okC7, ccC7, cls7 = True, 0, set()
for trial in range(8):
    sA, sB = (1, -1)[trial % 2], (1, -1)[(trial // 2) % 2]
    A, B = with_det(rand_rot(), sA), with_det(rand_rot(), sB)
    A1, B1 = with_det(rand_rot(), (1, -1)[trial // 4]), with_det(rand_rot(), -1)
    RA, eA, rA = eps_split(A)
    RB, eB, rB = eps_split(B)
    orient = (det3(A) * det3(B) == -1)
    cls7.add((rA, rB))
    okC7 &= is_orth(RA) and det3(RA) == 1 and is_orth(RB) and det3(RB) == 1 and orient == (rA != rB)
    for s in (1, -1):
        u, v = [s * t for t in XPLUS], [s * t for t in Z3]
        u1, v1 = apply3(tr3(A1), u), apply3(tr3(B1), v)
        for P, P1 in [(prodState(u, v), prodState(u1, v1)), (tens(sharpVec(u), sharpVec(v)), tens(sharpVec(u1), sharpVec(v1)))]:
            img = Ngate(A, B, A1, B1, P1)
            okC7 &= img == actC(A, actT(B, cnot(P)))
            red = actC(tr3(RA), actT(tr3(RB), img))
            okC7 &= red == gateOf(orient, P)
            ccC7 += red != gateOf(not orient, P)
check("C7 (G14) witness reduction for states and effects, s = +-1, all four det classes of (A, B), general pre-locals",
      okC7 and ccC7 > 0 and len(cls7) == 4, "countercontrol failures: %d" % ccC7)

okC8, vals8 = True, set()
for pat in range(16):
    taus = [bool((pat >> k) & 1) for k in range(4)]       # tau01, tau23, tau02, tau13
    wit = []
    for k, tau in enumerate(taus):
        A = with_det(rand_rot(), -1 if tau else 1)
        B = with_det(rand_rot(), 1)
        A1, B1 = rand_rot(), with_det(rand_rot(), -1)
        RA, _, _ = eps_split(A)
        RB, _, _ = eps_split(B)
        s = -1 if k == 3 else 1
        u, v = [s * t for t in XPLUS], [s * t for t in Z3]
        u1, v1 = apply3(tr3(A1), u), apply3(tr3(B1), v)
        base = prodState(u1, v1) if k < 2 else tens(sharpVec(u1), sharpVec(v1))
        wit.append(actC(tr3(RA), actT(tr3(RB), Ngate(A, B, A1, B1, base))))
    X, Y, E, F = wit
    val = ipW(X, tabMul(tabMul(E, Y), tabT(F)))
    odd = sum(taus) % 2 == 1
    vals8.add((odd, val))
    okC8 &= (val < 0) == odd
check("C8 (G14 end to end) famI on the reduced general-chart witnesses is negative exactly at odd patterns",
      okC8, "values (odd, value): %s" % sorted((o, str(v)) for (o, v) in vals8))

# ------------------------------------------------------------------------------------------------ C9
okC9 = True
for _ in range(6):
    Mm = [[rq() for _ in R3] for _ in R3]
    E, X = rtab(), rtab()
    okC9 &= ipW(E, actC(Mm, X)) == ipW(actC(tr3(Mm), E), X) and ipW(E, actT(Mm, X)) == ipW(actT(tr3(Mm), E), X)
    okC9 &= actC(Mm, actT(Mm, X)) == actT(Mm, actC(Mm, X))
okC9 &= all(actC(REFLY, cnot(actC(REFLY, w))) == cnotTw(w) for w in UNITS)
check("C9 (G3, O14) adjoints and actC/actT commutation for random non-orthogonal M; O14 on all units", okC9)


# ------------------------------------------------------------------------------------------------ complex layer
def c(a, b=0):
    return (Fr(a), Fr(b))


C0, C1_ = c(0), c(1)


def cadd(x, y):
    return (x[0] + y[0], x[1] + y[1])


def csub(x, y):
    return (x[0] - y[0], x[1] - y[1])


def cmul(x, y):
    return (x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def cconj(x):
    return (x[0], -x[1])


def cdiv(x, y):
    n = y[0] * y[0] + y[1] * y[1]
    z = cmul(x, cconj(y))
    return (z[0] / n, z[1] / n)


def cm_mul(A, B):
    n, k, m = len(A), len(B), len(B[0])
    out = []
    for i in range(n):
        row = []
        for j in range(m):
            acc = C0
            for t in range(k):
                acc = cadd(acc, cmul(A[i][t], B[t][j]))
            row.append(acc)
        out.append(row)
    return out


def cm_H(A):
    return [[cconj(A[j][i]) for j in range(len(A))] for i in range(len(A[0]))]


def cm_T(A):
    return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]


def cm_tr(A):
    acc = C0
    for i in range(len(A)):
        acc = cadd(acc, A[i][i])
    return acc


def cm_star(A):
    return [[cconj(v) for v in r] for r in A]


SIG = [[[C1_, C0], [C0, C1_]], [[C0, C1_], [C1_, C0]], [[C0, c(0, -1)], [c(0, 1), C0]], [[C1_, C0], [C0, c(-1)]]]
IDX = [(p1, p2) for p1 in range(2) for p2 in range(2)]


def tensorOf(XA, XB):                    # Matrix.of fun p q => XA p.1 q.1 * XB p.2 q.2
    return [[cmul(XA[p[0]][q[0]], XB[p[1]][q[1]]) for q in IDX] for p in IDX]


KR = [[tensorOf(SIG[m], SIG[n]) for n in R4] for m in R4]


def pauliW(om):
    out = [[C0] * 4 for _ in R4]
    for m in R4:
        for n in R4:
            if om[m][n] != 0:
                for i in R4:
                    for j in R4:
                        out[i][j] = cadd(out[i][j], cmul(c(om[m][n] / 4), KR[m][n][i][j]))
    return out


def pureTab(C):
    return [[cm_tr(cm_mul(cm_mul(cm_mul(cm_H(C), SIG[m]), C), cm_T(SIG[n])))[0] for n in R4] for m in R4]


def cdet(M):
    M = [list(r) for r in M]
    n, d = len(M), C1_
    for col in range(n):
        piv = next((r for r in range(col, n) if M[r][col] != C0), None)
        if piv is None:
            return C0
        if piv != col:
            M[col], M[piv] = M[piv], M[col]
            d = cmul(d, c(-1))
        d = cmul(d, M[col][col])
        for r in range(col + 1, n):
            f = cdiv(M[r][col], M[col][col])
            M[r] = [csub(M[r][j], cmul(f, M[col][j])) for j in range(n)]
    return d


def crank(M):
    M = [list(r) for r in M]
    n, m, rank, row = len(M), len(M[0]), 0, 0
    for col in range(m):
        piv = next((r for r in range(row, n) if M[r][col] != C0), None)
        if piv is None:
            continue
        M[row], M[piv] = M[piv], M[row]
        for r in range(n):
            if r != row and M[r][col] != C0:
                f = cdiv(M[r][col], M[row][col])
                M[r] = [csub(M[r][j], cmul(f, M[row][j])) for j in range(m)]
        row += 1
        rank += 1
    return rank


def psd_minors(Hm):
    from itertools import combinations
    for r in range(1, 5):
        for sub in combinations(range(4), r):
            dv = cdet([[Hm[i][j] for j in sub] for i in sub])
            if dv[1] != 0 or dv[0] < 0:
                return False
    return True


def PT2(M):                              # partial transpose on the second tensor factor: (p1,p2),(q1,q2) -> (p1,q2),(q1,p2)
    pos = {p: k for k, p in enumerate(IDX)}
    return [[M[pos[(p[0], q[1])]][pos[(q[0], p[1])]] for q in IDX] for p in IDX]


def rgq():
    return c(Fr(rng.randint(-3, 3), rng.randint(1, 2)), Fr(rng.randint(-3, 3), rng.randint(1, 2)))


def rC():
    return [[rgq(), rgq()], [rgq(), rgq()]]


def vvH(v):
    return [[cmul(v[i], cconj(v[j])) for j in range(len(v))] for i in range(len(v))]


def real_tab_eq(A, B):
    return all(A[m][n] == B[m][n] for m in R4 for n in R4)


# P1
okP1 = True
for _ in range(4):
    E, X = rtab(), rtab()
    okP1 &= cmul(c(4), cm_tr(cm_mul(pauliW(E), pauliW(X)))) == c(ipW(E, X))
for _ in range(4):
    C = rC()
    v = [C[0][0], C[0][1], C[1][0], C[1][1]]
    okP1 &= pauliW(pureTab(C)) == vvH(v)
check("P1 (L1, L2) ipW = 4 Re tr (pauliW E pauliW X) (exactly real); pauliW (pureTab C) = v v^H", okP1)
# P2
okP2, ccP2 = True, 0
for _ in range(6):
    C = rC()
    okP2 &= transposeW(pureTab(C)) == pureTab(cm_star(C))
    ccP2 += transposeW(pureTab(C)) != pureTab(cm_T(C))
check("P2 (L11 i) transposeW (pureTab C) = pureTab (C.map star), 6 Gaussian-rational C", okP2 and ccP2 > 0,
      "countercontrol (C^T) failures: %d" % ccP2)
# P3
okP3 = True
for _ in range(5):
    C = rC()
    okP3 &= actC(REFLY, pureTab(C)) == actT(REFLY, pureTab(cm_star(C)))
    okP3 &= actT(REFLY, actC(REFLY, pureTab(C))) == pureTab(cm_star(C))
okP3 &= all(pauliW(actT(REFLY, w)) == PT2(pauliW(w)) for w in UNITS)
sing = [c(0), c(1), c(-1), c(0)]
neg = cm_mul(cm_mul([[cconj(t) for t in sing]], pauliW(actT(REFLY, PHIW))), [[t] for t in sing])[0][0]
check("P3 (L11 ii, L12 cases) actC reflY (pureTab C) = actT reflY (pureTab C*); actT reflY (actC reflY (pureTab C)) = "
      "pureTab C*; actT reflY is the second-factor partial transpose", okP3 and actT(REFLY, PHIW) == IDW
      and neg[1] == 0 and neg[0] < 0, "countercontrol: singlet expectation of pauliW idW = %s" % neg[0])
# P4
okP4, ccP4 = True, 0
for _ in range(6):
    d0, d1 = rgq(), rgq()
    if d0 == C0 and d1 == C0:
        continue
    n = d0[0] ** 2 + d0[1] ** 2 + d1[0] ** 2 + d1[1] ** 2
    z = cmul(cconj(d0), d1)
    x = [2 * z[0] / n, 2 * z[1] / n, (d0[0] ** 2 + d0[1] ** 2 - d1[0] ** 2 - d1[1] ** 2) / n]
    D = [[d0, C0], [C0, d1]]
    okP4 &= norm2(x) == 1 and pureTab(D) == smul(n, cnot(prodState(x, Z3)))
    if z[1] != 0:
        ccP4 += pureTab(D) != smul(n, cnot(prodState([x[0], -x[1], x[2]], Z3)))
check("P4 (L8) pureTab (diag (d0, d1)) = n cnot (prodState (Bloch (d0, d1)) z3), complex d0, d1", okP4 and ccP4 > 0,
      "countercontrol (conjugate phase) failures: %d" % ccP4)


# P5
def su2(q):                              # U = q0 1 - i (q1 X + q2 Y + q3 Z), unit rational quaternion
    q0, q1, q2, q3 = q
    out = [[C0, C0], [C0, C0]]
    for k, coef in enumerate([c(q0), c(0, -q1), c(0, -q2), c(0, -q3)]):
        for i in range(2):
            for j in range(2):
                out[i][j] = cadd(out[i][j], cmul(coef, SIG[k][i][j]))
    return out


def spinR(U):
    return [[cm_tr(cm_mul(cm_mul(cm_mul(SIG[j + 1], U), SIG[k + 1]), cm_H(U)))[0] / 2 for k in R3] for j in R3]


QS = [(Fr(2, 3), Fr(1, 3), Fr(2, 3), 0), (Fr(1, 2), Fr(-1, 2), Fr(1, 2), Fr(1, 2)),
      (Fr(7, 11), Fr(-6, 11), Fr(0), Fr(6, 11)), (Fr(0), Fr(3, 5), Fr(0), Fr(4, 5))]
okP5, ccP5 = True, 0
Us = [su2(q) for q in QS]
Rs = [spinR(U) for U in Us]
for U, R in zip(Us, Rs):
    okP5 &= cdet(U) == C1_ and cm_mul(U, cm_H(U)) == [[C1_, C0], [C0, C1_]] and is_orth(R) and det3(R) == 1
for iu in range(len(Us)):
    for iv in range(len(Us)):
        C = rC()
        lhs = pureTab(cm_mul(cm_mul(Us[iu], C), cm_T(Us[iv])))
        okP5 &= lhs == actC(Rs[iu], actT(Rs[iv], pureTab(C)))
        ccP5 += lhs != actC(tr3(Rs[iu]), actT(Rs[iv], pureTab(C)))
check("P5 (L4, L6) R_U in SO(3); pureTab (U C V^T) = actC R_U (actT R_V (pureTab C)), 16 pairs", okP5 and ccP5 > 0,
      "countercontrol (R_U^T) failures: %d" % ccP5)

# ------------------------------------------------------------------------------------------------ F1 C_H
gens = [cnot, lambda w: actC(NFLIP, w), lambda w: actT(NFLIP, w)]


def as_imgs(fn):
    return tuple(tuple(tuple(r) for r in fn(u)) for u in UNITS)


def apply_imgs(imgs, om):
    out = zeros4()
    for k in range(16):
        cf = om[k // 4][k % 4]
        if cf != 0:
            out = add(out, smul(cf, [list(r) for r in imgs[k]]))
    return out


ident = as_imgs(lambda w: w)
group, frontier = {ident}, [ident]
while frontier:
    nxt = []
    for g in frontier:
        for h in gens:
            comp = tuple(tuple(tuple(r) for r in h([list(r) for r in g[k]])) for k in range(16))
            if comp not in group:
                group.add(comp)
                nxt.append(comp)
    frontier = nxt
RH = mat3([[0, 0, 1], [0, -1, 0], [1, 0, 0]])
psi1 = actT(RH, PHIW)


def certificate(target):
    """True iff every h(target), h in H, has zero local parts and an orthogonal correlation block, target_00 = 1 and
    ipW target target = 4; then W = 2 e00 - target is >= 0 on H.products and = -2 on target."""
    if target[0][0] != 1 or ipW(target, target) != 4:
        return False
    for g in group:
        t = apply_imgs(g, target)
        if any(t[0][j] != 0 for j in (1, 2, 3)) or any(t[i][0] != 0 for i in (1, 2, 3)):
            return False
        Tm = [[t[i + 1][j + 1] for j in R3] for i in R3]
        if not is_orth(Tm):
            return False
    return True


orth_ok = True
for g in group:
    for a in UNITS:
        for b in UNITS:
            orth_ok &= ipW(apply_imgs(g, a), apply_imgs(g, b)) == ipW(a, b)
    orth_ok &= apply_imgs(g, IDW)[0][0] == 1 and all(apply_imgs(g, u)[0][0] == (1 if u == unit(0, 0) else 0) for u in UNITS)
Wt = add(smul(Fr(2), unit(0, 0)), smul(Fr(-1), psi1))
spot = True
for g in group:
    for x in pts[:3] + [[Fr(1, 2), Fr(0), Fr(-1, 3)]]:
        for y in pts[2:] + [[Fr(0), Fr(0), Fr(0)]]:
            spot &= ipW(Wt, apply_imgs(g, prodState(x, y))) >= 0
f1 = (len(group) == 8 and orth_ok and certificate(psi1) and ipW(Wt, psi1) == -2 and spot
      and is_orth(RH) and det3(RH) == 1 and PHIW == cnot(prodState(XPLUS, Z3)))
check("F1 C_H exclusion by a linear witness: |H| = %d; h ipW-orthogonal, fixing e00; h(psi1) local parts 0 and "
      "orthogonal block for all h; W = 2 e00 - psi1 >= 0 on spot generators, = -2 on psi1" % len(group),
      f1 and not certificate(PHIW) and not certificate(prodState(XPLUS, Z3)),
      "countercontrol: certificate(phiW) = %s, certificate(product) = %s"
      % (certificate(PHIW), certificate(prodState(XPLUS, Z3))))

# ------------------------------------------------------------------------------------------------ F2, F3
sigma = add(smul(Fr(3, 4), prodState(XPLUS, Z3)), smul(Fr(1, 4), prodState(Z3, Z3)))
rho = cnot(sigma)
rhop = actT(RH, rho)
Pr_ = pauliW(rhop)
d_a = cdet(PT2(Pr_))
d_b = cdet(PT2(pauliW(cnot(rhop))))
d_c = cdet(PT2(pauliW(sigma)))
f2 = (psd_minors(Pr_) and crank(Pr_) == 2 and d_a[1] == 0 and d_a[0] < 0 and d_b[1] == 0 and d_b[0] < 0)
check("F2 convexity foil: rho' PSD rank 2; det PT_2 pauliW rho' < 0 and det PT_2 pauliW (cnot rho') < 0; control: "
      "sigma PPT", f2 and psd_minors(PT2(pauliW(sigma))),
      "dets %s, %s; control det %s" % (d_a[0], d_b[0], d_c[0]))
dpsi = cdet(pauliW(psi1))
check("F3 closedness foil: det pauliW psi1 = 0 (psi1 not positive definite); phiW = cnot (prodState xplus z3)",
      dpsi == C0 and crank(pauliW(psi1)) == 1 and PHIW == cnot(prodState(XPLUS, Z3)))

# ------------------------------------------------------------------------------------------------ B1, B2
import sympy as sp  # noqa: E402

w = [[sp.Symbol("w%d%d" % (m, n)) for n in R4] for m in R4]


def pairVal(a, b, om):
    return sum(a[m] * om[m][n] * b[n] for m in R4 for n in R4)


def sv(b):
    return [sp.Rational(1, 2)] + [sp.Rational(v) / 2 for v in b]


okB1 = True
for i in R3:
    for k in R3:
        ei = [int(t == i) for t in R3]
        ek = [int(t == k) for t in R3]
        mi, mk = [-t for t in ei], [-t for t in ek]
        okB1 &= sp.expand(pairVal(sv(ei), sv(ek), w) + pairVal(sv(mi), sv(mk), w) - (w[0][0] + w[i + 1][k + 1]) / 2) == 0
        okB1 &= sp.expand(pairVal(sv(ei), sv(mk), w) + pairVal(sv(mi), sv(ek), w) - (w[0][0] - w[i + 1][k + 1]) / 2) == 0
        for s in (1, -1):
            si = [s * t for t in ei]
            okB1 &= sp.expand(pairVal(sv(si), sv(ek), w) + pairVal(sv(si), sv(mk), w) - (w[0][0] + s * w[i + 1][0]) / 2) == 0
            sk = [s * t for t in ek]
            okB1 &= sp.expand(pairVal(sv(ei), sv(sk), w) + pairVal(sv(mi), sv(sk), w) - (w[0][0] + s * w[0][k + 1]) / 2) == 0
check("B1 (B1a) sharp-effect combinations give (w00 +- w_ik)/2, (w00 +- w_i0)/2, (w00 +- w_0k)/2 symbolically", okB1)

okB2, ccB2 = True, 0
for _ in range(4):
    X, Y, E, F = rtab(), rtab(), rtab(), rtab()
    # famI: sum E_{mu nu} F_{ka la} PB.prodEff(tabCoord mu nu)(tabCoord ka la) at PA.prodState X Y,
    # tok (PB -> PA): = PA.prodEff(tabCoord mu ka)(tabCoord nu la) = X_{mu ka} Y_{nu la}
    famI = sum(E[m][n] * F[k][l] * X[m][k] * Y[n][l] for m in R4 for n in R4 for k in R4 for l in R4)
    okB2 &= famI == fourVal(X, Y, E, F) == ipW(X, tabMul(tabMul(E, Y), tabT(F)))
    # famII: sum e_{mu nu} f_{ka la} PA.prodEff(tabCoord mu nu)(tabCoord ka la) at PB.prodState L L',
    # tok (PA -> PB): = PB.prodEff(tabCoord mu ka)(tabCoord nu la) = L_{mu ka} L'_{nu la}
    e, f, L, Lp = X, Y, E, F
    famII = sum(e[m][n] * f[k][l] * L[m][k] * Lp[n][l] for m in R4 for n in R4 for k in R4 for l in R4)
    okB2 &= famII == fourVal(e, f, L, Lp) == ipW(e, tabMul(tabMul(L, f), tabT(Lp)))
    wrong = sum(E[m][n] * F[k][l] * X[m][n] * Y[k][l] for m in R4 for n in R4 for k in R4 for l in R4)
    ccB2 += wrong != famI
check("B2 (B1e) tok-converted expansions equal fourVal and O1 for famI and famII", okB2 and ccB2 > 0,
      "countercontrol (no tok regrouping) failures: %d" % ccB2)

print("--- review_checks: %d/%d checks pass" % (sum(RES), len(RES)))
print("VERDICT REVIEW-CHECKS-EXACT" if all(RES) else "VERDICT NOT RENDERED")
