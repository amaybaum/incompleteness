"""Sweep for the pre-window-history and port-separation probes (coordinator, exploratory)."""
import sys, os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from coordinator_native_wave_checks import make, rank_mod, cond_rank, D
from itertools import product
bad_hist=[]; n=0
for q in (3,5,7):
    for alpha in range(1,q):
        for K in (2,3,4):
            for s in range(0,K+3):
                L=2*(K+s)+1; u=make(L,q,alpha); x=(0,0,0)
                C=[D(u(x,-1)),D(u(x,0))]+[D(u(x,-1-j)) for j in range(1,s+1)]
                Y=[D(u(x,t)) for t in range(1,K+1)]
                hr=rank_mod(C,q); r=cond_rank(C,Y,q); n+=1
                if hr!=2+s or r!=K: bad_hist.append((q,alpha,K,s,hr,r))
print('history sweep: %d cases; deficient (q, alpha, K, s, history rank, conditional rank): %s'%(n,bad_hist))
bad_sep=[]; n=0
for q in (3,5):
    for alpha in range(1,q):
        K=3; L=15; u=make(L,q,alpha)
        for d in range(0,5):
            for off in product(range(0,4),repeat=3):
                if sum(off)!=d or d==0: continue
                a=(0,0,0); b=off
                C=[D(u(p,s)) for p in (a,b) for s in (-1,0)]; Y=[D(u(p,t)) for p in (a,b) for t in range(1,K+1)]
                r=cond_rank(C,Y,q); rc=rank_mod(C,q); n+=1
                if r!=2*K or rc!=4: bad_sep.append((q,alpha,off,rc,r))
print('separation sweep: %d cases (L1 distance 1..4, K=3); deficient (q, alpha, offset, ready rank, conditional rank): %s'%(n,bad_sep[:12]),'... total',len(bad_sep))
# countercontrols: each must show a rank loss
u=make(9,3,1); x=(0,0,0)
nbr=[{('C',y):1} for y in [(1,0,0),(8,0,0),(0,1,0),(0,8,0),(0,0,1),(0,0,8)]]
C=[D(u(x,-1)),D(u(x,0))]+[D(u(x,-1-j)) for j in range(1,4)]
k1=cond_rank(C+nbr,[D(u(x,1))],3)
k2=cond_rank([D(u(x,-1)),D(u(x,0))],[D(u(x,t)) for t in range(1,4)]*2,3)
out=[]
for s in range(0,9):
    us=make(3,3,1)
    Cs=[D(us(x,-1)),D(us(x,0))]+[D(us(x,-1-j)) for j in range(1,s+1)]
    out.append(cond_rank(Cs,[D(us(x,t)) for t in range(1,5)],3))
print('countercontrols: history plus six neighbour values -> first future reading conditional rank %d (must be 0); duplicated port -> rank %d of 6 rows (must be 3); L=3 torus history s=0..8 -> conditional future ranks %s (must fall below 4)'%(k1,k2,out))
print('countercontrols:','detected' if k1==0 and k2==3 and min(out)<4 else 'MISSED')
