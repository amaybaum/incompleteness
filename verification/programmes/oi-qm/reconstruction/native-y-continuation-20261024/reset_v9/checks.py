"""Exact bounded native q8 boundary and initially prepared q9 continuation."""
import argparse,importlib.util,json,sys,hashlib
from pathlib import Path
from functools import lru_cache
from itertools import product
ap=argparse.ArgumentParser();ap.add_argument('--source-root',type=Path,default=Path(__file__).resolve().parent.parent)
root=ap.parse_args().source_root.resolve()
s=importlib.util.spec_from_file_location('v8',root/'reset_v8/probe.py');a=importlib.util.module_from_spec(s);s.loader.exec_module(a)
b=a.b;m=a.m;H=m.H;X=m.X;ZERO=m.ZERO;need=b.need;TR=tuple(product((0,1),repeat=3))
UR=tuple((u,j) for u in (0,1) for j in TR);UF=(1<<len(UR))-1
Q=(sum(u<<i for i,(u,j) in enumerate(UR)),0,UF);C=(Q[0],0,Q[0]);G=(Q[0],UF^Q[0],UF)
J=tuple(sum(j[k]<<i for i,(u,j) in enumerate(UR)) for k in range(3))
@lru_cache(None)
def direct4(t,aa,bb,n):
 if t<0 or min(aa+bb+abs(n+s) for s in (0,14,16,18))>t or (t-aa-bb-n)%2:return ZERO
 if t==0:return {(0,0,0):Q,(0,0,-14):C,(0,0,-16):G,(0,0,-18):J}.get((aa,bb,n),ZERO)
 ns=[]
 for k in (0,1):
  for sign in (-1,1):
   ab=[aa,bb];ab[k]+=sign;ab=sorted(map(abs,ab),reverse=True);ns.append(direct4(t-1,*ab,n))
 ns.extend([direct4(t-1,aa,bb,n-1),direct4(t-1,aa,bb,n+1)])
 return X(direct4(t-2,aa,bb,n),H(X(*ns)))
@lru_cache(None)
def strip4():
 values={};L=18
 def get(ell,aa,bb,n):
  aa,bb=sorted((abs(aa),abs(bb)),reverse=True)
  if ell<0 or aa+bb>ell or (ell-aa-bb)%2 or ell+aa+bb>L:return ZERO
  return values[ell,aa,bb][n]
 for ell,aa,bb in m.indices(L):
  arr=[direct4(ell,aa,bb,0)];values[ell,aa,bb]=arr
  for n in range(1,m.BASE+(L-ell)//2+1):
   side=X(*(get(ell-1,aa+da,bb+db,n) for da,db in ((-1,0),(1,0),(0,-1),(0,1))))
   arr.append(X(get(ell-2,aa,bb,n),H(X(arr[n-1],get(ell-2,aa,bb,n+1),side))))
 return values

def lane(v,i):return tuple((w>>i)&1 for w in v)
def code(v):return 4*v[0]+2*v[1]+v[2]
@lru_cache(None)
def raypair(x,j):
 f0=H(X(m.hp((0,x,0),75),m.hp((1,1,1),75)))
 f1=H(f0)
 for k in range(1,j+1):
  forcing=m.hp((0,x,0),k+75) if not k&75 else ZERO
  f0=H(X(f0,forcing));f1=H(X(f1,f0))
 return f0,f1
ROWS=tuple((x,u,my,mr,p,j) for x,u,my,mr,p in product((0,1),repeat=5) for j in TR)
FULL=(1<<len(ROWS))-1
XM,UM,MY,MR,PM=tuple(sum(row[k]<<i for i,row in enumerate(ROWS)) for k in range(5))
def expand(v):return tuple(sum(((w>>(8*u+code(j)))&1)<<i for i,(x,u,my,mr,p,j) in enumerate(ROWS)) for w in v)
@lru_cache(None)
def upper(t,v):
 aa,bb=sorted(map(abs,v[:2]),reverse=True);n=m.R-v[2];ell=t-n
 if ell<0 or aa+bb>ell or (ell-aa-bb)%2:return ZERO
 need(ell+aa+bb<=18,'upper coverage')
 return expand(strip4()[ell,aa,bb][n-m.P])
CONTROLS=[((0,-m.S,-m.d),XM),((0,m.S,-m.d),MY^MR),((m.T,m.P,-m.d),MY),((-m.T,m.P,-m.d),MR)]
RAYS={(0,-9,8):(176,0),(0,-10,9):(175,1)}
def base(t,v):
 out=upper(t,v)
 for pos,bits in CONTROLS:
  ds=tuple(abs(x-y) for x,y in zip(pos,v))
  if sum(ds)<=t:
   need(sum(ds)==t,'lower pre-R first front')
   if m.odd(ds):out=X(out,m.hp((0,bits,0),t))
 if t==m.R-1 and v in RAYS:
  j,level=RAYS[v]
  expected=m.hp((0,XM,0),t) if m.odd((0,m.S+v[1],m.d+v[2])) else ZERO
  need(out==expected,'entry origin only')
  out=tuple(sum(raypair(x,j)[level][k]<<i for i,(x,u,my,mr,p,jv) in enumerate(ROWS)) for k in range(3))
 return out

def compute(intervene=False):
 end=(0,0,9);old={v:base(m.R-2,v) for v in m.ball(9,end)};now={v:base(m.R-1,v) for v in m.ball(10,end)};records={}
 for tau in range(10):
  nxt={}
  for v in m.ball(9-tau,end):
   ns=[now[tuple(v[k]+(s if k==axis else 0) for k in range(3))] for axis in range(3) for s in (-1,1)]
   nxt[v]=X(old[v],H(X(*ns)))
  if tau==0:need(nxt[(0,0,0)]==(XM,FULL,XM^UM),'qY unchanged')
  if tau==7:need(nxt[(0,0,7)]==(0,0,XM^UM),'q7 unchanged')
  if tau==8:
   need(nxt[(0,0,8)]==(0,XM^UM,0),'q8 unchanged')
   if intervene:nxt[(0,0,8)]=(0,PM,0)
  records[tau]=nxt;old,now=now,nxt
 return now[end],records
def main():
 prov=json.loads((Path(__file__).resolve().parent/'PROVENANCE.json').read_text())
 need(all(hashlib.sha256((root/n).read_bytes()).hexdigest()==h for n,h in prov['files'].items()),'inherited dependency digests')
 need(m.P%(12*840**18)==0,'upper exact period')
 need(m.P%(384*840**2)==0,'coupled two-layer period')
 scalar=0
 for x in (0,1):
  for j in range(9):
   for level in (0,1):
    wanted=lane(a.direct(j+76+level,0,j,76+level),a.XR.index((x,(1,1,1))))
    need(raypair(x,j)[level]==wanted,'direct W coupled two-layer front');scalar+=1
 block_controls=0
 for x,f0start in product((0,1),TR):
  outputs=[]
  for f1start in TR:
   f0,f1=f0start,f1start
   for k in range(1,385):
    f0=H(X(f0,m.hp((0,x,0),k+75) if not k&75 else ZERO));f1=H(X(f1,f0))
   need(f0==f0start,'F0 block identity');outputs.append(code(f1));block_controls+=1
  need(len(set(outputs))==8,'F1 block permutation')
 upper_checks=0
 for (ell,aa,bb),arr in strip4().items():
  for n in range(3):need(arr[n]==direct4(n+ell,aa,bb,n),'upper direct collision');upper_checks+=16
 D=lambda x,y:sum(abs(a-bb) for a,bb in zip(x,y));q9=(0,m.S,77);h=(0,-76,76);N=m.R+9;jpos=(0,m.S,m.S+154)
 reached=[]
 for t,r in ((m.R-1,10),(m.R-2,9)):
  for v in m.ball(r,(0,0,9)):
   if D(h,(v[0],m.S+v[1],68+v[2]))<=t:reached.append([t-m.R,list(v)])
 need(reached==[[-1,[0,-10,9]],[-1,[0,-9,8]]],'two W entries')
 need(D(jpos,(0,m.S,76))==m.R+10,'J cannot reach q8 by its read')
 gp=root/'parallel_v3/history_control/SOURCE-GEOMETRY.json';geo=json.loads(gp.read_text())
 need(hashlib.sha256(gp.read_bytes()).hexdigest()=='2642e1a68825faa5d3bb1049e8722adec1ec33bd3f56b9e4416b2c902a85ec5d','geometry digest')
 need(len(geo['sources'])==1479,'source count')
 need(all(D(tuple(s['position']),q9)>=N and tuple(s['position'])!=jpos for s in geo['sources']),'initial ready extension no source overwrite')
 frontier=[((0,2*m.S,0),(0,1,0)),((m.T,m.P+m.S,0),(0,1,0)),((-m.T,m.P+m.S,0),(0,1,0)),((4*m.T,m.P+m.S,0),(0,1,0)),((0,0,0),(0,-1,0)),((0,0,-9*m.T),(0,0,-1))]
 need(all(D(v,q9)>=N and D(tuple(x+y for x,y in zip(v,d)),q9)==D(v,q9)+1 for v,d in frontier),'frontier rays not overwritten')
 need(D((0,-1,0),q9)==N+1,'first prior bank source outside endpoint cone')
 need((N+sum(q9))%2==0 and all(sum(v)%2==0 for v in (h,jpos)),'signal spacetime parity')
 native,rec=compute();late,_=compute(True)
 interface=[];oldout,oldrec=a.calc('qY')
 for x,u,my,mr in product((0,1),repeat=4):
  i=ROWS.index((x,u,my,mr,0,(0,0,0)));oi=a.ROWS.index((x,u,my,mr,x^u,(1,1,1),(0,1,1) if u==0 else (1,0,1)))
  v=(0,0,8);ns={}
  for axis in range(3):
   for sign in (-1,1):
    w=tuple(v[k]+(sign if k==axis else 0) for k in range(3));val=lane(rec[7][w],i)
    need(val==a.lane(oldrec[7][w],oi),'q8 incoming neighbor unchanged');ns[','.join(map(str,w))]=val
  old=lane(rec[6][v],i);need(old==a.lane(oldrec[6][v],oi),'q8 old local unchanged')
  need(X(old,H(X(*ns.values())))==(0,x^u,0),'scalar q8 update')
  interface.append({'x':x,'u':u,'mY':my,'mR':mr,'old_local':old,'incoming':ns,'q8':(0,x^u,0)})
 candidates={};tables={}
 for mode,out in [('native',native),('q8_intervention',late)]:
  table=[];by_u=[]
  for i,(x,u,my,mr,p,j) in enumerate(ROWS):need(lane(out,i)==lane(out,ROWS.index((x,u,0,0,p,j))),'q9 selector-mask independence')
  for x,u,p,j in product((0,1),(0,1),(0,1),TR):table.append(code(lane(out,ROWS.index((x,u,0,0,p,j)))))
  tables[mode]=table
  for u in (0,1):
   ds={}
   for j in TR:
    sets={v:set() for v in (0,1)}
    for x,p in product((0,1),repeat=2):sets[x^u if mode=='native' else p].add(code(lane(out,ROWS.index((x,u,0,0,p,j)))))
    if all(len(s)==1 for s in sets.values()):
     pair=tuple(next(iter(sets[v])) for v in (0,1))
     if pair[0]!=pair[1]:ds.setdefault(pair,[]).append(code(j))
   by_u.append(ds)
  common=sorted(set(by_u[0])&set(by_u[1]));candidates[mode]=[{'codes':pair,'J_by_u':[by_u[0][pair],by_u[1][pair]]} for pair in common]
 target_matches={}
 for name in ('clean_A','clean_B','mixer'):
  matches={}
  for u,seed in product((0,1),repeat=2):
   js=[]
   for j in TR:
    good=True
    for x in (0,1):
     y=x^u;want=(y^seed,0,0) if name=='clean_A' else (0,y^seed,0) if name=='clean_B' else (seed,y,seed*y)
     if lane(native,ROWS.index((x,u,0,0,0,j)))!=want:good=False
    if good:js.append(code(j))
   matches[f'{u},{seed}']=js
  target_matches[name]=matches
 masked_boundary=[]
 for x,u,my,mr,seed in product((0,1),repeat=5):
  j=(u^seed,seed,u^seed);i=ROWS.index((x,u,my,mr,0,j));v=(0,0,9)
  ns={','.join(map(str,w)):lane(rec[8][w],i) for axis in range(3) for sign in (-1,1) for w in [tuple(v[k]+(sign if k==axis else 0) for k in range(3))]}
  old=lane(rec[7][v],i);want=(0,x^u^seed,x^u^seed)
  need(lane(native,i)==want and X(old,H(X(*ns.values())))==want,'affine seed masked route')
  masked_boundary.append({'x':x,'u':u,'mY':my,'mR':mr,'a':seed,'J':j,'old_local':old,'incoming':ns,'q9':want})
 result={'native_masked_route':{'initial_J':'(u XOR a,a,u XOR a)','q9':'(0,y XOR a,y XOR a)','rows':len(masked_boundary),'boundary':masked_boundary},'schema':'oi.q8-next-interface.v9','checks':{'coupled_front_scalar':scalar,'two_layer_block_cases':block_controls,'upper_direct_scalar':upper_checks,'source_geometry':1479,'q8_boundary_rows':len(interface),'q9_diagnostic_rows':2*len(ROWS),'W_entries':reached,'first_frontier_source_excluded':True,'signal_spacetime_parity':0},'q8_interface':interface,'q9_table_order':'lexicographic x,u,p,J; code=4A+2B+D','q9_tables':tables,'q9_common_codes':candidates,'q9_target_matches':target_matches,'verdict':{'native_two_code':'exists' if candidates['native'] else 'excluded','late_q8_two_code':'exists' if candidates['q8_intervention'] else 'excluded','reset':'not_constructed','joint_history':'separate_obligation'}}
 print(json.dumps(result,indent=2,sort_keys=True))
if __name__=='__main__':main()
