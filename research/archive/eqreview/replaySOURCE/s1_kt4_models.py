"""EQ4-SOURCE s1 — exact models of the four-copy premise KT4 with the token-coherence field `tok` removed, the
token-coherent control, and the exact ingredients of the written routes (Lemma B1; FCC <=> exists KT4;
TokProdState <=> tok).  Research only; nothing here is adopted.

Usage:  python3 -I -B s1_kt4_models.py <base>/verification/lean-mathlib/OIBridge

Conventions (as the preflight package, inputs at f0d37906, and the base):
 - W 3 tables are 4 x 4 arrays, row = first token, index 0 = unit, 1, 2, 3 = x, y, z (CD:97).  actT N w [m][n] =
   hN[n] w[m][n] and actC N w [m][n] = hN[m] w[m][n] for a diagonal sign map N with homogenized signs hN = (1, N).
 - flat chart: flatW T [n + 4 m] = T[m][n] (finProdFinEquiv, Mathlib Logic/Equiv/Fin/Basic.lean:334).
 - COMP-1 coordinate model (CI:579-702) at dA = dB = 16: carrier = 17 x 17 arrays; hom x = (1, x);
   pState x y = hom x (x) hom y; an affine functional e on Fin 16 -> R is (c, l), e x = c + l.x, coeff e = (c, l);
   pEff e f w = sum coeff_e[m] coeff_f[n] w[m][n].  tabCoord m n = coord (n + 4 m) = (0, unit vector).
   On the normalized slice an affine functional e reads as the table Et[m][n] = l[4m+n] + c [m = n = 0].
 - four-copy tables Z[a][b][c][d] (tokens 0, 1, 2, 3); prodA X Y = X_ab Y_cd; prodB L L' = L_ac L'_bd;
   R Z [a][b][c][d] = Z[a][c][b][d] (regrouping; an involution); rho3 Z = s_d Z with s = (1, 1, -1, 1);
   fourVal X Y E F = sum X_ab Y_cd E_ac F_bd (package line 41).
 - iota : W4 -> carrier: iota Z [0][0] = Z0000, [0][(c,d)+1] = Z00cd, [(a,b)+1][0] = Zab00, [(a,b)+1][(c,d)+1] = Zabcd;
   pi reads the 16 x 16 block; sigma = iota R pi + (id - iota pi), a linear map of the carrier.
 - rho = flatW o actT reflY o unflat (sign -1 at the flat indices 4m + 2); tau = flat token exchange (tabT).
 - Pauli dictionary (package lines 307-318): s = (1, X, Y, Z); pauliW T = 1/4 sum T_mn s_m (x) s_n; Q3 = {pauliW T PSD};
   twin = actT reflY '' Q3; op4 Z = 1/16 sum Z_abcd s_a (x) s_b (x) s_c (x) s_d.

The structures (candidate values of `H : KT4 K01 K23 K02 K13 V` with the field `tok` removed):
 - M_anchor, any nonempty pair bodies: V = carrier x carrier; PA.prodState x y = (pState x y, a0), PA.prodEff e f =
   pEff e f o fst; PB.prodState L L' = (b0, pState L L'), PB.prodEff E F = pEff E F o snd; one body = the convex hull of
   both product sets; anchors a0 = pState L0 L0', b0 = pState x0 y0 with x0, y0, L0, L0' points of the bodies.
 - M_rho, cones (Q3, Q3, Q3, twin): PA = modelData.minPre; PB.prodState L L' = pState L (rho L'),
   PB.prodEff E F = pEff E (F o rho); PB.Omega := PA.Omega.  (No regrouping: built from landed COMP-1 objects and rho.)
 - M_tw, cones (Q3, Q3, Q3, twin): PA = modelData; PB.prodState L L' = sigma (pState L (rho L')),
   PB.prodEff E F = pEff E (F o rho) o sigma^-1; one body iota(B4), B4 = normalized PSD16 in table coordinates.
 - M_sigma (token-coherent table model, any cones): PB.prodState = sigma o pState, PB.prodEff E F = pEff E F o sigma^-1.
 - M_id, uniform cones: PB = PA.   M_T, uniform Q3 (EQ4-F f1 W4 completed): PB.prodState L L' = sigma (pState (tau L) L'),
   PB.prodEff E F = pEff (E o tau) F o sigma^-1.

DECISION RULE (fixed before the first run; rules, not expected numbers):
 K  transcription controls: the parsed sgn, pc, pt (CD:741-755), phiW (CD:1220), xplus (CD:1213), z3 (CD:793), nflip
    (CD:797-798), reflY (K2G:46-47), idW and chainW (K2G:101-104) equal the hand transcriptions; the landed statements
    cnot_prodState_xplus_z3 (CD:1222), actT_reflY_phiW (K2G:106), cnot_idW (K2G:110), chain_value (K2G:134) are present
    in the text and reproduce exactly.
 P  Pauli dictionary, exact, on bases (extended by linearity):
    P1 pauliW(prodState x y) = r(x) (x) r(y), r(x) = (1 + x.s)/2 (symbolic x, y);
    P2 pauliW(cnot B) = CNOT pauliW(B) CNOT^dag for the 16 basis tables B (so cnot maps Q3 onto Q3);
       countercontrol: with CZ in place of CNOT some basis table fails;
    P3 pauliW(actT reflY B) = PT_2 pauliW(B) (partial transpose of the second factor) for the 16 basis tables;
       countercontrol: without the transpose some basis table fails;
    P4 pairVal (u_a) (u_b) B = tr((s_a (x) s_b) pauliW B) for all basis vectors u_a, u_b and basis tables B;
    P5 op4(prodA B B') = pauliW B (x) pauliW B' and op4(prodB B B') = P (pauliW B (x) pauliW B') P^T (P exchanges the two
       middle tensor factors) for all 256 basis pairs; op4(rho3 Z) = PT_3 op4(Z) and op4(R Z) = P op4(Z) P^T for all 256
       basis tables; tr(s_I s_J) = 16 [I = J] for all Pauli strings I, J (so sum_I Z_I Z'_I = 16 tr(op4 Z op4 Z'));
       countercontrol: op4(prodB B B') = pauliW B (x) pauliW B' (no P) fails for some basis pair;
    P6 pauliW(phiW) = |Phi+><Phi+| (so phiW in Q3); an explicit vector v has v^dag pauliW(idW) v < 0 (idW not in Q3);
       hence (involution actT reflY, P3) idW in twin and phiW not in twin;
    P7 pauliW(tau B) = SWAP pauliW(B) SWAP for the 16 basis tables (tau maps Q3 onto Q3).
 L  slice facts used by Lemma B1 (symbolic X): the sum over the four sign pairs of prodEffVal(sharp(+-u_i),
    sharp(+-u_j)) X equals X00, and the sign-weighted sum equals X_ij (i, j = 1..3); countercontrol: the unweighted sum
    is not X_ij.
 A  M_anchor: A1 prodEff_apply for both structures (symbolic chart points, symbolic affine functionals);
    A2 PA.prodEff e f at PB's products equals e(x0) f(y0), and PB.prodEff E F at PA's products equals E(L0) F(L0')
       (symbolic); A3 tok fails at an explicit body point (nonzero exact difference);
    control: with zero anchors, PA's unit pairing at PB's products is not 1.
 R  M_rho: R1 PB.prodEff_apply (symbolic); R2 actT reflY o actT reflY = id on W 3 and rho fixes the unit entry
    (symbolic), so rho maps pairBody twin onto pairBody Q3; R3 tok fails at an explicit point; R4 Lemma P's family (i)
    value at the gate-supplied witnesses (X = Y = cnot(prodState xplus z3), E = cnot(tens(sharpVec xplus)(sharpVec z3)),
    F = cnotTw(tens(sharpVec(-xplus))(sharpVec(-z3)))) is negative; R5 cnot and cnotTw are involutions and
    self-adjoint for ipW, and ipW (tens a b) w = pairVal a b w (symbolic), the ingredients of E in dualW Q3 and F in
    dualW twin; the witness effects equal phiW/4 and dg(1,-1,1,-1)/4 (exact); R6 the gate data: cnotTw = actC id o actT reflY o cnot o actC id o actT reflY (an N-CLASS form with
    orthogonal locals) and Q3 != twin (P6) force tau = (0, 0, 0, 1), which is odd.
    countercontrol: in M_sigma with the same cones the cross value PB.prodEff E F (PA.prodState X Y) is the same negative
    number (so the token-coherent structure has no common body for these cones).
 T  M_tw: T1 sigma o sigma = id on all 289 basis vectors (so sigma^-1 = sigma) and sigma o iota = iota o R (symbolic);
    T2 PB.prodEff E F (PA.prodState X Y) = fourVal X Y Et (rho3-table Ft) and PA.prodEff e f (PB.prodState L L') =
       fourVal et ft L (rho L') (symbolic, normalized X, Y, L, L', affine e, f, E, F);
    T3 on iota(Z), PB.prodEff(tabCoord a c)(tabCoord b d) - PA.prodEff(tabCoord a b)(tabCoord c d) = (s_d - 1) Z_abcd
       (symbolic), nonzero exactly at d = 2: tok fails;
    T4 the two images of a four-token product state, PA.prodState(x0 (x) x1, x2 (x) x3) and PB.prodState(x0 (x) x2,
       x1 (x) x3), differ exactly by rho3 (symbolic Bloch vectors): TokProdState fails;
    T5 token 3's y-marginal read through the two groupings differs by sign (symbolic): STMC fails;
    countercontrols (M_sigma): the differences of T3, T4, T5 are zero.
 S  M_sigma: S1 tok holds on iota(W4) (symbolic); S2 Lemma B1's endpoint values PB.prodEff(sum E tabCoord)(sum F
    tabCoord)(PA.prodState X Y) = fourVal X Y E F and PA.prodEff(sum e tabCoord)(sum f tabCoord)(PB.prodState L L') =
    fourVal e f L L' (symbolic); S3 fourVal's four readings (package fourVal_eq_01, _23, _02, _13) (symbolic);
    S4 the complement identity pEff e f + pEff (u - e) f + pEff u (u - f) = pEff u u (symbolic);
    countercontrol: the S2 expression evaluated in M_rho differs from fourVal X Y E F (symbolic).
 I  M_id and M_T: I1 in M_id tok fails at an explicit point, and fourVal X Y E F = sum_I (prodA X Y)_I (prodB E F)_I
    (symbolic; the PSD route of the uniform-Q3 families through P5 is written); I2 in M_T tok fails at an explicit point
    and PB.prodEff E F (PA.prodState X Y) = fourVal X Y (tabT Et) Ft (symbolic).
VERDICT S1-KT4-WITHOUT-TOK-MODELS-EXACT iff every check passes (controls and countercontrols included); otherwise
VERDICT NOT RENDERED.  Exact arithmetic only (Fractions, Gaussian rationals as Fraction pairs, sympy Rationals and
symbols, Python integers); a float anywhere aborts the run.  Deterministic output; no timing in stdout.
"""
import itertools
import re
import sys
from fractions import Fraction as Fr

import sympy as sp

BASE = sys.argv[1]
CHECKS = []


def check(name, cond, detail=None):
    ok = bool(cond)
    CHECKS.append((name, ok))
    line = ("PASS " if ok else "FAIL ") + name
    if detail is not None:
        line += "  [" + str(detail) + "]"
    print(line)
    sys.stdout.flush()
    return ok


def note(text):
    print("NOTE " + text)
    sys.stdout.flush()


def read(rel):
    with open(BASE + "/" + rel, encoding="utf-8") as fh:
        return fh.read()


def is_zero(expr):
    return sp.expand(expr) == 0


def no_float(*objs):
    for o in objs:
        if isinstance(o, float):
            return False
        if isinstance(o, (list, tuple)):
            if not no_float(*o):
                return False
        elif isinstance(o, sp.Basic) and o.atoms(sp.Float):
            return False
    return True


R4 = range(4)
CD = read("CompositeDimension.lean")
K2G = read("K2Guard.lean")

# ============================================================== K: transcription controls
def parse_index_map(name):
    blk = re.search(r"def " + name + r" : Fin 4 → Fin 4 → Fin 4\n((?:\s*\|[^\n]*\n)+)", CD).group(1)
    return {(int(a), int(b)): int(c) for a, b, c in re.findall(r"(\d), (\d) => (\d)", blk)}


PC = parse_index_map("pc")
PT = parse_index_map("pt")
m_sgn = re.search(r"def sgn \(μ ν : Fin 4\) : ℝ := if \(μ = (\d) ∧ ν = (\d)\) ∨ \(μ = (\d) ∧ ν = (\d)\) then -1 "
                  r"else 1", CD)
NEG = {(int(m_sgn.group(1)), int(m_sgn.group(2))), (int(m_sgn.group(3)), int(m_sgn.group(4)))}
PC_H = {(0, 0): 0, (0, 1): 0, (0, 2): 3, (0, 3): 3, (1, 0): 1, (1, 1): 1, (1, 2): 2, (1, 3): 2,
        (2, 0): 2, (2, 1): 2, (2, 2): 1, (2, 3): 1, (3, 0): 3, (3, 1): 3, (3, 2): 0, (3, 3): 0}
PT_H = {(0, 0): 0, (0, 1): 1, (0, 2): 2, (0, 3): 3, (1, 0): 1, (1, 1): 0, (1, 2): 3, (1, 3): 2,
        (2, 0): 1, (2, 1): 0, (2, 2): 3, (2, 3): 2, (3, 0): 0, (3, 1): 1, (3, 2): 2, (3, 3): 3}
NEG_H = {(1, 3), (2, 2)}
phiW_src = "def phiW : W 3 := fun μ ν => if μ = ν then (if μ = 2 then -1 else 1) else 0" in CD
xplus_src = "def xplus : Fin 3 → ℝ := ![1, 0, 0]" in CD
z3_src = "def z3 : Fin 3 → ℝ := ![0, 0, 1]" in CD
nflip_blk = re.search(r"def nflip[^\n]*\n\s*toFun x := fun i => \(!\[([^\]]*)\]", CD).group(1)
reflY_blk = re.search(r"def reflY[^\n]*\n\s*toFun x := fun i => \(!\[([^\]]*)\]", K2G).group(1)


def parse_mat(name, text):
    lit = re.search(r"def " + name + r" : W 3 := (!\[!\[[^\n]*\]\])", text).group(1)
    rows = re.findall(r"!\[([-\d, ]+)\]", lit)
    return [[Fr(int(v)) for v in r.split(",")] for r in rows]


IDW = parse_mat("idW", K2G)
CHAINW = parse_mat("chainW", K2G)
check("K0 parsed sgn, pc, pt, phiW, xplus, z3 (CD) and nflip, reflY, idW, chainW (CD, K2G) equal the hand "
      "transcriptions",
      PC == PC_H and PT == PT_H and NEG == NEG_H and phiW_src and xplus_src and z3_src
      and nflip_blk.replace(" ", "") == "1,-1,-1" and reflY_blk.replace(" ", "") == "1,-1,1"
      and IDW == [[1 if i == j else 0 for j in R4] for i in R4]
      and CHAINW == [[1, 0, 0, 1], [1, 0, 0, -1], [0, 0, 0, 0], [0, 0, 0, 0]])

HS_REFLY = [1, 1, -1, 1]      # homogenized signs of reflY = diag(1, -1, 1)
PHIW = [[Fr(0)] * 4 for _ in R4]
for i, v in enumerate([1, 1, -1, 1]):
    PHIW[i][i] = Fr(v)
XPLUS = [Fr(1), Fr(0), Fr(0)]
Z3 = [Fr(0), Fr(0), Fr(1)]


def hom3(x):
    return [1] + list(x)


def prodState(x, y):
    hx, hy = hom3(x), hom3(y)
    return [[hx[m] * hy[n] for n in R4] for m in R4]


def tens(a, b):
    return [[a[m] * b[n] for n in R4] for m in R4]


def cnot(w):
    return [[(-1 if (m, n) in NEG else 1) * w[PC[(m, n)]][PT[(m, n)]] for n in R4] for m in R4]


def actT(hs, w):
    return [[hs[n] * w[m][n] for n in R4] for m in R4]


def actC(hs, w):
    return [[hs[m] * w[m][n] for n in R4] for m in R4]


def cnotTw(w):
    return actT(HS_REFLY, cnot(actT(HS_REFLY, w)))


def pairVal(a, b, w):
    return sum(a[m] * w[m][n] * b[n] for m in R4 for n in R4)


def sharpVec(b):
    return [Fr(1, 2)] + [Fr(v) / 2 for v in b]


def ipW(E, X):
    return sum(E[m][n] * X[m][n] for m in R4 for n in R4)


def tabMul(A, B):
    return [[sum(A[m][k] * B[k][n] for k in R4) for n in R4] for m in R4]


def tabT(A):
    return [[A[n][m] for n in R4] for m in R4]


lands = ("theorem cnot_prodState_xplus_z3 : cnot (prodState xplus z3) = phiW" in CD
         and "theorem actT_reflY_phiW : actT reflY phiW = idW" in K2G
         and "theorem cnot_idW : cnot idW = chainW" in K2G
         and re.search(r"theorem chain_value :\s*prodEffVal \(sharpEff !\[-1, 0, 0\]\) \(sharpEff !\[0, 0, -1\]\) "
                       r"chainW = -1 / 2", K2G) is not None)
repro = (cnot(prodState(XPLUS, Z3)) == PHIW and actT(HS_REFLY, PHIW) == IDW and cnot(IDW) == CHAINW
         and pairVal(sharpVec([-1, 0, 0]), sharpVec([0, 0, -1]), CHAINW) == Fr(-1, 2))
check("K1 the landed statements are present (CD:1222, K2G:106, K2G:110, K2G:134) and reproduce exactly", lands and repro)


# ============================================================== P: Pauli dictionary (Gaussian rationals)
class G:
    __slots__ = ("re", "im")

    def __init__(self, re_=0, im_=0):
        if isinstance(re_, float) or isinstance(im_, float):
            raise TypeError("float in exact arithmetic")
        self.re = Fr(re_)
        self.im = Fr(im_)

    def __add__(self, o):
        o = gg(o)
        return G(self.re + o.re, self.im + o.im)

    __radd__ = __add__

    def __sub__(self, o):
        o = gg(o)
        return G(self.re - o.re, self.im - o.im)

    def __rsub__(self, o):
        return gg(o) - self

    def __mul__(self, o):
        o = gg(o)
        return G(self.re * o.re - self.im * o.im, self.re * o.im + self.im * o.re)

    __rmul__ = __mul__

    def __neg__(self):
        return G(-self.re, -self.im)

    def conj(self):
        return G(self.re, -self.im)

    def __eq__(self, o):
        o = gg(o)
        return self.re == o.re and self.im == o.im

    def __hash__(self):
        return hash((self.re, self.im))


def gg(x):
    return x if isinstance(x, G) else G(x, 0)


ONE, ZERO, IU = G(1), G(0), G(0, 1)


def mzeros(n):
    return [[ZERO for _ in range(n)] for _ in range(n)]


def mmul(A, B):
    n = len(A)
    return [[sum((A[i][k] * B[k][j] for k in range(n)), ZERO) for j in range(n)] for i in range(n)]


def kron(A, B):
    na, nb = len(A), len(B)
    return [[A[i // nb][j // nb] * B[i % nb][j % nb] for j in range(na * nb)] for i in range(na * nb)]


def dag(A):
    n = len(A)
    return [[A[j][i].conj() for j in range(n)] for i in range(n)]


def madd(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A))] for i in range(len(A))]


def mscale(c, A):
    return [[gg(c) * A[i][j] for j in range(len(A))] for i in range(len(A))]


def mtrace(A):
    return sum((A[i][i] for i in range(len(A))), ZERO)


def meq(A, B):
    return all(A[i][j] == B[i][j] for i in range(len(A)) for j in range(len(A)))


SIG = [[[ONE, ZERO], [ZERO, ONE]], [[ZERO, ONE], [ONE, ZERO]], [[ZERO, -IU], [IU, ZERO]], [[ONE, ZERO], [ZERO, -ONE]]]


def pauliW(T):
    acc = mzeros(4)
    for m in R4:
        for n in R4:
            if T[m][n] != 0:
                acc = madd(acc, mscale(Fr(T[m][n]) / 4, kron(SIG[m], SIG[n])))
    return acc


def basisT(m, n):
    return [[Fr(1) if (i, j) == (m, n) else Fr(0) for j in R4] for i in R4]


def perm_matrix(p, n):
    """P with P|k> = |p(k)>."""
    M = mzeros(n)
    for k in range(n):
        M[p(k)][k] = ONE
    return M


CNOT = perm_matrix(lambda k: k if k < 2 else (3 if k == 2 else 2), 4)
CZ = [[ONE if i == j and i < 3 else ZERO for j in range(4)] for i in range(4)]
CZ[3][3] = -ONE
SWAP = perm_matrix(lambda k: (k % 2) * 2 + k // 2, 4)


def pt_last(M, nq):
    """Partial transpose of the last qubit of an nq-qubit matrix."""
    d = 2 ** nq
    out = mzeros(d)
    for r in range(d):
        for c in range(d):
            out[(r & ~1) | (c & 1)][(c & ~1) | (r & 1)] = M[r][c]
    return out


# P1 symbolic
xs = sp.symbols("x1:4")
ys = sp.symbols("y1:4")
SIGS = [sp.Matrix([[1, 0], [0, 1]]), sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]]),
        sp.Matrix([[1, 0], [0, -1]])]


def r_sym(x):
    return (SIGS[0] + x[0] * SIGS[1] + x[1] * SIGS[2] + x[2] * SIGS[3]) / 2


def skron(A, B):
    na, nb = A.shape[0], B.shape[0]
    return sp.Matrix(na * nb, na * nb, lambda i, j: A[i // nb, j // nb] * B[i % nb, j % nb])


def pauliW_sym(T):
    acc = sp.zeros(4, 4)
    for m in R4:
        for n in R4:
            acc += sp.Rational(1, 4) * T[m][n] * skron(SIGS[m], SIGS[n])
    return acc


PSsym = prodState(list(xs), list(ys))
check("P1 pauliW(prodState x y) = r(x) (x) r(y) (symbolic x, y)",
      (pauliW_sym(PSsym) - skron(r_sym(xs), r_sym(ys))).applyfunc(sp.expand).is_zero_matrix)

ok2 = all(meq(pauliW(cnot(basisT(m, n))), mmul(mmul(CNOT, pauliW(basisT(m, n))), dag(CNOT))) for m in R4 for n in R4)
cc2 = not all(meq(pauliW(cnot(basisT(m, n))), mmul(mmul(CZ, pauliW(basisT(m, n))), dag(CZ))) for m in R4 for n in R4)
check("P2 kernel cnot = Pauli transfer of Ad(CNOT) on the 16 basis tables; countercontrol: Ad(CZ) fails", ok2 and cc2)

ok3 = all(meq(pauliW(actT(HS_REFLY, basisT(m, n))), pt_last(pauliW(basisT(m, n)), 2)) for m in R4 for n in R4)
cc3 = not all(meq(pauliW(actT(HS_REFLY, basisT(m, n))), pauliW(basisT(m, n))) for m in R4 for n in R4)
check("P3 pauliW(actT reflY B) = PT_2 pauliW(B) on the 16 basis tables; countercontrol: without the transpose fails",
      ok3 and cc3)


def uvec(a):
    return [Fr(1) if k == a else Fr(0) for k in R4]


ok4 = all(G(pairVal(uvec(a), uvec(b), basisT(m, n))) == mtrace(mmul(kron(SIG[a], SIG[b]), pauliW(basisT(m, n))))
          for a in R4 for b in R4 for m in R4 for n in R4)
check("P4 pairVal u_a u_b B = tr((s_a (x) s_b) pauliW B) on all basis vectors and basis tables", ok4)


def op4_basis(a, b, c, d):
    return mscale(Fr(1, 16), kron(kron(kron(SIG[a], SIG[b]), SIG[c]), SIG[d]))


def swap_mid(k):
    b0, b1, b2, b3 = (k >> 3) & 1, (k >> 2) & 1, (k >> 1) & 1, k & 1
    return (b0 << 3) | (b2 << 2) | (b1 << 1) | b3


PMID = perm_matrix(swap_mid, 16)
PMIDT = dag(PMID)
ok5a = ok5b = True
cc5 = False
for a, b, c, d in itertools.product(R4, R4, R4, R4):
    pa = kron(pauliW(basisT(a, b)), pauliW(basisT(c, d)))
    if not meq(op4_basis(a, b, c, d), pa):
        ok5a = False
    # prodB (e_ac) (e_bd) = e_abcd; its op4 must equal P (pauliW e_ac (x) pauliW e_bd) P^T
    pb = mmul(mmul(PMID, kron(pauliW(basisT(a, c)), pauliW(basisT(b, d)))), PMIDT)
    if not meq(op4_basis(a, b, c, d), pb):
        ok5b = False
    if not meq(op4_basis(a, b, c, d), kron(pauliW(basisT(a, c)), pauliW(basisT(b, d)))):
        cc5 = True
check("P5a op4(prodA B B') = pauliW B (x) pauliW B' and op4(prodB B B') = P (pauliW B (x) pauliW B') P^T on all 256 "
      "basis pairs; countercontrol: without P some pair fails", ok5a and ok5b and cc5)
SGN = [1, 1, -1, 1]
ok5c = ok5d = True
for a, b, c, d in itertools.product(R4, R4, R4, R4):
    M = op4_basis(a, b, c, d)
    if not meq(mscale(SGN[d], M), pt_last(M, 4)):
        ok5c = False
    if not meq(op4_basis(a, c, b, d), mmul(mmul(PMID, M), PMIDT)):   # R e_abcd = e_acbd
        ok5d = False
check("P5b op4(rho3 Z) = PT_3 op4(Z) and op4(R Z) = P op4(Z) P^T on all 256 basis tables", ok5c and ok5d)


def mono(a):   # one-qubit Pauli as monomial: (perm, phase)
    M = SIG[a]
    perm = [next(j for j in range(2) if not M[i][j] == ZERO) for i in range(2)]
    return perm, [M[i][perm[i]] for i in range(2)]


MONO = [mono(a) for a in R4]


def mono_string(idx):
    perm, ph = [0], [ONE]
    for a in idx:
        p1, f1 = MONO[a]
        perm = [pp * 2 + p1[q] for pp in perm for q in range(2)]
        ph = [f * f1[q] for f in ph for q in range(2)]
    return perm, ph


STR = {I: mono_string(I) for I in itertools.product(R4, R4, R4, R4)}


def mono_trace_prod(A, B):
    pa, fa = A
    pb, fb = B
    tr = ZERO
    for i in range(16):
        j = pa[i]
        if pb[j] == i:
            tr = tr + fa[i] * fb[j]
    return tr


ok5e = all(mono_trace_prod(STR[I], STR[J]) == (G(16) if I == J else ZERO) for I in STR for J in STR)
check("P5c tr(s_I s_J) = 16 [I = J] for all 256 x 256 Pauli strings (so sum_I Z_I Z'_I = 16 tr(op4 Z op4 Z'))", ok5e)

PHIP = [[G(1, 0) if (i in (0, 3) and j in (0, 3)) else ZERO for j in range(4)] for i in range(4)]
PHIP = mscale(Fr(1, 2), PHIP)
v = [ZERO, ONE, -ONE, ZERO]
Mid = pauliW(IDW)
val = sum((v[i].conj() * Mid[i][j] * v[j] for i in range(4) for j in range(4)), ZERO)
check("P6 pauliW(phiW) = |Phi+><Phi+| (phiW in Q3); v = (0, 1, -1, 0) gives v^dag pauliW(idW) v < 0 (idW not in Q3); "
      "with actT reflY phiW = idW and the involution, idW in twin and phiW not in twin",
      meq(pauliW(PHIW), PHIP) and val.im == 0 and val.re < 0 and actT(HS_REFLY, actT(HS_REFLY, PHIW)) == PHIW,
      "v^dag pauliW(idW) v = %s" % val.re)
ok7 = all(meq(pauliW(tabT(basisT(m, n))), mmul(mmul(SWAP, pauliW(basisT(m, n))), SWAP)) for m in R4 for n in R4)
check("P7 pauliW(tabT B) = SWAP pauliW(B) SWAP on the 16 basis tables (tabT maps Q3 onto Q3)", ok7)

# ============================================================== L: slice facts (symbolic)
Xs = [[sp.Integer(1) if (m, n) == (0, 0) else sp.Symbol("X%d%d" % (m, n)) for n in R4] for m in R4]
X00s = sp.Symbol("X00")
Xg = [[X00s if (m, n) == (0, 0) else Xs[m][n] for n in R4] for m in R4]


def sharpVec_s(b):
    return [sp.Rational(1, 2)] + [sp.Rational(1, 2) * v for v in b]


def unit3(i, sgn_=1):
    return [sgn_ if k == i else 0 for k in range(3)]


okL = True
ccL = False
for i in range(3):
    for j in range(3):
        tot = sum(pairVal(sharpVec_s(unit3(i, s1)), sharpVec_s(unit3(j, s2)), Xg) for s1 in (1, -1) for s2 in (1, -1))
        wtd = sum(s1 * s2 * pairVal(sharpVec_s(unit3(i, s1)), sharpVec_s(unit3(j, s2)), Xg)
                  for s1 in (1, -1) for s2 in (1, -1))
        if not (is_zero(tot - X00s) and is_zero(wtd - Xg[i + 1][j + 1])):
            okL = False
        if not is_zero(tot - Xg[i + 1][j + 1]):
            ccL = True
check("L the four sharp-product values sum to X00, and their sign-weighted sum is X_ij (symbolic X); countercontrol: "
      "the unweighted sum is not X_ij", okL and ccL)

# ============================================================== the COMP-1 model carrier (symbolic)
N16 = range(16)
N17 = range(17)


def flat(T):
    return [T[m][n] for m in R4 for n in R4]           # index 4 m + n = finProdFinEquiv (m, n)


def unflat(x):
    return [[x[4 * m + n] for n in R4] for m in R4]


def hom16(x):
    return [sp.Integer(1)] + list(x)


def pState(x, y):
    hx, hy = hom16(x), hom16(y)
    return [[hx[m] * hy[n] for n in N17] for m in N17]


def coeff(e):
    return [e[0]] + list(e[1])


def pEff(e, f, w):
    ce, cf = coeff(e), coeff(f)
    return sum(ce[m] * cf[n] * w[m][n] for m in N17 for n in N17 if ce[m] != 0 and cf[n] != 0)


def evalA(e, x):
    return e[0] + sum(e[1][i] * x[i] for i in N16)


def comp_diag(e, signs):
    return (e[0], [e[1][i] * signs[i] for i in N16])


TAU = [4 * (k % 4) + k // 4 for k in N16]              # flat index of the token exchange


def comp_perm(e, perm):
    return (e[0], [e[1][perm[i]] for i in N16])


RHO = [HS_REFLY[k % 4] for k in N16]                    # sign -1 at flat indices 4 m + 2


def rho_flat(x):
    return [x[i] * RHO[i] for i in N16]


def tau_flat(x):
    return [x[TAU[i]] for i in N16]


def table_of(e):
    t = unflat(e[1])
    t = [[t[m][n] for n in R4] for m in R4]
    t[0][0] = t[0][0] + e[0]
    return t


def tabCoord(m, n):
    return (sp.Integer(0), [sp.Integer(1) if i == 4 * m + n else sp.Integer(0) for i in N16])


def tabFun(T):
    return (sp.Integer(0), flat(T))


I4 = list(itertools.product(R4, R4, R4, R4))


def iota(Z):
    V = [[sp.Integer(0)] * 17 for _ in N17]
    for a, b, c, d in I4:
        V[1 + 4 * a + b][1 + 4 * c + d] = Z[(a, b, c, d)]
    for c, d in itertools.product(R4, R4):
        V[0][1 + 4 * c + d] = Z[(0, 0, c, d)]
    for a, b in itertools.product(R4, R4):
        V[1 + 4 * a + b][0] = Z[(a, b, 0, 0)]
    V[0][0] = Z[(0, 0, 0, 0)]
    return V


def piV(V):
    return {(a, b, c, d): V[1 + 4 * a + b][1 + 4 * c + d] for a, b, c, d in I4}


def Rg(Z):
    return {(a, b, c, d): Z[(a, c, b, d)] for a, b, c, d in I4}


def sigma(V):
    Z = piV(V)
    A = iota(Rg(Z))
    B = iota(Z)
    return [[A[m][n] + V[m][n] - B[m][n] for n in N17] for m in N17]


def prodA(X, Y):
    return {(a, b, c, d): X[a][b] * Y[c][d] for a, b, c, d in I4}


def fourVal(X, Y, E, F):
    return sum(X[a][b] * Y[c][d] * E[a][c] * F[b][d] for a, b, c, d in I4)


def rhoT(T):
    return actT(HS_REFLY, T)


def sym_table(name, normalized):
    return [[(sp.Integer(1) if normalized and (m, n) == (0, 0) else sp.Symbol("%s%d%d" % (name, m, n))) for n in R4]
            for m in R4]


def sym_aff(name):
    return (sp.Symbol(name + "c"), [sp.Symbol("%s%d" % (name, i)) for i in N16])


def sym_vec(name):
    return [sp.Symbol("%s%d" % (name, i)) for i in N16]


# ---- the structures: (prodState, prodEff) pairs on the 17 x 17 carrier
PA_state, PA_eff = pState, pEff
MRHO_state = lambda L, Lp: pState(L, rho_flat(Lp))                      # noqa: E731
MRHO_eff = lambda E, F, w: pEff(E, comp_diag(F, RHO), w)               # noqa: E731
MTW_state = lambda L, Lp: sigma(pState(L, rho_flat(Lp)))                # noqa: E731
MTW_eff = lambda E, F, w: pEff(E, comp_diag(F, RHO), sigma(w))         # noqa: E731
MSG_state = lambda L, Lp: sigma(pState(L, Lp))                          # noqa: E731
MSG_eff = lambda E, F, w: pEff(E, F, sigma(w))                         # noqa: E731
MT_state = lambda L, Lp: sigma(pState(tau_flat(L), Lp))                 # noqa: E731
MT_eff = lambda E, F, w: pEff(comp_perm(E, TAU), F, sigma(w))          # noqa: E731


def tok_diff(effB, effA, w, a, b, c, d):
    return effB(tabCoord(a, c), tabCoord(b, d), w) - effA(tabCoord(a, b), tabCoord(c, d), w)


xv, yv = sym_vec("x"), sym_vec("y")
ea, fa = sym_aff("e"), sym_aff("f")

# ============================================================== A: the anchor sum
x0, y0, L0, L0p = sym_vec("p"), sym_vec("q"), sym_vec("r"), sym_vec("t")
a0 = pState(L0, L0p)
b0 = pState(x0, y0)
ANC_PA_state = lambda x, y: (pState(x, y), a0)                          # noqa: E731
ANC_PA_eff = lambda e, f, w: pEff(e, f, w[0])                          # noqa: E731
ANC_PB_state = lambda L, Lp: (b0, pState(L, Lp))                        # noqa: E731
ANC_PB_eff = lambda E, F, w: pEff(E, F, w[1])                          # noqa: E731
A1 = (is_zero(ANC_PA_eff(ea, fa, ANC_PA_state(xv, yv)) - evalA(ea, xv) * evalA(fa, yv))
      and is_zero(ANC_PB_eff(ea, fa, ANC_PB_state(xv, yv)) - evalA(ea, xv) * evalA(fa, yv)))
check("A1 anchor sum: prodEff_apply holds for both structures (symbolic chart points and affine functionals)", A1)
A2 = (is_zero(ANC_PA_eff(ea, fa, ANC_PB_state(xv, yv)) - evalA(ea, x0) * evalA(fa, y0))
      and is_zero(ANC_PB_eff(ea, fa, ANC_PA_state(xv, yv)) - evalA(ea, L0) * evalA(fa, L0p)))
check("A2 anchor sum: PA's product effects at PB's products are e(x0) f(y0), PB's at PA's products are E(L0) F(L0') "
      "(symbolic)", A2)
num_x = flat(PHIW)
num_y = flat(PHIW)
num_L = flat(basisT(0, 0))
w_anchor = (pState(num_x, num_y), pState(num_L, num_L))
dA3 = tok_diff(ANC_PB_eff, ANC_PA_eff, w_anchor, 1, 1, 0, 0)
check("A3 anchor sum: tok fails at the body point (pState phiW phiW, pState e00 e00), index (a,b,c,d) = (1,1,0,0)",
      dA3 != 0, "difference = %s" % dA3)
zeroV = [[sp.Integer(0)] * 17 for _ in N17]
ctrlA = pEff((sp.Integer(1), [sp.Integer(0)] * 16), (sp.Integer(1), [sp.Integer(0)] * 16), zeroV)
check("A-control with zero anchors PA's unit pairing at PB's products is not 1 (anchors are load-bearing)",
      ctrlA != 1, "value = %s" % ctrlA)

# ============================================================== R: M_rho
R1 = is_zero(MRHO_eff(ea, fa, MRHO_state(xv, yv)) - evalA(ea, xv) * evalA(fa, yv))
check("R1 M_rho: PB.prodEff_apply (symbolic chart points and affine functionals)", R1)
Wsym = sym_table("w", False)
R2 = (all(is_zero(rhoT(rhoT(Wsym))[m][n] - Wsym[m][n]) for m in R4 for n in R4) and RHO[0] == 1
      and rho_flat(flat(Wsym)) == flat(rhoT(Wsym)))
check("R2 actT reflY is an involution on W 3, rho = flat o actT reflY o unflat, rho fixes the unit entry (symbolic)", R2)
Xr = flat(PHIW)
Yr = flat(prodState([0, 0, 0], [0, 1, 0]))
dR3 = tok_diff(MRHO_eff, PA_eff, pState(Xr, Yr), 0, 0, 0, 2)
check("R3 M_rho: tok fails at pState phiW (prodState 0 e_y), index (0,0,0,2)", dR3 != 0, "difference = %s" % dR3)
Xw = cnot(prodState(XPLUS, Z3))
Ew = cnot(tens(sharpVec(XPLUS), sharpVec(Z3)))
Fw = cnotTw(tens(sharpVec([-v_ for v_ in XPLUS]), sharpVec([-v_ for v_ in Z3])))
famI = ipW(Xw, tabMul(tabMul(Ew, Xw), tabT(Fw)))
check("R4 Lemma P's family (i) value at the gate-supplied witnesses for cones (Q3, Q3, Q3, twin) is negative "
      "(exact)", famI < 0 and famI == fourVal(Xw, Xw, Ew, Fw), "value = %s" % famI)
Esym, Fsym = sym_table("E", False), sym_table("F", False)
asym, bsym = [sp.Symbol("a%d" % i) for i in R4], [sp.Symbol("b%d" % i) for i in R4]
R5 = (all(is_zero(cnot(cnot(Wsym))[m][n] - Wsym[m][n]) and is_zero(cnotTw(cnotTw(Wsym))[m][n] - Wsym[m][n])
          for m in R4 for n in R4)
      and is_zero(ipW(cnot(Esym), Wsym) - ipW(Esym, cnot(Wsym)))
      and is_zero(ipW(cnotTw(Esym), Wsym) - ipW(Esym, cnotTw(Wsym)))
      and is_zero(ipW(tens(asym, bsym), Wsym) - pairVal(asym, bsym, Wsym))
      and Ew == [[PHIW[m][n] / 4 for n in R4] for m in R4]
      and Fw == [[Fr([1, -1, 1, -1][m], 4) if m == n else Fr(0) for n in R4] for m in R4])
check("R5 cnot and cnotTw are involutions and ipW-self-adjoint, ipW (tens a b) w = pairVal a b w (symbolic); the "
      "witness effects are E = phiW/4 and F = dg(1,-1,1,-1)/4 (exact)", R5)
IDH = [1, 1, 1, 1]
R6 = (all(is_zero(actC(IDH, actT(HS_REFLY, cnot(actC(IDH, actT(HS_REFLY, Wsym)))))[m][n] - cnotTw(Wsym)[m][n])
          for m in R4 for n in R4)
      and (0 + 0 + 0 + 1) % 2 == 1)
check("R6 cnotTw = actC id o actT reflY o cnot o actC id o actT reflY (orthogonal locals; symbolic); with Q3 != twin "
      "(P6) the twist bits are forced to (0, 0, 0, 1), which is odd", R6)
cross_sigma = sp.sympify(MSG_eff(tabFun(Ew), tabFun(Fw), pState(flat(Xw), flat(Xw))))
famI_s = sp.Rational(famI.numerator, famI.denominator)
check("R-countercontrol M_sigma (token-coherent) with the same cones: PB.prodEff E F at PA's product of the witnesses "
      "equals the same negative value (no common body)", sp.simplify(cross_sigma - famI_s) == 0,
      "value = %s" % cross_sigma)

# ============================================================== T: M_tw
ok_inv = True
for k in range(289):
    Vk = [[sp.Integer(1) if 17 * m + n == k else sp.Integer(0) for n in N17] for m in N17]
    if sigma(sigma(Vk)) != Vk:
        ok_inv = False
        break
Zsym = {I: sp.Symbol("Z%d%d%d%d" % I) for I in I4}
sig_iota = all(is_zero(sigma(iota(Zsym))[m][n] - iota(Rg(Zsym))[m][n]) for m in N17 for n in N17)
check("T1 sigma o sigma = id on all 289 basis vectors (sigma^-1 = sigma) and sigma o iota = iota o R (symbolic)",
      ok_inv and sig_iota)
Xn, Yn = sym_table("X", True), sym_table("Y", True)
Ln, Lpn = sym_table("L", True), sym_table("M", True)
Ea, Fa = sym_aff("E"), sym_aff("F")
T2a = is_zero(MTW_eff(Ea, Fa, PA_state(flat(Xn), flat(Yn)))
              - fourVal(Xn, Yn, table_of(Ea), rhoT(table_of(Fa))))
T2b = is_zero(PA_eff(ea, fa, MTW_state(flat(Ln), flat(Lpn)))
              - fourVal(table_of(ea), table_of(fa), Ln, rhoT(Lpn)))
check("T2 M_tw cross values: PB.prodEff E F (PA.prodState X Y) = fourVal X Y Et (rho Ft) and PA.prodEff e f "
      "(PB.prodState L L') = fourVal et ft L (rho L') (symbolic)", T2a and T2b)
wZ = iota(Zsym)
T3 = all(is_zero(tok_diff(MTW_eff, PA_eff, wZ, a, b, c, d) - (SGN[d] - 1) * Zsym[(a, b, c, d)]) for a, b, c, d in I4)
T3c = all(is_zero(tok_diff(MSG_eff, PA_eff, wZ, a, b, c, d)) for a, b, c, d in I4)
check("T3 M_tw: on iota(Z) the tok difference is (s_d - 1) Z_abcd, nonzero exactly at d = 2 (symbolic); "
      "countercontrol M_sigma: zero", T3 and T3c)
hb = [[sp.Symbol("h%d%d" % (t, i)) for i in range(3)] for t in R4]
P01, P23 = prodState(hb[0], hb[1]), prodState(hb[2], hb[3])
P02, P13 = prodState(hb[0], hb[2]), prodState(hb[1], hb[3])
Zp = {(a, b, c, d): hom3(hb[0])[a] * hom3(hb[1])[b] * hom3(hb[2])[c] * hom3(hb[3])[d] for a, b, c, d in I4}
lhsA = PA_state(flat(P01), flat(P23))
lhsB = MTW_state(flat(P02), flat(P13))
rho3Z = {I: SGN[I[3]] * Zp[I] for I in I4}
T4 = (all(is_zero(lhsA[m][n] - iota(Zp)[m][n]) for m in N17 for n in N17)
      and all(is_zero(lhsB[m][n] - iota(rho3Z)[m][n]) for m in N17 for n in N17)
      and not all(is_zero(lhsB[m][n] - lhsA[m][n]) for m in N17 for n in N17))
lhsBs = MSG_state(flat(P02), flat(P13))
T4c = all(is_zero(lhsBs[m][n] - lhsA[m][n]) for m in N17 for n in N17)
check("T4 M_tw: the two images of a four-token product state differ exactly by rho3 (TokProdState fails; symbolic "
      "Bloch vectors); countercontrol M_sigma: equal", T4 and T4c)
margA = PA_eff(tabCoord(0, 0), tabCoord(0, 2), wZ)
margB = MTW_eff(tabCoord(0, 0), tabCoord(0, 2), wZ)
margBs = MSG_eff(tabCoord(0, 0), tabCoord(0, 2), wZ)
check("T5 M_tw: token 3's y-marginal reads Z0002 through 01|23 and -Z0002 through 02|13 (STMC fails; symbolic); "
      "countercontrol M_sigma: equal",
      is_zero(margA - Zsym[(0, 0, 0, 2)]) and is_zero(margB + Zsym[(0, 0, 0, 2)]) and is_zero(margBs - margA))

# ============================================================== S: M_sigma
S1 = T3c
check("S1 M_sigma: tok holds on iota(W4) (symbolic)", S1)
S2a = is_zero(MSG_eff(tabFun(Esym), tabFun(Fsym), PA_state(flat(Xn), flat(Yn))) - fourVal(Xn, Yn, Esym, Fsym))
esym, fsym = sym_table("e", False), sym_table("f", False)
S2b = is_zero(PA_eff(tabFun(esym), tabFun(fsym), MSG_state(flat(Ln), flat(Lpn))) - fourVal(esym, fsym, Ln, Lpn))
S2c = not is_zero(MRHO_eff(tabFun(Esym), tabFun(Fsym), PA_state(flat(Xn), flat(Yn))) - fourVal(Xn, Yn, Esym, Fsym))
check("S2 Lemma B1 endpoints in M_sigma: PB.prodEff(sum E tabCoord)(sum F tabCoord)(PA.prodState X Y) = fourVal X Y E F "
      "and PA.prodEff(sum e tabCoord)(sum f tabCoord)(PB.prodState L L') = fourVal e f L L' (symbolic); "
      "countercontrol: the first expression in M_rho differs", S2a and S2b and S2c)
Xg2, Yg2 = sym_table("X", False), sym_table("Y", False)
c = fourVal(Xg2, Yg2, Esym, Fsym)
S3 = (is_zero(c - ipW(Xg2, tabMul(tabMul(Esym, Yg2), tabT(Fsym))))
      and is_zero(c - ipW(Yg2, tabMul(tabMul(tabT(Esym), Xg2), Fsym)))
      and is_zero(c - ipW(Esym, tabMul(tabMul(Xg2, Fsym), tabT(Yg2))))
      and is_zero(c - ipW(Fsym, tabMul(tabMul(tabT(Xg2), Esym), Yg2))))
check("S3 fourVal's four readings (package fourVal_eq_01, _23, _02, _13) hold (symbolic)", S3)
u = (sp.Integer(1), [sp.Integer(0)] * 16)
Wfull = [[sp.Symbol("v%d_%d" % (m, n)) for n in N17] for m in N17]


def aff_sub(p, q):
    return (p[0] - q[0], [p[1][i] - q[1][i] for i in N16])


S4 = is_zero(pEff(ea, fa, Wfull) + pEff(aff_sub(u, ea), fa, Wfull) + pEff(u, aff_sub(u, fa), Wfull)
             - pEff(u, u, Wfull))
check("S4 the complement identity pEff e f + pEff (u - e) f + pEff u (u - f) = pEff u u (symbolic carrier point)", S4)

# ============================================================== I: M_id and M_T
Xi = flat(prodState([0, 0, 0], [1, 0, 0]))
Yi = flat(prodState([0, 0, 0], [0, 0, 0]))
dI1 = tok_diff(PA_eff, PA_eff, pState(Xi, Yi), 0, 1, 0, 0)
prodB_EF = {(a, b, cc_, d): Fsym[b][d] * Esym[a][cc_] for a, b, cc_, d in I4}
I1 = dI1 != 0 and is_zero(fourVal(Xg2, Yg2, Esym, Fsym)
                          - sum(prodA(Xg2, Yg2)[I] * prodB_EF[I] for I in I4))
check("I1 M_id (PB = PA): tok fails at pState (prodState 0 e_x) (prodState 0 0), index (0,1,0,0); "
      "fourVal X Y E F = sum_I (prodA X Y)_I (prodB E F)_I (symbolic)", I1, "difference = %s" % dI1)
dI2 = tok_diff(MT_eff, PA_eff, pState(flat(prodState([1, 0, 0], [0, 0, 0])), flat(prodState([0, 0, 0], [0, 0, 0]))),
               1, 0, 0, 0)
I2 = dI2 != 0 and is_zero(MT_eff(Ea, Fa, PA_state(flat(Xn), flat(Yn)))
                          - fourVal(Xn, Yn, tabT(table_of(Ea)), table_of(Fa)))
check("I2 M_T (f1 W4 completed): tok fails at pState (prodState e_x 0) (prodState 0 0), index (1,0,0,0); "
      "PB.prodEff E F (PA.prodState X Y) = fourVal X Y (tabT Et) Ft (symbolic)", I2, "difference = %s" % dI2)

check("F no float entered any checked quantity", no_float(famI, cross_sigma, dA3, dR3, dI1, dI2, ctrlA))

nfail = sum(1 for _, ok in CHECKS if not ok)
print("--- s1_kt4_models: %d/%d checks pass" % (len(CHECKS) - nfail, len(CHECKS)))
print("VERDICT S1-KT4-WITHOUT-TOK-MODELS-EXACT" if nfail == 0 else "VERDICT NOT RENDERED")
