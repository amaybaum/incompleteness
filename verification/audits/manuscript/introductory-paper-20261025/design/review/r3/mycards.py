from fractions import Fraction as F
from itertools import product
import numpy as np
C=(0,1)
swap=lambda s:(s[1],s[0])
def odds(proto):
    tot=F(0);n=0
    for h0,b0,r1,r2 in product(C,repeat=4):
        s=proto((h0,b0),r1,r2); n+=1
        tot+= (1 if s[0]==h0 else 0)
    return F(tot,n), n
rules={
 'one shuffle':            lambda s,r1,r2: swap(s),
 'two shuffles':           lambda s,r1,r2: swap(swap(s)),
 'peek passive':           lambda s,r1,r2: swap(swap(s)),
 'A burn overwritten':     lambda s,r1,r2: swap((swap(s)[0], r1)),
 'B hole replaced only':   lambda s,r1,r2: swap((r1, swap(s)[1])),
 'C both replaced':        lambda s,r1,r2: swap((r1, r2)),
 'D revealed->burn, new hole': lambda s,r1,r2: swap((r1, swap(s)[0])),
}
for k,f in rules.items(): print(k, *odds(f))
# chained one-street odds
T1=[[F(0)]*2 for _ in C]
for h0,b0 in product(C,repeat=2):
    T1[h0][swap((h0,b0))[0]]+=F(1,2)
T2=[[sum(T1[i][k]*T1[k][j] for k in C) for j in C] for i in C]
print('T1',T1,'chained match', T2[0][0])
# quantum embedding: swap unitary on C2xC2, channels Phi_t(rho)=Tr_H[U^t (rho x I/2) U^-t]
S=np.zeros((4,4))
for x,h in product(C,repeat=2): S[2*h+x,2*x+h]=1
def chan(t,rho):
    U=np.linalg.matrix_power(S,t); R=U@np.kron(rho,np.eye(2)/2)@U.T
    return np.einsum('ahbh->ab',R.reshape(2,2,2,2))
plus=np.array([[.5,.5],[.5,.5]])
print('Phi1(|+><+|)=',chan(1,plus).round(6).tolist(),' Phi2(|+><+|)=',chan(2,plus).round(6).tolist())
