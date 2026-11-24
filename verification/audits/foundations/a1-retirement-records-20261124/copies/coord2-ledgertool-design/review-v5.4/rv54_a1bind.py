"""A1: apply P's 401 edits in list order (P's variant selection on a running copy of each file at H) and bind
each applied occurrence, mapped back to byte offsets at H, to its splice (DESIGN-v5.4 sec. 6.1)."""
import importlib.util, hashlib, os, json, subprocess, collections
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
assert hashlib.sha256(open(os.path.join(D, 'edits_check.py'), 'rb').read()).hexdigest().startswith('2856e58c')
spec = importlib.util.spec_from_file_location('pec', os.path.join(D, 'edits_check.py')); ec = importlib.util.module_from_spec(spec); spec.loader.exec_module(ec)
H = '53c6601a10419b6b333cc992474272501ab542af'
edits = json.load(open(os.path.join(D, 'edits.json')))['edits']; led = json.load(open(os.path.join(D, 'ledger.json')))
sp = {s['id']: s for s in led['splices']}; retained = set(led['retained_unchanged'])
text = {}; applied = collections.defaultdict(list)  # per file: list of (H_start, H_end, delta) of applied edits
res = collections.Counter(); bad = []
for e in edits:
    f = e['file']
    if f not in text: text[f] = subprocess.run(['git', '-C', '<repo>', 'show', '%s:%s' % (H, f)], capture_output=True, check=True).stdout.decode()
    o, n, which = ec.variant(e, text[f])
    if o is None: res['lost'] += 1; bad.append(e['id']); continue
    i = text[f].index(o)
    # map running-copy char offset to H char offset through earlier applied edits
    hpos = i
    for (hs, he, d, rs, re_) in applied[f]:
        run_start = hs + sum(d2 for (hs2, _, d2, _, _) in applied[f] if hs2 < hs)
        if run_start + (he - hs) + d <= i: hpos -= d
    ht = subprocess.run(['git', '-C', '<repo>', 'show', '%s:%s' % (H, f)], capture_output=True, check=True).stdout.decode() if False else None
    text[f] = text[f][:i] + n + text[f][i + len(o):]
    applied[f].append((hpos, hpos + len(o), len(n) - len(o), i, i + len(n)))
    if e['id'] in retained:
        res['retained' + ('-identity' if o == n and e['id'] not in sp else '-BAD')] += 1; continue
    s = sp.get(e['id'])
    if s is None: res['no-splice'] += 1; bad.append(e['id']); continue
    Hb = subprocess.run(['git', '-C', '<repo>', 'show', '%s:%s' % (H, f)], capture_output=True, check=True).stdout
    Hs = Hb.decode()
    bs = len(Hs[:hpos].encode()); be = bs + len(o.encode())
    ok = (which == 'old' and bs == s['start'] and be == s['end'] and Hb[bs:be].decode() == o and s['new'] == n)
    res['bound' if ok else 'MISMATCH'] += 1
    if not ok: bad.append(e['id'])
print(dict(res), 'problems', bad[:10])
