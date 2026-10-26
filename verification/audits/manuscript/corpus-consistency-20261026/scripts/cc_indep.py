# Independent check of GR §6.1/§6.3: (a) rho ~ H^2/G is the Friedmann total-density normalisation;
# (b) rho_cut/rho_crit vs S_dS is a dimensional identity; numbers at H0=67.4 km/s/Mpc (Planck 2018).
import sympy as sp
c,G,hb,H,eps,k = sp.symbols('c G hbar H epsilon k', positive=True)
lp = sp.sqrt(hb*G/c**3)
rho_crit = 3*H**2*c**2/(8*sp.pi*G)                     # energy density, Friedmann, flat, TOTAL
S_dS = sp.pi*(c/H)**2/lp**2                            # A/(4 l_p^2), A = 4 pi (c/H)^2
rho_P = hb*c/lp**4                                     # Planck energy density, cutoff at l_p
print("(rho_P/rho_crit)/S_dS =", sp.simplify(rho_P/rho_crit/S_dS))
rho_eps = hb*c/eps**4
print("cutoff at eps: (rho_eps/rho_crit)/S_dS =", sp.simplify(rho_eps/rho_crit/S_dS), "; at eps=2 l_p:", sp.simplify((rho_eps/rho_crit/S_dS).subs(eps,2*lp)))
# explicit zero-point sum: rho_zp = int_0^{1/eps} (1/2) hbar c k * 4 pi k^2 dk/(2pi)^3 = hbar c/(16 pi^2 eps^4)
rho_zp = sp.integrate(sp.Rational(1,2)*hb*c*k*4*sp.pi*k**2/(2*sp.pi)**3,(k,0,1/eps))
print("zero-point sum / (hbar c/eps^4) =", sp.simplify(rho_zp/(hb*c/eps**4)), "; (rho_zp/rho_crit)/S_dS at eps=2 l_p:", sp.nsimplify(sp.simplify((rho_zp/rho_crit/S_dS).subs(eps,2*lp))))
# H-dependence: any component with Omega = O(1) scales as H^2/G; the ratio to S_dS is H-free
print("H appears in (rho_P/rho_crit)/S_dS:", sp.simplify(rho_P/rho_crit/S_dS).has(H))
# numbers
vals = {c:299792458, G:6.67430e-11, hb:1.054571817e-34, H:67.4e3/3.0856775814913673e22}
print("rho_crit [J/m^3] = %.3e" % float(rho_crit.subs(vals)))
print("Omega_L*rho_crit [J/m^3] (Omega_L=0.685) = %.3e" % (0.685*float(rho_crit.subs(vals))))
print("S_dS = %.3e ; rho_P/rho_crit = %.3e" % (float(S_dS.subs(vals)), float((rho_P/rho_crit).subs(vals))))
