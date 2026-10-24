"""Geometry and finite conditional law for the separate ninth-tick corollary."""
import json
from itertools import product
from fractions import Fraction
T=185;P=12*840**185;S=P+T;R=S+68;L=R+9
ports=[(0,T,0),(0,0,-8*T),(T,P,0),(-T,P,0),(4*T,P,0),(0,S,0),(12*R,0,0)]
deadlines=[T,T,S,S,S,S,R]
dirs=[(0,-1,0),(0,0,-1),(0,1,0),(0,1,0),(0,1,0),(0,1,0),(-1,0,0)]
J=(0,S,S+154);q9=(0,S,77)
def dist(p,q):return sum(abs(a-b) for a,b in zip(p,q))
def need(b,s):
 if not b:raise RuntimeError(s)
cases=0;edges=set()
for i,(p,e,a) in enumerate(zip(ports,dirs,deadlines)):
 axis=next(j for j in range(3) if e[j]);times={a+1,L}
 for q in ports+[q9,J]:
  t=(q[axis]-p[axis])*e[axis]
  if a+1<=t<=L:times.add(t)
 for t in sorted(times):
  f=tuple(x+t*d for x,d in zip(p,e))
  need(dist(f,p)==t,'own path')
  need(dist(f,q9)>L,'endpoint readiness preserves bank')
  need(f!=J,'new J does not replace a bank block')
  for j,q in enumerate(ports):
   dd=dist(f,q);need(dd>=t,'chronological ordering')
   if i!=j and dd==t:need(i<j,'equal-time ordering');edges.add((i,j))
  cases+=1
need(edges=={(2,5),(3,5)},'same edge set')
need(all(dist(J,p)>a for p,a in zip(ports,deadlines)),'J cannot affect informative deadlines')
need(dist(J,(0,S,75))>R+7 and dist(J,(0,S,76))>R+8,'J cannot affect earlier Y records')
need(dist(J,q9)==L,'new source at explicit boundary')
need(L<=2*R,'existing no-wrap horizon')
# Uniformity after arbitrary old-herald reweighting is pointwise in u,y:
# each fixed pair has exactly one a for either possible masked sign.
for u,y in product((0,1),repeat=2):
 law={}
 for a in(0,1):
  j=(u^a,a,u^a);need(j[1]==a,'conditional seed is retained injectively')
  t=y^a;law[t]=law.get(t,Fraction())+Fraction(1,2)
 need(law=={0:Fraction(1,2),1:Fraction(1,2)},'fair masked sign given old variables')
print(json.dumps({'schema':'oi.masked-route.history-corollary.v1','verdict':'PASS_CONDITIONAL_COROLLARY_CONTROLS','actual_breakpoint_cases':cases,'same_time_edges':[list(z)for z in sorted(edges)],'post_R_bank_bits':189,'whole_noise_bits':'6*P+18*d+189','joint_probability':'2^(-(6*P+18*d+189)-1)','scope':'Assumes independent free a at original preparation; old seven ports plus terminal q9 only; no whole-boundary or reset claim'},sort_keys=True,separators=(',',':')))
