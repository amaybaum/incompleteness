from eng import *
from collections import deque, Counter
import pickle
C=Cards(); std=QM(lift_tables(0,0,0))
_,eqF=pickle.load(open('fd_full.pkl','rb'))
def kcouple(k): return (0,lambda op,x: (None if x+1>k else x+1) if op=='c' else x)
# shortest distinguishing word, with the word itself
def witness(T1,T2,A,extra=None):
    x0=extra[0] if extra else 0
    st=(T1.init(),T2.init(),x0); seen={st}; Q=deque([(st,())])
    while Q:
        (a,b,x),w=Q.popleft()
        for op in A:
            x2=extra[1](op,x) if extra else 0
            if x2 is None: continue
            if isread(op):
                ra,rb=T1.read(op,a),T2.read(op,b)
                if {o:p for o,(p,_) in ra.items()}!={o:p for o,(p,_) in rb.items()}: return w+(op,),{o:str(p) for o,(p,_) in ra.items()},{o:str(p) for o,(p,_) in rb.items()}
                nx=[(ra[o][1],rb[o][1],x2,w+(op+'=%d'%o,)) for o in ra]
            else: nx=[(T1.gate(op,a),T2.gate(op,b),x2,w+(op,))]
            for a2,b2,x3,w2 in nx:
                k=(a2,b2,x3)
                if k not in seen: seen.add(k); Q.append((k,w2))
print('cards vs std QM, <=2 couples, shortest distinguishing word:',witness(C,std,FULL,kcouple(2)))
print('cards vs std QM, full alphabet:',witness(C,std,FULL))
ALTS={'no flips':['sA','sB','c','rA','rB'],'{sA,c,rA,rB}':['sA','c','rA','rB'],'no sB':['sA','c','xA','zA','xB','zB','rA','rB']}
for name,A in ALTS.items():
    okk=[t for t in TRIPLES if first_disagreement(C,QM(lift_tables(*t)),A,extra=kcouple(1)) is None]
    eqA=[t for t in okk if first_disagreement(std,QM(lift_tables(*t)),A) is None]
    print('P4_1 over',name,': std==cards:',first_disagreement(C,std,A,extra=kcouple(1)) is None,'| passing',len(okk),
          '| of which == std QM over alphabet',len(eqA),'| (sA,c) pairs:',len({(t[0],t[2]) for t in okk}))
# locality-restricted lifts: swap_A twist supported on A, swap_B twist on B (couple twist unrestricted)
LOC=[t for t in TRIPLES if t[0]%4==0 and t[1]//4==0]
print('local-swap-lift triples:',len(LOC))
for name,A in [('full',FULL)]+list(ALTS.items()):
    fd={t:first_disagreement(C,QM(lift_tables(*t)),A) for t in LOC}
    row=[]
    for L in range(2,11):
        s=[t for t in LOC if fd[t] is None or fd[t]>L]
        row.append((L,len(s),len({(t[0],t[2]) for t in s}),all(first_disagreement(std,QM(lift_tables(*t)),A) is None for t in s) if s else '-'))
        if not s: break
    print('local lifts,',name,': (L, survivors, (sA,c) pairs, all==stdQM over alph):',row)
