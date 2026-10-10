"""Fill result37.draft.md -> rec/result.md for A37-EXCLUSIVITY-PROVED. Reads runs37.txt (the runs table) and
fcomment37.txt (the owner's designation comment id for F) beside it."""
import importlib.util, os, re, hashlib
S = os.path.dirname(os.path.abspath(__file__)) + '/'
spec = importlib.util.spec_from_file_location('c37', S + 'rec/controls.py'); C = importlib.util.module_from_spec(spec); spec.loader.exec_module(C)
L = 'A37-EXCLUSIVITY-PROVED'
src = open(S + 'mod37v.lean', encoding='utf-8').read(); n = len(C.theorems(C.strip_comments(src))); assert n == 26, n
def blob_of(path):
    b = open(path, 'rb').read(); return hashlib.sha1(b'blob %d\0' % len(b) + b).hexdigest()
probeline = [l for l in open(S + 'probe37.log', encoding='utf-8').read().split('\n') if l.startswith('dita_arc_exclusivity_probe: OK')][0]
npass = len(re.findall(r'(?m)^\s+PASS\s', open(S + 'probe37.log', encoding='utf-8').read()))
DEV = """None. The audit of every identifier consumed by the proofs against the Provenance list finds no landed
declaration outside it: the twenty-six theorems consume Mathlib, this round's own shared lemmas, and
listed declarations of acts 35 and 36 only."""
RUNS = open(S + 'runs37.txt', encoding='utf-8').read().strip()
FCOMMENT = open(S + 'fcomment37.txt', encoding='utf-8').read().strip()
DISC = """- **The symmetry lemma's form.** The route names a rewrite with the Fourier symmetry; the first proof pass
  stated it for the `Matrix.of` form and the rewrite found no occurrence, since `simp only [Matrix.of_apply]`
  leaves the entries in the vector-literal form; the second pass states it in that form. The frozen
  statement `SYM` is unchanged.
- **The base control's identity.** The route names an entrywise identity; a 256-case split timed out at
  `whnf` on the first pass, and the second pass proves it from two sixteen-case table lemmas and `mul_one`.
  The frozen statement `BASE` is unchanged.
- **The first proof pass.** Run 36377702851 on the disposable branch went red with three errors, the two
  above and the kernel unknown constant they caused in the frozen control; all eight exclusion cores, the
  persistence core and the corollary were proved on that pass. The second pass is green.

None otherwise against the freeze."""
CL = '> **' + C.MENTION + ' — the result note.**\n' + '\n'.join('> ' + l for l in C.CLAUSE.split('\n'))
t = open(S + 'result37.draft.md', encoding='utf-8').read()
rep = {'@@SENTENCE@@': C.SENTENCES[L], '@@NTHM@@': 'twenty-six', '@@DEVIATIONS@@': DEV, '@@PROBELINE@@': probeline, '@@RUNS@@': RUNS,
       '@@DISCREPANCIES@@': DISC, '@@CLAUSE@@': CL, '@@PR@@': '764', '@@F@@': '8104323300a5d159cd16317d2fed3c43d44b4970',
       '@@PREREG_BLOB@@': blob_of(S + 'rec/preregistration.md'), '@@F_RUN@@': '36379070237', '@@F_COMMENT@@': FCOMMENT,
       '@@PROBE_BLOB@@': C.PROBE_BLOB, '@@NPASS@@': str(npass), '@@ROAD_BLOB@@': '24056ab42b1bc4d265342b805b97bb92d429cc18',
       '@@CONTROLS_BLOB@@': blob_of(S + 'rec/controls.py'), '@@NMUTS@@': '59'}
for k, v in rep.items():
    assert t.count(k) >= 1, k; t = t.replace(k, v)
assert '@@' not in t, re.findall(r'@@[A-Z0-9_]+@@', t)
open(S + 'rec/result.md', 'w', encoding='utf-8').write(t)
print('note_ok:', C.note_ok(t, L)); print('bytes', len(t.encode()))
