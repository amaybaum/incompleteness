"""Exact native readiness-flag boundary checks. Standard library; stdout only."""
from collections import Counter
from fractions import Fraction as Q
from itertools import product
from random import Random

DIRS=((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1))

def require(ok,label):
    if not ok: raise RuntimeError(label)

def degree(table):
    coefficients=list(table)
    n=(len(table)-1).bit_length()
    for i in range(n):
        for mask in range(1<<n):
            if mask>>i&1:coefficients[mask]^=coefficients[mask^(1<<i)]
    return max((mask.bit_count() for mask,v in enumerate(coefficients) if v),default=-1)

def polynomial_checks():
    # Complete census of degree <=2 functions on three variables.
    monomials=[0,1,2,4,3,5,6]
    ready=[int(x==0) for x in range(8)]
    require(degree(ready)==3,'three-bit readiness degree')
    distances=Counter()
    for coefficients in range(128):
        table=[]
        for x in range(8):
            value=0
            for j,mask in enumerate(monomials):
                if coefficients>>j&1 and (x&mask)==mask:value^=1
            table.append(value)
        require(degree(table)<=2,'quadratic census')
        distances[sum(a!=b for a,b in zip(table,ready))]+=1
    require(distances==Counter({1:8,3:56,5:56,7:8}),'quadratic distance distribution')
    # Eight single-error tables attain minimax error 1/8 as an abstract mixture.
    neighbors=[]
    for error_vertex in range(8):
        table=list(ready);table[error_vertex]^=1
        require(degree(table)<=2,'single-error quadratic')
        neighbors.append(table)
    require(all(sum(t[x]!=ready[x] for t in neighbors)==1 for x in range(8)),
            'abstract randomized tightness')
    for J in range(1,13):
        require(degree([int(x==0) for x in range(1<<J)])==J,'J-bit readiness degree')
    print('Polynomial PASS: all 128 quadratic tables; readiness distances {1:8,3:56,5:56,7:8}')
    print('Degree PASS: J=1..12; abstract randomized worst-case bound 1/8 is tight')

def shift(field,L):
    out=set()
    for x in field:
        for d in DIRS:
            y=tuple((a+b)%L for a,b in zip(x,d))
            if y in out:out.remove(y)
            else:out.add(y)
    return out

def step(old,cur,L):
    a,b,d=cur;ao,bo,do=old
    sa,sb,sd=[shift(f,L) for f in cur]
    return [sa^ao,sb^bo,sd^do^shift(a&b,L)^(sa&sb)^(sa&bo)^(sb&ao)]

def raw_checks():
    L=25;K=3;q=(12,0,0);o=(0,0,0)
    def norm(x):return sum(min(v,L-v) for v in x)
    rng=Random(1716)
    checks=0
    for background in range(3):
        old=[set() for _ in range(3)];cur=[set() for _ in range(3)]
        if background:
            for phase,fields in enumerate((old,cur)):
                for f in range(3):
                    while len(fields[f])<8:
                        x=tuple(rng.randrange(L) for _ in range(3))
                        if norm(x)>K and x!=q:fields[f].add(x)
        snapshots=[]
        for bits in product((0,1),repeat=3):
            p=[set(f) for f in old];c=[set(f) for f in cur]
            for f,x in enumerate(((L-1,0,0),(1,0,0),o)):
                if bits[f]:c[f].add(x)
            # All other readiness coordinates are zero. E_0 iff these three bits vanish.
            ready=all(not f for f in (c[0]&{(L-1,0,0)},c[1]&{(1,0,0)},c[2]&{o}))
            require(ready==(bits==(0,0,0)),'readiness three-cube')
            records=[]
            for t in range(5):
                records.append([set(f) for f in c])
                if background==0 and t==1:
                    require(int(o in c[2])==bits[0]*bits[1],'working two-input AND control')
                p,c=c,step(p,c,L)
            snapshots.append(records)
        for t in range(5):
            for f in range(3):
                derivative=set()
                for record in snapshots:derivative^=record[t][f]
                require(not derivative,'third difference of every raw output bit')
                checks+=1
    print('Raw-rule PASS:',checks,'whole-field third differences on the actual 25^3 torus')
    print('Positive control PASS: native two-input AND at the receiver; three-input readiness has odd parity')

def prepared_checks():
    for K in (1,2,3):
        m=2+3*K;counts=Counter();totals=Counter()
        # An arbitrary, strongly nonuniform complement, independent of uniform frontiers.
        for y,weight in enumerate((1,2,5,0)):
            for z in range(1<<m):
                w=y%3
                out=(z^(z<<1)^y)&((1<<m)-1)
                counts[w,out]+=weight;totals[w]+=weight
        require(all(counts[w,out]*(1<<m)==total for w,total in totals.items()
                    for out in range(1<<m)),'prepared-prior fiber bijection')
    # A copy does not alter a fair bit but discloses it completely.
    law=Counter((z,z) for z in (0,1))
    require(law[(0,1)]==law[(1,0)]==0,'copy leakage')
    print('Prepared-prior mechanism PASS: K=1,2,3; copy-to-record countercontrol reveals untouched bit')

def review_bound():
    b1=Q(1,2**117)
    b2=b1+Q(1,2**174)-Q(1,2**234)
    require(b2>b1 and b2<b1+Q(1,2**174),'strict TV correction')
    print('Review correction PASS: w=2 TV ceiling is 2^-117 + 2^-174 - 2^-234 > 2^-117')

def main():
    polynomial_checks();raw_checks();prepared_checks();review_bound()
    print('PASS: restricted raw-flag obstruction; no general apparatus or OI no-go')

if __name__=='__main__':main()
