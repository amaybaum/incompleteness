"""EQ4-SOURCE s2 — exact cores of the pair-level classifications (Q4).  Research only; nothing here is adopted.

  * hgate / hinv are not implied by the base's two-copy premises: the landed maximal and minimal bodies of two balls
    (ball3MaxComposite, ball3MinComposite, CI:807-812) with the landed native gate cnot (CD:1160) satisfy those premises
    and are not cnot-invariant.
  * hcl is not implied: the closure foil K_cl = int Q3 ∪ conv(SEP ∪ cnot SEP) (EQ3 p2 F4) has a boundary point of Q3 in
    its closure and not in it.
  * hadm is COMP-1's body bounds read in W 3 coordinates: definitional match of the COMP-1 model coordinates with
    DIM-1's.
  * hcls (N-CLASS) is not landed; the landed ingredients that EQ2-B's written route cites are present.

Usage:  python3 -I -B s2_pair_premises.py <base>/verification/lean-mathlib/OIBridge <mathlib4 root>

DECISION RULE (fixed before the first run; rules, not expected numbers):
 K  transcription controls: the parsed sgn, pc, pt (CD:741-755), phiW (CD:1220), idW, chainW (K2G:101-104) equal the
    hand transcriptions; cnot(prodState xplus z3) = phiW, actT reflY phiW = idW, cnot idW = chainW reproduce.
 D  definitional match (text of the base and of Mathlib v4.33.0):
    D1 COMP-1 Model.hom is `Fin.cons 1 x` (CI:582), DIM-1 hom is `Matrix.vecCons 1 x` (CD:100), and Mathlib's
       Matrix.vecCons is `Fin.cons h t` (Mathlib/Data/Fin/VecNotation.lean:59): Model.pState = prodState;
    D2 COMP-1 coeff (CI:602-603) and DIM-1 ehom (CD:167-168) are `cons (e 0)` of `e.linear` at the indicator of
       `i = j`, resp. `j = i`: Model.pEff e f = prodEffVal e f up to commuting the sums;
    D3 the statements used are present with the stated shapes: eball_three (TB:671), PreComposite.convex, prod_mem
       (CI:226-227), subset_maxBody (CI:467), maxBody (CI:271-274), CandidateCone (K2G:95-96), maxCone (CD:186-187),
       jointStates (CD:190-191), ball3MaxComposite and ball3MinComposite (CI:807-812).
 G  gate preservation is not implied:
    G1 the Lorentz pairings of idW: pairVal(u0, u0, idW) = 1, pairVal(u0, sharpVec c, idW) = pairVal(sharpVec b, u0,
       idW) = 1/2 and pairVal(sharpVec b, sharpVec c, idW) = (1 + b.c)/4 (symbolic b, c), all nonnegative on unit
       vectors (Cauchy-Schwarz, written; the reduction of every effect to these is EFF-1's lor_decomp, ES:449); and
       chainW = cnot idW has the negative value of K2G:134 on a pair of sharp effects (exact).  So maxCone(eball 3) is
       not cnot-invariant, and, cnot being an involution (CD:790), not cnot^-1-invariant;
    G2 the table functional F(w) = w00 - w11 + w22 - w33 satisfies F(prodState x y) = 1/2 |x - D y|^2 +
       1/2 (1 - |x|^2) + 1/2 (1 - |y|^2) with D = diag(1, -1, 1) (symbolic sum-of-squares identity), hence F >= 0 on
       every product of ball states and on their convex hull, while F(phiW) < 0 (exact): phiW = cnot(prodState xplus
       z3) is not in the minimal body;
    controls: F(idW) and F(chainW) are computed and reported; F on prodState xplus z3 is nonnegative; the sharp pair of
       K2G:134 is nonnegative on cnot of the four corner products (spot values of the landed cnot_prodState_mem_maxCone).
 C  closedness is not implied (closure foil):
    C1 for psi = (|00> + |01> + |10> - |11>)/2, the Pauli-expectation table T_psi is real and pauliW(T_psi) = |psi><psi|
       (exact): T_psi is a rank-one element of Q3;
    C2 the coefficient matrix C of psi has det C != 0 (not a product) and C00 C10 - C01 C11 != 0, while for
       CNOT(a (x) b) the same expression vanishes identically (symbolic a, b): psi is not a CNOT image of a product;
    C3 control: CNOT(|+> (x) |0>) has invariant 0 and its table equals cnot(prodState xplus z3) = phiW.
 N  N-CLASS sourcing: the landed lemmas cited by EQ2-B's route are present at the cited lines (RSB:60, 87, 99, 129,
    162; RelcSelectParity:329; CD:1805, 1870, 2051; CtrlGate RSB:45; ctrlGate_of_nativeGate RSB:53), and no
    classification theorem (`ctrlGate_classification`, `NClass`) is present in any base module.
VERDICT S2-PAIR-PREMISE-CORES-EXACT iff every check passes; otherwise VERDICT NOT RENDERED.  Exact arithmetic only.
"""
import os
import re
import sys
from fractions import Fraction as Fr

import sympy as sp

BASE = sys.argv[1]
MLROOT = sys.argv[2]
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


def lines_of(path):
    return read(path).split("\n")


R4 = range(4)
CD = read(BASE + "/CompositeDimension.lean")
K2G = read(BASE + "/K2Guard.lean")
CI = read(BASE + "/CompositeInterface.lean")
TB = read(BASE + "/TransitiveBody.lean")
CDL = CD.split("\n")
CIL = CI.split("\n")
K2L = K2G.split("\n")
TBL = TB.split("\n")

# ---------------------------------------------------------------- K
PC = {(int(a), int(b)): int(c) for a, b, c in
      re.findall(r"(\d), (\d) => (\d)", re.search(r"def pc : Fin 4 → Fin 4 → Fin 4\n((?:\s*\|[^\n]*\n)+)", CD).group(1))}
PT = {(int(a), int(b)): int(c) for a, b, c in
      re.findall(r"(\d), (\d) => (\d)", re.search(r"def pt : Fin 4 → Fin 4 → Fin 4\n((?:\s*\|[^\n]*\n)+)", CD).group(1))}
m_sgn = re.search(r"def sgn \(μ ν : Fin 4\) : ℝ := if \(μ = (\d) ∧ ν = (\d)\) ∨ \(μ = (\d) ∧ ν = (\d)\) then -1 "
                  r"else 1", CD)
NEG = {(int(m_sgn.group(1)), int(m_sgn.group(2))), (int(m_sgn.group(3)), int(m_sgn.group(4)))}
PC_H = {(0, 0): 0, (0, 1): 0, (0, 2): 3, (0, 3): 3, (1, 0): 1, (1, 1): 1, (1, 2): 2, (1, 3): 2,
        (2, 0): 2, (2, 1): 2, (2, 2): 1, (2, 3): 1, (3, 0): 3, (3, 1): 3, (3, 2): 0, (3, 3): 0}
PT_H = {(0, 0): 0, (0, 1): 1, (0, 2): 2, (0, 3): 3, (1, 0): 1, (1, 1): 0, (1, 2): 3, (1, 3): 2,
        (2, 0): 1, (2, 1): 0, (2, 2): 3, (2, 3): 2, (3, 0): 0, (3, 1): 1, (3, 2): 2, (3, 3): 3}


def parse_mat(name, text):
    lit = re.search(r"def " + name + r" : W 3 := (!\[!\[[^\n]*\]\])", text).group(1)
    return [[Fr(int(v)) for v in r.split(",")] for r in re.findall(r"!\[([-\d, ]+)\]", lit)]


IDW, CHAINW = parse_mat("idW", K2G), parse_mat("chainW", K2G)
PHIW = [[Fr(([1, 1, -1, 1][i]) if i == j else 0) for j in R4] for i in R4]
HS_REFLY = [1, 1, -1, 1]
XPLUS, Z3 = [1, 0, 0], [0, 0, 1]


def hom3(x):
    return [1] + list(x)


def prodState(x, y):
    hx, hy = hom3(x), hom3(y)
    return [[hx[m] * hy[n] for n in R4] for m in R4]


def cnot(w):
    return [[(-1 if (m, n) in NEG else 1) * w[PC[(m, n)]][PT[(m, n)]] for n in R4] for m in R4]


def actT(hs, w):
    return [[hs[n] * w[m][n] for n in R4] for m in R4]


def pairVal(a, b, w):
    return sum(a[m] * w[m][n] * b[n] for m in R4 for n in R4)


def sharpVec(b):
    return [sp.Rational(1, 2)] + [sp.Rational(1, 2) * sp.sympify(v) for v in b]


check("K parsed tables and literals equal the hand transcriptions; cnot(prodState xplus z3) = phiW, actT reflY phiW = "
      "idW, cnot idW = chainW reproduce",
      PC == PC_H and PT == PT_H and NEG == {(1, 3), (2, 2)}
      and "def phiW : W 3 := fun μ ν => if μ = ν then (if μ = 2 then -1 else 1) else 0" in CD
      and IDW == [[1 if i == j else 0 for j in R4] for i in R4]
      and CHAINW == [[1, 0, 0, 1], [1, 0, 0, -1], [0, 0, 0, 0], [0, 0, 0, 0]]
      and cnot(prodState(XPLUS, Z3)) == PHIW and actT(HS_REFLY, PHIW) == IDW and cnot(IDW) == CHAINW)

# ---------------------------------------------------------------- D
ml = read(os.path.join(MLROOT, "Mathlib/Data/Fin/VecNotation.lean")).split("\n")
D1 = (CIL[581].strip() == "def hom (x : Fin d → ℝ) : Fin (d + 1) → ℝ := Fin.cons 1 x"
      and CDL[99].strip() == "def hom (x : Fin d → ℝ) : HVec d := Matrix.vecCons 1 x"
      and ml[58].strip() == "def vecCons {n : ℕ} (h : α) (t : Fin n → α) : Fin n.succ → α :=" and ml[59].strip() ==
      "Fin.cons h t")
check("D1 Model.hom = Fin.cons 1 x (CI:582), DIM-1 hom = Matrix.vecCons 1 x (CD:100), Matrix.vecCons = Fin.cons "
      "(Mathlib Data/Fin/VecNotation.lean:59-60)", D1)
D2 = (CIL[601].strip() == "def coeff (e : (Fin d → ℝ) →ᵃ[ℝ] ℝ) : Fin (d + 1) → ℝ :="
      and CIL[602].strip() == "Fin.cons (e 0) fun i => e.linear (fun j => if i = j then 1 else 0)"
      and CDL[166].strip() == "noncomputable def ehom (e : (Fin d → ℝ) →ᵃ[ℝ] ℝ) : HVec d :="
      and CDL[167].strip() == "Matrix.vecCons (e 0) fun j => e.linear fun i => if j = i then (1 : ℝ) else 0")
check("D2 COMP-1 coeff (CI:602-603) and DIM-1 ehom (CD:167-168) are the same coefficient vector (indicator of i = j vs "
      "j = i)", D2)
D3 = (TBL[670].startswith("theorem eball_three : eball 3 = ball3")
      and CIL[225].strip() == "convex : Convex ℝ Ω"
      and CIL[226].strip() == "prod_mem : ∀ x ∈ ΩA, ∀ y ∈ ΩB, prodState x y ∈ Ω"
      and CIL[466].startswith("theorem subset_maxBody : P.Ω ⊆ P.toProductData.maxBody ΩA ΩB")
      and CIL[270].startswith("def maxBody (ΩA : Set (Fin dA → ℝ)) (ΩB : Set (Fin dB → ℝ)) : Set V :=")
      and K2L[94].strip() == "def CandidateCone (K : Set (W 3)) : Prop :="
      and K2L[95].strip() == "(∀ x ∈ eball 3, ∀ y ∈ eball 3, prodState x y ∈ K) ∧ K ⊆ maxCone (eball 3)"
      and CDL[185].strip() == "def maxCone (Ω : Set (Fin d → ℝ)) : Set (W d) :="
      and CDL[189].strip() == "def jointStates (Ω : Set (Fin d → ℝ)) : Set (W d) :="
      and CIL[806].startswith("def ball3MinComposite : Composite ball3 ball3 (Carrier 3 3)")
      and CIL[810].startswith("def ball3MaxComposite : Composite ball3 ball3 (Carrier 3 3)"))
check("D3 eball_three (TB:671), convex/prod_mem (CI:226-227), subset_maxBody (CI:467), maxBody (CI:271), "
      "CandidateCone (K2G:95-96), maxCone (CD:186), jointStates (CD:190), ball3Min/MaxComposite (CI:807, 811) present",
      D3)

# ---------------------------------------------------------------- G
bs, cs = sp.symbols("b1:4"), sp.symbols("c1:4")
u0 = [1, 0, 0, 0]
g1a = pairVal(u0, u0, IDW) == 1
g1b = sp.expand(pairVal(u0, sharpVec(cs), IDW) - sp.Rational(1, 2)) == 0
g1c = sp.expand(pairVal(sharpVec(bs), u0, IDW) - sp.Rational(1, 2)) == 0
g1d = sp.expand(pairVal(sharpVec(bs), sharpVec(cs), IDW) - (1 + sum(b * c for b, c in zip(bs, cs))) / 4) == 0
chain_neg = pairVal(sharpVec([-1, 0, 0]), sharpVec([0, 0, -1]), CHAINW)
check("G1 idW passes the Lorentz pairings (unit/unit 1; unit/sharp 1/2; sharp/sharp (1 + b.c)/4, symbolic) and "
      "chainW = cnot idW has a negative sharp-pair value: maxCone(eball 3) is not cnot-invariant",
      g1a and g1b and g1c and g1d and chain_neg < 0 and cnot(IDW) == CHAINW, "chainW value = %s" % chain_neg)
xs3, ys3 = sp.symbols("x1:4"), sp.symbols("y1:4")
Dy = [ys3[0], -ys3[1], ys3[2]]


def Ffun(w):
    return w[0][0] - w[1][1] + w[2][2] - w[3][3]


sos = (sum((xs3[i] - Dy[i]) ** 2 for i in range(3)) / 2 + (1 - sum(v ** 2 for v in xs3)) / 2
       + (1 - sum(v ** 2 for v in ys3)) / 2)
g2a = sp.expand(Ffun(prodState(xs3, ys3)) - sos) == 0
g2b = Ffun(PHIW) < 0 and cnot(prodState(XPLUS, Z3)) == PHIW
check("G2 F(prodState x y) = 1/2|x - Dy|^2 + 1/2(1 - |x|^2) + 1/2(1 - |y|^2) (symbolic), so F >= 0 on the minimal "
      "body, and F(phiW) < 0 with phiW = cnot(prodState xplus z3): the minimal body is not cnot-invariant",
      g2a and g2b, "F(phiW) = %s" % Ffun(PHIW))
corners = [(s1, s2) for s1 in (1, -1) for s2 in (1, -1)]
spot = [pairVal(sharpVec([-1, 0, 0]), sharpVec([0, 0, -1]),
                cnot(prodState([s1 * v for v in Z3], [s2 * v for v in Z3]))) for s1, s2 in corners]
spot += [pairVal(sharpVec([-1, 0, 0]), sharpVec([0, 0, -1]), cnot(prodState(XPLUS, Z3)))]
check("G-controls: F(prodState xplus z3) >= 0; the sharp pair of K2G:134 is nonnegative on cnot of the corner products "
      "and of prodState xplus z3 (spot values of the landed cnot_prodState_mem_maxCone); F(idW), F(chainW) reported",
      Ffun(prodState(XPLUS, Z3)) >= 0 and all(s >= 0 for s in spot),
      "F(idW) = %s, F(chainW) = %s, spot = %s" % (Ffun(IDW), Ffun(CHAINW), spot))

# ---------------------------------------------------------------- C
I = sp.I
S1 = [sp.Matrix([[1, 0], [0, 1]]), sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -I], [I, 0]]),
      sp.Matrix([[1, 0], [0, -1]])]


def skron(A, B):
    # run 2 fix: rectangular shapes (run 1 assumed square matrices and failed on column vectors)
    (ra, ca), (rb, cb) = A.shape, B.shape
    return sp.Matrix(ra * rb, ca * cb, lambda i, j: A[i // rb, j // cb] * B[i % rb, j % cb])


def table_of_state(psi):
    rho = psi * psi.H
    return [[sp.simplify((rho * skron(S1[m], S1[n])).trace()) for n in R4] for m in R4], rho


def pauliW(T):
    acc = sp.zeros(4, 4)
    for m in R4:
        for n in R4:
            acc += sp.Rational(1, 4) * T[m][n] * skron(S1[m], S1[n])
    return acc


psi = sp.Matrix([1, 1, 1, -1]) / 2
Tpsi, rho_psi = table_of_state(psi)
c1 = all(sp.im(Tpsi[m][n]) == 0 for m in R4 for n in R4) and (pauliW(Tpsi) - rho_psi).applyfunc(sp.simplify) == \
    sp.zeros(4, 4) and rho_psi.rank() == 1
check("C1 T_psi is real and pauliW(T_psi) = |psi><psi| (rank one): a boundary element of Q3", c1,
      "T_psi = %s" % [[sp.nsimplify(v) for v in row] for row in Tpsi])
Cm = sp.Matrix([[psi[0], psi[1]], [psi[2], psi[3]]])
inv_psi = Cm[0, 0] * Cm[1, 0] - Cm[0, 1] * Cm[1, 1]
a0, a1, b0, b1 = sp.symbols("a0 a1 b0 b1")
Ccn = sp.Matrix([[a0 * b0, a0 * b1], [a1 * b1, a1 * b0]])
inv_cn = sp.expand(Ccn[0, 0] * Ccn[1, 0] - Ccn[0, 1] * Ccn[1, 1])
CNOT = sp.Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
ab = CNOT * skron(sp.Matrix([a0, a1]), sp.Matrix([b0, b1]))
c2 = (Cm.det() != 0 and inv_psi != 0 and inv_cn == 0
      and list(ab) == [a0 * b0, a0 * b1, a1 * b1, a1 * b0])
check("C2 det C(psi) != 0 (not a product) and C00 C10 - C01 C11 != 0 for psi, while the expression vanishes "
      "identically on CNOT(a (x) b) (symbolic): psi is neither a product nor a CNOT image of a product", c2,
      "det = %s, invariant = %s" % (Cm.det(), inv_psi))
plus0 = CNOT * skron(sp.Matrix([1, 1]) / sp.sqrt(2), sp.Matrix([1, 0]))
Cp = sp.Matrix([[plus0[0], plus0[1]], [plus0[2], plus0[3]]])
Tp, _ = table_of_state(plus0)
c3 = sp.simplify(Cp[0, 0] * Cp[1, 0] - Cp[0, 1] * Cp[1, 1]) == 0 and all(
    sp.simplify(Tp[m][n] - PHIW[m][n]) == 0 for m in R4 for n in R4)
check("C3 control: CNOT(|+> (x) |0>) has invariant 0 and table cnot(prodState xplus z3) = phiW", c3)

# ---------------------------------------------------------------- N
RSB = read(BASE + "/RelcSelectBlock.lean").split("\n")
RSP = read(BASE + "/RelcSelectParity.lean").split("\n")
cite = [(RSB, 45, "structure CtrlGate"), (RSB, 53, "theorem ctrlGate_of_nativeGate"),
        (RSB, 60, "theorem gate_corner_ctrl"), (RSB, 87, "theorem lor_Minv_ctrl"),
        (RSB, 99, "theorem gate_corner_neg_ctrl"), (RSB, 129, "theorem gt_tangent_corners_ctrl"),
        (RSB, 162, "theorem gt_sphere_ctrl"), (RSP, 329, "theorem finrank_plus_eq_finrank_minus_relC"),
        (CDL, 1805, "theorem corner_form"), (CDL, 1870, "theorem lor_cornerMap"), (CDL, 2051, "theorem tangent_vanish")]
present = all(src[ln - 1].startswith(txt) for src, ln, txt in cite)
absent = True
for f in sorted(os.listdir(BASE)):
    if f.endswith(".lean"):
        t = read(os.path.join(BASE, f))
        if re.search(r"\bctrlGate_classification\b|\bNClass\b", t):
            absent = False
check("N the landed lemmas cited by EQ2-B's N-CLASS route are present at the cited lines, and no classification "
      "theorem (ctrlGate_classification, NClass) is present in the base", present and absent)

nfail = sum(1 for _, ok in CHECKS if not ok)
print("--- s2_pair_premises: %d/%d checks pass" % (len(CHECKS) - nfail, len(CHECKS)))
print("VERDICT S2-PAIR-PREMISE-CORES-EXACT" if nfail == 0 else "VERDICT NOT RENDERED")
