# GR §6.3 / ch07 §7.7: rho_QFT/rho_classical ~ M_Pl^4/(H^2/G) = S_dS.  What is identity, what is input?
import sympy as sp
H,G,hbar,c,Lam = sp.symbols('H G hbar c Lambda_UV', positive=True)
lp2 = hbar*G/c**3
rho_crit = 3*H**2*c**2/(8*sp.pi*G)            # Friedmann, flat: TOTAL density, not the vacuum component
S_dS = sp.pi*(c/H)**2/lp2                      # A/(4 l_p^2), A = 4 pi (c/H)^2
rho_cut = hbar*c*(1/Lam)**-4 if False else hbar*c/Lam**4   # zero-point density with cutoff length Lambda_UV (order of magnitude, hbar c / L^4)
r = sp.simplify((rho_cut/rho_crit)/S_dS)
print("(rho_cut/rho_crit)/S_dS =", r)
print("  at cutoff length = l_p:", sp.simplify(r.subs(Lam, sp.sqrt(lp2))))
# numbers
vals={H:67.4e3/3.0857e22, G:6.674e-11, hbar:1.0546e-34, c:2.998e8}
print("S_dS(H0=67.4) = %.3e" % float(S_dS.subs(vals)))
print("rho_crit = %.3e J/m^3" % float(rho_crit.subs(vals)))
print("Planck-cutoff ratio rho_P/rho_crit = %.3e" % float((rho_cut/rho_crit).subs(Lam,sp.sqrt(lp2)).subs(vals)))
# The identity is dimensional: (cutoff energy density)/(H^2/G) = (L_H/l_cut)^2 * (l_p/l_cut)^2 ; equals S_dS only for l_cut ~ l_p.
print("Omega_Lambda is not fixed by rho ~ H^2/G: any Omega_L in (0,1) gives rho_L ~ H^2/G; observed ~0.69 is an input.")
