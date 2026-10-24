#!/usr/bin/env python3
"""Independent integer-coded coupled-front, cycle and geometry review."""
from collections import Counter
from functools import lru_cache
import argparse
import hashlib
from itertools import product
import json
from math import comb
from pathlib import Path

T=185; P=12*840**185; S=T+P; R=S+68; L=R+9
GEOMETRY_SHA='2642e1a68825faa5d3bb1049e8722adec1ec33bd3f56b9e4416b2c902a85ec5d'

def need(ok,label):
    if not ok: raise RuntimeError(label)
def h(v): return ((v&3)<<1)|(((v>>2)&1)^((v>>1)&v&1))
def iterate(v,n):
    for _ in range(n%12): v=h(v)
    return v
def encode(v): return 4*v[0]+2*v[1]+v[2]
def distance(a,b): return sum(abs(x-y) for x,y in zip(a,b))

@lru_cache(None)
def parity(a,b,c): return (comb(a+b+c,a)*comb(b+c,b))%2

def front(x,w,m):
    @lru_cache(None)
    def f(r,j,k):
        if r<0: return 0
        if j<0: return iterate(w,r+m-1+k) if parity(r,m-1,k) else 0
        if k<0: return iterate(2*x,r+j+m-1) if parity(r,j,m-1) else 0
        return h(f(r-1,j,k)^f(r,j-1,k)^f(r,j,k-1))
    return f

def response(f,r,j,k,deadline,payload):
    value=iterate(payload,deadline-r-1)
    for s in range(r+1): value=h(value^f(s,j-1,k)^f(s,j,k-1))
    return value

def direct(x,w,payload,old,m,r,j,k):
    end=(r,j,m+k); deadline=sum(end)
    sources={(0,0,0):2*x,(0,-m,m):w,(r-deadline,j,m+k):payload}
    @lru_cache(None)
    def at(t,p):
        if t==-1: return old if p==(0,0,0) else 0
        if t==0: return sources.get(p,0)
        if all(distance(p,s)>t for s in sources) and distance(p,(0,0,0))>t+1: return 0
        incoming=0
        for a in range(3):
            for step in (-1,1):
                q=list(p);q[a]+=step;incoming^=at(t-1,tuple(q))
        return at(t-2,p)^h(incoming)
    need(all(at(t,end)==0 for t in range(deadline)),'direct blank prefix')
    return at(deadline,end)

def run(root):
    raw=(root/'parallel_v3/history_control/SOURCE-GEOMETRY.json').read_bytes()
    need(hashlib.sha256(raw).hexdigest()==GEOMETRY_SHA,'source geometry hash')
    sources=json.loads(raw)['sources'];need(len(sources)==1479,'source census')
    expected_raw=(root/'layout_v10/results.json').read_bytes()
    need(hashlib.sha256(expected_raw).hexdigest()=='364b976b7a57cebd42081b7b269e380930abe33264fade4658f6222e345a9f83',
         'reviewed author expectation hash')
    author=json.loads(expected_raw)
    need(all(iterate(v,12)==v for v in range(8)),'local order bound')
    need(P%(384*840**176)==0,'actual period divides P')
    # Force parity is checked with multinomial coefficients, not bit tests.
    for r,j in product(range(11),range(384)):
        need(parity(r,j,75)==parity(r,j+384,75),'forcing period')
    ports=[((0,T,0),T,(0,-1,0)),((0,0,-8*T),T,(0,0,-1)),
           ((T,P,0),S,(0,1,0)),((-T,P,0),S,(0,1,0)),
           ((4*T,P,0),S,(0,1,0)),((0,S,0),S,(0,1,0)),((12*R,0,0),R,(-1,0,0))]
    additions=[(0,2*S,0),(T,S+P,0),(-T,S+P,0),(4*T,S+P,0),
               (0,S,S+136),(0,S,-S-136),(0,S,S+150),(0,S,S+152),(0,S,S+154)]
    endpoints=[(10,S-d,67+d) for d in range(11,25)]
    pulses=[(q[0]-L,q[1],q[2]) for q in endpoints]
    compared=0; ray_tests=0
    for q,pulse in zip(endpoints,pulses):
        need(distance(q,(0,0,0))==distance(q,(0,-76,76))==L,'two physical fronts')
        for source in sources:
            d=distance(q,source['position'])
            need(d==L if source['owner']=='input' else d>L,'all original source distances')
            compared+=1
        need(all(distance(q,s)>L for s in additions),'later sources excluded')
        for port,deadline,direction in ports:
            axis=next(i for i,v in enumerate(direction) if v)
            closest=max(deadline+1,min(L,(q[axis]-port[axis])*direction[axis]))
            point=tuple(p+closest*v for p,v in zip(port,direction))
            need(distance(point,q)>L,'entire frontier outside cone')
            need(distance(pulse,port)>deadline,'mask source preserves old deadline')
            ray_tests+=1
        need(distance(pulse,(0,S,76))>R+8,'earlier q8 untouched')
        need(pulse[0]<-T,'pulse cannot coincide with old bank')
        need(distance((q[0]+L,q[1],q[2]),(4*T,P,0))==S-401,'positive-x conflict')
        need(distance(q,(0,S,76))>1,'no late-q8 operand')
        need(all(distance(p,q)>L for p in pulses if p!=pulse),'all pulse cross-exclusions')
    fs=[front(x,7,76) for x in (0,1)]
    rows=[]
    for d in range(11,25):
        j=185-d;k=d-9
        maps=[[response(fs[x],10,j,k,L,b) for b in range(8)] for x in (0,1)]
        need(all(sorted(a)==list(range(8)) for a in maps),'native payload permutations')
        relative=[maps[0].index(v) for v in maps[1]]
        need(all(relative[relative[relative[i]]]==i for i in range(8)),'relative cube identity')
        counts=Counter();seen=set()
        for i in range(8):
            if i in seen: continue
            cur=i;length=0
            while cur not in seen:seen.add(cur);length+=1;cur=relative[cur]
            counts[length]+=1
        expected=author['census'][d-11]
        need(maps==[[encode(v) for v in a] for a in expected['payload_maps']],'all author payload rows')
        need([fs[x](10,j,k) for x in (0,1)]==[encode(v) for v in expected['uncontrolled_x_outputs']],
             'uncontrolled fronts')
        # Invariance under T^2 entails invariance under T because T=(T^2)^2.
        square=[relative[relative[i]] for i in range(8)]
        need(all(square[square[i]]==relative[i] for i in range(8)),'odd-order law implication')
        rows.append({'delta':d,'cycle_length_counts':dict(counts),'payload_maps':maps})
    scalar_cases=0; shortcut_mismatches=0
    for x,w,b,old in product((0,1),(0,7),range(8),(0,7)):
        m,r,j,k=2,1,2,1; deadline=r+j+m+k
        f=front(x,w,m); result=direct(x,w,b,old,m,r,j,k)
        need(result==response(f,r,j,k,deadline,b),'independent bounded six-neighbor recursion')
        scalar_cases+=1
        shortcut=h(iterate(f(r,j,k),11)^iterate(b,deadline-1))
        shortcut_mismatches+=shortcut!=result
    need(shortcut_mismatches>0,'reject final-tick surrogate')
    xor_perm=[i^1 for i in range(8)]
    need(sum(1 for i in range(8) if i<xor_perm[i] and xor_perm[xor_perm[i]]==i)==4,'positive two-cycle control')
    return {'schema':'oi-alternate-layout-independent-review-v1','verdict':'PASS',
            'original_source_tests':compared,'frontier_family_tests':ray_tests,
            'period_coordinates':176,'period_divisor':'384*840^176','endpoint_maps':rows,
            'independent_scalar_cases':scalar_cases,'shortcut_mismatches':shortcut_mismatches,
            'scope':'four-history full-raw-law obstruction for the stated 14-endpoint product family'}

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--source-root',type=Path,default=Path(__file__).resolve().parents[2])
    args=parser.parse_args();print(json.dumps(run(args.source_root),indent=2,sort_keys=True))
