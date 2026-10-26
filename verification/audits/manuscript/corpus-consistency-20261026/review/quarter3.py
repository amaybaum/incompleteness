# Third route, no sympy: (A) exact Fraction arithmetic with pi carried as a formal factor
# (a = a0*pi, b = b0*pi, so pi cancels exactly as a ratio of rationals); (B) SI floating
# evaluation of the framework chain for a real black hole by integrating dS = dE/T_cl over
# mass growth (Clausius route, classical temperature, no T_H used), then expressing in l_p
# with hbar from the calibration; (C) countercontrols.
from fractions import Fraction as F
import math, random
random.seed(7)
def coeff_exact(a0, b0, c, G, kap, eps, sig):
    # pi factors: first-law prefactor 1/(a0*pi), KMS 1/(b0*pi). Work with pi-stripped rationals.
    # T_cl = c^2 kap eps^2 /(a0 pi G sig);  T_Q = hbar kap/(b0 pi c)  => hbar = b0 c^3 eps^2/(a0 G sig)  (pi cancels)
    hbar = F(b0)*c**3*eps**2/(F(a0)*G*sig)
    lp2 = hbar*G/c**3
    S_per_A = sig/eps**2
    return S_per_A*lp2
out=set()
for _ in range(200):
    r=lambda: F(random.randint(1,10**6), random.randint(1,10**6))
    out.add(coeff_exact(8,2,r(),r(),r(),r(),r()))
print("A. exact, a=8pi b=2pi, 200 random rational (c,G,kappa,eps,sigma):", out)
print("A'. countercontrol a=8pi,b=pi:", {coeff_exact(8,1,F(3),F(5),F(7),F(11),F(13))}, " a=4pi,b=2pi:", {coeff_exact(4,2,F(3),F(5),F(7),F(11),F(13))})
# B: SI chain. hbar_meas fixed; calibration fixes eps for given sigma; integrate Clausius dS = c^2 dM / T_cl(M)
c=299792458.0; G=6.67430e-11; hb=1.054571817e-34
for sig in (math.log(2), 1.0, math.log(6)):
    eps = math.sqrt(4*G*hb*sig/c**3)          # calibration, hbar measured
    def Tcl(M):                                # k_B T_cl, classical (contains no hbar)
        kap = c**4/(4*G*M); return c**2*eps**2*kap/(8*math.pi*G*sig)
    M0, M1, n = 1e30, 3e31, 200000
    h=(M1-M0)/n; S=0.0
    for i in range(n):                         # midpoint rule
        M=M0+(i+0.5)*h; S+= c**2*h/Tcl(M)
    A=lambda M: 16*math.pi*G**2*M**2/c**4
    lp2=hb*G/c**3
    print("B. sigma=%.4f: Delta S_Clausius / (Delta A / l_p^2) = %.12f" % (sig, S/((A(M1)-A(M0))/lp2)))
# C: countercontrol on B: skip the calibration (eps = l_p) -> 1/sigma, not 1/4
eps=math.sqrt(hb*G/c**3); sig=1.0
print("C. no calibration eps=l_p, sigma=1: S/(A/l_p^2) =", sig/eps**2*(hb*G/c**3))
