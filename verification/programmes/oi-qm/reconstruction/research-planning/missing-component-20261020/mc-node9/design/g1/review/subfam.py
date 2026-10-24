from eng import *
import pickle
from collections import Counter
C=Cards(); std=QM(lift_tables(0,0,0))
_,eqF=pickle.load(open('fd_full.pkl','rb'))
FAM={'P1a single system A {sA,xA,zA,rA}':['sA','xA','zA','rA'],
     'P1b single system B {sB,xB,zB,rB}':['sB','xB','zB','rB'],
     'P2 coupling, no swaps {c,flips,rA,rB}':['c','xA','zA','xB','zB','rA','rB'],
     'P3 local only {sA,sB,flips,rA,rB}':['sA','sB','xA','zA','xB','zB','rA','rB']}
def kcouple(k): return (0,lambda op,x: (None if x+1>k else x+1) if op=='c' else x)
ok={}
for name,A in FAM.items():
    ok[name]={t:first_disagreement(C,QM(lift_tables(*t)),A) is None for t in TRIPLES}
    print(name,': triples == cards on all words of the sub-family:',sum(ok[name].values()),
          '| std QM == cards on it:',first_disagreement(C,std,A) is None)
def report(label,S):
    print(label,':',len(S),'triples; all == std QM on all FULL words:',all(eqF[t] for t in S),
          '; #classes by (sA,sB,c) twist:',len(S))
S123=[t for t in TRIPLES if all(ok[n][t] for n in FAM)]
report('P1 & P2 & P3',S123)
def nm(k): a,b=divmod(k,4); return NM[a]+NM[b]
print('   survivors:',[(nm(a),nm(b),nm(c)) for a,b,c in S123])
W6=['sA','c']*3
def w6(t):
    th=QM(lift_tables(*t)); S=th.init()
    for op in W6: S=th.gate(op,S)
    return th.read('rB',S).get(1,(0,))[0]
print('   W6 values among P1-P3 survivors:',Counter(str(w6(t)) for t in S123))
for k in (1,2,3):
    okk={t:first_disagreement(C,QM(lift_tables(*t)),FULL,extra=kcouple(k)) is None for t in TRIPLES}
    print('P4_%d full alphabet, at most %d couple(s), all lengths: std QM == cards: %s; triples == cards: %d'%(
        k,k,first_disagreement(C,std,FULL,extra=kcouple(k)) is None,sum(okk.values())))
    S=[t for t in S123 if okk[t]]
    report('   P1&P2&P3&P4_%d'%k,S)
    S=[t for t in TRIPLES if okk[t]]
    report('   P4_%d alone'%k,S)
