import json,sys,re
def norm(x):
    s=json.dumps(x,sort_keys=True,default=str)
    s=re.sub(r'<tmp>/[^"\s,]*','<P>',s)
    s=re.sub(r'\b\d+\.\d+ ?s\b','<T>',s)
    return s
def load(p):
    d=json.load(open(p)); return {c['id']:c for c in d['controls']}
a=load(sys.argv[1]); b=load(sys.argv[2])
print('ids', len(a), len(b), 'only-a', sorted(set(a)-set(b)), 'only-b', sorted(set(b)-set(a)))
st=[k for k in a if k in b and a[k]['status']!=b[k]['status']]
print('status diffs', st)
ad=[k for k in a if k in b and norm(a[k]['actual'])!=norm(b[k]['actual'])]
print('actual diffs', len(ad), ad[:40])
from collections import Counter; print(Counter(c['status'] for c in b.values()))
