#!/usr/bin/env python3
"""citation_roles_check.py -- commit ids a record offers as support are reachable (AGENTS §A.42).

Usage:
    python3 tools/citation_roles_check.py <commit>     self-test, then check the commit
    python3 tools/citation_roles_check.py --self-test

Scope. A record opts in by carrying a manifest, `CITATIONS.json`, in its directory. The manifest
covers every file under that directory, subdirectories included, and nothing else; a directory
without one is not read. Records that keep their own form are never covered: a manifest whose
covered tree meets a record or closed namespace of verification/infrastructure/legacy-records.json,
verification/receipts/, verification/seals/ or a native round's record directory (from the
receipts in the tree) fails as `frozen-scope`, and a manifest whose tree holds another manifest
fails as `nested-manifest`.

Manifest:

    {"schema": "oi-citations", "version": 1,
     "ids": {"<40 lowercase hex>": "support" | "provenance" | "external", ...}}

with exactly those three fields and the ids in sorted order. The role is the author's declaration
and is never inferred. `external` is an object of another repository, such as the commit a pinned
workflow action names; it is not looked up here, and it cannot be support.

Ids. Every run of exactly 40 lowercase hexadecimal characters, bounded by non-hexadecimal
characters, in a covered file is an object id the record cites: a commit, or a blob or tree id. A
64-hex run (a SHA-256 digest) is not one, and neither is an abbreviated id. A `support` id must
name a commit; a blob or tree id is cited as `provenance`, and its claim is supported by the
commit that holds it.

At the commit under check, read from git objects and nothing else, a manifest fails when:

  malformed           it is not the manifest above;
  unlisted            a covered file cites an id the manifest does not list;
  unused              the manifest lists an id no covered file cites;
  absent              an id names no object in the repository: checked for every `support` id,
                      and for a `provenance` id when it lands, i.e. when main's copy of the same
                      manifest does not list it;
  support-not-commit  a `support` id names a blob or tree;
  support-unreachable a `support` id names a commit not reachable from the commit under check;
  external-in-repository  an `external` id names an object of this repository.

Main is refs/remotes/origin/main, else refs/heads/main; with neither, every id is checked as
landing. Reachability needs full history: a shallow repository is undecidable and fails."""
import json
import os
import re
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import v3_verifier as v3  # noqa: E402
import legacy_records_check as lr  # noqa: E402

NAME = b'CITATIONS.json'
ROLES = ('support', 'provenance', 'external')
PROTECTED = (b'verification/receipts', b'verification/seals')
MAIN_REFS = ('refs/remotes/origin/main', 'refs/heads/main')
OBJECT_ID = re.compile(rb'(?<![0-9A-Fa-f])[0-9a-f]{40}(?![0-9A-Fa-f])')


def load(raw):
    """{id: role}, or None when the manifest is malformed."""
    try:
        pairs = []
        m = json.loads(raw.decode('utf-8'),
                       object_pairs_hook=lambda kv: pairs.append(kv) or dict(kv))
    except (ValueError, UnicodeDecodeError):
        return None
    if any(len({k for k, _ in kv}) != len(kv) for kv in pairs):
        return None
    if not isinstance(m, dict) or set(m) != {'schema', 'version', 'ids'} \
            or m['schema'] != 'oi-citations' or m['version'] != 1 or type(m['version']) is not int:
        return None
    ids = m['ids']
    if not isinstance(ids, dict) or list(ids) != sorted(ids) or not all(
            isinstance(k, str) and re.fullmatch(r'[0-9a-f]{40}', k) and v in ROLES
            for k, v in ids.items()):
        return None
    return ids


def main_commit(repo):
    for ref in MAIN_REFS:
        out = repo.run(['rev-parse', '--verify', '-q', ref + '^{commit}'])
        if out:
            return out.decode().strip()
    return None


def protected(repo, files):
    """(directories, files) whose records keep their own form."""
    dirs, recs = set(PROTECTED), set()
    st = files.get(lr.MANIFEST.encode())
    if st is not None:
        m, why = lr.load_manifest(repo.blob(st[1]))
        if m is None:
            raise v3.Undecidable('legacy-' + why)
        dirs.update(n.encode() for n in m['closed_namespaces'])
        recs.update(p.encode() for p in m['records'])
    for p, (_mode, obj) in files.items():
        if not v3.RECEIPT_PATH.fullmatch(p):
            continue
        try:
            r = json.loads(repo.blob(obj).decode('utf-8'))
            dirs.update(b['path'].encode()[:-len('/preregistration.md')]
                        for b in r['control_plane_blobs']
                        if b['path'].endswith('/preregistration.md'))
        except (ValueError, UnicodeDecodeError, KeyError, TypeError, AttributeError):
            continue          # a receipt that does not parse fails v3-receipts, not here
    return dirs, recs


def object_type(repo, oid):
    out = repo.run(['cat-file', '-t', oid])
    return out.decode().strip() if out else None


def check(repo, c, main=None):
    """(problems, manifests, ids): problems is a list of (manifest, code, id, file)."""
    if repo.width() != 40:
        raise v3.Undecidable('object-format')
    repo.need(c)
    files = repo.entries(c)
    manifests = sorted(p for p in files if p == NAME or p.endswith(b'/' + NAME))
    if not manifests:
        return [], 0, 0
    pdirs, precs = protected(repo, files)
    main_files = repo.entries(main) if main else {}
    out, n_ids = [], 0
    for mp in manifests:
        d = mp[:-len(NAME)]                     # b'' or b'dir/'
        name = mp.decode('utf-8', 'replace')
        if any((p + b'/').startswith(d) or d.startswith(p + b'/')
               for p in pdirs) or any(r.startswith(d) for r in precs):
            out.append((name, 'frozen-scope', '', ''))
            continue
        if any(o != mp and o.startswith(d) for o in manifests):
            out.append((name, 'nested-manifest', '', ''))
            continue
        ids = load(repo.blob(files[mp][1]))
        if ids is None:
            out.append((name, 'malformed', '', ''))
            continue
        n_ids += len(ids)
        cited = {}
        for p in sorted(files):
            mode, obj = files[p]
            if p == mp or not p.startswith(d) or mode == '160000':
                continue
            for tok in OBJECT_ID.findall(repo.blob(obj)):
                cited.setdefault(tok.decode(), p.decode('utf-8', 'replace'))
        landed = {}
        if mp in main_files:
            landed = load(repo.blob(main_files[mp][1])) or {}
        for oid in sorted(set(cited) - set(ids)):
            out.append((name, 'unlisted', oid, cited[oid]))
        for oid in sorted(set(ids) - set(cited)):
            out.append((name, 'unused', oid, ''))
        for oid, role in ids.items():
            if role == 'provenance' and landed.get(oid) == 'provenance':
                continue
            t = object_type(repo, oid)
            if role == 'external':
                if t is not None:
                    out.append((name, 'external-in-repository', oid, cited.get(oid, '')))
            elif t is None:
                out.append((name, 'absent', oid, cited.get(oid, '')))
            elif role == 'support' and t != 'commit':
                out.append((name, 'support-not-commit', oid, cited.get(oid, '')))
            elif role == 'support' and not repo.is_ancestor(oid, c):
                out.append((name, 'support-unreachable', oid, cited.get(oid, '')))
    return out, len(manifests), n_ids


# ---------------------------------------------------------------------------------------------
# self-test: synthetic repositories; each mutant must fail with its target code and no other
# ---------------------------------------------------------------------------------------------
def verdict(target, codes):
    """A mutant is killed only when the check fails with its target code and nothing else."""
    codes = set(codes)
    if codes == {target}:
        return 'killed'
    if target in codes:
        return 'unclean'
    return 'survived'


def _manifest(ids):
    return (json.dumps({'schema': 'oi-citations', 'version': 1,
                        'ids': dict(sorted(ids.items()))}, indent=1) + '\n').encode()


def self_test():
    fails = []
    # live controls on the classifier, before any mutant is scored by it
    for target, codes, want in (('t', ['t'], 'killed'), ('t', ['t', 't'], 'killed'),
                                ('t', [], 'survived'), ('t', ['u'], 'survived'),
                                ('t', ['t', 'u'], 'unclean')):
        if verdict(target, codes) != want:
            fails.append('classifier: %s on %s' % (want, codes))
    with tempfile.TemporaryDirectory() as td:
        sc = v3.Scratch(os.path.join(td, 'r'))
        lone = sc.git(['hash-object', '-w', '--stdin'], data=b'lone\n').decode().strip()
        legacy = (json.dumps({'schema': 'oi-legacy-records', 'version': 1,
                              'closed_namespaces': ['old/round-a'],
                              'records': {'lone/r.md': lone}}) + '\n').encode()
        receipt = json.dumps({'control_plane_blobs': [
            {'path': 'prog/round-r/preregistration.md', 'blob': '0' * 40}]}).encode()
        sc.commit('M0', [], None, {
            b'base.txt': ('100644', b'base\n'),
            lr.MANIFEST.encode(): ('100644', legacy),
            b'old/round-a/r.md': ('100644', b'frozen\n'),
            b'lone/r.md': ('100644', b'lone\n'),
            b'verification/receipts/R-1.json': ('100644', receipt),
            b'prog/round-r/preregistration.md': ('100644', b'round\n')}, [])
        sc.commit('S', ['M0'], 'M0', {b'side.txt': ('100644', b'side\n')}, [])   # off main
        m0, s = sc.labels['M0'], sc.labels['S']
        blob = sc.repo.state(m0, b'base.txt')[1]
        gone, gone2 = 'ab' * 20, 'cd' * 20
        sc.git(['update-ref', 'refs/heads/main', m0])

        def codes(c, main):
            try:
                return {code for _m, code, _i, _f in check(sc.repo, c, main)[0]}
            except v3.Undecidable as u:     # a crash is a failure of the test, not a kill
                return {u.code}

        def case(label, sets, main=m0, parent='M0'):
            sc.commit(label, [parent], parent, sets, [])
            return codes(sc.labels[label], main)

        def rec(text, ids, extra=None):
            sets = {b'rec/NOTE.md': ('100644', text.encode()),
                    b'rec/CITATIONS.json': ('100644', _manifest(ids) if isinstance(ids, dict)
                                            else ids)}
            sets.update(extra or {})
            return sets

        good_text = ('support %s; provenance %s; blob %s; sha-256 %s; upper %s; short %s; '
                     'mixed-case run %s\n' % (m0, s, blob, 'e' * 64, gone.upper(), s[:12],
                                                'D' + gone))
        good_ids = {m0: 'support', s: 'provenance', blob: 'provenance'}
        positives = [
            ('positive fixture', rec(good_text, good_ids)),
            ('off-main id cited as provenance', rec('see %s\n' % s, {s: 'provenance'})),
            ('another repository\'s commit cited as external',
             rec('uses: actions/checkout@%s\n' % gone, {gone: 'external'})),
            ('ids in a subdirectory file', rec('x\n', {m0: 'support'}, {
                b'rec/sub/data.json': ('100644', ('{"c": "%s"}\n' % m0).encode())})),
            ('no manifest: not read', {b'other/NOTE.md': ('100644', ('%s\n' % gone).encode())}),
        ]
        for name, sets in positives:
            got = case('P-' + name, sets)
            if got:
                fails.append('%s: expected pass, got %s' % (name, sorted(got)))

        mutants = [
            ('off-main id cited as support', 'support-unreachable',
             rec('see %s\n' % s, {s: 'support'})),
            ('missing object as provenance', 'absent',
             rec('see %s\n' % gone, {gone: 'provenance'})),
            ('missing object as support', 'absent', rec('see %s\n' % gone, {gone: 'support'})),
            ('this repository\'s commit cited as external', 'external-in-repository',
             rec('see %s\n' % s, {s: 'external'})),
            ('blob as support', 'support-not-commit', rec('see %s\n' % blob, {blob: 'support'})),
            ('unlisted id', 'unlisted', rec('see %s and %s\n' % (m0, s), {m0: 'support'})),
            ('unlisted id in a subdirectory file', 'unlisted',
             rec('see %s\n' % m0, {m0: 'support'},
                 {b'rec/sub/x.out': ('100644', ('run at %s\n' % s).encode())})),
            ('unused id', 'unused', rec('see %s\n' % m0, {m0: 'support', s: 'provenance'})),
            ('malformed: not json', 'malformed', rec('x\n', b'{"schema": \n')),
            ('malformed: unknown role', 'malformed', rec('see %s\n' % m0, {m0: 'evidence'})),
            ('malformed: unknown field', 'malformed', rec('x\n', b'{"schema": "oi-citations", '
                                                          b'"version": 1, "ids": {}, "x": 1}')),
            ('malformed: version 2', 'malformed', rec('x\n', b'{"schema": "oi-citations", '
                                                      b'"version": 2, "ids": {}}')),
            ('malformed: version true', 'malformed', rec('x\n', b'{"schema": "oi-citations", '
                                                         b'"version": true, "ids": {}}')),
            ('malformed: unsorted ids', 'malformed', rec('%s %s\n' % (m0, s), (
                '{"schema": "oi-citations", "version": 1, "ids": {"%s": "support", '
                '"%s": "support"}}' % tuple(sorted([m0, s], reverse=True))).encode())),
            ('malformed: duplicate id', 'malformed', rec('%s\n' % m0, (
                '{"schema": "oi-citations", "version": 1, "ids": {"%s": "provenance", '
                '"%s": "support"}}' % (m0, m0)).encode())),
            ('malformed: short id', 'malformed', rec('x\n', ('{"schema": "oi-citations", '
                                                     '"version": 1, "ids": {"%s": "support"}}'
                                                     % m0[:12]).encode())),
            ('nested manifest', 'nested-manifest', rec('see %s\n' % m0, {m0: 'support'}, {
                b'rec/sub/CITATIONS.json': ('100644', _manifest({}))})),
            ('manifest over a native round record', 'frozen-scope', {
                b'prog/CITATIONS.json': ('100644', _manifest({}))}),
            ('manifest over a legacy closed namespace', 'frozen-scope', {
                b'old/CITATIONS.json': ('100644', _manifest({}))}),
            ('manifest over a legacy record', 'frozen-scope', {
                b'lone/CITATIONS.json': ('100644', _manifest({}))}),
            ('manifest inside a legacy closed namespace', 'frozen-scope', {
                b'old/round-a/sub/CITATIONS.json': ('100644', _manifest({}))}),
        ]
        results = {}
        for name, target, sets in mutants:
            got = case('X-' + name, sets)
            results[name] = got
            v = verdict(target, got)
            if v != 'killed':
                fails.append('%s: %s (target %s, got %s)' % (name, v, target, sorted(got)))

        # negative control: an unrelated failure is not a kill of the support-reachability mutant
        if verdict('support-unreachable', results['malformed: unknown role']) != 'survived':
            fails.append('negative control: an unrelated failure was counted as a kill')

        # landing: a provenance id is checked for existence when it lands, not after; an id main
        # already lists stays admitted once its object is gone (e.g. its branch deleted)
        sc.commit('L', ['M0'], 'M0', rec('see %s\n' % gone2, {gone2: 'provenance'}), [])
        lid = sc.labels['L']
        for name, main, want in (('landing', m0, {'absent'}), ('landed, main at it', lid, set()),
                                 ('no main ref given', None, {'absent'})):
            got = codes(lid, main)
            if got != want:
                fails.append('%s: expected %s, got %s' % (name, sorted(want), sorted(got)))
        got = case('L2', {b'rec/more.md': ('100644', b'more\n')}, main=lid, parent='L')
        if got:
            fails.append('after landing: expected pass, got %s' % sorted(got))
        got = case('L3', rec('see %s\n' % gone2, {gone2: 'support'}), main=lid, parent='L')
        if got != {'absent'}:
            fails.append('landed id re-declared support: expected absent, got %s' % sorted(got))
    for f in fails:
        print('SELF-TEST  FAIL  %s' % f)
    print('citation_roles_check: self-test %s (%d mutants, %d positives)' % (
        'OK' if not fails else 'FAILED', len(mutants), len(positives)))
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
        print('citation_roles_check: refused (%s)' % rf.code)
        return 2
    if not self_test():
        return 1
    repo = v3.Repo(os.getcwd())
    try:
        main_c = main_commit(repo)
        problems, n_man, n_ids = check(repo, c, main_c)
    except v3.Undecidable as u:
        print('CITATIONS  UNDECIDABLE  %s' % u.code)
        return 1
    for m, code, oid, f in problems:
        print('CITATION  %s  %s  %s  %s' % (m, code, oid, f))
    if main_c is None:
        print('CITATIONS  no main ref: every provenance id checked as landing')
    print('CITATIONS  %d manifest(s), %d id(s), %s' % (
        n_man, n_ids, 'all hold' if not problems else '%d problem(s)' % len(problems)))
    return 0 if not problems else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
