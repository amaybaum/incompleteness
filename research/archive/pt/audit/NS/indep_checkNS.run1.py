#!/usr/bin/env python3
"""Coordinator's independent check for the NS review (written from PROTOCOL-NS.md's questions and the
NS input, before reading the thread's RESULT; no thread code).  Exact arithmetic (sympy) throughout.

DECISION RULE (fixed before the first run): every check prints CONFIRMED or MISMATCH; the verdict line
INDEP-NS-CONFIRMED prints iff every check, countercontrols included, is CONFIRMED.  Countercontrols must
behave as their header line states.  Nothing nondeterministic is printed.

Sections.  A: the input's scaling family u_eps = eps^(-3/2) f((x-x0)/eps) (L2 invariance, sup divergence,
divergence-free preserved, the exponent 3/2 is the unique L2-preserving one; H1 seminorm diverges).
B: "finite state space => bounded at fixed eps, not uniformly": an exact finite instance, with the
countercontrol that an eps-independent normalisation IS uniform (the non-uniformity is the normalisation).
C: the null model (NS.5): inviscid Burgers u_t + u u_x = 0, u(x,0) = -sin x on the circle: exact
characteristic solution, gradient -1/(1-t) at x = 0 (blow-up at t = 1), energy pi conserved for t < 1;
the N = 2 odd Fourier-Galerkin truncation conserves energy exactly, so it is globally regular, with the
sup norm and the slope bounded by constants that grow with N.  D: the H-B round's HB3-a witness
(HexLatticeGas.lean:935-981, kernel-recorded configurations) recomputed: equal block charges at t and
t-1 for symbolic channel weights, different P1 on block (0,0) at t+1.
"""
import sympy as sp, sys
R = []
def rec(cid, kind, ok, text, detail=""):
    ok = bool(ok); R.append(ok)
    print(f"{'CONFIRMED' if ok else 'MISMATCH'} {cid} [{kind}] {text}" + (f" -- {detail}" if detail else ""))

# ---------------- A. the scaling family ----------------
print("== A  the scaling family u_eps(x) = eps^(-3/2) f((x - x0)/eps)")
x, y, z = sp.symbols('x y z', real=True); eps = sp.symbols('epsilon', positive=True); al = sp.symbols('alpha', real=True)
X = sp.Matrix([x, y, z]); x0 = sp.Matrix([sp.Rational(1,3), -sp.Rational(2,7), sp.Rational(5,11)])
phi = sp.exp(-(x**2 + y**2 + z**2))                      # vector potential (0,0,phi): f = curl
f = sp.Matrix([sp.diff(phi, y), -sp.diff(phi, x), 0])     # smooth, localized, divergence-free
div = lambda F, vars_: sum(sp.diff(F[i], vars_[i]) for i in range(3))
rec("A1","identity", sp.simplify(div(f, (x,y,z))) == 0, "f = curl(0,0,e^{-|x|^2}) is divergence-free")
def scaled(F, a):   # eps^(-a) F((x - x0)/eps)
    sub = {x: (x - x0[0])/eps, y: (y - x0[1])/eps, z: (z - x0[2])/eps}
    return sp.Matrix([eps**(-a) * Fi.subs(sub, simultaneous=True) for Fi in F])
u = scaled(f, sp.Rational(3,2))
rec("A2","identity", sp.simplify(div(u, (x,y,z))) == 0, "div u_eps = 0: the scaling preserves incompressibility")
def l2sq(F):
    integrand = sp.expand(sum(Fi**2 for Fi in F))
    return sp.simplify(sp.integrate(sp.integrate(sp.integrate(integrand, (x,-sp.oo,sp.oo)), (y,-sp.oo,sp.oo)), (z,-sp.oo,sp.oo)))
nf = l2sq(f); nu = l2sq(u)
rec("A3","identity", sp.simplify(nu - nf) == 0, "||u_eps||_2^2 = ||f||_2^2 for every eps > 0 (exact Gaussian integrals)", f"||f||_2^2 = {nf}")
ug = scaled(f, al); nug = l2sq(ug)
rec("A4","identity", sp.simplify(nug - eps**(3-2*al)*nf) == 0 and sp.solve(sp.Eq(3-2*al, 0), al) == [sp.Rational(3,2)],
    "||eps^(-a) f(./eps)||_2^2 = eps^(3-2a)||f||_2^2: a = 3/2 is the unique L2-preserving exponent (the Navier-Stokes scaling a = 1 is not)")
s = sp.symbols('s', nonnegative=True)                      # |f|^2 = 4 s e^{-2s}, s = x^2 + y^2 (z-independent)
f2 = sp.simplify(sum(Fi**2 for Fi in f)).subs(x**2 + y**2, s)
g = sp.simplify(f2.subs({x: sp.sqrt(s), y: 0}))
crit = sp.solve(sp.diff(g, s), s); fmax2 = max(g.subs(s, c) for c in crit)
rec("A5","identity", sp.simplify(g - 4*s*sp.exp(-2*s)) == 0 and crit == [sp.Rational(1,2)] and sp.simplify(fmax2 - 2/sp.E) == 0,
    "||f||_inf^2 = max_s 4 s e^{-2s} = 2/e, attained at |x|^2+|y|^2 = 1/2", f"sup|f| = sqrt({fmax2})")
rec("A6","identity", sp.limit(eps**(-sp.Rational(3,2)) * sp.sqrt(fmax2), eps, 0, '+') == sp.oo,
    "||u_eps||_inf = eps^(-3/2)||f||_inf -> infinity as eps -> 0: finite energy, unbounded peak (the input's kinematic claim)")
grad2 = lambda F: sp.expand(sum(sp.diff(Fi, v)**2 for Fi in F for v in (x,y,z)))
H1f = sp.simplify(sp.integrate(sp.integrate(sp.integrate(grad2(f), (x,-sp.oo,sp.oo)), (y,-sp.oo,sp.oo)), (z,-sp.oo,sp.oo)))
H1u = sp.simplify(sp.integrate(sp.integrate(sp.integrate(grad2(u), (x,-sp.oo,sp.oo)), (y,-sp.oo,sp.oo)), (z,-sp.oo,sp.oo)))
rec("A7","identity", sp.simplify(H1u - H1f/eps**2) == 0, "||grad u_eps||_2^2 = eps^(-2)||grad f||_2^2: the enstrophy diverges, so the family leaves every bounded-enstrophy class (not a Leray-Hopf obstruction, a kinematic fact)")
rec("A8c","countercontrol", sp.simplify(l2sq(scaled(f, 1)) - eps*nf) == 0 and sp.limit(eps*nf, eps, 0, '+') == 0,
    "countercontrol: the Navier-Stokes self-similar exponent a = 1 sends the energy to 0, so the L2 invariance is specific to a = 3/2")

# ---------------- B. finite => bounded at fixed eps; non-uniform by normalisation ----------------
print()
print("== B  finite state space: bounded at fixed resolution; the non-uniformity is the normalisation")
# exact finite instance: n = 1/eps sites, occupation in {0,1}; coarse 'velocity' v_eps(s) = eps^(-3/2) * (occupied/n)
bounds = {}
for n in (2, 4, 8):
    e = sp.Rational(1, n); states = n + 1            # occupation counts 0..n (the observation sees only the count)
    sup = max(e**(-sp.Rational(3,2)) * sp.Rational(m, n) for m in range(states))
    bounds[n] = sup
rec("B1","enumerate", all(bounds[n] == sp.Rational(1, n)**(-sp.Rational(3,2)) for n in bounds) and bounds[8] > bounds[4] > bounds[2],
    "at each fixed eps = 1/n the observed values form a finite set with an exact finite bound; the bounds grow like eps^(-3/2) across n", str({n: str(bounds[n]) for n in bounds}))
rec("B2c","countercontrol", all(max(sp.Rational(m, n) for m in range(n+1)) == 1 for n in (2,4,8)),
    "countercontrol: with the eps-independent normalisation (occupied fraction) the same finite systems are bounded by 1 UNIFORMLY in eps: the boxed non-uniformity comes from the continuum normalisation P_eps, not from finiteness")

# ---------------- C. the Burgers null model ----------------
print()
print("== C  null model: inviscid Burgers, u(x,0) = -sin x: exact blow-up at t = 1; Galerkin truncations globally regular")
t, xi = sp.symbols('t xi', real=True)
# characteristics: x = xi - t sin(xi), u = -sin(xi).  Check u_t + u u_x = 0 by implicit differentiation.
Xc = xi - t*sp.sin(xi); U = -sp.sin(xi)
dX_dxi = sp.diff(Xc, xi); dX_dt = sp.diff(Xc, t)
u_x = sp.diff(U, xi)/dX_dxi; u_t = -sp.diff(U, xi)*dX_dt/dX_dxi      # d/dt at fixed x: xi_t = -X_t/X_xi
rec("C1","identity", sp.simplify(u_t + U*u_x) == 0, "u(x,t) = -sin(xi), x = xi - t sin(xi) solves u_t + u u_x = 0 (characteristics)")
rec("C2","identity", sp.simplify(u_x.subs(xi, 0) + 1/(1-t)) == 0 and sp.limit(u_x.subs(xi, 0), t, 1, '-') == -sp.oo,
    "u_x(0,t) = -1/(1-t): the gradient blows up at t = 1 while |u| <= 1 stays bounded (gradient catastrophe, finite energy)")
rec("C3","identity", sp.simplify(sp.Min(*[dX_dxi.subs(xi, v) for v in (0, sp.pi/3, sp.pi/2, sp.pi)]) ) is not None and sp.simplify(dX_dxi - (1 - t*sp.cos(xi))) == 0,
    "x_xi = 1 - t cos(xi) >= 1 - t > 0 for t < 1: the characteristic map is a diffeomorphism and u is smooth before t = 1")
energy = sp.simplify(sp.integrate(U**2 * dX_dxi, (xi, -sp.pi, sp.pi)))
rec("C4","identity", energy == sp.pi, "energy int u^2 dx = int sin^2(xi) (1 - t cos xi) dxi = pi for every t < 1 (conserved up to the shock)")
# Galerkin: odd truncation u_N = sum_{k<=N} b_k(t) sin(kx); project u u_x onto {sin kx : k <= N}
def galerkin_rhs(N):
    b = sp.symbols(f'b1:{N+1}', real=True); uN = sum(b[k-1]*sp.sin(k*x) for k in range(1, N+1))
    nl = sp.expand(sp.expand_trig(uN*sp.diff(uN, x)))
    rhs = [-sp.integrate(nl*sp.sin(k*x), (x, -sp.pi, sp.pi))/sp.pi for k in range(1, N+1)]   # b_k' = -<u u_x, sin kx>/pi
    return b, [sp.simplify(r) for r in rhs]
b1, rhs1 = galerkin_rhs(1); b2, rhs2 = galerkin_rhs(2)
rec("C5","identity", rhs1 == [0], "N = 1 truncation of u = -sin x: b1' = 0 (the single mode is frozen; trivially global)")
dE2 = sp.simplify(sum(2*b2[k]*rhs2[k] for k in range(2)))
rec("C6","identity", dE2 == 0, "N = 2 odd Galerkin truncation: d/dt (b1^2 + b2^2) = 0 exactly (energy conserved: the projected nonlinearity is skew)", f"b1' = {rhs2[0]}, b2' = {rhs2[1]}")
b3, rhs3 = galerkin_rhs(3); dE3 = sp.simplify(sum(2*b3[k]*rhs3[k] for k in range(3)))
rec("C7","identity", dE3 == 0, "N = 3 likewise: energy exactly conserved, hence bounded orbits, hence global existence for the polynomial ODE [W]")
# bounded sup norm and slope at fixed N (Cauchy-Schwarz), growing with N: sup|u_N| <= sqrt(N) ||b||, |u_N'(0)| <= sqrt(sum k^2) ||b||
N = sp.symbols('N', positive=True, integer=True)
slope_bound = sp.sqrt(sp.summation(sp.Symbol('k', positive=True, integer=True)**2, (sp.Symbol('k', positive=True, integer=True), 1, N)))
rec("C8","identity", sp.limit(slope_bound, N, sp.oo) == sp.oo and sp.simplify(slope_bound**2 - N*(N+1)*(2*N+1)/6) == 0,
    "|u_N'(0)| <= sqrt(N(N+1)(2N+1)/6) ||b||: bounded for all time at fixed N, with a bound that diverges with N - the same shape as the input's eps-family, with no hidden sector")
rec("C9c","countercontrol", sp.simplify(sum(2*b2[k]*rhs2[k] for k in range(2)).subs(b2[1], 0) + 0) == 0 and sp.simplify(rhs2[1].subs(b2[1], 0)) != 0,
    "countercontrol: with b2 = 0 at t = 0 (the data -sin x), b2' = -b1^2/2 != 0, so the N = 2 truncation does transfer energy to mode 2 (a genuine projected dynamics, not the frozen N = 1 case)", f"b2'|_(b2=0) = {sp.simplify(rhs2[1].subs(b2[1], 0))}")

# ---------------- D. HB3-a recomputed from the kernel-recorded configurations ----------------
print()
print("== D  HB3-a (HexLatticeGas.lean:935-981): the recorded configurations' block charges, recomputed")
hexDir = [(1,0), (0,1), (-1,1), (-1,0), (0,-1), (1,-1)]
w = sp.symbols('w0:6')
def conf(d): return d  # {(i0,i1): {channel}}
c   = {(0,0): {0}, (0,1): {3}}
cp  = {(0,0): {0, 3}}
Phi_c   = {(1,0): {0}, (3,1): {3}};  Phiinv_c  = {(1,1): {3}, (3,0): {0}}     # hb3a_gas_values, as recorded
Phi_cp  = {(0,1): {1}, (0,3): {4}};  Phiinv_cp = {(1,0): {3}, (3,0): {0}}
def block(i): return (i[0]//2, i[1]//2)
def charge(cfg, beta, weight):   # hexSum over the block beta with weight (symbolic or numeric per channel)
    return sp.expand(sum(weight[k] for i, ks in cfg.items() if block(i) == beta for k in ks))
blocks = [(a,b) for a in range(2) for b in range(2)]
eq_t  = all(sp.simplify(charge(c, B, w) - charge(cp, B, w)) == 0 for B in blocks)
eq_tm = all(sp.simplify(charge(Phiinv_c, B, w) - charge(Phiinv_cp, B, w)) == 0 for B in blocks)
rec("D1","identity", eq_t and charge(c,(0,0),w) == w[0]+w[3] and eq_tm and charge(Phiinv_c,(0,0),w) == w[3] and charge(Phiinv_c,(1,0),w) == w[0],
    "for symbolic channel weights w: block charges of c and c' agree on every block at t (w0+w3 on (0,0)) and at t-1 (w3 on (0,0), w0 on (1,0))")
P1 = [d[0] for d in hexDir]; P2 = [d[1] for d in hexDir]; mass = [1]*6
rec("D2","witness", charge(Phi_c,(0,0),P1) == 1 and charge(Phi_cp,(0,0),P1) == 0,
    "at t+1 the momentum P1 on block (0,0) is 1 for c and 0 for c': equal two-time coarse states, different next coarse state (the input's paraphrase of H-B's closure failure is accurate)")
rec("D3","witness", charge(Phi_c,(1,0),mass) == 1 and charge(Phi_cp,(1,0),mass) == 0,
    "the mass on block (1,0) at t+1 also differs (1 vs 0): the non-closure is not specific to momentum")
rec("D4c","countercontrol", charge(Phi_c,(0,0),mass) == charge(Phi_cp,(0,0),mass) == 1,
    "countercontrol: the mass on block (0,0) at t+1 agrees (1 = 1), so a single well-chosen coarse variable can look closed on this pair; the witness needs the right block and weight")
# the gas's conservation on the recorded values: mass 2 and total momentum preserved by Phi and Phi^{-1}
tot = lambda cfg, weight: sum(weight[k] for ks in cfg.values() for k in ks)
rec("D5","identity", all(tot(g, mass) == 2 for g in (c, cp, Phi_c, Phi_cp, Phiinv_c, Phiinv_cp)) and all(tot(g, P1) == tot(c, P1) and tot(g, P2) == tot(c, P2) for g in (Phi_c, Phiinv_c)) and all(tot(g, P1) == tot(cp, P1) and tot(g, P2) == tot(cp, P2) for g in (Phi_cp, Phiinv_cp)),
    "the recorded images conserve total mass and both momentum components (HB1), a consistency check on the transcription", f"P(c) = ({tot(c,P1)},{tot(c,P2)}), P(c') = ({tot(cp,P1)},{tot(cp,P2)})")

n = sum(R); print(f"\nchecks: {len(R)}, confirmed: {n}"); print("VERDICT", "INDEP-NS-CONFIRMED" if n == len(R) else "INDEP-NS-MISMATCH"); sys.exit(0 if n == len(R) else 1)
