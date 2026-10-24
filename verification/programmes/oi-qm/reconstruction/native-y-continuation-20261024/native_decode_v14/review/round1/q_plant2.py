"""rev910b: reproduce author's planted restricted brute force (1,u,a), field coeffs (5,3,6,1,7,2)."""
import sys, json
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from native_table import q10_table
from review_checks import kernel, brute, solve, readout_sets, distinct_sets, CTX, idx, law_value
tab = [int(c, 16) for c in q10_table()[0]]
chosen = ('1', 'u', 'a'); fc = (5, 3, 6, 1, 7, 2)
cols = {n: sum(((fc[f] >> i) & 1) << (5 - f) for f in range(6)) for i, n in enumerate(chosen)}
t = list(tab)
for k in CTX:
    v = law_value(cols, k)
    for s in (0, 1):
        t[idx(s ^ k[0] ^ k[3], k, v >> 3, v & 7)] = 5 if s else 2
K = kernel(t)
bc, bd = brute(K, (0, 1, 4))
mine = [solve(readout_sets(K, D), set(chosen))[0] for D in range(1, 255)]
assert mine == bc and solve(distinct_sets(K), set(chosen))[0] == bd
print(json.dumps({'total': sum(bc), 'readouts': sum(1 for x in bc if x), 'diagnostic': bd}))
