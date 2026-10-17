import numpy as np
from scipy.optimize import minimize
from fractions import Fraction as Fr
rng=np.random.default_rng(7)
def ket(v): v=np.array(v,complex); return v/np.linalg.norm(v)
a=np.array([1,0],complex); b=np.array([1,0],complex)
a2=np.array([3/5,4/5],complex); b2=np.array([5/13,12j/13])
ab,a2b2=np.kron(a,b),np.kron(a2,b2); abc,a2b2c=np.kron(a,b.conj()),np.kron(a2,b2.conj())
ga=(1+1j)/3; de=(1-1j)/3
for A1 in [1/3,2/3]:
    B1=abs(ga)**2/A1; A2=1-A1; B2=1-B1
    psi=A1*ab+np.conj(ga)*a2b2          # ray of the rank-one Q3-face part
    u=A2*abc+np.conj(de)*a2b2c          # Gamma(|u><u|) is the Gamma-face part
    psi_n=psi/np.linalg.norm(psi); u_n=u/np.linalg.norm(u)
    def f(v):
        c=ket(v[0:2]+1j*v[2:4]); d=ket(v[4:6]+1j*v[6:8])
        return -(abs(np.vdot(psi_n,np.kron(c,d)))**2+abs(np.vdot(u_n,np.kron(c,d.conj())))**2)
    best=None
    for s in range(80):
        r=minimize(f,rng.normal(size=8),method='BFGS')
        if best is None or r.fun<best.fun: best=r
    v=best.x; c=ket(v[0:2]+1j*v[2:4]); d=ket(v[4:6]+1j*v[6:8])
    # normalize phase so that first nonzero comp is real
    c=c*np.exp(-1j*np.angle(c[0])); d=d*np.exp(-1j*np.angle(d[0]))
    print("A1",A1,"max",-best.fun,"c",np.round(c,4),"d",np.round(d,4))
    # also test simple candidates
    for cc,dd,name in [(a,b,'ab'),(a2,b2,"a'b'"),(a,b2,"ab'"),(a2,b,"a'b")]:
        val=abs(np.vdot(psi_n,np.kron(cc,dd)))**2+abs(np.vdot(u_n,np.kron(cc,dd.conj())))**2
        print("   at",name,val)
