from fractions import Fraction as F
from collections import defaultdict
p=[0,3,4,1,5,2]
for k in range(1,7):
    # joint over (x_0..x_{k+1}) from uniform over 6 states
    J=defaultdict(F)
    for s in range(6):
        xs=[];z=s
        for _ in range(k+2): xs.append(z//3); z=p[z]
        J[tuple(xs)]+=F(1,6)
    # gap: exist two positive histories x_<=k with same x_k and different P(x_{k+1}|.)
    cond=defaultdict(lambda: defaultdict(F)); tot=defaultdict(F)
    for h,w in J.items(): cond[h[:-1]][h[-1]]+=w; tot[h[:-1]]+=w
    by=defaultdict(set)
    for h in cond: by[h[-1]].add(tuple(cond[h][j]/tot[h] for j in range(2)))
    print(k, any(len(v)>1 for v in by.values()))
