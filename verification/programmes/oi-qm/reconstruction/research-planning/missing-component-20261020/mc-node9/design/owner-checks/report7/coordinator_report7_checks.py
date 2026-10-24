"""Coordinator checks for owner report 7, built from Main.md:290's rule on the declared graph,
not from the report's checker. Linear functionals over F2 on (u0..u4, v0..v4) are 10-bit masks."""
from itertools import product, combinations
from collections import defaultdict
N=5; EDGES=[(0,1),(1,2),(0,3),(1,4)]; VIS=(0,2,3,4); HID=1
def nb(E,x): return [b for a,b in E if a==x]+[a for a,b in E if b==x]
def step(st,E):
    u,v=st; return (tuple(sum(u[z] for z in nb(E,x))%2 ^ v[x] for x in range(N)), u)
def run(st,t,E):
    for _ in range(t): st=step(st,E)
    return st
def admissible():   # u3 = u4 = 0; everything else free
    for a,b,c,d,e,f,p,s in product((0,1),repeat=8): yield ((a,b,c,0,0),(d,e,f,p,s))
def support(E,readout):
    fib=defaultdict(set)
    for st in admissible():
        u,v=run(st,3,E); fib[readout(u,v)].add((u[HID],v[HID]))
    sz={len(x) for x in fib.values()}; assert len(sz)==1; return sz.pop()
whole=lambda u,v: tuple((u[x],v[x]) for x in VIS)
for name,E in [('both',EDGES),('(0,3) only',EDGES[:3]),('(1,4) only',EDGES[:2]+EDGES[3:]),('neither',EDGES[:2])]:
    print(name,'whole-site support at t=3:',support(E,whole))
print('positions-only (all visible u) support:',support(EDGES,lambda u,v: tuple(u[x] for x in VIS)))
print('momenta-only (all visible v) support:',support(EDGES,lambda u,v: tuple(v[x] for x in VIS)))
# hidden identity
for st in admissible():
    u,v=run(st,3,EDGES); assert (u[1],v[1])==(v[0]^v[2],u[0])
print('hidden (u1,v1) = (V0+V2, U0) on all 256 admissible states')
# Lagrangian count on 4 visible pairs: prod_{i=1..4}(2^i+1)
L=1
for i in range(1,5): L*=2**i+1
print('number of Lagrangian subspaces of F2^8 (formula):',L)
# independent rank-based check of the support over all Lagrangian readouts
def lin(t):  # matrix rows: final coordinate i as a mask over initial coordinates
    cols=[]
    for j in range(2*N):
        bits=[0]*(2*N); bits[j]=1
        u,v=run((tuple(bits[:N]),tuple(bits[N:])),t,EDGES); cols.append(list(u)+list(v))
    return [sum(cols[j][i]<<j for j in range(2*N)) for i in range(2*N)]
def rank(rows):
    piv={}
    for r in rows:
        while r:
            h=r.bit_length()-1
            if h in piv: r^=piv[h]
            else: piv[h]=r; break
    return len(piv)
M=lin(3)
coords=[x for x in VIS]+[N+x for x in VIS]   # visible functional basis: u0,u2,u3,u4,v0,v2,v3,v4
A=[1<<3,1<<4]                                # known: u3 = u4 = 0
T=[M[1],M[N+1]]
def omega(x,y):  # x,y: 8-bit masks over (u_vis..., v_vis...)
    return (bin((x&15)&(y>>4)).count('1')+bin((x>>4)&(y&15)).count('1'))%2
vecs=range(1,256)
# enumerate Lagrangians by greedy extension over isotropic bases (dedupe by span)
frontier={frozenset([0])}
for d in range(4):
    nxt=set()
    for S in frontier:
        for v in vecs:
            if v not in S and all(omega(v,w)==0 for w in S): nxt.add(frozenset(S|{x^v for x in S}))
    frontier=nxt
assert len(frontier)==L
hist=defaultdict(int)
for S in frontier:
    # pull back each functional in S to initial coordinates
    rows=[]
    for v in S:
        r=0
        for k in range(8):
            if (v>>k)&1: r^=M[coords[k]]
        rows.append(r)
    hist[2**(rank(A+rows+T)-rank(A+rows))]+=1
print('Lagrangian readouts by hidden support (rank method):',dict(sorted(hist.items())))
