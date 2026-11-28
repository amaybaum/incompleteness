# design r6 as amended by amendments 1 and 4: R6.RECON.2 (a)-(g), R6.RECON.21, OBL-28 C-29
"""The post-freeze route for reconciliation records named by --classify, and the record lint of --classify
records in the control harness.

Every condition is decided from git objects read through the verified reader. A record the route does not admit is
reported record-invalid and is not used. The route admits reconciliation records only; a review record named as the
primary record, and any other record kind written after the freeze, are not admitted.

The per-record conditions are separate functions, so that a later rule over several records (the one-record-per-path
condition (e) here) can be generalized without touching them.
"""
import json
import posixpath
import re

from . import outcome as oc
from . import records as rec
from . import util
from .gitobj import tree_entry
from .. import record_authority

recon_schema = 'oi-reconciliation/2'
recon_schemas = ('oi-reconciliation/1', 'oi-reconciliation/2')
review_schema = rec.review_schema
# the root under which reconciliation directories lie; a repository fact, kept outside the engine
audits_root = record_authority.reconciliation_root
_full_id = re.compile(r'[0-9a-f]{40}\Z')
regular_modes = ('100644', '100755')


class Scope:
    """What the route needs to know about the run: the roles, the paths it must keep records away from, and the
    records the configuration references.

    The tool-landing domain is the class with the tool-landing id in the side-change class record the configuration
    pins (`pinned_class_doc`); a class record named by --classify never contributes to it. The plan's record directory
    counts only when it is an authorized record directory."""

    def __init__(self, repo, H, M, X, F, harness, pinned_class_doc, plan_dir, ledgered, in_corpus, config_recon,
                 record_base=None):
        self.repo = repo
        self.H, self.M, self.X, self.F = H, M, X, F
        self.harness = harness
        cls = [c for c in ((pinned_class_doc or {}).get('classes') or [])
               if isinstance(c, dict) and c.get('id') == record_authority.tool_landing_class_id]
        self.prefixes = sorted({p.rstrip('/') + '/' for c in cls for p in (c.get('prefixes') or [])
                                if isinstance(p, str) and p})
        self.pins = {x['path']: x for c in cls for x in (c.get('pins') or [])
                     if isinstance(x, dict) and isinstance(x.get('path'), str)}
        d = plan_dir.rstrip('/') if plan_dir else None
        self.plan_dir = d + '/' if d and d in record_authority.authorized_record_directories else None
        self.ledgered = set(ledgered)
        self.in_corpus = in_corpus
        self.config_recon = list(config_recon)
        self.record_base = record_base
        self._base = None

    # (f) and R6.RECON.1: a reconciliation directory
    def placement_problem(self, path):
        if not path.startswith(audits_root):
            return 'not under %s' % audits_root
        if any(path.startswith(p) for p in self.prefixes):
            return 'under a prefix of the tool-landing class'
        if self.plan_dir and path.startswith(self.plan_dir):
            return "inside the plan's record directory"
        if path in self.ledgered or self.in_corpus(path):
            return 'a ledgered or corpus path'
        return None

    def record_bases(self):
        """The record base: the run's M; for a run on a predicted M, the commit M0 named with --record-base, admitted
        only when base_problems finds nothing (amendment 4). Naming M0 establishes nothing."""
        if self.record_base is None:
            return [self.M]
        return [self.record_base] if not self.base_problems() else []

    def base_problems(self):
        if self._base is None:
            self._base = record_base_problems(self.repo, self.record_base, self) if self.record_base else []
        return self._base

    # (c) (3): a path a step between M0 and M may change
    def step_path_problem(self, path, at_m):
        pin = self.pins.get(path)
        if pin is not None:
            if at_m is None:
                return '%s, a pin of the tool-landing class, is deleted' % path
            if at_m[0] not in regular_modes or not pin_matches(self.repo, self.M, path, pin):
                return '%s differs from its pin in the tool-landing class' % path
            return None
        if any(path.startswith(p) for p in self.prefixes):
            return None
        if self.plan_dir and path.startswith(self.plan_dir):
            return None
        return '%s is neither a tool-landing path nor in an authorized plan record directory' % path


def pin_matches(repo, rev, path, pin):
    data = repo.read(rev, path)
    if data is None:
        return False
    if pin.get('blob_sha256') is not None and util.sha256(data) != pin['blob_sha256']:
        return False
    if pin.get('git_blob') is not None and repo.blob_id(rev, path) != pin['git_blob']:
        return False
    return pin.get('blob_sha256') is not None or pin.get('git_blob') is not None


def in_memory(repo, rev):
    return rev in (getattr(repo, 'mem', None) or {})


# R6.RECON.2 (c) as amended by amendment 4: the record base M0 of a run on a predicted M, from git objects
def record_base_problems(repo, m0, scope):
    M = scope.M
    # (1) a full commit id of the repository object store, not an in-memory commit
    if not isinstance(m0, str) or not _full_id.match(m0):
        return ['the record base %r is not a full commit id' % (m0,)]
    if in_memory(repo, m0):
        return ['the record base is an in-memory commit']
    try:
        repo.parents(m0)
    except Exception:  # an id the object store does not hold
        return ['the record base is not a commit of the repository']
    # (2) M descends from M0 by single-parent in-memory commits
    chain = []
    cur = M
    while cur != m0:
        if not in_memory(repo, cur):
            return ['M does not descend from the record base by in-memory commits']
        ps = repo.parents(cur)
        if len(ps) != 1:
            return ['a commit between the record base and M has %d parents, not one' % len(ps)]
        chain.append((ps[0], cur))
        cur = ps[0]
    if not chain:
        return ['the record base is M itself: a run on M needs no record base']
    # (3) every changed path, per step and in the aggregate diff
    em = repo.entries(M)
    aggregate = set(changed_paths(repo, m0, M))
    for path in sorted(aggregate):
        prob = scope.step_path_problem(path, em.get(path))
        if prob:
            return [prob]
    for a, b in reversed(chain):
        for path in changed_paths(repo, a, b):
            if path not in aggregate:
                return ['%s changes between the record base and M but not in the aggregate diff' % path]
    # (4) no ledgered, corpus or scanned-set path
    scan = {p for p, _ in scanned(repo, m0, scope)} | {p for p, _ in scanned(repo, M, scope)}
    for path in sorted(aggregate):
        if path in scope.ledgered or scope.in_corpus(path):
            return ['%s, a ledgered or corpus path, changes between the record base and M' % path]
        if path in scan:
            return ['%s, a path of the scanned set, changes between the record base and M' % path]
    return []


def changed_paths(repo, a, b):
    ea, eb = repo.entries(a), repo.entries(b)
    return sorted(p for p in set(ea) | set(eb) if ea.get(p) != eb.get(p))


def scanned(repo, rev, scope):
    """The scanned set of a tree: every regular json file under verification/audits/, outside the tool-landing
    domain and the plan's record directory, whose content is a reconciliation or review record. [(path, bytes)]"""
    out = []
    for path, (mode, _oid) in sorted(repo.entries(rev).items()):
        if mode not in regular_modes or not path.endswith('.json') or not path.startswith(audits_root):
            continue
        if any(path.startswith(p) for p in scope.prefixes) or (scope.plan_dir and path.startswith(scope.plan_dir)):
            continue
        data = repo.read(rev, path)
        try:
            doc = json.loads(data.decode('utf-8'))
        except (ValueError, UnicodeDecodeError, AttributeError):
            continue
        if isinstance(doc, dict) and doc.get('schema') in recon_schemas + (review_schema,):
            out.append((path, data))
    return out


# (c) the record commit
def rev_problems(repo, rev_text, rev, scope):
    if not _full_id.match(rev_text or ''):
        return ['the record commit %r is not a full commit id' % rev_text]
    ps = repo.parents(rev)
    if len(ps) != 1:
        return ['the record commit has %d parents, not one' % len(ps)]
    if scope.record_base is not None and scope.base_problems():
        return ['the record base is not admitted: %s' % scope.base_problems()[0]]
    if ps[0] not in scope.record_bases():
        return ["the record commit's parent is not the run's record base"]
    er, ep = repo.entries(rev), repo.entries(ps[0])
    for path in sorted(set(er) | set(ep)):
        if er.get(path) == ep.get(path):
            continue
        if path in ep:
            return ['the record commit changes %s, which its parent holds' % path]
        if er[path][0] not in regular_modes or scope.placement_problem(path):
            return ['the record commit adds %s outside a reconciliation directory' % path]
    return []


# (b) the covered paths
def path_problems(repo, doc, scope):
    paths = [e.get('path') for e in (doc.get('paths') or []) if isinstance(e, dict)]
    if not paths:
        return ['the record covers no path']
    if scope.harness:
        # the control harness (R6.RECON.21): every covered path is a drifted path of the run, ledgered or, under
        # amendment 3, a corpus path
        bad = [p for p in paths if (p not in scope.ledgered and not scope.in_corpus(p)) or
               tree_entry(repo, scope.H, p) == tree_entry(repo, scope.M, p)]
        return ['%s is not a drifted path of the run' % bad[0]] if bad else []
    if scope.F is None:
        return ['no freeze F: the route needs F outside the control harness']
    changed = set()
    cur = scope.M
    while cur and not repo.is_ancestor(cur, scope.F):
        ps = repo.parents(cur)
        parent = ps[0] if ps else None
        for p in paths:
            if parent is None or tree_entry(repo, cur, p) != tree_entry(repo, parent, p):
                changed.add(p)
        cur = parent
    bad = [p for p in paths if p not in changed]
    return ['%s is changed on M by no commit after the freeze' % bad[0]] if bad else []


# (a) binding
def binding_problems(doc, scope):
    out = []
    if doc.get('M') != scope.M:
        out.append("the record does not name the run's M")
    if doc.get('X') != scope.X:
        out.append("the record does not name the run's X")
    return out


def reference_key(ref):
    """Identify a referenced record by path and byte digest."""
    # R6.RECON.29 treats identical bytes at two paths as distinct records.
    if isinstance(ref, dict):
        path, sha = ref.get('path'), ref.get('blob_sha256')
        if isinstance(path, str) and isinstance(sha, str):
            return path, sha
    return None


# (d) review, lint and lineage at the record commit
def lint_problems(repo, rev, path, data, doc, scope, scan, config_refs):
    sha = util.sha256(data)
    ref = {'path': path, 'blob_sha256': sha}
    # r6 Amendment 10: the admitted review's revision is the record base, REV's single parent
    st = rec.Store(scan, repo, [rev], record_commit=rev)
    if st.get(ref) is None:
        st.add(path, data)
    d = posixpath.dirname(path)
    keyed = [(p, s, record) for p, entries in st.by_path.items() for s, record in entries]
    reviews = [(s, p, rv) for p, s, rv in keyed
               if isinstance(rv, dict) and rv.get('schema') == review_schema and posixpath.dirname(p) == d
               and reference_key(rv.get('reviewed')) == (path, sha)]
    if len(reviews) != 1:
        return ['%d review records in the record directory name its blob, not one' % len(reviews)], None
    review = reviews[0]
    out = rec.lint_chain(ref, st, {sha, review[0]})
    heads = sorted(p for p, s, x in keyed if (p, s) != (path, sha) and isinstance(x, dict)
                   and reference_key(x.get('supersedes')) == (path, sha))
    if heads:
        out.append('%s in the scanned set supersedes it' % heads[0])
    if reference_key(doc.get('supersedes')) in config_refs:
        out.append('it supersedes a record the configuration references')
    return out, {'path': review[1], 'sha256': review[0]}


def admit(repo, cands, scope, items):
    """cands: [(rev_text, rev, path, data, doc)] of the reconciliation records named by --classify. Returns the
    admitted records (each with `_ref`) and a listing for the result; appends a record-invalid item per refusal."""
    config_refs = {reference_key(r['_ref']) for r in scope.config_recon}
    revs = {c[0] for c in cands}
    admitted, listing = [], []
    scans = {}
    for rev_text, rev, path, data, doc in cands:
        sha = util.sha256(data)
        probs = []
        if len(revs) > 1:
            probs.append('the run names more than one record commit')
        place = scope.placement_problem(path)
        if place:
            probs.append('the record is %s' % place)
        probs += rev_problems(repo, rev_text, rev, scope) if not probs else []
        probs += binding_problems(doc, scope) if not probs else []
        probs += path_problems(repo, doc, scope) if not probs else []
        review = None
        if not probs:
            if rev not in scans:
                scans[rev] = scanned(repo, rev, scope)
            lp, review = lint_problems(repo, rev, path, data, doc, scope, scans[rev], config_refs)
            probs += lp
            if review and scope.placement_problem(review['path']):
                probs.append('its review record is %s' % scope.placement_problem(review['path']))
        if probs:
            items.append(oc.make_item('RECORD', 'record-invalid', path, None, {'sha': sha, 'why': probs[0]},
                                      detail=probs))
            continue
        admitted.append(dict(doc, _ref={'path': path, 'blob_sha256': sha}, _source=rev))
        listing.append({'rev': rev, 'path': path, 'sha256': sha, 'review': review})
    # (e) one record per path, over the records the run reads and the unsuperseded records of the scanned sets
    # that name the run's M
    pool = {reference_key(r['_ref']): r for r in scope.config_recon + admitted}
    for scan in scans.values():
        st = rec.Store(scan)
        entries = {(p, s): doc for p, records in st.by_path.items() for s, doc in records if isinstance(doc, dict)}
        predecessor_refs = {reference_key(doc.get('supersedes')) for doc in entries.values()}
        for key, doc in entries.items():
            if doc.get('schema') in recon_schemas and doc.get('M') == scope.M and key not in predecessor_refs:
                pool.setdefault(key, doc)
    cover = {}
    for key, doc in pool.items():
        for e in doc.get('paths') or []:
            if isinstance(e, dict):
                cover.setdefault(e.get('path'), set()).add(key)
    clash = {key for refs in cover.values() if len(refs) > 1 for key in refs}
    for path, sha in sorted(clash):
        items.append(oc.make_item('RECORD', 'record-invalid', path, None,
                                  {'sha': sha, 'why': 'another record covers one of its paths'},
                                  detail='two or more reconciliation records cover one path; none applies'))
    keep = [r for r in admitted if reference_key(r['_ref']) not in clash]
    listing = [x for x in listing if (x['path'], x['sha256']) not in clash]
    return keep, listing, clash


# OBL-28 C-29
def lint_classified(repo, rev, path, data, doc, scope):
    """A --classify record of another kind in the control harness is linted at its record commit: exactly one
    ordinary review in its directory, with class widening reviews checked by the chain lint."""
    scan = scanned_all(repo, rev, posixpath.dirname(path))
    sha = util.sha256(data)
    st = rec.Store(scan, repo, [rev])
    if st.get({'path': path, 'blob_sha256': sha}) is None:
        st.add(path, data)
    d = posixpath.dirname(path)
    matches = {s: rv for s, (p, rv) in st.by_sha.items()
               if isinstance(rv, dict) and rv.get('schema') == review_schema and posixpath.dirname(p) == d
               and isinstance(rv.get('reviewed'), dict) and rv['reviewed'].get('blob_sha256') == sha}
    class_record = doc.get('schema') == rec.class_schema
    reviews = [s for s, rv in matches.items() if not class_record or rv.get('kind', 'review') == 'review']
    if len(reviews) != 1:
        return ['%d review records in the record directory name its blob, not one' % len(reviews)]
    return rec.lint_chain({'path': path, 'blob_sha256': sha}, st, {sha, *matches})


def scanned_all(repo, rev, directory):
    """The json records of one directory of a tree, with every predecessor a `supersedes` there names."""
    out = []
    pre = directory.rstrip('/') + '/'
    for path, (mode, _oid) in sorted(repo.entries(rev).items()):
        if mode in regular_modes and path.startswith(pre) and path.endswith('.json'):
            out.append((path, repo.read(rev, path)))
    return out
