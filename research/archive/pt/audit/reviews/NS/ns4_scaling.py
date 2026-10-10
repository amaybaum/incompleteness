#!/usr/bin/env python3
"""ns4_scaling.py -- thread NS, question NS.4 (exact: sympy with exact symbols and rationals, stdlib Fractions).

OBJECT. The input's kinematic family u_eps(x) = eps^(-3/2) f((x - x0)/eps) on R^3 (NS-INPUT L80-94), with the
concrete smooth divergence-free profile f = curl(0, 0, G), G = exp(-|y|^2), i.e. f = (-2 y2 G, 2 y1 G, 0);
eps > 0 and x0 = (a, b, c) symbolic.

CHECKS (each prints PASS or FAIL):
  S0  div f = 0 identically.
  S1  div u_eps = 0 identically (divergence-free preserved), symbolic eps, x0.
  S2  ||u_eps||_2^2 = ||f||_2^2 for symbolic eps > 0 (integral over R^3 computed by sympy at x0 = 0; the
      translation x0 is handled by S2t at a rational shift).
  S2t the same with x0 = (1/3, -2, 5/7).
  S3  sup|f| = sqrt(2/e), attained at y* = (1/sqrt 2, 0, 0) (stationarity and second-order check of
      g(r) = 4 r exp(-2r), r = y1^2 + y2^2 at y3 = 0, plus |f|^2 <= g(r)); hence ||u_eps||_inf = eps^(-3/2) sqrt(2/e),
      evaluated exactly at x = x0 + eps y*.
  S4  ||u_eps||_inf -> oo as eps -> 0+, while S2 holds: energy constant, peak divergent.
  S5  enstrophy ||grad u_eps||_2^2 = eps^(-2) ||grad f||_2^2 (x0 = 0).
  S6  NS scaling: u_lam(x,t) = lam u(lam x, lam^2 t), p_lam = lam^2 p(lam x, lam^2 t) maps NS residuals to
      lam^3 times NS residuals (each of the four terms checked exactly on two concrete smooth test pairs (u, p);
      the general statement is the chain rule [W]); and ||lam f(lam x)||_2^2 = ||f||_2^2 / lam for the profile f.
  CC1 wrong exponent: eps^(-1) f((x-x0)/eps) has ||.||_2^2 = eps ||f||_2^2 != ||f||_2^2 (breaks L^2 invariance).
  CC2 wrong dimension: in d = 2 the exponent -3/2 gives ||.||_2^2 = eps^(-1)||f2||_2^2; exponent -1 = -d/2 keeps it.
  CC3 non-solenoidal profile grad G: div of its eps-rescaling is not identically 0.
  F1  finite state space: for EVERY map T on a 4-element set (256 maps; 24 bijections) and the rational
      observation P(s) = (s+1)/3, the orbit maximum over the first 4 steps equals that over 64 steps (the sup
      over all times is a max over a finite set), for non-bijective maps as well -- reversibility is not used.
  F2  exact finite family, N = 4^m, m = 1..5, h = 1/N on the discrete torus (Z_N)^3: u_N = curl_h(psi e3),
      psi = A delta_0, A = 1/(2 sqrt h) = 2^(m-1), forward differences. Discrete divergence (forward) = 0 exactly;
      discrete energy h^3 sum |u|^2 = 1 for every m; sup|u_N| = 2^(3m-1) = N^(3/2)/2; translation by one cell (a
      bijection of the finite torus) preserves both, so sup over the orbit is finite at each N and unbounded in N.
  CC4 no concentration: the sampled field (sin 2 pi x2, 0, 0) on N = 4, 8, 16 has discrete energy exactly 1/2 and
      sup exactly 1 for every N (the value 1 at j = N/4; |sin| <= 1 [W]), so non-uniformity is not forced by
      finiteness or by an energy bound.

DECISION RULE (fixed before the first run). VERDICT-SCALING prints "L2-invariant, L-infinity-divergent,
divergence-free family confirmed; -3/2 is the L2-critical exponent in d = 3, not the NS-invariant one" iff
S0-S6 and CC1-CC3 all PASS; VERDICT-FINITE prints "bounded at each finite resolution for every map on a finite set;
non-uniform in resolution only under concentration" iff F1, F2, CC4 PASS. Any FAIL prints "NO VERDICT (control
failed)" for the verdict it belongs to.
"""
from fractions import Fraction
from itertools import product
import sympy as sp

results = {}


def record(name, ok, detail=""):
    results[name] = bool(ok)
    print(f"{name}: {'PASS' if ok else 'FAIL'}{(' -- ' + detail) if detail else ''}")


y1, y2, y3 = sp.symbols("y1 y2 y3", real=True)
x1, x2, x3 = sp.symbols("x1 x2 x3", real=True)
a, b, c = sp.symbols("a b c", real=True)
eps = sp.symbols("epsilon", positive=True)
oo = sp.oo
G = sp.exp(-(y1**2 + y2**2 + y3**2))
f = [sp.diff(G, y2), -sp.diff(G, y1), sp.Integer(0)]
Y = (y1, y2, y3)


def div(v, X):
    return sp.simplify(sum(sp.diff(v[i], X[i]) for i in range(3)))


def rescale(v, exponent, shift):
    sub = {y1: (x1 - shift[0]) / eps, y2: (x2 - shift[1]) / eps, y3: (x3 - shift[2]) / eps}
    return [eps**exponent * comp.subs(sub) for comp in v]


def l2sq(v, X):
    integrand = sp.expand(sum(comp**2 for comp in v))
    val = sp.integrate(integrand, (X[0], -oo, oo), (X[1], -oo, oo), (X[2], -oo, oo))
    # run 2: erfc(z) = 1 - erf(z) is applied exactly before simplifying (run 1 left erf + erfc unsimplified)
    return sp.simplify(val.rewrite(sp.erf))


X = (x1, x2, x3)
record("S0", div(f, Y) == 0, f"f = ({f[0]}, {f[1]}, 0)")
u = rescale(f, sp.Rational(-3, 2), (a, b, c))
record("S1", div(u, X) == 0, "div u_eps simplifies to 0")
nf = l2sq(f, Y)
nu0 = l2sq(rescale(f, sp.Rational(-3, 2), (0, 0, 0)), X)
record("S2", sp.simplify(nu0 - nf) == 0, f"||f||_2^2 = {nf}; ||u_eps||_2^2 = {nu0}")
nut = l2sq(rescale(f, sp.Rational(-3, 2), (sp.Rational(1, 3), -2, sp.Rational(5, 7))), X)
record("S2t", sp.simplify(nut - nf) == 0, f"shifted: {nut}")

r = sp.symbols("r", nonnegative=True)
g = 4 * r * sp.exp(-2 * r)
crit = sp.solve(sp.diff(g, r), r)
second = sp.simplify(sp.diff(g, r, 2).subs(r, sp.Rational(1, 2)))
fsq = sp.simplify(sum(comp**2 for comp in f))
bound = sp.simplify(fsq - g.subs(r, y1**2 + y2**2))  # = g(r) (e^{-2 y3^2} - 1) <= 0
peak = sp.sqrt(2 / sp.E)
ystar = {y1: 1 / sp.sqrt(2), y2: 0, y3: 0}
at_star = sp.simplify(sp.sqrt(fsq.subs(ystar)) - peak)
xstar = {x1: a + eps / sp.sqrt(2), x2: b, x3: c}
u_star = sp.simplify(sp.sqrt(sum(comp**2 for comp in u)).subs(xstar) - eps**sp.Rational(-3, 2) * peak)
ok3 = (crit == [sp.Rational(1, 2)] and second.is_negative and at_star == 0 and u_star == 0
       and sp.simplify(bound - g.subs(r, y1**2 + y2**2) * (sp.exp(-2 * y3**2) - 1)) == 0)
record("S3", ok3, f"critical r = {crit}, g''(1/2) = {second}, sup|f| = {peak}, |u_eps(x0 + eps y*)| = eps^(-3/2) sup|f|")
record("S4", sp.limit(eps**sp.Rational(-3, 2) * peak, eps, 0, "+") == oo, "eps^(-3/2) sqrt(2/e) -> oo")


def grad_sq(v, X):
    return sum(sp.diff(v[i], X[j])**2 for i in range(3) for j in range(3))


ens_f = sp.simplify(sp.integrate(sp.expand(grad_sq(f, Y)), (y1, -oo, oo), (y2, -oo, oo), (y3, -oo, oo)))
u00 = rescale(f, sp.Rational(-3, 2), (0, 0, 0))
ens_u = sp.simplify(sp.integrate(sp.expand(grad_sq(u00, X)), (x1, -oo, oo), (x2, -oo, oo), (x3, -oo, oo)))
record("S5", sp.simplify(ens_u - ens_f / eps**2) == 0, f"||grad f||^2 = {ens_f}; ||grad u_eps||^2 = {ens_u}")

# S6: NS scaling, checked term by term on two concrete smooth test pairs (u, p); the general statement is the
# chain rule [W]. Energy factor lam^(-1) checked on the Gaussian profile f.
t, lam, nu = sp.symbols("t lambda nu", positive=True)
s1, s2, s3, tau = sp.symbols("s1 s2 s3 tau", real=True)
S = (s1, s2, s3)
back = {s1: lam * x1, s2: lam * x2, s3: lam * x3, tau: lam**2 * t}
tests = [([sp.sin(s2) * sp.exp(-tau), s1**2 * tau, sp.cos(s3 + tau)], s1 * s2 * tau**2),
         ([s2 * s3, sp.exp(s1 - tau), s1 + s2**2], sp.sin(s1 * s3) + tau)]
ok6 = True
for Ut, Pt in tests:
    ul = [lam * comp.subs(back) for comp in Ut]
    pl = lam**2 * Pt.subs(back)
    for i in range(3):
        terms_l = [sp.diff(ul[i], t), sum(ul[j] * sp.diff(ul[i], X[j]) for j in range(3)),
                   nu * sum(sp.diff(ul[i], X[j], 2) for j in range(3)), sp.diff(pl, X[i])]
        terms_0 = [sp.diff(Ut[i], tau), sum(Ut[j] * sp.diff(Ut[i], S[j]) for j in range(3)),
                   nu * sum(sp.diff(Ut[i], S[j], 2) for j in range(3)), sp.diff(Pt, S[i])]
        for tl, t0 in zip(terms_l, terms_0):
            ok6 = ok6 and sp.simplify(tl - lam**3 * t0.subs(back)) == 0
lam_sub = {y1: lam * x1, y2: lam * x2, y3: lam * x3}
e_lam = l2sq([lam * comp.subs(lam_sub) for comp in f], X)
ok6 = ok6 and sp.simplify(e_lam - nf / lam) == 0
record("S6", ok6, f"each of d_t u, (u.grad)u, nu Lap u, grad p scales by lam^3; ||lam f(lam x)||^2 = {e_lam}")

n1 = l2sq(rescale(f, -1, (0, 0, 0)), X)
record("CC1", sp.simplify(n1 - eps * nf) == 0 and sp.simplify(n1 - nf) != 0, f"exponent -1: {n1}")
f2 = [sp.diff(sp.exp(-(y1**2 + y2**2)), y2), -sp.diff(sp.exp(-(y1**2 + y2**2)), y1)]
nf2 = sp.integrate(sp.expand(f2[0]**2 + f2[1]**2), (y1, -oo, oo), (y2, -oo, oo))


def l2sq_2d(expo):
    sub = {y1: x1 / eps, y2: x2 / eps}
    v = [eps**expo * comp.subs(sub) for comp in f2]
    return sp.simplify(sp.integrate(sp.expand(v[0]**2 + v[1]**2), (x1, -oo, oo), (x2, -oo, oo)))


m32, m1 = l2sq_2d(sp.Rational(-3, 2)), l2sq_2d(-1)
record("CC2", sp.simplify(m32 - nf2 / eps) == 0 and sp.simplify(m1 - nf2) == 0,
       f"d = 2: exponent -3/2 -> {m32}; exponent -1 -> {m1}")
gG = [sp.diff(G, v) for v in Y]
record("CC3", div(rescale(gG, sp.Rational(-3, 2), (a, b, c)), X) != 0, "div of rescaled grad G is not 0")

# F1: every map on a 4-element set; the orbit maximum over 4 steps equals that over 64 steps
f1_ok, nbij = True, 0
for T in product(range(4), repeat=4):
    nbij += len(set(T)) == 4
    for s0 in range(4):
        orbit, s = [], s0
        for _ in range(64):
            orbit.append(Fraction(s + 1, 3))
            s = T[s]
        f1_ok = f1_ok and max(orbit[:4]) == max(orbit)
record("F1", f1_ok and nbij == 24,
       f"256 maps ({nbij} bijections): orbit max over 4 steps = over 64 steps, for every map and start")

# F2: discrete curl family on (Z_N)^3
f2_ok, rows = True, []
for m in range(1, 6):
    N, h = 4**m, Fraction(1, 4**m)
    A = Fraction(2**(m - 1))  # = 1/(2 sqrt h)
    psi = {(0, 0, 0): A}

    def ps(i):
        return psi.get((i[0] % N, i[1] % N, i[2] % N), 0)

    sites = {(i0 % N, i1 % N, 0) for i0 in (-2, -1, 0, 1) for i1 in (-2, -1, 0, 1)}
    field = {}
    for x in sites:
        u1 = (ps((x[0], x[1] + 1, x[2])) - ps(x)) / h
        u2 = -(ps((x[0] + 1, x[1], x[2])) - ps(x)) / h
        if u1 or u2:
            field[x] = (u1, u2)

    def uu(x, k):
        return field.get((x[0] % N, x[1] % N, x[2] % N), (0, 0))[k]

    divs = [(uu((x[0] + 1, x[1], x[2]), 0) - uu(x, 0)) / h + (uu((x[0], x[1] + 1, x[2]), 1) - uu(x, 1)) / h
            for x in sites]
    energy = h**3 * sum(v[0]**2 + v[1]**2 for v in field.values())
    sup = max(max(abs(v[0]), abs(v[1])) for v in field.values())
    shifted = {((x[0] + 1) % N, x[1], x[2]): v for x, v in field.items()}
    e_shift = h**3 * sum(v[0]**2 + v[1]**2 for v in shifted.values())
    f2_ok = f2_ok and all(dv == 0 for dv in divs) and energy == 1 and sup == Fraction(2**(3 * m - 1)) \
        and e_shift == 1
    rows.append(f"N={N}: energy={energy}, sup={sup}")
record("F2", f2_ok, "; ".join(rows))

cc4_ok, rows = True, []
for N in (4, 8, 16):
    vals = [sp.sin(2 * sp.pi * sp.Rational(j, N)) for j in range(N)]
    en = sp.simplify(sp.expand(sum(v**2 for v in vals)) / N)
    peak_val = vals[N // 4]  # |sin| <= 1 everywhere [W]; the value 1 is attained exactly at j = N/4
    cc4_ok = cc4_ok and en == sp.Rational(1, 2) and peak_val == 1
    rows.append(f"N={N}: energy={en}, sup={peak_val}")
record("CC4", cc4_ok, "; ".join(rows))

sc = ["S0", "S1", "S2", "S2t", "S3", "S4", "S5", "S6", "CC1", "CC2", "CC3"]
print("VERDICT-SCALING: " + ("L2-invariant, L-infinity-divergent, divergence-free family confirmed; -3/2 is the "
                             "L2-critical exponent in d = 3, not the NS-invariant one"
                             if all(results[n] for n in sc) else "NO VERDICT (control failed)"))
print("VERDICT-FINITE: " + ("bounded at each finite resolution for every map on a finite set; non-uniform in "
                            "resolution only under concentration" if all(results[n] for n in ("F1", "F2", "CC4"))
                            else "NO VERDICT (control failed)"))
print(f"checks: {sum(results.values())}/{len(results)} PASS")
