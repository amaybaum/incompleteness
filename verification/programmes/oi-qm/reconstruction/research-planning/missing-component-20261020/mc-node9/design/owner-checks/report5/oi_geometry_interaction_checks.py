#!/usr/bin/env python3
"""Exact calibration of state geometry, tomography and interaction.
Standalone, standard library; no repository writes or quantum reconstruction.
All matrices used below are real rational, including Y tensor Y.
"""
from fractions import Fraction as F
from itertools import product
import json

def emit(label, obj):
    print(label + ' ' + json.dumps(obj, sort_keys=True))
def scale(t,a): return [[t*x for x in row] for row in a]
def add(a,b): return [[x+y for x,y in zip(r,s)] for r,s in zip(a,b)]
def mm(a,b): return [[sum(x*y for x,y in zip(r,c)) for c in zip(*b)] for r in a]
def tr(a): return sum(a[i][i] for i in range(len(a)))
def tp(a): return [list(r) for r in zip(*a)]
def kron(a,b):
    return [[a[i][j]*b[k][l] for j in range(len(a[0])) for l in range(len(b[0]))]
            for i in range(len(a)) for k in range(len(b))]
def flat(a): return [x for r in a for x in r]
def rank(rows):
    rows=[[F(x) for x in r] for r in rows]; n=0
    for j in range(len(rows[0])):
        p=next((i for i in range(n,len(rows)) if rows[i][j]),None)
        if p is None: continue
        rows[n],rows[p]=rows[p],rows[n]; v=rows[n][j]
        rows[n]=[x/v for x in rows[n]]
        for i in range(len(rows)):
            if i!=n:
                v=rows[i][j]; rows[i]=[x-v*y for x,y in zip(rows[i],rows[n])]
        n+=1
        if n==len(rows): break
    return n
def conj(u,a): return mm(mm(u,a),tp(u))
def expect(a,e): return tr(mm(a,e))
def ptb(a):
    return [[a[2*i+l][2*k+j] for k in range(2) for l in range(2)]
            for i in range(2) for j in range(2)]

I=[[1,0],[0,1]]; X=[[0,1],[1,0]]; Z=[[1,0],[0,-1]]
J=[[0,-1],[1,0]]
II=kron(I,I); XX=kron(X,X); ZZ=kron(Z,Z)
YY=scale(-1,kron(J,J)) # Y=iJ, so Y tensor Y=-J tensor J.
C=[[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]]
XZ=kron(X,Z)
assert mm(C,C)==II and conj(C,YY)==scale(-1,XZ)

# Two positive, real joint states invisible to ALL product rebit effects.
rp=scale(F(1,4),add(II,YY)); rm=scale(F(1,4),add(II,scale(-1,YY)))
for r in [rp,rm]:
    assert tp(r)==r and tr(r)==1
    assert mm(r,r)==scale(F(1,2),r) # eigenvalues 0 or 1/2 => PSD.
product_basis=[kron(a,b) for a,b in product([I,X,Z],repeat=2)]
assert rank([flat(a) for a in product_basis])==9
assert rank([flat(a) for a in product_basis]+[flat(YY)])==10
assert all(expect(rp,e)==expect(rm,e) for e in product_basis)
diff=add(rp,scale(-1,rm))
assert expect(conj(C,diff),XZ)==-2
ep=scale(F(1,2),add(I,X)); ez=scale(F(1,2),add(I,Z))
pplus=expect(conj(C,rp),kron(ep,ez))
pminus=expect(conj(C,rm),kron(ep,ez))
assert (pplus,pminus)==(0,F(1,2))
emit('REBIT_QUOTIENT_FAILURE',{'product_effect_rank':9,'full_real_symmetric_rank':10,
 'equal_on_entire_product_effect_span':True,'CNOT_YY_image':'-XZ',
 'after_CNOT_XZ_expectations':['-1','1'],
 'after_CNOT_plusX_plusZ_probabilities':[str(pplus),str(pminus)],
 'interpretation':'same local product table is not same full joint operational state'})

# Connected reversible interaction: U(theta)=exp(theta J tensor X).
# Its rational point c=3/5,s=4/5 avoids any reliance on disconnected CNOT.
A=kron(J,X)
assert tp(A)==scale(-1,A) and mm(A,A)==scale(-1,II)
U=add(scale(F(3,5),II),scale(F(4,5),A))
assert mm(U,tp(U))==II
assert conj(U,YY)==add(scale(F(-7,25),YY),scale(F(24,25),kron(I,Z)))
up=expect(conj(U,rp),kron(I,ez)); um=expect(conj(U,rm),kron(I,ez))
assert (up,um)==(F(49,50),F(1,50))
common=(up+um)/2
assert max(abs(up-common),abs(um-common))==F(12,25)
evolved_effects=[conj(tp(U),e) for e in product_basis]
assert rank([flat(e) for e in product_basis+evolved_effects])==10
emit('CONNECTED_REAL_INTERACTION',{'U':'(3 I + 4 (J tensor X))/5',
 'continuous_path':'exp(theta J tensor X)',
 'plusZ_B_probabilities':[str(up),str(um)],
 'probability_gap':str(up-um),'effect_span_growth':[9,10],
 'best_common_prediction_error':'12/25',
 'scope':'real quantum theory permits interaction by retaining its holistic coordinate'})

# Erasing the missing coordinate from a Bell state is not a valid repair.
bell=scale(F(1,4),add(add(add(II,XX),ZZ),scale(-1,YY)))
assert mm(bell,bell)==bell and tr(bell)==1
truncated=scale(F(1,4),add(add(II,XX),ZZ))
exminus=scale(F(1,2),add(I,scale(-1,X)))
ezminus=scale(F(1,2),add(I,scale(-1,Z)))
neg=expect(conj(C,truncated),kron(exminus,ezminus))
assert neg==F(-1,4)
emit('ERASED_CORRELATION_MUTANT',{'state':'(II+XX+ZZ)/4',
 'after_CNOT_minusX_minusZ_probability':str(neg),
 'scope':'naive rebit product-table truncation, not every possible disc theory'})

# Qubit maximal-product cone has positive-on-products non-PSD tables.
# W=SWAP/2 is the partial transpose of a Bell density matrix.
W=scale(F(1,4),add(add(add(II,XX),YY),ZZ))
assert W==ptb(bell)
singlet=[[0,0,0,0],[0,F(1,2),F(-1,2),0],
         [0,F(-1,2),F(1,2),0],[0,0,0,0]]
assert expect(W,singlet)==F(-1,2)
assert conj(C,singlet)==kron(exminus,ezminus)
assert expect(conj(C,W),kron(exminus,ezminus))==F(-1,2)
# For every pure complex product |a,b>, <a,b|W|a,b>=|<a|b>|^2/2 >=0.
# Exact rational directions check the equivalent formula (1+a.b)/4.
dirs={(F(1),F(0),F(0)),(F(-1),F(0),F(0))}
for k in range(-5,6):
    t=F(k,5); u=2*t/(1+t*t); v=(1-t*t)/(1+t*t)
    for d in [(u,v,F(0)),(u,F(0),v),(F(0),u,v)]: dirs.add(d)
count=0
for a,b in product(sorted(dirs),repeat=2):
    assert sum(x*x for x in a)==sum(x*x for x in b)==1
    p=(1+sum(x*y for x,y in zip(a,b)))/4
    assert 0<=p<=1; count+=1
# Consistently transpose both states and transformations: no contradiction.
twisted_output=ptb(conj(C,ptb(W)))
assert twisted_output==kron(ep,ez)
assert expect(twisted_output,kron(exminus,ezminus))==0
emit('PRODUCT_POSITIVITY_IS_NOT_GATE_VALIDITY',{'W':'SWAP/2',
 'rational_product_direction_pairs':count,
 'all_product_positivity_proof':'squared product-vector overlap / 2',
 'ordinary_CNOT_then_minusX_minusZ_probability':'-1/2',
 'consistently_twisted_CNOT_same_probability':'0',
 'scope':'forbidden with fixed standard gate lift; not a representation-independent rejection'})

# Minimal product cone cannot support the entangling gate either.
pluszero=kron(ep,ez)
assert conj(C,pluszero)==bell
# Product qubit states obey XX+ZZ <= 1 by Cauchy-Schwarz; mixtures inherit it.
assert expect(bell,add(XX,ZZ))==2
emit('MINIMAL_PRODUCT_CONE_FAILURE',{'CNOT_input':'|+0>',
 'CNOT_output':'Bell Phi+', 'XX_plus_ZZ_on_output':'2',
 'separable_bound':'1', 'all_product_bound_proof':'Cauchy-Schwarz, then convexity'})

# Lie closure of local Pauli Hamiltonians and one ZZ interaction.
# Nonzero commutators of distinct Pauli strings are scalar multiples
# of another Pauli string; phases irrelevant for real Lie-span membership.
bits={'I':(0,0),'X':(1,0),'Y':(1,1),'Z':(0,1)}
rev={v:k for k,v in bits.items()}
def bracket_label(a,b):
    anti=sum(bits[x][0]*bits[y][1]+bits[x][1]*bits[y][0]
             for x,y in zip(a,b))%2
    if not anti:return None
    return ''.join(rev[(bits[x][0]^bits[y][0],bits[x][1]^bits[y][1])]
                   for x,y in zip(a,b))
def lie_closure(seeds):
    s=set(seeds);sizes=[len(s)]
    while True:
        t=s|{v for a,b in product(s,repeat=2) if (v:=bracket_label(a,b))}
        if t==s:return s,sizes
        s=t;sizes.append(len(s))
local=['XI','YI','ZI','IX','IY','IZ']
ls,lh=lie_closure(local); full,fh=lie_closure(local+['ZZ'])
assert len(ls)==6 and full=={a+b for a,b in product('IXYZ',repeat=2)}-{'II'}
emit('QUANTUM_INTERACTION_CALIBRATION',{'local_Lie_dimension':len(ls),
 'local_plus_ZZ_Lie_dimension':len(full),'growth':fh,
 'scope':'assumed complex quantum representation and continuous controls'})

# Randomly selecting classical identity or CNOT gives a continuous path of
# stochastic maps, but its midpoint loses information and is not reversible.
mid=scale(F(1,2),add(II,C))
assert rank(mid)==3
assert [mid[i][2] for i in range(4)]==[mid[i][3] for i in range(4)]
emit('CONTINUITY_WITHOUT_REVERSIBILITY_MUTANT',{'map':'(identity+CNOT)/2',
 'rank':rank(mid),'merged_inputs':['10','11'],
 'scope':'a stochastic interpolation is not a continuous reversible control'})
emit('VERDICT',{'exact_checks':'PASS','OI_geometry_derived':False,
 'classification_theorem_reproved':False,'status':'exploratory calibration'})
