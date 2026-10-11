"""C23 — the 2-torus group of the tower's closure: the obstruction to explicit surgery cones, with a certificate.

Node C23 (round 5, research/countermodels). S0 (design, decision rules, predictions) in NOTES-C23, revised and fixed
2026-10-11T10:32Z (`date -u`) before this script was first run. Exact arithmetic only: Fractions and Gaussian rationals;
sympy for the symbolic identities. Deterministic. Writes the certificate `c23_certificate.json` (read by the independent
checker `c23_check.py`, which reads nothing else).

Group (NOTES-C23): G_T = T^2 x| V4 modulo phase, D(u, v) = diag(1, uv, u, v), CNOT = (2 3), X_B = (0 1)(2 3).
Checks:
  G1  group structure (symbolic) and V4; countercontrol: 1 (x) (3-4-5 rotation) is not monomial.
  G2  Lemma C23-1: the identity <h|D(u,v) X_B h> = beta + uv conj(beta) + u alpha + v conj(alpha) (symbolic), the modulus
      identity |beta + u alpha| = |conj(alpha) + u conj(beta)| on |u| = 1 (symbolic), exact instances of classes (i)-(v);
      countercontrol: a wrong v.
  G3  Theorem C23-2 (a): C18-1's witness on the orbit of largest c with 200 exact sample defects; countercontrol: the
      witness built with the smaller c.
  G4  Theorem C23-2 (b)-(c): the determinant identity; stage 4's K_T pair transported to the computational basis and
      re-verified; the mixture instance; countercontrol: a Bell projector outside L1'*.
  G5  Theorem C23-3: the r = 3 rank instance, the r = 2 partners with zero pairing and tightness instances at c = 3/2 and
      c = 101/100, the product-in-orbit instances; countercontrols as in S0.
  G6  the certificate file.
Decision rule (NOTES-C23 S0): VERDICT C23-EXACT iff G1-G6 give the predicted outcomes, countercontrols included.
Pre-run edits (before the first run): dead code removed (an unused helper and an unused line), a redundant special
case for class (iii) removed (the general partner formula covers it), a no-op sum in G4 simplified; no check changed.
Run from experiments/:  python3 -I -B c23_torus.py > c23_torus.out 2> c23_torus.err
"""
from fractions import Fraction as F
import itertools
import json
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

    def inv(self):
        a = self.abs2()
        return G(self.re / a, -self.im / a)

    def __truediv__(self, o):
        o = o if isinstance(o, G) else G(o)
        return self * o.inv()

    def __eq__(self, o):
        o = o if isinstance(o, G) else G(o)
        return self.re == o.re and self.im == o.im

    def iszero(self):
        return self.re == 0 and self.im == 0

    def js(self):
        return [str(self.re), str(self.im)]

    def __repr__(self):
        return f"({self.re}{'+' if self.im >= 0 else '-'}{abs(self.im)}i)"


I_ = G(0, 1)


def vec(*e):
    return [x if isinstance(x, G) else G(*x) if isinstance(x, tuple) else G(x) for x in e]


def ip(a, b):
    s = G(0)
    for x, y in zip(a, b):
        s = s + x.conj() * y
    return s


def n2(a):
    return ip(a, a).re


def mv(M, v):
    return [sum((M[i][j] * v[j] for j in range(4)), G(0)) for i in range(4)]


def mm(A, B):
    return [[sum((A[i][k] * B[k][j] for k in range(4)), G(0)) for j in range(4)] for i in range(4)]


def dag(A):
    return [[A[j][i].conj() for j in range(4)] for i in range(4)]


def eye():
    return [[G(1 if i == j else 0) for j in range(4)] for i in range(4)]


def msub(A, B):
    return [[A[i][j] - B[i][j] for j in range(4)] for i in range(4)]


def madd(A, B):
    return [[A[i][j] + B[i][j] for j in range(4)] for i in range(4)]


def msc(c, A):
    c = c if isinstance(c, G) else G(c)
    return [[c * A[i][j] for j in range(4)] for i in range(4)]


def tr(A):
    return sum((A[i][i] for i in range(4)), G(0))


def pr(A, B):
    return tr(mm(A, B)).re


def outer(v, w):
    return [[v[i] * w[j].conj() for j in range(4)] for i in range(4)]


def proj(v):
    return msc(G(F(1) / n2(v)), outer(v, v))


def defect(c, v):
    return msub(eye(), msc(G(c), proj(v)))


def qf(M, x):
    return ip(x, mv(M, x)).re


def detpsi(v):
    return v[0] * v[3] - v[1] * v[2]


def diag(*d):
    M = [[G(0)] * 4 for _ in range(4)]
    for i in range(4):
        M[i][i] = d[i] if isinstance(d[i], G) else G(d[i])
    return M


def perm(p):  # matrix sending e_j to e_{p[j]}
    M = [[G(0)] * 4 for _ in range(4)]
    for j in range(4):
        M[p[j]][j] = G(1)
    return M


def Dm(u, v):
    return diag(G(1), u * v, u, v)


def pyth(t):
    t = F(t)
    d = 1 + t * t
    return G((1 - t * t) / d, 2 * t / d)


CNOT = perm([0, 1, 3, 2])
XB = perm([1, 0, 3, 2])
IDm = eye()
V4 = {"e": IDm, "CNOT": CNOT, "XB": XB, "XBCNOT": mm(XB, CNOT)}


def mjs(M):
    return [[x.js() for x in row] for row in M]


def vjs(v):
    return [x.js() for x in v]


def meq(A, B):
    return all(A[i][j] == B[i][j] for i in range(4) for j in range(4))


results = []


def report(name, ok, detail):
    results.append(ok)
    print(f"{name}  {'PASS' if ok else 'FAIL'}  {detail}")


cert = {"meta": {"node": "C23", "thread": "research/countermodels", "round": 5,
                 "conventions": "computational basis |00>,|01>,|10>,|11> (control first, indices 0..3); complex numbers "
                                "as [re, im] with re, im exact rationals 'p/q'; matrices row-major; P_v = v v^dagger/|v|^2; "
                                "defect(c, v) = I - c P_v; pr(A, B) = Re tr(A B); G_T = T^2 x| V4 modulo phase with "
                                "T^2 = {diag(1, uv, u, v)} and V4 = permutations {e, (23), (01)(23), (01)}",
                 "claims": "C23-1 universal orthogonal pair; C23-2 rank-one route closed (c < 2; Bell corner; mixtures under "
                           "the overlap condition); C23-3 balanced route: the engine's local condition fails"}}

# ---------------- G1 ----------------
u, v, w = sp.symbols("u v w", nonzero=True)


def Ds(a, b):
    return sp.diag(1, a * b, a, b)


Ps = lambda p: sp.Matrix(4, 4, lambda i, j: 1 if p[j] == i else 0)
CN, XBs = Ps([0, 1, 3, 2]), Ps([1, 0, 3, 2])
RB = sp.kronecker_product(sp.eye(2), sp.diag(1, w))
ok1 = sp.simplify(RB - Ds(1, w)) == sp.zeros(4)
ok1 &= sp.simplify(CN * RB * CN - Ds(w, 1)) == sp.zeros(4)
ok1 &= sp.simplify(CN * Ds(u, v) * CN - Ds(v, u)) == sp.zeros(4)
ok1 &= sp.simplify(XBs * Ds(u, v) * XBs - u * v * Ds(1 / u, 1 / v)) == sp.zeros(4)
grp = {tuple(map(tuple, sp.eye(4).tolist()))}
frontier = [sp.eye(4)]
while frontier:
    nxt = []
    for M in frontier:
        for g in (CN, XBs):
            P = g * M
            key = tuple(map(tuple, P.tolist()))
            if key not in grp:
                grp.add(key)
                nxt.append(P)
    frontier = nxt
perms_found = sorted(tuple(int(next(i for i in range(4) if M[i][j] == 1)) for j in range(4)) for M in grp)
ok1 &= perms_found == sorted([(0, 1, 2, 3), (0, 1, 3, 2), (1, 0, 3, 2), (1, 0, 2, 3)])
R345 = sp.kronecker_product(sp.eye(2), sp.Matrix([[sp.Rational(3, 5), -sp.Rational(4, 5)], [sp.Rational(4, 5), sp.Rational(3, 5)]]))
cc1 = any(sum(1 for j in range(4) if R345[i, j] != 0) > 1 for i in range(4))
report("G1", ok1 and cc1, f"R_B(t) = D(1, w), CNOT R_B CNOT = D(w, 1), CNOT D(u,v) CNOT = D(v,u), X_B D(u,v) X_B = uv D(1/u,1/v): "
       f"{ok1}; <CNOT, X_B> = V4 with permutations {perms_found}; countercontrol 1 (x) R_345 not monomial: {cc1}")

# ---------------- G2: Lemma C23-1 ----------------
a = sp.symbols("a0:4", real=True)
b = sp.symbols("b0:4", real=True)
hs = [a[k] + sp.I * b[k] for k in range(4)]
uu, vv = sp.symbols("uu vv")
gh_s = [hs[1], uu * vv * hs[0], uu * hs[3], vv * hs[2]]  # D(u,v) X_B h
lhs = sum(sp.conjugate(hs[k]) * gh_s[k] for k in range(4))
al_s, be_s = sp.conjugate(hs[2]) * hs[3], sp.conjugate(hs[0]) * hs[1]
rhs = be_s + uu * vv * sp.conjugate(be_s) + uu * al_s + vv * sp.conjugate(al_s)
id1 = sp.expand(lhs - rhs) == 0
tt = sp.symbols("t", real=True)
x1, x2, y1, y2 = sp.symbols("x1 x2 y1 y2", real=True)
alpha, beta = x1 + sp.I * x2, y1 + sp.I * y2
ut = (1 - tt ** 2 + 2 * sp.I * tt) / (1 + tt ** 2)
m1 = (beta + ut * alpha) * sp.conjugate(beta + ut * alpha)
m2 = (sp.conjugate(alpha) + ut * sp.conjugate(beta)) * sp.conjugate(sp.conjugate(alpha) + ut * sp.conjugate(beta))
id2 = sp.simplify(sp.expand(m1 - m2)) == 0


def partner_v(h, uval):
    al, be = h[2].conj() * h[3], h[0].conj() * h[1]
    den = al.conj() + uval * be.conj()
    if den.iszero():
        return None
    return -(be + uval * al) / den


classes = [
    ("i", vec(6, (0, 1), 4, 3), G(1), None),
    ("ii", vec(2, (0, 3), 1, 6), G(1), None),
    ("iii", vec(3, 1, (0, 2), 0), G(1), G(-1)),
    ("iv", vec(3, 0, (0, 2), 1), G(1), G(1)),
    ("v", vec(2, 0, 0, (1, 1)), G(1), G(1)),
]
ok2 = True
c1_items = []
details2 = []
gelems = {}


def addg(name, M):
    gelems[name] = mjs(M)
    return name


for name, h, uval, vval in classes:
    al, be = h[2].conj() * h[3], h[0].conj() * h[1]
    if vval is None:
        vval = partner_v(h, uval)
    assert vval is not None and vval.abs2() == 1
    g = mm(Dm(uval, vval), XB)
    gh = mv(g, h)
    inner = ip(h, gh)
    # gh not proportional to h: some 2x2 minor nonzero
    notprop = any(not (h[i] * gh[j] - h[j] * gh[i]).iszero() for i in range(4) for j in range(4))
    ok2 = ok2 and inner.iszero() and notprop
    gname = addg(f"C23-1:{name}", g)
    c1_items.append({"class": name, "h": vjs(h), "g": gname, "alpha": al.js(), "beta": be.js()})
    details2.append(f"{name}: h = {h}, (u, v) = ({uval}, {vval}), <h|gh> = {inner}")
hii = classes[1][1]
vii = [partner_v(hii, uval) for uval in (I_, G(F(3, 5), F(4, 5)), G(F(5, 13), F(12, 13)))]
ok2 = ok2 and all(x == G(0, -1) for x in vii)
hi = classes[0][1]
cc2 = not ip(hi, mv(mm(Dm(G(1), G(1)), XB), hi)).iszero()
report("G2", id1 and id2 and ok2 and cc2,
       f"identity <h|D X_B h> = beta + uv conj(beta) + u alpha + v conj(alpha) (symbolic): {id1}; modulus identity on |u| = 1 "
       f"(symbolic, rational parametrization): {id2}; instances: {'; '.join(details2)}; class (ii) v(u) = -i at three more u: "
       f"{all(x == G(0, -1) for x in vii)}; countercontrol (i) with v = 1 nonzero: {cc2}")
cert["C23-1"] = {"instances": c1_items}

# ---------------- G3: Theorem C23-2 (a) ----------------
def modulus(x):
    r = sp.sqrt(sp.Rational(x.abs2().numerator, x.abs2().denominator))
    assert r.is_rational
    return F(int(r.p), int(r.q))


def dmin(h):
    """min over the G_T-orbit of |det Psi|^2/|h|^4 = min((|h0h3| - |h1h2|)^2, (|h0h2| - |h1h3|)^2)/|h|^4 (formula [W],
    NOTES-C23 S0 G3; rational moduli here)"""
    m = [modulus(x) for x in h]
    return min((m[0] * m[3] - m[1] * m[2]) ** 2, (m[0] * m[2] - m[1] * m[3]) ** 2) / n2(h) ** 2


def h1_ok(D, c):
    return 1 - 4 * D <= (F(2) / c - 1) ** 2


hstar, cstar = classes[0][1], F(51, 50)
htwo, ctwo = vec(4, (0, 1), 2, 3), F(101, 100)
Dstar, Dtwo = dmin(hstar), dmin(htwo)
lam = (cstar - 1) / (4 - 2 * cstar)
gstar = mm(Dm(G(1), partner_v(hstar, G(1))), XB)
hp = mv(gstar, hstar)
y = madd(proj(hstar), msc(G(lam), defect(cstar, hp)))
dh = defect(cstar, hstar)
tpts = [pyth(t) for t in (0, F(1, 2), 2, F(-1, 3), F(1, 5))]
samples = []
ok3 = True
minpair = None
n_s = 0
for seedname, hseed, cseed in (("star", hstar, cstar), ("two", htwo, ctwo)):
    for (ui, uval), (vi, vval) in itertools.product(enumerate(tpts), enumerate(tpts)):
        for sname, S in V4.items():
            g = mm(Dm(uval, vval), S)
            hl = mv(g, hseed)
            dl = defect(cseed, hl)
            p = pr(y, dl)
            s_hl = ip(hstar, hl).abs2() / (n2(hstar) * n2(hl))
            s_pl = ip(hp, hl).abs2() / (n2(hp) * n2(hl))
            ident = cstar * (1 - s_hl) + (cstar - cseed) * (s_hl + lam) + lam * cstar * cseed * s_pl
            pdh = pr(dl, dh)
            h1 = h1_ok(detpsi(hl).abs2() / n2(hl) ** 2, cseed)
            ok3 = ok3 and p >= 0 and p == ident and pdh > 0 and h1
            minpair = p if minpair is None else min(minpair, p)
            gname = addg(f"C23-2a:{seedname}:{ui}{vi}:{sname}", g)
            samples.append({"seed": seedname, "g": gname})
            n_s += 1
zero_on_dh = pr(y, dh)
neg = qf(y, hp) / n2(hp)
ok3 = ok3 and zero_on_dh == 0 and neg == lam * (1 - cstar) and neg < 0
ok3 = ok3 and h1_ok(Dstar, cstar) and h1_ok(Dtwo, ctwo) and Dstar > 0 and Dtwo > 0
lam2 = (ctwo - 1) / (4 - 2 * ctwo)
y2 = madd(proj(hstar), msc(G(lam2), defect(ctwo, hp)))
cc3v = pr(y2, dh)
cc3 = cc3v < 0
report("G3", ok3 and cc3 and n_s == 200,
       f"c* = {cstar}, c2 = {ctwo}, lambda = {lam}; D_min = {Dstar}, {Dtwo} (H1 at both); <y, d_h> = {zero_on_dh}; "
       f"(gh)^+ y (gh)/|gh|^2 = {neg}; {n_s} samples: pairing >= 0 and = C18-1 identity, <d, d_h> > 0, H1: {ok3}; "
       f"min sample pairing = {minpair}; countercontrol (witness with c2 on the c* orbit) <y2, d_h(c*)> = {cc3v}")
cert["C23-2a"] = {"seed_star": vjs(hstar), "c_star": str(cstar), "seed_two": vjs(htwo), "c_two": str(ctwo),
                  "g_pair": addg("C23-2a:pair", gstar), "lambda": str(lam), "samples": samples,
                  "Dmin_star": str(Dstar), "Dmin_two": str(Dtwo),
                  "countercontrol": {"c_small": str(ctwo), "lambda_small": str(lam2)}}

# ---------------- G4: Bell corner and mixtures ----------------
h0, h1, h2, h3 = sp.symbols("h0:4")
Dh = [h0, u * v * h1, u * h2, v * h3]
id3 = sp.expand(Dh[0] * Dh[3] - Dh[1] * Dh[2] - v * (h0 * h3 - u ** 2 * h1 * h2)) == 0
pi = [0, 3, 1, 2]  # z2e basis (|0+>, |1->, |0->, |1+>) index -> computational index


def transport(Mb):
    M = [[G(0)] * 4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            M[pi[i]][pi[j]] = Mb[i][j]
    return M


def l1p(uval, L):  # computational-basis circle-1' Lorentz element: -u E03 - conj(u) E30 + L (E11 + E22)
    M = [[G(0)] * 4 for _ in range(4)]
    M[0][3], M[3][0], M[1][1], M[2][2] = -uval, -uval.conj(), G(L), G(L)
    return M


c1v, c2v = G(F(1, 5), F(2, 5)), G(F(2, 5), F(-1, 5))
yB = [[G(1), G(1), c1v, G(0)], [G(1), G(1), c2v, G(0)], [c1v.conj(), c2v.conj(), G(1), G(0)], [G(0), G(0), G(0), G(1)]]
yP = transport(yB)
x0, L0 = G(F(31, 50), F(13, 100)), F(7, 17)
u0 = x0 - G(1)
q0P = msub(yP, l1p(u0, L0))
vB = vec(1, (F(-4, 5), F(-3, 5)), (0, F(157, 125)), 0)
vP = [G(0)] * 4
for i in range(4):
    vP[pi[i]] = vB[i]
PP = outer(vP, vP)  # unnormalized, as in z2e
tau = F(17)
zeta = PP[0][3] + (PP[1][1] + G(2 * tau)) * G(F(1, 2))
wP = madd(PP, l1p(zeta, tau))


def principal_minors_nonneg(M):
    for r in range(1, 5):
        for S in itertools.combinations(range(4), r):
            sub = sp.Matrix(r, r, lambda i, j: sp.Rational(M[S[i]][S[j]].re.numerator, M[S[i]][S[j]].re.denominator)
                            + sp.I * sp.Rational(M[S[i]][S[j]].im.numerator, M[S[i]][S[j]].im.denominator))
            dv = sp.simplify(sub.det())
            if sp.im(dv) != 0 or sp.re(dv) < 0:
                return False
    return True


def L1d(Y):
    s = Y[1][1].re + Y[2][2].re
    return s >= 0 and 4 * Y[0][3].abs2() <= s * s


def L2d(Y):
    s = Y[0][0].re + Y[3][3].re
    return s >= 0 and 4 * Y[1][2].abs2() <= s * s


okb = principal_minors_nonneg(q0P) and u0.abs2() <= L0 * L0 and L1d(yP) and L2d(yP)
okb &= principal_minors_nonneg(PP) and zeta.abs2() <= tau * tau and L1d(wP) and L2d(wP)
val = pr(yP, wP)
okb &= val == F(-6, 625)
Hp = [[G(1), G(1)], [G(1), G(-1)]]
IH = [[G(0)] * 4 for _ in range(4)]
for aa in range(2):
    for bb in range(2):
        for b2 in range(2):
            IH[2 * aa + bb][2 * aa + b2] = Hp[bb][b2]
okmap = True
for wv in (G(1), I_, G(F(3, 5), F(4, 5))):
    C1 = [G(1), G(1), wv, -wv]          # |0+> + w|1-> (unnormalized: (1,1,0,0) + w (0,0,1,-1))
    C2 = [G(1), G(-1), wv, wv]          # |0-> + w|1+> (unnormalized: (1,-1,0,0) + w (0,0,1,1))
    i1, i2 = mv(IH, C1), mv(IH, C2)
    t1, t2 = vec(1, 0, 0, wv), vec(0, 1, wv, 0)
    okmap = okmap and all((i1[p] * t1[q] - i1[q] * t1[p]).iszero() for p in range(4) for q in range(4))
    okmap = okmap and all((i2[p] * t2[q] - i2[q] * t2[p]).iszero() for p in range(4) for q in range(4))
# circle-1' defects are l1'(conj(w), 1)
okdef = all(meq(defect(F(2), vec(1, 0, 0, wv)), l1p(wv.conj(), 1)) for wv in (G(1), I_, G(F(3, 5), F(4, 5))))
# mixture instance
hm, cm = vec(3, (0, 2), 2, 1), F(1001, 1000)
Dm_ = dmin(hm)
modsm = [modulus(x) for x in hm]
overl = max((modsm[0] + modsm[3]) ** 2, (modsm[1] + modsm[2]) ** 2) <= n2(hm)
lamm = (cm - 1) / (4 - 2 * cm)
gm = mm(Dm(G(1), partner_v(hm, G(1))), XB)
hpm = mv(gm, hm)
ym = madd(proj(hm), msc(G(lamm), defect(cm, hpm)))
dhm = defect(cm, hm)
bell_ws = [G(1), G(-1), I_, G(0, -1), G(F(3, 5), F(4, 5)), G(F(-3, 5), F(4, 5)), G(F(3, 5), F(-4, 5)), G(F(-3, 5), F(-4, 5))]
bell_samples = [vec(1, 0, 0, wv) for wv in bell_ws] + [vec(0, 1, wv, 0) for wv in bell_ws]
okm = overl and h1_ok(Dm_, cm) and Dm_ > 0 and pr(ym, dhm) == 0 and qf(ym, hpm) < 0
okm &= all(pr(ym, defect(F(2), bb)) >= 0 and pr(defect(F(2), bb), dhm) > 0 for bb in bell_samples)
mix_orbit = []
for (ui, uval), (vi, vval) in itertools.product(enumerate(tpts[:3]), enumerate(tpts[:3])):
    for sname, S in V4.items():
        g = mm(Dm(uval, vval), S)
        dl = defect(cm, mv(g, hm))
        okm = okm and pr(ym, dl) >= 0 and pr(dl, dhm) > 0
        mix_orbit.append(addg(f"C23-2c:{ui}{vi}:{sname}", g))
bellP = proj(vec(1, 0, 0, 1))
cc4 = not L1d(bellP)
report("G4", id3 and okb and okmap and okdef and okm and cc4,
       f"det Psi(D(u,v)h) = v(h0h3 - u^2 h1h2) (symbolic): {id3}; transported K_T pair: q0' PSD, |u0|^2 = {u0.abs2()} <= "
       f"{L0 * L0}, y' and w' in L1'* n L2'*, |zeta|^2 <= tau^2, tr(y'w') = {val}: {okb}; 1 (x) H' maps C1, C2 onto C1', C2' "
       f"(three points): {okmap}; circle-1' defects = l1'(conj w, 1): {okdef}; mixture h = {hm} at c* = {cm}: overlap "
       f"condition {overl}, D_min = {Dm_}, witness >= 0 on 16 Bell defects and 36 orbit samples, < 0 on gh: {okm}; "
       f"countercontrol P_(1,0,0,1) outside L1'*: {cc4}")
cert["C23-2b"] = {"y": mjs(yP), "q0": mjs(q0P), "u0": u0.js(), "L0": str(L0), "w": mjs(wP), "v": vjs(vP),
                  "zeta": zeta.js(), "tau": str(tau), "value_tr_yw": str(val),
                  "IH_unnormalized": mjs(IH), "circle_points": [x.js() for x in (G(1), I_, G(F(3, 5), F(4, 5)))]}
cert["C23-2c"] = {"h": vjs(hm), "c": str(cm), "g_pair": addg("C23-2c:pair", gm), "lambda": str(lamm),
                  "bell_samples": [vjs(bb) for bb in bell_samples], "orbit_samples": mix_orbit, "Dmin": str(Dm_)}

# ---------------- G5: balanced route ----------------
def rank(rows):
    M = [r[:] for r in rows]
    rk, col = 0, 0
    nr, nc = len(M), len(M[0])
    for col in range(nc):
        piv = next((i for i in range(rk, nr) if not M[i][col].iszero()), None)
        if piv is None:
            continue
        M[rk], M[piv] = M[piv], M[rk]
        for i in range(nr):
            if i != rk and not M[i][col].iszero():
                f = M[i][col] / M[rk][col]
                M[i] = [M[i][j] - f * M[rk][j] for j in range(nc)]
        rk += 1
    return rk


def nullspace(rows):
    """basis of {k : sum_j rows[i][j] k_j = 0 for all i} over Q(i)"""
    M = [r[:] for r in rows]
    nr, nc = len(M), len(M[0])
    pivcols = []
    rk = 0
    for col in range(nc):
        piv = next((i for i in range(rk, nr) if not M[i][col].iszero()), None)
        if piv is None:
            continue
        M[rk], M[piv] = M[piv], M[rk]
        pv = M[rk][col]
        M[rk] = [x / pv for x in M[rk]]
        for i in range(nr):
            if i != rk and not M[i][col].iszero():
                f = M[i][col]
                M[i] = [M[i][j] - f * M[rk][j] for j in range(nc)]
        pivcols.append(col)
        rk += 1
    free = [c for c in range(nc) if c not in pivcols]
    basis = []
    for fc in free:
        k = [G(0)] * nc
        k[fc] = G(1)
        for r, pc in enumerate(pivcols):
            k[pc] = -M[r][fc]
        basis.append(k)
    return basis


us = [G(1), I_, G(F(3, 5), F(4, 5)), G(F(5, 13), F(12, 13))]
# (a) r = 3
ha = classes[0][1]
partners_a = []
for uval in us:
    g = mm(Dm(uval, partner_v(ha, uval)), XB)
    partners_a.append((addg(f"C23-3a:{uval}", g), mv(g, ha)))
rows_a = [[x.conj() for x in ph] for _, ph in partners_a]  # k orthogonal to ph: sum conj(ph_j) k_j = 0
rk_a = rank([ph for _, ph in partners_a])
ns_a = nullspace(rows_a)
ns_a_ok = len(ns_a) == 1 and all((ns_a[0][i] * ha[j] - ns_a[0][j] * ha[i]).iszero() for i in range(4) for j in range(4))
ns_a2 = nullspace(rows_a + [[x.conj() for x in ha]])
gbad = mm(Dm(G(1), G(1)), XB)
cc5 = rank([ph for _, ph in partners_a[:3]] + [mv(gbad, ha)]) == 4
ok5a = rk_a == 3 and ns_a_ok and len(ns_a2) == 0
# (b) r = 2 classes
r2 = [("ii", classes[1][1], vec(1, (0, -6), -2, 3)), ("iii", classes[2][1], vec(3, 1, (0, -5), 0)),
      ("iv", classes[3][1], vec(-5, 0, (0, 6), 3))]
tight_params = {
    ("ii", F(3, 2)): (pyth(F(1, 10)), G(0, F(199, 200))),
    ("iii", F(3, 2)): (pyth(F(1, 10)), G(0, F(629, 1000))),
    ("iv", F(3, 2)): (pyth(F(1, 10)), G(F(47, 1000), F(-443, 1000))),
    ("ii", F(101, 100)): (pyth(F(1, 10)), G(0, F(199, 200))),
    ("iii", F(101, 100)): (pyth(F(1, 20)), G(F(242, 1000), F(581, 1000))),
    ("iv", F(101, 100)): (pyth(F(1, 20)), G(F(322, 1000), F(-307, 1000))),
}
ok5b = True
det5b = []
cert_b = []
for name, h, k0pred in r2:
    pts = []
    for uval in us:
        vval = partner_v(h, uval)
        if vval is None:
            continue
        g = mm(Dm(uval, vval), XB)
        if not ip(h, mv(g, h)).iszero():
            continue
        pts.append((g, mv(g, h)))
    rk_b = rank([ph for _, ph in pts])
    rows_b = [[x.conj() for x in ph] for _, ph in pts] + [[x.conj() for x in h]]
    ns_b = nullspace(rows_b)
    k0 = ns_b[0] if len(ns_b) == 1 else None
    prop = k0 is not None and all((k0[i] * k0pred[j] - k0[j] * k0pred[i]).iszero() for i in range(4) for j in range(4))
    k0 = k0pred
    c = F(3, 2)
    d = msub(msub(eye(), msc(G(c), proj(h))), msc(G(2 - c), proj(k0)))
    zero_pairs = all(pr(d, mm(mm(g, d), dag(g))) == 0 for g, _ in pts)
    p = [h[i].conj() * k0[i] for i in range(4)]
    a12_nonzero = not (p[1] + p[2]).iszero()
    tights = []
    tight_ok = True
    for cv in (F(3, 2), F(101, 100)):
        ue, bco = tight_params[(name, cv)]
        dcv = msub(msub(eye(), msc(G(cv), proj(h))), msc(G(2 - cv), proj(k0)))
        U = Dm(ue, G(1))
        dU = mm(mm(U, dcv), dag(U))
        uc = [h[i] + bco * k0[i] for i in range(4)]
        coef = ip(uc, k0) / G(n2(uc))
        x = [k0[i] - coef * uc[i] for i in range(4)]
        q_u, q_x, q_xU, pair = qf(dcv, uc), qf(dcv, x), qf(dU, x), pr(dcv, dU)
        ok_t = q_u < 0 and q_x > 0 and pair > 0 and q_xU < 0 and ip(uc, x).iszero()
        tight_ok = tight_ok and ok_t
        tights.append({"c": str(cv), "U": addg(f"C23-3b:{name}:{cv}", U), "b": bco.js(), "u_cap": vjs(uc), "x": vjs(x)})
        det5b.append(f"{name} c={cv}: u'du = {float(q_u):.6f}, x'dx = {float(q_x):.6f}, x'(UdU+)x = {q_xU} "
                     f"({float(q_xU / n2(x)):.6f} normalized), <d,UdU+> = {float(pair):.4f}")
    okc = rk_b == 2 and len(ns_b) == 1 and prop and zero_pairs and a12_nonzero and tight_ok
    ok5b = ok5b and okc
    cert_b.append({"class": name, "h": vjs(h), "k0": vjs(k0), "partners_g": [addg(f"C23-3b:{name}:partner{j}", g)
                                                                          for j, (g, _) in enumerate(pts)],
                   "zero_pairing_c": str(F(3, 2)), "tight": tights})
    det5b.append(f"{name}: rank {rk_b}, partner unique and = {k0pred}: {len(ns_b) == 1 and prop}, zero pairing on "
                 f"{len(pts)} partners: {zero_pairs}, p1 + p2 = {p[1] + p[2]}")
# (c) two vanishing coordinates
c_insts = [vec(2, 0, 0, (1, 1)), vec(0, 2, (1, 1), 0)]
ok5c = all(detpsi(mv(CNOT, hh)).iszero() for hh in c_insts)
report("G5", ok5a and cc5 and ok5b and ok5c,
       f"(a) h = {ha}: partners rank {rk_a}, nullspace of k-perp-partners = C h: {ns_a_ok}, with k-perp-h: dim {len(ns_a2)}; "
       f"countercontrol (one non-orthogonalizing image) rank 4: {cc5}; (b) {'; '.join(det5b)}; (c) CNOT-images of "
       f"(2,0,0,1+i), (0,2,1+i,0) are products: {ok5c}")
cert["C23-3a"] = {"h": vjs(ha), "partners_g": [nm for nm, _ in partners_a], "countercontrol_g": addg("C23-3a:bad", gbad)}
cert["C23-3b"] = cert_b
cert["C23-3c"] = {"seeds": [vjs(hh) for hh in c_insts], "g": addg("C23-3c:CNOT", CNOT)}

# ---------------- G6: certificate ----------------
cert["group_elements"] = gelems
with open("c23_certificate.json", "w") as fh:
    json.dump(cert, fh, indent=1, sort_keys=True)
with open("c23_certificate.json", "rb") as fh:
    import hashlib
    digest = hashlib.sha256(fh.read()).hexdigest()
report("G6", len(gelems) > 0, f"certificate c23_certificate.json written: {len(gelems)} group elements, sha256 {digest}")

n_ok = sum(results)
print(f"CHECKS {n_ok}/{len(results)}")
print("VERDICT C23-EXACT" if n_ok == len(results) else "VERDICT C23-FAIL")
