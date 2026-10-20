#!/usr/bin/env python3
"""evidence_archive_check.py - the frozen evidence-retention archive is unchanged (AGENTS §A.42 item 8).

verification/audits/evidence-retention/ is frozen: it is neither extended nor maintained. This
check passes only when the directory's tree at HEAD is the pinned tree and the working tree adds,
changes or removes nothing under it. A change to the archive is an owner-authorized change of PIN.

    python3 tools/evidence_archive_check.py               exit 0 only when the archive is unchanged
    python3 tools/evidence_archive_check.py --self-test   exercise the comparison on fixed inputs

Run from anywhere inside the repository. A shallow clone is enough: no history is read.
"""
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARCHIVE = 'verification/audits/evidence-retention'
PIN = 'c8b7e8861dfbb79af1a71c8cef8fcfaf0acea85e'


def git(*args):
    return subprocess.run(['git', *args], cwd=ROOT, capture_output=True, text=True)


def problems(tree, dirty, untracked, pin=PIN):
    """The ways the observed state differs from the frozen archive; empty when it is unchanged."""
    p = []
    if tree != pin:
        p.append('tree %s at HEAD, pinned %s' % (tree or 'missing', pin))
    if dirty:
        p.append('uncommitted changes under %s' % ARCHIVE)
    for f in untracked:
        p.append('untracked file %s' % f)
    return p


def observe():
    r = git('rev-parse', '--verify', '--quiet', 'HEAD:' + ARCHIVE)
    tree = r.stdout.strip() if r.returncode == 0 else ''
    d = git('diff', '--quiet', 'HEAD', '--', ARCHIVE)
    if d.returncode not in (0, 1):
        raise RuntimeError('git diff failed: %s' % d.stderr.strip())
    u = git('ls-files', '--others', '--exclude-standard', '--', ARCHIVE)
    if u.returncode != 0:
        raise RuntimeError('git ls-files failed: %s' % u.stderr.strip())
    return tree, d.returncode == 1, [l for l in u.stdout.splitlines() if l]


def self_test():
    cases = [
        ('the pinned tree, clean', (PIN, False, []), 0),
        ('another tree', ('0' * 40, False, []), 1),
        ('no tree at HEAD', ('', False, []), 1),
        ('uncommitted changes', (PIN, True, []), 1),
        ('an untracked file', (PIN, False, [ARCHIVE + '/x.json']), 1),
    ]
    bad = 0
    for name, args, want in cases:
        got = len(problems(*args))
        ok = (got == 0) == (want == 0)
        bad += not ok
        print('%s  self: %s' % ('PASS' if ok else 'FAIL', name))
    if len(PIN) != 40 or any(c not in '0123456789abcdef' for c in PIN):
        print('FAIL  self: PIN is not a full tree id')
        bad += 1
    print('self-test: %s' % ('OK' if not bad else 'FAILED'))
    return 1 if bad else 0


def main(argv):
    if argv == ['--self-test']:
        return self_test()
    if argv:
        print(__doc__)
        return 2
    try:
        p = problems(*observe())
    except Exception as exc:  # fails closed
        print('evidence-archive: FAIL (%s: %s)' % (type(exc).__name__, exc))
        return 1
    for x in p:
        print('FAIL  %s' % x)
    print('evidence-archive: %s (pinned tree %s)' % ('FAIL' if p else 'OK', PIN[:12]))
    return 1 if p else 0


if __name__ == '__main__':
    raise SystemExit(main(sys.argv[1:]))
