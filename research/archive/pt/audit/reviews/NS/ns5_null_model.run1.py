#!/usr/bin/env python3
"""ns5_null_model.py -- thread NS, question NS.5 (decisive). Exact: sympy rationals/symbols, Fractions.

QUESTION. Is "regular finite approximants, singular continuum limit" (NS-INPUT L60-78; PROGRAMME S1 L129-143)
evidence of a hidden sector? Null models with NO hidden sector anywhere.

PART B -- inviscid Burgers u_t + u u_x = 0 on the circle, u(x,0) = -sin x. Characteristics: x = xi - t sin xi,
  u = -sin xi.
  B1 the characteristic solution satisfies the PDE (implicit differentiation, residual simplifies to 0).
  B2 initial condition: at t = 0, xi = x and u = -sin x.
  B3 Jacobian dx/dxi = 1 - t cos xi >= 1 - t > 0 for t < 1 and = 0 at (xi, t) = (0, 1); u_x(0,t) = -1/(1-t);
     lim_{t->1-} u_x(0,t) = -oo; t* = -1/min u0' = 1 (min of -cos x is -1, at x = 0 [W]; evaluated at 0 and pi).
  B4 |u| <= 1 for t < 1 (u = -sin xi): the singularity is a gradient blow-up with bounded velocity.
  B5 energy int_0^{2pi} u^2 dx = pi for every t < 1 (change of variables x -> xi, symbolic t).
PART G -- sine-Galerkin truncations u_N = sum_{k<=N} a_k(t) sin kx, a_k' = -(1/pi) int u_N (u_N)_x sin kx dx
  (direct projection of -u u_x; the odd subspace is invariant), N = 1..5.
  G1 energy pi sum a_k^2 conserved: sum a_k a_k' = 0 identically.   G2 Liouville: sum d a_k'/d a_k = 0.
  G3 reversibility: V(-a) = V(a) (quadratic), so a(t) -> -a(-t) maps solutions to solutions.
  G4 N = 2 system is a1' = a1 a2/2, a2' = -a1^2/2, solved exactly by a1 = -sech(t/2), a2 = -tanh(t/2) from
     a(0) = (-1, 0); N = 1 is stationary (u_1 = -sin x for all t).
  G5 along G4: a1^2 + a2^2 = 1 and the gradient at 0, a1 + 2 a2, stays in [-sqrt 5, -1] for all t >= 0 (exact
     values at tau = tanh(t/2) = 0, 2/sqrt 5, 1 plus monotonicity [W]), whereas the PDE from the same data has
     u_x(0,t) = -1/(1-t) (B3). General N [W]: on the energy sphere,
     ||d_x u_N||_inf <= sqrt(N(N+1)(2N+1)/6) * sqrt(sum a_k^2), finite for each N, growing with N.
  G6 countercontrol (closedness alone does not give regularity): y' = y^2, y(0) = 1 has y = 1/(1-t), blow-up
     at t = 1; it is exactly the gradient law D(u_x)/Dt = -u_x^2 along the characteristic xi = 0 with w = -u_x.
  G7 countercontrol (G1 is not vacuous): the broken N = 2 field (a1 a2, -a1^2/2) does not conserve energy.
PART C -- closure failure of the projected EXACT dynamics (resolved: mode 1).
  C1 for u = a1 sin x + a2 sin 2x + a3 sin 3x the exact rate of a1 is (a1 a2 + a2 a3)/2: at a1 = -1 the rate is
     0 for (a2, a3) = (0, 0) and 1/4 for (a2, a3) = (-1/2, 0) -- same resolved state, different resolved rate.
  C2 the resolved-energy flux d(pi a1^2)/dt = pi a1 (a1 a2 + a2 a3) is not identically 0 (transfer to the
     unresolved modes), while the N = 1 truncation has flux 0.
PART M -- SM.md Theorem 1a (L238-244), exact instance: U = Koopman matrix of the 5-cycle s -> s+1 mod 5, P the
  projection on coordinates {0,1}. M1: p_{t+1} = A p_t + sum_{s<t} B D^{t-1-s} C p_s + B D^t q_0 for t = 0..11 and two
  initial vectors. CC-M: the Markov part alone (p_{t+1} = A p_t) fails at some t.
PART F -- a fully observed finite bijective family with the boxed S1 shape. N = 4^m (m = 1..4), h = 1/N, lattice
  (Z_N)^3; states j in Z_{m+1}, Phi_N(j) = j+1 mod (m+1) (a bijection); observation P_N(j) = the field (8^j, 0, 0)
  on a cube of 4^(m-j) cells (side 4^(-j) = 1 - t_j at t_j = 1 - 4^(-j)), time map n(t) = min(j(t), m), n(1) = m.
  F1 P_N injective (nothing hidden); discrete energy h^3 sum |u|^2 = 1 at every state; sup over the orbit = 8^m =
     N^(3/2) (finite at each N, unbounded in N); the field at each t_j is the same for every N >= 4^j.
  CC-F no concentration (one cube of side 1, value 1): sup = 1 for every N.

DECISION RULE (fixed before the first run). VERDICT-NULL prints "null model holds: closed, energy-conserving,
volume-preserving, reversible truncations are globally regular while the continuum solution from the same data
blows up at t = 1; the projected exact dynamics is not closed; the boxed S1 shape is realized with nothing hidden"
iff B1-B5, G1-G5, C1, C2, M1, F1 all PASS and the countercontrols G6, G7, CC-M, CC-F all PASS (each countercontrol
PASSES when the stated failure or contrast is observed). Otherwise "NO VERDICT (control failed)". Scope: the stated
instances; general-N statements are [W] with the instances as checks; convergence of Galerkin truncations to the
smooth solution before t* is [L, unverified] and is not used by any check.
"""
from fractions import Fraction
import sympy as sp

results = {}


def record(name, ok, detail=""):
    results[name] = bool(ok)
    print(f"{name}: {'PASS' if ok else 'FAIL'}{(' -- ' + detail) if detail else ''}")


x, t, xi = sp.symbols("x t xi", real=True)
pi = sp.pi

# ---------------- PART B
Fimp = xi - t * sp.sin(xi) - x
xi_x = -sp.diff(Fimp, x) / sp.diff(Fimp, xi)
xi_t = -sp.diff(Fimp, t) / sp.diff(Fimp, xi)
u = -sp.sin(xi)
u_x, u_t = sp.diff(u, xi) * xi_x, sp.diff(u, xi) * xi_t
record("B1", sp.simplify(u_t + u * u_x) == 0, f"xi_x = {sp.simplify(xi_x)}, xi_t = {sp.simplify(xi_t)}")
record("B2", sp.simplify(Fimp.subs(t, 0).subs(xi, x)) == 0 and u.subs(xi, x) == -sp.sin(x), "t = 0: xi = x")
J = sp.diff(xi - t * sp.sin(xi), xi)
ux0 = sp.simplify(u_x.subs(xi, 0))
ok_b3 = (sp.simplify(J - (1 - t * sp.cos(xi))) == 0 and J.subs({xi: 0, t: 1}) == 0
         and sp.simplify(ux0 + 1 / (1 - t)) == 0 and sp.limit(ux0, t, 1, "-") == -sp.oo
         and sp.simplify(-1 / sp.Min(*[sp.diff(-sp.sin(x), x).subs(x, v) for v in (0, pi)])) == 1)
record("B3", ok_b3, f"J = {J}; u_x(0,t) = {ux0}; t* = 1")
record("B4", sp.simplify(u**2 - sp.sin(xi)**2) == 0, "u = -sin(xi), |u| <= 1 while J > 0 (bijective chart)")
energy = sp.simplify(sp.integrate(sp.sin(xi)**2 * J, (xi, 0, 2 * pi)))
record("B5", energy == pi, f"int u^2 dx = {energy} for all t < 1")

# ---------------- PART G
NMAX = 5
I3 = {}
for j in range(1, NMAX + 1):
    for l in range(1, NMAX + 1):
        for k in range(1, NMAX + 1):
            I3[(j, l, k)] = sp.integrate(sp.sin(j * x) * sp.cos(l * x) * sp.sin(k * x), (x, 0, 2 * pi))


def galerkin(N):
    a = sp.symbols(f"a1:{N + 1}", real=True)
    V = [sp.expand(-sum(a[j - 1] * a[l - 1] * l * I3[(j, l, k)] for j in range(1, N + 1)
                        for l in range(1, N + 1)) / pi) for k in range(1, N + 1)]
    return a, V


g1 = g2 = g3 = True
for N in range(1, NMAX + 1):
    a, V = galerkin(N)
    g1 = g1 and sp.expand(sum(a[k] * V[k] for k in range(N))) == 0
    g2 = g2 and sp.expand(sum(sp.diff(V[k], a[k]) for k in range(N))) == 0
    neg = {a[k]: -a[k] for k in range(N)}
    g3 = g3 and all(sp.expand(V[k].subs(neg, simultaneous=True) - V[k]) == 0 for k in range(N))
record("G1", g1, "sum a_k a_k' = 0 identically, N = 1..5")
record("G2", g2, "divergence of the truncated field = 0, N = 1..5")
record("G3", g3, "V(-a) = V(a), N = 1..5")
a2s, V2 = galerkin(2)
A1, A2 = a2s
sol = {A1: -sp.sech(t / 2), A2: -sp.tanh(t / 2)}
res = [sp.simplify((sp.diff(sol[A1], t) - V2[0].subs(sol)).rewrite(sp.exp)),
       sp.simplify((sp.diff(sol[A2], t) - V2[1].subs(sol)).rewrite(sp.exp))]
a1s, V1 = galerkin(1)
ok_g4 = (sp.expand(V2[0] - A1 * A2 / 2) == 0 and sp.expand(V2[1] + A1**2 / 2) == 0 and res == [0, 0]
         and sol[A1].subs(t, 0) == -1 and sol[A2].subs(t, 0) == 0 and V1 == [0])
record("G4", ok_g4, f"N=2 field: ({V2[0]}, {V2[1]}); residuals of the closed form: {res}; N=1 field: {V1}")
sphere = sp.simplify((sol[A1]**2 + sol[A2]**2).rewrite(sp.exp))
grad0 = sol[A1] + 2 * sol[A2]
tau_ = sp.symbols("tau", real=True)
gq = (-sp.sqrt(1 - tau_**2) - 2 * tau_)  # a2 = -tau, a1 = -sqrt(1 - tau^2), tau = tanh(t/2) in [0, 1) for t >= 0
crit = sp.solve(sp.diff(gq, tau_), tau_)
c0 = 2 * sp.sqrt(5) / 5  # 0 < c0, c0^2 = 4/5 < 1; gq decreases on [0, c0], increases on [c0, 1) [W]
vals = (sp.simplify(gq.subs(tau_, 0)), sp.simplify(gq.subs(tau_, c0)), sp.simplify(gq.subs(tau_, 1)))
ok_g5 = (sphere == 1 and crit == [c0] and c0**2 == sp.Rational(4, 5) and vals == (-1, -sp.sqrt(5), -2)
         and sp.simplify(grad0.subs(t, 0) + 1) == 0)
record("G5", ok_g5, f"a1^2 + a2^2 = {sphere}; a1 + 2 a2 at tau = 0, 2/sqrt5, 1: {vals}, so it stays in "
       "[-sqrt 5, -1] for all t >= 0")
yv = 1 / (1 - t)
w = -ux0
ok_g6 = (sp.simplify(sp.diff(yv, t) - yv**2) == 0 and yv.subs(t, 0) == 1 and sp.limit(yv, t, 1, "-") == sp.oo
         and sp.simplify(sp.diff(w, t) - w**2) == 0)
record("G6", ok_g6, "y' = y^2 blows up at t = 1; w = -u_x(0,t) obeys the same law")
broken = sp.expand(A1 * (A1 * A2) + A2 * (-A1**2 / 2))
record("G7", broken != 0, f"broken field: d/dt (a1^2 + a2^2)/2 = {broken}")

# ---------------- PART C
a3s, V3 = galerkin(3)
B1_, B2_, B3_ = a3s
rate1 = sp.expand(V3[0])
r_a = rate1.subs({B1_: -1, B2_: 0, B3_: 0})
r_b = rate1.subs({B1_: -1, B2_: sp.Rational(-1, 2), B3_: 0})
record("C1", sp.expand(rate1 - (B1_ * B2_ + B2_ * B3_) / 2) == 0 and r_a == 0 and r_b == sp.Rational(1, 4),
       f"rate of a1 = {rate1}; at a1 = -1: {r_a} vs {r_b}")
flux = sp.expand(pi * 2 * B1_ * rate1)
record("C2", flux != 0 and sp.expand(2 * pi * a1s[0] * V1[0]) == 0, f"d(pi a1^2)/dt = {flux}; N=1 truncation: 0")

# ---------------- PART M
n = 5
U = sp.zeros(n, n)
for s in range(n):
    U[s, (s + 1) % n] = 1
Pm = sp.diag(1, 1, 0, 0, 0)
Qm = sp.eye(n) - Pm
Am, Bm, Cm, Dm = Pm * U * Pm, Pm * U * Qm, Qm * U * Pm, Qm * U * Qm
m1, markov_fails = True, False
for v in (sp.Matrix([1, 2, 3, 4, 5]), sp.Matrix([3, -1, 0, 7, 2])):
    q0 = Qm * v
    ps = [Pm * (U**s) * v for s in range(13)]
    for tt in range(12):
        mem = sp.zeros(n, 1)
        for s in range(tt):
            mem += Bm * Dm**(tt - 1 - s) * Cm * ps[s]
        m1 = m1 and ps[tt + 1] == Am * ps[tt] + mem + Bm * Dm**tt * q0
        markov_fails = markov_fails or ps[tt + 1] != Am * ps[tt]
record("M1", m1, "exact projected identity holds for t = 0..11, two initial vectors")
record("CC-M", markov_fails, "the Markov part alone fails at some t")

# ---------------- PART F
f1, rows = True, []
for m in range(1, 5):
    N, h = 4**m, Fraction(1, 4**m)
    obs = []
    for j in range(m + 1):
        cells, amp = 4**(m - j), Fraction(8**j)
        obs.append((cells, amp, h**3 * cells**3 * amp**2, Fraction(cells, N)))
    bij = sorted((j + 1) % (m + 1) for j in range(m + 1)) == list(range(m + 1))
    injective = len({(o[0], o[1]) for o in obs}) == len(obs)
    energies_ok = all(o[2] == 1 for o in obs)
    sup = max(o[1] for o in obs)
    same_field = all(o[3] == Fraction(1, 4**j) and o[1] == 8**j for j, o in enumerate(obs))
    f1 = f1 and bij and injective and energies_ok and sup**2 == Fraction(N)**3 and same_field
    rows.append(f"N={N}: states {m + 1}, energy 1, sup {sup}")
record("F1", f1, "; ".join(rows))
ccf, rows = True, []
for m in range(1, 5):
    N, h, cells, amp = 4**m, Fraction(1, 4**m), 4**m, Fraction(1)
    en, sup = h**3 * cells**3 * amp**2, amp
    ccf = ccf and en == 1 and sup == 1
    rows.append(f"N={N}: energy {en}, sup {sup}")
record("CC-F", ccf, "unconcentrated cube: " + "; ".join(rows))

main = ["B1", "B2", "B3", "B4", "B5", "G1", "G2", "G3", "G4", "G5", "C1", "C2", "M1", "F1"]
ctrl = ["G6", "G7", "CC-M", "CC-F"]
if all(results[k] for k in main + ctrl):
    print("VERDICT-NULL: null model holds: closed, energy-conserving, volume-preserving, reversible truncations are "
          "globally regular while the continuum solution from the same data blows up at t = 1; the projected exact "
          "dynamics is not closed; the boxed S1 shape is realized with nothing hidden")
else:
    print("VERDICT-NULL: NO VERDICT (control failed)")
print(f"checks: {sum(results.values())}/{len(results)} PASS")
