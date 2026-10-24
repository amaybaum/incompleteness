"""Coordinator checks of the detector-boundary handoff v1 (independent code; standard library, fractions, mpmath).

K1  the all-frame bound: one-sided Chebyshev (Cantelli) P(Z <= -a) <= s^2/(s^2 + a^2) with s^2 = 9n/25, a = 4n/5 gives
    9/(16n + 9), and (13/16)(1 - 9/(16n + 9)) - 3/4 = (4n - 27)/(4(16n + 9)) (exact rational identity, n = 1..201);
    numerical evidence for irrational frames: P(W <= 0 | T = 1/(5n)) by exact enumeration over (S_y, S_z) at 30-digit
    precision for theta in {1, sqrt 2, pi/7, e/3} radians and n in {7, 15, 63}, against the bound.
K2  the full-record lower bound at n = 63, m = 256, recomputed from the per-trial probability of (S_x = n, D = 1).
K3  two-tick freshness of the pair-parity majority rule on the actual cubic geometry (5^3 torus): with the port's
    initial pair fixed, its six neighbours' initial pairs enumerated (2^12) and the second shell's current values
    fixed in 6 deterministic patterns, the port's next two values are i.i.d. fair, for each of the 4 port pairs.
K4  a propagation probe for the same rule (exploratory): every pattern of 1 to 3 ones in a 2 x 2 x 2 block as the
    current field, previous field zero or equal, on a 9^3 torus for 8 ticks; the largest distance reached by the
    support from the block.
"""
from fractions import Fraction as F
from math import comb
from itertools import product, combinations
import mpmath as mp

def K1():
    ok=True
    for n in range(1,202,2):
        s2=F(9*n,25); a=F(4*n,5)
        ok&= s2/(s2+a*a)==F(9,16*n+9)
        ok&= F(13,16)*(1-F(9,16*n+9))-F(3,4)==F(4*n-27,4*(16*n+9))
    mp.mp.dps=30; worst=None
    for n in (7,15,63):
        for th in (mp.mpf(1),mp.sqrt(2),mp.pi/7,mp.e/3):
            b=-mp.mpf(3)/5*mp.cos(th); c=mp.mpf(3)/5*mp.sin(th)
            neg=mp.mpf(0)
            for j in range(n+1):
                y=2*j-n
                for k in range(n+1):
                    z=2*k-n
                    if mp.mpf(4*n)/5+b*y+c*z<=0: neg+=comb(n,j)*comb(n,k)
            p=neg/mp.mpf(4)**n; bound=mp.mpf(9)/(16*n+9)
            ok&= p<=bound
            r=p/bound; worst=r if worst is None else max(worst,r)
    print('K1  Cantelli bound and gap identity exact for odd n <= 201; irrational frames (4 angles, n in {7,15,63}): P(W<=0 | T) <= 9/(16n+9) with largest ratio %s: %s'%(mp.nstr(worst,4),ok))
    return ok
def K2():
    n,m=63,256; M=1<<(9*n-1).bit_length()
    C=sum(5*x*comb(n,(x+n)//2) for x in range(1,n+1,2))
    p=F(C,M*2**n); c=1-(1-p)**m
    q0=F(1,M*2**n)                          # one trial: S_x = n (probability 2^-n) and D = 1 (1/M)
    first=c*q0/p                            # the first success carries that timestamp
    gap=first*F(4*n-27,4*(16*n+9))
    ok='%.12e'%float(gap)=='3.703827556461e-22' and first==c/C
    print('K2  full-record lower bound at n=63, m=256: %.12e (handoff 3.703827556461e-22); P(first success has T=1/(5n)) = c_m/C_n: %s'%(float(gap),ok))
    return ok
def lattice(side):
    sites=list(product(range(side),repeat=3)); nb={}
    for s in sites:
        row=[]
        for ax in range(3):
            for d in (-1,1):
                v=list(s); v[ax]=(v[ax]+d)%side; row.append(tuple(v))
        nb[s]=row
    return sites,nb
def fM(bits):
    px,py,pz=(bits[2*j]^bits[2*j+1] for j in range(3))
    return (px&py)^(py&pz)^(pz&px)
def K3():
    sites,nb=lattice(5); x=(0,0,0); N1=nb[x]
    shell=sorted({v for i in N1 for v in nb[i] if v!=x and v not in N1})
    patterns=[{v:0 for v in shell},{v:1 for v in shell}]
    for seed in (1,2,3,4):
        patterns.append({v:(hash((seed,v))>>3)&1 for v in shell})
    ok=True; n_cases=0
    for pat in patterns:
        for ox,cx in product((0,1),repeat=2):
            law={}
            for co in product((0,1),repeat=6):            # neighbours' current values
                cur={**pat,x:cx,**dict(zip(N1,co))}
                y1=fM(tuple(cur[v] for v in nb[x]))^ox
                for oo in product((0,1),repeat=6):        # neighbours' old values
                    nxt={i:fM(tuple(cur[v] for v in nb[i]))^o for i,o in zip(N1,oo)}
                    y2=fM(tuple(nxt[v] for v in N1))^cx
                    law[(y1,y2)]=law.get((y1,y2),0)+1
            ok&= set(law.values())=={2**10} and len(law)==4; n_cases+=1
    print('K3  pair-parity majority, 5^3 torus: (y1, y2) i.i.d. fair given the port pair, over 2^12 neighbour pairs, for %d (shell pattern, port pair) cases: %s'%(n_cases,ok))
    return ok
def K4():
    side=9; sites,nb=lattice(side); block=set(product((0,1),repeat=3))
    def dist(s):
        return sum(min(c,side-c) for c in s)
    best=(0,None); left=0; n=0
    for k in (1,2,3):
        for ones in combinations(sorted(block),k):
            for prev_mode in ('zero','equal'):
                cur={s:0 for s in sites}
                for o in ones: cur[o]=1
                prev=dict(cur) if prev_mode=='equal' else {s:0 for s in sites}
                far=0; out=False; n+=1
                for _ in range(8):
                    nxt={s:prev[s]^fM(tuple(cur[v] for v in nb[s])) for s in sites}
                    prev,cur=cur,nxt
                    sup=[s for s,v in cur.items() if v]
                    if any(s not in block for s in sup): out=True
                    if sup: far=max(far,max(dist(s) for s in sup))
                left+=out
                if far>best[0]: best=(far,(ones,prev_mode))
    print('K4  majority rule, 1-3 ones in the 2x2x2 block, previous zero or equal, 9^3 torus, 8 ticks: %d patterns; support leaves the block in %d; largest L1 distance from the origin %d'%(n,left,best[0]))
    return left
if __name__=='__main__':
    print(__doc__.strip().splitlines()[0])
    r=[K1(),K2(),K3()]; K4()
    print('coordinator positive checks:','green' if all(r) else 'RED')
