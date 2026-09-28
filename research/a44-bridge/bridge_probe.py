"""A44 bridge diagnostic -- exact separation tests of defined carriers against act 40's Dita locus.

Research thread, not a frozen probe. Everything asserted is exact arithmetic (Gaussian rationals in
Python fractions, integer exponent lattices); no floating-point value decides anything.

Objects are rebuilt from act 38/39's frozen probe definitions (verification/lean/dita_torus_probe.py):
  SIG = F4(z) (x) F4(w), z = (3+4i)/5, w = (5+12i)/13, index (a,b) -> 4a+b, scaled by 4 (unimodular entries)
  A = [a odd][b = 3][c odd], B = [a = 2][d = 1], C = [a+b odd][(c,d) in {(0,2),(2,0)}] on ((a,b),(c,d))
  H3(u) = SIG o u1^A u2^B u3^C (scaled by 4)
L = act 40's locus: u1 = +-1 or u2 = 1 or u3 = +-1.

Run: python3 bridge_probe.py  (single core, Python standard library only; about 50 s)
"""
import itertools, random, sys, time
from fractions import Fraction as Fr
from collections import Counter

T0 = time.time()
FAILS = []
def check(name, got, want):
    ok = got == want
    print(('PASS ' if ok else 'FAIL ') + name + ('' if ok else '  got=%r want=%r' % (got, want)))
    if not ok: FAILS.append(name)
    return ok

# ---- exact Gaussian rationals (as in the frozen probes) ------------------------------------------------------------
class G:
    __slots__ = ('a', 'b')
    def __init__(s, a, b=0): s.a = Fr(a); s.b = Fr(b)
    def __mul__(s, o): return G(s.a * o.a - s.b * o.b, s.a * o.b + s.b * o.a)
    def __add__(s, o): return G(s.a + o.a, s.b + o.b)
    def __sub__(s, o): return G(s.a - o.a, s.b - o.b)
    def __neg__(s): return G(-s.a, -s.b)
    def conj(s): return G(s.a, -s.b)
    def __eq__(s, o): return s.a == o.a and s.b == o.b
    def __hash__(s): return hash((s.a, s.b))
    def norm2(s): return s.a * s.a + s.b * s.b
    def key(s): return (s.a, s.b)
    def __repr__(s): return ('(%s %s %si)' % (s.a, '-' if s.b < 0 else '+', abs(s.b))) if s.b else str(s.a)
ZERO, ONE, I_ = G(0), G(1), G(0, 1)
MONE = G(-1)
def gpow(u, k):
    r = ONE
    for _ in range(abs(k)): r = r * (u if k > 0 else u.conj())
    return r

def F4(z):
    m = G(-1)
    return [[ONE, ONE, ONE, ONE], [ONE, z, m, -z], [ONE, m, ONE, m], [ONE, -z, m, z]]   # scaled by 2
def dita(X, Ys, D):
    return [[X[i // 4][j // 4] * D[j // 4][i % 4] * Ys[j // 4][i % 4][j % 4] for j in range(16)] for i in range(16)]
def kron(X, Y): return dita(X, [Y] * 4, [[ONE] * 4 for _ in range(4)])
z = G(Fr(3, 5), Fr(4, 5)); w = G(Fr(5, 13), Fr(12, 13))
SIG = kron(F4(z), F4(w))
def EA(i, j): a, b, c, d = i // 4, i % 4, j // 4, j % 4; return 1 if (a % 2 == 1 and b == 3 and c % 2 == 1) else 0
def EB(i, j): a, b, c, d = i // 4, i % 4, j // 4, j % 4; return 1 if (a == 2 and d == 1) else 0
def EC(i, j): a, b, c, d = i // 4, i % 4, j // 4, j % 4; return 1 if ((a + b) % 2 == 1 and (c, d) in ((0, 2), (2, 0))) else 0
EXP = [[(EA(i, j), EB(i, j), EC(i, j)) for j in range(16)] for i in range(16)]
N = 16
def H3(u):
    u1, u2, u3 = u
    return [[SIG[i][j] * gpow(u1, EXP[i][j][0]) * gpow(u2, EXP[i][j][1]) * gpow(u3, EXP[i][j][2]) for j in range(N)] for i in range(N)]
def in_L(u): return u[0] * u[0] == ONE or u[1] == ONE or u[2] * u[2] == ONE
def is_unitary(H):
    for i in range(N):
        for j in range(N):
            s = ZERO
            for k in range(N): s = s + H[i][k] * H[j][k].conj()
            if s != (G(16) if i == j else ZERO): return False
    return True
def vadd(*vs): return tuple(sum(x) for x in zip(*vs))
def vneg(v): return tuple(-x for x in v)

# ---- test points: exact Gaussian-rational units ----------------------------------------------------------------------
V1, V2, V3 = G(Fr(3, 5), Fr(4, 5)), G(Fr(5, 13), Fr(12, 13)), G(Fr(8, 17), Fr(15, 17))
V4, V5, V6 = G(Fr(7, 25), Fr(24, 25)), G(Fr(20, 29), Fr(21, 29)), G(Fr(12, 37), Fr(35, 37))
PTS = {
    'SIG(1,1,1)': (ONE, ONE, ONE), 'F1+(1,v2,v3)': (ONE, V2, V3), 'F1-(-1,v2,v3)': (MONE, V2, V3),
    'F2(v1,1,v3)': (V1, ONE, V3), 'F3+(v1,v2,1)': (V1, V2, ONE), 'F3-(v1,v2,-1)': (V1, V2, MONE),
    'D-(-1,-1,-1)': (MONE, MONE, MONE),
    'O1(v1,v2,v3)': (V1, V2, V3), 'O2 absent face (v1,-1,v3)': (V1, MONE, V3), 'O3 diag(i,i,i)': (I_, I_, I_),
    'O4 diag(v4,v4,v4)': (V4, V4, V4), 'O5(v5,v6,v4)': (V5, V6, V4), 'O6(-v1,v2,v3)': (-V1, V2, V3),
}
print('== section 0: objects')
for name, u in PTS.items():
    check('H3 at %s is a flat unitary (scaled: |h|=1, H H* = 16 I)' % name,
          (all(x.norm2() == 1 for r in H3(u) for x in r) and is_unitary(H3(u))), True)
check('act 40 membership of the test points',
      [in_L(u) for u in PTS.values()], [True] * 7 + [False] * 6)

# ---- integer lattices in Z^3 -----------------------------------------------------------------------------------------
def hnf(gens):
    """row-echelon (Hermite-style) basis of the Z-span of integer 3-vectors"""
    rows = [list(g) for g in set(tuple(g) for g in gens) if any(g)]
    basis = []
    for col in range(3):
        piv = [r for r in rows if r[col] != 0]
        rest = [r for r in rows if r[col] == 0]
        while len(piv) > 1:
            piv.sort(key=lambda r: abs(r[col]))
            p = piv[0]; new = [p]
            for r in piv[1:]:
                q = r[col] // p[col]
                r2 = [r[k] - q * p[k] for k in range(3)]
                (new if r2[col] != 0 else rest).append(r2)
            piv = new
        if piv:
            p = piv[0]
            if p[col] < 0: p = [-x for x in p]
            basis.append(p)
        rows = [r for r in rest if any(r)]
    return basis
def in_lattice(basis, v):
    v = list(v)
    for b in basis:
        col = next(k for k in range(3) if b[k] != 0)
        if v[col] % b[col] != 0: return False
        q = v[col] // b[col]; v = [v[k] - q * b[k] for k in range(3)]
    return not any(v)
def lattice_report(name, gens):
    B = hnf(gens)
    rank = len(B)
    det = None
    if rank == 3:
        M = [B[0], B[1], B[2]]
        det = abs(M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1]) - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
                  + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))
    det_rule = all(in_lattice(B, v) for v in ((2, 0, 0), (0, 1, 0), (0, 0, 2)))
    inj = rank == 3 and det == 1
    print('   lattice %-38s basis %-40s rank %d index %s  contains 2Z x Z x 2Z: %s  Z^3: %s'
          % (name, B, rank, det, det_rule, inj))
    return B, rank, det, det_rule, inj
def K_elements(B):
    """the finite annihilator K of a full-rank lattice, as exponent triples x in [0,1)^3 (u_k = exp(2 pi i x_k))"""
    M = [B[0], B[1], B[2]]
    det = abs(M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1]) - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
              + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))
    out = []
    for x in itertools.product(range(det), repeat=3):
        xs = [Fr(t, det) for t in x]
        if all(sum(b[k] * xs[k] for k in range(3)).denominator == 1 for b in B): out.append(tuple(xs))
    return out
def perp(B):
    """an integer vector orthogonal to a rank-<3 lattice"""
    for n in itertools.product(range(-3, 4), repeat=3):
        if any(n) and all(sum(b[k] * n[k] for k in range(3)) == 0 for b in B): return n
ROOT = {Fr(0): ONE, Fr(1, 4): I_, Fr(1, 2): MONE, Fr(3, 4): -I_}

# ---- the carriers --------------------------------------------------------------------------------------------------
# Each carrier: a function on scaled H3 values (exact) and, when monomial on the torus, its exponent generators.
def Gram(H):          # act 12 FibreGram at |A| = 1, scaled by 16: G_i(j,k) = conj(h_ij) h_ik
    return [[[H[i][j].conj() * H[i][k] for k in range(N)] for j in range(N)] for i in range(N)]
def car_O0(H): return tuple(x.norm2() for r in H for x in r)                    # act 14 O0 / act 7 readback of |U|^2
def car_gram_raw(H): return tuple(x.key() for Gi in Gram(H) for r in Gi for x in r)
def car_feat4(H):     # the 4-cycle coordinates ((a,a',a'),(b,b',b)) of act 24's mixedTriple, scaled by 16^3
    Gm = Gram(H)
    return tuple((Gm[a][b][b2] * Gm[a2][b2][b] * Gm[a2][b][b]).key()
                 for a in range(N) for a2 in range(N) for b in range(N) for b2 in range(N))
def car_cross12(H):   # act 12 TG3 cross-invariant  G_{i0}(i1,i0) G_{i1}(i0,i1)
    Gm = Gram(H)
    return tuple((Gm[i0][i1][i0] * Gm[i1][i0][i1]).key() for i0 in range(N) for i1 in range(N))
def idx(a, b): return 4 * a + b
A35_IDX = [(a, b, b2, c, c2, d) for a, b, b2, c, c2, d in itertools.product(range(4), repeat=6)]
def car_a35(H):       # act 35 a35_shared_cross_core coordinates  G_{(a,b)}((c,d),(c',d)) G_{(a,b')}((c',d),(c,d))
    Gm = Gram(H)
    return tuple((Gm[idx(a, b)][idx(c, d)][idx(c2, d)] * Gm[idx(a, b2)][idx(c2, d)][idx(c, d)]).key()
                 for a, b, b2, c, c2, d in A35_IDX)
def pred_a35(H):      # the Boolean identity of act 35: every such coordinate equals 1/256 (scaled: 1)
    return all(v == (Fr(1), Fr(0)) for v in car_a35(H))
def car_O1(H):        # act 14 anchored channel at |A| = 1 on matrix units: O1(E_jk)_{ii'} = h_ij conj(h_i'k)
    return tuple((H[i][j] * H[i2][k].conj()).key() for i in range(N) for i2 in range(N) for j in range(N) for k in range(N))

# exponent generators on the torus
E = EXP
gens = {
    'O0 (visible slice)': [(0, 0, 0)],
    'FibreGram raw': [vadd(E[i][k], vneg(E[i][j])) for i in range(N) for j in range(N) for k in range(N)],
    'featureVec (4-cycles)': [vadd(vneg(E[a][b]), E[a][b2], vneg(E[a2][b2]), E[a2][b])
                              for a in range(N) for a2 in range(N) for b in range(N) for b2 in range(N)],
    'act-12 cross invariant': [vadd(vneg(E[i0][i1]), E[i0][i0], vneg(E[i1][i0]), E[i1][i1]) for i0 in range(N) for i1 in range(N)],
    'act-35 cross coordinates': [vadd(vneg(E[idx(a, b)][idx(c, d)]), E[idx(a, b)][idx(c2, d)],
                                      vneg(E[idx(a, b2)][idx(c2, d)]), E[idx(a, b2)][idx(c, d)]) for a, b, b2, c, c2, d in A35_IDX],
    'O1 anchored channel': [vadd(E[i][j], vneg(E[i2][k])) for i in range(N) for i2 in range(N) for j in range(N) for k in range(N)],
    'single-fibre feature coords': [vadd(vneg(E[i][j1]), E[i][j2], vneg(E[i][j2]), E[i][j3], vneg(E[i][j3]), E[i][j1])
                                    for i in range(N) for j1 in range(N) for j2 in range(N) for j3 in range(N)],
}

# ---- full featureVec exponent distribution (all 16^6 coordinates) -----------------------------------------------------
print('== section 1: the full feature-vector exponent distribution')
Dpair = [[Counter(vadd(vneg(E[i][j]), E[i][k]) for i in range(N)) for k in range(N)] for j in range(N)]
NM = Counter()
for j1 in range(N):
    for j2 in range(N):
        for j3 in range(N):
            for m1, c1 in Dpair[j1][j2].items():
                for m2, c2 in Dpair[j2][j3].items():
                    m12 = vadd(m1, m2); c12 = c1 * c2
                    for m3, c3 in Dpair[j3][j1].items():
                        NM[vadd(m12, m3)] += c12 * c3
check('the exponent distribution covers all 16^6 coordinates', sum(NM.values()), 16 ** 6)
B_full = hnf(list(NM.keys())); B_4 = hnf(gens['featureVec (4-cycles)'])
check('the full feature-vector lattice equals the 4-cycle lattice (cycle space of K16,16)',
      all(in_lattice(B_4, m) for m in NM) and all(in_lattice(B_full, m) for m in gens['featureVec (4-cycles)']), True)
print('   distinct exponents: %d; max |m_k| = %s' % (len(NM), tuple(max(abs(m[k]) for m in NM) for k in range(3))))

# sample check of the monomial structure psi_p(u) = psi_p(SIG) u^{m_p} on random full coordinates, exactly
random.seed(44)
Gs = Gram(SIG)
sample = [tuple(random.randrange(N) for _ in range(6)) for _ in range(1500)]
def psi(Gm, p): i1, i2, i3, j1, j2, j3 = p; return Gm[i1][j1][j2] * Gm[i2][j2][j3] * Gm[i3][j3][j1]
def mono(u, m): return gpow(u[0], m[0]) * gpow(u[1], m[1]) * gpow(u[2], m[2])
def m_of(p):
    i1, i2, i3, j1, j2, j3 = p
    return vadd(vneg(E[i1][j1]), E[i1][j2], vneg(E[i2][j2]), E[i2][j3], vneg(E[i3][j3]), E[i3][j1])
okmono = True
for name in ('F1-(-1,v2,v3)', 'O1(v1,v2,v3)', 'O5(v5,v6,v4)'):
    Gu = Gram(H3(PTS[name]))
    okmono &= all(psi(Gu, p) == psi(Gs, p) * mono(PTS[name], m_of(p)) for p in sample)
check('psi_p(H3(u)) = psi_p(SIG) u^{m_p} on 1500 random full coordinates at three points', okmono, True)

# ---- controls of the rule ------------------------------------------------------------------------------------------
print('== section 2: controls of the decision rule')
def monomial_verdict(name, gens_):
    B, rank, det, det_rule, inj = lattice_report(name, gens_)
    return det_rule, inj, B, rank
# C+1: the indicator
vals_L = {in_L(u) for u in PTS.values() if in_L(u)}; vals_C = {in_L(u) for u in PTS.values() if not in_L(u)}
check('C+1 indicator 1_L: images of L and of its complement are disjoint ({True} vs {False})', (vals_L, vals_C), ({True}, {False}))
# C+2 / C-3: monomial controls
d, inj, _, _ = monomial_verdict('C+2 (u1^2, u2, u3^2)', [(2, 0, 0), (0, 1, 0), (0, 0, 2)])
check('C+2 registers DETECTOR, not injective (specific)', (d, inj), (True, False))
d, inj, B, _ = monomial_verdict('C-3 (u1^2, u2^2, u3^2)', [(2, 0, 0), (0, 2, 0), (0, 0, 2)])
check('C-3 registers BLIND', d, False)
u, k = (V1, ONE, V3), (ONE, MONE, ONE)
uk = tuple(a * b for a, b in zip(u, k))
check('C-3 exhibited collision: (v1,1,v3) in L, (v1,-1,v3) not, same (u1^2,u2^2,u3^2)',
      (in_L(u), in_L(uk), tuple(x * x for x in u) == tuple(x * x for x in uk)), (True, False, True))
# C-2: the non-constant character u1 u2 u3
d, inj, _, _ = monomial_verdict('C-2 u1 u2 u3', [(1, 1, 1)])
u, uk = (ONE, V2, V2.conj()), (V2, V2, V2.conj() * V2.conj())
check('C-2 registers BLIND with an exhibited collision (1,v2,v2bar) in L vs (v2,v2,v2bar^2) off L',
      (d, in_L(u), in_L(uk), u[0] * u[1] * u[2] == uk[0] * uk[1] * uk[2]), (False, True, False, True))
# C-1: gauge-invariant constants: the realizability sum and the feature norm
def gram_sum(H):
    Gm = Gram(H)
    return tuple(sum((Gm[i][j][k] for i in range(N)), ZERO).key() for j in range(N) for k in range(N))
check('C-1 realizability sum sum_i G_i = 16 I (scaled) is constant: equal at F1+ (in L) and O1 (off L)',
      gram_sum(H3(PTS['F1+(1,v2,v3)'])) == gram_sum(H3(PTS['O1(v1,v2,v3)'])) == tuple(((Fr(16) if j == k else Fr(0)), Fr(0)) for j in range(N) for k in range(N)), True)
check('C-1 feature norm: sum_p |psi_p|^2 = 16^6 * (16^-3)^2 = 1 at every point (every |psi_p| = 16^-3)',
      sum(NM.values()) * Fr(1, 16 ** 6), Fr(1))

# ---- the carriers on the torus -------------------------------------------------------------------------------------
print('== section 3: monomial carriers on the torus (exact lattice criterion)')
RES = {}
for name, g in gens.items():
    B, rank, det, det_rule, inj = lattice_report(name, g)
    RES[name] = (B, rank, det, det_rule, inj)
B, rank, det, det_rule, inj = lattice_report('featureVec (all 16^6 coords)', list(NM.keys()))
RES['featureVec (all)'] = (B, rank, det, det_rule, inj)

# consistency control against act 40: the class must separate u2 = 1 from u2 = -1
check('consistency control: (0,1,0) lies in the feature-vector lattice', in_lattice(RES['featureVec (all)'][0], (0, 1, 0)), True)
check('featureVec detects L on the torus (lattice contains 2Z x Z x 2Z)', RES['featureVec (all)'][3], True)
if RES['featureVec (all)'][1] == 3:
    Kf = K_elements(RES['featureVec (all)'][0])
    print('   annihilator K of the feature lattice (turns):', Kf)
check('O0 is strongly blind (lattice 0: constant)', RES['O0 (visible slice)'][1], 0)
check('single-fibre feature coordinates are strongly blind (lattice 0)', RES['single-fibre feature coords'][1], 0)

# exact collisions / separations exhibited at points for the non-trivial class-level named carriers
COLL = {}
def collide(car, u, v):
    return car(H3(u)) == car(H3(v))
for name, car in (('act-12 cross invariant', car_cross12), ('act-35 cross coordinates', car_a35)):
    B, rank, det, det_rule, inj = RES[name]
    if det_rule:
        print('   %s: lattice criterion says DETECTOR' % name)
        continue
    # build k in K outside S = {+-1} x {1} x {+-1}
    if rank < 3:
        n = perp(B)
        t = V4
        k = (gpow(t, n[0]), gpow(t, n[1]), gpow(t, n[2]))
        print('   %s: rank %d, circle direction %s in K' % (name, rank, n))
    else:
        Ks = K_elements(B)
        bad = [x for x in Ks if not (x[1] == 0 and x[0] in (0, Fr(1, 2)) and x[2] in (0, Fr(1, 2)))]
        x = bad[0]
        assert all(t in ROOT for t in x), 'K element not Gaussian: %r' % (x,)
        k = tuple(ROOT[t] for t in x)
        print('   %s: K = %s; using k = %s' % (name, Ks, x))
    # choose u in L with uk off L, per the lemma's proof
    cands = [(ONE, V2, V3), (V1, ONE, V3), (V1, V2, ONE), (MONE, V5, V6), (V5, V6, MONE)]
    u = next(c for c in cands if in_L(c) and not in_L(tuple(a * b for a, b in zip(c, k))))
    uk = tuple(a * b for a, b in zip(u, k)); COLL[name] = (u, uk)
    check('%s: exhibited exact collision, u=%s in L, uk=%s off L, all %d values equal'
          % (name, u, uk, len(car(H3(u)))), (in_L(u), in_L(uk), collide(car, u, uk)), (True, False, True))

# act 35's Boolean identity at the test points
vals = {name: pred_a35(H3(u)) for name, u in PTS.items()}
print('   act-35 identity holds at:', [n for n, v in vals.items() if v])
check('act-35 Boolean identity: holds at SIG, fails at a face point (F1-) and an off-face point (O1) -> collision False/False',
      (vals['SIG(1,1,1)'], vals['F1-(-1,v2,v3)'], vals['O1(v1,v2,v3)']), (True, False, False))

# featureVec: explicit detector formula from single 4-cycle coordinates
print('== section 4: an explicit feature-vector detector on the torus')
four = [(a, a2, b, b2) for a in range(N) for a2 in range(N) for b in range(N) for b2 in range(N)]
def m4(q): a, a2, b, b2 = q; return vadd(vneg(E[a][b]), E[a][b2], vneg(E[a2][b2]), E[a2][b])
want = {}
for q in four:
    m = m4(q)
    for key_, targets in (('u1', ((1, 0, 0), (-1, 0, 0))), ('u2', ((0, 1, 0), (0, -1, 0))), ('u3', ((0, 0, 1), (0, 0, -1)))):
        if m in targets and key_ not in want: want[key_] = (q, m)
print('   single 4-cycle coordinates found (index (a, a2, b, b2), exponent):', want)
single_ok = len(want) == 3
check('three single 4-cycle coordinates carry exponents +-(1,0,0), +-(0,1,0), +-(0,0,1)', single_ok, True)
if single_ok:
    Gs = Gram(SIG)
    def c4(Gm, q): a, a2, b, b2 = q; return Gm[a][b][b2] * Gm[a2][b2][b] * Gm[a2][b][b]
    ref = {k_: c4(Gs, q) for k_, (q, m) in want.items()}
    def f_detect(H):
        """psi_q(u) = psi_q(SIG) u_k^{+-1} for the three coordinates, so u1 = +-1 iff psi_q1(u) = +-psi_q1(SIG), etc."""
        Gm = Gram(H)
        x1, x2, x3 = (c4(Gm, want[k_][0]) for k_ in ('u1', 'u2', 'u3'))
        return x1 in (ref['u1'], -ref['u1']) or x2 == ref['u2'] or x3 in (ref['u3'], -ref['u3'])
    check('f(featureVec) = [psi_q1 = +-psi_q1(SIG)] or [psi_q2 = psi_q2(SIG)] or [psi_q3 = +-psi_q3(SIG)] equals 1_L at all 13 test points',
          [f_detect(H3(u)) for u in PTS.values()], [in_L(u) for u in PTS.values()])

# ---- gauge behaviour ---------------------------------------------------------------------------------------------
print('== section 5: behaviour under the two-sided invisible gauge (D1 H D2)')
D1 = [V1, V2, V3, V4, V5, V6, I_, MONE, V1 * V2, V2 * V3, V3 * V4, V4 * V5, V5 * V6, V6 * V1, V1.conj(), V2.conj()]
D2 = [V6, V5.conj(), V4, V3, I_, V2, V1, MONE, V3 * V3, V4 * V1, ONE, V2 * V6, V5, V4.conj(), V6 * V6, V3.conj()]
def gauge(H, d1, d2): return [[d1[i] * H[i][j] * d2[j] for j in range(N)] for i in range(N)]
Hx = H3(PTS['O5(v5,v6,v4)'])
Hg = gauge(Hx, D1, D2); Hl = gauge(Hx, D1, [ONE] * N); Hr = gauge(Hx, [ONE] * N, D2)
check('O0 unchanged by D1 . D2', car_O0(Hg) == car_O0(Hx), True)
check('featureVec 4-cycle coordinates unchanged by D1 . D2 (act 24 mixedTriple_gauge + act 12 left invariance)', car_feat4(Hg) == car_feat4(Hx), True)
check('act-12 cross invariant unchanged by D1 . D2', car_cross12(Hg) == car_cross12(Hx), True)
check('act-35 coordinates unchanged by D1 . D2', car_a35(Hg) == car_a35(Hx), True)
check('raw FibreGram: unchanged by D1 (left fibre group), moved by D2 (weak anchored phases)',
      (car_gram_raw(Hl) == car_gram_raw(Hx), car_gram_raw(Hr) == car_gram_raw(Hx)), (True, False))
check('O1 moved by D1 (act 14 PQ1b analogue) and by D2', (car_O1(Hl) == car_O1(Hx), car_O1(Hr) == car_O1(Hx)), (False, False))
# O1 carries the Gram data: O1(E_jk)_{ii} = G_i(k, j)   (anchoredChannel_eq_trace + crossFibreGram_diag)
Gx = Gram(Hx)
check('O1(E_jk)_ii = G_i(k,j) for all i, j, k (the Gram data are output probabilities of O1 on coherent inputs)',
      all(Hx[i][j] * Hx[i][k].conj() == Gx[i][k][j] for i in range(N) for j in range(N) for k in range(N)), True)
# O1 determines H up to a global phase: h_ij conj(h_00) recovers H / h_00
check('O1 determines H up to one global phase (h_ij = O1(E_j0)_{i0} / conj(h_00), |h_00| = 1)',
      all(Hx[i][j] * Hx[0][0].conj() * Hx[0][0] == Hx[i][j] for i in range(N) for j in range(N)), True)

# ---- the scalar distance to SIG -----------------------------------------------------------------------------------
print('== section 6: a continuous scalar carrier -- act 24/26 distance to the stratum point')
def dist2(u):   # 16^6 * dist(featureVec(H3 u), featureVec(SIG))^2 = sum_m N(m) |u^m - 1|^2, exact
    s = Fr(0)
    for m, c in NM.items():
        x = mono(u, m) - ONE
        s += c * x.norm2()
    return s
d_vals = {name: dist2(PTS[name]) for name in ('SIG(1,1,1)', 'F1-(-1,v2,v3)', 'D-(-1,-1,-1)', 'F2(v1,1,v3)')}
print('   16^6 d^2 at face points:', {k_: float(v) for k_, v in d_vals.items()})
check('d(., SIG) is not constant on L: 0 at SIG, > 0 at (-1,-1,-1) -> not a detector by the topological lemma (collision exhibited in section 8)',
      (d_vals['SIG(1,1,1)'] == 0, d_vals['D-(-1,-1,-1)'] > 0), (True, True))

# ---- section 7: Boolean carriers defined in the repository (hull and stratum membership) -------------------------------
print('== section 7: act 35 hull membership and act 34 stratum membership (necessary conditions, exact)')
def gdiv(x, y): n = y.norm2(); c = x * y.conj(); return G(c.a / n, c.b / n)
def col_hull_necessary(H):
    """necessary conditions for D1 H D2 to be act 35's column construction X[a,c] D[c,b] Y_c[b,d] at the product index
    (row (a,b) -> 4a+b, column (c,d) -> 4c+d): rows of each class b proportional on each block c, and
    lambda(a,b,c)/lambda(a,0,c) independent of c (act 38 Hazard 5's relaxed form)"""
    for b in range(4):
        for c in range(4):
            for a, a2 in itertools.combinations(range(4), 2):
                for d, d2 in itertools.combinations(range(4), 2):
                    r, r2, s, s2 = 4 * a + b, 4 * a2 + b, 4 * c + d, 4 * c + d2
                    if H[r][s] * H[r2][s2] != H[r][s2] * H[r2][s]: return False
    lam = {(a, b, c): gdiv(H[4 * a + b][4 * c], H[b][4 * c]) for a in range(4) for b in range(4) for c in range(4)}
    return all(lam[(a, b, c)] * lam[(a, 0, 0)] == lam[(a, b, 0)] * lam[(a, 0, c)]
               for a in range(4) for b in range(4) for c in range(4))
def transpose(H): return [list(c) for c in zip(*H)]
hull_col = {n: col_hull_necessary(H3(u)) for n, u in PTS.items()}
hull_row = {n: col_hull_necessary(transpose(H3(u))) for n, u in PTS.items()}
print('   column-hull necessary conditions hold at:', [n for n, v in hull_col.items() if v])
print('   row-hull necessary conditions hold at:   ', [n for n, v in hull_row.items() if v])
check('control: SIG satisfies the column-hull conditions (a product is a column construction with D = 1)', hull_col['SIG(1,1,1)'], True)
fc = next((n for n in list(PTS)[:7] if not hull_col[n]), None); fr = next((n for n in list(PTS)[:7] if not hull_row[n]), None)
check('column-hull membership: exhibited collision, face point %s and off-face O1 both fail the necessary conditions' % fc,
      (fc is not None, hull_col['O1(v1,v2,v3)']), (True, False))
check('row-hull membership: exhibited collision, face point %s and off-face O1 both fail the necessary conditions' % fr,
      (fr is not None, hull_row['O1(v1,v2,v3)']), (True, False))
check('stratum membership: F1- (in L) and O1 (off L) both fail act 35 identity, hence both off the product stratum',
      (vals['F1-(-1,v2,v3)'], vals['O1(v1,v2,v3)']), (False, False))

# ---- section 8: the toy coordinate u1 and the distance to SIG -----------------------------------------------------------
print('== section 8: the toy u1 and exact collisions of the distance to SIG')
u, v = (V1, ONE, V3), (V1, V2, V3)
check('toy u1 separates a cross-boundary pair ((1,v2,v3) vs (v1,v2,v3)) but collides ((v1,1,v3) in L, (v1,v2,v3) off L)',
      (PTS['F1+(1,v2,v3)'][0] != PTS['O1(v1,v2,v3)'][0], in_L(u), in_L(v), u[0] == v[0]), (True, True, False, True))
# symmetries of the exponent distribution under signed permutations of the three axes
syms = []
for perm in itertools.permutations(range(3)):
    for sg in itertools.product((1, -1), repeat=3):
        def T(m, perm=perm, sg=sg):
            out = [0, 0, 0]
            for k in range(3): out[perm[k]] = sg[k] * m[k]
            return tuple(out)
        if all(NM[T(m)] == c for m, c in NM.items()): syms.append((perm, sg))
print('   signed axis permutations preserving the exponent distribution:', syms)
# a constructive exact collision: with N(m) = N(-m), f(u) = sum_m N(m) Re u^m = P0(u1,u3) + 2 Re(u2 Q(u1,u3)),
# Q = sum_{m2 = 1} N(m) u1^m1 u3^m3.  At fixed (a, b), u2 = conj(Q)/Q gives Re(u2 Q) = Re(Q), the value at u2 = 1.
check('the exponent distribution is symmetric under m -> -m', all(NM[vneg(m)] == c for m, c in NM.items()), True)
a_, b_ = V1, V3
Q = ZERO
for m, c in NM.items():
    if m[1] == 1: Q = Q + G(c) * gpow(a_, m[0]) * gpow(b_, m[2])
u2c = gdiv(Q.conj(), Q)
xL, yO = (a_, ONE, b_), (a_, u2c, b_)
print('   Q(v1, v3) = %s; reflected u2 = conj(Q)/Q = %s' % (Q, u2c))
check('distance to SIG: exhibited exact collision (v1, 1, v3) in L and (v1, conj(Q)/Q, v3) off L, equal 16^6 d^2',
      (in_L(xL), in_L(yO), u2c.norm2() == 1, dist2(xL) == dist2(yO)), (True, False, True, True))
print('   16^6 d^2 at both points: %s' % dist2(xL))


# ---- section 9: an independent certificate that the off-L collision points admit no Dita structure -------------------
# In a Dita form M[(a,b),(c,d)] = X[a,c] D[c,b] Y_c[b,d] (X m x m, Y_c n x n) the rows with a common b form a class of m
# rows, the columns with a common c a block of n columns, and two rows of one class have a ratio vector constant on every
# block.  Under D1 . D2 a ratio vector is multiplied by one constant, so its level-set partition is unchanged: the
# condition below is necessary for a structure strictly or up to diagonal equivalence.  Exhaustively at one exact point:
# for every shape (m, n) in {(4,4), (8,2), (2,8)} and both orientations, enumerate every partition of the rows into
# classes of m rows, each pair of a class having all ratio level sets of size >= n; for each, the common block partition
# must refine the meet of all those level-set partitions, so every part of the meet has size divisible by n.  No
# surviving partition for any shape and orientation certifies that the point admits no Dita structure.  This uses
# nothing from act 40.
print('== section 9: independent non-Dita certificates at the off-L points used in collisions')
def level_key(M, r, r2): return tuple(gdiv(M[r][c], M[r2][c]).key() for c in range(N))
def surviving_partitions(M, m, n):
    lk, adj = {}, {r: set() for r in range(N)}
    for r, r2 in itertools.combinations(range(N), 2):
        k = level_key(M, r, r2)
        if min(Counter(k).values()) >= n: adj[r].add(r2); adj[r2].add(r); lk[(r, r2)] = k
    parts = []
    def rec(unassigned, classes):
        if not unassigned: parts.append(list(classes)); return
        r = min(unassigned)
        for rest in itertools.combinations(sorted(adj[r] & unassigned), m - 1):
            if all(y in adj[x] for x, y in itertools.combinations(rest, 2)):
                rec(unassigned - {r, *rest}, classes + [(r,) + rest])
    rec(set(range(N)), [])
    alive = 0
    for P in parts:
        keys = [lk[pr] for cl in P for pr in itertools.combinations(sorted(cl), 2)]
        meet = Counter(tuple(k[c] for k in keys) for c in range(N))
        if all(v % n == 0 for v in meet.values()): alive += 1
    return alive
def dita_necessary(H):
    return any(surviving_partitions(M, m, n) > 0 for M in (H, transpose(H)) for m, n in ((4, 4), (8, 2), (2, 8)))
cert_pts = {'O1(v1,v2,v3)': PTS['O1(v1,v2,v3)'], 'distance collision (v1,conj(Q)/Q,v3)': yO,
            'C-3 absent face (v1,-1,v3)': (V1, MONE, V3), 'O5(v5,v6,v4)': PTS['O5(v5,v6,v4)']}
for name_, (u_, uk_) in COLL.items(): cert_pts[name_ + ' collision partner'] = uk_
for name, u in cert_pts.items():
    check('no Dita structure at %s (necessary condition fails for every shape and orientation)' % name,
          dita_necessary(H3(u)), False)
for name in list(PTS)[:7]:
    check('control: the necessary condition holds at face point %s' % name, dita_necessary(H3(PTS[name])), True)


# ---- section 10: implementation-class predicates on the matrix itself --------------------------------------------------
print('== section 10: matrix-class predicates (LieRankSource.diagClass, permClass, IsMonomial, PreservesNonneg o conjChannel)')
def is_diag(H): return all(H[i][j] == ZERO for i in range(N) for j in range(N) if i != j)
def is_submonomial(H): return all(sum(1 for j in range(N) if H[i][j] != ZERO) <= 1 for i in range(N)) and \
                              all(sum(1 for i in range(N) if H[i][j] != ZERO) <= 1 for j in range(N))
def conj_preserves_nonneg_E11(H):   # conjChannel H applied to the nonnegative matrix unit E_11: entries h_i1 conj(h_k1)
    return all((H[i][1] * H[k][1].conj()).b == 0 and (H[i][1] * H[k][1].conj()).a >= 0 for i in range(N) for k in range(N))
for label, pred in (('diagClass', is_diag), ('submonomial (permClass, IsMonomial need it)', is_submonomial),
                    ('conjChannel preserves nonnegativity on E_11', conj_preserves_nonneg_E11)):
    vals_ = [pred(H3(u)) for u in PTS.values()]
    check('%s is False at all 13 points; collision F1+ (in L) vs O1 (off L)' % label, (set(vals_), vals_[1] == vals_[7]), ({False}, True))
check('symbolically: h_01 conj(h_21) = SIG_01 conj(SIG_21) = -1 for every u (both exponents zero)',
      (EXP[0][1], EXP[2][1], (SIG[0][1] * SIG[2][1].conj()).key()), ((0, 0, 0), (0, 0, 0), (Fr(-1), Fr(0))))

print('== summary: %d failures, %.1f s' % (len(FAILS), time.time() - T0))
if FAILS:
    print('FAILED:', FAILS); sys.exit(1)
print('bridge_probe: OK')
