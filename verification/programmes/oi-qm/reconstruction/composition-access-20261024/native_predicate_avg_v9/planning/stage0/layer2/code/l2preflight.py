"""NP-AVG-1 Stage 0 Layer 2: pre-flight controls (certificate item 2), in the job and at the
commit of the run.

Usage: python3 -I -B l2preflight.py --profile toy|v8 --workdir DIR [--quick]
                                    [--authorization F --owner-check F]
Writes DIR/preflight.json. Every check is read from an exit status and a JSON object:
- s0controls.py (C0-C3, C6 toy instances, C7-C18, the refusal check, the native self-test;
  full mode for v8; --quick only for the toy design evidence);
- the two direction mutants of C11's non-vacuity (blind -y; -y ignores fixed covers), each
  of which must fail C11 (exit 2, a C11 control failed);
- s0s6.py (S6) and s0symcheck.py (C0's v8 combinatorics; assertion-based, so always run
  without -O);
- l2selftest.py (the Layer-2 machinery controls);
- C12 on the profile's universe: the frame's even part equals V's cone in the pair (-1, 0)
  (B8 for v8: 833 cells), and every quantity of the universe (every even sample of every
  item, and the port samples) with no seed tip has its whole cone inside the frame; and the
  frame computed by l2plan's own cone code (which selects C7's closure-free set 2 and set 3,
  erratum E1 item E1-F3) equals the production frame on the same box (PO-L2-17);
- for v8 only, with the grant: C6's execution-time instances (the base context and the
  single item (q9, 9), against the hand derivations in l2config), C10 (ii) on v8's port
  samples.
Class: a failure of C6's execution-time instances, C9, C10 (ii), C11 (ii) or C12 is MISMATCH;
any other failure is VOID (section 5).
"""
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import s0geom as G        # noqa: E402
import l2config as CFG    # noqa: E402
import l2analysis as AN   # noqa: E402
import l2plan as PLAN     # noqa: E402

MISMATCH_CONTROLS = {'C9_monotone', 'C10_fixed', 'C11_props', 'C12_frame', 'C12_universe', 'C6_execution',
                     'C10ii_v8'}


def run_json(cmd):
    p = subprocess.run(cmd, capture_output=True, text=True)
    try:
        return p.returncode, json.loads(p.stdout)
    except ValueError:
        return p.returncode, None


def c12_universe(setup, grant, prof):
    ctx = G.Context(setup, (), 'G', G.FROZEN, grant)
    pair = ctx.pair
    V = (setup.origin, setup.n + 2)
    R = setup.n + 6
    box = [(c, s) for c in G.lball(R, setup.dim) for s in (-1, 0)]
    ev = [u for u in box if G.even(u)]
    frame = {u for u in ev if not ctx.eligible(u)}
    vcone = {u for u in ev if G.in_cone(u, V, pair)}
    plan_frame = {u for u in box if u in PLAN.Space(prof).frame()}
    prod_frame_all = {u for u in box if not ctx.eligible(u)}
    U = tuple((x, setup.tlast) for x in setup.region)
    uni = (G.record_samples(setup, U, G.FROZEN, grant) | ctx.port) - ctx.fixed
    bad = []
    for q in sorted(uni):
        if any(ctx.eligible(u) for u in G.tips(q, pair, setup.dim)):
            continue
        if any(ctx.eligible(u) for u in AN.cone_cells(q, pair, setup.dim)):
            bad.append(q)
    return {'pass': frame == vcone and not bad and plan_frame == prod_frame_all, 'frame_even_cells': len(frame),
            'V_cone_even_cells': len(vcone), 'l2plan_frame_equals_production_frame': plan_frame == prod_frame_all,
            'frame_cells_in_box': len(prod_frame_all),
            'universe_quantities': len(uni), 'in_frame_quantities_checked': sum(
                1 for q in uni if not any(ctx.eligible(u) for u in G.tips(q, pair, setup.dim))),
            'in_frame_cone_leaves_frame': [[list(c), t] for c, t in bad[:5]]}


def v8_execution(setup, grant):
    exp = CFG.CONFIG['expected']['v8']
    out = {}
    base_col = {}
    for name, rec in (('C6_base', ()), ('C6_q9_9', (((0, 0, 0), 9),))):
        res = {}
        ok = True
        for conv in ('A', 'G'):
            a = G.analyse(G.Context(setup, rec, conv, G.FROZEN, grant))
            got = {'retained': [[list(c), t] for c, t in a['retained']], 'survivor': a['survivor']}
            if conv == 'A' and 'in_clear' in exp[name]['A']:
                got['in_clear'] = [[list(c), t] for c, t in a['in_clear']]
            if conv == 'G' and 'truncated' in exp[name]['G']:
                got['truncated'] = [[list(c), t] for c, t in a['truncated']]
            res[conv] = got
            ok &= got == exp[name][conv]
            if name == 'C6_base':
                base_col[conv] = not a['survivor']
        out[name] = {'pass': ok, 'computed': res, 'expected': exp[name]}
    ctx = G.Context(setup, (), 'G', G.FROZEN, grant)
    pair = ctx.pair
    box = [(c, s) for c in G.lball(setup.n + 6, setup.dim) for s in (-1, 0)]
    bad = 0
    for q in ctx.port:
        bad += any(ctx.eligible(u) for u in G.tips(q, pair, setup.dim, G.FROZEN))
        bad += any(G.in_cone(u, q, pair, G.FROZEN) and ctx.eligible(u) for u in box)
    out['C10ii_v8'] = {'pass': bad == 0 and sorted(t for _, t in ctx.port) == exp['port_even_samples'],
                       'port_samples': sorted(t for _, t in ctx.port), 'not_in_frame': bad}
    return out, base_col


def main():
    args = sys.argv[1:]
    pname = args[args.index('--profile') + 1]
    workdir = args[args.index('--workdir') + 1]
    quick = '--quick' in args
    prof = CFG.profile(pname)
    import l2cert as CERT
    st = CERT.startup(pname, workdir, args, need=('manifest', 'auth'))
    if quick and prof['requires_authorization']:
        CERT.void(2, 'the v8 pre-flight runs the full control suite')
    py = sys.executable
    controls = {}
    q = ['--quick'] if quick else []
    code, res = run_json([py, '-I', '-B', os.path.join(HERE, 's0controls.py')] + q)
    for name, v in sorted((res or {}).items()):
        if isinstance(v, dict) and 'pass' in v:
            controls[name] = {'pass': v['pass'] is True and name not in res.get('failed', [name]),
                              'class': 'MISMATCH' if name in MISMATCH_CONTROLS else 'VOID'}
    controls['s0controls_exit'] = {'pass': code == 0 and res is not None and res.get('failed') == [], 'class': 'VOID',
                                   'exit': code}
    c11 = 'C11_dir_tables,C11_planted,C11_props'
    for m in ('blind_dir_minus_y', 'ignore_fixed_minus_y'):
        code_m, rm = run_json([py, '-I', '-B', os.path.join(HERE, 's0controls.py'), '--rule', m, '--only', c11] + q)
        killed = code_m == 2 and rm is not None and bool(set(rm['failed']) & set(c11.split(',')))
        controls['C11_nonvacuity_' + m] = {'pass': killed, 'class': 'VOID', 'exit': code_m,
                                           'failed': rm['failed'] if rm else 'unparseable'}
    code6, r6 = run_json([py, '-I', '-B', os.path.join(HERE, 's0s6.py')])
    controls['S6'] = {'pass': code6 == 0 and bool(r6) and r6.get('pass') is True, 'class': 'VOID', 'exit': code6}
    p = subprocess.run([py, '-I', '-B', os.path.join(HERE, 's0symcheck.py')], capture_output=True, text=True)
    controls['C0_v8_combinatorics'] = {'pass': p.returncode == 0, 'class': 'VOID', 'exit': p.returncode}
    codes, rs = run_json([py, '-I', '-B', os.path.join(HERE, 'l2selftest.py')])
    controls['L2_selftest'] = {'pass': codes == 0 and bool(rs) and rs.get('pass') is True, 'class': 'VOID',
                               'exit': codes, 'failed': rs.get('failed') if rs else 'unparseable'}
    setup = CFG.make_setup(G, pname)
    c12 = c12_universe(setup, st['grant'], prof)
    controls['C12_universe'] = dict(c12, **{'class': 'MISMATCH'})
    if pname == 'v8':
        ex, base_col = v8_execution(setup, st['grant'])
        controls['C6_execution'] = {'pass': ex['C6_base']['pass'] and ex['C6_q9_9']['pass'], 'class': 'MISMATCH',
                                    'detail': {k: ex[k] for k in ('C6_base', 'C6_q9_9')}}
        controls['C10ii_v8'] = dict(ex['C10ii_v8'], **{'class': 'MISMATCH'})
    else:
        tb = (res or {}).get('C6_hand', {}).get('toy_base_survivor', {})
        base_col = {'A': tb.get('A') is False, 'G': tb.get('G') is False}
    out = {'schema': 'np-avg-1/stage0/layer2/preflight/1', 'profile': pname, 'mode': 'quick' if quick else 'full',
           'code_digest': st['code_digest'], 'config_sha256': CFG.config_sha256(), 'commit': st['head'],
           'tree_clean': st['tree_clean'], 'ci_run': st['ci_run'],
           'authorization': None if st['echo'] is None else {'decision': st['echo']['decision'],
                                                            'artifact': st['echo']['artifact'],
                                                            'owner_check': st['echo']['owner_check']},
           'controls': controls, 'base_collapsed': base_col,
           'controls_counts_C8': (res or {}).get('C8_symmetry', {}).get('counts'),
           's0controls_result': res, 'l2selftest_result': rs, 'S6_result': r6,
           'pass': all(c['pass'] for c in controls.values())}
    with open(os.path.join(workdir, 'preflight.json'), 'w') as f:
        f.write(json.dumps(out, indent=1, sort_keys=True) + '\n')
    print(json.dumps({'pass': out['pass'], 'failed': sorted(k for k, c in controls.items() if not c['pass'])},
                     sort_keys=True))
    sys.exit(0 if out['pass'] else 2)


if __name__ == '__main__':
    main()
