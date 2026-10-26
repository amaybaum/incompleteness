"""Exact history-sidecar continuation. Standard library, stdout only.
The local recurrence core is inherited; late parity/front tests are separate.
"""
from pathlib import Path
from itertools import product
from functools import lru_cache
import json
from core import native_second,upper,hp,H,X,odd,ZERO

def need(v,m):
 if not v: raise RuntimeError(m)

T=185;P=12*840**T;S=T+P;d=68;R=S+d
side=(0,-1,2)
# All old selector masks and both unknown/sample values; record table is the
# already accepted shrinking diamond. Nothing is inserted during these runs.
for x,my,mr,u in product((0,1),repeat=4):
 y=x^u
 out,records=native_second(T,P,d,x,my,mr,u)
 need(records[1][side]==(0,1^y,x),'native history sidecar')
 expected={
  (0,-1,1):(x,1,y),
  (0,-1,3):(0,1^u,0),
  (0,0,2):(0,u,1),
  (0,-2,2):ZERO,
  (1,-1,2):ZERO,
  (-1,-1,2):ZERO,
 }
 for v,value in expected.items():need(records[0][v]==value,'six-neighbour table')
 need(X(*expected.values())==(x,0,1^y),'actual incoming neighbour sum')
 need(upper((u,0,1),R-1,(0,1,R-2))==ZERO,'old sidecar slice zero')
 need(H((x,0,1^y))==(0,1^y,x),'one native update')
 for p in (0,1):
  diagnostic,rec=native_second(T,P,d,x,my,mr,u,p)
  need(rec[1][side]==(0,1^y,x),'sidecar independent of diagnostic p')
  need(diagnostic[0]==p,'q2 raw A is actual diagnostic operand')
print('H1:16 native assignments and32 diagnostics; exact sidecar and six-neighbour proof table: PASS')

# Prefix uses distance, parity and the inherited first-arrival convention.
upperloc=(0,0,R)
lower=[(0,-S,-d),(0,S,-d),(T,P,-d),(-T,P,-d)]
dist=lambda a,b:sum(abs(x-y) for x,y in zip(a,b))
need(dist(side,upperloc)==R-1,'first possible upper arrival')
need(odd((0,1,R-2))==0,'upper first arrival cancels')
need(all(dist(side,v)>=R+1 for v in lower),'lower fronts absent throughR')
need((R-1)&1==0,'actual even upper distance')
need(dist(side,(0,0,0))==3,'qY diagnostic cannot arrive in one tick')
# All current local source positions are even in absolute lattice parity;
# the sidecar at tickR is in the other sector, while the previous unknown
# input cannot arrive untilR+2. No earlier uncontrolled source is admitted by
# the inherited ready cone, since these causal cones are its subsets.
need((sum((0,S-1,d+2))+R)%2==1,'sidecar atR opposite local current sector')
print('H2:sidecar prefix is zero throughR; arrivalR+1; no pre-R disclosure: PASS')

# Exact nexttick causal boundary. Merely being in a cone is not asserted to
# prove an unmasked leak; the clean-nuisance countercontrol is explicit.
sabs=(0,S-1,d+2);old=(0,0,0);frontier=(0,-1,0)
need(dist(sabs,old)==R+1,'previous-input distance')
need(dist(sabs,frontier)==R+2,'old frontier distance')
need(odd((S-1,d+2))==1,'old pulse first-arrival parity')
need(odd((S,d+2))==1,'frontier pulse first-arrival parity')
need((R+1)%12==2 and (R+2)%12==3,'actual H phases')
data=json.loads((Path(__file__).parent/'SOURCE-GEOMETRY.json').read_text())
inside=[src for src in data['sources'] if dist(tuple(src['position']),sabs)<=R+2]
need(len(data['sources'])==1479,'frozen source count')
need(len(inside)==1 and inside[0]['position']==[0,0,0],'all old source positions at nexttick')
controls=[(0,2*S,0),(T,P+S,0),(-T,P+S,0)]
pulses=[(0,S,S+2*d),(0,S,-S-2*d)]
need(all(sum(v)%2==0 for v in controls+pulses+[old]),'local inherited sources in even sector')
need((sum(sabs)+R+2)%2==1,'late sidecar in odd sector')
need(all(hp(g,R+1)==hp(g,2) for g in product((0,1),repeat=3)),'H2 old-pulse formula')
need(len({hp(g,2) for g in product((0,1),repeat=3)})==8,'all old triples distinct')
need(len({hp(m,R+2) for m in product((0,1),repeat=3)})==8,'frontier countercontrol also bijective')
print('H3:nexttick previous-input/frontier boundary; all1479 old sources checked; clean-nuisance output H²(g): PASS')

# Independent direct recursion for a previous-slice pulse. Arbitrary backgrounds
# in the opposite sector are included by an explicit deterministic formula;
# the invariant prevents them from entering these queried values.
def direct(g):
 @lru_cache(None)
 def at(t,pos):
  parity=sum(pos)&1
  if t==-1:
   if pos==(0,0,0):return g
   return tuple(((17*pos[0]+29*pos[1]+43*pos[2]+j*13)>>j)&1 for j in range(3)) if parity else ZERO
  if t==0:
   return tuple(((23*pos[0]+31*pos[1]+47*pos[2]+j*11)>>j)&1 for j in range(3)) if parity==0 else ZERO
  ns=[]
  for a in range(3):
   for sign in (-1,1):
    q=list(pos);q[a]+=sign;ns.append(at(t-1,tuple(q)))
  return X(at(t-2,pos),H(X(*ns)))
 return at
count=0
for g in product((0,1),repeat=3):
 at=direct(g)
 for a in range(6):
  for b in range(6):
   if a+b>7:continue
   n=a+b
   expected=hp(g,n) if odd((a,b)) else ZERO
   need(at(n+1,(a,b,0))==expected,'independent previous-pulse first-arrival recursion')
   count+=1
print('H4:%d direct previous-pulse first-arrival cases including dense opposite-parity backgrounds: PASS'%count)

# A simple explicit countercontrol: oldg nonzero gives a nonzero nexttick,
# while independent fixed-history sidecarD previously equalsx. No unconditional
# record-law inference or nexttick full-state memory is asserted.
need(any(hp(g,2)[2]!=x for x in (0,1) for g in product((0,1),repeat=3)),'not persistent raw x')
print('SCOPE:native one-tick sidecar accepted locally; persistent memory, joint nexttick record and G implementation remain open.')
