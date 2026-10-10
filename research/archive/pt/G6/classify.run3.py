#!/usr/bin/env python3
"""G6 classify.py -- node classes and the machine-readable graph (read-only; stdout only).

Run from pt/G6/ as `python3 -I -B classify.py`. Inputs: parse.out, edges.out (this directory). The stdout is
the content of graph.tsv (graph.tsv is a byte copy of classify.out).

RULES: NOTES N1 (classes) and N2 (root categories; named-hypothesis keywords), fixed before the first run.
  derived(u): as edges.py (status proved / kernel / conditional, kind not a definition, hypothesis-structure,
  axiom or condition). roots(u): every non-derived node reachable from u by R, RA, RN, KC edges (traversing
  through non-derived nodes), with the named hypotheses of every node met (u included).
  class(u), u derived: d if a PHYS root, else c if an OPER root, else b if a C root, else a (a0 no AX root and
  no FOUND root; a1 AX present, no FOUND; a2 FOUND present). u non-derived: a/gen (I1.1, I1.2), b/gen (C1-C4
  records I1.20-I1.24), otherwise e/<category>/<kind>.
DECISION RULE (fixed before the first run):
  G1  every one of the 633 records receives exactly one class.                                  PASS/FAIL
  G2  every edge of edges.out with a record source appears exactly once in the edge table.     PASS/FAIL
  G3  countercontrol: the classifier applied to a synthetic derived node whose only edge goes to I1.1 returns
      a1; with a further edge to I1.20 returns b; with a further edge to an OPER root returns c; with a
      further PHYS named hypothesis returns d.                                                  PASS/FAIL
  A line '#VERDICT GRAPH VALID' prints (as a comment row) only if G1-G3 pass.
Output: '#table nodes' then one row per node; '#table edges' then one row per edge; '#' comment rows.
AMENDMENT before run 2 (18:14Z; run 1 kept as classify.run1.{py,out,err}; rules G1-G3 unchanged). Review of
  run 1 found the N2 rules written for the manuscript H level applied to kernel records: (A1) N2 rule 8 sent
  ten kernel hypothesis-structures at level H (I4's substratum-class objects, which I4's header states are
  matrix-level theories or classes) to PHYS; they are kernel operational hypotheses: OPER. Rule 8 now applies
  to manuscript records only. (A2) free-text pieces of kernel records (I4 rows; records with kernel status)
  that match no keyword are binder conditions of a kernel declaration (e.g. 'Fin 2', 'Λ nonempty'): DEF, not
  level-defaulted. (A3) a derived node whose status reads 'conditional(-on) X' carries X as a named
  hypothesis (I3.184 had an empty depends_on). (A4) keywords added: 'completion conditions' -> OPER;
  'slow-bath', 'τ_B' -> C2; 'weak-coupling', '(EM)'/'EM' -> PHYS; 'μI' -> DEF. Both partitions are reported.
AMENDMENT before run 3 (18:20Z; run 2 kept as classify.run2.*): N2 rule 6 reads 'status a definition (...
  proved [K] (definition))'; the pattern missed the plural 'proved [K] (definitions)' of I3.11 (`cnot`, `nflip`,
  `z3`, `phiW`), which run 2 placed under OPER. Pattern widened to the plural only.
"""
import re

AX = {'I1.1', 'I1.2'}
CMAP = {'I1.20': 'C1', 'I1.21': 'C2', 'I1.22': 'C2', 'I1.23': 'C3', 'I1.24': 'C4',
        'I1.70': 'C4', 'I1.71': 'C4', 'I1.72': 'C4', 'I1.73': 'C4'}
GEN_B = {'I1.20', 'I1.21', 'I1.22', 'I1.23', 'I1.24'}
FOUND = {'I1.4', 'I1.6', 'I1.9', 'I1.12', 'I1.13', 'I1.14'}
PHYS = {'I1.5', 'I1.10', 'I1.11', 'I1.36', 'I1.61', 'I1.63', 'I1.64', 'I1.65', 'I1.66', 'I1.67', 'I1.68',
        'I1.74', 'I1.77', 'I2.6', 'I2.46', 'I2.73', 'I2.76', 'I2.86', 'I2.87', 'I2.102', 'I2.113'}
NEUTRAL = {'I1.16', 'I1.18', 'I1.19', 'I1.26', 'I1.37', 'I1.76', 'I1.78', 'I2.70', 'I2.78', 'I2.84', 'I2.85',
           'I2.110', 'I2.111'}
DEFN = {'I1.38', 'I1.39', 'I1.42', 'I1.57'}
NOISE = re.compile(r"\.(lean|md|py)\b|^(I[1-4]\b|I[1-4]'s|thread|the witnesses|presupposition|negated|step \d|"
                   r"act \d|\[|imported|the alternative it rejects|as stated|A5 is a hypothesis of)", re.I)
KW_C = [(re.compile(r'C1–C4|C1-C4'), ['C1', 'C2', 'C3', 'C4']), (re.compile(r'slow-bath|τ_B'), ['C2'])] + \
       [(re.compile(r'\bC%d\b' % k), ['C%d' % k]) for k in range(1, 5)] + \
       [(re.compile(r'\bpersistence\b', re.I), ['C2']), (re.compile(r'readback', re.I), ['C4']),
        (re.compile(r'\brecurrence\b', re.I), ['AX'])]
KW_F = re.compile(r'counting measure|Lemma 3', re.I)
KW_M = re.compile(r'finite visible alphabet|finite horizon|initial law|rational law|finite order|bijection|'
                  r'non-permutation|ρ_H|\[U,R_g\]|gaps|genericity|q prime|uniform|faithful deterministic '
                  r'realization|response-complete|μI', re.I)
KW_O = re.compile(r'inert spectators|reversible control|iterated composition|valid probabilities|trivial-ancilla|'
                  r'three principles|OI core|well-formedness|phase intervention|controllability|typed operational|'
                  r'operational lift|quantum experiment|instrument|interventions|ancilla|OI_Q|observable algebra|'
                  r'observer projection|QM description|completion conditions', re.I)
KW_P = re.compile(r'mixing hypothesis|\bETH\b|\bE[1-7]\b|M1-T|M1-B|\bA[1-6]\b|H-local-lift|H-scramble|H-Bell|'
                  r'holographic|Liouville|typicality|determinism|setting operations|readout|ensemble|'
                  r'nearest-neighbor|translation invariance|range-1|coupling|energy-conserving|site factorization|'
                  r'spatial locality|wave equation|foliation|lattice|staggered|Barandes|finiteness|trace-out|'
                  r'gauge|commutation|weak-coupling|\bEM\b', re.I)


def clean(s):
    return re.sub(r'\s+', ' ', s.replace('\t', ' ')).strip()


def load():
    nodes, order = {}, []
    for ln in open('parse.out', encoding='utf-8').read().split('\n'):
        f = ln.split('\t')
        if f[0] == 'N' and len(f) == 12:
            keys = ['id', 'title', 'kind', 'level', 'status', 'flag', 'dep', 'yields', 'bridge', 'bearing', 'src']
            nodes[f[1]] = dict(zip(keys, f[1:]))
            order.append(f[1])
    edges, prose, kc = [], {}, {}
    for ln in open('edges.out', encoding='utf-8').read().split('\n'):
        f = ln.split('\t')
        if f[0] == 'G' and len(f) == 7:
            edges.append(tuple(f[1:]))
        elif f[0] == 'P' and len(f) == 3:
            prose[f[1]] = [p for p in f[2].split(' ;; ') if p]
    return nodes, order, edges, prose


def derived(n):
    k = n['kind'].split(' ')[0].split('(')[0].rstrip(',;')
    st = n['status']
    if k in ('hypothesis-structure', 'definition-as-hypothesis', 'definition', 'axiom', 'condition'):
        return False
    if re.match(r'^(K\b|proved|conditional|theorem)', st):
        return True
    if k in ('theorem', 'lemma', 'manuscript-principle', 'obligation') and re.search(r'\bproved\b', st) \
            and not st.startswith('not at L') and not st.startswith('empirically'):
        return True
    return False


def span(level):
    return set(c for c in 'HOPMGX' if c in level.split('(')[0])


def is_dna(n):
    return 'do not assume' in n['flag'] or n['flag'].startswith('DNA') or 'do not assume' in n['flag'].lower()


def root_cat(i, n):
    if i in AX:
        return 'AX'
    if i in CMAP:
        return CMAP[i]
    if i in FOUND:
        return 'FOUND'
    if i in PHYS:
        return 'PHYS'
    if i in NEUTRAL or n['status'].startswith('scope statement'):
        return 'NEUTRAL'
    st = n['status']
    if i in DEFN or re.match(r'^(-|definition\b|definition \[K\]|definitions \[K\]|proved \[K\] \(definitions?\))', st):
        return 'DEF'
    if span(n['level']) & set('OPMG') or is_dna(n):
        return 'OPER'
    if is_kernel(i, n):
        return 'OPER'
    return 'PHYS'


def is_kernel(i, n):
    return i.startswith('I4.') or bool(re.match(r'^(K\b|proved \[K\]|definition \[K\]|definitions \[K\])',
                                               n['status']))


def prose_cat(piece, level, kernel=False):
    if NOISE.search(piece) or len(re.sub(r"[^A-Za-z]", '', re.sub(r'\b[A-Z][a-z]+[A-Z]\w*\b', '', piece))) < 3:
        return None, ''
    cs_all = []
    for rx, cs in KW_C:
        if rx.search(piece):
            cs_all += [c for c in cs if c not in cs_all]
    if cs_all:
        return cs_all, 'kw'
    if KW_F.search(piece):
        return ['FOUND'], 'kw'
    if KW_M.search(piece):
        return ['DEF'], 'kw'
    if KW_O.search(piece):
        return ['OPER'], 'kw'
    if KW_P.search(piece):
        return ['PHYS'], 'kw'
    if kernel:
        return ['DEF'], 'kernel-binder'
    sp = span(level)
    return (['OPER'] if sp & set('OPMG') else ['PHYS']), 'level'


def classify_node(i, nodes, deps, named, memo):
    """Return (roots dict cat -> sorted names, set of external names)."""
    seen, stack = set(), [i]
    cats, ext = {}, set()
    while stack:
        x = stack.pop()
        if x in seen:
            continue
        seen.add(x)
        for (piece, cs, how) in named.get(x, []):
            for c in cs:
                cats.setdefault(c, set()).add('"%s"@%s' % (piece[:60], x))
        for t in deps.get(x, []):
            if t.startswith(('K:', 'D:')):
                ext.add(t)
                continue
            if t not in seen:
                stack.append(t)
        if x != i and not derived(nodes[x]):
            c = root_cat(x, nodes[x])
            cats.setdefault(c, set()).add(x)
    return cats, ext


def class_of(i, n, cats):
    if not derived(n):
        if i in AX:
            return 'a', 'gen'
        if i in GEN_B:
            return 'b', 'gen:' + CMAP[i]
        k = n['kind'].split(' ')[0].split('(')[0].rstrip(',;')
        return 'e', '%s/%s' % (root_cat(i, n), k)
    if 'PHYS' in cats:
        return 'd', ''
    if 'OPER' in cats:
        return 'c', ''
    cs = sorted(c for c in cats if re.match(r'^C[1-4]$', c))
    if cs:
        return 'b', ','.join(cs)
    if 'FOUND' in cats:
        return 'a', 'a2'
    if 'AX' in cats:
        return 'a', 'a1'
    return 'a', 'a0'


def main():
    nodes, order, edges, prose = load()
    deps, seen_e = {}, set()
    for (s, d, k, xl, sup, note) in edges:
        if k == 'Y':
            continue
        deps.setdefault(s, [])
        if d not in deps[s]:
            deps[s].append(d)
    named = {}
    for i in order:
        pieces = list(prose.get(i, []))
        mcond = re.match(r'^(?:conditional-on|conditional)\s*[—:-]?\s*(.*)$', nodes[i]['status'])
        if mcond and derived(nodes[i]) and mcond.group(1).strip():
            pieces.append(mcond.group(1).strip()[:200])
        for piece in pieces:
            cs, how = prose_cat(piece, nodes[i]['level'], is_kernel(i, nodes[i]))
            if cs:
                named.setdefault(i, []).append((piece, cs, how))
    rows, classes = [], {}
    for i in order:
        n = nodes[i]
        cats, ext = classify_node(i, nodes, deps, named, None)
        cl, sub = class_of(i, n, cats)
        classes[i] = (cl, sub)
        need = []
        for c in ('C1', 'C2', 'C3', 'C4', 'FOUND', 'OPER', 'PHYS'):
            if c in cats and (cl in 'bcd' or c == 'FOUND'):
                need.append('%s=%s' % (c, ','.join(sorted(cats[c], key=lambda x: (len(x), x)))[:900]))
        rows.append([i, n['kind'], n['status'][:160], n['level'][:60], cl, sub,
                     ';'.join(deps.get(i, [])),
                     ' | '.join('%s{%s%s}' % (p[:120], '/'.join(cs), '*' if how == 'level' else '')
                                for (p, cs, how) in named.get(i, [])),
                     'DNA' if is_dna(n) else '-', 'derived' if derived(n) else 'non-derived',
                     ' ; '.join(need), ','.join(sorted(ext))])
    # G1-G3
    ok = {}
    ok['G1'] = len(rows) == 633 and all(r[4] in 'abcde' for r in rows)
    rec_edges = [e for e in edges if e[0] in nodes]
    ok['G2'] = len(rec_edges) == len(set((e[0], e[1], e[2]) for e in rec_edges))
    syn = dict(id='S.1', kind='theorem', status='proved [K]', level='H', flag='-')
    t = {}
    for extra, want in ((['I1.1'], ('a', 'a1')), (['I1.1', 'I1.20'], ('b', 'C1')),
                        (['I1.1', 'I1.20', 'I4.3'], ('c', '')), (['I1.1', 'I1.20', 'I4.3', 'PH'], ('d', ''))):
        d2 = dict(deps)
        d2['S.1'] = [x for x in extra if x != 'PH']
        nm2 = dict(named)
        if 'PH' in extra:
            nm2['S.1'] = [('mixing hypothesis', ['PHYS'], 'kw')]
        nodes2 = dict(nodes)
        nodes2['S.1'] = syn
        cats, _ = classify_node('S.1', nodes2, d2, nm2, None)
        t[str(extra)] = class_of('S.1', syn, cats) == want
    ok['G3'] = all(t.values())
    print('#table nodes')
    print('\t'.join(['id', 'kind', 'status', 'level', 'class', 'sublabel', 'depends_on', 'named_hypotheses',
                     'flag', 'derived', 'needs', 'external']))
    for r in rows:
        print('\t'.join(clean(x) for x in r))
    print('#table edges')
    print('\t'.join(['src', 'dst', 'kind', 'xlevel', 'supply', 'note']))
    for e in edges:
        print('\t'.join(clean(x) for x in e))
    cnt = {}
    for i in order:
        key = classes[i][0] + ('/' + classes[i][1].split(':')[0] if classes[i][0] in 'ae' and classes[i][1] else '')
        cnt[key] = cnt.get(key, 0) + 1
    print('#counts ' + ' '.join('%s=%d' % (k, cnt[k]) for k in sorted(cnt)))
    print('#checks ' + ' '.join('%s=%s' % (k, 'PASS' if ok[k] else 'FAIL') for k in ('G1', 'G2', 'G3'))
          + ' G3detail=' + ','.join('1' if v else '0' for v in t.values()))
    if all(ok.values()):
        print('#VERDICT GRAPH VALID')


if __name__ == '__main__':
    main()
