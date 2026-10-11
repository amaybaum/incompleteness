"""E19 probe -- the countercontrol family of draft S6 against the design-built Theorem S' (HO-30), the G768 cone (HO-31)
and the Clifford cone (HO-32) recomputed; the group the clause generates; Theorem C19-1 (a) and the product identity
the block module uses, on exact instances.  (exact: Gaussian rationals as pairs of Fractions; no floating point)

S0 (written 2026-10-11T07:41Z by `date -u`, before run 1; predictions in NOTES-E19.md S0).

SETTING (kernel vocabulary at L = 9f9f8257).  W 3 = 4 x 4 real tables w[mu][nu], mu the control token, nu the target
token (CompositeDimension.lean:97); actT N acts on the target index by (1 (+) N) (:198), actC N on the control index
(:201).  The kernel's cnot is the signed permutation cnotFun (pc, pt, sgn) and is PARSED here; rotFun (KInfFoundations
.lean, the lines of rotFun_apply), cycEquiv (:416) and nflip (CompositeDimension.lean:797, `![1, -1, -1]`) are PARSED.
The dictionary is EqvK2Schema's: dict w = (1/4) sum w[mu][nu] s_mu (x) s_nu, control first.  Lifts (D1): cnot =
Ad(CNOT), actT R_z(pi/2) = Ad(1 (x) S), actT cyc3 = Ad(1 (x) U_J), actC nflip = Ad(X (x) 1), actC R_z(pi/2) =
Ad(S (x) 1), actC cyc3 = Ad(U_J (x) 1).  A cone of the family is K(Z) = (PSD cap Z*) + cone Z with Z the orbit of the
defect d = I - c P_h under a group of lifts; its self-duality is Theorem S' in the finite form of the countermodels
thread's design module CmSprime (HO-30 item 1, `theorem_Sprime_ineq`, [D]), whose hypotheses are: unit seeds; c in (1, 2];
c < card n = 4; pairwise nonnegative trace pairings pr(d_j, d_k) = 4 - 2c + c^2 s_jk (all j, k, j = k included); and, on
every ordered pair j != k with positive pairing, (sqrt(c_j - 1) + sqrt(c_k - 1))^2 <= c_j c_k s_jk, which for a common c
is 4(c - 1) <= c^2 s_jk.  This probe checks those hypotheses exactly for each finite cone; it does NOT check S' itself.
Unit seeds: a seed h with |h|^2 = Q rational is unit after division by sqrt(Q); the hypotheses below the unit clause are
homogeneous in the seed, so they are checked on the unnormalised vectors (s_jk = |<h_j|h_k>|^2 / (|h_j|^2 |h_k|^2)).
ORBIT REDUCTION (used for KC and verified exactly on K384): for a group orbit {g h}, the set of pairwise squared overlaps
{s(g h, g' h)} equals the set {s(h, v) : v a ray of the orbit, v != ray(h)}, since s(g h, g' h) = s(h, g^{-1} g' h) for
unitary g, g' and g^{-1} g' h is a ray of the orbit.

CHECKS.
  D1  the six lifts above on all 16 basis tables through the dictionary; each lift unitary exactly.
  K1  K384 (HO-24's cone; S6's countercontrol K*): |h*|^2 = 128 (unit seed after division by sqrt 128); c = 401/400 in
      (1, 2] and < 4; the orbit of h* = (10, 2-2i, -1-3i, 3-i) under <CNOT, 1 (x) S, 1 (x) U_J> has 192 rays; on all
      18336 pairs the pairing 4 - 2c + c^2 s is positive and 4(c - 1) <= c^2 s; the diagonal pairing 4 - 2c + c^2 > 0;
      the set of pairwise overlaps equals the set of seed-vs-orbit overlaps (the orbit reduction, exact).
  K2  K768 (HO-31 item 2's cone): the group <cnot, actT S, actT J, actC nflip> of table maps has order 768; the orbit of
      h* under its lifts has 384 rays (stabilizer 2); the image of h* under X (x) 1 is not a ray of the 192-orbit (so
      actC nflip moves K384's defect set); no product (minimum normalised |det Psi|^2 = 85/2048); minimum and maximum
      squared overlap over all 73536 pairs; at c = 10001/10000: c in (1, 2], c < 4, H1 (1 - 4 D_min <= (2/c - 1)^2),
      every pairing positive, 4(c - 1) <= c^2 s on every pair.
  K3  KC (HO-32's Clifford cone, C15.2's seed h_C = (-480+7i, 357+870i, 939+834i, 448+486i), c = 100001/100000): the
      group <cnot, actT S, actT J, actC S, actT ... actC J> of table maps has order 11520; the orbit of h_C has 11520
      rays (trivial stabilizer); the minimum normalised |det Psi|^2 over the orbit is positive; the minimum and maximum
      seed-vs-orbit overlap (by the orbit reduction, the pairwise extremes); c in (1, 2], c < 4; H1; the pairing at the
      minimum overlap positive; 4(c - 1) <= c^2 s_min.
  K4  the group the clause generates (part (ii) of E19): every one of the 384 lifted matrices of G384 commutes with
      Z (x) 1, is block-diagonal P0 (x) U0 + P1 (x) U1, and has det U0 / det U1 in {1, -1}; the generators have ratios
      -1 (CNOT), 1 (1 (x) S), 1 (1 (x) U_J); the two-reflection construction on exact instances: with
      U_n = diag((3-4i)/5, (3+4i)/5), U_n X U_n^dag = n . sigma for n = (-7/25, 24/25, 0), and (U_n (x) ... ) --
      explicitly (1 (x) U_n) CNOT (1 (x) U_n)^dag = P0 (x) 1 + P1 (x) (n . sigma); the product of two such reflections is
      a block pair (1, R) with R in SU(2) of trace 2 n.m; the word (1 (x) U_J) . [(1 (x) U_n) CNOT (1 (x) U_n)^dag] .
      [(1 (x) U_m) CNOT (1 (x) U_m)^dag] equals the block pair (U_J, R U_J) up to a global phase, with U_m = U_J (so that
      m . sigma = U_J X U_J^dag); the controlled phase P0 (x) 1 + P1 (x) diag(1, i) has det ratio -i, outside {1, -1}.
  K5  Theorem C19-1 (a) on exact instances: for psi = |0> (x) a + |1> (x) b with Gaussian-rational a, b, the matrix
      M0 = [[conj a0, conj a1], [-a1, a0]] satisfies M0 a = (|a|^2, 0), M0 M0^dag = |a|^2 I and det M0 = |a|^2 (so
      M0/|a| is in SU(2)); with M1 from b, (M0 (+) M1) psi = (|a|^2, 0, |b|^2, 0), whose 2 x 2 reshaping has
      determinant 0 (a product); six instances including phi0 = (1, 2, 3i, -1+i), (3, 4i, 0, 5) and the edge cases
      a = 0, b = 0.
  K6  the product identity of the block module: for alpha, beta >= 0 rational with c = alpha^2 + beta^2 and
      x0 = (2 alpha beta, 0, alpha^2 - beta^2)/c (x0 = 0 when c = 0): x0 lies in eball 3 exactly, and
      c . dict(prodState x0 e3) = y y^dag for y = (alpha, 0, beta, 0); five instances including (0, 0), (1, 0), (0, 1).
  K7  the C21 safeguard for K768: d = I - c P_{h*} is not PSD (<h*|d|h*> = (1 - c)|h*|^2 < 0), so K768 != Q3; and with
      R = 1 (x) diag(1, (3+4i)/5) (D1: actT R_z(theta0)), R h* has squared overlap at most 1/c with every ray of the
      384-orbit, so P_{R h*} lies in PSD cap Z* and pairs (1 - c) < 0 with R d R^dag: the rotation with cos t = 3/5
      does not preserve K768 (the witness needs neither S' nor ReachPure).
COUNTERCONTROLS (each must fail as stated).
  XK1  "4(c' - 1) <= c'^2 s on every pair of K384 at c' = 301/300" -- must fail on the minimal-overlap pair.
  XK2  "4(c' - 1) <= c'^2 s on every pair of K768 at c' = 101/100" -- must fail on the minimal-overlap pair.
  XK3  "the controlled phase P0 (x) 1 + P1 (x) diag(1, i) is a word in the three generators" -- must fail: its det
       ratio is -i while every word has ratio +-1 (K4's invariant; checked by the invariant, not by enumeration).
  XK4  "M0 = [[conj a0, conj a1], [-a1, a0]] is unitary without normalisation" -- must fail at a = (3, 4i).
DECISION RULE (fixed before run 1).  VERDICT E19-S6-CONTROLS-EXACT iff D1 and K1-K7 print PASS, no FAIL is printed,
XK1-XK4 each print "COUNTER ... fails as stated", and the last line before the verdict is "checks: 8, failures: 0".
Otherwise "VERDICT NOT RENDERED" with the failing items.  The verdict says only that the exact items hold: it does not
say that any cone is self-dual (that is S' [D]), that OI supplies any cone or operation, that any operation is
available, or anything beyond two tokens.
"""
import itertools
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


def cdiv(x, y):
    d = y[0] * y[0] + y[1] * y[1]
    t = cmul(x, cconj(y))
    return (t[0] / d, t[1] / d)


def cscale(r, x):
    return (r * x[0], r * x[1])


def abs2(x):
    return x[0] * x[0] + x[1] * x[1]


def cadd_all(it):
    s = Z0
    for x in it:
        s = cadd(s, x)
    return s


def mmul(A, B):
    n, m, p = len(A), len(B), len(B[0])
    return [[cadd_all(cmul(A[i][k], B[k][j]) for k in range(m)) for j in range(p)] for i in range(n)]


def adj(A):
    return [[cconj(A[j][i]) for j in range(len(A))] for i in range(len(A[0]))]


def mvec(A, v):
    return [cadd_all(cmul(A[i][k], v[k]) for k in range(len(v))) for i in range(len(A))]


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


def mcscale(z, A):
    return [[cmul(z, A[i][j]) for j in range(len(A[0]))] for i in range(len(A))]


def trace(A):
    return cadd_all(A[i][i] for i in range(len(A)))


def inner(u, v):
    return cadd_all(cmul(cconj(u[i]), v[i]) for i in range(len(u)))


def norm2(v):
    return sum(abs2(x) for x in v)


def outer(u, v):
    return [[cmul(u[i], cconj(v[j])) for j in range(len(v))] for i in range(len(u))]


def det2(M):
    return csub(cmul(M[0][0], M[1][1]), cmul(M[0][1], M[1][0]))


def canon(v):
    k = next(t for t in range(len(v)) if v[t] != Z0)
    a = v[k]
    return tuple(cdiv(x, a) for x in v)


def s_of(u, v):
    return abs2(inner(u, v)) / (norm2(u) * norm2(v))


def det_norm(v):
    """normalised |det Psi|^2 of the 2 x 2 reshaping (control index first)"""
    return abs2(csub(cmul(v[0], v[3]), cmul(v[1], v[2]))) / (norm2(v) ** 2)


# ------------------------------------------------------------------ the kernel's cnot, rotFun, cycEquiv, nflip, parsed
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
CYC_SRC = [int(m_cyc.group(k)) for k in (1, 2, 3)]
ROT_OK = all(s in src_kf for s in ('rotFun t v 0 = Real.cos t * v 0 - Real.sin t * v 1 ∧',
                                    'rotFun t v 1 = Real.sin t * v 0 + Real.cos t * v 1 ∧ rotFun t v 2 = v 2'))
m_nf = re.search(r'def nflip : \(Fin 3 → ℝ\) →ₗ\[ℝ\] \(Fin 3 → ℝ\) where\n  toFun x := fun i => \(!\[(-?1), (-?1), (-?1)\] : Fin 3 → ℝ\) i \* x i', src_cd)
NFLIP = [int(m_nf.group(k)) for k in (1, 2, 3)]
print('parsed: pc, pt, sgn (16 entries each); cycEquiv v = (v %d, v %d, v %d); nflip = diag%s; rotFun_apply lines found: %s'
      % (CYC_SRC[0], CYC_SRC[1], CYC_SRC[2], tuple(NFLIP), ROT_OK), flush=True)


def cyc_matrix():
    return [[Fr(1) if CYC_SRC[i] == j else Fr(0) for j in range(3)] for i in range(3)]


def rot_matrix(c, s):
    return [[c, -s, Fr(0)], [s, c, Fr(0)], [Fr(0), Fr(0), Fr(1)]]


def nflip_matrix():
    return [[Fr(NFLIP[i]) if i == j else Fr(0) for j in range(3)] for i in range(3)]


def homog(N3):
    return [[Fr(1), Fr(0), Fr(0), Fr(0)]] + [[Fr(0)] + list(N3[i]) for i in range(3)]


def actT_table(N3, w):
    H = homog(N3)
    return [[sum(H[n][k] * w[m][k] for k in range(4)) for n in range(4)] for m in range(4)]


def actC_table(N3, w):
    H = homog(N3)
    return [[sum(H[m][k] * w[k][n] for k in range(4)) for n in range(4)] for m in range(4)]


def cnot_table(w):
    return [[SGN[(m, n)] * w[PC[(m, n)]][PT[(m, n)]] for n in range(4)] for m in range(4)]


def basis_table(m, n):
    return [[Fr(1) if (a, b) == (m, n) else Fr(0) for b in range(4)] for a in range(4)]


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


P0 = [[O1, Z0], [Z0, Z0]]
P1 = [[Z0, Z0], [Z0, O1]]
CNOT = madd(kron(P0, S0m), kron(P1, SX))
SPH = [[O1, Z0], [Z0, II]]
UJ = mscale(Fr(1, 2), msub(S0m, mcscale(II, madd(madd(SX, SY), SZ))))
L_TS, L_TJ, L_CX, L_CS, L_CJ = kron(S0m, SPH), kron(S0m, UJ), kron(SX, S0m), kron(SPH, S0m), kron(UJ, S0m)
L_RTH = kron(S0m, [[O1, Z0], [Z0, C(Fr(3, 5), Fr(4, 5))]])


def ad_matches(table_map, U):
    for m in range(4):
        for n in range(4):
            w = basis_table(m, n)
            if dict_of(table_map(w)) != mmul(mmul(U, dict_of(w)), adj(U)):
                return False
    return mmul(U, adj(U)) == eye(4)


ok_d1 = ROT_OK and all([
    ad_matches(cnot_table, CNOT),
    ad_matches(lambda w: actT_table(rot_matrix(Fr(0), Fr(1)), w), L_TS),
    ad_matches(lambda w: actT_table(cyc_matrix(), w), L_TJ),
    ad_matches(lambda w: actC_table(nflip_matrix(), w), L_CX),
    ad_matches(lambda w: actC_table(rot_matrix(Fr(0), Fr(1)), w), L_CS),
    ad_matches(lambda w: actC_table(cyc_matrix(), w), L_CJ),
    ad_matches(lambda w: actT_table(rot_matrix(Fr(3, 5), Fr(4, 5)), w), L_RTH)])
check('D1', ok_d1, 'parsed cnot = Ad(CNOT); actT R_z(pi/2) = Ad(1 (x) S); actT cyc3 = Ad(1 (x) U_J); actC nflip = Ad(X (x) 1); '
      'actC R_z(pi/2) = Ad(S (x) 1); actC cyc3 = Ad(U_J (x) 1); actT R_z(theta0) = Ad(1 (x) diag(1, (3+4i)/5)); all unitary')


# ------------------------------------------------------------------ signed permutations of the 16 table coordinates
def perm_of_cnot():
    return tuple((4 * PC[(m, n)] + PT[(m, n)], SGN[(m, n)]) for m in range(4) for n in range(4))


def perm_of_act(M3, side):
    H = [[1, 0, 0, 0]] + [[0] + [int(M3[i][j]) for j in range(3)] for i in range(3)]
    out = []
    for m in range(4):
        for n in range(4):
            if side == 'T':
                nz = [(k, H[n][k]) for k in range(4) if H[n][k] != 0]
                assert len(nz) == 1 and nz[0][1] in (1, -1)
                out.append((4 * m + nz[0][0], nz[0][1]))
            else:
                nz = [(k, H[m][k]) for k in range(4) if H[m][k] != 0]
                assert len(nz) == 1 and nz[0][1] in (1, -1)
                out.append((4 * nz[0][0] + n, nz[0][1]))
    return tuple(out)


def compose(p, q):
    return tuple((q[s][0], sg * q[s][1]) for (s, sg) in p)


IDENT = tuple((i, 1) for i in range(16))


def group_closure(gens):
    seen = {IDENT}
    frontier = [IDENT]
    while frontier:
        nxt = []
        for g in frontier:
            for h in gens:
                k = compose(h, g)
                if k not in seen:
                    seen.add(k)
                    nxt.append(k)
        frontier = nxt
    return seen


SP = {'cnot': perm_of_cnot(), 'TS': perm_of_act(rot_matrix(Fr(0), Fr(1)), 'T'), 'TJ': perm_of_act(cyc_matrix(), 'T'),
      'CX': perm_of_act(nflip_matrix(), 'C'), 'CS': perm_of_act(rot_matrix(Fr(0), Fr(1)), 'C'),
      'CJ': perm_of_act(cyc_matrix(), 'C')}


def orbit_rays(h, lifts):
    start = canon(h)
    seen = {start}
    frontier = [list(start)]
    while frontier:
        nxt = []
        for v in frontier:
            for U in lifts:
                w = canon(mvec(U, v))
                if w not in seen:
                    seen.add(w)
                    nxt.append(list(w))
        frontier = nxt
    return [list(v) for v in seen]


def sprime_hyps(rays, c, pairs_all=True, seed=None):
    """the hypotheses of theorem_Sprime_ineq for a common c on an orbit of rays; returns a dict of exact facts"""
    n = len(rays)
    pairing_diag = 4 - 2 * c + c * c
    if pairs_all:
        vals = []
        for i in range(n):
            for j in range(i + 1, n):
                vals.append(s_of(rays[i], rays[j]))
        smin, smax = min(vals), max(vals)
        npairs = len(vals)
    else:
        hc = canon(seed)
        vals = [s_of(seed, v) for v in rays if tuple(v) != hc]
        smin, smax = min(vals), max(vals)
        npairs = len(vals)
    pair_pos = (4 - 2 * c + c * c * smin > 0) and pairing_diag > 0
    cc = c * c * smin >= 4 * (c - 1)
    dmin = min(det_norm(v) for v in rays)
    h1 = 1 - 4 * dmin <= (2 / c - 1) ** 2
    return {'n': n, 'npairs': npairs, 'smin': smin, 'smax': smax, 'pair_pos': pair_pos, 'cc': cc, 'dmin': dmin,
            'h1': h1, 'c_ok': 1 < c <= 2 and c < 4, 'vals': vals}


# ------------------------------------------------------------------ K1: K384
hstar = [C(10), C(2, -2), C(-1, -3), C(3, -1)]
gens384 = [CNOT, L_TS, L_TJ]
orb384 = orbit_rays(hstar, gens384)
c384 = Fr(401, 400)
r1 = sprime_hyps(orb384, c384, pairs_all=True)
r1s = sprime_hyps(orb384, c384, pairs_all=False, seed=hstar)
reduction_ok = set(r1['vals']) == set(r1s['vals'])
k1 = (norm2(hstar) == 128 and r1['n'] == 192 and r1['npairs'] == 18336 and r1['c_ok'] and r1['pair_pos'] and r1['cc']
      and r1['h1'] and reduction_ok and r1['smin'] == Fr(25, 2048) and r1['smax'] == Fr(13, 16))
check('K1', k1, 'K384 against theorem_Sprime_ineq at c = 401/400: |h*|^2 = %d, %d rays, %d pairs, overlaps in [%s, %s], '
      'pairings positive (diag %s), 4(c-1) <= c^2 s on every pair: %s, H1 (D_min = %s): %s, c in (1,2] and < 4: %s; '
      'orbit reduction exact: %s (%d seed-vs-orbit values)'
      % (norm2(hstar), r1['n'], r1['npairs'], r1['smin'], r1['smax'], 4 - 2 * c384 + c384 * c384, r1['cc'], r1['dmin'],
         r1['h1'], r1['c_ok'], reduction_ok, len(set(r1s['vals']))))

# ------------------------------------------------------------------ K2: K768
G768 = group_closure([SP['cnot'], SP['TS'], SP['TJ'], SP['CX']])
G384 = group_closure([SP['cnot'], SP['TS'], SP['TJ']])
orb768 = orbit_rays(hstar, gens384 + [L_CX])
c768 = Fr(10001, 10000)
r2 = sprime_hyps(orb768, c768, pairs_all=True)
set384 = set(tuple(v) for v in orb384)
moved = canon(mvec(L_CX, hstar)) not in set384
k2 = (len(G384) == 384 and len(G768) == 768 and r2['n'] == 384 and Fr(len(G768), r2['n']) == 2 and moved
      and r2['dmin'] == Fr(85, 2048) and r2['c_ok'] and r2['h1'] and r2['pair_pos'] and r2['cc'])
check('K2', k2, 'K768 against theorem_Sprime_ineq at c = 10001/10000: |G384| = %d, |G768| = %d, %d rays (stabilizer %s), '
      'actC nflip moves K384\'s defect set: %s, D_min = %s (no product), %d pairs, overlaps in [%s, %s], H1: %s, '
      'pairings positive: %s, 4(c-1) <= c^2 s on every pair: %s, c in (1,2] and < 4: %s'
      % (len(G384), len(G768), r2['n'], Fr(len(G768), r2['n']), moved, r2['dmin'], r2['npairs'], r2['smin'], r2['smax'],
         r2['h1'], r2['pair_pos'], r2['cc'], r2['c_ok']))

# ------------------------------------------------------------------ K3: KC
hC = [C(-480, 7), C(357, 870), C(939, 834), C(448, 486)]
GC2 = group_closure([SP['cnot'], SP['TS'], SP['TJ'], SP['CS'], SP['CJ']])
orbC = orbit_rays(hC, [CNOT, L_TS, L_TJ, L_CS, L_CJ])
cC = Fr(100001, 100000)
r3 = sprime_hyps(orbC, cC, pairs_all=False, seed=hC)
k3 = (len(GC2) == 11520 and r3['n'] == 11520 and Fr(len(GC2), r3['n']) == 1 and r3['dmin'] > 0 and r3['c_ok']
      and r3['h1'] and r3['pair_pos'] and r3['cc'])
check('K3', k3, 'KC against theorem_Sprime_ineq at c = 100001/100000: |C2| = %d, %d rays (stabilizer %s), |h_C|^2 = %d, '
      'D_min = %s (positive: %s), seed-vs-orbit overlaps in [%s, %s] (= the pairwise extremes by the orbit reduction), '
      'H1: %s, pairing at s_min positive: %s, 4(c-1) <= c^2 s_min: %s, c in (1,2] and < 4: %s'
      % (len(GC2), r3['n'], Fr(len(GC2), r3['n']), norm2(hC), r3['dmin'], r3['dmin'] > 0, r3['smin'], r3['smax'], r3['h1'],
         r3['pair_pos'], r3['cc'], r3['c_ok']))


# ------------------------------------------------------------------ K4: the group the clause generates
def ad_sp(U):
    Ud = adj(U)
    out = []
    for k in range(16):
        m, n = divmod(k, 4)
        img = coord_of(mmul(mmul(U, T[m][n]), Ud))
        nz = [(4 * a + b, img[a][b] / 4) for a in range(4) for b in range(4) if img[a][b] != 0]
        assert len(nz) == 1 and nz[0][1] in (1, -1), 'not a Clifford element'
        out.append((nz[0][0], int(nz[0][1])))
    return tuple(out)


def matrix_group(gens_mat):
    gens_sp = [ad_sp(U) for U in gens_mat]
    grp = {IDENT: eye(4)}
    frontier = [IDENT]
    while frontier:
        nxt = []
        for a in frontier:
            for t, g in enumerate(gens_sp):
                b = compose(g, a)
                if b not in grp:
                    grp[b] = mmul(gens_mat[t], grp[a])
                    nxt.append(b)
        frontier = nxt
    return grp


ZI = kron(SZ, S0m)


def blocks(U):
    """block-diagonality with respect to Z (x) 1 and the two blocks"""
    offd = all(U[i][j] == Z0 for i in range(4) for j in range(4) if (i // 2) != (j // 2))
    return offd, [[U[i][j] for j in range(2)] for i in range(2)], [[U[i][j] for j in range(2, 4)] for i in range(2, 4)]


def det_ratio(U):
    offd, U0, U1 = blocks(U)
    assert offd
    return cdiv(det2(U0), det2(U1))


mg384 = matrix_group(gens384)
all_commute = all(mmul(U, ZI) == mmul(ZI, U) for U in mg384.values())
all_block = all(blocks(U)[0] for U in mg384.values())
ratios = set(det_ratio(U) for U in mg384.values())
gen_ratios = [det_ratio(CNOT), det_ratio(L_TS), det_ratio(L_TJ)]
# two reflections
Un = [[C(Fr(3, 5), Fr(-4, 5)), Z0], [Z0, C(Fr(3, 5), Fr(4, 5))]]
nvec = (Fr(-7, 25), Fr(24, 25), Fr(0))
nsig = madd(madd(mscale(nvec[0], SX), mscale(nvec[1], SY)), mscale(nvec[2], SZ))
refl_n = mmul(mmul(kron(S0m, Un), CNOT), adj(kron(S0m, Un)))
two_refl_n = refl_n == madd(kron(P0, S0m), kron(P1, nsig)) and mmul(mmul(Un, SX), adj(Un)) == nsig
msig = mmul(mmul(UJ, SX), adj(UJ))
refl_m = mmul(mmul(kron(S0m, UJ), CNOT), adj(kron(S0m, UJ)))
Rmat = mmul(nsig, msig)
word = mmul(mmul(kron(S0m, UJ), refl_n), refl_m)
target_pair = madd(kron(P0, UJ), kron(P1, mmul(Rmat, UJ)))
# equality up to a global phase: the two matrices are proportional
def proportional(A, B):
    k = next((i, j) for i in range(4) for j in range(4) if B[i][j] != Z0)
    lam = cdiv(A[k[0]][k[1]], B[k[0]][k[1]])
    return abs2(lam) == 1 and A == mcscale(lam, B)


word_ok = proportional(word, target_pair) and det2(Rmat) == O1 and refl_m == madd(kron(P0, S0m), kron(P1, msig))
msig_coords = [trace(mmul(SIG[k], msig))[0] / 2 for k in (1, 2, 3)]
cphase = madd(kron(P0, S0m), kron(P1, SPH))
cphase_ratio = det_ratio(cphase)
k4 = (len(mg384) == 384 and all_commute and all_block and ratios == {O1, C(-1)} and gen_ratios == [C(-1), O1, O1]
      and two_refl_n and word_ok and cphase_ratio == C(0, -1))
check('K4', k4, 'all %d lifted matrices of G384 commute with Z (x) 1 (%s), are block-diagonal (%s), with det U0/det U1 in %s; '
      'generator ratios %s; U_n X U_n^dag = n.sigma and (1 (x) U_n) CNOT (1 (x) U_n)^dag = P0 (x) 1 + P1 (x) n.sigma: %s; '
      'U_J X U_J^dag = m.sigma with m = %s; the word (1 (x) U_J)(refl_n)(refl_m) is the block pair (U_J, R U_J) up to a '
      'phase with R = (n.sigma)(m.sigma) in SU(2): %s; the controlled phase has det ratio %s'
      % (len(mg384), all_commute, all_block, sorted(ratios), gen_ratios, two_refl_n, tuple(msig_coords), word_ok,
         cphase_ratio))

# ------------------------------------------------------------------ K5: Theorem C19-1 (a) on exact instances
def block_to_e0(a):
    return [[cconj(a[0]), cconj(a[1])], [cscale(Fr(-1), a[1]), a[0]]]


def c19a(psi):
    a, b = psi[0:2], psi[2:4]
    na, nb = norm2(a), norm2(b)
    M0, M1 = block_to_e0(a), block_to_e0(b)
    ok = (mvec(M0, a) == [C(na), Z0] and mvec(M1, b) == [C(nb), Z0]
          and mmul(M0, adj(M0)) == mscale(na, eye(2)) and mmul(M1, adj(M1)) == mscale(nb, eye(2))
          and det2(M0) == C(na) and det2(M1) == C(nb))
    Bm = madd(kron(P0, M0), kron(P1, M1))
    img = mvec(Bm, psi)
    ok = ok and img == [C(na), Z0, C(nb), Z0] and csub(cmul(img[0], img[3]), cmul(img[1], img[2])) == Z0
    return ok


cases5 = [[C(1), C(2), C(0, 3), C(-1, 1)], [C(3), C(0, 4), Z0, C(5)], [C(1, 2), C(2, -1), Z0, Z0],
          [Z0, Z0, C(3, -4), C(5)], [C(6), C(0, 8), C(7, -24), Z0], [C(Fr(1, 3), 1), C(2, Fr(-1, 7)), C(0, 1), C(1, 1)]]
k5 = all(c19a(psi) for psi in cases5)
check('K5', k5, 'C19-1 (a) on %d exact states incl. phi0 and the edge cases a = 0, b = 0: M0 a = (|a|^2, 0), '
      'M0 M0^dag = |a|^2 I, det M0 = |a|^2, and (M0 (+) M1) psi = (|a|^2, 0, |b|^2, 0) is a product' % len(cases5))


# ------------------------------------------------------------------ K6: the product identity of the block module
def hom3(x):
    return [Fr(1)] + list(x)


def prod_state(x, y):
    hx, hy = hom3(x), hom3(y)
    return [[hx[m] * hy[n] for n in range(4)] for m in range(4)]


def k6_instance(al, be):
    c = al * al + be * be
    x0 = [Fr(0)] * 3 if c == 0 else [2 * al * be / c, Fr(0), (al * al - be * be) / c]
    inball = sum(t * t for t in x0) <= 1
    e3 = [Fr(0), Fr(0), Fr(1)]
    lhs = mscale(c, dict_of(prod_state(x0, e3)))
    y = [C(al), Z0, C(be), Z0]
    return inball and lhs == outer(y, y)


k6_cases = [(Fr(0), Fr(0)), (Fr(1), Fr(0)), (Fr(0), Fr(1)), (Fr(3), Fr(4)), (Fr(2, 7), Fr(5, 3))]
k6 = all(k6_instance(al, be) for al, be in k6_cases)
check('K6', k6, 'for (alpha, beta) in %s: x0 in eball 3 and c . dict(prodState x0 e3) = y y^dag with y = (alpha, 0, beta, 0)'
      % [(str(a), str(b)) for a, b in k6_cases])

# ------------------------------------------------------------------ K7: the C21 safeguard for K768
d768 = msub(eye(4), mscale(c768 / norm2(hstar), outer(hstar, hstar)))
val_h = inner(hstar, mvec(d768, hstar))
vR = mvec(L_RTH, hstar)
smax_R = max(s_of(vR, v) for v in orb768)
RdR = mmul(mmul(L_RTH, d768), adj(L_RTH))
pair_R = inner(vR, mvec(RdR, vR))
k7 = (val_h[1] == 0 and val_h[0] < 0 and val_h[0] == (1 - c768) * norm2(hstar) and smax_R < 1 / c768
      and pair_R[1] == 0 and pair_R[0] == (1 - c768) * norm2(hstar))
check('K7', k7, '<h*|d|h*> = %s < 0 (d not PSD, K768 != Q3); max overlap of R h* with the 384 rays = %s < 1/c = %s, '
      'so P_{R h*} in PSD cap Z*; <R h*| R d R^dag |R h*> = %s < 0: actT R_z(theta0) does not preserve K768'
      % (val_h[0], smax_R, 1 / c768, pair_R[0]))

# ------------------------------------------------------------------ countercontrols
cx1 = Fr(301, 300)
xk1_holds = cx1 * cx1 * r1['smin'] >= 4 * (cx1 - 1)
print('COUNTER XK1 %s: "4(c\'-1) <= c\'^2 s on every pair of K384 at c\' = 301/300" -- at s_min = %s: %s vs %s'
      % ('fails as stated' if not xk1_holds else 'DOES NOT FAIL', r1['smin'], cx1 * cx1 * r1['smin'], 4 * (cx1 - 1)), flush=True)
cx2 = Fr(101, 100)
xk2_holds = cx2 * cx2 * r2['smin'] >= 4 * (cx2 - 1)
print('COUNTER XK2 %s: "4(c\'-1) <= c\'^2 s on every pair of K768 at c\' = 101/100" -- at s_min = %s: %s vs %s'
      % ('fails as stated' if not xk2_holds else 'DOES NOT FAIL', r2['smin'], cx2 * cx2 * r2['smin'], 4 * (cx2 - 1)), flush=True)
xk3_holds = cphase_ratio in ratios
print('COUNTER XK3 %s: "the controlled phase is a word in the generators" -- its det ratio %s is %sin the set of ratios %s of '
      'every word (an invariant of products: ratios multiply; the generators have ratios +-1)'
      % ('fails as stated' if not xk3_holds else 'DOES NOT FAIL', cphase_ratio, '' if xk3_holds else 'not ', sorted(ratios)),
      flush=True)
a34 = [C(3), C(0, 4)]
M34 = block_to_e0(a34)
xk4_holds = mmul(M34, adj(M34)) == eye(2)
print('COUNTER XK4 %s: "M0 is unitary without normalisation" -- at a = (3, 4i): M0 M0^dag = %s I'
      % ('fails as stated' if not xk4_holds else 'DOES NOT FAIL', mmul(M34, adj(M34))[0][0][0]), flush=True)

# ------------------------------------------------------------------ verdict
nf = sum(1 for _, ok in RESULTS if not ok)
print('checks: %d, failures: %d' % (len(RESULTS), nf), flush=True)
counters_ok = (not xk1_holds) and (not xk2_holds) and (not xk3_holds) and (not xk4_holds)
if nf == 0 and len(RESULTS) == 8 and counters_ok:
    print('VERDICT E19-S6-CONTROLS-EXACT', flush=True)
else:
    print('VERDICT NOT RENDERED -- failing: %s%s' % ([n for n, ok in RESULTS if not ok],
                                                    '' if counters_ok else ' (a countercontrol did not fail as stated)'), flush=True)
print('exit 0' if nf == 0 and counters_ok else 'exit 1')
sys.exit(0 if nf == 0 and counters_ok else 1)
