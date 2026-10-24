# Independent check of HB-3alpha (option 2 mixture; option 1 = w=1) and A-8 reference values, via networkx network_simplex
import networkx as nx, itertools, math
from fractions import Fraction as Fr
from collections import deque
def torus(L, glue):
    G={}
    for v in itertools.product(range(L),repeat=3):
        G[v]=[tuple((v[i]+(s if i==d else 0))%L for i in range(3)) for d in range(3) for s in (1,-1)]
    A=(0,0,0); B=(L//2,)*3
    if glue: G[A]=G[A]+[B]; G[B]=G[B]+[A]
    return G,A,B
def bfs(G,s):
    d={s:0}; q=deque([s])
    while q:
        v=q.popleft()
        for u in G[v]:
            if u not in d: d[u]=d[v]+1; q.append(u)
    return d
def ballm(G,x,r):
    d=bfs(G,x); b=[v for v in d if d[v]<=r]; return {v:Fr(1,len(b)) for v in b}
def mix(m0,m1,w):
    m={}
    for v,p in m0.items(): m[v]=m.get(v,0)+(1-w)*p
    for v,p in m1.items(): m[v]=m.get(v,0)+w*p
    return m
def W1(mu,nu,G):
    keys=set(mu)|set(nu); diff={x:mu.get(x,0)-nu.get(x,0) for x in keys}
    den=1
    for x in keys: den=den*diff[x].denominator//math.gcd(den,diff[x].denominator)
    H=nx.DiGraph()
    src=[x for x in keys if diff[x]>0]; snk=[x for x in keys if diff[x]<0]
    for x in src: H.add_node(('s',x),demand=-int(diff[x]*den))
    for y in snk: H.add_node(('t',y),demand=int(-diff[y]*den))
    for x in src:
        d=bfs(G,x)
        for y in snk: H.add_edge(('s',x),('t',y),weight=d[y])
    cost,_=nx.network_simplex(H)
    return Fr(cost,den)
def s_r(r): return 1 if r==0 else 4*r*r+2
def Vb(dl): return sum(s_r(r) for r in range(dl+1))
def closed(w,dl):
    Z=Vb(dl)+Vb(dl-1); sh=s_r(dl); Er=Fr(sum(r*s_r(r) for r in range(dl+1)),Vb(dl))
    return (1-w)*(1+2*Er)+w*Fr(sh*(1+2*dl),Z)
for L,dls in ((6,(1,2)),(8,(1,2)),(10,(1,2)),(12,(1,2)),(14,(3,))):
    Gr,A,B=torus(L,False); Gg,_,_=torus(L,True)
    for dl in dls:
        e1=(1,0,0)
        wr=W1(ballm(Gr,A,dl),ballm(Gr,e1,dl),Gr)
        print(f'L={L} d={dl} ref kappa(A,A+e1)={1-wr}')
        for w in (Fr(1,100),Fr(1,4),Fr(1,2),Fr(1)):
            mA=mix(ballm(Gr,A,dl),ballm(Gg,A,dl),w); mB=mix(ballm(Gr,B,dl),ballm(Gg,B,dl),w)
            x=W1(mA,mB,Gg)
            ok = (x==closed(w,dl)) if 3*L>=2*(4*dl+1) else 'n/a'
            print(f'   w={w}: W1={x} closed={closed(w,dl)} match={ok} kappa={float(1-x):.4f}')
# monotonicity in w and delta-limit
for dl in (1,2,5,20,100):
    print('delta',dl,'kappa(w=1)=',float(1-closed(Fr(1),dl)),'kappa(w=1/2)=',float(1-closed(Fr(1,2),dl)),'kappa(w=0+)=',float(1-closed(Fr(0),dl)))
