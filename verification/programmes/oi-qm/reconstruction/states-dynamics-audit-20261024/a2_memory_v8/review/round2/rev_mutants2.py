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
    ('D1_power_rule_exponent_consistent', [
        ('n_hp = least_power_below(bh, HALF)', 'n_hp = least_power_below(bh * bh, HALF)'),
        ('check(bh ** n_hp < HALF and (n_hp == 1 or bh ** (n_hp - 1) >= HALF),',
         'check((bh * bh) ** n_hp < HALF and (n_hp == 1 or (bh * bh) ** (n_hp - 1) >= HALF),')]),
    ('D4_nearest_dyadic_wrong_neighbour', [
        ('return lo if abs(lo - QUANTUM) < abs(hi - QUANTUM) else hi', 'return hi if abs(lo - QUANTUM) < abs(hi - QUANTUM) else lo')]),
    ('D5_lists_against_ceiling', [
        ("post['certified_fails_before_nearest_dyadic_reset'] = k * n_hp < cross_near",
         "post['certified_fails_before_nearest_dyadic_reset'] = k * n_hp < cross_mem")]),
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
