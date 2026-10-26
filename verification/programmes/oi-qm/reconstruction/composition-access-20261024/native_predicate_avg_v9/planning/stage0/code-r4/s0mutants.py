"""NP-AVG-1 Stage 0 mutant campaign (design evidence; toys, planted sets and small windows
only). Usage: python3 -I -B s0mutants.py [--full]

Kill criterion (RC9 c): each mutant names its case, a (control, predicate) pair fixed
before the run. It counts as killed only when that control fails cleanly (the suite exits
2 with parseable JSON) AND the predicate holds on that control's output. Mutants run only
after the unmodified (frozen) suite has passed. Non-vacuity demonstration (RC7): the
single-direction over-retention mutant (blind -y) and the single-direction over-elimination
mutant (-y tips ignore fixed covers) must each fail C11 and leave every other control
green; the demonstration also reports the class's survivor counts and how many reported
counts are identically zero. Prints JSON; exit 0 iff every expectation holds."""
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
C11 = {'C11_dir_tables', 'C11_planted', 'C11_props'}
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
    'blind_B_minus_y': ('C11_props', 'P_A-dir violation on a B planted set', lambda r: r['pa_dir_violations'] > 0),
    'blind_G_minus_y': ('C11_props', 'P_G-dir violation on a G planted set', lambda r: r['pa_dir_violations'] > 0),
}
DEMO = ('blind_dir_minus_y', 'ignore_fixed_minus_y')
EQUIVALENT = ['parity_dropped(equivalent)', 'symmetric_blind(equivalent)']


def run(rule, full):
    cmd = [sys.executable, '-I', '-B', os.path.join(HERE, 's0controls.py'), '--rule', rule]
    if not full:
        cmd.append('--quick')
    p = subprocess.run(cmd, capture_output=True, text=True)
    try:
        res = json.loads(p.stdout)
    except ValueError:
        return p.returncode, None
    return p.returncode, res


def main():
    full = '--full' in sys.argv[1:]
    out = {'mode': 'full' if full else 'quick', 'mutants': {}, 'equivalent': {}}
    code, fres = run('frozen', full)
    out['frozen'] = {'exit': code, 'failed': fres['failed'] if fres else 'unparseable'}
    if code != 0 or not fres or fres['failed']:
        out['pass'] = False
        out['note'] = 'frozen suite not clean: no mutant run'
        print(json.dumps(out, sort_keys=True))
        sys.exit(1)
    ok = True
    counts = fres['C8_symmetry']['counts']
    for m, (control, case, pred) in CASES.items():
        code, res = run(m, full)
        clean = res is not None and code == 2
        hit = clean and control in res['failed'] and bool(pred(res[control]))
        entry = {'exit': code, 'failed': res['failed'] if res else 'unparseable',
                 'named_case': '%s: %s' % (control, case), 'killed': hit}
        if m in DEMO:
            others = sorted(set(res['failed']) - C11) if res else ['unparseable']
            entry['demo'] = {
                'fails_C11': bool(res) and bool(set(res['failed']) & C11),
                'other_controls_failed': others,
                'reported_counts_identical_to_frozen': bool(res) and res['C8_symmetry']['counts'] == counts,
                'pass': bool(res) and bool(set(res['failed']) & C11) and not others}
            ok &= entry['demo']['pass']
        out['mutants'][m] = entry
        ok &= hit
    out['demo_context'] = {
        'toy_survivors': fres['C11_props']['toy_survivors'],
        'reported_counts': len(counts),
        'reported_counts_identically_zero': sum(1 for v in counts.values() if v == 0)}
    for m in EQUIVALENT:
        code, res = run(m, full)
        out['equivalent'][m] = {'exit': code, 'failed': res['failed'] if res else 'unparseable'}
    out['pass'] = ok
    print(json.dumps(out, sort_keys=True))
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
