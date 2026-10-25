"""Conditional native raw-A extractor; exact standalone standard-library checks."""
from itertools import product
from functools import lru_cache
from pathlib import Path
import hashlib
import core_from_v1 as baseline
Z=(0,0,0); TARGET=(3,2,0); DEADLINE=5
DIRECTIONS=tuple(tuple(s if j==i else 0 for j in range(3)) for i in range(3) for s in (-1,1))
CONSTANTS={(0,1,-1):(0,1,0),(1,1,-2):(1,1,1),(8,2,0):(0,1,0)}

def need(v,m):
 if not v:raise RuntimeError(m)
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def dist(a,b):return sum(abs(x-y) for x,y in zip(a,b))
def H(v):a,b,d=v;return b,d,a^(b&d)
def xor(*vs):
 out=[0,0,0]
 for v in vs:
  for i in range(3):out[i]^=v[i]
 return tuple(out)
def ball(r,center=Z):
 return tuple(add(center,(x,y,z)) for x in range(-r,r+1) for y in range(-r,r+1) for z in range(-r,r+1) if abs(x)+abs(y)+abs(z)<=r)

def direct(q,old=Z,corrector=True):
 src=dict(CONSTANTS)
 if not corrector:del src[(8,2,0)]
 src[Z]=q
 @lru_cache(None)
 def at(t,v):
  if t==-1:return old if v==(1,0,0) else Z
  if t==0:return src.get(v,Z)
  return xor(at(t-2,v),H(xor(*(at(t-1,add(v,d)) for d in DIRECTIONS))))
 return at

def shell(q,corrector=True):
 src=dict(CONSTANTS)
 if not corrector:del src[(8,2,0)]
 src[Z]=q
 current={v:src.get(v,Z) for v in ball(DEADLINE,TARGET) if dist(v,TARGET)==DEADLINE}
 final_argument=None
 for r in range(DEADLINE-1,-1,-1):
  nxt={}
  for v in ball(r,TARGET):
   if dist(v,TARGET)!=r:continue
   arg=xor(*(current.get(add(v,d),Z) for d in DIRECTIONS))
   nxt[v]=H(arg)
   if r==0:final_argument=arg
  current=nxt
 return current[TARGET],final_argument

for q in product((0,1),repeat=3):
 at=direct(q)
 need(all(at(t,TARGET)==Z for t in range(5)),'blank prefix')
 need(at(5,TARGET)==(0,q[0],0),'arbitrary raw-A extraction')
 need(shell(q)==((0,q[0],0),(0,0,q[0])),'independent shell sweep')
 need(shell(q,False)==((0,q[0],1),(1,0,q[0])),'unflipped endpoint certificate')
print('A1: all8 raw triples; full native causal recursion equals independent first-arrival shell; prefix blank; endpoint (0,A,0): PASS')
for x,y in product((0,1),repeat=2):
 q=(y,y,1^(x&y));need(direct(q)(5,TARGET)==(0,y,0),'three-code input')
 for p in (0,1):
  q=(p,y,1^(x&y));need(direct(q)(5,TARGET)==(0,p,0),'actual A intervention')
print('A2: all4 native histories plus8 A-only diagnostic interventions; B,D held fixed: PASS')
need(all(dist(s,TARGET)==5 for s in (Z,)+tuple(CONSTANTS)),'all current sources on boundary')
need(all(dist((8,2,0),s)==10 for s in (Z,(0,1,-1),(1,1,-2))),'corrector cannot meet earlier')
need(3*(len(ball(5))+len(ball(4)))-3==1077,'readiness count')
print('G1: single unknown input;3 fixed sources; current/previous cones5/4; readiness1077 fixed bits: PASS')

# Complete periodic native lattice, independent packed implementation.
L=15; SIZE=L**3; MASK=255
coords=[(i%L,(i//L)%L,i//(L*L)) for i in range(SIZE)]
def index(v):return (v[0]%L)+L*(v[1]%L)+L*L*(v[2]%L)
links=[[index(add(v,d)) for d in DIRECTIONS] for v in coords]
center=TARGET
current_pins={index(v) for v in ball(5,center)}
previous_pins={index(v) for v in ball(4,center)}

def packed_step(old,now):
 nxt=[]
 for i,ns in enumerate(links):
  a=b=d=0
  for j in ns:
   v=now[j];a^=v[0];b^=v[1];d^=v[2]
  p=old[i];nxt.append((p[0]^b,p[1]^d,p[2]^a^(b&d)))
 return nxt
for seed in (17,91):
 def bg(i,k,phase):
  # Dense deterministic exterior, different across all8 truth-table lanes.
  n=(i+1)*1103515245+(k+3)*12345+seed+phase*2654435761
  return ((n>>3)^(n>>13)^n)&MASK
 old=[tuple(bg(i,k,0) for k in range(3)) for i in range(SIZE)]
 now=[tuple(bg(i,k,1) for k in range(3)) for i in range(SIZE)]
 for i in previous_pins:old[i]=Z
 for i in current_pins:now[i]=Z
 for v,q in CONSTANTS.items():now[index(v)]=tuple(MASK*b for b in q)
 now[index(Z)]=(240,204,170)
 initial=(old[:],now[:]);prefix=[]
 for t in range(6):
  prefix.append(now[index(TARGET)])
  if t<5:old,now=now,packed_step(old,now)
 need(prefix==[Z]*5+[(0,240,0)],'full-torus endpoint and prefix')
 # Exact inverse on the full phase, without knowing the input bits.
 for _ in range(5):old,now=packed_step(now,old),old
 need((old,now)==initial,'full-phase reversibility and retained information')
print('T1: full15^3 torus,2 dense arbitrary exteriors,all8 inputs,all6 receiver ticks; complete5-step inverse recovers initial phase: PASS')

# Actual q2 phase violates this gadget's proposed translated old-slice socket.
T=185;P=12*840**T
for x,u,my,mr in product((0,1),repeat=4):
 _,records=baseline.native_second(T,P,68,x,my,mr,u)
 need(records[1][(1,0,2)]==(0,1^u^my,my),'actual dirty old neighbor')
need(dist((1,0,0),TARGET)==4,'dirty old neighbor is required blank')
need(direct((0,0,1),(0,1,0))(5,TARGET)==(0,1,0),'dirty-socket countercontrol')
need(direct((0,0,1))(5,TARGET)==Z,'corresponding clean socket')
print('I1: actual old neighbor at q2+e_x is (0,1 XOR u XOR mY,mY), generally nonblank; controlled dirty-socket example flips result: PASS')
print('SCOPE: conditional native5-tick extractor proved; no late socket loading, native Y reset, joint instrument composition, or native access closure claimed.')
# Reject the simpler two-tick extractor, which copies B instead of actual A.
for q in product((0,1),repeat=3):
 second=xor(H(xor(q,(0,0,1))),H(q),H((0,0,1)))
 need(H(second)==(0,q[1],0),'two-tick derivative identity')
need(H(xor(H((1,0,0)),H((1,0,1)),H((0,0,1))))==(0,0,0),'B-copy fails A=1,B=0 intervention')
print('C1: two-tick B-copy passes native equal-A/B codes but fails actual-A intervention; rejected as substitute: PASS')
