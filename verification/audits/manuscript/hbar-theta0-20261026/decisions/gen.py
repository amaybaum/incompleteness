import sys,collections,re
sys.path.insert(0,'.')
from entries import E
ROOT='../snap/'
FULL=open(ROOT+'book/The-Incompleteness-of-Observation-FULL.md',encoding='utf-8').read().split('\n')
cache={}
def lines(f):
    if f not in cache: cache[f]=open(ROOT+f,encoding='utf-8').read().split('\n')
    return cache[f]
errs=[]; out={}
byline=collections.defaultdict(list)
for g,i,f,n,o,nw in E:
    L=lines(f)[n-1]
    c=L.count(o)
    if c!=1: errs.append(f"{i} {f}:{n} old occurs {c}x")
    full=''
    if f.startswith('book/') and f!='book/README.md':
        m=[k+1 for k,x in enumerate(FULL) if x==L]
        full=','.join(map(str,m)) if m else 'NONE'
        if len(m)!=1: errs.append(f"{i} FULL match {m}")
    out[i]=(g,f,n,full,o,nw)
    byline[(f,n,g[:2] if g.startswith('O') else 'N')].append((L.find(o),L.find(o)+len(o),i))
# overlap check within same line among N + each single option
for (f,n,grp),lst in byline.items():
    lst.sort()
    for a,b in zip(lst,lst[1:]):
        if a[1]>b[0] and not grp.startswith('O'): errs.append(f"overlap {a[2]} {b[2]}")
print("ERRORS:",errs if errs else "none", file=sys.stderr)
import json; json.dump(out,open('out.json','w'),ensure_ascii=False,indent=0)
# cross overlap: every pair on same line not both from mutually exclusive options of same decision
items=[(i,)+v for i,v in out.items()]
def span(i):
    g,f,n,full,o,nw=out[i]; L=lines(f)[n-1]; a=L.find(o); return f,n,a,a+len(o),g
ex=[]
ids=list(out)
for x in range(len(ids)):
    for y in range(x+1,len(ids)):
        f1,n1,a1,b1,g1=span(ids[x]); f2,n2,a2,b2,g2=span(ids[y])
        if (f1,n1)!=(f2,n2): continue
        same_dec = g1.startswith('O') and g2.startswith('O') and g1[:2]==g2[:2] and g1!=g2
        if a1<b2 and a2<b1 and not same_dec: ex.append((ids[x],ids[y]))
print("CROSS-OVERLAPS:",ex if ex else "none", file=sys.stderr)
