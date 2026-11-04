# Independent check (no repo imports): B1 K0 and B3k K1 horizons on F_lin from the AGHP dichotomy vs brute force.
from fractions import Fraction as Fr
from itertools import combinations
from math import gcd

def polys_primitive(n):
    out=[]
    for c in range(1<<n):
        p=(1<<n)|c
        if not (p&1): continue
        # order of z mod p
        x=1; o=None
        for k in range(1,(1<<n)):
            x<<=1
            if x>>n &1: x^=p
            if x==1: o=k;break
        if o==(1<<n)-1: out.append(p)
    return out

def records(p,n,K):
    cm=p&((1<<n)-1); recs=[]
    for x0 in (0,1):
        for h in range(1<<n):
            X=[x0]; x=x0
            for t in range(K):
                par=bin(h&cm).count('1')&1
                h=(h>>1)|(par<<(n-1))
                x^=h&1; X.append(x)
            recs.append(X)
    return recs

def b1_adv(recs,T):
    c=sum(1 for X in recs if sum(X[t] for t in T)&1)
    return abs(Fr(c,len(recs))-Fr(1,2))

def horizons(curve,K):
    kz=None
    for k in range(K+1):
        if curve[k]!=0: break
        kz=k
    def first(d):
        for k in range(K+1):
            if curve[k]>=d: return k
    return kz,first(Fr(1,8)),first(Fr(1,4))

for n,Kmax in ((3,9),(4,11)):
    fam=polys_primitive(n)
    worst=[];avg=[]
    for K in range(Kmax+1):
        R=[records(p,n,K) for p in fam]
        bw=Fr(0); ba=Fr(0)
        for r in range(1,K+2):
            for T in combinations(range(K+1),r):
                a=[b1_adv(Rp,T) for Rp in R]
                bw=max(bw,min(a)); ba=max(ba,sum(a)/len(a))
        worst.append(bw); avg.append(ba)
    phi=sum(1 for k in range(1,(1<<n)) if gcd(k,(1<<n)-1)==1)
    print("n",n,"|F|",len(fam),"B1 K0-worst",horizons(worst,Kmax),"predicted K_zero=phi(2^n-1)=",phi,
          "| B1 K0-avg",horizons(avg,Kmax),"predicted K_zero=n=",n)

# B3k K1 on the primary p_n: least K where some 2-position parity is constant; predicted K_zero = 2^n - 2
P={3:0b1011,4:0b10011,5:0b100101,6:0b1000011}
for n,p in P.items():
    K=(1<<n)+1
    recs=records(p,n,K)
    first=None
    for b in range(1,K+1):
        for a in range(b):
            vals={X[a]^X[b] for X in recs}
            if len(vals)==1: first=b;break
        if first: break
    # also confirm no 1- or 3-position marginal is non-uniform before 'first' (odd parities involve x0)
    print("n",n,"B3k first constant 2-parity at K =",first,"-> K_zero",first-1,"predicted",(1<<n)-2)
