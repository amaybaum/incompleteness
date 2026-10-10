# r1_inventory.py -- R6 node R1: the applicable-item list from the frozen step-1 inventories (read-only).
#
# DECISION RULE (fixed before the first run, 18:10Z):
#  Inputs (read-only): pt/I1/INVENTORY.md, pt/I2/INVENTORY.md, pt/I3/INVENTORY.md, pt/I3/r0lists.out, pt/I4/records.txt.
#  Parse every record: I1 '**I1.n — ...**' blocks, I2 and I3 '### Ik.n' blocks, I4 the 12-field records.txt lines.
#  Bearing class of an I3 record, from the text after 'bearing:' (prefix rule, applied in this order):
#    'direct' -> direct ; 'constrains the single-token structure the pair inherits' -> inherits ;
#    'constrains the composite only through' -> bridge ; [run 2] any other text containing 'only through' -> bridge ;
#    'constrains the single-token structure' -> notread ; 'none at L' -> none.
#  RUN-2 AMENDMENT (18:13Z, after run 1 failed C2 and C3; run 1 kept as r1_inventory.run1.*): (a) I3's own lists put
#    I3.96 and I3.99 ('constrains the single-token structure; at the pair level only through P-STAGE2/P-ACT2') under
#    'through bridge', so a record whose bearing names 'only through' is class bridge unless it begins with the
#    'inherits' phrase; (b) records.txt writes the I4 bearing as 'none' and the flag as 'DNA ;; ...': I4 bearing is
#    none iff it begins with 'none', do-not-assume iff the flag begins with 'DNA'. The controls are unchanged.
#  RUN-3 FIX (18:15Z): run 2 (kept as r1_inventory.run2.*) placed the new 'only through' test after the 'notread'
#    test, so it never fired; run 3 applies the run-2 rule in the order stated above. No rule or control changed.
#  CONTROLS (all must hold, else no VERDICT line):
#    C1 record counts I1 85, I2 113, I3 187, I4 248 (the threads' RESULT §0 counts);
#    C2 I3 bearing tally 80/25/20/17/45 and, class by class, the same id sets as I3's own r0lists.out;
#    C3 I4: exactly one record with bearing other than 'none at L', and it is I4.236; 44 records flagged do-not-assume;
#    C4 I2: no record with bearing other than 'none at L'; the do-not-assume flags are exactly I2.3, I2.29-I2.35,
#       I2.62, I2.63, I2.69 (I2 RESULT §0);
#    C5 I1: I1.17 is the one record whose bearing names 'constrains the composite only through' (I1 RESULT §0);
#    C6 countercontrol: the same prefix rule applied to a shuffled copy of the I3 bearing texts must NOT reproduce
#       r0lists.out (the comparison is not vacuous).
#  OUTPUT: one line per applicable item 'APPL <id> | <class> | <level> | <status, 60 chars> | <flag, 40 chars> | <title>':
#    I3 records with class != none, I4.236, I1.17, the 44 I4 and 11 I2 do-not-assume records (class 'HMG-dna').
import re, random, sys

PT = '/tmp/claude-0/-home-user-incompleteness/727ddb71-72ba-5388-a9a1-1413a0433ac0/scratchpad/pt'

def rd(p):
    with open(PT + '/' + p, encoding='utf-8') as f:
        return f.read()

def blocks(text, head_re):
    out, cur, cid = [], [], None
    for line in text.split('\n'):
        m = re.match(head_re, line)
        if m:
            if cid is not None:
                out.append((cid, cur))
            cid, cur = m.group(1), [line]
        elif cid is not None:
            if line.startswith('## ') or line.startswith('***'):
                out.append((cid, cur)); cid, cur = None, []
            else:
                cur.append(line)
    if cid is not None:
        out.append((cid, cur))
    return out

def joined(lines):
    s = '\n'.join(lines)
    return re.sub(r'\n\s+(?!- )', ' ', s)

def field(s, name, stops):
    m = re.search(re.escape(name) + r':\s*(.*?)(?=' + '|'.join(stops) + r'|\Z)', s, re.S)
    return re.sub(r'\s+', ' ', m.group(1)).strip() if m else ''

def bclass(b):
    b = b.strip().strip('*').strip()
    if b.startswith('direct'): return 'direct'
    if b.startswith('constrains the single-token structure the pair inherits'): return 'inherits'
    if b.startswith('constrains the composite only through'): return 'bridge'
    if 'only through' in b and b.startswith('constrains the single-token structure'): return 'bridge'
    if b.startswith('constrains the single-token structure'): return 'notread'
    if b.startswith('none at L'): return 'none'
    return 'UNCLASSIFIED'

ok = {}
# ---- I3
i3 = blocks(rd('I3/INVENTORY.md'), r'^### (I3\.\d+)\b')
rec3 = {}
for cid, lines in i3:
    s = joined(lines)
    title = lines[0].split(' ', 2)[2] if len(lines[0].split(' ', 2)) > 2 else ''
    kind = field(s, 'kind', [r' · level:'])
    level = field(s, 'level', [r' · status:'])
    status = field(s, 'status', [r'\n- '])
    bearing = field(s, '- bearing', [r' · flag:', r'\n- ']) or field(s, 'bearing', [r' · flag:', r'\n- '])
    flag = field(s, 'flag', [r'\n- ', r'\n###'])
    rec3[cid] = dict(title=title, kind=kind, level=level, status=status, bearing=bearing, flag=flag,
                     cls=bclass(bearing))
ok['C1-I3'] = len(rec3) == 187
r0 = rd('I3/r0lists.out')
lab = {'direct': r'\*\*direct\*\*', 'inherits': r'\*\*single-token inherited\*\*',
       'notread': r'\*\*single-token \(not inherited\)\*\*', 'bridge': r'\*\*through bridge\*\*',
       'none': r'\*\*none at L\*\*'}
ref = {}
for k, pat in lab.items():
    m = re.search(pat + r' \((\d+)\):(.*)', r0)
    ref[k] = (int(m.group(1)), set(re.findall(r'I3\.\d+', m.group(2)))) if m else (-1, set())
mine = {k: {c for c, r in rec3.items() if r['cls'] == k} for k in lab}
tally = {k: len(v) for k, v in mine.items()}
ok['C2-tally'] = tally == {'direct': 80, 'inherits': 25, 'notread': 20, 'bridge': 17, 'none': 45}
ok['C2-sets'] = all(mine[k] == ref[k][1] and ref[k][0] == len(ref[k][1]) for k in lab)
unclassified = sorted(c for c, r in rec3.items() if r['cls'] == 'UNCLASSIFIED')
# countercontrol C6: shuffle bearing texts across records
rng = random.Random(20261010)
ids = sorted(rec3, key=lambda c: int(c.split('.')[1]))
texts = [rec3[c]['bearing'] for c in ids]
rng.shuffle(texts)
shuf = {k: {c for c, t in zip(ids, texts) if bclass(t) == k} for k in lab}
ok['C6-countercontrol'] = any(shuf[k] != ref[k][1] for k in lab)
# ---- I4
rec4 = {}
for line in rd('I4/records.txt').split('\n'):
    if not line.strip() or line.startswith('#'):
        continue
    f = [x.strip() for x in line.split(' ¦ ')]
    if len(f) >= 11 and re.match(r'I4\.\d+$', f[0]):
        rec4[f[0]] = dict(title=f[2], kind=f[3], status=f[4], level=f[5], bridge=f[8], bearing=f[9], flag=f[10])
ok['C1-I4'] = len(rec4) == 248
nn4 = sorted(c for c, r in rec4.items() if not r['bearing'].startswith('none'))
ok['C3-bearing'] = nn4 == ['I4.236']
dna4 = sorted((c for c, r in rec4.items() if r['flag'].startswith('DNA')), key=lambda c: int(c.split('.')[1]))
ok['C3-dna44'] = len(dna4) == 44
# ---- I2
i2 = blocks(rd('I2/INVENTORY.md'), r'^### (I2\.\d+)\b')
rec2 = {}
for cid, lines in i2:
    s = joined(lines)
    rec2[cid] = dict(title=lines[0].split(' — ', 1)[-1], level=field(s, 'level', [r' · status:']),
                     status=field(s, 'status', [r' · flag:', r'\n- ']), flag=field(s, 'flag', [r'\n- ']),
                     bearing=field(s, 'bearing', [r'\n- ', r'\n###', r'\Z']))
ok['C1-I2'] = len(rec2) == 113
nn2 = sorted(c for c, r in rec2.items() if r['bearing'] and not r['bearing'].startswith('none at L'))
nobear2 = sorted(c for c, r in rec2.items() if not r['bearing'])
dna2 = sorted((c for c, r in rec2.items() if r['flag'].startswith('do not assume')), key=lambda c: int(c.split('.')[1]))
want2 = ['I2.3'] + ['I2.%d' % n for n in range(29, 36)] + ['I2.62', 'I2.63', 'I2.69']
ok['C4-bearing'] = nn2 == []
ok['C4-dna'] = dna2 == want2
# ---- I1
t1 = rd('I1/INVENTORY.md')
i1 = blocks(t1, r'^\*\*(I1\.\d+) — ')
ok['C1-I1'] = len(i1) == 85
b1 = {}
for cid, lines in i1:
    s = joined(lines)
    b1[cid] = field(s, 'bearing', [r' · flag', r'\n- ', r'\n\*\*', r'\Z'])
thr1 = sorted(c for c, b in b1.items() if 'constrains the composite only through' in b)
ok['C5-I1.17'] = thr1 == ['I1.17']
# ---- output
print('R1 applicable-item list (exact parse of the frozen step-1 inventories)')
print('UNCLASSIFIED I3 bearings:', unclassified if unclassified else 'none')
print('I3 tally:', tally, '| r0lists:', {k: ref[k][0] for k in lab})
print('I4 non-none bearing:', nn4, '| I4 do-not-assume:', len(dna4))
print('I2 non-none bearing:', nn2, '| I2 records without a parsed bearing field:', len(nobear2), '| I2 do-not-assume:', dna2)
print('I1 records naming a bridge in the bearing field:', thr1)
appl = []
for c in ids:
    r = rec3[c]
    if r['cls'] != 'none':
        appl.append((c, r['cls'], r['level'], r['status'], r['flag'], r['title']))
r = rec4['I4.236']; appl.append(('I4.236', 'inherits', r['level'], r['status'], r['flag'], r['title']))
appl.append(('I1.17', 'HMG-bridge-none', 'H', 'conditional-on (I1 record)', '-', 'layered theorem statement (Main.md:82)'))
for c in dna4:
    r = rec4[c]; appl.append((c, 'HMG-dna', r['level'], r['status'], r['flag'], r['title']))
for c in dna2:
    r = rec2[c]; appl.append((c, 'HMG-dna', r['level'], r['status'], r['flag'], r['title']))
def cut(x, n):
    x = re.sub(r'\s+', ' ', x); return x if len(x) <= n else x[:n - 1] + '…'
for a in appl:
    print('APPL %s | %s | %s | %s | %s | %s' % (a[0], a[1], cut(a[2], 18), cut(a[3], 60), cut(a[4], 40), cut(a[5], 70)))
print('applicable items:', len(appl), '= I3', sum(1 for a in appl if a[0].startswith('I3.')), '+ I4.236 + I1.17 +',
      len(dna4), 'I4 dna +', len(dna2), 'I2 dna')
for k in sorted(ok):
    print('CHECK', k, 'PASS' if ok[k] else 'FAIL')
if all(ok.values()) and not unclassified:
    print('VERDICT R1-ITEMS-EXACT: %d applicable items; I3 classes reproduce r0lists.out; controls green' % len(appl))
else:
    print('NO VERDICT (a control failed)')
