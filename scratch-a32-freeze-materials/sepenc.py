"""Exploration: the exponent encoding the S_SEP decide lemma will carry, checked independently
against the complex-number definition, and greedy covers per shape."""
import itertools, cmath
E = [[0,0,0,0],[0,1,2,3],[0,2,0,2],[0,3,2,1]]
def x(i,j,k): return E[i][k] + 4 - E[i][j]
def n(q):
    (i1,i2,i3),(j1,j2,j3) = q
    return x(i1,j1,j2) + x(i2,j2,j3) + x(i3,j3,j1)
# independent check against the complex definition at z = I
I = 1j
M = [[1,1,1,1],[1,I,-1,-I],[1,-1,1,-1],[1,-I,-1,I]]
def Fent(i,j,k): return (M[i][j].conjugate()*M[i][k])/4
IDX = [((a,b,c),(d,e,f)) for a in range(4) for b in range(4) for c in range(4) for d in range(4) for e in range(4) for f in range(4)]
for q in IDX:
    (i1,i2,i3),(j1,j2,j3) = q
    v = Fent(i1,j1,j2)*Fent(i2,j2,j3)*Fent(i3,j3,j1)
    assert abs(v - I**n(q)/64) < 1e-12
print('encoding matches mixedTriple F(I) on all 4096 coordinates')
ID=(0,1,2,3)
def sw(a,b):
    p=list(ID); p[a],p[b]=p[b],p[a]; return tuple(p)
R9=[(ID,ID),(ID,sw(2,3)),(ID,sw(1,2)),(sw(2,3),ID),(sw(2,3),sw(2,3)),(sw(2,3),sw(1,2)),(sw(1,2),ID),(sw(1,2),sw(2,3)),(sw(1,2),sw(1,2))]
def ap(r,q):
    (i1,i2,i3),(j1,j2,j3)=q; a,b=r
    return ((a[i1],a[i2],a[i3]),(b[j1],b[j2],b[j3]))
def swq(q):
    (i1,i2,i3),(j1,j2,j3)=q
    return ((j2,j3,j1),(i1,i2,i3))
def Kexp(ri,p):
    return 3*n(p) if ri==0 else n(ap(R9[ri],p))
def shape_exp(s,ri,pi,tau,p):
    q=ap((pi,tau),p); r=R9[ri]
    if s==1: return n(ap(r,q))
    if s==2: return 3*n(ap(r,q))
    if s==3: return 3*n(ap(r,swq(q)))
    if s==4: return n(ap(r,swq(q)))
PERMS=list(itertools.permutations(range(4)))
PAIRS=[(a,b) for a in PERMS for b in PERMS]
import json
covers={}
for s in (1,2,3,4):
    # candidate tests: (circle, coordinate)
    cand=[(ri,p) for ri in range(9) for p in IDX]
    sep={c:set() for c in cand}
    for k,(a,b) in enumerate(PAIRS):
        for c in cand:
            ri,p=c
            if Kexp(ri,p)%4 != shape_exp(s,ri,a,b,p)%4: sep[c].add(k)
    left=set(range(len(PAIRS))); cov=[]
    while left:
        c=max(cand,key=lambda c: len(sep[c]&left)); 
        assert sep[c]&left, ('uncoverable', s, len(left))
        cov.append(c); left-=sep[c]
    covers[s]=cov
    print('shape',s,'cover size',len(cov),cov)
json.dump({str(k):v for k,v in covers.items()},open('covers.json','w'))
