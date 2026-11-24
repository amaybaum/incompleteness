"""Parity of per-splice register/register-caps/infinity (DESIGN-v5.2 sec. 6.1) with P's per-edit static_new.
(1) Frozen data: P's own static_new over P's edits.json, and the per-splice computation (image against the
H bytes it replaces), with P's sentence split and with splitter v2. (2) Constructed two-step and merged-splice
cases showing that per-splice and per-edit results can differ."""
import sys, os, json, re, subprocess, importlib.util, hashlib, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rv5_rules as r
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
assert hashlib.sha256(open(os.path.join(D, 'edits_check.py'), 'rb').read()).hexdigest().startswith('2856e58c')
spec = importlib.util.spec_from_file_location('pec', os.path.join(D, 'edits_check.py'))
ec = importlib.util.module_from_spec(spec); spec.loader.exec_module(ec)
edits = json.load(open(os.path.join(D, 'edits.json'))); led = json.load(open(os.path.join(D, 'ledger.json')))
inf, reg, caps, ids = ec.static_new(edits)
print('P static_new over frozen edits: infinity', len(inf), 'register', len(reg), 'caps', len(caps))
H = '53c6601a10419b6b333cc992474272501ab542af'
cache = {}
def blob(f):
    if f not in cache: cache[f] = subprocess.run(['git', '-C', '<repo>', 'show', H + ':' + f], capture_output=True).stdout
    return cache[f]
kind = {e['id']: e.get('kind') for e in edits['edits']}
def per_pair(old, new, k, splitter):
    def assertions(text):
        out = []
        for sent in splitter(text):
            spans = [m.span() for m in ec.NEUTRAL.finditer(sent)]
            out += [m.group(0) for m in ec.INF.finditer(sent) if not any(a <= m.start() and m.end() <= b for a, b in spans)]
        return out
    a_new = assertions(new); a_old = assertions(re.sub(r'\bA1\b(?: \(finiteness\))?', 'finiteness', old))
    extra = collections.Counter(ec.inf_key(x) for x in a_new) - collections.Counter(ec.inf_key(x) for x in a_old)
    rg = set(x.lower() for x in ec.REG.findall(new)) - set(x.lower() for x in ec.REG.findall(old))
    cp = (set(ec.CAPS.findall(new)) - set(ec.CAPS.findall(old)) - ec.CAPS_OK) if k in ('ptr', 'consistency', 'handoff') else set()
    return sum(extra.values()), len(rg), len(cp)
v2 = lambda t: [s for lns, p in r.paragraphs(t.split('\n'), 2) for s in r.split_sentences(p, 2)] or [t]
for name, spl in (('P sentences()', ec.sentences), ('splitter v2', v2)):
    tot = [0, 0, 0]
    for s in led['splices']:
        old = blob(s['file'])[s['start']:s['end']].decode()
        res = per_pair(old, s['new'], kind[s['id']], spl)
        tot = [a + b for a, b in zip(tot, res)]
    print('per-splice (%s): infinity %d register %d caps %d' % (name, *tot))
# constructed cases
print('--- constructed cases (per-edit = P static_new on a one-edit list; per-splice = composite H->final) ---')
def p_edit(e):
    i, rg, c, _ = ec.static_new({'edits': [e]}); return len(i), len(rg), len(c)
cases = []
# (a) two-step: step 1 removes "now", step 2 re-adds it inside the step-1 text
H0 = 'The bound is now stated for the finite case.'
mid = 'The bound is stated for the finite case.'
fin = 'The bound is now stated for the finite case.'
cases.append(('a two-step reintroduces "now"', {'id': 'T1', 'kind': 'ptr', 'old': H0, 'new': mid, 'old_step2': 'is stated', 'new_step2': 'is now stated'}, H0, fin))
# (b) two-step: step 1 adds "no longer", step 2 removes it
H1 = 'The result holds for the finite case.'
mid1 = 'The result no longer holds for the finite case.'
fin1 = 'The result holds for the finite case.'
cases.append(('b two-step adds then removes', {'id': 'T2', 'kind': 'ptr', 'old': H1, 'new': mid1, 'old_step2': 'no longer holds', 'new_step2': 'holds'}, H1, fin1))
# (c) one splice covering two edits: edit 1 deletes "now" elsewhere, edit 2 adds "now"
cases.append(('c merged splice of two edits', None, 'It is now open. The case is finite.', 'It is open. The case is now finite.'))
for label, e, old, new in cases:
    pe = p_edit(e) if e else (p_edit({'id': 'c1', 'kind': 'ptr', 'old': 'It is now open.', 'new': 'It is open.'})[1] + p_edit({'id': 'c2', 'kind': 'ptr', 'old': 'The case is finite.', 'new': 'The case is now finite.'})[1],)
    ps = per_pair(old, new, 'ptr', ec.sentences)
    print('%-34s per-edit register=%s | per-splice register=%d' % (label, pe[1] if e else pe[0], ps[1]))
