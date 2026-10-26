"""Reviewer probe (design profile 'mid' only; refuses v8's key): does an interleaved assignment of
representatives by rank (shard k holds ranks q with q mod S == k) balance real shard time where the
contiguous representative-balanced subdivision does not (r5: 7.9 / 8.5 / 18.5 / 131.6 s)?
Runs: contiguous shards of the r5 subdivision at S=128 chosen as in midsize_validation (0, model-heaviest)
as a same-machine baseline, and interleaved shards k = 0, 37, 74, 111 at S=128. Normal mode, every gate
at the mid profile's rates. Each interleaved shard checks canon(r) == r for every rank it is given.
Usage: python3 -I -B interleave_mid.py <layer2/code> <calib.json> <out.json>"""
import json, sys, time
code, calibp, outp = sys.argv[1:4]
sys.path.insert(0, code)
import s0geom as G, l2config as CFG, l2analysis as AN, l2enum as ENUM, l2plan as PLAN, l2s1a as S1A
PNAME, S = 'mid', 128
prof = dict(CFG.profile(PNAME), shards=S)
setup = CFG.make_setup(G, PNAME)
assert setup.key() != (3, 6, (0, 0, -3))
sp = PLAN.Space(prof)
assert sp.key != PLAN.V8_KEY_LITERAL
plan, reps, _, info = PLAN.dry_shard_plan(sp, S)
ri = PLAN.RepIndex(PLAN.site_pair_counts(sp))
with open(calibp) as f:
    calib = json.load(f)
tA = {int(k): v for k, v in calib['closure_ns_A'].items()}
tG = {int(k): v for k, v in calib['closure_ns_G'].items()}
weights = PLAN.shard_context_weights(sp, ri, plan, lambda m: PLAN._t(tA, m) + PLAN._t(tG, m))
order = sorted(range(S), key=lambda k: weights[k])
s1a = S1A.run(PNAME, None, None)
bound = ENUM.load_bound(s1a, setup, None)
base = {c: set(G.Context(setup, (), c).run()) for c in ('A', 'G')}
grp = AN.group(setup)
out = {'R': ri.R, 'S': S, 'contiguous': [], 'interleaved': []}
for k in (0, order[-1]):
    sh = ENUM.Shard(setup, prof, bound, base, None, None)
    t = time.time()
    _, rr = ENUM.scan(setup, plan[k]['lo'], plan[k]['hi'], sh.grp, None)
    for i, r, o in rr:
        sh.rep(i, r, o)
    out['contiguous'].append({'shard': k, 'reps': len(rr), 'seconds': round(time.time() - t, 1)})
    print(out['contiguous'][-1], flush=True)
for k in (0, 37, 74, 111):
    sh = ENUM.Shard(setup, prof, bound, base, None, None)
    t = time.time()
    n = bad = 0
    for q in range(k, ri.R, S):
        i = ri.index_of_rank(q)
        r = tuple(sorted(G.record_at(setup, i)))
        if AN.canon(r, grp) != r:
            bad += 1
            continue
        sh.rep(i, r, AN.orbit(r, grp))
        n += 1
    out['interleaved'].append({'shard': k, 'reps': n, 'not_canonical': bad, 'seconds': round(time.time() - t, 1)})
    print(out['interleaved'][-1], flush=True)
with open(outp, 'w') as f:
    json.dump(out, f, indent=1)
