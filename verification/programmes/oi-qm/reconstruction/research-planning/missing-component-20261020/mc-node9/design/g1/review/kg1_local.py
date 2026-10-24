import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from eng import *
from collections import Counter
C=Cards(); std=QM(lift_tables(0,0,0))
A=['sA','c','rB']
loc_sA=[4*a for a in range(4)]   # P = (a on A) x (I on B)
res={}
for a in loc_sA:
    for c in range(16):
        th=QM(lift_tables(a,0,c)); res[(a,c)]=(first_disagreement(C,th,A), first_disagreement(std,th,A) is None)
h=Counter(v[0] for v in res.values())
print('K-G1, local swap_A lifts (64 (sA,c) pairs): first-disagreement histogram',sorted(h.items(),key=lambda x:(x[0] is None,x[0] or 0)))
mx=max(v[0] for v in res.values() if v[0] is not None) if all(v[0] is not None for v in res.values()) else None
print('max ell:',mx,' argmax pairs:',sorted(k for k,v in res.items() if v[0]==mx),' all ==stdQM over K-G1:',all(res[k][1] for k,v in res.items() if v[0]==mx))
print('pairs at ell=6:',sorted(k for k,v in res.items() if v[0]==6))
