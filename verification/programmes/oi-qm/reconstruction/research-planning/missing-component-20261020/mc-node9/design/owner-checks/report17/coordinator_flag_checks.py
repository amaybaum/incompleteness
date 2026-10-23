"""Coordinator checks of the native-flag-boundary handoff v1 (independent code; numpy).

F1  algebraic degree of the raw repaired rule, measured: k = 5 initial raw bits chosen at random (any field, either
    slice, anywhere on the torus) over a dense uniformly random background; every output bit at every site, ticks
    1..10 on a 7^3 torus (many wrap-arounds), has its algebraic normal form computed by a Moebius transform over the
    2^5 assignments. Maximum degree of A and B outputs, and of D outputs, over 40 random choices.
F2  countercontrol: the same measurement for a reversible second-order variant with feedback from D into A,
    A' = SA xor (SB)(SD) xor A_old (reversible because A' is (current force) xor A_old). The degree must exceed 2,
    or the measurement would be vacuous.
F3  the handoff's three-bit subcube on the actual apparatus (K = 3, L = 25): current A at (-1,0,0), current B at
    (1,0,0) and current D at the receiver, with every other readiness bit zero and the rest of the torus dense and
    random: E_K restricted to the subcube is three-bit zero detection, and every raw output bit at ticks 0..5 has
    degree at most 2 in those three bits.
F4  the parity argument for the 1/8 bound: the sum over the 3-cube of every degree-at-most-2 function is 0 (all
    2^7 of them), while the readiness indicator sums to 1; so each quadratic table errs somewhere, and the uniform
    mixture of the eight single-error tables errs with probability exactly 1/8 at every input.
"""
import numpy as np
from itertools import product
rng=np.random.default_rng(20261023)
def S(X):
    o=np.zeros_like(X)
    for ax in (-3,-2,-1): o^=np.roll(X,1,ax)^np.roll(X,-1,ax)
    return o
def step(p,c):
    (Ap,Bp,Dp),(A,B,D)=p,c; sa,sb=S(A),S(B)
    return (sa^Ap,sb^Bp,S(D)^Dp^S(A&B)^(sa&sb)^(sa&Bp)^(sb&Ap))
def step_fb(p,c):
    (Ap,Bp,Dp),(A,B,D)=p,c; sa,sb,sd=S(A),S(B),S(D)
    return (sa^(sb&sd)^Ap,sb^Bp,sd^Dp^S(A&B)^(sa&sb)^(sa&Bp)^(sb&Ap))
def moebius_degree(X,k):
    """X: (2^k, ...) uint8 truth tables along axis 0; returns max ANF degree over all other positions"""
    a=X.copy()
    for i in range(k):
        for m in range(1<<k):
            if m>>i&1: a[m]^=a[m^(1<<i)]
    deg=-1
    for m in range(1<<k):
        if a[m].any(): deg=max(deg,bin(m).count('1'))
    return deg
def run_degree(stepf,L,k,T,trials):
    worst={'AB':-1,'D':-1}
    for _ in range(trials):
        bg=[[rng.integers(0,2,(L,L,L),dtype=np.uint8) for _ in range(3)] for _ in range(2)]   # [slice][field]
        vars_=set()
        while len(vars_)<k:
            vars_.add((int(rng.integers(0,2)),int(rng.integers(0,3)),tuple(int(v) for v in rng.integers(0,L,3))))
        vars_=sorted(vars_)
        n=1<<k
        sl=[[np.repeat(bg[s][f][None],n,0) for f in range(3)] for s in range(2)]
        for i,(s,f,x) in enumerate(vars_):
            sl[s][f][(slice(None),)+x]=(np.arange(n)>>i)&1
        p,c=tuple(sl[0]),tuple(sl[1])
        for t in range(T):
            p,c=c,stepf(p,c)
            worst['AB']=max(worst['AB'],moebius_degree(c[0],k),moebius_degree(c[1],k))
            worst['D']=max(worst['D'],moebius_degree(c[2],k))
    return worst
def F1():
    w=run_degree(step,7,5,10,40)
    ok=w['AB']==1 and w['D']==2
    print('F1  repaired rule, 7^3 torus, ticks 1..10, 40 random 5-bit subcubes on dense random backgrounds: max degree of A/B outputs %d, of D outputs %d: %s'%(w['AB'],w['D'],ok))
    return ok
def F2():
    w=run_degree(step_fb,7,5,10,10)
    ok=max(w.values())>2
    print('F2  countercontrol with D feedback into A (A\' = SA xor (SB)(SD) xor A_old): max degree A/B %d, D %d; exceeds 2: %s'%(w['AB'],w['D'],ok))
    return ok
def F3():
    K=3; L=25; q=(12,0,0); r=np.arange(L); d=np.minimum(r,L-r); dist=d[:,None,None]+d[None,:,None]+d[None,None,:]
    inK=dist<=K; inK1=dist<=K-1
    ex=[np.zeros((L,L,L),bool) for _ in range(3)]; ex[0][K,0,0]=True; ex[1][0,K,0]=True
    tested=[(0,(L-1,0,0)),(1,(1,0,0)),(2,(0,0,0))]
    ok=True; worst=-1
    for trial in range(3):
        p=[rng.integers(0,2,(8,L,L,L),dtype=np.uint8) for _ in range(3)]; c=[rng.integers(0,2,(8,L,L,L),dtype=np.uint8) for _ in range(3)]
        for f in range(3):
            p[f][:]=p[f][:1]; c[f][:]=c[f][:1]          # same background for all eight assignments
            c[f][:,inK&~ex[f]]=0; p[f][:,inK1]=0; c[f][:,q[0],q[1],q[2]]=0; p[f][:,q[0],q[1],q[2]]=0
        for i,(f,x) in enumerate(tested): c[f][(slice(None),)+x]=(np.arange(8)>>i)&1
        ready=np.ones(8,bool)
        for f in range(3):
            ready&=~c[f][:,inK&~ex[f]].any(1); ready&=~p[f][:,inK1].any(1)
            ready&=(c[f][:,q[0],q[1],q[2]]==0)&(p[f][:,q[0],q[1],q[2]]==0)
        ok&=ready.tolist()==[True]+[False]*7
        P,C=tuple(p),tuple(c)
        for f in range(3): worst=max(worst,moebius_degree(C[f],3))
        for t in range(5):
            P,C=C,step(P,C)
            for f in range(3): worst=max(worst,moebius_degree(C[f],3))
    ok&=worst<=2
    print('F3  K=3, L=25, three tested readiness bits over 3 dense random backgrounds: E_K on the subcube is three-bit zero detection, and every raw output at ticks 0..5 has degree %d <= 2 in them: %s'%(worst,ok))
    return ok
def F4():
    x=list(product((0,1),repeat=3)); mons=[(),(0,),(1,),(2,),(0,1),(0,2),(1,2)]
    ok=True
    for coef in range(1<<7):
        tab=[sum(((coef>>j)&1)*int(all(v[i] for i in m)) for j,m in enumerate(mons))%2 for v in x]
        ok&=sum(tab)%2==0
    ready=[int(v==(0,0,0)) for v in x]
    ok&=sum(ready)%2==1
    mix=[sum(int((ready[i]^(i==e))!=ready[i]) for e in range(8)) for i in range(8)]
    ok&=mix==[1]*8
    print('F4  all 128 quadratic tables have even cube sum, the readiness table odd; the eight single-error tables err once each per input (mixture error 1/8): %s'%ok)
    return ok
if __name__=='__main__':
    print(__doc__.strip().splitlines()[0])
    r=[F1(),F2(),F3(),F4()]
    print('coordinator checks:','green' if all(r) else 'RED')
