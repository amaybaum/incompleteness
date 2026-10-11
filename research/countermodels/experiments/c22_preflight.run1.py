"""C22 preflight — exact checks of the new arguments behind the design module `OIBridge/CmSprimeCompact.lean`
(Theorem S′ for compact defect sets by finite-net approximation).

Node C22 (round 5, research/countermodels). S0 (predictions and decision rule) in NOTES-C22, written
2026-10-11T07:50Z (`date -u`) before this script was first run.

Checks (each with a control):
  Q1  the column identity pr q M = Σ_m qf M (B_m) for q = B B†, and the pairing estimate |pr q M| ≤ ε n tr q
      (ε² = max |M_ij|²); countercontrol: without the factor n the bound fails (q = vv†, v = (1,1,1,1), M = ones).
  Q2  the PSD entry bounds 4|q_ij|² ≤ (q_ii + q_jj)², |q_ij|² ≤ (tr q)²; countercontrol: a non-PSD Hermitian matrix.
  Q3  the defect entry bound |d_ij|² ≤ (1 + c)² for unit seeds; countercontrol: a non-unit seed.
  Q4  the net mechanism on the S2 circle (C13.7: g_w = (3, 3, w, −w), c = 21/20): (a) the finite theorem's hypotheses on
      the net and the off-net points, the symbolic overlap identity |⟨g_w|g_w'⟩|²/400 = |9 + w̄w'|²/100 and its minimum
      16/25; (b) the exact ε² of the net; (c) for pure q = P_v in Q ∩ F*, pr q d_w ≥ −ε n tr q and pr (q + δI) d_w ≥ 0,
      δ = ε n tr(q)/τ, at every off-net w; (d) the shift on a real instance: y = d_{w₀} is in K(Z)* but not in K(F)*
      (exact pure witness in the cap of w₀ outside every net cap), while y + ηI, η = ε n tr(y)/τ, pairs ≥ 0 with that
      witness and with every net defect.
  Q5  Bell-circle countercontrol: at c = 2 two non-antipodal points of a Bell circle pair negatively (the pairing
      hypothesis fails; consistent with C7.6).

Exact arithmetic only (Fractions / Gaussian rationals; sympy for the symbolic identity). Irrational bounds (ε, δ, η
are square roots of rationals) are compared through squares. Deterministic.
Decision rule (NOTES-C22 S0): VERDICT C22-PREFLIGHT-OK iff Q1–Q5 give the predicted outcome, countercontrols included.
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

    def __neg__(self):
        return G(-self.re, -self.im)

    def conj(self):
        return G(self.re, -self.im)

    def abs2(self):
        return self.re * self.re + self.im * self.im

    def __eq__(self, o):
        o = o if isinstance(o, G) else G(o)
        return self.re == o.re and self.im == o.im

    def __repr__(self):
        return f"({self.re}{'+' if self.im >= 0 else '-'}{abs(self.im)}i)"


def g(x):
    return x if isinstance(x, G) else G(*x) if isinstance(x, tuple) else G(x)


def vec(*entries):
    return [g(e) for e in entries]


def ip(a, b):
    """⟨a|b⟩ = Σ conj(a_i) b_i."""
    s = G(0)
    for x, y in zip(a, b):
        s = s + x.conj() * y
    return s


def norm2(a):
    return ip(a, a).re


def matmul(A, B):
    n = len(A)
    return [[sum((A[i][k] * B[k][j] for k in range(n)), G(0)) for j in range(n)] for i in range(n)]


def conjT(A):
    n = len(A)
    return [[A[j][i].conj() for j in range(n)] for i in range(n)]


def madd(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A))] for i in range(len(A))]


def msub(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A))] for i in range(len(A))]


def mscale(c, A):
    return [[g(c) * A[i][j] for j in range(len(A))] for i in range(len(A))]


def ident(n):
    return [[G(1 if i == j else 0) for j in range(n)] for i in range(n)]


def trace(A):
    return sum((A[i][i] for i in range(len(A))), G(0))


def pr(A, B):
    """pr A B = Re tr(A B)."""
    return trace(matmul(A, B)).re


def matvec(M, v):
    return [sum((M[i][j] * v[j] for j in range(len(v))), G(0)) for i in range(len(M))]


def qf(M, v):
    """qf M v = Re(v† M v)."""
    return ip(v, matvec(M, v)).re


def proj(v):
    """vv† / |v|² (a rank-one projector with rational entries when |v|² is rational)."""
    n2 = norm2(v)
    return [[v[i] * v[j].conj() * G(F(1) / n2) for j in range(len(v))] for i in range(len(v))]


def defect(c, v):
    """I − c P_v (v any nonzero vector; P_v = vv†/|v|²)."""
    return msub(ident(len(v)), mscale(c, proj(v)))


def is_hermitian(A):
    return all(A[i][j] == A[j][i].conj() for i in range(len(A)) for j in range(len(A)))


results = []


def report(name, ok, detail):
    results.append(ok)
    print(f"{name}  {'PASS' if ok else 'FAIL'}  {detail}")


N = 4

# ---------- Q1: column identity and pairing estimate ----------
Bs = [
    [vec(1, (0, 1), 2, 0), vec((1, 1), 0, 1, (0, -1)), vec(0, 2, (1, -1), 1), vec((2, 1), 1, 0, (1, 1))],
    [vec(3, 0, 0, 0), vec((1, 2), (0, 1), 0, 0), vec(0, 0, (2, 2), 1), vec(1, 1, 1, (1, 1))],
    [vec(1, 1, 1, 1), vec(1, (0, 1), -1, (0, -1)), vec(0, 0, 0, 0), vec((1, 1), 0, 0, 0)],
]
Ns = [
    [vec((2, 1), (0, 3), 1, (1, 1)), vec(0, 1, (2, -1), 0), vec((1, 0), (0, 1), (0, 2), 3), vec(1, 0, 0, (-1, 1))],
    [vec(5, 0, 0, 0), vec(0, (0, 2), 0, 0), vec(0, 0, 0, (3, 4)), vec(0, 0, 0, 1)],
]
ok1 = True
n_inst = 0
for B in Bs:
    q = matmul(B, conjT(B))                      # PSD
    assert is_hermitian(q)
    for Nm in Ns:
        M = madd(Nm, conjT(Nm))                  # Hermitian
        assert is_hermitian(M)
        cols = [[B[i][m] for i in range(N)] for m in range(N)]
        lhs = pr(q, M)
        rhs = sum(qf(M, col) for col in cols)
        eps2 = max(M[i][j].abs2() for i in range(N) for j in range(N))
        trq = pr(q, ident(N))
        bound_ok = lhs * lhs <= eps2 * N * N * trq * trq
        ok1 = ok1 and lhs == rhs and bound_ok
        n_inst += 1
v1 = vec(1, 1, 1, 1)
q_cc = matmul([[v1[i]] for i in range(N)], [[v1[j].conj() for j in range(N)]])
ones = [[G(1) for _ in range(N)] for _ in range(N)]
cc1_val = pr(q_cc, ones)
cc1 = cc1_val == F(16) and pr(q_cc, ident(N)) == F(4) and not (cc1_val * cc1_val <= 1 * pr(q_cc, ident(N)) ** 2)
report("Q1", ok1 and cc1, f"column identity and |pr q M|² ≤ ε²n²(tr q)² on {n_inst} instances: {ok1}; "
       f"countercontrol: pr q M = {cc1_val} = ε n tr q, and the bound without n fails: {cc1}")

# ---------- Q2: PSD entry bounds ----------
ok2 = True
for B in Bs:
    q = matmul(B, conjT(B))
    trq = pr(q, ident(N))
    for i in range(N):
        for j in range(N):
            a = q[i][j].abs2()
            ok2 = ok2 and 4 * a <= (q[i][i].re + q[j][j].re) ** 2 and a <= trq * trq
X = [[G(0), G(1), G(0), G(0)], [G(1), G(0), G(0), G(0)], [G(0)] * 4, [G(0)] * 4]
cc2 = is_hermitian(X) and not (4 * X[0][1].abs2() <= (X[0][0].re + X[1][1].re) ** 2)
report("Q2", ok2 and cc2, f"4|q_ij|² ≤ (q_ii+q_jj)² and |q_ij|² ≤ (tr q)² on {len(Bs)} PSD instances: {ok2}; "
       f"countercontrol (non-PSD X ⊕ 0 violates the first): {cc2}")

# ---------- Q3: defect entry bound ----------
seeds = [(F(3, 2), vec(3, (0, 4), 0, 0)), (F(2), vec(1, 0, 0, 1)), (F(21, 20), vec(3, 3, 1, -1)),
         (F(101, 100), vec(10, (2, -2), (-1, -3), (3, -1)))]
ok3 = True
for c, v in seeds:
    d = defect(c, v)
    ok3 = ok3 and all(d[i][j].abs2() <= (1 + c) ** 2 for i in range(N) for j in range(N))
vbad = vec(2, 0, 0, 0)
dbad = msub(ident(N), mscale(F(2), [[vbad[i] * vbad[j].conj() for j in range(N)] for i in range(N)]))  # non-unit seed, no normalization
cc3 = dbad[0][0] == G(-7) and not (dbad[0][0].abs2() <= 9)
report("Q3", ok3 and cc3, f"|d_ij|² ≤ (1+c)² on {len(seeds)} unit-seed instances: {ok3}; "
       f"countercontrol non-unit seed: d_00 = {dbad[0][0]}, bound 3 violated: {cc3}")

# ---------- Q4: the net mechanism on the S2 circle ----------
c4 = F(21, 20)
tau = 4 - c4
net = [G(1), G(0, 1), G(-1), G(0, -1), G(F(3, 5), F(4, 5)), G(F(-3, 5), F(4, 5)), G(F(-3, 5), F(-4, 5)),
       G(F(3, 5), F(-4, 5))]
offnet = [G(F(5, 13), F(12, 13)), G(F(-5, 13), F(12, 13)), G(F(8, 17), F(15, 17)), G(F(7, 25), F(24, 25)),
          G(F(-7, 25), F(-24, 25)), G(F(20, 29), F(21, 29)), G(F(15, 17), F(8, 17))]
assert all(w.abs2() == 1 for w in net + offnet)


def gw(w):
    return vec(3, 3, w, -w)


def d_of(w):
    return defect(c4, gw(w))


allw = net + offnet
# (a) finite-theorem hypotheses on all 15 points
ok4a = True
pairs_checked = 0
for w1, w2 in itertools.combinations(allw, 2):
    s = ip(gw(w1), gw(w2)).abs2() / (norm2(gw(w1)) * norm2(gw(w2)))
    pairing = pr(d_of(w1), d_of(w2))
    ok4a = ok4a and pairing == 4 - 2 * c4 + c4 * c4 * s and pairing >= 0 and c4 * c4 * s >= 4 * (c4 - 1)
    ok4a = ok4a and s == (G(9) + w1.conj() * w2).abs2() / 100
    pairs_checked += 1
ok4a = ok4a and all(norm2(gw(w)) == 20 for w in allw)
t = sp.symbols("t", real=True)
z = sp.cos(t) + sp.I * sp.sin(t)
expr = sp.simplify(sp.expand((9 + z) * (9 + sp.conjugate(z))))
ident_ok = sp.simplify(expr - (82 + 18 * sp.cos(t))) == 0
min_ok = sp.Rational(82 - 18, 100) == sp.Rational(16, 25)
report("Q4a", ok4a and ident_ok and min_ok,
       f"{pairs_checked} pairs: pairing formula, pairing ≥ 0, (CC) c²s ≥ 4(c−1) with c = 21/20: {ok4a}; "
       f"symbolic |9 + e^{{it}}|² = 82 + 18 cos t: {ident_ok}; minimum 64/100 = 16/25 (C13-S2's s_min): {min_ok}")


# (b) ε² of the net
def dev2(w, wp):
    D = msub(d_of(w), d_of(wp))
    return max(D[i][j].abs2() for i in range(N) for j in range(N))


eps2 = F(0)
nearest = {}
for w in offnet:
    best = min(((dev2(w, wp), k) for k, wp in enumerate(net)), key=lambda x: x[0])
    nearest[repr(w)] = (best[1], best[0])
    eps2 = max(eps2, best[0])
report("Q4b", eps2 > 0 and eps2 < F(1, 100),
       f"ε² = {eps2} ≈ {float(eps2):.6f} (ε ≈ {float(eps2) ** 0.5:.4f}); nearest net index and deviation² per off-net w: "
       f"{ {k: (v[0], str(v[1])) for k, v in nearest.items()} }")

# (c) pure q = P_v in Q ∩ F*, estimates at every off-net w
vs = [vec(1, 0, 0, 0), vec(1, 1, 1, 1), vec(0, 0, 1, 0), vec(1, 1, 0, 0), vec(306, 204, (75, 40), (-75, -40)),
      vec(1, (0, 1), 2, (1, 1)), vec(3, 3, 0, 5)]


def in_Fstar(v):
    """P_v pairs ≥ 0 with every net defect: |⟨g_w'|v⟩|²/(20|v|²) ≤ 1/c for every w' in the net."""
    return all(ip(gw(wp), v).abs2() * c4 <= 20 * norm2(v) for wp in net)


assert all(in_Fstar(v) for v in vs), [in_Fstar(v) for v in vs]
ok4c = True
n4c = 0
neg_seen = 0
for v in vs:
    q = proj(v)
    trq = pr(q, ident(N))
    assert trq == 1
    for w in offnet:
        p = pr(q, d_of(w))
        if p < 0:
            neg_seen += 1
            ok4c = ok4c and p * p <= eps2 * N * N * trq * trq          # pr q d_w ≥ −ε n tr q
            trd = pr(ident(N), d_of(w))
            delta2 = eps2 * N * N * trq * trq / (tau * tau)
            ok4c = ok4c and delta2 * trd * trd >= p * p                 # pr (q + δI) d_w ≥ 0
        n4c += 1
report("Q4c", ok4c and neg_seen >= 1,
       f"{n4c} (q, w) instances: pr q d_w ≥ −ε n tr q and pr (q + δI) d_w ≥ 0 (δ = ε n tr q/τ): {ok4c}; "
       f"instances with pr q d_w < 0 (where the estimate is load-bearing): {neg_seen}")

# (d) the shift on a real instance
w0 = G(F(15, 17), F(8, 17))
y = d_of(w0)
vwit = vec(306, 204, (75, 40), (-75, -40))
cap_w0 = ip(gw(w0), vwit).abs2() * c4 > 20 * norm2(vwit)              # open cap of w0
outside_net = in_Fstar(vwit)                                          # outside every closed net cap... (≤ 1/c)
p_y = pr(y, proj(vwit))
ok4d1 = cap_w0 and outside_net and p_y < 0                            # y ∉ K(F)*
y_in_Zstar = all(pr(y, d_of(w)) >= 0 for w in allw)                   # y ∈ Z* on the sampled points
try_ = pr(ident(N), y)
eta2 = eps2 * N * N * try_ * try_ / (tau * tau)                       # η = ε n tr(y)/τ  (= 4ε here)
ok4d2 = eta2 >= p_y * p_y and all(pr(y, d_of(wp)) >= 0 for wp in net)  # (y + ηI) pairs ≥ 0 with P_v and with net defects
# also with every sampled P_v in Q ∩ F*
ok4d3 = all((lambda p: p >= 0 or eta2 >= p * p)(pr(y, proj(v))) for v in vs)
report("Q4d", ok4d1 and y_in_Zstar and ok4d2 and ok4d3,
       f"w0 = {w0}: witness v in the open cap of w0 ({cap_w0}) and in F* ({outside_net}), pr y P_v = {p_y} < 0 "
       f"so y = d_w0 ∉ K(F)*; y ∈ Z* on all 15 points: {y_in_Zstar}; η² = {eta2} ≥ (pr y P_v)² = {p_y * p_y}: {ok4d2}; "
       f"y + ηI pairs ≥ 0 with every sampled P_v: {ok4d3}")

# ---------- Q5: Bell-circle countercontrol ----------
cB = F(2)
bell = lambda w: vec(1, 0, 0, w)                                      # |00⟩ + w|11⟩
pB = pr(defect(cB, bell(G(1))), defect(cB, bell(G(0, 1))))
sB = ip(bell(G(1)), bell(G(0, 1))).abs2() / 4
anti = pr(defect(cB, bell(G(1))), defect(cB, bell(G(-1))))
report("Q5", pB == 4 * sB - 4 and pB < 0 and anti == 0,
       f"Bell circle at c = 2: pairing(1, i) = {pB} = 4s − 4 with s = {sB} (negative: hypothesis fails); "
       f"antipodal pairing = {anti} (orthogonal, admissible)")

n_ok = sum(results)
print(f"CHECKS {n_ok}/{len(results)}")
print("VERDICT C22-PREFLIGHT-OK" if n_ok == len(results) else "VERDICT C22-PREFLIGHT-FAIL")
