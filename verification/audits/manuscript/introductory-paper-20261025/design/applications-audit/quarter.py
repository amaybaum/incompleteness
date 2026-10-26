# Is the Bekenstein-Hawking 1/4 an output or a calibration identity? (GR §3.1, §3.2 Step 4, §4, §5)
import sympy as sp
c,G,hbar,kappa,A,eps,sigma,kB,k8,kQ,eta = sp.symbols('c G hbar kappa A epsilon sigma k_B k8 kQ eta', positive=True)
# Inputs exactly as GR states them, with the two normalisation constants left symbolic:
#  first law (Jacobson / Einstein-eq prefactor): dE = c^2 kappa/(k8*G) dA      (GR uses k8 = 8*pi)
#  KMS/Gibbons-Hawking temperature:             kB T_Q = hbar kappa/(kQ*c)     (GR uses kQ = 2*pi)
#  entropy density (mode count):                dS = eta dA, eta = sigma/eps^2 (sigma, eps free)
TQ = hbar*kappa/(kQ*c*kB)
Tcl = (c**2*kappa/(k8*G))/(kB*eta)          # T_cl = dE/dS
hb = sp.solve(sp.Eq(Tcl,TQ), hbar)[0]       # calibration T_cl = T_Q -> hbar(eps,sigma)
print("hbar from calibration:", sp.simplify(hb.subs(eta, sigma/eps**2)))
lp2 = hbar*G/c**3
S = eta*A
ratio = sp.simplify((S/(A/lp2)).subs(hbar, hb))
print("S / (A/l_p^2) after calibration:", ratio, "  (eta, sigma, eps cancel:", not ratio.has(eta,sigma,eps),")")
print("with GR's constants:", ratio.subs({k8:8*sp.pi,kQ:2*sp.pi}))
# Control 1: change the first-law prefactor (e.g. a different gravitational coupling normalisation) -> coefficient moves
print("countercontrol k8=16*pi:", ratio.subs({k8:16*sp.pi,kQ:2*sp.pi}))
# Control 2: any eta whatsoever gives 1/4 -> the count does not constrain the coefficient
for e in [1/eps**2, 7/eps**2, sp.Rational(1,10**12)/eps**2]:
    r = sp.simplify((e*A/(A/lp2)).subs(hbar, hb.subs(eta,e)))
    print(" eta =",e," ->",r.subs({k8:8*sp.pi,kQ:2*sp.pi}))
# Control 3: Jacobson 1995 direction: take hbar given, eta free; Einstein-eq coupling G_eff = c^3/(4 eta hbar) (k8/kQ form)
Geff = sp.solve(sp.Eq(Tcl.subs(G,sp.Symbol('Geff',positive=True)),TQ), sp.Symbol('Geff',positive=True))[0]
print("Jacobson G_eff:", sp.simplify(Geff.subs({k8:8*sp.pi,kQ:2*sp.pi})))
# Hawking 1975 route: first law dM c^2 = (c^2 kappa/(8 pi G)) dA with T_H = hbar kappa/(2 pi c kB) => dS = dE/T
dS_dA = sp.simplify((c**2*kappa/(k8*G))/(kB*TQ)*kB)   # entropy in units of k_B
print("Hawking-route dS/dA (no mode count at all):", sp.simplify(dS_dA.subs({k8:8*sp.pi,kQ:2*sp.pi})*lp2))
