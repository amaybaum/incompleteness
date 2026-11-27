"""Self-test of the control-expectation gate: the gate's own controls GATE-1 to GATE-30 (design r6, sec. 16.7).

Each control builds a small fixture (an expectation file, a requirement list, runner records, mutation records and
their evidence) in a fresh directory, runs the gate on it in-process, and keeps the gate's exit status and
`gate-result.json` as the control's evidence. The self-test writes `control-records.json` (`oi-control-records/1`,
job `gate-self-test`) with one record per GATE row; the gate then evaluates those rows against the expectation
file like any other. The self-test passes only when every case gives its expected verdict and the gate module
imports only the standard library.

Standard library only; imports nothing from `tools/ledger_coverage/`.
"""
import ast
import copy
import hashlib
import importlib.util
import json
import os
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def _load_gate():
    spec = importlib.util.spec_from_file_location('control_gate_st', os.path.join(HERE, 'control_gate.py'))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


G = _load_gate()

STDLIB = frozenset(['argparse', 'ast', 'copy', 'hashlib', 'importlib', 'importlib.util', 'json', 'os', 're',
                    'shutil', 'subprocess', 'sys', 'tempfile'])


def imports_are_stdlib():
    """The gate's own sources import only the listed standard-library modules (R6.GATE.8)."""
    bad = []
    for name in ('control_gate.py', 'gate_selftest.py'):
        tree = ast.parse(open(os.path.join(HERE, name)).read())
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                bad += [a.name for a in node.names if a.name not in STDLIB]
            elif isinstance(node, ast.ImportFrom):
                bad.append('from %s' % node.module)
    return bad


def sha(b):
    return hashlib.sha256(b).hexdigest()


def dump(p, doc):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    data = doc if isinstance(doc, bytes) else (json.dumps(doc, indent=1, sort_keys=True) + '\n').encode()
    with open(p, 'wb') as f:
        f.write(data)
    return data


def tool_result(outcome, items=(), **extra):
    r = {'schema': 'oi-ledger-coverage/5', 'outcome': outcome, 'preflight': [{'id': 'p', 'passed': True}],
         'record_checks': None, 'items': list(items)}
    if outcome in ('ERROR', 'VOID', 'USAGE', 'INTERNAL'):
        r['stop'] = {'outcome': outcome, 'class': extra.pop('stop_class', 'X')}
    r.update(extra)
    return r


def item(cls, decision, subject='papers/x.md:1', obligation='RET', segment='s', fp=None):
    return {'obligation': obligation, 'class': cls, 'decision': decision, 'subject': subject, 'segment': segment,
            'fingerprint': fp or sha((cls + subject + obligation + str(segment)).encode())[:16]}


OUTSIDE = {'of': 'adversarial', 'scope': 'outside', 'why': 'self-test fixture'}


class Fixture(object):
    """A self-contained gate input: rows, requirements, records, mutation records and evidence."""

    def __init__(self, root):
        self.root = root
        if os.path.exists(root):
            shutil.rmtree(root)
        os.makedirs(root)
        self.rows = []
        self.reqs = []
        self.records = {}
        self.muts = []
        self.release = None
        self.release_fact = None
        self.raw_exp = None

    def req(self, rid, controls, kind='testable', verification=None):
        self.reqs.append({'id': rid, 'kind': kind, 'controls': list(controls),
                          'verification': verification if verification is not None else ['controls']})

    def row(self, rid, expect, req=None, **kw):
        r = {'id': rid, 'requirements': [req or 'R6.ST.%d' % (len(self.reqs) + 1)], 'runner': 'fixture.py:1',
             'operations': [], 'expect': expect, 'source': 'self-test', 'direction': OUTSIDE}
        r.update(kw)
        if r.get('direction') is None:
            r.pop('direction')
        self.rows.append(r)
        if req is None:
            self.req(r['requirements'][0], [rid])
        return r

    def evidence(self, rid, cases=None, procedure=None, files=None, job='job', drop=(), corrupt=()):
        """Writes `evidence/<job>/<rid>/` and its manifest. cases: {name: {exit, result, attested, bindings}}."""
        rel = os.path.join('evidence', job, rid.replace(':', '_'))
        d = os.path.join(self.root, rel)
        man = {'schema': G.SCHEMA_MAN, 'id': rid, 'job': job, 'files': {}, 'cases': []}
        for name, c in sorted((cases or {}).items()):
            tag = name.strip('()') or 'main'
            entry = {'case': name, 'argv': ['ledger_coverage.py', 'fixture'], 'bindings': c.get('bindings', {}),
                     'mutation': []}
            if 'exit' in c:
                entry['exit_file'] = tag + '.exit'
                man['files'][tag + '.exit'] = sha(dump(os.path.join(d, tag + '.exit'), ('%d\n' % c['exit']).encode()))
            if 'result' in c:
                entry['result_file'] = tag + '.result.json'
                man['files'][tag + '.result.json'] = sha(dump(os.path.join(d, tag + '.result.json'), c['result']))
            if 'attested' in c:
                entry['attested'] = tag + '.attested.json'
                man['files'][tag + '.attested.json'] = sha(dump(os.path.join(d, tag + '.attested.json'),
                                                                c['attested']))
            man['cases'].append(entry)
        for name, doc in sorted((files or {}).items()):
            man['files'][name] = sha(dump(os.path.join(d, name), doc))
        if procedure is not None:
            man['procedure'] = procedure
        for name in drop:
            os.remove(os.path.join(d, name))
        for name in corrupt:
            with open(os.path.join(d, name), 'ab') as f:
                f.write(b' ')
        dump(os.path.join(d, 'manifest.json'), man)
        return rel

    def record(self, rid, status, evidence=None, actual=None, job='job'):
        self.records.setdefault(job, []).append({'id': rid, 'status': status, 'actual': actual or {},
                                                 'predicate': 'self-test fixture', 'evidence': evidence})

    def mut(self, rid, status, killed_by, mutant_records, diff=b'--- a\n+++ b\n'):
        rel = self.evidence(rid, files={'mutant-records.json': mutant_records, 'mutation.diff': diff},
                            procedure={'lib': 'mutation', 'mutant_records': 'mutant-records.json',
                                       'diff': 'mutation.diff'}, job='mutation')
        self.muts.append({'id': rid, 'status': status, 'killed_by': killed_by, 'mutated_file': 'engine/x.py',
                          'rule': 'self-test', 'evidence': rel})

    def run(self):
        paths = []
        for job, recs in sorted(self.records.items()):
            p = os.path.join(self.root, 'records-%s.json' % job)
            dump(p, {'schema': G.SCHEMA_REC, 'job': job, 'records': recs})
            paths.append(p)
        mp = None
        if self.muts:
            mp = os.path.join(self.root, 'mutation-records.json')
            dump(mp, {'schema': G.SCHEMA_MUT, 'records': self.muts})
        exp = self.raw_exp if self.raw_exp is not None else {'schema': G.SCHEMA_EXP, 'record_id': 'self-test',
                                                             'rows': self.rows, 'retired': []}
        ctx = getattr(self, 'ctx', None) or G.Ctx()
        if self.release:
            # a fixture repository: one commit holding the files, then the commit under check adding the release
            # fact that names that commit's objects
            repo = os.path.join(self.root, 'repo')
            c1 = git_commit(repo, self.release)
            name, fact = self.release_fact
            c2 = git_commit(repo, {'%s/%s.json' % (G.FACTS_DIR, name): (json.dumps(fact(c1)) + '\n').encode()})
            ctx = G.Ctx(repo, c2)
        return G.run_gate(None, None, paths, mp, ctx, exp_doc=copy.deepcopy(exp),
                          req_doc=copy.deepcopy(self.reqs))


def blob_id(data):
    return hashlib.sha1(b'blob %d\0' % len(data) + data).hexdigest()


def git_commit(repo, files):
    """Writes `files` into the fixture repository's work tree and commits them; returns the commit id."""
    env = dict(os.environ, GIT_AUTHOR_NAME='fixture', GIT_AUTHOR_EMAIL='fixture.invalid',
               GIT_COMMITTER_NAME='fixture', GIT_COMMITTER_EMAIL='fixture.invalid',
               GIT_AUTHOR_DATE='2026-01-01T00:00:00Z', GIT_COMMITTER_DATE='2026-01-01T00:00:00Z')
    if not os.path.isdir(os.path.join(repo, '.git')):
        os.makedirs(repo, exist_ok=True)
        subprocess.run(['git', 'init', '-q', repo], check=True, env=env)
    for p, data in files.items():
        full = os.path.join(repo, p)
        os.makedirs(os.path.dirname(full), exist_ok=True)
        with open(full, 'wb') as f:
            f.write(data)
    subprocess.run(['git', '-C', repo, 'add', '-A'], check=True, env=env)
    subprocess.run(['git', '-C', repo, '-c', 'commit.gpgsign=false', 'commit', '-q', '-m', 'fixture'], check=True,
                   env=env)
    return subprocess.run(['git', '-C', repo, 'rev-parse', 'HEAD'], check=True, env=env,
                          stdout=subprocess.PIPE).stdout.decode().strip()


FAIL_EXP = {'outcome': 'FAIL', 'classes_exact': ['deny-match']}
FAIL_RES = tool_result('FAIL', [item('deny-match', 'FAIL')])


def clean(fx, rid='C1'):
    """One correct declarative row with its record and evidence."""
    fx.row(rid, FAIL_EXP)
    fx.record(rid, 'PASS', fx.evidence(rid, {'': {'exit': 20, 'result': FAIL_RES}}), {'exit': 20, 'outcome': 'FAIL'})


def rtl2_fixture(fx, records, drift=('AGENTS.md',), roles=None):
    roles = roles or {'H': 'h' * 40, 'M': 'm' * 40, 'C': 'c' * 40}
    fx.row('RT-L2', {'outcome': 'PASS'}, predicate_kind='procedural', procedure={'lib': 'rtl2'})
    ev = fx.evidence('RT-L2', {'': {'exit': 0, 'result': tool_result('PASS')}},
                     procedure={'lib': 'rtl2', 'drift': 'drift.json', 'records': 'records.json', 'roles': 'roles.json'},
                     files={'drift.json': list(drift), 'records.json': records, 'roles.json': roles})
    fx.record('RT-L2', 'PASS', ev)
    return roles


def case_1(fx):
    clean(fx)
    fx.records['job'][0]['actual'] = {'exit': 0, 'outcome': 'PASS'}


def case_2(fx):
    clean(fx)
    fx.row('C2', FAIL_EXP)


def case_3(fx):
    clean(fx)
    fx.record('C1', 'PASS', fx.records['job'][0]['evidence'], job='other')


def case_4(fx):
    clean(fx)
    fx.record('C9', 'PASS', fx.records['job'][0]['evidence'])


def case_5(fx):
    clean(fx)
    fx.row('C2', FAIL_EXP)
    fx.record('C2', 'NOT RUN', None, {'reason': 'not run'})


def case_6(fx):
    fx.row('A1r', {'outcome': 'FAIL', 'classes_exact': {'items[file=$rule_file]': ['record-invalid']}})
    res = tool_result('FAIL', [item('deny-match', 'FAIL', subject='papers/x.md:3')])
    ev = fx.evidence('A1r', {'': {'exit': 20, 'result': res, 'bindings': {'rule_file': 'rules/w1.json'}}})
    fx.record('A1r', 'PASS', ev, {'exit': 20, 'outcome': 'FAIL', 'lint_problems': ['W1-d']})


def case_7(fx):
    clean(fx)
    fx.rows[0]['requirements'] = []


def case_8(fx):
    clean(fx)
    fx.req('R6.ST.9', [])


def case_9(fx):
    fx.row('C1', FAIL_EXP)
    fx.record('C1', 'PASS', fx.evidence('C1', {'': {'exit': 20, 'result': FAIL_RES}}, corrupt=('main.result.json',)))


def sweep(fx, two):
    fx.row('SW1', {'outcome': 'ANY'}, predicate_kind='procedural', procedure={'lib': 'sweep'})
    base = tool_result('PASS', [])
    s1 = tool_result('FAIL', [item('missing', 'FAIL', subject='a:1')])
    s2 = tool_result('FAIL', [item('missing', 'FAIL', subject='a:2')] +
                     ([item('duplicated', 'FAIL', subject='a:2')] if two else []))
    ev = fx.evidence('SW1', {'': {'exit': 0, 'result': base}},
                     procedure={'lib': 'sweep', 'base': 'base.json',
                                'sites': [{'site': 'a:1', 'result': 's1.json'}, {'site': 'a:2', 'result': 's2.json'}]},
                     files={'base.json': base, 's1.json': s1, 's2.json': s2})
    fx.record('SW1', 'PASS', ev)


def case_10(fx):
    sweep(fx, True)


def case_11(fx):
    clean(fx)
    fx.row('RT-L2', {'outcome': 'PASS'}, status_allowed=['PASS', 'NOT RUN'],
           not_run={'reason': 'r', 'release_condition': 'c', 'release_check': G.RC_RTL2})
    fx.record('RT-L2', 'NOT RUN', None)
    # the release fact and the objects it names, in the tree of the commit under check (a fixture repository)
    agents = b'reconciled text\n'
    rec = {'schema': 'oi-reconciliation/1', 'record_id': 'r', 'author': 'session.fixture-writer-x', 'ledger_binding': {},
           'paths': [{'path': 'AGENTS.md', 'm': blob_id(agents), 'x': blob_id(agents)}],
           'changes_decisions_on_X': []}
    rb = (json.dumps(rec, indent=1) + '\n').encode()
    rev = {'schema': 'oi-review-record/1', 'reviewer': 'session.fixture-reviewer-y', 'method': 'read',
           'reviewed': {'path': 'plan/rec.json', 'blob_sha256': hashlib.sha256(rb).hexdigest()},
           'verdicts': [{'item': 'AGENTS.md', 'verdict': 'accept'}]}
    fx.release = {'AGENTS.md': agents, 'plan/rec.json': rb,
                  'plan/rec.review.json': (json.dumps(rev, indent=1) + '\n').encode()}
    fx.release_fact = ('RT-L2', lambda c: {'record': {'commit': c, 'path': 'plan/rec.json'},
                                           'review': {'commit': c, 'path': 'plan/rec.review.json'},
                                           'roles': {'H': c, 'M': c, 'C': c}})


def case_12(fx):
    for c in ('S11-2a', 'S11-2b'):
        clean(fx, c)
    fx.row('S11-2c', FAIL_EXP)
    fx.row('S11-2', {'outcome': 'COMPOSITE'}, runner=None, composed_of=['S11-2a', 'S11-2b', 'S11-2c'])


def case_13(fx):
    rtl2_fixture(fx, [{'path': 'AGENTS.md', 'reviewed': False, 'review_lint_passes': False,
                       'H': 'h' * 40, 'M': 'm' * 40, 'C': 'c' * 40}])


def case_14(fx):
    rtl2_fixture(fx, [{'path': 'AGENTS.md', 'reviewed': True, 'review_lint_passes': True,
                       'H': 'h' * 40, 'M': 'n' * 40, 'C': 'c' * 40}])


def case_15(fx):
    rtl2_fixture(fx, [{'path': 'AGENTS.md', 'reviewed': True, 'review_lint_passes': True,
                       'H': 'h' * 40, 'M': 'm' * 40, 'C': 'c' * 40}], drift=('AGENTS.md', '.claude/settings.json'))


def case_16(fx):
    fx.row('RT-T0', {'outcome': 'FAIL', 'counts': {'items[class=hp-unadjudicated]': 1}},
           reference={'region_lines.count': 215})
    res = tool_result('FAIL', [item('hp-unadjudicated', 'FAIL', obligation='HP')], region_lines={'count': 214})
    ev = fx.evidence('RT-T0', {'': {'exit': 20, 'result': res}})
    fx.record('RT-T0', 'PASS', ev)
    fx.rows[0]['expect']['counts']['region_lines.count'] = 214


def case_17(fx):
    clean(fx)
    fx.raw_exp = {'schema': 'oi-control-expectations/0', 'record_id': 'x', 'rows': fx.rows, 'retired': []}


def case_17b(fx):
    clean(fx)
    rows = copy.deepcopy(fx.rows)
    rows[0]['weight'] = 1
    fx.raw_exp = {'schema': G.SCHEMA_EXP, 'record_id': 'x', 'rows': rows, 'retired': []}


def case_17c(fx):
    clean(fx)
    rows = copy.deepcopy(fx.rows)
    rows[0]['status_allowed'] = ['PASS', 'NOT RUN']
    fx.raw_exp = {'schema': G.SCHEMA_EXP, 'record_id': 'x', 'rows': rows, 'retired': []}


def case_18(fx):
    clean(fx)
    sweep(fx, False)
    fx.row('P2', {'outcome': 'TEXT_EQUAL'}, predicate_kind='procedural', procedure={'lib': 'double-run'})
    r = tool_result('PASS')
    fx.record('P2', 'PASS', fx.evidence('P2', {'': {'attested': {'outcome': 'TEXT_EQUAL'}}},
                                        procedure={'lib': 'double-run', 'runs': ['r1.json', 'r2.json']},
                                        files={'r1.json': r, 'r2.json': r}))
    fx.row('N1', {'outcome': 'PASS'}, status_allowed=['PASS', 'NOT RUN'],
           not_run={'reason': 'deferred', 'release_condition': 'an owner decision', 'release_check': G.RC_FALSE})
    fx.record('N1', 'NOT RUN', None)


def case_19(fx):
    rtl2_fixture(fx, [{'path': 'AGENTS.md', 'reviewed': True, 'review_lint_passes': True,
                       'H': 'h' * 40, 'M': 'm' * 40, 'C': 'c' * 40}])


def case_20(fx):
    clean(fx)
    fx.records['job'][0]['status'] = 'FAIL'


def mut_base(fx, rows):
    clean(fx)
    for rid, allowed in rows:
        fx.row(rid, {'outcome': 'KILLED'}, status_allowed=allowed, runner='mutation harness',
               predicate_kind='procedural', direction=None)


def case_21(fx):
    mut_base(fx, [('MUT:s:M1', ['KILLED'])])
    fx.mut('MUT:s:M1', 'SURVIVED', [], {'C1': 'PASS'})


def case_22(fx):
    mut_base(fx, [('MUT:s:M1', ['KILLED']), ('MUT:s:M2', ['KILLED'])])
    fx.mut('MUT:s:M1', 'KILLED', ['C1'], {'C1': 'FAIL'})


def case_23(fx):
    mut_base(fx, [('MUT:s:M1', ['SURVIVED']), ('MUT:s:M2', ['NOT APPLIED']), ('MUT:s:M3', ['KILLED'])])
    fx.mut('MUT:s:M1', 'SURVIVED', [], {'C1': 'PASS'})
    fx.mut('MUT:s:M2', 'NOT APPLIED', [], {'C1': 'PASS'}, diff=b'')
    fx.mut('MUT:s:M3', 'KILLED', ['C1'], {'C1': 'FAIL'})


def case_24(fx):
    mut_base(fx, [('MUT:s:M1', ['KILLED'])])
    fx.mut('MUT:s:M1', 'NOT APPLIED', [], {'C1': 'PASS'}, diff=b'')


def case_25(fx):
    fx.row('REPRO-DOUBLE', {'outcome': 'TEXT_EQUAL'}, predicate_kind='procedural', procedure={'lib': 'double-run'})
    r = json.dumps(tool_result('PASS')).encode()
    fx.record('REPRO-DOUBLE', 'PASS', fx.evidence(
        'REPRO-DOUBLE', {'': {'attested': {'outcome': 'TEXT_EQUAL'}}},
        procedure={'lib': 'double-run', 'runs': ['r1.json', 'r2.json']}, files={'r1.json': r, 'r2.json': r + b' '}))


def case_26(fx):
    clean(fx, 'K-a')
    fx.row('K-b', FAIL_EXP)
    fx.record('K-b', 'FAIL', fx.evidence('K-b', {'': {'exit': 0, 'result': tool_result('PASS')}}))
    fx.row('K', FAIL_EXP, composed_of=['K-a', 'K-b'])
    fx.record('K', 'PASS', fx.evidence('K', {'': {'exit': 20, 'result': FAIL_RES}}))


def case_27a(fx):
    clean(fx)
    fx.rows[0]['direction'] = 'adversarial'


def case_27b(fx):
    clean(fx)
    fx.rows[0]['paired_with'] = ['C-none']


def composite_28(fx, a_fail):
    fx.row('T-a', FAIL_EXP)
    if a_fail:
        fx.record('T-a', 'FAIL', fx.evidence('T-a', {'': {'exit': 0, 'result': tool_result('PASS')}}))
    else:
        fx.record('T-a', 'PASS', fx.evidence('T-a', {'': {'exit': 20, 'result': FAIL_RES}}))
    nr = {'reason': 'deferred', 'release_condition': 'an owner decision', 'release_check': G.RC_FALSE}
    fx.row('T-b', {'outcome': 'PASS'}, status_allowed=['PASS', 'NOT RUN'], not_run=nr)
    fx.record('T-b', 'NOT RUN', None)
    fx.row('T', {'outcome': 'COMPOSITE'}, runner=None, composed_of=['T-a', 'T-b'],
           status_allowed=['PASS', 'NOT RUN'], not_run=nr)


def case_28a(fx):
    composite_28(fx, True)


def case_28b(fx):
    composite_28(fx, False)


def case_29(fx):
    clean(fx)
    fx.row('D1', {'outcome': 'DEFERRED'})
    fx.record('D1', 'PASS', fx.evidence('D1', {'': {'exit': 0, 'result': tool_result('PASS')}}))


def case_30a(fx):
    clean(fx)
    fx.req('R6.ST.8', [], kind='status', verification=[])


def case_30b(fx):
    clean(fx)
    fx.req('R6.ST.8', [], kind='status', verification=['review'])


# GATE id -> [(case name, builders, expected verdict, findings that must be included, exact findings or None)]
TABLE = {
    'GATE-1': [('', [case_1], 'GATE_FAIL', ['declarative-mismatch'], None)],
    'GATE-2': [('', [case_2], 'GATE_FAIL', ['missing-id'], None)],
    'GATE-3': [('', [case_3], 'GATE_FAIL', ['duplicate-id'], None)],
    'GATE-4': [('', [case_4], 'GATE_FAIL', ['unexpected-id'], None)],
    'GATE-5': [('', [case_5], 'GATE_FAIL', ['status-not-allowed'], None)],
    'GATE-6': [('', [case_6], 'GATE_FAIL', ['declarative-mismatch'], None)],
    'GATE-7': [('', [case_7], 'GATE_FAIL', ['correspondence-orphan-row'], None)],
    'GATE-8': [('', [case_8], 'GATE_FAIL', ['correspondence-orphan-requirement'], None)],
    'GATE-9': [('', [case_9], 'GATE_FAIL', ['raw-evidence-missing'], None)],
    'GATE-10': [('', [case_10], 'GATE_FAIL', ['procedural-failed'], None)],
    'GATE-11': [('', [case_11], 'GATE_FAIL', ['status-not-allowed'], None)],
    'GATE-12': [('', [case_12], 'GATE_FAIL', ['missing-id'], None)],
    'GATE-13': [('', [case_13], 'GATE_FAIL', ['procedural-failed'], None)],
    'GATE-14': [('', [case_14], 'GATE_FAIL', ['procedural-failed'], None)],
    'GATE-15': [('', [case_15], 'GATE_FAIL', ['procedural-failed'], None)],
    'GATE-16': [('', [case_16], 'GATE_HOLDS', [], ['reference-difference'])],
    'GATE-17': [('', [case_17, case_17b, case_17c], 'GATE_ERROR', ['file-invalid'], None)],
    'GATE-18': [('', [case_18], 'GATE_HOLDS', [], [])],
    'GATE-19': [('', [case_19], 'GATE_HOLDS', [], [])],
    'GATE-20': [('', [case_20], 'GATE_FAIL', ['status-actual-inconsistent'], None)],
    'GATE-21': [('', [case_21], 'GATE_FAIL', ['status-not-allowed'], None)],
    'GATE-22': [('', [case_22], 'GATE_FAIL', ['missing-id'], None)],
    'GATE-23': [('', [case_23], 'GATE_HOLDS', [], ['limitation-reported'])],
    'GATE-24': [('', [case_24], 'GATE_FAIL', ['status-not-allowed'], None)],
    'GATE-25': [('', [case_25], 'GATE_FAIL', ['procedural-failed'], None)],
    'GATE-26': [('', [case_26], 'GATE_FAIL', ['procedural-failed'], None)],
    'GATE-27': [('(a)', [case_27a], 'GATE_FAIL', ['direction-missing'], None),
                ('(b)', [case_27b], 'GATE_FAIL', ['direction-missing'], None)],
    'GATE-28': [('(a)', [case_28a], 'GATE_FAIL', ['status-not-allowed'], None),
                ('(b)', [case_28b], 'GATE_HOLDS', [], [])],
    'GATE-29': [('', [case_29], 'GATE_FAIL', ['deferred-expectation'], None)],
    'GATE-30': [('(a)', [case_30a], 'GATE_FAIL', ['correspondence-orphan-requirement'], None),
                ('(b)', [case_30b], 'GATE_HOLDS', [], None)],
}

EXTRA = {'GATE-28': {'(a)': ('FAIL',), '(b)': ('NOT RUN',)}}


def _findings(res):
    return sorted({f for e in res.get('rows', []) for f in e.get('findings', [])} | set(res.get('file_findings', [])))


def run(out):
    """Runs every case; writes the fixtures, `control-records.json` and the evidence under `out`.
    Returns (passed, out)."""
    if os.path.exists(out):
        shutil.rmtree(out)
    os.makedirs(out)
    bad_imports = imports_are_stdlib()
    records = []
    all_ok = not bad_imports
    summary = {'imports_outside_stdlib': bad_imports, 'controls': {}}
    for gid in sorted(TABLE, key=lambda g: int(g.split('-')[1])):
        evdir = os.path.join(out, 'evidence', 'gate-self-test', gid)
        man = {'schema': G.SCHEMA_MAN, 'id': gid, 'job': 'gate-self-test', 'files': {}, 'cases': []}
        ok_row = True
        actual = {'cases': {}}
        for name, builders, verdict, include, exact in TABLE[gid]:
            tag = name.strip('()') or 'main'
            results = []
            for i, b in enumerate(builders):
                fx = Fixture(os.path.join(out, 'fixtures', gid, '%s-%d' % (tag, i)))
                b(fx)
                code, res = fx.run()
                results.append((code, res))
            ok = True
            for code, res in results:
                f = _findings(res)
                ok = ok and res.get('verdict') == verdict and code == G.GATE_EXIT[verdict]
                ok = ok and set(include) <= set(f) and (exact is None or set(exact) == set(f))
                if gid in EXTRA:
                    want = EXTRA[gid][name][0]
                    comp = [r.get('composite_status') for r in res.get('rows', []) if 'components' in r]
                    ok = ok and comp == [want]
            code, res = results[0]
            data_exit = ('%d\n' % code).encode()
            data_res = (json.dumps(res, indent=1, sort_keys=True) + '\n').encode()
            dump(os.path.join(evdir, tag + '.exit'), data_exit)
            dump(os.path.join(evdir, tag + '.gate-result.json'), data_res)
            man['files'][tag + '.exit'] = sha(data_exit)
            man['files'][tag + '.gate-result.json'] = sha(data_res)
            for j, (c2, r2) in enumerate(results[1:], 1):
                d = (json.dumps(r2, indent=1, sort_keys=True) + '\n').encode()
                dump(os.path.join(evdir, '%s.variant%d.gate-result.json' % (tag, j)), d)
                man['files']['%s.variant%d.gate-result.json' % (tag, j)] = sha(d)
            man['cases'].append({'case': name, 'argv': ['gate self-test', gid, name], 'bindings': {}, 'mutation': [],
                                 'exit_file': tag + '.exit', 'result_file': tag + '.gate-result.json'})
            actual['cases'][name] = {'exit': code, 'outcome': res.get('verdict'), 'gate_findings': _findings(res),
                                     'variants': [r.get('verdict') for _, r in results[1:]]}
            ok_row = ok_row and ok
        dump(os.path.join(evdir, 'manifest.json'), man)
        records.append({'id': gid, 'status': 'PASS' if ok_row else 'FAIL', 'actual': actual,
                        'predicate': 'each case gives its expected gate verdict and findings',
                        'evidence': os.path.join('evidence', 'gate-self-test', gid)})
        summary['controls'][gid] = 'PASS' if ok_row else 'FAIL'
        all_ok = all_ok and ok_row
    dump(os.path.join(out, 'control-records.json'), {'schema': G.SCHEMA_REC, 'job': 'gate-self-test',
                                                     'records': records})
    dump(os.path.join(out, 'self-test-summary.json'), summary)
    return all_ok, out


if __name__ == '__main__':
    o = sys.argv[1] if len(sys.argv) > 1 else 'gate-self-test-out'
    ok, _ = run(o)
    print(json.dumps({'self_test': 'PASS' if ok else 'FAIL'}))
    sys.exit(0 if ok else 70)
