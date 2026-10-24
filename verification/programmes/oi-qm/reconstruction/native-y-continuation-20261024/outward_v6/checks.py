"""Bounded exact replay for straight outward ports k=1..12."""
from model import *
import hashlib

def need(ok,msg):
 if not ok:raise RuntimeError(msg)

need(BASE==253 and R==P+BASE,'actual parameters')
need(P%(12*840**24)==0,'universal strip exponent dividesP')
count=0;data=strip(24)
for (ell,a,b),arr in data.items():
 for n in range(9):
  exact=pulse(n+ell,*sorted((a,b,n),reverse=True))
  need(arr[n]==exact,'strip versus direct spatial recursion')
  count+=2
print('OUT1: %d scalar upper-pulse comparisons;252 strip entries, n0..8, bothu: PASS'%count)
print('OUT2: actualP divisible by universal exponent12*840^24; reduced axial coordinates stay positive: PASS')

geo_candidates=[Path(__file__).parent.parent/'parallel_v3/history_control/SOURCE-GEOMETRY.json',Path(__file__).parent/'SOURCE-GEOMETRY.json']
geo_path=next((q for q in geo_candidates if q.exists()),None)
need(geo_path is not None,'source geometry file unavailable')
geo_bytes=geo_path.read_bytes()
need(hashlib.sha256(geo_bytes).hexdigest()=='2642e1a68825faa5d3bb1049e8722adec1ec33bd3f56b9e4416b2c902a85ec5d','source geometry digest')
G=json.loads(geo_bytes)
need(len(G['sources'])==1479,'source export length')
D=lambda a,b:sum(abs(x-y) for x,y in zip(a,b))
up=(0,S,S+2*d)
controls=[(0,0,0),(0,2*S,0),(T,P+S,0),(-T,P+S,0)]
for k in range(1,13):
 q=(0,S,d+k);rad=R+k
 need(d+k<T,'old-source exclusion range')
 arrivals=[]
 for src in G['sources']:
  pos=tuple(src['position']);dist=D(pos,q)
  need(dist>=rad,'source inside cold interior')
  if dist==rad:arrivals.append((pos,src['field'],src['mask']))
 need(arrivals==[((0,0,0),1,64)],'only origin old boundary source')
 need(all(D(c,q)==rad and D(c,up)==2*R for c in controls),'four lower boundaries/separation')
 need(D((0,0,0),q)>rad-1,'previous unknown excluded')
 need(D((0,S,-S-2*d),q)>rad,'opposite reset excluded')
 need(11*R-k>rad,'remote x exclusion')
 for j in (1,2,12,d,P,R):
  for pos in ((0,2*S+j,0),(T,P+S+j,0),(-T,P+S+j,0),(4*T,P+S+j,0),(0,-j,0),(0,0,-9*T-j)):
   need(D(pos,q)>rad,'frontier outside cold extension')
 for t,radius in ((R-1,k+1),(R-2,k)):
  for v in ball(radius,(0,0,k)):
   a,b=sorted((abs(v[0]),abs(v[1])),reverse=True);ell=t-(R-v[2])
   if ell<0 or ell<a+b or (ell-a-b)%2:continue
   need(ell+a+b<=2*k,'upper strip budget')
   need(BASE-v[2]>=0,'positive reduced axis')
print('OUT3: all17748 old-source/k pairs, actual boundary geometry, frontiers and upper budgets<=2k: PASS')

outcomes={k:calc(k)[0] for k in range(1,13)}
for i,(x,u,my,mr,p) in enumerate(ROWS):
 expected={1:(1,1^x^p,u|(x^p)),
           2:(p,p^u^(x&u)^(p&u),1^p^(p&u)^(p&x&u)),
           3:(u|(x^p),x^p^(u&p)^(u&x&p),u&(x^p)),
           7:(x&(1^u)&(1^p),(x&(1^p))^(u&p),p)}
 for k,v in expected.items():need(lane(outcomes[k],i)==v,'full diagnostic formula')
print('OUT4: all32 assignments recover retained k1/k2/k3 formulas and newk7 formula: PASS')

expected_native={
1:((1,1,0),(1,0,1),(1,1,0),(1,0,1)),
2:((0,0,1),(1,1,1),(1,1,0),(0,0,1)),
3:((0,0,0),(1,0,1),(0,0,0),(1,1,1)),
4:((1,1,1),(1,1,0),(0,0,0),(1,1,0)),
5:((0,1,1),(1,0,0),(1,0,1),(1,0,0)),
6:((1,0,1),(1,0,1),(0,0,1),(0,0,0)),
7:((0,0,0),(0,1,1),(0,0,1),(0,1,0)),
8:((0,1,0),(0,1,0),(1,1,1),(1,1,1)),
9:((1,0,1),(1,1,0),(1,0,1),(0,0,1)),
10:((0,0,1),(1,0,1),(0,0,0),(0,1,1)),
11:((1,0,0),(0,0,1),(1,0,1),(1,1,1)),
12:((0,1,0),(0,1,1),(1,1,1),(1,0,1))}
for k,out in outcomes.items():
 for i,(x,u,my,mr,p) in enumerate(ROWS):
  need(lane(out,i)==lane(out,ROWS.index((x,u,0,0,p))),'diagnostic mask independence')
  if p==x^u:need(lane(out,i)==expected_native[k][2*x+u],'native output table')
print('OUT5: all384 diagnostic endpoint assignments are selector-mask independent; all192 native rows match retained tables: PASS')
raw=[]
for k,out in outcomes.items():
 for field in range(3):
  for c in (0,1):
   if out[field]==PM^(ALL*c):raw.append((k,field,c))
 table=expected_native[k]
 need(table[0]!=table[3] or table[1]!=table[2],'reject y-only full triple')
need(raw==[(2,0,0),(7,2,0)],'complete endpoint operand census')
need(len(set(expected_native[7]))==4,'four retained history codes')
for u in (0,1):need(hp((u,0,1),R-7)==(u,u,1),'k7 earliest prefix')
print('OUT6:72 endpoint field/complement candidates: exactlyk2.A andk7.D are rawp; no fullY-only triple amongk1..12: PASS')
print('OUT7: nativek7=(0,u,y) has4 history codes; earliest prefixR-7=(u,u,1) remains informative: PASS')
print('SCOPE: exact straight-outward endpoint family only; no clean reusable socket, reset, native access mechanism or joint-law certification.')
q2_raw=[]
for k in range(2,13):
 out,_=calc(k,'q2')
 for f in range(3):
  for c in (0,1):
   if out[f]==PM^(ALL*c):q2_raw.append((k,f,c))
need(q2_raw==[(2,0,0)],'q2 operand transfer census')
out,_=calc(7,'q2')
for i,(x,u,my,mr,p2) in enumerate(ROWS):
 need(lane(out,i)==(x^(x&u)^p2^(u&p2),x^p2,x^(x&u)^p2^(x&p2)^(x&u&p2)),'q2 diagnostic formula')
need(lane(out,ROWS.index((1,0,0,0,0)))[2]==1,'q2 intervention counterexample')
print('OUT8: q2.A intervention is not forwarded raw by any later endpoint k3..12; k7 counterexample retained: PASS')
