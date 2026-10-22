"""Coordinator checks for owner report 5, independent of its checker.
Complex matrices with Fraction entries (pairs re, im); the report's real trick Y(x)Y = -J(x)J is not used."""
from fractions import Fraction as F
from itertools import product
def c(a,b=0): return (F(a),F(b))
def cadd(x,y): return (x[0]+y[0],x[1]+y[1])
def cmul(x,y): return (x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def cconj(x): return (x[0],-x[1])
def M(rows): return [[r if isinstance(r,tuple) else c(r) for r in row] for row in rows]
def mm(A,B): return [[ (lambda i,j: __import__('functools').reduce(cadd,[cmul(A[i][k],B[k][j]) for k in range(len(B))],c(0)))(i,j) for j in range(len(B[0]))] for i in range(len(A))]
def dag(A): return [[cconj(A[j][i]) for j in range(len(A))] for i in range(len(A[0]))]
def kron(A,B): return [[cmul(A[i//len(B)][j//len(B)],B[i%len(B)][j%len(B)]) for j in range(len(A)*len(B))] for i in range(len(A)*len(B))]
def lin(*terms):
    n=len(terms[0][1]); out=[[c(0)]*n for _ in range(n)]
    for s,A in terms: out=[[cadd(out[i][j],cmul(c(s) if not isinstance(s,tuple) else s,A[i][j])) for j in range(n)] for i in range(n)]
    return out
def tr(A): return __import__('functools').reduce(cadd,[A[i][i] for i in range(len(A))],c(0))
def ex(rho,E): t=tr(mm(rho,E)); assert t[1]==0; return t[0]
I=M([[1,0],[0,1]]); X=M([[0,1],[1,0]]); Z=M([[1,0],[0,-1]]); Y=M([[0,c(0,-1)],[c(0,1),0]])
CN=M([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]])
YY=kron(Y,Y); II=kron(I,I)
# 1. CNOT (Y x Y) CNOT = -(X x Z), with genuine complex Y.
assert mm(mm(CN,YY),dag(CN))==lin((-1,kron(X,Z)))
# 2. rho+- as coin mixtures of real Bell states reachable by H, CNOT, X, Z (the real class of test-8 N2).
def ket(v): return [[c(x)] for x in v]
def proj(v,s): k=ket(v); return [[cmul(c(s),cmul(k[i][0],cconj(k[j][0]))) for j in range(4)] for i in range(4)]
h=F(1,2)
rp=lin((1,proj([0,1,1,0],h*h)),(1,proj([1,0,0,-1],h*h)))   # (psi+ + phi-)/2, each normalized: |v|^2=2
rm=lin((1,proj([1,0,0,1],h*h)),(1,proj([0,1,-1,0],h*h)))
assert rp==lin((F(1,4),II),(F(1,4),YY)) and rm==lin((F(1,4),II),(F(-1,4),YY))
local=[kron(A,B) for A,B in product([I,X,Z],repeat=2)]
assert all(ex(rp,E)==ex(rm,E) for E in local)
# with complex local effects the Y(x)Y coordinate IS a product of local tests: local tomography restores it
assert ex(rp,YY)==1 and ex(rm,YY)==-1
cp=mm(mm(CN,rp),dag(CN)); cm=mm(mm(CN,rm),dag(CN))
print('after CNOT <XZ>:',ex(cp,kron(X,Z)),ex(cm,kron(X,Z)))
# 3. continuous real interaction U=(3I+4 J(x)X)/5 and the 12/25 bound
J=M([[0,-1],[1,0]]); A=kron(J,X)
U=lin((F(3,5),II),(F(4,5),A))
assert mm(U,dag(U))==II
Pz=lin((h,II),(h,kron(I,Z)))
up=ex(mm(mm(U,rp),dag(U)),Pz); um=ex(mm(mm(U,rm),dag(U)),Pz)
print('P(+Z_B):',up,um,' best common error:',max(abs(up-(up+um)/2),abs(um-(up+um)/2)))
# 4. W = SWAP/2 positive on products, negative after CNOT
W=lin((F(1,4),II),(F(1,4),kron(X,X)),(F(1,4),YY),(F(1,4),kron(Z,Z)))
SW=M([[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]])
assert W==lin((h,SW))
Pm=kron(lin((h,I),(-h,X)),lin((h,I),(-h,Z)))
print('W after CNOT, P(-X,-Z):',ex(mm(mm(CN,W),dag(CN)),Pm))
