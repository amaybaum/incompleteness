# usage: shingle_range.py SRCFILE START END CORPUSGLOB... ; prints 5-shingle overlap of SRCFILE[START..END] vs corpus, and per-paragraph
import re,sys,glob
src,s,e=sys.argv[1],int(sys.argv[2]),int(sys.argv[3])
files=[f for g in sys.argv[4:] for f in glob.glob(g)]
def words(t):
    t=re.sub(r'\$[^$]*\$',' ',t)
    return re.findall(r"[a-z0-9]+",t.lower())
K=5;corpus=set()
for f in files:
    if f==src: continue
    w=words(open(f).read())
    for i in range(len(w)-K+1): corpus.add(tuple(w[i:i+K]))
lines=open(src).read().split('\n')
def ov(t):
    w=words(t);sh=[tuple(w[i:i+K]) for i in range(len(w)-K+1)]
    return (sum(x in corpus for x in sh)/len(sh) if sh else float('nan')),len(w)
print('files',len(files),'range',s,e,'overlap %.2f (%dw)'%ov('\n'.join(lines[s-1:e])))
for i in range(s,e+1):
    l=lines[i-1]
    if l.strip():
        o,n=ov(l); print(f'  {i:5d} {n:4d}w {o:5.2f}  {l[:70]}')
