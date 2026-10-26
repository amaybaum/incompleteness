# usage: mapline.py OLDFILE NEWFILE line[-line] ...
import sys,difflib
a=open(sys.argv[1]).read().split('\n'); b=open(sys.argv[2]).read().split('\n')
m={}
sm=difflib.SequenceMatcher(None,a,b,autojunk=False)
for tag,i1,i2,j1,j2 in sm.get_opcodes():
    for k in range(i1,i2):
        if tag=='equal': m[k+1]=(j1+(k-i1)+1,'same')
        elif tag=='replace': m[k+1]=(j1+min(k-i1,j2-j1-1)+1,'CHANGED')
        else: m[k+1]=(j1+1,'DELETED')
for arg in sys.argv[3:]:
    lo,hi=(arg.split('-')+[arg])[:2]; lo,hi=int(lo),int(hi)
    r=[m.get(k,(None,'?')) for k in range(lo,hi+1)]
    st='same' if all(x[1]=='same' for x in r) else ','.join(sorted(set(x[1] for x in r)))
    print(f'{arg:>10} -> {r[0][0]}-{r[-1][0]}  {st}  | {b[r[0][0]-1][:110] if r[0][0] else ""}')
