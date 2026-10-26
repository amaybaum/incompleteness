# How many "simple" closed forms land within 1 sigma of lambda = 0.22500 +- 0.00067 (PDG 2022 global fit, as cited at SM §7.1)?
# Family: (a/b) * pi^k * sqrt(r)^s, a,b in 1..12, k in {-2,-1,0,1}, r in {1,2,3,5,6}, s in {-1,1}
from fractions import Fraction
import math, itertools
lam, sd = 0.22500, 0.00067
hits=set()
for a,b in itertools.product(range(1,13),repeat=2):
    if math.gcd(a,b)!=1: continue
    for k in (-2,-1,0,1):
        for r in (1,2,3,5,6):
            for s in ((1,) if r==1 else (-1,1)):
                v = a/b * math.pi**k * math.sqrt(r)**s
                if abs(v-lam) <= sd:
                    hits.add((round(v,6), f"({a}/{b})*pi^{k}*sqrt({r})^{s}"))
for h in sorted(hits): print(h)
print("count within 1 sigma:", len(hits))
# total distinct values in family within [0.1,0.5] for density estimate
vals=set()
for a,b in itertools.product(range(1,13),repeat=2):
    if math.gcd(a,b)!=1: continue
    for k in (-2,-1,0,1):
        for r in (1,2,3,5,6):
            for s in ((1,) if r==1 else (-1,1)):
                v=a/b*math.pi**k*math.sqrt(r)**s
                if 0.1<=v<=0.5: vals.add(round(v,9))
print("family size in [0.1,0.5]:", len(vals), " expected hits in a 2-sigma window by uniform density:", round(len(vals)*2*sd/0.4,2))
print("1/(pi*sqrt2) =", 1/(math.pi*math.sqrt(2)))
