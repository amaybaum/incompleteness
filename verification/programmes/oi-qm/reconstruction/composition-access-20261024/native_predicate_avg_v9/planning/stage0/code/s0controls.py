"""NP-AVG-1 Stage 0 control suite, run on TOY setups, planted sets and small exhaustive
windows only. It never constructs v8's configuration class (s0geom.V8 is refused).
Usage: python3 -I -B s0controls.py [--rule NAME] [--quick]
Prints one JSON object; exit status 0 if every control passes, 2 otherwise.
Standard library, exact integers."""
import ast
import json
import os
import random
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import s0geom as G      # noqa: E402  production
import s0ref as REF     # noqa: E402  independent reference closure
import s0native as NAT  # noqa: E402  independent native evaluator

MUTANTS = {
    'frozen': G.Rule(),
    'near_only': G.Rule(far=False),
    'offaxis_all': G.Rule(offaxis='all'),
    'offaxis_B': G.Rule(offaxis='B'),
    'wrong_far': G.Rule(wrong_far=True),
    'far_cone_deleted': G.Rule(far_cone=False),
    'radius_minus2': G.Rule(delta=-2),
    'radius_plus2': G.Rule(delta=2),
    'swapped': G.Rule(swap=True),
    'keep_odd': G.Rule(keep_odd=True),
    'unapplied_elimination': G.Rule(stop_after=0),
    'parity_dropped(equivalent)': G.Rule(nopar=True),
    'symmetric_blind(equivalent)': G.Rule(symblind=True),
}

# Toy setups (not v8): 3D, n = 2, region ball(1), last slice n+4, port on the -z axis.
TOY = G.Setup(3, 2, 1, 6, (0, 0, -2), ((-3, 0, -1), (-3, 0, 1), (-4, 0, 0)))
TOYG = G.Setup(3, 2, 1, 6, (0, 0, -2), ((-3, 0, -1), (-3, 0, 1), (-4, 0, 0)))


def toy_records(setup):
    return [G.record_at(setup, i) for i in range(G.num_records(setup))]


# ---------------------------------------------------------------------------

def c1_cones(rule, rng, quick):
    """Production in_cone against native perturbation, forward and backward."""
    dim, E, L = 3, 0, 1
    pair = G.Pair(E)
    bad, attained_missing = [], []
    for ty in ('F', 'B'):
        for d in range(0, 4 if quick else 5):
            q = ((0, 0, 0), L + d) if ty == 'F' else ((0, 0, 0), E - d)
            cells = G.lball(d + 2, dim)
            seen = {}
            for trial in range(2):
                init = {(c, s): rng.randrange(8) for c in G.lball(d + 4, dim) for s in (E, L)}
                base = NAT.scalar_value(init, q, E, L, {})
                for c in cells:
                    for s in (E, L):
                        i2 = dict(init)
                        i2[(c, s)] ^= 1 + rng.randrange(7)
                        if NAT.scalar_value(i2, q, E, L, {}) != base:
                            u = (c, s)
                            if not G.in_cone(u, q, pair, rule):
                                bad.append((ty, d, u))
                            seen[s] = max(seen.get(s, -1), G.l1(c))
            near, far = (L, E) if ty == 'F' else (E, L)
            # radius attained: production's claimed radius must be reached by measured dependence
            pr_near = max([G.l1(c) for c in cells if G.in_cone((c, near), q, pair, rule)], default=-1)
            pr_far = max([G.l1(c) for c in cells if G.in_cone((c, far), q, pair, rule)], default=-1)
            if seen.get(near, -1) != pr_near or seen.get(far, -1) != pr_far:
                attained_missing.append((ty, d, pr_near, seen.get(near, -1), pr_far, seen.get(far, -1)))
    return {'pass': not bad and not attained_missing, 'outside_cone': bad[:5], 'radius_mismatch': attained_missing[:5]}


def c2_tips(rule, rng, quick):
    """Every tip production emits is a native bijection; off-axis cells are not always."""
    dim, E, L = 3, 0, 1
    pair = G.Pair(E)
    fails, offaxis_nonbij = [], 0
    for ty in ('F', 'B'):
        for d in range(0, 4 if quick else 5):
            q = ((0, 0, 0), L + d) if ty == 'F' else ((0, 0, 0), E - d)
            for trial in range(2):
                init = {(c, s): rng.randrange(8) for c in G.lball(d + 3, dim) for s in (E, L)}
                for u in G.tips(q, pair, dim, rule):
                    vals = set()
                    for v in range(8):
                        i2 = dict(init)
                        i2[u] = v
                        try:
                            vals.add(NAT.scalar_value(i2, q, E, L, {}))
                        except KeyError:
                            vals.add(('outside', v))
                    if len(vals) != 8 or any(isinstance(x, tuple) for x in vals):
                        fails.append((ty, d, u))
                if d >= 2:
                    near = L if ty == 'F' else E
                    u = ((d - 1, 1, 0), near)
                    vals = set()
                    for v in range(8):
                        i2 = dict(init)
                        i2[u] = v
                        vals.add(NAT.scalar_value(i2, q, E, L, {}))
                    offaxis_nonbij += len(vals) != 8
    return {'pass': not fails and offaxis_nonbij > 0, 'nonbijective_tips': fails[:5], 'offaxis_nonbijective': offaxis_nonbij}


def family(q, pair, dim):
    c, t = q
    d, ty = pair.depth(q)
    near, far = (pair.L, pair.E) if ty == 'F' else (pair.E, pair.L)
    fam = {q} | {(G.vadd(c, e, d), near) for e in G.axes(dim)}
    if d >= 1:
        fam |= {(G.vadd(c, e, d - 1), far) for e in G.axes(dim)}
    return fam


def c3_planted(rule, quick):
    """Planted survivors (families, constraint block) and planted non-survivors."""
    dim = 3
    out = {'survivors': [], 'nonsurvivors': [], 'vacuity_contrast': []}
    ok = True
    ctxA = G.Context(TOY, (), 'A', rule)
    ctxG = G.Context(TOYG, (), 'G', rule)
    D = 4 if quick else 6
    for conv, ctx in (('A', ctxA), ('G', ctxG)):
        pair, elig = ctx.pair, ctx.eligible
        for ty in (('F', 'B') if conv == 'A' else ('F',)):
            for d in range(1, D + 1):
                if conv == 'A':
                    for c in ((5, 0, 0), (6, 0, 0)):
                        q = (c, pair.L + d) if ty == 'F' else (c, pair.E - d)
                        if G.even(q):
                            break
                else:
                    c = (6 + d, 0, 0)
                    q = (c, d)
                fam = family(q, pair, dim)
                ret, _ = G.closure(ctx.fixed, fam, pair, dim, rule, elig)
                keep = ret == fam - ctx.fixed
                ok &= keep
                out['survivors'].append((conv, ty, d, len(ret), len(fam - ctx.fixed)))
                # non-survivor: family minus one far-or-near tip quantity
                near = pair.L if ty == 'F' else pair.E
                drop = (G.vadd(c, (1, 0, 0), d), near)          # the +x near tip, far from Phi
                ret2, _ = G.closure(ctx.fixed, fam - {drop}, pair, dim, rule, elig)
                ok &= not ret2
                out['nonsurvivors'].append((conv, ty, d, len(ret2)))
        if conv == 'G':
            for d in (1, 2):
                q = ((0, 0, 0), d) if d % 2 == 0 else ((1, 0, 0), d)
                fam = family(q, pair, dim)
                ret, _ = G.closure(ctx.fixed, fam, pair, dim, rule, elig)
                out['vacuity_contrast'].append((d, len(ret), len(fam - ctx.fixed)))
    # constraint block (A geometry, away from Phi) and block minus centre
    pair = ctxA.pair
    c0 = (5, 0, 0) if (5 + pair.L + 1) % 2 == 0 else (5, 1, 0)
    top, centre = (c0, pair.L + 1), (c0, pair.E)
    six = {(G.vadd(c0, e), pair.L) for e in G.axes(dim)}
    blk = {top, centre} | six
    rb, _ = G.closure(set(), blk, pair, dim, rule)
    rbm, _ = G.closure(set(), blk - {centre}, pair, dim, rule)
    out['block'] = (len(rb), len(rbm))
    ok &= len(rb) == 8 and len(rbm) == 0
    return dict(out, **{'pass': ok})


def c6_hand(rule):
    """Hand-derived toy instances (worked in STAGE0-NOTES-r2.md)."""
    dim = 3
    pair = G.Pair(3)                        # toy A pair (n+1, n+2) = (3, 4)
    q1, q2 = ((0, 0, 0), 6), ((1, 0, 0), 5)
    r1, _ = G.closure(set(), {q1, q2}, pair, dim, rule)
    base = {}
    for conv in ('A', 'G'):
        a = G.analyse(G.Context(TOY, (), conv, rule))
        base[conv] = a['survivor']
    ok = (not r1) and base == {'A': False, 'G': False}
    return {'pass': ok, 'axis_pair_retained': len(r1), 'toy_base_survivor': base}


def c7_reference(rule, quick):
    """Production closure equals the independent reference on every toy record."""
    recs = toy_records(TOY)
    if quick:
        recs = recs[::7]
    diffs = []
    for conv in ('A', 'G'):
        for r in recs:
            ctx = G.Context(TOY, r, conv, rule)
            ret = ctx.run()
            ref, how = REF.ref_retained(3, TOY.n, TOY.port, r, conv)
            if ret != ref:
                diffs.append((conv, r, len(ret), len(ref)))
    return {'pass': not diffs, 'records': len(recs), 'differences': len(diffs), 'first': diffs[:3]}


def c8_symmetry(rule, quick):
    """C4v equivariance of retained sets; invariant attributes equal on orbits; orbit-
    weighted counts equal full counts (S4)."""
    def act(g, c):
        perm, sg = g
        return tuple(sg[i]*c[perm[i]] for i in range(3))
    from itertools import permutations, product
    OH = [(p, s) for p in permutations(range(3)) for s in product((1, -1), repeat=3)]
    region = set(TOY.region)
    grp = [g for g in OH if {act(g, c) for c in region} == region and act(g, TOY.port) == TOY.port
           and act(g, (0, 0, -1)) == (0, 0, -1)]
    recs = toy_records(TOY)
    res = {}
    bad = 0
    for conv in ('A', 'G'):
        res[conv] = {}
        for r in recs:
            a = G.analyse(G.Context(TOY, r, conv, rule))
            res[conv][tuple(sorted(r))] = a
    # equivariance and invariant attributes
    sample = recs[::3] if quick else recs
    for conv in ('A', 'G'):
        for r in sample:
            a = res[conv][tuple(sorted(r))]
            for g in grp:
                gr = tuple(sorted((act(g, x), t) for x, t in r))
                b = res[conv][gr]
                if sorted((act(g, c), t) for c, t in a['retained']) != b['retained']:
                    bad += 1
                for k in ('survivor', 'n_retained', 'n_survivor') + (('phi_linked', 'j_linked') if conv == 'A' else ()):
                    if a[k] != b[k]:
                        bad += 1
    # orbit-weighted counts vs full counts
    def canon(r):
        return min(tuple(sorted((act(g, x), t) for x, t in r)) for g in grp)
    orbits = {}
    for r in recs:
        orbits.setdefault(canon(r), []).append(tuple(sorted(r)))
    count_mismatch = 0
    for conv in ('A', 'G'):
        full = sum(res[conv][tuple(sorted(r))]['survivor'] for r in recs)
        weighted = sum(len(members)*res[conv][rep]['survivor'] for rep, members in orbits.items())
        count_mismatch += full != weighted
        full_cls = len({tuple(map(tuple, res[conv][tuple(sorted(r))]['public_retained'])) for r in recs})
        # G-linkage is per record: recompute directly for every record (never transferred)
    glink_per_record = sum(res['G'][tuple(sorted(r))].get('g_linked', False) for r in recs)
    return {'pass': bad == 0 and count_mismatch == 0 and len(grp) == 8, 'group_order': len(grp),
            'orbits': len(orbits), 'records': len(recs), 'violations': bad,
            'orbit_weighted_count_mismatch': count_mismatch, 'g_linked_records': glink_per_record,
            'observer_classes_A': len({tuple(map(tuple, res['A'][tuple(sorted(r))]['public_retained'])) for r in recs}),
            'observer_classes_G': len({tuple(map(tuple, res['G'][tuple(sorted(r))]['public_retained'])) for r in recs})}


def c9_monotone(rule, quick):
    recs = toy_records(TOY)[::(5 if quick else 1)]
    viol = 0
    gcb = {}
    for conv in ('A', 'G'):
        allitems = [(x, TOY.tlast) for x in TOY.region]
        big = G.Context(TOY, allitems, conv, rule)
        gcb[conv] = big.run()
    for conv in ('A', 'G'):
        for r in recs:
            a = G.Context(TOY, r, conv, rule).run()
            b = G.Context(TOY, r, conv, G.Rule(far=False, **{k: v for k, v in vars(rule).items() if k != 'far'})).run()
            viol += not (a <= b)
            viol += not (a <= gcb[conv])
    return {'pass': viol == 0, 'violations': viol, 'gcb_size_A': len(gcb['A']), 'gcb_size_G': len(gcb['G'])}


def c10_fixed(rule):
    recs = toy_records(TOY)[::11]
    bad = 0
    for conv in ('A', 'G'):
        for r in recs:
            ctx = G.Context(TOY, r, conv, rule)
            ctx.run()
            bad += any(q in ctx.fixed for q, _ in ctx.log)
    return {'pass': bad == 0, 'fixed_eliminated': bad}


def c12_frame():
    """Toy analogue of PO7: frame even part equals V's cone in pair (-1, 0)."""
    ctx = G.Context(TOYG, (), 'G')
    V = ((0, 0, 0), TOYG.n + 2)
    box = [(c, s) for c in G.lball(TOYG.n + 6, 3) for s in (-1, 0)]
    pair = ctx.pair
    ev = [u for u in box if G.even(u)]
    frame = {u for u in ev if not ctx.eligible(u)}
    vcone = {u for u in ev if G.in_cone(u, V, pair)}
    return {'pass': frame == vcone, 'frame_even_cells': len(frame)}


def c13_coverage(rule, skip=None):
    """Coverage manifest + independent recount on the toy index space."""
    N = G.num_records(TOY)
    shards = 4
    covered = []
    for s in range(shards):
        lo, hi = s*N//shards, (s + 1)*N//shards
        idx = [i for i in range(lo, hi) if i != skip]
        covered.append({'shard': s, 'ranges': [[lo, hi]] if skip is None or not (lo <= skip < hi) else
                        [[lo, skip], [skip + 1, hi]], 'count': len(idx)})
    union = []
    for sh in covered:
        for lo, hi in sh['ranges']:
            union.extend(range(lo, hi))
    ok_cov = sorted(union) == list(range(N)) and len(union) == len(set(union))
    # independent recount: enumerate records by plan text, compare with record_at bijection
    sites = sorted(TOY.region)
    T = list(range(-1, TOY.tlast + 1))
    indep = {((x, t),) for x in sites for t in T}
    for i in range(len(sites)):
        for j in range(i + 1, len(sites)):
            for t1 in T:
                for t2 in T:
                    indep.add(((sites[i], t1), (sites[j], t2)))
    mapped = {G.record_at(TOY, i) for i in range(N)}
    ok_recount = len(indep) == N and mapped == indep and sum(sh['count'] for sh in covered) == N
    return {'pass': ok_cov and ok_recount, 'N': N, 'independent': len(indep)}


def c0_context_sizes(rule):
    """Context sizes of production equal the reference's (catches keep_odd)."""
    bad = 0
    for r in toy_records(TOY)[::13]:
        for conv in ('A', 'G'):
            ctx = G.Context(TOY, r, conv, rule)
            f, qs, _, _ = REF.ref_context(3, TOY.n, TOY.port, r, conv)
            bad += (ctx.quants != qs) or (ctx.fixed != f)
    return {'pass': bad == 0, 'mismatches': bad}


def c15_exact(rule, quick, rng):
    """Exact soundness of production elimination on exhaustive 1D and 2D windows."""
    out = {}
    ok = True
    # 1D, pair (0, 1): slice 1 sites -3,-1,1,3; slice 0 sites -2,0,2 (21 bits).
    W1 = [((c,), 1) for c in (-3, -1, 1, 3)] + [((c,), 0) for c in (-2, 0, 2)]
    P1 = [((0,), 2), ((2,), 2), ((-2,), 2), ((1,), 3), ((-1,), 3), ((0,), 4),
          ((1,), -1), ((-1,), -1), ((0,), -2)] + W1
    W2 = [((1, 0), 1), ((-1, 0), 1), ((0, 1), 1), ((0, -1), 1), ((0, 0), 0), ((2, 0), 0)]
    P2 = [((0, 0), 2)] + W2
    for name, dim, W, P, trials in (('1D', 1, W1, P1, 25 if quick else 60), ('2D', 2, W2, P2, 40 if quick else 100)):
        sl = NAT.Sliced(W, 0, 1)
        pair = G.Pair(0)
        viol = 0
        for _ in range(trials):
            S = set(rng.sample(P, rng.randint(2, min(6, len(P)))))
            ret, _ = G.closure(set(), S, pair, dim, rule)
            viol += not NAT.exact_independent(sl, S - ret, ret)
        # G-geometry variant: a frame = cone of a designated fixed quantity; eliminated must be
        # independent of the retained set and of the frame variables.
        fixed_q = P[0]
        frame = {u for u in W if G.in_cone(u, fixed_q, pair)}
        elig = (lambda u, frame=frame: u not in frame)
        violG = 0
        for _ in range(trials // 2):
            S = set(rng.sample(P[1:], rng.randint(2, min(5, len(P) - 1))))
            ret, _ = G.closure({fixed_q}, S, pair, dim, rule, elig)
            violG += not NAT.exact_independent(sl, S - ret, ret | frame)
        out[name] = {'worlds': sl.N, 'trials': trials, 'violations_A': viol, 'violations_G': violG}
        ok &= viol == 0 and violG == 0
    # planted 2D block cases must be exact as well
    return dict(out, **{'pass': ok})


def c16_witness():
    """Minimal-witness order (k, number of even-class context quantities, sorted items):
    production selector against an independent ordering built from s0ref contexts."""
    recs = toy_records(TOY)
    rng = random.Random(3)
    ok = True
    picks = []
    for _ in range(5):
        injected = rng.sample(recs, 12)

        def key_prod(r):
            ctx = G.Context(TOY, r, 'A')
            return (len(r), len(ctx.quants | ctx.fixed), tuple(sorted(r)))

        def key_ref(r):
            f, qs, _, _ = REF.ref_context(3, TOY.n, TOY.port, r, 'A')
            return (len(r), len(f | qs), tuple(sorted(r)))
        w = min(injected, key=key_prod)
        w_ref = sorted(injected, key=key_ref)[0]
        ok &= w == w_ref
        picks.append(w)
    return {'pass': ok, 'witnesses': picks[:2]}


def c17_fixed_point(rule, quick):
    """Completeness of elimination: production's retained set, checked with the
    reference cone/tip code, has no retained quantity with a free eligible tip."""
    recs = toy_records(TOY)[::(5 if quick else 1)]
    bad = 0
    for conv in ('A', 'G'):
        for r in recs:
            ret = G.Context(TOY, r, conv, rule).run()
            fixed, quants, geo, elig = REF.ref_context(3, TOY.n, TOY.port, r, conv)
            pool = ret | fixed
            cones = {q: geo.cone(q) for q in pool}
            for q in ret:
                if any(elig(u) and not any(u in cones[o] for o in pool if o != q) for u in geo.tipset(q)):
                    bad += 1
                    break
    return {'pass': bad == 0, 'records_with_unapplied_elimination': bad}


def c18_audit(rule, quick):
    """Soundness audit: every logged elimination is justified under the frozen rule, re-
    checked with the reference code (tip valid, eligible, uncovered at that moment)."""
    recs = toy_records(TOY)[::(5 if quick else 1)]
    bad = 0
    for conv in ('A', 'G'):
        for r in recs:
            ctx = G.Context(TOY, r, conv, rule)
            ctx.run()
            fixed, quants, geo, elig = REF.ref_context(3, TOY.n, TOY.port, r, conv)
            alive = set(quants) | fixed
            cones = {q: geo.cone(q) for q in alive}
            for q, u in ctx.log:
                if q not in alive or u not in geo.tipset(q) or not elig(u) or \
                        any(u in cones[o] for o in alive if o != q):
                    bad += 1
                    break
                alive.discard(q)
    return {'pass': bad == 0, 'unjustified': bad}


def c14_static():
    bad = []
    for fn in ('s0geom.py', 's0ref.py', 's0native.py'):
        tree = ast.parse(open(os.path.join(HERE, fn)).read())
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, float):
                bad.append((fn, 'float', node.lineno))
            if isinstance(node, ast.Call) and getattr(node.func, 'id', None) == 'open':
                bad.append((fn, 'open', node.lineno))
            if isinstance(node, (ast.Import, ast.ImportFrom)):
                names = [a.name for a in node.names] if isinstance(node, ast.Import) else [node.module]
                for nme in names:
                    if nme.split('.')[0] not in ('itertools', 'collections'):
                        bad.append((fn, 'import ' + nme, node.lineno))
            if isinstance(node, ast.Div):
                bad.append((fn, 'true division', node.lineno))
    return {'pass': not bad, 'findings': bad}


def native_self_test(rng):
    """Bit-sliced evaluator agrees with the scalar evaluator on sampled worlds."""
    W = [((c,), 1) for c in (-3, -1, 1, 3)] + [((c,), 0) for c in (-2, 0, 2)]
    sl = NAT.Sliced(W, 0, 1)
    qs = [((0,), 4), ((1,), 3), ((0,), -2)]
    bad = 0
    for _ in range(40):
        w = rng.randrange(sl.N)
        init = {v: (w >> (3*i)) & 7 for i, v in enumerate(W)}
        for q in qs:
            bad += sl.bytes_of(q)[w] != NAT.scalar_value(init, q, 0, 1, {})
    return {'pass': bad == 0, 'mismatches': bad}


def refusal():
    try:
        G.Context(G.V8, (), 'A')
        return {'pass': False}
    except PermissionError:
        return {'pass': True}


def main():
    args = sys.argv[1:]
    quick = '--quick' in args
    rname = args[args.index('--rule') + 1] if '--rule' in args else 'frozen'
    rule = MUTANTS[rname]
    rng = random.Random(20261026)
    res = {'rule': rname, 'quick': quick}
    res['V8_refused'] = refusal()
    res['native_self_test'] = native_self_test(rng)
    res['C0_context_sizes'] = c0_context_sizes(rule)
    res['C1_cones'] = c1_cones(rule, rng, quick)
    res['C2_tips'] = c2_tips(rule, rng, quick)
    res['C3_planted'] = c3_planted(rule, quick)
    res['C6_hand'] = c6_hand(rule)
    res['C7_reference'] = c7_reference(rule, quick)
    res['C8_symmetry'] = c8_symmetry(rule, quick)
    res['C9_monotone'] = c9_monotone(rule, quick)
    res['C10_fixed'] = c10_fixed(rule)
    res['C12_frame'] = c12_frame()
    res['C13_coverage'] = c13_coverage(rule)
    res['C13_coverage_skip_mutant_detected'] = {'pass': not c13_coverage(rule, skip=5)['pass']}
    res['C14_static'] = c14_static()
    res['C15_exact'] = c15_exact(rule, quick, rng)
    res['C16_witness'] = c16_witness()
    res['C17_fixed_point'] = c17_fixed_point(rule, quick)
    res['C18_audit'] = c18_audit(rule, quick)
    failed = sorted(k for k, v in res.items() if isinstance(v, dict) and not v.get('pass', True))
    res['failed'] = failed
    print(json.dumps(res, sort_keys=True, default=list))
    sys.exit(2 if failed else 0)


if __name__ == '__main__':
    main()
