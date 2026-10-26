"""Independent scalar signed-cluster/diamond check of the affine witness."""
from pathlib import Path
from functools import lru_cache
from itertools import product
from collections import Counter
from fractions import Fraction
import argparse,hashlib,json
H=(0,2,4,7,1,3,5,6)
T=185;P=12*840**185;S=T+P;R=S+68;N=R+9

def need(b,s):
 if not b:raise RuntimeError(s)
def pack(v):return 4*v[0]+2*v[1]+v[2]
def unpack(v):return(v>>2,(v>>1)&1,v&1)
def hp(v,n):
 for _ in range(n%12):v=H[v]
 return v
def dist(a,b):return sum(abs(x-y)for x,y in zip(a,b))
def odd(ds):
 v=0
 for d in ds:
  if v&d:return False
  v|=d
 return True

@lru_cache(None)
def lower(t,y,z,x):
 if t<0 or min(abs(y)+abs(z),abs(y+76)+abs(z-76))>t:return 0
 if t==0:return 2*x if(y,z)==(0,0)else 7 if(y,z)==(-76,76)else 0
 need(t==min(abs(y)+abs(z),abs(y+76)+abs(z-76)),'independent W grid remains first-front')
 return H[lower(t-1,y-1,z,x)^lower(t-1,y+1,z,x)^lower(t-1,y,z-1,x)^lower(t-1,y,z+1,x)]

def sources(u,a,b):
 delta=a^b
 return {(0,0,0):4*u+1,(0,0,-14):5*u,(0,0,-16):3+2*u,
         (0,0,-18):pack((u^b,a,u^a)),(1,0,-17):5*delta,(-1,0,-17):7*delta}

@lru_cache(None)
def direct(t,x,y,n,u,a,b):
 src=sources(u,a,b)
 if t<0 or min(abs(x-i)+abs(y-j)+abs(n-k)for i,j,k in src)>t or(t-x-y-n)%2:return 0
 if t==0:return src.get((x,y,n),0)
 inp=direct(t-1,x-1,y,n,u,a,b)^direct(t-1,x+1,y,n,u,a,b)
 inp^=direct(t-1,x,abs(y-1),n,u,a,b)^direct(t-1,x,y+1,n,u,a,b)
 inp^=direct(t-1,x,y,n-1,u,a,b)^direct(t-1,x,y,n+1,u,a,b)
 return direct(t-2,x,y,n,u,a,b)^H[inp]

@lru_cache(None)
def strip(u,a,b):
 rows={}
 def get(e,x,y,n):
  y=abs(y)
  if e<0 or abs(x)+y>e or(e-abs(x)-y)%2 or e+abs(x)+y>18:return 0
  return rows[e,x,y,n]
 for e in range(19):
  for x in range(-e,e+1):
   for y in range(e-abs(x)+1):
    if(e-abs(x)-y)%2 or e+abs(x)+y>18:continue
    rows[e,x,y,0]=direct(e,x,y,0,u,a,b)
    for n in range(1,254+(18-e)//2):
     inp=get(e,x,y,n-1)^get(e-2,x,y,n+1)
     for dx,dy in((-1,0),(1,0),(0,-1),(0,1)):inp^=get(e-1,x+dx,y+dy,n)
     rows[e,x,y,n]=get(e-2,x,y,n)^H[inp]
 return rows

def ball(r):
 for x in range(-r,r+1):
  for y in range(-r+abs(x),r-abs(x)+1):
   for z in range(-r+abs(x)+abs(y),r-abs(x)-abs(y)+1):yield(x,y,9+z)

@lru_cache(None)
def diamond(x,u,my,mr,a,b,forced=-1):
 upper=strip(u,a,b)
 def init(t,pos):
  xx,yy=pos[0],abs(pos[1]);n=R-pos[2];e=t-n
  value=upper[e,xx,yy,n-P] if e>=abs(xx)+yy and(e-abs(xx)-yy)%2==0 else 0
  for source,bit in[((0,-S,-68),x),((0,S,-68),my^mr),((T,P,-68),my),((-T,P,-68),mr)]:
   ds=[abs(a-b)for a,b in zip(pos,source)]
   if sum(ds)<=t:
    need(sum(ds)==t,'lower source at exact first arrival')
    if odd(ds):value^=hp(2*bit,t)
  if t==R-1 and pos in((0,-9,8),(0,-10,9)):
   y,z=T+pos[1],68+pos[2]
   need(value==(hp(2*x,t)if odd((S+pos[1],z))else 0),'W entry has no upper contribution')
   value=lower(y+z,y,z,x)
  return value
 old={v:init(R-2,v)for v in ball(9)};now={v:init(R-1,v)for v in ball(10)};q8=None
 for tau in range(10):
  nxt={}
  for v in ball(9-tau):
   ns=0
   for axis in range(3):
    for sign in(-1,1):
     w=list(v);w[axis]+=sign;ns^=now[tuple(w)]
   nxt[v]=old[v]^H[ns]
  if tau==0:need(nxt[0,0,0]==pack((x,1,x^u)),'qY preserved')
  if tau==7:need(nxt[0,0,7]==x^u,'q7 preserved')
  if tau==8:
   q8=nxt[0,0,8];need(q8==2*(x^u),'previous q8 preserved')
   if forced>=0:nxt[0,0,8]=2*forced
  old,now=now,nxt
 return now[0,0,9],q8

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--author',type=Path,default=Path(__file__).resolve().parent.parent);ap.add_argument('--source-root',type=Path);args=ap.parse_args();author=args.author
 source_root=args.source_root or author.parent.parent
 expected_hashes=json.loads((Path(__file__).resolve().parent/'INPUT-HASHES.json').read_text())
 need(all(hashlib.sha256((author/name).read_bytes()).hexdigest()==digest
          for name,digest in expected_hashes.items()),'reviewed immutable author bytes')
 evidence=json.loads((author/'symmetric-result.json').read_text());data=evidence['q9_table_hex']
 counted=0;accepted=0;fail=Counter();interventions=[]
 for x,u,my,mr,a,b in product((0,1),repeat=6):
  out,q8=diamond(x,u,my,mr,a,b)
  index=((((((x*2+u)*2+my)*2+mr)*2+a)*2+b)*8+4)*64+5*8+7
  need(out==int(data[index],16),'independent scalar versus published witness')
  if(a,b)!=(0,1):need(out==pack((0,x^u^a,x^u^b)),'accepted native phase-code witness');accepted+=1
  else:fail[x,u,out]+=1
  counted+=1
 for p in(0,1):
  bad=0
  for x,u,my,mr,a,b in product((0,1),repeat=6):
   if(a,b)==(0,1):continue
   out,_=diamond(x,u,my,mr,a,b,p)
   bad+=out!=pack((0,p^a,p^b))
  expected=next(r for r in evidence['q8_interventions']if r['candidate']==[4,5,7]and r['p']==p)
  need(bad==expected['mismatch_rows']==24,'late intervention obstruction');interventions.append(bad)
 # Independently compare the signed strip with direct native recursion at all
 # low-n coordinates for the actual eight u,a,b configurations, no family search.
 comparisons=0
 for u,a,b in product((0,1),repeat=3):
  for (e,x,y,n),value in strip(u,a,b).items():
   if n<3:need(value==direct(n+e,x,y,n,u,a,b),'signed strip direct control');comparisons+=1
 need(P%(12*840**18)==0,'actual signed-strip sufficient period')
 q9=(0,S,77);q8=(0,S,76)
 geometry_path=source_root/'parallel_v3/history_control/SOURCE-GEOMETRY.json'
 raw_geometry=geometry_path.read_bytes()
 need(hashlib.sha256(raw_geometry).hexdigest()=='2642e1a68825faa5d3bb1049e8722adec1ec33bd3f56b9e4416b2c902a85ec5d','inherited geometry hash')
 old_sources=json.loads(raw_geometry)['sources'];need(len(old_sources)==1479,'inherited source count')
 centers=[((0,T,0),T),((T,0,0),T),((-T,0,0),T),((4*T,0,0),T),((0,0,-8*T),T),
          ((0,S,0),S),((T,P,0),S),((-T,P,0),S),((4*T,P,0),S),
          ((0,S,68),R),((0,S,-68),R),((0,S,70),R+2),((0,S,71),R+3),
          ((12*R,0,0),R),((-12*R,0,0),R),((0,S,75),R+7),(q8,R+8)]
 for pos in[(0,S,S+154),(1,S,S+153),(-1,S,S+153)]:
  need(dist(pos,q9)==N and dist(pos,q8)==N+1,'source boundary and earlier read exclusion')
  need(all(tuple(item['position'])!=pos for item in old_sources),'no inherited source overwrite')
  need(all(dist(pos,center)>radius for center,radius in centers),'all earlier ready balls excluded')
  need(all(dist(pos,low)>=2*R for low in[(0,0,0),(0,2*S,0),(T,P+S,0),(-T,P+S,0),(0,-76,76)]),'upper/lower separation before R')
 # Every physical controller field is affine in old u and two new bits.
 rows=[]
 for coord in sources(0,0,0):
  values=[sources(u,a,b)[coord]for u,a,b in product((0,1),repeat=3)]
  for field in range(3):
   coef=[v>>field&1 for v in values]
   for k in range(3):
    for n in range(8):
     if n&(1<<k):coef[n]^=coef[n^(1<<k)]
   need(all(coef[n]==0 for n in(3,5,6,7)),'no nonlinear initial source term')
   rows.append(coef[1]+2*coef[2]+4*coef[4])
 basis={}
 for v in rows:
  while v:
   k=v.bit_length()-1
   if k in basis:v^=basis[k]
   else:basis[k]=v;break
 need(len(basis)==3,'controller rank three in old u and new a,b')
 # Recalculate the exhaustive table's decision predicate independently.
 # This checks verdict extraction for all candidates, not a second native
 # evolution of their rejected configurations.
 table_winners=[]
 for cc,kp,km in product(range(8),repeat=3):
  good=True
  for x,u,my,mr,a,b in product((0,1),repeat=6):
   if(a,b)==(0,1):continue
   index=((((((x*2+u)*2+my)*2+mr)*2+a)*2+b)*8+cc)*64+kp*8+km
   if int(data[index],16)!=pack((0,x^u^a,x^u^b)):good=False;break
  if good:table_winners.append([cc,kp,km])
 need(table_winners==evidence['accepted_three_mask_witnesses']==[[4,5,7],[4,7,5]],'complete table decision extraction')
 # Joint phase law with the already specified independent remote predicate/z.
 # This checks the finite assembly, not independent remote geometry certification.
 laws=[]
 for x,u in product((0,1),repeat=2):
  y=x^u;law=Counter();failed=0
  for a,b,k,z in product((0,1),(0,1),range(8),(0,1)):
   out,prev=diamond(x,u,0,0,a,b)
   if k<{(0,0):5,(1,0):3,(1,1):2,(0,1):0}[a,b]:
    raw=unpack(out);decoded=(raw[1],prev//2,raw[2],z);law[decoded]+=1
   else:failed+=1
  want=Counter()
  for a,b,w in[(0,0,5),(1,0,3),(1,1,2)]:
   for z in(0,1):want[y^a,y,y^b,z]=w
  need(law==want and failed==44,'full joint accepted phase law and failures');laws.append({'x':x,'u':u,'accepted':sum(law.values()),'failed':failed})
 result={'schema':'oi.affine-local-controller.review.v1','verdict':'PASS_SCOPED_WITNESS',
 'author_commit':'bf1bc9fb067e38417d8968e26a691debf7d3eb5f',
 'scalar_native_cases':counted,'accepted_cases':accepted,'failure_rows':sum(fail.values()),
 'failure_raw_by_x_u':[[x,u,out]for x,u,out in sorted(fail)],'late_intervention_mismatches':interventions,
 'signed_direct_comparisons':comparisons,'initial_affinity':'PASS','controller_rank':len(basis),
 'old_source_position_comparisons':3*len(old_sources),'old_ready_ball_comparisons':3*len(centers),
 'table_decision_candidates':512,'joint_phase_law_cases':laws,
 'scope':'One affine witness and its retained previous-slice Y/current X,R; no observer access or reusable interface certification.'}
 print(json.dumps(result,sort_keys=True,separators=(',',':')))
if __name__=='__main__':main()
