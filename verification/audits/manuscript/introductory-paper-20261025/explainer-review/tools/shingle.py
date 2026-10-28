import re,sys,glob,os
src=sys.argv[1]
def words(t):
    t=re.sub(r'\$[^$]*\$',' ',t)
    return re.findall(r"[a-z0-9]+",t.lower())
K=5
corpus=set()
files=[f for f in glob.glob(src+'/book/*.md')+glob.glob(src+'/papers/*.md') if not f.endswith('Explainer.md')]
for f in files:
    w=words(open(f).read())
    for i in range(len(w)-K+1): corpus.add(tuple(w[i:i+K]))
lines=open(src+'/Explainer.md').read().split('\n')
# sections by heading
secs=[];cur=None
for i,l in enumerate(lines,1):
    if l.startswith('#'):
        cur=[l,i,i,[]];secs.append(cur)
    elif cur: cur[2]=i;cur[3].append(l)
for h,s,e,body in secs:
    w=words('\n'.join(body))
    sh=[tuple(w[i:i+K]) for i in range(len(w)-K+1)]
    if not sh: continue
    hit=sum(1 for x in sh if x in corpus)
    print(f"{s:5d}-{e:5d} {len(w):5d}w  overlap {hit/len(sh):5.2f}  {h[:70]}")
