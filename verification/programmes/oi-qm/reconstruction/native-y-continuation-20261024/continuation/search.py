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
outs={(x,u):calc(x,u) for x,u in product((0,1),repeat=2)}
found=[]
for field in range(3):
 other=[j for j in range(3) if j!=field]
 for constants in product((0,1),repeat=2):
  good=ALL
  for (x,u),out in outs.items():
   expected=[None]*3;expected[field]=x^u
   for j,b in zip(other,constants):expected[j]=b
   for a,b in zip(out,expected):good &= a if b else ALL^a
  if good:
   idx=(good&-good).bit_length()-1
   found.append({'field':field,'constants':constants,'count':good.bit_count(),'first':idx})
print(json.dumps(found))
Path('continuation/search-results.json').write_text(json.dumps(found,indent=2))
for y in (0,1):
 a=outs[0,y];b=outs[1,1^y];diff=bx(a,b)
 print('public x dependence at y',y, [v.bit_count() for v in diff], 'any', (diff[0]|diff[1]|diff[2]).bit_count())
# Any nonconstant y-only whole triple, with no fixed choice of encoding.
valid=ALL
for y in (0,1):
 diff=bx(outs[0,y],outs[1,1^y]);valid&=ALL^(diff[0]|diff[1]|diff[2])
print('whole output independent of earlier x given y',valid.bit_count())
diff=bx(outs[0,1],outs[1,0])
print('y1 difference B XOR D always1',diff[1]^diff[2]==ALL)
# Algebraic normal forms in twenty independent slice controls.
def anf(v):
 a=bytearray((v>>i)&1 for i in range(N))
 for j in range(len(basis)):
  step=1<<j
  for b in range(0,N,2*step):
   for k in range(step):a[b+step+k]^=a[b+k]
 return [i for i,c in enumerate(a) if c]
for label,v in [('deltaB',diff[1])]:
 terms=anf(v)
 print(label,terms)
for my,mr in product((0,1),repeat=2):
 a=calc(0,1,my,mr);b=calc(1,0,my,mr);delta=bx(a,b)
 print('mask',my,mr,'deltaA0',delta[0]==0,'deltaBxorD1',delta[1]^delta[2]==ALL)
print('A exact y for all native lanes',all(o[0]==ALL*(x^u) for (x,u),o in outs.items()))
