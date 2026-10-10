"""
precheck_g7g14.py -- exact symbolic precheck of every table identity used by the G7, G14b and G6 proofs
(EQ4-F design runs 4-6). Definitions are transcribed from the base (CompositeDimension, K2Guard,
KInfFoundations, FourCopyEuler, FourCopyParity, FourCopyCore); transcriptions are checked against the
base source text in T0.

Usage: python3 -I -B precheck_g7g14.py <OIBridge dir>

Decision rule (fixed before the first run): VERDICT PRECHECK-G7G14-PASS iff every check P1-P13 and every
countercontrol N1-N5 behaves as stated (P: identity holds exactly; N: identity FAILS), and T0 passes;
otherwise VERDICT NOT RENDERED. Cosines and sines are independent symbols (c, s) wherever the Lean proof
closes by `ring`, so no trigonometric identity is assumed.
"""
import os
import sys
import itertools
import sympy as sp

OI = sys.argv[1]
results = []


def check(name, cond, detail=""):
    results.append(bool(cond))
    print(("PASS " if cond else "FAIL ") + name + (("  [" + detail + "]") if detail else ""))


def src(fn):
    with open(os.path.join(OI, fn), encoding="utf-8") as fh:
        return fh.read()


# ------------------------------------------------------------------ T0: transcription against the base text
cd = src("CompositeDimension.lean")
k2 = src("K2Guard.lean")
kf = src("KInfFoundations.lean")
eu = src("FourCopyEuler.lean")
pa = src("FourCopyParity.lean")
co = src("FourCopyCore.lean")
t0 = all([
    "def sgn (μ ν : Fin 4) : ℝ := if (μ = 1 ∧ ν = 3) ∨ (μ = 2 ∧ ν = 2) then -1 else 1" in cd,
    "| 0, 0 => 0 | 0, 1 => 0 | 0, 2 => 3 | 0, 3 => 3" in cd,
    "| 1, 0 => 1 | 1, 1 => 1 | 1, 2 => 2 | 1, 3 => 2" in cd,
    "| 2, 0 => 2 | 2, 1 => 2 | 2, 2 => 1 | 2, 3 => 1" in cd,
    "| 3, 0 => 3 | 3, 1 => 3 | 3, 2 => 0 | 3, 3 => 0" in cd,
    "| 0, 0 => 0 | 0, 1 => 1 | 0, 2 => 2 | 0, 3 => 3" in cd,
    "| 1, 0 => 1 | 1, 1 => 0 | 1, 2 => 3 | 1, 3 => 2" in cd,
    "| 2, 0 => 1 | 2, 1 => 0 | 2, 2 => 3 | 2, 3 => 2" in cd,
    "| 3, 0 => 0 | 3, 1 => 1 | 3, 2 => 2 | 3, 3 => 3" in cd,
    "def cnotFun (ω : W 3) : W 3 := fun μ ν => sgn μ ν * ω (pc μ ν) (pt μ ν)" in cd,
    "def phiW : W 3 := fun μ ν => if μ = ν then (if μ = 2 then -1 else 1) else 0" in cd,
    "def z3 : Fin 3 → ℝ := ![0, 0, 1]" in cd,
    "def xplus : Fin 3 → ℝ := ![1, 0, 0]" in cd,
    "toFun v := Matrix.vecCons (v 0) (N (Matrix.vecTail v))" in cd,
    "def actT (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (ω : W d) : W d := fun μ => homMap N (ω μ)" in cd,
    "fun μ ν => homMap N (fun κ => ω κ ν) μ" in cd,
    "def prodState (x y : Fin d → ℝ) : W d := fun μ ν => hom x μ * hom y ν" in cd,
    "toFun x := fun i => (![1, -1, 1] : Fin 3 → ℝ) i * x i" in k2,
    "def idW : W 3 := ![![1, 0, 0, 0], ![0, 1, 0, 0], ![0, 0, 1, 0], ![0, 0, 0, 1]]" in k2,
    "![Real.cos t * v 0 - Real.sin t * v 1, Real.sin t * v 0 + Real.cos t * v 1, v 2]" in kf,
    "theorem cycEquiv_apply' (v : Fin 3 → ℝ) : cycEquiv v = ![v 2, v 0, v 1] := rfl" in eu,
    "theorem cycEquiv_symm_apply' (v : Fin 3 → ℝ) : cycEquiv.symm v = ![v 1, v 2, v 0] := rfl" in eu,
    "theorem rotX_linear_apply (t : ℝ) (v : Fin 3 → ℝ) :" in eu,
    "((rotX t).linear : E3) v = cycEquiv (rotFun t (cycEquiv.symm v)) := rfl" in eu,
    "def dg (p q r s : ℝ) : W 3 := ![![p, 0, 0, 0], ![0, q, 0, 0], ![0, 0, r, 0], ![0, 0, 0, s]]" in pa,
    "def bellOf (A B : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) : W 3 := actC A (actT B phiW)" in co,
    "A ∘ₗ reflY ∘ₗ trn B" in co,
    "decide (LinearMap.det A * LinearMap.det B = -1)" in co,
    "((rot3 a).linear : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) ∘ₗ" in co,
])
check("T0 transcription: every transcribed definition matches the base source text", t0)

SGN = {}
PC = {}
PT = {}
pc_rows = [[0, 0, 3, 3], [1, 1, 2, 2], [2, 2, 1, 1], [3, 3, 0, 0]]
pt_rows = [[0, 1, 2, 3], [1, 0, 3, 2], [1, 0, 3, 2], [0, 1, 2, 3]]
for m in range(4):
    for n in range(4):
        SGN[m, n] = -1 if (m == 1 and n == 3) or (m == 2 and n == 2) else 1
        PC[m, n] = pc_rows[m][n]
        PT[m, n] = pt_rows[m][n]


def cnot(w):
    return sp.Matrix(4, 4, lambda m, n: SGN[m, n] * w[PC[m, n], PT[m, n]])


def H(M):
    """homMap as a 4x4 matrix: block diag(1, M)."""
    out = sp.zeros(4, 4)
    out[0, 0] = 1
    for i in range(3):
        for j in range(3):
            out[i + 1, j + 1] = M[i, j]
    return out


def actC(M, w):
    return H(M) * w           # (actC M w)_{mu nu} = sum_k H_{mu k} w_{k nu}


def actT(M, w):
    return w * H(M).T         # (actT M w)_{mu nu} = sum_k H_{nu k} w_{mu k}


def hom(x):
    return sp.Matrix([1, x[0], x[1], x[2]])


def prodState(x, y):
    return hom(x) * hom(y).T


PHI = sp.Matrix(4, 4, lambda m, n: (-1 if m == 2 else 1) if m == n else 0)
IDW = sp.eye(4)
REFLY = sp.diag(1, -1, 1)
XPLUS = [1, 0, 0]
Z3 = [0, 0, 1]


def dg(p, q, r, s_):
    return sp.diag(p, q, r, s_)


def rotfun_mat(c, s):
    # rotFun t v = (c v0 - s v1, s v0 + c v1, v2)
    return sp.Matrix([[c, -s, 0], [s, c, 0], [0, 0, 1]])


CYC = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])        # cycEquiv v = (v2, v0, v1)
CYC_S = sp.Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]])      # cycEquiv.symm v = (v1, v2, v0)


def rot3(c, s):
    return rotfun_mat(c, s)


def rotX(c, s):
    return CYC * rotfun_mat(c, s) * CYC_S


c, s, ca, sa, cb, sb = sp.symbols("c s ca sa cb sb")
v = sp.symbols("v0:4")
W = sp.Matrix(4, 4, lambda m, n: sp.Symbol(f"w{m}{n}"))


def zero(M):
    return sp.simplify(sp.expand(M)) == sp.zeros(*M.shape)


# ------------------------------------------------------------------ P1, P2: homMap of the rotations by index
hv = sp.Matrix(v)
R3, RX = rot3(c, s), rotX(c, s)
h3 = H(R3) * hv
hx = H(RX) * hv
p1 = [sp.expand(h3[0] - v[0]), sp.expand(h3[1] - (c * v[1] - s * v[2])), sp.expand(h3[2] - (s * v[1] + c * v[2])),
      sp.expand(h3[3] - v[3])]
p2 = [sp.expand(hx[0] - v[0]), sp.expand(hx[1] - v[1]), sp.expand(hx[2] - (c * v[2] - s * v[3])),
      sp.expand(hx[3] - (s * v[2] + c * v[3]))]
check("P1 homMap (rot3 t) at indices 0..3 = v0, c v1 - s v2, s v1 + c v2, v3", all(e == 0 for e in p1))
check("P2 homMap (rotX t) at indices 0..3 = v0, v1, c v2 - s v3, s v2 + c v3", all(e == 0 for e in p2))
# the affine/linear application of the rotations to xplus, z3
check("P2b rot3 a xplus = (ca, sa, 0); rotX b z3 = (0, -sb, cb)",
      list(rot3(ca, sa) * sp.Matrix(XPLUS)) == [ca, sa, 0] and list(rotX(cb, sb) * sp.Matrix(Z3)) == [0, -sb, cb])

# ------------------------------------------------------------------ P3, P4: cnot commutes with control z / target x
check("P3 cnot (actC (rot3 t) w) = actC (rot3 t) (cnot w), symbolic w, independent c, s",
      zero(cnot(actC(R3, W)) - actC(R3, cnot(W))))
check("P4 cnot (actT (rotX t) w) = actT (rotX t) (cnot w), symbolic w, independent c, s",
      zero(cnot(actT(RX, W)) - actT(RX, cnot(W))))
check("N1 countercontrol: cnot does NOT commute with actC (rotX t) (control x-rotation)",
      not zero(cnot(actC(RX, W)) - actC(RX, cnot(W))))
check("N2 countercontrol: cnot does NOT commute with actT (rot3 t) (target z-rotation)",
      not zero(cnot(actT(R3, W)) - actT(R3, cnot(W))))

# ------------------------------------------------------------------ P5: the transpose moves through phiW
check("P5 actT (rotX t) phiW = actC (rotX t) phiW and actT (rot3 t) phiW = actC (rot3 t) phiW",
      zero(actT(RX, PHI) - actC(RX, PHI)) and zero(actT(R3, PHI) - actC(R3, PHI)))
Mg = sp.Matrix(3, 3, lambda i, j: sp.Symbol(f"m{i}{j}"))
check("P5b general: actT M phiW = actC (reflY M^T reflY) phiW for symbolic M",
      zero(actT(Mg, PHI) - actC(REFLY * Mg.T * REFLY, PHI)))
check("N3 countercontrol: actT M phiW != actC M phiW for symbolic M", not zero(actT(Mg, PHI) - actC(Mg, PHI)))

# ------------------------------------------------------------------ P6, P7: G7(ii), G7(iii)
R3a, RXb = rot3(ca, sa), rotX(cb, sb)
lhs6 = cnot(prodState(list(R3a * sp.Matrix(XPLUS)), list(RXb * sp.Matrix(Z3))))
rhs6 = actC(R3a * RXb, PHI)
check("P6 G7(ii): cnot (prodState (rot3 a xplus) (rotX b z3)) = actC (rotWord a b) phiW (polynomial identity)",
      zero(lhs6 - rhs6))
check("P6b structural route: prodState (R3 xplus) (RX z3) = actC R3 (actT RX (prodState xplus z3))",
      zero(prodState(list(R3a * sp.Matrix(XPLUS)), list(RXb * sp.Matrix(Z3))) -
           actC(R3a, actT(RXb, prodState(XPLUS, Z3)))))
check("P6c cnot (prodState xplus z3) = phiW", zero(cnot(prodState(XPLUS, Z3)) - PHI))
check("P7 G7(iii): actC (rotWord a b) phiW = actT (rotWord' a b) phiW",
      zero(actC(R3a * RXb, PHI) - actT(RXb * R3a, PHI)))
check("N4 countercontrol: actC (rotWord a b) phiW != actT (rotWord a b) phiW (unreversed word)",
      not zero(actC(R3a * RXb, PHI) - actT(R3a * RXb, PHI)))

# ------------------------------------------------------------------ P8: link_mem's algebra
Ag = sp.Matrix(3, 3, lambda i, j: sp.Symbol(f"a{i}{j}"))
Bg = sp.Matrix(3, 3, lambda i, j: sp.Symbol(f"b{i}{j}"))
Wg = sp.Matrix(3, 3, lambda i, j: sp.Symbol(f"x{i}{j}"))
check("P8 actC A (actT B (actC Wd phiW)) = actC (A Wd) (actT B phiW) (symbolic A, B, Wd)",
      zero(actC(Ag, actT(Bg, actC(Wg, PHI))) - actC(Ag * Wg, actT(Bg, PHI))))
check("P8b actC A (actT (B Wd') phiW) = actC A (actT B (actT Wd' phiW)) (symbolic)",
      zero(actC(Ag, actT(Bg * Wg, PHI)) - actC(Ag, actT(Bg, actT(Wg, PHI)))))

# ------------------------------------------------------------------ P9-P11: G14b tables
check("P9 tabMul X idW = X (symbolic X)", zero(W * IDW - W))
check("P10 actC reflY idW = phiW", zero(actC(REFLY, IDW) - PHI))
check("P11 bellOf A B = actC (A reflY B^T) idW (symbolic A, B)",
      zero(actC(Ag, actT(Bg, PHI)) - actC(Ag * REFLY * Bg.T, IDW)))
# tabMul (actC P (actT Q phiW)) g = actC (P reflY Q^T) g (link_mul's hl), checked with g = idW and symbolic g
Gg = sp.Matrix(4, 4, lambda m, n: sp.Symbol(f"g{m}{n}"))
check("P11b tabMul (actC P (actT Q phiW)) g = actC (P reflY Q^T) g (symbolic P, Q, g)",
      zero(actC(Ag, actT(Bg, PHI)) * Gg - actC(Ag * REFLY * Bg.T, Gg)))

# ------------------------------------------------------------------ P12: the pi-rotation about y
RY = sp.diag(-1, 1, -1)
p, q, r, s_ = sp.symbols("p q r s_")
check("P12 rotYpi = diag(-1,1,-1) is in SO(3); actC rotYpi (dg p q r s) = dg p (-q) r (-s)",
      RY.T * RY == sp.eye(3) and RY.det() == 1 and zero(actC(RY, dg(p, q, r, s_)) - dg(p, -q, r, -s_)))
cnotTw = lambda w: actT(REFLY, cnot(actT(REFLY, w)))
sg = {False: -1, True: 1}
ok12b = True
for tau in (False, True):
    g = (lambda w: cnot(w)) if not tau else cnotTw
    a1 = g(prodState(XPLUS, Z3))
    a2 = g(prodState([-1, 0, 0], [0, 0, -1]))
    ok12b &= zero(a1 - dg(1, 1, sg[tau], 1)) and zero(a2 - dg(1, -1, sg[tau], -1)) and zero(a2 - actC(RY, a1))
check("P12b gateOf tau (prodState xplus z3) = dg 1 1 sgnB 1; at (-xplus, -z3) = dg 1 -1 sgnB -1 = actC rotYpi of it",
      ok12b)

# ------------------------------------------------------------------ P13: the orientation reduction, exact orthogonal locals
def rot_axis(axis, cc, ss):
    if axis == 0:
        return sp.Matrix([[1, 0, 0], [0, cc, -ss], [0, ss, cc]])
    if axis == 1:
        return sp.Matrix([[cc, 0, ss], [0, 1, 0], [-ss, 0, cc]])
    return sp.Matrix([[cc, -ss, 0], [ss, cc, 0], [0, 0, 1]])


pyth = [(sp.Rational(3, 5), sp.Rational(4, 5)), (sp.Rational(5, 13), sp.Rational(12, 13)),
        (sp.Rational(8, 17), sp.Rational(-15, 17))]
locals_ = []
for (c1, s1), (c2, s2) in itertools.product(pyth, pyth):
    Rm = rot_axis(0, c1, s1) * rot_axis(2, c2, s2)
    for refl in (sp.eye(3), sp.diag(1, -1, 1), sp.diag(-1, -1, -1)):
        locals_.append(Rm * refl)
ok13 = True
cnt = {True: 0, False: 0}
bad_swap = 0
for i, A_ in enumerate(locals_[:12]):
    for B_ in locals_[5:17]:
        assert A_.T * A_ == sp.eye(3) and B_.T * B_ == sp.eye(3)
        dA, dB = A_.det(), B_.det()
        tau = (dA * dB == -1)
        bell = actC(A_, actT(B_, PHI))
        C_ = A_ * REFLY * B_.T
        if tau:
            Rr = C_.T
            target = IDW
        else:
            Rr = REFLY * C_.T
            target = PHI
        okR = (Rr.T * Rr == sp.eye(3)) and Rr.det() == 1
        ok13 &= okR and zero(actC(Rr, bell) - target)
        ok13 &= (C_.det() == -dA * dB)
        # countercontrol: the other case's rotation is not a rotation or misses the target
        Rw = (REFLY * C_.T) if tau else C_.T
        tw = PHI if tau else IDW
        if not ((Rw.det() == 1) and zero(actC(Rw, bell) - tw)):
            bad_swap += 1
        cnt[tau] += 1
check("P13 orientation reduction on %d exact orthogonal pairs: rotation trn C (tau true) / reflY trn C (tau false) "
      "sends bellOf A B to idW / phiW; det C = -det A det B" % (cnt[True] + cnt[False]),
      ok13 and cnt[True] > 0 and cnt[False] > 0, f"true {cnt[True]}, false {cnt[False]}")
check("N5 countercontrol: the swapped assignment fails on every pair", bad_swap == cnt[True] + cnt[False],
      f"{bad_swap}")

print("--- precheck_g7g14: %d/%d checks behave as stated" % (sum(results), len(results)))
print("VERDICT PRECHECK-G7G14-PASS" if all(results) else "VERDICT NOT RENDERED")
