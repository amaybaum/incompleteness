"""Scratch per-call control for the interning sketch (diagnosis only). Executes the landed independent probe's
definitions and named test cases (its source up to the A41-I2 census, nothing else), then for every distinct named
matrix H and its transpose, and for every column subset S of size 2, 4 and 8, compares prop_partition on the landed
ratio table (keys = pairs of Fractions) against prop_partition on the interned table (keys = small ints).
Countercontrol: a deliberately non-injective interning (id mod 7) must differ somewhere, else the comparison is vacuous.

usage: python3 intern_control.py <repo root>
"""
import itertools, os, sys, time
REPO = sys.argv[1]
PROBE = os.path.join(REPO, 'verification', 'lean', 'dita_index_map_independent.py')
src = open(PROBE, encoding='utf-8').read()
cut = src.index("print('== A41-I2.")
NS = {'__name__': 'independent_head', '__file__': PROBE}
import contextlib, io
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(src[:cut], PROBE, 'exec'), NS)
ratio_table, prop_partition, A41_MATS, a41_key = NS['ratio_table'], NS['prop_partition'], NS['A41_MATS'], NS['a41_key']


def ratio_table_interned(H, mod=None):
    ids = {}
    def iid(k):
        v = ids.setdefault(k, len(ids))
        return v if mod is None else v % mod
    return [[[iid((H[i][s] * H[i][s0].conj()).key()) for s in range(16)] for s0 in range(16)] for i in range(16)]


SUBSETS = [S for n in (2, 4, 8) for S in itertools.combinations(range(16), n)]
seen = set(); mats = []
for role, H in A41_MATS:
    k = a41_key(H)
    if k in seen: continue
    seen.add(k); mats.append((role, H))
t0 = time.time(); calls = diff_new = diff_bad = 0; told = tnew = 0.0
for role, H in mats:
    for form, M in (('column', H), ('row', [list(c) for c in zip(*H)])):
        RT0 = ratio_table(M); RT1 = ratio_table_interned(M); RT2 = ratio_table_interned(M, mod=7)
        for S in SUBSETS:
            t = time.perf_counter(); a = prop_partition(RT0, S); told += time.perf_counter() - t
            t = time.perf_counter(); b = prop_partition(RT1, S); tnew += time.perf_counter() - t
            c = prop_partition(RT2, S)
            calls += 1; diff_new += a != b; diff_bad += a != c
print('distinct matrices %d, forms 2, subsets %d: %d prop_partition calls' % (len(mats), len(SUBSETS), calls))
print('interned vs landed: %d differing outputs (want 0); time landed %.1fs, interned %.1fs' % (diff_new, told, tnew))
print('countercontrol (id mod 7) vs landed: %d differing outputs (want > 0)' % diff_bad)
print('VERDICT', 'EQUIVALENT' if diff_new == 0 and diff_bad > 0 else ('VACUOUS' if diff_bad == 0 else 'DIFFERENT'),
      '(%.0fs)' % (time.time() - t0))
