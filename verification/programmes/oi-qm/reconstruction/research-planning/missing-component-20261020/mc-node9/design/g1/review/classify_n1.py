# independent n=1 classification of central extensions of V=F2^2 by Z_m with commutator (m/2)*omega
from itertools import product
V=[0,1,2,3]  # bit0=x, bit1=z
def om(u,v): return ((u&1)*((v>>1)&1)+((u>>1)&1)*(v&1))%2
for m in (2,4):
    nz=[(u,v) for u in (1,2,3) for v in (1,2,3)]
    cocs=[]
    for vals in product(range(m),repeat=9):
        b={(u,v):0 for u in V for v in V}
        for (u,v),x in zip(nz,vals): b[(u,v)]=x
        if any((b[(u,v)]-b[(v,u)]-(m//2)*om(u,v))%m for u in V for v in V): continue
        if all((b[(u,v)]+b[(u^v,w)]-b[(v,w)]-b[(u,v^w)])%m==0 for u in V for v in V for w in V): cocs.append(b)
    # classes mod coboundaries df(u,v)=f(u)+f(v)-f(u^v)
    cob=set()
    for f in product(range(m),repeat=3):
        F={0:0,1:f[0],2:f[1],3:f[2]}
        cob.add(tuple((F[u]+F[v]-F[u^v])%m for u in V for v in V))
    key=lambda b: tuple(b[(u,v)] for u in V for v in V)
    classes=[]; seen=set()
    for b in cocs:
        k=key(b)
        if k in seen: continue
        cl={tuple((x+y)%m for x,y in zip(k,c)) for c in cob}; seen|=cl; classes.append(b)
    def orders(b):
        # element (a,u); mult (a,u)(c,v)=(a+c+b(u,v),u^v)
        els=[(a,u) for a in range(m) for u in V]; cnt={}
        for g in els:
            h=g;k=1
            while h!=(0,0): h=((h[0]+g[0]+b[(h[1],g[1])])%m,h[1]^g[1]); k+=1
            cnt[k]=cnt.get(k,0)+1
        return tuple(sorted(cnt.items()))
    from collections import Counter
    print('m=%d: cocycles with commutator %s*omega: %d; coboundaries: %d; classes: %d; order statistics of classes:'%(m,m//2,len(cocs),len(cob),len(classes)),Counter(orders(b) for b in classes))
