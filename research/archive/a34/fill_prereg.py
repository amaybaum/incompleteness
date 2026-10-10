"""Fill the preregistration draft's placeholders: the pre-freeze runs table, the controls blob, the mutation count."""
import os, subprocess, sys
S = os.path.dirname(os.path.abspath(__file__))
t = open(os.path.join(S, 'preregistration.draft.md'), encoding='utf-8').read()
runs = open(os.path.join(S, 'runs34.txt'), encoding='utf-8').read().strip()
blob = subprocess.run(['git', 'hash-object', os.path.join(S, 'controls.py')], capture_output=True, text=True).stdout.strip()
nm = sys.argv[1]
for k, v in {'@@RUNS@@': runs, '@@CONTROLS_BLOB@@': blob, '@@NMUTS@@': nm}.items():
    assert t.count(k) >= 1, k
    t = t.replace(k, v)
assert '@@' not in t
open(os.path.join(S, 'rec', 'preregistration.md'), 'w', encoding='utf-8').write(t)
print('written; controls blob', blob)
