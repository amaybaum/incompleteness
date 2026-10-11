# c14_facial.py -- research/countermodels node C14 (round 3): the facial invariant c of a continuum defect; T on the
# explicit circle cone of the torus node S2 (C13.7's family).
# DECISION RULE (fixed before the first run, 2026-10-11T01:03:09Z by date -u; predictions in NOTES-C14 S0, 01:02:22Z):
#  Exact arithmetic only (int, Fraction, Gaussian rationals); no float (guard EX). Coordinates: the orthonormal basis
#  e = (|0+>, |1->, |0->, |1+>) of C^4 (traces and pairings are basis-independent); computational vectors E1 = (1,1,0,0),
#  E2 = (0,0,1,-1), E3 = (1,-1,0,0), E4 = (0,0,1,1) (= sqrt2 e_k) are used only to compute det Psi. The circle cone:
#  h_alpha = 3 e1 + e^{i alpha} e2 (p = 9/10), defects d_alpha = I - c P_{h_alpha}, c = 1000/961.
#  F0 window: lambda_max(h_alpha) = 9/10 for alpha in {0, pi/2, pi, 3pi/2, (3+4i)/5} (det Psi ratio 9/100 in computational
#     coordinates); H1: c 9/10 <= 1; (CC): overlaps on the circle >= (2p-1)^2 = 16/25 and c^2 16/25 >= 4(c - 1).
#  F1 contact points: v = a e1 + b e2 + x e3 + y e4 with a, b positive integers, 3a + b = 31k (k = 1, 2, 3), x, y Gaussian
#     integers with |x|^2 + |y|^2 = 100k^2 - a^2 - b^2 > 0 (enumerated: |Re|, |Im| <= 10); every listed v satisfies
#     c |<h_0|v>|^2 = |h_0|^2 |v|^2 (on the null quadric of d_0, i.e. <P_v, d_0> = 0) and, since a, b > 0, the maximum over alpha
#     of |<h_alpha|v>|^2 is attained at alpha = 0 ([W]: |3a + e^{-i alpha} b| <= 3a + b), so P_v is a pure member of K (pairs >= 0
#     with every d_alpha): P_v lies in the exposed face of K at d_0.
#  F2 the real span of {P_v} over the listed contact points has rank exactly 14 (exact rank over Q of the 16 real coordinates).
#  F3 every listed P_v satisfies <P_v, d_0> = 0 and <P_v, i[P_e2, d_0]> = 0 (the tangency constraint; P_e2 generates the circle);
#     d_0 and i[P_e2, d_0] are linearly independent (so the two constraints cut a 14-dimensional space).
#  F4 c(P00) >= 9 in this cone: nine pure states u orthogonal to |00> with c (3|<e1|u>| + |<e2|u>|)^2 <= 10 |u|^2 (exact decision:
#     R = 10|u|^2/c - 9|A|^2 - |B|^2 >= 0 and 36|A|^2|B|^2 <= R^2) whose projectors have rank 9.
#  CC1 a point with 3a + b = 31k but v orthogonal to e1 + ... -- a listed point with b replaced by -b (relative phase pi) has
#     <P_v, d_0> > 0 (not on the face: the alignment matters).
#  CC2 single-defect cone K({d_0}) (Lemma 2's situation): contact points with complex relative phase, 3a + b = 31k(3+4i)/5 (k = 5),
#     |v|^2 = 100k^2: their projectors have rank 15 (the full hyperplane d_0-perp): the drop to 14 is the circle's tangency.
#  VERDICT C14-FACIAL-EXACT iff every CHECK passes and every COUNTERCONTROL behaves as stated; else NO VERDICT.
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
def V(*xs): return [x if isinstance(x, GQ) else GQ(x) for x in xs]
def ipv(u, v): return sum((u[t].conj() * v[t] for t in range(len(u))), ZERO)
def n2v(v): return sum((x.n2() for x in v), Fr(0))
def proj(v):
    n = n2v(v); return [[v[i] * v[j].conj() / n for j in range(4)] for i in range(4)]
def mmul(A, B): return [[sum((A[i][t] * B[t][j] for t in range(4)), ZERO) for j in range(4)] for i in range(4)]
def tr(A): return sum((A[i][i] for i in range(4)), ZERO)
def hip(A, B): return tr(mmul(A, B))
def eye4(): return [[ONE if i == j else ZERO for j in range(4)] for i in range(4)]
def dvec(v, c): P = proj(v); return [[(ONE if i == j else ZERO) - GQ(c) * P[i][j] for j in range(4)] for i in range(4)]
def realvec(A):   # 16 real coordinates of a Hermitian matrix
    out = []
    for i in range(4):
        for j in range(i, 4):
            if i == j: out.append(A[i][i].r)
            else: out += [A[i][j].r, A[i][j].i]
    return out
def rank(rows):
    M = [list(r) for r in rows]; rk = 0; ncol = len(M[0]) if M else 0
    for col in range(ncol):
        piv = next((r for r in range(rk, len(M)) if M[r][col] != 0), None)
        if piv is None: continue
        M[rk], M[piv] = M[piv], M[rk]
        for r in range(len(M)):
            if r != rk and M[r][col] != 0:
                f = M[r][col] / M[rk][col]
                M[r] = [M[r][t] - f * M[rk][t] for t in range(ncol)]
        rk += 1
    return rk
def e_to_comp(v):   # v in e-coordinates -> computational coordinates (times sqrt2)
    a, b, x, y = v
    return [a + x, a - x, b + y, -b + y]
def detratio(v):
    w = e_to_comp(v); d = w[0] * w[3] - w[1] * w[2]; return d.n2() / n2v(w) ** 2

c = Fr(1000, 961)
p = Fr(9, 10)
h0 = V(3, 1, 0, 0)
d0 = dvec(h0, c)
# ---------- F0 window
ws = [ONE, II, GQ(-1), GQ(0, -1), GQ(Fr(3, 5), Fr(4, 5))]
lam_ok = all(detratio(V(3, w, 0, 0)) == Fr(9, 100) for w in ws)        # |det|^2/|v|^4 = 9/100  <=>  lambda_max = 9/10
ovs = [ipv(V(3, w, 0, 0), V(3, w2, 0, 0)).n2() / 100 for w in ws for w2 in ws]
win = lam_ok and c * Fr(9, 10) <= 1 and min(ovs) >= Fr(16, 25) and c * c * Fr(16, 25) >= 4 * (c - 1)
rec('CHECK', 'F0', win, 'the circle {3e1 + w e2}: lambda_max = 9/10, overlaps >= 16/25; at c = 1000/961 H1 and (CC) hold (S\' applies)', 'smallest sampled overlap %s' % min(ovs))

# ---------- F1 contact points
gints = [GQ(x, y) for x in range(-10, 11) for y in range(-10, 11)]
by_n2 = {}
for g in gints: by_n2.setdefault(g.n2(), []).append(g)
pts = []
for k in (1, 2, 3):
    for a in range(1, 31 * k // 3 + 1):
        b = 31 * k - 3 * a
        if b <= 0: continue
        R2 = 100 * k * k - a * a - b * b
        if R2 <= 0: continue
        cnt = 0
        for n1 in sorted(by_n2):
            if n1 > R2: break
            n2_ = R2 - n1
            if n2_ not in by_n2: continue
            for x in by_n2[n1][:2]:
                for y in by_n2[n2_][:2]:
                    pts.append(V(a, b, x, y)); cnt += 1
                    if cnt >= 4: break
                if cnt >= 4: break
            if cnt >= 4: break
cont_ok = True
for v in pts:
    on = (c * ipv(h0, v).n2() == n2v(h0) * n2v(v))
    pos = v[0].i == 0 and v[1].i == 0 and v[0].r > 0 and v[1].r > 0
    cont_ok &= on and pos and hip(proj(v), d0).iszero()
rec('CHECK', 'F1', cont_ok and len(pts) >= 14, 'contact points of d_0 (pure members of K on its null quadric, aligned at alpha = 0)', '%d points, (a, b) ratios %s' % (len(pts), sorted(set((int(v[0].r), int(v[1].r)) for v in pts))))

# ---------- F2 rank
rk = rank([realvec(proj(v)) for v in pts])
rec('CHECK', 'F2', rk == 14, 'the contact projectors span a space of real dimension exactly 14', 'rank %d' % rk)

# ---------- F3 tangency constraint
Pe2 = proj(V(0, 1, 0, 0))
comm = [[(mmul(Pe2, d0)[i][j] - mmul(d0, Pe2)[i][j]) * II for j in range(4)] for i in range(4)]   # i[P_e2, d_0]
tang = all(hip(proj(v), comm).iszero() for v in pts)
herm = all(comm[i][j] == comm[j][i].conj() for i in range(4) for j in range(4))
indep = rank([realvec(d0), realvec(comm)]) == 2
rec('CHECK', 'F3', tang and herm and indep, 'every contact projector is orthogonal to d_0 and to the tangent i[P_e2, d_0]; the two constraints are independent (face span <= 14)')

# ---------- F4 c(P00) >= 9
def in_K(u):
    A = ipv(V(1, 0, 0, 0), u); B = ipv(V(0, 1, 0, 0), u)
    Rr = 10 * n2v(u) / c - 9 * A.n2() - B.n2()
    return Rr >= 0 and 36 * A.n2() * B.n2() <= Rr * Rr
# |00> in e-coordinates (up to sqrt2): |00> = (|0+> + |0->)/sqrt2 -> (1, 0, 1, 0); its orthogonal complement
k00 = V(1, 0, 1, 0)
basis_perp = [V(1, 0, -1, 0), V(0, 1, 0, 0), V(0, 0, 0, 1)]
cands = []
for co in itertools.product([ONE, ZERO, II, GQ(-1), GQ(1, 1)], repeat=3):
    u = [sum((co[t] * basis_perp[t][q] for t in range(3)), ZERO) for q in range(4)]
    if n2v(u) == 0: continue
    if in_K(u): cands.append(u)
r9 = rank([realvec(proj(u)) for u in cands]) if cands else 0
perp = all(ipv(k00, u).iszero() for u in cands)
rec('CHECK', 'F4', r9 == 9 and perp, 'pure members of K orthogonal to |00> span Herm(|00>-perp): c(P00) >= 9 (= 9 by Lemma 1 of NOTES-C3)', '%d members, rank %d' % (len(cands), r9))

# ---------- countercontrols
v = pts[0]; vm = V(v[0], -v[1], v[2], v[3])
cc1 = hip(proj(vm), d0).r > 0
rec('COUNTERCONTROL', 'CC1', cc1, 'the same point with relative phase pi between e1 and e2 is off the face (<P_v, d_0> > 0)', '<P_v,d_0> = %s' % hip(proj(vm), d0).r)
# CC2: single-defect contact points with complex relative phase
pts2 = []
k = 5
target = GQ(31 * 3, 31 * 4)        # 3a + b = 31 k (3+4i)/5 with k = 5
for a in [GQ(x, y) for x in range(18, 38) for y in range(26, 48)]:
    b = target - GQ(3) * a
    R2 = 100 * k * k - a.n2() - b.n2()
    if R2 <= 0 or R2 not in by_n2 and not any((R2 - n1) in by_n2 for n1 in by_n2 if n1 <= R2):
        continue
    found = False
    for n1 in sorted(by_n2):
        if n1 > R2: break
        if (R2 - n1) in by_n2:
            pts2.append(V(a, b, by_n2[n1][0], by_n2[R2 - n1][0])); found = True; break
    if len(pts2) >= 30: break
on2 = all(c * ipv(h0, v).n2() == n2v(h0) * n2v(v) for v in pts2)
rk2 = rank([realvec(proj(v)) for v in pts2]) if pts2 else 0
rec('COUNTERCONTROL', 'CC2', on2 and rk2 == 15, 'the single-defect cone K({d_0}): points of the whole null quadric span the hyperplane d_0-perp (rank 15, Lemma 2); the circle cuts it to 14', '%d points, rank %d' % (len(pts2), rk2))

def nofloat(x):
    if isinstance(x, float): return False
    if isinstance(x, (list, tuple)): return all(nofloat(y) for y in x)
    return True
rec('CHECK', 'EX', nofloat([c, p, rk, rk2, r9]), 'no float in any recorded value')
nf = sum(1 for r in RES if not r)
print('summary: %d checks, %d failed' % (len(RES), nf))
if nf == 0:
    print('VERDICT C14-FACIAL-EXACT: on the S2 circle cone at c = %s the exposed face at a defect spans exactly %d dimensions (contact points; '
          'tangency bound), at P00 the pure members span %d; with Y6 no automorphism maps a defect to P00: T fails; the single-defect '
          'cone has %d (Lemma 2)' % (c, rk, r9, rk2))
else:
    print('NO VERDICT')
