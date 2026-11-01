"""Reviewer: 20a+44b decomposition and independent actual-L geometry. python3 -I -B arith_geom.py"""
from fractions import Fraction
nn = {(0,0):5,(0,1):0,(1,0):4,(1,1):1}
for s in (0,1):
    t1 = [nn[(y^s, r^s)] for y in (0,1) for r in (0,1) for z in (0,1)]
    t0 = [8-c for c in t1]
    # minimal positive multiplier c with all c*t integer
    def minmult(t):
        nz = [x for x in t if x]
        from math import gcd
        g = 0
        for x in nz: g = gcd(g, x)
        return Fraction(1, g)
    print('s', s, 't1', t1, 't0', t0, 'min multipliers', minmult(t1), minmult(t0))
    sols = [(a, b) for a in range(0, 5) for b in range(0, 3) if 20*a + 44*b == 64]
    print('  integer (a,b) with 20a+44b=64:', sols)
    # Also: a class with counts c*t1 for rational c: c must be integer since t1 contains 1
# actual geometry, my own formulation
T=185; P=12*840**185; S=P+T; R=S+68; L=R+9; H2=2*L
q9=(0,S,77)
ports=[(0,T,0),(0,0,-8*T),(T,P,0),(-T,P,0),(4*T,P,0),(0,S,0),(12*R,0,0),(48*L,0,0)]
dl=[T,T,S,S,S,S,R,L]; ax=[1,2,1,1,1,1,0,0]; sg=[-1,-1,1,1,1,1,-1,1]
def first_tail(site):
    best=None
    for i in range(8):
        lo, hi = max(dl[i], L)+1, H2
        # position along axis: ports[i][ax]+sg*t, t in [lo,hi]; nearest to site[ax]
        a=ports[i][ax[i]]; target=site[ax[i]]
        tstar = (target-a)*sg[i]   # t at which coordinate equals target
        t = min(max(tstar, lo), hi)
        d = abs(a+sg[i]*t-target) + sum(abs(ports[i][k]-site[k]) for k in range(3) if k!=ax[i])
        best = d if best is None else min(best, d)
    return best - L
def ball(r): return [(x,y,z) for x in range(-r,r+1) for y in range(-r,r+1) for z in range(-r,r+1) if abs(x)+abs(y)+abs(z)<=r]
reg = ball(4)
ft = [first_tail(tuple(q+o for q,o in zip(q9,x))) for x in reg]
print('region offsets', len(reg), 'first tail min/max', min(ft), max(ft))
named={'q8':(0,0,-1),'q10':(0,0,1),'m':(-1,0,0),'q9':(0,0,0),'q9+x':(1,0,0),'q9-y':(0,-1,0),'q9+y':(0,1,0)}
print({k: first_tail(tuple(q+o for q,o in zip(q9,x))) for k,x in sorted(named.items())})
srcA=[(-(L+1),S,76),(-(L+1),S,78),(-(L+2),S,77)]
n=6; srcS=[(-(n+1),0,-1),(-(n+1),0,1),(-(n+2),0,0)]
d=lambda a,b: sum(abs(p-q) for p,q in zip(a,b))
gA=[min(d(f,tuple(q+o for q,o in zip(q9,x))) for f in srcA)-L for x in reg]
gS=[min(d(f,x) for f in srcS)-n for x in reg]
print('G arrival min actual-L', min(gA), 'mapping equal on all', gA==gS)
# which port gives the first tail arrival
