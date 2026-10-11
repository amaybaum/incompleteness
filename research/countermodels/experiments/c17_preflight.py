"""C17 preflight — exact checks of the algebra the design module `OIBridge/CmSprime.lean` relies on.

Node C17 (round 4, research/countermodels). S0 (predictions and decision rule) in NOTES-C17, written
2026-10-11T04:28Z (`date -u`) before this script was first run.

Checks (each with a control):
  P1  the polynomial identity behind `capcocap_real` with the module's `linear_combination` certificate;
      countercontrol: the certificate without its second term leaves a nonzero remainder.
  P2  `qf_defect`: v†(I − c h h†)v = |v|² − c|⟨h|v⟩|²; countercontrol: h hᵀ in place of h h†.
  P3  `pr_one_defect`, `pr_defect_defect` for unit h, h′; countercontrol: a non-unit h.
  P4  the residual vector of `bessel_two`; countercontrol: non-orthogonal u, x.
  P5  open cap ⊆ open co-cap at the (CC) threshold (c = 5/4, c′ = 10/9, s = s* = 1/2);
      countercontrol: s = 1/3 < s* has a witness.
  P6  `capcocap_real` as stated (no sign condition on b), on an exact rational grid;
      countercontrol: (CC) violated, a grid instance violates the conclusion.
  P7  the hypotheses of `control_single_defect`; countercontrol: c = 5 makes tr d < 0.

Exact arithmetic only (sympy for P1, Fractions / Gaussian rationals elsewhere). Deterministic.
Decision rule (NOTES-C17 S0): VERDICT C17-PREFLIGHT-OK iff all seven checks give the predicted outcome,
countercontrols included.
"""
from fractions import Fraction as F
import itertools
import sympy as sp


# ---------- Gaussian rationals ----------
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

    def conj(self):
        return G(self.re, -self.im)

    def abs2(self):
        return self.re * self.re + self.im * self.im

    def __eq__(self, o):
        o = o if isinstance(o, G) else G(o)
        return self.re == o.re and self.im == o.im

    def __repr__(self):
        return f"({self.re}{'+' if self.im >= 0 else '-'}{abs(self.im)}i)"


def vec(*entries):
    return [e if isinstance(e, G) else G(*e) if isinstance(e, tuple) else G(e) for e in entries]


def ip(a, b):
    """⟨a|b⟩ = a† b = Σ conj(a_i) b_i (the module's `ip a b = star a ⬝ᵥ b`)."""
    s = G(0)
    for x, y in zip(a, b):
        s = s + x.conj() * y
    return s


def norm2(a):
    return ip(a, a).re


def smul(c, a):
    return [c * x for x in a]


def vsub(a, b):
    return [x - y for x, y in zip(a, b)]


def defect_matrix(c, h, conj=True):
    n = len(h)
    return [[G(1 if i == j else 0) - G(c) * h[i] * (h[j].conj() if conj else h[j]) for j in range(n)]
            for i in range(n)]


def matvec(M, v):
    return [sum((M[i][j] * v[j] for j in range(len(v))), G(0)) for i in range(len(M))]


def matmul(A, B):
    n = len(A)
    return [[sum((A[i][k] * B[k][j] for k in range(n)), G(0)) for j in range(n)] for i in range(n)]


def trace(M):
    return sum((M[i][i] for i in range(len(M))), G(0))


results = []


def report(name, ok, detail):
    results.append(ok)
    print(f"{name}  {'PASS' if ok else 'FAIL'}  {detail}")


# ---------- P1: the identity of capcocap_real ----------
K, Kp, R, Rp, A_, G_, p = sp.symbols("K Kp R Rp A G p")
lhs = K**2 * ((Kp * A_ * G_ - Rp * p)**2 - Kp**2 * (1 - G_**2) * (p**2 - A_**2))
rhs = (Kp * (K * A_ - p) * (K * Kp * A_ + Kp * p - 2 * K * Rp * p * G_)
       + p**2 * (K * Kp * G_ - R - Rp) * (K * Kp * G_ + R - Rp))
e5 = K**2 - (1 + R**2)
e6 = Kp**2 - (1 + Rp**2)
q1 = -p**2 * (Kp**2 - Rp**2)
q2 = -R**2 * p**2
rem = sp.expand(lhs - rhs - (q1 * e5 + q2 * e6))
rem_cc = sp.expand(lhs - rhs - q1 * e5)
report("P1", rem == 0 and rem_cc != 0,
       f"remainder {rem}; countercontrol (q2 dropped) remainder has {len(sp.Add.make_args(rem_cc))} terms")

# ---------- P2: qf_defect ----------
inst2 = [
    (F(7, 5), vec((1, 2), (0, -1), (3, 0), (-1, 1)), vec((2, 0), (1, 1), (0, -3), (1, 0))),
    (F(3, 2), vec((F(3, 5), 0), (0, F(4, 5)), 0, 0), vec((1, -1), (2, 3), (0, 1), (-2, 0))),
    (F(2), vec((1, 1), (1, -1), (0, 1), (1, 0)), vec((0, 1), (1, 0), (-1, -1), (2, 2))),
]
ok2 = True
cc2_breaks = 0
for c, h, v in inst2:
    M = defect_matrix(c, h)
    q = ip(v, matvec(M, v))
    formula = G(norm2(v) - c * ip(h, v).abs2())
    ok2 = ok2 and q == formula
    Mt = defect_matrix(c, h, conj=False)
    qt = ip(v, matvec(Mt, v))
    if not qt == formula:
        cc2_breaks += 1
report("P2", ok2 and cc2_breaks >= 1,
       f"identity on {len(inst2)} instances: {ok2}; countercontrol h hT breaks it on {cc2_breaks}/{len(inst2)}")

# ---------- P3: pr_one_defect, pr_defect_defect ----------
h_a = vec((F(3, 5), 0), (0, F(4, 5)), 0, 0)
h_b = vec((F(1, 2), 0), (F(1, 2), 0), (F(1, 2), 0), (0, F(1, 2)))
h_c = vec((F(2, 3), 0), (0, F(2, 3)), (F(1, 3), 0), 0)
units = [h_a, h_b, h_c]
assert all(norm2(h) == 1 for h in units)
ok3 = True
for (h1, h2), (c1, c2) in itertools.product(itertools.combinations(units, 2),
                                            [(F(5, 4), F(10, 9)), (F(2), F(3, 2)), (F(101, 100), F(2))]):
    D1, D2 = defect_matrix(c1, h1), defect_matrix(c2, h2)
    ok3 = ok3 and trace(D1) == G(4 - c1)
    ok3 = ok3 and trace(matmul(D1, D2)) == G(4 - c1 - c2 + c1 * c2 * ip(h1, h2).abs2())
h_big = smul(G(2), h_a)
D1, D2 = defect_matrix(F(5, 4), h_big), defect_matrix(F(10, 9), h_b)
cc3 = not trace(matmul(D1, D2)) == G(4 - F(5, 4) - F(10, 9) + F(5, 4) * F(10, 9) * ip(h_big, h_b).abs2())
report("P3", ok3 and cc3, f"trace formulas on 9 pairs: {ok3}; countercontrol non-unit h breaks the pairing: {cc3}")

# ---------- P4: the residual of bessel_two ----------
inst4 = [
    (vec(1, (0, 1), 0, 0), vec((0, 1), 1, 1, 0), vec(2, (1, -1), 3, (0, 1))),
    (vec(1, 1, 1, 1), vec(1, -1, (0, 1), (0, -1)), vec((1, 2), 0, (-3, 1), (2, 0))),
]
ok4 = True
for u, x, h in inst4:
    assert ip(u, x) == G(0)
    U, X, H = norm2(u), norm2(x), norm2(h)
    a, b = ip(u, h), ip(x, h)
    w = vsub(vsub(smul(G(U * X), h), smul(G(X) * a, u)), smul(G(U) * b, x))
    ok4 = ok4 and ip(w, u) == G(0) and ip(w, x) == G(0)
    ok4 = ok4 and ip(w, h) == G(U * X * H - X * a.abs2() - U * b.abs2())
    ok4 = ok4 and ip(w, w) == G(U * X) * ip(w, h)
    ok4 = ok4 and a.abs2() * X + b.abs2() * U <= H * U * X
u, xx, h = vec(1, (0, 1), 0, 0), vec(1, 1, 0, 0), vec(2, (1, -1), 3, (0, 1))
U, X = norm2(u), norm2(xx)
a, b = ip(u, h), ip(xx, h)
w = vsub(vsub(smul(G(U * X), h), smul(G(X) * a, u)), smul(G(U) * b, xx))
cc4 = not ip(w, u) == G(0)
report("P4", ok4 and cc4, f"residual identities and Bessel on {len(inst4)} instances: {ok4}; "
       f"countercontrol non-orthogonal u, x gives <w|u> = {ip(w, u)}")


# ---------- P5: open cap inside open co-cap at the threshold ----------
def in_cap(c, h, v):
    return norm2(v) * norm2(h) < c * ip(h, v).abs2()


def in_cocap(c, h, v):
    return (c - 1) * norm2(v) * norm2(h) < c * ip(h, v).abs2()


c5, c5p = F(5, 4), F(10, 9)
h5 = vec(1, 0, 0, 0)
h5p = vec(1, 1, 0, 0)
h5pp = vec(1, 1, 1, 0)
thr = (F(1, 2) + F(1, 3)) ** 2
assert thr == c5 * c5p * ip(h5, h5p).abs2() / (norm2(h5) * norm2(h5p))          # equality in (CC)
assert thr > c5 * c5p * ip(h5, h5pp).abs2() / (norm2(h5) * norm2(h5pp))         # (CC) violated
points = []
for t in itertools.product(range(-6, 7), repeat=4):
    if any(t):
        points.append(vec(*t))
for t in itertools.product(range(-2, 3), range(-2, 3), range(-2, 3), range(-2, 3), range(-1, 2), range(-1, 2)):
    if any(t):
        points.append(vec((t[0], t[1]), (t[2], t[3]), (t[4], 0), (0, t[5])))
for k in range(0, 500):
    points.append(vec(1000, -k, 0, 0))
    points.append(vec(1000, -k, 1, 0))
    points.append(vec(1000, (-k, 3), 0, (0, 2)))
ncap = 0
viol = 0
wit = 0
witness = None
for v in points:
    if in_cap(c5, h5, v):
        ncap += 1
        if not in_cocap(c5p, h5p, v):
            viol += 1
        if not in_cocap(c5p, h5pp, v):
            wit += 1
            if witness is None:
                witness = v
explicit = vec(3, -1, -1, 0)
explicit_ok = in_cap(c5, h5, explicit) and not in_cocap(c5p, h5pp, explicit)
report("P5", viol == 0 and wit >= 1 and explicit_ok and ncap > 1000,
       f"{len(points)} points, {ncap} in the cap; violations at s = s*: {viol}; "
       f"countercontrol s = 1/3: {wit} witnesses (first {witness}), explicit (3,-1,-1,0): {explicit_ok}")

# ---------- P6: capcocap_real as stated ----------
rs = [F(1, 5), F(1, 3), F(1, 2), F(3, 4), F(1)]
Gs = [F(k, 10) for k in range(0, 11)]
As = [F(1, 2), F(1), F(3, 2), F(2)]
Vs = [F(k, 4) for k in range(1, 21)]
bs = [F(k, 4) for k in range(-12, 13)]
checked = 0
counter = 0
cc_found = None
for r, rp in itertools.product(rs, rs):
    c, cp = 1 + r * r, 1 + rp * rp
    for g in Gs:
        cc_holds = (r + rp) ** 2 <= c * cp * g * g
        for a in As:
            for V in Vs:
                if not V < c * a * a:
                    continue
                for b in bs:
                    if not (b - a * g) ** 2 <= (1 - g * g) * (V - a * a):
                        continue
                    concl = (cp - 1) * V < cp * b * b
                    if cc_holds:
                        checked += 1
                        if not concl:
                            counter += 1
                    elif not concl and cc_found is None:
                        cc_found = (r, rp, g, a, V, b)
report("P6", checked > 1000 and counter == 0 and cc_found is not None,
       f"{checked} instances with (CC): {counter} counterexamples; countercontrol (CC violated) instance "
       f"(r, r', G, A, V, b) = {tuple(str(z) for z in cc_found) if cc_found else None}")

# ---------- P7: the control's hypotheses ----------
e0 = vec(1, 0, 0, 0)
D = defect_matrix(F(3, 2), e0)
diag_ok = all(D[i][j] == G(0) for i in range(4) for j in range(4) if i != j)
eig = [D[i][i].re for i in range(4)]
tr_ok = trace(D) == G(F(5, 2))
D5 = defect_matrix(F(5), e0)
cc7 = trace(D5) == G(-1)
report("P7", diag_ok and eig == [F(-1, 2), 1, 1, 1] and tr_ok and cc7,
       f"eigenvalues {[str(e) for e in eig]}, trace {trace(D)}; countercontrol c = 5: trace {trace(D5)}")

n_ok = sum(results)
print(f"CHECKS {n_ok}/{len(results)}")
print("VERDICT C17-PREFLIGHT-OK" if n_ok == len(results) else "VERDICT C17-PREFLIGHT-FAIL")
