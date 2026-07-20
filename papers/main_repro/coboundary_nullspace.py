#!/usr/bin/env python3
"""Main §3.x reconstruction lemma (ancilla-marginal form) — numerical completeness check.
Claim verified: the linearized idempotency constraint
    Σ_b (θ_ab + θ_bc) M_i[a,b] M_i[b,c] = θ_ac M_i[a,c]   (all i,a,c; θ real antisymmetric)
has null space of dimension EXACTLY D-1 (the diagonal coboundary θ_ab = α_a - α_b) for
generic Ĥ, across (n, m_a) = (3,4), (2,3), (4,2), (3,3), (2,4).  D = n·m_a.
"""
import numpy as np
rng=np.random.default_rng(7)
def check(n,ma,trials=3):
    D=n*ma; npar=D*(D-1)//2
    idx={}; k=0
    for a in range(D):
        for b in range(a+1,D): idx[(a,b)]=k; k+=1
    def th(v,a,b):
        if a==b: return 0.0
        return v[idx[(a,b)]] if a<b else -v[idx[(b,a)]]
    dims=[]
    for t in range(trials):
        A=rng.normal(size=(D,D))+1j*rng.normal(size=(D,D)); H=(A+A.conj().T)/2
        _,V=np.linalg.eigh(H)                       # columns = eigenvectors |a>
        M=[]                                        # M_i[a,b] = <a|P_i|b>
        for i in range(n):
            sel=np.zeros(D); sel[i*ma:(i+1)*ma]=1
            M.append(V.conj().T@np.diag(sel)@V)
        rows=[]
        for i in range(n):
            Mi=M[i]
            for a in range(D):
                for c in range(D):
                    row=np.zeros(npar,dtype=complex)
                    for b in range(D):
                        w=Mi[a,b]*Mi[b,c]
                        for (p,qq),sgn in (((a,b),1),((b,c),1)):
                            if p!=qq:
                                j=idx[(p,qq)] if p<qq else idx[(qq,p)]
                                row[j]+= w*(1 if p<qq else -1)*sgn
                    if a!=c:
                        j=idx[(a,c)] if a<c else idx[(c,a)]
                        row[j]-= Mi[a,c]*(1 if a<c else -1)
                    rows.append(row)
        Areal=np.vstack([np.vstack(rows).real,np.vstack(rows).imag])
        sv=np.linalg.svd(Areal,compute_uv=False)
        tol=max(Areal.shape)*np.finfo(float).eps*sv[0]*100
        dims.append(npar-int((sv>tol).sum()))
    return dims
allok=True
for n,ma in [(3,4),(2,3),(4,2),(3,3),(2,4)]:
    D=n*ma; dims=check(n,ma)
    ok=all(d==D-1 for d in dims); allok&=ok
    print(f"(n,m_a)=({n},{ma}) D={D:2d}: null-space dims over trials {dims}  expected {D-1} -> {'PASS' if ok else 'FAIL'}")
print("ALL PASS: coboundary exhausts the null space (dim = D-1, generic Ĥ)" if allok else "FAILURE")
