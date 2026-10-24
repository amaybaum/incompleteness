"""Coordinator checks of the native-wave handoff v1 (independent code; standard library and fractions only).

R1  light-cone recursion, written afresh: u_x(t) = alpha sum_{y~x} u_y(t-1) - u_x(t-2) (mod q), with u(-1), u(0) the
    initial variables, memoized over (site, t). One port on L = 9, q = 3, alpha = 1: conditional ranks and the
    frontier coefficient alpha^t of u_{x+t e1}(0) in u_x(t).
R2  generality of the one-port lemma: q in {3, 5, 7}, every nonzero alpha, L = 2K + 1, K = 3: full conditional rank.
R3  eight ports on L = 18 built directly on that torus (no translation from L = 9): disjoint supports, ranks 16 and 48.
R4  port separation probe (exploratory): two ports at axis distance d on L = 18, K = 4; joint conditional rank of
    their 8 future readings given their 4 initial readings.
R5  the first-success call law from i.i.d. uniform symbols: failure q^-n, P(wait k, mark d) = (q-1)/q^(k+1), for
    q in {3, 5}, n <= 3 (exact enumeration).
R6  pre-window history (gem-finding probe): give the observer the port readings u_x(-s), ..., u_x(0) of s earlier
    ticks (backward evolution of the same bijection); conditional rank of the K = 4 future readings, s = 0..6.
"""
from fractions import Fraction as F
from itertools import product
from functools import lru_cache

def rank_mod(rows,q):
    rows=[dict(r) for r in rows if r]; basis={}
    for r in rows:
        r={k:v%q for k,v in r.items() if v%q}
        while r:
            k=max(r)
            if k in basis:
                f=r[k]; b=basis[k]
                for kk,vv in b.items():
                    r[kk]=(r.get(kk,0)-f*vv)%q
                    if r[kk]==0: del r[kk]
            else:
                inv=pow(r[k],q-2,q); basis[k]={kk:vv*inv%q for kk,vv in r.items()}; break
    return len(basis)

def make(L,q,alpha):
    def nb(x):
        for a in range(3):
            for s in (1,-1):
                y=list(x); y[a]=(y[a]+s)%L; yield tuple(y)
    @lru_cache(maxsize=None)
    def u(x,t):
        if t==-1: return ((('P',x),1),)
        if t==0: return ((('C',x),1),)
        if t>0:
            acc={}
            for y in nb(x):
                for k,v in u(y,t-1): acc[k]=(acc.get(k,0)+alpha*v)%q
            for k,v in u(x,t-2): acc[k]=(acc.get(k,0)-v)%q
        else:   # backward: u(t-1) = alpha A u(t) - u(t+1)   (inverse map)
            acc={}
            for y in nb(x):
                for k,v in u(y,t+1): acc[k]=(acc.get(k,0)+alpha*v)%q
            for k,v in u(x,t+2): acc[k]=(acc.get(k,0)-v)%q
        return tuple(sorted((k,v) for k,v in acc.items() if v))
    return u
def cond_rank(rows_c,rows_y,q): return rank_mod(rows_c+rows_y,q)-rank_mod(rows_c,q)
def D(t): return dict(t)

def R1():
    u=make(9,3,1); x=(0,0,0)
    C=[D(u(x,-1)),D(u(x,0))]; Y=[D(u(x,t)) for t in range(1,5)]
    ranks=[cond_rank(C,Y[:t],3) for t in range(1,5)]
    front=all(D(u(x,t)).get(('C',(t,0,0)))==1 and all(('C',(t,0,0)) not in D(u(x,s)) for s in range(-1,t)) for t in range(1,5))
    ok=ranks==[1,2,3,4] and front
    print('R1  L=9 one port (fresh recursion): conditional ranks %s, frontier coefficients alpha^t present and new: %s'%(ranks,ok)); return ok
def R2():
    ok=True; n=0
    for q in (3,5,7):
        for alpha in range(1,q):
            K=3; L=2*K+1; u=make(L,q,alpha); x=(0,0,0)
            C=[D(u(x,-1)),D(u(x,0))]; Y=[D(u(x,t)) for t in range(1,K+1)]
            r=cond_rank(C,Y,q); ok&= r==K; n+=1
            coef=all(D(u(x,t)).get(('C',(t,0,0)))==pow(alpha,t,q) for t in range(1,K+1)); ok&=coef
    print('R2  one-port lemma for q in {3,5,7}, every nonzero alpha, L=7, K=3 (%d cases): full conditional rank and frontier alpha^t: %s'%(n,ok)); return ok
def R3():
    u=make(18,3,1); cs=list(product((0,9),repeat=3)); K=4
    C=[D(u(c,s)) for c in cs for s in (-1,0)]; Y=[D(u(c,t)) for c in cs for t in range(1,K+1)]
    sup=[set().union(*(set(D(u(c,t))) for t in range(-1,K+1))) for c in cs]
    disj=all(sup[i].isdisjoint(sup[j]) for i in range(8) for j in range(i))
    rc=rank_mod(C,3); rj=rank_mod(C+Y,3)
    ok=disj and rc==16 and rj==48
    print('R3  L=18 eight ports built on that torus: supports disjoint %s; ranks ready %d, joint %d: %s'%(disj,rc,rj,ok)); return ok
def R4():
    u=make(18,3,1); K=4; out=[]
    for d in range(1,10):
        a=(0,0,0); b=(d,0,0)
        C=[D(u(p,s)) for p in (a,b) for s in (-1,0)]; Y=[D(u(p,t)) for p in (a,b) for t in range(1,K+1)]
        out.append((d,cond_rank(C,Y,3)))
    print('R4  two ports at axis distance d (L=18, K=4): conditional rank of 8 future readings: %s'%out)
    return out
def R5():
    ok=True
    for q in (3,5):
        for n in (1,2,3):
            law={}
            for seq in product(product(range(q),repeat=2),repeat=n):
                rec=('F',)
                for k,(h,m) in enumerate(seq):
                    if h: rec=('S',k+1,m); break
                law[rec]=law.get(rec,0)+F(1,q**(2*n))
            ok&= law[('F',)]==F(1,q**n)
            ok&= all(law[('S',k,d)]==F(q-1,q**(k+1)) for k in range(1,n+1) for d in range(q))
    print('R5  first-success call law from i.i.d. uniform symbols, q in {3,5}, n <= 3: failure q^-n, (q-1)/q^(k+1) per mark: %s'%ok); return ok
def R6():
    u=make(9,3,1); x=(0,0,0); K=4; res=[]
    Y=[D(u(x,t)) for t in range(1,K+1)]
    for s in range(0,7):
        C=[D(u(x,-1)),D(u(x,0))]+[D(u(x,-1-j)) for j in range(1,s+1)]
        res.append((s,rank_mod(C,3),cond_rank(C,Y,3)))
    print('R6  pre-window port history u_x(-1-s..0), L=9, K=4: (s, history rank, conditional future rank) %s'%res)
    return res
if __name__=='__main__':
    print(__doc__.strip().splitlines()[0])
    a=[R1(),R2(),R3(),R5()]; R4(); R6()
    print('coordinator positive checks:','green' if all(a) else 'RED')
