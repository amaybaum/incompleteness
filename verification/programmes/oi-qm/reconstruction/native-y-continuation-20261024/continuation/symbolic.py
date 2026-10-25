from core import upper,hp,odd,ball
from itertools import product
from pathlib import Path
import json
D=json.loads(Path('continuation/patterns.json').read_text());basis=[int(v,16) for v in D['basis']]
T=185;P=12*840**T;S=T+P;d=68;R=S+d;end=(0,0,2)
slots=[(R-2,v) for v in ball(2,end)]+[(R-1,v) for v in ball(3,end)]
Z=frozenset();O=frozenset({0})
def var(i):return frozenset({1<<i})
def plus(*vs):
 out=Z
 for v in vs:out=out^v
 return out
def times(a,b):
 out=set()
 for x in a:
  for y in b:
   m=x|y
   if m in out:out.remove(m)
   else:out.add(m)
 return frozenset(out)
def vx(*vs):return tuple(plus(*(v[i] for v in vs)) for i in range(3))
def h(v):a,b,c=v;return b,c,plus(a,times(b,c))
x,u,my,mr=(var(i) for i in (0,1,22,23))
controls=[((0,-S,-d),x),((0,S,-d),plus(my,mr)),((T,P,-d),my),((-T,P,-d),mr)]
def base(t,v):
 a=upper((0,0,1),t,(v[0],v[1],R-v[2]));b=upper((1,0,1),t,(v[0],v[1],R-v[2]))
 out=[plus(O if a[i] else Z,u if a[i]^b[i] else Z) for i in range(3)]
 for loc,bit in controls:
  ds=tuple(abs(a-b) for a,b in zip(v,loc))
  if sum(ds)==t and odd(ds):
   for i,c in enumerate(hp((0,1,0),t)):
    if c:out[i]=plus(out[i],bit)
 slot=slots.index((t,v))
 for j,pat in enumerate(basis):
  if pat>>slot&1:
   for i,c in enumerate(hp((0,1,0),t)):
    if c:out[i]=plus(out[i],var(j+2))
 return tuple(out)
old={v:base(R-2,v) for v in ball(2,end)};now={v:base(R-1,v) for v in ball(3,end)}
for tick in range(R,R+3):
 nxt={}
 for v in ball(R+2-tick,end):
  ns=[]
  for axis in range(3):
   for sign in (-1,1):
    w=list(v);w[axis]+=sign;ns.append(now[tuple(w)])
  nxt[v]=vx(old[v],h(vx(*ns)))
 old,now=now,nxt
out=now[end]
def sub(poly,assignment):
 ans=Z
 for m in poly:
  good=True
  for i,b in assignment.items():
   if m>>i&1:
    if not b:good=False;break
    m^=1<<i
  if good:ans=plus(ans,frozenset({m}))
 return ans

def show(poly):
 names=['x','u']+['c'+str(i) for i in range(20)]+['mY','mR']
 return ' XOR '.join('1' if not m else '*'.join(names[i] for i in range(24) if m>>i&1) for m in sorted(poly)) or '0'
delta=tuple(plus(sub(p,{0:0,1:1}),sub(p,{0:1,1:0})) for p in out)
print('Output A:',show(out[0]));print('Delta on y=1:',[show(p) for p in delta])
if out[0]!=plus(x,u):raise RuntimeError('A changed')
if delta[0]!=Z or plus(delta[1],delta[2])!=O:raise RuntimeError('invariant failed')
for i,p in enumerate(out):print('Output',i,show(p))
Path('continuation/symbolic-results.json').write_text(json.dumps({'outputs':[sorted(p) for p in out],'delta':[sorted(p) for p in delta]},indent=2))
