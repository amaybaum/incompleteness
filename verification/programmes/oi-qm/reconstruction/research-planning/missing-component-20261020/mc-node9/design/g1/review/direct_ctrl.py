# Control: direct comparison of full joint record distributions word by word (no BFS-depth argument).
from eng import *
import pickle
def joint(T,word):
    br={():(F(1),T.init())}
    for op in word:
        nb={}
        for rec,(p,s) in br.items():
            if isread(op):
                for o,(q,s2) in T.read(op,s).items(): nb[rec+(o,)]=(p*q,s2)
            else: nb[rec]=(p,T.gate(op,s))
        br=nb
    return {r:p for r,(p,_) in br.items()}
L=3
words=[w for l in range(1,L+1) for w in product(FULL,repeat=l)]
C=Cards(); cj={w:joint(C,w) for w in words}
fd,_=pickle.load(open('fd_full.pkl','rb'))
mism=0; cnt={2:0,3:0}
for t in TRIPLES:
    th=QM(lift_tables(*t))
    ok2=all(joint(th,w)==cj[w] for w in words if len(w)<=2)
    ok3=ok2 and all(joint(th,w)==cj[w] for w in words if len(w)==3)
    cnt[2]+=ok2; cnt[3]+=ok3
    if ok2!=(fd[t] is None or fd[t]>2) or ok3!=(fd[t] is None or fd[t]>3): mism+=1
print('direct word-level: L<=2 pass',cnt[2],' L<=3 pass',cnt[3],' disagreements with BFS-depth method:',mism)
