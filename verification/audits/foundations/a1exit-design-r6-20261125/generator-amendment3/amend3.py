"""Generator of amendment 3 to design r6: general multi-path reconciliation (owner decisions of
2026-11-26T06:34:32Z, #1169 comment 7184569981, and 2026-11-26T06:37:58Z, #1169 comment 7184626125, item 4).

Usage: python3 -I -B amend3.py BASE OUT

BASE holds DESIGN-r6.md, EXPECTATIONS.json, REQUIREMENTS.json and LANDING-MANIFEST.md as amendment 2 leaves them
(each checked against its sha256 below). The script reads owner-decisions-amendment3.json beside itself and writes
into OUT the amended DESIGN-r6.md, EXPECTATIONS.json and REQUIREMENTS.json, the change record AMENDMENT-3.md and the
updated LANDING-MANIFEST.md.

Every text edit is anchored on an exact string that must occur once. Self-checks: correspondence in both directions
for every row and requirement amendment 3 touches; a second direction on every new row; every invariant key in the
closed vocabulary of sec. 16.10; new ids unused in the base files; no existing expectation row changed; no existing
requirement loses a control. Standard library only; deterministic.
"""
import copy
import hashlib
import json
import os
import re
import sys

BASE_SHA256 = {
    'DESIGN-r6.md': 'ca367e744b85fc5d28d463c0eb568b4198e3a768b0ea64e54532385ff086c1c5',
    'EXPECTATIONS.json': 'eaec250ec932e563ad68a493cc846307c3b172ac0454028a231c08a5b259b2f9',
    'REQUIREMENTS.json': '77ba1d9c40ac67180939a696b3d4b9c5bf674083cc50d6f7b0744ff3d35d2243',
    'LANDING-MANIFEST.md': '79a46892ba8aa9649852e90914af599006209c9ab88c2933cbe19e9329cf9acd',
}
HERE = os.path.dirname(os.path.abspath(__file__))
SRC = 'r6 amendment 3 (owner decisions of 2026-11-26T06:34:32Z, #1169 comment 7184569981, and 2026-11-26T06:37:58Z, ' \
      '#1169 comment 7184626125)'
FLAG = 'added by amendment 3; no runner records it before the tool revision implements it'
PENDING = ('amendment 3 (multi-path reconciliation): drafted under the owner\'s authorization of 2026-11-26T06:34:32Z '
           '(#1169 comment 7184569981); needs independent review and the owner\'s acceptance before any tool revision '
           'implements it')
MARK = '(amendment 3, sec. 0.4: pending independent review and the owner\'s acceptance)'
NONE_DRIFT = {'not_class': ['base-drift', 'record-invalid']}


def sha(b):
    return hashlib.sha256(b).hexdigest()


def once(text, old, new, what):
    c = text.count(old)
    if c != 1:
        raise SystemExit('anchor for %s occurs %d times' % (what, c))
    return text.replace(old, new)


def dumpj(doc):
    return (json.dumps(doc, indent=1, ensure_ascii=False) + '\n').encode('utf-8')


def row(rid, req, kind, direction, expect, restored, case):
    r = {'id': rid, 'requirements': req, 'runner': None, 'operations': ['execution']}
    if direction != 'adversarial':
        r['direction'] = direction
    if kind != 'declarative':
        r['predicate_kind'] = kind
    r['expect'] = expect
    if restored is not None:
        r['restored'] = restored
    r['source'] = SRC
    r['flags'] = [FLAG]
    return r, case


def fail(case, conds=None, extra=None):
    c = {'case': case, 'outcome': 'FAIL', 'classes_include': ['base-drift'] + (extra or [])}
    if conds:
        c['invariants'] = [{'failed_conditions_include': x} for x in conds]
    return c


def rinv(case):
    return {'case': case, 'outcome': 'FAIL', 'classes_include': ['record-invalid']}


RECONCILED = {'outcome': 'ANY', 'invariants': [NONE_DRIFT]}

ROWS = [
    row('RECON-MULTI', ['R6.RECON.4', 'R6.RECON.5', 'R6.RECON.15', 'R6.RECON.16'], 'declarative', 'both', {'cases': [
        {'case': 'two ledgered paths in two files changed on M, each covered by its own reviewed reconciliation record '
                 'bound to the run, every condition RC1-RC14 holding for each (positive)',
         'outcome': 'ANY', 'invariants': [NONE_DRIFT]},
        {'case': 'the same two paths covered by one reviewed record with two path entries, each with its own '
                 'ledger_binding (positive)',
         'outcome': 'ANY', 'invariants': [NONE_DRIFT]},
        fail('countercase: the same run with the second record removed', ['RC10']),
        fail('countercase: the second record failing RC2 (its m differs from the path\'s blob at M)', ['RC2', 'RC10']),
        fail('countercase: an unledgered non-corpus path changed on M left unclassified', ['RC11'])]},
        None,
        'several drifted ledgered paths, each covered by an entry of a reconciliation record: RC10 and RC11 read over '
        'the run\'s locally valid entries; one uncovered drifted path fails RC10 for every entry'),
    row('RECON-ENUM', ['R6.RECON.22'], 'declarative', 'both', {'cases': [
        {'case': 'three ledgered paths changed on M, two covered by applying records and one by none',
         'outcome': 'FAIL', 'classes_include': ['base-drift'],
         'invariants': [{'items_include': [{'class': 'base-drift', 'subject': '$uncovered_path'}]},
                        {'equals': 'the result lists exactly one disposition for each path that differs between H and '
                                   'M and is ledgered or corpus: two reconciled, each naming its record, and one '
                                   'base-drift naming that no admitted record covers it; no other path has one'}]},
        {'case': 'countercase: the same result with one disposition removed',
         'outcome': 'PREDICATE', 'invariants': [{'schema_errors': ['missing disposition']}]},
        {'case': 'countercase: the same result with a disposition for a path that does not differ between H and M',
         'outcome': 'PREDICATE', 'invariants': [{'schema_errors': ['disposition for an unchanged path']}]}]},
        None,
        'every ledgered or corpus path that differs between H and M has exactly one disposition (reconciled, naming '
        'its record, or base-drift, naming why); the result checker refuses a missing or extra one'),
    row('RECON-CORPUS', ['R6.RECON.3', 'R6.RECON.8', 'R6.RECON.22'], 'declarative', 'both', {'cases': [
        {'case': 'a corpus path the ledger does not list, changed on M, covered by a reviewed record entry with no '
                 'splices, l equal to m, x equal to the path\'s blob at H, and null ledger_binding values (positive)',
         'outcome': 'ANY', 'invariants': [NONE_DRIFT]},
        fail('countercase: the same entry with l differing from m', ['RC7']),
        fail('countercase: the same entry with a non-null ledger_binding value', ['RC13']),
        fail('countercase: the same path with no record')]},
        None,
        'an unledgered corpus path changed on M is reconciled by an entry without splices under the same conditions; '
        'without an applying entry it stays base-drift'),
    row('RECON-CONFLICT', ['R6.RECON.24', 'R6.RECON.4', 'R6.RECON.18'], 'declarative', 'adversarial', {'cases': [
        fail('M changes a byte of the line holding a splice, outside the splice\'s span', ['RC14']),
        fail('M changes a byte of a sentence (splitter version 2) that overlaps a splice\'s span, on another line',
             ['RC14']),
        fail('M changes the line of a retained site of the path', ['RC14']),
        fail('M adds a second copy of a splice\'s context window elsewhere in the file', ['RC14']),
        fail('a protected range of the record overlaps a translated splice\'s context window at M', ['RC14']),
        fail('M changes the bytes of a splice\'s span and the old bytes occur once elsewhere at M', ['RC14'])]},
        {'outcome': 'ANY', 'invariants': [NONE_DRIFT,
                                          {'baseline': 'the same path with M\'s changes outside every context window '
                                                       'and retained-site line'}]},
        'RC14: a change on M that touches a splice\'s context window (its lines, and for a corpus path its '
        'sentences), a retained site\'s line, or that a protected range claims inside a window, fails the record; the '
        'conflict is reported, never resolved by translation'),
    row('RECON-TRIAL', ['R6.RECON.23', 'R6.RECON.21'], 'declarative', 'both', {'cases': [
        {'case': 'two drifted ledgered corpus paths with applying records; M\'s changes add text no profile matches '
                 '(positive)',
         'outcome': 'ANY', 'invariants': [NONE_DRIFT]},
        fail('countercase: M\'s change adds, outside every context window, a sentence a deny profile matches',
             ['reconciled-state']),
        fail('countercase: M\'s change adds an unclassified hit of a review profile with applies_to tree',
             ['reconciled-state']),
        fail('countercase: M changes one file of a mirror pair and not the other', ['reconciled-state']),
        fail('countercase: M removes a literal that a pin of the configuration requires at X', ['reconciled-state']),
        {'case': 'countercase: RT-L2 with every drifted path covered by an applying record and the reconciled-state '
                 'trial failing',
         'outcome': 'FAIL', 'invariants': [{'drift_state_in': ['unresolved']}]}]},
        None,
        'the reconciled-state trial: deny and tree review profiles (op D) and op C\'s postconditions at the landing '
        '(or in-memory landing) find nothing the same checks at the candidate do not find; a new finding keeps its '
        'path base-drift and RT-L2 unresolved'),
    row('RECON-SCI', ['R6.RECON.25', 'R6.RECON.1'], 'declarative', 'adversarial', {'cases': [
        rinv('a path entry without scientific_effect'),
        rinv('a scientific_effect whose conclusions name an edit id that is not a splice of the path'),
        rinv('a scientific_effect with an empty assessment or method'),
        rinv('a review record whose verdicts do not cover the entry\'s scientific_effect item, or do not accept it'),
        rinv('a review record whose reviewer equals the record\'s author')]},
        {'outcome': 'ANY', 'invariants': [{'record_admitted': '$record'}, {'not_class': ['record-invalid']}]},
        'scientific verification is the reviewer\'s: the tool checks only that each entry carries a '
        'scientific_effect of the stated form and that a non-author review accepts it; it cannot check the '
        'assessment\'s truth'),
]
NEW_IDS = [r['id'] for r, _ in ROWS]
REQ_CONTROLS = {}
for _r, _ in ROWS:
    for _q in _r['requirements']:
        REQ_CONTROLS.setdefault(_q, []).append(_r['id'])
NEW_REQS = ['R6.RECON.22', 'R6.RECON.23', 'R6.RECON.24', 'R6.RECON.25']
TOUCHED = ['R6.RECON.1', 'R6.RECON.3', 'R6.RECON.4', 'R6.RECON.5', 'R6.RECON.8', 'R6.RECON.15', 'R6.RECON.16',
           'R6.RECON.18', 'R6.RECON.21']

RESPONSIBILITIES = [
    ('Mechanical verification', 'R6.RECON.22, R6.RECON.15 (RC10), R6.RECON.16 (RC11), R6.RECON.5 (RC13), R6.RECON.3 '
     'and R6.RECON.8 (unledgered corpus paths), R6.RECON.4', 'RECON-ENUM, RECON-MULTI, RECON-CORPUS', 'the tool'),
    ('Scientific verification', 'R6.RECON.25, R6.RECON.1 (`scientific_effect`)', 'RECON-SCI',
     'the independent reviewer; the tool binds the review and checks its form only'),
    ('Conflict detection', 'R6.RECON.24 (RC14), R6.RECON.4, R6.RECON.18', 'RECON-CONFLICT', 'the tool'),
    ('Trial verification', 'R6.RECON.23, R6.RECON.21', 'RECON-TRIAL', 'the tool, on the reconciled state'),
]

NEW_REQ_TEXT = '''
**R6.RECON.22** **Mechanical verification: drift assessment** %(mark)s. The complete
ledger-path check is mandatory: every op C run with `M` gives every path that differs between `H` and `M` and is
ledgered or corpus exactly one disposition in its result: `reconciled`, naming the record and entry that apply, or an
item `base-drift` (FAIL), naming each failed condition or that no admitted record covers the path. No such path is
omitted, none has two, and a path that does not differ has none; the result's JSON Schema refuses a result that breaks
this. Drift is reported and assessed (R6.RECON.23 to R6.RECON.25); the tool changes no file and reverts nothing.
Sources: %(src)s. Controls: RECON-ENUM, RECON-CORPUS.

**R6.RECON.23** **Trial verification: the reconciled-state trial** %(mark)s. When a ledgered or
corpus path differs between `H` and `M`, the run evaluates, besides `X` (or `C`), the landing `L`, or for a
prediction the in-memory landing of R6.TREE.15 built from the run's `M` and `C`: (a) op D on it, with the A1
configuration's deny profiles and its review profiles whose `applies_to` is `tree`, over the corpus; (b) the
postconditions op C evaluates at `X` (R6.TREE.9), the pin postconditions and mirror identity among them, for the
ledgered paths. A finding at the landing that the same evaluation at `X` (or `C`) does not have, matched by its
fingerprint, is a FAIL `base-drift` of the path it lies in, naming the condition `reconciled-state`, unless records
and rules resolve it there under their own rules (sec. 14, R6.HIT.1), exactly as they would at `X`. A drifted path is
reconciled only if this holds, and RT-L2's validly reconciled state requires it (R6.RECON.21). The trial is recorded as
its own run on the exact `M`; when `M` changes (R6.RECON.20), it is run again. No expectation of an existing control
changes. Op B is not repeated at the landing: its segments are `E..H` and `H..X`, and drift lies in `H..M`.
Sources: %(src)s. Controls: RECON-TRIAL.

**R6.RECON.24** **Conflict detection: RC14** %(mark)s. For each entry of a reconciliation record:
(a) each splice's context window at `H` (the bytes from the start of the first line that overlaps the splice's span
to the end of the last such line, widened, for a corpus path, to the sentences of splitter version 2 that overlap the
span) occurs exactly once at `M`, at the splice's translated offset less its distance from the window's start, with
the same bytes; (b) the line of each retained site of the path (the ledger interface's `retained`, resolved at `H`
through the site map) occurs exactly once at `M`, with the same bytes; (c) no protected range of the entry overlaps a
translated splice's context window at `M`. Otherwise RC14 fails: the record does not apply, the path stays
`base-drift`, and the result names RC14 and the splice or site. A change on `M` that touches a planned retirement
edit's context is reported as a conflict and never resolved by translation; a translation that relocates a splice
whose span `M` changed fails here.
Sources: %(src)s. Controls: RECON-CONFLICT.

**R6.RECON.25** **Scientific verification: the reviewed scientific effect** %(mark)s. Whether a
change on `M` affects the scientific justification for the retirement is established by the independent review, not
by the tool. Each path entry of a reconciliation record carries `scientific_effect`: `conclusions`, the ledger edit
ids of the path whose justification the change could bear on (or `none`); `assessment`, the writer's statement of the
effect; and `method`, what was re-derived or re-run to establish it. The review record covers `scientific_effect` as
an item of the entry, and the reviewer re-derives it under R6.REC.2. The tool checks only the form: the field and its
three parts are present and non-empty; each named edit id is a splice id of the path; the review's verdicts cover the
item and accept it; record lint holds (R6.REC.6). It does not and cannot check that the assessment is true or that the
conclusions listed are complete; those rest on the review. A failure of form is FAIL `record-invalid`.
Sources: %(src)s. Controls: RECON-SCI.
'''


def note(owner):
    out = ['', '### 0.4 Amendment 3 of 2026-11-26', '']
    for d in owner['decisions']:
        out += ['The owner decided at %s (%s, %s, relayed by the %s). Excerpt, in the order of the source (table cells '
                'joined by " | ", table padding removed; headings left out; each line prefixed by "> "; "[...]" marks '
                'text left out):' % (d['record'], d['author'], d['time'], d['relayed_by']), '']
        out.append('\n>\n'.join('> ' + (x if x is not None else '[...]') for x in d['quotes']))
        out.append('')
    out += [
        'Amendment 3 generalizes reconciliation from one drifted path to any set of drifted ledgered and corpus paths, '
        'with no exemption and no file-specific rule; AMENDMENT-3.md gives the analysis of the single-path '
        'assumptions it removes. Its requirements are pending independent review and the owner\'s acceptance. The four '
        'responsibilities are kept apart:',
        '',
        '| Responsibility | Requirements | Controls | Established by |',
        '|---|---|---|---|',
    ] + ['| %s | %s | %s | %s |' % r for r in RESPONSIBILITIES] + [
        '',
        'What the tool can check mechanically: every changed ledgered or corpus path and its disposition; each record '
        'entry\'s binding and RC1-RC14 from git objects; the absence, at the landing, of any profile finding or '
        'postcondition failure that the candidate does not have; the form of the scientific review. What it cannot '
        'check: whether a change bears on the scientific justification beyond what the profiles and postconditions '
        'detect (for example a change to a verification script\'s logic, or a change in a sentence\'s meaning that no '
        'profile matches); that rests on the independent review of R6.RECON.25.',
        '',
        'Preserved, stated before the change as its controls (AGENTS.md sec. A.29): the meaning of RC1-RC9, RC12 and '
        'RC13 for each path; the composition and translation rules (R6.TREE.12, R6.TREE.13); `base-drift` for every '
        'drifted path that no applying record covers (R6.TREE.7); identical items on `X` with and without the records '
        '(R6.RECON.3); the composition\'s authority over a record\'s `l` (R6.RECON.19); the post-freeze route and its '
        'one record per path (R6.RECON.2); RT-L2\'s three values; and every existing control row and expectation, none '
        'of which changes. With one drifted ledgered path and no other side change, RC10 and RC11 as amended give the '
        'verdicts they gave before.',
        '',
    ]
    return '\n'.join(out)


def amend_design(t, owner):
    t = once(t, "The record names the commits `M` and `X` and the paths it covers, its\n"
                "`ledger_binding` (`ledger_base`, and the canonical sha256 of the path's `files` entry, of its splice\n"
                "list and of its edit-list entries), `changes_decisions_on_X`, and for each path: `side_change_commits`,",
             "The record names the commits `M` and `X` and the paths it covers, its\n"
             "`ledger_base`, `changes_decisions_on_X`, and for each path: its `ledger_binding` (the canonical sha256 of\n"
             "the path's `files` entry, of its splice list and of its edit-list entries, each null for a corpus path the\n"
             "ledger does not list), its `scientific_effect` (R6.RECON.25), `side_change_commits`,", 'R6.RECON.1 fields')
    t = once(t, "and `sha256`. Its review record names the reviewer, under the ownership chain of sec. 11.\n"
                "Sources: V2-146. Controls: N3, N4, POSTF-5.",
             "and `sha256`. Its review record names the reviewer, under the ownership chain of sec. 11. The per-path\n"
             "`ledger_binding` and `scientific_effect` come from amendment 3 (sec. 0.4) and are pending independent\n"
             "review and the owner's acceptance.\n"
             "Sources: V2-146. Controls: N3, N4, POSTF-5, RECON-SCI.",
             'R6.RECON.1 controls')
    t = once(t, "reconciliation records and requiring identical items on `X`; any difference is FAIL `record-invalid`.\n"
                "Sources: E-1342, V2-147, RV-027. Controls: N2, N3, N3-config-route.",
             "reconciliation records and requiring identical items on `X`; any difference is FAIL `record-invalid`.\n"
             "A record may also name a corpus path that `M` changes and the ledger does not list (the only-`M`-changed\n"
             "case of R6.TREE.12, `base-drift` under R6.TREE.7); its entry has no splices, its `l` is `m` and its `x` is\n"
             "the path's blob at `H`, and the same conditions apply %s.\n"
             "Sources: E-1342, V2-147, RV-027. Controls: N2, N3, N3-config-route, RECON-CORPUS." % MARK,
             'R6.RECON.3')
    t = once(t, "**R6.RECON.4** A reconciliation record applies only if every one of its conditions RC1-RC13 holds at\n"
                "the run's `M` and `L`. The tool evaluates each condition itself, from git objects, and never takes the\n"
                "record's statement that it holds.\nSources: E-1343. Controls: N4, N5.",
             "**R6.RECON.4** A reconciliation record applies only if every one of its conditions RC1-RC14 holds at\n"
             "the run's `M` and `L`, for each of its path entries. The tool evaluates each condition itself, from git\n"
             "objects, and never takes the record's statement that it holds. An entry is locally valid when RC1-RC9\n"
             "and RC12-RC14 hold for it; RC10 and RC11 are read over the run's locally valid entries %s.\n"
             "Sources: E-1343. Controls: N4, N5, RECON-MULTI, RECON-CONFLICT." % MARK, 'R6.RECON.4')
    t = once(t, "`roles.scientific_base` and to the record's `ledger_base`, and the canonical sha256 (sorted keys, no\n"
                "whitespace, UTF-8) of the path's `files` entry, of its splice list and of its edit-list entries equal\n"
                "the record's `ledger_binding` values.\nSources: E-1344. Controls: N4.",
             "`roles.scientific_base` and to the record's `ledger_base`, and the canonical sha256 (sorted keys, no\n"
             "whitespace, UTF-8) of the path's `files` entry, of its splice list and of its edit-list entries equal\n"
             "the values of the entry's own `ledger_binding`; for a corpus path the ledger does not list, the three\n"
             "values are null and the ledger has no `files` entry, splice or edit entry for the path %s.\n"
             "Sources: E-1344. Controls: N4, RECON-MULTI." % MARK, 'R6.RECON.5')
    t = once(t, "**R6.RECON.8** RC3 (uniqueness at `H`): the path has at least one splice, and each splice's old bytes\n"
                "occur exactly once at `H`, at the splice's start, hash to its `old_sha256`, and match the record's\n"
                "`start_H` and `end_H`.\nSources: E-1347. Controls: N12.",
             "**R6.RECON.8** RC3 (uniqueness at `H`): the path has at least one splice, and each splice's old bytes\n"
             "occur exactly once at `H`, at the splice's start, hash to its `old_sha256`, and match the record's\n"
             "`start_H` and `end_H`. For the entry of a corpus path the ledger does not list (R6.RECON.3), RC3 to\n"
             "RC6 hold exactly when the ledger has no splice for the path and the entry lists none %s.\n"
             "Sources: E-1347. Controls: N12, RECON-CORPUS." % MARK, 'R6.RECON.8')
    t = once(t, "**R6.RECON.15** RC10 (other ledgered files): for every ledgered file other than the record's path, the\n"
                "blob at `M` equals the blob at `H`, and its sha256 at `M` equals its `base_sha256`. A difference from\n"
                "the tool's evaluation of RC10 is a verification defect.\nSources: E-1350. Controls: N16, N16-file.",
             "**R6.RECON.15** RC10 (other ledgered files): for every ledgered file other than the entry's path, either\n"
             "the blob at `M` equals the blob at `H` and its sha256 at `M` equals its `base_sha256`, or the file is\n"
             "covered by a locally valid entry of a reconciliation record of the run (R6.RECON.4). If a ledgered file\n"
             "that differs between `H` and `M` is covered by no locally valid entry, RC10 fails for every entry of the\n"
             "run, naming that file %s. A difference from the tool's evaluation of RC10 is a verification defect.\n"
             "Sources: E-1350. Controls: N16, N16-file, RECON-MULTI." % MARK, 'R6.RECON.15')
    t = once(t, "**R6.RECON.16** RC11 (classified side changes): every path that differs between `H` and `M`, other than\n"
                "the record's path, is not a corpus path and is classified",
             "**R6.RECON.16** RC11 (classified side changes): every path that differs between `H` and `M`, other than\n"
             "the paths covered by the run's locally valid entries (R6.RECON.4) %s, is not a corpus path and is "
             "classified" % MARK, 'R6.RECON.16')
    t = once(t, "Sources: E-1350, A-055. Controls: N17, RDIR-8, RDIR-15, RDIR-18, RDIR-19, RDIR-20, MUT:o9:RDIR-m11.",
             "Sources: E-1350, A-055. Controls: N17, RDIR-8, RDIR-15, RDIR-18, RDIR-19, RDIR-20, MUT:o9:RDIR-m11, "
             "RECON-MULTI.", 'R6.RECON.16 controls')
    t = once(t, "Sources: E-1352. Controls: N3, N4, N5, N6, N7, N8, N9, N12, N13, N14, N15, N16, N17, N18, TT8.",
             "Sources: E-1352. Controls: N3, N4, N5, N6, N7, N8, N9, N12, N13, N14, N15, N16, N17, N18, TT8, "
             "RECON-CONFLICT.", 'R6.RECON.18 controls')
    t = once(t, "  `C`; RT-L2 holds;\n",
             "  `C`; and the reconciled-state trial of R6.RECON.23 holds at the run's `M` %s; RT-L2 holds;\n" % MARK,
             'R6.RECON.21 validly reconciled')
    t = once(t, "Sources: E-1355, OC-3. Controls: RT-L2, RT-O9-L2, GATE-13, GATE-14, GATE-15, GATE-19, RTL2-BIND.",
             "Sources: E-1355, OC-3. Controls: RT-L2, RT-O9-L2, GATE-13, GATE-14, GATE-15, GATE-19, RTL2-BIND, "
             "RECON-TRIAL.", 'R6.RECON.21 controls')
    t = once(t, "\n***\n\n## 24. Engine, purity scope (Z9), generality",
             NEW_REQ_TEXT % {'mark': MARK, 'src': 'amendment 3 (#1169 comments 7184569981 and 7184626125)'}
             + "\n***\n\n## 24. Engine, purity scope (Z9), generality", 'new requirements')
    # R6.CTRL.3: the six rows and the recount
    t = once(t, "direction on each of those 42 rows and adds 14 rows (B1) and 6 rows (B4), each with one. Counted",
             "direction on each of those 42 rows and adds 14 rows (B1) and 6 rows (B4), each with one, and amendment 3\n"
             "adds %d rows (sec. 0.4), each with one. Counted" % len(ROWS), 'R6.CTRL.3 rows')
    m = re.search(r"\(\d+ rows, \d+ of them recording `scope: \"outside\"`; \d+ carry a `restored` expectation, \d+ "
                  r"declare direction `both`, \d+ name `paired_with`, \d+ are exempt as observations\)", t)
    if not m or t.count(m.group(0)) != 1:
        raise SystemExit('R6.CTRL.3 counts')
    t = t.replace(m.group(0), '(%s)' % COUNTS)
    # Table 17.1
    anchor = [x for x in re.finditer(r'^\| RTL2-BIND \| [^\n]*$', t, re.M)]
    if len(anchor) != 1:
        raise SystemExit('RTL2-BIND table row')
    ins = '\n'.join(table_row(r, c) for r, c in ROWS)
    t = t[:anchor[0].end()] + '\n' + ins + t[anchor[0].end():]
    # sec. 0.4
    a = t.index('### 0.3 Amendment 2 of 2026-11-26')
    b = t.index('\n***\n\n## 1. Notation and symbols', a)
    t = t[:b] + '\n' + note(owner) + t[b:]
    return t


def table_row(r, case):
    kind = 'proc' if r.get('predicate_kind') == 'procedural' else 'decl'
    d = r.get('direction', 'adversarial')
    dirs = {'adversarial': 'adv', 'positive': 'pos', 'both': 'both'}[d]
    return '| %s | %s | to be implemented (tool revision) | %s | %s | %s (amendment 3) |' % (
        r['id'], ', '.join(r['requirements']), kind, dirs, case)


COUNTS = ''


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


def amend_expectations(E):
    E = copy.deepcopy(E)
    ids = {r['id'] for r in E['rows']}
    for r, _ in ROWS:
        if r['id'] in ids:
            raise SystemExit('id %s already a row' % r['id'])
        E['rows'].append(r)
    return E


def amend_requirements(R):
    R = copy.deepcopy(R)
    by = {q['id']: q for q in R}
    for q in NEW_REQS:
        if q in by:
            raise SystemExit('requirement %s exists' % q)
    for rid, ctl in sorted(REQ_CONTROLS.items()):
        if rid in NEW_REQS:
            continue
        q = by[rid]
        if q['kind'] != 'testable' or set(ctl) & set(q['controls']):
            raise SystemExit('%s: controls' % rid)
        q['controls'] = q['controls'] + ctl
    for rid in TOUCHED:
        by[rid]['pending_owner_confirmation'] = by[rid]['pending_owner_confirmation'] + [PENDING]
    i = [k for k, q in enumerate(R) if q['id'] == 'R6.RECON.21'][0]
    new = [{'id': q, 'section': 'RECON', 'section_number': 23, 'kind': 'testable',
            'sources': ['#1169 comment 7184569981', '#1169 comment 7184626125'],
            'controls': list(REQ_CONTROLS[q]), 'verification': ['controls'], 'open': [],
            'pending_owner_confirmation': [PENDING], 'owner_decision': []} for q in NEW_REQS]
    return R[:i + 1] + new + R[i + 1:]


def vocabulary(t):
    a = t.index('### 16.10 Annex: invariant vocabulary')
    b = t.index('***', a)
    return set(re.findall(r'`([A-Za-z_0-9]+)`', t[t.index('\n\n', t.index('A key outside it', a)):b]))


def self_checks(E0, E, R0, R, t, base_texts):
    problems = []
    rows = {r['id']: r for r in E['rows']}
    reqs = {q['id']: q for q in R}
    for rid in NEW_IDS + NEW_REQS:
        for name, b in base_texts.items():
            if re.search(r'(?<![A-Za-z0-9.-])%s(?![A-Za-z0-9-])' % re.escape(rid), b):
                problems.append('%s already occurs in base %s' % (rid, name))
    if 'RC14' in ''.join(base_texts.values()):
        problems.append('RC14 already occurs in a base file')
    for r, _ in ROWS:
        for q in r['requirements']:
            if r['id'] not in reqs[q]['controls']:
                problems.append('%s lists %s, which does not name it' % (r['id'], q))
        d = r.get('direction', 'adversarial')
        if d != 'both' and r.get('restored') is None:
            problems.append('%s: no second direction' % r['id'])
    for q in NEW_REQS + list(REQ_CONTROLS):
        for c in reqs[q]['controls']:
            if c not in rows or q not in rows[c]['requirements']:
                problems.append('%s names %s, which does not list it' % (q, c))
        start = t.index('**%s**' % q)
        nxt = re.compile(r'\n(?:\*\*R6\.|\*\*\*|#)').search(t, start + 1)
        cl = t[start:nxt.start()].split('Controls:')[-1]
        for c in REQ_CONTROLS.get(q, []):
            if not re.search(r'(?<![A-Za-z0-9-])%s(?![A-Za-z0-9-])' % re.escape(c), cl):
                problems.append('%s: DESIGN Controls line does not name %s' % (q, c))
    vocab = vocabulary(t)
    if len(vocab) != 153:
        problems.append('vocabulary has %d keys' % len(vocab))

    def walk(rid, e):
        if not e:
            return
        for inv in e.get('invariants', []):
            for k in inv:
                if k not in vocab:
                    problems.append('%s: invariant key %s outside the vocabulary' % (rid, k))
        for c in e.get('cases', []):
            walk(rid, c)
    for r, _ in ROWS:
        walk(r['id'], r['expect'])
        walk(r['id'], r.get('restored'))
    r0 = {r['id']: r for r in E0['rows']}
    for rid, r in r0.items():
        if rows.get(rid) != r:
            problems.append('existing row %s changed' % rid)
    if {k: v for k, v in E0.items() if k != 'rows'} != {k: v for k, v in E.items() if k != 'rows'}:
        problems.append('EXPECTATIONS.json top-level fields changed')
    q0 = {q['id']: q for q in R0}
    for rid, q in q0.items():
        q1 = reqs[rid]
        if q1['controls'][:len(q['controls'])] != q['controls']:
            problems.append('requirement %s lost or reordered a control' % rid)
        for f in q:
            if f not in ('controls', 'pending_owner_confirmation') and q[f] != q1[f]:
                problems.append('requirement %s field %s changed' % (rid, f))
    for rid in [x for x in TOUCHED if x != 'R6.RECON.18'] + NEW_REQS:  # R6.RECON.18 gains only a control
        start = t.index('**%s**' % rid)
        nxt = re.compile(r'\n(?:\*\*R6\.|\*\*\*|#)').search(t, start + 1)
        if MARK not in t[start:nxt.start()] and 'come from amendment 3 (sec. 0.4)' not in t[start:nxt.start()]:
            problems.append('%s does not carry the amendment-3 mark' % rid)
    return problems


ANALYSIS = r'''## 1. Single-path analysis

Read against the design as amended by amendments 1 and 2. What already handles several drifted paths:

- The landing composition (R6.TREE.12, R6.TREE.13) is per path and applies to every path of the landing; several
  splices in one file compose by their `M`-translated offsets, which must be unique and must not overlap.
- `base-drift` (R6.TREE.7) is decided per path; the own-diff rule (R6.TREE.14) exempts "reconciled paths", plural.
- RC1 to RC9, RC12 and RC13 are stated per path (RC9 per file, after the file's last translated splice), and a record
  lists `paths`, each with its own blobs, splices and protected ranges.
- The post-freeze route admits one record per path (R6.RECON.2 (e)), which allows many paths, all read from one
  record commit `REV`.
- RT-L2's validly reconciled state requires every drifted path to be covered (R6.RECON.21); the gate's `rtl2`
  predicate loops over the drifted paths (GATE-15 has two).
- `X` and `X_rep` have the single parent `H` and do not read `M` (R6.TREE.9, R6.EVID.8), so the candidate side carries
  no assumption about how many paths drifted.

The single-path assumptions, each removed by amendment 3:

1. RC10 (R6.RECON.15) requires every ledgered file other than the record's path to equal `H` at `M`. With two drifted
   ledgered paths every record fails RC10, whatever records exist (the tool at adb8fc43 evaluates it so, in
   engine/reconcile.py). At `main` b6c6b80b, AGENTS.md and verification/lean/edge_rigidity_probe.py both differ from
   `H`, so the B4 AGENTS.md record cannot apply. Amendment 3 reads RC10 over the run's locally valid entries.
2. RC11 (R6.RECON.16) excludes only the record's path and requires every other changed path to be non-corpus and
   classified; a second drifted ledgered or corpus path fails it for the same reason. Amendment 3 excludes every path
   covered by a locally valid entry.
3. `ledger_binding` is a record-level field defined by "the path's" entry (R6.RECON.1, R6.RECON.5); for a record with
   two paths it is ambiguous (the B4 record carries it at the top level). Amendment 3 makes it per path entry.
4. R6.RECON.3 and RC3 confine records to ledgered paths that both `M` and the retirement change. A corpus path the
   ledger does not list, changed on `M`, is `base-drift` with no route at all, so every later correction to an
   unledgered manuscript file blocks the landing. Amendment 3 lets an entry without splices cover such a path, under
   the same conditions (RC3 to RC6 read for a path without splices).
5. Conflict detection is implicit. Translation (R6.TREE.13) moves a splice to the unique occurrence of its old bytes
   at `M`; RC5's identity case compares bytes only up to the splice's end, and RC9 protects only bytes after the last
   splice that the writer lists. A change on `M` to the rest of a splice's line or sentence, or to a retained site, is
   not detected, and a changed span whose old bytes occur once elsewhere is silently relocated. Amendment 3 adds RC14.
6. Nothing checks the reconciled state against the retirement's scans: `M`'s changes reach `L` unscanned (a corpus
   path changed on `M` is not checked as an unledgered segment, R6.TREE.7; op B on `L` was never implemented, sec. 33),
   and the trial controls read `H`-based trees only. Amendment 3 adds the reconciled-state trial.
7. Whether a change on `M` affects the scientific justification is nowhere stated as a reviewed judgement. Amendment 3
   adds `scientific_effect`, reviewed, whose form the tool checks.

Not a single-path assumption, left unchanged: RT-L2's expectation text says "the reconciliation record" and its
release-check key "a reconciliation record", but the predicate covers every drifted path.

The eleven paths now affected are the two drifted ledgered paths at `main` b6c6b80b and the nine ledgered manuscript
files that #1582 would restore; amendment 3 names none of them, and its rules apply to any path.
'''


def change_record(owner, outs, gen_sha, owner_sha):
    lines = ['# r6 amendment 3: change record', '',
             'Owner decisions: %s. Quoted as excerpts in DESIGN-r6.md sec. 0.4. Generated by '
             'generator-amendment3/amend3.py (sha256 %s) from the amendment-2 outputs and '
             'generator-amendment3/owner-decisions-amendment3.json (sha256 %s). Amendment 3 is a draft: it adopts '
             'nothing, needs independent review and the owner\'s acceptance, and authorizes no merge, dispatch, freeze '
             'or trial.' % ('; '.join('%s, %s (%s)' % (d['author'], d['time'], d['record'])
                                      for d in owner['decisions']), gen_sha, owner_sha), '']
    lines += ANALYSIS.split('\n')
    lines += ['## 2. Responsibilities', '', '| Responsibility | Requirements | Controls | Established by |',
              '|---|---|---|---|'] + ['| %s | %s | %s | %s |' % r for r in RESPONSIBILITIES] + ['']
    lines += ['## 3. Changes', '', '| File | Place | Change |', '|---|---|---|',
              '| DESIGN-r6.md | sec. 0.4 (new) | the owner decisions quoted; responsibilities, mechanical scope and '
              'preserved results stated |',
              '| DESIGN-r6.md | R6.RECON.1 | per-path `ledger_binding`; `scientific_effect` per path |',
              '| DESIGN-r6.md | R6.RECON.3, R6.RECON.8 (RC3) | an entry without splices for an unledgered corpus path '
              'changed on `M` |',
              '| DESIGN-r6.md | R6.RECON.4 | RC1-RC14 for each entry; locally valid entries |',
              '| DESIGN-r6.md | R6.RECON.5 (RC13) | binding per entry; null values for an unledgered corpus path |',
              '| DESIGN-r6.md | R6.RECON.15 (RC10), R6.RECON.16 (RC11) | read over the run\'s locally valid entries |',
              '| DESIGN-r6.md | R6.RECON.18 | RECON-CONFLICT named as RC14\'s control |',
              '| DESIGN-r6.md | R6.RECON.21 | validly reconciled also requires the reconciled-state trial |',
              '| DESIGN-r6.md | R6.RECON.22 to R6.RECON.25 (new) | mechanical verification, trial verification, '
              'conflict detection (RC14), scientific verification |',
              '| DESIGN-r6.md | R6.CTRL.3, Table 17.1 | %d rows counted and added after RTL2-BIND |' % len(ROWS),
              '| EXPECTATIONS.json | rows %s (new) | each records both directions; runner null |' % ', '.join(NEW_IDS),
              '| REQUIREMENTS.json | R6.RECON.22 to R6.RECON.25 (new); %s | controls appended; '
              '`pending_owner_confirmation` added |' % ', '.join(TOUCHED), '']
    lines += ['## 4. Preserved results (stated in advance; AGENTS.md sec. A.29)', '',
              '- The meaning of RC1 to RC9, RC12 and RC13 for each path, and their controls N3 to N18, TT8 and '
              'N3-config-route, unchanged.',
              '- The composition and translation rules R6.TREE.12 and R6.TREE.13 and their controls LC-1 to LC-7, RL, '
              'RT-L, TT7 and TT8, unchanged.',
              '- `base-drift` for every drifted path that no applying entry covers (R6.TREE.7): no path is exempt.',
              '- Identical items on `X` with and without the records (R6.RECON.3), and the composition\'s authority '
              'over `l` (R6.RECON.19).',
              '- The post-freeze route (R6.RECON.2, POSTF-1 to POSTF-5), RT-L2\'s three values (R6.GATE.16, GATE-13 to '
              'GATE-15, GATE-19, RTL2-BIND).',
              '- No existing expectation row changes, and no requirement loses a control (checked by the generator).',
              '- Hard-to-vary check: with one drifted ledgered path and no other side change, RC10 and RC11 as amended '
              'reduce to the old RC10 and RC11, so every existing control keeps its verdict. Beyond the case it was '
              'built for, the amendment predicts checkable outcomes: with AGENTS.md alone reconciled at `main` '
              'b6c6b80b, RC10 fails naming verification/lean/edge_rigidity_probe.py; and RC14 decides, from the bytes, '
              'whether any of #1582\'s restored corrections touches the context of a retirement splice. The second is '
              'to be checked when its records are drafted; amendment 3 does not assume its outcome.', '']
    lines += ['## 5. What the tool can and cannot check', '',
              '- Can, from git objects: every changed ledgered or corpus path and its one disposition; each entry\'s '
              'binding and RC1-RC14; RC10 and RC11 over the run\'s entries; profile findings and postconditions at the '
              'landing against the candidate; the form of `scientific_effect` and its review.',
              '- Cannot: whether a change bears on the scientific justification beyond the profiles and postconditions '
              '(a change to a verification script\'s logic, as in edge_rigidity_probe.py, or to a sentence\'s meaning '
              'that no profile matches); whether the listed conclusions are complete; whether the assessment is true. '
              'These rest on the independent review (R6.RECON.25), which must name what it re-ran, for example the '
              'probe at the composed blob.', '']
    lines += ['## 6. Tool changes implied (not made here)', '',
              '- engine/reconcile.py: RC10 and RC11 over locally valid entries; per-entry `ledger_binding` in RC13; '
              'entries without splices for unledgered corpus paths (RC3 to RC6, RC7, RC8); RC14 (context windows by '
              'lines and, for corpus paths, splitter-v2 sentences; retained sites through the site map; protected '
              'ranges); RC14 in `condition_order`.',
              '- The result and its JSON Schema: one disposition per drifted ledgered or corpus path (R6.RECON.22).',
              '- The reconciled-state trial: op D and op C\'s postconditions at the landing or in-memory landing, '
              'compared with the candidate by fingerprint (R6.RECON.23); RT-L2\'s runner includes it.',
              '- Record lint of `scientific_effect` (R6.RECON.25).',
              '- Runners for %s.' % ', '.join(NEW_IDS),
              '- The B4 records rebuilt in the amended schema (per-path binding, `scientific_effect`), with a record '
              'entry for each drifted path.', '']
    lines += ['## 7. Outputs', '', '| File | sha256 |', '|---|---|']
    for n in ('DESIGN-r6.md', 'EXPECTATIONS.json', 'REQUIREMENTS.json'):
        lines.append('| %s | %s |' % (n, sha(outs[n])))
    lines += ['', 'Self-checks: correspondence for every touched row and requirement, second directions, the '
              'invariant vocabulary, new ids unused, no existing row changed, no requirement losing a control.', '']
    return '\n'.join(lines)


def manifest(m, outs, gen_sha, owner_sha):
    for n, label in (('DESIGN-r6.md', 'final r6 document (the design)'),
                     ('EXPECTATIONS.json', 'final r6 document (expectation file)'),
                     ('REQUIREMENTS.json', 'final r6 document (requirement index)')):
        mm = [x for x in re.finditer(r'^\| %s \| [^\n]*$' % re.escape(n), m, re.M)]
        if len(mm) != 1:
            raise SystemExit('manifest row %s' % n)
        m = m[:mm[0].start()] + '| %s | %s | amendment-3 output | %s |' % (n, label, sha(outs[n])) + m[mm[0].end():]
    rows = ('| AMENDMENT-3.md | change record of amendment 3 | amendment-3 output | %s |\n'
            '| generator-amendment3/amend3.py | amendment-3 generator | amendment-3 generator | %s |\n'
            '| generator-amendment3/owner-decisions-amendment3.json | amendment-3 generator input (the owner decisions '
            'quoted) | amendment-3 generator | %s |\n' % (sha(outs['AMENDMENT-3.md']), gen_sha, owner_sha))
    m = once(m, '| LANDING-MANIFEST.md | this manifest (A5) | amendment-2 output | (this file) |',
             rows + '| LANDING-MANIFEST.md | this manifest (A5) | amendment-3 output | (this file) |', 'manifest self')
    para = ('\nAmendment 3 (owner decisions of 2026-11-26T06:34:32Z and 2026-11-26T06:37:58Z, amaybaum, #1169 comments '
            '7184569981 and 7184626125, quoted in DESIGN-r6.md sec. 0.4): DESIGN-r6.md, EXPECTATIONS.json and '
            'REQUIREMENTS.json are amended, and AMENDMENT-3.md records the analysis and the changes. Recipe: run the '
            'amendment-2 recipe into `out2/`, copy REQUIREMENTS.json of `out1/` into `out2/`, and run `python3 -I -B '
            'generator-amendment3/amend3.py out2 out3`. It checks the four files against their sha256, exits 0 and '
            'writes into `out3/` the files of sec. 1 marked "amendment-3 output" with the sha256 stated and this '
            'manifest.\n')
    m = once(m, '\n## 2. Files left to Git history', para + '\n## 2. Files left to Git history', 'manifest recipe')
    return m


def main():
    global COUNTS
    if len(sys.argv) != 3:
        sys.stderr.write('usage: amend3.py BASE OUT\n')
        return 64
    base, out = sys.argv[1], sys.argv[2]
    data = {}
    for n, h in BASE_SHA256.items():
        with open(os.path.join(base, n), 'rb') as f:
            data[n] = f.read()
        if sha(data[n]) != h:
            sys.stderr.write('%s: sha256 %s, expected %s\n' % (n, sha(data[n]), h))
            return 65
    with open(os.path.join(HERE, 'owner-decisions-amendment3.json'), 'rb') as f:
        owner_b = f.read()
    owner = json.loads(owner_b)
    E0 = json.loads(data['EXPECTATIONS.json'])
    R0 = json.loads(data['REQUIREMENTS.json'])
    E = amend_expectations(E0)
    R = amend_requirements(R0)
    COUNTS = counts_text(E)
    t = amend_design(data['DESIGN-r6.md'].decode('utf-8'), owner)
    problems = self_checks(E0, E, R0, R, t, {n: b.decode('utf-8') for n, b in data.items()})
    if problems:
        sys.stderr.write('self-check failures:\n' + '\n'.join(problems) + '\n')
        return 1
    outs = {'DESIGN-r6.md': t.encode('utf-8'), 'EXPECTATIONS.json': dumpj(E), 'REQUIREMENTS.json': dumpj(R)}
    with open(os.path.join(HERE, 'amend3.py'), 'rb') as f:
        gen_sha = sha(f.read())
    outs['AMENDMENT-3.md'] = change_record(owner, outs, gen_sha, sha(owner_b)).encode('utf-8')
    outs['LANDING-MANIFEST.md'] = manifest(data['LANDING-MANIFEST.md'].decode('utf-8'), outs, gen_sha,
                                           sha(owner_b)).encode('utf-8')
    os.makedirs(out, exist_ok=True)
    for n, b in sorted(outs.items()):
        with open(os.path.join(out, n), 'wb') as f:
            f.write(b)
        print('%s %s' % (sha(b), n))
    return 0


if __name__ == '__main__':
    sys.exit(main())
