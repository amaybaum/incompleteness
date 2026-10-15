# F2-4 design probe (floating point, design evidence only). See ../RULES.md.
# F2-4 design probe (floating point): one-duration D1 under R_cf, coupling-independent graph and
# guaranteed-link certificate; feasibility timing.
import numpy as np, itertools as it, time, sys
TOL=1e-9
def symrep(e,q):
    e%=q; return e if 2*e<=q else e-q
def weyl1(q):
    w=np.exp(2j*np.pi/q); X=np.roll(np.eye(q),1,axis=0); Z=np.diag(w**np.arange(q)); return X,Z
def W1(q,x,z):
    X,Z=weyl1(q); return np.linalg.matrix_power(X,x%q)@np.linalg.matrix_power(Z,z%q)
def ufree(q):   # a unitary with Ad_u X = Z^{+-1}: the DFT
    w=np.exp(2j*np.pi/q); return np.array([[w**(j*k) for k in range(q)] for j in range(q)])/np.sqrt(q)
def free_halves(q):
    u=ufree(q); ev,V=np.linalg.eig(u)
    # group eigenvalues
    keys=[]; 
    for e in ev:
        if not any(abs(e-k)<1e-7 for k in keys): keys.append(e)
    P=[sum(np.outer(V[:,i],V[:,i].conj()) for i in range(q) if abs(ev[i]-k)<1e-7) for k in keys]
    # orthonormalize projectors (eig of unitary normal: fine if V unitary); use spectral via Schur
    from scipy.linalg import schur
    T,Q=schur(u,output='complex'); d=np.diag(T)
    P=[Q[:,[i for i in range(q) if abs(d[i]-k)<1e-7]] for k in keys]; P=[p@p.conj().T for p in P]
    th=[np.angle(k)/(2*np.pi) for k in keys]
    hs=[]
    for pat in it.product((0,1),repeat=len(keys)-1):
        n=(0,)+pat; hs.append(sum(np.exp(1j*np.pi*(th[i]+n[i]))*P[i] for i in range(len(keys))))
    return hs
def rel1(q,h):  # single-site relation: v -> set of w with nonzero W(w) component in h W(v) h^dag, both h and h^dag
    R={}
    for v in it.product(range(q),repeat=2):
        A=W1(q,*v); s=set()
        for hh in (h,h.conj().T):
            B=hh@A@hh.conj().T
            for w in it.product(range(q),repeat=2):
                c=np.trace(W1(q,*w).conj().T@B)/q
                if abs(c)>TOL: s.add(w)
        R[v]=s
    return R
def symp_gens_cf(q,N):
    J=np.zeros((2*N,2*N),int)
    for i in range(N): J[i,N+i]=1; J[N+i,i]=-1   # (x,z)->(z,-x) sitewise
    gens=[J%q]
    for i,j in it.combinations(range(N),2):
        for m in range(1,q):
            T=np.eye(2*N,dtype=int); T[N+i,j]=-m; T[N+j,i]=-m   # z -> z - M x
            gens.append((J@T)%q)
    return gens
def orbits(gens,q,N):
    pts=[p for p in it.product(range(q),repeat=2*N) if any(p)]; where={}; orbs=[]
    for p in pts:
        if p in where: continue
        k=len(orbs); where[p]=k; fr=[p]; orb=[p]
        while fr:
            nw=[]
            for v in fr:
                for g in gens:
                    w=tuple((g@np.array(v))%q)
                    if w not in where: where[w]=k; orb.append(w); nw.append(w)
            fr=nw
        orbs.append(orb)
    return orbs,where
class UF:
    def __init__(s,n): s.p=list(range(n))
    def f(s,a):
        while s.p[a]!=a: s.p[a]=s.p[s.p[a]]; a=s.p[a]
        return a
    def u(s,a,b):
        a,b=s.f(a),s.f(b)
        if a!=b: s.p[a]=b
    def n(s): return len({s.f(i) for i in range(len(s.p))})
def free_links(q,N,R1,where,uf):
    # (v_1..v_N) ~ (w_1..w_N), w_i in R1(v_i) (v_i=0 -> 0)
    for v in where:
        vs=[(v[i],v[N+i]) for i in range(N)]
        choices=[[(0,0)] if s==(0,0) else sorted(R1[s]-{(0,0)}) for s in vs]
        for c in it.product(*choices):
            w=tuple([a for a,b in c]+[b for a,b in c])
            if any(w): uf.u(where[v],where[w])
def diag_links(q,N,g_fn,pair,where,uf):
    # diagonal gate on pair (i,j): Ad_g W(x,z) has components (x, z+k), k in supp FT_y [g(y+x)/g(y)]
    pts=list(it.product(range(q),repeat=N))
    for x in it.product(range(q),repeat=N):
        f=np.array([g_fn(tuple((y[a]+x[a])%q for a in range(N)))/g_fn(y) for y in pts])
        F=np.fft.fftn(f.reshape([q]*N))/q**N
        ks=[k for k in it.product(range(q),repeat=N) if abs(F[k])>TOL]
        for z in it.product(range(q),repeat=N):
            v=tuple(x)+tuple(z)
            if not any(v): continue
            for k in ks:
                w=tuple(x)+tuple((z[a]-k[a])%q for a in range(N))   # sign of k irrelevant for support (k and -k both? use both)
                w2=tuple(x)+tuple((z[a]+k[a])%q for a in range(N))
                for ww in (w,w2):
                    if any(ww): uf.u(where[v],where[ww])
def run(q,N,npat=None,seed=0):
    t0=time.time()
    gens=symp_gens_cf(q,N); orbs,where=orbits(gens,q,N)
    # map lines to orbit index first: union-find over lines, pre-merged by orbits
    lines=list(where.keys()); idx={v:i for i,v in enumerate(lines)}
    hs=free_halves(q)
    out=[]
    for fi,h in enumerate(hs):
        R1=rel1(q,h)
        uf=UF(len(lines)); 
        for o in orbs:
            for v in o[1:]: uf.u(idx[o[0]],idx[v])
        free_links(q,N,R1,idx,uf)
        ncomp=uf.n()
        # components structure
        comps={}
        for v in lines: comps.setdefault(uf.f(idx[v]),[]).append(v)
        sizes=sorted(len(c) for c in comps.values())
        out.append((fi,ncomp,sizes))
    print(f"(q,N)=({q},{N}) orbits {sorted(len(o) for o in orbs)}; H+free-half components per free pattern: {[(f,n,s) for f,n,s in out]}  [{time.time()-t0:.1f}s]")
    return orbs,where,hs
for q,N in [(3,2),(3,3),(5,2)]:
    run(q,N)
