"""Coordinator check of the owner's temporal-retention note (2026-10-22), from Main.md:290's rule.
Five-site graph (0,1),(1,2),(0,3),(1,4), hidden site 1, u3 = u4 = 0; four-site graph (0,1),(1,2),(0,3),
hidden site 1, memory (u3, v3) = (0, 0)."""
from itertools import product
from collections import defaultdict
def nb(E,x): return [b for a,b in E if a==x]+[a for a,b in E if b==x]
def step(st,E,N):
    u,v=st; return (tuple(sum(u[z] for z in nb(E,x))%2 ^ v[x] for x in range(N)), u)
def traj(st,E,N,T):
    out=[st]
    for _ in range(T): st=step(st,E,N); out.append(st)
    return out
def support(states,E,N,T,VIS,record,at):
    fib=defaultdict(set)
    for st in states:
        tr=traj(st,E,N,T); fib[record(tr)].add((tr[at][0][1],tr[at][1][1]))
    sz={len(x) for x in fib.values()}; return min(sz),max(sz)
E5=[(0,1),(1,2),(0,3),(1,4)]; V5=(0,2,3,4)
S5=[((a,b,c,0,0),(d,e,f,p,s)) for a,b,c,d,e,f,p,s in product((0,1),repeat=8)]
upos=lambda tr,t,V: tuple(tr[t][0][x] for x in V)
print('five-site, u-only at t=3:',support(S5,E5,5,3,V5,lambda tr: upos(tr,3,V5),3))
print('five-site, u-only at t=2 (hidden at t=2):',support(S5,E5,5,3,V5,lambda tr: upos(tr,2,V5),2))
print('five-site, u-only at t=2 and t=3 retained (hidden at t=3):',support(S5,E5,5,3,V5,lambda tr: upos(tr,2,V5)+upos(tr,3,V5),3))
# the three-bit formulas
for st in S5:
    tr=traj(st,E5,5,3); (u2,v2),(u3,v3)=tr[2],tr[3]
    assert u3[1]==u2[0]^u2[2] and v3[1]==u3[0]
print('u1(3) = u0(2)+u2(2) and v1(3) = u0(3) on all 256 states')
# period and terminal u-only minimum over one period
T5=next(t for t in range(1,40) if all(traj(s,E5,5,t)[-1]==s for s in [((a,b,c,q,r),(d,e,f,p,s_)) for a,b,c,q,r,d,e,f,p,s_ in product((0,1),repeat=10)]))
print('five-site period:',T5,' u-only terminal support min over t=0..%d:'%(T5-1),
      min(support(S5,E5,5,t,V5,lambda tr,t=t: upos(tr,t,V5),t)[0] for t in range(T5)))
E4=[(0,1),(1,2),(0,3)]; V4=(0,2,3)
S4=[((a,b,c,0),(d,e,f,0)) for a,b,c,d,e,f in product((0,1),repeat=6)]
print('four-site u-only terminal support min over t=0..9:',
      min(support(S4,E4,4,t,V4,lambda tr,t=t: upos(tr,t,V4),t)[0] for t in range(10)))
print('four-site u-only at t=2 and t=3 retained:',support(S4,E4,4,3,V4,lambda tr: upos(tr,2,V4)+upos(tr,3,V4),3))
