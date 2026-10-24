from eng import *
from collections import Counter
import time,sys
std=QM(lift_tables(0,0,0)); C=Cards()
t0=time.time()
fd={}; eqstd={}
for t in TRIPLES:
    th=QM(lift_tables(*t))
    fd[t]=first_disagreement(C,th,FULL)
    eqstd[t]=first_disagreement(std,th,FULL) is None
print('first card/lift disagreement length over 4096 triples:',sorted(Counter(fd.values()).items()))
for L in range(1,8):
    surv=[t for t in TRIPLES if fd[t] is None or fd[t]>L]
    print('L=%d survivors %d'%(L,len(surv)), ' all == std QM (all words):', all(eqstd[t] for t in surv) if surv else '-')
print('triples == std QM on all words:',sorted(t for t in TRIPLES if eqstd[t]))
print('time %.1fs'%(time.time()-t0))
import pickle; pickle.dump((fd,eqstd),open('fd_full.pkl','wb'))
