"""Exact q7 incoming interface and initial-only q8 extension; stdout is JSON."""
from functools import lru_cache
from itertools import product
from pathlib import Path
import hashlib,json,sys
import inherited_model as m
sys.modules['model']=m
import inherited_correction_model as c

def need(ok,label):
 if not ok:raise RuntimeError(label)

def xor(*v):return m.X(*v)

TRIPLES=tuple(product((0,1),repeat=3))
UR=tuple((u,g) for u in (0,1) for g in TRIPLES)
UF=(1<<len(UR))-1
Q=(sum(u<<i for i,(u,g) in enumerate(UR)),0,UF)
C=(Q[0],0,Q[0])
G=tuple(sum(g[j]<<i for i,(u,g) in enumerate(UR)) for j in range(3))

@lru_cache(None)
def direct(t,a,b,n):
 if t<0 or min(a+b+abs(n+s) for s in (0,14,16))>t or (t-a-b-n)%2:return m.ZERO
 if t==0:return {(0,0,0):Q,(0,0,-14):C,(0,0,-16):G}.get((a,b,n),m.ZERO)
 terms=[]
 for axis in (0,1):
  for sign in (-1,1):
   ab=[a,b];ab[axis]+=sign;ab=sorted(map(abs,ab),reverse=True)
   terms.append(direct(t-1,*ab,n))
 terms.extend((direct(t-1,a,b,n-1),direct(t-1,a,b,n+1)))
 return xor(direct(t-2,a,b,n),m.H(xor(*terms)))

@lru_cache(None)
def upper_strip():
 L=16;BASE=m.BASE;values={}
 def get(ell,a,b,n):
  if ell<0:return m.ZERO
  a,b=sorted((abs(a),abs(b)),reverse=True)
  if a+b>ell or (ell-a-b)%2 or ell+a+b>L:return m.ZERO
  return values[ell,a,b][n]
 for ell,a,b in m.indices(L):
  cap=BASE+(L-ell)//2;arr=[direct(ell,a,b,0)];values[ell,a,b]=arr
  for n in range(1,cap+1):
   trans=xor(get(ell-1,a-1,b,n),get(ell-1,a+1,b,n),get(ell-1,a,b-1,n),get(ell-1,a,b+1,n))
   arr.append(xor(get(ell-2,a,b,n),m.H(xor(arr[n-1],get(ell-2,a,b,n+1),trans))))
 return values

ROWS=tuple((x,u,my,mr,p,g) for x,u,my,mr,p in product((0,1),repeat=5) for g in TRIPLES)
FULL=(1<<len(ROWS))-1
XM,UM,MY,MR,PM=tuple(sum(row[j]<<i for i,row in enumerate(ROWS)) for j in range(5))
def expand(v):
 return tuple(sum(((w>>(8*row[1]+TRIPLES.index(row[5])))&1)<<i for i,row in enumerate(ROWS)) for w in v)
def upper(t,v):
 a,b=sorted(map(abs,v[:2]),reverse=True);n=m.R-v[2];ell=t-n
 if ell<0 or a+b>ell or (ell-a-b)%2:return m.ZERO
 need(ell+a+b<=16,'upper strip covered')
 return expand(upper_strip()[ell,a,b][n-m.P])

def calc(site):
 end=(0,0,8)
 controls=[((0,-m.S,-m.d),XM),((0,m.S,-m.d),MY^MR),((m.T,m.P,-m.d),MY),((-m.T,m.P,-m.d),MR)]
 def base(t,v):
  val=upper(t,v)
  for pos,bits in controls:
   ds=tuple(abs(a-b) for a,b in zip(pos,v))
   if sum(ds)<=t:
    need(sum(ds)==t,'lower only first arrival before R')
    if m.odd(ds):val=xor(val,m.hp((0,bits,0),t))
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
   nxt[v]=xor(old[v],m.H(xor(*ns)))
  if tau==0:
   need(nxt[(0,0,0)]==(XM,FULL,XM^UM),'original qY intact')
   if site=='qY':nxt[(0,0,0)]=(XM,FULL,PM)
  if tau==2 and site=='q2':
   q=nxt[(0,0,2)]
   need(q==(XM^UM,XM^UM,FULL^(XM&(XM^UM))),'native q2 intact')
   nxt[(0,0,2)]=(PM,q[1],q[2])
  if tau==7 and site=='q7':
   need(nxt[(0,0,7)]==(0,0,XM^UM),'native clean q7 before intervention')
   nxt[(0,0,7)]=(0,0,PM)
  records[tau]=nxt;old,now=now,nxt
 return now[end],records

def lane(v,i):return tuple((w>>i)&1 for w in v)
def anf(values,names):
 co=list(values)
 for b in range(len(names)):
  for mask in range(len(co)):
   if mask&(1<<b):co[mask]^=co[mask^(1<<b)]
 return ['*'.join(names[b] for b in range(len(names)) if mask&(1<<b)) or '1' for mask,a in enumerate(co) if a]

def main():
 checks={}
 source=Path(__file__).parent
 hashes={f:hashlib.sha256((source/f).read_bytes()).hexdigest() for f in ('inherited_model.py','inherited_correction_model.py')}
 expected=json.loads((source/'PROVENANCE.json').read_text())['inherited_files']
 need(hashes==expected,'inherited hashes');checks['inherited_hashes']=True
 need(m.P%(12*840**16)==0,'actual P period');checks['actual_period_divisibility']=True
 data=upper_strip();count=0
 for (ell,a,b),arr in data.items():
  for n in range(6):
   need(arr[n]==direct(n+ell,a,b,n),'full tripole direct control');count+=16
 checks['direct_scalar_comparisons']=count
 # Independent dipole evaluator (all C values) at overlapping entries.
 dip=c.dipole_strip();comp=0
 for key,arr in dip.items():
  for n in (0,3,100,245):
   if n>=len(arr):continue
   for u in (0,1):
    want=lane(arr[n],8*u+5*u);got=lane(data[key][n],8*u)
    need(got==want,'G zero full dipole agreement');comp+=1
 checks['independent_dipole_comparisons']=comp
 q7=(0,m.S,m.d+7);q8=(0,m.S,m.d+8);q9=(0,m.S,m.d+9)
 N=m.R+7;f=(0,m.S,m.S+2*m.d+14);g=(0,m.S,m.S+2*m.d+16)
 D=lambda a,b:sum(abs(x-y) for x,y in zip(a,b))
 need(D(g,q7)==N+2 and D(g,q8)==N+1 and D(g,q9)==N,'G first arrival distances')
 centers=[((0,m.T,0),m.T),((m.T,0,0),m.T),((-m.T,0,0),m.T),((4*m.T,0,0),m.T),((0,0,-8*m.T),m.T),((0,m.S,0),m.S),((m.T,m.P,0),m.S),((-m.T,m.P,0),m.S),((4*m.T,m.P,0),m.S),((0,m.S,m.d),m.R),((0,m.S,-m.d),m.R),((0,m.S,m.d+2),m.R+2),((0,m.S,m.d+3),m.R+3),((12*m.R,0,0),m.R),((-12*m.R,0,0),m.R)]
 need(all(D(g,v)>N+1 for v,r in centers),'old receiver histories unaffected')
 need(all(D(g,v)>r for v,r in centers),'old ready balls exclude G')
 need(D(g,f)==2,'G source distinct from correction')
 checks['first_arrival_and_old_regions']=True
 # Adopt only this explicit depth8 candidate extension, with C and G kept.
 geo_paths=[]
 for parent in source.parents:
  geo_paths.extend(parent/sub for sub in ('parallel_v3/history_control/SOURCE-GEOMETRY.json','outward_v6_geometry/SOURCE-GEOMETRY.json','outward_v6/SOURCE-GEOMETRY.json'))
 gp=next((p for p in geo_paths if p.exists()),None)
 need(gp is not None,'inherited geometry available')
 need(hashlib.sha256(gp.read_bytes()).hexdigest()=='2642e1a68825faa5d3bb1049e8722adec1ec33bd3f56b9e4416b2c902a85ec5d','geometry digest')
 geo=json.loads(gp.read_text());arrivals=[]
 need(len(geo['sources'])==1479,'source count')
 for entry in geo['sources']:
  pos=tuple(entry['position']);dist=D(pos,q8)
  need(dist>=N+1,'no inherited source in added ready interior')
  need(pos!=g,'G overwrites no inherited source')
  if dist==N+1:arrivals.append((pos,entry['field'],entry['mask']))
 need(arrivals==[((0,0,0),1,64)],'only inherited origin boundary')
 lower=[(0,0,0),(0,2*m.S,0),(m.T,m.P+m.S,0),(-m.T,m.P+m.S,0)]
 up=(0,m.S,m.S+2*m.d)
 need(all(D(v,q8)==N+1 and D(v,up)==2*m.R for v in lower),'lower fronts and collision separation')
 need(D((0,0,0),q8)>N and D((0,m.S,-m.S-2*m.d),q8)>N+1,'old previous unknown and opposite reset excluded')
 need(m.d+8<m.T and 11*m.R-8>N+1,'finite and remote source exclusions')
 # Each near frontier coordinate below continues outward as j increases.
 frontier_bases=[((0,2*m.S,0),(0,1,0)),((m.T,m.P+m.S,0),(0,1,0)),((-m.T,m.P+m.S,0),(0,1,0)),((4*m.T,m.P+m.S,0),(0,1,0)),((0,0,0),(0,-1,0)),((0,0,-9*m.T),(0,0,-1))]
 for origin,step in frontier_bases:
  need(D(origin,q8)>=N+1,'frontier base outside/intersects ready boundary')
  test=tuple(a+b for a,b in zip(origin,step))
  need(D(test,q8)==D(origin,q8)+1,'frontier outward ray gives exact positive slope')
 checks['readiness_source_geometry_entries']=1479
 # Export the exact already-prepared incoming interface. No G reaches it.
 interface={}
 for site in ('qY','q2'):
  out,rec=m.calc(7,site);entry=[]
  for i,row in enumerate(m.ROWS):
   ns={}
   for axis in range(3):
    for sign in (-1,1):
     w=[0,0,7];w[axis]+=sign;w=tuple(w)
     value=rec[6][w]
     if w==(0,0,8):value=xor(value,(m.UM,0,m.UM))
     ns[','.join(map(str,w))]=lane(value,i)
   old=lane(rec[5][(0,0,7)],i)
   result=xor(old,m.H(xor(*ns.values())))
   x,u,my,mr,p=row
   want=(x&(1^u)&(1^p),(x^u)&(1^p),p) if site=='qY' else ((x^p)&(1^u),x^u^p,x^(x&u)^p^(x&p)^(x&u&p))
   need(result==want,'q7 actual incoming interface')
   entry.append({'row':row,'old_local':old,'incoming':ns,'endpoint':result})
  interface[site]=entry
 checks['actual_q7_interface_rows']=64
 results={};native_candidates={};socket_candidates={};raw_tables={};native_forms={};q7_formula_rows=0
 for site in ('qY','q2','q7'):
  out,rec=calc(site);entries=[]
  for i,row in enumerate(ROWS):
   x,u,my,mr,p,gv=row
   if site in ('qY','q2'):
    original=interface[site][m.ROWS.index(row[:5])]['endpoint']
    need(lane(rec[7][(0,0,7)],i)==tuple(original),'q7 invariant under G and extension')
   entries.append({'row':row,'q8':lane(out,i)})
  results[site]=entries
  if site=='q7':
   # Obtain the entire Q/C/G upper neighbor change at q9,N. It depends only u,G.
   upper_now=upper_strip()[16,0,0][244]
   for i,(x,u,my,mr,p,gv) in enumerate(ROWS):
    delta=xor(lane(upper_now,8*u+TRIPLES.index(gv)),lane(upper_now,8*u))
    a,b,cbit=delta
    want=(x^b,1^x^u^(x&u)^p^cbit,
          x^u^(x&u)^(p&(1^x^u))^a^(b&(x^u^(x&u)^p))^(cbit&(x^1^u))^(b&cbit))
    need(lane(out,i)==want,'full q7-input formula including actual old term')
    q7_formula_rows+=1
   for u in (0,1):
    socket_candidates[str(u)]=[gv for gv in TRIPLES if all(lane(out,i)==(0,p,0) for i,(x,uu,my,mr,p,gval) in enumerate(ROWS) if uu==u and gval==gv)]
  if site=='qY':
   for u in (0,1):
    native_candidates[str(u)]=[gv for gv in TRIPLES if all(lane(out,i)==(0,p,0) for i,(x,uu,my,mr,p,gval) in enumerate(ROWS) if uu==u and gval==gv and p==x^u)]
   # Whole q8 output as G varies for each fixed original diagnostic row.
   for row in m.ROWS:
    vals=[lane(out,ROWS.index(row+(gv,))) for gv in TRIPLES]
    need(len(set(vals))==8,'G to full q8 output permutation')
    raw_tables[','.join(map(str,row))]=vals
 checks['extension_diagnostic_rows']=3*len(ROWS)
 checks['G_endpoint_permutations']=32
 common={}
 for site in ('qY','q7'):
  candidates=[]
  for g0,g1 in product(TRIPLES,repeat=2):
   outputs={0:set(),1:set()}
   for ent in results[site]:
    x,u,my,mr,p,gv=ent['row']
    if gv!=(g0,g1)[u] or (site=='qY' and p!=x^u):continue
    outputs[p].add(ent['q8'])
   if all(len(v)==1 for v in outputs.values()) and outputs[0]!=outputs[1]:
    candidates.append({'G0':g0,'G1':g1,'codes':[list(outputs[p])[0] for p in (0,1)]})
  common[site]=candidates
 checks['apparatus_source_pairs_per_encoding_test']=64
 checks['q7_intervention_formula_rows']=q7_formula_rows
 # The native incoming interface has a compact exact description.
 for ent in interface['qY']:
  x,u,my,mr,p=ent['row']
  if p!=x^u:continue
  for key,val in ent['incoming'].items():
   if key=='0,0,6':want=(1^x,0,1^(x&u))
   elif key=='0,-1,7':want=(1^u,1,x&u)
   elif key=='-1,0,7':want=(1^u,1,u&mr)
   elif key=='1,0,7':want=(1^u,1,u&my)
   elif key=='0,1,7':want=(1^u,1,u&(my^mr))
   else:want=(1^u,1,0)
   need(val==want,'native incoming interface formula')
  need(ent['old_local']==(1,1,1),'native old local formula')
 checks['native_incoming_formula_rows']=16
 measurements={'native_route_G_by_u':native_candidates,'q7_socket_G_by_u':socket_candidates,'common_two_code_G_pairs':common}
 verdict={'unprepared_q8':'underdetermined_by_q7_ready_region','native_route_in_G_u_family':'exists' if all(native_candidates.values()) else 'excluded','q7_input_socket_in_G_u_family':'exists' if all(socket_candidates.values()) else 'excluded','reset_5_3_2':'not_constructed'}
 verdict['native_common_two_code_in_G_u_family']='exists' if common['qY'] else 'excluded'
 verdict['q7_common_two_code_socket_in_G_u_family']='exists' if common['q7'] else 'excluded'
 print(json.dumps({'schema':'oi.native-reset.q7-interface.v1','checks':checks,'measurements':measurements,'verdict':verdict,'q7_interface':interface,'q8_diagnostics':results,'q8_G_permutations':raw_tables},sort_keys=True,separators=(',',':')))

if __name__=='__main__':main()
