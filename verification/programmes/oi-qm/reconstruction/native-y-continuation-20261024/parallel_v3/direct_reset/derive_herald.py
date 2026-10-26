import compiler as c
from itertools import product
from pathlib import Path
import json
u,v,k0,k1,k2=map(c.lit,range(5))
def AND(*a):return a[0] if len(a)==1 else c.AND(a[0],AND(*a[1:]))
def OR(*a):return a[0] if len(a)==1 else c.OR(a[0],OR(*a[1:]))
low5=OR(c.NOT(k2),AND(c.NOT(k1),c.NOT(k0)))
low3=AND(c.NOT(k2),OR(c.NOT(k1),c.NOT(k0)))
low2=AND(c.NOT(k2),c.NOT(k1))
f=OR(AND(c.NOT(u),c.NOT(v),low5),AND(u,c.NOT(v),low3),AND(u,v,low2))
prog=c.program(f,c.target(f,4))
L=((len(prog)+13)//12)*12
while L-2-len(prog)<6:L+=12
padded=c.pad(prog,L-2)+((0,()),)
T,sources=c.realize({1:padded})
if T!=L:raise RuntimeError('bad deadline')
print('word',len(prog),'L',L,'sources',len(sources),flush=True)
Path(__file__).with_name('herald.json').write_text(json.dumps({'word_length':len(prog),'deadline':L,'program':padded,'sources':[[list(p),field,mask] for (p,field),mask in sorted(sources.items())]},separators=(',',':'))+'\n')
