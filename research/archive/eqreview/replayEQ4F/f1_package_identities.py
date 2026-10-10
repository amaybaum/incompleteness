"""EQ4-F exact identity checks for the four-copy formalization package (design only; base bcbc516f).

Own code: imports nothing from scratchpad/eq2, scratchpad/eq3 or scratchpad/eqreview.  Kernel conventions are typed
in by hand and re-parsed from the base text as a transcription control.
Usage:  python3 -I -B f1_package_identities.py <base>/verification/lean-mathlib/OIBridge

Conventions.  W 3 tables are 4 x 4 matrices, row = first token, index 0 = unit (CompositeDimension.lean:97, :100).
homMap N = 1 (+) N (CD:112); actT N w = w . homMap(N)^T (CD:198); actC N w = homMap(N) . w (CD:201).  The Euclidean
pairing <A, B> = sum A_mn B_mn.  Table product A.B is the matrix product (never the pointwise product).  The four-copy
contraction is c(X, Y, E, F) = sum_{a,b,c,d} X_ab Y_cd E_ac F_bd (tokens 0, 1, 2, 3; groupings 01|23 and 02|13).
Pauli dictionary (used only in block G): s0 = 1, s1 = X, s2 = Y, s3 = Z; pauliW(T) = (1/4) sum T_mn s_m (x) s_n.
Q3 = {T : pauliW(T) PSD}; Tw = actT reflY '' Q3, so T in Tw iff actT reflY T in Q3 (reflY is an involution).

DECISION RULE (fixed before the first run; rules, not expected numbers):
  K  transcription controls: parsed sgn/pc/pt (CD:741-755), phiW (CD:1220), xplus (CD:1213), z3 (CD:793), nflip
     (CD:797-798), reflY (K2Guard:46-47), idW and chainW (K2G:101-104) equal the hand transcriptions; the landed
     theorem statements cnot_prodState_xplus_z3 (CD:1222), actT_reflY_phiW (K2G:106), cnot_idW (K2G:110) are present
     in the text and reproduce numerically.
  R  target relabellings (symbolic generic tables X, Y, E, F): c(X, Y, E, F) equals <X, E.Y.F^T> (target 01),
     <Y, E^T.X.F> (target 23), <E, X.F.Y^T> (target 02) and <F, X^T.E.Y> (target 13); countercontrol: the target-23
     form without transposes, <Y, E.X.F^T>, differs from c (nonzero symbolic difference).
  W  four-copy cone level on the 256-entry carrier (symbolic): effA(e,f)(prodA X Y) = <e,X><f,Y>;
     effB(E,F)(prodB L L') = <E,L><F,L'>; effB(E,F)(prodA X Y) = c(X,Y,E,F); effA(e,f)(prodB L L') = c(e,f,L,L');
     token coherence effA(a b^T, c d^T) = effB(a c^T, b d^T) as functionals of a generic 256-entry table;
     countercontrol: with the 02 factor read transposed (effB'(E,F) = effB(E^T,F)) token coherence fails.
  C  cnot' = actT reflY . cnot . actT reflY (symbolic where stated): involution; orthogonal and symmetric as a 16 x 16
     matrix; fixes the unit entry; cnot'(prodState xplus z3) = idW; frame on the four corner products (corners z3, -z3);
     relT and relC with nflip (symbolic); cnot'(prodState x y) = actT reflY (cnot (prodState x (reflY y))) (symbolic).
  B  aligned parity from gate-supplied Bell data only (exact rationals): for each of the 16 assignments tau on
     (01, 23, 02, 13) with gates g_p = cnot^(tau_p) (cnot^0 = cnot, cnot^1 = cnot'), the states are g_p of the four
     corner products prodState(s xplus, t z3) and the effects are g_p of the corresponding sharp product effect tables
     sharpVec(s xplus) sharpVec(t z3)^T (s, t = +-1); the minimum over family (i) <X, E.Y.F^T> (X, Y states of 01, 23;
     E, F effects of 02, 13) and family (ii) <e, L.f.L'^T> (L, L' states of 02, 13; e, f effects of 01, 23) is
     negative iff tau_01 + tau_13 + tau_23 + tau_02 is odd.
  G  general charts (exact rational O(3) post-locals of both determinants; Q3 tested by all 15 principal minors of the
     Hermitian matrix pauliW, exact): controls pauliW(phiW) = |Phi+><Phi+|, pauliW(prodState x y) = rho(x) (x) rho(y)
     (symbolic), phiW in Q3 and not in Tw, idW in Tw and not in Q3; G1 for each determinant pattern of (A, B) and two
     draws, actC A (actT B phiW) is in Q3 iff det A det B = 1 and in Tw iff det A det B = -1; G2 for every tau in
     {0,1}^4 and two draws of post-locals with det A_p det B_p = (-1)^tau_p, Theta = actC R02 . actT R13
     (R_p = A_p reflY B_p^T) maps rep = actC A23 (actT B23 phiW) into C01 (Q3 if tau_01 = 0, else Tw) and not into
     the other cone iff the 4-cycle parity is even; G3 countercontrol: with R'_p = A2_p^T reflY B2_p from pre-locals
     whose determinant product is opposite on pair 02, the same test disagrees with the parity rule on some tau.
VERDICT F1-PACKAGE-IDENTITIES-EXACT iff every check passes; otherwise VERDICT NOT RENDERED.  Exact arithmetic only
(sympy Rationals, the Gaussian unit I, symbols; fractions.Fraction in block B); no solver calls.
"""
import itertools
import random
import re
import sys
from fractions import Fraction as Fr

import sympy as sp
from sympy import I, Matrix, Rational as R, eye, zeros

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


def Z(M):
    return M.applyfunc(sp.expand).is_zero_matrix


def no_float(*objs):
    return all(not sp.sympify(o).atoms(sp.Float) for o in objs)


# ------------------------------------------------------------------ K transcription (hand) and parse (base text)
HAND_NEG = [(1, 3), (2, 2)]
HAND_PC = [[0, 0, 3, 3], [1, 1, 2, 2], [2, 2, 1, 1], [3, 3, 0, 0]]
HAND_PT = [[0, 1, 2, 3], [1, 0, 3, 2], [1, 0, 3, 2], [0, 1, 2, 3]]
HAND_PHIW = sp.diag(1, 1, -1, 1)
HAND_IDW = eye(4)
HAND_CHAINW = Matrix([[1, 0, 0, 1], [1, 0, 0, -1], [0, 0, 0, 0], [0, 0, 0, 0]])
HAND_XPLUS = [1, 0, 0]
HAND_Z3 = [0, 0, 1]
HAND_NFLIP = [1, -1, -1]
HAND_REFLY = [1, -1, 1]

cd = open(BASE + "/CompositeDimension.lean", encoding="utf-8").read()
k2 = open(BASE + "/K2Guard.lean", encoding="utf-8").read()

i_s = cd.index("def sgn (μ ν : Fin 4) : ℝ :=")
sgn_line = cd[i_s:cd.index("\n", i_s)]
neg_parsed = sorted((int(a), int(b)) for a, b in re.findall(r"μ = (\d) ∧ ν = (\d)", sgn_line))


def parse_idx_table(name):
    i = cd.index("def " + name + " : Fin 4 → Fin 4 → Fin 4")
    block = cd[i:i + 400]
    tab = [[None] * 4 for _ in range(4)]
    for m, n, v in re.findall(r"\|\s*(\d),\s*(\d)\s*=>\s*(\d)", block)[:16]:
        tab[int(m)][int(n)] = int(v)
    return tab


i_p = cd.index("def phiW : W 3 :=")
phi_line = cd[i_p:cd.index("\n", i_p)].strip()


def parse_vec3(src, name):
    i = src.index("def " + name + " : Fin 3 → ℝ := ![")
    line = src[i:src.index("\n", i)]
    return [int(v) for v in re.search(r"!\[([-\d, ]+)\]", line).group(1).split(",")]


def parse_diag_map(src, name):
    i = src.index("def " + name + " : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ) where")
    block = src[i:i + 300]
    return [int(v) for v in re.search(r"toFun x := fun i => \(!\[([-\d, ]+)\] : Fin 3 → ℝ\) i \* x i",
                                      block).group(1).split(",")]


def parse_w3(src, name):
    i = src.index("def " + name + " : W 3 := ")
    line = src[i:src.index("\n", i)]
    rows = re.findall(r"!\[([-\d, ]+)\]", line)
    return Matrix([[int(v) for v in r.split(",")] for r in rows])


ok_k0 = (neg_parsed == HAND_NEG and "then -1 else 1" in sgn_line
         and parse_idx_table("pc") == HAND_PC and parse_idx_table("pt") == HAND_PT
         and phi_line == "def phiW : W 3 := fun μ ν => if μ = ν then (if μ = 2 then -1 else 1) else 0"
         and parse_vec3(cd, "xplus") == HAND_XPLUS and parse_vec3(cd, "z3") == HAND_Z3
         and parse_diag_map(cd, "nflip") == HAND_NFLIP and parse_diag_map(k2, "reflY") == HAND_REFLY
         and parse_w3(k2, "idW") == HAND_IDW and parse_w3(k2, "chainW") == HAND_CHAINW)
check("K0 parsed sgn, pc, pt, phiW, xplus, z3, nflip (CD), reflY, idW, chainW (K2G) equal the hand transcriptions",
      ok_k0)
ok_stmt = ("theorem cnot_prodState_xplus_z3 : cnot (prodState xplus z3) = phiW" in cd
           and "theorem actT_reflY_phiW : actT reflY phiW = idW" in k2
           and "theorem cnot_idW : cnot idW = chainW" in k2)


def sgn(m, n):
    return -1 if (m, n) in HAND_NEG else 1


def cnot(w):
    return Matrix(4, 4, lambda m, n: sgn(m, n) * w[HAND_PC[m][n], HAND_PT[m][n]])


def H(N):
    M = eye(4)
    M[1:, 1:] = Matrix(N)
    return M


def actT(N, w):
    return w * H(N).T


def actC(N, w):
    return H(N) * w


def hom(x):
    return Matrix([1] + list(x))


def prodState(x, y):
    return hom(x) * hom(y).T


def sharpVec(b):
    return Matrix([R(1, 2)] + [sp.S(v) / 2 for v in b])


REFLY = sp.diag(*HAND_REFLY)
NFLIP = sp.diag(*HAND_NFLIP)
DELTA = HAND_PHIW


def cnotp(w):                                     # cnot' = actT reflY . cnot . actT reflY
    return actT(REFLY, cnot(actT(REFLY, w)))


check("K1 the landed statements are present and reproduce: cnot(prodState xplus z3) = phiW (CD:1222), "
      "actT reflY phiW = idW (K2G:106), cnot idW = chainW (K2G:110)",
      ok_stmt and cnot(prodState(HAND_XPLUS, HAND_Z3)) == DELTA and actT(REFLY, DELTA) == HAND_IDW
      and cnot(HAND_IDW) == HAND_CHAINW)


def ip(A, B):
    return sp.expand(sum(A[m, n] * B[m, n] for m in range(4) for n in range(4)))


def symtab(p):
    return Matrix(4, 4, lambda m, n: sp.Symbol("%s%d%d" % (p, m, n), real=True))


# ------------------------------------------------------------------ R target relabellings
X, Y, E, F = symtab("x"), symtab("y"), symtab("e"), symtab("f")


def contract(X_, Y_, E_, F_):
    return sp.expand(sum(X_[a, b] * Y_[c, d] * E_[a, c] * F_[b, d]
                         for a, b, c, d in itertools.product(range(4), repeat=4)))


cval = contract(X, Y, E, F)
t01 = ip(X, E * Y * F.T)
t23 = ip(Y, E.T * X * F)
t02 = ip(E, X * F * Y.T)
t13 = ip(F, X.T * E * Y)
check("R1 target 01: c(X,Y,E,F) = <X, E.Y.F^T> (symbolic; family (i) and, renamed, family (ii) <e, L.f.L'^T>)",
      sp.expand(cval - t01) == 0)
check("R2 target 23: c(X,Y,E,F) = <Y, E^T.X.F> (symbolic; links read through the token exchange)",
      sp.expand(cval - t23) == 0)
check("R3 target 02: c(X,Y,E,F) = <E, X.F.Y^T> (symbolic; the 01, 23 tables act as links)",
      sp.expand(cval - t02) == 0)
check("R4 target 13: c(X,Y,E,F) = <F, X^T.E.Y> (symbolic)", sp.expand(cval - t13) == 0)
check("R5 countercontrol: the target-23 form without transposes, <Y, E.X.F^T>, differs from c (symbolic)",
      sp.expand(cval - ip(Y, E * X * F.T)) != 0)

# ------------------------------------------------------------------ W four-copy cone level
OM = {}
for a, b, c, d in itertools.product(range(4), repeat=4):
    OM[(a, b, c, d)] = sp.Symbol("o%d%d%d%d" % (a, b, c, d), real=True)
IDX4 = list(itertools.product(range(4), repeat=4))


def effA(e_, f_, om):
    return sp.expand(sum(e_[a, b] * f_[c, d] * om[(a, b, c, d)] for a, b, c, d in IDX4))


def effB(E_, F_, om):
    return sp.expand(sum(E_[a, c] * F_[b, d] * om[(a, b, c, d)] for a, b, c, d in IDX4))


def prodA(X_, Y_):
    return {(a, b, c, d): X_[a, b] * Y_[c, d] for a, b, c, d in IDX4}


def prodB(L_, Lp_):
    return {(a, b, c, d): L_[a, c] * Lp_[b, d] for a, b, c, d in IDX4}


L, Lp, e, f = symtab("l"), symtab("m"), symtab("u"), symtab("v")
ok_w1 = sp.expand(effA(e, f, prodA(X, Y)) - ip(e, X) * ip(f, Y)) == 0
ok_w2 = sp.expand(effB(E, F, prodB(L, Lp)) - ip(E, L) * ip(F, Lp)) == 0
ok_w3 = sp.expand(effB(E, F, prodA(X, Y)) - cval) == 0
ok_w4 = sp.expand(effA(e, f, prodB(L, Lp)) - contract(e, f, L, Lp)) == 0
check("W1 within a grouping, product effects on product states factor: effA(e,f)(prodA X Y) = <e,X><f,Y> and "
      "effB(E,F)(prodB L L') = <E,L><F,L'> (symbolic)", ok_w1 and ok_w2)
check("W2 across groupings the values are the contraction: effB(E,F)(prodA X Y) = c(X,Y,E,F) (family (i)) and "
      "effA(e,f)(prodB L L') = c(e,f,L,L') (family (ii)) (symbolic)", ok_w3 and ok_w4)
va, vb, vc, vd = (Matrix(4, 1, lambda m, _: sp.Symbol("%s%d" % (p, m), real=True)) for p in "abcd")
tokA = effA(va * vb.T, vc * vd.T, OM)
tokB = effB(va * vc.T, vb * vd.T, OM)
check("W3 token coherence of the W4 model: effA(a b^T, c d^T) = effB(a c^T, b d^T) on a generic 256-entry table "
      "(symbolic a, b, c, d)", sp.expand(tokA - tokB) == 0)
tokBt = effB((va * vc.T).T, vb * vd.T, OM)
check("W4 countercontrol: reading the 02 factor transposed (effB(E^T, F)) breaks token coherence (symbolic)",
      sp.expand(tokA - tokBt) != 0)

# ------------------------------------------------------------------ C cnot'
w = symtab("w")


def mat16(fun):
    M = zeros(16, 16)
    for k in range(16):
        Ek = zeros(4, 4)
        Ek[k // 4, k % 4] = 1
        img = fun(Ek)
        for j in range(16):
            M[j, k] = img[j // 4, j % 4]
    return M


CP16 = mat16(cnotp)
check("C1 cnot' is an involution (symbolic), orthogonal and symmetric as a 16 x 16 matrix, and fixes the unit entry",
      Z(cnotp(cnotp(w)) - w) and CP16.T * CP16 == eye(16) and CP16.T == CP16
      and sp.expand(cnotp(w)[0, 0] - w[0, 0]) == 0)
check("C2 cnot'(prodState xplus z3) = idW (twin Bell table) and cnot'(sharpVec xplus sharpVec z3^T) = idW/4",
      cnotp(prodState(HAND_XPLUS, HAND_Z3)) == HAND_IDW
      and cnotp(sharpVec(HAND_XPLUS) * sharpVec(HAND_Z3).T) == HAND_IDW / 4
      and no_float(sharpVec(HAND_XPLUS)))
corner = {0: HAND_Z3, 1: [-v for v in HAND_Z3]}
ok_frame = all(cnotp(prodState(corner[a], corner[b])) == prodState(corner[a], corner[(a + b) % 2])
               for a in (0, 1) for b in (0, 1))
ok_relT = Z(actT(NFLIP, cnotp(actT(NFLIP, w))) - cnotp(w))
ok_relC = Z(actC(NFLIP, cnotp(actC(NFLIP, w))) - actT(NFLIP, cnotp(w)))
check("C3 cnot' satisfies the table identities of NativeGate with nflip and z3: frame on the four corner products, "
      "relT and relC (symbolic)", ok_frame and ok_relT and ok_relC)
xs = [sp.Symbol("p%d" % j, real=True) for j in range(3)]
ys = [sp.Symbol("q%d" % j, real=True) for j in range(3)]
check("C4 cnot'(prodState x y) = actT reflY (cnot (prodState x (reflY y))) (symbolic x, y): positivity of cnot' on "
      "products reduces to cnot's (CD:1152) and the ball invariance of reflY (K2G:67)",
      Z(cnotp(prodState(xs, ys)) - actT(REFLY, cnot(prodState(xs, list(REFLY * Matrix(ys)))))))

# ------------------------------------------------------------------ B aligned parity from gate-supplied Bell data
def to_fr(M):
    return [[Fr(int(sp.numer(M[i, j])), int(sp.denom(M[i, j]))) for j in range(4)] for i in range(4)]


def fmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(4)) for j in range(4)] for i in range(4)]


def ftr(A):
    return [[A[j][i] for j in range(4)] for i in range(4)]


def fip(A, B):
    return sum(A[i][j] * B[i][j] for i in range(4) for j in range(4))


GATES = {0: cnot, 1: cnotp}
SIGNS = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
STATES = {t: [to_fr(GATES[t](prodState([s * v for v in HAND_XPLUS], [u * v for v in HAND_Z3])))
              for s, u in SIGNS] for t in (0, 1)}
EFFECTS = {t: [to_fr(GATES[t](sharpVec([s * v for v in HAND_XPLUS]) * sharpVec([u * v for v in HAND_Z3]).T))
               for s, u in SIGNS] for t in (0, 1)}
ok_par, mins = True, []
for tau in itertools.product((0, 1), repeat=4):
    t01, t23, t02, t13 = tau
    m1 = min(fip(Xs, fmul(fmul(Es, Ys), ftr(Fs))) for Xs in STATES[t01] for Ys in STATES[t23]
             for Es in EFFECTS[t02] for Fs in EFFECTS[t13])
    m2 = min(fip(es, fmul(fmul(Ls, fs), ftr(Lps))) for Ls in STATES[t02] for Lps in STATES[t13]
             for es in EFFECTS[t01] for fs in EFFECTS[t23])
    odd = (t01 + t13 + t23 + t02) % 2 == 1
    mins.append("%d%d%d%d:%s/%s" % (t01, t23, t02, t13, m1, m2))
    ok_par &= ((min(m1, m2) < 0) == odd)
check("B1 control: the gate-supplied states are four distinct tables per orientation and the effects are the states/4",
      all(len({str(S) for S in STATES[t]}) == 4 for t in (0, 1))
      and all(EFFECTS[t][k] == [[v / 4 for v in row] for row in STATES[t][k]] for t in (0, 1) for k in range(4)))
check("B2 aligned charts: over gate-supplied Bell states and effects only, a negative family value exists iff the "
      "4-cycle parity tau_01 + tau_13 + tau_23 + tau_02 is odd (16 assignments; order 01,23,02,13)  ["
      + " ".join(mins) + "]", ok_par)

# ------------------------------------------------------------------ G general charts
S0 = eye(2)
SX = Matrix([[0, 1], [1, 0]])
SY = Matrix([[0, -I], [I, 0]])
SZ = Matrix([[1, 0], [0, -1]])
SIG = [S0, SX, SY, SZ]
SS = [[sp.kronecker_product(SIG[m], SIG[n]) for n in range(4)] for m in range(4)]


def pauliW(T):
    out = zeros(4, 4)
    for m in range(4):
        for n in range(4):
            if T[m, n] != 0:
                out += T[m, n] * SS[m][n]
    return (out / 4).applyfunc(sp.expand)


def rho1(x):
    return ((S0 + x[0] * SX + x[1] * SY + x[2] * SZ) / 2).applyfunc(sp.expand)


def is_psd(M):
    M = M.applyfunc(sp.expand)
    if not Z(M - M.H):
        return False
    for k in range(1, 5):
        for rows in itertools.combinations(range(4), k):
            dval = sp.expand(M.extract(list(rows), list(rows)).det(method="berkowitz"))
            if sp.expand(sp.im(dval)) != 0 or sp.expand(sp.re(dval)) < 0:
                return False
    return True


def inQ3(T):
    return is_psd(pauliW(T))


def inTw(T):
    return is_psd(pauliW(actT(REFLY, T)))


PHIP = Matrix([[1, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 1]]) / 2
check("G0 controls: pauliW(phiW) = |Phi+><Phi+|, pauliW(prodState x y) = rho(x) (x) rho(y) (symbolic x, y); phiW is in "
      "Q3 and not in Tw; idW is in Tw and not in Q3",
      Z(pauliW(DELTA) - PHIP) and Z(pauliW(prodState(xs, ys)) - sp.kronecker_product(rho1(xs), rho1(ys)))
      and inQ3(DELTA) and not inTw(DELTA) and inTw(HAND_IDW) and not inQ3(HAND_IDW))
rng = random.Random(20261009)


def rat_rot():
    a, b, c = (R(rng.randint(-5, 5), rng.randint(1, 4)) for _ in range(3))
    S = Matrix([[0, -a, -b], [a, 0, -c], [b, c, 0]])
    return ((eye(3) - S) * (eye(3) + S).inv()).applyfunc(sp.expand)


def rat_orth(det_sign):
    Q = rat_rot()
    return Q if det_sign == 1 else (Q * REFLY).applyfunc(sp.expand)


ok_g1, g1_log = True, []
for da, db in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
    for _ in range(2):
        A, B = rat_orth(da), rat_orth(db)
        ok_orth = Z(A.T * A - eye(3)) and Z(B.T * B - eye(3)) and A.det() == da and B.det() == db
        beta = actC(A, actT(B, DELTA))
        q, t = inQ3(beta), inTw(beta)
        ok_g1 &= ok_orth and no_float(beta) and q == (da * db == 1) and t == (da * db == -1)
        g1_log.append("%+d%+d:%s%s" % (da, db, "Q" if q else "-", "T" if t else "-"))
check("G1 the Bell state of a gate with post-locals (A, B) is in Q3 iff det A det B = 1 and in Tw iff det A det B = -1 "
      "(exact rational O(3), both determinants, two draws each)  [" + " ".join(g1_log) + "]", ok_g1)
PAIRS = ["01", "23", "02", "13"]
ok_g2, ok_g3_disagree, g2_log = True, False, []
for tau in itertools.product((0, 1), repeat=4):
    tdict = dict(zip(PAIRS, tau))
    even = (tdict["01"] + tdict["13"] + tdict["23"] + tdict["02"]) % 2 == 0
    for draw in range(2):
        post, Rm = {}, {}
        for p in PAIRS:
            sa = rng.choice((1, -1))
            sb = sa * (1 if tdict[p] == 0 else -1)
            A, B = rat_orth(sa), rat_orth(sb)
            post[p] = (A, B)
            Rm[p] = (A * REFLY * B.T).applyfunc(sp.expand)
        rep = actC(post["23"][0], actT(post["23"][1], DELTA))
        img = (H(Rm["02"]) * rep * H(Rm["13"]).T).applyfunc(sp.expand)
        inC01 = inQ3(img) if tdict["01"] == 0 else inTw(img)
        inOther = inTw(img) if tdict["01"] == 0 else inQ3(img)
        consistent = inC01 and not inOther
        ok_g2 &= (consistent == even) and no_float(img)
        # countercontrol: pre-locals whose determinant product is opposite to the post-locals' on pair 02
        A2, B2 = rat_orth(1), rat_orth(-post["02"][0].det() * post["02"][1].det())
        A2b, B2b = rat_orth(1), rat_orth(post["13"][0].det() * post["13"][1].det())
        Rp02 = (A2.T * REFLY * B2).applyfunc(sp.expand)
        Rp13 = (A2b.T * REFLY * B2b).applyfunc(sp.expand)
        img_p = (H(Rp02) * rep * H(Rp13).T).applyfunc(sp.expand)
        cons_p = (inQ3(img_p) if tdict["01"] == 0 else inTw(img_p)) and not \
            (inTw(img_p) if tdict["01"] == 0 else inQ3(img_p))
        ok_g3_disagree |= (cons_p != even)
    g2_log.append("%d%d%d%d:%s" % (tdict["01"], tdict["23"], tdict["02"], tdict["13"], "even" if even else "odd"))
check("G2 general charts: Theta = actC R02 . actT R13 (R = A reflY B^T, post-locals) maps the Bell state of pair 23 "
      "into C01 and not into the other cone iff the 4-cycle parity of tau_p = [det A_p det B_p = -1] is even "
      "(16 assignments x 2 draws)  [" + " ".join(g2_log) + "]", ok_g2)
check("G3 countercontrol: with R' from pre-locals (N's own dual) whose determinant product is opposite on pair 02, "
      "the same test disagrees with the parity rule", ok_g3_disagree)

npass = sum(1 for _, c in CHECKS if c)
print("--- f1_package_identities: %d/%d checks pass" % (npass, len(CHECKS)))
print("VERDICT F1-PACKAGE-IDENTITIES-EXACT" if npass == len(CHECKS) else "VERDICT NOT RENDERED")
