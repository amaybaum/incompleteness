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
import importlib.util
import io
import json
import os
import shutil
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
CFG = {'config_id': 'a1', 'version': 1, 'path': 'p/c.json', 'commit': 'f' * 40, 'blob_sha256': 'c' * 64}


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


def s11_fixture(fx, mutate=None):
    """S11-2a: the named unmutated run at E and the run at its planted child, as the recorder retains them."""
    subj = '%s:%d' % (PLANTED, LINE)
    before = _result(E, [], False)
    after = _result(X, [GST.item('deny-match', 'FAIL', subject=subj, obligation='TERMS'),
                        GST.item('unclassified', 'REVIEW_REQUIRED', subject=subj, obligation='TERMS')], True)
    argv0 = ['coverage', '--config', 'f' * 40 + ':p/c.json', '--out', '/o/1', '--repo', '.', '--commit', E,
             '--check', 'item2']
    argv1 = ['coverage', '--config', 'f' * 40 + ':p/c.json', '--out', '/o/2', '--repo', '.', '--commit', X,
             '--check', 'item2']
    mutation = [{'path': PLANTED, 'before': 'a' * 40, 'after': 'b' * 40}]
    bindings = {'new_line': subj}
    st = {'before': before, 'after': after, 'argv0': argv0, 'argv1': argv1, 'mutation': mutation,
          'bindings': bindings}
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
    v, rows = gate_rows(root, 's11b-positive', lambda fx: s11b_fixture(fx))
    case('ITEM2-CHECK/22', 'S11-2b run under --check item2: the gate holds', (v, rows),
         v == 'GATE_HOLDS' and rows.get('S11-2b') == [])
    v, rows = gate_rows(root, 's11b-wrong', lambda fx: s11b_fixture(fx, 'item7'))
    case('ITEM2-CHECK/23', 'S11-2b run under another check: the gate refuses it', (v, rows),
         v == 'GATE_FAIL' and 'declarative-mismatch' in rows.get('S11-2b', []))


SUITES = [('item2-engine', item2_engine), ('item2-gate', item2_gate)]


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
