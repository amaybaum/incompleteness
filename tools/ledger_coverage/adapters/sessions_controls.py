"""Local controls for the A1 staging amendment r2 supplement S-1 (recorded session identities, AMENDMENT-S-1.md sec. 8),
at the level of its mechanical predicates (engine/sessions.py) over explicit records in an in-memory repository. The
predicates are not yet called by a run: applying the identity change to every record the tool reads (OQ-S1-1) needs
every record fixture migrated to registered identities first. The control ids carry the prefix PRED: and name the
S-1 control whose predicate dimension each exercises; none stands for the run-level control itself, and no
expectation row is registered by this suite.

Usage: python3 -I -B tools/ledger_coverage/adapters/sessions_controls.py OUT
Writes OUT/sessions-controls.json and exits 0 when every control holds, 1 otherwise.
"""
import copy
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

from ledger_coverage import record_authority as ra  # noqa: E402
from ledger_coverage.engine import config  # noqa: E402
from ledger_coverage.engine import gitobj  # noqa: E402
from ledger_coverage.engine import records  # noqa: E402
from ledger_coverage.engine import sessions as S  # noqa: E402
from ledger_coverage.engine import util  # noqa: E402

RESULTS = []
D = 'plan'
REG = D + '/' + ra.session_registry
REPO = ra.session_repository
THREADS = ra.session_designation_threads


def case(cid, expected, actual, holds):
    RESULTS.append({'id': cid, 'expected': expected, 'actual': actual, 'status': 'PASS' if holds else 'FAIL'})


def url(n, thread=1169, repo=REPO, kind='issues'):
    return 'https://github.com/%s/%s/%d#issuecomment-%d' % (repo, kind, thread, n)


def entry(pid, ref, spawned_by=None, same_party=(), scope=(D,), n=None):
    return {'id': pid, 'kind': pid.split('.', 1)[0], 'platform_ref': ref, 'spawned_by': spawned_by,
            'same_party': list(same_party), 'scope': list(scope), 'designation': url(n or (100 + len(pid)))}


W1, R1, X1, RR = 'session.w1', 'session.r1', 'session.x1', 'session.reg-reviewer'


def base_entries():
    return [entry(W1, 'p-w1'), entry(R1, 'p-r1'), entry(X1, 'p-x1'), entry(RR, 'p-rr'),
            entry('person.owner', 'p-owner', scope=(D, 'verification'))]


def registry(parties=None, withdrawn=(), author=W1):
    return {'schema': S.schema, 'author': author, 'parties': parties if parties is not None else base_entries(),
            'withdrawn': list(withdrawn)}


def pins(rows):
    return ('# PREREG\n\n### 1.1 Record pins\n\n| file | sha256 |\n|---|---|\n' +
            ''.join('| `%s` | `%s` |\n' % r for r in rows)).encode()


class World(object):
    """F: the registry, its pinned review and the PREREG.md beside them; R0, F's parent, holds the registry alone and
    is the review's revision."""

    def __init__(self, reg=None, review=None, mutate_review=None, pin_registry=True, pin_review=True,
                 registry_bytes=None, extra=None, reviewer=RR):
        self.ov = gitobj.Overlay()
        self.reg = reg if reg is not None else registry()
        self.data = registry_bytes if registry_bytes is not None else util.canonical(self.reg)
        self.sha = util.sha256(self.data)
        self.R0 = self.ov.add_commit({REG: self.data}, [], 'R0')
        es = S.entries(self.reg)
        rv = review if review is not None else {
            'schema': records.review_schema, 'reviewer': reviewer, 'method': 'read',
            'reviewed': {'path': REG, 'blob_sha256': self.sha}, 'revision': self.R0,
            'platform_ref': (es.get(reviewer) or {}).get('platform_ref', 'p-none'),
            'verdicts': [{'item': i, 'verdict': 'accept'} for i in records.item_ids(self.reg)], 'dissent': ''}
        if mutate_review:
            mutate_review(rv)
        self.review = rv
        self.rv_bytes = (json.dumps(rv, indent=1, sort_keys=True) + '\n').encode()
        rows = []
        if pin_registry:
            rows.append((ra.session_registry, self.sha))
        if pin_review:
            rows.append(('reg.review.json', util.sha256(self.rv_bytes)))
        files = {REG: self.data, D + '/reg.review.json': self.rv_bytes, D + '/PREREG.md': pins(rows)}
        files.update(extra or {})
        self.F = self.ov.add_commit(files, [self.R0], 'F')

    def admit(self, cfg_records=()):
        return S.admit(self.ov, self.F, D, config.read_pin_table, cfg_records, ra.session_registry, REPO, THREADS)


def canon(doc):
    return util.canonical(doc)


def review_of(w, reviewer, path, data, revision=None, platform_ref=None, rid='r', **kw):
    """A review by `reviewer` of `path` (bytes `data`) whose revision is a commit holding it, child of F."""
    rev = revision or w.ov.add_commit({path: data}, [w.F], 'rev-' + rid)
    es = S.entries(w.reg)
    rv = {'schema': records.review_schema, 'reviewer': reviewer, 'method': 'read',
          'reviewed': {'path': path, 'blob_sha256': util.sha256(data)}, 'revision': rev,
          'platform_ref': platform_ref if platform_ref is not None else (es.get(reviewer) or {}).get('platform_ref'),
          'verdicts': [{'item': 'i', 'verdict': 'accept'}], 'dissent': ''}
    rv.update(kw)
    return rv, rev


REC_PATH = D + '/rec.json'
REC = {'schema': 'oi-scope/1', 'author': W1, 'record_id': 'x'}
REC_B = (json.dumps(REC) + '\n').encode()


def lint(w, reviewer, doc=None, root=None, review_path=D + '/rec.review.json', mutate=None, registry_failed=False,
         rec_path=REC_PATH):
    rv, rev = review_of(w, reviewer, rec_path, REC_B)
    if mutate:
        mutate(rv, rev)
    return S.lint_review_problems(w.ov, rv, review_path, REC, doc or w.reg, root or rev, registry_failed)


def with_entries(fn):
    es = base_entries()
    fn({e['id']: e for e in es})
    return registry(es)


def suite_admission():
    w = World()
    doc, probs = w.admit()
    case('PRED:S1-POS/admission', 'the registry pinned at F, canonical, with one pinned review by a reviewer outside '
                                  'the writer\'s party accepting every item, is admitted', probs, doc is not None and not probs)
    case('PRED:S1-POS/lint', 'a review by r1 of w1\'s record, revision holding the bytes, platform_ref equal, in scope: '
                             'counts', lint(w, R1), lint(w, R1) == [])
    case('PRED:S1-POS/widening', 'writer w1, ordinary reviewer r1, widening reviewer x1 in distinct parties',
         S.independence_problems(w.reg, W1, [R1], X1), S.independence_problems(w.reg, W1, [R1], X1) == [])
    case('PRED:S1-POS/item-ids', 'R6.RECON.31 row: party:<id> per entry and withdrawn:<id> per withdrawal',
         records.item_ids(registry(withdrawn=[{'id': X1, 'designation': url(7)}])),
         records.item_ids(registry(withdrawn=[{'id': X1, 'designation': url(7)}])) ==
         ['party:' + e['id'] for e in base_entries()] + ['withdrawn:' + X1])

    out = {}
    out['absent from the pin table'] = World(pin_registry=False).admit()[1]
    w2 = World()
    out['differs from its pinned SHA-256'] = S.admit(
        _with_file(w2, REG, w2.data + b' '), w2.F2, D, config.read_pin_table, (), ra.session_registry, REPO,
        THREADS)[1]
    out['no pinned review'] = World(pin_review=False).admit()[1]
    w3 = World()
    out['two pinned reviews'] = S.admit(_with_file(w3, D + '/reg.review2.json', w3.rv_bytes, pin=True), w3.F2, D,
                                        config.read_pin_table, (), ra.session_registry, REPO, THREADS)[1]
    out['not canonical'] = World(registry_bytes=json.dumps(registry(), indent=1).encode()).admit()[1]
    want = {'absent from the pin table': 'not pinned', 'differs from its pinned SHA-256': 'pinned SHA-256',
            'no pinned review': 'no pinned review', 'two pinned reviews': 'more than one',
            'not canonical': 'not canonical'}
    case('PRED:S1-NO-REGISTRY', 'absent from F\'s pin table, differing from its pinned SHA-256, without its pinned '
                                'review, with two, or not canonical JSON: the registry fails, each for that reason',
         out, all(any(want[k] in p for p in out[k]) for k in want))
    # a registry in D_rec at F that F's pin table does not pin is never read (no argument, commit author or host
    # record supplies one: admit has no such input)
    out = World(pin_registry=False).admit()
    case('PRED:S1-REGISTRY-BY-ARGUMENT', 'a registry present in D_rec but not pinned by F: ignored, the registry fails',
         out, out[0] is None and out[1] == ['the registry is not pinned at F'])

    out = {}
    w = World()
    try:
        w.admit([{'kind': 'sessions', 'path': D + '/other-sessions.json', 'blob_sha256': w.sha}])
        out['other path'] = 'admitted'
    except ValueError as exc:
        out['other path'] = str(exc)
    try:
        w.admit([{'kind': 'sessions', 'path': REG, 'blob_sha256': '7' * 64}])
        out['other blob'] = 'admitted'
    except ValueError as exc:
        out['other blob'] = str(exc)
    try:
        w.admit([{'kind': 'sessions', 'path': REG, 'blob_sha256': w.sha}])
        out['the pinned reference'] = 'admitted'
    except ValueError as exc:
        out['the pinned reference'] = str(exc)
    case('PRED:S1-KIND-ROW', 'R6.RECON.33 row: a configuration record of kind sessions other than the pinned path and '
                             'blob is CONFIG_INVALID; the pinned reference is accepted', out,
         out['other path'].startswith('CONFIG_INVALID') and out['other blob'].startswith('CONFIG_INVALID') and
         out['the pinned reference'] == 'admitted')

    out = {}
    out['omits a withdrawn item'] = World(reg=registry(withdrawn=[{'id': X1, 'designation': url(7)}]),
                                          mutate_review=lambda rv: rv.__setitem__('verdicts', [
                                              v for v in rv['verdicts'] if not v['item'].startswith('withdrawn:')])
                                          ).admit()[1]
    case('PRED:S1-REGISTRY-REVIEW-PARTIAL', 'the registry review accepts every party: item and omits a withdrawn: item: '
                                            'the registry fails', out, all(out.values()))
    out = {}
    out['rejects party:r1'] = World(mutate_review=lambda rv: rv['verdicts'][[v['item'] for v in rv['verdicts']].index(
        'party:' + R1)].__setitem__('verdict', 'reject')).admit()[1]
    case('PRED:S1-MISSING-LINK', 'r1 was spawned by w1 but its entry has spawned_by null; the registry review rejects '
                                 'the item against the form comment: the registry fails, and with it every review',
         out, all(out.values()) and lint(World(), R1, registry_failed=True) != [])
    out = {}
    out['registry reviewer in the writer\'s party'] = World(reviewer=R1, reg=with_entries(
        lambda m: m[R1].__setitem__('same_party', [W1]))).admit()[1]
    out['registry reviewer scope misses D_rec'] = World(reg=with_entries(
        lambda m: m[RR].__setitem__('scope', ['elsewhere']))).admit()[1]
    case('PRED:S1-REGISTRY-REVIEWER', 'the registry\'s reviewer in the writer\'s party, or without scope over D_rec: '
                                      'the registry fails', out, all(out.values()))


def _with_file(w, path, data, pin=False):
    """A child F2 of F that changes one file; with pin, also lists it in the pin table."""
    files = {p: w.ov.read(w.F, p) for p in w.ov.entries(w.F)}
    files[path] = data
    if pin:
        rows = list(config.read_pin_table(w.ov.read(w.F, D + '/PREREG.md')).items())
        rows.append((path.rsplit('/', 1)[1], util.sha256(data)))
        files[D + '/PREREG.md'] = pins(rows)
    w.F2 = w.ov.add_commit(files, [w.F], 'F2')
    return w.ov


def suite_wellformed():
    def probs(reg):
        return S.registry_problems(canon(reg), reg, REPO, THREADS)
    out = {}
    out['same_party names no entry'] = probs(with_entries(lambda m: m[R1].__setitem__('same_party', ['session.ghost'])))
    out['spawned_by names no entry'] = probs(with_entries(lambda m: m[R1].__setitem__('spawned_by', 'session.ghost')))
    out['withdrawn id names no entry'] = probs(registry(withdrawn=[{'id': 'session.ghost', 'designation': url(7)}]))
    case('PRED:S1-DANGLING-LINK', 'a same_party or spawned_by member, or a withdrawn element\'s id, names no entry: the '
                                  'registry fails', out, all(out.values()))
    out = {}
    es = base_entries()
    out['equal ids'] = probs(registry(es + [dict(es[1], platform_ref='p-other')]))
    out['prefix differs from kind'] = probs(with_entries(lambda m: m[R1].__setitem__('kind', 'person')))
    out['shared platform_ref'] = probs(with_entries(lambda m: m[R1].__setitem__('platform_ref', 'p-w1')))
    out['upper-case id'] = probs(with_entries(lambda m: m[R1].__setitem__('id', 'session.R1')))
    out['root as scope'] = probs(with_entries(lambda m: m[R1].__setitem__('scope', ['.'])))
    out['extra key'] = probs(with_entries(lambda m: m[R1].__setitem__('note', 'x')))
    out['author not an entry'] = probs(registry(author='session.ghost'))
    case('PRED:S1-DUP-ID', 'equal ids; an id whose prefix differs from its kind; a shared platform_ref; and the grammar '
                           'near-misses (upper case, the root as scope, a key outside the closed set, an author that is '
                           'not an entry): the registry fails', out, all(out.values()))
    out = {}
    out['empty'] = probs(with_entries(lambda m: m[R1].__setitem__('designation', '')))
    out['not a comment URL'] = probs(with_entries(lambda m: m[R1].__setitem__('designation', 'https://example.org/x')))
    out['another repository'] = probs(with_entries(lambda m: m[R1].__setitem__('designation', url(5, repo='o/r'))))
    out['an unadmitted thread'] = probs(with_entries(lambda m: m[R1].__setitem__('designation', url(5, thread=42))))
    out['withdrawal designation not a comment URL'] = probs(registry(withdrawn=[{'id': X1, 'designation': 'x'}]))
    ok = {'#1169 issue': probs(with_entries(lambda m: m[R1].__setitem__('designation', url(5)))),
          '#1577 pull': probs(with_entries(lambda m: m[R1].__setitem__('designation', url(5, 1577, kind='pull'))))}
    case('PRED:S1-DESIGNATION', 'a designation empty, not a comment URL, in another repository or in an unadmitted '
                                'thread: the registry fails; a comment URL in #1169 or #1577 is accepted', (out, ok),
         all(out.values()) and not any(ok.values()))
    out = {'bare login': 'amaybaum', 'prefix differs': 'person.w1', 'upper case': 'session.W1',
           'absent from the registry': 'session.ghost', 'a URL': url(5)}
    got = {k: S.is_identity(registry(), v) for k, v in out.items()}
    case('PRED:S1-LOGIN', 'author and reviewer as a GitHub login, or the other near-miss mutants of R6.RECON.29: not '
                          'identity strings; the record fails lint', (got, S.record_author_problems(
                              registry(), dict(REC, author='amaybaum'), REC_PATH)),
         not any(got.values()) and S.record_author_problems(registry(), dict(REC, author='amaybaum'), REC_PATH) != [])


def suite_party():
    out = {}
    for name, fn in (('S1-SAME-PARTY', lambda m: m[R1].__setitem__('same_party', [W1])),
                     ('S1-SAME-PARTY-REVERSED', lambda m: m[W1].__setitem__('same_party', [R1])),
                     ('S1-SPAWNED', lambda m: m[R1].__setitem__('spawned_by', W1))):
        reg = with_entries(fn)
        w = World(reg=reg)
        out[name] = lint(w, R1)
        case('PRED:' + name, 'the reviewer in the author\'s party: review disqualified', out[name], out[name] != [])
    es = base_entries() + [entry('session.s', 'p-s', same_party=[W1])]
    for e in es:
        if e['id'] == R1:
            e['same_party'] = ['session.s']
    w = World(reg=registry(es))
    x = lint(w, R1)
    case('PRED:S1-SAME-PARTY-CHAIN', 'r1 -> s -> w1 through same_party: review disqualified', x, x != [])
    reg = with_entries(lambda m: m[X1].__setitem__('same_party', [R1]))
    x = S.independence_problems(reg, W1, [R1], X1)
    case('PRED:S1-WIDENING-SAME-PARTY', 'the widening reviewer in an ordinary reviewer\'s party: disqualified', x, x != [])
    reg = with_entries(lambda m: m[X1].__setitem__('spawned_by', W1))
    x = S.independence_problems(reg, W1, [R1], X1)
    case('PRED:S1-WIDENING-AUTHOR-PARTY', 'the widening reviewer in the author\'s party: disqualified', x, x != [])
    reg = registry()
    x = S.independence_problems(reg, W1, [R1, 'session.r9'], X1)
    case('PRED:S1-WIDENING-ANY-ORDINARY', 'the widening comparison runs against every ordinary reviewer', x,
         x == [] and S.independence_problems(with_entries(lambda m: m[X1].__setitem__('same_party', [RR])), W1,
                                             [R1, RR], X1) != [])
    unreg = lint(World(), 'session.ghost')
    case('PRED:S1-UNREGISTERED', 'the reviewer id is in no entry: review disqualified', unreg, unreg != [])


def suite_withdrawal():
    reg = registry(base_entries() + [entry('session.r2', 'p-r2')],
                   withdrawn=[{'id': 'session.r2', 'designation': url(9)}])
    w = World(reg=reg)
    x = lint(w, 'session.r2')
    rv, _ = review_of(w, 'session.r2', REC_PATH, REC_B, invalidates={'path': REC_PATH})
    det = S.detection_outcome(w.ov, rv, D + '/inv.json', REC, True, reg, rv['revision'], False)
    case('PRED:S1-WITHDRAWN', 'a review by a withdrawn id is disqualified; an invalidating review by it is a genuine '
                              'finding with a form failure (the permanent block)', (x, det),
         x != [] and det[0] == 'genuine' and det[1] != [])
    es = base_entries() + [entry('session.r2', 'p-r2', same_party=[W1]), entry('session.r3', 'p-r3',
                                                                               same_party=['session.r2'])]
    reg = registry(es, withdrawn=[{'id': 'session.r2', 'designation': url(9)}])
    w = World(reg=reg)
    x = lint(w, 'session.r3')
    case('PRED:S1-WITHDRAWAL-KEEPS-LINKS', 'r2 in w1\'s party and withdrawn; r3 linked to w1 only through r2: still '
                                           'in w1\'s party, review disqualified', x, x != [])
    prev = registry(withdrawn=[{'id': X1, 'designation': url(9)}])
    x = S.append_only_problems(prev, registry())
    case('PRED:S1-WITHDRAWAL-REMOVED', 'a withdrawal listed at F_prev absent at F: the registry fails (S1.5)', x, x != [])


def suite_continuity():
    prev = registry()
    out = {}
    out['an entry removed'] = S.append_only_problems(prev, registry(base_entries()[1:]))
    out['an entry edited'] = S.append_only_problems(prev, with_entries(lambda m: m[R1].__setitem__('scope', ['x'])))
    out['a new entry linking two parties'] = S.append_only_problems(
        prev, registry(base_entries() + [entry('session.n', 'p-n', same_party=[W1, R1])]))
    ok = S.append_only_problems(prev, registry(base_entries() + [entry('session.n', 'p-n', same_party=[W1])]))
    case('PRED:S1-REGISTRY-CHANGED', 'between F_prev and F an entry removed, edited, or a new entry linking two existing '
                                     'parties: the registry fails; a new entry joining one party is accepted', (out, ok),
         all(out.values()) and ok == [])
    # a genuine finding at F_prev keeps binding: the later registry that would merge its reviewer into the author's
    # party fails S1.5, so the F_prev registry is the one that decides the finding
    w = World(reg=prev)
    rv, _ = review_of(w, R1, REC_PATH, REC_B, invalidates={'path': REC_PATH})
    at_prev = S.detection_outcome(w.ov, rv, D + '/inv.json', REC, True, prev, rv['revision'], False)
    later = with_entries(lambda m: m[R1].__setitem__('same_party', [W1]))
    case('PRED:S1-RETRO-MERGE', 'a finding genuine at F_prev; a later registry linking its reviewer and author fails '
                                'S1.5, and the finding keeps binding', (at_prev, S.append_only_problems(prev, later)),
         at_prev == ('genuine', []) and S.append_only_problems(prev, later) != [])


def suite_binding():
    w = World()
    out = {}
    out['platform_ref differs'] = lint(w, R1, mutate=lambda rv, rev: rv.__setitem__('platform_ref', 'p-w1'))
    out['platform_ref missing'] = lint(w, R1, mutate=lambda rv, rev: rv.pop('platform_ref'))
    case('PRED:S1-PLATFORM-REF', 'a review\'s platform_ref differs from its reviewer\'s entry, or is missing: '
                                 'disqualified', out, all(out.values()))
    out = {}
    other = w.ov.add_commit({REC_PATH: b'other bytes\n'}, [w.F], 'other')
    out['other bytes'] = lint(w, R1, root=other, mutate=lambda rv, rev: rv.__setitem__('revision', other))
    stray = w.ov.add_commit({REC_PATH: REC_B}, [], 'stray')
    out['unreachable from the root'] = lint(w, R1, root=w.F, mutate=lambda rv, rev: rv.__setitem__('revision', stray))
    out['missing'] = lint(w, R1, mutate=lambda rv, rev: rv.pop('revision'))
    out['not held'] = lint(w, R1, mutate=lambda rv, rev: rv.__setitem__('revision', '7' * 40))
    case('PRED:S1-REVISION-MISMATCH', 'revision holding other bytes, unreachable from the root, missing or not held: '
                                      'disqualified', out, all(out.values()))
    # post-F: a review whose revision is a commit after F, reachable from effective M, binds; and a post-F finding
    rv, rev = review_of(w, R1, REC_PATH, REC_B)
    M = w.ov.add_commit({'later.txt': b'x\n'}, [rev], 'M')
    bind = S.review_binding_problems(w.ov, rv, D + '/rec.review.json', w.reg, M)
    rv2, _ = review_of(w, R1, REC_PATH, REC_B, revision=rev, invalidates={'path': REC_PATH})
    det = S.detection_outcome(w.ov, rv2, D + '/inv.json', REC, True, w.reg, M, False)
    case('PRED:S1-REVISION-POST-F', 'a custody review and a post-F finding review, revision a commit after F reachable '
                                    'from effective M: both bind', (bind, det), bind == [] and det == ('genuine', []))
    reg = with_entries(lambda m: m[R1].__setitem__('scope', ['a/b']))
    w2 = World(reg=reg)
    out = {'a/bc/x.json': lint(w2, R1, rec_path='a/bc/x.json', review_path='a/b/r.json'),
           'a/b/c/x.json (covered)': lint(w2, R1, rec_path='a/b/c/x.json', review_path='a/b/r.json')}
    case('PRED:S1-SCOPE-BOUNDARY', 'scope a/b; reviewed path a/bc/x.json: disqualified; a/b/c/x.json is covered', out,
         out['a/bc/x.json'] != [] and out['a/b/c/x.json (covered)'] == [])
    x = lint(w, R1, review_path='elsewhere/rec.review.json')
    case('PRED:S1-OUT-OF-SCOPE', 'the review file\'s own path outside the reviewer\'s scope: disqualified', x, x != [])
    x = S.record_author_problems(w.reg, REC, 'elsewhere/rec.json')
    case('PRED:S1-AUTHOR-SCOPE', 'a record\'s path outside its author\'s scope: the record fails lint', x, x != [])


def suite_detection():
    w = World()
    out = {}
    rv, _ = review_of(w, W1, REC_PATH, REC_B, invalidates={'path': REC_PATH})
    out['same id, in R*'] = S.detection_outcome(w.ov, rv, D + '/i.json', REC, True, w.reg, rv['revision'], False)
    out['same id, absent from R*'] = S.detection_outcome(w.ov, rv, D + '/i.json', REC, False, w.reg, rv['revision'],
                                                         False)
    case('PRED:S1-INVALIDATING-SAME-ID', 'an invalidating review whose reviewer is the record author\'s id, record in '
                                         'R*: disqualified; absent from R*: provisional (r9 Amendment 1)', out,
         out['same id, in R*'] == ('disqualified', []) and out['same id, absent from R*'] == ('provisional', []))
    reg = with_entries(lambda m: m[R1].__setitem__('same_party', [W1]))
    w2 = World(reg=reg)
    rv, _ = review_of(w2, R1, REC_PATH, REC_B, invalidates={'path': REC_PATH})
    x = S.detection_outcome(w2.ov, rv, D + '/i.json', REC, True, reg, rv['revision'], False)
    case('PRED:S1-INVALIDATING-SAME-PARTY', 'the reviewer in the author\'s party but not the same id: a genuine finding '
                                            'with a form failure', x, x[0] == 'genuine' and x[1] != [])
    out = {}
    rv, _ = review_of(w, 'session.ghost', REC_PATH, REC_B, invalidates={'path': REC_PATH})
    out['not an identity string'] = S.detection_outcome(w.ov, rv, D + '/i.json', REC, True, w.reg, rv['revision'],
                                                        False)
    rv, _ = review_of(w, R1, REC_PATH, REC_B, invalidates={'path': REC_PATH})
    out['registry fails'] = S.detection_outcome(w.ov, rv, D + '/i.json', REC, True, w.reg, rv['revision'], True)
    rv3 = copy.deepcopy(rv)
    rv3['platform_ref'] = 'p-x1'
    out['platform_ref fails'] = S.detection_outcome(w.ov, rv3, D + '/i.json', REC, True, w.reg, rv['revision'], False)
    case('PRED:S1-INVALIDATING-UNREGISTERED', 'a reviewer that is not an identity string, a failed registry or a failed '
                                              'platform_ref: a genuine finding with a form failure, never a lapse', out,
         all(v[0] == 'genuine' and v[1] for v in out.values()))


SUITES = [('admission', suite_admission), ('wellformed', suite_wellformed), ('party', suite_party),
          ('withdrawal', suite_withdrawal), ('continuity', suite_continuity), ('binding', suite_binding),
          ('detection', suite_detection)]


def main(out):
    if os.path.exists(out):
        shutil.rmtree(out)
    os.makedirs(out)
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
    bad = [c['id'] for c in RESULTS if c['status'] != 'PASS']
    print(json.dumps({'cases': len(RESULTS), 'failed': bad}))
    return 0 if not bad else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else 'sessions-controls-out'))
