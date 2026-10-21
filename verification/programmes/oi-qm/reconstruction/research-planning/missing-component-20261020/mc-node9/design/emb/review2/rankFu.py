# rank of the visible functionals restricted to unknown coordinates, mixed n=3 case (star centre 0,
# R={0 FULL, 1 NONE}, toy 2) at t=2; symbolic tracking, independent of the repo.
n=3; adj=[[1,2],[0],[0]]
U=[1<<x for x in range(n)]; V=[1<<(n+x) for x in range(n)]
for t in range(2):
    nU=[]
    for x in range(n):
        a=V[x]
        for z in adj[x]: a^=U[z]
        nU.append(a)
    U,V=nU,U
um=((1<<2*n)-1)&~((1<<0)|(1<<n))  # site 0 clean
F=[U[0]&um,V[0]&um,U[1]&um,V[1]&um]
def rank(vs):
    vs=[v for v in vs if v]; r=0
    while vs:
        p=max(vs); hb=p.bit_length()-1
        vs=[v^p if (v>>hb)&1 else v for v in vs if v!=p]; vs=[v for v in vs if v]; r+=1
    return r
print("rank F_u =",rank(F),"r =",2,"(visible pairs)")
