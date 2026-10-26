"""NP-AVG-1 Stage 0 Layer 2: cost calibration for the dry-run estimate (section 3 of the plan).

Usage: python3 -I -B l2calib.py --out calib.json [--sets 12]
Times the production closure and the C7 reference on planted quantity sets only: m quantities
drawn at random from the even class of a displaced ball, ball(4) centred at (40, 0, 0), over
slices -1..23, with the A pair (7, 8) and the G pair (-1, 0). Under G, eligibility is
'outside the cones of an eleven-quantity planted frame' (the toy's fixed quantities and port
samples, displaced to the same centre), so the cost of the eligibility test is represented, memoized per frame as in s0geom.Context.
These sets are neither records nor v8 contexts, and only timings are recorded: no retained
set is written. The output is timing data and is not deterministic; the dry run reads it.
"""
import json
import os
import random
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import s0geom as G        # noqa: E402
import s0ref as REF       # noqa: E402
import l2refcheck as RC   # noqa: E402

SIZES = (8, 12, 16, 20, 24, 28, 32, 36, 40)


def planted(rng, m, centre):
    pool = [(G.vadd(centre, c), t) for c in G.lball(4, 3) for t in range(-1, 24) if (G.l1(c) + t) % 2 == 0]
    return set(rng.sample(pool, m))


def main():
    args = sys.argv[1:]
    nsets = int(args[args.index('--sets') + 1]) if '--sets' in args else 12
    rng = random.Random(20261026)
    centre = (40, 0, 0)
    pA, pG = G.Pair(7), G.Pair(-1)
    toy_frame = [(G.vadd(centre, e), 3) for e in G.axes(3)] + [(centre, 4), (centre, 2)] + \
        [(G.vadd(centre, (0, 0, -2)), s) for s in (0, 1, 2)]

    memo = {}

    def elig(u):
        v = memo.get(u)
        if v is None:
            v = memo[u] = not any(G.in_cone(u, f, pG) for f in toy_frame)
        return v
    out = {'schema': 'np-avg-1/stage0/layer2/calib/1', 'python': sys.version.split()[0], 'sets_per_size': nsets,
           'closure_ns_A': {}, 'closure_ns_G': {}, 'ref_c7_ns_A': {}, 'ref_c7_ns_G': {}, 'deterministic': False}
    for m in SIZES:
        sets = [planted(rng, m, centre) for _ in range(nsets)]
        for conv, pair, el in (('A', pA, None), ('G', pG, elig)):
            t0 = time.perf_counter_ns()
            for S in sets:
                G.closure(set(), S, pair, 3, G.FROZEN, el)
            out['closure_ns_%s' % conv][str(m)] = (time.perf_counter_ns() - t0)//nsets
            refel = (lambda u: True) if el is None else el
            t0 = time.perf_counter_ns()
            for S in sets[:3]:
                REF.greatest(set(), S, RC.CachedGeo(3, pair.E), refel, 8)
            out['ref_c7_ns_%s' % conv][str(m)] = (time.perf_counter_ns() - t0)//3
    text = json.dumps(out, indent=1, sort_keys=True)
    if '--out' in args:
        with open(args[args.index('--out') + 1], 'w') as f:
            f.write(text + '\n')
    print(text)


if __name__ == '__main__':
    main()
