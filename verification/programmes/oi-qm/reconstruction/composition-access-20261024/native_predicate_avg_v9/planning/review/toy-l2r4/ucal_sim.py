"""Reviewer probe: sampling spread of calib_aggregate's u_cal candidates at n calibrations,
lognormal per-calibration aggregates with log-sigma s (true p99 of the ratio = exp(2.326*sqrt2*s))."""
import random, math, statistics, json
rng = random.Random(1)
out = {}
for n in (10, 20, 40):
    for s in (0.06, 0.09):
        e, nm, mm = [], [], []
        for _ in range(2000):
            a = [math.exp(rng.gauss(0, s)) for _ in range(n)]
            pr = sorted(x/y for i, x in enumerate(a) for j, y in enumerate(a) if i != j)
            e.append(pr[math.ceil(0.99*len(pr)) - 1]); mm.append(max(a)/min(a))
            nm.append(math.exp(2.326*math.sqrt(2)*statistics.stdev(math.log(x) for x in a)))
        q = lambda v, p: sorted(v)[int(p*len(v))]
        out['n=%d s=%.2f' % (n, s)] = {'true': round(math.exp(2.326*math.sqrt(2)*s), 3),
            'empirical_p99 [5%,50%,95%]': [round(q(e, p), 3) for p in (.05, .5, .95)],
            'normal [5%,50%,95%]': [round(q(nm, p), 3) for p in (.05, .5, .95)],
            'max/min [5%,50%,95%]': [round(q(mm, p), 3) for p in (.05, .5, .95)]}
print(json.dumps(out, indent=1))
