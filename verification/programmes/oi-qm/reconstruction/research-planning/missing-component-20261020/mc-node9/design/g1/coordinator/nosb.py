import sys,itertools
from collections import Counter
src=open('corr.py').read().split("alphabet=")[0].replace("L=int(sys.argv[1])","L=0")
exec(src)
alphabet=['sA','c','xA','zA','xB','zB','rA','rB']
base={'xA':(kron(X,I),0),'zA':(kron(Z,I),0),'xB':(kron(I,X),0),'zB':(kron(I,Z),0)}
HA=kron(Hs,I)
W6=('sA','c')*3+('rB',)
def G_of(a,c):
    G=dict(base); G['sA']=(P2[a].dot(HA),1); G['c']=(P2[c].dot(CN),0); return G
cards={}
def words(L): return [w for l in range(1,L+1) for w in itertools.product(alphabet,repeat=l)]
for L in (5,6):
    ws=words(L); cw={w:card_records(w) for w in ws}
    for local in (False,True):
        A=[0,4,8,12] if local else range(16)   # P2 index a*4+b : local => b==0 (I on B)
        surv=[(a,c) for a in A for c in range(16) if all(qm_records(w,G_of(a,c))==cw[w] for w in ws)]
        vals=Counter(sum(v for r,v in qm_records(W6,G_of(a,c)).items() if r[-1]==1) for a,c in surv)
        print('no swap_B, L',L,'local swap lift' if local else 'any swap lift','survivors',len(surv),'W6 values',dict(vals))
