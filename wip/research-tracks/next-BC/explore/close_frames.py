# exploratory float: for a close pair, which 2-frames {w1, w2} of zhat inside B6 admit an effect E
# with E and I - E block-positive (the most permissive effect set over all domain cones)?
# BP for two qubits = decomposable (Woronowicz/Stormer, recalled): E = P1 + G(Q1), I - E = P2 + G(Q2).
import numpy as np
from scipy.optimize import minimize
rng=np.random.default_rng(11)
def PT(M): return M.reshape(2,2,2,2).transpose(0,3,2,1).reshape(4,4)
def ket(v): v=np.array(v,complex); return v/np.linalg.norm(v)
a=np.array([1,0],complex); b=np.array([1,0],complex)
a2=np.array([4/5,3/5],complex); b2=np.array([12/13,5j/13])
ab,a2b2,ab2,a2b=np.kron(a,b),np.kron(a2,b2),np.kron(a,b2),np.kron(a2,b)
def W(al,be,ga,de):
    return al*np.outer(ab,ab.conj())+be*np.outer(a2b2,a2b2.conj())+ga*np.outer(ab,a2b2.conj())+np.conj(ga)*np.outer(a2b2,ab.conj())+de*np.outer(ab2,a2b.conj())+np.conj(de)*np.outer(a2b,ab2.conj())
z=W(1,1,0,0); zh=z/np.trace(z).real
def L(v):
    M=(v[:16]+1j*v[16:]).reshape(4,4); return M@M.conj().T
def unpack(x):
    P1,Q1,P2,Q2=L(x[0:32]),L(x[32:64]),L(x[64:96]),L(x[96:128])
    al,be,g1,g2,e1,e2=x[128:134]; p=1/(1+np.exp(-x[134]))
    return P1,Q1,P2,Q2,(al,be,g1+1j*g2,e1+1j*e2),p
def pen(x):
    P1,Q1,P2,Q2,c,p=unpack(x)
    E=P1+PT(Q1); R=P2+PT(Q2)
    s=np.linalg.norm(E+R-np.eye(4))**2
    w1=W(*c); t1=np.trace(w1).real
    w2=(zh-p*w1/t1)/(1-p)
    # w1/t1 and w2 normalized states in B6: inequality on coordinates of w2 = W(...)
    c2=((1/2-p*c[0]/t1)/(1-p),(1/2-p*c[1]/t1)/(1-p),(-p*c[2]/t1)/(1-p),(-p*c[3]/t1)/(1-p))
    def b6(cc):
        al,be,ga,de=cc; return max(0,abs(ga)+abs(de)-np.sqrt(max(al,0)*max(be,0)))**2+min(al,0)**2+min(be,0)**2
    s+=b6(c)+b6(c2)
    s+=(np.trace(E@w1).real/t1-1)**2+(np.trace(E@w2).real)**2
    s+= (t1<=0)*1.0
    return s
sols=[]
for trial in range(60):
    x0=rng.normal(size=135)*0.3
    x0[128:130]=rng.uniform(0.2,1.5,2)
    r=minimize(pen,x0,method='L-BFGS-B',options={'maxiter':20000})
    if r.fun<1e-9:
        P1,Q1,P2,Q2,c,p=unpack(r.x); t1=np.trace(W(*c)).real
        sols.append((abs(c[2])/t1,abs(c[3])/t1,p))
print("solutions found:",len(sols))
for s in sols[:40]:
    print("  |ga1|=%.4f |de1|=%.4f p=%.3f"%s)
