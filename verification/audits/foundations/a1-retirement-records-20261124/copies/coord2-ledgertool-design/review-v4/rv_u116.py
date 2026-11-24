"""Unheld p0+ext hit lines at T1' (content-held = equal to a site's pin text, or to a converted
`read` line, in the same file), the 84 among them, and how many of the rest equal an unheld H line."""
import sys, os, json, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rv_git as g, rv_hp as hp, rv_prof as pr
rows = g.load('rows.json')
def held_sets(scope):
    held = collections.defaultdict(set)
    for s in hp.SM:
        if s['line']:
            held[s['file'] if scope == 'file' else '*'].add(g.lines(g.E, s['file'])[s['line'] - 1])
    for r in rows['new_site_rules']:
        for k in r.get('read', []):
            f, _, ln = k.rpartition(':')
            held[f if scope == 'file' else '*'].add(g.lines(g.E, f)[int(ln) - 1])
    return held
s84 = {tuple(x) for x in json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'out-84.json')))}
for scope in ('file', 'global'):
    held = held_sets(scope)
    def unheld(c):
        out = {}
        for f in g.corpus(c):
            hs = held[f if scope == 'file' else '*']
            for i, l in enumerate(g.lines(c, f), 1):
                if l not in hs and pr.hits(l, pr.P0EXT):
                    out[(f, i)] = l
        return out
    UT, UH = unheld(g.T), unheld(g.H)
    uh_text = collections.defaultdict(set)
    for (f, i), l in UH.items(): uh_text[f].add(l)
    outside = {k: v for k, v in UT.items() if k not in s84}
    same = [k for k, v in outside.items() if v in uh_text[k[0]]]
    print(scope, 'unheld T1p', len(UT), '84 subset', s84 <= set(UT), 'outside', len(outside), 'identical-to-unheld-H', len(same), 'rest', len(outside) - len(same))
    if scope == 'file':
        rest = sorted(k for k in outside if outside[k] not in uh_text[k[0]])
        json.dump(rest, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'out-23.json'), 'w'))
