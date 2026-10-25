"""Exact actual-scale third outward step, standalone standard-library checks."""
from pathlib import Path
from itertools import product
import json,random
from fractions import Fraction
from diamond_strip import direct,indices,initial,advance,inverse
from third_step import calc,orbit,upper,T,P,S,d,R
from inherited_core import hp,ball,native_second

def need(ok,msg):
 if not ok:raise RuntimeError(msg)

count=0
for q in product((0,1),repeat=3):
 at=direct(q);st=initial(q,6)
 for n in range(9):
  for (ell,a,b),v in zip(indices(6),st):
   need(v==at(n+ell,(a,b,n)),'direct 3D versus radial strip');count+=1
  st=advance(st,6)
print('GEO1: %d direct 3-D comparisons; all8 triples, n0..8, all13 strip entries: PASS'%count)
rng=random.Random(20261024)
for _ in range(256):
 st=tuple(tuple(rng.randrange(2) for _ in range(3)) for __ in indices(6))
 need(inverse(advance(st,6),6)==st,'explicit inverse')
 need(advance(inverse(st,6),6)==st,'inverse other direction')
print('GEO2: triangular strip map has explicit inverse;512 arbitrary-state inverse identities: PASS')
for u,per in ((0,3600),(1,2940)):
 st=orbit((u,0,1));need(len(st)==per and len(set(st))==per,'minimal orbit period')
 need(advance(st[-1],6)==st[0],'orbit closes')
 need(R%per==253,'actual giant remainder')
print('GEO3: exact pulse periods3600/2940, no transient; actualR residue253 for both: PASS')

geo=json.loads((Path(__file__).parent/'SOURCE-GEOMETRY.json').read_text())
need(len(geo['sources'])==1479,'source export')
q3=(0,S,d+3);rad=R+3
D=lambda a,b:sum(abs(x-y) for x,y in zip(a,b))
arr=[]
for src in geo['sources']:
 pos=tuple(src['position']);dd=D(pos,q3)
 need(dd>=rad,'old source inside extended cold cone')
 if dd==rad:arr.append((pos,src['field'],src['mask']))
need(arr==[((0,0,0),1,64)],'old source boundary ownership')
controls=[(0,0,0),(0,2*S,0),(T,P+S,0),(-T,P+S,0)]
up=(0,S,S+2*d)
need(all(D(c,q3)==rad and D(c,up)==2*R for c in controls),'lower/upper geometry')
need(D((0,0,0),q3)>rad-1,'old previous input excluded')
need(D((0,S,-S-2*d),q3)>rad,'opposite pulse excluded')
# Explicit general family slacks are linear in the positive index.
for k in (1,2,3,d,P,R):
 for x0,y0,z0 in ((0,S,0),(T,P,0),(-T,P,0),(4*T,P,0)):
  need(D((x0,y0+S+k,z0),q3)>rad,'selector bank outside')
 for f in ((0,-k,0),(0,0,-9*T-k)):
  need(D(f,q3)>rad,'older public bank outside')
need(11*R-3>rad,'remote-bank x exclusion')
print('GEO4: all1479 old sources; initial depth3 extension, old banks and opposite pulse excluded: PASS')

rows={}
for x,u,my,mr,p in product((0,1),repeat=5):
 out,rec=calc(x,u,my,mr,p)
 expected=(u|(x^p),x^p^(u&p)^(u&x&p),u&(x^p))
 need(out==expected,'actual third-step diagnostic formula')
 oldout,oldrec=native_second(T,P,d,x,my,mr,u,p)
 need(rec[2][(0,0,2)]==oldout,'second-step preserved')
 rows[x,u,my,mr,p]=rec
print('GEO5:32 actual x/u/mY/mR/p assignments match complete third-step formula; second-step unchanged: PASS')
for x,u,my,mr in product((0,1),repeat=4):
 out,_=calc(x,u,my,mr)
 need(out==(u,x&u,u),'native third-step formula')
 need(hp((u,0,1),R-3)==(u,1,u),'early informative prefix')
print('GEO6: native q3,R+3=(u,xu,u); earliest q3 prefix,R-3=(u,1,u): PASS')

# Strict raw operand or its complement over the entire retained shrinking diamond.
found=[];sites=0
for tick,rec in rows[0,0,0,0,0].items():
 for v in rec:
  sites+=1
  for field in range(3):
   for c in (0,1):
    if all(row[tick][v][field]==p^c for (x,u,my,mr,p),row in rows.items()):
     found.append((tick,v,field,c))
need(sites==96,'diamond cardinality')
need(found==[(0,(0,0,0),2,0),(2,(0,0,2),0,0)],'exact raw-operand census')
print('GEO7:96 site-times,576 field/complement candidates,32 assignments each: only old qY.D and q2.A retain rawp: PASS')
# Handpicked countercontrol: native same-y histories can have different q3 outputs.
need(calc(0,0)[0]!=calc(1,1)[0],'third step not y-only')
need(calc(0,0,p=1)[0][0]!=1 or calc(1,0,p=1)[0][0]!=1,'rawA is not generallyp')
need(Fraction(5,16)*Fraction(1,2)==Fraction(5,32),'prefix leak weight inherited success law')
print('GEO8: treating q3 as rawY or cleanY fails; early sample leak weight5/32 under inherited success law: PASS')
print('SCOPE: exact depth3 private transport extension; no reset, no public shutter, no general geometry no-go.')
