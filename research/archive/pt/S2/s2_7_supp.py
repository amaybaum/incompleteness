#!/usr/bin/env python3
"""S2 / S2.4-S2.5 supplement: three cells of the generated-systems table.  Exact arithmetic only.

Run:  cd pt/S2 && python3 -I -B s2_7_supp.py ../base/verification/lean-mathlib/OIBridge

DECISION RULES (fixed before the first run):
 U0 Transcription: pc/pt parsed; cnot involution; cnot pxz = phiW.  Failure: ABORT.
 U1 The CtrlGate family exceeds K_gen: with Rz = Rz(3/5, 4/5) and G_t = cnot o actT Rz (a CtrlGate member,
    s2_2 Q3), the generated table s_c = actT Rz (cnot prodState(xplus, (0,1,0))) = (cnot o G_t)(cnot prodState(...)) is
    pure, has table rank > 1 and cnot(s_c) has table rank > 1 (outside K_gen by extremality, written).
    Countercontrol: with Rz replaced by the identity the same test must FAIL (the table is a cnot image of a product).
 U2 An improper target pre-local breaks consistency: G_r = cnot o actT(Rz o reflY) satisfies frame and relC (CtrlGate)
    exactly, and an exact negative product-effect value of G_r(G_r(prodState x y)) is found on axis/Pythagorean data.
 U3 The odd class: g_Tw = sigma o cnot o sigma maps sigma(cnot prodState x y) to prodState-type tables
    (g_Tw o sigma o cnot = sigma) exactly, so sigma K_gen is g_Tw-invariant; cnot does not preserve sigma K_gen:
    cnot(g_Tw(pxz)) = chainW, with the landed value -1/2 at the sharp effects of -e1, -e3.
 VERDICT lines print only if U0-U3 pass and the countercontrol fails as required.
"""
import sys, os, re
from fractions import Fraction as Fr
import sympy as sp

OK = True
NPASS = 0
def check(name, cond, detail=""):
    global OK, NPASS
    if cond:
        NPASS += 1; print(f"PASS {name}" + (f"  [{detail}]" if detail else ""))
    else:
        OK = False; print(f"FAIL {name}" + (f"  [{detail}]" if detail else ""))
def control(name, should_fail_cond, detail=""):
    global OK, NPASS
    if not should_fail_cond:
        NPASS += 1; print(f"PASS countercontrol {name} fails as required" + (f"  [{detail}]" if detail else ""))
    else:
        OK = False; print(f"FAIL countercontrol {name} did not fail" + (f"  [{detail}]" if detail else ""))

IDX = [(m, n) for m in range(4) for n in range(4)]
def k(m, n): return 4 * m + n
def mmul(A, B):
    return [[sum(A[i][r] * B[r][j] for r in range(len(B)) if A[i][r] != 0) for j in range(len(B[0]))] for i in range(len(A))]
def mvec(A, v):
    return [sum(A[i][r] * v[r] for r in range(len(v)) if A[i][r] != 0) for i in range(len(A))]
def eye(n): return [[1 if i == j else 0 for j in range(n)] for i in range(n)]
def hom(x): return (1, x[0], x[1], x[2])
def prodState(x, y):
    hx, hy = hom(x), hom(y); return [hx[m] * hy[n] for (m, n) in IDX]
def pairVal(a, b, w): return sum(a[m] * w[k(m, n)] * b[n] for (m, n) in IDX)
def sharpv(b): return (Fr(1, 2), Fr(b[0], 2), Fr(b[1], 2), Fr(b[2], 2))
def homMap(N):
    H = [[0] * 4 for _ in range(4)]; H[0][0] = 1
    for i in range(3):
        for j in range(3): H[i + 1][j + 1] = N[i][j]
    return H
def actC_map(N):
    H = homMap(N); M = [[0] * 16 for _ in range(16)]
    for m in range(4):
        for n in range(4):
            for q in range(4):
                if H[m][q] != 0: M[k(m, n)][k(q, n)] += H[m][q]
    return M
def actT_map(N):
    H = homMap(N); M = [[0] * 16 for _ in range(16)]
    for m in range(4):
        for n in range(4):
            for l in range(4):
                if H[n][l] != 0: M[k(m, n)][k(m, l)] += H[n][l]
    return M
def m3(A, B): return [[sum(A[i][r] * B[r][j] for r in range(3)) for j in range(3)] for i in range(3)]
def table_rank(w):
    return sp.Matrix([[sp.nsimplify(w[k(m, n)]) for n in range(4)] for m in range(4)]).rank()

oib = sys.argv[1] if len(sys.argv) > 1 else "../base/verification/lean-mathlib/OIBridge"
src = open(os.path.join(oib, "CompositeDimension.lean"), encoding="utf-8").read()
PC = [[0, 0, 3, 3], [1, 1, 2, 2], [2, 2, 1, 1], [3, 3, 0, 0]]
PT = [[0, 1, 2, 3], [1, 0, 3, 2], [1, 0, 3, 2], [0, 1, 2, 3]]
def SGN(m, n): return -1 if ((m == 1 and n == 3) or (m == 2 and n == 2)) else 1
def parse_table(name):
    body = re.search(r"def " + name + r" : Fin 4 → Fin 4 → Fin 4\n(.*?)\n\n", src, re.S).group(1)
    T = [[None] * 4 for _ in range(4)]
    for a, b, c in re.findall(r"\|\s*(\d),\s*(\d)\s*=>\s*(\d)", body):
        T[int(a)][int(b)] = int(c)
    return T
check("U0.pc/pt transcription", parse_table("pc") == PC and parse_table("pt") == PT)
CNOT = [[0] * 16 for _ in range(16)]
for (m, n) in IDX:
    CNOT[k(m, n)][k(PC[m][n], PT[m][n])] = SGN(m, n)
check("U0.cnot involution", mmul(CNOT, CNOT) == eye(16))
xplus, yplus, z3 = (1, 0, 0), (0, 1, 0), (0, 0, 1)
phiW = [(1 if m != 2 else -1) if m == n else 0 for (m, n) in IDX]
pxz = prodState(xplus, z3)
check("U0.cnot pxz = phiW", mvec(CNOT, pxz) == phiW)
if not OK:
    print("ABORT"); sys.exit(1)

# dictionary for purity
I2 = sp.eye(2); X = sp.Matrix([[0, 1], [1, 0]]); Y = sp.Matrix([[0, -sp.I], [sp.I, 0]]); Z = sp.Matrix([[1, 0], [0, -1]])
PAULI = [I2, X, Y, Z]
SS = [[sp.kronecker_product(PAULI[m], PAULI[n]) for n in range(4)] for m in range(4)]
def rho_of(w):
    R = sp.zeros(4, 4)
    for (m, n) in IDX:
        if w[k(m, n)] != 0: R += sp.nsimplify(w[k(m, n)]) * SS[m][n]
    return R / 4
def is_pure(w):
    R = rho_of(w)
    return sp.simplify(R * R - R) == sp.zeros(4, 4) and sp.simplify(R.trace()) == 1

# ---------------------------------------------------------------- U1
c, s = Fr(3, 5), Fr(4, 5)
RZ = [[c, -s, 0], [s, c, 0], [0, 0, 1]]
Gt = mmul(CNOT, actT_map(RZ))
check("U1.cnot o G_t = actT Rz", mmul(CNOT, Gt) == actT_map(RZ))
base = mvec(CNOT, prodState(xplus, yplus))
s_c = mvec(actT_map(RZ), base)
r1, r2 = table_rank(s_c), table_rank(mvec(CNOT, s_c))
check("U1.s_c pure", is_pure(s_c))
check("U1.s_c outside K_gen (table ranks of s_c and cnot s_c > 1)", r1 > 1 and r2 > 1, f"{r1}, {r2}")
b1, b2 = table_rank(base), table_rank(mvec(CNOT, base))
control("U1.with Rz = I the table lies outside K_gen", b1 > 1 and b2 > 1, f"{b1}, {b2}")

# ---------------------------------------------------------------- U2
REFLY = [[1, 0, 0], [0, -1, 0], [0, 0, 1]]
R0 = m3(RZ, REFLY)
Gr = mmul(CNOT, actT_map(R0))
NFLIP = [[1, 0, 0], [0, -1, 0], [0, 0, -1]]
ACn, ATn = actC_map(NFLIP), actT_map(NFLIP)
corner = {0: z3, 1: (0, 0, -1)}
frame = all(mvec(Gr, prodState(corner[a], corner[b])) == prodState(corner[a], corner[(a + b) % 2])
            for a in (0, 1) for b in (0, 1))
check("U2.G_r frame", frame)
check("U2.G_r relC", mmul(ACn, mmul(Gr, ACn)) == mmul(ATn, Gr))
G2 = mmul(Gr, Gr)
pts = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1), (Fr(3, 5), Fr(4, 5), 0), (0, Fr(3, 5), Fr(4, 5))]
wit = None
for x in pts:
    for y in pts:
        img = mvec(G2, prodState(x, y))
        for e in pts:
            for f in pts:
                v = pairVal(sharpv(e), sharpv(f), img)
                if v < 0 and wit is None:
                    wit = (x, y, e, f, v)
check("U2.exact negative value of G_r(G_r(prodState x y)) (inconsistent)", wit is not None, str(wit))

# ---------------------------------------------------------------- U3
SIG = actT_map(REFLY)
gTw = mmul(SIG, mmul(CNOT, SIG))
check("U3.g_Tw o sigma o cnot = sigma", mmul(gTw, mmul(SIG, CNOT)) == SIG)
chainW = [1, 0, 0, 1, 1, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0]
cg = mvec(CNOT, mvec(gTw, pxz))
check("U3.cnot(g_Tw(pxz)) = chainW", cg == chainW)
check("U3.value -1/2 at the sharp effects of -e1, -e3", pairVal(sharpv((-1, 0, 0)), sharpv((0, 0, -1)), cg) == Fr(-1, 2))

print(f"SUMMARY checks passed={NPASS} all_ok={OK}")
if OK:
    print("VERDICT SUPPLEMENT: the CtrlGate family generates tables outside K_gen (exact pure witness); an improper "
          "target pre-local in the CtrlGate family is inconsistent; the odd class cone sigma K_gen is g_Tw-invariant "
          "and not cnot-invariant (chainW, -1/2)")
else:
    print("NO VERDICT")
