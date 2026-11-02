# Countercheck of Main §3.4 Remark (a variational identity): at (nV,nH)=(2,3), horizon as in
# memory_probes.py (predict X3 from history (X0,X1,X2)), does the infimum of I(hist;H2|X2) over ALL
# fixed-dimension realizations (any permutation, any prior on C_V x C_H) attain M_t, where the
# probe only searched uniform priors?  The objective is convex in the within-class split (fixed P(hist)),
# and the feasible set is a product of simplices, so a local optimum is global.
from itertools import permutations
from collections import defaultdict
from fractions import Fraction as F
import numpy as np
from math import log2
from scipy.optimize import minimize
nV,nH=2,3; N=nV*nH
def path(perm,s):
    p=[s//nH]; 
    for _ in range(3):
        s=perm[s]; p.append(s//nH)
    return tuple(p)
def h2(perm,s):
    return perm[perm[s]]%nH
def law_uniform(perm):
    L=defaultdict(lambda:F(0))
    for s in range(N): L[path(perm,s)]+=F(1,N)
    return dict(L)
def Mt(L):
    # I(X0,X1; X3 | X2)
    m=0.0
    by=defaultdict(lambda:defaultdict(float))
    for pth,p in L.items(): by[pth[2]][(pth[:2],pth[3])]+=float(p)
    for x2,d in by.items():
        W=sum(d.values()); ph=defaultdict(float); py=defaultdict(float)
        for (h,y),v in d.items(): ph[h]+=v; py[y]+=v
        for (h,y),v in d.items():
            if v>0: m+=v*log2(v*W/(ph[h]*py[y]))
    return m
def IHH(perm,mu):
    by=defaultdict(lambda:defaultdict(float))
    for s in range(N):
        pth=path(perm,s); by[pth[2]][(pth[:3],h2(perm,s))]+=mu[s]
    m=0.0
    for x2,d in by.items():
        W=sum(d.values())
        if W<=0: continue
        ph=defaultdict(float); py=defaultdict(float)
        for (h,y),v in d.items(): ph[h]+=v; py[y]+=v
        for (h,y),v in d.items():
            if v>1e-15: m+=v*log2(v*W/(ph[h]*py[y]))
    return m
targets={}
for perm in permutations(range(N)):
    L=law_uniform(perm); key=tuple(sorted(L.items()))
    targets.setdefault(key,L)
tg=[(k,L,Mt(L)) for k,L in targets.items()]
tg=[t for t in tg if t[2]>1e-12]
print("processes with M_t>0:",len(tg))
# for each perm compute classes
res={}
for perm in permutations(range(N)):
    cls=defaultdict(list)
    for s in range(N): cls[path(perm,s)].append(s)
    for k,L,M in tg:
        # feasibility: every path with P>0 must have a nonempty class; paths absent from L must... class mass must be 0
        if any(pth not in cls for pth in L): continue
        # states in classes whose path not in L must get mass 0
        free=[]; fixed=np.zeros(N)
        ok=True
        groups=[]
        for pth,ss in cls.items():
            P=float(L.get(pth,0))
            groups.append((ss,P))
        def unpack(z):
            mu=np.zeros(N); i=0
            for ss,P in groups:
                w=np.abs(z[i:i+len(ss)])+1e-300; i+=len(ss)
                mu[ss]=P*w/w.sum()
            return mu
        nz=sum(len(ss) for ss,_ in groups)
        best=1e9
        for trial in range(4):
            z0=np.random.rand(nz)+0.05
            r=minimize(lambda z: IHH(perm,unpack(z)),z0,method='Nelder-Mead',options={'xatol':1e-10,'fatol':1e-12,'maxiter':4000})
            best=min(best,r.fun)
        prev=res.get(k,(1e9,None))
        if best<prev[0]: res[k]=(best,perm)
att=0
for k,L,M in tg:
    b,perm=res[k]
    flag=abs(b-M)<1e-6
    att+=flag
    print(f"M_t={M:.6f} inf_any_prior={b:.6f} residual={b-M:.6f} {'ATTAINS' if flag else ''}")
print("attained for",att,"of",len(tg))
