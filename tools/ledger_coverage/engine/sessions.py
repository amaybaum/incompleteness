# Staging S-2's ordinary review predicates. They share the engine's identity and revision checks.
from . import findings as fd
from . import records


def review_binding_problems(repo, review, root):
    # S-1 section 3, retained in S2.3 for ordinary roots.
    return records.revision_problems(repo, [root], review)


def lint_review_problems(repo, review, record_doc, root):
    # S2.5 record lint requires an author identity, independent review and exact revision binding.
    author = record_doc.get('author') if isinstance(record_doc, dict) else None
    if not fd.identity_ok(author):
        return ['the record\'s author is not an identity string']
    return fd.independence_problems(review, [author]) + review_binding_problems(repo, review, root)


def detection_outcome(repo, review, reviewed_doc, in_rstar, root):
    # S2.5: missing reviewed record is a provisional block. Byte equality alone disqualifies a reviewer.
    if not in_rstar:
        return 'provisional', []
    author = reviewed_doc.get('author') if isinstance(reviewed_doc, dict) else None
    who = review.get('reviewer') if isinstance(review, dict) else None
    if fd.identity_ok(who) and who == author:
        return 'disqualified', []
    return 'genuine', fd.independence_problems(review, [author]) + review_binding_problems(repo, review, root)
