"""Check the provenance errata of this directory against the repository.

For each entry of errata.json:
  E1  the citing record is unchanged: its blob at HEAD is the pinned blob, and the cited line names the run
      and the cited head;
  E2  the cited head names no object in the repository, shares its first 8 hex digits with the real head, and
      differs from it;
  E3  when the real head is present, its tree and parent are the recorded ones and every content check holds;
      the commit is reachable from no ref of the host, so a clone of main lacks it until it is restored from a
      preservation bundle, and E3 then reports the entry as not checkable here (an error with
      --require-objects);
  E4  the README lists the entry with its status, and the entry's outcome names jobs and served digests.
The job conclusions, the jobs' head commits and the log facts are host records read through the API; they are
recorded with their provenance and cannot be re-derived from the tree.

Usage: python3 -I check_errata.py [--require-objects] [--self-test]"""
import copy, json, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = subprocess.run(['git', '-C', HERE, 'rev-parse', '--show-toplevel'], capture_output=True, text=True,
                      check=True).stdout.strip()
REL = os.path.relpath(HERE, ROOT)
HEX40 = re.compile(r'^[0-9a-f]{40}$')
STATUSES = ('holds', 'partly holds', 'does not hold', 'not established')


def git(*a, ok=False):
    p = subprocess.run(['git', '-C', ROOT, *a], capture_output=True)
    if ok:
        return p.returncode == 0
    if p.returncode:
        raise RuntimeError('git %s: %s' % (' '.join(a), p.stderr.decode('utf-8', 'replace').strip()))
    return p.stdout


def has_object(oid, kind=None):
    return git('cat-file', '-e', oid + ('^{%s}' % kind if kind else ''), ok=True)


def show(rev, path):
    return git('show', '%s:%s' % (rev, path)).decode('utf-8')


def content_check(c, head):
    k = c['kind']
    if k == 'count_lines_matching':
        n = sum(1 for l in show(head, c['path']).split('\n') if re.search(c['regex'], l))
        return n == c['expect'], '%s: %d lines match %r, expected %d' % (c['path'], n, c['regex'], c['expect'])
    if k == 'line_contains':
        lines = show(head, c['path']).split('\n')
        got = lines[c['line'] - 1] if 0 < c['line'] <= len(lines) else ''
        return c['text'] in got, '%s:%d does not contain %r' % (c['path'], c['line'], c['text'])
    if k == 'consecutive_lines':
        lines = [l.strip() for l in show(head, c['path']).split('\n')]
        want = c['lines']
        hit = any(lines[i:i + len(want)] == want for i in range(len(lines)))
        return hit, '%s: lines %r are not consecutive' % (c['path'], want)
    if k == 'diff_paths':
        got = sorted(git('diff', '--name-only', c['against'], head).decode().split())
        return got == sorted(c['expect']), 'diff from %s touches %r, expected %r' % (c['against'][:8], got, sorted(c['expect']))
    if k == 'diff_adds_line':
        d = git('diff', c['against'], head, '--', c['path']).decode('utf-8')
        return ('+' + c['text']) in d.split('\n'), 'diff from %s does not add %r' % (c['against'][:8], c['text'])
    if k == 'diff_line_counts':
        d = git('diff', '--numstat', c['against'], head, '--', c['path']).decode().split()
        got = (int(d[0]), int(d[1])) if len(d) >= 2 else None
        return got == (c['added'], c['removed']), 'diff from %s: %r lines added/removed, expected %r' % (
            c['against'][:8], got, (c['added'], c['removed']))
    if k == 'tree_equals_cited':
        t = git('rev-parse', head + '^{tree}').decode().strip()
        return t == c['cited_tree'], 'tree %s is not the cited tree %s' % (t, c['cited_tree'])
    if k == 'blob_at':
        p = subprocess.run(['git', '-C', ROOT, 'rev-parse', '%s:%s' % (head, c['path'])], capture_output=True, text=True)
        b = p.stdout.strip() if p.returncode == 0 else None
        return b == c['blob'], '%s is %s, expected %s' % (c['path'], b, c['blob'])
    if k == 'blobs_equal_at':
        bad = []
        for path in c['paths']:
            x = subprocess.run(['git', '-C', ROOT, 'rev-parse', '%s:%s' % (head, path)], capture_output=True, text=True).stdout.strip()
            y = subprocess.run(['git', '-C', ROOT, 'rev-parse', '%s:%s' % (c['other'], path)], capture_output=True, text=True).stdout.strip()
            if not x or x != y:
                bad.append(path)
        return not bad, '%r differ between the real head and %s' % (bad, c['other'][:8])
    return False, 'unknown content check %r' % k


def check(data, readme, require_objects):
    fails, unchecked, checked = [], [], 0
    for e in data['entries']:
        eid = e['id']
        f = lambda code, msg: fails.append('%s %s %s' % (code, eid, msg))
        for key in ('citing_blob', 'cited_head', 'real_head', 'real_tree', 'real_parent'):
            if not HEX40.match(e.get(key, '')):
                f('E0', '%s is not a full 40-hex id' % key)
        path, line = e['location'].rsplit(':', 1)
        line = int(line)
        # E1: the frozen record is unchanged and the cited line is the one recorded
        p = subprocess.run(['git', '-C', ROOT, 'rev-parse', 'HEAD:' + path], capture_output=True, text=True)
        blob = p.stdout.strip() if p.returncode == 0 else None
        if blob != e['citing_blob']:
            f('E1', '%s has blob %s at HEAD, pinned %s' % (path, blob, e['citing_blob']))
        else:
            text = show('HEAD', path).split('\n')
            got = text[line - 1] if 0 < line <= len(text) else ''
            if e['run_id'] not in got or e['cited_head'] not in got:
                f('E1', '%s does not name run %s and %s' % (e['location'], e['run_id'], e['cited_head']))
        # E2: the cited head names nothing, and is the real head's 8-hex prefix with a different tail
        if has_object(e['cited_head']):
            f('E2', 'the cited head %s names an object in the repository' % e['cited_head'])
        if e['cited_head'][:8] != e['real_head'][:8] or e['cited_head'] == e['real_head']:
            f('E2', 'the cited head %s is not a prefix collision with %s' % (e['cited_head'], e['real_head']))
        # E3: the real head's objects, when present
        if not has_object(e['real_head'], 'commit'):
            (fails if require_objects else unchecked).append(
                'E3 %s real head %s is not in this repository; restore it from the preservation bundles' % (eid, e['real_head']))
        else:
            checked += 1
            tree = git('rev-parse', e['real_head'] + '^{tree}').decode().strip()
            if tree != e['real_tree']:
                f('E3', 'real head tree %s, recorded %s' % (tree, e['real_tree']))
            parent = git('log', '-1', '--format=%P', e['real_head']).decode().strip()
            if parent != e['real_parent']:
                f('E3', 'real head parent %s, recorded %s' % (parent, e['real_parent']))
            for c in e['content_checks']:
                good, msg = content_check(c, e['real_head'])
                if not good:
                    f('E3', msg)
        # E4: the README states the entry and its status; the outcome carries its provenance
        if e.get('status') not in STATUSES:
            f('E4', 'status %r is not one of %r' % (e.get('status'), STATUSES))
        row = next((l for l in readme.split('\n') if l.startswith('| %s |' % eid)), None)
        if row is None or ('| %s |' % e.get('status')) not in row or e['location'] not in row:
            f('E4', 'the README has no row for %s with its location and status %r' % (eid, e.get('status')))
        out = e.get('outcome', {})
        if not out.get('jobs') or out.get('every_job_head_is_the_real_head') is not True:
            f('E4', 'the outcome records no jobs, or not that every job ran on the real head')
        for lf in out.get('log_facts', []):
            if not re.match(r'^[0-9a-f]{64}$', lf.get('served_sha256', '')) or not lf.get('facts'):
                f('E4', 'log facts of job %s carry no served digest or no facts' % lf.get('job'))
    return fails, unchecked, checked


def self_test(data, readme):
    """Each mutation must fail with its code; the unmutated table must pass where the objects are present."""
    base_fails, _, n_checked = check(data, readme, False)
    assert not base_fails, base_fails
    E = lambda d, i: d['entries'][i]
    def put(i, key, val):
        return lambda d, r: (E(d, i).__setitem__(key, val), r)[1]
    def put_check(i, j, key, val):
        return lambda d, r: (E(d, i)['content_checks'][j].__setitem__(key, val), r)[1]
    cases = [
        ('E1', 'a changed citing blob', put(0, 'citing_blob', '0' * 40)),
        ('E1', 'a citing line that does not name the cited head',
         lambda d, r: (E(d, 0).__setitem__('location', E(d, 0)['location'].rsplit(':', 1)[0] + ':1'), r)[1]),
        ('E2', 'a cited head that names an object', lambda d, r: (E(d, 0).__setitem__('cited_head', git('rev-parse', 'HEAD').decode().strip()), r)[1]),
        ('E2', 'a cited head that is not a prefix collision', put(1, 'real_head', 'f' * 40)),
        ('E4', 'a README without a row', lambda d, r: r.replace('| PE-3 |', '| PE-X |')),
        ('E4', 'a README row with another status', lambda d, r: r.replace('| partly holds |', '| holds |')),
        ('E4', 'a status outside the vocabulary', put(2, 'status', 'mostly')),
        ('E4', 'an outcome without a served digest', lambda d, r: (E(d, 3)['outcome']['log_facts'][0].__setitem__('served_sha256', ''), r)[1]),
        ('E0', 'a truncated id', put(3, 'real_tree', '12a695df')),
    ]
    if n_checked:
        cases += [
            ('E3', 'a wrong recorded tree', put(0, 'real_tree', '0' * 40)),
            ('E3', 'a wrong recorded parent', put(1, 'real_parent', '0' * 40)),
            ('E3', 'a wrong #check count', put_check(0, 1, 'expect', 21)),
            ('E3', 'a wrong theorem count', put_check(2, 1, 'expect', 53)),
            ('E3', 'a wrong blob at a path', put_check(3, 1, 'blob', '0' * 40)),
            ('E3', 'a tree that is not the cited tree', put_check(3, 0, 'cited_tree', '0' * 40)),
            ('E3', 'a line without the notation', put_check(0, 2, 'line', 357)),
            ('E3', 'an import order that does not hold',
             lambda d, r: (E(d, 0)['content_checks'][3].__setitem__('lines', list(reversed(E(d, 0)['content_checks'][3]['lines']))), r)[1]),
            ('E3', 'a diff touching other paths', lambda d, r: (E(d, 1)['content_checks'][0]['expect'].append('papers/Main.md'), r)[1]),
            ('E3', 'a line the diff does not add', put_check(1, 1, 'text', 'import Mathlib.Foo')),
            ('E3', 'wrong diff line counts', put_check(1, 2, 'removed', 2)),
            ('E3', 'blobs compared with a commit that differs', put_check(3, len(data['entries'][3]['content_checks']) - 1, 'other', data['entries'][0]['real_head'])),
        ]
    for code, name, mut in cases:
        d = copy.deepcopy(data)
        r = mut(d, readme)
        fails, _, _ = check(d, r, False)
        if not any(x.split()[0] == code for x in fails):
            raise AssertionError('mutation not caught as %s: %s (%r)' % (code, name, fails))
    return len(cases), n_checked


def main():
    args = sys.argv[1:]
    data = json.load(open(os.path.join(HERE, 'errata.json'), encoding='utf-8'))
    readme = open(os.path.join(HERE, 'README.md'), encoding='utf-8').read()
    if '--self-test' in args:
        n, k = self_test(data, readme)
        print('errata self-test: OK (%d mutations caught; content checks exercised on %d entr%s with objects present)'
              % (n, k, 'y' if k == 1 else 'ies'))
        return 0
    fails, unchecked, checked = check(data, readme, '--require-objects' in args)
    for x in fails:
        print('FAIL', x)
    for x in unchecked:
        print('NOT CHECKABLE HERE', x)
    n = len(data['entries'])
    print('ERRATA  %s (%d entr%s, %d with the real head present and checked, %d failure(s))'
          % ('HOLDS' if not fails else 'FAILS', n, 'y' if n == 1 else 'ies', checked, len(fails)))
    return 1 if fails else 0


if __name__ == '__main__':
    sys.exit(main())
