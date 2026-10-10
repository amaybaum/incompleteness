"""EQ4-SIX probe s5 -- the sector Xi (S_3 and zero-sum phases): exact facts for c = 0 and c = 1.  Research only.

Usage:  python3 -I -B s5_xi_sector.py <base>/verification/lean-mathlib/OIBridge
Imports the copied library eq4_lib.py (sha256 cc2c6aca94007ac8) and sympy (symbolic identities only).

Xi = {X = sum_w d_w Pi_w + c|000><111| + conj(c)|111><000|}  (Pi_w: projector on computational strings of weight w);
Xi is the fixed space of S_3 (token permutations) and of the phases diag(1, e^{i t1}) (x) ... with t1 + t2 + t3 = 0;
Tw_Xi is the average over these symmetries (finite average: S_3 x the phases with t_j in (2 pi / 4) Z summing to 0
mod 2 pi suffices on Herm(8): the weights w and the 000-111 coherence are the only invariants).  For an admissible
K3, K3 cap Xi = Tw_Xi(K3) is self-dual in Xi (c = 0: for B(X, Y) = tr(X T Y); c = 1: Euclidean); with phase invariance
the modulus form is  d0 d0' + 3 d1 d1' + 3 d2 d2' + d3 d3' - 2 |c||c'|.  Notation u0 = sqrt(d0 d3), u1 = sqrt(d1 d2).

Written claims (NOTES N2.6).
 (i)   BS* cap Xi = {d >= 0, |c| <= u0 + u1}  (AM-GM on biproducts a (x) chi; equality cases explicit).
 (ii)  Tw_Xi(BS) = (BS* cap Xi)^* = {d >= 0, |c| <= min(u0, 3 u1)}  (inf_u (u0 v0 + 3 u1 v1)/(u0 + u1) = min(v0, 3 v1)).
 (iii) K_A forces, on the locus rho = d0 d2^3/(d3 d1^3) = 1 (the diagonal-filter orbit of GD cap Xi), the profile
       phi_A = min(u0 + u1, 3 u1, u0/2 + 3 u1/2); phi_A is self-dual for the form u0 v0 + 3 u1 v1.
 (iv)  c = 1: B_tw* cap Xi = {d >= 0, |c| <= 2 u1}, Tw_Xi(B_tw) = {|c| <= (3/2) u1}; K_tw forces
       phi_tw = min(2 u1, u0/2 + 3 u1/2) on rho = 1, self-dual.
 (v)   Diagonal filters diag(1, t_j) map (d, |c|) to (d_w e_w(mu)/C(3,w), |c| sqrt(mu1 mu2 mu3)) after the S_3 twirl,
       mu_j = |t_j|^2; since e1 e2 >= 9 e3 (Maclaurin), u1 grows at least like sqrt(mu1 mu2 mu3) while u0 scales
       exactly so: every profile nondecreasing in u1 and 1-homogeneous in (u0, u1) gives a diagonal-filter-invariant cone.

DECISION RULE (fixed before the first run; rules, not expected numbers).  VERDICT `S5-XI-SECTOR-EXACT` iff all:
  K  transcription control.
  T  the finite twirl reproduces the Xi projection on all 64 matrix units (exact, eq4_lib).
  A  (i): on 4 exact instances (d with rational u0, u1) and |c| = u0 + u1 the explicit biproduct vector built from the
     AM-GM equality conditions gives value 0, and with |c| = u0 + u1 + 1/10 it gives a negative value (countercontrol);
     symbolic identity: the biproduct value minus the AM-GM lower bound is a sum of squares plus dropped nonnegative
     terms (sympy).
  B  (ii): the 2D dual formula at the two vertices; the twirls of a product state |psi>^(x)3 and of Phi+ (x) |+><+|
     (exact) lie on the boundary |c| = min(u0, 3 u1).
  C  (iii): the 92 K_A inequalities restricted to x = (d0 + c, d0 - c, d1, ..., d1) reduce to exactly the three
     bounds of phi_A (exact linear-form bookkeeping); phi_A's dual by vertex enumeration equals phi_A.
  D  (iv): the same for K_tw (36 generators, which are their own inequalities); B_tw* bound: on 4 exact instances the
     PT_3 biproduct equality case gives value 0 at |c| = 2 u1 and a negative value at 2 u1 + 1/10; the twin-hull
     element PT_2(Psi+) (x) |+><+| twirls to the boundary |c| = (3/2) u1; phi_tw self-dual.
  E  (v): sympy identity e1 e2 - 9 e3 = sum_cyc mu_k (mu_i - mu_j)^2.
"""
import itertools
import random
import sys
from fractions import Fraction as Fr

sys.path.insert(0, __file__.rsplit("/", 1)[0] if "/" in __file__ else ".")
import sympy as sp  # noqa: E402

import eq4_lib as L  # noqa: E402

BASE = sys.argv[1]
rep = L.Report("s5_xi_sector")
rng = random.Random(2026100955)
rep.check("K0 transcription control", L.transcription_control(BASE)[0])
X3 = (0, 1, 2)
WT = [bin(a).count("1") for a in range(8)]


def xi_coords(X):
    d = [Fr(0)] * 4
    for a in range(8):
        d[WT[a]] += X.get(a, a).re
    d = [d[w] / [1, 3, 3, 1][w] for w in range(4)]
    return d, X.get(0, 7)


def xi_op(d, c):
    out = {}
    for a in range(8):
        if d[WT[a]] != 0:
            out[(a, a)] = L.G(d[WT[a]])
    c = L.G.of(c)
    if not c.is_zero():
        out[(0, 7)] = c
        out[(7, 0)] = c.conj()
    return L.Op(X3, out)


# ------------------------------------------------------------------------------------------------ T finite twirl
PERMS = list(itertools.permutations(range(3)))
PHASES = []
for t1 in range(4):
    for t2 in range(4):
        t3 = (-t1 - t2) % 4
        PHASES.append((t1, t2, t3))
IPOW = [L.G(1), L.G(0, 1), L.G(-1), L.G(0, -1)]


def twirl(X):
    acc = L.Op(X3, {})
    for perm in PERMS:
        Y = L.reorder(L.relabel(X, {0: perm[0] + 10, 1: perm[1] + 10, 2: perm[2] + 10}), (10, 11, 12))
        Y = L.relabel(Y, {10: 0, 11: 1, 12: 2})
        for ph in PHASES:
            U = L.tensor(*[L.Op((q,), {(0, 0): L.ONE, (1, 1): IPOW[ph[q]]}) for q in range(3)])
            acc = acc + L.ad(U, Y)
    return acc.scale(Fr(1, len(PERMS) * len(PHASES)))


ok_t = True
for (r, c), u in L.units(X3):
    tw = twirl(u)
    d, cc = xi_coords(u)
    ok_t &= tw == xi_op(d, cc)
rep.check("T the finite twirl over S_3 x {zero-sum phases in (2 pi/4)Z} equals the Xi projection on all 64 units", ok_t)


# ------------------------------------------------------------------------------------------------ A BS* cap Xi
def biproduct_value(d, c, a, chi):
    """<a chi| X |a chi> with a on token 0, chi on tokens (1, 2)."""
    vec = [L.ZERO] * 8
    for i in range(2):
        for j in range(4):
            vec[4 * i + j] = L.G.of(a[i]) * L.G.of(chi[j])
    X = xi_op(d, c)
    return L.pair(X, L.ket_op(vec, X3))


ok_a = True
for _ in range(4):
    s0, s3, s1, s2 = [Fr(rng.randint(1, 4)) ** 2 for _ in range(4)]
    # rational square roots: d entries are squares of integers
    r0, r3, r1, r2 = [Fr(int(sp.sqrt(v))) for v in (s0, s3, s1, s2)]
    u1 = r1 * r2
    # equality case: x^2 d0 = y^2 d3 and z^2 d2 = w^2 d1 with x y = z w, x = a0 chi00, y = a1 chi11, z = a0 chi11,
    # w = a1 chi00 and phases making 2 Re(c conj(a0 chi00) a1 chi11) = -2 c x y.  Take a0 = 1, chi00 = 1:
    # y = x r0 / r3 = r0 / r3 (x = 1), z = chi11 = ?, w = a1 with z w = x y.  Choose a1 = w, chi11 = z with
    # z^2 d2 = w^2 d1 -> z r2 = w r1, and z w = y: z = sqrt(y r1 / r2), w = sqrt(y r2 / r1).  Avoid square roots by
    # scaling: pick y = r1 r2 m^2 ... simpler: parametrize directly with a1 = w, chi11 = z rational:
    #   need z r2 = w r1 and z w = r0 / r3 * (a0 chi00 = 1).  Set w = r2 * k, z = r1 * k, then k^2 r1 r2 = r0 / r3,
    #   i.e. k^2 = r0 / (r1 r2 r3): rescale d0 to make this a square.
    k = Fr(rng.randint(1, 3), rng.randint(1, 3))
    r0 = k * k * r1 * r2 * r3
    d = [r0 * r0, s1, s2, s3]
    u0 = r0 * r3
    c = u0 + u1
    a = [Fr(1), -r2 * k]          # a0 = 1, a1 = -w (the sign makes the coherence term negative)
    chi = [Fr(1), Fr(0), Fr(0), r1 * k]
    v0 = biproduct_value(d, c, a, chi)
    v1 = biproduct_value(d, c + Fr(1, 10), a, chi)
    ok_a &= v0 == 0 and v1.re < 0 and v1.im == 0
# symbolic: value - lower bound = (x sqrt d0 - y sqrt d3)^2 + (z sqrt d2 - w sqrt d1)^2 + 2 x y (u0 + u1 - c)
x, y, z, w, D0, D3, D1, D2, cc = sp.symbols("x y z w D0 D3 D1 D2 c", positive=True)
expr = (x ** 2 * D0 ** 2 + y ** 2 * D3 ** 2 + z ** 2 * D2 ** 2 + w ** 2 * D1 ** 2 - 2 * cc * x * y
        - ((x * D0 - y * D3) ** 2 + (z * D2 - w * D1) ** 2 + 2 * x * y * (D0 * D3 + D1 * D2 - cc)))
expr = sp.expand(expr.subs(w, x * y / z) * z ** 2)
rep.check("A BS* cap Xi = {|c| <= u0 + u1}: explicit biproducts give 0 at |c| = u0 + u1 and < 0 at u0 + u1 + 1/10 (4 exact "
          "instances); symbolic: value - [two squares + 2xy(u0 + u1 - |c|)] = 0 under xy = zw (d = squares D^2)",
          ok_a and sp.simplify(expr) == 0)


# ------------------------------------------------------------------------------------------------ B Tw(BS)
def u_of(d):
    return d[0] * d[3], d[1] * d[2]   # squared u0, u1


ok_b = True
# 2D dual at vertices: inf over u in R^2_+ of (u0 v0 + 3 u1 v1)/(u0 + u1) is attained at u = (1,0) or (0,1)
for v0, v1 in [(Fr(1), Fr(1)), (Fr(2), Fr(1, 3)), (Fr(1, 5), Fr(3))]:
    vals = [(t * v0 + 3 * (1 - t) * v1) for t in [Fr(i, 20) for i in range(21)]]
    ok_b &= min(vals) == min(v0, 3 * v1)
psi = L.ket_op([2, 1], (0,))
prod3 = L.tensor(psi, L.relabel(psi, {0: 1}), L.relabel(psi, {0: 2}))
dP, cP = xi_coords(twirl(prod3))
u0sq, u1sq = u_of(dP)
ok_b &= cP.abs2() == u0sq and cP.abs2() <= 9 * u1sq        # |c| = u0 <= 3 u1
plus = L.ket_op([1, 1], (2,)).scale(Fr(1, 2))
bstate = L.tensor(L.phi_plus(0, 1), plus)
dB, cB = xi_coords(twirl(bstate))
u0sq, u1sq = u_of(dB)
ok_b &= cB.abs2() == u0sq and cB.abs2() == 9 * u1sq          # |c| = u0 = 3 u1
rep.check("B Tw(BS) = {|c| <= min(u0, 3 u1)}: dual formula exact at the vertices; twirled product |psi>^3 has |c| = u0 <= "
          "3 u1 and twirled Phi+ (x) |+><+| has |c| = u0 = 3 u1 (both on the boundary)", ok_b)


# ------------------------------------------------------------------------------------------------ C K_A on Xi cap GD
def KA_gens():
    G = []
    for j, k in itertools.combinations(range(8), 2):
        G.append([1 if i in (j, k) else 0 for i in range(8)])
    for j in range(8):
        G.append([1 - 2 * (i == j) for i in range(8)])
    for j in range(8):
        for p in range(8):
            if p != j:
                G.append([1 - 2 * (i == j) + 2 * (i == p) for i in range(8)])
    return G


d0s, d1s, cs = sp.symbols("d0 d1 c", real=True)
xvec = [d0s + cs, d0s - cs] + [d1s] * 6
forms = set()
for g in KA_gens():
    f = sp.expand(sum(gi * xi for gi, xi in zip(g, xvec)))
    forms.add(f)
# each form is a*d0 + b*d1 + e*c >= 0; with |c| free in sign, bound |c| <= (a d0 + b d1)/|e| for e != 0
bounds = set()
nonneg = set()
for f in forms:
    a_ = f.coeff(d0s)
    b_ = f.coeff(d1s)
    e_ = f.coeff(cs)
    if e_ == 0:
        nonneg.add((a_, b_))
    else:
        bounds.add((sp.Rational(a_, abs(e_)), sp.Rational(b_, abs(e_))))
# minimal bounds (u0 = d0, u1 = d1 on GD cap Xi): remove dominated (a, b) pairs
minimal = {bd for bd in bounds if not any((o[0] <= bd[0] and o[1] <= bd[1] and o != bd) for o in bounds)}
expect = {(sp.Integer(1), sp.Integer(1)), (sp.Integer(0), sp.Integer(3)), (sp.Rational(1, 2), sp.Rational(3, 2))}


def dual2(breaks):
    """phi(u) = min over (a, b) of a u0 + b u1; dual phi°(v) = inf_u (u0 v0 + 3 u1 v1)/phi(u) over the breakpoints of
    phi (vertices of the piecewise-linear 1-homogeneous function on the simplex u0 + u1 = 1) and the endpoints."""
    ts = {Fr(0), Fr(1)}
    bl = list(breaks)
    for (a1, b1), (a2, b2) in itertools.combinations(bl, 2):
        # a1 t + b1 (1 - t) = a2 t + b2 (1 - t)
        den = (a1 - b1) - (a2 - b2)
        if den != 0:
            t = Fr(b2 - b1) / den
            if 0 <= t <= 1:
                ts.add(t)
    return sorted(ts)


def check_selfdual(breaks, samples):
    ok = True
    ts = dual2(breaks)
    for v0, v1 in samples:
        best = None
        for t in ts:
            ph = min(a * t + b * (1 - t) for a, b in breaks)
            if ph > 0:
                val = (t * v0 + 3 * (1 - t) * v1) / ph
                best = val if best is None else min(best, val)
        ok &= best == min(a * v0 + b * v1 for a, b in breaks)
    return ok


bA = [(Fr(1), Fr(1)), (Fr(0), Fr(3)), (Fr(1, 2), Fr(3, 2))]
samp = [(Fr(i), Fr(j)) for i in range(0, 6) for j in range(0, 6) if i + j > 0]
rep.check("C K_A restricted to GD cap Xi: the c-dependent inequalities reduce to |c| <= min(u0 + u1, 3 u1, u0/2 + 3u1/2) "
          "(minimal set %s; c-free forms %d); phi_A equals its dual on 35 exact sample points"
          % (sorted((str(a), str(b)) for a, b in minimal), len(nonneg)),
          minimal == expect and all(a >= 0 and b >= 0 for a, b in nonneg) and check_selfdual(bA, samp))


# ------------------------------------------------------------------------------------------------ D c = 1
def ptb_value(d, c, a, chi):
    vec = [L.ZERO] * 8
    for i in range(2):
        for j in range(4):
            vec[4 * i + j] = L.G.of(a[i]) * L.G.of(chi[j])
    X = L.ptranspose(xi_op(d, c), [2])
    return L.pair(X, L.ket_op(vec, X3))


ok_d = True
for _ in range(4):
    r1, r2 = Fr(rng.randint(1, 4)), Fr(rng.randint(1, 4))
    k = Fr(rng.randint(1, 3), rng.randint(1, 3))
    d = [Fr(rng.randint(0, 3)), r1 * r1, r2 * r2, Fr(rng.randint(0, 3))]
    u1 = r1 * r2
    c = 2 * u1
    # PT_3 X = diag + c |001><110| + h.c.; biproduct a (x) chi across 1|23: coherence between |0,01> and |1,10>.
    # equality: p d001 + q d110 + s d010 + t d101 = 2 c sqrt(pq) with p = |a0 chi01|^2, q = |a1 chi10|^2,
    # s = |a0 chi10|^2, t = |a1 chi01|^2: take a0 = 1, chi01 = 1, a1 = -r1/r2... (d001 = d1, d110 = d2, d010 = d1,
    # d101 = d2): choose |a1 chi10| = r1/r2 (so p d1 = q d2) and |a0 chi10| = |a1 chi01| (s = t) with s t = p q:
    # a1 = -r1/r2, chi10 = 1.
    a = [Fr(1), -r1 / r2]
    chi = [Fr(0), Fr(1), Fr(1), Fr(0)]
    v0 = ptb_value(d, c, a, chi)
    v1 = ptb_value(d, c + Fr(1, 10), a, chi)
    ok_d &= v0 == 0 and v1.re < 0
psi_plus = L.ket_op([0, 1, 1, 0], (0, 1)).scale(Fr(1, 2))
tw_el = L.tensor(L.ptranspose(psi_plus, [1]), plus)
dT, cT = xi_coords(twirl(tw_el))
ok_d &= 4 * cT.abs2() == 9 * dT[1] * dT[2] and dT[0] * dT[3] == 0
# K_tw restricted to GD cap Xi
p0 = (1, 1, 0, 0, 0, 0, 0, 0)
t0 = (1, 1, 1, 1, 1, -1, 1, -1)
k0 = (-1, 3, 1, 1, 1, 1, 1, 1)
gens7 = [(1, 0, 3, 2, 5, 4, 7, 6), (6, 7, 4, 5, 2, 3, 0, 1), (4, 5, 6, 7, 0, 1, 2, 3), (2, 3, 0, 1, 6, 7, 4, 5),
         (1, 0, 3, 2, 4, 5, 6, 7), (0, 1, 2, 3, 6, 7, 4, 5), (0, 1, 4, 5, 2, 3, 6, 7)]
group = {tuple(range(8))}
frontier = [tuple(range(8))]
while frontier:
    nf = []
    for g in frontier:
        for h in gens7:
            cc_ = tuple(g[h[i]] for i in range(8))
            if cc_ not in group:
                group.add(cc_)
                nf.append(cc_)
    frontier = nf
KT = sorted({tuple(v[g[i]] for i in range(8)) for v in (p0, t0, k0) for g in group})
bounds_t = set()
for g in KT:
    f = sp.expand(sum(gi * xi for gi, xi in zip(g, xvec)))
    e_ = f.coeff(cs)
    if e_ != 0:
        bounds_t.add((sp.Rational(f.coeff(d0s), abs(e_)), sp.Rational(f.coeff(d1s), abs(e_))))
min_t = {bd for bd in bounds_t if not any((o[0] <= bd[0] and o[1] <= bd[1] and o != bd) for o in bounds_t)}
expect_t = {(sp.Integer(0), sp.Integer(2)), (sp.Rational(1, 2), sp.Rational(3, 2))}
bT = [(Fr(0), Fr(2)), (Fr(1, 2), Fr(3, 2))]
rep.check("D c = 1: B_tw* cap Xi bound |c| <= 2 u1 attained by explicit PT_3 biproducts (4 exact instances, countercontrol "
          "+1/10 negative); PT_2(Psi+) (x) |+><+| twirls to |c| = (3/2) u1 with u0 = 0; K_tw (%d generators) restricted to "
          "GD cap Xi gives |c| <= min(2 u1, u0/2 + 3 u1/2) (minimal set %s), self-dual on 35 exact sample points"
          % (len(KT), sorted((str(a), str(b)) for a, b in min_t)),
          ok_d and len(KT) == 36 and min_t == expect_t and check_selfdual(bT, samp))

# ------------------------------------------------------------------------------------------------ E Maclaurin
m1, m2, m3 = sp.symbols("m1 m2 m3", positive=True)
e1 = m1 + m2 + m3
e2 = m1 * m2 + m1 * m3 + m2 * m3
e3 = m1 * m2 * m3
ident = sp.expand(e1 * e2 - 9 * e3 - (m1 * (m2 - m3) ** 2 + m2 * (m1 - m3) ** 2 + m3 * (m1 - m2) ** 2))
rep.check("E Maclaurin: e1 e2 - 9 e3 = sum_cyc mu_k (mu_i - mu_j)^2 (symbolic); so (e1/3)(e2/3) >= e3 and the twirled "
          "diagonal filters raise u1 at least by sqrt(mu1 mu2 mu3)", ident == 0)
rep.verdict("S5-XI-SECTOR-EXACT")
