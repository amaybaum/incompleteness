# Swap phi(x,h)=(h,x) on qubit (x) + qubit (h); compare hidden prior uniform vs initialized |0>.
import numpy as np, itertools
SW=np.zeros((4,4))
for x,h in itertools.product((0,1),repeat=2): SW[2*h+x,2*x+h]=1   # |x,h> -> |h,x>
def ch(rho,tau,t):
    U=np.linalg.matrix_power(SW,t); R=U@np.kron(rho,tau)@U.T
    return R.reshape(2,2,2,2).trace(axis1=1,axis2=3)
plus=np.array([[.5,.5],[.5,.5]]); uni=np.eye(2)/2; zero=np.diag([1.,0])
for name,tau in (("uniform",uni),("initialized |0>",zero)):
    print(name,"Phi1(|+><+|)=",ch(plus,tau,1).round(3).tolist(),"Phi2(|+><+|)=",ch(plus,tau,2).round(3).tolist())
# classical-memory decomposition for the uniform case: I_o = 1/4 s_o . s_o (Pauli twirl), Psi_o = s_o . s_o
P=[np.eye(2),np.array([[0,1],[1,0]]),np.array([[0,-1j],[1j,0]]),np.diag([1,-1])]
rng=np.random.default_rng(0); A=rng.normal(size=(2,2))+1j*rng.normal(size=(2,2)); rho=A@A.conj().T; rho/=np.trace(rho)
step1=sum(0.25*s@rho@s.conj().T for s in P); step2=sum(s@(0.25*s@rho@s.conj().T)@s.conj().T for s in P)
print("sum_o I_o(rho) == I/2:",np.allclose(step1,np.eye(2)/2),"; sum_o Psi_o(I_o(rho)) == rho:",np.allclose(step2,rho))
# check Phi1 for uniform equals I/2 on random rho, Phi2 equals identity
print("uniform Phi1(rho)==I/2:",np.allclose(ch(rho,uni,1),np.eye(2)/2),"; Phi2(rho)==rho:",np.allclose(ch(rho,uni,2),rho))
