#!/usr/bin/env python3
"""G6 parse.py -- uniform node table of the four step-1 inventories (read-only; stdout only).

Run from pt/G6/ as `python3 -I -B parse.py`. Reads ../I1/INVENTORY.md, ../I2/INVENTORY.md, ../I3/INVENTORY.md,
../I4/records.txt (I4's machine-readable source). Writes nothing; prints tables to stdout.

DECISION RULE (fixed before the first run):
  P1  record counts I1 85, I2 113, I3 187, I4 248, and ids 1..n contiguous in each inventory.         PASS/FAIL
  P2  every record has a non-empty kind, level and status, and a depends_on field (possibly '-').      PASS/FAIL
  P3  every id token in a depends_on field names an existing record (dangling ids are listed).         PASS/FAIL
  C1  countercontrol: the id extractor on the synthetic text 'I3.999; I3.13-I3.15; as I3.37' (en dash)
      must report I3.999 dangling, expand the range to exactly I3.13, I3.14, I3.15, and return I3.37 as an
      'as' reference (inherit), not as a plain edge.                                                    PASS/FAIL
  A line 'VERDICT PARSE VALID' prints only if P1, P2, P3 and C1 all pass.
Tables: '#T nodes' (one row per record), '#T idedges' (R and RA edges from depends_on ids),
'#T yedges' (Y: ids named in a yields field), '#T names' (backticked names in titles -> ids).
Fields are tab-separated; tabs and newlines inside fields are replaced by single spaces.
"""
import re

INV = {'I1': '../I1/INVENTORY.md', 'I2': '../I2/INVENTORY.md', 'I3': '../I3/INVENTORY.md'}
I4SRC = '../I4/records.txt'
EXPECT = {'I1': 85, 'I2': 113, 'I3': 187, 'I4': 248}
HDR = {'I1': re.compile(r'^\*\*(I1\.\d+) — '), 'I2': re.compile(r'^### (I2\.\d+) — '),
       'I3': re.compile(r'^### (I3\.\d+)[ ]')}
RANGE = re.compile(r'(I[1-4])\.(\d+)\s*[–-]\s*(?:I[1-4]\.)?(\d+)')
IDRE = re.compile(r'(?<![\w.])I[1-4]\.\d+(?![\d])')
ASRE = re.compile(r'\bas (I[1-4]\.\d+)((?:\s*(?:,|and)\s*I[1-4]\.\d+)*)')
STOP = re.compile(r'(?:\s·\s|\.\s|;\s|\s)(?:yields|bridge|bearing|flag|provenance|scope|statement|'
                  r'lemma-folded|depends_on)\s*:')
BT = re.compile(r'`([^`]+)`')
IDENT = re.compile(r"^[A-Za-z_][A-Za-z0-9_'.₀-₉ᵢⱼ]*$")


def clean(s):
    return re.sub(r'\s+', ' ', s.replace('\t', ' ')).strip()


def blocks(inv):
    lines = open(INV[inv], encoding='utf-8').read().split('\n')
    recs, cur = [], None
    for ln in lines:
        m = HDR[inv].match(ln)
        if m:
            if cur:
                recs.append(cur)
            cur = [m.group(1), [ln]]
            continue
        if cur is None:
            continue
        if ln.startswith('***') or ln.startswith('## '):
            recs.append(cur)
            cur = None
            continue
        cur[1].append(ln)
    if cur:
        recs.append(cur)
    return recs


def split_bullets(lines):
    head, bullets = [], []
    for ln in lines:
        if ln.startswith('- '):
            bullets.append(ln[2:])
        elif bullets and ln.startswith('  '):
            bullets[-1] += ' ' + ln.strip()
        elif not bullets:
            head.append(ln)
    return clean(' '.join(head)), [clean(b) for b in bullets]


def field(bullets, key):
    for b in bullets:
        m = re.search(r'(?:^|\s|·|\.)' + key + r'\s*:', b)
        if not m:
            continue
        rest = b[m.end():]
        s = STOP.search(rest)
        return clean(rest[:s.start()] if s else rest)
    return None


def parse_i1(recs):
    out = []
    for rid, lines in recs:
        head, bullets = split_bullets(lines)
        mt = re.match(r'\*\*I1\.\d+ — (.*?)\*\*(.*)$', head)
        title, rest = (mt.group(1), mt.group(2)) if mt else (head, '')
        mk = re.search(r'kind (.*?) · level (.*?) · status:? (.*?) · flag (.*)$', rest)
        kind, level, status, flag = (mk.groups() if mk else ('', '', '', ''))
        out.append(dict(id=rid, title=clean(title), kind=clean(kind), level=clean(level),
                        status=clean(status), flag=clean(flag), dep=field(bullets, 'depends_on'),
                        yields=field(bullets, 'yields'), bridge=field(bullets, 'bridge'),
                        bearing=field(bullets, 'bearing'), src=clean(' '.join(bullets[:2]))[:400]))
    return out


def parse_i2(recs):
    out = []
    for rid, lines in recs:
        head, bullets = split_bullets(lines)
        title = re.sub(r'^### I2\.\d+ — ', '', head)
        kb = next((b for b in bullets if b.startswith('kind:')), '')
        mk = re.search(r'kind: (.*?) · level: (.*?) · status: (.*?) · flag: (.*)$', kb)
        kind, level, status, flag = (mk.groups() if mk else ('', '', '', ''))
        stm = [b for b in bullets if b.startswith('statement')]
        out.append(dict(id=rid, title=clean(title), kind=clean(kind), level=clean(level),
                        status=clean(status), flag=clean(flag), dep=field(bullets, 'depends_on'),
                        yields=field(bullets, 'yields'), bridge=field(bullets, 'bridge'),
                        bearing=field(bullets, 'bearing'), src=clean(' '.join(stm))[:400]))
    return out


def parse_i3(recs):
    out = []
    for rid, lines in recs:
        head, bullets = split_bullets(lines)
        title = re.sub(r'^### I3\.\d+ ', '', head)
        kb = next((b for b in bullets if b.startswith('kind:')), '')
        mk = re.search(r'kind: (.*?) · level: (.*?) · status: (.*)$', kb)
        kind, level, status = (mk.groups() if mk else ('', '', ''))
        fl = field(bullets, 'flag')
        stm = [b for b in bullets if b.startswith('statement')]
        out.append(dict(id=rid, title=clean(title), kind=clean(kind), level=clean(level),
                        status=clean(status), flag=clean(fl or ''), dep=field(bullets, 'depends_on'),
                        yields=field(bullets, 'yields'), bridge=field(bullets, 'bridge'),
                        bearing=field(bullets, 'bearing'), src=clean(' '.join(stm))[:400]))
    return out


def parse_i4():
    out = []
    for ln in open(I4SRC, encoding='utf-8').read().split('\n'):
        if not ln.startswith('I4.'):
            continue
        f = ln.split(' ¦ ')
        if len(f) != 12:
            out.append(dict(id=f[0], title='', kind='', level='', status='', flag='', dep=None,
                            yields='', bridge='', bearing='', src='BADROW'))
            continue
        out.append(dict(id=f[0], title=clean(f[2]), kind=clean(f[3]), level=clean(f[5]),
                        status=clean(f[4]), flag=clean(f[10]), dep=clean(f[6]), yields=clean(f[7]),
                        bridge=clean(f[8]), bearing=clean(f[9]), src=clean(f[1])))
    return out


def extract_ids(text):
    """Return (plain ids, 'as' ids) from a depends_on text; ranges expanded."""
    if not text:
        return [], []
    as_ids = []
    for m in ASRE.finditer(text):
        as_ids.append(m.group(1))
        as_ids += re.findall(r'I[1-4]\.\d+', m.group(2))
    t = ASRE.sub(' ', text)
    plain = []
    for m in RANGE.finditer(t):
        a, b = int(m.group(2)), int(m.group(3))
        if a < b <= a + 60:
            plain += ['%s.%d' % (m.group(1), k) for k in range(a, b + 1)]
    t = RANGE.sub(' ', t)
    plain += IDRE.findall(t)
    seen, res = set(), []
    for x in plain:
        if x not in seen:
            seen.add(x)
            res.append(x)
    return res, as_ids


def title_names(rec):
    """Backticked identifiers of a title (I1-I3), or the I4 name; returned as a list."""
    if rec['id'].startswith('I4.'):
        nm = re.sub(r'\s*\(.*$', '', rec['title']).strip()
        return [nm] if nm else []
    res = []
    for x in BT.findall(rec['title']):
        for part in re.split(r'[,/ ]+', x):
            part = part.strip()
            if part and IDENT.match(part) and not re.match(r'^I[1-4]\.\d+$', part):
                res.append(part)
    return res


def main():
    recs = (parse_i1(blocks('I1')) + parse_i2(blocks('I2')) + parse_i3(blocks('I3')) + parse_i4())
    byid = {r['id']: r for r in recs}
    ok = {}
    # P1
    p1 = True
    for inv, n in EXPECT.items():
        ids = [r['id'] for r in recs if r['id'].startswith(inv + '.')]
        nums = sorted(int(x.split('.')[1]) for x in ids)
        if len(ids) != n or nums != list(range(1, n + 1)) or len(set(ids)) != len(ids):
            p1 = False
            print('P1 FAIL %s count=%d' % (inv, len(ids)))
    ok['P1'] = p1
    # P2
    p2 = True
    for r in recs:
        if not (r['kind'] and r['level'] and r['status']) or r['dep'] is None:
            p2 = False
            print('P2 MISSING-FIELD %s kind=%r level=%r status=%r dep=%r' % (
                r['id'], r['kind'][:20], r['level'][:20], r['status'][:20], r['dep']))
    ok['P2'] = p2
    # P3 and edges
    idedges, yedges, dangling = [], [], []
    for r in recs:
        plain, as_ids = extract_ids(r['dep'] or '')
        for t in plain:
            (idedges if t in byid else dangling).append((r['id'], t, 'R'))
        for t in as_ids:
            (idedges if t in byid else dangling).append((r['id'], t, 'RA'))
        yp, ya = extract_ids(r['yields'] or '')
        for t in yp + ya:
            if t in byid and t != r['id']:
                yedges.append((t, r['id'], 'Y'))
    for d in dangling:
        print('P3 DANGLING %s -> %s (%s)' % d)
    ok['P3'] = not dangling
    # C1 countercontrol
    plain, as_ids = extract_ids('I3.999; I3.13–I3.15; as I3.37')
    c1 = (plain == ['I3.13', 'I3.14', 'I3.15', 'I3.999'] and as_ids == ['I3.37']
          and 'I3.999' not in byid)
    ok['C1'] = c1
    print('C1 synthetic: plain=%s as=%s dangling_check=%s' % (plain, as_ids, 'I3.999' not in byid))
    # tables
    print('#T nodes\tid\ttitle\tkind\tlevel\tstatus\tflag\tdepends_on\tyields\tbridge\tbearing\tsrc')
    for r in recs:
        print('\t'.join(['N', r['id'], r['title'], r['kind'], r['level'], r['status'], r['flag'],
                         r['dep'] or '', r['yields'] or '', r['bridge'] or '', r['bearing'] or '',
                         r['src']]))
    print('#T idedges\tsrc\tdst\tkind')
    for e in idedges:
        print('E\t%s\t%s\t%s' % e)
    print('#T yedges\tsrc\tdst\tkind')
    for e in sorted(set(yedges)):
        print('Y\t%s\t%s\t%s' % e)
    print('#T names\tname\tid')
    for r in recs:
        for nm in title_names(r):
            print('M\t%s\t%s' % (nm, r['id']))
    for k in ('P1', 'P2', 'P3', 'C1'):
        print('%s %s' % (k, 'PASS' if ok[k] else 'FAIL'))
    print('counts: records=%d idedges=%d yedges=%d dangling=%d' % (
        len(recs), len(idedges), len(set(yedges)), len(dangling)))
    if all(ok.values()):
        print('VERDICT PARSE VALID')


if __name__ == '__main__':
    main()
