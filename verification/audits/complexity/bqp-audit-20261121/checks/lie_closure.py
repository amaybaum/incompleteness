# Exact Lie-closure dimension (over R) of the real span of {i(1-P)/2 : P in a set of permutation
# involutions} inside u(N), N = 2^n. Every generator annihilates the uniform vector, so the closure
# lies in u(N-1) acting on its orthogonal complement, of real dimension (N-1)^2.
# Arithmetic: Gaussian rationals with fractions.Fraction; rank by exact Gaussian elimination.
# Expected output (observed, then recorded; not preregistered): 2, 9, 49.
#   control: two commuting NOTs give a two-dimensional abelian algebra;
#   2 bits, NOT/CNOT/SWAP: 9 = (4-1)^2; 3 bits, NOT/CNOT/Toffoli: 49 = (8-1)^2.
# A finite witness for N = 4 and N = 8 only. It says nothing about gate cost or efficiency.
import itertools
from fractions import Fraction as Fr
def mul(A,B,N):
    C=[[(Fr(0),Fr(0))]*N for _ in range(N)]
    for i in range(N):
        for k in range(N):
            a=A[i][k]
            if a==(0,0): continue
            for j in range(N):
                b=B[k][j]
                if b==(0,0): continue
                r,s=C[i][j]; C[i][j]=(r+a[0]*b[0]-a[1]*b[1], s+a[0]*b[1]+a[1]*b[0])
    return C
def sub(A,B,N): return [[(A[i][j][0]-B[i][j][0],A[i][j][1]-B[i][j][1]) for j in range(N)] for i in range(N)]
def vec(A): return [x for row in A for e in row for x in e]
class Span:
    def __init__(s): s.piv={}  # pivot col -> reduced row
    def add(s,v):
        v=list(v)
        for c,r in s.piv.items():
            if v[c]!=0:
                f=v[c]; v=[a-f*b for a,b in zip(v,r)]
        for c,x in enumerate(v):
            if x!=0:
                v=[a/x for a in v]
                for c2,r in list(s.piv.items()):
                    if r[c]!=0: f=r[c]; s.piv[c2]=[a-f*b for a,b in zip(r,v)]
                s.piv[c]=v; return True
        return False
def gen(p):
    N=len(p); G=[[(Fr(0),Fr(0))]*N for _ in range(N)]
    for x in range(N):
        G[x][x]=(Fr(0),G[x][x][1]+Fr(1,2))
        G[p[x]][x]=(Fr(0),G[p[x]][x][1]-Fr(1,2))
    return G
def closure(perms):
    N=len(perms[0]); S=Span(); B=[]
    for p in perms:
        g=gen(p)
        if S.add(vec(g)): B.append(g)
    i=0
    while i<len(B):
        for j in range(i):
            c=sub(mul(B[i],B[j],N),mul(B[j],B[i],N),N)
            if S.add(vec(c)): B.append(c)
        i+=1
    return len(B)
def bp(n,f): return [f(x) for x in range(2**n)]
X0=lambda x:x^1; X1=lambda x:x^2
C01=lambda x: x^2 if x&1 else x; C10=lambda x: x^1 if x&2 else x
SW=lambda x: ((x&1)<<1)|((x>>1)&1)
c0=closure([bp(2,f) for f in [X0,X1]])
print("control, NOTs only (expect 2, abelian):",c0)
c2=closure([bp(2,f) for f in [X0,X1,C01,C10,SW]])
print("2-bit NOT,CNOT,SWAP: dim",c2,"of u(4)=16; (N-1)^2 = 9")
fs=[lambda x,i=i:x^(1<<i) for i in range(3)]
for c,t in itertools.permutations(range(3),2): fs.append(lambda x,c=c,t=t: x^(1<<t) if x>>c&1 else x)
fs.append(lambda x: x^4 if (x&3)==3 else x)
c3=closure([bp(3,f) for f in fs])
print("3-bit NOT,CNOT,Toffoli: dim",c3,"of u(8)=64; (N-1)^2 = 49")
assert (c0,c2,c3)==(2,9,49), (c0,c2,c3)
print("OK")
