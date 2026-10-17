"""Exploratory: tree closures of the cited commits/trees, by file extension (for the withholding policy)."""
import collections, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gitobj import Store, parse_tree, parse_commit
W = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'work')
src = Store(os.path.join(W, 'src.git'))
main = set(l.strip() for l in open(os.path.join(W, 'main-objects.txt')))
U = json.load(open(os.path.join(W, 'union-stage1.json')))['objects']
RESEARCH = {'4dc0321ca2aac6f6aca6f55efc90b7f51330334a', '5f4089a4500a59943c33ba13656b2530824068c5',
            '78aa5b25415cf1cd26994cb2280343ab86cd72d9', '8508d17278ea11b90fd37d137172e18a25b3835f',
            '9430c4635c34ef8f252176925201737a6966235d', 'a163b9246a98ef100cbf256e51b00e39a1fc564a',
            'e7d380fcb9881e3063243aaa149e85be3cd0a914'}
def walk(tree, prefix, out):
    if tree in main: return
    t, data = src.read(tree)
    out.setdefault(tree, ('tree', prefix or '/'))
    for mode, name, oid in parse_tree(data):
        p = prefix + name
        if mode == '40000': walk(oid, p + '/', out)
        elif mode == '160000': continue
        elif oid not in main: out.setdefault(oid, ('blob', p))
ext = collections.Counter(); extb = collections.Counter(); objs = {}
for oid, r in U.items():
    if oid in RESEARCH: continue
    if r['type'] == 'commit':
        tree, parents, hdr, msg = parse_commit(src.read(oid)[1]); walk(tree, '', objs)
    elif r['type'] == 'tree':
        walk(oid, '', objs)
for oid, (t, p) in objs.items():
    if t != 'blob': continue
    e = os.path.splitext(p)[1] or '(none)'; ext[e] += 1; extb[e] += src.check(oid)[1]
print(len(objs), sum(1 for v in objs.values() if v[0]=='tree'), 'trees')
for e, n in ext.most_common(): print(f'{e:12} {n:5} {extb[e]:>10}')
big = sorted(((src.check(o)[1], p) for o, (t, p) in objs.items() if t == 'blob'), reverse=True)[:25]
for s, p in big: print(s, p)
print('----')
for oid, (t, p) in sorted(objs.items(), key=lambda x: x[1][1]):
    if t == 'blob' and os.path.splitext(p)[1] in ('.log', '.out', '.txt', '.pdf', ''):
        print(oid[:10], src.check(oid)[1], p)
