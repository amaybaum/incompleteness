"""Exploratory exact checks of native acquisition and finite record lifetime.
Coordinate order: u0,...,u5,v0,...,v5. Standard library only.
"""
from collections import defaultdict, Counter

N = 6
EDGES = ((0,1),(1,2),(0,3),(1,4),(0,5),(2,5))
VISIBLE_U = (0,2,3,4,5)
CONSTRAINTS = (1<<9, 1<<10, 1<<5)  # v3=v4=u5=0
INITIAL = tuple(s for s in range(4096)
                if all((s&a).bit_count()%2 == 0 for a in CONSTRAINTS))

def step(s, edges=EDGES):
    u = [(s>>j)&1 for j in range(N)]
    v = [(s>>(j+N))&1 for j in range(N)]
    for a,b in edges:
        v[a] ^= u[b]
        v[b] ^= u[a]
    return sum(x<<i for i,x in enumerate(v+u))

def evolve(s,t):
    for _ in range(t):
        s = step(s)
    return s

def omega(a,b):
    return (((a&63)&(b>>6)).bit_count()+((a>>6)&(b&63)).bit_count())%2

def read(s,indices):
    return tuple((s>>j)&1 for j in indices)

def span(rows):
    s = {0}
    for r in rows:
        s |= {x^r for x in tuple(s)}
    return s

def pulled(t,mask):
    return sum(((evolve(1<<j,t)&mask).bit_count()%2)<<j for j in range(12))

assert len(INITIAL) == 512
assert len({step(s) for s in range(4096)}) == 4096
assert all(omega(step(1<<i),step(1<<j)) == omega(1<<i,1<<j)
           for i in range(12) for j in range(12))
assert all(omega(a,b)==0 for a in CONSTRAINTS for b in CONSTRAINTS)
period = next(t for t in range(1,100) if all(evolve(1<<j,t)==1<<j for j in range(12)))
assert period == 18
assert all(evolve(s,18)==s for s in range(4096))
print('One uniform product preparation on 512 states; bijective symplectic update; exact period 18.')

# The earlier correlated menu maps to the product menu in one native step.
oldA = (1<<3,1<<4,(1<<11)^1^4)
oldI = {s for s in range(4096) if all((s&a).bit_count()%2==0 for a in oldA)}
assert {step(s) for s in oldI} == set(INITIAL)
assert {evolve(s,17) for s in INITIAL} == oldI
print('Earlier correlated menu -> product menu in one step; reverse in 17 steps.')

changed = 0
for s in INITIAL:
    z = step(s)
    y = step(z)
    k = (z>>5)&1
    f = ((z>>0)^(z>>2))&1
    assert (z>>11)&1 == 0
    assert (y>>5)&1 == f == (y>>1)&1
    assert (y&1) == (((y>>7)&1)^k)
    assert (y>>11)&1 == k
    assert f == (((s>>3)^(s>>6)^(s>>8))&1)
    assert k == (((s>>0)^(s>>2)^(s>>11))&1)
    # Background subtraction at the identical pre-record state z.
    disconnected = step(z,EDGES[:-2])
    core_mask = 4095 ^ ((1<<5)|(1<<11))
    assert ((y^disconnected)&core_mask) == k*5
    changed += bool((y^disconnected)&core_mask)
assert changed == 256
print('Recording and decoder identities hold on every state; core kick in 256/512 cases.')

expected = {
    'native': (32,{2:32}),
    'read conjugate': (64,{1:64}),
    'cancel kick': (32,{1:32}),
    'disconnect final step': (16,{2:16}),
}
for mode, target in expected.items():
    branches = defaultdict(Counter)
    for s in INITIAL:
        z = step(s)
        y = step(z)
        if mode == 'cancel kick': y ^= ((z>>5)&1)*5
        if mode == 'disconnect final step': y = step(z,EDGES[:-2])
        indices = VISIBLE_U + ((11,) if mode=='read conjugate' else ())
        branches[read(y,indices)][read(y,(1,7))] += 1
    actual = (len(branches),dict(sorted(Counter(map(len,branches.values())).items())))
    assert actual == target
    assert all(len(set(c.values()))==1 for c in branches.values())
    print(mode+': record count, hidden-support histogram = '+str(actual))

def bad(s):
    return step(s)^(((s>>5)&1)*5)
failures = [(i,j) for i in range(12) for j in range(12)
            if omega(bad(1<<i),bad(1<<j)) != omega(1<<i,1<<j)]
assert len(failures)==4
print('Copy-with-cancelled-kick fails 4 symplectic basis-pair checks.')

frow = pulled(2,1<<5)
recoverable = []
print('time: hidden possibilities; stored-parity possibilities, for each record')
for t in range(18):
    hidden,parity = defaultdict(Counter),defaultdict(Counter)
    for s in INITIAL:
        y = evolve(s,t)
        rec = read(y,VISIBLE_U)
        hidden[rec][read(y,(1,7))] += 1
        parity[rec][(evolve(s,2)>>5)&1] += 1
    hs = sorted(set(map(len,hidden.values())))
    fs = sorted(set(map(len,parity.values())))
    assert len(hs)==len(fs)==1 and hs[0]>=2
    assert all(len(set(c.values()))==1 for c in parity.values())
    certified = frow in span(list(CONSTRAINTS)+[pulled(t,1<<i) for i in VISIBLE_U])
    assert certified == (fs == [1])
    if certified: recoverable.append(t)
    print(str(t)+': '+str(hs[0])+'; '+str(fs[0]))
assert recoverable == [1,2,11,15]
print('Stored parity recoverable exactly at times '+str(recoverable)+' modulo 18.')
print('PASS: exact enumeration and linear-span check agree. No external history used.')
