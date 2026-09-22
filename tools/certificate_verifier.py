#!/usr/bin/env python3
"""certificate_verifier.py -- the generic, versioned verifier of round certificates (V6).

A landed round is DATA under this protocol: a certificate naming its protocol version, its
mandated base, its ordered control-plane artifacts, its evidence, its contributions and its
dependencies, and an attestation record naming its exact sealed head, that head's tree and its
landing merge. This verifier reads that data and derives every git-derivable fact again. It carries
no round-specific branch: no round stem appears in its logic, and the guard that installs it checks
that mechanically against this file's text.

Standard library only. Dispatches on `protocol` to a frozen per-version path.

    --mode shadow          report only; always exits 0
    --mode authoritative   exit non-zero on any failing certificate, record, policy or vector
    --self-test            the internal fixtures, no repository read
    --corpus DIR           the conformance corpus to execute (default: the checked-in one);
                           --no-corpus skips it
    --root DIR             the repository root (default: the parent of this file's directory)
    --subject certified|current-tree
                           the subject the topology rule evaluates; `current-tree` is the FAILING
                           reading the conformance corpus exercises and is never used to certify

Derivations, each fail-closed:

  B  the main merge, in first-parent order on main, of the last `execution_affecting` artifact in
     the certificate's ordered `control_plane`; the flag is carried by the artifact, never inferred.
  E  the recorded sealed head must equal the derived candidate -- the non-first parent of the
     recorded landing that passes the strengthened ancestry check -- and separately the tree of
     the sealed head must equal the recorded tree. A tree-identical commit with different parents
     is not the sealed head.
  L  the unique merge in the union of the visibility targets whose non-first parent is exactly the
     sealed head; the recorded landing must equal it. Zero, multiple and unequal-to-recorded are
     three distinct failures.
  A  the record exists, its `certificate` blob equals the certificate, and every git-derivable
     field agrees with git.

Visibility targets: on a push the reachable history of HEAD; on a pull request the real
`pull_request.head.sha` and the live `refs/remotes/origin/<base ref>`, never `pull_request.base.sha`,
a local branch or the synthetic merge. An unresolvable base ref fails closed.

The universal live rule: every evidence id of every accepted certificate resolves, through the
relocation ledger, to exactly one current path carrying its certified blob. Contributions are not
pinned. The live policy is data-only and exact-count. The legacy-owned set names at most one round
that a prior protocol still certifies; such a round is reported and no validity claim is made about
it in either direction.
"""
import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

HEX = re.compile(r'^[0-9a-f]{40}$')
CERT_DIR = os.path.join('verification', 'certificates')
SCHEMA = 'oi-round-certificate'
PROTOCOLS = (1, 2)
ORIGINS = ('translated-v1', 'bootstrap-v1', 'native-v2')
SHAPES = ('sealing', 'non-sealing', 'content-only')
TRANSLATION_FROM = ('seal-record', 'guard-block', 'round-directory')
PREDICATE_TYPES = ('blob-pinned', 'path-absent', 'file-contains', 'file-lacks')
CERT_REQUIRED = ('schema', 'protocol', 'round', 'origin', 'shape', 'dependencies', 'evidence',
                 'contributions')
CERT_TOPOLOGY = ('directory', 'control_plane', 'base')
CERT_ALLOWED = set(CERT_REQUIRED) | set(CERT_TOPOLOGY) | {'translation'}
ROW_COMMON = ('round', 'protocol', 'origin', 'kind', 'certificate', 'base')
ROW_TOPOLOGY = ('sealed_head', 'tree', 'landing')
CI_KEYS = ('exact_e', 'exact_l', 'main_push')
CLAUSE_REQUIRED = ('id', 'owner_round', 'protocol', 'predicate', 'activation', 'expiry', 'evidence')
LEGACY_ENTRY = ('stem', 'directory', 'preregistration_blob', 'base')
STEM = re.compile(r'^[A-Z][A-Z0-9]{1,7}$')


def blob_id(data):
    return hashlib.sha1(b'blob %d\x00' % len(data) + data).hexdigest()


def is_hex(v):
    return isinstance(v, str) and bool(HEX.match(v))


# ---------------------------------------------------------------------------------------------
# git
# ---------------------------------------------------------------------------------------------
class Git:
    def __init__(self, cwd):
        self.cwd = cwd

    def run(self, *args):
        try:
            r = subprocess.run(('git',) + args, cwd=self.cwd, capture_output=True, timeout=120)
        except Exception:  # noqa: BLE001 -- git unusable is a fail-closed None
            return None
        if r.returncode != 0:
            return None
        return r.stdout.decode('utf-8', 'replace')

    def rev(self, name):
        out = self.run('rev-parse', '--verify', '--quiet', name + '^{commit}')
        return out.strip() if out else None

    def exists(self, sha):
        return is_hex(sha) and self.run('cat-file', '-e', sha + '^{commit}') is not None

    def tree_of(self, sha):
        out = self.run('rev-parse', sha + '^{tree}')
        return out.strip() if out else None

    def blob_at(self, rev, path):
        out = self.run('rev-parse', '--verify', '--quiet', '%s:%s' % (rev, path))
        return out.strip() if out else None

    def parents(self, sha):
        out = self.run('rev-list', '--parents', '-n', '1', sha)
        return out.split()[1:] if out else None

    def is_ancestor(self, a, b):
        return self.run('merge-base', '--is-ancestor', a, b) is not None

    def strong_ancestry(self, base, head):
        """`base` an ancestor of `head`, and every commit of `rev-list head ^base` a descendant of
        `base`: no pre-freeze side history."""
        if not (self.exists(base) and self.exists(head)):
            return False
        if not self.is_ancestor(base, head):
            return False
        listed = self.run('rev-list', head, '^' + base)
        if listed is None:
            return False
        return all(self.is_ancestor(base, r) for r in listed.split())

    def merges_with_second_parent(self, target, sealed):
        """The merges reachable from `target` carrying `sealed` as a non-first parent."""
        out = self.run('log', '--format=%H %P', target)
        if out is None:
            return None
        found = []
        for line in out.split('\n'):
            parts = line.split()
            if len(parts) > 2 and sealed in parts[2:]:
                found.append(parts[0])
        return found

    def has_blob(self, rev, blob):
        out = self.run('ls-tree', '-r', rev)
        return None if out is None else any(
            line.split('\t')[0].split()[2] == blob for line in out.split('\n') if line.strip())

    def introducing_commits(self, target, blob):
        """The first-parent commits, from `target`, at which the artifact `blob` first entered the
        tree: present there and absent at the first parent. By blob and not by path, so a control
        plane that re-froze an existing path, or a path the layout migration later moved, is
        located at the merge that brought THAT artifact in."""
        out = self.run('log', '--first-parent', '--format=%H', '--find-object=' + blob, target)
        if out is None:
            return None
        found = []
        for sha in out.split():
            here = self.has_blob(sha, blob)
            parents = self.parents(sha)
            if here is None or parents is None:
                return None
            before = self.has_blob(parents[0], blob) if parents else False
            if here and not before:
                found.append(sha)
        return found


# ---------------------------------------------------------------------------------------------
# the store
# ---------------------------------------------------------------------------------------------
def read_json_dir(path):
    """{stem: parsed or ('error', code)} over one directory of per-record JSON files."""
    out = {}
    if not os.path.isdir(path):
        return out
    for name in sorted(os.listdir(path)):
        full = os.path.join(path, name)
        if not name.endswith('.json') or not os.path.isfile(full):
            continue
        stem = name[:-5]
        try:
            with open(full, 'rb') as fh:
                raw = fh.read()
            out[stem] = (json.loads(raw.decode('utf-8')), blob_id(raw))
        except Exception:  # noqa: BLE001 -- unreadable is a failure, never an absence
            out[stem] = (('error', 'schema:unreadable'), None)
    return out


def read_json_file(path):
    if not os.path.isfile(path):
        return None
    try:
        with open(path, 'rb') as fh:
            return json.loads(fh.read().decode('utf-8'))
    except Exception:  # noqa: BLE001
        return ('error', 'schema:unreadable')


class Store:
    def __init__(self, root):
        base = os.path.join(root, CERT_DIR)
        self.present = os.path.isdir(base)
        self.certs = {}
        self.stray = []
        for stem, (obj, blob) in read_json_dir(base).items():
            if stem in ('live-policy', 'legacy-v1-owned'):
                continue
            if not STEM.match(stem):
                self.stray.append(stem)
                continue
            self.certs[stem] = (obj, blob)
        self.rows = read_json_dir(os.path.join(base, 'attestations'))
        self.relocations = read_json_dir(os.path.join(base, 'relocations'))
        self.policy = read_json_file(os.path.join(base, 'live-policy.json'))
        self.legacy = read_json_file(os.path.join(base, 'legacy-v1-owned.json'))


# ---------------------------------------------------------------------------------------------
# schema, pure
# ---------------------------------------------------------------------------------------------
def validate_cert(stem, obj):
    """Failure codes of one certificate's schema; [] when it is well formed."""
    if isinstance(obj, tuple):
        return [obj[1]]
    if not isinstance(obj, dict):
        return ['schema:not-an-object']
    codes = []
    for f in CERT_REQUIRED:
        if f not in obj:
            codes.append('schema:missing:' + f)
    extra = sorted(set(obj) - CERT_ALLOWED)
    for k in extra:
        codes.append('schema:unknown-key:' + k)
    if codes:
        return codes
    if obj['schema'] != SCHEMA:
        codes.append('schema:schema')
    if obj['protocol'] not in PROTOCOLS or isinstance(obj['protocol'], bool):
        codes.append('schema:protocol')
    if obj['round'] != stem or not STEM.match(str(obj['round'])):
        codes.append('schema:round-filename-mismatch')
    if obj['origin'] not in ORIGINS:
        codes.append('schema:origin')
    if obj['shape'] not in SHAPES:
        codes.append('schema:shape')
    if codes:
        return codes
    if obj['shape'] == 'content-only':
        for f in ('control_plane', 'base'):
            if f in obj:
                codes.append('schema:content-only-topology:' + f)
    else:
        for f in CERT_TOPOLOGY:
            if f not in obj:
                codes.append('schema:missing:' + f)
        if not codes:
            if not is_hex(obj['base']):
                codes.append('schema:hash:base')
            cp = obj['control_plane']
            if not isinstance(cp, list) or not cp:
                codes.append('schema:control-plane')
            else:
                for e in cp:
                    if not (isinstance(e, dict) and set(e) == {'path', 'blob', 'merge',
                                                              'execution_affecting'}):
                        codes.append('schema:control-plane-entry')
                        break
                    if not (is_hex(e['blob']) and is_hex(e['merge'])
                            and isinstance(e['execution_affecting'], bool)
                            and isinstance(e['path'], str) and e['path']):
                        codes.append('schema:control-plane-entry')
                        break
    if 'directory' in obj and not (isinstance(obj['directory'], str) and obj['directory']
                                   and not obj['directory'].startswith('/')):
        codes.append('schema:directory')
    if not isinstance(obj['dependencies'], list) or not all(
            isinstance(d, str) and STEM.match(d) for d in obj['dependencies']):
        codes.append('schema:dependencies')
    if not isinstance(obj['evidence'], list):
        codes.append('schema:evidence')
    else:
        seen = set()
        for e in obj['evidence']:
            if not (isinstance(e, dict) and set(e) == {'id', 'path', 'blob'}
                    and isinstance(e['id'], str) and isinstance(e['path'], str)):
                codes.append('schema:evidence-entry')
                break
            if not is_hex(e['blob']):
                codes.append('schema:hash:evidence')
                break
            if e['id'] in seen:
                codes.append('schema:evidence-duplicate-id')
                break
            seen.add(e['id'])
    if not isinstance(obj['contributions'], list) or not all(
            isinstance(c, dict) and set(c) == {'path'} and isinstance(c['path'], str)
            for c in obj['contributions']):
        codes.append('schema:contributions')
    if obj['origin'] == 'translated-v1':
        t = obj.get('translation')
        if t is None:
            codes.append('schema:missing:translation')
        elif not (isinstance(t, dict) and set(t) == {'from', 'migration_snapshot'}
                  and t['from'] in TRANSLATION_FROM and is_hex(t['migration_snapshot'])):
            codes.append('schema:translation')
    elif 'translation' in obj:
        codes.append('schema:forbidden:translation')
    return codes


def validate_row(stem, obj):
    """Failure codes of one attestation record's schema; [] when well formed."""
    if isinstance(obj, tuple):
        return [obj[1]]
    if not isinstance(obj, dict):
        return ['row:schema:not-an-object']
    codes = []
    for f in ROW_COMMON:
        if f not in obj:
            codes.append('row:schema:missing:' + f)
    if codes:
        return codes
    if obj['round'] != stem:
        codes.append('row:schema:round-filename-mismatch')
    if obj['protocol'] not in PROTOCOLS or isinstance(obj['protocol'], bool):
        codes.append('row:schema:protocol')
    if obj['origin'] not in ORIGINS:
        codes.append('row:schema:origin')
    if obj['kind'] not in ('landed', 'base-only'):
        codes.append('row:schema:kind')
    if not is_hex(obj['certificate']):
        codes.append('row:schema:hash:certificate')
    if not is_hex(obj['base']):
        codes.append('row:schema:hash:base')
    if codes:
        return codes
    allowed = set(ROW_COMMON)
    if obj['kind'] == 'landed':
        for f in ROW_TOPOLOGY:
            if f not in obj:
                codes.append('row:schema:missing:' + f)
            elif not is_hex(obj[f]):
                codes.append('row:schema:hash:' + f)
        allowed |= set(ROW_TOPOLOGY)
    else:
        # forbidden means forbidden, not tolerated: a base-only record carrying `sealed_head: null`
        # is a seal asserted for a round that has none
        for f in ROW_TOPOLOGY:
            if f in obj:
                codes.append('row:schema:base-only-topology:' + f)
    if obj['origin'] == 'translated-v1':
        if 'ci' in obj:
            codes.append('row:schema:ci-forbidden')
        if 'migration_snapshot' not in obj:
            codes.append('row:schema:missing:migration_snapshot')
        elif not is_hex(obj['migration_snapshot']):
            codes.append('row:schema:hash:migration_snapshot')
        allowed.add('migration_snapshot')
    else:
        if 'migration_snapshot' in obj:
            codes.append('row:schema:migration-snapshot-forbidden')
        ci = obj.get('ci')
        if ci is None:
            codes.append('row:schema:missing:ci')
        elif not (isinstance(ci, dict) and set(ci) == set(CI_KEYS) and all(
                isinstance(ci[k], dict) and set(ci[k]) == {'run', 'head_sha', 'conclusion'}
                and is_hex(ci[k]['head_sha']) for k in CI_KEYS)):
            codes.append('row:schema:ci')
        allowed.add('ci')
    for k in sorted(set(obj) - allowed):
        codes.append('row:schema:unknown-key:' + k)
    return codes


def validate_relocations(records):
    """The ledger of relocation events as a whole: seq contiguous from 1, records well formed."""
    codes = []
    rows = []
    for name, (obj, _blob) in sorted(records.items()):
        if isinstance(obj, tuple) or not isinstance(obj, dict):
            codes.append('relocation:schema:' + name)
            continue
        if set(obj) != {'seq', 'evidence_id', 'from', 'to', 'blob', 'authorizing_round'}:
            codes.append('relocation:schema:' + name)
            continue
        if not (isinstance(obj['seq'], int) and not isinstance(obj['seq'], bool)
                and is_hex(obj['blob']) and isinstance(obj['from'], str)
                and isinstance(obj['to'], str) and isinstance(obj['evidence_id'], str)
                and STEM.match(str(obj['authorizing_round']))):
            codes.append('relocation:schema:' + name)
            continue
        rows.append(obj)
    rows.sort(key=lambda r: r['seq'])
    seqs = [r['seq'] for r in rows]
    if seqs != list(range(1, len(seqs) + 1)):
        codes.append('relocation:seq')
    return codes, rows


def validate_policy(obj):
    if obj is None:
        return ['live-policy:missing'], []
    if isinstance(obj, tuple) or not isinstance(obj, dict):
        return ['live-policy:schema'], []
    if set(obj) != {'protocol', 'count', 'policies'} or obj['protocol'] != 2:
        return ['live-policy:schema'], []
    if not isinstance(obj['policies'], list):
        return ['live-policy:schema'], []
    codes = []
    if obj['count'] != len(obj['policies']):
        codes.append('live-policy:count')
    for i, c in enumerate(obj['policies']):
        if not isinstance(c, dict):
            codes.append('live-policy:clause:%d' % i)
            continue
        for f in CLAUSE_REQUIRED:
            if f not in c or c[f] in (None, '', [], {}):
                codes.append('live-policy:clause:%s:missing:%s' % (c.get('id', i), f))
        p = c.get('predicate')
        if not (isinstance(p, dict) and p.get('type') in PREDICATE_TYPES):
            codes.append('live-policy:clause:%s:predicate-type' % c.get('id', i))
    return codes, obj['policies']


def validate_legacy(obj):
    if obj is None:
        return ['legacy-owned:missing'], []
    if isinstance(obj, tuple) or not isinstance(obj, dict):
        return ['legacy-owned:schema'], []
    if set(obj) != {'protocol', 'count', 'rounds'} or obj['protocol'] != 2 \
            or not isinstance(obj['rounds'], list):
        return ['legacy-owned:schema'], []
    codes = []
    if obj['count'] != len(obj['rounds']):
        codes.append('legacy-owned:count')
    if len(obj['rounds']) > 1:
        codes.append('legacy-owned:more-than-one')
    entries = []
    for e in obj['rounds']:
        if not (isinstance(e, dict) and set(e) == set(LEGACY_ENTRY) and STEM.match(str(e['stem']))
                and is_hex(e['preregistration_blob']) and is_hex(e['base'])
                and isinstance(e['directory'], str)):
            codes.append('legacy-owned:entry')
            continue
        entries.append(e)
    return codes, entries


def eval_predicate(root, p):
    """One live-policy predicate on the current tree. True when it holds."""
    path = os.path.join(root, *str(p.get('path', '')).split('/'))
    t = p.get('type')
    if t == 'path-absent':
        return not os.path.exists(path)
    if not os.path.isfile(path):
        return False
    with open(path, 'rb') as fh:
        data = fh.read()
    if t == 'blob-pinned':
        return blob_id(data) == p.get('blob')
    text = data.decode('utf-8', 'replace')
    if t == 'file-contains':
        return str(p.get('text', '')) in text
    if t == 'file-lacks':
        return str(p.get('text', '')) not in text
    return False


# ---------------------------------------------------------------------------------------------
# visibility
# ---------------------------------------------------------------------------------------------
def visibility_targets(env, git):
    """[(sha, label)], or (None, code) to fail closed."""
    if not str(env.get('GITHUB_EVENT_NAME', '')).startswith('pull_request'):
        head = git.rev('HEAD')
        if head is None:
            return None, 'visibility:head-unresolvable'
        return [(head, 'HEAD')], None
    path = env.get('GITHUB_EVENT_PATH', '')
    if not path or not os.path.exists(path):
        return None, 'visibility:no-event-payload'
    try:
        with open(path, encoding='utf-8') as fh:
            pr = json.load(fh)['pull_request']
        head = pr['head']['sha']
        base_ref = (pr.get('base') or {}).get('ref') or env.get('GITHUB_BASE_REF')
    except Exception:  # noqa: BLE001
        return None, 'visibility:event-payload'
    if not is_hex(head):
        return None, 'visibility:head-sha'
    if not isinstance(base_ref, str) or not base_ref or base_ref.startswith('-') \
            or not re.fullmatch(r'[0-9A-Za-z._][0-9A-Za-z._/-]*', base_ref):
        return None, 'visibility:base-ref-unresolvable'
    tip = git.rev('refs/remotes/origin/%s' % base_ref)
    if tip is None:
        # a local refs/heads/<ref> is not accepted in its place, and neither is
        # pull_request.base.sha: neither is evidence of the live base branch tip
        return None, 'visibility:base-ref-unresolvable'
    if not git.exists(head):
        return None, 'visibility:head-absent'
    return [(head, 'pull_request.head.sha'), (tip, 'refs/remotes/origin/%s' % base_ref)], None


# ---------------------------------------------------------------------------------------------
# the derivations
# ---------------------------------------------------------------------------------------------
def derive_base(cert, targets, git):
    """Codes for the B derivation of one certificate with a control plane."""
    codes = []
    last = None
    for entry in cert['control_plane']:
        cands = set()
        for tgt, _lab in targets:
            got = git.introducing_commits(tgt, entry['blob'])
            if got is None:
                return ['base:git']
            cands.update(got)
        if not cands:
            codes.append('base:zero-candidates')
            continue
        if len(cands) > 1:
            codes.append('base:multiple-candidates')
            continue
        (merge,) = cands
        if merge != entry['merge']:
            codes.append('base:merge-disagreement')
            continue
        if entry['execution_affecting']:
            last = merge
    if codes:
        return codes
    if last is None:
        return ['base:no-execution-affecting']
    if last != cert['base']:
        return ['base:disagreement']
    return []


def derive_landed(row, targets, git, subject):
    """Codes for the E, tree(E) and L derivations of one landed record."""
    base, sealed, landing, tree = row['base'], row['sealed_head'], row['landing'], row['tree']
    if not git.exists(base):
        return ['base:unreachable']
    if not git.exists(sealed):
        return ['sealed-head:unrecoverable']
    if not git.exists(landing):
        return ['landing:unrecoverable']
    codes = []
    # E from the recorded landing: the non-first parents passing the strengthened check
    parents = git.parents(landing) or []
    cands = [p for p in parents[1:] if git.strong_ancestry(base, p)]
    if not cands:
        codes.append('sealed-head:zero-candidates')
    elif len(cands) > 1:
        codes.append('sealed-head:multiple-candidates')
    elif cands[0] != sealed:
        codes.append('sealed-head:disagreement')
    # tree(E), separately: the ancestry proposition is about the commit, the tree about content
    if subject == 'current-tree':
        head = git.rev('HEAD')
        got = git.tree_of(head) if head else None
    else:
        got = git.tree_of(sealed)
    if got != tree:
        codes.append('topology:tree-mismatch')
    if not git.strong_ancestry(base, sealed):
        codes.append('topology:ancestry')
    # L over the union of the visibility targets
    found = set()
    for tgt, _lab in targets:
        got = git.merges_with_second_parent(tgt, sealed)
        if got is None:
            return codes + ['landing:git']
        found.update(got)
    if not found:
        codes.append('landing:zero-candidates')
    elif len(found) > 1:
        codes.append('landing:multiple-candidates')
    elif next(iter(found)) != landing:
        codes.append('landing:disagreement')
    return codes


def derive_base_only(row, targets, git):
    if not git.exists(row['base']):
        return ['base:unreachable']
    if not any(git.is_ancestor(row['base'], tgt) for tgt, _lab in targets):
        return ['base:unreachable']
    return []


# ---------------------------------------------------------------------------------------------
# the evidence rule
# ---------------------------------------------------------------------------------------------
def resolve_evidence(root, certs_ok, relocations):
    """Every evidence id of every accepted certificate resolves through the relocation chain to
    exactly one current path carrying its certified blob. Returns (codes, resolved_count)."""
    codes = []
    known = {}
    for stem, cert in certs_ok.items():
        for e in cert['evidence']:
            known[e['id']] = (e['path'], e['blob'])
    by_id = {}
    for r in relocations:
        by_id.setdefault(r['evidence_id'], []).append(r)
    for r in relocations:
        if r['evidence_id'] not in known:
            codes.append('relocation:unknown-evidence:%s' % r['evidence_id'])
    resolved = 0
    for eid, (path, blob) in sorted(known.items()):
        chain = sorted(by_id.get(eid, []), key=lambda r: r['seq'])
        cur = path
        sources = []
        ok = True
        for r in chain:
            if r['from'] != cur:
                codes.append('relocation:missing-source:%s' % eid)
                ok = False
                break
            if r['blob'] != blob:
                codes.append('relocation:blob-mismatch:%s' % eid)
                ok = False
                break
            same_from = [x for x in chain if x['from'] == r['from']]
            if len(same_from) > 1:
                codes.append('relocation:fork:%s' % eid)
                ok = False
                break
            sources.append(cur)
            cur = r['to']
        if not ok:
            continue
        full = os.path.join(root, *cur.split('/'))
        if not os.path.isfile(full):
            codes.append('evidence:missing:%s' % eid)
            continue
        with open(full, 'rb') as fh:
            if blob_id(fh.read()) != blob:
                codes.append('evidence:blob-mismatch:%s' % eid)
                continue
        for s in sources:
            if os.path.exists(os.path.join(root, *s.split('/'))):
                codes.append('relocation:duplicate-active:%s' % eid)
                ok = False
                break
        if ok:
            resolved += 1
    return codes, resolved


# ---------------------------------------------------------------------------------------------
# the evaluation of one repository
# ---------------------------------------------------------------------------------------------
class Result:
    def __init__(self):
        self.lines = []
        self.codes = []
        self.certs = {}      # stem -> (verdict, codes)
        self.rows = {}       # stem -> (kind, verdict, codes)
        self.legacy = []
        self.policies = 0
        self.evidence = (0, 0)
        self.targets = []

    def fail(self, *codes):
        self.codes.extend(codes)

    def ok(self):
        return not self.codes


def evaluate(root, env, subject='certified'):
    res = Result()
    git = Git(root)
    store = Store(root)
    if not store.present:
        res.fail('store:absent')
        return res
    targets, code = visibility_targets(env, git)
    if targets is None:
        res.fail(code)
        res.lines.append('  TARGETS  fail-closed: %s' % code)
        return res
    res.targets = targets
    res.lines.append('  TARGETS  ' + '; '.join('%s %s' % (lab, sha[:12]) for sha, lab in targets))
    for name in store.stray:
        res.fail('store:stray-file:' + name)

    # -- schema of every object ---------------------------------------------------------------
    certs = {}
    cert_codes = {}
    for stem, (obj, _blob) in sorted(store.certs.items()):
        codes = validate_cert(stem, obj)
        cert_codes[stem] = codes
        if not codes:
            certs[stem] = obj
    rows = {}
    row_codes = {}
    for stem, (obj, _blob) in sorted(store.rows.items()):
        codes = validate_row(stem, obj)
        row_codes[stem] = codes
        if not codes:
            rows[stem] = obj
    reloc_codes, relocations = validate_relocations(store.relocations)
    policy_codes, policies = validate_policy(store.policy)
    legacy_codes, legacy = validate_legacy(store.legacy)

    # -- provenance across the corpus ---------------------------------------------------------
    boot = [s for s, c in certs.items() if c['origin'] == 'bootstrap-v1']
    if len(boot) > 1:
        for s in boot:
            cert_codes[s].append('provenance:second-bootstrap')
    for stem, cert in certs.items():
        if cert['shape'] == 'content-only' and stem in store.rows:
            cert_codes[stem].append('row:content-only')
        elif cert['origin'] == 'translated-v1' and cert['shape'] != 'content-only' \
                and stem not in store.rows:
            cert_codes[stem].append('ledger:row-missing')
    for stem in store.rows:
        if stem not in store.certs:
            row_codes[stem].append('ledger:row-without-certificate')

    # -- the legacy-owned set -----------------------------------------------------------------
    for e in legacy:
        stem = e['stem']
        if stem in store.certs:
            legacy_codes.append('legacy-owned:has-certificate:' + stem)
        if stem in store.rows:
            legacy_codes.append('legacy-owned:has-row:' + stem)
        pre = os.path.join(root, 'verification', *e['directory'].split('/'), 'preregistration.md')
        got = None
        if os.path.isfile(pre):
            with open(pre, 'rb') as fh:
                got = blob_id(fh.read())
        if got != e['preregistration_blob']:
            legacy_codes.append('legacy-owned:preregistration:' + stem)
        if not git.exists(e['base']):
            legacy_codes.append('legacy-owned:base:' + stem)
        res.legacy.append(stem)
        res.lines.append('  LEGACY-V1-OWNED  %s  (a prior protocol certifies it; no validity '
                         'claim is made here in either direction)' % stem)
    # a certificate for a stem in the set is that stem's own failure as well
    for e in legacy:
        if e['stem'] in cert_codes:
            cert_codes[e['stem']].append('legacy-owned:certificate-for-owned-stem')

    # -- derivations --------------------------------------------------------------------------
    derived = {}
    for stem, cert in certs.items():
        if cert['shape'] != 'content-only':
            derived[stem] = derive_base(cert, targets, git)
            cert_codes[stem].extend(derived[stem])
    for stem, row in rows.items():
        codes = []
        cert = certs.get(stem)
        if cert is None:
            codes.append('row:certificate-invalid')
        else:
            if row['protocol'] != cert['protocol'] or row['origin'] != cert['origin']:
                codes.append('row:certificate-mismatch:identity')
            if cert['shape'] == 'content-only':
                codes.append('row:content-only')
            elif row['base'] != cert['base']:
                codes.append('row:base-mismatch')
            if cert['origin'] == 'translated-v1':
                want = store.certs[stem][1]
            else:
                want = git.blob_at(row['sealed_head'], '%s/%s.json' % (CERT_DIR.replace(os.sep, '/'), stem)) \
                    if row['kind'] == 'landed' else store.certs[stem][1]
            if row['certificate'] != want:
                codes.append('row:certificate-mismatch')
        if row['kind'] == 'landed':
            codes.extend(derive_landed(row, targets, git, subject))
        else:
            codes.extend(derive_base_only(row, targets, git))
        row_codes[stem].extend(codes)

    # -- dependencies, to a fixpoint ----------------------------------------------------------
    verdict = {}
    for stem in store.certs:
        verdict[stem] = 'FAIL' if cert_codes[stem] else 'PASS'
        if stem in store.rows and row_codes[stem]:
            verdict[stem] = 'FAIL'
    for _round in range(len(store.certs) + 1):
        changed = False
        for stem, cert in certs.items():
            for dep in cert['dependencies']:
                if dep not in store.certs:
                    code = 'dependency:missing:' + dep
                elif dep in certs and certs[dep]['protocol'] > cert['protocol']:
                    code = 'dependency:protocol-order:' + dep
                elif verdict.get(dep) == 'FAIL':
                    code = 'dependency:failed:' + dep
                else:
                    continue
                if code not in cert_codes[stem]:
                    cert_codes[stem].append(code)
                    verdict[stem] = 'FAIL'
                    changed = True
        if not changed:
            break

    # -- the live rules -----------------------------------------------------------------------
    accepted = {s: certs[s] for s in certs if verdict[s] == 'PASS'}
    ev_codes, resolved = resolve_evidence(root, accepted, relocations)
    res.evidence = (resolved, len(ev_codes))
    pol_viol = []
    for c in policies:
        if isinstance(c, dict) and isinstance(c.get('predicate'), dict) \
                and c['predicate'].get('type') in PREDICATE_TYPES:
            if not eval_predicate(root, c['predicate']):
                pol_viol.append('live-policy:violated:%s' % c.get('id'))
            res.lines.append('  POLICY  %s  owner %s' % (c.get('id'), c.get('owner_round')))
    res.policies = len(policies)

    # -- report -------------------------------------------------------------------------------
    for stem in sorted(store.certs):
        codes = cert_codes[stem]
        v = verdict[stem]
        if v == 'PASS' and stem not in store.rows and certs[stem]['origin'] != 'translated-v1' \
                and certs[stem]['shape'] != 'content-only':
            v = 'UNATTESTED'
        res.certs[stem] = (v, codes)
        res.lines.append('  CERT  %-8s %-10s %s' % (stem, v, ', '.join(codes) if codes else 'ok'))
        res.codes.extend('%s:%s' % (stem, c) for c in codes)
    for stem in sorted(store.rows):
        codes = row_codes[stem]
        kind = rows[stem]['kind'] if stem in rows else '?'
        res.rows[stem] = (kind, 'FAIL' if codes else 'PASS', codes)
        res.lines.append('  ROW   %-8s %-10s %s  %s' % (stem, kind, 'FAIL' if codes else 'PASS',
                                                      ', '.join(codes) if codes else 'ok'))
        res.codes.extend('%s:%s' % (stem, c) for c in codes)
    for code in reloc_codes + ev_codes + policy_codes + pol_viol + legacy_codes:
        res.codes.append(code)
    res.lines.append('  EVIDENCE  %d id(s) resolved to their certified blobs, %d failure(s)'
                     % (resolved, len(ev_codes)))
    res.lines.append('  RELOCATIONS  %d record(s)' % len(relocations))
    res.lines.append('  POLICIES  %d clause(s)' % len(policies))
    return res


# ---------------------------------------------------------------------------------------------
# the conformance corpus
# ---------------------------------------------------------------------------------------------
PLACEHOLDER = re.compile(r'\{\{(sha|tree|blob):([A-Za-z0-9_-]+)(?::([^}]+))?\}\}')


def build_repo(recipe, workdir):
    """A synthetic repository from a recipe: commits built with commit-tree so parent order is
    exact, each commit's tree stated in full (or inherited from another commit and overridden),
    placeholders resolved to the SHAs, trees and blobs of commits already built."""
    def g(*a, env=None):
        e = dict(os.environ)
        e.update(env or {})
        r = subprocess.run(('git',) + a, cwd=workdir, capture_output=True, text=True, env=e)
        if r.returncode != 0:
            raise RuntimeError('git %s: %s' % (' '.join(a), r.stderr.strip()))
        return r.stdout.strip()

    g('init', '-q', '-b', 'main')
    g('config', 'user.email', 'corpus@example.invalid')
    g('config', 'user.name', 'corpus')
    g('config', 'commit.gpgsign', 'false')
    shas, trees, files_at = {}, {}, {}

    def subst(text, self_files=None):
        def rep(m):
            kind, name, path = m.group(1), m.group(2), m.group(3)
            if kind == 'sha':
                return shas[name]
            if kind == 'tree':
                return trees[name]
            if name == 'self':
                return blob_id(self_files[path].encode('utf-8'))
            return blob_id(files_at[name][path].encode('utf-8'))
        return PLACEHOLDER.sub(rep, text)

    for c in recipe['commits']:
        files = dict(files_at[c['inherit']]) if c.get('inherit') else {}
        for p in c.get('delete', []):
            files.pop(p, None)
        for p, content in c.get('files', {}).items():
            files[p] = content
        # pass 1: placeholders naming earlier commits; pass 2: self blobs
        first = {p: (v if '{{blob:self:' in v else subst(v)) for p, v in files.items()}
        final = {p: subst(v, self_files=first) for p, v in first.items()}
        index = os.path.join(workdir, '.git', 'index-' + c['name'])
        env = {'GIT_INDEX_FILE': index}
        for p, content in sorted(final.items()):
            bid = subprocess.run(['git', 'hash-object', '-w', '--stdin'], cwd=workdir,
                                 input=content.encode('utf-8'), capture_output=True).stdout.decode().strip()
            g('update-index', '--add', '--cacheinfo', '100644,%s,%s' % (bid, p), env=env)
        tree = g('write-tree', env=env)
        args = ['commit-tree', tree, '-m', c['name']]
        for p in c.get('parents', []):
            args += ['-p', shas[p]]
        sha = g(*args)
        shas[c['name']], trees[c['name']], files_at[c['name']] = sha, tree, final
    for ref, name in recipe.get('refs', {}).items():
        g('update-ref', ref, shas[name])
    head = recipe['head']
    g('update-ref', 'refs/heads/main', shas[head])
    g('checkout', '-q', '--force', shas[recipe.get('checkout', head)])
    return shas


def vector_env(vec, shas, workdir):
    ev = vec.get('event', {'name': 'push'})
    if ev.get('name') != 'pull_request':
        return {'GITHUB_EVENT_NAME': 'push'}
    payload = {'pull_request': {'number': 1, 'head': {'sha': shas[ev['head']]},
                                'base': {'ref': ev.get('base_ref', 'main'),
                                         'sha': shas[ev['base_sha']] if ev.get('base_sha') else None}}}
    path = os.path.join(workdir, '.git', 'event.json')
    with open(path, 'w', encoding='utf-8') as fh:
        json.dump(payload, fh)
    return {'GITHUB_EVENT_NAME': 'pull_request', 'GITHUB_EVENT_PATH': path}


def exact_set(executed, corpus):
    """The vacuity guard: the executed vector set equals the corpus exactly."""
    executed, corpus = list(executed), list(corpus)
    if len(executed) != len(corpus):
        return ['vacuity:count']
    if sorted(executed) != sorted(corpus):
        return ['vacuity:ids']
    if len(set(executed)) != len(executed):
        return ['vacuity:duplicate']
    return []


def run_vector(vec, corpus_ids):
    """(verdict, reason, codes) of one vector."""
    ev = vec.get('evaluate', 'verify')
    if ev.startswith('vacuity:'):
        ids = list(corpus_ids)
        if ev == 'vacuity:fewer':
            ids = ids[:-1]
        elif ev == 'vacuity:substituted':
            ids = ids[:-1] + ['not-a-vector']
        codes = exact_set(ids, corpus_ids)
        return ('FAIL' if codes else 'PASS'), (codes[0] if codes else 'ok'), codes
    workdir = tempfile.mkdtemp(prefix='cert-corpus-')
    try:
        shas = build_repo(vec['repo'], workdir)
        env = vector_env(vec, shas, workdir)
        if ev == 'subject:current-tree':
            certified = evaluate(workdir, env, subject='certified')
            if not certified.ok():
                return 'FAIL', 'certified-subject-fails', certified.codes
            res = evaluate(workdir, env, subject='current-tree')
        else:
            res = evaluate(workdir, env)
        want = vec.get('expect', {}).get('reason')
        bare = [c.split(':', 1)[1] if c.split(':', 1)[0] in res.certs or c.split(':', 1)[0] in res.rows
                else c for c in res.codes]
        if 'require_legacy' in vec and sorted(res.legacy) != sorted(vec['require_legacy']):
            return 'FAIL', 'legacy-owned-not-reported', bare
        if not res.codes:
            return 'PASS', 'ok', []
        hit = [c for c in bare if want and (c == want or c.startswith(want + ':'))]
        return 'FAIL', (hit[0] if hit else bare[0]), bare
    except Exception as exc:  # noqa: BLE001 -- a vector that cannot be built is a mismatch
        return 'ERROR', 'exception:%s' % type(exc).__name__, []
    finally:
        shutil.rmtree(workdir, ignore_errors=True)


def run_corpus(corpus_dir, out):
    """Executes every vector, prints each id and verdict, and requires the executed set to equal
    the corpus exactly. Returns the failure codes."""
    codes = []
    expected_path = os.path.join(corpus_dir, 'expected.json')
    expected = read_json_file(expected_path)
    if not isinstance(expected, dict):
        return ['vacuity:expected-missing']
    vectors = {}
    for name in sorted(os.listdir(corpus_dir)):
        if name.endswith('.json') and name != 'expected.json':
            v = read_json_file(os.path.join(corpus_dir, name))
            if not isinstance(v, dict) or 'id' not in v:
                codes.append('vacuity:unreadable-vector:' + name)
                continue
            if v['id'] != name[:-5]:
                codes.append('vacuity:vector-id-filename:' + name)
                continue
            vectors[v['id']] = v
    corpus_ids = sorted(expected)
    families = {}
    executed = []
    mismatches = 0
    for vid in sorted(vectors):
        vec = vectors[vid]
        exp = expected.get(vid)
        if exp != vec.get('expect'):
            codes.append('vacuity:expected-mismatch:' + vid)
            continue
        verdict, reason, _bare = run_vector(vec, corpus_ids)
        executed.append(vid)
        families[vec.get('family', '?')] = families.get(vec.get('family', '?'), 0) + 1
        want_v, want_r = (exp or {}).get('verdict'), (exp or {}).get('reason')
        match = verdict == want_v and (verdict == 'PASS' or reason == want_r
                                       or reason.startswith(str(want_r) + ':'))
        if not match:
            mismatches += 1
            codes.append('vector:%s:%s/%s' % (vid, verdict, reason))
        out('  VECTOR  %-52s %-5s %-44s %s' % (vid, verdict, reason, 'MATCH' if match else 'MISMATCH'))
    codes.extend(exact_set(executed, corpus_ids))
    out('  VECTORS executed %d; corpus %d; families %s; mismatches %d; exact %s'
        % (len(executed), len(corpus_ids),
           ' '.join('%s=%d' % kv for kv in sorted(families.items())), mismatches,
           'yes' if executed and sorted(executed) == corpus_ids else 'NO'))
    return codes


# ---------------------------------------------------------------------------------------------
# self-test
# ---------------------------------------------------------------------------------------------
def self_test():
    ok = True
    h = '0' * 40
    good = {'schema': SCHEMA, 'protocol': 2, 'round': 'ZZ', 'origin': 'native-v2',
            'shape': 'non-sealing', 'directory': 'x/y', 'base': h,
            'control_plane': [{'path': 'a.md', 'blob': h, 'merge': h, 'execution_affecting': True}],
            'dependencies': [], 'evidence': [{'id': 'ZZ/a.md', 'path': 'a.md', 'blob': h}],
            'contributions': []}
    ok &= validate_cert('ZZ', good) == []
    ok &= validate_cert('ZZ', dict(good, extra=1)) == ['schema:unknown-key:extra']
    ok &= 'schema:content-only-topology:base' in validate_cert(
        'ZZ', dict(good, shape='content-only'))
    ok &= 'schema:missing:translation' in validate_cert('ZZ', dict(good, origin='translated-v1'))
    ok &= 'schema:forbidden:translation' in validate_cert(
        'ZZ', dict(good, translation={'from': 'seal-record', 'migration_snapshot': h}))
    ok &= validate_cert('ZZ', dict(good, protocol=3)) == ['schema:protocol']
    row = {'round': 'ZZ', 'protocol': 2, 'origin': 'native-v2', 'kind': 'landed', 'certificate': h,
           'base': h, 'sealed_head': h, 'tree': h, 'landing': h,
           'ci': {k: {'run': 1, 'head_sha': h, 'conclusion': 'success'} for k in CI_KEYS}}
    ok &= validate_row('ZZ', row) == []
    ok &= 'row:schema:base-only-topology:sealed_head' in validate_row(
        'ZZ', dict(row, kind='base-only', sealed_head=None))
    ok &= 'row:schema:missing:ci' in validate_row('ZZ', {k: v for k, v in row.items() if k != 'ci'})
    ok &= 'row:schema:ci-forbidden' in validate_row('ZZ', dict(row, origin='translated-v1',
                                                                migration_snapshot=h))
    ok &= exact_set(['a', 'b'], ['a', 'b']) == []
    ok &= exact_set(['a'], ['a', 'b']) == ['vacuity:count']
    ok &= exact_set(['a', 'c'], ['a', 'b']) == ['vacuity:ids']
    ok &= validate_legacy({'protocol': 2, 'count': 1, 'rounds': []})[0] == ['legacy-owned:count']
    ok &= validate_policy({'protocol': 2, 'count': 0, 'policies': []})[0] == []
    # the recipe builder: a base, an execution head, a landing, one certificate and record
    work = tempfile.mkdtemp(prefix='cert-selftest-')
    try:
        recipe = {'commits': [
            {'name': 'c0', 'files': {'f': 'c0\n'}},
            {'name': 'B', 'parents': ['c0'], 'inherit': 'c0', 'files': {'v/x/preregistration.md': 'p\n'}},
            # the certificate is written by the round during its execution, so it is in E's tree
            {'name': 'E', 'parents': ['B'], 'inherit': 'B', 'files': {
                'v/x/result.md': 'r\n',
                'verification/certificates/ZZ.json': json.dumps({
                    'schema': SCHEMA, 'protocol': 2, 'round': 'ZZ', 'origin': 'native-v2',
                    'shape': 'non-sealing', 'directory': 'x', 'base': '{{sha:B}}',
                    'control_plane': [{'path': 'v/x/preregistration.md',
                                       'blob': '{{blob:B:v/x/preregistration.md}}',
                                       'merge': '{{sha:B}}', 'execution_affecting': True}],
                    'dependencies': [], 'evidence': [
                        {'id': 'ZZ/result.md', 'path': 'v/x/result.md',
                         'blob': '{{blob:self:v/x/result.md}}'}],
                    'contributions': []}, sort_keys=True) + '\n'}},
            {'name': 'L', 'parents': ['B', 'E'], 'inherit': 'E'},
            {'name': 'H', 'parents': ['L'], 'inherit': 'L', 'files': {
                'verification/certificates/attestations/ZZ.json': json.dumps({
                    'round': 'ZZ', 'protocol': 2, 'origin': 'native-v2', 'kind': 'landed',
                    'certificate': '{{blob:E:verification/certificates/ZZ.json}}',
                    'base': '{{sha:B}}', 'sealed_head': '{{sha:E}}', 'tree': '{{tree:E}}',
                    'landing': '{{sha:L}}',
                    'ci': {k: {'run': 1, 'head_sha': '{{sha:E}}', 'conclusion': 'success'}
                           for k in CI_KEYS}}, sort_keys=True) + '\n',
                'verification/certificates/live-policy.json':
                    '{"protocol": 2, "count": 0, "policies": []}\n',
                'verification/certificates/legacy-v1-owned.json':
                    '{"protocol": 2, "count": 0, "rounds": []}\n'}}],
            'head': 'H'}
        shas = build_repo(recipe, work)
        res = evaluate(work, {'GITHUB_EVENT_NAME': 'push'})
        ok &= res.ok() and res.certs.get('ZZ', ('',))[0] == 'PASS'
        # the certificate at E is the native record's subject: a certificate that differs at E
        # from the record's blob fails on that record and nowhere else
        ok &= 'topology:tree-mismatch' in [c.split(':', 1)[1] for c in
                                           evaluate(work, {'GITHUB_EVENT_NAME': 'push'},
                                                    subject='current-tree').codes]
    finally:
        shutil.rmtree(work, ignore_errors=True)
    print('certificate_verifier: self-test %s' % ('OK' if ok else 'FAILED'))
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--mode', choices=('shadow', 'authoritative'), default='shadow')
    ap.add_argument('--root', default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    ap.add_argument('--corpus', default=None)
    ap.add_argument('--no-corpus', action='store_true')
    ap.add_argument('--self-test', action='store_true')
    ap.add_argument('--subject', choices=('certified', 'current-tree'), default='certified')
    a = ap.parse_args()
    if a.self_test:
        return self_test()
    root = os.path.abspath(a.root)
    print('certificate_verifier: mode %s, root %s' % (a.mode, root))
    res = evaluate(root, os.environ, subject=a.subject)
    for line in res.lines:
        print(line)
    n_pass = sum(1 for v, _c in res.certs.values() if v == 'PASS')
    n_un = sum(1 for v, _c in res.certs.values() if v == 'UNATTESTED')
    n_fail = sum(1 for v, _c in res.certs.values() if v == 'FAIL')
    print('  CERTIFICATES  %d: %d PASS, %d UNATTESTED, %d FAIL; records %d; legacy-owned %d'
          % (len(res.certs), n_pass, n_un, n_fail, len(res.rows), len(res.legacy)))
    codes = list(res.codes)
    if not a.no_corpus:
        corpus = a.corpus or os.path.join(root, CERT_DIR, 'conformance', 'v2')
        codes += run_corpus(corpus, print)
    print('certificate_verifier: %s %s (%d failure(s))'
          % (a.mode, 'OK' if not codes else 'FAIL', len(codes)))
    for c in codes:
        print('    ' + c)
    if a.mode == 'authoritative':
        return 1 if codes else 0
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
