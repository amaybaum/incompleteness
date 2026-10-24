"""Coordinator checks for owner reports of 2026-10-22 (product-ready memory, relay, two-record mask,
heralding closure), written from Main.md:290's rule without the reports' code. Exact integers/Fractions."""
from itertools import product
from collections import defaultdict
from fractions import Fraction as Fr
def nb(E,x): return [b for a,b in E if a==x]+[a for a,b in E if b==x]
def step(st,E):
    u,v=st; n=len(u); return (tuple(sum(u[z] for z in nb(E,x))%2 ^ v[x] for x in range(n)), u)
def run(st,t,E):
    for _ in range(t): st=step(st,E)
    return st
def states(n,clean_u,clean_v):
    free=[('u',i) for i in range(n) if i not in clean_u]+[('v',i) for i in range(n) if i not in clean_v]
    for bits in product((0,1),repeat=len(free)):
        u=[0]*n; v=[0]*n
        for (k,i),b in zip(free,bits): (u if k=='u' else v)[i]=b
        yield (tuple(u),tuple(v))
def period(n,E):
    basis=[]
    for i in range(2*n):
        b=[0]*(2*n); b[i]=1; basis.append((tuple(b[:n]),tuple(b[n:])))
    t=1; cur=[step(s,E) for s in basis]
    while cur!=basis: cur=[step(s,E) for s in cur]; t+=1
    return t
def supports(S,E,t,vis,hid=1,extra=None):
    fib=defaultdict(set)
    for s in S:
        u,v=run(s,t,E); rec=tuple(u[x] for x in vis)+(extra(u,v) if extra else ())
        fib[rec].add((u[hid],v[hid]))
    return sorted({len(x) for x in fib.values()})
# A. product-ready six-site memory
E6=[(0,1),(1,2),(0,3),(1,4),(0,5),(2,5)]; V6=(0,2,3,4,5)
S6=list(states(6,{5},{3,4}))
assert len(S6)==512 and period(6,E6)==18
for s in S6:
    u1,v1=run(s,1,E6); u2,v2=run(s,2,E6)
    f=u1[0]^u1[2]; assert u2[5]==f==u2[1]
hs=[supports(S6,E6,t,V6) for t in range(18)]
print('A six-site: period 18; u5(2)=u1(2)=u0(1)+u2(1) on 512 states')
print('  hidden support by t:',[h[0] for h in hs])
print('  with v5(2) also read:',supports(S6,E6,2,V6,extra=lambda u,v:(v[5],)))
rec=[]
for t in range(18):
    fib=defaultdict(set)
    for s in S6:
        u,_=run(s,t,E6); u1,_=run(s,1,E6); fib[tuple(u[x] for x in V6)].add(u1[0]^u1[2])
    if all(len(x)==1 for x in fib.values()): rec.append(t)
print('  historical parity recoverable from visible u at t =',rec)
# B. relay, k = 0..3
for k in range(4):
    n=6+k; E=E6+[(j-1,j) for j in range(6,n)]; V=tuple(x for x in range(n) if x!=1)
    cu={5}|{j for j in range(6,n) if j%2==1}; cv={3,4}|{j for j in range(6,n) if j%2==0}
    S=list(states(n,cu,cv)); P=period(n,E)
    for s in S:
        u1,_=run(s,1,E); f=u1[0]^u1[2]
        for r in range(k+1): assert run(s,2+r,E)[0][5+r]==f
    mn=min(supports(S,E,t,V)[0] for t in range(P))
    print('B relay k=%d: %d states, period %d, u_{5+r}(2+r)=f for r<=%d, min hidden support over period %d'%(k,len(S),P,k,mn))
# C. seven-site masked conjugate
E7=E6+[(5,6)]; V7=(0,2,3,4,5,6); S7=list(states(7,{5},{3,4,6}))
fib=defaultdict(lambda: defaultdict(int))
for s in S7:
    u,v=run(s,2,E7); r=s[0][6]
    assert (u[0]^u[6])==(v[1]^r) and u[1]==u[5]
    assert run(s,12,E7)[0][4]==r
    fib[tuple(u[x] for x in V7)][r]+=1
assert all(c[0]==c[1] for c in fib.values())
print('C seven-site: m = u0(2)+u6(2) = v1(2)+r, r fair on all %d complete records; u4(12)=u6(0)'%len(fib))
# D. heralding on four sites, edge (0,1), coins at 2,3
E4=[(0,1)]; S4=list(states(4,{2,3},{0,1}))
acc=defaultdict(int); late=defaultdict(int); sel=0
for s in S4:
    q,Q=s[0][0],s[0][1]; c,d=s[1][2],s[1][3]
    u,v=run(s,1,E4); assert (u[0],v[0],u[1],v[1],u[2],u[3])==(Q,q,q,Q,c,d)
    if q==0 or (c,d)==(0,0):
        sel+=1; acc[(u[0],v[0])]+=1
        u6,v6=run(s,6,E4); late[(u6[0],v6[0])]+=1
tot=sum(acc.values())
print('D heralding: success',Fr(sel,16),' accepted output',{k:Fr(x,tot) for k,x in sorted(acc.items())})
print('  free-history countercontrol at t=6',{k:Fr(x,tot) for k,x in sorted(late.items())})
# K1: vertices of {0<=p<=1/2, sum p = 1} on F2^2 are the six half-half pairs; every pair is an affine line
pts=list(product((0,1),repeat=2))
for a,b in [(a,b) for i,a in enumerate(pts) for b in pts[i+1:]]:
    d=(a[0]^b[0],a[1]^b[1]); normal=[w for w in [(0,1),(1,0),(1,1)] if (w[0]*d[0]+w[1]*d[1])%2==0][0]
    line={x for x in pts if ((x[0]^a[0])*normal[0]+(x[1]^a[1])*normal[1])%2==0}
    assert line=={a,b}
print('  K1: all six two-point subsets of F2^2 are affine lines (vertex set of {p_x <= 1/2})')
