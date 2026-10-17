# exploratory float: frames {psi, Gamma(phi)} for B6 states with ga, de != 0, in BP (effects PPT)
import numpy as np
from scipy.optimize import minimize
rng=np.random.default_rng(3)
def PT(M): return M.reshape(2,2,2,2).transpose(0,3,2,1).reshape(4,4)
def neg(M):
    w=np.linalg.eigvalsh((M+M.conj().T)/2); return np.sum(np.minimum(w,0)**2)
def herm(v):
    M=np.zeros((4,4),complex); k=0
    for i in range(4): M[i,i]=v[k]; k+=1
    for i in range(4):
        for j in range(i+1,4): M[i,j]=v[k]+1j*v[k+1]; M[j,i]=v[k]-1j*v[k+1]; k+=2
    return M
def ket(v): v=np.array(v,complex); return v/np.linalg.norm(v)
th=0.6; ph=0.9
a=ket([1,0]); b=ket([1,0]); a2=ket([np.cos(th),np.sin(th)]); b2=ket([np.cos(ph),1j*np.sin(ph)])
ab,a2b2,ab2,a2b=np.kron(a,b),np.kron(a2,b2),np.kron(a,b2),np.kron(a2,b)
def w_of(al,be,ga,de):
    return al*np.outer(ab,ab.conj())+be*np.outer(a2b2,a2b2.conj())+ga*np.outer(ab,a2b2.conj())+np.conj(ga)*np.outer(a2b2,ab.conj())+de*np.outer(ab2,a2b.conj())+np.conj(de)*np.outer(a2b,ab2.conj())
def decomps(al,be,ga,de):
    # A1 roots of -be A1^2 + (al be + |ga|^2 - |de|^2) A1 - al |ga|^2 = 0
    roots=np.roots([-be, al*be+abs(ga)**2-abs(de)**2, -al*abs(ga)**2])
    out=[]
    for A1 in roots:
        if abs(A1.imag)>1e-12 or A1.real<=0 or A1.real>=al: continue
        A1=A1.real; B1=abs(ga)**2/A1; A2=al-A1; B2=be-B1
        if B1<=0 or B2<=0: continue
        P=w_of(A1,B1,ga,0); Q=w_of(A2,B2,0,de)   # P rank one psd on span{ab,a'b'}, Q = Gamma(rank one)
        out.append((P,Q))
    return out
def best_E(P,Q,starts=30):
    # E psd-type distinguisher: Tr(E P)=Tr P, Tr(E Q)=0, E, I-E PPT
    tp=np.trace(P).real; tq=np.trace(Q).real
    def pen(v):
        E=herm(v); R=np.eye(4)-E
        return (np.trace(E@P).real/tp-1)**2+(np.trace(E@Q).real/tq)**2+neg(E)+neg(PT(E))+neg(R)+neg(PT(R))
    best=np.inf
    for s in range(starts):
        r=minimize(pen,rng.normal(size=16)*0.5,method='BFGS',options={'gtol':1e-14,'maxiter':5000})
        best=min(best,r.fun)
    return best
for (al,be,ga,de) in [(1,1,0.3,0.3),(1,1,0.45,0.05j),(1,0.7,0.2+0.1j,-0.25),(1,1,0.05,0.05),(1,1,0.49,0.49)]:
    w=w_of(al,be,ga,de)
    ds=decomps(al,be,ga,de)
    res=[best_E(P,Q) for P,Q in ds]
    # control: Q3 effects only psd (no PPT) for same decomposition
    print((al,be,ga,de),"n decomps",len(ds),"BP-best",["%.2e"%r for r in res], flush=True)
