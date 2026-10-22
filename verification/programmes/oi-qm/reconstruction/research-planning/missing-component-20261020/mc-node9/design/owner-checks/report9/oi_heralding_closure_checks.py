"""Exact native heralding controls and a complete two-pair affine-state census.
Exploratory, read-only research. Standard Python 3 only.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations

def step(s,n,edges):
    u=[(s>>j)&1 for j in range(n)]
    v=[(s>>(n+j))&1 for j in range(n)]
    for a,b in edges: v[a]^=u[b];v[b]^=u[a]
    return sum(z<<j for j,z in enumerate(v+u))

def initial(n,clean):
    free=[j for j in range(2*n) if j not in clean]
    return [sum(((s>>k)&1)<<j for k,j in enumerate(free))
            for s in range(1<<len(free))]

def omega(a,b,n):
    low=(1<<n)-1
    return (((a&low)&(b>>n)).bit_count()+((a>>n)&(b&low)).bit_count())%2

def span(rows):
    out={0}
    for r in rows: out|={x^r for x in tuple(out)}
    return frozenset(out)

def posterior(counter):
    total=sum(counter.values())
    return {k:Fraction(v,total) for k,v in sorted(counter.items())}

print('EXPLORATORY DESIGN EVIDENCE; no repository changes or independent review.')
print('FOUR-SITE NATIVE HERALD: edge (0,1), two isolated coins.')
n=4;edges=((0,1),);clean=(4,5,2,3);I=initial(n,clean)
assert len(I)==16
assert all(omega(1<<a,1<<b,n)==0 for a in clean for b in clean)
accepted=[];fine=defaultdict(Counter);coarse=Counter()
for s in I:
    y=step(s,n,edges)
    q,Q,c,d=(s>>0)&1,(s>>1)&1,(s>>6)&1,(s>>7)&1
    assert (y&1,(y>>4)&1,(y>>1)&1,(y>>5)&1)==(Q,q,q,Q)
    rec=((y>>1)&1,(y>>2)&1,(y>>3)&1)
    assert rec==(q,c,d)
    target=(y&1,(y>>4)&1)
    fine[rec][target]+=1
    if q==0 or (c,d)==(0,0):
        accepted.append((s,y));coarse[target]+=1
assert len(accepted)==10
assert all(sorted(c.values())==[1,1] for c in fine.values())
assert coarse==Counter({(0,0):4,(1,0):4,(0,1):1,(1,1):1})
print('Success=5/8; post-herald target distribution:',posterior(coarse))
print('Every exact record leaves a uniform two-point target; coarse herald gives an 4/5 : 1/5 mixture of two such states.')

# The symmetric edge supplies both the record and its disturbance.
for s in I:
    coupled=step(s,n,edges);uncoupled=step(s,n,())
    assert (coupled^uncoupled)&((1<<0)|(1<<4))==((s>>1)&1)
print('Background subtraction: hidden u receives initial pointer u; hidden v is unchanged relative to no edge.')

# Deliberate failure: keep the acceptance flag outside the physical model.
late=Counter();flag_by_record=defaultdict(Counter)
selected={s for s,_ in accepted}
for s in I:
    y=s
    for _ in range(6): y=step(y,n,edges)
    assert y==s
    rec=tuple((y>>j)&1 for j in (1,2,3))
    flag_by_record[rec][s in selected]+=1
    if s in selected: late[(y&1,(y>>4)&1)]+=1
assert late==Counter({(0,0):8,(1,0):2})
assert all(c==Counter({True:5,False:3}) for c in flag_by_record.values())
print('External-history countercontrol at t=6:',posterior(late))
print('At t=6 each visible position record has 5 accepted and 3 rejected histories: no physical herald flag remains in this readout.')

# Keep the earlier source bit physically available at the terminal cut instead.
print('NINE-SITE EMBEDDED RETENTION: path 0--1--...--6; isolated coins 7,8.')
n=9;edges=tuple((j,j+1) for j in range(6))
clean=[n]+[n+j if j%2 else j for j in range(1,7)]+[n+7,n+8]
I=initial(n,clean);assert len(I)==512
assert all(omega(1<<a,1<<b,n)==0 for a in clean for b in clean)
coarse=Counter();fine=defaultdict(Counter);accept_count=0
for s in I:
    y=s
    for _ in range(6): y=step(y,n,edges)
    q=(s&1);c=(s>>7)&1;d=(s>>8)&1
    assert ((y>>6)&1)==q
    assert ((y>>7)&1,(y>>8)&1)==(c,d)
    assert (y&1)==0
    target=(y&1,(y>>n)&1)
    # Stronger check: use every visible position, not only the herald bits.
    rec=tuple((y>>j)&1 for j in range(1,n))
    fine[rec][target]+=1
    if q==0 or (c,d)==(0,0):
        coarse[target]+=1;accept_count+=1
assert accept_count==320
assert coarse==Counter({(0,0):160,(0,1):160})
assert all(len(c)==2 and len(set(c.values()))==1 for c in fine.values())
print('Success=5/8; source q retained in u6(6); accepted target:',posterior(coarse))
print('Every complete terminal position record leaves two equally likely target states.')

# Exhaust all uniform affine isotropic states of two canonical pairs.
n=2
subspaces={span(())}
subspaces|={span((a,)) for a in range(1,16)}
subspaces|={span((a,b)) for a,b in combinations(range(1,16),2) if omega(a,b,n)==0}
assert len(subspaces)==31
supports=set()
for A in subspaces:
    for s in range(16):
        support=frozenset(x for x in range(16)
                          if all(((x^s)&a).bit_count()%2==0 for a in A))
        supports.add(support)
assert len(supports)==91
outcomes=Counter();checked=0
for support in supports:
    for kept in ({0},{1},{0,1}):
        selected=[x for x in support if ((x>>1)&1) in kept]
        if not selected: continue
        out=Counter((x&1,(x>>2)&1) for x in selected)
        assert max(Fraction(v,len(selected)) for v in out.values())<=Fraction(1,2)
        assert len(out) in (2,4) and len(set(out.values()))==1
        outcomes[len(out)]+=1;checked+=1
print('Two-pair closure census: 31 isotropic constraint subspaces, 91 distinct affine states.')
print(f'All {checked} nonempty herald events pass; target support histogram={dict(sorted(outcomes.items()))}.')

# Exact one-pair convex characterization: p_x<=1/2, p_x>=0, sum p_x=1.
# Its vertices are uniform on two of four points; all such pairs are affine lines.
for a,b in combinations(range(4),2):
    assert len({a,b})==2
    difference=a^b
    normal=next(r for r in range(1,4) if (difference&r).bit_count()%2==0)
    assert {(x) for x in range(4) if ((x^a)&normal).bit_count()%2==0}=={a,b}
assert max(posterior(Counter({0:4,1:4,2:1,3:1})).values())<=Fraction(1,2)
assert max(posterior(Counter({0:8,1:2})).values())>Fraction(1,2)
print('Allowed coarse state has maximum point probability 2/5; free-history state has 4/5 and fails the one-pair convex bound.')
print('PASS: all exact native enumerations, herald probabilities, retained-record controls, and affine closure checks.')
