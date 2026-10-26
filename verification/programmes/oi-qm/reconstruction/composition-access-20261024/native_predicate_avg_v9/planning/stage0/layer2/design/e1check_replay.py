"""Layer-2 design evidence: erratum E1's consistency check (stage0/amendments/E1-check/e1_check.py,
in effect, not edited) replayed against Layer 2 r3's code and regenerated toy run. E1-check
imports Layer 2's engine, analysis and merge on the toy profile and reads the toy run's
result.json, s1a.json and shard files; its retained output e1_check.out is pinned by SHA-256 in
the erratum. The replay must exit 0 and print output byte-identical to e1_check.out, which shows
that r3 keeps every value E1-check verified (the r5 count list read by part B, the toy counts of
part C, the shared-tip tally of part F, the toy S1a values of parts G and K, and the label and
rule T behaviour of part K). Usage: python3 -I -B e1check_replay.py <stage0/amendments/E1-check>.
Prints JSON; exit 0 iff so. Writes nothing."""
import hashlib
import json
import os
import subprocess
import sys

d = sys.argv[1]
p = subprocess.run([sys.executable, '-I', '-B', os.path.join(d, 'e1_check.py')], capture_output=True, text=True)
with open(os.path.join(d, 'e1_check.out'), encoding='utf-8') as f:
    ret = f.read()
same = p.stdout == ret
try:
    failed = json.loads(p.stdout).get('failed')
except ValueError:
    failed = 'unparseable'
out = {'exit': p.returncode, 'failed': failed, 'output_identical_to_retained_e1_check_out': same,
       'replay_sha256': hashlib.sha256(p.stdout.encode()).hexdigest(),
       'retained_sha256': hashlib.sha256(ret.encode()).hexdigest(), 'pass': p.returncode == 0 and same}
print(json.dumps(out, indent=1, sort_keys=True))
sys.exit(0 if out['pass'] else 2)
