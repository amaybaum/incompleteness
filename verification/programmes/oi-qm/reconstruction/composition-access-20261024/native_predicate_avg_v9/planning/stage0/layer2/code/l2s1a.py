"""NP-AVG-1 Stage 0 Layer 2: the S1a driver (section 5b item 5; section 12).

Usage: python3 -I -B l2s1a.py --profile toy|v8 --workdir DIR [--authorization F --owner-check F]
Writes DIR/s1a.json (DIR/s1a.O.json under -O).

The global closure bound: the closures under A and G, with L3prime and with L3, of the union
of all items' samples. That union is the context of the record {(x, t_last) : x in Reg},
since every item's samples are those of (x, t_last) at slices up to t. The per-line
closures: the same for the items of every axis-parallel line meeting Reg (L3prime;
reported only, N5). L_A and L_G (rule T's inputs) are read from the L3prime bounds; the L3
values are reported beside them.

S1a's own validity, the fields from which the merge derives S1a's diagnostic status sigma
(erratum E1, item E1-T2):
- case 2 (a)-(c): C0 (contexts), C17 and C18 with the reference code on the L3prime and the L3
  bound closures, the L3 ones with near tips only (L2-R8);
- case 2 (d): L_A and L_G recomputed from the L3prime bounds with s0ref's explicit cones and
  tips (l2refcheck.ref_linked_counts) must equal the production values; the L3 values are
  recomputed the same way and a difference is reported only;
- case 3 (a), (b): no fixed quantity in a bound closure's elimination log; ret_L3prime within
  ret_L3 on the bounds.
The file records 'status' as computed here from these fields (VOID before MISMATCH); the merge
re-derives sigma from the fields, adds cases 1 (a)-(c) and 3 (c), evaluates rule T iff sigma = OK,
and never lets sigma override the run's label.
"""
import hashlib
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import s0geom as G        # noqa: E402
import s0ref as REF       # noqa: E402
import l2analysis as AN   # noqa: E402
import l2refcheck as RC   # noqa: E402
import l2config as CFG    # noqa: E402

L3 = G.Rule(far=False)


def lines(setup):
    """Axis-parallel lines meeting Reg: (axis, fixed coordinates) -> sorted sites."""
    out = {}
    for x in setup.region:
        for i in range(setup.dim):
            key = (i, tuple(x[j] for j in range(setup.dim) if j != i))
            out.setdefault(key, []).append(x)
    return {k: sorted(v) for k, v in sorted(out.items())}


def linked_counts(ctx, ret, setup):
    """(L_A or L_G, list) for a retained set: under A, quantities whose cone contains a Phi cell
    (the six slice-(n+1) cells or V's cell); under G, quantities with a seed tip whose cone
    contains a source cell at slice 0."""
    pair = ctx.pair
    if ctx.conv == 'A':
        sel = [q for q in sorted(ret) if any(G.in_cone(c, q, pair, G.FROZEN) for c in sorted(ctx.phi_cells))]
    else:
        src = [(x, 0) for x in setup.sources]
        sel = [q for q in sorted(ret) if any(ctx.eligible(u) for u in G.tips(q, pair, setup.dim, G.FROZEN))
               and any(G.in_cone(c, q, pair, G.FROZEN) for c in src)]
    return len(sel), sel


def run(pname, grant, refgrant):
    setup = CFG.make_setup(G, pname)
    U = tuple((x, setup.tlast) for x in setup.region)
    out = {'schema': 'np-avg-1/stage0/layer2/s1a/2', 'profile': pname, 'bound': {}, 'sizes': {}, 'checks': {}}
    rets, ctxs = {}, {}
    for conv in ('A', 'G'):
        for rname, rule in (('L3prime', G.FROZEN), ('L3', L3)):
            ctx = G.Context(setup, U, conv, rule, grant)
            ret = ctx.run()
            rets[(conv, rname)], ctxs[(conv, rname)] = ret, ctx
            out['bound']['%s:%s' % (conv, rname)] = AN.qkey(ret)
            out['sizes']['%s:%s' % (conv, rname)] = {'context_quantities': len(ctx.quants), 'retained': len(ret),
                                                    'eliminated': len(ctx.log)}
    L = {}
    for conv in ('A', 'G'):
        for rname in ('L3prime', 'L3'):
            n, sel = linked_counts(ctxs[(conv, rname)], rets[(conv, rname)], setup)
            L['%s:%s' % (conv, rname)] = n
            if rname == 'L3prime':
                out['linked_quantities_%s' % conv] = AN.qkey(sel)
    out['L_A'], out['L_G'] = L['A:L3prime'], L['G:L3prime']
    out['L_bound_rule'] = 'L3prime'
    out['L_reported_L3'] = {'L_A': L['A:L3'], 'L_G': L['G:L3']}
    # validity
    mism, void = [], []
    out['fixed_in_log'], out['L3prime_within_L3'] = [], {}
    Lref = {'L3prime': {}, 'L3': {}}
    for conv in ('A', 'G'):
        for rname in ('L3prime', 'L3'):
            if any(q in ctxs[(conv, rname)].fixed for q, _, _ in ctxs[(conv, rname)].log):
                mism.append('C10i:%s:%s' % (conv, rname))
                out['fixed_in_log'].append('%s:%s' % (conv, rname))
        out['L3prime_within_L3'][conv] = rets[(conv, 'L3prime')] <= rets[(conv, 'L3')]
        if not out['L3prime_within_L3'][conv]:
            mism.append('C9:%s:L3prime_not_within_L3' % conv)
        port = None if setup.port is None else tuple(setup.port)
        fixed, quants, geo, elig = REF.ref_context(setup.dim, setup.n, port, U, conv, refgrant)
        # case 2 (d): the reference's Phi cells are its fixed site-times other than p (slice n)
        phi_ref = {q for q in fixed if q[1] != setup.n}
        src_ref = [(tuple(x), 0) for x in setup.sources]
        for rname in ('L3prime', 'L3'):
            Lref[rname]['L_' + conv] = RC.ref_linked_counts(rets[(conv, rname)], phi_ref, src_ref, conv, geo, elig)
        chk = {}
        for rname, near_only in (('L3prime', False), ('L3', True)):
            ctx = ctxs[(conv, rname)]
            c0 = ctx.quants == quants and ctx.fixed == fixed
            b17 = RC.c17_stream(rets[(conv, rname)], fixed, geo, elig, near_only)
            b18 = RC.c18_stream(ctx.log, fixed, quants, geo, elig, near_only)
            chk[rname] = {'C0_context_equal': c0, 'C17_free_tips': b17, 'C18_unjustified': b18}
            if not c0 or b17 or b18:
                void.append('reference:%s:%s' % (conv, rname))
        out['checks'][conv] = chk
    out['L_reference'] = Lref
    if [Lref['L3prime']['L_A'], Lref['L3prime']['L_G']] != [out['L_A'], out['L_G']]:
        void.append('reference_L:L3prime')        # case 2 (d)
    out['L_reference_L3_differs'] = [Lref['L3']['L_A'], Lref['L3']['L_G']] != [L['A:L3'], L['G:L3']]
    out['lines'] = []
    for (axis, rest), sites in lines(setup).items():
        rec = tuple((x, setup.tlast) for x in sites)
        ent = {'axis': axis, 'at': list(rest), 'sites': len(sites)}
        for conv in ('A', 'G'):
            ctx = G.Context(setup, rec, conv, G.FROZEN, grant)
            a = G.analyse(ctx)
            ent[conv] = {'retained': a['n_retained'], 'survivors': a['n_survivor'],
                         'linked': a['phi_linked'] if conv == 'A' else a['g_linked']}
        out['lines'].append(ent)
    out['n_lines'] = len(out['lines'])
    out['status'] = 'VOID' if void else ('MISMATCH' if mism else 'OK')
    out['status_reasons'] = void + mism
    out['config_sha256'] = CFG.config_sha256()
    return out


def main():
    args = sys.argv[1:]
    pname = args[args.index('--profile') + 1]
    workdir = args[args.index('--workdir') + 1]
    import l2cert as CERT
    st = CERT.startup(pname, workdir, args, need=('manifest', 'auth', 'preflight', 'mutants', 'dryrun'))
    out = run(pname, st['grant'], st['refgrant'])
    import l2manifest as MAN
    out['code_digest'] = MAN.load(HERE).get('code_digest')
    out['commit'] = st['head']
    out['tree_clean'] = st['tree_clean']
    out['ci_run'] = st['ci_run']
    out['sha256'] = hashlib.sha256(CFG.canonical(out).encode()).hexdigest()
    name = 's1a%s.json' % ('.O' if sys.flags.optimize else '')
    with open(os.path.join(workdir, name), 'w') as f:
        f.write(CFG.canonical(out) + '\n')
    print(json.dumps({'written': name, 'status': out['status'], 'L_A': out['L_A'], 'L_G': out['L_G'],
                      'n_lines': out['n_lines']}, sort_keys=True))


if __name__ == '__main__':
    main()
