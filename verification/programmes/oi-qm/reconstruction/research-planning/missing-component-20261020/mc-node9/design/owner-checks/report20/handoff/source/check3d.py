import numpy as np, sys, time
from engine import vars_tt, step, degree
from builder import realize
def run3d(n,bg=None,mutate=None):
    T,srcs=realize(n)
    if mutate: srcs=mutate(srcs)
    L=2*T+3; vs,full=vars_tt(n); W=len(full)
    if bg is None:
        p=np.zeros((3,L,L,L,W),np.uint64); c=np.zeros_like(p)
    else:
        g=np.random.default_rng(bg)
        p=g.integers(0,2,(3,L,L,L,1)).astype(np.uint64)*full; c=g.integers(0,2,(3,L,L,L,1)).astype(np.uint64)*full
        r=np.arange(L); d=np.minimum(r,L-r); dist=d[:,None,None]+d[None,:,None]+d[None,None,:]
        c[:,dist<=T]=0; p[:,dist<=T-1]=0
    for pos,f,(const,vset) in srcs:
        val=full.copy() if const else np.zeros_like(full)
        for j in vset: val^=vs[j]
        c[(f,)+tuple(a%L for a in pos)]^=val
    for t in range(T): p,c=c,step(p,c)
    want=full.copy()
    for v in vs: want&=v
    out=c[2,0,0,0]
    deg,_=degree(out,n)
    return bool(np.array_equal(out,want)),deg,T,len(srcs)
if __name__=='__main__':
    for n in [int(a) for a in sys.argv[1:]]:
        t0=time.time()
        z=run3d(n); b1=run3d(n,bg=100+n); b2=run3d(n,bg=200+n)
        print('n',n,'T',z[2],'sources',z[3],'zero bg (AND, degree)',z[:2],'dense bg1',b1[:2],'dense bg2',b2[:2],'%.0fs'%(time.time()-t0),flush=True)
