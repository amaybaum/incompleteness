import sympy as sp
# --- 1/4: GR Step 4 exactly as written (GR:148): k_B T_cl = c^2 eps^2 kappa/(8 pi G sigma); T_Q = hbar kappa/(2 pi c k_B)
c,G,hb,ka,eps,sig,A,kB,a,b = sp.symbols('c G hbar kappa epsilon sigma A k_B a b',positive=True)
kTcl = c**2*eps**2*ka/(a*G*sig)          # a = 8 pi in GR
kTQ  = hb*ka/(b*c)                        # b = 2 pi in GR
# Where does kTcl come from? dE/dS with dE = c^2 kappa dA/(aG), dS = sigma dA/eps^2 (in k_B units)
assert sp.simplify(kTcl - (c**2*ka/(a*G))/(sig/eps**2))==0
sol = sp.solve(sp.Eq(kTcl,kTQ), eps**2/sig)  # solve for the only combination fixed
print("calibration fixes eps^2/sigma =", sol)
r = sp.solve(sp.Eq(kTcl,kTQ), hb)[0]
print("hbar =", sp.simplify(r), " GR:", sp.simplify(r.subs({a:8*sp.pi,b:2*sp.pi})))
lp2 = hb*G/c**3
Scount = sig*A/eps**2
# impose calibration by eliminating eps^2
Scal = Scount.subs(eps, sp.sqrt(sig*sol[0])) if False else sp.simplify(Scount.subs(eps**2, sp.solve(sp.Eq(kTcl,kTQ),eps**2)[0]))
coef = sp.simplify(Scal/(A/lp2))
print("S_count/(A/l_p^2) after calibration =", coef, "-> GR:", coef.subs({a:8*sp.pi,b:2*sp.pi}), "free of sigma:", not coef.has(sig))
# Hawking route with no count: dS = dE/T_Q
dS = (c**2*ka/(a*G))/kTQ
print("Hawking route dS/dA * l_p^2 =", sp.simplify(dS*lp2).subs({a:8*sp.pi,b:2*sp.pi}))
# countercontrol: a mismatched count without calibration (sigma, eps free; hbar fixed) is NOT 1/4 in general
print("uncalibrated S/(A/l_p^2) =", sp.simplify(Scount/(A/lp2)))
# --- 10^122 identity
H,l = sp.symbols('H l_cut',positive=True)
rho_cut = hb*c/l**4
rho_crit = 3*H**2*c**2/(8*sp.pi*G)
SdS = sp.pi*(c/H)**2/lp2
print("(rho_cut/rho_crit)/S_dS =", sp.simplify((rho_cut/rho_crit)/SdS), " (lp^4/l^4 * 8/3 expected):", sp.simplify((rho_cut/rho_crit)/SdS - sp.Rational(8,3)*lp2**2/l**4)==0)
# mode-sum version: rho = (1/2) hbar c * int d^3k/(2pi)^3 k up to 1/l = hbar c /(16 pi^2 l^4)
k=sp.symbols('k',positive=True)
rho_ms = sp.Rational(1,2)*hb*c*sp.integrate(4*sp.pi*k**2*k,(k,0,1/l))/(2*sp.pi)**3
print("mode-sum rho =", sp.simplify(rho_ms), " factor vs S_dS:", sp.simplify((rho_ms/rho_crit)/SdS*l**4/lp2**2))
vals={H:67.4e3/3.0857e22,G:6.674e-11,hb:1.0546e-34,c:2.998e8}
lp=sp.sqrt(lp2)
for name,rho in [("hbar c/l_p^4",rho_cut),("mode sum",rho_ms)]:
    R=float((rho/rho_crit).subs(l,lp).subs(vals)); print(name, "rho/rho_crit=%.2e  rho/rho_Lambda(0.685)=%.2e"%(R,R/0.685))
print("S_dS=%.3e"%float(SdS.subs(vals)))
