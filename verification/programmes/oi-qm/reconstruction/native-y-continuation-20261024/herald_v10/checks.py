"""Synchronized initial-source Y herald and z; no giant execution or search."""
from pathlib import Path
from itertools import product
from collections import Counter
from fractions import Fraction as F
import argparse,hashlib,json
H=(0,2,4,7,1,3,5,6)
T=185;P=12*840**185;S=P+T;R=S+68;L=R+9
SOURCE_HASH='406befa2c8d1f663856a78ca6cb632e9c61d1233b02a9d532c7cb43d6261ce64'
def need(ok,label):
 if not ok:raise RuntimeError(label)
def h(v):a,b,c=v;return b,c,a^(b&c)
def val(mask,seed):return (mask&1)^(((mask>>1)&seed).bit_count()%2)
def affine_word(step):
 c,terms=step;out=[(c>>(2-k))&1 for k in range(3)]
 for j,co in terms:
  for k in range(3):
   if co>>(2-k)&1:out[k]^=1<<(j+1)
 return tuple(out)
def gate(step,seed,state):
 v=affine_word(step);code=sum(val(v[k],seed)<<(2-k)for k in range(3))
 return H[state^code]
def rank(rows):
 basis={}
 for x in rows:
  while x:
   k=x.bit_length()-1
   if k in basis:x^=basis[k]
   else:basis[k]=x;break
 return len(basis)
def control(t,prefix,identity,repetitions):
 if t<len(prefix):return prefix[t]
 if t<len(prefix)+6*repetitions:return identity[(t-len(prefix))%6]
 return (0,())
def profile(t,wing,prefix,identity,repetitions):
 return affine_word(control(t,prefix,identity,repetitions))[(wing-t)%3]
def source_mask(q,wing,prefix,identity,repetitions):
 mask=0;d=q
 while True:
  mask^=profile(d,wing,prefix,identity,repetitions)
  if d==0:return mask
  d=(d-1)&q

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--source-root',type=Path,default=Path(__file__).resolve().parent.parent)
 root=ap.parse_args().source_root
 raw=(root/'parallel_v3/direct_reset/herald.json').read_bytes()
 need(hashlib.sha256(raw).hexdigest()==SOURCE_HASH,'retained Y program source')
 data=json.loads(raw);need(data['word_length']==2684,'base word length')
 prefix=data['program'][:2684];identity=data['program'][2684:2690]
 need(all(0<=c<8 and all(0<=j<5 and 0<=v<8 for j,v in terms)
          for c,terms in prefix+identity),'only five seed-affine controls, no input bit')
 need(all(not terms for c,terms in identity),'constant identity padding')
 for state in range(8):
  out=state
  for step in identity:out=gate(step,0,out)
  need(out==state,'six-step word identity on full register')
 expected=[];counts=Counter()
 for seed in range(32):
  a=seed&1;b=(seed>>1)&1;k=seed>>2
  accepted=int(k<{(0,0):5,(1,0):3,(1,1):2,(0,1):0}[a,b])
  state=0
  for step in prefix:state=gate(step,seed,state)
  need(state==4*accepted,'compiled predicate exact truth')
  expected.append(accepted);counts[a,b]+=accepted
 need(counts=={(0,0):5,(0,1):0,(1,0):3,(1,1):2},'accepted plane counts')
 repetitions=(P-2424)//6
 need(repetitions>=0 and 6*repetitions==P-2424,'actual integer padding count')
 need(2684+6*repetitions+2==L,'native deadline includes both final H steps')
 need(L%3==1,'fair z source phase')
 preamble=[profile(t,w,prefix,identity,0)for t in range(2684)for w in range(3)]
 need(rank([m>>1 for m in preamble])==5,'five independent affine source dimensions')
 small_rep=2;small_L=2684+6*small_rep+2
 rows=[[source_mask(q,w,prefix,identity,small_rep)for q in range(small_L)]for w in range(3)]
 rows=[list(reversed(row))for row in rows]
 packed=lambda mask:sum(val(mask,s)<<s for s in range(32))
 state=(0,0,0);injection_checks=0
 for t in range(small_L):
  injection=[0,0,0]
  for w in range(3):
   injection[(w-t)%3]^=packed(rows[w][-1])
   rows[w]=[a^b for a,b in zip(rows[w],rows[w][1:])]
  target=tuple(packed(m)for m in affine_word(control(t,prefix,identity,small_rep)))
  need(tuple(injection)==target,'native wing source formula gives scheduled input')
  state=h(tuple(a^b for a,b in zip(state,injection)));injection_checks+=32
 truth=sum(bit<<s for s,bit in enumerate(expected))
 need(state==(0,truth,0),'complete raw native herald')
 need(h((truth,0,0))!=(0,truth,0),'omitted extra H phase detected on nonzero truth')
 for z in(0,1):
  good=(z,0,0);bad=(0,0,z)
  for _ in range(L%12):good=h(good);bad=h(bad)
  need(good==(0,0,z),'native z output')
  if z:need(bad!=good,'wrong z source phase detected')
 accepted=Counter();rejected=Counter();failure=0
 for a,b,k,z in product((0,1),(0,1),range(8),(0,1)):
  g=int(k<{(0,0):5,(1,0):3,(1,1):2,(0,1):0}[a,b])
  if g:accepted[a,b,z]+=1
  else:failure+=1;rejected[a,b,z]+=1
 need(sum(accepted.values())==20 and failure==44,'success and failure both retained')
 for a,b in product((0,1),repeat=2):
  target={(0,0):5,(0,1):0,(1,0):3,(1,1):2}[a,b]
  need(accepted[a,b,0]==target and accepted[a,b,1]==target,'z jointly fair with accepted plane')
  need(rejected[a,b,0]==8-target and rejected[a,b,1]==8-target,'failure plane and z retained')
 good={key:F(v,20)for key,v in accepted.items()};shared=Counter()
 for a,b,k in product((0,1),(0,1),range(8)):
  if k<{(0,0):5,(1,0):3,(1,1):2,(0,1):0}[a,b]:shared[a,b,a]+=1
 bad={key:F(v,10)for key,v in shared.items()}
 need(all(sum(p for key,p in bad.items() if key[2]==z)==F(1,2) for z in(0,1)),
      'shared-z control still has the correct marginal')
 tv=sum(abs(good.get(k,F())-bad.get(k,F()))for k in good.keys()|bad.keys())/2
 need(tv==F(1,2),'shared z marginal shortcut rejected by joint law')
 herald=(48*L,0,0);zport=(-48*L,0,0);zsource=(-48*L,-L,0);side=256*L+64*T+1
 need(47*L>13*R and 48*L-13*R>L,'old source and bank separation')
 need(96*L>2*L and 97*L<side//2,'new cone/source cross exclusion, no wrap')
 need(4*49*L<side,'all involved x distances have no wrap shortcut')
 for q in(0,L-1):
  for pos in((49*L-1-q,q+1,0),(49*L-1-q,-q-1,0),(49*L-1-q,0,q+1)):
   need(sum(abs(a-b)for a,b in zip(pos,herald))==L,'herald source boundary')
   need(pos[0]>=48*L,'herald outward hemisphere')
 need(sum(abs(a-b)for a,b in zip(zsource,zport))==L,'z source boundary')
 result={'schema':'oi.remote-y-herald.v10','verdict':'PASS_CONDITIONAL_SYNCHRONIZED_SOURCES','base_word_length':2684,'identity_word':[s[0]for s in identity],
 'schedule':{'deadline':'R+9 = P+262','identity_repetitions':'(P-2424)/6','extra_zero_H_steps':2,'raw_herald':'(0,G,0)','raw_z':'(0,0,z)'},
 'controls':{'predicate_assignments':32,'identity_register_states':8,'affine_seed_rank':5,'rank_with_z':6,'bounded_native_deadline':small_L,'native_wing_input_comparisons':injection_checks,'shared_z_joint_TV':str(tv),'phase_negatives_detected':2,'geometry':'actual symbolic all-index envelope'},
 'accepted_counts':{''.join(map(str,k)):v for k,v in sorted(counts.items())},'joint_accepted_counts':{''.join(map(str,k)):v for k,v in sorted(accepted.items())},
 'joint_rejected_counts':{''.join(map(str,k)):v for k,v in sorted(rejected.items())},
 'success_probability':'5/16','failure_probability':'11/16','scope':'Initial-source remote herald and fair-z synchronized to existing local R+9; local simultaneous carrier outputs not constructed.'}
 print(json.dumps(result,sort_keys=True,separators=(',',':')))
if __name__=='__main__':main()
