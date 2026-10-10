#!/usr/bin/env python3
"""S2 / node S2.3: local tomography of a pair system built from data on an ABSTRACT carrier.
Exact arithmetic only (Fractions, integers, sympy rationals / symbols).

Run:  cd pt/S2 && python3 -I -B s2_3_lt.py ../base/verification/lean-mathlib/OIBridge

Setting.  A pair system realizing the certified native gate on an abstract carrier V = W 3 (+) H (H hidden, never
read by a product test).  pi : V -> W 3 is the product-test table (pi(u, h) = u).  Products are (prodState x y, 0)
(COMP-1 ProductData, bi-affine).  The gate N : V -> V is linear and has the certified PRODUCT ACTION:
pi(N(p, 0)) = cnot(p) for every product p.  Generation: preparations = N-words applied to products (and mixtures);
tests = product tests preceded by N-words.  Block form N = [[A, B], [C, D]] w.r.t. W 3 (+) H.
  PTQ (product-test quotient, K2-LEDGER) of N on the generated span S: pi(N s) = cnot(pi s) for s in S.
  INV2 (carrier level): N o N = id on V.

DECISION RULES (fixed before the first run):
 L0 Transcription: pc/pt parsed equal the hard-coded tables, cnot involution, cnot pxz = phiW.  Failure: ABORT.
 L1 The 16 product tables prodState(x, y), x, y in {xplus, (0,1,0), z3, 0}, have rank 16 (so the product action fixes
    A = cnot: written step).
 L2 Symbolic identities for generic B (16x2), C (2x16), D (2x2) and a generic table u (16 symbols), with A = cnot:
    (i) pi N (cnot u, C u) - cnot(pi (cnot u, C u)) = B C u ;  (ii) the W3 x W3 block of N o N is I + B C.
    Countercontrol: for an explicit B, C with B C != 0 the difference (i) at u = pxz must be nonzero.
 L3 Involutive positive control N_inv (H = R^2, C w = (w_10 + w_11, 0), B h = h_2 (e_03 + e_33), D = -I):
    N_inv o N_inv = I exactly; C pxz != 0 (the hidden register is excited by the gate); on the finite generated
    instance every generated label value equals prodEffVal e f (cnot^k (pi s)) (LT through tables).
    Countercontrol: the hidden coordinate is NOT a function of the table on the generated span (two span elements with
    equal tables and different hidden parts are exhibited) -- it must fail to be a function.
 L4 Register model N_reg = [[cnot, I - cnot], [cnot, -cnot]] on W 3 (+) W 3: product action holds; N^2 = cnot (+) cnot;
    N^4 = I; INV2 FAILS (countercontrol: N^2 = I must fail); B C != 0; exact LT-failure witness: s = N(pxz, 0) and
    s' = N^2(pxz, 0) have equal tables while pi(N s) != pi(N s'); every label value on the finite generated instance
    lies in [0, 1] and the unit label is 1 (valid pre-composite data); the generated set is closed under N and N^3.
 L5 Order-3 model N_3 = [[cnot, 0], [C, R]], R = [[0,-1],[1,-1]] (R^3 = I): N_3 o N_3 != I (carrier INV2 fails) while
    B = 0 gives PTQ, and on the finite generated instance every label value factors through tables (LT holds).
 L6 Rebit control (d = 2, real QT, two copies of the disk): Ad(CNOT) preserves the 10-dim real symmetric span and is an
    involution there; its product action C on the 9-dim product-test table space has C(X(x)Z) = 0, so C o C != I;
    rho0 = (1/2)(rho_{+x} (x) rho_{-z} + rho_{-x} (x) rho_{+z}) is a mixture of products, rho1 = Ad(CNOT) rho0 =
    (I + Y(x)Y)/4; pi(rho1) = pi(I/4) while pi(Ad(CNOT) rho1) != pi(Ad(CNOT) I/4): LT fails although N o N = I.
 VERDICT lines print only if L0-L6 pass and every countercontrol fails as required.
"""
import sys, os, re, itertools
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
    n, q, p = len(A), len(B), len(B[0])
    return [[sum(A[i][r] * B[r][j] for r in range(q) if A[i][r] != 0) for j in range(p)] for i in range(n)]
def mvec(A, v):
    return [sum(A[i][r] * v[r] for r in range(len(v)) if A[i][r] != 0) for i in range(len(A))]
def eye(n): return [[1 if i == j else 0 for j in range(n)] for i in range(n)]
def hom(x): return (1, x[0], x[1], x[2])
def prodState(x, y):
    hx, hy = hom(x), hom(y); return [hx[m] * hy[n] for (m, n) in IDX]
def pairVal(a, b, w): return sum(a[m] * w[k(m, n)] * b[n] for (m, n) in IDX)
def sharp(b): return (Fr(1, 2), Fr(b[0], 2), Fr(b[1], 2), Fr(b[2], 2))
UNIT = (1, 0, 0, 0)

def frank(rows):
    M = [[Fr(x) for x in r] for r in rows]
    rk = 0; ncol = len(M[0]) if M else 0
    for c in range(ncol):
        piv = next((i for i in range(rk, len(M)) if M[i][c] != 0), None)
        if piv is None: continue
        M[rk], M[piv] = M[piv], M[rk]
        for i in range(len(M)):
            if i != rk and M[i][c] != 0:
                f = M[i][c] / M[rk][c]
                M[i] = [M[i][j] - f * M[rk][j] for j in range(ncol)]
        rk += 1
    return rk

# ---------------------------------------------------------------- L0
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
check("L0.pc/pt transcription", parse_table("pc") == PC and parse_table("pt") == PT)
CNOT = [[0] * 16 for _ in range(16)]
for (m, n) in IDX:
    CNOT[k(m, n)][k(PC[m][n], PT[m][n])] = SGN(m, n)
check("L0.cnot involution", mmul(CNOT, CNOT) == eye(16))
xplus, yplus, z3, zero = (1, 0, 0), (0, 1, 0), (0, 0, 1), (0, 0, 0)
phiW = [(1 if m != 2 else -1) if m == n else 0 for (m, n) in IDX]
pxz = prodState(xplus, z3)
check("L0.cnot pxz = phiW", mvec(CNOT, pxz) == phiW)
if not OK:
    print("ABORT"); sys.exit(1)

# ---------------------------------------------------------------- L1
basis_pts = [xplus, yplus, z3, zero]
check("L1.16 product tables span W 3", frank([prodState(x, y) for x in basis_pts for y in basis_pts]) == 16)

# ---------------------------------------------------------------- L2 symbolic block identities
Bs = sp.Matrix(16, 2, lambda i, j: sp.Symbol(f"b{i}_{j}"))
Cs = sp.Matrix(2, 16, lambda i, j: sp.Symbol(f"c{i}_{j}"))
Ds = sp.Matrix(2, 2, lambda i, j: sp.Symbol(f"d{i}_{j}"))
us = sp.Matrix(16, 1, lambda i, j: sp.Symbol(f"u{i}"))
CN = sp.Matrix(CNOT)
Nbig = sp.Matrix(sp.BlockMatrix([[CN, Bs], [Cs, Ds]]))
state = sp.Matrix.vstack(CN * us, Cs * us)                # N(u, 0) = (cnot u, C u)
img = Nbig * state
diff = sp.expand(img[:16, 0] - CN * state[:16, 0])
check("L2.(i) pi N(cnot u, Cu) - cnot pi(cnot u, Cu) = B C u", sp.expand(diff - Bs * Cs * us) == sp.zeros(16, 1))
NN = Nbig * Nbig
check("L2.(ii) W3-block of N o N = I + B C", sp.expand(NN[:16, :16] - (sp.eye(16) + Bs * Cs)) == sp.zeros(16, 16))
Bx = sp.zeros(16, 2); Bx[k(0, 3), 1] = 1
Cx = sp.zeros(2, 16); Cx[1, k(1, 0)] = 1
dx = (Bx * Cx * sp.Matrix(pxz))
control("L2.difference vanishes for B C != 0 at u = pxz", dx == sp.zeros(16, 1))

# ---------------------------------------------------------------- shared: build block maps
def block(A, B, C, D):
    n1, n2 = len(A), len(D)
    M = [[0] * (n1 + n2) for _ in range(n1 + n2)]
    for i in range(n1):
        for j in range(n1): M[i][j] = A[i][j]
        for j in range(n2): M[i][n1 + j] = B[i][j]
    for i in range(n2):
        for j in range(n1): M[n1 + i][j] = C[i][j]
        for j in range(n2): M[n1 + i][n1 + j] = D[i][j]
    return M
AX = [xplus, (-1, 0, 0), yplus, (0, -1, 0), z3, (0, 0, -1)]
PRODS = [prodState(x, y) for x in AX for y in AX]
EFFS = [(sharp(e), sharp(f)) for e in AX for f in AX] + [(UNIT, UNIT)]

def generate(N, nh, maxlen):
    """Orbit of the products under N up to word length maxlen (as tuples)."""
    out = []
    for p in PRODS:
        s = list(p) + [0] * nh
        for t in range(maxlen + 1):
            out.append(tuple(s))
            s = mvec(N, s)
    return out
def labels_value(N, s, kpow, e, f):
    t = list(s)
    for _ in range(kpow): t = mvec(N, t)
    return pairVal(e, f, t[:16])
def cpow(u, kpow):
    t = list(u)
    for _ in range(kpow): t = mvec(CNOT, t)
    return t

# ---------------------------------------------------------------- L3 involutive positive control
nh = 2
delta = [0] * 16; delta[k(0, 3)] = 1; delta[k(3, 3)] = 1
check("L3.cnot delta = delta", mvec(CNOT, delta) == delta)
Cinv = [[0] * 16 for _ in range(2)]; Cinv[0][k(1, 0)] = 1; Cinv[0][k(1, 1)] = 1
ell_cnot = all(sum(Cinv[0][j] * CNOT[j][i] for j in range(16)) == Cinv[0][i] for i in range(16))
check("L3.ell o cnot = ell", ell_cnot)
Binv = [[0, delta[i]] for i in range(16)]
Dinv = [[-1, 0], [0, -1]]
Ninv = block(CNOT, Binv, Cinv, Dinv)
check("L3.N_inv o N_inv = I", mmul(Ninv, Ninv) == eye(18))
check("L3.hidden register excited: C pxz != 0", mvec(Cinv, pxz) != [0, 0])
G3 = generate(Ninv, nh, 2)
fact = all(labels_value(Ninv, s, kp, e, f) == pairVal(e, f, cpow(s[:16], kp))
           for s in G3 for kp in range(3) for (e, f) in EFFS)
check("L3.every generated label value = prodEffVal of cnot^k(table) (LT through tables)", fact)
s1 = mvec(Ninv, list(pxz) + [0, 0])                 # (cnot pxz, C pxz)
# a span element with the same table and hidden part 0: express cnot pxz in the product basis
tgt = s1[:16]
Bm = sp.Matrix([prodState(x, y) for x in basis_pts for y in basis_pts]).T
coef = Bm.solve(sp.Matrix(tgt))
s2 = [sum(coef[j] * Bm[i, j] for j in range(16)) for i in range(16)] + [0, 0]
func = (s1[16:] == s2[16:]) or (s1[:16] != [sp.nsimplify(t) for t in s2[:16]])
control("L3.hidden coordinate is a function of the table on the generated span", func,
        f"hidden {s1[16:]} vs {s2[16:]}")

# ---------------------------------------------------------------- L4 register model
I16 = eye(16)
IminusC = [[I16[i][j] - CNOT[i][j] for j in range(16)] for i in range(16)]
negC = [[-CNOT[i][j] for j in range(16)] for i in range(16)]
Nreg = block(CNOT, IminusC, CNOT, negC)
check("L4.product action pi N(p,0) = cnot p", all(mvec(Nreg, list(p) + [0] * 16)[:16] == mvec(CNOT, p) for p in PRODS))
N2 = mmul(Nreg, Nreg)
check("L4.N^2 = cnot (+) cnot", N2 == block(CNOT, [[0] * 16 for _ in range(16)], [[0] * 16 for _ in range(16)], CNOT))
check("L4.N^4 = I", mmul(N2, N2) == eye(32))
control("L4.INV2 (N^2 = I)", N2 == eye(32))
BC = mmul(IminusC, CNOT)
check("L4.B C != 0", any(any(x != 0 for x in r) for r in BC))
s = mvec(Nreg, list(pxz) + [0] * 16); sp_ = mvec(Nreg, s)
check("L4.equal tables pi s = pi s' (= cnot pxz)", s[:16] == sp_[:16] == phiW)
Ns, Nsp = mvec(Nreg, s), mvec(Nreg, sp_)
check("L4.pi(N s) != pi(N s') (LT fails)", Ns[:16] != Nsp[:16], f"pi(N s)=phiW:{Ns[:16]==phiW} pi(N s')=pxz:{Nsp[:16]==pxz}")
G4 = generate(Nreg, 16, 3)
vals = [labels_value(Nreg, st, kp, e, f) for st in G4 for kp in range(4) for (e, f) in EFFS]
check("L4.all generated label values in [0,1]", all(0 <= v <= 1 for v in vals))
check("L4.unit label = 1 on the generated instance", all(labels_value(Nreg, st, kp, UNIT, UNIT) == 1
                                                          for st in G4 for kp in range(4)))
G4set = set(G4)
closedN = all(tuple(mvec(Nreg, list(st))) in G4set for st in G4)
check("L4.generated set closed under N (hence under N^-1 = N^3)", closedN)

# ---------------------------------------------------------------- L5 order-3 model
R3 = [[0, -1], [1, -1]]
check("L5.R^3 = I", mmul(R3, mmul(R3, R3)) == eye(2))
N3 = block(CNOT, [[0, 0] for _ in range(16)], Cinv, R3)
control("L5.carrier INV2 (N_3^2 = I)", mmul(N3, N3) == eye(18))
G5 = generate(N3, 2, 3)
fact5 = all(labels_value(N3, st, kp, e, f) == pairVal(e, f, cpow(st[:16], kp))
            for st in G5 for kp in range(4) for (e, f) in EFFS)
check("L5.LT through tables holds on the generated instance (B = 0)", fact5)

# ---------------------------------------------------------------- L6 rebit control
I2 = sp.eye(2); X = sp.Matrix([[0, 1], [1, 0]]); Z = sp.Matrix([[1, 0], [0, -1]]); Y = sp.Matrix([[0, -sp.I], [sp.I, 0]])
kron = sp.kronecker_product
UCN = kron(sp.Matrix([[1, 0], [0, 0]]), I2) + kron(sp.Matrix([[0, 0], [0, 1]]), X)
VIS = [(a, b) for a in (I2, X, Z) for b in (I2, X, Z)]
YY = kron(Y, Y)
check("L6.CNOT real", all(sp.im(x) == 0 for x in UCN))
def ad(R): return UCN * R * UCN.T
def vis_table(R): return [sp.nsimplify((R * kron(a, b)).trace()) for (a, b) in VIS]
basis10 = [kron(a, b) for (a, b) in VIS] + [YY]
sym_ok = all(sp.simplify(ad(Bm_) - ad(Bm_).T) == sp.zeros(4, 4) and all(sp.im(x) == 0 for x in ad(Bm_))
             for Bm_ in basis10)
check("L6.Ad(CNOT) maps the real symmetric span to itself", sym_ok)
check("L6.Ad(CNOT) involution", all(sp.simplify(ad(ad(Bm_)) - Bm_) == sp.zeros(4, 4) for Bm_ in basis10))
check("L6.CNOT (X(x)Z) CNOT = -Y(x)Y", sp.simplify(ad(kron(X, Z)) + YY) == sp.zeros(4, 4))
Cm = sp.Matrix([[sp.Rational(vis_table(ad(kron(a, b)))[i], 4) for (a, b) in VIS] for i in range(9)])
check("L6.product action C has C(X(x)Z) = 0", Cm[:, VIS.index((X, Z))] == sp.zeros(9, 1))
check("L6.C o C != I", Cm * Cm != sp.eye(9))
rp = lambda a: (I2 + a) / 2
rho0 = (kron(rp(X), rp(-Z)) + kron(rp(-X), rp(Z))) / 2
rho1 = ad(rho0)
check("L6.rho1 = (I + Y(x)Y)/4", sp.simplify(rho1 - (sp.eye(4) + YY) / 4) == sp.zeros(4, 4))
check("L6.pi(rho1) = pi(I/4)", vis_table(rho1) == vis_table(sp.eye(4) / 4))
check("L6.pi(Ad rho1) != pi(Ad(I/4)) (LT fails though N o N = I)", vis_table(ad(rho1)) != vis_table(ad(sp.eye(4) / 4)))

print(f"SUMMARY checks passed={NPASS} all_ok={OK}")
if OK:
    print("VERDICT BLOCK-LEMMA: for a pair system realizing the certified product action of cnot, PTQ of the gate on "
          "the generated span <=> B C = 0, and N o N = I forces B C = 0 (symbolic identities)")
    print("VERDICT INV2: an involutive gate with an excited hidden register still gives LT through tables (positive "
          "control); the register model (N^4 = I, N^2 != I) satisfies product action, validity and reversibility and "
          "is not locally tomographic (exact witness)")
    print("VERDICT STRENGTH: carrier-level INV2 is strictly stronger than LT (order-3 model: LT holds, N^2 != I); the "
          "rebit control shows the certified involutive table action is needed (N^2 = I, product action not "
          "involutive, LT fails)")
else:
    print("NO VERDICT")
