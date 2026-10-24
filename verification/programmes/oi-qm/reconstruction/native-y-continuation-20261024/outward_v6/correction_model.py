"""Candidate q7 boundary source: full upper/C dipole, no pulse superposition."""
from functools import lru_cache
from itertools import product
from model import H,X,ZERO,indices,strip
DIPOLE_ROWS=tuple((u,c) for u in (0,1) for c in product((0,1),repeat=3))
FULL=(1<<len(DIPOLE_ROWS))-1
Q=(sum(u<<i for i,(u,c) in enumerate(DIPOLE_ROWS)),0,FULL)
C=tuple(sum(c[j]<<i for i,(u,c) in enumerate(DIPOLE_ROWS)) for j in range(3))
@lru_cache(None)
def direct(t,a,b,n):
 if t<0 or min(a+b+abs(n),a+b+abs(n+14))>t or (t-a-b-n)%2:return ZERO
 if t==0:return Q if (a,b,n)==(0,0,0) else C if (a,b,n)==(0,0,-14) else ZERO
 ns=[]
 for j in range(2):
  for sign in (-1,1):
   ab=[a,b];ab[j]+=sign;ab=sorted(map(abs,ab),reverse=True)
   ns.append(direct(t-1,*ab,n))
 ns.extend((direct(t-1,a,b,n-1),direct(t-1,a,b,n+1)))
 return X(direct(t-2,a,b,n),H(X(*ns)))

@lru_cache(None)
def dipole_strip():
 L=14;BASE=245;values={}
 def get(ell,a,b,n):
  if ell<0:return ZERO
  a,b=sorted((abs(a),abs(b)),reverse=True)
  if a+b>ell or (ell-a-b)%2 or ell+a+b>L:return ZERO
  return values[ell,a,b][n]
 for ell,a,b in indices(L):
  cap=BASE+(L-ell)//2;arr=[direct(ell,a,b,0)];values[ell,a,b]=arr
  for n in range(1,cap+1):
   trans=X(get(ell-1,a-1,b,n),get(ell-1,a+1,b,n),get(ell-1,a,b-1,n),get(ell-1,a,b+1,n))
   arr.append(X(get(ell-2,a,b,n),H(X(arr[n-1],get(ell-2,a,b,n+1),trans))))
 return values

def result():
 packed=dipole_strip()[14,0,0][245]
 tables=[]
 for u in (0,1):
  table=[tuple((w>>(8*u+c))&1 for w in packed) for c in range(8)]
  base=table[0];target=X(base,(u,0,u))
  matches=[DIPOLE_ROWS[8*u+c][1] for c,v in enumerate(table) if v==target]
  tables.append({'u':u,'table':table,'base':base,'target':target,'matches':matches})
 return tables

if __name__=='__main__':
 import json
 print(json.dumps(result()))
