exec(open('corr.py').read().split("alphabet=")[0].replace("L=int(sys.argv[1])","L=4"))
alphabet=['sA','sB','c','xA','zA','xB','zB','rA','rB']
import itertools
base={'xA':(kron(X,I),0),'zA':(kron(Z,I),0),'xB':(kron(I,X),0),'zB':(kron(I,Z),0)}
HA=kron(Hs,I); HB=kron(I,Hs)
def G_of(a,b,c):
    G=dict(base); G['sA']=(P2[a].dot(HA),1); G['sB']=(P2[b].dot(HB),1); G['c']=(P2[c].dot(CN),0); return G
w4=[w for l in range(1,5) for w in itertools.product(alphabet,repeat=l)]
cards4={w:card_records(w) for w in w4}
passing=[t for t in itertools.product(range(16),repeat=3) if all(qm_records(w,G_of(*t))==cards4[w] for w in w4)]
print('passing at L<=4:',passing)
std=G_of(0,0,0)
w5=[w for w in itertools.product(alphabet,repeat=5)]
import random; random.seed(0); w7=[tuple(random.choice(alphabet) for _ in range(7)) for _ in range(20000)]
for t in passing:
    G=G_of(*t)
    e5=all(qm_records(w,G)==qm_records(w,std) for w in w5)
    e7=all(qm_records(w,G)==qm_records(w,std) for w in w7)
    print(t,'== standard QM on all length-5 words:',e5,'; on 20000 random length-7 words:',e7)
