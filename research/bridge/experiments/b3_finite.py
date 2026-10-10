# b3_finite.py -- research/bridge node B3: finite versus continuous.  What a fixed finite substratum (and a directed
# tower of finite substrata) can realize as readout-respecting hidden permutations, on one token and on the pair with
# the native gate; the exact reduction of A_miss.  Exact arithmetic only (Fraction, sympy Rational).
#
# DECISION RULE (fixed before the first run, about 2026-10-10T20:31Z; run 1 header misstated it as 20:44Z, which
# was later than the run itself (20:32:58Z); corrected after run 1, rule text unchanged):
#  Transcription as in b1/b2 (CD:97-202, :741-797; KIF:411-425).  R1 := the order-3 rotation about (5,1,1) of the
#  stage-4 record (Y7; INTEGRATION-NOTE-STAGE4.md:42), written exactly as (1/9)[[8,1,4],[4,-4,-7],[1,8,-4]]
#  (Rodrigues with cos = -1/2, sin = sqrt3/2, n = (5,1,1)/sqrt27; every sqrt cancels).
#  X1 HOMOMORPHISM: on the octahedral ontic token (b1 model), the induced maps of readout-respecting permutations
#     satisfy O_(pi o sig) = O_pi O_sig for all 48 x 48 pairs (so a finite substratum yields a finite token group).
#  X2 NATIVE FRAME GROUP WITH THE GATE: the group generated on W 3 by cnot, actC S, actT S, actC cyc3, actT cyc3
#     (S = R_z(pi/2)), all signed permutations of the 16 entries, is enumerated by closure; its order is measured.
#     Pass iff the enumeration closes (finite) below the cap 10^6.
#  X3 R1: orthogonal, det 1, R1^3 = I, fixes (5,1,1), not a signed permutation (off the native frame).  Ontic token
#     Lam_R1 = <R1>.{+-e_i}: its size is measured; every point is a unit vector; R1 permutes Lam_R1; R_A P_R1 =
#     Hom(R1) R_A exactly (readout-respecting, induced map R1); rank R_A = 4.
#  X4 <cnot, actC R1> HAS AN ELEMENT OF INFINITE ORDER: search the words of length <= 6 in {cnot, actC R1, actC R1^2}
#     for a rational trace that is not an integer ([W]: a finite-order real matrix has an algebraic-integer trace; a
#     rational algebraic integer is an integer).  Pass iff one is found (the first is printed).
#  X5 A_MISS AS TWO RATIONAL MATRICES: tr R_z(th) = 11/5 is not an integer (cos th = 3/5: infinite order), likewise
#     tr R_x(th); K(Z_F) is moved out by actC R_z(th) (witness < 0) and by actC S (witness < 0), each against a
#     certified y in Q3 ∩ Z_F*.
#  X6 TOWERS (identity component): A_n := actC([n]x) (the generator of the local circle about n on the control),
#     B_n := cnot A_n cnot; the commutator [A_n, B_n] is measured for n = e_x, e_z (frame) and n = (3/5, 0, 4/5)
#     (off-frame); and the same with actT on the target.  Pass iff the frame brackets vanish and the off-frame
#     brackets do not.
#  X7 (exploratory, not required for the verdict) a certified witness that actC R1 moves K(Z_F) out, searched in the
#     pool {act_tau(h) p_u} over h in the rational rotations listed in the script and their pairwise products;
#     printed if found, else "R1 witness not found in pool".
#  CONTROLS: C1 integer traces for the finite-order elements cnot, actC S, actC cyc3, actC R1 (the trace test does not
#  fire on finite-order elements); C2 the Q3-control of the witnesses (M(y) PSD for the selected y); C3 the identity
#  map is in the X2 enumeration and every enumerated element fixes the (0,0) entry.
#  VERDICT LINES: "FIXED FINITE SUBSTRATUM: REALIZED GROUPS ARE FINITE" iff X1 and X2; "R1 IS H-SOURCEABLE ON ONE TOKEN,
#  NOT TOGETHER WITH CNOT ON ANY FINITE PAIR SUBSTRATUM" iff X3 and X4; "A_MISS IS (b) FOR TWO RATIONAL MATRICES;
#  EACH ALONE EXCLUDES K(Z_F)" iff X5; "TOWERS: CNOT WITH AN OFF-FRAME LOCAL CIRCLE GENERATES A NONABELIAN IDENTITY
#  COMPONENT; FRAME AXES COMMUTE" iff X6.  Overall "VERDICT B3-FINITE-EXACT" iff X1-X6 and C1-C3 pass; else
#  "VERDICT NONE".
from fractions import Fraction as F
from itertools import permutations, product
import sympy as sp

RES = []
def check(name, ok, info=""):
    RES.append((name, bool(ok)))
    print(f"CHECK {name}: {'PASS' if ok else 'FAIL'} {info}")

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
def mm(a, b): return [[sum(F(a[i][k]) * F(b[k][j]) for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
def T_(a): return [[a[j][i] for j in range(len(a))] for i in range(len(a[0]))]
def actC(N, w): return mm(Hom(N), w)
def actT(N, w): return mm(w, T_(Hom(N)))
def act(tau, N, w): return actC(N, w) if tau == "C" else actT(N, w)
def SGN(m, n): return -1 if (m, n) in ((1, 3), (2, 2)) else 1
PC = [[0, 0, 3, 3], [1, 1, 2, 2], [2, 2, 1, 1], [3, 3, 0, 0]]
PT = [[0, 1, 2, 3], [1, 0, 3, 2], [1, 0, 3, 2], [0, 1, 2, 3]]
def cnot(w): return [[SGN(m, n) * F(w[PC[m][n]][PT[m][n]]) for n in range(4)] for m in range(4)]
def ip(a, b): return sum(F(a[i][j]) * F(b[i][j]) for i in range(4) for j in range(4))
def E(m, n): return [[F(1) if (i, j) == (m, n) else F(0) for j in range(4)] for i in range(4)]
BASIS = [E(m, n) for m in range(4) for n in range(4)]
def lin(*terms):
    out = [[F(0)] * 4 for _ in range(4)]
    for c, M in terms:
        for i in range(4):
            for j in range(4):
                out[i][j] += F(c) * F(M[i][j])
    return out
def mat16(f):                                   # 16x16 Fraction matrix of a linear map on W 3 (row-major flatten)
    cols = [f(b) for b in BASIS]
    return [[cols[c][r // 4][r % 4] for c in range(16)] for r in range(16)]
def mul16(A, B): return [[sum(A[i][k] * B[k][j] for k in range(16)) for j in range(16)] for i in range(16)]
def tr16(A): return sum(A[i][i] for i in range(16))
def mul3(A, B): return [[sum(F(A[i][k]) * F(B[k][j]) for k in range(3)) for j in range(3)] for i in range(3)]
def vec3(N, v): return [sum(F(N[i][k]) * F(v[k]) for k in range(3)) for i in range(3)]
I3 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
Sg = [[0, -1, 0], [1, 0, 0], [0, 0, 1]]
cyc3 = [[0, 0, 1], [1, 0, 0], [0, 1, 0]]
def Rx(c, s): return [[1, 0, 0], [0, c, -s], [0, s, c]]
def Ry(c, s): return [[c, 0, s], [0, 1, 0], [-s, 0, c]]
def Rz(c, s): return [[c, -s, 0], [s, c, 0], [0, 0, 1]]
th = (F(3, 5), F(4, 5))
R1 = [[F(8, 9), F(1, 9), F(4, 9)], [F(4, 9), F(-4, 9), F(-7, 9)], [F(1, 9), F(8, 9), F(-4, 9)]]
SIGNS = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
def zs(s1, s2): return lin((F(1, 4), E(0, 0)), (F(s1, 4), E(1, 3)), (F(s2, 4), E(2, 2)), (F(-s1 * s2, 4), E(3, 1)))
ZF = {s: zs(*s) for s in SIGNS}
def ps(s1, s2): return lin((F(1, 4), E(0, 0)), (F(-s1, 4), E(1, 3)), (F(-s2, 4), E(2, 2)), (F(s1 * s2, 4), E(3, 1)))
PS = {s: ps(*s) for s in SIGNS}

# ---------------- X1 ----------------
LAM = [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]]
idx = {tuple(F(c) for c in v): i for i, v in enumerate(LAM)}
RA = sp.Matrix(4, 6, lambda i, a: int(hom(LAM[a])[i]))
kerA = RA.nullspace()
def Pmat(pi):
    P = sp.zeros(6, 6)
    for a in range(6):
        P[pi[a], a] = 1
    return P
Ginv = (RA * RA.T).inv()
induced = {}
for pi in permutations(range(6)):
    P = Pmat(pi)
    if all((RA * P * k).is_zero_matrix for k in kerA):
        O = RA * P * RA.T * Ginv
        induced[pi] = O
hom_ok = all(induced[tuple(p[q[a]] for a in range(6))] == induced[p] * induced[q]
             for p in induced for q in induced)
check("X1 O_(pi o sig) = O_pi O_sig on all respecting pairs", hom_ok and len(induced) == 48, f"(|G| = {len(induced)})")

# ---------------- X2 ----------------
def sperm(f):                                    # a signed permutation of the 16 entries as (perm, signs)
    perm, sgn = [], []
    for c in range(16):
        out = f(BASIS[c])
        nz = [(r, out[r // 4][r % 4]) for r in range(16) if out[r // 4][r % 4] != 0]
        if len(nz) != 1 or abs(nz[0][1]) != 1:
            return None
        perm.append(nz[0][0]); sgn.append(int(nz[0][1]))
    return (tuple(perm), tuple(sgn))
def compose(g, h):                               # (g o h): column c -> h then g
    pg, sg = g; ph, sh = h
    return (tuple(pg[ph[c]] for c in range(16)), tuple(sh[c] * sg[ph[c]] for c in range(16)))
gens2 = [sperm(cnot), sperm(lambda w: actC(Sg, w)), sperm(lambda w: actT(Sg, w)),
         sperm(lambda w: actC(cyc3, w)), sperm(lambda w: actT(cyc3, w))]
ident = (tuple(range(16)), tuple([1] * 16))
seen, frontier, CAP = {ident}, [ident], 10 ** 6
while frontier and len(seen) < CAP:
    new = []
    for g in frontier:
        for h in gens2:
            k = compose(h, g)
            if k not in seen:
                seen.add(k); new.append(k)
    frontier = new
finite2 = (not frontier) and all(g is not None for g in gens2)
fix00 = all(p[0] == 0 and s[0] == 1 for (p, s) in seen)
check("X2 <cnot, actC/actT S, actC/actT cyc3> is finite", finite2, f"order = {len(seen)}")
check("C3 identity enumerated; every element fixes the (0,0) entry", ident in seen and fix00)

# ---------------- X3 ----------------
R1R1t = mul3(R1, T_(R1))
R1c = mul3(R1, mul3(R1, R1))
detR1 = sp.Matrix(3, 3, lambda i, j: sp.Rational(R1[i][j].numerator, R1[i][j].denominator)).det()
fix = vec3(R1, [5, 1, 1]) == [F(5), F(1), F(1)]
signedperm = all(sum(1 for c in r if c != 0) == 1 and all(c in (0, 1, -1) for c in r) for r in R1)
x3a = R1R1t == [[F(int(i == j)) for j in range(3)] for i in range(3)] and R1c == R1R1t and detR1 == 1 and fix \
    and not signedperm
orbit = []
for v in LAM:
    w = [F(c) for c in v]
    for _ in range(3):
        if w not in orbit:
            orbit.append(w)
        w = vec3(R1, w)
unitv = all(sum(c * c for c in v) == 1 for v in orbit)
perm_ok = all(vec3(R1, v) in orbit for v in orbit)
RAR = sp.Matrix(4, len(orbit), lambda i, a: sp.Rational(hom(orbit[a])[i].numerator, hom(orbit[a])[i].denominator))
PR = sp.zeros(len(orbit), len(orbit))
for a, v in enumerate(orbit):
    PR[orbit.index(vec3(R1, v)), a] = 1
HR = sp.Matrix(4, 4, lambda i, j: sp.Rational(Hom(R1)[i][j].numerator, Hom(R1)[i][j].denominator))
x3b = unitv and perm_ok and (RAR * PR == HR * RAR) and RAR.rank() == 4
check("X3 R1 exact rotation of order 3 about (5,1,1), off the frame", x3a)
check("X3 R1 realized as a readout-respecting permutation of a finite ontic token", x3b, f"|Lam_R1| = {len(orbit)}")

# ---------------- X4 ----------------
MC = mat16(cnot)
MR = mat16(lambda w: actC(R1, w))
MR2 = mul16(MR, MR)
letters = {"cnot": MC, "R1": MR, "R1^2": MR2}
found = None
def words(n):
    if n == 0:
        yield []
        return
    for w in words(n - 1):
        for l in letters:
            if w and ((w[-1] == "cnot") == (l == "cnot")):
                continue                          # alternate gate / local letters
            yield w + [l]
for L in range(1, 7):
    for w in words(L):
        M = letters[w[0]]
        for l in w[1:]:
            M = mul16(M, letters[l])
        t = tr16(M)
        if t.denominator != 1:
            found = (w, t)
            break
    if found:
        break
check("X4 <cnot, actC R1> contains an element with non-integer rational trace (infinite order)", found is not None,
      f"word = {found[0] if found else None}, trace = {found[1] if found else None}")
c1 = all(tr16(mat16(f)).denominator == 1 for f in (cnot, lambda w: actC(Sg, w), lambda w: actC(cyc3, w),
                                                    lambda w: actC(R1, w)))
check("C1 integer traces for the finite-order elements cnot, actC S, actC cyc3, actC R1", c1)

# ---------------- X5 ----------------
trz = sum(F(Rz(*th)[i][i]) for i in range(3)); trx = sum(F(Rx(*th)[i][i]) for i in range(3))
I2 = sp.eye(2); X = sp.Matrix([[0, 1], [1, 0]]); Y = sp.Matrix([[0, -sp.I], [sp.I, 0]]); Z = sp.Matrix([[1, 0], [0, -1]])
SIG = [I2, X, Y, Z]
SS = [[sp.kronecker_product(SIG[m], SIG[n]) for n in range(4)] for m in range(4)]
lam = sp.symbols('lam')
def Mdict(w): return sum((sp.Rational(F(w[m][n]).numerator, F(w[m][n]).denominator) * SS[m][n]
                          for m in range(4) for n in range(4)), sp.zeros(4, 4))
def is_psd(Mx):
    cp = sp.Poly(sp.expand((Mx - lam * sp.eye(4)).det()), lam).all_coeffs()
    return all(sp.re(c) == c and (-1) ** k * c >= 0 for k, c in enumerate(cp))
def zstar(y): return all(ip(y, z) >= 0 for z in ZF.values())
yS = act("C", Rx(0, 1), PS[(1, 1)])
vS = min(ip(actC(Sg, ZF[s]), y) for s in SIGNS for y in [act(t, h, PS[u]) for t in "CT" for h in (Rx(0, 1), Rz(0, 1))
                                                          for u in SIGNS] if zstar(y))
vZ = min(ip(actC(Rz(*th), ZF[s]), y) for s in SIGNS for y in [act(t, h, PS[u]) for t in "CT" for h in (Rx(0, 1), Rz(0, 1))
                                                               for u in SIGNS] if zstar(y))
cert = all(is_psd(Mdict(act(t, h, PS[u]))) for t in "CT" for h in (Rx(0, 1), Rz(0, 1)) for u in SIGNS)
check("X5 tr R_z(th) = 11/5 and tr R_x(th) non-integer (infinite order)", trz == F(11, 5) and trx.denominator != 1,
      f"tr = {trz}, {trx}")
check("X5 K(Z_F) moved out by actC S and by actC R_z(th) (certified witnesses)", vS < 0 and vZ < 0 and cert,
      f"S: {vS}, R_z(th): {vZ}")
check("C2 witnesses are PSD (Q3-control)", cert)

# ---------------- X6 ----------------
def cross(n): return [[0, -n[2], n[1]], [n[2], 0, -n[0]], [-n[1], n[0], 0]]
def Gen(tau, n):
    G = [[F(0)] * 4 for _ in range(4)]
    for i in range(3):
        for j in range(3):
            G[i + 1][j + 1] = F(cross(n)[i][j])
    return mat16(lambda w: mm(G, w) if tau == "C" else mm(w, T_(G)))
def bracket_zero(tau, n):
    A = Gen(tau, n)
    B = mul16(MC, mul16(A, MC))
    C = [[x - y for x, y in zip(r1, r2)] for r1, r2 in zip(mul16(A, B), mul16(B, A))]
    return all(c == 0 for r in C for c in r)
fr = [("C", [1, 0, 0]), ("C", [0, 0, 1]), ("T", [1, 0, 0]), ("T", [0, 0, 1])]
of = [("C", [F(3, 5), 0, F(4, 5)]), ("T", [F(3, 5), 0, F(4, 5)])]
fz = {f"{t}{n}": bracket_zero(t, n) for t, n in fr}
oz = {f"{t}{[str(c) for c in n]}": bracket_zero(t, n) for t, n in of}
check("X6 frame-axis circles commute with their cnot-conjugates; off-frame circles do not",
      all(fz.values()) and not any(oz.values()), f"frame zero: {fz}; off-frame zero: {oz}")

# ---------------- X7 (exploratory) ----------------
rots = [I3, Rx(0, 1), Rx(0, -1), Ry(0, 1), Ry(0, -1), Rz(0, 1), Rz(0, -1), cyc3, T_(cyc3), R1, T_(R1),
        Rx(*th), Rx(th[0], -th[1]), Ry(*th), Ry(th[0], -th[1]), Rz(*th), Rz(th[0], -th[1])]
rot2 = {}
for a in rots:
    for b in rots:
        m = mul3(a, b)
        rot2[tuple(tuple(r) for r in m)] = m
best = None
for m in rot2.values():
    for t in "CT":
        for u in SIGNS:
            y = act(t, m, PS[u])
            if not zstar(y):
                continue
            for s in SIGNS:
                v = ip(actC(R1, ZF[s]), y)
                if best is None or v < best[0]:
                    best = (v, t, u, s, m)
if best is not None and best[0] < 0 and is_psd(Mdict(act(best[1], best[4], PS[best[2]]))):
    print(f"RESULT K(Z_F) MOVED OUT BY actC R1 (certified witness, value {best[0]})")
else:
    print(f"INFO R1 witness not found in pool (min = {best[0] if best else None}); stage-4/R6 record: -2383/5316 [A]")

# ---------------- verdict lines ----------------
ok = dict(RES)
def allp(*names): return all(ok[n] for n in names)
if hom_ok and finite2:
    print("RESULT FIXED FINITE SUBSTRATUM: REALIZED GROUPS ARE FINITE")
if x3a and x3b and found is not None:
    print("RESULT R1 IS H-SOURCEABLE ON ONE TOKEN, NOT TOGETHER WITH CNOT ON ANY FINITE PAIR SUBSTRATUM")
if trz == F(11, 5) and vS < 0 and vZ < 0 and cert:
    print("RESULT A_MISS IS (b) FOR TWO RATIONAL MATRICES; EACH ALONE EXCLUDES K(Z_F)")
if all(fz.values()) and not any(oz.values()):
    print("RESULT TOWERS: CNOT WITH AN OFF-FRAME LOCAL CIRCLE GENERATES A NONABELIAN IDENTITY COMPONENT; FRAME AXES COMMUTE")
allok = all(o for _, o in RES)
print(f"SUMMARY {sum(o for _, o in RES)}/{len(RES)} checks pass")
print("VERDICT B3-FINITE-EXACT" if allok else "VERDICT NONE")
