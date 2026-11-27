"""Fixture identities for staging S-1 (recorded session identities): registered ids in place of logins, a session
registry and its review, and the review fields S-1 sec. 3 binds (`revision`, `platform_ref`). Used by the control
fixtures; a fixture supplies its own registry among its test objects (S-1 sec. 5, registry source for controls).

The owner's entry is one constant, OWNER, of kind "person": how a registry entry is marked as the owner (for
migration.approval and the adjudication owner identities) awaits an owner decision, and whichever form it takes is
slotted in here.
"""
import json
import re

from ledger_coverage import record_authority as ra
from ledger_coverage.engine import util

WRITER = 'session.fixture-writer'
REVIEWER = 'session.fixture-reviewer'
WIDENER = 'session.fixture-widener'
REGISTRY_REVIEWER = 'session.fixture-registry-reviewer'
OWNER = 'person.fixture-owner'
BASE_IDS = (WRITER, REVIEWER, WIDENER, REGISTRY_REVIEWER, OWNER)
# top-level directories the fixture parties may author and review in (S1.6; the root is never a scope)
SCOPE = ('book', 'doc', 'out', 'papers', 'plan', 'syn', 'tools', 'verification')
REGISTRY_FILE = ra.session_registry
REVIEW_SCHEMA = 'oi-review-record/1'


def review_record(fields):
    """Every review record the fixtures and controls construct is built here, from its fields. It carries staging S-2
    S2.3's independence declaration, {not_author: true, depends_on: []}, unless the fields give one."""
    out = dict(fields)
    out.setdefault('independence', {'not_author': True, 'depends_on': []})
    return out


def session_id(name):
    """The registered id of a further fixture party named `name` (for example a second writer)."""
    s = re.sub('[^a-z0-9-]+', '-', name.lower()).strip('-') or 'party'
    return 'session.fixture-' + s


def platform_ref(pid):
    return 'fixture:' + pid


def designation(n):
    """An owner form comment URL in #1169 posted after the thread's admission (S1.2)."""
    return 'https://github.com/%s/issues/1169#issuecomment-%d' % (ra.session_repository,
                                                                   ra.session_designation_threads[1169] + n)


def entry(pid, n, spawned_by=None, same_party=(), scope=SCOPE):
    return {'id': pid, 'kind': pid.split('.', 1)[0], 'platform_ref': platform_ref(pid), 'spawned_by': spawned_by,
            'same_party': list(same_party), 'scope': list(scope), 'designation': designation(n)}


def registry(ids=BASE_IDS, author=WRITER, withdrawn=()):
    ids = list(dict.fromkeys(ids))
    return {'schema': ra.session_registry_schema, 'author': author,
            'parties': [entry(pid, i + 1) for i, pid in enumerate(ids)], 'withdrawn': list(withdrawn)}


def registry_bytes(doc):
    return util.canonical(doc)


def item_ids(doc):
    return ['party:%s' % e['id'] for e in doc['parties']] + ['withdrawn:%s' % w['id'] for w in doc['withdrawn']]


def bind(review, revision):
    """A review carrying the sec. 3 binding: `revision` (a commit holding the reviewed bytes, reachable from the root
    the review is read from) and `platform_ref` equal to its reviewer's entry."""
    out = dict(review)
    out['revision'] = revision
    out['platform_ref'] = platform_ref(review.get('reviewer'))
    return out


def registry_review(path, data, revision, reviewer=REGISTRY_REVIEWER):
    doc = json.loads(data.decode('utf-8'))
    return bind(review_record({'schema': REVIEW_SCHEMA, 'reviewer': reviewer,
                 'reviewed': {'path': path, 'blob_sha256': util.sha256(data)},
                 'method': 'checked each entry and withdrawal against its form comment',
                 'verdicts': [{'item': i, 'verdict': 'accept'} for i in item_ids(doc)]}), revision)


def is_review(data):
    try:
        d = json.loads(data.decode('utf-8'))
    except (ValueError, UnicodeDecodeError, AttributeError):
        return False
    return isinstance(d, dict) and d.get('schema') == REVIEW_SCHEMA
