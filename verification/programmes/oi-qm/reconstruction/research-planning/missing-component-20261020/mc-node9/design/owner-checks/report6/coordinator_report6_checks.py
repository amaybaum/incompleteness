"""Coordinator checks for owner report 6, written from Main.md:290's rule and the declared graph,
without the report's hand-coded update. u'_x = XOR_{z~x} u_z XOR v_x, v'_x = u_x."""
from itertools import product
from collections import defaultdict
EDGES=[(0,1),(1,2),(0,3)]
def nbrs(E,x): return [b for a,b in E if a==x]+[a for a,b in E if b==x]
def step(st,E):
    u,v=st
    return (tuple(sum(u[z] for z in nbrs(E,x))%2 ^ v[x] for x in range(4)), u)
def run(st,t,E=EDGES):
    for _ in range(t): st=step(st,E)
    return st
VIS=(0,2,3)
def rec(st): u,v=st; return tuple((u[x],v[x]) for x in VIS)
def hid(st): u,v=st; return (u[1],v[1])
allst=[(tuple(u),tuple(v)) for u in product((0,1),repeat=4) for v in product((0,1),repeat=4)]
# period
s2=lambda s: run(s,10)
assert all(s2(s)==s for s in allst) and not all(run(s,5)==s for s in allst)
print('global period divides 10, not 5:',True, ' period 2 fails:', not all(run(s,2)==s for s in allst))
# closed forms after three updates, initial core (a,b,c,d,e,f) = (u0,u1,u2,v0,v1,v2), memory (q,p) = (u3,v3)
for a,b,c,d,e,f,q,p in product((0,1),repeat=8):
    st=run(((a,b,c,q),(d,e,f,p)),3); u,v=st
    U0,U2,V0,V2,Q,P=u[0],u[2],v[0],v[2],u[3],v[3]
    assert (U0,U2,V0,V2,Q,P)==(b^d^f, d^q, a^c^e^p, a^e, c^e, b^d)
    assert hid(st)==(V2^p, U0^q)
    # decoder
    dd=U2^q; bb=P^dd; ff=U0^P; cc=V0^V2^p; ee=Q^cc; aa=V2^ee
    assert (aa,bb,cc,dd,ee,ff)==(a,b,c,d,e,f)
print('closed forms, hidden identity and decoder: all 256 inputs')
# support table over time with known memory (0,0)
def support(t,E=EDGES,mem=((0,0),)):
    fib=defaultdict(set)
    for core in product((0,1),repeat=6):
        for q,p in mem:
            a,b,c,d,e,f=core; st=run(((a,b,c,q),(d,e,f,p)),t,E); fib[rec(st)].add(hid(st))
    sizes={len(s) for s in fib.values()}; assert len(sizes)==1; return sizes.pop()
print('known-pair support t=0..9:',[support(t) for t in range(10)])
print('memory edge removed, support t=0..9:',[support(t,[(0,1),(1,2)]) for t in range(10)])
print('unknown memory pair at t=3:',support(3,mem=tuple(product((0,1),repeat=2))),
      ' known parity at t=3:',support(3,mem=((0,0),(1,1))))
