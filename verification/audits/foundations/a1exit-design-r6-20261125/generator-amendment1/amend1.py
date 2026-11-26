"""Generator of amendment 1 to design r6 (owner decision of 2026-11-26T04:39:58Z, #1169 comment 7182798225).

Usage: python3 -I -B amend1.py BASE OUT

BASE is a directory holding DESIGN-r6.md, EXPECTATIONS.json, REQUIREMENTS.json and LANDING-MANIFEST.md exactly as
they are in verification/audits/foundations/a1exit-design-r6-20261125/ at main 02b8e20839d4700de721f8427b3fe9f3c746b71f
(each checked against its sha256 below). The script reads owner-decision-amendment1.json and, when present,
b4-design-edits.json (the B4 design corrections, a list of anchored edits) beside itself and writes into OUT the amended DESIGN-r6.md, EXPECTATIONS.json and REQUIREMENTS.json, the change record AMENDMENT-1.md and the
updated LANDING-MANIFEST.md. Every text edit is anchored on an exact string that must occur exactly once. After the
edits it runs its self-checks (correspondence in both directions, a second direction on every row in scope, the
closed invariant vocabulary of sec. 16.10, multi-key invariants, identifier uniqueness) and exits nonzero on any
failure. Standard library only; deterministic (no time, no randomness, sorted output where order is free).
"""
import copy
import hashlib
import json
import os
import re
import sys

BASE_SHA256 = {
    'DESIGN-r6.md': '8727f498a621fd45a0dcbb63061483b69b873f747f497f45f00ae416f02685e5',
    'EXPECTATIONS.json': 'a24a7b2bcaf5cdaeee6ca791cd4af11d1787043252d96bcb512825c9df17e847',
    'REQUIREMENTS.json': 'dbdba73379e99c7a4d66228aa7a60fe64af7154efbe9c836b814c768f6988167',
    'LANDING-MANIFEST.md': '0fe34b3b02e43a02faddb1bccae39f60d8b39c85f86df7e8ba481d0afa4df098',
}
HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = 'r6 amendment 1 (owner decision of 2026-11-26T04:39:58Z, #1169 comment 7182798225; %s)'
FLAG_NEW = 'added by amendment 1 (%s); no runner records it before the tool revision implements it'
RESTORED_CLEAN = {'outcome': 'RESULT_EQUAL_CLEAN',
                  'invariants': [{'baseline': 'the same run on the restored (unmutated) tree'}]}
OLD_VD = 'VD-RESTORE: no second direction recorded'
NEW_VD = ('VD-RESTORE: second direction recorded by amendment 1 (B2); restored case or countercase not executed by '
          'the runners of the tool commit')


def sha(b):
    return hashlib.sha256(b).hexdigest()


def once(text, old, new, what):
    n = text.count(old)
    if n != 1:
        raise SystemExit('anchor for %s occurs %d times' % (what, n))
    return text.replace(old, new)


def dumpj(doc):
    return (json.dumps(doc, indent=1, ensure_ascii=False) + '\n').encode('utf-8')


# ------------------------------------------------------------------------------------------------------------------
# B1: the new control rows. Each states a second direction (a restored expectation or direction `both` with a
# countercase); runner null until the tool revision implements it.

def row(rid, req, ops, kind, direction, expect, restored, case, dec='B1'):
    r = {'id': rid, 'requirements': req, 'runner': None, 'operations': ops}
    if direction != 'adversarial':
        r['direction'] = direction
    if kind != 'declarative':
        r['predicate_kind'] = kind
    r['expect'] = expect
    if restored is not None:
        r['restored'] = restored
    r['source'] = SOURCE % dec
    r['flags'] = [FLAG_NEW % dec]
    return r, case


NEW_ROWS = [
    row('PIPE-STAGES', ['R6.PIPE.1'], ['terms'], 'declarative', 'adversarial', {'cases': [
        {'case': 'an unknown flag together with a ledger whose splice hash differs from H',
         'outcome': 'USAGE', 'invariants': [{'no_result_written': True}]},
        {'case': 'a ledger whose splice hash differs from H together with a failing preflight control',
         'outcome': 'ERROR', 'stop_class': 'LEDGER_INTEGRITY', 'invariants': [{'none': 'items'}]},
        {'case': 'a failing preflight control together with a planted deny match',
         'outcome': 'VOID', 'stop_class': 'PREFLIGHT_FAILED', 'invariants': [{'none': 'items[class=deny-match]'}]}]},
        RESTORED_CLEAN,
        'two faults of different stages planted at once: usage with integrity, integrity with a failing preflight '
        'control, a failing preflight control with a deny match; the earlier stage decides and no later stage runs'),
    row('PIPE-REPO', ['R6.PIPE.4'], ['terms'], 'declarative', 'adversarial',
        {'outcome': 'ERROR', 'stop_class': 'UNRESOLVABLE'},
        {'outcome': 'RESULT_EQUAL_CLEAN',
         'invariants': [{'baseline': 'the same run with --repo naming the repository'}]},
        '`--repo` naming an existing directory that is not a git repository'),
    row('PIPE-CHAIN', ['R6.PIPE.6'], ['coverage'], 'declarative', 'both', {'cases': [
        {'case': ['two segments whose consecutive endpoints differ', 'a chain that does not end at the named commit'],
         'outcome': 'ERROR', 'invariants': [{'no_result_written': False}]},
        {'case': 'no --segment, an HP obligation of the configuration naming the segment (positive)',
         'outcome': 'ANY', 'invariants': [{'equals': 'one segment from the pin to the named commit, of kind hp'}]},
        {'case': 'no --segment and no HP obligation naming it (positive)',
         'outcome': 'ANY', 'invariants': [{'equals': 'one unledgered segment from the pin to the named commit'}]}]},
        {'outcome': 'RESULT_EQUAL_CLEAN',
         'invariants': [{'baseline': 'the same run with an unbroken chain from the pin to the named commit'}]},
        'a broken segment chain (consecutive endpoints differ; a chain not ending at the named commit) is an integrity '
        'ERROR with `result.json` (C-12); with no `--segment`, the default segment is of kind `hp` where an HP '
        'obligation names it, else unledgered'),
    row('PIPE-UNRESOLVED', ['R6.PIPE.7'], ['coverage'], 'declarative', 'adversarial', {
        'outcome': 'FAIL', 'classes_include': ['missing'],
        'sites': [{'subject': '$site', 'state': 'unresolved', 'classes_include': ['missing']}],
        'invariants': [{'items_include': [{'subject': '$site', 'segment': '$first_segment'}]},
                       {'none': 'items[subject=$site,segment=$second_segment]'}]},
        {'outcome': 'RESULT_EQUAL_CLEAN',
         'invariants': [{'baseline': 'the same two segments with the site unchanged'}]},
        'a site removed without a splice in the first of two unledgered segments and untouched in the second: FAIL '
        '`missing` (R6.CLASS.2); it stays unresolved and its item carries the first segment'),
    row('PIPE-PRIOR', ['R6.PIPE.8'], ['terms'], 'declarative', 'both', {'cases': [
        {'case': 'a hit present at the prior endpoint and at the named commit',
         'outcome': 'REVIEW_REQUIRED', 'exit': 10,
         'invariants': [{'items_include': [{'subject': '$old_hit', 'pre_existing': True}]}]},
        {'case': 'a hit first present at the named commit (countercase)',
         'outcome': 'REVIEW_REQUIRED', 'exit': 10,
         'invariants': [{'items_include': [{'subject': '$new_hit', 'pre_existing': False}]}]}]},
        None,
        '`pre_existing` computed at the prior endpoint (the last segment\'s FROM): true for a hit already there, false '
        'for a new hit; the exit status reports every item either way'),
    row('ANCH-OVERRIDE', ['R6.ANCH.8'], ['record'], 'declarative', 'both', {'cases': [
        {'case': 'an override whose anchor is not a substring of the pin line',
         'outcome': 'FAIL', 'classes_exact': ['record-invalid'],
         'invariants': [{'record_checks_failed_include': 'pin_findings'}]},
        {'case': 'a valid override whose pin-line text moves after the pin (positive: the anchor is never searched '
                 'later)',
         'outcome': 'ANY', 'invariants': [{'none': 'items[class=record-invalid]'}]}]},
        {'outcome': 'RESULT_EQUAL_CLEAN', 'invariants': [{'baseline': 'the same record with a valid anchor'}]},
        'an override anchor checked once, at the pin: an anchor that is not a substring of the pin line FAILs '
        '`record-invalid` through `record_checks.pin_findings`; a valid anchor is not searched again'),
    row('HP-MERGE-PR', ['R6.HP.1'], ['coverage'], 'declarative', 'adversarial', {
        'outcome': 'ERROR', 'stop_class': 'CONFIG_INVALID', 'invariants': [{'none': 'items'}]},
        {'outcome': 'RESULT_EQUAL_CLEAN',
         'invariants': [{'baseline': 'the same configuration with the merge whose subject names its own pull request'}]},
        'a configuration (control harness) pinning an HP merge whose subject names a different pull-request number: '
        'ERROR `CONFIG_INVALID` before any subject is evaluated'),
    row('HP-SEMCLASS', ['R6.HP.5'], ['coverage'], 'declarative', 'adversarial', {
        'outcome': 'FAIL', 'classes_include': ['record-invalid']},
        {'outcome': 'RESULT_EQUAL_CLEAN',
         'invariants': [{'baseline': 'the same adjudication with its semantic_classification'}]},
        'an HP adjudication entry without `semantic_classification`'),
    row('HP-RECORDS', ['R6.HP.14', 'R6.HP.5'], ['coverage'], 'declarative', 'adversarial', {'cases': [
        {'case': 'an HP record supplied with --hp that fails its schema',
         'outcome': 'FAIL', 'classes_include': ['record-invalid']},
        {'case': 'an HP record whose fingerprint for the site differs (its semantic_classification edited after '
                 'fingerprinting)',
         'outcome': 'FAIL', 'sites': [{'subject': '$site', 'classes_include': ['hp-unadjudicated']}]},
        {'case': 'a record supplied with --classify that the configuration does not reference',
         'outcome': 'FAIL', 'classes_include': ['record-invalid']}]},
        {'outcome': 'RESULT_EQUAL_CLEAN',
         'invariants': [{'baseline': 'the same run with the valid record, which resolves the site'}]},
        'HP records enter through `--hp` or `--classify` under sec. 11: a schema-invalid record and an unreferenced '
        'record are `record-invalid`; a record resolves a site only when every fingerprint matches'),
    row('CTX-INDICATOR', ['R6.CTX.8'], ['coverage'], 'declarative', 'adversarial', {
        'outcome': 'ERROR', 'stop_class': 'CONFIG_UNREVIEWED'},
        {'outcome': 'RESULT_EQUAL_CLEAN',
         'invariants': [{'baseline': 'the same configuration with the preregistered indicator definitions'}]},
        'a configuration whose definition of one meaning-context indicator differs from the configuration it '
        'supersedes, without a widening review (widening, R6.CFG.7; ERROR `CONFIG_UNREVIEWED`, R6.VALID.3)'),
    row('OUT-FROZEN', ['R6.OUT.16'], ['record'], 'declarative', 'adversarial', {
        'outcome': 'INTERNAL',
        'invariants': [{'message_names': 'the exception class and the failing stage'},
                       {'none': 'calls of the frozen main()'}]},
        {'outcome': 'RESULT_EQUAL_CLEAN', 'invariants': [{'baseline': 'the same run without the injected exception'}]},
        'an exception injected into a frozen-code call of op A becomes a structured INTERNAL with its class and stage; '
        'the frozen `main()` is never called'),
    row('OUT-EXPLAIN', ['R6.OUT.22'], ['coverage', 'terms'], 'procedural', 'both', {'cases': [
        {'case': 'a run with a site, a hit, a file, a pin and an item, one item REVIEW_REQUIRED',
         'outcome': 'ANY',
         'invariants': [{'all': 'subjects', 'have': {'explanation': [
             'subject id and kind', 'anchor and its hashes', 'provenance chain', 'rule id and rule blob hash, or null',
             'each matcher\'s result', 'resulting state']}},
             {'all': 'items[decision=REVIEW_REQUIRED]', 'have': {'resolution_needed': 'record kind and fields'}},
             {'equal_field': 'each explanation\'s rule blob hash equals the sha256 of the rule file\'s blob'}]},
        {'case': 'the same result with one subject\'s explanation removed (countercase)',
         'outcome': 'PREDICATE', 'invariants': [{'schema_errors': ['missing explanation']}]}]},
        None,
        'every subject carries an explanation with the fields of R6.OUT.22, its values checked against the run\'s '
        'inputs; a result missing one fails schema validation (the schema part is also tested by '
        'S7-schema-and-checker)'),
    row('OUT-ADAPTERS', ['R6.OUT.25'], ['record'], 'declarative', 'both', {'cases': [
        {'case': 'a run whose adapters read the Phase-0 and Phase-2 record directories (positive)',
         'outcome': 'ANY',
         'invariants': [{'all': 'adapter inputs read', 'have': {'blob_hash_listed_in': 'adapters'}}]},
        {'case': 'the same run with one adapter input blob changed (countercase)',
         'outcome': 'ANY',
         'invariants': [{'equals': 'adapters differs from the first run only in the changed input\'s blob hash'}]}]},
        None,
        'the blob hash of every input an adapter reads is listed in `adapters`; changing one input changes exactly its '
        'entry'),
    row('OUT-NOTRUNC', ['R6.OUT.28'], ['terms'], 'declarative', 'both', {'cases': [
        {'case': 'a synthetic file with 5000 unexplained repo hit lines',
         'outcome': 'REVIEW_REQUIRED', 'counts': {'items[class=unclassified]': 5000}},
        {'case': 'the same file with one hit line removed (countercase)',
         'outcome': 'REVIEW_REQUIRED', 'counts': {'items[class=unclassified]': 4999}}]},
        None,
        'every hit is listed: 5000 hit lines give 5000 items; one fewer gives 4999'),
]

NEW_REQ = {r['requirements'][0]: r['id'] for r, _ in NEW_ROWS}
NEW_REQ_CONTROLS = dict((k, [v]) for k, v in NEW_REQ.items())
NEW_REQ_CONTROLS['R6.OUT.22'] = ['S7-schema-and-checker', 'OUT-EXPLAIN']
NEW_REQ_CONTROLS['R6.HP.5'] = ['HP-SEMCLASS', 'HP-RECORDS']

# B4: design corrections for the B4 records (owner directions of 2026-11-26T04:52:48Z, #1169 comment 7182986451).
# The text edits are the anchored entries of b4-design-edits.json; these are the control rows they name. Parts A
# (post-freeze route) and D (binding to the run's M and X) need the owner's specific approval (sec. 0.2).
B4 = 'B4; owner directions of 2026-11-26T04:52:48Z, #1169 comment 7182986451'
B4_DIRECTIONS = {
    'record': '#1169 comment 7182986451', 'author': 'amaybaum', 'time': '2026-11-26T04:52:48Z',
    'quotes': [
        "Record location | Keep reconciliation records outside the tool's landing paths. Resolve the contradictory "
        "design wording through independent review.",
        'M and X commit identifiers | Complete them when the actual commits exist, using independently reviewed '
        'superseding records.',
        'Records created after freezing | Investigate the conflict now. Do not bypass chain-mode validation or '
        'silently introduce an exception.',
        'Include any necessary design corrections in the consolidated amendment where practical, rather than '
        'creating another series of amendments.',
        'Do not introduce multi-path reconciliation merely to accommodate #1560. We should avoid further expansion '
        'of the verification tool when a simpler solution exists.']}
POSTF_POS = {'outcome': 'ANY', 'invariants': [{'record_admitted': '$record'}]}
REC_INVALID = {'outcome': 'FAIL', 'classes_include': ['record-invalid']}


def fcase(text, extra=None):
    c = dict(case=text, **REC_INVALID)
    if extra:
        c['classes_include'] = c['classes_include'] + extra
    return c


B4_ROWS = [
    row('POSTF-1', ['R6.RECON.2', 'R6.REC.4'], ['execution'], 'declarative', 'both', {'cases': [
        {'case': 'a reviewed reconciliation record and its review record in one reconciliation directory at REV, '
                 'named by --classify REV:PATH, covering a ledgered path changed on M by a commit that is not an '
                 'ancestor of F, every condition RC1-RC13 holding (positive)',
         'outcome': 'ANY',
         'invariants': [{'record_admitted': '$record'}, {'none': 'items[class=record-invalid]'},
                        {'none': 'items[class=base-drift]'},
                        {'equals': 'inputs.classify_records lists the record with its rev, path and sha256 and the '
                                   'path and sha256 of its review record'}]},
        {'case': 'a reviewed side-change class record and its review record at REV, pinning a path changed on M by '
                 'a commit that is not an ancestor of F (positive)',
         'outcome': 'ANY',
         'invariants': [{'record_admitted': '$record'}, {'none': 'items[class=side-change-unclassified]'}]},
        {'case': 'countercase: the same run without the reconciliation record',
         'outcome': 'FAIL', 'classes_include': ['base-drift']}]},
        None,
        'post-freeze route (R6.RECON.2): a reviewed reconciliation or side-change class record written after `F` '
        'for a path changed on `M` after `F`, named by `--classify REV:PATH`, is admitted in the `M` role and listed '
        'in `inputs.classify_records` with its review; without it the path is `base-drift`', B4),
    row('POSTF-2', ['R6.RECON.2'], ['execution'], 'declarative', 'adversarial', {'cases': [
        fcase('a reviewed reconciliation record named by --classify REV:PATH whose covered path is changed on M only '
              'by commits that are ancestors of F', ['base-drift']),
        fcase('a reviewed side-change class record named by --classify REV:PATH one of whose pinned paths is '
              'changed on M only by commits that are ancestors of F')]},
        POSTF_POS,
        'a post-freeze record covering a path that no commit on `M` after `F` changed: FAIL `record-invalid`; the '
        'restored case is the POSTF-1 input', B4),
    row('POSTF-3', ['R6.RECON.2', 'R6.REC.5'], ['execution'], 'declarative', 'adversarial', {'cases': [
        fcase('a reviewed hit-classification record written after F, named by --classify REV:PATH from a '
              'reconciliation directory'),
        fcase('a reviewed HP adjudication written after F, named the same way')]},
        {'outcome': 'RESULT_EQUAL_CLEAN', 'invariants': [{'baseline': 'the same run without the record'}]},
        'a record of another kind written after `F` and not referenced by the configuration: FAIL `record-invalid`, '
        'never used', B4),
    row('POSTF-4', ['R6.RECON.2', 'R6.REC.7'], ['execution'], 'declarative', 'adversarial', {'cases': [
        fcase("no review record naming the record's blob in the same directory of REV's tree"),
        fcase("two review records naming the record's blob in that directory"),
        fcase("another record in that directory of REV's tree supersedes the record"),
        fcase('two records in the reconciliation directory at REV supersede the same predecessor')]},
        POSTF_POS,
        'post-freeze review and lineage: no review, two reviews, a superseded record and ambiguous ancestry in the '
        'reconciliation directory at `REV` are each FAIL `record-invalid`; the restored case is the POSTF-1 input',
        B4),
    row('POSTF-5', ['R6.RECON.2', 'R6.RECON.1'], ['execution'], 'declarative', 'adversarial', {'cases': [
        fcase('PATH under a prefix of the tool-landing class'),
        fcase("PATH inside the plan's record directory"),
        fcase('the review record in a directory other than the record\'s')]},
        POSTF_POS,
        'a post-freeze record outside a reconciliation directory (under a tool-landing prefix, inside the plan\'s '
        'record directory) or with its review elsewhere: FAIL `record-invalid`; the restored case is the POSTF-1 '
        'input', B4),
    row('RTL2-BIND', ['R6.RECON.21'], ['execution'], 'procedural', 'both', {'cases': [
        {'case': "a reviewed reconciliation record bound to the run: ledger_base the run's H, naming the run's M and "
                 "X, its m and x the path's blobs at the run's M and C (positive)",
         'outcome': 'PASS', 'invariants': [{'drift_state_in': ['reconciled']}]},
        {'case': "countercase: the same record naming a commit other than the run's M",
         'outcome': 'FAIL', 'invariants': [{'drift_state_in': ['unresolved']}]},
        {'case': "countercase: the same record naming a commit other than the run's X",
         'outcome': 'FAIL', 'invariants': [{'drift_state_in': ['unresolved']}]},
        {'case': 'countercase: the same record with M and X null',
         'outcome': 'FAIL', 'invariants': [{'drift_state_in': ['unresolved']}]}]},
        None,
        'the binding clause of R6.RECON.21: a reviewed record that does not name the run\'s `M` and `X` leaves the '
        'drift state unresolved (synthetic configuration)', B4),
]
B4_ROWS[5][0]['procedure'] = {'name': 'rtl2-binding', 'lib': 'rtl2',
                              'evidence': ['run result.json', 'each reconciliation record used and its review record',
                                           "the run's H, M, X and C"]}
B4_REQ_CONTROLS = {}
for _r, _ in B4_ROWS:
    for _q in _r['requirements']:
        B4_REQ_CONTROLS.setdefault(_q, []).append(_r['id'])
PENDING_A = ("amendment 1, B4 part A (post-freeze route of R6.RECON.2): needs the owner's specific approval; the "
             "alternative is a new configuration version and a new freeze (R6.CFG.3)")
PENDING_D = ("amendment 1, B4 part D (the binding names the run's M and X): needs the owner's specific approval")
B4_PENDING = {'R6.REC.4': PENDING_A, 'R6.RECON.2': PENDING_A, 'R6.REC.5': PENDING_A, 'R6.CFG.4': PENDING_A,
              'R6.OUT.5': PENDING_A, 'R6.VALID.3': PENDING_A, 'R6.RECON.21': PENDING_D}

# B2: the 42 rows. Positive rows take a countercase (direction `both`), N10 and N11 pair, the rest a restored case.
COUNTERCASES = {
    'RT-L2': {'case': 'countercase: the same run with the reconciliation record unreviewed (drafted)',
              'outcome': 'FAIL', 'invariants': [{'drift_state_in': ['unresolved']}]},
    'RT-X': {'case': 'countercase: the side-change class record without the workflow path',
             'outcome': 'REVIEW_REQUIRED', 'classes_include': ['side-change-unclassified']},
    'TT8': {'case': 'countercase: the same landing with a ledgered path changed on main after H',
            'outcome': 'FAIL', 'classes_include': ['base-drift']},
    'N3-config-route': {'case': 'countercase: the same record, supplied through the configuration\'s `records`, with '
                                'its `ledger_binding` altered by one byte',
                        'outcome': 'FAIL', 'classes_include': ['base-drift'],
                        'invariants': [{'failed_conditions_include': 'RC13'}]},
    'TT13': {'case': 'countercase: a tool-landing path whose blob differs from its class pin',
             'outcome': 'REVIEW_REQUIRED', 'classes_include': ['side-change-unclassified']},
}
POSITIVE_CASE = 'the control input (positive)'
PAIRS = {'N10': ['N11'], 'N11': ['N10'], 'N3': ['N4']}
EXTRA_PAIRS = {'N4': ['N3']}
Z9H_RESTORED = {'outcome': 'LINT_PASS',
                'invariants': [{'baseline': "the same lint with 'guard-pin' removed from the engine module"}]}


def in_scope_missing(rows):
    out = []
    for r in rows:
        if r['id'].startswith(('MUT:', 'GATE-')):
            continue
        d = r.get('direction', 'adversarial')
        dof = d.get('of') if isinstance(d, dict) else d
        if isinstance(d, dict) and ('scope' in d or d.get('exempt') == 'observation'):
            continue
        if dof == 'both' or r.get('restored') is not None or r.get('paired_with'):
            continue
        out.append(r['id'])
    return out


def amend_expectations(E):
    E = copy.deepcopy(E)
    rows = E['rows']
    by = {r['id']: r for r in rows}
    missing = in_scope_missing(rows)
    if len(missing) != 42:
        raise SystemExit('expected 42 rows without a second direction, found %d' % len(missing))
    changes = []
    for rid in missing:
        r = by[rid]
        if rid in PAIRS:
            r['paired_with'] = PAIRS[rid]
            how = 'paired_with %s' % PAIRS[rid][0]
        elif rid == 'RT-L':
            if not any('mutant' in json.dumps(c['case']) for c in r['expect']['cases']):
                raise SystemExit('RT-L has no mutant case')
            r['direction'] = dict(r['direction'], of='both')
            how = 'direction both (its mutant case "L carries H\'s workflow copy" is the opposite direction)'
        elif rid in COUNTERCASES:
            if 'cases' in r['expect']:
                raise SystemExit('%s already has cases' % rid)
            first = dict(case=POSITIVE_CASE, **r['expect'])
            r['expect'] = {'cases': [first, COUNTERCASES[rid]]}
            r['direction'] = dict(r['direction'], of='both')
            how = 'direction both with countercase "%s"' % COUNTERCASES[rid]['case']
        elif rid == 'Z9h':
            r['restored'] = Z9H_RESTORED
            how = 'restored LINT_PASS (the lint without the planted value)'
        else:
            r['restored'] = copy.deepcopy(RESTORED_CLEAN)
            how = 'restored RESULT_EQUAL_CLEAN (the same run on the unmutated tree)'
        if rid == 'Z9h':
            r['flags'] = [NEW_VD if f.startswith('VD-RESTORE') else f for f in r.get('flags', [])]
        else:
            r['flags'] = [NEW_VD if f.startswith(OLD_VD) else f for f in r.get('flags', [])]
        r['source'] = r['source'] + '; second direction: ' + SOURCE % 'B2'
        changes.append((rid, 'B2', how))
    for rid, p in EXTRA_PAIRS.items():
        by[rid]['paired_with'] = p
        changes.append((rid, 'B2', 'also paired_with %s (reciprocal of %s)' % (p[0], p[0])))
    s7 = by['S7-schema-and-checker']
    s7['requirements'] = s7['requirements'] + ['R6.OUT.22']
    changes.append(('S7-schema-and-checker', 'B1', 'names R6.OUT.22 (the explanation is part of the JSON Schema '
                                                    'the row validates every written result against)'))
    for r, case in NEW_ROWS:
        if r['id'] in by:
            raise SystemExit('new id %s already a row' % r['id'])
        rows.append(r)
        changes.append((r['id'], 'B1', 'new row for %s' % r['requirements'][0]))
    for r, case in B4_ROWS:
        if r['id'] in by:
            raise SystemExit('new id %s already a row' % r['id'])
        rows.append(r)
        changes.append((r['id'], 'B4', 'new row for %s' % ', '.join(r['requirements'])))
    return E, changes


def amend_requirements(R):
    R = copy.deepcopy(R)
    by = {q['id']: q for q in R}
    for rid, ctl in NEW_REQ_CONTROLS.items():
        q = by[rid]
        if q['controls'] or q['kind'] != 'testable':
            raise SystemExit('%s: not a testable requirement without controls' % rid)
        q['controls'] = list(ctl)
    for rid, after in (('R6.REC.18', 'TR28-consumer'), ('R6.CTRL.23', 'TR28-tool')):
        c = by[rid]['controls']
        if 'TR28' in c:
            raise SystemExit('%s already names TR28' % rid)
        c.insert(c.index(after) + 1, 'TR28')
    for rid, ctl in sorted(B4_REQ_CONTROLS.items()):
        q = by[rid]
        if q['kind'] != 'testable' or set(ctl) & set(q['controls']):
            raise SystemExit('%s: B4 controls' % rid)
        q['controls'] = q['controls'] + ctl
    for rid, note in sorted(B4_PENDING.items()):
        if by[rid]['pending_owner_confirmation']:
            raise SystemExit('%s: pending_owner_confirmation not empty' % rid)
        by[rid]['pending_owner_confirmation'] = [note]
    return R


# ------------------------------------------------------------------------------------------------------------------
# DESIGN-r6.md

def table_row(r, case, dec='B1'):
    kind = 'proc' if r.get('predicate_kind') == 'procedural' else 'decl'
    d = r.get('direction', 'adversarial')
    dof = d.get('of') if isinstance(d, dict) else d
    dirs = {'adversarial': 'adv', 'positive': 'pos', 'both': 'both'}[dof]
    return '| %s | %s | to be implemented (tool revision) | %s | %s | %s (amendment 1, %s) |' % (
        r['id'], ', '.join(r['requirements']), kind, dirs, case, dec)


COUNTS = ''
B4_EDITS = []
B4_SHA = None


def counts_text(E):
    rows = [r for r in E['rows'] if not r['id'].startswith(('MUT:', 'GATE-'))]

    def dof(r):
        d = r.get('direction', 'adversarial')
        return d.get('of') if isinstance(d, dict) else d
    n_out = sum(1 for r in rows if isinstance(r.get('direction'), dict) and 'scope' in r['direction'])
    n_ex = sum(1 for r in rows if isinstance(r.get('direction'), dict) and r['direction'].get('exempt') == 'observation')
    return ('%d rows, %d of them recording `scope: "outside"`; %d carry a `restored` expectation, %d declare '
            'direction `both`, %d name `paired_with`, %d are exempt as observations'
            % (len(rows), n_out, sum(1 for r in rows if r.get('restored') is not None),
               sum(1 for r in rows if dof(r) == 'both'), sum(1 for r in rows if r.get('paired_with')), n_ex))


def apply_b4(t):
    # Design corrections for the B4 records, supplied as anchored edits in b4-design-edits.json beside this script
    # (absent until that text is provided): [{"label", "anchor", "replacement"}], each anchor occurring once.
    for e in B4_EDITS:
        t = once(t, e['anchor'], e['replacement'], 'B4 ' + e['label'])
    return t


def b4_note():
    d = B4_DIRECTIONS
    return (
        'B4 design corrections. The owner\'s directions on the questions raised by the B4 records are recorded at %s '
        '(%s, %s). Quoted (table cells joined by " | ", table padding removed; each line prefixed by "> "):\n\n'
        % (d['record'], d['author'], d['time'])
        + '\n>\n'.join('> ' + x for x in d['quotes']) + '\n\n'
        '- Part A, records written after `F` (needs the owner\'s specific approval). R6.REC.4 and R6.RECON.2 admit a '
        'record written after `F`, while R6.REC.4, R6.REC.5, R6.CFG.4 (`records`), R6.OUT.5 and R6.VALID.3 require '
        'the configuration at `F` to reference every record a run uses and make any other record `record-invalid`, '
        'and R6.CFG.3 requires a new configuration version and a new freeze for any change to the configuration. '
        'Chain-mode admission implements the second set, so the admission R6.RECON.2 states is unreachable. Part A '
        'makes it reachable by the post-freeze route of R6.RECON.2, conditions (a) to (e), each checked by the tool '
        'from git objects: only reconciliation and side-change class records with their review records, only for '
        'paths changed on `M` after `F`, and only in the `M` role. Configuration admission, execution identity and '
        'chain-mode validation are otherwise unchanged, and every other unreferenced record stays `record-invalid`. '
        'Controls POSTF-1 to POSTF-5. The alternative, which adds no route, narrows R6.RECON.2 and R6.REC.4 to a new '
        'configuration version and a new freeze (R6.CFG.3) for every record written after `F`; it needs a freeze '
        '(AGENTS.md sec. A.50 item 5) whenever `M` gains a side change after `F` before the landing. The owner '
        'chooses between them; until then part A is proposed text that no tool revision implements, and the '
        'requirements it touches carry it in `pending_owner_confirmation`.\n'
        '- Part B, record location (owner direction; independent review). R6.RECON.1, R6.REC.1 and R6.PLACE.5 placed '
        'reconciliation records in the tool\'s audit directory, a prefix of the tool\'s landing paths (R6.PLACE.8), '
        'while R6.RECON.21 and R6.EVID.8 require them outside those paths. They lie in a reconciliation directory '
        '(R6.RECON.1), and R6.REC.7\'s ambiguous-ancestry scope includes those directories.\n'
        '- Part D, binding (needs the owner\'s specific approval). R6.RECON.21\'s binding clause requires the record '
        'to name the run\'s `M` and also its `X`, so that `M` and `X` completed by a superseding record are checked '
        'against the run; control RTL2-BIND. It strengthens the clause and adds no requirement identifier.\n\n')


def amend_design(t, owner):
    q = owner['quotes']
    note = (
        '\n### 0.2 Amendment 1 of 2026-11-26\n\n'
        'The owner decided on the brief of 2026-11-26 in the coordinating session; the decision is recorded at %s '
        '(%s, %s). Quoted (part 1 of the decision record), byte-exact as relayed (each line prefixed by "> "):\n\n' % (
            owner['record'], owner['author'], owner['time'])
        + '\n>\n'.join('> ' + x for x in q) + '\n\n'
        'Amendment 1 applies the decisions on B1, B2, B3 and B5, which weaken no requirement and add no exemption, and '
        'the B4 design corrections stated after this list; AMENDMENT-1.md maps each change to its decision:\n\n'
        '- B1. The 14 testable requirements that named no control (R6.PIPE.1, R6.PIPE.4, R6.PIPE.6, R6.PIPE.7, '
        'R6.PIPE.8, R6.ANCH.8, R6.HP.1, R6.HP.5, R6.HP.14, R6.CTX.8, R6.OUT.16, R6.OUT.22, R6.OUT.25, R6.OUT.28) each '
        'name a control: 14 new rows, and R6.OUT.22 also names S7-schema-and-checker, which validates every written '
        'result against the JSON Schema that holds the explanation. S7-schema-and-checker does not test the '
        'explanation\'s values, so it does not fully cover R6.OUT.22 alone; OUT-EXPLAIN tests them. Each new row '
        'records a second direction.\n'
        '- B2. Each of the 42 rows in the both-directions scope of R6.CTRL.3 that recorded no second direction records '
        'one: 33 by a `restored` expectation; N10 and N11 by `paired_with` (the same run differing only in the landing '
        'blob of `AGENTS.md` and the record\'s `l` naming it); N3 by `paired_with` N4 (the same record with its '
        '`ledger_binding` altered by one byte; N4 also names N3); and RT-L, RT-L2, RT-X, TT8, TT13 and '
        'N3-config-route by direction `both` (RT-L by its existing mutant case, the others by a countercase).\n'
        '- B3. R6.REC.18 and R6.CTRL.23 name the composite TR28, as Table 17.1 states.\n'
        '- B5. R6.GATE.3 states the reading of multi-key invariant objects.\n'
        '- The identifier migration of sec. 34 (OBL-22) is not applied by this amendment: OBL-22 places it in the tool '
        'revision that implements the gate. The owner\'s approval of it is quoted above ("Identifier rename"). The '
        '`runner` fields keep their cites; they are refreshed from the tool revision\'s final lines when it lands, '
        'and the gate never reads them (R6.GATE.9).\n'
        '- B4. The records themselves are drafted and reviewed on a separate branch; the design corrections that '
        'drafting them showed to be needed are stated after this list.\n\n'
        + b4_note() +
        'Amendment 1 is a design change under its own independent review; it adopts nothing beyond the quoted '
        'decisions and authorizes no merge, dispatch, freeze or trial.\n')
    t = once(t, '\n***\n\n## 1. Notation and symbols', '\n' + note + '\n***\n\n## 1. Notation and symbols', '0.2 note')
    # B1: the requirements' Controls lists
    t = once(t, 'Sources: E-058, V1-035. Controls: none (no control checks the stage order directly; X1 and '
                'R6.OUT.9\'s\nprecedence depend on it).',
             'Sources: E-058, V1-035. Controls: PIPE-STAGES.', 'R6.PIPE.1')
    plain = {'R6.PIPE.4': 'V1-017', 'R6.PIPE.6': 'V1-022, V1-036, V1-069', 'R6.PIPE.7': 'V1-038',
             'R6.PIPE.8': 'V1-024', 'R6.ANCH.8': 'V1-046', 'R6.HP.1': 'E-064, RV-020, V2-036', 'R6.HP.5': 'V2-041',
             'R6.HP.14': 'V1-023', 'R6.CTX.8': 'E-083', 'R6.OUT.16': 'E-105', 'R6.OUT.22': 'E-109, V2-066',
             'R6.OUT.25': 'V1-020', 'R6.OUT.28': 'V1-067'}
    for rid, src in plain.items():
        start = t.index('**%s**' % rid)
        end = t.index('\n\n', start)
        block = t[start:end]
        old = 'Sources: %s. Controls: none.' % src
        if block.count(old) != 1:
            raise SystemExit('Controls anchor of %s' % rid)
        t = t[:start] + block.replace(old, 'Sources: %s. Controls: %s.' % (src, ', '.join(NEW_REQ_CONTROLS[rid]))) \
            + t[end:]
    t = once(t, '''Testable requirements with no control in the expectation file; each needs a control row before r6 is final, and each is a named blocker on the correspondence check (rows added by r6 for R6.PUR.12, R6.ANCH.10, R6.ANCH.12, R6.ANCH.15, R6.HP.7, R6.OUT.7 and R6.OUT.20 are named in those requirements):

- R6.PIPE.1 (stage order), R6.PIPE.4 (`--repo`), R6.PIPE.6 (segment chain and default segment),
  R6.PIPE.7 (state carried across segments), R6.PIPE.8 (prior endpoint), R6.PIPE.15 (only partly: CLASS-RETAINED tests `retained-changed`; `ignored_fields` and the unknown schema id have no control);
- R6.ANCH.8 (override anchors; RD-27);
- R6.HP.1 (merge cross-check), R6.HP.5 (presence of `semantic_classification`), R6.HP.14 (supply of HP records);
- R6.CTX.8 (indicator change is widening);
- R6.OUT.16 (frozen-code wrapping), R6.OUT.22 (explanation),
  R6.OUT.25 (adapter input hashes), R6.OUT.28 (no truncation; RD-15);
- R6.SPLIT.3 (conformance check, OD-23; a reading check, not a control).''',
             '''Testable requirements that named no control in the adopted expectation file name one by amendment 1 (sec. 0.2, B1): R6.PIPE.1 (stage order) PIPE-STAGES; R6.PIPE.4 (`--repo`) PIPE-REPO; R6.PIPE.6 (segment chain and default segment) PIPE-CHAIN; R6.PIPE.7 (state carried across segments) PIPE-UNRESOLVED; R6.PIPE.8 (prior endpoint) PIPE-PRIOR; R6.ANCH.8 (override anchors; RD-27) ANCH-OVERRIDE; R6.HP.1 (merge cross-check) HP-MERGE-PR; R6.HP.5 (presence of `semantic_classification`) HP-SEMCLASS; R6.HP.14 (supply of HP records) HP-RECORDS; R6.CTX.8 (indicator change is widening) CTX-INDICATOR; R6.OUT.16 (frozen-code wrapping) OUT-FROZEN; R6.OUT.22 (explanation) S7-schema-and-checker and OUT-EXPLAIN; R6.OUT.25 (adapter input hashes) OUT-ADAPTERS; R6.OUT.28 (no truncation; RD-15) OUT-NOTRUNC. Rows added by r6 for R6.PUR.12, R6.ANCH.10, R6.ANCH.12, R6.ANCH.15, R6.HP.7, R6.OUT.7 and R6.OUT.20 are named in those requirements. Still covered only in part:

- R6.PIPE.15 (CLASS-RETAINED tests `retained-changed`; `ignored_fields` and the unknown schema id have no control);
- R6.SPLIT.3 (conformance check, OD-23; a reading check, not a control).''', 'no-control section')
    # B3
    t = once(t, 'Controls: TR14, TR14-tool, TR15, TR28-tool, TR28-consumer,\nTR29,',
             'Controls: TR14, TR14-tool, TR15, TR28-tool, TR28-consumer, TR28,\nTR29,', 'R6.REC.18 TR28')
    t = once(t, 'TR15-consumer, TR28-consumer, TR28-tool, TR29, TR29-tool, TR30, TR45-opB, TR45-opC, TR46, TR48, '
                'TR50, TR50-consumer, TR51, TR51-consumer, TR52, TR52-consumer.',
             'TR15-consumer, TR28-consumer, TR28-tool, TR28, TR29, TR29-tool, TR30, TR45-opB, TR45-opC, TR46, TR48, '
             'TR50, TR50-consumer, TR51, TR51-consumer, TR52, TR52-consumer.', 'R6.CTRL.23 TR28')
    # B5
    t = once(t, '  section (16.10). An unknown key makes the file invalid.',
             '  section (16.10). An unknown key makes the file invalid. An object may hold several keys when every\n'
             '  key is in the vocabulary and their combined meaning is unambiguous (a key such as `all`, `condition`,\n'
             '  `arm` or `each_listed_line` with its companion `have`, `holds`, `equals`, `has` or `reason`); it\n'
             '  counts as one condition. The gate lists every such object in `gate-result.json`\n'
             '  (`compound_invariants`), and each listed object is reviewed for an unambiguous combined meaning\n'
             '  (amendment 1, B5).', 'R6.GATE.3 B5')
    # B2: counts in R6.CTRL.3 and OBL-20
    t = once(t, '42 rows in scope record no second direction (`direction-missing`), and 217 rows are flagged VD-RESTORE.',
             '42 rows in scope recorded no second direction (`direction-missing`), and 217 rows are flagged VD-RESTORE\n'
             '(these figures are those of the adopted file, before amendment 1). Amendment 1 (sec. 0.2) records a second\n'
             'direction on each of those 42 rows and adds 14 rows (B1) and %d rows (B4), each with one. Counted\n'
             'mechanically over the amended file\'s rows outside the MUT and GATE namespaces (%s): no row in scope\n'
             'records no second direction.'
             % (len(B4_ROWS), COUNTS), 'R6.CTRL.3 counts')
    t = once(t, 'mechanically from the per-row decisions of R6.CTRL.3 (42 of them record no second direction and are\n'
                'reported as `direction-missing`).',
             'mechanically from the per-row decisions of R6.CTRL.3 (42 of them recorded no second direction and were\n'
             'reported as `direction-missing`; amendment 1 records one on each, so their remaining defect is the\n'
             'execution of the recorded case).', 'OBL-20')
    # Table 17.1: direction cells and new rows
    for rid in ('RT-L', 'RT-L2', 'RT-X', 'TT8', 'TT13'):
        m = [x for x in re.finditer(r'^\| %s \| [^|\n]* \| [^|\n]* \| (?:decl|proc) \| [^\n]*$' % re.escape(rid), t, re.M)]
        if len(m) != 1:
            raise SystemExit('table row %s found %d times' % (rid, len(m)))
        line = m[0].group(0)
        cells = line.split(' | ')
        if cells[4] != 'pos':
            raise SystemExit('table row %s direction %r' % (rid, cells[4]))
        cells[4] = 'both'
        new = ' | '.join(cells)
        t = t[:m[0].start()] + new + t[m[0].end():]
    s7 = [x for x in re.finditer(r'^\| S7-schema-and-checker \| [^\n]*$', t, re.M)]
    if len(s7) != 1:
        raise SystemExit('S7 table row')
    line = s7[0].group(0)
    cells = line.split(' | ')
    if 'R6.OUT.22' in cells[1]:
        raise SystemExit('S7 row already names R6.OUT.22')
    cells[1] = cells[1] + ', R6.OUT.22'
    t = t[:s7[0].start()] + ' | '.join(cells) + t[s7[0].end():]
    anchor = [x for x in re.finditer(r'^\| REP-BUILD \| R6\.EVID\.8 \| [^\n]*$', t, re.M)]
    if len(anchor) != 1:
        raise SystemExit('REP-BUILD table row')
    ins = '\n'.join([table_row(r, c) for r, c in NEW_ROWS] + [table_row(r, c, 'B4') for r, c in B4_ROWS])
    t = t[:anchor[0].end()] + '\n' + ins + t[anchor[0].end():]
    return t


def vocabulary(t):
    a = t.index('### 16.10 Annex: invariant vocabulary')
    b = t.index('***', a)
    return set(re.findall(r'`([A-Za-z_0-9]+)`', t[t.index('\n\n', t.index('A key outside it', a)):b]))


def self_checks(E, R, t):
    rows = {r['id']: r for r in E['rows']}
    reqs = {q['id']: q for q in R}
    retired = {x['old_id'] for x in E['retired']}
    problems = []
    named = set()
    for q in R:
        for c in q['controls']:
            named.add(c)
            if c not in rows:
                problems.append('%s names %s, not a row' % (q['id'], c))
        if not q['controls'] and q['kind'] == 'testable':
            problems.append('%s: testable, no control' % q['id'])
        for c in q['controls']:
            if c in rows and q['id'] not in rows[c]['requirements']:
                problems.append('%s names %s, which does not list it' % (q['id'], c))
    for rid, r in rows.items():
        if rid not in named:
            problems.append('row %s named by no requirement' % rid)
        for x in r['requirements']:
            if x not in reqs:
                problems.append('row %s: requirement %s absent' % (rid, x))
            elif rid not in reqs[x]['controls'] and rid in [n[0].get('id') for n in NEW_ROWS + B4_ROWS]:
                problems.append('row %s lists %s, which does not name it' % (rid, x))
        for p in r.get('paired_with', []):
            if p not in rows:
                problems.append('row %s pairs with %s, not a row' % (rid, p))
    for rid in in_scope_missing(E['rows']):
        problems.append('row %s: no second direction' % rid)
    vocab = vocabulary(t)
    if len(vocab) != 153:
        problems.append('vocabulary has %d keys' % len(vocab))

    def walk_exp(rid, e):
        if not e:
            return
        for inv in e.get('invariants', []):
            for k in inv:
                if k not in vocab:
                    problems.append('row %s: invariant key %s outside the vocabulary' % (rid, k))
        for c in e.get('cases', []):
            walk_exp(rid, c)
    for rid, r in rows.items():
        walk_exp(rid, r.get('expect'))
        walk_exp(rid, r.get('restored'))
    for r, _ in NEW_ROWS + B4_ROWS:
        if r['id'] in retired:
            problems.append('new id %s is retired' % r['id'])
    # B4: each requirement a B4 row lists names it in its DESIGN-r6.md block (the Controls line edited by the
    # anchored B4 entries), and every B4 table row is present.
    for rid, ctl in B4_REQ_CONTROLS.items():
        start = t.index('**%s**' % rid)
        nxt = re.compile(r'\n(?:\*\*R6\.|\*\*\*|#)').search(t, start + 1)
        cl = t[start:nxt.start()].split('Controls:')[-1]
        for c in ctl:
            if not re.search(r'(?<![A-Za-z0-9-])%s(?![A-Za-z0-9-])' % re.escape(c), cl):
                problems.append('%s: DESIGN Controls line does not name %s' % (rid, c))
    for r, _ in B4_ROWS:
        if len(re.findall(r'^\| %s \| ' % re.escape(r['id']), t, re.M)) != 1:
            problems.append('table row %s not present once' % r['id'])
    return problems


BASE_DIR = None


def main():
    global BASE_DIR
    if len(sys.argv) != 3:
        sys.stderr.write('usage: amend1.py BASE OUT\n')
        return 64
    BASE_DIR, out = sys.argv[1], sys.argv[2]
    data = {}
    for n, h in BASE_SHA256.items():
        with open(os.path.join(BASE_DIR, n), 'rb') as f:
            data[n] = f.read()
        if sha(data[n]) != h:
            sys.stderr.write('%s: sha256 %s, expected %s\n' % (n, sha(data[n]), h))
            return 65
    with open(os.path.join(HERE, 'owner-decision-amendment1.json'), 'rb') as f:
        owner_b = f.read()
    owner = json.loads(owner_b)
    E0 = json.loads(data['EXPECTATIONS.json'])
    R0 = json.loads(data['REQUIREMENTS.json'])
    E, changes = amend_expectations(E0)
    R = amend_requirements(R0)
    global COUNTS
    COUNTS = counts_text(E)
    b4p = os.path.join(HERE, 'b4-design-edits.json')
    global B4_SHA
    if os.path.exists(b4p):
        with open(b4p, 'rb') as f:
            b4b = f.read()
        B4_SHA = sha(b4b)
        B4_EDITS.extend(json.loads(b4b))
    t = apply_b4(amend_design(data['DESIGN-r6.md'].decode('utf-8'), owner))
    problems = self_checks(E, R, t)
    if problems:
        sys.stderr.write('self-check failures:\n' + '\n'.join(problems) + '\n')
        return 1
    outs = {'EXPECTATIONS.json': dumpj(E), 'REQUIREMENTS.json': dumpj(R), 'DESIGN-r6.md': t.encode('utf-8')}
    with open(os.path.join(HERE, 'amend1.py'), 'rb') as f:
        gen_sha = sha(f.read())
    outs['AMENDMENT-1.md'] = change_record(changes, owner, outs, gen_sha, sha(owner_b)).encode('utf-8')
    outs['LANDING-MANIFEST.md'] = manifest(data['LANDING-MANIFEST.md'].decode('utf-8'), outs, gen_sha,
                                           sha(owner_b)).encode('utf-8')
    os.makedirs(out, exist_ok=True)
    for n, b in sorted(outs.items()):
        with open(os.path.join(out, n), 'wb') as f:
            f.write(b)
        print('%s %s' % (sha(b), n))
    return 0


def change_record(changes, owner, outs, gen_sha, owner_sha):
    lines = [
        '# r6 amendment 1: change record',
        '',
        'Owner decision (%s, %s; %s, relayed by the %s), quoted (part 1 of the decision record) in DESIGN-r6.md sec. 0.2. Generated by '
        'generator-amendment1/amend1.py (sha256 %s) from the directory at main 02b8e20839d4700de721f8427b3fe9f3c746b71f '
        'and generator-amendment1/owner-decision-amendment1.json (sha256 %s). This record maps every change to the '
        'decision it implements; it adopts nothing beyond that decision and authorizes no merge, dispatch, freeze or '
        'trial.' % (owner['author'], owner['time'], owner['record'], owner['relayed_by'], gen_sha, owner_sha)
        + (' The B4 design corrections implement the owner\'s directions of %s (%s, %s), quoted in DESIGN-r6.md sec. '
           '0.2, from generator-amendment1/b4-design-edits.json (sha256 %s).'
           % (B4_DIRECTIONS['time'], B4_DIRECTIONS['author'], B4_DIRECTIONS['record'], B4_SHA) if B4_EDITS else ''),
        '',
        '## 1. Expectation file and requirement list',
        '',
        '| Row or requirement | Decision | Change |',
        '|---|---|---|',
    ]
    for rid, dec, how in changes:
        lines.append('| %s | %s | %s |' % (rid, dec, how))
    for rid, ctl in sorted(NEW_REQ_CONTROLS.items()):
        lines.append('| %s | B1 | controls: %s |' % (rid, ', '.join(ctl)))
    lines += ['| R6.REC.18 | B3 | controls: TR28 added after TR28-consumer |',
              '| R6.CTRL.23 | B3 | controls: TR28 added after TR28-tool |']
    for rid, ctl in sorted(B4_REQ_CONTROLS.items()):
        lines.append('| %s | B4 | controls: %s appended |' % (rid, ', '.join(ctl)))
    for rid, note in sorted(B4_PENDING.items()):
        lines.append('| %s | B4 | pending_owner_confirmation: "%s" |' % (rid, note))
    lines += ['']
    lines += [
        '## 2. DESIGN-r6.md',
        '',
        '| Place | Decision | Change |',
        '|---|---|---|',
        '| sec. 0.2 (new) | all | the owner decision quoted byte-exact as relayed; the scope of amendment 1 |',
        '| R6.PIPE.1, R6.PIPE.4, R6.PIPE.6, R6.PIPE.7, R6.PIPE.8, R6.ANCH.8, R6.HP.1, R6.HP.5, R6.HP.14, R6.CTX.8, '
        'R6.OUT.16, R6.OUT.22, R6.OUT.25, R6.OUT.28 | B1 | "Controls: none" replaced by the controls named in sec. 1 |',
        '| "Requirements of sections 0 to 8 with no control" | B1 | the list of 14 blockers replaced by the controls '
        'that name them; R6.PIPE.15 and R6.SPLIT.3 stay listed as partly covered |',
        '| R6.REC.18, R6.CTRL.23 | B3 | TR28 added to the Controls lists |',
        '| R6.GATE.3 | B5 | multi-key invariant objects: allowed when every key is in the vocabulary and their combined '
        'meaning is unambiguous; one condition |',
        '| R6.CTRL.3, OBL-20 | B2 | the 42 rows recorded as having a second direction by amendment 1 |',
        '| Table 17.1 | B1, B2 | 14 rows added after REP-BUILD; RT-L, RT-L2, RT-X, TT8 and TT13 direction `both`; '
        'S7-schema-and-checker names R6.OUT.22 |',
    ] + ['| %s | B4 | anchored design correction (b4-design-edits.json) |' % e['label'] for e in B4_EDITS] + [
        '| sec. 0.2, R6.CTRL.3, Table 17.1 | B4 | the B4 directions quoted and parts A, B and D stated; the six B4 rows '
        'counted and added to Table 17.1 after the B1 rows |'] * bool(B4_EDITS) + [
        '',
        '## 3. Not changed by amendment 1',
        '',
        '- No requirement is weakened, withdrawn or re-kinded; no row is retired; no exemption (`scope`, `exempt`) '
        'is added; no `status_allowed` admits a new status.',
        '- The identifier migration of sec. 34 and MIGRATION.json: applied in the tool revision (OBL-22), with the '
        'owner\'s approval quoted in sec. 0.2.',
        '- The `runner` fields: kept; refreshed from the tool revision\'s final lines when it lands (the gate does '
        'not read them, R6.GATE.9). New rows have `runner` null until implemented.',
        '- The invariant vocabulary (153 keys): unchanged; every new invariant uses a listed key.',
        '- B4: the records themselves (reconciliation record and side-change class records) are drafted and '
        'reviewed on a separate branch; only the design text is corrected here.',
        '- B4 parts A and D need the owner\'s specific approval before any tool revision implements them; their '
        'requirements carry this in `pending_owner_confirmation`. Part A qualifies the rule that the configuration '
        'at `F` references every record a run uses (R6.REC.4, R6.REC.5, R6.CFG.4, R6.OUT.5, R6.VALID.3) by the '
        'checked post-freeze route of R6.RECON.2; the alternative that adds no route is a new configuration version '
        'and a new freeze (R6.CFG.3) for every record written after `F`. Part B follows the owner\'s direction on '
        'record location and needs independent review. Part D strengthens R6.RECON.21.',
        '- Not adopted from the proposed B4 text: a reserved side-change class `admitted-record` classifying records '
        'and review records in a reconciliation directory on `M`. A class record that is not itself on that `M` (one '
        'frozen with the plan, or one the post-freeze route admits) already pins such files by blob without a hash '
        'cycle (R6.TREE.5), so the class would widen the tool without need (owner direction: "We should avoid '
        'further expansion of the verification tool when a simpler solution exists.").',
        '',
        '## 4. Outputs',
        '',
        '| File | sha256 |',
        '|---|---|',
    ]
    for n in ('DESIGN-r6.md', 'EXPECTATIONS.json', 'REQUIREMENTS.json'):
        lines.append('| %s | %s |' % (n, sha(outs[n])))
    lines += ['', 'Self-checks run by the generator: correspondence in both directions (every testable requirement '
              'names a control, every named control is a row that lists the requirement, every row is named); a '
              'second direction on every row in the both-directions scope; every invariant key in the 153-key '
              'vocabulary; no new id retired or already a row.', '']
    return '\n'.join(lines)


def manifest(m, outs, gen_sha, owner_sha):
    for n, label in (('DESIGN-r6.md', 'final r6 document (the design)'),
                     ('EXPECTATIONS.json', 'final r6 document (expectation file)'),
                     ('REQUIREMENTS.json', 'final r6 document (requirement index)')):
        mm = [x for x in re.finditer(r'^\| %s \| [^\n]*$' % re.escape(n), m, re.M)]
        if len(mm) != 1:
            raise SystemExit('manifest row %s' % n)
        new = '| %s | %s | amendment-1 output | %s |' % (n, label, sha(outs[n]))
        m = m[:mm[0].start()] + new + m[mm[0].end():]
    rows = ('| AMENDMENT-1.md | change record of amendment 1 | amendment-1 output | %s |\n'
            '| generator-amendment1/amend1.py | amendment-1 generator | amendment-1 generator | %s |\n'
            '| generator-amendment1/owner-decision-amendment1.json | amendment-1 generator input (the owner decision '
            'quoted) | amendment-1 generator | %s |\n' % (sha(outs['AMENDMENT-1.md']), gen_sha, owner_sha))
    if B4_EDITS:
        rows += ('| generator-amendment1/b4-design-edits.json | amendment-1 generator input (the B4 design corrections, '
                 'anchored edits) | amendment-1 generator | %s |\n' % B4_SHA)
    m = once(m, '| LANDING-MANIFEST.md | this manifest (A5) | round-6 output | (this file) |',
             rows + '| LANDING-MANIFEST.md | this manifest (A5) | amendment-1 output | (this file) |', 'manifest self row')
    para = ('\nAmendment 1 (owner decision of 2026-11-26T04:39:58Z, amaybaum, #1169 comment 7182798225, quoted in '
            'DESIGN-r6.md sec. 0.2): DESIGN-r6.md, EXPECTATIONS.json and REQUIREMENTS.json are amended, and '
            'AMENDMENT-1.md maps each change to its decision. Recipe: lay out `base/` with the four files DESIGN-r6.md, '
            'EXPECTATIONS.json, REQUIREMENTS.json and LANDING-MANIFEST.md of this directory at main '
            '02b8e20839d4700de721f8427b3fe9f3c746b71f, and run `python3 -I -B generator-amendment1/amend1.py base out`. '
            'It checks the four files against their sha256, exits 0 and writes into `out/` the files of sec. 1 marked '
            '"amendment-1 output" with the sha256 stated and this manifest; the earlier rows of sec. 1 and their '
            'recipes are unchanged.\n')
    m = once(m, '\n## 2. Files left to Git history', para + '\n## 2. Files left to Git history', 'manifest recipe')
    return m


if __name__ == '__main__':
    sys.exit(main())
