#!/usr/bin/env python3
"""Independent exact controls for record-fibre state identifiability.

No import from the author's checker, no floating-point arithmetic, and no
assert-based controls (normal/-O have the same predicates).
"""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import permutations, product
from math import gcd
from pathlib import Path
import hashlib
import json

checks = 0

def require(value, label):
    global checks
    checks += 1
    if not value:
        raise RuntimeError(label)

def records(p, r, s, length):
    word=[]
    for _ in range(length):
        word.append(r[s]);s=p[s]
    return tuple(word)

def period(p):
    unused=set(range(len(p)));answer=1
    while unused:
        start=next(iter(unused));s=start;length=0
        while s in unused:
            unused.remove(s);length+=1;s=p[s]
        require(s == start, 'permutation cycles close')
        answer=answer*length//gcd(answer,length)
    return answer

def partition(p,r,support,length):
    fibres=defaultdict(set)
    for s in support:
        fibres[records(p,r,s,length)].add(s)
    return frozenset(frozenset(x) for x in fibres.values())

def law(p,r,support,length):
    count=Counter(records(p,r,s,length) for s in support)
    return {w:Fraction(c,len(support)) for w,c in count.items()}

model_count=0;support_count=0
for n in range(1,5):
    for p in permutations(range(n)):
        full=period(p)
        for r in product(range(2),repeat=n):
            model_count+=1
            for mask in range(1,1<<n):
                support=[s for s in range(n) if mask>>s&1]
                support_count+=1
                # Full-period words are an independent oracle for all future
                # records. Compare directly to the N-1 deterministic bound.
                oracle=partition(p,r,support,full)
                finite=partition(p,r,support,max(1,n-1))
                require(finite==oracle,'N-1 records determine future classes')
                # Use a nonuniform prior; conditioning cannot resurrect a
                # zero-support state and every compatible positive mass stays.
                weights={s:s+1 for s in support}
                for cell in finite:
                    normalizer=sum(weights[s] for s in cell)
                    posterior={s:Fraction(weights[s],normalizer) for s in cell}
                    require(sum(posterior.values())==1,'posterior normalizes')
                    require(all(x>0 for x in posterior.values()),'fibre support retained')
                    require((max(posterior.values())==1)==(len(cell)==1),'posterior point identification')

# User's model, derived directly from bit coordinates.
states=list(product(range(2),repeat=2));index={s:i for i,s in enumerate(states)}
swap=tuple(index[(h,v)] for v,h in states);visible=tuple(v for v,h in states)
swap_rows=[]
for s,(v,h) in enumerate(states):
    w=records(swap,visible,s,3)
    require(w==(v,h,v),'swap three-record formula')
    require((w[0],w[1])==(v,h),'two records recover initial pair')
    current=states[swap[s]]
    require(current==(w[1],w[0]),'two records recover current pair')
    swap_rows.append({'initial':[v,h],'records':list(w),'current_after_one':list(current)})
require(len({tuple(x['records'][:2]) for x in swap_rows})==4,'all four two-record words distinct')
by_history=defaultdict(list)
for s in range(4):
    w=records(swap,visible,s,3);by_history[w[:2]].append(w[2])
require(set(by_history[(0,0)])=={0} and set(by_history[(1,0)])=={1},'C4 same-present/different-past next laws')
require(Counter(records(swap,visible,s,2) for s in range(4))=={(0,0):1,(0,1):1,(1,0):1,(1,1):1},'uniform past/current independent bits')

# Arbitrary-capacity counterfamily, with algebraic formula in the review note.
registers=[]
for m in range(1,7):
    xs=list(product(range(2),repeat=m+1));ids={x:i for i,x in enumerate(xs)}
    p=tuple(ids[x[1:]+x[:1]] for x in xs);r=tuple(x[0] for x in xs)
    words={records(p,r,s,m+1) for s in range(len(xs))}
    require(len(words)==len(xs),'register word map injective')
    for s,x in enumerate(xs):
        require(records(p,r,s,m+1)==x,'register all initial bits read')
        require(records(p,r,s,m+2)[-1]==x[0],'register C4 return X_(m+1)=X_0')
    same_present=defaultdict(set)
    for s,x in enumerate(xs):
        w=records(p,r,s,m+2);same_present[(w[m],w[0])].add(w[m+1])
    require(all(same_present[(cur,past)]=={past} for cur in range(2) for past in range(2)),'register memory after state inference')
    registers.append({'hidden_bits':m,'hidden_states':1<<m,'states':len(xs),'identifying_record_length':m+1,'conditional_memory_bits_at_t_m':1})

# A genuine persistent passive ambiguity, and its interface dependence.
xs=list(product(range(2),repeat=3));ids={x:i for i,x in enumerate(xs)}
p8=tuple(ids[(h,v,b)] for v,h,b in xs);r8=tuple(v for v,h,b in xs)
q8=partition(p8,r8,range(8),8)
require(len(q8)==4 and all(len(c)==2 for c in q8),'passive spectator class sizes')
for length in range(1,8):
    require(law(swap,visible,range(4),length)==law(p8,r8,range(8),length),'same visible law can hide microscopic fibres')
expanded=tuple((v,b) for v,h,b in xs)
require(all(len(c)==1 for c in partition(p8,expanded,range(8),2)),'expanded interface reads spectator')
# An explicit reversible intervention swaps hidden b into the visible slot.
action=tuple(ids[(b,h,v)] for v,h,b in xs)
require(r8[action[ids[(0,0,0)]]]!=r8[action[ids[(0,0,1)]]],'allowed intervention can separate passive-equivalent states')

# The global bound cannot be replaced by the size of a noninvariant support.
p4=(1,2,3,0);r4=(0,0,0,1);a=(0,1)
require(partition(p4,r4,a,2)==frozenset([frozenset(a)]),'two-support delayed separation')
require(all(len(c)==1 for c in partition(p4,r4,a,3)),'global N-1 bound survives')

# Current-state inference differs from initial inference without invertibility.
merge=tuple(index[(v,0)] for v,h in states)
cell={s for s in range(4) if records(merge,visible,s,2)==(0,0)}
require(len(cell)==2,'noninvertible initial ambiguity')
require({states[merge[s]][1] for s in cell}=={0},'noninvertible current hidden bit identified')

result={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'status':'PASS','checks':checks,'binary_readout_permutation_models':model_count,'nonempty_support_cases':support_count,'swap':swap_rows,'swap_conditional_memory_bits':1,'cyclic_register_controls':registers,'passive_spectator_quotient_states':len(q8),'passive_spectator_class_size':2,'model_and_interface_boundaries':['known model versus unknown microscopic family','support restriction','passive versus intervention records','whole-carrier bound versus support size','invertibility for current-state reconstruction','retained records versus instantaneous readout']}
print(json.dumps(result,indent=2,sort_keys=True))
