#!/usr/bin/env python3
"""check_retention.py -- verifies the evidence-retention archive from the repository tree alone.

No git history, network or third-party package is used. From the repository root:

    python3 -I verification/audits/evidence-retention/check_retention.py           # check, exit 1 on any failure
    python3 -I verification/audits/evidence-retention/check_retention.py --self-test

Checked, for every manifest entry:
  R1  every archived file exists, and its size and sha256 are the recorded ones;
  R2  a file kept "complete-as-cited" has exactly the digest the citing record names;
  R3  every citation's file exists, its git blob id is the recorded one (the historical record is unchanged),
      and the cited line still contains the cited token;
  R4  an excerpt's line count equals the lines its recorded ranges name;
  R5  no archived file matches the secret patterns;
  R6  every file in the archive directory is listed in the manifest or is one of the archive's own fixed files.
The manifest's "missing" list is printed; missing evidence is a gap, not a failure.
"""
import hashlib
import json
import os
import re
import shutil
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
FIXED = {'README.md', 'manifest.json', 'check_retention.py', 'build_archive.py', 'audit/offmain_audit.py', 'audit/offmain_audit-output.txt',
         'audit/audit.md'}
SECRET = re.compile(r'gh[pousr]_[A-Za-z0-9]{20,}|github_pat_|AKIA[0-9A-Z]{16}|-----BEGIN|bearer [a-z0-9]'
                    r'|x-access-token|[?&](sig|signature|sv|se|token)=|passw(or)?d\s*[:=]|api[_-]?key\s*[:=]'
                    r'|private[_-]?key', re.I)
SECRET_OK = re.compile(r'Secret source: Actions|AUTHORIZATION: basic \*\*\*')


def blob_id(data):
    return hashlib.sha1(b'blob %d\0' % len(data) + data).hexdigest()


def check(archive, root):
    fails, gaps = [], []
    man = json.load(open(os.path.join(archive, 'manifest.json'), encoding='utf-8'))
    if man.get('schema') != 'oi-evidence-retention':
        return ['manifest schema'], gaps
    listed = set()
    for e in man['entries']:
        for f in e.get('files', []):
            listed.add(f['path'])
            p = os.path.join(archive, f['path'])
            if not os.path.isfile(p):
                fails.append('R1 %s: %s missing' % (e['id'], f['path']))
                continue
            data = open(p, 'rb').read()
            if len(data) != f['bytes'] or hashlib.sha256(data).hexdigest() != f['sha256']:
                fails.append('R1 %s: %s size or sha256 differs' % (e['id'], f['path']))
            text = data.decode('utf-8', 'replace')
            if any(SECRET.search(l) and not SECRET_OK.search(l) for l in text.split('\n')):
                fails.append('R5 %s: %s matches a secret pattern' % (e['id'], f['path']))
            if f.get('kind') == 'excerpt':
                n = sum(b - a + 1 for a, b in f['source']['line_ranges'])
                if len(text.split('\n')) - 1 != n:
                    fails.append('R4 %s: %s has %d lines, ranges name %d' % (e['id'], f['path'], len(text.split('\n')) - 1, n))
        if e.get('kind') == 'complete-as-cited':
            f = e['files'][0]
            if f['sha256'] != e['cited_digest'] or e.get('matches_cited_digest') is not True:
                fails.append('R2 %s: not byte-identical to the cited digest' % e['id'])
        for c in e.get('citations', []):
            p = os.path.join(root, c['path'])
            if not os.path.isfile(p):
                fails.append('R3 %s: citing file %s missing' % (e['id'], c['path']))
                continue
            data = open(p, 'rb').read()
            if blob_id(data) != c['blob']:
                fails.append('R3 %s: citing file %s changed (blob %s, recorded %s)' % (e['id'], c['path'], blob_id(data)[:12], c['blob'][:12]))
            lines = data.decode('utf-8', 'replace').split('\n')
            if c['line'] > len(lines) or c['token'] not in lines[c['line'] - 1]:
                fails.append('R3 %s: %s:%d no longer contains %s' % (e['id'], c['path'], c['line'], c['token'][:16]))
    for dirpath, _, files in os.walk(archive):
        for fn in files:
            rel = os.path.relpath(os.path.join(dirpath, fn), archive).replace(os.sep, '/')
            if '__pycache__' in rel:
                continue
            if rel not in listed and rel not in FIXED:
                fails.append('R6 unlisted file %s' % rel)
    gaps = man.get('missing', [])
    return fails, gaps


def report(archive, root):
    fails, gaps = check(archive, root)
    man = json.load(open(os.path.join(archive, 'manifest.json'), encoding='utf-8'))
    nfiles = sum(len(e.get('files', [])) for e in man['entries'])
    ncites = sum(len(e.get('citations', [])) for e in man['entries'])
    print('RETENTION  %d entries, %d archived files, %d citations' % (len(man['entries']), nfiles, ncites))
    for g in gaps:
        print('GAP  %s' % json.dumps(g, sort_keys=True))
    for f in fails:
        print('FAIL  %s' % f)
    print('RETENTION  %s (%d failure(s), %d gap(s))' % ('HOLDS' if not fails else 'FAILS', len(fails), len(gaps)))
    return 0 if not fails else 1


def self_test(archive, root):
    """Each mutation must be detected; the unmutated copy must pass."""
    man = json.load(open(os.path.join(archive, 'manifest.json'), encoding='utf-8'))
    ok = True
    with tempfile.TemporaryDirectory() as tmp:
        troot = os.path.join(tmp, 'root')
        tarch = os.path.join(troot, 'archive')
        shutil.copytree(archive, tarch, ignore=shutil.ignore_patterns('__pycache__'))
        for e in man['entries']:
            for c in e.get('citations', []):
                dst = os.path.join(troot, c['path'])
                if not os.path.exists(dst):
                    os.makedirs(os.path.dirname(dst), exist_ok=True)
                    shutil.copyfile(os.path.join(root, c['path']), dst)

        def expect(name, mutate, restore, rule=None):
            nonlocal ok
            mutate()
            fails, _ = check(tarch, troot)
            restore()
            good = (not fails) if rule is None else any(f.startswith(rule + ' ') for f in fails)
            ok &= good
            print('%s self: %s%s' % ('PASS' if good else 'FAIL', name, '' if rule is None else ' (%s)' % rule))

        noop = lambda: None
        mp = os.path.join(tarch, 'manifest.json')
        morig = open(mp, 'rb').read()

        def edit_manifest(fn):
            def go():
                m = json.loads(morig)
                fn(m)
                open(mp, 'w', encoding='utf-8').write(json.dumps(m))
            return go
        restore_manifest = lambda: open(mp, 'wb').write(morig)

        expect('unmutated copy passes', noop, noop)
        e0 = next(e for e in man['entries'] if e.get('files'))
        f0 = os.path.join(tarch, e0['files'][0]['path'])
        orig = open(f0, 'rb').read()
        expect('a flipped byte in an archived file', lambda: open(f0, 'wb').write(bytes([orig[0] ^ 1]) + orig[1:]),
               lambda: open(f0, 'wb').write(orig), 'R1')
        expect('a removed archived file', lambda: os.remove(f0), lambda: open(f0, 'wb').write(orig), 'R1')
        cac = next((i for i, e in enumerate(man['entries']) if e.get('kind') == 'complete-as-cited'), None)
        if cac is not None:
            expect('a complete-as-cited entry whose digest differs from the cited one',
                   edit_manifest(lambda m: m['entries'][cac].__setitem__('cited_digest', '0' * 64)), restore_manifest, 'R2')
        c0 = next(c for e in man['entries'] for c in e.get('citations', []))
        cp = os.path.join(troot, c0['path'])
        corig = open(cp, 'rb').read()
        expect('a changed historical record', lambda: open(cp, 'wb').write(corig + b'\n'), lambda: open(cp, 'wb').write(corig), 'R3')
        lines = corig.split(b'\n')

        def drop_token():
            l = lines[:]
            l[c0['line'] - 1] = l[c0['line'] - 1].replace(c0['token'].encode(), b'X' * len(c0['token']))
            open(cp, 'wb').write(b'\n'.join(l))
        expect('a cited token removed from its line', drop_token, lambda: open(cp, 'wb').write(corig), 'R3')
        xi = next(((i, j) for i, e in enumerate(man['entries']) for j, f in enumerate(e.get('files', []))
                   if f.get('kind') == 'excerpt'), None)
        if xi:
            i, j = xi
            expect('an excerpt whose ranges name one more line than it has',
                   edit_manifest(lambda m: m['entries'][i]['files'][j]['source']['line_ranges'].append([10 ** 7, 10 ** 7])),
                   restore_manifest, 'R4')
            xp = os.path.join(tarch, man['entries'][i]['files'][j]['path'])
            xorig = open(xp, 'rb').read()
            expect('a secret pattern in an archived file', lambda: open(xp, 'wb').write(xorig + b'ghp_' + b'A' * 36 + b'\n'),
                   lambda: open(xp, 'wb').write(xorig), 'R5')
        extra = os.path.join(tarch, 'ci', 'unlisted.txt')
        expect('an unlisted file in the archive',
               lambda: (os.makedirs(os.path.dirname(extra), exist_ok=True), open(extra, 'w').write('x')),
               lambda: os.remove(extra), 'R6')
    print('self-test: %s' % ('OK' if ok else 'FAILED'))
    return 0 if ok else 1


if __name__ == '__main__':
    root = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
    if sys.argv[1:] == ['--self-test']:
        sys.exit(self_test(HERE, root))
    if sys.argv[1:]:
        print(__doc__)
        sys.exit(2)
    sys.exit(report(HERE, root))
