#!/usr/bin/env python3
"""
ds7_structure.py -- thread DS, question DS.7(c): which parts of the double-slit setting are single-system statements
and which involve a second system and a correlating operation, checked on the objects landed at L.

TRANSCRIPTION (from pt/base/verification/lean-mathlib/OIBridge/CompositeDimension.lean at L = 9f9f8257)
  sgn :741 (-1 at (1,3) and (2,2)), pc :744-748, pt :751-755, cnotFun :758 (cnot :775),
  hom :100 (x -> (1, x)), prodState :161 (hom x ⊗ hom y), actT :198 (row-wise homMap: omega -> omega homMap(N)^T),
  actC :201 (homMap(N) omega), z3 :793 = (0,0,1), xplus :1213 = (1,0,0), phiW :1220 = diag(1,1,-1,1).
  Effects: an affine effect e(x) = e0 + e.x has homogenized coefficients (e0, e1, e2, e3) (ehom, :167); the value of
  e ⊗ f on omega is sum_{mu,nu} ehom(e)_mu omega_{mu nu} ehom(f)_nu (pairVal :164, prodEffVal :182). The unit effect is
  (1,0,0,0). Row index mu = first token (control = path), column index nu = second token (target = detector).
  From AncillaInterference.lean :87-94: hMat = (1/sqrt2)[[1,1],[1,-1]].
  From verification/lean/kt4_prem1_probe.py :119, :560-562: R_H = [[0,0,1],[0,-1,0],[1,0,0]],
  T_psi = actT R_H phiW = [[1,0,0,0],[0,0,0,1],[0,0,1,0],[0,1,0,0]] (a landed exact probe, not a kernel theorem).
Dictionary used only for cross-checks: pauli(omega) = (1/4) sum omega_{mu nu} s_mu ⊗ s_nu, s = (1, X, Y, Z).

DECISION RULES (fixed in this header before the first run; rules, not expected numbers)
Each check prints "ID | text | PASS/FAIL". A countercontrol (CC-) PASSES when the alternative it names is shown to
fail exactly. A block prints its VERDICT only if all its checks PASS, else "VERDICT <block>: VOID". "ALL BLOCKS GREEN"
prints only if every block is green. Exact arithmetic only (sympy, Rationals, sqrt(2)).

S0 dictionary: pauli(cnotFun w) == CNOT pauli(w) CNOT^dag for a symbolic table w (16 real symbols), with
   CNOT = |0><0| ⊗ 1 + |1><1| ⊗ X (control = first factor).
   CC-S0a: with Y and Z interchanged in the dictionary, the equality fails. CC-S0b: with the control on the second
   factor, the equality fails.
S1 the record is the landed gate on a product: cnotFun(prodState xplus z3) == phiW.
   CC-S1: cnotFun(prodState xplus xplus) == prodState xplus xplus (a detector prepared on the gate's flip axis is
   left unchanged: no record), and it differs from phiW.
S2 suppression and what fixes its amount. For symbolic path x = (x1,x2,x3) and detector n = (n1,n2,n3):
   S2-marginal: the path marginal (column nu = 0) of cnotFun(prodState x n) == (1, n1 x1, n1 x2, x3) identically.
   S2-gamma: tr(X rho_n) == n1 for rho_n = (1 + n.s)/2 (the coherence factor gamma = tr(UL^dag UR rho0) of ds5 F3
             with UL = 1, UR = X), identically.
   S2-two-system: at x = xplus, the path marginals for n = z3 and n = xplus differ (the suppression is not a function
             of the path state alone).
   CC-S2: without the gate, the path marginal of prodState x n is (1, x1, x2, x3) for every n.
S3 the eraser is a pair statement. omegaB := (1/2)(prodState z3 z3 + prodState (-z3) (-z3)) (a separable, classical
   record). PASS iff
   S3-a: phiW and omegaB have equal path marginals, equal detector marginals and equal (3,3) entry (Z⊗Z), so the
         unread-detector screen statistics and the which-path statistics coincide;
   S3-b: conditioned on the detector effects f_{+-X} = (1/2)(1, +-1, 0, 0) (the unnormalized path vector
         sum_nu omega_{mu nu} f_nu), phiW gives (1/2)(1, +-1, 0, 0) (path Bloch +-e1: fringes, antifringes) and
         omegaB gives (1/2)(1, 0, 0, 0) (no fringes);
   S3-c: phiW and omegaB differ exactly in the X⊗X and Y⊗Y entries.
   CC-S3: conditioned on the record-basis effects f_{+-Z} = (1/2)(1, 0, 0, +-1), phiW and omegaB give the same vectors.
S4 with a controllable relative phase on the path side the setting is a Bell scenario. E(a,b) = sum_ij a_i w_ij b_j.
   S4-tsirelson: S(phiW) == 2 sqrt2 at a0 = (1,0,0), a1 = (0,1,0), b0 = (1,-1,0)/sqrt2, b1 = (1,1,0)/sqrt2.
   S4-local: max |A0 B0 + A0 B1 + A1 B0 - A1 B1| over the 16 deterministic +-1 assignments == 2 (exhaustive).
   CC-S4: at the same settings S(omegaB) == 0 and S(prodState xplus z3) == 0.
S5 a general detector leaves K_gen = SEP + cnot SEP. psi := CZ (|+> ⊗ |+>) (a phase-kick record, detector in |+>).
   S5-table: the Pauli table of psi psi^dag == actT(R_H, phiW) == the landed T_psi table.
   S5-a: with F := (1/2) 1 - psi psi^dag: tr(F (rho_x ⊗ rho_y)) == (1/4)(1 - x^T M y), M := correlation block of psi,
         M^T M = 1, and 1 - x^T M y == (1/2)|x - M y|^2 + (1/2)(1 - |x|^2) + (1/2)(1 - |y|^2) (identities), so F >= 0
         on every product of ball points.
   S5-b: tr(F CNOT (rho_x ⊗ rho_y) CNOT^dag) == (1/4)(1 - x^T M' y) with M' orthogonal (identities), so F >= 0 on every
         cnot image of a product of ball points.
   S5-c: tr(F psi psi^dag) == -1/2.
   [W] F is linear and >= 0 on the generators of K_gen, hence on K_gen; so the phase-kick record state is not in K_gen.
   S5-stats: the path marginal of psi psi^dag equals that of phiW (both: no coherence).
   CC-S5: tr(F pauli(phiW)) >= 0 (phiW is a generator of K_gen); the exact value is printed.
S6 the balanced mixer moves the all-ones ray: hMat (1,1) == (sqrt2, 0), and no z satisfies (sqrt2, 0) == z (1,1).
   CC-S6: the swap permutation fixes (1,1).
"""
from itertools import product

import sympy as sp

I = sp.I
R4 = range(4)
results, order = {}, []


def chk(block, cid, text, ok):
    ok = bool(ok)
    results.setdefault(block, []).append(ok)
    if block not in order:
        order.append(block)
    print(f"{cid} | {text} | {'PASS' if ok else 'FAIL'}")


def verdict(block, text):
    print(f"VERDICT {block}: {text}" if all(results.get(block, [False])) else f"VERDICT {block}: VOID")


# ------------------------------------------------------------------ transcription of the landed definitions
NEG = {(1, 3), (2, 2)}
PC = [[0, 0, 3, 3], [1, 1, 2, 2], [2, 2, 1, 1], [3, 3, 0, 0]]
PT = [[0, 1, 2, 3], [1, 0, 3, 2], [1, 0, 3, 2], [0, 1, 2, 3]]


def sgn(m, n):
    return -1 if (m, n) in NEG else 1


def cnotFun(w):
    return sp.Matrix(4, 4, lambda m, n: sgn(m, n) * w[PC[m][n], PT[m][n]])


def hom(x):
    return sp.Matrix([1] + list(x))


def prodState(x, y):
    return hom(x) * hom(y).T


def homMap(R):
    M = sp.zeros(4, 4)
    M[0, 0] = 1
    M[1:4, 1:4] = sp.Matrix(R)
    return M


def actT(R, w):
    return w * homMap(R).T


z3 = [0, 0, 1]
mz3 = [0, 0, -1]
xplus = [1, 0, 0]
phiW = sp.diag(1, 1, -1, 1)
R_H = sp.Matrix([[0, 0, 1], [0, -1, 0], [1, 0, 0]])
T_psi_landed = sp.Matrix([[1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0]])

# ------------------------------------------------------------------ dictionary
X = sp.Matrix([[0, 1], [1, 0]])
Y = sp.Matrix([[0, -I], [I, 0]])
Z = sp.Matrix([[1, 0], [0, -1]])
E2 = sp.eye(2)
SIG = [E2, X, Y, Z]


def kron(A, B):
    return sp.kronecker_product(A, B)


def pauli(w, sig=SIG):
    out = sp.zeros(4, 4)
    for m in R4:
        for n in R4:
            if w[m, n] != 0:
                out += w[m, n] * kron(sig[m], sig[n])
    return out / 4


def table(rho):
    return sp.Matrix(4, 4, lambda m, n: sp.simplify((rho * kron(SIG[m], SIG[n])).trace()))


CNOT = sp.Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
CNOT_rev = sp.Matrix([[1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0]])

# ------------------------------------------------------------------ S0
w = sp.Matrix(4, 4, lambda m, n: sp.Symbol(f"w{m}{n}", real=True))
ok0 = (pauli(cnotFun(w)) - CNOT * pauli(w) * CNOT.H).applyfunc(sp.expand) == sp.zeros(4, 4)
chk("S0", "S0", "pauli(cnotFun w) == CNOT pauli(w) CNOT^dag for symbolic w (control = path token)", ok0)
SIGswap = [E2, X, Z, Y]
okA = (pauli(cnotFun(w), SIGswap) - CNOT * pauli(w, SIGswap) * CNOT.H).applyfunc(sp.expand) == sp.zeros(4, 4)
chk("S0", "CC-S0a", "with Y and Z interchanged in the dictionary the equality fails", not okA)
okB = (pauli(cnotFun(w)) - CNOT_rev * pauli(w) * CNOT_rev.H).applyfunc(sp.expand) == sp.zeros(4, 4)
chk("S0", "CC-S0b", "with the control on the detector token the equality fails", not okB)
verdict("S0", "the landed cnot is conjugation by CNOT with the path token as control (Pauli dictionary)")

# ------------------------------------------------------------------ S1
rec = cnotFun(prodState(xplus, z3))
chk("S1", "S1", f"cnotFun(prodState xplus z3) == phiW: {rec == phiW}", rec == phiW)
nore = cnotFun(prodState(xplus, xplus))
chk("S1", "CC-S1", f"detector on the flip axis: cnotFun(prodState xplus xplus) == prodState xplus xplus: "
    f"{nore == prodState(xplus, xplus)}; equals phiW: {nore == phiW}",
    nore == prodState(xplus, xplus) and nore != phiW)
verdict("S1", "a perfect which-path record made by the landed gate on (path |+>, detector on the corner axis) is "
        "phiW")

# ------------------------------------------------------------------ S2
x1, x2, x3, n1, n2, n3 = sp.symbols("x1 x2 x3 n1 n2 n3", real=True)
xs, ns = [x1, x2, x3], [n1, n2, n3]
out = cnotFun(prodState(xs, ns))
pm = [sp.expand(out[m, 0]) for m in R4]
chk("S2", "S2-marginal", f"path marginal of cnot(prodState x n) = {pm}",
    pm == [1, sp.expand(n1 * x1), sp.expand(n1 * x2), x3])
dm = [sp.expand(out[0, n]) for n in R4]
print(f"INFO | detector marginal of cnot(prodState x n) = {dm}")
rho_n = (E2 + n1 * X + n2 * Y + n3 * Z) / 2
g_n = sp.expand((X * rho_n).trace())
chk("S2", "S2-gamma", f"tr(X rho_n) = {g_n} (the coherence factor of the cnot record)", g_n == n1)
mz = [cnotFun(prodState(xplus, z3))[m, 0] for m in R4]
mx = [cnotFun(prodState(xplus, xplus))[m, 0] for m in R4]
chk("S2", "S2-two-system", f"x = xplus: path marginal with n = z3 is {mz}, with n = xplus is {mx}", mz != mx)
pm0 = [sp.expand(prodState(xs, ns)[m, 0]) for m in R4]
chk("S2", "CC-S2", f"no gate: path marginal of prodState x n = {pm0} (independent of n)", pm0 == [1, x1, x2, x3])
verdict("S2", "on the path alone the unread cnot record is the dephasing r -> (n1 r1, n1 r2, r3); its strength n1 "
        "is the detector's state component on the flip axis, a second-system quantity")

# ------------------------------------------------------------------ S3
omegaB = (prodState(z3, z3) + prodState(mz3, mz3)) / 2
pmA = [phiW[m, 0] for m in R4]
pmB = [omegaB[m, 0] for m in R4]
dmA = [phiW[0, n] for n in R4]
dmB = [omegaB[0, n] for n in R4]
chk("S3", "S3-a", f"path marginals {pmA} / {pmB}; detector marginals {dmA} / {dmB}; ZZ entries "
    f"{phiW[3, 3]} / {omegaB[3, 3]}", pmA == pmB and dmA == dmB and phiW[3, 3] == omegaB[3, 3])
h = sp.Rational(1, 2)


def cond(wt, f):
    return [sp.expand(sum(wt[m, n] * f[n] for n in R4)) for m in R4]


fXp, fXm = [h, h, 0, 0], [h, -h, 0, 0]
cA = (cond(phiW, fXp), cond(phiW, fXm))
cB = (cond(omegaB, fXp), cond(omegaB, fXm))
chk("S3", "S3-b", f"X-readout conditionals: phiW {cA}; omegaB {cB}",
    cA == ([h, h, 0, 0], [h, -h, 0, 0]) and cB == ([h, 0, 0, 0], [h, 0, 0, 0]))
dif = phiW - omegaB
nz = sorted((m, n) for m in R4 for n in R4 if dif[m, n] != 0)
chk("S3", "S3-c", f"phiW - omegaB nonzero exactly at {nz}", nz == [(1, 1), (2, 2)])
fZp, fZm = [h, 0, 0, h], [h, 0, 0, -h]
chk("S3", "CC-S3", f"Z-readout conditionals equal: phiW {cond(phiW, fZp)},{cond(phiW, fZm)}; omegaB "
    f"{cond(omegaB, fZp)},{cond(omegaB, fZm)}",
    cond(phiW, fZp) == cond(omegaB, fZp) and cond(phiW, fZm) == cond(omegaB, fZm))
verdict("S3", "the screen pattern with the detector unread and the which-path statistics cannot tell the coherent "
        "record phiW from the separable record omegaB; only a detector readout complementary to the record can")

# ------------------------------------------------------------------ S4
r2 = sp.sqrt(2)
a0, a1 = sp.Matrix([1, 0, 0]), sp.Matrix([0, 1, 0])
b0, b1 = sp.Matrix([1, -1, 0]) / r2, sp.Matrix([1, 1, 0]) / r2


def corr(wt, a, b):
    return sp.simplify((a.T * wt[1:4, 1:4] * b)[0, 0])


def chsh(wt):
    return sp.simplify(corr(wt, a0, b0) + corr(wt, a0, b1) + corr(wt, a1, b0) - corr(wt, a1, b1))


S_phi = chsh(phiW)
chk("S4", "S4-tsirelson", f"S(phiW) = {S_phi}", sp.simplify(S_phi - 2 * r2) == 0)
mx_loc = max(abs(A0 * B0 + A0 * B1 + A1 * B0 - A1 * B1) for A0, A1, B0, B1 in product([1, -1], repeat=4))
chk("S4", "S4-local", f"max over 16 deterministic local assignments = {mx_loc}", mx_loc == 2)
SB, SP = chsh(omegaB), chsh(prodState(xplus, z3))
chk("S4", "CC-S4", f"S(omegaB) = {SB}; S(prodState xplus z3) = {SP}", SB == 0 and SP == 0)
verdict("S4", "with two path settings (a controllable relative phase) and two detector readouts, the cnot record "
        "reaches 2 sqrt2 > 2")

# ------------------------------------------------------------------ S5
CZ = sp.diag(1, 1, 1, -1)
plus = sp.Matrix([1, 1]) / r2
psi = CZ * kron(plus, plus)
rho_psi = psi * psi.H
Tpsi = table(rho_psi)
aTp = actT(R_H, phiW)
chk("S5", "S5-table", f"table(CZ|++>) == actT(R_H, phiW): {Tpsi == aTp}; == landed T_psi: {Tpsi == T_psi_landed}",
    Tpsi == aTp and Tpsi == T_psi_landed)
F = sp.eye(4) / 2 - rho_psi
y1, y2, y3 = sp.symbols("y1 y2 y3", real=True)
xv, yv = sp.Matrix([x1, x2, x3]), sp.Matrix([y1, y2, y3])
rho_x = (E2 + x1 * X + x2 * Y + x3 * Z) / 2
rho_y = (E2 + y1 * X + y2 * Y + y3 * Z) / 2
M = Tpsi[1:4, 1:4]
valP = sp.expand((F * kron(rho_x, rho_y)).trace())
sos = sp.expand(((xv - M * yv).T * (xv - M * yv))[0, 0] / 2 + (1 - (xv.T * xv)[0, 0]) / 2
                + (1 - (yv.T * yv)[0, 0]) / 2)
okP = (sp.expand(valP - (1 - (xv.T * M * yv)[0, 0]) / 4) == 0 and M.T * M == sp.eye(3)
       and sp.expand(1 - (xv.T * M * yv)[0, 0] - sos) == 0)
chk("S5", "S5-a", f"tr(F rho_x⊗rho_y) == (1/4)(1 - x^T M y), M = {M.tolist()}, M^T M = 1, SOS identity", okP)
psi2 = CNOT.H * psi
M2 = table(psi2 * psi2.H)[1:4, 1:4]
valC = sp.expand((F * CNOT * kron(rho_x, rho_y) * CNOT.H).trace())
sos2 = sp.expand(((xv - M2 * yv).T * (xv - M2 * yv))[0, 0] / 2 + (1 - (xv.T * xv)[0, 0]) / 2
                 + (1 - (yv.T * yv)[0, 0]) / 2)
okC = (sp.expand(valC - (1 - (xv.T * M2 * yv)[0, 0]) / 4) == 0 and M2.T * M2 == sp.eye(3)
       and sp.expand(1 - (xv.T * M2 * yv)[0, 0] - sos2) == 0)
chk("S5", "S5-b", f"tr(F CNOT rho_x⊗rho_y CNOT^dag) == (1/4)(1 - x^T M' y), M' = {M2.tolist()}, orthogonal, SOS", okC)
v_psi = sp.simplify((F * rho_psi).trace())
chk("S5", "S5-c", f"tr(F psi psi^dag) = {v_psi}", v_psi == -sp.Rational(1, 2))
chk("S5", "S5-stats", f"path marginals: CZ record {[Tpsi[m, 0] for m in R4]}, phiW {[phiW[m, 0] for m in R4]}",
    [Tpsi[m, 0] for m in R4] == [phiW[m, 0] for m in R4])
v_phi = sp.simplify((F * pauli(phiW)).trace())
chk("S5", "CC-S5", f"tr(F pauli(phiW)) = {v_phi} (must be >= 0: phiW generates K_gen)", v_phi >= 0)
verdict("S5", "the phase-kick record CZ|++> = actT R_H phiW = T_psi lies outside K_gen, with the same path "
        "statistics as the cnot record")

# ------------------------------------------------------------------ S6
hMat = sp.Matrix([[1, 1], [1, -1]]) / r2
ones = sp.Matrix([1, 1])
img = hMat * ones
zsol = sp.solve([img[0] - sp.Symbol("z"), img[1] - sp.Symbol("z")], sp.Symbol("z"), dict=True)
chk("S6", "S6", f"hMat (1,1) = {list(img)}; solutions z of hMat(1,1) == z(1,1): {zsol}",
    list(img) == [r2, 0] and zsol == [])
SW = sp.Matrix([[0, 1], [1, 0]])
chk("S6", "CC-S6", f"swap (1,1) = {list(SW * ones)}", SW * ones == ones)
verdict("S6", "the balanced mixer of AncillaInterference moves the all-ones ray")

# ------------------------------------------------------------------ summary
green = [blk for blk in order if all(results[blk])]
print(f"SUMMARY: {sum(len(v) for v in results.values())} checks; blocks green {len(green)}/{len(order)}")
if len(green) == len(order):
    print("ALL BLOCKS GREEN")
