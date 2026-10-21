#!/usr/bin/env python3
"""Exact controls for the independent OI fixed-gate handoff; no repository writes.
Python standard library only. Gaussian integers are pairs (real, imaginary).
The simulator deliberately imports quantum matrix rules; it is a calibration.
"""
from fractions import Fraction as F
from collections import Counter
from math import atan2, pi
from decimal import Decimal, localcontext
import json

Z=(0,0); O=(1,0)
def ga(x,y): return (x[0]+y[0], x[1]+y[1])
def gm(x,y): return (x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def gc(x): return (x[0],-x[1])
def mat(rows): return [[(x,0) if isinstance(x,int) else x for x in row] for row in rows]
def mm(A,B):
    C=[[Z for _ in B[0]] for _ in A]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)): C[i][j]=ga(C[i][j],gm(A[i][k],B[k][j]))
    return C
def adj(A): return [[gc(A[j][i]) for j in range(len(A))] for i in range(len(A[0]))]
def kron(A,B): return [[gm(A[i//len(B)][j//len(B[0])],B[i%len(B)][j%len(B[0])]) for j in range(len(A[0])*len(B[0]))] for i in range(len(A)*len(B))]
def tr(A):
    assert all(A[i][i][1]==0 for i in range(len(A)))
    return sum(A[i][i][0] for i in range(len(A)))
def lift(U,n,q):
    V=[[O]]
    for i in range(n): V=kron(V,U if i==q else I)
    return V
I=mat([[1,0],[0,1]])
M=mat([[3,-4],[4,3]])
S=mat([[1,0],[0,(0,1)]])
X=mat([[0,1],[1,0]])
ZZ=mat([[1,0],[0,-1]])
CNOT=mat([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]])

class Machine:
    """Unnormalized density D/25**k plus a residual interval index j.
    Initial j is uniform on range(25**K), independent of protocol choice.
    Logical measurements append physical records to a declared list.
    This logical machine is not itself a reversible lattice implementation.
    """
    def __init__(self,n,K,j):
        self.n=n; self.K=K; self.k=0; self.j=j; self.records=[]
        self.D=[[Z for _ in range(2**n)] for _ in range(2**n)]
        self.D[0][0]=O
        self.valid()
    def valid(self):
        assert self.k<=self.K
        assert 0<=self.j<tr(self.D)*25**(self.K-self.k)
    def gate(self,name,q=0):
        if name=='R': U=lift(M,self.n,q); self.k+=1
        elif name=='S': U=lift(S,self.n,q)
        elif name=='CNOT':
            assert self.n==2 and q==0
            U=CNOT
        else: raise ValueError(name)
        self.D=mm(mm(U,self.D),adj(U)); self.valid()
    def inverse_R(self,q=0):
        for _ in range(2): self.gate('S',q)
        self.gate('R',q)
        for _ in range(2): self.gate('S',q)
    def measure(self,q=0):
        mask=1<<(self.n-1-q)
        d0=[[self.D[i][j] if not(i&mask) and not(j&mask) else Z for j in range(len(self.D))] for i in range(len(self.D))]
        width0=tr(d0)*25**(self.K-self.k)
        if self.j<width0: outcome=0; self.D=d0
        else:
            outcome=1; self.j-=width0
            self.D=[[self.D[i][j] if (i&mask) and (j&mask) else Z for j in range(len(self.D))] for i in range(len(self.D))]
        self.records.append(outcome); self.valid()
        return outcome
    def append_zero(self):
        self.D=kron(self.D,mat([[1,0],[0,0]])); self.n+=1; self.valid()
    def discard_last(self):
        d=len(self.D)//2
        self.D=[[ga(self.D[2*i][2*j],self.D[2*i+1][2*j+1]) for j in range(d)] for i in range(d)]
        self.n-=1; self.valid()

def run(name,K,j):
    t=Machine(1,K,j)
    if name=='once': t.gate('R'); t.measure()
    elif name=='twice': t.gate('R'); t.gate('R'); t.measure()
    elif name=='echo': t.gate('R'); t.inverse_R(); t.measure()
    elif name=='read_between': t.gate('R'); t.measure(); t.gate('R'); t.measure()
    elif name=='adaptive':
        t.gate('R'); b=t.measure()
        t.gate('R' if b else 'S'); t.measure()
    elif name=='phase': t.gate('R'); t.gate('S'); t.gate('R'); t.measure()
    elif name=='composite':
        t.gate('R'); t.append_zero(); t.gate('CNOT'); t.gate('R'); t.measure(0); t.measure(1)
    elif name=='discard':
        t.gate('R'); t.append_zero(); t.gate('CNOT'); t.discard_last(); t.gate('R'); t.measure()
    else: raise ValueError(name)
    return tuple(t.records)

def counts(name,K): return Counter(run(name,K,j) for j in range(25**K))
expected={
 'once':{(0,):225,(1,):400},
 'twice':{(0,):49,(1,):576},
 'echo':{(0,):625},
 'read_between':{(0,0):81,(0,1):144,(1,0):256,(1,1):144},
 'adaptive':{(0,0):225,(1,0):256,(1,1):144},
 'phase':{(0,):337,(1,):288},
 'composite':{(0,0):81,(0,1):256,(1,0):144,(1,1):144},
 'discard':{(0,):337,(1,):288}}
out={}
for name,target in expected.items():
    result=counts(name,2)
    assert result==target,(name,result)
    out[name]={''.join(map(str,k)):v for k,v in sorted(result.items())}
print('EXHAUSTIVE_625_SEEDS '+json.dumps(out,sort_keys=True))

# Exact compatibility at the outcome-record level under j_(K+1)=25*j_K+d.
# Exhaust all 25 possible refinements for every seed of the one-R experiment.
assert all(run('once',2,25*j+d)==run('once',1,j) for j in range(25) for d in range(25))
# Exhaust all 15625 refinements for the adaptive two-R protocol.
assert all(run('adaptive',3,25*j+d)==run('adaptive',2,j) for j in range(625) for d in range(25))
print('BUDGET_COMPATIBILITY once 625/625; adaptive 15625/15625')

# Choi calibration: Bell state is an external exact calibration input, not
# claimed to be exactly preparable by the finite rational gate alphabet.
B=mat([[1,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,1]]) # density B/2
L=lift(M,2,0)
C=mm(mm(L,B),adj(L)) # output density C/50
v=[3,-4,4,3]
assert C==mat([[a*b for b in v] for a in v])
assert mm(C,C)==mat([[50*a*b for b in v] for a in v])
for which in (0,1):
    reduced=[[Z for _ in range(2)] for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for b in range(2):
                a0,a1=(2*i+b,2*j+b) if which==0 else (2*b+i,2*b+j)
                reduced[i][j]=ga(reduced[i][j],C[a0][a1])
    assert reduced==mat([[25,0],[0,25]])
cor={}
for name,A,Bb in [('XX',X,X),('ZZ',ZZ,ZZ),('XZ',X,ZZ),('ZX',ZZ,X)]:
    cor[name]=str(F(tr(mm(C,kron(A,Bb))),50))
assert cor=={'XX':'-7/25','ZZ':'-7/25','XZ':'24/25','ZX':'-24/25'}
print('CHOI_EXACT pure; both marginals I/2; '+json.dumps(cor,sort_keys=True))

# Three simple countercontrols: the diamond, dephasing, and population-only R.
assert F(24,25)+F(7,25)==F(31,25)>1
assert F(9,25)**2+F(16,25)**2==F(337,625)!=F(49,625)
assert mm(mm(ZZ,M),ZZ)==adj(M)
print('COUNTERCONTROLS diamond L1=31/25; population/dephasing second read 337/625 != 49/625; ZRZ=R_inverse')

# Direct basis-permutation dilations preserve diagonal states. The target R|0>
# has off-diagonal 12/25 and X+ probability 49/50, versus 1/2 for any diagonal.
rho=mat([[9,12],[12,16]])
assert F(tr(mm(rho,X)),25)==F(24,25)
assert (1+F(24,25))/2==F(49,50)
assert F(49,50)-F(1,2)==F(12,25)
assert F(9,25).denominator & (F(9,25).denominator-1) != 0
print('BASIS_DILATION obstruction: minimum trace distance 12/25 (proof in report); binary uniform seeds cannot give unconditional 9/25 exactly')

def power(n):
    a,b=1,0
    for _ in range(abs(n)): a,b=3*a-4*b,4*a+3*b
    if n<0:b=-b
    d=5**abs(n)
    assert a*a+b*b==d*d
    return a,b,d
for n in range(1,101):
    a,b,d=power(n)
    assert a%5==3 and b%5==4
    assert F(a*a,d*d).denominator==25**n
print('UNIFORM_SEED_DENOMINATOR exact denominator 25^n for n=1..100; general modular proof in report')

theta=atan2(4,3)
bench=[]
for N in (10,100,1000):
    pick=lambda target:min(range(-N,N+1),key=lambda n:abs((n*theta-target+pi/2)%pi-pi/2))
    m,k=pick(pi/4),pick(pi/8)
    a,b,d=power(m); c,e,f=power(k)
    value=2*(F(c*c-e*e,f*f)+F(2*a*b,d*d)**2*F(2*c*e,f*f))
    assert value>2 and value*value<8
    with localcontext() as ctx:
        ctx.prec=30
        decimal=Decimal(value.numerator)/Decimal(value.denominator)
    bench.append({'search_bound':N,'m':m,'k':k,'CHSH':str(decimal),'exact_bounds':'2<S and S^2<8'})
print('BELL_BENCHMARK '+json.dumps(bench,sort_keys=True))
print('PASS: exact arithmetic except candidate selection for Bell powers; all reported probabilities and inequalities checked exactly.')
