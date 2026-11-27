"""Local controls for the A1 staging amendment r2 supplement S-2 (procedural reviewer independence,
AMENDMENT-S-2.md sec. 7): the S-1 controls S-2 retains (restated where it says so), at the level of the predicates of
engine/sessions.py over explicit records in an in-memory repository, and the S-2 controls of record lint through the
run's lint (records.lint_chain). The control ids carry the prefix PRED: and name the S-1 or S-2 control whose
predicate dimension each exercises; none stands for the run-level control itself, and no expectation row is
registered by this suite.

Usage: python3 -I -B tools/ledger_coverage/adapters/sessions_controls.py OUT
Writes OUT/sessions-controls.json and exits 0 when every control holds, 1 otherwise.
"""
import importlib.util
import json
import os
import shutil
import sys

here = os.path.dirname(os.path.abspath(__file__))
if 'ledger_coverage' not in sys.modules:
    _pkg = os.path.dirname(here)
    _spec = importlib.util.spec_from_file_location('ledger_coverage', os.path.join(_pkg, '__init__.py'),
                                                   submodule_search_locations=[_pkg])
    sys.modules['ledger_coverage'] = importlib.util.module_from_spec(_spec)
    _spec.loader.exec_module(sys.modules['ledger_coverage'])

from ledger_coverage.adapters import control_records  # noqa: E402
from ledger_coverage.adapters.identity_fixture import review_record  # noqa: E402
from ledger_coverage.engine import gitobj  # noqa: E402
from ledger_coverage.engine import records  # noqa: E402
from ledger_coverage.engine import sessions as S  # noqa: E402
from ledger_coverage.engine import util  # noqa: E402

RESULTS = []
# R6.GATE.5 and R6.GATE.7: the runs captured since the previous case are its evidence
LOCAL = control_records.LocalSuite('sessions')
D = 'plan'


def case(cid, expected, actual, holds, attested=None):
    RESULTS.append({'id': cid, 'expected': expected, 'actual': actual, 'status': 'PASS' if holds else 'FAIL',
                    'attested': attested})
    LOCAL.case(cid)


W1, R1, X1 = 'session.w1', 'session.r1', 'session.x1'
REC_PATH = D + '/rec.json'
REC = {'schema': 'oi-scope/1', 'author': W1, 'record_id': 'x'}
REC_B = (json.dumps(REC) + '\n').encode()


class World(object):
    """R0 holds the record; F, its child, is the root a review is read from."""

    def __init__(self):
        self.ov = gitobj.Overlay()
        self.R0 = self.ov.add_commit({REC_PATH: REC_B}, [], 'R0')
        self.F = self.ov.add_commit({REC_PATH: REC_B, D + '/PREREG.md': b'# PREREG\n'}, [self.R0], 'F')


def review_of(w, reviewer, path, data, revision=None, **kw):
    """A review by `reviewer` of `path` (bytes `data`), its revision R0 unless given, with its declaration."""
    rv = review_record({'schema': records.review_schema, 'reviewer': reviewer, 'method': 'read',
                        'reviewed': {'path': path, 'blob_sha256': util.sha256(data)}, 'revision': revision or w.R0,
                        'verdicts': [{'item': 'i', 'verdict': 'accept'}], 'dissent': ''})
    rv.update(kw)
    return rv


def lint(w, reviewer, doc=None, root=None, mutate=None):
    rv = review_of(w, reviewer, REC_PATH, REC_B)
    if mutate:
        mutate(rv)
    return S.lint_review_problems(w.ov, rv, doc or REC, root or w.F)


def suite_retained():
    """S-2 sec. 7, retained from S-1."""
    w = World()
    case('PRED:S1-POS', 'writer w1, ordinary reviewer r1, widening reviewer x1, pairwise different identities, each '
                        'review with a valid revision and a declaration naming none of the other roles: the review '
                        'counts and the widening review is independent of w1 and r1',
         [lint(w, R1), records_widening(w)], lint(w, R1) == [] and records_widening(w) == [])
    x = lint(w, 'amaybaum', doc=dict(REC, author='amaybaum'))
    case('PRED:S1-LOGIN', 'author and reviewer both the shared GitHub login: the same identity, so the review '
                          'counts as no review', x, x != [])
    out = {}
    other = w.ov.add_commit({REC_PATH: b'other bytes\n'}, [w.F], 'other')
    out['other bytes'] = lint(w, R1, root=other, mutate=lambda rv: rv.__setitem__('revision', other))
    stray = w.ov.add_commit({REC_PATH: REC_B}, [], 'stray')
    out['unreachable from the root'] = lint(w, R1, mutate=lambda rv: rv.__setitem__('revision', stray))
    out['missing'] = lint(w, R1, mutate=lambda rv: rv.pop('revision'))
    out['not held'] = lint(w, R1, mutate=lambda rv: rv.__setitem__('revision', '7' * 40))
    case('PRED:S1-REVISION-MISMATCH', 'revision holding other bytes, unreachable from the root, missing or not held: '
                                      'the review counts as no review', out, all(out.values()))
    # post-F: a review whose revision is a commit after F, reachable from effective M, binds; and a post-F finding
    rev = w.ov.add_commit({REC_PATH: REC_B, 'post.txt': b'x\n'}, [w.F], 'after F')
    M = w.ov.add_commit({'later.txt': b'x\n'}, [rev], 'M')
    rv = review_of(w, R1, REC_PATH, REC_B, revision=rev)
    bind = S.review_binding_problems(w.ov, rv, M)
    rv2 = review_of(w, R1, REC_PATH, REC_B, revision=rev, invalidates={'path': REC_PATH})
    det = S.detection_outcome(w.ov, rv2, REC, True, M)
    case('PRED:S1-REVISION-POST-F', 'a custody review and a post-F finding review, revision a commit after F reachable '
                                    'from effective M: both bind', (bind, det), bind == [] and det == ('genuine', []))
    out = {}
    rv = review_of(w, W1, REC_PATH, REC_B, invalidates={'path': REC_PATH})
    out['same id, in R*'] = S.detection_outcome(w.ov, rv, REC, True, w.F)
    out['same id, absent from R*'] = S.detection_outcome(w.ov, rv, REC, False, w.F)
    case('PRED:S1-INVALIDATING-SAME-ID', 'an invalidating review whose reviewer is byte-equal to the record\'s author, '
                                         'record in R*: disqualified; absent from R*: provisional (r9 Amendment 1)',
         out, out['same id, in R*'] == ('disqualified', []) and out['same id, absent from R*'] == ('provisional', []))


def records_widening(w):
    """The S2.4 condition of the widening role (R6.REC.13): independent of the author and of the ordinary reviewer."""
    from ledger_coverage.engine import findings as fd
    return fd.independence_problems(review_of(w, X1, REC_PATH, REC_B), [W1, R1])


def suite_s2_lint():
    """Staging S-2 S2.4/S2.5 in record lint (R6.REC.6), through the run's lint (records.lint_chain): a review counts
    only when it is independent of the record's author, compared by key (S2.2), with its declaration (S2.3)."""
    author = 'session.fixture-writer'

    def lint(review=None, rec_author=author, **kw):
        doc = {'schema': 'oi-term-rules/2', 'record_id': 'r1', 'author': rec_author, 'supersedes': None,
               'rules': [{'id': 'q1'}]}
        rb = util.canonical(doc)
        ref = {'path': D + '/r.json', 'blob_sha256': util.sha256(rb)}
        rv = review_record({'schema': records.review_schema, 'reviewer': 'session.fixture-reviewer', 'reviewed': ref,
                            'method': 'read', 'verdicts': [{'item': 'q1', 'verdict': 'accept'}]})
        rv.update(kw)
        if review is not None:
            review(rv)
        entries = [(ref['path'], rb), (D + '/r.review.json', util.canonical(rv))]
        return records.lint_chain(ref, records.Store(entries), {util.sha256(b) for _, b in entries})
    got = lint()
    case('PRED:S2-POS', 'a review by another identity carrying a well-formed declaration: the record passes lint',
         got, got == [])
    decl = {'absent': lint(review=lambda r: r.pop('independence')),
            'not_author false': lint(independence={'not_author': False, 'depends_on': []}),
            'not_author "true"': lint(independence={'not_author': 'true', 'depends_on': []}),
            'an extra key': lint(independence={'not_author': True, 'depends_on': [], 'scope': 'x'}),
            'depends_on not an array': lint(independence={'not_author': True, 'depends_on': 'session.x'}),
            'depends_on holding a malformed string': lint(independence={'not_author': True, 'depends_on': ['a b']}),
            'two same-identity elements': lint(independence={'not_author': True,
                                                             'depends_on': ['session.x', 'Session_X']})}
    case('PRED:S2-DECL-MISSING', 'the declaration absent or malformed: the review counts as no review', decl,
         all(decl.values()))
    dep = {'names the author': lint(independence={'not_author': True, 'depends_on': [author]}),
           'names it respelled': lint(independence={'not_author': True, 'depends_on': ['SESSION_FIXTURE_WRITER']})}
    case('PRED:S2-DECL-AUTHOR', 'depends_on names the author, plainly or respelled: the review counts as no review',
         dep, all(dep.values()))
    same = {'Session_Fixture-Writer': lint(reviewer='Session_Fixture-Writer', rec_author='session.fixture-writer'),
            'SESSIONFIXTUREWRITER': lint(reviewer='SESSIONFIXTUREWRITER', rec_author='session.fixture-writer'),
            'shared login': lint(reviewer='amaybaum', rec_author='amaybaum')}
    case('PRED:S2-RESPELL', 'the writer reviewing its own record under a respelling, or author and reviewer one shared '
                            'login: the same identity by key, so the review counts as no review', same,
         all(same.values()))
    bad = [' session.r', 'session r', 'session.\u0433', '1234', '', 'a' * 129, 'https://example.invalid/runs/1']
    mal = {repr(v): lint(reviewer=v) for v in bad}
    mal.update({'author ' + repr(v): lint(rec_author=v) for v in bad})
    case('PRED:S2-MALFORMED', 'a reviewer or author that is not an identity string: the record fails lint', mal,
         all(mal.values()))


SUITES = [('retained', suite_retained), ('s2-lint', suite_s2_lint)]


def main(out):
    if os.path.exists(out):
        shutil.rmtree(out)
    os.makedirs(out)
    LOCAL.start()
    for name, fn in SUITES:
        try:
            fn()
        except Exception as exc:  # a suite that cannot run is a failed control of its own
            import traceback
            case(name + '/group-error', 'the suite runs', '%s: %s %s' % (type(exc).__name__, exc,
                                                                          traceback.format_exc()[-1500:]), False)
    with open(os.path.join(out, 'sessions-controls.json'), 'w') as f:
        json.dump({'schema': 'oi-local-controls/1', 'suite': 'sessions', 'cases': RESULTS}, f, indent=1,
                  sort_keys=True, default=str)
        f.write('\n')
    LOCAL.write(out, RESULTS)
    bad = [c['id'] for c in RESULTS if c['status'] != 'PASS']
    print(json.dumps({'cases': len(RESULTS), 'failed': bad}))
    return 0 if not bad else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else 'sessions-controls-out'))
