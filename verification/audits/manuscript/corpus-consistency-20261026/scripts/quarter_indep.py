# Independent re-derivation of the Bekenstein-Hawking coefficient under GR §3-§5's calibration.
# Written from GR.md text (687e885b), not from S/paper/apps/quarter.py.
# Route: hold the MEASURED hbar fixed and ask what the calibration T_cl = T_Q imposes on the
# mode density; then compute S/A in units of 1/l_p^2. Separate controls and countercontrols.
import sympy as sp
from fractions import Fraction
import random

c, G, hbar, kappa, A, eps, sigma, a, b, km = sp.symbols('c G hbar kappa A epsilon sigma a b kappa_m', positive=True)
lp2 = hbar*G/c**3                       # Planck area, with hbar the measured constant

def coefficient(eta, a_=a, b_=b):
    """Return S/(A/l_p^2) after imposing the calibration.
    first law: dE = c^2 kappa/(a G) dA   (GR: a = 8 pi)
    KMS:       k_B T_Q = hbar kappa/(b c) (GR: b = 2 pi)
    entropy:   dS = eta dA (nats)
    T_cl = (dE/dA)/(dS/dA). The calibration T_cl = T_Q is one equation; solve it for hbar
    (GR's reading: hbar output) and separately for eta (measured-hbar reading)."""
    Tcl = (c**2*kappa/(a_*G))/eta
    TQ = hbar*kappa/(b_*c)
    calib = sp.Eq(Tcl, TQ)
    hb = sp.solve(calib, hbar)
    assert len(hb) == 1
    S_over = sp.simplify((eta*A)/(A/lp2.subs(hbar, hb[0])))
    return S_over, calib

# (1) GR's own density eta = sigma/eps^2 with kappa_m: eta = km*sigma/eps^2
r1, calib = coefficient(km*sigma/eps**2)
print("1. S/(A/lp^2) =", r1, "| depends on eps,sigma,km:", r1.has(eps, sigma, km))
print("   at GR constants a=8pi, b=2pi:", r1.subs({a: 8*sp.pi, b: 2*sp.pi}))
# (2) measured-hbar reading: solve the calibration for eta
eta_s = sp.Symbol('eta', positive=True)
_, cal2 = coefficient(eta_s)
eta_sol = sp.solve(cal2, eta_s)[0]
print("2. calibration forces eta =", sp.simplify(eta_sol*lp2), "/ l_p^2  (GR consts:",
      sp.simplify((eta_sol*lp2).subs({a: 8*sp.pi, b: 2*sp.pi})), ")")
eps_sol = sp.solve(sp.Eq(sigma/eps**2, eta_sol.subs({a: 8*sp.pi, b: 2*sp.pi})), eps)
print("   => eps =", [sp.simplify(e/sp.sqrt(lp2)) for e in eps_sol], "* l_p  (only eps/sqrt(sigma) fixed)")
# (3) arbitrary positive function of eps, sigma: coefficient is still b/a (identity in eta)
f = sp.Function('f', positive=True)(eps, sigma)
r3, _ = coefficient(f)
print("3. arbitrary eta=f(eps,sigma):", r3)
# (4) exact rational spot checks (no floating point): random eta values
random.seed(1)
vals = set()
for _ in range(50):
    q = sp.Rational(random.randint(1, 10**9), random.randint(1, 10**9))
    r, _ = coefficient(q/eps**2)
    vals.add(sp.nsimplify(r.subs({a: 8*sp.pi, b: 2*sp.pi})))
print("4. 50 random rational mode densities give coefficient set:", vals)
# (5) countercontrol: change either normalisation and the coefficient moves (the test is not vacuous)
print("5. a=16pi ->", r1.subs({a: 16*sp.pi, b: 2*sp.pi}), "; b=pi ->", r1.subs({a: 8*sp.pi, b: sp.pi}))
# (6) countercontrol: WITHOUT the calibration, the count alone with eps fixed independently
#     (e.g. eps = l_p, sigma = 1) gives S = A/l_p^2, not A/4l_p^2: the count by itself does not carry 1/4
S_nocal = (sigma*A/eps**2).subs({eps: sp.sqrt(lp2), sigma: 1})/(A/lp2)
print("6. no calibration, eps=l_p, sigma=1: S/(A/lp^2) =", S_nocal)
# (7) Hawking route, no mode count: dS/dA = (dE/dA)/T_H
dSdA = (c**2*kappa/(a*G))/(hbar*kappa/(b*c))
print("7. Hawking route dS/dA * l_p^2 =", sp.simplify(dSdA*lp2), "-> GR consts:", sp.simplify((dSdA*lp2).subs({a: 8*sp.pi, b: 2*sp.pi})))
# (8) the boxed hbar of GR §3.2 is reproduced (control that inputs are transcribed faithfully)
hb_box = sp.solve(calib, hbar)[0].subs({a: 8*sp.pi, b: 2*sp.pi, km: 1})
print("8. hbar =", sp.simplify(hb_box), " matches GR box c^3 eps^2/(4 G sigma):",
      sp.simplify(hb_box - c**3*eps**2/(4*G*sigma)) == 0)
