"""Staging r2 supplement S-1 (recorded session identities, adopted at its reviewed head with the five OQ defaults):
the session registry (schema oi-a1-staging-sessions/1; its file name, repository and admitted threads are passed by
the caller from record_authority.py), its admission from F's pin table,
the party relation, the registry's review, append-only continuity across freezes, scope, independence, what a review
binds, and the outcomes of S1.8 (record lint) and S1.9 (detection), as mechanical predicates over explicit records.

The tool reads `oi-designate` and `oi-withdraw` form comments only as recorded inputs: an entry's `designation`, and a
withdrawal's, is checked as a comment URL in this repository in an admitted thread; the comment's content and its
author are not read (S1.2: whether a comment is in the owner's form is procedural, R6.REC.3). The tool never writes
`oi-` text.
"""
import posixpath
import re

from . import findings as fd
from . import gitobj
from . import util

schema = 'oi-a1-staging-sessions/1'
ENTRY_KEYS = {'id', 'kind', 'platform_ref', 'spawned_by', 'same_party', 'scope', 'designation'}
TOP_KEYS = {'schema', 'author', 'parties', 'withdrawn'}
_id = re.compile(r'^(session|person)\.[a-z0-9][a-z0-9-]{1,62}$')
_hex40 = re.compile(r'^[0-9a-f]{40}$')


def comment_url_ok(url, repository, threads):
    """A comment URL in this repository, in an admitted thread, posted after that thread's admission (S1.2):
    https://github.com/<repository>/(issues|pull)/<n>#issuecomment-<id>, with n a key of `threads` and id greater than
    threads[n], the comment id of the record that admitted the thread (comment ids increase with posting time)."""
    if not isinstance(url, str):
        return False
    m = re.match(r'^https://github\.com/([^/]+/[^/]+)/(issues|pull)/(\d+)#issuecomment-(\d+)$', url)
    if not m or m.group(1) != repository or int(m.group(3)) not in threads:
        return False
    after = threads[int(m.group(3))]
    return type(after) is int and int(m.group(4)) > after


def registry_problems(data, doc, repository, threads):
    """S1.1, S1.2 (designation form) and S1.4: [] when the registry is well formed and unambiguous; otherwise the
    reasons it fails (the whole registry fails)."""
    out = []
    if not isinstance(doc, dict):
        return ['the registry is not a strict-parsed JSON object']
    if data != util.canonical(doc):
        out.append('the registry is not canonical JSON (R6.RECON.29)')
    if set(doc) != TOP_KEYS:
        out.append('the registry\'s keys are not exactly %s' % sorted(TOP_KEYS))
    if doc.get('schema') != schema:
        out.append('the registry\'s schema is not %s' % schema)
    parties = doc.get('parties')
    withdrawn = doc.get('withdrawn')
    if not isinstance(parties, list) or not parties:
        return out + ['parties is not a non-empty array']
    if not isinstance(withdrawn, list):
        return out + ['withdrawn is not an array']
    ids = []
    refs = []
    for i, e in enumerate(parties):
        if not isinstance(e, dict) or set(e) != ENTRY_KEYS:
            out.append('parties[%d]: the keys are not exactly %s' % (i, sorted(ENTRY_KEYS)))
            continue
        pid = e.get('id')
        if not isinstance(pid, str) or not _id.match(pid) or pid.split('.', 1)[0] != e.get('kind'):
            out.append('parties[%d]: id %r breaks its grammar or its prefix differs from kind' % (i, pid))
        if e.get('kind') not in ('session', 'person'):
            out.append('parties[%d]: kind is not session or person' % i)
        if not (isinstance(e.get('platform_ref'), str) and e['platform_ref']):
            out.append('parties[%d]: platform_ref is not a non-empty string' % i)
        if not (e.get('spawned_by') is None or isinstance(e.get('spawned_by'), str)):
            out.append('parties[%d]: spawned_by is not an id or null' % i)
        if not (isinstance(e.get('same_party'), list) and all(isinstance(x, str) for x in e['same_party'])):
            out.append('parties[%d]: same_party is not an array of ids' % i)
        sc = e.get('scope')
        if not (isinstance(sc, list) and sc and all(_scope_ok(x) for x in sc)):
            out.append('parties[%d]: scope is not a non-empty array of paths (the root is not a scope)' % i)
        if not comment_url_ok(e.get('designation'), repository, threads):
            out.append('parties[%d]: designation is not an owner form comment URL in an admitted thread' % i)
        ids.append(pid)
        refs.append(e.get('platform_ref'))
    if len(ids) != len(set(map(str, ids))):
        out.append('two entries have equal id')
    if len([r for r in refs if isinstance(r, str)]) != len({r for r in refs if isinstance(r, str)}):
        out.append('two entries share a platform_ref')
    known = set(x for x in ids if isinstance(x, str))
    for e in parties:
        if not isinstance(e, dict):
            continue
        links = ([e['spawned_by']] if isinstance(e.get('spawned_by'), str) else []) + \
            [x for x in e.get('same_party') or [] if isinstance(x, str)]
        for x in links:
            if x not in known:
                out.append('entry %s links %s, which names no entry' % (e.get('id'), x))
    for i, w in enumerate(withdrawn):
        if not isinstance(w, dict) or set(w) != {'id', 'designation'}:
            out.append('withdrawn[%d]: the keys are not exactly [designation, id]' % i)
            continue
        if w.get('id') not in known:
            out.append('withdrawn[%d]: id %r names no entry' % (i, w.get('id')))
        if not comment_url_ok(w.get('designation'), repository, threads):
            out.append('withdrawn[%d]: designation is not an owner form comment URL in an admitted thread' % i)
    if doc.get('author') not in known:
        out.append('the registry\'s author is not an entry')
    return out


def _scope_ok(x):
    return fd._enc('path', x) and x not in ('.',)


def entries(doc):
    return {e['id']: e for e in doc.get('parties') or [] if isinstance(e, dict) and isinstance(e.get('id'), str)}


def withdrawn_ids(doc):
    return {w.get('id') for w in doc.get('withdrawn') or [] if isinstance(w, dict)}


def party(doc, x):
    """S1.3: the closure of {x} under same_party and spawned_by, each read in both directions. Withdrawn entries keep
    their links."""
    es = entries(doc)
    adj = {}
    for pid, e in es.items():
        links = ([e['spawned_by']] if isinstance(e.get('spawned_by'), str) else []) + \
            [y for y in e.get('same_party') or [] if isinstance(y, str)]
        for y in links:
            adj.setdefault(pid, set()).add(y)
            adj.setdefault(y, set()).add(pid)
    seen, todo = {x}, [x]
    while todo:
        c = todo.pop()
        for y in adj.get(c, ()):
            if y not in seen:
                seen.add(y)
                todo.append(y)
    return seen


def same_party(doc, a, b):
    return a == b or b in party(doc, a) or a in party(doc, b)


def is_identity(doc, x):
    """R6.RECON.29 as amended: the id of exactly one entry of the admitted registry, not withdrawn."""
    return isinstance(x, str) and x in entries(doc) and x not in withdrawn_ids(doc)


def under_scope(scope, path):
    """S1.6: a path is under a scope entry when the entry's components are a prefix of the path's, compared whole."""
    if not isinstance(path, str):
        return False
    pc = path.split('/')
    for s in scope or []:
        sc = s.split('/')
        if len(sc) <= len(pc) and pc[:len(sc)] == sc:
            return True
    return False


def item_ids(doc):
    """R6.RECON.31 row for oi-a1-staging-sessions/1 (records.item_ids carries the same row)."""
    from . import records
    return records.item_ids(doc)


def record_author_problems(doc, record, record_path):
    """S1.8 and S1.6 for a record: its author is an identity string and its path is under the author's scope."""
    a = (record or {}).get('author') if isinstance(record, dict) else None
    if not is_identity(doc, a):
        return ['the record\'s author is not an identity string']
    if not under_scope(entries(doc)[a].get('scope'), record_path):
        return ['the record\'s path is outside its author\'s scope']
    return []


def review_binding_problems(repo, review, review_path, doc, root):
    """S-1 sec. 3 and S1.8: the review's reviewer is an identity string; revision is a commit reachable through any
    parent from `root` whose tree holds reviewed.path at a regular mode with bytes hashing to reviewed.blob_sha256;
    platform_ref equals the reviewer's entry; reviewed.path and the review file's path are under the reviewer's scope.
    [] when the review binds."""
    out = []
    if not isinstance(review, dict):
        return ['not a review']
    who = review.get('reviewer')
    if not is_identity(doc, who):
        return ['the reviewer is not an identity string (unregistered, withdrawn or malformed)']
    e = entries(doc)[who]
    rv = review.get('reviewed') if isinstance(review.get('reviewed'), dict) else {}
    rev = review.get('revision')
    ok = isinstance(rev, str) and _hex40.match(rev) is not None
    if ok:
        try:
            ok = rev == root or repo.is_ancestor(rev, root)
            ent = repo.entries(rev).get(rv.get('path')) if ok else None
            ok = ok and ent is not None and ent[0] in ('100644', '100755') and \
                util.sha256(repo.read(rev, rv['path'])) == rv.get('blob_sha256')
        except gitobj.Unresolvable:  # an unheld revision binds nothing
            ok = False
    if not ok:
        out.append('revision is missing, unreachable from the root, or does not hold the reviewed bytes')
    if review.get('platform_ref') != e.get('platform_ref'):
        out.append('platform_ref is missing or differs from the reviewer\'s entry')
    if not under_scope(e.get('scope'), rv.get('path')) or not under_scope(e.get('scope'), review_path):
        out.append('a path is outside the reviewer\'s scope')
    return out


def independence_problems(doc, author, reviewers, widening=None):
    """S1.7: no ordinary reviewer in the author's party; the widening reviewer in neither the author's party nor any
    ordinary reviewer's. For the configuration and the staging roots the writer, the ordinary reviewer and the
    widening reviewer are then in pairwise distinct parties, since those are exactly the three comparisons."""
    out = []
    for r in reviewers:
        if same_party(doc, r, author):
            out.append('the reviewer %s is in the party of the author %s' % (r, author))
    if widening is not None:
        if same_party(doc, widening, author):
            out.append('the widening reviewer %s is in the party of the author' % widening)
        for r in reviewers:
            if same_party(doc, widening, r):
                out.append('the widening reviewer %s is in the party of the ordinary reviewer %s' % (widening, r))
    return out


def lint_review_problems(repo, review, review_path, record_doc, doc, root, registry_failed):
    """S1.8: why a review counts as no review in record lint ([] when it counts): a failed registry, a reviewer that
    is not an identity string, a failed revision, platform_ref or scope, or a reviewer in the author's party."""
    if registry_failed:
        return ['the session registry fails (S1.4)']
    out = review_binding_problems(repo, review, review_path, doc, root)
    if out:
        return out
    author = (record_doc or {}).get('author')
    if not is_identity(doc, author):
        return ['the record\'s author is not an identity string']
    if same_party(doc, review.get('reviewer'), author):
        return ['the reviewer is in the party of the record\'s author']
    return []


def detection_outcome(repo, review, review_path, reviewed_doc, in_rstar, doc, root, registry_failed):
    """S1.9 for a review carrying invalidates or invalidated: 'disqualified' only when its reviewer is the same id as
    the named record's author with that record in R*; 'provisional' when the record is absent from R* (r9 Amendment
    1); otherwise 'genuine', with the form failures (a reviewer in the author's party but not the same id, not an
    identity string, a failed registry, revision or platform_ref) as the second value."""
    if not in_rstar:
        return 'provisional', []
    author = (reviewed_doc or {}).get('author')
    who = review.get('reviewer') if isinstance(review, dict) else None
    # only a registered, unwithdrawn id equal to the author's, under a registry that holds, disqualifies: a login, a
    # withdrawn id or any equal string under a failed registry is a genuine finding with a form failure
    if not registry_failed and is_identity(doc, who) and who == author:
        return 'disqualified', []
    form = []
    if registry_failed:
        form.append('the session registry fails (S1.4)')
    else:
        form += review_binding_problems(repo, review, review_path, doc, root)
        if not form and same_party(doc, who, author):
            form.append('the reviewer is in the party of the record\'s author but not the same id')
    return 'genuine', form


def registry_review_problems(repo, review, review_path, reg_ref, doc, root, d_rec):
    """S1.2: the registry's review binds its exact path and blob, meets sec. 3 with root F and scope over D_rec, has
    a reviewer outside the writer's party, and accepts every item (party:<id>, withdrawn:<id>) exactly once; any
    rejected or omitted item fails the registry."""
    if not isinstance(review, dict) or review.get('reviewed') != reg_ref:
        return ['the registry has no review of its exact path and blob']
    out = review_binding_problems(repo, review, review_path, doc, root)
    who = review.get('reviewer')
    if is_identity(doc, who):
        if not under_scope(entries(doc)[who].get('scope'), d_rec.rstrip('/') + '/x'):
            out.append('the registry reviewer\'s scope does not cover D_rec')
        if same_party(doc, who, doc.get('author')):
            out.append('the registry reviewer is in the writer\'s party')
    ids = item_ids(doc)
    vs = {}
    for v in review.get('verdicts') or []:
        if isinstance(v, dict):
            vs.setdefault(v.get('item'), []).append(v.get('verdict'))
    if any(i not in vs or vs[i] != ['accept'] for i in ids) or set(vs) - set(ids):
        out.append('the registry review does not accept every item exactly once')
    if isinstance(review.get('dissent'), str) and review['dissent'].strip():
        out.append('the registry review dissents')
    return out


def append_only_problems(prev, cur):
    """S1.5: every prior entry and withdrawal appears byte-identical (canonical JSON element) at F, and the party
    relation restricted to ids registered at F_prev is unchanged."""
    out = []
    cur_elems = {util.canonical(e) for e in cur.get('parties') or []}
    cur_w = {util.canonical(w) for w in cur.get('withdrawn') or []}
    for e in prev.get('parties') or []:
        if util.canonical(e) not in cur_elems:
            out.append('the prior entry %s is not byte-identical at F' % (e or {}).get('id'))
    for w in prev.get('withdrawn') or []:
        if util.canonical(w) not in cur_w:
            out.append('the prior withdrawal of %s is absent at F' % (w or {}).get('id'))
    old = set(entries(prev))
    for a in old:
        if party(prev, a) & old != party(cur, a) & old:
            out.append('the party of %s among the prior ids changes at F' % a)
            break
    return out


def admit(repo, F, d_rec, read_pin_table, cfg_records, file_name, repository, threads):
    """S1.1, S1.2, S1.4 and the R6.RECON.33 row: the registry admitted from F's pin table (the PREREG.md of D_rec at
    F) at D_rec/file_name with the pinned SHA-256, and its review: the one pinned file of D_rec that is an
    oi-review-record/1 of the registry's exact path and blob. Returns (doc, problems); the registry fails exactly when
    problems is non-empty, and no registry is taken from anywhere else (an argument, a commit author, a host record).
    Where the configuration's records list a record of kind `sessions`, its reference must equal the pinned path and
    blob: otherwise ValueError('CONFIG_INVALID: ...')."""
    d = d_rec.rstrip('/')
    path = d + '/' + file_name
    pp = d + '/PREREG.md'

    def regular(p):
        e = repo.entries(F).get(p)
        return e is not None and e[0] in ('100644', '100755')
    table = None
    if regular(pp):
        try:
            table = read_pin_table(repo.read(F, pp))
        except Exception as exc:  # config.PinTableError: a malformed pin table pins nothing
            if isinstance(exc, gitobj.Unresolvable):
                raise
            table = None
    sha = (table or {}).get(file_name)
    for r in cfg_records or []:
        if isinstance(r, dict) and r.get('kind') == 'sessions' and \
                (sha is None or (r.get('path'), r.get('blob_sha256')) != (path, sha)):
            raise ValueError('CONFIG_INVALID: the configuration lists a sessions record other than the one F\'s '
                             'pin table pins')
    if table is None:
        return None, ['F has no readable pin table beside D_rec']
    if not sha:
        return None, ['the registry is not pinned at F']
    if not regular(path):
        return None, ['the registry is absent at F or not a regular file']
    data = repo.read(F, path)
    if util.sha256(data) != sha:
        return None, ['the registry differs from its pinned SHA-256']
    doc = fd.strict_parse(data)
    probs = registry_problems(data, doc, repository, threads)
    if probs:
        return None, probs
    ref = {'path': path, 'blob_sha256': sha}
    reviews = []
    for name, h in sorted(table.items()):
        p = d + '/' + name
        if name == file_name or not regular(p):
            continue
        b = repo.read(F, p)
        if util.sha256(b) != h:
            continue
        rv = fd.strict_parse(b)
        if isinstance(rv, dict) and rv.get('schema') == 'oi-review-record/1' and rv.get('reviewed') == ref:
            reviews.append((p, rv))
    if len(reviews) != 1:
        return None, ['the registry has %s pinned review of its exact path and blob' %
                      ('no' if not reviews else 'more than one')]
    rp, rv = reviews[0]
    probs = registry_review_problems(repo, rv, rp, ref, doc, F, d)
    return (None, probs) if probs else (doc, [])
