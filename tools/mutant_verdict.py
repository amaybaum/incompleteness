#!/usr/bin/env python3
"""Classify one mutant run of an evidence-retention check (the `retention-tests` workflow).

    mutant_verdict.py CHECK RC EXPECT LOG      print the verdict; exit 0 only for KILLED
    mutant_verdict.py --check-expect CHECK EXPECT
                                               exit 0 if EXPECT is acceptable for CHECK, else print why
    mutant_verdict.py --self-test              run the classifier against fixtures shaped like the tools' output

A mutant counts as caught only when its check failed *cleanly* and *on its target*:

  KILLED        rc is 1; the output contains no Python traceback; its last line is CHECK's own failing
                verdict line; and a failing case matches EXPECT under CHECK's rule (below).
  SURVIVED      rc is 0: the check passed on the mutant.
  INFRA         rc is a timeout or signal status (124 and above, or negative): the run did not finish.
  CRASHED       anything else that failed: a traceback anywhere in the output, or any Python stack-frame or
                syntax-error location line (`File "...", line N`), including one printed by a subprocess the
                check runs, such as the gate's, whose header may have been truncated away; an exit status
                other than 1; or a last line that is not CHECK's failing verdict.
  NOT-TARGETED  the check failed cleanly, but no failing case matches EXPECT.

Matching EXPECT, by check:
  retention-self-test, tools-self-test   EXPECT is the exact name of a failing case as printed on its
                                         `FAIL self: NAME` line, with its trailing rule tag such as ` (C2)`
                                         when the case prints one.
  objects-self-test                      EXPECT is the exact name of a case-table row whose verdict is not
                                         `FAILS as required` or `PASSES as required`.
  gate, retention, objects,              these report failures as messages (`FAIL  ...`, and the gate's
  objects-reconstitute                   embedded `FAIL self: ...`). EXPECT is a substring of a failing
                                         line's text after its `FAIL` prefix, at least 12 characters, and
                                         may not itself begin with `FAIL` or `self:`.

Only KILLED exits 0, so a crash, a timeout, an unrelated failure or a passing check is never reported as a
regression caught.
"""
import re
import sys

TRACEBACK = 'Traceback (most recent call last):'
# A Python stack frame or syntax-error location line. The gate prints a failed subprocess's stderr cut to its
# last 2000 characters, which can drop the Traceback header, and a SyntaxError has no header at all; both
# still carry these lines.
_FRAME = re.compile(r'^\s*File "[^"]*", line \d+')
REQUIRED = ('FAILS as required', 'PASSES as required')
VERDICT = {
    'gate': r'^EVIDENCE-RETENTION  FAILS\b',
    'retention': r'^RETENTION  FAILS\b',
    'retention-self-test': r'^self-test: FAILED$',
    'objects': r'^check_objects: FAILED\b',
    'objects-reconstitute': r'^check_objects: FAILED\b',
    'objects-self-test': r'^self-test: FAILED \(\d+ cases\)$',
    'tools-self-test': r'^(comparator )?self-test: FAILED\b',
}
FAMILY = {
    'retention-self-test': 'case', 'tools-self-test': 'case',
    'objects-self-test': 'table',
    'gate': 'message', 'retention': 'message', 'objects': 'message', 'objects-reconstitute': 'message',
}
_TABLE_ROW = re.compile(r'^  (.+?)\s{2,}(\S.*?)\s{2,}(FAILS as required|PASSES as required|NOT DETECTED|FAILS)(  \[.*)?\s*$')
MIN_CASE, MIN_MESSAGE = 8, 12


def expect_problem(check, expect):
    """None if EXPECT is acceptable for CHECK, else the reason it is not."""
    if not isinstance(check, str) or check not in VERDICT:
        return 'unknown check %r' % (check,)
    if not isinstance(expect, str) or '\n' in expect or expect != expect.strip():
        return 'expect must be one line with no surrounding spaces'
    if FAMILY[check] == 'message':
        if len(expect) < MIN_MESSAGE or expect.startswith(('FAIL', 'self:')):
            return ('for %s, expect is a failure message fragment of at least %d characters that does not begin '
                    'with FAIL or self:' % (check, MIN_MESSAGE))
    elif len(expect) < MIN_CASE:
        return 'for %s, expect is the exact name of the targeted case (at least %d characters)' % (check, MIN_CASE)
    return None


def _hits(check, expect, lines):
    fam = FAMILY[check]
    if fam == 'case':
        # The whole printed name, rule tag included: some names recur under two tags, and which tags a run prints
        # can itself depend on the mutant.
        return [l for l in lines if l.startswith('FAIL self: ') and l[len('FAIL self: '):] == expect]
    if fam == 'table':
        out = []
        for l in lines:
            m = _TABLE_ROW.match(l)
            if m and m.group(1).rstrip() == expect and m.group(3) not in REQUIRED:
                out.append(l)
        return out
    out = []
    for l in lines:
        for prefix in ('FAIL self: ', 'FAIL  '):
            if l.startswith(prefix) and expect in l[len(prefix):]:
                out.append(l)
                break
    return out


def classify(check, rc, expect, text):
    why = expect_problem(check, expect)
    if why:
        return 'INVALID', why
    if rc == 0:
        return 'SURVIVED', '%s passed on the mutant' % check
    if rc < 0 or rc >= 124:
        return 'INFRA', '%s did not finish (status %d)' % (check, rc)
    lines = [l for l in text.splitlines() if l.strip()]
    if any(l.startswith(TRACEBACK) or _FRAME.match(l) for l in lines):
        return 'CRASHED', '%s printed a Python traceback or stack frame (the check or a subprocess crashed)' % check
    last = lines[-1] if lines else ''
    if rc != 1 or not re.search(VERDICT[check], last):
        return 'CRASHED', '%s exited %d without its failing verdict line; last line: %s' % (check, rc, last[:160])
    hits = _hits(check, expect, lines)
    if not hits:
        return 'NOT-TARGETED', '%s failed, but no failing case matches %r' % (check, expect)
    return 'KILLED', '%s failed on the target: %s' % (check, hits[0].strip()[:160])


def self_test():
    T = 'a gate step whose status differs'
    M = 'the receipt of round X is not covered'
    gate_end = 'EVIDENCE-RETENTION  FAILS (history mode: 1 failure(s); self-test OK; retained objects FAILED)\n'
    cases = [
        # (name, check, rc, expect, output, verdict)
        ('a targeted self-test failure is KILLED', 'retention-self-test', 1, T + ' (C2)',
         'PASS self: x\nFAIL self: %s (C2)\nself-test: FAILED\n' % T, 'KILLED'),
        ('an untagged case is named without a tag', 'retention-self-test', 1, T,
         'PASS self: x\nFAIL self: %s\nself-test: FAILED\n' % T, 'KILLED'),
        ('a tagged case named without its tag is NOT-TARGETED', 'retention-self-test', 1, T,
         'FAIL self: %s (C2)\nself-test: FAILED\n' % T, 'NOT-TARGETED'),
        ('a case named with another tag is NOT-TARGETED', 'retention-self-test', 1, T + ' (R12)',
         'FAIL self: %s (R8)\nself-test: FAILED\n' % T, 'NOT-TARGETED'),
        ('a longer case that only begins with the target is NOT-TARGETED', 'retention-self-test', 1, T,
         'PASS self: %s\nFAIL self: %s, twice (C2)\nself-test: FAILED\n' % (T, T), 'NOT-TARGETED'),
        ('a fragment of a case name is NOT-TARGETED', 'tools-self-test', 1, 'step whose status',
         'FAIL self: %s (C2)\nself-test: FAILED\ncomparator self-test: FAILED (4 expected result(s))\n' % T, 'NOT-TARGETED'),
        ('a passing check is SURVIVED', 'retention-self-test', 0, T, 'PASS self: x\nself-test: OK\n', 'SURVIVED'),
        ('an import error is CRASHED, not KILLED', 'retention-self-test', 1, T,
         'Traceback (most recent call last):\n  File "x", line 1\nModuleNotFoundError: No module named y\n', 'CRASHED'),
        ('a crash after a failing case is CRASHED, not KILLED', 'retention-self-test', 1, T,
         'FAIL self: %s (C2)\nTraceback (most recent call last):\nKeyError: z\n' % T, 'CRASHED'),
        ('a subprocess crash inside a cleanly failing gate is CRASHED', 'gate', 1, M,
         'FAIL  %s\nTraceback (most recent call last):\n  File "check_objects.py", line 9\nKeyError: oid\n%s' % (M, gate_end),
         'CRASHED'),
        ('a syntax error is CRASHED', 'tools-self-test', 1, T, '  File "x", line 3\nSyntaxError: invalid syntax\n', 'CRASHED'),
        ('a subprocess traceback truncated past its header, inside a cleanly failing gate, is CRASHED', 'gate', 1, M,
         'FAIL  %s\n    verification/audits/evidence-retention/check_objects.py", line 812, in walk\n'
         '  File "/home/runner/work/x/verification/audits/evidence-retention/check_objects.py", line 830, in walk\n'
         '    raise KeyError(oid)\nKeyError: oid\n%s' % (M, gate_end), 'CRASHED'),
        ('a subprocess syntax error inside a cleanly failing gate is CRASHED', 'gate', 1, M,
         'FAIL  %s\n  File "/home/runner/work/x/job_outputs.py", line 4\n    def (\n        ^\nSyntaxError: invalid syntax\n%s'
         % (M, gate_end), 'CRASHED'),
        ('a bare name shared by cases under two tags does not identify the target', 'retention-self-test', 1, T,
         'PASS self: %s (R12)\nFAIL self: %s (R8)\nself-test: FAILED\n' % (T, T), 'NOT-TARGETED'),
        ('the tagged name still identifies a case whose bare name is shared', 'retention-self-test', 1, T + ' (R8)',
         'PASS self: %s (R12)\nFAIL self: %s (R8)\nself-test: FAILED\n' % (T, T), 'KILLED'),
        ('an unrelated failing case is NOT-TARGETED', 'retention-self-test', 1, T,
         'FAIL self: some other case (C1)\nself-test: FAILED\n', 'NOT-TARGETED'),
        ('a target named only on a passing line is NOT-TARGETED', 'retention-self-test', 1, T,
         'PASS self: %s (C2)\nFAIL self: other (C1)\nself-test: FAILED\n' % T, 'NOT-TARGETED'),
        ('a timeout is INFRA', 'gate', 124, M, 'FAIL  %s\n' % M, 'INFRA'),
        ('a SIGKILL after timeout is INFRA', 'gate', 137, M, '', 'INFRA'),
        ('a signal is INFRA', 'gate', -9, M, '', 'INFRA'),
        ('exit 2 with a verdict line is CRASHED', 'retention', 2, M, 'FAIL  %s\nRETENTION  FAILS (1 failure(s))\n' % M, 'CRASHED'),
        ('a targeted gate failure is KILLED', 'gate', 1, M, 'FAIL  %s\n%s' % (M, gate_end), 'KILLED'),
        ('a targeted objects failure is KILLED', 'objects', 1, M, 'FAIL  %s\ncheck_objects: FAILED (1)\n' % M, 'KILLED'),
        ('an objects table row NOT DETECTED is KILLED', 'objects-self-test', 1, T,
         '  %s  O7   NOT DETECTED\n  other case    O1   FAILS as required  [x]\nself-test: FAILED (2 cases)\n' % T, 'KILLED'),
        ('an objects table row FAILS (should pass) is KILLED', 'objects-self-test', 1, T,
         '  %s  -    FAILS  [unexpected]\nself-test: FAILED (1 cases)\n' % T, 'KILLED'),
        ('an objects row as required is NOT-TARGETED', 'objects-self-test', 1, T,
         '  %s  O7   FAILS as required\n  other case    O1   NOT DETECTED\nself-test: FAILED (2 cases)\n' % T, 'NOT-TARGETED'),
        ('the target inside another row\'s error text is NOT-TARGETED', 'objects-self-test', 1, T,
         '  %s  O7   FAILS as required\n  other case    O1   NOT DETECTED  [%s]\nself-test: FAILED (2 cases)\n' % (T, T),
         'NOT-TARGETED'),
        ('a rule column holding an object id is parsed', 'objects-self-test', 1, T,
         '  %s  O10 1ab0fd9dd2c6:  NOT DETECTED\n  other case    O3 1ab0/O7 1ab0  FAILS as required\nself-test: FAILED (2 cases)\n' % T,
         'KILLED'),
        ('a row whose name extends the target is NOT-TARGETED', 'objects-self-test', 1, T,
         '  %s in tranche 2  O7   NOT DETECTED\nself-test: FAILED (1 cases)\n' % T, 'NOT-TARGETED'),
        ('the comparator verdict line counts for tools-self-test', 'tools-self-test', 1, T + ' (C2)',
         'FAIL self: %s (C2)\nself-test: FAILED\ncomparator self-test: FAILED (4 expected result(s))\n' % T, 'KILLED'),
        ('another check\'s verdict line is CRASHED', 'objects', 1, M, 'FAIL  %s\nRETENTION  FAILS (1)\n' % M, 'CRASHED'),
        ('an empty expect is INVALID', 'gate', 1, '', 'FAIL  x\n' + gate_end, 'INVALID'),
        ('a short case expect is INVALID', 'retention-self-test', 1, 'a case', '', 'INVALID'),
        ('a message expect that is a bare prefix is INVALID', 'gate', 1, 'FAIL self: the', '', 'INVALID'),
        ('a short message expect is INVALID', 'gate', 1, 'not covered', '', 'INVALID'),
        ('an expect with surrounding spaces is INVALID', 'retention-self-test', 1, ' ' + T, '', 'INVALID'),
        ('an unknown check is INVALID', 'rm -rf', 1, T, '', 'INVALID'),
        ('a non-string check is INVALID', ['gate'], 1, T, '', 'INVALID'),
        ('a non-string expect is INVALID', 'gate', 1, 12345678901234, '', 'INVALID'),
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
    if len(argv) == 4 and argv[1] == '--check-expect':
        why = expect_problem(argv[2], argv[3])
        if why:
            print(why)
        return 1 if why else 0
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
