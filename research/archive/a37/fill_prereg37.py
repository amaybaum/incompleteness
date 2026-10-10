"""Fill preregistration.draft.md -> rec/preregistration.md.
usage: python3 fill_prereg37.py"""
import hashlib, importlib.util, os, re, subprocess, sys
S = os.path.dirname(os.path.abspath(__file__)) + '/'
def blob_of(path):
    b = open(path, 'rb').read()
    return hashlib.sha1(b'blob %d\0' % len(b) + b).hexdigest()
PROBE_BLOB = blob_of(S + 'dita_arc_exclusivity_probe.py')
spec = importlib.util.spec_from_file_location('c37', S + 'rec/controls.py'); C = importlib.util.module_from_spec(spec); spec.loader.exec_module(C)
assert C.PROBE_BLOB == PROBE_BLOB, (C.PROBE_BLOB, PROBE_BLOB)
CONTROLS_BLOB = blob_of(S + 'rec/controls.py')
log = open(S + 'probe37.log', encoding='utf-8').read()
npass = len(re.findall(r'(?m)^\s+PASS\s', log)); nfail = len(re.findall(r'(?m)^\s+FAIL\s', log))
assert nfail == 0 and 'dita_arc_exclusivity_probe: OK' in log, (npass, nfail)
secs = int(re.findall(r'\((\d+)s\)', log)[-1]); mins = (secs + 30) // 60
road = {lab: blob_of(S + 'roadmap-%s.md' % lab) for lab in ('A37-EXCLUSIVITY-PROVED', 'A37-EXCLUSIVITY-FAILS')}
bad, rows, dmuts, muts = C.self_test()
assert [b for b in bad if not b.startswith('agreement')] == [], bad
assert dmuts == 8, dmuts
RUNS = '''| run | head | what the head carries | outcome |
| --- | --- | --- | --- |
| 36377310857 | `10781e7560210e9625076d9cc47d8f2c295317b0` | **the thirteen frozen propositions and the corollary of this file** as fourteen `#check` commands under the frozen header, wired directly after `DitaHierarchy`, with a disposable census family | all seven jobs green: all fourteen `#check`s elaborate and no error is reported; the release gate passes with twelve receipts holding; the kernel check is green; the probe shards run `D`'s lists and are green |
| 36377702851 | `52ef3fb2dc4be0bc5fcaf3207b103e3096c676f7` | the first proof pass: the module with the verdict, every core proved as in the route, the symmetry core by a rewrite with the Fourier symmetry stated in the unreduced form and the base control by a 256-case split | the `Mathlib bridge` build is red with three errors, none in a frozen statement: the rewrite of the symmetry core finds no occurrence of its pattern, since `simp only [Matrix.of_apply]` leaves the Fourier entries in the vector-literal form; the base control times out at `whnf`; and the frozen control depending on it is a kernel unknown constant. **All eight exclusion cores, the persistence core and the corollary are proved on this first pass**, each printing its axioms; every other job is green |
| 36378121576 | `d79ac73c85ab51b06cd6541f3770a684e6d50ee8` | the second proof pass: the Fourier symmetry lemma stated in the vector-literal form, the base control's Kronecker identity by two sixteen-case table lemmas and `mul_one` | all seven jobs green: the twenty-six theorems compile under their statements with no error, and every named result prints its axioms within `propext`, `Classical.choice` and `Quot.sound` — the axiom audit finds no `sorryAx` in any of the twenty-six; the release gate's `lean-axioms` step reports 4829 named results and no sorry; the kernel check is green |
| 36378520807 | `133c9d17d6de18076873e2b0aa8bc58e140858cf` | **the countercontrol**: the previous head with one deliberate defect, the first witness position of the exclusion core of class `k1` moved from row `(1, 0)` to row `(1, 1)` | red, as required. The `Mathlib bridge` build fails with exactly two errors, both inside that core — `ring failed` at the forced identity, which no longer holds at the moved position, and the unsolved goal it leaves — and nothing else in the build fails; the kernel check is green; the probe shards run `D`'s lists and are green |
| 36378528259 | `2b1bfb971c4ecbcbdcd0d72519259099aa76deb8` | the second proof pass with the **frozen probe** (blob as frozen below) wired into the `Numerical probes / A36 hierarchy` shard by the two frozen lines | all seven jobs green; the probe reports ''' + str(npass) + ''' `PASS` and no `FAIL` and ends with its `OK` line, in 105 seconds after act 36's probe in the same shard — the design run of the probe as frozen |'''
t = open(S + 'preregistration.draft.md', encoding='utf-8').read()
rep = {'@@RUNS@@': RUNS, '@@PROBE_BLOB@@': PROBE_BLOB, '@@CONTROLS_BLOB@@': CONTROLS_BLOB, '@@NMUTS@@': str(muts),
       '@@NPASS@@': str(npass), '@@PROBE_MIN@@': '2 to %d' % max(mins, 3), '@@ROAD_PV@@': road['A37-EXCLUSIVITY-PROVED'], '@@ROAD_FL@@': road['A37-EXCLUSIVITY-FAILS']}
for k, v in rep.items():
    assert t.count(k) >= 1, k; t = t.replace(k, v)
assert '@@' not in t, re.findall(r'@@[A-Z0-9_]+@@', t)
open(S + 'rec/preregistration.md', 'w', encoding='utf-8').write(t)
print('preregistration.md written; probe', PROBE_BLOB, 'controls', CONTROLS_BLOB, 'muts', muts, 'npass', npass, 'mins', mins)
