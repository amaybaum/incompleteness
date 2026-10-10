"""Fill result36.draft.md -> rec/result.md for A36-HIERARCHY. Reads runs36.txt (the runs table) beside it."""
import importlib.util, os, re
S = os.path.dirname(os.path.abspath(__file__)) + '/'
spec = importlib.util.spec_from_file_location('c36', S + 'rec/controls.py'); C = importlib.util.module_from_spec(spec); spec.loader.exec_module(C)
L = 'A36-HIERARCHY'
src = open(S + 'mod36v.lean', encoding='utf-8').read(); n = len(C.theorems(C.strip_comments(src))); assert n == 37, n
probeline = [l for l in open(S + 'probe36.log', encoding='utf-8').read().split('\n') if l.startswith('dita_hierarchy_probe: OK')][0]
DEV = """None. The audit of every identifier consumed by the proofs against the Provenance list finds no landed
declaration outside it: the thirty-seven theorems consume Mathlib, this round's own shared lemmas, and
listed declarations of acts 12, 23, 24, 25, 34 and 35 only."""
RUNS = open(S + 'runs36.txt', encoding='utf-8').read().strip()
DISC = """- **The line's witnesses.** The freeze's route names the constant twist `D ≡ −i` with the inner factors
  scaled by `(1 + i)/4`; the execution takes `D ≡ 1` with the inner row construction's outer factor
  `((1 − i)/2) · [[1, 1], [1, −1]]` and its inner factors scaled by `1/2`, the same product `1/4` and
  the same family. The witnesses are existentially quantified in the frozen statement, which is
  unchanged.
- **The reindexing lemma.** The route names `Matrix.submatrix_mul_equiv` and `Fintype.sum_equiv`; the
  execution proves the reindexing of a unitary matrix by two bijections directly from
  `Function.Bijective.sum_comp` (`a36_shared_reindex_unitary`), and the instances by explicit
  equivalences built from `finProdFinEquiv`, `Equiv.prodAssoc`, `Equiv.prodComm` and `Equiv.prodCongr`,
  with the bijective-function form as a second alternative inside the same proof. Every lemma is in
  the shared row of the matrix.
- **The first proof pass.** Run 36337348555 on the disposable branch went red with seventeen errors,
  all in the proofs and none in a frozen statement: a binder shadowing in the executor's flatness
  template, the three-way case split of the twist's unit-modulus checks, a `simp` ordering in the
  phase lemma, and the conjugates of numerals in the point's exclusion. The second pass is green.

None otherwise against the freeze."""
CL = '> **' + C.MENTION + ' — the result note.**\n' + '\n'.join('> ' + l for l in C.CLAUSE.split('\n'))
t = open(S + 'result36.draft.md', encoding='utf-8').read()
rep = {'@@SENTENCE@@': C.SENTENCES[L], '@@NTHM@@': 'thirty-seven', '@@DEVIATIONS@@': DEV,
       '@@PROBELINE@@': probeline, '@@RUNS@@': RUNS, '@@DISCREPANCIES@@': DISC, '@@CLAUSE@@': CL}
for k, v in rep.items():
    assert t.count(k) >= 1, k; t = t.replace(k, v)
assert '@@' not in t, re.findall(r'@@[A-Z0-9]+@@', t)
open(S + 'rec/result.md', 'w', encoding='utf-8').write(t)
print('note_ok:', C.note_ok(t, L)); print('bytes', len(t.encode()))
