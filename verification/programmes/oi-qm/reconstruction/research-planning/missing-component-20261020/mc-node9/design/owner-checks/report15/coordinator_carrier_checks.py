"""Coordinator checks of the joint-readiness and carrier-compatibility handoffs v1 (independent code; numpy).

N1  the repaired three-field rule, implemented raw on random tori: C = D xor AB satisfies C' = S C xor C_old at
    every tick, and the explicit inverse (current, next) -> previous recovers the previous slice.
N2  the carrier construction with every bit outside E_K drawn at random (both time slices, all three fields, the
    whole torus), K = 2, 3, 4: the receiver record is silent before K and (a, b, ab) at K. Countercontrols: the
    same backgrounds with one receiver-cone readiness bit left free, and the original detector rule.
N3  source freshness under those random backgrounds: the frontier is the current A, B, D bits at q + t e_y,
    t = 1..K (a different frontier from the handoff's); enumerating it, for each background and payload, every one
    of the 8^K raw source words occurs exactly once and the receiver record does not change.
N4  box invariance of the pair-parity majority rule: random two-slice patterns supported in random boxes, and in
    random products of coordinate subsets, on a 12^3 torus for 30 ticks.
N5  probe (exploratory): a one-site perturbation of the majority rule on a uniformly random background.
N6  the joint-readiness tick-2 defect of the original rule under E_blank: the raw AND error Z_2 xor H_2 M_2 is a
    bilinear form in the free initial A and B bits (radius-3 ball, both time slices, the 14 E constraints imposed);
    its matrix is read off by simulating the original rule with one A bit and one B bit, bilinearity is checked on
    random pairs, and the error probability is (1 - 2^-r)/2 for its F2 rank r.
N7  the frontier coefficient c_t of F_t G_t in Z_t for the original rule, t = 1..8 (expected t mod 2).
"""
import numpy as np
rng=np.random.default_rng(20261023)
def S(X):
    out=np.zeros_like(X)
    for ax in (-3,-2,-1):
        out^=np.roll(X,1,axis=ax)^np.roll(X,-1,axis=ax)
    return out
def step(p,c):
    (Ap,Bp,Dp),(A,B,D)=p,c
    sa,sb=S(A),S(B)
    return (sa^Ap, sb^Bp, S(D)^Dp^S(A&B)^(sa&sb)^(sa&Bp)^(sb&Ap))
def back(c,n):
    (A,B,D),(An,Bn,Dn)=c,n
    sa,sb=S(A),S(B); Ap=sa^An; Bp=sb^Bn
    return (Ap,Bp,Dn^S(D)^S(A&B)^(sa&sb)^(sa&Bp)^(sb&Ap))
def step_orig(p,c):
    (Ap,Bp,Dp),(A,B,D)=p,c
    return (S(A)^Ap,S(B)^Bp,S(D)^Dp^S(A&B))
def rnd(shape): return rng.integers(0,2,size=shape,dtype=np.uint8)
def N1():
    ok=True; n=0
    for shape in ((7,7,7),(6,5,4),(9,8,10)):
        p=tuple(rnd((64,)+shape) for _ in range(3)); c=tuple(rnd((64,)+shape) for _ in range(3))
        for _ in range(12):
            nx=step(p,c)
            Cp,Cc,Cn=p[2]^(p[0]&p[1]),c[2]^(c[0]&c[1]),nx[2]^(nx[0]&nx[1])
            ok&=bool(np.array_equal(Cn,S(Cc)^Cp))
            ok&=all(np.array_equal(x,y) for x,y in zip(back(c,nx),p))
            p,c=c,nx; n+=64
    print('N1  repaired rule on random tori (7^3, 6x5x4, 9x8x10; 64 states x 12 ticks each): C\' = S C xor C_old and the inverse recovers the previous slice, %d transitions: %s'%(n,ok))
    return ok
def l1(L):
    r=np.arange(L); d=np.minimum(r,L-r)
    return d[:,None,None]+d[None,:,None]+d[None,None,:]
def ready(K,batch,free_one=False):
    """random two-slice states on the (8K+1)^3 torus, then E_K imposed; returns (prev, cur), payload sites"""
    L=8*K+1; dist=l1(L); q=(4*K,0,0)
    p=[rnd((batch,L,L,L)) for _ in range(3)]; c=[rnd((batch,L,L,L)) for _ in range(3)]
    inK=dist<=K; inK1=dist<=K-1
    for f in range(3):
        c[f][:,inK]=0; p[f][:,inK1]=0; c[f][(slice(None),)+q]=0; p[f][(slice(None),)+q]=0
    if free_one:                      # leave the current-A bit at (0,0,K) free: one shortest path to o, coefficient 1
        c[0][:,0,0,K]=rng.integers(0,2,size=batch,dtype=np.uint8)
    return p,c,L,q
def N2():
    ok=True; ctrl={}; tot=0
    for K in (2,3,4):
        bad_free=0; bad_orig=0
        for a in (0,1):
            for b in (0,1):
                for free_one in (False,True):
                    p,c,L,q=ready(K,40,free_one)
                    c[0][:,K,0,0]=a; c[1][:,0,K,0]=b
                    rec=[]; P,C=tuple(p),tuple(c)
                    po,co=tuple(x.copy() for x in p),tuple(x.copy() for x in c)
                    for t in range(K):
                        P,C=C,step(P,C); po,co=co,step_orig(po,co)
                        rec.append(np.stack([x[:,0,0,0] for x in C],1))
                    want=np.array([0,0,0]*(K-1)+[a,b,a*b],dtype=np.uint8)
                    got=np.concatenate(rec,1)
                    good=np.all(got==want,1)
                    if free_one: bad_free+=int((~good).sum())
                    else:
                        ok&=bool(good.all()); tot+=len(good)
                        orig_term=np.stack([x[:,0,0,0] for x in co],1)
                        bad_orig+=int(np.any(orig_term!=np.array([a,b,a*b]),1).sum())
        ctrl[K]=(bad_free,bad_orig)
    ok&=all(v[0]>0 for v in ctrl.values()) and ctrl[3][1]>0
    print('N2  carrier with full random background outside E_K, K=2,3,4, 40 backgrounds per payload: receiver record ((0,0,0)^(K-1),(a,b,ab)) in all %d runs; countercontrols (runs off the record of 160 per K): one free cone bit %s, original rule terminal %s: %s'%(tot,{k:v[0] for k,v in ctrl.items()},{k:v[1] for k,v in ctrl.items()},ok))
    return ok
def N3():
    ok=True; cases=0
    for K in (2,3):
        L=8*K+1
        for a in (0,1):
            for b in (0,1):
                for bg in range(4):
                    p,c,L,q=ready(K,1)
                    c[0][:,K,0,0]=a; c[1][:,0,K,0]=b
                    n=8**K
                    p=[np.repeat(x,n,0) for x in p]; c=[np.repeat(x,n,0) for x in c]
                    idx=np.arange(n)
                    for f in range(3):
                        for t in range(1,K+1):
                            c[f][:,q[0],t,0]=(idx>>(f*K+t-1))&1
                    P,C=tuple(p),tuple(c); src=[]; rec=[]
                    for t in range(K):
                        P,C=C,step(P,C)
                        src.append(np.stack([x[:,q[0],0,0] for x in C],1)); rec.append(np.stack([x[:,0,0,0] for x in C],1))
                    words=np.concatenate(src,1); code=(words.astype(np.int64)*(1<<np.arange(3*K))).sum(1)
                    ok&=len(np.unique(code))==n
                    r=np.concatenate(rec,1); ok&=bool(np.all(r==np.array([0,0,0]*(K-1)+[a,b,a*b])))
                    cases+=1
    print('N3  source freshness, random backgrounds, frontier along +y from q, K=2,3: in all %d (background, payload) cases the 8^K frontier assignments give 8^K distinct raw source words and an unchanged receiver record: %s'%(cases,ok))
    return ok
def maj_step(p,c):
    px=np.roll(c,1,-3)^np.roll(c,-1,-3); py=np.roll(c,1,-2)^np.roll(c,-1,-2); pz=np.roll(c,1,-1)^np.roll(c,-1,-1)
    return p^((px&py)^(py&pz)^(pz&px))
def N4():
    L=12; ok=True; n=0; moved=0
    for trial in range(400):
        if trial%2==0:
            sets=[]
            for _ in range(3):
                lo=rng.integers(0,L); w=rng.integers(1,6); sets.append(np.isin(np.arange(L),(lo+np.arange(w))%L))
        else:
            sets=[rng.random(L)<0.35 for _ in range(3)]
            for s in sets: s[rng.integers(0,L)]=True
        box=sets[0][:,None,None]&sets[1][None,:,None]&sets[2][None,None,:]
        p=rnd((L,L,L))&box; c=rnd((L,L,L))&box
        for _ in range(30):
            p,c=c,maj_step(p,c)
            ok&=not bool((c&~box).any())
        moved+=int(c.any()); n+=1
    print('N4  majority rule: %d random two-slice patterns (half in boxes up to 5^3, half in random coordinate-subset products) on a 12^3 torus, 30 ticks: support never leaves the set: %s (%d still nonzero at tick 30)'%(n,ok,moved))
    return ok
def N5():
    L=21; rows=[]
    for trial in range(20):
        p=rnd((L,L,L)); c=rnd((L,L,L)); c2=c.copy(); c2[0,0,0]^=1; p2=p.copy()
        dist=l1(L); far=[]
        for t in range(1,9):
            p,c=c,maj_step(p,c); p2,c2=c2,maj_step(p2,c2)
            d=c^c2; far.append(int(dist[d.astype(bool)].max()) if d.any() else -1)
        rows.append(far)
    rows=np.array(rows)
    print('N5  probe: one-site flip on a uniform random background, majority rule, 21^3, 20 backgrounds: farthest L1 distance of the difference at ticks 1..8: max %s, median %s'%(rows.max(0).tolist(),np.median(rows,0).astype(int).tolist()))
def rank2(M):
    M=M.copy()%2; r=0
    for col in range(M.shape[1]):
        piv=np.nonzero(M[r:,col])[0]
        if len(piv)==0: continue
        i=r+piv[0]; M[[r,i]]=M[[i,r]]
        rows=np.nonzero(M[:,col])[0]; rows=rows[rows!=r]
        M[rows]^=M[r]; r+=1
        if r==M.shape[0]: break
    return r
def orig_run(Ap,A0,Bp,B0,T,site):
    z=np.zeros_like(A0); P,C=(Ap,Bp,z),(A0,B0,z.copy()); out=[]
    for _ in range(T):
        P,C=C,step_orig(P,C); out.append(tuple(x[(slice(None),)+site] for x in C))
    return out
def N6():
    L=11; o=(0,0,0); e=(1,0,0); fixed0={o}|{d for d in ((L-1,0,0),(0,1,0),(0,L-1,0),(0,0,1),(0,0,L-1))}
    dist=l1(L); ball=[tuple(int(v) for v in s) for s in zip(*np.nonzero(dist<=3))]
    var=[(0,s) for s in ball if s not in fixed0]+[(-1,s) for s in ball if s!=o]
    nv=len(var)
    def fields(rows):
        n=len(rows); Ap=np.zeros((n,L,L,L),np.uint8); A0=np.zeros_like(Ap)
        for k,row in enumerate(rows):
            for i in np.nonzero(row)[0]:
                tm,s=var[i]; (A0 if tm==0 else Ap)[(k,)+s]^=1
        return Ap,A0
    I=np.eye(nv,dtype=np.uint8); M=np.zeros((nv,nv),np.uint8)
    for i in range(nv):
        Ap,A0=fields(np.repeat(I[i:i+1],nv,0)); Bp,B0=fields(I)
        (H1,M1,Z1),(H2,M2,Z2)=orig_run(Ap,A0,Bp,B0,2,o)
        M[i]=Z2^(H2&M2)
    X=rng.integers(0,2,size=(200,nv),dtype=np.uint8); Y=rng.integers(0,2,size=(200,nv),dtype=np.uint8)
    Ap,A0=fields(X); Bp,B0=fields(Y); (_,_,_),(H2,M2,Z2)=orig_run(Ap,A0,Bp,B0,2,o)
    pred=np.einsum('ki,ij,kj->k',X.astype(np.int64),M.astype(np.int64),Y.astype(np.int64))%2
    bil=bool(np.array_equal(pred,(Z2^(H2&M2)).astype(np.int64)))
    r=rank2(M); num=2**(r)-1; den=2**(r+1)
    ok=bil and r==12 and (num,den)==(4095,8192)
    print('N6  original rule, E_blank, tick 2: %d free A and %d free B initial bits (radius-3 ball); bilinearity on 200 random pairs %s; F2 rank of the error form %d; P(Z_2 != H_2 M_2) = %d/%d: %s'%(nv,nv,bil,r,num,den,ok))
    return ok
def N7():
    L=19; cs=[]
    for t in range(1,9):
        Ap=np.zeros((1,L,L,L),np.uint8); A0=Ap.copy(); A0[0,t,0,0]=1; B0=A0.copy()
        cs.append(int(orig_run(Ap,A0,Ap.copy(),B0,t,(0,0,0))[-1][2][0]))
    ok=cs==[t%2 for t in range(1,9)]
    print('N7  original rule, frontier coefficient of F_t G_t in Z_t, t=1..8: %s (t mod 2): %s'%(cs,ok))
    return ok
if __name__=='__main__':
    print(__doc__.strip().splitlines()[0])
    r=[N1(),N2(),N3(),N4()]; N5(); r+=[N6(),N7()]
    print('coordinator positive checks:','green' if all(r) else 'RED')
