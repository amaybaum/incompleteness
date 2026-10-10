"""EQ5-PREM q3 — Part B.  Exact tests of the candidate formulations of "physical reversibility" and "operational
availability" of a pair's native gate against the landed countermodels (the bodies of ball3MaxComposite and
ball3MinComposite with cnot, re-derived here) and a new one, the twin cone with cnot (a chart mismatch); plus the
four-token check that KT(4) consistency does not supply hgate.  Research only; nothing here is adopted.

Usage:  python3 -I -B q3_gate.py <base>/verification/lean-mathlib/OIBridge

Conventions: W 3 tables are 4 x 4 (index 0 = unit; row = control = first token); actT N w [m][n] = hN[n] w[m][n],
actC N w [m][n] = hN[m] w[m][n] for diagonal sign maps; cnot w [m][n] = sgn(m,n) w[pc(m,n)][pt(m,n)] (CD:741-755);
pairVal a b w = sum a_m w_mn b_n; ipW E X = sum E_mn X_mn; tens a b = a b^T; sharpVec b = (1, b)/2; Pauli dictionary
pauliW T = 1/4 sum T_mn s_m (x) s_n, Q3 = {pauliW T PSD}, twin = actT reflY '' Q3 (package :307-318).
Pair bodies of the three models (normalized slices of the cones): MAX = maxCone (eball 3) (the body of
ball3MaxComposite read in W 3, SOURCE s2 D1-D3), MIN = the convex hull of the product states (ball3MinComposite), TWIN.

Candidate formulations (B1), each a predicate on (K, N) with N = cnot:
 K1    DIM-1's IsNot (nflip), NativeGate (eball 3) z3 nflip cnot and Entangling (landed; independent of K).
 NGOF  K1-BRIDGE-1's NativeGateOf with avail = every effect of the ball (EffectSpace:415 gives maxConeOf = maxCone).
 PAIR  the other stated pair premises: N-CLASS (cnot with identity locals), CandidateCone, IsConvexCone, IsClosed.
 SD    self-duality of the pair cone, dualW K = K.
 IIP   N is an isometry, fixing the centroid, of the IIP-1 invariant inner product of the pair body.
 PRP   product-level reversibility relative to K: N and N^-1 map every product state into K.
 JR    COMP-1 JointReversible {N} / OrbitGeneration PreservesBody of the pair body (hgate /\ hinv on the slice).
 OAE   effect-side availability: the ipW-adjoint of N (= N, cnot being an ipW-self-adjoint involution) maps dualW K
       into dualW K.
 OPACT K-infinity-Act transported: N is OPACT-1 operation data with AffineRespect and an inverse datum on a stage system
       whose completion body is the pair body (then PreservesBody by preservesBody_inducedEquiv, CA:352).

DECISION RULE (fixed before the first run; rules, not expected numbers):
 K  transcription: the parsed sgn, pc, pt (CD:741-755), nflip (CD:797-798), reflY (K2G:46-47), z3, xplus, phiW
    (CD:793, :1213, :1220), idW, chainW (K2G:101-104) equal the hand transcriptions; the landed statements
    cnot_prodState_xplus_z3 (CD:1222), actT_reflY_phiW (K2G:106), cnot_idW (K2G:110), chain_value (K2G:134),
    nativeGate_cnot (CD:1160), entangling_cnot (CD:1380), maxConeOf_fullEffects (EffectSpace:415) are present, and the
    first four reproduce exactly.
 G  the countermodels (exact):
    G-MAX  idW is in maxCone: pairVal against the generators of the effect cone (hom 0 and sharpVec b, lor_decomp
           ES:449) gives 1, 1/2, 1/2 and (1 + b.c)/4 (symbolic), nonnegative for unit b, c; cnot idW = chainW has the value
           -1/2 at the sharp pair of K2G:134.  So hgate fails; hinv fails (cnot is an involution, exact on the 16 basis
           tables).
    G-MIN  F(w) = w00 - w11 + w22 - w33 satisfies F(prodState x y) = 1/2|x - Dy|^2 + 1/2(1 - |x|^2) + 1/2(1 - |y|^2),
           D = diag(1, -1, 1) (symbolic), so F >= 0 on MIN; F(phiW) < 0 with phiW = cnot(prodState xplus z3).
    G-TWIN (t1) actT reflY (prodState x y) = prodState x (reflY y) and actT reflY is an involution (symbolic);
           (t2) pauliW (prodState x y) = r(x) (x) r(y), r(x) = (1 + x.s)/2 (symbolic): products are PSD, so the
           products lie in Q3 and, by t1, in TWIN; (t3) pairVal a b w = tr((A (x) B) pauliW w) with A = sum a_m s_m
           (symbolic w, a, b), and pairVal a b (actT reflY w) = pairVal a (homMap reflY b) w (symbolic): Q3 and TWIN lie
           in maxCone; (t4) v^dag pauliW(idW) v < 0 for v = (0, 1, -1, 0) with actT reflY phiW = idW: phiW is not in
           TWIN while prodState xplus z3 is, so hgate fails, and hinv fails; (t5) N-CLASS with identity locals, and the
           NativeGate frame, relT, relC of cnot reproduce exactly; (t6) actT reflY is ipW-self-adjoint (symbolic), the
           ingredient of dualW TWIN = actT reflY (dualW Q3); (t7) cnot is a signed permutation of the 16 table
           coordinates, orthogonal (M^T M = I) and fixing e00.
 T  the candidate table: for each model in {MAX, MIN, TWIN} and each candidate, HOLDS / FAILS (with an exact witness or
    the landed identifier) or N/A (not evaluated, with the reason).  REFUTATION: "P => hgate" is REFUTED by a model iff P
    HOLDS and hgate FAILS there.  Consistency control: no relabelling formulation (JR, OAE, OPACT) may HOLD in a model
    where hgate FAILS.
 F  four-token level: the product identities that make uniform SEP and uniform maxCone satisfy FourCopyCoherent hold
    (symbolic): fourVal (prodState x0 x1) (prodState x2 x3) E F = ipW E (prodState x0 x2) * ipW F (prodState x1 x3) and
    fourVal X Y (tens a a') (tens b b') = pairVal a b X * pairVal a' b' Y (and the famII forms).
 VERDICT Q3-PART-B-GATE-EXACT iff every K, G, T-consistency and F check passes; otherwise VERDICT NOT RENDERED.  Exact
 arithmetic only.  No timing in stdout.
"""
import itertools
import os
import re
import sys
from fractions import Fraction as Fr

import sympy as sp

LEAN = sys.argv[1]
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


def read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


R4 = range(4)
CD = read(os.path.join(LEAN, "CompositeDimension.lean"))
K2G = read(os.path.join(LEAN, "K2Guard.lean"))
ES = read(os.path.join(LEAN, "EffectSpace.lean"))
CDL = CD.split("\n")


def zero(e):
    return sp.expand(e) == 0


# ------------------------------------------------------------------ K transcription
def pmap(name):
    blk = re.search(r"def " + name + r" : Fin 4 → Fin 4 → Fin 4\n((?:\s*\|[^\n]*\n)+)", CD).group(1)
    return {(int(a), int(b)): int(c) for a, b, c in re.findall(r"(\d), (\d) => (\d)", blk)}


PC, PT = pmap("pc"), pmap("pt")
msg = re.search(r"def sgn \(μ ν : Fin 4\) : ℝ := if \(μ = (\d) ∧ ν = (\d)\) ∨ \(μ = (\d) ∧ ν = (\d)\) then -1 else 1", CD)
NEG = {(int(msg.group(1)), int(msg.group(2))), (int(msg.group(3)), int(msg.group(4)))}
PC_H = {(0, 0): 0, (0, 1): 0, (0, 2): 3, (0, 3): 3, (1, 0): 1, (1, 1): 1, (1, 2): 2, (1, 3): 2,
        (2, 0): 2, (2, 1): 2, (2, 2): 1, (2, 3): 1, (3, 0): 3, (3, 1): 3, (3, 2): 0, (3, 3): 0}
PT_H = {(0, 0): 0, (0, 1): 1, (0, 2): 2, (0, 3): 3, (1, 0): 1, (1, 1): 0, (1, 2): 3, (1, 3): 2,
        (2, 0): 1, (2, 1): 0, (2, 2): 3, (2, 3): 2, (3, 0): 0, (3, 1): 1, (3, 2): 2, (3, 3): 3}
nflip_t = re.search(r"def nflip[^\n]*\n\s*toFun x := fun i => \(!\[([^\]]*)\]", CD).group(1).replace(" ", "")
reflY_t = re.search(r"def reflY[^\n]*\n\s*toFun x := fun i => \(!\[([^\]]*)\]", K2G).group(1).replace(" ", "")


def parse_mat(name, text):
    lit = re.search(r"def " + name + r" : W 3 := (!\[!\[[^\n]*\]\])", text).group(1)
    return [[sp.Integer(int(v)) for v in r.split(",")] for r in re.findall(r"!\[([-\d, ]+)\]", lit)]


IDW, CHAINW = parse_mat("idW", K2G), parse_mat("chainW", K2G)
lit_ok = ("def z3 : Fin 3 → ℝ := ![0, 0, 1]" in CD and "def xplus : Fin 3 → ℝ := ![1, 0, 0]" in CD
          and "def phiW : W 3 := fun μ ν => if μ = ν then (if μ = 2 then -1 else 1) else 0" in CD)
present = ("theorem cnot_prodState_xplus_z3 : cnot (prodState xplus z3) = phiW" in CD
           and "theorem actT_reflY_phiW : actT reflY phiW = idW" in K2G and "theorem cnot_idW : cnot idW = chainW" in K2G
           and CDL[1159].startswith("theorem nativeGate_cnot : NativeGate (eball 3) z3 nflip cnot where")
           and CDL[1379].startswith("theorem entangling_cnot : Entangling (eball 3) cnot :=")
           and ES.split("\n")[414].startswith("theorem maxConeOf_fullEffects (Ω : Set (Fin d → ℝ)) : maxConeOf (fullEffects Ω) = maxCone Ω")
           and re.search(r"theorem chain_value :\s*prodEffVal \(sharpEff !\[-1, 0, 0\]\) \(sharpEff !\[0, 0, -1\]\) "
                         r"chainW = -1 / 2", K2G) is not None)
HS_RY = [1, 1, -1, 1]
HS_NF = [1, 1, -1, -1]
PHIW = [[sp.Integer([1, 1, -1, 1][i]) if i == j else sp.Integer(0) for j in R4] for i in R4]
XPLUS, Z3 = [1, 0, 0], [0, 0, 1]


def hom(x):
    return [sp.Integer(1)] + [sp.sympify(v) for v in x]


def prodState(x, y):
    hx, hy = hom(x), hom(y)
    return [[hx[m] * hy[n] for n in R4] for m in R4]


def cnot(w):
    return [[(-1 if (m, n) in NEG else 1) * w[PC[(m, n)]][PT[(m, n)]] for n in R4] for m in R4]


def actT(hs, w):
    return [[hs[n] * w[m][n] for n in R4] for m in R4]


def actC(hs, w):
    return [[hs[m] * w[m][n] for n in R4] for m in R4]


def pairVal(a, b, w):
    return sp.expand(sum(a[m] * w[m][n] * b[n] for m in R4 for n in R4))


def ipW(E, X):
    return sp.expand(sum(E[m][n] * X[m][n] for m in R4 for n in R4))


def tens(a, b):
    return [[a[m] * b[n] for n in R4] for m in R4]


def sharpVec(b):
    return [sp.Rational(1, 2)] + [sp.Rational(1, 2) * sp.sympify(v) for v in b]


def teq(A, B):
    return all(zero(A[m][n] - B[m][n]) for m in R4 for n in R4)


repro = (teq(cnot(prodState(XPLUS, Z3)), PHIW) and teq(actT(HS_RY, PHIW), IDW) and teq(cnot(IDW), CHAINW)
         and pairVal(sharpVec([-1, 0, 0]), sharpVec([0, 0, -1]), CHAINW) == sp.Rational(-1, 2))
check("K transcription and landed statements: sgn, pc, pt, nflip, reflY, z3, xplus, phiW, idW, chainW; "
      "cnot_prodState_xplus_z3, actT_reflY_phiW, cnot_idW, chain_value (reproduced), nativeGate_cnot, entangling_cnot, "
      "maxConeOf_fullEffects (present)",
      PC == PC_H and PT == PT_H and NEG == {(1, 3), (2, 2)} and nflip_t == "1,-1,-1" and reflY_t == "1,-1,1"
      and lit_ok and present and repro
      and IDW == [[1 if i == j else 0 for j in R4] for i in R4]
      and CHAINW == [[1, 0, 0, 1], [1, 0, 0, -1], [0, 0, 0, 0], [0, 0, 0, 0]])

Wsym = [[sp.Symbol("w%d%d" % (m, n)) for n in R4] for m in R4]
BASIS = [[[sp.Integer(1) if (i, j) == (m, n) else sp.Integer(0) for j in R4] for i in R4] for m in R4 for n in R4]
invol = all(teq(cnot(cnot(B)), B) for B in BASIS)

# ------------------------------------------------------------------ G-MAX
bs, cs = sp.symbols("b1:4"), sp.symbols("c1:4")
u0 = [1, 0, 0, 0]
gmax = (pairVal(u0, u0, IDW) == 1 and zero(pairVal(u0, sharpVec(cs), IDW) - sp.Rational(1, 2))
        and zero(pairVal(sharpVec(bs), u0, IDW) - sp.Rational(1, 2))
        and zero(pairVal(sharpVec(bs), sharpVec(cs), IDW) - (1 + sum(b * c for b, c in zip(bs, cs))) / 4))
chain_val = pairVal(sharpVec([-1, 0, 0]), sharpVec([0, 0, -1]), cnot(IDW))
check("G-MAX idW in maxCone (pairings 1, 1/2, 1/2, (1 + b.c)/4 on the generators of the effect cone, symbolic); "
      "cnot idW = chainW is -1/2 at a sharp pair: hgate fails on MAX; cnot is an involution (16 basis tables): hinv "
      "fails", gmax and chain_val < 0 and invol, "value = %s" % chain_val)

# ------------------------------------------------------------------ G-MIN
xs, ys = sp.symbols("x1:4"), sp.symbols("y1:4")
Dy = [ys[0], -ys[1], ys[2]]


def Ffun(w):
    return w[0][0] - w[1][1] + w[2][2] - w[3][3]


sos = (sum((xs[i] - Dy[i]) ** 2 for i in range(3)) / 2 + (1 - sum(v ** 2 for v in xs)) / 2
       + (1 - sum(v ** 2 for v in ys)) / 2)
gmin = zero(Ffun(prodState(xs, ys)) - sos) and Ffun(PHIW) < 0
check("G-MIN F(prodState x y) = 1/2|x - Dy|^2 + 1/2(1 - |x|^2) + 1/2(1 - |y|^2) (symbolic), so F >= 0 on MIN; "
      "F(phiW) < 0 with phiW = cnot(prodState xplus z3): hgate fails on MIN", gmin, "F(phiW) = %s" % Ffun(PHIW))

# ------------------------------------------------------------------ G-TWIN
I_ = sp.I
SIG = [sp.Matrix([[1, 0], [0, 1]]), sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -I_], [I_, 0]]),
       sp.Matrix([[1, 0], [0, -1]])]


def kron(A, B):
    (ra, ca), (rb, cb) = A.shape, B.shape
    return sp.Matrix(ra * rb, ca * cb, lambda i, j: A[i // rb, j // cb] * B[i % rb, j % cb])


def pauliW(T):
    acc = sp.zeros(4, 4)
    for m in R4:
        for n in R4:
            if T[m][n] != 0:
                acc += sp.Rational(1, 4) * T[m][n] * kron(SIG[m], SIG[n])
    return acc


def r_of(x):
    return (SIG[0] + x[0] * SIG[1] + x[1] * SIG[2] + x[2] * SIG[3]) / 2


t1 = teq(actT(HS_RY, prodState(xs, ys)), prodState(xs, [ys[0], -ys[1], ys[2]])) and teq(actT(HS_RY, actT(HS_RY, Wsym)), Wsym)
t2 = (pauliW(prodState(xs, ys)) - kron(r_of(xs), r_of(ys))).applyfunc(sp.expand) == sp.zeros(4, 4)
As, Bs = sp.symbols("a0:4"), sp.symbols("e0:4")
Amat = sum((As[m] * SIG[m] for m in R4), sp.zeros(2, 2))
Bmat = sum((Bs[m] * SIG[m] for m in R4), sp.zeros(2, 2))
t3a = zero((kron(Amat, Bmat) * pauliW(Wsym)).trace() - pairVal(As, Bs, Wsym))
t3b = zero(pairVal(As, Bs, actT(HS_RY, Wsym)) - pairVal(As, [Bs[0], Bs[1], -Bs[2], Bs[3]], Wsym))
vv = sp.Matrix([0, 1, -1, 0])
neg_idw = sp.simplify((vv.H * pauliW(IDW) * vv)[0])
t4 = teq(actT(HS_RY, PHIW), IDW) and neg_idw < 0 and teq(cnot(prodState(XPLUS, Z3)), PHIW)
# t5: N-CLASS with identity locals; NativeGate frame, relT, relC of cnot
HID = [1, 1, 1, 1]
nclass = teq(actC(HID, actT(HID, cnot(actC(HID, actT(HID, Wsym))))), cnot(Wsym))


def corner(a):
    return [0, 0, 1] if a == 0 else [0, 0, -1]


frame = all(teq(cnot(prodState(corner(a), corner(b))), prodState(corner(a), corner((a + b) % 2)))
            for a in (0, 1) for b in (0, 1))
relT = teq(actT(HS_NF, cnot(actT(HS_NF, Wsym))), cnot(Wsym))
relC = teq(actC(HS_NF, cnot(actC(HS_NF, Wsym))), actT(HS_NF, cnot(Wsym)))
t5 = nclass and frame and relT and relC
Esym = [[sp.Symbol("E%d%d" % (m, n)) for n in R4] for m in R4]
t6 = zero(ipW(actT(HS_RY, Esym), Wsym) - ipW(Esym, actT(HS_RY, Wsym)))
M = sp.zeros(16, 16)
for m in R4:
    for n in R4:
        M[4 * m + n, 4 * PC[(m, n)] + PT[(m, n)]] = -1 if (m, n) in NEG else 1
e00 = sp.Matrix([1] + [0] * 15)
t7 = (M.T * M == sp.eye(16)) and (M * e00 == e00) and all(sum(abs(M[i, j]) for j in range(16)) == 1 for i in range(16))
check("G-TWIN (t1) actT reflY maps prodState x y to prodState x (reflY y), involution; (t2) pauliW(prodState x y) = "
      "r(x) (x) r(y); (t3) pairVal a b w = tr((A (x) B) pauliW w) and the reflY pullback; (t4) v^dag pauliW(idW) v < 0, "
      "actT reflY phiW = idW, phiW = cnot(prodState xplus z3): hgate fails on TWIN; (t5) N-CLASS (identity locals), "
      "frame, relT, relC; (t6) actT reflY ipW-self-adjoint; (t7) cnot orthogonal signed permutation fixing e00",
      t1 and t2 and t3a and t3b and t4 and t5 and t6 and t7,
      "t1 %s t2 %s t3 %s/%s t4 %s (value %s) t5 %s t6 %s t7 %s" % (t1, t2, t3a, t3b, t4, neg_idw, t5, t6, t7))

# ------------------------------------------------------------------ the witnesses used in the candidate table
SINGLET = [[sp.Integer([1, -1, -1, -1][i]) if i == j else sp.Integer(0) for j in R4] for i in R4]
DPRIME = [[sp.Integer([1, -1, 1, -1][i]) if i == j else sp.Integer(0) for j in R4] for i in R4]
hb, hc = hom(bs), hom(cs)
sing_in_max = zero(pairVal(hb, hc, SINGLET) - (1 - sum(b * c for b, c in zip(bs, cs))))
dp_in_max = zero(pairVal(hb, hc, DPRIME) - (1 - bs[0] * cs[0] + bs[1] * cs[1] - bs[2] * cs[2]))
sd_max_w = ipW(IDW, SINGLET)                 # idW in MAX, SINGLET in MAX, pairing negative: idW not in dualW MAX
bell_eff = cnot(tens(sharpVec(XPLUS), sharpVec(Z3)))
oae_max_w = ipW(bell_eff, DPRIME)            # tens(sharp, sharp) in dualW MAX; its cnot image is negative on DPRIME
check("W witnesses: SINGLET and D' = dg(1,-1,1,-1) pair with hom b (x) hom c as 1 - b.c and 1 - b1c1 + b2c2 - b3c3 "
      "(symbolic; nonnegative for |b|,|c| <= 1, so both lie in maxCone); ipW(idW, SINGLET) < 0; cnot(tens(sharpVec "
      "xplus)(sharpVec z3)) = phiW/4 and ipW(phiW/4, D') < 0",
      sing_in_max and dp_in_max and sd_max_w < 0 and teq(bell_eff, [[v / 4 for v in row] for row in PHIW])
      and oae_max_w < 0, "ipW(idW, SINGLET) = %s, ipW(cnot tens, D') = %s" % (sd_max_w, oae_max_w))

# ------------------------------------------------------------------ T the candidate table
H = "FAILS"
TABLE = {
    "MAX": {"hgate": ("FAILS", "cnot idW = chainW, -1/2 at a sharp pair (G-MAX)"),
            "K1": ("HOLDS", "nativeGate_cnot CD:1160, entangling_cnot CD:1380, isNot_nflip CD:838 (independent of K)"),
            "NGOF": ("HOLDS", "avail = all effects: maxConeOf = maxCone (EffectSpace:415); then NativeGateOf = NativeGate"),
            "PAIR": ("HOLDS", "SOURCE s2 D1-D3 + G-MAX: maxCone is a closed CandidateCone convex cone; N-CLASS (t5)"),
            "SD": ("FAILS", "idW in MAX and SINGLET in MAX with ipW(idW, SINGLET) < 0 (W)"),
            "IIP": ("N/A", "the second moments of MAX are not computed here"),
            "PRP": ("HOLDS", "posFwd/posInv of nativeGate_cnot: cnot(prodState x y) in maxCone (CD:1152)"),
            "JR": ("FAILS", "PreservesBody {cnot} would contain hgate (G-MAX)"),
            "OAE": ("FAILS", "tens(sharpVec xplus)(sharpVec z3) in dualW MAX, its cnot image phiW/4 is negative on D' in MAX"),
            "OPACT": ("FAILS", "preservesBody_inducedEquiv (CA:352) would give PreservesBody, contradicting G-MAX")},
    "MIN": {"hgate": ("FAILS", "F(phiW) = -2 with phiW = cnot(prodState xplus z3) (G-MIN)"),
            "K1": ("HOLDS", "as MAX (independent of K)"),
            "NGOF": ("HOLDS", "as MAX"),
            "PAIR": ("HOLDS", "SOURCE s2: the minimal body is a closed CandidateCone convex cone; N-CLASS (t5)"),
            "SD": ("FAILS", "dualW MIN = maxCone contains idW, which is not in MIN (idW is not in Q3 (t4) and MIN is in Q3 (t2))"),
            "IIP": ("N/A", "the second moments of MIN are not computed here"),
            "PRP": ("FAILS", "cnot(prodState xplus z3) = phiW is not in MIN (G-MIN)"),
            "JR": ("FAILS", "would contain hgate (G-MIN)"),
            "OAE": ("FAILS", "dualW MIN = maxCone contains idW; cnot idW = chainW is not in maxCone (G-MAX)"),
            "OPACT": ("FAILS", "would give PreservesBody (CA:352), contradicting G-MIN")},
    "TWIN": {"hgate": ("FAILS", "prodState xplus z3 in TWIN (t1, t2), cnot image phiW not in TWIN (t4)"),
             "K1": ("HOLDS", "as MAX (independent of K)"),
             "NGOF": ("HOLDS", "as MAX"),
             "PAIR": ("HOLDS", "CandidateCone: products in TWIN (t1, t2), TWIN in maxCone (t3); convex cone and closed "
                               "(linear image of Q3, W); N-CLASS with identity locals (t5)"),
             "SD": ("HOLDS", "dualW TWIN = actT reflY (dualW Q3) = TWIN: t6 + Q3 self-dual (package O28, W)"),
             "IIP": ("HOLDS", "cnot orthogonal, fixing e00 (t7); the IIP-1 form of TWIN is a multiple of the Euclidean "
                              "one (W: Ad SU(4) irreducible on traceless Hermitian, PT_2 diagonal +-1)"),
             "PRP": ("FAILS", "cnot(prodState xplus z3) = phiW is not in TWIN (t4)"),
             "JR": ("FAILS", "would contain hgate (t4)"),
             "OAE": ("FAILS", "dualW TWIN = TWIN contains prodState xplus z3; its cnot image phiW is not in TWIN (t4)"),
             "OPACT": ("FAILS", "would give PreservesBody (CA:352), contradicting t4")},
}
CANDS = ["K1", "NGOF", "PAIR", "SD", "IIP", "PRP", "JR", "OAE", "OPACT"]
for mdl in ["MAX", "MIN", "TWIN"]:
    for c in ["hgate"] + CANDS:
        v, why = TABLE[mdl][c]
        print("RESULT %-4s %-5s %-5s  (%s)" % (mdl, c, v, why))
consistency = all(not (TABLE[m]["hgate"][0] == "FAILS" and TABLE[m][c][0] == "HOLDS")
                  for m in TABLE for c in ("JR", "OAE", "OPACT"))
basis_ok = (gmax and chain_val < 0 and gmin and t1 and t2 and t3a and t3b and t4 and t5 and t6 and t7 and sing_in_max
            and dp_in_max and sd_max_w < 0 and oae_max_w < 0)
check("T consistency: no relabelling formulation (JR, OAE, OPACT) HOLDS where hgate FAILS, and every exact entry of the "
      "table rests on a passing check above", consistency and basis_ok)

# ------------------------------------------------------------------ F four-token level
x = [sp.symbols("p%d_1:4" % t) for t in R4]
X0 = prodState(x[0], x[1])
Y0 = prodState(x[2], x[3])
Fsym = [[sp.Symbol("F%d%d" % (m, n)) for n in R4] for m in R4]


def fourVal(X, Y, E, F):
    return sp.expand(sum(X[a][b] * Y[c][d] * E[a][c] * F[b][d]
                         for a, b, c, d in itertools.product(R4, R4, R4, R4)))


f_sep_I = zero(fourVal(X0, Y0, Esym, Fsym) - ipW(Esym, prodState(x[0], x[2])) * ipW(Fsym, prodState(x[1], x[3])))
L0, L1 = prodState(x[0], x[2]), prodState(x[1], x[3])
f_sep_II = zero(fourVal(Esym, Fsym, L0, L1) - ipW(Esym, prodState(x[0], x[1])) * ipW(Fsym, prodState(x[2], x[3])))
a1, a2 = sp.symbols("q0:4"), sp.symbols("r0:4")
b1, b2 = sp.symbols("s0:4"), sp.symbols("t0:4")
Ysym = [[sp.Symbol("Y%d%d" % (m, n)) for n in R4] for m in R4]
f_max_I = zero(fourVal(Wsym, Ysym, tens(a1, a2), tens(b1, b2)) - pairVal(a1, b1, Wsym) * pairVal(a2, b2, Ysym))
f_max_II = zero(fourVal(tens(a1, b1), tens(a2, b2), Wsym, Ysym) - pairVal(a1, a2, Wsym) * pairVal(b1, b2, Ysym))
check("F four-token level: FourCopyCoherent's two families factorize on the generators for uniform SEP (product states "
      "against arbitrary effect tables) and for uniform maxCone (arbitrary states against product effect tables), "
      "symbolic", f_sep_I and f_sep_II and f_max_I and f_max_II)

nfail = sum(1 for _, ok in CHECKS if not ok)
if nfail == 0:
    for c in CANDS:
        ref = [m for m in TABLE if TABLE[m][c][0] == "HOLDS" and TABLE[m]["hgate"][0] == "FAILS"]
        print("REFUTATION %-5s => hgate : %s" % (c, ("REFUTED by " + ", ".join(ref)) if ref else "SURVIVES"))
print("--- q3_gate: %d/%d checks pass" % (len(CHECKS) - nfail, len(CHECKS)))
print("VERDICT Q3-PART-B-GATE-EXACT" if nfail == 0 else "VERDICT NOT RENDERED")
