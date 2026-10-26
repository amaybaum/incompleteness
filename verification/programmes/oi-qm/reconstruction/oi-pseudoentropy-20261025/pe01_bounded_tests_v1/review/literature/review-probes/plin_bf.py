# Independent brute force (distribution comparison, not rank): plin_m2 K1 K_zero on G_lin(p), n=5.
from itertools import product
from collections import Counter
def rec(p,n,K,x0,h):
    cm=p&((1<<n)-1); X=[x0]; x=x0
    for t in range(K):
        par=bin(h&cm).count('1')&1; h=(h>>1)|(par<<(n-1)); x^=h&1; X.append(x)
    return X
def gl2():
    out=[]
    for a,b,c,d in product((0,1),repeat=4):
        if (a*d+b*c)%2==1: out.append(((a,b),(c,d)))
    return out
def filt(A,bv,X,K):
    v=(0,0)
    for t in range(K):
        x=X[t]; v=((A[0][0]*v[0]+A[0][1]*v[1]+x*bv[0])%2,(A[1][0]*v[0]+A[1][1]*v[1]+x*bv[1])%2)
    return v+(X[K],)
def kzero(p,n,Kmax):
    obs=[(A,bv) for A in gl2() for bv in product((0,1),repeat=2)]
    for K in range(Kmax+1):
        recsP=[rec(p,n,K,x0,h) for x0 in (0,1) for h in range(1<<n)]
        recsQ=[list(r) for r in product((0,1),repeat=K+1)]
        for A,bv in obs:
            P=Counter(filt(A,bv,X,K) for X in recsP); Q=Counter(filt(A,bv,X,K) for X in recsQ)
            nP=len(recsP); nQ=len(recsQ)
            keys=set(P)|set(Q)
            if any(P[k]*nQ!=Q[k]*nP for k in keys): return K-1
    return None
print('G_lin n=5 plin_m2 K_zero', kzero(0b100101,5,16))
print('G_lin_sib n=5 plin_m2 K_zero', kzero(0b101001,5,16))
