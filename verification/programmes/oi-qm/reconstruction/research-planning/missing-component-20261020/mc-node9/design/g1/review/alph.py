from eng import *
from collections import Counter
import pickle
std=QM(lift_tables(0,0,0)); C=Cards()
_,eqfull=pickle.load(open('fd_full.pkl','rb'))
ALPHS={'full':FULL,
 'no flips {sA,sB,c,rA,rB}':['sA','sB','c','rA','rB'],
 '{sA,c,rA,rB}':['sA','c','rA','rB'],
 'no sB {sA,c,4 flips,rA,rB}':['sA','c','xA','zA','xB','zB','rA','rB'],
 'K-G1 {sA,c,rB}':['sA','c','rB'],
}
res={}
for name,A in ALPHS.items():
    fd={}; eq={}
    for t in TRIPLES:
        th=QM(lift_tables(*t)); fd[t]=first_disagreement(C,th,A); eq[t]=first_disagreement(std,th,A) is None
    res[name]=(fd,eq)
    print('==',name,'| std-QM vs cards first disagreement:',first_disagreement(C,std,A),
          '| fd histogram:',sorted(Counter(fd.values()).items(),key=lambda x:(x[0] is None,x[0] or 0)))
    print('   triples == std QM over this alphabet:',sum(eq.values()))
    for L in range(1,10):
        s=[t for t in TRIPLES if fd[t] is None or fd[t]>L]
        if not s: print('   L=%d: 0 survivors'%L); break
        print('   L=%d: %4d survivors; all == std QM over alphabet: %s; all == std QM over FULL: %s; W6-relevant (sA,c) pairs: %d'%(
            L,len(s),all(eq[t] for t in s),all(eqfull[t] for t in s),len({(t[0],t[2]) for t in s})))
pickle.dump(res,open('alph.pkl','wb'))
