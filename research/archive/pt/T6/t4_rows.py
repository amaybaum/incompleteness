# t4_rows.py -- T6 node C2: the row-by-row check of the countermodel K(Z_F) against R6's audited Table A2 (the 199
# applicable items), with my own re-check attached to every row the verdict leans on.  Read-only; exact text work.
# DECISION RULE (fixed before the first run, 19:12:56Z by date -u):
#  Inputs (data): ../R6/REASSESSMENT.md Table A2 rows (between '### Table A2' and '### Table A3'); ../R6/r1_inventory.out
#   APPL lines (status, flag, level per id); ./t3_countermodel.out CHECK lines; the kernel tree at L.
#  For each of the 199 rows, by R6's class:
#   K-blind classes (def, thm, gate, inh, b1, d4s): the backticked identifiers of the row's statement column are looked
#     up as kernel declarations at L (regex on theorem|lemma|def|abbrev|structure|class); the row is KBLIND-OK iff
#     every found declaration's statement (text before ':=') binds no variable of type `Set (W …)` (binder regex
#     `[({] name : Set (W` or `∀ name : Set (W`; a definition whose own type is Set (W d), like maxCone, binds none);
#     it does not quantify over a pair cone, so it cannot tell K(Z_F) from Q3.  [Pre-run edit 19:14Z: the binder
#     regex replaces a substring test that would have caught result types.]  Rows with no kernel declaration found are listed
#     NO-DECL with R6's evidence string (single-token PT/ROADMAP items, [D] definitions) and read in TEST.md.
#   cone and kthm rows: each mapped (data below) to t3 CHECK ids; CONE-OK iff every mapped check PASSes in t3's output.
#   hmg rows: kernel items (I4.*) looked up; NR-OK iff every found declaration's module closure excludes
#     CompositeDimension; manuscript items (I1.17, I2.*) are NR by t1 (no bridge) and listed with their level.
#   nr rows: listed with R6's reason; NR-OK (no theorem at L quantifies over a pair cone other than the reflY no-go, t2).
#   dna, d4f, cand rows (R6: FAILS [hyp]) and d4v rows (SATISFIES vacuous): HYP-OK iff the r1 status does not begin
#     with 'proved [K]' and is not a definition, or the flag is 'do not assume'; the t3 witness ids are attached where
#     my verdict uses the failure ((b) forms, IE1, IE1Drive, K2 clause, Q3).
#  VERDICT ROWS-OK iff 199 rows, every K-blind row KBLIND-OK or NO-DECL, every cone/kthm row CONE-OK, every hmg kernel
#   row NR-OK, every FAILS row HYP-OK, and t3's VERDICT line is C1-KZF-EXACT.  Countercontrol CC: the K-blind test
#   applied to `no_candidateCone_cnot_reflY` (a pair-cone theorem) must report a `Set (W` binder.
import os, re

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.normpath(os.path.join(HERE, '..', 'base'))
TREE = os.path.join(BASE, 'verification', 'lean-mathlib', 'OIBridge')
mods = {fn[:-5]: os.path.join(TREE, fn) for fn in sorted(os.listdir(TREE)) if fn.endswith('.lean')}
text = {m: open(p, encoding='utf-8').read() for m, p in mods.items()}
imp_re = re.compile(r'^import\s+OIBridge\.([A-Za-z0-9_]+)\s*$', re.M)
imports = {m: sorted(set(x for x in imp_re.findall(t) if x in mods)) for m, t in text.items()}
def closure(m):
    seen, st = set(), [m]
    while st:
        x = st.pop()
        if x in seen: continue
        seen.add(x); st.extend(imports.get(x, []))
    return seen
decl_re = re.compile(r'^(?:@\[[^\]]*\]\s*)?(?:private\s+|protected\s+)?(?:noncomputable\s+)?'
                     r'(theorem|lemma|def|abbrev|structure|class)\s+([^\s(:{\[]+)', re.M)
DECL = {}
for m in sorted(mods):
    t = text[m]; ms = list(decl_re.finditer(t))
    for i, mt in enumerate(ms):
        end = ms[i + 1].start() if i + 1 < len(ms) else len(t)
        body = t[mt.start():end]
        st = body.split(':=')[0] if mt.group(1) not in ('structure', 'class') else body
        name = mt.group(2).split('.')[-1]
        DECL.setdefault(name, []).append((m, t.count('\n', 0, mt.start()) + 1, st))
BINDER = re.compile(r"[({]\s*[A-Za-z_][\w']*\s*:\s*Set \(W\b|∀\s*[A-Za-z_][\w']*\s*:\s*Set \(W\b")
def lookup(names):
    out = []
    for n in names:
        for m, line, st in DECL.get(n, []): out.append((n, m, line, st))
    return out

rows = []
sec = None
for ln in open(os.path.join(HERE, '..', 'R6', 'REASSESSMENT.md'), encoding='utf-8'):
    if ln.startswith('### Table A2'): sec = 'A2'; continue
    if ln.startswith('### Table A3'): sec = None
    if sec == 'A2' and ln.startswith('| I'):
        f = [x.strip() for x in ln.strip().strip('|').split('|')]
        rows.append(f)          # id, statement, class, verdict, evidence
appl = {}
for ln in open(os.path.join(HERE, '..', 'R6', 'r1_inventory.out'), encoding='utf-8'):
    if ln.startswith('APPL '):
        f = [x.strip() for x in ln[5:].split('|')]
        appl[f[0]] = f
t3 = open(os.path.join(HERE, 't3_countermodel.out'), encoding='utf-8').read()
t3pass = {m.group(1).strip(): m.group(2) == 'PASS' for m in re.finditer(r'^CHECK (.{30}) (PASS|FAIL)', t3, re.M)}
t3verdict = 'VERDICT C1-KZF-EXACT' in t3
def t3ok(ids): return all(any(k.startswith(i) and v for k, v in t3pass.items()) for i in ids)
CONEMAP = {
    'I3.43': ['Z3', 'Z1', 'Z2', 'Z4'], 'I3.114': ['Z3', 'Z1', 'Z2', 'Z4', 'Z5'], 'I3.116': ['Z3', 'Z1', 'Z2', 'Z4', 'Z5', 'Z8'],
    'I3.118': ['Z5', 'D0a'], 'I3.130': ['Z3', 'Z1', 'Z2', 'Z4'], 'I3.131': ['Z1', 'Z2', 'Z4'], 'I3.132': ['Z5', 'D0a'],
    'I3.147': ['Z3'], 'I3.148': ['Z5', 'D0a'], 'I3.149': ['Z1', 'Z2', 'Z4'], 'I3.156': ['Z5', 'D0a'],
    'I3.159': ['Z3', 'Z1', 'Z2', 'Z4', 'Z5', 'Z8'], 'I3.44': ['Z7']}
WIT = {'I3.137': ['B (b)', 'B flow'], 'I3.142': ['B (b)'], 'I3.144': ['Z6'], 'I3.150': ['B (b)', 'B flow'],
       'I3.153': ['B (b)', 'B flow'], 'I3.165': ['B (b)', 'B flow'], 'I3.155': ['B (b)']}
KBLIND = {'def', 'thm', 'gate', 'inh', 'b1', 'd4s'}
tally, bad, nodecl = {}, [], []
print('ROW id | R6 class | R6 verdict | T6 verdict | status at L (r1) | T6 re-check')
for f in rows:
    rid, stmt, cls, verd, evid = f[0], f[1], f[2], f[3], f[4]
    status = appl.get(rid, ['', '', '', '?'])[3]
    flag = appl.get(rid, ['', '', '', '', '-'])[4] if rid in appl else '-'
    names = re.findall(r'`([A-Za-z_][A-Za-z0-9_.]*)`', stmt)
    if cls in KBLIND:
        found = lookup(names)
        cone = [x for x in found if BINDER.search(x[3])]
        if found and not cone:
            t6, ev = 'SATISFIES', 'KBLIND-OK: %s' % ', '.join(sorted(set('%s %s.lean:%d' % (n, m, l) for n, m, l, _ in found))[:3])
        elif not found:
            t6, ev = 'SATISFIES', 'NO-DECL (R6: %s)' % evid[:70]; nodecl.append(rid)
        else:
            t6, ev = 'CHECK', 'pair-cone binder in %s' % cone[0][0]; bad.append(rid)
    elif cls in ('cone', 'kthm'):
        ids = CONEMAP.get(rid)
        ok = ids is not None and t3ok(ids)
        t6, ev = ('SATISFIES' if ok else 'CHECK'), 't3 %s' % ('+'.join(ids) if ids else 'UNMAPPED')
        if not ok: bad.append(rid)
    elif cls == 'hmg':
        found = lookup(names + [stmt.split()[0]] if stmt else names)
        reach = [x for x in found if 'CompositeDimension' in closure(x[1])]
        if rid.startswith('I4.'):
            ok = bool(found) and not reach
            t6, ev = ('NOT REACHED' if ok else 'CHECK'), 'NR-OK: %s' % ', '.join(sorted(set('%s %s.lean:%d' % (n, m, l) for n, m, l, _ in found))[:2]) if ok else 'module reaches CompositeDimension or not found'
            if not ok: bad.append(rid)
        else:
            t6, ev = 'NOT REACHED', 'manuscript level %s; no bridge at L (t1)' % appl.get(rid, ['', '', '?'])[2]
    elif cls == 'nr':
        t6, ev = 'NOT REACHED', 'R6: %s; no pair-cone theorem at L other than the reflY no-go (t2)' % evid[:60]
    else:   # dna, d4f, cand, d4v
        hyp = not status.startswith('proved [K]') and 'definition' not in status.split(';')[0] or 'do not assume' in flag
        if not hyp: bad.append(rid)
        wit = WIT.get(rid)
        if cls == 'd4v':
            t6 = 'SATISFIES (vacuous)'
            ev = 'its hypothesis fails: %s' % ('IE1 fails (t3 B)' if rid == 'I3.187' else 'H fails, contrapositive of the [D] theorem with IE1 failing (t3 B)')
        else:
            t6 = 'FAILS [hyp]'
            ev = ('t3 %s' % '+'.join(wit)) if wit and t3ok(wit) else 'R6 [A] (not used by the T6 verdict)'
        ev += ' | hypothesis status: %s' % ('yes' if hyp else 'NO')
    tally[t6] = tally.get(t6, 0) + 1
    print('ROW %s | %s | %s | %s | %s | %s' % (rid, cls, verd[:22], t6, status[:48], ev))
print('TALLY %s' % ', '.join('%s %d' % (k, tally[k]) for k in sorted(tally)))
print('NO-DECL rows (%d): %s' % (len(nodecl), ', '.join(nodecl)))
cc = any(BINDER.search(st) for _, _, _, st in lookup(['no_candidateCone_cnot_reflY']))
cc &= not any(BINDER.search(st) for _, _, _, st in lookup(['maxCone']))
print('CC no_candidateCone_cnot_reflY carries a pair-cone binder: %s' % cc)
ok = len(rows) == 199 and not bad and t3verdict and cc
print('VERDICT ROWS-OK: 199 rows; %s; every cone row backed by a PASS of t3; every FAILS row a hypothesis' % ', '.join('%s %d' % (k, tally[k]) for k in sorted(tally))
      if ok else 'VERDICT NONE: rows=%d bad=%s t3verdict=%s cc=%s' % (len(rows), bad, t3verdict, cc))
