"""item7-literal recount: case-sensitive literals over papers/*.md, book/*.md (top level)."""
import re, sys
sys.path.insert(0, __import__('os').path.dirname(__file__))
import rv_git as g
for name, c in (('T1p', g.T), ('H', g.H), ('E', g.E)):
    res = {}
    for lit in ('six structural', 'Fourteen', 'sixth of'):
        res[lit] = [(f, i) for f in g.corpus(c) for i, l in enumerate(g.lines(c, f), 1) if lit in l]
    a1 = [(f, i) for f in g.corpus(c) for i, l in enumerate(g.lines(c, f), 1) if re.search(r'\bA1\b', l)]
    print(name, {k: len(v) for k, v in res.items()}, 'A1', len(a1))
    for k, v in res.items():
        for f, i in v: print('  ', k, '|', f, i)
    if name == 'T1p':
        for f, i in a1: print('   A1 |', f, i)
