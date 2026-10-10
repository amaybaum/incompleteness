#!/usr/bin/env python3
"""Coordinator's independent check of the research/origin thread's round-2 exact claims (branch head 42bc3da6).
Own code; reads nothing.  Run: python3 -I -B indep_checkO2.py
DECISION RULE (fixed before the first run): CONFIRMED/MISMATCH per line; INDEP-O2-FIXED iff all CONFIRMED.
 X1 (O7-D1) R01 = rot(pi/4) on the pair (0,1), R12 = rot(pi/4) on (1,2), as 3x3 rotations: U = R01 R12 has
    2 cos(theta) = sqrt2 - 1/2 with minimal polynomial x^2 + x - 7/4 (not monic over Z: infinite order); R01 has order
    8; the only real eigenline of R01 is e2 and of R12 is e0, so no line is invariant under both; R01 moves the axis of
    U off its line.  With the classification of closed subgroups of SO(3) [L] (finite, SO(2), O(2), SO(3); the finite
    ones containing an element of order 8 are cyclic or dihedral and fix a line; SO(2) and O(2) fix a line) the closure
    of <R01, R12> is SO(3): the thread's density certificate.
 X2 (O7-D2) the Hadamard pair H01 = H (+) 1, H12 = 1 (+) H (reflections, det -1): U' = H01 H12 has 2 cos = -3/2
    (infinite order) and BOTH reflections fix the axis of U' exactly, so <H01, H12> is infinite dihedral about that
    axis and its closure is a proper closed subgroup (the stabilizer of the axis, a copy of O(2)): the thread's
    correction of the coordinator's round-1 reading (X5 of indep_checkO: infinite order, not density).
 X3 (O5-T1a) exclusivity: on Omega = {0,1}^2 with all 24 exchanges and ONE passive repeatable readout of any one of
    the 14 nontrivial set partitions of Omega, every point mass is reachable from the uniform seed (exact BFS over
    posteriors), so the body is the full simplex whatever further instruments are added.
 X4 (O5-KB1) the KB-D instrument on the z-partition equals forget_x o Luders_z branch by branch (symbolic p).
 X5 (O6-I) the Kochen-Specker circle tower: with rho_psi(l) = cos(l - psi)/2 on |l - psi| < pi/2 and the half-circle
    readout at u, P(up at u | psi) = (1 + cos(u - psi))/2 exactly (symbolic integral), repeatable (= 1 at u = psi);
    on the Pythagorean stages (directions k a, cos a = 3/5, |k| <= n, n = 1..4) the exact table of single and two-step
    readouts has rank 3; e^{ia} has minimal polynomial 5x^2 - 6x + 5 (not monic: infinite order); the closure member
    R(pi/2) gives the balanced value 1/2 from psi = 0 while no stage datum k a does (T_k(3/5) != 0 for 1 <= k <= 60).
 X6 (O7-L3) level three, exact over Q(sqrt2): M1 = mixImage 3 (pi/4) = rot(pi/4) (x) I_3 on Fin 2 x Fin 3, M2 = P M1 P^T
    with P the shift (s, k) -> (s, k + s mod 3), U = M1 M2 orthogonal; Pi = (2/3)(U + U^T) is a projector of rank 4
    commuting with U, with U + U^T = 0 on its complement (U^2 = -1 there) and 2 cos(theta) = 3/2 on its range (infinite
    order); Y = Pi (U - U^T) Pi / 2 lies in the Lie algebra of the closure of <U> (the circle {cos(phi) + sin(phi) J}
    on the range of Pi, since U^{4k} is dense in it).  The Lie algebra generated from Y under conjugation by the five
    adjacent transpositions (which generate S_6) and by M1, M1^T and under brackets has dimension 15 = dim so(6);
    under the transpositions alone it has dimension 10 and annihilates the all-ones vector (so(5) of that hyperplane);
    the countercontrol Y0 = (e0 - e1)(e2 - e3)^T - (e2 - e3)(e0 - e1)^T under the transpositions alone stays at 10.
    With Cartan's closed-subgroup theorem [L] this gives: the closure of <M1, permutations> contains SO(6).
"""
import itertools
from fractions import Fraction as Fr
import sympy as sp
from sympy import Matrix, Rational as Q, sqrt, simplify, cos, sin, pi, symbols, integrate, I
R = []
def rec(cid, ok, text, detail=""):
    ok = bool(ok); R.append(ok)
    print(f"{'CONFIRMED' if ok else 'MISMATCH'} {cid} {text}" + (f" -- {detail}" if detail else ""))
print("== X1 density certificate on three states")
c = s = sqrt(2) / 2
R01 = Matrix([[c, -s, 0], [s, c, 0], [0, 0, 1]]); R12 = Matrix([[1, 0, 0], [0, c, -s], [0, s, c]])
U = R01 * R12; twocos = simplify(U.trace() - 1)
x = symbols('x'); minpoly = sp.minimal_polynomial(twocos, x)
order8 = (R01 ** 8 == sp.eye(3)) and all(simplify(R01 ** k - sp.eye(3)) != sp.zeros(3, 3) for k in range(1, 8))
def real_eigenlines(M):
    return [v for val, mult, vecs in M.eigenvects() if val.is_real for v in vecs]
l01 = real_eigenlines(R01); l12 = real_eigenlines(R12)
axisU = (U - sp.eye(3)).nullspace()[0]
moved = simplify(axisU.cross(R01 * axisU)) != sp.zeros(3, 1)
common = any(simplify(a.cross(b)) == sp.zeros(3, 1) for a in l01 for b in l12)
rec('X1', simplify(twocos - (sqrt(2) - Q(1, 2))) == 0 and sp.Poly(minpoly, x).all_coeffs() == [1, 1, Q(-7, 4)] and order8 and len(l01) == 1 and len(l12) == 1 and not common and moved,
    '2cos = sqrt2 - 1/2 (min poly x^2 + x - 7/4), R01 of order 8, no common invariant line, R01 moves the axis of U: closure SO(3) with [L]', 'min poly %s' % minpoly)
print("== X2 the Hadamard pair is dihedral about one axis")
H = Matrix([[1, 1], [1, -1]]) / sqrt(2)
H01 = sp.diag(H, 1); H12 = sp.diag(1, H); Up = H01 * H12
axisUp = (Up - sp.eye(3)).nullspace()[0]
fixed = simplify(H01 * axisUp - axisUp) == sp.zeros(3, 1) and simplify(H12 * axisUp - axisUp) == sp.zeros(3, 1)
rec('X2', simplify(Up.trace() - 1 + Q(3, 2)) == 0 and H01.det() == -1 and H12.det() == -1 and fixed and simplify(H01 ** 2 - sp.eye(3)) == sp.zeros(3, 3),
    "2cos = -3/2 (infinite order) but both reflections fix the axis of U': infinite dihedral, closure a proper O(2)", 'axis %s' % list(axisUp))
print("== X3 exclusivity on the 14 nontrivial partitions")
Om = [(0, 0), (0, 1), (1, 0), (1, 1)]
def set_partitions(elems):
    if not elems: yield []; return
    first, rest = elems[0], elems[1:]
    for p in set_partitions(rest):
        for i in range(len(p)): yield p[:i] + [[first] + p[i]] + p[i + 1:]
        yield [[first]] + p
parts = [p for p in set_partitions(list(range(4))) if len(p) > 1]
perms = list(itertools.permutations(range(4)))
def reach(part):
    start = (Fr(1, 4),) * 4; seen = {start}; frontier = [start]
    while frontier:
        nxt = []
        for st in frontier:
            outs = []
            for g in perms: outs.append(tuple(st[g[i]] for i in range(4)))
            for block in part:
                m = sum(st[i] for i in block)
                if m > 0: outs.append(tuple((st[i] / m if i in block else Fr(0)) for i in range(4)))
            for o in outs:
                if o not in seen: seen.add(o); nxt.append(o)
        frontier = nxt
    return seen
pm = {tuple(Fr(1) if i == j else Fr(0) for i in range(4)) for j in range(4)}
ok3 = len(parts) == 14 and all(pm <= reach(p) for p in parts)
rec('X3', ok3, 'with the exchanges and one passive readout of any of the 14 nontrivial partitions every point mass is reachable: the body is the simplex', '%d partitions' % len(parts))
print("== X4 KB-D instrument = forget_x o Luders_z")
p00, p01, p10, p11 = symbols('p00 p01 p10 p11', positive=True)
pvec = [p00, p01, p10, p11]
def luders_z(p, a): m = p[2 * a] + p[2 * a + 1]; return [p[i] / m if i // 2 == a else 0 for i in range(4)]
def forget_x(q): return [(q[2 * (i // 2)] + q[2 * (i // 2) + 1]) / 2 for i in range(4)]
kbd = {a: [Q(1, 2) if i // 2 == a else 0 for i in range(4)] for a in (0, 1)}
ok4 = all(all(simplify(u - v) == 0 for u, v in zip(forget_x(luders_z(pvec, a)), kbd[a])) for a in (0, 1))
rec('X4', ok4, 'forget_x(Luders_z(p | z = a)) is the uniform posterior on the cell {z = a}, branch by branch')
print("== X5 the Kochen-Specker circle tower")
lam, beta = symbols('lam beta', real=True)
P_up = integrate(cos(lam) / 2, (lam, beta - pi / 2, pi / 2))             # 0 < beta < pi: overlap of the two half-circles
law = simplify(P_up - (1 + cos(beta)) / 2) == 0 and simplify(P_up.subs(beta, 0)) == 1
def cs(k):   # exact (cos ka, sin ka) with cos a = 3/5
    z = complex(1, 0); c0, s0 = Fr(3, 5), Fr(4, 5); cr, sr = Fr(1), Fr(0)
    for _ in range(abs(k)): cr, sr = cr * c0 - sr * s0, sr * c0 + cr * s0
    return (cr, sr if k >= 0 else -sr)
def resp(u, psi): return (1 + u[0] * psi[0] + u[1] * psi[1]) / 2
def frank(rows):
    rows = [list(r) for r in rows]; rk = 0; ncol = len(rows[0])
    for col in range(ncol):
        piv = next((r for r in range(rk, len(rows)) if rows[r][col] != 0), None)
        if piv is None: continue
        rows[rk], rows[piv] = rows[piv], rows[rk]
        for r in range(len(rows)):
            if r != rk and rows[r][col] != 0:
                f = rows[r][col] / rows[rk][col]; rows[r] = [a - f * b for a, b in zip(rows[r], rows[rk])]
        rk += 1
    return rk
ranks = []
for n in range(1, 5):
    dirs = [cs(k) for k in range(-n, n + 1)]
    tab = [[resp(u, psi) for u in dirs] + [resp(u, psi) * resp(u2, u) for u in dirs for u2 in dirs] for psi in dirs]
    ranks.append(frank(tab))
mp = sp.minimal_polynomial(Q(3, 5) + Q(4, 5) * I, x); mp_coeffs = sp.Poly(mp, x).all_coeffs()
infinite = mp_coeffs == [1, Q(-6, 5), 1] or mp_coeffs == [5, -6, 5]
T = [Fr(1), Fr(3, 5)]
for k in range(2, 61): T.append(2 * Fr(3, 5) * T[-1] - T[-2])
no_stage_witness = all(T[k] != 0 for k in range(1, 61))
closure_witness = resp(cs(0), (Fr(0), Fr(1))) == Fr(1, 2)        # psi rotated by pi/2 read along u = 0
rec('X5', law and ranks == [3, 3, 3, 3] and infinite and no_stage_witness and closure_witness,
    'cosine law exact and repeatable; stage tables rank 3; e^{ia} of infinite order; 1/2 only for the closure member R(pi/2)', 'ranks %s, min poly %s' % (ranks, mp))
print("== X6 level three: Lie algebra of the closure")
class Q2:
    __slots__ = ('a', 'b')
    def __init__(self, a=0, b=0): self.a = Fr(a); self.b = Fr(b)
    def __add__(self, o): o = cv(o); return Q2(self.a + o.a, self.b + o.b)
    __radd__ = __add__
    def __neg__(self): return Q2(-self.a, -self.b)
    def __sub__(self, o): return self + (-cv(o))
    def __mul__(self, o): o = cv(o); return Q2(self.a * o.a + 2 * self.b * o.b, self.a * o.b + self.b * o.a)
    __rmul__ = __mul__
    def inv(self): d = self.a * self.a - 2 * self.b * self.b; return Q2(self.a / d, -self.b / d)
    def __truediv__(self, o): return self * cv(o).inv()
    def __eq__(self, o): o = cv(o); return self.a == o.a and self.b == o.b
    def zero(self): return self.a == 0 and self.b == 0
    def __repr__(self): return "(%s+%s r2)" % (self.a, self.b)
def cv(v): return v if isinstance(v, Q2) else Q2(v, 0)
N = 6
def mz(): return [[Q2() for _ in range(N)] for _ in range(N)]
def mid(): M = mz(); [M[i].__setitem__(i, Q2(1)) for i in range(N)]; return M
def mmul(A, B): return [[sum((A[i][k] * B[k][j] for k in range(N)), Q2()) for j in range(N)] for i in range(N)]
def mT(A): return [[A[j][i] for j in range(N)] for i in range(N)]
def madd(A, B): return [[A[i][j] + B[i][j] for j in range(N)] for i in range(N)]
def msub(A, B): return [[A[i][j] - B[i][j] for j in range(N)] for i in range(N)]
def msc(c, A): return [[cv(c) * A[i][j] for j in range(N)] for i in range(N)]
def meq(A, B): return all((A[i][j] - B[i][j]).zero() for i in range(N) for j in range(N))
def vec(A): return [A[i][j] for i in range(N) for j in range(N)]
def idx(s_, k): return 3 * s_ + k
h = Q2(0, Fr(1, 2))                       # sqrt2 / 2 = cos(pi/4) = sin(pi/4)
M1 = mz()
for k in range(3):
    M1[idx(0, k)][idx(0, k)] = h; M1[idx(0, k)][idx(1, k)] = -h; M1[idx(1, k)][idx(0, k)] = h; M1[idx(1, k)][idx(1, k)] = h
Pm = mz()
for s_ in range(2):
    for k in range(3): Pm[idx(s_, (k + s_) % 3)][idx(s_, k)] = Q2(1)
M2 = mmul(mmul(Pm, M1), mT(Pm)); Um = mmul(M1, M2); UmT = mT(Um)
orth = meq(mmul(UmT, Um), mid())
Pi = msc(Fr(2, 3), madd(Um, UmT))
proj = meq(mmul(Pi, Pi), Pi) and meq(mT(Pi), Pi) and meq(mmul(Um, Pi), mmul(Pi, Um))
trPi = sum((Pi[i][i] for i in range(N)), Q2())
compl = meq(mmul(madd(Um, UmT), msub(mid(), Pi)), mz())            # U + U^T = 0 off the range of Pi
onV = meq(mmul(madd(Um, UmT), Pi), msc(Fr(3, 2), Pi))              # 2 cos(theta) = 3/2 on the range
Y = msc(Fr(1, 2), mmul(mmul(Pi, msub(Um, UmT)), Pi))
class Ech:
    def __init__(self): self.rows = []       # list of (pivot, vector) fully reduced
    def insert(self, v):
        v = list(v)
        for p, w in self.rows:
            if not v[p].zero():
                f = v[p] / w[p]; v = [a - f * b for a, b in zip(v, w)]
        piv = next((i for i, a in enumerate(v) if not a.zero()), None)
        if piv is None: return False
        for j, (p, w) in enumerate(self.rows):
            if not w[piv].zero():
                f = w[piv] / v[piv]; self.rows[j] = (p, [a - f * b for a, b in zip(w, v)])
        self.rows.append((piv, v)); return True
def lie_closure(seed, conj):
    basis = []; ech = Ech(); queue = [seed]
    while queue:
        v = queue.pop(0)
        if not ech.insert(vec(v)): continue
        basis.append(v)
        for g, gi in conj: queue.append(mmul(mmul(g, v), gi))
        for w in basis: queue.append(msub(mmul(v, w), mmul(w, v)))
    return basis
transp = []
for i in range(5):
    Tm = mid(); Tm[i][i] = Q2(); Tm[i + 1][i + 1] = Q2(); Tm[i][i + 1] = Q2(1); Tm[i + 1][i] = Q2(1); transp.append((Tm, Tm))
conj_perm = transp; conj_full = transp + [(M1, mT(M1)), (mT(M1), M1)]
Lp = lie_closure(Y, conj_perm); Lf = lie_closure(Y, conj_full)
ones = [Q2(1)] * N
def annihilates_ones(A): return all(sum((A[i][j] for j in range(N)), Q2()).zero() for i in range(N))
def skew(A): return meq(mT(A), msc(-1, A))
Y0 = mz()
for (i, j, sgn) in ((0, 2, 1), (0, 3, -1), (1, 2, -1), (1, 3, 1)):
    Y0[i][j] = Q2(sgn); Y0[j][i] = Q2(-sgn)
L0 = lie_closure(Y0, conj_perm)
ok6 = orth and proj and trPi == Q2(4) and compl and onV and len(Lp) == 10 and all(annihilates_ones(A) and skew(A) for A in Lp) and len(Lf) == 15 and all(skew(A) for A in Lf) and len(L0) == 10
rec('X6', ok6, 'U orthogonal; Pi a rank-4 projector commuting with U; U + U^T = 0 off it and = (3/2) Pi on it; Lie closure of Y: 10 under the permutations (inside so(5) of the all-ones hyperplane), 15 = so(6) with Ad(M1); countercontrol Y0 stays at 10',
    'dims perm-only %d, full %d, countercontrol %d; trace Pi = %s' % (len(Lp), len(Lf), len(L0), trPi))
print("SUMMARY %d/%d CONFIRMED" % (sum(R), len(R)))
print("INDEP-O2-FIXED" if all(R) else "INDEP-O2-MISMATCH")
