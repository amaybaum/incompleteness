"""EQ2-A probe A1 -- the Pauli/twin package (two tokens), exact.  Research only; base bcbc516f.

Usage: python3 -I -B a1_pauli_twin.py <CompositeDimension.lean> <K2Guard.lean>

DECISION RULE (fixed before the first run):
  The verdict line `A1-IDENTITIES-EXACT` prints iff EVERY check below passes, including
    T0  the transcription control (tables parsed from the base == independent hand transcription), and
    K   the landed-fact controls (actT_reflY_phiW, cnot_prodState_xplus_z3, cnot_idW, chain_value = -1/2,
        rotation_chain_value = 0, cnot involutive, frame/relT/relC of cnot with nflip),
  and every countercontrol fails in the way it must.  Otherwise the verdict is `A1-NOT-RENDERED` and the failing
  checks are listed.  Symbolic identities are decided by sympy `expand(...) == 0` on polynomial expressions with
  rational/Gaussian coefficients (exact).  No floating point.
Checks:
  A1.1  pauliW (prodState x y) = rho x (x) rho y                         (symbolic x, y)
  A1.2  pairVal a b w = tr((A (x) B) pauliW w), A = sum a_mu sigma_mu    (symbolic a, b, w)
  A1.3  tr(P_a P_b) = 2^n delta_ab for Pauli strings, n = 1, 2, 3
  A1.4  pauliW w is Hermitian for real w; the 16 kron(P_mu, P_nu) are R-linearly independent (rank 16)
  A1.5  coordinates of the twist maps: actT reflY = PT_B, actC reflY = PT_A, transposeW = global transpose
        = actC reflY . actT reflY, swapW = Ad SWAP, actT nflip = Ad(1 (x) X), cnot = Ad CNOT
  A1.6  chart2 a a idW = diag(1, a a^T) (symbolic a); four exact orthogonal a (2 proper, 2 improper) fix idW;
        control: a = diag(2,1,1) does not; IsOrth id and IsOrth reflY
  A1.7  pauliW idW = SWAP/2; singlet v = (0,1,-1,0): v^H pauliW(idW) v = -1, v^H v = 2
  A1.8  pauliW phiW = (1/2) w w^H with w = (1,0,0,1)            (phiW in Q3, rank one)
  A1.9  chart2 id reflY = actT reflY and actT reflY is an involution (so chart2 id reflY '' twin = Q3)
  A1.10 (derived) twin not uniformly presented: idW in twin (K1 + A1.8), fixed by uniform charts (A1.6), not in Q3 (A1.7)
  A1.11 exchange: chart2 id reflY . swapW . chart2 id reflY = transposeW . swapW; Pauli image = (SWAP X SWAP)^T
  A1.12 three copies, rho = |0><0|_A (x) Phi+_BC: idle extension of transposeW.swapW on (A,B) has
        v^H M v = -1 at v = e_001 - e_100 (|v|^2 = 2); control: idle extension of swapW gives (1/2) u'u'^H (PSD);
        countercontrol: idle extension of transposeW alone is not positive (v = e_001 - e_010)
  A1.13 EX alone at two copies: swapW . actT reflY = actC reflY . swapW and actC reflY = transposeW . actT reflY,
        so swapW '' twin = twin (with transposeW '' Q3 = Q3)
  A1.14 orientation classes: chart2 R R = transposeW; chart2 I R phiW = idW; chart2 R I phiW = idW (both not in Q3)
  A1.15 cnot' := actT reflY . cnot . actT reflY: cnot'(prodState xplus z3) = idW; cnot' involutive
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sympy as sp  # noqa: E402
from sympy import I, Matrix, Rational as R, eye, zeros  # noqa: E402

import eq2a_lib as L  # noqa: E402

cd_path, k2_path = sys.argv[1], sys.argv[2]
check = L.check


def zero(M):
    return M.applyfunc(sp.expand).is_zero_matrix


# ---------------------------------------------------------------- T0 transcription control
tabs = L.parse_cnot_tables(cd_path)
sgn, pc, pt_ = tabs
neg = {(i, j) for i in range(4) for j in range(4) if sgn[i][j] == -1}
check("T0 parsed sgn/pc/pt == hand transcription", neg == L.HAND_NEG and pc == L.HAND_PC and pt_ == L.HAND_PT)
idW, chainW, refl = L.parse_k2guard_tables(k2_path)
phiW = L.parse_phiW(cd_path)
check("T0 parsed idW, chainW, phiW, reflY == hand transcription",
      idW == L.HAND_IDW and chainW == L.HAND_CHAINW and phiW == L.HAND_PHIW and refl == [1, -1, 1])
cnot = L.cnot_fun(tabs)
RY, NF, ID = L.REFLY, L.NFLIP, L.ID3

# ---------------------------------------------------------------- K landed-fact controls
check("K1 actT reflY phiW = idW (K2Guard:106)", L.actT(RY, phiW) == idW)
check("K2 cnot (prodState xplus z3) = phiW (CompositeDimension:1222)", cnot(L.prod_state(L.XPLUS, L.Z3)) == phiW)
check("K3 cnot idW = chainW (K2Guard:110)", cnot(idW) == chainW)
check("K4 chain value = -1/2 (K2Guard:134)",
      L.pair_val(L.sharp_vec([-1, 0, 0]), L.sharp_vec([0, 0, -1]), cnot(L.actT(RY, cnot(L.prod_state(L.XPLUS, L.Z3)))))
      == R(-1, 2))
check("K5 rotation chain value = 0 (K2Guard:223)",
      L.pair_val(L.sharp_vec([-1, 0, 0]), L.sharp_vec([0, 0, -1]), cnot(L.actT(NF, cnot(L.prod_state(L.XPLUS, L.Z3)))))
      == 0)
Wsym = Matrix(4, 4, lambda m, n: sp.Symbol(f"w{m}{n}", real=True))
check("K6 cnot involutive (symbolic)", zero(cnot(cnot(Wsym)) - Wsym))
check("K6 relT: actT nflip (cnot (actT nflip w)) = cnot w (symbolic)", zero(L.actT(NF, cnot(L.actT(NF, Wsym))) - cnot(Wsym)))
check("K6 relC: actC nflip (cnot (actC nflip w)) = actT nflip (cnot w) (symbolic)",
      zero(L.actC(NF, cnot(L.actC(NF, Wsym))) - L.actT(NF, cnot(Wsym))))
corner = {0: L.Z3, 1: [0, 0, -1]}
check("K6 frame: cnot (prod (corner a) (corner b)) = prod (corner a) (corner (a+b))",
      all(cnot(L.prod_state(corner[a], corner[b])) == L.prod_state(corner[a], corner[(a + b) % 2])
          for a in range(2) for b in range(2)))

# ---------------------------------------------------------------- A1.1 - A1.4
x = sp.symbols("x0:3", real=True)
y = sp.symbols("y0:3", real=True)
check("A1.1 pauliW (prodState x y) = rho x (x) rho y (symbolic)",
      zero(L.pauliW(L.prod_state(x, y)) - L.kron(L.rho1(x), L.rho1(y))))
a = sp.symbols("a0:4", real=True)
b = sp.symbols("b0:4", real=True)
lhs = L.pair_val(a, b, Wsym)
rhs = (L.kron(L.effop1(a), L.effop1(b)) * L.pauliW(Wsym)).trace()
check("A1.2 pairVal a b w = tr((A (x) B) pauliW w) (symbolic; imaginary part identically 0)", sp.expand(lhs - rhs) == 0)
import itertools  # noqa: E402
ok3 = True
for n in (1, 2, 3):
    strings = list(itertools.product(range(4), repeat=n))
    mats = {s: L.kron(*[L.PAULI[i] for i in s]) for s in strings}
    for s in strings:
        for t in strings:
            tr = (mats[s] * mats[t]).trace()
            if tr != (2 ** n if s == t else 0):
                ok3 = False
check("A1.3 tr(P_s P_t) = 2^n delta_st for all Pauli strings, n = 1, 2, 3", ok3)
check("A1.4 pauliW w is Hermitian for real symbolic w", zero(L.pauliW(Wsym) - L.pauliW(Wsym).H))
vecs = []
for m in range(4):
    for n in range(4):
        K = L.kron(L.PAULI[m], L.PAULI[n])
        vecs.append([sp.re(e) for e in K] + [sp.im(e) for e in K])
check("A1.4 the 16 kron(P_mu, P_nu) are R-linearly independent (rank 16 as real 32-vectors)", Matrix(vecs).rank() == 16)

# ---------------------------------------------------------------- A1.5 twist maps in coordinates
rhoW = L.pauliW(Wsym)
check("A1.5 pauliW (actT reflY w) = PT_B (pauliW w)", zero(L.pauliW(L.actT(RY, Wsym)) - L.pt(rhoW, 1, [2, 2])))
check("A1.5 pauliW (actC reflY w) = PT_A (pauliW w)", zero(L.pauliW(L.actC(RY, Wsym)) - L.pt(rhoW, 0, [2, 2])))
check("A1.5 transposeW = actC reflY . actT reflY", zero(L.transposeW(Wsym) - L.actC(RY, L.actT(RY, Wsym))))
check("A1.5 pauliW (transposeW w) = (pauliW w)^T", zero(L.pauliW(L.transposeW(Wsym)) - rhoW.T))
SWAP = L.swap_matrix([2, 2], [1, 0])
check("A1.5 pauliW (swapW w) = SWAP pauliW(w) SWAP", zero(L.pauliW(L.swapW(Wsym)) - SWAP * rhoW * SWAP))
IX = L.kron(L.S0, L.SX)
check("A1.5 pauliW (actT nflip w) = (1 (x) X) pauliW(w) (1 (x) X)", zero(L.pauliW(L.actT(NF, Wsym)) - IX * rhoW * IX))
CNOT = Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
check("A1.5 pauliW (cnot w) = CNOT pauliW(w) CNOT (control = first copy)", zero(L.pauliW(cnot(Wsym)) - CNOT * rhoW * CNOT))

# ---------------------------------------------------------------- A1.6 chart2 a a idW
A = Matrix(3, 3, lambda i, j: sp.Symbol(f"a{i}{j}", real=True))
M = L.chart2(A, A, idW)
target = sp.diag(1, A * A.T)
check("A1.6 chart2 a a idW = diag(1, a a^T) (symbolic a)", zero(M - target))
skews = [Matrix([[0, R(1, 2), R(-1, 3)], [R(-1, 2), 0, R(2, 5)], [R(1, 3), R(-2, 5), 0]]),
         Matrix([[0, 3, 1], [-3, 0, R(-7, 4)], [-1, R(7, 4), 0]])]
orths = []
for Sk in skews:
    q = L.cayley(Sk)
    orths += [q, q * RY]
ok_o = all((q * q.T - eye(3)).is_zero_matrix for q in orths)
dets = sorted(q.det() for q in orths)
check(f"A1.6 four exact orthogonal a with determinants {dets}", ok_o and dets == [-1, -1, 1, 1])
check("A1.6 chart2 a a idW = idW for each of the four", all(L.chart2(q, q, idW) == idW for q in orths))
D2 = sp.diag(2, 1, 1)
check("A1.6 control: a = diag(2,1,1) (not orthogonal) does NOT fix idW", L.chart2(D2, D2, idW) != idW)
check("A1.6 IsOrth id and IsOrth reflY (a a^T = 1)", ID * ID.T == eye(3) and RY * RY.T == eye(3))

# ---------------------------------------------------------------- A1.7 / A1.8
check("A1.7 pauliW idW = SWAP/2", zero(L.pauliW(idW) - SWAP / 2))
v = Matrix([0, 1, -1, 0])
val = (v.H * L.pauliW(idW) * v)[0, 0]
check(f"A1.7 singlet witness: v^H pauliW(idW) v = {val}, v^H v = {(v.H * v)[0, 0]}",
      val == -1 and (v.H * v)[0, 0] == 2)
wv = Matrix([1, 0, 0, 1])
check("A1.8 pauliW phiW = (1/2) w w^H, w = (1,0,0,1)", zero(L.pauliW(phiW) - (wv * wv.H) / 2))

# ---------------------------------------------------------------- A1.9 - A1.11
check("A1.9 chart2 id reflY = actT reflY (symbolic)", zero(L.chart2(ID, RY, Wsym) - L.actT(RY, Wsym)))
check("A1.9 actT reflY is an involution (symbolic)", zero(L.actT(RY, L.actT(RY, Wsym)) - Wsym))
check("A1.10 derived: idW in twin, idW fixed by every uniform orthogonal chart, idW not in Q3",
      L.actT(RY, phiW) == idW and all(L.chart2(q, q, idW) == idW for q in orths) and val < 0)
chi = lambda w: L.chart2(ID, RY, w)  # noqa: E731  (its own inverse, A1.9)
check("A1.11 chi . swapW . chi = transposeW . swapW (symbolic)",
      zero(chi(L.swapW(chi(Wsym))) - L.transposeW(L.swapW(Wsym))))
check("A1.11 Pauli image of the presented exchange = (SWAP X SWAP)^T",
      zero(L.pauliW(L.transposeW(L.swapW(Wsym))) - (SWAP * rhoW * SWAP).T))

# ---------------------------------------------------------------- A1.12 three copies
e = lambda bits: Matrix([1 if i == int(bits, 2) else 0 for i in range(8)])  # noqa: E731
zero1 = Matrix([1, 0])
phiP = Matrix([1, 0, 0, 1])
rho = L.kron(zero1 * zero1.T, phiP * phiP.T / 2)
tab = L.coordsN(rho, 3)
check("A1.12 round trip pauli3(coords3 rho) = rho", zero(L.pauliN(tab, 3) - rho))
u = e("000") + e("011")
check("A1.12 rho = (1/2) u u^H with u = e_000 + e_011 (rho in Q_ABC, rank one)", zero(rho - u * u.H / 2))
g_twin = lambda w: L.transposeW(L.swapW(w))  # noqa: E731
Mtw = L.pauliN(L.idle_ext(g_twin, tab, (0, 1)), 3)
vt = e("001") - e("100")
valt = (vt.H * Mtw * vt)[0, 0]
check(f"A1.12 idle extension of transposeW.swapW on (A,B): v^H M v = {valt} at v = e_001 - e_100 (|v|^2 = 2)",
      valt == -1)
Msw = L.pauliN(L.idle_ext(L.swapW, tab, (0, 1)), 3)
up = e("000") + e("101")
check("A1.12 control: idle extension of swapW = (1/2) u'u'^H with u' = e_000 + e_101 (PSD)", zero(Msw - up * up.H / 2))
Mt = L.pauliN(L.idle_ext(L.transposeW, tab, (0, 1)), 3)
vc = e("001") - e("010")
valc = (vc.H * Mt * vc)[0, 0]
check(f"A1.12 countercontrol: idle extension of transposeW alone: v^H M v = {valc} at v = e_001 - e_010", valc == -1)

# ---------------------------------------------------------------- A1.13 - A1.15
check("A1.13 swapW . actT reflY = actC reflY . swapW (symbolic)",
      zero(L.swapW(L.actT(RY, Wsym)) - L.actC(RY, L.swapW(Wsym))))
check("A1.13 actC reflY = transposeW . actT reflY (symbolic)",
      zero(L.actC(RY, Wsym) - L.transposeW(L.actT(RY, Wsym))))
check("A1.14 chart2 R R = transposeW (symbolic)", zero(L.chart2(RY, RY, Wsym) - L.transposeW(Wsym)))
check("A1.14 chart2 I R phiW = idW and chart2 R I phiW = idW", L.chart2(ID, RY, phiW) == idW and L.chart2(RY, ID, phiW) == idW)
check("A1.14 transposeW phiW = phiW (the global transpose keeps the Bell table)", L.transposeW(phiW) == phiW)
cnotp = lambda w: L.actT(RY, cnot(L.actT(RY, w)))  # noqa: E731
check("A1.15 cnot'(prodState xplus z3) = idW (non-product image of a pure product)", cnotp(L.prod_state(L.XPLUS, L.Z3)) == idW)
check("A1.15 cnot' involutive (symbolic)", zero(cnotp(cnotp(Wsym)) - Wsym))

ok = L.summary("a1_pauli_twin")
print("VERDICT " + ("A1-IDENTITIES-EXACT" if ok else "A1-NOT-RENDERED"))
sys.exit(0 if ok else 1)
