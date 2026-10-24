import itertools
from fractions import Fraction as F
def rank(rows):
    M=[list(map(F,r)) for r in rows]; rk=0; cols=len(M[0]) if M else 0
    for c in range(cols):
        piv=next((i for i in range(rk,len(M)) if M[i][c]!=0),None)
        if piv is None: continue
        M[rk],M[piv]=M[piv],M[rk]
        for i in range(len(M)):
            if i!=rk and M[i][c]!=0:
                f=M[i][c]/M[rk][c]; M[i]=[x-f*y for x,y in zip(M[i],M[rk])]
        rk+=1
    return rk
def mul_row(w,M): return [sum(w[i]*M[i][j] for i in range(len(w))) for j in range(len(M[0]))]
# (2)
deals=[(a,b) for a in (0,1) for b in range(4)]
sup=[S for S in itertools.combinations(deals,4) if sum(1 for a,b in S if a==0)==3]
cls={min(tuple(sorted((a,p[b]) for a,b in S)) for p in itertools.permutations(range(4))) for S in sup}
print('(2) 3:1 supports',len(sup),'classes',len(cls))
# (3) single system, Lemma-W style: functionals w (row over configs), w -> w*T for branch maps T
cfg=[(v,h) for v in (0,1) for h in (0,1)]
def T_swap():
    T=[[F(0)]*4 for _ in range(4)]
    for i,(v,h) in enumerate(cfg): T[i][cfg.index((h,v))]=F(1)   # row i = from config i; maps prob vectors p'=pT
    return T
def T_read(r):
    T=[[F(0)]*4 for _ in range(4)]
    for i,(v,h) in enumerate(cfg):
        if v==r:
            for h2 in (0,1): T[i][cfg.index((v,h2))]+=F(1,2)
    return T
ops=[T_swap(),T_read(0),T_read(1)]
# functional f(p)= p . w ; after op T: f(pT)= p.(T w). So w -> T w (column action)
def Tw(T,w): return [sum(T[i][j]*w[j] for j in range(4)) for i in range(4)]
W=[[F(1)]*4]
while True:
    new=W+[Tw(T,w) for T in ops for w in W]
    if rank(new)==rank(W): break
    # keep a basis
    B=[]
    for w in new:
        if rank(B+[w])>rank(B): B.append(w)
    W=B
print('(3) functional span dim',rank(W))
# (4) reservoir reuse vs fresh: reads with swaps between; read: record v, h<-e, e<-h (reversible)
def experiment(reuse):
    br={}
    nres=1 if reuse else 3
    for v,h,*es in itertools.product((0,1),repeat=2+nres):
        es=list(es); rec=[]
        for k in range(3):
            j=0 if reuse else k
            rec.append(v); h,es[j]=es[j],h          # read: record v, swap h with reservoir card
            if k<2: v,h=h,v                         # swap system cards between reads
        br.setdefault(tuple(rec),set()).add((v,h))
    return sorted({len(s) for s in br.values()})
print('(4) fresh supports',experiment(False),'reused supports',experiment(True))
