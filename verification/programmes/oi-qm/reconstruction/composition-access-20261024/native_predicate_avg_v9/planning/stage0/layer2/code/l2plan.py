"""NP-AVG-1 Stage 0 Layer 2: the dry run (section 5b item 1; certificate item 7).

Computes, from the configuration constants alone, the index space, the orbit count (by
Burnside's lemma), the shard plan, the context-size histogram, the masking-equivalent
record count and the cost estimate. It imports neither the engine (s0geom) nor the
reference (s0ref): it constructs no Setup, no Context and no record through the guarded
entry points, and computes no closure (static check L2-S1 verifies the imports). Its
formulas are checked against the engine on the toy profile by l2selftest (L2-PLAN, L2-MASK).

Usage: python3 -I -B l2plan.py --profile toy|v8 [--calib calib.json] [--out dryrun.json]
                               [--shared-tips]
--shared-tips enumerates the record space combinatorially (no closure) to count records with
a shared near tip (C7's scope); it is run in the authorized CI dry run, not locally on v8.
"""
import hashlib
import json
import os
import sys
from collections import Counter
from fractions import Fraction
from itertools import permutations, product

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import l2config as CFG  # noqa: E402


def lball(r, dim):
    if r < 0:
        return []
    if dim == 0:
        return [()]
    return [(x,) + rest for x in range(-r, r + 1) for rest in lball(r - abs(x), dim - 1)]


def norm(c):
    return sum(abs(i) for i in c)


class Space:
    def __init__(self, prof):
        s = prof['setup']
        self.dim, self.n, self.rho, self.tlast = s['dim'], s['n'], s['rho'], s['tlast']
        self.port = tuple(s['port'])
        self.k = prof['k']
        self.region = sorted(lball(self.rho, self.dim))
        self.slices = list(range(-1, self.tlast + 1))
        o = (0,)*self.dim
        six = []
        for i in range(self.dim):
            for sg in (1, -1):
                six.append((tuple(sg if j == i else 0 for j in range(self.dim)), self.n + 1))
        self.fixed = set(six) | {(o, self.n + 2), (o, self.n)}
        self.port_even = {(self.port, s) for s in range(0, self.n + 1) if (norm(self.port) + s) % 2 == 0}
        self.removed = self.fixed | self.port_even

    def n_records(self):
        ni, ns, nt = len(self.region)*len(self.slices), len(self.region), len(self.slices)
        return ni + (ns*(ns - 1)//2)*nt*nt if self.k == 2 else ni

    def item_set(self, x, t):
        return {(x, s) for s in range(-1, t + 1) if (norm(x) + s) % 2 == 0} - self.removed

    def group(self):
        dim = self.dim
        q8 = tuple(-1 if j == dim - 1 else 0 for j in range(dim))
        q10 = tuple(1 if j == dim - 1 else 0 for j in range(dim))
        reg = set(self.region)
        out = []
        for pp in permutations(range(dim)):
            for ss in product((1, -1), repeat=dim):
                def a(c, pp=pp, ss=ss):
                    return tuple(ss[i]*c[pp[i]] for i in range(dim))
                if {a(c) for c in reg} == reg and a(self.port) == self.port and a(q8) == q8 and a(q10) == q10:
                    out.append(a)
        return out

    def orbits_burnside(self):
        grp = self.group()
        nt = len(self.slices)
        fix1 = sum(sum(1 for x in self.region if g(x) == x)*nt for g in grp)
        fix2 = 0
        for g in grp:
            nf = sum(1 for x in self.region if g(x) == x)
            swaps = sum(1 for x in self.region if g(x) != x and g(g(x)) == x)//2
            fix2 += (nf*(nf - 1)//2)*nt*nt + swaps*nt
        single = fix1//len(grp)
        pair = fix2//len(grp) if self.k == 2 else 0
        return len(grp), single, pair


def shard_plan(N, S):
    return [{'shard': s, 'lo': s*N//S, 'hi': (s + 1)*N//S, 'count': (s + 1)*N//S - s*N//S} for s in range(S)]


def context_histogram(sp):
    """Histogram of the number of non-fixed context quantities over all records (singles and
    two-site pairs), from per-item sample counts."""
    base = len(sp.port_even - sp.fixed)
    per_site = {x: Counter(len(sp.item_set(x, t)) for t in sp.slices) for x in sp.region}
    singles = Counter()
    for h in per_site.values():
        for a, c in h.items():
            singles[base + a] += c
    pairs = Counter()
    if sp.k == 2:
        tot = Counter()
        for h in per_site.values():
            tot.update(h)
        for a, ca in tot.items():
            for b, cb in tot.items():
                pairs[base + a + b] += ca*cb
        for h in per_site.values():
            for a, ca in h.items():
                for b, cb in h.items():
                    pairs[base + a + b] -= ca*cb
        pairs = Counter({k: v//2 for k, v in pairs.items() if v})
    return singles, pairs


def masking_equivalent(sp, merge_fixed=True):
    """Number of records in masking-equivalence classes of size >= 2 (E2). With merge_fixed
    (the plan's reading, 'equal even-class contexts'), samples that are fixed quantities or
    port samples are merged with them (E1); with merge_fixed False, records are compared by
    their even record samples alone (the code-r5 design-evidence reading). Exact integers.
    Canonical form: an item (x, t) maps to (x, m), m the largest slice of its sample set
    (empty sets map to nothing); two records have equal sample sets iff their canonical
    forms are equal (LAYER2-PLAN.md PO-L2-7)."""
    rem = sp.removed if merge_fixed else set()

    def m_of(x, t):
        st = {(x, s) for s in range(-1, t + 1) if (norm(x) + s) % 2 == 0} - rem
        return max(s for _, s in st) if st else None
    c = {x: Counter(m_of(x, t) for t in sp.slices) for x in sp.region}
    E = {x: c[x].get(None, 0) for x in sp.region}
    Etot = sum(E.values())
    total = 0

    def add(size):
        return size if size >= 2 else 0
    # empty class: singles with empty sets and pairs of empty items at distinct sites
    empty = Etot + ((Etot*Etot - sum(v*v for v in E.values()))//2 if sp.k == 2 else 0)
    total += add(empty)
    for x in sp.region:
        for m, cxm in c[x].items():
            if m is None:
                continue
            total += add(cxm + (cxm*(Etot - E[x]) if sp.k == 2 else 0))
    if sp.k == 2:
        reg = sp.region
        for i in range(len(reg)):
            for j in range(i + 1, len(reg)):
                for m1, c1 in c[reg[i]].items():
                    if m1 is None:
                        continue
                    for m2, c2 in c[reg[j]].items():
                        if m2 is not None:
                            total += add(c1*c2)
    return total


def near_tips(q, E):
    """{(e, tip)} of q's near tips for the pair (E, E+1) (plan section 2)."""
    c, t = q
    L = E + 1
    d, near = (t - L, L) if t >= L else (E - t, E)
    dim = len(c)
    out = set()
    for i in range(dim):
        for sg in (1, -1):
            e = tuple(sg if j == i else 0 for j in range(dim))
            out.add((e, (tuple(a + d*b for a, b in zip(c, e)), near)))
    return out


def shared_tip_records(sp):
    """Records whose initial context (non-fixed quantities) has a cell that is the e-near-tip
    of two distinct quantities, per convention (A: pair (n+1, n+2); G: pair (-1, 0)).
    Enumerates the record space combinatorially; no closure."""
    out = {}
    for conv, E in (('A', sp.n + 1), ('G', -1)):
        port_q = sp.port_even - sp.fixed

        def tipsets(qs):
            return [near_tips(q, E) for q in sorted(qs)]

        def shared(qs):
            seen = {}
            for i, ts in enumerate(tipsets(qs)):
                for k in ts:
                    if k in seen and seen[k] != i:
                        return True
                    seen[k] = i
            return False
        items = [(x, t) for x in sp.region for t in sp.slices]
        sets = {it: sp.item_set(*it) for it in items}
        n = sum(shared(port_q | sets[it]) for it in items)
        if sp.k == 2:
            for i, a in enumerate(sp.region):
                for b in sp.region[i + 1:]:
                    for t1 in sp.slices:
                        for t2 in sp.slices:
                            n += shared(port_q | sets[(a, t1)] | sets[(b, t2)])
        out[conv] = n
    return out


def estimate(sp, hist, orbits, N, calib, prof):
    """Cost estimate in runner-seconds, as an exact fraction rounded up: representatives per
    context size (records scaled by orbits/N) x [2 tA(m) + 2 tG(m)] (four closures per
    representative) x the gate overhead factor x 2 (normal and -O runs)."""
    bud = CFG.CONFIG['budget']
    singles, pairs = hist
    tA = {int(k): v for k, v in calib['closure_ns_A'].items()}
    tG = {int(k): v for k, v in calib['closure_ns_G'].items()}

    def t_of(table, m):
        ks = sorted(table)
        hi = [k for k in ks if k >= m]
        return table[hi[0]] if hi else table[ks[-1]]*m//ks[-1]
    ns = 0
    for m, cnt in list(singles.items()) + list(pairs.items()):
        ns += cnt*(2*t_of(tA, m) + 2*t_of(tG, m))
    ns = Fraction(ns*orbits, N)*bud['gate_overhead_factor']*2
    seconds = -((-ns.numerator)//(ns.denominator*10**9))
    budget_s = bud['runner_hours']*3600
    shard_s = bud['timeout_minutes']['shard']*60
    per_shard = -((-seconds)//prof['shards'])
    frac_ok = seconds*bud['launch_if_estimate_at_most_denominator'] <= budget_s*bud['launch_if_estimate_at_most_numerator']
    shard_ok = per_shard*bud['launch_if_estimate_at_most_denominator'] <= shard_s*bud['launch_if_estimate_at_most_numerator']
    return {'estimate_runner_seconds': seconds, 'estimate_per_shard_seconds': per_shard,
            'budget_runner_seconds': budget_s, 'shard_timeout_seconds': shard_s,
            'launch_within_budget': frac_ok and shard_ok,
            'excludes': 'the C7 reference on shared-tip records and every per-survivor gate (survivor count '
                        'unknown before the run); see LAYER2-PLAN.md section 3'}


def main():
    args = sys.argv[1:]
    pname = args[args.index('--profile') + 1]
    prof = CFG.profile(pname)
    sp = Space(prof)
    N = sp.n_records()
    gorder, so, po = sp.orbits_burnside()
    S = prof['shards']
    singles, pairs = context_histogram(sp)
    out = {'schema': 'np-avg-1/stage0/layer2/dryrun/1', 'profile': pname, 'records': N,
           'group_order': gorder, 'orbits': so + po, 'single_orbits': so, 'pair_orbits': po,
           'shards': shard_plan(N, S), 'context_quantities_singles': {str(k): v for k, v in sorted(singles.items())},
           'context_quantities_pairs': {str(k): v for k, v in sorted(pairs.items())},
           'max_context_quantities': max(list(singles) + list(pairs)),
           'max_context_with_fixed': max(list(singles) + list(pairs)) + len(sp.fixed),
           'closures_computed': 0, 'contexts_constructed': 0, 'engine_imported': 'l2plan imports no engine',
           'config_sha256': CFG.config_sha256()}
    if not prof['requires_authorization']:
        # a reported count (section 6, C8); computed in the dry run for the toy profile only. For
        # v8 the merge computes it in the authorized run.
        out['masking_equivalent_records'] = masking_equivalent(sp, True)
        out['masking_equivalent_records_record_sample_reading'] = masking_equivalent(sp, False)
    exp = CFG.CONFIG['expected'].get(pname, {})
    checks = {}
    for k_exp, k_out in (('records', 'records'), ('orbits', 'orbits'), ('group_order', 'group_order')):
        if k_exp in exp:
            checks[k_exp] = exp[k_exp] == out[k_out]
    out['expected_checks'] = checks
    if '--shared-tips' in args:
        out['shared_tip_records'] = shared_tip_records(sp)
    if '--calib' in args:
        with open(args[args.index('--calib') + 1], 'rb') as f:
            raw = f.read()
        calib = json.loads(raw)
        out['calib_sha256'] = hashlib.sha256(raw).hexdigest()
        out['cost'] = estimate(sp, (singles, pairs), so + po, N, calib, prof)
    out['pass'] = all(checks.values())
    text = json.dumps(out, sort_keys=True, indent=1)
    if '--out' in args:
        with open(args[args.index('--out') + 1], 'w') as f:
            f.write(text + '\n')
    print(text)
    sys.exit(0 if out['pass'] else 2)


if __name__ == '__main__':
    main()
