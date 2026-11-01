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
    ('u1_scope_break_but_targets_x1', 'x1_scalar_evaluator_agrees',
     "REGION = sorted(ball(RHO))", "REGION = sorted(ball(RHO-1))"),
    ('u2_syntax_error', 'x1_scalar_evaluator_agrees',
     "NS = 6 ", "NS = = 6 "),
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
