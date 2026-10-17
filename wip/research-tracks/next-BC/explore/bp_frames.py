# exploratory float search for frame decompositions in maxCone = BP (effects: E, I - sum E separable = PPT)
import numpy as np, itertools, sys
from scipy.optimize import minimize
rng = np.random.default_rng(int(sys.argv[1]) if len(sys.argv)>1 else 0)
def PT(M):
    T=M.reshape(2,2,2,2).transpose(0,3,2,1).reshape(4,4); return T
def neg(M):
    w=np.linalg.eigvalsh((M+M.conj().T)/2); return np.sum(np.minimum(w,0)**2)
def herm(v):
    M=np.zeros((4,4),complex); k=0
    for i in range(4):
        M[i,i]=v[k]; k+=1
    for i in range(4):
        for j in range(i+1,4):
            M[i,j]=v[k]+1j*v[k+1]; M[j,i]=v[k]-1j*v[k+1]; k+=2
    return M
def member(v,t):
    u=v[:4]+1j*v[4:]; u=u/np.linalg.norm(u); P=np.outer(u,u.conj())
    return P if t=='P' else PT(P)
def penalty(x,rho,types,sep=True):
    k=len(types); off=0
    oms=[]
    for t in types:
        oms.append(member(x[off:off+8],t)); off+=8
    w=np.exp(x[off:off+k]); w=w/w.sum(); off+=k
    Es=[]
    for _ in range(k):
        Es.append(herm(x[off:off+16])); off+=16
    pen=np.linalg.norm(rho-sum(wi*o for wi,o in zip(w,oms)))**2
    for j in range(k):
        for l in range(k):
            pen+=(np.real(np.trace(Es[j]@oms[l]))-(1 if j==l else 0))**2
    rest=np.eye(4)-sum(Es)
    for E in Es+[rest]:
        pen+=neg(E)+ (neg(PT(E)) if sep else 0)
    return pen
def search(rho,types,sep=True,starts=40):
    best=np.inf
    k=len(types); n=8*k+k+16*k
    for s in range(starts):
        x0=rng.normal(size=n)
        r=minimize(penalty,x0,args=(rho,types,sep),method='BFGS',options={'maxiter':4000,'gtol':1e-12})
        best=min(best,r.fun)
        if best<1e-12: break
    return best
def ket(v): v=np.array(v,complex); return v/np.linalg.norm(v)
th=np.pi/5
x=np.outer(ket([1,0,0,0]),ket([1,0,0,0]))
t=ket([np.cos(th),np.sin(th)]); y=np.outer(np.kron(t,t),np.kron(t,t).conj())
zhat=(x+y)/np.trace(x+y).real
# a B6 state with gamma, delta != 0: mix of a Q3-face pure state and a Gamma-face pure state
a,b,a2,b2=ket([1,0]),ket([1,0]),t,t
psi=ket(np.kron(a,b)+0.7*np.kron(a2,b2)); phi=ket(np.kron(a,b.conj())+0.6j*np.kron(a2,b2.conj()))
w6=0.5*np.outer(psi,psi.conj())+0.5*PT(np.outer(phi,phi.conj()))
bell=[ket([1,0,0,1]),ket([1,0,0,-1]),ket([0,1,1,0]),ket([0,1,-1,0])]
lam=[0.55,0.25,0.15,0.05]
rbd=sum(l*np.outer(v,v.conj()) for l,v in zip(lam,bell))
tests={'zhat':zhat,'w6':w6,'bell-diag':rbd}
for name,rho in tests.items():
    for types in [('P','P'),('P','G'),('G','G'),('P','P','G'),('P','G','G'),('P','P','P')]:
        b_sep=search(rho,types,True,starts=12)
        print(f"{name:10s} types={''.join(types):4s} BP-best={b_sep:.2e}", flush=True)
    print(f"{name:10s} control: quantum effects (PSD, no PPT), types PP..: ", f"{search(rho,('P',)*4,False,starts=6):.2e}" if name=='bell-diag' else f"{search(rho,('P','P'),False,starts=6):.2e}", flush=True)
