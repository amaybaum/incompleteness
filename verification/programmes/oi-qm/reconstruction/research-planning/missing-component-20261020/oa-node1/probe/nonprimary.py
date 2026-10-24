#!/usr/bin/env python3
"""nonprimary.py -- exact check, standard library only (Fractions over Q(sqrt3)(i)).
Question (node 1, route R2-strob): is the uniform-ray (ones-fixing) exclusion of stroboscopic
interpolation of native pair bijections a property of the substratum dynamics, or of the choice of
the principal (primary) logarithm?
Generators are logarithms divided by pi.  A logarithm L of a permutation matrix P with
exp(L) = P is PRIMARY if it is a function of P; NON-PRIMARY logs add 2*pi*i*K with K Hermitian,
integer spectrum, [K,P] = 0, K not a function of P (possible only when P has a repeated eigenvalue).
Decision rule (fixed before running): the ones-fixing exclusion is branch-relative iff
  (a) exp(L_np) = CNOT exactly, and (b) the Lie algebra of the principal logs plus L_np is not
  ones-fixing; it is branch-independent iff (b) fails for every tested non-primary K.
Controls: POS (principal-only algebra reproduces dim 9, ones-fixing: independent code path vs the
recorded x-screen P4); NEG (K = uniform projector, non-primary yet ones-fixing: the test can return
'ones-fixing' on a non-primary log); E0 (non-primary log of the identity is the posited phase flow);
KNOB (two admissible K give different half-period flows).
"""
from fractions import Fraction as Fr
from itertools import permutations
class R:
    __slots__=('a','b')
    def __init__(s,a=0,b=0): s.a=Fr(a); s.b=Fr(b)
    def __add__(s,o): return R(s.a+o.a,s.b+o.b)
    def __sub__(s,o): return R(s.a-o.a,s.b-o.b)
    def __mul__(s,o): return R(s.a*o.a+3*s.b*o.b,s.a*o.b+s.b*o.a)
    def __neg__(s): return R(-s.a,-s.b)
    def z(s): return s.a==0 and s.b==0
    def inv(s):
        d=s.a*s.a-3*s.b*s.b; return R(s.a/d,-s.b/d)
    def __eq__(s,o): return s.a==o.a and s.b==o.b
class C:
    __slots__=('x','y')
    def __init__(s,x=None,y=None): s.x=x if x is not None else R(); s.y=y if y is not None else R()
    def __add__(s,o): return C(s.x+o.x,s.y+o.y)
    def __sub__(s,o): return C(s.x-o.x,s.y-o.y)
    def __mul__(s,o): return C(s.x*o.x-s.y*o.y,s.x*o.y+s.y*o.x)
    def conj(s): return C(s.x,-s.y)
    def z(s): return s.x.z() and s.y.z()
    def __eq__(s,o): return s.x==o.x and s.y==o.y
def c(re=0,im=0,re3=0,im3=0): return C(R(re,re3),R(im,im3))
N=4
Z=lambda: [[c() for _ in range(N)] for _ in range(N)]
def I():
    M=Z()
    for k in range(N): M[k][k]=c(1)
    return M
def mul(A,B):
    M=Z()
    for i in range(N):
        for j in range(N):
            s=c()
            for k in range(N): s=s+A[i][k]*B[k][j]
            M[i][j]=s
    return M
def add(A,B): return [[A[i][j]+B[i][j] for j in range(N)] for i in range(N)]
def sc(z,A): return [[z*A[i][j] for j in range(N)] for i in range(N)]
def sub(A,B): return add(A,sc(c(-1),B))
def eq(A,B): return all(A[i][j]==B[i][j] for i in range(N) for j in range(N))
def br(A,B): return sub(mul(A,B),mul(B,A))
def pm(p):
    M=Z()
    for col,row in enumerate(p): M[row][col]=c(1)
    return M
def order(p):
    q=list(range(N)); k=0
    while True:
        q=[p[x] for x in q]; k+=1
        if q==list(range(N)): return k
W={1:[c(1)],2:[c(1),c(-1)],3:[c(1),c(Fr(-1,2),0,0,Fr(1,2)),c(Fr(-1,2),0,0,Fr(-1,2))],4:[c(1),c(0,1),c(-1),c(0,-1)]}
def projectors(p):
    P=pm(p); m=order(p); w=W[m]; pw=[I()]
    for _ in range(m-1): pw.append(mul(pw[-1],P))
    out=[]
    for j in range(m):
        Pi=Z()
        for k in range(m): Pi=add(Pi,sc(w[(j*k)%m].conj(),pw[k]))
        out.append((Fr(2*j,m),sc(c(Fr(1,m)),Pi)))
    return out
def plog(p):
    L=Z()
    for th,Pi in projectors(p):
        if th>1: th-=2
        L=add(L,sc(c(0,th),Pi))
    return L  # (1/pi) * principal log
def vec(A):
    v=[]
    for i in range(N):
        for j in range(N): v+=[A[i][j].x,A[i][j].y]
    return v
def lie_dim(gens):
    basis=[]; mats=[]
    def red(v):
        v=list(v)
        for piv,b in basis:
            if not v[piv].z():
                f=v[piv]; v=[v[k]-f*b[k] for k in range(len(v))]
        return v
    def ins(A):
        v=red(vec(A))
        for k,x in enumerate(v):
            if not x.z():
                f=x.inv(); v=[y*f for y in v]
                nb=[]
                for piv,b in basis:
                    if not b[k].z():
                        g=b[k]; b=[b[t]-g*v[t] for t in range(len(v))]
                    nb.append((piv,b))
                basis[:]=nb+[(k,v)]; mats.append(A); return True
        return False
    for g in gens: ins(g)
    ch=True
    while ch:
        ch=False; cur=list(mats)
        for a in range(len(cur)):
            for b in range(a+1,len(cur)):
                if ins(br(cur[a],cur[b])): ch=True
    return mats
def ones_fixing(A):
    w=[sum((A[i][j] for j in range(N)),c()) for i in range(N)]
    return all(x==w[0] for x in w)
def unif_fixing(mats): return all(ones_fixing(A) for A in mats)
def E(a):
    M=Z(); M[a][a]=c(1); return M
results=[]
def rec(name,ok,info=''):
    results.append(ok); print(('PASS ' if ok else 'FAIL ')+name+(' : '+info if info else ''))
# basis order 00,01,10,11 ; CNOT (control token 1) swaps 10<->11
cnot=(0,1,3,2); CN=pm(cnot)
perms=list(permutations(range(N)))
PL=[plog(p) for p in perms]
# exactness of principal logs: spectral reconstruction sum_j w_j Pi_j = P  (generic sanity)
okrec=all(eq(add(Z(),sum_j) if False else (lambda pr:(lambda S:S)(__import__('functools').reduce(add,[sc(W[order(p)][k],Pi) for k,(th,Pi) in enumerate(pr)],Z())))(projectors(p)),pm(p)) for p in perms)
rec('SPEC every native pair bijection equals sum_j omega^j Pi_j (projectors exact)',okrec)
# POS control: principal-only algebra
A0=lie_dim(PL)
rec('POS principal-log algebra of the 24 native pair bijections: dim 9 (x-screen P4 value), ones-fixing',len(A0)==9 and unif_fixing(A0),'dim %d, ones-fixing %s'%(len(A0),unif_fixing(A0)))
# non-primary log of CNOT: K = E00 (Hermitian, integer spectrum, commutes with CNOT, inside +1 eigenspace)
K=E(0)
rec('NP1 [K,CNOT]=0 and CNOT K = K (K inside the +1 eigenspace)',eq(br(K,CN),Z()) and eq(mul(CN,K),K))
fun_of_P=False
# K a function of CNOT iff K in span{I, CNOT}
for a in [Fr(0),Fr(1)]:
    pass
# check K not in span{I,CNOT}: entries (0,0)=1,(1,1)=0 would need alpha+beta*1 equal on both diag -> impossible
rec('NP2 K is not a function of CNOT (K00 != K11 while CNOT acts identically on 00 and 01)',not (K[0][0]==K[1][1]))
# exp(L_np) = CNOT: L_np = L_p + 2 pi i K, commuting, exp(2 pi i K) = I + (e^{2 pi i}-1)K = I
Lp=plog(cnot); Lnp=add(Lp,sc(c(0,2),K))
rec('NP3 [L_p, K]=0 so exp(L_np)=exp(L_p)exp(2 pi i K)=CNOT*I exactly',eq(br(Lp,K),Z()))
# half-period flows: U_p(1/2) = Pi_+ + i Pi_-, phase factor exp(i pi K) = I - 2K
prs=projectors(cnot)  # th=0 -> Pi_+, th=1 -> Pi_-
Pp=[Pi for th,Pi in prs if th==0][0]; Pm=[Pi for th,Pi in prs if th==1][0]
Up=add(Pp,sc(c(0,1),Pm)); Unp=mul(Up,sub(I(),sc(c(2),K)))
rec('NP4 U_p(1/2)^2 = CNOT and U_np(1/2)^2 = CNOT (both are half-period values of time-one CNOT flows)',eq(mul(Up,Up),CN) and eq(mul(Unp,Unp),CN))
rec('NP5 U_p(1/2) fixes the uniform ray; U_np(1/2) does not',ones_fixing(Up) and not ones_fixing(Unp))
def creal_multiple(A):
    # A = c*M with M real?  find a nonzero entry, divide, test all ratios real (Q(sqrt3) imaginary part zero)
    for i in range(N):
        for j in range(N):
            if not A[i][j].z():
                z0=A[i][j]
                # ratio A_kl / z0 real  <=> Im(A_kl * conj(z0)) = 0
                return all((A[k][l]*z0.conj()).y.z() for k in range(N) for l in range(N))
    return True
rec('NP6 U_np(1/2) is not a scalar multiple of a real matrix (reality invariant broken)',not creal_multiple(Unp))
A1=lie_dim(PL+[Lnp])
rec('NP7 principal logs + one non-primary CNOT log: dim 16 = u(4), not ones-fixing',len(A1)==16 and not unif_fixing(A1),'dim %d, ones-fixing %s'%(len(A1),unif_fixing(A1)))
# NEG control: K = uniform projector J/4 (in +1 eigenspace of CNOT, commutes, integer spectrum, not a function of CNOT)
J=Z()
for i in range(N):
    for j in range(N): J[i][j]=c(Fr(1,4))
rec('NEG0 J/4 is a projector commuting with CNOT, not a function of CNOT',eq(mul(J,J),J) and eq(br(J,CN),Z()) and not (J[0][1]==Z()[0][1] and J[0][0]==J[2][2] and J[2][3]==Z()[2][3]) )
A2=lie_dim(PL+[add(Lp,sc(c(0,2),J))])
rec('NEG non-primary log with K = J/4 keeps the algebra ones-fixing (the test can say ones-fixing on a non-primary log)',unif_fixing(A2),'dim %d'%len(A2))
# E0 control: non-primary log of the identity, 2 pi i E00: its flow at t = 1/4 is the quarter phase diag(i,1,1,1)
Q=I(); Q[0][0]=c(0,1)
rec('E0 exp((1/4)*2 pi i E00) = diag(i,1,1,1), the quarter phase (I + (i-1)E00)',eq(add(I(),sc(c(-1,1),E(0))),Q))
# KNOB: K' = |v><v|, v = (|00>+|01>)/sqrt2 also admissible; half-period flow differs from K=E00
Kv=Z()
for i in (0,1):
    for j in (0,1): Kv[i][j]=c(Fr(1,2))
Unp2=mul(Up,sub(I(),sc(c(2),Kv)))
rec('KNOB K\' = |v><v| (v in +1 eigenspace) admissible and gives a different half-period flow',eq(br(Kv,CN),Z()) and eq(mul(Kv,Kv),Kv) and not eq(Unp2,Unp) and eq(mul(Unp2,Unp2),CN))
# IDN control: non-primary log of the identity with K = |+><+| (x) I: flow at t = 1/4 is non-monomial, period 4
Kp=Z()
for (i,j) in [(0,0),(0,2),(2,0),(2,2),(1,1),(1,3),(3,1),(3,3)]: Kp[i][j]=c(Fr(1,2))
Uq=add(I(),sc(c(-1,1),Kp))
U4=mul(mul(Uq,Uq),mul(Uq,Uq))
nonmono=any(sum(1 for j in range(N) if not Uq[i][j].z())>1 for i in range(N))
rec('IDN K=|+><+|(x)I is a projector; exp((1/4)2 pi i K) is non-monomial and its 4th power is I (an interpolation of doing nothing)',eq(mul(Kp,Kp),Kp) and nonmono and eq(U4,I()))
print('SUMMARY %d/%d PASS'%(sum(results),len(results)))
ok=all(results)
if ok:
    print('VERDICT R2-STROB: the ones-fixing exclusion of stroboscopic interpolation is branch-relative: with the principal logarithm the native algebra is ones-fixing (dim %d); one non-primary logarithm of CNOT, exact at integer times, gives dim %d and leaves the uniform ray, and the non-primary freedom contains the posited quarter phase (E0 control).'%(len(A0),len(A1)))
else:
    print('VERDICT VOID: a control or check failed')
