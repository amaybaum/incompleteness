"""Coordinator checks of the nonlinear-frontier handoff v1 (independent code; numpy).

Rule: U' = H(S U) xor U_old with U = (A, B, D), H(a, b, d) = (b, d, a xor bd), S the six-neighbour XOR.

G1  reversibility: explicit inverse U_old = U' xor H(S U) on random tori (7^3, 6x5x4) over 12 ticks; H is a
    permutation of the eight triples.
G2  source freshness on dense full-torus backgrounds (every unreserved bit of both slices random), frontier along
    -y (the handoff uses +x), K = 2, 3, 4 on an 11^3 torus, 4 backgrounds each: every one of the 8^K source words
    occurs exactly once; and for every prefix of every length the next triple is exactly uniform.
G3  the joint apparatus (K = 2, L = 17, q = (8,0,0)) on 3 dense full-torus backgrounds, with all 8 inputs x 64
    frontier assignments per background: receiver record ((0,0,0), (c, ab, abc)) in every run, and for each input
    the 64 source words are all distinct and the same set for every input; plus the complemented encoding.
G4  degree growth with more variables: 8 and 10 free initial bits at random over dense backgrounds on a 7^3 torus,
    ticks 1..10, maximum algebraic degree of any output bit (Moebius transform).
G5  the readiness count J for the joint apparatus, recounted from its definition.
"""
import numpy as np
from itertools import product
rng=np.random.default_rng(20261023)
def S(X):
    o=np.zeros_like(X)
    for ax in (-3,-2,-1): o^=np.roll(X,1,ax)^np.roll(X,-1,ax)
    return o
def force(c):
    sa,sb,sd=S(c[0]),S(c[1]),S(c[2]); return (sb,sd,sa^(sb&sd))
def step(p,c):
    f=force(c); return tuple(x^y for x,y in zip(p,f))
def back(c,n):
    f=force(c); return tuple(x^y for x,y in zip(n,f))
def rnd(shape): return rng.integers(0,2,size=shape,dtype=np.uint8)
def G1():
    H=lambda a,b,d:(b,d,a^(b&d))
    ok=len({H(*v) for v in product((0,1),repeat=3)})==8
    for shape in ((7,7,7),(6,5,4)):
        p=tuple(rnd((32,)+shape) for _ in range(3)); c=tuple(rnd((32,)+shape) for _ in range(3))
        for _ in range(12):
            n=step(p,c); ok&=all(np.array_equal(x,y) for x,y in zip(back(c,n),p)); p,c=c,n
    print('G1  H permutes the eight triples; explicit inverse recovers the previous slice on random 7^3 and 6x5x4 tori over 12 ticks: %s'%ok)
    return ok
def G2():
    ok=True; cases=0
    for K in (2,3,4):
        L=11; n=8**K
        for bg in range(4):
            p=[np.repeat(rnd((1,L,L,L)),n,0) for _ in range(3)]; c=[np.repeat(rnd((1,L,L,L)),n,0) for _ in range(3)]
            idx=np.arange(n)
            for t in range(1,K+1):
                for f in range(3): c[f][:,0,(-t)%L,0]=(idx>>(3*(t-1)+f))&1
            P,C=tuple(p),tuple(c); words=[]
            for t in range(K):
                P,C=C,step(P,C); words.append(sum(C[f][:,0,0,0].astype(np.int64)<<f for f in range(3)))
            code=sum(w<<(3*i) for i,w in enumerate(words))
            ok&=len(np.unique(code))==n
            for s in range(K):
                pre=sum(w<<(3*i) for i,w in enumerate(words[:s])) if s else np.zeros(n,np.int64)
                key=pre*8+words[s]
                cnt=np.bincount(key,minlength=8**(s+1)).reshape(-1,8)
                ok&=bool((cnt==cnt[:,:1]).all())
            cases+=1
    print('G2  dense full-torus backgrounds, frontier along -y, K=2,3,4 on 11^3, %d cases: every source word once, next triple uniform given every prefix: %s'%(cases,ok))
    return ok
def G3():
    K=2; L=17; q=(8,0,0); r=np.arange(L); d=np.minimum(r,L-r); dist=d[:,None,None]+d[None,:,None]+d[None,None,:]
    pa,pb,pc=(1,1,0),(1,L-1,0),(0,0,2); ok=True
    for comp in (False,True):
        for bg in range(3):
            n=8*64; idx=np.arange(n); inp=idx>>6; fr=idx&63
            p=[np.repeat(rnd((1,L,L,L)),n,0) for _ in range(3)]; c=[np.repeat(rnd((1,L,L,L)),n,0) for _ in range(3)]
            for f in range(3):
                c[f][:,dist<=2]=0; p[f][:,dist<=1]=0; c[f][:,q[0],q[1],q[2]]=0; p[f][:,q[0],q[1],q[2]]=0
            x=[(inp>>i)&1 for i in range(3)]
            a,b,cc=[(1-v) if comp else v for v in x]
            c[1][:,pa[0],pa[1],pa[2]]=a; c[2][:,pb[0],pb[1],pb[2]]=b; c[2][:,pc[0],pc[1],pc[2]]=cc
            for t in range(1,K+1):
                for f in range(3): c[f][:,q[0]+t,0,0]=(fr>>(3*(t-1)+f))&1
            P,C=tuple(p),tuple(c); rec=[]; src=[]
            for t in range(K):
                P,C=C,step(P,C)
                rec.append(np.stack([v[:,0,0,0] for v in C],1)); src.append(sum(C[f][:,q[0],q[1],q[2]].astype(np.int64)<<f for f in range(3)))
            want1=np.zeros((n,3),np.uint8); want2=np.stack([cc,a*b,a*b*cc],1).astype(np.uint8)
            ok&=bool(np.array_equal(rec[0],want1)) and bool(np.array_equal(rec[1],want2))
            if comp: ok&=bool(np.array_equal(rec[1][:,2],(inp==0).astype(np.uint8)))
            word=src[0]*8+src[1]; sets=[]
            for i in range(8):
                s=word[inp==i]; ok&=len(np.unique(s))==64; sets.append(tuple(sorted(s)))
            ok&=len(set(sets))==1
    print('G3  joint apparatus, 3 dense full-torus backgrounds x 512 (input, frontier) assignments, AND3 and complemented zero test: receiver ((0,0,0),(c,ab,abc)) in every run, 64 distinct source words per input, same set for every input: %s'%ok)
    return ok
def mdeg(X,k):
    a=X.copy()
    for i in range(k):
        for m in range(1<<k):
            if m>>i&1: a[m]^=a[m^(1<<i)]
    return max((bin(m).count('1') for m in range(1<<k) if a[m].any()),default=-1)
def G4():
    L=7; out={}
    for k in (8,10):
        best=[0]*10
        for trial in range(3):
            n=1<<k
            sl=[[np.repeat(rnd((1,L,L,L)),n,0) for _ in range(3)] for _ in range(2)]
            vs=set()
            while len(vs)<k: vs.add((int(rng.integers(0,2)),int(rng.integers(0,3)),tuple(int(v) for v in rng.integers(0,L,3))))
            for i,(s,f,x) in enumerate(sorted(vs)): sl[s][f][(slice(None),)+x]=(np.arange(n)>>i)&1
            p,c=tuple(sl[0]),tuple(sl[1])
            for t in range(10):
                p,c=c,step(p,c); best[t]=max(best[t],max(mdeg(c[f],k) for f in range(3)))
        out[k]=best
    ok=out[8][-1]>6 and out[10][-1]>6
    print('G4  max output degree, 3 random choices each, ticks 1..10, 7^3 torus: 8 variables %s; 10 variables %s; exceeds 6: %s'%(out[8],out[10],ok))
    return ok
def G5():
    b=lambda R:sum(1 for v in product(range(-R,R+1),repeat=3) if sum(map(abs,v))<=R)
    J=3*b(2)-3+3*b(1)+6
    print('G5  readiness of the joint apparatus: 3 x %d current ball bits - 3 input slots + 3 x %d previous ball bits + 6 source bits = %d: %s'%(b(2),b(1),J,J==99))
    return J==99
if __name__=='__main__':
    print(__doc__.strip().splitlines()[0])
    r=[G1(),G2(),G3(),G4(),G5()]
    print('coordinator checks:','green' if all(r) else 'RED')
