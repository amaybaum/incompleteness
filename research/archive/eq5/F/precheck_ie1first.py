"""EQ4-F proof-completion design: exact pre-checks for the IE1-first route of Theorem C (research only).

Usage:  python3 -I -B precheck_ie1first.py <base>/verification/lean-mathlib/OIBridge

Tables are 4x4 real matrices Om[mu][nu] (row = first token).  Kernel conventions, read from the base:
  actT N om = om . H(N)^T,  actC N om = H(N) . om,  H(N) = homMap N = diag(1, N);
  prodState x y = hom x (outer) hom y;  phiW = diag(1, 1, -1, 1) = H(reflY);  cnot = the signed permutation
  (sgn, pc, pt) of CompositeDimension;  rot3 t rotates the first two coordinates;  rotX = cyc3 . rot3 . cyc3^-1.

DECISION RULE (fixed before the first run; rules, not expected numbers).  Print `VERDICT IE1FIRST-PRECHECK-EXACT` iff
every check passes; otherwise `VERDICT NOT RENDERED`.  Exact rationals throughout (rational points on circles via the
Pythagorean parametrization; rational orthogonal matrices via the Cayley transform).
  K0  transcription: sgn, pc, pt parsed from the base file equal the transcription used here.
  M1  control family: for 6 rational equatorial unit x = (c, s, 0), cnot(prodState x z3) . phiW is diag(1, R) with R
      the z-rotation with (cos, sin) = (c, s) [so cnot(prodState x z3) = actC (rot3 phi) phiW].
  M2  target family: for 6 rational unit y = (0, s, c), cnot(prodState xplus y) . phiW is diag(1, R) with R a rotation
      about the first axis (R e1 = e1, det R = 1).
  M3  combined: for 36 pairs (x, y) of M1 x M2 vectors, cnot(prodState x y) . phiW = diag(1, R) with R in SO(3) and
      R = R_M1(x) . R_M2(y).
  M4  countercontrol: a non-equatorial unit x (z-component 3/5) gives cnot(prodState x z3) . phiW not of the form
      diag(1, R) with R orthogonal.
  M5  Theta identity: for 4 random rational orthogonal A02, B02, A13, B13 (det signs mixed), on all 16 units g,
      bellOf02 . g . bellOf13^T = actC (A02 reflY B02^T) (actT (A13 reflY B13^T) g); countercontrol: without reflY it
      fails.
  M6  control-side rotated links: with L = actC A02 (actT B02 (actC R phiW)), L . g . bellOf13^T =
      actC (A02 R A02^T) (Theta g) on all units; countercontrol: actC (A02^T R A02) fails.
  M7  target-side rotated links: with L = actC A02 (actT B02 (actT R phiW)), L . g . bellOf13^T =
      Theta (actC (B02 R^T B02^T) g) on all units.
  M8  Theta is orthogonal for ipW on all pairs of units.
  M9  N-CLASS Bell data: N = actC A (actT B (cnot (actC A' (actT B' w)))): N (prodState (A'^T xplus) (B'^T z3)) =
      bellOf A B and N (tens (sharpVec (A'^T xplus)) (sharpVec (B'^T z3))) = (1/4) bellOf A B; N is ipW-orthogonal.
  M10 link family: N (prodState (A'^T x) (B'^T y)) = actC A (actT B (cnot (prodState x y))) for M3's (x, y).
  M11 orientation bookkeeping: det(A reflY B^T) = -det A det B for the M5 matrices.
"""
import random
import re
import sys
from fractions import Fraction as Fr
from itertools import product

BASE = sys.argv[1]
rng = random.Random(20261009)
RES = []


def check(name, ok, detail=""):
    RES.append(bool(ok))
    print("%s %s%s" % ("PASS" if ok else "FAIL", name, (" -- " + detail) if detail else ""), flush=True)


# ------------------------------------------------------------------------------------------------ linear algebra
def mm(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]


def tr_(A):
    return [list(r) for r in zip(*A)]


def eye(n):
    return [[Fr(int(i == j)) for j in range(n)] for i in range(n)]


def det3(M):
    return (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1]) - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
            + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))


def H(N):
    out = [[Fr(0)] * 4 for _ in range(4)]
    out[0][0] = Fr(1)
    for i in range(3):
        for j in range(3):
            out[i + 1][j + 1] = Fr(N[i][j])
    return out


def actC(N, om):
    return mm(H(N), om)


def actT(N, om):
    return mm(om, tr_(H(N)))


def hom(x):
    return [Fr(1)] + [Fr(v) for v in x]


def prodState(x, y):
    hx, hy = hom(x), hom(y)
    return [[hx[m] * hy[n] for n in range(4)] for m in range(4)]


def sharpVec(b):
    return [Fr(1, 2)] + [Fr(v) / 2 for v in b]


def tens(a, b):
    return [[a[m] * b[n] for n in range(4)] for m in range(4)]


def ipW(E, X):
    return sum(E[m][n] * X[m][n] for m in range(4) for n in range(4))


def unit(i, j):
    U = [[Fr(0)] * 4 for _ in range(4)]
    U[i][j] = Fr(1)
    return U


reflY = [[Fr(1), Fr(0), Fr(0)], [Fr(0), Fr(-1), Fr(0)], [Fr(0), Fr(0), Fr(1)]]
phiW = H(reflY)
xplus = [Fr(1), Fr(0), Fr(0)]
z3 = [Fr(0), Fr(0), Fr(1)]

# ------------------------------------------------------------------------------------------- kernel cnot tables
SGN = lambda m, n: Fr(-1) if (m == 1 and n == 3) or (m == 2 and n == 2) else Fr(1)  # noqa: E731
PC = [[0, 0, 3, 3], [1, 1, 2, 2], [2, 2, 1, 1], [3, 3, 0, 0]]
PT = [[0, 1, 2, 3], [1, 0, 3, 2], [1, 0, 3, 2], [0, 1, 2, 3]]
src = open(BASE + "/CompositeDimension.lean").read()


def parse_table(name):
    m = re.search(r"def %s : Fin 4 → Fin 4 → Fin 4\n((?:  \|.*\n){4})" % name, src)
    rows = []
    for line in m.group(1).strip().splitlines():
        vals = [int(v) for v in re.findall(r"=> (\d)", line)]
        rows.append(vals)
    return rows


sgn_line = re.search(r"def sgn \(μ ν : Fin 4\) : ℝ := (.*)", src).group(1).strip()
ok_k0 = (parse_table("pc") == PC and parse_table("pt") == PT
         and sgn_line == "if (μ = 1 ∧ ν = 3) ∨ (μ = 2 ∧ ν = 2) then -1 else 1")
check("K0 transcription of sgn, pc, pt from the base", ok_k0)


def cnot(om):
    return [[SGN(m, n) * om[PC[m][n]][PT[m][n]] for n in range(4)] for m in range(4)]


def circ(u):
    u = Fr(u)
    return (1 - u * u) / (1 + u * u), 2 * u / (1 + u * u)


def block_R(M):
    """If M = diag(1, R), return R; else None."""
    if M[0][0] != 1 or any(M[0][j] != 0 for j in range(1, 4)) or any(M[i][0] != 0 for i in range(1, 4)):
        return None
    return [[M[i + 1][j + 1] for j in range(3)] for i in range(3)]


def is_SO3(R):
    return R is not None and mm(R, tr_(R)) == eye(3) and det3(R) == 1


def rotz(c, s):
    return [[c, -s, Fr(0)], [s, c, Fr(0)], [Fr(0), Fr(0), Fr(1)]]


# M1
us = [Fr(1, 2), Fr(1, 3), Fr(2), Fr(-3, 4), Fr(5, 7), Fr(-1, 5)]
ok_m1, R1s = True, []
for u in us:
    c, s = circ(u)
    x = [c, s, Fr(0)]
    R = block_R(mm(cnot(prodState(x, z3)), phiW))
    R1s.append((x, R))
    ok_m1 &= R is not None and R == rotz(c, s)
check("M1 control family: cnot(prodState x z3) = actC (z-rotation x) phiW for 6 equatorial x", ok_m1)
# M2
ok_m2, R2s = True, []
for u in us:
    c, s = circ(u)
    y = [Fr(0), s, c]
    R = block_R(mm(cnot(prodState(xplus, y)), phiW))
    R2s.append((y, R))
    ok_m2 &= is_SO3(R) and [R[i][0] for i in range(3)] == [1, 0, 0] and R[0] == [1, 0, 0]
check("M2 target family: cnot(prodState xplus y) = actC R phiW, R a rotation about the first axis, 6 y", ok_m2,
      "example R = %s" % [[str(v) for v in r] for r in R2s[0][1]])
# M3
ok_m3 = True
for (x, Ra) in R1s:
    for (y, Rb) in R2s:
        R = block_R(mm(cnot(prodState(x, y)), phiW))
        ok_m3 &= is_SO3(R) and R == mm(Ra, Rb)
check("M3 combined: cnot(prodState x y) = actC (R1(x) R2(y)) phiW, R in SO(3), 36 pairs", ok_m3)
# M4
xn = [Fr(4, 5), Fr(0), Fr(3, 5)]
Rn = block_R(mm(cnot(prodState(xn, z3)), phiW))
check("M4 countercontrol: non-equatorial x gives no orthogonal block", Rn is None or mm(Rn, tr_(Rn)) != eye(3))


def cayley(a, b, c):
    """Rational rotation from the Cayley transform of the skew matrix (a, b, c)."""
    S = [[Fr(0), -Fr(c), Fr(b)], [Fr(c), Fr(0), -Fr(a)], [-Fr(b), Fr(a), Fr(0)]]
    I3 = eye(3)
    Mm = [[I3[i][j] - S[i][j] for j in range(3)] for i in range(3)]
    Mp = [[I3[i][j] + S[i][j] for j in range(3)] for i in range(3)]
    # inverse of Mp by adjugate
    d = det3(Mp)
    adj = [[(Mp[(j + 1) % 3][(i + 1) % 3] * Mp[(j + 2) % 3][(i + 2) % 3]
             - Mp[(j + 1) % 3][(i + 2) % 3] * Mp[(j + 2) % 3][(i + 1) % 3]) for j in range(3)] for i in range(3)]
    inv = [[adj[i][j] / d for j in range(3)] for i in range(3)]
    return mm(Mm, inv)


def rand_orth():
    R = cayley(Fr(rng.randint(-4, 4), rng.randint(1, 3)), Fr(rng.randint(-4, 4), rng.randint(1, 3)),
               Fr(rng.randint(-4, 4), rng.randint(1, 3)))
    if rng.random() < 0.5:
        R = mm(R, reflY)
    return R


def bellOf(A, B):
    return actC(A, actT(B, phiW))


ok_m5, fail_m5c, ok_m6, fail_m6c, ok_m7, ok_m8, ok_m11 = True, 0, True, 0, True, True, True
for trial in range(4):
    A02, B02, A13, B13 = rand_orth(), rand_orth(), rand_orth(), rand_orth()
    b02, b13 = bellOf(A02, B02), bellOf(A13, B13)
    R02, R13 = mm(mm(A02, reflY), tr_(B02)), mm(mm(A13, reflY), tr_(B13))
    ok_m11 &= det3(R02) == -det3(A02) * det3(B02) and det3(R13) == -det3(A13) * det3(B13)

    def Theta(g):
        return mm(mm(b02, g), tr_(b13))

    units = [unit(i, j) for i in range(4) for j in range(4)]
    for g in units:
        ok_m5 &= Theta(g) == actC(R02, actT(R13, g))
        fail_m5c += Theta(g) != actC(mm(A02, tr_(B02)), actT(mm(A13, tr_(B13)), g))
    Rr = cayley(Fr(1, 2), Fr(-1, 3), Fr(2, 5))
    L = actC(A02, actT(B02, actC(Rr, phiW)))
    Lt = actC(A02, actT(B02, actT(Rr, phiW)))
    for g in units:
        lhs = mm(mm(L, g), tr_(b13))
        ok_m6 &= lhs == actC(mm(mm(A02, Rr), tr_(A02)), Theta(g))
        fail_m6c += lhs != actC(mm(mm(tr_(A02), Rr), A02), Theta(g))
        ok_m7 &= mm(mm(Lt, g), tr_(b13)) == Theta(actC(mm(mm(B02, tr_(Rr)), tr_(B02)), g))
    for g in units:
        for h in units:
            ok_m8 &= ipW(Theta(g), Theta(h)) == ipW(g, h)
check("M5 Theta = actC (A02 reflY B02^T) . actT (A13 reflY B13^T) on all units (4 draws); without reflY it fails",
      ok_m5 and fail_m5c > 0, "%d unit failures for the countercontrol" % fail_m5c)
check("M6 control-side rotated link = actC (A02 R A02^T) . Theta; the conjugation in the other order fails",
      ok_m6 and fail_m6c > 0, "%d unit failures for the countercontrol" % fail_m6c)
check("M7 target-side rotated link = Theta . actC (B02 R^T B02^T)", ok_m7)
check("M8 Theta is ipW-orthogonal on all 256 unit pairs (4 draws)", ok_m8)
# M9, M10
ok_m9, ok_m10 = True, True
for trial in range(4):
    A, B, A1, B1 = rand_orth(), rand_orth(), rand_orth(), rand_orth()

    def N(w):
        return actC(A, actT(B, cnot(actC(A1, actT(B1, w)))))

    x0 = [sum(A1[k][i] * xplus[k] for k in range(3)) for i in range(3)]   # A1^T xplus
    y0 = [sum(B1[k][i] * z3[k] for k in range(3)) for i in range(3)]      # B1^T z3
    ok_m9 &= N(prodState(x0, y0)) == bellOf(A, B)
    ok_m9 &= N(tens(sharpVec(x0), sharpVec(y0))) == [[v / 4 for v in r] for r in bellOf(A, B)]
    units = [unit(i, j) for i in range(4) for j in range(4)]
    for g in units:
        for h in units:
            ok_m9 &= ipW(N(g), N(h)) == ipW(g, h)
    for (x, _) in R1s[:3]:
        for (y, _) in R2s[:3]:
            xa = [sum(A1[k][i] * x[k] for k in range(3)) for i in range(3)]
            yb = [sum(B1[k][i] * y[k] for k in range(3)) for i in range(3)]
            ok_m10 &= N(prodState(xa, yb)) == actC(A, actT(B, cnot(prodState(x, y))))
check("M9 N-CLASS Bell state, Bell effect (1/4) and ipW-orthogonality (4 draws)", ok_m9)
check("M10 link family: N (prodState (A'^T x) (B'^T y)) = actC A (actT B (cnot (prodState x y)))", ok_m10)
check("M11 det(A reflY B^T) = -det A det B", ok_m11)
print("--- precheck_ie1first: %d/%d checks pass" % (sum(RES), len(RES)))
print("VERDICT IE1FIRST-PRECHECK-EXACT" if all(RES) else "VERDICT NOT RENDERED")
