#!/usr/bin/env python3
"""Coordinator's baseline parse of the four step-1 inventories (pt/I1..I4/INVENTORY.md), written before G6 reports.
Extracts per record: id, kind, level, status keyword, the inventory ids mentioned in its depends_on field, and the
ids mentioned in its yields field.  Prints counts and dangling references; writes nodes.tsv and edges_by_id.tsv next
to this script.  Read-only on the inventories.  Run: python3 -I -B parse_inventories.py from pt/audit/stage6-inputs/G-audit/
DECISION RULE (fixed before the first run): CONFIRMED/MISMATCH lines for the expected record counts (85, 113, 187, 248),
for 'no dangling depends_on id' and 'no dangling yields id'; BASELINE-FIXED iff all CONFIRMED (dangling ids are
reported, not failed, when they are forward references to a sibling thread's record that exists).
"""
import re, os, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..'))
R = []
def rec(cid, ok, text, detail=""):
    ok = bool(ok); R.append(ok)
    print(f"{'CONFIRMED' if ok else 'MISMATCH'} {cid} {text}" + (f" -- {detail}" if detail else ""))
IDRE = re.compile(r'\bI[1-4]\.\d+\b')
def split_records(T, text):
    """Return list of (id, name, body) in file order."""
    # Run 1 required I1's bold title to close on the same line (six titles wrap) and parsed the inline
    # 'kind: … · level: … · status: …' lines of I2/I3 with a line-start regex; both fixed here, run 1 kept.
    if T == 'I1':
        pat = re.compile(r'^\*\*(I1\.\d+) — (.*?)\*\*', re.M | re.S)
    else:
        pat = re.compile(r'^### (%s\.\d+)\s*[—–-]?\s*(.*)$' % T, re.M)
    ms = list(pat.finditer(text))
    out = []
    for k, m in enumerate(ms):
        start = m.start(); end = ms[k + 1].start() if k + 1 < len(ms) else len(text)
        out.append((m.group(1), m.group(2).strip().strip('`').strip(), text[start:end]))
    return out
def field(body, name):
    # fields appear as '- name: …' / '- **name:** …' on their own line, or inline as 'name: X · level: Y · …'
    m = re.search(r'(?:^|\n)-\s*\**%s:?\**\s*:?\s*(.*?)(?=\s*·\s*\**(?:kind|level|status|flag|statement|provenance|depends_on|yields|bridge|bearing|note):?\**|\n-\s*\**[a-z_]+:?\**\s*:?|\n###|\n\*\*I|\Z)' % name, body, re.S)
    if m: return m.group(1).strip()
    m = re.search(r'\b%s:?\s+(.*?)(?=\s*·\s*(?:kind|level|status|flag|statement|provenance|depends_on|yields|bridge|bearing|note)\b|\n-\s|\Z)' % name, body, re.S)
    return m.group(1).strip() if m else ''
def first_status_word(s):
    s = s.lower().strip()
    for w in ['proved [k]', 'proved [m]', 'proved [manuscript', 'proved', 'assumed', 'conditional', 'open', 'refuted', 'empirically', 'definition', 'scope', 'pt-record', 'not at l', 'design', 'k', 'm', '-', '—']:
        if s.startswith(w): return w
    return s.split(' ')[0] if s else '?'
nodes = {}; edges = []; yields = []
expected = {'I1': 85, 'I2': 113, 'I3': 187, 'I4': 248}
for T in ['I1', 'I2', 'I3', 'I4']:
    text = open(os.path.join(ROOT, T, 'INVENTORY.md'), encoding='utf-8').read()
    recs = split_records(T, text)
    ids = [r[0] for r in recs]
    rec('N-' + T, len(set(ids)) == expected[T] and len(ids) == len(set(ids)), '%s: %d records parsed, no duplicate ids' % (T, len(set(ids))), 'first %s last %s' % (ids[0] if ids else '-', ids[-1] if ids else '-'))
    for rid, name, body in recs:
        kind = field(body, 'kind'); level = field(body, 'level'); status = field(body, 'status')
        dep = field(body, 'depends_on'); yl = field(body, 'yields')
        # run 3: newlines inside wrapped fields are folded to spaces so the tsv has one row per record (run 2 kept)
        fold = lambda z: ' '.join(z.split())
        nodes[rid] = dict(name=fold(name)[:80], kind=fold(kind.split('·')[0])[:60], level=fold(level.split('·')[0])[:20], status=first_status_word(fold(status.split('·')[0])))
        for d in sorted(set(IDRE.findall(dep))):
            if d != rid: edges.append((rid, d))
        for y in sorted(set(IDRE.findall(yl))):
            if y != rid: yields.append((rid, y))
allids = set(nodes)
dang_dep = sorted({d for _, d in edges if d not in allids}); dang_y = sorted({y for _, y in yields if y not in allids})
rec('D-dep', not dang_dep, 'every inventory id mentioned in a depends_on field exists', 'dangling: %s' % dang_dep[:20])
rec('D-yld', not dang_y, 'every inventory id mentioned in a yields field exists', 'dangling: %s' % dang_y[:20])
cross = [(a, b) for a, b in edges if a.split('.')[0] != b.split('.')[0]]
print('nodes %d; depends_on id-edges %d (cross-thread %d); yields id-edges %d' % (len(nodes), len(edges), len(cross), len(yields)))
from collections import Counter
for T in ['I1', 'I2', 'I3', 'I4']:
    c = Counter(nodes[i]['status'] for i in nodes if i.startswith(T + '.'))
    l = Counter(nodes[i]['level'] for i in nodes if i.startswith(T + '.'))
    print(T, 'status:', dict(c.most_common(8)), '| level:', dict(l.most_common(8)))
here = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(here, 'nodes.tsv'), 'w', encoding='utf-8') as f:
    f.write('id\tname\tkind\tlevel\tstatus\n')
    for i in sorted(nodes, key=lambda s: (int(s[1]), int(s.split('.')[1]))):
        n = nodes[i]; f.write('\t'.join([i, n['name'], n['kind'], n['level'], n['status']]) + '\n')
with open(os.path.join(here, 'edges_by_id.tsv'), 'w', encoding='utf-8') as f:
    f.write('from\tto\trelation\n')
    for a, b in edges: f.write('%s\t%s\tdepends_on\n' % (a, b))
    for a, b in yields: f.write('%s\t%s\tyields\n' % (a, b))
print('SUMMARY %d/%d CONFIRMED' % (sum(R), len(R)))
print('BASELINE-FIXED' if all(R) else 'BASELINE-MISMATCH')
