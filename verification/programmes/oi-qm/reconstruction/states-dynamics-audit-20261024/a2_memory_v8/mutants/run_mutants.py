"""Mutants for a2_memory_v8/checks.py: each must fail cleanly on the control it targets.

Standard library only. The unmodified checker runs first and must reproduce result.json byte for byte;
then each mutant is written to a temporary directory (with the checker's own directory substituted for
its location, so the pinned input still resolves) and run with python3 -I -B. A mutant counts as caught
only when it exits 2 and its first output line begins with VOID and the targeted control's label. The report is deterministic.
"""
import os
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
TARGET = os.path.normpath(os.path.join(HERE, '..'))
CHECKS = os.path.join(TARGET, 'checks.py')
RESULT = os.path.join(TARGET, 'result.json')

MUTANTS = [
    ('M1_grid_constant', 'K1 memoryless reproduction',
     'g = Grid(16, 16, 24)', 'g = Grid(16, 17, 24)', 'K1 rebuilt counts equal executed a2 controller'),
    ('M2_cut_rounding', 'K2 retained-seed reproduction',
     'j = -((-x.numerator) // x.denominator)        # ceil', 'j = x.numerator // x.denominator',
     'K2 retained-seed TV equals a2_depth_v7'),
    ('M3_mismatch_range_n1', 'K5 marginal insufficiency / step (4)',
     'RUN_RANGE = None', 'RUN_RANGE = 1', 'step4 dyadic chain without run mismatch'),
    ('M4_base5_to_base4', 'K4 base-5 countercontrol',
     "for D0, D1 in enumerate_chains(n, 5):\n            chains += 1\n            for cl in class_analysis(n, D0, D1, 5):",
     "for D0, D1 in enumerate_chains(n, 4):\n            chains += 1\n            for cl in class_analysis(n, D0, D1, 4):",
     'K4 base-5 countercontrol finds an exact match'),
    ('M5_root_rounding', 'K7 certified enclosures',
     'hi = Q(k, d) if Q(k, d) ** 2 >= x else Q(k + 1, d)', 'hi = Q(k, d)', 'K7 square-root upper enclosure'),
    ('M6_missing_restart', 'K8 restart mechanics',
     'if self.clear and self.j == self.k:', 'if False:', 'K8 state machine equals product of block laws'),
    ('M7_half_depth_off_by_one', 'K7 depth minimality',
     'n_half = floor_q(1 / c_low) + 1', 'n_half = floor_q(1 / c_low) + 2', 'K7 half-depth minimal for its rule'),
    ('M8_wrong_initial_phase', 'K1 generic engine',
     "chain = {'n': 4, 'init': {idx['X', 1]: Q(1)}, 'D': D}", "chain = {'n': 4, 'init': {idx['a', 1]: Q(1)}, 'D': D}",
     'K1 generic engine equals product engine'),
    ('M9_pinned_hash', 'pinned input',
     "V7_RESULT_SHA256 = '2e8988de", "V7_RESULT_SHA256 = '2e8988df", 'K1/K2 pinned a2_depth_v7 result.json hash'),
    ('M10_memoryless_rounding', 'K6 RS(4,1) memoryless identity',
     'p4 = Q(-((-4 * 16) // 5), 16)', 'p4 = Q((4 * 16) // 5, 16)', 'K6 RS(4,1) is the memoryless 4-bit reset'),
    # added after the independent review (its mutants R1, R4, R10, R15)
    ('M11_power_rule_exponent', 'K7 power-rule control',
     'n_hp = least_n_above(lambda n: power_rule_lower(bh, n), HALF)',
     'n_hp = least_n_above(lambda n: power_rule_lower(bh * bh, n), HALF)',
     'K7 power-rule depth is the least n with lower bound above 1/2'),
    ('M12_drop_closedness', 'step-5 class analysis',
     'if all(i in reach[j] for j in reach[i]):', 'if True:', 'step4 nonsingular stationary system'),
    ('M13_fewer_chains', 'census count',
     'per_state = list(compositions(N, 2 * n))', 'per_state = list(compositions(N, 2 * n))[:-1]',
     'census chain count equals C(2^B+2n-1,2n-1)^n'),
    ('M14_memory_formula', 'memory column',
     "'memory_bits_upper': (k - 1) * B + (k - 1) + (k - 1).bit_length()",
     "'memory_bits_upper': (k - 1) * B + (k - 1).bit_length()", 'memory column bounds the persistent-state count'),
    # added after the re-check (its double mutant D1 and report-level mutant D5)
    ('M15_power_rule_exponent_consistent', 'K7 exact power-rule check',
     '    return 1 - bc ** n\n', '    return 1 - bc ** (2 * n)\n', 'K7 exact product TV inside power-rule bracket'),
    ('M16_lists_against_ceiling', 'comparison-flag recomputation',
     "post['certified_fails_before_nearest_dyadic_reset'] = k * n_hp < cross_near",
     "post['certified_fails_before_nearest_dyadic_reset'] = k * n_hp < cross_mem",
     'comparison flags recomputed from stored depths and the nearest-dyadic crossing'),
    # added at the owner's request: further consistent wrong-bound mutants (implementation and its own check changed together)
    ('M17_threshold_consistent', 'exact ceiling-rounded crossing at k=1',
     'n_hp = least_n_above(lambda n: power_rule_lower(bh, n), HALF)\n                check(power_rule_lower(bh, n_hp) > HALF and (n_hp == 1 or power_rule_lower(bh, n_hp - 1) <= HALF),',
     'n_hp = least_n_above(lambda n: power_rule_lower(bh, n), Q(1, 4))\n                check(power_rule_lower(bh, n_hp) > Q(1, 4) and (n_hp == 1 or power_rule_lower(bh, n_hp - 1) <= Q(1, 4)),',
     'K7 power rule brackets the exact ceiling-rounded crossing'),
    ('M18_weaker_bound_consistent', 'preregistered-rule comparison',
     '    return 1 - bc ** n\n', '    return 1 - bc ** ((n + 1) // 2)\n',
     'K7 power-rule depth no later than the preregistered depth'),
    # M15 with independent constraints disabled one at a time: each remaining one must still catch it
    ('M19_consistent_exponent_consistency_only', 'certificate consistency',
     [('    return 1 - bc ** n\n', '    return 1 - bc ** (2 * n)\n'),
      ('check(T >= power_rule_lower(bh, n) and T * T <= 1 - (bl * bl) ** n,', 'check(True,'),
      ("check(T >= power_rule_lower(bh, h), 'K7 exact T(h) >= power-rule lower bound at k=1')", 'pass')],
     None, 'K7 upper and lower half-level certificates consistent'),
    ('M20_consistent_exponent_exact_k1_only', 'K7 exact k=1 check alone',
     [('    return 1 - bc ** n\n', '    return 1 - bc ** (2 * n)\n'),
      ('check(T >= power_rule_lower(bh, n) and T * T <= 1 - (bl * bl) ** n,', 'check(True,'),
      ("check(n_lp < n_hp, 'K7 upper and lower half-level certificates consistent')", 'pass')],
     None, 'K7 exact T(h) >= power-rule lower bound at k=1'),
    # added after re-check 2 (its W1a, W1b, W3, W4): wrong enclosures or depths fed consistently to every rule
    ('M21_bc_enclosure_scaled_1e-4', 'independent BC recomputation',
     [('        lo += root_lo(x)\n        hi += root_hi(x)\n',
       '        lo += root_lo(x) * Q(9999, 10000)\n        hi += root_hi(x) * Q(9999, 10000)\n')],
     None, 'audit independent BC enclosure overlaps the reported enclosure'),
    ('M22_bc_enclosure_scaled_1e-6', 'independent BC recomputation',
     [('        lo += root_lo(x)\n        hi += root_hi(x)\n',
       '        lo += root_lo(x) * Q(999999, 1000000)\n        hi += root_hi(x) * Q(999999, 1000000)\n')],
     None, 'audit independent BC enclosure overlaps the reported enclosure'),
    ('M23_bound_5pct_strong', 'independent depth recomputation',
     [('    return 1 - bc ** n\n', '    return 1 - bc ** (n + n // 20)\n')],
     None, 'audit recomputed depth equals reported (power_rule_T_above_half_for_h_at_least)'),
    ('M24_depth_one_block_early', 'independent depth recomputation',
     [('n_hp = least_n_above(lambda n: power_rule_lower(bh, n), HALF)',
       'n_hp = least_n_above(lambda n: power_rule_lower(bh, n + 1), HALF)'),
      ('check(power_rule_lower(bh, n_hp) > HALF and (n_hp == 1 or power_rule_lower(bh, n_hp - 1) <= HALF),',
       'check(power_rule_lower(bh, n_hp + 1) > HALF and (n_hp == 1 or power_rule_lower(bh, n_hp) <= HALF),')],
     None, 'audit recomputed depth equals reported (power_rule_T_above_half_for_h_at_least)'),
    ('M25_depth_one_block_early_certificates_only', 'certificate-level exact checks alone',
     [('n_hp = least_n_above(lambda n: power_rule_lower(bh, n), HALF)',
       'n_hp = least_n_above(lambda n: power_rule_lower(bh, n + 1), HALF)'),
      ('check(power_rule_lower(bh, n_hp) > HALF and (n_hp == 1 or power_rule_lower(bh, n_hp - 1) <= HALF),',
       'check(power_rule_lower(bh, n_hp + 1) > HALF and (n_hp == 1 or power_rule_lower(bh, n_hp) <= HALF),'),
      ("check(pp[field] == val, 'audit recomputed depth equals reported (' + field + ')')", 'pass')],
     None, 'audit certificate T>1/2 contradicted by exact TV'),
]

LOCATION = 'HERE = os.path.dirname(os.path.abspath(__file__))'


def run(path):
    p = subprocess.run([sys.executable, '-I', '-B', path], capture_output=True, text=True)
    return p.returncode, p.stdout


def main():
    with open(CHECKS) as f:
        src = f.read()
    lines = []
    code, out = run(CHECKS)
    with open(RESULT) as f:
        ref = f.read()
    if code != 0 or out != ref:
        print('VOID: unmodified checker does not reproduce result.json')
        sys.exit(2)
    lines.append('unmodified: exit 0, output equals result.json')
    caught_all = True
    with tempfile.TemporaryDirectory() as tmp:
        for name, control, old, new, label in MUTANTS:
            pairs = old if isinstance(old, list) else [(old, new)]
            mutated = src
            for o, n in pairs:
                if mutated.count(o) != 1 or src.count(LOCATION) != 1:
                    print(f'VOID: mutant {name} does not apply exactly once')
                    sys.exit(2)
                mutated = mutated.replace(o, n)
            mutated = mutated.replace(LOCATION, f'HERE = {TARGET!r}')
            path = os.path.join(tmp, name + '.py')
            with open(path, 'w') as f:
                f.write(mutated)
            code, out = run(path)
            first = out.splitlines()[0] if out else ''
            caught = code == 2 and first.startswith('VOID: ' + label)
            caught_all &= caught
            lines.append(f'{name}: targets {control}; exit {code}; {first[:120]}; '
                         + ('CAUGHT' if caught else 'NOT CAUGHT'))
    lines.append('all mutants caught' if caught_all else 'SOME MUTANT NOT CAUGHT')
    print('\n'.join(lines))
    sys.exit(0 if caught_all else 1)


if __name__ == '__main__':
    main()
