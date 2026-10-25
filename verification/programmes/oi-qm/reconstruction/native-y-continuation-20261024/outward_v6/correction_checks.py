"""Candidate q7 correction: full dipole, unique-front geometry, both diagnostics."""
from pathlib import Path
from itertools import product
import hashlib,json
from model import *
from correction_model import direct,dipole_strip,DIPOLE_ROWS,result

def need(ok,msg):
 if not ok:raise RuntimeError(msg)

# The entire nonlinear upper/C dipole is evaluated, not added pulse outputs.
tables=result();data=dipole_strip();count=0
for (ell,a,b),arr in data.items():
 for n in range(9):
  need(arr[n]==direct(n+ell,a,b,n),'dipole strip versus direct 3D')
  count+=16
need(P%(12*840**14)==0,'actual shift exponent')
print('COR1: %d scalar direct dipole comparisons; all16 u/C assignments and70 strip entries,n0..8: PASS'%count)
expected=[[(1,1,0),(0,1,0),(1,0,1),(1,1,1),(0,1,1),(0,0,1),(0,0,0),(1,0,0)],
          [(1,1,1),(1,1,0),(1,0,1),(1,0,0),(0,0,0),(0,1,0),(0,0,1),(0,1,1)]]
for u,tab in enumerate(tables):
 need(tab['table']==expected[u],'full neighbor permutation table')
 need(len(set(tab['table']))==8,'C to neighbor bijection')
 need(tab['matches']==[(u,0,u)],'initial source inverse')
 need(X(tab['table'][0],tab['table'][5*u])==(u,0,u),'net incoming correction')
 old=strip(14)[12,0,0][246]
 need(tuple((v>>u)&1 for v in old)==(1,1,1),'old q7 triple')
 # C=0 is the unmodified upper pulse, checked against separate pulse evaluator.
 baseline=strip(14)[14,0,0][245]
 need(tab['base']==tuple((v>>u)&1 for v in baseline),'zero-C baseline')
print('COR2: both8-state input-source maps bijective; unique C=(u,0,u) gives delta=(u,0,u); old q7 triple111: PASS')

q7=(0,S,d+7);q8=(0,S,d+8);N7=R+7;f=(0,S,S+2*d+14);up=(0,S,S+2*d)
D=lambda a,b:sum(abs(x-y) for x,y in zip(a,b))
need(D(f,q7)==N7 and D(f,q8)==N7-1,'new-source first arrival')
need(D(f,up)==14,'dipole spacing')
need(D(up,q8)==R-8,'reduced dipole axis')
need((R-8)-P==245 and (N7-1)-P==259,'reduced query')
lower=[(0,0,0),(0,2*S,0),(T,P+S,0),(-T,P+S,0)]
need(all(D(c,f)==2*N7 for c in lower),'lower sources cannot meet correction beforeN7')
for axis in range(3):
 for sign in (-1,1):
  w=list(q7);w[axis]+=sign;w=tuple(w)
  need(D(f,w)==(N7-1 if w==q8 else N7+1),'only upper neighbor affected')
need(D(f,q7)>N7-2,'old local slice unaffected')
need(all(D(c,q8)>N7-1 for c in lower),'no lower source at upper neighbor')
need(D((0,S,d),q8)>N7-1-R,'qY diagnostic excluded from upper neighbor')
need(D((0,S,d+2),q8)>N7-1-(R+2),'q2 diagnostic excluded from upper neighbor')
# Existing prepared current balls, including q2/q3; new f is outside each.
old_centers=[((0,T,0),T),((T,0,0),T),((-T,0,0),T),((4*T,0,0),T),((0,0,-8*T),T),
 ((0,S,0),S),((T,P,0),S),((-T,P,0),S),((4*T,P,0),S),
 ((0,S,d),R),((0,S,-d),R),((0,S,d+2),R+2),((0,S,d+3),R+3),
 ((12*R,0,0),R),((-12*R,0,0),R)]
need(all(D(f,c)>radius for c,radius in old_centers),'old ready regions untouched')
need(all(D(f,c)>N7 for c,radius in old_centers),'old receiver histories throughN7 untouched')
for k in range(1,7):need(D(f,(0,S,d+k))>R+k,'earlier outward endpoints untouched')
geo_candidates=[Path(__file__).parent.parent/'parallel_v3/history_control/SOURCE-GEOMETRY.json',Path(__file__).parent/'SOURCE-GEOMETRY.json']
gp=next((p for p in geo_candidates if p.exists()),None);need(gp is not None,'geometry available')
prov=json.loads((Path(__file__).parent/'PROVENANCE.json').read_text())
need(hashlib.sha256(gp.read_bytes()).hexdigest()==prov['source_geometry_sha256'],'geometry digest')
G=json.loads(gp.read_text());need(all(tuple(src['position'])!=f for src in G['sources']),'no old source overwritten')
# All protected near frontier families havez=0 or negativez; remote families have nonzerox.
need(f[2]>0 and f[0]==0,'protected family disjointness form')
print('COR3: complete first-arrival geometry; only upper neighbor changes atN7−1; all15 old ready regions and receiver histories excluded: PASS')

# Use the newly evaluated dipole neighbor to recompute the full final native update.
# Both intervention sites are tested separately, retaining every other field.
for site in ('qY','q2'):
 out,rec=calc(7,site)
 old=(ALL,ALL,ALL)
 neighbors=[]
 end=(0,0,7)
 for axis in range(3):
  for sign in (-1,1):
   w=list(end);w[axis]+=sign;w=tuple(w)
   neighbors.append(rec[6][w])
 prior_sum=X(*neighbors)
 need(X(old,H(prior_sum))==out,'unmodified full final update')
 actual_old=rec[5][end]
 need(actual_old==old,'old local term checked in retained diamond')
 delta=(UM,0,UM)
 corrected=X(old,H(X(prior_sum,delta)))
 for i,(x,u,my,mr,p) in enumerate(ROWS):
  if site=='qY':expected_row=(x&(1^u)&(1^p),(x^u)&(1^p),p)
  else:expected_row=((x^p)&(1^u),x^u^p,x^(x&u)^p^(x&p)^(x&u&p))
  need(lane(corrected,i)==expected_row,'corrected diagnostic formula')
  if p==x^u:need(lane(corrected,i)==(0,0,p),'native clean code')
 if site=='qY':need(corrected[2]==PM,'raw qY operand retained')
 else:need(lane(corrected,ROWS.index((1,0,0,0,0)))==(1,1,1),'q2 input counterexample persists')
print('COR4: all32 qY.D diagnostic rows yield(x(1+u)(1+p),(x+u)(1+p),p); native rows clean(0,0,y): PASS')
print('COR5: all32 q2.A diagnostic rows checked separately; x1/u0/p20 still gives111, so reusable q2 transfer not proved: PASS')
for u in (0,1):need(hp((u,0,1),R-7)==(u,u,1),'old early prefix remains')
print('COR6: correction cannot affect any q7 prefix; informativeR−7 prefix(u,u,1) remains private: PASS')
print('SCOPE: native clean qY readout under modified initial depth7 preparation; no native reset or arbitrary q2-input socket.')
