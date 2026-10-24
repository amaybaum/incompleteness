# Independent check of the report's CHSH formula against the actual state/observables,
# exact rational arithmetic (real matrices; R^n has rational entries).
from fractions import Fraction as F
from itertools import product
def mm(A,B): return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def T(A): return [list(r) for r in zip(*A)]
def kron(A,B): return [[A[i//len(B)][j//len(B[0])]*B[i%len(B)][j%len(B[0])] for j in range(len(A[0])*len(B[0]))] for i in range(len(A)*len(B))]
R=[[F(3,5),F(-4,5)],[F(4,5),F(3,5)]]; Rinv=T(R); Z=[[F(1),F(0)],[F(0),F(-1)]]; I=[[F(1),F(0)],[F(0),F(1)]]
def pw(n):
    M=I
    for _ in range(abs(n)): M=mm(M,R if n>0 else Rinv)
    return M
CNOT=[[F(int(i==j if i<2 else (i^1)==j)) for j in range(4)] for i in range(4)]
def chsh(m,k):
    psi=[[x] for x in [pw(m)[0][0],F(0),pw(m)[1][0],F(0)]]  # R^m|0> (x) |0>
    psi=mm(CNOT,psi)
    conj=lambda U: mm(T(U),mm(Z,U))   # U^dagger Z U
    A=[Z,conj(pw(-m))]; B=[conj(pw(-k)),conj(pw(k))]
    E=lambda a,b: mm(T(psi),mm(kron(a,b),psi))[0][0]
    e=[[E(A[i],B[j]) for j in range(2)] for i in range(2)]
    best=max(s1*e[0][0]+s2*e[0][1]+s3*e[1][0]+s4*e[1][1] for s1,s2,s3,s4 in product([1,-1],repeat=4) if s1*s2*s3*s4==-1)
    c=pw(k); cos2k=c[0][0]**2-c[1][0]**2; sin2k=2*c[0][0]*c[1][0]
    d=pw(m); sin2m=2*d[0][0]*d[1][0]
    formula=2*(cos2k+sin2m**2*sin2k)
    return e,best,formula
for m,k in [(-6,-3),(1,1),(2,-1),(3,2),(72,-47)]:
    e,best,formula=chsh(m,k)
    print(m,k,'max-CHSH-over-sign-patterns==formula:',best==formula, float(best), float(formula))
print('--- fixed sign patterns vs formula over m,k in [-6,6]')
pats=[p for p in product([1,-1],repeat=4) if p[0]*p[1]*p[2]*p[3]==-1]
ok={p:0 for p in pats}; tot=0
for m in range(-6,7):
    for k in range(-6,7):
        e,best,formula=chsh(m,k); tot+=1
        for p in pats:
            if p[0]*e[0][0]+p[1]*e[0][1]+p[2]*e[1][0]+p[3]*e[1][1]==formula: ok[p]+=1
for p in pats: print(p, ok[p],'/',tot)
