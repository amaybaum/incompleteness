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
    # scope changed consistently in the main family and the audit (k range 1..15)
    ('L1_k_range_15_both', [('def family(Bs=(2, 3, 4), kmax=16):', 'def family(Bs=(2, 3, 4), kmax=15):'),
                            ('def independent_audit(fam, encl, Bs=(2, 3, 4), kmax=16):', 'def independent_audit(fam, encl, Bs=(2, 3, 4), kmax=15):')]),
    # member dropped from the main family only
    ('L2_k_range_15_main_only', [('def family(Bs=(2, 3, 4), kmax=16):', 'def family(Bs=(2, 3, 4), kmax=15):')]),
    # two members swapped (relabelled) in the reported family
    ('L3_members_swapped', [('    fam, encl = family()\n', "    fam, encl = family()\n    fam['B3_k5'], fam['B3_k6'] = fam['B3_k6'], fam['B3_k5']\n")]),
    # one member dropped from the reported family after computation
    ('L3b_member_deleted', [('    fam, encl = family()\n', "    fam, encl = family()\n    del fam['B4_k16']\n")]),
    # tenth threshold changed (main computes with it; audit hardcodes 1/10)
    ('L4_tenth_threshold', [('TENTH, HALF = Q(1, 10), Q(1, 2)', 'TENTH, HALF = Q(1, 5), Q(1, 2)')]),
    # B range changed consistently in the main family and the audit (B=2,3 only)
    ('L5_B_range_both', [('def family(Bs=(2, 3, 4), kmax=16):', 'def family(Bs=(2, 3), kmax=16):'),
                         ('def independent_audit(fam, encl, Bs=(2, 3, 4), kmax=16):', 'def independent_audit(fam, encl, Bs=(2, 3), kmax=16):')]),
    # audit restricted to a subset while the main family keeps all members (audit scope narrowed)
    ('L6_audit_subset_only', [('    audit = independent_audit(fam, encl)\n', '    audit = independent_audit(fam, encl, Bs=(2,), kmax=4)\n')]),
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
        open(os.path.join(run, 'out.json'), 'w').write(p.stdout)
        first = p.stdout.splitlines()[0][:110] if p.stdout else ('STDERR:' + p.stderr.strip().splitlines()[-1][:100] if p.stderr else '')
        print(f'{name}: exit {p.returncode}; same_as_result={p.stdout == ref}; {first}', flush=True)


if __name__ == '__main__':
    main()
