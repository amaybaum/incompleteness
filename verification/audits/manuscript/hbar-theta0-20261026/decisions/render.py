import json,re,sys
out=json.load(open('out.json',encoding='utf-8'))
def blk(i):
    g,f,n,full,o,nw=out[i]
    fl=f" [FULL:{full}]" if full and full!='NONE' else (" (not mirrored in FULL)" if f=='book/README.md' else "")
    return f"**{i}** `{f}:{n}`{fl}\n```text\nOLD: {o}\nNEW: {nw}\n```\n"
def ids_for(groups): return [i for i,v in out.items() if v[0] in groups]
t=open('template.md',encoding='utf-8').read()
def sub(m):
    spec=m.group(1)
    if spec.startswith('GROUP:'): ids=ids_for(spec[6:].split(','))
    else: ids=spec.split(',')
    return '\n'.join(blk(i) for i in ids)
t=re.sub(r'\{\{([^}]+)\}\}',sub,t)
open('../../DECISIONS.md','w',encoding='utf-8').write(t)
print(len(t))
