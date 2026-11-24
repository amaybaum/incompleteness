"""D3: HP context-structure-changed items at H = LIST/TABLE sites (sec. 4.2 definitions, pin line at E)
unique at E and H, whose neighbour context or structure context changed E..H, not meaning-context FAILs.
Also the RET count over sites unique at H and T1'."""
import sys, os, re, json, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rv_git as g, rv_hp as hp
src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'rv_ctx_v4.py')).read().split("rates = collections.Counter()")[0]
ns = {'__file__': __file__}; exec(src, ns)
items = {'EH': [], 'HT': []}
for k, s in enumerate(hp.SM):
    f = s['file']; pin = g.lines(g.E, f)[s['line'] - 1]
    if not (ns['is_list'](pin) or ns['TABLE'].match(pin)): continue
    sc = ns['list_ctx'] if ns['is_list'](pin) else ns['table_ctx']
    pos = {}
    for n, c in (('E', g.E), ('H', g.H), ('T', g.T)):
        L = g.lines(c, f); o = [i for i, l in enumerate(L) if l == pin]
        if len(o) == 1: pos[n] = (L, o[0])
    for seg, (a, b) in (('EH', ('E', 'H')), ('HT', ('H', 'T'))):
        if a in pos and b in pos:
            (La, ia), (Lb, ib) = pos[a], pos[b]
            cch = ns['ctx'](La, ia) != ns['ctx'](Lb, ib)
            if (cch or sc(La, ia) != sc(Lb, ib)) and not (ns['MEAN_TRUE'](s['s3']) and cch):
                items[seg].append('%s:%d%s' % (f, s['line'], '' if 'T' in pos else ' (not unique at T1p)'))
for seg, v in items.items(): print(seg, len(v), v)
