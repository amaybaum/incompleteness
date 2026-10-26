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

W4 = [('n_hp = least_n_above(lambda n: power_rule_lower(bh, n), HALF)', 'n_hp = least_n_above(lambda n: power_rule_lower(bh, n + 1), HALF)'), ('check(power_rule_lower(bh, n_hp) > HALF and (n_hp == 1 or power_rule_lower(bh, n_hp - 1) <= HALF),', 'check(power_rule_lower(bh, n_hp + 1) > HALF and (n_hp == 1 or power_rule_lower(bh, n_hp) <= HALF),')]
MUT = [
    # shared constant: one edit reaches the main depth search and the audit's certificate thresholds
    ('A1_shared_HALF_quarter', [('TENTH, HALF = Q(1, 10), Q(1, 2)', 'TENTH, HALF = Q(1, 10), Q(1, 4)')]),
    # shared helper: digest used by the main block-TV field and by the audit comparison
    ('A2_shared_digest_constant', [("    return hashlib.sha256(f'{x.numerator:x}/{x.denominator:x}'.encode()).hexdigest()",
                                    "    return 'same'")]),
    # shared stdlib helper isqrt (root_lo/root_hi and the audit BC) biased in one place
    ('A3_shared_isqrt_biased', [('from math import comb, isqrt, lcm',
                                 'from math import comb, lcm\nfrom math import isqrt as _isqrt\n\n\ndef isqrt(x):\n    return _isqrt(x) * 99999 // 100000')]),
    # reported depths and the audit's expected depth changed together (one block early)
    ('A4_main_and_audit_one_block_early', W4 + [
        ('n_hp = audit_least(lambda n: 2 * Unum ** n < Dn ** n,', 'n_hp = audit_least(lambda n: 2 * Unum ** (n + 1) < Dn ** (n + 1),')]),
    # reported bound and the audit's restated definition changed together (5% too strong)
    ('A5_main_and_audit_bound_5pct', [
        ('    return 1 - bc ** n\n', '    return 1 - bc ** (n + n // 20)\n'),
        ('n_hp = audit_least(lambda n: 2 * Unum ** n < Dn ** n,', 'n_hp = audit_least(lambda n: 2 * Unum ** (n + n // 20) < Dn ** (n + n // 20),')]),
    # tv_iid, used for the reported crossings and the audit's k=1 certificates, scaled by 0.9
    ('A6_shared_tv_iid_scaled', [('        c = c * (h - i) // (i + 1)\n    return Q(tot, 2 * D ** h)',
                                  '        c = c * (h - i) // (i + 1)\n    return Q(9 * tot, 20 * D ** h)')]),
    # reported enclosure widened upward (conservative-looking), depths built from it
    ('A7_reported_enclosure_widened', [('        hi += root_hi(x)\n', '        hi += root_hi(x) + Q(1, 10 ** 9)\n')]),
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
