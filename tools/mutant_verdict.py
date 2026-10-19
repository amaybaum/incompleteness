#!/usr/bin/env python3
"""Classify one mutant run of an evidence-retention check (the `retention-tests` workflow).

    mutant_verdict.py CHECK RC EXPECT LOG      print the verdict; exit 0 only for KILLED
    mutant_verdict.py --self-test              run the classifier against synthetic outputs

A mutant counts as caught only when the check failed *cleanly* and *on its target*:

  KILLED        rc is 1, the output ends in CHECK's own failing verdict line, and some failing-case line
                of CHECK's format contains EXPECT (the named case the mutant was written to break).
  SURVIVED      rc is 0: the check passed on the mutant.
  INFRA         rc is a timeout or signal status (124 and above, or negative): the run did not finish.
  CRASHED       rc is nonzero but the output does not end in CHECK's failing verdict line: an import or
                syntax error, an uncaught exception, or an unrelated tool failure.
  NOT-TARGETED  the check failed cleanly, but no failing-case line names EXPECT: it failed on something
                other than the mutant's target.

EXPECT must be a non-empty line of at least 8 characters, so that it names a case rather than matching any
line by accident. Only KILLED exits 0; every other verdict exits 1, so a crash, a timeout or an unrelated
failure can never be reported as a regression caught.
"""
import re
import sys

# Per check: the regular expression for its final failing verdict line, and a predicate for a failing-case line.
_FAIL_PREFIX = lambda line: line.startswith('FAIL')
_OBJECTS_CASE = lambda line: line.startswith('  ') and ' as required' not in line and not line.startswith('  pending')
CHECKS = {
    'gate': (r'^EVIDENCE-RETENTION  FAILS\b', _FAIL_PREFIX),
    'retention': (r'^RETENTION  FAILS\b', _FAIL_PREFIX),
    'retention-self-test': (r'^self-test: FAILED$', _FAIL_PREFIX),
    'objects': (r'^check_objects: FAILED\b', _FAIL_PREFIX),
    'objects-reconstitute': (r'^check_objects: FAILED\b', _FAIL_PREFIX),
    'objects-self-test': (r'^self-test: FAILED \(\d+ cases\)$', _OBJECTS_CASE),
    'tools-self-test': (r'^(comparator )?self-test: FAILED\b', _FAIL_PREFIX),
}
MIN_EXPECT = 8


def classify(check, rc, expect, text):
    if not isinstance(check, str) or check not in CHECKS:
        return 'INVALID', 'unknown check %r' % (check,)
    if not isinstance(expect, str) or '\n' in expect or len(expect.strip()) < MIN_EXPECT:
        return 'INVALID', 'expect must name the targeted case (one line, at least %d characters)' % MIN_EXPECT
    if rc == 0:
        return 'SURVIVED', '%s passed on the mutant' % check
    if rc < 0 or rc >= 124:
        return 'INFRA', '%s did not finish (status %d)' % (check, rc)
    verdict_re, is_case = CHECKS[check]
    lines = [l for l in text.splitlines() if l.strip()]
    last = lines[-1] if lines else ''
    if rc != 1 or not re.search(verdict_re, last):
        return 'CRASHED', '%s exited %d without its failing verdict line; last line: %s' % (check, rc, last[:160])
    hits = [l for l in lines if is_case(l) and expect in l]
    if not hits:
        return 'NOT-TARGETED', '%s failed, but no failing case names %r' % (check, expect)
    return 'KILLED', '%s failed on the target: %s' % (check, hits[0].strip()[:160])


def self_test():
    T = 'a gate step whose status differs'
    cases = [
        # (name, check, rc, expect, output, verdict)
        ('a targeted self-test failure is KILLED', 'retention-self-test', 1, T,
         'PASS self: x\nFAIL self: %s (C2)\nself-test: FAILED\n' % T, 'KILLED'),
        ('a passing check is SURVIVED', 'retention-self-test', 0, T, 'PASS self: x\nself-test: OK\n', 'SURVIVED'),
        ('an import error is CRASHED, not KILLED', 'retention-self-test', 1, T,
         'Traceback (most recent call last):\n  File "x", line 1\nModuleNotFoundError: No module named y\n', 'CRASHED'),
        ('a crash after a failing case is CRASHED, not KILLED', 'retention-self-test', 1, T,
         'FAIL self: %s (C2)\nTraceback (most recent call last):\nKeyError: z\n' % T, 'CRASHED'),
        ('a syntax error is CRASHED', 'tools-self-test', 1, T, '  File "x", line 3\nSyntaxError: invalid syntax\n', 'CRASHED'),
        ('an unrelated failing case is NOT-TARGETED', 'retention-self-test', 1, T,
         'FAIL self: some other case (C1)\nself-test: FAILED\n', 'NOT-TARGETED'),
        ('a target named only on a passing line is NOT-TARGETED', 'retention-self-test', 1, T,
         'PASS self: %s (C2)\nFAIL self: other (C1)\nself-test: FAILED\n' % T, 'NOT-TARGETED'),
        ('a timeout is INFRA', 'gate', 124, T, 'FAIL  %s\n' % T, 'INFRA'),
        ('a signal is INFRA', 'gate', -9, T, '', 'INFRA'),
        ('exit 2 with a verdict line is CRASHED', 'retention', 2, T, 'FAIL  %s\nRETENTION  FAILS (1 failure(s))\n' % T, 'CRASHED'),
        ('a targeted gate failure is KILLED', 'gate', 1, T,
         'FAIL  %s\nEVIDENCE-RETENTION  FAILS (history mode: 1 failure(s); self-test OK)\n' % T, 'KILLED'),
        ('a targeted objects failure is KILLED', 'objects', 1, T, 'FAIL  %s\ncheck_objects: FAILED (1)\n' % T, 'KILLED'),
        ('an objects self-test case not as required is KILLED', 'objects-self-test', 1, T,
         '  %s  O7  PASSES (should fail)\n  other  O1  FAILS as required\nself-test: FAILED (2 cases)\n' % T, 'KILLED'),
        ('an objects self-test case as required is NOT-TARGETED', 'objects-self-test', 1, T,
         '  %s  O7  FAILS as required\n  other  O1  NOT DETECTED\nself-test: FAILED (2 cases)\n' % T, 'NOT-TARGETED'),
        ('the comparator verdict line counts for tools-self-test', 'tools-self-test', 1, T,
         'FAIL self: %s (C2)\nself-test: FAILED\ncomparator self-test: FAILED (4 expected result(s))\n' % T, 'KILLED'),
        ('another check\'s verdict line is CRASHED', 'objects', 1, T, 'FAIL  %s\nRETENTION  FAILS (1)\n' % T, 'CRASHED'),
        ('an empty expect is INVALID', 'gate', 1, '', 'FAIL  x\nEVIDENCE-RETENTION  FAILS (x)\n', 'INVALID'),
        ('a short expect is INVALID', 'gate', 1, 'FAIL', 'FAIL  x\nEVIDENCE-RETENTION  FAILS (x)\n', 'INVALID'),
        ('an unknown check is INVALID', 'rm -rf', 1, T, '', 'INVALID'),
        ('a non-string check is INVALID', ['gate'], 1, T, '', 'INVALID'),
    ]
    bad = 0
    for name, check, rc, expect, out, want in cases:
        try:
            got = classify(check, rc, expect, out)[0]
        except Exception as e:  # a classifier that raises fails its case
            got = 'raised %s' % type(e).__name__
        good = got == want
        bad += not good
        print('%s self: %s (want %s, got %s)' % ('PASS' if good else 'FAIL', name, want, got))
    print('self-test: %s (%d cases)' % ('OK' if not bad else 'FAILED', len(cases)))
    return 1 if bad else 0


def main(argv):
    if argv[1:] == ['--self-test']:
        return self_test()
    if len(argv) != 5:
        print(__doc__)
        return 2
    check, rc, expect, log = argv[1:]
    try:
        rc = int(rc)
    except ValueError:
        print('INVALID  rc %r is not an integer' % rc)
        return 1
    with open(log, encoding='utf-8', errors='replace') as f:
        text = f.read()
    verdict, why = classify(check, rc, expect, text)
    print('%s  %s' % (verdict, why))
    return 0 if verdict == 'KILLED' else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv))
