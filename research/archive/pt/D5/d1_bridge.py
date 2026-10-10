# d1_bridge.py -- thread D5 (BRIDGE-DERIVE), stage 5.  Exact arithmetic only (sympy Rational / I).
# Run: python3 -I -B d1_bridge.py  from pt/D5/ ; argv: none.  Reads (read-only) two Lean files at L.
#
# DECISION RULES (fixed before the first run; rules, not expected numbers):
#  Every check prints "PASS <id>" or "FAIL <id>"; countercontrols (ids ending in 'c') PASS exactly when the
#  control behaves as a control must (the property under test FAILS on it).  A VERDICT line prints only if
#  every line, checks and countercontrols, is PASS; otherwise "NO VERDICT".
#  A  transcription.  A1: sgn/pc/pt parsed from CompositeDimension.lean (:741-755) give cnot = Ad(CNOT)
#     (control first) on all 16 basis tables; A1c: the target-first CNOT must disagree somewhere.  A2: nflip
#     parsed (:798) equals the rotation of Ad(X); A2c: Ad(Z) must differ.  A3: cyc3 parsed from
#     KInfFoundations.lean (:417) is a proper rotation of order 3 with J e_x = e_y, and J L_x J^-1 = L_y.
#     A4: actC R(U) and actT R(U) equal Ad(U x I), Ad(I x U) on all 16 basis tables for two exact unitaries;
#     A4c: actT must differ from Ad(U x I).  A5: relT, relC hold for (cnot, nflip) on all basis tables.
#  B  L3 for (b_DJ).  B1: the real Lie algebra generated (on the 16-dim table space) by the actC generator of
#     the drive (rotation about the NOT axis x), its J-conjugate, and their cnot-conjugates has dimension 6 and
#     contains the table images of i(s_k x P+) and i(s_k x P-), k = x,y,z.  B1c: the drive alone with cnot
#     must give dimension < 6 (abelian);  B2c: the target drive with cnot must give dimension < 6.
#     B3: the exotic cones fail (b_DJ): <actC R_z(pi) E0, E0> < 0 with R_z(pi) = R_x(pi)R_y(pi) a product of
#     the NOT and its J-conjugate; a pure state of K(Z_F) (all Bell-type overlaps <= 1/2) pairs < 0 with
#     actC J e_s.  B4 (retention): Ad(U x I) preserves Q3 on the tested tables (unitary conjugation; PSD of
#     the image of a PSD table checked by exact eigen-free criterion: image = U rho U^dag).
#  C  substratum-class transcription.  C1: the monomial 2x2 unitaries diag(1,i) and X map to R_z(pi/2) and
#     nflip; C2: over all 24 arrangements of |phi0| = (1,2,3,4)/sqrt30 into a 2x2 matrix, min|det| = d0 > 0;
#     C3: c = 513/512 satisfies 1 < c <= 2 and c*m <= 1 where m = (1 + sqrt(1-4 d0^2))/2 (exact, by squaring
#     with signs checked);  C2c: for the product magnitudes (1,2,2,4)/5 the min|det| must be 0.
#  D  lambda countercontrol: for uniform K(E0), the four-copy family-(i) value <E0, E.E0.F^T> with
#     E = cnot(prodState e2 e3), F = cnot(prodState e1 e2) (both in K(E0) = K(E0)*) must be < 0;
#     Dc (retention-type control): the same value with X = Y = phiW (in Q3) must be >= 0.
#  E  eta: K(E0) is not invariant under actC nflip: a pure phi with <phi|pW(E0)|phi> >= 0 and
#     <phi|pW(actC nflip E0)|phi> < 0 exists (exhibited exactly).  E0c: the same phi on E0 itself >= 0.
#  F  zeta: K(Z_F) is drivable as a body: the Bell-diagonal flow U(w) (|w| = 1 symbolic) fixes every defect
#     e_s; U(-1) is an involution moving a pure state of K(Z_F); J = Ad(X x I) permutes Z_F and
#     J U(-1) J^-1 moves a point every flow member fixes.  F6c: a Householder flow member off the Bell basis
#     must move some defect e_s out of K(Z_F) (pure witness of K(Z_F) pairing < 0).
import sys, re, itertools
from sympy import Matrix, Rational as Q, I, eye, zeros, sqrt, simplify, expand, conjugate, symbols, kronecker_product as kron
BASE = '../base/verification/lean-mathlib/OIBridge/'
lines = []
def rep(ok, cid, msg=''):
    lines.append(('PASS' if ok else 'FAIL') + ' ' + cid + ((' ' + msg) if msg else ''))
    print(lines[-1])
def clean(M):
    return M.applyfunc(lambda z: simplify(expand(z)))
X = Matrix([[0, 1], [1, 0]]); Y = Matrix([[0, -I], [I, 0]]); Z = Matrix([[1, 0], [0, -1]]); E2 = eye(2)
S = [E2, X, Y, Z]
def pW(w):  # pauliW: (1/4) sum w_mn s_m x s_n, first index = first token (control)
    M = zeros(4, 4)
    for a in range(4):
        for b in range(4):
            if w[a, b] != 0:
                M += w[a, b] * kron(S[a], S[b])
    return M / 4
def tab(rho):  # inverse of pW: tab_mn = tr(rho s_m x s_n)
    return Matrix(4, 4, lambda a, b: simplify(expand((rho * kron(S[a], S[b])).trace())))
def Eab(a, b):
    M = zeros(4, 4); M[a, b] = 1; return M
def ipW(w, v):
    return sum(w[a, b] * v[a, b] for a in range(4) for b in range(4))
def hom(x):
    return Matrix([1, x[0], x[1], x[2]])
def prodState(x, y):
    return hom(x) * hom(y).T
def Hh(R):  # homogenized map diag(1, R)
    M = eye(4)
    for i in range(3):
        for j in range(3):
            M[i + 1, j + 1] = R[i, j]
    return M
def actC(R, w): return Hh(R) * w
def actT(R, w): return w * Hh(R).T
def rotOf(U):  # SO(3) image of a 2x2 unitary: R_ij = tr(s_i U s_j U^dag)/2
    Ud = U.H
    return Matrix(3, 3, lambda i, j: simplify(expand((S[i + 1] * U * S[j + 1] * Ud).trace() / 2)))
# ---- Section A: transcription from the Lean source at L ----
cd = open(BASE + 'CompositeDimension.lean').read()
def parse_tab(name):
    m = re.search(r'def ' + name + r' : Fin 4 → Fin 4 → Fin 4\n(.*?)\n\n', cd, re.S)
    t = {}
    for a, b, c in re.findall(r'\| (\d), (\d) => (\d)', m.group(1)):
        t[(int(a), int(b))] = int(c)
    return t
PC = parse_tab('pc'); PT = parse_tab('pt')
msg = re.search(r'def sgn \(μ ν : Fin 4\) : ℝ := if \(μ = (\d) ∧ ν = (\d)\) ∨ \(μ = (\d) ∧ ν = (\d)\) then -1 else 1', cd)
neg = {(int(msg.group(1)), int(msg.group(2))), (int(msg.group(3)), int(msg.group(4)))}
def cnot(w):
    return Matrix(4, 4, lambda a, b: (-1 if (a, b) in neg else 1) * w[PC[(a, b)], PT[(a, b)]])
P0 = Matrix([[1, 0], [0, 0]]); P1 = Matrix([[0, 0], [0, 1]])
CN = kron(P0, E2) + kron(P1, X)          # control first
CNt = kron(E2, P0) + kron(X, P1)         # target first (countercontrol)
ok1 = len(PC) == 16 and len(PT) == 16 and len(neg) == 2
okc = True; bad = False
for a in range(4):
    for b in range(4):
        w = Eab(a, b)
        if clean(CN * pW(w) * CN.H - pW(cnot(w))) != zeros(4, 4): ok1 = False
        if clean(CNt * pW(w) * CNt.H - pW(cnot(w))) != zeros(4, 4): bad = True
rep(ok1, 'A1', 'cnot (parsed CompositeDimension.lean:741-758) = Ad(CNOT control-first) on 16 basis tables')
rep(bad, 'A1c', 'target-first CNOT disagrees on some basis table')
mn = re.search(r'toFun x := fun i => \(!\[(-?\d), (-?\d), (-?\d)\] : Fin 3 → ℝ\) i \* x i', cd)
NF = Matrix.diag(*[int(mn.group(k)) for k in (1, 2, 3)])
rep(NF == rotOf(X), 'A2', 'nflip (parsed :798) = rotation of Ad(X) = R_x(pi), diag%s' % str(list(NF.diagonal())))
rep(NF != rotOf(Z), 'A2c', 'nflip differs from the rotation of Ad(Z)')
kf = open(BASE + 'KInfFoundations.lean').read()
mc = re.search(r'toFun v := !\[v (\d), v (\d), v (\d)\]', kf)
idx = [int(mc.group(k)) for k in (1, 2, 3)]
MJ = Matrix(3, 3, lambda i, j: 1 if idx[i] == j else 0)
Lx = Matrix([[0, 0, 0], [0, 0, -1], [0, 1, 0]]); Ly = Matrix([[0, 0, 1], [0, 0, 0], [-1, 0, 0]])
Lz = Matrix([[0, -1, 0], [1, 0, 0], [0, 0, 0]])
okJ = MJ.det() == 1 and MJ ** 3 == eye(3) and MJ != eye(3) and MJ * Matrix([1, 0, 0]) == Matrix([0, 1, 0]) \
    and MJ * Lx * MJ.inv() == Ly
rep(okJ, 'A3', 'cyc3 (parsed KInfFoundations.lean:417) proper, order 3, J e_x = e_y, J L_x J^-1 = L_y')
U1 = Matrix([[Q(3, 5), Q(4, 5) * I], [Q(4, 5) * I, Q(3, 5)]])            # exact unitary
U2 = Matrix([[Q(1, 2) + Q(1, 2) * I, Q(1, 2) + Q(1, 2) * I], [-Q(1, 2) + Q(1, 2) * I, Q(1, 2) - Q(1, 2) * I]]) / 1
ok4 = True; ok4c = False
for U in (U1, U2):
    if clean(U * U.H) != eye(2): ok4 = False
    R = rotOf(U)
    for a in range(4):
        for b in range(4):
            w = Eab(a, b)
            if clean(kron(U, E2) * pW(w) * kron(U, E2).H - pW(actC(R, w))) != zeros(4, 4): ok4 = False
            if clean(kron(E2, U) * pW(w) * kron(E2, U).H - pW(actT(R, w))) != zeros(4, 4): ok4 = False
            if clean(kron(U, E2) * pW(w) * kron(U, E2).H - pW(actT(R, w))) != zeros(4, 4): ok4c = True
rep(ok4, 'A4', 'actC R(U) = Ad(U x I), actT R(U) = Ad(I x U) on 16 basis tables, two exact unitaries')
rep(ok4c, 'A4c', 'actT R(U) differs from Ad(U x I) somewhere')
ok5 = all(actT(NF, cnot(actT(NF, Eab(a, b)))) == cnot(Eab(a, b)) and
          actC(NF, cnot(actC(NF, Eab(a, b)))) == actT(NF, cnot(Eab(a, b))) for a in range(4) for b in range(4))
rep(ok5, 'A5', 'relT and relC (CompositeDimension.lean:224-225) hold for (cnot, nflip) on all basis tables')
# ---- Section B: L3 for (b_DJ) on the table space (16x16 maps on row-major vec) ----
def H0(L):
    M = zeros(4, 4)
    for i in range(3):
        for j in range(3):
            M[i + 1, j + 1] = L[i, j]
    return M
Cm = zeros(16, 16)
for a in range(4):
    for b in range(4):
        Cm[4 * a + b, 4 * PC[(a, b)] + PT[(a, b)]] = -1 if (a, b) in neg else 1
def gC(L): return kron(H0(L), eye(4))
def gT(L): return kron(eye(4), H0(L))
def closure(gens):
    basis = []
    def add(M):
        trial = basis + [M]
        if Matrix([list(B) for B in trial]).rank() > len(basis):
            basis.append(M); return True
        return False
    for g in gens: add(g)
    changed = True
    while changed:
        changed = False
        for A in list(basis):
            for B in list(basis):
                if add(A * B - B * A): changed = True
    return basis
def ad_tab(Hm):  # table map of rho -> -i[H, rho]
    M = zeros(16, 16)
    for a in range(4):
        for b in range(4):
            r = pW(Eab(a, b)); img = tab(-I * (Hm * r - r * Hm))
            for c in range(4):
                for d in range(4):
                    M[4 * c + d, 4 * a + b] = img[c, d]
    return M
gx = gC(Lx); gy = gC(MJ * Lx * MJ.inv())
L6 = closure([gx, gy, Cm * gx * Cm, Cm * gy * Cm])
Pp = (E2 + X) / 2; Pm = (E2 - X) / 2
targets = [ad_tab(kron(S[k], P) / 2) for k in (1, 2, 3) for P in (Pp, Pm)]
span_rank = Matrix([list(B) for B in L6]).rank()
with_t = Matrix([list(B) for B in L6] + [list(T) for T in targets]).rank()
rep(len(L6) == 6 and span_rank == 6 and with_t == 6, 'B1',
    'Lie closure {drive_C, J drive_C J^-1, cnot-conjugates}: dim %d, contains ad(s_k x P+-): %s' % (len(L6), with_t == 6))
L_drive = closure([gx, Cm * gx * Cm])
rep(len(L_drive) < 6, 'B1c', 'drive on the control alone with cnot: dim %d (< 6)' % len(L_drive))
L_tdrive = closure([gT(Lx), Cm * gT(Lx) * Cm])
rep(len(L_tdrive) < 6, 'B2c', 'drive on the target alone with cnot: dim %d (< 6)' % len(L_tdrive))
E0 = Eab(0, 0) + Eab(1, 3) - Eab(2, 2)
RyPi = MJ * NF * MJ.inv(); RzPi = NF * RyPi
v3 = ipW(actC(RzPi, E0), E0)
rep(RyPi == Matrix.diag(-1, 1, -1) and RzPi == Matrix.diag(-1, -1, 1) and v3 < 0, 'B3a',
    '<actC(R_x(pi) R_y(pi)) E0, E0> = %s < 0: K(E0) fails (b_DJ)' % v3)
SS = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
def psi(s): return Matrix([1, s[0] * s[1], s[0], -s[1]]) / 2
def eS(s): return tab((eye(4) - 2 * psi(s) * psi(s).H) / 8)
def neg_eigvec(M, lam):
    ns = (M - lam * eye(4)).nullspace()
    return ns[0] if ns else None
okb = False
for s in SS:
    img = actC(MJ, eS(s)); v = neg_eigvec(pW(img), Q(-1, 8))
    if v is None: continue
    nv = simplify((v.H * v)[0])
    ovs = [simplify(abs((psi(t).H * v)[0]) ** 2 / nv) for t in SS]
    val = simplify(ipW(tab(v * v.H / nv), img))
    if all(o <= Q(1, 2) for o in ovs) and val < 0:
        okb = True; rep(True, 'B3b', 'actC J e_%s leaves K(Z_F): witness overlaps %s, pairing %s' % (str(s), ovs, val)); break
if not okb: rep(False, 'B3b', 'no pure witness of K(Z_F) found for actC J')
phi = Matrix([1, 2, 3 * I, -1 + I]); rho = phi * phi.H; Rr = rotOf(U1)
cp1 = (pW(tab(rho))).charpoly().as_expr(); cp2 = (pW(actC(Rr, tab(rho)))).charpoly().as_expr()
rep(simplify(cp1 - cp2) == 0, 'B4', 'retention: actC R(U) preserves the spectrum of a pure table (Ad(U x I), A4)')
# ---- Section C: the substratum (monomial) class transcribed ----
Rq = rotOf(Matrix([[1, 0], [0, I]]))
rep(Rq == Matrix([[0, -1, 0], [1, 0, 0], [0, 0, 1]]) and rotOf(X) == NF, 'C1',
    'monomials diag(1,i), X -> R_z(pi/2), nflip: the class is O(2) about the corner axis z')
def mindet(f):
    return min(abs(f[p[0]] * f[p[3]] - f[p[1]] * f[p[2]]) for p in itertools.permutations(range(4)))
d0n = mindet([1, 2, 3, 4]); d0 = Q(d0n, 30)
rep(d0 > 0, 'C2', 'phi0 = (1,2,3,4)/sqrt30: min over 24 arrangements |det| = %s > 0 (unreachable)' % d0)
rep(mindet([1, 2, 2, 4]) == 0, 'C2c', 'product magnitudes (1,2,2,4)/5: min |det| = 0 (reachable)')
c = Q(513, 512); rhs = 2 / c - 1
rep(c > 1 and c <= 2 and rhs > 0 and 1 - 4 * d0 ** 2 <= rhs ** 2, 'C3',
    'c = 513/512: 1 < c <= 2 and c*m <= 1, m = (1+sqrt(1-4 d0^2))/2 = (1+sqrt(%s))/2' % (1 - 4 * d0 ** 2))
# ---- Section D: lambda countercontrol on uniform K(E0) ----
units = [[1, 0, 0], [0, 1, 0], [0, 0, 1], [-1, 0, 0], [0, -1, 0], [0, 0, -1]]
CP = [cnot(prodState(x, y)) for x in units for y in units]
def fam1(Xt, Yt, Et, Ft): return ipW(Xt, Et * Yt * Ft.T)
vals = [fam1(E0, E0, Et, Ft) for Et in CP for Ft in CP]
e1, e2, e3 = units[0], units[1], units[2]
vref = fam1(E0, E0, cnot(prodState(e2, e3)), cnot(prodState(e1, e2)))
rep(min(vals) < 0, 'D', 'uniform K(E0): min family-(i) value over 1296 gate-supplied effect pairs = %s; at (e2e3, e1e2): %s'
    % (min(vals), vref))
phiW = cnot(prodState([1, 0, 0], [0, 0, 1]))
valsQ = [fam1(phiW, phiW, Et, Ft) for Et in CP for Ft in CP]
rep(min(valsQ) >= 0, 'Dc', 'uniform Q3 control (X = Y = phiW): min over the same pairs = %s >= 0' % min(valsQ))
# ---- Section E: eta (native-gate relations) does not give (b) for the NOT ----
E0n = actC(NF, E0)
ph = Matrix.vstack(kron(X, Z) + eye(4), kron(Y, Y) + eye(4)).nullspace()[0]
a0 = simplify((ph.H * pW(E0) * ph)[0]); a1 = simplify((ph.H * pW(E0n) * ph)[0])
rep(E0n == Eab(0, 0) + Eab(1, 3) + Eab(2, 2) and a0 >= 0 and a1 < 0, 'E',
    'actC nflip E0 = E00+E13+E22 leaves K(E0): <phi|pW(E0)|phi> = %s >= 0, <phi|pW(image)|phi> = %s < 0' % (a0, a1))
perm_ok = all(any(actC(NF, eS(s)) == eS(t) for t in SS) for s in SS)
rep(perm_ok, 'E0c', 'control: actC nflip permutes the defects of Z_F (K(Z_F) is not moved by the NOT)')
# ---- Section F: zeta, the pair body of K(Z_F) is drivable ----
gram = Matrix(4, 4, lambda i, j: (psi(SS[i]).H * psi(SS[j]))[0])
u = symbols('u', real=True); w = (1 - u ** 2 + 2 * I * u) / (1 + u ** 2)
def Uf(wv): return eye(4) + (wv - 1) * psi(SS[0]) * psi(SS[0]).H
okF1 = gram == eye(4) and simplify(w * conjugate(w)) == 1
for s in SS:
    d = (eye(4) - 2 * psi(s) * psi(s).H) / 8
    if clean(Uf(w) * d * Uf(w).H - d) != zeros(4, 4): okF1 = False
rep(okF1, 'F1', 'Bell-type basis orthonormal; the flow U(w), |w| = 1 (symbolic u), fixes every defect of Z_F')
Nf = Uf(-1); chi = (psi(SS[0]) + psi(SS[1])); Nchi = Nf * chi
inK = all(abs((psi(t).H * chi)[0]) ** 2 / (chi.H * chi)[0] <= Q(1, 2) for t in SS)
rep(Nf * Nf == eye(4) and inK and tab(chi * chi.H) != tab(Nchi * Nchi.H), 'F2',
    'N = U(-1) is an involution moving the pure state of K(Z_F) on (psi0+psi1)')
Jm = kron(X, E2); jimg = []
for s in SS:
    im = Jm * psi(s); hit = [t for t in SS if im == psi(t) or im == -psi(t)]
    jimg.append(hit[0] if hit else None)
j = SS.index(jimg[0]) if jimg[0] is not None else None
k = [t for t in range(4) if t not in (0, j)][0] if j is not None else None
ok3 = None not in jimg and len(set(jimg)) == 4
if ok3:
    JNJ = Jm * Nf * Jm.H; chi2 = psi(SS[j]) + psi(SS[k])
    fixed = clean(Uf(w) * chi2 - chi2) == zeros(4, 1)
    moved = tab(chi2 * chi2.H) != tab((JNJ * chi2) * (JNJ * chi2).H)
    inK2 = all(abs((psi(t).H * chi2)[0]) ** 2 / (chi2.H * chi2)[0] <= Q(1, 2) for t in SS)
    ok3 = fixed and moved and inK2
rep(ok3, 'F3', 'J = Ad(X x I) permutes Z_F; J N J^-1 moves a point of K(Z_F) that every flow member fixes')
Hh00 = eye(4) - 2 * Matrix([1, 0, 0, 0]) * Matrix([[1, 0, 0, 0]]); f6 = False
for s in SS:
    ch = Hh00 * psi(s); nn = (ch.H * ch)[0]
    if all(abs((psi(t).H * ch)[0]) ** 2 / nn <= Q(1, 2) for t in SS):
        img = tab(Hh00 * ((eye(4) - 2 * psi(s) * psi(s).H) / 8) * Hh00.H)
        if ipW(tab(ch * ch.H / nn), img) < 0: f6 = True
rep(f6, 'F6c', 'control: a Householder member off the Bell basis moves a defect out of K(Z_F)')
nf = sum(1 for l in lines if l.startswith('FAIL'))
print('SUMMARY %d lines, %d FAIL' % (len(lines), nf))
if nf == 0:
    print('VERDICT D1-BRIDGE-EXACT: transcription exact; (b_DJ) Lie closure = su(2)+su(2) (dim 6); drive alone and target '
          'drive < 6; K(E0), K(Z_F) fail (b_DJ); monomial class + cnot + T leaves phi0 unreachable (seed c = 513/512); '
          'lambda fails on uniform K(E0), holds on the Q3 control; native relations do not give (b) for the NOT; '
          'K(Z_F) carries a drivable pair body')
else:
    print('NO VERDICT')
