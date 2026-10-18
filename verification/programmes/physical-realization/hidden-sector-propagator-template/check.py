"""Exact projected-memory template, checked against direct state-index evolution.

Recipe: python3 -I -B check.py | cmp - output.json  (never -O; checks do not use assert).
A failed check prints its name to stderr and exits with status 1.
"""
from fractions import Fraction as F
from itertools import permutations
import json
import sys

count = 0
def check(condition, name='check'):
    global count
    if not condition:
        print(f'CHECK FAILED: {name}', file=sys.stderr)
        sys.exit(1)
    count += 1

class InvalidPremise(Exception):
    pass

def premise(condition, name):
    if not condition:
        raise InvalidPremise(name)

countercontrols = []
def reject(name, rejected):
    # A countercontrol runs a corrupted input through a real check; it passes only if rejected.
    check(rejected, f'countercontrol accepted: {name}')
    countercontrols.append(name)

def mm(a, b):
    return [[sum((x*y for x,y in zip(row,col)),F()) for col in zip(*b)] for row in a]
def mv(a, v):
    return [sum((x*y for x,y in zip(row,v)),F()) for row in a]
def add(a, b):
    return [x+y for x,y in zip(a,b)]
def sub(a, b):
    return [x-y for x,y in zip(a,b)]
def eye(n):
    return [[F(i==j) for j in range(n)] for i in range(n)]
def mpow(a, n):
    out=eye(len(a))
    for _ in range(n): out=mm(a,out)
    return out

def construct(phi, labels, pi):
    n=len(phi); m=max(labels)+1
    premise(sorted(phi)==list(range(n)), 'bijection')
    premise(set(labels)==set(range(m)), 'surjective partition')
    premise(all(x>0 for x in pi) and sum(pi)==1, 'positive law')
    premise(all(pi[phi[i]]==pi[i] for i in range(n)), 'stationary prior')
    p=[[F(labels[i]==a) for i in range(n)] for a in range(m)]
    q=mv(p,pi)
    r=[[pi[i]/q[a] if labels[i]==a else F() for a in range(m)] for i in range(n)]
    u=[[F(phi[j]==i) for j in range(n)] for i in range(n)]
    d=mm(r,p); identity=eye(n)
    hidden=[[identity[i][j]-d[i][j] for j in range(n)] for i in range(n)]
    a=mm(mm(p,u),r); b=mm(p,u)
    c=mm(mm(hidden,u),r); e=mm(mm(hidden,u),hidden)
    return p,r,u,hidden,a,b,c,e,q

def direct(phi, labels, rho):
    # Independent index route: no matrix pushforward or lift is used.
    out=[F() for _ in range(max(labels)+1)]
    for i,weight in enumerate(rho): out[labels[i]]+=weight
    nxt=[F() for _ in rho]
    for i,weight in enumerate(rho): nxt[phi[i]]+=weight
    return out,nxt

def recurrence(phi, labels, blocks, rho0, steps=9, memory=True, hidden_start=True):
    # Per step: projection matches the index route; projected recurrence matches the
    # direct next projection; the next projection is a probability law.
    p,r,u,qproj,a,b,c,e,_=blocks
    eta0=mv(qproj,rho0) if hidden_start else [F() for _ in rho0]
    rho=rho0[:]; history=[]; results=[]
    for t in range(steps):
        current,next_rho=direct(phi,labels,rho)
        results.append(current==mv(p,rho)); history.append(current)
        predicted=add(mv(a,current),mv(b,mv(mpow(e,t),eta0)))
        if memory:
            for j in range(t):
                predicted=add(predicted,mv(b,mv(mpow(e,t-1-j),mv(c,history[j]))))
        expected,_=direct(phi,labels,next_rho)
        results.append(predicted==expected)
        results.append(sum(expected)==1 and all(x>=0 for x in expected))
        rho=next_rho
    return results

def premise_rejected(phi, labels, pi):
    try: construct(phi,labels,pi)
    except InvalidPremise: return True
    return False

cases=0
for n in (3,4):
    partitions=([(0,0,1),(0,1,1)] if n==3 else
                [(0,0,1,1),(0,1,0,1),(0,1,2,2)])
    for phi in permutations(range(n)):
        # A nonuniform stationary law, constant on each permutation cycle.
        weights=[None]*n
        for i in range(n):
            if weights[i] is not None: continue
            j=i
            while weights[j] is None:
                weights[j]=i+1; j=phi[j]
        pi=[F(x,sum(weights)) for x in weights]
        for labels in partitions:
            blocks=construct(phi,labels,pi)
            p,r,u,qproj,a,b,c,e,reference=blocks
            m=len(p)
            check(mm(p,r)==eye(m)); check(mm(qproj,qproj)==qproj)
            check(mv(a,reference)==reference)
            check(all(x>=0 for row in a for x in row))
            check(all(sum(a[i][j] for i in range(m))==1 for j in range(m)))
            initial=[pi]+[[F(i==j) for i in range(n)] for j in range(n)]
            initial.append(mv(r,[F(i==0) for i in range(m)]))
            for rho0 in initial:
                for ok in recurrence(phi,labels,blocks,rho0):
                    check(ok,'projected recurrence')
                cases+=1

phi=(1,2,3,0); labels=(0,0,1,1); pi=[F(1,4)]*4
cycle_blocks=construct(phi,labels,pi)
p,r,u,qproj,a,b,c,e,_=cycle_blocks
macro=[F(1),F()]; rho=mv(r,macro)
series=[]
for _ in range(5):
    observed,rho=direct(phi,labels,rho); series.append(observed)
check(series==[[F(1),F()],[F(1,2),F(1,2)],[F(),F(1)],
               [F(1,2),F(1,2)],[F(1),F()]])
check(mv(mpow(a,2),macro)!=series[2])  # Omitted memory despite equilibrated lift.
point=[F(1),F(),F(),F()]
current,nxt=direct(phi,labels,point)
check(mv(a,current)!=direct(phi,labels,nxt)[0])  # Omitted initial hidden deviation.
other=[F(),F(1),F(),F()]
check(direct(phi,labels,point)[0]==direct(phi,labels,other)[0])
check(direct(phi,labels,direct(phi,labels,point)[1])[0]!=
      direct(phi,labels,direct(phi,labels,other)[1])[0])
# Countercontrols: corrupted inputs through the same recurrence and premise checks.
lifted=mv(r,macro)
check(all(recurrence(phi,labels,cycle_blocks,lifted)), 'four-cycle lifted recurrence')
reject('memory terms omitted (four-cycle, lifted law)',
       not all(recurrence(phi,labels,cycle_blocks,lifted,memory=False)))
check(all(recurrence(phi,labels,cycle_blocks,point)), 'four-cycle point-mass recurrence')
reject('initial hidden term omitted (four-cycle, point mass)',
       not all(recurrence(phi,labels,cycle_blocks,point,hidden_start=False)))
reject('non-bijective update', premise_rejected((1,1,3,0),labels,pi))
reject('non-surjective partition', premise_rejected(phi,(0,0,2,2),pi))
reject('non-stationary prior', premise_rejected(phi,labels,[F(1,2),F(1,6),F(1,6),F(1,6)]))

# Main §2.4: literal visible x in {0,1}, hidden h in {1,...,6}.
source_phi=[]
for x in range(2):
    for h in range(6):
        source_phi.append((1-x)*6+h if h<2 else x*6+(h^1))
source_labels=tuple(i//6 for i in range(12))
source_blocks=construct(source_phi,source_labels,[F(1,12)]*12)
sp,sr,su,sq,sa,sb,sc,se,_=source_blocks
check(all(source_phi[source_phi[i]]==i for i in range(12)))
check(sa==[[F(2,3),F(1,3)],[F(1,3),F(2,3)]])
source_k2=mm(mm(sp,mpow(su,2)),sr)
check(source_k2==eye(2))
check(source_k2!=mm(sa,sa))
source_bc=mm(sb,sc)
check(source_bc==[[F(4,9),F(-4,9)],[F(-4,9),F(4,9)]])
epower=eye(12)
for j in range(8):
    kernel=mm(mm(sb,epower),sc)
    check(kernel==[[F(-1,3)**j*x for x in row] for row in source_bc])
    epower=mm(se,epower)
for i in range(12):
    point=[F(i==j) for j in range(12)]
    observed,nxt=direct(source_phi,source_labels,point)
    check(mv(sp,mv(su,point))==direct(source_phi,source_labels,nxt)[0])
# The full recurrence on Main §2.4 from every point state and both lifted macro laws.
source_initial=[[F(i==j) for j in range(12)] for i in range(12)]
source_initial+=[mv(sr,[F(1),F()]),mv(sr,[F(),F(1)])]
for rho0 in source_initial:
    for ok in recurrence(source_phi,source_labels,source_blocks,rho0):
        check(ok,'Main 2.4 recurrence')
# Countercontrol: the memory kernel with ratio +1/3 (E replaced by -E) on the lifted law.
flipped=(sp,sr,su,sq,sa,sb,sc,[[-x for x in row] for row in se],None)
reject('Main 2.4 memory kernel with ratio +1/3',
       not all(recurrence(source_phi,source_labels,flipped,source_initial[12])))
print(json.dumps({'checks':count,'cases':cases,'countercontrols':len(countercontrols),
                  'countercontrols_rejected':countercontrols,
                  'four_cycle':[[str(x) for x in row] for row in series],
                  'Main_2_4_A':[[str(x) for x in row] for row in sa],
                  'Main_2_4_memory_0':[[str(x) for x in row] for row in source_bc],
                  'scope':'exact conditional projected-memory template; physical model inputs OPEN'},
                 indent=2,sort_keys=True))
