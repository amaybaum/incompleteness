"""Reviewer mutants for a2_memory_v8/checks.py (beyond the author's M1-M10).

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
    ('R1_power_rule_exponent', 'n_hp = least_power_below(bh, HALF)', 'n_hp = least_power_below(bh * bh, HALF)'),
    ('R2_run_comparator_shift', 'if first is None and a != QUANTUM ** t:', 'if first is None and a != QUANTUM ** (t + 1):'),
    ('R3_chi_lambda_off', 'lam = QUANTUM * N\n', 'lam = QUANTUM * N + 1\n'),
    ('R4_drop_closedness', 'if all(i in reach[j] for j in reach[i]):', 'if True:'),
    ('R5_K5_vacuous', "if cl['freq'] == QUANTUM:", "if cl['freq'] == QUANTUM + 1:"),
    ('R6_rs_cut', 'cutq = QUANTUM\n', 'cutq = Q(13, 16)\n'),
    ('R7_inflate_c_low', 'c_low, c_up = 1 - bh, 1 - bl', 'c_low, c_up = 2 * (1 - bh), 1 - bl'),
    ('R8_inflate_c_low_x1.2', 'c_low, c_up = 1 - bh, 1 - bl', 'c_low, c_up = Q(6, 5) * (1 - bh), 1 - bl'),
    ('R9_uniform_pi', 'pi = solve(A, b)', 'pi = [Q(1, m)] * m'),
    ('R10_fewer_chains', 'per_state = list(compositions(N, 2 * n))', 'per_state = list(compositions(N, 2 * n))[:-1]'),
    ('R11_K3_wrong_source', "'D': {1: {(0, 0): QUANTUM}, 0: {(0, 0): 1 - QUANTUM}}}",
     "'D': {1: {(0, 0): Q(13, 16)}, 0: {(0, 0): Q(3, 16)}}}"),
    ('R12_power_upper_exponent', 'least_power_below(bl * bl, Q(3, 4)) - 1', 'least_power_below(bl, Q(3, 4)) - 1'),
    ('R13_restart_off_by_one', 'if self.clear and self.j == self.k:', 'if self.clear and self.j == self.k + 1:'),
    ('R14_quantum_3_4', 'QUANTUM = Q(4, 5) ', 'QUANTUM = Q(3, 4) '),
    ('R15_memory_formula', "'memory_bits_upper': (k - 1) * B + (k - 1) + (k - 1).bit_length()",
     "'memory_bits_upper': (k - 1) * B + (k - 1).bit_length()"),
]
TAMPER = [('I1_tampered_v7_input', b'"A_reset_a_read_X":"', b'"A_reset_a_read_X":" ')]


def main():
    src = open(os.path.join(SRC_DIR, 'checks.py')).read()
    ref = open(os.path.join(SRC_DIR, 'result.json')).read()
    v7 = open(os.path.join(SRC_DIR, '..', 'a2_depth_v7', 'result.json'), 'rb').read()
    jobs = [(n, o, nw, None) for n, o, nw in MUT] + [(n, None, None, (o, nw)) for n, o, nw in TAMPER]
    for name, old, new, tam in jobs:
        base = os.path.join(WORK, name)
        os.makedirs(os.path.join(base, 'a2_memory_v8'), exist_ok=True)
        os.makedirs(os.path.join(base, 'a2_depth_v7'), exist_ok=True)
        s = src
        if old is not None:
            assert s.count(old) == 1, name
            s = s.replace(old, new)
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
