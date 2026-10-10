"""Exploration only: explicit column phases c for GramPhaseEquiv (g G) G' in the pair-agreement
lemmas (G' j k = conj(c j) (gG) j k c k), as monomials +-w^e read off numerically at two generic
parameters and then checked exactly on the symbol level elsewhere."""
import numpy as np, cmath
ID=(0,1,2,3); D=(1,0,3,2); X=(3,2,1,0); S23=(0,1,3,2); S12=(0,2,1,3)
def M(z): return np.array([[1,1,1,1],[1,z,-1,-z],[1,-1,1,-1],[1,-z,-1,z]],dtype=complex)/2
def F(z):
    U=M(z); return np.array([[[np.conj(U[i,j])*U[i,k] for k in range(4)] for j in range(4)] for i in range(4)])
def rel(G,pi,tau): return np.array([[[G[pi[i],tau[j],tau[k]] for k in range(4)] for j in range(4)] for i in range(4)])
def phase(G,Gp):
    # c j = c 0 * ...: G' i 0 k = conj(c0) G i 0 k c k -> c k/c0 = G'[i,0,k]/G[i,0,k]
    c=np.array([Gp[0,0,k]/G[0,0,k] for k in range(4)])
    ok=np.allclose(np.einsum('j,ijk,k->ijk',np.conj(c),G,c),Gp)
    return c,ok
def mono(vals,z):
    out=[]
    for v in vals:
        for s in (1,-1):
            for e,name in ((0,'1'),(1,'w'),(-1,'star w')):
                if abs(v - s*z**e)<1e-9: out.append(('-' if s<0 else '')+name)
    return out
cases=[("gA C0", (ID,X), None, 'conj'),("gC C0",(X,ID),None,'conj'),("gB C0",(ID,D),None,'conj'),("gD C0",(D,ID),None,'conj')]
fix={1:("gA",(ID,X)),2:("gB",(ID,D)),3:("gC",(X,ID)),4:("gA",(ID,X)),5:("gB",(ID,D)),6:("gD",(D,ID)),7:("gA",(ID,X)),8:("gB",(ID,D))}
R=[(a,b) for a in (ID,S23,S12) for b in (ID,S23,S12)]
z=cmath.exp(0.37j)
for name,g,_,_ in cases:
    c,ok=phase(rel(F(z),*g),F(np.conj(z)))
    print(name,"-> F(star z):",ok,mono(c,z))
for r,(name,g) in fix.items():
    a,b=R[r]
    G=rel(F(z),a,b)
    c,ok=phase(rel(G,*g),G)
    print("circle",r,R[r],name,"fixes:",ok,mono(c,z))
