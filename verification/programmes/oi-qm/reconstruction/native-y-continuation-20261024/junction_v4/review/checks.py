"""Independent review: free junction pivot, exact native propagation and parity.
No author code imports; source table is retained data only. No writes or network.
"""
from pathlib import Path
from functools import lru_cache
from itertools import product
import json
import hashlib

def need(value,label):
 if not value:raise RuntimeError(label)
T=185;P=12*840**T;S=T+P;d=68;R=S+d;N=R+3
pivot=(0,-72,70);target=(0,S-1,70)
def length(p,q):return sum(abs(a-b) for a,b in zip(p,q))
def plus(p,q):return tuple(a+b for a,b in zip(p,q))
axes=((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1))

# Inventory independently transcribed from the transfer/selector/X/outward reports.
original={'X':(0,T,0),'Y':(T,0,0),'R':(-T,0,0),'Z':(4*T,0,0),'H':(0,0,-8*T)}
regions=[('old-'+key,c,T) for key,c in original.items()]
regions += [('relay-'+key,plus(c,(0,P,0)),S) for key,c in original.items() if key!='H']
regions += [('collision+', (0,S,d),R),('collision-',(0,S,-d),R),
            ('out2',(0,S,d+2),R+2),('out3',(0,S,d+3),R+3),
            ('herald',(12*R,0,0),R),('privateZ',(-12*R,0,0),R)]
slacks={name:length(pivot,c)-r for name,c,r in regions}
need(len(slacks)==15,'15 inventoried regions')
for name in ('old-X','old-Y','old-R','relay-X','relay-Y','relay-R'):need(slacks[name]==142,'original/relay slack')
need(slacks['old-Z']==slacks['relay-Z']==3*T+142,'Z slack')
need(slacks['old-H']==7*T+142,'oldH slack')
need((slacks['collision+'],slacks['collision-'],slacks['out2'],slacks['out3'])==(6,142,2,2),'collision/outward slack')
need(slacks['herald']==slacks['privateZ']==11*R+142,'remote slack')
need(all(v>0 for v in slacks.values()),'free pivot')
# Even every generic perpendicular relay d0 >=0 would leave this pivot outside.
for d0 in (0,1,6,68,70,71,184,185,R):
 need(length(pivot,(0,S,d0))-(S+d0)==(142-2*d0 if d0<=70 else 2),'generic +relay slack')
 need(length(pivot,(0,S,-d0))-(S+d0)==142,'generic -relay slack')
geometry_path=(Path(__file__).resolve().parent/'../../parallel_v3/history_control/SOURCE-GEOMETRY.json').resolve()
if not geometry_path.is_file():geometry_path=Path(__file__).with_name('SOURCE-GEOMETRY.json')
geometry_bytes=geometry_path.read_bytes()
need(hashlib.sha256(geometry_bytes).hexdigest()=='2642e1a68825faa5d3bb1049e8722adec1ec33bd3f56b9e4416b2c902a85ec5d','retained source geometry digest')
geometry=json.loads(geometry_bytes)
need(len(geometry['sources'])==1479,'source count')
need(all(tuple(v['position'])!=pivot for v in geometry['sources']),'not an original affine source')
# All old/selector banks have z=0 or negative z; remote banks are x-separated.
need(pivot[2]>0 and pivot[1]!=0,'not in Mj/Nj/Fik banks')
controls=[(0,2*S,0),(T,P+S,0),(-T,P+S,0),(4*T,P+S,0),(0,S,S+2*d),(0,S,-S-2*d)]
need(pivot not in controls,'not a control or pulse')
need(length(pivot,target)==N and plus(pivot,(0,N,0))==target,'unique positive-y ray')
L=64*R+64*T+1
need(L>2*N and L%2==1,'odd torus with no competing short winding ray')
for centre,deadline in (((0,S,d),R),((0,S,d+2),R+2),((0,S,d+3),R+3),(target,R+2)):
 need(length(pivot,centre)>deadline,'accepted earlier endpoint unaffected')
print('V1: independent ready/source/bank inventory; all15 exact slacks; pivot free even with q3 extension; no-wrap axial path: PASS')

# Literal permutation table: integer encoding A=bit0, B=bit1, D=bit2.
H=(0,4,1,5,2,6,7,3)
for a,b in product(range(8),repeat=2):
 need(len({a^H[m^b] for m in range(8)})==8,'all offset maps invertible')
# General ray geometry for every k follows from one affine coordinate identity;
# instantiate endpoints, near endpoint, and both huge indices.
for k in (1,2,3,T,R,N):
 v=plus(pivot,(0,k,0))
 need(length(pivot,v)>k-2,'old term outside pivot cone')
 for e in axes:
  need(length(pivot,plus(v,e))==(k-1 if e==(0,-1,0) else k+1),'only predecessor can depend on pivot')
print('V2: all64 translated H maps bijective; complete ray old/five-neighbor independence distances: PASS')

# Independent dense-background native recursion with eight scalar-state lanes.
def dense(seed):
 def background(t,v):
  a,b,c=v;n=(a*131+b*593+c*1297+t*2017+seed*7919)
  return ((n*n+17*n+23*seed)^(n>>2))&7
 @lru_cache(None)
 def evolve(t,v):
  if t==0 and v==(0,0,0):return tuple(range(8))
  if t in (-1,0):return (background(t,v),)*8
  neighbours=[evolve(t-1,plus(v,e)) for e in axes]
  old=evolve(t-2,v)
  out=[]
  for lane in range(8):
   z=0
   for n in neighbours:z ^= n[lane]
   out.append(old[lane]^H[z])
  return tuple(out)
 return evolve
cases=0;changed=0
for seed in (2,7,19):
 at=dense(seed)
 for e in axes:
  bare=tuple(range(8))
  for k in range(1,8):
   pos=tuple(k*a for a in e);old=at(k-2,pos)
   others=[at(k-1,plus(pos,w)) for w in axes if w!=tuple(-a for a in e)]
   need(len(set(old))==1 and all(len(set(v))==1 for v in others),'offsets independent of pivot')
   value=at(k,pos);need(set(value)==set(range(8)),'native dense-background permutation')
   bare=tuple(H[v] for v in bare);changed += value!=bare;cases+=1
need(changed>0,'offset-free shortcut must fail')
print('V3: %d independent dense3D native ray cases,all8 pivots; background offsets matter: PASS'%cases)

# A native counterexample to inferring full-history law from a uniform marginal.
@lru_cache(None)
def clean(t,v):
 if t<0 or sum(map(abs,v))>t:return (0,)*8
 if t==0:return tuple(range(8)) if v==(0,0,0) else (0,)*8
 old=clean(t-2,v);ns=[clean(t-1,plus(v,e)) for e in axes]
 out=[]
 for lane in range(8):
  z=0
  for w in ns:z^=w[lane]
  out.append(old[lane]^H[z])
 return tuple(out)
record=clean(1,(0,1,0));terminal=clean(2,(0,2,0))
need(len(set(record))==len(set(terminal))==8,'both marginally uniform')
need(len(set(zip(record,terminal)))==8,'joint not uniform product64')
need(clean(2,(1,1,0))==(0,)*8,'two shortest paths cancel')
print('V4: native marginal-vs-history and multiple-path cancellation countercontrols: PASS')

# Local no-wrap parity only: odd periodic lattices have wrap edges violating it.
def parity(v,t):return (sum(v)+t)%2
need(parity(target,N)==0,'active target parity')
for p,t,expected in (((0,-1,0),0,1),((0,-2,0),0,0),((0,0,0),-1,1)):
 need(parity(p,t)==expected,'resource parity')
need(length((0,-1,0),target)==N-1 and length((0,-2,0),target)==N,'old current frontier capture')
need(length((0,0,0),target)==N-2,'old previous input capture')
for j in (3,4,N):need(length((0,-j,0),target)==N+j-2>N,'later Mj outside')
need(((L-1)+0)%2==0 and (0+1)%2==1,'odd wrap edge violates global spacetime sector')
# Capturing M2 does not imply a nonzero isolated pulse arrival.
parts=(S+1,70)
need((parts[0]&parts[1])==2,'M2 two-coordinate path parity overlap')
need(sum(q.bit_count() for q in parts)>sum(parts).bit_count(),'isolated M2 shortest-path count even')
print('V5: active local parity excludes M1/old previous input but retains M2; global odd-torus qualification necessary; isolated M2 arrival cancels: PASS')

# New initial prescription: active current spatial-even and previous spatial-odd.
inside=[row for row in geometry['sources'] if length(tuple(row['position']),target)<=N]
need(len(inside)==1 and inside[0]['position']==[0,0,0] and inside[0]['field']==1 and inside[0]['mask']==64,'only original x-B source remains')
exceptions=[(0,0,0),(0,2*S,0),(T,P+S,0),(-T,P+S,0),(0,S,S+2*d),(0,-2,0)]
need(len(set(exceptions))==6 and all(parity(v,0)==0 for v in exceptions),'six distinct active current exceptions')
need([length(v,target)-N for v in exceptions]==[-2,0,0,0,-4,0],'exact six-source distances')
need(length((4*T,P+S,0),target)==N+3*T,'Z selector outside')
need(length((0,S,-S-2*d),target)==N+2*d,'opposite pulse outside')
for j in (1,2,3,70,T,P,R):
 need(length((0,-j,0),target)-N==j-2,'Mj slack identity')
 need(length((0,0,-9*T-j),target)-N==9*T+j-2,'Nj slack identity')
 for key,c in original.items():
  if key=='H':continue
  f=plus(c,(0,P+S+j,0))
  need(length(f,target)-N==j+(3*T if key=='Z' else 0),'Fik slack identity')
need(12*R>N,'all remote source/bank x separation')
need(parity((0,0,0),-1)==1,'previous unknown input inactive')
print('V6: new initial active-sector prescription preserves source exceptions and all named banks; exactly6 current sources and zero active previous sector: PASS')
print('VERDICT: ACCEPT unchanged-junction obstruction and compatible initial geometry only; extended output, joint-history law, and integrated reset remain OPEN.')
