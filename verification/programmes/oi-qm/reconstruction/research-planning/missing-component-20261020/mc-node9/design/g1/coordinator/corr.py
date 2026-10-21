import numpy as np, itertools, sys
from fractions import Fraction as F
from collections import Counter
L=int(sys.argv[1])
I=np.eye(2,dtype=object); X=np.array([[0,1],[1,0]],dtype=object); Z=np.array([[1,0],[0,-1]],dtype=object)
Hs=np.array([[1,1],[1,-1]],dtype=object); CN=np.array([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]],dtype=object)
P1=[I,X,Z,X.dot(Z)]; P2=[np.kron(a,b) for a in P1 for b in P1]
kron=np.kron
# ---- card theory: distribution over (qA,pA,qB,pB) as dict
def card_apply(op,dist):
    out={}
    for (qA,pA,qB,pB),w in dist.items():
        if op=='sA': s=(pA,qA,qB,pB)
        elif op=='sB': s=(qA,pA,pB,qB)
        elif op=='c': s=(qA,pA^pB,qB^qA,pB)
        elif op=='xA': s=(qA^1,pA,qB,pB)
        elif op=='zA': s=(qA,pA^1,qB,pB)
        elif op=='xB': s=(qA,pA,qB^1,pB)
        elif op=='zB': s=(qA,pA,qB,pB^1)
        out[s]=out.get(s,0)+w
    return out
def card_read(sys_,dist):   # returns {outcome: (prob, dist)}
    res={}
    for (qA,pA,qB,pB),w in dist.items():
        r = qA if sys_=='A' else qB
        for f in (0,1):
            s=(qA,f,qB,pB) if sys_=='A' else (qA,pA,qB,f)
            d=res.setdefault(r,{}); d[s]=d.get(s,0)+w/2
    return res
def card_records(word):
    br={():{(0,a,0,b):F(1,4) for a in (0,1) for b in (0,1)}}
    for op in word:
        nb={}
        for rec,d in br.items():
            if op in ('rA','rB'):
                for r,dd in card_read(op[1],d).items(): nb[rec+(r,)]=dd
            else: nb[rec]=card_apply(op,d)
        br=nb
    return {rec:sum(d.values()) for rec,d in br.items() if sum(d.values())>0}
# ---- lifted QM theory: unnormalized integer vectors with scale exponent
P0A=kron(np.diag([1,0]),I).astype(object);P1A=kron(np.diag([0,1]),I).astype(object)
P0B=kron(I,np.diag([1,0])).astype(object);P1B=kron(I,np.diag([0,1])).astype(object)
def qm_records(word,G):
    br={():(np.array([1,0,0,0],dtype=object),0)}   # vec, number of sqrt2 factors
    for op in word:
        nb={}
        for rec,(v,k) in br.items():
            if op=='rA':
                for r,P in ((0,P0A),(1,P1A)): nb[rec+(r,)]=(P.dot(v),k)
            elif op=='rB':
                for r,P in ((0,P0B),(1,P1B)): nb[rec+(r,)]=(P.dot(v),k)
            else:
                M,dk=G[op]; nb[rec]=(M.dot(v),k+dk)
        br=nb
    out={}
    for rec,(v,k) in br.items():
        p=F(sum(int(x)**2 for x in v),2**k)
        if p>0: out[rec]=p
    return out
alphabet=['sA','sB','c','xA','zA','xB','zB','rA','rB']
words=[w for l in range(1,L+1) for w in itertools.product(alphabet,repeat=l)]
cards={w:card_records(w) for w in words}
base={'xA':(kron(X,I),0),'zA':(kron(Z,I),0),'xB':(kron(I,X),0),'zB':(kron(I,Z),0)}
HA=kron(Hs,I); HB=kron(I,Hs)
cnt=Counter(); passing=[]
for a,b,c in itertools.product(range(16),repeat=3):
    G=dict(base); G['sA']=(P2[a].dot(HA),1); G['sB']=(P2[b].dot(HB),1); G['c']=(P2[c].dot(CN),0)
    ok=all(qm_records(w,G)==cards[w] for w in words)
    if ok: passing.append((a,b,c))
print('L =',L,'words',len(words),'lift triples agreeing with cards on all words <= L:',len(passing))
# do the passing triples give QM-standard W6?
def w6(G):
    r=qm_records(('sA','c')*3+('rB',),G); return r.get(('sA',)*0+(1,),0) if False else sum(p for rec,p in r.items() if rec[-1]==1)
vals=Counter()
for a,b,c in passing:
    G=dict(base); G['sA']=(P2[a].dot(HA),1); G['sB']=(P2[b].dot(HB),1); G['c']=(P2[c].dot(CN),0)
    vals[w6(G)]+=1
print('W6 values among passing triples:',dict(vals))
