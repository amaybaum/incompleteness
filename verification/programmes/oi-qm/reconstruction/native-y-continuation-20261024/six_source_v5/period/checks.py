"""Bounded checks for the exact giant-P reduction of the origin/M2 cluster."""
from functools import lru_cache
from itertools import product,permutations
from math import lcm
from strip import H,X,Z,indices,advance,inverse
T=185;P=12*840**T;S=T+P;R=S+68;N=S+71

def need(ok,msg):
 if not ok:raise RuntimeError(msg)

def dipole(x,m):
 sources={(0,0,0):(0,x,0),(0,-2,0):m}
 @lru_cache(None)
 def at(t,p):
  if t<0:return Z
  if min(sum(abs(a-b) for a,b in zip(p,q)) for q in sources)>t:return Z
  if t==0:return sources.get(p,Z)
  ns=[]
  for j in range(3):
   for s in (-1,1):
    q=list(p);q[j]+=s;ns.append(at(t-1,tuple(q)))
  return X(at(t-2,p),H(X(*ns)))
 return at

count=0
for x in (0,1):
 for m in product((0,1),repeat=3):
  at=dipole(x,m)
  state=tuple(at(ell,(a,0,b)) for ell,a,b in indices(6))
  for n in range(9):
   for (ell,a,b),v in zip(indices(6),state):
    need(v==at(n+ell,(a,n,b)),'dipole strip recurrence');count+=1
   state=advance(state,6)
print('PER1: %d direct dipole/strip comparisons; all16 x/M2 assignments, n0..8,13 entries: PASS'%count)

# A small full abstract strip permutation, not merely pulse-state tests.
keys=indices(2);states=list(product(tuple(product((0,1),repeat=3)),repeat=len(keys)))
image={st:advance(st,2) for st in states}
need(len(set(image.values()))==len(states),'whole strip permutation')
seen=set();periods=[]
for st in states:
 if st in seen:continue
 cur=st;k=0
 while cur not in seen:
  seen.add(cur);k+=1;cur=image[cur]
 need(cur==st,'permutation orbit')
 need((12*840**2)%k==0,'universal period divides bound')
 periods.append(k)
print('PER2: all%d abstract L2 states form a permutation; orbit lengths%s divide12*840^2: PASS'%(len(states),sorted(set(periods))))

need(lcm(*range(1,9))==840,'S8 exponent')
for perm in permutations(range(8)):
 seen=set()
 for i in range(8):
  if i in seen:continue
  j=i;length=0
  while j not in seen:seen.add(j);length+=1;j=perm[j]
  need(840%length==0,'permutation cycle exponent')
print('PER3: every one of40320 triple permutations has exponent dividing840: PASS')
for q in product((0,1),repeat=3):
 v=q
 for _ in range(12):v=H(v)
 need(v==q,'H exponent12')
need(P%(12*840**144)==0,'actual giantP has required divisibility')
print('PER4: H^12=id and actualP divisible by12*840^144: PASS')

# Enumerate the two finite local cross sections, keeping actual axial offsets.
counts=[]
for timeoffset,radius,maxweight in ((-1,72,142),(-2,71,140)):
 count=0;worst=0;minn=T
 for dx in range(-radius,radius+1):
  for dy in range(-radius+abs(dx),radius-abs(dx)+1):
   for dz in range(-radius+abs(dx)+abs(dy),radius-abs(dx)-abs(dy)+1):
    j=-1+dy;nprime=T+j;z=70+dz;ell=timeoffset-j
    # Ignore points beyond the cluster's leading cone, since both clusters vanish there.
    if ell<abs(dx)+abs(z) or (ell-abs(dx)-abs(z))%2:continue
    weight=ell+abs(dx)+abs(z)
    need(weight<=maxweight<=144,'strip budget')
    need(nprime>0,'reduced axial coordinate positive')
    # Leading lag from origin is 0 or2 throughout the relevant cone.
    lag=ell-abs(dx)-abs(z)
    need(lag in (0,2),'nearfront depth')
    count+=1;worst=max(worst,weight);minn=min(minn,nprime)
 counts.append((timeoffset,count,worst,minn))
print('PER5: exact preS slice budgets(offset,count,maxweight,minnprime)=%s: PASS'%counts)

# Retain the first actual interaction; isolated-superposition fails.
x=1;m=(0,0,1);at=dipole(x,m)
a=dipole(x,Z);b=dipole(0,m)
need(at(1,(0,-1,0))==H(X((0,x,0),m)),'first native collision')
need(at(1,(0,-1,0))!=X(a(1,(0,-1,0)),b(1,(0,-1,0))),'reject isolated pulse sum')
print('PER6: actual initial dipole interaction retained; isolated-pulse sum countercontrol fails at tick1: PASS')
print('SCOPE: exact period-reduction theorem and bounded controls; six-source endpoint not evaluated by this checker.')
