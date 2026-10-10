#!/usr/bin/env python3
"""v3_verifier.py -- the V3 verifier (round V3-2; the V3 verdict from round V3-11).

This tool implements the protocol-3 specification (verification/infrastructure/v3/architecture.md).
Its --receipts mode is the V3 verdict the release gate runs: it verifies every receipt in a
commit's tree from the commit that last wrote it and exits 1 on any receipt that does not hold. The
projection over the V2 attestation rows, and the shadow report that prints it, gate nothing. V1 and
V2 keep running beside it; they do not decide whether a native round is protocol-valid.

Entry points, exactly:

    --self-test                    internal fixtures; exit 1 on a fixture not as expected
    --corpus [DIR]                 the conformance corpus as an exact set; exit 1 on any vector not
                                   as expected (default: verification/infrastructure/v3/conformance)
    --verify-round <Q>             lifecycle T1, T3 or T5, T6 and T7 from the receipt commit Q
    --reachable <C> <Q>            a diagnostic, never a verdict: whether Q is an ancestor of C
    --receipts <C>                 every receipt in C's tree, verified from the commit reachable
                                   from C that last wrote it; exit 1 on any that does not hold
    --project <subject>            the projection of the V2 attestation rows read at <subject>
    --mode shadow --subject <C>    the corpus and the projection, reported; always exits 0

Every commit argument must be a full-length lowercase hexadecimal object id. A ref name, HEAD or
an abbreviated id is refused before any repository read: locating a commit is the caller's
business (S1). The repository is the current working directory.

Commit-local by construction: the only process-environment value read is PATH, once, below; every
git subprocess receives an explicit environment built from it and fixed literals. The tool performs
no network operation, reads no ref, host payload, clock or working-tree file of the repository
under verification, and evaluates every assertion at the commit it names (S1, S6).

Verdicts: HOLDS; FAILS with reason codes, whose prefix is the family of the settlement broken
(t1: s3: s4: s7: s8: s9: s10: s12: input:); UNDECIDABLE with one code, for an object the repository
does not contain or a shallow repository. UNDECIDABLE is never promoted to HOLDS.

It implements the settled specification: the settlements of K1-K4 and G5-G7 that round V3-3 fixed
and of G8-G12 that round V3-5 fixed. The settled rules are printed at every shadow run.

It verifies repository facts and provenance. Whether a round holds is decided from its final receipt
commit Q and the commits the receipt names; how a round's commits reach main is outside it (round
V3-8). --reachable reports whether Q is an ancestor of a commit, as a diagnostic that no verdict
reads.

Standard library only.
"""
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile

# The one read of the process environment.
_PATH = os.environ.get('PATH', '/usr/bin:/bin')

GIT_ENV = {
    'PATH': _PATH,
    'LC_ALL': 'C',
    'LANG': 'C',
    'HOME': '/nonexistent-v3-shadow',
    'GIT_CONFIG_NOSYSTEM': '1',
    'GIT_CONFIG_GLOBAL': '/dev/null',
    'GIT_TERMINAL_PROMPT': '0',
    'GIT_OPTIONAL_LOCKS': '0',
}
COMMIT_ENV = dict(GIT_ENV, **{
    'GIT_AUTHOR_NAME': 'v3-shadow', 'GIT_AUTHOR_EMAIL': 'v3-shadow@invalid',
    'GIT_AUTHOR_DATE': '1700000000 +0000',
    'GIT_COMMITTER_NAME': 'v3-shadow', 'GIT_COMMITTER_EMAIL': 'v3-shadow@invalid',
    'GIT_COMMITTER_DATE': '1700000000 +0000',
})

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_CORPUS = os.path.join(os.path.dirname(HERE), 'verification', 'infrastructure', 'v3',
                              'conformance')
ATTESTATION_DIR = 'verification/certificates/attestations/'

SETTLED = (
    'K1  the preregistration at F carries one `v3-round` block: round <id>, kind '
    '<sealing|non-sealing>, record-directory <path>/, the one directory holding every '
    'control-plane path of delta(D, F); the receipt must agree with it',
    'K2  at F the preregistration carries exactly one `v3-governed-paths` block and exactly one '
    '`v3-round` block, and no amendment carries either',
    'K3  for every reconciliation, D lies on the first-parent chain of its first parent; for i>1, '
    'the previous first parent lies on the first-parent chain of this one',
    'K4  every receipt commit, superseded or final, is a single-parent child of the reconciliation '
    'before it, changing exactly the receipt path plus the seal records the final receipt names; '
    'a superseded receipt is not read',
    'G5  the execution commits of a halted round are linear from F and change no control-plane '
    'file; their delta from F need not be authorized',
    'G6  the governed-path block at F has literal record entries for the record directory and the '
    'receipt path, no execution entry within the record directory, and no other record entry '
    'outside it but a sealing round\'s `record A` of its seal record path',
    'G7  at every commit of the round after F, superseded or final, the control-plane files are '
    'exactly those at F, each with its state at F',
    'G8  no ref, branch or host state is a predicate input; a control plane that names one changes '
    'no predicate',
    'G9  before F the control plane is a draft: its commits may add, modify or delete '
    'control-plane files, and only the declarations at F are read',
    'G10 declaration blocks are recognized by exact lines: an opener is three backticks and the '
    'info string, a closer three backticks; a near miss of a reserved info string in any '
    'control-plane file at F makes the control plane invalid',
    'G11 the reconciliations and receipt commits of the round are exactly the chain Q reaches; an '
    'abandoned attempt is not an object of the round',
    'G12 a sealing round has one seal record, verification/v3-seals/<round>.json, declared '
    '`record A` and named alone by its receipt; no round changes another round\'s receipt or V3 '
    'seal record, or any path under verification/seals/',
)

HEX = {'sha1': 40, 'sha256': 64}
ROUND_ID = re.compile(r'^[A-Z0-9]+(-[A-Z0-9]+)*$')
DIGEST = re.compile(r'^[0-9a-f]{64}$')
OPS = ('A', 'M', 'D', 'AM', 'AD', 'MD', 'AMD')
REASONS = {'halted-before-certification': ('e', 'tree_e', 'execution_delta_digest'),
           'no-execution-commits': ('withdrawal',)}


class Undecidable(Exception):
    def __init__(self, code):
        Exception.__init__(self, code)
        self.code = code


class Refused(Exception):
    def __init__(self, code):
        Exception.__init__(self, code)
        self.code = code


# ---------------------------------------------------------------------------------------------
# arguments
# ---------------------------------------------------------------------------------------------
def check_oid(s):
    """A full-length lowercase hexadecimal object id, or Refused -- decided before any read."""
    if not isinstance(s, str) or not re.fullmatch(r'[0-9a-f]+', s) or len(s) not in (40, 64):
        raise Refused('input:not-an-object-id')
    return s


# ---------------------------------------------------------------------------------------------
# git, with an explicit environment
# ---------------------------------------------------------------------------------------------
class Repo:
    def __init__(self, cwd):
        self.cwd = cwd
        self._trees = {}
        self._fmt = None

    def run(self, args, data=None, env=None, ok=(0,)):
        r = subprocess.run(['git'] + list(args), cwd=self.cwd, input=data, capture_output=True,
                           env=env or GIT_ENV)
        if r.returncode not in ok:
            return None
        return r.stdout

    def fmt(self):
        if self._fmt is None:
            out = self.run(['rev-parse', '--show-object-format'])
            if out is None:
                raise Undecidable('input:not-a-repository')
            self._fmt = out.decode().strip()
            out = self.run(['rev-parse', '--is-shallow-repository'])
            if out is not None and out.decode().strip() == 'true':
                raise Undecidable('undecidable:shallow-repository')
        return self._fmt

    def width(self):
        return HEX[self.fmt()]

    def need(self, oid):
        """oid must name a commit present in the repository."""
        if not isinstance(oid, str) or len(oid) != self.width() \
                or not re.fullmatch(r'[0-9a-f]+', oid):
            raise Undecidable('undecidable:malformed-object-id')
        if self.run(['cat-file', '-e', oid + '^{commit}']) is None:
            raise Undecidable('undecidable:object-absent')
        return oid

    def parents(self, oid):
        self.need(oid)
        return self.run(['rev-list', '--parents', '-n', '1', oid]).decode().split()[1:]

    def tree(self, oid):
        self.need(oid)
        return self.run(['rev-parse', oid + '^{tree}']).decode().strip()

    def entries(self, oid):
        """{path bytes: (mode, object id)} of the commit's tree, recursively."""
        if oid not in self._trees:
            self.need(oid)
            out = self.run(['ls-tree', '-r', '-z', '--full-tree', oid])
            m = {}
            for rec in out.split(b'\0'):
                if not rec:
                    continue
                meta, path = rec.split(b'\t', 1)
                mode, _typ, obj = meta.decode().split(' ')
                m[path] = (mode, obj)
            self._trees[oid] = m
        return self._trees[oid]

    def state(self, oid, path):
        return self.entries(oid).get(path)

    def blob(self, obj):
        out = self.run(['cat-file', 'blob', obj])
        if out is None:
            raise Undecidable('undecidable:object-absent')
        return out

    def rev_list(self, head, exclude):
        self.need(head)
        self.need(exclude)
        return self.run(['rev-list', head, '^' + exclude]).decode().split()

    def is_ancestor(self, a, b):
        self.need(a)
        self.need(b)
        rc = subprocess.run(['git', 'merge-base', '--is-ancestor', a, b], cwd=self.cwd,
                            capture_output=True, env=GIT_ENV).returncode
        if rc not in (0, 1):
            raise Undecidable('undecidable:ancestry')
        return rc == 0

    def first_parent_chain(self, oid):
        self.need(oid)
        return set(self.run(['rev-list', '--first-parent', oid]).decode().split())

    def delta(self, x, y):
        self.need(x)
        self.need(y)
        out = self.run(['diff-tree', '-r', '--raw', '--no-renames', '--no-abbrev', '-z', x, y])
        return parse_delta(out, self.fmt())


# ---------------------------------------------------------------------------------------------
# S8 -- canonical deltas
# ---------------------------------------------------------------------------------------------
class DeltaInvalid(Exception):
    pass


def parse_delta(raw, fmt):
    """Records (status, path, old_mode, old_oid, new_mode, new_oid) from the -z raw output."""
    width = HEX[fmt]
    fields = raw.split(b'\0')
    if fields and fields[-1] == b'':
        fields.pop()
    if len(fields) % 2:
        raise DeltaInvalid('s8:malformed-record')
    records, seen = [], set()
    for i in range(0, len(fields), 2):
        meta, path = fields[i], fields[i + 1]
        m = re.fullmatch(rb':([0-7]{6}) ([0-7]{6}) ([0-9a-f]+) ([0-9a-f]+) (.)', meta)
        if not m:
            raise DeltaInvalid('s8:malformed-record')
        om, nm, oo, no, st = (g.decode() for g in m.groups())
        if len(oo) != width or len(no) != width:
            raise DeltaInvalid('s8:object-id-width')
        if st not in ('A', 'D', 'M', 'T'):
            raise DeltaInvalid('s8:status-' + st)
        if path in seen:
            raise DeltaInvalid('s8:path-twice')
        seen.add(path)
        records.append((st, path, om, oo, nm, no))
    records.sort(key=lambda r: r[1])
    return records


def delta_bytes(records, fmt):
    out = b'v3-delta\0v1\0' + fmt.encode() + b'\0'
    for st, path, om, oo, nm, no in sorted(records, key=lambda r: r[1]):
        for f in (st.encode(), path, om.encode(), oo.encode(), nm.encode(), no.encode()):
            out += f + b'\0'
    return out


def delta_digest(records, fmt):
    return hashlib.sha256(delta_bytes(records, fmt)).hexdigest()


# ---------------------------------------------------------------------------------------------
# S7 -- governed-path sets
# ---------------------------------------------------------------------------------------------
def fenced_blocks(text, info):
    """The bodies of the fenced blocks whose info string is exactly `info`; None if one of them
    is not closed."""
    lines = text.split('\n')
    out, i = [], 0
    while i < len(lines):
        if lines[i] == '```' + info:
            j = i + 1
            while j < len(lines) and lines[j] != '```':
                j += 1
            if j == len(lines):
                return None
            out.append(lines[i + 1:j])
            i = j + 1
        else:
            i += 1
    return out


# G10: a line with an opener's shape for a reserved info string that is not an opener.
NEAR_MISS = re.compile(r'[ \t]*(?:`{3,}|~{3,})[ \t]*(v3-round|v3-governed-paths)(?:[ \t\r].*)?',
                       re.S)


def has_near_miss(text):
    """G10: whether a line of `text` is a near miss for a reserved info string."""
    for line in text.split('\n'):
        m = NEAR_MISS.fullmatch(line)
        if m and line != '```' + m.group(1):
            return True
    return False


def path_ok(p):
    if p == '' or '\r' in p or '\n' in p or '\t' in p or p.startswith('/') or '//' in p:
        return False
    segs = p[:-1].split('/') if p.endswith('/') else p.split('/')
    return not any(s in ('.', '..') for s in segs)


def parse_governed_lines(lines):
    """[(class, ops, path)] or a code."""
    entries, seen = [], set()
    for line in lines:
        if line.strip() == '' or line.startswith('#'):
            continue
        parts = line.split(' ', 2)
        if len(parts) != 3:
            return 's7:field-count'
        cls, ops, path = parts
        if cls not in ('execution', 'record'):
            return 's7:unknown-class'
        if ops not in OPS:
            return 's7:ops'
        if not path_ok(path):
            return 's7:path'
        if path in seen:
            return 's7:path-twice'
        seen.add(path)
        entries.append((cls, ops, path))
    return entries


def parse_governed_text(text):
    blocks = fenced_blocks(text, 'v3-governed-paths')
    if blocks is None:
        return 's7:unclosed-block'
    if len(blocks) != 1:
        return 's7:block-count'
    return parse_governed_lines(blocks[0])


def governed_bytes(entries):
    out = b'v3-governed-paths\0v1\0'
    for cls, ops, path in sorted(entries, key=lambda e: e[2].encode()):
        out += cls.encode() + b'\0' + ops.encode() + b'\0' + path.encode() + b'\0'
    return out


def governed_digest(entries):
    return hashlib.sha256(governed_bytes(entries)).hexdigest()


def governing(entries, path):
    """The entry of greatest length whose path equals `path` or is a directory prefix of it."""
    if isinstance(path, bytes):
        try:
            path = path.decode('utf-8')
        except UnicodeDecodeError:
            return None
    best = None
    for e in entries:
        p = e[2]
        if path == p or (p.endswith('/') and path.startswith(p)):
            if best is None or len(p) > len(best[2]):
                best = e
    return best


def seal_record_path(round_id):
    """G12: a sealing round's one seal record path."""
    return 'verification/v3-seals/%s.json' % round_id


def foreign(own, path):
    """G12: whether `path` is receipt or seal state that is not the round's own, where `own` is
    the round's (receipt path, seal record path or None)."""
    if isinstance(path, bytes):
        path = path.decode('utf-8', 'replace')
    return (path.startswith('verification/receipts/') and path != own[0]) \
        or path.startswith('verification/seals/') \
        or (path.startswith('verification/v3-seals/') and path != own[1])


def authorized(entries, status, path, own):
    if foreign(own, path):
        return False
    e = governing(entries, path)
    if e is None:
        return False
    return ('M' if status == 'T' else status) in e[1]


# ---------------------------------------------------------------------------------------------
# S4 -- the receipt, standalone
# ---------------------------------------------------------------------------------------------
FIELDS = ('schema', 'version', 'round', 'status', 'kind', 'object_format', 'd', 'f',
          'control_plane_blobs', 'governed_paths_digest', 'e', 'tree_e', 'execution_delta_digest',
          'withdrawal', 'candidates', 'landing', 'seal', 'attestations', 'absent')


def _dupcheck(pairs):
    keys = [k for k, _ in pairs]
    if len(keys) != len(set(keys)):
        raise ValueError('duplicate key')
    return dict(pairs)


def load_receipt(raw):
    """(object, None) or (None, code)."""
    try:
        text = raw.decode('utf-8') if isinstance(raw, bytes) else raw
        if text.startswith('﻿'):
            return None, 's4:byte-order-mark'
        obj = json.loads(text, object_pairs_hook=_dupcheck)
    except ValueError as exc:
        return None, 's4:duplicate-key' if 'duplicate' in str(exc) else 's4:not-json'
    if not isinstance(obj, dict):
        return None, 's4:not-an-object'
    return obj, None


def _oid(v, w):
    return isinstance(v, str) and len(v) == w and re.fullmatch(r'[0-9a-f]+', v) is not None


def _path(v):
    return isinstance(v, str) and path_ok(v)


def column(r):
    """complete / halted-exec / halted-none / None."""
    if r.get('status') == 'complete':
        return 'complete'
    if r.get('status') == 'halted':
        return 'halted-exec' if 'withdrawal' in r else 'halted-none'
    return None


def validate_receipt(r):
    """Codes (empty when the receipt satisfies S4 standalone)."""
    codes = []
    for k in r:
        if k not in FIELDS:
            codes.append('s4:unknown-key:' + k)
    col = column(r)
    if col is None:
        return codes + ['s4:status']
    fmt = r.get('object_format')
    w = HEX.get(fmt)
    if w is None:
        codes.append('s4:object-format')
        w = 40
    sealing = r.get('kind') == 'sealing'
    rule = {
        'schema': 'R', 'version': 'R', 'round': 'R', 'status': 'R', 'kind': 'R',
        'object_format': 'R', 'd': 'R', 'f': 'R', 'control_plane_blobs': 'R',
        'governed_paths_digest': 'R',
        'e': {'complete': 'R'}.get(col, 'A'), 'tree_e': {'complete': 'R'}.get(col, 'A'),
        'execution_delta_digest': {'complete': 'R'}.get(col, 'A'),
        'withdrawal': {'complete': '-', 'halted-exec': 'R', 'halted-none': 'A'}[col],
        'candidates': 'R', 'landing': 'R',
        'seal': 'R' if (col == 'complete' and sealing) else '-',
        'attestations': 'R', 'absent': '-' if col == 'complete' else 'R',
    }
    absent = r.get('absent', {})
    if 'absent' in r and not isinstance(absent, dict):
        codes.append('s4:absent-type')
        absent = {}
    for k, how in rule.items():
        present = k in r
        if how == 'R' and not present:
            codes.append('s4:required-missing:' + k)
        elif how == '-' and present:
            codes.append('s4:forbidden-present:' + k)
        elif how == 'A':
            if present:
                codes.append('s4:absent-field-present:' + k)
            if k not in absent:
                codes.append('s4:absent-without-reason:' + k)
    for k, code in absent.items():
        if rule.get(k) != 'A':
            codes.append('s4:reason-for-non-absent-field:' + str(k))
        if code not in REASONS:
            codes.append('s4:unknown-reason-code:' + str(code))
        elif k not in REASONS[code]:
            codes.append('s4:reason-not-admitted:' + str(k))
    if 'execution_delta_digest' in r and 'e' not in r:
        codes.append('s4:delta-digest-without-e')
    # types
    if 'schema' in r and r['schema'] != 'v3-receipt':
        codes.append('s4:schema')
    if 'version' in r and (r['version'] != 1 or isinstance(r['version'], bool)):
        codes.append('s4:version')
    if 'round' in r and not (isinstance(r['round'], str) and ROUND_ID.match(r['round'])):
        codes.append('s4:round-id')
    if 'kind' in r and r['kind'] not in ('sealing', 'non-sealing'):
        codes.append('s4:kind')
    for k in ('d', 'f', 'e', 'tree_e', 'withdrawal'):
        if k in r and not _oid(r[k], w):
            codes.append('s4:object-id:' + k)
    for k in ('governed_paths_digest', 'execution_delta_digest'):
        if k in r and not (isinstance(r[k], str) and DIGEST.match(r[k])):
            codes.append('s4:digest:' + k)
    cpb = r.get('control_plane_blobs')
    if 'control_plane_blobs' in r:
        if not (isinstance(cpb, list) and cpb and all(
                isinstance(x, dict) and set(x) == {'path', 'blob'} and _path(x['path'])
                and _oid(x['blob'], w) for x in cpb)):
            codes.append('s4:control-plane-blobs')
        elif [x['path'].encode() for x in cpb] != sorted(x['path'].encode() for x in cpb) \
                or len({x['path'] for x in cpb}) != len(cpb):
            codes.append('s4:control-plane-blobs-order')
    cand = r.get('candidates')
    if 'candidates' in r:
        if not (isinstance(cand, list) and all(
                isinstance(x, dict) and set(x) == {'commit', 'tree', 'measured'}
                and _oid(x['commit'], w) and _oid(x['tree'], w) and isinstance(x['measured'], str)
                for x in cand)):
            codes.append('s4:candidates')
        elif col == 'halted-exec' and not cand:
            codes.append('s4:candidates-empty')
        elif col == 'halted-none' and cand:
            codes.append('s4:candidates-non-empty')
    lan = r.get('landing')
    if 'landing' in r:
        ok = isinstance(lan, dict) and set(lan) == {'base', 'object', 'reconciliations',
                                                    'resolved_paths', 'delta_digest'}
        if ok:
            recs, rp = lan['reconciliations'], lan['resolved_paths']
            ok = (_oid(lan['base'], w) and _oid(lan['object'], w) and isinstance(recs, list)
                  and recs and all(_oid(x, w) for x in recs) and recs[-1] == lan['object']
                  and isinstance(rp, list) and all(_path(x) for x in rp)
                  and [x.encode() for x in rp] == sorted({x.encode() for x in rp})
                  and isinstance(lan['delta_digest'], str) and DIGEST.match(lan['delta_digest'])
                  is not None)
        if not ok:
            codes.append('s4:landing')
    seal = r.get('seal')
    if 'seal' in r:
        ok = isinstance(seal, dict) and set(seal) == {'records'} \
            and isinstance(seal['records'], list) and seal['records'] and all(
                isinstance(x, dict) and set(x) == {'path', 'blob'} and _path(x['path'])
                and _oid(x['blob'], w) for x in seal['records'])
        if ok:
            ps = [x['path'].encode() for x in seal['records']]
            ok = ps == sorted(set(ps))
        if ok and isinstance(r.get('round'), str):
            ok = ps == [seal_record_path(r['round']).encode()]
        if not ok:
            codes.append('s4:seal')
    att = r.get('attestations')
    if 'attestations' in r:
        if not (isinstance(att, list) and all(
                isinstance(x, dict) and set(x) == {'kind', 'subject', 'commit', 'record'}
                and x['kind'] in ('owner-designation', 'check-run') and x['subject'] in ('F', 'E')
                and _oid(x['commit'], w) and isinstance(x['record'], str) for x in att)):
            codes.append('s4:attestations')
        else:
            def count(kind, subj):
                return sum(1 for x in att if x['kind'] == kind and x['subject'] == subj)
            for kind in ('owner-designation', 'check-run'):
                if count(kind, 'F') < 1:
                    codes.append('s4:attestation-minimum:%s:F' % kind)
                if col == 'complete' and count(kind, 'E') < 1:
                    codes.append('s4:attestation-minimum:%s:E' % kind)
                if col != 'complete' and count(kind, 'E'):
                    codes.append('s4:attestation-for-E-in-halted-receipt')
            for x in att:
                want = r.get('f') if x['subject'] == 'F' else r.get('e')
                if want is not None and x['commit'] != want:
                    codes.append('s4:attestation-commit:%s' % x['subject'])
    return codes


# ---------------------------------------------------------------------------------------------
# the control plane at F (T1, with K1 and K2)
# ---------------------------------------------------------------------------------------------
def control_plane(repo, d, f):
    """(record_dir, round, kind, entries, {path bytes: blob}, codes)."""
    codes = []
    cp_paths = []
    for st, path, *_ in repo.delta(d, f):
        if re.fullmatch(rb'.+/(preregistration\.md|amendments/.+)', path):
            cp_paths.append(path)
        else:
            codes.append('t1:non-control-plane-change')
    # K1: the record directory is the one directory R such that every control-plane path of
    # delta(D, F) is R's preregistration.md or lies under R's amendments/.
    fits = sorted(r for r in {p[:-len(b'preregistration.md')] for p in cp_paths
                              if p.endswith(b'/preregistration.md')}
                  if all(p == r + b'preregistration.md' or p.startswith(r + b'amendments/')
                         for p in cp_paths))
    if len(fits) != 1:
        return None, None, None, None, {}, codes + ['t1:record-directory']
    (rdir,) = fits
    files = {}
    for path, (mode, obj) in repo.entries(f).items():
        if path == rdir + b'preregistration.md' or path.startswith(rdir + b'amendments/'):
            files[path] = obj
    if rdir + b'preregistration.md' not in files:
        return None, None, None, None, files, codes + ['t1:no-preregistration']
    gov_blocks, round_blocks = [], []
    for p in sorted(files):
        t = repo.blob(files[p]).decode('utf-8', 'replace')
        if has_near_miss(t):
            return None, None, None, None, files, codes + ['t1:near-miss']
        g = fenced_blocks(t, 'v3-governed-paths')
        rb = fenced_blocks(t, 'v3-round')
        if g is None or rb is None:
            return None, None, None, None, files, codes + ['t1:unclosed-block']
        if p == rdir + b'preregistration.md':
            gov_blocks += g
            round_blocks += rb
        elif g or rb:
            codes.append('t1:block-in-amendment')
    if len(gov_blocks) != 1:
        codes.append('t1:governed-block-count')
    if len(round_blocks) != 1:
        codes.append('t1:round-block-count')
    if codes:
        return None, None, None, None, files, codes
    entries = parse_governed_lines(gov_blocks[0])
    if isinstance(entries, str):
        return None, None, None, None, files, [entries]
    decl = {}
    for line in round_blocks[0]:
        if line.strip() == '' or line.startswith('#'):
            continue
        parts = line.split(' ', 1)
        if len(parts) != 2 or parts[0] not in ('round', 'kind', 'record-directory') \
                or parts[0] in decl:
            return None, None, None, None, files, ['t1:round-block']
        decl[parts[0]] = parts[1]
    if set(decl) != {'round', 'kind', 'record-directory'} or not ROUND_ID.match(decl['round']) \
            or decl['kind'] not in ('sealing', 'non-sealing') \
            or not path_ok(decl['record-directory']) or not decl['record-directory'].endswith('/'):
        return None, None, None, None, files, ['t1:round-block']
    if decl['record-directory'].encode() != rdir:
        return None, None, None, None, files, ['t1:record-directory-mismatch']
    receipt_path = 'verification/receipts/%s.json' % decl['round']
    codes += record_class_codes(entries, decl['record-directory'], receipt_path, decl['kind'], 't1')
    return rdir, decl['round'], decl['kind'], entries, files, codes


def record_class_codes(entries, rd, rp, kind, fam):
    """G6: the record class is exactly the round's own record."""
    codes = []
    seal = seal_record_path(rp[len('verification/receipts/'):-len('.json')])
    literal = {e[2] for e in entries if e[0] == 'record'}
    for p in (rd, rp):
        if p not in literal:
            codes.append(fam + ':record-class-omits:' + p)
    for cls, ops, p in entries:
        if cls == 'execution' and p.startswith(rd):
            codes.append(fam + ':execution-entry-within-record-directory')
        if cls == 'record' and p not in (rd, rp) and not p.startswith(rd):
            if kind != 'non-sealing' and p == seal and ops == 'A':
                continue
            codes.append(fam + ':record-entry-outside-own-record')
    if kind == 'sealing' and ('record', 'A', seal) not in entries:
        codes.append(fam + ':seal-record-entry')
    return codes


def check_t1(repo, d, f, cp_files):
    """Every commit of rev-list F ^D has one parent and changes only control-plane files."""
    codes = []
    if not repo.is_ancestor(d, f):
        return ['t1:d-not-ancestor']
    for c in repo.rev_list(f, d):
        ps = repo.parents(c)
        if len(ps) != 1:
            codes.append('t1:not-single-parent')
            continue
        for st, path, *_ in repo.delta(ps[0], c):
            if not re.fullmatch(rb'.+/(preregistration\.md|amendments/.+)', path):
                codes.append('t1:non-control-plane-change')
    return sorted(set(codes))


def is_control_plane(rdir, path):
    return path == rdir + b'preregistration.md' or path.startswith(rdir + b'amendments/')


def check_linear(repo, base, head, family):
    """Every commit of rev-list head ^base has one parent, that parent base or another listed."""
    if not repo.is_ancestor(base, head):
        return [family + ':not-descendant']
    listed = repo.rev_list(head, base)
    s = set(listed)
    for c in listed:
        ps = repo.parents(c)
        if len(ps) != 1 or (ps[0] not in s and ps[0] != base):
            return [family + ':not-linear']
    return []


def check_execution(repo, f, e, rdir, entries, own):
    """S3: linear from F, authorized under S7, no control-plane file changed after F."""
    codes = check_linear(repo, f, e, 's3')
    if codes:
        return codes
    for c in repo.rev_list(e, f):
        (p,) = repo.parents(c)
        if any(is_control_plane(rdir, r[1]) for r in repo.delta(p, c)):
            codes.append('s3:control-plane-changed-after-f')
            break
    for st, path, *_ in repo.delta(f, e):
        if not authorized(entries, st, path, own):
            codes.append('s3:unauthorized')
            break
    return codes


def cp_state(repo, oid, rdir):
    return {p: s for p, s in repo.entries(oid).items() if is_control_plane(rdir, p)}


def check_control_plane_frozen(repo, f, oids, rdir, family):
    """S2 and G7: at every commit of the round after F, the control-plane files have exactly
    their states at F."""
    want = cp_state(repo, f, rdir)
    for oid in oids:
        if oid is not None and cp_state(repo, oid, rdir) != want:
            return [family + ':control-plane-changed-after-f']
    return []


def check_halted_execution(repo, f, last, rdir):
    """S3's form and G5: it binds every execution commit, certified or not."""
    codes = check_linear(repo, f, last, 's12')
    if codes:
        return codes
    for c in repo.rev_list(last, f):
        (p,) = repo.parents(c)
        if any(is_control_plane(rdir, r[1]) for r in repo.delta(p, c)):
            return ['s12:control-plane-changed-after-f']
    return []


def check_withdrawal(repo, f, w, rdir, entries):
    """S12: W restores every execution path's state at F and keeps the result note."""
    codes = []
    fe, we = repo.entries(f), repo.entries(w)
    for path in set(fe) | set(we):
        g = governing(entries, path)
        if g is not None and g[0] == 'execution' and fe.get(path) != we.get(path):
            codes.append('s12:withdrawal-invariant')
            break
    if rdir + b'result.md' not in we:
        codes.append('s12:result-note-absent-at-w')
    return codes


def check_first_parent_chains(repo, d, recs):
    """K3."""
    codes, prev = [], None
    for r in recs:
        p1 = repo.parents(r)[0]
        chain = repo.first_parent_chain(p1)
        if d not in chain:
            codes.append('s9:d-not-on-first-parent-chain')
        if prev is not None and prev not in chain:
            codes.append('s9:first-parent-chain-regressed')
        prev = p1
    return codes


def check_landing_complete(repo, d, e, lb, lam, entries, resolved, receipt_path, own):
    """S9 conditions 1 to 3."""
    codes = []
    delta = repo.delta(lb, lam)
    for st, path, *_ in delta:
        if not authorized(entries, st, path, own):
            codes.append('s9:landing-unauthorized')
            break
    res = {p.encode() for p in resolved}
    for p in res:
        if governing(entries, p) is None:
            codes.append('s9:resolved-path-ungoverned')
            break
    for st, path, *_ in delta:
        if path == receipt_path or path in res:
            continue
        if repo.state(lam, path) != repo.state(e, path):
            codes.append('s9:landing-state-differs-from-e')
            break
    dpaths = {r[1] for r in delta}
    for st, path, *_ in repo.delta(d, e):
        se = repo.state(e, path)
        if path in dpaths and repo.state(lam, path) == se:
            continue
        if repo.state(lb, path) == se or path in res:
            continue
        codes.append('s9:execution-change-lost')
        break
    return codes, delta


def check_landing_halted(repo, lb, lam, entries, rdir, receipt_path, own):
    codes = []
    delta = repo.delta(lb, lam)
    for st, path, *_ in delta:
        if not (path.startswith(rdir) or path == receipt_path):
            codes.append('s12:landing-publishes-non-record-path')
            break
        if not authorized(entries, st, path, own):
            codes.append('s12:landing-unauthorized')
            break
    if rdir + b'result.md' not in repo.entries(lam):
        codes.append('s12:result-note-absent-at-landing')
    return codes, delta


def receipt_delta_ok(repo, parent, child, receipt_path, seal_paths):
    ps = repo.parents(child)
    if ps != [parent]:
        return False
    got = {r[1] for r in repo.delta(parent, child)}
    return got == {receipt_path} | set(seal_paths)


def read_receipt_at(repo, oid, path):
    st = repo.state(oid, path)
    if st is None:
        return None
    obj, err = load_receipt(repo.blob(st[1]))
    return obj if err is None else None


# ---------------------------------------------------------------------------------------------
# the round, from Q
# ---------------------------------------------------------------------------------------------
def verify_round(repo, q):
    """(verdict, codes, attestation lines)."""
    try:
        return _verify_round(repo, q)
    except Undecidable as u:
        return 'UNDECIDABLE', [u.code], []
    except DeltaInvalid as di:
        return 'FAILS', [str(di)], []


def _verify_round(repo, q):
    repo.need(q)
    qp = repo.parents(q)
    if len(qp) != 1:
        return 'FAILS', ['s10:q-not-single-parent'], []
    lam = qp[0]
    rpaths = [r[1] for r in repo.delta(lam, q)
              if re.fullmatch(rb'verification/receipts/[A-Z0-9]+(-[A-Z0-9]+)*\.json', r[1])]
    if len(rpaths) != 1:
        return 'FAILS', ['s10:receipt-path'], []
    receipt_path = rpaths[0]
    st = repo.state(q, receipt_path)
    if st is None:
        return 'FAILS', ['s10:receipt-absent'], []
    r, err = load_receipt(repo.blob(st[1]))
    if err:
        return 'FAILS', [err], []
    codes = validate_receipt(r)
    if codes:
        return 'FAILS', codes, []
    if r['object_format'] != repo.fmt():
        return 'FAILS', ['s4:object-format-mismatch'], []
    if receipt_path != ('verification/receipts/%s.json' % r['round']).encode():
        codes.append('s4:receipt-path-round')
    att = ['ATTESTATION  %s %s %s  recorded, unverified: %s'
           % (a['kind'], a['subject'], a['commit'][:12], a['record']) for a in r['attestations']]
    d, f = repo.need(r['d']), repo.need(r['f'])
    # T1 and the control plane
    rdir, rid, kind, entries, cp_files, cpc = control_plane(repo, d, f)
    codes += cpc
    if entries is None:
        return 'FAILS', codes, att
    codes += check_t1(repo, d, f, cp_files)
    own = ('verification/receipts/%s.json' % rid,
           seal_record_path(rid) if kind == 'sealing' else None)
    if r['round'] != rid:
        codes.append('s4:round-disagrees-with-f')
    if r['kind'] != kind:
        codes.append('s4:kind-disagrees-with-f')
    if r['governed_paths_digest'] != governed_digest(entries):
        codes.append('s4:governed-paths-digest')
    want = [{'path': p.decode('utf-8', 'replace'), 'blob': cp_files[p]} for p in sorted(cp_files)]
    if r['control_plane_blobs'] != want:
        codes.append('s4:control-plane-blobs-disagree-with-f')
    for c in r['candidates']:
        if repo.tree(repo.need(c['commit'])) != c['tree']:
            codes.append('s4:candidate-tree')
    lan = r['landing']
    recs = [repo.need(x) for x in lan['reconciliations']]
    if lam != lan['object']:
        codes.append('s10:q-parent-not-landing-object')
    col = column(r)
    # T3 or T5
    if col == 'complete':
        e = repo.need(r['e'])
        if repo.tree(e) != r['tree_e']:
            codes.append('s4:tree-e')
        codes += check_execution(repo, f, e, rdir, entries, own)
        if not any(x for x in codes if x.startswith('s3:')):
            if delta_digest(repo.delta(f, e), repo.fmt()) != r['execution_delta_digest']:
                codes.append('s4:execution-delta-digest')
        head_before = e
    elif col == 'halted-exec':
        w = repo.need(r['withdrawal'])
        wp = repo.parents(w)
        if len(wp) != 1 or wp[0] == f:
            codes.append('s12:withdrawal-parent')
        else:
            last = wp[0]
            codes += check_halted_execution(repo, f, last, rdir)
            if last not in [c['commit'] for c in r['candidates']]:
                codes.append('s12:last-execution-commit-not-a-candidate')
        codes += check_withdrawal(repo, f, w, rdir, entries)
        codes += check_control_plane_frozen(repo, f, [w], rdir, 's12')
        head_before = w
    else:
        c = repo.parents(recs[0])[1] if len(repo.parents(recs[0])) == 2 else None
        if c is None or repo.parents(c) != [f]:
            codes.append('s12:record-commit-not-child-of-f')
        else:
            for st_, path, *_ in repo.delta(f, c):
                if not (path.startswith(rdir) or path == receipt_path):
                    codes.append('s12:record-commit-changes-non-record-path')
                    break
            if rdir + b'result.md' not in repo.entries(c):
                codes.append('s12:result-note-absent')
            codes += check_control_plane_frozen(repo, f, [c], rdir, 's12')
        head_before = c
    # T6: reconciliations
    seal_paths = [x['path'].encode() for x in r.get('seal', {}).get('records', [])]
    prev_q = None
    for i, rc in enumerate(recs):
        ps = repo.parents(rc)
        if len(ps) != 2:
            codes.append('s9:reconciliation-not-a-two-parent-merge')
            continue
        want2 = head_before if i == 0 else prev_q
        if ps[1] != want2:
            codes.append('s9:reconciliation-second-parent')
        if i + 1 < len(recs):
            nxt = repo.parents(recs[i + 1])
            prev_q = nxt[1] if len(nxt) == 2 else None
            if prev_q is None:
                continue
            if not receipt_delta_ok(repo, rc, prev_q, receipt_path, seal_paths):
                codes.append('s10:superseded-receipt-commit')
            elif not all(authorized(entries, x[0], x[1], own) for x in repo.delta(rc, prev_q)):
                codes.append('s10:receipt-commit-unauthorized')
    codes += check_first_parent_chains(repo, d, recs)
    codes += check_control_plane_frozen(repo, f, recs, rdir, 's9')
    codes += check_control_plane_frozen(repo, f, [q], rdir, 's10')
    lb = repo.parents(lam)[0] if len(repo.parents(lam)) == 2 else None
    if lb is None or lb != lan['base']:
        codes.append('s9:landing-base')
    elif col == 'complete':
        lcodes, ldelta = check_landing_complete(repo, d, head_before, lb, lam, entries,
                                                lan['resolved_paths'], receipt_path, own)
        codes += lcodes
        if delta_digest(ldelta, repo.fmt()) != lan['delta_digest']:
            codes.append('s4:landing-delta-digest')
    else:
        lcodes, ldelta = check_landing_halted(repo, lb, lam, entries, rdir, receipt_path,
                                              own)
        codes += lcodes
        if delta_digest(ldelta, repo.fmt()) != lan['delta_digest']:
            codes.append('s4:landing-delta-digest')
    # T7: Q
    if not receipt_delta_ok(repo, lam, q, receipt_path, seal_paths):
        codes.append('s10:receipt-commit-delta')
    elif not all(authorized(entries, x[0], x[1], own) for x in repo.delta(lam, q)):
        codes.append('s10:receipt-commit-unauthorized')
    for x in r.get('seal', {}).get('records', []):
        stq = repo.state(q, x['path'].encode())
        if stq is None or stq[1] != x['blob']:
            codes.append('s10:seal-record-blob')
        g = governing(entries, x['path'])
        if g is None or g[0] != 'record':
            codes.append('s10:seal-record-not-a-record-path')
    codes = sorted(set(codes))
    return ('FAILS' if codes else 'HOLDS'), codes, att


def reachable(repo, c, q):
    """A diagnostic, never a verdict (S10): 'true' when Q is an ancestor of C, a commit being its
    own ancestor; 'false' when it is not; 'undecidable' with a code when the repository cannot
    say. No predicate reads it, and it never changes a verdict."""
    try:
        return ('true' if repo.is_ancestor(q, c) else 'false'), None
    except Undecidable as u:
        return 'undecidable', u.code


RECEIPT_DIR = b'verification/receipts/'
RECEIPT_PATH = re.compile(rb'verification/receipts/[A-Z0-9]+(-[A-Z0-9]+)*\.json')


def receipts(repo, c):
    """(all hold, lines): every receipt in C's tree, each verified from its receipt commit, the
    commit reachable from C that last wrote it. A path under verification/receipts/ that is not a
    receipt path fails, and so does a receipt whose receipt commit does not hold. UNDECIDABLE, a
    shallow repository included, is never promoted to HOLDS."""
    try:
        repo.need(c)
        paths = sorted(p for p in repo.entries(c) if p.startswith(RECEIPT_DIR))
    except Undecidable as u:
        return False, ['RECEIPTS  UNDECIDABLE  %s' % u.code]
    lines, ok = [], True
    for p in paths:
        name = p.decode('utf-8', 'replace')
        if not RECEIPT_PATH.fullmatch(p):
            lines.append('RECEIPT  %s  FAILS  s10:receipt-path' % name)
            ok = False
            continue
        out = repo.run(['rev-list', '-n', '1', c, '--', name])
        q = out.decode().strip() if out else ''
        if not q:
            lines.append('RECEIPT  %s  UNDECIDABLE  undecidable:receipt-commit' % name)
            ok = False
            continue
        verdict, codes, _att = verify_round(repo, q)
        lines.append('RECEIPT  %s  Q %s  %s%s' % (name, q, verdict,
                                                   '  ' + ', '.join(codes) if codes else ''))
        ok = ok and verdict == 'HOLDS'
    lines.append('RECEIPTS  %d receipt(s), %s' % (len(paths), 'all hold' if ok else 'NOT ALL HOLD'))
    return ok, lines


# ---------------------------------------------------------------------------------------------
# the projection: V2 attestation rows, commit-locally
# ---------------------------------------------------------------------------------------------
AXES = {'landed': ('X1', 'X2', 'X3', 'X4'), 'base-only': ('X0',)}


def _strong(repo, base, head):
    if not repo.is_ancestor(base, head):
        return False
    return all(repo.is_ancestor(base, c) for c in repo.rev_list(head, base))


def project(repo, subject):
    """Lines of the projection report, in a fixed order."""
    lines = []
    try:
        repo.need(subject)
        out = repo.run(['ls-tree', '-z', '--name-only', subject, ATTESTATION_DIR])
    except Undecidable as u:
        return ['PROJECTION  UNDECIDABLE %s' % u.code]
    names = sorted(n for n in out.split(b'\0') if n.endswith(b'.json'))
    lines.append('PROJECTION  subject %s  rows %d' % (subject, len(names)))
    cells = 0
    for n in names:
        stem = n.rsplit(b'/', 1)[1][:-5].decode()
        blob = repo.state(subject, n)
        try:
            row = json.loads(repo.blob(blob[1]).decode('utf-8'))
        except (ValueError, Undecidable):
            lines.append('ROWFINDING  %s  row-unreadable' % stem)
            continue
        kind = row.get('kind') if isinstance(row, dict) else None
        need = {'landed': ('base', 'sealed_head', 'tree', 'landing'),
                'base-only': ('base',)}.get(kind)
        if need is None or any(not isinstance(row.get(k), str) for k in need):
            lines.append('ROWFINDING  %s  row-kind-or-field' % stem)
            continue
        verdicts = {}
        for axis in AXES[kind]:
            cells += 1
            try:
                verdicts[axis] = _axis(repo, subject, kind, axis, row)
            except Undecidable as u:
                verdicts[axis] = 'UNDECIDABLE ' + u.code
        lines.append('ROW  %-6s %-9s %s' % (stem, kind, '  '.join(
            '%s=%s' % (a, verdicts[a]) for a in AXES[kind])))
        if kind == 'landed':
            lines.append('V3ONLY  %-6s %s' % (stem, _v3only(repo, row)))
    lines.append('PROJECTION  cells %d' % cells)
    return lines


def _axis(repo, subject, kind, axis, row):
    if axis == 'X0':
        b = repo.need(row['base'])
        return 'HOLDS' if repo.is_ancestor(b, subject) else 'FAILS'
    base, sealed, landing = (repo.need(row[k]) for k in ('base', 'sealed_head', 'landing'))
    if axis == 'X1':
        return 'HOLDS' if repo.tree(sealed) == row['tree'] else 'FAILS'
    if axis == 'X2':
        return 'HOLDS' if _strong(repo, base, sealed) else 'FAILS'
    ps = repo.parents(landing)
    if axis == 'X3':
        return 'HOLDS' if len(ps) == 2 and ps[1] == sealed else 'FAILS'
    return 'HOLDS' if len(ps) >= 2 and ps[1] == sealed else 'FAILS'


def _v3only(repo, row):
    try:
        base, sealed, landing = (repo.need(row[k]) for k in ('base', 'sealed_head', 'landing'))
        lin = 'linear' if not check_linear(repo, base, sealed, 'x') else 'not-linear'
        p1 = repo.parents(landing)[0]
        fp = 'base-on-first-parent-chain' if base in repo.first_parent_chain(p1) \
            else 'base-off-first-parent-chain'
        dg = delta_digest(repo.delta(base, sealed), repo.fmt())
        return '%s %s delta=%s' % (lin, fp, dg)
    except (Undecidable, DeltaInvalid) as exc:
        return 'UNDECIDABLE ' + str(exc)


# ---------------------------------------------------------------------------------------------
# synthetic repositories for the corpus
# ---------------------------------------------------------------------------------------------
class Scratch:
    """A repository built by plumbing in a temporary directory, with fixed identities and dates so
    that every object id is reproducible."""

    def __init__(self, workdir):
        self.dir = workdir
        self.repo = Repo(workdir)
        subprocess.run(['git', 'init', '-q', '--object-format=sha1', workdir],
                       capture_output=True, env=GIT_ENV, check=True)
        self.labels = {}
        self.files = {}

    def git(self, args, data=None, env=None):
        out = self.repo.run(args, data=data, env=env)
        if out is None:
            raise RuntimeError('scratch git failed: %s' % args[0])
        return out

    def _tree(self, files):
        tree = {}
        for path, (mode, content) in files.items():
            parts = path.split(b'/')
            node = tree
            for p in parts[:-1]:
                node = node.setdefault(p, {})
            node[parts[-1]] = (mode, content)
        return self._write(tree)

    def _write(self, node):
        lines = b''
        for name in sorted(node):
            v = node[name]
            if isinstance(v, dict):
                lines += b'040000 tree ' + self._write(v).encode() + b'\t' + name + b'\0'
            else:
                mode, content = v
                oid = self.git(['hash-object', '-w', '--stdin'], data=content).decode().strip()
                lines += mode.encode() + b' blob ' + oid.encode() + b'\t' + name + b'\0'
        return self.git(['mktree', '-z'], data=lines).decode().strip()

    def commit(self, label, parents, base, sets, dels):
        files = dict(self.files.get(base, {})) if base else {}
        for p in dels:
            files.pop(p, None)
        files.update(sets)
        tree = self._tree(files)
        args = ['commit-tree', tree, '-m', label]
        for p in parents:
            args += ['-p', self.labels[p]]
        oid = self.git(args, env=COMMIT_ENV).decode().strip()
        self.labels[label] = oid
        self.files[label] = files
        return oid


PLACEHOLDER = re.compile(r'\{\{([a-z]+):([^}]*)\}\}')


def render(s, sc):
    def sub(m):
        op, arg = m.group(1), m.group(2).split('|')
        if op == 'sha':
            return sc.labels[arg[0]]
        if op == 'tree':
            return sc.repo.tree(sc.labels[arg[0]])
        if op == 'blob':
            return sc.repo.state(sc.labels[arg[0]], arg[1].encode())[1]
        if op == 'gpd':
            st = sc.repo.state(sc.labels[arg[0]], arg[1].encode())
            return governed_digest(parse_governed_text(sc.repo.blob(st[1]).decode()))
        if op == 'delta':
            return delta_digest(sc.repo.delta(sc.labels[arg[0]], sc.labels[arg[1]]),
                                sc.repo.fmt())
        if op == 'textblob':
            data = arg[0].encode('utf-8')
            return hashlib.sha1(b'blob %d\0' % len(data) + data).hexdigest()
        raise KeyError(op)
    return PLACEHOLDER.sub(sub, s)


def render_obj(o, sc):
    if isinstance(o, str):
        return render(o, sc)
    if isinstance(o, list):
        return [render_obj(x, sc) for x in o]
    if isinstance(o, dict):
        return {k: render_obj(v, sc) for k, v in o.items()}
    return o


def content(spec, sc):
    if isinstance(spec, str):
        return ('100644', spec.encode('utf-8'))
    if 'json' in spec:
        return ('100644', (json.dumps(render_obj(spec['json'], sc), indent=1,
                                      ensure_ascii=False) + '\n').encode('utf-8'))
    if 'text' in spec:
        return (spec.get('mode', '100644'), render(spec['text'], sc).encode('utf-8'))
    raise ValueError('content spec')


def expect_ok(expect, verdict, codes):
    if verdict != expect['verdict']:
        return False
    fam = expect.get('family')
    return fam is None or any(c.startswith(fam + ':') for c in codes)


def run_repo_vector(vec, workdir):
    """(ok, detail)."""
    sc = Scratch(workdir)
    saved = {}
    for step in vec['steps']:
        if 'commit' in step:
            base = step.get('from', step['parents'][0] if step.get('parents') else None)
            sets = {p.encode('utf-8'): content(s, sc) for p, s in step.get('set', {}).items()}
            dels = [p.encode('utf-8') for p in step.get('del', [])]
            sc.commit(step['commit'], step.get('parents', []), base, sets, dels)
        elif 'ref' in step:
            if step.get('delete'):
                sc.git(['update-ref', '-d', step['ref']])
            else:
                sc.git(['update-ref', step['ref'], sc.labels[step['to']]])
        elif 'config' in step:
            sc.git(['config'] + step['config'])
        elif 'write' in step:
            path = os.path.join(workdir, *step['write'].split('/'))
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, 'w', encoding='utf-8') as fh:
                fh.write(step['text'])
        elif 'check' in step:
            args = [sc.labels[a] for a in step['args']]
            if step['check'] == 'verify-round':
                verdict, codes, _ = verify_round(Repo(workdir), args[0])
                got = (verdict, codes)
            elif step['check'] == 'reachable':
                state, code = reachable(Repo(workdir), args[0], args[1])
                got = (state, [code] if code else [])
            elif step['check'] == 'delta':
                r = Repo(workdir)
                got = ('HOLDS', [delta_digest(r.delta(args[0], args[1]), r.fmt())])
            else:
                return False, 'unknown check'
            if 'as' in step:
                saved[step['as']] = got
            if 'same_as' in step and saved.get(step['same_as']) != got:
                return False, 'output differs from %s' % step['same_as']
            exp = step['expect']
            if 'reachable' in exp:
                if got[0] != exp['reachable'] or ('code' in exp and got[1] != [exp['code']]):
                    return False, 'REACHABLE %s' % (got[1][0] if got[1] else got[0])
            elif 'digest' in exp:
                if got[1] != [exp['digest']]:
                    return False, 'digest %s' % (got[1][:1],)
            elif not expect_ok(exp, got[0], got[1]):
                return False, '%s %s' % (got[0], ','.join(got[1]))
        else:
            return False, 'unknown step'
    return True, ''


def run_vector(vec, cwd):
    kind = vec.get('kind')
    try:
        if kind == 's7':
            res = parse_governed_text(vec['text'])
            exp = vec['expect']
            if isinstance(res, str):
                return expect_ok(exp, 'FAILS', [res]), res
            codes = []
            rnd = vec.get('round')
            if rnd:
                codes += record_class_codes(res, rnd['record_directory'], rnd['receipt_path'],
                                            None, 's7')
            if codes:
                return expect_ok(exp, 'FAILS', codes), ','.join(codes)
            if exp['verdict'] != 'HOLDS':
                return False, 'HOLDS'
            if 'digest' in exp and governed_digest(res) != exp['digest']:
                return False, 'digest ' + governed_digest(res)
            for path, entry, ops in vec.get('governs', []):
                g = governing(res, path)
                if (g[2] if g else None) != entry or (g[1] if g else None) != ops:
                    return False, 'governs ' + path
            return True, ''
        if kind == 's8-repo':
            r = Repo(cwd)
            recs = r.delta(check_oid(vec['from']), check_oid(vec['to']))
            got = delta_digest(recs, r.fmt())
            sts = sorted({x[0] for x in recs})
            ok = got == vec['expect']['digest'] and sts == sorted(vec['expect']['statuses'])
            return ok, '' if ok else 'digest ' + got
        if kind == 's4':
            if 'receipt_text' in vec:
                obj, err = load_receipt(vec['receipt_text'])
            else:
                obj, err = vec['receipt'], None
            codes = [err] if err else validate_receipt(obj)
            verdict = 'FAILS' if codes else 'HOLDS'
            return expect_ok(vec['expect'], verdict, codes), ','.join(codes)
        if kind == 'input':
            try:
                for a in vec['argv']:
                    check_oid(a)
            except Refused as rf:
                return expect_ok(vec['expect'], 'REFUSED', [rf.code]), rf.code
            return False, 'accepted'
        if kind == 'repo':
            with tempfile.TemporaryDirectory() as td:
                return run_repo_vector(vec, os.path.join(td, 'r'))
    except Undecidable as u:
        return False, 'UNDECIDABLE ' + u.code
    except (DeltaInvalid, Refused) as exc:
        return expect_ok(vec.get('expect', {'verdict': '?'}), 'FAILS', [str(exc)]), str(exc)
    return False, 'unknown kind'


def run_corpus(corpus_dir, cwd):
    """(all as expected, lines)."""
    lines = []
    try:
        names = sorted(n for n in os.listdir(corpus_dir) if n.endswith('.json'))
    except OSError:
        return False, ['CORPUS  absent']
    ok_all, ids = True, set()
    for n in names:
        with open(os.path.join(corpus_dir, n), encoding='utf-8') as fh:
            vec = json.load(fh)
        vid = vec.get('id')
        if vid in ids or n != '%s.json' % vid:
            ok_all = False
            lines.append('VECTOR  %s  SET-NOT-EXACT' % n)
            continue
        ids.add(vid)
        ok, detail = run_vector(vec, cwd)
        ok_all &= ok
        lines.append('VECTOR  %s  %s%s' % (vid, 'AS-EXPECTED' if ok else 'NOT-AS-EXPECTED',
                                          '' if ok else '  ' + detail))
    lines.append('CORPUS  %d vector(s), %s' % (len(names), 'exact and as expected' if ok_all
                                               else 'NOT as expected'))
    return ok_all, lines


# ---------------------------------------------------------------------------------------------
# self-test
# ---------------------------------------------------------------------------------------------
G1 = ('```v3-governed-paths\nrecord AM verification/infrastructure/round-ex-1/\n'
      'record AM verification/receipts/EX-1.json\nexecution AMD tools/ex/\n'
      'execution M verification/README.md\n```\n')


def self_test():
    fails = []
    # S7: the architecture document's digest of G1 (an expected value from outside this tool)
    e = parse_governed_text(G1)
    if isinstance(e, str) or governed_digest(e) != \
            'e8bbfdef7908f026af80b86520349aa377d6963d98a995799aaf83d36251e946':
        fails.append('s7-g1-digest')
    if parse_governed_text('```v3-governed-paths\nrecord MA a/\n```\n') != 's7:ops':
        fails.append('s7-ops-order')
    # S8: the architecture document's scratch delta with LF and e-acute in a path
    with tempfile.TemporaryDirectory() as td:
        sc = Scratch(os.path.join(td, 'r'))
        sc.commit('a', [], None, {b'base.txt': ('100644', b'a\n')}, [])
        sc.commit('b', ['a'], 'a', {b'base.txt': ('100644', b'b\n'),
                                    b'dir/new\nline-\xc3\xa9.txt': ('100644', b'x')}, [])
        got = delta_digest(sc.repo.delta(sc.labels['a'], sc.labels['b']), 'sha1')
        if got != '61e4a51182e953b8cd90fe5b95031af5f531744fa5c7a75e865d460da87c36cd':
            fails.append('s8-lf-digest')
    # S4: presence rules on a minimal complete receipt
    base = {'schema': 'v3-receipt', 'version': 1, 'round': 'EX-1', 'status': 'complete',
            'kind': 'non-sealing', 'object_format': 'sha1', 'd': 'd' * 40, 'f': 'f' * 40,
            'control_plane_blobs': [{'path': 'x/preregistration.md', 'blob': '1' * 40}],
            'governed_paths_digest': '9' * 64, 'e': 'e' * 40, 'tree_e': '0' * 40,
            'execution_delta_digest': '8' * 64, 'candidates': [],
            'landing': {'base': 'b' * 40, 'object': 'c' * 40, 'reconciliations': ['c' * 40],
                        'resolved_paths': [], 'delta_digest': '7' * 64},
            'attestations': [
                {'kind': k, 'subject': s, 'commit': ('f' if s == 'F' else 'e') * 40, 'record': 'r'}
                for s in ('F', 'E') for k in ('owner-designation', 'check-run')]}
    if validate_receipt(base):
        fails.append('s4-minimal-complete')
    bad = dict(base)
    bad['withdrawal'] = 'a' * 40
    if not any(c.startswith('s4:forbidden-present') for c in validate_receipt(bad)):
        fails.append('s4-forbidden')
    # input refusal
    for a in ('HEAD', 'refs/heads/x', '9c48062'):
        try:
            check_oid(a)
            fails.append('input-' + a)
        except Refused:
            pass
    for f_ in fails:
        print('SELF-TEST  FAIL  %s' % f_)
    print('v3_verifier: self-test %s' % ('OK' if not fails else 'FAILED'))
    return 0 if not fails else 1


# ---------------------------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------------------------
USAGE = ('usage: v3_verifier.py --self-test | --corpus [DIR] | --verify-round <Q> | '
         '--reachable <C> <Q> | --receipts <C> | --project <subject> | '
         '--mode shadow --subject <commit>')


def main(argv):
    cwd = os.getcwd()
    try:
        if argv == ['--self-test']:
            return self_test()
        if argv[:1] == ['--corpus'] and len(argv) <= 2:
            ok, lines = run_corpus(argv[1] if len(argv) == 2 else DEFAULT_CORPUS, cwd)
            print('\n'.join(lines))
            return 0 if ok else 1
        if argv[:1] == ['--verify-round'] and len(argv) == 2:
            q = check_oid(argv[1])
            verdict, codes, att = verify_round(Repo(cwd), q)
            print('\n'.join(att))
            print('VERDICT  %s%s' % (verdict, '  ' + ', '.join(codes) if codes else ''))
            return 0
        if argv[:1] == ['--reachable'] and len(argv) == 3:
            c, q = check_oid(argv[1]), check_oid(argv[2])
            state, code = reachable(Repo(cwd), c, q)
            print('REACHABLE %s' % (code if code else state))
            return 0
        if argv[:1] == ['--receipts'] and len(argv) == 2:
            c = check_oid(argv[1])
            ok, lines = receipts(Repo(cwd), c)
            print('\n'.join(lines))
            return 0 if ok else 1
        if argv[:1] == ['--project'] and len(argv) == 2:
            s = check_oid(argv[1])
            print('\n'.join(project(Repo(cwd), s)))
            return 0
        if argv[:2] == ['--mode', 'shadow'] and len(argv) == 4 and argv[2] == '--subject':
            try:
                s = check_oid(argv[3])
            except Refused as rf:
                print('v3_verifier shadow report: subject refused (%s)' % rf.code)
                return 0
            print('v3_verifier shadow report -- DIAGNOSTIC: this report gates nothing; the V3 '
                  'verdict is --receipts, run by the release gate')
            print('settled rules (verification/infrastructure/v3/architecture.md):')
            for k in SETTLED:
                print('  ' + k)
            ok, lines = run_corpus(DEFAULT_CORPUS, cwd)
            print('\n'.join(lines))
            print('\n'.join(project(Repo(cwd), s)))
            print('v3_verifier: shadow report complete (%s)' % (
                'corpus as expected' if ok else 'SHADOW DEFECT: corpus not as expected'))
            return 0
    except Refused as rf:
        print('v3_verifier: refused (%s)' % rf.code)
        return 2
    print(USAGE)
    return 2


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
