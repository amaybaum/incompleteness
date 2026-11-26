"""Independent control-expectation gate of the ledger coverage tool (design r6, sec. 16).

The gate decides the verdict on every control of the expectation file (`oi-control-expectations/1`) from
structured data only (AGENTS.md sec. A.44): the runners' `control-records.json` files, the mutation run's
`mutation-records.json`, the evidence manifests and files they name, the expectation file and the requirement
list. It derives each actual value itself and never trusts a runner's `actual` or `status` (R6.GATE.8). It
imports nothing from `tools/ledger_coverage/`: only the standard library (checked by its self-test).

Exit codes: 0 GATE_HOLDS, 20 GATE_FAIL, 65 GATE_ERROR (`file-invalid`), 70 VOID (the gate's self-test failed),
64 USAGE. The gate runs its self-test (GATE-1 to GATE-30, R6.GATE.13) before it evaluates real records, and
writes `gate-result.json` (`oi-control-gate/1`) and, for the self-test, a `control-records.json` with one record
per GATE row and its evidence.

Run with `python3 -I -S -B tools/ledger_coverage/gate/control_gate.py ...`.
"""
import argparse
import ast
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

SCHEMA_EXP = 'oi-control-expectations/1'
SCHEMA_REC = 'oi-control-records/1'
SCHEMA_MUT = 'oi-mutation-records/1'
SCHEMA_MAN = 'oi-control-evidence/1'
SCHEMA_GATE = 'oi-control-gate/1'

GATE_EXIT = {'GATE_HOLDS': 0, 'GATE_FAIL': 20, 'GATE_ERROR': 65}
VOID_EXIT = 70
USAGE_EXIT = 64
TOOL_EXIT = {'PASS': 0, 'REVIEW_REQUIRED': 10, 'FAIL': 20, 'USAGE': 64, 'ERROR': 65, 'VOID': 70, 'INTERNAL': 71}
TOOL_OUTCOMES = frozenset(TOOL_EXIT)
SUBJECT_OUTCOMES = frozenset([
    'NO_ITEM', 'ITEM', 'ANY', 'NON_ACCEPTANCE', 'ACCEPTED', 'PRE_RUN_PASSED', 'PRE_RUN_FAILED', 'LINT_PASS',
    'LINT_FAIL', 'RC_HOLDS', 'RC_FAILS', 'RESULT_EQUAL_CLEAN', 'RESULT_EQUAL_FULL_STORE',
    'RESULT_EQUAL_WITHOUT_AMENDMENT', 'REPLAY_EQUAL', 'LANDING_VERIFIED', 'LANDING_REFUSED', 'RESOLVED',
    'TEXT_EQUAL', 'HASH_EQUAL', 'PREDICATE', 'ORACLE', 'COUNTERCONTROL', 'REFUSED', 'NOT_REFUSED', 'COMPOSITE'])
GATE_OUTCOMES = frozenset(GATE_EXIT)
MUT_OUTCOMES = frozenset(['KILLED', 'SURVIVED', 'NOT_APPLIED'])
OUTCOMES = TOOL_OUTCOMES | SUBJECT_OUTCOMES | GATE_OUTCOMES | MUT_OUTCOMES | frozenset(['DEFERRED'])

ROW_FIELDS = frozenset([
    'id', 'migrated_from', 'requirements', 'runner', 'operations', 'direction', 'paired_with', 'predicate_kind',
    'case', 'expect', 'candidate_expectations', 'restored', 'procedure', 'composed_of', 'depends_on',
    'status_allowed', 'not_run', 'reference', 'source', 'flags'])
EXPECT_FIELDS = frozenset([
    'outcome', 'exit', 'stop_class', 'classes_exact', 'classes_include', 'counts', 'sites', 'invariants',
    'gate_findings_include', 'gate_findings_exact', 'cases'])
CASE_FIELDS = EXPECT_FIELDS - {'cases'} | {'case'}
RECORD_STATUSES = frozenset(['PASS', 'FAIL', 'NOT RUN'])
MUT_STATUSES = frozenset(['KILLED', 'SURVIVED', 'NOT APPLIED'])
ROW_STATUSES = RECORD_STATUSES | MUT_STATUSES
LIBS = frozenset(['rel-equal', 'sweep', 'set', 'replay', 'hash', 'double-run', 'ast', 'rtl2', 'prerun', 'consumer',
                  'lint', 'oracle', 'fixture'])
REQ_KINDS = frozenset(['testable', 'obligation', 'definition', 'governance', 'scope', 'status'])
REQ_ID = re.compile(r'R6\.[A-Z0-9]+\.[0-9]+\Z')
MUT_ID = re.compile(r'MUT:[a-z0-9]+:[A-Za-z0-9-]+\Z')

# The closed invariant vocabulary of DESIGN-r6.md sec. 16.10 (153 keys).
INVARIANT_KEYS = frozenset('''
L_blob X_and_M_views_differ a3_a5_evaluated a5_evaluated a5_unequal_paths acceptable_as_new_run
added_relative_to_unmutated admission_mode admission_mode_not all arm baseline before_host_read
before_unloaded_import blob_at_L byte_identical bytes_read_before_type_check cached_map_equals_ls_tree_in_both_orders
cached_paths_name_the_blob candidate_and_landing_pass checkers_run_from class_meaning_table_equal_in_every_result
class_route_entry_stands classed_items_missing_meaning classed_items_quoting_meaning_min clean_path
clone_checked_out clones commit_paths_classified compare_by component_results_preserved composed_blob
composite_status composition_evaluated condition config_in_landing countercontrol_class_review_landed_cycle
countercontrol_config_landed_cycle directory_admitted distinct_maps_for_distinct_trees drift_state_in
each_listed_line each_with entry_exit entry_point_ran equal_across equal_field equals
error_result_carries_table evaluated_in every_record_verifies evil_ran existing_conformance_controls_unchanged
exit_not_in failed_conditions_include file_executed finding_value findings fixture git_honours_graft
git_status_porcelain_empty harness_dir_files has have hit_at_offset_in_image hit_profiles_include holds
host_calls imported_files_within in_memory_commits_own_map index_unchanged inputs_equal
items_equal_run_without_file items_include killed_by killed_by_nonempty landing_record_lists lint_problems
linted_paths_include mappings_unchanged marker_written message_names module_init_ran mutated_literal
mutated_literal_rule mutation_attempts_refused names_commit names_edit negative_example_matches_widened_rule
new_reader_refused_with no_error no_exception no_group_error no_result_with_outcome no_result_written no_stop
none not_class not_in_H_to_M_scan nothing_cached_by_a_refusal objects_fetched
old_style_X_vs_M_comparison_reports others_class out_dir_created payload_ran per_failed_check per_operation
per_site rc11_evaluated reader_cases_refused_with reason record_admitted record_checks_failed_include
record_directory_entries_equal record_directory_state reference_graph_cycle refs_unchanged refused
replay_equality representative_candidate resid_key restored_of_each_component result_equal_without_file
results_validated_min retired_lines_count rt_l2_status rule_active same_reader_path_map_unchanged
same_reader_serves_verified_bytes same_view_returned scanned_paths_within schema_errors selected_offset
self_test_imports_all_accepted side_change_obligation side_changes_classified_by side_changes_exact
sites_resolved_by_it snapshot_T_recorded snapshot_fields_all_present source_map_nonempty stderr_json_outcome
stop_class_in superseding_record_used supplied_file_read_as_evidence terms_and_execution_equal_clean
tool_and_workflow_blobs_equal_pins tool_run_exit value value_occurs_in value_set_includes walk_terminates
writes_only_under
'''.split())

# The evidence a procedure library requires (R6.GATE.7, R6.GATE.8): named inputs of the manifest's procedure.
LIB_INPUTS = {
    'rel-equal': ('runs',),
    'sweep': ('base', 'sites'),
    'set': ('listing', 'actual_set'),
    'replay': ('runs',),
    'hash': ('runs',),
    'double-run': ('runs',),
    'ast': ('inputs', 'attested'),
    'rtl2': ('drift', 'records', 'roles'),
    'prerun': ('step_exit', 'marker_listing', 'sentinel', 'import_trace'),
    'consumer': ('results', 'landing_record', 'snapshot', 'attested'),
    'lint': ('findings', 'source_map'),
    'oracle': ('tool_output', 'oracle_output'),
    'fixture': ('ls_remote_fixture', 'landing_check_exit'),
}

FINDING_FAIL = frozenset([
    'missing-id', 'unexpected-id', 'duplicate-id', 'status-not-allowed', 'declarative-mismatch', 'procedural-failed',
    'raw-evidence-missing', 'status-actual-inconsistent', 'correspondence-orphan-row',
    'correspondence-orphan-requirement', 'expect-null', 'direction-missing', 'deferred-expectation'])
FINDING_INFO = frozenset(['reference-difference', 'limitation-reported'])


COMPOUND = []


class FileInvalid(Exception):
    """An invalid expectation, record, mutation-record or manifest file: the gate's ERROR (65)."""


def sha256_file(path):
    with open(path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def load_json(path, what):
    try:
        with open(path, 'rb') as f:
            return json.loads(f.read().decode('utf-8'))
    except (OSError, ValueError, UnicodeDecodeError) as exc:
        raise FileInvalid('%s unreadable: %s: %r' % (what, path, exc))


# ---------------------------------------------------------------------------------------------------------------
# Release checks (R6.GATE.15). Each release check of the expectation file is a predicate stated in prose; the gate
# evaluates it by the evaluator keyed to its exact text. An unknown text makes the file invalid.

RC_FALSE = 'false until an owner-approved expectation change replaces this entry'
RC_TR5_PASS = 'TR5 status PASS'
RC_EI14 = ('a host run record of the pinned workflow with event workflow_dispatch on a ref other than refs/heads/main, '
           'whose head holds T\', is retained in the evidence referenced at the commit under check')
RC_RTL2 = ('a reconciliation record named by the run from a commit outside the tool\'s landing paths, whose review '
           'record passes record lint and whose H, M and C blob ids equal the predicted run roles')
RC_RTT = 'a reviewed record of a sec. 8.2 kind referenced by the configuration at the commit under check'
RC_TR5 = ('the configuration path at the candidate F named by --freeze is listed in the last Record pins subsection of '
          'the PREREG.md beside it')
RELEASE_CHECKS = frozenset([RC_FALSE, RC_TR5_PASS, RC_EI14, RC_RTL2, RC_RTT, RC_TR5])


# Release facts are read from git objects at the commit under check (--commit), never from a local directory: the
# file `<facts_dir>/<row id>.json` in that commit's tree names the objects the fact rests on, and each evaluator
# checks those objects itself. An absent file is a fact not established (the check is false).
FACTS_DIR = 'verification/audits/foundations/ledger-coverage-tool-20261123/release'
AUDIT_DIR = 'verification/audits/foundations/ledger-coverage-tool-20261123/'
WORKFLOW_PATH = '.github/workflows/ledger-coverage.yml'
T_PRIME = '14ac71b4b0a0c0aa2d7068d6799a73f474097060'
HEX40 = re.compile('[0-9a-f]{40}\\Z')
# the record kinds of the reviewed records RT-T needs (the source design's sec. 8.2)
SEC82_KINDS = frozenset(['hp', 'context-adjudication', 'hit-classification'])


def _release_fact(ctx, name):
    """The release fact `<facts_dir>/<name>.json` in the tree of the commit under check, or None."""
    if not (ctx.repo and ctx.commit):
        return None
    data = git_show(ctx.repo, '%s:%s/%s.json' % (ctx.commit, ctx.facts_dir, name))
    if data is None:
        return None
    try:
        doc = json.loads(data.decode('utf-8'))
    except ValueError as exc:
        raise FileInvalid('release fact %s at %s: %s' % (name, ctx.commit, exc))
    if not isinstance(doc, dict):
        raise FileInvalid('release fact %s at %s is not an object' % (name, ctx.commit))
    return doc


def git_blob_id(repo, rev_path):
    r = subprocess.run(['git', '--no-replace-objects', '-C', repo, 'rev-parse', '--verify', '--quiet',
                        rev_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return r.stdout.decode().strip() if r.returncode == 0 else None


def git_is_ancestor(repo, a, b):
    r = subprocess.run(['git', '--no-replace-objects', '-C', repo, 'merge-base', '--is-ancestor', a, b],
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return r.returncode == 0


def _json_blob(repo, ref):
    if not (isinstance(ref, dict) and isinstance(ref.get('commit'), str) and HEX40.match(ref['commit'])
            and isinstance(ref.get('path'), str)):
        return None, None
    data = git_show(repo, '%s:%s' % (ref['commit'], ref['path']))
    if data is None:
        return None, None
    try:
        return data, json.loads(data.decode('utf-8'))
    except ValueError:
        return data, None


def ei14_release(ctx):
    """A host run record of the pinned workflow, event workflow_dispatch, on a ref other than refs/heads/main,
    whose head holds T' (T' is the head or its ancestor), retained at the commit under check."""
    f = _release_fact(ctx, 'EI14-dispatch')
    if not f:
        return False
    head = f.get('head_sha')
    return bool(f.get('event') == 'workflow_dispatch' and isinstance(f.get('ref'), str) and f['ref']
                and f['ref'] != 'refs/heads/main' and f.get('workflow_path') == WORKFLOW_PATH
                and isinstance(head, str) and HEX40.match(head) and git_is_ancestor(ctx.repo, T_PRIME, head))


def rtl2_release(ctx, name='RT-L2'):
    """A reconciliation record named by the run from a commit outside the tool's landing paths, whose review record
    passes the gate's structural lint (schema, reviewed path and sha256, a reviewer other than the author, every
    verdict accept) and whose per-path blob ids at H, M and C equal those of the predicted run roles."""
    f = _release_fact(ctx, name)
    if not f:
        return False
    roles = f.get('roles') or {}
    if not all(isinstance(roles.get(k), str) and HEX40.match(roles[k]) for k in ('H', 'M', 'C')):
        return False
    ref = f.get('record') or {}
    path = ref.get('path') if isinstance(ref, dict) else None
    if not isinstance(path, str) or path.startswith(('tools/', AUDIT_DIR)) or path == WORKFLOW_PATH:
        return False
    rb, rec = _json_blob(ctx.repo, ref)
    _, rev = _json_blob(ctx.repo, f.get('review'))
    if not (isinstance(rec, dict) and rec.get('schema') == 'oi-reconciliation/1' and isinstance(rev, dict)):
        return False
    reviewed = rev.get('reviewed') or {}
    verdicts = rev.get('verdicts') or []
    if not (rev.get('schema') == 'oi-review-record/1' and reviewed.get('path') == path
            and reviewed.get('blob_sha256') == hashlib.sha256(rb).hexdigest()
            and isinstance(rev.get('reviewer'), str) and rev['reviewer'] and rev['reviewer'] != rec.get('author')
            and verdicts and all(isinstance(v, dict) and v.get('verdict') == 'accept' for v in verdicts)):
        return False
    entries = rec.get('paths') or []
    if not entries:
        return False
    for e in entries:
        if not isinstance(e, dict) or not isinstance(e.get('path'), str):
            return False
        for field, role in (('h', 'H'), ('m', 'M'), ('x', 'C')):
            if field == 'h' and field not in e:
                continue
            if git_blob_id(ctx.repo, '%s:%s' % (roles[role], e['path'])) != e.get(field):
                return False
    return True


def rtt_release(ctx):
    """A reviewed record of a sec. 8.2 kind referenced by the configuration (--config) at the commit under check:
    the configuration's `records` list it with its blob sha256, and a review record listed beside it reviews
    exactly that blob."""
    if not (ctx.repo and ctx.commit and ctx.config_path):
        return False
    data = git_show(ctx.repo, '%s:%s' % (ctx.commit, ctx.config_path))
    try:
        cfg = json.loads(data.decode('utf-8')) if data is not None else None
    except ValueError:
        cfg = None
    refs = [r for r in ((cfg or {}).get('records') or []) if isinstance(r, dict)] if isinstance(cfg, dict) else []
    reviews = []
    for r in refs:
        if r.get('kind') == 'review':
            _, rv = _json_blob(ctx.repo, {'commit': ctx.commit, 'path': r.get('path')})
            if isinstance(rv, dict) and rv.get('schema') == 'oi-review-record/1':
                reviews.append(rv)
    for r in refs:
        if r.get('kind') in SEC82_KINDS:
            b = git_show(ctx.repo, '%s:%s' % (ctx.commit, r.get('path')))
            if b is None or hashlib.sha256(b).hexdigest() != r.get('blob_sha256'):
                continue
            for rv in reviews:
                rd = rv.get('reviewed') or {}
                vs = rv.get('verdicts') or []
                if rd.get('path') == r.get('path') and rd.get('blob_sha256') == r.get('blob_sha256') and vs and \
                        all(isinstance(v, dict) and v.get('verdict') == 'accept' for v in vs):
                    return True
    return False


def git_show(repo, rev_path):
    r = subprocess.run(['git', '--no-replace-objects', '-C', repo, 'cat-file', 'blob', rev_path],
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return r.stdout if r.returncode == 0 else None


def tr5_release(ctx):
    """True iff the configuration path at the candidate F (--freeze) is listed in the last `Record pins`
    subsection of the PREREG.md in the configuration's directory at F. Evaluated from git objects."""
    if not (ctx.repo and ctx.freeze and ctx.config_path):
        return False
    if not re.fullmatch('[0-9a-f]{40}', ctx.freeze):
        return False
    d = ctx.config_path.rsplit('/', 1)[0] if '/' in ctx.config_path else ''
    prereg = git_show(ctx.repo, '%s:%s' % (ctx.freeze, (d + '/' if d else '') + 'PREREG.md'))
    if prereg is None or git_show(ctx.repo, '%s:%s' % (ctx.freeze, ctx.config_path)) is None:
        return False
    text = prereg.decode('utf-8', 'replace').splitlines()
    starts = [i for i, ln in enumerate(text) if re.match(r'#+\s+Record pins\s*$', ln)]
    if not starts:
        return False
    i = starts[-1]
    level = len(text[i]) - len(text[i].lstrip('#'))
    body = []
    for ln in text[i + 1:]:
        m = re.match(r'(#+)\s', ln)
        if m and len(m.group(1)) <= level:
            break
        body.append(ln)
    name = ctx.config_path.rsplit('/', 1)[-1]
    return any(('`%s`' % ctx.config_path) in ln or ('`%s`' % name) in ln for ln in body)


def evaluate_release(ctx, text, statuses):
    if text == RC_FALSE:
        return False
    if text == RC_TR5_PASS:
        return statuses.get('TR5') == 'PASS'
    if text == RC_EI14:
        return ei14_release(ctx)
    if text == RC_RTL2:
        return rtl2_release(ctx)
    if text == RC_RTT:
        return rtt_release(ctx)
    if text == RC_TR5:
        return tr5_release(ctx)
    raise FileInvalid('unknown release check %r' % text)


# ---------------------------------------------------------------------------------------------------------------
# Expectation file and requirement list

def _check_expect(e, where, allow_cases=True):
    if not isinstance(e, dict):
        raise FileInvalid('%s: expect is not an object' % where)
    unknown = set(e) - (EXPECT_FIELDS if allow_cases else CASE_FIELDS)
    if unknown:
        raise FileInvalid('%s: unknown expect fields %s' % (where, sorted(unknown)))
    if 'outcome' in e and e['outcome'] not in OUTCOMES:
        raise FileInvalid('%s: unknown outcome %r' % (where, e['outcome']))
    if 'exit' in e and not isinstance(e['exit'], int):
        raise FileInvalid('%s: exit is not an integer' % where)
    for inv in e.get('invariants', []):
        # R6.GATE.3 (amendment 1, B5): an object may hold several keys when every key is in the vocabulary and
        # their combined meaning is unambiguous; it counts as one condition, and the gate lists it in its result.
        if not (isinstance(inv, dict) and inv):
            raise FileInvalid('%s: an invariant is not an object' % where)
        for k in inv:
            if k not in INVARIANT_KEYS:
                raise FileInvalid('%s: invariant key %r outside the vocabulary' % (where, k))
        if len(inv) > 1:
            COMPOUND.append(where)
    for k in ('gate_findings_include', 'gate_findings_exact'):
        if k in e:
            if not isinstance(e[k], list) or any(f not in FINDING_FAIL | FINDING_INFO | {'file-invalid'} for f in e[k]):
                raise FileInvalid('%s: %s names an unknown finding' % (where, k))
    if 'counts' in e and not isinstance(e['counts'], dict):
        raise FileInvalid('%s: counts is not an object' % where)
    if 'cases' in e:
        if not allow_cases or not isinstance(e['cases'], list) or not e['cases']:
            raise FileInvalid('%s: malformed cases' % where)
        for c in e['cases']:
            if not isinstance(c, dict) or 'case' not in c:
                raise FileInvalid('%s: a case has no name' % where)
            _check_expect(c, where + ' case %r' % (c['case'],), allow_cases=False)


def load_expectations(path=None, doc=None):
    del COMPOUND[:]
    e = doc if doc is not None else load_json(path, 'expectation file')
    if not isinstance(e, dict) or set(e) != {'schema', 'record_id', 'rows', 'retired'}:
        raise FileInvalid('expectation file: top-level fields must be schema, record_id, rows, retired')
    if e['schema'] != SCHEMA_EXP:
        raise FileInvalid('expectation file: schema %r' % e['schema'])
    if not isinstance(e['rows'], list) or not isinstance(e['retired'], list):
        raise FileInvalid('expectation file: rows and retired must be arrays')
    rows = {}
    for r in e['rows']:
        if not isinstance(r, dict) or not isinstance(r.get('id'), str):
            raise FileInvalid('a row has no id')
        rid = r['id']
        unknown = set(r) - ROW_FIELDS
        if unknown:
            raise FileInvalid('row %s: unknown fields %s' % (rid, sorted(unknown)))
        for req in ('requirements', 'runner', 'operations', 'expect'):
            if req not in r:
                raise FileInvalid('row %s: field %s missing' % (rid, req))
        if rid in rows:
            raise FileInvalid('row id %s repeated' % rid)
        if rid.startswith('MUT:') and not MUT_ID.match(rid):
            raise FileInvalid('row %s: malformed mutant id' % rid)
        if not isinstance(r['requirements'], list) or not all(isinstance(x, str) for x in r['requirements']):
            raise FileInvalid('row %s: requirements is not a list of ids' % rid)
        if r['runner'] is not None and not isinstance(r['runner'], str):
            raise FileInvalid('row %s: runner' % rid)
        if not isinstance(r['operations'], list):
            raise FileInvalid('row %s: operations' % rid)
        d = r.get('direction', 'adversarial')
        dof = d.get('of') if isinstance(d, dict) else d
        if dof not in ('positive', 'adversarial', 'both'):
            raise FileInvalid('row %s: direction' % rid)
        if isinstance(d, dict) and not (set(d) - {'of', 'why'}) <= {'exempt', 'required', 'scope'}:
            raise FileInvalid('row %s: direction fields' % rid)
        if r.get('predicate_kind', 'declarative') not in ('declarative', 'procedural'):
            raise FileInvalid('row %s: predicate_kind' % rid)
        allowed = r.get('status_allowed', ['PASS'])
        if not isinstance(allowed, list) or not allowed or any(s not in ROW_STATUSES for s in allowed):
            raise FileInvalid('row %s: status_allowed' % rid)
        nr = r.get('not_run')
        if 'NOT RUN' in allowed:
            if not (isinstance(nr, dict) and set(nr) == {'reason', 'release_condition', 'release_check'}
                    and all(isinstance(nr[k], str) and nr[k].strip() for k in nr)):
                raise FileInvalid('row %s: NOT RUN allowed without reason, release condition and release check' % rid)
            if nr['release_check'] not in RELEASE_CHECKS:
                raise FileInvalid('row %s: release check with no evaluator: %r' % (rid, nr['release_check']))
        elif nr is not None:
            raise FileInvalid('row %s: not_run without NOT RUN allowed' % rid)
        proc = r.get('procedure')
        if proc is not None:
            if not isinstance(proc, dict) or proc.get('lib') not in LIBS:
                raise FileInvalid('row %s: procedure lib' % rid)
        for k in ('composed_of', 'depends_on', 'paired_with'):
            if k in r and (not isinstance(r[k], list) or not all(isinstance(x, str) for x in r[k])):
                raise FileInvalid('row %s: %s' % (rid, k))
        if r['expect'] is not None:
            _check_expect(r['expect'], 'row %s' % rid)
        if r.get('restored') is not None:
            _check_expect(r['restored'], 'row %s restored' % rid)
        rows[rid] = r
    retired = {}
    for x in e['retired']:
        if not (isinstance(x, dict) and set(x) == {'old_id', 'disposition', 'underlying'}):
            raise FileInvalid('a retired entry is malformed')
        u = x['underlying']
        if not (isinstance(u, str) and (u.startswith('preserved-at ') or u.startswith('obsolete: ')
                                        or u == 'withdrawal-needs-decision')):
            raise FileInvalid('retired %s: underlying %r' % (x['old_id'], u))
        if x['old_id'] in rows:
            raise FileInvalid('retired id %s is a row id' % x['old_id'])
        retired[x['old_id']] = x
    for rid, r in rows.items():
        for k in ('composed_of', 'depends_on'):
            for c in r.get(k, []):
                if c not in rows:
                    raise FileInvalid('row %s: %s names %s, not a row' % (rid, k, c))
    return e, rows, retired


def load_requirements(path=None, doc=None):
    q = doc if doc is not None else load_json(path, 'requirement list')
    if not isinstance(q, list):
        raise FileInvalid('requirement list is not an array')
    out = {}
    for x in q:
        if not (isinstance(x, dict) and {'id', 'kind', 'controls', 'verification'} <= set(x)):
            raise FileInvalid('requirement entry malformed')
        if not REQ_ID.match(x['id']) and not re.fullmatch(r'OBL-[0-9]+', x['id']):
            raise FileInvalid('requirement id %r' % x['id'])
        if x['kind'] not in REQ_KINDS or not isinstance(x['controls'], list) or not isinstance(x['verification'], list):
            raise FileInvalid('requirement %s malformed' % x['id'])
        if x['id'] in out:
            raise FileInvalid('requirement %s repeated' % x['id'])
        out[x['id']] = x
    return out


def correspondence(rows, retired, reqs):
    """R6.GATE.12, both directions. Returns [(subject, finding, detail)]."""
    out = []
    named = set()
    for q in reqs.values():
        if q['controls']:
            for c in q['controls']:
                named.add(c)
                if c in retired:
                    out.append((q['id'], 'correspondence-orphan-requirement', 'names retired id %s as a live control' % c))
                elif c not in rows:
                    out.append((q['id'], 'correspondence-orphan-requirement', 'names %s, which is not a row' % c))
        elif q['kind'] == 'testable':
            out.append((q['id'], 'correspondence-orphan-requirement', 'a testable requirement names no control'))
        elif not [v for v in q['verification'] if v == 'review' or re.fullmatch(r'OBL-[0-9]+', v)]:
            out.append((q['id'], 'correspondence-orphan-requirement',
                        'a %s requirement names neither a control nor its verification' % q['kind']))
    for rid, r in rows.items():
        if not r['requirements']:
            out.append((rid, 'correspondence-orphan-row', 'no requirement'))
        for x in r['requirements']:
            if x not in reqs:
                out.append((rid, 'correspondence-orphan-row', 'names %s, absent from the requirement list' % x))
        if rid not in named:
            out.append((rid, 'correspondence-orphan-row', 'named by no requirement'))
    return out


def direction_findings(rows):
    """R6.GATE.9 `direction-missing`: a row in the both-directions scope with no second direction recorded, or a
    paired_with naming an id that is not a row. Mutant rows and the gate's own controls are outside by namespace;
    a row outside the scope records `scope`."""
    out = []
    for rid, r in rows.items():
        for p in r.get('paired_with', []):
            if p not in rows:
                out.append((rid, 'direction-missing', 'paired_with names %s, not a row' % p))
        if rid.startswith('MUT:') or rid.startswith('GATE-'):
            continue
        d = r.get('direction', 'adversarial')
        dof = d.get('of') if isinstance(d, dict) else d
        if isinstance(d, dict) and ('scope' in d or d.get('exempt') == 'observation'):
            continue
        if dof == 'both' or r.get('restored') is not None or r.get('paired_with'):
            continue
        out.append((rid, 'direction-missing', 'no second direction recorded'))
    return out


# ---------------------------------------------------------------------------------------------------------------
# Records, mutation records and manifests

def load_records(paths):
    """Returns ({id: (job, record)}, findings). Duplicate ids within or across jobs are findings."""
    seen = {}
    findings = []
    for p in paths:
        d = load_json(p, 'record file')
        if not (isinstance(d, dict) and set(d) == {'schema', 'job', 'records'} and d['schema'] == SCHEMA_REC
                and isinstance(d['job'], str) and isinstance(d['records'], list)):
            raise FileInvalid('record file %s: not %s' % (p, SCHEMA_REC))
        for rec in d['records']:
            if not (isinstance(rec, dict) and set(rec) == {'id', 'status', 'actual', 'predicate', 'evidence'}):
                raise FileInvalid('record file %s: a record has fields other than id, status, actual, predicate, '
                                  'evidence' % p)
            if rec['status'] not in RECORD_STATUSES:
                raise FileInvalid('record file %s: status %r of %s' % (p, rec['status'], rec['id']))
            if rec['id'] in seen:
                findings.append((rec['id'], 'duplicate-id', 'recorded by job %s and job %s' % (seen[rec['id']][0], d['job'])))
                continue
            seen[rec['id']] = (d['job'], rec, os.path.dirname(os.path.abspath(p)))
    return seen, findings


def load_mutation_records(path):
    if path is None:
        return {}, []
    d = load_json(path, 'mutation record file')
    if not (isinstance(d, dict) and set(d) == {'schema', 'records'} and d['schema'] == SCHEMA_MUT
            and isinstance(d['records'], list)):
        raise FileInvalid('mutation record file: not %s' % SCHEMA_MUT)
    out, findings = {}, []
    for m in d['records']:
        if not (isinstance(m, dict) and set(m) == {'id', 'status', 'killed_by', 'mutated_file', 'rule', 'evidence'}):
            raise FileInvalid('mutation record malformed')
        if m['status'] not in MUT_STATUSES or not isinstance(m['killed_by'], list):
            raise FileInvalid('mutation record %s malformed' % m.get('id'))
        if m['id'] in out:
            findings.append((m['id'], 'duplicate-id', 'two mutation records'))
            continue
        out[m['id']] = (m, os.path.dirname(os.path.abspath(path)))
    return out, findings


class Evidence(object):
    """A verified evidence directory: the manifest and the sha256-checked files it names."""

    def __init__(self, base, rel, rid):
        self.problems = []
        self.dir = os.path.normpath(os.path.join(base, rel)) if isinstance(rel, str) else None
        self.man = None
        if self.dir is None or not os.path.isfile(os.path.join(self.dir, 'manifest.json')):
            self.problems.append('manifest absent')
            return
        man = load_json(os.path.join(self.dir, 'manifest.json'), 'manifest')
        if not (isinstance(man, dict) and man.get('schema') == SCHEMA_MAN and isinstance(man.get('files'), dict)
                and isinstance(man.get('cases', []), list)):
            raise FileInvalid('manifest of %s: not %s' % (rid, SCHEMA_MAN))
        if man.get('id') != rid:
            self.problems.append('manifest id %r is not %r' % (man.get('id'), rid))
        for f, h in sorted(man['files'].items()):
            p = os.path.normpath(os.path.join(self.dir, f))
            if not p.startswith(self.dir + os.sep) or not os.path.isfile(p):
                self.problems.append('file %s absent' % f)
            elif sha256_file(p) != h:
                self.problems.append('file %s does not match its sha256' % f)
        self.man = man

    def path(self, name):
        if name is None:
            return None
        if self.man is None or name not in self.man['files']:
            self.problems.append('file %s not named by the manifest' % name)
            return None
        p = os.path.join(self.dir, name)
        return p if os.path.isfile(p) else None

    def json(self, name):
        p = self.path(name)
        return None if p is None else load_json(p, 'evidence file %s' % name)

    def text(self, name):
        p = self.path(name)
        if p is None:
            return None
        with open(p, 'rb') as f:
            return f.read()

    def case(self, name):
        for c in (self.man or {}).get('cases', []):
            if c.get('case') == name:
                return c
        return None


# ---------------------------------------------------------------------------------------------------------------
# Declarative evaluation (R6.GATE.8)

def recompute_outcome(result):
    """The gate's own sec. 7 precedence: a stop's outcome (USAGE, INTERNAL, ERROR, VOID) first, then VOID for a
    failed preflight, FAIL for failed record checks or a FAIL item, REVIEW_REQUIRED for a REVIEW item, else PASS.

    A stop is `{class, message, detail}` (DESIGN-r6.md sec. 7, result schema): it names no outcome, and which of
    USAGE, INTERNAL, ERROR and VOID stopped the run is not derivable from `preflight`, `record_checks` and `items`.
    For a result with a stop, the stop's outcome is the result's `outcome` when it is one of those four, and the
    caller's cross-check against the exit file decides it; any other `outcome` beside a stop is reported as the
    inconsistent value `STOP_WITHOUT_STOP_OUTCOME`, which equals no expected outcome."""
    stop = result.get('stop')
    if isinstance(stop, dict) and stop:
        o = stop.get('outcome', result.get('outcome'))
        return o if o in ('USAGE', 'INTERNAL', 'ERROR', 'VOID') else 'STOP_WITHOUT_STOP_OUTCOME'
    if result.get('outcome') == 'USAGE' and 'items' not in result and 'preflight' not in result:
        # the USAGE object written to stderr (no result file is written for USAGE, R6.OUT.1)
        return 'USAGE'
    if result.get('operation') == 'purity-lint' and isinstance(result.get('findings'), list):
        # the purity lint's verdict is its findings list
        return 'FAIL' if result['findings'] else 'PASS'
    if any(not p.get('passed') for p in result.get('preflight') or []):
        return 'VOID'
    rc = result.get('record_checks')
    if rc is not None and not rc.get('holds', False):
        return 'FAIL'
    items = result.get('items') or []
    if any(i.get('decision') == 'FAIL' for i in items):
        return 'FAIL'
    if any(i.get('decision') == 'REVIEW_REQUIRED' for i in items):
        return 'REVIEW_REQUIRED'
    return 'PASS'


class Unbound(Exception):
    pass


def _bind(v, bindings):
    if isinstance(v, str) and v.startswith('$'):
        if v[1:] not in bindings:
            raise Unbound(v)
        return bindings[v[1:]]
    return v


def _field(obj, k):
    if k == 'file':
        return obj.get('file', obj.get('subject'))
    if k == 'path':
        return obj.get('path', obj.get('file', obj.get('subject')))
    return obj.get(k)


def _has(obj, k, v):
    """One field condition of an item pattern: `<field>_include` tests membership in the item's list field (for
    example `alternatives_include`), `profile` also matches a member of the item's `profiles`, any other key tests
    equality of the field."""
    if k.endswith('_include') and k[:-len('_include')] in obj:
        got = obj.get(k[:-len('_include')])
        return v in got if isinstance(got, list) else got == v
    if k == 'profile' and 'profile' not in obj and isinstance(obj.get('profiles'), list):
        return v in obj['profiles']
    return _field(obj, k) == v


def _names(obj, subj):
    """Whether a result site or item is the subject `subj`: its subject, site or site_id equal to it, or that id
    with the pin suffix (`<file>:<line>@<pin>`); a `<file>:<line>` subject also names the item at that file and
    line; a delegated class is named by its class id (`delegated_class`), its items' subject being a message."""
    if not isinstance(subj, str):
        return False
    ids = [obj.get(k) for k in ('subject', 'site', 'site_id') if isinstance(obj.get(k), str)]
    if subj in ids or obj.get('delegated_class') == subj or any(x.startswith(subj + '@') for x in ids):
        return True
    m = re.fullmatch(r'(.+):([0-9]+)', subj)
    return bool(m and obj.get('file') == m.group(1) and str(obj.get('line')) == m.group(2))


def parse_filter(spec, bindings):
    """`unit[k=v,...]` with `|` between alternative values; `unit[k_nonempty]` tests a non-empty field."""
    m = re.fullmatch(r'([a-z_]+)(?:\[(.*)\])?', spec)
    if not m:
        return None, None
    unit, body = m.group(1), m.group(2)
    conds = []
    if body:
        for part in body.split(','):
            if '=' in part:
                k, v = part.split('=', 1)
                conds.append((k, [_bind(x, bindings) for x in v.split('|')]))
            elif part.endswith('_nonempty'):
                conds.append((part[:-len('_nonempty')], None))
            else:
                return None, None
    return unit, conds


def _match(obj, conds):
    for k, vals in conds:
        got = _field(obj, k)
        if vals is None:
            if not got:
                return False
        elif k == 'profile' and got is None and isinstance(obj.get('profiles'), list):
            if not set(str(v) for v in vals) & set(str(p) for p in obj['profiles']):
                return False
        elif str(got) not in [str(v) for v in vals] and got not in vals:
            return False
    return True


def extract_count(key, result, bindings, attested):
    """Returns (value, source) for a count key, or (None, None) when the key cannot be extracted."""
    if key.startswith('finding_counts:'):
        cur = result.get('finding_counts')
        k = key[len('finding_counts:'):]
        if isinstance(cur, dict) and k in cur:
            # the result's flat form: one key `obligation/decision/class`
            return cur[k], 'result'
        for p in k.split('/'):
            cur = cur.get(p) if isinstance(cur, dict) else None
        return (cur if cur is not None else 0), 'result'
    if key.startswith('site_counts:'):
        sc = result.get('site_counts') or {}
        return sc.get(key[len('site_counts:'):], 0), 'result'
    unit, conds = parse_filter(key, bindings)
    if unit in ('items', 'findings', 'hits', 'sites', 'lines', 'sentences') and conds is not None:
        src = {'items': 'items', 'findings': 'items', 'hits': 'hits', 'sites': 'sites'}.get(unit, 'items')
        objs = [o for o in (result.get(src) or []) if isinstance(o, dict) and _match(o, conds)]
        if unit == 'lines':
            return len({(_field(o, 'file'), o.get('line')) for o in objs}), 'result'
        if unit == 'sentences':
            return len({(_field(o, 'file'), o.get('line'), o.get('sentence')) for o in objs}), 'result'
        if src not in result and not objs and unit in ('hits', 'sites') and key in attested:
            return attested[key], 'attested'
        return len(objs), 'result'
    cur = result
    for p in key.split('.'):
        cur = cur.get(p) if isinstance(cur, dict) else None
    if isinstance(cur, list):
        # a count key naming a list field of the result (merger_groups) counts its members
        return len(cur), 'result'
    if cur is not None:
        return cur, 'result'
    if key in attested:
        return attested[key], 'attested'
    return None, None


# the item fields whose values are enumerations or literals, so that `{"all": ..., "have": {...}}` is decided by
# equality; any other `have` field is prose and stays attested
LITERAL_FIELDS = frozenset(['obligation', 'class', 'decision', 'state', 'profiles', 'rule_id', 'segment'])
SELECTABLE = frozenset(['items', 'hits', 'sites'])


def _select(spec, result, bindings):
    """The result members a `unit[filter]` spec selects, or None when the spec is not such a filter."""
    if not isinstance(spec, str):
        return None
    unit, conds = parse_filter(spec, bindings)
    if unit not in SELECTABLE or conds is None:
        return None
    return [o for o in (result.get(unit) or []) if isinstance(o, dict) and _match(o, conds)]


def _computed_invariant(k, v, result, bindings):
    """(holds, actual, 'result') for an invariant the gate computes from the result alone, else None."""
    if k == 'none':
        sel = _select(v, result, bindings)
        if sel is not None:
            return not sel, len(sel), 'result'
        return None
    if k == 'record_admitted' and isinstance(v, str) and \
            isinstance((result.get('inputs') or {}).get('classify_records'), list):
        # the records the post-freeze route admitted, as the result lists them
        want = _bind(v, bindings)
        got = sorted(str(x.get('path')) for x in result['inputs']['classify_records'] if isinstance(x, dict))
        return want in got, got, 'result'
    if k == 'composed_blob' and isinstance(result.get('landing_compositions'), list):
        a = sorted(str(c.get('composed_blob')) for c in result['landing_compositions'] if isinstance(c, dict))
        return v in a, a, 'result'
    if k == 'a5_unequal_paths' and isinstance((result.get('record_directory') or {}).get('unequal'), dict):
        a = len(result['record_directory']['unequal'])
        return a == v, a, 'result'
    if k == 'rule_active' and isinstance((result.get('record_directory') or {}).get('state'), str):
        a = result['record_directory']['state'] == 'active'
        return a == v, a, 'result'
    if k.startswith('{'):
        inv = json.loads(k)
        if set(inv) == {'all', 'have'} and isinstance(inv['have'], dict) and set(inv['have']) <= LITERAL_FIELDS:
            sel = _select(inv['all'], result, bindings)
            if sel is not None:
                bad = [o.get('subject') for o in sel if not all(_has(o, f, _bind(x, bindings)) if f != 'profiles'
                                                                else o.get(f) == x for f, x in inv['have'].items())]
                return not bad, {'selected': len(sel), 'not_having': bad[:5]}, 'result'
        if set(inv) == {'condition', 'holds'} and isinstance(result.get('side_changes'), list):
            evs = [ev for sc in result['side_changes'] if isinstance(sc, dict)
                   for ev in sc.get('record_conditions') or [] if isinstance(ev, dict)]
            if evs:
                failed = any(inv['condition'] in (ev.get('failed') or []) for ev in evs)
                return (not failed) == inv['holds'], not failed, 'result'
    return None


def eval_invariant(k, v, result, case, attested, bindings):
    """Returns (holds, actual, source). Keys the gate can compute from the retained result are computed; any
    other key must be attested in the case's sha256-checked attested file, equal to the expectation."""
    if isinstance(result, dict) and result.get('schema') == SCHEMA_GATE:
        comps = [r for r in result.get('rows', []) if 'components' in r]
        if k == 'composite_status':
            a = [r.get('composite_status') for r in comps]
            return a == [v], a, 'gate result'
        if k == 'component_results_preserved':
            a = bool(comps) and all(all({'id', 'status', 'findings'} <= set(c) for c in r['components'])
                                    for r in comps)
            return a == v, a, 'gate result'
    if result is not None:
        if k == 'no_stop':
            a = not result.get('stop')
            return a == v, a, 'result'
        if k == 'stop_class_in':
            a = (result.get('stop') or {}).get('class')
            return a in v, a, 'result'
        if k in ('admission_mode', 'admission_mode_not'):
            a = ((result.get('config') or {}).get('admission') or {}).get('mode')
            return (a == v) if k == 'admission_mode' else (a != v), a, 'result'
        if k == 'not_class':
            a = sorted({i.get('class') for i in result.get('items') or []})
            vals = v if isinstance(v, list) else [v]
            return not (set(vals) & set(a)), a, 'result'
        if k == 'items_include':
            items = result.get('items') or []
            miss = [w for w in v if not any(all(_has(i, kk, _bind(vv, bindings)) for kk, vv in w.items())
                                            for i in items)]
            return not miss, {'missing': miss}, 'result'
        if k == 'failed_conditions_include' and isinstance(result.get('side_changes'), list):
            # the record conditions each side change's evaluation failed (RC1-RC13), read from the result
            a = sorted({str(x) for sc in result['side_changes'] if isinstance(sc, dict)
                        for ev in sc.get('record_conditions') or [] if isinstance(ev, dict)
                        for x in ev.get('failed') or []})
            return v in a, a, 'result'
        if k == 'tool_run_exit':
            return case.get('_exit') == v, case.get('_exit'), 'exit file'
        if k == 'stderr_json_outcome':
            return result.get('outcome') == v, result.get('outcome'), 'result'
        computed = _computed_invariant(k, v, result, bindings)
        if computed is not None:
            return computed
    if k == 'out_dir_created' and isinstance(case.get('out_dir_exists'), bool):
        # the recorder's observation of the --out directory right after the run (manifest field)
        return case['out_dir_exists'] == v, case['out_dir_exists'], 'manifest'
    if k == 'no_result_written':
        a = case.get('_result_absent')
        if a is not None:
            return a == v, a, 'out listing'
    if k in attested:
        return attested[k] == v, attested[k], 'attested'
    return False, None, 'unattested'


def _check_of(shared):
    """The --check operand of a parsed coverage invocation (exactly one, by _coverage_invocation)."""
    return shared[shared.index('--check') + 1]


def _coverage_invocation(argv):
    """Returns the evaluated commit and the arguments which must match across the pair."""
    if not (isinstance(argv, list) and argv and argv[0] == 'coverage'
            and all(isinstance(arg, str) for arg in argv)):
        return None
    shared = list(argv)
    commit = None
    for flag in ('--commit', '--out'):
        if shared.count(flag) != 1:
            return None
        index = shared.index(flag)
        if index + 1 == len(shared) or shared[index + 1].startswith('--'):
            return None
        if flag == '--commit':
            commit = shared[index + 1]
        del shared[index:index + 2]
    if shared.count('--check') != 1:
        return None
    index = shared.index('--check')
    if index + 1 == len(shared) or not shared[index + 1] or shared[index + 1].startswith('--'):
        return None
    return commit, shared


# The A1 staging amendment r2 (sec. 1, DELTA-PROPOSAL.json `item2`): the authoritative Item 2 check and the exact
# approved source and pattern pins of its three tree review profiles. Each retained S11-2a invocation names this
# check, and each result reports these profiles under the same reviewed configuration pin.
ITEM2_CHECK = 'item2'
ITEM2_PLANTED_PATH = 'book/ch18-beyond.md'
ITEM2_PROFILES = {
    'p0-core': ('9882df8f2d41eee47790560b0e22aac03e95370f',
                'verification/audits/foundations/a1-scope-phase0-20261120/sites.json',
                '00165404a6411a219a875ea1d9d6187e1d0d8f9951637fbb31ca0280212b4a5f',
                '939cafdad4dbcb47762af98a82a357bf2f1ff0da17408177d806eaff18204d93'),
    'p0-para': ('9882df8f2d41eee47790560b0e22aac03e95370f',
                'verification/audits/foundations/a1-scope-phase0-20261120/sites.json',
                '00165404a6411a219a875ea1d9d6187e1d0d8f9951637fbb31ca0280212b4a5f',
                '28b482757bee068e79eaac85619b4fd0a0e6f23e4d72cdd2b8252fb22167bd42'),
    'ledger-ext': ('9882df8f2d41eee47790560b0e22aac03e95370f',
                   'verification/audits/foundations/a1exit-ledger-20261120/ledger_check.py',
                   '34314041cff64f01287bd195d33c61cd17882166e11bd1296b005e72d4ad78e8',
                   '63f19fbfea68e9468aadcb5fa52685f1c4f15f38f4b376dc9d48de5c0ef25a2e'),
}


def item2_profile_problems(result, commit, deny_exempt):
    """The Item 2 profile selection of one retained coverage result: the result reports the three approved review
    profiles at their exact pins, and `profiles_evaluated` at the evaluated commit is exactly those three plus every
    deny profile the result's configuration reports, or the three alone where the commit is deny-exempt (exact E or H,
    R6.PROF.4). A deny set that is required and empty is a missing scan, never a clean one."""
    probs = []
    profs = result.get('profiles')
    if not isinstance(profs, list) or not all(isinstance(p, dict) for p in profs):
        return ['no profile records']
    by = {}
    for p in profs:
        by.setdefault(p.get('name'), []).append(p)
    for name, (src_commit, path, blob, pattern) in sorted(ITEM2_PROFILES.items()):
        got = by.get(name) or []
        if len(got) != 1 or got[0].get('kind') != 'review' or got[0].get('source_commit') != src_commit or \
                got[0].get('path') != path or got[0].get('blob_sha256') != blob or \
                got[0].get('pattern_sha256') != pattern:
            probs.append('profile %s is not at its approved pin' % name)
    deny = sorted(n for n, ps in by.items() if any(p.get('kind') == 'deny' for p in ps))
    want = sorted(set(ITEM2_PROFILES) | (set() if deny_exempt else set(deny)))
    if not deny_exempt and not deny:
        probs.append('no deny profile reported for a tree that requires the deny scan')
    if result.get('profiles_evaluated') != {commit: want}:
        probs.append('profiles_evaluated %r is not %r' % (result.get('profiles_evaluated'), {commit: want}))
    return probs


def _s11_unmutated_result(ev, case, result):
    """Bind S11-2a's subtraction to the retained R6.PLAN.4 coverage run on E."""
    named = ev.case('unmutated')
    if not named or case.get('baseline_argv') != named.get('argv'):
        return None
    linked_bytes = ev.text(case.get('baseline_file'))
    if linked_bytes is None or linked_bytes != ev.text(named.get('result_file')):
        return None
    before = ev.json(named.get('result_file'))
    unmutated = _coverage_invocation(named.get('argv'))
    mutated = _coverage_invocation(case.get('argv'))
    # R6.NOTE.1 pins the ledger's E independently of the runner's chosen baseline.
    pin = 'e837e3dbaa605efc867a213f3345cee14c36d8f5'
    if not (isinstance(before, dict) and isinstance(result, dict) and unmutated and mutated
            and unmutated[0] == pin and mutated[0] != pin and unmutated[1] == mutated[1]
            and before.get('operation') == result.get('operation') == 'coverage'
            and before.get('evaluated') == {'commit': pin}
            and result.get('evaluated') == {'commit': mutated[0]}
            and before.get('config') and before.get('config') == result.get('config')
            and isinstance(before.get('items'), list)):
        return None
    # Open: the reviewed configuration's path and digest are not bound here. Staging r2 requires both runs to use
    # "the same reviewed config pin" but names no source from which the gate could read the expected path and digest
    # (no staged configuration or admission record exists yet); a configuration substituted in both runs alike
    # passes this check, and the deny set is read from the results' own profile records.
    # A1 staging amendment r2: both invocations name the authoritative check (a same wrong check in both is refused),
    # and both results evaluate the approved profiles: the review set alone at exact E, the review set and the
    # configured deny profiles at the planted child.
    if _check_of(unmutated[1]) != ITEM2_CHECK or _check_of(mutated[1]) != ITEM2_CHECK or \
            before.get('profiles') != result.get('profiles') or \
            item2_profile_problems(before, pin, True) or item2_profile_problems(result, mutated[0], False):
        return None
    # the adopted mutation: one changed path, the planted file, with distinct before and after blobs
    planted = str((case.get('bindings') or {}).get('new_line') or '').rsplit(':', 1)[0]
    mut = case.get('mutation')
    if planted != ITEM2_PLANTED_PATH or not isinstance(mut, list) or len(mut) != 1 or \
            not isinstance(mut[0], dict) or mut[0].get('path') != planted or \
            not all(isinstance(mut[0].get(k), str) and HEX40.match(mut[0][k]) for k in ('before', 'after')) or \
            mut[0]['before'] == mut[0]['after']:
        return None
    outcome = recompute_outcome(before)
    if outcome not in ('PASS', 'REVIEW_REQUIRED', 'FAIL') or before.get('outcome') != outcome:
        return None
    exit_bytes = ev.text(named.get('exit_file'))
    if exit_bytes != ('%d\n' % TOOL_EXIT[outcome]).encode():
        return None
    return before


def is_line_patch_rc8(row):
    procedure = row.get('procedure') or {}
    return row['id'] == 'LINE-PATCH-RC8' and procedure.get('name') == 'line-patch-rc8' and \
        procedure.get('lib') == 'oracle'


def line_patch_case(ev, case):
    """Read one raw in-process RC8 evaluation and its inputs from the evidence set."""
    if case.get('argv') != ['in-process', 'line-patch RC8 evaluation']:
        raise ValueError('missing or malformed in-process RC8 invocation')
    name = case.get('result_file')
    data = ev.text(name) if isinstance(name, str) else None
    if data is None:
        raise ValueError('missing evaluation file')

    def unique_fields(pairs):
        obj = dict(pairs)
        if len(obj) != len(pairs):
            raise ValueError('duplicate evaluation or input key')
        return obj

    def reject_constant(value):
        raise ValueError('invalid JSON constant %s' % value)

    doc = json.loads(data.decode('utf-8'), object_pairs_hook=unique_fields,
                     parse_constant=reject_constant, parse_float=reject_constant)
    if not isinstance(doc, dict) or set(doc) != {'operation', 'context', 'candidate_blob', 'record', 'ledger',
                                                 'evaluation'} or doc['operation'] != 'execution':
        raise ValueError('invalid RC8 evaluation document')
    context, record, ledger, evaluation = (doc[k] for k in ('context', 'record', 'ledger', 'evaluation'))
    if not all(isinstance(v, dict) for v in (context, record, ledger, evaluation)):
        raise ValueError('invalid RC8 inputs or result')
    if set(context) != {'H', 'M', 'X', 'classes', 'record_refs'} or not all(
            isinstance(context[k], str) and HEX40.fullmatch(context[k]) for k in ('H', 'M', 'X')) or \
            context['classes'] != [] or context['record_refs'] != {}:
        raise ValueError('invalid synthetic evaluator context')
    entries = record.get('paths')
    if not isinstance(entries, list) or len(entries) != 1 or not isinstance(entries[0], dict):
        raise ValueError('the reconciliation record must retain one entry')
    entry = entries[0]
    path = entry.get('path')
    files = ledger.get('files')
    if path != 'doc/s.md' or path != evaluation.get('path') or \
            not isinstance(files, dict) or set(files) != {path} or not isinstance(files[path], dict):
        raise ValueError('the ledger and evaluation must name the record entry path')
    if ledger.get('base') != context['H'] or record.get('ledger_base') != context['H'] or \
            record.get('M') != context['M'] or record.get('X') != context['X']:
        raise ValueError('the ledger or record does not name the evaluator roles')
    list_fields = ('splices', 'retained', 'mirrors', 'ignored_fields', 'errors', 'edits')
    if set(ledger) != {'base', 'splices', 'files', 'retained', 'mirrors', 'ignored_fields', 'errors', 'edits',
                       'pin_rules', 'raw'} or not all(isinstance(ledger[key], list) for key in list_fields) or \
            not ledger['splices'] or not isinstance(ledger['pin_rules'], dict) or \
            not all(isinstance(splice, dict) and isinstance(splice.get('new'), str) and
                    splice.get('new_bytes') == splice['new'].encode().hex() for splice in ledger['splices']) or \
            not isinstance(ledger['raw'], dict):
        raise ValueError('invalid retained line-patch ledger')
    raw = ledger['raw']
    raw_files = raw.get('files')
    if set(raw) != {'files', 'splices', 'edits'} or not isinstance(raw_files, dict) or set(raw_files) != {path} or \
            not isinstance(raw_files[path], dict) or set(raw_files[path]) != {'base_sha256', 'expected_sha256'} or \
            not isinstance(raw['edits'], list) or raw['splices'] != [
                {k: v for k, v in splice.items() if k != 'new_bytes'} for splice in ledger['splices']]:
        raise ValueError('invalid raw line-patch ledger view')
    if set(files[path]) != {'base_sha256', 'expected_sha256'} or \
            files[path]['base_sha256'] != raw_files[path]['base_sha256']:
        raise ValueError('raw and normalized file entries disagree on the base hash')
    digest = files[path]['expected_sha256']
    if not all(isinstance(value, str) and re.fullmatch('[0-9a-f]{64}', value)
               for value in (digest, raw_files[path]['expected_sha256'], files[path]['base_sha256'])):
        raise ValueError('invalid ledger file hash')
    holds, failed = evaluation.get('holds'), evaluation.get('failed')
    if not isinstance(holds, dict) or type(holds.get('RC8')) is not bool or not isinstance(failed, list) or \
            not all(isinstance(name, str) for name in failed) or len(set(failed)) != len(failed) or \
            holds['RC8'] == ('RC8' in failed):
        raise ValueError('malformed or inconsistent RC8 verdict')
    return doc, entry, digest


def eval_line_patch_case(exp, name, ev, findings):
    actual = {'case': name}
    try:
        cases = (ev.man or {}).get('cases', [])
        case, = [c for c in cases if isinstance(c, dict) and c.get('case') == name]
        doc, _, _ = line_patch_case(ev, case)
    except ValueError as exc:
        findings.append(('raw-evidence-missing', 'case %r: %s' % (name, exc)))
        return actual
    evaluation = doc['evaluation']
    actual['outcome'] = 'RC_HOLDS' if evaluation['holds']['RC8'] else 'RC_FAILS'
    if actual['outcome'] != exp.get('outcome'):
        findings.append(('declarative-mismatch', 'case %r: unexpected RC8 verdict %s' % (name, actual['outcome'])))
    if set(exp) - {'case', 'outcome', 'invariants'}:
        findings.append(('raw-evidence-missing', 'case %r: unsupported RC8 expectation fields' % name))
    for invariant in exp.get('invariants', []):
        actual['failed_conditions'] = evaluation['failed']
        if invariant != {'failed_conditions_include': 'RC8'} or 'RC8' not in evaluation['failed']:
            findings.append(('declarative-mismatch', 'case %r: failed conditions %s' % (name, evaluation['failed'])))
    return actual


def eval_case(exp, case_name, ev, row, record, findings_out):
    """Evaluates one expectation (the row's, one of its cases, or its restored case) against the retained
    evidence of the case. Appends findings; returns the extracted actual."""
    if is_line_patch_rc8(row):
        return eval_line_patch_case(exp, case_name, ev, findings_out)
    rid = row['id']
    c = ev.case(case_name)
    actual = {'case': case_name}
    if c is None:
        findings_out.append(('raw-evidence-missing', 'no evidence for case %r' % case_name))
        return actual
    bindings = c.get('bindings') or {}
    attested = {}
    if c.get('attested'):
        attested = ev.json(c['attested']) or {}
    exit_code = None
    if c.get('exit_file'):
        t = ev.text(c['exit_file'])
        try:
            exit_code = int(t.decode().strip()) if t is not None else None
        except ValueError:
            exit_code = None
        if exit_code is None:
            findings_out.append(('raw-evidence-missing', 'exit file of case %r unreadable' % case_name))
    result = ev.json(c['result_file']) if c.get('result_file') else None
    c['_exit'] = exit_code
    listing = ev.json(c['out_listing']) if c.get('out_listing') else None
    if listing is not None:
        c['_result_absent'] = not any(str(x).endswith('result.json') for x in listing)
    actual['exit'] = exit_code
    if rid == 'S11-2b' and case_name == '':
        # A1 staging amendment r2: S11-2b runs coverage under the same named Item 2 check on its own child
        inv = _coverage_invocation(c.get('argv'))
        if not inv or _check_of(inv[1]) != ITEM2_CHECK:
            findings_out.append(('declarative-mismatch', 'case %r: the coverage invocation does not name --check %s'
                                 % (case_name, ITEM2_CHECK)))
    o = exp.get('outcome')
    try:
        if o in TOOL_OUTCOMES:
            if result is None:
                findings_out.append(('raw-evidence-missing', 'no result file for case %r' % case_name))
                return actual
            got = recompute_outcome(result)
            actual['outcome'] = got
            if result.get('outcome') != got:
                findings_out.append(('declarative-mismatch', 'case %r: result outcome %r, recomputed %r'
                                     % (case_name, result.get('outcome'), got)))
            if got != o:
                findings_out.append(('declarative-mismatch', 'case %r: outcome %r, expected %r' % (case_name, got, o)))
            want_exit = exp.get('exit', TOOL_EXIT[o])
            if exit_code != want_exit or exit_code != TOOL_EXIT.get(got):
                findings_out.append(('declarative-mismatch', 'case %r: exit %r, expected %r' % (case_name, exit_code,
                                                                                               want_exit)))
        elif o in GATE_OUTCOMES:
            if result is None:
                findings_out.append(('raw-evidence-missing', 'no gate result for case %r' % case_name))
                return actual
            got = result.get('verdict')
            actual['outcome'] = got
            actual['gate_findings'] = sorted({f for e in result.get('rows', []) for f in e.get('findings', [])}
                                             | set(result.get('file_findings', [])))
            if got != o:
                findings_out.append(('declarative-mismatch', 'case %r: verdict %r, expected %r' % (case_name, got, o)))
            want_exit = exp.get('exit', GATE_EXIT[o])
            if exit_code != want_exit:
                findings_out.append(('declarative-mismatch', 'case %r: exit %r, expected %r' % (case_name, exit_code,
                                                                                               want_exit)))
            gf = set(actual['gate_findings'])
            if 'gate_findings_include' in exp and not set(exp['gate_findings_include']) <= gf:
                findings_out.append(('declarative-mismatch', 'case %r: gate findings %s lack %s'
                                     % (case_name, sorted(gf), exp['gate_findings_include'])))
            if 'gate_findings_exact' in exp and set(exp['gate_findings_exact']) != gf:
                findings_out.append(('declarative-mismatch', 'case %r: gate findings %s, expected exactly %s'
                                     % (case_name, sorted(gf), exp['gate_findings_exact'])))
        elif o == 'ANY' or o is None:
            pass
        elif o in ('NO_ITEM', 'ITEM') and result is not None:
            # over the items the case's classes_exact filter selects, when it states one; else over all items
            sel = result.get('items') or []
            ce = exp.get('classes_exact')
            if isinstance(ce, dict) and len(ce) == 1:
                _, conds = parse_filter(next(iter(ce)), bindings)
                sel = [i for i in sel if conds is not None and _match(i, conds)]
            n = len(sel)
            actual['outcome'] = 'ITEM' if n else 'NO_ITEM'
            if actual['outcome'] != o:
                findings_out.append(('declarative-mismatch', 'case %r: %s, expected %s' % (case_name,
                                                                                         actual['outcome'], o)))
        elif o in ('RESULT_EQUAL_CLEAN', 'RESULT_EQUAL_FULL_STORE', 'RESULT_EQUAL_WITHOUT_AMENDMENT',
                   'REPLAY_EQUAL') and c.get('baseline_file'):
            # gate-computed: the case's item tuples and outcome equal those of the retained baseline run
            base = ev.json(c['baseline_file'])
            same = (result is not None and base is not None and _tuples(result) == _tuples(base)
                    and recompute_outcome(result) == recompute_outcome(base))
            actual['outcome'] = o if same else 'RESULT_DIFFERS'
            if not same:
                findings_out.append(('declarative-mismatch', 'case %r: result differs from its baseline' % case_name))
        elif o in SUBJECT_OUTCOMES | MUT_OUTCOMES:
            got = attested.get('outcome')
            actual['outcome'] = got
            if got != o:
                findings_out.append(('declarative-mismatch' if got is not None else 'raw-evidence-missing',
                                     'case %r: attested outcome %r, expected %r' % (case_name, got, o)))
        if 'stop_class' in exp:
            got = ((result or {}).get('stop') or {}).get('class')
            actual['stop_class'] = got
            if got != exp['stop_class']:
                findings_out.append(('declarative-mismatch', 'case %r: stop class %r, expected %r'
                                     % (case_name, got, exp['stop_class'])))
        items = (result or {}).get('items') or []
        for key, inc in (('classes_exact', False), ('classes_include', True)):
            if key not in exp:
                continue
            spec = exp[key]
            pairs = spec.items() if isinstance(spec, dict) else [('items', spec)]
            for filt, want in pairs:
                unit, conds = parse_filter(filt, bindings)
                if conds is None:
                    raise FileInvalid('row %s: unparseable item filter %r' % (rid, filt))
                got = sorted({i.get('class') for i in items if _match(i, conds)})
                actual.setdefault(key, {})[filt] = got
                ok = set(want) <= set(got) if inc else set(want) == set(got)
                if not ok:
                    findings_out.append(('declarative-mismatch', 'case %r: %s %s = %s, expected %s'
                                         % (case_name, key, filt, got, want)))
        for key, want in sorted((exp.get('counts') or {}).items()):
            got, src = extract_count(key, result or {}, bindings, attested)
            actual.setdefault('counts', {})[key] = got
            if src is None:
                findings_out.append(('raw-evidence-missing', 'case %r: count %s not extractable' % (case_name, key)))
            elif got != want:
                findings_out.append(('declarative-mismatch', 'case %r: count %s = %r, expected %r'
                                     % (case_name, key, got, want)))
        for s in exp.get('sites') or []:
            subj = _bind(s.get('subject'), bindings) if 'subject' in s else None
            fields = {k: v for k, v in s.items() if k != 'subject'}
            if subj is None and isinstance(s.get('all'), str) and \
                    set(s) - {'all'} <= LITERAL_FIELDS and _select(s['all'], result or {}, bindings) is not None:
                # every selected result site has the stated literal fields (read from the result)
                sel = _select(s['all'], result or {}, bindings)
                bad = [x.get('site_id') for x in sel if not all(x.get(k) == v for k, v in s.items() if k != 'all')]
                if not sel or bad:
                    findings_out.append(('declarative-mismatch', 'case %r: site condition %s fails for %s'
                                         % (case_name, s, bad[:5] or 'no selected site')))
                continue
            if subj is None:
                got = attested.get('sites:' + json.dumps(s, sort_keys=True))
                if got is not True:
                    findings_out.append(('raw-evidence-missing' if got is None else 'declarative-mismatch',
                                         'case %r: site condition %s not attested' % (case_name, s)))
                continue
            sites = [x for x in ((result or {}).get('sites') or []) if _names(x, subj)]
            sitems = [i for i in items if _names(i, subj)]
            ok = bool(sites or sitems)
            for k, v in fields.items():
                if k in ('classes_exact', 'classes_include'):
                    got = sorted({i.get('class') for i in sitems})
                    ok = ok and (set(v) == set(got) if k == 'classes_exact' else set(v) <= set(got))
                elif k == 'added_relative_to_unmutated':
                    baseline = (_s11_unmutated_result(ev, c, result) if rid == 'S11-2a'
                                else ev.json(c.get('baseline_file')))
                    if not (isinstance(baseline, dict) and isinstance(baseline.get('items'), list)
                            and isinstance(v, dict) and v):
                        findings_out.append(('raw-evidence-missing', 'case %r: site %s has no countable baseline'
                                             % (case_name, subj)))
                        continue
                    additions = {}
                    for query in sorted(v):
                        before, before_source = extract_count(query, baseline, bindings, {})
                        after, after_source = extract_count(query, result or {}, bindings, {})
                        if (before_source != 'result' or after_source != 'result'
                                or type(before) is not int or type(after) is not int):
                            findings_out.append(('raw-evidence-missing', 'case %r: site %s count %s unavailable'
                                                 % (case_name, subj, query)))
                            continue
                        additions[query] = after - before
                    actual.setdefault(k, {})[subj] = additions
                    ok = ok and additions == v
                else:
                    ok = ok and any(x.get(k) == v for x in sites + sitems)
            if not ok:
                findings_out.append(('declarative-mismatch', 'case %r: site %s does not meet %s' % (case_name, subj,
                                                                                                    fields)))
        for inv in exp.get('invariants') or []:
            if len(inv) > 1:
                k, v = json.dumps(inv, sort_keys=True), True
            else:
                k, v = next(iter(inv.items()))
            if k == 'baseline':
                continue
            holds, got, src = eval_invariant(k, v, result, c, attested, bindings)
            actual.setdefault('invariants', {})[k] = {'value': got, 'source': src}
            if not holds:
                findings_out.append(('raw-evidence-missing' if src == 'unattested' else 'declarative-mismatch',
                                     'case %r: invariant %s %s' % (case_name, k, 'not attested' if src == 'unattested'
                                                                   else 'does not hold (%r)' % (got,))))
    except Unbound as exc:
        findings_out.append(('raw-evidence-missing', 'case %r: binding %s unbound' % (case_name, exc)))
    # the runner's value must equal the value the gate reads
    ra = record.get('actual') if isinstance(record.get('actual'), dict) else {}
    rc = ra.get('cases', {}).get(case_name) if isinstance(ra.get('cases'), dict) else (ra if case_name == '' else None)
    if isinstance(rc, dict):
        for k in ('exit', 'outcome', 'stop_class'):
            if k in rc and k in actual and rc[k] != actual[k]:
                findings_out.append(('declarative-mismatch', 'case %r: the runner states %s %r, the evidence %r'
                                     % (case_name, k, rc[k], actual[k])))
    return actual


# ---------------------------------------------------------------------------------------------------------------
# Procedural evaluation (R6.GATE.8)

def _tuples(result, decision=None):
    return sorted(set((i.get('obligation'), i.get('class'), i.get('segment'), i.get('fingerprint'))
                      for i in (result or {}).get('items') or []
                      if decision is None or i.get('decision') == decision))


def eval_line_patch_oracle(row, ev, findings):
    """Derive both RC8 expectations from one retained candidate blob and a one-field ledger change."""
    actual = {'lib': 'oracle', 'agree': False}
    try:
        manifest = ev.man or {}
        proc = manifest.get('procedure')
        cases = manifest.get('cases', [])
        names = [c['case'] for c in row['expect']['cases']]
        if not isinstance(proc, dict) or proc.get('name') != 'line-patch-rc8' or proc.get('lib') != 'oracle' or \
                len(cases) != 2 or not all(isinstance(case, dict) for case in cases) or \
                [case.get('case') for case in cases] != names:
            raise ValueError('expected the two named RC8 cases and their oracle inputs')
        outputs = [case.get('result_file') for case in cases]
        candidate_file = proc.get('oracle_output')
        digest_file = proc.get('candidate_digest')
        files = outputs + [candidate_file, digest_file]
        if not all(isinstance(name, str) for name in files) or len(set(files)) != 4 or \
                proc.get('tool_output') != outputs:
            raise ValueError('oracle inputs do not name two distinct evaluations and both candidate blobs')
        candidate = ev.text(candidate_file)
        companion = ev.text(digest_file)
        if candidate is None or companion is None:
            raise ValueError('candidate or digest bytes are missing')
        first, second = (line_patch_case(ev, case) for case in cases)
        first_doc, entry, first_expected = first
        second_doc, _, second_expected = second
        path = entry['path']

        def same_input(value):
            doc = value[0]
            ledger = doc['ledger']
            file_entry = {k: v for k, v in ledger['files'][path].items() if k != 'expected_sha256'}
            inputs = (doc['context'], doc['record'], dict(ledger, files={path: file_entry}))
            return json.dumps(inputs, sort_keys=True, ensure_ascii=False)

        if second[1]['path'] != path or same_input(first) != same_input(second):
            raise ValueError('evaluator inputs differ beyond the normalized expected_sha256')
        digest = hashlib.sha256(candidate).hexdigest()
        git_blob = hashlib.sha1(('blob %d\0' % len(candidate)).encode() + candidate).hexdigest()
        if first_doc['candidate_blob'] != git_blob or second_doc['candidate_blob'] != git_blob or \
                entry.get('x') != git_blob or entry.get('x_sha256') != digest:
            raise ValueError('candidate bytes do not match the observed blob and reconciliation entry')
        if companion != (digest + '\n').encode('ascii'):
            raise ValueError('the candidate digest file does not match the patched bytes')
        companion_blob = hashlib.sha1(('blob %d\0' % len(companion)).encode() + companion).hexdigest()
        # World derives the synthetic candidate from H as its sole parent with subject X and two regular files.
        # Recompute the Overlay.derive identity without importing the engine or trusting a reported commit id.
        base = first_doc['context']['H'].encode('ascii')
        overlay = hashlib.sha1(b'X' + base)
        for changed_path, blob in sorted(((path, git_blob), ('out/digest.txt', companion_blob))):
            overlay.update(changed_path.encode('utf-8') + b'\0' + b'100644:' + blob.encode('ascii'))
        overlay.update(base)
        if overlay.hexdigest() != first_doc['context']['X']:
            raise ValueError('the candidate blobs do not derive the reported synthetic X')
        raw_expected = first_doc['ledger']['raw']['files'][path]['expected_sha256']
        if raw_expected != digest or first_expected != digest or second_expected == digest:
            raise ValueError('the stated and wrong hashes do not form an RC8 pair')
        verdicts = [doc['evaluation']['holds']['RC8'] for doc in (first_doc, second_doc)]
        if verdicts != [first_expected == digest, second_expected == digest]:
            raise ValueError('the tool verdicts disagree with the candidate hash')
        actual.update(agree=True, candidate_sha256=digest, candidate_commit=overlay.hexdigest())
    except ValueError as exc:
        findings.append(('procedural-failed', 'line-patch-rc8: %s' % exc))
    return actual


def eval_procedure(row, ev, findings_out, repo=None):
    if is_line_patch_rc8(row):
        return eval_line_patch_oracle(row, ev, findings_out)
    lib = row['procedure']['lib']
    proc = (ev.man or {}).get('procedure') or {}
    missing = [k for k in LIB_INPUTS[lib] if k not in proc]
    if proc.get('lib') != lib or missing:
        findings_out.append(('raw-evidence-missing', 'procedure %s: inputs %s absent' % (lib, missing)))
        return {}
    actual = {'lib': lib}

    def fail(why):
        findings_out.append(('procedural-failed', '%s: %s' % (lib, why)))

    if lib in ('rel-equal', 'replay', 'hash', 'double-run'):
        runs = proc['runs']
        if not (isinstance(runs, list) and len(runs) >= 2):
            fail('fewer than two runs')
            return actual
        if lib == 'rel-equal':
            ts = [_tuples(ev.json(r)) for r in runs]
            actual['equal'] = all(t == ts[0] for t in ts)
            if not actual['equal']:
                fail('item tuples differ between %s' % runs)
        elif lib == 'double-run':
            bs = [ev.text(r) for r in runs]
            actual['byte_identical'] = None not in bs and all(b == bs[0] for b in bs)
            if not actual['byte_identical']:
                fail('the result files differ')
        elif lib == 'replay':
            docs = [ev.json(r) for r in runs]
            for d in docs:
                if isinstance(d, dict):
                    ((d.get('config') or {}).get('admission') or {}).pop('mode', None)
            actual['equal'] = None not in docs and all(d == docs[0] for d in docs)
            if not actual['equal']:
                fail('the results differ beyond config.admission.mode')
        else:
            hs = [((ev.json(r) or {}).get('engine') or {}).get('blob_sha256') for r in runs]
            actual['hashes'] = hs
            if None in hs or len(set(hs)) != 1:
                fail('engine.blob_sha256 differs or is absent')
    elif lib == 'sweep':
        base = set(_tuples(ev.json(proc['base']), 'FAIL'))
        want = proc.get('new_fail_per_site', 1)
        bad = []
        for site in proc['sites']:
            new_fail = set(_tuples(ev.json(site['result']), 'FAIL')) - base
            if len(new_fail) != want:
                bad.append((site.get('site'), len(new_fail)))
        actual['sites'] = len(proc['sites'])
        actual['bad_sites'] = bad
        if bad:
            fail('sites without exactly %d new FAIL tuple: %s' % (want, bad[:5]))
    elif lib == 'set':
        listing = ev.json(proc['listing']) or []
        got = sorted(ev.json(proc['actual_set']) or [])
        rule = proc.get('rule', {})
        exp = sorted(p for p in listing if any(p == x or p.startswith(x.rstrip('/') + '/')
                                               for x in rule.get('prefixes', [])))
        actual['equal'] = exp == got
        if exp != got:
            fail('expected set differs from the actual set')
    elif lib == 'rtl2':
        drift = ev.json(proc['drift']) or []
        recs = ev.json(proc['records']) or []
        roles = ev.json(proc['roles']) or {}
        uncovered = []
        for path in drift:
            ok = any(r.get('path') == path and r.get('reviewed') is True and r.get('review_lint_passes') is True
                     and all(r.get(k) == roles.get(k) and roles.get(k) for k in ('H', 'M', 'C')) for r in recs)
            if not ok:
                uncovered.append(path)
        # amendment 4 (R6.GATE.16): on a predicted M (roles name the runner's pinned main as M0), every retained run
        # that names a record base records the pinned main as inputs.record_base, and at least one run names it
        base_wrong = []

        def held(rev):
            return bool(repo) and isinstance(rev, str) and HEX40.match(rev) is not None and \
                git_blob_id(repo, rev + '^{commit}') is not None

        def arg(argv, name):
            return argv[argv.index(name) + 1] if name in argv and argv.index(name) + 1 < len(argv) else None

        def predicted(c):
            # a run that names --record-base, or names --main with a commit the repository does not hold while its
            # scientific base is a commit the repository holds (an in-memory M built on the real history), is a run
            # on a predicted M; a wholly synthetic world (its H not held either) is not
            argv = c.get('argv') or []
            if '--record-base' in argv:
                return True
            m, h = arg(argv, '--main'), arg(argv, '--scientific-base')
            return m is not None and isinstance(m, str) and HEX40.match(m) is not None and not held(m) and held(h)
        if roles.get('M0') is None and any(predicted(c) for c in (ev.man or {}).get('cases', [])):
            base_wrong.append('(the roles name no M0, and a retained run is on a predicted M)')
        if roles.get('M0') is not None:
            named = [c for c in (ev.man or {}).get('cases', []) if '--record-base' in (c.get('argv') or [])]
            for c in named:
                res = ev.json(c.get('result_file')) if c.get('result_file') else None
                got = ((res or {}).get('inputs') or {}).get('record_base')
                if got != roles['M0'] or not (isinstance(got, str) and HEX40.match(got)):
                    base_wrong.append(c.get('case'))
            if not named:
                base_wrong.append('(no run names a record base)')
            actual['record_base_matches'] = not base_wrong
        actual['rt_l2'] = 'PASS' if not uncovered and not base_wrong else 'FAIL'
        actual['state'] = 'no drift' if not drift else ('validly reconciled' if not uncovered else 'unresolved')
        if uncovered:
            fail('drifted paths not validly reconciled: %s' % uncovered)
        if base_wrong:
            fail("the record base is not the runner's pinned main, or no M0 is named, in cases %s" % base_wrong)
    elif lib == 'lint':
        findings = ev.json(proc['findings'])
        smap = ev.json(proc['source_map'])
        actual['source_map_nonempty'] = bool(smap)
        actual['findings'] = findings
        if not smap:
            fail('the linted source map is empty')
    else:
        # prerun, consumer, oracle, fixture, ast: attested with checked evidence; every named file must be present
        # and verified, and the runner's value must equal the value read from the attested file.
        for k in LIB_INPUTS[lib]:
            v = proc[k]
            for name in (v if isinstance(v, list) else [v]):
                if isinstance(name, str) and ev.path(name) is None:
                    fail('evidence file %s absent' % name)
        if lib == 'oracle':
            a, b = ev.json(proc['tool_output']), ev.json(proc['oracle_output'])
            actual['agree'] = a == b
            if a != b:
                fail('the tool output differs from the oracle output')
        if lib == 'fixture':
            t = ev.text(proc['landing_check_exit'])
            actual['landing_check_exit'] = t.decode().strip() if t else None
    return actual


# ---------------------------------------------------------------------------------------------------------------
# The verdict

RANK = {'PASS': 0, 'NOT RUN': 1, 'FAIL': 2, 'ERROR': 3}


class Ctx(object):
    """The release-check context: the repository, the commit under check (whose tree holds the release facts), the
    facts directory in that tree, the candidate F and the configuration path."""

    def __init__(self, repo=None, commit=None, freeze=None, config_path=None, facts_dir=FACTS_DIR):
        self.repo = repo
        self.commit = commit
        self.freeze = freeze
        self.config_path = config_path
        self.facts_dir = facts_dir


def reference_differences(row, actuals):
    out = []
    ref = row.get('reference') or {}
    counts = {}
    for a in actuals:
        counts.update(a.get('counts') or {})
    for k, v in ref.items():
        if isinstance(v, (int, float)) and not isinstance(v, bool) and k in counts and counts[k] != v:
            out.append('%s: extracted %r, reference %r' % (k, counts[k], v))
    return out


def evaluate(exp_doc, rows, retired, reqs, records, mutations, ctx):
    """Returns the gate-result document."""
    entries = {}
    file_findings = []

    def entry(rid):
        if rid not in entries:
            entries[rid] = {'id': rid, 'status': None, 'findings': [], 'details': [], 'actual': {},
                            'runner_status': None}
        return entries[rid]

    def add(rid, finding, detail):
        e = entry(rid)
        if finding not in e['findings']:
            e['findings'].append(finding)
        e['details'].append('%s: %s' % (finding, detail))

    for subj, f, d in correspondence(rows, retired, reqs):
        if subj in rows:
            add(subj, f, d)
        else:
            file_findings.append(f)
            entries.setdefault('requirement:' + subj, {'id': 'requirement:' + subj, 'status': 'FAIL', 'findings': [],
                                                        'details': [], 'actual': {}, 'runner_status': None})
            e = entries['requirement:' + subj]
            if f not in e['findings']:
                e['findings'].append(f)
            e['details'].append('%s: %s' % (f, d))
    for subj, f, d in direction_findings(rows):
        add(subj, f, d)
    recs, dup = records
    muts, mdup = mutations
    for subj, f, d in dup + mdup:
        add(subj, f, d)
    for rid in sorted(set(recs) | set(muts)):
        if rid not in rows:
            add(rid, 'unexpected-id', 'recorded but not in the expectation file')
            entry(rid)['status'] = 'FAIL'

    # rows in dependency order: components and dependencies first, release-check dependencies (TR5) first
    order, seen = [], set()

    def visit(rid, stack=()):
        if rid in seen:
            return
        if rid in stack:
            raise FileInvalid('composition or dependency cycle at %s' % rid)
        for c in rows[rid].get('composed_of', []) + rows[rid].get('depends_on', []):
            visit(c, stack + (rid,))
        if rows[rid].get('not_run', {}).get('release_check') == RC_TR5_PASS and 'TR5' in rows:
            visit('TR5', stack + (rid,))
        seen.add(rid)
        order.append(rid)
    for rid in sorted(rows):
        visit(rid)

    status = {}
    for rid in order:
        row = rows[rid]
        e = entry(rid)
        allowed = row.get('status_allowed', ['PASS'])
        own = []
        if row['expect'] is None:
            add(rid, 'expect-null', 'expect is null')
        elif row['expect'].get('outcome') == 'DEFERRED':
            add(rid, 'deferred-expectation', 'expect outcome is DEFERRED')
        rec_status = None
        if rid.startswith('MUT:'):
            if rid not in muts:
                add(rid, 'missing-id', 'no mutation record')
            else:
                m, base = muts[rid]
                rec_status = m['status']
                e['runner_status'] = rec_status
                ev = Evidence(base, m['evidence'], rid)
                if ev.problems:
                    add(rid, 'raw-evidence-missing', '; '.join(ev.problems))
                else:
                    mrecs = ev.json((ev.man.get('procedure') or {}).get('mutant_records'))
                    if not isinstance(mrecs, dict):
                        add(rid, 'raw-evidence-missing', 'the per-control records of the mutant run are absent')
                    else:
                        killed = sorted(k for k, v in mrecs.items() if k in recs and recs[k][1]['status'] != v)
                        e['actual'] = {'killed_by': killed, 'mutated_file': m['mutated_file'], 'rule': m['rule']}
                        if m['status'] == 'KILLED' and sorted(m['killed_by']) != killed:
                            add(rid, 'status-actual-inconsistent', 'killed_by %s, recomputed %s'
                                % (m['killed_by'], killed))
                        if m['status'] == 'SURVIVED' and killed:
                            add(rid, 'status-actual-inconsistent', 'recorded SURVIVED, killed by %s' % killed)
                        if m['status'] == 'NOT APPLIED' and ev.text((ev.man.get('procedure') or {}).get('diff')):
                            add(rid, 'status-actual-inconsistent', 'recorded NOT APPLIED with a non-empty diff')
                    if m['status'] == 'KILLED' and not m['killed_by']:
                        add(rid, 'status-not-allowed', 'KILLED with an empty killed_by')
                if rec_status not in allowed:
                    add(rid, 'status-not-allowed', 'status %s, allowed %s' % (rec_status, allowed))
                elif rec_status != 'KILLED':
                    add(rid, 'limitation-reported', '%s admitted as a named limitation' % rec_status)
            status[rid] = 'FAIL' if set(e['findings']) & FINDING_FAIL else (rec_status or 'FAIL')
            continue
        has_runner = row['runner'] is not None
        if has_runner or not row.get('composed_of'):
            if rid not in recs:
                add(rid, 'missing-id', 'no record')
            else:
                job, rec, base = recs[rid]
                rec_status = rec['status']
                e['runner_status'] = rec_status
                if rec_status == 'NOT RUN':
                    if 'NOT RUN' not in allowed:
                        add(rid, 'status-not-allowed', 'NOT RUN not allowed')
                    elif evaluate_release(ctx, row['not_run']['release_check'], status):
                        add(rid, 'status-not-allowed', 'NOT RUN while its release check holds')
                else:
                    ev = Evidence(base, rec['evidence'], rid)
                    if ev.problems:
                        add(rid, 'raw-evidence-missing', '; '.join(ev.problems))
                    fl = []
                    acts = []
                    if ev.man is not None and row['expect'] is not None and row['expect'].get('outcome') != 'DEFERRED':
                        ex = row['expect']
                        if 'cases' in ex:
                            for c in ex['cases']:
                                names = c['case'] if isinstance(c['case'], list) else [c['case']]
                                for n in names:
                                    acts.append(eval_case(c, n, ev, row, rec, fl))
                        elif ex.get('outcome') != 'COMPOSITE':
                            acts.append(eval_case(ex, '', ev, row, rec, fl))
                        if row.get('restored') is not None and row['restored'].get('outcome') != 'COMPOSITE':
                            acts.append(eval_case(row['restored'], 'restored', ev, row, rec, fl))
                        if row.get('procedure'):
                            acts.append(eval_procedure(row, ev, fl, ctx.repo))
                        if ev.problems:
                            fl.append(('raw-evidence-missing', '; '.join(sorted(set(ev.problems)))))
                    for f, d in fl:
                        add(rid, f, d)
                    e['actual'] = acts
                    for d in reference_differences(row, acts):
                        add(rid, 'reference-difference', d)
                    gate_holds = not (set(e['findings']) & FINDING_FAIL)
                    if rec_status == 'FAIL' and gate_holds:
                        add(rid, 'status-actual-inconsistent', 'runner FAIL, the evidence meets expect')
                    if rec_status == 'PASS' and not gate_holds:
                        add(rid, 'status-actual-inconsistent', 'runner PASS, the gate does not hold')
                    if rec_status == 'FAIL' and 'FAIL' not in allowed:
                        add(rid, 'status-not-allowed', 'FAIL not allowed')
                    for dep in row.get('depends_on', []):
                        if status.get(dep) != 'PASS':
                            add(rid, 'status-not-allowed', 'PASS while dependency %s is %s' % (dep, status.get(dep)))
        own = rec_status
        if row.get('composed_of'):
            comps = [(c, status.get(c, 'FAIL'), list(entries.get(c, {}).get('findings', []))) for c in row['composed_of']]
            e['components'] = [{'id': c, 'status': cs, 'findings': cf} for c, cs, cf in comps]
            for c, cs, cf in comps:
                if 'missing-id' in cf:
                    add(rid, 'missing-id', 'component %s has no record' % c)
            own_part = []
            if has_runner:
                own_failed = own is None or own == 'FAIL' or bool(set(e['findings']) & FINDING_FAIL)
                own_part = ['FAIL' if own_failed else own]
            agg = max([cs for _, cs, _ in comps] + own_part, key=lambda x: RANK.get(x, 3))
            e['composite_status'] = agg
            if own_part == ['PASS'] and any(cs in ('FAIL', 'ERROR') for _, cs, _ in comps):
                add(rid, 'procedural-failed', 'its own record holds while a component does not')
            if agg in ('FAIL', 'ERROR'):
                add(rid, 'status-not-allowed', 'composite aggregate %s' % agg)
            elif agg == 'NOT RUN':
                if 'NOT RUN' not in allowed:
                    add(rid, 'status-not-allowed', 'composite NOT RUN not allowed')
                elif evaluate_release(ctx, row['not_run']['release_check'], status):
                    add(rid, 'status-not-allowed', 'composite NOT RUN while its release check holds')
            status[rid] = 'FAIL' if set(e['findings']) & FINDING_FAIL else agg
            e['status'] = status[rid]
            if e['status'] == 'FAIL':
                e['composite_status'] = 'FAIL' if agg != 'ERROR' else agg
            continue
        if set(e['findings']) & FINDING_FAIL:
            status[rid] = 'FAIL'
        else:
            status[rid] = own if own in ('PASS', 'NOT RUN') else 'FAIL'
        e['status'] = status[rid]

    for rid, e in entries.items():
        if e['status'] is None:
            e['status'] = status.get(rid, 'FAIL')
    allf = sorted({f for e in entries.values() for f in e['findings']} | set(file_findings))
    holds = not (set(allf) & FINDING_FAIL)
    counts = {}
    for rid in rows:
        s = entries[rid]['status']
        counts[s] = counts.get(s, 0) + 1
    return {
        'schema': SCHEMA_GATE,
        'expectation_record_id': exp_doc['record_id'],
        'verdict': 'GATE_HOLDS' if holds else 'GATE_FAIL',
        'status_counts': counts,
        'met': counts.get('PASS', 0) + counts.get('KILLED', 0),
        'findings': allf,
        'file_findings': sorted(set(file_findings)),
        'compound_invariants': sorted(set(COMPOUND)),
        'rows': [entries[k] for k in sorted(entries)],
    }


def run_gate(exp_path, req_path, record_paths, mut_path, ctx, exp_doc=None, req_doc=None):
    """Returns (exit code, gate-result document)."""
    try:
        exp, rows, retired = load_expectations(exp_path, exp_doc)
        reqs = load_requirements(req_path, req_doc)
        records = load_records(record_paths)
        mutations = load_mutation_records(mut_path)
        res = evaluate(exp, rows, retired, reqs, records, mutations, ctx)
    except FileInvalid as exc:
        return GATE_EXIT['GATE_ERROR'], {'schema': SCHEMA_GATE, 'verdict': 'GATE_ERROR', 'findings': ['file-invalid'],
                                         'file_findings': ['file-invalid'], 'error': str(exc), 'rows': []}
    return GATE_EXIT[res['verdict']], res


def write_json(path, doc):
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    with open(path, 'w') as f:
        json.dump(doc, f, indent=1, sort_keys=True)
        f.write('\n')


def main(argv=None):
    ap = argparse.ArgumentParser(prog='control_gate.py', description=__doc__.split('\n\n')[0])
    ap.add_argument('--self-test', action='store_true', help='run GATE-1 to GATE-30 only')
    ap.add_argument('--expectations')
    ap.add_argument('--requirements')
    ap.add_argument('--records', action='append', default=[], help='a control-records.json (repeatable)')
    ap.add_argument('--mutation-records')
    ap.add_argument('--repo', help='repository whose git objects the release checks read')
    ap.add_argument('--commit', help='the commit under check (default: the repository HEAD); its tree holds the '
                    'release facts')
    ap.add_argument('--facts-dir', default=FACTS_DIR, help='the release facts directory in that tree')
    ap.add_argument('--freeze', help='candidate F, a full commit id (TR5 release check)')
    ap.add_argument('--config', help='configuration path in F (TR5 release check)')
    ap.add_argument('--out', required=True)
    try:
        a = ap.parse_args(argv)
    except SystemExit as exc:
        return USAGE_EXIT if exc.code else 0
    if os.path.exists(a.out) and os.listdir(a.out):
        sys.stderr.write(json.dumps({'outcome': 'USAGE', 'reason': '--out exists and is not empty'}) + '\n')
        return USAGE_EXIT
    os.makedirs(a.out, exist_ok=True)
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        'gate_selftest', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'gate_selftest.py'))
    gate_selftest = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(gate_selftest)
    st_ok, st_dir = gate_selftest.run(os.path.join(a.out, 'self-test'))
    if not st_ok:
        write_json(os.path.join(a.out, 'gate-result.json'), {'schema': SCHEMA_GATE, 'verdict': 'VOID',
                                                             'reason': 'gate self-test failed'})
        return VOID_EXIT
    if a.self_test:
        return 0
    if not (a.expectations and a.requirements):
        sys.stderr.write(json.dumps({'outcome': 'USAGE', 'reason': '--expectations and --requirements required'}) + '\n')
        return USAGE_EXIT
    recs = list(a.records) + [os.path.join(st_dir, 'control-records.json')]
    commit = None
    if a.repo:
        commit = git_blob_id(a.repo, (a.commit or 'HEAD') + '^{commit}')
        if commit is None:
            sys.stderr.write(json.dumps({'outcome': 'USAGE', 'reason': 'the commit under check does not resolve'})
                             + '\n')
            return USAGE_EXIT
    code, res = run_gate(a.expectations, a.requirements, recs, a.mutation_records,
                         Ctx(a.repo, commit, a.freeze, a.config, a.facts_dir))
    res['commit_under_check'] = commit
    write_json(os.path.join(a.out, 'gate-result.json'), res)
    return code


if __name__ == '__main__':
    sys.exit(main())
