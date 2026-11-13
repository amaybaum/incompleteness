#!/usr/bin/env python3
"""Research-only non-scientific tests. Never import the checker or run any frozen fixture.

Only inspected pure guard/hash/collection definitions and literals are extracted from the checker.
Controls are loaded from inspected definitions and metadata, excluding configuration comprehensions.
Scientific control routines, full self-tests and the CLI are forbidden before any test invokes a control.
All host/evidence readers below receive synthetic responses; no network or git process is launched.
"""
import ast
from fractions import Fraction
import hashlib
import io
import json
from pathlib import Path
import types
import unittest
from unittest.mock import patch
from urllib.parse import parse_qs, urlsplit
import zipfile

ROOT = Path(__file__).resolve().parent
CHECKER_TEXT = (ROOT / 'qc21_check.py').read_text()
CONTROLS_TEXT = (ROOT / 'controls.py').read_text()


def forbidden(*args, **kwargs):
    raise AssertionError('forbidden scientific/CLI/process entry in non-scientific test')


def control_module():
    module = types.ModuleType('qc21_nonscientific_controls')
    nodes = []
    for node in ast.parse(CONTROLS_TEXT).body:
        if isinstance(node, ast.If):
            continue
        if isinstance(node, ast.Assign) and any(isinstance(x, (ast.ListComp, ast.SetComp, ast.DictComp,
                                                               ast.GeneratorExp)) for x in ast.walk(node)):
            # In particular, do not initialize the unused U-prime CFGS table.
            continue
        if isinstance(node, ast.FunctionDef):
            if node.name.startswith('stab_') or node.name in ('_igcd', '_idiv', 'selftest_stab', 'self_test', 'main'):
                continue
            expressions = node.decorator_list + node.args.defaults
            expressions += [x for x in node.args.kw_defaults if x is not None]
            self_contained = all(not any(isinstance(x, (ast.Call, ast.NamedExpr)) for x in ast.walk(e))
                                 for e in expressions)
            assert self_contained, 'uninspected definition-time execution'
        elif isinstance(node, ast.Assign):
            calls = [x for x in ast.walk(node) if isinstance(x, ast.Call)]
            assert all(isinstance(x.func, ast.Name) and x.func.id == 'upload' for x in calls), 'uninspected initializer'
        nodes.append(node)
    exec(compile(ast.Module(body=nodes, type_ignores=[]), '<isolated-control-definitions>', 'exec'), module.__dict__)
    assert 'CFGS' not in module.__dict__
    for name in ('main', 'control_main', 'self_test', 'selftest_stab', 'stab_false_check', 'stab_false_control', 'stab_rank',
                 'stab_matrix', 'stab_unit_pair_fires', 'code_t', 'check_mode'):
        setattr(module, name, forbidden)
    module.subprocess = types.SimpleNamespace(run=forbidden, PIPE=None)
    return module


def checker_namespace():
    tree = ast.parse(CHECKER_TEXT)
    names = {'s_mode', 's_refusal', 's_entry', 'h_sha256', 'ordered_unique', 'ordered_key', 'v_unique',
             'canonical', 'jsonable', 'fstr', 'k_fragment_controls'}
    constants = {'_SHA_K', '_SHA_H0', 'HEX', 'DISPATCH_EVENT', 'ROUND_REF'}
    ns = {'json': json, 'Fraction': Fraction, 'os': types.SimpleNamespace(environ={}),
          'sys': types.SimpleNamespace(argv=['isolated-selftest']), 'REFUSAL_CALLS': 0,
          'self_test': forbidden, 'stress_output': forbidden, 's_decisive': forbidden}
    defs = []
    for node in tree.body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
            if node.targets[0].id in constants:
                ns[node.targets[0].id] = ast.literal_eval(node.value)
        elif isinstance(node, ast.ClassDef) and node.name == 'QC21Refusal':
            defs.append(node)
        elif isinstance(node, ast.FunctionDef) and node.name in names:
            defs.append(node)
    assert {x.name for x in defs if isinstance(x, ast.FunctionDef)} == names
    # No top-level native configuration, rounds, fixtures, solver or verifier body is compiled.
    exec(compile(ast.Module(body=defs, type_ignores=[]), '<isolated-guard-definitions>', 'exec'), ns)
    ns['fixture_measurements'] = lambda sha=None: {
        'mode': 'fixture', 'P': 'placeholder', 'parameters': {'dispatch_sha': sha},
        'flags': {'fixture_mismatches': []}}
    return ns


def fixture_record():
    return {'schema': 'arp2-qc21-measurements', 'version': 1, 'mode': 'fixture', 'complete': False,
            'parameters': {}, 'P': 'placeholder', 'P_controls': 'placeholder', 'REP_INV': 'placeholder',
            'B': {'fragments': [{'name': 'B-P', 'lp': 'placeholder'}, {'name': 'A-of-B', 'lp': 'placeholder'}],
                  'bp_equals_qmp': 'placeholder', 'B1': 'placeholder'}, 'C': 'placeholder',
            'fixtures': {}, 'controls': {}, 'budget': {'respected': 'placeholder'},
            'flags': {x: 'placeholder' for x in ('P', 'B', 'C', 'levels')}}


class NonScientificTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.control = control_module()

    def test_actual_static_scans(self):
        for name in ('static_checker', 'c_exact', 'c_indep'):
            self.assertEqual(getattr(self.control, name)(CHECKER_TEXT), [], name)
        self.assertEqual(self.control.static_controls(CONTROLS_TEXT), [])
        self.assertEqual(self.control.c_iface(CHECKER_TEXT, CONTROLS_TEXT), [])

    def test_synthetic_tokens_and_notes(self):
        self.control.LOG.clear()
        self.control.selftest_decide()
        self.assertGreater(len(self.control.LOG), 30)
        self.assertEqual([name for name, good in self.control.LOG if not good], [])

    def test_synthetic_records_and_resource_rule(self):
        self.control.LOG.clear()
        self.control.selftest_files()
        self.assertEqual([name for name, good in self.control.LOG if not good], [])

    def test_synthetic_host_predicates(self):
        self.control.LOG.clear()
        self.control.selftest_runs()
        self.assertEqual([name for name, good in self.control.LOG if not good], [])

    def test_source_binding_pins_and_first_execution(self):
        m = self.control
        line = '- **`S_max`** = 100000'
        self.assertEqual(m.s_max_errors(line, 100000, 100000), [])
        for text, code, stress in [('', 100000, 100000), (line+'\n'+line, 100000, 100000),
                                   ('- **`S_max`** = 99999', 99999, 99999),
                                   (line, 100001, 100000), (line, 100000, 100001)]:
            self.assertTrue(m.s_max_errors(text, code, stress))
        self.assertTrue(m.pending_unbackticked('- **`S_max`** = PENDING'))
        self.assertFalse(m.pending_unbackticked('Only `PENDING` is quoted.'))
        records = [{'head_sha': 'a'*40, 'head_branch': m.ROUND_BRANCH,
                    'event': 'pull_request', 'created_at': '2026-11-10T02:00:00Z'},
                   {'head_sha': 'b'*40, 'head_branch': m.ROUND_BRANCH,
                    'event': 'push', 'created_at': '2026-11-10T01:00:00Z'}]
        with patch.object(m, 'git_has', return_value=True), patch.object(m, 'git_is_ancestor', return_value=True):
            self.assertEqual(m.run_class_first_execution(records, 'f'*40), '2026-11-10T01:00:00Z')
        with patch.object(m, 'git_has', return_value=False):
            with self.assertRaises(m.CaptureFailed):
                m.run_class_first_execution(records, 'f'*40)
        with patch.object(m, 'git_blob', return_value='0'*40), patch.object(m, 'read_bytes', side_effect=forbidden):
            self.assertFalse(m.v3_working_copy_ok())

    def test_inert_workflow_and_required_removals(self):
        m = self.control
        base = (ROOT.parent / 'verify.yml.input').read_bytes()
        identity = hashlib.sha1(b'blob '+str(len(base)).encode()+b'\0'+base).hexdigest()
        self.assertEqual(identity, '3a9dc8a97fd6f9d6d5f17cf390b5aabf37d65233')
        def read(commit, path):
            self.assertEqual((commit, path), (m.D_SHA, m.WORKFLOW))
            return base
        m.LOG.clear()
        with patch.object(m, 'git_show', side_effect=read):
            m.selftest_w()
        self.assertEqual([name for name, good in m.LOG if not good], [])
        self.assertIn('name: arp2-qc21-fixtures\n', m.SPLICE_FROZEN_JOBS)
        self.assertIn('name: arp2-qc21-stress\n', m.SPLICE_FROZEN_JOBS)
        self.assertIn('name: arp2-qc21-measurements\n', m.SPLICE_FROZEN_JOBS)

    def test_actual_static_mutation_suite_without_files(self):
        m = self.control
        m.LOG.clear()
        def source(path):
            if path == m.CHECKER:
                return CHECKER_TEXT
            if path == m.CONTROLS:
                return CONTROLS_TEXT
            raise AssertionError('unexpected source read')
        with patch.object(m, 'read_text', side_effect=source):
            m.selftest_static()
        self.assertTrue(m.LOG)
        self.assertEqual([name for name, good in m.LOG if not good], [])

    def test_signature_environment_and_alias_mutations(self):
        mutations = [
            CHECKER_TEXT.replace('def s_refusal():', 'def s_refusal(unused=0, /):', 1),
            CHECKER_TEXT.replace('def s_refusal():', 'def s_refusal(*, unused=0):', 1),
            CHECKER_TEXT.replace('status, text = s_entry(sys.argv, os.environ)',
                                 'status, text = s_entry(sys.argv, {})', 1).replace(
                                     'def t_misc():\n', 'def t_misc():\n    s_mode([], os.environ)\n', 1),
            CHECKER_TEXT.replace('def t_misc():\n', 'def t_misc():\n    collection_type = set\n    collection_type()\n', 1),
            CHECKER_TEXT.replace('def t_misc():\n', 'def t_misc():\n    collection_type = frozenset\n    collection_type()\n', 1)]
        for mutated in mutations:
            self.assertNotEqual(mutated, CHECKER_TEXT)
            self.assertTrue(self.control.static_checker(mutated))
        alias = CHECKER_TEXT.replace('def v_unique(values):',
                                    'v_shared = ordered_unique\n\ndef v_unique(values):\n    return v_shared(values)', 1)
        self.assertTrue(self.control.c_indep(alias))
        for suffix in ('\ndef s_bind(_=(v_unique := ordered_unique)):\n    pass\n',
                       '\ndef s_bind(arg: (v_unique := ordered_unique)):\n    pass\n',
                       '\nclass Other((v_unique := ordered_unique)):\n    pass\n'):
            self.assertTrue(self.control.c_indep(CHECKER_TEXT + suffix))
        # Every registered builder must independently retain the first refusal.
        for builder in ('s_build_p', 's_build_b', 's_build_c', 's_build_repinv'):
            index = CHECKER_TEXT.index('def '+builder+'(')
            mutated = CHECKER_TEXT[:index] + CHECKER_TEXT[index:].replace('    s_refusal()\n', '', 1)
            self.assertNotEqual(mutated, CHECKER_TEXT)
            self.assertTrue(self.control.static_checker(mutated))

    def test_guard_modes_without_computation(self):
        ns = checker_namespace()
        env = {'GITHUB_EVENT_NAME': ns['DISPATCH_EVENT'], 'GITHUB_RUN_ATTEMPT': '1', 'GITHUB_REF': ns['ROUND_REF']}
        self.assertEqual(ns['s_mode'](['q', '--event', ns['DISPATCH_EVENT']], env), 'decisive')
        for key in env:
            self.assertEqual(ns['s_mode'](['q', '--event', ns['DISPATCH_EVENT']], dict(env, **{key: 'wrong'})), 'fixture')
        for event in ('fixture', 'push', 'pull_request', 'closed-or-other'):
            code, text = ns['s_entry'](['q', '--event', event], env)
            self.assertEqual(code, 0)
            self.assertEqual(json.loads(text)['mode'], 'fixture')
        self.assertEqual(ns['s_entry'](['q'], env)[0], 4)
        self.assertEqual(ns['s_entry'](['q', '--event', 'fixture', '--dispatch-sha', 'bad'], env)[0], 4)
        self.assertEqual(ns['REFUSAL_CALLS'], 0)
        with self.assertRaises(ns['QC21Refusal']):
            ns['s_refusal']()
        self.assertEqual(ns['REFUSAL_CALLS'], 1)

    def test_standard_hash_and_generic_collections(self):
        ns = checker_namespace()
        for raw in (b'', b'abc', b'abcdbcdecdefdefgefghfghighijhijkijkljklmklmnlmnomnopnopq'):
            self.assertEqual(ns['h_sha256'](raw), hashlib.sha256(raw).hexdigest())
        unique = ns['ordered_unique']
        self.assertEqual(list(unique(['b', 'a', 'b'])), ['b', 'a'])
        self.assertEqual(unique(['a', 'b']), unique(['b', 'a']))
        self.assertEqual(list(unique(['b']) | unique(['a', 'b'])), ['b', 'a'])
        self.assertEqual(ns['ordered_key'](['b', 'a', 'b']), ('a', 'b'))
        self.assertEqual(ns['v_unique']([3, 2, 3]), {3: None, 2: None})

    def test_fixture_marker_rejects_real_or_incomplete_fields(self):
        marker = self.control.run_class_fixture_mode
        self.assertTrue(marker(fixture_record()))
        for field, value in (('complete', True), ('P', {'actual': True}), ('C', None), ('mode', 'decisive')):
            record = fixture_record(); record[field] = value
            self.assertFalse(marker(record))
        record = fixture_record();record['B']['fragments'][0]['lp'] = 'feasible'
        self.assertFalse(marker(record))

    def test_pages_fail_closed_on_duplicates_counts_and_forbidden(self):
        m = self.control
        with patch.object(m, 'gh_get', side_effect=[(True, {'total_count': 2, 'jobs': [{'id': 1}]}),
                                                   (True, {'total_count': 2, 'jobs': [{'id': 2}]})]):
            self.assertEqual(m.run_class_pages('jobs', 'jobs', ('1', '1')), [{'id': 1}, {'id': 2}])
        for responses in ([ (False, 'Forbidden') ],
                          [(True, {'total_count': 2, 'jobs': [{'id': 1}]}), (True, {'total_count': 2, 'jobs': [{'id': 1}]})],
                          [(True, {'total_count': 2, 'jobs': []})],
                          [(True, {'total_count': 2, 'jobs': [{'id': 1}]}), (True, {'total_count': 3, 'jobs': [{'id': 2}]})]):
            with patch.object(m, 'gh_get', side_effect=responses):
                self.assertIsNone(m.run_class_pages('jobs', 'jobs', ('1', '1')))

    def test_calendar_and_saturated_window(self):
        m = self.control
        for text in ('0001-01-01T00:00:00Z', '2000-02-29T23:59:59Z', '2026-11-10T12:00:00Z'):
            self.assertEqual(m.run_class_time_text(m.run_class_time_value(text)), text)
        with self.assertRaises(m.Refused):
            m.run_class_time_value('1900-02-29T00:00:00Z')
        with patch.object(m, 'gh_get', return_value=(True, {'total_count': 1000, 'workflow_runs': []})):
            self.assertIsNone(m.run_class_run_listing('runs-all', '2026-11-10T00:00:00Z', '2026-11-10T00:00:00Z'))
        def response(kind, start, stop, page):
            if start != stop:
                return True, {'total_count': 1000, 'workflow_runs': []}
            ident = 1 if start.endswith('00Z') else 2
            return True, {'total_count': 1, 'workflow_runs': [{'id': ident, 'created_at': start, 'head_sha': 'a'*40}]}
        with patch.object(m, 'gh_get', side_effect=response):
            result = m.run_class_run_listing('runs-all', '2026-11-10T00:00:00Z', '2026-11-10T00:00:01Z')
            self.assertEqual(len(result['runs']), 2)

    def test_b1_structured_conclusions_positive_and_mutations(self):
        import re
        m = self.control
        source = (ROOT.parent / 'verify.yml.input').read_text()
        a42 = "Numerical probes / A42 exclusion (${{ matrix.part }})"
        keep = "ARP-1-MARC keep the measurements"
        report = "KTRANS-SEP-2 axiom reports within the three axioms"
        marker = "KTRANS-SEP-2 marker complete reports with an axiom outside the three"
        parts = ('paths', 'r5', 'n18:0', 'n18:1', 'n18:2', 'dfs:0', 'dfs:1', 'dfs:2',
                 'dfs:3', 'dfs:4', 'dfs:5', 'sathr', 'cubes:0', 'cubes:1', 'cubes:2')
        def make(event):
            names = [x for x in re.findall(r'(?m)^    name: ([^\n]+)$', source) if x != a42]
            names += ([a42] if event == 'pull_request' else
                      [a42.replace("${{ matrix.part }}", x) for x in parts])
            names += [m.JOB_A, m.JOB_B]
            result = []
            for name in names:
                skip = event == 'pull_request' and name in (a42, m.JOB_B)
                steps = [{'name': 'other step', 'conclusion': 'success'}]
                if name == 'Mathlib bridge':
                    steps = [{'name': report, 'conclusion': 'success'},
                             {'name': marker, 'conclusion': 'skipped'}]
                if name == 'Numerical probes / ARP-1-MARC exact span check':
                    steps.append({'name': keep, 'conclusion': 'skipped' if event == 'pull_request' else 'success'})
                if name == m.JOB_A:
                    steps = [{'name': x, 'conclusion': 'success'} for x in (m.STEP_A3, m.STEP_A3B, m.STEP_A7)]
                result.append({'name': name, 'conclusion': 'skipped' if skip else 'success',
                               'steps': None if skip else steps})
            return result
        for event in ('pull_request', 'workflow_dispatch'):
            good = make(event)
            self.assertEqual(m.run_class_expected_conclusions(good, event, source), [])
            for item, new in ((a42 if event == 'pull_request' else a42.replace('${{ matrix.part }}', 'paths'),
                               'success' if event == 'pull_request' else 'skipped'),
                              ('Numerical probes / core A', 'skipped')):
                bad = json.loads(json.dumps(good))
                next(x for x in bad if x['name'] == item)['conclusion'] = new
                self.assertTrue(m.run_class_expected_conclusions(bad, event, source))
            for name, position, outcome in (
                ('Mathlib bridge', 1, 'success'),
                ('Mathlib bridge', 0, 'skipped'),
                ('Numerical probes / ARP-1-MARC exact span check', -1,
                 'success' if event == 'pull_request' else 'skipped')):
                bad = json.loads(json.dumps(good))
                next(x for x in bad if x['name'] == name)['steps'][position]['conclusion'] = outcome
                self.assertTrue(m.run_class_expected_conclusions(bad, event, source))
            self.assertTrue(m.run_class_expected_conclusions(good[:-1], event, source))
            self.assertTrue(m.run_class_expected_conclusions(good, event, source.replace('probes_a42_exclusion:', 'wrong_job:')))
            self.assertTrue(m.run_class_expected_conclusions(good, event, source.replace('n18:2', 'n18:9')))
            # A failed A42 job fails on either event.
            bad = json.loads(json.dumps(good))
            next(x for x in bad if x['name'].startswith('Numerical probes / A42 exclusion'))['conclusion'] = 'failure'
            self.assertTrue(m.run_class_expected_conclusions(bad, event, source))
            # A renamed keyed step is a missing required step.
            for job, step in (('Numerical probes / ARP-1-MARC exact span check', keep),
                              ('Mathlib bridge', report), ('Mathlib bridge', marker)):
                bad = json.loads(json.dumps(good))
                target = next(x for x in bad if x['name'] == job)['steps']
                next(x for x in target if x['name'] == step)['name'] = step + ' (renamed)'
                self.assertTrue(m.run_class_expected_conclusions(bad, event, source), step)
            # A changed keyed guard or id in D's workflow fails.
            for old, new in (("if: ${{ github.event_name == 'workflow_dispatch' }}\n    runs-on",
                              "if: ${{ always() }}\n    runs-on"),
                             ("if: ${{ always() && github.event_name == 'workflow_dispatch' }}",
                              "if: ${{ always() }}"),
                             ("id: ktrans_sep2_axioms", "id: ktrans_sep2_reports"),
                             ("outputs.reports == 'complete-nonstandard'", "outputs.reports != 'complete'")):
                changed = source.replace(old, new, 1)
                self.assertNotEqual(changed, source, old)
                self.assertTrue(m.run_class_expected_conclusions(good, event, changed), old)
        # A missing matrix shard on dispatch fails.
        good = make('workflow_dispatch')
        for part in ('paths', 'n18:1', 'cubes:2'):
            bad = [x for x in good if x['name'] != a42.replace('${{ matrix.part }}', part)]
            self.assertEqual(len(bad), len(good) - 1)
            self.assertTrue(m.run_class_expected_conclusions(bad, 'workflow_dispatch', source), part)

    def test_b3_limits_must_be_present_in_both_independent_checks(self):
        m = self.control
        checker = checker_namespace()['k_fragment_controls']
        good = {'name': 'B-P', 'lp': 'feasible', 'verified': True,
                'budget_values': [3, 3, 3], 'cap_values': [4, 4, 4, 4],
                'pivots': 1, 'max_bits': 2, 'work': 3, 'n_extreme': 1,
                'd': 2, 'c': 3, 'effects_before_reduction': 4}
        for fn in (checker, m.fragment_controls):
            self.assertTrue(fn([good])['C-BUDGET']['green'])
            for field, value in (('budget_values', []), ('budget_values', [1, 2]),
                                 ('cap_values', None), ('cap_values', [1, 2, 3]),
                                 ('budget_values', [True, 3, 3]), ('d', True)):
                bad = dict(good, **{field: value})
                self.assertFalse(fn([bad])['C-BUDGET']['green'], field)
            bad = dict(good)
            del bad['budget_values']
            self.assertFalse(fn([bad])['C-BUDGET']['green'])
            self.assertTrue(fn([dict(good, lp='out_of_scope', budget_values=[])])['C-BUDGET']['green'])

    def test_b4_cursor_link_pagination_and_error_boundary(self):
        m = self.control
        a, b = {'id': 1, 'activity_type': 'push'}, {'id': 2, 'activity_type': 'force_push'}
        success = types.SimpleNamespace(returncode=0, stdout=json.dumps([[a], [b]]), stderr='')
        with patch.object(m.subprocess, 'run', return_value=success) as process:
            self.assertEqual(m.gh_get('activity', 'safe-branch'), (True, [a, b]))
            argv = process.call_args.args[0]
            self.assertIn('--paginate', argv)
            self.assertIn('--slurp', argv)
            query = parse_qs(urlsplit(next(x for x in argv if '?' in x)).query, strict_parsing=True)
            self.assertEqual(query.get('per_page'), ['100'])
            self.assertNotIn('page', query)  # no numbered pagination; gh follows the Link cursor
        for pages in ([], [a], [[a], [a]], [[{'id': None, 'activity_type': 'push'}]],
                      [[a], [{'id': '1', 'activity_type': 'push'}]], [[a, {'id': '01', 'activity_type': 'push'}]],
                      [[{'id': '\u0663', 'activity_type': 'push'}]], [[{'id': True, 'activity_type': 'push'}]]):
            with patch.object(m.subprocess, 'run',
                              return_value=types.SimpleNamespace(returncode=0, stdout=json.dumps(pages), stderr='')):
                self.assertFalse(m.gh_get('activity', 'safe-branch')[0])
        with patch.object(m.subprocess, 'run',
                          return_value=types.SimpleNamespace(returncode=1, stdout='', stderr='Forbidden')):
            self.assertFalse(m.gh_get('activity', 'safe-branch')[0])

    def test_b5_deciding_step_is_valid_not_just_present(self):
        m = self.control
        good = m.synthetic_stress()
        self.assertTrue(m.stress_validate(good)[0])
        for value in (None, 0, 1, 5, True, '4'):
            bad = json.loads(json.dumps(good))
            bad['fragments'][0]['decided_by'] = value
            self.assertFalse(m.stress_validate(bad)[0])
        bad = json.loads(json.dumps(good))
        bad['fragments'][0]['name'] = 'synthetic:C-SYM'
        bad['fragments'][0]['decided_by'] = 2
        self.assertFalse(m.stress_validate(bad)[0])
        bad['fragments'][0]['decided_by'] = 4
        self.assertTrue(m.stress_validate(bad)[0])

    def test_zip_binding_and_member_guard(self):
        m = self.control
        def archive(member='measurements.json'):
            buffer = io.BytesIO()
            with zipfile.ZipFile(buffer, 'w') as output:
                output.writestr(member, json.dumps({'synthetic_test': True}))
            return buffer.getvalue()
        raw = archive()
        art = {'id': 3, 'name': 'arp2-qc21-measurements', 'workflow_run': {'id': 1, 'head_sha': 'a'*40},
               'expired': False, 'expires_at': '2099-01-01T00:00:00Z', 'digest': 'sha256:'+hashlib.sha256(raw).hexdigest()}
        def serve(kind, *args):
            if kind == 'artifacts':
                return True, {'total_count': 1, 'artifacts': [art]}
            if kind == 'artifact-zip':
                return True, raw
            raise AssertionError(kind)
        with patch.object(m, 'gh_get', side_effect=serve):
            good = m.run_class_artifact_binding(1, 'a'*40)
            self.assertTrue(good['valid'])
            self.assertFalse(m.run_class_artifact_binding(1, 'a'*40, {'wrong_record': True})['valid'])
            art['expired'] = True
            self.assertFalse(m.run_class_artifact_binding(1, 'a'*40)['valid'])
            art['expired'] = False;raw = archive('other.json');art['digest'] = 'sha256:'+hashlib.sha256(raw).hexdigest()
            self.assertFalse(m.run_class_artifact_binding(1, 'a'*40)['valid'])
        bad = [CONTROLS_TEXT.replace('zipfile.ZipFile(io.BytesIO(blob))', 'zipfile.ZipFile(io.BytesIO(blob), "w")', 1),
               CONTROLS_TEXT.replace('archive.read("measurements.json")', 'archive.read("other.json")', 1),
               CONTROLS_TEXT.replace('zipfile.ZipFile(io.BytesIO(blob))', 'zipfile.ZipFile("path")', 1),
               CONTROLS_TEXT.replace('members = archive.namelist()', 'alias = archive\n            members = alias.namelist()', 1)]
        for source in bad:
            self.assertNotEqual(source, CONTROLS_TEXT)
            self.assertTrue(m.static_controls(source))


if __name__ == '__main__':
    unittest.main(verbosity=2)
