from fractions import Fraction as F
import itertools
# site k bits (a,b); u=(-1)^a, v=(-1)^b; x=(u-v)/2, z=(u+v)/2  (report §4)
def coords(a,b):
    u,v=(-1)**a,(-1)**b; return F(u-v,2),F(u+v,2)
vertex={('X',1):None,('X',-1):None,('Z',1):None,('Z',-1):None}
for a in (0,1):
    for b in (0,1):
        x,z=coords(a,b)
        if x!=0: vertex[('X',int(x))]=(a,b)
        if z!=0: vertex[('Z',int(z))]=(a,b)
def G(s):  # (aA,bA,aB,bB) -> (aA, bA^bB, aB^aA, bB)
    aA,bA,aB,bB=s; return (aA,bA^bB,aB^aA,bB)
def read(dist,site,axis,sign):  # unnormalized branch: weight (1+sign*coord)/2, reset site to vertex
    out={}
    for s,w in dist.items():
        a,b=s[2*site],s[2*site+1]; x,z=coords(a,b); c=x if axis=='X' else z
        p=w*(1+sign*c)/2
        if p:
            va,vb=vertex[(axis,sign)]; t=list(s); t[2*site],t[2*site+1]=va,vb; t=tuple(t)
            out[t]=out.get(t,0)+p
    return out
def prep(Alabels):
    d={}
    for (aA,bA) in Alabels:
        for aB,bB in itertools.product((0,1),repeat=2):
            d[(aA,bA,aB,bB)]=F(1,len(Alabels)*4)
    return d
PZ=[vertex[('Z',1)],vertex[('Z',-1)]]; PX=[vertex[('X',1)],vertex[('X',-1)]]
for name,L in (('PZ',PZ),('PX',PX)):
    d=prep(L)
    d=read(d,1,'X',1); d={G(s):w for s,w in d.items()}; d=read(d,1,'X',1); d=read(d,0,'X',1)
    print(name,'P(+++) =',sum(d.values()))
