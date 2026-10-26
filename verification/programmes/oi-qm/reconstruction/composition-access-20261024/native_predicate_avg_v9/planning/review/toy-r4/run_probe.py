import json, subprocess, sys, os
from concurrent.futures import ThreadPoolExecutor
code = sys.argv[1]; names = sys.argv[2:]
def run(m):
    cmd = [sys.executable, '-I', '-B', os.path.join(code, 's0controls.py'), '--rule', m, '--quick']
    p = subprocess.run(cmd, capture_output=True, text=True)
    try:
        return m, p.returncode, json.loads(p.stdout)
    except Exception:
        return m, p.returncode, {'_stderr': p.stderr[-1500:]}
with ThreadPoolExecutor(2) as ex:
    res = list(ex.map(run, ['frozen'] + names))
base = res[0][2]
out = {}
for m, rc, r in res:
    if '_stderr' in r:
        out[m] = {'exit': rc, 'stderr': r['_stderr']}; continue
    out[m] = {'exit': rc, 'failed': r['failed'],
              'C11_i': {k: r['C11_dir_tables'][k] for k in ('table_mismatches', 'decision_inconsistent')},
              'C11_ii': {k: r['C11_props'][k] for k in ('pa_dir_violations', 'pa_aggregate_violations', 'planted_retained')},
              'C11_iii': {k: r['C11_planted'][k] for k in ('failures', 'adjacent_failures', 'first')},
              'counts_identical_to_frozen': r['C8_symmetry']['counts'] == base['C8_symmetry']['counts']}
print(json.dumps(out, indent=1, default=list))
