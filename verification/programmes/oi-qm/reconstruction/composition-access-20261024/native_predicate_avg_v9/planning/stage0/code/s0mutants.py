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
}
EQUIVALENT = ['parity_dropped(equivalent)', 'symmetric_blind(equivalent)']


def run(rule, full):
    cmd = [sys.executable, '-I', '-B', os.path.join(HERE, 's0controls.py'), '--rule', rule]
    if not full:
        cmd.append('--quick')
    p = subprocess.run(cmd, capture_output=True, text=True)
    res = json.loads(p.stdout)
    return p.returncode, res['failed']


def main():
    full = '--full' in sys.argv[1:]
    out = {'mode': 'full' if full else 'quick', 'mutants': {}, 'equivalent': {}}
    ok = True
    code, failed = run('frozen', full)
    out['frozen'] = {'exit': code, 'failed': failed}
    ok &= code == 0 and not failed
    for m, targets in EXPECT.items():
        code, failed = run(m, full)
        hit = sorted(set(failed) & set(targets))
        caught = code == 2 and bool(hit)
        out['mutants'][m] = {'exit': code, 'failed': failed, 'named_targets': targets,
                             'named_targets_failed': hit, 'caught': caught}
        ok &= caught
    for m in EQUIVALENT:
        code, failed = run(m, full)
        closure_controls = [c for c in failed if c not in ('C1_cones',)]
        out['equivalent'][m] = {'exit': code, 'failed': failed,
                                'closure_level_controls_failed': closure_controls}
    out['pass'] = ok
    print(json.dumps(out, sort_keys=True))
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
