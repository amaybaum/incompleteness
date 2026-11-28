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
import functools
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
# r6 amendment 9 (owner-approved; rows that read the configuration's rule records gate plan freeze F, OBL-3)
RC_RULES = 'the configuration at the commit under check references reviewed rule records (OBL-3)'
RC_REP_BUILD = 'the subject under check is the exact candidate F assessed by OBL-16(a)'
RELEASE_CHECKS = frozenset([RC_FALSE, RC_TR5_PASS, RC_EI14, RC_RTL2, RC_RTT, RC_TR5, RC_RULES, RC_REP_BUILD])
F_REQUIRED_ROWS = frozenset(['REP-BUILD', 'RT-T', 'TR5', 'S11-2', 'S11-2a', 'S11-2b', 'S11-2c'])
RETIREMENT_DRIFT_ROWS = frozenset(('RT-L2', 'RT-O9-L2'))
# amendment 8, M8-3 and M8-4 (R6.GATE.15): a row outside the A1 path admits NOT RUN with this reason and RC_FALSE;
# where no runner records it, the gate records it NOT RUN
A8_REASON = 'outside the A1 path (amendment 8)'


# Release facts are read from git objects at the commit under check (--commit), never from a local directory: the
# file `<facts_dir>/<row id>.json` in that commit's tree names the objects the fact rests on, and each evaluator
# checks those objects itself. An absent file is a fact not established (the check is false).
FACTS_DIR = 'verification/audits/foundations/ledger-coverage-tool-20261123/release'
AUDIT_DIR = 'verification/audits/foundations/ledger-coverage-tool-20261123/'
WORKFLOW_PATH = '.github/workflows/ledger-coverage.yml'
# R6.PLACE.8 with amendment 8, M8-11: the tool's landing paths
LANDING_PREFIXES = ('tools/', AUDIT_DIR, 'verification/audits/foundations/a1exit-staging-amendment-20261126/',
                    'verification/audits/foundations/a1exit-adjudication-design-20261126/')
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


_IDENTITY = re.compile(r'[A-Za-z0-9][A-Za-z0-9._:-]{0,127}\Z')
_KEY_DROP = str.maketrans('', '', '._:-')


def _identity_ok(v):
    """Staging S-2 S2.1: an identity string matches [A-Za-z0-9][A-Za-z0-9._:-]{0,127} as a whole and is not made
    only of digits."""
    return isinstance(v, str) and v.isascii() and _IDENTITY.match(v) is not None and not v.isdigit()


def _identity_key(v):
    """S2.2: ASCII letters made lowercase and `.`, `_`, `:` and `-` removed."""
    return v.lower().translate(_KEY_DROP)


def _independent_of_author(rev, author):
    """S2.5 lint and S2.4 with X = {author}: the author and the reviewer identity strings; the declaration
    {not_author: true, depends_on: identity strings, no two the same identity}; neither the reviewer nor any
    depends_on element the same identity (S2.2) as the author."""
    who, ind = rev.get('reviewer'), rev.get('independence')
    deps = ind.get('depends_on') if isinstance(ind, dict) else None
    if not (_identity_ok(author) and _identity_ok(who) and isinstance(ind, dict) and
            set(ind) == {'not_author', 'depends_on'} and ind['not_author'] is True and isinstance(deps, list) and
            all(_identity_ok(d) for d in deps) and len({_identity_key(d) for d in deps}) == len(deps)):
        return False
    return all(_identity_key(x) != _identity_key(author) for x in [who] + deps)


def rtl2_release(ctx, name='RT-L2'):
    """Reconciliation evidence from outside the tool's landing paths, with an independent, accepting review.

    Under Amendment 10 the review names REV's single parent (M, or the pinned M0 for a predicted M). The record
    and review are both read from REV, and per-path blob ids must match the run's H, M and C.
    """
    f = _release_fact(ctx, name)
    if not f:
        return False
    roles = f.get('roles') or {}
    if not isinstance(roles, dict) or not all(isinstance(roles.get(k), str) and HEX40.fullmatch(roles[k])
                                               for k in ('H', 'M', 'C')):
        return False
    ref = f.get('record') or {}
    path = ref.get('path') if isinstance(ref, dict) else None
    if not isinstance(path, str) or path.startswith(LANDING_PREFIXES) or path == WORKFLOW_PATH:
        return False
    review_ref = f.get('review')
    if not isinstance(review_ref, dict) or review_ref.get('commit') != ref.get('commit'):
        return False
    rb, rec = _json_blob(ctx.repo, ref)
    _, rev = _json_blob(ctx.repo, review_ref)
    if not (isinstance(rec, dict) and rec.get('schema') == 'oi-reconciliation/2' and isinstance(rev, dict)):
        return False
    if any(rec.get(field) != roles[role] for field, role in (('ledger_base', 'H'), ('M', 'M'), ('X', 'C'))):
        return False
    record_base = roles.get('M0', roles['M'])
    if not isinstance(record_base, str) or not HEX40.fullmatch(record_base) or rev.get('revision') != record_base:
        return False
    if 'M0' in roles and record_base == roles['M']:
        return False
    record_commit = ref['commit']
    parents = subprocess.run(['git', '--no-replace-objects', '-C', ctx.repo, 'cat-file', 'commit', record_commit],
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if parents.returncode != 0 or [line for line in parents.stdout.split(b'\n\n', 1)[0].splitlines()
                                   if line.startswith(b'parent ')] != [b'parent ' + record_base.encode('ascii')]:
        return False
    review_path = review_ref['path']
    if os.path.dirname(review_path) != os.path.dirname(path):
        return False
    for file in (path, review_path):
        entry = git_entry(ctx.repo, record_commit, file)
        if entry is None or entry[0] not in ('100644', '100755'):
            return False
    reviewed = rev.get('reviewed') or {}
    verdicts = rev.get('verdicts') or []
    if not (rev.get('schema') == 'oi-review-record/1' and isinstance(reviewed, dict) and reviewed.get('path') == path
            and reviewed.get('blob_sha256') == hashlib.sha256(rb).hexdigest()
            and _independent_of_author(rev, rec.get('author'))
            and verdicts and all(isinstance(v, dict) and v.get('verdict') == 'accept' for v in verdicts)):
        return False
    entries = rec.get('paths') or []
    if not entries:
        return False
    # R6.RECON.2(c)(4) excludes changes to covered ledgered and corpus paths between M0 and a predicted M.
    # The release check can match their m pins at M0 even when the predicted commit exists only in the runner.
    compare_main = roles['M']
    if 'M0' in roles and git_blob_id(ctx.repo, roles['M'] + '^{commit}') is None:
        compare_main = record_base
    for e in entries:
        if not isinstance(e, dict) or not isinstance(e.get('path'), str):
            return False
        for field, commit in (('m', compare_main), ('x', roles['C'])):
            blob = git_blob_id(ctx.repo, '%s:%s' % (commit, e['path']))
            if blob is None or blob != e.get(field):
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


def rule_records_reviewed(cfg, read):
    """RC_RULES: the configuration lists at least one rule record, and each, its bytes hashing to the pinned
    sha256, is reviewed by an accepting review record listed among the configuration's `records` that names exactly
    that blob. `read(path)` returns the bytes of a path in the tree the configuration is read from, or None."""
    if not isinstance(cfg, dict):
        return False
    rules = [r for r in (cfg.get('rules') or []) if isinstance(r, dict)]
    if not rules:
        return False
    reviews = []
    for r in (cfg.get('records') or []):
        if isinstance(r, dict) and r.get('kind') == 'review':
            b = read(r.get('path'))
            try:
                rv = json.loads(b.decode('utf-8')) if b is not None else None
            except ValueError:
                rv = None
            if isinstance(rv, dict) and rv.get('schema') == 'oi-review-record/1':
                reviews.append(rv)
    for r in rules:
        b = read(r.get('path'))
        if b is None or hashlib.sha256(b).hexdigest() != r.get('blob_sha256'):
            return False
        if not any((rv.get('reviewed') or {}).get('path') == r.get('path') and
                   (rv.get('reviewed') or {}).get('blob_sha256') == r.get('blob_sha256') and rv.get('verdicts') and
                   all(isinstance(v, dict) and v.get('verdict') == 'accept' for v in rv['verdicts'])
                   for rv in reviews):
            return False
    return True


def rules_release(ctx):
    """RC_RULES at the commit under check, the configuration given by --config."""
    if not (ctx.repo and ctx.commit and ctx.config_path):
        return False
    data = git_show(ctx.repo, '%s:%s' % (ctx.commit, ctx.config_path))
    try:
        cfg = json.loads(data.decode('utf-8')) if data is not None else None
    except ValueError:
        cfg = None
    return rule_records_reviewed(cfg, lambda p: git_show(ctx.repo, '%s:%s' % (ctx.commit, p))
                                 if isinstance(p, str) else None)


def git_show(repo, rev_path):
    r = subprocess.run(['git', '--no-replace-objects', '-C', repo, 'cat-file', 'blob', rev_path],
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return r.stdout if r.returncode == 0 else None


def tr5_release(ctx):
    """True iff the configuration at the candidate F (--freeze) is listed, as a pin row naming its file, in the last
    Record pins subsection (the heading `### N.N Record pins` of DESIGN-r6 sec. 6.3, R6.REC.16; `last_pin_rows`) of the
    PREREG.md in the configuration's directory at F. Evaluated from git objects."""
    if not (ctx.repo and ctx.freeze and ctx.config_path):
        return False
    if not re.fullmatch('[0-9a-f]{40}', ctx.freeze):
        return False
    d = ctx.config_path.rsplit('/', 1)[0] if '/' in ctx.config_path else ''
    prereg = git_show(ctx.repo, '%s:%s' % (ctx.freeze, (d + '/' if d else '') + 'PREREG.md'))
    if prereg is None or git_show(ctx.repo, '%s:%s' % (ctx.freeze, ctx.config_path)) is None:
        return False
    name = ctx.config_path.rsplit('/', 1)[-1]
    rows = last_pin_rows(prereg)
    return rows is not None and any(f == name for f, _ in rows)


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
    if text == RC_RULES:
        return rules_release(ctx)
    if text == RC_REP_BUILD:
        return assessment_subject(ctx)['phase'] == 'candidate-F'
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
    """A `$name` is replaced by its binding wherever it appears in an expectation value: the value itself, or any
    member of a list or value of an object nested in it (R6.GATE.3 does not restrict where a `$name` may appear)."""
    if isinstance(v, str) and v.startswith('$'):
        if v[1:] not in bindings:
            raise Unbound(v)
        return bindings[v[1:]]
    if isinstance(v, list):
        return [_bind(x, bindings) for x in v]
    if isinstance(v, dict):
        return {k: _bind(x, bindings) for k, x in v.items()}
    return v


def _field(obj, k):
    if k == 'file':
        return obj.get('file', obj.get('subject'))
    if k == 'path':
        return obj.get('path', obj.get('file', obj.get('subject')))
    return obj.get(k)


def _has(obj, k, v):
    """One field condition of an item pattern: `<field>_include` tests membership in the item's list field (for
    example `alternatives_include`), `profile` also matches a member of the item's `profiles`. A delegated finding
    can name its class or the supplied file, and an item's explanation can be carried in `why`."""
    if k.endswith('_include') and k[:-len('_include')] in obj:
        got = obj.get(k[:-len('_include')])
        return v in got if isinstance(got, list) else got == v
    if k == 'profile' and 'profile' not in obj and isinstance(obj.get('profiles'), list):
        return v in obj['profiles']
    if k == 'reason':
        return obj.get('reason', obj.get('why')) == v
    if k == 'subject' and isinstance(v, str) and obj.get('obligation') == 'DELEGATED':
        return obj.get('subject') == v or obj.get('delegated_class') == v or (
            obj.get('tree') == 'supplied' and obj.get('file') == v)
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


def _site_lines(site):
    current = site.get('current')
    lines = current.get('lines') if isinstance(current, dict) else None
    if isinstance(lines, list) and len(lines) == 2 and all(type(n) is int for n in lines) and 0 < lines[0] <= lines[1]:
        return lines
    return None


def _site_at_eof(site, splice):
    """Check the retained no-LF fixture bytes and the reported replacement of its final line."""
    lines = _site_lines(site)
    if not (lines and isinstance(splice, dict) and splice.get('path') == site['current'].get('file') and
            all(isinstance(splice.get(k), str) for k in ('before', 'after', 'new'))):
        return False
    before, after, new = (splice[k].encode('utf-8') for k in ('before', 'after', 'new'))
    start, end = splice.get('start'), splice.get('end')
    if not (before and after and not before.endswith(b'\n') and not after.endswith(b'\n') and
            type(start) is int and type(end) is int and before.rfind(b'\n') < start < end == len(before) and
            b'\n' not in new and before[:start] + new == after and before != after):
        return False
    last = after.count(b'\n') + 1
    digest = hashlib.sha256(after.rsplit(b'\n', 1)[-1]).hexdigest()
    return (lines == [last, last] and site.get('state') == 'authorized-replacement' and
            site['current'].get('sha256') == site.get('new_region_sha256') == digest)


def _site_matches(obj, k, v, result, bindings):
    """Read the declared observations from the result's site, item or hit fields."""
    if k in ('located', 'line_range') and type(v) is bool:
        return bool(_site_lines(obj)) == v
    if k == 'span_end' and v == 'EOF':
        return _site_at_eof(obj, result.get('eof_splice'))
    if k in ('via', 'search_agrees'):
        trace = obj.get('translation_check')
        if not isinstance(trace, dict):
            return False
        if k == 'via':
            return v == 'translation'
        line = trace.get('translated_line')
        return v is True and type(line) is int and type(trace.get('searched_line')) is int and (
            line == trace['searched_line'] and _site_lines(obj) == [line, line])
    if k == 'region_shared_with' and isinstance(v, list):
        group = obj.get(k)
        return isinstance(group, dict) and group.get('with') == v
    if k == 'state' and v == 'as classified':
        ref = _bind('$record', bindings)
        return (isinstance(ref, dict) and set(ref) == {'path', 'blob_sha256'} and
                isinstance(ref['path'], str) and bool(ref['path']) and
                isinstance(ref['blob_sha256'], str) and re.fullmatch(r'[0-9a-f]{64}', ref['blob_sha256']) and
                obj.get('state') == 'PASS' and obj.get('classified_by') == ref)
    if k == 'names_class' and v is True:
        cls = _bind('$class_id', bindings)
        return isinstance(cls, str) and bool(cls) and obj.get('why') == 'the blob at M differs from the pin of class ' + cls
    return _has(obj, k, v) if k == 'reason' else obj.get(k) == v


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
    frozen_message = k == 'message_names' and v == 'the exception class and the failing stage'
    frozen_main = k == 'none' and v == 'calls of the frozen main()'
    if (frozen_message or frozen_main) and result.get('operation') == 'record' and result.get('outcome') == 'INTERNAL':
        stop = result.get('stop') or {}
        detail = stop.get('detail') if isinstance(stop, dict) else None
        if not isinstance(detail, dict):
            return False, None, 'result'
        stage, cls, message = (detail.get(f) for f in ('stage', 'class', 'message'))
        if frozen_message:
            expected = '%s raised %s: %s' % (stage, cls, message)
            holds = all(isinstance(f, str) for f in (stage, cls, message)) and bool(stage and cls)
            return holds and stop.get('message') == expected, stop.get('message'), 'result'
        calls = detail.get('calls')
        holds = isinstance(calls, list) and all(isinstance(c, str) and c not in ('main', 'main()') for c in calls)
        return holds and isinstance(stage, str) and stage not in ('main', 'main()'), calls, 'result'
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
    if k == 'record_checks_failed_include' and v == 'pin_findings':
        pin_findings = (result.get('record_checks') or {}).get('pin_findings')
        return isinstance(pin_findings, list) and bool(pin_findings), pin_findings, 'result'
    if k == 'record_checks_failed_include' and isinstance((result.get('record_checks') or {}).get('ck_errors'), list):
        # op A: the frozen checks that failed, the identifier that leads each entry of record_checks.ck_errors
        a = sorted({str(e).split()[0] for e in result['record_checks']['ck_errors'] if str(e).split()})
        return v in a, a, 'result'
    if k == 'per_failed_check':
        checks = result.get('record_checks')
        if result.get('operation') != 'record' or not isinstance(checks, dict) or checks.get('holds') is not False:
            return False, None, 'result'
        eq = checks.get('equalities')
        if not (isinstance(eq, list) and all(isinstance(e, dict) and isinstance(e.get('name'), str) and e['name']
                                            and type(e.get('equal')) is bool for e in eq) and
                isinstance(checks.get('errors'), list) and isinstance(checks.get('pin_findings'), list) and
                type(checks.get('frozen_self_test')) is bool):
            return False, None, 'result'
        if len({e['name'] for e in eq}) != len(eq):
            return False, None, 'result'
        failed = {e['name'] for e in eq if not e['equal']}
        failed.update(name for name, bad in (('equalities', len(eq) != 5), ('errors', checks['errors']),
                                             ('frozen_self_test', not checks['frozen_self_test']),
                                             ('pin_findings', checks['pin_findings'])) if bad)
        named = {i['subject'] for i in result.get('items', []) if isinstance(i, dict) and
                 i.get('obligation') == 'RECORD' and i.get('class') == 'record-invalid' and
                 i.get('decision') == 'FAIL' and isinstance(i.get('subject'), str)}
        missing = failed - named
        return bool(failed) and not missing, {'failed': sorted(failed), 'missing': sorted(missing)}, 'result'
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


def _side_changes(result):
    scan = (result or {}).get('side_changes')
    if isinstance(scan, list) and all(isinstance(s, dict) and isinstance(s.get('path'), str) for s in scan):
        return scan
    return None


def _tt2_comparison_paths(result):
    """Derive the reported paths from the two retained TT2 tree maps and check the observed diff."""
    if not isinstance(result, dict) or result.get('operation') != 'direct tree comparison':
        return None
    roles = [result.get(k) for k in ('scientific_base', 'main', 'candidate')]
    if not all(isinstance(rev, str) and HEX40.fullmatch(rev) for rev in roles):
        return None
    trees = result.get('tree_entries')
    if not isinstance(trees, dict) or set(trees) != {'m', 'x'}:
        return None
    mp, xp = trees['m'], trees['x']
    for tree in (mp, xp):
        if not isinstance(tree, dict) or not all(isinstance(path, str) and path and isinstance(blob, str)
                                                and HEX40.fullmatch(blob) for path, blob in tree.items()):
            return None
    ledgered = result.get('ledgered_paths')
    if not isinstance(ledgered, list) or not all(isinstance(p, str) and p and p in xp for p in ledgered) or \
            len(ledgered) != len(set(ledgered)):
        return None
    changed = [{'path': p, 'm': mp.get(p), 'x': xp.get(p)}
               for p in sorted((mp.keys() | xp.keys()) - set(ledgered)) if mp.get(p) != xp.get(p)]
    return [entry['path'] for entry in changed] if result.get('unledgered_changes') == changed else None


def _tt7_landing_roles(result):
    """Validate the retained landing's role and blob identities before comparing the TT7 cases."""
    if not isinstance(result, dict) or result.get('operation') != 'execution':
        return None
    keys = ('scientific_base', 'main', 'candidate', 'landing', 'candidate_blob', 'landing_blob')
    roles = {key: result.get(key) for key in keys}
    if not all(isinstance(value, str) and HEX40.fullmatch(value) for value in roles.values()):
        return None
    if roles['candidate'] in (roles['scientific_base'], roles['main']) or \
            roles['landing'] in (roles['scientific_base'], roles['main'], roles['candidate']):
        return None
    return roles if result.get('landing_parents') == [roles['main'], roles['candidate']] else None


def _tt7_landing_blobs(result, roles, bindings):
    comps = result.get('landing_compositions') if roles else None
    if not (isinstance(comps, list) and len(comps) == 1 and isinstance(comps[0], dict)):
        return None
    record = comps[0]
    computed = record.get('composed_blob')
    landed = roles['landing_blob']
    if not isinstance(computed, str) or not HEX40.fullmatch(computed) or record.get('l') != landed:
        return None
    if not bindings.get('ledgered') or record.get('path') != bindings['ledgered']:
        return None
    return {'composed_blob': computed, 'L_blob': landed}


def _bootstrap_refusals_hold(trace):
    try:
        probes = trace['bootstrap_refusals']
        ordinary = ['-S', '-B']
        isolated = ['-I', '-S', '-B']
        cases = {
            'ordinary bootstrap': (ordinary, True),
            'safe-path bootstrap': (ordinary + ['-E', '-s', '-P'], False),
            'checkout entry': (isolated, True),
            'link into checkout': (isolated, True),
            'link out of checkout': (isolated, True),
        }
        if set(probes) != cases.keys():
            return False
        checkout = probes['checkout entry']['checkout'].rstrip('/')
        ordinary_root = probes['ordinary bootstrap']['checkout'].rstrip('/')
        into = probes['link into checkout']['injected']
        external = into.rsplit('/', 1)[0]
        if (not checkout.startswith('/') or not ordinary_root.startswith('/') or
                checkout == ordinary_root or not external.startswith('/') or
                external == checkout or external.startswith(checkout + '/')):
            return False
        direct = checkout + '/tools'
        operands = {
            'ordinary bootstrap': (ordinary_root, ordinary_root + '/tools', ordinary_root + '/tools', None),
            'safe-path bootstrap': (ordinary_root, None, None, None),
            'checkout entry': (checkout, direct, direct, None),
            'link into checkout': (checkout, external + '/checkout', direct, direct),
            'link out of checkout': (checkout, direct + '/external', external, external),
        }
        for subject, (flags, injected) in cases.items():
            p = probes[subject]
            imports = p['imports']
            stderr = p['stderr']
            result = json.loads(stderr)
            if (tuple(p[k] for k in ('checkout', 'injected', 'resolved', 'link_target')) != operands[subject] or
                    (injected and imports['path_at_entry'][0] != p['injected']) or
                    p['flags'] != flags or p['exit'] != 65 or
                    p['result_written'] is not False or len(stderr.splitlines()) != 1 or
                    result['schema'] != 'oi-ledger-coverage/5' or result['outcome'] != 'ERROR' or
                    result['exit_status'] != 65 or result['stop']['class'] != 'NOT_ISOLATED' or
                    'sys' not in imports['startup'] or imports['added'] != [] or
                    not set(imports['requested']) <= set(imports['startup'])):
                return False
        return True
    except (AttributeError, IndexError, TypeError, KeyError, ValueError):
        return False


def eval_invariant(k, v, result, case, attested, bindings, declared_sites=()):
    """Returns (holds, actual, source). Keys the gate can compute from the retained result are computed; any
    other key must be attested in the case's sha256-checked attested file, equal to the expectation."""
    if k == 'old_style_X_vs_M_comparison_reports':
        got = _tt2_comparison_paths(result)
        if got is None:
            return False, None, 'unattested'
        path = _bind(v, bindings)
        return got == [path] and (k not in attested or attested[k] == v), got, 'result'
    if isinstance(result, dict) and result.get('schema') == SCHEMA_GATE:
        comps = [r for r in result.get('rows', []) if 'components' in r]
        if k == 'composite_status':
            a = [r.get('composite_status') for r in comps]
            return a == [v], a, 'gate result'
        if k == 'component_results_preserved':
            a = bool(comps) and all(all({'id', 'status', 'findings'} <= set(c) for c in r['components'])
                                    for r in comps)
            return a == v, a, 'gate result'
    if k in ('not_in_H_to_M_scan', 'class_route_entry_stands'):
        scan = _side_changes(result)
        if scan is None:
            return False, None, 'unattested'
        if k == 'not_in_H_to_M_scan':
            path = _bind(v, bindings)
            absent = not any(s['path'] == path for s in scan)
            return isinstance(path, str) and bool(path) and absent, path if absent else None, 'result'
        path, cls = _bind('$path', bindings), _bind('$class_id', bindings)
        entries = [s for s in scan if s['path'] == path]
        findings = [i for i in result.get('items') or [] if _names(i, path)]
        actual = (isinstance(cls, str) and bool(cls) and len(entries) == 1 and entries[0].get('class') == cls
                  and entries[0].get('why') is None and
                  any(i.get('class') == 'side-change-unclassified' and _has(i, 'reason', 'differs from F')
                      for i in findings))
        return actual == v, actual, 'result'
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
            classes = {i.get('class') for i in result.get('items') or []}
            vals = v if isinstance(v, list) else [v]
            if 'record-directory' in vals:
                scan = _side_changes(result)
                paths = [_bind(site['subject'], bindings) for site in declared_sites if 'subject' in site]
                if scan is None or not paths or any(not isinstance(p, str) or not p for p in paths):
                    return False, None, 'unattested'
                paths = set(paths)
                entries = [entry for entry in scan if entry['path'] in paths]
                # R6.RDIR.1 and R6.RDIR.10: verify each named addition's scan entry.
                # Other paths in the same record directory may legitimately have the reserved class.
                if (len(entries) != len(paths) or {entry['path'] for entry in entries} != paths or
                        any('class' not in entry or
                            (entry['class'] is not None and not isinstance(entry['class'], str))
                            for entry in entries)):
                    return False, None, 'unattested'
                if any(entry['class'] == 'record-directory' for entry in entries):
                    classes.add('record-directory')
            return not (set(vals) & classes), sorted(classes), 'result'
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


# S11-2a supplement (A1 staging amendment r2, adopted at 6de7efa4): the admitted A1 record directory of R6.A1CFG.1,
# held as a constant of the gate (it imports nothing from the tool; a change to R6.A1CFG.1's tuple needs the same change
# here), and the stand-in subject of a1_controls.simulated_freeze restated (a tool revision of simulated_freeze or
# Overlay.derive must change this restatement with it)
S11_A1_DIRECTORY = 'verification/audits/foundations/a1exit-deletion-20261121'
S11_STANDIN_SUBJECT = 'stand-in for F: the staged configuration in the plan record directory'
S11_P_ORACLE_COMMIT = '4c79be642ca631573f06b444903be75ec4f5e2b6'
S11_P_ORACLE_ROWS = {'S11-57a', 'S11-57b', 'S11-57c', 'S11-57d', 'S11-58a-f',
                     'S11-58g', 'S11-58h', 'S11-58i', 'S11-58j', 'S11-58k'}
_RECORD_PINS = re.compile(r'^### \d+\.\d+ Record pins\b')
_PIN_ROW = re.compile(r'^\|\s*`([^`]+)`\s*\|\s*`([^`]*)`\s*\|\s*$')


def last_pin_rows(prereg):
    """The pin rows (file, value) of the last Record pins subsection of a PREREG.md: the last line matching
    `### N.N Record pins` (DESIGN-r6 sec. 6.3, R6.REC.16, as the tool's config.read_pin_table reads it), up to the
    next line beginning with `#`. None when there is no such subsection. Shared by tr5_release and s11_binding."""
    if prereg is None:
        return None
    lines = prereg.decode('utf-8', 'replace').splitlines()
    starts = [i for i, ln in enumerate(lines) if _RECORD_PINS.match(ln)]
    if not starts:
        return None
    rows = []
    for ln in lines[starts[-1] + 1:]:
        if ln.startswith('#'):
            break
        m = _PIN_ROW.match(ln.strip())
        if m:
            rows.append((m.group(1), m.group(2)))
    return rows


def git_entry(repo, commit, path):
    """(mode, object id) of the tree entry at `path` in `commit`, or None; read from git objects."""
    r = subprocess.run(['git', '--no-replace-objects', '-C', repo, 'ls-tree', '-z', commit, '--', path],
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if r.returncode != 0:
        raise FileInvalid('the tree of %s cannot be read' % commit)
    for ent in r.stdout.split(b'\0'):
        if not ent:
            continue
        meta, _, name = ent.partition(b'\t')
        parts = meta.split()
        if name.decode('utf-8', 'replace') == path and len(parts) == 3:
            return parts[0].decode(), parts[2].decode()
    return None


REGULAR_MODES = ('100644', '100755')
REP_LEDGER = AUDIT_DIR + 'rep/ledger.json'
REP_EDITS = AUDIT_DIR + 'rep/edits.json'
REP_TEMPLATE = AUDIT_DIR + 'rep/control-instance.json'
REP_BUILDER = 'tools/ledger_coverage/adapters/rep_build.py'
REP_LEDGER_GIT = 'ba37c1cdb560cb5fceeeb2b46a3091c832b4a80e'
REP_EDITS_GIT = 'ec384fdfbc12937b860e2f226355e8c5d94820a5'
REP_E = 'e837e3dbaa605efc867a213f3345cee14c36d8f5'
REP_SUBJECT = 'X_rep: the representative retirement candidate of design r6 R6.EVID.8'
REP_MARKER = b'X_rep delegated-path marker (design r6 R6.EVID.8): %s\n'
REP_CASES = (
    'build X_rep from H, the pinned ledger and edit list, and the configuration\'s control instance',
    "the pinned ledger with one splice's new bytes changed by one byte",
    'a builder that imports a module under tools/ledger_coverage/engine/',
)
REP_INVOCATIONS = (
    'X_rep build (a1_controls.py rep_build_control)',
    'X_rep build with a mutated ledger (a1_controls.py rep_build_control)',
    'X_rep builder importing the engine (a1_controls.py rep_build_control)',
)
REP_HASH_REASON = "a ledgered path's sha256 differs from the ledger's expected_sha256"
REP_IMPORT_REASON = 'the builder imports from the engine under test'
REP_DESCRIPTOR = 'a1-staging-transition.json'
REP_PRIOR = 'a1-staging-prior.json'
REP_LANDING_PREFIXES = LANDING_PREFIXES + ('verification/audits/foundations/a1exit-design-r6-20261125/',)
REP_NAMESPACES = (
    ('class', AUDIT_DIR + 'records/a1-staging-class-', 'oi-side-change-classes/1', 'a1-staging-tool-landing'),
    ('allow', S11_A1_DIRECTORY + '/a1-staging-allow-', 'oi-term-rules/2', 'a1-staging-w1-w2'),
)


def _file_sha(data):
    return hashlib.sha256(data).hexdigest()


def _git_oid(kind, data):
    return hashlib.sha1(('%s %d\0' % (kind, len(data))).encode() + data).hexdigest()


def _rep_git_env():
    return dict(os.environ, GIT_NO_LAZY_FETCH='1', GIT_ALLOW_PROTOCOL='', GIT_TERMINAL_PROMPT='0',
                GIT_GRAFT_FILE=os.devnull)


def _git_rep_read(repo, *args):
    result = subprocess.run(['git', '--no-replace-objects', '-C', repo, *args], capture_output=True,
                            env=_rep_git_env())
    if result.returncode:
        raise ValueError('Git could not read %s' % ' '.join(args))
    return result.stdout


def _rep_commit(repo, oid):
    if not isinstance(oid, str) or not HEX40.fullmatch(oid):
        raise ValueError('a representative role has no full commit id')
    raw = _git_rep_read(repo, 'cat-file', 'commit', oid)
    header = raw.split(b'\n\n', 1)[0].splitlines()
    if _git_oid('commit', raw) != oid or not header or not header[0].startswith(b'tree '):
        raise ValueError('Git commit %s does not verify' % oid)
    return (header[0][5:].decode('ascii'),
            [line[7:].decode('ascii') for line in header if line.startswith(b'parent ')])


def _rep_walk(repo, start, end):
    """Inclusive first-parent path from independently read commit headers."""
    path = []
    current = end
    while True:
        path.append(current)
        _, parents = _rep_commit(repo, current)
        if current == start:
            return list(reversed(path))
        if not parents:
            raise ValueError('%s is absent from the first-parent path ending at %s' % (start, end))
        current = parents[0]


@functools.lru_cache(maxsize=32)
def _rep_entries(repo, commit):
    """Resolve paths, modes and ids through rehashed raw tree objects, independently of rev/path lookup."""
    tree, _ = _rep_commit(repo, commit)
    out = {}
    args = ['git', '--no-replace-objects', '-C', repo, 'cat-file', '--batch']
    with subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL,
                          env=_rep_git_env()) as proc:
        def walk(oid, directory):
            proc.stdin.write(oid.encode('ascii') + b'\n')
            proc.stdin.flush()
            header = proc.stdout.readline().split()
            if len(header) != 3 or header[:2] != [oid.encode('ascii'), b'tree']:
                raise ValueError('Git tree %s is unreadable' % oid)
            size = int(header[2])
            raw = proc.stdout.read(size)
            if len(raw) != size or proc.stdout.read(1) != b'\n' or _git_oid('tree', raw) != oid:
                raise ValueError('Git tree %s does not verify' % oid)
            pos, names = 0, set()
            while pos < len(raw):
                space = raw.index(b' ', pos)
                nul = raw.index(b'\0', space)
                mode, name, child = raw[pos:space], raw[space + 1:nul], raw[nul + 1:nul + 21].hex()
                if mode not in (b'40000', b'100644', b'100755', b'120000', b'160000') or \
                        not HEX40.fullmatch(child) or name in (b'', b'.', b'..') or b'/' in name or name in names:
                    raise ValueError('Git tree %s has an invalid entry' % oid)
                names.add(name)
                path = directory + name.decode('utf-8', 'surrogateescape')
                if mode == b'40000':
                    walk(child, path + '/')
                else:
                    out[path] = (mode.decode('ascii'), child)
                pos = nul + 21

        walk(tree, '')
    return out


def _rep_entry(repo, commit, path):
    if not isinstance(path, str) or not path or any(p in ('', '.', '..') for p in path.split('/')):
        raise ValueError('a representative input names an invalid repository path')
    entry = _rep_entries(repo, commit).get(path)
    if not entry or entry[0] not in REGULAR_MODES:
        raise ValueError('%s is not a regular entry at %s' % (path, commit))
    return _rep_blob(repo, entry)


def _rep_blob(repo, entry):
    mode, oid = entry
    raw = _git_rep_read(repo, 'cat-file', 'blob', oid)
    if _git_oid('blob', raw) != oid:
        raise ValueError('Git blob %s does not verify' % oid)
    return {'mode': mode, 'git_blob': oid, 'blob_sha256': _file_sha(raw)}, raw


def _rep_input(repo, ref, commit, path=None):
    """Read a named operand and verify every retained identity field against Git."""
    if not isinstance(ref, dict) or ref.get('commit') != commit or (path and ref.get('path') != path):
        raise ValueError('the recorded operand does not name its required commit and path')
    path = ref['path']
    entry, raw = _rep_entry(repo, commit, path)
    if ref != dict(entry, commit=commit, path=path):
        raise ValueError('the recorded operand %s differs from its Git entry' % path)
    return raw


def _rep_pin(repo, commit, ref):
    if not isinstance(ref, dict) or set(ref) != {'path', 'blob_sha256'}:
        raise ValueError('a representative reference is not a path and a digest')
    _, raw = _rep_entry(repo, commit, ref['path'])
    if _file_sha(raw) != ref['blob_sha256']:
        raise ValueError('the representative reference %s differs from the blob at %s' % (ref['path'], commit))
    return raw


def _rep_plan_pin(repo, commit, name):
    _, prereg = _rep_entry(repo, commit, S11_A1_DIRECTORY + '/PREREG.md')
    digests = [h for p, h in (last_pin_rows(prereg) or []) if p == name]
    if len(digests) != 1 or not re.fullmatch('[0-9a-f]{64}', digests[0]):
        raise ValueError('the Record pins table does not uniquely pin %s' % name)
    return {'path': S11_A1_DIRECTORY + '/' + name, 'blob_sha256': digests[0]}


def _first_parent_delta(base, after):
    return {p for p in base.keys() | after.keys() if base.get(p) != after.get(p)}


def _tool_acceptance_scope(ctx, candidate, *, current_main):
    """Compare the complete proposed landing tree with its first parent and the existing reviewed edit scope."""
    repo, base, preview = ctx.repo, ctx.tool_base, ctx.tool_preview
    if not base or not preview:
        raise ValueError('tool acceptance requires the exact proposed first parent and merge preview')
    if current_main and base != git_blob_id(repo, 'refs/remotes/origin/main^{commit}'):
        raise ValueError('the proposed first parent differs from the independently read origin/main')
    tree, parents = _rep_commit(repo, preview)
    if parents != [base, candidate]:
        raise ValueError('the proposed landing does not have the exact first parent and tool candidate')
    original, proposed, accepted = [_rep_entries(repo, c) for c in (base, preview, candidate)]
    merge_base = _git_rep_read(repo, 'merge-base', '--all', base, candidate).decode('ascii').splitlines()
    if len(merge_base) != 1:
        raise ValueError('the tool candidate has no unique merge base with the proposed first parent')
    fork = _rep_entries(repo, merge_base[0])
    delta = _first_parent_delta(original, proposed)
    if not delta or delta != {p for p in _first_parent_delta(fork, accepted) if accepted.get(p) != original.get(p)}:
        raise ValueError('the proposed first-parent delta omits or adds paths relative to the exact candidate')
    led_entry, led = _rep_entry(repo, candidate, REP_LEDGER)
    edit_entry, edits = _rep_entry(repo, candidate, REP_EDITS)
    ledger, plan = json.loads(led), json.loads(edits)
    scope = set(ledger['files'])
    if ((led_entry['git_blob'], edit_entry['git_blob']) != (REP_LEDGER_GIT, REP_EDITS_GIT) or
            ledger['edits_sha256'] != edit_entry['blob_sha256'] or not scope or
            scope != {item['file'] for item in plan['edits']}):
        raise ValueError('the checkout lacks the existing complete approved edit-path scope')
    if delta & scope or any(p != WORKFLOW_PATH and not p.startswith(REP_LANDING_PREFIXES) for p in delta):
        raise ValueError('the proposed tool landing touches an edit path or exceeds the authorized landing scope')
    if any(p not in proposed or proposed[p][0] not in REGULAR_MODES or proposed[p] != accepted.get(p)
           for p in delta):
        raise ValueError('a proposed first-parent delta entry is nonregular, deleted or differs from the candidate')
    return {'base': base, 'preview': preview, 'tree': tree, 'edit_paths': sorted(scope), 'delta': {
        p: {'before': original.get(p), 'after': proposed[p]} for p in sorted(delta)}}


def _rep_lineage(repo, commits, role, prefix, schema, record_id, root):
    """Independently recover the designated lineage, including retention and entry modes at each commit."""
    if root.get('path') != prefix + 'root.json':
        raise ValueError('the descriptor names another %s root' % role)
    chain, known = [], {}
    for commit in commits:
        current = {p: e for p, e in _rep_entries(repo, commit).items()
                   if p.startswith(prefix) and '/' not in p[len(prefix):]}
        if not known and set(current) != {root['path']}:
            raise ValueError('the preparation base does not hold exactly the designated %s root' % role)
        if any(current.get(p) != e for p, e in known.items()):
            raise ValueError('a %s lineage entry is missing or was changed at %s' % (role, commit))
        pending = []
        for p in sorted(current.keys() - known.keys()):
            entry, raw = _rep_entry(repo, commit, p)
            pin, doc = {'path': p, 'blob_sha256': entry['blob_sha256']}, json.loads(raw)
            if not isinstance(doc, dict) or doc.get('schema') != schema or doc.get('record_id') != record_id or \
                    'supersedes' not in doc:
                raise ValueError('a %s namespace member has the wrong schema or lineage id' % role)
            pending.append((pin, doc['supersedes']))
        while pending:
            tip = chain[-1] if chain else None
            successors = [pair for pair in pending if pair[1] == tip]
            if len(successors) != 1 or (tip is None and successors[0][0] != root):
                raise ValueError('the %s lineage has a fork, another root or a wrong predecessor' % role)
            chain.append(successors[0][0])
            pending.remove(successors[0])
        known = current
    return chain


def _rep_ref(value):
    return {k: value[k] for k in ('path', 'blob_sha256')}


def _rep_role_selection(config, class_tip, allow_tip):
    """Match the actual configured roles, including the records through which they are read."""
    classes = [r for r in config['records'] if r.get('kind') == 'side-change-classes' and
               r['path'].startswith(REP_NAMESPACES[0][1])]
    rules = [r for r in config['rules'] if r['path'].startswith(REP_NAMESPACES[1][1])]
    if config['roles'].get('side_change_classes') != class_tip or [_rep_ref(r) for r in classes] != [class_tip] or \
            [_rep_ref(r) for r in rules] != [allow_tip]:
        raise ValueError('the configuration does not select the exact active class and allow references')


def _rep_review_pool(repo, commit, config=None, *, dirs=(AUDIT_DIR + 'records/', S11_A1_DIRECTORY + '/')):
    """Read exact configured reviews and the eligible record-directory reviews of predecessors."""
    if config is not None:
        refs = [_rep_ref(r) for r in config['records'] if r.get('kind') == 'review']
        candidates = [(r['path'], _rep_pin(repo, commit, r)) for r in refs]
    else:
        candidates = [(p, _rep_blob(repo, ent)[1]) for p, ent in _rep_entries(repo, commit).items()
                      if p.startswith(dirs) and p.endswith('.json') and ent[0] in REGULAR_MODES]
    reviews = []
    for path, raw in candidates:
        try:
            review = json.loads(raw)
        except ValueError:
            if config is not None:
                raise ValueError('the configured review %s is invalid JSON' % path)
            continue
        if isinstance(review, dict) and review.get('schema') == 'oi-review-record/1':
            reviews.append(review)
        elif config is not None:
            raise ValueError('the configured review %s does not have the ordinary review schema' % path)
    return reviews


def _rep_review_valid(repo, commit, review, ref, author, items):
    rev = review.get('revision')
    verdicts = review.get('verdicts')
    if not (isinstance(rev, str) and HEX40.fullmatch(rev) and _independent_of_author(review, author) and
            isinstance(verdicts, list) and all(isinstance(v, dict) for v in verdicts)):
        return False
    _rep_commit(repo, rev)
    _git_rep_read(repo, 'merge-base', '--is-ancestor', rev, commit)
    return (_rep_pin(repo, rev, ref) is not None and bool(items) and
            len({v.get('item') for v in verdicts}) == len(verdicts) and
            set(items) <= {v.get('item') for v in verdicts if v.get('verdict') == 'accept'})


def _rep_allow_widening(old, current):
    """R6.REC.13 changed items for the designated allow lineage."""
    old_rules = {r['id']: r for r in old.get('rules', [])}
    changed = []
    for r in current['rules']:
        if r.get('kind') != 'allow':
            raise ValueError('the designated allow lineage carries a non-allow rule')
        rid = r['id']
        if rid not in {'W1-b', 'W1-c', 'W1-d', 'W2-a', 'W2-b'}:
            raise ValueError('the designated allow lineage carries an allowance outside the adopted ids')
        q = old_rules.get(rid)
        if q is None:
            changed.append(rid + ':new allow rule without supersedes')
            continue
        before, after = q['matcher'], r['matcher']
        conditions = (
            (set(r['scope']['files']) - set(q['scope']['files']), 'added files'),
            (before['literal'] != after['literal'], 'changed literal'),
            (len(after.get('context', [])) < len(before.get('context', [])) or
             set(map(str, before.get('context', []))) - set(map(str, after.get('context', []))),
             'fewer context literals'),
            (set(map(str, before.get('negative', []))) - set(map(str, after.get('negative', []))),
             'fewer negative literals'),
            (sorted(json.dumps(f, sort_keys=True, separators=(',', ':'), ensure_ascii=False)
                    for f in q['fingerprints']) !=
             sorted(json.dumps(f, sort_keys=True, separators=(',', ':'), ensure_ascii=False)
                    for f in r['fingerprints']),
             'fingerprint set changed'),
            (r['max_instances'] > q['max_instances'], 'larger max_instances'),
            (q['context_required'] and not r['context_required'], 'context_required turned off'),
        )
        changed.extend(rid + ':' + what for changed_scope, what in conditions if changed_scope)
        old_allowance = {(f['file'], f['sentence_sha256'], f['context_sha256']): f.get('negative_allowance') or {}
                         for f in q['fingerprints']}
        for f in r['fingerprints']:
            prior = old_allowance.get((f['file'], f['sentence_sha256'], f['context_sha256']))
            new = f.get('negative_allowance') or {}
            if new and (prior is None or any(n > prior.get(k, 0) for k, n in new.items())):
                changed.append(rid + ':negative_allowance added, raised or moved')
                break
    return changed


def _rep_class_widening(old, current):
    """R6.RECON.34 widening and R6.RECON.31 review items for a class successor."""
    def classes(doc):
        by_id = {}
        for entry in doc['classes']:
            cid, prefixes, pins = entry['id'], entry['prefixes'], entry['pins']
            if not isinstance(cid, str) or not cid or cid in by_id:
                raise ValueError('a class record has a missing or duplicate class id')
            if not isinstance(prefixes, list) or not all(isinstance(p, str) and p for p in prefixes):
                raise ValueError('a class has malformed prefixes')
            if not isinstance(pins, list):
                raise ValueError('a class has no pin list')
            by_path = {}
            for pin in pins:
                if not isinstance(pin, dict) or set(pin) != {'path', 'blob_sha256'} or \
                        not isinstance(pin['path'], str) or not pin['path'] or \
                        not isinstance(pin['blob_sha256'], str) or not re.fullmatch('[0-9a-f]{64}', pin['blob_sha256']):
                    raise ValueError('a class pin must name an exact path and SHA-256')
                if pin['path'] in by_path:
                    raise ValueError('a class has a duplicate pin path')
                by_path[pin['path']] = pin['blob_sha256']
            by_id[cid] = entry, {p.rstrip('/') for p in prefixes}, by_path
        return by_id

    before, after = classes(old), classes(current)
    for cid, (_, prefixes, pins) in after.items():
        _, old_prefixes, old_pins = before.get(cid, (None, set(), {}))
        if prefixes - old_prefixes or pins.items() - old_pins.items():
            break
    else:
        return []
    items = {cid for cid in before.keys() | after.keys() if before.get(cid) != after.get(cid)}
    absent = object()
    fields = (old.keys() | current.keys()) - {'classes', 'supersedes', 'version'}
    changed_fields = {'field:' + key for key in fields if old.get(key, absent) != current.get(key, absent)}
    if items & changed_fields:
        raise ValueError('a class widening review item is ambiguous')
    return sorted(items | changed_fields)


def _rep_lineage_reviews(repo, snapshot, config_commit, config, chains, *, record_commits=None):
    history = _rep_review_pool(repo, snapshot)
    active = history if config is None else _rep_review_pool(repo, config_commit, config)
    for role, chain in chains.items():
        prior_doc, prior_ref = {}, None
        for ref in chain:
            holder = snapshot if record_commits is None else record_commits[ref['path'], ref['blob_sha256']]
            doc = json.loads(_rep_pin(repo, holder, ref))
            is_tip = ref == chain[-1]
            pool, scope = (active, config_commit) if is_tip else (history, snapshot)
            if is_tip:
                _rep_pin(repo, config_commit, ref)
            exact = [r for r in pool if r.get('reviewed') == ref]
            ordinary = [r for r in exact if r.get('kind', 'review') == 'review']
            entries = doc['classes' if role == 'class' else 'rules']
            if not entries:
                raise ValueError('the %s representative scope is empty' % role)
            items = [r['id'] for r in entries] or [doc['record_id']]
            author = doc.get('author')
            if not ordinary or not all(r.get('method') and
                                       _rep_review_valid(repo, scope, r, ref, author, items) for r in ordinary):
                raise ValueError('ordinary review does not qualify %s' % ref['path'])
            if role == 'class' and prior_ref is not None:
                changed = _rep_class_widening(prior_doc, doc)
                if changed:
                    reviews = [r for r in exact if r.get('kind') == 'widening']
                    if not reviews or not all(
                            r.get('replaces') == prior_ref and isinstance(r.get('method'), str) and
                            re.search(r'\b[0-9a-f]{40}\b', r['method']) and
                            _rep_review_valid(repo, scope, r, ref, author, changed) and
                            len(r['verdicts']) == len(changed) and
                            all(set(v) == {'item', 'verdict', 'reason'} and isinstance(v['reason'], str)
                                for v in r['verdicts']) and
                            all(_independent_of_author(r, o['reviewer']) for o in ordinary) for r in reviews):
                        raise ValueError('class widening review does not qualify %s' % ref['path'])
            widened = _rep_allow_widening(prior_doc, doc) if role == 'allow' else []
            if widened:
                # At the designated root the predecessor field must be explicitly null.
                others = [r['reviewer'] for r in ordinary]
                if not any(r.get('kind') == 'widening' and 'replaces' in r and r['replaces'] == prior_ref and
                           all(v['verdict'] == 'accept' for v in r.get('verdicts', [])) and
                           _rep_review_valid(repo, scope, r, ref, author, widened) and
                           all(_independent_of_author(r, who) for who in others) and
                           (prior_ref is not None or
                            all(_independent_of_author(o, r['reviewer']) for o in ordinary)) for r in exact):
                    raise ValueError('widening review does not qualify %s' % ref['path'])
            prior_doc, prior_ref = doc, ref


def _rep_auxiliary_lineage(repo, freeze, config, tip, kind, schema, dirs):
    """Resolve the exact predecessors of a configured record on F's first-parent history."""
    chain, holders = [], {}
    ref, lineage_id, paths = tip, None, set()
    while ref is not None:
        if not isinstance(ref, dict) or set(ref) != {'path', 'blob_sha256'} or \
                not isinstance(ref['path'], str) or any(p in ('', '.', '..') for p in ref['path'].split('/')) or \
                not isinstance(ref['blob_sha256'], str) or not re.fullmatch('[0-9a-f]{64}', ref['blob_sha256']):
            raise ValueError('the %s lineage has an invalid reference' % kind)
        key = (ref['path'], ref['blob_sha256'])
        if key in holders or (kind == 'side-change-classes' and ref['path'] in paths):
            raise ValueError('the %s lineage has a repeated reference' % kind)
        holder = freeze
        while True:
            entry = _rep_entries(repo, holder).get(ref['path'])
            if entry is not None:
                if entry[0] in REGULAR_MODES:
                    info, raw = _rep_blob(repo, entry)
                    if info['blob_sha256'] == ref['blob_sha256']:
                        break
                elif kind == 'side-change-classes':
                    raise ValueError('the auxiliary class lineage contains a nonregular record')
            parents = _rep_commit(repo, holder)[1]
            if not parents or ref == tip:
                raise ValueError('the %s lineage lacks its exact record at %s' % (kind, ref['path']))
            holder = parents[0]
        doc = json.loads(raw)
        if not isinstance(doc, dict) or doc.get('schema') != schema or \
                not isinstance(doc.get('record_id'), str) or not doc['record_id'] or 'supersedes' not in doc or \
                (lineage_id is not None and doc['record_id'] != lineage_id):
            raise ValueError('the %s record is outside its declared lineage' % kind)
        lineage_id = doc['record_id']
        chain.append(ref)
        holders[key] = holder
        paths.add(ref['path'])
        ref = doc['supersedes']

    chain_entries = {(r['path'], r['blob_sha256']) for r in chain}
    successors = {(older['path'], older['blob_sha256']): (newer['path'], newer['blob_sha256'])
                  for newer, older in zip(chain, chain[1:])}
    extra = set()
    configured = {r['path'] for r in config['records'] if r.get('kind') == kind}
    for path, entry in _rep_entries(repo, freeze).items():
        if entry[0] not in REGULAR_MODES or not (path in configured or path.startswith(dirs) and
                                                path.endswith('.json')):
            continue
        info, raw = _rep_blob(repo, entry)
        key = (path, info['blob_sha256'])
        if key in chain_entries:
            continue
        try:
            doc = json.loads(raw)
        except ValueError:
            continue
        if not isinstance(doc, dict):
            continue
        if (doc.get('schema'), doc.get('record_id')) != (schema, lineage_id):
            parent = doc.get('supersedes')
            if kind == 'scope' and isinstance(parent, dict) and set(parent) == {'path', 'blob_sha256'} and \
                    isinstance(parent['path'], str) and isinstance(parent['blob_sha256'], str) and \
                    (parent['path'], parent['blob_sha256']) in successors:
                raise ValueError('the scope lineage has an incompatible competing successor')
            continue
        predecessor = doc.get('supersedes')
        if not isinstance(predecessor, dict) or set(predecessor) != {'path', 'blob_sha256'}:
            raise ValueError('the %s lineage has another root' % kind)
        before = (predecessor['path'], predecessor['blob_sha256'])
        if before in successors:
            raise ValueError('the %s lineage has ambiguous successors' % kind)
        successors[before] = key
        extra.add(key)
    # An unused descendant can be on this lineage. A fork or reused lineage id cannot qualify the selected record.
    point = (tip['path'], tip['blob_sha256'])
    while successors.get(point) in extra:
        point = successors[point]
        extra.remove(point)
    if extra:
        raise ValueError('the %s record_id is reused outside its exact lineage' % kind)
    return list(reversed(chain)), holders


def _rep_auxiliary_class_lineage(repo, freeze, config, tip):
    return _rep_auxiliary_lineage(repo, freeze, config, tip, 'side-change-classes', REP_NAMESPACES[0][2],
                                  (AUDIT_DIR + 'records/', S11_A1_DIRECTORY + '/'))


def _rep_class_pins(repo, commit, class_tip):
    doc = json.loads(_rep_pin(repo, commit, class_tip))
    classes = [c for c in doc['classes'] if c['id'] == 'tool-landing']
    if len(classes) != 1:
        raise ValueError('the active class does not define tool-landing exactly once')
    prefixes = tuple(p.rstrip('/') + '/' for p in classes[0]['prefixes'])
    if any(not p.startswith(REP_LANDING_PREFIXES) or any(e in ('', '.', '..') for e in p[:-1].split('/'))
           for p in prefixes):
        raise ValueError('the tool-landing class has a prefix outside its allowed scope')
    pins = classes[0]['pins']
    result = {}
    for pin in pins:
        _rep_pin(repo, commit, pin)
        if pin['path'] in result or (pin['path'] != WORKFLOW_PATH and not pin['path'].startswith(prefixes)):
            raise ValueError('the tool-landing class pin is repeated or outside its permitted prefixes')
        result[pin['path']] = pin['blob_sha256']
    return result


def _reviewed_items(doc):
    fields = (('rules', 'id'), ('sites', 'site_id'), ('entries', 'id'), ('classifications', 'id'),
              ('records', 'id'), ('classes', 'id'))
    if doc.get('schema') == 'oi-retirement-config/1':
        return [doc['config_id']]
    return [v[k] for field, k in fields for v in doc.get(field, [])] or [doc['record_id']]


def _rep_tool_image(repo, commit, config):
    entries = _rep_entries(repo, commit)
    paths = {p for p in entries if p == 'tools/ledger_coverage.py' or p.startswith('tools/ledger_coverage/')}
    refs = config['tool']['files']
    pins = {r['path']: r['blob_sha256'] for r in refs}
    if not paths or len(pins) != len(refs) or pins.keys() != paths or \
            config['tool']['workflow']['path'] != WORKFLOW_PATH:
        raise ValueError('the configuration does not pin the complete tool and workflow image')
    pins[WORKFLOW_PATH] = config['tool']['workflow']['blob_sha256']
    for path, digest in pins.items():
        _rep_pin(repo, commit, {'path': path, 'blob_sha256': digest})
    return paths | {WORKFLOW_PATH}


def _rep_live_subject(ctx, binding, config, descriptor, chains, class_pins, template):
    """Tie the live binding to the assessed F, the independently read main tip and the actual normal merge."""
    repo, F = ctx.repo, ctx.freeze
    B, S, M, T = binding['B'], ctx.rep_snapshot, ctx.rep_main, ctx.tool_landing
    tip = ctx.main_tip
    if not isinstance(tip, str) or not HEX40.fullmatch(tip) or \
            git_blob_id(repo, 'refs/remotes/origin/main^{commit}') != tip:
        raise ValueError('the representative main tip differs from the independently read origin/main')
    if binding.get('T_land') != T or binding.get('M_rep') != M or binding.get('main_tip') != tip:
        raise ValueError('the live landing or main roles differ from the assessment operands')
    if T == B or _rep_walk(repo, M, tip) != binding['main_path'] or \
            _rep_walk(repo, T, B) != binding['landing_to_base']:
        raise ValueError('the representative anchor and preparation base lack the required first-parent placement')
    if binding['descriptor'] != _rep_plan_pin(repo, F, REP_DESCRIPTOR) or \
            _rep_pin(repo, F, binding['descriptor']) != _rep_pin(repo, S, binding['descriptor']):
        raise ValueError('the representative descriptor differs from the one pinned at F')
    path_f = _rep_walk(repo, B, F)
    for role, prefix, schema, record_id in REP_NAMESPACES:
        if _rep_lineage(repo, path_f, role, prefix, schema, record_id, descriptor[role + '_root']) != chains[role]:
            raise ValueError('the candidate F and representative snapshot select different %s lineages' % role)
    prior = json.loads(_rep_pin(repo, F, _rep_plan_pin(repo, F, REP_PRIOR)))
    if not isinstance(prior, dict) or set(prior) != {'schema', 'freeze'} or \
            prior.get('schema') != 'oi-a1-staging-prior/1':
        raise ValueError('the prior-freeze declaration at F is invalid')
    if prior['freeze'] is not None:
        previous = prior['freeze']
        if previous not in path_f[:-1] or _rep_plan_pin(repo, previous, REP_DESCRIPTOR) != binding['descriptor']:
            raise ValueError('the prior freeze lacks continuity with the assessed F')
        _rep_pin(repo, previous, binding['descriptor'])
        _, prereg = _rep_entry(repo, previous, S11_A1_DIRECTORY + '/PREREG.md')
        older_configs = []
        for name, digest in last_pin_rows(prereg) or []:
            ref = {'path': S11_A1_DIRECTORY + '/' + name, 'blob_sha256': digest}
            raw = _rep_pin(repo, previous, ref)
            try:
                doc = json.loads(raw)
            except ValueError:
                continue
            if isinstance(doc, dict) and doc.get('schema') == 'oi-retirement-config/1':
                older_configs.append(ref)
        if len(older_configs) != 1:
            raise ValueError('the prior freeze does not uniquely pin its configuration')
        old_pin = older_configs[0]
        current_pin = _rep_plan_pin(repo, F, os.path.basename(ctx.config_path))
        if old_pin['blob_sha256'] != current_pin['blob_sha256'] and config.get('supersedes') != old_pin:
            raise ValueError('the configuration does not supersede the previously pinned configuration')
    ledger = json.loads(_rep_pin(repo, F, _rep_plan_pin(repo, F, 'ledger.json')))
    edits = _rep_plan_pin(repo, F, 'edits.json')
    _rep_pin(repo, F, edits)
    final_h = config['roles']['scientific_base']
    if ledger.get('base') != final_h or ledger.get('edits_sha256') != edits['blob_sha256'] or \
            final_h in (B, T) or final_h not in binding['landing_to_base']:
        raise ValueError('the final ledger, edit list or scientific base at F is misbound')
    allowances = json.loads(_rep_pin(repo, S, chains['allow'][-1]))['rules']
    if not allowances or any(r.get('recorded_at') != final_h or not r.get('fingerprints') for r in allowances):
        raise ValueError('the active allowance proofs do not bind their fingerprints to final H')
    for path in {f['file'] for r in allowances for f in r['fingerprints']}:
        _rep_entry(repo, final_h, path)
    ledger_paths = sorted(ledger['files'])
    if not ledger_paths or binding.get('ledger_paths') != ledger_paths:
        raise ValueError('the representative evidence omits the complete final ledger path set')

    tree, parents = _rep_commit(repo, T)
    if len(parents) != 2 or parents[0] != ctx.tool_base or (tree, parents, parents[1]) != (binding.get('landing_tree'),
                                                           binding.get('landing_parents'),
                                                           binding.get('tool_candidate')):
        raise ValueError('the landing record does not identify the actual normal tool merge and candidate')
    base, landed, candidate, main = [_rep_entries(repo, c) for c in (parents[0], T, parents[1], M)]
    delta = _first_parent_delta(base, landed)
    if not delta or delta & set(ledger_paths) or any(
            p != WORKFLOW_PATH and not p.startswith(REP_LANDING_PREFIXES) for p in delta):
        raise ValueError('the actual first-parent landing delta is outside the approved path scope')
    if any(p not in landed or landed[p][0] not in REGULAR_MODES or
           landed[p] != candidate.get(p) or landed[p] != main.get(p) for p in delta):
        raise ValueError('a landing delta entry is missing, nonregular or substituted')
    proposal = _tool_acceptance_scope(ctx, parents[1], current_main=False)
    actual_delta = {p: {'before': base.get(p), 'after': landed[p]} for p in delta}
    if proposal['delta'] != actual_delta:
        raise ValueError('the actual tool landing differs from the retained reviewed proposal')
    after = {p: _rep_blob(repo, landed[p])[0] for p in delta}
    before = {}
    for p in delta & base.keys():
        mode, oid = base[p]
        before[p] = (_rep_blob(repo, base[p])[0] if mode in REGULAR_MODES else
                     {'mode': mode, 'git_blob': oid, 'blob_sha256': None})
    if binding.get('landing_delta') != {p: {'before': before.get(p), 'after': after[p]} for p in delta} or \
            class_pins != {p: e['blob_sha256'] for p, e in after.items()}:
        raise ValueError('the retained delta or class pins differ from the complete actual first-parent delta')
    if not {REP_TEMPLATE, REP_EDITS, REP_LEDGER} <= delta:
        raise ValueError('the actual tool landing delta omits the template or its fixed input copies')
    tool_paths = _rep_tool_image(repo, T, template)
    audit_refs = [r for r in _rep_refs(template) if r['path'].startswith(AUDIT_DIR)]
    for ref in audit_refs:
        _rep_pin(repo, T, ref)
    image_paths = tool_paths | {p for p in landed if p.startswith(AUDIT_DIR + 'rep/')} | \
        {r['path'] for r in audit_refs}
    current = _rep_entries(repo, binding['tool_rev'])
    for entries in (candidate, main, current):
        if any(entries.get(p) != landed[p] for p in image_paths) or any(
                p not in image_paths for p in entries if
                p.startswith(('tools/ledger_coverage/', AUDIT_DIR + 'rep/'))):
            raise ValueError('the accepted tool, workflow, template or control input image has changed')
    if binding.get('tool_image') != {p: after[p] if p in after else _rep_blob(repo, landed[p])[0]
                                     for p in image_paths} or config.get('tool') != template.get('tool'):
        raise ValueError('the candidate F or retained image does not pin the exact accepted tool')
    # After final H, the representative staging comparison has its own exact role and record pins.
    # A matching prefix does not classify an added path. The later actual M has its own full check.
    patterns = [re.compile(p) for p in config['corpus'].get('patterns', [])]
    corpus = set(config['corpus'].get('paths', []))
    staging_delta = _first_parent_delta(_rep_entries(repo, final_h), main)
    staged_entries = {p: _rep_blob(repo, main[p])[0] for p in staging_delta if p in main and
                      main[p][0] in REGULAR_MODES and p not in ledger['files'] and p not in corpus and
                      not any(pat.search(p) for pat in patterns)}
    observed_pins = {(p, entry['blob_sha256'], blob) for p, entry in staged_entries.items()
                     for blob in (None, entry['git_blob'])}
    staged = [descriptor['custody'], binding['descriptor'],
              *(r for role in binding['chains_at_M'].values() for r in role)]
    reviews = _rep_review_pool(repo, F, config)
    for source in config['records']:
        ref = _rep_ref(source)
        if not any(r.get('reviewed') == ref and r.get('kind', 'review') == 'review' for r in reviews):
            continue
        record = json.loads(_rep_pin(repo, source.get('commit', F), ref))
        if any(r.get('method') and r.get('reviewed') == ref and r.get('kind', 'review') == 'review' and
               _rep_review_valid(repo, F, r, ref, record.get('author'), _reviewed_items(record))
               for r in reviews):
            staged.append(ref)
            if record.get('schema') == 'oi-side-change-classes/1':
                other_pins = [p for c in record['classes'] if c['id'] != 'tool-landing'
                              for p in c.get('pins', []) if {'path', 'blob_sha256'} <= p.keys()]
                if ref != chains['class'][-1] and ('supersedes' not in record or record['supersedes'] is not None) and any(
                        (p['path'], p['blob_sha256'], p.get('git_blob')) in observed_pins for p in [ref, *other_pins]):
                    chain, holders = _rep_auxiliary_class_lineage(repo, F, config, ref)
                    _rep_lineage_reviews(repo, F, F, config, {'class': chain}, record_commits=holders)
                staged.extend(other_pins)
    for source in config['records']:
        if source.get('kind') == 'review':
            ref = _rep_ref(source)
            review = json.loads(_rep_pin(repo, F, ref))
            if review.get('reviewed') in staged:
                staged.append(ref)
    pins = {(r['path'], r['blob_sha256'], r.get('git_blob')) for r in staged}
    unresolved = staging_delta - {p for p, _, _ in observed_pins & pins}
    if unresolved:
        raise ValueError('unclassified or drifted representative staging paths: %s' % sorted(unresolved)[:8])
    path = _rep_walk(repo, final_h, M)
    changes = {}
    for a, b in zip(path, path[1:]):
        scope = _first_parent_delta(_rep_entries(repo, a), _rep_entries(repo, b)) & staging_delta
        changes.update({p: b for p in scope})
    return {p: {'commit': changes[p], **staged_entries[p]} for p in sorted(staging_delta)}


def _rep_fill(template, roles):
    if isinstance(template, list):
        return [_rep_fill(v, roles) for v in template]
    if isinstance(template, dict):
        result = {k: _rep_fill(v, roles) for k, v in template.items() if k != 'fill'}
        if 'fill' in template:
            if {'path', 'blob_sha256'} & result.keys():
                raise ValueError('a template hole also names a fixed reference')
            result.update(roles[template['fill']])
        return result
    return template


def _rep_refs(value):
    if isinstance(value, dict):
        pin = [_rep_ref(value)] if {'path', 'blob_sha256'} <= value.keys() else []
        return pin + [r for child in value.values() for r in _rep_refs(child)]
    if isinstance(value, list):
        return [r for child in value for r in _rep_refs(child)]
    return []


def _rep_dependency_check(repo, binding, instance, template, template_raw, config, operands):
    """Reconstruct K1 edges from the filled/template bytes and references actually available to the binding."""
    S, M, B = binding['S'], binding['M'], binding['B']
    commits = list(dict.fromkeys([M, S, B, binding['template']['commit'], operands['config']['commit']]))
    entries = [_rep_entries(repo, c) for c in commits]
    template_digest, instance_digest = _file_sha(template_raw), binding['instance_sha256']
    fixed = [_rep_ref(operands[k]) for k in ('builder', 'ledger', 'edits', 'delegation')]
    nodes = {template_digest: _rep_refs(template),
             instance_digest: _rep_refs(instance) + fixed + [binding['descriptor'], _rep_ref(binding['template'])]}
    active, done = set(), set()

    def walk(digest, references):
        if digest in active:
            raise ValueError('the representative instance has a cycle in its actual dependency links')
        if digest in done:
            return
        active.add(digest)
        for ref in references:
            child = ref['blob_sha256']
            if child not in nodes:
                nodes[child] = []
                for tree in entries:
                    entry = tree.get(ref['path'])
                    if entry and entry[0] in REGULAR_MODES:
                        info, raw = _rep_blob(repo, entry)
                        if info['blob_sha256'] == child:
                            try:
                                nodes[child] = _rep_refs(json.loads(raw))
                            except ValueError:
                                pass
                            break
            walk(child, nodes[child])
        active.remove(digest)
        done.add(digest)

    walk(instance_digest, nodes[instance_digest])
    config_digest = operands['config']['blob_sha256']
    walk(config_digest, _rep_refs(config))


def _rep_build_inputs(ev, ctx, phase, observed):
    repo, binding, operands = ctx.repo, observed['control_instance'], observed['operands']
    mode = {'tool-acceptance': 'fixture', 'candidate-F': 'live'}[phase]
    F = ctx.freeze if mode == 'live' else None
    B, S, M, tool = (binding[k] for k in ('B', 'S', 'M', 'tool_rev'))
    if binding.get('mode') != mode or binding.get('freeze') != F or \
            tool != git_blob_id(repo, 'HEAD^{commit}') or (F is None and tool != ctx.tool_candidate):
        raise ValueError('the REP-BUILD evidence belongs to another assessed subject or applicability')
    if F is not None and (S != ctx.rep_snapshot or M != ctx.rep_main):
        raise ValueError('the representative snapshot or main differs from the assessment operands')
    config_commit = F or S
    config = json.loads(_rep_input(repo, operands['config'], config_commit, ctx.config_path if F else None))
    if config.get('schema') != 'oi-retirement-config/1':
        raise ValueError('the selected configuration does not have the retirement config schema')
    if F is not None and _rep_ref(operands['config']) != _rep_plan_pin(repo, F, os.path.basename(ctx.config_path)):
        raise ValueError('the live representative configuration differs from the Record pin at F')
    if binding['descriptor']['path'] != S11_A1_DIRECTORY + '/' + REP_DESCRIPTOR:
        raise ValueError('the representative descriptor is outside its designated path')
    desc = json.loads(_rep_pin(repo, S, binding['descriptor']))
    if not isinstance(desc, dict) or set(desc) != {'schema', 'base', 'custody', 'class_root', 'allow_root'} or \
            desc['schema'] != 'oi-a1-staging-transition/1' or desc['base'] != B:
        raise ValueError('the descriptor does not bind the stated preparation base and two roots')
    _rep_pin(repo, B, desc['custody'])
    walk_s, walk_m = _rep_walk(repo, B, S), _rep_walk(repo, B, M)
    chains = {}
    for walk, name in ((walk_s, 'S'), (walk_m, 'M')):
        chain = {role: _rep_lineage(repo, walk, role, prefix, schema, record_id, desc[role + '_root'])
                 for role, prefix, schema, record_id in REP_NAMESPACES}
        chains[name] = chain
        if binding.get('chains_at_' + name) != chain or binding.get(
                'snapshot_path' if name == 'S' else 'representative_path') != walk:
            raise ValueError('the retained role lineage or path differs from the verified %s lineage' % name)
    class_tip = chains['M']['class'][-1]
    allow_tip = chains['S']['allow'][-1]
    if class_tip != binding['class_tip'] or class_tip != chains['S']['class'][-1] or allow_tip != binding['allow_tip']:
        raise ValueError('the representative and snapshot class/allow roles are stale or mismatched')
    _rep_role_selection(config, class_tip, allow_tip)
    _rep_lineage_reviews(repo, S, config_commit, config, chains['S'])
    if chains['M']['allow'] != chains['S']['allow']:
        _rep_lineage_reviews(repo, M, M, None, {'allow': chains['M']['allow']})
    class_pins = _rep_class_pins(repo, M, class_tip)
    origin = ctx.tool_landing if F else tool
    tpl = binding['template']
    template_raw = _rep_input(repo, tpl, origin, REP_TEMPLATE)
    template = json.loads(template_raw)
    roles = {'class-tip-at-M': class_tip, 'allow-tip-at-S': allow_tip}
    inst_raw = ev.text('control-instance.json')
    if (template['roles'].get('side_change_classes') != {'fill': 'class-tip-at-M'} or
            {r['blob_sha256'] for r in chains['M']['class']} &
            {r['blob_sha256'] for r in _rep_refs(template)} or inst_raw is None or
            tpl['blob_sha256'] != class_pins.get(REP_TEMPLATE) or
            _file_sha(inst_raw) != binding['instance_sha256']):
        raise ValueError('the exact unfilled template and filled instance are not bound to the role pins')
    instance = json.loads(inst_raw)
    if instance != _rep_fill(template, roles):
        raise ValueError('the retained instance does not fill the exact template from the resolved roles')
    _rep_role_selection(instance, class_tip, allow_tip)
    verified_staging = {}
    if F:
        verified_staging = _rep_live_subject(ctx, binding, config, desc, chains['S'], class_pins, template)
    else:
        _rep_tool_image(repo, tool, template)
        for path in (REP_BUILDER, REP_EDITS, REP_LEDGER):
            entry, _ = _rep_entry(repo, tool, path)
            if class_pins.get(path) != entry['blob_sha256']:
                raise ValueError('the fixture omits the exact tool-candidate input %s' % path)
    builder = _rep_input(repo, operands['builder'], tool, REP_BUILDER)
    ledger = _rep_input(repo, operands['ledger'], origin, REP_LEDGER)
    edits = _rep_input(repo, operands['edits'], origin, REP_EDITS)
    dref = _rep_ref(instance['delegation'])
    delegation = _rep_input(repo, operands['delegation'], instance['delegation'].get('commit') or origin, dref['path'])
    if _file_sha(delegation) != dref['blob_sha256'] or \
            _git_oid('blob', ledger) != REP_LEDGER_GIT or _git_oid('blob', edits) != REP_EDITS_GIT:
        raise ValueError('the representative delegation, ledger or edits differ from their exact pins')
    H, E = json.loads(ledger)['base'], operands['E']
    if operands['H'] != H or E != REP_E:
        raise ValueError('the representative E or ledger base is substituted')
    _rep_walk(repo, E, H)
    if F:
        _rep_walk(repo, H, ctx.tool_landing)
    _rep_dependency_check(repo, binding, instance, template, template_raw, config, operands)
    return H, M, ledger, edits, builder, json.loads(delegation), verified_staging


def _rep_spliced(raw, path, ledger):
    want = ledger['files'][path]
    if _file_sha(raw) != want['base_sha256']:
        raise ValueError('a ledgered path does not match its exact scientific base')
    body, previous = raw, len(raw)
    splices = sorted((s for s in ledger['splices'] if s['file'] == path),
                     key=lambda s: (s['start'], s['end']), reverse=True)
    for splice in splices:
        start, end, new = splice['start'], splice['end'], splice['new'].encode()
        if not 0 <= start <= end <= previous or _file_sha(raw[start:end]) != splice['old_sha256'] or \
                _file_sha(new) != splice['new_sha256']:
            raise ValueError('a retained ledger splice is out of bounds, overlapping or mismatched')
        body = body[:start] + new + body[end:]
        previous = start
    return body


def _rep_construction(repo, inputs):
    H, M, ledger_bytes, edits, _, delegation = inputs[:6]
    ledger = json.loads(ledger_bytes)
    if ledger['edits_sha256'] != _file_sha(edits) or any(s['file'] not in ledger['files'] for s in ledger['splices']):
        raise ValueError('the ledger does not bind the edits or one of its splices names another path')
    changes = {}
    for path, pin in ledger['files'].items():
        _, raw = _rep_entry(repo, H, path)
        body = _rep_spliced(raw, path, ledger)
        if _file_sha(body) != pin['expected_sha256']:
            raise ValueError(REP_HASH_REASON)
        if body != raw:
            changes[path] = body
    for path, raw in ((S11_A1_DIRECTORY + '/ledger.json', ledger_bytes), (S11_A1_DIRECTORY + '/edits.json', edits)):
        if path in ledger['files']:
            raise ValueError('a pinned plan copy aliases a ledgered path')
        changes[path] = raw
    delegated = {p for c in delegation['classes'] for p in c['paths'] if not p.endswith('/')}
    markers = {p: REP_MARKER % p.encode() for p in delegated - ledger['files'].keys()}
    if changes.keys() & markers.keys():
        raise ValueError('a delegated marker aliases a pinned plan copy')
    entries_h, entries_m = _rep_entries(repo, H), _rep_entries(repo, M)
    if any(e.get(p, (None, None))[1] == _git_oid('blob', b) for p, b in markers.items()
           for e in (entries_h, entries_m)):
        raise ValueError('a representative marker does not differ from both H and its designated M')
    changes.update(markers)
    measured = {p: {'mode': '100644', 'git_blob': _git_oid('blob', b), 'blob_sha256': _file_sha(b)}
                for p, b in changes.items()}
    changed_values = {p: '100644:' + ent['git_blob'] for p, ent in measured.items()}
    h = hashlib.sha1()
    h.update(REP_SUBJECT.encode())
    h.update(H.encode())
    for p in sorted(changed_values):
        h.update(p.encode() + b'\0' + changed_values[p].encode())
    h.update(H.encode())
    # The overlay reports its deterministic tree id from materialized file values, while its entry map
    # preserves the untouched base's modes. Derive the id and the changed entry map independently.
    values = {p: '100644:' + oid if mode in REGULAR_MODES else '120000:' + _git_oid('blob', b'')
              for p, (mode, oid) in entries_h.items() if mode != '160000'}
    values.update(changed_values)
    tree = hashlib.sha1(repr(sorted(values.items())).encode()).hexdigest()
    delta = {p: e for p, e in measured.items() if entries_h.get(p) != (e['mode'], e['git_blob'])}
    return {'commit': h.hexdigest(), 'tree': tree, 'parents': [H], 'changes': delta,
            'reads': {'H': sorted(ledger['files'].keys() | markers.keys()), 'M': sorted(markers)}}


def _rep_imports(source):
    imports = set()
    for node in ast.walk(ast.parse(source)):
        if isinstance(node, ast.Import):
            imports.update(n.name for n in node.names)
        elif isinstance(node, ast.ImportFrom):
            imports.add('.' * node.level + (node.module or ''))
    return imports


def _rep_mutated_ledger(repo, H, ledger_raw, mutant_raw):
    ledger, mutant = json.loads(ledger_raw), json.loads(mutant_raw)
    original, changed = ledger['splices'][0], mutant['splices'][0]
    before, after = original['new'].encode(), changed['new'].encode()
    if len(before) != len(after) or sum(o != n for o, n in zip(before, after)) != 1 or \
            changed['new_sha256'] != _file_sha(after):
        raise ValueError('the retained ledger mutant does not change exactly one new byte and its splice digest')
    mutant['splices'][0] = dict(changed, new=original['new'], new_sha256=original['new_sha256'])
    if mutant != ledger:
        raise ValueError('the retained ledger mutant makes changes outside that byte')
    mutant['splices'][0] = changed
    path = original['file']
    _, raw = _rep_entry(repo, H, path)
    if _file_sha(_rep_spliced(raw, path, mutant)) == ledger['files'][path]['expected_sha256']:
        raise ValueError('the retained one-byte mutant did not violate the expected path digest')
    return original['id'], path


def eval_rep_build(row, ev, ctx, phase, findings):
    """Read the three existing case observations and independently bind and evaluate their actual inputs."""
    actual = [{'case': name} for name in REP_CASES]
    cases = row['expect'].get('cases', [])
    if tuple(c.get('case') for c in cases) != REP_CASES:
        raise FileInvalid('REP-BUILD does not specify its three adopted cases')
    if ev.man is None or not all(isinstance(c, dict) for c in ev.man['cases']) or \
            [c.get('case') for c in ev.man['cases']] != list(REP_CASES):
        findings.append(('raw-evidence-missing', 'REP-BUILD must retain each of its three cases exactly once'))
        return actual
    if [c.get('argv') for c in ev.man['cases']] != [['in-process', name] for name in REP_INVOCATIONS]:
        findings.append(('raw-evidence-missing', 'REP-BUILD does not retain the three prescribed actual invocations'))
        return actual
    observed = [ev.json(ev.case(name).get('result_file')) for name in REP_CASES]
    if not all(isinstance(d, dict) for d in observed):
        findings.append(('raw-evidence-missing', 'REP-BUILD is missing a raw case observation'))
        return actual
    inputs = None
    try:
        inputs = _rep_build_inputs(ev, ctx, phase, observed[0])
        expected = _rep_construction(ctx.repo, inputs)
        builds = observed[0]['builds']
        if not isinstance(builds, list) or len(builds) != 2 or any(
                {k: b[k] for k in expected} != expected for b in builds):
            raise ValueError('the two observed builds differ from the independently derived commit, tree or entries')
        if _rep_imports(inputs[4]) - {'hashlib', 'json'} or observed[0].get('nonconforming') != []:
            raise ValueError('the exact builder imports outside its standard-library scope or reports nonconformance')
        actual[0].update(outcome='HASH_EQUAL', builds=builds, applicability=observed[0]['control_instance']['mode'],
                         operands=observed[0]['operands'])
        if phase == 'candidate-F':
            actual[0]['verified_staging_changes'] = inputs[-1]
    except (ValueError, SyntaxError, KeyError, AttributeError, TypeError) as exc:
        findings.append(('declarative-mismatch', 'REP-BUILD construction/binding: %s' % exc))
    if inputs is None:
        return actual
    try:
        mutant = ev.text('ledger.mutant.json')
        splice, path = _rep_mutated_ledger(ctx.repo, inputs[0], inputs[2], mutant)
        wanted = {'outcome': 'REFUSED', 'reason': REP_HASH_REASON}
        if (observed[1].get('splice'), observed[1].get('file')) != (splice, path) or \
                observed[1].get('outcome') != wanted['outcome'] or observed[1].get('reason') not in (
                    REP_HASH_REASON, '%s: %s' % (REP_HASH_REASON, path)):
            raise ValueError('the one-byte mutant did not report the required expected_sha256 refusal')
        actual[1].update(wanted, splice=splice, path=path)
    except (ValueError, KeyError, TypeError) as exc:
        findings.append(('declarative-mismatch', 'REP-BUILD ledger mutant: %s' % exc))
    try:
        source, mutant = inputs[4], ev.text('rep_build.mutant.py')
        planted = source.replace(b'import hashlib\n', b'import hashlib\nfrom ledger_coverage.engine import util\n', 1)
        if mutant != planted or source == mutant or _rep_imports(mutant) - _rep_imports(source) != {
                'ledger_coverage.engine'}:
            raise ValueError('the retained builder mutant is not the exact engine import case')
        if (observed[2].get('outcome'), observed[2].get('reason')) != ('REFUSED', REP_IMPORT_REASON):
            raise ValueError('the engine-import mutant did not report the required refusal')
        actual[2].update(outcome='REFUSED', reason=REP_IMPORT_REASON)
    except (ValueError, SyntaxError, TypeError) as exc:
        findings.append(('declarative-mismatch', 'REP-BUILD import mutant: %s' % exc))
    return actual


def _case_args(argv, flag):
    if not isinstance(argv, list) or not all(isinstance(arg, str) for arg in argv):
        return None
    values = [argv[i + 1] for i, arg in enumerate(argv[:-1]) if arg == flag and not argv[i + 1].startswith('--')]
    return values if len(values) == argv.count(flag) else None


def _rep_fixed_reconciliation(ctx, phase, rid, ev, case, result):
    """Bind fixed N10/N11 to their own Git inputs and the same accepted tool image."""
    repo = ctx.repo
    fixed_commit, sep, fixed_path = (ctx.fixed_config or '').partition(':')
    if not sep or not HEX40.fullmatch(fixed_commit):
        raise ValueError('the gate has no exact fixed configuration ref')
    scope = ev.json('fixed-inputs.json')
    if not isinstance(scope, dict) or scope.get('scope') != 'fixed representative reconciliation control':
        raise ValueError('the exact fixed reconciliation scope is missing')
    tool = scope['tool']
    allowed = {git_blob_id(repo, 'HEAD^{commit}')}
    if phase == 'candidate-F':
        _, parents = _rep_commit(repo, ctx.tool_landing)
        if len(parents) != 2:
            raise ValueError('the fixed control cannot be attributed to an accepted tool merge')
        allowed.add(parents[1])
    if tool not in allowed or case.get('argv') != [
            'in-process', 'execution main role and landing (a1_conformance.n10_n11)']:
        raise ValueError('the fixed control ran at a different tool or invocation')
    config_bytes = _rep_input(repo, scope['configuration'], fixed_commit, fixed_path)
    config = json.loads(config_bytes)
    delegation = scope['delegation']
    delegation_bytes = _rep_input(repo, delegation, fixed_commit, config['delegation']['path'])
    if config_bytes != ev.text('configuration.json') or delegation_bytes != ev.text('delegation.json') or \
            _rep_ref(delegation) != _rep_ref(config['delegation']):
        raise ValueError('the retained configuration or delegation differs from its fixed Git input')
    builder = {k: v for k, v in scope['builder'].items() if k != 'imports'}
    source = _rep_input(repo, builder, tool, REP_BUILDER)
    _rep_input(repo, scope['runner'], tool, 'tools/ledger_coverage/adapters/a1_conformance.py')
    if [r['blob_sha256'] for r in config['tool']['files'] if r['path'] == REP_BUILDER] != [builder['blob_sha256']] or \
            _rep_imports(source) - {'hashlib', 'json'}:
        raise ValueError('the fixed config does not pin the actual representative builder')
    copies = []
    for name, path, oid in (('ledger', REP_LEDGER, REP_LEDGER_GIT), ('edits', REP_EDITS, REP_EDITS_GIT)):
        source_entry, raw = _rep_entry(repo, tool, path)
        observed, copy_path = scope['inputs'][name], S11_A1_DIRECTORY + '/' + name + '.json'
        if (source_entry['mode'], source_entry['git_blob']) != ('100644', oid) or observed['path'] != path or \
                observed['copy_at'] != copy_path or any(observed[k] != v for k, v in source_entry.items()) or \
                len(observed['copies']) != 3 or any(
                    (c['path'], c['mode'], c['git_blob']) != (copy_path, '100644', oid) for c in observed['copies']):
            raise ValueError('the fixed control changes a pinned %s source or copy' % name)
        copies.append(raw)
    ledger, H, M = json.loads(copies[0]), scope['H_rep'], scope['M']
    if (scope['E'], H, M) != (REP_E, ledger['base'], '8e9b83341cf5bc7fd9fb260892d0385fc9bfab4d') or \
            config['roles']['scientific_base'] != H or config['roles']['record_commit'] != H or \
            config['roles']['pin'] != REP_E:
        raise ValueError('the fixed representative E, H or M binding differs')
    build = _rep_construction(repo, (H, M, copies[0], copies[1], source, json.loads(delegation_bytes)))
    X, L = scope['X_rep'], scope['L']
    if (X, scope['X_rep_tree'], scope['X_rep_parents']) != (build['commit'], build['tree'], build['parents']) or \
            scope['L_parents'] != [M, X] or scope['landing_pair_delta'] != ['AGENTS.md']:
        raise ValueError('the fixed candidate or comparison landing is misbound')
    agents = scope['AGENTS']
    composed = [c for c in result.get('landing_compositions', []) if c.get('path') == 'AGENTS.md']
    path = 'AGENTS.md'
    h_entry, m_entry = [_rep_entries(repo, c)[path] for c in (H, M)]
    if len(composed) != 1:
        raise ValueError('the fixed result does not retain exactly one AGENTS.md composition')
    want_x, want_l = build['changes'][path]['git_blob'], composed[0]['l']
    if len(agents) != 4 or any(
            (r['commit'], r['path'], r['mode'], r['git_blob']) != (commit, path, mode, oid)
            for r, (commit, mode, oid) in zip(agents, ((H, *h_entry), (M, *m_entry),
                                                      (X, '100644', want_x), (L, '100644', want_l)))):
        raise ValueError('the AGENTS.md comparison uses substituted entries')
    if want_l != (want_x if rid == 'N10' else composed[0]['composed_blob']):
        raise ValueError('the fixed landing no longer has its prescribed AGENTS.md operand')
    read = scope['read_scope']
    trace = scope['execution_reads']['paths']
    h_entries, m_entries = _rep_entries(repo, H), _rep_entries(repo, M)
    ledgered, side = set(ledger['files']), _first_parent_delta(h_entries, m_entries)
    x_entries = dict(h_entries)
    x_entries.update({p: (e['mode'], e['git_blob']) for p, e in build['changes'].items()})
    patterns = [re.compile(p) for p in config['corpus'].get('patterns', [])]
    exact = set(config['corpus'].get('paths', []))
    corpus = {p for table in (h_entries, m_entries, x_entries) for p, (mode, _) in table.items()
              if mode != '160000' and (p in exact or any(rx.search(p) for rx in patterns))}
    inherited = {oid for mode, oid in h_entries.values() if mode != '160000'} | {REP_LEDGER_GIT, REP_EDITS_GIT}
    by_id = set(scope['execution_reads']['blobs']) - inherited
    read_paths = set(trace.get(X, [])) | {p for p, (_, oid) in x_entries.items() if oid in by_id}
    if (scope['ledgered_paths'] != sorted(ledgered) or scope['side_change_paths'] != sorted(side) or
            scope['corpus_paths'] != sorted(corpus) or 'AGENTS.md' not in read_paths or
            read['paths'] != sorted(read_paths) or read['read_at_X_rep'] != len(read_paths) or
            read['outside_scope'] or read_paths - ledgered - side - corpus):
        raise ValueError('the fixed reconciliation path-read scope differs')


def _representative_read_scope(repo, config, ledger, edits, x, observed):
    origin = json.loads(ledger)
    base = {p: oid for p, (mode, oid) in _rep_entries(repo, origin['base']).items() if mode in REGULAR_MODES}
    paths = {**base, **{p: e['git_blob'] for p, e in x['changes'].items()}}
    excluded = set(base.values()) | {_git_oid('blob', ledger), _git_oid('blob', edits)}
    trace = observed['read_trace']
    path_reads, blob_reads = trace['paths'], trace['blobs']
    if (path_reads != sorted(set(path_reads)) or blob_reads != sorted(set(blob_reads)) or
            not all(HEX40.fullmatch(oid) for oid in blob_reads)):
        return False
    x_blobs = set(blob_reads) - excluded
    reads = set(path_reads) | {p for p, oid in paths.items() if oid in x_blobs}
    scope = set(origin['files']) | set(config['corpus'].get('paths', []))
    patterns = [re.compile(s) for s in config['corpus'].get('patterns', [])]
    return (bool(reads) and sorted(reads) == observed['read_paths'] and
            all(p in paths and (p in scope or any(rx.search(p) for rx in patterns)) for p in reads))


def _rt_t0_observations(result):
    """Read RT-T0's site, merger and overlap counts from the coverage result."""
    historical, retirement = result['segments']
    E, H, X = historical['from'], historical['to'], retirement['to']
    if (E != REP_E or not all(isinstance(c, str) and HEX40.fullmatch(c) for c in (H, X)) or
            retirement['from'] != H or result['evaluated'] != {'commit': X} or
            (historical['kind'], retirement['kind']) != ('hp', 'ledgered') or
            (historical['name'], retirement['name']) != (E[:8] + '..' + H[:8], H[:8] + '..' + X[:8])):
        raise ValueError('RT-T0 coverage does not retain the exact E..H and H..X segments')

    moved, unchanged = 0, 0
    groups, peers, by_site, splices = {}, {}, {}, set()
    for site in result['sites']:
        sid = site['site_id']
        if (sid in by_site or not re.fullmatch(re.escape(site['file']) + r':[1-9][0-9]*@' + E[:8], sid)):
            raise ValueError('RT-T0 repeats or misidentifies a pinned site')
        by_site[sid] = site
        statuses = [(s['segment'], s['status']) for s in site['statuses']]
        if [segment for segment, _ in statuses] not in ([], [historical['name']],
                                                         [historical['name'], retirement['name']]):
            raise ValueError('RT-T0 case has unknown, repeated or misordered site segments')
        moved += (retirement['name'], 'moved') in statuses
        unchanged += (retirement['name'], 'unchanged') in statuses
        region, line = site['region_splices'], site['line_splices']
        if (not isinstance(region, list) or not isinstance(line, list) or
                not all(isinstance(s, str) and s for s in region + line) or
                region != sorted(set(region)) or line != sorted(set(line)) or not set(line) <= set(region) or
                site['hp_overlap'] is not bool(region)):
            raise ValueError('RT-T0 region and line overlap observations disagree')
        splices.update(region)
        group = site['region_shared_with']
        if group is not None:
            identity = site['file'], group['step'], group['region_sha256']
            groups.setdefault(identity, set()).add(sid)
            peers[sid] = group['with']
    if (not isinstance(result['merger_groups'], list) or sorted(result['merger_groups']) !=
            sorted(list(group) for group in groups) or any(
                peers[sid] != sorted(members - {sid}) or len(members) < 2
                for members in groups.values() for sid in members)):
        raise ValueError('RT-T0 reported mergers disagree with their reciprocal site memberships')

    overlaps = set()
    for item in result['items']:
        if item['obligation'] == 'RET' and item['class'] == 'untracked-hp-overlap':
            sid = item['subject']
            site = by_site[sid]
            if (sid in overlaps or item['segment'] != retirement['name'] or item['decision'] != 'FAIL' or
                    item['file'] != site['file'] or not site['region_splices'] or
                    item['splices'] != site['region_splices'] or item['hp_overlap'] is not True):
                raise ValueError('RT-T0 retirement finding does not bind the same site region and segment')
            overlaps.add(sid)
    if overlaps != {sid for sid, site in by_site.items() if site['region_splices']}:
        raise ValueError('RT-T0 has unaccounted region overlaps')
    return {
        'sites[moved_in=H..X]': moved,
        'site_counts:unchanged': unchanged + moved,
        'merger_groups': len(groups),
        'sites[region_shared_with_nonempty]': len(peers),
        'region_splices_distinct': len(splices),
        'items[obligation=RET,class=untracked-hp-overlap,attribution=line]':
            sum(bool(by_site[sid]['line_splices']) for sid in overlaps),
    }, {sid.rsplit('@', 1)[0]: by_site[sid]['region_splices'] for sid in peers}


def _rt_t0_case_bound(case, result, observed, ctx):
    """Bind the fixed adverse coverage run independently of the live RT-T inputs."""
    repo = ctx.repo
    fixed, sep, path = (ctx.fixed_config or '').partition(':')
    if not sep or not HEX40.fullmatch(fixed) or fixed == ctx.freeze:
        return False
    config_bytes = _rep_input(repo, observed['config'], fixed, path)
    config = json.loads(config_bytes)
    T = git_blob_id(repo, 'HEAD^{commit}')
    copies = []
    for name, oid in ((REP_LEDGER, REP_LEDGER_GIT), (REP_EDITS, REP_EDITS_GIT), (REP_BUILDER, None)):
        ref, raw = _rep_entry(repo, T, name)
        if ref != _rep_entry(repo, ctx.tool_landing, name)[0] or (oid is not None and ref['git_blob'] != oid):
            return False
        copies.append(raw)
    ledger, edits, builder = copies
    H = json.loads(ledger)['base']
    roles = config['roles']
    if (roles['pin'], roles['scientific_base'], roles['record_commit']) != (REP_E, H, H):
        return False
    _rep_walk(repo, REP_E, H)
    spec = config['adapters']['ledger']
    edit_pins = [r for r in spec['companion'] if r['role'] == 'edits']
    if (_rep_ref(spec) != {'path': REP_LEDGER, 'blob_sha256': _file_sha(ledger)} or
            len(edit_pins) != 1 or _rep_pin(repo, edit_pins[0].get('commit') or T, _rep_ref(edit_pins[0])) != edits):
        return False
    delegation = config['delegation']
    contract = _rep_pin(repo, delegation.get('commit') or fixed, _rep_ref(delegation))
    built = _rep_construction(repo, (H, ctx.rep_main, ledger, edits, builder, json.loads(contract)))
    X = built['commit']
    observed_cfg = result['config']
    invocation = ['coverage', '--config', fixed + ':' + path, '--commit', X, '--check', ITEM2_CHECK,
                  '--segment', REP_E + '..' + H, '--segment', H + '..' + X + '=' + T + ':' + REP_LEDGER]
    argv = list(case['argv'])
    for flag in ('--out', '--repo'):
        if len(_case_args(argv, flag) or []) != 1:
            return False
        i = argv.index(flag)
        del argv[i:i + 2]
    if (argv != invocation or result['invocation'] != invocation or result['operation'] != 'coverage' or
            result['harness'] is not True or observed_cfg['admission']['mode'] != 'control-harness' or
            (observed_cfg['commit'], observed_cfg['path'], observed_cfg['blob_sha256']) !=
            (fixed, path, _file_sha(config_bytes)) or result['records_used'] or
            [s['from'] for s in result['segments']] != [REP_E, H] or
            [s['to'] for s in result['segments']] != [H, X] or result['evaluated'] != {'commit': X}):
        return False
    checked = [c['profiles'] for c in config['checks'] if c['id'] == ITEM2_CHECK]
    if len(checked) != 1 or set(checked[0]) != set(ITEM2_PROFILES):
        return False
    profiles = []
    for p in config['profiles']:
        source = p['source']
        if ('path' in source or 'blob_sha256' in source) and (p['name'] in checked[0] or p['kind'] == 'deny'):
            _rep_pin(repo, source.get('commit') or fixed, _rep_ref(source))
        profiles.append({'name': p['name'], 'kind': p['kind'], 'source_commit': source.get('commit'),
                         'path': source.get('path'), 'blob_sha256': source.get('blob_sha256'),
                         'pattern_sha256': p['pattern_sha256']})
    denies = {p['name'] for p in profiles if p['kind'] == 'deny'}
    return (bool(denies) and result['profiles'] == profiles and
            result['profiles_evaluated'] == {X: sorted(set(ITEM2_PROFILES) | denies)} and
            result['rule_files'] == [_rep_ref(r) for r in config['rules']] and
            _representative_read_scope(repo, config, ledger, edits, built, observed))


def _rt_d_counts(result, census):
    hits = result.get('hits') if isinstance(result, dict) else None
    other_hits = census.get('hits') if isinstance(census, dict) else None
    if not isinstance(hits, list) or not isinstance(other_hits, list):
        return {}
    coords = lambda hit: (hit['file'], hit['line'])
    other_profiles = {coords(h): set(h['profiles']) - {'resid'} for h in other_hits}
    allowed = {'W1-b', 'W1-c', 'W1-d', 'W2-a', 'W2-b'}
    pass_lines = {coords(h) for h in hits if h['state'] == 'PASS' and
                  isinstance(h.get('rule_id'), str) and h['rule_id'] in allowed}
    resid = {coords(h) for h in hits if h['state'] == 'REVIEW_REQUIRED' and 'resid' in h['profiles']}
    counts = {'lines[state=PASS,rule_id=W1|W2]': len(pass_lines),
              'lines[profile=resid,decision=REVIEW_REQUIRED]': len(resid)}
    if resid <= other_profiles.keys():
        counts['lines[profile=resid,only_profile=true]'] = sum(not other_profiles[p] for p in resid)
    return counts


def _rt_d_scope(repo, F, config, projected):
    """Bind the selected scope and independently check its exact supersession chain."""
    refs = [_rep_ref(r) for r in config['records'] if r.get('kind') == 'scope']
    scopes = [(r, json.loads(_rep_pin(repo, F, r))) for r in refs]
    (ref, scope), = [(r, d) for r, d in scopes if d.get('profile') == 'repo']
    scope_bytes = _rep_input(repo, projected['scope'], F, ref['path'])
    if (_file_sha(scope_bytes) != ref['blob_sha256'] or scope['schema'] != 'oi-scope/1' or
            'supersedes' not in scope or projected['records_used'] != [dict(ref, kind='scope')]):
        raise ValueError('RT-D did not read the exact configured repo scope')
    active = _rep_review_pool(repo, F, config)
    if scope['supersedes'] is None:
        ordinary = [r for r in active if r.get('reviewed') == ref and r.get('kind', 'review') == 'review']
        if not ordinary or not all(r.get('method') and
                                   _rep_review_valid(repo, F, r, ref, scope.get('author'), _reviewed_items(scope)) and
                                   all(v['verdict'] == 'accept' for v in r['verdicts']) for r in ordinary):
            raise ValueError('the RT-D scope lacks qualifying independent review')
        return scope

    config_dir = os.path.dirname(projected['config']['path'])
    record_dirs = [os.path.dirname(r['path']) for r in config['rules'] + config['records']]
    common = os.path.commonpath(record_dirs)
    dirs = tuple(d + '/' if d else '' for d in sorted({config_dir} | ({common} if common else set(record_dirs))))
    chain, holders = _rep_auxiliary_lineage(repo, F, config, ref, 'scope', 'oi-scope/1', dirs)
    history = _rep_review_pool(repo, F, dirs=dirs)
    prior, prior_ref = {}, None
    for current_ref in chain:
        current = json.loads(_rep_pin(repo, holders[current_ref['path'], current_ref['blob_sha256']], current_ref))
        reviews = [r for r in (active if current_ref == ref else history) if r.get('reviewed') == current_ref]
        ordinary = [r for r in reviews if r.get('kind', 'review') == 'review']
        if not ordinary or not all(_rt_d_scope_review_form(r, _reviewed_items(current)) and
                                   _rep_review_valid(repo, F, r, current_ref, current['author'],
                                                     _reviewed_items(current)) for r in ordinary):
            raise ValueError('the RT-D scope lacks a complete independent ordinary review')
        absent = object()
        fields = (prior.keys() | current.keys()) - {'supersedes', 'version'}
        changed = sorted('field:' + k for k in fields if prior.get(k, absent) != current.get(k, absent))
        if prior_ref is not None and changed:
            widening = [r for r in reviews if r.get('kind') == 'widening']
            if (not widening or not all(_rt_d_scope_review_form(r, changed) for r in widening) or
                    not any(r.get('replaces') == prior_ref and
                            _rep_review_valid(repo, F, r, current_ref, current['author'], changed) and
                            all(_independent_of_author(r, o['reviewer']) for o in ordinary) for r in widening)):
                raise ValueError('the RT-D scope lacks a qualifying independent widening review')
        prior, prior_ref = current, current_ref
    return scope


def _rt_d_scope_review_form(review, items):
    required = {'schema', 'reviewer', 'reviewed', 'revision', 'independence', 'method', 'verdicts'}
    if review.get('kind') == 'widening':
        required.add('replaces')
    method, verdicts = review.get('method'), review.get('verdicts')
    return (required <= review.keys() <= required | {'kind', 'dissent'} and
            ('dissent' not in review or isinstance(review['dissent'], str)) and
            isinstance(method, str) and re.search(r'\b[0-9a-f]{40}\b', method) is not None and
            isinstance(verdicts, list) and len(verdicts) == len(items) and
            all(isinstance(v, dict) and set(v) == {'item', 'verdict', 'reason'} and
                isinstance(v['item'], str) and isinstance(v['reason'], str) and
                v['verdict'] == 'accept' for v in verdicts) and {v['item'] for v in verdicts} == set(items))


def _rt_d_repo_pattern(repo, F, specs, projected):
    """Extract the declared repo review pattern independently of the engine."""
    spec = specs['repo']
    source = spec['source']
    if ((spec['kind'], spec['scope'], spec['applies_to']) != ('review', 'repo', 'tree') or
            spec.get('except') or source['extractor'] != {'kind': 'python-ast-assign', 'selector': 'REPO_PAT'}):
        raise ValueError('RT-D requires the declared repo review profile')
    raw = _rep_input(repo, projected['repo_profile_source'], source.get('commit') or F, source['path'])
    nodes = [n.value for n in ast.parse(raw).body if isinstance(n, ast.Assign) and
             any(getattr(t, 'id', None) == 'REPO_PAT' for t in n.targets)]
    if _file_sha(raw) != source['blob_sha256'] or len(nodes) != 1:
        raise ValueError('RT-D repo profile source differs from the pinned input')
    call = nodes[0]
    if not (isinstance(call, ast.Call) and isinstance(call.func, ast.Attribute) and
            isinstance(call.func.value, ast.Name) and call.func.value.id == 're' and call.func.attr == 'compile' and
            len(call.args) == 1 and not call.keywords and isinstance(call.args[0], ast.Constant) and
            isinstance(call.args[0].value, str)):
        raise ValueError('RT-D repo profile is not the declared literal regex')
    pattern = call.args[0].value
    if _file_sha(json.dumps(pattern, ensure_ascii=False).encode()) != spec['pattern_sha256']:
        raise ValueError('RT-D repo profile pattern digest differs')
    return re.compile(pattern)


def _rt_d_projection_bound(repo, F, path, config, ledger, edits, x, primary, census):
    """Check the confined census and reproduce membership from verified Git bytes."""
    case, projected, observed = census
    X = x['commit']
    if (case['argv'] != ['in-process', 'RT-D review membership at residual coordinates'] or
            projected['exit_status'] != 0 or projected['evaluated'] != {'commit': X} or
            _file_sha(_rep_input(repo, projected['config'], F, path)) != primary['config']['blob_sha256']):
        return False
    scope = _rt_d_scope(repo, F, config, projected)
    specs = {p['name']: p for p in config['profiles']}
    review_names = {'p0-core', 'p0-para', 'ledger-ext', 'ptr', 'count-grep', 'resid'}
    names, = [c['profiles'] for c in config['checks'] if c['id'] == 'item7']
    if (primary['profiles_evaluated'] != {X: sorted(names)} or
            {n for n in names if specs[n]['kind'] == 'review'} != review_names or
            any(specs[n]['scope'] != 'corpus' for n in review_names) or specs['resid']['applies_to'] != 'added-text'):
        return False
    rows = [{'name': p['name'], 'kind': p['kind'], 'source_commit': p['source'].get('commit'),
             'path': p['source'].get('path'), 'blob_sha256': p['source'].get('blob_sha256'),
             'pattern_sha256': p['pattern_sha256']} for p in config['profiles']]
    if primary['profiles'] != rows:
        return False
    for n in review_names:
        source = specs[n]['source']
        if source['extractor']['kind'] != 'literal-list':
            _rep_pin(repo, source.get('commit') or F, _rep_ref(source))
    matcher = _rt_d_repo_pattern(repo, F, specs, projected)
    residual = [h for h in primary['hits'] if h['state'] == 'REVIEW_REQUIRED' and 'resid' in h['profiles']]
    wanted = sorted({h['file'] for h in residual})
    if (not wanted or observed['read_paths'] != wanted or observed['read_trace']['paths'] != wanted or
            not _representative_read_scope(repo, config, ledger, edits, x, observed)):
        return False
    ex_prefix, ex_files = tuple(scope.get('exclude_prefixes', [])), set(scope.get('exclude_files', []))
    allow = [re.compile(p) for p in scope.get('include_patterns_within_excluded', [])]
    exclude = [re.compile(p) for p in scope.get('exclude_patterns', [])]
    retained = json.loads(ledger)
    splices = {p: [] for p in wanted}
    for splice in retained['splices']:
        if splice['file'] in splices:
            splices[splice['file']].append(splice)
    texts, image_lines, selected = {}, {}, []
    for p in wanted:
        _, raw = _rep_entry(repo, retained['base'], p)
        raw = _rep_spliced(raw, p, retained)
        if p in x['changes'] and _file_sha(raw) != x['changes'][p]['blob_sha256']:
            return False
        if b'\r' in raw:
            return False
        rows = raw.decode('utf-8').split('\n')
        texts[p] = rows[:-1] if not raw or raw.endswith(b'\n') else rows
        shift = 0
        image_lines[p] = set()
        for splice in sorted(splices[p], key=lambda s: (s['start'], s['end'])):
            start, length = splice['start'] + shift, len(splice['new'].encode())
            shift += length - (splice['end'] - splice['start'])
            if length:
                first = raw.count(b'\n', 0, start) + 1
                last = raw.count(b'\n', 0, start + length - 1) + 1
                image_lines[p].update(range(first, last + 1))
        if not (p in ex_files or any(rx.search(p) for rx in exclude) or b'\x00' in raw or
                (p.startswith(ex_prefix) and not any(rx.search(p) for rx in allow))):
            selected.append(p)
    selected_set = set(selected)
    expected, seen = [], set()
    for h in residual:
        p, n, names = h['file'], h['line'], set(h['profiles'])
        if ((p, n) in seen or not (type(n) is int and n in image_lines[p] and 1 <= n <= len(texts[p])) or
                not names <= review_names or h['tree'] != X):
            return False
        seen.add((p, n))
        text = texts[p][n - 1]
        if _file_sha(text.encode()) != h['line_sha256']:
            return False
        if p in selected_set and matcher.search(text):
            names.add('repo')
        expected.append({'file': p, 'line': n, 'line_sha256': h['line_sha256'], 'profiles': sorted(names)})
    return projected['selected_paths'] == selected and projected['hits'] == expected


def _fixed_item7a(result, ctx):
    """Derive the original Item 7 counts and retired-line predicate from the actual payload."""
    items = result['items']
    line_deny = {(i['file'], i['line']) for i in items if i['class'] == 'deny-match' and i['level'] == 'line'}
    sentences = {(i['file'], n) for i in items if i['class'] == 'deny-match' and i['level'] == 'sentence'
                 for n in range(i['line'], i['last_line'] + 1)}
    unclassified = {(i['file'], i['line']) for i in items if i['class'] == 'final-unclassified'
                    and i['decision'] == 'FAIL'}
    counts = {'lines[class=deny-match]': len(line_deny), 'lines[class=final-unclassified]': len(unclassified),
              'fail_lines': len(line_deny | unclassified),
              'lines[class=deny-match,count_sentence_lines=true]': len(line_deny | sentences),
              'fail_lines[count_sentence_lines=true]': len(line_deny | sentences | unclassified)}
    T = ctx.tool_candidate or ctx.tool_landing
    repo = ctx.repo
    _, raw = _rep_entry(repo, T, REP_LEDGER)
    if _git_oid('blob', raw) != REP_LEDGER_GIT:
        raise ValueError('the fixed Item 7 ledger does not match the adopted control copy')
    ledger = json.loads(raw)
    H = ledger['base']
    retired = set()
    if result['evaluated']['commit'] == H:
        pattern = re.compile(r'\bA1\b|Fourteen|six structural|sixth of')
        for p, entry in _rep_entries(repo, H).items():
            if not re.fullmatch(r'(book|papers)/[^/]+\.md', p):
                continue
            _, body = _rep_blob(repo, entry)
            after = _rep_spliced(body, p, ledger) if p in ledger['files'] else body
            current = set(after.decode('utf-8').splitlines())
            retired.update((p, n) for n, line in enumerate(body.decode('utf-8').splitlines(), 1)
                           if pattern.search(line) and line not in current and (p, n) not in line_deny)
        counts['retired_lines'] = len(retired)
    return counts, bool(retired) and retired <= unclassified, unclassified


FIXED_TERMS_ROWS = frozenset(('RT-DR3W', 'RT-I7', 'RT-I7A'))
FIXED_DR3_H = '12a9281fb88c14395b6715a3bf4b4f6b030f433c'
FIXED_DR3_H_SHA = 'd87acac54b5f6392af3323630236d98b14bb4d485d10c0ff56b20806b0883e27'
FIXED_DR3_X_SHA = '59b68984e659ef808819e02d4653d80388f8bd2f4c009796b162fc2453882ce2'
FIXED_DR3_CASE = 'AGENTS.md at H (control input agents-md-at-H)'
FIXED_X_CASE = 'at X_rep (R6.EVID.8)'
FIXED_DENY_PROFILES = ['DR-1', 'DR-3', 'DR-4', 'DR-5']
FIXED_ITEM7_PROFILES = ['p0-core', 'p0-para', 'ledger-ext', 'ptr', 'count-grep', 'resid'] + FIXED_DENY_PROFILES


def _fixed_terms_inputs(ctx, phase, ev):
    repo, scope = ctx.repo, ev.json('fixed-inputs.json')
    C, sep, path = (ctx.fixed_config or '').partition(':')
    if not sep or not HEX40.fullmatch(C) or scope.get('scope') != 'fixed representative terminology control':
        raise ValueError('the exact fixed terminology scope or configuration is missing')
    tool = scope['tool']
    allowed = {ctx.tool_candidate} if phase == 'tool-acceptance' else {git_blob_id(repo, 'HEAD^{commit}')}
    if phase == 'candidate-F':
        _, parents = _rep_commit(repo, ctx.tool_landing)
        if len(parents) != 2:
            raise ValueError('the exact accepted tool merge is missing')
        allowed.add(parents[1])
    if tool not in allowed or scope['M'] != C:
        raise ValueError('the fixed terminology tool or marker comparison tree has been substituted')
    config = json.loads(_rep_input(repo, scope['configuration'], C, path))
    led = _rep_input(repo, scope['ledger'], tool, REP_LEDGER)
    edits = _rep_input(repo, scope['edits'], tool, REP_EDITS)
    H = json.loads(led)['base']
    if (_git_oid('blob', led), _git_oid('blob', edits), scope['H_rep'], scope['E']) != (
            REP_LEDGER_GIT, REP_EDITS_GIT, H, REP_E) or \
            (config['roles']['scientific_base'], config['roles']['record_commit'], config['roles']['pin']) != (
                H, H, REP_E):
        raise ValueError('the fixed E, H, ledger or edit input differs from its adopted pin')
    _rep_walk(repo, REP_E, H)
    for name in ('delegation', 'controls'):
        spec = config[name]
        raw = _rep_input(repo, scope[name], spec.get('commit') or C, spec['path'])
        if _rep_ref(spec) != _rep_ref(scope[name]):
            raise ValueError('the fixed %s differs from its configuration pin' % name)
        if name == 'delegation':
            delegation = json.loads(raw)
        else:
            controls = json.loads(raw)
    builder = _rep_input(repo, scope['builder'], tool, REP_BUILDER)
    runner = 'tools/ledger_coverage/adapters/a1_controls.py'
    _rep_input(repo, scope['runner'], tool, runner)
    pins = {r['path']: r['blob_sha256'] for r in config['tool']['files']}
    if ({p: pins.get(p) for p in (REP_BUILDER, runner)} !=
            {REP_BUILDER: _file_sha(builder), runner: scope['runner']['blob_sha256']} or
            _rep_imports(builder) - {'hashlib', 'json'}):
        raise ValueError('the fixed configuration does not pin the actual runner and representative builder')
    build = _rep_construction(repo, (H, C, led, edits, builder, delegation))
    if (scope['X_rep'], scope['X_rep_tree'], scope['X_rep_parents'], scope['build_reads']) != (
            build['commit'], build['tree'], build['parents'], build['reads']):
        raise ValueError('the exact representative candidate or its H/M reads differ')
    return scope, config, controls, build, led, edits


def _fixed_profile_source(repo, commit, spec, paths):
    source = spec['source']
    if source['extractor']['kind'] == 'literal-list':
        return None
    revision = source.get('commit') or commit
    if source['path'] not in paths.get(revision, ()):
        raise ValueError('missing read of the exact %s profile source' % spec['name'])
    return _rep_pin(repo, revision, _rep_ref(source))


def _fixed_dr3w_case(repo, C, H, X, case, result, config, controls, build):
    subject = H if case['case'] in (FIXED_DR3_CASE, 'restored') else X
    path = 'AGENTS.md'
    refs = {r['id']: r for r in controls['control_inputs']}
    witness = {'id': 'agents-md-at-H', 'commit': H, 'path': path,
               'blob': FIXED_DR3_H, 'sha256': FIXED_DR3_H_SHA}
    counter = {'id': 'agents-md-at-Xrep', 'path': path, 'candidate': 'X_rep (R6.EVID.8)',
               'sha256': FIXED_DR3_X_SHA}
    entry = _rep_entry(repo, H, path)[0] if subject == H else build['changes'][path]
    if (refs[witness['id']] != witness or refs[counter['id']] != counter or
            entry['blob_sha256'] != (FIXED_DR3_H_SHA if subject == H else FIXED_DR3_X_SHA) or
            (subject == H and entry['git_blob'] != FIXED_DR3_H) or
            result['input'] != dict(entry, path=path, commit=subject) or
            case['argv'] != ['in-process', 'DR-3 fixed sentence scan']):
        raise ValueError('the exact DR-3 witness or countercase input differs')
    profile = next(p for p in config['profiles'] if p['name'] == 'DR-3')
    raw = _fixed_profile_source(repo, C, profile, result['paths_by_commit'])
    source = profile['source']
    if (source['extractor'] != {'kind': 'json-pointer', 'selector': '/rules/1/patterns'} or
            source['path'] != AUDIT_DIR + 'rules/dr-deny-v1.json' or
            profile.get('combine') != 'all' or profile.get('levels') != ['sentence'] or
            profile.get('kind') != 'deny' or config['sentence']['splitter_version'] != 2):
        raise ValueError('the approved DR-3 sentence profile differs')
    deny = json.loads(raw)['rules'][1]
    patterns = json.dumps(deny['patterns'], sort_keys=True, separators=(',', ':'), ensure_ascii=False).encode()
    observed = {'spec': profile, 'pattern_sha256': _file_sha(patterns)}
    source_rev = source.get('commit') or C
    reads = {subject: [path], source_rev: [source['path']]}
    if source_rev == subject:
        reads[subject] = sorted((path, source['path']))
    positive = {'file': path, 'line': 37, 'sentence': '37:39', 'sentence_start_line': 37,
                'sentence_end_line': 39, 'rule_id': 'DR-3'}
    if (deny['id'] != 'DR-3' or observed['pattern_sha256'] != profile['pattern_sha256'] or
            result['profile'] != observed or result['paths_by_commit'] != reads or
            result['read_trace'] != {'paths': reads[subject], 'blobs': []} or
            result['items'] != ([positive] if subject == H else [])):
        raise ValueError('the observed DR-3 profile, read paths or sentence spans differ')


def _fixed_terms_case(ctx, phase, rid, ev, case, result, observed):
    scope, cfg, controls, build, led, edits = _fixed_terms_inputs(ctx, phase, ev)
    repo, C, path, H, X = ctx.repo, scope['configuration']['commit'], scope['configuration']['path'], \
        scope['H_rep'], scope['X_rep']
    name = case['case']
    if case['mutation'] != []:
        raise ValueError('the fixed case carries an unprescribed mutation')
    if rid == 'RT-DR3W':
        _fixed_dr3w_case(repo, C, H, X, case, result, cfg, controls, build)
        return
    subject = X if name == FIXED_X_CASE or (name == 'restored' and rid == 'RT-I7A') else H
    expected = ['terms', '--config', C + ':' + path, '--commit', subject]
    adapters = cfg['adapters']['ledger']
    ledger_paths = set()
    if rid == 'RT-I7':
        names = ['item7-literal']
        expected += ['--profile', 'item7-literal']
    elif name == 'retired deny profile census':
        names = FIXED_DENY_PROFILES
        expected += ['--profile', ','.join(names)]
    else:
        names = FIXED_ITEM7_PROFILES
        pinned_led = adapters.get('commit') or C
        expected += ['--base', H, '--ledger', pinned_led + ':' + REP_LEDGER, '--check', 'item7', '--final']
        checks = [c for c in cfg['checks'] if c['id'] == 'item7']
        companions = [r for r in adapters['companion'] if r['role'] == 'edits']
        if (checks != [{'id': 'item7', 'profiles': names, 'final_profiles': ['ptr', 'count-grep']}] or
                adapters['path'] != REP_LEDGER or len(companions) != 1 or companions[0]['path'] != REP_EDITS):
            raise ValueError('the adopted item7 check or copied ledger adapter inputs differ')
        companion = companions[0]
        if (_rep_pin(repo, pinned_led, _rep_ref(adapters)) != led or
                _rep_pin(repo, companion.get('commit') or pinned_led, _rep_ref(companion)) != edits or
                REP_LEDGER not in observed['paths_by_commit'].get(pinned_led, ()) or
                REP_EDITS not in observed['paths_by_commit'].get(companion.get('commit') or pinned_led, ())):
            raise ValueError('the item7 scan did not read the exact ledger and companion edits')
        ledger_paths = set(json.loads(led)['files'])
        if subject == X and observed['paths_by_commit'].get(H) != sorted(ledger_paths):
            raise ValueError('the item7 candidate scan does not retain the complete H-ledger read scope')
    invocation = list(case['argv'])
    for flag in ('--out', '--repo'):
        if len(_case_args(invocation, flag) or []) != 1:
            raise ValueError('the fixed scan invocation has malformed path arguments')
        i = invocation.index(flag)
        del invocation[i:i + 2]
    info = result['config']
    if (invocation != expected or result['invocation'] != expected or result['operation'] != 'terms' or
            result['evaluated'] != {'commit': subject} or
            (info['commit'], info['path'], info['blob_sha256']) != (C, path, scope['configuration']['blob_sha256']) or
            info['admission']['mode'] != 'control-harness' or result.get('harness') is not True or
            result['records_used'] != [] or result['control'] != 'rule files replaced in memory by the control' or
            observed['rule_selection_inputs'] != [result['rule_files']] or
            result['rule_files'] != [_rep_ref(r) for r in cfg['rules']]):
        raise ValueError('the actual terms invocation, configuration or fixed rule selection differs')
    reads_by_commit = observed['paths_by_commit']
    if path not in reads_by_commit.get(C, ()) or observed['read_trace']['paths'] != reads_by_commit.get(subject):
        raise ValueError('the actual configuration or evaluated read trace is absent')
    profile_records = []
    for spec in cfg['profiles']:
        source = spec['source']
        _fixed_profile_source(repo, C, spec, reads_by_commit)
        if spec.get('except'):
            _fixed_profile_source(repo, C, dict(spec['except'], name=spec['name'] + ' exclusion'), reads_by_commit)
        profile_records.append({'name': spec['name'], 'kind': spec['kind'], 'path': source.get('path'),
                                'source_commit': source.get('commit'), 'blob_sha256': source.get('blob_sha256'),
                                'pattern_sha256': spec['pattern_sha256']})
    if rid == 'RT-I7':
        literal = next(p for p in cfg['profiles'] if p['name'] == 'item7-literal')
        if (literal['source']['extractor'] != {'kind': 'literal-list', 'selector': ['Fourteen', 'six structural',
                                                                                 'sixth of']} or
                literal['kind'] != 'countercontrol' or literal.get('report_regex') != r'\bA1\b'):
            raise ValueError('the literal countercontrol profile differs')
    if result['profiles'] != profile_records or result['profiles_evaluated'] != {subject: sorted(names)}:
        raise ValueError('the reported evaluated profiles differ from the fixed source and pattern pins')
    entries = _rep_entries(repo, H)
    patterns = [re.compile(p) for p in cfg['corpus'].get('patterns', [])]
    exact = set(cfg['corpus'].get('paths', []))
    allowed = {p for p in entries.keys() | (build['changes'].keys() if subject == X else set())
               if p in exact or any(rx.search(p) for rx in patterns)}
    if (not allowed or result['covered_paths'] != sorted(allowed) or
            observed['read_paths'] != sorted(allowed | ledger_paths) or
            not _representative_read_scope(repo, cfg, led, edits, build if subject == X else {'changes': {}}, observed)):
        raise ValueError('the fixed terms path reads do not cover exactly the applicable corpus and ledger scope')


def _candidate_case_bound(rid, case, result, observed, ctx, *, census=None):
    """Check exact candidate-F operands independently of the runner's status."""
    F, path, digest, _ = s11_binding(ctx)
    repo, argv = ctx.repo, case.get('argv')
    config = json.loads(_rep_pin(repo, F, {'path': path, 'blob_sha256': digest}))
    info = result['config']
    if (info.get('path'), info.get('blob_sha256')) != (path, digest) or \
            _case_args(argv, '--config') != [F + ':' + path]:
        return False
    invocation = list(argv)
    for flag in ('--out', '--repo'):
        if len(_case_args(argv, flag) or []) != 1:
            return False
        i = invocation.index(flag)
        del invocation[i:i + 2]
    if result.get('invocation') != invocation:
        return False
    if rid in ('RT-D', 'RT-D-gr58'):
        T, M, S = ctx.tool_landing, ctx.rep_main, ctx.rep_snapshot
        snapshot = observed['representative_binding']
        if (snapshot['freeze'], snapshot['T_land'], snapshot['M_rep'], snapshot['S']) != (F, T, M, S):
            return False
        _rep_role_selection(config, snapshot['class_tip'], snapshot['allow_tip'])
        _rep_pin(repo, F, snapshot['allow_tip'])
        _, ledger = _rep_entry(repo, T, REP_LEDGER)
        _, edits = _rep_entry(repo, T, REP_EDITS)
        _, builder = _rep_entry(repo, T, REP_BUILDER)
        _, template = _rep_entry(repo, T, REP_TEMPLATE)
        if _git_oid('blob', ledger) != REP_LEDGER_GIT or _git_oid('blob', edits) != REP_EDITS_GIT:
            return False
        rep_h = json.loads(ledger)['base']
        delegation = json.loads(_rep_pin(repo, T, _rep_ref(json.loads(template)['delegation'])))
        x = _rep_construction(repo, (rep_h, M, ledger, edits, builder, delegation))
        hit = F + ':' + AUDIT_DIR + 'records/gr58-hit-classification-v3.json'
        if (argv[0] != 'terms' or result.get('operation') != 'terms' or
                result.get('evaluated') != {'commit': x['commit']} or
                _case_args(argv, '--commit') != [x['commit']] or _case_args(argv, '--base') != [rep_h] or
                _case_args(argv, '--ledger') != [T + ':' + REP_LEDGER] or
                result.get('rule_files') != [_rep_ref(r) for r in config['rules']]):
            return False
        valid = (_case_args(argv, '--profile') == [] and _case_args(argv, '--scope') == [] and
                 _case_args(argv, '--check') == ['item7'])
        classified = [hit] if rid == 'RT-D-gr58' else []
        return (valid and _case_args(argv, '--classify') == classified and
                _representative_read_scope(repo, config, ledger, edits, x, observed) and
                (census is None or _rt_d_projection_bound(repo, F, path, config, ledger, edits, x, result, census)))
    if rid == 'TR5':
        adm = info['admission']
        snap = adm['snapshot']
        run = snap['run']
        T = snap['tool_commit']
        _, prereg = _rep_entry(repo, F, S11_A1_DIRECTORY + '/PREREG.md')
        if (argv[0] != 'terms' or result.get('operation') != 'terms' or
                _case_args(argv, '--freeze') != [F] or adm['mode'] != 'chain' or result.get('harness') or
                snap['freeze'] != F or snap['configuration'] != {'path': path, 'blob_sha256': digest} or
                snap['pin_table'] != {'path': S11_A1_DIRECTORY + '/PREREG.md', 'blob_sha256': _file_sha(prereg)} or
                run.get('head_sha') != T or run.get('event') != 'workflow_dispatch' or
                run.get('head_branch') != 'main' or run.get('workflow_path') != WORKFLOW_PATH or
                run.get('repository_id') != config['repository_id'] or
                run.get('head_repository_id') != config['repository_id'] or not run.get('run_id') or
                snap.get('workflow') != config['tool']['workflow'] or snap.get('evaluated') != result.get('evaluated') or
                snap.get('invocation') != invocation):
            return False
        _rep_walk(repo, T, ctx.main_tip)
        _rep_tool_image(repo, T, config)
        reviews = snap['configuration_review']
        config_ref = {'path': path, 'blob_sha256': digest}
        if not reviews or snap.get('tool_blobs') != {r['path']: r['blob_sha256'] for r in config['tool']['files']}:
            return False
        ordinary = []
        for ref in reviews:
            if ref != _rep_plan_pin(repo, F, os.path.basename(ref['path'])):
                return False
            review = json.loads(_rep_pin(repo, F, ref))
            if review.get('schema') == 'oi-review-record/1' and review.get('kind', 'review') == 'review' and \
                    review.get('reviewed') == config_ref:
                ordinary.append(review)
        return bool(ordinary) and all(
            r.get('method') and _rep_review_valid(repo, F, r, config_ref, config.get('author'), _reviewed_items(config))
            for r in ordinary)

    evaluated = result['evaluated']['commit']
    H = config['roles']['scientific_base']
    if (not isinstance(evaluated, str) or not HEX40.fullmatch(evaluated) or not argv or argv[0] != 'coverage' or
            _case_args(argv, '--freeze') != [F] or info.get('admission', {}).get('mode') != 'chain' or
            _case_args(argv, '--check') != [ITEM2_CHECK] or _case_args(argv, '--commit') != [evaluated] or
            _case_args(argv, '--segment') != [REP_E + '..' + H,
                                              H + '..' + evaluated + '=' + F + ':' + S11_A1_DIRECTORY + '/ledger.json']):
        return False
    refs = [r for r in config['records'] if r.get('kind') in SEC82_KINDS]
    if {r['kind'] for r in refs} != SEC82_KINDS:
        return False
    hp = [F + ':' + r['path'] for r in refs if r['kind'] == 'hp']
    classifications = [F + ':' + r['path'] for r in refs if r['kind'] != 'hp']
    if len(hp) != 1 or _case_args(argv, '--hp') != hp or \
            sorted(_case_args(argv, '--classify') or []) != sorted(classifications):
        return False
    reviews = _rep_review_pool(repo, F, config)
    used = {(r['path'], r['blob_sha256']) for r in result['records_used']}
    for r in refs:
        ref = _rep_ref(r)
        record = json.loads(_rep_pin(repo, F, ref))
        if (r['path'], r['blob_sha256']) not in used or not any(
                rv.get('kind', 'review') == 'review' and rv.get('reviewed') == ref and rv.get('method') and
                _rep_review_valid(repo, F, rv, ref, record.get('author'), _reviewed_items(record)) and
                all(v['verdict'] == 'accept' for v in rv['verdicts']) for rv in reviews):
            return False
    inputs = observed['representative_inputs']
    if (inputs['H'], inputs['E']) != (H, REP_E) or not config['roles'].get('pin') == REP_E or \
            sorted(r['path'] for r in inputs['records']) != sorted(r['path'] for r in refs):
        return False
    _rep_input(repo, inputs['config'], F, path)
    for operand in inputs['records']:
        _rep_input(repo, operand, F)
    pinned = [_rep_plan_pin(repo, F, name + '.json') for name in ('ledger', 'edits')]
    ledger, edits = [_rep_input(repo, inputs[name], F, ref['path']) for name, ref in zip(('ledger', 'edits'), pinned)]
    if any(_rep_ref(inputs[name]) != ref for name, ref in zip(('ledger', 'edits'), pinned)):
        return False
    delegation = json.loads(_rep_pin(repo, F, _rep_ref(config['delegation'])))
    _, builder = _rep_entry(repo, git_blob_id(repo, 'HEAD^{commit}'), REP_BUILDER)
    x = _rep_construction(repo, (H, ctx.rep_main, ledger, edits, builder, delegation))
    return evaluated == x['commit'] and _representative_read_scope(repo, config, ledger, edits, x, observed)


def s11_standin(F, P, b):
    """standin(F, P, b): the id the runner's in-memory stand-in for F carries (sec. 2 of the supplement)."""
    h = hashlib.sha1()
    h.update(S11_STANDIN_SUBJECT.encode('utf-8'))
    h.update(F.encode('ascii'))
    h.update(P.encode('utf-8') + b'\x00' + ('100644:' + b).encode('ascii'))
    h.update(F.encode('ascii'))
    return h.hexdigest()


def s11_binding(ctx):
    """(F, P, S, b) of the configuration admitted at F, derived without reading either run's result or argv: F the
    gate's --freeze, equal to the commit under check; P the gate's --config, in the admitted A1 record directory; S the
    SHA-256 F's pin table (the last Record pins subsection of the PREREG.md beside P, R6.REC.16) lists for P's file,
    in exactly one row; b the git blob id of the regular entry F:P, whose bytes hash to S. None on any failure."""
    if ctx is None or not (ctx.repo and ctx.freeze and ctx.config_path and ctx.commit):
        return None
    F, P = ctx.freeze, ctx.config_path
    if not HEX40.match(F) or F != ctx.commit or '/' not in P or P.rsplit('/', 1)[0] != S11_A1_DIRECTORY:
        return None
    d, name = P.rsplit('/', 1)
    pe = git_entry(ctx.repo, F, d + '/PREREG.md')
    if pe is None or pe[0] not in ('100644', '100755'):
        return None
    prereg = git_show(ctx.repo, pe[1])
    if prereg is None:
        return None
    rows = [h for f, h in last_pin_rows(prereg) or () if f == name]
    if len(rows) != 1 or not re.fullmatch('[0-9a-f]{64}', rows[0]):
        return None
    S = rows[0]
    ce = git_entry(ctx.repo, F, P)
    if ce is None or ce[0] not in ('100644', '100755'):
        return None
    data = git_show(ctx.repo, ce[1])
    if data is None or hashlib.sha256(data).hexdigest() != S:
        return None
    return F, P, S, ce[1]


def s11_run_bound(argv, result, binding):
    """One S11-2a run bound to (F, P, S): its result's config names P and S, and its argv carries exactly one
    --config whose path is P and whose commit is F or standin(F, P, b)."""
    F, P, S, b = binding
    cfg = (result or {}).get('config') if isinstance(result, dict) else None
    if not (isinstance(cfg, dict) and cfg.get('path') == P and cfg.get('blob_sha256') == S):
        return False
    vals = [argv[i + 1] for i, a in enumerate(argv or []) if a == '--config' and i + 1 < len(argv)]
    if len(vals) != 1 or not isinstance(vals[0], str) or ':' not in vals[0]:
        return False
    commit, path = vals[0].split(':', 1)
    return path == P and commit in (F, s11_standin(F, P, b))


def _s11_unmutated_result(ev, case, result, ctx=None):
    """Bind S11-2a's subtraction to the retained R6.PLAN.4 coverage run on E, both runs bound to the configuration
    admitted at F (S11-2a supplement)."""
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
    # the S11-2a supplement: both runs bound, each independently, to (F, P, S) read from the gate's --freeze and
    # --config and F's pin table, never from either run (a configuration substituted in both runs alike is refused)
    binding = s11_binding(ctx)
    if binding is None or not s11_run_bound(named.get('argv'), before, binding) or \
            not s11_run_bound(case.get('argv'), result, binding):
        return None
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


def eval_z9f_case(exp, case_name, ev, findings_out, ctx):
    """Check the retained selector and lint inputs, with the real adapter pinned to the checked tree."""
    actual = {'case': case_name}
    adapter = 'tools/ledger_coverage/adapters/a1exit_exact_edit.py'
    entry = 'tools/ledger_coverage.py'
    package = 'tools/ledger_coverage/'
    engine = package + 'engine/scope_probe.py'
    verifier_sources = {package + 'engine/' + name + '.py': 'verifier-' + name + '.py'
                        for name in ('purity', 'selftest', 'cli')}
    verifier_sources[entry] = 'verifier-entry.py'
    literal = 'a1exit deletion exact-edit ledger v2'
    cases = {'adapter module containing the string': 'engine-clean.py', 'the string in the engine': 'engine-literal.py'}
    try:
        manifest = ev.man or {}
        proc = manifest.get('procedure')
        members = manifest.get('cases') or []
        if (not isinstance(proc, dict) or proc.get('name') != 'purity-lint' or proc.get('lib') != 'lint' or
                not all(isinstance(c, dict) for c in members) or
                [c.get('case') for c in members] != list(cases) or
                not all(isinstance(proc.get(k), str) for k in ('findings', 'source_map', 'value_set', 'production_paths'))):
            raise ValueError('the two named cases and their lint procedure are required')
        case = ev.case(case_name)
        result = ev.json(case.get('result_file'))
        inputs = {adapter: 'adapter.py', entry: 'entry.py', engine: cases[case_name]}
        if not isinstance(result, dict) or result.get('operation') != 'purity-lint' or result.get('input_files') != inputs:
            raise ValueError('the retained input paths do not give the required source layout')
        blobs = {path: ev.text(member) for path, member in inputs.items()}
        if any(b is None for b in blobs.values()):
            raise ValueError('bytes of a named source are absent')
        if not (ctx and ctx.repo and isinstance(ctx.commit, str) and re.fullmatch(r'[0-9a-f]{40}', ctx.commit)):
            raise ValueError('the checked Git tree is needed to verify the real adapter')
        git_adapter = git_entry(ctx.repo, ctx.commit, adapter)
        if (not git_adapter or git_adapter[0] not in ('100644', '100755') or
                git_show(ctx.repo, ctx.commit + ':' + adapter) != blobs[adapter]):
            raise ValueError('the real adapter bytes differ from the blob at the checked commit')
        if proc.get('verifier_sources') != verifier_sources:
            raise ValueError('the production verifier and dispatch sources must name the required files')
        verifier_hashes = {}
        for path, member in verifier_sources.items():
            raw = ev.text(member)
            git_source = git_entry(ctx.repo, ctx.commit, path)
            if (raw is None or not git_source or git_source[0] not in ('100644', '100755') or
                    git_show(ctx.repo, ctx.commit + ':' + path) != raw):
                raise ValueError('the retained verifier source %s differs from the regular blob at the checked commit'
                                 % path)
            verifier_hashes[path] = hashlib.sha256(raw).hexdigest()
        tree = subprocess.run(['git', '--no-replace-objects', '-C', ctx.repo, 'ls-tree', '-r', '--name-only', '-z',
                               ctx.commit, '--', package + 'engine', entry], capture_output=True)
        if tree.returncode:
            raise ValueError('the checked engine source listing cannot be read')
        tree_paths = tree.stdout.decode().split('\0')
        expected_paths = sorted(p[len(package):] for p in tree_paths if p.startswith(package + 'engine/') and
                                p.endswith('.py') and '__pycache__' not in p.split('/'))
        production_paths = ev.json(proc['production_paths'])
        if not expected_paths or entry not in tree_paths or production_paths != sorted(expected_paths + ['ledger_coverage.py']):
            raise ValueError('the default production selection differs from the exact committed engine scope')
        assignment = [node.value for node in ast.parse(blobs[adapter]).body if isinstance(node, ast.Assign) and
                      any(isinstance(t, ast.Name) and t.id == 'LEDGER_SCHEMA' for t in node.targets)]
        if (len(assignment) != 1 or not isinstance(assignment[0], ast.Constant) or assignment[0].value != literal):
            raise ValueError('the real adapter does not declare the required ledger literal')
        maps = ev.json(proc['source_map'])
        selected = {'ledger_coverage.py': blobs[entry].decode(), engine[len(package):]: blobs[engine].decode()}
        if (not isinstance(maps, dict) or set(maps) != set(cases) or maps[case_name] != selected or
                result.get('selected_paths') != sorted(selected)):
            raise ValueError('the production selector must include both engine sources and exclude the adapter')
        values = ev.json(proc['value_set'])
        if not isinstance(values, list) or not all(isinstance(v, str) for v in values) or literal not in values:
            raise ValueError('the exact adapter literal is absent from the retained lint value set')
        planted = case_name == 'the string in the engine'
        expected_code = ('value = %r\n' % literal).encode() if planted else b'value = None\n'
        if blobs[engine] != expected_code or blobs[entry] != b'value = None\n':
            raise ValueError('the engine witness and neutral entry point do not form the required pair')
        expected_findings = (["engine/scope_probe.py:1: string literal %r occurs in a configuration or record" % literal]
                             if planted else [])
        reports = ev.json(proc['findings'])
        exit_code = 20 if planted else 0
        if (not isinstance(reports, dict) or set(reports) != set(cases) or reports[case_name] != expected_findings or
                result.get('findings') != expected_findings or result.get('exit_status') != exit_code or
                ev.text(case.get('exit_file')) != ('%d\n' % exit_code).encode()):
            raise ValueError('the retained lint findings and status do not match the exact literal control')
        actual.update(outcome='LINT_FAIL' if planted else 'LINT_PASS', exit=exit_code,
                      adapter_path=adapter, adapter_sha256=hashlib.sha256(blobs[adapter]).hexdigest(),
                      production_verifier_sha256=verifier_hashes,
                      fixture_selected_paths=sorted(selected), production_selected_count=len(production_paths),
                      production_excludes_adapter=True)
        # The owner-approved reading of the legacy linted_paths_include key checks the inputs to
        # the selector. In production only the two selected engine paths above reach the lint.
        observations = {'source_map_nonempty': (bool(selected), 'production-selected source map'),
                        'linted_paths_include': ('adapters/', 'selector inputs')}
        actual['invariants'] = {k: {'value': observations[k][0], 'source': observations[k][1]}
                                for inv in exp.get('invariants') or [] for k in inv}
        if (actual['outcome'] != exp.get('outcome') or
                any(observations[k][0] != v for inv in exp.get('invariants') or [] for k, v in inv.items())):
            raise ValueError('the measured scope and outcome do not meet the declared case')
    except (KeyError, ValueError, SyntaxError, FileInvalid) as exc:
        findings_out.append(('procedural-failed', 'Z9f case %r: %s' % (case_name, exc)))
    return actual


def eval_lc_case(exp, case_name, ev, row, findings):
    """Bind the claimed LC result to its exact fixture bytes and recompute the landing rule."""
    actual = {'case': case_name}
    try:
        declared = row['expect']['cases']
        names = [c['case'] for c in declared]
        if [c.get('case') for c in (ev.man or {}).get('cases', [])] != names:
            raise ValueError('the complete named landing fixture evidence is required')
        position = names.index(case_name)
        raw = ev.case(case_name)
        op = 'compose_landing' if position == 0 else 'execution.landing'
        label = 'landing builder' if position == 0 else 'execution landing checker'
        result = ev.json(raw['result_file'])
        if raw.get('argv') != ['in-process', label] or result['operation'] != op or result.get('in_process') is not True:
            raise ValueError('the retained runner did not invoke the prescribed landing stage')
        want = next(inv['fixture'] for inv in declared[0]['invariants'] if 'fixture' in inv)
        fixture = result['fixture']
        path = want['path']
        splice, = want['splices']
        h, c, m = (fixture[role].encode() for role in ('H', 'C', 'M'))
        start, end = splice['start'], splice['end']
        old, new = h[start:end], result['splice_bytes'].encode()
        if position == 3:
            want = dict(want, M=(old + h).decode())
        if (fixture != want or not 0 <= start < end <= len(h) or _file_sha(old) != splice['old_sha256'] or
                _file_sha(new) != splice['new_sha256']):
            raise ValueError('the exact fixture inputs, splice span or splice bytes differ')

        conflict = c != h and m != h and c != m
        offsets = []
        if conflict:
            offsets = [i for i in range(len(m) - len(old) + 1) if m[i:i + len(old)] == old]
            composed = m[:offsets[0]] + new + m[offsets[0] + len(old):] if len(offsets) == 1 else None
        else:
            composed = m if c == h else c
        landing = result['landing']
        body = landing['bytes'].encode()

        def entry(data):
            return path.encode() + b'\0' + b'100644:' + _git_oid('blob', data).encode()

        H = hashlib.sha1(b'landing base' + entry(h)).hexdigest()
        C = hashlib.sha1(b'landing candidate' + H.encode() + entry(c)).hexdigest()
        M = hashlib.sha1(b'landing main' + H.encode() + entry(m)).hexdigest()
        parents = M.encode() + C.encode()
        subject = b'adverse landing' if position >= 2 else b'in-memory landing'
        change = entry(body) if position >= 2 or body != m else b''
        L = hashlib.sha1(subject + M.encode() + change + parents).hexdigest()
        blob = _git_oid('blob', body)
        if (result['roles'] != {'H': H, 'C': C, 'M': M, 'L': L} or landing['parents'] != [M, C] or
                landing['mode'] != '100644' or landing['git_blob'] != blob):
            raise ValueError('the regular-file bytes and parent order do not derive the observed landing')
        compositions = [{'path': path, 'composed_blob': None if composed is None else _git_oid('blob', composed),
                         'l': blob}] if conflict and position != 0 else []
        if result['landing_compositions'] != compositions:
            raise ValueError('the landing checker did not report the required composition')
        if position < 2 and body != composed:
            raise ValueError('the builder or verified landing differs from the computed composition')
        if position == 2 and (composed is None or len(body) != len(composed) or
                              sum(a != b for a, b in zip(body, composed)) != 1):
            raise ValueError('the adverse landing does not change exactly one byte')
        refusal = result['builder_refusal']
        if position == 3:
            if composed is not None or len(offsets) != 2 or refusal != '%s: %s: old bytes occur 2 times at M' % (
                    path, splice['id']):
                raise ValueError('the exact repeated-span fixture must refuse composition')
        elif refusal is not None:
            raise ValueError('an unexpected builder refusal was reported')

        expect_classes = exp.get('classes_include', [])
        observed = [(i['class'], i['obligation'], i['decision'], i['subject'], i['file']) for i in result['items']]
        if observed != [(cls, 'MAIN', 'FAIL', path, path) for cls in expect_classes]:
            raise ValueError('the landing findings do not name the required class and path')
        measured = recompute_outcome(result)
        code = TOOL_EXIT[measured]
        outcome = ('HASH_EQUAL' if position == 0 else 'LANDING_VERIFIED') if measured == 'PASS' else measured
        if (outcome != exp['outcome'] or measured != result['outcome'] or result['exit_status'] != code or
                ev.text(raw['exit_file']) != ('%d\n' % code).encode()):
            raise ValueError('the recorded and recomputed landing outcomes or exit codes differ')
        derived = {'fixture': fixture, 'composed_blob': {'path': path, 'bytes': body.decode(), 'sha256': _file_sha(body)}}
        for inv in exp.get('invariants', []):
            for key, expected in inv.items():
                if not isinstance(expected, dict) or {k: derived[key][k] for k in expected} != expected:
                    raise ValueError('the retained %s differs from the adopted case' % key)
        actual.update(outcome=outcome, exit=code, landing_blob_sha256=_file_sha(body), landing_compositions=compositions)
    except (KeyError, ValueError, TypeError, AttributeError) as exc:
        findings.append(('declarative-mismatch', 'LC case %r: %s' % (case_name, exc)))
    return actual


def _s11_reason(result):
    errors = (result.get('stop') or {}).get('detail', {}).get('errors', [])
    for message in errors:
        if not isinstance(message, str):
            continue
        match = re.match(r'^E([0-9]+): (?:the edit is (lost)|(?:a )?(chained) edit)\b', message)
        if match:
            return {'names_edit': int(match[1]), 'reason': match[2] or match[3]}


def _s11_stage_evidence(ev, case, result):
    stage = 'per-edit unit' if result['splices'] is None else 'ledger correspondence'
    outcome = recompute_outcome(result)
    if (case['argv'] != ['in-process', stage] or result['operation'] != stage or
            result['outcome'] != outcome or result['exit_status'] != TOOL_EXIT.get(outcome) or
            ev.text(case['exit_file']) != ('%d\n' % result['exit_status']).encode()):
        raise ValueError('the retained invocation, result and exit differ')
    if stage == 'ledger correspondence':
        inputs = result['operands']
        ledger, edits = inputs['ledger'], inputs['edits']
        blobs = {'edits.json': edits.encode(), 'ledger.json': ledger.encode()}
        pin = {'path': 'ledger.json', 'blob_sha256': _file_sha(blobs['ledger.json']),
               'companion': [{'path': 'edits.json', 'role': 'edits', 'blob_sha256': _file_sha(blobs['edits.json'])}]}
        led = json.loads(ledger)
        base = hashlib.sha1(b'S11 correspondence base' + b'f.md\0' + b'100644:' +
                            _git_oid('blob', result['text'].encode()).encode()).hexdigest()
        overlay = hashlib.sha1(b'S11 correspondence operands' + base.encode())
        for path, data in sorted(blobs.items()):
            overlay.update(path.encode() + b'\0' + b'100644:' + _git_oid('blob', data).encode())
        overlay.update(base.encode())
        if (inputs['pin'] != pin or led['edits_sha256'] != pin['companion'][0]['blob_sha256'] or
                led['base'] != inputs['base'] or inputs['base'] != base or inputs['commit'] != overlay.hexdigest() or
                led['splices'] != result['splices'] or
                json.loads(edits)['edits'] != [dict(e, site=e['id'], part=1) for e in result['edits']]):
            raise ValueError('the retained ledger or edit list differs from the dispatched pins')
    return outcome


def _s11_clean_result(rid, ev, case, result):
    baseline = ev.case('baseline') or {}
    files = (baseline.get('result_file'), case.get('baseline_file'), case.get('result_file'))
    if (not all(files) or len(set(files)) != 3 or case.get('baseline_argv') != baseline.get('argv') or
            case.get('argv') != baseline.get('argv') or ev.text(files[0]) is None or
            ev.text(files[0]) != ev.text(files[1]) or ev.text(files[1]) != ev.text(files[2]) or
            _s11_stage_evidence(ev, baseline, ev.json(files[0])) != 'PASS' or
            _s11_stage_evidence(ev, case, result) != 'PASS'):
        return False
    primary = {'S11-57b': 'at H', 'S11-57c': 'correspondence', 'S11-58a-f': 'a'}.get(rid, '')
    original = ev.json((ev.case(primary) or {})['result_file'])
    if result['text'] != original['text']:
        return False
    if rid in ('S11-58a-f', 'S11-58i'):
        return original == result
    edits = original['edits']
    if rid in ('S11-57a', 'S11-57b'):
        edit = edits[0]
        return result['edits'] == [dict(edit, new_step2=edit['old_step2'])] and result['splices'] is None
    if rid == 'S11-57d':
        edit = edits[0]
        return result['edits'] == [dict(edit, new=edit['old'])] and result['splices'] is None
    if rid in ('S11-58h', 'S11-58j', 'S11-58k'):
        return result['edits'] == edits[1:] and len(result['splices']) == 1
    return result['edits'] == edits and result['splices'] != original['splices']


def _s11_oracle_result(rid, name, ev, proc):
    case = ev.case(name)
    result = ev.json(case['result_file'])
    tool = ev.json(proc['tool_output'])[name]
    oracle = ev.json(proc['oracle_output'])[name]
    if result != tool or any(tool[k] != oracle[k] for k in ('text', 'edits')):
        raise ValueError('the oracle outputs and case result do not bind the same input')
    outcome = _s11_stage_evidence(ev, case, result)
    counts = tool['per_edit']['counts']
    if counts != {k: len(oracle['static_new'][k]) for k in ('infinity', 'register', 'register-caps')}:
        raise ValueError('the per-edit counts differ from P static_new')
    variants = [pair[:2] if pair[0] is not None else None for pair in oracle['variants']]
    if tool['selections'] != variants:
        raise ValueError('the selections differ from P')
    if rid in ('S11-57a', 'S11-57b', 'S11-57c') and counts['register'] != 1:
        raise ValueError('the per-edit result does not contain the expected register finding')
    if rid == 'S11-57a':
        old, new = variants[0]
        if (old != new or tool['per_splice']['operation'] != 'per-splice unit' or
                recompute_outcome(tool['per_splice']) != 'PASS'):
            raise ValueError('the unchanged selected splice alone did not pass')
    if rid == 'S11-57b':
        fields = ('old', 'new') if name == 'at H' else ('old_step2', 'new_step2')
        if variants[0] != [tool['edits'][0][k] for k in fields]:
            raise ValueError('the selected pair does not match the named base')
    if rid == 'S11-57d' and tool['sentences'] != oracle['sentences']:
        raise ValueError('the tool and P sentence splits differ')
    if rid == 'S11-58a-f':
        old = {'a': 'alpha one.', 'b': 'beta two.', 'c': None,
               'd': 'alpha one.', 'e': 'beta two.', 'f': None}[name]
        counts_at_h = tuple(tool['text'].count(tool['edits'][0][k]) for k in ('old', 'old_step2'))
        if (counts_at_h != {'a': (1, 0), 'b': (0, 1), 'c': (0, 0),
                            'd': (1, 1), 'e': (2, 1), 'f': (2, 2)}[name] or
                oracle['variants'][0][0] != old or bool(tool.get('stop')) != (old is None)):
            raise ValueError('the selection or refusal does not match the original case')
    if rid == 'S11-58g' and variants[0] != [tool['edits'][0][k] for k in ('old_step2', 'new_step2')]:
        raise ValueError('P did not select the alternate pair')
    if rid == 'S11-58h' and oracle['during_application'][1][0] is not None:
        raise ValueError('P did not lose the later edit during application')
    if rid == 'S11-58i':
        old = oracle['variants'][0][0]
        if old is None or len(tool['text'][:tool['text'].index(old)].encode()) != tool['splices'][0]['start']:
            raise ValueError('the selected byte offset differs from P')
    if rid == 'S11-58k' and oracle['applied'].get('f.md') != 'xQ':
        raise ValueError('the retained P application did not produce xQ')
    return outcome


def eval_case(exp, case_name, ev, row, record, findings_out, ctx=None, phase=None):
    """Evaluates one expectation (the row's, one of its cases, or its restored case) against the retained
    evidence of the case. Appends findings; returns the extracted actual."""
    if is_line_patch_rc8(row):
        return eval_line_patch_case(exp, case_name, ev, findings_out)
    if row['id'] == 'Z9f':
        return eval_z9f_case(exp, case_name, ev, findings_out, ctx)
    if row['id'] in ('LC-1', 'LC-2', 'LC-3', 'LC-4', 'LC-5', 'LC-6'):
        return eval_lc_case(exp, case_name, ev, row, findings_out)
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
    rt_t0 = rid == 'RT-T0' and 'sites[moved_in=H..X]' in row['expect'].get('counts', {})
    rt_t0_counts, rt_t0_merged = {}, {}
    if rt_t0:
        try:
            rt_t0_counts, rt_t0_merged = _rt_t0_observations(result)
            actual['merger_group_overlaps'] = {p: s for p, s in rt_t0_merged.items() if s}
            if phase == 'candidate-F' and not _rt_t0_case_bound(c, result, attested, ctx):
                raise ValueError('the exact fixed inputs or representative read scope do not verify')
        except (ValueError, KeyError, TypeError, AttributeError) as exc:
            findings_out.append(('declarative-mismatch', 'RT-T0 case %r: %s' % (case_name, exc)))
    terminology_counts = {}
    retired_hold, unclassified = False, set()
    fixed_terms = phase in ('tool-acceptance', 'candidate-F') and rid in FIXED_TERMS_ROWS
    fixed_bound = False
    if fixed_terms:
        try:
            _fixed_terms_case(ctx, phase, rid, ev, c, result, attested)
            if rid == 'RT-I7A' and case_name == 'at H':
                census = ev.case('retired deny profile census')
                _fixed_terms_case(ctx, phase, rid, ev, census, ev.json(census['result_file']),
                                  ev.json(census['attested']))
            fixed_bound = True
        except (ValueError, SyntaxError, KeyError, TypeError, AttributeError, StopIteration) as exc:
            findings_out.append(('declarative-mismatch', 'case %r does not bind the fixed %s operands: %s'
                                 % (case_name, rid, exc)))
    if phase in ('tool-acceptance', 'candidate-F') and rid == 'RT-I7A' and case_name != 'restored':
        try:
            terminology_counts, retired_hold, unclassified = _fixed_item7a(result, ctx)
        except (ValueError, KeyError, TypeError, AttributeError):
            findings_out.append(('raw-evidence-missing', 'the fixed Item 7 partitions cannot be reconstructed'))
    if phase in ('tool-acceptance', 'candidate-F') and rid in ('N10', 'N11') and case_name == '':
        try:
            _rep_fixed_reconciliation(ctx, phase, rid, ev, c, result)
        except (ValueError, SyntaxError, KeyError, IndexError, TypeError, AttributeError) as exc:
            findings_out.append(('declarative-mismatch', 'the fixed %s operands do not verify: %s' % (rid, exc)))
    if phase == 'candidate-F' and rid in ('RT-T', 'TR5', 'RT-D', 'RT-D-gr58'):
        try:
            census = None
            if rid == 'RT-D' and case_name == '':
                case = ev.case('all review profiles')
                census = case, ev.json(case['result_file']), ev.json(case['attested'])
            bound = _candidate_case_bound(rid, c, result, attested, ctx, census=census)
            if bound and census is not None:
                terminology_counts = _rt_d_counts(result, census[1])
        except (ValueError, KeyError, TypeError, AttributeError, SyntaxError, re.error):
            bound = False
        if not bound:
            findings_out.append(('declarative-mismatch', 'case %r does not bind the actual %s operands at F'
                                 % (case_name, rid)))
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
        elif rid in S11_P_ORACLE_ROWS and o in ('ORACLE', 'RESULT_EQUAL_CLEAN'):
            try:
                if o == 'ORACLE':
                    proc = (ev.man or {}).get('procedure') or {}
                    same = _s11_oracle_result(rid, case_name, ev, proc) == 'PASS'
                else:
                    same = _s11_clean_result(rid, ev, c, result)
            except (ValueError, KeyError, TypeError, IndexError, AttributeError):
                same = False
            actual['outcome'] = o if same else 'RESULT_DIFFERS'
            if not same:
                findings_out.append(('declarative-mismatch', 'case %r: %s evidence differs' % (case_name, o)))
        elif rt_t0 and o == 'RESULT_EQUAL_CLEAN':
            primary = ev.case('')
            first = ev.json(primary.get('result_file')) if primary else None
            clean = ev.json(c.get('baseline_file'))
            same = (result is not None and result == first == clean and bool(rt_t0_counts) and
                    exit_code == result['exit_status'] and c.get('baseline_argv') == primary.get('argv'))
            actual['outcome'] = o if same else 'RESULT_DIFFERS'
            if not same:
                findings_out.append(('declarative-mismatch', 'RT-T0 restored result differs from its bound raw case'))
        elif rid == 'TT2' and o == 'RESULT_EQUAL_CLEAN':
            baseline = ev.json(c['baseline_file']) if c.get('baseline_file') else None
            countercase = ev.case('') or {}
            adverse = ev.json(countercase['result_file']) if countercase.get('result_file') else None
            same = (_tt2_comparison_paths(result) == [] and result == baseline and
                    bool(_tt2_comparison_paths(adverse)) and result['main'] == result['scientific_base'] ==
                    adverse['scientific_base'] and adverse['main'] != result['main'] and
                    result['candidate'] == adverse['candidate'] and
                    result['ledgered_paths'] == adverse['ledgered_paths'] and
                    result['tree_entries']['x'] == adverse['tree_entries']['x'])
            actual['outcome'] = o if same else 'RESULT_DIFFERS'
            if not same:
                findings_out.append(('declarative-mismatch', 'case %r: no clean restored TT2 comparison of X and H'
                                     % case_name))
        elif rid == 'TT7' and o == 'RESULT_EQUAL_CLEAN':
            baseline_file = c.get('baseline_file')
            clean = (ev.case('baseline') or {}).get('result_file')
            baseline = ev.json(baseline_file) if baseline_file else None
            clean_result = ev.json(clean) if clean else None
            composed = ev.case('landing under the computed composition') or {}
            dropped = ev.case('landing that drops the main-side edit') or {}
            adverse = ev.json(composed['result_file']) if composed.get('result_file') else None
            wrong = ev.json(dropped['result_file']) if dropped.get('result_file') else None
            restored, original = _tt7_landing_roles(result), _tt7_landing_roles(adverse)
            incorrect = _tt7_landing_roles(wrong)
            same = (restored is not None and original is not None and incorrect is not None and
                    bool(baseline_file and clean and c.get('result_file')) and
                    len({baseline_file, clean, c['result_file']}) == 3 and result == baseline == clean_result and
                    restored['scientific_base'] == restored['main'] == original['scientific_base'] and
                    original['main'] != restored['main'] and restored['candidate'] == original['candidate'] and
                    restored['landing'] not in (original['landing'], incorrect['landing']) and
                    restored['candidate_blob'] == restored['landing_blob'] == original['candidate_blob'] and
                    result.get('landing_compositions') == [] and result.get('items') == [] and
                    recompute_outcome(result) == 'PASS')
            actual['outcome'] = o if same else 'RESULT_DIFFERS'
            if not same:
                findings_out.append(('declarative-mismatch', 'case %r: no clean TT7 landing with M restored to H'
                                     % case_name))
        elif fixed_terms and o == 'RESULT_EQUAL_CLEAN':
            baseline_name = {'RT-DR3W': FIXED_DR3_CASE, 'RT-I7': 'at H', 'RT-I7A': FIXED_X_CASE}[rid]
            clean = ev.case(baseline_name) or {}
            files = (clean.get('result_file'), c.get('baseline_file'), c.get('result_file'))
            same = (fixed_bound and all(files) and len(set(files)) == 3 and
                    c.get('baseline_argv') == clean.get('argv') and
                    ev.text(files[0]) == ev.text(files[1]) == ev.text(files[2]) and
                    attested == (ev.json(clean['attested']) if clean.get('attested') else {}))
            actual['outcome'] = o if same else 'RESULT_DIFFERS'
            if not same:
                findings_out.append(('declarative-mismatch', 'case %r differs from the actual fixed clean scan'
                                     % case_name))
        elif o in ('RESULT_EQUAL_CLEAN', 'RESULT_EQUAL_FULL_STORE', 'RESULT_EQUAL_WITHOUT_AMENDMENT',
                   'REPLAY_EQUAL') and c.get('baseline_file'):
            # gate-computed: the case's item tuples and outcome equal those of the retained baseline run
            base = ev.json(c['baseline_file'])
            same = (result is not None and base is not None and _tuples(result) == _tuples(base)
                    and recompute_outcome(result) == recompute_outcome(base))
            actual['outcome'] = o if same else 'RESULT_DIFFERS'
            if not same:
                findings_out.append(('declarative-mismatch', 'case %r: result differs from its baseline' % case_name))
        elif rid == 'TT2' and o == 'COUNTERCONTROL':
            reported = _tt2_comparison_paths(result)
            actual['outcome'] = o if reported else None
            if not reported or ('outcome' in attested and attested['outcome'] != o):
                findings_out.append(('raw-evidence-missing' if reported is None else 'declarative-mismatch',
                                     'case %r: no consistent direct tree comparison for TT2' % case_name))
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
            if key in rt_t0_counts:
                got, src = rt_t0_counts[key], 'result'
            elif rid == 'S11-57d' and key == 'sentences':
                split = (result or {}).get('sentences')
                got = len(split[0]) if isinstance(split, list) and len(split) == 1 and isinstance(split[0], list) else None
                src = 'result' if got is not None else None
            elif rid == 'RT-I7' and key.startswith('lines[literal='):
                literal = key.removeprefix('lines[literal=').removesuffix(']')
                if literal == 'A1':
                    got = (result or {}).get('reports', {}).get('item7-literal', {}).get('report_regex_lines')
                else:
                    got = len({(i['file'], i['line']) for i in items if literal in i.get('literals', [])})
                src = 'result' if got is not None else None
            elif ((rid == 'RT-I7A' and phase in ('tool-acceptance', 'candidate-F')) or
                  (rid == 'RT-D' and phase == 'candidate-F' and key.startswith('lines['))):
                got = terminology_counts.get(key)
                src = 'result' if got is not None else None
            else:
                got, src = extract_count(key, result or {}, bindings, attested)
            actual.setdefault('counts', {})[key] = got
            if src is None:
                findings_out.append(('raw-evidence-missing', 'case %r: count %s not extractable' % (case_name, key)))
            elif got != want:
                findings_out.append(('declarative-mismatch', 'case %r: count %s = %r, expected %r'
                                     % (case_name, key, got, want)))
        for s in exp.get('sites') or []:
            subj = _bind(s.get('subject'), bindings) if 'subject' in s else None
            # `$name` values are bindings the runner's manifest supplies (R6.GATE.3), in a site's fields as in its subject
            fields = {k: (v if k in ('classes_exact', 'classes_include') else _bind(v, bindings))
                      for k, v in s.items() if k != 'subject'}
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
                if rt_t0 and fields == {'all': 'other merger-group sites', 'overlapped_by_splice': None}:
                    named = {s['subject'] for s in exp['sites'] if 'subject' in s}
                    other = rt_t0_merged.keys() - named
                    got = bool(other) and all(not rt_t0_merged[site] for site in other)
                elif rid == 'RT-DR3W':
                    got = any(i.get('rule_id') == 'DR-3' and
                              i['sentence_start_line'] == s['sentence_start_line'] and
                              set(s['lines']) <= set(range(i['sentence_start_line'], i['sentence_end_line'] + 1))
                              for i in items)
                elif rid == 'RT-I7A' and phase in ('tool-acceptance', 'candidate-F'):
                    full = 'book/The-Incompleteness-of-Observation-FULL.md'
                    want = {('papers/SM.md', 1394), ('papers/GR.md', 58),
                            ('book/ch09-universality.md', 137), ('book/ch19-open-problems.md', 198),
                            ('book/ch19-open-problems.md', 212), ('book/appendix-b-derivations.md', 235),
                            ('book/appendix-b-derivations.md', 246),
                            *((full, n) for n in (2554, 5270, 5284, 5914, 5925))}
                    got = unclassified == want and all(i['class'] == 'final-unclassified'
                                                     for i in items if (i.get('file'), i.get('line')) in want)
                else:
                    got = attested.get('sites:' + json.dumps(s, sort_keys=True))
                if got is not True:
                    findings_out.append(('raw-evidence-missing' if got is None else 'declarative-mismatch',
                                         'case %r: site condition %s not attested' % (case_name, s)))
                continue
            subjects = ((result or {}).get('sites') or []) + ((result or {}).get('hits') or [])
            sites = [x for x in subjects if _names(x, subj)]
            sitems = [i for i in items if _names(i, subj)]
            ok = bool(sites or sitems)
            for k, v in fields.items():
                if rt_t0 and k == 'overlapped_by_splice':
                    ok = ok and rt_t0_merged.get(subj) == [v]
                elif rid == 'RT-I7' and k == 'literal':
                    ok = ok and any(v in i.get('literals', []) for i in sitems)
                elif k in ('classes_exact', 'classes_include'):
                    got = sorted({i.get('class') for i in sitems})
                    ok = ok and (set(v) == set(got) if k == 'classes_exact' else set(v) <= set(got))
                elif k == 'added_relative_to_unmutated':
                    baseline = (_s11_unmutated_result(ev, c, result, ctx) if rid == 'S11-2a'
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
                    ok = ok and any(_site_matches(x, k, v, result or {}, bindings) for x in sites + sitems)
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
            if rid in ('S11-58h', 'S11-58j', 'S11-58k') and set(inv) == {'names_edit', 'reason'}:
                got, src = _s11_reason(result or {}), 'result'
                holds = got == inv
            elif rid == 'S11-58i' and k in ('selected_offset', 'refused'):
                splices = (result or {}).get('splices') or []
                if k == 'refused':
                    got = bool(result.get('stop')) if result is not None else None
                else:
                    got = splices[0].get('start') if len(splices) == 1 and isinstance(splices[0], dict) else None
                src, holds = 'result', got == v
            elif rid == 'EI6' and phase in ('tool-acceptance', 'candidate-F') and k == 'before_unloaded_import':
                got, src = _bootstrap_refusals_hold(ev.json('import-trace.json')), 'result'
                holds = got == v
            elif fixed_terms and k in ('representative_candidate', 'scanned_paths_within'):
                holds, got, src = fixed_bound, v if fixed_bound else None, 'verified fixed inputs and reads'
            elif rid == 'RT-I7A' and phase in ('tool-acceptance', 'candidate-F') and 'each_listed_line' in inv:
                holds, got, src = retired_hold, retired_hold, 'result'
            elif rid == 'TT7' and k in ('L_blob', 'composed_blob'):
                roles = _tt7_landing_roles(result)
                blobs = _tt7_landing_blobs(result, roles, bindings)
                got = (blobs or {}).get(k)
                holds, src = got is not None and got == v, 'result' if got is not None else 'unattested'
                if holds and case_name == 'landing that drops the main-side edit':
                    composed = ev.case('landing under the computed composition') or {}
                    paired = ev.json(composed['result_file']) if composed.get('result_file') else None
                    other = _tt7_landing_roles(paired)
                    holds = bool(other and all(roles[key] == other[key]
                                               for key in ('scientific_base', 'main', 'candidate')) and
                                 roles['landing'] != other['landing'] and
                                 roles['candidate_blob'] == other['candidate_blob'] == roles['landing_blob'] and
                                 roles['landing_blob'] != other['landing_blob'])
            else:
                holds, got, src = eval_invariant(k, v, result, c, attested, bindings, exp.get('sites') or ())
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
        if proc.get('blobs') and proc.get('nodes'):
            # the listing's blob ids against the nodes the procedure's graph used: every listed path is a node of the
            # graph carrying the listed blob
            blobs = ev.json(proc['blobs']) or {}
            nodes = ev.json(proc['nodes']) or {}
            bad = sorted(q for q, b in blobs.items() if (nodes.get(q) or {}).get('git_blob') != b)
            actual['blob_mismatch'] = bad[:20]
            if bad or not blobs:
                fail('listed blob ids differ from the graph nodes: %s' % bad[:5])
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
        if lib == 'oracle' and row['id'] in S11_P_ORACLE_ROWS:
            try:
                pin = _rep_plan_pin(repo, S11_P_ORACLE_COMMIT, 'edits_check.py')
                if ev.text('p-edits_check.py') != _rep_pin(repo, S11_P_ORACLE_COMMIT, pin):
                    raise ValueError('the retained oracle source differs from the pin at P')
                names = {n for case in row['expect'].get('cases', [{'case': ''}])
                         for n in (case['case'] if isinstance(case['case'], list) else [case['case']])}
                if any(set(ev.json(proc[key])) != names for key in ('tool_output', 'oracle_output')):
                    raise ValueError('the oracle outputs do not cover the declared cases exactly')
                for name in sorted(names):
                    _s11_oracle_result(row['id'], name, ev, proc)
                actual['agree'] = True
            except (ValueError, KeyError, TypeError, IndexError, AttributeError) as exc:
                actual['agree'] = False
                fail(str(exc))
        elif lib == 'oracle':
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

    def __init__(self, repo=None, commit=None, freeze=None, config_path=None, facts_dir=FACTS_DIR, *,
                 tool_candidate=None, rep_main=None, rep_snapshot=None, tool_landing=None, main_tip=None,
                 tool_base=None, tool_preview=None, fixed_config=None):
        self.repo = repo
        self.commit = commit
        self.freeze = freeze
        self.config_path = config_path
        self.facts_dir = facts_dir
        self.tool_candidate = tool_candidate
        self.rep_main = rep_main
        self.rep_snapshot = rep_snapshot
        self.tool_landing = tool_landing
        self.main_tip = main_tip
        self.tool_base = tool_base
        self.tool_preview = tool_preview
        self.fixed_config = fixed_config


def assessment_subject(ctx):
    """Identify the Amendment 11 assessment before examining any runner result or release evidence."""
    if ctx.tool_candidate is not None:
        candidate = ctx.tool_candidate
        if ctx.freeze is not None or any(v is not None for v in
                                         (ctx.rep_main, ctx.rep_snapshot, ctx.tool_landing, ctx.main_tip)):
            why = 'tool acceptance and candidate-F operands were supplied together'
        elif not (ctx.repo and HEX40.fullmatch(candidate) and candidate == ctx.commit and
                  candidate == git_blob_id(ctx.repo, 'HEAD^{commit}')):
            why = 'the tool candidate is not the full commit id of the checkout under check'
        elif git_entry(ctx.repo, candidate, S11_A1_DIRECTORY + '/PREREG.md') is not None:
            why = 'the checkout under check carries the A1 PREREG.md'
        else:
            return {'phase': 'tool-acceptance', 'tool_candidate': candidate}
    else:
        binding = s11_binding(ctx)
        if binding is not None and git_blob_id(ctx.repo, ctx.freeze + '^{commit}') == ctx.freeze:
            F, path, digest, _ = binding
            return {'phase': 'candidate-F', 'freeze': F, 'configuration': {'path': path, 'blob_sha256': digest}}
        why = 'the checked subject lacks a matching exact candidate F and configuration Record pin'
    return {'phase': 'invalid', 'reason': why}


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
    # Standalone release-check controls still exercise the unchanged individual release facts.
    # The retained A1 gate has the REP-BUILD phase contract and applies it to all its due rows.
    tool_drift_scope = ctx.tool_candidate is not None and bool(RETIREMENT_DRIFT_ROWS & rows.keys())
    subject = assessment_subject(ctx) if {'REP-BUILD', 'S11-2'} & rows.keys() or tool_drift_scope else None
    phase = subject['phase'] if subject else None
    try:
        rules_at_f = rules_release(ctx) if phase == 'candidate-F' else None
    except (ValueError, TypeError, AttributeError):
        rules_at_f = False
    scope_problem = None
    if phase == 'tool-acceptance' and ('REP-BUILD' in rows or tool_drift_scope):
        try:
            subject['landing_scope'] = _tool_acceptance_scope(ctx, ctx.tool_candidate, current_main=True)
        except (ValueError, KeyError, TypeError, AttributeError) as exc:
            scope_problem = str(exc)
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
        nr = row.get('not_run') or {}
        due_at_f = rid in F_REQUIRED_ROWS or nr.get('release_check') == RC_RULES
        tool_drift_row = tool_drift_scope and rid in RETIREMENT_DRIFT_ROWS
        if phase == 'invalid' and (due_at_f or tool_drift_row):
            add(rid, 'status-not-allowed', subject['reason'])
        if (rid == 'REP-BUILD' or tool_drift_row) and scope_problem:
            add(rid, 'status-not-allowed', scope_problem)
        if rules_at_f is False and nr.get('release_check') == RC_RULES:
            add(rid, 'status-not-allowed', 'the required reviewed rule records are absent or misbound at F')
        if rid == 'S11-2' and phase and rid in recs:
            add(rid, 'unexpected-id', 'S11-2 is determined by its three component records')
        if (nr.get('reason') == A8_REASON and nr.get('release_check') == RC_FALSE and 'NOT RUN' in allowed
                and rid not in recs and rid not in muts and not row.get('composed_of')):
            e['details'].append('not-run: %s; no runner records it' % A8_REASON)
            status[rid] = 'FAIL' if set(e['findings']) & FINDING_FAIL else 'NOT RUN'
            e['status'] = status[rid]
            continue
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
                deferred_drift = tool_drift_row and phase == 'tool-acceptance' and not scope_problem
                if deferred_drift and rec_status != 'NOT RUN':
                    add(rid, 'status-not-allowed', 'drift and reconciliation are due at the retirement landing')
                if rec_status == 'NOT RUN':
                    if 'NOT RUN' not in allowed:
                        add(rid, 'status-not-allowed', 'NOT RUN not allowed')
                    elif rid == 'REP-BUILD' and phase == 'tool-acceptance':
                        add(rid, 'status-not-allowed', 'tool acceptance requires all three REP-BUILD fixture cases')
                    elif due_at_f and phase == 'candidate-F':
                        add(rid, 'status-not-allowed', 'PASS is required at the assessed candidate F')
                    elif rid == 'G-A1' and phase == 'candidate-F':
                        # OBL-16 keeps native delegated checks on X and C at retirement execution.
                        # The candidate-F chain attestation by itself supplies neither subject.
                        pass
                    elif deferred_drift:
                        e['details'].append('not-run: real drift and reconciliation are due at the retirement landing')
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
                        if rid == 'REP-BUILD':
                            acts.extend(eval_rep_build(row, ev, ctx, phase, fl))
                        elif 'cases' in ex:
                            for c in ex['cases']:
                                names = c['case'] if isinstance(c['case'], list) else [c['case']]
                                for n in names:
                                    acts.append(eval_case(c, n, ev, row, rec, fl, ctx, phase))
                        elif ex.get('outcome') != 'COMPOSITE':
                            acts.append(eval_case(ex, '', ev, row, rec, fl, ctx, phase))
                        if row.get('restored') is not None and row['restored'].get('outcome') != 'COMPOSITE':
                            acts.append(eval_case(row['restored'], 'restored', ev, row, rec, fl, ctx, phase))
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
        if rid == 'REP-BUILD' and phase == 'tool-acceptance' and rec_status == 'PASS' and \
                not (set(e['findings']) & FINDING_FAIL):
            own = 'NOT RUN'
            e['details'].append('not-run: %s; the three tool-acceptance fixture cases passed' % nr['reason'])
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
                elif due_at_f and phase == 'candidate-F':
                    add(rid, 'status-not-allowed', 'composite PASS is required at the assessed candidate F')
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
    result = {
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
    if subject is not None:
        result['subject'] = subject
    return result


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
    ap.add_argument('--freeze', help='the full commit id of the candidate F under assessment')
    ap.add_argument('--config', help='configuration path in the assessed commit')
    ap.add_argument('--tool-candidate', help='the full checkout id for tool acceptance')
    ap.add_argument('--tool-base', help='the proposed landing first parent at origin/main')
    ap.add_argument('--tool-preview', help='the exact proposed merge commit of the tool candidate into its base')
    ap.add_argument('--fixed-config', help='the full revision and path of the retained fixed-case configuration')
    ap.add_argument('--rep-main', help='the full commit id of the representative main anchor')
    ap.add_argument('--rep-snapshot', help='the full commit id of the reviewed representative snapshot')
    ap.add_argument('--tool-landing', help='the full commit id of the actual tool landing')
    ap.add_argument('--main-tip', help='the full commit id of independently read main')
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
                         Ctx(a.repo, commit, a.freeze, a.config, a.facts_dir, tool_candidate=a.tool_candidate,
                             rep_main=a.rep_main, rep_snapshot=a.rep_snapshot, tool_landing=a.tool_landing,
                             main_tip=a.main_tip, tool_base=a.tool_base, tool_preview=a.tool_preview,
                             fixed_config=a.fixed_config))
    res['commit_under_check'] = commit
    write_json(os.path.join(a.out, 'gate-result.json'), res)
    return code


if __name__ == '__main__':
    sys.exit(main())
