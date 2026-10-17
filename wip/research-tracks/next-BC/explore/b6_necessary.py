# exploratory float: necessary condition for a {psi, Gamma phi} frame in BP:
#   |<psi|cd>|^2 + |<phi|c conj(d)>|^2 <= 1 for all unit c, d.
import numpy as np
from scipy.optimize import minimize
rng=np.random.default_rng(5)
def ket(v): v=np.array(v,complex); return v/np.linalg.norm(v)
def setup(th,ph):
    a=ket([1,0]); b=ket([1,0]); a2=ket([np.cos(th),np.sin(th)]); b2=ket([np.cos(ph),1j*np.sin(ph)])
    return a,b,a2,b2
def decomps(al,be,ga,de):
    roots=np.roots([-be, al*be+abs(ga)**2-abs(de)**2, -al*abs(ga)**2]); out=[]
    for A1 in roots:
        if abs(A1.imag)>1e-12: continue
        A1=A1.real; B1=abs(ga)**2/A1; A2=al-A1; B2=be-B1
        if A1<=0 or A2<=0 or B1<=0 or B2<=0: continue
        out.append((A1,B1,A2,B2))
    return out
def maxviol(psi,phi):
    def f(v):
        c=ket(v[0:2]+1j*v[2:4]); d=ket(v[4:6]+1j*v[6:8])
        return -(abs(np.vdot(psi,np.kron(c,d)))**2+abs(np.vdot(phi,np.kron(c,d.conj())))**2)
    best=0
    for s in range(60):
        r=minimize(f,rng.normal(size=8),method='BFGS'); best=max(best,-r.fun)
    return best
for (th,ph) in [(0.6,0.9),(0.3,0.4),(1.0,1.2)]:
    a,b,a2,b2=setup(th,ph)
    ab,a2b2=np.kron(a,b),np.kron(a2,b2); abc,a2b2c=np.kron(a,b.conj()),np.kron(a2,b2.conj())
    for (al,be,ga,de) in [(1,1,0.3,0.3),(1,1,0.45,0.05),(1,1,0.05,0.45),(1,1,0.2,0.2j),(1,0.5,0.2,0.3)]:
        res=[]
        for (A1,B1,A2,B2) in decomps(al,be,ga,de):
            psi=ket(np.sqrt(A1)*ab+(np.conj(ga)/np.sqrt(A1))*a2b2)
            # Gamma(|u><u|) with u = sqrt(A2) a b* + f a' b'*, Gamma(sqrt(A2) conj(f) |ab*><a'b'*|) = de |ab'><a'b|
            f=np.conj(de)/np.sqrt(A2)
            phi=ket(np.sqrt(A2)*abc+f*a2b2c)
            res.append(maxviol(psi,phi))
        print(f"th={th} ph={ph} w={(al,be,ga,de)} max |<psi|cd>|^2+|<phi|cd*>|^2 per decomposition:",["%.4f"%r for r in res],flush=True)
