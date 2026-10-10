"""Fill preregistration.draft.md -> rec/preregistration.md.
usage: python3 fill_prereg36.py <probe design run id> <probe design head sha>"""
import hashlib, importlib.util, os, re, subprocess, sys
S = os.path.dirname(os.path.abspath(__file__)) + '/'
RUN_P, HEAD_P = sys.argv[1], sys.argv[2]
OLD2_OUTCOME = 'the `Mathlib bridge` build and the kernel check are green; the probes job is red at exactly the same check and for the same reason, the sector fates at the structured combination, `(8, False, False, None)` twice, with every other check passing, 55 `PASS` and 1 `FAIL`: the `u = 1` identity, the second point `Pu u₅` with its defect 37 and its six searches with the frozen `2 × 8` structure all pass'
def blob_of(path):
    b = open(path, 'rb').read()
    return hashlib.sha1(b'blob %d\0' % len(b) + b).hexdigest()
PROBE_BLOB = blob_of(S + 'dita_hierarchy_probe.py')
spec = importlib.util.spec_from_file_location('c36', S + 'rec/controls.py'); C = importlib.util.module_from_spec(spec); spec.loader.exec_module(C)
assert C.PROBE_BLOB == PROBE_BLOB, (C.PROBE_BLOB, PROBE_BLOB)
CONTROLS_BLOB = blob_of(S + 'rec/controls.py')
log = open(S + 'probe36.log', encoding='utf-8').read()
npass = len(re.findall(r'(?m)^\s+PASS\s', log)); nfail = len(re.findall(r'(?m)^\s+FAIL\s', log))
assert nfail == 0 and 'dita_hierarchy_probe: OK' in log, (npass, nfail)
secs = int(re.findall(r'\((\d+)s\)', log)[-1]); mins = (secs + 30) // 60
road = {}
for lab in ('A36-HIERARCHY', 'A36-NOT-HIERARCHY'):
    road[lab] = blob_of(S + 'roadmap-%s.md' % lab)
# the mutation count from the self-test run beside the draft
bad, rows, dmuts, muts = C.self_test()
assert [b for b in bad if not b.startswith('agreement')] == [], bad
RUNS = '''| run | head | what the head carries | outcome |
| --- | --- | --- | --- |
| 36330185755 | `8fb7e1ed82d48c8bbc1de7622095058e4987016a` | **the nine frozen propositions and the corollary of this file** as ten `#check` commands under the frozen header, wired directly after `DitaHull`, with a disposable census family; the flatness predicate `flg` written with an anonymous binder | the `Mathlib bridge` build is red with one error, `Unknown identifier α` at the `flg` lambda, whose implicit type argument is inaccessible to an anonymous binder; the kernel check is green |
| 36330499550 | `ae1e671754c75583ff6c3b00e849bb055ce5d628` | the same head with `flg` written with the explicit binders `{α : Type} [Fintype α] [DecidableEq α] (X : Matrix α α ℂ)`, the text frozen in this file | all three jobs green: all ten `#check`s elaborate and no error is reported; the release gate passes all 21 steps with eleven receipts holding; the kernel check is green; the probes job runs `D`'s list and is green |
| 36331117696 | `0a5c2f52119e6a1ad64dbb22cebcffadc842ac8c` | **the countercontrol**: the previous head with one deliberate defect, an extra argument to `dg` in `P_R`'s `HULLG` conjunct | red, as required. The `Mathlib bridge` build fails with exactly one source error, `OIBridge/DitaHierarchy.lean:69:14: Application type mismatch`, at that argument, and nothing else fails in the build; the kernel check is green; the probes job runs `D`'s list and is green |
| 36331629574 | `3641125e17fb0b439c02d6a60a991158fc70ee9f` | the elaboration head with a first draft of the probe, blob `c95dbde5019b8f5942e22d033054ee8f5e8769db`, wired into the `Numerical probes` job by the one token: sections 1 to 6 as frozen below, without the `u = 1` identity control and the second point of the line, and with the sector certificate tested at one structured integer combination per sector | the `Mathlib bridge` build and the kernel check are green; the probes job is red at exactly one check, the sector fates: the certificate **fails** at the structured combination of each 8-dimensional sector, `(8, False, False, None)` against the expected `(8, False, True, None)`, while every other check of the six sections passes, 44 `PASS` and 1 `FAIL`. The failure is the direction dependence of Hazard 6, not a change in the mathematics: at random directions the certificate holds, at structured ones it fails |
| 36331881958 | `2f9707a16757f110b7244fe4b48cd96593f69b44` | the same with the `u = 1` identity control and the second point `Pu u₅` added, blob `8bae58ccb008249c9e2844167de2a56a06ee2e6b` | ''' + OLD2_OUTCOME + ''' |
| ''' + RUN_P + ''' | `''' + HEAD_P + '''` | the elaboration head with the **frozen probe** (blob as frozen below): the second draft with the sector certificate tested at three seeded pseudo-random directions per sector and its direction dependence asserted at the basis vectors | all three jobs green; the probe reports ''' + str(npass) + ''' `PASS` and no `FAIL` and ends with its `OK` line — the design run of the probe as frozen |'''
t = open(S + 'preregistration.draft.md', encoding='utf-8').read()
rep = {'@@RUNS@@': RUNS, '@@PROBE_BLOB@@': PROBE_BLOB, '@@CONTROLS_BLOB@@': CONTROLS_BLOB, '@@NMUTS@@': str(muts),
       '@@NPASS@@': str(npass), '@@PROBE_MIN@@': '13 to %d' % mins, '@@ROAD_HI@@': road['A36-HIERARCHY'], '@@ROAD_NH@@': road['A36-NOT-HIERARCHY']}
for k, v in rep.items():
    assert t.count(k) >= 1, k; t = t.replace(k, v)
assert '@@' not in t, re.findall(r'@@[A-Z0-9_]+@@', t)
open(S + 'rec/preregistration.md', 'w', encoding='utf-8').write(t)
print('preregistration.md written; probe', PROBE_BLOB, 'controls', CONTROLS_BLOB, 'muts', muts, 'npass', npass, 'mins', mins)
