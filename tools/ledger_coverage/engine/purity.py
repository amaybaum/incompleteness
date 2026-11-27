"""Z9: the engine contains no retirement constant (sec. 16.1)."""
import ast
import json
import os
import re

here = os.path.dirname(os.path.abspath(__file__))

# The allowlist, in three categories; each category is itself linted below.
field_names = frozenset([
    'id', 'file', 'start', 'end', 'new', 'old', 'old_sha256', 'new_sha256', 'new_bytes', 'splices', 'sites', 'base',
    'files', 'retained', 'mirrors', 'mirror_of', 'site_id', 'pin_line', 'carried', 'row', 'code', 'owner', 'author',
    'reviewer', 'reviewed', 'verdicts', 'verdict', 'supersedes', 'path', 'blob_sha256', 'segment', 'kind', 'name',
    'line', 'lines', 'commit', 'parent', 'position', 'pre_sha256', 'post_sha256', 'steps', 'own_lines', 'item',
    'rules', 'profiles', 'pattern', 'patterns', 'scope', 'matcher', 'literal', 'context', 'negative', 'fingerprints',
    'max_instances', 'context_required', 'recorded_at', 'positive_examples', 'negative_examples', 'countercontrol',
    'reason', 'method', 'dissent', 'authorizes', 'record', 'review', 'time', 'comment_id', 'edits', 'targets',
    'pin_note', 'checker', 'source', 'extractor', 'selector', 'applies_to', 'levels', 'combine', 'except', 'mode',
    'flags', 'report_regex', 'splice_kinds', 'replaced_text_rewrite', 'replacement', 'match_keys', 'key', 'checks',
    'final_profiles', 'default_for', 'roles', 'pin', 'scientific_base', 'record_commit', 'side_change_classes',
    'corpus', 'adapters', 'ledger', 'sitemap', 'replay', 'delegation', 'adapter', 'adapter_version', 'module',
    'module_path', 'record_tree', 'functions', 'companion', 'role', 'hp_obligations', 'merges', 'pr', 'first_parent',
    'records', 'operations', 'controls', 'control_inputs', 'control_input', 'sentence_line', 'alternative',
    'operations', 'direction', 'context_mapping', 'source_field', 'values', 'default', 'indicators', 'strip',
    'definitions', 'on', 'effect', 'list_item_patterns', 'table_row_pattern', 'caption_prefixes', 'sentence',
    'splitter_version', 'abbreviations', 'config_id', 'version', 'retirement', 'schema', 'widening_review', 'notes',
    'errors', 'pin_rules', 'min_len', 'skip_prefixes', 'prefix', 'ignored_fields', 'base_sha256', 'expected_sha256',
    'context_field_value', 'quote', 'override_anchors', 'read_entries', 'equalities', 'equal', 'self_test',
    'ck_errors', 'extended_unmapped', 'from_context_sha256', 'to_context_sha256', 'from_structure_sha256',
    'to_structure_sha256', 'semantic_classification', 'classifications', 'entries', 'classes', 'paths', 'prefixes',
    'line_sha256', 'record_id', 'exclude_prefixes', 'exclude_files', 'include_patterns_within_excluded',
    'exclude_patterns', 'ledgered_paths', 'params', 'evidence', 'sha256', 'blob', 'class_adapters', 'issue', 'sentences',
    'manuscript_digest', 'paths_record', 'record-dir', 'interface', 'module_sha256', 'regex', 'context_field',
    'INTERFACE', 'NAME', 'VERSION', 'outcome', 'exit_status', 'items', 'preflight', 'record_checks', 'passed',
    'scientific_effect', 'conclusions', 'assessment', 'invalidated', 'resolutions', 'ledger_binding', 'ledger_base',
    'holds', 'obligation', 'class', 'decision', 'subject', 'fingerprint', 'm', 'l', 'h', 'c', 'x', 'list', 'check',
    'message', 'status', 'match', 'H', 'X', 'M', 'L', 'C', 'GITHUB_ACTIONS', 'GITHUB_RUN_ID', 'GITHUB_TOKEN',
    'GITHUB_API_URL', 'GITHUB_REPOSITORY_ID',
    # design r6 amendment 4: the record base and the reassessment record (R6.RECON.2 (c), R6.RECON.27)
    'record_base', 'finding', 'repair', 'edit', 'rederivation', 'commits', 'target', 'start_H',
    'side_change_commits', 'category3', 'findings', 'blocked', 'reassessments', 'run_level',
    # the site field of R6.CTX.10 and the key of the session registry's withdrawals (oi-a1-staging-sessions/1)
    'partial_quote', 'withdrawn',
])
schema_ids = frozenset([
    'oi-ledger-coverage/5', 'oi-retirement-config/1', 'oi-term-rules/2', 'oi-delegation/1', 'oi-hp-adjudication/1',
    'oi-context-adjudication/1', 'oi-hit-classification/1', 'oi-scope/1', 'oi-side-change-classes/1',
    'oi-reconciliation/1', 'oi-reconciliation/2', 'oi-review-record/1', 'oi-ledger-landing/1', 'oi-reassessment/1',
    'oi-obl29-custody/1',
])
enumerations = frozenset([
    'PASS', 'REVIEW_REQUIRED', 'FAIL', 'USAGE', 'ERROR', 'VOID', 'INTERNAL',
    'unauthorized-change', 'missing', 'duplicated', 'ambiguous', 'context-meaning-unverified', 'retained-changed',
    'unauthorized-edit', 'unledgered-file-change', 'hp-unadjudicated', 'untracked-hp-overlap', 'provenance-mismatch',
    'provenance-gap', 'provenance-foreign', 'provenance-ambiguous', 'adjudication-row-changed', 'deny-match',
    'item7-literal-match', 'rule-negative-match', 'rule-overreach', 'record-invalid', 'stale-adjudication',
    'final-unclassified', 'pin-broken', 'pin-target-missing', 'mirror-mismatch', 'lean-code-change',
    'delegated-evidence-invalid', 'candidate-parent', 'landing-parents', 'landing-first-parent-not-M',
    'landing-drops-main-change', 'landing-conflict-unresolved', 'landing-extra-change', 'base-drift', 'unclassified',
    'new-pattern-in-replacement', 'unclassified-in-replacement', 'rule-fingerprint-mismatch', 'rule-stale',
    'context-structure-changed', 'delegated-evidence-missing', 'side-change-unclassified',
    'retirement-blocked', 'RC14', 'reconciled-state', 'reconciled', 'reconciled-resolved', 'no-effect', 'invalidates',
    'PIN_MISMATCH', 'RECORD_TREE_MISMATCH', 'SCIENTIFIC_BASE_MISMATCH', 'MAIN_NOT_DESCENDANT', 'SOURCE_CHANGED',
    'LEDGER_INTEGRITY', 'EDITS_HASH_MISMATCH', 'ENCODING', 'UNRESOLVABLE', 'CONFIG_INVALID', 'CONFIG_UNSUPPORTED',
    'CONFIG_UNREVIEWED', 'CONFIG_INCONSISTENT', 'CONFIG_NO_CONTROLS', 'PREFLIGHT_FAILED',
    'json-pointer', 'python-ast-assign', 'literal-list', 'review', 'deny', 'tree', 'added-text', 'accept', 'reject',
    'dissent', 'countercontrol', 'allow', 'review-pattern', 'corpus', 'ledgered', 'repo', 'all-corpus', 'any', 'all',
    'line', 'sentence', 'splice', 'tokens', 'spans', 'stripped', 'quote', 'meaning', 'structure-list',
    'structure-table', 'info', 'invalid', 'positive', 'adversarial', 'record', 'coverage', 'execution', 'terms',
    'self-test', 'purity-lint', 'ledger', 'sitemap', 'replay', 'delegation', 'chain', 'harness', 'HP', 'RET', 'TERMS',
    'RECORD', 'MAIN', 'DELEGATED', 'BOF', 'EOF', 'hp', 'ledgered', 'unledgered', 'unchanged', 'moved',
    'authorized-replacement', 'authorized-removal', 'unresolved', 'carried', 'changed', 'removed', 'conforms',
    'pass', 'fail', 'missing', 'widening', 'edits', 'checker', 'identity', 'scope', 'classification',
    'none', 'side-change-classes', 'REPLAY_REFUSED', 'REPLAY_MISMATCH', 'reassessment',
    # the outcome names of R6.GATE.3 the engine controls attest
    'COUNTERCONTROL', 'LINT_PASS', 'LINT_FAIL',
    'RC1', 'RC2', 'RC3', 'RC4', 'RC5', 'RC6', 'RC7', 'RC8', 'RC9', 'RC10', 'RC11', 'RC12', 'RC13',
    'U', 'M', 'K', 'B', 'H', 'O', 'R', 'S1', 'N2', 'B1', 'B2', 'B3', 'B4', 'B6', 'K1', 'K2', 'K3', 'K4', 'K5',
    'M1', 'M2', 'M3', 'M4', 'M5', 'M6', 'M11', 'O1', 'O9',
])
# The design's fixed name of the plan's file of record pins (sec. 6.3, configuration admission point 2): a fourth
# category, linted to be one file name of the plan's record directory. It names no retirement.
interface_names = frozenset(['PREREG.md'])
_hex = re.compile(r'(?<![0-9A-Za-z])[0-9a-fA-F]{7,}(?![0-9A-Za-z])')
_field_rx = re.compile(r'^[A-Za-z_][A-Za-z0-9_-]*$')
_schema_rx = re.compile(r'^oi-[a-z0-9-]+/[0-9]+$')
_enum_rx = re.compile(r'^[A-Za-z][A-Za-z0-9_-]*$')


def lint_allowlist():
    bad = []
    bad += ['field name %r' % x for x in field_names if not _field_rx.match(x)]
    bad += ['schema id %r' % x for x in schema_ids if not _schema_rx.match(x)]
    bad += ['enumeration %r' % x for x in enumerations if not _enum_rx.match(x)]
    bad += ['interface name %r' % x for x in interface_names if not re.match(r'^[A-Za-z][A-Za-z0-9_-]*\.md$', x)]
    return bad


def allowed(s):
    return s in field_names or s in schema_ids or s in enumerations or s in interface_names


def engine_sources(root=None):
    root = root or here
    out = {}
    for dp, dn, fn in os.walk(root):
        dn[:] = [d for d in dn if d != '__pycache__']
        for f in sorted(fn):
            if f.endswith('.py'):
                p = os.path.join(dp, f)
                with open(p, encoding='utf-8') as fh:
                    out[os.path.relpath(p, os.path.dirname(root))] = fh.read()
    entry = os.path.join(os.path.dirname(os.path.dirname(root)), 'ledger_coverage.py')
    if os.path.exists(entry):
        with open(entry, encoding='utf-8') as fh:
            out['ledger_coverage.py'] = fh.read()
    return out


def string_values(doc, out=None):
    out = set() if out is None else out
    if isinstance(doc, str):
        out.add(doc)
    elif isinstance(doc, dict):
        for v in doc.values():
            string_values(v, out)
    elif isinstance(doc, list):
        for v in doc:
            string_values(v, out)
    return out


def source_values(data, name):
    """String values of a record an adapter reads (a json file). A source file named as a companion (a checker)
    is code, not a record; its string constants are not values of the configuration."""
    try:
        return string_values(json.loads(data.decode('utf-8')))
    except (ValueError, UnicodeDecodeError):
        return set()


def config_values(read, commit, cfg):
    """B5: the value set of one configuration: its own values, every record and rule it references, its controls
    and delegation contract, and every file its adapters read (`path`, `companion`, `module_path`)."""
    values = string_values(cfg)
    refs = list(cfg.get('rules', [])) + list(cfg.get('records', [])) + [cfg.get('controls')] + \
        ([cfg['delegation']] if cfg.get('delegation') else [])
    for r in refs:
        if isinstance(r, dict) and r.get('path'):
            b = read(r.get('commit') or commit, r['path'])
            if b is not None:
                values |= source_values(b, r['path'])
    for spec in (cfg.get('adapters') or {}).values():
        if not isinstance(spec, dict):
            continue
        named = [(spec.get('commit') or commit, spec.get('path'))]
        named += [(c.get('commit') or spec.get('commit') or commit, c.get('path')) for c in spec.get('companion', [])]
        if spec.get('module_path'):
            named.append((spec.get('commit') or commit, spec['module_path']))
        for c, pth in named:
            if pth:
                b = read(c, pth)
                if b is not None:
                    values |= source_values(b, pth)
    return values


def lint_sources(sources, values, profiles):
    """sources: {name: text}; values: strings of the configurations and their records; profiles: compiled
    review and deny profiles of the first configuration. Returns findings."""
    found = lint_allowlist()
    for name, text in sorted(sources.items()):
        try:
            tree = ast.parse(text)
        except SyntaxError as exc:
            found.append('%s: does not parse (%s)' % (name, exc))
            continue
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, str):
                s = node.value
                # R6.CORE.3: the allowlist exempts a value from the value-set clause only; the hexadecimal and
                # profile clauses apply to every literal
                if _hex.search(s):
                    found.append('%s:%d: hexadecimal literal of 7 or more digits' % (name, node.lineno))
                if s in values and s.strip() and not allowed(s):
                    found.append('%s:%d: string literal %r occurs in a configuration or record'
                                 % (name, node.lineno, s[:60]))
                for p in profiles:
                    if p.matches(s):
                        found.append('%s:%d: string literal matched by profile %s' % (name, node.lineno, p.name))
                        break
            elif isinstance(node, ast.Constant) and isinstance(node.value, int) and not isinstance(node.value, bool):
                if len(str(abs(node.value))) >= 7:
                    found.append('%s:%d: numeric literal of 7 or more digits' % (name, node.lineno))
            ids = []
            if isinstance(node, ast.Name):
                ids.append(node.id)
            elif isinstance(node, (ast.FunctionDef, ast.ClassDef)):
                ids.append(node.name)
            elif isinstance(node, ast.Attribute):
                ids.append(node.attr)
            elif isinstance(node, ast.arg):
                ids.append(node.arg)
            for ident in ids:
                for p in profiles:
                    if p.matches(ident):
                        found.append('%s: identifier %r matched by profile %s' % (name, ident, p.name))
                        break
    return found


def lint_engine(values=(), profiles=()):
    return lint_sources(engine_sources(), set(values), list(profiles))
