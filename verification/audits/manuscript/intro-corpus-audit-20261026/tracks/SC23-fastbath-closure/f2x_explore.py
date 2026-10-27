# EXPLORATORY (not preregistered): does small record-conditional eps (relaxation lambda -> 1) imply
# a stochastic divisor T^(2) = T Lambda? Exhaustive over bijections of Z3 x Z2, relax p->(1-l)p+l*pi.
# Control: l = 1 must give Lambda == T exactly (stochastic) for every invertible T.
import itertools
from fractions import Fraction as F
def inv3(M):
    a,b,c=M[0];d,e,f=M[1];g,h,i=M[2]
    det=a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)
    if det==0: return None
    adj=[[e*i-f*h,c*h-b*i,b*f-c*e],[f*g-d*i,a*i-c*g,c*d-a*f],[d*h-e*g,b*g-a*h,a*e-b*d]]
    return [[x/det for x in r] for r in adj]
def mm(A,B): return [[sum(A[i][k]*B[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
sp=[(x,h) for x in range(3) for h in range(2)]
def run(lam):
    n_inv=n_neg=0; ctrl=True; ex=None
    for img in itertools.permutations(sp):
        phi=dict(zip(sp,img))
        T=[[F(0)]*3 for _ in range(3)]; mu={}
        for x0 in range(3):
            for h in range(2):
                x1,h1=phi[(x0,h)]; T[x0][x1]+=F(1,2); mu.setdefault((x0,x1),[F(0),F(0)])[h1]+=F(1,2)
        T2=[[F(0)]*3 for _ in range(3)]; eps=F(0)
        for (x0,x1),d in mu.items():
            tot=sum(d); d=[(1-lam)*v/tot+lam*F(1,2) for v in d]; eps=max(eps,abs(d[0]-F(1,2)))
            for h in range(2):
                x2,_=phi[(x1,h)]; T2[x0][x2]+=T[x0][x1]*d[h]
        Ti=inv3(T)
        if Ti is None: continue
        n_inv+=1; L=mm(Ti,T2)
        if lam==1 and L!=T: ctrl=False
        if min(min(r) for r in L)<0:
            n_neg+=1
            if ex is None: ex=(T,L,eps)
    return n_inv,n_neg,ctrl,ex
for lam in (F(1),F(999,1000),F(999999,1000000)):
    n_inv,n_neg,ctrl,ex=run(lam)
    print(f"lambda={lam}: invertible-T bijections={n_inv}, with negative unique divisor={n_neg}, control(Lambda==T at lambda=1)={ctrl}")
    if ex: print("   example eps=",ex[2]," T=",[[str(v) for v in r] for r in ex[0]]," min Lambda entry=",min(min(r) for r in ex[1]))
