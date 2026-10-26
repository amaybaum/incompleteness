from fractions import Fraction as Fr
from itertools import product
import sys
sys.path.insert(0,'.')
from aghp_check import polys_primitive, records  # local probe module only
n=5; fam=polys_primitive(n)
for K in (5,6,7):
    N=1<<(K+1); q=Fr(1,N)
    D=[]
    for p in fam:
        R=records(p,n,K); cnt={}
        for X in R:
            k=int(''.join(map(str,X)),2); cnt[k]=cnt.get(k,0)+1
        D.append({k:Fr(c,len(R)) for k,c in cnt.items()})
    best=Fr(0)
    for s in product((1,-1),repeat=len(fam)):
        if s[0]==-1: continue
        tot=Fr(0)
        for x in range(N):
            v=sum(si*(Di.get(x,Fr(0))-q) for si,Di in zip(s,D))
            if v>0: tot+=v
        best=max(best,tot/len(fam))
    print("K",K,"B3w K0-avg (whole record as window)",best,float(best))
