"""Preregistered controls of design amendment r4: the record-directory rule (O9-1 to O9-25, O9-12b; A.9) and the
item-2 record interfaces (I2-1 to I2-8; B.4). Run by conformance_controls.py; each control records its id, its
expectation, its predicate and what it found.

Engine-level cases build their repositories in memory and call the M role (`Execution.main_role`), the R11 condition
(`reconcile.evaluate`) or the context (`reconcile.RecordDirectory`) directly; the cases marked "full path" run the
`execution` or `coverage` operation through `cli.run` on the synthetic host world, with the tool's own authority
constant (`record_authority.AUTHORIZED_RECORD_DIRECTORIES`).
"""
import io
import json
import re

from ledger_coverage import record_authority
from ledger_coverage.engine import cli, execution as exmod, outcome as oc, pipeline as pl, reconcile as rc, util
from ledger_coverage.engine import controls_engine as ce
from ledger_coverage.engine.gitobj import Overlay
from ledger_coverage.adapters import host_fixture as hf, synthetic_fixture as sf

AUTH = record_authority.AUTHORIZED_RECORD_DIRECTORIES[0]
CFG = AUTH + '/retirement-config.json'
PRE = AUTH + '/PREREG.md'


def sha(b):
    return util.sha256(b)


# ---- engine-level worlds ---------------------------------------------------------------------------------------

class ModeOverlay:
    """A test double over an Overlay that reports mode 100755 for chosen (commit, path) entries (the Overlay has no
    executable-file value); every other call is the Overlay's."""

    def __init__(self, repo, exec_entries):
        self._r = repo
        self._x = set(exec_entries)

    def entries(self, cid):
        e = dict(self._r.entries(cid))
        for c, p in self._x:
            if c == cid and p in e:
                e[p] = ('100755', e[p][1])
        return e

    def mode(self, cid, path):
        e = self.entries(cid).get(path)
        return None if e is None else e[0]

    def __getattr__(self, name):
        return getattr(self._r, name)


class Ctx:
    def __init__(self, repo, corpus=()):
        self.repo = repo
        self._c = set(corpus)

    def in_corpus(self, p):
        return p in self._c


def plan_files(d=AUTH, cfg=None, extra=None):
    files = {d + '/retirement-config.json': b'{"synthetic": "configuration"}\n',
             d + '/PREREG.md': b'# synthetic plan\n\n### 1.1 Record pins\n',
             d + '/review.json': b'{"synthetic": "review"}\n',
             d + '/ledger.json': b'{"synthetic": "ledger"}\n'}
    files.update(extra or {})
    return files


def world(m_change=None, f_extra=None, h_extra=None, m_extra=None, d=AUTH):
    """H (a base commit), F (H plus the plan directory) and M (H plus the plan directory as merged, with
    `m_change` applied: {path: bytes, tuple or None})."""
    repo = Overlay(None)
    hfiles = {'doc/a.md': b'base text\n', 'notes/n.txt': b'note\n'}
    hfiles.update(h_extra or {})
    H = repo.add_commit(hfiles, [], 'H')
    pf = plan_files(d, extra=f_extra)
    F = repo.derive(H, pf, parents=[H], subject='F')
    mf = dict(pf)
    mf.update(m_extra or {})
    for p, v in (m_change or {}).items():
        mf[p] = v
    M = repo.derive(H, mf, parents=[H], subject='M')
    return repo, H, F, M


def run_main(repo, H, F, M, cpath=CFG, classes=(), authorized=(AUTH,), ledgered=(), corpus=(), rule=True):
    """The M role (Execution.main_role) over H..M, with the record-directory rule when `rule`."""
    led = {'base': H, 'files': {p: {} for p in ledgered}, 'splices': [], 'retained': []}
    ex = exmod.Execution(Ctx(repo, corpus), H, H, led, None, M, None, None, list(classes), ())
    ex.record_refs = {}
    if rule:
        ex.record_dir_args = {'F': F, 'cpath': cpath, 'authorized': tuple(authorized)}
    try:
        ex.main_role(set(ledgered) | set(corpus))
    except oc.Stop as s:
        return {'stop': s.cls, 'condition': (s.detail or {}).get('condition'), 'message': s.message}
    except Exception as exc:  # recorded, so that a control can require its absence
        return {'exception': '%s: %s' % (type(exc).__name__, exc)}
    return {'items': sorted((i['class'], i['subject'], i.get('why')) for i in ex.items),
            'side': sorted((e['path'], e['class'], e.get('why')) for e in ex.side_changes),
            'rd': ex.rd.summary() if ex.rd else None, 'entries': ex.side_changes}


def r11(repo, H, F, M, cpath=CFG, classes=(), authorized=(AUTH,), ledgered=(), corpus=()):
    """R11 of a reconciliation record whose own path is outside the world, evaluated with the run's context."""
    try:
        rd = rc.RecordDirectory(repo, H, F, M, cpath, authorized, set(ledgered), Ctx(repo, corpus).in_corpus,
                                list(classes))
    except oc.Stop as s:
        return {'stop': s.cls, 'condition': (s.detail or {}).get('condition'), 'evaluated': False}
    led = {'base': H, 'files': {}, 'splices': [], 'retained': []}
    try:
        ev = rc.evaluate(repo, Ctx(repo, corpus), H, M, H, led, {}, {'path': 'zz/none'}, list(classes), {}, rd)
    except Exception as exc:
        return {'exception': '%s: %s' % (type(exc).__name__, exc)}
    return {'R11': ev['holds'].get('R11'), 'rd': rd.summary()}


def unclassified(res, path):
    return [x for x in res.get('items', []) if x[0] == 'side-change-unclassified' and x[1] == path]


def side_of(res, path):
    return [x for x in res.get('side', []) if x[0] == path]


# ---- full-path worlds (cli on the synthetic host world) -------------------------------------------------------

def syn_world(config_path, records_extra=None, files_extra=None, edits=None):
    syn = sf.Syn()
    edits = edits if edits is not None else []
    pd = sf.patch_doc(syn.H, edits)
    base = {'patch_sha': sha(pd), 'files': {'syn/patch.json': pd}, 'config_path': config_path}
    c0, p0, s0, f0 = syn.build(base)
    recs = json.loads(f0[p0])['records']
    files = dict(base['files'])
    files.update(files_extra or {})
    v = dict(base, files=files)
    if records_extra is not None:
        v['extra'] = {'records': recs + records_extra(files)}
    c, p, s, f = syn.build(v)
    w = hf.World(syn.repo, syn.H)
    F = hf.freeze(syn.repo, c, p)
    return syn, w, c, p, F


def exec_run(r, syn, w, F, p, M, freeze=True, extra=()):
    X = syn.H
    argv = ['execution', '--config', '%s:%s' % (F, p), '--out', r.out()] + (w.args(F) if freeze else []) + \
        ['--scientific-base', syn.H, '--candidate', X, '--ledger', '%s:syn/patch.json' % F, '--main', M] + list(extra)
    code, res = cli.run(argv, repo=syn.repo, stderr=io.StringIO(), control=w.control(w.checkout()), environ={})
    return code, res or {}


def plan_on(syn, F, p, base, changes=None):
    """M: `base` plus every entry of F's configuration directory (the plan's merge), with `changes` applied."""
    d = p.rsplit('/', 1)[0]
    files = {q: syn.repo.read(F, q) for q in syn.repo.paths(F) if rc.inside(d, q)}
    files.update(changes or {})
    return syn.repo.derive(base, files, parents=[base], subject='M with the plan directory')


def strip_run(res):
    """A result without the run's directory and the record-directory summary, for result comparisons."""
    d = json.loads(json.dumps(res, default=str))
    d.pop('record_directory', None)
    for k in ('out', 'run', 'timing'):
        d.pop(k, None)
    return util.canonical(d)


def without_rule(fn):
    """fn() with the M role's record-directory context disabled (the tool without this amendment)."""
    orig = exmod.Execution._record_directory
    exmod.Execution._record_directory = lambda self, lc: None
    try:
        return fn()
    finally:
        exmod.Execution._record_directory = orig


# ---- the O-9 controls -----------------------------------------------------------------------------------------

def o9_controls(r, check):
    names = sorted(plan_files())

    # O9-1
    repo, H, F, M = world()
    res = run_main(repo, H, F, M)
    check('O9-1', 'every entry of D at M equal to F: each record-directory; A.5 no unequal path; no '
          'side-change-unclassified', 'each D path classified record-directory; rd.unequal empty; no unclassified item',
          res, all(side_of(res, p) == [(p, 'record-directory', None)] for p in names) and
          (res.get('rd') or {}).get('unequal') == {} and not [x for x in res.get('items', [])
                                                              if x[0] == 'side-change-unclassified'])

    # O9-2
    mod = AUTH + '/review.json'
    repo, H, F, M = world({mod: b'{"synthetic": "review", "changed": true}\n'})
    res = run_main(repo, H, F, M)
    check('O9-2', 'one file in D modified on M after F: that file side-change-unclassified (differs from F); the others '
          'record-directory', 'the modified file unclassified "differs from F"; the other three record-directory',
          res, unclassified(res, mod) == [('side-change-unclassified', mod, 'differs from F')] and
          all(side_of(res, p) == [(p, 'record-directory', None)] for p in names if p != mod))

    # O9-3
    add = AUTH + '/added.json'
    repo, H, F, M = world(m_extra={add: b'{}\n'})
    res = run_main(repo, H, F, M)
    check('O9-3', 'a file added in D on M, absent at F: side-change-unclassified (absent at F)',
          'the added file unclassified "absent at F"', res,
          unclassified(res, add) == [('side-change-unclassified', add, 'absent at F')])

    # O9-4
    dele = AUTH + '/ledger.json'
    repo, H, F, M = world({dele: None})
    res = run_main(repo, H, F, M)
    scan_lists = bool(side_of(res, dele))
    check('O9-4', 'a file of F in D deleted on M (absent at H and M): side-change-unclassified (absent at M), reported '
          'by A.5 although the H-to-M scan does not list it', 'an unclassified item "absent at M" for the deleted path, '
          'and no side-change entry for it from the scan', res,
          unclassified(res, dele) == [('side-change-unclassified', dele, 'absent at M')] and not scan_lists)

    # O9-5
    out_p = 'notes/same.txt'
    repo, H, F, M = world(f_extra={out_p: b'same\n'}, m_extra={out_p: b'same\n'})
    res = run_main(repo, H, F, M)
    check('O9-5', 'a path outside D whose blob at M equals its blob at F: side-change-unclassified (outside the record '
          'directory)', 'unclassified "outside the record directory"', res,
          unclassified(res, out_p) == [('side-change-unclassified', out_p, 'outside the record directory')])

    # O9-6
    sib = AUTH + '-x/f.json'
    repo, H, F, M = world(f_extra={sib: b'{}\n'}, m_extra={sib: b'{}\n'})
    res = run_main(repo, H, F, M)
    check('O9-6', 'a sibling path D-x/f sharing D as a string prefix, equal at F and M: side-change-unclassified',
          'the sibling path unclassified (outside the record directory); not record-directory', res,
          unclassified(res, sib) == [('side-change-unclassified', sib, 'outside the record directory')] and
          not [x for x in side_of(res, sib) if x[1] == 'record-directory'])

    # O9-7
    bad = [AUTH + '/./x', AUTH + '/../x', AUTH + '//x', AUTH + '/x/..', AUTH + '/']
    good = [AUTH + '/x', AUTH + '/a/b.json']
    got = {p: rc.clean_path(p) for p in bad + good}
    check('O9-7', 'the clean-path predicate applied to paths with a ., .. or empty component: each refused (tested on the '
          'predicate)', 'clean_path false for each bad path, true for each good path', got,
          not any(got[p] for p in bad) and all(got[p] for p in good))

    # O9-8: mode change, symbolic link, submodule; through the M role and through R11
    o8 = {}
    m_p, l_p, s_p = AUTH + '/mode.sh', AUTH + '/link', AUTH + '/sub'
    base_repo, H, F, M = world(f_extra={m_p: b'#!/bin/sh\n', l_p: b'target bytes\n', s_p: b'regular\n'},
                               m_change={l_p: ('symlink', 'target bytes\n'), s_p: ('submodule', '1' * 40)},
                               m_extra={m_p: b'#!/bin/sh\n'})
    repo = ModeOverlay(base_repo, [(M, m_p)])
    res = run_main(repo, H, F, M)
    o8['M role'] = {k: res.get(k) for k in ('items', 'exception', 'stop')}
    o8['R11'] = r11(repo, H, F, M)
    want = {m_p: 'differs from F', l_p: 'not a regular file', s_p: 'not a regular file'}
    check('O9-8', 'in D: a mode change; a symbolic link at M where F has a regular file of the same bytes; a submodule '
          'at M; through the M role and through R11: each side-change-unclassified with its reason; R11 fails; no '
          'exception', 'each path unclassified with its reason in the M role; R11 false; no exception, no stop', o8,
          'exception' not in res and 'stop' not in res and
          all(unclassified(res, p) == [('side-change-unclassified', p, w)] for p, w in want.items()) and
          o8['R11'].get('R11') is False and 'exception' not in o8['R11'])

    # O9-9: a ledgered path, and separately a corpus path, inside D
    lp = AUTH + '/ledger.json'
    repo, H, F, M = world()
    a = run_main(repo, H, F, M, ledgered=[lp])
    b = run_main(repo, H, F, M, corpus=[lp])
    check('O9-9', 'a ledgered path, and separately a corpus path, inside D: ERROR CONFIG_INCONSISTENT (D3)',
          'both runs stop CONFIG_INCONSISTENT with condition D3', {'ledgered': a, 'corpus': b},
          all(x.get('stop') == 'CONFIG_INCONSISTENT' and x.get('condition') == 'D3' for x in (a, b)))

    # O9-10: a configuration in the root directory
    repo = Overlay(None)
    H = repo.add_commit({'doc/a.md': b'base\n'}, [], 'H')
    F = repo.derive(H, {'retirement-config.json': b'{}\n', 'PREREG.md': b'# p\n'}, parents=[H], subject='F')
    M = repo.derive(H, {'retirement-config.json': b'{}\n', 'PREREG.md': b'# p\n'}, parents=[H], subject='M')
    res = run_main(repo, H, F, M, cpath='retirement-config.json')
    check('O9-10', 'a configuration in the root directory: ERROR CONFIG_INCONSISTENT (authority)',
          'the run stops CONFIG_INCONSISTENT with condition authority', res,
          res.get('stop') == 'CONFIG_INCONSISTENT' and res.get('condition') == 'authority')

    # O9-11
    repo, H, F, M = world(h_extra={AUTH + '/old.txt': b'old\n'})
    res = run_main(repo, H, F, M)
    check('O9-11', 'a path inside D that exists at H: ERROR CONFIG_INCONSISTENT (D2)', 'stop CONFIG_INCONSISTENT, D2',
          res, res.get('stop') == 'CONFIG_INCONSISTENT' and res.get('condition') == 'D2')

    # O9-12: a class prefix inside the authorized D
    sub = AUTH + '/sub/f.json'
    repo, H, F, M = world(f_extra={sub: b'{}\n'}, m_extra={sub: b'{}\n'})
    cls = [{'id': 'c', 'prefixes': [AUTH + '/sub/'], 'pins': []}]
    res = run_main(repo, H, F, M, classes=cls)
    check('O9-12', 'the authorized D, with a side-change class whose prefix lies inside D: ERROR CONFIG_INCONSISTENT '
          '(D3)', 'stop CONFIG_INCONSISTENT, D3', res,
          res.get('stop') == 'CONFIG_INCONSISTENT' and res.get('condition') == 'D3')

    # O9-12b: a configuration under .github/, (a) present at H, (b) absent at H
    gd = '.github/plan'
    repo, H, F, M = world(d=gd, h_extra={gd + '/existing.txt': b'x\n'})
    a = run_main(repo, H, F, M, cpath=gd + '/retirement-config.json')
    a0 = run_main(repo, H, F, M, cpath=gd + '/retirement-config.json', rule=False)
    repo, H, F, M = world(d=gd)
    b = run_main(repo, H, F, M, cpath=gd + '/retirement-config.json')
    check('O9-12b', 'a configuration under .github/ with an entry inside it on M: (a) present at H: the rule inactive, no '
          'record-directory, the result equal to the run without this amendment; (b) absent at H: ERROR '
          'CONFIG_INCONSISTENT (authority)', '(a) items and side changes equal to the run without the rule, state '
          'inactive; (b) stop CONFIG_INCONSISTENT, authority', {'a': a, 'a_without': a0, 'b': b},
          a.get('items') == a0.get('items') and a.get('side') == a0.get('side') and
          not [x for x in a.get('side', []) if x[1] == 'record-directory'] and
          (a.get('rd') or {}).get('state', '').startswith('inactive') and
          b.get('stop') == 'CONFIG_INCONSISTENT' and b.get('condition') == 'authority')

    # O9-13: a class pin naming a D path, differing from M
    p13 = AUTH + '/review.json'
    repo, H, F, M = world()
    cls = [{'id': 'pinned', 'pins': [{'path': p13, 'git_blob': None, 'blob_sha256': '0' * 64}]}]
    res = run_main(repo, H, F, M, classes=cls)
    check('O9-13', 'a path in D, equal at F and M, that a class names with a pin differing from M: '
          'side-change-unclassified naming the class; not record-directory',
          'unclassified with the class-pin reason naming class pinned', res,
          unclassified(res, p13) == [('side-change-unclassified', p13,
                                      'the blob at M differs from the pin of class pinned')] and
          not [x for x in side_of(res, p13) if x[1] == 'record-directory'])

    # O9-14: no --freeze (full path, control harness)
    syn, w, c, p, F = syn_world(CFG)
    M = plan_on(syn, F, p, syn.H)
    argv = ['execution', '--config', '%s:%s' % (F, p), '--out', r.out(), '--scientific-base', syn.H, '--candidate',
            syn.H, '--ledger', '%s:syn/patch.json' % F, '--main', M]
    code, res = cli.run(argv, repo=syn.repo, harness=True, stderr=io.StringIO())
    res = res or {}
    dpaths = [e for e in res.get('side_changes', []) if rc.inside(AUTH, e['path'])]
    check('O9-14', 'no --freeze: the rule inactive; files in D side-change-unclassified; A.5 not evaluated',
          'no record_directory in the result; every D side change unclassified', {'exit': code, 'side': dpaths,
                                                                                 'rd': res.get('record_directory')},
          'record_directory' not in res and dpaths and all(e['class'] is None for e in dpaths))

    # O9-15, O9-18, O9-19: R11
    repo, H, F, M = world()
    a = r11(repo, H, F, M)
    repo, H, F, M = world({AUTH + '/review.json': b'{"changed": 1}\n'})
    b = r11(repo, H, F, M)
    repo, H, F, M = world({AUTH + '/ledger.json': None})
    c_ = r11(repo, H, F, M)
    check('O9-15', 'a reconciliation record, M with D equal to F: R11 holds', 'R11 true', a, a.get('R11') is True)
    check('O9-18', 'a reconciliation record, M with one file of D modified after F: R11 fails', 'R11 false', b,
          b.get('R11') is False)
    check('O9-19', 'a reconciliation record, M with one file of F\'s D deleted: R11 fails (A.5)', 'R11 false', c_,
          c_.get('R11') is False)

    # O9-16: a configuration in a newly introduced, unrelated directory (full path, the tool's constant)
    other = 'syn2/new/plan/r1/retirement-config.json'
    syn, w, c, p, F = syn_world(other)
    M = plan_on(syn, F, p, syn.H)
    code, res = exec_run(r, syn, w, F, p, M)
    check('O9-16', 'a configuration in a newly introduced, unrelated directory (absent at H, holding the configuration '
          'and a file of record pins, no ledgered, corpus, class or .github/ path): ERROR CONFIG_INCONSISTENT '
          '(authority)', 'exit 65, stop CONFIG_INCONSISTENT, condition authority',
          {'exit': code, 'stop': res.get('stop')}, code == 65 and (res.get('stop') or {}).get('class') ==
          'CONFIG_INCONSISTENT' and ((res.get('stop') or {}).get('detail') or {}).get('condition') == 'authority')

    # O9-17, O9-24: the reserved class id; O9-24 through --classify (full path)
    repo, H, F, M = world()
    res = run_main(repo, H, F, M, classes=[{'id': rc.RECORD_DIRECTORY, 'pins': []}])
    check('O9-17', 'a class record defining class id record-directory: ERROR CONFIG_INCONSISTENT (D5)',
          'stop CONFIG_INCONSISTENT, D5', res, res.get('stop') == 'CONFIG_INCONSISTENT' and res.get('condition') == 'D5')
    cls_doc = {'schema': 'oi-side-change-classes/1', 'record_id': 'reserved', 'author': sf.WRITER, 'supersedes': None,
               'classes': [{'id': rc.RECORD_DIRECTORY, 'prefixes': ['notes/'], 'reason': 'synthetic', 'pins': []}]}
    cp = 'syn/reserved-classes.json'

    def extra_cls(files):
        files[cp] = sf.jb(cls_doc)
        return [{'kind': 'classification', 'path': cp, 'blob_sha256': sha(files[cp])}] + \
            syn_.chain(files, cp, sf.REVIEWER)
    syn_ = sf.Syn()
    pd = sf.patch_doc(syn_.H, [])
    base = {'patch_sha': sha(pd), 'files': {'syn/patch.json': pd}, 'config_path': CFG}
    c0, p0, s0, f0 = syn_.build(base)
    files = dict(base['files'])
    recs = json.loads(f0[p0])['records'] + extra_cls(files)
    c1, p1, s1, f1 = syn_.build(dict(base, files=files, extra={'records': recs}))
    w1 = hf.World(syn_.repo, syn_.H)
    F1 = hf.freeze(syn_.repo, c1, p1)
    M1 = plan_on(syn_, F1, p1, syn_.H)
    code, res = exec_run(r, syn_, w1, F1, p1, M1, extra=['--classify', '%s:%s' % (F1, cp)])
    check('O9-24', 'a class record admitted through --classify that defines the class id record-directory: ERROR '
          'CONFIG_INCONSISTENT (D5)', 'exit 65, stop CONFIG_INCONSISTENT, condition D5',
          {'exit': code, 'stop': res.get('stop')}, code == 65 and (res.get('stop') or {}).get('class') ==
          'CONFIG_INCONSISTENT' and ((res.get('stop') or {}).get('detail') or {}).get('condition') == 'D5')

    # O9-20: R11 with an unauthorized D: ERROR before R11 is evaluated
    calls = []
    orig = rc.evaluate

    def spy(*a, **k):
        calls.append(1)
        return orig(*a, **k)
    ud = 'unauth/plan/dir'
    repo, H, F, M = world(d=ud)
    rc.evaluate = spy
    try:
        led = {'base': H, 'files': {'doc/a.md': {}}, 'splices': [], 'retained': []}
        M2 = repo.derive(M, {'doc/a.md': b'drift\n'}, parents=[M], subject='M drift')
        recon = [{'paths': [{'path': 'doc/a.md'}], '_ref': {'path': 'x', 'blob_sha256': '0' * 64}}]
        ex = exmod.Execution(Ctx(repo), H, H, led, None, M2, None, None, [], recon)
        ex.record_refs = {}
        ex.record_dir_args = {'F': F, 'cpath': ud + '/retirement-config.json', 'authorized': (AUTH,)}
        try:
            ex.main_role({'doc/a.md'})
            got = {'stop': None}
        except oc.Stop as s:
            got = {'stop': s.cls, 'condition': (s.detail or {}).get('condition')}
    finally:
        rc.evaluate = orig
    got['evaluations'] = len(calls)
    check('O9-20', 'a reconciliation record, M with a file of D equal to F, but D not authorized: ERROR '
          'CONFIG_INCONSISTENT (authority) before R11 is evaluated', 'stop CONFIG_INCONSISTENT, authority; no call of '
          'reconcile.evaluate', got, got.get('stop') == 'CONFIG_INCONSISTENT' and got.get('condition') == 'authority'
          and got['evaluations'] == 0)

    # O9-21: a class pin that matches M, on a file that differs between F and M
    p21 = AUTH + '/review.json'
    new = b'{"changed on M": true}\n'
    repo, H, F, M = world({p21: new})
    cls = [{'id': 'matching', 'pins': [{'path': p21, 'git_blob': repo.blob_id(M, p21), 'blob_sha256': sha(new)}]}]
    res = run_main(repo, H, F, M, classes=cls)
    check('O9-21', 'a file in D that differs between F and M, and a class pin naming it that matches M: the class '
          'route\'s entry stands and A.5 issues side-change-unclassified (differs from F); not accepting',
          'side-change entry class matching; an unclassified item "differs from F"', res,
          side_of(res, p21) == [(p21, 'matching', None)] and
          unclassified(res, p21) == [('side-change-unclassified', p21, 'differs from F')])

    # O9-22: an unauthorized D with no entry on M (full path), compared with the tool without the rule
    syn, w, c, p, F = syn_world('syn/cfg/config.json')
    M = syn.repo.derive(syn.H, {'notes/m.txt': b'main\n'}, parents=[syn.H], subject='M')
    with_r = exec_run(r, syn, w, F, p, M)
    without = without_rule(lambda: exec_run(r, syn, w, F, p, M))
    check('O9-22', 'an unauthorized D with no entry inside it on M, under execution --main --freeze: no ERROR; side '
          'changes classified exactly as without this amendment', 'no stop; record_directory state inactive; result '
          'equal to the run without the rule', {'exit': with_r[0], 'rd': with_r[1].get('record_directory'),
                                               'exit_without': without[0]},
          not with_r[1].get('stop') and with_r[0] == without[0] and
          strip_run(with_r[1]) == strip_run(without[1]) and
          (with_r[1].get('record_directory') or {}).get('state', '').startswith('inactive'))

    # O9-23: the authorized D under coverage (no M): A.3-A.5 never evaluated
    built = []
    orig_rd = rc.RecordDirectory

    class Trap(orig_rd):
        def __init__(self, *a, **k):
            built.append(1)
            orig_rd.__init__(self, *a, **k)
    syn, w, c, p, F = syn_world(CFG)
    argv = ['coverage', '--config', '%s:%s' % (F, p), '--out', r.out()] + w.args(F) + ['--commit', syn.H]
    rc.RecordDirectory = Trap
    try:
        code, res = cli.run(argv, repo=syn.repo, stderr=io.StringIO(), control=w.control(w.checkout()), environ={})
    finally:
        rc.RecordDirectory = orig_rd
    res = res or {}
    check('O9-23', 'the authorized D and a configuration whose run is coverage (no M): no evaluation of A.3-A.5',
          'no RecordDirectory built; no record_directory in the result; no stop', {'exit': code, 'built': len(built),
                                                                                 'stop': res.get('stop')},
          not built and 'record_directory' not in res and not res.get('stop'))

    # O9-25: the synthetic world of the conformance controls: an unauthorized D (syn) present at H, entries on M
    syn, w, c, p, F = syn_world('syn/config.json')
    M = syn.repo.derive(syn.H, {'notes/m.txt': b'main\n'}, parents=[syn.H], subject='M')
    present_h = any(rc.inside('syn', q) for q in syn.repo.entries(syn.H))
    on_m = any(rc.inside('syn', q) for q in syn.repo.entries(M))
    with_r = exec_run(r, syn, w, F, p, M)
    without = without_rule(lambda: exec_run(r, syn, w, F, p, M))
    check('O9-25', 'the synthetic world: an unauthorized D (syn) present at H, with entries inside it on M, under '
          'execution --main --freeze: no ERROR; the rule inactive; side changes, items and outcome equal to the same '
          'run without this amendment (the existing conformance controls are checked by their own results)',
          'D present at H and on M; no stop; state inactive; result equal to the run without the rule',
          {'present_at_H': present_h, 'on_M': on_m, 'exit': with_r[0], 'rd': with_r[1].get('record_directory'),
           'exit_without': without[0]},
          present_h and on_m and not with_r[1].get('stop') and with_r[0] == without[0] and
          strip_run(with_r[1]) == strip_run(without[1]) and
          (with_r[1].get('record_directory') or {}).get('state') == 'inactive: unauthorized, present at H')


# ---- the item-2 controls --------------------------------------------------------------------------------------

def arm_text(workflow_path):
    with open(workflow_path, encoding='utf-8') as f:
        for line in f:
            if line.strip().startswith('item2-coverage)'):
                return line.strip()
    return None


EXPECTED_ARM = ('item2-coverage) exec python3 -I -S -B tools/ledger_coverage.py coverage "$@" --commit "$X" '
                '--segment "$E..$H" --segment "$H..$X=$F:$D/ledger.json" --hp "$F:$D/hp.json" '
                '--classify "$F:$A/records/gr58-hit-classification-v1.json" '
                '--classify "$F:$D/context-adjudications.json" --classify "$F:$D/hit-classifications.json" ;;')


def arm_classify(arm):
    """The --classify operands of the arm, with $F and $D unresolved."""
    return re.findall(r'--classify "([^"]+)"', arm or '')


def i2_world(ctx_doc, hit_doc, reference=True, review=True, drop=()):
    """The synthetic world with the plan directory's two item-2 records, referenced by the configuration and
    reviewed (each as the flags say); `drop` names records absent from F."""
    d = 'syn/plan'
    cpath = d + '/retirement-config.json'
    names = {'context': d + '/context-adjudications.json', 'hits': d + '/hit-classifications.json'}

    def extra(files):
        out = []
        for k, doc in (('context', ctx_doc), ('hits', hit_doc)):
            if k in drop:
                continue
            files[names[k]] = sf.jb(doc)
            if reference:
                out.append({'kind': 'record', 'path': names[k], 'blob_sha256': sha(files[names[k]])})
            if review:
                out += syn.chain(files, names[k], sf.REVIEWER)
        return out
    syn = sf.Syn()
    pd = sf.patch_doc(syn.H, [])
    base = {'patch_sha': sha(pd), 'files': {'syn/patch.json': pd}, 'config_path': cpath}
    c0, p0, s0, f0 = syn.build(base)
    files = dict(base['files'])
    recs = json.loads(f0[p0])['records'] + extra(files)
    if not reference:
        recs = json.loads(f0[p0])['records']
    c, p, s, f = syn.build(dict(base, files=files, extra={'records': recs}))
    for k in drop:
        files.pop(names[k], None)
    w = hf.World(syn.repo, syn.H)
    F = hf.freeze(syn.repo, c, p)
    if drop:
        F = syn.repo.derive(F, {names[k]: None for k in drop}, parents=syn.repo.parents(F), subject='F without')
    return syn, w, F, p, d, names


def coverage_via_arm(r, syn, w, F, p, d, arm):
    """The coverage operation with the --classify operands of the workflow arm, $F and $D resolved; returns
    (exit, result, the context and hit records the pipeline received)."""
    got = {}
    orig_cov, orig_terms = pl.Coverage, pl.Terms

    class Cov(orig_cov):
        def __init__(self, ctx, commit, segs, chk, adj, hits, *a, **k):
            got['context'] = list((adj or {}).get('context', []))
            got['hits'] = list(hits or [])
            orig_cov.__init__(self, ctx, commit, segs, chk, adj, hits, *a, **k)
    ops = []
    for op in arm_classify(arm):
        if '$A/' in op:
            continue
        ops += ['--classify', op.replace('$F', F).replace('$D', d)]
    argv = ['coverage', '--config', '%s:%s' % (F, p), '--out', r.out()] + w.args(F) + ['--commit', syn.H] + ops
    pl.Coverage = Cov
    try:
        code, res = cli.run(argv, repo=syn.repo, stderr=io.StringIO(), control=w.control(w.checkout()), environ={})
    finally:
        pl.Coverage, pl.Terms = orig_cov, orig_terms
    return code, res or {}, got


def ctx_doc_of(entries, rid='ctx-adj'):
    return {'schema': 'oi-context-adjudication/1', 'record_id': rid, 'author': sf.WRITER, 'supersedes': None,
            'entries': entries}


def hit_doc_of(cls, rid='hit-cls'):
    return {'schema': 'oi-hit-classification/1', 'record_id': rid, 'author': sf.WRITER, 'supersedes': None,
            'classifications': cls}


def i2_controls(r, check, workflow_path):
    arm = arm_text(workflow_path)
    check('I2-1', 'the item2-coverage arm: exactly the existing arguments followed by the two --classify arguments of '
          'B.2, every expansion quoted', 'the arm line equals the expected text', arm, arm == EXPECTED_ARM)

    # I2-2: a meaning-context adjudication through context-adjudications.json resolves its site (as K10)
    w = ce.World(sites=[(3, 'sd'), (7, 'sr')])
    x = w.child(w.pin, ce.base_text.replace('beta line two stands here.', 'beta line two does not stand.'))
    sd = '%s:3@%s' % (ce.doc_path, w.pin[:8])
    cv, it = w.coverage(x, [ce.seg(w.pin, x)], hits=False)
    sg0 = cv.segments[0]
    entry = {'id': 'c1', 'site_id': sd, 'segment': sg0['name'], 'from_context_sha256': sg0['ctx_from'][sd][0],
             'to_context_sha256': util.context_hash_block(w.ctx().ft(x, ce.doc_path).lines, 2, 3),
             'statement': 'the qualification is still stated', 'author': sf.WRITER}
    syn, sw, F, p, d, names = i2_world(ctx_doc_of([entry]), hit_doc_of([]))
    code, res, got = coverage_via_arm(r, syn, sw, F, p, d, arm)
    routed = [e for e in got.get('context', []) if e.get('id') == 'c1']
    cv10, it10 = w.coverage(x, [ce.seg(w.pin, x)], adj={'context': routed}, hits=False)
    check('I2-2', 'a meaning-context adjudication supplied through context-adjudications.json, matching both context '
          'hashes of a meaning-context site: that site PASS (sec. 4.1 row 2), as K10',
          'the adjudication reaches the context collection through the arm\'s --classify; with it the site has no '
          'item, without it context-meaning-unverified', {'exit': code, 'stop': res.get('stop'), 'routed': routed,
                                                         'without': ce.classes([i for i in it if i['subject'] == sd]),
                                                         'with': [i['class'] for i in it10 if i['subject'] == sd]},
          not res.get('stop') and routed == [entry] and
          [i['class'] for i in it if i['subject'] == sd] == ['context-meaning-unverified'] and
          not [i for i in it10 if i['subject'] == sd])

    # I2-3: context-adjudications.json absent at F
    syn, sw, F, p, d, names = i2_world(ctx_doc_of([]), hit_doc_of([]), drop=('context',))
    code, res, got = coverage_via_arm(r, syn, sw, F, p, d, arm)
    check('I2-3', 'context-adjudications.json absent at F: ERROR SOURCE_CHANGED', 'exit 65, stop SOURCE_CHANGED',
          {'exit': code, 'stop': res.get('stop')}, code == 65 and (res.get('stop') or {}).get('class') ==
          'SOURCE_CHANGED')

    # I2-4: hit-classifications.json not referenced by the configuration
    syn, sw, F, p, d, names = i2_world(ctx_doc_of([]), hit_doc_of([]), reference=False, review=False)
    code, res, got = coverage_via_arm(r, syn, sw, F, p, d, arm)
    inv = sorted(i['subject'] for i in res.get('items', []) if i['class'] == 'record-invalid')
    check('I2-4', 'hit-classifications.json present but not referenced by the configuration: record-invalid; the hit '
          'stays REVIEW_REQUIRED', 'record-invalid names the file; no hit record reaches the pipeline',
          {'exit': code, 'record_invalid': inv, 'hits': got.get('hits')},
          names['hits'] in inv and not got.get('hits'))

    # I2-5: a referenced record without a valid review
    syn, sw, F, p, d, names = i2_world(ctx_doc_of([]), hit_doc_of([]), review=False)
    code, res, got = coverage_via_arm(r, syn, sw, F, p, d, arm)
    inv = sorted(i['subject'] for i in res.get('items', []) if i['class'] == 'record-invalid')
    check('I2-5', 'a referenced record without a valid review: record-invalid', 'record-invalid names both files',
          {'exit': code, 'record_invalid': inv}, names['hits'] in inv and names['context'] in inv)

    # I2-6: an empty entries list with its record_id and review; without record_id, or without review, invalid
    syn, sw, F, p, d, names = i2_world(ctx_doc_of([]), hit_doc_of([]))
    code, res, got = coverage_via_arm(r, syn, sw, F, p, d, arm)
    ok = not [i for i in res.get('items', []) if i['class'] == 'record-invalid'] and not res.get('stop')
    nid = ctx_doc_of([])
    nid.pop('record_id')
    syn2, sw2, F2, p2, d2, n2 = i2_world(nid, hit_doc_of([]))
    code2, res2, got2 = coverage_via_arm(r, syn2, sw2, F2, p2, d2, arm)
    syn3, sw3, F3, p3, d3, n3 = i2_world(ctx_doc_of([]), hit_doc_of([]), review=False)
    code3, res3, got3 = coverage_via_arm(r, syn3, sw3, F3, p3, d3, arm)
    inv2 = [i['subject'] for i in res2.get('items', []) if i['class'] == 'record-invalid']
    inv3 = [i['subject'] for i in res3.get('items', []) if i['class'] == 'record-invalid']
    check('I2-6', 'an empty entries list with its record_id, referenced, with a valid review bound to that record_id: '
          'admitted, no site resolved; the same file without record_id, or without a review, record-invalid',
          'no record-invalid for the empty reviewed file; record-invalid for the file without record_id and for the '
          'unreviewed file', {'exit': code, 'admitted': ok, 'no_record_id': inv2, 'no_review': inv3,
                              'stops': [res.get('stop'), res2.get('stop'), res3.get('stop')]},
          ok and got.get('context') == [] and n2['context'] in inv2 and n3['context'] in inv3)

    # I2-7: a hit classification through hit-classifications.json resolves a hit outside any HP region
    wz = ce.World(text=ce.base_text.replace('delta line four stands here.', 'delta line four names zeta here.'))
    ctx = wz.ctx()
    line = 'delta line four names zeta here.'
    tm0 = pl.Terms(ctx, wz.pin, [ctx.profiles['np-review']], [], hit_records=())
    tm0.review(held={})
    hit = {'id': 'h1', 'file': ce.doc_path, 'line_sha256': sha(line.encode()), 'segment': None,
           'profiles': ['np-review'], 'semantic_classification': 'unrelated use', 'author': sf.WRITER}
    syn, sw, F, p, d, names = i2_world(ctx_doc_of([]), hit_doc_of([hit]))
    code, res, got = coverage_via_arm(r, syn, sw, F, p, d, arm)
    routed = [h for h in got.get('hits', []) if h.get('id') == 'h1']
    rec_ = [dict({k: v for k, v in h.items() if k != '_ref'}) for h in routed]
    tm1 = pl.Terms(ctx, wz.pin, [ctx.profiles['np-review']], [], hit_records=rec_)
    tm1.review(held={})
    s0 = [h['state'] for h in tm0.hits if h['line_sha256'] == hit['line_sha256']]
    s1 = [h['state'] for h in tm1.hits if h['line_sha256'] == hit['line_sha256']]
    check('I2-7', 'a hit classification supplied through hit-classifications.json, matching a hit outside any HP region '
          'by its line sha256: that hit resolved as the classification states; without the record, REVIEW_REQUIRED',
          'the record reaches the hit collection through the arm\'s --classify; the hit is not PASS without it and '
          'PASS with it', {'exit': code, 'routed': len(routed), 'without': s0, 'with': s1},
          not res.get('stop') and len(routed) == 1 and s0 and s0[0] != 'PASS' and s1 == ['PASS'])

    # I2-8: an indicator adjudication through context-adjudications.json resolves a structure item
    lt = '# h\n\nlead-in sentence:\n\n- item one here\n- item two here\n\ntrailer paragraph.\n'
    w6 = ce.World(lt, sites=[(5, 'sr')])
    x6 = w6.child(w6.pin, lt.replace('lead-in sentence:', 'lead-in changed:'))
    cv6, it6 = w6.coverage(x6, [ce.seg(w6.pin, x6)], hits=False)
    s6 = '%s:5@%s' % (ce.doc_path, w6.pin[:8])
    seg6 = cv6.segments[0]
    out6 = cv6.site_out[s6]
    st6 = [s for s in cv6.states if s.site['site_id'] == s6][0]
    lt6 = w6.ctx().ft(x6, ce.doc_path).lines
    from_ctx6, from_struct6 = seg6['ctx_from'][s6]
    to_ctx6 = util.context_hash_block(lt6, st6.start, st6.start + len(st6.block))
    to_struct6 = w6.ctx().indicators.structure(set(st6.site['effects']), lt6, st6.start)
    entry6 = {'id': 'i1', 'site_id': s6, 'segment': seg6['name'], 'from_context_sha256': from_ctx6,
              'to_context_sha256': to_ctx6, 'from_structure_sha256': from_struct6,
              'to_structure_sha256': to_struct6, 'statement': 'the list still states the qualification',
              'author': sf.WRITER}
    syn, sw, F, p, d, names = i2_world(ctx_doc_of([entry6]), hit_doc_of([]))
    code, res, got = coverage_via_arm(r, syn, sw, F, p, d, arm)
    routed = [e for e in got.get('context', []) if e.get('id') == 'i1']
    cv6b, it6b = w6.coverage(x6, [ce.seg(w6.pin, x6)], adj={'context': routed}, hits=False)
    check('I2-8', 'an indicator adjudication supplied through context-adjudications.json, matching both context hashes and '
          'both structure hashes of a LIST or TABLE site: the context-structure-changed item resolved; without it '
          'REVIEW_REQUIRED context-structure-changed', 'the adjudication reaches the context collection through the '
          'arm; without it context-structure-changed, with it no item on the site',
          {'exit': code, 'routed': routed, 'without': ce.classes(it6), 'with': ce.classes(it6b), 'site': out6},
          not res.get('stop') and routed == [entry6] and ce.classes(it6) == ['context-structure-changed'] and
          not [i for i in it6b if i['subject'] == s6])


IDS = ['O9-1', 'O9-2', 'O9-3', 'O9-4', 'O9-5', 'O9-6', 'O9-7', 'O9-8', 'O9-9', 'O9-10', 'O9-11', 'O9-12', 'O9-12b',
       'O9-13', 'O9-14', 'O9-15', 'O9-16', 'O9-17', 'O9-18', 'O9-19', 'O9-20', 'O9-21', 'O9-22', 'O9-23', 'O9-24',
       'O9-25', 'I2-1', 'I2-2', 'I2-3', 'I2-4', 'I2-5', 'I2-6', 'I2-7', 'I2-8']
