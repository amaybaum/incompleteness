"""Reviewer double/report mutants (multi-replacement) for a2_memory_v8/checks.py (beyond the author's M1-M10).

Usage: python3 -I -B rev_mutants.py <tree a2_memory_v8 dir> <work dir>
Each mutant: copy checks.py into <work>/<name>/a2_memory_v8/, copy the pinned v7 result.json to
<work>/<name>/a2_depth_v7/ (optionally tampered), run with -I -B, record exit and first line, and whether
stdout equals result.json.
"""
import os
import shutil
import subprocess
import sys

SRC_DIR, WORK = sys.argv[1], sys.argv[2]

MUT = [
    # W1: wrong BC enclosure (BC scaled down), fed consistently to every depth rule and every check that uses BC
    ('W1a_bc_enclosure_scaled_1e-4', [
        ('        lo += root_lo(x)\n        hi += root_hi(x)\n',
         '        lo += root_lo(x) * Q(9999, 10000)\n        hi += root_hi(x) * Q(9999, 10000)\n')]),
    ('W1b_bc_enclosure_scaled_1e-6', [
        ('        lo += root_lo(x)\n        hi += root_hi(x)\n',
         '        lo += root_lo(x) * Q(999999, 1000000)\n        hi += root_hi(x) * Q(999999, 1000000)\n')]),
    # W2: wrong constant in the preregistered rule (claims T>1/2 once n c > 1/2) together with a bound twice as strong
    ('W2_prereg_constant_and_bound', [
        ('n_half = floor_q(1 / c_low) + 1 ', 'n_half = floor_q(1 / (2 * c_low)) + 1 '),
        ('check(n_half * c_low > 1 and (n_half - 1) * c_low <= 1,', 'check(n_half * 2 * c_low > 1 and (n_half - 1) * 2 * c_low <= 1,'),
        ('    return 1 - bc ** n\n', '    return 1 - bc ** (2 * n)\n')]),
    # W3: bound 5% too strong inside the shared function
    ('W3_bound_5pct_strong', [('    return 1 - bc ** n\n', '    return 1 - bc ** (n + n // 20)\n')]),
    # W4: consistent off-by-one in the depth search and its minimality check (depth one block early)
    ('W4_depth_one_block_early', [
        ('n_hp = least_n_above(lambda n: power_rule_lower(bh, n), HALF)',
         'n_hp = least_n_above(lambda n: power_rule_lower(bh, n + 1), HALF)'),
        ('check(power_rule_lower(bh, n_hp) > HALF and (n_hp == 1 or power_rule_lower(bh, n_hp - 1) <= HALF),',
         'check(power_rule_lower(bh, n_hp + 1) > HALF and (n_hp == 1 or power_rule_lower(bh, n_hp) <= HALF),')]),
    # W5: preregistered constant x1.5 together with a 1.5x-strong bound
    ('W5_prereg_x1.5_and_bound_x1.5', [
        ('n_half = floor_q(1 / c_low) + 1 ', 'n_half = floor_q(2 / (3 * c_low)) + 1 '),
        ('check(n_half * c_low > 1 and (n_half - 1) * c_low <= 1,', 'check(n_half * 3 * c_low > 2 and (n_half - 1) * 3 * c_low <= 2,'),
        ('    return 1 - bc ** n\n', '    return 1 - bc ** (n + n // 2)\n')]),
]
TAMPER = []


def main():
    src = open(os.path.join(SRC_DIR, 'checks.py')).read()
    ref = open(os.path.join(SRC_DIR, 'result.json')).read()
    v7 = open(os.path.join(SRC_DIR, '..', 'a2_depth_v7', 'result.json'), 'rb').read()
    jobs = [(n, reps, None, None) for n, reps in MUT] + [(n, None, None, (o, nw)) for n, o, nw in TAMPER]
    for name, old, new, tam in jobs:
        base = os.path.join(WORK, name)
        os.makedirs(os.path.join(base, 'a2_memory_v8'), exist_ok=True)
        os.makedirs(os.path.join(base, 'a2_depth_v7'), exist_ok=True)
        s = src
        for o_, n_ in (old or []):
            assert s.count(o_) == 1, (name, o_)
            s = s.replace(o_, n_)
        open(os.path.join(base, 'a2_memory_v8', 'checks.py'), 'w').write(s)
        shutil.copy(os.path.join(SRC_DIR, 'PLAN.md'), os.path.join(base, 'a2_memory_v8', 'PLAN.md'))  # author adaptation: PLAN.md is now a pinned input
        data = v7
        if tam:
            assert data.count(tam[0]) == 1, name
            data = data.replace(tam[0], tam[1])
        open(os.path.join(base, 'a2_depth_v7', 'result.json'), 'wb').write(data)
        run = os.path.join(base, 'run')
        os.makedirs(run, exist_ok=True)
        p = subprocess.run([sys.executable, '-I', '-B', os.path.join(base, 'a2_memory_v8', 'checks.py')],
                           capture_output=True, text=True, cwd=run)
        first = p.stdout.splitlines()[0][:110] if p.stdout else ('STDERR:' + p.stderr.strip().splitlines()[-1][:100] if p.stderr else '')
        print(f'{name}: exit {p.returncode}; same_as_result={p.stdout == ref}; {first}', flush=True)


if __name__ == '__main__':
    main()
