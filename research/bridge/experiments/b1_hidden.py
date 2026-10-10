# b1_hidden.py -- research/bridge node B1: the hidden-level (H) composite and the locality-of-registers route.
# Exact arithmetic only (fractions.Fraction; sympy Rational matrices for rank / nullspace).  No floats.
#
# DECISION RULE (fixed before the first run, 2026-10-10T20:16Z by date -u; written before any execution):
#  Transcription from L (CompositeDimension.lean:97-202 W/hom/prodState/actT/actC, :741-788 sgn/pc/pt/cnot,
#  :793 z3, :797 nflip, :1213 xplus, :1220 phiW; EffectSpace.lean:57 sharpVec; KInfFoundations.lean:411-425 rot3,
#  cyc3).  pairVal(a,b,w) = sum a_m w_mn b_n (CompositeDimension.lean:164).
#  K0  (a) cnot(prodState xplus z3) == phiW = diag(1,1,-1,1) (the kernel theorem CD:1222, recomputed);
#      (b) cnot is an involution; frame: cnot(prodState(c_a, c_b)) = prodState(c_a, c_{a+b}), c_0 = z3, c_1 = -z3;
#      (c) actC N (prodState x y) = prodState (N x) y and actT N (prodState x y) = prodState x (N y) for the listed
#          N, x, y.  Pass iff all hold exactly.
#  H1  LOCALITY OF REGISTERS (L-REG), exact finite model.  Token ontic set Lam = {+x,-x,+y,-y,+z,-z} (6 points);
#      readout R_A: R^6 -> R^4, R_A delta_a = hom(v_a).  Pair: Lam x Lam (36 points), R = R_A (x) R_B (16 x 36).
#      (a) RESPECT: a permutation pi of Lam respects ker R_A iff R_A P_pi k = 0 for a basis k of ker R_A.  Enumerate
#          all 720 permutations; record the number that respect; for each, O_pi := R_A P_pi R_A^T (R_A R_A^T)^-1 and
#          check O_pi R_A = R_A P_pi exactly and O_pi = 1 (+) N_pi.  Record |{N_pi}| and whether the set is closed
#          under composition (a finite group), and membership of nflip, rot3(pi) = diag(-1,-1,1), S = R_z(pi/2), cyc3.
#      (b) IDLE EXTENSION INDUCED: for every respecting pi, R (P_pi (x) I_6) == actC(N_pi) o R and
#          R (I_6 (x) P_pi) == actT(N_pi) o R as 16 x 36 matrices.  Pass iff all equal.
#      (c) SEPARABILITY HALF-SPACE: w = E00 - E11 + E22 - E33.  <w, R delta_(a,b)> >= 0 for all 36 ontic products;
#          <w, phiW> < 0 is measured.  Written fact used ([W]): <w, prodState x y> = 1 - x.Dy, D = diag(1,-1,1),
#          >= 1 - |x||y| >= 0 on the ball.  Every hidden permutation G of Lam x Lam maps the 36 point masses onto
#          themselves, so the cone R(Delta) is G-invariant; cnot maps R delta_(+x,+z) = prodState(xplus, z3) to phiW
#          with <w, phiW> < 0, so cnot is induced by no hidden permutation of this model.  Pass iff the 36 values
#          are >= 0 and <w, phiW> < 0.
#  H2  BELL.  Settings a0 = e_x, a1 = e_z, b0 = (4/5, 0, 3/5), b1 = (4/5, 0, -3/5) (exact unit vectors).
#      P(o,o'|a,b) = pairVal(sharpVec(o a), sharpVec(o' b), w) for o, o' in {+1,-1}; E = sum o o' P;
#      S = E(a0,b0) + E(a0,b1) + E(a1,b0) - E(a1,b1).
#      (a) for phiW: every P in [0,1], each setting's four P sum to 1; S is measured.
#      (b) local bound: max and min of S over the 16 deterministic local strategies (q_a0, q_a1, r_b0, r_b1 in {+-1})
#          are measured; [W] every Bell-local model is a mixture of these, so |S| <= max.
#      (c) for each Bell-type defect z_s of K(Z_F) (T6 TEST.md §3.1), normalized by its (0,0) entry: settings
#          b0 = (4u + 3v)/5, b1 = (4u - 3v)/5 with u = T^T a0, v = T^T a1 (T the 3x3 correlation block); S measured,
#          probabilities checked in [0,1].
#      (d) membership of phiW in K(Z_F): <phiW, z_s> >= 0 for all s and M(phiW) has nonnegative principal-minor
#          sums (the dictionary M is a comparison tool only, never a premise).
#  H3  LOCAL TOMOGRAPHY SPAN: the 36 ontic products R delta_(a,b) have rank 16 in W 3 (so a linear map that agrees
#      with actC(N) on them equals actC(N)).
#  CONTROLS / COUNTERCONTROLS (each must behave as stated, else the verdict is void):
#   CC1 the transposition (+x <-> +y) of Lam does not respect ker R_A (RESPECT can fail);
#   CC2 for the product state prodState(xplus, z3) the measured |S| <= the measured local maximum;
#   CC3 the PR box (P(o,o'|a_i,b_j) = 1/2 [o o' = (-1)^(i j)]) has S = 4 > local maximum (the bound is not vacuous
#       for nonlocal tables);
#   CC4 the token swap SWAP (a nonlocal hidden permutation) is not of the form P_pi (x) I for any respecting pi.
#  VERDICT LINES are generated from the measurements:
#   "L-REG INDUCES THE IDLE EXTENSION" iff H1(a),(b) pass;
#   "L-REG HIDDEN CONE CANNOT HOST CNOT" iff H1(c) passes;
#   "L-REG EXCLUDES EVERY CANDIDATE CONE (BELL)" iff H2(a) passes and S(phiW) > the measured local maximum;
#   overall "VERDICT B1-HIDDEN-EXACT" iff K0, H1, H2, H3 and CC1-CC4 all pass; else "VERDICT NONE".
from fractions import Fraction as F
from itertools import permutations, product
import sympy as sp

RES = []
def check(name, ok, info=""):
    RES.append((name, bool(ok)))
    print(f"CHECK {name}: {'PASS' if ok else 'FAIL'} {info}")

# ---------------- kernel transcription ----------------
def hom(x): return [F(1)] + [F(v) for v in x]
def prodState(x, y):
    hx, hy = hom(x), hom(y)
    return [[hx[m] * hy[n] for n in range(4)] for m in range(4)]
def Hom(N):
    H = [[F(0)] * 4 for _ in range(4)]
    H[0][0] = F(1)
    for i in range(3):
        for j in range(3):
            H[i + 1][j + 1] = F(N[i][j])
    return H
def mm(a, b): return [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
def T_(a): return [[a[j][i] for j in range(len(a))] for i in range(len(a[0]))]
def actC(N, w): return mm(Hom(N), w)
def actT(N, w): return mm(w, T_(Hom(N)))
def SGN(m, n): return -1 if (m, n) in ((1, 3), (2, 2)) else 1
PC = [[0, 0, 3, 3], [1, 1, 2, 2], [2, 2, 1, 1], [3, 3, 0, 0]]
PT = [[0, 1, 2, 3], [1, 0, 3, 2], [1, 0, 3, 2], [0, 1, 2, 3]]
def cnot(w): return [[SGN(m, n) * w[PC[m][n]][PT[m][n]] for n in range(4)] for m in range(4)]
def pairVal(a, b, w): return sum(a[m] * w[m][n] * b[n] for m in range(4) for n in range(4))
def ip(a, b): return sum(a[i][j] * b[i][j] for i in range(4) for j in range(4))
def sharpVec(v): return [F(1, 2)] + [F(c) / 2 for c in v]
def E(m, n): return [[F(1) if (i, j) == (m, n) else F(0) for j in range(4)] for i in range(4)]
def lin(*terms):
    out = [[F(0)] * 4 for _ in range(4)]
    for c, M in terms:
        for i in range(4):
            for j in range(4):
                out[i][j] += F(c) * M[i][j]
    return out
xplus, z3 = [1, 0, 0], [0, 0, 1]
phiW = [[F(1) if i == j and i != 2 else (F(-1) if i == j == 2 else F(0)) for j in range(4)] for i in range(4)]
nflip = [[1, 0, 0], [0, -1, 0], [0, 0, -1]]
rotPi = [[-1, 0, 0], [0, -1, 0], [0, 0, 1]]
Sgate = [[0, -1, 0], [1, 0, 0], [0, 0, 1]]          # R_z(pi/2) = rot3(pi/2): (x,y,z) -> (-y, x, z)
cyc3 = [[0, 0, 1], [1, 0, 0], [0, 1, 0]]            # cyc3 v = (v2, v0, v1)
I3 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
def key3(N): return tuple(tuple(F(c) for c in r) for r in N)
def neg(v): return [-c for c in v]

# ---------------- K0 ----------------
check("K0a cnot(prodState xplus z3) == phiW", cnot(prodState(xplus, z3)) == phiW)
basis = [E(m, n) for m in range(4) for n in range(4)]
check("K0b cnot involution", all(cnot(cnot(b)) == b for b in basis))
corner = {0: z3, 1: neg(z3)}
check("K0b frame", all(cnot(prodState(corner[a], corner[b])) == prodState(corner[a], corner[(a + b) % 2])
                       for a in (0, 1) for b in (0, 1)))
samples_x = [[F(1, 3), F(-2, 3), F(2, 3)], [F(3, 5), F(0), F(4, 5)], [F(0), F(0), F(0)]]
samples_N = [nflip, Sgate, cyc3, [[F(3, 5), F(-4, 5), 0], [F(4, 5), F(3, 5), 0], [0, 0, 1]]]
ok = True
for N in samples_N:
    for x in samples_x:
        for y in samples_x:
            Nx = [sum(F(N[i][k]) * x[k] for k in range(3)) for i in range(3)]
            Ny = [sum(F(N[i][k]) * y[k] for k in range(3)) for i in range(3)]
            ok &= actC(N, prodState(x, y)) == prodState(Nx, y)
            ok &= actT(N, prodState(x, y)) == prodState(x, Ny)
check("K0c actC/actT on products", ok)

# ---------------- H1: the L-REG model ----------------
LAM = [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]]
RA = sp.Matrix(4, 6, lambda i, a: sp.Rational(hom(LAM[a])[i].numerator, hom(LAM[a])[i].denominator))
kerA = RA.nullspace()
print(f"INFO rank R_A = {RA.rank()}, dim ker R_A = {len(kerA)}")
Ginv = (RA * RA.T).inv()
def Pmat(pi):                       # pushforward of point masses: delta_a -> delta_pi(a)
    P = sp.zeros(6, 6)
    for a in range(6):
        P[pi[a], a] = 1
    return P
respecting, Ns = [], {}
for pi in permutations(range(6)):
    P = Pmat(pi)
    if all((RA * P * k).is_zero_matrix for k in kerA):
        O = RA * P * RA.T * Ginv
        good = (O * RA == RA * P) and O[0, 0] == 1 and all(O[0, j] == 0 for j in range(1, 4)) \
            and all(O[i, 0] == 0 for i in range(1, 4))
        if not good:
            check("H1a induced map of a respecting perm has form 1 (+) N", False, str(pi))
        N = [[F(int(O[i + 1, j + 1].p), int(O[i + 1, j + 1].q)) for j in range(3)] for i in range(3)]
        respecting.append((pi, N))
        Ns[key3(N)] = N
print(f"INFO respecting permutations: {len(respecting)}; distinct induced N: {len(Ns)}")
def mul3(A, B): return [[sum(F(A[i][k]) * F(B[k][j]) for k in range(3)) for j in range(3)] for i in range(3)]
closed = all(key3(mul3(A, B)) in Ns for A in Ns.values() for B in Ns.values())
members = {nm: key3(N) in Ns for nm, N in [("nflip", nflip), ("rot3(pi)", rotPi), ("S=R_z(pi/2)", Sgate),
                                           ("cyc3", cyc3)]}
check("H1a RESPECT group finite and closed", closed and len(Ns) > 0, f"|G|={len(Ns)} members={members}")
check("H1a contains nflip, rot3(pi), S, cyc3", all(members.values()))
# pair readout R = R_A (x) R_B : R^36 -> W 3 (flattened row-major 16)
pairs = [(a, b) for a in range(6) for b in range(6)]
def Rcol(a, b): return prodState(LAM[a], LAM[b])
R = sp.Matrix(16, 36, lambda r, c: sp.Rational(Rcol(*pairs[c])[r // 4][r % 4].numerator,
                                                Rcol(*pairs[c])[r // 4][r % 4].denominator))
def wmat(f):                         # 16x16 matrix of a linear map on W 3 given as a function of tables
    M = sp.zeros(16, 16)
    for c in range(16):
        out = f(basis[c])
        for r in range(16):
            M[r, c] = sp.Rational(out[r // 4][r % 4].numerator, out[r // 4][r % 4].denominator)
    return M
okb = True
for pi, N in respecting:
    PA = sp.zeros(36, 36)
    PB = sp.zeros(36, 36)
    for c, (a, b) in enumerate(pairs):
        PA[pairs.index((pi[a], b)), c] = 1
        PB[pairs.index((a, pi[b])), c] = 1
    okb &= (R * PA == wmat(lambda w: actC(N, w)) * R)
    okb &= (R * PB == wmat(lambda w: actT(N, w)) * R)
check("H1b R (P_pi (x) I) = actC(N_pi) R and R (I (x) P_pi) = actT(N_pi) R for every respecting pi", okb,
      f"({len(respecting)} perms)")
wsep = lin((1, E(0, 0)), (-1, E(1, 1)), (1, E(2, 2)), (-1, E(3, 3)))
vals = [ip(wsep, Rcol(a, b)) for (a, b) in pairs]
vphi = ip(wsep, phiW)
check("H1c separability half-space holds on the 36 ontic products, fails at phiW",
      min(vals) >= 0 and vphi < 0, f"min ontic = {min(vals)}, <w, phiW> = {vphi}")
print("RESULT L-REG HIDDEN CONE CANNOT HOST CNOT" if (min(vals) >= 0 and vphi < 0) else "RESULT (H1c not established)")
if closed and okb and all(members.values()):
    print("RESULT L-REG INDUCES THE IDLE EXTENSION")

# ---------------- H2: Bell ----------------
a0, a1 = [F(1), F(0), F(0)], [F(0), F(0), F(1)]
b0, b1 = [F(4, 5), F(0), F(3, 5)], [F(4, 5), F(0), F(-3, 5)]
def stats(w, a, b):
    P = {(o, p): pairVal(sharpVec([o * c for c in a]), sharpVec([p * c for c in b]), w) for o in (1, -1) for p in (1, -1)}
    return P
def chsh(w, A0, A1, B0, B1):
    tot, valid = F(0), True
    for (a, b, sgn) in ((A0, B0, 1), (A0, B1, 1), (A1, B0, 1), (A1, B1, -1)):
        P = stats(w, a, b)
        valid &= all(F(0) <= p <= 1 for p in P.values()) and sum(P.values()) == 1
        tot += sgn * sum(o * p * P[(o, p)] for (o, p) in P)
    return tot, valid
S_phi, val_phi = chsh(phiW, a0, a1, b0, b1)
det_vals = []
for qa0, qa1, rb0, rb1 in product((1, -1), repeat=4):
    det_vals.append(qa0 * rb0 + qa0 * rb1 + qa1 * rb0 - qa1 * rb1)
Lmax, Lmin = max(det_vals), min(det_vals)
check("H2a phiW statistics valid", val_phi, f"S(phiW) = {S_phi}")
check("H2b local deterministic bound measured", True, f"max = {Lmax}, min = {Lmin}")
def zs(s1, s2): return lin((F(1, 4), E(0, 0)), (F(s1, 4), E(1, 3)), (F(s2, 4), E(2, 2)), (F(-s1 * s2, 4), E(3, 1)))
SIGNS = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
okc = True
for s in SIGNS:
    z = zs(*s)
    zn = [[c / z[0][0] for c in r] for r in z]
    T = [[zn[i + 1][j + 1] for j in range(3)] for i in range(3)]
    u = [sum(T[i][j] * a0[i] for i in range(3)) for j in range(3)]
    v = [sum(T[i][j] * a1[i] for i in range(3)) for j in range(3)]
    B0 = [(4 * u[k] + 3 * v[k]) / 5 for k in range(3)]
    B1 = [(4 * u[k] - 3 * v[k]) / 5 for k in range(3)]
    Sz, vz = chsh(zn, a0, a1, B0, B1)
    unit = sum(c * c for c in B0) == 1 and sum(c * c for c in B1) == 1
    okc &= vz and unit and Sz > Lmax
    print(f"INFO defect z_{s}: S = {Sz}, valid = {vz}, unit settings = {unit}")
check("H2c each Bell-type defect z_s exceeds the local bound with valid statistics", okc)
pz = [ip(phiW, zs(*s)) for s in SIGNS]
# comparison tool: M(phiW) = sum w_mn sigma_m (x) sigma_n; principal-minor sums of a Hermitian matrix all >= 0
# with alternating characteristic coefficients <=> PSD.
I2 = sp.eye(2); X = sp.Matrix([[0, 1], [1, 0]]); Y = sp.Matrix([[0, -sp.I], [sp.I, 0]]); Z = sp.Matrix([[1, 0], [0, -1]])
SIG = [I2, X, Y, Z]
def Mdict(w): return sum((sp.Rational(w[m][n].numerator, w[m][n].denominator) * sp.kronecker_product(SIG[m], SIG[n])
                          for m in range(4) for n in range(4)), sp.zeros(4, 4))
lam = sp.symbols('lam')
cp = sp.Poly((Mdict(phiW) - lam * sp.eye(4)).det(), lam).all_coeffs()      # (-1)^4 lam^4 + ...
psd = all((-1) ** k * c >= 0 for k, c in enumerate(cp))
check("H2d phiW in K(Z_F): <phiW, z_s> >= 0 for all s and M(phiW) PSD (comparison)", min(pz) >= 0 and psd,
      f"pairings = {pz}")
if val_phi and S_phi > Lmax:
    print("RESULT L-REG EXCLUDES EVERY CANDIDATE CONE (BELL)")

# ---------------- H3 ----------------
check("H3 the 36 ontic products span W 3", R.rank() == 16, f"rank = {R.rank()}")

# ---------------- countercontrols ----------------
tp = [2, 1, 0, 3, 4, 5]                              # +x <-> +y
check("CC1 transposition (+x <-> +y) violates RESPECT", not all((RA * Pmat(tp) * k).is_zero_matrix for k in kerA))
S_prod, vprod = chsh(prodState(xplus, z3), a0, a1, b0, b1)
check("CC2 product state within the local bound", vprod and abs(S_prod) <= Lmax, f"S(prod) = {S_prod}")
def chsh_table(P):
    tot = F(0)
    for (i, j, sgn) in ((0, 0, 1), (0, 1, 1), (1, 0, 1), (1, 1, -1)):
        tot += sgn * sum(o * p * P[(i, j, o, p)] for o in (1, -1) for p in (1, -1))
    return tot
PR = {(i, j, o, p): (F(1, 2) if o * p == (-1) ** (i * j) else F(0)) for i in (0, 1) for j in (0, 1)
      for o in (1, -1) for p in (1, -1)}
check("CC3 PR box exceeds the local bound", chsh_table(PR) > Lmax, f"S(PR) = {chsh_table(PR)}")
SW = sp.zeros(36, 36)
for c, (a, b) in enumerate(pairs):
    SW[pairs.index((b, a)), c] = 1
is_local = False
for pi, N in respecting:
    PA = sp.zeros(36, 36)
    for c, (a, b) in enumerate(pairs):
        PA[pairs.index((pi[a], b)), c] = 1
    if PA == SW:
        is_local = True
check("CC4 SWAP of the registers is not P_pi (x) I", not is_local)

allok = all(ok for _, ok in RES)
print(f"SUMMARY {sum(ok for _, ok in RES)}/{len(RES)} checks pass")
print("VERDICT B1-HIDDEN-EXACT" if allok else "VERDICT NONE")
