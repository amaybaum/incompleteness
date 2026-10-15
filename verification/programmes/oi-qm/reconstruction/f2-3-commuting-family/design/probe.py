# Design probe only (floating point): do non-diagonal coupling generators commute within layers?
import numpy as np, itertools
q=3; w=np.exp(2j*np.pi/q); h=(q+1)//2
I=np.eye(q)
def lift(k):  # principal theta for eigenvalue w^{-k}
    t=(-k/q)%1.0
    return t-1 if t>0.5 else t
def Gs(m): return np.diag([lift(h*m*y*y % q) for y in range(q)])
def Gp0(m): return np.diag([lift(m*a*b % q) for a in range(q) for b in range(q)])
def ket(*ys):
    v=np.zeros(q**len(ys)); idx=0
    for y in ys: idx=idx*q+y
    v[idx]=1; return v
def proj(v): v=v/np.linalg.norm(v); return np.outer(v,v.conj())
C=np.zeros((q,q)); 
for y in range(q): C[(-y)%q,y]=1
def expm_h(G): e,V=np.linalg.eigh(G); return V@np.diag(np.exp(2j*np.pi*e))@V.conj().T
def gate_p(m): return np.diag([w**(-(m*a*b)%q) for a in range(q) for b in range(q)])
def comm(A,B): return np.linalg.norm(A@B-B@A)
cands={
 'diag(principal)':lambda m:Gp0(m),
 'P_phi (|11>+|22>)':lambda m:Gp0(m)+proj(ket(1,1)+ket(2,2)),
 'C-projector (1-CC)/2':lambda m:Gp0(m)+(np.eye(q*q)-np.kron(C,C))/2,
}
for name,G in cands.items():
    ok_gen=all(np.allclose(expm_h(G(m)),gate_p(m)*np.exp(2j*np.pi*0)) or np.allclose(expm_h(G(m))/expm_h(G(m))[0,0]*gate_p(m)[0,0],gate_p(m)) for m in range(1,q))
    n2=max(max(comm(np.kron(Gs(a),I),G(b)),comm(np.kron(I,Gs(a)),G(b))) for a in range(1,q) for b in range(1,q))
    n3=max(comm(np.kron(G(a),I),np.kron(I,G(b))) for a in range(1,q) for b in range(1,q))
    print(f"{name:24s} generator ok={ok_gen}  N=2 R_self max|[site,pair]|={n2:.2e}  N=3 chain max|[G12,G23]|={n3:.2e}")
