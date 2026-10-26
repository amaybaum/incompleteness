import json, subprocess, sys, os
from concurrent.futures import ThreadPoolExecutor
code = sys.argv[1]; mode = sys.argv[2]; names = sys.argv[3:]
def run(m):
    cmd = [sys.executable, '-I', '-B', os.path.join(code, 's0controls.py'), '--rule', m] + (['--quick'] if mode == 'quick' else [])
    p = subprocess.run(cmd, capture_output=True, text=True)
    try:
        return m, p.returncode, json.loads(p.stdout)
    except Exception:
        return m, p.returncode, {'_stderr': p.stderr[-2000:]}
with ThreadPoolExecutor(2) as ex:
    res = list(ex.map(run, ['frozen'] + names))
base = res[0][2]
out = {}
for m, rc, r in res:
    if '_stderr' in r:
        out[m] = {'exit': rc, 'stderr': r['_stderr']}; continue
    out[m] = {'exit': rc, 'failed': r['failed'],
              'C11_i_mismatches': r['C11_dir_tables']['mismatches'], 'C11_i_first': r['C11_dir_tables']['first'][:1],
              'C11_ii_pa_dir': r['C11_props']['pa_dir_violations'], 'C11_ii_pa_agg': r['C11_props']['pa_aggregate_violations'],
              'C11_ii_planted_retained': r['C11_props']['planted_retained'],
              'counts_identical_to_frozen': r['C8_symmetry']['counts'] == base['C8_symmetry']['counts'],
              'counts_differing': sorted(k for k in base['C8_symmetry']['counts'] if r['C8_symmetry']['counts'].get(k) != base['C8_symmetry']['counts'][k])[:6]}
print(json.dumps(out, indent=1, default=list))
