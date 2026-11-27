"""Local controls for the A1 staging amendment r2 (verification/audits/foundations/a1exit-staging-amendment-20261126/).

The amendment names four cases to register after adoption (DELTA-PROPOSAL.json `cases_to_register_after_adoption`):
ITEM2-CHECK, STAGING-ROLE-CHAIN, STAGING-FIRST-ALLOW and STAGING-CONFIG-REVIEWS. This suite runs their mechanical
parts, positive and negative, against in-memory synthetic objects and the independent gate. Each sub-case has its own
id `<CASE>/<n>`; the expected verdict of each is stated beside it. The expectation rows for these cases are not
registered by this suite (registration is an adoption act), so its records are local evidence only.

Usage: python3 -I -B tools/ledger_coverage/adapters/staging_controls.py OUT
Writes OUT/staging-controls.json and exits 0 when every sub-case holds, 1 otherwise.
"""
import copy
import hashlib
import importlib.util
import io
import json
import os
import shutil
import subprocess
import sys
import tempfile

here = os.path.dirname(os.path.abspath(__file__))
if 'ledger_coverage' not in sys.modules:
    _pkg = os.path.dirname(here)
    _spec = importlib.util.spec_from_file_location('ledger_coverage', os.path.join(_pkg, '__init__.py'),
                                                   submodule_search_locations=[_pkg])
    sys.modules['ledger_coverage'] = importlib.util.module_from_spec(_spec)
    _spec.loader.exec_module(sys.modules['ledger_coverage'])

from ledger_coverage.adapters import synthetic_fixture as sf  # noqa: E402
from ledger_coverage.adapters import record_directory_controls as rdc  # noqa: E402


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


GATE_DIR = os.path.join(os.path.dirname(here), 'gate')
GST = _load('gate_selftest_staging', os.path.join(GATE_DIR, 'gate_selftest.py'))
G = GST.G

RESULTS = []


def case(cid, expected, actual, holds):
    RESULTS.append({'id': cid, 'expected': expected, 'actual': actual, 'status': 'PASS' if holds else 'FAIL'})


# ---- ITEM2-CHECK: the engine side -----------------------------------------------------------------------------

def item2_engine(root):
    r = sf.Runner(root)
    syn = sf.Syn()
    edits = [('# synthetic', ['# synthetic', '', 'Preface line one.'])]
    pd = sf.patch_doc(syn.H, edits)
    base = {'patch_sha': sf.sha(pd), 'files': {'syn/patch.json': pd}}

    def run(args, variant=None):
        v = dict(base)
        v.update(variant or {})
        c, p, s, _ = syn.build(v)
        code, res = r.cli(syn.repo, ['coverage', '--commit', syn.H] + args, c, p, s)
        return code, ((res or {}).get('stop') or {}).get('class'), (res or {}).get('outcome')

    zc = [{'id': 'zc', 'profiles': ['axiom-Z', 'beta-word', 'Z-premise'], 'final_profiles': ['axiom-Z']}]
    got = run(['--check', 'zc'])
    case('ITEM2-CHECK/1', 'the explicit known check on a valid configuration runs (no stop)', got,
         got[0] in (0, 10, 20) and got[1] is None)
    got = run([])
    case('ITEM2-CHECK/2', 'no --check on a valid configuration: USAGE (exit 64)', got, got[0] == 64)
    got = run(['--check', 'nope'])
    case('ITEM2-CHECK/3', 'an unknown --check on a valid configuration: USAGE (exit 64)', got, got[0] == 64)
    got = run(['--check', 'zc', '--check', 'zc'])
    case('ITEM2-CHECK/4', 'a repeated --check on a valid configuration: USAGE (exit 64)', got, got[0] == 64)
    got = run(['--check', 'zc'], {'extra': {'checks': [dict(zc[0], default_for=['coverage'])]}})
    case('ITEM2-CHECK/5', 'a check carrying default_for: ERROR CONFIG_INVALID even with --check naming it', got,
         got[:2] == (65, 'CONFIG_INVALID'))
    got = run([], {'extra': {'checks': [dict(zc[0], default_for=['coverage'])]}})
    case('ITEM2-CHECK/6', 'a check carrying default_for and no --check: ERROR CONFIG_INVALID (the default is not '
                          'used)', got, got[:2] == (65, 'CONFIG_INVALID'))
    got = run(['--check', 'zc'], {'extra': {'checks': [{'id': 'zc', 'profiles': zc[0]['profiles']}]}})
    case('ITEM2-CHECK/7', 'a check without final_profiles: ERROR CONFIG_INVALID', got,
         got[:2] == (65, 'CONFIG_INVALID'))
    got = run(['--check', 'zc'], {'extra': {'checks': zc + zc}})
    case('ITEM2-CHECK/8', 'two checks with one id: ERROR CONFIG_INCONSISTENT', got,
         got[:2] == (65, 'CONFIG_INCONSISTENT'))


# ---- ITEM2-CHECK: the workflow arm (I2-1) ---------------------------------------------------------------------

def item2_arm(repo_root):
    wf = os.path.join(repo_root, '.github', 'workflows', 'ledger-coverage.yml')
    arm = rdc.arm_text(wf)
    case('ITEM2-CHECK/9', 'the retained workflow arm equals the adopted command with --check item2 after --commit',
         arm, arm == rdc.EXPECTED_ARM)
    base = rdc.EXPECTED_ARM
    variants = {
        'no --check': base.replace(' --check item2', ''),
        'another check': base.replace('--check item2', '--check item7'),
        '--check moved to the end': base.replace(' --check item2', '').replace(' ;;', ' --check item2 ;;'),
        'a --classify operand dropped': base.replace(' --classify "$F:$D/hit-classifications.json"', ''),
        'two --classify operands reordered': base.replace(
            '--classify "$F:$D/context-adjudications.json" --classify "$F:$D/hit-classifications.json"',
            '--classify "$F:$D/hit-classifications.json" --classify "$F:$D/context-adjudications.json"'),
        'a --classify operand changed': base.replace('gr58-hit-classification-v3', 'gr58-hit-classification-v4'),
        'an expansion unquoted': base.replace('--commit "$X"', '--commit $X'),
    }
    got = {k: v != rdc.EXPECTED_ARM for k, v in variants.items()}
    case('ITEM2-CHECK/10', 'each altered arm differs from the adopted command (I2-1 rejects it)', got, all(got.values()))


# ---- ITEM2-CHECK: the S11-2a and S11-2b evidence through the independent gate ---------------------------------

E = 'e837e3dbaa605efc867a213f3345cee14c36d8f5'
X = '1' * 40
PLANTED = 'book/ch18-beyond.md'
LINE = 41
A1P = G.S11_A1_DIRECTORY + '/retirement-config.json'
CFG_BYTES = b'{"config_id": "a1", "version": 1}\n'
CFG = {'config_id': 'a1', 'version': 1, 'path': A1P, 'commit': 'f' * 40,
       'blob_sha256': __import__('hashlib').sha256(CFG_BYTES).hexdigest()}


def pin_table(rows, earlier=None):
    out = '# PREREG\n\n'
    if earlier is not None:
        out += '### 1.1 Record pins\n\n| file | sha256 |\n|---|---|\n' + ''.join(
            '| `%s` | `%s` |\n' % r for r in earlier) + '\n'
    out += '### 2.1 Record pins\n\n| file | sha256 |\n|---|---|\n' + ''.join('| `%s` | `%s` |\n' % r for r in rows)
    return out.encode()


def s11_repo(fx, files=None):
    """A fixture repository holding F: the configuration at A1P and the PREREG.md beside it listing it (S11-2a
    supplement). Returns (repo, F)."""
    d = G.S11_A1_DIRECTORY
    base = {A1P: CFG_BYTES, d + '/PREREG.md': pin_table([('retirement-config.json', CFG['blob_sha256'])])}
    base.update(files or {})
    base = {k: v for k, v in base.items() if v is not None}
    repo = os.path.join(fx.root, 'repo')
    return repo, GST.git_commit(repo, base)


def _profiles():
    out = [{'name': n, 'kind': 'review', 'source_commit': c, 'path': p, 'blob_sha256': b, 'pattern_sha256': h}
           for n, (c, p, b, h) in sorted(G.ITEM2_PROFILES.items())]
    out.append({'name': 'ptr', 'kind': 'deny', 'source_commit': 'a' * 40, 'path': 'x.json', 'blob_sha256': 'd' * 64,
                'pattern_sha256': 'e' * 64})
    return out


def _result(commit, items, deny):
    rv = sorted(G.ITEM2_PROFILES)
    return GST.tool_result('FAIL' if any(i['decision'] == 'FAIL' for i in items) else
                           ('REVIEW_REQUIRED' if items else 'PASS'), items, operation='coverage',
                           evaluated={'commit': commit}, config=dict(CFG), profiles=_profiles(),
                           profiles_evaluated={commit: sorted(rv + (['ptr'] if deny else []))})


def s11_fixture(fx, mutate=None, repo_files=None):
    """S11-2a: the named unmutated run at E and the run at its planted child, as the recorder retains them, both on the
    real runner's argv shape: --config <standin(F, P, b)>:P, results naming P and S; the gate run with --freeze F,
    --config P and the commit under check F (S11-2a supplement)."""
    repo, F = s11_repo(fx, repo_files)
    standin = G.s11_standin(F, A1P, GST.blob_id(CFG_BYTES))
    fx.ctx = G.Ctx(repo, F, F, A1P)
    subj = '%s:%d' % (PLANTED, LINE)
    before = _result(E, [], False)
    after = _result(X, [GST.item('deny-match', 'FAIL', subject=subj, obligation='TERMS'),
                        GST.item('unclassified', 'REVIEW_REQUIRED', subject=subj, obligation='TERMS')], True)
    argv0 = ['coverage', '--config', standin + ':' + A1P, '--out', '/o/1', '--repo', '.', '--commit', E,
             '--check', 'item2']
    argv1 = ['coverage', '--config', standin + ':' + A1P, '--out', '/o/2', '--repo', '.', '--commit', X,
             '--check', 'item2']
    mutation = [{'path': PLANTED, 'before': 'a' * 40, 'after': 'b' * 40}]
    bindings = {'new_line': subj}
    st = {'before': before, 'after': after, 'argv0': argv0, 'argv1': argv1, 'mutation': mutation,
          'bindings': bindings, 'repo': repo, 'F': F, 'standin': standin, 'fx': fx}
    if mutate:
        mutate(st)
    fx.row('S11-2a', {'outcome': 'FAIL', 'classes_include': ['unclassified', 'deny-match'],
                      'sites': [{'subject': '$new_line', 'classes_include': ['unclassified'],
                                 'added_relative_to_unmutated': {'items[class=unclassified,subject=$new_line]': 1}}]},
           operations=['coverage'])
    rel = os.path.join('evidence', 'job', 'S11-2a')
    d = os.path.join(fx.root, rel)
    man = {'schema': G.SCHEMA_MAN, 'id': 'S11-2a', 'job': 'job', 'files': {}, 'cases': []}

    def put(name, doc):
        man['files'][name] = GST.sha(GST.dump(os.path.join(d, name), doc))
        return name
    bres = (json.dumps(st['before'], indent=1, sort_keys=True) + '\n').encode()
    man['cases'].append({'case': 'unmutated', 'argv': st['argv0'], 'bindings': {}, 'mutation': [],
                         'exit_file': put('u.exit', ('%d\n' % G.TOOL_EXIT[st['before']['outcome']]).encode()),
                         'result_file': put('u.result.json', bres)})
    man['cases'].append({'case': '', 'argv': st['argv1'], 'bindings': st['bindings'], 'mutation': st['mutation'],
                         'exit_file': put('m.exit', ('%d\n' % G.TOOL_EXIT[st['after']['outcome']]).encode()),
                         'result_file': put('m.result.json', st['after']),
                         'baseline_file': put('m.baseline.result.json', bres), 'baseline_argv': st['argv0']})
    GST.dump(os.path.join(d, 'manifest.json'), man)
    fx.record('S11-2a', 'PASS', rel)


def s11b_fixture(fx, check='item2'):
    fx.row('S11-2b', {'outcome': 'FAIL', 'classes_include': ['missing']}, operations=['coverage'])
    res = GST.tool_result('FAIL', [GST.item('missing', 'FAIL', subject='papers/x.md:3@e837e3db')],
                          operation='coverage', evaluated={'commit': X})
    rel = os.path.join('evidence', 'job', 'S11-2b')
    d = os.path.join(fx.root, rel)
    man = {'schema': G.SCHEMA_MAN, 'id': 'S11-2b', 'job': 'job', 'files': {}, 'cases': []}
    for name, doc in (('m.exit', b'20\n'), ('m.result.json', res)):
        man['files'][name] = GST.sha(GST.dump(os.path.join(d, name), doc))
    man['cases'].append({'case': '', 'argv': ['coverage', '--config', 'f' * 40 + ':p/c.json', '--out', '/o/3',
                                              '--commit', X, '--check', check],
                         'bindings': {}, 'mutation': [], 'exit_file': 'm.exit', 'result_file': 'm.result.json'})
    GST.dump(os.path.join(d, 'manifest.json'), man)
    fx.record('S11-2b', 'PASS', rel)


def gate_rows(root, name, build):
    fx = GST.Fixture(os.path.join(root, name))
    build(fx)
    code, res = fx.run()
    rows = {r['id']: sorted(set(r.get('findings', []))) for r in res.get('rows', [])}
    return res.get('verdict'), rows


def s11_binding_controls(root):
    """The S11-2a supplement (adopted at 6de7efa4): both runs bound to the configuration (F, P, S) admitted at F."""
    d = G.S11_A1_DIRECTORY

    def refused(v, rows):
        return v == 'GATE_FAIL' and 'raw-evidence-missing' in rows.get('S11-2a', [])

    def both(st, path=None, sha=None):
        for k in ('before', 'after'):
            st[k]['config'] = dict(st[k]['config'], **({'path': path} if path else {}),
                                   **({'blob_sha256': sha} if sha else {}))
        if path:
            for k in ('argv0', 'argv1'):
                i = st[k].index('--config') + 1
                st[k][i] = st[k][i].split(':', 1)[0] + ':' + path
    v, rows = gate_rows(root, 'bind-pos', lambda fx: s11_fixture(fx))
    case('S11-2a-BIND-POS', 'both runs name --config <stand-in>:P and carry P and S; F is --freeze and the commit '
                            'under check; F\'s pin table lists P with S: GATE_HOLDS', (v, rows),
         v == 'GATE_HOLDS' and rows.get('S11-2a') == [])
    out = {}
    for name, mut in (('other path', lambda st: both(st, path=d + '/other-config.json')),
                      ('other digest', lambda st: both(st, sha='9' * 64))):
        out[name] = gate_rows(root, 'bind-both-' + name.replace(' ', '-'), lambda fx, m=mut: s11_fixture(fx, m))
    case('S11-2a-BOTH-ARMS-SUBST', 'both runs, argv and results alike, name another configuration (another path, or '
                                   'the same path with another digest): refused, raw-evidence-missing', out,
         all(refused(*x) for x in out.values()))
    decoy = 'verification/audits/other-plan/retirement-config.json'

    def use_decoy(st):
        st['fx'].ctx = G.Ctx(st['repo'], st['F'], st['F'], decoy)
        both(st, path=decoy)
    v, rows = gate_rows(root, 'bind-decoy', lambda fx: s11_fixture(fx, use_decoy, repo_files={
        decoy: CFG_BYTES, 'verification/audits/other-plan/PREREG.md': pin_table([('retirement-config.json',
                                                                                 CFG['blob_sha256'])])}))
    case('S11-2a-DECOY-CONFIG', 'a second configuration in another directory, listed beside it, used by the gate\'s '
                                '--config and both runs: refused (outside the admitted record directory)', (v, rows),
         refused(v, rows))

    v, rows = gate_rows(root, 'bind-one-arm', lambda fx: s11_fixture(fx, lambda st: (
        st['argv1'].__setitem__(st['argv1'].index('--config') + 1, st['standin'] + ':' + d + '/x.json'))))
    case('S11-2a-ONE-ARM-SUBST', 'only the mutated run names another configuration: refused', (v, rows),
         refused(v, rows))
    v, rows = gate_rows(root, 'bind-pin-mismatch', lambda fx: s11_fixture(fx, repo_files={
        d + '/PREREG.md': pin_table([('retirement-config.json', '7' * 64)])}))
    case('S11-2a-PIN-MISMATCH', 'the pin table lists P with another SHA-256: refused', (v, rows), refused(v, rows))
    v, rows = gate_rows(root, 'bind-pin-earlier', lambda fx: s11_fixture(fx, repo_files={
        d + '/PREREG.md': pin_table([('other.json', '7' * 64)],
                                    earlier=[('retirement-config.json', CFG['blob_sha256'])])}))
    case('S11-2a-PIN-EARLIER-SUBSECTION', 'P listed only in an earlier Record pins subsection: refused', (v, rows),
         refused(v, rows))
    v, rows = gate_rows(root, 'bind-pin-two-rows', lambda fx: s11_fixture(fx, repo_files={
        d + '/PREREG.md': pin_table([('retirement-config.json', CFG['blob_sha256']),
                                     ('retirement-config.json', CFG['blob_sha256'])])}))
    case('S11-2a-PIN-TWO-ROWS', 'the last Record pins subsection lists P in two rows (both with S): refused',
         (v, rows), refused(v, rows))
    later = pin_table([('other.json', '7' * 64)]) + (
        '\n### 3.1 Record inventory\n\n| file | sha256 |\n|---|---|\n| `retirement-config.json` | `%s` |\n'
        % CFG['blob_sha256']).encode()
    v, rows = gate_rows(root, 'bind-pin-later-heading', lambda fx: s11_fixture(fx, repo_files={
        d + '/PREREG.md': later}))
    case('S11-2a-PIN-LATER-HEADING', 'a later heading that is not Record pins carries a table listing P with S, while '
                                     'the last Record pins subsection does not list P: refused', (v, rows),
         refused(v, rows))

    def literal_other_freeze(st):
        f2 = GST.git_commit(st['repo'], {'notes.txt': b'later\n'})
        st['fx'].ctx = G.Ctx(st['repo'], st['F'], f2, A1P)
        for k in ('argv0', 'argv1'):
            st[k][st[k].index('--config') + 1] = f2 + ':' + A1P
    v, rows = gate_rows(root, 'bind-literal-other-freeze', lambda fx: s11_fixture(fx, literal_other_freeze))
    case('S11-2a-LITERAL-OTHER-FREEZE', 'both runs name a literal --config F\':P and the gate\'s --freeze is F\', a '
                                        'commit whose pin table lists P with S and which holds P, other than the '
                                        'commit under check: refused', (v, rows), refused(v, rows))
    out = {}
    for name, ctxf in (('no freeze', lambda st: G.Ctx(st['repo'], st['F'], None, A1P)),
                       ('no config', lambda st: G.Ctx(st['repo'], st['F'], st['F'], None))):
        out[name] = gate_rows(root, 'bind-' + name.replace(' ', '-'),
                              lambda fx, f_=ctxf: s11_fixture(fx, lambda st: setattr(st['fx'], 'ctx', f_(st))))
    case('S11-2a-NO-FREEZE', 'the gate run without --freeze, or without --config: refused', out,
         all(refused(*x) for x in out.values()))

    def wrong_freeze(st):
        f2 = GST.git_commit(st['repo'], {'notes.txt': b'later\n'})
        st['fx'].ctx = G.Ctx(st['repo'], st['F'], f2, A1P)
    v, rows = gate_rows(root, 'bind-wrong-freeze', lambda fx: s11_fixture(fx, wrong_freeze))
    case('S11-2a-WRONG-FREEZE', '--freeze names a commit other than the commit under check whose pin table lists the '
                                'configuration: refused', (v, rows), refused(v, rows))

    def other_parent(st):
        bad = G.s11_standin('3' * 40, A1P, GST.blob_id(CFG_BYTES))
        for k in ('argv0', 'argv1'):
            st[k][st[k].index('--config') + 1] = bad + ':' + A1P
    v, rows = gate_rows(root, 'bind-standin-parent', lambda fx: s11_fixture(fx, other_parent))
    case('S11-2a-STAND-IN-PARENT', 'both runs name a stand-in whose parent is not the commit under check: refused',
         (v, rows), refused(v, rows))

    def forged(st):
        bad = G.s11_standin(st['F'], A1P, GST.blob_id(b'{"other": 1}\n'))
        for k in ('argv0', 'argv1'):
            st[k][st[k].index('--config') + 1] = bad + ':' + A1P
    v, rows = gate_rows(root, 'bind-forged', lambda fx: s11_fixture(fx, forged))
    case('S11-2a-FORGED-STAND-IN', 'both runs name a stand-in id derived from another blob: refused', (v, rows),
         refused(v, rows))
    v, rows = gate_rows(root, 'bind-p-absent', lambda fx: s11_fixture(fx, repo_files={A1P: None}))
    case('S11-2a-P-ABSENT-AT-F', 'the pin table lists P with S but F\'s tree does not hold P: refused', (v, rows),
         refused(v, rows))
    # the gate's restated stand-in id equals the runner's (a1_controls.simulated_freeze over gitobj.Overlay.derive)
    from ledger_coverage.adapters import a1_controls as a1c
    from ledger_coverage.engine import gitobj
    ov = gitobj.Overlay()
    F0 = ov.add_commit({'x': b'x\n'}, [], 'F')
    tool = a1c.simulated_freeze(ov, F0, A1P, CFG_BYTES)
    gate = G.s11_standin(F0, A1P, GST.blob_id(CFG_BYTES))
    case('S11-2a-STANDIN-MATCHES-TOOL', 'the gate\'s standin(F, P, b) equals the id of the runner\'s in-memory '
                                        'stand-in for the same F, P and bytes', {'tool': tool, 'gate': gate},
         tool == gate)


def tr5_release_controls(root):
    """RC_TR5 reads the pin table as DESIGN-r6 sec. 6.3 fixes it (R6.REC.16): the last subsection headed
    `### N.N Record pins`, the reader the gate shares with the S11-2a binding."""
    d = G.S11_A1_DIRECTORY
    numbered = pin_table([('retirement-config.json', CFG['blob_sha256'])])
    variants = {
        'numbered': numbered,
        'unnumbered ###': numbered.replace(b'### 2.1 Record pins', b'### Record pins'),
        'unnumbered ##': numbered.replace(b'### 2.1 Record pins', b'## Record pins'),
        'earlier only': pin_table([('other.json', '7' * 64)], earlier=[('retirement-config.json', CFG['blob_sha256'])]),
        'later non-pins table': pin_table([('other.json', '7' * 64)]) + (
            '\n### 3.1 Record inventory\n\n| file | sha256 |\n|---|---|\n| `retirement-config.json` | `%s` |\n'
            % CFG['blob_sha256']).encode(),
    }
    out = {}
    for name, prereg in variants.items():
        fx = GST.Fixture(os.path.join(root, 'tr5-' + name.replace(' ', '-').replace('#', 'h')))
        repo, F = s11_repo(fx, {d + '/PREREG.md': prereg})
        ctx = G.Ctx(repo, F, F, A1P)
        out[name] = {'tr5_release': G.tr5_release(ctx), 'evaluate_release': G.evaluate_release(ctx, G.RC_TR5, {}),
                     's11_binding': G.s11_binding(ctx) is not None}
    want = {'numbered': True, 'unnumbered ###': False, 'unnumbered ##': False, 'earlier only': False,
            'later non-pins table': False}
    case('TR5-RELEASE-PIN-HEADING', 'the TR5 release check holds at F whose last `### N.N Record pins` subsection '
                                    'lists the configuration, and agrees with the S11-2a binding; an unnumbered '
                                    'Record pins heading, a listing only in an earlier pins subsection, or one only '
                                    'in a later table that is not Record pins does not count', out,
         all(out[k]['tr5_release'] is want[k] and out[k]['evaluate_release'] is want[k] and
             out[k]['s11_binding'] is want[k] for k in want))


def _release_gate(root, name, rid, rc, files, ctx_fn, mode='NOT RUN'):
    """A gate run at a fixture F (s11_repo plus `files`): one clean row and the deferred row `rid` with release check
    `rc`, recorded NOT RUN ('NOT RUN'), run with its evidence ('run'), or run with its evidence missing ('missing').
    Returns {release, verdict, findings of rid}."""
    fx = GST.Fixture(os.path.join(root, 'rel-' + name))
    GST.clean(fx)
    fx.row(rid, {'outcome': 'PASS'}, status_allowed=['PASS', 'NOT RUN'],
           not_run={'reason': 'deferred', 'release_condition': 'c', 'release_check': rc})
    if mode == 'NOT RUN':
        fx.record(rid, 'NOT RUN', None)
    else:
        ev = fx.evidence(rid, {'': {'exit': 0, 'result': GST.tool_result('PASS')}})
        if mode == 'missing':
            ev = ev + '-absent'
        fx.record(rid, 'PASS', ev, {'exit': 0, 'outcome': 'PASS'})
    repo, F = s11_repo(fx, files)
    fx.ctx = ctx_fn(repo, F)
    release = G.evaluate_release(fx.ctx, rc, {})
    code, res = fx.run()
    rows = {r['id']: sorted(set(r.get('findings', []))) for r in res.get('rows', [])}
    return {'release': release, 'verdict': res.get('verdict'), 'findings': rows.get(rid)}


def release_gate_controls(root):
    """TR5 and RT-T at a fixture F carrying the configuration and a design-form pin table (DESIGN-r6 sec. 6.3): a
    release check that holds makes NOT RUN a gate failure, so the obligation can only be met by a run with its
    evidence; one that does not hold leaves the row deferred. Wrong bindings and inadmissible evidence do not hold."""
    d = G.S11_A1_DIRECTORY
    sha = CFG['blob_sha256']
    pins = lambda rows, **kw: {d + '/PREREG.md': pin_table(rows, **kw)}
    good = pins([('retirement-config.json', sha)])
    at_f = lambda repo, F: G.Ctx(repo, F, F, A1P)

    def held(x):
        return x['release'] is True
    def deferred_ok(x):
        return x['release'] is False and x['verdict'] == 'GATE_HOLDS' and x['findings'] == []
    def demanded(x, finding):
        return x['release'] is True and x['verdict'] == 'GATE_FAIL' and finding in (x['findings'] or [])

    # TR5 (RC_TR5)
    t = lambda n, files, ctx_fn=at_f, mode='NOT RUN': _release_gate(root, 'tr5-' + n, 'TR5', G.RC_TR5, files,
                                                                    ctx_fn, mode)
    x = t('pos-run', good, mode='run')
    case('TR5-REL-POS-RUN', 'at F listing the configuration in its last `### N.N Record pins` subsection, the release '
                            'check holds and TR5 run with its evidence passes the gate', x,
         held(x) and x['verdict'] == 'GATE_HOLDS' and x['findings'] == [])
    x = t('not-run', good)
    case('TR5-REL-NOT-RUN', 'the same F with TR5 recorded NOT RUN: the gate fails (status-not-allowed)', x,
         demanded(x, 'status-not-allowed'))
    x = t('evidence-missing', good, mode='missing')
    case('TR5-REL-EVIDENCE-MISSING', 'the same F with TR5 recorded PASS and its evidence absent: the gate fails '
                                     '(raw-evidence-missing)', x, demanded(x, 'raw-evidence-missing'))
    later = pin_table([('other.json', '7' * 64)]) + (
        '\n### 3.1 Record inventory\n\n| file | sha256 |\n|---|---|\n| `retirement-config.json` | `%s` |\n'
        % sha).encode()
    num = pin_table([('retirement-config.json', sha)])
    variants = {
        'no-freeze-or-config': (good, lambda repo, F: G.Ctx(repo, F, None, None)),
        'wrong-config-path': (good, lambda repo, F: G.Ctx(repo, F, F, d + '/other-config.json')),
        'config-absent-at-f': (dict(good, **{A1P: None}), at_f),
        'earlier-subsection-only': (pins([('other.json', '7' * 64)], earlier=[('retirement-config.json', sha)]),
                                    at_f),
        'unnumbered-h3': ({d + '/PREREG.md': num.replace(b'### 2.1 Record pins', b'### Record pins')}, at_f),
        'unnumbered-h2': ({d + '/PREREG.md': num.replace(b'### 2.1 Record pins', b'## Record pins')}, at_f),
        'numbered-h4': ({d + '/PREREG.md': num.replace(b'### 2.1 Record pins', b'#### 2.1 Record pins')}, at_f),
        'later-numbered-non-pins': ({d + '/PREREG.md': later}, at_f),
        'freeze-abbreviated': (good, lambda repo, F: G.Ctx(repo, F, F[:12], A1P)),
    }
    out = {}
    for n, (files, cf) in variants.items():
        out[n] = t(n, files, cf)
    # --freeze naming another commit F', whose pin table does not list the configuration
    def other_f(repo, F):
        f2 = GST.git_commit(repo, {d + '/PREREG.md': pin_table([('other.json', '7' * 64)])})
        return G.Ctx(repo, F, f2, A1P)
    out['freeze-another-f'] = t('freeze-another-f', good, other_f)
    case('TR5-REL-WRONG-BINDING', 'no --freeze/--config; --config naming another path; the configuration absent at F; '
                                  'listed only in an earlier pins subsection, under an unnumbered or #### heading, or '
                                  'in a later numbered heading that is not Record pins; --freeze abbreviated or naming '
                                  'another F\' that does not list it: the release check does not hold and TR5 stays '
                                  'deferred', out, all(deferred_ok(v) for v in out.values()))
    x = t('digest-mismatch', pins([('retirement-config.json', '7' * 64)]))
    x['s11_binding'] = G.s11_binding(G.Ctx(*_repo_of(root, 'tr5-digest-mismatch'), A1P)) is not None
    case('TR5-REL-DIGEST-MISMATCH', 'F lists the configuration with another SHA-256: RC_TR5 (a listing test) holds, '
                                    'so TR5 NOT RUN still fails the gate; the S11-2a binding refuses the same F', x,
         demanded(x, 'status-not-allowed') and x['s11_binding'] is False)

    # RT-T (RC_RTT): a reviewed record of a sec. 8.2 kind referenced by the configuration at the commit under check
    kind = sorted(G.SEC82_KINDS)[0]
    rec = b'{"record": 1}\n'
    rsha = hashlib.sha256(rec).hexdigest()

    def rtt_files(kind=kind, listed_sha=None, review=None, list_review=True, schema='oi-review-record/1'):
        rv = review if review is not None else {
            'schema': schema, 'reviewer': 'reviewer-y', 'reviewed': {'path': d + '/rec.json', 'blob_sha256': rsha},
            'verdicts': [{'item': 'i', 'verdict': 'accept'}]}
        refs = [{'kind': kind, 'path': d + '/rec.json', 'blob_sha256': listed_sha or rsha}]
        if list_review:
            refs.append({'kind': 'review', 'path': d + '/rec.review.json'})
        cfg = dict(json.loads(CFG_BYTES.decode()), records=refs)
        cb = (json.dumps(cfg, indent=1, sort_keys=True) + '\n').encode()
        return {A1P: cb, d + '/rec.json': rec, d + '/rec.review.json': (json.dumps(rv) + '\n').encode(),
                d + '/PREREG.md': pin_table([('retirement-config.json', hashlib.sha256(cb).hexdigest())])}
    r = lambda n, files, ctx_fn=at_f, mode='NOT RUN': _release_gate(root, 'rtt-' + n, 'RT-T', G.RC_RTT, files,
                                                                    ctx_fn, mode)
    x = r('pos-run', rtt_files(), mode='run')
    case('RT-T-REL-POS-RUN', 'the configuration at the commit under check references a sec. 8.2 record with its '
                             'SHA-256 and a review accepting exactly that blob: the release check holds and RT-T run '
                             'with its evidence passes the gate', x,
         held(x) and x['verdict'] == 'GATE_HOLDS' and x['findings'] == [])
    x = r('not-run', rtt_files())
    case('RT-T-REL-NOT-RUN', 'the same with RT-T recorded NOT RUN: the gate fails (status-not-allowed)', x,
         demanded(x, 'status-not-allowed'))
    x = r('evidence-missing', rtt_files(), mode='missing')
    case('RT-T-REL-EVIDENCE-MISSING', 'the same with RT-T recorded PASS and its evidence absent: the gate fails '
                                      '(raw-evidence-missing)', x, demanded(x, 'raw-evidence-missing'))
    base_rv = {'schema': 'oi-review-record/1', 'reviewer': 'reviewer-y',
               'reviewed': {'path': d + '/rec.json', 'blob_sha256': rsha}}
    out = {
        'no-config-argument': r('no-config', rtt_files(), lambda repo, F: G.Ctx(repo, F, F, None)),
        'wrong-config-path': r('wrong-path', rtt_files(), lambda repo, F: G.Ctx(repo, F, F, d + '/other.json')),
        'record-digest-mismatch': r('digest', rtt_files(listed_sha='7' * 64)),
        'record-bytes-differ-from-listing-and-review': r('bytes', rtt_files(listed_sha='7' * 64, review=dict(
            base_rv, reviewed={'path': d + '/rec.json', 'blob_sha256': '7' * 64},
            verdicts=[{'item': 'i', 'verdict': 'accept'}]))),
        'not-a-sec82-kind': r('kind', rtt_files(kind='review-scope')),
        'review-of-another-blob': r('other-blob', rtt_files(review=dict(base_rv, reviewed={
            'path': d + '/rec.json', 'blob_sha256': '7' * 64}, verdicts=[{'item': 'i', 'verdict': 'accept'}]))),
        'review-rejects': r('rejects', rtt_files(review=dict(base_rv, verdicts=[{'item': 'i', 'verdict': 'reject'}]))),
        'review-no-verdicts': r('no-verdicts', rtt_files(review=dict(base_rv, verdicts=[]))),
        'review-wrong-schema': r('schema', rtt_files(schema='oi-review-record/0')),
        'review-not-listed': r('unlisted', rtt_files(list_review=False)),
    }
    # the configuration at F only, not at the commit under check
    def later_commit(repo, F):
        c = GST.git_commit(repo, {A1P: CFG_BYTES})
        return G.Ctx(repo, c, F, A1P)
    out['config-only-at-f'] = r('only-at-f', rtt_files(), later_commit)
    case('RT-T-REL-INADMISSIBLE', 'no --config or another path; the record\'s SHA-256 differs from its listing (also where '
                                  'the listing and the review agree with each other); a kind '
                                  'outside sec. 8.2; a review of another blob, rejecting, without verdicts, of another '
                                  'schema, or not listed; the reviewed record referenced only at F and not at the '
                                  'commit under check: the release check does not hold and RT-T stays deferred', out,
         all(deferred_ok(v) for v in out.values()))


def _repo_of(root, name):
    repo = os.path.join(root, 'rel-' + name, 'repo')
    head = subprocess.run(['git', '-C', repo, 'rev-parse', 'HEAD'], stdout=subprocess.PIPE).stdout.decode().strip()
    return repo, head, head


def item2_gate(root):
    def wrong_check(st):
        for k in ('argv0', 'argv1'):
            st[k][st[k].index('--check') + 1] = 'item7'

    def wrong_config(st):
        st['after']['config'] = dict(CFG, blob_sha256='9' * 64)

    def pin_drift(st):
        for k in ('before', 'after'):
            st[k]['profiles'][0]['pattern_sha256'] = '0' * 64

    def profile_added(st):
        st['after']['profiles_evaluated'][X] = sorted(st['after']['profiles_evaluated'][X] + ['resid'])

    def profile_omitted(st):
        st['before']['profiles_evaluated'][E] = sorted(G.ITEM2_PROFILES)[:2]

    def deny_missing(st):
        st['after']['profiles_evaluated'][X] = sorted(G.ITEM2_PROFILES)

    def deny_at_e(st):
        st['before']['profiles_evaluated'][E] = sorted(list(G.ITEM2_PROFILES) + ['ptr'])

    def baseline_not_e(st):
        other = '2' * 40
        st['argv0'][st['argv0'].index('--commit') + 1] = other
        st['before']['evaluated'] = {'commit': other}
        st['before']['profiles_evaluated'] = {other: st['before']['profiles_evaluated'][E]}

    def mutation_elsewhere(st):
        st['mutation'] = [{'path': 'book/ch17.md', 'before': 'a' * 40, 'after': 'b' * 40}]

    def two_paths(st):
        st['mutation'] = st['mutation'] + [{'path': 'book/ch17.md', 'before': 'a' * 40, 'after': 'b' * 40}]

    v, rows = gate_rows(root, 's11a-positive', lambda fx: s11_fixture(fx))
    case('ITEM2-CHECK/11', 'S11-2a evidence with --check item2 in both runs, the approved pins, the review set at E '
                           'and review plus deny at the child, the planted mutation: the gate holds', (v, rows),
         v == 'GATE_HOLDS' and rows.get('S11-2a') == [])
    negs = [('12', 'the same substituted valid check (item7) in both invocations', wrong_check),
            ('13', 'a different reviewed configuration pin in the child run', wrong_config),
            ('14', 'a profile pattern pin differing from the approved pin', pin_drift),
            ('15', 'a review profile added to the evaluated set', profile_added),
            ('16', 'a review profile omitted from the evaluated set at E', profile_omitted),
            ('17', 'the deny scan missing at the child', deny_missing),
            ('18', 'a deny profile evaluated at exact E (no exemption)', deny_at_e),
            ('19', 'the unmutated run substituted by a run on a commit other than E', baseline_not_e),
            ('20', 'the mutation recorded on another path than the planted one', mutation_elsewhere),
            ('21', 'the child changing a second path', two_paths)]
    for n, what, mut in negs:
        v, rows = gate_rows(root, 's11a-' + n, lambda fx, m=mut: s11_fixture(fx, m))
        case('ITEM2-CHECK/' + n, what + ': the gate refuses S11-2a (raw-evidence-missing, no countable baseline)',
             (v, rows), v == 'GATE_FAIL' and 'raw-evidence-missing' in rows.get('S11-2a', []))
    def no_deny(st):
        for k in ('before', 'after'):
            st[k]['profiles'] = [x for x in st[k]['profiles'] if x['kind'] != 'deny']
        st['after']['profiles_evaluated'][X] = sorted(G.ITEM2_PROFILES)
    v, rows = gate_rows(root, 's11a-24', lambda fx: s11_fixture(fx, no_deny))
    case('ITEM2-CHECK/24', 'no deny profile reported in either result, the child evaluated with the review set alone: '
                           'refused (a missing deny scan is not a clean one)', (v, rows),
         v == 'GATE_FAIL' and 'raw-evidence-missing' in rows.get('S11-2a', []))
    s11_binding_controls(root)
    tr5_release_controls(root)
    release_gate_controls(root)
    v, rows = gate_rows(root, 's11b-positive', lambda fx: s11b_fixture(fx))
    case('ITEM2-CHECK/22', 'S11-2b run under --check item2: the gate holds', (v, rows),
         v == 'GATE_HOLDS' and rows.get('S11-2b') == [])
    v, rows = gate_rows(root, 's11b-wrong', lambda fx: s11b_fixture(fx, 'item7'))
    case('ITEM2-CHECK/23', 'S11-2b run under another check: the gate refuses it', (v, rows),
         v == 'GATE_FAIL' and 'declarative-mismatch' in rows.get('S11-2b', []))


# ---- STAGING-ROLE-CHAIN and STAGING-CONFIG-REVIEWS: chain admission through the CLI ---------------------------

def _patched_authority():
    """The role selectors pointed at synthetic directories for the duration of a run (an in-process control; the
    tool's own selectors are unchanged on disk)."""
    from ledger_coverage import record_authority as ra
    saved = (ra.transition_roles, ra.authorized_record_directories)
    ra.transition_roles = (
        dict(ra.transition_roles[0], directory='syn/cls/'),
        dict(ra.transition_roles[1], directory='syn/cfg/'))
    ra.authorized_record_directories = ('syn/cfg',)
    return ra, saved


CLS_ROOT, ALLOW_ROOT = 'syn/cls/a1-staging-class-root.json', 'syn/cfg/a1-staging-allow-root.json'
CUSTODY = 'syn/custody/CUSTODY.json'


def cls_doc(n, sup):
    return {'schema': 'oi-side-change-classes/1', 'record_id': 'a1-staging-tool-landing', 'supersedes': sup,
            'author': sf.WRITER, 'classes': [{'id': 'syn-class', 'paths': ['syn/x%d' % n]}]}


def allow_doc():
    return {'schema': 'oi-term-rules/2', 'record_id': 'a1-staging-w1-w2', 'supersedes': None, 'author': sf.WRITER,
            'rules': []}


def review_doc(path, b, reviewer=sf.REVIEWER, kind=None, replaces=None, items=None, **extra):
    from ledger_coverage.engine import records as rec
    d = {'schema': 'oi-review-record/1', 'reviewer': reviewer, 'reviewed': {'path': path, 'blob_sha256': sf.sha(b)},
         'method': 'read', 'verdicts': [{'item': i, 'verdict': 'accept'} for i in
                                        (items if items is not None else rec.item_ids(json.loads(b)))]}
    if kind:
        d['kind'] = kind
        d['replaces'] = replaces
    d.update(extra)
    return d


class ChainWorld:
    """B (custody, both roots), a first-parent chain of class successors, and a configuration frozen on top that
    references a class record and its review. Every part can be varied by the cases."""

    def __init__(self, root):
        self.r = sf.Runner(root)
        self.syn = sf.Syn()
        self.repo = self.syn.repo
        edits = [('# synthetic', ['# synthetic', '', 'Preface line one.'])]
        self.pd = sf.patch_doc(self.syn.H, edits)

    def chain(self, b_extra=None, steps=(), base=None):
        """Returns (B, tip commit, {path: bytes} of the class records) for `steps`, a list of {path: bytes or None}
        applied one commit each after B."""
        repo = self.repo
        c0 = sf.jb(cls_doc(0, None))
        files = {CUSTODY: b'{"archive": true}\n', CLS_ROOT: c0, ALLOW_ROOT: sf.jb(allow_doc()),
                 'syn/cls/reviews/root.review.json': sf.jb(review_doc(CLS_ROOT, c0))}
        files.update(b_extra or {})
        B = repo.derive(base or self.syn.H, files, parents=[base or self.syn.H], subject='B')
        cur = B
        for st in steps:
            cur = repo.derive(cur, st, parents=[cur], subject='step')
        return B, cur

    def successor(self, n, prev_path, prev_bytes, path=None):
        b = sf.jb(cls_doc(n, {'path': prev_path, 'blob_sha256': sf.sha(prev_bytes)}))
        path = path or 'syn/cls/a1-staging-class-v%d.json' % n
        return path, b, {path: b, 'syn/cls/reviews/v%d.review.json' % n: sf.jb(review_doc(path, b))}

    def config(self, tip, pin, B, prior=None, desc=None, extra_files=None, records_extra=(), variant=None):
        """The configuration commit on top of `tip`, referencing `pin` (path, bytes) and its review; the transition
        descriptor and prior declaration in the configuration directory."""
        repo = self.repo
        K = repo.derive(tip, {}, parents=[tip], subject='K')
        c0 = repo.read(B, CLS_ROOT)
        d = desc if desc is not None else {
            'schema': 'oi-a1-staging-transition/1', 'base': B,
            'custody': {'path': CUSTODY, 'blob_sha256': sf.sha(repo.read(B, CUSTODY))},
            'class_root': {'path': CLS_ROOT, 'blob_sha256': sf.sha(c0)},
            'allow_root': {'path': ALLOW_ROOT, 'blob_sha256': sf.sha(repo.read(B, ALLOW_ROOT))}}
        files = {'syn/cfg/a1-staging-transition.json': sf.jb(d) if isinstance(d, dict) else d,
                 'syn/cfg/a1-staging-prior.json': sf.jb(prior if prior is not None else
                                                       {'schema': 'oi-a1-staging-prior/1', 'freeze': None})}
        files.update(extra_files or {})
        recs = []
        if pin is not None:
            pp, pb = pin
            rv = pp.rsplit('/', 1)[0] + '/reviews/' + pp.rsplit('/', 1)[1][:-5] + '.pin-review.json'
            files[rv] = sf.jb(review_doc(pp, pb))
            recs = [{'kind': 'record', 'path': pp, 'blob_sha256': sf.sha(pb)},
                    {'kind': 'review', 'path': rv, 'blob_sha256': sf.sha(files[rv])}]
        recs += list(records_extra)
        v = {'patch_sha': sf.sha(self.pd), 'files': dict({'syn/patch.json': self.pd}, **files), 'add_records': recs}
        v.update(variant or {})
        c, p, s, allf = self.syn.build(v, at=K)
        return c, p, s, allf

    def run(self, c, p, listed=None, F=None, drop=()):
        from ledger_coverage.adapters import host_fixture as hf
        from ledger_coverage.engine import cli
        w = hf.World(self.repo, c)
        if F is None:
            F = hf.freeze(self.repo, c, p, listed=listed)
            if drop:
                F = self.repo.derive(F, {q: None for q in drop}, parents=self.repo.parents(F), subject='F less')
        argv = ['coverage', '--config', '%s:%s' % (F, p), '--out', self.r.out()] + w.args(F) + \
            ['--commit', self.syn.H, '--check', 'zc']
        ra, saved = _patched_authority()
        try:
            code, res = cli.run(argv, repo=self.repo, harness=False, stderr=io.StringIO(),
                                control=w.control(w.checkout()))
        finally:
            ra.transition_roles, ra.authorized_record_directories = saved
        res = res or {}
        return code, (res.get('stop') or {}).get('class'), (res.get('stop') or {}).get('message', ''), \
            res.get('transition'), F, res


def role_chain(root):
    W = ChainWorld(root)
    c0 = sf.jb(cls_doc(0, None))
    p1, b1, f1 = W.successor(1, CLS_ROOT, c0)
    p2, b2, f2 = W.successor(2, p1, b1)

    def refused(got, phrase):
        """Refused by the transition, for the stated reason."""
        return got[0] == 65 and got[1] == 'CONFIG_UNREVIEWED' and 'transition' in got[2] and phrase in got[2]
    why = {'3': 'not the current class tip', '4': 'not the current class tip', '5': 'not exactly the root',
           '6': 'second root', '7': 'does not extend the current tip', '8': 'does not extend the current tip',
           '9': 'is deleted, renamed, rewritten', '10': 'is deleted, renamed, rewritten',
           '11': 'is deleted, renamed, rewritten', '12': 'is not a regular file', '13': 'is not JSON',
           '14': 'with record_id', '15': 'does not hash to the descriptor', '16': 'not on the first-parent chain',
           '17': 'custody archive', '18': 'exactly the keys'}

    B, tip = W.chain(steps=[f1, f2])
    c, p, s, _ = W.config(tip, (p2, b2), B)
    got = W.run(c, p)
    case('STAGING-ROLE-CHAIN/1', 'B holds exactly the two roots; two appended successors; the configuration pins the '
                                 'exact class tip: admitted, the tip reported', got[:4],
         got[1] is None and got[0] in (0, 10, 20) and (got[3] or {}).get('tips', {}).get('class') ==
         {'path': p2, 'blob_sha256': sf.sha(b2)})
    F_ok = got[4]
    # a linear suffix appended in one commit
    B, tip = W.chain(steps=[dict(f1, **f2)])
    c, p, s, _ = W.config(tip, (p2, b2), B)
    got = W.run(c, p)
    case('STAGING-ROLE-CHAIN/2', 'two successors appended in one commit, ordered by their exact references: admitted',
         got[:4], got[1] is None and got[0] in (0, 10, 20))
    negs = []
    B, tip = W.chain(steps=[f1, f2])
    negs.append(('3', 'the configuration pins the stale tip (the first successor)', W.config(tip, (p1, b1), B)))
    negs.append(('4', 'the configuration pins the root while successors exist', W.config(tip, (CLS_ROOT, c0), B)))
    Bx, tipx = W.chain(b_extra={'syn/cls/a1-staging-class-other.json': sf.jb(cls_doc(9, None))}, steps=[f1])
    negs.append(('5', 'B holds a second member in the class namespace', W.config(tipx, (p1, b1), Bx)))
    second = sf.jb(cls_doc(7, None))
    B, tip = W.chain(steps=[f1, {'syn/cls/a1-staging-class-x.json': second}])
    negs.append(('6', 'a second root (supersedes null) appended after B', W.config(tip, (p1, b1), B)))
    pf, bf, ff = W.successor(3, CLS_ROOT, c0, path='syn/cls/a1-staging-class-fork.json')
    B, tip = W.chain(steps=[f1, ff])
    negs.append(('7', 'a fork: two successors of the root', W.config(tip, (p1, b1), B)))
    alias = 'syn/cls/a1-staging-class-alias.json'
    pa, ba, fa = W.successor(4, alias, c0)
    B, tip = W.chain(steps=[fa])
    negs.append(('8', 'a successor naming the root\'s bytes at another path (reference path substitution)',
                 W.config(tip, (pa, ba), B)))
    B, tip = W.chain(steps=[f1, {CLS_ROOT: None}])
    negs.append(('9', 'the root deleted after B', W.config(tip, (p1, b1), B)))
    B, tip = W.chain(steps=[f1, {p1: b1 + b' '}])
    negs.append(('10', 'a committed successor rewritten in place', W.config(tip, (p1, b1 + b' '), B)))
    B, tip = W.chain(steps=[f1, {p1: None, 'syn/cls/a1-staging-class-moved.json': b1}])
    negs.append(('11', 'a committed successor renamed (same bytes at a different path)',
                 W.config(tip, ('syn/cls/a1-staging-class-moved.json', b1), B)))
    B, tip = W.chain(steps=[f1, {'syn/cls/a1-staging-class-link.json': ('symlink', 'x')}])
    negs.append(('12', 'a non-regular namespace member', W.config(tip, (p1, b1), B)))
    B, tip = W.chain(steps=[f1, {'syn/cls/a1-staging-class-bad.json': b'{not json'}])
    negs.append(('13', 'a malformed namespace member', W.config(tip, (p1, b1), B)))
    bad_id = sf.jb(dict(cls_doc(5, {'path': p1, 'blob_sha256': sf.sha(b1)}), record_id='tool-landing-classes'))
    B, tip = W.chain(steps=[f1, {'syn/cls/a1-staging-class-v5.json': bad_id}])
    negs.append(('14', 'a successor reusing another (legacy) record id', W.config(tip, (p1, b1), B)))
    B, tip = W.chain(steps=[f1])
    negs.append(('15', 'the descriptor names a root digest other than the root at B',
                 W.config(tip, (p1, b1), B, desc={'schema': 'oi-a1-staging-transition/1', 'base': B,
                                                  'custody': {'path': CUSTODY,
                                                              'blob_sha256': sf.sha(b'{"archive": true}\n')},
                                                  'class_root': {'path': CLS_ROOT, 'blob_sha256': '0' * 64},
                                                  'allow_root': {'path': ALLOW_ROOT,
                                                                 'blob_sha256': sf.sha(sf.jb(allow_doc()))}})))
    # a commit holding the same custody and roots, but off F's first-parent chain
    other = W.repo.derive(W.syn.H, {CUSTODY: b'{"archive": true}\n', CLS_ROOT: c0, ALLOW_ROOT: sf.jb(allow_doc()),
                                    'z': b'z'}, parents=[W.syn.H], subject='elsewhere')
    negs.append(('16', 'the descriptor\'s base is not on F\'s first-parent chain (incomplete path)',
                 W.config(tip, (p1, b1), B, desc={'schema': 'oi-a1-staging-transition/1', 'base': other,
                                                  'custody': {'path': CUSTODY,
                                                              'blob_sha256': sf.sha(b'{"archive": true}\n')},
                                                  'class_root': {'path': CLS_ROOT, 'blob_sha256': sf.sha(c0)},
                                                  'allow_root': {'path': ALLOW_ROOT,
                                                                 'blob_sha256': sf.sha(sf.jb(allow_doc()))}})))
    negs.append(('17', 'the custody archive differs from its descriptor pin',
                 W.config(tip, (p1, b1), B, desc={'schema': 'oi-a1-staging-transition/1', 'base': B,
                                                  'custody': {'path': CUSTODY, 'blob_sha256': '1' * 64},
                                                  'class_root': {'path': CLS_ROOT, 'blob_sha256': sf.sha(c0)},
                                                  'allow_root': {'path': ALLOW_ROOT,
                                                                 'blob_sha256': sf.sha(sf.jb(allow_doc()))}})))
    negs.append(('18', 'a descriptor with an extra key', W.config(tip, (p1, b1), B, desc=sf.jb(
        {'schema': 'oi-a1-staging-transition/1', 'base': B, 'namespaces': ['syn/'],
         'custody': {'path': CUSTODY, 'blob_sha256': sf.sha(b'{"archive": true}\n')},
         'class_root': {'path': CLS_ROOT, 'blob_sha256': sf.sha(c0)},
         'allow_root': {'path': ALLOW_ROOT, 'blob_sha256': sf.sha(sf.jb(allow_doc()))}}))))
    for n, what, (c, p, s, _) in negs:
        got = W.run(c, p)
        case('STAGING-ROLE-CHAIN/' + n, what + ': admission refused (ERROR CONFIG_UNREVIEWED, transition: %s)' % why[n],
             got[:3], refused(got, why[n]))
    # the descriptor or prior declaration not bound by the pin table
    c, p, s, allf = W.config(tip, (p1, b1), B)
    listed = {q: b for q, b in allf.items() if q.startswith('syn/cfg/') and q.endswith('.json') and
              '/' not in q[len('syn/cfg/'):] and not q.endswith('a1-staging-transition.json')}
    got = W.run(c, p, listed=listed)
    case('STAGING-ROLE-CHAIN/19', 'a namespace member pinned while the pin table omits the descriptor: refused',
         got[:3], refused(got, 'does not bind both'))
    listed = {q: b for q, b in allf.items() if q.startswith('syn/cfg/') and q.endswith('.json') and
              '/' not in q[len('syn/cfg/'):] and not q.endswith('a1-staging-prior.json')}
    got = W.run(c, p, listed=listed)
    case('STAGING-ROLE-CHAIN/20', 'the pin table omits the prior-freeze declaration: refused', got[:3],
         refused(got, 'does not bind both'))
    # prior-freeze continuity (the configuration pins no namespace member here, so that it is unchanged between
    # the freezes unless a case changes it; the descriptor alone puts the transition in play)
    B, t1 = W.chain(steps=[f1])
    c1, p_, s1, _ = W.config(t1, None, B)
    g1 = W.run(c1, p_)
    Fprev = g1[4]
    t2 = W.repo.derive(Fprev, f2, parents=[Fprev], subject='successor after F_prev')
    c2, p_, s2, _ = W.config(t2, None, B, prior={'schema': 'oi-a1-staging-prior/1', 'freeze': Fprev})
    got = W.run(c2, p_)
    case('STAGING-ROLE-CHAIN/21', 'a later F extends the declared prior freeze on the first-parent path, the same '
                                  'descriptor bound there, the configuration unchanged: admitted', got[:4],
         g1[1] is None and got[1] is None and (got[3] or {}).get('prior', {}).get('freeze') == Fprev)
    # a sibling freeze: a real freeze of the same configuration and descriptor on a branch from t1, off F's path
    sib_tip = W.repo.derive(t1, {'syn/sibling.txt': b's'}, parents=[t1], subject='sibling branch')
    cs, ps_, ss_, _ = W.config(sib_tip, None, B)
    gs = W.run(cs, ps_)
    sib = gs[4]
    c3, p_, s3, _ = W.config(t2, None, B, prior={'schema': 'oi-a1-staging-prior/1', 'freeze': sib})
    got = W.run(c3, p_)
    case('STAGING-ROLE-CHAIN/22', 'the declared prior freeze is a sibling freeze descending from B with the same '
                                  'descriptor and configuration, not on F\'s first-parent path: refused as not a strict '
                                  'ancestor', {'sibling_admitted': gs[:3], 'run': got[:3]},
         gs[1] is None and refused(got, 'not a strict ancestor'))
    c4, p_, s4, _ = W.config(t2, None, B, prior={'schema': 'oi-a1-staging-prior/1', 'freeze': None})
    got = W.run(c4, p_)
    case('STAGING-ROLE-CHAIN/23', 'a null prior declaration after an earlier designation: admitted by the tool (the '
                                  'return to null is refused procedurally, by the owner decision and review)',
         got[:3], got[1] is None)
    # a prior freeze whose pin table binds another descriptor
    alt = W.config(t1, None, B, desc={'schema': 'oi-a1-staging-transition/1', 'base': B,
                                          'custody': {'path': CUSTODY,
                                                      'blob_sha256': sf.sha(b'{"archive": true}\n')},
                                          'class_root': {'path': CLS_ROOT, 'blob_sha256': sf.sha(c0)},
                                          'allow_root': {'path': ALLOW_ROOT,
                                                         'blob_sha256': sf.sha(sf.jb(allow_doc()))}},
                   extra_files={'syn/cfg/padding.json': b'{"x": 1}\n'})
    ga = W.run(alt[0], alt[1])
    Fa = ga[4]
    t3 = W.repo.derive(Fa, f2, parents=[Fa], subject='after F_a')
    c5, p_, s5, _ = W.config(t3, None, B, prior={'schema': 'oi-a1-staging-prior/1', 'freeze': Fa},
                             desc={'schema': 'oi-a1-staging-transition/1', 'base': B,
                                   'custody': {'path': CUSTODY, 'blob_sha256': sf.sha(b'{"archive": true}\n')},
                                   'class_root': {'path': CLS_ROOT, 'blob_sha256': sf.sha(c0)},
                                   'allow_root': {'path': ALLOW_ROOT, 'blob_sha256': sf.sha(sf.jb(allow_doc()))},
                                   })
    # same descriptor content, so this one is admitted; then a different descriptor at F (a key order change)
    got = W.run(c5, p_)
    d_other = sf.jb({'schema': 'oi-a1-staging-transition/1', 'base': B,
                     'custody': {'path': CUSTODY, 'blob_sha256': sf.sha(b'{"archive": true}\n')},
                     'class_root': {'path': CLS_ROOT, 'blob_sha256': sf.sha(c0)},
                     'allow_root': {'path': ALLOW_ROOT, 'blob_sha256': sf.sha(sf.jb(allow_doc()))}}).rstrip() + b'\n\n'
    c6, p_, s6, _ = W.config(t3, None, B, prior={'schema': 'oi-a1-staging-prior/1', 'freeze': Fa}, desc=d_other)
    got6 = W.run(c6, p_)
    case('STAGING-ROLE-CHAIN/24', 'the prior freeze binds a descriptor whose bytes differ from F\'s: refused',
         {'same': got[:3], 'differs': got6[:3]}, got[1] is None and refused(got6, 'same transition descriptor'))
    # a changed configuration that does not supersede the configuration the prior freeze binds
    c7, p_, s7, _ = W.config(t2, None, B, prior={'schema': 'oi-a1-staging-prior/1', 'freeze': Fprev},
                             variant={'version': 2})
    got = W.run(c7, p_)
    case('STAGING-ROLE-CHAIN/25', 'the configuration changed since the prior freeze without superseding it: refused',
         got[:3], refused(got, 'does not supersede'))
    # a tool-landing class record outside the namespace while the transition is in play (review finding 11)
    from ledger_coverage import record_authority as ra1
    tlb = sf.jb({'schema': 'oi-side-change-classes/1', 'record_id': 'syn-tl-outside', 'supersedes': None,
                 'author': sf.WRITER, 'classes': [{'id': ra1.tool_landing_class_id, 'prefixes': ['tools/x/'],
                                                   'reason': 'r', 'pins': []}]})
    B9, t9 = W.chain(steps=[f1])
    c9, p9, s9, _ = W.config(t9, ('syn/other-classes/classes.json', tlb), B9,
                             extra_files={'syn/other-classes/classes.json': tlb})
    got = W.run(c9, p9)
    case('STAGING-ROLE-CHAIN/27', 'while the transition is in play, a tool-landing class record outside the namespace '
                                  'pinned by the configuration: refused (the role pin is the class tip)', got[:3],
         refused(got, 'tool-landing class pin'))
    # unauthorized directory
    from ledger_coverage import record_authority as ra0
    case('STAGING-ROLE-CHAIN/26', 'the tool\'s own selectors name fixed namespaces, root paths and record ids, and no '
                                  'configuration field or option chooses them',
         [r['directory'] + r['root'] for r in ra0.transition_roles],
         [r['directory'] + r['root'] for r in ra0.transition_roles] ==
         ['verification/audits/foundations/ledger-coverage-tool-20261123/records/a1-staging-class-root.json',
          'verification/audits/foundations/a1exit-deletion-20261121/a1-staging-allow-root.json'] and
         [r['record_id'] for r in ra0.transition_roles] == ['a1-staging-tool-landing', 'a1-staging-w1-w2'])
    return F_ok


def representative_snapshot(root):
    """Staging r2 sec. 2 / R6.EVID.8: the representative-control role binding at a verified snapshot S."""
    from ledger_coverage.engine import transition as tr
    from ledger_coverage import record_authority as ra
    W = ChainWorld(root)
    c0 = sf.jb(cls_doc(0, None))
    p1, b1, f1 = W.successor(1, CLS_ROOT, c0)
    p2, b2, f2 = W.successor(2, p1, b1)
    B, S = W.chain(steps=[f1])
    desc = {'schema': 'oi-a1-staging-transition/1', 'base': B,
            'custody': {'path': CUSTODY, 'blob_sha256': sf.sha(W.repo.read(B, CUSTODY))},
            'class_root': {'path': CLS_ROOT, 'blob_sha256': sf.sha(c0)},
            'allow_root': {'path': ALLOW_ROOT, 'blob_sha256': sf.sha(W.repo.read(B, ALLOW_ROOT))}}
    roles = (dict(ra.transition_roles[0], directory='syn/cls/'), dict(ra.transition_roles[1], directory='syn/cfg/'))
    M_same = W.repo.derive(S, {'notes/m.txt': b'm\n'}, parents=[S], subject='M landing the same tip')
    M_ahead = W.repo.derive(S, f2, parents=[S], subject='M with a newer class tip')
    off = W.repo.derive(W.syn.H, {'notes/o.txt': b'o\n'}, parents=[W.syn.H], subject='M off B')

    def run(M):
        try:
            got = tr.representative_binding(W.repo, B, S, M, roles, desc)
            return 'ok', got['class_tip_at_M']
        except tr.Refused as exc:
            return 'refused', str(exc)
    got = run(M_same)
    case('STAGING-ROLE-CHAIN/28', 'R6.EVID.8 snapshot S on the verified path B..S; the class tip resolved at S equals '
                                  'the landed class tip in M (path and digest): the role binding holds', got,
         got == ('ok', {'path': p1, 'blob_sha256': sf.sha(b1)}))
    got = run(M_ahead)
    case('STAGING-ROLE-CHAIN/29', 'M\'s landed class tip is newer than the tip at S: refused (the affected controls stay '
                                  'open)', got, got[0] == 'refused' and 'not the landed class tip in M' in got[1])
    got = run(off)
    case('STAGING-ROLE-CHAIN/30', 'B is not on M\'s first-parent chain: the role binding cannot be verified (refused)',
         got, got[0] == 'refused' and 'not on the first-parent chain' in got[1])
    bad = W.repo.derive(S, {'syn/cls/a1-staging-class-x.json': sf.jb(cls_doc(7, None))}, parents=[S], subject='S2')
    try:
        tr.representative_binding(W.repo, B, bad, bad, roles, desc)
        got = 'ok'
    except tr.Refused as exc:
        got = str(exc)
    case('STAGING-ROLE-CHAIN/31', 'the snapshot S holds a second root in the class namespace: the bounded namespace '
                                  'check refuses it', got, 'second root' in got)


def config_reviews(root):
    W = ChainWorld(root)
    B, tip = W.chain()
    c, p, s, allf = W.config(tip, None, B)
    got = W.run(c, p)
    case('STAGING-CONFIG-REVIEWS/1', 'the pin table binds the configuration, its one ordinary review and the '
                                     'transition metadata: admitted', got[:3], got[1] is None)
    cfg_b = allf[p]
    dup = sf.jb(review_doc(p, cfg_b, reviewer='reviewer-c', items=['synthetic-retirement-config']))
    c2, p2, s2, _ = W.config(tip, None, B, extra_files={'syn/cfg/review-2.json': dup})
    got = W.run(c2, p2)
    case('STAGING-CONFIG-REVIEWS/2', 'a duplicate ordinary review of the configuration in the pin table: refused',
         got[:3], got[:2] == (65, 'CONFIG_UNREVIEWED'))
    listed = {q: b for q, b in allf.items() if q.startswith('syn/cfg/') and q.endswith('.json') and
              '/' not in q[len('syn/cfg/'):] and not q.endswith('/review.json')}
    got = W.run(c, p, listed=listed)
    case('STAGING-CONFIG-REVIEWS/3', 'the configuration\'s review present beside it but omitted from the pin table: '
                                     'refused (no file is discovered outside the table)', got[:3],
         got[:2] == (65, 'CONFIG_UNREVIEWED'))
    rv_ref = {'kind': 'review', 'path': 'syn/cfg/self.review.json', 'blob_sha256': '0' * 64}
    selfrev = sf.jb({'schema': 'oi-review-record/1', 'reviewer': 'reviewer-c', 'kind': 'widening',
                     'reviewed': {'path': 'syn/cfg/config.json', 'blob_sha256': '0' * 64}, 'replaces': None,
                     'method': 'read', 'verdicts': []})
    rv_ref['blob_sha256'] = sf.sha(selfrev)
    c3, p3, s3, _ = W.config(tip, None, B, extra_files={'syn/cfg/self.review.json': selfrev},
                             records_extra=[rv_ref])
    got = W.run(c3, p3)
    case('STAGING-CONFIG-REVIEWS/4', 'the configuration\'s records reference a widening review of the configuration '
                                     'itself: ERROR CONFIG_INVALID', got[:3], got[:2] == (65, 'CONFIG_INVALID'))
    outside = sf.jb({'schema': 'oi-review-record/1', 'reviewer': 'reviewer-c',
                     'reviewed': {'path': 'syn/cfg/config.json', 'blob_sha256': '0' * 64}, 'method': 'read',
                     'verdicts': []})
    out_ref = {'kind': 'review', 'path': 'syn/elsewhere/self.review.json', 'blob_sha256': sf.sha(outside)}
    c5, p5, s5, _ = W.config(tip, None, B, extra_files={'syn/elsewhere/self.review.json': outside},
                             records_extra=[out_ref])
    got = W.run(c5, p5)
    case('STAGING-CONFIG-REVIEWS/11', 'the configuration\'s records reference a review of the configuration lying '
                                      'outside the pin table: ERROR CONFIG_INVALID', got[:3],
         got[:2] == (65, 'CONFIG_INVALID') and 'review of the configuration itself' in got[2])
    desc_ref = {'kind': 'review', 'path': 'syn/cfg/a1-staging-transition.json',
                'blob_sha256': sf.sha(allf['syn/cfg/a1-staging-transition.json'])}
    c4, p4, s4, _ = W.config(tip, None, B, records_extra=[desc_ref])
    got = W.run(c4, p4)
    case('STAGING-CONFIG-REVIEWS/5', 'the frozen transition descriptor used as a record of the configuration: ERROR '
                                     'CONFIG_INVALID (control metadata admits no record or review)', got[:3],
         got[:2] == (65, 'CONFIG_INVALID'))


def config_widening(root):
    """The configuration's own widening review (staging r2 sec. 3): chosen from the pin table only, unique, naming the
    exact new configuration in `reviewed` and the exact old one in `replaces`."""
    r = sf.Runner(root)
    syn = sf.Syn()
    pd = sf.patch_doc(syn.H, [])
    b1 = {'patch_sha': sf.sha(pd), 'files': {'syn/patch.json': pd}}
    c1, p1, h1, f1 = syn.build(b1)
    sup = {'path': p1, 'blob_sha256': h1}
    d1 = p1.rsplit('/', 1)[0] + '/'
    v2 = dict(b1, version=2, supersedes=sup, config_path='syn/cfg2/config.json',
              extra={'corpus': {'patterns': [r'^doc/[^/]+\.md$', r'^notes/[^/]+\.md$']}},
              files=dict(b1['files'], **{p1: f1[p1], d1 + 'review.json': f1[d1 + 'review.json']}))

    def widen(n=1, replaces=None, reviewer=sf.WIDENER):
        def post(path, cfg_sha):
            out = {}
            for k in range(n):
                wr = {'schema': 'oi-review-record/1', 'kind': 'widening', 'reviewer': reviewer if k == 0 else
                      'widener-e', 'reviewed': {'path': path, 'blob_sha256': cfg_sha},
                      'replaces': replaces if replaces is not None else sup, 'method': 'read the widened corpus',
                      'verdicts': [{'item': 'synthetic-retirement-config:changed corpus', 'verdict': 'accept'}]}
                out[path.rsplit('/', 1)[0] + '/widening-%d.json' % k] = sf.jb(wr)
            return out
        return post

    def run(post):
        c, p, h, _ = syn.build(dict(v2, post=post) if post else v2)
        code, res = r.cli(syn.repo, ['coverage', '--commit', syn.H, '--check', 'zc'], c, p, h)
        st = (res or {}).get('stop') or {}
        return code, st.get('class'), st.get('message', '')
    got = run(widen())
    case('STAGING-CONFIG-REVIEWS/7', 'a widening configuration with one widening review in the pin table naming the '
                                     'exact new and old configurations: admitted', got, got[1] is None)
    got = run(None)
    case('STAGING-CONFIG-REVIEWS/8', 'the widening configuration without a widening review: refused', got,
         got[:2] == (65, 'CONFIG_UNREVIEWED') and 'widening without a widening review' in got[2])
    got = run(widen(n=2))
    case('STAGING-CONFIG-REVIEWS/9', 'two widening reviews of the configuration in the pin table: refused', got,
         got[:2] == (65, 'CONFIG_UNREVIEWED') and 'more than one widening review' in got[2])
    got = run(widen(replaces={'path': 'syn/cfg/elsewhere.json', 'blob_sha256': h1}))
    case('STAGING-CONFIG-REVIEWS/10', 'the widening review names the old configuration\'s bytes at another path: '
                                      'refused', got,
         got[:2] == (65, 'CONFIG_UNREVIEWED') and 'widening without a widening review' in got[2])


# ---- STAGING-FIRST-ALLOW: the widening review of the designated root --------------------------------------------

def first_allow(root):
    from ledger_coverage.engine import records as rec, rules as rulemod
    doc = {'schema': 'oi-term-rules/2', 'record_id': 'a1-staging-w1-w2', 'supersedes': None, 'author': sf.WRITER,
           'rules': [{'id': i, 'kind': 'allow'} for i in ('W1-b', 'W1-c', 'W1-d', 'W2-a', 'W2-b')]}
    b = sf.jb(doc)
    ref = {'path': ALLOW_ROOT, 'blob_sha256': sf.sha(b)}
    changed = rulemod.file_widening(None, doc)
    ordinary = review_doc(ALLOW_ROOT, b)

    def problems(wide, designated=True, old_ref=None, path=ALLOW_ROOT, data=b):
        entries = [(path, data), ('syn/cfg/r.json', sf.jb(ordinary))]
        if wide is not None:
            entries.append(('syn/cfg/w.json', sf.jb(wide)))
        st = rec.Store(entries)
        st.designated_roots = {(ALLOW_ROOT, sf.sha(b))} if designated else set()
        adm = {sf.sha(x) for _, x in entries}
        r = {'path': path, 'blob_sha256': sf.sha(data)}
        return rec.widening_review_problems(r, st, adm, rec.reviewers_of(r, st), sf.WRITER, old_ref, changed)

    def wide(**kw):
        d = {'schema': 'oi-review-record/1', 'kind': 'widening', 'reviewer': sf.WIDENER,
             'reviewed': dict(ref), 'replaces': None, 'method': 'read',
             'verdicts': [{'item': i, 'verdict': 'accept'} for i in changed]}
        d.update(kw)
        for k in [k for k, v in kw.items() if v == '__drop__']:
            d.pop(k)
        return d
    got = problems(wide())
    case('STAGING-FIRST-ALLOW/1', 'the designated root, a distinct widening reviewer, replaces explicitly null, an '
                                  'accept verdict for every initial allow rule: no problem', got, got == [])
    negs = [
        ('2', 'replaces omitted on the designated root', problems(wide(replaces='__drop__'))),
        ('3', 'replaces non-null on the designated root (an invented predecessor)',
         problems(wide(replaces={'path': 'x.json', 'blob_sha256': '0' * 64}))),
        ('4', 'replaces null on a record that is not the designated root', problems(wide(), designated=False)),
        ('5', 'replaces null on an ordinary widening successor', problems(
            wide(), designated=False, old_ref={'path': 'syn/cfg/old.json', 'blob_sha256': '2' * 64})),
        ('6', 'the widening reviewer is the ordinary reviewer', problems(wide(reviewer=sf.REVIEWER))),
        ('7', 'the widening reviewer is the writer', problems(wide(reviewer=sf.WRITER))),
        ('8', 'the reviewed reference names the root\'s bytes at another path',
         problems(wide(reviewed={'path': 'syn/cfg/elsewhere.json', 'blob_sha256': sf.sha(b)}))),
        ('9', 'the reviewed digest differs', problems(wide(reviewed={'path': ALLOW_ROOT, 'blob_sha256': '3' * 64}))),
        ('10', 'one initial allow rule has no verdict',
         problems(wide(verdicts=[{'item': i, 'verdict': 'accept'} for i in changed[1:]]))),
        ('11', 'one verdict is not accept',
         problems(wide(verdicts=[{'item': i, 'verdict': 'reject' if k == 0 else 'accept'}
                                 for k, i in enumerate(changed)]))),
        ('12', 'no widening review', problems(None)),
        ('13', 'a successor whose widening review names the predecessor\'s bytes at a wrong path', problems(
            wide(replaces={'path': 'syn/cfg/wrong.json', 'blob_sha256': '2' * 64}), designated=False,
            old_ref={'path': 'syn/cfg/old.json', 'blob_sha256': '2' * 64})),
    ]
    for n, what, got in negs:
        case('STAGING-FIRST-ALLOW/' + n, what + ': refused', got, bool(got))
    got = problems(wide(replaces='__drop__'), designated=False)
    case('STAGING-FIRST-ALLOW/15', 'a root that is not the designated root, its widening review omitting replaces: '
                                   'refused (R6.RECON.31; no predecessor can be named)', got,
         any('without a predecessor outside the designated root' in x for x in got))
    got = problems(wide(replaces={'path': 'syn/cfg/old.json', 'blob_sha256': '2' * 64}), designated=False,
                   old_ref={'path': 'syn/cfg/old.json', 'blob_sha256': '2' * 64})
    case('STAGING-FIRST-ALLOW/14', 'an ordinary successor\'s widening review naming the exact predecessor: no problem',
         got, got == [])


def first_allow_admission(root):
    """The designated allow root on the ordinary admission path: the configuration's rule file is the designated root
    (transition in play), with its ordinary review and its widening review (replaces: null) as records; the rule-file
    lint refuses a widening review that lists an item twice (record-invalid)."""
    from ledger_coverage.engine import rules as rulemod
    W = ChainWorld(root)
    pats, allow = W.syn.rule_files()
    doc = dict(allow, record_id='a1-staging-w1-w2', supersedes=None)
    ab = sf.jb(doc)
    pb = sf.jb(pats)
    B, tip = W.chain(b_extra={ALLOW_ROOT: ab})
    changed = rulemod.file_widening(None, doc)
    ordinary = sf.jb(review_doc(ALLOW_ROOT, ab))

    def run(dup):
        verdicts = [{'item': i, 'verdict': 'accept'} for i in changed]
        wide = sf.jb({'schema': 'oi-review-record/1', 'kind': 'widening', 'reviewer': sf.WIDENER,
                      'reviewed': {'path': ALLOW_ROOT, 'blob_sha256': sf.sha(ab)}, 'replaces': None,
                      'method': 'read the initial allow rules', 'verdicts': verdicts + (verdicts[:1] if dup else [])})
        files = {'syn/cfg/allow-root.review.json': ordinary, 'syn/cfg/allow-root.widening.json': wide}
        recs = [{'kind': 'review', 'path': q, 'blob_sha256': sf.sha(b)} for q, b in sorted(files.items())]
        c, p, s_, _ = W.config(tip, None, B, extra_files=files, records_extra=recs,
                               variant={'extra': {'rules': [{'path': 'syn/rules-pat.json', 'blob_sha256': sf.sha(pb)},
                                                            {'path': ALLOW_ROOT, 'blob_sha256': sf.sha(ab)}]}})
        got = W.run(c, p)
        res = got[5]
        inv = [d for i in res.get('items', []) if i['class'] == 'record-invalid' and i.get('subject') == ALLOW_ROOT
               for d in (i.get('detail') or [])]
        return got[:3], inv, (res.get('transition') or {}).get('tips', {}).get('allow')
    ok_run, ok_inv, ok_tip = run(False)
    bad_run, bad_inv, _ = run(True)
    case('STAGING-FIRST-ALLOW/16', 'on the ordinary admission path, the designated allow root pinned as a rule file with '
                                   'its ordinary review and a widening review (replaces: null) covering each initial '
                                   'allow rule once: admitted, the root not record-invalid; the same widening review '
                                   'listing an item twice: the root is record-invalid (more than one verdict)',
         {'ok': [ok_run, ok_inv, ok_tip], 'dup': [bad_run, bad_inv]},
         ok_run[1] is None and not ok_inv and ok_tip == {'path': ALLOW_ROOT, 'blob_sha256': sf.sha(ab)} and
         bad_run[1] is None and any('more than one verdict' in d for d in bad_inv))


# ---- K1-GRAPH: acyclic layout and the two cycle countercases -----------------------------------------------------

def k1_layout(root):
    from ledger_coverage.adapters import a1_controls as a1
    jb = sf.jb
    tool = {'tools/ledger_coverage.py': b'entry\n', 'tools/ledger_coverage/x.py': b'x\n'}

    def layout(landed_extra=(), config_self=False):
        nodes = dict(tool)
        cls = jb({'pins': [{'path': q, 'blob_sha256': sf.sha(b)} for q, b in sorted(nodes.items())]})
        nodes['rec/cls-root.json'] = cls
        nodes['rec/cls-root.review.json'] = jb(review_doc('rec/cls-root.json', cls))
        desc = jb({'class_root': {'path': 'rec/cls-root.json', 'blob_sha256': sf.sha(cls)}})
        nodes['plan/transition.json'] = desc
        cfg = {'records': [{'path': 'rec/cls-root.json', 'blob_sha256': sf.sha(cls)}]}
        cfg_b = jb(cfg)
        nodes['plan/config.json'] = cfg_b
        rw = jb(review_doc('plan/config.json', cfg_b, kind='widening', replaces={'path': 'plan/old.json',
                                                                                'blob_sha256': '4' * 64}))
        nodes['plan/config.widen.json'] = rw
        nodes['plan/config.review.json'] = jb(review_doc('plan/config.json', cfg_b))
        req = {'plan/config.json': ['rec/cls-root.json'],
               'plan/PREREG.md': ['plan/config.json', 'plan/config.review.json', 'plan/config.widen.json',
                                  'plan/transition.json'],
               'plan/config.widen.json': ['plan/config.json'], 'plan/config.review.json': ['plan/config.json'],
               'plan/transition.json': ['rec/cls-root.json'], 'rec/cls-root.review.json': ['rec/cls-root.json'],
               'rec/cls-root.json': sorted(tool) + list(landed_extra)}
        if config_self:
            req['plan/config.json'] = req['plan/config.json'] + ['plan/config.widen.json']
        nodes['plan/PREREG.md'] = b'pins\n'
        return a1.reference_graph(nodes, req)[1]
    got = (layout(), layout(config_self=True), layout(landed_extra=['plan/transition.json']),
           layout(landed_extra=['rec/cls-root.review.json']), layout(landed_extra=['plan/config.json']))
    case('STAGING-CONFIG-REVIEWS/6', 'the dependency-ordered layout (custody and tool, then class and allow roots, '
                                     'their reviews and the descriptor, the configuration, its own reviews, the '
                                     'external pin table) has no cycle; the configuration naming its own widening '
                                     'review, and a class pin of the descriptor, its review or the configuration, each '
                                     'give a cycle (K1-GRAPH)', got,
         got[0] is None and all(bool(x) for x in got[1:]))


SUITES = [('representative-snapshot', representative_snapshot), ('item2-engine', item2_engine), ('item2-gate', item2_gate), ('role-chain', role_chain),
          ('config-reviews', config_reviews), ('config-widening', config_widening), ('first-allow', first_allow),
          ('first-allow-admission', first_allow_admission), ('k1-layout', k1_layout)]


def main(out):
    if os.path.exists(out):
        shutil.rmtree(out)
    os.makedirs(out)
    root = tempfile.mkdtemp(prefix='staging-', dir=out)
    repo_root = os.path.dirname(os.path.dirname(os.path.dirname(here)))
    item2_arm(repo_root)
    for name, fn in SUITES:
        try:
            fn(os.path.join(root, name))
        except Exception as exc:  # a suite that cannot run is a failed case of its own
            import traceback
            case(name + '/group-error', 'the suite runs', '%s: %s %s' % (type(exc).__name__, exc,
                                                                          traceback.format_exc()[-1200:]), False)
    with open(os.path.join(out, 'staging-controls.json'), 'w') as f:
        json.dump({'schema': 'oi-local-controls/1', 'suite': 'staging', 'cases': RESULTS}, f, indent=1,
                  sort_keys=True, default=str)
        f.write('\n')
    bad = [c['id'] for c in RESULTS if c['status'] != 'PASS']
    print(json.dumps({'cases': len(RESULTS), 'failed': bad}))
    return 0 if not bad else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else 'staging-controls-out'))
