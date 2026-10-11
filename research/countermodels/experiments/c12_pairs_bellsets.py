# c12_pairs_bellsets.py -- research/countermodels node C12 (round 3): the non-Bell pair theorem; Conjecture C8-C at four
# members (all ten orthogonality patterns) and for finite Bell sets without orthogonal pairs.
# DECISION RULE (fixed before the first run, 2026-10-11T00:35:57Z by date -u; predictions in NOTES-C12 S0, 00:35:34Z):
#  Exact arithmetic only (int, Fraction, Gaussian rationals GQ); no float anywhere (guard EX). The instance data (Bell
#  vectors as Gaussian-integer parameters, witness points v as Gaussian-integer vectors) were found by a numerical search in
#  the scratchpad (search aid only, not evidence) and are hard-coded below; every claim is decided by the exact checks here.
#  Defects d = I - c P_h (P_h = h h^dag / |h|^2); <A, B> = tr(AB); overlap s(u, v) = |<u|v>|^2/(|u|^2 |v|^2).
#  PSD decisions by the Faddeev-LeVerrier characteristic polynomial (Hermitian A is PSD iff e1..e4 >= 0).
#  P (pair theorem). h1 = (1,0,0,0), h2 = (x, y, 0, 0), c_i = 1 + r_i^2. Criterion (CC): L = c1 c2 s - (c1 - 1) - (c2 - 1) >= 0
#    and L^2 >= 4 (c1 - 1)(c2 - 1) (equivalent to c1 c2 s >= (sqrt(c1-1) + sqrt(c2-1))^2). For each case the criterion is
#    computed and compared with the predicted side (below / at / above the threshold s* = (r1+r2)^2/((1+r1^2)(1+r2^2))).
#    Self-dual side (incl. the threshold): Theorem S' applies (record); consequence check: for both ordered pairs (j, k) the
#    far cap-edge point v of cap_j on the geodesic away from h_k (t_e = the largest multiple of 10^-9 with t_e^2 < T2, as
#    in c11) gives y = P_v + lam d_k, <y, d_j> = 0, lam > 0, y PSD. Witness side: at the far cap-edge point of cap_1,
#    s(h2, v) < 1 - 1/c2, <y, d1> = 0, <y, d2> > 0, x = v-orthogonal part of h2 has x^dag y x < 0 (y in K* \ K).
#    Bell pair (r1, r2) = (1, 1): s* = 1; the case s = 9/10 is on the witness side (C4.1); the orthogonal case s = 0 has
#    <d1, d2> = 0 (Theorem S; criterion not applicable) -- recorded.
#  B (four-member Bell sets). g(al, be, om) = (al, be, -conj(be) om, conj(al) om) with om in {1, i, -1, -i}: maximally
#    entangled (|det Psi|^2 = |g|^4 / 4). For each of the ten patterns: the vectors are pairwise distinct rays, the degree
#    sequence of the non-orthogonality graph is the stated one; for K4 and C4 the four vectors are linearly independent
#    (det != 0; for K4 hence every admissible (g1, g2) leaves two vectors with independent W-perp projections, outside C8's
#    theorem; for C4 not on one Bell circle). Witness (C8-L): for the given (i, k, v): k is a neighbour of i, s(g_i, v) > 1/2,
#    lam = -<P_v, d_i>/<d_k, d_i> > 0, y = P_v + lam d_k, <y, d_i> = 0, <y, d_l> >= 0 for every l, and x = h_k - (<v|h_k>/|v|^2) v
#    has x^dag y x < 0 and x^dag d_m x >= 0 for every m orthogonal to g_i. Then y in K(Z)* \ K(Z) (C8-L).
#  G (no orthogonal pairs, larger sets): six- and eight-member sets: maximally entangled, pairwise non-orthogonal, distinct,
#    and for every vertex the other members span C^4 (some 4 of them have nonzero determinant), so Tool A of NOTES-C12 is
#    unavailable at every vertex; the same exact witness check as B.
#  CC1 Z_F: all cross pairings 0 (no vertex has a neighbour; C8-L cannot start).
#  CC2 on a self-dual-side pair the witness construction fails as it must: at the far cap-edge point s(h_k, v) >= 1 - 1/c_k.
#  CC3 the square on one Bell circle {psi1, psi3, (psi1 +- psi3)/sqrt2} (C4 pattern, C8 (b)): its four vectors span a
#    2-dimensional space (rank 2), the degenerate case of Tool C.
#  VERDICT C12-PAIRS-BELLSETS-EXACT iff every CHECK passes and every COUNTERCONTROL behaves as stated; else NO VERDICT.
#  Verdict text generated from the measured values.
from math import isqrt
from fractions import Fraction as Fr
import itertools

RES = []
def rec(kind, cid, ok, text, detail=''):
    ok = bool(ok); RES.append(ok)
    print('%s %-4s %s %s%s' % (kind, cid, 'PASS' if ok else 'FAIL', text, (' -- ' + detail) if detail else ''))

class GQ:
    __slots__ = ('r', 'i')
    def __init__(self, r, i=0):
        self.r = r if isinstance(r, Fr) else Fr(r); self.i = i if isinstance(i, Fr) else Fr(i)
    def __add__(s, o): o = o if isinstance(o, GQ) else GQ(o); return GQ(s.r + o.r, s.i + o.i)
    __radd__ = __add__
    def __sub__(s, o): o = o if isinstance(o, GQ) else GQ(o); return GQ(s.r - o.r, s.i - o.i)
    def __rsub__(s, o): return GQ(o) - s
    def __neg__(s): return GQ(-s.r, -s.i)
    def __mul__(s, o):
        o = o if isinstance(o, GQ) else GQ(o); return GQ(s.r * o.r - s.i * o.i, s.r * o.i + s.i * o.r)
    __rmul__ = __mul__
    def conj(s): return GQ(s.r, -s.i)
    def n2(s): return s.r * s.r + s.i * s.i
    def __truediv__(s, o):
        if not isinstance(o, GQ): o = GQ(o)
        d = o.n2(); t = s * o.conj(); return GQ(t.r / d, t.i / d)
    def iszero(s): return s.r == 0 and s.i == 0
    def __eq__(s, o): o = o if isinstance(o, GQ) else GQ(o); return s.r == o.r and s.i == o.i
    def __hash__(s): return hash((s.r, s.i))
ZERO, ONE, II = GQ(0), GQ(1), GQ(0, 1)
def mmul(A, B): return [[sum((A[i][t] * B[t][j] for t in range(len(B))), ZERO) for j in range(len(B[0]))] for i in range(len(A))]
def madd(A, B): return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def mscale(c, A): return [[c * x for x in r] for r in A]
def eye(n): return [[ONE if i == j else ZERO for j in range(n)] for i in range(n)]
def tr(A): return sum((A[i][i] for i in range(len(A))), ZERO)
def mv(A, v): return [sum((A[i][t] * v[t] for t in range(len(v))), ZERO) for i in range(len(A))]
def ipv(u, v): return sum((u[t].conj() * v[t] for t in range(len(u))), ZERO)
def n2v(v): return sum((x.n2() for x in v), Fr(0))
def ovl(u, v): return ipv(u, v).n2() / (n2v(u) * n2v(v))
def detr(v): return (v[0] * v[3] - v[1] * v[2]).n2() / n2v(v) ** 2
def proj(v):
    n = n2v(v); return [[v[i] * v[j].conj() / n for j in range(4)] for i in range(4)]
def hip(A, B): return tr(mmul(A, B))
def dvec(v, c): return madd(eye(4), mscale(GQ(-c), proj(v)))
def isreal(x): return x.i == 0
def charpoly_e(A):
    n = 4; I4 = eye(n); Mk = [[ZERO] * n for _ in range(n)]; ck = ONE; coeffs = [ONE]
    for k in range(1, n + 1):
        Mk = madd(mmul(A, Mk), mscale(ck, I4))
        ck = GQ(Fr(-1, k)) * tr(mmul(A, Mk))
        coeffs.append(ck)
    return [coeffs[k] * (1 if k % 2 == 0 else -1) for k in range(1, n + 1)]
def psd(A):
    e = charpoly_e(A); return all(isreal(x) and x.r >= 0 for x in e)
def V(*xs): return [x if isinstance(x, GQ) else GQ(x) for x in xs]
def det4(M):   # exact determinant of a 4x4 GQ matrix (Laplace)
    def det(m):
        if len(m) == 1: return m[0][0]
        s = ZERO
        for j in range(len(m)):
            minor = [r[:j] + r[j + 1:] for r in m[1:]]
            term = m[0][j] * det(minor)
            s = s + term if j % 2 == 0 else s - term
        return s
    return det(M)
def geo(hj, hk, c):
    kap = ipv(hj, hk)
    uu = [hk[q] - (kap / n2v(hj)) * hj[q] for q in range(4)]
    w = [kap.conj() * x for x in uu]
    T2 = (c - 1) * n2v(hj) / n2v(w)
    te = Fr(isqrt(T2.numerator * 10 ** 18 // T2.denominator), 10 ** 9)
    while te * te >= T2: te -= Fr(1, 10 ** 9)
    return [hj[q] - GQ(te) * w[q] for q in range(4)], te
def cc_holds(c1, c2, s):
    L = c1 * c2 * s - (c1 - 1) - (c2 - 1)
    return L >= 0 and L * L >= 4 * (c1 - 1) * (c2 - 1)

# ---------- P: the pair theorem
cases = []   # (label, r1, r2, (x, y), predicted side)
for (r1, r2) in [(Fr(1, 2), Fr(1, 2)), (Fr(1, 3), Fr(1, 3)), (Fr(3, 4), Fr(3, 4)), (Fr(1, 10), Fr(1, 10)), (Fr(1, 2), Fr(3, 4)), (Fr(1), Fr(1, 2))]:
    q = (r1 + r2) / (1 - r1 * r2)      # threshold ratio x/y
    cases.append(((r1, r2), (q.numerator, q.denominator), 'at'))
    cases.append(((r1, r2), (q.numerator * 5 + q.denominator, q.denominator * 5), 'above'))     # larger overlap: self-dual side
    cases.append(((r1, r2), (q.numerator * 4, q.denominator * 5), 'below'))                      # smaller overlap: witness side
pok = True; prec = []
for (r1, r2), (x, y), side in cases:
    c1, c2 = 1 + r1 * r1, 1 + r2 * r2
    h1 = V(1, 0, 0, 0); h2 = V(x, y, 0, 0)
    s = ovl(h1, h2)
    sstar = (r1 + r2) ** 2 / ((1 + r1 * r1) * (1 + r2 * r2))
    holds = cc_holds(c1, c2, s)
    side_ok = (side == 'at' and s == sstar and holds) or (side == 'above' and s > sstar and holds) or (side == 'below' and s < sstar and not holds)
    d1, d2 = dvec(h1, c1), dvec(h2, c2)
    G = hip(d1, d2).r
    ok = side_ok and G > 0
    if holds:   # S' consequence at both far cap edges
        for (hj, hk, cj, ck, dj, dk) in [(h1, h2, c1, c2, d1, d2), (h2, h1, c2, c1, d2, d1)]:
            v, te = geo(hj, hk, cj)
            lam = -hip(proj(v), dj).r / G
            yv = madd(proj(v), mscale(GQ(lam), dk))
            ok &= ovl(hj, v) > 1 / cj and lam > 0 and hip(yv, dj).iszero() and psd(yv) and ovl(hk, v) >= 1 - 1 / ck
        tag = 'self-dual (S\')'
    else:
        v, te = geo(h1, h2, c1)
        lam = -hip(proj(v), d1).r / G
        yv = madd(proj(v), mscale(GQ(lam), d2))
        xx = [h2[q] - (ipv(v, h2) / n2v(v)) * v[q] for q in range(4)]
        xyx = ipv(xx, mv(yv, xx))
        ok &= ovl(h1, v) > 1 / c1 and ovl(h2, v) < 1 - 1 / c2 and lam > 0 and hip(yv, d1).iszero() and hip(yv, d2).r > 0 and isreal(xyx) and xyx.r < 0
        tag = 'witness'
    pok &= ok
    prec.append('(%s,%s) c=(%s,%s) s=%s [%s s*=%s]: %s%s' % (r1, r2, c1, c2, s, side, sstar, tag, '' if ok else ' FAILED'))
rec('CHECK', 'P1', pok, 'pair theorem instances: the criterion c1 c2 s >= (sqrt(c1-1)+sqrt(c2-1))^2 separates S\'-self-dual pairs from exact witnesses', '; '.join(prec))
# Bell pair (r = 1, 1): threshold s* = 1
hb1 = V(1, 0, 0, 0); hb2 = V(3, 1, 0, 0)
sb = ovl(hb1, hb2)
db1, db2 = dvec(hb1, 2), dvec(hb2, 2)
Gb = hip(db1, db2).r
v, te = geo(hb1, hb2, Fr(2))
lam = -hip(proj(v), db1).r / Gb
yv = madd(proj(v), mscale(GQ(lam), db2))
xx = [hb2[q] - (ipv(v, hb2) / n2v(v)) * v[q] for q in range(4)]
xyx = ipv(xx, mv(yv, xx))
bell_w = (not cc_holds(Fr(2), Fr(2), sb)) and ovl(hb1, v) > Fr(1, 2) and ovl(hb2, v) < Fr(1, 2) and hip(yv, db1).iszero() and hip(yv, db2).r > 0 and xyx.r < 0
orth0 = hip(dvec(V(1, 0, 0, 0), 2), dvec(V(0, 1, 0, 0), 2)).iszero()
rec('CHECK', 'P2', bell_w and orth0, 'c = 2: threshold s* = 1, the pair at s = %s has an exact witness (C4.1); an orthogonal Bell pair has <d1, d2> = 0 (Theorem S)' % sb)

# ---------- B: four-member Bell sets
OMG = [ONE, II, GQ(-1), GQ(0, -1)]
def g_of(p):
    ar, ai, br, bi, oi = p; al, be, om = GQ(ar, ai), GQ(br, bi), OMG[oi]
    return [al, be, -(be.conj() * om), al.conj() * om]
INST = {
 'K2+2K1': ([[1, -1, 0, 1, 3], [1, -1, 1, -1, 0], [0, 0, -1, 0, 3], [-2, -1, 2, 1, 3]], 3, 2, [(-2, -6), (6, 1), (2, 4), (2, 5)], (1, 1, 0, 0)),
 '2K2': ([[0, -2, -2, -1, 1], [-2, 1, -1, 0, 1], [0, 2, 2, 1, 3], [-1, 0, 2, 0, 1]], 2, 1, [(-1, 2), (4, 3), (2, 8), (-11, 1)], (1, 1, 1, 1)),
 'P3+K1': ([[1, -1, -1, -1, 0], [2, -2, 0, 2, 1], [0, 0, -1, 1, 0], [2, 1, -1, 1, 2]], 1, 3, [(0, -4), (-2, 2), (-4, -1), (-3, 3)], (2, 1, 1, 0)),
 'K3+K1': ([[-1, 2, 1, 1, 1], [1, 1, 0, 0, 3], [2, 2, -1, -1, 1], [1, 1, 1, 1, 3]], 3, 0, [(5, 0), (1, 5), (5, 4), (0, -2)], (2, 2, 2, 0)),
 'P4': ([[-2, 2, -1, 1, 2], [-1, 0, 1, 1, 2], [-1, 1, 2, 0, 3], [-1, 1, 0, 0, 3]], 0, 1, [(-3, 0), (-2, 0), (0, 0), (0, 2)], (2, 2, 1, 1)),
 'K1,3': ([[-1, 0, 1, -2, 1], [0, -2, 0, -2, 3], [-2, 2, 2, -1, 3], [-2, -1, -1, 1, 3]], 3, 2, [(0, -5), (-3, 1), (5, -1), (0, 4)], (3, 1, 1, 1)),
 'C4': ([[0, 2, 2, -2, 2], [2, 0, -1, -1, 2], [2, -1, -1, -1, 3], [1, -1, 2, 1, 3]], 2, 0, [(3, -3), (-4, -1), (0, 1), (-2, -6)], (2, 2, 2, 2)),
 'paw': ([[-1, 0, -2, -1, 0], [-2, 2, 2, 2, 3], [-2, 2, 1, -2, 0], [1, -2, 1, -2, 0]], 2, 0, [(0, 2), (1, -4), (0, 0), (-5, -2)], (3, 2, 2, 1)),
 'diamond': ([[-1, -2, 0, 1, 1], [-1, -1, 0, 0, 1], [-2, 1, 1, -2, 3], [-1, -1, -2, 1, 1]], 3, 1, [(0, -1), (-2, 0), (-4, 1), (-4, -1)], (3, 3, 2, 2)),
 'K4': ([[-1, -2, 0, 2, 2], [2, 1, 0, -1, 0], [1, 2, -2, 0, 3], [2, 0, -1, -2, 0]], 0, 1, [(-4, -4), (4, 5), (2, -4), (3, -6)], (3, 3, 3, 3)),
}
def canon(v):
    k = next(t for t in range(4) if not v[t].iszero()); a = v[k]; return tuple(x / a for x in v)
def witness_ok(gs, i, k, v):
    n = len(gs)
    Z = [dvec(g, 2) for g in gs]
    orth = [[ipv(gs[a], gs[b]).iszero() for b in range(n)] for a in range(n)]
    if orth[i][k] or i == k: return False, 'k not a neighbour'
    if not ovl(gs[i], v) > Fr(1, 2): return False, 'v not in cap i'
    Gik = hip(Z[k], Z[i]).r
    lam = -hip(proj(v), Z[i]).r / Gik
    y = madd(proj(v), mscale(GQ(lam), Z[k]))
    pairs = [hip(y, z) for z in Z]
    x = [gs[k][q] - (ipv(v, gs[k]) / n2v(v)) * v[q] for q in range(4)]
    xyx = ipv(x, mv(y, x))
    l4 = [ipv(x, mv(Z[m], x)) for m in range(n) if m != i and orth[i][m]]
    ok = lam > 0 and pairs[i].iszero() and all(isreal(p) and p.r >= 0 for p in pairs) and isreal(xyx) and xyx.r < 0 and all(isreal(t) and t.r >= 0 for t in l4)
    return ok, 'lam=%s, min<y,d_l>(l!=i)=%s, x^dag y x/|x|^2=%s, (L4) count %d' % (lam, min(p.r for j, p in enumerate(pairs) if j != i), xyx.r / n2v(x), len(l4))
bok = True; brec = []
for name, (params, i, k, vint, degexp) in INST.items():
    gs = [g_of(p) for p in params]
    me = all(detr(g) == Fr(1, 4) for g in gs)
    distinct = len(set(canon(g) for g in gs)) == 4
    orth = [[ipv(gs[a], gs[b]).iszero() for b in range(4)] for a in range(4)]
    deg = tuple(sorted([sum(1 for b in range(4) if b != a and not orth[a][b]) for a in range(4)], reverse=True))
    v = [GQ(a, b) for a, b in vint]
    wok, wrec = witness_ok(gs, i, k, v)
    extra = True; xrec = ''
    if name in ('K4', 'C4'):
        dt = det4([list(g) for g in gs])
        extra = not dt.iszero(); xrec = '; det != 0: %s' % extra
    ok = me and distinct and deg == degexp and wok and extra
    bok &= ok
    brec.append('%s: degrees %s, (i, k) = (%d, %d), %s%s%s' % (name, deg, i, k, wrec, xrec, '' if ok else ' FAILED'))
rec('CHECK', 'B1', bok, 'all ten orthogonality patterns of four Bell vectors: exact C8-L witnesses (K4 and C4 instances linearly independent)', '; '.join(brec))
# K4 instance outside C8's theorem: for every admissible (g1, g2) (g2 of maximal overlap with g1) the other two are not in W or W-perp
gsK = [g_of(p) for p in INST['K4'][0]]
outside = True
for a in range(4):
    ovs = {b: ovl(gsK[a], gsK[b]) for b in range(4) if b != a}
    mx = max(ovs.values())
    for b in [b for b in ovs if ovs[b] == mx]:
        for c in range(4):
            if c in (a, b): continue
            inWperp = ipv(gsK[a], gsK[c]).iszero() and ipv(gsK[b], gsK[c]).iszero()
            if inWperp: outside = False
rec('CHECK', 'B2', outside and not det4([list(g) for g in gsK]).iszero(), 'the K4 instance is in C8\'s open class: linearly independent, no member in W-perp for any admissible (g1, g2) (so no common perpendicular e exists)')

# ---------- G: larger sets without orthogonal pairs
GI = {
 6: ([[-1, 2, 1, 1, 2], [0, -1, 0, 2, 0], [-1, -2, 0, 1, 0], [-1, -1, 0, 0, 3], [2, 1, 2, -1, 0], [-2, 2, 1, -2, 0]], 0, 3, [(-4, 3), (3, 0), (2, -1), (1, 1)]),
 8: ([[1, 0, 2, -2, 0], [-2, -2, -1, 1, 3], [-2, -2, 1, -1, 0], [-2, 2, -1, -2, 3], [-1, -1, 0, 1, 3], [2, 1, -2, -2, 1], [1, -1, -1, 0, 0], [-2, 2, 2, -2, 0]], 7, 2, [(-4, 4), (4, -7), (-8, -6), (-7, 0)]),
}
gok = True; grec = []
for nm, (params, i, k, vint) in GI.items():
    gs = [g_of(p) for p in params]
    me = all(detr(g) == Fr(1, 4) for g in gs)
    distinct = len(set(canon(g) for g in gs)) == nm
    noorth = all(not ipv(gs[a], gs[b]).iszero() for a in range(nm) for b in range(nm) if a != b)
    span4 = all(any(not det4([list(gs[t]) for t in comb]).iszero() for comb in itertools.combinations([t for t in range(nm) if t != a], 4)) for a in range(nm))
    v = [GQ(a, b) for a, b in vint]
    wok, wrec = witness_ok(gs, i, k, v)
    ok = me and distinct and noorth and span4 and wok
    gok &= ok
    grec.append('%d members: no orthogonal pair %s, every vertex\'s neighbours span C^4 %s, (i, k) = (%d, %d), %s' % (nm, noorth, span4, i, k, wrec))
rec('CHECK', 'G1', gok, 'six- and eight-member Bell sets without orthogonal pairs (Tool A unavailable at every vertex): exact C8-L witnesses', '; '.join(grec))

# ---------- countercontrols
psi = [V(1, 1, 1, -1), V(1, -1, 1, 1), V(1, -1, -1, -1), V(1, 1, -1, 1)]
cc1 = all(hip(dvec(psi[a], 2), dvec(psi[b], 2)).iszero() for a in range(4) for b in range(4) if a != b)
rec('COUNTERCONTROL', 'CC1', cc1, 'Z_F: all cross pairings vanish, no vertex has a neighbour (C8-L cannot start; Theorem S)')
# CC2: self-dual side, the witness construction fails
r1 = r2 = Fr(1, 2); c = 1 + r1 * r1
h1 = V(1, 0, 0, 0); h2 = V(5 * 4 + 3, 3 * 5, 0, 0)    # above the threshold (x/y = 4/3 + 1/5)
v, te = geo(h1, h2, c)
cc2 = cc_holds(c, c, ovl(h1, h2)) and ovl(h2, v) >= 1 - 1 / c
rec('COUNTERCONTROL', 'CC2', cc2, 'self-dual side (c = 5/4, s = %s): at the far cap edge s(h2, v) = %s >= 1 - 1/c = %s: no witness from the construction' % (ovl(h1, h2), ovl(h2, v), 1 - 1 / c))
# CC3: the square on one Bell circle
sq = [psi[0], psi[2], [psi[0][q] + psi[2][q] for q in range(4)], [psi[0][q] - psi[2][q] for q in range(4)]]
mes = all(detr(g) == Fr(1, 4) for g in sq)
rank2 = det4([list(g) for g in sq]).iszero() and not ipv(sq[0], sq[0]).iszero() and ipv(sq[0], sq[1]).iszero()   # sq[2], sq[3] are sq[0] +- sq[1] by construction
orthsq = [[ipv(sq[a], sq[b]).iszero() for b in range(4)] for a in range(4)]
degsq = tuple(sorted([sum(1 for b in range(4) if b != a and not orthsq[a][b]) for a in range(4)], reverse=True))
rec('COUNTERCONTROL', 'CC3', mes and rank2 and degsq == (2, 2, 2, 2), 'the square on one Bell circle: C4 pattern %s with its four vectors in a 2-dimensional span (Tool C\'s degenerate case; C8 (b))' % (degsq,))

def nofloat(x):
    if isinstance(x, float): return False
    if isinstance(x, (list, tuple)): return all(nofloat(y) for y in x)
    return True
rec('CHECK', 'EX', nofloat([cases, list(INST.values()), list(GI.values())]), 'no float in any input or recorded value')
nf = sum(1 for r in RES if not r)
print('summary: %d checks, %d failed' % (len(RES), nf))
if nf == 0:
    print('VERDICT C12-PAIRS-BELLSETS-EXACT: the pair criterion separates %d S\'-self-dual pairs from %d exact witnesses (Bell threshold s* = 1); '
          'exact C8-L witnesses for all ten orthogonality patterns of four Bell vectors (K4 in C8\'s open class) and for six- and '
          'eight-member Bell sets without orthogonal pairs' % (sum(1 for t in cases if t[2] != 'below'), sum(1 for t in cases if t[2] == 'below')))
else:
    print('NO VERDICT')
