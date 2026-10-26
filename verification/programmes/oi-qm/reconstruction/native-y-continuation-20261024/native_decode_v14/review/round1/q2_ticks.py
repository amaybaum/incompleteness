"""rev910b Q2: at which tick does the q10 cell first carry s under the v14 class?"""
import sys, json
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from native_table import q10_table, ROWS, R, L
from review_checks import kernel, readout_sets, solve, FEAT, CTX, idx
tab, _, _ = q10_table()
ticks = q10_table.ticks
assert ticks[10] == tab
out = {}
for tick in (8, 9, 10):
    t = [int(c, 16) for c in ticks[tick]]
    en_dep = sum(1 for i, r in enumerate(ROWS) if t[i] != t[idx(r[0], r[1:6], 0, 0)])
    K = kernel(t)
    tot = sum(solve(readout_sets(K, D), set(FEAT))[0] for D in range(1, 255))
    out['R+%d%s' % (tick, ' (=L)' if tick == 9 else (' (=L+1)' if tick == 10 else ''))] = {
        'rows_depending_on_E_or_N': en_dep, 'fixed_readout_solutions_all_254': tot}
print(json.dumps(out, indent=1))
