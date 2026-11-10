#!/usr/bin/env python3
"""Research-only non-scientific tests. Never import the checker or run any frozen fixture.

Only inspected pure guard/hash/collection definitions and literals are extracted from the checker.
The controls module's top-level calls only format inert workflow text. Scientific control routines,
full self-tests and the CLI are replaced by forbidden stubs before any test invokes a control.
All host/evidence readers below receive synthetic responses; no network or git process is launched.
"""
import ast
from fractions import Fraction
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import types
import unittest
from unittest.mock import patch
import zipfile

ROOT = Path(__file__).resolve().parent
CHECKER_TEXT = (ROOT / 'qc21_check.py').read_text()
CONTROLS_TEXT = (ROOT / 'controls.py').read_text()


def forbidden(*args, **kwargs):
    raise AssertionError('forbidden scientific/CLI/process entry in non-scientific test')


def control_module():
    spec = importlib.util.spec_from_file_location('qc21_nonscientific_controls', ROOT / 'controls.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    for name in ('main', 'self_test', 'selftest_stab', 'stab_false_check', 'stab_false_control', 'stab_rank',
                 'stab_matrix', 'stab_unit_pair_fires', 'code_t', 'check_mode'):
        setattr(module, name, forbidden)
    module.subprocess = types.SimpleNamespace(run=forbidden, PIPE=None)
    return module


def checker_namespace():
    tree = ast.parse(CHECKER_TEXT)
    names = {'s_mode', 's_refusal', 's_entry', 'h_sha256', 'ordered_unique', 'ordered_key', 'v_unique',
             'canonical', 'jsonable', 'fstr'}
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
