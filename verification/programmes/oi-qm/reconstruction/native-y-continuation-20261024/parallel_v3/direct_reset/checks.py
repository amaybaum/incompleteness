"""Exact standard-library checks. No network, no writes, explicit -O failures."""
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache,reduce
from itertools import product
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parent
D=json.loads((ROOT/'herald.json').read_text());L=D['deadline'];ZERO=(0,0,0)
def need(ok,msg):
 if not ok:raise RuntimeError(msg)
def H(q):a,b,d=q;return b,d,a^(b&d)
def X(*qs):return tuple(reduce(int.__xor__,(q[i] for q in qs),0) for i in range(3))
def hp(q,n):
 for _ in range(n%12):q=H(q)
 return q
def mix(q,u):a,b,d=q;return a^u,b,d^(u&b)
def dist(p,q):return sum(abs(a-b) for a,b in zip(p,q))
def tables(n):return [sum(1<<j for j in range(1<<n) if j>>i&1) for i in range(n)]
def accept(u,v,k):return k<{(0,0):5,(1,0):3,(1,1):2,(0,1):0}[u,v]
for q in product((0,1),repeat=3):
 need(hp(q,12)==q,'H period12')
 for u in (0,1):
  need(H(X(hp(q,L-1),hp((u,0,0),L-1)))==mix(q,u),'native first-arrival mixer')
  need(mix(mix(q,u),u)==q,'mixer involution')
print('M1: all8 arbitrary triples and both seeds; native first-arrival formula and inverse: PASS',flush=True)
# Independent six-neighbour recursion: 256 lanes = arbitrary Q,u,v,old Q.
vs=tables(8);Q=tuple(vs[:3]);u,v=vs[3:5];oldQ=tuple(vs[5:]);short=12
initial={(0,0,0):Q,(2*short,0,0):(u,0,0),(-2*short,0,0):(v,0,0)}
@lru_cache(None)
def native(t,p):
 if t==-1:return oldQ if p==(0,0,0) else ZERO
 if t==0:return initial.get(p,ZERO)
 if min(dist(p,s) for s in initial)>t and dist(p,(0,0,0))>t+1:return ZERO
 ns=[]
 for axis in range(3):
  for sign in (-1,1):
   w=list(p);w[axis]+=sign;ns.append(native(t-1,tuple(w)))
 return X(native(t-2,p),H(X(*ns)))
for p,expected in (((short,0,0),mix(Q,u)),((-short,0,0),mix(Q,v)),((0,short,0),Q)):
 need(native(short,p)==expected,'full native collision')
 need(all(native(t,p)==ZERO for t in range(short)),'blank prefix')
print('M2: independent3D recursion,L12,256 lanes,3 receivers,blank prefixes: PASS',flush=True)
# Standalone geometry, not inherited late-q2 phase.
receivers={'X':(L,0,0),'R':(-L,0,0),'Y':(0,L,0),'G':(12*L,0,0),'Z':(-12*L,0,0)}
srcs=[('Q',(0,0,0)),('u',(2*L,0,0)),('v',(-2*L,0,0)),('z',(-12*L,-L,0))]
herald_sources={(tuple(p),field):mask for p,field,mask in D['sources']}
for (p,field),mask in herald_sources.items():
 need(dist(p,(0,0,0))==L,'herald source boundary')
 srcs.append(('G',(p[0]+12*L,p[1],p[2])))
for name,q in receivers.items():
 allowed={'X':{'Q','u'},'R':{'Q','v'},'Y':{'Q'},'G':{'G'},'Z':{'z'}}[name]
 for source,p in srcs:
  dd=dist(p,q);need(dd==L if source in allowed else dd>L,'source ownership')
 need(dist((0,0,0),q)>L-1,'old unknown excluded')
need(L==2700 and L%12==0,'phase')
print('G1: L2700 source ownership,7832 herald entries,single Q,old unknown excluded: PASS',flush=True)
# Actual native wing recursion on32 lanes.
variables=tables(5);full=(1<<32)-1
def affine(mask):
 out=full if mask&1 else 0
 for i,x in enumerate(variables):
  if mask>>(i+1)&1:out^=x
 return out
rows=[]
for wing in range(3):
 row=[]
 for x in range(L+1):
  r=L-x;p=((x,r,0),(x,-r,0),(x,0,r))[wing]
  row.append(herald_sources.get((p,wing),0))
 rows.append(row)
state=ZERO
for tick in range(L):
 injected=[0,0,0]
 for wing in range(3):
  injected[(wing-tick)%3]^=affine(rows[wing][-2])
  rows[wing]=[a^b for a,b in zip(rows[wing],rows[wing][1:])]
 expected=[0,0,0]
 if tick<len(D['program']):
  constant,terms=D['program'][tick]
  for j in range(3):
   expected[j]=full if constant>>(2-j)&1 else 0
   for i,coefficient in terms:
    if coefficient>>(2-j)&1:expected[j]^=variables[i]
 need(injected==expected,'native wing vs word')
 state=H(X(state,tuple(injected)))
truth=sum(1<<i for i in range(32) if accept(i&1,(i>>1)&1,i>>2))
need(state==(0,truth,0) and truth.bit_count()==10,'raw herald')
print('H1: all2700 native wing/axis steps,32 cases; raw herald=(0,G,0),10/32 success: PASS',flush=True)
# Entire tagged carrier and every failure, no acceptance change adopted.
def raw(x,y,u,v,z):
 q=(y,y,1^(x&y));return mix(q,u),q,mix(q,v),(0,0,z)
def decode(rr):
 a,b,c,z=rr;y=b[0];g=b[2]^1
 need(a[1]==y and c[1]==y and b[1]==y,'B metadata')
 need(a[2]^1^(a[0]&a[1])^a[1]==g,'X tag extraction')
 need(c[2]^1^(c[0]&c[1])^c[1]==g,'R tag extraction')
 need(z[:2]==(0,0),'Z fields')
 return (a[0],y,c[0],z[2]),g
for x,y in product((0,1),repeat=2):
 law=Counter();failure=F(0)
 for u,v,k,z in product((0,1),(0,1),range(8),(0,1)):
  if not accept(u,v,k):failure+=F(1,64);continue
  rr=raw(x,y,u,v,z);j,g=decode(rr)
  need(g==x*y and j==(y^u,y,y^v,z),'full decode')
  law[(rr,j,g)]+=F(1,64)
 need(failure==F(11,16),'failure retained')
 for u,v,count in ((0,0,5),(1,0,3),(1,1,2)):
  for z in (0,1):
   rr=raw(x,y,u,v,z);j,g=decode(rr)
   need(law[(rr,j,g)]==F(count,64),'whole raw law')
 need(sum(law.values())==F(5,16) and sum(law.values())+failure==1,'normalization')
print('P1:4 histories,256 seed cases; entire tagged-carrier law5:3:2; success5/16,failure11/16: PASS',flush=True)
for x,y,u,v,z in product((0,1),repeat=5):
 rr=raw(x,y,u,v,z)
 for index,new in ((0,y^u),(2,y^v)):
  need(rr[index]==(new,y,1^(x&y)^((new^y)&y)),'terminal metadata only')
print('P2: entire X/R cell determined by public(x,y) and designated sign; no other fresh-seed leak: PASS',flush=True)
correct=[F(5,10),F(3,10),F(2,10)];wrong=[F(5,10),F(2,10),F(3,10)]
need(correct[0]==wrong[0],'X blind control')
need(abs(sum(correct[:2])-sum(wrong[:2]))==F(1,10),'R catches wrong calibration')
need(F(5,16)*F(1,10)==F(1,32),'R TV withfailure')
a={raw(0,1,u,v,z) for u,v,count in ((0,0,5),(1,0,3),(1,1,2)) for z in (0,1)}
b={raw(1,1,u,v,z) for u,v,count in ((0,0,5),(1,0,3),(1,1,2)) for z in (0,1)}
need(not a&b,'strict rawhistory independence must fail')
need(all((y^(x^y))==x for x,y in product((0,1),repeat=2)),'old seed reuse forces Xnew=x')
print('C1: swapped5:2:3 caught by R(TV1/10;1/32 withfailure); strict common raw encoding fails(TV1); old-seed reuse fails: PASS',flush=True)
# Exact two-encounter composition of kernels; not a native geometric splice.
for oldx in (0,1):
 seq=Counter()
 for u1,v1,k1,z1,u2,v2,k2,z2 in product((0,1),(0,1),range(8),(0,1),(0,1),(0,1),range(8),(0,1)):
  ok1=k1<{(0,0):5,(1,0):4,(1,1):1,(0,1):0}[u1,v1]
  if not ok1:key=('failure1',)
  else:
   y=oldx^u1
   if not accept(u2,v2,k2):key=('failure2',y)
   else:key=('success',y,raw(oldx,y,u2,v2,z2))
  seq[key]+=F(1,4096)
 need(seq['failure1',]==F(11,16),'first failure')
 for y in (0,1):
  need(seq['failure2',y]==F(55,512),'second failure')
  for u2,v2,count in ((0,0,5),(1,0,3),(1,1,2)):
   for z2 in (0,1):need(seq['success',y,raw(oldx,y,u2,v2,z2)]==F(5*count,2048),'full sequential law')
 need(sum(seq.values())==1,'sequential normalization')
print('P3:8192 two-encounter seed cases,all failure records; both success25/256; older5/8 selector gives125/2048: PASS',flush=True)
print('SCOPE: conditional standalone prepared native socket; tagged law is candidate, no encoding relaxation adopted; actual q2 integration remains open.')
