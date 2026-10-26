"""Layer-2 design evidence for the cost model's overhead factor (LAYER2-R3-REVIEW R5). The
estimate's closures term is overhead x (four bare closures per representative); overhead = 2 is a
judgement. This measures, locally and bounded, the ratio

    overhead = time of l2enum.Shard.rep on an orbit / time of the representative's four bare closures

with the representative-sampled gates off and C7's own closures stubbed out (they are the C7
term), so that the ratio covers what the factor is meant to cover: carrying the closures to every
member, each member's attributes and counts, C9 and C10 (i), the class keys and C7's
closure-free scope predicates. Two populations, toy geometry only:
- every orbit of the toy class (contexts of at most 8 quantities);
- planted records of the toy setup: 3 to 6 items at sites of ball(3), slices -1..6, drawn with a
  fixed seed (contexts up to the mid-20s; not records of the toy index space, not v8).
Timing data, not deterministic. Usage: python3 -I -B overhead_measure.py <layer2/code> <out.json>
[--planted 120]. Prints a summary JSON."""
import json
import random
import statistics
import sys
import time

code, outp = sys.argv[1], sys.argv[2]
NP = int(sys.argv[sys.argv.index('--planted') + 1]) if '--planted' in sys.argv else 120
sys.path.insert(0, code)
import s0geom as G        # noqa: E402
import l2config as CFG    # noqa: E402
import l2analysis as AN   # noqa: E402
import l2enum as ENUM     # noqa: E402

setup = CFG.make_setup(G, 'toy')
if setup.key() == (3, 6, (0, 0, -3)):
    raise SystemExit('refusing: v8 configuration class')
grp = AN.group(setup)
off = 10**12
prof = dict(CFG.profile('toy'), sampling={'C8_orbits': off, 'C11i': off, 'C17': off, 'C18': off})
base = {c: set(G.Context(setup, (), c).run()) for c in ('A', 'G')}
ENUM.Shard.c7_record = lambda self, idx, m, conv, carried, dcache: True   # the C7 term's closures, excluded
L3 = G.Rule(far=False)


def measure(orbits):
    """[(context size of the representative, bare ns, rep ns)] per orbit; the bound is each
    record's own L3 closure union, so C9 holds and no witness path runs."""
    out = []
    for idx, (r, orb) in enumerate(orbits):
        bound = {}
        for c in ('A', 'G'):
            q = set()
            for m in orb:
                q |= G.Context(setup, m, c).quants
            bound[(c, 'L3prime')] = bound[(c, 'L3')] = q
        sh = ENUM.Shard(setup, prof, bound, base, None, None)
        t0 = time.perf_counter_ns()
        for c in ('A', 'G'):
            for rule in (G.FROZEN, L3):
                G.Context(setup, r, c, rule).run()
        t1 = time.perf_counter_ns()
        sh.rep(idx, r, orb)
        t2 = time.perf_counter_ns()
        out.append((len(G.Context(setup, r, 'A').quants), t1 - t0, t2 - t1))
    return out


def summary(rows):
    ratios = [b/a for _, a, b in rows]
    tot = sum(b for _, _, b in rows)/sum(a for _, a, _ in rows)
    q = sorted(ratios)
    return {'orbits': len(rows), 'max_context_quantities': max(m for m, _, _ in rows),
            'ratio_of_totals': round(tot, 3), 'median': round(statistics.median(ratios), 3),
            'p90': round(q[int(0.9*(len(q) - 1))], 3), 'max': round(max(ratios), 3)}


toy = []
for i in range(G.num_records(setup)):
    r = tuple(sorted(G.record_at(setup, i)))
    if AN.canon(r, grp) == r:
        toy.append((r, AN.orbit(r, grp)))
rng = random.Random(20261026)
sites = G.lball(3, 3)
planted = []
while len(planted) < NP:
    k = rng.randint(3, 6)
    xs = rng.sample(sites, k)
    r = tuple(sorted((x, rng.randint(-1, 6)) for x in xs))
    planted.append((r, AN.orbit(r, grp)))
t0 = time.time()
res = {'toy_class': summary(measure(toy)), 'planted': summary(measure(planted))}
out = {'schema': 'np-avg-1/stage0/layer2/overhead/1', 'deterministic': False, 'python': sys.version.split()[0],
       'configured_overhead_factor': CFG.CONFIG['budget']['gate_overhead_factor'],
       'definition': 'Shard.rep time (gates off, C7 closures excluded) / four bare closures of the representative',
       'measured': res, 'seconds': round(time.time() - t0),
       'note': 'toy geometry only; contexts below v8 sizes (v8 mean 16, max 29); says nothing certain about v8'}
with open(outp, 'w') as f:
    json.dump(out, f, indent=1, sort_keys=True)
    f.write('\n')
print(json.dumps(out, indent=1, sort_keys=True))
