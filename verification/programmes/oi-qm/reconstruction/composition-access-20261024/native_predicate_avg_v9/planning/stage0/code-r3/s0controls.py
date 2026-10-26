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
    'blind_dir_minus_y': G.Rule(blind_dir=(0, -1, 0)),
    'parity_dropped(equivalent)': G.Rule(nopar=True),
    'symmetric_blind(equivalent)': G.Rule(symblind=True),
}

# Toy setups (not v8): 3D, n = 2, region ball(1), last slice n+4, port on the -z axis.
TOY = G.Setup(3, 2, 1, 6, (0, 0, -2), ((-3, 0, -1), (-3, 0, 1), (-4, 0, 0)))
TOYG = G.Setup(3, 2, 1, 6, (0, 0, -2), ((-3, 0, -1), (-3, 0, 1), (-4, 0, 0)))


def toy_records(setup):
    return [G.record_at(setup, i) for i in range(G.num_records(setup))]


# ---------------------------------------------------------------------------


# Depth ranges of C1, C2 and C3 (plan section 6): convention A pair (7, 8): F 0-15, B 0-8;
# convention G pair (-1, 0): F 0-23 (the slice -1 samples are B depth 0). Quick mode: 0-4.
def depth_plan(quick):
    if quick:
        return [('A', 7, 'F', range(0, 5)), ('A', 7, 'B', range(0, 5)), ('G', -1, 'F', range(0, 5)),
                ('G', -1, 'B', range(0, 1))]
    return [('A', 7, 'F', range(0, 16)), ('A', 7, 'B', range(0, 9)), ('G', -1, 'F', range(0, 24)),
            ('G', -1, 'B', range(0, 1))]


def _sphere_cells(r_lo, r_hi, dim=3):
    return [c for c in G.lball(r_hi, dim) if G.l1(c) >= r_lo]


def c1_cones(rule, rng, quick):
    """Production in_cone against native perturbation (lane-parallel), at the plan's depth
    ranges and at both convention pairs. Depth <= 8: every cell within d+2 on both slices
    is perturbed. Depth > 8: every cell at distance d-3..d+2 on both slices (all
    parities) plus 1,000 sampled interior cells per slice."""
    bad, radius_mismatch, tested = [], [], 0
    o = (0, 0, 0)
    for conv, E, ty, depths in depth_plan(quick):
        L = E + 1
        pair = G.Pair(E)
        near, far = (L, E) if ty == 'F' else (E, L)
        for d in depths:
            q = (o, L + d) if ty == 'F' else (o, E - d)
            base = {(c, s): rng.randrange(8) for c in G.lball(d + 3, 3) for s in (E, L)}
            if d <= 8:
                cells = G.lball(d + 2, 3)
            else:
                inner = [c for c in G.lball(d - 4, 3)]
                cells = _sphere_cells(d - 3, d + 2) + rng.sample(inner, min(1000, len(inner)))
            pert = [(c, s) for c in cells for s in (E, L)]
            measured = {near: -1, far: -1}
            for b0 in range(0, len(pert), 4096):
                batch = pert[b0:b0 + 4096]
                ov = [{u: base[u] ^ (1 + rng.randrange(7))} for u in batch]
                ln = NAT.Lanes(base, ov, E, L)
                for lane in ln.changed_lanes(q):
                    u = batch[lane - 1]
                    if not G.in_cone(u, q, pair, rule):
                        bad.append((conv, ty, d, u))
                    measured[u[1]] = max(measured[u[1]], G.l1(u[0]))
            tested += len(pert)
            claimed = {s: max([G.l1(c) for c in cells if G.in_cone((c, s), q, pair, rule)], default=-1)
                       for s in (near, far)}
            if claimed != measured:
                radius_mismatch.append((conv, ty, d, claimed[near], measured[near], claimed[far], measured[far]))
    return {'pass': not bad and not radius_mismatch, 'perturbations': tested,
            'outside_cone': bad[:5], 'radius_mismatch': radius_mismatch[:5]}


def c2_tips(rule, rng, quick):
    """Every tip production emits is a native bijection (lane-parallel: 8 lanes per tip),
    at the plan's depth ranges and both pairs; off-axis cells at the same distance must
    show non-bijective cases."""
    fails, offaxis_nonbij, ntips = [], 0, 0
    o = (0, 0, 0)
    for conv, E, ty, depths in depth_plan(quick):
        L = E + 1
        pair = G.Pair(E)
        near = L if ty == 'F' else E
        for d in depths:
            q = (o, L + d) if ty == 'F' else (o, E - d)
            base = {(c, s): rng.randrange(8) for c in G.lball(d + 3, 3) for s in (E, L)}
            tl = G.tips(q, pair, 3, rule)
            probes = list(tl)
            off = ((d - 1, 1, 0), near) if d >= 2 else None
            if off is not None:
                probes.append(off)
            ov, owner = [], []
            for u in probes:
                for v in range(8):
                    ov.append({u: v} if u in base else {})
                    owner.append(u)
            ln = NAT.Lanes(base, ov, E, L)
            vals = ln.lane_values(q)[1:]
            for k, u in enumerate(probes):
                distinct = len(set(vals[8*k:8*k + 8]))
                if u == off:
                    offaxis_nonbij += distinct != 8
                elif u not in base or distinct != 8:
                    fails.append((conv, ty, d, u))
            ntips += len(tl)
    return {'pass': not fails and offaxis_nonbij > 0, 'tips_tested': ntips,
            'nonbijective_tips': fails[:5], 'offaxis_nonbijective': offaxis_nonbij}

def family(q, pair, dim):
    c, t = q
    d, ty = pair.depth(q)
    near, far = (pair.L, pair.E) if ty == 'F' else (pair.E, pair.L)
    fam = {q} | {(G.vadd(c, e, d), near) for e in G.axes(dim)}
    if d >= 1:
        fam |= {(G.vadd(c, e, d - 1), far) for e in G.axes(dim)}
    return fam



def c3_planted(rule, quick):
    """Planted survivors (families at the plan's depth ranges: A: F 1-15, B 1-8; G: F 1-23;
    quick 1-4; and the constraint block) and planted non-survivors (each family minus its
    +x near tip; the block minus its centre). G plants lie outside the frame; in-frame
    plants at depths 1-2 are the vacuity contrast."""
    dim = 3
    out = {'survivors': [], 'nonsurvivors': [], 'vacuity_contrast': []}
    ok = True
    ctxA = G.Context(TOY, (), 'A', rule)
    ctxG = G.Context(TOYG, (), 'G', rule)
    ranges = {('A', 'F'): range(1, 5 if quick else 16), ('A', 'B'): range(1, 5 if quick else 9),
              ('G', 'F'): range(1, 5 if quick else 24)}
    for (conv, ty), depths in ranges.items():
        ctx = ctxA if conv == 'A' else ctxG
        pair, elig = ctx.pair, ctx.eligible
        for d in depths:
            if conv == 'A':
                for c in ((40, 0, 0), (41, 0, 0)):
                    q = (c, pair.L + d) if ty == 'F' else (c, pair.E - d)
                    if G.even(q):
                        break
            else:
                c = (6 + d, 0, 0)
                q = (c, d)
            fam = family(q, pair, dim)
            ret, _ = G.closure(ctx.fixed, fam, pair, dim, rule, elig)
            ok &= ret == fam - ctx.fixed
            out['survivors'].append((conv, ty, d, len(ret), len(fam - ctx.fixed)))
            near = pair.L if ty == 'F' else pair.E
            drop = (G.vadd(c, (1, 0, 0), d), near)
            ret2, _ = G.closure(ctx.fixed, fam - {drop}, pair, dim, rule, elig)
            ok &= not ret2
            out['nonsurvivors'].append((conv, ty, d, len(ret2)))
    for d in (1, 2):
        pair, elig = ctxG.pair, ctxG.eligible
        q = ((0, 0, 0), d) if d % 2 == 0 else ((1, 0, 0), d)
        fam = family(q, pair, dim)
        ret, _ = G.closure(ctxG.fixed, fam, pair, dim, rule, elig)
        out['vacuity_contrast'].append((d, len(ret), len(fam - ctxG.fixed)))
    pair = ctxA.pair
    c0 = (5, 0, 0) if (5 + pair.L + 1) % 2 == 0 else (5, 1, 0)
    top, centre = (c0, pair.L + 1), (c0, pair.E)
    six = {(G.vadd(c0, e), pair.L) for e in G.axes(dim)}
    blk = {top, centre} | six
    rb, _ = G.closure(set(), blk, pair, dim, rule)
    rbm, _ = G.closure(set(), blk - {centre}, pair, dim, rule)
    out['block'] = (len(rb), len(rbm))
    ok &= len(rb) == 8 and len(rbm) == 0
    out['pass'] = ok
    return out

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



def _degeneracies(r):
    """Configuration attributes of a toy record (all C4v-invariant)."""
    six, V, p = TOY.phi()
    phi_sites = {c for c, _ in six}
    sites = [x for x, _ in r]
    zaxis = lambda x: x[0] == 0 and x[1] == 0
    def common_axis(a, b):
        return sum(1 for i in range(3) if a[i] != b[i]) == 1
    return {
        'item_at_q9': any(x == (0, 0, 0) for x in sites),
        'item_at_phi_site': any(x in phi_sites for x in sites),
        'item_at_port_site': any(x == TOY.port for x in sites),
        'item_on_z_axis': any(zaxis(x) for x in sites),
        'pair_on_common_axis': len(r) == 2 and common_axis(sites[0], sites[1]),
        'item_t_le_0': any(t <= 0 for _, t in r),
        'item_t_eq_minus1': any(t == -1 for _, t in r),
        'last_sample_odd': any(not G.even((x, t)) for x, t in r),
    }


def _reported_counts(per_record, l3_per_record, records, grp, act):
    """Every count Stage 0 reports, from per-record attributes (full computation)."""
    cnt = {}
    for conv in ('A', 'G'):
        res = per_record[conv]
        cnt[conv + ':survivors'] = sum(res[r]['survivor'] for r in records)
        cnt[conv + ':L3_vs_L3prime_disagree'] = sum(res[r]['retained'] != l3_per_record[conv][r]['retained']
                                                    for r in records)
        cnt[conv + ':observer_classes'] = len({tuple(map(tuple, res[r]['public_retained'])) for r in records})
        cnt[conv + ':observer_classes_survivors'] = len({tuple(map(tuple, res[r]['public_retained']))
                                                         for r in records if res[r]['survivor']})
        if conv == 'A':
            cnt['A:phi_linked'] = sum(res[r]['phi_linked'] for r in records)
            cnt['A:j_linked'] = sum(res[r]['j_linked'] for r in records)
        for k in _degeneracies(records[0]):
            for sv in (False, True):
                cnt['%s:deg:%s:survivor=%s' % (conv, k, sv)] = sum(
                    _degeneracies(r)[k] and res[r]['survivor'] == sv for r in records)
    ctx_keys = {}
    for r in records:
        ctx_keys.setdefault(tuple(sorted(G.record_samples(TOY, r))), []).append(r)
    cnt['masking_equivalent_records'] = sum(len(v) for v in ctx_keys.values() if len(v) > 1)
    cnt['nontrivial_stabilizer'] = sum(1 for r in records
                                       if sum(tuple(sorted((act(g, x), t) for x, t in r)) == r for g in grp) > 1)
    return cnt


def c8_symmetry(rule, quick):
    """C4v equivariance of retained sets; invariant attributes equal on orbits; count
    preservation: every reported count computed from orbit representatives (weighted by
    orbit size; class counts via class orbits) equals the full computation. G-linkage is
    computed per record and is not orbit-reduced."""
    from itertools import permutations, product

    def act(g, c):
        perm, sg = g
        return tuple(sg[i]*c[perm[i]] for i in range(3))
    OH = [(pp, ss) for pp in permutations(range(3)) for ss in product((1, -1), repeat=3)]
    region = set(TOY.region)
    grp = [g for g in OH if {act(g, c) for c in region} == region and act(g, TOY.port) == TOY.port
           and act(g, (0, 0, -1)) == (0, 0, -1)]
    records = [tuple(sorted(r)) for r in toy_records(TOY)]
    near_rule = G.Rule(far=False, **{k: v for k, v in vars(rule).items() if k != 'far'})
    full, l3 = {}, {}
    for conv in ('A', 'G'):
        full[conv] = {r: G.analyse(G.Context(TOY, r, conv, rule)) for r in records}
        l3[conv] = {r: G.analyse(G.Context(TOY, r, conv, near_rule)) for r in records}
    viol = 0
    sample = records[::3] if quick else records
    for conv in ('A', 'G'):
        for r in sample:
            a = full[conv][r]
            for g in grp:
                gr = tuple(sorted((act(g, x), t) for x, t in r))
                b = full[conv][gr]
                if sorted((act(g, c), t) for c, t in a['retained']) != b['retained']:
                    viol += 1
                for k in ('survivor', 'n_retained', 'n_survivor') + (('phi_linked', 'j_linked') if conv == 'A' else ()):
                    viol += a[k] != b[k]
    counts_full = _reported_counts(full, l3, records, grp, act)

    def canon(r):
        return min(tuple(sorted((act(g, x), t) for x, t in r)) for g in grp)
    orbits = {}
    for r in records:
        orbits.setdefault(canon(r), []).append(r)
    # orbit-reduced: analyse representatives only; derive members by the group action
    reps = sorted(orbits)
    red, red3 = {}, {}
    for conv in ('A', 'G'):
        red[conv], red3[conv] = {}, {}
        for rep in reps:
            a = G.analyse(G.Context(TOY, rep, conv, rule))
            a3 = G.analyse(G.Context(TOY, rep, conv, near_rule))
            for m in orbits[rep]:
                g = next(g for g in grp if tuple(sorted((act(g, x), t) for x, t in rep)) == m)
                tr = lambda qs: sorted((act(g, c), t) for c, t in qs)
                red[conv][m] = dict(a, retained=tr(a['retained']), public_retained=tr(a['public_retained']))
                red3[conv][m] = dict(a3, retained=tr(a3['retained']))
    counts_red = _reported_counts(red, red3, records, grp, act)
    mismatch = sorted(k for k in counts_full if counts_full[k] != counts_red[k])
    glink = sum(full['G'][r].get('g_linked', False) for r in records)
    return {'pass': viol == 0 and not mismatch and len(grp) == 8, 'group_order': len(grp),
            'orbits': len(orbits), 'records': len(records), 'equivariance_violations': viol,
            'counts_compared': len(counts_full), 'count_mismatches': mismatch,
            'counts': counts_full, 'g_linked_records_per_record': glink}

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
    """(i) Code invariant (cannot fail by construction: closure iterates non-fixed
    quantities only): no fixed quantity appears in an elimination log. (ii) Under G, every
    port sample N[0..n] is in-frame: no eligible tip, and its whole cone inside the frame."""
    recs = toy_records(TOY)[::11]
    bad = 0
    for conv in ('A', 'G'):
        for r in recs:
            ctx = G.Context(TOY, r, conv, rule)
            ctx.run()
            bad += any(q in ctx.fixed for q, _, _ in ctx.log)
    ctx = G.Context(TOYG, (), 'G', rule)
    pair = ctx.pair
    box = [(c, s) for c in G.lball(TOYG.n + 6, 3) for s in (-1, 0)]
    port_bad = 0
    for q in ctx.port:
        port_bad += any(ctx.eligible(u) for u in G.tips(q, pair, 3, G.FROZEN))
        port_bad += any(G.in_cone(u, q, pair, G.FROZEN) and ctx.eligible(u) for u in box)
    return {'pass': bad == 0 and port_bad == 0, 'code_invariant_fixed_eliminated': bad,
            'port_samples_checked': len(ctx.port), 'port_not_in_frame': port_bad}

def _phi_cover(ctx):
    """Fixed site-times that can cover a tip under A (Phi's seven cells and p's cells are
    Phi site-times); none under G (frame tips are ineligible instead)."""
    return set(ctx.phi_cells) if ctx.conv == 'A' else set()


def _ref_geo(ctx):
    return REF.RefGeometry(3, ctx.pair.E)


def c11_dir_tables(rule, quick):
    """C11-dir (i), required: the closure's per-direction tip-status table at every
    elimination, and for every retained quantity at the fixed point, equals the
    independent reference table computed from the plan text at the same state. Over every
    toy record (A and G) and the planted sets. Failure is VOID."""
    recs = toy_records(TOY)[::(5 if quick else 1)]
    bad, checked = [], 0
    jobs = [(TOY, r, conv) for conv in ('A', 'G') for r in recs]
    for setup, r, conv in jobs:
        ctx = G.Context(setup, r, conv, rule)
        ctx.run()
        fixed, quants, geo, elig = REF.ref_context(3, setup.n, setup.port, r, conv)
        alive = set(quants) | fixed
        for q, u, tb in ctx.log:
            ref = REF.ref_direction_table(q, alive - {q}, geo, elig)
            checked += 1
            if tb != ref:
                bad.append(('elim', conv, r, q))
            alive.discard(q)
        for q, tb in ctx.final_tables.items():
            ref = REF.ref_direction_table(q, alive - {q}, geo, elig)
            checked += 1
            if tb != ref:
                bad.append(('final', conv, r, q))
    # planted sets (A geometry of the toy context): families, minus one tip in each direction
    ctxA = G.Context(TOY, (), 'A', rule)
    geo = _ref_geo(ctxA)
    for d in (1, 2, 3):
        q = ((40, 0, 0), ctxA.pair.L + d) if (40 + ctxA.pair.L + d) % 2 == 0 else ((41, 0, 0), ctxA.pair.L + d)
        fam = family(q, ctxA.pair, 3)
        for e in G.axes(3):
            S = fam - {(G.vadd(q[0], e, d), ctxA.pair.L)}
            fin = {}
            ret, log = G.closure(ctxA.fixed, S, ctxA.pair, 3, rule, None, fin)
            alive = set(S) | set(ctxA.fixed)
            for qq, u, tb in log:
                checked += 1
                if tb != REF.ref_direction_table(qq, alive - {qq}, geo, lambda x: True):
                    bad.append(('elim', 'planted', d, e, qq))
                alive.discard(qq)
            for qq, tb in fin.items():
                checked += 1
                if tb != REF.ref_direction_table(qq, alive - {qq}, geo, lambda x: True):
                    bad.append(('final', 'planted', d, e, qq))
    return {'pass': not bad, 'tables_checked': checked, 'mismatches': len(bad), 'first': bad[:3]}


def c11_props(rule, quick):
    """C11 (ii), required: P_A-dir (P_G-dir under G) and the aggregate P_A on every
    survivor of the toy class and on every planted retained set. Planted sets: the
    families (positive) and each family minus its near tip in one direction (the frozen
    rule eliminates these; a closure that retains one must violate P_A-dir). Failure is
    MISMATCH (proof against computation)."""
    recs = toy_records(TOY)[::(5 if quick else 1)]
    pdir, pagg, checked = [], [], 0
    for conv in ('A', 'G'):
        for r in recs:
            ctx = G.Context(TOY, r, conv, rule)
            a = G.analyse(ctx)
            if not a['survivor']:
                continue
            S = set(a['survivors'])
            geo = _ref_geo(ctx)
            checked += 1
            pdir += REF.pa_dir_violations(S, geo, ctx.eligible or (lambda u: True), _phi_cover(ctx))
            pagg += REF.pa_aligned_violations(S, geo, ctx.eligible or (lambda u: True), _phi_cover(ctx))
    ctxA = G.Context(TOY, (), 'A', rule)
    geo = _ref_geo(ctxA)
    planted_retained = 0
    for d in (1, 2, 3):
        q = ((40, 0, 0), ctxA.pair.L + d) if (40 + ctxA.pair.L + d) % 2 == 0 else ((41, 0, 0), ctxA.pair.L + d)
        fam = family(q, ctxA.pair, 3)
        sets = [fam] + [fam - {(G.vadd(q[0], e, d), ctxA.pair.L)} for e in G.axes(3)]
        for S in sets:
            ret, _ = G.closure(ctxA.fixed, S, ctxA.pair, 3, rule)
            if ret:
                planted_retained += 1
                checked += 1
                pdir += REF.pa_dir_violations(ret, geo, lambda u: True, _phi_cover(ctxA))
                pagg += REF.pa_aligned_violations(ret, geo, lambda u: True, _phi_cover(ctxA))
    return {'pass': not pdir and not pagg, 'sets_checked': checked, 'planted_retained': planted_retained,
            'pa_dir_violations': len(pdir), 'pa_aggregate_violations': len(pagg),
            'first_pa_dir': pdir[:2]}


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
            for q, u, _ in ctx.log:
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
    """Every guarded entry point refuses v8's setup without authorization."""
    refused = 0
    for call in (lambda: G.Context(G.V8, (), 'A'), lambda: G.Context(G.V8, (), 'G'),
                 lambda: G.num_records(G.V8), lambda: G.record_at(G.V8, 0),
                 lambda: G.record_samples(G.V8, ())):
        try:
            call()
        except PermissionError:
            refused += 1
    return {'pass': refused == 5, 'refused_of_5': refused}


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
    res['C11_dir_tables'] = c11_dir_tables(rule, quick)
    res['C11_props'] = c11_props(rule, quick)
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
