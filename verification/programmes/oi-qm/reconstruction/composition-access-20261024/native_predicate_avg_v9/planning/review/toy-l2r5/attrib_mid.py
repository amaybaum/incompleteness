"""Reviewer probe (design profile 'mid' only): attribute one interleaved shard's time (S=128, k given)
to C7's per-record work (Shard.c7_record, wrapped), and the rest; and count C7 records by set.
Usage: python3 -I -B attrib_mid.py <layer2/code> K"""
import json, sys, time
code, K = sys.argv[1], int(sys.argv[2])
sys.path.insert(0, code)
import s0geom as G, l2config as CFG, l2analysis as AN, l2enum as ENUM, l2plan as PLAN, l2s1a as S1A
prof = dict(CFG.profile('mid'), shards=128)
setup = CFG.make_setup(G, 'mid')
assert setup.key() != (3, 6, (0, 0, -3))
sp = PLAN.Space(prof)
ri = PLAN.RepIndex(PLAN.site_pair_counts(sp))
s1a = S1A.run('mid', None, None)
bound = ENUM.load_bound(s1a, setup, None)
base = {c: set(G.Context(setup, (), c).run()) for c in ('A', 'G')}
grp = AN.group(setup)
acc = {'c7_seconds': 0.0, 'c7_calls': 0}
orig = ENUM.Shard.c7_record
def wrapped(self, *a, **k):
    t = time.perf_counter()
    try:
        return orig(self, *a, **k)
    finally:
        acc['c7_seconds'] += time.perf_counter() - t
        acc['c7_calls'] += 1
ENUM.Shard.c7_record = wrapped
sh = ENUM.Shard(setup, prof, bound, base, None, None)
t = time.perf_counter()
n = 0
for q in range(K, ri.R, 128):
    i = ri.index_of_rank(q)
    r = tuple(sorted(G.record_at(setup, i)))
    sh.rep(i, r, AN.orbit(r, grp))
    n += 1
tot = time.perf_counter() - t
o = sh.output()
print(json.dumps({'shard': K, 'reps': n, 'total_s': round(tot, 1), 'c7_record_s': round(acc['c7_seconds'], 1),
                  'c7_record_calls': acc['c7_calls'], 'c7_share': round(acc['c7_seconds']/tot, 3),
                  'C7_scope_coverage': o.get('C7_scope_coverage')}, default=str)[:1500])
