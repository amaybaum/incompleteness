"""Separate stdlib rational-complex certificate implementation; imports no probe."""
from fractions import Fraction as F

def c(a=0,b=0): return F(a),F(b)
def plus(x,y): return x[0]+y[0],x[1]+y[1]
def neg(x): return -x[0],-x[1]
def mul(x,y): return x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0]
def conj(x): return x[0],-x[1]
Z=c(); ONE=c(1)
def matrix(n): return [[Z for _ in range(n)] for _ in range(n)]
def identity(n):
    x=matrix(n)
    for i in range(n): x[i][i]=ONE
    return x
def add(x,y): return [[plus(a,b) for a,b in zip(r,t)] for r,t in zip(x,y)]
def scale(x,a): return [[mul(v,c(a)) for v in r] for r in x]
def dagger(x): return [[conj(x[j][i]) for j in range(len(x))] for i in range(len(x))]
def multiply(x,y):
    n=len(x); out=matrix(n)
    for i in range(n):
        for j in range(n):
            for k in range(n): out[i][j]=plus(out[i][j],mul(x[i][k],y[k][j]))
    return out
def adjoint(k,x): return multiply(multiply(k,x),dagger(k))
def transpose_second(x):
    return [[x[2*(i//2)+j%2][2*(j//2)+i%2] for j in range(4)] for i in range(4)]
def trace(x):
    out=Z
    for i in range(len(x)): out=plus(out,x[i][i])
    return out
def pairing(x,y): return trace(multiply(x,y))
def kron(x,y):
    return [[mul(x[i//2][j//2],y[i%2][j%2]) for j in range(4)] for i in range(4)]
def conjugate_entries(x): return [[conj(v) for v in r] for r in x]
def projector(v, denominator=1):
    return [[mul(mul(a,conj(b)),c(F(1,denominator))) for b in v] for a in v]

checks=0
def require(test,name):
    global checks
    if not test: raise AssertionError(name)
    checks+=1

I=identity(4)
D=[[ONE,Z],[Z,c(F(3,5),F(4,5))]]
U=kron(identity(2),D)
Ubar=conjugate_entries(U)
def stopped(x): return add(scale(adjoint(U,x),F(5,8)),scale(x,F(3,8)))
B=projector([ONE,Z,Z,ONE],2)
minus=projector([Z,ONE,c(-1),Z],2)
require(pairing(transpose_second(B),minus)==c(F(-1,2)), 'Bell negative exact vector')
require(transpose_second(transpose_second(B))==B,'Bell involution')
require(trace(transpose_second(B))==ONE,'Bell trace')
qout=stopped(B)
require(plus(mul(qout[0][0],qout[3][3]),neg(mul(qout[0][3],qout[3][0])))==c(F(3,64)),'actual quantum PSD minor')
K=[[ONE,c(0,F(1,3))],[c(F(2,5)),c(F(1,2))]]
L=kron(identity(2),K); Lbar=conjugate_entries(L)
for i in range(4):
    for j in range(4):
        E=matrix(4); E[i][j]=ONE
        require(transpose_second(transpose_second(E))==E,f'involution {i},{j}')
        require(trace(transpose_second(E))==trace(E),f'trace {i},{j}')
        require(transpose_second(adjoint(L,transpose_second(E)))==adjoint(Lbar,E),f'CP {i},{j}')
        require(transpose_second(stopped(transpose_second(E)))==add(scale(adjoint(Ubar,E),F(5,8)),scale(E,F(3,8))),f'protocol {i},{j}')

# Write Bell columns directly, instead of composing the other script's gates.
z=c(F(3,5),F(4,5))
vectors=[[ONE,Z,Z,z],[Z,z,ONE,Z],[ONE,Z,Z,neg(z)],[Z,z,c(-1),Z]]
frame=[transpose_second(projector(v,2)) for v in vectors]
total=matrix(4)
for x in frame: total=add(total,x)
require(total==I,'frame sum')
for i,x in enumerate(frame):
    require(trace(x)==ONE,f'frame trace {i}')
    pre=transpose_second(x)
    require(multiply(pre,pre)==pre,f'projector {i}')
    for j,y in enumerate(frame): require(pairing(x,y)==c(int(i==j)),f'distinction {i},{j}')
mixed=matrix(4)
for i,x in enumerate(frame): mixed=add(mixed,scale(x,F(i+1,10)))
require(trace(mixed)==ONE,'mixture trace')
for i,x in enumerate(frame): require(pairing(mixed,x)==c(F(i+1,10)),f'mixture weight {i}')
for i in range(4):
    E=matrix(4); E[i][i]=ONE
    require(stopped(E)==E,f'classical {i}')

# Independently apply CNOT as a permutation, without copying its matrix.
permutation=[0,1,3,2]
P=projector([ONE,Z,ONE,Z],2)
rotated=[[P[permutation[i]][permutation[j]] for j in range(4)] for i in range(4)]
pre=transpose_second(rotated)
require(rotated==B,'CNOT product image')
require(pairing(pre,minus)==c(F(-1,2)),'tilted product exclusion')
def cnot_permute(x): return [[x[permutation[i]][permutation[j]] for j in range(4)] for i in range(4)]
def tilted(x): return cnot_permute(transpose_second(x))
require(pairing(tilted(minus),P)==c(F(-1,2)),'tilt fails product positivity')
seed=projector([ONE,ONE,ONE,Z],3)
tilt_state=tilted(seed)
tilt_test=tilted(projector([ONE,c(0,1),c(0,-1),Z],3))
require(transpose_second(cnot_permute(tilt_state))==seed,'tilted seed membership')
require(pairing(tilt_test,tilt_state)==c(F(1,9)),'tilted input positive')
require(pairing(tilt_test,stopped(tilt_state))==c(F(-1,9)),'tilted protocol failure')

mutations=[
    transpose_second(adjoint(L,transpose_second(B)))==adjoint(L,B),
    transpose_second(stopped(transpose_second(B)))==add(scale(adjoint(U,B),F(5,8)),scale(B,F(3,8))),
    pairing(frame[0],frame[1])==ONE,
    pairing(pre,minus)[0]>=0,
]
for i,test in enumerate(mutations): require(not test,f'mutation {i}')
print('CONTROLS',checks)
print('MUTATIONS rejected',len(mutations))
print('CERTIFICATES coPSD local preservation; CNOT tilt fails protocol and domain')
print('SP => guaranteed stopped-map preservation: OPEN on the common domain')
