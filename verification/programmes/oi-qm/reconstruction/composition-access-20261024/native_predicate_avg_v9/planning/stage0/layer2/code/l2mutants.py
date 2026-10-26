"""NP-AVG-1 Stage 0 Layer 2: the mutant campaign (certificate item 3).

Usage: python3 -I -B l2mutants.py --workdir DIR [--full]
Writes DIR/mutant-campaign.json; exit 0 iff every expectation holds.

Precondition (RC9 c): mutants run only after the unmodified suite has passed. The campaign
reads DIR/preflight.json (structured) and runs only if it passed for the same code_digest;
otherwise it writes pass = false and runs no mutant.

Kill criterion (section 6; A.40): each mutant names its case, a (control, predicate) pair
fixed in CASES below before the run. It is killed only when the run exits 2 with parseable
JSON, the named control is among the failed ones, and the predicate holds on that control's
output.

QUICK (local design evidence): each Layer-1 rule mutant runs s0controls.py --quick --only
<its named control>; the two non-vacuity mutants (blind -y; -y ignores fixed covers) run the
whole quick suite, since their demonstration is that C11 fails and every other control stays
green, with the reported counts equal to the frozen rule's. The Layer-2 machinery mutants run
l2selftest.py --mutant M --only <its named case>. The two equivalent mutants are not run in
QUICK.
FULL (CI only, owner-approved dispatch): every rule mutant runs the full suite, every machinery
mutant runs every self-test case, and the equivalent mutants run as well.
"""
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import l2manifest as MAN   # noqa: E402

C11 = {'C11_dir_tables', 'C11_planted', 'C11_props'}
# The Layer-1 table (STAGE0-PLAN-r5.md section 6), from code-r5 s0mutants.CASES unchanged.
CASES = {
    'near_only': ('C3_planted', 'block minus centre retained', lambda r: r['block'][1] > 0),
    'offaxis_all': ('C2_tips', 'an emitted tip is not bijective', lambda r: len(r['nonbijective_tips']) > 0),
    'offaxis_B': ('C2_tips', 'an emitted B-type tip is not bijective',
                  lambda r: any(t[1] == 'B' for t in r['nonbijective_tips'])),
    'wrong_far': ('C15_exact', 'exactness violation', lambda r: r['1D']['violations_A'] + r['2D']['violations_A'] > 0),
    'far_cone_deleted': ('C1_cones', 'dependence outside the cone', lambda r: len(r['outside_cone']) > 0),
    'radius_minus2': ('C1_cones', 'dependence outside the cone', lambda r: len(r['outside_cone']) > 0),
    'radius_plus2': ('C1_cones', 'claimed radius not attained', lambda r: len(r['radius_mismatch']) > 0),
    'swapped': ('C1_cones', 'cone mismatch', lambda r: len(r['outside_cone']) + len(r['radius_mismatch']) > 0),
    'keep_odd': ('C0_context_sizes', 'context differs from the reference', lambda r: r['mismatches'] > 0),
    'unapplied_elimination': ('C17_fixed_point', 'retained quantity with a free tip',
                              lambda r: r['records_with_unapplied_elimination'] > 0),
    'blind_dir_minus_y': ('C11_dir_tables', 'table mismatch', lambda r: r['table_mismatches'] > 0),
    'ignore_fixed_minus_y': ('C11_planted', 'Phi-adjacent family eliminated', lambda r: r['adjacent_failures'] > 0),
    'decide_blind_minus_y': ('C11_dir_tables', 'decision inconsistent with table',
                             lambda r: r['decision_inconsistent'] > 0),
    'decide_ignore_fixed_minus_y': ('C11_dir_tables', 'decision inconsistent with table',
                                    lambda r: r['decision_inconsistent'] > 0),
    'blind_B_minus_y': ('C11_props', 'P_A-dir violation on a B planted set',
                        lambda r: any(k in ('A_B', 'adjPhi_A_B') for k in r['pa_dir_violation_set_kinds'])),
    'blind_G_minus_y': ('C11_props', 'P_G-dir violation on a G planted set',
                        lambda r: any(k in ('G_F', 'adjFrame_G_F') for k in r['pa_dir_violation_set_kinds'])),
    'decide_frame_ignore_minus_x': ('C11_planted', 'frame-adjacent G family eliminated',
                                    lambda r: 'adjFrame_G_F' in r['failed_set_kinds']),
}
DEMO = ('blind_dir_minus_y', 'ignore_fixed_minus_y')
EQUIVALENT = ['parity_dropped(equivalent)', 'symmetric_blind(equivalent)']


def run(cmd):
    p = subprocess.run(cmd, capture_output=True, text=True)
    try:
        return p.returncode, json.loads(p.stdout)
    except ValueError:
        return p.returncode, None


def main():
    args = sys.argv[1:]
    workdir = args[args.index('--workdir') + 1]
    full = '--full' in args
    py = sys.executable
    ok_man, _, man = MAN.verify(HERE)
    cd = man.get('code_digest') if man else None
    out = {'schema': 'np-avg-1/stage0/layer2/mutant-campaign/1', 'mode': 'full' if full else 'quick',
           'code_digest': cd, 'manifest_ok': ok_man, 'rule_mutants': {}, 'machinery_mutants': {}}
    try:
        with open(os.path.join(workdir, 'preflight.json')) as f:
            pf = json.load(f)
    except (OSError, ValueError):
        pf = None
    clean = bool(pf) and pf.get('pass') is True and pf.get('code_digest') == cd and ok_man
    out['unmodified_suite'] = {'source': 'preflight.json', 'passed': clean,
                               'mode': pf.get('mode') if pf else None}
    if not clean:
        out['pass'] = False
        out['note'] = 'unmodified suite not clean for this code_digest: no mutant run'
        text = json.dumps(out, indent=1, sort_keys=True)
        with open(os.path.join(workdir, 'mutant-campaign.json'), 'w') as f:
            f.write(text + '\n')
        print(text)
        sys.exit(1)
    frozen_counts = pf.get('controls_counts_C8')
    ok = True
    base = [py, '-I', '-B', os.path.join(HERE, 's0controls.py')] + ([] if full else ['--quick'])
    for m, (control, case, pred) in CASES.items():
        demo = m in DEMO
        cmd = base + ['--rule', m] + ([] if (full or demo) else ['--only', control])
        code, res = run(cmd)
        clean_fail = res is not None and code == 2
        try:
            hit = clean_fail and control in res['failed'] and bool(pred(res[control]))
        except (KeyError, TypeError, IndexError):
            hit = False
        entry = {'exit': code, 'failed': res['failed'] if res else 'unparseable',
                 'named_case': '%s: %s' % (control, case), 'killed': hit,
                 'run': 'whole suite' if (full or demo) else 'named control only'}
        if demo:
            others = sorted(set(res['failed']) - C11) if res else ['unparseable']
            same = bool(res) and frozen_counts is not None and res.get('C8_symmetry', {}).get('counts') == frozen_counts
            entry['demo'] = {'fails_C11': bool(res) and bool(set(res['failed']) & C11),
                             'other_controls_failed': others, 'reported_counts_identical_to_frozen': same,
                             'pass': bool(res) and bool(set(res['failed']) & C11) and not others}
            ok &= entry['demo']['pass']
        out['rule_mutants'][m] = entry
        ok &= hit
    import l2selftest as ST
    for m, (_, case, desc) in ST.MUTANTS.items():
        code, res = run([py, '-I', '-B', os.path.join(HERE, 'l2selftest.py'), '--mutant', m] +
                        ([] if full else ['--only', case]))
        hit = res is not None and code == 2 and case in res.get('failed', [])
        out['machinery_mutants'][m] = {'exit': code, 'failed': res['failed'] if res else 'unparseable',
                                       'named_case': '%s: %s' % (case, desc), 'killed': hit,
                                       'run': 'every self-test case' if full else 'named case only'}
        ok &= hit
    if full:
        out['equivalent'] = {}
        for m in EQUIVALENT:
            code, res = run(base + ['--rule', m])
            out['equivalent'][m] = {'exit': code, 'failed': res['failed'] if res else 'unparseable'}
        ok &= out['equivalent']['parity_dropped(equivalent)']['failed'] == [] and \
            out['equivalent']['symmetric_blind(equivalent)']['failed'] == ['C1_cones']
    else:
        out['not_run_in_quick'] = {'equivalent mutants': EQUIVALENT,
                                   'whole-suite runs of the non-demonstration rule mutants': sorted(set(CASES) - set(DEMO)),
                                   'all-case self-test runs of the machinery mutants': sorted(ST.MUTANTS),
                                   'full-depth controls': 'C1 F 0-15/B 0-8/G 0-23, C2, C3 full ranges, C15 full trials',
                                   'status': 'pending: the full campaign runs in CI on owner-approved dispatch'}
    out['killed'] = sum(e['killed'] for e in out['rule_mutants'].values()) + \
        sum(e['killed'] for e in out['machinery_mutants'].values())
    out['total'] = len(out['rule_mutants']) + len(out['machinery_mutants'])
    out['pass'] = bool(ok)
    text = json.dumps(out, indent=1, sort_keys=True)
    with open(os.path.join(workdir, 'mutant-campaign.json'), 'w') as f:
        f.write(text + '\n')
    print(text)
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
