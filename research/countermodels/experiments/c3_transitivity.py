# c3_transitivity.py -- research/countermodels node C3: exact ingredients of the analysis of extreme-ray transitivity T.
# DECISION RULE (fixed before the first run, 2026-10-10T20:44:05Z by date -u):
#  Conventions as in c1_cones.py. T: the automorphism group of K acts transitively on the normalized extreme rays.
#  T1 (normalization): sum of squared entries of prodState(a, b) = (1 + |a|^2)(1 + |b|^2) (symbolic), = 4 on S^2 x S^2;
#     the 16 functions {1, a_i, b_j, a_i b_j} on S^2 x S^2 are linearly independent (exact 16 x 16 evaluation matrix at
#     rational points of the spheres, nonsingular), so E00 is, up to scale, the only table pairing constantly with all
#     pure products.
#  T2 (the support lemma): for a table y with pauliW(y) = 0 (+) Y3 on |00>^perp (Y3 a symbolic Hermitian 3x3),
#     4 <prodState(a,b), y> ... equals 4 w^dag Y3 w / (|a|^2|b|^2)-normalized form with w = (a0 b1, a1 b0, a1 b1) for
#     spinors a = (a0, a1), b = (b0, b1): checked as the symbolic identity ipW(prodState(n(a), n(b)), y) =
#     4 w^dag Y3 w / ((|a0|^2+|a1|^2)(|b0|^2+|b1|^2)), n(.) the Bloch vector of a spinor. With [W] surjectivity of
#     (a, b) -> w onto {r != 0} this gives: a member of maxCone supported on |00>^perp is PSD.
#  T3 (surgery defects have c = 15): for each defect z of K(E0), K(e_{3/4}), K_F2, K(Z_F), a pure member v of K on the null
#     quadric of z (ipW(T_v, z) = 0) with every other defect constraint strict (ipW(T_v, z') > 0): the [W] lemma of
#     NOTES-C3 (an open set of pure members on the quadric spans z^perp) then gives c(z) = 15.
#  T4 (the sphere condition of the compact case): the normalized extreme rays (entry (0,0) = 1) of K(Z_F) -- the defects
#     4 z_s and pure tables -- all have squared norm 4; the normalized defect of K(e_c) has squared norm 1 + 2c^2 (< 4 on
#     (1/2, 1]); record of K(E0): 3.
#  COUNTERCONTROLS: CC1 a mixed (non-pure) PSD table (E00) has squared norm 1, not 4; CC2 for the non-orthogonal pair
#  {F, actC Rx F} (cos 3/5) there is a pure state with both constraints violated (so caps overlap: the T3 premise
#  "disjoint caps" is load-bearing); CC3 the identity of T2 fails if w is replaced by (a0 b0, a1 b0, a1 b1).
#  VERDICT C3-INGREDIENTS-EXACT printed iff T1-T4 pass and the countercontrols fail as stated.
import sympy as sp
from itertools import product

iu, Rt = sp.I, sp.Rational
s = [sp.eye(2), sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -iu], [iu, 0]]), sp.Matrix([[1, 0], [0, -1]])]
def kron(A, B): return sp.Matrix(4, 4, lambda i, j: A[i // 2, j // 2] * B[i % 2, j % 2])
SS = [[kron(s[m], s[n]) for n in range(4)] for m in range(4)]
SSP = [[[(i, j, SS[m][n][j, i]) for i in range(4) for j in range(4) if SS[m][n][j, i] != 0] for n in range(4)] for m in range(4)]
def pW(w): return sp.expand(sum((w[m, n] * SS[m][n] for m in range(4) for n in range(4)), sp.zeros(4, 4)) / 4)
def table(A):
    t = sp.Matrix(4, 4, lambda m, n: sp.expand(sum(A[i, j] * v for i, j, v in SSP[m][n])))
    assert all(sp.expand(sp.im(x)) == 0 for x in t), 'non-real table'
    return t.applyfunc(lambda x: sp.expand(sp.re(x)))
def ip(a, b): return sp.expand(sum(a[m, n] * b[m, n] for m in range(4) for n in range(4)))
def E(m, n):
    t = sp.zeros(4, 4); t[m, n] = 1; return t
def hom(x): return sp.Matrix([1] + list(x))
def prod(x, y): return hom(x) * hom(y).T
def Tpure(v):
    v = sp.Matrix(v); return table(v * v.H / sp.expand((v.H * v)[0]))
SGN = lambda m, n: -1 if (m, n) in [(1, 3), (2, 2)] else 1
PC = [[0, 0, 3, 3], [1, 1, 2, 2], [2, 2, 1, 1], [3, 3, 0, 0]]
PT = [[0, 1, 2, 3], [1, 0, 3, 2], [1, 0, 3, 2], [0, 1, 2, 3]]
def cnot(w): return sp.Matrix(4, 4, lambda m, n: SGN(m, n) * w[PC[m][n], PT[m][n]])
def Hom(N):
    H = sp.eye(4); H[1:, 1:] = N; return H
def actC(N, w): return Hom(N) * w
RES = {}
def chk(cid, ok, note=''):
    RES[cid] = bool(ok); print('CHECK %-34s %s %s' % (cid, 'PASS' if ok else 'FAIL', note))

# T1
xs, ys = sp.symbols('x1:4', real=True), sp.symbols('y1:4', real=True)
P = prod(xs, ys)
n2 = sp.expand(sum(P[m, n] ** 2 for m in range(4) for n in range(4)))
t1a = sp.expand(n2 - (1 + sum(x * x for x in xs)) * (1 + sum(y * y for y in ys))) == 0
pts = [(Rt(3, 5), Rt(4, 5), 0), (Rt(4, 5), 0, Rt(3, 5)), (0, Rt(3, 5), Rt(4, 5)), (Rt(-3, 5), Rt(4, 5), 0), (Rt(2, 3), Rt(1, 3), Rt(2, 3)),
       (Rt(-2, 3), Rt(2, 3), Rt(1, 3)), (Rt(1, 3), Rt(-2, 3), Rt(2, 3)), (0, 0, 1), (1, 0, 0), (0, 1, 0), (Rt(6, 7), Rt(2, 7), Rt(3, 7))]
assert all(sum(c * c for c in p) == 1 for p in pts)
rows = []
for a, b in product(pts, repeat=2):
    rows.append([1] + list(a) + list(b) + [a[i] * b[j] for i in range(3) for j in range(3)])
M16 = sp.Matrix(rows)
t1b = M16.rank() == 16
chk('T1 normalization', t1a and t1b, '|prodState(a,b)|^2 = (1+|a|^2)(1+|b|^2) = 4 on S^2 x S^2; {1, a_i, b_j, a_i b_j} independent (rank 16)')
# T2
hs = sp.symbols('h0:9', real=True)
Y3 = sp.Matrix([[hs[0], hs[3] + iu * hs[4], hs[5] + iu * hs[6]], [hs[3] - iu * hs[4], hs[1], hs[7] + iu * hs[8]],
                [hs[5] - iu * hs[6], hs[7] - iu * hs[8], hs[2]]])
R4 = sp.zeros(4, 4); R4[1:, 1:] = Y3
y = table(R4)
ar = sp.symbols('ar0 ai0 ar1 ai1', real=True); br = sp.symbols('br0 bi0 br1 bi1', real=True)
a0, a1 = ar[0] + iu * ar[1], ar[2] + iu * ar[3]; b0, b1 = br[0] + iu * br[1], br[2] + iu * br[3]
def bloch(u0, u1):
    nn = sp.expand(u0 * sp.conjugate(u0) + u1 * sp.conjugate(u1))
    return [sp.expand(2 * sp.re(sp.conjugate(u0) * u1)), sp.expand(2 * sp.im(sp.conjugate(u0) * u1)), sp.expand(u0 * sp.conjugate(u0) - u1 * sp.conjugate(u1))], nn
na, Na = bloch(a0, a1); nb, Nb = bloch(b0, b1)
ha, hb = sp.Matrix([Na] + na), sp.Matrix([Nb] + nb)       # homogeneous vectors: table of (a a^dag) (x) (b b^dag)
lhs = sp.expand(ip(ha * hb.T, y))                         # = Na Nb ipW(prodState(n(a)/Na, n(b)/Nb), y)
def wform(w):
    w = sp.Matrix(w); return sp.expand(4 * (w.H * Y3 * w)[0])
w_ok = [a0 * b1, a1 * b0, a1 * b1]
t2 = sp.expand(lhs - wform(w_ok)) == 0
chk('T2 support lemma identity', t2, 'Na Nb ipW(prodState, y) = 4 w^dag Y3 w with w = (a0 b1, a1 b0, a1 b1) (symbolic)')
cc3 = sp.expand(lhs - wform([a0 * b0, a1 * b0, a1 * b1])) != 0
RES['CC3 wrong w fails'] = cc3
print('COUNTERCONTROL CC3 w = (a0 b0, a1 b0, a1 b1): identity %s' % ('fails (as required)' if cc3 else 'HOLDS (FAIL)'))
# T3
def zs(s1, s2): return (E(0, 0) + s1 * E(1, 3) + s2 * E(2, 2) - s1 * s2 * E(3, 1)) / 4
ZF = [zs(a, b) for a, b in [(1, 1), (1, -1), (-1, 1), (-1, -1)]]
F = zs(-1, -1)
CONES = {'K(E0)': [E(0, 0) + E(1, 3) - E(2, 2)], 'K(e_3/4)': [E(0, 0) + Rt(3, 4) * (E(1, 3) - E(2, 2))], 'K_F2': [F, cnot(F)], 'K(Z_F)': ZF}
GB = [0, 1, -1, iu, 2, 1 + iu]
ok3 = True; notes = []
for nm, Z in CONES.items():
    for k, z in enumerate(Z):
        M = pW(z); ev = M.eigenvects()
        neg = [v for l, mu, vs in ev if l < 0 for v in vs]; pos = [v for l, mu, vs in ev if l > 0 for v in vs]
        lneg = [l for l, mu, vs in ev if l < 0][0]
        found = None
        for co in product(GB, repeat=len(pos)):
            if all(c == 0 for c in co): continue
            u = sum((c * v for c, v in zip(co, pos)), sp.zeros(4, 1))
            num = sp.expand((u.H * M * u)[0]); g = neg[0]
            gg = sp.expand((g.H * g)[0])
            # v = t g + u with t^2 (-lneg) gg = num  (on the quadric); choose u with num/(-lneg gg) a rational square
            r = sp.sqrt(num / (-lneg * gg))
            if not r.is_rational: continue
            v = r * g + u
            w = Tpure(v)
            if ip(z, w) != 0: continue
            if all(ip(z2, w) > 0 for j, z2 in enumerate(Z) if j != k):
                found = w; break
        ok3 &= found is not None
        notes.append('%s z%d %s' % (nm, k, 'ok' if found is not None else 'NONE'))
chk('T3 open pure set on each null quadric', ok3, '; '.join(notes))
# T4
cs = sp.Symbol('c', positive=True)
norms_ZF = set(sp.expand(ip(4 * z, 4 * z)) for z in ZF)
pure_norm = sp.expand(ip(Tpure(sp.Matrix([1, 2, iu, 3])), Tpure(sp.Matrix([1, 2, iu, 3]))))
ec = E(0, 0) + cs * (E(1, 3) - E(2, 2))
nec = sp.expand(ip(ec, ec))
E0n = ip(CONES['K(E0)'][0], CONES['K(E0)'][0])
t4 = norms_ZF == {4} and pure_norm == 4 and sp.expand(nec - (1 + 2 * cs ** 2)) == 0 and E0n == 3
chk('T4 sphere condition', t4, 'K(Z_F): normalized defects |4z_s|^2 = %s, pure %s; K(e_c): %s; K(E0): %s' % (norms_ZF, pure_norm, sp.factor(nec), E0n))
cc1 = ip(E(0, 0), E(0, 0)) == 1
RES['CC1 mixed table not on the sphere'] = cc1
print('COUNTERCONTROL CC1 E00 squared norm %s (not 4, as required)' % ip(E(0, 0), E(0, 0)))
Rxc = sp.Matrix([[1, 0, 0], [0, Rt(3, 5), -Rt(4, 5)], [0, Rt(4, 5), Rt(3, 5)]])
gF = actC(Rxc, F)
def negv(z):
    M = pW(z); l = min(M.eigenvals()); return (M - l * sp.eye(4)).nullspace()[0]
c1v, c2v = negv(F), negv(gF)
both = None
for k in range(0, 9):
    for ph in (1, iu, -1, -iu):
        w = Tpure(c1v + Rt(k, 4) * ph * c2v)
        if ip(F, w) < 0 and ip(gF, w) < 0: both = (k, ph); break
    if both: break
RES['CC2 overlapping caps'] = both is not None
print('COUNTERCONTROL CC2 {F, actC Rx F}: a pure state violating both constraints: %s' % (both,))
bad = [k for k, v in RES.items() if not v]
print('summary: %d checks, %d failed%s' % (len(RES), len(bad), (': ' + ', '.join(bad)) if bad else ''))
print('VERDICT C3-INGREDIENTS-EXACT' if not bad else 'NO VERDICT')
