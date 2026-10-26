"""Does the invalid variant T >= 1 - BC^(2n) get violated by exact memoryless TV (k=1)? Float BC fine for a probe;
exact TV via integers. Usage: python3 -I -B pow_probe.py"""
import math
from fractions import Fraction as F
from math import comb
def tv(p, h):
    D = 5 * p.denominator; pn = p.numerator * 5; qn = 4 * p.denominator
    return F(sum(comb(h, i) * abs(pn**i * (D-pn)**(h-i) - qn**i * (D-qn)**(h-i)) for i in range(h+1)), 2 * D**h)
for p, H in ((F(7, 8), 400), (F(13, 16), 2600), (F(3, 4), 400)):
    bc = math.sqrt(float(p) * 0.8) + math.sqrt((1 - float(p)) * 0.2)
    viol = [h for h in range(1, H, 7 if H > 1000 else 1) if float(tv(p, h)) < 1 - bc ** (2 * h) - 1e-12]
    ok1 = all(float(tv(p, h)) >= 1 - bc ** h - 1e-12 for h in range(1, H, 37))
    print(str(p), 'violations of 1-BC^(2h):', viol[:5], len(viol), 'valid 1-BC^h sampled:', ok1)
