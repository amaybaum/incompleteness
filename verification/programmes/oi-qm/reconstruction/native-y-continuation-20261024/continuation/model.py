from core import *
from pathlib import Path
import json
D=json.loads(Path('continuation/patterns.json').read_text());basis=[int(v,16) for v in D['basis']]
T=185;P=12*840**T;S=T+P;d=68;R=S+d;end=(0,0,2)
N=1<<len(basis);ALL=(1<<N)-1
# Truth-table variable: bit lane m evaluates the source-selection bits of m.
variables=[]
for i in range(len(basis)):
 k=1<<i;variables.append(((1<<k)-1)<<k)
 variables[-1]*=ALL//((1<<(2*k))-1)
slots=[(R-2,v) for v in ball(2,end)]+[(R-1,v) for v in ball(3,end)]
perturb={}
for j,slot in enumerate(slots):
 w=0
 for p,var in zip(basis,variables):
  if p>>j&1:w^=var
 perturb[slot]=w

def bx(*vs):return tuple(__import__('functools').reduce(int.__xor__,(v[i] for v in vs),0) for i in range(3))
def bh(v):a,b,c=v;return b,c,a^(b&c)
def calc(x,u,my=0,mr=0,p=None):
 controls=[((0,-S,-d),x),((0,S,-d),my^mr),((T,P,-d),my),((-T,P,-d),mr)]
 def base(t,v):
  val=upper((u,0,1),t,(v[0],v[1],R-v[2]))
  for loc,bit in controls:
   ds=tuple(abs(a-b) for a,b in zip(v,loc))
   if sum(ds)==t and odd(ds):val=X(val,hp((0,bit,0),t))
  out=[ALL*b for b in val]
  for i,b in enumerate(hp((0,1,0),t)):
   if b:out[i]^=perturb[t,v]
  return tuple(out)
 old={v:base(R-2,v) for v in ball(2,end)};now={v:base(R-1,v) for v in ball(3,end)}
 for tick in range(R,R+3):
  nxt={}
  for v in ball(R+2-tick,end):
   ns=[]
   for axis in range(3):
    for sign in (-1,1):
     w=list(v);w[axis]+=sign;ns.append(now[tuple(w)])
   nxt[v]=bx(old[v],bh(bx(*ns)))
  if tick==R and p is not None:nxt[(0,0,0)]=tuple(ALL*b for b in (x,1,p))
  old,now=now,nxt
 return now[end]
