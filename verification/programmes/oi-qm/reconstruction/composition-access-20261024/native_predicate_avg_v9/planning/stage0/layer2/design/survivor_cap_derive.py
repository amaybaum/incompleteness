"""Layer-2 design evidence (r5; owner 2026-10-26: "The survivor cap should likewise follow from a
justified resource and completeness analysis, not a convenient placeholder"). Deterministic; reads
design/overhead/survivor-cap.json (memory and time per gated survivor orbit, measured on planted
toy-geometry orbits; the v8 survivor term per cap unit from the planted calibration) and computes:

1. Completeness: P(INCOMPLETE by the cap) = P(some shard receives more than c survivor orbits). Under
   the deterministic subdivision every shard holds floor or ceil of R/S representatives (exact; on v8
   R/S = 816,050/32, about 25,500), so a survivor orbit's shard is uniform over shards if survivors are
   spread over representatives independently of index. Survivors are not expected to be independent:
   they come from geometric constraint blocks, and the planted ones cluster. The clustering is not
   measured on any available class (the toy class and the four mid-size shards have no survivor), so
   it enters as a parameter: X survivor orbits arrive as X/b clusters of b orbits, each cluster wholly
   in one shard (a site pair holds at most 625 representatives, under 3 % of a v8 shard, so a cluster
   within a site pair falls in one shard or straddles two; one shard is the conservative case), the
   clusters uniform and independent. P is computed exactly (a polynomial-coefficient recursion over
   shards, in exact rationals).
2. Resources per shard at cap c: kept memory c x 0.55 MB and transient 2.0 MB (measured maxima);
   time c x t_orbit both copies, t_orbit = survivor term per cap unit / S (model, planted calibration).
3. The derived cap c*(X, b, alpha): the smallest c with P <= alpha; with its memory and time, the
   campaign cost c x (survivor term per cap unit), and the per-job inequality's room at S = 32.
The assumptions that are judgements (alpha, the reference X, b) are reported as parameters; the
proposal states which it uses. Usage: python3 -I -B survivor_cap_derive.py <survivor-cap.json> <out.json>"""
import json
import sys
from fractions import Fraction
from math import factorial

inp, outp = sys.argv[1], sys.argv[2]
with open(inp) as f:
    sc = json.load(f)
S = 32
per_cap_unit = sc['model']['v8_survivor_term_per_cap_unit_runner_seconds_median']     # both copies, all shards
t_orbit = per_cap_unit/S                                                                # per shard, both copies
mem_kept = sc['measured_planted']['kept_bytes']['max']
mem_peak = sc['measured_planted']['peak_transient_bytes']['max']


def p_exceed(X, b, c, S=S):
    """P(some shard gets more than c orbits), X orbits in ceil(X/b) clusters of b (the last smaller), each
    cluster uniform over S shards, independent. Exact. A shard gets more than c orbits iff it gets more
    than floor(c/b) full clusters (the partial cluster is placed as a full one: conservative)."""
    n = -(-X//b)
    m = c//b
    # P(every shard <= m clusters) = n!/S^n * [x^n] (sum_{k<=m} x^k/k!)^S
    poly = [Fraction(1, factorial(k)) for k in range(min(m, n) + 1)]
    acc = [Fraction(1)]
    for _ in range(S):
        new = [Fraction(0)]*(min(len(acc) + len(poly) - 1, n + 1))
        for i, a in enumerate(acc):
            if a == 0:
                continue
            for j, p in enumerate(poly):
                if i + j > n:
                    break
                new[i + j] += a*p
        acc = new
    ok = acc[n]*factorial(n)/Fraction(S)**n if n < len(acc) else Fraction(0)
    return float(1 - ok)


XS, BS, ALPHAS = (16, 32, 64, 128), (1, 4, 8, 16), (0.01, 0.05)
CS = (4, 8, 12, 16, 24, 32, 48, 64)
table = {}
for X in XS:
    for b in BS:
        table['X=%d,b=%d' % (X, b)] = {str(c): p_exceed(X, b, c) for c in CS}
derived = {}
for alpha in ALPHAS:
    for X in XS:
        for b in BS:
            c_star = next((c for c in range(1, 257) if p_exceed(X, b, c) <= alpha), None)
            derived['alpha=%s,X=%d,b=%d' % (alpha, X, b)] = c_star
res = {'schema': 'np-avg-1/stage0/layer2/survivor-cap-derivation/1', 'shards': S,
       'inputs': {'survivor_term_per_cap_unit_runner_seconds': per_cap_unit, 't_orbit_per_shard_both_copies_s':
                  round(t_orbit, 1), 'kept_bytes_per_orbit_max': mem_kept, 'peak_transient_bytes_max': mem_peak,
                  'source': 'survivor-cap.json: planted toy-geometry orbits (memory, measured); the planted calibration '
                            '(time per orbit at m_max, modelled)'},
       'assumptions': ['survivor orbits uniform over representatives (exact representative balance under the '
                       'deterministic subdivision; independence of index is assumed)',
                       'clusters of b orbits, each wholly in one shard, independent (b not measured: no class '
                       'available here has a survivor)',
                       'the time per orbit is the cost model at m_max (unvalidated; LAYER2-PLAN.md section 3.6)'],
       'P_incomplete_by_cap': table, 'derived_cap_smallest_c_with_P_le_alpha': derived,
       'resources_by_cap': {str(c): {'kept_MB_per_shard': round(c*mem_kept/1e6, 1),
                                     'peak_transient_MB': round(mem_peak/1e6, 1),
                                     'seconds_per_shard_both_copies': round(c*t_orbit, 1),
                                     'campaign_runner_seconds': round(c*per_cap_unit)} for c in CS}}
with open(outp, 'w') as f:
    json.dump(res, f, sort_keys=True, indent=1)
    f.write('\n')
print(json.dumps({'derived_alpha_0.01': {k: v for k, v in derived.items() if k.startswith('alpha=0.01')},
                  't_orbit': round(t_orbit, 1)}, sort_keys=True))
