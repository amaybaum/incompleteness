from core import *
T=185;P=12*840**T;S=T+P;d=68;R=S+d
end=(0,0,2)
slots=[(R-2,v) for v in ball(2,end)]+[(R-1,v) for v in ball(3,end)]
def pattern(loc):
 out=0
 for i,(t,v) in enumerate(slots):
  ds=tuple(abs(a-b) for a,b in zip(v,loc))
  if sum(ds)==t and odd(ds):out|=1<<i
 return out
basis={}; examples={};patterns=set()
js=set(range(1024))|{2**k+j for k in range(R.bit_length()) for j in (-2,-1,0,1,2)}
for z in (1,2):
 radius=R+2-abs(z-2)
 for j in sorted(js):
  if not 0<=j<=radius:continue
  for sx,sy in ((1,1),(1,-1),(-1,1),(-1,-1)):
   loc=(sx*j,sy*(radius-j),z);p=pattern(loc);patterns.add(p);w=p
   while w:
    k=w.bit_length()-1
    if k in basis:w^=basis[k]
    else:
     basis[k]=w;examples[k]=(loc,p);break
print('patterns',len(patterns),'rank',len(basis))
for k,(loc,p) in examples.items():print(k, 'loc_small_x',loc[0] if abs(loc[0])<10000 else 'large','z',loc[2], 'pattern',hex(p))
import json
from pathlib import Path
Path('continuation/patterns.json').write_text(json.dumps({'basis':[hex(w) for w in basis.values()],'examples':[[list(loc),hex(p)] for loc,p in examples.values()],'count':len(patterns)}))
