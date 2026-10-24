import itertools
from collections import deque
def torus(L, glue):
    G={}
    for v in itertools.product(range(L),repeat=3):
        G[v]=[tuple((v[i]+(s if i==d else 0))%L for i in range(3)) for d in range(3) for s in (1,-1)]
    A=(0,0,0); B=(L//2,)*3
    if glue: G[A]=G[A]+[B]; G[B]=G[B]+[A]
    return G
def ecc(G,s):
    d={s:0}; q=deque([s])
    while q:
        v=q.popleft()
        for u in G[v]:
            if u not in d: d[u]=d[v]+1; q.append(u)
    return max(d.values())
for L in (4,6,8,10,12):
    X=torus(L,False); Y=torus(L,True)
    rX=ecc(X,(0,0,0)); rY=min(ecc(Y,v) for v in Y)
    print(L, rX, rY, 'lb', (rX-rY)/(2*L), 3/8-1/(4*L), 'ecc_Y(A)=',ecc(Y,(0,0,0)))
