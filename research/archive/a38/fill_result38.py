"""Fill result38.draft.md -> rec/result.md for A38-NON-DITA-WITNESS-PROVED. Reads runs38.txt (the runs table),
fcomment38.txt (the owner's designation comment id for F), fmeta38.json ({pr, F, F_run, road_blob}) beside it."""
import importlib.util, os, re, hashlib, json
S = os.path.dirname(os.path.abspath(__file__)) + '/'
spec = importlib.util.spec_from_file_location('c38', S + 'rec/controls.py'); C = importlib.util.module_from_spec(spec); spec.loader.exec_module(C)
L = 'A38-NON-DITA-WITNESS-PROVED'
src = open(S + 'mod38v.lean', encoding='utf-8').read(); n = len(C.theorems(C.strip_comments(src)))
WORDS = {122: 'one hundred and twenty-two', 121: 'one hundred and twenty-one', 123: 'one hundred and twenty-three', 124: 'one hundred and twenty-four'}
def blob_of(path):
    b = open(path, 'rb').read(); return hashlib.sha1(b'blob %d\0' % len(b) + b).hexdigest()
log = open(S + 'probe38.log', encoding='utf-8').read()
probeline = [l for l in log.split('\n') if l.startswith('dita_local_escape_probe: OK')][0]
npass = len(re.findall(r'(?m)^\s+PASS\s', log))
meta = json.load(open(S + 'fmeta38.json'))
DEV = open(S + 'deviations38.txt', encoding='utf-8').read().strip()
RUNS = open(S + 'runs38.txt', encoding='utf-8').read().strip()
FCOMMENT = open(S + 'fcomment38.txt', encoding='utf-8').read().strip()
DISC = open(S + 'discrepancies38.txt', encoding='utf-8').read().strip()
CL = '> **' + C.MENTION + ' — the result note.**\n' + '\n'.join('> ' + l for l in C.CLAUSE.split('\n'))
bad, rows, dmuts, muts = C.self_test()
assert [b for b in bad if not b.startswith('agreement')] == [], bad
t = open(S + 'result38.draft.md', encoding='utf-8').read()
rep = {'@@SENTENCE@@': C.SENTENCES[L], '@@NTHM@@': WORDS.get(n, str(n)), '@@DEVIATIONS@@': DEV, '@@PROBELINE@@': probeline, '@@RUNS@@': RUNS,
       '@@DISCREPANCIES@@': DISC, '@@CLAUSE@@': CL, '@@PR@@': str(meta['pr']), '@@F@@': meta['F'],
       '@@PREREG_BLOB@@': blob_of(S + 'rec/preregistration.md'), '@@F_RUN@@': str(meta['F_run']), '@@F_COMMENT@@': FCOMMENT,
       '@@PROBE_BLOB@@': C.PROBE_BLOB, '@@NPASS@@': str(npass), '@@ROAD_BLOB@@': meta['road_blob'],
       '@@CONTROLS_BLOB@@': blob_of(S + 'rec/controls.py'), '@@NMUTS@@': str(muts)}
for k, v in rep.items():
    assert t.count(k) >= 1, k; t = t.replace(k, v)
assert '@@' not in t, re.findall(r'@@[A-Z0-9_]+@@', t)
open(S + 'rec/result.md', 'w', encoding='utf-8').write(t)
print('note_ok:', C.note_ok(t, L)); print('bytes', len(t.encode()), 'theorems', n)
