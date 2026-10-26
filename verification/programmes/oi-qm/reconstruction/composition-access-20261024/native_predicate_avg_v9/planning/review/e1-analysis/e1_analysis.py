"""Reviewer analysis for E1 (C7 set 2, orbit reduction, the G decomposition, count semantics).
TOY PROFILE ONLY (3D, n = 2, ball(1), last slice 6, port (0,0,-2)); nothing touches v8's class.
Usage: python3 -I -B e1_analysis.py <layer2/code>
Prints one JSON object. Deterministic. Standard library, exact integers."""
import hashlib
import json
import sys
from itertools import combinations

sys.path.insert(0, sys.argv[1])
import s0geom as G        # noqa: E402  production
import s0ref as REF       # noqa: E402  reference
import l2analysis as AN   # noqa: E402
import l2config as CFG    # noqa: E402
import l2plan as PLAN     # noqa: E402

setup = CFG.make_setup(G, 'toy')
assert (setup.dim, setup.n, tuple(setup.port)) != (3, 6, (0, 0, -3))
N = G.num_records(setup)
grp = AN.group(setup)
SALT = CFG.CONFIG['sampling_salt']
OUT = {'profile': 'toy', 'records': N, 'group_order': len(grp)}
FAILS = []


def check(name, ok, detail=None):
    OUT.setdefault('checks', {})[name] = {'pass': bool(ok), 'detail': detail}
    if not ok:
        FAILS.append(name)


def sampled(stream, i, rate):
    h = hashlib.sha256(('%s|%s|%d' % (SALT, stream, i)).encode()).digest()
    return int.from_bytes(h[:8], 'big') % rate == 0


recs = [tuple(sorted(G.record_at(setup, i))) for i in range(N)]
index = {r: i for i, r in enumerate(recs)}
canon = {r: AN.canon(r, grp) for r in recs}
orbit_of = {}
for r in recs:
    orbit_of.setdefault(canon[r], []).append(r)
g_to = {}                                   # member -> g with g.rep = member
for rep in orbit_of:
    for m, g in AN.orbit(rep, grp).items():
        g_to[m] = g


def ref_tips(q, geo):
    """{(e, 'near'|'far'): cell} from the plan text."""
    c = q[0]
    _, d, near, far = geo.kind(q)
    out = {}
    for i in range(geo.dim):
        for s in (1, -1):
            e = REF.unit(geo.dim, i, s)
            out[(e, 'near')] = (REF.shift(c, e, d), near)
            if d >= 1:
                out[(e, 'far')] = (REF.shift(c, e, d - 1), far)
    return out


def shared_near(Q, geo, elig=None):
    """E1's definition: q != q' in Q and e with equal e-tips (optionally: the tip eligible)."""
    seen = {}
    for q in sorted(Q):
        for (e, kind), u in ref_tips(q, geo).items():
            if kind != 'near' or (elig is not None and not elig(u)):
                continue
            k = (e, u)
            if k in seen and seen[k] != q:
                return True
            seen.setdefault(k, q)
    return False


# ---------------------------------------------------------------- per record, per convention
data = {}
for conv in ('A', 'G'):
    for r in recs:
        ctx = G.Context(setup, r, conv, G.FROZEN)
        prod = frozenset(ctx.run())
        fixed, quants, geo, elig = REF.ref_context(setup.dim, setup.n, tuple(setup.port), r, conv)
        ref, _ = REF.greatest(fixed, quants, geo, elig, 8)
        Q0 = frozenset(set(quants) - set(fixed))
        seed = {q for q in Q0 if any(elig(u) for u in ref_tips(q, geo).values())}
        inframe = Q0 - seed
        a = G.analyse(G.Context(setup, r, conv, G.FROZEN))
        data[(conv, r)] = dict(prod=prod, ref=frozenset(ref), Q0=Q0, seed=frozenset(seed), inframe=frozenset(inframe),
                               surv=a['survivor'], geo=geo, elig=elig, fixed=frozenset(fixed))

# ---------------------------------------------------------------- (A1) equivariance and carried closures
viol_ref, viol_prod, viol_ver = 0, 0, 0
for conv in ('A', 'G'):
    for r in recs:
        rep, g = canon[r], g_to[r]
        dr, drep = data[(conv, r)], data[(conv, rep)]
        carried_prod = frozenset(AN.act_set(g, drep['prod']))
        carried_ref = frozenset(AN.act_set(g, drep['ref']))
        viol_prod += carried_prod != dr['prod']
        viol_ref += carried_ref != dr['ref']
        viol_ver += (carried_prod == dr['ref']) != (drep['prod'] == drep['ref'])
check('A1.production_equivariant_on_all_toy_records', viol_prod == 0, viol_prod)
check('A1.reference_equivariant_on_all_toy_records', viol_ref == 0, viol_ref)
check('A1.C7_verdict_member_equals_representative', viol_ver == 0, viol_ver)
agree = sum(data[k]['prod'] == data[k]['ref'] for k in data)
check('A1.C7_agrees_on_every_toy_record_both_conventions', agree == 2 * N, agree)

# ---------------------------------------------------------------- (A2) the populations
pop = {}
for conv in ('A', 'G'):
    d = {k[1]: v for k, v in data.items() if k[0] == conv}
    S = {r for r in recs if d[r]['surv']}
    T = {r for r in recs if shared_near(d[r]['prod'], d[r]['geo'])}
    Te = {r for r in recs if shared_near(d[r]['prod'], d[r]['geo'], d[r]['elig'])}
    I = {r for r in recs if shared_near(d[r]['Q0'], d[r]['geo'])}
    F = {r for r in recs if shared_near(d[r]['inframe'], d[r]['geo'])}       # closure-free
    H100 = {r for r in recs if sampled('C7_H100', index[r], 100)}
    H1000 = {r for r in recs if sampled('C7_H1000', index[r], 1000)}
    pop[conv] = dict(S=S, T=T, Te=Te, I=I, F=F, H100=H100, H1000=H1000)
    inv = {name: all(all(m in X for m in orbit_of[canon[r]]) for r in X) for name, X in
           (('Surv', S), ('T', T), ('T_eligible', Te), ('I', I), ('F', F))}
    check('A2.%s.sets_are_unions_of_orbits' % conv, all(inv.values()), inv)
    check('A2.%s.T_subset_I' % conv, T <= I)
    check('A2.%s.T_eligible_subset_Surv' % conv, Te <= S, len(Te - S))
    if conv == 'A':
        check('A2.A.T_subset_Surv', T <= S, len(T - S))
    else:
        check('A2.G.T_equals_(T_and_Surv)_union_F', T == ((T & S) | F), [len(T), len((T & S) | F)])
    reps_T = {canon[r] for r in T}
    OUT.setdefault('populations', {})[conv] = {
        'Surv': len(S), 'T (set 2, any tip)': len(T), 'T eligible tips only': len(Te),
        'I (initial-context tie)': len(I), 'F (in-frame tie, closure-free)': len(F),
        'T minus Surv': len(T - S), 'I minus (Surv or T)': len(I - S - T),
        'I_and_H100 (records)': len(I & H100), 'H1000 (records)': len(H1000),
        'set 2 orbits (representatives)': len(reps_T), 'set 2 records = sum of orbit sizes':
            sum(len(orbit_of[q]) for q in reps_T),
        'sampled sets: orbits touched': {'I_and_H100': len({canon[r] for r in I & H100}),
                                         'H1000': len({canon[r] for r in H1000})}}

# ---------------------------------------------------------------- (A3) the G decomposition (structural)
dec_bad, inert_bad, fixed_inert_bad = 0, 0, 0
for r in recs:
    d = data[('G', r)]
    geo, elig = d['geo'], d['elig']
    # every in-frame quantity is retained; the seed part's closure ignores the in-frame and fixed quantities
    out_ref, _ = REF.greatest(set(), d['seed'], geo, elig, 8)
    dec_bad += d['prod'] != (d['inframe'] | frozenset(out_ref))
    for q in d['inframe']:
        inert_bad += any(elig(u) for u in geo.cone(q))
    for f in d['fixed']:
        fixed_inert_bad += any(elig(u) for u in geo.cone(f))
check('A3.G_closure_equals_inframe_union_GSS_of_seed_part_without_fixed', dec_bad == 0, dec_bad)
check('A3.G_inframe_cones_contain_no_eligible_cell', inert_bad == 0, inert_bad)
check('A3.G_fixed_cones_contain_no_eligible_cell', fixed_inert_bad == 0, fixed_inert_bad)

# ---------------------------------------------------------------- (A4) planted faults and what detects them
RATE = {'C11i': 1000, 'C17': 1000, 'C18': 1000, 'C7_H1000': 1000, 'C8': 100}


def fault_F1(conv, r, prod):
    """Equivariant fault: drop every retained in-frame quantity whose near tip is shared with
    another retained quantity (in the same direction). Over-elimination of in-frame ties."""
    d = data[(conv, r)]
    geo = d['geo']
    drop = set()
    tips = {}
    for q in prod:
        for (e, k), u in ref_tips(q, geo).items():
            if k == 'near':
                tips.setdefault((e, u), set()).add(q)
    for qs in tips.values():
        if len(qs) > 1:
            drop |= {q for q in qs if q in d['inframe']}
    return frozenset(prod - drop)


def fault_F2(conv, r, prod):
    """Non-equivariant, member-only fault: F1, but only on records that are not their orbit's
    canonical representative."""
    return prod if canon[r] == r else fault_F1(conv, r, prod)


det = {}
for fname, fault in (('F1_equivariant_inframe_tie_drop', fault_F1), ('F2_member_only', fault_F2)):
    for conv in ('G',):
        d = {r: data[(conv, r)] for r in recs}
        direct = {r: fault(conv, r, d[r]['prod']) for r in recs}
        # reported (orbit-reduced): carried from the representative's directly computed (faulty) closure
        reported = {r: frozenset(AN.act_set(g_to[r], direct[canon[r]])) for r in recs}
        wrong_reported = {r for r in recs if reported[r] != d[r]['ref']}
        wrong_direct = {r for r in recs if direct[r] != d[r]['ref']}
        T_comp_reported = {r for r in recs if shared_near(reported[r], d[r]['geo'])}
        S = pop[conv]['S']
        F = pop[conv]['F']
        rep_idx = {r: index[canon[r]] for r in recs}

        def sampled_rep(stream, rate):
            return {r for r in recs if sampled(stream, rep_idx[r], rate)}
        runs = {
            'set1_Surv (computed)': {r for r in recs if r in S},
            'set2_T computed closure, orbit-reduced (E1 as drafted)': T_comp_reported,
            'set2_F_union_TS closure-free, direct per member (recommended)': F | (T_comp_reported & S),
            'set3_I_and_H100 (record index)': pop[conv]['I'] & pop[conv]['H100'],
            'set4_H1000 (record index)': pop[conv]['H1000'],
            'C11i/C17/C18 1-in-1000 (rep index)': sampled_rep('C11i', 1000) | sampled_rep('C17', 1000) |
                                                   sampled_rep('C18', 1000),
            'C8 1-in-100 orbits (direct member recomputation)': sampled_rep('C8_orbits', 100),
        }
        res = {'records_with_wrong_reported_result': len(wrong_reported),
               'records_with_wrong_direct_result': len(wrong_direct), 'detected_by': {}}
        for name, X in runs.items():
            if name.startswith('C8'):
                target = {r for r in recs if reported[r] != direct[r]}   # C8 compares carried with direct
            elif 'direct per member' in name:
                target = wrong_direct           # these compute the member directly
            else:
                target = wrong_reported         # these check the reported (carried) result
            res['detected_by'][name] = len(X & target)
        det[fname] = res
OUT['planted_faults_G'] = det
check('A4.F1_escapes_set2_as_drafted', det['F1_equivariant_inframe_tie_drop']['detected_by'][
    'set2_T computed closure, orbit-reduced (E1 as drafted)'] == 0,
    'a fault that destroys the tie removes the record from its own check')
check('A4.F1_caught_by_closure_free_set2_on_every_affected_record',
      det['F1_equivariant_inframe_tie_drop']['detected_by']['set2_F_union_TS closure-free, direct per member (recommended)']
      == det['F1_equivariant_inframe_tie_drop']['records_with_wrong_direct_result'])
check('A4.F2_invisible_in_reported_results', det['F2_member_only']['records_with_wrong_reported_result'] == 0)
check('A4.F2_caught_only_by_direct_member_computation',
      det['F2_member_only']['detected_by']['set2_F_union_TS closure-free, direct per member (recommended)'] ==
      det['F2_member_only']['records_with_wrong_direct_result'] > 0)

# ---------------------------------------------------------------- (B) count semantics
ctxkey = {}
for r in recs:
    c = G.Context(setup, r, 'A', G.FROZEN)
    ctxkey.setdefault(frozenset(c.quants | c.fixed), []).append(r)
ME = {r for v in ctxkey.values() if len(v) > 1 for r in v}
ST = {r for r in recs if AN.stabilizer_order(r, grp) > 1}
plain_me = len(ME)
plain_st = sum(1 for r in recs if len(orbit_of[canon[r]]) < len(grp))
check('B.masking_equivalent_brute_force_equals_toy_run', plain_me == 1398, plain_me)
check('B.nontrivial_stabilizer_two_definitions_agree', len(ST) == plain_st == 1176, [len(ST), plain_st])
inv_me = all(all(m in ME for m in orbit_of[canon[r]]) for r in ME)
inv_st = all(all(m in ST for m in orbit_of[canon[r]]) for r in ST)
check('B.both_predicates_C4v_invariant', inv_me and inv_st)
# constancy of survivor status on masking-equivalence classes
const = all(len({data[(conv, r)]['surv'] for r in v}) == 1 for v in ctxkey.values() for conv in ('A', 'G'))
check('B.survivor_status_constant_on_masking_classes', const)
tables = {}
for conv in ('A', 'G'):
    S = pop[conv]['S']
    for name, X in (('masking_equivalent', ME), ('nontrivial_stabilizer', ST)):
        cells = {'survivor=True': len(X & S), 'survivor=False': len(X - S), 'marginal (plain count)': len(X)}
        tables['%s:%s' % (conv, name)] = cells
        check('B.%s.%s.marginal_identity' % (conv, name),
              cells['survivor=True'] + cells['survivor=False'] == cells['marginal (plain count)'])
OUT['count_tables_toy'] = tables
# rank: the information content of 58 / 60 / 62 is the same (linear span)
OUT['count_rank_argument'] = ('per degeneracy D and convention c: cells n(D,c,T), n(D,c,F); marginal n(D). '
                              'Identities n(D,c,T)+n(D,c,F)=n(D) for c=A,G. 54+4 (58) lists n(D), n(D,A,T), '
                              'n(D,G,T): 3 numbers, rank 3. 62 adds n(D,A,F), n(D,G,F): 5 numbers, rank 3. '
                              '60 lists the 4 cells: rank 3.')
OUT['pass'] = not FAILS
OUT['failed'] = FAILS
print(json.dumps(OUT, indent=1, sort_keys=True, default=list))
sys.exit(0 if not FAILS else 2)
