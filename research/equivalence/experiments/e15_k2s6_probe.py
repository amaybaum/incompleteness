"""E15 probe -- the exact layer of draft S6 (K2-SCHEMA-1): the positive control Q3, the reachability lemma on exact
instances, and HO-24's countercontrol recomputed: the native octahedral repertoire on one token leaves an explicit
invariant cone that contains the products, lies in its own dual, differs from Q3, and is not preserved by the flow.
(exact: Gaussian rationals as pairs of Fractions; sympy only in R1, which is E10's L4 code copied unchanged)

S0 (written 2026-10-11T03:08Z by `date -u`, before run 1; predictions in NOTES-E15.md S0).

SETTING (kernel vocabulary at L).  W 3 = 4 x 4 real tables w[mu][nu], mu the control token, nu the target token
(CompositeDimension.lean:97).  actT N acts on the target index by (1 (+) N) (:198).  The kernel's cnot is the signed
permutation cnotFun (:741-:758) and is PARSED here; rotFun (KInfFoundations.lean, the lines of rotFun_apply) and
cycEquiv (:416) are PARSED.  The dictionary is EqvK2Schema's: dict w = (1/4) sum w[mu][nu] s_mu (x) s_nu, control
first; coordOf H [mu][nu] = tr((s_mu (x) s_nu) H); Q3 = {w : dict w PSD}.  The finite clause is invariance under
G384 = <cnot, actT R_z(pi/2), actT cyc3> (HO-14, HO-24); the full flow is invariance under actT (rotLin t), all t, with
actT cycEquiv (the module's A_miss, HO-5's form).  The countercontrol is HO-24 item 4's cone
K* = (PSD cap Z*) + cone Z, Z the G384-orbit of the defect d* = I - c* P_{h*}, h* = (10, 2-2i, -1-3i, 3-i)/sqrt(128),
c* = 401/400.  Its self-duality is Theorem S' of the countermodels thread (HO-24 item 3, [W], read by the
coordinator), whose hypothesis is condition (CC) on every pair; this probe checks (CC) and every other exact item and
does NOT check S' itself.

CHECKS.
  D1  the lift: through the dictionary, on all 16 basis tables, the parsed cnot is Ad(CNOT) (CNOT = P0 (x) 1 + P1 (x) X),
      actT R_z(pi/2) is Ad(1 (x) diag(1, i)), actT cyc3 is Ad(1 (x) U_J) with U_J = (I - i(X + Y + Z))/2, and actT
      R_z(theta0) (cos theta0 = 3/5, sin theta0 = 4/5) is Ad(1 (x) diag(1, (3 + 4i)/5)); each lift is unitary exactly.
  D2  the table group <cnot, actT R_z(pi/2), actT cyc3> is a group of 384 signed permutations of the 16 coordinates.
  P1  positive control (H1 for Q3): dict(prodState x y) is PSD for 36 pairs of rational ball points (exact principal
      minors), and dict(prodState x y) = rho_x (x) rho_y.
  P2  positive control (H3 for Q3, an instance): an exact non-PSD Hermitian table pairs negatively with a pure state,
      and tr(A B) >= 0 for a PSD pair.
  X1  the orbit of the ray of h* under the lift generators has exactly 192 rays, closed under each generator (so the
      defect set Z is invariant under the three table generators of G384 by D1).
  X2  the 18336 pairwise squared overlaps lie in [25/2048, 13/16], both bounds attained; every pairing
      tr(d_j d_k) = 4 - 2c* + c*^2 s_jk is positive.
  X3  H1 for K*: for every defect, c* lambda_max <= 1, by the exact test 1 - 4D <= (2/c* - 1)^2 with D the normalized
      |det Psi|^2 (the minimum D is 85/2048), so every product state pairs nonnegatively with every defect.
  X4  (CC) at c* = 401/400: c*^2 s_jk >= 4(c* - 1) on all 18336 pairs.
  X5  K* differs from Q3: <h*| d* |h*> = 1 - c* = -1/400 < 0, so d* (in K*) is not in Q3; and with T_h read as
      coordOf(P_h), HO-24's table z* = E00/2 - (c*/8) T_{h*} satisfies dict z* = d*/8 exactly.
  X6  the flow is load-bearing: with R = 1 (x) diag(1, (3 + 4i)/5) (D1: actT R_z(theta0)), the state v_R = R h* has
      squared overlap at most 1/c* = 400/401 with every ray of Z, so P_{v_R} is PSD and lies in Z*; it therefore
      pairs nonnegatively with every element of K* (with PSD cap Z* as a PSD matrix [L: tr(AB) >= 0 for PSD A, B];
      with cone Z by the definition of Z*); its pairing with R d* R^* is 1 - c* < 0; hence R d* R^* is not in K*
      although d* is, and actT R_z(theta0) does not preserve K*.
  X7  the reachability side of the finite clause: the orbit of phi0 = (1, 2, 3i, -1+i)/4 under the lift generators
      has 384 rays and none is a product (every normalized |det Psi|^2 > 0; minimum 5/256), so no element of G384
      carries phi0 to a product state: the finite-group analogue of ReachPure fails at phi0 (NOTES-E10 F1).
  R1  positive control for ReachPure (lemma L4 of NOTES-E10, E10's code unchanged): CNOT (1 (x) W) CNOT = P0 (x) W +
      P1 (x) X W X, and the word (1 (x) W') CNOT (1 (x) W) CNOT carries a product to each of five exact pure states.
COUNTERCONTROLS (each must fail as stated).
  XC1  "(CC) holds on every pair at c' = 301/300" -- must fail (on the minimal-overlap pair): the bound is sharp at the
       pair level.
  XC2  "K* is invariant under actT R_z(theta0)" -- must fail by X6's witness.
  XC3  "the finite clause forces Q3, i.e. d* is PSD" -- must fail by X5.
DECISION RULE (fixed before run 1).  VERDICT E15-S6-EXACT-LAYER-CONSISTENT iff D1, D2, P1, P2, X1-X7 and R1 print PASS,
no FAIL is printed, XC1, XC2 and XC3 each print "COUNTER ... fails as stated", and the last line before the verdict is
"checks: 12, failures: 0".  Otherwise "VERDICT NOT RENDERED" with the failing items.  The verdict says only that the
exact items hold; it does not say that K* is self-dual (that is Theorem S' [W]), that OI supplies any cone, or anything
beyond two tokens.
"""
import re
import sys
from fractions import Fraction as Fr

KERNEL_CD = '../../../verification/lean-mathlib/OIBridge/CompositeDimension.lean'
KERNEL_KF = '../../../verification/lean-mathlib/OIBridge/KInfFoundations.lean'
RESULTS = []


def check(name, ok, detail=''):
    RESULTS.append((name, bool(ok)))
    print(('PASS ' if ok else 'FAIL ') + name + ((' -- ' + detail) if detail else ''), flush=True)


# ------------------------------------------------------------------ Gaussian rationals
Z0 = (Fr(0), Fr(0))
O1 = (Fr(1), Fr(0))
II = (Fr(0), Fr(1))


def C(a, b=0):
    return (Fr(a), Fr(b))


def cadd(x, y):
    return (x[0] + y[0], x[1] + y[1])


def csub(x, y):
    return (x[0] - y[0], x[1] - y[1])


def cmul(x, y):
    return (x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def cconj(x):
    return (x[0], -x[1])


def cscale(r, x):
    return (r * x[0], r * x[1])


def abs2(x):
    return x[0] * x[0] + x[1] * x[1]


def mmul(A, B):
    n, m, p = len(A), len(B), len(B[0])
    out = []
    for i in range(n):
        row = []
        for j in range(p):
            s = Z0
            for k in range(m):
                s = cadd(s, cmul(A[i][k], B[k][j]))
            row.append(s)
        out.append(row)
    return out


def adj(A):
    return [[cconj(A[j][i]) for j in range(len(A))] for i in range(len(A[0]))]


def mvec(A, v):
    return [cadd_all(cmul(A[i][k], v[k]) for k in range(len(v))) for i in range(len(A))]


def cadd_all(it):
    s = Z0
    for x in it:
        s = cadd(s, x)
    return s


def kron(A, B):
    return [[cmul(A[i // 2][j // 2], B[i % 2][j % 2]) for j in range(4)] for i in range(4)]


def eye(n):
    return [[O1 if i == j else Z0 for j in range(n)] for i in range(n)]


def madd(A, B):
    return [[cadd(A[i][j], B[i][j]) for j in range(len(A[0]))] for i in range(len(A))]


def msub(A, B):
    return [[csub(A[i][j], B[i][j]) for j in range(len(A[0]))] for i in range(len(A))]


def mscale(r, A):
    return [[cscale(r, A[i][j]) for j in range(len(A[0]))] for i in range(len(A))]


def trace(A):
    return cadd_all(A[i][i] for i in range(len(A)))


def inner(u, v):          # <u|v> = sum conj(u_i) v_i
    return cadd_all(cmul(cconj(u[i]), v[i]) for i in range(len(u)))


def outer(u, v):          # |u><v|
    return [[cmul(u[i], cconj(v[j])) for j in range(len(v))] for i in range(len(u))]


def key_of(M):
    return tuple(x for row in M for x in row)


# ------------------------------------------------------------------ the kernel's cnot, rotFun and cycEquiv, parsed
def parse_table(src, name):
    m = re.search(r'def %s : Fin 4 → Fin 4 → Fin 4\n((?:  \|.*\n)+)' % name, src)
    entries = re.findall(r'(\d), (\d) => (\d)', m.group(1))
    T = {(int(a), int(b)): int(c) for a, b, c in entries}
    assert len(T) == 16
    return T


def parse_sgn(src):
    m = re.search(r'def sgn \(μ ν : Fin 4\) : ℝ := if \(μ = (\d) ∧ ν = (\d)\) ∨ \(μ = (\d) ∧ ν = (\d)\) then -1 else 1', src)
    neg = {(int(m.group(1)), int(m.group(2))), (int(m.group(3)), int(m.group(4)))}
    return {(a, b): (-1 if (a, b) in neg else 1) for a in range(4) for b in range(4)}


src_cd = open(KERNEL_CD, encoding='utf-8').read()
src_kf = open(KERNEL_KF, encoding='utf-8').read()
PC, PT, SGN = parse_table(src_cd, 'pc'), parse_table(src_cd, 'pt'), parse_sgn(src_cd)
m_cyc = re.search(r'noncomputable def cycEquiv : \(Fin 3 → ℝ\) ≃ₗ\[ℝ\] \(Fin 3 → ℝ\) where\n  toFun v := !\[v (\d), v (\d), v (\d)\]', src_kf)
CYC_SRC = [int(m_cyc.group(k)) for k in (1, 2, 3)]          # (cyc v) i = v (CYC_SRC[i])
ROT_OK = all(s in src_kf for s in ('rotFun t v 0 = Real.cos t * v 0 - Real.sin t * v 1 ∧',
                                    'rotFun t v 1 = Real.sin t * v 0 + Real.cos t * v 1 ∧ rotFun t v 2 = v 2'))
print('parsed: pc, pt, sgn (16 entries each); cycEquiv v = (v %d, v %d, v %d); rotFun_apply lines found: %s'
      % (CYC_SRC[0], CYC_SRC[1], CYC_SRC[2], ROT_OK), flush=True)


def cyc_matrix():
    return [[Fr(1) if CYC_SRC[i] == j else Fr(0) for j in range(3)] for i in range(3)]


def rot_matrix(c, s):
    return [[c, -s, Fr(0)], [s, c, Fr(0)], [Fr(0), Fr(0), Fr(1)]]


# ------------------------------------------------------------------ the dictionary
S0m = [[O1, Z0], [Z0, O1]]
SX = [[Z0, O1], [O1, Z0]]
SY = [[Z0, C(0, -1)], [II, Z0]]
SZ = [[O1, Z0], [Z0, C(-1)]]
SIG = [S0m, SX, SY, SZ]
T = [[kron(SIG[m], SIG[n]) for n in range(4)] for m in range(4)]


def dict_of(w):
    H = [[Z0] * 4 for _ in range(4)]
    for m in range(4):
        for n in range(4):
            if w[m][n] != 0:
                H = madd(H, mscale(Fr(w[m][n]) / 4, T[m][n]))
    return H


def coord_of(H):
    out = []
    for m in range(4):
        row = []
        for n in range(4):
            t = trace(mmul(T[m][n], H))
            assert t[1] == 0
            row.append(t[0])
        out.append(row)
    return out


def actT_table(N3, w):
    H = [[Fr(1), Fr(0), Fr(0), Fr(0)]] + [[Fr(0)] + list(N3[i]) for i in range(3)]
    return [[sum(H[n][k] * w[m][k] for k in range(4)) for n in range(4)] for m in range(4)]


def cnot_table(w):
    return [[SGN[(m, n)] * w[PC[(m, n)]][PT[(m, n)]] for n in range(4)] for m in range(4)]


def basis_table(m, n):
    return [[Fr(1) if (a, b) == (m, n) else Fr(0) for b in range(4)] for a in range(4)]


P0 = [[O1, Z0], [Z0, Z0]]
P1 = [[Z0, Z0], [Z0, O1]]
CNOT = madd(kron(P0, S0m), kron(P1, SX))
UJ = mscale(Fr(1, 2), msub(S0m, [[cmul(II, x) for x in row] for row in madd(madd(SX, SY), SZ)]))
L_RZ90 = kron(S0m, [[O1, Z0], [Z0, II]])
L_CYC = kron(S0m, UJ)
L_RTH = kron(S0m, [[O1, Z0], [Z0, C(Fr(3, 5), Fr(4, 5))]])


def ad_matches(table_map, U):
    for m in range(4):
        for n in range(4):
            w = basis_table(m, n)
            lhs = dict_of(table_map(w))
            rhs = mmul(mmul(U, dict_of(w)), adj(U))
            if lhs != rhs:
                return False
    return mmul(U, adj(U)) == eye(4)


ok_d1 = ROT_OK and all([
    ad_matches(cnot_table, CNOT),
    ad_matches(lambda w: actT_table(rot_matrix(Fr(0), Fr(1)), w), L_RZ90),
    ad_matches(lambda w: actT_table(cyc_matrix(), w), L_CYC),
    ad_matches(lambda w: actT_table(rot_matrix(Fr(3, 5), Fr(4, 5)), w), L_RTH)])
check('D1', ok_d1, 'parsed cnot = Ad(CNOT); actT R_z(pi/2) = Ad(1 (x) diag(1, i)); actT cyc3 = Ad(1 (x) (I - i(X+Y+Z))/2); '
      'actT R_z(theta0) = Ad(1 (x) diag(1, (3+4i)/5)); all four lifts unitary')


# ------------------------------------------------------------------ D2: the table group (E10 F1's construction)
def perm_of_cnot():
    return tuple((4 * PC[(m, n)] + PT[(m, n)], SGN[(m, n)]) for m in range(4) for n in range(4))


def perm_of_actT(M3):
    H = [[1, 0, 0, 0]] + [[0] + [int(M3[i][j]) for j in range(3)] for i in range(3)]
    out = []
    for m in range(4):
        for n in range(4):
            nz = [(k, H[n][k]) for k in range(4) if H[n][k] != 0]
            assert len(nz) == 1 and nz[0][1] in (1, -1)
            out.append((4 * m + nz[0][0], nz[0][1]))
    return tuple(out)


def compose(p, q):
    return tuple((q[s][0], sg * q[s][1]) for (s, sg) in p)


gens_tab = [perm_of_cnot(), perm_of_actT(rot_matrix(Fr(0), Fr(1))), perm_of_actT(cyc_matrix())]
ident = tuple((i, 1) for i in range(16))
seen = {ident}
frontier = [ident]
while frontier:
    nxt = []
    for g in frontier:
        for h in gens_tab:
            k = compose(h, g)
            if k not in seen:
                seen.add(k)
                nxt.append(k)
    frontier = nxt
check('D2', len(seen) == 384, 'the table group <cnot, actT R_z(pi/2), actT cyc3> has order %d' % len(seen))


# ------------------------------------------------------------------ P1, P2: the positive control Q3
def is_psd_herm(H):
    """exact PSD test for a Hermitian 4 x 4 Gaussian-rational matrix: every principal minor >= 0"""
    import itertools
    for r in range(1, 5):
        for idx in itertools.combinations(range(4), r):
            sub = [[H[i][j] for j in idx] for i in idx]
            d = det_c(sub)
            if d[1] != 0 or d[0] < 0:
                return False
    return True


def det_c(M):
    n = len(M)
    if n == 1:
        return M[0][0]
    s = Z0
    for j in range(n):
        minor = [row[:j] + row[j + 1:] for row in M[1:]]
        term = cmul(M[0][j], det_c(minor))
        s = cadd(s, term) if j % 2 == 0 else csub(s, term)
    return s


def hom(x):
    return [Fr(1)] + [Fr(t) for t in x]


def prod_table(x, y):
    hx, hy = hom(x), hom(y)
    return [[hx[m] * hy[n] for n in range(4)] for m in range(4)]


def bloch(x):
    return mscale(Fr(1, 2), madd(madd(S0m, mscale(Fr(x[0]), SX)), madd(mscale(Fr(x[1]), SY), mscale(Fr(x[2]), SZ))))


ball_pts = [(Fr(3, 5), Fr(4, 5), Fr(0)), (Fr(0), Fr(0), Fr(1)), (Fr(1, 3), Fr(-2, 3), Fr(2, 3)), (Fr(1, 2), Fr(0), Fr(0)),
            (Fr(-2, 7), Fr(3, 7), Fr(-6, 7)), (Fr(0), Fr(0), Fr(0))]
ok_p1 = True
for x in ball_pts:
    for y in ball_pts:
        Hxy = dict_of(prod_table(x, y))
        if not (is_psd_herm(Hxy) and Hxy == kron(bloch(x), bloch(y))):
            ok_p1 = False
check('P1', ok_p1, 'dict(prodState x y) = rho_x (x) rho_y and PSD for all 36 pairs of six rational ball points')
Abad = dict_of([[Fr(1) if (a, b) == (0, 0) else Fr(0) for b in range(4)] for a in range(4)])
Abad = madd(Abad, mscale(Fr(-2, 1), outer([O1, Z0, Z0, O1], [O1, Z0, Z0, O1])))       # I/4 - 2 |00+11><00+11|
vpure = [O1, Z0, Z0, O1]
pair_bad = trace(mmul(Abad, outer(vpure, vpure)))
Apsd = outer([C(1), C(2), C(0, 1), C(-1, 1)], [C(1), C(2), C(0, 1), C(-1, 1)])
Bpsd = outer([C(0, 1), C(1), C(3), C(1, -2)], [C(0, 1), C(1), C(3), C(1, -2)])
pair_ok = trace(mmul(Apsd, Bpsd))
check('P2', (not is_psd_herm(Abad)) and pair_bad[0] < 0 and pair_bad[1] == 0 and pair_ok[0] >= 0 and pair_ok[1] == 0,
      'a non-PSD table pairs %s with the pure Bell table; a PSD pair pairs %s' % (pair_bad[0], pair_ok[0]))


# ------------------------------------------------------------------ orbits of rays under the lift generators
LIFTS = [CNOT, L_RZ90, L_CYC]


def ray_orbit(v0):
    k0 = key_of(outer(v0, v0))
    vecs = {k0: v0}
    frontier = [v0]
    while frontier:
        nxt = []
        for v in frontier:
            for U in LIFTS:
                w = mvec(U, v)
                k = key_of(outer(w, w))
                if k not in vecs:
                    vecs[k] = w
                    nxt.append(w)
        frontier = nxt
    closed = all(key_of(outer(mvec(U, v), mvec(U, v))) in vecs for v in vecs.values() for U in LIFTS)
    return list(vecs.values()), closed


def ndet2(v):
    """normalized |det Psi|^2 of the coefficient matrix [[v0, v1], [v2, v3]]"""
    n2 = sum(abs2(x) for x in v)
    return abs2(csub(cmul(v[0], v[3]), cmul(v[1], v[2]))) / (n2 * n2)


H_STAR = [C(10), C(2, -2), C(-1, -3), C(3, -1)]
NH = sum(abs2(x) for x in H_STAR)
CSTAR = Fr(401, 400)
orb, closed = ray_orbit(H_STAR)
check('X1', len(orb) == 192 and closed and NH == 128,
      'the orbit of the ray of h* has %d rays, closed under the three lift generators; |h*|^2 = %s' % (len(orb), NH))

s_min, s_max = None, None
pair_pos = True
n_pairs = 0
min_pair = None
for j in range(len(orb)):
    for k in range(j + 1, len(orb)):
        s = abs2(inner(orb[j], orb[k])) / (NH * NH)
        n_pairs += 1
        if s_min is None or s < s_min:
            s_min, min_pair = s, (j, k)
        if s_max is None or s > s_max:
            s_max = s
        if not (4 - 2 * CSTAR + CSTAR * CSTAR * s > 0):
            pair_pos = False
check('X2', n_pairs == 18336 and s_min == Fr(25, 2048) and s_max == Fr(13, 16) and pair_pos,
      '%d pairs; squared overlaps in [%s, %s]; every tr(d_j d_k) > 0' % (n_pairs, s_min, s_max))

D_list = [ndet2(v) for v in orb]
bound = (2 / CSTAR - 1) ** 2
ok_h1 = all(1 - 4 * D <= bound for D in D_list)
check('X3', ok_h1 and min(D_list) == Fr(85, 2048),
      'H1 for every defect at c* = 401/400 (1 - 4D <= (2/c* - 1)^2 = %s); minimum normalized |det Psi|^2 = %s'
      % (bound, min(D_list)))

cc = lambda c, s: c * c * s >= 4 * (c - 1)
ok_cc = s_min is not None and all(
    cc(CSTAR, abs2(inner(orb[j], orb[k])) / (NH * NH)) for j in range(len(orb)) for k in range(j + 1, len(orb)))
check('X4', ok_cc, '(CC) c*^2 s >= 4(c* - 1) on all %d pairs (threshold s >= %s)' % (n_pairs, 4 * (CSTAR - 1) / CSTAR ** 2))

P_star = mscale(Fr(1, 128), outer(H_STAR, H_STAR))
d_star = msub(eye(4), mscale(CSTAR, P_star))
val = inner(H_STAR, mvec(d_star, H_STAR))
val = (val[0] / 128, val[1] / 128)
z_star = [[(Fr(1, 2) if (m, n) == (0, 0) else Fr(0)) - CSTAR / 8 * cst for n, cst in enumerate(row)]
          for m, row in enumerate(coord_of(P_star))]
ok_x5 = val == (1 - CSTAR, Fr(0)) and val[0] < 0 and dict_of(z_star) == mscale(Fr(1, 8), d_star)
check('X5', ok_x5, '<h*| d* |h*> = %s < 0, so d* is not PSD; dict(z*) = d*/8' % val[0])

v_R = mvec(L_RTH, H_STAR)
ov = [abs2(inner(v_R, v)) / (NH * NH) for v in orb]
P_R = mscale(Fr(1, 128), outer(v_R, v_R))
Rd = mmul(mmul(L_RTH, d_star), adj(L_RTH))
pair_R = trace(mmul(P_R, Rd))
ok_x6 = max(ov) <= 1 / CSTAR and pair_R == (1 - CSTAR, Fr(0)) and is_psd_herm(mscale(Fr(128), P_R))
check('X6', ok_x6, 'max squared overlap of R h* with the 192 rays = %s <= 400/401; <P_{Rh*}, R d* R^*> = %s < 0'
      % (max(ov), pair_R[0]))

PHI0 = [C(1), C(2), C(0, 3), C(-1, 1)]
orb0, closed0 = ray_orbit(PHI0)
dets0 = [ndet2(v) for v in orb0]
check('X7', len(orb0) == 384 and closed0 and min(dets0) > 0 and min(dets0) == Fr(5, 256),
      'the orbit of phi0 has %d rays, none a product; minimum normalized |det Psi|^2 = %s' % (len(orb0), min(dets0)))

# ------------------------------------------------------------------ R1: L4 of NOTES-E10 (E10's code, unchanged)
import sympy as sp

R = sp.Rational
I = sp.I
s0 = sp.eye(2)
sx = sp.Matrix([[0, 1], [1, 0]])
K4 = sp.kronecker_product
P0s = sp.Matrix([[1, 0], [0, 0]])
P1s = sp.Matrix([[0, 0], [0, 1]])
CNOTs = K4(P0s, s0) + K4(P1s, sx)
W = sp.Matrix(2, 2, sp.symbols('w0:4'))
ok_b1 = sp.simplify(CNOTs * K4(s0, W) * CNOTs - (K4(P0s, W) + K4(P1s, sx * W * sx))) == sp.zeros(4, 4)


def w_from_axis(n):
    """a unitary W with W (n . s) W^* = s_x (so W^* s_x W = n . s), from the eigenvectors of n . s and of s_x"""
    a_plus = sp.Matrix([n[2] + 1, n[0] + I * n[1]])
    a_plus = a_plus / sp.sqrt(sp.expand((a_plus.H * a_plus)[0, 0]))
    a_minus = sp.Matrix([-sp.conjugate(a_plus[1]), sp.conjugate(a_plus[0])])
    b_plus = sp.Matrix([1, 1]) / sp.sqrt(2)
    b_minus = sp.Matrix([1, -1]) / sp.sqrt(2)
    return (b_plus * a_plus.H + b_minus * a_minus.H).applyfunc(sp.expand)


def reach(psi):
    psi = sp.Matrix(psi)
    nrm = sp.sqrt(sp.expand((psi.H * psi)[0, 0]))
    psi = (psi / nrm).applyfunc(sp.expand)
    x = sp.Matrix([psi[0], psi[1]])
    y = sp.Matrix([psi[2], psi[3]])
    a = sp.sqrt(sp.expand((x.H * x)[0, 0]))
    b = sp.sqrt(sp.expand((y.H * y)[0, 0]))
    ket0 = sp.Matrix([1, 0])
    ket1 = sp.Matrix([0, 1])
    if b == 0 or a == 0:
        v = x / a if b == 0 else y / b
        Wp = sp.Matrix.hstack(v, sp.Matrix([-sp.conjugate(v[1]), sp.conjugate(v[0])]))
        Wm = s0
        c = ket0 if b == 0 else ket1
    else:
        xh, yh = x / a, y / b
        kappa = sp.expand((xh.H * yh)[0, 0])
        n = (sp.re(kappa), -sp.im(kappa), sp.sqrt(sp.expand(1 - kappa * sp.conjugate(kappa))))
        Wm = w_from_axis(n)
        u = Wm * ket0
        v = sx * Wm * ket1
        Wp = (sp.Matrix.hstack(xh, yh) * sp.Matrix.hstack(u, v).inv()).applyfunc(sp.expand)
        c = a * ket0 + b * ket1
    start = sp.kronecker_product(c, ket0)
    g = K4(s0, Wp) * CNOTs * K4(s0, Wm) * CNOTs
    out = g * start
    rho_out = out * out.H
    rho_psi = psi * psi.H
    z4, z2 = sp.zeros(4, 4), sp.zeros(2, 2)
    ok = ((rho_out - rho_psi).applyfunc(sp.expand) == z4 and (Wp.H * Wp - s0).applyfunc(sp.expand) == z2
          and (Wm.H * Wm - s0).applyfunc(sp.expand) == z2)
    return ok


def rational_state(a, b, xh, kappa, nz):
    xh = sp.Matrix(xh)
    xperp = sp.Matrix([-sp.conjugate(xh[1]), sp.conjugate(xh[0])])
    yh = kappa * xh + nz * xperp
    return [a * xh[0], a * xh[1], b * yh[0], b * yh[1]]


states = {
    'product (3/5, 4/5) (x) |0>': [R(3, 5), R(4, 5), 0, 0],
    'Bell (|00>+|11>)': [1, 0, 0, 1],
    'kappa = (4+4i)/9, n_z = 7/9': rational_state(R(3, 5), R(4, 5), [1, 0], (4 + 4 * I) / 9, R(7, 9)),
    'kappa = 7i/25, n_z = 24/25': rational_state(R(5, 13), R(12, 13), [1, 0], 7 * I / 25, R(24, 25)),
    'kappa = 9(1+4i)/49, n_z = 32/49, x = (3/5, 4i/5)': rational_state(R(8, 17), R(15, 17), [R(3, 5), 4 * I / 5], 9 * (1 + 4 * I) / 49, R(32, 49)),
}
reach_ok = {k: reach(v) for k, v in states.items()}
check('R1', ok_b1 and all(reach_ok.values()),
      'CNOT (1 (x) W) CNOT = P0 (x) W + P1 (x) X W X; the L4 word reaches all five states: %s' % all(reach_ok.values()))

# ------------------------------------------------------------------ countercontrols
counters = []
j0, k0 = min_pair
c_prime = Fr(301, 300)
xc1_claim = all(cc(c_prime, abs2(inner(orb[j], orb[k])) / (NH * NH)) for j in range(len(orb)) for k in range(j + 1, len(orb)))
xc1_fail_at_min = not cc(c_prime, abs2(inner(orb[j0], orb[k0])) / (NH * NH))
counters.append(('XC1', (not xc1_claim) and xc1_fail_at_min,
                 '(CC) at 301/300 fails on the minimal-overlap pair (s = %s < %s)'
                 % (s_min, 4 * (c_prime - 1) / c_prime ** 2)))
xc2_claim = pair_R[0] >= 0      # an element of K* invariant images would pair nonnegatively with P_{Rh*}
counters.append(('XC2', (not xc2_claim) and ok_x6, 'R d* R^* pairs %s with P_{Rh*}, an element of K*' % pair_R[0]))
xc3_claim = is_psd_herm(mscale(Fr(400), d_star))
counters.append(('XC3', not xc3_claim, 'd* is not PSD (<h*|d*|h*> = %s)' % val[0]))
for name, failed_as_stated, detail in counters:
    print(('COUNTER %s fails as stated' % name) if failed_as_stated else ('COUNTER %s DID NOT FAIL' % name),
          '--', detail, flush=True)

nfail = sum(1 for _, ok in RESULTS if not ok)
print('checks: %d, failures: %d' % (len(RESULTS), nfail), flush=True)
if nfail == 0 and len(RESULTS) == 12 and all(c[1] for c in counters):
    print('VERDICT E15-S6-EXACT-LAYER-CONSISTENT')
else:
    bad = [n for n, ok in RESULTS if not ok] + [c[0] for c in counters if not c[1]]
    print('VERDICT NOT RENDERED -- failing: %s' % bad)
sys.exit(0)
