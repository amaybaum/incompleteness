from fractions import Fraction as Fr
import math
G=6.67430e-11; hbar=1.054571817e-34; c=299792458.0; Msun=1.98892e30
H0_kmsMpc=67.7; Mpc=3.0856775814913673e22
H=H0_kmsMpc*1e3/Mpc
print("1/H [s] =", 1/H)
# standard photon-only Hawking estimate: t = 5120 pi G^2 M^3/(hbar c^4)
def t_std(M): return 5120*math.pi*G**2*M**3/(hbar*c**4)
# Page 1976: massless (photons+gravitons+3 nu): t ~ 8.66e-27 (M/g)^3 s for M>>1e17 g ; photons+gravitons only: 2.66e-? use Page's coefficient alpha= 3.8e-5? use Page: dM/dt=-alpha hbar c^4/(G^2 M^2), alpha~2.011e-4 (neutrinos+photons+gravitons), 3.8e-5 photons+gravitons? compute range
for name,a in [("Page photons+gravitons alpha=3.8e-5 (approx)",3.8e-5),("Page incl 3 nu alpha=2.011e-4",2.011e-4)]:
    def t(M,a=a): return G**2*M**3/(3*a*hbar*c**4)
    print(name, "t(30Msun) =", t(30*Msun))
M=30*Msun
te=t_std(M)
print("photon-only std t_evap(30Msun) [s] =", te, " years:", te/3.156e7)
for tauD in [1e17, 1/H, 4.35e17, 1e18]:
    print(" tauD=%.3g  ratio=%.3e  log10=%.2f"%(tauD, te/tauD, math.log10(te/tauD)))
# smallest ratio: use largest emission (alpha bigger -> shorter t). Upper bound alpha: if all SM species massless, greybody ~ maybe alpha up to ~1e-3. 
for a in [1e-3, 1e-2]:
    t=G**2*M**3/(3*a*hbar*c**4); print(" alpha=%g t=%.3e ratio vs 1e18 = %.3e"%(a,t,t/1e18))
# crossover mass where t_evap = tauD (photon-only std formula)
for tauD in [1e17,1/H]:
    Mx=(tauD*hbar*c**4/(5120*math.pi*G**2))**(1/3); print("crossover M (std) for tauD=%.3g: %.3e kg"%(tauD,Mx))
# t_P = 0.646 t_evap
print("t_P/tauD (1e17):", 0.6464*te/1e17)
