#!/usr/bin/env python3
"""legacy_records_check.py -- the records of the rounds landed before V3 are immutable (round V3-13).

Usage:
    python3 tools/legacy_records_check.py <commit>     self-test, then check the commit
    python3 tools/legacy_records_check.py --self-test

The manifest verification/infrastructure/legacy-records.json lists closed namespaces and records,
each a path and a blob. At the commit named, read from git objects and nothing else:

  records     every record is a regular file with its blob: a changed file is `mutated`, a missing
              one `deleted`, one of another mode `mode`;
  closed      every file under a closed namespace is a record: any other is `added`;
  provenance  the manifest's blob is INITIAL, the population round V3-12 measured and round V3-13
              installed, or the manifest's blob at the certified execution head E of a native round
              whose receipt is in the commit's tree, whose receipt holds, and whose frozen
              governed-path block governs the manifest's path by an execution entry that permits
              modification. A change to a legacy record or to the population is a native round's
              governed work; a commit that changes a record and the manifest together fails.

Native rounds' own records are not here: `tools/v3_verifier.py --receipts` keeps them (G13).
Needs full history for the provenance of a changed manifest; the commit must be a full-length
lowercase object id."""
import json
import os
import re
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import v3_verifier as v3  # noqa: E402

MANIFEST = 'verification/infrastructure/legacy-records.json'
INITIAL = '9e48bd31797e1673f03807e699a10ae4a0b960c7'


def load_manifest(raw):
    """(manifest, None) or (None, reason)."""
    try:
        m = json.loads(raw.decode('utf-8'))
    except (ValueError, UnicodeDecodeError):
        return None, 'manifest-unreadable'
    if not isinstance(m, dict) or set(m) != {'schema', 'version', 'closed_namespaces', 'records'} \
            or m['schema'] != 'oi-legacy-records' or m['version'] != 1:
        return None, 'manifest-schema'
    ns, rec = m['closed_namespaces'], m['records']
    if not isinstance(ns, list) or ns != sorted(set(ns)) or not all(
            isinstance(n, str) and n and not n.endswith('/') for n in ns):
        return None, 'manifest-namespaces'
    if not isinstance(rec, dict) or list(rec) != sorted(rec) or not all(
            isinstance(v, str) and re.fullmatch(r'[0-9a-f]{40}', v) for v in rec.values()):
        return None, 'manifest-records'
    return m, None


def under(path, d):
    return path == d or path.startswith(d + '/')


def governs_manifest(repo, r):
    """Whether the round's frozen governed-path block governs the manifest by an execution entry
    that permits modification."""
    pre = [b for b in r['control_plane_blobs'] if b['path'].endswith('/preregistration.md')]
    if len(pre) != 1:
        return False
    text = repo.blob(pre[0]['blob']).decode('utf-8', 'replace')
    entries = v3.parse_governed_text(text)
    if isinstance(entries, str):
        return False
    g = v3.governing(entries, MANIFEST)
    return g is not None and g[0] == 'execution' and 'M' in g[1]


def provenance(repo, c, blob):
    """None when the manifest's blob at C is admitted; a reason otherwise."""
    if blob == INITIAL:
        return None
    for p in sorted(x for x in repo.entries(c) if v3.RECEIPT_PATH.fullmatch(x)):
        out = repo.run(['rev-list', '-n', '1', c, '--', p.decode()])
        q = out.decode().strip() if out else ''
        if not q:
            continue
        r = v3.read_receipt_at(repo, q, p)
        if r is None or r.get('status') != 'complete' or not governs_manifest(repo, r):
            continue
        st = repo.state(r['e'], MANIFEST.encode())
        if st is None or st[1] != blob:
            continue
        verdict, _codes, _att = v3.verify_round(repo, q)
        if verdict == 'HOLDS':
            return None
    return 'manifest-provenance'


def check(repo, c):
    """(ok, lines)."""
    try:
        repo.need(c)
        files = repo.entries(c)
        st = files.get(MANIFEST.encode())
        if st is None:
            return False, ['LEGACY  FAILS  manifest-absent']
        m, why = load_manifest(repo.blob(st[1]))
        if m is None:
            return False, ['LEGACY  FAILS  ' + why]
        lines = []
        for path, blob in m['records'].items():
            got = files.get(path.encode())
            if got is None:
                lines.append('RECORD  %s  deleted' % path)
            elif got[0] != '100644':
                lines.append('RECORD  %s  mode %s' % (path, got[0]))
            elif got[1] != blob:
                lines.append('RECORD  %s  mutated' % path)
        for p in sorted(files):
            path = p.decode('utf-8', 'replace')
            if path not in m['records'] and any(under(path, d) for d in m['closed_namespaces']):
                lines.append('RECORD  %s  added' % path)
        why = provenance(repo, c, st[1])
        if why:
            lines.append('LEGACY  FAILS  ' + why)
    except v3.Undecidable as u:
        return False, ['LEGACY  UNDECIDABLE  %s' % u.code]
    ok = not lines
    lines.append('LEGACY  %d record(s) in %d closed namespace(s), %s' % (
        len(m['records']), len(m['closed_namespaces']), 'all intact' if ok else 'NOT INTACT'))
    return ok, lines


# ---------------------------------------------------------------------------------------------
# self-test: synthetic repositories, each change the check must reject and the ones it must not
# ---------------------------------------------------------------------------------------------
def _manifest(records, ns):
    return (json.dumps({'schema': 'oi-legacy-records', 'version': 1, 'closed_namespaces': ns,
                        'records': dict(sorted(records.items()))}, indent=1) + '\n').encode()


def _round_case(sc, blobs, governed, holds=True):
    """A native round from B that rewrites a record and the manifest; the check at its receipt
    commit. `holds` False records a wrong execution delta digest, so the receipt does not hold."""
    tag = ('G' if governed else 'N') + ('' if holds else 'X')
    rd = 'verification/infrastructure/round-ex-%s/' % tag.lower()
    block = ['record AM ' + rd, 'record AM verification/receipts/EX-%s.json' % tag,
             'execution M old/round-a/preregistration.md']
    if governed:
        block.append('execution M ' + MANIFEST)
    pre = ('# EX-%s\n\n```v3-round\nround EX-%s\nkind non-sealing\nrecord-directory %s\n```\n\n'
           '```v3-governed-paths\n%s\n```\n' % (tag, tag, rd, '\n'.join(block)))
    new_blob = sc.git(['hash-object', '-w', '--stdin'], data=b'repaired\n').decode().strip()
    sc.commit(tag + 'F', ['B'], 'B', {(rd + 'preregistration.md').encode(): ('100644',
                                                                          pre.encode())}, [])
    sc.commit(tag + 'E', [tag + 'F'], tag + 'F', {
        b'old/round-a/preregistration.md': ('100644', b'repaired\n'),
        MANIFEST.encode(): ('100644', _manifest(dict(blobs, **{
            'old/round-a/preregistration.md': new_blob}), ['old/round-a', 'old/seals']))}, [])
    sc.commit(tag + 'L', ['B', tag + 'E'], tag + 'E', {}, [])
    receipt = {
        'schema': 'v3-receipt', 'version': 1, 'round': 'EX-' + tag, 'status': 'complete',
        'kind': 'non-sealing', 'object_format': 'sha1', 'd': '{{sha:B}}', 'f': '{{sha:%sF}}' % tag,
        'control_plane_blobs': [{'path': rd + 'preregistration.md',
                                 'blob': '{{blob:%sF|%spreregistration.md}}' % (tag, rd)}],
        'governed_paths_digest': '{{gpd:%sF|%spreregistration.md}}' % (tag, rd),
        'e': '{{sha:%sE}}' % tag, 'tree_e': '{{tree:%sE}}' % tag,
        'execution_delta_digest': '{{delta:%sF|%sE}}' % (tag, tag) if holds else '0' * 64,
        'candidates': [],
        'landing': {'base': '{{sha:B}}', 'object': '{{sha:%sL}}' % tag,
                    'reconciliations': ['{{sha:%sL}}' % tag], 'resolved_paths': [],
                    'delta_digest': '{{delta:B|%sL}}' % tag},
        'attestations': [{'kind': k, 'subject': s_, 'commit': '{{sha:%s%s}}' % (tag, s_),
                          'record': 'r'} for s_ in ('F', 'E')
                         for k in ('owner-designation', 'check-run')]}
    sc.commit(tag + 'Q', [tag + 'L'], tag + 'L', {
        ('verification/receipts/EX-%s.json' % tag).encode(): v3.content({'json': receipt}, sc)},
        [])
    ok, _lines = check(sc.repo, sc.labels[tag + 'Q'])
    return ok


def self_test():
    fails = []
    with tempfile.TemporaryDirectory() as td:
        sc = v3.Scratch(os.path.join(td, 'r'))
        rec = {'old/round-a/preregistration.md': b'frozen\n', 'old/seals/A.json': b'{}\n'}
        blobs = {p: sc.git(['hash-object', '-w', '--stdin'], data=b).decode().strip()
                 for p, b in rec.items()}
        base = {p.encode(): ('100644', b) for p, b in rec.items()}
        base[b'live.md'] = ('100644', b'live\n')
        global INITIAL
        saved = INITIAL
        man = _manifest(blobs, ['old/round-a', 'old/seals'])
        INITIAL = sc.git(['hash-object', '--stdin'], data=man).decode().strip()
        base[MANIFEST.encode()] = ('100644', man)
        try:
            sc.commit('B', [], None, base, [])
            cases = [
                ('intact', {}, [], True),
                ('live file changed', {b'live.md': ('100644', b'x\n')}, [], True),
                ('record mutated', {b'old/round-a/preregistration.md': ('100644', b'x\n')}, [],
                 False),
                ('record deleted', {}, [b'old/seals/A.json'], False),
                ('record mode', {b'old/seals/A.json': ('100755', b'{}\n')}, [], False),
                ('file added to a closed namespace', {b'old/round-a/extra.md': ('100644', b'x\n')},
                 [], False),
                ('record and manifest changed together, no round',
                 {b'old/round-a/preregistration.md': ('100644', b'x\n'),
                  MANIFEST.encode(): ('100644', _manifest(dict(blobs, **{
                      'old/round-a/preregistration.md': sc.git(
                          ['hash-object', '-w', '--stdin'], data=b'x\n').decode().strip()}),
                      ['old/round-a', 'old/seals']))}, [], False),
            ]
            for i, (name, sets, dels, want) in enumerate(cases):
                sc.commit('C%d' % i, ['B'], 'B', sets, dels)
                ok, _lines = check(sc.repo, sc.labels['C%d' % i])
                if ok != want:
                    fails.append(name)
            # a native round that governs the manifest changes a record and the population
            # together: admitted once its receipt holds; the same round without the manifest in
            # its governed paths is not, and neither is the governing round whose receipt fails
            for governed, holds, want in ((True, True, True), (False, True, False),
                                          (True, False, False)):
                if not _round_case(sc, blobs, governed, holds) is want:
                    fails.append('native round, manifest %sgoverned, receipt %s' % (
                        '' if governed else 'not ', 'holding' if holds else 'failing'))
            # the manifest's own schema
            for name, raw in (('unsorted records', b'{"schema": "oi-legacy-records", "version": 1, '
                               b'"closed_namespaces": [], "records": {"b": "' + b'1' * 40 +
                               b'", "a": "' + b'1' * 40 + b'"}}'),
                              ('unknown field', b'{"schema": "oi-legacy-records", "version": 1, '
                               b'"closed_namespaces": [], "records": {}, "extra": 1}')):
                if load_manifest(raw)[0] is not None:
                    fails.append('schema: ' + name)
        finally:
            INITIAL = saved
    for f in fails:
        print('SELF-TEST  FAIL  %s' % f)
    print('legacy_records_check: self-test %s' % ('OK' if not fails else 'FAILED'))
    return not fails


def main(argv):
    if argv == ['--self-test']:
        return 0 if self_test() else 1
    if len(argv) != 1:
        print(__doc__.split('\n\n')[1])
        return 2
    try:
        c = v3.check_oid(argv[0])
    except v3.Refused as rf:
        print('legacy_records_check: refused (%s)' % rf.code)
        return 2
    if not self_test():
        return 1
    ok, lines = check(v3.Repo(os.getcwd()), c)
    print('\n'.join(lines))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
