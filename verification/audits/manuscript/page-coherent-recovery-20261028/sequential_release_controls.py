#!/usr/bin/env python3
"""Bounded exact checks of the clocked release permutation, not physical evaporation."""
from collections import Counter
from fractions import Fraction
import json

checks=0

def require(ok,label):
    global checks
    checks+=1
    if not ok:raise SystemExit('FAIL: '+label)

def step(state,n):
    t,x,y=state
    if t<n:
        d=((x>>t)^(y>>t))&1
        x^=d<<t;y^=d<<t
    return ((t+1)%(n+1),x,y)

def inverse(state,n):
    t,x,y=state;t=(t-1)%(n+1)
    if t<n:
        d=((x>>t)^(y>>t))&1
        x^=d<<t;y^=d<<t
    return t,x,y

def purity(states):
    # Direct amplitude contraction, tracing clock and X. All amplitudes 1/sqrt(N).
    rho=Counter()
    for t,x,y in states:
        for u,a,b in states:
            if (t,x)==(u,a):rho[y,b]+=1
    return Fraction(sum(z*z for z in rho.values()),len(states)**2)

def spaces(n):
    levels=[{(0,)}]
    for k in range(n):
        nxt=set()
        for v in levels[-1]:
            old=set(v)
            for x in range(1,1<<n):
                if x not in old:nxt.add(tuple(sorted(old|{x^y for y in v})))
        levels.append(nxt)
    return levels

basis_cases=0;window_cases=0
for n in range(1,5):
    whole=[(t,x,y) for t in range(n+1) for x in range(1<<n) for y in range(1<<n)]
    require(len({step(a,n) for a in whole})==len(whole),'configuration permutation')
    for a in whole:
        require(inverse(step(a,n),n)==a and step(inverse(a,n),n)==a,'two-sided inverse')
        z=a
        for _ in range(2*(n+1)):z=step(z,n)
        require(z==a,'full reversible period')
        basis_cases+=1
    for k,level in enumerate(spaces(n)):
        for v in sorted(level):
            state=[(0,x,0) for x in v]
            for r in range(n+1):
                mask=(1<<r)-1
                expected=sorted((r,x&~mask,x&mask) for x in v)
                require(sorted(state)==expected,'finite release window coordinate map')
                i=sum(x>>r==0 for x in v).bit_length()-1
                j=sum(x&mask==0 for x in v).bit_length()-1
                require(purity(state)==Fraction(1,1<<(k-i-j)),'direct trajectory reduced purity')
                if k in (0,n):require(purity(state)==1,'extreme-rank coherent/configuration control')
                state=[step(a,n) for a in state]
                window_cases+=1
            for _ in range(n+1):state=[step(a,n) for a in state]
            require(sorted(state)==[(0,x,0) for x in v],'later recoupling restores initial state')
    for k in range(n+1):
        state=[(0,x,0) for x in range(1<<k)]
        for r in range(n+1):
            require(purity(state)==1,'unmixed coherent product does not entangle')
            state=[step(a,n) for a in state]
    for x in range(1<<n):
        state=[(0,x,0)]
        for r in range(n+1):
            require(purity(state)==1,'every definite configuration stays unentangled')
            state=[step(a,n) for a in state]

for m in range(1,5):
    n=2*m
    v=tuple(sorted(sum(((x>>i)&1)*((1<<i)|(1<<(n-1-i))) for i in range(m)) for x in range(1<<m)))
    state=[(0,x,0) for x in v]
    for r in range(n+1):
        require(purity(state)==Fraction(1,1<<min(r,n-r)),'explicit mirror Bell release tent')
        state=[step(a,n) for a in state]

# Coherent clock plus coherent X: four equal-amplitude configurations.
coherent_clock=[(t,x,0) for t in (0,1) for x in (0,1)]
require(purity(coherent_clock)==1,'clock counterexample initially pure radiation')
after=[step(a,1) for a in coherent_clock]
require(purity(after)==Fraction(3,4),'coherent clock violates definite-clock conclusion')
print(json.dumps({'status':'PASS','explicit_predicates':checks,'basis_configurations':basis_cases,
 'coherent_state_window_cases':window_cases,'coherent_clock_counterexample_purity':str(purity(after)),
 'scope':'Autonomous finite release toy; no physical evaporation, energy law or derived scrambling.'},indent=2,sort_keys=True))
