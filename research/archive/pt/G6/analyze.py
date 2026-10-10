#!/usr/bin/env python3
"""G6 analyze.py -- items 1-3 of PROTOCOL-STAGE6-AMENDMENT-1 A1.4 over graph.tsv (read-only; stdout only).

Run from pt/G6/ as `python3 -I -B analyze.py`. Inputs: graph.tsv, parse.out (titles, statuses, bridge fields).
RULES (NOTES N1-N3, fixed before the first run):
  dependency edges = R, RA, RN, KC (Y only in the robustness control); seeds = I3.1, I3.6, I3.7, I3.11, I3.43,
  I3.147-I3.153; Anc(P) = nodes reachable from a seed (seeds included); Desc(AX) = nodes from which I1.1 or
  I1.2 is reachable (I1.1, I1.2 included). Do-not-assume set = rows flagged DNA in graph.tsv together with the
  step-1 lists (I2: I2.3, I2.29-I2.35, I2.62, I2.63, I2.69; I3: I3.137, I3.142, I3.144, I3.150-I3.155).
  A discharge clause is a sentence of a do-not-assume record's status that names a kernel theorem and an
  object ('for', 'discharg', 'satisf', 'realiz', 'refuted', 'holds', 'proved', 'implied', 'equivalent').
DECISION RULE (fixed before the first run):
  A1  meeting: report MEET-K if Anc(P) and Desc(AX) share a node reachable from AX through within-level and
      kernel-supplied cross-level edges only; MEET-MS if they share a node only through manuscript-asserted
      cross-level edges; NO-MEET if they share no node. Computed with and without Y edges.
  A2  countercontrol: with one synthetic edge I3.1 -> I1.1 added, the same computation must return a meeting
      (MEET-K or MEET-MS); with the synthetic edge absent the result is reported as computed.
  A3  every seed is present in graph.tsv and every do-not-assume id of the step-1 lists is present.
  A line 'VERDICT ANALYSIS COMPLETE' prints only if A2 and A3 pass (A1 is a measurement, not a pass/fail).
AMENDMENT before run 3 (18:18Z; run 2 kept as analyze.run2.*; run 1 was the same script on the graph of
  classify run 2 and its output was overwritten by run 2; rules A1-A3 unchanged): the discharge extraction
  read any word before '(' as a theorem name. It now takes a theorem cited as '(name, File.lean:n)' or
  '(name, :n)' or 'name (File.lean:n)' / 'name (:n)', the clause text before it as the object, and, for a
  theorem with no record, the heads of its declared arguments at L (read from the kernel) as its premises.
  Users of each do-not-assume item are intersected with Anc(P).
"""
import re

SEEDS = ['I3.1', 'I3.6', 'I3.7', 'I3.11', 'I3.43', 'I3.147', 'I3.148', 'I3.149', 'I3.150', 'I3.151', 'I3.152',
         'I3.153']
DNA_LISTS = ['I2.3'] + ['I2.%d' % k for k in range(29, 36)] + ['I2.62', 'I2.63', 'I2.69', 'I3.137', 'I3.142',
                                                               'I3.144'] + ['I3.%d' % k for k in range(150, 156)]
DEPK = ('R', 'RA', 'RN', 'KC')
OBL = {
    'I3.1': 'K2 (I3.165): two-copy local tomography, the carrier W d',
    'I3.43': 'K2 (hadm: products in K, K within maxCone)', 'I3.147': 'K2 (hadm (a): products in K)',
    'I3.131': 'P-STAGE2 (I3.145)', 'I3.148': 'P-ACT2 (I3.146)', 'I3.132': 'P-ACT2 (I3.146)',
    'I3.149': 'none at L (no ROADMAP row; dualW/ipW/Q3 design-only, AUDIT-I 5.4)',
    'I3.150': 'K2 local actions + K-inf-Act I3.168 / K-inf-Drive I3.169',
    'I3.151': 'K2 local actions + K-inf-Act I3.168 / K-inf-Drive I3.169',
    'I3.152': 'K2 local actions + K-inf-Act I3.168 / K-inf-Drive I3.169',
    'I3.153': 'K2 local actions + K-inf-Act I3.168 / K-inf-Drive I3.169',
    'I3.137': 'K2 local actions (IE1 unsourced)',
    'I3.8': 'K1 I3.164 (selector); P-ACT2 (gate as pair operation)',
    'I3.9': 'K1 I3.164 (selector); P-ACT2 (gate as pair operation)',
    'I3.23': 'K1 I3.164 (selector); P-ACT2', 'I3.29': 'K1 I3.164 (selector); P-ACT2',
    'I3.48': 'K-inf (I3.166, effect soundness)', 'I3.73': 'K-inf-Seed I3.171', 'I3.74': 'K-inf-Act I3.168',
    'I3.75': 'K-inf-V4 I3.172', 'I3.76': 'K-inf-Trans I3.170', 'I3.66': 'K-inf-Drive I3.169',
    'I3.92': 'K-inf-Stage I3.167', 'I3.94': 'K-inf-Stage I3.167', 'I3.96': 'K-inf-Stage I3.167',
    'I3.99': 'K-inf-Act I3.168', 'I3.114': 'K2 (COMP-1 adapter to W d open)',
    'I3.115': 'K2 (COMP-1 adapter to W d open)', 'I3.116': 'K2 (COMP-1 adapter to W d open)'}


ANCP = set()
KDIR = '../base/verification/lean-mathlib/OIBridge'


def kernel_heads(name, loc):
    import os
    files = sorted(x for x in os.listdir(KDIR) if x.endswith('.lean'))
    want = loc.split(':')[0]
    for f in ([want] if want else []) + files:
        if f not in files:
            continue
        lines = open(os.path.join(KDIR, f), encoding='utf-8').read().split('\n')
        for j, ln in enumerate(lines):
            if re.match(r'^\s*(?:private\s+|protected\s+)?(?:theorem|lemma)\s+' + re.escape(name) + r'(?![\w\'.])', ln):
                txt = ' '.join(lines[j:j + 30]).split(':=')[0]
                after = txt[txt.index(name) + len(name):]
                heads, depth, cur, k = [], 0, '', 0
                while k < len(after):
                    c = after[k]
                    if c in '({[⦃':
                        if depth == 0:
                            cur = ''
                        depth += 1
                    elif c in ')}]⦄':
                        depth -= 1
                        if depth == 0:
                            ty = cur.split(':', 1)[1] if ':' in cur else cur
                            mh = re.match(r"^[¬(\s]*([A-Za-z_][A-Za-z0-9_'.]*)", ty.strip())
                            heads.append(mh.group(1) if mh else ty.strip()[:30])
                    elif depth == 0 and c == ':':
                        break
                    elif depth > 0:
                        cur += c
                    k += 1
                return '%s:%d %s' % (f, j + 1, ', '.join(heads) or '(none: closed statement)')
    return 'declaration not found at L'


def load():
    nodes, order, edges, sec = {}, [], [], None
    for ln in open('graph.tsv', encoding='utf-8').read().split('\n'):
        if ln.startswith('#table nodes'):
            sec = 'n'
            continue
        if ln.startswith('#table edges'):
            sec = 'e'
            continue
        if not ln or ln.startswith('#'):
            continue
        f = ln.split('\t')
        if sec == 'n' and f[0] != 'id' and len(f) == 12:
            nodes[f[0]] = dict(zip(['id', 'kind', 'status', 'level', 'cls', 'sub', 'deps', 'named', 'flag',
                                    'derived', 'needs', 'ext'], f))
            order.append(f[0])
        elif sec == 'e' and f[0] != 'src' and len(f) == 6:
            edges.append(tuple(f))
    meta = {}
    for ln in open('parse.out', encoding='utf-8').read().split('\n'):
        f = ln.split('\t')
        if f[0] == 'N' and len(f) == 12:
            meta[f[1]] = dict(title=f[2], status=f[5], bridge=f[9], bearing=f[10], level=f[4])
    return nodes, order, edges, meta


def span(level):
    return set(c for c in 'HOPMGX' if c in level.split('(')[0])


def adj(edges, kinds, extra=()):
    fwd, rev = {}, {}
    for (s, d, k, xl, sup, note) in list(edges) + list(extra):
        if k not in kinds:
            continue
        fwd.setdefault(s, set()).add((d, xl, sup))
        rev.setdefault(d, set()).add((s, xl, sup))
    return fwd, rev


def reach(start, g, allow=lambda xl, sup: True):
    seen, stack = set(start), list(start)
    while stack:
        x = stack.pop()
        for (y, xl, sup) in g.get(x, ()):
            if y not in seen and allow(xl, sup):
                seen.add(y)
                stack.append(y)
    return seen


def meeting(edges, nodes, kinds, extra=()):
    fwd, rev = adj(edges, kinds, extra)
    anc = reach(SEEDS, fwd)
    desc_all = reach(['I1.1', 'I1.2'], rev)
    desc_k = reach(['I1.1', 'I1.2'], rev, lambda xl, sup: xl != '1' or sup == 'K')
    both_all = anc & desc_all
    both_k = anc & desc_k
    verdict = 'MEET-K' if both_k else ('MEET-MS' if both_all else 'NO-MEET')
    return verdict, anc, desc_all, desc_k, both_all


def main():
    nodes, order, edges, meta = load()
    names = {}
    for ln in open('parse.out', encoding='utf-8').read().split('\n'):
        f = ln.split('\t')
        if f[0] == 'M' and len(f) == 3:
            names.setdefault(f[1], []).append(f[2])
    ok = {}
    ok['A3'] = all(s in nodes for s in SEEDS) and all(d in nodes for d in DNA_LISTS)
    # ---- S1 partition
    print('== S1 partition')
    cnt = {}
    for i in order:
        n = nodes[i]
        cnt.setdefault(n['cls'], []).append(i)
    for c in 'abcde':
        print('class %s: %d' % (c, len(cnt.get(c, []))))
    for i in order:
        n = nodes[i]
        if n['cls'] in 'ab':
            print('S1a/b %s\t%s/%s\t%s\tneeds: %s\text: %s' % (i, n['cls'], n['sub'], n['level'][:30], n['needs'][:300],
                                                              n['ext'][:120]))
    freq = {}
    for i in order:
        n = nodes[i]
        if n['cls'] in 'cd':
            for part in n['needs'].split(' ; '):
                if part.startswith('OPER=') or part.startswith('PHYS='):
                    cat = part[:4]
                    for r in part[5:].split(','):
                        if re.match(r'^I[1-4]\.\d+$', r):
                            freq.setdefault((n['cls'], cat, r), 0)
                            freq[(n['cls'], cat, r)] += 1
    for (c, cat, r), v in sorted(freq.items(), key=lambda x: (-x[1], x[0])):
        if v >= 3:
            print('S1root\tclass %s\t%s\t%s\t%d items\t%s' % (c, cat, r, v, meta[r]['title'][:70]))
    for i in order:
        n = nodes[i]
        if n['cls'] in 'cd':
            roots = []
            for part in n['needs'].split(' ; '):
                if part[:5] in ('OPER=', 'PHYS='):
                    ids = [r for r in part[5:].split(',') if re.match(r'^I[1-4]\.\d+$', r)]
                    txt = [r for r in part[5:].split(',') if not re.match(r'^I[1-4]\.\d+$', r)]
                    roots.append('%s=%s%s' % (part[:4], ','.join(ids), (' +%d named' % len(txt)) if txt else ''))
            cs = [p.split('=')[0] for p in n['needs'].split(' ; ') if re.match(r'^C[1-4]=', p)]
            print('S1c/d %s\t%s\t%s\t%s\t%s' % (i, n['cls'], n['level'][:25], ' ; '.join(roots), ','.join(cs)))
    for i in order:
        n = nodes[i]
        if n['cls'] == 'e':
            print('S1e %s\t%s\t%s' % (i, n['sub'], meta[i]['title'][:60]))
    # ---- S2 do-not-assume
    print('== S2 do-not-assume')
    dna = [i for i in order if nodes[i]['flag'] == 'DNA' or i in DNA_LISTS]
    fwd, rev = adj(edges, DEPK)
    ANCP.update(reach(SEEDS, fwd))
    for i in dna:
        st = meta[i]['status']
        users = sorted(s for (s, xl, sup) in rev.get(i, ()) if nodes[s]['derived'] == 'derived')
        print('S2 %s\t%s\tclass %s/%s\tstatus: %s' % (i, meta[i]['title'][:70], nodes[i]['cls'], nodes[i]['sub'],
                                                     st[:420]))
        for m in re.finditer(r'([^;()]*?)\(?`?([A-Za-z_][A-Za-z0-9_\'.]*)`?,?\s*\(?((?:[A-Za-z]+\.lean)?:\d+)\)', st):
            clause, t, loc = m.group(1).strip(' ,;'), m.group(2), m.group(3)
            if not re.search(r'_|[a-z][A-Z]', t):
                continue
            rid = [r for r in names.get(t, []) if r != i]
            if rid:
                r = rid[0]
                prem = nodes[r]['deps'] or '(none)'
                print('S2d %s\t[%s] %s (%s) -> %s [%s/%s]\tpremises: %s' % (i, clause[-90:], t, loc, r, nodes[r]['cls'],
                                                                       nodes[r]['sub'], prem[:220]))
            else:
                print('S2d %s\t[%s] %s (%s) -> no record\tdeclared arguments: %s' % (i, clause[-90:], t, loc,
                                                                                 kernel_heads(t, loc)))
        print('S2u %s\tappears as a hypothesis of %d derived nodes: %s' % (i, len(users), ' '.join(users[:25])))
        print('S2p %s\tof which in Anc(P): %s' % (i, ' '.join(sorted(set(users) & ANCP)) or 'none'))
    # ---- S3 meeting
    print('== S3 ancestor / descendant')
    v0, anc, dall, dk, both = meeting(edges, nodes, DEPK)
    vy, ancy, dally, dky, bothy = meeting(edges, nodes, DEPK + ('Y',))
    syn = [('I3.1', 'I1.1', 'R', '1', 'K', 'synthetic')]
    vs, _, _, _, _ = meeting(edges, nodes, DEPK, syn)
    ok['A2'] = vs in ('MEET-K', 'MEET-MS')
    print('S3 verdict (R,RA,RN,KC): %s; with Y: %s; countercontrol with synthetic I3.1->I1.1: %s' % (v0, vy, vs))
    print('S3 Anc(P): %d nodes; Desc(AX): %d nodes (%d through kernel-supplied or within-level edges); '
          'shared: %d; with Y: Anc %d, Desc %d, shared %d' % (len(anc), len(dall), len(dk), len(both), len(ancy),
                                                             len(dally), len(bothy)))
    for i in order:
        if i in anc:
            n = nodes[i]
            print('S3anc %s\t%s\t%s\t%s\t%s' % (i, n['level'][:20], n['derived'], n['cls'] + '/' + n['sub'],
                                               meta[i]['title'][:60]))
    for i in order:
        if i in anc and nodes[i]['derived'] != 'derived':
            print('S3root %s\t%s\t%s' % (i, meta[i]['title'][:60], OBL.get(i, 'unmapped; bridge field: ' +
                                                                            meta[i]['bridge'][:160])))
    for i in order:
        if i in dall:
            n = nodes[i]
            print('S3desc %s\t%s\t%s\t%s\t%s' % (i, n['level'][:20], n['derived'], n['cls'] + '/' + n['sub'],
                                                meta[i]['title'][:60]))
    lv = {}
    for i in dall:
        for c in span(nodes[i]['level']):
            lv[c] = lv.get(c, 0) + 1
    kd = sorted(i for i in dall if re.match(r'^(K\b|proved \[K\]|definition \[K\]|definitions \[K\])',
                                            meta[i]['status']))
    print('S3 Desc(AX) by level letter: %s; kernel-status members: %s' % (
        ' '.join('%s=%d' % (k, lv[k]) for k in sorted(lv)), ' '.join(kd) or 'none'))
    # frontier: edges into Desc(AX) from outside and out of Anc(P)
    for (s, d, k, xl, sup, note) in edges:
        if k in DEPK and s in dall and d not in dall and xl == '1':
            print('S3xdesc %s -> %s (%s, cross-level, supply %s)' % (s, d, k, sup))
    # ---- S4 cross-level edges
    print('== S4 cross-level edges')
    cl = {}
    for (s, d, k, xl, sup, note) in edges:
        if k in DEPK and xl == '1':
            key = ('/'.join(sorted(span(nodes[s]['level']))), '/'.join(sorted(span(nodes[d]['level']))), sup)
            cl.setdefault(key, []).append('%s>%s' % (s, d))
    for key in sorted(cl):
        print('S4 %s -> %s supply %s: %d  %s' % (key[0], key[1], key[2], len(cl[key]), ' '.join(cl[key][:40])))
    # ---- S5 P-level nodes and their sources
    print('== S5 P-level nodes')
    for i in order:
        if 'P' in span(nodes[i]['level']):
            clos = reach([i], fwd)
            ax = sorted(x for x in clos if x in ('I1.1', 'I1.2', 'I1.20', 'I1.21', 'I1.22', 'I1.23', 'I1.24'))
            ol = sorted(x for x in clos if x != i and x in nodes and 'O' in span(nodes[x]['level'])
                        and 'P' not in span(nodes[x]['level']))
            hm = sorted(x for x in clos if x != i and x in nodes and span(nodes[x]['level']) & set('HMGX'))
            print('S5 %s\tAX/C in closure: %s\tO-level in closure: %d\tH/M/G/X in closure: %s' % (
                i, ','.join(ax) or 'none', len(ol), ','.join(hm) or 'none'))
    print('checks: A2=%s A3=%s' % ('PASS' if ok['A2'] else 'FAIL', 'PASS' if ok['A3'] else 'FAIL'))
    if ok['A2'] and ok['A3']:
        print('VERDICT ANALYSIS COMPLETE')


if __name__ == '__main__':
    main()
