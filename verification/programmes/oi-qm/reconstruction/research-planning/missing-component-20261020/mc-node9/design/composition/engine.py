"""Exact engines for the report18 rule. Bitpacked truth tables (numpy uint64) on a torus, and sparse ANF."""
import numpy as np
from itertools import product
DIRS=((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1))
def vars_tt(n):
    N=1<<n; W=max(1,N//64); idx=np.arange(N)
    out=[]
    for j in range(n):
        bits=((idx>>j)&1).astype(np.uint64)
        if N<64: bits=np.concatenate([bits,np.zeros(64-N,np.uint64)])
        words=(bits.reshape(-1,64)<<np.arange(64,dtype=np.uint64)).sum(1).astype(np.uint64) if False else None
        w=np.zeros(W,np.uint64)
        b=bits.reshape(W,64)
        for k in range(64): w|=(b[:,k]<<np.uint64(k))
        out.append(w)
    full=np.zeros(W,np.uint64)
    fb=np.zeros(W*64,np.uint64); fb[:N]=1; fb=fb.reshape(W,64)
    for k in range(64): full|=(fb[:,k]<<np.uint64(k))
    return out,full
def S(X):
    o=np.zeros_like(X)
    for ax in (1,2,3): o^=np.roll(X,1,ax)^np.roll(X,-1,ax)
    return o
def step(p,c):
    sa,sb,sd=S(c[0:1])[0],S(c[1:2])[0],S(c[2:3])[0]
    n=np.empty_like(c); n[0]=p[0]^sb; n[1]=p[1]^sd; n[2]=p[2]^sa^(sb&sd); return n
def run(n,L,slots,T,bg=None,pins=None,record=None):
    """slots: list of (slice -1/0, field 0/1/2, pos, value) where value = ('x',j) input j, ('c',j) copy of input j,
    ('one',) constant one. Receiver at origin. Returns list of current states per tick 0..T (arrays (3,L,L,L,W))."""
    vs,full=vars_tt(n); W=len(full)
    if bg is None:
        p=np.zeros((3,L,L,L,W),np.uint64); c=np.zeros_like(p)
    else:
        g=np.random.default_rng(bg)
        p=(g.integers(0,2,(3,L,L,L,1)).astype(np.uint64)*full); c=(g.integers(0,2,(3,L,L,L,1)).astype(np.uint64)*full)
        r=np.arange(L); d=np.minimum(r,L-r); dist=d[:,None,None]+d[None,:,None]+d[None,None,:]
        c[:,dist<=T]=0; p[:,dist<=T-1]=0
    for s,f,x,v in slots:
        x=tuple(a%L for a in x); val=vs[v[1]] if v[0] in ('x','c') else full
        (c if s==0 else p)[(f,)+x]^=val
    hist=[c.copy()]
    for t in range(T): p,c=c,step(p,c); hist.append(c.copy())
    return hist,full
def degree(tt_words,n):
    N=1<<n; bits=np.unpackbits(tt_words.view(np.uint8),bitorder='little')[:N].astype(np.uint8)
    a=bits.copy()
    for i in range(n):
        s=1<<i; a=a.reshape(-1,2*s); a[:,s:]^=a[:,:s]; a=a.reshape(-1)
    nz=np.nonzero(a)[0]
    return max((bin(int(m)).count('1') for m in nz),default=-1), bits
def is_and(tt_words,n):
    deg,bits=degree(tt_words,n); want=np.zeros(1<<n,np.uint8); want[-1]=1
    return bool(np.array_equal(bits,want)),deg
