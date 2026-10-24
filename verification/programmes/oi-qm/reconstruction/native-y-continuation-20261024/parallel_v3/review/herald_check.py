"""Independent Lucas-path source-to-axis herald verification, no compiler import."""
from pathlib import Path
from functools import reduce
from itertools import product
import json,hashlib

ROOT=Path(__file__).resolve().parents[1]
D=json.loads((ROOT/'direct_reset/herald.json').read_text())
L=D['deadline'];SOURCES=D['sources']
def need(v,s):
 if not v:raise RuntimeError(s)
need(L==2700 and L%12==0,'deadline')
# Separate the three single-field source wings. All source coordinates are actual data.
wing=[[0]*L for _ in range(3)]
seen=set()
for p,field,mask in SOURCES:
 x,y,z=p;r=L-x
 need(0<=x<L and r>0 and 0<=field<3 and 0<mask<64,'source domain')
 need((y,z)==((r,0),(-r,0),(0,r))[field],'source wing and field')
 need((tuple(p),field) not in seen,'unique source coordinate');seen.add((tuple(p),field))
 wing[field][x]=mask
need(len(SOURCES)==7832,'source count')
# Affine encoding uses exactly five seed directions and no input-dependent source.
basis={}
for _,_,mask in SOURCES:
 w=mask>>1
 while w:
  k=w.bit_length()-1
  if k in basis:w ^= basis[k]
  else:basis[k]=w;break
need(len(basis)==5,'five independent seed coordinates')

# Truth-table lanes for u,v,k0,k1,k2; direct evaluation of affine source masks.
def affine(mask):
 out=0
 for lane in range(32):
  value=(mask&1)^((lane&(mask>>1)).bit_count()%2)
  out |= value<<lane
 return out
H=(0,4,1,5,2,6,7,3)
def power(v,n):
 for _ in range(n%12):v=H[v]
 return v
A=B=C=0
for tick in range(L):
 # At axis x=L-tick-1 each wing contribution is a binomial path sum.
 # Lucas: precisely j subset-of tick have odd binomial coefficients.
 m=[0,0,0];sub=tick
 while True:
  source_x=L-tick-1+sub
  for field in range(3):m[field] ^= wing[field][source_x]
  if sub==0:break
  sub=(sub-1)&tick
 injected=[0,0,0]
 for field in range(3):
  target_field=power(1<<field,tick)
  need(target_field in (1,2,4),'pure-field rotation')
  injected[target_field.bit_length()-1] ^= affine(m[field])
 a=A^injected[0];b=B^injected[1];c=C^injected[2]
 A,B,C=b,c,a^(b&c)
truth=0
for lane in range(32):
 u=lane&1;v=(lane>>1)&1;k=lane>>2
 if k<{(0,0):5,(1,0):3,(1,1):2,(0,1):0}[u,v]:truth |= 1<<lane
need((A,B,C)==(0,truth,0) and truth.bit_count()==10,'full herald from source paths')
print('HER1: all7832 source entries lie on specified boundary wings; unique and affine rank5: PASS')
print('HER2: independent Lucas shortest-path source sum plus2700 native axis updates, all32 seeds, raw(0,G,0),10/32: PASS')
print('SCOPE: exact source-defined standalone native herald checked; compiler-generation algorithm and actual-q2 integration are not certified.')
receivers={'X':(L,0,0),'R':(-L,0,0),'Y':(0,L,0),'G':(12*L,0,0),'Z':(-12*L,0,0)}
points=[('Q',(0,0,0)),('u',(2*L,0,0)),('v',(-2*L,0,0)),('z',(-12*L,-L,0))]
points += [('G',(p[0]+12*L,p[1],p[2])) for p,field,mask in SOURCES]
allowed={'X':{'Q','u'},'R':{'Q','v'},'Y':{'Q'},'G':{'G'},'Z':{'z'}}
for name,c in receivers.items():
 for tag,p in points:
  distance=sum(abs(a-b) for a,b in zip(p,c))
  need(distance==L if tag in allowed[name] else distance>L,'independent source ownership')
 need(sum(map(abs,c))>L-1,'previous arbitrary origin triple excluded')
need(power(4,L)==4,'pureD Z preserved')
print('HER3: every source vs all5 receivers; intended first-arrival boundaries and foreign exclusion; previous input excluded: PASS')
