"""C18 — explicit cones where rank-one surgeries with a common c fail: three attempts, exact checks.

Node C18 (round 4, research/countermodels). S0 (predictions and decision rules) in NOTES-C18, written
2026-10-11T04:55Z (`date -u`) before this script was first run.

Groups. Case B (NOTES-C13 R0): G_B = T^3 x| <cnot, g'> acting in the orthonormal basis b^_k = b_k/|b_k| by
D.sigma~ (D diagonal phases, sigma~ in {I, cnot = (12), g' = (34), cnot g' = (12)(34)} as permutation matrices).
S2 with G16 (NOTES-C13 C13-S2): in B = (|0+>, |0->, |1+>, |1->): T^2 = diag(conj x1, conj x2, x2, x1),
cnot = diag(1,1,1,-1), Z(x)I = diag(1,1,-1,-1), I(x)Z = permutation (12)(34), T = complex conjugation.

Checks (each with its control): A1-id, A1-B, A1-S2, A1-cc, A1-Bell; A2a, A2b-partners, A2b-zero, A2b-near;
A3-irr, A3-perm, A3-schur, A3-slice. Exact arithmetic only (Gaussian rationals; sympy for identities). Deterministic.
"""
from fractions import Fraction as F
import itertools
import sympy as sp


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

    def __neg__(self):
        return G(-self.re, -self.im)

    def __mul__(self, o):
        o = o if isinstance(o, G) else G(o)
        return G(self.re * o.re - self.im * o.im, self.re * o.im + self.im * o.re)

    __rmul__ = __mul__

    def conj(self):
        return G(self.re, -self.im)

    def abs2(self):
        return self.re * self.re + self.im * self.im

    def inv(self):
        a = self.abs2()
        return G(self.re / a, -self.im / a)

    def __eq__(self, o):
        o = o if isinstance(o, G) else G(o)
        return self.re == o.re and self.im == o.im

    def __hash__(self):
        return hash((self.re, self.im))

    def __repr__(self):
        if self.im == 0:
            return f"{self.re}"
        return f"({self.re}{'+' if self.im >= 0 else '-'}{abs(self.im)}i)"


I_ = G(0, 1)


def V(*xs):
    return [x if isinstance(x, G) else G(x) for x in xs]


def ip(a, b):
    s = G(0)
    for x, y in zip(a, b):
        s = s + x.conj() * y
    return s


def n2(a):
    return ip(a, a).re


def proj(h):
    """h h† / |h|² (exact)."""
    nn = n2(h)
    return [[h[i] * h[j].conj() * G(1 / nn) for j in range(len(h))] for i in range(len(h))]


def eye(n=4):
    return [[G(1 if i == j else 0) for j in range(n)] for i in range(n)]


def madd(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A))] for i in range(len(A))]


def msub(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A))] for i in range(len(A))]


def mscale(c, A):
    c = c if isinstance(c, G) else G(c)
    return [[c * A[i][j] for j in range(len(A))] for i in range(len(A))]


def mmul(A, B):
    n = len(A)
    return [[sum((A[i][k] * B[k][j] for k in range(n)), G(0)) for j in range(n)] for i in range(n)]


def tr(A):
    return sum((A[i][i] for i in range(len(A))), G(0))


def pair(A, B):
    t = tr(mmul(A, B))
    assert t.im == 0
    return t.re


def defect(c, h):
    return msub(eye(len(h)), mscale(c, proj(h)))


def qform(A, x):
    Ax = [sum((A[i][j] * x[j] for j in range(len(x))), G(0)) for i in range(len(x))]
    t = ip(x, Ax)
    assert t.im == 0
    return t.re


def apply_perm(perm, v):
    """(sigma~ v)_m = v_{perm[m]} (perm as a tuple of indices)."""
    return [v[perm[m]] for m in range(len(v))]


def apply_diag(d, v):
    return [d[m] * v[m] for m in range(len(v))]


def s_ov(a, b):
    """squared overlap of the rays of a and b."""
    return ip(a, b).abs2() / (n2(a) * n2(b))


results = []


def report(name, ok, detail):
    results.append(ok)
    print(f"{name}  {'PASS' if ok else 'FAIL'}  {detail}")


UNITS = [G(1), I_, G(-1), -I_, G(F(3, 5), F(4, 5)), G(F(5, 13), F(-12, 13)), G(F(-8, 17), F(15, 17))]

# ===================== Attempt 1 =====================
cs, cl, s, s1 = sp.symbols("cstar c_l s s_prime")
lam_s = (cs - 1) / (4 - 2 * cs)
lhs = (1 - cl * s) + lam_s * (4 - cs - cl + cs * cl * s1)
rhs = cs * (1 - s) + (cs - cl) * (s + lam_s) + lam_s * cs * cl * s1
ident = sp.simplify(lhs - rhs)
report("A1-id", ident == 0, f"<y,d_l> - [c*(1-s) + (c*-c_l)(s+lam) + lam c* c_l s'] = {ident}")


def witness_checks(h, hp, cstar, samples):
    """samples: list of (c_l, h_l). Returns (all identity matches, min pairing, h'†yh' sign, d_h pairing)."""
    lam = (cstar - 1) / (4 - 2 * cstar)
    y = madd(proj(h), mscale(lam, defect(cstar, hp)))
    dh = defect(cstar, h)
    ok_id = True
    mn = None
    pos_dh = True
    for c_l, h_l in samples:
        d_l = defect(c_l, h_l)
        p = pair(y, d_l)
        sh, shp = s_ov(h, h_l), s_ov(hp, h_l)
        formula = cstar * (1 - sh) + (cstar - c_l) * (sh + lam) + lam * cstar * c_l * shp
        ok_id = ok_id and p == formula
        mn = p if mn is None or p < mn else mn
        pos_dh = pos_dh and pair(d_l, dh) > 0
    q = qform(y, hp)
    return ok_id, mn, q, pair(y, dh), pos_dh


# A1-B: case B in b^ coordinates
PI_B = [(0, 1, 2, 3), (1, 0, 2, 3), (0, 1, 3, 2), (1, 0, 3, 2)]
hB = V(2, 1, 0, 0)
hBp = V(1, -2, 0, 0)
cnot_b = (1, 0, 2, 3)
assert apply_diag(V(1, -1, 1, 1), apply_perm(cnot_b, hB)) == hBp
h2B = V(1, G(0, 1), 2, G(1, 1))
c_star, c_two = F(51, 50), F(101, 100)
samples = []
for (c_l, base) in [(c_star, hB), (c_two, h2B)]:
    for perm in PI_B:
        for dvec in [(UNITS[0], UNITS[1], UNITS[4], UNITS[5]), (UNITS[2], UNITS[4], UNITS[6], UNITS[1]),
                     (UNITS[5], UNITS[3], UNITS[1], UNITS[6]), (UNITS[0], UNITS[0], UNITS[0], UNITS[0])]:
            samples.append((c_l, apply_diag(list(dvec), apply_perm(perm, base))))
samples.append((c_star, hBp))
okid, mn, q, pdh, posdh = witness_checks(hB, hBp, c_star, samples)
report("A1-B", okid and mn >= 0 and q < 0 and pdh == 0 and posdh,
       f"{len(samples)} sample defects (orbits of (2,1,0,0) at 51/50 and (1,i,2,1+i) at 101/100): identity {okid}, "
       f"min pairing {mn}, h'†yh' = {q}, <y,d_h> = {pdh}, all <d_l,d_h> > 0: {posdh}")

# A1-S2: B coordinates
def s2_elements(units):
    """sample elements of G_S2 as functions v -> g v."""
    els = []
    for x1, x2 in itertools.product(units[:5], units[2:6]):
        D = V(x1.conj(), x2.conj(), x2, x1)
        for extra in [V(1, 1, 1, 1), V(1, 1, 1, -1), V(1, 1, -1, -1)]:
            for perm in [(0, 1, 2, 3), (1, 0, 3, 2)]:
                for conjugate in [False, True]:
                    def g(v, D=D, extra=extra, perm=perm, conjugate=conjugate):
                        w = [x.conj() for x in v] if conjugate else list(v)
                        w = apply_perm(perm, w)
                        w = apply_diag(extra, w)
                        return apply_diag(D, w)
                    els.append(g)
    return els


S2_EL = s2_elements(UNITS)
hS = V(3, 0, 0, 1)
hSp = apply_perm((1, 0, 3, 2), hS)          # (I(x)Z) h = 3|0-> + |1+>
assert ip(hS, hSp) == G(0)
h2S = V(1, 1, 1, I_)
cS_star, cS_two = F(21, 20), F(41, 40)
samplesS = [(cS_star, g(hS)) for g in S2_EL[::7]] + [(cS_two, g(h2S)) for g in S2_EL[::11]] + [(cS_star, hSp)]
okid, mn, q, pdh, posdh = witness_checks(hS, hSp, cS_star, samplesS)
report("A1-S2", okid and mn >= 0 and q < 0 and pdh == 0 and posdh,
       f"{len(samplesS)} sample defects (orbits of 3|0+>+|1-> at 21/20 and (1,1,1,i) at 41/40): identity {okid}, "
       f"min pairing {mn}, h'†yh' = {q}, <y,d_h> = {pdh}, all <d_l,d_h> > 0: {posdh}")

# A1-cc: two values of c on one orbit; the witness on the smaller c fails
c_hi, c_lo = F(51, 50), F(101, 100)
lam_lo = (c_lo - 1) / (4 - 2 * c_lo)
y_lo = madd(proj(hB), mscale(lam_lo, defect(c_lo, hBp)))
bad = pair(y_lo, defect(c_hi, hB))
lam_hi = (c_hi - 1) / (4 - 2 * c_hi)
y_hi = madd(proj(hB), mscale(lam_hi, defect(c_hi, hBp)))
good = min(pair(y_hi, defect(c, v)) for c in (c_hi, c_lo) for v in (hB, hBp))
report("A1-cc", bad < 0 and good >= 0,
       f"witness on c = 101/100 against d_h(51/50): {bad} (< 0); witness on c = 51/50 against the four defects: min {good}")

# A1-Bell: S2 mixtures with the Bell circles C1 = {(1,0,0,w)}, C2 = {(0,1,w,0)} at c = 2
lamS = (cS_star - 1) / (4 - 2 * cS_star)
yS = madd(proj(hS), mscale(lamS, defect(cS_star, hSp)))
neg = pair(yS, defect(2, V(1, 0, 0, 1)))
hQ = V(1, 1, 1, I_)
hQp = apply_diag(V(1, 1, -1, -1), hQ)        # (Z(x)I) h
assert ip(hQ, hQp) == G(0)
cQ = F(11, 10)
lamQ = (cQ - 1) / (4 - 2 * cQ)
yQ = madd(proj(hQ), mscale(lamQ, defect(cQ, hQp)))
bell_pts = [V(1, 0, 0, w) for w in UNITS] + [V(0, 1, w, 0) for w in UNITS]
minQ = min(pair(yQ, defect(2, b)) for b in bell_pts)
max_sb = max(s_ov(hQ, b) for b in bell_pts)
# symbolic: for |w| = 1, s_b = |1 - i w|^2/8 (C1) and |1 + w|^2/8 (C2), both <= 1/2
report("A1-Bell", neg < 0 and minQ >= (cQ - 1) / 2 and max_sb <= F(1, 2),
       f"circle orbit at 21/20 vs Bell w=1: {neg} (< 0, lemma inapplicable); orbit of (1,1,1,i) at 11/10: "
       f"min Bell pairing {minQ} >= (c*-1)/2 = {(cQ - 1) / 2}, max s_b {max_sb}")

# ===================== Attempt 2 =====================
# A2a: rank-two negative part is never block-positive
def prod_vec(a, b):
    return [a[0] * b[0], a[0] * b[1], a[1] * b[0], a[1] * b[1]]


def two_defect(c1, h1, c2, h2):
    return msub(msub(eye(), mscale(c1, proj(h1))), mscale(c2, proj(h2)))


pairs = [((F(3, 2), V(1, 0, 0, 1)), (F(5, 4), V(0, 1, 1, 0)), prod_vec(V(1, 1), V(1, 1))),
         ((F(6, 5), V(3, 0, 0, 1)), (F(11, 10), V(0, 1, 3, 0)), prod_vec(V(1, 1), V(3, 1)))]
ok2a = True
vals2a = []
for (c1, h1), (c2, h2), p in pairs:
    assert ip(h1, h2) == G(0)
    # p lies in span(h1, h2): p = alpha h1 + beta h2 with the coefficients <h_i|p>/|h_i|^2
    a1, a2 = ip(h1, p) * G(1 / n2(h1)), ip(h2, p) * G(1 / n2(h2))
    ok2a = ok2a and [a1 * x + a2 * y for x, y in zip(h1, h2)] == p
    val = qform(two_defect(c1, h1, c2, h2), p)
    vals2a.append(val)
    ok2a = ok2a and val < 0
# control: a rank-one defect within H1 (h = 3|00> + |11>, lambda_max = 9/10, c = 10/9): nonnegative on products
hc = V(3, 0, 0, 1)
dc = defect(F(10, 9), hc)
grid = [prod_vec(V(a, b), V(c, e)) for a, b, c, e in itertools.product([1, 2, -1, I_], [0, 1, I_, -2], [1, 3, -I_], [0, 1, 2])]
minc = min(qform(dc, p) / n2(p) for p in grid if n2(p) > 0)
at00 = qform(dc, prod_vec(V(1, 0), V(1, 0)))
report("A2a", ok2a and minc >= 0 and at00 == 0,
       f"p in the negative plane, p†dp = {vals2a} (< 0); control rank-one defect at 10/9: min over {len(grid)} products "
       f"{minc}, value at |00> {at00}")

# A2b: balanced rank-two defects in case B
d1, d2, d3, d4 = sp.symbols("d1 d2 d3 d4")
hb = [sp.Rational(2, 7), sp.Rational(3, 7), 0, sp.Rational(6, 7)]
kb = [sp.Rational(2, 7), sp.Rational(3, 7), 0, sp.Rational(-13, 42)]
D = [d1, d2, d3, d4]


def sym_ip_g(a, b, perm):
    """<a | D sigma~ b> with real a (coefficients of a are real here)."""
    sb = [b[perm[m]] for m in range(4)]
    return sp.expand(sum(a[m] * D[m] * sb[m] for m in range(4)))


part = {}
for perm, name in zip(PI_B, ["e", "(12)", "(34)", "(12)(34)"]):
    part[name] = sym_ip_g(hb, hb, perm)
# for e, (12), (34): one coefficient's modulus exceeds the sum of the others (no zero on the torus)
def dominated(expr):
    coeffs = [abs(sp.Poly(expr, *D).coeff_monomial(x)) for x in D]
    m = max(coeffs)
    return m > sum(coeffs) - m


okp = dominated(part["e"]) and dominated(part["(12)"]) and dominated(part["(34)"])
fam = part["(12)(34)"]
okp = okp and sp.simplify(fam.subs(d2, -d1)) == 0 and sp.Poly(fam, *D).coeff_monomial(d3) == 0 \
    and sp.Poly(fam, *D).coeff_monomial(d4) == 0
report("A2b-partners", okp and sum(x * x for x in hb) == 1 and sum(a * b for a, b in zip(hb, kb)) == 0,
       f"<h|D s~ h>: e {part['e']}, (12) {part['(12)']}, (34) {part['(34)']} (dominated); (12)(34) {fam} "
       f"(zero iff d2 = -d1)")
perm1234 = PI_B[3]
zs = [sym_ip_g(hb, kb, perm1234), sym_ip_g(kb, hb, perm1234), sym_ip_g(kb, kb, perm1234)]
zs = [sp.simplify(z.subs(d2, -d1)) for z in zs]
report("A2b-zero", all(z == 0 for z in zs),
       f"on d2 = -d1: <h|gk>, <k|gh>, <k|gk> = {zs} (plane of the partner orthogonal to span(h, k))")

# A2b-near: the engine's local condition fails for a nearby pair d, U d U†
hE = V(F(2, 7), F(3, 7), 0, F(6, 7))
kE = V(F(2, 7), F(3, 7), 0, F(-13, 42))
cE = F(3, 2)
dE = msub(msub(eye(), mscale(cE, proj(hE))), mscale(2 - cE, proj(kE)))
k2 = n2(kE)
found = None
ctrl_ok = True
for m in [20, 40, 80]:
    for sgn in [1, -1]:
        ph = G(F(m * m - 1, m * m + 1), F(sgn * 2 * m, m * m + 1))
        U = [[ph if (i == j == 0) else G(1 if i == j else 0) for j in range(4)] for i in range(4)]
        Ud = [[U[i][j].conj() for i in range(4)] for j in range(4)]
        dU = mmul(mmul(U, dE), Ud)
        for b in [F(166, 100), F(1663, 1000), F(165, 100)]:
            for phi in [I_, -I_]:
                u = [hE[i] + G(b) * phi * kE[i] for i in range(4)]
                x = [G(-b * k2) * hE[i] + phi * kE[i] for i in range(4)]
                assert ip(u, x) == G(0)
                incap = qform(dE, u) < 0
                ctrl_ok = ctrl_ok and (not incap or qform(dE, x) > 0)
                if incap and pair(dE, dU) > 0 and qform(dU, x) < 0 and found is None:
                    found = (m, sgn, b, phi, qform(dU, x), qform(dE, x))
report("A2b-near", found is not None and ctrl_ok,
       f"nearby pair violating the local condition (m, sign, b, phi, x†(UdU†)x, x†dx) = {found}; "
       f"control x†dx > 0 at every tested cap point: {ctrl_ok}")

# ===================== Attempt 3 =====================
# A3-irr: six inequivalent off-diagonal characters of the diagonal subgroups
blocks = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]


def chars_ok(diag_elems):
    vals = {bk: [D_[bk[0]] * D_[bk[1]].conj() for D_ in diag_elems] for bk in blocks}
    ok = True
    for b1, b2 in itertools.combinations(blocks, 2):
        ok = ok and any(x != y for x, y in zip(vals[b1], vals[b2])) \
            and any(x != y.conj() for x, y in zip(vals[b1], vals[b2]))
    ok = ok and all(any(v.im != 0 for v in vals[bk]) for bk in blocks)
    return ok


diagB = [V(*dv) for dv in itertools.product(UNITS[:2], UNITS[3:5], UNITS[4:6], UNITS[5:7])]
diagS = []
for x1, x2 in itertools.product(UNITS[3:6], UNITS[4:7]):
    for extra in [V(1, 1, 1, 1), V(1, 1, 1, -1), V(1, 1, -1, -1)]:
        diagS.append(apply_diag(extra, V(x1.conj(), x2.conj(), x2, x1)))
report("A3-irr", chars_ok(diagB) and chars_ok(diagS),
       f"case B torus ({len(diagB)} elements) and S2's <T^2, cnot, Z(x)I> ({len(diagS)} elements): six pairwise "
       f"inequivalent, non-real off-diagonal characters")

# A3-perm: permutations of the diagonal commuting with the eigenline action, refuted except e
def centralizer(gens):
    out = []
    for t in itertools.permutations(range(4)):
        if all(tuple(t[g[i]] for i in range(4)) == tuple(g[t[i]] for i in range(4)) for g in gens):
            out.append(t)
    return out


b1 = V(4, G(-2, 4), 6, G(-3, 6))
b2 = V(4, G(-2, 4), G(-3, 6), 6)
b3 = V(G(1, 2), 2, 0, 0)
b4 = V(10, G(-5, 10), G(-6, -12), G(-6, -12))
Bb = [b1, b2, b3, b4]
assert all(ip(Bb[i], Bb[j]) == G(0) for i in range(4) for j in range(4) if i != j)
assert [n2(b) for b in Bb] == [117, 117, 9, 585]


def pB(p):
    """squared moduli of p's coordinates in the orthonormal basis b^."""
    return [ip(b, p).abs2() / n2(b) for b in Bb]


def pS(p):
    return [x.abs2() for x in p]


prodsB = [prod_vec(V(a, b), V(c, e)) for a, b, c, e in itertools.product([1, 2, I_, G(1, 1)], [1, 3, -1], [1, 2, I_], [1, -3, G(2, 1)])]
prodsS = [[a * s_ for a in (a0, a1) for s_ in (sp_, sm)] for a0, a1, sp_, sm in
          itertools.product([1, 2, I_], [1, 3, -1], [1, 2, G(1, 1)], [1, -3, I_])]
prodsS = [V(*p) for p in prodsS]


def refute(cent, prods, coords):
    bad = []
    for t in cent:
        if t == (0, 1, 2, 3):
            continue
        hit = False
        for p in prods:
            q = coords(p)
            if any(x == 0 for x in q):
                continue
            if any(q[t[j]] * q[t[k]] < q[j] * q[k] for j in range(4) for k in range(4) if j != k):
                hit = True
                break
        if not hit:
            bad.append(t)
    return bad


centB = centralizer([PI_B[1], PI_B[2]])
centS = centralizer([(1, 0, 3, 2)])
unrefB = refute(centB, prodsB, pB)
unrefS = refute(centS, prodsS, pS)
report("A3-perm", unrefB == [] and unrefS == [] and len(centB) == 8 and len(centS) == 8,
       f"centralizers of order {len(centB)} (case B) and {len(centS)} (S2); permutations not refuted by a "
       f"full-support product: {unrefB + unrefS}")

# A3-schur: a non-coboundary multiplier destroys positivity at a full-support product; a coboundary keeps it
def schur_image_scaled(M, p, basis=None):
    if basis is None:
        z = list(p)
    else:
        z = [ip(b, p) for b in basis]          # <b_k|p> = |b_k| x_k : congruence by diag(|b_k|)
    return [[z[i] * M[i][j].conj() * z[j].conj() for j in range(4)] for i in range(4)]


def det3(A, idx):
    a = [[A[i][j] for j in idx] for i in idx]
    return (a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1]) - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
            + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0]))


Mbad = [[G(1) for _ in range(4)] for _ in range(4)]
Mbad[0][1] = Mbad[1][0] = G(-1)
vcob = V(1, I_, -1, G(F(3, 5), F(4, 5)))
Mgood = [[vcob[i] * vcob[j].conj() for j in range(4)] for i in range(4)]
pfull = prod_vec(V(1, 2), V(1, -3))
XbB = schur_image_scaled(Mbad, pfull, Bb)
XgB = schur_image_scaled(Mgood, pfull, Bb)
pfullS = V(*[a * s_ for a in (G(1), G(2)) for s_ in (G(1), G(-3))])
XbS = schur_image_scaled(Mbad, pfullS)
XgS = schur_image_scaled(Mgood, pfullS)
dbB, dbS = det3(XbB, (0, 1, 2)), det3(XbS, (0, 1, 2))
# coboundary: X = w w† with w_i = z_i conj(v_i)
def is_rank_one_psd(X, z, v):
    w = [z[i] * v[i].conj() for i in range(4)]
    return all(X[i][j] == w[i] * w[j].conj() for i in range(4) for j in range(4))


zB = [ip(b, pfull) for b in Bb]
report("A3-schur", dbB.re < 0 and dbB.im == 0 and dbS.re < 0 and dbS.im == 0
       and is_rank_one_psd(XgB, zB, vcob) and is_rank_one_psd(XgS, list(pfullS), vcob),
       f"M_12 = -1: 3x3 principal minor {dbB} (case B, scaled) and {dbS} (S2) < 0; coboundary multiplier: image = w w† "
       f"(PSD) in both")

# A3-slice: every eigenline projector is the image of a product under the group (definitional for g', B)
cnot = lambda v: [v[0], v[1], v[3], v[2]]
okslice = (cnot(b1) == b2) and (b3 == prod_vec(V(1, 0), V(G(1, 2), 2))) and \
          (b1 == prod_vec(V(2, 3), V(2, G(-1, 2))))
report("A3-slice", okslice,
       "b1 = (2,3)(x)(2,-1+2i) and b3 = |0>(x)(1+2i,2) products, b2 = CNOT b1; b4 = g' b3 by definition of g'; "
       "B is a product basis: every eigenline projector lies in G.SEP, so every invariant self-dual cone with H1 "
       "has slice R^4_+")

n_ok = sum(results)
print(f"CHECKS {n_ok}/{len(results)}")
print("VERDICT C18-EXACT" if n_ok == len(results) else "VERDICT C18-FAIL")
