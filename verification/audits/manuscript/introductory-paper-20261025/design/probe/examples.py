from fractions import Fraction as F
from itertools import product
# Main §2.4 minimal model: x in {0,1}, h in {1..6}, sigma = listed transpositions
pairs=[((0,1),(1,1)),((0,2),(1,2)),((0,3),(0,4)),((0,5),(0,6)),((1,3),(1,4)),((1,5),(1,6))]
s={}
for a,b in pairs: s[a]=b; s[b]=a
states=[(x,h) for x in (0,1) for h in range(1,7)]
assert sorted(s)==sorted(states) and all(s[s[z]]==z for z in states)  # involution => bijection
def T(k):
    M=[[F(0)]*2 for _ in range(2)]
    for x in (0,1):
        for h in range(1,7):
            z=(x,h)
            for _ in range(k): z=s[z]
            M[x][z[0]]+=F(1,6)
    return M
T1,T2=T(1),T(2)
print("T(1,0)=",T1,"T(2,0)=",T2)
det=T1[0][0]*T1[1][1]-T1[0][1]*T1[1][0]
inv=[[T1[1][1]/det,-T1[0][1]/det],[-T1[1][0]/det,T1[0][0]/det]]
Lam=[[sum(inv[i][k]*T2[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
# Main writes Λ(2,1)=T(2,0)T(1,0)^{-1}; with T2=I both orders coincide
print("Lambda=",Lam)
# conditional memory with x0 uniform, h uniform
joint={}
for x0 in (0,1):
    for h in range(1,7):
        z1=s[(x0,h)]; z2=s[z1]
        key=(x0,z1[0],z2[0]); joint[key]=joint.get(key,0)+F(1,12)
p=lambda pred: sum(v for k,v in joint.items() if pred(k))
print("P(x2=0|x1=1,x0=0)=",p(lambda k:k==(0,1,0))/p(lambda k:k[0]==0 and k[1]==1))
print("P(x2=0|x1=1)=",p(lambda k:k[1]==1 and k[2]==0)/p(lambda k:k[1]==1))
# XOR family: X0,X1 iid uniform, X2 = X0 xor X1
J={(a,b,a^b):F(1,4) for a,b in product((0,1),repeat=2)}
def tk(i,j):
    M=[[F(0)]*2 for _ in range(2)]
    for k,v in J.items(): M[k[i]][k[j]]+=v*2
    return M
print("XOR T(1,0),T(2,1),T(2,0):",tk(0,1),tk(1,2),tk(0,2))
import math
def H(d):
    return -sum(float(v)*math.log2(float(v)) for v in d.values() if v)
def marg(idx):
    d={}
    for k,v in J.items():
        kk=tuple(k[i] for i in idx); d[kk]=d.get(kk,0)+v
    return d
I=H(marg((0,1)))+H(marg((1,2)))-H(J)-H(marg((1,)))
print("I(X0;X2|X1) bits =",I)
# control: Markov (iid) process must give 0
Jc={k:F(1,8) for k in product((0,1),repeat=3)}
J2=J; J=Jc
print("control iid I =",H(marg((0,1)))+H(marg((1,2)))-H(J)-H(marg((1,))))
