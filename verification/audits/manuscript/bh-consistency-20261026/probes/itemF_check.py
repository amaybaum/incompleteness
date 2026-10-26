# Independent exact-rational re-check of BH-01 item F (GR A.7 decoupling ordering).
# t_evap = 5120*pi*G^2*M^3/(hbar*c^4*Gamma)  [GR:849-851: alpha = hbar c^4 Gamma/(15360 pi G^2), t_evap = M0^3/(3 alpha)]
from fractions import Fraction as Fr
pi_lo, pi_hi = Fr(333,106), Fr(355,113)
# GM_sun (IAU 2015 nominal) = 1.3271244e20 m^3 s^-2 exactly (nominal); G CODATA 2018 6.67430(15)e-11
GMsun = Fr(13271244,10**5)*10**20/10**0  # 1.3271244e20
GMsun = Fr(13271244)*Fr(10)**13
G_lo, G_hi = Fr(667415,10**5)*Fr(10)**-11, Fr(667445,10**5)*Fr(10)**-11
hbar = Fr(1054571817,10**9)*Fr(10)**-34   # exact SI
c = Fr(299792458)
def tevap_bounds(M_lo, M_hi, Gam_lo, Gam_hi):
    # t = 5120 pi G^2 M^3 /(hbar c^4 Gamma); with M given as GM/G -> G^2 M^3 = (GM)^3 / G
    pass
# 30 M_sun: G^2 M^3 = (G M)^3 / G
GM = 30*GMsun
lo = 5120*pi_lo*GM**3/G_hi/(hbar*c**4*Fr(1000))
hi = 5120*pi_hi*GM**3/G_lo/(hbar*c**4*Fr(1,100))
tau_lo, tau_hi = Fr(10)**16, Fr(10)**19
r_lo, r_hi = lo/tau_hi, hi/tau_lo
def sci(x):
    import decimal
    decimal.getcontext().prec=8
    return str(decimal.Decimal(x.numerator)/decimal.Decimal(x.denominator))
print("30 Msun: t_evap/tau in [", sci(r_lo), ",", sci(r_hi), "]")
# Page time beta=1: t_P = (1-2^{-3/2}) t_evap ; lower bound 1-2^{-3/2} > 0.6464
print("t_P/tau >= ", sci(r_lo*Fr(6464,10000)))
# central reference: Gamma=1, tau=1e17, 1 Msun -> years
t1 = 5120*Fr(314159265,10**8)*GMsun**3/Fr(66743,10**4)/Fr(10)**-11/(hbar*c**4)
print("1 Msun, Gamma=1: t_evap [yr] ~", sci(t1/Fr(31557600)))
# mass at which t_evap = tau_B^D: worst cases. M^3 = tau*hbar c^4 Gamma/(5120 pi G^2)
import decimal
def cube_root(x):
    return float(x)**(1/3)
Mmin = cube_root(tau_lo*hbar*c**4*Fr(1,100)/(5120*pi_hi*G_hi**2))
Mmax = cube_root(tau_hi*hbar*c**4*Fr(1000)/(5120*pi_lo*G_lo**2))
print("t_evap = tau_B^D at M in [%.4g, %.4g] kg (float cube root)"%(Mmin,Mmax))
