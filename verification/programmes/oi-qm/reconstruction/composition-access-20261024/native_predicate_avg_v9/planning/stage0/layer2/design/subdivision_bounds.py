"""Layer-2 design evidence (r5; owner 2026-10-26: deterministic subdivision of heavy site pairs; the
count-only module's resource limit). Deterministic; no closure.

For the toy profile and three analogues ball(1), ball(2), ball(3) (dim 3, slices -1..23, port
(0, 0, -2), C4v about the last axis, as in LAYER2-R4-REVIEW's concentration probe; none is v8's
region, and ball(4) is not run, since its site-pair counts would be v8's), at 32 shards (and at the
toy profile's 4 for the toy):
- the representatives per shard under the index-even plan and under the deterministic subdivision
  (l2plan.subdivision_cuts), as heaviest/mean;
- the modelled closure cost per shard (shard_context_weights with the planted calibration's
  t_A(m) + t_G(m)) under both plans, as heaviest/mean;
- the plan's accounting checks;
- the representative flags of l2plan.RepIndex against the engine's canonical-image test
  (l2analysis.canon over s0geom.record_at): every index for the toy, ball(1) and ball(2), and every
  401st for ball(3); and, for every profile, every single site and every site pair at the slice pairs
  (0, 0), (0, 1), (1, 0) and (2, 1), which separate the four in-pair cases (all, none, t1 <= t2,
  t1 < t2);
- the count-only module's cost: l2sitepairs run as its own process (python3 -I -B, the module's own
  resource limits) on each profile, wall time and peak resident memory.
The printed summary is deterministic given the calibration; the timings (the flag check's and the count
module's) are in the output file only.
Usage: python3 -I -B subdivision_bounds.py <layer2/code> <calib.json> <out.json>"""
import json
import os
import subprocess
import sys
import tempfile
import time

code, calibp, outp = sys.argv[1], sys.argv[2], sys.argv[3]
sys.path.insert(0, code)
import s0geom as G        # noqa: E402
import l2config as CFG    # noqa: E402
import l2analysis as AN   # noqa: E402
import l2plan as PLAN     # noqa: E402

with open(calibp) as f:
    calib = json.load(f)
tA = {int(k): v for k, v in calib['closure_ns_A'].items()}
tG = {int(k): v for k, v in calib['closure_ns_G'].items()}


def wfun(m):
    return PLAN._t(tA, m) + PLAN._t(tG, m)


def analogue(rho):
    return {'setup': {'dim': 3, 'n': 5, 'rho': rho, 'tlast': 23, 'port': [0, 0, -2], 'sources': []}, 'k': 2}


PROFILES = [('toy', CFG.profile('toy'), 1), ('ball1', analogue(1), 1), ('ball2', analogue(2), 1),
            ('ball3', analogue(3), 401)]


def ratio(v):
    return round(max(v)*len(v)/sum(v), 3) if sum(v) else None


def count_process(pr):
    """l2sitepairs.count in its own process under the module's resource limits: (seconds, peak RSS kB)."""
    s = pr['setup']
    prog = ('import sys, time, resource\nsys.path.insert(0, %r)\nimport l2sitepairs as C\n'
            'resource.setrlimit(resource.RLIMIT_CPU, (C.RESOURCE_LIMIT["cpu_seconds"],) * 2)\n'
            'resource.setrlimit(resource.RLIMIT_AS, (C.RESOURCE_LIMIT["address_space_bytes"],) * 2)\n'
            't = time.time(); c = C.count({"dim": %d, "rho": %d, "tlast": %d, "port": %r})\n'
            'print(round(time.time() - t, 3), resource.getrusage(resource.RUSAGE_SELF).ru_maxrss, c["representatives_total"])'
            % (os.path.abspath(code), s['dim'], s['rho'], s['tlast'], tuple(s['port'])))
    with tempfile.TemporaryDirectory() as d:
        p = subprocess.run([sys.executable, '-I', '-B', '-c', prog], capture_output=True, text=True, cwd=d, timeout=300)
    sec, rss, R = p.stdout.split()
    return float(sec), int(rss), int(R)


out = {'shards': 32, 'profiles': {}}
for name, pr, stride in PROFILES:
    sp = PLAN.Space(pr)
    if sp.key == PLAN.V8_KEY_LITERAL:
        raise SystemExit('refusing: v8 configuration class')
    ri = PLAN.RepIndex(PLAN.site_pair_counts(sp))
    row = {'sites': len(sp.region), 'records': ri.N, 'representatives': ri.R}
    for S in sorted({32, pr.get('shards', 32)}):
        sub = PLAN.plan_from_cuts(ri, PLAN.subdivision_cuts(ri, S))
        even = PLAN.shard_plan(ri.N, S)
        for sh in even:
            sh['representatives'] = ri.before(sh['hi']) - ri.before(sh['lo'])
        row['S=%d' % S] = {
            'reps_heaviest_over_mean': {'index_even': ratio([sh['representatives'] for sh in even]),
                                        'subdivision': ratio([sh['representatives'] for sh in sub])},
            'reps_per_shard_range_subdivision': [min(sh['representatives'] for sh in sub),
                                                 max(sh['representatives'] for sh in sub)],
            'empty_shards_index_even': sum(1 for sh in even if sh['representatives'] == 0),
            'model_cost_heaviest_over_mean': {
                'index_even': ratio(PLAN.shard_context_weights(sp, ri, even, wfun)),
                'subdivision': ratio(PLAN.shard_context_weights(sp, ri, sub, wfun))},
            'accounting': PLAN.plan_accounting(ri, sub)}
    setup = G.Setup(pr['setup']['dim'], pr['setup']['n'], pr['setup']['rho'], pr['setup']['tlast'],
                    tuple(pr['setup']['port']), tuple(tuple(x) for x in pr['setup']['sources']))
    grp = AN.group(setup)
    t = time.time()
    bad = n = 0
    for i in range(0, ri.N, stride):
        r = tuple(sorted(G.record_at(setup, i)))
        bad += (AN.canon(r, grp) == r) != ri.is_rep(i)
        n += 1
    nt, ns = len(sp.slices), len(sp.region)
    blk = list(range(0, ns*nt, nt))
    blk += [ns*nt + p*nt*nt + a*nt + b for p in range(ns*(ns - 1)//2) for a, b in ((0, 0), (0, 1), (1, 0), (2, 1))]
    bad_b = 0
    for i in blk:
        r = tuple(sorted(G.record_at(setup, i)))
        bad_b += (AN.canon(r, grp) == r) != ri.is_rep(i)
    row['flags_vs_engine_canon'] = {'indices_checked': n, 'stride': stride, 'mismatches': bad,
                                    'every_block_indices_checked': len(blk), 'every_block_mismatches': bad_b,
                                    'in_pair_cases': {k: sum(1 for b in ri.blocks[ns:] if b[2] == k)
                                                      for k in ('all', 'none', 'upper', 'strict')},
                                    'seconds': round(time.time() - t, 1)}
    sec, rss, R = count_process(pr)
    row['count_module'] = {'seconds': sec, 'peak_rss_kB': rss, 'representatives_agree': R == ri.R}
    out['profiles'][name] = row
out['count_module_resource_limit'] = __import__('l2sitepairs').RESOURCE_LIMIT
out['v8_region_size'] = {'sites': 129, 'site_pairs': 129*128//2, 'note': 'not run: the count module refuses v8 without '
                                                                      'its own authorization'}
with open(outp, 'w') as f:
    json.dump(out, f, sort_keys=True, indent=1)
    f.write('\n')
summary = {k: {'reps': v['S=32']['reps_heaviest_over_mean'], 'cost': v['S=32']['model_cost_heaviest_over_mean'],
               'flag_mismatches': v['flags_vs_engine_canon']['mismatches'] +
               v['flags_vs_engine_canon']['every_block_mismatches'],
               'in_pair_cases': v['flags_vs_engine_canon']['in_pair_cases'],
               'count_module_agrees': v['count_module']['representatives_agree']} for k, v in out['profiles'].items()}
print(json.dumps(summary, sort_keys=True))
sys.exit(0 if all(v['flag_mismatches'] == 0 and all(out['profiles'][k]['S=32']['accounting'].values())
                  for k, v in summary.items()) else 2)
