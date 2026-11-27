"""Fixture identities and the review records of the control fixtures (staging S-2): identity strings (S2.1) for the
fixture parties, the one constructor of a review record, which carries S2.3's independence declaration, and the
binding of a review to the commit its reviewer read (`revision`, S-1 sec. 3 as S-2 S2.3 keeps it).
"""
import json

from ledger_coverage import record_authority as ra

WRITER = 'session.fixture-writer'
REVIEWER = 'session.fixture-reviewer'
WIDENER = 'session.fixture-widener'
OWNER = ra.OWNER_IDENTITIES[0]
REVIEW_SCHEMA = 'oi-review-record/1'


def review_record(fields):
    """Every review record the fixtures and controls construct is built here, from its fields. It carries staging S-2
    S2.3's independence declaration, {not_author: true, depends_on: []}, unless the fields give one."""
    out = dict(fields)
    out.setdefault('independence', {'not_author': True, 'depends_on': []})
    return out


def bind(review, revision):
    """A review carrying `revision`, a commit holding the reviewed bytes and reachable from the root the review is
    read from (S-1 sec. 3), and its independence declaration (S-2 S2.3)."""
    out = review_record(review)
    out['revision'] = revision
    return out


def is_review(data):
    try:
        d = json.loads(data.decode('utf-8'))
    except (ValueError, UnicodeDecodeError, AttributeError):
        return False
    return isinstance(d, dict) and d.get('schema') == REVIEW_SCHEMA
