"""Replay control for a probe optimization.

Runs a probe as it was at a given commit and as it is in the working tree, and requires the two to
print the same PASS and FAIL lines, with the same values, in the same order, and the same summary
line. A probe whose arithmetic is rewritten for speed must assert exactly what it asserted before;
this is the check that it does.

    python3 tools/probe_replay_check.py <commit> <probe path>      run both and compare
    python3 tools/probe_replay_check.py --self-test                the comparison on synthetic logs

Exit 1 on any difference, on a nonzero exit of either probe, or on a self-test failure.
"""
import os
import re
import subprocess
import sys
import tempfile
import time

CHECK = re.compile(r'^  (PASS|FAIL)  .*$')
SUMMARY = re.compile(r'^\w+: (OK|FAILED)')


def lines_of(log):
    """The check lines and the summary line, in order, with timing lines dropped."""
    out = [l for l in log.split('\n') if CHECK.match(l)]
    out += [l for l in log.split('\n') if SUMMARY.match(l)]
    return out


def compare(old_log, new_log):
    a, b = lines_of(old_log), lines_of(new_log)
    diffs = []
    for i in range(max(len(a), len(b))):
        x = a[i] if i < len(a) else '<absent>'
        y = b[i] if i < len(b) else '<absent>'
        if x != y:
            diffs.append((i, x, y))
    return a, b, diffs


def run(cmd, cwd):
    t0 = time.time()
    p = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    return p.returncode, p.stdout, p.stderr, time.time() - t0


def main(argv):
    if argv == ['--self-test']:
        same = 'x\n  PASS  a  1\n  (3s)\n  PASS  b  (1, 2)\n\nprobe: OK -- s\n'
        a, b, d = compare(same, same.replace('(3s)', '(9s)'))
        if d or len(a) != 3:
            print('self-test FAILED: identical logs differ'); return 1
        for bad in (same.replace('  PASS  b  (1, 2)', '  PASS  b  (1, 3)'), same.replace('  PASS  a  1\n', ''),
                    same.replace('probe: OK -- s', 'probe: FAILED (1)'), same.replace('  PASS  b', '  FAIL  b')):
            _, _, d = compare(same, bad)
            if not d:
                print('self-test FAILED: a difference was accepted'); return 1
        print('probe_replay_check: self-test OK (identical logs agree; a changed value, a dropped check, a changed summary and a flipped verdict are each rejected)')
        return 0
    if len(argv) != 2:
        print(__doc__); return 2
    commit, path = argv
    cwd = os.path.dirname(os.path.abspath(path)) or '.'
    old_src = subprocess.run(['git', 'show', '%s:%s' % (commit, path)], capture_output=True, text=True, check=True).stdout
    fd, old_path = tempfile.mkstemp(prefix='replay_old_', suffix='.py', dir=cwd)
    with os.fdopen(fd, 'w', encoding='utf-8') as f:
        f.write(old_src)
    try:
        procs = {}
        for name, target in (('old', old_path), ('new', os.path.abspath(path))):
            procs[name] = (time.time(), subprocess.Popen([sys.executable, target], cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True))
        results = {}
        for name, (t0, p) in procs.items():
            out, err = p.communicate()
            results[name] = (p.returncode, out, err, time.time() - t0)
    finally:
        os.unlink(old_path)
    for name in ('old', 'new'):
        rc, out, err, dt = results[name]
        print('%s: exit %d in %.0f s, %d check lines' % (name, rc, dt, len([l for l in out.split('\n') if CHECK.match(l)])))
        if rc != 0:
            print(err[-2000:])
    a, b, diffs = compare(results['old'][1], results['new'][1])
    for i, x, y in diffs:
        print('DIFF at %d:\n  old: %s\n  new: %s' % (i, x, y))
    ok = not diffs and results['old'][0] == 0 and results['new'][0] == 0
    print('probe_replay_check: %s -- %d lines compared, %d difference(s)' % ('OK' if ok else 'FAILED', len(a), len(diffs)))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
