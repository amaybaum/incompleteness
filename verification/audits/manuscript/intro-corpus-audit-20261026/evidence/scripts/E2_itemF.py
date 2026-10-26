#!/usr/bin/env python3
"""E2: independent rational-interval recomputation of BH-01 item F (GR A.7 decoupling arithmetic).
t_evap = 5120 pi G^2 M^3 / (hbar c^4 Gamma) = 10240 pi^2 (GM)^3 / (G h c^4 Gamma), with h and c
exact (SI 2019), CODATA 2018 G = 6.67430(15)e-11, IAU 2015 nominal GM_sun = 1.3271244e20 m^3 s^-2,
pi in [333/106, 355/113], Gamma in [1/100, 1000], tau_B^D in [1e16, 1e19] s (BH-01 REPORT:221-224).
Every bound is a Fraction; floats are used only to print.

Usage: python3 -I E2_itemF.py [out.json]
"""
import json, os, sys
from fractions import Fraction as F

h = F(662607015, 10**42)
c = F(299792458)
G_lo, G_hi = F(667415, 10**16), F(667445, 10**16)
GMsun = F(13271244) * 10**13
pi_lo, pi_hi = F(333, 106), F(355, 113)
gam_lo, gam_hi = F(1, 100), F(1000)
tau_lo, tau_hi = F(10**16), F(10**19)
M30 = 30

def t_evap(GM, G, pi, gam):
    return 10240 * pi * pi * GM**3 / (G * h * c**4 * gam)

t_min = t_evap(M30 * GMsun, G_hi, pi_lo, gam_hi)
t_max = t_evap(M30 * GMsun, G_lo, pi_hi, gam_lo)
ratio_lo, ratio_hi = t_min / tau_hi, t_max / tau_lo

# mass in kg at which t_evap = tau: M^3 = tau G h c^4 Gamma / (10240 pi^2 G^3) with GM = G M
def cube_root_bounds(x, lo, hi, it=200):
    for _ in range(it):
        mid = (lo + hi) / 2
        if mid**3 < x:
            lo = mid
        else:
            hi = mid
    return lo, hi
def m3(tau, G, pi, gam):
    return tau * h * c**4 * gam / (10240 * pi * pi * G**2)
Mlo3 = m3(tau_lo, G_hi, pi_hi, gam_lo)
Mhi3 = m3(tau_hi, G_lo, pi_lo, gam_hi)
Mlo = cube_root_bounds(Mlo3, F(1), F(10**14), 120)[0]
Mhi = cube_root_bounds(Mhi3, F(1), F(10**14), 120)[1]

# reference control: 1 M_sun, Gamma = 1, in years (Julian year)
yr = F(36525 * 86400, 100)
ref = (t_evap(GMsun, G_hi, pi_lo, F(1)) / yr, t_evap(GMsun, G_lo, pi_hi, F(1)) / yr)

out = {"ratio_30Msun": [float(ratio_lo), float(ratio_hi)],
       "ratio_30Msun_claim": ["1.785e57 (truncated)", "1.786e65 (rounded up)"],
       "ratio_lo_ge_1.785e57": ratio_lo >= F(1785, 1000) * 10**57,
       "ratio_hi_le_1.786e65": ratio_hi <= F(1786, 1000) * 10**65,
       "ratio_lo_lt_1.786e57": ratio_lo < F(1786, 1000) * 10**57,
       "ratio_hi_gt_1.785e65": ratio_hi > F(1785, 1000) * 10**65,
       "crossing_mass_kg": [float(Mlo), float(Mhi)],
       "crossing_claim_kg": ["1.059e10", "4.918e12"],
       "crossing_lo_ge_1.059e10": Mlo >= F(1059, 1000) * 10**10,
       "crossing_hi_le_4.918e12": Mhi <= F(4918, 1000) * 10**12,
       "reference_1Msun_gamma1_yr": [float(ref[0]), float(ref[1])],
       "reference_in_[2.0,2.2]e67": ref[0] >= 2 * F(10)**67 and ref[1] <= F(22, 10) * F(10)**67}
js = json.dumps(out, indent=1)
if len(sys.argv) > 1:
    if os.path.abspath(sys.argv[1]) == os.path.abspath(__file__):
        sys.exit("refusing to overwrite this script")
    open(sys.argv[1], "w").write(js + "\n")
print(js)
