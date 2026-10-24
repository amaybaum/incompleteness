from eng import *
std=lift_tables(0,0,0)
def adW(w): return conj_table(PAULI[w],1)
def compose(t2,t1):  # t2 after t1
    return {k:(t1[k][0]*t2[t1[k][1]][0],t2[t1[k][1]][1]) for k in range(16)}
surv=[(0,0,0),(0,3,8),(12,0,0),(12,3,8)]
Wset={'I':0,'Z_A':8,'Z_B':2,'Z_AZ_B':10}
found={}
for wn,w in Wset.items():
    A=adW(w)
    conjd={op:compose(A,compose(std[op],A)) for op in std}   # Ad(W) Ad(U) Ad(W)  (Ad(W) is an involution)
    for t in surv:
        if lift_tables(*t)==conjd: found[t]=wn
    fixes_init=frozenset((s*A[k][0],A[k][1]) for s,k in QM0)==QM0
    fixes_reads=A[ZA]==(1,ZA) and A[ZB]==(1,ZB)
    commutes_flips=all(compose(A,FLIPS[f])==compose(FLIPS[f],A) for f in FLIPS)
    print('W=%-7s fixes |00> record group: %s; fixes Z_A,Z_B records: %s; commutes with every flip: %s'%(wn,fixes_init,fixes_reads,commutes_flips))
print('survivor -> W with survivor = Ad(W) std Ad(W)^-1:',found)
