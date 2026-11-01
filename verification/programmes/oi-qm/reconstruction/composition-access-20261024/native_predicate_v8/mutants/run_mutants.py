#!/usr/bin/env python3
"""Textual mutants of ../checks.py: each must fail in the way it targets.

Usage: python3 -I -B run_mutants.py <checks.py> <empty work directory>

The work directory may be relative; it is made absolute before use. The
script exits 1 unless every mutant is caught.

Each mutant replaces one exact text, which must occur once, writes the mutant
checker into the work directory, runs it with python3 -I -B from there, and
records the exit status, verdict and failing control. A control mutant is
caught only if it exits 2 with verdict VOID naming its target control; the
injection mutant is caught only if the verdict becomes HOLDS_WITHIN_SCOPE.
"""
import json
import os
import subprocess
import sys

MUTANTS = [
    ('m1_scalar_H_or', 'x1_scalar_evaluator_agrees',
     "        return (b << 2) | (d << 1) | (a ^ (b & d))",
     "        return (b << 2) | (d << 1) | (a ^ (b | d))"),
    ('m2_inverse_offset', 'x2_seven_site_inverse',
     "self.V[l] ^ H[q8[l] ^ q10[l] ^ mm[l] ^ cx] == self.p",
     "self.V[l] ^ H[q8[l] ^ q10[l] ^ mm[l] ^ cx ^ 1] == self.p"),
    ('m3_law_rejects_all', 'x3_planted_positive_found',
     "        if len(blocks) != 2:\n            return None",
     "        if len(blocks) != 2 or True:\n            return None"),
    ('m4a_direct_statistic_accepts_all', 'x4_planted_negatives_rejected_and_encodings_accepted',
     "    return tot > 0 and all(c*tt == t*tot for c, t in zip(counts, target))",
     "    return tot > 0"),
    # Shared by the search and x4: the search space then exceeds its cap,
    # and the run is void before x4 is reached.
    ('m4b_law_accepts_any_two_blocks', 'search_decided_family|x4',
     "        if c0 == self.t1 and c1 == self.t0:\n            return 0",
     "        if True:\n            return 0"),
    # Post-review (reviewer's R7): the law statistic checks block sizes only;
    # the permuted-threshold plant also splits 20/44 and must be rejected by x4.
    ('m4c_law_checks_block_sizes_only', 'x4_planted_negatives_rejected_and_encodings_accepted',
     "        if c0 == self.t1 and c1 == self.t0:\n            return 0\n"
     "        if c1 == self.t1 and c0 == self.t0:\n            return 1",
     "        if sum(c0) == sum(self.t1) and sum(c1) == sum(self.t0):\n            return 0\n"
     "        if sum(c1) == sum(self.t1) and sum(c0) == sum(self.t0):\n            return 1"),
    ('m5_reduction_allows_uncovered_v', 'x5_reduction_equals_brute_force',
     "        if len(nontriv) != 1:\n            return False",
     "        if len(nontriv) > 1:\n            return False\n        if not nontriv:\n            continue"),
    ('m6_tail_window_shift', 'x6',
     "            lo, hi = max(deadlines[i], L)+1, H2",
     "            lo, hi = max(deadlines[i], L)+2, H2"),
    ('m7a_actual_source_moved', 'x7_geometry',
     "    sources = [(-(L+1), S, 76), (-(L+1), S, 78), (-(L+2), S, 77)]",
     "    sources = [(-(L+1), S, 76), (-(L+1), S, 78), (-(L+1), S, 77)]"),
    ('m7b_arrival_check_late', 'x7_pre_arrival_samples_constant',
     "                   if t < min(dist(f, x) for f in SRC))",
     "                   if t < min(dist(f, x) for f in SRC)+1)"),
    ('m8_bitsliced_rule_or', 'x2|x1',
     "            ha, hb, hd = b, d, a ^ (b & d)",
     "            ha, hb, hd = b, d, a ^ (b | d)"),
    # Post-review (reviewer's R1 and R8): the searched domain shrinks.
    ('m10_region_radius_3', 'x0_scope_parameters',
     "REGION = sorted(ball(RHO))",
     "REGION = sorted(ball(RHO-1))"),
    ('m11_reads_to_L_plus_9', 'x0_scope_parameters',
     "TEND = NS+1+TAU ",
     "TEND = NS+1+TAU-8 "),
    ('m9_inject_A_at_first_G_arrival', 'HOLDS_WITHIN_SCOPE',
     "            fam, row = run_family(seed)",
     "            fam, row = run_family(seed, ((4, 0, 0), 12))"),
]


def main():
    src, work = sys.argv[1], os.path.abspath(sys.argv[2])
    text = open(src, encoding='utf-8').read()
    lines = []
    for name, target, old, new in MUTANTS:
        if text.count(old) != 1:
            raise RuntimeError('anchor for %s occurs %d times' % (name, text.count(old)))
        path = os.path.join(work, name+'.py')
        with open(path, 'w', encoding='utf-8') as f:
            f.write(text.replace(old, new))
        proc = subprocess.run([sys.executable, '-I', '-B', path], cwd=work,
                              capture_output=True, text=True, timeout=900)
        try:
            out = json.loads(proc.stdout)
            verdict = out.get('verdict')
            failed = out.get('required_controls', {}).get('failed')
        except ValueError:
            verdict, failed = 'UNPARSED', 'unparsed output, exit status %d' % proc.returncode
        if target == 'HOLDS_WITHIN_SCOPE':
            caught = proc.returncode == 0 and verdict == 'HOLDS_WITHIN_SCOPE'
            extra = out.get('common_stream_closed_admissible_R') if verdict != 'UNPARSED' else None
        else:
            caught = (proc.returncode == 2 and verdict == 'VOID' and isinstance(failed, str)
                      and any(failed.startswith(t) for t in target.split('|')))
            extra = None
        lines.append({'mutant': name, 'target': target, 'exit_status': proc.returncode,
                      'verdict': verdict, 'failed_control': failed, 'caught': caught,
                      'admissible_common_R': extra})
    all_caught = all(r['caught'] for r in lines)
    print(json.dumps({'mutants': lines, 'all_caught': all_caught}, indent=2, sort_keys=True))
    if not all_caught:
        sys.exit(1)


if __name__ == '__main__':
    main()
