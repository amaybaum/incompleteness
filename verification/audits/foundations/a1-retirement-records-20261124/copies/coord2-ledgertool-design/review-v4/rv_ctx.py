"""Context changes (sec. 4), the 12 meaning-context failures, S0 indicators (sec. 4.2) and indicator
items (sec. 4.3), implemented by the reviewer from the design text."""
import sys, os, re, json, collections, hashlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rv_git as g, rv_hp as hp
P0 = {s['id']: s for s in g.load('sites.json')['sites']}
MEAN_TRUE = lambda v: v.startswith('not determined') or v.startswith('per unit')
def ctx(L, i):  # i 0-based
    a = next((L[j] for j in range(i - 1, -1, -1) if L[j].strip()), 'BOF')
    b = next((L[j] for j in range(i + 1, len(L)) if L[j].strip()), 'EOF')
    return (a, b)
def strip(l):
    l = l.lstrip()
    l = re.sub(r'^(?:>\s*)+', '', l)
    l = re.sub(r'^#{1,6}\s*', '', l, count=1)
    l = re.sub(r'^(?:[-*+]|\d+[.)])\s*', '', l, count=1)
    l = re.sub(r'^[*_]+', '', l)
    return l
ANAPH = re.compile(r'^(This|These|Such|Hence|Thus|It|Under this)\b')
LIST1 = re.compile(r'^\s*(>\s*)*([-*+]|\d+[.)])\s+')
LIST2 = re.compile(r'^\s*(>\s*)*(([-*+]|\d+[.)])\s+)?[*_]{0,2}\(\s*([A-Z]{1,3}\d{1,2}[a-z]?|[ivx]{1,4})\s*\)')
TABLE = re.compile(r'^\s*\|')
def is_list(l): return bool(LIST1.match(l) or LIST2.match(l))
def ws(s): return ' '.join(s.split())
def list_ctx(L, i):
    j = i - 1
    while j >= 0 and (not L[j].strip() or is_list(L[j])): j -= 1
    lead = L[j] if j >= 0 else 'BOF'
    k = i + 1
    while k < len(L) and (not L[k].strip() or is_list(L[k])): k += 1
    trail = L[k] if k < len(L) else 'EOF'
    sib = [L[x] for x in range(j + 1, k) if x != i and L[x].strip()]
    return json.dumps([lead, sib, trail], sort_keys=True)
def table_ctx(L, i):
    a = i
    while a - 1 >= 0 and TABLE.match(L[a - 1]): a -= 1
    b = i
    while b + 1 < len(L) and TABLE.match(L[b + 1]): b += 1
    header = L[a]
    cap_above = next((L[j] for j in range(a - 1, -1, -1) if L[j].strip()), 'BOF')
    nb = next((L[j] for j in range(b + 1, len(L)) if L[j].strip()), '')
    cap_below = nb if (nb.startswith('Table:') or nb.startswith(': ')) else ''
    return json.dumps([header, cap_above, cap_below], sort_keys=True)
rates = collections.Counter(); ind = {}
for k, s in enumerate(hp.SM):
    pin = g.lines(g.E, s['file'])[s['line'] - 1]
    d = {'anaph': bool(ANAPH.match(strip(pin))), 'list': is_list(pin), 'table': bool(TABLE.match(pin)),
         'partial': s['p0_id'] in P0 and ws(P0[s['p0_id']]['quote']) != ws(pin)}
    ind[k] = d
    for x, v in d.items(): rates[x] += v
print('rates of 697', dict(rates))
changes = []; items = []
for k, s in enumerate(hp.SM):
    f = s['file']; pin = g.lines(g.E, f)[s['line'] - 1]
    Ls = {n: g.lines(c, f) for n, c in (('E', g.E), ('H', g.H), ('T', g.T))}
    pos = {}
    for n, L in Ls.items():
        o = [i for i, l in enumerate(L) if l == pin]
        if len(o) != 1: break
        pos[n] = o[0]
    if len(pos) != 3: continue
    c = {n: ctx(Ls[n], pos[n]) for n in pos}
    segs = [seg for seg, (a, b) in (('EH', ('E', 'H')), ('HT', ('H', 'T'))) if c[a] != c[b]]
    if segs:
        changes.append((k, segs))
    # indicator items
    for seg, (a, b) in (('EH', ('E', 'H')), ('HT', ('H', 'T'))):
        sc = None
        if ind[k]['list']: sc = list_ctx
        elif ind[k]['table']: sc = table_ctx
        if sc and (c[a] != c[b] or sc(Ls[a], pos[a]) != sc(Ls[b], pos[b])) and not (MEAN_TRUE(s['s3']) and c[a] != c[b]):
            items.append((seg, '%s:%d' % (f, s['line']), 'list' if ind[k]['list'] else 'table'))
print('changes', len(changes), collections.Counter(tuple(x[1]) for x in changes))
ch_rates = collections.Counter()
for k, segs in changes:
    for x, v in ind[k].items(): ch_rates[x] += v
print('indicator among changes', dict(ch_rates))
marked = [(segs, hp.SM[k]['file'], hp.SM[k]['line'], hp.SM[k]['s3']) for k, segs in changes if MEAN_TRUE(hp.SM[k]['s3'])]
for seg in ('EH', 'HT'):
    m = [(f, l) for segs, f, l, s3 in marked if seg in segs]
    print('meaning-context failures', seg, len(m), m)
nd = [x for x in marked if x[3].startswith('not determined')]
print('not-determined only:', collections.Counter(s for x in nd for s in x[0]))
anaph_fail = [(hp.SM[k]['file'], hp.SM[k]['line']) for k, segs in changes if ind[k]['anaph']]
print('ANAPH failures', anaph_fail)
print('indicator items', items)
print('s3 categories', collections.Counter('visible' if s['s3'].startswith('visible') else 'n/a' if s['s3'] == 'n/a' else 'nd' if s['s3'].startswith('not det') else 'pu' for s in hp.SM))
