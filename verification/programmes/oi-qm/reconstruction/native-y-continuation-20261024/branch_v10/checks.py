"""Finite affine-source audit of the actual native q9 table; no surrogate law."""
import argparse,hashlib,json
from pathlib import Path
from itertools import product
ap=argparse.ArgumentParser();ap.add_argument('--source-root',type=Path,default=Path(__file__).resolve().parent.parent)
p=ap.parse_args().source_root.resolve();T=185;P=12*840**185;S=T+P;R=S+68;N=R+9

def need(ok,msg):
 if not ok:raise RuntimeError(msg)
def bits(n):return (n>>2,(n>>1)&1,n&1)
def code(t):return 4*t[0]+2*t[1]+t[2]
def main():
 raw=(p/'reset_v9/result.json').read_bytes();d=json.loads(raw)
 manifest=(p/'reset_v9/SHA256SUMS').read_text().splitlines()
 digest=next(line.split()[0] for line in manifest if line.split()[1]=='result.json')
 need(hashlib.sha256(raw).hexdigest()==digest,'source table checksum')
 t=d['q9_tables']['native'];table={};k=0
 for x,u,q,j in product((0,1),(0,1),(0,1),range(8)):table[x,u,q,j]=t[k];k+=1
 need(all(table[x,u,0,j]==table[x,u,1,j] for x,u,j in product((0,1),(0,1),range(8))),'native diagnostic p absent')
 out=lambda x,u,j:table[x,u,0,j]
 need(all(len({out(x,u,j) for j in range(8)})==8 for x,u in product((0,1),repeat=2)),'J output permutations')
 common={}
 for j0,j1 in product(range(8),repeat=2):
  pair0=tuple(out(y,0,j0) for y in (0,1));pair1=tuple(out(y^1,1,j1) for y in (0,1))
  if pair0==pair1:common[j0,j1]=pair0
 groups={delta:[] for delta in range(8)}
 for (j0,j1),pair in common.items():groups[j0^j1].append({'J0':j0,'J1':j1,'codes':pair})
 affine_valid3=[];affine_valid4=[];common_affine=0;maximum=0
 for c,cu,ca,cb in product(range(8),repeat=4):
  vals={};valid=True
  for aa,bb in product((0,1),repeat=2):
   j0=c^(ca if aa else 0)^(cb if bb else 0);j1=j0^cu
   if (j0,j1) not in common:valid=False;break
   vals[aa,bb]=common[j0,j1]
  if not valid:continue
  common_affine+=1
  count=min(len({vals[ab][y] for ab in ((0,0),(1,0),(1,1))}) for y in (0,1));maximum=max(maximum,count)
  if count==3:affine_valid3.append([c,cu,ca,cb])
  if all(len({v[y] for v in vals.values()})==4 for y in (0,1)):affine_valid4.append([c,cu,ca,cb])
 # Stronger accepted-only family: failure mask01 unconstrained.
 accepted_only=[]
 for c,cu,ca,cb in product(range(8),repeat=4):
  vals=[]
  for aa,bb in ((0,0),(1,0),(1,1)):
   j0=c^(ca if aa else 0)^(cb if bb else 0)
   if (j0,j0^cu) not in common:break
   vals.append(common[j0,j0^cu])
  if len(vals)==3 and all(len({v[y] for v in vals})==3 for y in (0,1)):accepted_only.append([c,cu,ca,cb])
 truth={};cases=[]
 for u,aa,bb in product((0,1),repeat=3):
  matches=[j for j in range(8) if all(out(y^u,u,j)==code((0,y^aa,y^bb)) for y in (0,1))]
  need(len(matches)==1,'unique two-sign control table');truth[u,aa,bb]=matches[0]
  cases.append({'u':u,'a':aa,'b':bb,'J':bits(matches[0])})
 anf=[]
 for field in range(3):
  cs=[bits(truth[i&1,(i>>1)&1,(i>>2)&1])[field] for i in range(8)]
  for bit in range(3):
   for i in range(8):
    if i&(1<<bit):cs[i]^=cs[i^(1<<bit)]
  anf.append([i for i,c in enumerate(cs) if c])
 degree=max(i.bit_count() for terms in anf for i in terms)
 need(degree>1,'nonaffine target detected')
 # Existing one-mask route must be accepted by the same source table.
 for x,u,aa in product((0,1),repeat=3):need(out(x,u,code((u^aa,aa,u^aa)))==code((0,x^u^aa,x^u^aa)),'one-mask positive control')
 need(len(common)==8 and maximum==2,'common-code capacity')
 need(not affine_valid3 and not affine_valid4 and not accepted_only,'affine three-mask exclusion')
 # Exact shallow branch source ownership. These are distances, not dynamics.
 targets={'A':(-1,S,76),'B':(0,S-1,76),'C':(0,S,77)}
 sources={'A':(-S-78,S,76),'B':(0,-78,76),'C':(0,S,S+154)}
 D=lambda a,b:sum(abs(x-y) for x,y in zip(a,b))
 cross={a:{b:D(src,t)-N for b,t in targets.items()} for a,src in sources.items()}
 need(all(cross[a][b]==(0 if a==b else 2) for a,b in product(targets,repeat=2)),'separate control cones')
 centers=[((0,T,0),T),((T,0,0),T),((-T,0,0),T),((4*T,0,0),T),((0,0,-8*T),T),((0,S,0),S),((T,P,0),S),((-T,P,0),S),((4*T,P,0),S),((0,S,68),R),((0,S,-68),R),((0,S,70),R+2),((0,S,71),R+3),((12*R,0,0),R),((-12*R,0,0),R),((0,S,75),R+7),((0,S,76),R+8),((0,S,77),N)]
 margins={a:min(D(src,c)-r for c,r in centers) for a,src in sources.items()}
 # C is the existing source and exactly on the q9 boundary; A/B are outside.
 need(all(v>=0 for v in margins.values()),'no source pins in old ready interiors')
 positive_x=(S+78,S,76);positive_margin=D(positive_x,(4*T,P,0))-S
 need(positive_margin<0,'positive-x ready-conflict control')
 older={'origin':(0,0,0),'W':(0,-76,76),'selector_R':(-T,P+S,0),'selector_R_bank1':(-T,P+S+1,0),'selector_R_bank2':(-T,P+S+2,0)}
 arrivals={name:{a:D(src,t)-N for a,t in targets.items()} for name,src in older.items()}
 need(arrivals['selector_R']['A']==-2 and arrivals['selector_R_bank1']['A']==-1 and arrivals['selector_R_bank2']['A']==0,'side-branch coupled frontier obligation')
 need(arrivals['origin']['B']==-2 and arrivals['W']['B']==-2,'backward-y lag obligation')
 result={'schema':'oi.simultaneous-branch.control-v10','source_result_sha256':digest,'affine_sources_examined':4096,'common_affine_sources':common_affine,'max_distinct_accepted_mask_codes':maximum,'affine_three_mask_solutions':affine_valid3,'affine_four_mask_solutions':affine_valid4,'accepted_only_affine_solutions':accepted_only,'common_code_groups_by_u_coefficient':groups,'nonlinear_required_J':cases,'J_anf_monomial_bitmasks_u_a_b':anf,'J_boolean_degree':degree,'geometry':{'cross_arrival_minus_N':cross,'minimum_old_ready_margins':margins,'positive_x_conflict_margin':positive_margin,'older_source_arrival_minus_N':arrivals},'verdict':{'affine_single_source_three_masks':'excluded','nonlinear_two_slice_truth_table':'exists_not_natively_supplied','same_tick_spatial_branches':'not_constructed','full_reset':'not_constructed'}}
 print(json.dumps(result,indent=2,sort_keys=True))
if __name__=='__main__':main()
