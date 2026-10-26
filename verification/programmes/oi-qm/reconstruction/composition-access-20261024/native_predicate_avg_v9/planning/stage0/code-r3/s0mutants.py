"""NP-AVG-1 Stage 0 mutant campaign (toys only). Runs s0controls.py under each rule
mutant in a fresh interpreter and checks that every non-equivalent mutant fails at
least one of its named controls. Usage: python3 -I -B s0mutants.py [--full]
Prints JSON; exit 0 iff every expectation holds. Standard library."""
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
EXPECT = {
    'near_only': ['C3_planted', 'C7_reference', 'C17_fixed_point'],
    'offaxis_all': ['C2_tips', 'C3_planted', 'C18_audit'],
    'offaxis_B': ['C2_tips', 'C3_planted', 'C18_audit'],
    'wrong_far': ['C2_tips', 'C3_planted', 'C15_exact', 'C18_audit'],
    'far_cone_deleted': ['C1_cones', 'C3_planted'],
    'radius_minus2': ['C1_cones', 'C3_planted'],
    'radius_plus2': ['C1_cones', 'C3_planted', 'C6_hand'],
    'swapped': ['C1_cones', 'C2_tips'],
    'keep_odd': ['C0_context_sizes', 'C18_audit'],
    'unapplied_elimination': ['C17_fixed_point', 'C7_reference', 'C3_planted'],
    'blind_dir_minus_y': ['C11_dir_tables', 'C11_props'],
}
# Non-vacuity demonstration for the required per-direction control (owner, S11): the
# blind-direction mutant must be caught by C11-dir while every aggregate control passes
# and every reported count (C8) equals the frozen rule's.
DEMO = 'blind_dir_minus_y'
DIRECTION_CONTROLS = {'C11_dir_tables', 'C11_props'}
EQUIVALENT = ['parity_dropped(equivalent)', 'symmetric_blind(equivalent)']


def run(rule, full):
    cmd = [sys.executable, '-I', '-B', os.path.join(HERE, 's0controls.py'), '--rule', rule]
    if not full:
        cmd.append('--quick')
    p = subprocess.run(cmd, capture_output=True, text=True)
    res = json.loads(p.stdout)
    return p.returncode, res['failed'], res


def main():
    full = '--full' in sys.argv[1:]
    out = {'mode': 'full' if full else 'quick', 'mutants': {}, 'equivalent': {}}
    ok = True
    code, failed, fres = run('frozen', full)
    out['frozen'] = {'exit': code, 'failed': failed}
    ok &= code == 0 and not failed
    for m, targets in EXPECT.items():
        code, failed, mres = run(m, full)
        if m == DEMO:
            agg_failed = sorted(set(failed) - DIRECTION_CONTROLS)
            same_counts = mres['C8_symmetry']['counts'] == fres['C8_symmetry']['counts']
            props = mres['C11_props']
            demo = {'aggregate_controls_failed': agg_failed, 'reported_counts_identical_to_frozen': same_counts,
                    'C11_dir_tables_mismatches': mres['C11_dir_tables']['mismatches'],
                    'pa_dir_violations': props['pa_dir_violations'],
                    'pa_aggregate_violations': props['pa_aggregate_violations']}
            demo['pass'] = (not agg_failed and same_counts and mres['C11_dir_tables']['mismatches'] > 0
                            and props['pa_dir_violations'] > 0 and props['pa_aggregate_violations'] == 0)
            out['direction_demo'] = demo
            ok &= demo['pass']
        hit = sorted(set(failed) & set(targets))
        caught = code == 2 and bool(hit)
        out['mutants'][m] = {'exit': code, 'failed': failed, 'named_targets': targets,
                             'named_targets_failed': hit, 'caught': caught}
        ok &= caught
    for m in EQUIVALENT:
        code, failed, _ = run(m, full)
        closure_controls = [c for c in failed if c not in ('C1_cones',)]
        out['equivalent'][m] = {'exit': code, 'failed': failed,
                                'closure_level_controls_failed': closure_controls}
    out['pass'] = ok
    print(json.dumps(out, sort_keys=True))
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
