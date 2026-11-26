# design r6 as amended by amendment 1: R6.RECON.2 (a)-(g), R6.RECON.21, OBL-28 C-29
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

    def __init__(self, repo, H, M, X, F, harness, pinned_class_doc, plan_dir, ledgered, in_corpus, config_recon):
        self.repo = repo
        self.H, self.M, self.X, self.F = H, M, X, F
        self.harness = harness
        cls = [c for c in ((pinned_class_doc or {}).get('classes') or [])
               if isinstance(c, dict) and c.get('id') == record_authority.tool_landing_class_id]
        self.prefixes = sorted({p for c in cls for p in (c.get('prefixes') or []) if isinstance(p, str)})
        d = plan_dir.rstrip('/') if plan_dir else None
        self.plan_dir = d + '/' if d and d in record_authority.authorized_record_directories else None
        self.ledgered = set(ledgered)
        self.in_corpus = in_corpus
        self.config_recon = list(config_recon)

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
        """The record base: the run's M, in every admission mode. The record base of a predicted M (the main commit
        M0 it is built from) needs an input the adopted design does not give; it awaits a design amendment."""
        return [self.M]


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
        # the control harness (R6.RECON.21): every covered path is a drifted path of the run
        bad = [p for p in paths if p not in scope.ledgered or repo.blob_id(scope.H, p) == repo.blob_id(scope.M, p)]
        return ['%s is not a drifted path of the run' % bad[0]] if bad else []
    if scope.F is None:
        return ['no freeze F: the route needs F outside the control harness']
    changed = set()
    cur = scope.M
    while cur and not repo.is_ancestor(cur, scope.F):
        ps = repo.parents(cur)
        parent = ps[0] if ps else None
        for p in paths:
            if parent is None or repo.blob_id(cur, p) != repo.blob_id(parent, p):
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


# (d) review, lint and lineage at the record commit
def lint_problems(repo, rev, path, data, doc, scope, scan, config_shas):
    sha = util.sha256(data)
    ref = {'path': path, 'blob_sha256': sha}
    st = rec.Store(scan)
    if st.get(ref) is None:
        st.add(path, data)
    d = posixpath.dirname(path)
    reviews = [(s, p, rv) for s, (p, rv) in st.by_sha.items()
               if isinstance(rv, dict) and rv.get('schema') == review_schema and posixpath.dirname(p) == d
               and isinstance(rv.get('reviewed'), dict) and rv['reviewed'].get('blob_sha256') == sha]
    if len(reviews) != 1:
        return ['%d review records in the record directory name its blob, not one' % len(reviews)], None
    review = reviews[0]
    out = rec.lint_chain(ref, st, {sha, review[0]})
    heads = sorted(p for s, (p, x) in st.by_sha.items() if s != sha and isinstance(x, dict)
                   and isinstance(x.get('supersedes'), dict) and x['supersedes'].get('blob_sha256') == sha)
    if heads:
        out.append('%s in the scanned set supersedes it' % heads[0])
    sup = doc.get('supersedes')
    if isinstance(sup, dict) and sup.get('blob_sha256') in config_shas:
        out.append('it supersedes a record the configuration references')
    return out, {'path': review[1], 'sha256': review[0]}


def admit(repo, cands, scope, items):
    """cands: [(rev_text, rev, path, data, doc)] of the reconciliation records named by --classify. Returns the
    admitted records (each with `_ref`) and a listing for the result; appends a record-invalid item per refusal."""
    config_shas = {(r.get('_ref') or {}).get('blob_sha256') for r in scope.config_recon}
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
            lp, review = lint_problems(repo, rev, path, data, doc, scope, scans[rev], config_shas)
            probs += lp
            if review and scope.placement_problem(review['path']):
                probs.append('its review record is %s' % scope.placement_problem(review['path']))
        if probs:
            items.append(oc.make_item('RECORD', 'record-invalid', path, None, {'sha': sha, 'why': probs[0]},
                                      detail=probs))
            continue
        admitted.append(dict(doc, _ref={'path': path, 'blob_sha256': sha}))
        listing.append({'rev': rev, 'path': path, 'sha256': sha, 'review': review})
    # (e) one record per path, over the records the run reads and the unsuperseded records of the scanned sets
    # that name the run's M
    others = []
    for rev, scan in scans.items():
        st = rec.Store(scan)
        superseded_shas = {x['supersedes'].get('blob_sha256') for _s, (_p, x) in st.by_sha.items()
                           if isinstance(x, dict) and isinstance(x.get('supersedes'), dict)}
        others += [dict(x, _ref={'path': p, 'blob_sha256': s}) for s, (p, x) in st.by_sha.items()
                   if isinstance(x, dict) and x.get('schema') in recon_schemas and x.get('M') == scope.M
                   and s not in superseded_shas]
    pool = {}
    for r in list(scope.config_recon) + admitted + others:
        pool[(r.get('_ref') or {}).get('blob_sha256')] = r
    cover = {}
    for s, r in pool.items():
        for e in r.get('paths') or []:
            if isinstance(e, dict):
                cover.setdefault(e.get('path'), set()).add(s)
    clash = {s for ss in cover.values() if len(ss) > 1 for s in ss}
    keep = []
    for r in admitted:
        s = r['_ref']['blob_sha256']
        if s in clash:
            items.append(oc.make_item('RECORD', 'record-invalid', r['_ref']['path'], None,
                                      {'sha': s, 'why': 'another record covers one of its paths'},
                                      detail='two or more reconciliation records cover one path; none applies'))
        else:
            keep.append(r)
    listing = [x for x in listing if x['sha256'] not in clash]
    return keep, listing, clash


# OBL-28 C-29
def lint_classified(repo, rev, path, data, doc, scope):
    """A --classify record of another kind in the control harness is linted at its record commit: exactly one
    review record in its directory, and the chain lint over the records of that directory."""
    scan = scanned_all(repo, rev, posixpath.dirname(path))
    sha = util.sha256(data)
    st = rec.Store(scan)
    if st.get({'path': path, 'blob_sha256': sha}) is None:
        st.add(path, data)
    d = posixpath.dirname(path)
    reviews = [s for s, (p, rv) in st.by_sha.items()
               if isinstance(rv, dict) and rv.get('schema') == review_schema and posixpath.dirname(p) == d
               and isinstance(rv.get('reviewed'), dict) and rv['reviewed'].get('blob_sha256') == sha]
    if len(reviews) != 1:
        return ['%d review records in the record directory name its blob, not one' % len(reviews)]
    return rec.lint_chain({'path': path, 'blob_sha256': sha}, st, {sha, reviews[0]})


def scanned_all(repo, rev, directory):
    """The json records of one directory of a tree, with every predecessor a `supersedes` there names."""
    out = []
    pre = directory.rstrip('/') + '/'
    for path, (mode, _oid) in sorted(repo.entries(rev).items()):
        if mode in regular_modes and path.startswith(pre) and path.endswith('.json'):
            out.append((path, repo.read(rev, path)))
    return out
