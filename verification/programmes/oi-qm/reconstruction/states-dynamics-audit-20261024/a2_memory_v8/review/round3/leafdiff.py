"""Reviewer leaf diff of two result.json files (identity paths). Usage: python3 -I -B leafdiff.py old new"""
import json, sys
def leaves(x, p=()):
    if isinstance(x, dict):
        if not x: yield p, {}
        for k, v in x.items(): yield from leaves(v, p + (k,))
    elif isinstance(x, list):
        if not x: yield p, []
        for i, v in enumerate(x): yield from leaves(v, p + (i,))
    else: yield p, x
O = dict(leaves(json.load(open(sys.argv[1])))); N = dict(leaves(json.load(open(sys.argv[2]))))
ch = [p for p in O if p in N and O[p] != N[p]]; rm = [p for p in O if p not in N]; ad = [p for p in N if p not in O]
print('old', len(O), 'new', len(N), 'changed', len(ch), 'removed', len(rm), 'added', len(ad))
for p in ch: print('CHANGED', '/'.join(map(str, p)), '|', str(O[p])[:70], '->', str(N[p])[:70])
for p in rm: print('REMOVED', '/'.join(map(str, p)))
for p in ad: print('ADDED', '/'.join(map(str, p)), '=', str(N[p])[:60])
