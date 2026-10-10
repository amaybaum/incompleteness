"""K2.2a negative controls, exact (Fractions), incremental echelon Lie closure. Prints as it goes."""
import sys
exec(open('k22a_closure.py').read().split("surv={0:")[0])
from fractions import Fraction as Fr
class Span:
    def __init__(s): s.rows={}  # pivot -> normalised row (list of Fr)
    def reduce(s,v):
        v=[Fr(x) for x in v]
        for p,r in s.rows.items():
            if v[p]!=0:
                f=v[p]; v=[a-f*b for a,b in zip(v,r)]
        return v
    def add(s,v):
        v=s.reduce(v)
        p=next((i for i,x in enumerate(v) if x!=0),None)
        if p is None: return False
        pv=v[p]; v=[x/pv for x in v]
        for q in list(s.rows):
            r=s.rows[q]
            if r[p]!=0:
                f=r[p]; s.rows[q]=[a-f*b for a,b in zip(r,v)]
        s.rows[p]=v; return True
def lie_dim(gens, cap=256):
    S=Span(); basis=[]
    queue=[g for g in gens]
    while queue:
        g=queue.pop()
        if S.add(flat(g)):
            for b in basis:
                queue.append(br(g,b))
            basis.append(g)
            if len(basis)>=cap: break
    return basis
def closure(G):
    pows=[[[int(a==b) for b in range(16)] for a in range(16)]]; P=G
    while P!=pows[0]: pows.append(P); P=mul(P,G)
    gens=[]
    for Pw in pows:
        Pi=inv_signed_perm(Pw); gens+=[mul(mul(Pw,x),Pi) for x in local]
    L=lie_dim(gens); return len(L), same(L,su4), same(L,su4PT), len(pows)
Id=[[int(a==b) for b in range(16)] for a in range(16)]
SW=[[int(b==(a%4)*4+a//4) for b in range(16)] for a in range(16)]
Nm=[[1,0,0,0],[0,1,0,0],[0,0,-1,0],[0,0,0,-1]]
for name,G in [('identity',Id),('SWAP',SW),('N(x)N',kron(Nm,Nm))]+[('failing SO-class %d' % i, M(Gs[cs[i][0]])) for i in (2,3,4,5,8,9,14,15)]+[('surviving SO-class 1 (re-check)',M(Gs[cs[1][0]]))]:
    print('%-32s dim, =su4, =PT su4 PT, order:' % name, closure(G), flush=True)
