"""Exact radial-strip recurrence for a lone pulse in the native cubic update."""
from functools import lru_cache
from itertools import product
Z=(0,0,0)
def H(v):a,b,d=v;return b,d,a^(b&d)
def X(*vs):return tuple(sum(v[i] for v in vs)%2 for i in range(3))
@lru_cache(None)
def indices(L,maxl=None):
 if maxl is None:maxl=L
 return tuple((l,a,b) for l in range(maxl+1) for a in range(l+1) for b in range(a+1) if a+b<=l and a+b+l<=L and (l-a-b)%2==0)

def direct(q):
 @lru_cache(None)
 def at(t,p):
  if t<0 or sum(map(abs,p))>t:return Z
  if t==0:return q if p==(0,0,0) else Z
  return X(at(t-2,p),H(X(*(at(t-1,tuple(p[i]+(s if i==j else 0) for i in range(3))) for j in range(3) for s in (-1,1)))))
 return at

def initial(q,L):
 at=direct(q)
 return tuple(at(l,(a,b,0)) for l,a,b in indices(L))

def advance(state,L,maxl=None):
 keys=indices(L,maxl)
 old=dict(zip(keys,state));new={};future_layers={}
 def val(tab,l,a,b):
  a,b=sorted((abs(a),abs(b)),reverse=True)
  return tab.get((l,a,b),Z)
 for l,a,b in keys:
  future=Z
  if l>=2:
   # Future lower-layer strip is determined before this layer.
   if l not in future_layers:
    smaller_keys=indices(L,l-2)
    smaller=advance(tuple(new[k] for k in smaller_keys),L,l-2)
    future_layers[l]=dict(zip(smaller_keys,smaller))
   future=future_layers[l].get((l-2,a,b),Z)
  trans=X(val(new,l-1,a-1,b),val(new,l-1,a+1,b),val(new,l-1,a,b-1),val(new,l-1,a,b+1))
  new[l,a,b]=X(val(new,l-2,a,b),H(X(old[l,a,b],future,trans)))
 return tuple(new[k] for k in keys)

if __name__=='__main__':
 for L in (4,6):
  print('L',L,'indices',len(indices(L)),flush=True)
  for u in (0,1):
   q=(u,0,1);s=initial(q,L);start=s
   for n in range(1,200001):
    s=advance(s,L)
    if s==start:break
   print('u',u,'period',n,'returned',s==start,flush=True)

def inverse(newstate,L,maxl=None):
 keys=indices(L,maxl);new=dict(zip(keys,newstate));old={};future_layers={}
 def val(tab,l,a,b):
  a,b=sorted((abs(a),abs(b)),reverse=True)
  return tab.get((l,a,b),Z)
 def ih(v):a,b,d=v;return d^(a&b),a,b
 for l,a,b in keys:
  future=Z
  if l>=2:
   if l not in future_layers:
    kk=indices(L,l-2)
    future_layers[l]=dict(zip(kk,advance(tuple(new[k] for k in kk),L,l-2)))
   future=future_layers[l].get((l-2,a,b),Z)
  trans=X(val(new,l-1,a-1,b),val(new,l-1,a+1,b),val(new,l-1,a,b-1),val(new,l-1,a,b+1))
  old[l,a,b]=X(ih(X(new[l,a,b],val(new,l-2,a,b))),future,trans)
 return tuple(old[k] for k in keys)
