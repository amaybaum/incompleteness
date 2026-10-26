"""NP-AVG-1 Stage 0 Layer 2: the production record driver and per-record analysis (section 5b
items 1-4 and 6), one shard per invocation.

Usage: python3 -I -B l2enum.py --profile toy|v8 --shard s --workdir DIR
                               [--authorization FILE --owner-check FILE]
Reads from DIR: dryrun.json, preflight.json, mutant-campaign.json, s1a.json. Writes
DIR/shard-<s>.json. Before computing anything it runs l2cert.startup (certificate items 1, 2,
3, 6 and the dry-run part of 7); on any failure it prints a VOID object and exits 2.

The shard covers the index range [lo, hi) of the dry run's plan. Each index is mapped by
s0geom.record_at to a record; a record that is not the canonical representative of its C4v
orbit is counted as scanned and skipped; a representative's closures are computed once
(A and G, L3prime and L3) and carried to every orbit member by the group action, and every
attribute of a member is then computed from the member's own record and its carried
retained set (l2analysis.post_closure). Source-dependent attributes are therefore computed
per record. In-run gates (C7, C8, C9, C10 i, C11 i and ii, C17, C18) run on the
representatives and samples the configuration fixes, and on every member of every survivor orbit
(L2-R2), up to the survivor cap, beyond which the run is INCOMPLETE (L2-R3); their tallies are written to the shard
file, and the merge turns them into labels (section 5).
"""
import hashlib
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import s0geom as G        # noqa: E402  production engine
import s0ref as REF       # noqa: E402  independent reference (contexts for the gates)
import l2analysis as AN   # noqa: E402
import l2refcheck as RC   # noqa: E402
import l2config as CFG    # noqa: E402

L3 = G.Rule(far=False)
WITNESS_CAP = 100      # diagnostics only (first gate failures); witnesses keep a running minimum


def sampled(name, idx, rate):
    """Deterministic 1-in-rate sample of representatives by index (configuration salt)."""
    if rate == 1:
        return True
    h = hashlib.sha256(('%s|%s|%d' % (CFG.CONFIG['sampling_salt'], name, idx)).encode()).digest()
    return int.from_bytes(h[:8], 'big') % rate == 0


def iter_indices(lo, hi):
    return range(lo, hi)


def scan(setup, lo, hi, grp, grant):
    """The coverage scan: (scanned, [(index, representative record, orbit)]) over [lo, hi)."""
    scanned, reps = 0, []
    for i in iter_indices(lo, hi):
        r = tuple(sorted(G.record_at(setup, i, grant)))
        scanned += 1
        if AN.canon(r, grp) == r:
            reps.append((i, r, AN.orbit(r, grp)))
    return scanned, reps


def enc(qs):
    return AN.qkey(qs)


def c9_ok(ret, ret3, bound, conv):
    """C9: ret_L3prime within ret_L3, and each within the global bound of its rule."""
    a, b = set(ret), set(ret3)
    return a <= b and a <= bound[(conv, 'L3prime')] and b <= bound[(conv, 'L3')]


def c10i_ok(ctx):
    return not any(q in ctx.fixed for q, _, _ in ctx.log)


def ref_ctx(setup, r, conv, refgrant):
    port = None if setup.port is None else tuple(setup.port)
    fixed, quants, geo, elig = REF.ref_context(setup.dim, setup.n, port, r, conv, refgrant)
    return fixed, quants, RC.CachedGeo(setup.dim, geo.E), elig


def phi_cover(setup, fixed, conv):
    p = (setup.origin, setup.n)
    return {q for q in fixed if q != p} if conv == 'A' else set()


def props_violations(setup, S, conv, r, refgrant):
    if not S:
        return 0
    fixed, _, geo, elig = ref_ctx(setup, r, conv, refgrant)
    vd, va = RC.props(set(S), geo, elig, phi_cover(setup, fixed, conv))
    return len(vd) + len(va)


def direct(setup, m, grant):
    out = {}
    for conv in ('A', 'G'):
        ctx = G.Context(setup, m, conv, G.FROZEN, grant)
        a = G.analyse(ctx)
        ctx3 = G.Context(setup, m, conv, L3, grant)
        a3 = G.analyse(ctx3)
        out[conv] = (ctx, a, ctx3, a3)
    return out


def c16_key(setup, r, grant):
    ctx = G.Context(setup, r, 'A', G.FROZEN, grant)
    return [len(r), len(ctx.quants | ctx.fixed), [[list(x), t] for x, t in sorted(r)]]


def c16_order(key):
    """The C16 order: k, then the number of even-class context quantities, then the sorted items."""
    return (key[0], key[1], tuple((tuple(x), t) for x, t in key[2]))


class Shard:
    def __init__(self, setup, prof, bound, base_ret, grant, refgrant):
        self.setup, self.prof, self.bound, self.base_ret = setup, prof, bound, base_ret
        self.grant, self.refgrant = grant, refgrant
        self.grp = AN.group(setup)
        self.rates = prof['sampling']
        self.c7_scope = prof['C7_scope']
        self.cap = CFG.CONFIG['budget']['survivor_cap_per_shard']
        self.counts = {k: 0 for k in AN.count_keys() if k.split(':')[-1] not in AN.CLASS_KEYS
                       and k != 'masking_equivalent_records'}
        self.classes = {(conv, cat): {} for conv in ('A', 'G') for cat in ('all', 'survivors', 'collapsed')}
        self.base_relative = {'A': 0, 'G': 0}
        self.l3_only = {'A': 0, 'G': 0}
        self.gates = {g: {'checked': 0, 'failed': 0} for g in
                      ('C0_context', 'C7', 'C8', 'C9', 'C10i', 'C11i', 'C11ii', 'C17', 'C18')}
        self.gates['C11i']['tables'] = 0
        self.gates['C7']['shared_tip_reps'] = 0
        self.survivors, self.first_fail = [], []
        self.survivor_reps = 0
        self.survivor_cap_exceeded = False
        self.witness_min, self.witness_seen = None, 0

    def fail(self, gate, idx, extra=None):
        # first failures are diagnostics only; the labels read the 'failed' counts
        self.gates[gate]['failed'] += 1
        if len(self.first_fail) < WITNESS_CAP:
            self.first_fail.append([gate, idx, extra])

    def add_witness(self, cand):
        """L2-R1: a running minimum by the C16 key over every candidate; the count is kept."""
        self.witness_seen += 1
        if self.witness_min is None or c16_order(cand['key']) < c16_order(self.witness_min['key']):
            self.witness_min = cand

    def ref_gates(self, idx, rec, conv, ctx, do7, do11, do17, do18):
        """C0 (context), C7, C11 (i), C17 and C18 on one record, with that record's own reference
        context and the production closure computed for that record."""
        setup = self.setup
        fixed, quants, geo, elig = ref_ctx(setup, rec, conv, self.refgrant)
        self.gates['C0_context']['checked'] += 1
        if ctx.quants != quants or ctx.fixed != fixed:
            self.fail('C0_context', idx, conv)
        if do7:
            self.gates['C7']['checked'] += 1
            same, _ = RC.c7(fixed, quants, ctx.retained, geo, elig, CFG.CONFIG['C7_brute_limit'])
            if not same:
                self.fail('C7', idx, conv)
        if do11:
            n, mism, inc = RC.c11i(fixed, quants, ctx.log, ctx.final_tables, geo, elig)
            self.gates['C11i']['checked'] += 1
            self.gates['C11i']['tables'] += n
            if mism or inc:
                self.fail('C11i', idx, [conv, mism, inc])
        if do17:
            self.gates['C17']['checked'] += 1
            if not RC.c17(ctx.retained, fixed, geo, elig):
                self.fail('C17', idx, conv)
        if do18:
            self.gates['C18']['checked'] += 1
            if not RC.c18(ctx.log, fixed, quants, geo, elig):
                self.fail('C18', idx, conv)

    def member_ref_gates(self, idx, m, d):
        """L2-R2: every gate on one member of a survivor orbit, both conventions."""
        for conv in ('A', 'G'):
            self.ref_gates(idx, m, conv, d[conv][0], True, True, True, True)

    def mismatch_conditions(self, m, d):
        conds = []
        for conv in ('A', 'G'):
            ctx, a, ctx3, a3 = d[conv]
            if not (c10i_ok(ctx) and c10i_ok(ctx3)):
                conds.append('C10i:' + conv)
            if not c9_ok(a['retained'], a3['retained'], self.bound, conv):
                conds.append('C9:' + conv)
            if a['survivor'] and props_violations(self.setup, a['survivors'], conv, m, self.refgrant):
                conds.append('C11ii:' + conv)
        return conds

    def rep(self, idx, r, orb):
        setup, grant = self.setup, self.grant
        reps = direct(setup, r, grant)
        surv_any = reps['A'][1]['survivor'] or reps['G'][1]['survivor']
        gated = surv_any and self.survivor_reps < self.cap
        if surv_any:
            self.survivor_reps += 1
            if not gated:
                self.survivor_cap_exceeded = True
        mismatch_here = False
        # C10 (i): code invariant; a failure is the MISMATCH 'a fixed quantity is eliminated'
        for conv in ('A', 'G'):
            for c in (reps[conv][0], reps[conv][2]):
                self.gates['C10i']['checked'] += 1
                if not c10i_ok(c):
                    self.fail('C10i', idx, conv)
                    mismatch_here = True
        # members: carry the closures, compute every attribute per member
        member_views = {}
        for m, g in sorted(orb.items()):
            view = {}
            for conv in ('A', 'G'):
                ctx, a, ctx3, a3 = reps[conv]
                ctx_m = G.Context(setup, m, conv, G.FROZEN, grant)
                am = AN.post_closure(ctx_m, AN.act_set(g, a['retained']))
                a3m = {'retained': AN.act_set(g, a3['retained']), 'survivor_L3': None}
                ctx3_m = G.Context(setup, m, conv, L3, grant)
                a3m['survivor_L3'] = AN.post_closure(ctx3_m, a3m['retained'])['survivor']
                view[conv] = (ctx_m, am, a3m)
                self.gates['C9']['checked'] += 1
                if not c9_ok(am['retained'], a3m['retained'], self.bound, conv):
                    self.fail('C9', idx, [conv, [[list(x), t] for x, t in m]])
                    mismatch_here = True
                if am['survivor']:
                    self.gates['C11ii']['checked'] += 1
                    if props_violations(setup, am['survivors'], conv, m, self.refgrant):
                        self.fail('C11ii', idx, [conv, [[list(x), t] for x, t in m]])
                        mismatch_here = True
                if set(am['retained']) - self.base_ret[conv]:
                    self.base_relative[conv] += 1
                if a3m['survivor_L3'] and not am['survivor']:
                    self.l3_only[conv] += 1
            contrib = AN.member_contributions(setup, m, view['A'][1], view['G'][1], view['A'][2], view['G'][2])
            for k, v in contrib.items():
                self.counts[k] += v
            member_views[m] = (view, contrib)
        if len(self.grp) // len(orb) > 1:
            self.counts['nontrivial_stabilizer'] += len(orb)
        # observer classes: the canonical image of the representative's public set and its orbit size
        for conv in ('A', 'G'):
            a = reps[conv][1]
            key, osz = AN.canon_set(a['public_retained'], self.grp)
            k = tuple(enc(key))
            cat = 'survivors' if a['survivor'] else 'collapsed'
            self.classes[(conv, 'all')][k] = osz
            self.classes[(conv, cat)][k] = osz
        # reference gates on the representative: shared tip (scope), samples (non-survivor orbits)
        for conv in ('A', 'G'):
            ctx = reps[conv][0]
            shared = AN.shared_near_tip(ctx.quants, ctx.pair, setup.dim)
            if shared:
                self.gates['C7']['shared_tip_reps'] += 1
            if surv_any:
                continue        # survivor orbits: every member below (L2-R2)
            do7 = (shared and self.c7_scope == 'initial_context') or sampled('C7', idx, self.rates['C7'])
            do11 = sampled('C11i', idx, self.rates['C11i'])
            do17 = sampled('C17', idx, self.rates['C17'])
            do18 = sampled('C18', idx, self.rates['C18'])
            if do7 or do11 or do17 or do18:
                self.ref_gates(idx, r, conv, ctx, do7, do11, do17, do18)
        # direct closure of every member on survivor, mismatch and sampled orbits (C8; L2-R2)
        if gated or mismatch_here or sampled('C8_orbits', idx, self.rates['C8_orbits']):
            self.gates['C8']['checked'] += 1
            bad = 0
            for m, (view, contrib) in sorted(member_views.items()):
                d = reps if m == r else direct(setup, m, grant)
                dA, dG = d['A'][1], d['G'][1]
                c_direct = AN.member_contributions(setup, m, dA, dG, d['A'][3], d['G'][3])
                bad += c_direct != contrib
                for conv in ('A', 'G'):
                    am, dd = view[conv][1], d[conv][1]
                    keys = ('retained', 'survivor', 'n_retained', 'n_survivor', 'public_retained') + \
                        (('phi_linked', 'j_linked', 'private_phi', 'private_J') if conv == 'A'
                         else ('g_linked', 'source_cells', 'truncated'))
                    bad += any(am[k] != dd[k] for k in keys)
                    bad += view[conv][2]['retained'] != d[conv][3]['retained']
                if gated:
                    self.member_ref_gates(idx, m, d)
                conds = self.mismatch_conditions(m, d)
                if conds:
                    self.add_witness({'key': c16_key(setup, m, grant), 'conditions': conds, 'index': idx})
            if bad:
                self.fail('C8', idx, bad)
        # survivor detail (the classified residue, section 3), up to the survivor cap
        if gated:
            det = {'index': idx, 'record': [[list(x), t] for x, t in r], 'orbit_size': len(orb),
                   'members': [[[list(x), t] for x, t in m] for m in sorted(orb)]}
            for conv in ('A', 'G'):
                ctx, a, ctx3, a3 = reps[conv]
                S = a['survivors']
                e = {'survivor': a['survivor'], 'n_survivor': len(S), 'survivors': enc(S),
                     'retained': enc(a['retained']), 'public_retained': enc(a['public_retained']),
                     'rule_dependence': 'both' if a['survivor'] and a3['survivor'] else
                     ('L3_only' if a3['survivor'] else ('L3prime_only' if a['survivor'] else 'neither')),
                     'shared_aligned_tips': AN.shared_aligned_tips(S, ctx.pair, setup.dim),
                     'cover_components': AN.cover_components(S, ctx.pair, setup.dim, ctx.eligible),
                     'residual_support_bits': AN.residual_support_bits(ctx, S) if S else 0}
                e['exceeds_S_max'] = e['residual_support_bits'] > CFG.CONFIG['S_max_bits']
                if conv == 'A':
                    e.update(phi_linked=a['phi_linked'], j_linked=a['j_linked'], private_phi=enc(a['private_phi']),
                             private_J=enc(a['private_J']))
                else:
                    e['per_member_g_linked'] = [member_views[m][0]['G'][1]['g_linked'] for m in sorted(orb)]
                    e['per_member_source_cells'] = [enc(member_views[m][0]['G'][1]['source_cells']) for m in sorted(orb)]
                det[conv] = e
            self.survivors.append(det)

    def output(self):
        cls = {}
        for (conv, cat), d in sorted(self.classes.items()):
            cls['%s:%s' % (conv, cat)] = [[list(k), v] for k, v in sorted(d.items())]
        return {'counts_additive': self.counts, 'class_keys': cls, 'base_relative_survivor_records': self.base_relative,
                'L3_only_survivor_records': self.l3_only, 'gates': self.gates, 'gate_failures_first': self.first_fail,
                'witness_min': self.witness_min, 'witness_candidates_seen': self.witness_seen,
                'survivor_representatives': self.survivor_reps, 'survivor_cap': self.cap,
                'survivor_cap_exceeded': self.survivor_cap_exceeded, 'survivors': self.survivors}


def load_bound(s1a, setup, grant):
    b = {}
    for key, flat in s1a['bound'].items():
        conv, rule = key.split(':')
        qs = set()
        step = setup.dim + 1
        for i in range(0, len(flat), step):
            qs.add((tuple(flat[i:i + setup.dim]), flat[i + setup.dim]))
        b[(conv, rule)] = qs
    return b


def run_shard(pname, s, workdir, st):
    grant, refgrant, echo = st['grant'], st['refgrant'], st['echo']
    prof = CFG.profile(pname)
    setup = CFG.make_setup(G, pname)
    with open(os.path.join(workdir, 'dryrun.json'), 'rb') as f:
        draw = f.read()
    dry = json.loads(draw)
    with open(os.path.join(workdir, 's1a.json'), 'rb') as f:
        sraw = f.read()
    s1a = json.loads(sraw)
    plan = dry['shards'][s]
    lo, hi = plan['lo'], plan['hi']
    bound = load_bound(s1a, setup, grant)
    base_ret = {conv: set(G.Context(setup, (), conv, G.FROZEN, grant).run()) for conv in ('A', 'G')}
    sh = Shard(setup, prof, bound, base_ret, grant, refgrant)
    scanned, reps = scan(setup, lo, hi, sh.grp, grant)
    for idx, r, orb in reps:
        sh.rep(idx, r, orb)
    import l2manifest as MAN
    ok, _, man = MAN.verify(HERE)
    out = {'schema': 'np-avg-1/stage0/layer2/shard/2', 'profile': pname, 'shard': s, 'shards': len(dry['shards']),
           'range': [lo, hi], 'records': dry['records'], 'scanned': scanned, 'representatives': len(reps),
           'orbit_weight': sum(len(o) for _, _, o in reps), 'group_order': len(sh.grp),
           'code_digest': man.get('code_digest') if man else None, 'config_sha256': CFG.config_sha256(),
           'commit': st['head'], 'tree_clean': st['tree_clean'], 'ci_run': st['ci_run'],
           'dryrun_sha256': hashlib.sha256(draw).hexdigest(), 's1a_sha256': hashlib.sha256(sraw).hexdigest(),
           'authorization': None if echo is None else {'decision': echo['decision'], 'artifact': echo['artifact'],
                                                       'owner_check': echo['owner_check'], 'ci_run': st['ci_run']},
           'base_retained': {conv: enc(sorted(v)) for conv, v in base_ret.items()}}
    out.update(sh.output())
    body = CFG.canonical(out)
    out['sha256'] = hashlib.sha256(body.encode()).hexdigest()
    return out


def main():
    args = sys.argv[1:]
    pname = args[args.index('--profile') + 1]
    s = int(args[args.index('--shard') + 1])
    workdir = args[args.index('--workdir') + 1]
    import l2cert as CERT
    st = CERT.startup(pname, workdir, args)
    out = run_shard(pname, s, workdir, st)
    name = 'shard-%d%s.json' % (s, '.O' if sys.flags.optimize else '')
    with open(os.path.join(workdir, name), 'w') as f:
        f.write(CFG.canonical(out) + '\n')
    print(json.dumps({'shard': s, 'written': 'shard-%d' % s, 'sha256': out['sha256'],
                      'representatives': out['representatives'],
                      'gates_failed': {k: v['failed'] for k, v in out['gates'].items() if v['failed']}}, sort_keys=True))


if __name__ == '__main__':
    main()
