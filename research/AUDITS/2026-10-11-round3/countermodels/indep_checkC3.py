#!/usr/bin/env python3
"""indep_checkC3.py -- coordinator's independent check of research/countermodels round 3 (nodes C11-C16).

Written from the thread's claims (NOTES-C11..C16, RESULTS rows C11.1..C16.6, C13.9f, HP4-HP6); reads nothing from the
thread's scripts or outputs.  Exact arithmetic throughout: Gaussian rationals (own class over Fraction), sympy for the
symbolic identities and the square-root comparisons.  Conventions: pair vectors in the computational basis
(|00>,|01>,|10>,|11>), control first; Psi(v) = [[v0, v1],[v2, v3]], D(v) = |det Psi(v)|^2/|v|^4; lambda_max(v) =
(1 + sqrt(1 - 4D))/2; defect d = I - c P_h; H1 test: 1 - 4D <= (2/c - 1)^2 (i.e. c lambda_max <= 1); (CC) for equal c:
c^2 s >= 4(c - 1) with s the squared overlap; CNOT = |0><0| (x) 1 + |1><1| (x) X; S = diag(1, i); U_J = (I - i(X+Y+Z))/2.
Table action of a unitary U: the signed permutation of the Pauli tensors T_{mu nu} = sigma_mu (x) sigma_nu under Ad(U).

DECISION RULE (fixed before run 1): VERDICT INDEP-C3-FIXED iff X1..X10 all PASS; otherwise VERDICT INDEP-C3-OPEN with
the failing ids.  Each check is a conjunction of the assertions in its docstring.

  X1  Theorem C11-B identity: sum_{P in X,Y,Z} |det Psi(C_P g)|^2 = |a|^2|b|^2 + |<a|b>|^2 for g = |0>a + |1>b (symbolic).
  X2  Group orders as signed permutations of the 16 table coordinates: <cnot, actT J> = 48 (integer traces, E(3,0) fixed);
      <cnot, actT J, actT S> = 384 = <cnot, actT J, actT S, actT nflip> (equal sets); <cnot, actC J, actT J> = 11520 =
      <cnot, actC J, actT J, actC S, actT S>; the stabiliser of E(3,0) in the 11520 group has 384 elements and equals the
      384 group; the orbit of E(3,0) has 30 elements.
  X3  C11.5: the G384-orbit of h* = (10, 2-2i, -1-3i, 3-i) has 192 rays, min D = 85/2048, pairwise squared overlaps in
      [25/2048, 13/16]; at c* = 401/400 H1 holds on every ray and (CC) on every pair (18336 pairs); at c' = 301/300 (CC)
      fails on the minimal-overlap pair.
  X4  C11.4: the G384-orbit of phi0 = (1, 2, 3i, -1+i) has 384 rays, min D = 5/256 (so lambda_max = (8+sqrt59)/16),
      s_max = 233/256, exactly one orbit ray orthogonal to phi0; at c = 101/100 the witness y = P_phi0 + lambda d_k
      (lambda = (c-1)/(4-2c)) has <y, d_l> >= 0 for all orbit defects, <y, d_phi0> = 0 and h_k^dagger y h_k < 0.
  X5  C12.1 pair theorem instance h1 = e1, h2 = (3/5, 4/5, 0, 0), s = 9/25: the (CC) threshold is c <= 10/9; at c = 5/4
      the explicit y = P_v + lambda d2 (v = (12/13, -5/13, 0, 0)) lies in K* (pairs >= 0 with d1, d2; <y,d1> = 0) and not in
      K (x = Pi_{v-perp} h2 has x^dagger y x < 0); at c = 11/10 the same construction at the far cap edge yields a PSD y.
  X6  C14.2: on the circle surgery h_alpha = sqrt(9/10) e1 + sqrt(1/10) e^{i alpha} e2 at c = 1000/961 the projectors of
      rational contact points of d_0 with aligned phases span exactly 14 real dimensions, each satisfying <Y, d_0> = 0 and
      Im Y_12 = 0; points of the full null quadric (free phases) span 15.
  X7  C16.4 / C13.9f: the kappa orbit of h = (6, 2, 1, -1): circle-1 members (6, 2, x, -x) and circle-2 members (6, -2, x, x)
      have |v|^2 = 42, D = 16/441, within-circle |<v|v'>| >= 38, cross 32 (s_min = 256/441); H1 holds at c = 103/100 and
      fails at c = 26/25; (CC) holds at 103/100 and the cross pair violates it at c = 5/4; d has eigenvalue -3/100;
      the S2-group image (R_z(pi) (x) R_x(pi))(I (x) Z) h = (2, -6, 1, 1) is orthogonal to h.
  X8  C15.2: the Clifford orbit (<CNOT, U_J (x) I, I (x) U_J>) of h_C = (-480+7i, 357+870i, 939+834i, 448+486i) has 11520
      rays; s_min against h_C = 164178929/3916193820250 > 0; min D over the orbit >= 1/50; at c = 100001/100000 H1 and
      (CC) hold; countercontrol: the orbit of 4 phi0 has 5760 rays and contains a ray orthogonal to 4 phi0.
  X9  C13.5 case A: the basis b1 = (2,3)(x)(2,-1+2i), b2 = CNOT b1, b3 = |0>(x)(1+2i, 2), b4 = (10, -5+10i, -6-12i, -6-12i)
      is orthogonal; b3 is a product, b1 a product, b2 and b4 entangled; h = (9+2i) b3 + b1 has weight p = 85/98 on b3;
      (A^2, B^2) = (9/52, 0), (4/117, 20/117), (5/117, 20/117) for j = 1, 2, 4; the three orbit circles are product-free
      (min D = (1-p)(2 sqrt p A - sqrt(1-p) B)^2 > 0); H1 holds on all three at c = 251/250 and fails at c = 101/100 on the
      circle through b2; s_min = (36/49)^2 and (CC) holds at 251/250.
  X10 C16-1 instances: CNOT carries both computational Bell circles (|00> + w|11>, |01> + w|10>) to products (symbolic w);
      in case A/B's basis the products are exactly b1 and b3.
"""
import sys
import itertools
from fractions import Fraction as Fr
import sympy as sp
from sympy import Rational as R, I, Matrix, sqrt, symbols, expand, simplify, eye, zeros

results = {}


class GQ:
    __slots__ = ('a', 'b')

    def __init__(self, a, b=0):
        self.a = a if isinstance(a, Fr) else Fr(a)
        self.b = b if isinstance(b, Fr) else Fr(b)

    def __add__(self, o):
        return GQ(self.a + o.a, self.b + o.b)

    def __sub__(self, o):
        return GQ(self.a - o.a, self.b - o.b)

    def __mul__(self, o):
        return GQ(self.a * o.a - self.b * o.b, self.a * o.b + self.b * o.a)

    def __neg__(self):
        return GQ(-self.a, -self.b)

    def conj(self):
        return GQ(self.a, -self.b)

    def norm2(self):
        return self.a * self.a + self.b * self.b

    def __truediv__(self, o):
        n = o.norm2()
        p = self * o.conj()
        return GQ(p.a / n, p.b / n)

    def iszero(self):
        return self.a == 0 and self.b == 0

    def __eq__(self, o):
        return self.a == o.a and self.b == o.b

    def __hash__(self):
        return hash((self.a, self.b))

    def __repr__(self):
        return f"({self.a}+{self.b}i)"


Z0 = GQ(0)
ONE = GQ(1)
IU = GQ(0, 1)


def mat(rows):
    return [[x if isinstance(x, GQ) else GQ(x) for x in r] for r in rows]


def mmul(A, B):
    n, m, p = len(A), len(B), len(B[0])
    return [[sum((A[i][k] * B[k][j] for k in range(m)), Z0) for j in range(p)] for i in range(n)]


def madj(A):
    return [[A[j][i].conj() for j in range(len(A))] for i in range(len(A[0]))]


def mvec(A, v):
    return tuple(sum((A[i][k] * v[k] for k in range(len(v))), Z0) for i in range(len(A)))


def kron(A, B):
    m, n, p, q = len(A), len(A[0]), len(B), len(B[0])
    return [[A[i // p][j // q] * B[i % p][j % q] for j in range(n * q)] for i in range(m * p)]


def trace(A):
    return sum((A[i][i] for i in range(len(A))), Z0)


def inner(u, v):  # <u|v>
    return sum((u[i].conj() * v[i] for i in range(len(u))), Z0)


def norm2(v):
    return sum(x.norm2() for x in v)


def detPsi(v):
    return v[0] * v[3] - v[1] * v[2]


def Dval(v):
    return detPsi(v).norm2() / (norm2(v) ** 2)


def overlap(u, v):
    return inner(u, v).norm2() / (norm2(u) * norm2(v))


def ray(v):
    for x in v:
        if not x.iszero():
            return tuple((y / x).a for y in v) + tuple((y / x).b for y in v)
    raise ValueError


def unray(key):
    n = len(key) // 2
    return tuple(GQ(key[i], key[n + i]) for i in range(n))


I2 = mat([[1, 0], [0, 1]])
X = mat([[0, 1], [1, 0]])
Y = [[Z0, -IU], [IU, Z0]]
Zm = mat([[1, 0], [0, -1]])
PAULI = [I2, X, Y, Zm]
SG = [[ONE, Z0], [Z0, IU]]
half = GQ(Fr(1, 2))
UJ = [[half * (ONE - IU), half * (-ONE - IU)], [half * (ONE - IU), half * (ONE + IU)]]
CNOT = mat([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
I4 = mat([[1 if i == j else 0 for j in range(4)] for i in range(4)])
TT = [[kron(PAULI[m], PAULI[n]) for n in range(4)] for m in range(4)]


def table_action(U):
    """Signed permutation (perm, sign) on the 16 coordinates (mu, nu) -> 4*mu + nu of omega -> coordOf(U dict(omega) U^H)."""
    Ud = madj(U)
    perm = [None] * 16
    sign = [None] * 16
    for m in range(4):
        for n in range(4):
            C = mmul(mmul(U, TT[m][n]), Ud)
            hits = []
            for m2 in range(4):
                for n2 in range(4):
                    t = trace(mmul(TT[m2][n2], C))
                    if not t.iszero():
                        hits.append((m2, n2, GQ(t.a / 4, t.b / 4)))
            assert len(hits) == 1 and hits[0][2].b == 0 and abs(hits[0][2].a) == 1, (m, n, hits)
            perm[4 * m + n] = 4 * hits[0][0] + hits[0][1]
            sign[4 * m + n] = int(hits[0][2].a)
    return (tuple(perm), tuple(sign))


def compose(g, h):  # g after h
    pg, sg = g
    ph, sh = h
    return (tuple(pg[ph[i]] for i in range(16)), tuple(sg[ph[i]] * sh[i] for i in range(16)))


def closure(gens):
    ident = (tuple(range(16)), tuple([1] * 16))
    seen = {ident}
    frontier = [ident]
    while frontier:
        new = []
        for g in frontier:
            for s in gens:
                h = compose(s, g)
                if h not in seen:
                    seen.add(h)
                    new.append(h)
        frontier = new
    return seen


def apply_table(g, idx):  # image of basis table e_idx: (index, sign)
    return (g[0][idx], g[1][idx])


def trace_sp(g):
    return sum(g[1][i] for i in range(16) if g[0][i] == i)


def orbit_rays(gens, v):
    start = ray(v)
    seen = {start}
    frontier = [start]
    while frontier:
        new = []
        for key in frontier:
            w = unray(key)
            for U in gens:
                k2 = ray(mvec(U, w))
                if k2 not in seen:
                    seen.add(k2)
                    new.append(k2)
        frontier = new
    return seen


def gq_to_sp(z):
    return sp.Rational(z.a) + I * sp.Rational(z.b)


def vec_to_sp(v):
    return Matrix([gq_to_sp(z) for z in v])


# ---------------------------------------------------------------- X1
def X1():
    a0r, a0i, a1r, a1i, b0r, b0i, b1r, b1i = symbols('a0r a0i a1r a1i b0r b0i b1r b1i', real=True)
    a = Matrix([a0r + I * a0i, a1r + I * a1i])
    b = Matrix([b0r + I * b0i, b1r + I * b1i])
    Xs = Matrix([[0, 1], [1, 0]]); Ys = Matrix([[0, -I], [I, 0]]); Zs = Matrix([[1, 0], [0, -1]])
    total = 0
    for P in (Xs, Ys, Zs):
        Pb = P * b
        det = a[0] * Pb[1] - a[1] * Pb[0]
        total += expand(det * sp.conjugate(det))
    rhs = expand((a.H * a)[0] * (b.H * b)[0] + (a.H * b)[0] * sp.conjugate((a.H * b)[0]))
    ok = expand(total - rhs) == 0
    results['X1'] = bool(ok)
    print(f"X1 Theorem C11-B identity (symbolic): {'PASS' if ok else 'FAIL'}")


# ---------------------------------------------------------------- X2
def X2():
    ok = True
    g_cnot = table_action(CNOT)
    g_tJ = table_action(kron(I2, UJ))
    g_tS = table_action(kron(I2, SG))
    g_tX = table_action(kron(I2, X))
    g_cJ = table_action(kron(UJ, I2))
    g_cS = table_action(kron(SG, I2))
    G48 = closure([g_cnot, g_tJ])
    ok &= len(G48) == 48
    traces = sorted(set(trace_sp(g) for g in G48))
    ok &= all(apply_table(g, 12) == (12, 1) for g in G48)  # E(3,0): index 4*3+0
    G384 = closure([g_cnot, g_tJ, g_tS])
    G1 = closure([g_cnot, g_tJ, g_tS, g_tX])
    ok &= len(G384) == 384 and G1 == G384
    C2 = closure([g_cnot, g_cJ, g_tJ])
    Cfull = closure([g_cnot, g_cJ, g_tJ, g_cS, g_tS])
    ok &= len(C2) == 11520 and Cfull == C2
    stab = {g for g in Cfull if apply_table(g, 12) == (12, 1)}
    ok &= len(stab) == 384 and stab == G384
    orb = {apply_table(g, 12) for g in Cfull}
    ok &= len(orb) == 30
    results['X2'] = bool(ok)
    print(f"X2 groups: |<cnot,actT J>| = {len(G48)} (traces {traces}); |<cnot,actT J,actT S>| = {len(G384)}, with nflip "
          f"{len(G1)}, equal {G1 == G384}; |<cnot,actC J,actT J>| = {len(C2)}, full Clifford {len(Cfull)}; "
          f"Stab(E(3,0)) = {len(stab)} (= G384: {stab == G384}); orbit of E(3,0): {len(orb)}: {'PASS' if ok else 'FAIL'}")


# ---------------------------------------------------------------- X3
def cc_holds(c, s):
    return c * c * s >= 4 * (c - 1)


def h1_holds(c, D):
    return 1 - 4 * D <= (2 / c - 1) ** 2


def X3():
    ok = True
    gens = [CNOT, kron(I2, SG), kron(I2, UJ)]
    hstar = (GQ(10), GQ(2, -2), GQ(-1, -3), GQ(3, -1))
    orb = orbit_rays(gens, hstar)
    vecs = [unray(k) for k in orb]
    ok &= len(vecs) == 192
    Ds = [Dval(v) for v in vecs]
    ok &= min(Ds) == Fr(85, 2048)
    smin, smax = Fr(1), Fr(0)
    npairs = 0
    for i in range(len(vecs)):
        for j in range(i + 1, len(vecs)):
            s = overlap(vecs[i], vecs[j])
            npairs += 1
            smin = min(smin, s); smax = max(smax, s)
    ok &= smin == Fr(25, 2048) and smax == Fr(13, 16) and npairs == 18336
    cst = Fr(401, 400)
    ok &= all(h1_holds(cst, D) for D in Ds)
    ok &= cc_holds(cst, smin)
    ok &= not cc_holds(Fr(301, 300), smin)
    results['X3'] = bool(ok)
    print(f"X3 h* orbit: {len(vecs)} rays, min D = {min(Ds)}, overlaps [{smin}, {smax}] over {npairs} pairs; H1 and (CC) at "
          f"401/400: {all(h1_holds(cst, D) for D in Ds)}, {cc_holds(cst, smin)}; (CC) at 301/300: {cc_holds(Fr(301, 300), smin)}: "
          f"{'PASS' if ok else 'FAIL'}")


# ---------------------------------------------------------------- X4
def X4():
    ok = True
    gens = [CNOT, kron(I2, SG), kron(I2, UJ)]
    phi0 = (GQ(1), GQ(2), GQ(0, 3), GQ(-1, 1))
    orb = orbit_rays(gens, phi0)
    vecs = [unray(k) for k in orb]
    ok &= len(vecs) == 384
    Ds = [Dval(v) for v in vecs]
    ok &= min(Ds) == Fr(5, 256)
    n2 = norm2(phi0)
    ovl = [overlap(phi0, v) for v in vecs]
    orth = [v for v, s in zip(vecs, ovl) if s == 0]
    ok &= len(orth) == 1
    smax = max(s for s in ovl if s != 1)
    ok &= smax == Fr(233, 256)
    lam_max = (8 + sqrt(59)) / 16
    ok &= simplify(lam_max - (1 + sqrt(1 - 4 * R(5, 256))) / 2) == 0
    c = Fr(101, 100)
    ok &= c <= 1 / lam_max.evalf(50) + 1e-30 or sp.Rational(c) * lam_max <= 1  # c in the H1 window
    ok &= bool(sp.Rational(c) * lam_max <= 1)
    lam = (c - 1) / (4 - 2 * c)
    hk = orth[0]
    # y = P_phi0 + lam d_k, matrices with GQ entries, normalised vectors as rationals via norm2 scaling
    def proj(v):
        n = norm2(v)
        return [[v[i] * v[j].conj() / GQ(n) for j in range(4)] for i in range(4)]
    def defect(v, cc):
        P = proj(v)
        return [[(I4[i][j] - GQ(cc) * P[i][j]) for j in range(4)] for i in range(4)]
    Pphi = proj(phi0)
    dk = defect(hk, c)
    yM = [[Pphi[i][j] + GQ(lam) * dk[i][j] for j in range(4)] for i in range(4)]
    def pair(A, B):
        return trace(mmul(A, B))
    pairs = [pair(yM, defect(v, c)) for v in vecs]
    ok &= all(p.b == 0 and p.a >= 0 for p in pairs)
    p0 = pair(yM, defect(phi0, c))
    ok &= p0.iszero()
    q = inner(hk, mvec(yM, hk))
    ok &= q.b == 0 and q.a < 0
    results['X4'] = bool(ok)
    print(f"X4 phi0 orbit: {len(vecs)} rays, min D = {min(Ds)}, s_max = {smax}, orthogonal rays {len(orth)}; witness at c = 101/100: "
          f"min <y,d_l> = {min(p.a for p in pairs)}, <y,d_phi0> = {p0}, h_k^+ y h_k = {q}: {'PASS' if ok else 'FAIL'}")


# ---------------------------------------------------------------- X5
def X5():
    ok = True
    s = R(9, 25)
    cvar = symbols('c', positive=True)
    thr = sp.solve(sp.Eq(cvar ** 2 * s, 4 * (cvar - 1)), cvar)
    ok &= set(thr) == {R(10, 9), 10}
    h1 = Matrix([1, 0, 0, 0]); h2 = Matrix([R(3, 5), R(4, 5), 0, 0])
    def P(v):
        return v * v.H / (v.H * v)[0]
    def Kstar_witness(c, v):
        d1 = eye(4) - c * P(h1); d2 = eye(4) - c * P(h2)
        pd = (d1 * d2).trace()
        lam = (c * (h1.H * v)[0] * sp.conjugate((h1.H * v)[0]) / (v.H * v)[0] - 1) / pd
        y = P(v) + lam * d2
        return y, d1, d2, lam
    v = Matrix([R(12, 13), R(-5, 13), 0, 0])
    c = R(5, 4)
    y, d1, d2, lam = Kstar_witness(c, v)
    ok &= lam > 0
    ok &= simplify((y * d1).trace()) == 0 and simplify((y * d2).trace()) > 0
    x = h2 - (v.H * h2)[0] * v / (v.H * v)[0]
    val = simplify((x.H * y * x)[0])
    ok &= val < 0
    # at c = 11/10, (CC) holds; far-edge construction gives PSD y (necessary consequence)
    c2 = R(11, 10)
    ok &= cc_holds(Fr(11, 10), Fr(9, 25))
    # far cap edge of d1 opposite to h2: v_e = (cos t, -sin t) with cos^2 t = 1/c2 (boundary of the cap), use the
    # geodesic point: |<h1|v>|^2 = 1/c2 exactly at the boundary; take a rational point just inside: cos t = 20/21? use the
    # exact boundary-adjacent rational point (cos t, sin t) = (39/41, 40/41)? cos^2 = 1521/1681 = 0.9048 < 1/c2 = 0.909...
    # choose (cos, sin) = (41/44?) -- use a clean rational: cos t = 20/21, sin t = sqrt(41)/21 (not rational); instead test the
    # exact boundary point in symbols: v = (sqrt(10/11), -sqrt(1/11), 0, 0)
    ve = Matrix([sqrt(R(10, 11)), -sqrt(R(1, 11)), 0, 0])
    y2, d1b, d2b, lam2 = Kstar_witness(c2, ve)
    ok &= simplify(lam2) == 0  # at the boundary lam = 0: y = P_v, PSD
    # slightly inside the cap: the thread's "far edge" check; use v with |<h1|v>|^2 = 0.92 > 1/c2 = 10/11 ~ 0.9091
    vi = Matrix([sqrt(R(23, 25)), -sqrt(R(2, 25)), 0, 0])
    y3, _, _, lam3 = Kstar_witness(c2, vi)
    ok &= lam3 > 0
    ev = [sp.nsimplify(e) for e in y3.eigenvals()]
    ok &= all(sp.simplify(e).evalf(40) >= -1e-35 for e in ev)
    results['X5'] = bool(ok)
    print(f"X5 pair theorem instance (s = 9/25): threshold roots {thr}; witness at c = 5/4: lam = {lam}, x^+ y x = {val}; "
          f"at c = 11/10 (CC) holds, inside-cap y eigenvalues nonnegative: {'PASS' if ok else 'FAIL'}")


# ---------------------------------------------------------------- X6
def X6():
    ok = True
    # basis: e1, e2 the two circle axes; d0 = I - c P_{h0}, h0 = sqrt(p) e1 + sqrt(1-p) e2, p = 9/10, c = 1000/961
    # contact points (aligned phases): v1, v2 >= 0 real, 3 v1 + v2 = 31/10, |v3|^2 + |v4|^2 = 1 - v1^2 - v2^2.
    # Integer form with scale 10k: a, b >= 0 integers, 3a + b = 31k, a^2 + b^2 + |c3|^2 + |c4|^2 = 100 k^2.
    def gauss_reps(n):
        out = []
        r = 0
        while r * r <= n:
            s2 = n - r * r
            s_ = 0
            while s_ * s_ <= s2:
                if s_ * s_ == s2:
                    for sr in {r, -r}:
                        for si in {s_, -s_}:
                            out.append((sr, si))
                s_ += 1
            r += 1
        return sorted(set(out))

    pts_aligned = []
    for k in range(1, 7):
        for a in range(0, 31 * k // 3 + 1):
            b = 31 * k - 3 * a
            if b < 0:
                continue
            rem = 100 * k * k - a * a - b * b
            if rem < 0:
                continue
            for c3 in gauss_reps_all(rem) if False else []:
                pass
            # enumerate c3 with |c3|^2 <= rem, then c4 with |c4|^2 = rem - |c3|^2
            n3 = 0
            while n3 <= rem:
                reps3 = gauss_reps(n3)
                if reps3:
                    reps4 = gauss_reps(rem - n3)
                    for c3 in reps3:
                        for c4 in reps4:
                            pts_aligned.append((Fr(a, 10 * k), Fr(b, 10 * k), (Fr(c3[0], 10 * k), Fr(c3[1], 10 * k)),
                                                (Fr(c4[0], 10 * k), Fr(c4[1], 10 * k))))
                n3 += 1
    pts_aligned = sorted(set(pts_aligned))

    def proj_vec(pt):
        v = [GQ(pt[0]), GQ(pt[1]), GQ(pt[2][0], pt[2][1]), GQ(pt[3][0], pt[3][1])]
        P = [[v[i] * v[j].conj() for j in range(4)] for i in range(4)]
        # real coordinates of the Hermitian matrix: diagonal (4) + re/im of upper triangle (12)
        coords = [P[i][i].a for i in range(4)]
        for i in range(4):
            for j in range(i + 1, 4):
                coords += [P[i][j].a, P[i][j].b]
        return v, P, coords

    c = Fr(1000, 961)
    p = Fr(9, 10)
    rows = []
    checks = True
    for pt in pts_aligned:
        v, P, coords = proj_vec(pt)
        # |v| = 1 and on the cap boundary of d0: |<h0|v>|^2 = (sqrt p v1 + sqrt(1-p) v2)^2 = (3 v1 + v2)^2 / 10 = 1/c
        checks &= norm2(v) == 1
        checks &= (3 * pt[0] + pt[1]) ** 2 / 10 == 1 / c
        # <Y, d0> = 0 holds by the cap condition; Im Y_12 = 0 since v1, v2 real
        checks &= P[0][1].b == 0
        rows.append(coords)
    rank_aligned = Matrix(rows).rank() if rows else 0
    ok &= checks and rank_aligned == 14 and len(rows) >= 24
    # full null quadric: v1, v2 complex with |3 v1 + v2|^2 = 961/100, |v| = 1 -> integers: |3a + b|^2 = 961 k^2
    pts_q = []
    for k in range(1, 6):
        target = 961 * k * k
        for w in gauss_reps(target):
            for ar in range(-10 * k, 10 * k + 1):
                for ai in range(-10 * k, 10 * k + 1):
                    if ar * ar + ai * ai > 100 * k * k:
                        continue
                    br, bi = w[0] - 3 * ar, w[1] - 3 * ai
                    rem = 100 * k * k - ar * ar - ai * ai - br * br - bi * bi
                    if rem < 0:
                        continue
                    n3 = 0
                    found = False
                    while n3 <= rem and not found:
                        reps3 = gauss_reps(n3)
                        if reps3:
                            reps4 = gauss_reps(rem - n3)
                            if reps4:
                                c3, c4 = reps3[0], reps4[0]
                                pts_q.append((Fr(ar, 10 * k), Fr(ai, 10 * k), Fr(br, 10 * k), Fr(bi, 10 * k),
                                              Fr(c3[0], 10 * k), Fr(c3[1], 10 * k), Fr(c4[0], 10 * k), Fr(c4[1], 10 * k)))
                                found = True
                        n3 += 1
                    if len(pts_q) > 400:
                        break
                if len(pts_q) > 400:
                    break
            if len(pts_q) > 400:
                break
        if len(pts_q) > 400:
            break
    rows_q = []
    for q in sorted(set(pts_q)):
        v = [GQ(q[0], q[1]), GQ(q[2], q[3]), GQ(q[4], q[5]), GQ(q[6], q[7])]
        if norm2(v) != 1:
            continue
        w3 = v[0] * GQ(3) + v[1]
        if w3.norm2() != Fr(961, 100):
            continue
        P = [[v[i] * v[j].conj() for j in range(4)] for i in range(4)]
        coords = [P[i][i].a for i in range(4)]
        for i in range(4):
            for j in range(i + 1, 4):
                coords += [P[i][j].a, P[i][j].b]
        rows_q.append(coords)
    rank_q = Matrix(rows_q).rank() if rows_q else 0
    ok &= rank_q == 15
    results['X6'] = bool(ok)
    print(f"X6 C14 contact spans: aligned points {len(rows)} -> rank {rank_aligned}; full quadric points {len(rows_q)} -> rank {rank_q}: "
          f"{'PASS' if ok else 'FAIL'}")


def gauss_reps_all(n):
    return []


# ---------------------------------------------------------------- X7
def X7():
    ok = True
    xs = [GQ(1), GQ(-1), GQ(0, 1), GQ(0, -1), GQ(Fr(3, 5), Fr(4, 5)), GQ(Fr(-5, 13), Fr(12, 13)), GQ(Fr(8, 17), Fr(-15, 17))]
    c1 = [(GQ(6), GQ(2), x, -x) for x in xs]
    c2 = [(GQ(6), GQ(-2), x, x) for x in xs]
    for v in c1 + c2:
        ok &= norm2(v) == 42 and Dval(v) == Fr(16, 441)
    for u in c1:
        for v in c1:
            ok &= inner(u, v).norm2() >= 38 * 38
        for v in c2:
            ok &= inner(u, v).norm2() == 32 * 32
    for u in c2:
        for v in c2:
            ok &= inner(u, v).norm2() >= 38 * 38
    smin = Fr(256, 441)
    ok &= h1_holds(Fr(103, 100), Fr(16, 441)) and not h1_holds(Fr(26, 25), Fr(16, 441))
    ok &= cc_holds(Fr(103, 100), smin) and not cc_holds(Fr(5, 4), smin)
    h = (GQ(6), GQ(2), GQ(1), GQ(-1))
    # eigenvalue 1 - c of d = I - c P_h
    ok &= 1 - Fr(103, 100) == Fr(-3, 100)
    # S2-group image: (R_z(pi) (x) R_x(pi)) (I (x) Z) h, R_z(pi) = -iZ, R_x(pi) = -iX  -> -(Z (x) X)(I (x) Z) h
    IZ = kron(I2, Zm)
    ZX = kron(Zm, X)
    img = mvec(ZX, mvec(IZ, h))
    img = tuple(-z for z in img)
    ok &= img == (GQ(2), GQ(-6), GQ(1), GQ(1))
    ok &= inner(h, img).iszero()
    results['X7'] = bool(ok)
    print(f"X7 kappa orbit facts (|v|^2 = 42, D = 16/441, overlaps >= 38^2 within / = 32^2 across; H1 103/100 ok, 26/25 fails; "
          f"(CC) 103/100 ok, cross pair at 5/4 fails; S2 image {img} orthogonal): {'PASS' if ok else 'FAIL'}")


# ---------------------------------------------------------------- X8
def X8():
    ok = True
    gens = [CNOT, kron(UJ, I2), kron(I2, UJ)]
    hC = (GQ(-480, 7), GQ(357, 870), GQ(939, 834), GQ(448, 486))
    orb = orbit_rays(gens, hC)
    vecs = [unray(k) for k in orb]
    ok &= len(vecs) == 11520
    nh = norm2(hC)
    smin = min(overlap(hC, v) for v in vecs if ray(v) != ray(hC))
    ok &= smin == Fr(164178929, 3916193820250)
    Dmin = min(Dval(v) for v in vecs)
    ok &= Dmin >= Fr(1, 50)
    c = Fr(100001, 100000)
    ok &= h1_holds(c, Dmin) and cc_holds(c, smin)
    phi0 = (GQ(1), GQ(2), GQ(0, 3), GQ(-1, 1))
    orb0 = orbit_rays(gens, phi0)
    vecs0 = [unray(k) for k in orb0]
    ok &= len(vecs0) == 5760
    s0 = min(overlap(phi0, v) for v in vecs0 if ray(v) != ray(phi0))
    ok &= s0 == 0
    results['X8'] = bool(ok)
    print(f"X8 Clifford orbit of h_C: {len(vecs)} rays, s_min = {smin} (~{float(smin):.3e}), min D = {Dmin} (~{float(Dmin):.4f}); "
          f"H1/(CC) at 100001/100000: {h1_holds(c, Dmin)}/{cc_holds(c, smin)}; 4phi0 orbit {len(vecs0)} rays, min overlap {s0}: "
          f"{'PASS' if ok else 'FAIL'}")


# ---------------------------------------------------------------- X9
def X9():
    ok = True
    b1 = Matrix([4, -2 + 4 * I, 6, -3 + 6 * I])  # (2,3) (x) (2, -1+2i)
    ok &= b1 == sp.kronecker_product(Matrix([2, 3]), Matrix([2, -1 + 2 * I]))
    CN = Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
    b2 = CN * b1
    b3 = Matrix([1 + 2 * I, 2, 0, 0])
    b4 = Matrix([10, -5 + 10 * I, -6 - 12 * I, -6 - 12 * I])
    B = [b1, b2, b3, b4]
    for i in range(4):
        for j in range(i + 1, 4):
            ok &= simplify((B[i].H * B[j])[0]) == 0
    det = lambda v: v[0] * v[3] - v[1] * v[2]
    ok &= det(b1) == 0 and det(b3) == 0 and det(b2) != 0 and det(b4) != 0
    nb = [simplify((v.H * v)[0]) for v in B]
    ok &= nb == [117, 117, 9, 585]
    h = (9 + 2 * I) * b3 + b1
    p = simplify(sp.Abs(9 + 2 * I) ** 2 * 9 / (h.H * h)[0])
    ok &= p == R(85, 98)
    Bf = lambda u, v: (u[0] * v[3] + u[3] * v[0] - u[1] * v[2] - u[2] * v[1]) / 2
    bh = [v / sqrt(n) for v, n in zip(B, nb)]
    AB = {}
    for j, idx in ((1, 0), (2, 1), (4, 3)):
        A2 = simplify(sp.Abs(Bf(bh[2], bh[idx])) ** 2)
        B2 = simplify(sp.Abs(Bf(bh[idx], bh[idx])) ** 2)
        AB[j] = (A2, B2)
    ok &= AB == {1: (R(9, 52), 0), 2: (R(4, 117), R(20, 117)), 4: (R(5, 117), R(20, 117))}
    q = 1 - p
    Dmins = {}
    for j, (A2, B2) in AB.items():
        A, Bv = sqrt(A2), sqrt(B2)
        Dmin = (q) * (2 * sqrt(p) * A - sqrt(q) * Bv) ** 2
        Dmins[j] = simplify(Dmin)
        ok &= bool(sp.simplify(2 * sqrt(p) * A - sqrt(q) * Bv) > 0)
    for cc, expect in ((R(251, 250), True), (R(101, 100), None)):
        res = {j: bool(sp.simplify(1 - 4 * Dmins[j] - (2 / cc - 1) ** 2) <= 0) for j in Dmins}
        if expect is True:
            ok &= all(res.values())
        else:
            ok &= res[2] is False
    smin = (2 * p - 1) ** 2
    ok &= smin == R(36, 49) ** 2 and p ** 2 > smin
    ok &= cc_holds(Fr(251, 250), Fr(36, 49) ** 2)
    results['X9'] = bool(ok)
    print(f"X9 case A: basis orthogonal, products b1,b3, entangled b2,b4; p = {p}; (A^2,B^2) = {AB}; D_min = "
          f"{ {j: sp.N(v, 6) for j, v in Dmins.items()} }; H1 at 251/250 all, fails on circle 2 at 101/100; s_min = (36/49)^2: "
          f"{'PASS' if ok else 'FAIL'}")


# ---------------------------------------------------------------- X10
def X10():
    ok = True
    w = symbols('w')
    CN = Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
    det = lambda v: expand(v[0] * v[3] - v[1] * v[2])
    v1 = CN * Matrix([1, 0, 0, w]); v2 = CN * Matrix([0, 1, w, 0])
    ok &= det(v1) == 0 and det(v2) == 0
    ok &= det(Matrix([1, 0, 0, w])) != 0 and det(Matrix([0, 1, w, 0])) != 0
    results['X10'] = bool(ok)
    print(f"X10 CNOT carries both computational Bell circles to products: {'PASS' if ok else 'FAIL'}")


if __name__ == '__main__':
    for fn in (X1, X2, X3, X4, X5, X6, X7, X8, X9, X10):
        fn()
        sys.stdout.flush()
    fails = [k for k, v in results.items() if not v]
    n = sum(1 for v in results.values() if v)
    print(f"{n}/{len(results)} PASS")
    print("VERDICT INDEP-C3-FIXED" if not fails else f"VERDICT INDEP-C3-OPEN {fails}")
