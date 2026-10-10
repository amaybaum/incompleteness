#!/usr/bin/env python3
"""S2 / node S2.5 (continued) and the flagged routes: what lies beyond the fixed-frame native family.
Exact integer / rational / Gaussian-rational / polynomial arithmetic only.

Run:  cd pt/S2 && python3 -I -B s2_2_beyond.py ../base/verification/lean-mathlib/OIBridge

Conventions as in s2_1_native.py (landed definitions re-transcribed and re-checked here).  Pauli dictionary
w_mn = Tr(rho s_m (x) s_n), first factor = token 1 (control).  Bloch rotations: Rx(c,s) about x0, Rz(c,s) about x2.
C(R,S) := actC R o actT S o cnot o actC R^T o actT S^T  (the local-rotation conjugate of cnot by (R,S)).
SWAP w := w^T (token exchange; not a landed object: an [N] datum).
psi_w := (3|00> + 4|01> + 5|11>)/sqrt(50) (amplitudes in the frame's computational basis; rational table).
Monomial class M: conjugations by unitaries that send each computational basis vector to a phase times a basis
vector (frame-respecting unitaries, diagonal phases, SWAP, local Paulis), and the global transpose.

DECISION RULES (fixed before the first run):
 Q0 Transcription: as R0 of s2_1 (pc, pt, sgn parsed; cnot involution; cnot pxz = phiW).  Failure: ABORT.
 Q1 SWAP: SWAP = Ad(swap unitary) exactly; the group <cnot, SWAP> on W 3 is closed exactly and its order printed;
    the state s_w = SWAP(cnot(prodState u v)), u = (24/25,0,7/25), v = (24/25,0,-7/25), is pure (rho^2 = rho), has
    table rank > 1 and cnot(s_w) has table rank > 1 (so s_w lies outside K_gen by extremality, written step);
    countercontrol: cnot(prodState u v) itself must FAIL the "outside K_gen" test (its cnot image has rank 1).
 Q2 Monomial obstruction: psi_w is pure and in Q3 (exact); its computational modulus pattern p_ab = rho_{ab,ab} is
    read from its table; NO arrangement of the four numbers as a 2x2 matrix has determinant 0 (all 24 permutations);
    countercontrol: the pattern of a pure product state must have an arrangement with determinant 0.  The Schmidt
    spectrum of psi_w equals that of cnot(prodState((3/5,0,4/5), z3)) (reduced Bloch lengths equal, exact).
    For every element g of the group <cnot, SWAP>: g(psi_w) has table rank != 1 (finite exact cross-check, independent
    of the modulus argument, that psi_w lies in no g(SEP), hence outside K_swap by extremality).
 Q3 Frame-respecting gates are monomial: for the CtrlGate member G_t = cnot o actT Rz(3/5,4/5): frame and relC hold,
    relT FAILS (so G_t is CtrlGate, not NativeGate) exactly; cnot o G_t = actT Rz (a local rotation acting on every
    table) exactly.  For the Gaussian-rational unitary Uz = diag(a, conj a), a = (3-4i)/5: Ad(I (x) Uz) = actT M_Z with
    M_Z read off and checked to be a rotation about x2; G' = cnot o actT M_Z satisfies frame and relC, fails relT;
    G' = Ad(CNOT.(I (x) Uz)) and that unitary is monomial in the computational basis.
 Q4 Diagonal entangling family: for U_ZZ = diag(a, conj a, conj a, a), a = (3-4i)/5: cnot o Ad(U_ZZ) o cnot equals
    actT M for a 3x3 rotation M about the z axis (exact), M != I.
 Q5 Frame covariance words (symbolic in (c, s) modulo c^2 + s^2 - 1, and at (3/5, 4/5)):
    W_A = cnot o C(Rx,I) o C(I,Zpi) o C(Rx,Zpi) equals actC M_A with M_A a rotation about x0, M_A != I at (3/5,4/5);
    W_B = cnot o C(I,Rz) o C(Xpi,I) o C(Xpi,Rz) equals actT M_B with M_B a rotation about x2, M_B != I at (3/5,4/5).
    Countercontrol: the shorter word cnot o C(Rx,I) is NOT a local map (it must fail the locality test).
 Q6 Local agency instance (flagged; analysed, not used as a premise): T_psi = actT R_H phiW is pure, in Q3, with
    table rank 4 and cnot(T_psi) table rank 4 (outside K_gen by extremality); it is reached by one local rotation
    acting on the entangled table phiW.
 VERDICT lines print only if Q0-Q6 pass with their countercontrols failing as required.
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
def mat_mul(A, B):
    return tuple(tuple(sum(A[i][r] * B[r][j] for r in range(16) if A[i][r] != 0) for j in range(16)) for i in range(16))
def mat_vec(A, v):
    return tuple(sum(A[i][r] * v[r] for r in range(16) if A[i][r] != 0) for i in range(16))
I16 = tuple(tuple(1 if i == j else 0 for j in range(16)) for i in range(16))
def homMap(N):
    H = [[0] * 4 for _ in range(4)]; H[0][0] = 1
    for i in range(3):
        for j in range(3):
            H[i + 1][j + 1] = N[i][j]
    return H
def actC_map(N):
    H = homMap(N); M = [[0] * 16 for _ in range(16)]
    for m in range(4):
        for n in range(4):
            for q in range(4):
                if H[m][q] != 0: M[k(m, n)][k(q, n)] += H[m][q]
    return tuple(tuple(r) for r in M)
def actT_map(N):
    H = homMap(N); M = [[0] * 16 for _ in range(16)]
    for m in range(4):
        for n in range(4):
            for l in range(4):
                if H[n][l] != 0: M[k(m, n)][k(m, l)] += H[n][l]
    return tuple(tuple(r) for r in M)
def tr3(N): return [[N[j][i] for j in range(3)] for i in range(3)]
def diag3(a, b, c): return [[a, 0, 0], [0, b, 0], [0, 0, c]]
def hom(x): return (1, x[0], x[1], x[2])
def prodState(x, y):
    hx, hy = hom(x), hom(y); return tuple(hx[m] * hy[n] for (m, n) in IDX)
def table_rank(w):
    M = [[sp.nsimplify(w[k(m, n)]) for n in range(4)] for m in range(4)]
    return sp.Matrix(M).rank()

# ---------------------------------------------------------------- Q0 transcription
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
check("Q0.pc/pt transcription", parse_table("pc") == PC and parse_table("pt") == PT)
CNOT = [[0] * 16 for _ in range(16)]
for (m, n) in IDX:
    CNOT[k(m, n)][k(PC[m][n], PT[m][n])] = SGN(m, n)
CNOT = tuple(tuple(r) for r in CNOT)
check("Q0.cnot involution", mat_mul(CNOT, CNOT) == I16)
z3 = (0, 0, 1); xplus = (1, 0, 0)
phiW = tuple((1 if m != 2 else -1) if m == n else 0 for (m, n) in IDX)
check("Q0.cnot pxz = phiW", mat_vec(CNOT, prodState(xplus, z3)) == phiW)
if not OK:
    print("ABORT"); sys.exit(1)

# ---------------------------------------------------------------- dictionary
I2 = sp.eye(2); X = sp.Matrix([[0, 1], [1, 0]]); Y = sp.Matrix([[0, -sp.I], [sp.I, 0]]); Z = sp.Matrix([[1, 0], [0, -1]])
PAULI = [I2, X, Y, Z]
SS = [[sp.kronecker_product(PAULI[m], PAULI[n]) for n in range(4)] for m in range(4)]
def rho_of(w):
    R = sp.zeros(4, 4)
    for (m, n) in IDX:
        if w[k(m, n)] != 0: R += sp.nsimplify(w[k(m, n)]) * SS[m][n]
    return R / 4
def w_of(R):
    return tuple(sp.nsimplify(sp.expand((R * SS[m][n]).trace())) for (m, n) in IDX)
def Ad_map(U):
    Ud = U.H; M = [[0] * 16 for _ in range(16)]
    for c, (m, n) in enumerate(IDX):
        col = w_of(U * SS[m][n] * Ud)
        for r in range(16):
            v = sp.nsimplify(col[r] / 4)
            M[r][c] = int(v) if v == int(v) else v
    return tuple(tuple(r) for r in M)
def is_pure(w):
    R = rho_of(w)
    return sp.simplify(R * R - R) == sp.zeros(4, 4) and sp.simplify(R.trace()) == 1
def psd_exact(R):
    n = R.shape[0]
    for r in range(1, n + 1):
        for S in itertools.combinations(range(n), r):
            d = sp.nsimplify(sp.expand(R.extract(list(S), list(S)).det()))
            if sp.re(d) < 0: return False
    return True

# ---------------------------------------------------------------- Q1 SWAP
SWAP = [[0] * 16 for _ in range(16)]
for (m, n) in IDX:
    SWAP[k(m, n)][k(n, m)] = 1
SWAP = tuple(tuple(r) for r in SWAP)
USW = sp.Matrix([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]])
check("Q1.SWAP = Ad(swap unitary)", Ad_map(USW) == SWAP)
def closure(gens):
    seen = {I16}; frontier = [I16]
    while frontier:
        nxt = []
        for g in frontier:
            for h in gens:
                p = mat_mul(h, g)
                if p not in seen:
                    seen.add(p); nxt.append(p)
        frontier = nxt
    return seen
GS = closure([CNOT, SWAP])
print(f"INFO order of <cnot, SWAP> on W 3 = {len(GS)}")
u = (Fr(24, 25), Fr(0), Fr(7, 25)); v = (Fr(24, 25), Fr(0), Fr(-7, 25))
cu = mat_vec(CNOT, prodState(u, v))
s_w = mat_vec(SWAP, cu)
check("Q1.s_w pure", is_pure(s_w))
r1, r2 = table_rank(s_w), table_rank(mat_vec(CNOT, s_w))
check("Q1.s_w outside K_gen (rank s_w > 1 and rank cnot s_w > 1)", r1 > 1 and r2 > 1, f"ranks {r1}, {r2}")
rc1, rc2 = table_rank(cu), table_rank(mat_vec(CNOT, cu))
control("Q1.cnot(prodState u v) outside K_gen", rc1 > 1 and rc2 > 1, f"ranks {rc1}, {rc2}")

# ---------------------------------------------------------------- Q2 monomial obstruction
amp = sp.Matrix([3, 4, 0, 5]) / sp.sqrt(50)
RHOW = amp * amp.T
psi_w = w_of(RHOW)
check("Q2.psi_w table rational", all(sp.nsimplify(t).is_rational for t in psi_w))
check("Q2.psi_w pure", is_pure(psi_w))
check("Q2.psi_w in Q3", psd_exact(rho_of(psi_w)))
pat = [sp.nsimplify(rho_of(psi_w)[i, i]) for i in range(4)]
print(f"INFO psi_w modulus pattern (|c00|^2,|c01|^2,|c10|^2,|c11|^2) = {pat}")
def any_rank1(p):
    for perm in itertools.permutations(range(4)):
        a, b, c, d = (p[perm[0]], p[perm[1]], p[perm[2]], p[perm[3]])
        if a * d - b * c == 0:
            return True
    return False
check("Q2.no arrangement of the psi_w pattern is rank one (24 permutations)", not any_rank1(pat))
prod_pat = [sp.nsimplify(rho_of(prodState((Fr(3, 5), 0, Fr(4, 5)), (0, Fr(4, 5), Fr(3, 5))))[i, i]) for i in range(4)]
control("Q2.a pure product pattern has no rank-one arrangement", not any_rank1(prod_pat))
def red_len2(w):   # squared Bloch length of the token-1 marginal
    return sp.nsimplify(w[k(1, 0)] ** 2 + w[k(2, 0)] ** 2 + w[k(3, 0)] ** 2)
cx = mat_vec(CNOT, prodState((Fr(3, 5), 0, Fr(4, 5)), z3))
check("Q2.Schmidt spectrum of psi_w = that of cnot(prodState((3/5,0,4/5), z3))",
      red_len2(psi_w) == red_len2(cx) and is_pure(cx), f"{red_len2(psi_w)} vs {red_len2(cx)}")
GSinv = list(GS)    # group: inverses are members
outside = True
for g in GSinv:
    img = mat_vec(g, psi_w)
    if table_rank(img) == 1:
        outside = False
check("Q2.psi_w outside every g(SEP), g in <cnot, SWAP> (finite rank test)", outside)

# ---------------------------------------------------------------- Q3 CtrlGate family member
c, s = Fr(3, 5), Fr(4, 5)
RZ = [[c, -s, 0], [s, c, 0], [0, 0, 1]]
RX = [[1, 0, 0], [0, c, -s], [0, s, c]]
Gt = mat_mul(CNOT, actT_map(RZ))
NFLIP = diag3(1, -1, -1)
ACn, ATn = actC_map(NFLIP), actT_map(NFLIP)
corner = {0: z3, 1: (0, 0, -1)}
frame = all(mat_vec(Gt, prodState(corner[a], corner[b])) == prodState(corner[a], corner[(a + b) % 2])
            for a in (0, 1) for b in (0, 1))
relC = mat_mul(ACn, mat_mul(Gt, ACn)) == mat_mul(ATn, Gt)
relT = mat_mul(ATn, mat_mul(Gt, ATn)) == Gt
check("Q3.G_t frame", frame)
check("Q3.G_t relC", relC)
control("Q3.G_t relT", relT)
check("Q3.cnot o G_t = actT Rz (local, acts on every table)", mat_mul(CNOT, Gt) == actT_map(RZ))
# the half-angle unitary of Rz(3/5,4/5): e^{-i t/2} with cos t = 3/5 -> e^{-i t/2} = (2 - i)/sqrt5 (irrational);
# use instead the exact Bloch-level identity above, and test monomiality at the operator level on a rational member:
# Rz with cos = -7/25, sin = 24/25 has half-angle unitary diag(a, conj a), a = (3 - 4i)/5.
aa = (3 - 4 * sp.I) / 5
UZ = sp.diag(aa, sp.conjugate(aa))
UC = sp.Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
AUZ = Ad_map(sp.kronecker_product(I2, UZ))
MZ = [[AUZ[k(0, i + 1)][k(0, j + 1)] for j in range(3)] for i in range(3)]
check("Q3.Ad(I (x) Uz) = actT M_Z", AUZ == actT_map(MZ), f"M_Z = {MZ}")
check("Q3.M_Z is a rotation about x2, not the identity",
      MZ[2] == [0, 0, 1] and MZ[0][2] == 0 and MZ[1][2] == 0 and MZ != diag3(1, 1, 1))
Gt2 = mat_mul(CNOT, actT_map(MZ))
frame2 = all(mat_vec(Gt2, prodState(corner[a], corner[b])) == prodState(corner[a], corner[(a + b) % 2])
             for a in (0, 1) for b in (0, 1))
check("Q3.G' frame and relC", frame2 and mat_mul(ACn, mat_mul(Gt2, ACn)) == mat_mul(ATn, Gt2))
control("Q3.G' relT", mat_mul(ATn, mat_mul(Gt2, ATn)) == Gt2)
Umono = UC * sp.kronecker_product(I2, UZ)
check("Q3.G' = Ad(CNOT (I (x) Uz))", Ad_map(Umono) == Gt2)
mono = all(sum(1 for i in range(4) if Umono[i, j] != 0) == 1 for j in range(4))
check("Q3.that unitary is monomial in the computational basis", mono)

# ---------------------------------------------------------------- Q4 diagonal entangling family
UZZ = sp.diag(aa, sp.conjugate(aa), sp.conjugate(aa), aa)
AZZ = Ad_map(UZZ)
comp = mat_mul(CNOT, mat_mul(AZZ, CNOT))
Mt = [[comp[k(0, i + 1)][k(0, j + 1)] for j in range(3)] for i in range(3)]
check("Q4.cnot o Ad(ZZ) o cnot = actT M (local)", comp == actT_map(Mt), f"M = {Mt}")
check("Q4.M is a rotation about x2 and not the identity",
      Mt[2] == [0, 0, 1] and Mt[0][2] == 0 and Mt[1][2] == 0 and Mt != diag3(1, 1, 1))
check("Q4.U_ZZ is diagonal (monomial)", all(UZZ[i, j] == 0 for i in range(4) for j in range(4) if i != j))

# ---------------------------------------------------------------- Q5 frame covariance words
def Cconj(R, S):
    return mat_mul(actC_map(R), mat_mul(actT_map(S), mat_mul(CNOT, mat_mul(actC_map(tr3(R)), actT_map(tr3(S))))))
def local_read(Mx, side):
    if side == "C":
        Mt_ = [[Mx[k(i + 1, 0)][k(j + 1, 0)] for j in range(3)] for i in range(3)]
        return Mt_, (Mx == actC_map(Mt_))
    Mt_ = [[Mx[k(0, i + 1)][k(0, j + 1)] for j in range(3)] for i in range(3)]
    return Mt_, (Mx == actT_map(Mt_))
ZPI = diag3(-1, -1, 1); XPI = diag3(1, -1, -1); I3 = diag3(1, 1, 1)
WA = mat_mul(CNOT, mat_mul(Cconj(RX, I3), mat_mul(Cconj(I3, ZPI), Cconj(RX, ZPI))))
MA, locA = local_read(WA, "C")
check("Q5.W_A = actC M_A at (3/5,4/5)", locA, f"M_A = {MA}")
check("Q5.M_A rotation about x0, not identity", MA[0] == [1, 0, 0] and MA != I3)
WB = mat_mul(CNOT, mat_mul(Cconj(I3, RZ), mat_mul(Cconj(XPI, I3), Cconj(XPI, RZ))))
MB, locB = local_read(WB, "T")
check("Q5.W_B = actT M_B at (3/5,4/5)", locB, f"M_B = {MB}")
check("Q5.M_B rotation about x2, not identity", MB[2] == [0, 0, 1] and MB != I3)
short = mat_mul(CNOT, Cconj(RX, I3))
_, locS = local_read(short, "C")
_, locS2 = local_read(short, "T")
control("Q5.cnot o C(Rx,I) is local", locS or locS2)
# symbolic version modulo c^2 + s^2 - 1
cs, ss = sp.symbols("c s")
def red(e):
    e = sp.expand(e)
    if e.is_number:
        return e
    return sp.expand(sp.reduced(e, [cs ** 2 + ss ** 2 - 1], ss, cs)[1])
def smat_mul(A, B):
    return tuple(tuple(red(sum(A[i][r] * B[r][j] for r in range(16) if A[i][r] != 0)) for j in range(16)) for i in range(16))
def sactC(N):
    return actC_map(N)
RXs = [[1, 0, 0], [0, cs, -ss], [0, ss, cs]]
RZs = [[cs, -ss, 0], [ss, cs, 0], [0, 0, 1]]
def sC(R, S):
    return smat_mul(actC_map(R), smat_mul(actT_map(S), smat_mul(CNOT, smat_mul(actC_map(tr3(R)), actT_map(tr3(S))))))
WAs = smat_mul(CNOT, smat_mul(sC(RXs, I3), smat_mul(sC(I3, ZPI), sC(RXs, ZPI))))
MAs = [[WAs[k(i + 1, 0)][k(j + 1, 0)] for j in range(3)] for i in range(3)]
ACs = tuple(tuple(red(x) for x in row) for row in actC_map(MAs))
check("Q5.W_A = actC M_A symbolically (mod c^2+s^2-1)", ACs == WAs, f"M_A = {MAs}")
orthA = all(red(sum(MAs[i][r] * MAs[j][r] for r in range(3)) - (1 if i == j else 0)) == 0 for i in range(3) for j in range(3))
check("Q5.M_A orthogonal symbolically", orthA)
WBs = smat_mul(CNOT, smat_mul(sC(I3, RZs), smat_mul(sC(XPI, I3), sC(XPI, RZs))))
MBs = [[WBs[k(0, i + 1)][k(0, j + 1)] for j in range(3)] for i in range(3)]
ATs = tuple(tuple(red(x) for x in row) for row in actT_map(MBs))
check("Q5.W_B = actT M_B symbolically (mod c^2+s^2-1)", ATs == WBs, f"M_B = {MBs}")

# ---------------------------------------------------------------- Q6 local agency instance (flagged)
RH = [[0, 0, 1], [0, -1, 0], [1, 0, 0]]
Tpsi = mat_vec(actT_map(RH), phiW)
check("Q6.T_psi pure", is_pure(Tpsi))
check("Q6.T_psi in Q3", psd_exact(rho_of(Tpsi)))
tr1, tr2 = table_rank(Tpsi), table_rank(mat_vec(CNOT, Tpsi))
check("Q6.T_psi outside K_gen (table ranks of T_psi and cnot T_psi > 1)", tr1 > 1 and tr2 > 1, f"{tr1}, {tr2}")

print(f"SUMMARY checks passed={NPASS} all_ok={OK}")
if OK:
    print(f"VERDICT SWAP: token exchange with cnot generates a finite group (order {len(GS)}); its cone strictly "
          "contains K_gen (exact pure witness) and excludes psi_w (exact): more than K_gen, not Q3, not IE1")
    print("VERDICT MONOMIAL-OBSTRUCTION: psi_w (pure, in Q3, Schmidt-equivalent to a cnot image of a product) has a "
          "modulus pattern with no rank-one arrangement; with the written Milman step, no construction whose operations "
          "are frame-monomial unitary conjugations (or the global transpose) generates Q3 or an IE1 cone")
    print("VERDICT CTRLGATE: the fixed-frame CtrlGate family is continuous (target pre-rotations about z3), consists "
          "of monomial gates, and generates local target rotations acting on every table; it stays in the monomial class")
    print("VERDICT FRAME-COVARIANCE: four local-rotation conjugates of cnot compose to a local rotation on either token "
          "(exact, symbolic); with all frames the local rotation group acts, i.e. IE1-type invariance")
else:
    print("NO VERDICT")
