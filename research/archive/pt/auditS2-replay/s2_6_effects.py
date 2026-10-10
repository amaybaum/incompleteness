#!/usr/bin/env python3
"""S2 / node S2.6: generated effects versus the full duals; which effect set the theorem's premises consume.
Exact arithmetic only (Fractions, sympy rationals / symbols).

Run:  cd pt/S2 && python3 -I -B s2_6_effects.py ../base/verification/lean-mathlib/OIBridge ../inputs/fourcopy

Objects: ipW(E, X) = sum E_mn X_mn (design FourCopyDefs); dualW; fourVal X Y E F = sum X_ab Y_cd E_ac F_bd
(= ipW X (E Y F^T), famI); K_gen = cone(SEP u cnot SEP); E_gen = cone of the tables of the generated tests
"w then e (x) f", w in {id, cnot}; T_psi = actT R_H phiW; F = E00/2 - T_psi/4 (Thread A's dual witness).

DECISION RULES (fixed before the first run):
 F0 Transcription: pc/pt parsed; cnot involution; cnot pxz = phiW.  Failure: ABORT.
 F1 cnot is symmetric and orthogonal for ipW (matrix C^T = C, C^T C = I), so the table of the test "cnot then e (x) f"
    is cnot(ehom e (x) ehom f); every sharp product effect table equals (1/4) prodState(b, c) (axis and Pythagorean
    unit vectors).  Hence E_gen = K_gen as cones (written step).
 F2 ipW(E, X) = 4 Tr(rho(E) rho(X)) on all 256 basis pairs (so dualW Q3 = Q3 by self-duality of the PSD cone, written).
 F3 F: ipW(F, T_psi) = -1/2; symbolically ipW(F, prodState x y) = 1/2 - (1/4)(1 + x^T M y) and
    ipW(F, cnot prodState x y) = 1/2 - (1/4)(1 + x^T M' y) with M, M' orthogonal (exact), so F is in dualW K_gen
    (written Cauchy-Schwarz step); rho(F) is not PSD, certified exactly by Tr(rho(F) rho(T_psi)) = -1/8 with
    rho(T_psi) a pure state, so F lies outside Q3 and outside E_gen; T_psi lies in Q3 but outside E_gen (table ranks
    of T_psi and cnot T_psi both > 1).
 F4 famI(phiW, phiW, T_psi/4, F) = -1/8 exactly (an instance with Bell states and full-dual effects).
 F5 FCC on generated objects of uniform K_gen: famI and famII are >= 0 (i) at (phiW, phiW) against all pairs of
    generated effect tables of the axis data, (ii) symmetrically for famII, (iii) on a fixed deterministic sample of
    quadruples of generated states and generated effects.  Countercontrol: the instance of F4 must fail (negative).
 F6 Source scan of the design proof (FourCopyIE1, FourCopyBridge): every FCC application on the proof path of
    kt4_forward_ie1 is classified slot by slot (a slot written `_` is bound to its membership hypothesis, a named slot is
    a free variable).  Required pattern: cross_rel's upper use binds the effect slots and frees the state slots; every
    lower use (cross_rel and the four inv_* lemmas) binds the state slots and frees the effect slots; target02 maps upper
    to famII and lower to famI; the parity witness use binds all slots.  Countercontrol: a planted line with bound
    effect slots must be classified "effects bound".
 F7 IE1 fails for K_gen: phiW is in K_gen and T_psi = actT R_H phiW is not (F3's ranks).
 VERDICT lines print only if F0-F7 pass and the countercontrols fail as required.
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
def transpose(A): return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]
def hom(x): return (1, x[0], x[1], x[2])
def prodState(x, y):
    hx, hy = hom(x), hom(y); return [hx[m] * hy[n] for (m, n) in IDX]
def outer(a, b): return [a[m] * b[n] for (m, n) in IDX]
def ipW(E, X): return sum(E[i] * X[i] for i in range(16))
def as44(w): return [[w[k(m, n)] for n in range(4)] for m in range(4)]
def fourVal(X, Y, E, F):
    Xm, Ym, Em, Fm = as44(X), as44(Y), as44(E), as44(F)
    EYFt = mmul(mmul(Em, Ym), transpose(Fm))
    return sum(Xm[a][b] * EYFt[a][b] for a in range(4) for b in range(4))
def famI(X, Y, E, F): return fourVal(X, Y, E, F)
def famII(L, Lp, e, f):
    # ipW e (tabMul (tabMul L f) (tabT L')) = sum_ab e_ab (L f L'^T)_ab
    em, Lm, fm, Lpm = as44(e), as44(L), as44(f), as44(Lp)
    M = mmul(mmul(Lm, fm), transpose(Lpm))
    return sum(em[a][b] * M[a][b] for a in range(4) for b in range(4))
def sharpv(b): return (Fr(1, 2), Fr(b[0], 2), Fr(b[1], 2), Fr(b[2], 2))
def table_rank(w):
    return sp.Matrix(as44([sp.nsimplify(t) for t in w])).rank()

# ---------------------------------------------------------------- F0
oib = sys.argv[1] if len(sys.argv) > 1 else "../base/verification/lean-mathlib/OIBridge"
fcp = sys.argv[2] if len(sys.argv) > 2 else "../inputs/fourcopy"
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
check("F0.pc/pt transcription", parse_table("pc") == PC and parse_table("pt") == PT)
CNOT = [[0] * 16 for _ in range(16)]
for (m, n) in IDX:
    CNOT[k(m, n)][k(PC[m][n], PT[m][n])] = SGN(m, n)
check("F0.cnot involution", mmul(CNOT, CNOT) == eye(16))
xplus, z3 = (1, 0, 0), (0, 0, 1)
phiW = [(1 if m != 2 else -1) if m == n else 0 for (m, n) in IDX]
pxz = prodState(xplus, z3)
check("F0.cnot pxz = phiW", mvec(CNOT, pxz) == phiW)
if not OK:
    print("ABORT"); sys.exit(1)

# ---------------------------------------------------------------- F1
check("F1.cnot symmetric (C^T = C)", transpose(CNOT) == CNOT)
check("F1.cnot orthogonal (C^T C = I)", mmul(transpose(CNOT), CNOT) == eye(16))
UNITS = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1),
         (Fr(3, 5), Fr(4, 5), 0), (0, Fr(3, 5), Fr(4, 5)), (Fr(1, 3), Fr(2, 3), Fr(2, 3))]
sh = all(outer(sharpv(b), sharpv(c)) == [t / 4 for t in prodState(b, c)] for b in UNITS for c in UNITS)
check("F1.sharp product effect tables = (1/4) prodState(b, c)", sh)

# ---------------------------------------------------------------- F2 ipW = 4 Tr(rho rho)
I2 = sp.eye(2); X = sp.Matrix([[0, 1], [1, 0]]); Y = sp.Matrix([[0, -sp.I], [sp.I, 0]]); Z = sp.Matrix([[1, 0], [0, -1]])
PAULI = [I2, X, Y, Z]
SS = [[sp.kronecker_product(PAULI[m], PAULI[n]) for n in range(4)] for m in range(4)]
def rho_of(w):
    R = sp.zeros(4, 4)
    for (m, n) in IDX:
        if w[k(m, n)] != 0: R += sp.nsimplify(w[k(m, n)]) * SS[m][n]
    return R / 4
basis = [[1 if i == j else 0 for i in range(16)] for j in range(16)]
f2 = all(ipW(basis[i], basis[j]) == sp.nsimplify(4 * (rho_of(basis[i]) * rho_of(basis[j])).trace())
         for i in range(16) for j in range(16))
check("F2.ipW(E, X) = 4 Tr(rho(E) rho(X)) on all 256 basis pairs", f2)

# ---------------------------------------------------------------- F3 the dual witness F
RH = [[0, 0, 1], [0, -1, 0], [1, 0, 0]]
def actT_map(N):
    H = [[1, 0, 0, 0]] + [[0] + list(N[i]) for i in range(3)]
    M = [[0] * 16 for _ in range(16)]
    for m in range(4):
        for n in range(4):
            for l in range(4):
                if H[n][l] != 0: M[k(m, n)][k(m, l)] += H[n][l]
    return M
Tpsi = mvec(actT_map(RH), phiW)
E00 = prodState((0, 0, 0), (0, 0, 0))
Fw = [Fr(E00[i], 2) - Fr(Tpsi[i], 4) for i in range(16)]
check("F3.ipW(F, T_psi) = -1/2", ipW(Fw, Tpsi) == Fr(-1, 2), str(ipW(Fw, Tpsi)))
xs = sp.symbols("x0 x1 x2"); ys = sp.symbols("y0 y1 y2")
PS = [sp.Integer(1) * t for t in prodState(xs, ys)]
def read_form(expr):
    """expr = c0 + sum M_ij x_i y_j + linear terms; return (const, M, linear_ok)."""
    expr = sp.expand(expr)
    poly = sp.Poly(expr, *xs, *ys)
    const = poly.coeff_monomial(1)
    M = [[poly.coeff_monomial(xs[i] * ys[j]) for j in range(3)] for i in range(3)]
    lin = all(poly.coeff_monomial(v) == 0 for v in list(xs) + list(ys))
    deg_ok = all(sum(mon[:3]) <= 1 and sum(mon[3:]) <= 1 for mon in poly.monoms())
    return const, M, lin and deg_ok
def orth(M): return all(sum(M[i][r] * M[j][r] for r in range(3)) == (1 if i == j else 0) for i in range(3) for j in range(3))
c1, M1, ok1 = read_form(ipW([sp.nsimplify(t) for t in Fw], PS))
c2, M2, ok2 = read_form(ipW([sp.nsimplify(t) for t in Fw], [sp.expand(t) for t in mvec(CNOT, PS)]))
check("F3.ipW(F, prodState x y) = 1/4 - (1/4) x^T M y with M orthogonal", ok1 and c1 == sp.Rational(1, 4) and
      orth([[-4 * t for t in r] for r in M1]), f"M = {[[-4 * t for t in r] for r in M1]}")
check("F3.ipW(F, cnot prodState x y) = 1/4 - (1/4) x^T M' y with M' orthogonal", ok2 and c2 == sp.Rational(1, 4) and
      orth([[-4 * t for t in r] for r in M2]), f"M' = {[[-4 * t for t in r] for r in M2]}")
RF = rho_of(Fw)
RT = rho_of(Tpsi)
check("F3.T_psi in Q3 (pure: rho^2 = rho, trace 1)", sp.simplify(RT * RT - RT) == sp.zeros(4, 4) and RT.trace() == 1)
trFT = sp.nsimplify(sp.expand((RF * RT).trace()))
check("F3.rho(F) not PSD: Tr(rho(F) rho(T_psi)) = -1/8 < 0 with rho(T_psi) PSD (F outside Q3, hence outside E_gen)",
      trFT == sp.Rational(-1, 8), str(trFT))
r1, r2 = table_rank(Tpsi), table_rank(mvec(CNOT, Tpsi))
check("F3.T_psi outside E_gen = K_gen (table ranks of T_psi, cnot T_psi > 1)", r1 > 1 and r2 > 1, f"{r1}, {r2}")

# ---------------------------------------------------------------- F4
v4 = famI(phiW, phiW, [Fr(t, 4) for t in Tpsi], Fw)
check("F4.famI(phiW, phiW, T_psi/4, F) = -1/8", v4 == Fr(-1, 8), str(v4))

# ---------------------------------------------------------------- F5 FCC on generated objects
AX = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
GEN_EFF = []
for b in AX:
    for c in AX:
        E = outer(sharpv(b), sharpv(c))
        GEN_EFF.append(E); GEN_EFF.append(mvec(CNOT, E))
GEN_ST = []
for b in AX + [(Fr(3, 5), Fr(4, 5), 0), (0, Fr(3, 5), Fr(4, 5))]:
    for c in AX + [(Fr(3, 5), Fr(4, 5), 0)]:
        P = prodState(b, c)
        GEN_ST.append(P); GEN_ST.append(mvec(CNOT, P))
i_ok = all(famI(phiW, phiW, E, F) >= 0 for E in GEN_EFF for F in GEN_EFF)
check("F5.(i) famI(phiW, phiW, E, F) >= 0 for all generated effect pairs (5184)", i_ok)
ii_ok = all(famII(phiW, phiW, e, f) >= 0 for e in GEN_EFF for f in GEN_EFF)
check("F5.(ii) famII(phiW, phiW, e, f) >= 0 for all generated effect pairs (5184)", ii_ok)
seed = 12345
def lcg():
    global seed
    seed = (1103515245 * seed + 12345) % (2 ** 31)
    return seed
iii_ok = True
for _ in range(3000):
    Xs = GEN_ST[lcg() % len(GEN_ST)]; Ys = GEN_ST[lcg() % len(GEN_ST)]
    Es = GEN_EFF[lcg() % len(GEN_EFF)]; Fs = GEN_EFF[lcg() % len(GEN_EFF)]
    if famI(Xs, Ys, Es, Fs) < 0 or famII(Xs, Ys, Es, Fs) < 0:
        iii_ok = False
check("F5.(iii) famI and famII >= 0 on 3000 sampled generated quadruples", iii_ok)
control("F5.instance with the full-dual effects (F4) is nonnegative", v4 >= 0)

# ---------------------------------------------------------------- F6 source scan
ie1 = open(os.path.join(fcp, "FourCopyIE1.lean"), encoding="utf-8").read()
bridge = open(os.path.join(fcp, "FourCopyBridge.lean"), encoding="utf-8").read()
def decl_body(text, name):
    mm = re.search(r"theorem " + re.escape(name) + r"\b(.*?)(?=\n(?:theorem|def|/--|set_option|end)\b)", text, re.S)
    return mm.group(1) if mm else ""
def apps(body, fam):
    return [m.group(1).split() for m in re.finditer(r"h\." + fam + r"((?:\s+[^\s)]+){8})", body)]
def classify(args):
    st = "states bound" if args[0] == "_" and args[2] == "_" else ("states free" if args[0] != "_" and args[2] != "_" else "mixed")
    ef = "effects bound" if args[4] == "_" and args[6] == "_" else ("effects free" if args[4] != "_" and args[6] != "_" else "mixed")
    return st, ef
res = {}
for name in ["cross_rel", "inv_left_ctrl", "inv_right_ctrl", "inv_left_partner", "inv_right_partner",
             "kt4_parity_of_witnesses"]:
    b = decl_body(ie1, name)
    res[name] = {fam: [classify(a) for a in apps(b, fam)] for fam in ("upper", "lower", "famI", "famII")}
for name in res:
    print(f"INFO scan {name}: " + "; ".join(f"{fam}={res[name][fam]}" for fam in res[name] if res[name][fam]))
pat_ok = (res["cross_rel"]["upper"] == [("states free", "effects bound")] and
          res["cross_rel"]["lower"] == [("states bound", "effects free")] and
          all(res[n]["lower"] == [("states bound", "effects free")] for n in
              ["inv_left_ctrl", "inv_right_ctrl", "inv_left_partner", "inv_right_partner"]) and
          all(not res[n]["upper"] for n in ["inv_left_ctrl", "inv_right_ctrl", "inv_left_partner", "inv_right_partner"]) and
          res["kt4_parity_of_witnesses"]["famI"] == [("states bound", "effects bound")])
check("F6.consumption pattern on the proof path", pat_ok)
t02 = decl_body(bridge, "FourCopyCoherent.target02")
t02_ok = re.search(r"upper X hX Y hY E hE F hF := by\s*\n\s*have h1 := h\.famII", t02) is not None and \
         re.search(r"lower L hL L' hL' e he f hf := by\s*\n\s*have h1 := h\.famI ", t02) is not None
check("F6.target02: upper reads famII, lower reads famI", t02_ok)
planted = classify("_ sa _ sb _ ea _ eb".split())
control("F6.classifier calls a bound-effect line 'effects free'", planted[1] == "effects free", str(planted))

# ---------------------------------------------------------------- F7
check("F7.IE1 fails for K_gen: phiW in K_gen, actT R_H phiW outside (ranks)", mvec(CNOT, pxz) == phiW and r1 > 1 and r2 > 1)

print(f"SUMMARY checks passed={NPASS} all_ok={OK}")
if OK:
    print("VERDICT EFFECTS: for the cnot-generated pair system the generated effect cone equals the generated state cone "
          "K_gen; the full dual dualW K_gen is strictly larger (F outside Q3); FCC restricted to generated effects holds "
          "for uniform K_gen on every checked instance (written: all generated objects lie in Q3); the failing instance "
          "uses non-generated effects")
    print("VERDICT CONSUMPTION: the design proof consumes FCC with bound (gate-supplied) effects and free states in "
          "cross_rel's first half, and with bound (gate-supplied) states and FREE full-dual effects in cross_rel's second "
          "half and the four invariance lemmas, for both families (target02 swaps them); the parity step binds all slots")
else:
    print("NO VERDICT")
