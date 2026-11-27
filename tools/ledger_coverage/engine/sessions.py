"""Staging r2 supplement S-2 (procedural reviewer independence) as mechanical predicates over explicit records: what
a review binds (`revision`, S-1 sec. 3, which S-2 S2.3 keeps), and the outcomes of S2.5 in record lint and in
detection. Identities are identity strings compared by key (S2.1, S2.2, findings.identity_ok and same_identity), and
are read only from record fields, never from an argument, a commit author or a host record (S2.6). The run applies
S2.4 through findings.independence_problems in record lint and detection; it does not call these predicates, and
its record lint does not yet check `revision`.
"""
import re

from . import findings as fd
from . import gitobj
from . import util

_hex40 = re.compile(r'^[0-9a-f]{40}$')


def review_binding_problems(repo, review, root):
    """S-1 sec. 3: `revision` is a commit reachable through any parent from `root` whose tree holds reviewed.path at
    a regular mode with bytes hashing to reviewed.blob_sha256. [] when the review binds."""
    if not isinstance(review, dict):
        return ['not a review']
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
    return [] if ok else ['revision is missing, unreachable from the root, or does not hold the reviewed bytes']


def lint_review_problems(repo, review, record_doc, root):
    """S2.5, record lint: why a review counts as no review ([] when it counts): the record's author not an identity
    string, a review not independent (S2.4) of that author, or a failed revision."""
    author = record_doc.get('author') if isinstance(record_doc, dict) else None
    if not fd.identity_ok(author):
        return ['the record\'s author is not an identity string']
    return fd.independence_problems(review, [author]) + review_binding_problems(repo, review, root)


def detection_outcome(repo, review, reviewed_doc, in_rstar, root):
    """S2.5, detection, for a review carrying invalidates or invalidated: 'provisional' when the record it names is
    absent from R* (r9 Amendment 1); 'disqualified' only when its reviewer is an identity string byte-equal to that
    record's author; otherwise 'genuine', with its form failures (a malformed reviewer or declaration, a declaration
    naming the author, a reviewer the same identity as the author without byte equality, a failed revision) as the
    second value."""
    if not in_rstar:
        return 'provisional', []
    author = reviewed_doc.get('author') if isinstance(reviewed_doc, dict) else None
    who = review.get('reviewer') if isinstance(review, dict) else None
    if fd.identity_ok(who) and who == author:
        return 'disqualified', []
    return 'genuine', fd.independence_problems(review, [author]) + review_binding_problems(repo, review, root)
