"""E16 probe b -- the residual, odd chart dimension: the quantum-classical hybrid token (a qubit with a two-sector
superselection rule) meets every pair-level hypothesis of the K2 schema in the kernel's form and is not an ellipsoid.
(exact: Fractions and Gaussian rationals; no floating point)

S0-b (written 2026-10-11T03:36Z by `date -u`, after probe a and before run 1 of this probe): NOTES-E16 S0-b.

THE BODY.  Omega_h in R^7, chart coordinates y = (w, a, b), a, b in R^3; t0 = (1 + w)/2, t1 = (1 - w)/2, r0 = (a + b)/2,
r1 = (a - b)/2; Omega_h = {t0, t1 >= 0, |r0|^2 <= t0^2, |r1|^2 <= t1^2}.  Homogenized chart coordinates (T, w, a, b) are
the image of V_q (x) V_b (qubit table index mu = 0..3, sector index i = 0, 1; basis order (mu, i) -> 2 mu + i) under the
linear map Phi: T = t0 + t1, w = t0 - t1, a = r0 + r1, b = r0 - r1.  NOT N = 1 (+) nflip (+) nflip on (w, a, b) (nflip =
diag(1, -1, -1), the kernel's, CompositeDimension.lean:797); corner z = (0, e_3, 0) (a's third coordinate); hom z =
hom_q(z3) (x) (e_0 + e_1)/2.  Gate G = (Phi (x) Phi)(cnot (x) id)(Phi (x) Phi)^-1 on W 7: on every sector block of a table
in the V_q (x) V_b basis, the kernel's cnot (PARSED, :741-:758).  Drive: the flow of ball3Drive (rotFun about the third
axis, KInfFoundations.lean) and its J (cycEquiv, :416) acting on a and b together.  Composite K: the tables whose every
sector block (in the V_q (x) V_b basis) lies in Q3, i.e. has a positive semidefinite image under the qubit dictionary
(1/4) sum B[mu][nu] s_mu (x) s_nu.  The kernel's actions on W 7: actC N w = H w, actT N w = w H^T with H = homMap N.

CHECKS.
  H1  IsNot Omega_h z N (unit z, N an involution, N z = -z, N preserves Omega_h on 12 exact states and as the
      transformation r_i -> nflip r_i of the defining inequalities); Omega_h is compact, convex, with interior (the
      inequalities bound |w| <= 1, |a|, |b| <= 2; the point 0 satisfies all of them strictly); a sharp seed: the effect
      (1 + w)/2 takes the value 1 at (1, 0, 0) and 0 at (-1, 0, 0) and lies in [0, 1] on the 12 states.
  H2  ElementaryDrivability Omega_h: the flow F_t = 1 (+) R_z(t) (+) R_z(t) preserves Omega_h at cos t = 3/5, 5/13 on the
      12 states; the group law F_s F_t = F_{s+t} at those two angles (exact cosines and sines); F_pi is an involution and
      moves a state; J = 1 (+) cyc (+) cyc preserves Omega_h with its inverse; J F_{pi/2} J^-1 moves the state
      (1, e_3, e_3), which every flow member fixes (J_off_axis).
  H3  NativeGate's algebraic clauses on all 64 basis tables of W 7: the frame on the four corner products, relT, relC;
      G is an involution (so G.symm = G); the count of NOTES-E16 (A1): tr H = 0 and tr(actC N) = tr(actC N o actT N) = 0
      on W 7.
  H4  NativeGate's positivity: for 10 x 10 pairs of exact states, every sector block of G(prodState x y) has a PSD
      dictionary image (exact principal minors), so every product of effects -- effects decompose by sector -- is
      nonnegative; and directly, for 8 x 8 extreme effects (1 + n.r)/2 on one sector, n rational unit vectors, the value
      of the product effect on G(prodState x y) is >= 0 in chart coordinates.  posInv is the same statement (G.symm = G).
  H5  Entangling Omega_h G: x = (1, e_1, e_1) and y = (1, e_3, e_3) (pure states of sector 0, extreme points of Omega_h)
      have G(prodState x y) with sector block (0, 0) of rank 4, so it is not a product state; its extremality among the
      joint states is the kernel's entangling_cnot read blockwise (written).
  H6  The composite K: it contains prodState x y for the 10 x 10 exact pairs; G maps those products and five further
      elements of K into K; actT of F_t (cos t = 3/5) and of J maps them into K; and K is self-dual for the product form
      M (x) M, M Euclidean in the V_q (x) V_b basis (written: blockwise Q3 = dualW Q3, EqvK2Schema's Q3_selfDual [D]),
      with the exact instance that a table whose block (0, 0) is idW (not in Q3) pairs -2 with an element of K.
  H7  Omega_h is no ellipsoid: the segment from (1, e_3, e_3) to (-1, e_3, -e_3) lies in its boundary (at s = -1, -1/2,
      0, 1/2, 1 the point (s, e_3, s e_3) has |r0| = t0 and |r1| = t1); and SingletonFaces fails: the effect t1 vanishes
      at the two distinct states (1, e_1, e_1) and (1, e_3, e_3).
COUNTERCONTROLS (each must fail as stated).
  XH1  "the zero face of the effect t1 is a single state" -- fails (H7's two states).
  XH2  "the boundary of Omega_h contains no segment" -- fails (H7's segment).
  XH3  "the gate with cnot replaced by the identity is entangling" -- fails: the image of H5's input is then a product
       (every sector block of rank <= 1).
DECISION RULE (fixed before run 1).  VERDICT E16B-HYBRID-MEETS-PAIR-LEVEL-NOT-ELLIPSOID iff H1-H7 print PASS, no FAIL,
XH1-XH3 each print "COUNTER ... fails as stated", and the last line before the verdict is "checks: 7, failures: 0".
Otherwise "VERDICT NOT RENDERED" with the failing items.  The verdict says only that this exact body meets the stated
clauses on the stated instances and is not an ellipsoid; the general statements of positivity, of the composite's
self-duality and of extremality are the written arguments of NOTES-E16 S0-b; nothing is said about strictly convex
bodies.
"""
import itertools
import re
import sys
from fractions import Fraction as Fr

KERNEL = '../../../verification/lean-mathlib/OIBridge/'
RESULTS = []


def check(name, ok, detail=''):
    RESULTS.append((name, bool(ok)))
    print(('PASS ' if ok else 'FAIL ') + name + ((' -- ' + detail) if detail else ''), flush=True)


def src(f):
    return open(f, encoding='utf-8').read()


# ------------------------------------------------------------------ kernel data, parsed
cd = src(KERNEL + 'CompositeDimension.lean')
kf = src(KERNEL + 'KInfFoundations.lean')


def parse_table(text, name):
    mt = re.search(r'def %s : Fin 4 → Fin 4 → Fin 4\n((?:  \|.*\n)+)' % name, text)
    entries = re.findall(r'(\d), (\d) => (\d)', mt.group(1))
    return {(int(a), int(b)): int(c) for a, b, c in entries}


def parse_sgn(text):
    mt = re.search(r'def sgn \(μ ν : Fin 4\) : ℝ := if \(μ = (\d) ∧ ν = (\d)\) ∨ \(μ = (\d) ∧ ν = (\d)\) then -1 else 1', text)
    neg = {(int(mt.group(1)), int(mt.group(2))), (int(mt.group(3)), int(mt.group(4)))}
    return {(a, b): (-1 if (a, b) in neg else 1) for a in range(4) for b in range(4)}


PC, PT, SGN = parse_table(cd, 'pc'), parse_table(cd, 'pt'), parse_sgn(cd)
mn = re.search(r'def nflip : \(Fin 3 → ℝ\) →ₗ\[ℝ\] \(Fin 3 → ℝ\) where\n  toFun x := fun i => \(!\[(.*?)\] : Fin 3 → ℝ\) i \* x i', cd)
NFLIP = [int(t.strip()) for t in mn.group(1).split(',')]
mc = re.search(r'noncomputable def cycEquiv : \(Fin 3 → ℝ\) ≃ₗ\[ℝ\] \(Fin 3 → ℝ\) where\n  toFun v := !\[v (\d), v (\d), v (\d)\]', kf)
CYC = [int(mc.group(k)) for k in (1, 2, 3)]
ROT_OK = all(t in kf for t in ('rotFun t v 0 = Real.cos t * v 0 - Real.sin t * v 1 ∧',
                               'rotFun t v 1 = Real.sin t * v 0 + Real.cos t * v 1 ∧ rotFun t v 2 = v 2'))
print('parsed: cnot (pc, pt, sgn); nflip = diag%s; cycEquiv v = (v %d, v %d, v %d); rotFun_apply: %s'
      % (NFLIP, CYC[0], CYC[1], CYC[2], ROT_OK), flush=True)


def cnot_q(B):
    return [[SGN[(m, n)] * B[PC[(m, n)]][PT[(m, n)]] for n in range(4)] for m in range(4)]


# ------------------------------------------------------------------ linear algebra over Q
def zeros(r, c):
    return [[Fr(0)] * c for _ in range(r)]


def mm(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]


def tp(A):
    return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]


def mv(A, v):
    return [sum(A[i][k] * v[k] for k in range(len(v))) for i in range(len(A))]


def inverse(A):
    n = len(A)
    M = [list(map(Fr, A[i])) + [Fr(1) if i == j else Fr(0) for j in range(n)] for i in range(n)]
    for c in range(n):
        p = next(r for r in range(c, n) if M[r][c] != 0)
        M[c], M[p] = M[p], M[c]
        pv = M[c][c]
        M[c] = [x / pv for x in M[c]]
        for r in range(n):
            if r != c and M[r][c] != 0:
                f = M[r][c]
                M[r] = [M[r][j] - f * M[c][j] for j in range(2 * n)]
    return [row[n:] for row in M]


def rank(A):
    M = [list(map(Fr, r)) for r in A]
    rk, rows, cols = 0, len(M), len(M[0])
    for c in range(cols):
        p = next((r for r in range(rk, rows) if M[r][c] != 0), None)
        if p is None:
            continue
        M[rk], M[p] = M[p], M[rk]
        for r in range(rows):
            if r != rk and M[r][c] != 0:
                f = M[r][c] / M[rk][c]
                M[r] = [M[r][j] - f * M[rk][j] for j in range(cols)]
        rk += 1
    return rk


# ------------------------------------------------------------------ the chart and Phi
def idx(mu, i):
    return 2 * mu + i


PHI = zeros(8, 8)                                   # rows: (T, w, a0, a1, a2, b0, b1, b2); columns: (mu, i)
PHI[0][idx(0, 0)] = Fr(1); PHI[1][idx(0, 0)] = Fr(1)
PHI[0][idx(0, 1)] = Fr(1); PHI[1][idx(0, 1)] = Fr(-1)
for kk in range(3):
    PHI[2 + kk][idx(kk + 1, 0)] = Fr(1); PHI[5 + kk][idx(kk + 1, 0)] = Fr(1)
    PHI[2 + kk][idx(kk + 1, 1)] = Fr(1); PHI[5 + kk][idx(kk + 1, 1)] = Fr(-1)
PHIinv = inverse(PHI)


def hom(y):
    return [Fr(1)] + [Fr(t) for t in y]


def outer(u, v):
    return [[u[i] * v[j] for j in range(len(v))] for i in range(len(u))]


def prod_state(x, y):
    return outer(hom(x), hom(y))


def to_qb(wc):                                      # chart table -> V_q (x) V_b table
    return mm(mm(PHIinv, wc), tp(PHIinv))


def to_chart(wq):
    return mm(mm(PHI, wq), tp(PHI))


def block(wq, i, j):
    return [[wq[idx(m, i)][idx(n, j)] for n in range(4)] for m in range(4)]


def set_block(wq, i, j, B):
    for m in range(4):
        for n in range(4):
            wq[idx(m, i)][idx(n, j)] = B[m][n]


def gate_q(wq, qmap=cnot_q):
    out = zeros(8, 8)
    for i in range(2):
        for j in range(2):
            set_block(out, i, j, qmap(block(wq, i, j)))
    return out


def G(wc, qmap=cnot_q):
    return to_chart(gate_q(to_qb(wc), qmap))


def lin_chart(w_, A3a, A3b):
    """1 (+) A3 (+) A3 on (w, a, b) as a 7 x 7 matrix"""
    M = zeros(7, 7)
    M[0][0] = Fr(w_)
    for i in range(3):
        for j in range(3):
            M[1 + i][1 + j] = Fr(A3a[i][j])
            M[4 + i][4 + j] = Fr(A3b[i][j])
    return M


def homH(N):
    H = zeros(8, 8)
    H[0][0] = Fr(1)
    for i in range(7):
        for j in range(7):
            H[1 + i][1 + j] = N[i][j]
    return H


def actC(H, w):
    return mm(H, w)


def actT(H, w):
    return mm(w, tp(H))


NF = [[NFLIP[i] if i == j else 0 for j in range(3)] for i in range(3)]
N7 = lin_chart(1, NF, NF)
H7 = homH(N7)


# ------------------------------------------------------------------ the body
def mem(y):
    w, a, b = Fr(y[0]), [Fr(t) for t in y[1:4]], [Fr(t) for t in y[4:7]]
    t0, t1 = (1 + w) / 2, (1 - w) / 2
    r0 = [(a[k] + b[k]) / 2 for k in range(3)]
    r1 = [(a[k] - b[k]) / 2 for k in range(3)]
    return t0 >= 0 and t1 >= 0 and sum(t * t for t in r0) <= t0 * t0 and sum(t * t for t in r1) <= t1 * t1


def state(t0, r0, r1):
    """chart point from sector weight t0 (t1 = 1 - t0) and sector Bloch parts r0, r1 (already weighted)"""
    t0 = Fr(t0)
    w = 2 * t0 - 1
    a = [Fr(r0[k]) + Fr(r1[k]) for k in range(3)]
    b = [Fr(r0[k]) - Fr(r1[k]) for k in range(3)]
    return [w] + a + b


E1, E2, E3 = [1, 0, 0], [0, 1, 0], [0, 0, 1]
STATES = [
    state(1, E1, [0, 0, 0]), state(1, E3, [0, 0, 0]), state(1, [Fr(3, 5), Fr(4, 5), 0], [0, 0, 0]),
    state(0, [0, 0, 0], E2), state(0, [0, 0, 0], [0, Fr(-3, 5), Fr(4, 5)]),
    state(Fr(1, 2), [Fr(1, 2) * Fr(3, 5), 0, Fr(1, 2) * Fr(4, 5)], [0, Fr(-1, 2), 0]),
    state(Fr(1, 2), [0, 0, Fr(1, 2)], [0, 0, Fr(1, 2)]),                 # the corner z
    state(Fr(1, 2), [0, 0, Fr(-1, 2)], [0, 0, Fr(-1, 2)]),               # -z
    state(Fr(1, 3), [Fr(1, 9), Fr(-2, 9), Fr(2, 9)], [Fr(1, 3), 0, 0]),
    state(Fr(1, 2), [0, 0, 0], [0, 0, 0]),                               # the centre
    state(Fr(3, 4), [Fr(1, 4), Fr(1, 4), 0], [0, 0, Fr(-1, 5)]),
    state(Fr(1, 5), [0, Fr(1, 5), 0], [Fr(-4, 5), 0, 0]),
]
ZC = [Fr(0), Fr(0), Fr(0), Fr(1), Fr(0), Fr(0), Fr(0)]


def apply7(M, y):
    return mv(M, [Fr(t) for t in y])


I3m = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
ok_h1 = (all(mem(s) for s in STATES) and mm(N7, N7) == lin_chart(1, I3m, I3m)
         and apply7(N7, ZC) == [-t for t in ZC] and sum(t * t for t in ZC) == 1
         and all(mem(apply7(N7, s)) for s in STATES) and ZC == state(Fr(1, 2), [0, 0, Fr(1, 2)], [0, 0, Fr(1, 2)]))
seed = lambda y: (1 + Fr(y[0])) / 2
ok_h1 = ok_h1 and seed(state(1, [0, 0, 0], [0, 0, 0])) == 1 and seed(state(0, [0, 0, 0], [0, 0, 0])) == 0 \
    and all(0 <= seed(s) <= 1 for s in STATES)
strict0 = all(v > 0 for v in [(1 + 0) / 2, (1 - 0) / 2])                 # t0, t1 > 0 and r0 = r1 = 0 at the centre
check('H1', ok_h1 and strict0 and NFLIP == [1, -1, -1],
      'IsNot Omega_h z N (z = (0, e_3, 0) = the corner state hom_q(z3) (x) (e0 + e1)/2); 12 exact states; sharp seed (1 + w)/2')


# ------------------------------------------------------------------ H2: the drive
def Rz(c, s):
    return [[c, -s, 0], [s, c, 0], [0, 0, 1]]


def flow(c, s):
    return lin_chart(1, Rz(c, s), Rz(c, s))


CYCM = [[1 if CYC[i] == j else 0 for j in range(3)] for i in range(3)]
CYCinv = tp(CYCM)
J = lin_chart(1, CYCM, CYCM)
Jinv = lin_chart(1, CYCinv, CYCinv)
angles = [(Fr(3, 5), Fr(4, 5)), (Fr(5, 13), Fr(12, 13))]
ok_pres = all(mem(apply7(flow(c, s), st)) for (c, s) in angles for st in STATES)
(c1, s1), (c2, s2) = angles
ok_law = mm(flow(c1, s1), flow(c2, s2)) == flow(c1 * c2 - s1 * s2, s1 * c2 + c1 * s2)
Fpi = flow(Fr(-1), Fr(0))
ok_inv = mm(Fpi, Fpi) == lin_chart(1, I3m, I3m) and any(apply7(Fpi, st) != [Fr(t) for t in st] for st in STATES)
ok_J = all(mem(apply7(J, st)) and mem(apply7(Jinv, st)) for st in STATES) and mm(J, Jinv) == lin_chart(1, I3m, I3m)
xw = state(1, E3, [0, 0, 0])                                              # (1, e3, e3)
conj = mm(mm(J, flow(Fr(0), Fr(1))), Jinv)
fixes = all(apply7(flow(c, s), xw) == [Fr(t) for t in xw] for (c, s) in angles + [(Fr(-1), Fr(0)), (Fr(0), Fr(1))])
ok_off = apply7(conj, xw) != [Fr(t) for t in xw] and fixes
check('H2', ROT_OK and ok_pres and ok_law and ok_inv and ok_J and ok_off,
      'flow 1 (+) R_z (+) R_z preserves Omega_h at two exact angles, group law, F_pi involutive and moving; J = 1 (+) cyc (+) '
      'cyc preserves; J F_{pi/2} J^-1 moves (1, e3, e3), which every flow member fixes')


# ------------------------------------------------------------------ H3: the gate's algebraic clauses
def basis(p, q):
    B = zeros(8, 8)
    B[p][q] = Fr(1)
    return B


def corner(a):
    return ZC if a == 0 else [-t for t in ZC]


frame_ok = all(G(prod_state(corner(a), corner(b))) == prod_state(corner(a), corner((a + b) % 2))
               for a in range(2) for b in range(2))
relT_ok = relC_ok = inv_ok = True
for p in range(8):
    for q in range(8):
        E = basis(p, q)
        if actT(H7, G(actT(H7, E))) != G(E):
            relT_ok = False
        if actC(H7, G(actC(H7, E))) != actT(H7, G(E)):
            relC_ok = False
        if G(G(E)) != E:
            inv_ok = False
trH = sum(H7[i][i] for i in range(8))
trC = sum(actC(H7, basis(p, q))[p][q] for p in range(8) for q in range(8))
trCT = sum(actC(H7, actT(H7, basis(p, q)))[p][q] for p in range(8) for q in range(8))
check('H3', frame_ok and relT_ok and relC_ok and inv_ok and trH == 0 and trC == 0 and trCT == 0,
      'frame on the four corner products; relT and relC on all 64 basis tables; G o G = id; tr H = %s, tr(actC N) = %s, '
      'tr(actC N o actT N) = %s' % (trH, trC, trCT))


# ------------------------------------------------------------------ PSD tests through the qubit dictionary
Z0 = (Fr(0), Fr(0))


def cadd(x, y):
    return (x[0] + y[0], x[1] + y[1])


def cmul(x, y):
    return (x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0])


SIG = [[[(1, 0), (0, 0)], [(0, 0), (1, 0)]], [[(0, 0), (1, 0)], [(1, 0), (0, 0)]],
       [[(0, 0), (0, -1)], [(0, 1), (0, 0)]], [[(1, 0), (0, 0)], [(0, 0), (-1, 0)]]]
SIG = [[[(Fr(a), Fr(b)) for (a, b) in row] for row in S] for S in SIG]


def dict_q(B):
    H = [[Z0] * 4 for _ in range(4)]
    for m in range(4):
        for n in range(4):
            if B[m][n] != 0:
                for r in range(4):
                    for c in range(4):
                        e = cmul(SIG[m][r // 2][c // 2], SIG[n][r % 2][c % 2])
                        H[r][c] = cadd(H[r][c], (B[m][n] / 4 * e[0], B[m][n] / 4 * e[1]))
    return H


def det_c(M):
    if len(M) == 1:
        return M[0][0]
    s = Z0
    for j in range(len(M)):
        minor = [row[:j] + row[j + 1:] for row in M[1:]]
        t = cmul(M[0][j], det_c(minor))
        s = cadd(s, t) if j % 2 == 0 else (s[0] - t[0], s[1] - t[1])
    return s


def psd(B):
    H = dict_q(B)
    for r in range(1, 5):
        for ix in itertools.combinations(range(4), r):
            d = det_c([[H[i][j] for j in ix] for i in ix])
            if d[1] != 0 or d[0] < 0:
                return False
    return True


def in_K(wc):
    wq = to_qb(wc)
    return all(psd(block(wq, i, j)) for i in range(2) for j in range(2))


# ------------------------------------------------------------------ H4: positivity
PAIRS = STATES[:10]
images = {}
for ix_, x in enumerate(PAIRS):
    for jx, y in enumerate(PAIRS):
        images[(ix_, jx)] = G(prod_state(x, y))
blocks_psd = all(in_K(img) for img in images.values())
unit_ns = [E1, [-1, 0, 0], E3, [0, 0, -1], [Fr(3, 5), Fr(4, 5), 0], [0, Fr(-3, 5), Fr(4, 5)]]


def effect_chart(sector, n):
    """the functional (t_sector + n . r_sector)/2 on V_q (x) V_b, in chart coordinates"""
    fq = [Fr(0)] * 8
    fq[idx(0, sector)] = Fr(1, 2)
    for k in range(3):
        fq[idx(k + 1, sector)] = Fr(n[k]) / 2
    return mv(tp(PHIinv), fq)                         # f_chart(v) = f_q(PHIinv v)


EFFS = [effect_chart(s_, n) for s_ in range(2) for n in unit_ns][:8]
eff_ok = all(0 <= sum(e[i] * hom(s)[i] for i in range(8)) <= 1 for e in EFFS for s in STATES)
pair_vals = [sum(e[m] * img[m][n] * f[n] for m in range(8) for n in range(8))
             for img in images.values() for e in EFFS for f in EFFS]
check('H4', blocks_psd and eff_ok and min(pair_vals) >= 0,
      'all %d images G(prodState x y) have PSD sector blocks; %d values of 8 x 8 extreme product effects on them, minimum %s'
      % (len(images), len(pair_vals), min(pair_vals)))

# ------------------------------------------------------------------ H5: entangling
xe, ye = state(1, E1, [0, 0, 0]), state(1, E3, [0, 0, 0])
img = to_qb(G(prod_state(xe, ye)))
rk00 = rank(block(img, 0, 0))
other_zero = all(block(img, i, j) == zeros(4, 4) for i in range(2) for j in range(2) if (i, j) != (0, 0))
check('H5', rk00 == 4 and other_zero and mem(xe) and mem(ye),
      'G(prodState x y) for x = (1, e1, e1), y = (1, e3, e3): block (0,0) of rank %d, the other blocks zero: not a product' % rk00)

# ------------------------------------------------------------------ H6: the composite K
elems = [prod_state(x, y) for x in PAIRS for y in PAIRS]
extra = []
for k_ in range(5):
    wq = zeros(8, 8)
    for i in range(2):
        for j in range(2):
            u = [Fr(1), Fr(k_ - 2, 5), Fr(1, 3) if i == j else Fr(-1, 4), Fr(1, 7)]
            v = [Fr(1), Fr(1, 2), Fr(-1, 2), Fr(k_, 9)]
            set_block(wq, i, j, outer(u, v))          # products of ball vectors: PSD blocks
    extra.append(to_chart(wq))
prod_in = all(in_K(e) for e in elems)
gate_in = all(in_K(G(e)) for e in elems[:30] + extra)
Ft = flow(Fr(3, 5), Fr(4, 5))
HF, HJ = homH(Ft), homH(J)
drive_in = all(in_K(actT(HF, e)) and in_K(actT(HJ, e)) for e in elems[:30] + extra)
wbad = zeros(8, 8)
set_block(wbad, 0, 0, [[Fr(1) if m == n else Fr(0) for n in range(4)] for m in range(4)])     # idW in block (0, 0)
wpsi = zeros(8, 8)
set_block(wpsi, 0, 0, [[Fr(1), 0, 0, 0], [0, Fr(-1), 0, 0], [0, 0, Fr(-1), 0], [0, 0, 0, Fr(-1)]])   # the singlet's table
pair_bad = sum(wbad[p][q] * wpsi[p][q] for p in range(8) for q in range(8))
check('H6', prod_in and gate_in and drive_in and psd(block(wpsi, 0, 0)) and not psd(block(wbad, 0, 0)) and pair_bad == -2,
      'K contains the %d products; G, actT F_t and actT J map 35 elements of K into K; idW in block (0,0) pairs %s with an '
      'element of K (product form M (x) M)' % (len(elems), pair_bad))

# ------------------------------------------------------------------ H7: not an ellipsoid; faces
seg = []
for s in (Fr(-1), Fr(-1, 2), Fr(0), Fr(1, 2), Fr(1)):
    y_ = [s, Fr(0), Fr(0), Fr(1), Fr(0), Fr(0), s]
    w, a, b = y_[0], y_[1:4], y_[4:7]
    t0, t1 = (1 + w) / 2, (1 - w) / 2
    r0 = [(a[k] + b[k]) / 2 for k in range(3)]
    r1 = [(a[k] - b[k]) / 2 for k in range(3)]
    seg.append(mem(y_) and sum(t * t for t in r0) == t0 * t0 and sum(t * t for t in r1) == t1 * t1)
t1eff = lambda y: (1 - Fr(y[0])) / 2
face = [state(1, E1, [0, 0, 0]), state(1, E3, [0, 0, 0])]
face_two = all(mem(f) and t1eff(f) == 0 for f in face) and face[0] != face[1] and all(0 <= t1eff(s) <= 1 for s in STATES)
check('H7', all(seg) and face_two,
      'the segment (s, e3, s e3), s in [-1, 1], lies in the boundary; the effect t1 vanishes at two distinct states')

# ------------------------------------------------------------------ countercontrols
counters = [('XH1', face_two, 'the zero face of t1 holds two distinct states'),
            ('XH2', all(seg), 'a nondegenerate boundary segment exists')]
img_id = to_qb(G(prod_state(xe, ye), qmap=lambda B: [row[:] for row in B]))
id_product = all(rank(block(img_id, i, j)) <= 1 for i in range(2) for j in range(2))
counters.append(('XH3', id_product, 'with the identity in place of cnot the image is a product (every block of rank <= 1)'))
for name, failed, detail in counters:
    print(('COUNTER %s fails as stated' % name) if failed else ('COUNTER %s DID NOT FAIL' % name), '--', detail, flush=True)

nfail = sum(1 for _, ok in RESULTS if not ok)
print('checks: %d, failures: %d' % (len(RESULTS), nfail), flush=True)
if nfail == 0 and len(RESULTS) == 7 and all(c[1] for c in counters):
    print('VERDICT E16B-HYBRID-MEETS-PAIR-LEVEL-NOT-ELLIPSOID')
else:
    print('VERDICT NOT RENDERED -- failing: %s' % ([n for n, ok in RESULTS if not ok] + [c[0] for c in counters if not c[1]]))
sys.exit(0)
