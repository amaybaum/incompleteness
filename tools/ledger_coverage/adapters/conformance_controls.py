"""Controls of the design (v6.0e; sec. 10.2, 10.4, 13.2, 16): configuration admission and execution identity on an
in-memory host (TR1-TR3, TR5, TR13-TR15, TR28, TR29, TR48, TR50-TR52, EI1, EI2, EI4, EI7), the consumer's acceptance
predicate (X11, TR14, TR15, TR28-TR30, TR50-TR52, EI2, EI3, EI7, GV7) and the landing's re-resolution of `M` (EI5),
the durable evidence TR45/TR46, the verified reader on small on-disk repositories (GV1-GV6), the host-read failures
(GV7), the pre-run pin check and the entry point as subprocess runs on trees materialized under OUT_DIR (EI6,
EI8-EI15), native delegation G4-G9 on a small on-disk repository, the delegated clone's git configuration (O3-FILTER),
commits after X R16/R17, widening A12r,
the synthetic parts of S4a and Z11, the lineage controls LN1-LN8 and LN10 (DI-2), and the retained controls for the
independent reviews' findings (R3-F2, R4-B3, R4-B3-DUP, R5-N6, R6-G6).

Every control is reported as {id, expected, predicate, actual, status} with status PASS, FAIL or NOT RUN (sec. 10.4,
B6; r6 R6.GATE.5: no SKIP). A control that needs the real host (a CI job with the host's API) is NOT RUN here, never
PASS. Every in-process tool run is captured (control_records.Recorder.wrap_cli) and retained as the evidence of the
control recorded next; `control-records.json` (oi-control-records/1) and `evidence/conformance/<id>/` are written
beside the summary, for the gate (design r6 sec. 16).

Usage: python3 -I -B tools/ledger_coverage/adapters/conformance_controls.py OUT_DIR
"""
import ast
import copy
import gzip
import hashlib
import io
import json
import os
import re
import shutil
import stat
import subprocess
import sys
import tempfile
import zlib

here = os.path.dirname(os.path.abspath(__file__))
tools = os.path.dirname(os.path.dirname(here))
if 'ledger_coverage' not in sys.modules:
    # the package is loaded by its location, as the entry point loads it; no directory is put on sys.path
    import importlib.util
    _pkg = os.path.dirname(here)
    _spec = importlib.util.spec_from_file_location('ledger_coverage', os.path.join(_pkg, '__init__.py'),
                                                   submodule_search_locations=[_pkg])
    sys.modules['ledger_coverage'] = importlib.util.module_from_spec(_spec)
    _spec.loader.exec_module(sys.modules['ledger_coverage'])

from ledger_coverage.engine import checker, cli, delegation as delmod, execution as exmod  # noqa: E402
from ledger_coverage.engine import gitobj, host as hostmod, purity, schema as schemamod, util  # noqa: E402
from ledger_coverage.adapters import host_fixture as hf, synthetic_fixture as sf  # noqa: E402
from ledger_coverage.adapters import record_directory_controls as rdc  # noqa: E402
from ledger_coverage.adapters import control_records  # noqa: E402
from ledger_coverage.adapters import identity_fixture as idf_  # noqa: E402
from ledger_coverage.adapters.identity_fixture import review_record  # noqa: E402
from ledger_coverage.adapters import postfreeze_controls as pfc  # noqa: E402

RESULTS = []
# R6.GATE.7: the tool runs captured since the previous record are the evidence of the next one
REC = control_records.Recorder('conformance', None)
RUNS = {}
ATTESTED = {}
PROCEDURES = {}
WORKFLOW = os.path.join(os.path.dirname(tools), '.github', 'workflows', 'ledger-coverage.yml')


def record(cid, expected, predicate, actual, status, cases=None, attested=None, baseline_of=None):
    """`cases`: per captured run of this control, in order, None or (case name, bindings) naming it as an
    expectation case (R6.GATE.7); `attested`: {case: {key: value}} the runner states for a case; `baseline_of`:
    {case: earlier case} whose result a restored case is compared with."""
    RESULTS.append({'id': cid, 'expected': expected, 'predicate': predicate, 'actual': actual, 'status': status})
    runs = REC.take()
    for run, c in zip(runs, cases or []):
        if c is not None:
            run['case'], run['bindings'] = c[0], dict(c[1] or {})
    for run in runs:
        if run['case'] in (attested or {}):
            run['attested'] = dict(run.get('attested') or {}, **attested[run['case']])
        if run['case'] in (baseline_of or {}):
            run['baseline'] = next((x for x in runs if x['case'] == baseline_of[run['case']]), None)
    RUNS.setdefault(cid, []).extend(runs)


def check(cid, expected, predicate, actual, holds, cases=None, attested=None, baseline_of=None, files=None,
          procedure=None):
    """`files` and `procedure`: evidence files and the procedure inputs naming them (R6.GATE.8)."""
    record(cid, expected, predicate, actual, 'PASS' if holds else 'FAIL', cases, attested, baseline_of)
    if files is not None or procedure is not None:
        PROCEDURES[cid] = (files, procedure)


def not_run(cid, expected, why):
    record(cid, expected, None, why, 'NOT RUN')


def retain_restored(run, baseline):
    """Retain a fresh execution on the clean fixture alongside its earlier result."""
    before = len(REC.pending)
    run()
    if len(REC.pending) != before + 1:
        raise ValueError('a restoration must capture one new execution')
    REC.name_last('restored', baseline=baseline)



def sha(b):
    return hashlib.sha256(b).hexdigest()


def stop(res):
    return (res or {}).get('stop', {}).get('class')


def classes(res):
    return sorted({i['class'] for i in (res or {}).get('items', [])})


def show(code, res):
    return {'exit': code, 'stop': stop(res), 'message': ((res or {}).get('stop') or {}).get('message', '')[:200]}


def refused(code, res):
    return code == 65 and stop(res) == 'CONFIG_UNREVIEWED'


def snapshot_of(res):
    return (((res or {}).get('config') or {}).get('admission') or {}).get('simulated_chain', {}).get('snapshot', {})


UNREV = 'ERROR CONFIG_UNREVIEWED, exit 65'


# ---- the admission and execution-identity world -------------------------------------------------------------------

class TR:
    """A synthetic configuration at commit c (its directory syn/cfg/ holding the configuration and its review), a
    plan commit F with a PREREG.md beside the configuration, and an in-memory host world with a tool commit T."""

    def __init__(self, runner, variant=None):
        self.r = runner
        self.syn = sf.Syn()
        pd = sf.patch_doc(self.syn.H, [])
        v = {'patch_sha': sha(pd), 'files': {'syn/patch.json': pd}}
        v.update(variant or {})
        self.c, self.p, self.s, self.files = self.syn.build(v)
        self.repo = self.syn.repo

    def world(self, **kw):
        return hf.World(self.repo, self.syn.H, **kw)

    def freeze(self, **kw):
        return hf.freeze(self.repo, self.c, self.p, **kw)

    def run(self, w, F, args=None, control=None, environ=None, op=None, checkout=None, path=None):
        argv = (op or ['terms']) + ['--config', '%s:%s' % (F, path or self.p), '--out', self.r.out()] + \
            (args if args is not None else w.args(F)) + ['--commit', self.syn.H]
        ctl = w.control(checkout if checkout is not None else w.checkout()) if control is None else control
        return cli.run(argv, repo=self.repo, stderr=io.StringIO(), control=ctl,
                       environ=environ if environ is not None else {})


def with_tool(r, files=None, wf=None, wf_path=hf.WF_PATH, extra=None, run=None):
    """A configuration pinning the given tool files and workflow, its F, and a world whose T holds them."""
    tf = dict(hf.TOOL_FILES if files is None else files)
    t = TR(r, {'tool': hf.tool_pins(tf, wf, wf_path)})
    w = t.world(tool_files=tf, wf=wf, wf_path=wf_path, extra=extra, run=dict({'workflow_path': wf_path}, **(run or {})))
    return t, w, t.freeze()


def tr_controls(r, native_tr5=False):
    t = TR(r)
    w = t.world()
    F = t.freeze()
    code, res = t.run(w, F)
    snap = snapshot_of(res)
    fields = ['run', 'tool_commit', 'tool_blobs', 'workflow', 'freeze', 'pin_table', 'configuration',
              'configuration_review', 'evaluated', 'invocation']
    run_fields = ['run_id', 'repository_id', 'head_repository_id', 'event', 'head_branch', 'workflow_path',
                  'head_sha']
    pos = dict(show(code, res), missing=[f for f in fields if f not in snap],
               missing_run=[f for f in run_fields if f not in snap.get('run', {})])
    clean = REC.name_last(None, attested={'snapshot_fields_all_present': not pos['missing']
                                         and not pos['missing_run']})
    retain_restored(lambda: t.run(w, F), clean)
    check('TR5-sim', 'the whole of sec. 6.3 holds on the in-memory host (--freeze F, --config F:path, the PREREG.md '
          'beside the configuration listing it and its review, a workflow_dispatch run in the configuration\'s '
          'repository, T\'s tool files and workflow equal to the pins and to the checkout): every snapshot field '
          'recorded; the result is a control artefact (control-harness), never chain',
          "exit == 0, admission.mode == 'control-harness', harness is true, every snapshot field and run field "
          "present, tool_commit == T and freeze == F", pos,
          code == 0 and res['config']['admission']['mode'] == 'control-harness' and res.get('harness') is True
          and not pos['missing'] and not pos['missing_run'] and snap.get('tool_commit') == w.T and
          snap.get('freeze') == F)
    if not native_tr5:
        not_run('TR5', '`config.admission: "chain"` with every snapshot field of sec. 6.3 recorded (positive control, '
               'CI only)', 'needs a run of the pinned workflow in the repository the configuration names, with the '
                'host API; CI plan in the report')
    # TR1: no --freeze, with and without the in-memory host
    a1 = show(*t.run(w, F, args=[], control={}))
    REC.name_last(None, attested={'message_names': '--freeze' if '--freeze' in a1['message'] else None})
    a2 = show(*t.run(w, F, args=[]))
    retain_restored(lambda: t.run(w, F), clean)
    check('TR1', 'a run without --freeze: ' + UNREV, "both runs (no host; the in-memory host) exit 65 with stop "
          "'CONFIG_UNREVIEWED' naming --freeze", [a1, a2],
          all(o['exit'] == 65 and o['stop'] == 'CONFIG_UNREVIEWED' and '--freeze' in o['message'] for o in (a1, a2)))
    # TR2: the configuration not in the pin table of the PREREG.md beside it
    rv = t.p.rsplit('/', 1)[0] + '/review.json'
    F2 = t.freeze(listed={rv: t.repo.read(t.c, rv)})
    o2 = show(*t.run(w, F2))
    retain_restored(lambda: t.run(w, F), clean)
    check('TR2', 'a configuration whose sha256 is not in the pin table of the PREREG.md beside it: ' + UNREV,
          "exit == 65 and stop == 'CONFIG_UNREVIEWED', refused by the pin table's rows", o2,
          o2['exit'] == 65 and o2['stop'] == 'CONFIG_UNREVIEWED' and o2['message'].startswith('the last Record pins'))
    # TR3: the review beside the configuration, naming its blob, not in the pin table
    F3 = t.freeze(listed={t.p: t.repo.read(t.c, t.p)})
    o3 = show(*t.run(w, F3))
    retain_restored(lambda: t.run(w, F), clean)
    check('TR3', 'a review record placed beside the configuration, naming its blob, but not in F\'s pin table: '
          + UNREV, "exit == 65 and stop == 'CONFIG_UNREVIEWED', refused because no review is listed", o3,
          o3['exit'] == 65 and o3['stop'] == 'CONFIG_UNREVIEWED' and o3['message'].startswith('no review record of the'))
    # the configuration read from F only: --config naming another commit than --freeze
    other_c = t.repo.derive(F, {}, parents=[F], subject='another commit')
    of = show(*cli.run(['terms', '--config', '%s:%s' % (other_c, t.p), '--out', r.out(), '--freeze', F, '--commit',
                        t.syn.H], repo=t.repo, stderr=io.StringIO(), control=w.control(w.checkout()), environ={}))
    REC.name_last(None, attested={'message_names': 'F' if 'from F only' in of['message'] else None})
    check('ADM-CONFIG-AT-F', 'configuration admission point 1: the configuration is read only from F\'s tree, never '
          'from another commit (implementation control)', "--config naming a commit other than --freeze exits 65 "
          "CONFIG_UNREVIEWED, naming F", of, of['exit'] == 65 and of['stop'] == 'CONFIG_UNREVIEWED' and
          'from F only' in of['message'])
    # TR13: a local run, all inputs otherwise valid; and a run whose environment imitates a host job without a token
    code13, res13 = t.run(w, F, control={}, environ={})
    o13 = show(code13, res13)
    local13 = REC.name_last('local run, all inputs valid')
    code13b, res13b = t.run(w, F, control={}, environ={'GITHUB_ACTIONS': 'true', 'GITHUB_RUN_ID': '7'})
    o13b = show(code13b, res13b)
    REC.name_last('host-imitating environment without a token')
    # the consumer given the local run's result: never acceptable
    pins13 = {'config': {'path': t.p, 'blob_sha256': t.s}, 'freeze': F}
    acc13 = checker.accept(res13 or {}, code13, pins13)
    REC.capture_doc('checker.accept', res13 or {}, case='acceptance',
                    attested={'outcome': 'ACCEPTED' if acc13 else 'NON_ACCEPTANCE'})
    t.run(w, F, control={}, environ={})
    REC.name_last('restored', baseline=local13)
    files13 = {'results.json': {'local run, all inputs valid': {'raw': res13, 'exit': code13},
                                'host-imitating environment without a token': {'raw': res13b, 'exit': code13b}},
               'landing.json': {'used_by_accept': False}, 'snapshot.json': {'pins': pins13},
               'acceptance.json': {'acceptance': acc13}}
    check('TR13', 'a local run, all inputs otherwise valid: no "chain" admission; never acceptable',
          "both exit 65 with stop 'CONFIG_UNREVIEWED'", [o13, o13b],
          all(o['exit'] == 65 and o['stop'] == 'CONFIG_UNREVIEWED' for o in (o13, o13b)) and not acc13,
          files=files13, procedure={'name': 'acceptance', 'lib': 'consumer', 'results': 'results.json',
                                    'landing_record': 'landing.json', 'snapshot': 'snapshot.json',
                                    'attested': 'acceptance.json'})
    # TR14 at the tool
    out14 = {}
    for name, run in (('fork', {'repository_id': 78, 'head_repository_id': 78}),
                      ('other repository', {'repository_id': 79, 'head_repository_id': 79}),
                      ('pull_request from a fork',
                       {'head_repository_id': 78, 'event': 'pull_request'}),
                      ('head repository a fork, event workflow_dispatch', {'head_repository_id': 78}),
                      ('repository another, head repository canonical', {'repository_id': 79})):
        out14[name] = show(*t.run(t.world(run=run), F))
        REC.name_last(name)
    retain_restored(lambda: t.run(w, F), clean)
    check('TR14-tool', 'the same workflow and tool run in a fork, or in another repository; separately, a '
          'pull_request run from a fork, executed and listed in the canonical repository: ERROR at the tool (repository or head '
          'repository id differs from repository_id); the consumer half is reported with the acceptance controls',
          "every case exits 65 with stop 'CONFIG_UNREVIEWED'", out14,
          all(o['exit'] == 65 and o['stop'] == 'CONFIG_UNREVIEWED' for o in out14.values()))
    # TR15 at the tool
    t15, w15, F15 = with_tool(r)
    t15.run(w15, F15)
    clean15 = REC.name_last('clean workflow pin')
    w15.h.runs[w15.run_id]['head_sha'] = t15.world(wf=hf.WF + b'# a changed step\n').T
    a15 = show(*t15.run(w15, F15))
    REC.name_last('workflow blob differs at T')
    t15b, w15b, F15b = with_tool(r, wf_path='.github/workflows/other/lc.yml')
    w15b.h.runs[w15b.run_id]['workflow_path'] = hf.WF_PATH
    b15 = show(*t15b.run(w15b, F15b))
    other = hf.World(t.repo, t.syn.H, wf_path='.github/workflows/other/lc.yml',
                     run={'workflow_path': '.github/workflows/other/lc.yml'})
    c15 = show(*t.run(other, F))
    REC.name_last('same-named workflow at another path')
    w15.h.runs[w15.run_id]['head_sha'] = w15.T
    retain_restored(lambda: t15.run(w15, F15), clean15)
    check('TR15', 'a run of a workflow whose blob at T differs from tool.workflow.blob_sha256 (CX-2); separately a '
          'same-named workflow at a path other than tool.workflow.path: ERROR at the tool',
          "all three cases (a changed workflow at T; the run's workflow path differing from the pin; a same-named "
          "workflow at another path) exit 65 with stop 'CONFIG_UNREVIEWED'", [a15, b15, c15],
          all(o['exit'] == 65 and o['stop'] == 'CONFIG_UNREVIEWED' for o in (a15, b15, c15)))
    # TR28 / TR52: a tool blob differing from its pin; an extra file under the package directory
    blob = show(*t.run(t.world(tool_files=dict(hf.TOOL_FILES, **{hf.PKG + 'engine/x.py': b'x = 2\n'})), F))
    REC.name_last('tool blob differs')
    extra = show(*t.run(t.world(extra={hf.PKG + 'engine/y.py': b'y = 1\n'}), F))
    REC.name_last('extra file under tools/ledger_coverage/')
    retain_restored(lambda: t.run(w, F), clean)
    check('TR28-tool', 'a T whose tool blobs differ from the configuration\'s tool.files pins (CX-1), or that carries '
          'an extra file under the package directory: ERROR at the tool; the consumer half is TR28-consumer',
          "both exit 65 with stop 'CONFIG_UNREVIEWED'", {'blob': blob, 'extra': extra},
          all(o['exit'] == 65 and o['stop'] == 'CONFIG_UNREVIEWED' for o in (blob, extra)))
    extra2 = show(*t.run(t.world(extra={hf.PKG + 'notes.txt': b'a file the pins do not name\n'}), F))
    retain_restored(lambda: t.run(w, F), clean)
    check('TR52', 'an additional file under the package directory at T that tool.files does not name: ERROR',
          "exit 65 with stop 'CONFIG_UNREVIEWED'", extra2, extra2['exit'] == 65 and
          extra2['stop'] == 'CONFIG_UNREVIEWED')
    # TR48: the positive K7 control
    code48, res48 = t.run(w, F)
    snap48 = snapshot_of(res48)
    exact_tool_blobs = snap48.get('tool_blobs') == {f['path']: f['blob_sha256'] for f in hf.tool_pins()['files']}
    exact_workflow = snap48.get('workflow') == hf.tool_pins()['workflow']
    recorded_tool = snap48.get('tool_commit') == w.T
    clean48 = REC.name_last('', attested={'snapshot_T_recorded': recorded_tool,
                                          'tool_and_workflow_blobs_equal_pins': exact_tool_blobs and exact_workflow})
    retain_restored(lambda: t.run(w, F), clean48)
    check('TR48', 'a valid T whose package directory and entry point hold exactly tool.files, each regular with its '
          'pinned blob, the workflow equal to its pin, the checkout equal to T: execution identity holds; T and every '
          'tool and workflow blob recorded',
          "exit 0; the snapshot's tool_commit is T, tool_blobs equal the pins and workflow equals the pin",
          {'exit': code48, 'tool_commit': recorded_tool, 'tool_blobs': snap48.get('tool_blobs'),
           'workflow': snap48.get('workflow')},
          code48 == 0 and recorded_tool and exact_tool_blobs and exact_workflow)
    # TR50: the workflow at T one byte different
    o50 = show(*t.run(t.world(wf=hf.WF + b'#'), F))
    retain_restored(lambda: t.run(w, F), clean)
    check('TR50', 'the workflow at tool.workflow.path at T modified by one byte: ERROR', "exit 65 with stop "
          "'CONFIG_UNREVIEWED'", o50, o50['exit'] == 65 and o50['stop'] == 'CONFIG_UNREVIEWED')
    # TR51: a symlink, separately a submodule entry, under the package directory
    o51 = {}
    for name, val in (('symlink', ('symlink', 'elsewhere.py')), ('submodule', ('submodule', 'ab' * 20))):
        o51[name] = show(*t.run(t.world(tool_files=dict(hf.TOOL_FILES, **{hf.PKG + 'engine/x.py': val})), F))
        REC.name_last('symlink under tools/ledger_coverage/' if name == 'symlink' else 'submodule entry')
        o51[name + ' (an added entry)'] = show(*t.run(t.world(extra={hf.PKG + 'engine/z': val}), F))
    retain_restored(lambda: t.run(w, F), clean)
    check('TR51', 'a symlink, separately a submodule entry, under the package directory in T\'s tree: ERROR in each '
          'case', "every case exits 65 with stop 'CONFIG_UNREVIEWED'", o51,
          all(o['exit'] == 65 and o['stop'] == 'CONFIG_UNREVIEWED' for o in o51.values()))
    # TR29 at the tool: head branch not main; head_sha the evaluated commit
    a29 = show(*t.run(t.world(run={'head_branch': 'feature'}), F))
    REC.name_last('head_sha on a branch',
                  attested={'message_names': 'head_branch' if 'head branch' in a29['message'] else None})
    wx = t.world()
    wx.h.runs[wx.run_id]['head_sha'] = t.syn.H
    b29 = show(*t.run(wx, F))
    REC.name_last('head_sha is X')
    retain_restored(lambda: t.run(w, F), clean)
    check('TR29-tool', 'a run whose head_sha is not on main (its head branch is not main): ERROR at the tool before any '
          'evaluation; separately a run whose head_sha is the evaluated commit X (no tool there): ERROR',
          "both exit 65 with stop 'CONFIG_UNREVIEWED'; the first names the head branch", [a29, b29],
          a29['exit'] == 65 and a29['stop'] == 'CONFIG_UNREVIEWED' and 'head branch' in a29['message'] and
          b29['exit'] == 65 and b29['stop'] == 'CONFIG_UNREVIEWED')
    # EI1: the checkout differs from T
    ck = w.checkout()
    patched = dict(ck, **{hf.PKG + 'engine/x.py': b'x = 3\n'})
    pyc = dict(ck, **{hf.PKG + 'engine/__pycache__/x.cpython-313.pyc': b'\x00compiled'})
    e1 = {'patched module': show(*t.run(w, F, checkout=patched)), 'bytecode file': show(*t.run(w, F, checkout=pyc)),
          '(countercontrol) the checkout equal to T': show(*t.run(w, F, checkout=ck))}
    equal_checkout = REC.name_last('equal checkout (positive)')
    retain_restored(lambda: t.run(w, F, checkout=ck), equal_checkout)
    check('EI1', 'the tool run directly, without the pre-run check, on a checkout of T in which one tool file differs '
          'from T\'s blob, or that holds a file T does not (a compiled-bytecode file): ERROR at the tool',
          "both mutants exit 65 with stop 'CONFIG_UNREVIEWED' naming the checkout; the equal checkout exits 0", e1,
          all(e1[k]['exit'] == 65 and e1[k]['stop'] == 'CONFIG_UNREVIEWED' and 'checkout' in e1[k]['message']
              for k in ('patched module', 'bytecode file')) and
          e1['(countercontrol) the checkout equal to T']['exit'] == 0,
          cases=[('tool file differs from T, run directly', {}), ('extra bytecode file, run directly', {})])
    # EI2 at the tool
    e2 = {}
    for event in ('pull_request', 'schedule', 'workflow_run'):
        e2[event] = show(*t.run(t.world(run={'event': event}), F))
        REC.name_last(event)
    push_world = t.world(run={'event': 'push'})
    push_code, push_result = t.run(push_world, F)
    e2['(countercontrol) push'] = show(push_code, push_result)
    push_baseline = REC.name_last('push (tool half, positive)',
                                  attested={'outcome': 'NOT_REFUSED' if push_code == 0 else 'REFUSED'})
    retain_restored(lambda: t.run(push_world, F), push_baseline)
    check('EI2', 'a run whose event is pull_request (head in the canonical repository); separately schedule; '
          'separately workflow_run: ERROR at the tool; the consumer half is reported with the acceptance controls',
          "the three events exit 65 with stop 'CONFIG_UNREVIEWED'; a push run exits 0", e2,
          all(e2[k]['exit'] == 65 and e2[k]['stop'] == 'CONFIG_UNREVIEWED'
              for k in ('pull_request', 'schedule', 'workflow_run')) and e2['(countercontrol) push']['exit'] == 0)
    ei4_controls(t, w)
    gv6_controls(t, w)
    gv7_tool_controls(t, w, F)
    ei7_controls(r)
    return t


def ei4_controls(t, w):
    d = t.p.rsplit('/', 1)[0] + '/'
    cfg = t.repo.read(t.c, t.p)
    rv = t.repo.read(t.c, d + 'review.json')
    # a second configuration (another tool pin set) and its review, placed in the plan directory and listed only by
    # the PREREG.md of a second directory
    other = json.loads(cfg)
    other['notes'] = 'a second configuration'
    other['config_id'] = 'synthetic-retirement-config-b'
    ob = sf.jb(other)
    orv = sf.jb(review_record({'schema': 'oi-review-record/1', 'reviewer': sf.REVIEWER, 'method': 'read',
                 'reviewed': {'path': d + 'other.json', 'blob_sha256': sha(ob)},
                 'verdicts': [{'item': other['config_id'], 'verdict': 'accept'}]}))
    second = {'syn/second/PREREG.md': hf.pin_table({'other.json': sha(ob), 'other-review.json': sha(orv)}),
              'syn/second/other.json': ob, 'syn/second/other-review.json': orv,
              d + 'other.json': ob, d + 'other-review.json': orv}
    Fa = t.freeze(listed={t.p: cfg, d + 'review.json': rv}, extra=second)
    out = {'(a) the other configuration in the plan directory': show(*t.run(w, Fa, path=d + 'other.json'))}
    code, res = t.run(w, Fa, args=['--freeze', Fa, '--pin-table', '%s:syn/second/PREREG.md' % Fa],
                      path=d + 'other.json')
    out['(b) a caller argument naming the second PREREG.md'] = {'exit': code, 'result': res}
    Fc = t.freeze(listed={d + 'review.json': rv}, earlier={'config.json': sha(cfg), 'review.json': sha(rv)})
    out['(c) the last Record pins subsection omits the configuration'] = show(*t.run(w, Fc))
    out['(d) no PREREG.md beside the configuration'] = show(*t.run(w, t.c))
    bad = hf.pin_table({'config.json': sha(cfg), 'review.json': sha(rv)}) + b'| `ledger.json` | 0123 |\n'
    out['(d2) a malformed row in the last Record pins subsection'] = show(*t.run(w, t.freeze(prereg=bad)))
    dup = hf.pin_table({'config.json': sha(cfg), 'review.json': sha(rv)}) + ('| `config.json` | `%s` |\n'
                                                                            % sha(b'other')).encode()
    out['(d3) a file listed twice in the last Record pins subsection'] = show(*t.run(w, t.freeze(prereg=dup)))
    out['(countercontrol) the plan\'s own configuration'] = show(*t.run(w, Fa))
    clean = REC.name_last('plan configuration (positive)')
    retain_restored(lambda: t.run(w, Fa), clean)
    ok = all(v['exit'] == 65 and v['stop'] == 'CONFIG_UNREVIEWED' for k, v in out.items() if k[:3] in ('(a)', '(c)',
                                                                                                      '(d)', '(d2',
                                                                                                      '(d3'))
    ok = ok and 'malformed' in out['(d2) a malformed row in the last Record pins subsection']['message'] and \
        'twice' in out['(d3) a file listed twice in the last Record pins subsection']['message']
    check('EI4', 'F holds the plan directory with its PREREG.md and a second directory whose PREREG.md lists another '
          'configuration: (a) that configuration in the plan directory, listed only by the second PREREG.md; (b) a '
          'caller argument naming the second PREREG.md as pin table; (c) the plan PREREG.md whose last Record pins '
          'subsection omits the configuration while an earlier one lists it; (d) no PREREG.md beside the '
          'configuration; separately a malformed row in its last Record pins subsection',
          "(a), (c), (d) and the malformed row exit 65 with stop 'CONFIG_UNREVIEWED'; (b) exits 64 with no result; "
          "the plan's own configuration at the same F exits 0", out,
          ok and out['(b) a caller argument naming the second PREREG.md'] == {'exit': 64, 'result': None} and
          out['(countercontrol) the plan\'s own configuration']['exit'] == 0,
          cases=[(name, {}) for name in ('(a)', '(b)', '(c)', '(d)', 'malformed Record pins row')])


def gv6_controls(t, w):
    """GV6 on in-memory trees (the on-disk cases are in gv_disk_controls): a symlink entry at the configuration's
    path in F, at the pin table's path, at a record's path."""
    d = t.p.rsplit('/', 1)[0] + '/'
    F = t.freeze()
    t.run(w, F)
    clean = REC.name_last('clean regular entries')
    out = {'configuration': show(*t.run(w, t.repo.derive(F, {t.p: ('symlink', 'review.json')}, parents=[t.c]))),
           'pin table': show(*t.run(w, t.repo.derive(F, {d + 'PREREG.md': ('symlink', '../PREREG.md')},
                                                     parents=[t.c])))}
    code, res = t.run(w, t.repo.derive(F, {'syn/rules-allow.json': ('symlink', 'rules-pat.json')}, parents=[t.c]))
    out['record'] = dict(show(code, res), record_invalid=sorted({i['subject'] for i in (res or {}).get('items', [])
                                                                 if i['class'] == 'record-invalid'}))
    retain_restored(lambda: t.run(w, F), clean)
    check('GV6', 'a symlink entry at the configuration\'s path in F; separately at the pin table\'s path; separately '
          'at a record\'s path: refused in each case', "the first two exit 65 with stop 'CONFIG_UNREVIEWED'; the "
          "record is record-invalid (exit 20)", out,
          all(out[k]['exit'] == 65 and out[k]['stop'] == 'CONFIG_UNREVIEWED' for k in ('configuration', 'pin table'))
          and out['record']['exit'] == 20 and 'syn/rules-allow.json' in out['record']['record_invalid'],
          cases=[None, ('symlink at configuration path', {}), ('symlink at pin table path', {}),
                 ('symlink at a record path', {'record': 'syn/rules-allow.json'})])


def gv7_tool_controls(t, w, F):
    out = {}
    t.run(w, F)
    clean = REC.name_last('complete run record')
    for name, how in (('run record read fails', ('fail', 'run')), ('run record incomplete', ('incomplete', 'run'))):
        w2 = t.world()
        getattr(w2.h, how[0]).add(how[1])
        out[name] = show(*t.run(w2, F))
        REC.name_last(name)
    # a host-run class whose run and job records cannot be read, are incomplete, or come from another event
    from ledger_coverage.adapters import deleg_host_run as hr
    cls = {'id': 'ci', 'adapter': 'host-run', 'paths': [], 'params': {'workflow_path': 'wf.yml', 'jobs': ['build']}}
    dl = delmod.Delegation({'schema': 'oi-delegation/1', 'classes': [cls]}, {'host-run': hr})
    X = t.syn.H
    good = [{'run_id': 9, 'workflow_path': 'wf.yml', 'head_sha': X, 'event': 'workflow_dispatch',
             'repository_id': hf.REPO_ID, 'head_repository_id': hf.REPO_ID,
             'jobs': [{'id': 1, 'name': 'build', 'conclusion': 'success'}]}]
    cases = {'good': (set(), set(), good), 'runs read fails': ({'runs'}, set(), good),
             'runs incomplete': (set(), {'runs'}, good),
             'run from a pull_request event': (set(), set(), [dict(good[0], event='pull_request')]),
             'run in a fork': (set(), set(), [dict(good[0], head_repository_id=78)])}
    deleg = {}
    failing_items = []
    observed_hosts = {}
    for name, (fail, inc, runs) in cases.items():
        h = hostmod.MemoryHost()
        h.fail, h.incomplete = set(fail), set(inc)
        h.host_runs = {X: runs}
        env = delmod.Native(t.repo, None, '/nonexistent', X, True, host=h, repo_id=hf.REPO_ID)
        items, report = dl.verify(t.repo, {'scientific_base': X, 'candidate': X, 'freeze': X, 'certified': X,
                                            'ledger_sha256': '0' * 64}, env, {'splices': []})
        deleg[name] = sorted({(i['class'], i['decision']) for i in items})
        observed_hosts[name] = {'runs': runs, 'fail': sorted(fail), 'incomplete': sorted(inc)}
        REC.capture_doc('host-run delegation', control_records.stage_doc(items, operation='delegation',
                                                                        delegated=report), case=name)
        if name != 'good':
            failing_items.extend(items)
    REC.capture_doc('host-run delegation (combined returned items)',
                    control_records.stage_doc(failing_items, operation='delegation'),
                    case='host-run class records incomplete (4 cases)')
    retain_restored(lambda: t.run(w, F), clean)
    out['host-run class'] = deleg
    missing = [('delegated-evidence-missing', 'REVIEW_REQUIRED')]
    check('GV7-tool', 'the host\'s REST API failing or incomplete: the run record (no "chain", ERROR '
          'CONFIG_UNREVIEWED); the run and job records of a host-run class (REVIEW_REQUIRED '
          'delegated-evidence-missing, never PASS); a run of another event or from a fork is not evidence; no '
          'fallback source in any case (the consumer\'s artifact list is reported with the acceptance controls)',
          "both run-record cases exit 65 CONFIG_UNREVIEWED; the host-run class gives no item with the good run and "
          "exactly delegated-evidence-missing in the four other cases", out,
          all(out[k]['exit'] == 65 and out[k]['stop'] == 'CONFIG_UNREVIEWED'
              for k in ('run record read fails', 'run record incomplete')) and
          'host call failed' in out['run record read fails']['message'] and deleg['good'] == [] and
          all(deleg[k] == missing for k in deleg if k != 'good'), files={'host-runs.json': observed_hosts})


# The workflow forms the `uses:` line rule refuses (sec. 6.3 point 5; control EI7), each a complete workflow blob.
_WF_HEAD = 'name: lc\non:\n  workflow_dispatch:\njobs:\n  run:\n    runs-on: ubuntu-24.04\n'
_STEPS = '    steps:\n'
_HEX = '0123456789abcdef0123456789abcdef01234567'
EI7_FORMS = {
    'local action ./.github/actions/x': _STEPS + '      - uses: ./.github/actions/x\n',
    'local reusable workflow': _STEPS + '      - uses: ./.github/workflows/w.yml\n',
    'a tag': _STEPS + '      - uses: owner/action@v4\n',
    'a branch': _STEPS + '      - uses: owner/action@main\n',
    'a quoted key': _STEPS + '      - "uses": owner/action@%s\n' % _HEX,
    'an escaped key': _STEPS + '      - "\\x75ses": ./x\n',
    'a flow mapping': _STEPS + '      - {uses: ./x}\n',
    'a flow sequence': '    steps: [ {"\\x75ses": ./x} ]\n',
    'an anchor and alias': '    x: &a ./x\n' + _STEPS + '      - uses: *a\n',
    'a block scalar': _STEPS + '      - uses: >\n          ./x\n',
    'a complex key': _STEPS + '      - ? uses\n        : ./x\n',
    'an escaped key after a dash and two spaces': _STEPS + '      -  "\\x75ses": ./x\n',
    'a flow mapping after a dash and two spaces': _STEPS + '      -  {"\\x75ses": ./x}\n',
    'a tag after a dash and two spaces': _STEPS + '      -  !!str "\\x75ses": ./x\n',
    'a nested dash': _STEPS + '      - - "\\x75ses": ./x\n',
    'a whole-document flow mapping after ---': None,
    'a tab after the dash': _STEPS + '      -\t"\\x75ses": ./x\n',
    'a tab after a colon before a flow collection': '    steps:\t[ {"\\x75ses": ./x} ]\n',
    'the key in upper case (any letter case)': _STEPS + '      - USES: ./x\n',
    'a local action with a 40-hex suffix': _STEPS + '      - uses: ./.github/actions/x@%s\n' % _HEX,
    'a local reusable workflow with a 40-hex suffix': '    uses: ./.github/workflows/w.yml@%s\n' % _HEX,
    'a parent path with a 40-hex suffix': _STEPS + '      - uses: ../x/y@%s\n' % _HEX,
    'an owner name beginning with a hyphen, with a 40-hex suffix': _STEPS + '      - uses: -foo/bar@%s\n' % _HEX,
}


def ei7_blob(name):
    if name == 'a whole-document flow mapping after ---':
        return ('--- {"jobs": {"run": {"runs-on": "ubuntu-24.04", "steps": [{"\\x75ses": "./x"}]}}}\n').encode()
    return (_WF_HEAD + EI7_FORMS[name]).encode()


def ei7_controls(r):
    tool, cons = {}, {}
    labels = {'local action ./.github/actions/x': 'local action',
              'a whole-document flow mapping after ---': 'whole-document flow mapping',
              'a tab after the dash': 'tab after dash',
              'a tab after a colon before a flow collection': 'tab after colon before flow collection'}
    for name in EI7_FORMS:
        blob = ei7_blob(name)
        t, w, F = with_tool(r, wf=blob)
        code, res = t.run(w, F)
        tool[name] = show(code, res)
        label = labels.get(name, name.removeprefix('a ').removeprefix('an '))
        label = label.replace('after a dash', 'after dash')
        REC.name_last(label, attested={'message_names': 'line rule' if 'uses' in tool[name]['message'] else None})
        cons[name] = bool(checker.uses_line_problems(blob))
    t, w, F = with_tool(r)
    pos = show(*t.run(w, F))
    clean = REC.name_last('conforming 40-hex uses line (positive)')
    retain_restored(lambda: t.run(w, F), clean)
    check('EI7-tool', 'a pinned workflow blob with each form the `uses:` line rule refuses (a local action, a local '
          'reusable workflow, a tag, a branch, a quoted or escaped key, a flow mapping or sequence, an anchor and '
          'alias, a block scalar, a complex key, the forms of review v6.0d B-1, a local action, a local reusable '
          'workflow or a parent path each with a 40-hex suffix, and an owner name beginning with a hyphen): ERROR at '
          'the tool in each case, the blob being the configuration\'s pinned workflow; the consumer half is reported with the acceptance '
          'controls', "every form exits 65 with stop 'CONFIG_UNREVIEWED' naming the line rule, and the rule refuses "
          "each blob; the conforming workflow (a uses line naming an action by a 40-hex id) exits 0",
          {'tool': tool, 'rule': cons, 'positive': pos},
          all(o['exit'] == 65 and o['stop'] == 'CONFIG_UNREVIEWED' and 'uses' in o['message'] for o in tool.values())
          and all(cons.values()) and pos['exit'] == 0 and len(tool) == 23)


# ---- the consumer's acceptance predicate --------------------------------------------------------------------------

def acceptance_controls(r, t):
    w = t.world()
    F = t.freeze()
    code, res = t.run(w, F)
    snap = snapshot_of(res)
    cfg = json.loads(t.repo.read(F, t.p))
    pins = {'config': {'path': t.p, 'blob_sha256': t.s}, 'freeze': F, 'pin_table': snap['pin_table'],
            'adapters': {a['name']: a['module_sha256'] for a in res.get('adapters', [])}, 'tool': cfg['tool'],
            'repository_id': cfg['repository_id']}
    o = r.out()
    code_h, res_h = cli.run(['terms', '--config', '%s:%s' % (t.c, t.p), '--out', o, '--commit', t.syn.H],
                            repo=t.repo, harness=True, stderr=io.StringIO())
    files_h = sorted(os.listdir(o))
    unmarked = copy.deepcopy(res)
    del unmarked['harness']
    relabelled = copy.deepcopy(unmarked)
    relabelled['config']['admission'] = {'mode': 'control-harness', 'snapshot': snapshot_of(res)}
    x11_accept = {'harness result': checker.accept(res_h, code_h, pins), 'simulated-chain result':
                  checker.accept(res, code, pins), 'marker removed': checker.accept(unmarked, code, pins),
                  'relabelled control-harness': checker.accept(relabelled, code, pins)}
    # the restored case: the same harness run again, against the first
    o2 = r.out()
    cli.run(['terms', '--config', '%s:%s' % (t.c, t.p), '--out', o2, '--commit', t.syn.H],
            repo=t.repo, harness=True, stderr=io.StringIO())
    x11_files = {'results.json': {'harness result': {'raw': res_h, 'exit': code_h, 'out_listing': files_h},
                                  'simulated-chain result': {'raw': res, 'exit': code},
                                  'marker removed': {'raw': unmarked, 'exit': code},
                                  'relabelled control-harness': {'raw': relabelled, 'exit': code}},
                 'landing.json': {'used_by_accept': False}, 'snapshot.json': {'snapshot': snap, 'pins': pins},
                 'acceptance.json': x11_accept}
    check('X11', 'a control-harness PASS result presented with the pinned tool and configuration hashes: '
          'non-acceptance; the harness never writes result.json',
          "accept() is false for the harness result, for the simulated-chain result, and for that result with its "
          "harness marker removed, with or without the snapshot (admission not chain); the harness run directory holds control-result.json only",
          {'harness_exit': code_h, 'files': files_h}, code_h == 0 and not checker.accept(res_h, code_h, pins) and
          not checker.accept(res, code, pins) and not checker.accept(unmarked, code, pins) and
          not checker.accept(relabelled, code, pins)
          and files_h == ['control-result.json'],
          cases=[('simulated-chain run', None), ('', None), ('restored', None)],
          attested={'': {'outcome': 'ACCEPTED' if any(x11_accept.values()) else 'NON_ACCEPTANCE',
                         'harness_dir_files': files_h}},
          baseline_of={'restored': ''}, files=x11_files,
          procedure={'name': 'acceptance', 'lib': 'consumer', 'results': 'results.json',
                     'landing_record': 'landing.json', 'snapshot': 'snapshot.json', 'attested': 'acceptance.json'})
    # a chain-labelled copy, the landing record, and the consumer's host checks
    chain = copy.deepcopy(res)
    del chain['harness']
    chain['config']['admission'] = {'mode': 'chain', 'snapshot': snap,
                                    'snapshot_sha256': res['config']['admission']['snapshot_sha256']}
    raw = util.dump_result(chain).encode('utf-8')
    gz = checker.deterministic_gzip(raw)
    w.h.artifacts[(w.run_id, 'ledger-coverage-result')] = sha(raw)
    M = t.repo.derive(w.T, {'notes/later.txt': b'a later commit on main\n'}, parents=[w.T], subject='main')
    landing = {'evaluated': snap.get('evaluated'), 'artifact_name': 'ledger-coverage-result',
               'result_sha256': sha(raw), 'main': M}

    def consumer(raw_=raw, pins_=pins, host=w.h, landing_=landing, repo=t.repo):
        return checker.accept_with_host(raw_, 0, pins_, host, landing_, repo)

    def retain_consumer_case(name, evidence, raw_=raw, pins_=pins, host=w.h, landing_=landing, repo=t.repo):
        accepted = consumer(raw_, pins_, host, landing_, repo)
        result = json.loads(raw_)
        reported = result['config']['admission']['snapshot']
        artifact_digests = [{'run_id': rid, 'name': artifact, 'sha256': digest}
                            for (rid, artifact), digest in sorted(host.artifacts.items())]
        evidence[name] = {'raw_result': raw_.decode('utf-8'), 'input_exit': 0, 'accepted': accepted,
                          'landing': copy.deepcopy(landing_), 'pins': copy.deepcopy(pins_),
                          'snapshot': reported, 'host_runs': copy.deepcopy(host.runs),
                          'host_artifact_digests': artifact_digests,
                          'host_failure_modes': {'failed': sorted(host.fail), 'incomplete': sorted(host.incomplete)},
                          'tool_entries': {path: entry for path, entry in repo.entries(reported['tool_commit']).items()
                                           if path.startswith((hf.PKG, '.github/workflows/')) or path == hf.ENTRY}}
        run = REC.capture_doc('checker.accept_with_host', result, case=name, raw=raw_,
                              attested={'outcome': 'ACCEPTED' if accepted else 'NON_ACCEPTANCE'})
        return accepted, run

    def consumer_cases(cid, description, negative, positive, good=None, aggregate=None):
        evidence, rejected = {}, {}
        for name, variant in negative:
            accepted, _ = retain_consumer_case(name, evidence, **variant)
            rejected[name] = not accepted
        if aggregate is not None:
            REC.capture_doc('aggregate of retained checker.accept_with_host calls', {'rejected': rejected},
                            case=aggregate,
                            attested={'outcome': 'NON_ACCEPTANCE' if all(rejected.values()) else 'ACCEPTED'})
        good = good or {}
        accepted, clean = retain_consumer_case(positive, evidence, **good)
        restored, restoration = retain_consumer_case('restored', evidence, **good)
        restoration['baseline'] = clean
        files = {
            'results.json': {name: {'raw': row['raw_result'], 'exit': row['input_exit']}
                             for name, row in evidence.items()},
            'landings.json': {name: row['landing'] for name, row in evidence.items()},
            'snapshots.json': {name: {k: row[k] for k in ('snapshot', 'pins', 'host_runs', 'host_failure_modes',
                                                          'host_artifact_digests', 'tool_entries')}
                               for name, row in evidence.items()},
            'acceptance.json': {name: row['accepted'] for name, row in evidence.items()},
        }
        check(cid, description, 'consumer refuses the variants and accepts the original and restored cases',
              dict(rejected=rejected, accepted=accepted, restored=restored),
              all(rejected.values()) and accepted and restored, files=files,
              procedure={'name': 'acceptance', 'lib': 'consumer', 'results': 'results.json',
                         'landing_record': 'landings.json', 'snapshot': 'snapshots.json',
                         'attested': 'acceptance.json'})

    def doc_with(**snap_changes):
        d = copy.deepcopy(chain)
        d['config']['admission']['snapshot'].update(snap_changes)
        b = util.dump_result(d).encode('utf-8')
        return b

    def host_with(art_raw=None, **run_changes):
        h = copy.deepcopy(w.h)
        h.runs[w.run_id].update(run_changes)
        if art_raw is not None:
            h.artifacts[(w.run_id, 'ledger-coverage-result')] = sha(art_raw)
        return h
    old_schema = copy.deepcopy(chain)
    old_schema['schema'] = 'oi-ledger-coverage/4'
    # review impl-v6.0e N-2: the /5 schema requires config.admission wherever a result carries config (sec. 5)
    no_adm = copy.deepcopy(chain)
    del no_adm['config']['admission']
    schema_errs = {'chain': schemamod.validate(chain), 'without config.admission': schemamod.validate(no_adm)}
    schema_cases = {'oi-ledger-coverage/5 chain result': chain, 'the same result labelled oi-ledger-coverage/4': old_schema}
    accepted_schemas = {}
    for name, doc in schema_cases.items():
        accepted = checker.accept(doc, 0, pins)
        accepted_schemas[name] = accepted
        REC.capture_doc('checker.accept', doc, case=name,
                        attested={'outcome': 'ACCEPTED' if accepted else 'NON_ACCEPTANCE'})
    for name, short, doc in (('schema validation of the chain result', 'chain', chain),
                             ('schema validation without config.admission', 'without config.admission', no_adm)):
        REC.capture_doc('result schema validation', doc, case=name,
                        attested={'outcome': 'PREDICATE', 'schema_errors': schema_errs[short]})
    v5 = accepted_schemas['oi-ledger-coverage/5 chain result']
    v4 = accepted_schemas['the same result labelled oi-ledger-coverage/4']
    check('ACCEPT-SCHEMA', 'sec. 5: a result of another schema id than oi-ledger-coverage/5 is never acceptable; the '
          '/5 schema requires config.admission in a result that carries config (implementation control)',
          "accept() true for the /5 chain result and false for the same as /4; the schema passes the chain result "
          "and refuses it without config.admission",
          {'v5': v5, 'v4': v4, 'schema': schema_errs},
          v5 and not v4 and not schema_errs['chain'] and
          schema_errs['without config.admission'] == ['$.config: missing admission'],
          files={'inputs.json': {**schema_cases, 'without config.admission': no_adm},
                 'landing.json': {'fixture': landing, 'used_by_accept': False},
                 'snapshot.json': {'snapshot': snap, 'pins': pins},
                 'decisions.json': {'acceptance': accepted_schemas, 'schema_errors': schema_errs}},
          procedure={'name': 'acceptance', 'lib': 'consumer', 'results': 'inputs.json',
                     'landing_record': 'landing.json', 'snapshot': 'snapshot.json', 'attested': 'decisions.json'})
    consumer_cases('TR30', 'the consumer checks the evaluated commits against the landing record', [
        ('evaluated commits differ', {'landing_': dict(landing, evaluated={'commit': '0' * 40})})],
        'matching (positive)')
    gz_bad = checker.deterministic_gzip(raw + b' ')
    expected_digest = landing['result_sha256']

    def compressed_case(name, compressed):
        verified = checker.verify_compressed(compressed, expected_digest)
        contents = gzip.decompress(compressed)
        run = REC.capture_doc('checker.verify_compressed', json.loads(contents), case=name, raw=contents,
                              attested={'outcome': 'LANDING_VERIFIED' if verified else 'LANDING_REFUSED'})
        return verified, run

    exact, exact_run = compressed_case('exact', gz)
    altered, _ = compressed_case('uncompressed sha256 differs', gz_bad)
    restored_gzip = checker.deterministic_gzip(raw)
    restored, restore_run = compressed_case('restored', restored_gzip)
    restore_run['baseline'] = exact_run
    check('TR46', 'a committed compressed result whose uncompressed sha256 differs from the recorded one: refused '
          'at landing', "verify_compressed is true for the exact bytes and false for the altered ones, and the gzip "
          "header carries mtime 0 and operating-system byte 255",
          {'exact': exact, 'altered': altered, 'restored': restored,
           'mtime_zero': gz[4:8] == b'\x00\x00\x00\x00', 'os_byte': gz[9]},
          exact and not altered and restored and restored_gzip == gz and
          gz[4:8] == b'\x00\x00\x00\x00' and gz[9] == 255,
          files={'exact.json.gz': gz, 'altered.json.gz': gz_bad, 'restored.json.gz': restored_gzip,
                 'exact.json': exact_run['result'][1], 'restored.json': restore_run['result'][1],
                 'landing.json': landing, 'snapshot.json': snap},
          procedure={'name': 'landing-verify', 'lib': 'replay', 'runs': ['exact.json', 'restored.json']})
    # consumer halves
    fork_host = copy.deepcopy(w.h)
    fork_host.runs[w.run_id].update(repository_id=78, head_repository_id=78)
    consumer_cases('TR14', 'the consumer rejects a run or a reader outside the configured repository', [
        ('fork', {'host': host_with(repository_id=78, head_repository_id=78)}),
        ('other repository', {'host': host_with(repository_id=79, head_repository_id=79)}),
        ('pull_request from a fork', {'host': host_with(head_repository_id=78, event='pull_request')}),
        ('consumer in a fork', {'host': fork_host})], 'canonical (positive)')
    # TR15 / TR50 / TR28 / TR51 / TR52 / EI7 at the consumer: a T whose files or workflow differ from the pins
    def forged_inputs(**kw):
        w2 = t.world(**kw)
        b = doc_with(tool_commit=w2.T, run=dict(snap['run'], head_sha=w2.T))
        h = host_with(art_raw=b, head_sha=w2.T)
        lnd = dict(landing, result_sha256=sha(b), main=t.repo.derive(w2.T, {}, parents=[w2.T], subject='main'))
        if kw.get('wf_path'):
            h.runs[w.run_id]['workflow_path'] = kw['wf_path']
        return {'raw_': b, 'host': h, 'landing_': lnd}
    equal = forged_inputs()
    extra_file = forged_inputs(extra={hf.PKG + 'engine/y.py': b'y = 1\n'})
    consumer_cases('TR15-consumer', 'the consumer checks the exact workflow path and blob', [
        ('workflow blob differs at T', forged_inputs(wf=hf.WF + b'# a changed step\n')),
        ('same-named workflow at another path', forged_inputs(wf_path='.github/workflows/other/lc.yml'))],
        'workflow equal to its pin (positive)', equal)
    consumer_cases('TR28-consumer', 'the consumer checks every pinned tool blob and the exact path set', [
        ('tool blob differs', forged_inputs(tool_files=dict(hf.TOOL_FILES, **{hf.PKG + 'engine/x.py': b'x = 2\n'}))),
        ('extra file', extra_file)], 'equal (positive)', equal)
    consumer_cases('TR50-consumer', 'the consumer refuses a one-byte workflow difference', [
        ('workflow at tool.workflow.path one byte different', forged_inputs(wf=hf.WF + b'#'))],
        'workflow equal to its pin (positive)', equal)
    consumer_cases('TR51-consumer', 'the consumer requires regular tool entries', [
        ('symlink under tools/ledger_coverage/', forged_inputs(
            tool_files=dict(hf.TOOL_FILES, **{hf.PKG + 'engine/x.py': ('symlink', 'e.py')}))),
        ('submodule entry', forged_inputs(extra={hf.PKG + 'engine/z': ('submodule', 'ab' * 20)}))],
        'regular files only (positive)', equal)
    consumer_cases('TR52-consumer', 'the consumer refuses an additional tool path', [
        ('an additional file under tools/ledger_coverage/ not in tool.files', extra_file)],
        'exactly tool.files (positive)', equal)

    def ei7_inputs(form):
        t7, w7, F7 = with_tool(r, wf=ei7_blob(form))
        cfg7 = json.loads(t7.repo.read(F7, t7.p))
        d7 = copy.deepcopy(chain)
        d7['config']['admission']['snapshot'].update(tool_commit=w7.T, workflow=cfg7['tool']['workflow'],
                                                     run=dict(snap['run'], head_sha=w7.T))
        b7 = util.dump_result(d7).encode('utf-8')
        h7 = host_with(art_raw=b7, head_sha=w7.T)
        return {'raw_': b7, 'pins_': dict(pins, tool=cfg7['tool']), 'host': h7,
                'landing_': dict(landing, result_sha256=sha(b7), main=t7.repo.derive(w7.T, {}, parents=[w7.T])),
                'repo': t7.repo}
    consumer_cases('EI7-consumer', 'the consumer refuses each of the twenty-three workflow forms', [
        (form, ei7_inputs(form)) for form in EI7_FORMS], 'the conforming workflow (positive)',
        aggregate='each workflow form the uses: line rule refuses (23 forms, as EI7-tool)')
    # TR29 at the consumer
    other_tool_result = doc_with(tool_commit=t.syn.H)
    consumer_cases('TR29', "the consumer checks the producing tool commit and main's first-parent chain", [
        ('branch', {'landing_': dict(landing, main=t.syn.H)}),
        ('head_sha is X', {'host': host_with(head_sha=t.syn.H)}),
        ('recorded T differs from head_sha', {'raw_': other_tool_result, 'host': host_with(art_raw=other_tool_result),
                                             'landing_': dict(landing, result_sha256=sha(other_tool_result))})],
        'on chain (positive)')
    # EI2 at the consumer
    consumer_cases('EI2-consumer', 'the consumer rejects runs from disallowed events', [
        (event, {'host': host_with(event=event)}) for event in ('pull_request', 'schedule', 'workflow_run')],
        'push (positive)', {'host': host_with(event='push')})
    # EI3: F, pin table and configuration path against the landing record
    consumer_cases('EI3', 'the consumer checks the freeze, pin table and configuration reference', [
        ('F differs', {'pins_': dict(pins, freeze=t.c)}),
        ('pin table differs', {'pins_': dict(pins, pin_table=dict(pins['pin_table'], blob_sha256='0' * 64))}),
        ('pin table path differs', {'pins_': dict(pins, pin_table=dict(pins['pin_table'], path='syn/second/PREREG.md'))}),
        ('configuration path differs', {'pins_': dict(pins, config=dict(pins['config'], path='syn/cfg/other.json'))})],
        'matching landing record (positive)')
    # GV7 at the consumer; R4-N2 (the result bound to the run's artifact)
    failing = copy.deepcopy(w.h)
    failing.fail.add('artifacts')
    incomplete = copy.deepcopy(w.h)
    incomplete.incomplete.add('artifacts')
    run_fail = copy.deepcopy(w.h)
    run_fail.fail.add('run')
    consumer_cases('GV7-consumer', 'the consumer rejects absent host data and a different artifact hash', [
        ('artifact list fails', {'host': failing}),
        ('incomplete records', {'host': incomplete}),
        ('run record fails', {'host': run_fail}),
        ('R4-N2: the artifact digest differs from the result', {'raw_': raw + b'\n'})],
        'complete host data')
    replay_controls(r, t, F, chain, raw, gz, snap)


def ei5_controls(r):
    t = TR(r)
    w = t.world()
    L1 = t.syn.H
    absent = '1' * 40
    cases = {
        'ls-remote fails': (128, '', L1),
        'ls-remote raises': (None, '', L1),
        'no refs/heads/main line': (0, '%s\trefs/heads/other\n' % L1, L1),
        'more than one line': (0, '%s\trefs/heads/main\n%s\trefs/heads/main\n' % (L1, w.T), L1),
        'not full 40-hex': (0, '%s\trefs/heads/main\n' % L1[:12], L1),
        'unreadable id': (0, '%s\trefs/heads/main\n' % absent, L1),
        "id other than L's first parent": (0, '%s\trefs/heads/main\n' % w.T, L1),
        "unreadable id equal to L's first parent": (0, '%s\trefs/heads/main\n' % absent, absent),
    }
    positive = "one main line equal to L's first parent (countercontrol)"
    clean_input = (0, '%s\tHEAD\n%s\trefs/heads/main\n' % (w.T, L1), L1)

    # the landing check's exit status is mapped from the in-process call, not read from a process exit
    EI5_EXIT_SOURCE = 'mapped: 0 when checker.resolve_main returns, 1 when it raises ValueError (no process exit)'

    def evaluate(name, remote_exit, stdout, first_parent):
        def ls_remote():
            if remote_exit is None:
                raise OSError('no network')
            return remote_exit, stdout

        try:
            resolved = checker.resolve_main(ls_remote, t.repo, first_parent)
            observed = {'resolved': resolved, 'exit_status': 0, 'exit_status_source': EI5_EXIT_SOURCE}
            outcome = 'RESOLVED'
        except ValueError as exc:
            observed = {'error': str(exc), 'exit_status': 1, 'exit_status_source': EI5_EXIT_SOURCE}
            outcome = 'LANDING_REFUSED'
        run = REC.capture_doc('checker.resolve_main', observed, case=name, attested={'outcome': outcome})
        return observed, run

    out = {name: evaluate(name, *args)[0] for name, args in cases.items()}
    out[positive], clean = evaluate(positive, *clean_input)
    out['restored'], restoration = evaluate('restored', *clean_input)
    restoration['baseline'] = clean
    fixtures = {**cases, positive: clean_input, 'restored': clean_input}
    check('EI5', 'before landing, git ls-remote failing; separately returning no refs/heads/main line or more than '
          'one; separately an id that is not a full 40-hex id, or that the verified reader cannot read (including one '
          'equal to L\'s given first parent); separately an id other than L\'s first parent: the landing is refused in '
          'each case',
          "every case is refused; one main line equal to L's first parent resolves to it", out,
          all(out[name]['exit_status'] == 1 for name in cases) and out[positive].get('resolved') == L1 and
          out['restored'] == out[positive],
          files={'ls-remote-fixtures.json': {name: {'exit': code, 'stdout': stdout, 'first_parent': first_parent}
                                            for name, (code, stdout, first_parent) in fixtures.items()},
                 'landing-check-exits.json': {name: v['exit_status'] for name, v in out.items()}},
          procedure={'name': 'landing-resolve', 'lib': 'fixture', 'ls_remote_fixture': 'ls-remote-fixtures.json',
                     'landing_check_exit': 'landing-check-exits.json'})


def o3_controls(r):
    """Review impl-v6.0e D-11 (O-3): the disposable clones of delegated runs check out with the system and global git
    configuration disabled, so a smudge filter defined in either never runs. Each configuration is a separate case:
    the filter in a global configuration file (GIT_CONFIG_GLOBAL), in a system configuration file
    (GIT_CONFIG_SYSTEM), and injected through the caller's environment (GIT_CONFIG_COUNT, GIT_CONFIG_KEY_n,
    GIT_CONFIG_VALUE_n; R6.DELEG.3); in each case the same checkout with that configuration in force runs it (the
    countercontrol), and for the environment case so does Native.clone with its environment stripping disabled."""
    base = tempfile.mkdtemp(prefix='o3-', dir=r.out_root)
    src = os.path.join(base, 'src')
    os.makedirs(src)
    gitb(src, 'init', '-q')
    with open(os.path.join(src, '.gitattributes'), 'w') as f:
        f.write('*.txt filter=smudge-probe\n')
    with open(os.path.join(src, 'a.txt'), 'w') as f:
        f.write('x\n')
    gitb(src, 'add', '.')
    gitb(src, 'commit', '-qm', 'c')
    c = gitb(src, 'rev-parse', 'HEAD')

    def case(scope):
        d = os.path.join(base, scope)
        os.makedirs(d)
        marker, cfg = os.path.join(d, 'MARKER'), os.path.join(d, scope + 'config')
        with open(cfg, 'w') as f:
            f.write('[filter "smudge-probe"]\n\tsmudge = "sh -c \'touch %s; cat\'"\n\trequired = true\n' % marker)
        keys = ('GIT_CONFIG_GLOBAL', 'GIT_CONFIG_SYSTEM', 'GIT_CONFIG_NOSYSTEM', 'GIT_CONFIG_COUNT',
                'GIT_CONFIG_KEY_0', 'GIT_CONFIG_VALUE_0', 'GIT_CONFIG_KEY_1', 'GIT_CONFIG_VALUE_1', 'GIT_TEMPLATE_DIR')
        saved = {k: os.environ.get(k) for k in keys}
        os.environ.pop('GIT_CONFIG_NOSYSTEM', None)
        if scope == 'global':
            os.environ['GIT_CONFIG_GLOBAL'] = cfg
        elif scope == 'system':
            os.environ['GIT_CONFIG_GLOBAL'] = os.devnull
            os.environ['GIT_CONFIG_SYSTEM'] = cfg
        elif scope == 'template':
            # the same filter in the config of a template directory named by GIT_TEMPLATE_DIR (a clone copies it
            # into the new repository's .git/config)
            tpl = os.path.join(d, 'template')
            os.makedirs(tpl)
            shutil.copyfile(cfg, os.path.join(tpl, 'config'))
            os.environ['GIT_CONFIG_GLOBAL'] = os.devnull
            os.environ.pop('GIT_CONFIG_SYSTEM', None)
            os.environ['GIT_TEMPLATE_DIR'] = tpl
        else:
            # the same filter injected through the caller's environment (GIT_CONFIG_COUNT, _KEY_n, _VALUE_n)
            os.environ['GIT_CONFIG_GLOBAL'] = os.devnull
            os.environ.pop('GIT_CONFIG_SYSTEM', None)
            os.environ.update({'GIT_CONFIG_COUNT': '2',
                               'GIT_CONFIG_KEY_0': 'filter.smudge-probe.smudge',
                               'GIT_CONFIG_VALUE_0': "sh -c 'touch %s; cat'" % marker,
                               'GIT_CONFIG_KEY_1': 'filter.smudge-probe.required', 'GIT_CONFIG_VALUE_1': 'true'})
        def take_marker():
            # the marker listing after one step; the marker is removed so that each step is observed on its own
            got = ['MARKER'] if os.path.exists(marker) else []
            if got:
                os.remove(marker)
            return got
        try:
            cl = delmod.Native(gitobj.GitRepo(src), src, os.path.join(d, 'out'), c, True).clone(c)
            native = {'clone': bool(cl), 'file_checked_out': bool(cl) and os.path.exists(os.path.join(cl, 'a.txt')),
                      'marker': os.path.exists(marker)}
            native_markers = take_marker()
            cc = os.path.join(d, 'counter')
            subprocess.run(['git', 'clone', '-q', '--no-local', '--no-checkout', src, cc], capture_output=True)
            rc = subprocess.run(['git', '-C', cc, 'checkout', '-q', '--detach', c], capture_output=True).returncode
            counter = {'checkout_exit': rc, 'marker': os.path.exists(marker)}
            take_marker()
            unstripped = None
            if scope in ('environment', 'template'):
                # the countercontrol on the tool's own path: Native.clone with the stripping disabled (its environment
                # as before R6.DELEG.3's fix: the caller's, system configuration off and global configuration empty;
                # no empty --template) runs the injected filter
                real_env, real_opts = delmod.clone_env, delmod.clone_options
                delmod.clone_env = lambda environ: dict(environ, GIT_CONFIG_NOSYSTEM='1', GIT_CONFIG_GLOBAL=os.devnull)
                delmod.clone_options = lambda: []
                try:
                    try:
                        cl2 = delmod.Native(gitobj.GitRepo(src), src, os.path.join(d, 'out-unstripped'), c,
                                            True).clone(c)
                    except RuntimeError as exc:
                        cl2 = None
                        unstripped_error = str(exc)[:300]
                    else:
                        unstripped_error = None
                finally:
                    delmod.clone_env, delmod.clone_options = real_env, real_opts
                unstripped = {'clone': bool(cl2), 'error': unstripped_error, 'marker': take_marker() == ['MARKER']}
        finally:
            for k, v in saved.items():
                if v is None:
                    os.environ.pop(k, None)
                else:
                    os.environ[k] = v
        return {'native': native, 'countercontrol': counter, 'native_markers': native_markers,
                'unstripped': unstripped}
    out = {scope: case(scope) for scope in ('global', 'system', 'environment', 'template')}
    # the environment case has no expectation row case: it is recorded under its own case names in the control's
    # evidence (R6.DELEG.3; added beside the two cases the expectation states)
    names = {'global': 'filter in a global configuration file', 'system': 'filter in a system configuration file',
             'environment': 'filter injected through GIT_CONFIG_COUNT, GIT_CONFIG_KEY_n and GIT_CONFIG_VALUE_n in the '
                            "caller's environment",
             'template': 'filter in the config of a template directory named by GIT_TEMPLATE_DIR'}
    counter_case = 'plain clone and checkout with that configuration (countercontrol)'
    for scope, o in out.items():
        REC.capture_doc('delegation.Native.clone with the smudge filter in force (%s)' % scope,
                        dict(o['native'], exit_status=None), case=names[scope],
                        attested={'outcome': 'PREDICATE', 'clone_checked_out': o['native']['file_checked_out'],
                                  'marker_written': o['native']['marker']})
    for scope, o in out.items():
        cc_ok = o['countercontrol']['checkout_exit'] == 0 and o['countercontrol']['marker']
        REC.capture_doc('plain git clone and checkout with the smudge filter in force (%s)' % scope,
                        dict(o['countercontrol'], exit_status=None),
                        case=counter_case if scope == 'global' else counter_case + ', ' + scope,
                        attested={'outcome': 'COUNTERCONTROL' if cc_ok else None,
                                  'marker_written': o['countercontrol']['marker']})
    for scope in ('environment', 'template'):
        un = out[scope]['unstripped']
        REC.capture_doc('delegation.Native.clone with the stripping disabled (%s)' % scope, dict(un, exit_status=None),
                        case='Native.clone with the stripping disabled, %s (countercontrol)' % names[scope],
                        attested={'outcome': 'COUNTERCONTROL' if un['marker'] else None,
                                  'marker_written': un['marker']})
    unstripped_all = all(out[sc]['unstripped']['marker'] for sc in ('environment', 'template'))
    # The expectation names lib `oracle`, which DESIGN-r6 sec. 16.4 defines as the tool result against P's retained
    # output; the frozen plan P has no output for a smudge filter, so no oracle output exists. A plain clone run with
    # the clone recipe Native.clone itself uses (delegation.py) would not be independent of the thing under test and
    # is not presented as one. The oracle input is therefore left absent and the row fails on it; the point is for
    # the owner. The native and countercontrol marker measurements above are retained as measured.
    o3_files = {'tool-marker-listing.json': {scope: o['native_markers'] for scope, o in out.items()}}
    # the runner does not record PASS while the input its expectation's library needs is absent
    oracle_output = None
    check('O3-FILTER', 'review impl-v6.0e D-11 (O-3): a git configuration defining a required smudge filter and a '
          'commit whose .gitattributes names it, each case separately: the filter in a global configuration file, '
          'in a system configuration file, injected through the caller\'s environment, and in a template directory\'s '
          'config (GIT_TEMPLATE_DIR); the delegated runs\' disposable clone (Native.clone) checks the commit out '
          'without running the filter (implementation control)',
          "in each case Native.clone checks the commit out and the filter's marker is not written; a plain clone and "
          "checkout of the same commit with that configuration in force writes it (the countercontrol); with the "
          "environment and template cases, Native.clone with its stripping disabled writes it too; the oracle "
          "output the expectation's library names exists (it does not: no output of P for a smudge filter)",
          out,
          all(o['native']['clone'] and o['native']['file_checked_out'] and not o['native']['marker'] and
              o['countercontrol']['checkout_exit'] == 0 and o['countercontrol']['marker'] and
              o['native_markers'] == []
              for o in out.values()) and unstripped_all and oracle_output is not None,
          files=o3_files, procedure={'name': 'smudge-filter', 'lib': 'oracle',
                                     'tool_output': 'tool-marker-listing.json'})


# ---- the verified reader on small on-disk repositories (GV1-GV6) -------------------------------------------------

GIT_ENV = dict(GIT_AUTHOR_NAME='fixture', GIT_AUTHOR_EMAIL='fixture', GIT_COMMITTER_NAME='fixture',
               GIT_COMMITTER_EMAIL='fixture', GIT_AUTHOR_DATE='2026-01-01T00:00:00Z',
               GIT_COMMITTER_DATE='2026-01-01T00:00:00Z', GIT_CONFIG_NOSYSTEM='1', GIT_CONFIG_GLOBAL=os.devnull)


def gitb(d, *a, data=None, check_=True):
    r = subprocess.run(['git', '-C', d] + list(a), input=data, capture_output=True, env=dict(os.environ, **GIT_ENV))
    if check_ and r.returncode:
        raise RuntimeError('git %s: %s' % (' '.join(a[:3]), r.stderr.decode()[-300:]))
    return r.stdout.decode().strip() if r.returncode == 0 else None


class Disk:
    """Writes the commits of an in-memory world into a fresh on-disk repository, as real objects."""

    def __init__(self, d):
        self.d = d
        os.makedirs(d)
        gitb(d, 'init', '-q')
        self.memo = {}

    def blob(self, data):
        return gitb(self.d, 'hash-object', '-w', '--stdin', data=data)

    def tree(self, files):
        top = {}
        for p, v in files.items():
            parts = p.split('/')
            cur = top
            for x in parts[:-1]:
                cur = cur.setdefault(x, {})
            cur[parts[-1]] = v
        return self._tree(top)

    def _tree(self, node):
        lines = []
        for name, v in sorted(node.items()):
            if isinstance(v, dict):
                lines.append('040000 tree %s\t%s' % (self._tree(v), name))
            elif isinstance(v, tuple) and v[0] == 'submodule':
                lines.append('160000 commit %s\t%s' % (v[1], name))
            elif isinstance(v, tuple):
                lines.append('120000 blob %s\t%s' % (self.blob(v[1].encode() if isinstance(v[1], str) else v[1]),
                                                     name))
            else:
                lines.append('100644 blob %s\t%s' % (self.blob(v), name))
        return gitb(self.d, 'mktree', data=('\n'.join(lines) + '\n').encode() if lines else b'')

    def commit(self, ov, cid):
        """The real id of the in-memory commit `cid` of the overlay `ov` (parents first); a commit already in the
        store is its own id."""
        if cid in self.memo:
            return self.memo[cid]
        if cid not in ov.mem:
            return cid
        parents = [self.commit(ov, p) for p in ov.parents(cid)]
        files = ov._files(cid)
        tid = self.tree({p: v for p, v in files.items() if v is not None})
        args = ['commit-tree', tid]
        for p in parents:
            args += ['-p', p]
        real = gitb(self.d, *args, data=(ov.subject(cid) + '\n').encode())
        self.memo[cid] = real
        return real

    def loose(self, oid):
        return os.path.join(self.d, '.git', 'objects', oid[:2], oid[2:])


def disk_world(r, name):
    """The synthetic world (pin, the merge m1, H; the configuration commit c; F; the tool commit T) written into a
    fresh on-disk repository under OUT_DIR. Returns (disk, ids, config path, a run function)."""
    syn = sf.Syn()
    dk = Disk(os.path.join(r.out_root, name))
    real = {k: dk.commit(syn.repo, getattr(syn, k)) for k in ('pin', 'm1', 'H')}
    disk_repo = gitobj.GitRepo(dk.d)
    syn.repo = gitobj.Overlay(disk_repo)
    syn.pin, syn.m1, syn.H = real['pin'], real['m1'], real['H']
    syn.materialize = lambda cid: dk.commit(syn.repo, cid)
    pd = sf.patch_doc(syn.H, [])
    c, p, s, _ = syn.build({'patch_sha': sha(pd), 'files': {'syn/patch.json': pd}})
    w = hf.World(syn.repo, syn.H)
    F = hf.freeze(syn.repo, c, p)
    X = syn.repo.derive(syn.H, {sf.DOC: (sf.TEXT + '\nA closing remark appears.\n').encode()}, parents=[syn.H],
                        subject='candidate')
    ids = dict(real, c=dk.commit(syn.repo, c), F=dk.commit(syn.repo, F), T=dk.commit(syn.repo, w.T),
               X=dk.commit(syn.repo, X))
    ids['M'] = dk.commit(syn.repo, syn.repo.derive(X, {'notes/m.txt': b'main\n'}, parents=[X], subject='main'))
    host = hostmod.MemoryHost()
    host.runs[hf.RUN_ID] = {'repository_id': hf.REPO_ID, 'head_repository_id': hf.REPO_ID, 'event': 'workflow_dispatch',
                            'head_branch': 'main', 'workflow_path': hf.WF_PATH, 'head_sha': ids['T']}

    def run(op='terms', commit=None, extra=(), store=None):
        repo = gitobj.GitRepo(store or dk.d)
        o = r.out()
        argv = [op, '--config', '%s:%s' % (ids['F'], p), '--out', o, '--freeze', ids['F']] + \
            (['--commit', commit or ids['X']] if op == 'terms' else []) + list(extra)
        code, res = cli.run(argv, repo=repo, stderr=io.StringIO(),
                            control={'host': host, 'run_id': hf.RUN_ID, 'repo_id': hf.REPO_ID,
                                     'checkout': {q: hf.TOOL_FILES[q] for q in hf.TOOL_FILES}}, environ={})
        return code, res
    return dk, ids, p, run


def same(a, b):
    """Two results equal as results: canonical JSON, the run directory aside."""
    return a[0] == b[0] and util.canonical(a[1]) == util.canonical(b[1])


def gv_disk_controls(r):
    dk, ids, p, run = disk_world(r, 'gv-store')
    clean = run()
    baseline = REC.name_last('clean store')
    execution_args = ['--scientific-base', ids['H'], '--candidate', ids['X'],
                      '--ledger', '%s:syn/patch.json' % ids['c'], '--main', ids['M']]
    clean_exec = run('execution', extra=execution_args)
    execution_baseline = REC.name_last('clean execution')
    base_ok = clean[0] in (0, 10, 20) and not stop(clean[1])

    def relational_evidence(variant, observations, **extra):
        return {'files': {'clean.json': baseline['result'][1], 'observed.json': variant['result'][1],
                          'observations.json': observations, **extra},
                'procedure': {'name': 'relational', 'lib': 'rel-equal', 'runs': ['clean.json', 'observed.json']}}

    # GV1: replace refs; a ref name
    def copy_store(name):
        d = os.path.join(r.out_root, name)
        shutil.copytree(dk.d, d, symlinks=True)
        return d
    g1 = {}
    d1 = copy_store('gv1-commit')
    fake = gitb(d1, 'commit-tree', gitb(d1, 'rev-parse', ids['m1'] + '^{tree}'), data=b'replacement\n')
    gitb(d1, 'replace', ids['m1'], fake)
    live1 = gitb(d1, 'rev-list', '--count', ids['H'])
    g1['commit of the chain replaced: equal'] = same(run(store=d1), clean)
    changed_commit = REC.name_last('replace ref for an E..H commit', baseline=baseline)
    d1b = copy_store('gv1-blob')
    cfg_blob = gitb(d1b, 'rev-parse', '%s:%s' % (ids['F'], p))
    other_blob = gitb(d1b, 'hash-object', '-w', '--stdin', data=b'{"schema": "substituted"}\n')
    gitb(d1b, 'replace', '-f', cfg_blob, other_blob)
    live1b = gitb(d1b, 'cat-file', '-p', '%s:%s' % (ids['F'], p))
    g1['configuration blob replaced: equal'] = same(run(store=d1b), clean)
    changed_config = REC.name_last('replace ref for the configuration blob', baseline=baseline)
    gitb(dk.d, 'branch', '-f', 'main', ids['X'])
    gitb(dk.d, 'tag', '-f', 'v1', ids['X'])
    by_ref = {}
    for name in ('main', 'v1', 'HEAD', ids['X'][:12], ids['X'].upper()):
        by_ref[name] = show(*run(commit=name))
        REC.name_last('role commit as a ref name' if name == 'main' else 'role supplied as ' + name)
    g1['ref names unresolvable'] = all(v['exit'] == 65 and v['stop'] == 'UNRESOLVABLE' and
                                       'refs are not consulted' in v['message'] for v in by_ref.values())
    g1['(countercontrol) the replace refs are live'] = live1 == '1' and '"substituted"' in (live1b or '')
    retain_restored(run, baseline)
    check('GV1', 'a replace ref that substitutes a commit of the E..H chain, and separately one that substitutes the '
          'configuration\'s blob at F; separately a role commit given as a ref name (main, a tag): the replace refs '
          'are ignored (the result equals that of the same store without them); the ref name is an unresolvable '
          'object (ERROR), refs not being consulted',
          "both replaced stores give results equal to the clean store's; main, a tag, HEAD, an abbreviated and an "
          "upper-case id each exit 65 UNRESOLVABLE; git itself sees both replacements (the controls are live)",
          dict(g1, by_ref=by_ref, clean=show(*clean)), base_ok and all(g1.values()),
          **relational_evidence(changed_commit, g1, **{'configuration-result.json': changed_config['result'][1]}))
    # GV2: a graft file
    d2 = copy_store('gv2')
    with open(os.path.join(d2, '.git', 'info', 'grafts'), 'w') as f:
        f.write(ids['m1'] + '\n')
    live2 = gitb(d2, 'rev-list', '--count', ids['H'])
    g2 = {'equal': same(run(store=d2), clean), 'live': live2 == '1'}
    graft_result = REC.name_last('', baseline=baseline, attested={'git_honours_graft': g2['live']})
    retain_restored(run, baseline)
    check('GV2', 'a graft file that makes a commit of the E..H chain parentless: ignored, the result equals that '
          'without the graft file', "the result equals the clean store's; git itself honours the graft (the "
          "control is live)", g2, base_ok and all(g2.values()), **relational_evidence(graft_result, g2))
    # GV3: a commit-graph recording false parents
    d3 = copy_store('gv3')
    gitb(d3, 'branch', '-f', 'all-m', ids['M'])
    gitb(d3, 'branch', '-f', 'all-f', ids['F'])
    gitb(d3, 'branch', '-f', 'all-t', ids['T'])
    unrelated = gitb(d3, 'commit-tree', gitb(d3, 'mktree', data=b''), data=b'unrelated root\n')
    gitb(d3, 'branch', '-f', 'unrelated', unrelated)
    gitb(d3, 'commit-graph', 'write', '--reachable')
    patched = patch_commit_graph(d3, ids['H'], unrelated)
    live3 = gitb(d3, '-c', 'core.commitGraph=true', 'rev-list', '--first-parent', ids['H'], check_=False)
    merge = gitb(d3, 'commit-tree', gitb(d3, 'rev-parse', ids['X'] + '^{tree}'), '-p', ids['X'], '-p', ids['T'],
                 data=b'a two-parent commit\n')
    g3_parents = gitobj.GitRepo(d3).parents(merge) == [ids['X'], ids['T']]
    terms_equal = same(run(store=d3), clean)
    graph_terms = REC.name_last('', baseline=baseline)
    execution_equal = same(run('execution', store=d3, extra=execution_args), clean_exec)
    graph_execution = REC.name_last('execution with the graph')
    restored_execution_equal = same(run('execution', extra=execution_args), clean_exec)
    restored_execution = REC.name_last('restored execution')
    graph_terms['attested'] = {'terms_and_execution_equal_clean': terms_equal and execution_equal}
    retain_restored(run, baseline)
    g3 = {'parsed parents of a two-parent commit': g3_parents, 'patched': patched,
          'live': bool(live3) and ids['pin'] not in live3.split() and unrelated in live3.split(),
          'terms equal (rule-stale scoping, hp chain)': terms_equal,
          'execution equal (H on M\'s first-parent chain)': execution_equal,
          'restored execution equal': restored_execution_equal}
    check('GV3', 'a commit-graph file recording false parents for a commit between H and M and for the rules\' '
          'recorded_at scoping: ignored; H on M\'s first-parent chain and the rule-stale scoping equal those of the '
          'clean store', "terms and execution results equal the clean store's; git itself follows the false "
          "parent (the control is live)", g3, base_ok and all(g3.values()),
          **relational_evidence(graph_terms, g3, **{'graph-execution.json': graph_execution['result'][1],
                                                  'restored-execution.json': restored_execution['result'][1],
                                                  'clean-execution.json': execution_baseline['result'][1]}))
    # GV4: loose objects that do not hash to their ids
    g4 = {}
    targets = {'configuration blob at F': (gitb(dk.d, 'rev-parse', '%s:%s' % (ids['F'], p)), 'CONFIG_UNREVIEWED'),
               'pin table blob': (gitb(dk.d, 'rev-parse', '%s:%s' % (ids['F'], p.rsplit('/', 1)[0] +
                                                                          '/PREREG.md')), 'CONFIG_UNREVIEWED'),
               'tree of X': (gitb(dk.d, 'rev-parse', ids['X'] + ':doc'), 'UNRESOLVABLE'),
               'commit of E..H': (ids['pin'], 'UNRESOLVABLE'),
               'tool blob at T': (gitb(dk.d, 'rev-parse', '%s:%s' % (ids['T'], hf.PKG + 'engine/x.py')),
                                    'CONFIG_UNREVIEWED'),
               # review impl-v6.0e D-6: the HP chain check reads the HP merge first; ERROR 65 and no PASS, its class
               # either the inconsistent-configuration or the unresolvable-object error
               'HP merge': (ids['m1'], ('CONFIG_INCONSISTENT', 'UNRESOLVABLE'))}
    for name, (oid, want) in targets.items():
        d4 = copy_store('gv4-%d' % len(g4))
        kind = gitb(d4, 'cat-file', '-t', oid)
        raw = subprocess.run(['git', '-C', d4, 'cat-file', kind, oid], capture_output=True).stdout
        if kind == 'commit':
            other = raw[:-2] + bytes([raw[-2] ^ 1]) + raw[-1:]
        elif kind == 'tree':
            other = raw.replace(b's.md', b's.me', 1)
        else:
            other = raw + b' '
        f = dk.loose(oid).replace(dk.d, d4)
        os.chmod(f, 0o644)
        with open(f, 'wb') as fh:
            fh.write(zlib.compress(b'%s %d\x00' % (kind.encode(), len(other)) + other))
        served = subprocess.run(['git', '-C', d4, 'cat-file', kind, oid], capture_output=True)
        pretty = subprocess.run(['git', '-C', d4, 'cat-file', '-p', oid], capture_output=True).returncode == 0
        code4, res4 = run(store=d4)
        REC.name_last(name)
        o = show(code4, res4)
        wants = want if isinstance(want, tuple) else (want,)
        g4[name] = dict(o, want=want, outcome=(res4 or {}).get('outcome'),
                        git_serves_the_content=served.returncode == 0 and served.stdout == other,
                        git_cat_file_p_prints_it=pretty,
                        holds=code4 == 65 and o['stop'] in wants and (res4 or {}).get('outcome') != 'PASS' and
                        served.stdout == other)
    retain_restored(run, baseline)
    check('GV4', 'a loose object whose stored content does not hash to its id, each case separately: the '
          'configuration\'s blob at F, the pin table\'s blob, a tree of X, a commit of E..H, a tool blob at T, the HP '
          'merge: ERROR in each case (CONFIG_UNREVIEWED for an admission or identity read, the unresolvable-object '
          'error otherwise; the HP merge, read first by the HP chain check, CONFIG_INCONSISTENT or the '
          'unresolvable-object error), although git cat-file -p prints the content',
          "each case exits 65 with its stated class and no PASS, and git serves the substituted content (git "
          "cat-file <type>, the "
          "read the store answers; -p is recorded: it prints blobs and commits and refuses the tree)", g4,
          all(v['holds'] for v in g4.values()))
    # GV5: a store lacking a parent a bounded walk needs; a partial store lacking a blob; a shallow store that holds
    # every object the run needs
    d5 = copy_store('gv5-shallow')
    os.remove(dk.loose(ids['m1']).replace(dk.d, d5))
    with open(os.path.join(d5, '.git', 'shallow'), 'w') as f:
        f.write(ids['H'] + '\n')
    def object_count(store):
        return len(gitb(store, 'cat-file', '--batch-all-objects', '--batch-check').splitlines())

    shallow_before = object_count(d5)
    a5 = show(*run(store=d5))
    shallow_after = object_count(d5)
    REC.name_last('shallow boundary inside E..H', attested={'objects_fetched': shallow_after - shallow_before})
    src = copy_store('gv5-source')
    for k in ('c', 'F', 'T', 'X', 'M'):
        gitb(src, 'branch', '-f', 'r-' + k, ids[k])
    gitb(src, 'config', 'uploadpack.allowFilter', 'true')
    gitb(src, 'config', 'uploadpack.allowAnySHA1InWant', 'true')
    d5b = os.path.join(r.out_root, 'gv5-partial')
    subprocess.run(['git', 'clone', '-q', '--no-checkout', '--filter=blob:none', '--mirror', 'file://' + src, d5b],
                   capture_output=True, env=dict(os.environ, **GIT_ENV), check=True)
    before = object_count(d5b)
    b5 = show(*run(store=d5b))
    after = object_count(d5b)
    REC.name_last('partial store lacking a blob', attested={'objects_fetched': after - before})
    d5c = copy_store('gv5-shallow-ok')
    with open(os.path.join(d5c, '.git', 'shallow'), 'w') as f:
        f.write(ids['pin'] + '\n')
    shallow_flag = gitb(d5c, 'rev-parse', '--is-shallow-repository')
    c5 = run(store=d5c)
    minimal = REC.name_last('shallow store holding every needed object', baseline=baseline)
    retain_restored(run, minimal)
    g5 = {'shallow boundary inside E..H': dict(a5, objects_before=shallow_before, objects_after=shallow_after),
          'partial store lacking blobs': dict(b5, objects_before=before,
                                                                                 objects_after=after),
          'shallow store holding every needed object': dict(show(*c5), is_shallow=shallow_flag,
                                                            equal=same(c5, clean))}
    check('GV5', 'a store lacking a parent a bounded walk needs (a shallow store whose boundary lies inside E..H; '
          'separately a partial store lacking a needed blob): ERROR, with no object fetched; a shallow store that '
          'holds every object the run needs proceeds as in a full store',
          "the first two exit 65 (UNRESOLVABLE or CONFIG_UNREVIEWED) and the partial store's object count is "
          "unchanged; the third is a shallow repository whose result equals the full store's", g5,
          a5['exit'] == 65 and b5['exit'] == 65 and before == after and shallow_before == shallow_after and
          shallow_flag == 'true' and same(c5, clean), **relational_evidence(minimal, g5))
    # GV6 on disk: a symlink entry at the configuration's path in F
    d6 = copy_store('gv6')
    tree = gitb(d6, 'rev-parse', ids['F'] + '^{tree}')
    ls = subprocess.run(['git', '-C', d6, 'ls-tree', '-r', '-z', tree], capture_output=True).stdout.split(b'\x00')
    files = {}
    for rec_ in ls:
        if rec_:
            meta, _, path = rec_.partition(b'\t')
            files[path.decode()] = meta.split()[2].decode()
    dk6 = Disk.__new__(Disk)
    dk6.d, dk6.memo = d6, {}
    entries = {q: subprocess.run(['git', '-C', d6, 'cat-file', 'blob', b], capture_output=True).stdout
               for q, b in files.items()}
    entries[p] = ('symlink', 'review.json')
    t6 = dk6.tree(entries)
    F6 = gitb(d6, 'commit-tree', t6, '-p', ids['c'], data=b'freeze\n')
    repo6 = gitobj.GitRepo(d6)
    run()
    clean = REC.name_last('regular configuration entry')
    o = r.out()
    host_reads = []

    class RecordingHost(hostmod.MemoryHost):
        def _need(self, what):
            host_reads.append(what)
            return super()._need(what)

    code6, res6 = cli.run(['terms', '--config', '%s:%s' % (F6, p), '--out', o, '--freeze', F6, '--commit', ids['X']],
                          repo=repo6, stderr=io.StringIO(),
                          control={'host': RecordingHost(), 'run_id': 1, 'repo_id': hf.REPO_ID}, environ={})
    REC.name_last('', attested={'before_host_read': not host_reads})
    retain_restored(run, clean)
    check('GV6-disk', 'a symlink entry (mode 120000) at the configuration\'s path in an on-disk F: refused before '
          'any host read', "exit 65 with stop 'CONFIG_UNREVIEWED'", dict(show(code6, res6), host_reads=host_reads),
          code6 == 65 and stop(res6) == 'CONFIG_UNREVIEWED' and 'not a regular file' in show(code6, res6)['message']
          and not host_reads, files={'host-reads.json': host_reads})


def cache_controls(r):
    """The verified reader's per-commit path and entry caches (implementation controls of the performance
    correction): a corrupted object is refused whether or not the commit's paths are already cached, a refused tree
    leaves nothing cached, and no caller can change a cached mapping."""
    dk, ids, p, run = disk_world(r, 'cache-store')
    X = ids['X']

    def ls_tree(store, c):
        out = subprocess.run(['git', '--no-replace-objects', '-C', store, 'ls-tree', '-r', '-z', '--full-tree', c],
                             capture_output=True).stdout.split(b'\x00')
        got = {}
        for rec_ in out:
            if rec_:
                meta, _, path = rec_.partition(b'\t')
                parts = meta.split()
                if parts[1] == b'blob':
                    got[path.decode()] = parts[2].decode()
        return got

    def predicate(cid, cases, attested, tool_output, oracle_output, exit_status=None):
        # the reader cases as retained evidence: the per-case outcomes (case ''), the values stated for them, and
        # the reader's path map beside git ls-tree's (the oracle library compares the two)
        REC.capture_doc('verified reader cases (conformance_controls.py)', {'cases': cases, 'exit_status': exit_status},
                        case='', attested=dict(attested, outcome='PREDICATE'))
        return {'files': {'tool-output.json': tool_output, 'oracle-output.json': oracle_output},
                'procedure': {'name': 'object-reader', 'lib': 'oracle', 'tool_output': 'tool-output.json',
                              'oracle_output': 'oracle-output.json'}}
    blob = gitb(dk.d, 'rev-parse', '%s:%s' % (X, sf.DOC))
    tree = gitb(dk.d, 'rev-parse', X + ':doc')
    d1 = os.path.join(r.out_root, 'cache-blob')
    shutil.copytree(dk.d, d1, symlinks=True)
    raw = subprocess.run(['git', '-C', d1, 'cat-file', 'blob', blob], capture_output=True).stdout
    f = dk.loose(blob).replace(dk.d, d1)
    os.chmod(f, 0o644)
    with open(f, 'wb') as fh:
        fh.write(zlib.compress(b'blob %d\x00' % (len(raw) + 1) + raw + b' '))

    def refused(fn):
        try:
            fn()
            return 'accepted'
        except gitobj.Unresolvable as exc:
            return 'refused: %s' % str(exc)[:80]
    cold = gitobj.GitRepo(d1)
    warm = gitobj.GitRepo(d1)
    warm_paths = dict(warm.paths(X))
    out = {'blob, paths not cached': refused(lambda: cold.read(X, sf.DOC)),
           'blob, paths already cached': refused(lambda: warm.read(X, sf.DOC)),
           'blob, paths cached, second read': refused(lambda: warm.read(X, sf.DOC)),
           'the cached paths name the blob': warm_paths.get(sf.DOC) == blob}
    d2 = os.path.join(r.out_root, 'cache-tree')
    shutil.copytree(dk.d, d2, symlinks=True)
    rawt = subprocess.run(['git', '-C', d2, 'cat-file', 'tree', tree], capture_output=True).stdout
    ft = dk.loose(tree).replace(dk.d, d2)
    os.chmod(ft, 0o644)
    with open(ft, 'wb') as fh:
        other = rawt.replace(b's.md', b's.me', 1)
        fh.write(zlib.compress(b'tree %d\x00' % len(other) + other))
    rt = gitobj.GitRepo(d2)
    out['tree, first paths call'] = refused(lambda: rt.paths(X))
    out['tree, second paths call (nothing cached by the refusal)'] = refused(lambda: rt.paths(X))
    out['tree, entries call'] = refused(lambda: rt.entries(X))
    out['tool run on the corrupted blob'] = show(*run(store=d1))
    REC.name_last('tool run on the corrupted blob')
    ok = all(str(v).startswith('refused') and 'does not hash' in str(v) for k, v in out.items()
             if k.startswith(('blob,', 'tree,'))) and out['the cached paths name the blob'] and \
        out['tool run on the corrupted blob']['exit'] == 65
    reader = {k: v for k, v in out.items() if k.startswith(('blob,', 'tree,'))}
    ev_cache = predicate('GV-CACHE', out, {
        'reader_cases_refused_with': 'does not hash to its id' if all(
            str(v).startswith('refused') and 'does not hash to its id' in str(v) for v in reader.values()) else None,
        'cached_paths_name_the_blob': out['the cached paths name the blob'],
        'nothing_cached_by_a_refusal':
            str(out['tree, second paths call (nothing cached by the refusal)']).startswith('refused')},
        warm_paths, ls_tree(dk.d, X), exit_status=out['tool run on the corrupted blob']['exit'])
    check('GV-CACHE', 'a corrupted object is refused exactly as before the per-commit caches: a corrupted blob whose '
          'commit\'s paths are already cached, and one whose are not; a corrupted tree on every call, nothing cached '
          'by the refusal; a tool run reading the corrupted blob is ERROR (implementation control)',
          "every reader case refuses with 'does not hash to its id'; the cached paths still name the blob; the tool "
          "run exits 65", out, ok, **ev_cache)
    # callers cannot change a cached mapping
    g = gitobj.GitRepo(dk.d)
    ov = gitobj.Overlay(g)
    Xm = ov.derive(X, {'notes/extra.txt': b'x\n'}, parents=[X])
    attempts = {}
    for name, view in (('GitRepo.paths', g.paths(X)), ('GitRepo.entries', g.entries(X)),
                       ('Overlay.paths (in-memory commit)', ov.paths(Xm)),
                       ('Overlay.entries (in-memory commit)', ov.entries(Xm)),
                       ('Overlay.paths (base commit)', ov.paths(X))):
        before = dict(view)
        tried = []
        for how, act in (('item assignment', lambda v: v.__setitem__(sf.DOC, '0' * 40)),
                         ('item deletion', lambda v: v.__delitem__(sf.DOC)),
                         ('pop', lambda v: v.pop(sf.DOC)), ('update', lambda v: v.update({'a': 'b'})),
                         ('clear', lambda v: v.clear())):
            try:
                act(view)
                tried.append('%s: allowed' % how)
            except (TypeError, AttributeError):
                tried.append('%s: refused' % how)
        copy_ = dict(view)
        copy_[sf.DOC] = '0' * 40
        again = g.paths(X) if name.startswith('GitRepo.paths') else g.entries(X) if name == 'GitRepo.entries' else \
            ov.paths(Xm) if name == 'Overlay.paths (in-memory commit)' else ov.entries(Xm) if \
            name == 'Overlay.entries (in-memory commit)' else ov.paths(X)
        attempts[name] = {'attempts': tried, 'unchanged after the attempts and a mutated copy': dict(again) == before,
                          'same view returned': again is view}
    # the cache is keyed by the exact commit id: a different commit never receives another commit's mapping
    commits = [ids[k] for k in ('pin', 'H', 'c', 'F', 'T', 'X', 'M')]
    keyed = {}
    for order in (commits, list(reversed(commits))):
        g2 = gitobj.GitRepo(dk.d)
        for c in order:
            keyed.setdefault(c, []).append(dict(g2.paths(c)) == ls_tree(dk.d, c))
    distinct = len({tuple(sorted(gitobj.GitRepo(dk.d).paths(c).items())) for c in commits})
    g3 = gitobj.GitRepo(dk.d)
    first, second = g3.paths(ids['X']), g3.paths(ids['M'])
    ov2 = gitobj.Overlay(gitobj.GitRepo(dk.d))
    m1 = ov2.derive(ids['X'], {'notes/one.txt': b'1\n'}, parents=[ids['X']])
    m2 = ov2.derive(ids['X'], {'notes/two.txt': b'2\n'}, parents=[ids['X']])
    ov_ok = 'notes/one.txt' in ov2.paths(m1) and 'notes/one.txt' not in ov2.paths(m2) and \
        'notes/two.txt' in ov2.paths(m2) and 'notes/two.txt' not in ov2.paths(m1) and \
        dict(ov2.paths(ids['X'])) == ls_tree(dk.d, ids['X'])
    keyout = {'each commit\'s cached map equals git ls-tree of that commit, in both read orders': keyed,
              'distinct maps among the seven commits': distinct,
              'X and M (M changes one path) give different views': first is not second and
              'notes/m.txt' in second and 'notes/m.txt' not in first,
              'in-memory commits each get their own map': ov_ok}
    ev_key = predicate('GV-CACHE-KEY', keyout, {
        'cached_map_equals_ls_tree_in_both_orders': all(all(v) for v in keyed.values()),
        'distinct_maps_for_distinct_trees': distinct,
        'X_and_M_views_differ': keyout['X and M (M changes one path) give different views'],
        'in_memory_commits_own_map': ov_ok},
        {c: dict(gitobj.GitRepo(dk.d).paths(c)) for c in commits}, {c: ls_tree(dk.d, c) for c in commits})
    check('GV-CACHE-KEY', 'the path cache is keyed by the exact verified commit id: each commit\'s cached map equals '
          'that commit\'s tree (git ls-tree, replacement disabled), whatever the order in which commits are read; a '
          'different commit never receives another commit\'s map; likewise for in-memory commits (implementation '
          'control)', "every comparison true in both orders; seven commits with different trees give seven distinct "
          "maps; X's and M's views differ in notes/m.txt; the two in-memory commits each see only their own file",
          keyout, all(all(v) for v in keyed.values()) and distinct == 7 and
          keyout['X and M (M changes one path) give different views'] and ov_ok, **ev_key)
    # corruption of the store after a successful read (stated, not claimed as detected): the reader caches every
    # verified object for its lifetime, so the same reader serves the bytes it verified and does not re-read the
    # store; a new reader verifies again and refuses
    d3 = os.path.join(r.out_root, 'cache-after-read')
    shutil.copytree(dk.d, d3, symlinks=True)
    same = gitobj.GitRepo(d3)
    before_bytes = same.read(ids['X'], sf.DOC)
    paths_before = dict(same.paths(ids['X']))
    f3 = dk.loose(blob).replace(dk.d, d3)
    os.chmod(f3, 0o644)
    with open(f3, 'wb') as fh:
        fh.write(zlib.compress(b'blob %d\x00' % (len(raw) + 1) + raw + b' '))
    after_read = {'same reader, read after the corruption': 'served the verified bytes'
                  if same.read(ids['X'], sf.DOC) == before_bytes else 'other bytes',
                  'same reader, paths after the corruption equal': dict(same.paths(ids['X'])) == paths_before,
                  'a new reader': refused(lambda: gitobj.GitRepo(d3).read(ids['X'], sf.DOC))}
    nr = str(after_read['a new reader'])
    ev_after = predicate('GV-CACHE-AFTER-READ', after_read, {
        'same_reader_serves_verified_bytes': after_read['same reader, read after the corruption'] ==
        'served the verified bytes',
        'same_reader_path_map_unchanged': after_read['same reader, paths after the corruption equal'],
        'new_reader_refused_with': 'does not hash to its id' if nr.startswith('refused') and
        'does not hash to its id' in nr else nr},
        paths_before, ls_tree(dk.d, ids['X']))
    check('GV-CACHE-AFTER-READ', 'corruption of the object store after a successful read: within one reader\'s '
          'lifetime it is not re-detected (the reader serves the bytes it verified, from its object cache, which the '
          'reader held before this correction too); a new reader verifies the object again and refuses it '
          '(implementation control; it states the behaviour and claims no detection after a read)',
          "the same reader returns the bytes it verified and the same path map; a new reader refuses with 'does not "
          "hash to its id'", after_read,
          after_read['same reader, read after the corruption'] == 'served the verified bytes' and
          after_read['same reader, paths after the corruption equal'] and
          str(after_read['a new reader']).startswith('refused') and 'does not hash' in after_read['a new reader'],
          **ev_after)
    hows = ['item assignment', 'item deletion', 'pop', 'update', 'clear']
    ev_imm = predicate('GV-CACHE-IMMUTABLE', attempts, {
        'mutation_attempts_refused': [h for h in hows if all('%s: refused' % h in v['attempts']
                                                               for v in attempts.values())],
        'mappings_unchanged': all(v['unchanged after the attempts and a mutated copy'] for v in attempts.values()),
        'same_view_returned': all(v['same view returned'] for v in attempts.values())},
        dict(g.paths(X)), ls_tree(dk.d, X))
    check('GV-CACHE-IMMUTABLE', 'no caller can change a cached path or entry mapping: each is a read-only view '
          '(assignment, deletion, pop, update and clear refused); a mutated copy leaves the cache unchanged; later '
          'calls return the same view (implementation control)',
          "every mutation attempt refused, every mapping unchanged, the same view object returned", attempts,
          all(all(t.endswith('refused') for t in v['attempts']) and v['unchanged after the attempts and a mutated copy']
              and v['same view returned'] for v in attempts.values()), **ev_imm)


def patch_commit_graph(d, commit, new_parent):
    """Rewrites, in the commit-graph file of `d`, the first parent of `commit` to `new_parent` (both must be in the
    graph). Returns True when patched."""
    p = os.path.join(d, '.git', 'objects', 'info', 'commit-graph')
    data = bytearray(open(p, 'rb').read())
    if data[:4] != b'CGPH':
        return False
    nchunks = data[6]
    chunks = {}
    for i in range(nchunks + 1):
        off = 8 + 12 * i
        chunks[bytes(data[off:off + 4])] = int.from_bytes(data[off + 4:off + 12], 'big')
    order = sorted(chunks.items(), key=lambda kv: kv[1])
    oidl = chunks[b'OIDL']
    cdat = chunks[b'CDAT']
    n = (cdat - oidl) // 20
    oids = [bytes(data[oidl + 20 * i:oidl + 20 * (i + 1)]).hex() for i in range(n)]
    if commit not in oids or new_parent not in oids:
        return False
    i, j = oids.index(commit), oids.index(new_parent)
    rec_ = cdat + i * 36
    data[rec_ + 20:rec_ + 24] = j.to_bytes(4, 'big')
    os.chmod(p, 0o644)
    open(p, 'wb').write(bytes(data))
    del order
    return True


# ---- the pre-run pin check and the entry point as subprocess runs (EI6, EI8-EI15) --------------------------------

MARKER = b'''import os as _os
_m = _os.environ.get('PROBE_MARKER_DIR') or '/nonexistent'
open(_os.path.join(_m, 'MARKER-' + __name__.replace('.', '_')), 'w').write(__file__ or '?')
'''
EXT_SRC = br'''#include <Python.h>
#include <stdio.h>
#include <stdlib.h>
static struct PyModuleDef m = {PyModuleDef_HEAD_INIT, "util", NULL, -1, NULL};
PyMODINIT_FUNC PyInit_util(void) {
    const char *d = getenv("PROBE_MARKER_DIR"); char p[4096];
    snprintf(p, sizeof p, "%s/MARKER-extension-util", d ? d : "/nonexistent");
    FILE *f = fopen(p, "w"); if (f) { fputs("so", f); fclose(f); }
    return PyModule_Create(&m);
}
'''


def extract_prerun(blob):
    """The pre-run program of a workflow blob by the rule of sec. 6.3 point 5: the step whose name is exactly
    `pre-run pin check`; its single run: line; the single-quoted argument of -c, verbatim. None unless exactly one
    such step with one such line exists."""
    lines = blob.decode('utf-8').split('\n')
    idx = [i for i, l in enumerate(lines) if re.fullmatch(r'\s*(- )?name: pre-run pin check\s*', l)]
    if len(idx) != 1:
        return None
    i = idx[0]
    ind = len(lines[i]) - len(lines[i].lstrip(' -'))
    runs = []
    for l in lines[i + 1:]:
        if l.strip() and (len(l) - len(l.lstrip(' ')) < ind or l.lstrip().startswith('- ')):
            break
        if re.match(r'\s*run:', l):
            runs.append(l)
    if len(runs) != 1:
        return None
    m = re.fullmatch(r"\s*run: python3 -I -S -B -c '([^']*)'\s*", runs[0])
    return m.group(1) if m else None


def tool_tree():
    """{path: bytes} of the running tool's files (the entry point and the package directory, no bytecode cache)."""
    out = {}
    with open(os.path.join(tools, 'ledger_coverage.py'), 'rb') as f:
        out['tools/ledger_coverage.py'] = f.read()
    pkg = os.path.join(tools, 'ledger_coverage')
    for dp, dn, fn in os.walk(pkg):
        dn[:] = sorted(x for x in dn if x != '__pycache__')
        for n in sorted(fn):
            q = os.path.join(dp, n)
            with open(q, 'rb') as f:
                out['tools/' + os.path.relpath(q, tools).replace(os.sep, '/')] = f.read()
    return out


class EI:
    """A materialized checkout of T under OUT_DIR (a git repository), F with plan/retirement-config.json carrying
    tool.files, and the pre-run program extracted from the workflow."""

    def __init__(self, r, prog):
        self.r = r
        self.prog = prog
        self.base = os.path.join(r.out_root, 'ei-base')
        self.files = tool_tree()
        for q, b in self.files.items():
            f = os.path.join(self.base, q)
            os.makedirs(os.path.dirname(f), exist_ok=True)
            with open(f, 'wb') as fh:
                fh.write(b)
        gitb(self.base, 'init', '-q')
        gitb(self.base, 'add', 'tools')
        gitb(self.base, 'commit', '-q', '-m', 'T')
        self.F = self.freeze(self.files)
        self.n = 0
        self.observations = {}

    def freeze(self, files, cfg=None, where=None):
        doc = cfg if cfg is not None else {'tool': {'files': [{'path': q, 'blob_sha256': sha(b)}
                                                              for q, b in sorted(files.items())]}}
        d = where or self.base
        b = gitb(d, 'hash-object', '-w', '--stdin', data=json.dumps(doc).encode())
        t1 = gitb(d, 'mktree', data=('100644 blob %s\tretirement-config.json\n' % b).encode())
        t2 = gitb(d, 'mktree', data=('040000 tree %s\tplan\n' % t1).encode())
        return gitb(d, 'commit-tree', t2, data=b'F\n')

    def fresh(self, name):
        self.n += 1
        d = os.path.join(self.r.out_root, 'ei-%02d-%s' % (self.n, re.sub(r'[^a-z0-9]+', '-', name.lower())[:40]))
        shutil.copytree(self.base, d, symlinks=True)
        os.makedirs(os.path.join(d, 'm'))
        return d

    def prerun(self, d, ref='refs/heads/main', F=None, cfg='plan/retirement-config.json'):
        env = {'PATH': os.environ.get('PATH', '/usr/bin:/bin'), 'HOME': d, 'PROBE_MARKER_DIR': os.path.join(d, 'm'),
               'F': self.F if F is None else F, 'CFG': cfg, 'GIT_CONFIG_NOSYSTEM': '1',
               'GIT_CONFIG_GLOBAL': os.devnull}
        if ref is not None:
            env['GITHUB_REF'] = ref
        p = subprocess.run([sys.executable, '-I', '-S', '-B', '-c', self.prog], cwd=d, env=env, capture_output=True)
        return p.returncode, p.stdout.decode('utf-8', 'replace'), p.stderr.decode('utf-8', 'replace')

    def entry(self, d, extra=(), flags=('-I', '-S', '-B'), out_name='out'):
        env = {'PATH': os.environ.get('PATH', '/usr/bin:/bin'), 'HOME': d, 'PROBE_MARKER_DIR': os.path.join(d, 'm')}
        out = os.path.join(self.r.out_root, os.path.basename(d) + '-' + out_name)
        p = subprocess.run([sys.executable] + list(flags) + ['tools/ledger_coverage.py', 'purity-lint', '--out', out]
                           + list(extra), cwd=d, env=env, capture_output=True)
        res = os.path.join(out, 'result.json')
        return p.returncode, (open(res, 'rb').read() if os.path.exists(res) else None), p.stderr.decode('utf-8',
                                                                                                         'replace')

    @staticmethod
    def markers(d):
        return sorted(os.listdir(os.path.join(d, 'm')))

    def case(self, name, mutate=None, ref='refs/heads/main', F=None, cfg='plan/retirement-config.json'):
        d = self.fresh(name)
        if mutate:
            got = mutate(d)
            if got is not None and F is None and got.get('F'):
                F = got['F']
        code, stdout, stderr = self.prerun(d, ref, F, cfg)
        line = (stdout + stderr).strip().split('\n')[-1][:160]
        o = {'prerun_exit': code, 'prerun': line}
        raw_result, entry_stderr = None, None
        if code == 0:
            o['entry_exit'], raw_result, entry_stderr = self.entry(d)
        o['markers'] = self.markers(d)
        o['dir'] = d
        self.observations[d] = {'step_stdout': stdout, 'step_stderr': stderr, 'entry_result': raw_result,
                                'entry_stderr': entry_stderr, 'ref': ref, 'freeze': self.F if F is None else F,
                                'config_path': cfg}
        return o


def entry_refusal(d, out, flags, injected=None):
    """Observe imports from interpreter startup through the entry's refusal."""
    probe = '''
import sys
entry, out, injected = sys.argv[1:]
startup = sorted(sys.modules)
requested = []
original = __builtins__.__import__

def observe(name, *args, **kwargs):
    requested.append(name)
    return original(name, *args, **kwargs)

if injected:
    sys.path.insert(0, injected)
path_at_entry = list(sys.path)
sys.argv = [entry, 'purity-lint', '--out', out]
source = compile(open(entry, 'rb').read(), entry, 'exec')
__builtins__.__import__ = observe
try:
    exec(source, {'__name__': '__main__', '__file__': entry})
finally:
    __builtins__.__import__ = original
    print(repr({'startup': startup, 'requested': requested, 'added': sorted(set(sys.modules) - set(startup)),
                'path_at_entry': path_at_entry}))
'''
    cmd = [sys.executable, *flags, '-c', probe, 'tools/ledger_coverage.py', out, injected or '']
    p = subprocess.run(cmd, cwd=d, capture_output=True, text=True,
                       env={'PATH': os.environ.get('PATH', ''), 'PROBE_MARKER_DIR': os.path.join(d, 'm')})
    try:
        imports = ast.literal_eval(p.stdout.strip())
        error = json.loads(p.stderr)
    except (SyntaxError, ValueError):
        imports, error = None, {}
    return {'flags': list(flags), 'checkout': os.path.realpath(d), 'injected': injected,
            'resolved': os.path.realpath(injected) if injected else None,
            'link_target': os.readlink(injected) if injected and os.path.islink(injected) else None,
            'exit': p.returncode, 'imports': imports, 'stderr': p.stderr,
            'result_written': os.path.exists(out)}, error


def ei_controls(r):
    try:
        with open(WORKFLOW, 'rb') as f:
            wf = f.read()
    except OSError as exc:
        for cid in ['EI6'] + ['EI%d' % i for i in range(8, 16)]:
            record(cid, 'the control runs', None, 'the pinned workflow text is missing: %s' % exc, 'FAIL')
        return
    prog = extract_prerun(wf)
    if prog is None:
        for cid in ['EI6'] + ['EI%d' % i for i in range(8, 16)]:
            record(cid, 'the control runs', None, 'no pre-run program extractable by the rule of point 5', 'FAIL')
        return
    e = EI(r, prog)
    engine_util = 'tools/ledger_coverage/engine/util.py'

    def failed(o):
        return o['prerun_exit'] != 0 and 'entry_exit' not in o and not o['markers']

    def check_prerun(cid, expected, predicate, actual, holds, cases, clean_name=None, attest=None):
        """Attach the observed subprocess outputs and a separate rerun of the clean checkout."""
        checked = dict(cases)
        if clean_name is None:
            clean_name = 'clean checkout'
            checked[clean_name] = o8
        clean = checked[clean_name]
        restored = e.case(cid + ' restored')
        checked['restored'] = restored
        runs, evidence = {}, {}
        for name, case in checked.items():
            observed = e.observations[case['dir']]
            raw_result = observed['entry_result']
            outcome = 'PRE_RUN_PASSED' if case['prerun_exit'] == 0 else 'PRE_RUN_FAILED'
            reported = {'outcome': outcome, 'entry_point_ran': 'entry_exit' in case,
                        'marker_written': bool(case['markers'])}
            if 'entry_exit' in case:
                reported['entry_exit'] = case['entry_exit']
            reported.update((attest or {}).get(name, {}))
            result = json.loads(raw_result) if raw_result is not None else {'exit_status': case['prerun_exit']}
            runs[name] = REC.capture_doc('workflow pre-run check', result, case=name, raw=raw_result,
                                         attested=reported)
            evidence[name] = {key: value for key, value in observed.items() if key != 'entry_result'}
        runs['restored']['baseline'] = runs[clean_name]
        same_clean = (e.observations[restored['dir']]['entry_result'] ==
                      e.observations[clean['dir']]['entry_result'] and
                      restored.get('entry_exit') == clean.get('entry_exit') and
                      restored['prerun_exit'] == clean['prerun_exit'] and restored['markers'] == clean['markers'])
        files = {
            'step-exits.json': {name: case['prerun_exit'] for name, case in checked.items()},
            'markers.json': {name: case['markers'] for name, case in checked.items()},
            'entry-invocations.json': {name: {'ran': 'entry_exit' in case, 'exit': case.get('entry_exit')}
                                       for name, case in checked.items()},
            'outputs.json': evidence,
        }
        check(cid, expected, predicate, actual, holds and same_clean, files=files,
              procedure={'lib': 'prerun', 'step_exit': 'step-exits.json', 'marker_listing': 'markers.json',
                         'sentinel': 'entry-invocations.json', 'import_trace': 'outputs.json'})

    # EI8
    o8 = e.case('EI8 clean')
    check_prerun('EI8', 'the pre-run check on a clean checkout of a T equal to the configuration\'s tool.files: the step '
          'passes and the entry point runs (positive control)', "pre-run exit 0 naming every file, entry exit 0, no "
          "marker", o8, o8['prerun_exit'] == 0 and o8['prerun'].startswith('PRE-RUN OK %d ' % len(e.files)) and
          o8.get('entry_exit') == 0 and not o8['markers'], {'': o8}, clean_name='')

    # EI9: an unchecked-hash bytecode file
    def pyc(d):
        import importlib.util as iu
        import marshal
        src = os.path.join(d, engine_util)
        code = compile(MARKER, src, 'exec')
        blob = iu.MAGIC_NUMBER + (1).to_bytes(4, 'little') + iu.source_hash(MARKER) + marshal.dumps(code)
        cache = iu.cache_from_source(src)
        os.makedirs(os.path.dirname(cache), exist_ok=True)
        with open(cache, 'wb') as f:
            f.write(blob)
    o9 = e.case('EI9 pyc', pyc)
    d9 = e.fresh('EI9 countercontrol')
    pyc(d9)
    e.entry(d9)
    o9['countercontrol: the entry point run directly writes the marker'] = e.markers(d9)
    check_prerun('EI9', 'the pre-run check on a checkout holding an unchecked-hash bytecode file for engine/util.py (built '
          'for the running interpreter\'s cache tag) whose code writes a marker: the step fails; the job ends before '
          'the entry point runs; the marker is never written', "pre-run exit nonzero, the entry point not run, no "
          "marker; run without the pre-run step the same tree writes the marker (the probe is live)", o9,
          failed(o9) and bool(o9['countercontrol: the entry point run directly writes the marker']), {'': o9})

    # EI10: an extension module beside the pinned util.py
    cc = shutil.which('cc') or shutil.which('gcc')
    if cc is None:
        # no SKIP (R6.GATE.5) and EI10 admits no NOT RUN: a control that cannot run here fails
        record('EI10', 'the pre-run check fails before the entry point runs; the module\'s init never runs', None,
               'not run: no C compiler in this environment', 'FAIL')
    else:
        import sysconfig
        ext = os.path.join(r.out_root, 'ei-ext')
        os.makedirs(ext, exist_ok=True)
        with open(os.path.join(ext, 'util.c'), 'wb') as f:
            f.write(EXT_SRC)
        so = os.path.join(ext, 'util' + (sysconfig.get_config_var('EXT_SUFFIX') or '.so'))
        built = subprocess.run([cc, '-shared', '-fPIC', '-I', sysconfig.get_paths()['include'], '-o', so,
                                os.path.join(ext, 'util.c')], capture_output=True).returncode == 0

        def so_file(d):
            shutil.copy(so, os.path.join(d, 'tools/ledger_coverage/engine', os.path.basename(so)))
        o10 = e.case('EI10 extension', so_file)
        d10 = e.fresh('EI10 countercontrol')
        so_file(d10)
        e.entry(d10)
        o10['countercontrol: the entry point run directly runs the init'] = e.markers(d10)
        check_prerun('EI10', 'the pre-run check on a checkout holding an extension module beside the pinned engine/util.py: '
              'the step fails before the entry point runs; the module\'s init never runs', "pre-run exit nonzero, "
              "the entry point not run, no marker; without the pre-run step the init runs (the probe is live)",
              dict(o10, built=built), built and failed(o10) and
              bool(o10['countercontrol: the entry point run directly runs the init']), {'': o10},
              attest={'': {'module_init_ran': bool(o10['markers'])}})

    # EI11: the pinned util.py a symlink to a payload outside the package
    def link_util(d):
        with open(os.path.join(d, 'payload.py'), 'wb') as f:
            f.write(MARKER)
        os.remove(os.path.join(d, engine_util))
        os.symlink('../../../payload.py', os.path.join(d, engine_util))
    o11 = e.case('EI11 symlinked module', link_util)
    d11 = e.fresh('EI11 countercontrol')
    link_util(d11)
    e.entry(d11)
    o11['countercontrol'] = e.markers(d11)
    check_prerun('EI11', 'the pre-run check on a checkout in which the pinned path engine/util.py is a symlink to a payload '
          'outside the package: the step fails before the entry point runs; the payload never runs',
          "pre-run exit nonzero naming a non-regular entry, no marker; without the pre-run step the payload runs",
          o11, failed(o11) and 'non-regular' in o11['prerun'] and bool(o11['countercontrol']), {'': o11},
          attest={'': {'payload_ran': bool(o11['markers']),
                       'message_names': 'non-regular entry' if 'non-regular entry' in o11['prerun'] else None}})

    # EI12: the entry point a symlink to tools/evil.py
    def link_entry(d):
        with open(os.path.join(d, 'tools', 'evil.py'), 'wb') as f:
            f.write(MARKER)
        os.remove(os.path.join(d, 'tools', 'ledger_coverage.py'))
        os.symlink('evil.py', os.path.join(d, 'tools', 'ledger_coverage.py'))
    o12 = e.case('EI12 symlinked entry', link_entry)
    d12 = e.fresh('EI12 countercontrol')
    link_entry(d12)
    e.entry(d12)
    o12['countercontrol'] = e.markers(d12)
    check_prerun('EI12', 'the pre-run check on a checkout in which the entry point is a symlink to tools/evil.py: the step '
          'fails before the entry point runs; evil.py never runs', "pre-run exit nonzero, no marker; without the "
          "pre-run step evil.py runs", o12, failed(o12) and bool(o12['countercontrol']), {'': o12},
          attest={'': {'evil_ran': bool(o12['markers'])}})

    # EI13
    def one_byte(d):
        with open(os.path.join(d, engine_util), 'ab') as f:
            f.write(b'#')

    def missing(d):
        os.remove(os.path.join(d, 'tools/ledger_coverage/engine/rules.py'))

    def extra_py(d):
        with open(os.path.join(d, 'tools/ledger_coverage/engine/extra.py'), 'wb') as f:
            f.write(MARKER)

    def fifo(d):
        os.mkfifo(os.path.join(d, 'tools/ledger_coverage/engine/fifo'))

    def tools_link_inside(d):
        os.rename(os.path.join(d, 'tools'), os.path.join(d, 'real'))
        os.symlink('real', os.path.join(d, 'tools'))

    def tools_link_outside(d):
        outside = os.path.join(r.out_root, 'ei-outside-' + os.path.basename(d))
        os.rename(os.path.join(d, 'tools'), outside)
        os.symlink(outside, os.path.join(d, 'tools'))
    o13 = {'pinned file changed': e.case('EI13 one byte', one_byte),
           'pinned file missing': e.case('EI13 missing', missing),
           'extra .py file': e.case('EI13 extra', extra_py),
           'non-regular non-directory entry': e.case('EI13 fifo', fifo),
           'tools symlink inside checkout': e.case('EI13 tools link inside', tools_link_inside),
           'tools symlink outside checkout': e.case('EI13 tools link outside', tools_link_outside),
           'F not fetched': e.case('EI13 F absent', F='1' * 40),
           'configuration absent at F': e.case('EI13 config absent', cfg='plan/none.json'),
           'configuration without tool.files': e.case(
               'EI13 no tool files', F=e.freeze({}, cfg={'tool': {}}))}
    check_prerun('EI13', 'the pre-run check, each case separately: a pinned file changed by one byte; a pinned file missing; '
          'an extra .py file; a directory entry that is neither a regular file nor a directory; tools a symlink to a '
          'real directory inside the checkout, and separately to an absolute path outside it; F not fetched; the '
          'configuration path absent at F; a configuration without tool.files: the step fails in each case before '
          'the entry point runs', "every case: pre-run exit nonzero, the entry point not run, no marker", o13,
          all(failed(o) for o in o13.values()), o13)

    # EI14: the CX-3 tree
    def cx3(d):
        for m in ('hashlib', 're', 'subprocess', 'json'):
            with open(os.path.join(d, 'tools', m + '.py'), 'wb') as f:
                f.write(MARKER)
    # 'reaching the tool' and 'consumer' on the in-memory host over the CX-3 tree (as TR29-tool and TR29 do on the
    # fixture tree): R6.REC.18 point 6. The tool, given a run record whose head_branch is not main, refuses
    # (ERROR CONFIG_UNREVIEWED) before any evaluation; the shadow files are watched through a marker directory. The
    # consumer is given a result produced from the same T' and a main whose first-parent chain does not hold T';
    # its countercontrol is the same result with a main that holds T'.
    cx3_files = {'tools/%s.py' % m: MARKER for m in ('hashlib', 're', 'subprocess', 'json')}
    mdir14 = tempfile.mkdtemp(prefix='ei14-markers-', dir=r.out_root)
    saved14 = os.environ.get('PROBE_MARKER_DIR')
    os.environ['PROBE_MARKER_DIR'] = mdir14
    try:
        t14, w14, F14 = with_tool(r, extra=cx3_files, run={'head_branch': 'feature'})
        a14 = show(*t14.run(w14, F14))
        markers14 = sorted(os.listdir(mdir14))
        REC.name_last('reaching the tool',
                      attested={'message_names': 'head_branch' if 'head branch' in (a14.get('message') or '') else None,
                                'file_executed': bool(markers14)})
        w14.h.runs[w14.run_id]['head_branch'] = 'main'
        code14c, res14c = t14.run(w14, F14)
        REC.name_last("consumer input: the tool run on T' with a head_branch main run record")
        markers14 = sorted(os.listdir(mdir14))
    finally:
        if saved14 is None:
            os.environ.pop('PROBE_MARKER_DIR', None)
        else:
            os.environ['PROBE_MARKER_DIR'] = saved14
    consumer14 = {'input_exit': code14c}
    try:
        snap14 = snapshot_of(res14c)
        cfg14 = json.loads(t14.repo.read(F14, t14.p))
        pins14 = {'config': {'path': t14.p, 'blob_sha256': t14.s}, 'freeze': F14, 'pin_table': snap14['pin_table'],
                  'adapters': {a_['name']: a_['module_sha256'] for a_ in res14c.get('adapters', [])},
                  'tool': cfg14['tool'], 'repository_id': cfg14['repository_id']}
        chain14 = copy.deepcopy(res14c)
        chain14.pop('harness', None)
        chain14['config']['admission'] = {'mode': 'chain', 'snapshot': snap14,
                                          'snapshot_sha256': res14c['config']['admission']['snapshot_sha256']}
        raw14 = util.dump_result(chain14).encode('utf-8')
        w14.h.artifacts[(w14.run_id, 'ledger-coverage-result')] = sha(raw14)
        main_off = t14.repo.derive(t14.syn.H, {'notes/later.txt': b'a later commit on main\n'}, parents=[t14.syn.H],
                                   subject="main without T'")
        main_on = t14.repo.derive(w14.T, {'notes/later.txt': b'a later commit on main\n'}, parents=[w14.T],
                                  subject="main holding T'")
        landing14 = {'evaluated': snap14.get('evaluated'), 'artifact_name': 'ledger-coverage-result',
                     'result_sha256': sha(raw14), 'main': main_off}
        consumer14['accepted_branch'] = checker.accept_with_host(raw14, 0, pins14, w14.h, landing14, t14.repo)
        consumer14['accepted_on_main'] = checker.accept_with_host(raw14, 0, pins14, w14.h,
                                                                  dict(landing14, main=main_on), t14.repo)
        REC.capture_doc('checker.accept_with_host', chain14, case='consumer', raw=raw14,
                        attested={'outcome': 'ACCEPTED' if consumer14['accepted_branch'] else 'NON_ACCEPTANCE'})
    except Exception as exc:
        consumer14['error'] = '%s: %s' % (type(exc).__name__, exc)
    # the observability countercontrol of file_executed: the CX-3 shadow file's bytes as T' holds them, executed
    # directly with the same marker directory variable, write a marker, so an import of it would have been seen. The
    # in-process tool reads T' through git objects and imports nothing from it, so file_executed false there is weak
    # evidence; the substantive evidence that nothing unpinned executes on a branch dispatch is EI14-dispatch (a real
    # dispatch of the pinned workflow, NOT RUN until the owner approves the launch)
    obs_dir = tempfile.mkdtemp(prefix='ei14-observe-', dir=r.out_root)
    shadow_py = os.path.join(obs_dir, 'shadow_json.py')
    with open(shadow_py, 'wb') as f:
        f.write(t14.repo.read(w14.T, 'tools/json.py') or b'')
    os.makedirs(os.path.join(obs_dir, 'm'))
    p_obs = subprocess.run([sys.executable, '-I', '-S', '-B', shadow_py], capture_output=True,
                           env={'PATH': os.environ.get('PATH', ''), 'PROBE_MARKER_DIR': os.path.join(obs_dir, 'm')})
    observed14 = sorted(os.listdir(os.path.join(obs_dir, 'm')))
    REC.capture_doc('the CX-3 shadow file tools/json.py of T\' executed directly (observability countercontrol)',
                    {'exit_status': None, 'exit': p_obs.returncode, 'markers': observed14},
                    case="reaching the tool: the CX-3 shadow file executed directly writes its marker "
                         "(observability countercontrol)",
                    attested={'outcome': 'COUNTERCONTROL' if observed14 else None, 'marker_written': bool(observed14)})
    tool14 = {'run': a14, 'markers': markers14, 'observability_countercontrol': {'exit': p_obs.returncode,
                                                                                'markers': observed14}}
    o14a = e.case('EI14 branch', cx3, ref='refs/heads/feature')
    o14b = e.case('EI14 on main', cx3)
    clean_res = e.entry(e.fresh('EI14 clean reference'))[1]
    d14 = o14b['dir']
    same14 = e.entry(d14, out_name='again')[1] == clean_res
    # the retained cases: the two pre-run halves, and (above) 'reaching the tool' and 'consumer' on the in-memory host
    branch14, main14 = 'pre-run check given GITHUB_REF of a branch (simulated)', 'same file at an on-main T'
    check_prerun('EI14', 'the CX-3 tree, a branch T\' holding the pinned files and unpinned tools/hashlib.py (re.py, '
          'subprocess.py, json.py): dispatched on the branch the pre-run check fails (GITHUB_REF), so nothing runs; '
          'the same files at an on-main T: the pre-run check passes, the files never execute, the run is unaffected '
          '(the tool\'s head_branch refusal and the consumer\'s first-parent walk, on the in-memory host)',
          "branch: pre-run exit nonzero naming GITHUB_REF, no marker; main: pre-run exit 0, entry exit 0, no marker, "
          "and the result equals that of the clean tree; the tool on the in-memory host given head_branch feature: "
          "exit 65 CONFIG_UNREVIEWED naming the head branch, no marker; the consumer refuses the result with a main "
          "not holding T' and accepts it with a main holding T' (countercontrol)",
          {'branch': o14a, 'main': o14b, 'result_equal': same14, 'tool': tool14, 'consumer': consumer14},
          failed(o14a) and 'GITHUB_REF' in o14a['prerun'] and o14b['prerun_exit'] == 0 and
          o14b.get('entry_exit') == 0 and not o14b['markers'] and same14 and
          a14['exit'] == 65 and a14['stop'] == 'CONFIG_UNREVIEWED' and 'head branch' in (a14.get('message') or '') and
          not markers14 and bool(observed14) and consumer14.get('accepted_branch') is False and
          consumer14.get('accepted_on_main') is True,
          {branch14: o14a, main14: o14b}, clean_name=main14,
          attest={branch14: {'message_names': 'GITHUB_REF' if 'GITHUB_REF' in o14a['prerun'] else None},
                  main14: {'file_executed': bool(o14b['markers']), 'result_equal_without_file': same14}})
    # EI14's branch-dispatch half needs a host dispatch of the pinned workflow on a branch holding T' (its
    # expectation admits NOT RUN until that run exists); recorded NOT RUN, with no evidence of its own
    not_run('EI14-dispatch', 'the pinned workflow dispatched on a branch holding T\': the pre-run check fails naming '
            'GITHUB_REF, the entry point never runs, no marker', 'no dispatch of the pinned workflow on a branch '
            'holding T\' has been made; it needs the tool landed and a launch the owner approves')

    # EI15
    def changed_code(d):
        with open(os.path.join(d, engine_util), 'ab') as f:
            f.write(b'\n' + MARKER)
        files = dict(e.files)
        with open(os.path.join(d, engine_util), 'rb') as f:
            files[engine_util] = f.read()
        return {'F': e.freeze(files, where=d)}
    o15 = {'workflow_dispatch on a branch with F prime': e.case('EI15 branch F prime', changed_code,
                                                                                  ref='refs/heads/feature'),
           'GITHUB_REF refs/tags/main': e.case('EI15 tag', ref='refs/tags/main'),
           'GITHUB_REF unset': e.case('EI15 unset', ref=None),
           'F as HEAD': e.case('EI15 HEAD', F='HEAD'),
           'F abbreviated': e.case('EI15 abbreviated', F=e.F[:12]),
           'F upper case': e.case('EI15 upper', F=e.F.upper())}
    counter = e.case('EI15 countercontrol main F prime', changed_code)
    positive = 'plan F on refs/heads/main (countercontrol)'
    check_prerun('EI15', 'the pre-run check, each case separately: a workflow_dispatch run on a branch with F\' a commit '
          'whose configuration pins the branch\'s changed tool code; GITHUB_REF refs/tags/main; F given as HEAD, as '
          'an abbreviated id, or in upper case: the step fails in each case before the entry point runs; with the '
          'plan\'s F on main the step passes (countercontrol EI8)',
          "every case fails with no marker; the same changed tree and F' with GITHUB_REF refs/heads/main passes "
          "the step (the ref test is what refuses), and EI8 passes", dict(o15, countercontrol=counter),
          all(failed(o) for o in o15.values()) and counter['prerun_exit'] == 0 and o8['prerun_exit'] == 0,
          {**o15, 'changed code on main': counter, positive: o8}, clean_name=positive)

    # EI6: unpinned files beside the package never execute; isolation is required before any import
    d6 = e.fresh('EI6 shadow')
    for m in ('hashlib', 're', 'subprocess', 'json', 'importlib'):
        with open(os.path.join(d6, 'tools', m + '.py'), 'wb') as f:
            f.write(MARKER)
    code6, res6, err6 = e.entry(d6, flags=('-I', '-S', '-B', '-v'))
    loaded = sorted(set(re.findall(r"(?:code object from|matches|loaded from) '?([^'\s]+\.(?:pyc|py|so))\b", err6)))
    stdlib = _interpreter_dirs(d6)
    installed = _installed_dirs()
    pinned = {os.path.realpath(os.path.join(d6, q)) for q in e.files}

    def allowed_file(f):
        return ei6_allowed(os.path.realpath(f), pinned, stdlib, installed)
    stray = [f for f in loaded if not allowed_file(f)]
    neg6 = ei6_installed_cases(e, stdlib, installed)
    code6c, res6c, _ = e.entry(e.fresh('EI6 clean reference'))
    same6 = res6 == res6c
    d6b = e.fresh('EI6 no isolation')
    with open(os.path.join(d6b, 'tools', 'json.py'), 'wb') as f:
        f.write(MARKER)
    code_no_i, res_no_i, err_no_i = e.entry(d6b, flags=('-B',))
    marks_no_i = e.markers(d6b)
    # the same refusal traced with -v (a separate run): which modules the interpreter imported. The refusal is before
    # any import of a module not loaded at start when neither json (the first module imported after the check, here
    # shadowed by tools/json.py) nor any ledger_coverage module is imported
    code_no_i_v, _, err_no_i_v = e.entry(d6b, flags=('-B', '-v'), out_name='out-v')
    trace_no_i = sorted(set(re.findall(r"^import '([^']+)'", err_no_i_v, re.M)))
    after_check = [m for m in trace_no_i if m == 'json' or m.startswith('json.') or 'ledger_coverage' in m]
    before_unloaded = code_no_i == 65 and code_no_i_v == 65 and not marks_no_i and not e.markers(d6b) and \
        bool(trace_no_i) and not after_check
    code_no_i2 = e.entry(d6b, flags=('-B', '-E', '-s', '-P'))[0]  # not isolated, no checkout directory on sys.path
    d6c = e.fresh('EI6 checkout on sys.path')
    with open(os.path.join(d6c, 'tools', 'json.py'), 'wb') as f:
        f.write(MARKER)
    external = os.path.join(r.out_root, 'ei6-external')
    os.makedirs(external)
    alias_in = os.path.join(external, 'checkout')
    alias_out = os.path.join(d6c, 'tools', 'external')
    os.symlink(os.path.join(d6c, 'tools'), alias_in)
    os.symlink(external, alias_out)
    isolated = ('-I', '-S', '-B')
    probes = [
        ('ordinary bootstrap', d6b, ('-S', '-B'), os.path.join(d6b, 'tools')),
        ('safe-path bootstrap', d6b, ('-S', '-B', '-E', '-s', '-P'), None),
        ('checkout entry', d6c, isolated, os.path.join(d6c, 'tools')),
        ('link into checkout', d6c, isolated, alias_in),
        ('link out of checkout', d6c, isolated, alias_out),
    ]
    refusals = {}
    for i, (subject, checkout, flags, injected) in enumerate(probes):
        result, error = entry_refusal(checkout, os.path.join(r.out_root, 'ei6-bootstrap-%d' % i), flags, injected)
        refusals[subject] = result
        imports = result['imports']
        before_unloaded = (before_unloaded and result['exit'] == 65 and not result['result_written'] and
                           error.get('exit_status') == 65 and error.get('outcome') == 'ERROR' and
                           (error.get('stop') or {}).get('class') == 'NOT_ISOLATED' and
                           isinstance(imports, dict) and bool(imports['startup']) and not imports['added'] and
                           set(imports['requested']) <= set(imports['startup']))
    checkout_exit = refusals['checkout entry']['exit']
    out6 = {'shadow run': {'exit': code6, 'markers': e.markers(d6), 'stray_imports': stray[:10],
                           'imports_seen': len(loaded), 'result_equal_to_clean': same6},
            'without -I': {'exit': code_no_i, 'markers': marks_no_i},
            'without -I, with -E -s -P (no checkout directory on sys.path)': {'exit': code_no_i2,
                                                                             'markers': e.markers(d6b)},
            'checkout directory on sys.path': {'exit': checkout_exit, 'markers': e.markers(d6c)},
            'installed packages': neg6}
    # the retained cases: the shadow run and the clean reference run as its restored case, and the installed-package
    # predicate cases; the run without -I is retained as its case below (no result.json: R6.OUT.4)
    shadow = 'unpinned shadow modules (tools/hashlib.py, re.py, subprocess.py, json.py, importlib.py) under -I -S -B'
    within = 'tool.files or stdlib (-I -S path less purelib, platlib, site-packages, dist-packages, by real path)'
    run6 = REC.capture_doc('entry point purity-lint, -I -S -B, shadow modules present',
                           json.loads(res6) if res6 else {'exit_status': code6}, case=shadow, raw=res6,
                           attested={'marker_written': bool(e.markers(d6)),
                                     'imported_files_within': within if loaded and not stray else None,
                                     'items_equal_run_without_file': same6})
    # R6.OUT.4 / R6.OUT.6: the run without -I writes no result.json; its retained output is its exit status, its
    # --out listing and its one stderr line, which is the case's result document only when it is one JSON object
    # (the documented form: ERROR with the stop class NOT_ISOLATED)
    try:
        err_doc = json.loads(err_no_i)
    except ValueError:
        err_doc = None
    REC.capture(['python3', '-B', 'tools/ledger_coverage.py', 'purity-lint', '--out',
                 os.path.join(r.out_root, os.path.basename(d6b) + '-out')], code_no_i,
                os.path.join(r.out_root, os.path.basename(d6b) + '-out'), case='without -I, or checkout dir on sys.path',
                stderr=err_no_i if isinstance(err_doc, dict) else None,
                attested={'before_unloaded_import': before_unloaded})
    fx6, cert6 = neg6['fixture package'], neg6['installed package certifi']
    refused6 = fx6['exit'] == 0 and fx6['traced'] > 0 and not fx6['admitted'] and \
        (not cert6['present'] or (cert6['traced'] > 0 and not cert6['admitted']))
    REC.capture_doc('EI6 predicate on traced imports (conformance_controls.ei6_installed_cases)',
                    dict(neg6, exit_status=None), case='fixture and installed-package files',
                    attested={'outcome': 'REFUSED' if refused6 else 'NOT_REFUSED',
                              'self_test_imports_all_accepted': neg6['self-test run']['exit'] == 0 and
                              neg6['self-test run']['out_of_tree_imports'] > 0 and not neg6['self-test run']['refused']})
    REC.capture_doc('entry point purity-lint, -I -S -B, clean checkout', json.loads(res6c) if res6c else
                    {'exit_status': code6c}, case='restored', raw=res6c, baseline=run6)
    files6 = {'entry-exits.json': {shadow: code6, 'without -I': code_no_i,
                                   'without -I, with -E -s -P': code_no_i2, 'checkout directory on sys.path':
                                   checkout_exit, 'restored': code6c},
              'markers.json': {shadow: e.markers(d6), 'without -I': marks_no_i, 'checkout directory on sys.path':
                               e.markers(d6c)},
              'entry-invocations.json': {shadow: {'ran': True, 'exit': code6},
                                         'without -I': {'ran': True, 'exit': code_no_i}},
              'import-trace.json': {'loaded': loaded, 'stray': stray,
                                    'bootstrap_refusals': refusals,
                                    'without -I (-v)': {'exit': code_no_i_v, 'imported': trace_no_i,
                                                        'imported_after_the_check': after_check}},
              'refusal-stderr.json': {'without -I': err_no_i, 'without -I result written': res_no_i is not None}}
    check('EI6', 'the checkout of a T holding, besides the pinned files, unpinned tools/hashlib.py (re.py, '
          'subprocess.py, json.py, importlib.py) whose bodies write a marker: the marker is never written, every '
          'imported module\'s file lies in tool.files or the interpreter\'s standard library, and the run\'s result '
          'equals that without the files; separately the entry point run without -I, or with a checkout directory '
          'on sys.path: ERROR at the entry point, exit 65, before any import of a module not loaded at start. The '
          'standard library is the interpreter\'s -I -S import path less its installed-package directories '
          '(sysconfig purelib and platlib, site-packages and dist-packages, by real path); its predicate refuses an '
          'installed-package import (a fixture package in a site-packages directory under a standard-library '
          'directory, and an installed package of the interpreter where one is present) and accepts every import of '
          'a real -I -S -B self-test run',
          "shadow run (the workflow's flags -I -S -B): exit 0, no marker, no imported file outside the pins and the "
          "interpreter's standard library, result equal; "
          "without -I and with the checkout on sys.path: exit 65 and no marker (json.py shadows the first module "
          "imported after the check); installed packages: no allowed directory is or lies under an installed-package "
          "directory, every traced file of the fixture package's import (and of the installed package's, where "
          "present) is refused, and every out-of-tree import of the self-test run is accepted", out6,
          code6 == 0 and not out6['shadow run']['markers'] and not stray and loaded and same6 and
          code_no_i == 65 and not marks_no_i and before_unloaded and isinstance(err_doc, dict) and
          (err_doc.get('stop') or {}).get('class') == 'NOT_ISOLATED' and code_no_i2 == 65 and not e.markers(d6b) and checkout_exit == 65 and not out6['checkout directory on sys.path'][
              'markers'] and neg6['holds'],
          files=files6, procedure={'lib': 'prerun', 'step_exit': 'entry-exits.json', 'marker_listing': 'markers.json',
                                   'sentinel': 'entry-invocations.json', 'import_trace': 'import-trace.json'})


# the directory names under which an interpreter keeps installed packages (EI6)
INSTALLED_NAMES = ('site-packages', 'dist-packages')
_TRACE = r"(?:code object from|matches|loaded from) '?([^'\s]+\.(?:pyc|py|so))\b"


def ei6_allowed(rf, pinned, stdlib, installed):
    """EI6's predicate on the real path of one imported file: a pinned file, or a file under a directory of the
    interpreter's -I -S import path that is neither at or under an installed-package directory nor below a
    site-packages or dist-packages directory inside that directory."""
    if rf in pinned:
        return True
    if any(rf == i or rf.startswith(i + os.sep) for i in installed):
        return False
    for s in stdlib:
        if rf.startswith(s + os.sep) and not any(n in INSTALLED_NAMES for n in rf[len(s) + 1:].split(os.sep)[:-1]):
            return True
    return False


def _installed_dirs():
    """The real paths of the interpreter's installed-package directories: sysconfig's purelib and platlib under
    every scheme it defines, site's site-packages and user site-packages, and each site-packages or dist-packages
    directory on its import path without -S."""
    prog = ('import sys, json, sysconfig, site\n'
            'd = []\n'
            'for s in sysconfig.get_scheme_names():\n'
            '    try:\n'
            '        p = sysconfig.get_paths(s)\n'
            '    except Exception:\n'
            '        continue\n'
            '    d += [p.get("purelib"), p.get("platlib")]\n'
            'd += list(site.getsitepackages()) + [site.getusersitepackages()]\n'
            'print(json.dumps(d))')
    p = subprocess.run([sys.executable, '-I', '-S', '-c', prog], cwd='/', capture_output=True, text=True)
    q = subprocess.run([sys.executable, '-I', '-c', 'import sys, json; print(json.dumps(sys.path))'], cwd='/',
                       capture_output=True, text=True)
    out = {os.path.realpath(x) for x in json.loads(p.stdout) if x}
    for x in json.loads(q.stdout):
        rx = os.path.realpath(x) if x else ''
        if rx and any(n in INSTALLED_NAMES for n in rx.split(os.sep)):
            out.add(rx)
    return out


def ei6_installed_cases(e, stdlib, installed):
    """EI6's negative control on its own predicate: the allowed directories hold no installed-package directory;
    a traced import of a fixture package from a site-packages directory (a symlink to dist-packages, as CPython lays
    it out) inside a standard-library-like directory is refused; a traced import of an installed package of the
    interpreter (certifi, where present) is refused; every out-of-tree import of a real -I -S -B self-test run is
    accepted."""
    out = {}
    bad_dirs = sorted(s for s in stdlib if any(s == i or s.startswith(i + os.sep) for i in installed) or
                      any(n in INSTALLED_NAMES for n in s.split(os.sep)))
    out['allowed directories at or under an installed-package directory'] = bad_dirs
    root = os.path.join(e.r.out_root, 'ei6-installed')
    lib = os.path.join(root, 'lib', 'python3')
    os.makedirs(os.path.join(lib, 'dist-packages', 'ei6fixture'))
    with open(os.path.join(lib, 'dist-packages', 'ei6fixture', '__init__.py'), 'w') as f:
        f.write('X = 1\n')
    os.symlink('dist-packages', os.path.join(lib, 'site-packages'))
    prog = 'import sys; sys.path.insert(0, %r); import ei6fixture' % os.path.join(lib, 'site-packages')
    p = subprocess.run([sys.executable, '-I', '-S', '-B', '-v', '-c', prog], cwd=root, capture_output=True,
                       text=True, env={'PATH': os.environ.get('PATH', '')})
    rlib = os.path.realpath(lib)
    fx = sorted({os.path.realpath(f) for f in re.findall(_TRACE, p.stderr)
                 if os.path.realpath(f).startswith(rlib + os.sep)})
    out['fixture package'] = {'exit': p.returncode, 'traced': len(fx),
                              'admitted': [f for f in fx if ei6_allowed(f, set(), set(stdlib) | {rlib}, installed)]}
    q = subprocess.run([sys.executable, '-I', '-B', '-v', '-c', 'import certifi'], cwd=root, capture_output=True,
                       text=True, env={'PATH': os.environ.get('PATH', '')})
    if q.returncode == 0:
        cf_ = sorted({os.path.realpath(f) for f in re.findall(_TRACE, q.stderr)
                      if os.sep + 'certifi' + os.sep in os.path.realpath(f)})
        out['installed package certifi'] = {'present': True, 'traced': len(cf_),
                                            'admitted': [f for f in cf_ if ei6_allowed(f, set(), stdlib, installed)]}
    else:
        out['installed package certifi'] = {'present': False}
    d = e.fresh('EI6 self-test imports')
    so = os.path.join(e.r.out_root, 'ei6-selftest-out')
    t = subprocess.run([sys.executable, '-I', '-S', '-B', '-v', 'tools/ledger_coverage.py', 'self-test', '--out', so],
                       cwd=d, capture_output=True, text=True, env={'PATH': os.environ.get('PATH', '')})
    rd = os.path.realpath(d)
    ext = sorted({os.path.realpath(f) for f in re.findall(_TRACE, t.stderr)
                  if not os.path.realpath(f).startswith(rd + os.sep)})
    out['self-test run'] = {'exit': t.returncode, 'out_of_tree_imports': len(ext),
                            'refused': [f for f in ext if not ei6_allowed(f, set(), stdlib, installed)][:10]}
    cert = out['installed package certifi']
    out['holds'] = (not bad_dirs and p.returncode == 0 and len(fx) > 0 and not out['fixture package']['admitted'] and
                    (not cert['present'] or (cert['traced'] > 0 and not cert['admitted'])) and
                    t.returncode == 0 and len(ext) > 0 and not out['self-test run']['refused'])
    return out


def _interpreter_dirs(checkout):
    """The real paths of the interpreter's own import path under the workflow's flags -I -S (-S leaves the runner
    image's installed packages off sys.path; sec. 6.3 residual trust), none of which may lie inside the checkout.
    Installed-package directories inside these are excluded by EI6's predicate (ei6_allowed)."""
    p = subprocess.run([sys.executable, '-I', '-S', '-c', 'import sys, json; print(json.dumps(sys.path))'], cwd='/',
                       capture_output=True, text=True)
    dirs = {os.path.realpath(x) for x in json.loads(p.stdout) if x}
    root = os.path.realpath(checkout)
    return {x for x in dirs if not (x == root or x.startswith(root + os.sep))}


def config_lint_controls(r):
    """Sec. 16.2 and 16.6 at load (implementation controls of the configuration lint for `tool`, `repository_id`,
    `retirement` and the record kinds), through the control harness and through the simulated chain."""
    syn = sf.Syn()
    pd = sf.patch_doc(syn.H, [])
    base = {'patch_sha': sha(pd), 'files': {'syn/patch.json': pd}}
    pins = hf.tool_pins()
    outside = dict(pins, files=pins['files'] + [{'path': 'tools/other.py', 'blob_sha256': '0' * 64}])
    no_entry = dict(pins, files=[f for f in pins['files'] if f['path'] != hf.ENTRY])
    twice = dict(pins, files=pins['files'] + pins['files'][:1])
    auth_doc = {'schema': 'oi-owner-authorization/1', 'record_id': 'a', 'author': sf.WRITER, 'supersedes': None}
    variants = {'tool.files names a path outside the tool': {'tool': outside},
                'tool.files omits the entry point': {'tool': no_entry},
                'tool.files names a path twice': {'tool': twice},
                'tool.workflow without a sha256': {'tool': dict(pins, workflow={'path': hf.WF_PATH})},
                'repository_id zero': {'repository_id': 0},
                'repository_id a string': {'repository_id': '77'},
                'tool missing': {'drop': ['tool']},
                'retirement.owner present': {'extra': {'retirement': {'name': 'synthetic', 'issue': 'none',
                                                                       'owner': 4242}}},
                'a record of the retired kind oi-owner-authorization/1': {'records_extra': {'syn/auth.json': auth_doc}}}
    out = {}
    for name, v in variants.items():
        c, p, s_, _ = syn.build(dict(base, **v))
        out[name] = show(*r.cli(syn.repo, ['terms', '--commit', syn.H], c, p, s_, harness=True))
        REC.name_last(name)
    c, p, s_, _ = syn.build(base)
    out['(countercontrol) the valid configuration'] = show(*r.cli(syn.repo, ['terms', '--commit', syn.H], c, p, s_,
                                                                  harness=True))
    REC.name_last('the valid configuration (countercontrol)')
    check('CONFIG-LINT', 'sec. 16.2 lint and sec. 16.6: tool.files naming a path outside the entry point and the package, '
          'omitting the entry point or naming a path twice; a workflow pin without its sha256; repository_id not a '
          'positive integer; tool missing; a retirement field other than name and issue; a record of a kind the design '
          'does not define (the retired oi-owner-authorization/1): ERROR CONFIG_INVALID in each case (implementation '
          'control)', "every variant exits 65 CONFIG_INVALID; the valid configuration exits 0", out,
          all(v['exit'] == 65 and v['stop'] == 'CONFIG_INVALID' for k, v in out.items()
              if not k.startswith('(countercontrol)')) and out['(countercontrol) the valid configuration']['exit'] == 0)


def meaning_controls(r):
    """Sec. 5, "Class meanings" (B-4): every result carries the fixed table, and every item, site state and file
    state in one of the four classes quotes its meaning."""
    from ledger_coverage.engine import outcome as oc
    syn = sf.Syn()
    edits = [('# synthetic', ['# synthetic', '', 'Preface line one.', '', 'Preface line two.'])]
    X, c, p, s_ = sf.y_world(syn, edits)
    Xb = syn.repo.derive(syn.H, {sf.DOC: sf.apply_text(sf.TEXT, [('# synthetic', ['# synthetic', '', 'Preface uno.',
                                                                                 '', 'Preface line two.'])]).encode()},
                         parents=[syn.H])
    seg = ['--segment', '%s..%s' % (syn.pin, syn.H), '--segment', '%s..%s=%s:syn/patch.json' % (syn.H, Xb, c)]
    code, res = r.cli(syn.repo, ['coverage', '--commit', Xb, '--check', 'zc'] + seg, c, p, s_)
    REC.name_last('coverage result')
    found, missing = [], []

    def walk(x):
        if isinstance(x, dict):
            for key in ('class', 'status', 'state'):
                if x.get(key) in oc.class_meaning:
                    (found if x.get('meaning') == oc.class_meaning[x[key]] else missing).append(x[key])
            for k, v in x.items():
                if k != 'config':
                    walk(v)
        elif isinstance(x, list):
            for v in x:
                walk(v)
    walk(res or {})
    code2, res2 = r.cli(syn.repo, ['record', '--pin', syn.pin, '--record', syn.H], c, p, s_)
    REC.name_last('error result')
    table_equal = (res or {}).get('class_meaning') == (res2 or {}).get('class_meaning') == oc.class_meaning
    error_with_table = code2 == 65 and (res2 or {}).get('class_meaning') == oc.class_meaning
    meanings = {'class_meaning_table_equal_in_every_result': table_equal,
                'classed_items_quoting_meaning_min': min(1, len(found)),
                'classed_items_missing_meaning': len(missing),
                'error_result_carries_table': error_with_table}
    REC.capture_doc('result class-meaning audit', {'quoted_classes': found, 'missing_classes': missing},
                    case='', attested={'outcome': 'PREDICATE', **meanings})
    check('B4-MEANING', 'sec. 5 (B-4): every result carries class_meaning, identical in each; every item and state '
          'of the classes authorized-replacement, authorized-removal, unauthorized-edit or unauthorized-change quotes '
          'its meaning from the table (implementation control)',
          "a coverage run with an unauthorized-edit item and an ERROR result both carry the table equal to "
          "outcome.class_meaning; at least one classed item or state, and every one quotes its meaning",
          {'coverage_exit': code, 'quoted': sorted(set(found)), 'missing': missing[:5], 'error_result_table':
           (res2 or {}).get('class_meaning') == oc.class_meaning},
          table_equal and error_with_table and 'unauthorized-edit' in found and not missing,
          files={'coverage.json': res, 'error.json': res2, 'meanings.json': meanings},
          procedure={'name': 'class-meaning', 'lib': 'ast', 'inputs': ['coverage.json', 'error.json'],
                     'attested': 'meanings.json'})


def simrun(r, syn, c, p, argv_tail, op):
    """The run of `op` with the configuration at the plan commit F (c plus a PREREG.md beside the configuration)
    on the in-memory host world (a control artefact, never "chain")."""
    w = hf.World(syn.repo, syn.H)
    F = hf.freeze(syn.repo, c, p)
    argv = [op, '--config', '%s:%s' % (F, p), '--out', r.out()] + w.args(F) + list(argv_tail(F))
    return cli.run(argv, repo=syn.repo, stderr=io.StringIO(), control=w.control(w.checkout()), environ={})

def f2_controls(r):
    """F2: a side-change class record referenced by the configuration is chain-linted in op C (sec. 6.3): one
    without a review record gives FAIL record-invalid and classifies nothing."""
    def scenario(case, with_class, reviewed):
        syn = sf.Syn()
        edits = [('# synthetic', ['# synthetic', '', 'Preface line one.'])]
        pd = sf.patch_doc(syn.H, edits)
        base = {'patch_sha': sha(pd), 'files': {'syn/patch.json': pd}}
        c0, p0, s0, f0 = syn.build(base)
        recs = json.loads(f0[p0])['records']
        M = syn.repo.derive(syn.H, {'notes/side.txt': b'side change on main\n'}, parents=[syn.H], subject='M')
        cls = {'schema': 'oi-side-change-classes/1', 'record_id': 'syn-classes', 'author': sf.WRITER,
               'supersedes': None,
               'classes': [{'id': 'notes', 'prefixes': ['notes/'], 'reason': 'synthetic',
                            'pins': [{'path': 'notes/side.txt', 'git_blob': syn.repo.blob_id(M, 'notes/side.txt'),
                                      'blob_sha256': sha(b'side change on main\n')}]}]}
        files = dict(base['files'])
        v = dict(base)
        if with_class:
            cb = sf.jb(cls)
            files['syn/classes.json'] = cb
            extra = [{'kind': 'side-change-classes', 'path': 'syn/classes.json', 'blob_sha256': sha(cb)}]
            if reviewed:
                extra += syn.chain(files, 'syn/classes.json', sf.REVIEWER)
            v['extra'] = {'records': recs + extra}
        v['files'] = files
        c, p, s, f = syn.build(v)
        X = syn.repo.derive(syn.H, {sf.DOC: sf.apply_text(syn.repo.read(syn.H, sf.DOC).decode(), edits).encode()},
                            parents=[syn.H], subject='X')
        code, res = simrun(r, syn, c, p, lambda F: ['--scientific-base', syn.H, '--candidate', X, '--ledger',
                                                    '%s:syn/patch.json' % F, '--main', M], 'execution')
        REC.name_last(case, bindings={'class_record': 'syn/classes.json', 'side_path': 'notes/side.txt'})
        items = sorted({(i['class'], str(i.get('subject'))) for i in (res or {}).get('items', [])
                        if i['class'] in ('record-invalid', 'side-change-unclassified', 'base-drift')})
        return {'exit': code, 'outcome': (res or {}).get('outcome'), 'stop': stop(res), 'items': items}
    out = {'none': scenario('no class record', False, False),
           'reviewed': scenario('reviewed class record (positive)', True, True),
           'unreviewed': scenario('class record without a review record', True, False)}
    un = out['unreviewed']
    check('R3-F2', 'op C: a side-change class record referenced by the configuration with no review record: FAIL '
          'record-invalid, and the side change stays unclassified; the reviewed record classifies it; with no class '
          'record it is side-change-unclassified',
          "unreviewed: exit 20, record-invalid on syn/classes.json and side-change-unclassified on notes/side.txt; "
          "reviewed: no record-invalid and no side-change-unclassified; none: side-change-unclassified", out,
          un['exit'] == 20 and ('record-invalid', 'syn/classes.json') in un['items'] and
          ('side-change-unclassified', 'notes/side.txt') in un['items'] and
          not out['reviewed']['items'] and
          ('side-change-unclassified', 'notes/side.txt') in out['none']['items'])


def _r4_class_scenario(r, case, cls_mut=None, verdicts=None):
    """Op C over a synthetic side change on main and a configuration-referenced side-change class record with its
    review (the given verdicts; one accept for class `notes` by default)."""
    syn = sf.Syn()
    edits = [('# synthetic', ['# synthetic', '', 'Preface line one.'])]
    pd = sf.patch_doc(syn.H, edits)
    base = {'patch_sha': sha(pd), 'files': {'syn/patch.json': pd}}
    c0, p0, s0, f0 = syn.build(base)
    recs = json.loads(f0[p0])['records']
    M = syn.repo.derive(syn.H, {'notes/side.txt': b'side change on main\n'}, parents=[syn.H], subject='M')
    cls = {'schema': 'oi-side-change-classes/1', 'record_id': 'syn-classes', 'author': sf.WRITER,
           'supersedes': None,
           'classes': [{'id': 'notes', 'prefixes': ['notes/'], 'reason': 'synthetic',
                        'pins': [{'path': 'notes/side.txt', 'git_blob': syn.repo.blob_id(M, 'notes/side.txt'),
                                  'blob_sha256': sha(b'side change on main\n')}]}]}
    if cls_mut:
        cls_mut(cls)
    files = dict(base['files'])
    cb = sf.jb(cls)
    files['syn/classes.json'] = cb
    ref = {'path': 'syn/classes.json', 'blob_sha256': sha(cb)}
    vs = verdicts if verdicts is not None else [{'item': 'notes', 'verdict': 'accept'}]
    rv = review_record({'schema': 'oi-review-record/1', 'reviewer': sf.REVIEWER, 'reviewed': ref, 'method': 'read',
          'verdicts': vs})
    files['syn/classes.review.json'] = sf.jb(rv)
    extra = [{'kind': 'side-change-classes', 'path': 'syn/classes.json', 'blob_sha256': sha(cb)},
             {'kind': 'review', 'path': 'syn/classes.review.json',
              'blob_sha256': sha(files['syn/classes.review.json'])}]
    v = dict(base, files=files, extra={'records': recs + extra})
    c, p, s, f = syn.build(v)
    X = syn.repo.derive(syn.H, {sf.DOC: sf.apply_text(syn.repo.read(syn.H, sf.DOC).decode(), edits).encode()},
                        parents=[syn.H], subject='X')
    try:
        code, res = simrun(r, syn, c, p, lambda F: ['--scientific-base', syn.H, '--candidate', X, '--ledger',
                                                    '%s:syn/patch.json' % F, '--main', M], 'execution')
    except Exception as exc:
        return {'exit': 'EXCEPTION', 'exception': '%s: %s' % (type(exc).__name__, exc)}
    REC.name_last(case, bindings={'class_record': 'syn/classes.json', 'side_path': 'notes/side.txt'},
                  attested={'no_exception': code != 71, 'exit_not_in': [] if code == 71 else [71]})
    its = (res or {}).get('items', [])
    return {'exit': code, 'stop': stop(res),
            'record_invalid': sorted(str(i.get('subject')) for i in its if i['class'] == 'record-invalid'),
            'unclassified': sorted(str(i.get('subject')) for i in its if i['class'] == 'side-change-unclassified')}


def r4_b3_controls(r):
    """B3: every list entry of a reviewed record carries its id field; a record where one does not is record-invalid
    and its verdicts cannot fall back to the record id."""
    def second_without_id(c):
        c['classes'].append({'prefixes': ['other/'], 'reason': 'x', 'pins': []})

    def none_with_id(c):
        for k in c['classes']:
            k.pop('id')
    acc = lambda *ids: [{'item': i, 'verdict': 'accept'} for i in ids]  # noqa: E731
    positive = 'C0 ids and one verdict per class (positive)'
    out = {positive: _r4_class_scenario(r, positive)}
    for case, mutant, verdicts in (
            ('C9 a second class without id', second_without_id, acc('syn-classes')),
            ('C9b with a verdict for the class that has one', second_without_id, acc('notes', 'syn-classes')),
            ('C8 no class has an id', none_with_id, acc('syn-classes'))):
        out[case] = _r4_class_scenario(r, case, mutant, verdicts)
    bad = [v for k, v in out.items() if k != positive]
    pos = out[positive]
    check('R4-B3', 'a side-change class record one of whose classes lacks its id field (C9, and C9b with a verdict '
          'for the class that has one), or all of whose classes lack it (C8), is record-invalid (sec. 6.3: one '
          'verdict per item id; a missing field is record-invalid); no verdict on the record id stands in for the '
          'per-item verdicts; the side change stays unclassified; no exception; the record with ids and one verdict '
          'per class classifies the side change',
          "C9, C9b, C8: exit 20, record-invalid on syn/classes.json, notes/side.txt unclassified; C0: exit 10, no "
          "record-invalid, nothing unclassified", out,
          all(o['exit'] == 20 and 'syn/classes.json' in o['record_invalid'] and 'notes/side.txt' in o['unclassified']
              for o in bad) and
          pos.get('exit') == 10 and not pos.get('record_invalid') and not pos.get('unclassified'))


def r4_b3_duplicate_controls(r):
    """B3 (duplicates): an item id given to two items of a record, or two verdicts for one item, is record-invalid;
    two classes of a class record sharing an id are ERROR CONFIG_INCONSISTENT (S7, Z11), also in chain mode."""
    from ledger_coverage.engine import records as rec

    def lint(case, ids, verdicts):
        d = {'schema': 'oi-hit-classification/1', 'record_id': 'h', 'author': 'session.fixture-writer-a', 'supersedes': None,
             'classifications': [{'id': i} for i in ids]}
        db = util.canonical(d)
        ref = {'path': 'r/h.json', 'blob_sha256': sha(db)}
        rb = util.canonical(review_record({'schema': 'oi-review-record/1', 'reviewer': 'session.fixture-reviewer-b', 'reviewed': ref,
                             'method': 'read', 'verdicts': [{'item': i, 'verdict': v} for i, v in verdicts]}))
        ov, root, ents = idf_.unit_store([('r/h.json', db), ('r/h.review.json', rb)])
        rb = ents[1][1]
        st = rec.Store(ents, ov, [root])
        observed = rec.lint_chain(ref, st, {sha(x) for x in (db, rb)})
        REC.capture_doc('records.lint_chain', {'problems': observed, 'record': db.decode('utf-8'),
                                             'review': rb.decode('utf-8')}, case=case,
                        attested={'outcome': 'LINT_FAIL' if observed else 'LINT_PASS'})
        return observed

    def dup_class(c):
        c['classes'].append(dict(c['classes'][0], prefixes=['other/']))
    acc = [{'item': 'notes', 'verdict': 'accept'}]
    positive = 'lint: distinct ids, one verdict each (positive)'
    out = {case: lint(case, ids, verdicts) for case, ids, verdicts in (
        (positive, ['a', 'b'], [('a', 'accept'), ('b', 'accept')]),
        ('lint: id given to two items', ['a', 'a'], [('a', 'accept')]),
        ('lint: two verdicts for one item', ['a', 'b'], [('a', 'accept'), ('b', 'reject'), ('b', 'accept')]))}
    out['op C: two classes with one id'] = _r4_class_scenario(r, 'op C: two classes with one id', dup_class, acc + acc)
    out['op C: two verdicts for one class'] = _r4_class_scenario(
        r, 'op C: two verdicts for one class', None, [{'item': 'notes', 'verdict': 'reject'}] + acc)
    pos = out[positive]
    two = out['op C: two verdicts for one class']
    check('R4-B3-DUP', 'an item id given to more than one item of a record, or an item given more than one verdict, '
          'makes the record record-invalid; a class record defining one class id twice is ERROR CONFIG_INCONSISTENT '
          '(S7, Z11) in chain mode; distinct ids with one verdict each lint clean',
          "the positive lint is empty; the duplicate-id lint names the id; the duplicate-verdict lint reports it; "
          "op C with the duplicate class id stops 65 CONFIG_INCONSISTENT; op C with two verdicts for notes is exit "
          "20 with record-invalid on syn/classes.json and notes/side.txt unclassified", out,
          pos == [] and any('more than one item' in x for x in out['lint: id given to two items']) and
          any('more than one verdict' in x for x in out['lint: two verdicts for one item']) and
          out['op C: two classes with one id'].get('exit') == 65 and
          out['op C: two classes with one id'].get('stop') == 'CONFIG_INCONSISTENT' and
          two.get('exit') == 20 and 'syn/classes.json' in two.get('record_invalid', []) and
          'notes/side.txt' in two.get('unclassified', []))


def r5_n6_controls(r):
    """N6: a side-change class record whose `classes` is an object, not a list, is record-invalid (sec. 6.3, a field
    error), never an internal error."""
    def as_object(c):
        c['classes'] = {'notes': c['classes'][0]}
    got = _r4_class_scenario(r, 'classes is an object', as_object)
    pos = _r4_class_scenario(r, 'classes is a list (positive)')
    check('R5-N6', 'a side-change class record referenced by the configuration whose classes field is an object: '
          'FAIL record-invalid, the side change unclassified, no exception and no INTERNAL exit; the record with a '
          'class list classifies it',
          "object: exit 20, record-invalid on syn/classes.json, notes/side.txt unclassified; list: exit 10, nothing "
          "record-invalid or unclassified", {'object': got, 'list': pos},
          got.get('exit') == 20 and 'syn/classes.json' in got.get('record_invalid', []) and
          'notes/side.txt' in got.get('unclassified', []) and pos.get('exit') == 10 and
          not pos.get('record_invalid') and not pos.get('unclassified'))


def _show(code, res):
    return {'exit': code, 'stop': stop(res), 'message': ((res or {}).get('stop') or {}).get('message', '')[:200],
            'record_invalid': sorted({str(i.get('subject')) for i in (res or {}).get('items', [])
                                      if i['class'] == 'record-invalid'})}

PAT = 'syn/rules-pat.json'
LINEAGE_KINDS = {
    'oi-hp-adjudication/1': 'HP',
    'oi-context-adjudication/1': 'context',
    'oi-hit-classification/1': 'hit classification',
    'oi-term-rules/2': 'rule',
    'oi-scope/1': 'scope',
    'oi-side-change-classes/1': 'side-change class',
    'oi-reconciliation/1': 'reconciliation',
    'oi-retirement-config/1': 'configuration',
}


def retain_lineage_lint(case, ref, problems, **facts):
    """Retain the in-process lint diagnostics with the record item's normal tool classification."""
    from ledger_coverage.engine import outcome as oc
    items = []
    if problems:
        items.append(oc.make_item('RECORD', 'record-invalid', ref['path'], None,
                                  {'sha': ref['blob_sha256'], 'why': problems[0]}, detail=problems))
    REC.capture_doc('record lineage lint', control_records.stage_doc(items, operation='record-lint', **facts),
                    case=case, bindings={'record': ref['path']},
                    attested={'walk_terminates': True})


def _chain(files, path, verdict='accept', review=True):
    """The review record of the record at `path` (written into `files`); returns its reference for the
    configuration."""
    from ledger_coverage.engine import records as rec
    doc = json.loads(files[path])
    ref = {'path': path, 'blob_sha256': sha(files[path])}
    rp = path[:-5] + '.review.json'
    files.pop(rp, None)
    out = []
    if review:
        files[rp] = sf.jb(review_record({'schema': 'oi-review-record/1', 'reviewer': sf.REVIEWER, 'reviewed': ref, 'method': 'read',
                           'verdicts': [{'item': i, 'verdict': verdict} for i in rec.item_ids(doc)]}))
        out.append({'kind': 'review', 'path': rp, 'blob_sha256': sha(files[rp])})
    return out


def _variant_doc(files, src, dst, sup=None, **fields):
    """A rule file at `dst`: the record at `src` with `supersedes` naming `sup` (a path in `files`) and the given
    fields changed (None removes a field)."""
    doc = json.loads(files[src])
    if sup is not None:
        doc['supersedes'] = {'path': sup, 'blob_sha256': sha(files[sup])}
    for k, v in fields.items():
        if v is None:
            doc.pop(k, None)
        else:
            doc[k] = v
    files[dst] = sf.jb(doc)
    return dst


class LN:
    """A synthetic configuration whose rule files form `supersedes` chains, run in the full chain on an in-memory
    host world (sec. 6.3, DI-2)."""

    def __init__(self, r, variant=None):
        self.r = r
        self.syn = sf.Syn()
        pd = sf.patch_doc(self.syn.H, [])
        v = dict({'patch_sha': sha(pd), 'files': {'syn/patch.json': pd}}, **(variant or {}))
        _, self.p, _, files = self.syn.build(v)
        # the commit is rebuilt in place of H (commit), so the reviews are bound again there
        self.files = {q: idf_.unbind(b) for q, b in files.items()}
        self.cfg = json.loads(self.files[self.p])
        for x in self.cfg['records']:
            if x.get('path') in files and files[x['path']] != self.files[x['path']]:
                x['blob_sha256'] = sha(self.files[x['path']])

    def use_rules(self, replace, extra_records=()):
        """The configuration uses the rule files `replace` maps to (old path -> new path, or None to drop), with
        their chains in `extra_records`; the dropped files' own chains are no longer referenced."""
        dropped = set(replace)
        rules = []
        for ref in self.cfg['rules']:
            if ref['path'] in replace:
                if replace[ref['path']] is not None:
                    rules.append({'path': replace[ref['path']], 'blob_sha256': sha(self.files[replace[ref['path']]])})
            else:
                rules.append(ref)
        self.cfg['rules'] = rules
        stems = {q[:-5] for q in dropped}
        self.cfg['records'] = [x for x in self.cfg['records'] if not any(x['path'].startswith(st + '.')
                                                                         for st in stems)
                               and x.get('kind') != 'superseded-rules'] + list(extra_records)

    def add_rules(self, path, extra_records):
        self.cfg['rules'].append({'path': path, 'blob_sha256': sha(self.files[path])})
        self.cfg['records'] += list(extra_records)

    def commit(self, extra_cfg_files=None):
        cb = sf.jb(self.cfg)
        self.files[self.p] = cb
        d = self.p.rsplit('/', 1)[0] + '/'
        cref = {'path': self.p, 'blob_sha256': sha(cb)}
        rv = sf.jb(review_record({'schema': 'oi-review-record/1', 'reviewer': sf.REVIEWER, 'reviewed': cref, 'method': 'read',
                    'verdicts': [{'item': self.cfg['config_id'], 'verdict': 'accept'}]}))
        self.files[d + 'review.json'] = rv
        for q, b in (extra_cfg_files or {}).items():
            self.files[q] = b(cref) if callable(b) else b
        c, _f = idf_.commit_bound(self.syn.repo, self.syn.H, self.files, self.syn.repo.parents(self.syn.H),
                                 self.syn.repo.subject(self.syn.H), config_path=self.p)
        self.cfg = json.loads(self.files[self.p])
        return c, sha(self.files[self.p])

    def run(self, **kw):
        c, csha = self.commit(**kw)
        code, res = simrun(self.r, self.syn, c, self.p, lambda F: ['--commit', self.syn.H], 'terms')
        o = _show(code, res)
        o['rule_files'] = [x['path'] for x in (res or {}).get('rule_files', [])]
        o['why'] = {str(i.get('subject')): ' | '.join(map(str, i.get('detail') or [i.get('evidence', {}).get('why')]))
                    [:400] for i in (res or {}).get('items', []) if i['class'] == 'record-invalid'}
        return o


def _invalid(o, path, word=None):
    return o['exit'] == 20 and path in o['record_invalid'] and (word is None or word in o['why'].get(path, ''))


def _clean(o, path):
    return o['exit'] == 0 and path in o['rule_files'] and not o['record_invalid']


def allow_rule_limits(r):
    """Exercise the allow-rule limits with byte-bound synthetic record reviews."""
    allow_path = 'syn/rules-allow.json'
    pattern_path = 'syn/rules-pat.json'

    def changed_allow(fields, label):
        runner = LN(r)
        doc = json.loads(runner.files[allow_path])
        doc['rules'][0].update(fields)
        body = sf.jb(doc)
        runner.files[allow_path] = body
        digest = sha(body)
        for ref in runner.cfg['rules']:
            if ref['path'] == allow_path:
                ref['blob_sha256'] = digest
        for ref in runner.cfg['records']:
            path = ref['path']
            if path in ('syn/rules-allow.review.json', 'syn/rules-allow.widen.json'):
                review = json.loads(runner.files[path])
                review['reviewed']['blob_sha256'] = digest
                runner.files[path] = sf.jb(review)
                ref['blob_sha256'] = sha(runner.files[path])
        result = runner.run()
        REC.name_last(label, bindings={'rule_file': allow_path})
        return result

    _, doc = sf.Syn().rule_files()
    matcher = doc['rules'][0]['matcher']
    minimum = {sense: changed_allow({'matcher': dict(matcher, literal=literal)},
                                  'an allow rule whose matcher.literal is shorter than 8 characters and '
                                  + sense + ' the trigger')
               for sense, literal in (('contains', 'Axiom Z'), ('does not contain', 'named'))}
    check('RULE-MINLIT', 'both short allow-rule literals are refused',
          'each mutated rule file gives record-invalid for the minimum literal length', minimum,
          all(_invalid(obs, allow_path, 'at least eight characters') for obs in minimum.values()))

    allow = changed_allow({'fingerprints': [], 'max_instances': 0},
                          'an allow rule with zero fingerprints and max_instances equal to the fingerprint count')
    deny = LN(r).run()
    REC.name_last('a deny rule, which carries no fingerprints (positive)',
                  bindings={'rule_file': pattern_path})
    check('RULE-ZEROFP', 'an allow rule needs a fingerprint and a deny rule needs none',
          'the mutated allow file is record-invalid and the unchanged deny file is admitted',
          {'allow': allow, 'deny': deny},
          _invalid(allow, allow_path, 'at least one fingerprint') and _clean(deny, pattern_path))


def _ln_pat_v2(r, sup=PAT, dst='syn/rules-pat-v2.json', chain_kw=None, setup=None, case=None, **fields):
    """R2 at `dst`, superseding `sup`, used by the configuration in place of the pattern rule file."""
    x = LN(r)
    if setup is not None:
        setup(x)
    _variant_doc(x.files, PAT, dst, sup=sup, **fields)
    refs = _chain(x.files, dst, **(chain_kw or {}))
    x.use_rules({PAT: dst}, refs)
    observed = x.run()
    REC.name_last(case, bindings={'record': dst})
    return observed


def ln1_ln8(r):
    from ledger_coverage.engine import records as rec
    # LN1: in memory, for each kind of S4a; and in a run, for a rule file
    out = {}
    for k, case in LINEAGE_KINDS.items():
        idf = 'config_id' if k == 'oi-retirement-config/1' else 'record_id'
        entries = []

        def chained(path, doc):
            db = util.canonical(doc)
            ref = {'path': path, 'blob_sha256': sha(db)}
            rv = util.canonical(review_record({'schema': rec.review_schema, 'reviewer': 'session.fixture-rv', 'reviewed': ref, 'method': 'read',
                                 'verdicts': [{'item': doc[idf], 'verdict': 'accept'}]}))
            entries.extend([(path, db), (path + '.review', rv)])
            return ref
        pref = chained('r/p.json', {'schema': k, idf: 'p', 'author': 'session.fixture-w', 'supersedes': None})
        sref = chained('r/s.json', {'schema': k, idf: 's', 'author': 'session.fixture-w', 'supersedes': pref})
        ov, root, entries = idf_.unit_store(entries)
        st = rec.Store(entries, ov, [root])
        probs = rec.lint_chain(sref, st, {sha(b) for _, b in entries})
        out[k] = probs[:1]
        retain_lineage_lint(case, sref, probs, inputs={path: data.decode('utf-8') for path, data in entries})
    run = _ln_pat_v2(r, record_id='another-lineage')
    check('LN1', '(review probe E6) a record superseding a record of the same kind and schema, present at F, with '
          'another record_id; for each kind of S4a (config_id for the configuration): FAIL record-invalid for each kind',
          "for each kind, lint_chain (whose problems are record-invalid) reports the superseding record, the "
          "predecessor passing its own lint; and a terms run using such a rule file exits 20 with record-invalid on it",
          {'lint': out, 'run': run}, all(out.values()) and _invalid(run, 'syn/rules-pat-v2.json'))
    # LN2 (positive)
    o = _ln_pat_v2(r)
    REC.name_last('', attested={'superseding_record_used': 'syn/rules-pat-v2.json' in o['rule_files']})
    check('LN2', '(positive) a record superseding a record of the same kind, schema and record_id that itself passes '
          'the lint: no record-invalid; the run uses the superseding record',
          "exit 0, no record-invalid, and the run's rule files include the superseding record", o,
          _clean(o, 'syn/rules-pat-v2.json'))
    # LN3
    res = {case: _ln_pat_v2(r, case=case, record_id=value) for case, value in (
        ('record_id missing', None), ('record_id empty', ''), ('record_id not a string', 7))}

    def no_id_predecessor(x):
        _variant_doc(x.files, PAT, 'syn/rules-pat-r1.json', record_id=None, author='session.fixture-writer-c')
        _chain(x.files, 'syn/rules-pat-r1.json')
    case = 'predecessor lacks record_id'
    res[case] = _ln_pat_v2(r, sup='syn/rules-pat-r1.json', setup=no_id_predecessor, case=case)
    check('LN3', 'a superseding record whose record_id is missing, empty or not a string; separately, a valid '
          'superseding record whose predecessor lacks a valid record_id: FAIL record-invalid in each case',
          "each run exits 20 with record-invalid on the superseding record, naming the lineage id", res,
          all(_invalid(o, 'syn/rules-pat-v2.json', 'lineage id') for o in res.values()))

    # LN4
    narrowed = [dict(rr, patterns={'a': r'\bAxiom Z\b[^.]{0,30}\b(holds|assumed)\b'}) if rr['id'] == 'syn-deny'
                else rr for rr in json.loads(LN(r).files[PAT])['rules']]

    def predecessor(case, widened=False, widening_review=None, **kw):
        def setup(x):
            if widened:
                # the predecessor changes a deny rule's pattern against its own predecessor (PAT), which is widening
                # (sec. 6.3), with a regular review and, as given, a widening review of it
                _variant_doc(x.files, PAT, 'syn/rules-pat-r1.json', sup=PAT, author='session.fixture-writer-c', rules=narrowed)
            else:
                _variant_doc(x.files, PAT, 'syn/rules-pat-r1.json', author='session.fixture-writer-c')
            _chain(x.files, 'syn/rules-pat-r1.json', **kw)
            if widening_review is not None:
                x.files['syn/rules-pat-r1.widen.json'] = sf.jb(widening_review(x.files))
        if widened:
            return _ln_pat_v2(r, sup='syn/rules-pat-r1.json', setup=setup, rules=narrowed, case=case)
        return _ln_pat_v2(r, sup='syn/rules-pat-r1.json', setup=setup, case=case)

    def wr(items):
        def make(files):
            return review_record({'schema': 'oi-review-record/1', 'kind': 'widening', 'reviewer': sf.WIDENER, 'method': 'read',
                    'reviewed': {'path': 'syn/rules-pat-r1.json', 'blob_sha256': sha(files['syn/rules-pat-r1.json'])},
                    'replaces': {'path': PAT, 'blob_sha256': sha(files[PAT])},
                    'verdicts': [{'item': i, 'verdict': 'accept'} for i in items]})
        return make
    res = {case: predecessor(case, **options) for case, options in (
        ('predecessor without review', {'review': False}),
        ('predecessor verdict not accept', {'verdict': 'reject'}),
        ('predecessor widens without review', {'widened': True}),
        ('widening review omits the changed item', {'widened': True, 'widening_review': wr(['other'])}))}
    pos = predecessor('valid widening review (positive)', widened=True, widening_review=wr(['changed pattern']))
    check('LN4', 'a predecessor of the same lineage that fails the lint itself (no review record; separately, a verdict '
          'not accept; separately, a predecessor that widens its own predecessor without a valid widening review): '
          'FAIL record-invalid for the superseding record in each case',
          "each run exits 20 with record-invalid on the superseding record, naming its predecessor; with a valid "
          "widening review of the widened predecessor the run is clean",
          dict(res, **{'(countercontrol) the widened predecessor with a valid widening review': pos}),
          all(_invalid(o, 'syn/rules-pat-v2.json', 'predecessor') for o in res.values()) and
          _clean(pos, 'syn/rules-pat-v2.json'))
    # LN5: a synthetic in-memory store that resolves each named {path, blob_sha256} without rehashing
    res = {}
    for case in ('two-record cycle', 'self-supersession'):
        fake = {'a': '1' * 64, 'b': '2' * 64, 's': '3' * 64}
        docs = {}
        if case == 'two-record cycle':
            docs[('r/a.json', fake['a'])] = {'schema': 'oi-scope/1', 'record_id': 'x', 'author': 'session.fixture-w',
                                             'supersedes': {'path': 'r/b.json', 'blob_sha256': fake['b']}}
            docs[('r/b.json', fake['b'])] = {'schema': 'oi-scope/1', 'record_id': 'x', 'author': 'session.fixture-w',
                                             'supersedes': {'path': 'r/a.json', 'blob_sha256': fake['a']}}
            top = {'schema': 'oi-scope/1', 'record_id': 'x', 'author': 'session.fixture-w',
                   'supersedes': {'path': 'r/a.json', 'blob_sha256': fake['a']}}
        else:
            top = {'schema': 'oi-scope/1', 'record_id': 'x', 'author': 'session.fixture-w',
                   'supersedes': {'path': 'r/t.json', 'blob_sha256': fake['s']}}
        tb = util.canonical(top)
        tref = {'path': 'r/t.json', 'blob_sha256': sha(tb)}
        if case == 'self-supersession':
            docs[('r/t.json', fake['s'])] = top
        entries = [('r/t.json', tb)]
        for (q, h) in list(docs) + [('r/t.json', sha(tb))]:
            rv = util.canonical(review_record({'schema': rec.review_schema, 'reviewer': 'session.fixture-rv', 'reviewed': {'path': q,
                                                                                            'blob_sha256': h},
                                 'method': 'read', 'verdicts': [{'item': 'x', 'verdict': 'accept'}]}))
            entries += [(q + '.review', rv)]
        ov, root, entries = idf_.unit_store(entries)
        st = rec.Store(entries, ov, [root])
        st.resolver = lambda ref, docs=docs: docs.get((ref.get('path'), ref.get('blob_sha256')))
        # no commit can hold bytes that hash to the invented digests, so no review of these predecessors binds its
        # revision (S-1 sec. 3); the predecessors' own lint is taken as passing, so that the chain walk itself, and
        # its termination, is what this control measures
        st._pred_cache.update({h: [] for (_q, h) in docs})
        probs = rec.lint_chain(tref, st, {sha(b) for _, b in entries})
        res[case] = probs[:2]
        retain_lineage_lint(case, tref, probs, inputs=[[path, data.decode('utf-8')] for path, data in entries],
                            resolution=[{'path': path, 'sha256': digest, 'record': value}
                                        for (path, digest), value in docs.items()])
    check('LN5', 'a supersedes cycle of two records, and a self-supersession, in a synthetic in-memory store that '
          'resolves each named {path, blob_sha256} to the given record without rehashing: FAIL record-invalid in both; '
          'the chain walk terminates',
          "lint_chain returns, for both, a problem naming the loop", res,
          all(any('loops' in p for p in v) for v in res.values()))

    # LN6: a fork in the audit directory
    def fork(x):
        _variant_doc(x.files, PAT, 'syn/rules-pat-v2b.json', sup=PAT, author='session.fixture-writer-c')
        _chain(x.files, 'syn/rules-pat-v2b.json')
    o = _ln_pat_v2(r, setup=fork)
    check('LN6', 'two records of one lineage superseding the same predecessor, both in the audit directory at F, only '
          'one referenced by the configuration: FAIL record-invalid (ambiguous ancestry)',
          "exit 20 with record-invalid on the referenced record, naming the ambiguous ancestry", o,
          _invalid(o, 'syn/rules-pat-v2.json', 'ambiguous ancestry'))
    # LN7: two heads
    res = {}
    x = LN(r)
    beta = [dict(rr, id='syn-beta-b') for rr in json.loads(x.files[PAT])['rules'] if rr['id'] == 'syn-beta']
    _variant_doc(x.files, PAT, 'syn/rules-pat-b.json', rules=beta, author='session.fixture-writer-c')
    x.add_rules('syn/rules-pat-b.json', _chain(x.files, 'syn/rules-pat-b.json'))
    res['two first records'] = x.run()
    REC.name_last('two heads, supersedes null')
    x = LN(r)
    _variant_doc(x.files, PAT, 'syn/rules-pat-v2.json', sup=PAT)
    _variant_doc(x.files, PAT, 'syn/rules-pat-v2b.json', sup=PAT, author='session.fixture-writer-c')
    refs = _chain(x.files, 'syn/rules-pat-v2.json') + _chain(x.files, 'syn/rules-pat-v2b.json')
    x.use_rules({PAT: 'syn/rules-pat-v2.json'}, refs)
    x.add_rules('syn/rules-pat-v2b.json', [])
    res['two diverging chains'] = x.run()
    REC.name_last('two diverging chains')
    check('LN7', 'two records with one record_id and kind, each with supersedes: null (separately, two chains from one '
          'first record that diverge), both read in one run: FAIL record-invalid (two heads)',
          "each run exits 20 with record-invalid on both records, naming two heads", res,
          _invalid(res['two first records'], PAT, 'two heads') and
          _invalid(res['two first records'], 'syn/rules-pat-b.json', 'two heads') and
          _invalid(res['two diverging chains'], 'syn/rules-pat-v2.json', 'two heads') and
          _invalid(res['two diverging chains'], 'syn/rules-pat-v2b.json', 'two heads'))

    # LN8: an unrelated chain
    def middle(**fields):
        def setup(x):
            _variant_doc(x.files, PAT, 'syn/rules-pat-m.json', sup=PAT, author='session.fixture-writer-c', **fields)
        return setup
    res = {case: _ln_pat_v2(r, sup='syn/rules-pat-m.json', setup=middle(**fields), case=case)
           for case, fields in (('middle record other record_id', {'record_id': 'other'}),
                                ('middle record other schema', {'schema': 'oi-term-rules/3'}))}
    check('LN8', 'a three-record chain whose middle record has another record_id (separately, another schema of the '
          'same kind): FAIL record-invalid (unrelated chain)',
          "each run exits 20 with record-invalid on the head, naming another lineage or another kind, schema", res,
          _invalid(res['middle record other record_id'], 'syn/rules-pat-v2.json', 'another lineage') and
          _invalid(res['middle record other schema'], 'syn/rules-pat-v2.json', 'another kind'))


    # LN10 (positive)
    x = LN(r)
    beta = [dict(rr, id='syn-beta-x') for rr in json.loads(x.files[PAT])['rules'] if rr['id'] == 'syn-beta']
    _variant_doc(x.files, PAT, 'syn/rules-extra.json', rules=beta, record_id=None, author='session.fixture-writer-c')
    x.add_rules('syn/rules-extra.json', _chain(x.files, 'syn/rules-extra.json'))
    o = x.run()
    check('LN10', '(positive) a record with supersedes: null and no record_id, named by no supersedes: no '
          'record-invalid', "exit 0, no record-invalid, the record among the run's rule files", o,
          _clean(o, 'syn/rules-extra.json'))


def r6_g6(r):
    """G-6: a record_id carried by a record off the referenced record's supersedes chain is a reused id."""
    x = LN(r)
    _variant_doc(x.files, PAT, 'syn/rules-pat-dup.json', author='session.fixture-writer-c')
    reused = x.run()
    REC.name_last('a second record with the rule file record_id off its chain',
                  bindings={'rule_file': PAT},
                  attested={'message_names': 'reused' if 'reused' in reused['why'].get(PAT, '') else None})
    clean = LN(r).run()
    REC.name_last('no such record (positive)')
    out = {'a second record with the rule file\'s record_id, off its chain': reused, '(positive) no such record': clean}
    check('R6-G6', 'a record in the audit directory at F carrying the record_id, kind and schema of a rule file the '
          'configuration references, with supersedes null (not on that file\'s supersedes chain) (sec. 6.3, DI-2: '
          '"a record_id carried by two records that do not lie on one supersedes chain is" a reused id): FAIL '
          'record-invalid on the referenced rule file; without that record the run is clean',
          "the first exits 20 with record-invalid on syn/rules-pat.json naming the reuse; the second exits 0 with no "
          "record-invalid", out,
          _invalid(reused, PAT, 'reused') and clean['exit'] == 0 and not clean['record_invalid'])


def replay_controls(r, t, F, chain, raw, gz, snap):
    d = tempfile.mkdtemp(prefix='landing-', dir=r.out_root)
    land = {'schema': 'oi-ledger-landing/1', 'name': 'syn-round-1',
            'result': {'path': 'result.json.gz', 'sha256': sha(raw), 'compressed_sha256': sha(gz)},
            'snapshot': {'path': 'snapshot.json', 'sha256': chain['config']['admission']['snapshot_sha256']}}
    open(os.path.join(d, 'landing.json'), 'wb').write(hf.jb(land))
    open(os.path.join(d, 'result.json.gz'), 'wb').write(gz)
    open(os.path.join(d, 'snapshot.json'), 'wb').write(hf.jb(snap))
    out = r.out()
    code, res = cli.run(['replay', '--snapshot', os.path.join(d, 'landing.json'), '--out', out], repo=t.repo,
                        stderr=io.StringIO())
    eq = (res or {}).get('replay', {}).get('equal_to_committed')
    mode = ((res or {}).get('config') or {}).get('admission', {}).get('mode')
    REC.name_last('op-B replay', attested={'outcome': 'REPLAY_EQUAL' if eq is True else None,
                                           'acceptable_as_new_run': checker.accept(res or {}, code, {})})
    op_b = REC.pending[-1]
    bad = tempfile.mkdtemp(prefix='landing-bad-', dir=r.out_root)
    for f in ('landing.json', 'snapshot.json'):
        shutil.copy(os.path.join(d, f), bad)
    open(os.path.join(bad, 'result.json.gz'), 'wb').write(checker.deterministic_gzip(raw + b'\n'))
    code_b, res_b = cli.run(['replay', '--snapshot', os.path.join(bad, 'landing.json'), '--out', r.out()],
                            repo=t.repo, stderr=io.StringIO())
    REC.name_last('recorded result hash differs')
    # restored: the same replay of the unaltered landing, against the op-B replay
    cli.run(['replay', '--snapshot', os.path.join(d, 'landing.json'), '--out', r.out()], repo=t.repo,
            stderr=io.StringIO())
    REC.name_last('restored', baseline=op_b)
    check('TR45-opB', 'the offline replay of an op-B/D result from its committed snapshot: output equal to the '
          'committed result except config.admission.mode = "replay"; never acceptable; a result file that does not '
          'hash to its recorded sha256 makes the replay refuse',
          "replay exit equals the committed exit, equal_to_committed is true, mode is 'replay', accept() is false; "
          "the altered landing refuses with REPLAY_REFUSED",
          {'exit': code, 'equal': eq, 'mode': mode, 'altered': (code_b, stop(res_b))},
          code == chain['exit_status'] and eq is True and mode == 'replay' and
          not checker.accept(res or {}, code, {}) and (code_b, stop(res_b)) == (65, 'REPLAY_REFUSED'),
          files={'committed-result.json': raw, 'landing.json': land, 'snapshot.json': snap},
          procedure={'name': 'landing-verify', 'lib': 'replay', 'run_cases': ['op-B replay', 'restored']})


SC42 = 'audit/sc42-result.json'
CTL = 'audit/sc42-controls.json'
CHK = 'audit/check_sc42.py'
CHECKER_SRC = b'''import os, sys
ROOT = os.getcwd()
if '--self-test' in sys.argv:
    sys.stdout.write(open(os.path.join(ROOT, 'audit/sc42-controls.json')).read())
else:
    sys.stdout.write('{"base": "%s", "sites": %d}\\n' % (open(os.path.join(ROOT, 'audit/base.txt')).read().strip(),
                     len(open(os.path.join(ROOT, 'doc/a.md')).read().split())))
'''


def git(d, *a, env=None):
    e = dict(os.environ, GIT_AUTHOR_NAME='fixture', GIT_AUTHOR_EMAIL='fixture@invalid', GIT_COMMITTER_NAME='fixture',
             GIT_COMMITTER_EMAIL='fixture@invalid', GIT_AUTHOR_DATE='2026-01-01T00:00:00Z',
             GIT_COMMITTER_DATE='2026-01-01T00:00:00Z')
    return subprocess.run(['git', '-C', d] + list(a), capture_output=True, text=True, env=e, check=True).stdout.strip()


def commit_files(d, files, msg):
    for p, b in files.items():
        f = os.path.join(d, p)
        if b is None:
            os.remove(f)
            continue
        os.makedirs(os.path.dirname(f), exist_ok=True)
        open(f, 'wb').write(b)
    git(d, 'add', '-A')
    git(d, 'commit', '-q', '-m', msg)
    return git(d, 'rev-parse', 'HEAD')


def g_controls(r):
    from ledger_coverage.adapters import deleg_rerun_equal as rerun, deleg_preserve_check as pc
    from ledger_coverage.adapters import deleg_fingerprint_regen as fr
    d = tempfile.mkdtemp(prefix='g-repo-', dir=r.out_root)
    git(d, 'init', '-q')
    words = b'one two three\n'
    good = b'{"base": "basecommit", "sites": 3}\n'
    H = commit_files(d, {'doc/a.md': words, 'audit/base.txt': b'basecommit\n', CHK: CHECKER_SRC,
                         CTL: open_controls(), SC42: good}, 'H')
    X = commit_files(d, {'doc/b.md': b'x\n'}, 'X')
    F = X
    repo = gitobj.GitRepo(d)
    cls = {'id': 'sc42', 'adapter': 'rerun-equal', 'paths': [SC42],
           'params': {'must_contain': 'basecommit', 'controls_path': CTL, 'checker_path': CHK}}
    roles = {'scientific_base': H, 'candidate': X, 'freeze': F, 'certified': X, 'ledger_sha256': '0' * 64}
    dele = delmod.Delegation({'schema': 'oi-delegation/1', 'classes': [cls]}, {'rerun-equal': rerun})

    def env(out):
        return delmod.Native(repo, d, out, F, True)

    def evaluate(case, delegation, repository, run_roles, native_env, supplied=None):
        items, report = delegation.verify(repository, run_roles, native_env, {'splices': []}, supplied)
        checked_classes = [{'subject': item['class'], 'state': item['state']} for item in report['classes']]
        doc = control_records.stage_doc(items, operation='delegation', roles=run_roles, delegated=report,
                                        sites=checked_classes)
        REC.capture_doc('delegation.verify', doc, case=case)
        return items, report

    def clean_sc42(case):
        return evaluate(case, dele, repo, roles, env(r.out()))

    items, _ = clean_sc42('positive')
    baseline = REC.pending[-1]
    pos = [i['class'] for i in items]
    # G4: a supplied result file claiming verbose_equal true, while the clone's re-execution differs
    Xb = commit_files(d, {SC42: b'{"base": "basecommit", "sites": 4}\n'}, 'X with a hand-edited result')
    supplied = {'sc42-rerun.json': b'{"candidate": "%s", "verbose_exit": 0, "verbose_equal": true, '
                                  b'"self_test_equal": true, "plan": "%s"}' % (Xb.encode(), F.encode())}
    items4, rep4 = evaluate('re-execution differs', dele, repo, dict(roles, candidate=Xb, certified=Xb),
                            env(r.out()), supplied)
    REC.name_last('re-execution differs', attested={
        'supplied_file_read_as_evidence': 'sc42-rerun.json' not in rep4['supplied_evidence_ignored']})
    retain_restored(lambda: clean_sc42('restored'), baseline)
    check('G4', 'sc42 with a supplied result claiming verbose_equal true while the clone\'s re-execution differs: FAIL '
          'delegated-evidence-invalid; the supplied file is not read as evidence',
          "the positive case has no item; the mutant gives delegated-evidence-invalid; the report lists the supplied "
          "file as ignored", {'positive': pos, 'mutant': sorted({i['class'] for i in items4}),
                              'ignored': rep4['supplied_evidence_ignored'], 'runs': len(rep4['evidence_record']['runs'])},
          pos == [] and 'delegated-evidence-invalid' in {i['class'] for i in items4} and
          rep4['supplied_evidence_ignored'] == ['sc42-rerun.json'])
    # G9: C = X plus one commit changing the SC-42 result file; X alone passes
    C = Xb
    clean9, _ = clean_sc42('class run at X')
    baseline = REC.pending[-1]
    items9, _ = evaluate('class run from the clone at C', dele, repo, dict(roles, certified=C), env(r.out()))
    retain_restored(lambda: clean_sc42('restored'), baseline)
    trees = {(i['tree'], i['class']) for i in items9}
    check('G9', 'C = X plus one commit that changes the SC-42 result file, the class at X alone passing: FAIL for '
          'sc42 from the clone at C', "no item at X; delegated-evidence-invalid at C",
          sorted(trees), not clean9 and ('C', 'delegated-evidence-invalid') in trees and
          not any(t_ == 'X' for t_, _ in trees))
    # G8: no F; a supplied result with plan null
    clean_sc42('valid freeze and evidence')
    baseline = REC.pending[-1]
    null_plan = {'sc42-rerun.json': b'{"plan": null}'}
    items8, _ = evaluate('null plan without named evidence', dele, repo, dict(roles, freeze=None),
                         env(r.out()), null_plan)
    cls_of = {(i['class'], i.get('tree')) for i in items8}
    dele_ev = delmod.Delegation({'schema': 'oi-delegation/1', 'classes': [dict(cls, evidence=['sc42-rerun.json'])]},
                                {'rerun-equal': rerun})
    items8b, _ = evaluate('', dele_ev, repo, dict(roles, freeze=None), env(r.out()), null_plan)
    # bound independently of the result: the delegation class id and the name its evidence field lists
    REC.name_last('', bindings={'class': cls['id'], 'field': dele_ev.doc['classes'][0]['evidence'][0]})
    retain_restored(lambda: clean_sc42('restored'), baseline)
    c8 = sorted({i['class'] for i in items8b})
    check('G8', 'delegated evidence with plan null and no F: never PASS: REVIEW_REQUIRED delegated-evidence-missing '
          'for the class, and the field FAIL delegated-evidence-invalid',
          "the class gives delegated-evidence-missing and the plan-null file delegated-evidence-invalid",
          {'without_named_evidence': sorted(cls_of), 'with': c8},
          c8 == ['delegated-evidence-invalid', 'delegated-evidence-missing'])
    # G5: coverage-ledger against the census the tool runs in the clone
    census = b'''import json, sys
print(json.dumps({"entries": [{"id": "S:1", "fingerprint": "%s"}]}))
'''
    led_path = 'cov/LEDGER.json'
    led_h = b'[{"id": "S:1", "fingerprint": "aaaa"}]\n'
    d5 = tempfile.mkdtemp(prefix='g5-repo-', dir=r.out_root)
    git(d5, 'init', '-q')
    H5 = commit_files(d5, {led_path: led_h, 'tools/proof_census.py': census % b'bbbb'}, 'H')
    X5 = commit_files(d5, {led_path: led_h.replace(b'aaaa', b'bbbb')}, 'X')
    X5b = commit_files(d5, {led_path: led_h.replace(b'aaaa', b'cccc')}, 'X stale')
    repo5 = gitobj.GitRepo(d5)
    cls5 = {'id': 'coverage-ledger', 'adapter': 'fingerprint-regen', 'paths': [led_path], 'ledgered_paths': [led_path],
            'params': {'stale_ids': ['S:1'], 'census_path': 'tools/proof_census.py'}}
    dl5 = delmod.Delegation({'schema': 'oi-delegation/1', 'classes': [cls5]}, {'fingerprint-regen': fr})
    def census_case(case, tree, supplied=None):
        run_roles = dict(roles, scientific_base=H5, candidate=tree, freeze=tree, certified=tree)
        return evaluate(case, dl5, repo5, run_roles, delmod.Native(repo5, d5, r.out(), tree, True), supplied)

    ok5, _ = census_case('census equal', X5)
    baseline = REC.pending[-1]
    bad5, _ = census_case('census differs', X5b,
                          {'proof-census.json': b'{"entries": [{"id": "S:1", "fingerprint": "cccc"}]}'})
    retain_restored(lambda: census_case('restored', X5), baseline)
    check('G5', 'coverage-ledger with a supplied census JSON; one STALE value at X differing from the census the '
          'tool runs: FAIL', "no item when the value equals the tool's census; delegated-evidence-invalid when it "
          "differs, whatever the supplied file says",
          {'positive': [i['class'] for i in ok5], 'mutant': sorted({i['class'] for i in bad5})},
          not ok5 and 'delegated-evidence-invalid' in {i['class'] for i in bad5})
    # G6: tex with a supplied preserve_check result reporting pass, while a TeX stamp at X is wrong
    d6 = tempfile.mkdtemp(prefix='g6-repo-', dir=r.out_root)
    git(d6, 'init', '-q')
    md = b'# doc\n'
    H6 = commit_files(d6, {'p/A.md': md, 'p/A.tex': b'tex\n% source-sha256: 0\n'}, 'H')
    # a checker that runs in the disposable clone and reports pass for the tree it is given, so that the right
    # stamp is decided by the stamps alone (the tool re-derives them and validates the result's binding)
    chk6 = ('import hashlib, json, sys\n'
            'a = dict(zip(sys.argv[1::2], sys.argv[2::2]))\n'
            'me = hashlib.sha256(open(__file__, "rb").read()).hexdigest()\n'
            'json.dump({"schema": "a1exit-checker-result-v1", "checker": "preserve_check.py", "plan": a["--plan"], '
            '"base": "%s", "ledger_sha256": "%s", "candidate": a["--commit"], "exit": 0, "verdict": "pass", '
            '"checks": [], "checker_blob_sha256": me}, open(a["--result-json"], "w"))\n'
            % (H6, roles['ledger_sha256'])).encode()
    X6 = commit_files(d6, {'p/A.tex': b'tex\n% source-sha256: ' + sha(md).encode() + b'\n', 'p/check.py': chk6}, 'X')
    X6b = commit_files(d6, {'p/A.tex': b'tex\n% source-sha256: ' + b'1' * 64 + b'\n'}, 'X wrong stamp')
    repo6 = gitobj.GitRepo(d6)
    cls6 = {'id': 'tex', 'adapter': 'preserve-check-v1', 'paths': ['p/A.tex'],
            'params': {'sources': {'p/A.tex': 'p/A.md'}, 'checker_path': 'p/check.py', 'checker_sha256': sha(chk6),
                       'required_checks': []}}
    dl6 = delmod.Delegation({'schema': 'oi-delegation/1', 'classes': [cls6]}, {'preserve-check-v1': pc})
    good_res = b'{"schema": "a1exit-checker-result-v1", "verdict": "pass", "plan": "%s"}' % X6b.encode()
    def stamp_case(case, tree, supplied=None, native=False):
        run_roles = dict(roles, scientific_base=H6, candidate=tree, freeze=tree, certified=tree)
        return evaluate(case, dl6, repo6, run_roles, delmod.Native(repo6, d6, r.out(), tree, True) if native else None,
                        supplied)

    bad6, _ = stamp_case('wrong stamp', X6b, {'tex-preserve-check.json': good_res})
    ok6, _ = stamp_case('right stamp', X6, native=True)
    baseline = REC.pending[-1]
    retain_restored(lambda: stamp_case('restored', X6, native=True), baseline)
    check('G6', 'tex with a supplied preserve_check result reporting pass, while a TeX stamp at X is wrong: FAIL '
          'delegated-evidence-invalid', "the wrong stamp gives delegated-evidence-invalid; the right stamp gives no "
          "item (the checker runs in the clone and passes)",
          {'wrong': sorted({i['class'] for i in bad6}), 'right': sorted({i['class'] for i in ok6})},
          'delegated-evidence-invalid' in {i['class'] for i in bad6} and not ok6)
    # G7: pdf evidence whose candidate_tree differs from X's, or whose artifact hash differs
    cls7 = {'id': 'pdf', 'adapter': 'preserve-check-v1', 'paths': ['p/A.tex'],
            'params': {'workflow_path': 'wf.yml', 'job': 'pdf-compare', 'checker_sha256': 'c' * 64}}
    dl7 = delmod.Delegation({'schema': 'oi-delegation/1', 'classes': [cls7]}, {'preserve-check-v1': pc})

    class H7:
        def __init__(self, result, art):
            self.res, self.art = result, art

        def runs_for(self, rid, head):
            return [{'workflow_path': 'wf.yml', 'head_sha': head, 'event': 'workflow_dispatch', 'repository_id': rid,
                     'head_repository_id': rid, 'jobs': [{'name': 'pdf-compare', 'conclusion': 'success'}],
                     'result': self.res, 'artifact_sha256': self.art}]
    tree = repo6.tree_id(X6)
    good7 = {'candidate_commit': X6, 'candidate_tree': tree, 'sha256': 'd' * 64, 'checker_blob_sha256': 'c' * 64}
    pdf_roles = dict(roles, scientific_base=H6, candidate=X6, freeze=X6, certified=X6)

    def pdf_case(name, res_, art):
        native = delmod.Native(repo6, d6, r.out(), X6, True, host=H7(res_, art), repo_id=1)
        return evaluate(name, dl7, repo6, pdf_roles, native)

    out7 = {}
    for name, res_, art in (('good evidence', good7, 'd' * 64),
                            ('candidate_tree differs', dict(good7, candidate_tree='0' * 40), 'd' * 64),
                            ('artifact hash differs', good7, 'e' * 64)):
        it, _ = pdf_case(name, res_, art)
        out7[name] = sorted({i['class'] for i in it})
    baseline = next(run for run in REC.pending if run['case'] == 'good evidence')
    retain_restored(lambda: pdf_case('restored', good7, 'd' * 64), baseline)
    check('G7', 'pdf evidence whose candidate_tree differs from X\'s, or whose artifact hash differs: FAIL '
          'delegated-evidence-invalid', "good: no item; tree and artifact mutants: delegated-evidence-invalid",
          out7, out7['good evidence'] == [] and out7['candidate_tree differs'] == ['delegated-evidence-invalid'] and
          out7['artifact hash differs'] == ['delegated-evidence-invalid'])
    not_run('G-A1', 'the A1 classes executed natively in disposable clones at X and C (tex, sc42, coverage-ledger) '
            'and the host-run classes (pdf, ci) read from the host API', 'needs F and a CI job (sec. A.40: a full '
            'clone of the repository per tree); CI plan in the report')


def open_controls():
    return b'{"controls": "fixed"}\n'


def r_controls(r):
    from ledger_coverage.engine import controls_engine as ce
    w = ce.World()
    H = w.pin
    a = ce.off(ce.base_text, 'beta line two')
    led = ce.ledger(H, [(ce.doc_path, a, a + 4, 'betx')], w.repo)
    led['edits'] = []
    X = w.child(H, ce.base_text.replace('beta line two', 'betx line two', 1), subject='candidate')
    ctx = w.ctx()

    class D:
        def paths(self):
            return []

        def record_prefixes(self):
            return ['plan/']

        def owns_ledgered(self, p):
            return False
    def after(commits, case, **bindings):
        # the execution's commits-after check as a retained stage result, named as the expectation case
        ex = exmod.Execution(ctx, H, X, led, D())
        ex.commits_after(commits)
        REC.capture_doc('Execution.commits_after (conformance_controls.py)',
                        control_records.stage_doc(ex.items, operation='execution', checks=ex.checks),
                        case=case, bindings=bindings)
        return ex

    def restored_pair():
        clean = after([], 'baseline')
        after([], 'restored')
        REC.pending[-1]['baseline'] = REC.pending[-2]
        return clean
    C16 = w.repo.derive(X, {'notes/unrelated.txt': b'x\n'}, parents=[X], subject='C16')
    e = after([C16], '', commit=C16)
    c16 = [(i['class'], i.get('commit')) for i in e.items]
    REC.pending[-1]['attested'] = {'names_commit': '$commit' if c16 == [('unauthorized-change', C16)] else None}
    restored_pair()
    check('R16', 'C = X plus one commit that changes an unledgered, undeclared path: FAIL unauthorized-change naming '
          'that commit', "one unauthorized-change item whose commit is that commit", c16,
          c16 == [('unauthorized-change', C16)])
    C17 = w.repo.derive(X, {'plan/execution/result.json': b'{}\n'}, parents=[X], subject='C17')
    e17 = after([C17], '')
    paths17 = e17.checks[-1]['commits'][0]['paths']
    REC.pending[-1]['attested'] = {'commit_paths_classified': 'record' if paths17 and
                                   all(x['class'] == 'record' for x in paths17) else None}
    restored_pair()
    check('R17', 'C = X plus one commit that changes only a record path the plan admits after F: PASS for that '
          'commit', "no item; the path is classified record", {'items': e17.items,
                                                                   'paths': e17.checks[-1]['commits'][0]['paths']},
          not e17.items and e17.checks[-1]['commits'][0]['paths'] == [{'path': 'plan/execution/result.json',
                                                                       'class': 'record'}])


def a12r(r):
    """A widening review whose verdicts omit one changed item; separately one naming another superseded blob."""
    syn = sf.Syn()
    pd = sf.patch_doc(syn.H, [])
    base = {'patch_sha': sha(pd), 'files': {'syn/patch.json': pd}, 'allow_widened': True, 'widening_review': True}
    out = {}
    clean_commit, clean_path, clean_sha, _ = syn.build(base)
    argv = ['terms', '--commit', syn.H]
    code, res = r.cli(syn.repo, argv, clean_commit, clean_path, clean_sha)
    out['complete'] = (code, classes(res))
    clean = REC.name_last('complete review (positive)')
    rule_path = 'syn/rules-allow.json'
    for name, extra in (
            ('verdicts omit one changed item', {'widening_items': ['syn-allow-1:other']}),
            ('names another superseded blob',
             {'widening_replaces': {'path': rule_path, 'blob_sha256': '1' * 64}})):
        c, p, s, _ = syn.build(dict(base, **extra))
        code, res = r.cli(syn.repo, argv, c, p, s)
        out[name] = (code, classes(res))
        widened_ref = next(ref for ref in json.loads(syn.repo.read(c, p))['rules']
                           if ref['path'].startswith('syn/rules-allow'))
        REC.name_last(name, bindings={'rule_file': widened_ref['path']})
    retain_restored(lambda: r.cli(syn.repo, argv, clean_commit, clean_path, clean_sha), clean)
    check('A12r', 'a widening review whose verdicts omit one changed item; separately one naming another superseded '
          'blob: FAIL record-invalid each', "complete: exit 0; both mutants: exit 20 with record-invalid",
          out, out['complete'][0] == 0 and all(code == 20 and 'record-invalid' in result_classes
                                               for name, (code, result_classes) in out.items() if name != 'complete'))


def z11_s4a(r):
    syn = sf.Syn()
    pd = sf.patch_doc(syn.H, [])
    cls = {'schema': 'oi-side-change-classes/1', 'record_id': 'k1', 'author': sf.WRITER, 'supersedes': None,
           'classes': [{'id': 'trial-workflow', 'pins': []}]}
    cls2 = dict(cls, record_id='k2')
    c, p, s, _ = syn.build({'patch_sha': sha(pd), 'files': {'syn/patch.json': pd},
                            'records_extra': {'syn/k1.json': cls, 'syn/k2.json': cls2}})
    # records_extra gives kind "record"; mark them as side-change class records in the configuration
    cfg = json.loads(syn.repo.read(c, p))
    for rr in cfg['records']:
        if rr['path'] in ('syn/k1.json', 'syn/k2.json'):
            rr['kind'] = 'side-change-classes'
    c2 = syn.repo.derive(c, {p: sf.jb(cfg)}, parents=syn.repo.parents(c))
    code, res = r.cli(syn.repo, ['terms', '--commit', syn.H], c2, p, sha(sf.jb(cfg)), harness=True)
    REC.name_last('two records, one class id')
    one = dict(cls, classes=[{'id': 'a', 'pins': []}, {'id': 'a', 'pins': []}])
    c3, p3, s3, _ = syn.build({'patch_sha': sha(pd), 'files': {'syn/patch.json': pd},
                               'records_extra': {'syn/k1.json': one}})
    cfg3 = json.loads(syn.repo.read(c3, p3))
    for rr in cfg3['records']:
        if rr['path'] == 'syn/k1.json':
            rr['kind'] = 'side-change-classes'
    c4 = syn.repo.derive(c3, {p3: sf.jb(cfg3)}, parents=syn.repo.parents(c3))
    code2, res2 = r.cli(syn.repo, ['terms', '--commit', syn.H], c4, p3, sha(sf.jb(cfg3)), harness=True)
    REC.name_last('one record, duplicate class id')
    check('Z11', 'two class records, or one record, defining the same class id: ERROR CONFIG_INCONSISTENT',
          "both exit 65 with stop CONFIG_INCONSISTENT", [(code, stop(res)), (code2, stop(res2))],
          (code, stop(res)) == (65, 'CONFIG_INCONSISTENT') and (code2, stop(res2)) == (65, 'CONFIG_INCONSISTENT'))
    # S4a: a record of each kind whose supersedes names a blob absent from the object store, or another kind
    from ledger_coverage.engine import records as rec
    out = {}
    for k, kind in LINEAGE_KINDS.items():
        other = {'schema': 'oi-scope/1' if k != 'oi-scope/1' else 'oi-term-rules/2', 'record_id': 'o',
                 'supersedes': None, 'author': 'session.fixture-w'}
        ob = util.canonical(other)
        for case, sup in (('absent', {'path': 'r/none.json', 'blob_sha256': '0' * 64}),
                          ('other-kind', {'path': 'r/o.json', 'blob_sha256': sha(ob)})):
            doc = {'schema': k, 'record_id': 'r', 'config_id': 'r', 'author': 'session.fixture-w', 'supersedes': sup}
            db = util.canonical(doc)
            st = rec.Store([('r/r.json', db), ('r/o.json', ob)])
            ref = {'path': 'r/r.json', 'blob_sha256': sha(db)}
            probs = rec.supersedes_problems(ref, doc, st)
            out['%s/%s' % (k, case)] = bool(probs)
            name = kind if case == 'other-kind' else kind + ' (absent predecessor)'
            retain_lineage_lint(name, ref, probs, inputs={'record': db.decode('utf-8'),
                                                         'other_record': ob.decode('utf-8')})
    check('S4a', 'a record of each kind whose supersedes names a blob that does not exist, or a record of another '
          'kind: FAIL record-invalid for each kind', "every kind and case gives a supersedes problem (which "
          "lint_chain reports as record-invalid)", out, all(out.values()))




# every control this runner implements; one whose group stopped before it ran is FAIL, never absent
ALL_IDS = ['TR5-sim', 'TR5', 'TR1', 'TR2', 'TR3', 'TR13', 'TR14-tool', 'TR14', 'TR15', 'ADM-CONFIG-AT-F',
           'ACCEPT-SCHEMA', 'CONFIG-LINT', 'B4-MEANING', 'GV-CACHE', 'GV-CACHE-IMMUTABLE', 'GV-CACHE-KEY',
           'GV-CACHE-AFTER-READ', 'TR28-tool', 'TR28-consumer', 'TR29-tool',
           'TR29', 'TR30', 'TR45-opB', 'TR46', 'TR48', 'TR50', 'TR51', 'TR52', 'X11', 'EI1', 'EI2', 'EI2-consumer',
           'EI3', 'EI4', 'EI5', 'EI6', 'EI7-tool', 'EI8', 'EI9', 'EI10', 'EI11', 'EI12', 'EI13', 'EI14', 'EI15', 'GV1',
           'GV2', 'GV3', 'GV4', 'GV5', 'GV6', 'GV6-disk', 'GV7-tool', 'GV7-consumer', 'R16', 'R17', 'A12r', 'Z11',
           'S4a', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9', 'G-A1', 'R3-F2', 'R4-B3', 'R4-B3-DUP', 'R5-N6', 'R6-G6',
           'LN1', 'LN2', 'LN3', 'LN4', 'LN5', 'LN6', 'LN7', 'LN8', 'LN10', 'O3-FILTER',
           'RULE-MINLIT', 'RULE-ZEROFP'] + rdc.IDS


def write(out_root):
    os.makedirs(out_root, exist_ok=True)
    seen = {}
    for rrec in RESULTS:
        seen[rrec['id']] = seen.get(rrec['id'], 0) + 1
    for cid, n in sorted(seen.items()):
        if n > 1:
            record(cid + '-duplicate-id', 'every control id is reported once', None, '%d reports' % n, 'FAIL')
    summary = {}
    for rrec in RESULTS:
        summary[rrec['status']] = summary.get(rrec['status'], 0) + 1
    doc = {'schema': 'oi-control-report/1', 'controls': sorted(RESULTS, key=lambda x: x['id']), 'summary': summary}
    with open(os.path.join(out_root, 'conformance-controls.json'), 'w', encoding='utf-8') as f:
        f.write(json.dumps(doc, indent=1, sort_keys=True, default=str) + '\n')
    # R6.GATE.5 and R6.GATE.7: one record per control with its retained evidence, read by the gate
    REC.out_dir = out_root
    done = set()
    for rrec in sorted(RESULTS, key=lambda x: x['id']):
        if rrec['id'] in done:
            continue
        done.add(rrec['id'])
        REC.pending = RUNS.get(rrec['id'], [])
        files, proc = PROCEDURES.get(rrec['id'], (None, None))
        REC.record(rrec['id'], rrec['status'], rrec['actual'], rrec['predicate'] or rrec['expected'],
                   attested=ATTESTED.get(rrec['id']), files=files, procedure=proc)
    REC.write()
    return doc


def main(out_root, native_tr5=False):
    os.makedirs(out_root, exist_ok=True)
    REC.wrap_cli(cli)
    r = sf.Runner(tempfile.mkdtemp(prefix='conf-', dir=out_root))
    t = None
    groups = [('TR', lambda: tr_controls(r, native_tr5)), ('EI5', lambda: ei5_controls(r)), ('O3', lambda: o3_controls(r)),
              ('R16', lambda: r_controls(r)),
              ('A12r', lambda: a12r(r)), ('rule limits', lambda: allow_rule_limits(r)),
              ('Z11', lambda: z11_s4a(r)), ('G', lambda: g_controls(r)),
              ('GV', lambda: gv_disk_controls(r)), ('GV-CACHE', lambda: cache_controls(r)),
              ('EI', lambda: ei_controls(r)),
              ('R3-F2', lambda: f2_controls(r)), ('R4-B3', lambda: r4_b3_controls(r)),
              ('R4-B3-DUP', lambda: r4_b3_duplicate_controls(r)), ('R5-N6', lambda: r5_n6_controls(r)),
              ('LN', lambda: ln1_ln8(r)), ('R6-G6', lambda: r6_g6(r)),
              ('CONFIG-LINT', lambda: config_lint_controls(r)), ('B4-MEANING', lambda: meaning_controls(r)),
              # design amendment r4: the record-directory rule (O-9) and the item-2 record interfaces
              ('O9', lambda: rdc.o9_controls(r, check, REC)), ('I2', lambda: rdc.i2_controls(r, check, WORKFLOW, REC)),
              # design amendment 1: the post-freeze route
              ('POSTF', lambda: pfc.postf_controls(r, check)),
              ('LINE-PATCH-RC8', lambda: pfc.line_patch_control(r, check, REC.capture_doc)),
              # design amendment 4: the record base of a predicted M
              ('RECORD-BASE', lambda: pfc.rb_controls(r, check)),
              # design amendments 3 and 4: the category-3 block
              ('RECON-BLOCK', lambda: pfc.block_controls(r, check)),
              # design amendment 4: the category-3 keying and the reassessment
              ('BLOCK-KEY', lambda: pfc.bk_controls(r, check)),
              ('MIGRATION-RECORD', lambda: pfc.migration_controls(r, check)),
              # design amendment 3: the scientific effect, through the post-freeze route
              ('RECON-SCI', lambda: pfc.sci_controls(r, check))]
    for name, fn in groups:
        try:
            got = fn()
            if name == 'TR':
                t = got
        except Exception as exc:
            import traceback
            record('%s-group' % name, 'the group runs', None, '%s: %s %s' % (type(exc).__name__, exc,
                                                                             traceback.format_exc()[-1500:]), 'FAIL')
    if t is not None:
        try:
            acceptance_controls(r, t)
        except Exception as exc:
            import traceback
            record('acceptance-group', 'the group runs', None, '%s: %s %s' % (type(exc).__name__, exc,
                                                                              traceback.format_exc()[-1500:]), 'FAIL')
    for cid in ALL_IDS:
        if cid == 'TR5' and native_tr5:
            continue
        if not any(x['id'] == cid for x in RESULTS):
            record(cid, 'the control runs', None, 'its group stopped before it ran: %s'
                   % '; '.join(str(x['actual'])[-300:] for x in RESULTS if x['id'].endswith('-group')), 'FAIL')
    return write(out_root)


if __name__ == '__main__':
    doc = main(sys.argv[1], native_tr5=sys.argv[2:] == ['--native-tr5'])
    print(json.dumps(doc['summary'], sort_keys=True))
    for c in doc['controls']:
        if c['status'] != 'PASS':
            print(c['status'], c['id'], json.dumps(c['actual'], default=str)[:300])
