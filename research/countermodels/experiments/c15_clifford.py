# c15_clifford.py -- research/countermodels extra node C15 (round 3): an explicit exotic cone for the native Clifford
# family <cnot, actC cyc3, actT cyc3> (the group of the finite half of A_miss in the overview; definition only).
# DECISION RULE (fixed before the first run, 2026-10-11T01:08:11Z by date -u; predictions in NOTES-C15 S0, 01:07:47Z):
#  Exact arithmetic only (int, Fraction, Gaussian rationals GQ); no float (guard EX). Conventions as in c11_octahedral.py.
#  D0  PC, PT, SGN equal the Lean text of CompositeDimension.lean at L.
#  G1  closure of {cnot, actC cyc3, actT cyc3} as signed permutations of the 16 coordinates: order 11520 (record), each
#      element fixes E00.
#  G2  Ad(CNOT) = cnot, Ad(UJ (x) I) = actC cyc3, Ad(I (x) UJ) = actT cyc3 on the 16 basis tables (UJ = (I - i(X+Y+Z))/2),
#      so Ad maps the lifted group onto the G1 group ([W]: a homomorphism whose kernel is the scalar matrices).
#  X1  h = (-480+7i, 357+870i, 939+834i, 448+486i): the orbit of the ray of h under the three lifted generators (breadth-first
#      search on canonical rays, v / first nonzero entry) -- record its size; for every orbit ray v: det ratio d(v) > 0
#      (no product) and 1 - 4 d(v) <= (2/c - 1)^2 at c = 100001/100000 (H1: c lambda_max <= 1); for every orbit ray v != [h]:
#      s(h, v) > 0, and with s_min the minimum, c^2 s_min >= 4(c - 1) ((CC) for every pair of the orbit, [W]: s(gh, g'h) =
#      s(h, g^-1 g' h)).
#  CC1 4 phi0 = (1, 2, 3i, -1+i): its orbit contains a ray v with <phi0|v> = 0 exactly (an orthogonal pair: S' unavailable).
#  VERDICT C15-CLIFFORD-EXACT iff every CHECK passes and the countercontrol behaves as stated; else NO VERDICT.
import re
from fractions import Fraction as Fr

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
def M(rows): return [[x if isinstance(x, GQ) else GQ(x) for x in r] for r in rows]
def mmul(A, B): return [[sum((A[i][t] * B[t][j] for t in range(len(B))), ZERO) for j in range(len(B[0]))] for i in range(len(A))]
def dag(A): return [[A[j][i].conj() for j in range(len(A))] for i in range(len(A[0]))]
def kron(A, B): return [[A[i // 2][j // 2] * B[i % 2][j % 2] for j in range(4)] for i in range(4)]
def madd(A, B): return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def mscale(c, A): return [[c * x for x in r] for r in A]
def mv(A, v): return [sum((A[i][t] * v[t] for t in range(4)), ZERO) for i in range(4)]
def ipv(u, v): return sum((u[t].conj() * v[t] for t in range(4)), ZERO)
def n2v(v): return sum((x.n2() for x in v), Fr(0))
def ovl(u, v): return ipv(u, v).n2() / (n2v(u) * n2v(v))
def detr(v): return (v[0] * v[3] - v[1] * v[2]).n2() / n2v(v) ** 2
def canon(v):
    k = next(t for t in range(4) if not v[t].iszero()); a = v[k]; return tuple(x / a for x in v)

s0 = M([[1, 0], [0, 1]]); sx = M([[0, 1], [1, 0]]); sy = M([[0, GQ(0, -1)], [II, 0]]); sz = M([[1, 0], [0, -1]])
SIG = [s0, sx, sy, sz]
SS = [[kron(SIG[m], SIG[n]) for n in range(4)] for m in range(4)]
SSP = [[[(i, j, SS[m][n][j][i]) for i in range(4) for j in range(4) if not SS[m][n][j][i].iszero()] for n in range(4)] for m in range(4)]
def pW(w): return [[sum((GQ(w[m][n]) * SS[m][n][i][j] for m in range(4) for n in range(4) if w[m][n] != 0), ZERO) / 4 for j in range(4)] for i in range(4)]
def table(A):
    t = [[sum((A[i][j] * val for i, j, val in SSP[m][n]), ZERO) for n in range(4)] for m in range(4)]
    assert all(x.i == 0 for r in t for x in r), 'non-real table'
    return [[x.r for x in r] for r in t]
def Eb(m, n): w = [[0] * 4 for _ in range(4)]; w[m][n] = 1; return w
BASIS = [Eb(m, n) for m in range(4) for n in range(4)]

SGN = lambda m, n: -1 if (m, n) in [(1, 3), (2, 2)] else 1
PC = [[0, 0, 3, 3], [1, 1, 2, 2], [2, 2, 1, 1], [3, 3, 0, 0]]
PT = [[0, 1, 2, 3], [1, 0, 3, 2], [1, 0, 3, 2], [0, 1, 2, 3]]
src = open('../../../verification/lean-mathlib/OIBridge/CompositeDimension.lean', encoding='utf-8').read()
def lean_table(name):
    blk = re.search(r'def %s : Fin 4 → Fin 4 → Fin 4\n((?:  \|.*\n){4})' % name, src).group(1)
    tab = [[None] * 4 for _ in range(4)]
    for a, b, v in re.findall(r'(\d), (\d) => (\d)', blk): tab[int(a)][int(b)] = int(v)
    return tab
sgn_ok = re.search(r'def sgn \(μ ν : Fin 4\) : ℝ := if \(μ = 1 ∧ ν = 3\) ∨ \(μ = 2 ∧ ν = 2\) then -1 else 1', src) is not None
rec('CHECK', 'D0', lean_table('pc') == PC and lean_table('pt') == PT and sgn_ok, 'PC, PT, SGN equal the Lean text (CompositeDimension.lean:741-755 at L)')

def cnotT(w): return [[SGN(m, n) * w[PC[m][n]][PT[m][n]] for n in range(4)] for m in range(4)]
def Hom(N): return [[1, 0, 0, 0]] + [[0] + list(r) for r in N]
def actC(N): Hm = Hom(N); return lambda w: [[sum(Hm[m][k] * w[k][n] for k in range(4)) for n in range(4)] for m in range(4)]
def actT(N): Hm = Hom(N); return lambda w: [[sum(w[m][k] * Hm[n][k] for k in range(4)) for n in range(4)] for m in range(4)]
cyc3 = [[0, 0, 1], [1, 0, 0], [0, 1, 0]]
def as_sp(f):
    out = []
    for b in BASIS:
        w = f(b); nz = [(m * 4 + n, w[m][n]) for m in range(4) for n in range(4) if w[m][n] != 0]
        assert len(nz) == 1 and nz[0][1] in (1, -1); out.append(nz[0])
    return tuple(out)
def compose(p, q): return tuple((p[i][0], p[i][1] * s) for (i, s) in q)
gens_sp = [as_sp(cnotT), as_sp(actC(cyc3)), as_sp(actT(cyc3))]
idsp = tuple((i, 1) for i in range(16))
GRP = {idsp}; fr = [idsp]
while fr:
    nf = []
    for a in fr:
        for g in gens_sp:
            b = compose(g, a)
            if b not in GRP: GRP.add(b); nf.append(b)
    fr = nf
rec('CHECK', 'G1', len(GRP) == 11520 and all(p[0] == (0, 1) for p in GRP), 'closure of {cnot, actC cyc3, actT cyc3} as signed permutations', 'order %d' % len(GRP))

P0 = M([[1, 0], [0, 0]]); P1 = M([[0, 0], [0, 1]])
CNOT = madd(kron(P0, s0), kron(P1, sx))
UJ = mscale(GQ(Fr(1, 2)), madd(s0, mscale(GQ(0, -1), madd(madd(sx, sy), sz))))
def Ad_sp(U):
    out = []
    for b in BASIS:
        w = table(mmul(mmul(U, pW(b)), dag(U)))
        nz = [(m * 4 + n, w[m][n]) for m in range(4) for n in range(4) if w[m][n] != 0]
        if len(nz) != 1 or nz[0][1] not in (1, -1): return None
        out.append((nz[0][0], int(nz[0][1])))
    return tuple(out)
GU = [CNOT, kron(UJ, s0), kron(s0, UJ)]
rec('CHECK', 'G2', [Ad_sp(U) for U in GU] == gens_sp and mmul(UJ, dag(UJ)) == M([[1, 0], [0, 1]]), 'Ad(CNOT), Ad(UJ (x) I), Ad(I (x) UJ) are cnot, actC cyc3, actT cyc3 (the lift maps onto G1)')

def orbit(h):
    start = canon(h); seen = {start}; fr = [list(start)]
    while fr:
        nf = []
        for v in fr:
            for U in GU:
                w = canon(mv(U, v))
                if w not in seen: seen.add(w); nf.append(list(w))
        fr = nf
    return [list(v) for v in seen]
h = [GQ(-480, 7), GQ(357, 870), GQ(939, 834), GQ(448, 486)]
c = Fr(100001, 100000)
orb = orbit(h)
dets = [detr(v) for v in orb]
h1 = all(d > 0 for d in dets) and all(1 - 4 * d <= (2 / c - 1) ** 2 for d in dets)
hc = canon(h)
ovs = [ovl(h, v) for v in orb if tuple(v) != hc]
smin = min(ovs)
cc = smin > 0 and c * c * smin >= 4 * (c - 1)
rec('CHECK', 'X1', len(orb) == 11520 and h1 and cc,
    'h\'s orbit: 11520 rays, no product, H1 at c = 100001/100000, no orthogonal pair and (CC) for every pair: K(G (I - cP_h)) is explicit given Theorem S\'',
    'orbit %d rays; min det ratio %s (~%s); s_min %s (~%s)' % (len(orb), min(dets), str(round(min(dets).numerator * 10 ** 6 // min(dets).denominator)) + 'e-6', smin, str(smin.numerator * 10 ** 9 // smin.denominator) + 'e-9'))
phi = [GQ(1), GQ(2), GQ(0, 3), GQ(-1, 1)]
orbp = orbit(phi)
cc1 = any(ipv(phi, v).iszero() for v in orbp)
rec('COUNTERCONTROL', 'CC1', cc1, '4 phi0 = (1, 2, 3i, -1+i) has an exactly orthogonal ray in its orbit (S\' unavailable for it)', 'orbit %d rays' % len(orbp))

def nofloat(x):
    if isinstance(x, float): return False
    if isinstance(x, (list, tuple)): return all(nofloat(y) for y in x)
    return True
rec('CHECK', 'EX', nofloat([c, smin, min(dets)]), 'no float in any recorded value')
nf = sum(1 for r in RES if not r)
print('summary: %d checks, %d failed' % (len(RES), nf))
if nf == 0:
    print('VERDICT C15-CLIFFORD-EXACT: <cnot, actC cyc3, actT cyc3> has order %d; the orbit of h has %d product-free rays with no '
          'orthogonal pair (s_min = %s); at c = %s H1 and (CC) hold: an explicit invariant exotic cone given Theorem S\'' % (len(GRP), len(orb), smin, c))
else:
    print('NO VERDICT')
