"""Fill result.draft.md -> rec/result.md from stage2.lean, texts34.json and runs.
usage: python3 fill_result34.py"""
import re, json, importlib.util, os
S = os.path.dirname(os.path.abspath(__file__)) + '/'
spec = importlib.util.spec_from_file_location('c34', S + 'controls.py'); C = importlib.util.module_from_spec(spec); spec.loader.exec_module(C)
T = json.load(open(S + 'texts34.json'))
src = open(S + 'stage2.lean', encoding='utf-8').read()
code = C.strip_comments(src)
th = C.theorems(code)
n = len(th)
NUM = {80: 'eighty', 81: 'eighty-one', 82: 'eighty-two', 83: 'eighty-three'}
nk = len(re.findall(r'(?m)^theorem (\S+) :(?:(?!^theorem ).)*?decide \+kernel', code, re.S))
DEV = """The following landed theorems, absent from the Provenance list, are consumed by shared lemmas — every one against the first row of the matrix, and none by a verdict theorem, a control or `a34_c_exclusive` directly:

| helper | landed in | consumed by |
| --- | --- | --- |
| `fibreGram_apply` | `TwoSidedGauge.lean` | `a34_shared_entry_norm`, `a34_shared_proper_core`, `a34_shared_product_core` |
| `iso2_classes_single` | `OrbitGeometryIsometries.lean` | `a34_shared_tup_real`, `a34_shared_product_core` |

Each is a landed, kernel-checked theorem of the modules the frozen import closes over; none is
re-proved or paraphrased. They are recorded here as the freeze requires and change no statement."""
RUNS = open(S + 'devruns34.txt', encoding='utf-8').read().strip()
DISC = """- The two helpers recorded above under the route-authorization matrix: `fibreGram_apply`, act 12's
  unfolding of a fibre-Gram entry, and act 25's `iso2_classes_single`, both landed and both inside
  the frozen import closure, consumed by shared lemmas only.
- `a34_control_proper` is proved through act 12's `sh1_necessity` from an admissible dilation whose
  anchored block is the witness matrix, rather than by verifying the four realizability conditions
  one by one as the route's step 6 sketched; the route names `sh1_necessity` among its ingredients
  and the statement is unchanged.
- `a34_shared_vertex_core`, the shared vertex of two adjacent circles as one point, is proved from
  act 33's twelve incidence equalities `a33_shared_inc_…` composed pairwise, since
  `a33_shared_vertex` states the implication from a coincidence to the vertex condition and not its
  converse. The Provenance list names the whole of act 33's module, so this is a choice within the
  authorized set and not a deviation.

None otherwise against the freeze."""
CL = '\n'.join('> ' + l for l in T['CLAUSE'].split('\n'))
t = open(S + 'result.draft.md', encoding='utf-8').read()
rep = {'@@NTHM@@': NUM[n], '@@NKERNEL@@': str(nk), '@@DEVIATIONS@@': DEV, '@@RUNS@@': RUNS, '@@DISCREPANCIES@@': DISC,
       '@@CLAUSE@@': CL, '@@SENTENCE@@': T['SENTENCES']['A34-STRATIFIED']}
for k, v in rep.items():
    assert t.count(k) == 1, k
    t = t.replace(k, v)
assert '@@' not in t
open(S + 'rec/result.md', 'w', encoding='utf-8').write(t)
print('theorems', n, 'kernel-decided', nk)
print('note findings', C.note_ok(t, 'A34-STRATIFIED'))
