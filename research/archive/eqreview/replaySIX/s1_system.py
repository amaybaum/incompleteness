"""EQ4-SIX probe s1 -- N1: the complete six-token constraint system after uniformity (c = 0 and c = 1).  Research only.

Usage:  python3 -I -B s1_system.py <base>/verification/lean-mathlib/OIBridge
Imports only the copied library eq4_lib.py (sha256 cc2c6aca94007ac8).

Setting.  P6: every nonempty S in {0..5} carries one closed convex cone K_S; for every bipartition S = A|B,
K_A (x) K_B <= K_S and K_A* (x) K_B* <= K_S*; K_1 = PSD_2; pair cones PSD_4 (c = 0) or the twin cone PT(PSD_4)
(c = 1) in aligned charts.  Settled (EQ4-P, audited): uniformity of triples and of four-token sets within six tokens,
S_3 symmetry, one-token filter invariance (five tokens), co-self-duality K3 = T(K3*) (c = 0) / K3 = K3* (c = 1).

Written claim W1 (NOTES N1).  With the minimal choices K_4 = cl cone(K1 (x) K3, K2 (x) K2, glued states),
K_5 = cl cone(products), K_6 = cl cone(products), P6 holds iff K3 satisfies
  (A1) BS <= K3 <= BS*  (c = 1: B_tw <= K3 <= B_tw*);  (A2) invariance under one-token CP maps (incl. renames);
  (A3) co-self-duality;  (A4) the crossing-split glue network is >= 0:
       N(x, y, e, f) = tr[ Glue_e(e, f; z) Glue_s(x, y; w) ] >= 0,
       Glue_s = tr_pq[(w_pq (x) 1)(x_{p r1 r2} (x) y_{q u1 u2})],  Glue_e = tr_st[(z_st (x) 1)(e_{s r1 u1} (x) f_{t r2 u2})]
  for x, y in K3, e, f in K3*, w a pair effect, z a pair state.
Every other pairing among the generators of L_4 and of the effect-side set is implied by (A1)-(A3); the crossing
constraints of five-sets and six-sets either have an empty intersection (automatic) or reduce to (A2), (A3), (A4).

DECISION RULE (fixed before the first run; rules, not expected numbers).  VERDICT `S1-SYSTEM-EXACT` iff all:
  K  transcription control (eq4_lib, base conventions).
  E  enumeration (exhaustive, exact): over every subset S of {0..5} with |S| >= 2 and every ordered pair of distinct
     unordered bipartitions (effect side A|B, state side C|D): (E1) whenever a part has one token, some intersection is
     empty; (E2) every pair with all four intersections nonempty has |S| in {4, 5, 6} and part sizes: |S| = 4 -> 2|2 vs
     2|2; |S| = 5 -> parts in {2, 3}; |S| = 6 -> parts in {2, 3, 4}; (E3) no such pair involves a five-token part;
     (E4) the six-token pairs fall into exactly the size classes {2|4 vs 2|4, 2|4 vs 3|3, 3|3 vs 2|4, 3|3 vs 3|3}
     (counts printed).
  B  five-token crossing = one-token filter: for rank-one e = |eps><eps| on (p,q), x = |xi><xi| on (p,r) and y on
     (q,s,t), the conditional tr_pq[(e (x) 1)(x (x) y)] equals Ad(U)(y renamed q -> r) with U = Xi^T conj(E) on all 64
     units y (3 random exact instances); countercontrol: U' = Xi conj(E) fails on some unit.  Also: for a given U,
     E = 1 and Xi = U^T reproduce Ad(U) (every filter arises).
  C  glued state against a 1|3 product effect a_{r1} (x) b_{r2 u1 u2} equals the five-token crossing value
     tr[(w (x) b)(cond(a; x) (x) y)] (3 random exact instances).
  D  glued state against a 2|2 product effect crossing the glue split, with rank-one pair effects (Bell w, a, b
     filtered: w = Phi+ and a = (1 (x) A) Phi+ (1 (x) A)^dag, b likewise with B): the value equals
     (1/8) tr(x T(Ad(k) y)) with k = 1 (x) A^dag (x) B^dag on (q, u1, u2) after renaming (3 random exact instances);
     countercontrol: the same with Ad(k) and no T differs.
  F  same-split glue network with Bell links equals (1/4) tr(T(M) N) with M = tr_R[(e (x) 1_p)(x (x) 1_s)] on (p, s)
     and N = tr_U[(f (x) 1_q)(y (x) 1_t)] on (q, t), after renaming p, s -> q, t... (identity on 3 random exact
     instances); and the five-token confinement M in PT(PSD_4): <M, (1/2)PT_p(z renamed)> is the value of a five-token
     crossing with a Bell effect (identity on all 16 units z).  Countercontrol: the crossing-split network is not equal
     to (1/4) tr(T(M') N') for the analogous two-token contractions (fails on a random instance).
  G  c = 1 analogue of B and D with twin links (SWAP/2): with the twin effect PT_q(Ad(A) Phi+) and the twin state
     PT_r(Ad(B) Phi+) the five-token conditional is Ad(V) of the renamed y with V = (1/2) conj(B) A^T (derived by
     index computation in NOTES), and the theta reduction holds without T.
  Q  QM control: with PSD nodes the crossing-split network is >= 0 (3 random exact instances); W3 nodes give a
     nonnegative value; the PN countercontrol of EQ4-P (GHZ against W3 through three Bell links) is -1/16 < 0.
"""
import itertools
import random
import sys
from fractions import Fraction as Fr

sys.path.insert(0, __file__.rsplit("/", 1)[0] if "/" in __file__ else ".")
import eq4_lib as L  # noqa: E402

BASE = sys.argv[1]
rep = L.Report("s1_system")
rng = random.Random(2026100951)
rep.check("K0 transcription control", L.transcription_control(BASE)[0])

# ------------------------------------------------------------------------------------------------ E enumeration
TOK = tuple(range(6))


def bipartitions(S):
    S = tuple(sorted(S))
    first = S[0]
    rest = S[1:]
    out = []
    for r in range(0, len(rest)):
        for comb in itertools.combinations(rest, r):
            A = frozenset((first,) + comb)
            B = frozenset(S) - A
            if B:
                out.append((A, B))
    return out


ok_e1 = ok_e2 = ok_e3 = True
six_classes = {}
counts = {4: 0, 5: 0, 6: 0}
for n in range(2, 7):
    for S in itertools.combinations(TOK, n):
        bps = bipartitions(S)
        for (A, B), (C, D) in itertools.product(bps, bps):
            if {A, B} == {C, D}:
                continue
            inter = [A & C, A & D, B & C, B & D]
            allne = all(inter)
            if min(len(A), len(B), len(C), len(D)) == 1 and allne:
                ok_e1 = False
            if allne:
                counts[n] = counts.get(n, 0) + 1
                sizes = sorted([len(A), len(B), len(C), len(D)])
                if n == 4 and not (len(A) == 2 and len(C) == 2):
                    ok_e2 = False
                if n == 5 and not all(s in (2, 3) for s in sizes):
                    ok_e2 = False
                if n == 6 and not all(s in (2, 3, 4) for s in sizes):
                    ok_e2 = False
                if n not in (4, 5, 6):
                    ok_e2 = False
                if 5 in sizes:
                    ok_e3 = False
                if n == 6:
                    ef = "%d|%d" % tuple(sorted((len(A), len(B))))
                    st = "%d|%d" % tuple(sorted((len(C), len(D))))
                    six_classes[(ef, st)] = six_classes.get((ef, st), 0) + 1
rep.check("E1 every ordered pair of bipartitions with a one-token part has an empty intersection", ok_e1)
rep.check("E2 crossings with all intersections nonempty: |S| = 4: 2|2 vs 2|2; |S| = 5: parts in {2,3}; |S| = 6: parts in "
          "{2,3,4} (counts %s)" % counts, ok_e2)
rep.check("E3 no crossing with all intersections nonempty has a five-token part (K_5 enters only automatically)", ok_e3)
ok_e4 = set(six_classes) == {("2|4", "2|4"), ("2|4", "3|3"), ("3|3", "2|4"), ("3|3", "3|3")}
rep.check("E4 six-token crossing classes (effects, states) = %s" % sorted(six_classes.items()), ok_e4)


# ------------------------------------------------------------------------------------------------ helpers
def rvec(n):
    return [L.rand_gauss(rng) for _ in range(2 ** n)]


def mat2_from_vec(v):
    return [[v[0], v[1]], [v[2], v[3]]]


def conjm(M):
    return [[M[i][j].conj() for j in range(2)] for i in range(2)]


def transm(M):
    return [[M[j][i] for j in range(2)] for i in range(2)]


def mul2(A, B):
    return [[A[i][0] * B[0][j] + A[i][1] * B[1][j] for j in range(2)] for i in range(2)]


def rel(A, m, qs):
    return L.reorder(L.relabel(A, m), qs)


# ------------------------------------------------------------------------------------------------ B five-token crossing
p, q, r, s, t = 0, 1, 2, 3, 4
ok_b = True
ok_bc = False
for _ in range(3):
    ev = rvec(2)
    xv = rvec(2)
    e = L.ket_op(ev, (p, q))
    x = L.ket_op(xv, (p, r))
    E = mat2_from_vec(ev)
    Xi = mat2_from_vec(xv)
    U = mul2(transm(Xi), conjm(E))
    U2 = mul2(Xi, conjm(E))
    Uop = L.op(U, (r,))
    U2op = L.op(U2, (r,))
    for _, y in L.units((q, s, t)):
        lhs = L.reorder(L.cond(e, L.tensor(x, y)), (r, s, t))
        yr = rel(y, {q: r}, (r, s, t))
        ok_b &= lhs == L.ad(Uop, yr)
        if not (lhs == L.ad(U2op, yr)):
            ok_bc = True
# every filter arises: E = 1, Xi = U^T
Ug = [[L.rand_gauss(rng) for _ in range(2)] for _ in range(2)]
e1 = L.ket_op([1, 0, 0, 1], (p, q))
xi = transm(Ug)
x1 = L.ket_op([xi[0][0], xi[0][1], xi[1][0], xi[1][1]], (p, r))
ok_every = True
for _, y in L.units((q, s, t)):
    lhs = L.reorder(L.cond(e1, L.tensor(x1, y)), (r, s, t))
    ok_every &= lhs == L.ad(L.op(Ug, (r,)), rel(y, {q: r}, (r, s, t)))
rep.check("B five-token crossing (pair effect on (p,q), pair state on (p,r), y on (q,s,t)): conditional = Ad(Xi^T conj E) of "
          "the renamed y on all 64 units (3 random exact rank-one instances); every filter Ad(U) arises (E = 1, Xi = U^T); "
          "countercontrol Xi conj E fails", ok_b and ok_every and ok_bc)

# ------------------------------------------------------------------------------------------------ C glued state vs 1|3
P_, Q_, R1, R2, U1, U2 = 10, 11, 12, 13, 14, 15
ok_c = True
for _ in range(3):
    w = L.rand_psd(rng, (P_, Q_), rank=2)
    x = L.rand_op(rng, (P_, R1, R2))
    y = L.rand_op(rng, (Q_, U1, U2))
    a = L.rand_op(rng, (R1,))
    b = L.rand_op(rng, (R2, U1, U2))
    gs = L.cond(w, L.tensor(x, y))
    lhs = L.pair(L.tensor(a, b), gs)
    xa = L.cond(a, x)
    rhs = L.pair(L.tensor(w, b), L.tensor(xa, y))
    ok_c &= lhs == rhs
rep.check("C glued state against a 1|3 product effect = five-token crossing value with cond(a; x) (3 random exact "
          "instances)", ok_c)


# ------------------------------------------------------------------------------------------------ D theta reduction
def bell_filtered(Am, a_, b_):
    """(1 (x) A) Phi+ (1 (x) A)^dag on (a_, b_), Phi+ normalized."""
    return L.ad(L.op(Am, (b_,)), L.phi_plus(a_, b_))


ok_d = True
ok_dc = False
for _ in range(3):
    Am = [[L.rand_gauss(rng) for _ in range(2)] for _ in range(2)]
    Bm = [[L.rand_gauss(rng) for _ in range(2)] for _ in range(2)]
    x = L.rand_op(rng, (P_, R1, R2))
    y = L.rand_op(rng, (Q_, U1, U2))
    w = L.phi_plus(P_, Q_)
    a2 = bell_filtered(Am, R1, U1)
    b2 = bell_filtered(Bm, R2, U2)
    val = L.pair(L.tensor(a2, b2), L.cond(w, L.tensor(x, y)))
    k = L.tensor(L.identity((Q_,)), L.op(conjm(transm(Am)), (U1,)), L.op(conjm(transm(Bm)), (U2,)))
    ky = L.ad(k, y)
    yren = rel(ky, {Q_: P_, U1: R1, U2: R2}, (P_, R1, R2))
    pred = L.pair(x, L.transpose(yren)) * Fr(1, 8)
    ok_d &= val == pred
    pred2 = L.pair(x, yren) * Fr(1, 8)
    if not (val == pred2):
        ok_dc = True
rep.check("D glued state against a crossing 2|2 product of filtered Bell effects = (1/8) tr(x T(Ad(1 (x) A^dag (x) B^dag) y)) "
          "(3 random exact instances): implied by (A2) + (A3); countercontrol without T differs", ok_d and ok_dc)

# ------------------------------------------------------------------------------------------------ F same split
S_, T_ = 16, 17
ok_f = True
ok_fc = False
for _ in range(3):
    x = L.rand_op(rng, (P_, R1, R2))
    y = L.rand_op(rng, (Q_, U1, U2))
    e = L.rand_op(rng, (S_, R1, R2))
    f = L.rand_op(rng, (T_, U1, U2))
    gs = L.cond(L.phi_plus(P_, Q_), L.tensor(x, y))
    ge_same = L.cond(L.phi_plus(S_, T_), L.tensor(e, f))
    val = L.pair(ge_same, gs)
    M = L.ptrace(L.matmul(L.tensor(e, L.identity((P_,))), L.tensor(x, L.identity((S_,)))), (P_, S_))
    N = L.ptrace(L.matmul(L.tensor(f, L.identity((Q_,))), L.tensor(y, L.identity((T_,)))), (Q_, T_))
    Nren = rel(N, {Q_: P_, T_: S_}, (P_, S_))
    pred = L.pair(L.transpose(M), Nren) * Fr(1, 4)
    ok_f &= val == pred
    # crossing split for the countercontrol: e on (s, r1, u1), f on (t, r2, u2)
    ec = rel(e, {R2: U1}, (S_, R1, U1))
    fc = rel(f, {U1: R2}, (T_, R2, U2))
    ge_cross = L.cond(L.phi_plus(S_, T_), L.tensor(ec, fc))
    valc = L.pair(ge_cross, gs)
    if not (valc == val):
        ok_fc = True
# five-token confinement of M: <M, (1/2) PT_p(z renamed)> is a five-token crossing value with the Bell effect
O_ = 18
ok_f2 = True
x = L.rand_op(rng, (P_, R1, R2))
e = L.rand_op(rng, (S_, R1, R2))
M = L.ptrace(L.matmul(L.tensor(e, L.identity((P_,))), L.tensor(x, L.identity((S_,)))), (P_, S_))
for _, z in L.units((O_, S_)):
    # five tokens {p, o, s, r1, r2}: effects e (x) Phi+_{p o}, states x (x) z_{o s}
    v5 = L.pair(L.tensor(e, L.phi_plus(P_, O_)), L.tensor(x, z))
    zren = rel(z, {O_: P_}, (P_, S_))
    pred = L.pair(M, L.ptranspose(zren, [P_])) * Fr(1, 2)
    ok_f2 &= v5 == pred
rep.check("F same-split glue network = (1/4) tr(T(M) N) with the two-token contractions (3 random exact instances); "
          "five-token confinement: <M, (1/2) PT_p(z)> is a five-token crossing value on all 16 units z, so M is in "
          "PT(PSD_4)* = PT(PSD_4) and, with T(PT(PSD_4)) = PT(PSD_4), the value is >= 0; countercontrol: the "
          "crossing-split value differs", ok_f and ok_f2 and ok_fc)


# ------------------------------------------------------------------------------------------------ G c = 1 analogues
def twin(a_, b_):
    return L.swap_half(a_, b_)


ok_g1 = True
for _ in range(2):
    Am = [[L.rand_gauss(rng) for _ in range(2)] for _ in range(2)]
    Bm = [[L.rand_gauss(rng) for _ in range(2)] for _ in range(2)]
    # twin effect = PT_q of a filtered Bell effect; twin state = PT_r of a filtered Bell state
    et = L.ptranspose(L.ad(L.op(Am, (q,)), L.phi_plus(p, q)), [q])
    xt = L.ptranspose(L.ad(L.op(Bm, (r,)), L.phi_plus(p, r)), [r])
    # predicted V = (1/2) conj(B) A^T (index computation, NOTES N1); check on all 64 units y of (q, s, t)
    V = [[v * L.G(Fr(1, 2)) for v in row] for row in mul2(conjm(Bm), transm(Am))]
    Vop = L.op(V, (r,))
    for _, y in L.units((q, s, t)):
        lhs = L.reorder(L.cond(et, L.tensor(xt, y)), (r, s, t))
        ok_g1 &= lhs == L.ad(Vop, rel(y, {q: r}, (r, s, t)))
ok_g2 = True
for _ in range(2):
    x = L.rand_op(rng, (P_, R1, R2))
    y = L.rand_op(rng, (Q_, U1, U2))
    val = L.pair(L.tensor(twin(R1, U1), twin(R2, U2)), L.cond(twin(P_, Q_), L.tensor(x, y)))
    yren = rel(y, {Q_: P_, U1: R1, U2: R2}, (P_, R1, R2))
    ok_g2 &= val == L.pair(x, yren) * Fr(1, 8)
rep.check("G c = 1: the five-token conditional with a twin effect and a twin state is Ad((1/2) conj(B) A^T) of the renamed y "
          "(all 64 units, 2 random exact instances); the twin theta value is (1/8) tr(x y) (no T): implied by "
          "filter invariance and K3 = K3*", ok_g1 and ok_g2)


# ------------------------------------------------------------------------------------------------ Q QM controls
def net_cross(x, y, e, f, w, z):
    gs = L.cond(w, L.tensor(x, y))
    ge = L.cond(z, L.tensor(e, f))
    return L.pair(ge, gs)


ok_q = True
for _ in range(3):
    x = L.rand_psd(rng, (P_, R1, R2), rank=2)
    y = L.rand_psd(rng, (Q_, U1, U2), rank=2)
    e = L.rand_psd(rng, (S_, R1, U1), rank=2)
    f = L.rand_psd(rng, (T_, R2, U2), rank=2)
    v = net_cross(x, y, e, f, L.phi_plus(P_, Q_), L.phi_plus(S_, T_))
    ok_q &= v.im == 0 and v.re >= 0
W = L.w3((0, 1, 2))
vw = net_cross(rel(W, {0: P_, 1: R1, 2: R2}, (P_, R1, R2)), rel(W, {0: Q_, 1: U1, 2: U2}, (Q_, U1, U2)),
               rel(W, {0: S_, 1: R1, 2: U1}, (S_, R1, U1)), rel(W, {0: T_, 1: R2, 2: U2}, (T_, R2, U2)),
               L.phi_plus(P_, Q_), L.phi_plus(S_, T_))
links = L.tensor(L.phi_plus(0, 3), L.phi_plus(1, 4), L.phi_plus(2, 5))
v6 = L.pair(L.tensor(L.ghz((0, 1, 2)), L.w3((3, 4, 5))), links)
rep.check("Q QM controls: PSD nodes give crossing-split values >= 0 (3 random exact instances); W3 nodes give %s >= 0; "
          "countercontrol GHZ against W3 through three Bell links = %s < 0" % (vw, v6),
          ok_q and vw.im == 0 and vw.re >= 0 and v6.im == 0 and v6.re < 0)

rep.verdict("S1-SYSTEM-EXACT")
