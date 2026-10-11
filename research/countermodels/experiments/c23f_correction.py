"""C23F — the forward correction F-C5-1 of C23-2 (b)-(c): no G_T-orbit is admissible at c = 2; the weight bound 4 - 2 sqrt 2.

Round 6, research/countermodels. S0 (design, predictions, decision rule) appended to NOTES-C23 at 2026-10-11T15:20:46Z
(`date -u`), committed in a0a0177c before this script was written. Exact arithmetic only: Fractions and Gaussian
rationals; sympy for the symbolic identities and for sqrt(2). Deterministic.

Conventions (NOTES-C23): basis |00>, |01>, |10>, |11> (indices 0..3, control first); CNOT = the permutation (2 3);
X_B = 1 (x) X = (0 1)(2 3); D(u, v) = diag(1, uv, u, v); G_T = T^2 x| V4 modulo phase. Psi(h) = [[h0, h1], [h2, h3]],
|det Psi(h)|^2 / |h|^4 = D(h); lambda_max = (1 + sqrt(1 - 4 D))/2 for unit h. a_i = |h_i|, x = a0 a3 - a1 a2,
y = a0 a2 - a1 a3, S = sum a_i^2, A = a0^2 + a1^2, B = a2^2 + a3^2.
Checks:
  F1  CNOT carries every Bell state of C1' u C2' to a product (ten rational w, both circles; symbolic on the orbit);
      the c = 2 defect of the image pairs -1 with that product.
  F2  the four coset determinant identities (symbolic); D_min = min(x^2, y^2)/S^2 on 12 exact seeds against an exact
      minimization of |A - zB|^2 over unimodular z (the minimizer z = A conj(B)/|AB| and 32 rational unimodular z).
  F3  x + y = (a0 - a1)(a2 + a3), x - y = (a0 + a1)(a3 - a2) and the two sum-of-nonnegative-terms certificates.
  F4  attainment at h* = (sqrt2/2, 0, 1/2, 1/2): x^2 = y^2 = 1/8, c_max = 4 - 2 sqrt 2 exactly; comparisons of weights.
  F5  exhaustive exact control of D_min <= 1/8 over a in {0..6}^4 (integers) and m = (a_i^2) in {0..9}^4.
  F6  countercontrols and consequences: (a) T^2 x| <X_B> keeps the orbit of (1, 0, 0, 1) at D = 1/4; (b) T^2 x| <X_B>
      maps C1' u C2' into itself while CNOT maps it to products; (c) the mixture seed (3, 2i, 2, 1): D_min = 1/324 under
      G_T, admissible at 1001/1000; (d) C18-1's identity (symbolic) and the sign of its three terms for c_l in [0, c*].
Decision rule (NOTES-C23, round-6 appendix, S0): VERDICT C23F-EXACT iff F1-F6 give the predicted outcomes,
countercontrols included; a failed run is kept as .run1.*.
Pre-run edits (before the first run): F1's symbolic part computes the CNOT image of the torus orbit through the same
permutation helper as F2 (the first draft had the two determinants written out by hand); F1's pairing builds the c = 2
defect of the image as a matrix; the printed D_min of F2 is computed exactly (min(P, Q) - 2 sqrt(m0 m1 m2 m3))/S^2 instead
of through sympy's Min; no check's criterion changed.
Run from experiments/:  python3 -I -B c23f_correction.py > c23f_correction.out 2> c23f_correction.err
"""
from fractions import Fraction as F
import itertools
import sympy as sp


# ---------------- Gaussian rationals ----------------
class G:
    __slots__ = ("re", "im")

    def __init__(self, re, im=0):
        self.re = F(re)
        self.im = F(im)

    def __add__(self, o):
        o = o if isinstance(o, G) else G(o)
        return G(self.re + o.re, self.im + o.im)

    __radd__ = __add__

    def __sub__(self, o):
        o = o if isinstance(o, G) else G(o)
        return G(self.re - o.re, self.im - o.im)

    def __rsub__(self, o):
        return G(o) - self

    def __mul__(self, o):
        o = o if isinstance(o, G) else G(o)
        return G(self.re * o.re - self.im * o.im, self.re * o.im + self.im * o.re)

    __rmul__ = __mul__

    def __neg__(self):
        return G(-self.re, -self.im)

    def conj(self):
        return G(self.re, -self.im)

    def abs2(self):
        return self.re * self.re + self.im * self.im

    def __truediv__(self, o):
        o = o if isinstance(o, G) else G(o)
        a = o.abs2()
        return self * G(o.re / a, -o.im / a)

    def iszero(self):
        return self.re == 0 and self.im == 0

    def __repr__(self):
        return f"({self.re}{'+' if self.im >= 0 else '-'}{abs(self.im)}i)"


def vec(*xs):
    return [x if isinstance(x, G) else G(*x) if isinstance(x, tuple) else G(x) for x in xs]


def n2(v):
    return sum((x.abs2() for x in v), F(0))


def detpsi(h):
    return h[0] * h[3] - h[1] * h[2]


def Dmat(u, v):
    return [u * 0 + 1, u * v, u, v]  # diagonal entries of D(u, v)


def apply_diag(dg, h):
    return [dg[i] * h[i] for i in range(4)]


def perm(p, h):
    # (p h)[p[i]] = h[i]
    out = [None] * 4
    for i in range(4):
        out[p[i]] = h[i]
    return out


CNOTP = [0, 1, 3, 2]
XBP = [1, 0, 3, 2]


def unimod(a, b, c):
    # (a + bi)/c with a^2 + b^2 = c^2
    assert a * a + b * b == c * c
    return G(F(a, c), F(b, c))


TRIPLES = [(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25), (20, 21, 29), (12, 35, 37), (9, 40, 41), (28, 45, 53)]
UNIMOD = []
for (a, b, c) in TRIPLES:
    for (sa, sb) in [(1, 1), (-1, 1), (1, -1), (-1, -1)]:
        UNIMOD.append(unimod(sa * a, sb * b, c))
UNIMOD = UNIMOD[:32]

results = []


def report(name, ok, detail):
    results.append(bool(ok))
    print(f"{name}  {'PASS' if ok else 'FAIL'}  {detail}")


def ssqrt(q):
    return sp.sqrt(sp.Rational(q.numerator, q.denominator))


# ---------------- F1: CNOT carries the Bell circles to products ----------------
W10 = [G(1), G(-1), G(0, 1), G(0, -1), unimod(3, 4, 5), unimod(-3, 4, 5), unimod(3, -4, 5), unimod(-3, -4, 5),
       unimod(5, 12, 13), unimod(8, 15, 17)]
ok1 = True
n_states = 0
for w in W10:
    for b in (vec(1, 0, 0, w), vec(0, 1, w, 0)):
        n_states += 1
        me = detpsi(b).abs2() / (n2(b) ** 2) == F(1, 4)
        cb = perm(CNOTP, b)
        prod = detpsi(cb).iszero()
        # d = I - 2 cb cb^dag/|cb|^2 as a matrix; the form (cb^dag d cb)/|cb|^2
        nb = n2(cb)
        dmat = [[(G(1) if i == j else G(0)) - G(2) * cb[i] * cb[j].conj() / G(nb) for j in range(4)] for i in range(4)]
        dcb = [sum((dmat[i][j] * cb[j] for j in range(4)), G(0)) for i in range(4)]
        form = sum((cb[i].conj() * dcb[i] for i in range(4)), G(0)) / G(nb)
        val = form.re if form.im == 0 else None
        ok1 = ok1 and me and prod and val == -1
u_s, v_s, w_s = sp.symbols("u v w")
hs = sp.symbols("h0 h1 h2 h3")


def sym_apply(dg, perm_p, hh):
    x = [dg[i] * hh[i] for i in range(4)]
    out = [None] * 4
    for i in range(4):
        out[perm_p[i]] = x[i]
    return out


dgs = [1, u_s * v_s, u_s, v_s]
g_c1 = sym_apply(dgs, CNOTP, (1, 0, 0, w_s))
g_c2 = sym_apply(dgs, CNOTP, (0, 1, w_s, 0))
sym1 = sp.expand(g_c1[0] * g_c1[3] - g_c1[1] * g_c1[2])
sym2 = sp.expand(g_c2[0] * g_c2[3] - g_c2[1] * g_c2[2])
report("F1", ok1 and sym1 == 0 and sym2 == 0 and CNOTP == [0, 1, 3, 2],
       f"{n_states} Bell states (ten rational w, both circles): maximally entangled (|det Psi|^2/|b|^4 = 1/4), CNOT image a "
       f"product (det = 0), the c = 2 defect of the image pairs -1 with it: {ok1}; symbolic on the T^2-orbits: det Psi("
       f"CNOT D(u,v) b) = 0 for both circles: {sym1 == 0 and sym2 == 0}; CNOT = (2 3) in G_1")

# ---------------- F2: coset determinant identities; D_min formula ----------------
ID = [0, 1, 2, 3]
XC = [XBP[CNOTP[i]] for i in range(4)]  # X_B after CNOT
cos = {
    "e": (ID, v_s * (hs[0] * hs[3] - u_s ** 2 * hs[1] * hs[2])),
    "CNOT": (CNOTP, u_s * (hs[0] * hs[2] - v_s ** 2 * hs[1] * hs[3])),
    "X_B": (XBP, -v_s * (hs[0] * hs[3] - u_s ** 2 * hs[1] * hs[2])),
    "X_B CNOT": (XC, -u_s * (hs[0] * hs[2] - v_s ** 2 * hs[1] * hs[3])),
}
id_ok = True
for nm, (pp, expect) in cos.items():
    g = sym_apply(dgs, pp, hs)
    d = sp.expand(g[0] * g[3] - g[1] * g[2] - expect)
    id_ok = id_ok and d == 0

SEEDS = [vec(6, (0, 1), 4, 3), vec(4, (0, 1), 2, 3), vec(3, (0, 2), 2, 1), vec(2, (0, 3), 1, 6), vec(3, 1, (0, 2), 0),
         vec(3, 0, (0, 2), 1), vec((1, 1), (2, -1), 3, (0, 1)), vec(5, (1, 2), (2, 2), (-1, 3)),
         vec(10, (2, -2), (-1, -3), (3, -1)), vec(1, 1, 1, (0, 1)), vec(2, 1, (1, 1), 3), vec(7, (0, 5), (1, -4), 2)]


def min_check(A, B):
    """exact: min over unimodular z of |A - zB|^2 equals (|A| - |B|)^2."""
    a2, b2 = A.abs2(), B.abs2()
    closed = sp.Rational(a2.numerator, a2.denominator) + sp.Rational(b2.numerator, b2.denominator) \
        - 2 * ssqrt(a2 * b2)
    # minimizer z0 = A conj(B)/(|A||B|) (when AB != 0): |A - z0 B|^2 = |A|^2 + |B|^2 - 2|A||B|
    if a2 != 0 and b2 != 0:
        Ar = sp.Rational(A.re.numerator, A.re.denominator) + sp.I * sp.Rational(A.im.numerator, A.im.denominator)
        Br = sp.Rational(B.re.numerator, B.re.denominator) + sp.I * sp.Rational(B.im.numerator, B.im.denominator)
        z0 = Ar * sp.conjugate(Br) / (ssqrt(a2) * ssqrt(b2))
        val = sp.expand((Ar - z0 * Br) * sp.conjugate(Ar - z0 * Br))
        at_min = sp.simplify(val - closed) == 0 and sp.simplify(sp.Abs(z0) ** 2 - 1) == 0
    else:
        at_min = True  # then |A - zB| is constant = max(|A|, |B|) = ||A| - |B||
    # every rational unimodular z gives a value >= closed:  q >= r - 2 sqrt(s)  <=>  r - q <= 0 or (r - q)^2 <= 4 s
    lower = True
    for z in UNIMOD:
        q = (A - z * B).abs2()
        r = a2 + b2
        s = a2 * b2
        t = r - q
        lower = lower and (t <= 0 or t * t <= 4 * s)
    return at_min and lower, closed


f2_ok = True
f2_detail = []
for h in SEEDS:
    S = n2(h)
    okA, xA = min_check(h[0] * h[3], h[1] * h[2])
    okB, xB = min_check(h[0] * h[2], h[1] * h[3])
    a = [ssqrt(x.abs2()) for x in h]
    xx = a[0] * a[3] - a[1] * a[2]
    yy = a[0] * a[2] - a[1] * a[3]
    agree = sp.simplify(sp.expand(xx ** 2) - xA) == 0 and sp.simplify(sp.expand(yy ** 2) - xB) == 0
    m = [x.abs2() for x in h]
    Pq, Qq = m[0] * m[3] + m[1] * m[2], m[0] * m[2] + m[1] * m[3]
    dmin = (sp.Rational(min(Pq, Qq).numerator, min(Pq, Qq).denominator) - 2 * ssqrt(m[0] * m[1] * m[2] * m[3])) \
        / sp.Rational(S.numerator, S.denominator) ** 2
    f2_ok = f2_ok and okA and okB and agree
    f2_detail.append(str(sp.radsimp(dmin)))
report("F2", id_ok and f2_ok,
       f"coset identities det Psi(g D(u,v) h) for g in {{e, CNOT, X_B, X_B CNOT}} (symbolic): {id_ok}; on 12 exact seeds "
       f"the minimum of |A - zB|^2 over unimodular z is (|A| - |B|)^2 (minimizer exact, 32 rational z above it) for both "
       f"moduli and agrees with x^2, y^2: {f2_ok}; D_min = {', '.join(f2_detail)}")

# ---------------- F3: the bound's certificates ----------------
a0, a1, a2, a3 = sp.symbols("a0 a1 a2 a3", nonnegative=True)
X = a0 * a3 - a1 * a2
Y = a0 * a2 - a1 * a3
S_ = a0 ** 2 + a1 ** 2 + a2 ** 2 + a3 ** 2
A_ = a0 ** 2 + a1 ** 2
B_ = a2 ** 2 + a3 ** 2
fac1 = sp.expand(X + Y - (a0 - a1) * (a2 + a3)) == 0
fac2 = sp.expand(X - Y - (a0 + a1) * (a3 - a2)) == 0
cert1 = sp.expand(S_ ** 2 / 2 - (X + Y) ** 2 - ((A_ - B_) ** 2 / 2 + A_ * (a2 - a3) ** 2 + 2 * a0 * a1 * (a2 + a3) ** 2)) == 0
cert2 = sp.expand(S_ ** 2 / 2 - (X - Y) ** 2 - ((A_ - B_) ** 2 / 2 + B_ * (a0 - a1) ** 2 + 2 * a2 * a3 * (a0 + a1) ** 2)) == 0
# |x| + |y| = max(|x + y|, |x - y|): on the four sign cases
signs = all(abs(p) + abs(q) == max(abs(p + q), abs(p - q)) for p in (-3, -1, 0, 2, 5) for q in (-4, 0, 1, 3))
report("F3", fac1 and fac2 and cert1 and cert2 and signs,
       f"x + y = (a0 - a1)(a2 + a3): {fac1}; x - y = (a0 + a1)(a3 - a2): {fac2}; S^2/2 - (x+y)^2 = (A-B)^2/2 + A(a2-a3)^2 + "
       f"2a0a1(a2+a3)^2: {cert1}; S^2/2 - (x-y)^2 = (A-B)^2/2 + B(a0-a1)^2 + 2a2a3(a0+a1)^2: {cert2}; |x|+|y| = "
       f"max(|x+y|, |x-y|) on sampled integers: {signs}; hence D_min <= ((|x|+|y|)/2)^2/S^2 <= 1/8")

# ---------------- F4: attainment and the weight bound ----------------
r2 = sp.sqrt(2)
hstar = [r2 / 2, 0, sp.Rational(1, 2), sp.Rational(1, 2)]
xs = hstar[0] * hstar[3] - hstar[1] * hstar[2]
ys = hstar[0] * hstar[2] - hstar[1] * hstar[3]
Ss = sum(t ** 2 for t in hstar)
dstar = sp.simplify(sp.Min(xs ** 2, ys ** 2) / Ss ** 2)
cmax = sp.simplify(2 / (1 + sp.sqrt(1 - 4 * dstar)))
bound = 4 - 2 * r2
att = sp.simplify(xs ** 2 - sp.Rational(1, 8)) == 0 and sp.simplify(ys ** 2 - sp.Rational(1, 8)) == 0 and Ss == 1
cm_ok = sp.simplify(cmax - bound) == 0
prodone = sp.simplify(bound * (2 + r2) / 4 - 1) == 0


def less_than_bound(q):
    # q < 4 - 2 sqrt 2  <=>  4 - q > 0 and (4 - q)^2 > 8
    return (4 - q) > 0 and (4 - q) ** 2 > 8


cmp_ok = all(less_than_bound(q) for q in (F(51, 50), F(101, 100), F(1001, 1000), F(251, 250))) and \
    not less_than_bound(F(6, 5)) and not less_than_bound(F(2))
report("F4", att and cm_ok and prodone and cmp_ok,
       f"h* = (sqrt2/2, 0, 1/2, 1/2): x^2 = y^2 = 1/8, |h*| = 1: {att}; D_min(h*) = {dstar}; c_max = 2/(1 + sqrt(1 - 4 D_min)) "
       f"= {sp.radsimp(cmax)} = 4 - 2 sqrt 2: {cm_ok}; (4 - 2 sqrt 2)(2 + sqrt 2)/4 = 1: {prodone}; 51/50, 101/100, "
       f"1001/1000, 251/250 < 4 - 2 sqrt 2 < 6/5 < 2: {cmp_ok}")

# ---------------- F5: exhaustive exact control ----------------
viol_a = 0
best_a = F(0)
best_a_at = None
for a in itertools.product(range(7), repeat=4):
    S = sum(t * t for t in a)
    if S == 0:
        continue
    x_ = a[0] * a[3] - a[1] * a[2]
    y_ = a[0] * a[2] - a[1] * a[3]
    m_ = F(min(x_ * x_, y_ * y_), S * S)
    if m_ > F(1, 8):
        viol_a += 1
    if m_ > best_a:
        best_a, best_a_at = m_, a
viol_m = 0
eq_m = []
for m in itertools.product(range(10), repeat=4):
    S = sum(m)
    if S == 0:
        continue
    P = m[0] * m[3] + m[1] * m[2]
    Q = m[0] * m[2] + m[1] * m[3]
    M = m[0] * m[1] * m[2] * m[3]
    t = F(min(P, Q)) - F(S * S, 8)  # D_min * S^2 - S^2/8 = t - 2 sqrt(M)
    if t > 0 and t * t > 4 * M:
        viol_m += 1
    if t >= 0 and t * t == 4 * M:
        eq_m.append(m)
f5 = viol_a == 0 and viol_m == 0 and (2, 0, 1, 1) in eq_m
report("F5", f5,
       f"a in {{0..6}}^4 (integers): violations {viol_a}, max D_min = {best_a} at {best_a_at} (< 1/8: 1/8 needs S^2 = 8 x^2); "
       f"m in {{0..9}}^4 (a_i = sqrt m_i): violations {viol_m}, equality D_min = 1/8 at {len(eq_m)} tuples, e.g. "
       f"{eq_m[:6]}; (2, 0, 1, 1) among them: {(2, 0, 1, 1) in eq_m}")

# ---------------- F6: countercontrols and consequences ----------------
# (a) T^2 x| <X_B> keeps (1, 0, 0, 1) maximally entangled
b0 = vec(1, 0, 0, 1)
ca = True
for (u, v) in list(zip(UNIMOD[:16], UNIMOD[16:32])):
    g1 = apply_diag(Dmat(u, v), b0)
    g2 = perm(XBP, g1)
    for gg in (g1, g2):
        ca = ca and detpsi(gg).abs2() / n2(gg) ** 2 == F(1, 4)
# (b) T^2 x| <X_B> maps C1' u C2' into itself; CNOT maps it to products


def in_bell(h):
    if h[1].iszero() and h[2].iszero() and not h[0].iszero():
        return h[0].abs2() == h[3].abs2()
    if h[0].iszero() and h[3].iszero() and not h[1].iszero():
        return h[1].abs2() == h[2].abs2()
    return False


cb_ok = True
for w in W10[:6]:
    for b in (vec(1, 0, 0, w), vec(0, 1, w, 0)):
        for (u, v) in list(zip(UNIMOD[:8], UNIMOD[8:16])):
            g1 = apply_diag(Dmat(u, v), b)
            cb_ok = cb_ok and in_bell(g1) and in_bell(perm(XBP, g1)) and detpsi(perm(CNOTP, g1)).iszero()
# (c) the mixture seed
hm = vec(3, (0, 2), 2, 1)
am = [3, 2, 2, 1]
xm = am[0] * am[3] - am[1] * am[2]
ym = am[0] * am[2] - am[1] * am[3]
Sm = sum(t * t for t in am)
dm = F(min(xm * xm, ym * ym), Sm * Sm)
cst = F(1001, 1000)
adm = 1 - 4 * dm <= (2 / cst - 1) ** 2
cc_ok = dm == F(1, 324) and adm and n2(hm) == Sm
# (d) C18-1's identity
cs, cl, s, sprime = sp.symbols("cstar cl s sprime")
lam = (cs - 1) / (4 - 2 * cs)
lhs = 1 - cl * s + lam * (4 - cs - cl + cs * cl * sprime)
rhs = cs * (1 - s) + (cs - cl) * (s + lam) + lam * cs * cl * sprime
ident = sp.simplify(lhs - rhs) == 0
c0 = sp.Rational(51, 50)
signs_ok = True
for clv in (sp.Integer(0), sp.Integer(1), c0):
    for sv in (sp.Integer(0), sp.Rational(1, 3), sp.Integer(1)):
        for spv in (sp.Integer(0), sp.Rational(1, 2), sp.Integer(1)):
            terms = [c0 * (1 - sv), (c0 - clv) * (sv + lam.subs(cs, c0)), lam.subs(cs, c0) * c0 * clv * spv]
            signs_ok = signs_ok and all(t >= 0 for t in terms)
pair_ok = all((4 - clv - c0 + clv * c0 * sv) >= 4 - 2 * c0 for clv in (sp.Integer(1), c0) for sv in (0, sp.Rational(1, 2), 1))
report("F6", ca and cb_ok and cc_ok and ident and signs_ok and pair_ok,
       f"(a) without CNOT (T^2 x| <X_B>) the orbit of (1,0,0,1) keeps D = 1/4 at 16 torus points and their X_B images: {ca}; "
       f"(b) T^2 x| <X_B> maps 12 Bell states x 8 torus points into C1' u C2', CNOT maps every image to a product: {cb_ok}; "
       f"(c) mixture seed (3, 2i, 2, 1): D_min = {dm} under G_T, admissible at 1001/1000: {cc_ok}; (d) C18-1's identity "
       f"(symbolic): {ident}; its three terms >= 0 for c_l in {{0, 1, c*}} at c* = 51/50: {signs_ok}; <d_l, d_h> >= 4 - 2c* "
       f"for c_l in {{1, c*}}: {pair_ok}")

n_ok = sum(results)
print(f"CHECKS {n_ok}/{len(results)}")
print("VERDICT C23F-EXACT" if n_ok == len(results) else "VERDICT C23F-FAIL")
