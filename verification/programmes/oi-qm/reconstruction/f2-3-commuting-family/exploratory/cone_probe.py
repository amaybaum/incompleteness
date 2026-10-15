# Probe (floating point, scratch only): on E1-L's generator family, does a strict one-edge cone of the
# coupling-layer flow at intermediate flow times coincide with F2-3's commuting condition?
import numpy as np, itertools as it
from scipy.linalg import expm
rng=np.random.default_rng(7)
def symrep(e,q):
    e%=q; return e if 2*e<=q else e-q
def G0(q,b):   # principal generator of delta_ij(b) = diag(w^{-b yi yj}) on q^2
    return np.diag([symrep(-b*yi*yj,q)/q for yi in range(q) for yj in range(q)]).astype(complex)
def classes(q,b):
    cl={}
    for yi in range(q):
        for yj in range(q): cl.setdefault((-b*yi*yj)%q,[]).append(yi*q+yj)
    return cl
def rand_K(q,b,rank=1):   # integer-spectrum K (projector) inside one eigenspace class of the gate
    cl=[v for v in classes(q,b).values() if len(v)>=2]; idx=cl[rng.integers(len(cl))]
    v=np.zeros((q*q,rank),complex); v[idx,:]=rng.normal(size=(len(idx),rank))+1j*rng.normal(size=(len(idx),rank))
    Qm,_=np.linalg.qr(v); return Qm@Qm.conj().T
def emb(A,sites,q,N=3):  # A on pair (sites) of N-site chain
    # reorder: build full operator via tensor with identity then permute
    rest=[s for s in range(N) if s not in sites]; d=q**N
    full=np.kron(A,np.eye(q**len(rest))); order=list(sites)+rest
    T=full.reshape([q]*(2*N)); perm=[order.index(s) for s in range(N)]
    T=T.transpose(perm+[N+p for p in perm]); return T.reshape(d,d)
def weight_on_3(Os,q):  # norm of the part acting nontrivially on site 3 (index 2)
    T=Os.reshape(q*q,q,q*q,q); tr=np.einsum('aibi->ab',T)/q
    return np.linalg.norm(Os-np.kron(tr,np.eye(q)))
def cone_viol(Gp,Gp2,q,b,b2,svals=(0.1,0.3,0.5,0.7,0.9,1.0)):
    H=emb(Gp,(0,1),q)+emb(Gp2,(1,2),q); out=[]
    basis=[np.kron(np.outer(np.eye(q)[a],np.eye(q)[c]),np.eye(q*q)) for a in range(q) for c in range(q)]
    for s in svals:
        U=expm(2j*np.pi*s*H); out.append(max(weight_on_3(U.conj().T@O@U,q) for O in basis))
    return out
def comm(Gp,Gp2,q): return np.linalg.norm(emb(Gp,(0,1),q)@emb(Gp2,(1,2),q)-emb(Gp2,(1,2),q)@emb(Gp,(0,1),q))
for q in (3,5):
    for (b,b2) in ((1,1),(1,2)):
        print(f"== q={q} chain couplings M12={b}, M23={b2}")
        A,B=G0(q,b),G0(q,b2)
        v=cone_viol(A,B,q,b,b2); print(f"principal: commutator {comm(A,B,q):.2e}  cone violation over s {np.round(v,6)}")
        if q==3:
            phi=np.zeros(9,complex); phi[1*3+1]=phi[2*3+2]=1/np.sqrt(2); Kphi=np.outer(phi,phi.conj())
            C=np.zeros((3,3)); 
            for y in range(3): C[(-y)%3,y]=1
            KC=(np.eye(9)-np.kron(C,C))/2
            for nm,K in (("M_phi",Kphi),("M_C",KC)):
                A2,B2=A+K,B+K   # same G(m) per gate type: K added to every pair generator of value m (here b=b2 or not)
                if b!=b2: B2=G0(q,b2)+K if np.allclose(K@G0(q,b2),G0(q,b2)@K) else G0(q,b2)
                print(f"{nm}: K commutes with G0(b2) {np.allclose(K@G0(q,b2),G0(q,b2)@K)}; commutator {comm(A2,B2,q):.2e}  cone violation {np.round(cone_viol(A2,B2,q,b,b2),6)}")
        nonc=0; cone_ok_noncomm=0; mins=[]
        for trial in range(40):
            K1=rand_K(q,b); K2=rand_K(q,b2) if b2!=b else K1   # one generator per gate type
            A2,B2=A+K1,B+K2
            c=comm(A2,B2,q); v=cone_viol(A2,B2,q,b,b2)
            if c>1e-8:
                nonc+=1; mins.append(max(v[:-1]))
                if max(v[:-1])<1e-8: cone_ok_noncomm+=1
        print(f"random lifted members: {nonc}/40 non-commuting; of those, {cone_ok_noncomm} satisfy the strict cone at s<1; min violation {min(mins) if mins else None:.3e}")
# contrast: generic non-diagonal Hermitian pair terms (outside E1-L's family) that commute
print("== contrast")
q=3; X=np.roll(np.eye(3),1,axis=0); Z=np.diag(np.exp(2j*np.pi*np.arange(3)/3))
A=np.kron(X+X.conj().T,X+X.conj().T); B=A.copy()
print("XX-type pair terms on chain: commutator", f"{comm(A,B,q):.2e}", "cone violation", np.round(cone_viol(A,B,q,1,1),6))
