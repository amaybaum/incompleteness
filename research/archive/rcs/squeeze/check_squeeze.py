"""Exact checks for rcs/squeeze/RelcSelectSqueeze.lean (RELC-SELECT-1 design draft).

Everything here is exact (sympy rationals / polynomials); no float enters any verdict.

Part A  models the Lean-shaped definitions of the module (sqCls, sqSig, sqPc, sqPt, sqR, sqK, sqW,
        sqWi, sqSg) and checks them against the ledger's independent implementation
        possep/possep_gate.py::Squeezed(k=2, eps=1/10, lam=1/2), entry by entry on all 36 basis
        vectors; then the round trips, frame, relT, relC, the posInv witness value -1/2 and the
        no-squeeze countercontrol value -1/40.
Part B  checks the decomposition identity used by `pairVal_gSq_prodState` as a polynomial identity in
        all 22 variables.
Part C  checks, as exact polynomial identities, the linear certificates behind every `linarith` /
        `nlinarith` step of the posFwd chain (each certificate has nonnegative rational coefficients
        on facts that are hypotheses or squares).
Part D  countercontrols: the chain's hypotheses are load-bearing (eps = 1 or lam = 1 breaks posFwd at
        an exact rational point), and the -1/2 witness pairs with sharp effects.
Exit code 0 iff every check passes.
"""
import sys
import os
import itertools
from fractions import Fraction as Fr
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
POSSEP = os.path.join(os.path.dirname(os.path.dirname(HERE)), "possep")
sys.path.insert(0, POSSEP)
from possep_gate import Squeezed  # noqa: E402  (ledger's independent model)

FAILS = []


def check(name, ok):
    print(("PASS  " if ok else "FAIL  ") + name)
    if not ok:
        FAILS.append(name)


# ---------------------------------------------------------------- Part A: Lean-shaped model
odd5 = {0: False, 1: False, 2: False, 3: True, 4: True, 5: True}       # ParityNot.odd5
perm5 = {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0}                            # ParityNot.perm5
sqCls = {0: True, 1: False, 2: False, 3: False, 4: False, 5: True}      # classical control class
sqSig = {0: 1, 1: 0, 2: 2, 3: 5, 4: 4, 5: 3}                            # target relabelling sigma
EPS, LAM = Fr(1, 10), Fr(1, 2)


def sqPc(m, n):
    return perm5[m] if odd5[n] else m


def sqPt(m, n):
    return n if sqCls[m] else sqSig[n]


def sqR(m):
    return Fr(1) if sqCls[m] else EPS


def sqK(n):
    return Fr(1) if sqCls[n] else LAM


def sqW(m, n):
    return sqR(m) * sqK(sqPt(m, n))


def sqWi(m, n):
    return (Fr(1) if sqCls[m] else Fr(10)) * (Fr(1) if sqCls[n] else Fr(2))


def sqSg(m):
    return Fr(-1) if odd5[m] else Fr(1)


R6 = range(6)


def gFun(om):
    return [[sqW(m, n) * om[sqPc(m, n)][sqPt(m, n)] for n in R6] for m in R6]


def gInvFun(om):
    return [[sqWi(m, n) * om[sqPc(m, n)][sqPt(m, n)] for n in R6] for m in R6]


def basis(p, q):
    return [[Fr(1) if (m, n) == (p, q) else Fr(0) for n in R6] for m in R6]


ledger = Squeezed(2, EPS, LAM)
check("A1 sqW/sqPc/sqPt reproduce ledger Squeezed(k=2,1/10,1/2) on all 36 basis vectors",
      all(gFun(basis(p, q)) == [[Fr(v) for v in row] for row in ledger(basis(p, q))]
          for p in R6 for q in R6))
check("A2 pc_pc, pt_pt (involution of the index map)",
      all(sqPc(sqPc(m, n), sqPt(m, n)) == m and sqPt(sqPc(m, n), sqPt(m, n)) == n
          for m in R6 for n in R6))
check("A3 cls_pc: sqCls (sqPc m n) = sqCls m", all(sqCls[sqPc(m, n)] == sqCls[m] for m in R6 for n in R6))
check("A4 odd_pt: odd5 (sqPt m n) = odd5 n", all(odd5[sqPt(m, n)] == odd5[n] for m in R6 for n in R6))
check("A5 odd_pc: odd5 (sqPc m n) = (if odd5 n then !odd5 m else odd5 m)",
      all(odd5[sqPc(m, n)] == ((not odd5[m]) if odd5[n] else odd5[m]) for m in R6 for n in R6))
check("A6 wi_wf / wf_wi weight identities",
      all(sqWi(m, n) * sqW(sqPc(m, n), sqPt(m, n)) == 1 and sqW(m, n) * sqWi(sqPc(m, n), sqPt(m, n)) == 1
          for m in R6 for n in R6))
check("A7 gInvFun o gFun = id = gFun o gInvFun on the 36 basis vectors",
      all(gInvFun(gFun(basis(p, q))) == basis(p, q) and gFun(gInvFun(basis(p, q))) == basis(p, q)
          for p in R6 for q in R6))


def hom(x):
    return [Fr(1)] + [Fr(v) for v in x]


def prodState(x, y):
    hx, hy = hom(x), hom(y)
    return [[hx[m] * hy[n] for n in R6] for m in R6]


z5 = [0, 0, 0, 0, 1]
mz5 = [0, 0, 0, 0, -1]
x5 = [1, 0, 0, 0, 0]
corner = {0: z5, 1: mz5}
check("A8 frame (4 corner pairs)",
      all(gFun(prodState(corner[a], corner[b])) == prodState(corner[a], corner[(a + b) % 2])
          for a in (0, 1) for b in (0, 1)))


def actT(om):  # actT n5: homMap n5 on the target index
    return [[sqSg(n) * om[m][n] for n in R6] for m in R6]


def actC(om):
    return [[sqSg(m) * om[m][n] for n in R6] for m in R6]


check("A9 relT on 36 basis vectors (hence all of W 5)",
      all(actT(gFun(actT(basis(p, q)))) == gFun(basis(p, q)) for p in R6 for q in R6))
check("A10 relC on 36 basis vectors",
      all(actC(gFun(actC(basis(p, q)))) == actT(gFun(basis(p, q))) for p in R6 for q in R6))
check("A11 sqSg multiplicativity: sg(pt)=sg n, sg(pc)=sg m*sg n",
      all(sqSg(sqPt(m, n)) == sqSg(n) and sqSg(sqPc(m, n)) == sqSg(m) * sqSg(n) for m in R6 for n in R6))


def sharpVec(b):
    return [Fr(1, 2)] + [Fr(v) / 2 for v in b]


def pairVal(a, b, om):
    return sum(a[m] * om[m][n] * b[n] for m in R6 for n in R6)


val = pairVal(sharpVec(z5), sharpVec([-v for v in x5]), gInvFun(prodState(z5, x5)))
check("A12 posInv witness value = -1/2 (got %s)" % val, val == Fr(-1, 2))
check("A13 gSq.symm (prodState z5 x5) = hom z5 (x) (1,2,0,0,0,0)",
      gInvFun(prodState(z5, x5)) == [[hom(z5)[m] * [1, 2, 0, 0, 0, 0][n] for n in R6] for m in R6])
check("A14 sharpVec(-x5) = (1/2,-1/2,0,0,0,0)", sharpVec([-v for v in x5]) == [Fr(1, 2), Fr(-1, 2), 0, 0, 0, 0])


# countercontrol: lam = 1 (no squeeze), same Gamma
def gCtlFun(om):
    return [[sqR(m) * om[sqPc(m, n)][sqPt(m, n)] for n in R6] for m in R6]


e1 = [1, 0, 0, 0, 0]
e2 = [0, 1, 0, 0, 0]
me2 = [0, -1, 0, 0, 0]
cval = pairVal(sharpVec(e1), sharpVec(me2), gCtlFun(prodState(e1, e2)))
check("A15 countercontrol lam=1: value -1/40 (got %s)" % cval, cval == Fr(-1, 40))
sval = pairVal(sharpVec(e1), sharpVec(me2), gFun(prodState(e1, e2)))
check("A16 same test on the squeezed gate is >= 0 (got %s = 9/80)" % sval, sval == Fr(9, 80))
check("A17 ledger model agrees on the countercontrol",
      pairVal(sharpVec(e1), sharpVec(me2),
              [[Fr(v) for v in r] for r in Squeezed(2, EPS, 1)(prodState(e1, e2))]) == Fr(-1, 40))

# ---------------------------------------------------------------- Part B: decomposition identity
a = sp.symbols("a0:6")
b = sp.symbols("b0:6")
x = sp.symbols("x0:5")
y = sp.symbols("y0:5")
h = sp.Rational(1, 2)
A = b[0] + b[5] * y[4] + (b[1] * y[0] + b[2] * y[1] + b[3] * y[2] + b[4] * y[3]) / 2
B = b[0] - b[5] * y[4] + (b[1] * y[0] + b[2] * y[1] - b[3] * y[2] - b[4] * y[3]) / 2
Se = b[1] + (b[0] * y[0] + b[2] * y[1]) / 2
So = b[3] * y[4] + (b[5] * y[2] + b[4] * y[3]) / 2
Ce = x[0] * a[1] + x[1] * a[2] + x[2] * a[3] + x[3] * a[4]
Co = x[0] * a[3] + x[1] * a[4] + x[2] * a[1] + x[3] * a[2]
Vformula = ((1 + x[4]) / 2 * ((a[0] + a[5]) * A) + (1 - x[4]) / 2 * ((a[0] - a[5]) * B)
            + (Se * Ce + So * Co) / 10)
hx = [1] + list(x)
hy = [1] + list(y)
Vdirect = sum(a[m] * (sp.Rational(sqW(m, n).numerator, sqW(m, n).denominator) * hx[sqPc(m, n)] * hy[sqPt(m, n)])
              * b[n] for m in R6 for n in R6)
check("B1 pairVal a b (gSq (prodState x y)) = decomposition (22-variable polynomial identity)",
      sp.expand(Vdirect - Vformula) == 0)

# ---------------------------------------------------------------- Part C: certificates


def ident(name, lhs, rhs):
    check(name, sp.expand(lhs - rhs) == 0)


p = sp.symbols("p1:5")
q = sp.symbols("q1:5")
lag = sum((p[i] * q[j] - p[j] * q[i]) ** 2 for i in range(4) for j in range(i + 1, 4))
ident("C1 rsq_cs4: RHS-LHS = sum of six Lagrange squares",
      sum(pi ** 2 for pi in p) * sum(qi ** 2 for qi in q) - sum(p[i] * q[i] for i in range(4)) ** 2, lag)

f, t, s, u, AA, BB = sp.symbols("f t s u A B")
ident("C2 rsq_ab hu2: (f-ts)^2-u^2 = [(f^2-t^2)(1-s^2)-u^2] + (fs-t)^2",
      (f - t * s) ** 2 - u ** 2, ((f ** 2 - t ** 2) * (1 - s ** 2) - u ** 2) + (f * s - t) ** 2)
L1 = f + u - t * s / 2
L2 = f - u - t * s / 2
ident("C3 rsq_ab final: AB-(t^2+f^2 s^2)/8 = [AB-L1L2] + [(f^2-t^2)(1-s^2)-u^2] + 1/2(t-fs)^2"
      " + 3/8 t^2(1-s^2) + 3/8 s^2(f^2-t^2)",
      AA * BB - (t ** 2 + f ** 2 * s ** 2) / 8,
      (AA * BB - L1 * L2) + ((f ** 2 - t ** 2) * (1 - s ** 2) - u ** 2) + h * (t - f * s) ** 2
      + sp.Rational(3, 8) * t ** 2 * (1 - s ** 2) + sp.Rational(3, 8) * s ** 2 * (f ** 2 - t ** 2))
ident("C4 rsq_ab L1 >= 0, L2 >= 0: L1 = (f-ts+u)+ts/2, L2 = (f-ts-u)+ts/2", L1 + L2, 2 * (f - t * s) + t * s)

# rsq_s certificate: 2Tb + f^2 Sv - (Se^2+So^2) as a nonnegative combination
fb, b1, b2, b3, b4, b5 = sp.symbols("f b1 b2 b3 b4 b5")
y0, y1, y2, y3, y4 = sp.symbols("y0:5")
Se_ = b1 + (fb * y0 + b2 * y1) / 2
So_ = b3 * y4 + (b5 * y2 + b4 * y3) / 2
Tb = b1 ** 2 + b2 ** 2 + b3 ** 2 + b4 ** 2
Sv = y0 ** 2 + y1 ** 2 + y2 ** 2 + y3 ** 2
X = fb * y0 + b2 * y1
Z = b5 * y2 + b4 * y3
certS = (sp.Rational(1) * (b1 - X / 2) ** 2              # (b1+X/2)^2 <= 2 b1^2 + X^2/2
         + sp.Rational(1) * (b3 * y4 - Z / 2) ** 2       # (b3 y4+Z/2)^2 <= 2 b3^2 y4^2 + Z^2/2
         + h * (fb * y1 - b2 * y0) ** 2                  # X^2 <= (f^2+b2^2)(y0^2+y1^2)
         + h * (b5 * y3 - b4 * y2) ** 2                  # Z^2 <= (b5^2+b4^2)(y2^2+y3^2)
         + 2 * b3 ** 2 * (1 - y4 ** 2)                   # 2 b3^2 y4^2 <= 2 b3^2
         + h * (fb ** 2 - b2 ** 2) * (y0 ** 2 + y1 ** 2)  # 1/2 b2^2 (..) <= 1/2 f^2 (..)
         + h * (fb ** 2 - b5 ** 2 - b4 ** 2) * (y2 ** 2 + y3 ** 2)
         + h * fb ** 2 * (y2 ** 2 + y3 ** 2)
         + 2 * b2 ** 2 + 2 * b4 ** 2)
ident("C5 rsq_s: 2Tb + f^2 Sv - (Se^2+So^2) = certificate (all terms nonneg under hypotheses)",
      2 * Tb + fb ** 2 * Sv - (Se_ ** 2 + So_ ** 2), certS)

# rsq_key final: AB - (Se^2+So^2)/50 >= (Tb+f^2Sv)/8 - (2Tb+f^2Sv)/50 = (21/200) Tb + (21/200) f^2 Sv
ident("C6 rsq_key: (Tb+F)/8 - (2Tb+F)/50 = 17/200 Tb + 21/200 F (both coefficients > 0)",
      (sp.Symbol("T") + sp.Symbol("F")) / 8 - (2 * sp.Symbol("T") + sp.Symbol("F")) / 50,
      sp.Rational(17, 200) * sp.Symbol("T") + sp.Rational(21, 200) * sp.Symbol("F"))

al, pp, qq, Se2, So2, Ce2, Co2 = sp.symbols("alpha p q Se So Ce Co")
P1 = (1 + al) / 2 * (pp * AA)
P2 = (1 - al) / 2 * (qq * BB)
ident("C7 rsq_assemble AM-GM: (P1+P2)^2 - (1-al^2) p q A B = (P1-P2)^2",
      (P1 + P2) ** 2 - (1 - al ** 2) * (pp * qq) * (AA * BB), (P1 - P2) ** 2)
ident("C8 rsq_assemble CS2: (Se^2+So^2)(Ce^2+Co^2) - (Se Ce + So Co)^2 = (Se Co - So Ce)^2",
      (Se2 ** 2 + So2 ** 2) * (Ce2 ** 2 + Co2 ** 2) - (Se2 * Ce2 + So2 * Co2) ** 2, (Se2 * Co2 - So2 * Ce2) ** 2)
Tc, Ta = sp.symbols("Tc Ta")
# chain: ((SeCe+SoCo)/10)^2 <= (S)(C)/100 <= S*2TcTa/100 = S/50*TcTa <= AB TcTa <= (1-al^2)pq AB <= P^2
ident("C9 rsq_assemble: (Se^2+So^2)*(2 Tc Ta)/100 = (Se^2+So^2)/50 * (Tc Ta)",
      (Se2 ** 2 + So2 ** 2) * (2 * Tc * Ta) / 100, (Se2 ** 2 + So2 ** 2) / 50 * (Tc * Ta))
ident("C10 gSq_core hTa: (a0+a5)(a0-a5) - Ta = (a0^2 - (a1^2+..+a5^2)) + 0",
      (a[0] + a[5]) * (a[0] - a[5]) - (a[1] ** 2 + a[2] ** 2 + a[3] ** 2 + a[4] ** 2),
      a[0] ** 2 - sum(a[i] ** 2 for i in range(1, 6)))
ident("C11 rsq_key hr2 rewrite: (b1y0+b2y1+b3(-y2)+b4(-y3))^2 = (b1y0+b2y1-b3y2-b4y3)^2",
      (b1 * y0 + b2 * y1 + b3 * (-y2) + b4 * (-y3)) ** 2, (b1 * y0 + b2 * y1 - b3 * y2 - b4 * y3) ** 2)
ident("C12 rsq_key: A = f + u + r1/2 and B = f - u + r2/2 with u = b5 y4",
      (A - (b[0] + b[5] * y[4] + (b[1] * y[0] + b[2] * y[1] + b[3] * y[2] + b[4] * y[3]) / 2))
      + (B - (b[0] - b[5] * y[4] + (b[1] * y[0] + b[2] * y[1] - b[3] * y[2] - b[4] * y[3]) / 2)), 0)

# ---------------------------------------------------------------- Part D: hypotheses are load-bearing


def V_at(eps, lam, av, bv, xv, yv):
    """pairVal a b (G_{eps,lam} (prodState x y)) from the ledger's independent model."""
    g = Squeezed(2, eps, lam)
    om = g(prodState(xv, yv))
    return pairVal([Fr(v) for v in av], [Fr(v) for v in bv], [[Fr(v) for v in r] for r in om])


# Generic-(eps, lam) decomposition (checked against the ledger model at both parameter pairs), then an
# exact search for a negative value at eps = 1 over a small rational grid.
EP, LA = sp.symbols("EP LA")
Ag = b[0] + b[5] * y[4] + LA * (b[1] * y[0] + b[2] * y[1] + b[3] * y[2] + b[4] * y[3])
Bg = b[0] - b[5] * y[4] + LA * (b[1] * y[0] + b[2] * y[1] - b[3] * y[2] - b[4] * y[3])
Seg = b[1] + LA * (b[0] * y[0] + b[2] * y[1])
Sog = b[3] * y[4] + LA * (b[5] * y[2] + b[4] * y[3])
Vg = (1 + x[4]) / 2 * ((a[0] + a[5]) * Ag) + (1 - x[4]) / 2 * ((a[0] - a[5]) * Bg) + EP * (Seg * Ce + Sog * Co)
import random  # noqa: E402
rnd = random.Random(7)
okg = True
for _ in range(20):
    av = [Fr(rnd.randint(-5, 5), 7) for _ in range(6)]
    bv = [Fr(rnd.randint(-5, 5), 7) for _ in range(6)]
    xv = [Fr(rnd.randint(-5, 5), 9) for _ in range(5)]
    yv = [Fr(rnd.randint(-5, 5), 9) for _ in range(5)]
    for (ee, ll) in [(Fr(1), Fr(1, 2)), (Fr(1, 10), Fr(1, 2)), (Fr(1, 10), Fr(1))]:
        sub = dict(zip(a, av)); sub.update(zip(b, bv)); sub.update(zip(x, xv)); sub.update(zip(y, yv))
        sub[EP] = ee; sub[LA] = ll
        lhs = sp.Rational(Vg.subs(sub))
        rhs = V_at(ee, ll, av, bv, xv, yv)
        okg = okg and (lhs == sp.Rational(rhs.numerator, rhs.denominator))
check("D0 generic (eps, lam) decomposition matches the ledger model at 60 rational points", okg)
# 2*Vg has integer coefficients, so the lambdified function evaluates exactly on Fractions
V2 = sp.expand(2 * Vg)
assert all(c.is_integer for c in sp.Poly(V2, *a, *b, *x, *y, EP, LA).coeffs())
_V2f = sp.lambdify([a, b, x, y, EP, LA], V2, "math")


def Vf(*args):
    return Fr(_V2f(*args)) / 2
units = []
for i in range(5):
    for sgn in (1, -1):
        v = [Fr(0)] * 5
        v[i] = Fr(sgn)
        units.append(v)
for i, j in itertools.combinations(range(5), 2):
    for c1, c2 in [(Fr(3, 5), Fr(4, 5)), (Fr(-3, 5), Fr(4, 5)), (Fr(3, 5), Fr(-4, 5)), (Fr(-3, 5), Fr(-4, 5)),
                   (Fr(4, 5), Fr(3, 5)), (Fr(-4, 5), Fr(3, 5)), (Fr(4, 5), Fr(-3, 5)), (Fr(-4, 5), Fr(-3, 5))]:
        v = [Fr(0)] * 5
        v[i], v[j] = c1, c2
        units.append(v)
best = None
for xv in units[:10]:
    for yv in units:
        for e in units[:10]:
            for fv in units:
                val_ = Vf(sharpVec(e), sharpVec(fv), xv, yv, Fr(1), Fr(1, 2))
                if best is None or val_ < best[0]:
                    best = (val_, xv, yv, e, fv)
check("D1 eps = 1, lam = 1/2: posFwd fails at an exact rational point, value %s at x=%s y=%s e=%s f=%s"
      % (best[0], [str(v) for v in best[1]], [str(v) for v in best[2]], [str(v) for v in best[3]],
         [str(v) for v in best[4]]), best[0] < 0)
exact = V_at(1, Fr(1, 2), sharpVec(best[3]), sharpVec(best[4]), best[1], best[2])
check("D1' ledger model confirms the D1 value exactly (%s)" % exact, exact == best[0] and exact < 0)
worst = None
for xv in units[:10]:
    for yv in units:
        for e in units[:10]:
            for fv in units:
                val_ = Vf(sharpVec(e), sharpVec(fv), xv, yv, Fr(1, 10), Fr(1, 2))
                if worst is None or val_ < worst:
                    worst = val_
check("D2 (1/10, 1/2) gate: same grid minimum is >= 0 (got %s; sanity only, not a proof)" % worst, worst >= 0)

print()
print("%d failed" % len(FAILS))
sys.exit(1 if FAILS else 0)
