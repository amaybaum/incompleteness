"""Preregistered controls of design amendment r4: the record-directory rule (RDIR-1 to RDIR-25, RDIR-12b; A.9) and the
item-2 record interfaces (I2-1 to I2-8; B.4). Run by conformance_controls.py; each control records its id, its
expectation, its predicate and what it found.

Engine-level cases build their repositories in memory and call the M role (`Execution.main_role`), the RC11 condition
(`reconcile.evaluate`) or the context (`reconcile.RecordDirectory`) directly; the cases marked "full path" run the
`execution` or `coverage` operation through `cli.run` on the synthetic host world, with the tool's own authority
constant (`record_authority.authorized_record_directories`).
"""
import io
import json
import re
from functools import partial

from ledger_coverage import record_authority
from ledger_coverage.engine import cli, execution as exmod, outcome as oc, pipeline as pl, reconcile as rc, util
from ledger_coverage.engine import controls_engine as ce
from ledger_coverage.engine.gitobj import Overlay
from ledger_coverage.adapters import control_records, host_fixture as hf, synthetic_fixture as sf

AUTH = record_authority.authorized_record_directories[0]
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


def run_main(repo, H, F, M, cpath=CFG, classes=(), authorized=(AUTH,), ledgered=(), corpus=(), rule=True,
             recorder=None):
    """The M role (Execution.main_role) over H..M, with the record-directory rule when `rule`."""
    led = {'base': H, 'files': {p: {} for p in ledgered}, 'splices': [], 'retained': []}
    ex = exmod.Execution(Ctx(repo, corpus), H, H, led, None, M, None, None, list(classes), ())
    ex.record_refs = {}
    if rule:
        ex.record_dir_args = {'freeze': F, 'cpath': cpath, 'authorized': tuple(authorized)}
    try:
        ex.main_role(set(ledgered) | set(corpus))
    except oc.Stop as s:
        if recorder is not None:
            doc = control_records.stage_doc(ex.items, operation='execution.main_role', stop=s)
            recorder.capture_doc('execution.main_role', doc)
        return {'stop': s.cls, 'condition': (s.detail or {}).get('condition'), 'message': s.message}
    except Exception as exc:  # recorded, so that a control can require its absence
        return {'exception': '%s: %s' % (type(exc).__name__, exc)}
    summary = ex.rd.summary() if ex.rd else None
    if recorder is not None:
        doc = control_records.stage_doc(ex.items, operation='execution.main_role',
                                        record_directory=summary, side_changes=ex.side_changes,
                                        inputs={'H': H, 'F': F, 'M': M, 'config_path': cpath})
        recorder.capture_doc('execution.main_role', doc)
    return {'items': sorted((i['class'], i['subject'], i.get('why')) for i in ex.items),
            'side': sorted((e['path'], e['class'], e.get('why')) for e in ex.side_changes),
            'rd': summary, 'entries': ex.side_changes}


def r11(repo, H, F, M, cpath=CFG, classes=(), authorized=(AUTH,), ledgered=(), corpus=()):
    """RC11 of a reconciliation record whose own path is outside the world, evaluated with the run's context."""
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
    return {'RC11': ev['holds'].get('RC11'), 'rd': rd.summary()}


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


def o98_run(r, case):
    """RDIR-8, one case: the synthetic host world with the configuration in the authorized directory and a reconciliation
    record for the corpus file (referenced by the configuration and reviewed); M = H plus the plan directory as F holds
    it, with the case's change, plus a change of the corpus file, so that the M role evaluates the record's RC11. Runs
    `execution --main` through cli.run. case None: the baseline, D equal to F."""
    path = AUTH + {'mode': '/mode.sh', 'symlink': '/link', 'submodule': '/sub', None: '/mode.sh'}[case]
    syn = sf.Syn()
    pd = sf.patch_doc(syn.H, [])
    rec_doc = {'schema': 'oi-reconciliation/1', 'record_id': 'o98-recon', 'author': sf.WRITER, 'supersedes': None,
               'ledger_binding': {}, 'changes_decisions_on_X': [],
               'paths': [{'id': 'doc', 'path': sf.DOC, 'side_change_commits': [], 'splices': [], 'protected': []}]}
    files = {'syn/patch.json': pd, path: b'#!/bin/sh\ntarget bytes\n'}
    files['syn/o98-recon.json'] = sf.jb(rec_doc)
    base = {'patch_sha': sha(pd), 'files': {'syn/patch.json': pd}, 'config_path': CFG}
    c0, p0, s0, f0 = syn.build(base)
    recs = json.loads(f0[p0])['records'] + \
        [{'kind': 'reconciliation', 'path': 'syn/o98-recon.json', 'blob_sha256': sha(files['syn/o98-recon.json'])}] + \
        syn.chain(files, 'syn/o98-recon.json', sf.REVIEWER)
    c, p, s, f = syn.build(dict(base, files=files, extra={'records': recs}))
    w = hf.World(syn.repo, syn.H)
    F = hf.freeze(syn.repo, c, p)
    d = p.rsplit('/', 1)[0]
    plan = {q: syn.repo.read(F, q) for q in syn.repo.paths(F) if rc.inside(d, q)}
    if case == 'symlink':
        plan[path] = ('symlink', plan[path])
    elif case == 'submodule':
        plan[path] = ('submodule', '1' * 40)
    plan[sf.DOC] = syn.repo.read(syn.H, sf.DOC) + b'\nA change on main.\n'
    M = syn.repo.derive(syn.H, plan, parents=[syn.H], subject='M with the plan directory and a corpus change')
    repo = ModeOverlay(syn.repo, [(M, path)] if case == 'mode' else [])
    argv = ['execution', '--config', '%s:%s' % (F, p), '--out', r.out()] + w.args(F) + \
        ['--scientific-base', syn.H, '--candidate', syn.H, '--ledger', '%s:syn/patch.json' % F, '--main', M]
    try:
        code, res = cli.run(argv, repo=repo, stderr=io.StringIO(), control=w.control(w.checkout()), environ={})
    except Exception as exc:
        return {'exception': '%s: %s' % (type(exc).__name__, exc)}
    res = res or {}
    if res.get('stop'):
        return {'exit': code, 'stop': res.get('stop')}
    doc_entry = [e for e in res.get('side_changes', []) if e['path'] == sf.DOC]
    evs = (doc_entry[0].get('record_conditions') or []) if doc_entry else []
    holds = evs[0].get('holds', {}) if evs else {}
    return {'exit': code, 'path': path, 'record_directory': res.get('record_directory'),
            'case_items': sorted((i['class'], i['subject'], i.get('why')) for i in res.get('items', [])
                                 if i['subject'] == path),
            'RC11': holds.get('RC11'), 'other_conditions': {k: v for k, v in sorted(holds.items()) if k != 'RC11'},
            'record_evaluated': bool(evs)}


# ---- the O-9 controls -----------------------------------------------------------------------------------------

def o9_controls(r, check, recorder):
    names = sorted(plan_files())
    main_role = partial(run_main, recorder=recorder)

    def equal_without(with_run, without_run):
        with_run['baseline'] = without_run
        return {'files': {'with-rule.json': with_run['result'][1], 'without-rule.json': without_run['result'][1]},
                'procedure': {'name': 'relational', 'lib': 'rel-equal',
                              'runs': ['with-rule.json', 'without-rule.json']}}

    def rc11_case(observed):
        holds = observed.get('RC11')
        recorder.capture_doc('reconcile.evaluate RC11', observed, case='',
                             attested={'outcome': 'RC_HOLDS' if holds is True else 'RC_FAILS',
                                       json.dumps({'condition': 'RC11', 'holds': holds}, sort_keys=True): True})

    # RDIR-1
    repo, H, F, M = world()
    res = main_role(repo, H, F, M)
    all_paths_classified = all(side_of(res, p) == [(p, 'record-directory', None)] for p in names)
    all_invariant = json.dumps({'all': 'paths_in_D', 'have': {'class': 'record-directory'}}, sort_keys=True)
    recorder.name_last('', attested={all_invariant: all_paths_classified})
    check('RDIR-1', 'every entry of D at M equal to F: each record-directory; A.5 no unequal path; no '
          'side-change-unclassified', 'each D path classified record-directory; rd.unequal empty; no unclassified item',
          res, all_paths_classified and
          (res.get('rd') or {}).get('unequal') == {} and not [x for x in res.get('items', [])
                                                              if x[0] == 'side-change-unclassified'])

    # RDIR-2
    mod = AUTH + '/review.json'
    repo, H, F, M = world({mod: b'{"synthetic": "review", "changed": true}\n'})
    res = main_role(repo, H, F, M)
    others_classified = all(side_of(res, p) == [(p, 'record-directory', None)] for p in names if p != mod)
    recorder.name_last('', bindings={'modified': mod},
                       attested={'others_class': 'record-directory' if others_classified else None})
    check('RDIR-2', 'one file in D modified on M after F: that file side-change-unclassified (differs from F); the others '
          'record-directory', 'the modified file unclassified "differs from F"; the other three record-directory',
          res, unclassified(res, mod) == [('side-change-unclassified', mod, 'differs from F')] and
          others_classified)

    # RDIR-3
    add = AUTH + '/added.json'
    repo, H, F, M = world(m_extra={add: b'{}\n'})
    res = main_role(repo, H, F, M)
    recorder.name_last('', bindings={'added': add})
    check('RDIR-3', 'a file added in D on M, absent at F: side-change-unclassified (absent at F)',
          'the added file unclassified "absent at F"', res,
          unclassified(res, add) == [('side-change-unclassified', add, 'absent at F')])

    # RDIR-4
    dele = AUTH + '/ledger.json'
    repo, H, F, M = world({dele: None})
    res = main_role(repo, H, F, M)
    scan_lists = bool(side_of(res, dele))
    recorder.name_last('', bindings={'deleted': dele}, attested={'not_in_H_to_M_scan': None if scan_lists else dele})
    check('RDIR-4', 'a file of F in D deleted on M (absent at H and M): side-change-unclassified (absent at M), reported '
          'by A.5 although the H-to-M scan does not list it', 'an unclassified item "absent at M" for the deleted path, '
          'and no side-change entry for it from the scan', res,
          unclassified(res, dele) == [('side-change-unclassified', dele, 'absent at M')] and not scan_lists)

    # RDIR-5
    out_p = 'notes/same.txt'
    repo, H, F, M = world(f_extra={out_p: b'same\n'}, m_extra={out_p: b'same\n'})
    res = main_role(repo, H, F, M)
    recorder.name_last('', bindings={'outside': out_p})
    check('RDIR-5', 'a path outside D whose blob at M equals its blob at F: side-change-unclassified (outside the record '
          'directory)', 'unclassified "outside the record directory"', res,
          unclassified(res, out_p) == [('side-change-unclassified', out_p, 'outside the record directory')])

    # RDIR-6
    sib = AUTH + '-x/f.json'
    repo, H, F, M = world(f_extra={sib: b'{}\n'}, m_extra={sib: b'{}\n'})
    res = main_role(repo, H, F, M)
    recorder.name_last('', bindings={'sibling': sib})
    check('RDIR-6', 'a sibling path D-x/f sharing D as a string prefix, equal at F and M: side-change-unclassified',
          'the sibling path unclassified (outside the record directory); not record-directory', res,
          unclassified(res, sib) == [('side-change-unclassified', sib, 'outside the record directory')] and
          not [x for x in side_of(res, sib) if x[1] == 'record-directory'])

    # RDIR-7
    bad = [AUTH + '/./x', AUTH + '/../x', AUTH + '//x', AUTH + '/x/..', AUTH + '/']
    good = [AUTH + '/x', AUTH + '/a/b.json']
    got = {p: rc.clean_path(p) for p in bad + good}
    predicate = {'.': got[bad[0]], '..': got[bad[1]] or got[bad[3]],
                 'empty component': got[bad[2]] or got[bad[4]], 'good path': all(got[p] for p in good)}
    recorder.capture_doc('reconcile.clean_path', {'paths': got}, case='',
                         attested={'outcome': 'PREDICATE', 'clean_path': predicate})
    check('RDIR-7', 'the clean-path predicate applied to paths with a ., .. or empty component: each refused (tested on the '
          'predicate)', 'clean_path false for each bad path, true for each good path', got,
          not any(got[p] for p in bad) and all(got[p] for p in good),
          files={'paths.json': bad + good, 'observed.json': got},
          procedure={'name': 'predicate', 'lib': 'ast', 'inputs': 'paths.json', 'attested': 'observed.json'})

    # RDIR-8: a mode change, a symbolic link and a submodule in D, each in its own world, each through the full
    # `execution --main` path (the M role) and, in the same run, through the RC11 of a reconciliation record the
    # configuration references; compared with the same world with D equal to F, where RC11 holds
    cases = {'mode': 'differs from F', 'symlink': 'not a regular file', 'submodule': 'not a regular file'}
    o8 = {'baseline': o98_run(r, None)}
    recorder.name_last('RC11 holds with the original directory')
    ok = o8['baseline'].get('RC11') is True and not o8['baseline'].get('stop') and \
        not o8['baseline'].get('exception') and not o8['baseline'].get('case_items')
    for case, why in cases.items():
        got = o98_run(r, case)
        o8[case] = got
        label = 'mode change, M role' if case == 'mode' else case + ', M role'
        recorder.name_last(label, bindings={'p': got.get('path')},
                           attested={'no_exception': 'exception' not in got and got.get('exit') != 71})
        ok = ok and not got.get('stop') and not got.get('exception') and \
            got.get('case_items') == [('side-change-unclassified', got['path'], why)] and got.get('RC11') is False and \
            got.get('other_conditions') == o8['baseline'].get('other_conditions')
    rc11_failed = all(o8[case].get('RC11') is False for case in cases)
    rc11_invariant = json.dumps({'condition': 'RC11', 'holds': False}, sort_keys=True)
    recorder.capture_doc('combined RC11 observations', o8, case='each case through RC11',
                         attested={'outcome': 'RC_FAILS' if rc11_failed else 'RC_HOLDS',
                                   rc11_invariant: rc11_failed,
                                   'no_group_error': all('exception' not in observed for observed in o8.values())})
    check('RDIR-8', 'in D: the same blob with a mode change (100644 to 100755); a symbolic link at M where F has a regular '
          'file of the same bytes; a submodule entry at M; each case run through the full execution --main path (the M '
          'role) and, separately, through a reconciliation record\'s RC11: each side-change-unclassified (differs from '
          'F, not a regular file, not a regular file); RC11 fails in each case; no exception and no *-group-error in '
          'either path', 'per case, in its own world and through cli.run: exactly one unclassified item on the case path '
          'with its reason; the RC11 of the referenced reconciliation record false, every other condition equal to the '
          'baseline world, where RC11 holds; no stop and no exception', o8, ok)

    # RDIR-9: a ledgered path, and separately a corpus path, inside D
    lp = AUTH + '/ledger.json'
    repo, H, F, M = world()
    a = main_role(repo, H, F, M, ledgered=[lp])
    recorder.name_last('ledgered path in D', attested={'reason': a.get('condition')})
    b = main_role(repo, H, F, M, corpus=[lp])
    recorder.name_last('corpus path in D', attested={'reason': b.get('condition')})
    check('RDIR-9', 'a ledgered path, and separately a corpus path, inside D: ERROR CONFIG_INCONSISTENT (Dir3)',
          'both runs stop CONFIG_INCONSISTENT with condition Dir3', {'ledgered': a, 'corpus': b},
          all(x.get('stop') == 'CONFIG_INCONSISTENT' and x.get('condition') == 'Dir3' for x in (a, b)))

    # RDIR-10: a configuration in the root directory
    repo = Overlay(None)
    H = repo.add_commit({'doc/a.md': b'base\n'}, [], 'H')
    F = repo.derive(H, {'retirement-config.json': b'{}\n', 'PREREG.md': b'# p\n'}, parents=[H], subject='F')
    M = repo.derive(H, {'retirement-config.json': b'{}\n', 'PREREG.md': b'# p\n'}, parents=[H], subject='M')
    res = main_role(repo, H, F, M, cpath='retirement-config.json')
    with_rule = recorder.name_last('')
    res0 = main_role(repo, H, F, M, cpath='retirement-config.json', rule=False)
    without = recorder.name_last('without the amendment')
    check('RDIR-10', 'a configuration in the root directory: the rule inactive, the run unchanged (items and side changes '
          'equal to the same run without this amendment), no record-directory classification (amendment r5)',
          'no stop and no exception; items and side changes equal to the run without the rule; no side change '
          'classified record-directory; the context inactive', {'with': res, 'without': res0},
          'stop' not in res and 'exception' not in res and res.get('items') == res0.get('items') and
          res.get('side') == res0.get('side') and
          not [x for x in res.get('side', []) if x[1] == rc.record_directory_class] and
          (res.get('rd') or {}).get('state', '').startswith('inactive'),
          **equal_without(with_rule, without))

    # RDIR-11
    repo, H, F, M = world(h_extra={AUTH + '/old.txt': b'old\n'})
    res = main_role(repo, H, F, M)
    recorder.name_last('', attested={'reason': res.get('condition')})
    check('RDIR-11', 'a path inside D that exists at H: ERROR CONFIG_INCONSISTENT (Dir2)', 'stop CONFIG_INCONSISTENT, Dir2',
          res, res.get('stop') == 'CONFIG_INCONSISTENT' and res.get('condition') == 'Dir2')

    # RDIR-12: a class prefix inside the authorized D
    sub = AUTH + '/sub/f.json'
    repo, H, F, M = world(f_extra={sub: b'{}\n'}, m_extra={sub: b'{}\n'})
    cls = [{'id': 'c', 'prefixes': [AUTH + '/sub/'], 'pins': []}]
    res = main_role(repo, H, F, M, classes=cls)
    recorder.name_last('', attested={'reason': res.get('condition')})
    check('RDIR-12', 'the authorized D, with a side-change class whose prefix lies inside D: ERROR CONFIG_INCONSISTENT '
          '(Dir3)', 'stop CONFIG_INCONSISTENT, Dir3', res,
          res.get('stop') == 'CONFIG_INCONSISTENT' and res.get('condition') == 'Dir3')

    # RDIR-12b: a configuration under .github/, (a) present at H, (b) absent at H
    gd = '.github/plan'
    repo, H, F, M = world(d=gd, h_extra={gd + '/existing.txt': b'x\n'})
    a = main_role(repo, H, F, M, cpath=gd + '/retirement-config.json')
    with_rule = recorder.name_last('(a) directory present at H')
    a0 = main_role(repo, H, F, M, cpath=gd + '/retirement-config.json', rule=False)
    without = recorder.name_last('without the amendment')
    repo, H, F, M = world(d=gd)
    b = main_role(repo, H, F, M, cpath=gd + '/retirement-config.json')
    reason = 'directory not admitted' if 'directory not admitted' in b.get('message', '') else b.get('condition')
    recorder.name_last('(b) directory absent at H', attested={'reason': reason})
    check('RDIR-12b', 'a configuration under .github/ with an entry inside it on M: (a) present at H: the rule inactive, no '
          'record-directory, the result equal to the run without this amendment; (b) absent at H: ERROR '
          'CONFIG_INCONSISTENT (directory not admitted)', '(a) items and side changes equal to the run without the rule, state '
          'inactive; (b) stop CONFIG_INCONSISTENT, authority', {'a': a, 'a_without': a0, 'b': b},
          a.get('items') == a0.get('items') and a.get('side') == a0.get('side') and
          not [x for x in a.get('side', []) if x[1] == 'record-directory'] and
          (a.get('rd') or {}).get('state', '').startswith('inactive') and
          b.get('stop') == 'CONFIG_INCONSISTENT' and b.get('condition') == 'authority',
          **equal_without(with_rule, without))

    # RDIR-13: a class pin naming a D path, differing from M
    p13 = AUTH + '/review.json'
    repo, H, F, M = world()
    cls = [{'id': 'pinned', 'pins': [{'path': p13, 'git_blob': None, 'blob_sha256': '0' * 64}]}]
    res = main_role(repo, H, F, M, classes=cls)
    recorder.name_last('', bindings={'p': p13})
    check('RDIR-13', 'a path in D, equal at F and M, that a class names with a pin differing from M: '
          'side-change-unclassified naming the class; not record-directory',
          'unclassified with the class-pin reason naming class pinned', res,
          unclassified(res, p13) == [('side-change-unclassified', p13,
                                      'the blob at M differs from the pin of class pinned')] and
          not [x for x in side_of(res, p13) if x[1] == 'record-directory'])

    # RDIR-14: no --freeze (full path, control harness)
    syn, w, c, p, F = syn_world(CFG)
    M = plan_on(syn, F, p, syn.H)
    argv = ['execution', '--config', '%s:%s' % (F, p), '--out', r.out(), '--scientific-base', syn.H, '--candidate',
            syn.H, '--ledger', '%s:syn/patch.json' % F, '--main', M]
    code, res = cli.run(argv, repo=syn.repo, harness=True, stderr=io.StringIO())
    res = res or {}
    dpaths = [e for e in res.get('side_changes', []) if rc.inside(AUTH, e['path'])]
    no_record_directory = 'record_directory' not in res
    unclassified_paths = bool(dpaths) and all(e['class'] is None for e in dpaths)
    invariant = json.dumps({'all': 'paths_in_D', 'have': {'class': 'side-change-unclassified'}}, sort_keys=True)
    recorder.name_last('', attested={'rule_active': not no_record_directory, 'a5_evaluated': not no_record_directory,
                                     invariant: unclassified_paths})
    check('RDIR-14', 'no --freeze: the rule inactive; files in D side-change-unclassified; A.5 not evaluated',
          'no record_directory in the result; every D side change unclassified', {'exit': code, 'side': dpaths,
                                                                                 'rd': res.get('record_directory')},
          no_record_directory and unclassified_paths)

    # RDIR-15, RDIR-18, RDIR-19: RC11
    repo, H, F, M = world()
    a = r11(repo, H, F, M)
    repo, H, F, M = world({AUTH + '/review.json': b'{"changed": 1}\n'})
    b = r11(repo, H, F, M)
    repo, H, F, M = world({AUTH + '/ledger.json': None})
    c_ = r11(repo, H, F, M)
    rc11_case(a)
    check('RDIR-15', 'a reconciliation record, M with D equal to F: RC11 holds', 'RC11 true', a, a.get('RC11') is True)
    rc11_case(b)
    check('RDIR-18', 'a reconciliation record, M with one file of D modified after F: RC11 fails', 'RC11 false', b,
          b.get('RC11') is False)
    rc11_case(c_)
    check('RDIR-19', 'a reconciliation record, M with one file of F\'s D deleted: RC11 fails (A.5)', 'RC11 false', c_,
          c_.get('RC11') is False)

    # RDIR-16: a configuration in a newly introduced, unrelated directory (full path, the tool's constant)
    other = 'syn2/new/plan/r1/retirement-config.json'
    syn, w, c, p, F = syn_world(other)
    M = plan_on(syn, F, p, syn.H)
    code, res = exec_run(r, syn, w, F, p, M)
    reason = (res.get('stop') or {}).get('message', '')
    recorder.name_last('', attested={'reason': 'directory not admitted' if 'directory not admitted' in reason else None})
    check('RDIR-16', 'a configuration in a newly introduced, unrelated directory (absent at H, holding the configuration '
          'and a file of record pins, no ledgered, corpus, class or .github/ path): ERROR CONFIG_INCONSISTENT '
          '(directory not admitted)', 'exit 65, stop CONFIG_INCONSISTENT, condition authority',
          {'exit': code, 'stop': res.get('stop')}, code == 65 and (res.get('stop') or {}).get('class') ==
          'CONFIG_INCONSISTENT' and ((res.get('stop') or {}).get('detail') or {}).get('condition') == 'authority')

    # RDIR-17, RDIR-24: the reserved class id; RDIR-24 through --classify (full path)
    repo, H, F, M = world()
    res = main_role(repo, H, F, M, classes=[{'id': rc.record_directory_class, 'pins': []}])
    recorder.name_last('', attested={'reason': res.get('condition')})
    check('RDIR-17', 'a class record defining class id record-directory: ERROR CONFIG_INCONSISTENT (Dir5)',
          'stop CONFIG_INCONSISTENT, Dir5', res, res.get('stop') == 'CONFIG_INCONSISTENT' and res.get('condition') == 'Dir5')
    cls_doc = {'schema': 'oi-side-change-classes/1', 'record_id': 'reserved', 'author': sf.WRITER, 'supersedes': None,
               'classes': [{'id': rc.record_directory_class, 'prefixes': ['notes/'], 'reason': 'synthetic', 'pins': []}]}
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
    recorder.name_last('', attested={'reason': ((res.get('stop') or {}).get('detail') or {}).get('condition')})
    check('RDIR-24', 'a class record admitted through --classify that defines the class id record-directory: ERROR '
          'CONFIG_INCONSISTENT (Dir5)', 'exit 65, stop CONFIG_INCONSISTENT, condition Dir5',
          {'exit': code, 'stop': res.get('stop')}, code == 65 and (res.get('stop') or {}).get('class') ==
          'CONFIG_INCONSISTENT' and ((res.get('stop') or {}).get('detail') or {}).get('condition') == 'Dir5')

    # RDIR-20: RC11 with an unauthorized D: ERROR before RC11 is evaluated
    calls = []
    orig = rc.evaluate

    def spy(*a, **k):
        calls.append(1)
        return orig(*a, **k)
    ud = 'unauth/plan/dir'
    repo, H, F, M = world(d=ud)
    rc.evaluate = spy
    observed_stop = None
    try:
        led = {'base': H, 'files': {'doc/a.md': {}}, 'splices': [], 'retained': []}
        M2 = repo.derive(M, {'doc/a.md': b'drift\n'}, parents=[M], subject='M drift')
        recon = [{'paths': [{'path': 'doc/a.md'}], '_ref': {'path': 'x', 'blob_sha256': '0' * 64}}]
        ex = exmod.Execution(Ctx(repo), H, H, led, None, M2, None, None, [], recon)
        ex.record_refs = {}
        ex.record_dir_args = {'freeze': F, 'cpath': ud + '/retirement-config.json', 'authorized': (AUTH,)}
        try:
            ex.main_role({'doc/a.md'})
            got = {'stop': None}
        except oc.Stop as s:
            observed_stop = s
            got = {'stop': s.cls, 'condition': (s.detail or {}).get('condition')}
    finally:
        rc.evaluate = orig
    got['evaluations'] = len(calls)
    reason = 'directory not admitted' if observed_stop and 'directory not admitted' in observed_stop.message else None
    recorder.capture_doc('execution.main_role with observed reconciliation calls',
                         control_records.stage_doc(ex.items, operation='execution.main_role', stop=observed_stop,
                                                   reconciliation_calls=len(calls)), case='',
                         attested={'reason': reason, 'rc11_evaluated': bool(calls)})
    check('RDIR-20', 'a reconciliation record, M with a file of D equal to F, but D not authorized: ERROR '
          'CONFIG_INCONSISTENT (directory not admitted) before RC11 is evaluated', 'stop CONFIG_INCONSISTENT, authority; no call of '
          'reconcile.evaluate', got, got.get('stop') == 'CONFIG_INCONSISTENT' and got.get('condition') == 'authority'
          and got['evaluations'] == 0)

    # RDIR-21: a class pin that matches M, on a file that differs between F and M
    p21 = AUTH + '/review.json'
    new = b'{"changed on M": true}\n'
    repo, H, F, M = world({p21: new})
    cls = [{'id': 'matching', 'pins': [{'path': p21, 'git_blob': repo.blob_id(M, p21), 'blob_sha256': sha(new)}]}]
    res = main_role(repo, H, F, M, classes=cls)
    class_route_stands = side_of(res, p21) == [(p21, 'matching', None)]
    recorder.name_last('', attested={'class_route_entry_stands': class_route_stands})
    check('RDIR-21', 'a file in D that differs between F and M, and a class pin naming it that matches M: the class '
          'route\'s entry stands and A.5 issues side-change-unclassified (differs from F); not accepting',
          'side-change entry class matching; an unclassified item "differs from F"', res,
          class_route_stands and
          unclassified(res, p21) == [('side-change-unclassified', p21, 'differs from F')])

    # RDIR-22: an unauthorized D with no entry on M (full path), compared with the tool without the rule
    syn, w, c, p, F = syn_world('syn/cfg/config.json')
    M = syn.repo.derive(syn.H, {'notes/m.txt': b'main\n'}, parents=[syn.H], subject='M')
    with_r = exec_run(r, syn, w, F, p, M)
    with_run = recorder.name_last('', attested={'no_error': not with_r[1].get('stop')})
    without = without_rule(lambda: exec_run(r, syn, w, F, p, M))
    without_run = recorder.name_last('without the amendment')
    check('RDIR-22', 'an unauthorized D with no entry inside it on M, under execution --main --freeze: no ERROR; side '
          'changes classified exactly as without this amendment', 'no stop; record_directory state inactive; result '
          'equal to the run without the rule', {'exit': with_r[0], 'rd': with_r[1].get('record_directory'),
                                               'exit_without': without[0]},
          not with_r[1].get('stop') and with_r[0] == without[0] and
          strip_run(with_r[1]) == strip_run(without[1]) and
          (with_r[1].get('record_directory') or {}).get('state', '').startswith('inactive'),
          **equal_without(with_run, without_run))

    # RDIR-23: the authorized D under coverage (no M): A.3-A.5 never evaluated
    built = []
    orig_rd = rc.RecordDirectory

    class Trap(orig_rd):
        def __init__(self, *a, **k):
            built.append(1)
            orig_rd.__init__(self, *a, **k)
    syn, w, c, p, F = syn_world(CFG)
    argv = ['coverage', '--config', '%s:%s' % (F, p), '--out', r.out()] + w.args(F) + \
        ['--commit', syn.H, '--check', 'zc']
    rc.RecordDirectory = Trap
    try:
        code, res = cli.run(argv, repo=syn.repo, stderr=io.StringIO(), control=w.control(w.checkout()), environ={})
    finally:
        rc.RecordDirectory = orig_rd
    res = res or {}
    rd_evaluated = bool(built) or 'record_directory' in res
    with_run = recorder.name_last('', attested={'a3_a5_evaluated': rd_evaluated})
    opts = {'repo': syn.repo, 'stderr': io.StringIO(), 'control': w.control(w.checkout()), 'environ': {}}
    clean_argv = argv.copy()
    clean_argv[clean_argv.index('--out') + 1] = r.out()
    code0, res0 = without_rule(lambda: cli.run(clean_argv, **opts))
    without_run = recorder.name_last('without the amendment')
    check('RDIR-23', 'the authorized D and a configuration whose run is coverage (no M): no evaluation of A.3-A.5',
          'no RecordDirectory built; no record_directory in the result; no stop', {'exit': code, 'built': len(built),
                                                                                 'stop': res.get('stop')},
          not rd_evaluated and not res.get('stop') and code0 == code and strip_run(res or {}) == strip_run(res0 or {}),
          **equal_without(with_run, without_run))

    # RDIR-25: the synthetic world of the conformance controls: an unauthorized D (syn) present at H, entries on M
    syn, w, c, p, F = syn_world('syn/config.json')
    M = syn.repo.derive(syn.H, {'notes/m.txt': b'main\n'}, parents=[syn.H], subject='M')
    present_h = any(rc.inside('syn', q) for q in syn.repo.entries(syn.H))
    on_m = any(rc.inside('syn', q) for q in syn.repo.entries(M))
    with_r = exec_run(r, syn, w, F, p, M)
    with_run = recorder.name_last('', attested={'no_error': not with_r[1].get('stop')})
    without = without_rule(lambda: exec_run(r, syn, w, F, p, M))
    without_run = recorder.name_last('without the amendment')
    check('RDIR-25', 'the synthetic world: an unauthorized D (syn) present at H, with entries inside it on M, under '
          'execution --main --freeze: no ERROR; the rule inactive; side changes, items and outcome equal to the same '
          'run without this amendment (the existing conformance controls are checked by their own results)',
          'D present at H and on M; no stop; state inactive; result equal to the run without the rule',
          {'present_at_H': present_h, 'on_M': on_m, 'exit': with_r[0], 'rd': with_r[1].get('record_directory'),
           'exit_without': without[0]},
          present_h and on_m and not with_r[1].get('stop') and with_r[0] == without[0] and
          strip_run(with_r[1]) == strip_run(without[1]) and
          (with_r[1].get('record_directory') or {}).get('state') == 'inactive: unauthorized, present at H',
          **equal_without(with_run, without_run))


# ---- the item-2 controls --------------------------------------------------------------------------------------

def arm_text(workflow_path):
    with open(workflow_path, encoding='utf-8') as f:
        for line in f:
            if line.strip().startswith('item2-coverage)'):
                return line.strip()
    return None


# A1 staging amendment r2 (R6.PLAN.4, R6.ITEM2.1, I2-1): the named check `item2` directly after --commit "$X"; both
# segments, the HP input and the three --classify operands keep their order and quoting.
EXPECTED_ARM = ('item2-coverage) exec python3 -I -S -B tools/ledger_coverage.py coverage "$@" --commit "$X" '
                '--check item2 --segment "$E..$H" --segment "$H..$X=$F:$D/ledger.json" --hp "$F:$D/hp.json" '
                '--classify "$F:$A/records/gr58-hit-classification-v3.json" '
                '--classify "$F:$D/context-adjudications.json" --classify "$F:$D/hit-classifications.json" ;;')


def arm_classify(arm):
    """The --classify operands of the arm, with $F and $D unresolved."""
    return re.findall(r'--classify "([^"]+)"', arm or '')


def i2_world(ctx_doc, hit_doc, reference=True, review=True, drop=(), unref=()):
    """The synthetic world with the plan directory's two item-2 records, referenced by the configuration and
    reviewed (each as the flags say); `drop` names records absent from F; `unref` names records present at F but
    neither referenced by the configuration nor reviewed."""
    d = 'syn/plan'
    cpath = d + '/retirement-config.json'
    names = {'context': d + '/context-adjudications.json', 'hits': d + '/hit-classifications.json'}

    def extra(files):
        out = []
        for k, doc in (('context', ctx_doc), ('hits', hit_doc)):
            if k in drop:
                continue
            files[names[k]] = sf.jb(doc)
            if k in unref:
                continue
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


def coverage_via_arm(r, syn, w, F, p, d, arm, commit=None):
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
    # the synthetic configuration's own check stands for the arm's `--check item2` (A1 staging amendment r2, sec. 1)
    argv = ['coverage', '--config', '%s:%s' % (F, p), '--out', r.out()] + w.args(F) + \
        ['--commit', commit or syn.H, '--check', 'zc'] + ops
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


def i2_controls(r, check, workflow_path, recorder):
    arm = arm_text(workflow_path)
    matches = arm == EXPECTED_ARM
    with open(workflow_path, 'rb') as f:
        workflow = f.read()
    invariant = json.dumps({'arm': 'item2-coverage',
                            'equals': 'existing arguments followed by the two --classify arguments of B.2, '
                                      'every expansion quoted'}, sort_keys=True)
    recorder.capture_doc('the item2-coverage workflow arm', {'observed': arm}, case='',
                         attested={'outcome': 'TEXT_EQUAL' if matches else 'TEXT_DIFFERS', invariant: matches})
    check('I2-1', 'the item2-coverage arm: the exact workflow arm with --check item2 after --commit "$X", retaining '
          'both segments and all existing operands, every expansion quoted', 'the arm line equals the expected text',
          arm, matches, files={'workflow.yml': workflow, 'expected.txt': EXPECTED_ARM.encode('utf-8'),
                               'observed.json': {'arm': arm, 'matches': matches}},
          procedure={'name': 'workflow-text', 'lib': 'ast', 'inputs': ['workflow.yml', 'expected.txt'],
                     'attested': 'observed.json'})

    def site_case(name, site, coverage, items, **inputs):
        selected = [item for item in items if item['subject'] == site]
        recorder.capture_doc('coverage of the named site',
                             control_records.stage_doc(selected, operation='coverage', sites=[coverage.site_out[site]],
                                                       inputs=inputs),
                             case=name, bindings={'site': site})

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
    recorder.name_last('workflow coverage')
    routed = [e for e in got.get('context', []) if e.get('id') == 'c1']
    cv10, it10 = w.coverage(x, [ce.seg(w.pin, x)], adj={'context': routed}, hits=False)
    site_case('with record', sd, cv10, it10, routed=routed)
    site_case('without', sd, cv, it, routed=[])
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

    # I2-4: a non-empty hit-classifications.json that resolves a concrete hit when referenced; not referenced, it is
    # record-invalid and the hit stays REVIEW_REQUIRED
    line = 'The beta value is reported here.'
    hit4 = {'id': 'h4', 'file': sf.DOC, 'line_sha256': sha(line.encode()), 'segment': None,
            'profiles': ['beta-word'], 'semantic_classification': 'an unrelated use of the word', 'author': sf.WRITER}

    def i24(reference):
        syn, sw, F, p, d, names = i2_world(ctx_doc_of([]), hit_doc_of([hit4]), unref=() if reference else ('hits',))
        X = syn.repo.derive(syn.H, {sf.DOC: syn.repo.read(syn.H, sf.DOC) + ('\n%s\n' % line).encode()},
                            parents=[syn.H], subject='a candidate with a beta-word hit')
        code, res, got = coverage_via_arm(r, syn, sw, F, p, d, arm, commit=X)
        ln = [i for i, l in enumerate(syn.repo.read(X, sf.DOC).decode().split('\n'), 1) if l == line]
        on = sorted((i['class'], i.get('decision')) for i in res.get('items', [])
                    if i.get('file') == sf.DOC and ln and i.get('line') == ln[0])
        inv = sorted(i['subject'] for i in res.get('items', []) if i['class'] == 'record-invalid')
        subj = [i['subject'] for i in res.get('items', []) if i.get('file') == sf.DOC and ln and
                i.get('line') == ln[0]]
        return {'exit': code, 'stop': res.get('stop'), 'items_on_hit': on, 'record_invalid': inv,
                'hit_subject': subj[0] if subj else '%s:%d' % (sf.DOC, ln[0] if ln else 0),
                'hits_reaching_pipeline': len(got.get('hits') or []), 'file': names['hits']}
    # the case the row states (not referenced) first, so that it is the row's case; the referenced run follows
    neg = i24(False)
    pos = i24(True)
    check('I2-4', 'hit-classifications.json present but not referenced by the configuration: record-invalid; the hit '
          'stays REVIEW_REQUIRED', 'referenced and reviewed, the record resolves the concrete beta-word hit (no item on '
          'its line); not referenced, the file is record-invalid, no hit record reaches the pipeline and the same hit is '
          'an item with decision REVIEW_REQUIRED', {'referenced': pos, 'not referenced': neg},
          not pos['stop'] and not pos['items_on_hit'] and pos['hits_reaching_pipeline'] == 1 and
          not neg['stop'] and neg['record_invalid'] == [neg['file']] and neg['hits_reaching_pipeline'] == 0 and
          neg['items_on_hit'] and all(dec == oc.review for _, dec in neg['items_on_hit']),
          cases=[('', {'hit': neg['hit_subject']}), ('referenced (positive)', {'hit': neg['hit_subject']})])

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
    routed_context = got.get('context')
    recorder.name_last('empty entries with record_id and review',
                       attested={'record_admitted': ok and routed_context == [],
                                 'sites_resolved_by_it': len(routed_context) if routed_context is not None else None})
    nid = ctx_doc_of([])
    nid.pop('record_id')
    syn2, sw2, F2, p2, d2, n2 = i2_world(nid, hit_doc_of([]))
    code2, res2, got2 = coverage_via_arm(r, syn2, sw2, F2, p2, d2, arm)
    recorder.name_last('without record_id')
    syn3, sw3, F3, p3, d3, n3 = i2_world(ctx_doc_of([]), hit_doc_of([]), review=False)
    code3, res3, got3 = coverage_via_arm(r, syn3, sw3, F3, p3, d3, arm)
    recorder.name_last('without review')
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
    recorder.name_last('workflow coverage')
    routed = [e for e in got.get('context', []) if e.get('id') == 'i1']
    cv6b, it6b = w6.coverage(x6, [ce.seg(w6.pin, x6)], adj={'context': routed}, hits=False)
    site_case('with adjudication', s6, cv6b, it6b, routed=routed)
    site_case('without', s6, cv6, it6, routed=[])
    check('I2-8', 'an indicator adjudication supplied through context-adjudications.json, matching both context hashes and '
          'both structure hashes of a LIST or TABLE site: the context-structure-changed item resolved; without it '
          'REVIEW_REQUIRED context-structure-changed', 'the adjudication reaches the context collection through the '
          'arm; without it context-structure-changed, with it no item on the site',
          {'exit': code, 'routed': routed, 'without': ce.classes(it6), 'with': ce.classes(it6b), 'site': out6},
          not res.get('stop') and routed == [entry6] and ce.classes(it6) == ['context-structure-changed'] and
          not [i for i in it6b if i['subject'] == s6])


IDS = ['RDIR-1', 'RDIR-2', 'RDIR-3', 'RDIR-4', 'RDIR-5', 'RDIR-6', 'RDIR-7', 'RDIR-8', 'RDIR-9', 'RDIR-10', 'RDIR-11', 'RDIR-12', 'RDIR-12b',
       'RDIR-13', 'RDIR-14', 'RDIR-15', 'RDIR-16', 'RDIR-17', 'RDIR-18', 'RDIR-19', 'RDIR-20', 'RDIR-21', 'RDIR-22', 'RDIR-23', 'RDIR-24',
       'RDIR-25', 'I2-1', 'I2-2', 'I2-3', 'I2-4', 'I2-5', 'I2-6', 'I2-7', 'I2-8']
