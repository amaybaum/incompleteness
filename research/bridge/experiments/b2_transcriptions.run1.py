# b2_transcriptions.py -- research/bridge node B2: the embedded-observation principles at L transcribed to W 3 and
# tested against the countermodel K(Z_F) = (Q3 ∩ Z_F*) + cone Z_F by exact computation.
# Exact arithmetic only (Fraction; sympy over Q(i)).  The dictionary M(w) = sum w_mn s_m (x) s_n and Q3 are tools of
# construction and verification of the model, never premises.
#
# DECISION RULE (fixed before the first run, 2026-10-10T20:24Z by date -u):
#  Kernel transcription as in b1_hidden.py (CD:97-202, :741-797, :1220; KIF:411-425).  Z_F = {z_s},
#  z_s = (E00 + s1 E13 + s2 E22 - s1 s2 E31)/4; P_s = (I - s1 X(x)Z - s2 Y(x)Y + s1 s2 Z(x)X)/4; p_s = table(P_s)
#  (T6 TEST.md §3.1-§3.2).  "y certified in K": M(y) PSD (characteristic-coefficient test) and <y, z_t> >= 0 for all
#  t (so y ∈ Q3 ∩ Z_F* ⊆ K).  "v certified outside K": <v, y> < 0 for a certified y in K (uses only K ⊆ K*, the
#  elementary half of T6 §3.3 step 1).  "g certified in Aut(K)": g maps Z_F onto Z_F, g is orthogonal for ipW, and
#  M(g w) = V M(w) V^dag or V M(w)^T V^dag for an explicit unitary V on all 16 basis tables (then g K = K [W]).
#  Transcriptions (pair families are data, never built as tensor products of token families):
#   T-EO  (EmbeddedObservation.lean:98-124): token family A1 = affine self-maps of the ball (contains rot3 t, cyc3);
#         pair family A2 = Aut(K); (R) the token's level-1 family := A2; (L) closed under conjugation by carrier
#         isomorphisms (Aut(K), SWAP); (M) the token theory is the member at the token.  Derived discard clause
#         (closure_of_embedded, :184): x -> margA(g(prodState x y)) maps the ball into the ball for g in A2.
#         TEST E1a: the generators GEN = {cnot, SWAP, actC/actT nflip, actC/actT rot3(pi), actC D o actT D'
#         (D, D' signed diagonal, det D det D' = 1)} are certified in Aut(K).  E1b: the discard clause on the
#         listed rational points (|marg|^2 <= 1).
#   T-OR  (CompletedOI.lean:327; stage 5 zeta, drivability form): the pair slice is itself drivable.  TEST E2a: for
#         w = (3+4i)/5, U(w) = I + (w-1) P_(1,1) is unitary and Ad U(w) fixes every z_t (so it preserves K [W]);
#         E2b: N = Ad U(-1) is an involution on W 3 and moves a certified K-point; E2c: J = actC nflip is in Aut(K)
#         and off-axis: for symbolic w' on the unit circle, x_i (rank one on P_(1,1)e_0 + P_(-1,1)e_0) is fixed by
#         J N J^-1 and moved by Ad U(w') iff w' != 1; x_ii (rank one on P_(1,-1)e_0 + P_(-1,1)e_0) is moved by
#         J N J^-1 (witness for w' = 1); x_i, x_ii certified in K.
#   T-PRE (ReferenceExtension.lean:447): every available token operation O has actC O, actT O available on the pair
#         (available = K-preserving).  TEST E3a: g_tau certified in Aut(K) for g in V4 = {I, R_x(pi), R_y(pi),
#         R_z(pi)}, tau in {C, T}; E3b: for g in {S = R_z(pi/2), cyc3, cyc3^-1, R_z(th), R_x(th)} (cos th = 3/5,
#         sin th = 4/5) and tau in {C, T}: a certified y in K and an s with <g_tau z_s, y> < 0 (most negative over
#         the pool Y = {h_tau' p_u : h in {R_x(+-pi/2), R_y(+-pi/2), R_z(+-pi/2), cyc3^+-1}, tau', u}).
#   T-CS  (ImplementationLocality.lean:359, certified instance StructuralClosure.lean:261 for IsMonomial,
#         SubstratumInterface.lean:75): monomial qubit unitaries map to O(2) about z on the token; transcription =
#         (b) for R_z(phi) and R_x(pi) on each token.  TEST E4: symbolic flow law <R_z(c,s)_tau z_t, R_z(0,1)_tau p_t>
#         = -s/8 identically in (c, s), and the rational instance (3/5, 4/5) gives a negative value against a
#         certified y; dictionary check: the monomial unitaries diag(1, (3+4i)/5) and X map to R_z(th) and R_x(pi).
#   T-LFE (LiftAudit.lean:51, :112): gateFlow(sigma, t) for sigma = the NOT; levelPerm keeps the ancilla a spectator,
#         so the every-level clause transcribes to (b) for the NOT's flow on one token.  TEST E5: the Bloch image of
#         P_+ + v P_- (v = e^{i pi t}) is R_x with (cos, sin) = (Re v, Im v): at v = i it is R_x(pi/2), at v = -1
#         nflip, at v = (3+4i)/5 R_x(th); R_x(th)_tau moves K out (certified witness); level 1 alone is a single-
#         token statement (rot about x preserves the ball: checked on the listed points).
#  CONTROLS: C1 dictionary identity tr(M(a)M(b)) = 4 ipW(a,b) on all 256 basis pairs; C2 (§A.21) every pool element
#  (a rotated p_u) has M(y) PSD with trace 1 (a rotated Bell projector); C3 the symmetries nflip,
#  rot3(pi) on either token give no negative pairing with the pool; C4 Q3-control: for g in the E3b list, g_tau maps
#  each pool element to a PSD table (the modeled actions keep Q3).
#  Pre-run edits (20:31Z, before the first run): C2 wording corrected (M(p_s) has trace 1); simplify replaced by
#  expand in the dictionary checks (exact for Gaussian-rational entries; speed only).
#  VERDICT LINES (generated from the checks): "T-EO: K(Z_F) SATISFIES" iff E1a,E1b; "T-OR(drivability): K(Z_F)
#  SATISFIES" iff E2a-E2c; "T-PRE: VIOLATED BY K(Z_F) AS SOON AS ONE OF S, J, R_z(th), R_x(th) IS AVAILABLE ON A TOKEN;
#  SATISFIED WITH A1 = V4" iff E3a,E3b; "T-CS(substratum class): VIOLATED BY K(Z_F) (phase flow)" iff E4;
#  "T-LFE: EVERY-LEVEL CLAUSE VIOLATED, LEVEL 1 SATISFIED" iff E5.  Overall "VERDICT B2-TRANSCRIPTIONS-EXACT" iff all
#  checks and C1-C4 pass; else "VERDICT NONE".
from fractions import Fraction as F
from itertools import product
import sympy as sp

RES = []
def check(name, ok, info=""):
    RES.append((name, bool(ok)))
    print(f"CHECK {name}: {'PASS' if ok else 'FAIL'} {info}")

# ---------- W 3 tables (Fractions) ----------
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
def act(tau, N, w): return actC(N, w) if tau == "C" else actT(N, w)
def SGN(m, n): return -1 if (m, n) in ((1, 3), (2, 2)) else 1
PC = [[0, 0, 3, 3], [1, 1, 2, 2], [2, 2, 1, 1], [3, 3, 0, 0]]
PT = [[0, 1, 2, 3], [1, 0, 3, 2], [1, 0, 3, 2], [0, 1, 2, 3]]
def cnot(w): return [[SGN(m, n) * w[PC[m][n]][PT[m][n]] for n in range(4)] for m in range(4)]
def swap(w): return T_(w)
def ip(a, b): return sum(F(a[i][j]) * F(b[i][j]) for i in range(4) for j in range(4))
def E(m, n): return [[F(1) if (i, j) == (m, n) else F(0) for j in range(4)] for i in range(4)]
def lin(*terms):
    out = [[F(0)] * 4 for _ in range(4)]
    for c, M in terms:
        for i in range(4):
            for j in range(4):
                out[i][j] += F(c) * F(M[i][j])
    return out
key = lambda w: tuple(tuple(F(c) for c in r) for r in w)
BASIS = [E(m, n) for m in range(4) for n in range(4)]
def D3(a, b, c): return [[a, 0, 0], [0, b, 0], [0, 0, c]]
nflip, rotPi, I3 = D3(1, -1, -1), D3(-1, -1, 1), D3(1, 1, 1)
RyPi = D3(-1, 1, -1)
def Rx(c, s): return [[1, 0, 0], [0, c, -s], [0, s, c]]
def Ry(c, s): return [[c, 0, s], [0, 1, 0], [-s, 0, c]]
def Rz(c, s): return [[c, -s, 0], [s, c, 0], [0, 0, 1]]
cyc3 = [[0, 0, 1], [1, 0, 0], [0, 1, 0]]
cyc3i = T_(cyc3)
th = (F(3, 5), F(4, 5))
SIGNS = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
def zs(s1, s2): return lin((F(1, 4), E(0, 0)), (F(s1, 4), E(1, 3)), (F(s2, 4), E(2, 2)), (F(-s1 * s2, 4), E(3, 1)))
ZF = {s: zs(*s) for s in SIGNS}
ZFK = set(key(z) for z in ZF.values())

# ---------- dictionary (construction / verification tool only) ----------
I2 = sp.eye(2); X = sp.Matrix([[0, 1], [1, 0]]); Y = sp.Matrix([[0, -sp.I], [sp.I, 0]]); Z = sp.Matrix([[1, 0], [0, -1]])
SIG = [I2, X, Y, Z]
SS = [[sp.kronecker_product(SIG[m], SIG[n]) for n in range(4)] for m in range(4)]
def R_(f): return sp.Rational(f.numerator, f.denominator)
def Mdict(w): return sum((R_(F(w[m][n])) * SS[m][n] for m in range(4) for n in range(4)), sp.zeros(4, 4))
def table(Mx):
    out = []
    for m in range(4):
        row = []
        for n in range(4):
            v = sp.expand((Mx * SS[m][n]).trace() / 4)
            if not v.is_real or not v.is_Rational:
                raise ValueError(f"non-rational table entry {v}")
            row.append(F(int(v.p), int(v.q)))
        out.append(row)
    return out
lam = sp.symbols('lam')
def is_psd(Mx):
    cp = sp.Poly(sp.expand((Mx - lam * sp.eye(4)).det()), lam).all_coeffs()
    cps = [sp.simplify(c) for c in cp]
    return all(c.is_real and (-1) ** k * c >= 0 for k, c in enumerate(cps))
def certified_in_K(y):
    return is_psd(Mdict(y)) and all(ip(y, z) >= 0 for z in ZF.values())
P = {s: (sp.eye(4) - s[0] * SS[1][3] - s[1] * SS[2][2] + s[0] * s[1] * SS[3][1]) / 4 for s in SIGNS}
pS = {s: table(P[s]) for s in SIGNS}

# ---------- C1 dictionary identity ----------
ok = all(sp.expand((Mdict(a) * Mdict(b)).trace() - 4 * R_(ip(a, b))) == 0 for a in BASIS for b in BASIS)
check("C1 tr(M(a)M(b)) = 4 ipW(a,b) on 256 basis pairs", ok)
check("Z0 M(z_s) = I/2 - P_s and P_s orthogonal rank-one projectors summing to I",
      all(sp.simplify(Mdict(ZF[s]) - (sp.eye(4) / 2 - P[s])) == sp.zeros(4, 4) for s in SIGNS)
      and all(sp.simplify(P[s] * P[t] - (P[s] if s == t else sp.zeros(4, 4))) == sp.zeros(4, 4)
              for s in SIGNS for t in SIGNS)
      and sp.simplify(sum((P[s] for s in SIGNS), sp.zeros(4, 4)) - sp.eye(4)) == sp.zeros(4, 4))

# ---------- Aut(K) certification ----------
def is_orth(f):
    M = [[ip(f(BASIS[c]), BASIS[r]) for c in range(16)] for r in range(16)]
    return all(sum(M[k][i] * M[k][j] for k in range(16)) == (1 if i == j else 0) for i in range(16) for j in range(16))
def implements(f, V, transpose=False):
    for b in BASIS:
        lhs = Mdict(f(b))
        mb = Mdict(b)
        rhs = V * (mb.T if transpose else mb) * V.H
        if not sp.expand(lhs - rhs).is_zero_matrix:
            return False
    return True
def certify_aut(f, V, transpose=False):
    perm = set(key(f(z)) for z in ZF.values()) == ZFK
    return perm and is_orth(f) and implements(f, V, transpose)
CNOTU = sp.Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
SWAPU = sp.Matrix([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]])
PAULI_OF = {key(Hom(I3)): I2, key(Hom(nflip)): X, key(Hom(RyPi)): Y, key(Hom(rotPi)): Z}
gens = [("cnot", cnot, CNOTU, False), ("SWAP", swap, SWAPU, False),
        ("actC nflip", lambda w: actC(nflip, w), sp.kronecker_product(X, I2), False),
        ("actT nflip", lambda w: actT(nflip, w), sp.kronecker_product(I2, X), False),
        ("actC rot3pi", lambda w: actC(rotPi, w), sp.kronecker_product(Z, I2), False),
        ("actT rot3pi", lambda w: actT(rotPi, w), sp.kronecker_product(I2, Z), False)]
# signed diagonals: det +1 are Pauli conjugations; det -1 = Pauli conjugation composed with complex conjugation
# (= transpose for Hermitian M) on that side; pairs with det product 1 are implemented globally.
diag_ok = True
for d in product((1, -1), repeat=3):
    for e in product((1, -1), repeat=3):
        dd, de = d[0] * d[1] * d[2], e[0] * e[1] * e[2]
        if dd * de != 1:
            continue
        D, Dp = D3(*d), D3(*e)
        f = (lambda D, Dp: (lambda w: actC(D, actT(Dp, w))))(D, Dp)
        if dd == 1:
            V = sp.kronecker_product(PAULI_OF[key(Hom(D))], PAULI_OF[key(Hom(Dp))])
            diag_ok &= certify_aut(f, V, False)
        else:   # D = -(det+1 element): D = Dplus * reflY-type; implement as V M^T V^dag with V built from -D
            Dm, Dpm = D3(*[-c for c in d]), D3(*[-c for c in e])     # det +1 partners
            # complex conjugation on both sides = transpose; it maps sigma_y -> -sigma_y on each side, i.e. acts as
            # diag(1,-1,1) = reflY on each token; D = reflY * (Pauli rotation) on each side.
            refl = D3(1, -1, 1)
            A = [[sum(D[i][k] * refl[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
            Ap = [[sum(Dp[i][k] * refl[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
            V = sp.kronecker_product(PAULI_OF[key(Hom(A))], PAULI_OF[key(Hom(Ap))])
            diag_ok &= certify_aut(f, V, True)
gen_ok = all(certify_aut(f, V, t) for (_, f, V, t) in gens)
check("E1a generators cnot, SWAP, actC/actT nflip, actC/actT rot3(pi) certified in Aut(K)", gen_ok)
check("E1a signed-diagonal pairs (det D det D' = 1) certified in Aut(K)", diag_ok, "(32 maps)")

# ---------- E1b discard clause ----------
pts = [[F(0), F(0), F(0)], [F(1), F(0), F(0)], [F(0), F(0), F(-1)], [F(3, 5), F(4, 5), F(0)],
       [F(1, 3), F(2, 3), F(-2, 3)], [F(1, 2), F(-1, 2), F(1, 2)]]
def margA(w): return [w[i][0] / w[0][0] for i in range(1, 4)]
okd = True
for (_, f, _, _) in gens:
    for x in pts:
        for y in pts:
            mA = margA(f(prodState(x, y)))
            okd &= sum(c * c for c in mA) <= 1
check("E1b discard: margA(g(prodState x y)) in the ball for every generator and listed point", okd)
if gen_ok and diag_ok and okd:
    print("RESULT T-EO: K(Z_F) SATISFIES (with rot3 t and cyc3 available on the token; A2 = Aut(K))")

# ---------- E2 observer recursion, drivability form ----------
def Ad(U, w): return table(U * Mdict(w) * U.H)
wq = sp.Rational(3, 5) + sp.Rational(4, 5) * sp.I
U = sp.eye(4) + (wq - 1) * P[(1, 1)]
unit = sp.simplify(U * U.H - sp.eye(4)) == sp.zeros(4, 4)
fixes = all(Ad(U, ZF[s]) == ZF[s] for s in SIGNS)
check("E2a U(w) unitary, Ad U(w) fixes every defect", unit and fixes)
Um = sp.eye(4) - 2 * P[(1, 1)]
e0 = sp.Matrix([1, 0, 0, 0])
def rank1(v): return table(v * v.H)
phi1 = P[(1, 1)] * e0 + P[(1, -1)] * e0
x1 = rank1(phi1)
invol = all(Ad(Um, Ad(Um, b)) == b for b in BASIS)
moves = Ad(Um, x1) != x1
check("E2b N = Ad U(-1) involution; moves a certified K-point", invol and moves and certified_in_K(x1))
J = lambda w: actC(nflip, w)
phi_i = P[(1, 1)] * e0 + P[(-1, 1)] * e0
phi_ii = P[(1, -1)] * e0 + P[(-1, 1)] * e0
xi, xii = rank1(phi_i), rank1(phi_ii)
JNJ = lambda w: J(Ad(Um, J(w)))
wp = sp.symbols('wp')                                    # w' on the unit circle: conj(w') = 1/w'
Uwp = sp.eye(4) + (wp - 1) * P[(1, 1)]
Uwp_H = sp.eye(4) + (1 / wp - 1) * P[(1, 1)]
Mxi = Mdict(xi)
diff = sp.simplify(Uwp * Mxi * Uwp_H - Mxi)
sol = sp.solve([sp.numer(sp.together(e)) for e in diff if sp.simplify(e) != 0], wp, dict=True)
off_i = (JNJ(xi) == xi) and sol == [{wp: 1}]
off_ii = JNJ(xii) != xii
check("E2c J = actC nflip off-axis: x_i fixed by J N J^-1, moved by Ad U(w') iff w' = 1 fails; x_ii moved",
      off_i and off_ii and certified_in_K(xi) and certified_in_K(xii), f"solutions of Ad U(w') x_i = x_i: {sol}")
if unit and fixes and invol and moves and off_i and off_ii:
    print("RESULT T-OR(drivability): K(Z_F) SATISFIES (pair-level flow Ad U(w), NOT Ad U(-1), J = actC nflip)")

# ---------- E3 OI+-1 / parallel reference extension ----------
okV4 = True
for g in (I3, nflip, RyPi, rotPi):
    for tau in "CT":
        V = sp.kronecker_product(PAULI_OF[key(Hom(g))], I2) if tau == "C" else \
            sp.kronecker_product(I2, PAULI_OF[key(Hom(g))])
        okV4 &= certify_aut(lambda w, g=g, tau=tau: act(tau, g, w), V, False)
check("E3a V4 = {I, R_x(pi), R_y(pi), R_z(pi)} on either token certified in Aut(K)", okV4)
H_list = [("Rx(pi/2)", Rx(0, 1)), ("Rx(-pi/2)", Rx(0, -1)), ("Ry(pi/2)", Ry(0, 1)), ("Ry(-pi/2)", Ry(0, -1)),
          ("Rz(pi/2)", Rz(0, 1)), ("Rz(-pi/2)", Rz(0, -1)), ("cyc3", cyc3), ("cyc3^-1", cyc3i)]
POOL = []
for (hn, h) in H_list:
    for tau in "CT":
        for s in SIGNS:
            POOL.append((f"{hn}_{tau} p_{s}", act(tau, h, pS[s])))
pool_cert = [(nm, y) for (nm, y) in POOL if certified_in_K(y)]
print(f"INFO pool: {len(POOL)} elements, {len(pool_cert)} certified in K")
E3B = [("S=R_z(pi/2)", Rz(0, 1)), ("cyc3", cyc3), ("cyc3^-1", cyc3i), ("R_z(th)", Rz(*th)), ("R_x(th)", Rx(*th))]
okb = True
for (gn, g) in E3B:
    for tau in "CT":
        best = None
        for s in SIGNS:
            v = act(tau, g, ZF[s])
            for (nm, y) in pool_cert:
                val = ip(v, y)
                if best is None or val < best[0]:
                    best = (val, s, nm)
        okb &= best[0] < 0
        print(f"INFO witness {gn}_{tau}: min <g z_s, y> = {best[0]} at s = {best[1]}, y = {best[2]}")
check("E3b S, cyc3^{+-1}, R_z(th), R_x(th) on either token move K out (certified witnesses)", okb and len(pool_cert) > 0)
if okV4 and okb:
    print("RESULT T-PRE: VIOLATED BY K(Z_F) AS SOON AS ONE OF S, J, R_z(th), R_x(th) IS AVAILABLE ON A TOKEN; "
          "SATISFIED WITH A1 = V4")

# ---------- E4 ContextStable, substratum (monomial) class ----------
c, s_ = sp.symbols('c s')
def act_sym(tau, N, w):                       # symbolic actC/actT on sympy tables
    H = sp.zeros(4, 4); H[0, 0] = 1
    for i in range(3):
        for j in range(3):
            H[i + 1, j + 1] = N[i][j]
    Wm = sp.Matrix(4, 4, lambda i, j: R_(F(w[i][j])))
    return H * Wm if tau == "C" else Wm * H.T
def ip_sym(A, Bt): return sp.expand(sum(A[i, j] * R_(F(Bt[i][j])) for i in range(4) for j in range(4)))
flow_ok = True
for tau in "CT":
    for sg in SIGNS:
        lhs = act_sym(tau, [[c, -s_, 0], [s_, c, 0], [0, 0, 1]], ZF[sg])
        y = act(tau, Rz(0, 1), pS[sg])
        flow_ok &= sp.simplify(ip_sym(lhs, y) + s_ / 8) == 0 and certified_in_K(y)
def bloch(Um_):
    return [[sp.simplify((SIG[i + 1] * Um_ * SIG[j + 1] * Um_.H).trace() / 2) for j in range(3)] for i in range(3)]
dict_ok = bloch(sp.diag(1, wq)) == [[sp.Rational(3, 5), -sp.Rational(4, 5), 0], [sp.Rational(4, 5), sp.Rational(3, 5), 0],
                                     [0, 0, 1]] and bloch(X) == [[1, 0, 0], [0, -1, 0], [0, 0, -1]]
inst = min(ip(actC(Rz(*th), ZF[sg]), act("C", Rz(0, 1), pS[sg])) for sg in SIGNS)
check("E4 monomial dictionary: diag(1,(3+4i)/5) -> R_z(th), X -> R_x(pi) = nflip", dict_ok)
check("E4 symbolic flow law <R_z(c,s)_tau z_t, R_z(pi/2)_tau p_t> = -s/8 with certified witness", flow_ok)
check("E4 rational instance (3/5, 4/5) negative", inst < 0, f"value = {inst}")
if dict_ok and flow_ok and inst < 0:
    print("RESULT T-CS(substratum class): VIOLATED BY K(Z_F) (continuous phase flow about z)")

# ---------- E5 LayerFlowExecutable ----------
Pp, Pm = (I2 + X) / 2, (I2 - X) / 2
def gflow(v): return Pp + v * Pm
b_i = bloch(gflow(sp.I)); b_m1 = bloch(gflow(-1)); b_th = bloch(gflow(wq))
lfe_dict = (b_i == [[1, 0, 0], [0, 0, -1], [0, 1, 0]] and b_m1 == [[1, 0, 0], [0, -1, 0], [0, 0, -1]]
            and b_th == [[1, 0, 0], [0, sp.Rational(3, 5), -sp.Rational(4, 5)], [0, sp.Rational(4, 5), sp.Rational(3, 5)]])
wit = min(ip(actC(Rx(*th), ZF[sg]), y) for sg in SIGNS for (_, y) in pool_cert)
lvl1 = all(sum(sum(F(Rx(*th)[i][k]) * x[k] for k in range(3)) ** 2 for i in range(3)) == sum(v * v for v in x) for x in pts)
check("E5 gateFlow of the NOT is R_x(pi t): v = i -> R_x(pi/2), v = -1 -> nflip, v = (3+4i)/5 -> R_x(th)", lfe_dict)
check("E5 every-level clause = (b) for R_x(th): violated (certified witness); level 1 preserves the ball", wit < 0 and lvl1,
      f"witness = {wit}")
if lfe_dict and wit < 0 and lvl1:
    print("RESULT T-LFE: EVERY-LEVEL CLAUSE VIOLATED BY K(Z_F), LEVEL 1 SATISFIED")

# ---------- controls ----------
okC2 = all(is_psd(Mdict(y)) and Mdict(y).trace() == 1 for (_, y) in POOL)
check("C2 every pool element is PSD with trace 1 (rotated Bell projectors; Q3 kept)", okC2)
okC3 = True
for g in (nflip, rotPi):
    for tau in "CT":
        for s in SIGNS:
            okC3 &= all(ip(act(tau, g, ZF[s]), y) >= 0 for (_, y) in pool_cert)
check("C3 symmetries nflip, rot3(pi) give no negative pairing over the certified pool", okC3)
okC4 = all(is_psd(Mdict(act(tau, g, y))) for (_, g) in E3B for tau in "CT" for (_, y) in pool_cert[:8])
check("C4 the modeled local actions keep Q3 on certified pool elements", okC4)

allok = all(o for _, o in RES)
print(f"SUMMARY {sum(o for _, o in RES)}/{len(RES)} checks pass")
print("VERDICT B2-TRANSCRIPTIONS-EXACT" if allok else "VERDICT NONE")
