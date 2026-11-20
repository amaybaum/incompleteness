#!/usr/bin/env python3
"""A1-EXIT ledger: build the site map at the pin and run the completeness checks of PREREG.md §5.

Usage (from the repository root):
  python3 -I -B verification/audits/foundations/a1exit-ledger-20261120/ledger_check.py build   # writes sitemap.json
  python3 -I -B verification/audits/foundations/a1exit-ledger-20261120/ledger_check.py check   # CK1-CK8 + rebuild compare
  python3 -I -B verification/audits/foundations/a1exit-ledger-20261120/ledger_check.py self-test

The site map relocates the Phase-0 site census (a1-scope-phase0-20261120/sites.json) to the working
tree and adds every line matching the Phase-0 pattern set that has no Phase-0 counterpart. It reads
only the working tree and the records named below; it classifies nothing new except through
rows.json's `new_site_rules`.
"""
import difflib
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..'))
FOUND = os.path.join(ROOT, 'verification', 'audits', 'foundations')
P0 = os.path.join(FOUND, 'a1-scope-phase0-20261120', 'sites.json')
P1 = os.path.join(FOUND, 'a1-scope-phase0-20261120', 'phase1_ledger.json')
P2L = os.path.join(FOUND, 'a1-scope-phase2-20261120', 'phase2_ledger.json')
P2D = os.path.join(FOUND, 'a1-scope-phase2-20261120', 'dispositions.json')
ROWS = os.path.join(HERE, 'rows.json')
SITEMAP = os.path.join(HERE, 'sitemap.json')

PHASE3_FILES = ['papers/Methodology.md', 'papers/Computation.md', 'papers/Introduction.md',
                'papers/Complexity.md', 'papers/Medicine.md', 'book/ch14-quantum-computing.md',
                'book/ch18-beyond.md']
FULL = 'book/The-Incompleteness-of-Observation-FULL.md'
PTR_PATTERNS = ('core:P1', 'core:P2', 'core:P5')


def load(p):
    with open(p, encoding='utf-8') as f:
        return json.load(f)


def corpus_files():
    out = []
    for d in ('papers', 'book'):
        for n in sorted(os.listdir(os.path.join(ROOT, d))):
            if n.endswith('.md'):
                out.append(d + '/' + n)
    return out


def read_lines(rel):
    with open(os.path.join(ROOT, rel), encoding='utf-8') as f:
        return f.read().split('\n')


def compile_patterns(p0):
    pats = []
    for k, v in p0['core_patterns'].items():
        pats.append(('core:' + k, re.compile(v)))
    for k, v in p0['paraphrase_patterns'].items():
        pats.append(('para:' + k, re.compile(v)))
    return pats


def scan(pats, files):
    hits = {}
    for rel in files:
        for i, line in enumerate(read_lines(rel), 1):
            m = [k for k, rx in pats if rx.search(line)]
            if m:
                hits[(rel, i)] = m
    return hits


def splice_map():
    """old line text fragment -> new fragment, from the applied Phase-1 and Phase-2 ledgers."""
    sp = []
    for p in (P1, P2L):
        for s in load(p)['splices']:
            sp.append((s['file'], s['old'], s['new'], s['unit']))
    return sp


def relocate(site, lines_by_file, splices):
    rel = site['file']
    if rel not in lines_by_file:
        lines_by_file[rel] = read_lines(rel)
    lines = lines_by_file[rel]
    q = site['quote']
    exact = [i for i, l in enumerate(lines, 1) if q in l]
    if len(exact) == 1:
        return exact[0], 'exact', None
    if len(exact) > 1:
        best = min(exact, key=lambda i: abs(i - site['line']))
        return best, 'exact-dup', None
    # apply splices recorded for this file
    q2, units = q, []
    for f, old, new, unit in splices:
        if (f == rel or (rel == FULL and f == FULL)) and old in q2:
            q2 = q2.replace(old, new)
            units.append(unit)
    if units:
        hit = [i for i, l in enumerate(lines, 1) if q2 in l]
        if hit:
            return min(hit, key=lambda i: abs(i - site['line'])), 'splice', units
    # anchors: the quote's first or last 60 characters, found in one line near the old position
    if len(q) > 80:
        for a in (q[:60], q[-60:]):
            hit = [i for i, l in enumerate(lines, 1) if a in l]
            if hit:
                return min(hit, key=lambda i: abs(i - site['line'])), 'anchor', units or None
    # fuzzy: same file; the quote is one sentence of its line, so score by the longest common block
    best, br = None, 0.0
    lo, hi = max(1, site['line'] - 150), min(len(lines), site['line'] + 150)
    for i in range(lo, hi + 1):
        l = lines[i - 1]
        if not l.strip():
            continue
        sm = difflib.SequenceMatcher(None, q, l, autojunk=False)
        m = sm.find_longest_match(0, len(q), 0, len(l))
        r = m.size / max(1, len(q))
        if r > br:
            best, br = i, r
    if best and br >= 0.5:
        return best, 'fuzzy:%.2f' % br, units or None
    return None, 'removed', units or None


def build():
    p0 = load(P0)
    rows = load(ROWS)
    pats = compile_patterns(p0)
    files = corpus_files()
    hits = scan(pats, files)
    splices = splice_map()
    lines_by_file = {}
    sites, claimed = [], set()
    for s in p0['sites']:
        ln, how, units = relocate(s, lines_by_file, splices)
        rec = {'p0_id': s['id'], 'file': s['file'], 'line': ln, 'relocation': how,
               'splice_units': units, 'p0_class': s['class'], 'p0_rows': s['rows'],
               'p0_phase': s['phase'], 'p0_action': s['action'], 'mirror_of': s['mirror_of'],
               'patterns_at_pin': hits.get((s['file'], ln), []) if ln else []}
        if ln:
            claimed.add((s['file'], ln))
        sites.append(rec)
    for (rel, ln), m in sorted(hits.items()):
        if (rel, ln) in claimed:
            continue
        sites.append({'p0_id': 'new', 'file': rel, 'line': ln, 'relocation': 'new',
                      'splice_units': None, 'p0_class': None, 'p0_rows': [], 'p0_phase': None,
                      'p0_action': None, 'mirror_of': None, 'patterns_at_pin': m})
    p2 = {d['site']: d for d in load(P2D)['dispositions']}
    p0keys = {'%s:%d' % (x['file'], x['line']) for x in p0['sites']}
    for key, d in sorted(p2.items()):
        if key.startswith('FULL<-') or key in p0keys or d['phase0_class'] != 'census':
            continue
        rel, ln = key.rsplit(':', 1)
        ln = int(ln)
        if (rel, ln) in claimed or any(x['file'] == rel and x['line'] == ln for x in sites):
            continue
        sites.append({'p0_id': 'p2-census', 'file': rel, 'line': ln, 'relocation': 'p2-census',
                      'splice_units': None, 'p0_class': 'P2-census', 'p0_rows': [], 'p0_phase': 'P2',
                      'p0_action': d['action'], 'mirror_of': None, 'patterns_at_pin': hits.get((rel, ln), [])})
    present = {(x['file'], x['line']) for x in sites}
    for key in sorted(rows.get('site_overrides', {})):
        rel, ln = key.rsplit(':', 1)
        if (rel, int(ln)) not in present:
            sites.append({'p0_id': 'extra', 'file': rel, 'line': int(ln), 'relocation': 'extra',
                          'splice_units': None, 'p0_class': None, 'p0_rows': [], 'p0_phase': None,
                          'p0_action': None, 'mirror_of': None, 'patterns_at_pin': hits.get((rel, int(ln)), [])})
    for rec in sites:
        assign(rec, rows)
        if rec['p0_id'] not in ('new', 'p2-census', 'extra'):
            p0s = next(x for x in p0['sites'] if x['id'] == rec['p0_id'])
            k0 = '%s:%d' % (p0s['file'], p0s['line'])
            if rec['file'] == FULL and rec['mirror_of']:
                k0 = 'FULL<-' + rec['mirror_of']
        else:
            k0 = '%s:%s' % (rec['file'], rec['line'])
        d = p2.get(k0)
        rec['p2_action'] = d['action'] if d else None
        rec['p2_units'] = d['units'] if d else None
        rec['p2_reason'] = d['reason'] if d else None
        rec['s3'] = s3(rec, rows)
    sites.sort(key=lambda x: (x['file'], x['line'] or 0))
    return {'schema': 'a1exit site map v1', 'pin_note': 'line numbers at the working tree the map was built from',
            'sites': sites}


def s3(rec, rows):
    """Is the finite-only, conditional or open qualification visible at this site now?"""
    if rec['row'] in (None, '-'):
        return 'n/a'
    if rec['owner'] == 'Q3 propagation':
        return 'not determined: Q3 census'
    if rec['code'] == 'ptr':
        return 'visible (names the hypothesis); rewritten at deletion'
    r = rows_by_id(rows).get(rec['row'])
    if r and r['owner'] in ('Q1', 'Q2', 'R6', 'Main:764', 'Step-2 phase') and r['status'] != 'done':
        return 'per unit ' + r['owner']
    if rec.get('p2_action') == 'edit' or rec.get('splice_units'):
        return 'visible (applied splice)'
    if rec.get('p2_action') == 'N' or rec['p0_action'] in ('K', 'N') or (rec['p0_action'] or '').startswith(('E', 'B')):
        return 'visible (P0/P1/P2 disposition)'
    if rec['p0_id'] == 'new':
        return 'visible (' + rec.get('reason', '') + ')'
    return 'not determined'


def site_key(rec):
    return '%s:%s' % (rec['file'], rec['line'])


def assign(rec, rows):
    """Ledger row, correction code, owner and status for a site, from rows.json rules only."""
    key = site_key(rec)
    ov = rows.get('site_overrides', {})
    if rec['p0_id'] in ov or key in ov:
        o = ov.get(rec['p0_id']) or ov.get(key)
        rec.update({k: o[k] for k in ('row', 'code', 'reason', 'owner') if k in o})
    else:
        cls = rec['p0_class']
        if rec['p0_id'] == 'new':
            rule = None
            for r in rows['new_site_rules']:
                if re.search(r['match'], rec['file'] + ':' + read_lines(rec['file'])[rec['line'] - 1]):
                    rule = r
                    break
            if rule is None:
                rec.update({'row': None, 'code': None, 'reason': 'unclassified new site'})
                return
            rec.update({'row': rule['row'], 'code': rule['code'], 'reason': rule['reason']})
        elif cls in ('FP', 'FREE'):
            rec.update({'row': '-', 'code': 'none', 'reason': 'P0 class %s' % cls})
        elif cls == 'P2-census':
            if rec['p0_action'] == 'N':
                rec.update({'row': '-', 'code': 'none', 'reason': 'P2 census extension, kept (finite-model statement)'})
            else:
                rec.update({'row': 'X-02', 'code': None, 'reason': 'P2 census extension, edited (A-C units)'})
        elif rec['line'] is None:
            rec.update({'row': '-', 'code': 'none', 'reason': 'removed since P0 (no line at the pin)'})
        else:
            row = None
            for k in rec['p0_rows']:
                if k in rows['p0_row_map']:
                    row = rows['p0_row_map'][k]
                    break
            if cls in ('INFLOW', 'R5'):
                row = rows['p0_class_map'][cls]
            if cls == 'DECL':
                row = rows['p0_row_map'].get('DECL:' + (rec['p0_rows'][0] if rec['p0_rows'] else ''),
                                             rows['p0_class_map']['DECL'])
            if row is None:
                row = rows['p0_class_map'].get(cls)
            rec.update({'row': row, 'code': None, 'reason': 'P0 rows %s' % ','.join(rec['p0_rows'])})
    r = rows_by_id(rows).get(rec['row'])
    if rec.get('code') is None:
        ptr = any(p in PTR_PATTERNS for p in rec['patterns_at_pin'])
        if rec['file'] in PHASE3_FILES or (rec['file'] == FULL and (rec['mirror_of'] or '').split(':')[0] in PHASE3_FILES):
            rec['code'] = 'unit'
            rec['owner'] = 'Q3 propagation'
        elif ptr:
            rec['code'] = 'ptr'
        else:
            rec['code'] = r['site_code'] if r else None
    if 'owner' not in rec:
        if rec['code'] == 'ptr':
            rec['owner'] = 'final deletion'
        elif rec['code'] == 'unit' and r:
            rec['owner'] = r['owner']
        else:
            rec['owner'] = 'none'


def rows_by_id(rows):
    return {r['id']: r for r in rows['rows']}


def check(sm, rows, quiet=False):
    errs = []
    rid = rows_by_id(rows)
    # CK1
    seeds = ['M%d' % i for i in range(1, 22) if i != 0] + ['C%d' % i for i in range(1, 15)] + ['R%d' % i for i in range(1, 7)]
    covered = set()
    for r in rows['rows']:
        covered.update(r['sources'])
    for s in seeds:
        if s not in covered:
            errs.append('CK1 REMAINDER %s maps to no row' % s)
    # CK2
    for k in rows['stage0_rows'] + rows['stage1ii_rows'] + rows['oa4_rows']:
        if k not in covered:
            errs.append('CK2 %s maps to no row' % k)
    # CK3, CK4, CK6, CK7
    p3 = 0
    for s in sm['sites']:
        if s['p0_class'] not in ('FP', 'FREE') and s['p0_id'] != 'new' and s['line'] is not None and s['row'] in (None,):
            errs.append('CK3 %s %s unmapped' % (s['p0_id'], site_key(s)))
        if s['p0_id'] == 'new' and s['row'] is None:
            errs.append('CK4 new site %s unclassified' % site_key(s))
        if s['row'] not in (None, '-') and s['row'] not in rid:
            errs.append('CK3 %s maps to unknown row %s' % (site_key(s), s['row']))
        if s['row'] not in (None, '-') and any(p in PTR_PATTERNS for p in s['patterns_at_pin']):
            if s['code'] not in ('ptr', 'unit') and not s.get('reason', '').startswith('none:'):
                errs.append('CK6 %s names A1/item (ii) with code %s' % (site_key(s), s['code']))
        if s['p0_phase'] == 'P2' and (s['file'] in PHASE3_FILES or (s['file'] == FULL and (s['mirror_of'] or '').split(':')[0] in PHASE3_FILES)):
            p3 += 1
            if s['owner'] != 'Q3 propagation':
                errs.append('CK7 %s not owned by Q3' % site_key(s))
    if p3 != 77:
        errs.append('CK7 Phase-3 sites listed: %d, expected 77' % p3)
    # CK5
    for r in rows['rows']:
        if r['disposition'] not in ('J', 'F', 'O'):
            errs.append('CK5 %s disposition %r' % (r['id'], r['disposition']))
        if r['disposition'] == 'J' and r.get('s1') not in ('No', 'Relabel'):
            errs.append('CK5 %s J with S1 %r' % (r['id'], r.get('s1')))
        if r['disposition'] in ('F', 'O') and not r.get('mirrors') and not any(x['row'] == r['id'] for x in sm['sites']):
            errs.append('CK5 %s %s without mirror list' % (r['id'], r['disposition']))
    # CK8
    if not rows.get('lean'):
        errs.append('CK8 no Lean entries')
    if not any('a1_of_finite' in l['decl'] for l in rows.get('lean', [])):
        errs.append('CK8 a1_of_finite not listed')
    if not quiet:
        for e in errs:
            print(e)
    return errs


def short(rel):
    m = {'papers/Main.md': 'M', 'papers/SM.md': 'SM', 'papers/GR.md': 'GR', 'papers/Substratum.md': 'Sub',
         'papers/Structure.md': 'Str', 'papers/Methodology.md': 'Meth', 'papers/Computation.md': 'Comp',
         'papers/Complexity.md': 'Cx', 'papers/Introduction.md': 'Intro', 'papers/Medicine.md': 'Med', FULL: 'FULL'}
    if rel in m:
        return m[rel]
    b = rel.split('/')[-1].replace('.md', '')
    if b.startswith('ch'):
        return b[:4]
    return {'glossary': 'gloss', 'preface': 'pref'}.get(b, b.replace('appendix-', 'app').split('-')[0])


def cell(t):
    return str(t).replace('|', '\\|').replace('\n', ' ')


def render(sm, rows):
    """The ledger table and the summary counts, generated from rows.json and sitemap.json."""
    from collections import Counter
    out = ['| Id | Dependency (home at the pin) | Sources | How A1 enters | Disp. | Weaker condition (J) | Disguised A1? (S1) | Exit route | Correction | Sites and S3 (qualification visible?) | Owner | Status |',
           '|---|---|---|---|---|---|---|---|---|---|---|---|']
    for r in rows['rows']:
        ss = [x for x in sm['sites'] if x['row'] == r['id']]
        c = Counter('not determined' if x['s3'].startswith('not determined') else x['s3'].split(' (')[0] for x in ss)
        codes = Counter(x['code'] for x in ss)
        if ss:
            lst = ', '.join('%s:%s' % (short(x['file']), x['line']) for x in ss[:12]) + (' …' if len(ss) > 12 else '')
            s3 = '%d sites (%s); codes %s. %s' % (len(ss), ', '.join('%s %d' % kv for kv in sorted(c.items())),
                                                 ', '.join('%s %d' % kv for kv in sorted(codes.items())), lst)
        else:
            s3 = 'no primary site'
        if r.get('mirrors'):
            s3 += '; also ' + ', '.join(r['mirrors'])
        s1 = (r['s1'] + ': ' + r['s1_reason']) if r['disposition'] == 'J' else 'n/a (not J)'
        out.append('| ' + ' | '.join(cell(v) for v in [
            r['id'], r['title'] + ' (' + r['home'] + ')', ', '.join(r['sources']), r['how'], r['disposition'],
            r['weaker'] or '—', s1, r['exit'], r['correction'], s3, r['owner'], r['status']]) + ' |')
    disp = Counter(r['disposition'] for r in rows['rows'])
    own = Counter(r['owner'] for r in rows['rows'])
    st = Counter(r['status'].split(' (')[0].split(';')[0] for r in rows['rows'])
    s1 = Counter(r['s1'] for r in rows['rows'] if r['disposition'] == 'J')
    sc = Counter(x['code'] for x in sm['sites'] if x['row'] not in (None, '-'))
    so = Counter(x['owner'] for x in sm['sites'] if x['row'] not in (None, '-'))
    cnt = ['| Measure | Counts |', '|---|---|',
           '| Rows | %d |' % len(rows['rows']),
           '| Disposition | ' + ', '.join('%s %d' % kv for kv in sorted(disp.items())) + ' |',
           '| S1 on J rows | ' + ', '.join('%s %d' % kv for kv in sorted(s1.items())) + ' |',
           '| Row owner | ' + ', '.join('%s %d' % kv for kv in sorted(own.items())) + ' |',
           '| Row status | ' + ', '.join('%s %d' % kv for kv in sorted(st.items())) + ' |',
           '| Sites in the map | %d (%d mapped to a row; %d FP, FREE or kept) |' % (
               len(sm['sites']), sum(1 for x in sm['sites'] if x['row'] not in (None, '-')),
               sum(1 for x in sm['sites'] if x['row'] == '-')),
           '| Mapped sites by correction code | ' + ', '.join('%s %d' % kv for kv in sorted(sc.items())) + ' |',
           '| Mapped sites by owner | ' + ', '.join('%s %d' % kv for kv in sorted(so.items())) + ' |']
    def grouped(pred):
        g = {}
        for x in sm['sites']:
            if x['row'] not in (None, '-') and pred(x):
                g.setdefault(short(x['file']), []).append('%d (%s)' % (x['line'], x['row']))
        return '\n'.join('- **%s** (%d): %s' % (k, len(v), ', '.join(v)) for k, v in sorted(g.items()))
    p3 = grouped(lambda x: x['owner'] == 'Q3 propagation')
    ptr = grouped(lambda x: x['code'] == 'ptr')
    return {'TABLE': '\n'.join(out), 'COUNTS': '\n'.join(cnt), 'PHASE3': p3, 'PTR': ptr}


def splice_block(text, tag, body):
    a, b = '<!-- %s:BEGIN -->' % tag, '<!-- %s:END -->' % tag
    i, j = text.index(a) + len(a), text.index(b)
    return text[:i] + '\n' + body + '\n' + text[j:]


def self_test():
    rows = load(ROWS)
    sm = load(SITEMAP)
    ok = True
    # countercontrol 1: a synthetic site with no row
    bad = json.loads(json.dumps(sm))
    bad['sites'].append({'p0_id': 'new', 'file': 'papers/Main.md', 'line': 1, 'row': None, 'code': None,
                         'p0_class': None, 'p0_phase': None, 'patterns_at_pin': [], 'owner': 'none',
                         'mirror_of': None})
    ok &= any(e.startswith('CK4') for e in check(bad, rows, quiet=True))
    # countercontrol 2: a J row with S1 = Yes
    r2 = json.loads(json.dumps(rows))
    j = next(r for r in r2['rows'] if r['disposition'] == 'J')
    j['s1'] = 'Yes'
    ok &= any(e.startswith('CK5') for e in check(sm, r2, quiet=True))
    # countercontrol 3: a dropped Phase-3 site
    bad3 = json.loads(json.dumps(sm))
    for i, s in enumerate(bad3['sites']):
        if s['owner'] == 'Q3 propagation':
            del bad3['sites'][i]
            break
    ok &= any(e.startswith('CK7') for e in check(bad3, rows, quiet=True))
    # control: the real data pass
    ok &= check(sm, rows, quiet=True) == []
    print('self-test', 'PASS' if ok else 'FAIL')
    return ok


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else 'check'
    if mode == 'build':
        sm = build()
        with open(SITEMAP, 'w', encoding='utf-8') as f:
            json.dump(sm, f, indent=1, ensure_ascii=False)
            f.write('\n')
        print('sites', len(sm['sites']))
        return 0
    if mode == 'render':
        sm, rows = load(SITEMAP), load(ROWS)
        blocks = render(sm, rows)
        p = os.path.join(HERE, 'LEDGER.md')
        with open(p, encoding='utf-8') as f:
            text = f.read()
        for k, v in blocks.items():
            text = splice_block(text, k, v)
        with open(p, 'w', encoding='utf-8') as f:
            f.write(text)
        print('rendered')
        return 0
    if mode == 'check':
        sm = load(SITEMAP)
        rebuilt = build()
        if rebuilt != sm:
            print('REBUILD differs from sitemap.json')
            return 1
        blocks = render(sm, load(ROWS))
        with open(os.path.join(HERE, 'LEDGER.md'), encoding='utf-8') as f:
            text = f.read()
        new = text
        for k, v in blocks.items():
            new = splice_block(new, k, v)
        if new != text:
            print('LEDGER.md table or counts differ from the render')
            return 1
        errs = check(sm, load(ROWS))
        print('CK1-CK8', 'PASS' if not errs else 'FAIL (%d)' % len(errs))
        return 1 if errs else 0
    if mode == 'self-test':
        return 0 if self_test() else 1
    print(__doc__)
    return 2


if __name__ == '__main__':
    sys.exit(main())
