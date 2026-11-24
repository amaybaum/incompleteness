"""HP walk per DESIGN-v4 sec. 3.2 (reviewer's implementation from the text), and RET overlap
per sec. 3.4/5 (region-attributed). Writes out-hp.json."""
import sys, os, json, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rv_git as g
chain = g.git('rev-list', '--first-parent', '--reverse', '%s..%s' % (g.E, g.H)).split()
parents = {c: g.git('rev-parse', c + '^1').strip() for c in chain}
SM = g.load('sitemap.json')['sites']
LED = g.load('ledger.json')

def occ(block, L):
    n = len(block); out = []
    if n == 0: return out
    for i in range(len(L) - n + 1):
        if L[i:i + n] == block: out.append(i)
    return out

def trim(b):
    while b and not b[0].strip(): b = b[1:]
    while b and not b[-1].strip(): b = b[:-1]
    return b

def walk(site):
    f = site['file']; Lp0 = g.lines(g.E, f)
    region = [Lp0[site['line'] - 1]]
    steps = []
    for c in chain:
        p = parents[c]
        Lp, Lc = g.lines(p, f), g.lines(c, f)
        if Lp == Lc:
            continue
        op, oc = occ(region, Lp), occ(region, Lc)
        if len(op) == 1 and len(oc) == 1:
            continue
        if len(op) != 1:
            return {'status': 'ambiguous', 'steps': steps}
        k = op[0]; n = len(region)
        cntp = collections.Counter(Lp); cntc = collections.Counter(Lc)
        up = None
        for j in range(k - 1, -1, -1):
            if cntp[Lp[j]] == 1 and cntc[Lp[j]] == 1: up = j; break
        lo = None
        for j in range(k + n, len(Lp)):
            if cntp[Lp[j]] == 1 and cntc[Lp[j]] == 1: lo = j; break
        uc = Lc.index(Lp[up]) if up is not None else -1
        lc = Lc.index(Lp[lo]) if lo is not None else len(Lc)
        if uc >= lc:
            return {'status': 'ambiguous', 'steps': steps}
        pre = trim(Lp[(up if up is not None else -1) + 1: (lo if lo is not None else len(Lp))])
        post = trim(Lc[uc + 1: lc])
        steps.append({'commit': c, 'pre': pre, 'post': post})
        region = post
        if not region:
            return {'status': 'removed', 'steps': steps, 'region': []}
    return {'status': 'changed' if steps else 'unchanged', 'steps': steps, 'region': region}

def line_spans(text):
    spans = []; pos = 0
    for l in text.split('\n'):
        spans.append((pos, pos + len(l.encode('utf-8')))); pos += len(l.encode('utf-8')) + 1
    return spans

def overlaps(sp, a, b):
    s, e = sp['start'], sp['end']
    if s == e:
        return a < s < b
    return s < b and e > a

if __name__ == '__main__':
    splices = collections.defaultdict(list)
    for s in LED['splices']: splices[s['file']].append(s)
    res = []
    for idx, s in enumerate(SM):
        w = walk(s)
        rec = {'idx': idx, 'file': s['file'], 'line': s['line'], 'status': w['status'], 'nsteps': len(w['steps']),
               'first': w['steps'][0]['commit'] if w['steps'] else None}
        if w['status'] == 'changed':
            LH = g.lines(g.H, s['file']); o = occ(w['region'], LH)
            rec['unique_at_H'] = len(o) == 1
            if len(o) == 1:
                spans = line_spans(g.text(g.H, s['file']))
                a = spans[o[0]][0]; b = spans[o[0] + len(w['region']) - 1][1]
                rec['H_lines'] = [o[0] + 1, o[0] + len(w['region'])]
                rec['region_hash'] = hash(tuple(w['region']))
                rec['overlap'] = sorted(sp['id'] for sp in splices[s['file']] if overlaps(sp, a, b))
        res.append(rec)
    hp = [r for r in res if r['status'] in ('changed', 'removed', 'ambiguous')]
    print('HP sites', len(hp), collections.Counter(r['status'] for r in hp))
    print('unique at H', sum(1 for r in hp if r.get('unique_at_H')))
    print('multi-step', [(r['file'], r['line']) for r in hp if r['nsteps'] > 1])
    subj = {c: g.git('log', '-1', '--format=%s', c).strip()[:60] for c in chain}
    print('first-change', collections.Counter(subj[r['first']] for r in hp))
    ov = [r for r in hp if r.get('overlap')]
    print('HP sites overlapped', len(ov), 'distinct splices', len(set(x for r in ov for x in r['overlap'])))
    shared = collections.defaultdict(list)
    for r in hp:
        if r.get('region_hash') is not None: shared[(r['file'], tuple(r['H_lines']))].append((r['file'], r['line']))
    print('shared regions', [v for v in shared.values() if len(v) > 1])
    json.dump(res, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'out-hp.json'), 'w'), indent=0)
