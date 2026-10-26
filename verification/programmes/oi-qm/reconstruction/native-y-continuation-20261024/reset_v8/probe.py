"""Physical origin/W first-front collision, followed by the native q8 diamond."""
from functools import lru_cache
from itertools import product
from pathlib import Path
import hashlib,json,importlib.util,sys
# Reuse the immutable sibling checkpoint instead of duplicating its evaluators.
prior=Path(__file__).resolve().parent.parent/'reset_v7'
sys.path.insert(0,str(prior))
spec=importlib.util.spec_from_file_location('reset_v7_probe',prior/'probe.py')
b=importlib.util.module_from_spec(spec)
spec.loader.exec_module(b)
m=b.m
TRIPLES=b.TRIPLES
XR=tuple((x,w) for x in (0,1) for w in TRIPLES)
XF=(1<<len(XR))-1
XX=sum(x<<i for i,(x,w) in enumerate(XR))
WW=tuple(sum(w[j]<<i for i,(x,w) in enumerate(XR)) for j in range(3))
ZERO=(0,0,0)
X=m.X;H=m.H;need=b.need

def force(j,x):return m.hp((0,x,0),j+75) if j&75==0 else ZERO

@lru_cache(None)
def ray(j):
 state=H(X(m.hp((0,XX,0),75),m.hp(WW,75)))
 for k in range(1,j+1):state=H(X(state,force(k,XX)))
 return state

@lru_cache(None)
def direct(t,a,y,z):
 if t<0 or min(a+abs(y)+abs(z),a+abs(y+76)+abs(z-76))>t or (t-a-y-z)%2:return ZERO
 if t==0:return (0,XX,0) if (a,y,z)==(0,0,0) else WW if (a,y,z)==(0,-76,76) else ZERO
 terms=[direct(t-1,abs(a-1),y,z),direct(t-1,a+1,y,z),direct(t-1,a,y-1,z),direct(t-1,a,y+1,z),direct(t-1,a,y,z-1),direct(t-1,a,y,z+1)]
 return X(direct(t-2,a,y,z),H(X(*terms)))

ROWS=tuple((x,u,my,mr,p,w,g) for x,u,my,mr,p in product((0,1),repeat=5) for w,g in product(TRIPLES,repeat=2))
FULL=(1<<len(ROWS))-1
XM,UM,MY,MR,PM=tuple(sum(row[j]<<i for i,row in enumerate(ROWS)) for j in range(5))
def lane(v,i):return tuple((a>>i)&1 for a in v)
def expand_upper(v):
 return tuple(sum(((f>>(8*u+TRIPLES.index(g)))&1)<<i for i,(x,u,my,mr,p,w,g) in enumerate(ROWS)) for f in v)
def expand_lower(v):
 return tuple(sum(((f>>(8*x+TRIPLES.index(w)))&1)<<i for i,(x,u,my,mr,p,w,g) in enumerate(ROWS)) for f in v)

@lru_cache(None)
def upper(t,v):
 a,bb=sorted(map(abs,v[:2]),reverse=True);n=m.R-v[2];ell=t-n
 if ell<0 or a+bb>ell or (ell-a-bb)%2:return ZERO
 need(ell+a+bb<=16,'upper budget')
 return expand_upper(b.upper_strip()[ell,a,bb][n-m.P])

def calc(site):
 end=(0,0,8)
 controls=[((0,-m.S,-m.d),XM),((0,m.S,-m.d),MY^MR),((m.T,m.P,-m.d),MY),((-m.T,m.P,-m.d),MR)]
 entry=(0,-9,8);workspace=expand_lower(ray(176))
 def base(t,v):
  val=upper(t,v)
  for pos,bits in controls:
   ds=tuple(abs(a-bb) for a,bb in zip(pos,v))
   if sum(ds)<=t:
    need(sum(ds)==t,'pre-R lower frontier')
    if m.odd(ds):val=X(val,m.hp((0,bits,0),t))
  if t==m.R-1 and v==entry:
   need(val==(0,XM,0),'one-site original lower input')
   val=workspace
  return val
 old={v:base(m.R-2,v) for v in m.ball(8,end)}
 now={v:base(m.R-1,v) for v in m.ball(9,end)}
 records={}
 for tau in range(9):
  nxt={}
  for v in m.ball(8-tau,end):
   ns=[]
   for axis in range(3):
    for sign in (-1,1):
     w=list(v);w[axis]+=sign;ns.append(now[tuple(w)])
   nxt[v]=X(old[v],H(X(*ns)))
  if tau==0:
   need(nxt[(0,0,0)]==(XM,FULL,XM^UM),'original qY signal preserved')
   if site=='qY':nxt[(0,0,0)]=(XM,FULL,PM)
  if tau==2 and site=='q2':
   q=nxt[(0,0,2)]
   need(q==(XM^UM,XM^UM,FULL^(XM&(XM^UM))),'original q2 preserved')
   nxt[(0,0,2)]=(PM,q[1],q[2])
  if tau==7:
   if site=='qY':expected=(XM&(FULL^UM)&(FULL^PM),(XM^UM)&(FULL^PM),PM)
   elif site=='q2':expected=((XM^PM)&(FULL^UM),XM^UM^PM,XM^(XM&UM)^PM^(XM&PM)^(XM&UM&PM))
   else:expected=(0,0,XM^UM)
   need(nxt[(0,0,7)]==expected,'q7 native/past diagnostic unchanged')
   if site=='q7':nxt[(0,0,7)]=(0,0,PM)
  records[tau]=nxt;old,now=now,nxt
 return now[end],records

def code(v):return 4*v[0]+2*v[1]+v[2]

def main():
 p=Path(__file__).parent;prov=json.loads((p/'PROVENANCE.json').read_text())
 need(all(hashlib.sha256((p/f).read_bytes()).hexdigest()==h for f,h in prov['inherited_files'].items()),'inherited file digests')
 checks={'inherited_hashes':True}
 period=384*840
 need(m.P%period==0,'actual P divisible by ray period')
 need(m.P%(12*840**16)==0,'actual P divisible by upper strip period')
 checks['actual_period_divisibility']=True
 permutations=[]
 for x in (0,1):
  perm=[]
  for state in TRIPLES:
   q=state
   for j in range(1,385):q=H(X(q,force(j,x)))
   perm.append(code(q))
  need(len(set(perm))==8,'forcing block is a permutation')
  for a in range(8):
   q=a
   for _ in range(840):q=perm[q]
   need(q==a,'permutation exponent')
  need(all(force(j,x)==force(j+384,x) for j in range(384)),'forcing period finite control')
  permutations.append(perm)
 checks['forcing_block_permutations']=permutations
 for j in range(9):need(ray(j)==direct(j+76,0,j,76),'direct native coupled ray control')
 checks['direct_coupled_scalar_comparisons']=9*16
 nonlinear=[]
 for i,(x,w) in enumerate(XR):
  isolated=X(m.hp((0,x,0),76),m.hp(w,76))
  if lane(ray(0),i)!=isolated:nonlinear.append([x,code(w),code(lane(ray(0),i)),code(isolated)])
 need(bool(nonlinear),'nonlinear countercontrol active')
 checks['isolated_superposition_counterexamples']=nonlinear
 # Actual cone/source geometry, not reduced surrogate coordinates.
 D=lambda a,bb:sum(abs(x-y) for x,y in zip(a,bb))
 N=m.R+7;q7=(0,m.S,75);q8=(0,m.S,76);h=(0,-76,76);g=(0,m.S,m.S+152)
 need(D(h,q7)==N+2 and D(h,q8)==N+1,'W first arrivals')
 reached=[]
 for t,rad in ((m.R-1,9),(m.R-2,8)):
  for v in m.ball(rad,(0,0,8)):
   absolute=(v[0],m.S+v[1],m.d+v[2])
   if D(h,absolute)<=t:reached.append((t-m.R,v,D(h,absolute)-t))
 need(reached==[(-1,(0,-9,8),0)],'one exact entry point')
 centers=[((0,m.T,0),m.T),((m.T,0,0),m.T),((-m.T,0,0),m.T),((4*m.T,0,0),m.T),((0,0,-8*m.T),m.T),((0,m.S,0),m.S),((m.T,m.P,0),m.S),((-m.T,m.P,0),m.S),((4*m.T,m.P,0),m.S),((0,m.S,m.d),m.R),((0,m.S,-m.d),m.R),((0,m.S,m.d+2),m.R+2),((0,m.S,m.d+3),m.R+3),((12*m.R,0,0),m.R),((-12*m.R,0,0),m.R)]
 need(all(D(h,v)>r for v,r in centers),'W outside all designated old cones')
 need(any(D(h,v)<=N+1 for v,r in centers),'late old-record background is not pointwise protected')
 geo_paths=[parent/sub for parent in p.parents for sub in ('parallel_v3/history_control/SOURCE-GEOMETRY.json','outward_v6_geometry/SOURCE-GEOMETRY.json','outward_v6/SOURCE-GEOMETRY.json')]
 gp=next((q for q in geo_paths if q.exists()),None);need(gp is not None,'source geometry available')
 need(hashlib.sha256(gp.read_bytes()).hexdigest()=='2642e1a68825faa5d3bb1049e8722adec1ec33bd3f56b9e4416b2c902a85ec5d','source geometry digest')
 geo=json.loads(gp.read_text());need(len(geo['sources'])==1479,'source count')
 for src in geo['sources']:
  pos=tuple(src['position']);need(pos!=h and D(pos,q8)>=N+1,'source and ready exclusion')
 checks['original_source_geometry_entries']=1479
 checks['W_cone_entry']=[[-1,[0,-9,8],0]]
 checks['designated_readouts_excluded']=len(centers)
 # Full collision diamond, including all source interactions.
 outcomes={};tables={};encoding={};baseline_count=0
 for site in ('qY','q2','q7'):
  out,rec=calc(site);oldout,_=b.calc(site)
  for i,row in enumerate(ROWS):
   x,u,my,mr,inp,w,g=row
   if w==(0,0,0):
    need(lane(out,i)==b.lane(oldout,b.ROWS.index((x,u,my,mr,inp,g))),'W=0 inherited endpoint');baseline_count+=1
   zeroindex=ROWS.index((x,u,0,0,inp,w,g))
   need(lane(out,i)==lane(out,zeroindex),'endpoint selector-mask independence')
  outcomes[site]=out
  tables[site]=[code(lane(out,ROWS.index((x,u,0,0,inp,w,g)))) for x,u,inp in product((0,1),repeat=3) for w,g in product(TRIPLES,repeat=2)]
  if site=='q2':continue
  by_u=[]
  for u in (0,1):
   candidates={}
   for w,g in product(TRIPLES,repeat=2):
    codes={0:set(),1:set()}
    for x,inp in product((0,1),repeat=2):
     if site=='qY' and inp!=x^u:continue
     codes[inp].add(code(lane(out,ROWS.index((x,u,0,0,inp,w,g)))))
    if all(len(v)==1 for v in codes.values()):
     pair=tuple(next(iter(codes[v])) for v in (0,1))
     if pair[0]!=pair[1]:candidates.setdefault(pair,[]).append((code(w),code(g)))
   by_u.append(candidates)
  common=sorted(set(by_u[0])&set(by_u[1]))
  encoding[site]=[{'codes':key,'u0_WG':by_u[0][key],'u1_WG':by_u[1][key]} for key in common]
 checks['W0_baseline_rows']=baseline_count
 checks['full_diagnostic_rows']=3*len(ROWS)
 checks['selector_mask_independence_rows']=3*len(ROWS)
 verdict={'native_common_two_code':'exists' if encoding['qY'] else 'excluded','q7_common_two_code_socket':'exists' if encoding['q7'] else 'excluded','reset_5_3_2':'not_constructed','full_public_record_law':'not_established_for_extension'}
 result={'schema':'oi.workspace-reset.v8','checks':checks,'ray_query_j_reduced':176,'encoding_candidates':encoding,'q8_table_order':'lexicographic (x,u,p,Wcode,Gcode), bits packed A*4+B*2+D; masks checked independent','q8_tables':tables,'verdict':verdict}
 print(json.dumps(result,sort_keys=True,separators=(',',':')))

if __name__=='__main__':main()
