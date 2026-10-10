"""First-order boundary condition on continuous symmetries of any cone min <= C <= max (exact, sympy over Q).
If exp(sX) preserves C for all s, then for every pure product p = p_v (x) p_w and effect f_v = (1,-v) vanishing on p_v:
(f_v (x) g)(exp(sX) p) >= 0 with equality at s = 0, for every g in L_n, hence (f_v (x) I) X p = 0; symmetrically
(I (x) f_w) X p = 0; and normalization (u (x) u)^T X = 0. Sampled rational points give a superset of the true solution
space, so an upper bound on its dimension is exact."""
import itertools, sympy as sp
def pyth(k):
    pts=[]
    for m in range(1,k+1):
        for q in range(0,m):
            den=m*m+q*q; pts.append((sp.Rational(m*m-q*q,den),sp.Rational(2*m*q,den)))
    return pts
def run(n):
    d=n*n; Xs=sp.symbols('x0:%d'%(d*d)); X=sp.Matrix(d,d,Xs)
    if n==3:
        base=pyth(4); vs=[]
        for c,s in base: vs+= [(c,s),(-c,s),(c,-s),(-s,c)]
        vs=[sp.Matrix([a,b]) for a,b in vs]
    else:
        vs=[]
        for (c1,s1),(c2,s2) in itertools.product(pyth(3),repeat=2):
            vs.append(sp.Matrix([c1*c2,c1*s2,s1])); vs.append(sp.Matrix([-s1,c1*s2,c1*c2]))
        vs+= [sp.Matrix(r) for r in ([1,0,0],[0,1,0],[0,0,1],[-1,0,0],[0,-1,0],[0,0,-1])]
    vs=vs[:20]
    I=sp.eye(n); eqs=[]
    u=sp.zeros(n,1); u[0]=1; uu=sp.kronecker_product(u,u)
    eqs+=list(uu.T*X)
    for v in vs:
        pv=sp.Matrix([1]+list(v)); fv=sp.Matrix([1]+list(-v))
        for w in vs:
            pw=sp.Matrix([1]+list(w)); fw=sp.Matrix([1]+list(-w))
            Xp=X*sp.kronecker_product(pv,pw)
            eqs+=list(sp.kronecker_product(fv.T,I)*Xp)+list(sp.kronecker_product(I,fw.T)*Xp)
    A=sp.Matrix([[sp.diff(e,x) for x in Xs] for e in eqs])
    ns=A.nullspace()
    return ns
if __name__=="__main__":
 for n in (3,4):
    ns=run(n); print('n=%d: dimension of first-order solution space (upper bound, exact over Q): %d'%(n,len(ns)),flush=True)
