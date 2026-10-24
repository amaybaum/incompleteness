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

    {"schema": "oi-citations", "version": 2, "ids": {
      "<40 lowercase hex>": {"role": "support",    "claim": "<path>:<line>",
                             "claim_sha256": "<64 lowercase hex>"},
      "<40 lowercase hex>": {"role": "provenance", "reason": "<why it is not load-bearing>"},
      "<40 lowercase hex>": {"role": "external",   "repository": "<owner>/<repo>"}},
     "retired": {"<40 lowercase hex>": <downgrade record>}}

with exactly those fields, `retired` optional and non-empty when present, the ids of each map
in sorted order and none in both, and each entry carrying exactly its role and that role's
fields, each a non-empty string; a `provenance` or `external` entry may also carry a
`downgrade` record (below). Roles are the author's declaration and are never inferred;
each entry states something a reviewer can check:

  support     `claim` is a repository path under the manifest's directory, other than the
              manifest, and a line of that file on which the id appears: the claim it supports.
              `claim_sha256` is the SHA-256 of that line's normalized text (runs of ASCII
              whitespace collapsed to one space, the ends trimmed). The hash is an integrity aid
              for the line `claim` names; the claim is identified by `claim`, never by its hash.
  provenance  `reason` says why the id is historical and not load-bearing.
  external    `repository` names the other repository the object belongs to (not this one), and
              every occurrence of the id in a covered file names it: immediately preceded by
              `<owner>/<repo>@`, or inside a URL `https://github.com/<owner>/<repo>/.../<id>`.

Downgrades. A downgrade record is

    {"from_claim": "<path>:<line>", "from_claim_sha256": "<64 lowercase hex>",
     "reason": "<why the claim was removed or narrowed>"}

and matches a support entry whose `claim` and `claim_sha256` it repeats. Against main (every
manifest main's tree has, at any path):

  - a support id of main that no manifest of the commit lists as `support` needs a matching
    record in some manifest of the commit: as the `downgrade` of the entry that now lists it, or
    under `retired` when no entry does, whether or not the id is still cited;
  - an entry of the commit that lists such an id as `provenance` or `external` needs a matching
    `downgrade` of its own, unless main's copy of that manifest already lists it so;
  - such an id's claim must not stand anywhere in the commit's tree: no line, in any file,
    covered or not, may hash to its `claim_sha256`, or match main's claimed line once every run
    of 7 or more hexadecimal characters is removed and the text case-folded (so abbreviating,
    uppercasing or deleting the id leaves the claim unchanged);
  - a support id of main that some manifest of the commit still lists as `support` needs no
    record, but main's claim of it may stand, in that loose sense, only on lines that still
    carry the id: a claim kept while its reference is deleted, abbreviated or uppercased fails,
    wherever the id is still declared support.

The baseline is therefore every support declaration of every manifest of main's tree, whatever
directory or manifest held it, so a manifest removed, renamed or split, or an id deleted from
its claim, cannot carry a dependency away unrecorded.

Independently of main, a record fails while any line of the tree hashes to its
`from_claim_sha256`. Each failure is `support-downgrade`. A genuine rewording or removal of the
claim with a matching record passes, by design: the record is the reviewable statement of what
became of the claim. No syntactic checker can reliably decide whether an arbitrarily rewritten
claim means the same as the one it replaced: these controls catch the known structural evasions,
and independent review still decides whether a downgrade is scientifically justified.

Ids. Every run of exactly 40 lowercase hexadecimal characters, bounded by non-hexadecimal
characters, in a covered file is an object id the record cites: a commit, or a blob or tree id. A
64-hex run (a SHA-256 digest) is not one, and neither is an abbreviated id. A `support` id must
name a commit; a blob or tree id is cited as `provenance`, and its claim is supported by the
commit that holds it.

At the commit under check, read from git objects and nothing else, a manifest fails when:

  malformed               it is not the manifest above;
  unlisted                a covered file cites an id the manifest does not list;
  unused                  the manifest lists an id no covered file cites;
  claim-outside           a support claim names a path outside the manifest's directory, or the
                          manifest itself;
  claim-file-absent       a support claim names a file the commit does not have;
  claim-line-mismatch     the claimed line does not exist or does not carry the id;
  claim-hash-mismatch     the claimed line's normalized text does not hash to `claim_sha256`;
  support-downgrade       a support id of main is listed as support by no manifest of the
                          commit without a matching record, or its claim, or a record's claim,
                          still stands (Downgrades, above);
  absent                  an id names no object in the repository: checked for every `support`
                          id, and for a `provenance` id when it lands, i.e. when main's copy of
                          the same manifest does not list it as provenance;
  support-not-commit      a `support` id names a blob, tree or tag;
  support-unreachable     a `support` id names a commit not reachable from the commit under
                          check (a commit the change under review adds is reachable);
  external-this-repository  an `external` entry names this repository;
  external-unqualified    an occurrence of an `external` id does not name its declared repository;
  external-in-repository  an `external` id names an object of this repository.

Main is refs/remotes/origin/main, else refs/heads/main; with neither, every id is checked as
landing. Reachability needs full history: a shallow repository is undecidable and fails.

Limitations:
  - Uppercase and abbreviated ids are not read, although git resolves both.
  - Every covered file is scanned as bytes, binary or NUL-containing files included, so an id
    inside a compressed or UTF-16 file is not seen. A symlink is scanned as its target path, not
    the target file; a submodule entry is not scanned.
  - `external-in-repository` is checked on every build, so an external object that later enters
    this repository turns main red until the manifest is corrected.
  - A provenance id's existence, and every downgrade, is checked against a main that lacks the
    change, i.e. in pull-request CI; a commit that reaches main without pull-request CI is
    compared against itself and skips both. With no main ref, nothing is compared, and only the
    test that a record's claim does not stand by its normalized hash runs.
  - An id some manifest of the commit still lists as `support` needs no record, so a claim of it
    reworded beyond its ids, the reference dropped, passes while the id stays declared support
    on another line; its reachability is still checked there.
  - A record may sit in any manifest of the commit, so removing every manifest of the tree
    leaves nowhere to record a downgrade, and such a commit fails.
  - An unrelated record that newly lists a downgraded support id as provenance needs a
    `downgrade` record of its own.
  - The loose comparison uses main's claimed line, so it runs only against main; a claim line
    that is nothing but ids and whitespace has no loose form and is compared by its hash alone.
    A rewording beyond the ids, with a matching record, passes. An unrelated line that matches a
    claim loosely (the same words around another id) is taken for the claim.
  - Lines inserted above a claim shift it: the entry then fails as `claim-line-mismatch` or
    `claim-hash-mismatch`, depending on what the claimed line now holds, until it is updated.
  - THIS_REPOSITORY is a constant: in a fork or after a rename it must be edited, or an external
    entry naming the new name is not refused as this repository (external-in-repository still
    refuses an object this repository holds).
  - When main has a support entry or the commit a record, the check reads and hashes every
    line of the tree once (one `git cat-file --batch`; several seconds on this repository's
    tree). The self-test takes about 10 s and runs before every check.
  - A 40-hex value that names no git object of any repository (a SHA-1 file digest) has no role.
  - The checker forces a reviewable statement per id; whether a reason is honest, or a claim
    really rests on its id, is for review."""
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import v3_verifier as v3  # noqa: E402
import legacy_records_check as lr  # noqa: E402

NAME = b'CITATIONS.json'
FIELDS = {'support': ('claim', 'claim_sha256'), 'provenance': ('reason',),
          'external': ('repository',)}
DOWNGRADE = ('from_claim', 'from_claim_sha256', 'reason')
SHA256 = re.compile(r'[0-9a-f]{64}')
HEX_RUN = re.compile(rb'[0-9A-Fa-f]{7,}')
THIS_REPOSITORY = 'amaybaum/incompleteness'
PROTECTED = (b'verification/receipts', b'verification/seals')
MAIN_REFS = ('refs/remotes/origin/main', 'refs/heads/main')
OBJECT_ID = re.compile(rb'(?<![0-9A-Fa-f])[0-9a-f]{40}(?![0-9A-Fa-f])')
CLAIM = re.compile(r'([^:\0]+):([1-9][0-9]*)')
REPOSITORY = re.compile(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+')
NAME_CHARS = rb'[A-Za-z0-9_.-]+'
QUALIFIERS = (re.compile(rb'(?<![A-Za-z0-9_.-])(' + NAME_CHARS + rb')/(' + NAME_CHARS + rb')@\Z'),
              re.compile(rb'https://github\.com/(' + NAME_CHARS + rb')/(' + NAME_CHARS +
                         rb')/[^\s"\'<>()\[\]`]*\Z'))


def repository_name(name):
    name = name.lower()
    return name[:-4] if name.endswith('.git') else name


def qualifier(data, start):
    """The `owner/repo` an id occurrence at `start` names, normalized, or None."""
    before = data[max(0, start - 512):start]
    for rx in QUALIFIERS:
        m = rx.search(before)
        if m:
            return repository_name((m.group(1) + b'/' + m.group(2)).decode())
    return None


def line_sha256(line):
    """SHA-256 of a line's normalized text: ASCII whitespace runs collapsed, the ends trimmed."""
    return hashlib.sha256(b' '.join(line.split())).hexdigest()


def _text(v):
    return isinstance(v, str) and bool(v.strip())


def _downgrade_ok(dg):
    return isinstance(dg, dict) and set(dg) == set(DOWNGRADE) \
        and all(_text(dg[f]) for f in DOWNGRADE) and bool(CLAIM.fullmatch(dg['from_claim'])) \
        and bool(SHA256.fullmatch(dg['from_claim_sha256']))


def load(raw):
    """({id: entry}, {retired id: record}), or None when the manifest is malformed."""
    try:
        pairs = []
        m = json.loads(raw.decode('utf-8'),
                       object_pairs_hook=lambda kv: pairs.append(kv) or dict(kv))
    except (ValueError, UnicodeDecodeError):
        return None
    if any(len({k for k, _ in kv}) != len(kv) for kv in pairs):
        return None
    if not isinstance(m, dict) or not {'schema', 'version', 'ids'} <= set(m) \
            or set(m) - {'schema', 'version', 'ids', 'retired'} \
            or m['schema'] != 'oi-citations' or m['version'] != 2 or type(m['version']) is not int:
        return None
    ids, retired = m['ids'], m.get('retired', {})
    for keyed in (ids, retired):
        if not isinstance(keyed, dict) or list(keyed) != sorted(keyed) or not all(
                isinstance(k, str) and re.fullmatch(r'[0-9a-f]{40}', k) for k in keyed):
            return None
    if 'retired' in m and not retired or set(ids) & set(retired) \
            or not all(_downgrade_ok(r) for r in retired.values()):
        return None
    out = {}
    for k, e in ids.items():
        role = e.get('role') if isinstance(e, dict) else None
        fields = FIELDS.get(role) if isinstance(role, str) else None
        if fields is None:
            return None
        extra = set(e) - {'role'} - set(fields)
        if not set(fields) <= set(e) or not all(_text(e[f]) for f in fields) \
                or extra - ({'downgrade'} if role != 'support' else set()):
            return None
        if role == 'support' and not (CLAIM.fullmatch(e['claim'])
                                      and SHA256.fullmatch(e['claim_sha256'])):
            return None
        if role == 'external' and not REPOSITORY.fullmatch(e['repository']):
            return None
        if 'downgrade' in e and not _downgrade_ok(e['downgrade']):
            return None
        out[k] = dict(e)
    return out, {k: dict(r) for k, r in retired.items()}


def manifest_paths(files):
    return sorted(p for p in files if p == NAME or p.endswith(b'/' + NAME))


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


def claim_problem(repo, files, d, mp, entry, oid):
    """None when `path:line` names a covered file whose line carries the id and hashes to
    `claim_sha256`; else the code."""
    path, line = CLAIM.fullmatch(entry['claim']).groups()
    p = path.encode()
    if not p.startswith(d) or p == mp or any(s in (b'', b'.', b'..') for s in p.split(b'/')):
        return 'claim-outside'
    if p not in files or files[p][0] == '160000':
        return 'claim-file-absent'
    lines = repo.blob(files[p][1]).split(b'\n')
    n = int(line)
    if n > len(lines) or oid.encode() not in OBJECT_ID.findall(lines[n - 1]):
        return 'claim-line-mismatch'
    if line_sha256(lines[n - 1]) != entry['claim_sha256']:
        return 'claim-hash-mismatch'
    return None


def loose_sha256(line):
    """SHA-256 of a line's text with every run of 7 or more hexadecimal characters removed, then
    case-folded and whitespace-normalized: the claim whatever became of the ids on it."""
    text = HEX_RUN.sub(b'', line).decode('utf-8', 'replace').casefold()
    return hashlib.sha256(' '.join(text.split()).encode()).hexdigest()


EMPTY_LOOSE = loose_sha256(b'')


class TreeLines:
    """Where the lines of the commit's tree that hash to the given normalized or loose hashes
    stand, from every blob of the tree read in one `git cat-file --batch`; each distinct line is
    hashed once."""

    def __init__(self, repo, files, strict, loose):
        self.strict_at, self.loose_at = {h: [] for h in strict}, \
            {h: [] for h in loose if h != EMPTY_LOOSE}
        if not self.strict_at and not self.loose_at:
            return
        paths = [(p, obj) for p, (mode, obj) in sorted(files.items()) if mode != '160000']
        r = subprocess.run(['git', 'cat-file', '--batch'], cwd=repo.cwd, env=v3.GIT_ENV,
                           input=''.join(obj + '\n' for _p, obj in paths).encode(),
                           capture_output=True)
        if r.returncode != 0:
            raise v3.Undecidable('undecidable:object-absent')
        seen, out, at = {}, r.stdout, 0
        for p, obj in paths:
            nl = out.index(b'\n', at)
            head = out[at:nl].split()
            if len(head) != 3 or head[0].decode() != obj:
                raise v3.Undecidable('undecidable:object-absent')
            size = int(head[2])
            data, at = out[nl + 1:nl + 1 + size], nl + 2 + size
            for i, line in enumerate(data.split(b'\n')):
                hit = seen.get(line)
                if hit is None:
                    hit = seen[line] = (self.strict_at.get(line_sha256(line)),
                                        self.loose_at.get(loose_sha256(line)))
                for lst in hit:
                    if lst is not None:
                        lst.append((p, i + 1, line))

    def strict(self, sha):
        """[(path, line number, text)] of the lines with this normalized hash."""
        return self.strict_at.get(sha, [])

    def loose(self, sha):
        """[(path, line number, text)] of the lines with this loose hash."""
        return self.loose_at.get(sha, [])


def at(hits):
    p, n, _t = hits[0]
    return '%s:%d' % (p.decode('utf-8', 'replace'), n)


def old_line(repo, files, claim):
    """The text main's tree holds at `path:line`, or None."""
    path, n = CLAIM.fullmatch(claim).groups()
    st = files.get(path.encode())
    if st is None or st[0] == '160000':
        return None
    lines = repo.blob(st[1]).split(b'\n')
    return lines[int(n) - 1] if int(n) <= len(lines) else None


def matches(record, entry):
    return (record['from_claim'], record['from_claim_sha256']) \
        == (entry['claim'], entry['claim_sha256'])


def check(repo, c, main=None):
    """(problems, manifests, ids): problems is a list of (manifest, code, id, detail)."""
    if repo.width() != 40:
        raise v3.Undecidable('object-format')
    repo.need(c)
    files = repo.entries(c)
    manifests = manifest_paths(files)
    main_files = repo.entries(main) if main else {}
    main_entries = {mp: (load(repo.blob(main_files[mp][1])) or ({}, {}))[0]
                    for mp in manifest_paths(main_files)}
    main_support = [(mp, k, e) for mp in sorted(main_entries)
                    for k, e in sorted(main_entries[mp].items()) if e['role'] == 'support']
    if not manifests and not main_support:
        return [], 0, 0
    pdirs, precs = protected(repo, files) if manifests else (set(), set())
    out, n_ids, loaded, broken = [], 0, {}, set()
    for mp in manifests:
        d = mp[:-len(NAME)]                     # b'' or b'dir/'
        name = mp.decode('utf-8', 'replace')
        if any((p + b'/').startswith(d) or d.startswith(p + b'/')
               for p in pdirs) or any(r.startswith(d) for r in precs):
            out.append((name, 'frozen-scope', '', ''))
            broken.add(mp)
            continue
        if any(o != mp and o.startswith(d) for o in manifests):
            out.append((name, 'nested-manifest', '', ''))
            broken.add(mp)
            continue
        man = load(repo.blob(files[mp][1]))
        if man is None:
            out.append((name, 'malformed', '', ''))
            broken.add(mp)
            continue
        ids, loaded[mp] = man[0], man
        n_ids += len(ids)
        cited, quals = {}, {}
        for p in sorted(files):
            mode, obj = files[p]
            if p == mp or not p.startswith(d) or mode == '160000':
                continue
            data = repo.blob(obj)
            for tok in OBJECT_ID.finditer(data):
                oid = tok.group().decode()
                cited.setdefault(oid, p.decode('utf-8', 'replace'))
                quals.setdefault(oid, set()).add(qualifier(data, tok.start()))
        landed = {k: e['role'] for k, e in main_entries.get(mp, {}).items()}
        for oid in sorted(set(cited) - set(ids)):
            out.append((name, 'unlisted', oid, cited[oid]))
        for oid in sorted(set(ids) - set(cited)):
            out.append((name, 'unused', oid, ''))
        for oid, e in ids.items():
            role = e['role']
            if role == 'support':
                why = claim_problem(repo, files, d, mp, e, oid)
                if why:
                    out.append((name, why, oid, e['claim']))
            if role == 'provenance' and landed.get(oid) == 'provenance':
                continue
            t = object_type(repo, oid)
            if role == 'external':
                declared = repository_name(e['repository'])
                if declared == THIS_REPOSITORY:
                    out.append((name, 'external-this-repository', oid, e['repository']))
                elif any(q != declared for q in quals.get(oid, ())):
                    out.append((name, 'external-unqualified', oid, cited.get(oid, '')))
                if t is not None:
                    out.append((name, 'external-in-repository', oid, cited.get(oid, '')))
            elif t is None:
                out.append((name, 'absent', oid, cited.get(oid, '')))
            elif role == 'support' and t != 'commit':
                out.append((name, 'support-not-commit', oid, cited.get(oid, '')))
            elif role == 'support' and not repo.is_ancestor(oid, c):
                out.append((name, 'support-unreachable', oid, cited.get(oid, '')))
    out.extend(downgrades(repo, files, main_files, main_entries, main_support, loaded, broken))
    return out, len(manifests), n_ids


def downgrades(repo, files, main_files, main_entries, main_support, loaded, broken):
    """support-downgrade problems. A support id of any main manifest that no manifest of the commit
    lists as support needs a record matching that support entry, as the `downgrade` of an entry
    or under `retired`, and its claim must not stand anywhere in the tree; an entry of the commit
    listing such an id otherwise needs a matching record of its own; and no record's claim may
    stand unchanged anywhere in the tree."""
    out = []
    support_now = {k for ids, _r in loaded.values() for k, e in ids.items()
                   if e['role'] == 'support'}
    records = sorted((mp, k, e['downgrade']) for mp, (ids, _r) in loaded.items()
                     for k, e in ids.items() if 'downgrade' in e)
    records += sorted((mp, k, r) for mp, (_i, retired) in loaded.items()
                      for k, r in retired.items())
    was = [(mp, k, e) for mp, k, e in main_support if mp not in broken and k not in support_now]
    looses = {}
    for mp, oid, e in main_support:
        text = old_line(repo, main_files, e['claim'])
        looses[(mp, oid)] = loose_sha256(text) if text is not None \
            and line_sha256(text) == e['claim_sha256'] else EMPTY_LOOSE
    lines = TreeLines(repo, files, {e['claim_sha256'] for _m, _k, e in was}
                      | {r['from_claim_sha256'] for _m, _k, r in records}, set(looses.values()))
    for mp, oid, e in main_support:
        if mp in broken:
            continue
        name = mp.decode('utf-8', 'replace')
        loose = looses[(mp, oid)]
        if oid in support_now:
            # still support somewhere: its claim may stand only with the reference on it
            bare = [h for h in lines.loose(loose) if oid.encode() not in OBJECT_ID.findall(h[2])]
            if bare:
                out.append((name, 'support-downgrade', oid, 'the claim of %s stands at %s '
                            'without its reference' % (e['claim'], at(bare))))
            continue
        if not any(k == oid and matches(r, e) for _m, k, r in records):
            out.append((name, 'support-downgrade', oid,
                        'no downgrade record for the support claim %s' % e['claim']))
        hits = lines.strict(e['claim_sha256']) or lines.loose(loose)
        if hits:
            out.append((name, 'support-downgrade', oid,
                        'the claim of %s stands at %s' % (e['claim'], at(hits))))
    for mp, (ids, _r) in sorted(loaded.items()):
        name = mp.decode('utf-8', 'replace')
        for oid, e in sorted(ids.items()):
            prior = main_entries.get(mp, {}).get(oid)
            if e['role'] == 'support' or prior is not None and prior['role'] != 'support':
                continue
            supported = [w for _m, k, w in was if k == oid]
            dg = e.get('downgrade')
            if supported and not (dg and any(matches(dg, w) for w in supported)):
                out.append((name, 'support-downgrade', oid, '%s record for the support claim %s'
                            % ('no downgrade' if dg is None else 'a non-matching downgrade',
                               supported[0]['claim'])))
    for mp, oid, r in records:
        hits = lines.strict(r['from_claim_sha256'])
        if hits:
            out.append((mp.decode('utf-8', 'replace'), 'support-downgrade', oid,
                        'the claim of %s stands at %s' % (r['from_claim'], at(hits))))
    return out


def check_against_main(repo, c):
    """check() with main resolved from the repository's refs: (problems, manifests, ids, main)."""
    m = main_commit(repo)
    return check(repo, c, m) + (m,)


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


def _manifest(entries, ordered=False, retired=None):
    ids = entries if ordered else dict(sorted(entries.items()))
    m = {'schema': 'oi-citations', 'version': 2, 'ids': ids}
    if retired is not None:
        m['retired'] = dict(sorted(retired.items()))
    return (json.dumps(m, indent=1) + '\n').encode()


def _claim(sets, oid):
    """The first `path:line` among the fixture's files whose line carries the id."""
    for p in sorted(sets):
        for i, line in enumerate(sets[p][1].split(b'\n')):
            if oid.encode() in OBJECT_ID.findall(line):
                return '%s:%d' % (p.decode(), i + 1)
    return 'rec/NOTE.md:1'


def _claim_sha256(sets, claim):
    """The hash of the fixture line `path:line` names, or a placeholder when there is none."""
    m = CLAIM.fullmatch(claim)
    if not m:
        return '0' * 64
    path, n = m.groups()
    lines = sets.get(path.encode(), ('', b''))[1].split(b'\n')
    return line_sha256(lines[int(n) - 1]) if int(n) <= len(lines) else '0' * 64


def _support(sets, oid, claim=None):
    claim = claim or _claim(sets, oid)
    return {'role': 'support', 'claim': claim, 'claim_sha256': _claim_sha256(sets, claim)}


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
        sc.commit('B1', ['M0'], 'M0', {b'branch.txt': ('100644', b'branch\n')}, [])
        m0, s, b1 = sc.labels['M0'], sc.labels['S'], sc.labels['B1']
        blob, tree = sc.repo.state(m0, b'base.txt')[1], sc.repo.tree(m0)
        tag = sc.git(['mktag'], data=('object %s\ntype commit\ntag t1\ntagger t <t@invalid> '
                                      '1700000000 +0000\n\ntag\n' % m0).encode()).decode().strip()
        gone, gone2 = 'ab' * 20, 'cd' * 20
        sc.git(['update-ref', 'refs/heads/main', m0])

        def codes(c, main):
            try:
                return {code for _m, code, _i, _f in check(sc.repo, c, main)[0]}
            except v3.Undecidable as u:     # a crash is a failure of the test, not a kill
                return {u.code}
            except Exception as e:          # noqa: BLE001
                return {'crash:' + type(e).__name__}

        def case(label, sets, main=m0, parent='M0', dels=()):
            sc.commit(label, [parent], parent, sets, list(dels))
            return codes(sc.labels[label], main)

        def rec(text, ids, extra=None, d='rec'):
            """A record d/ citing `text`; ids maps an id to a role, whose fields the fixture
            fills in, or to a literal entry, a support entry's missing hash filled in from its
            claimed line; bytes are a literal manifest."""
            sets = {(d + '/NOTE.md').encode(): ('100644', text.encode())}
            sets.update(extra or {})
            if isinstance(ids, dict):
                fill = {'support': lambda o: _support(sets, o),
                        'provenance': lambda o: {'role': 'provenance', 'reason': 'fixture'},
                        'external': lambda o: {'role': 'external',
                                               'repository': 'actions/checkout'}}
                entries = {}
                for o, e in ids.items():
                    if not isinstance(e, dict):
                        e = fill[e](o)
                    elif e.get('role') == 'support' and 'claim' in e and 'claim_sha256' not in e:
                        e = dict(e, claim_sha256=_claim_sha256(sets, e['claim']))
                    entries[o] = e
                ids = _manifest(entries)
            sets[(d + '/CITATIONS.json').encode()] = ('100644', ids)
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
            ('external id in a URL into its repository',
             rec('https://github.com/Actions/Checkout/commit/%s\n' % gone, {gone: 'external'})),
            ('support id a commit the change under check adds, not on main',
             rec('see %s\n' % b1, {b1: 'support'}), 'B1'),
            ('support claimed on a later line of a subdirectory file', rec('x\n', {m0: 'support'}, {
                b'rec/sub/data.json': ('100644', ('{\n "c": "%s"\n}\n' % m0).encode())})),
            ('entries written out literally', rec(
                'see %s\nprovenance %s\nuses: actions/checkout@%s\n' % (m0, s, gone), {
                    m0: {'role': 'support', 'claim': 'rec/NOTE.md:1'},
                    s: {'role': 'provenance', 'reason': 'the run this record replaced'},
                    gone: {'role': 'external', 'repository': 'actions/checkout'}})),
            ('no manifest: not read', {b'other/NOTE.md': ('100644', ('%s\n' % gone).encode())}),
            ('claim hash over whitespace-normalized text', rec(
                '\t see   %s \r\n' % m0, {m0: {'role': 'support', 'claim': 'rec/NOTE.md:1',
                                               'claim_sha256': hashlib.sha256(
                                                   ('see %s' % m0).encode()).hexdigest()}})),
        ]
        for name, sets, *parent in positives:
            got = case('P-' + name, sets, parent=(parent or ['M0'])[0])
            if got:
                fails.append('%s: expected pass, got %s' % (name, sorted(got)))

        two = 'see %s\nand nothing here\n' % m0
        dg_ok = {'from_claim': 'rec/NOTE.md:2', 'from_claim_sha256': 'f' * 64, 'reason': 'x'}
        mutants = [
            ('off-main id cited as support', 'support-unreachable',
             rec('see %s\n' % s, {s: 'support'})),
            ('missing object as provenance', 'absent',
             rec('see %s\n' % gone, {gone: 'provenance'})),
            ('missing object as support', 'absent', rec('see %s\n' % gone, {gone: 'support'})),
            ('blob as support', 'support-not-commit', rec('see %s\n' % blob, {blob: 'support'})),
            ('tree as support', 'support-not-commit', rec('see %s\n' % tree, {tree: 'support'})),
            ('tag as support', 'support-not-commit', rec('see %s\n' % tag, {tag: 'support'})),
            ('claim on a line without the id', 'claim-line-mismatch',
             rec(two, {m0: {'role': 'support', 'claim': 'rec/NOTE.md:2'}})),
            ('claim past the end of the file', 'claim-line-mismatch',
             rec('x\nsee %s' % m0, {m0: {'role': 'support', 'claim': 'rec/NOTE.md:9'}})),
            ('claim outside the manifest directory', 'claim-outside',
             rec(two, {m0: {'role': 'support', 'claim': 'base.txt:1'}})),
            ('claim escaping the directory by ..', 'claim-outside',
             rec(two, {m0: {'role': 'support', 'claim': 'rec/../rec/NOTE.md:1'}})),
            ('claim naming the manifest itself', 'claim-outside',
             rec(two, {m0: {'role': 'support', 'claim': 'rec/CITATIONS.json:4'}})),
            ('claim naming a file the commit lacks', 'claim-file-absent',
             rec(two, {m0: {'role': 'support', 'claim': 'rec/gone.md:1'}})),
            ('external commit of this repository', 'external-in-repository',
             rec('uses: actions/checkout@%s\n' % s, {s: 'external'})),
            ('external id unqualified', 'external-unqualified',
             rec('pinned to %s\n' % gone, {gone: 'external'})),
            ('external id qualified once, unqualified once', 'external-unqualified',
             rec('uses: actions/checkout@%s\n# pinned to %s\n' % (gone, gone),
                 {gone: 'external'})),
            ('external id qualified with another repository', 'external-unqualified',
             rec('uses: actions/setup-python@%s\n' % gone, {gone: 'external'})),
            ('external entry naming this repository', 'external-this-repository',
             rec('uses: amaybaum/incompleteness@%s\n' % gone,
                 {gone: {'role': 'external', 'repository': 'Amaybaum/Incompleteness.git'}})),
            ('unlisted id', 'unlisted', rec('see %s and %s\n' % (m0, s), {m0: 'support'})),
            ('unlisted id in a subdirectory file', 'unlisted',
             rec('see %s\n' % m0, {m0: 'support'},
                 {b'rec/sub/x.out': ('100644', ('run at %s\n' % s).encode())})),
            ('unlisted id in a NUL-containing file', 'unlisted',
             rec('see %s\n' % m0, {m0: 'support'},
                 {b'rec/data.bin': ('100644', b'\x00\x01' + s.encode() + b'\x00\xff')})),
            ('unused id', 'unused', rec('see %s\n' % m0, {m0: 'support', s: 'provenance'})),
            ('malformed: not json', 'malformed', rec('x\n', b'{"schema": \n')),
            ('malformed: wrong schema', 'malformed', rec('x\n', b'{"schema": "oi-legacy-records", '
                                                        b'"version": 2, "ids": {}}')),
            ('malformed: version 1', 'malformed', rec('x\n', b'{"schema": "oi-citations", '
                                                      b'"version": 1, "ids": {}}')),
            ('malformed: version 2.0', 'malformed', rec('x\n', b'{"schema": "oi-citations", '
                                                        b'"version": 2.0, "ids": {}}')),
            ('malformed: version true', 'malformed', rec('x\n', b'{"schema": "oi-citations", '
                                                         b'"version": true, "ids": {}}')),
            ('malformed: unknown field', 'malformed', rec('x\n', b'{"schema": "oi-citations", '
                                                          b'"version": 2, "ids": {}, "x": 1}')),
            ('malformed: bare role string', 'malformed', rec('see %s\n' % s, (
                '{"schema": "oi-citations", "version": 2, "ids": {"%s": "provenance"}}'
                % s).encode())),
            ('malformed: unknown role', 'malformed',
             rec('see %s\n' % m0, {m0: {'role': 'evidence', 'reason': 'x'}})),
            ('malformed: support without claim', 'malformed',
             rec('see %s\n' % m0, {m0: {'role': 'support'}})),
            ('malformed: claim without a line', 'malformed',
             rec('see %s\n' % m0, {m0: {'role': 'support', 'claim': 'rec/NOTE.md'}})),
            ('malformed: provenance without reason', 'malformed',
             rec('see %s\n' % s, {s: {'role': 'provenance'}})),
            ('malformed: provenance with an empty reason', 'malformed',
             rec('see %s\n' % s, {s: {'role': 'provenance', 'reason': ' '}})),
            ('malformed: entry with another role\'s field', 'malformed',
             rec('see %s\n' % s, {s: {'role': 'provenance', 'reason': 'x', 'claim': 'a:1'}})),
            ('malformed: external without an owner', 'malformed',
             rec('uses: checkout@%s\n' % gone, {gone: {'role': 'external',
                                                       'repository': 'checkout'}})),
            ('malformed: unsorted ids', 'malformed', rec('%s %s\n' % (m0, s), _manifest({
                o: {'role': 'provenance', 'reason': 'x'}
                for o in sorted([m0, s], reverse=True)}, ordered=True))),
            ('malformed: duplicate id', 'malformed', rec('%s\n' % m0, (
                '{"schema": "oi-citations", "version": 2, "ids": {"%s": {"role": "provenance", '
                '"reason": "x"}, "%s": {"role": "provenance", "reason": "y"}}}'
                % (m0, m0)).encode())),
            ('malformed: short id', 'malformed', rec('x\n', _manifest({
                m0[:12]: {'role': 'provenance', 'reason': 'x'}}))),
            ('claim hash of another line', 'claim-hash-mismatch',
             rec(two, {m0: {'role': 'support', 'claim': 'rec/NOTE.md:1',
                            'claim_sha256': line_sha256(b'and nothing here')}})),
            ('claim hash of the line before normalization', 'claim-hash-mismatch',
             rec('see  %s\n' % m0, {m0: {'role': 'support', 'claim': 'rec/NOTE.md:1',
                                         'claim_sha256': hashlib.sha256(
                                             ('see  %s' % m0).encode()).hexdigest()}})),
            ('malformed: support without claim_sha256', 'malformed', rec('see %s\n' % m0, _manifest(
                {m0: {'role': 'support', 'claim': 'rec/NOTE.md:1'}}))),
            ('malformed: claim_sha256 in uppercase', 'malformed', rec('see %s\n' % m0, _manifest(
                {m0: {'role': 'support', 'claim': 'rec/NOTE.md:1',
                      'claim_sha256': line_sha256(('see %s' % m0).encode()).upper()}}))),
            ('malformed: downgrade on a support entry', 'malformed', rec('see %s\n' % m0, {m0: dict(
                {'role': 'support', 'claim': 'rec/NOTE.md:1'}, downgrade=dict(dg_ok))})),
            ('malformed: downgrade with an empty reason', 'malformed', rec('see %s\n' % s, {s: {
                'role': 'provenance', 'reason': 'x', 'downgrade': dict(dg_ok, reason=' ')}})),
            ('malformed: downgrade without from_claim_sha256', 'malformed', rec(
                'see %s\n' % s, {s: {'role': 'provenance', 'reason': 'x', 'downgrade': {
                    'from_claim': 'rec/NOTE.md:2', 'reason': 'x'}}})),
            ('malformed: downgrade with an extra field', 'malformed', rec('see %s\n' % s, {s: {
                'role': 'provenance', 'reason': 'x', 'downgrade': dict(dg_ok, note='x')}})),
            ('malformed: empty retired', 'malformed', rec('x\n', _manifest({}, retired={}))),
            ('malformed: retired id also listed', 'malformed', rec('see %s\n' % s, _manifest(
                {s: {'role': 'provenance', 'reason': 'x'}}, retired={s: dict(dg_ok)}))),
            ('malformed: retired record without a reason', 'malformed', rec('x\n', _manifest(
                {}, retired={s: {'from_claim': 'rec/NOTE.md:2', 'from_claim_sha256': 'f' * 64}}))),
            ('malformed: retired ids unsorted', 'malformed', rec('x\n', (
                '{"schema": "oi-citations", "version": 2, "ids": {}, "retired": {"%s": %s, '
                '"%s": %s}}' % (s, json.dumps(dg_ok), m0, json.dumps(dg_ok))).encode()
                if s > m0 else ('{"schema": "oi-citations", "version": 2, "ids": {}, "retired": '
                                '{"%s": %s, "%s": %s}}' % (m0, json.dumps(dg_ok), s,
                                                           json.dumps(dg_ok))).encode())),
            ('malformed: downgrade as a string', 'malformed', rec('see %s\n' % s, {s: {
                'role': 'provenance', 'reason': 'x', 'downgrade': 'narrowed'}})),
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
            ('manifest in verification/receipts/', 'frozen-scope', {
                b'verification/receipts/CITATIONS.json': ('100644', _manifest({}))}),
            ('manifest in verification/seals/', 'frozen-scope', {
                b'verification/seals/CITATIONS.json': ('100644', _manifest({}))}),
        ]
        for name, target, sets in mutants:
            got = case('X-' + name, sets)
            v = verdict(target, got)
            if v != 'killed':
                fails.append('%s: %s (target %s, got %s)' % (name, v, target, sorted(got)))

        # a submodule entry in a covered directory is not scanned, and is no claim file
        def gitlink(label, sets):
            sc.commit(label + '-base', ['M0'], 'M0', sets, [])
            base = sc.labels[label + '-base']
            sub = sc.git(['rev-parse', base + ':rec']).decode().strip()
            rec_tree = sc.git(['mktree', '-z'], data=sc.git(['ls-tree', '-z', sub]) + (
                '160000 commit %s\tmod\0' % m0).encode()).decode().strip()
            root = [e for e in sc.git(['ls-tree', '-z', base]).split(b'\0')
                    if e and not e.endswith(b'\trec')]
            root = b''.join(e + b'\0' for e in root) + ('040000 tree %s\trec\0' % rec_tree).encode()
            tree = sc.git(['mktree', '-z'], data=root).decode().strip()
            return codes(sc.git(['commit-tree', tree, '-p', m0, '-m', label],
                                env=v3.COMMIT_ENV).decode().strip(), m0)
        for name, sets, want in (
                ('submodule entry in a covered directory', rec('see %s\n' % m0, {m0: 'support'}),
                 set()),
                ('support claim naming a submodule entry', rec('see %s\n' % m0, {m0: {
                    'role': 'support', 'claim': 'rec/mod:1', 'claim_sha256': 'f' * 64}}),
                 {'claim-file-absent'})):
            got = gitlink('G-' + name, sets)
            if got != want:
                fails.append('%s: expected %s, got %s' % (name, sorted(want), sorted(got)))

        # negative controls, on fixtures of their own: a live unrelated failure (an unused id, no
        # reachability defect) is not a kill of the support-reachability mutant, and a fixture
        # that fails on its target and on something else is unclean, not a kill
        got = case('N-unrelated', rec('see %s\n' % m0, {m0: 'support', blob: 'provenance'}))
        if got != {'unused'} or verdict('support-unreachable', got) != 'survived':
            fails.append('negative control: unrelated failure %s scored %s' % (
                sorted(got), verdict('support-unreachable', got)))
        got = case('N-unclean', rec('see %s and %s\n' % (s, m0), {s: 'support'}))
        if got != {'support-unreachable', 'unlisted'} \
                or verdict('support-unreachable', got) != 'unclean':
            fails.append('negative control: two failures %s scored %s' % (
                sorted(got), verdict('support-unreachable', got)))

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
        # an id main lists as external, re-declared provenance, is checked as landing
        sc.commit('LX', ['M0'], 'M0', rec('uses: actions/checkout@%s\n' % gone2,
                                          {gone2: 'external'}), [])
        got = case('LX2', rec('see %s\n' % gone2, {gone2: 'provenance'}), main=sc.labels['LX'],
                   parent='LX')
        if got != {'absent'}:
            fails.append('landed external re-declared provenance: expected absent, got %s'
                         % sorted(got))

        # downgrades: on main D0, rec/ lists m0 as the support of rec/NOTE.md:2; on main DX it lists
        # gone. Each case is a child of its main, checked against it, and must fail with exactly
        # the codes given; support-downgrade is SD.
        SD = 'support-downgrade'
        claim_line = 'The bound holds at %s.' % m0
        h0, h_stale = line_sha256(claim_line.encode()), line_sha256(b'The bound was read off.')
        hist = 'history: %s' % m0
        reworded = 'The bound is established at %s.' % m0
        narrowed = 'The bound holds at %s for n <= 4 only.' % m0
        d0_text = '# Note\n%s\n%s\n' % (claim_line, hist)
        sc.commit('D0', ['M0'], 'M0', rec(d0_text, {m0: 'support'}), [])
        sc.commit('DX', ['M0'], 'M0', rec('# Note\nThe bound holds at %s.\n' % gone,
                                          {gone: 'support'}), [])
        sc.commit('DI', ['M0'], 'M0', rec('# Note\n%s\n\nend\n' % m0, {m0: 'support'}), [])
        # DS: main's own entry is stale, its claim_sha256 not the hash of the line it names
        sc.commit('DS', ['M0'], 'M0', rec('# Note\nan aside on %s\n' % m0, {m0: {
            'role': 'support', 'claim': 'rec/NOTE.md:2', 'claim_sha256': h_stale}}), [])
        hx = line_sha256(('The bound holds at %s.' % gone).encode())
        if json.loads(sc.files['D0'][b'rec/CITATIONS.json'][1])['ids'][m0]['claim_sha256'] != h0 \
                or codes(sc.labels['D0'], m0) or codes(sc.labels['DX'], m0) != {'absent'}:
            fails.append('downgrade fixtures: D0 does not hold, or DX fails otherwise than absent')
        dg0 = {'from_claim': 'rec/NOTE.md:2', 'from_claim_sha256': h0,
               'reason': 'the bound is withdrawn'}
        dgx = {'from_claim': 'rec/NOTE.md:2', 'from_claim_sha256': hx,
               'reason': 'the action is pinned, not relied on'}

        def prov(dg=None):
            e = {'role': 'provenance', 'reason': 'the run the bound was read from'}
            return dict(e, downgrade=dg) if dg else e

        def ext(dg=None):
            e = {'role': 'external', 'repository': 'actions/checkout'}
            return dict(e, downgrade=dg) if dg else e

        gone_rec = (b'rec/NOTE.md', b'rec/CITATIONS.json')
        note = lambda *ls: '# Note\n' + ''.join(x + '\n' for x in ls)        # noqa: E731
        dcases = [
            # name, sets, deletions, parent and main, expected codes
            ('support relabelled provenance without a record', rec(d0_text, {m0: prov()}), (),
             'D0', {SD}),
            ('record, the claim unchanged at its line', rec(d0_text, {m0: prov(dg0)}), (), 'D0',
             {SD}),
            ('record, the claim moved to another line', rec(note(hist, claim_line),
                                                            {m0: prov(dg0)}), (), 'D0', {SD}),
            ('record, the claim moved with its whitespace changed', rec(note(
                hist, '  ' + claim_line.replace(' ', ' \t ') + ' '), {m0: prov(dg0)}), (), 'D0',
             {SD}),
            ('record, the claim moved to a subdirectory file', rec(note(hist), {m0: prov(dg0)}, {
                b'rec/sub/x.md': ('100644', (claim_line + '\n').encode())}), (), 'D0', {SD}),
            ('the claim reworded, relabelled without a record', rec(note(reworded, hist),
                                                                    {m0: prov()}), (), 'D0', {SD}),
            ('record not matching main\'s claim hash', rec(note(hist), {m0: prov(dict(
                dg0, from_claim_sha256=line_sha256(reworded.encode())))}), (), 'D0', {SD}),
            ('record not matching main\'s claim path', rec(note(hist), {m0: prov(dict(
                dg0, from_claim='rec/NOTE.md:3'))}), (), 'D0', {SD}),
            ('support relabelled external without a record', rec(
                note('uses: actions/checkout@%s' % gone), {gone: ext()}), (), 'DX', {SD}),
            ('support entry dropped while the id is cited', rec(note(hist), {}), (), 'D0',
             {'unlisted', SD}),
            ('record, the claim removed', rec(note(hist), {m0: prov(dg0)}), (), 'D0', set()),
            ('record, narrowed text added above the old claim left in place', rec(
                note(narrowed, claim_line), {m0: prov(dg0)}), (), 'D0', {SD}),
            ('record, the claim narrowed with new text', rec(note(narrowed, hist),
                                                             {m0: prov(dg0)}), (), 'D0', set()),
            ('support relabelled external with a record', rec(
                note('uses: actions/checkout@%s' % gone), {gone: ext(dgx)}), (), 'DX', set()),
            ('support kept, its claim moved and rehashed', rec(note(hist, claim_line),
                                                               {m0: 'support'}), (), 'D0', set()),
            ('support entry dropped with its citations, no record', rec(note(), {}), (), 'D0',
             {SD}),
            ('support entry retired with its citations', rec(note(), _manifest(
                {}, retired={m0: dg0})), (), 'D0', set()),
            ('manifest removed, its directory still citing the id', {},
             (b'rec/CITATIONS.json',), 'D0', {SD}),
            ('manifest removed, the claim reworded, its directory still citing the id', {
                b'rec/NOTE.md': ('100644', note(reworded).encode())}, (b'rec/CITATIONS.json',),
             'D0', {SD}),
            ('manifest removed, the claim moved unchanged out of scope', {
                b'other/x.md': ('100644', (claim_line + '\n').encode())}, gone_rec, 'D0', {SD}),
            ('record removed with its claim, no record', {}, gone_rec, 'D0', {SD}),
            ('record removed with its claim, retired in another manifest', {
                b'other/CITATIONS.json': ('100644', _manifest({}, retired={m0: dg0}))},
             gone_rec, 'D0', set()),
            ('record moved, relabelled without a record', rec(note(hist), {m0: prov()}, d='rec2'),
             gone_rec, 'D0', {SD}),
            ('record moved, a record kept with the claim unchanged', rec(
                d0_text, {m0: prov(dg0)}, d='rec2'), gone_rec, 'D0', {SD}),
            ('record moved, a record kept with the claim removed', rec(
                note(hist), {m0: prov(dg0)}, d='rec2'), gone_rec, 'D0', set()),
            ('record moved, still support', rec(d0_text, {m0: 'support'}, d='rec2'), gone_rec,
             'D0', set()),
            ('record moved without a manifest, the claim reworded', {
                b'rec2/NOTE.md': ('100644', note(reworded).encode())}, gone_rec, 'D0', {SD}),
            # the second review's seven bypasses
            ('the id removed from text and manifest, the claim kept', rec(
                note('The bound holds.'), {}), (), 'D0', {SD}),
            ('the id abbreviated on the claim, the entry dropped', rec(
                note('The bound holds at %s.' % m0[:12]), {}), (), 'D0', {SD}),
            ('the id uppercased on the claim, the entry dropped', rec(
                note('The bound holds at %s.' % m0.upper()), {}), (), 'D0', {SD}),
            ('the claim moved verbatim to a directory without a manifest', rec(note('moved'), {}, {
                b'loose/x.md': ('100644', (claim_line + '\n').encode())}), (), 'D0', {SD}),
            ('the claim moved verbatim to another manifest\'s record as provenance', rec(
                note('moved'), {}, {b'other/x.md': ('100644', (claim_line + '\n').encode()),
                                    b'other/CITATIONS.json': ('100644', _manifest(
                                        {m0: prov()}))}), (), 'D0', {SD}),
            ('record kept, the claim moved verbatim out of the covered tree', rec(
                note(hist), {m0: prov(dg0)}, {
                    b'loose/x.md': ('100644', (claim_line + '\n').encode())}), (), 'D0', {SD}),
            ('manifest renamed citations.json, the id removed from the text', {
                b'rec/NOTE.md': ('100644', note('The bound holds.').encode()),
                b'rec/citations.json': ('100644', _manifest({}))}, (b'rec/CITATIONS.json',),
             'D0', {SD}),
            ('manifest removed, the claim kept with its reference deleted', {
                b'rec/NOTE.md': ('100644', note('The bound holds at .').encode())},
             (b'rec/CITATIONS.json',), 'D0', {SD}),
            # the id still declared support on another line: the claim may not stay without it
            ('still support on another line, the reference deleted from the claim', rec(
                note(hist, 'The bound holds at .'), {m0: 'support'}), (), 'D0', {SD}),
            ('still support on another line, the reference abbreviated on the claim', rec(
                note(hist, 'The bound holds at %s.' % m0[:12]), {m0: 'support'}), (), 'D0', {SD}),
            ('still support on another line, the reference uppercased on the claim', rec(
                note(hist, 'The bound holds at %s.' % m0.upper()), {m0: 'support'}), (), 'D0',
             {SD}),
            ('still support in another manifest, the claim kept without its reference', rec(
                note('The bound holds at .'), {}, {
                    b'other/x.md': ('100644', (hist + '\n').encode()),
                    b'other/CITATIONS.json': ('100644', _manifest({m0: _support(
                        {b'other/x.md': ('100644', (hist + '\n').encode())}, m0)}))}), (),
             'D0', {SD}),
            ('still support, the claim reworded with its reference', rec(
                note(reworded, hist), {m0: 'support'}), (), 'D0', set()),
            ('still support, the claim also quoted with its reference elsewhere', rec(
                d0_text, {m0: {'role': 'support', 'claim': 'rec/NOTE.md:2'}}, {
                    b'loose/x.md': ('100644', (claim_line + '\n').encode())}), (), 'D0', set()),
            # with a matching record: the claim counts as unchanged when its only edit is to its id
            ('retired, the id abbreviated on the unchanged claim', rec(
                note('The bound holds at %s.' % m0[:12]), _manifest({}, retired={m0: dg0})), (),
             'D0', {SD}),
            ('retired, the id uppercased on the unchanged claim', rec(
                note('The bound holds at %s.' % m0.upper()), _manifest({}, retired={m0: dg0})),
             (), 'D0', {SD}),
            ('retired, the id removed from the unchanged claim', rec(
                note('The bound holds at .'), _manifest({}, retired={m0: dg0})), (), 'D0', {SD}),
            ('retired, the id removed and the claim reworded', rec(
                note('The bound holds.'), _manifest({}, retired={m0: dg0})), (), 'D0', set()),
            # a relabel in another manifest needs its own record
            ('retired in rec/, relabelled provenance in other/ without a record', rec(
                note('moved'), _manifest({}, retired={m0: dg0}), {
                    b'other/x.md': ('100644', (reworded + '\n').encode()),
                    b'other/CITATIONS.json': ('100644', _manifest({m0: prov()}))}), (), 'D0',
             {SD}),
            ('a claim line of nothing but the id, retired and removed', rec(
                '# Note\n\nend\n', _manifest({}, retired={m0: dict(
                    dg0, from_claim_sha256=line_sha256(m0.encode()))})), (), 'DI', set()),
            ('relabelled external in place, its only record retired in another manifest', rec(
                note('uses: actions/checkout@%s' % gone), {gone: ext()}, {
                    b'other/CITATIONS.json': ('100644', _manifest({}, retired={gone: dgx}))}),
             (), 'DX', {SD}),
            ('retired with a record not matching main\'s claim hash', rec(note(), _manifest(
                {}, retired={m0: dict(dg0, from_claim_sha256=h_stale)})), (), 'D0', {SD}),
            ('retired with a record not matching main\'s claim path', rec(note(), _manifest(
                {}, retired={m0: dict(dg0, from_claim='rec/NOTE.md:3')})), (), 'D0', {SD}),
            ('retired, the id removed and only the case of the claim changed', rec(
                note('THE BOUND HOLDS AT .'), _manifest({}, retired={m0: dg0})), (), 'D0', {SD}),
            ('retired against a stale main entry: the line it names is not the claim', rec(
                note('an aside on'), _manifest({}, retired={m0: dict(
                    dg0, from_claim_sha256=h_stale)})), (), 'DS', set()),
            ('relabelled provenance in place, its only record retired in another manifest', rec(
                note(hist), {m0: prov()}, {b'other/CITATIONS.json': ('100644', _manifest(
                    {}, retired={m0: dg0}))}), (), 'D0', {SD}),
            ('relabelled provenance in other/ with the record, the claim reworded', rec(
                note('moved'), {}, {b'other/x.md': ('100644', (reworded + '\n').encode()),
                                    b'other/CITATIONS.json': ('100644', _manifest(
                                        {m0: prov(dg0)}))}), (), 'D0', set()),
            ('limitation: another record citing a removed manifest\'s support id', dict(rec(
                note(hist), {m0: prov()}, d='other')), (b'rec/CITATIONS.json',), 'D0', {SD}),
        ]
        for name, sets, dels, parent, want in dcases:
            got = case('D-' + name, sets, main=sc.labels[parent], parent=parent, dels=dels)
            if got != want:
                fails.append('downgrade, %s: expected %s, got %s' % (name, sorted(want),
                                                                     sorted(got)))
        # with no main ref nothing is compared, but a record whose claim stands still fails; and
        # once a downgrade has landed it needs nothing more, unless its claim comes back
        for name, sets, want in (
                ('no main ref, relabelled without a record', rec(d0_text, {m0: prov()}), set()),
                ('no main ref, a record whose claim stands', rec(d0_text, {m0: prov(dg0)}), {SD})):
            got = case('D-' + name, sets, main=None, parent='D0')
            if got != want:
                fails.append('downgrade, %s: expected %s, got %s' % (name, sorted(want),
                                                                     sorted(got)))
        # negative control on a fixture of its own: an unrelated failure under the same main (an
        # unused id, the support kept) is not a kill of a downgrade mutant
        got = case('N-downgrade', rec(d0_text, {m0: 'support', s: 'provenance'}),
                   main=sc.labels['D0'], parent='D0')
        if got != {'unused'} or verdict(SD, got) != 'survived':
            fails.append('negative control: unrelated failure under D0 %s scored %s' % (
                sorted(got), verdict(SD, got)))
        dl = sc.labels['D-record, the claim removed']
        for name, sets, want in (
                ('after a landed downgrade', {b'rec/more.md': ('100644', b'more\n')}, set()),
                ('a landed record whose claim comes back', {b'rec/back.md': (
                    '100644', (claim_line + '\n').encode())}, {SD})):
            got = case('D-' + name, sets, main=dl, parent='D-record, the claim removed')
            if got != want:
                fails.append('downgrade, %s: expected %s, got %s' % (name, sorted(want),
                                                                     sorted(got)))
        n_down = len(dcases) + 5

        # main resolved from real refs, with HEAD at the commit under check: origin/main is
        # preferred over a stale local main, local main is used alone, and with neither every id
        # is checked as landing. L lists gone2 as provenance; M0 does not.
        sc.git(['symbolic-ref', 'HEAD', 'refs/heads/work'])
        sc.git(['update-ref', 'refs/heads/work', lid])
        for name, origin, local, want_main, want in (
                ('origin/main at the commit under check, local main stale', lid, m0, lid, set()),
                ('origin/main without the id, local main with it', m0, lid, m0, {'absent'}),
                ('local main only', None, lid, lid, set()),
                ('neither ref', None, None, None, {'absent'})):
            for ref, at in (('refs/remotes/origin/main', origin), ('refs/heads/main', local)):
                sc.git(['update-ref', ref, at] if at else ['update-ref', '-d', ref])
            try:
                problems, _n, _i, got_main = check_against_main(sc.repo, lid)
                got = {code for _m, code, _o, _f in problems}
            except Exception as e:          # noqa: BLE001
                got, got_main = {'crash:' + type(e).__name__}, '?'
            if got_main != want_main or got != want:
                fails.append('refs, %s: main %s, codes %s' % (name, got_main, sorted(got)))
    for f in fails:
        print('SELF-TEST  FAIL  %s' % f)
    print('citation_roles_check: self-test %s (%d mutants, %d positives, 3 negative controls, '
          '6 landing, 2 submodule, %d downgrade and 4 main-ref cases)' % (
              'OK' if not fails else 'FAILED', len(mutants), len(positives), n_down))
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
        problems, n_man, n_ids, main_c = check_against_main(repo, c)
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
