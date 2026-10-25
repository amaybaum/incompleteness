"""Signed transverse native upper strip for the fixed64 affine controller family."""
import argparse,importlib.util,sys,json,hashlib
from pathlib import Path
from itertools import product
from functools import lru_cache
ap=argparse.ArgumentParser();ap.add_argument('--source-root',type=Path,default=Path(__file__).resolve().parent.parent.parent)
ap.add_argument('--symmetric',action='store_true')
args=ap.parse_args();root=args.source_root.resolve()
spec=importlib.util.spec_from_file_location('v9',root/'reset_v9/checks.py');v=importlib.util.module_from_spec(spec);saved_argv=sys.argv;sys.argv=[str(root/'reset_v9/checks.py'),'--source-root',str(root)];spec.loader.exec_module(v);sys.argv=saved_argv
m=v.m;X=m.X;H=m.H;ZERO=m.ZERO;need=v.need;TR=v.TR
MINUS=TR if args.symmetric else ((0,0,0),)
UR=tuple((u,a,b,c,k,km) for u,a,b in product((0,1),repeat=3) for c,k,km in product(TR,TR,MINUS));UF=(1<<len(UR))-1
U=sum(u<<i for i,(u,a,b,c,k,km) in enumerate(UR));Q=(U,0,UF);C0=(U,0,U);G=(U,UF^U,UF)
J=tuple(sum(((u^a,a,u^a)[f]^((a^b)&c[f]))<<i for i,(u,a,b,c,k,km) in enumerate(UR)) for f in range(3))
K=tuple(sum(((a^b)&k[f])<<i for i,(u,a,b,c,k,km) in enumerate(UR)) for f in range(3))
KM=tuple(sum(((a^b)&km[f])<<i for i,(u,a,b,c,k,km) in enumerate(UR)) for f in range(3))
SOURCES={(-1,0,-17):KM,(0,0,0):Q,(0,0,-14):C0,(0,0,-16):G,(0,0,-18):J,(1,0,-17):K}
@lru_cache(None)
def direct(t,x,y,n):
 if t<0 or min(abs(x-a)+abs(y-b)+abs(n-c) for a,b,c in SOURCES)>t or (t-x-y-n)%2:return ZERO
 if t==0:return SOURCES.get((x,y,n),ZERO)
 ns=[direct(t-1,x-1,y,n),direct(t-1,x+1,y,n),direct(t-1,x,abs(y-1),n),direct(t-1,x,y+1,n),direct(t-1,x,y,n-1),direct(t-1,x,y,n+1)]
 return X(direct(t-2,x,y,n),H(X(*ns)))
@lru_cache(None)
def strip():
 L=18;values={}
 def get(ell,x,y,n):
  y=abs(y)
  if ell<0 or abs(x)+y>ell or (ell-abs(x)-y)%2 or ell+abs(x)+y>L:return ZERO
  return values[ell,x,y][n]
 for ell in range(L+1):
  for x in range(-ell,ell+1):
   for y in range(ell-abs(x)+1):
    if (ell-abs(x)-y)%2 or ell+abs(x)+y>L:continue
    arr=[direct(ell,x,y,0)];values[ell,x,y]=arr
    for n in range(1,m.BASE+(L-ell)//2+1):
     side=X(*(get(ell-1,x+dx,y+dy,n) for dx,dy in ((-1,0),(1,0),(0,-1),(0,1))))
     arr.append(X(get(ell-2,x,y,n),H(X(arr[n-1],get(ell-2,x,y,n+1),side))))
 return values
ROWS=tuple((x,u,my,mr,a,b,c,k,km) for x,u,my,mr,a,b in product((0,1),repeat=6) for c,k,km in product(TR,TR,MINUS))
FULL=(1<<len(ROWS))-1
XM,UM,MY,MR=tuple(sum(r[f]<<i for i,r in enumerate(ROWS)) for f in range(4))
URINDEX={row:i for i,row in enumerate(UR)}
def lane(q,i):return tuple((w>>i)&1 for w in q)
def code(q):return 4*q[0]+2*q[1]+q[2]
@lru_cache(None)
def expand(q):
 return tuple(sum(((w>>URINDEX[u,a,b,c,k,km])&1)<<i for i,(x,u,my,mr,a,b,c,k,km) in enumerate(ROWS)) for w in q)
@lru_cache(None)
def upper(t,p):
 x,y,n=p[0],abs(p[1]),m.R-p[2];ell=t-n
 if ell<0 or abs(x)+y>ell or (ell-abs(x)-y)%2:return ZERO
 need(ell+abs(x)+y<=18,'signed upper budget')
 return expand(strip()[ell,x,y][n-m.P])
CONTROLS=[((0,-m.S,-m.d),XM),((0,m.S,-m.d),MY^MR),((m.T,m.P,-m.d),MY),((-m.T,m.P,-m.d),MR)]
def base(t,p):
 out=upper(t,p)
 for pos,bits in CONTROLS:
  ds=tuple(abs(a-b) for a,b in zip(pos,p))
  if sum(ds)<=t:
   need(sum(ds)==t,'lower first front')
   if m.odd(ds):out=X(out,m.hp((0,bits,0),t))
 if t==m.R-1 and p in v.RAYS:
  j,level=v.RAYS[p]
  expected=m.hp((0,XM,0),t) if m.odd((0,m.S+p[1],m.d+p[2])) else ZERO
  need(out==expected,'lower origin-only entry')
  out=tuple(sum(v.raypair(x,j)[level][f]<<i for i,(x,u,my,mr,a,b,c,k,km) in enumerate(ROWS)) for f in range(3))
 return out

def compute(force_p=None):
 end=(0,0,9);old={p:base(m.R-2,p) for p in m.ball(9,end)};now={p:base(m.R-1,p) for p in m.ball(10,end)}
 for tau in range(10):
  nxt={}
  for p in m.ball(9-tau,end):
   ns=[now[tuple(p[f]+(sgn if f==axis else 0) for f in range(3))] for axis in range(3) for sgn in (-1,1)]
   nxt[p]=X(old[p],H(X(*ns)))
  if tau==7:need(nxt[(0,0,7)]==(0,0,XM^UM),'q7 preserved')
  if tau==8:
   need(nxt[(0,0,8)]==(0,XM^UM,0),'q8 preserved')
   if force_p is not None:nxt[(0,0,8)]=(0,FULL*force_p,0)
  old,now=now,nxt
 return now[end]
def main():
 prov=json.loads((Path(__file__).resolve().parent/'PROVENANCE.json').read_text())
 need(all(hashlib.sha256((root/n).read_bytes()).hexdigest()==h for n,h in prov['files'].items()),'inherited source digests')
 need(m.P%(12*840**18)==0,'actual signed-strip period')
 data=strip();direct_count=baseline_count=0
 for (ell,x,y),arr in data.items():
  for n in range(3):need(arr[n]==direct(n+ell,x,y,n),'signed cluster direct control');direct_count+=len(UR)
  key=(ell,*sorted((abs(x),y),reverse=True))
  for n in (0,3,245):
   if n>=len(arr):continue
   for u,a,b in product((0,1),repeat=3):
    i=URINDEX[u,a,b,(0,0,0),(0,0,0),(0,0,0)];j=code((u^a,a,u^a))
    need(lane(arr[n],i)==v.lane(v.strip4()[key][n],8*u+j),'K0 C0 baseline strip');baseline_count+=1
 D=lambda a,b:sum(abs(x-y) for x,y in zip(a,b));q9=(0,m.S,77);N=m.R+9;kpos=(1,m.S,m.S+153);jpos=(0,m.S,m.S+154)
 need(D(kpos,q9)==D(jpos,q9)==N,'new source first arrival')
 need(D(kpos,(0,m.S,76))==N+1,'K excluded from q8 read')
 centers=[((0,m.T,0),m.T),((m.T,0,0),m.T),((-m.T,0,0),m.T),((4*m.T,0,0),m.T),((0,0,-8*m.T),m.T),((0,m.S,0),m.S),((m.T,m.P,0),m.S),((-m.T,m.P,0),m.S),((4*m.T,m.P,0),m.S),((0,m.S,68),m.R),((0,m.S,-68),m.R),((0,m.S,70),m.R+2),((0,m.S,71),m.R+3),((12*m.R,0,0),m.R),((-12*m.R,0,0),m.R),((0,m.S,75),m.R+7),((0,m.S,76),m.R+8)]
 need(all(D(kpos,c)>t for c,t in centers),'K outside prior ready balls')
 geo=json.loads((root/'parallel_v3/history_control/SOURCE-GEOMETRY.json').read_text())
 need(all(tuple(e['position'])!=kpos for e in geo['sources']),'K no inherited source overwrite')
 # All six declared public-bank rays have x in {0,+T,-T,4T}; K.x=1.
 need(kpos[0] not in (0,m.T,-m.T,4*m.T),'K not a public-bank position')
 kmpos=(-1,m.S,m.S+153)
 need(D(kmpos,q9)==N and all(D(kmpos,c)>t for c,t in centers),'Kminus old-ready geometry')
 need(kmpos[0] not in (0,m.T,-m.T,4*m.T) and all(tuple(e['position'])!=kmpos for e in geo['sources']),'Kminus bank/source exclusion')
 lower=[(0,0,0),(0,2*m.S,0),(m.T,m.P+m.S,0),(-m.T,m.P+m.S,0),(0,-76,76)]
 need(all(D(z,src)>=2*m.R for z in lower for src in (kpos,kmpos,jpos)),'no premature upper/lower coupling')
 out=compute();rowindex={r:i for i,r in enumerate(ROWS)};records=[];passing=[];passing_all=[];raw=[];k_effect=0
 for c,k,km in product(TR,TR,MINUS):
  bad=[];badaccepted=[];mask_dependence=0
  for x,u,my,mr,a,b in product((0,1),repeat=6):
   got=lane(out,rowindex[x,u,my,mr,a,b,c,k,km]);want=(0,x^u^a,x^u^b)
   if got!=want:
    bad.append([x,u,my,mr,a,b,code(got),code(want)])
    if (a,b)!=(0,1):badaccepted.append(bad[-1])
   if got!=lane(out,rowindex[x,u,0,0,a,b,c,k,km]):mask_dependence+=1
   if a==b:need(got==(0,x^u^a,x^u^a),'equal-mask positive control')
   if got!=lane(out,rowindex[x,u,my,mr,a,b,c,(0,0,0),(0,0,0)]):k_effect+=1
  records.append({'C':code(c),'V':code(k),'Vminus':code(km),'selector_mask_dependence_rows':mask_dependence,'accepted_mismatch_rows':len(badaccepted),'all_mismatch_rows':len(bad),'first_accepted_counterexample':badaccepted[0] if badaccepted else None})
  if not badaccepted:passing.append([code(c),code(k),code(km)])
  if not bad:passing_all.append([code(c),code(k),code(km)])
 for row in ROWS:raw.append(code(lane(out,rowindex[row])))
 need(k_effect>0,'additional source has nonvacuous physical effect')
 if args.symmetric:
  single=json.loads((Path(__file__).resolve().parent/'single-result.json').read_text())
  subset=''.join(format(code(lane(out,i)),'x') for i,row in enumerate(ROWS) if row[-1]==(0,0,0))
  need(subset==single['q9_table_hex'],'all single-K rows preserved')
 interventions=[];failure_rows=[]
 if passing:
  for ccode,kcode,kmcode in passing:
   c,k,km=TR[ccode],TR[kcode],TR[kmcode]
   for x,u,my,mr in product((0,1),repeat=4):failure_rows.append({'candidate':[ccode,kcode,kmcode],'x':x,'u':u,'mY':my,'mR':mr,'a':0,'b':1,'raw':lane(out,rowindex[x,u,my,mr,0,1,c,k,km])})
  for pp in (0,1):
   changed=compute(pp)
   for ccode,kcode,kmcode in passing:
    c,k,km=TR[ccode],TR[kcode],TR[kmcode];bad=[]
    for x,u,my,mr,a,b in product((0,1),repeat=6):
     if (a,b)==(0,1):continue
     got=lane(changed,rowindex[x,u,my,mr,a,b,c,k,km]);want=(0,pp^a,pp^b)
     if got!=want:bad.append([x,u,my,mr,a,b,code(got),code(want)])
    interventions.append({'candidate':[ccode,kcode,kmcode],'p':pp,'mismatch_rows':len(bad),'first_counterexample':bad[0] if bad else None})
 result={'q8_interventions':interventions,'failure_pattern01_raw':failure_rows,'schema':'oi.branch.native-controller.v10','symmetric':args.symmetric,'candidate_count':len(TR)*len(TR)*len(MINUS),'checks':{'signed_upper_direct_scalar':direct_count,'axis_baseline_scalar':baseline_count,'full_diagnostic_rows':len(ROWS),'K_effect_rows':k_effect,'K_old_ready_exclusion':True,'K_bank_coordinate_exclusion':True},'candidate_row_fields':['C','V','Vminus','accepted_mismatch_rows','all_mismatch_rows','selector_mask_dependence_rows','first_accepted_counterexample'],'candidate_results':[[z[f] for f in ['C','V','Vminus','accepted_mismatch_rows','all_mismatch_rows','selector_mask_dependence_rows','first_accepted_counterexample']] for z in records],'accepted_three_mask_witnesses':passing,'all_four_mask_witnesses':passing_all,'table_order':'x,u,mY,mR,a,b,Ccode,Vpluscode,Vminuscode; all selector masks retained','q9_table_hex':''.join(format(z,'x') for z in raw),'verdict':{'fixed512_affine_family' if args.symmetric else 'fixed64_affine_family':'exists' if passing else 'excluded','full_reset':'not_constructed','two_slice_access':'not_adopted'}}
 print(json.dumps(result,sort_keys=True,separators=(',',':')))
if __name__=='__main__':main()
