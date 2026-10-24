import numpy as np, itertools
from collections import Counter
I=np.eye(2,dtype=object); X=np.array([[0,1],[1,0]],dtype=object); Z=np.array([[1,0],[0,-1]],dtype=object)
Hs=np.array([[1,1],[1,-1]],dtype=object); CN=np.array([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]],dtype=object)
P1=[I,X,Z,X.dot(Z)]
P2=[np.kron(a,b) for a in P1 for b in P1]
def run(S,C,k):   # S: swap_A lift (scaled), C: couple lift; word (S,C)^3, then extra S if k==7
    psi=np.array([1,0,0,0],dtype=object)
    for _ in range(3): psi=C.dot(S.dot(psi))
    if k==7: psi=S.dot(psi)
    tot=sum(int(x)**2 for x in psi); p1=sum(int(psi[i])**2 for i in (1,3))
    from fractions import Fraction as F; return F(p1,tot)
HA=np.kron(Hs,I)
cnt=Counter()
for Ps in P2:
    for Pc in P2:
        S=Ps.dot(HA); C=Pc.dot(CN)
        cnt[(run(S,C,6),run(S,C,7))]+=1
print(dict(cnt))
names=['I','X','Z','XZ']
for i,a in enumerate(P1):
    for j,b in enumerate(P1):
        S=np.kron(a,b).dot(HA)
        print('swap lift',names[i]+'_A',names[j]+'_B','·H_A -> W6',run(S,CN,6),'W7',run(S,CN,7))
