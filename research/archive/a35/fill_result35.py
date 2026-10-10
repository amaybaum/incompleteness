"""Fill result.draft.md -> rec/result.md for A35-DITA-STRATIFIED."""
import importlib.util, os, re
S = os.path.dirname(os.path.abspath(__file__)) + '/'
spec = importlib.util.spec_from_file_location('c35', S + 'controls.py'); C = importlib.util.module_from_spec(spec); spec.loader.exec_module(C)
L = 'A35-DITA-STRATIFIED'
src = open(S + 'stage2.lean', encoding='utf-8').read(); n = len(C.theorems(C.strip_comments(src))); assert n == 56
probeline = [l for l in open(S + 'probe-amended2.log', encoding='utf-8').read().split('\n') if l.startswith('dita_defect_probe: OK')][0]
DEV = """None. The audit of every identifier consumed by the proofs against the Provenance list finds no landed
declaration outside it: the fifty-six theorems consume Mathlib, this round's own shared lemmas, and
listed declarations of acts 12, 21, 23, 25, 26, 33 and 34 only."""
RUNS = open(S + 'runs35.txt', encoding='utf-8').read().strip()
DISC = """- **Amendment 1.** The freeze in force is `F = a58d39ae…`, the preregistration with its amendment 1,
  designated by comment 5855240090 after the parent `62479b57…`, designated by comment 5854712207,
  was held on the owner's review. The amendment corrects the preregistration in four places: the
  probe's run sites; the probe's tangent check, which compared a rank with itself, and its
  stabilizer enumeration, whose rounded-bytes comparison distinguished `0.0` from `−0.0` and
  undercounted the stabilizers as 512 and 16 where the exact values are 8192 and 128; the wording
  of the open modulus and of the `P0` sentence; and the record files and blobs. The execution
  departs from the preregistration exactly where the amendment does, and nowhere else.
- **The probe's line count.** The preregistration's runs table says the probe of its blob reports
  57 `PASS`; it prints 39, and the corrected probe prints 43, as the amendment records.
- **The witness core.** The freeze's route proves act 34's witness statement in one core lemma;
  the execution proves its six conjuncts as separate shared lemmas (`a35_shared_wit_mem`,
  `a35_shared_wit_notin`, `a35_shared_wit_val`, `a35_shared_wit_rel`, `a35_shared_wit_feat`,
  with `a35_shared_wit_eq`) assembled by `a35_shared_wit_core`, after the one-lemma form timed out
  in elaboration. Every lemma is in the shared row of the matrix; the statement is unchanged.
- **The conjugation's unitarity.** `a35_shared_conj_unitary` is proved entrywise from
  `Matrix.mem_unitaryGroup_iff`, since the Mathlib the bridge builds against has no
  `unitary.star_mem` under that name; the route's transpose-of-the-star reading is not used.

None otherwise against the freeze."""
CL = '> **' + C.MENTION + ' — the result note.**\n' + '\n'.join('> ' + l for l in C.CLAUSE.split('\n'))
t = open(S + 'result.draft.md', encoding='utf-8').read()
rep = {'@@FCOMMENT@@': '5855240090', '@@SENTENCE@@': C.SENTENCES[L], '@@NTHM@@': 'fifty-six', '@@DEVIATIONS@@': DEV,
       '@@PROBELINE@@': probeline, '@@RUNS@@': RUNS, '@@DISCREPANCIES@@': DISC, '@@CLAUSE@@': CL}
for k, v in rep.items():
    assert t.count(k) >= 1, k; t = t.replace(k, v)
assert '@@' not in t, re.findall(r'@@[A-Z0-9]+@@', t)
open(S + 'rec/result.md', 'w', encoding='utf-8').write(t)
print('note_ok:', C.note_ok(t, L)); print('bytes', len(t.encode()))
