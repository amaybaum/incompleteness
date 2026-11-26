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
        fail('countercase: the same entry with x differing from the path\'s blob at H', ['RC8']),
        fail('countercase: the same entry with a non-null ledger_binding value', ['RC13']),
        fail('countercase: the same path with no record')]},
        None,
        'an unledgered corpus path changed on M is reconciled by an entry without splices under the same conditions; '
        'without an applying entry it stays base-drift'),
    row('RECON-CONFLICT', ['R6.RECON.24', 'R6.RECON.4', 'R6.RECON.18', 'R6.CTRL.21'], 'declarative', 'adversarial', {'cases': [
        fail('M changes a byte of the line holding a splice, outside the splice\'s span', ['RC14']),
        fail('M changes a byte of a sentence (splitter version 2) that overlaps a splice\'s span, on another line',
             ['RC14']),
        fail('M changes the line of a retained site of the path', ['RC14']),
        fail('M adds a second copy of a splice\'s context window elsewhere in the file', ['RC14']),
        fail('M changes the bytes of a splice\'s span and the old bytes occur once elsewhere at M', ['RC14'])]},
        {'outcome': 'ANY', 'invariants': [NONE_DRIFT,
                                          {'baseline': 'the same path with M\'s changes outside every context window '
                                                       'and retained-site line'}]},
        'RC14: a change on M that touches a splice\'s context window (its lines, and for a corpus path its '
        'sentences) or a retained site\'s line fails the record; the conflict is reported, never resolved by '
        'translation'),
    row('RECON-TRIAL', ['R6.RECON.23', 'R6.RECON.21'], 'declarative', 'both', {'cases': [
        {'case': 'two drifted ledgered corpus paths with applying records; M\'s changes add text no profile matches '
                 '(positive)',
         'outcome': 'ANY', 'invariants': [NONE_DRIFT]},
        fail('countercase: M\'s change adds, outside every context window, a sentence a deny profile matches',
             ['reconciled-state']),
        fail('countercase: M\'s change adds an unclassified hit of a review profile with applies_to tree',
             ['reconciled-state']),
        fail('countercase: M changes one file of a mirror pair and not the other (a run-level item naming the drifted '
             'file)', ['reconciled-state']),
        fail('countercase: M adds a second occurrence of a deny match that X already has once (multiplicity)',
             ['reconciled-state']),
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
        rinv('a scientific_effect whose conclusions name an id that is no edit id of the ledger'),
        rinv('a scientific_effect with an empty assessment or method'),
        rinv('a review record whose verdicts do not cover the entry\'s scientific_effect item, or do not accept it'),
        rinv('a review record whose reviewer equals the record\'s author'),
        rinv('a scientific_effect without verdict, or with verdict invalidates and no invalidated edit id, or an '
             'invalidated sha256 that differs from the edit-list entry\'s'),
        rinv('an executed path\'s entry whose method names no check re-run at the composed blob')]},
        {'outcome': 'ANY', 'invariants': [{'record_admitted': '$record'}, {'not_class': ['record-invalid']},
                                          {'baseline': 'a valid entry of an unledgered corpus path whose conclusions '
                                                       'name an edit id of another path'}]},
        'scientific verification is the reviewer\'s: the tool checks only that each entry carries a '
        'scientific_effect of the stated form and that a non-author review accepts it; it cannot check the '
        'assessment\'s truth'),
    row('RECON-CATEGORY', ['R6.RECON.22', 'R6.RECON.24'], 'declarative', 'both', {'cases': [
        {'case': 'a drifted ledgered path whose changes on M lie outside every context window and retained-site line, '
                 'covered by an applying entry (positive: category 1, mechanical)',
         'outcome': 'ANY', 'invariants': [NONE_DRIFT, {'equals': 'the path\'s disposition is reconciled, category 1'}]},
        fail('countercase: the same path with a change on M inside a splice\'s context window and no resolution '
             '(category 2, unresolved)', ['RC14']),
        fail('countercase: the same path with a change on M to a splice\'s span, so that its old bytes do not occur '
             'at M (category 2, unresolved)', ['RC4', 'RC14'])]},
        None,
        'the category of a drifted path is computed: category 1 when every condition RC1-RC14 holds with no conflict; '
        'category 2 when RC14 finds a conflict or a splice\'s old bytes do not occur once at M; category 2 is never '
        'reconciled by translation'),
    row('RECON-OVERLAP', ['R6.RECON.24', 'R6.TREE.12'], 'declarative', 'both', {'cases': [
        {'case': 'a category-2 path whose entry carries a resolution for the conflicting splice: its window is the '
                 'conflicting context window at M, its resolved bytes contain the splice\'s approved new bytes '
                 'exactly once, l equals the composition outside the window, scientific_effect names the splice with '
                 'verdict no-effect, and the review accepts the resolution and the scientific_effect (positive)',
         'outcome': 'ANY',
         'invariants': [NONE_DRIFT, {'equals': 'the path\'s disposition is reconciled-resolved, category 2'}]},
        fail('countercase: the same entry without the resolution', ['RC14']),
        fail('countercase: resolved bytes that do not contain the splice\'s new bytes', ['RC14']),
        fail('countercase: l differing from the composition outside the resolution window', ['RC7']),
        fail('countercase: a resolution window other than the conflicting context window', ['RC14']),
        {'case': 'a category-2 path whose change on M rewrote a splice\'s span (its old bytes no longer occur at M), '
                 'resolved by a reviewed resolution whose window occurs once at M and whose resolved bytes carry the '
                 'new bytes once; RC4 to RC6 read on the window and RC9 outside it (positive)',
         'outcome': 'ANY',
         'invariants': [NONE_DRIFT, {'equals': 'the path\'s disposition is reconciled-resolved, category 2'}]},
        fail('countercase: a resolution window that occurs twice at M', ['RC14']),
        {'case': 'a splice whose H context window occurs twice at M (identical table rows), resolved through a '
                 'writer-chosen window that occurs exactly once at M, confirmed by the review item (positive)',
         'outcome': 'ANY',
         'invariants': [NONE_DRIFT, {'equals': 'the path\'s disposition is reconciled-resolved, category 2'}]},
        {'case': 'countercase: a changed-span resolution whose writer-chosen window the review does not confirm (no '
                 'review item that the window covers every changed byte and keeps or justifies each)',
         'outcome': 'FAIL', 'classes_include': ['record-invalid']},
        fail('countercase: a conflict on a retained site\'s line with a resolution offered for it (no resolution '
             'route)', ['RC14']),
        {'case': 'countercase: scientific_effect that does not name the overlapped splice',
         'outcome': 'FAIL', 'classes_include': ['record-invalid']},
        {'case': 'countercase: a review whose verdicts do not cover the resolution',
         'outcome': 'FAIL', 'classes_include': ['record-invalid']}]},
        None,
        'category 2 is resolved only explicitly: a reviewed resolution that keeps the planned edit\'s new bytes, with '
        'a renewed scientific review naming the splice; the landing then equals the resolved composition'),
    row('RECON-BLOCK', ['R6.RECON.26', 'R6.RECON.25', 'R6.CLASS.10'], 'declarative', 'both', {'cases': [
        {'case': 'a reviewed entry whose scientific_effect verdict is invalidates, naming an edit id of the path',
         'outcome': 'FAIL', 'classes_include': ['retirement-blocked']},
        {'case': 'a reviewed entry of an unledgered corpus path whose verdict invalidates an edit of a ledgered path',
         'outcome': 'FAIL', 'classes_include': ['retirement-blocked']},
        {'case': 'the same, with a later record superseding it whose verdict is no-effect',
         'outcome': 'FAIL', 'classes_include': ['retirement-blocked']},
        {'case': 'the same, with every other drifted path reconciled',
         'outcome': 'FAIL', 'classes_include': ['retirement-blocked']},
        {'case': 'the blocking record landed on main, and a later run naming a REV whose tree omits it in the '
                 'reconciliation directory it used, or a chain run without --classify',
         'outcome': 'FAIL', 'classes_include': ['retirement-blocked']},
        {'case': 'a writer\'s verdict no-effect with a non-author review whose verdict on the scientific_effect finds '
                 'invalidation, naming the invalidated edit id and its sha256',
         'outcome': 'FAIL', 'classes_include': ['retirement-blocked']},
        {'case': 'the same review finding, followed by a new record of the same path with verdict no-effect and an '
                 'accepting review',
         'outcome': 'FAIL', 'classes_include': ['retirement-blocked']},
        {'case': 'a later commit on M reverting the invalidating change, the plan unchanged',
         'outcome': 'FAIL', 'classes_include': ['retirement-blocked']},
        {'case': 'a revert of the path to exactly H\'s bytes with no other drifted path (a run-level item names the '
                 'path)',
         'outcome': 'FAIL', 'classes_include': ['retirement-blocked']},
        {'case': 'a reviewed repair of the change landed on M and recorded by its own reconciliation record entry, the '
                 'plan unchanged',
         'outcome': 'FAIL', 'classes_include': ['retirement-blocked']},
        {'case': 'a new configuration version with a new freeze whose ledger still carries the invalidated edit-list '
                 'entry unchanged',
         'outcome': 'FAIL', 'classes_include': ['retirement-blocked']},
        {'case': 'countercase: the same entry with verdict no-effect (positive)',
         'outcome': 'ANY', 'invariants': [{'not_class': ['retirement-blocked']}]},
        {'case': 'countercase: the run under a revised plan, a new configuration whose ledger changes the invalidated '
                 'edit\'s edit-list entry (positive)',
         'outcome': 'ANY', 'invariants': [{'not_class': ['retirement-blocked']}]},
        {'case': 'countercase: the run under a revised plan whose ledger no longer carries the invalidated edit, the '
                 'finding and the repair still on M (positive)',
         'outcome': 'ANY', 'invariants': [{'not_class': ['retirement-blocked']}]}]},
        None,
        'category 3: a reviewed finding that a change invalidates the basis of a planned edit blocks the retirement '
        '(FAIL retirement-blocked); an entry with that verdict never applies; no reconciliation record clears the '
        'block; only a revised plan that changes or removes the invalidated edit does'),
]
for _r, _ in ROWS:
    if _r['id'] in ('RECON-CATEGORY', 'RECON-OVERLAP', 'RECON-BLOCK'):
        _r['source'] = SRC + '; categories: #1169 comment 7184808247 (2026-11-26T06:48:37Z), item 3'
        if _r['id'] == 'RECON-BLOCK':
            _r['source'] += '; block lifecycle: #1169 comment 7185092393 (2026-11-26T07:05:39Z), item 4'
NEW_IDS = [r['id'] for r, _ in ROWS]
REQ_CONTROLS = {}
for _r, _ in ROWS:
    for _q in _r['requirements']:
        REQ_CONTROLS.setdefault(_q, []).append(_r['id'])
NEW_REQS = ['R6.RECON.22', 'R6.RECON.23', 'R6.RECON.24', 'R6.RECON.25', 'R6.RECON.26']
TOUCHED = ['R6.RECON.1', 'R6.RECON.3', 'R6.RECON.4', 'R6.RECON.5', 'R6.RECON.8', 'R6.RECON.15', 'R6.RECON.16',
           'R6.RECON.18', 'R6.RECON.21', 'R6.TREE.12', 'R6.CLASS.10', 'R6.CTRL.21', 'R6.RECON.2', 'R6.CORE.5']

RESPONSIBILITIES = [
    ('Mechanical verification', 'R6.RECON.22 (dispositions and categories), R6.RECON.15 (RC10), R6.RECON.16 (RC11), R6.RECON.5 (RC13), R6.RECON.3 '
     'and R6.RECON.8 (unledgered corpus paths), R6.RECON.4', 'RECON-ENUM, RECON-MULTI, RECON-CORPUS, '
     'RECON-CATEGORY', 'the tool'),
    ('Scientific verification', 'R6.RECON.25, R6.RECON.1 (`scientific_effect`), R6.RECON.26 (the blocking state)',
     'RECON-SCI, RECON-BLOCK',
     'the independent reviewer; the tool binds the review and checks its form only'),
    ('Conflict detection', 'R6.RECON.24 (RC14 and explicit resolution), R6.TREE.12, R6.RECON.4, R6.RECON.18',
     'RECON-CONFLICT, RECON-CATEGORY, RECON-OVERLAP', 'the tool; a resolution\'s wording by the reviewer'),
    ('Trial verification', 'R6.RECON.23, R6.RECON.21', 'RECON-TRIAL', 'the tool, on the reconciled state'),
]
CATEGORIES = [
    ('1, mechanical', 'every condition RC1-RC14 holds; no conflict', '`reconciled`',
     'the tool computes the category; the entry applies only with a reviewed `no-effect` verdict (R6.RECON.25)',
     'RECON-CATEGORY'),
    ('2, overlap', 'RC14 finds a conflict, or a splice\'s old bytes do not occur once at `M` (its span changed)',
     '`reconciled-resolved` with an applying reviewed resolution of each conflicting splice and a renewed scientific '
     'review; otherwise `base-drift`. A retained-site conflict has no resolution: `base-drift` until a revised plan '
     '(a new freeze)', 'the tool decides the category; the reviewer the resolution', 'RECON-CATEGORY, RECON-OVERLAP'),
    ('3, invalidating', 'a reviewed `scientific_effect` with verdict `invalidates`, for an edit of any path', '`retirement-blocked` (FAIL), '
     'which no reconciliation record clears; only a revised plan (a new freeze, AGENTS.md sec. A.50) does',
     'the review; the tool enforces the block', 'RECON-BLOCK'),
]

NEW_REQ_TEXT = '''
**R6.RECON.22** **Mechanical verification: drift assessment** %(mark)s. The complete
ledger-path check is mandatory: every op C run with `M` gives every path that differs between `H` and `M` and is
ledgered or corpus exactly one disposition in its result: `reconciled`, naming the record and entry that apply, or an
item `base-drift` (FAIL), naming each failed condition or that no admitted record covers the path. No such path is
omitted, none has two, and a path that does not differ has none; the result's JSON Schema refuses a result that breaks
this. A run-level `reconciled-state` item (R6.RECON.23) or `retirement-blocked` item (R6.RECON.26) is not a
disposition. Each disposition carries the path's
category: category 1 (mechanical), when every condition RC1-RC14 holds for an applying entry with no conflict,
disposition `reconciled`; category 2 (overlap), when RC14 finds a conflict or a splice's old bytes do not occur once at
`M`, disposition `reconciled-resolved` only under an explicit resolution (R6.RECON.24), otherwise `base-drift`;
category 3 (invalidating), when a reviewed `scientific_effect` finds that the change invalidates the basis of a planned
edit, disposition `retirement-blocked` (R6.RECON.26), which takes precedence over every other. Categories 1 and 2 are
computed from git objects; category 3 is read from the bound review. Drift is reported and assessed (R6.RECON.23 to
R6.RECON.26); the tool changes no file and reverts nothing.
Sources: %(src3)s. Controls: RECON-ENUM, RECON-CORPUS, RECON-CATEGORY.

**R6.RECON.23** **Trial verification: the reconciled-state trial** %(mark)s. When a ledgered or
corpus path differs between `H` and `M`, the run evaluates, besides `X` (or `C`), the landing `L`, or for a
prediction the in-memory landing of R6.TREE.15 built from the run's `M` and `C`: (a) op D on it, with the A1
configuration's deny profiles and its review profiles whose `applies_to` is `tree`, over the corpus; (b) the
postconditions op C evaluates at `X` (R6.TREE.9), the pin postconditions and mirror identity among them, for the
ledgered paths. Findings at the landing are matched with those of the same evaluation at `X` (or `C`) by fingerprint,
the tree field excluded, counting multiplicities: a fingerprint found k times at the landing and j times at `X` gives
k - j new findings when k > j. A new finding that records and rules do not resolve there under their own rules (sec.
14, R6.HIT.1), exactly as they would at `X`, is a FAIL `base-drift` naming the condition `reconciled-state`: it is the
disposition of the drifted path it lies in; a new finding in a path that does not differ (for example a mirror or pin
finding produced by a change to its counterpart) is a run-level item naming the drifted paths whose changes produced
it, and while it stands every drifted path of the run takes the disposition `base-drift` naming `reconciled-state`.
RT-L2's validly reconciled state requires that no such finding exists (R6.RECON.21). Records frozen at `F` are the only records that can resolve such a finding in a
chain-admitted run (R6.RECON.2 (a)), so a new finding at the landing after `F` that they do not resolve needs a new
configuration version and a new freeze (R6.CFG.3). The trial is recorded as its own run on the exact `M`; when `M`
changes (R6.RECON.20), it is run again. The tool's trial is a scan: it executes no check of the repository. Executable
checks bearing on a drifted path (Lean, verification scripts, generated artifacts) are re-run at the landing by the
delegation contract where a delegated class covers the path (sec. 13, R6.TREE.19), and otherwise by the independent
reviewer under R6.RECON.25. Op B is not repeated at the landing: outside resolution windows, RC14 (a) and (b) keep
every spliced or retained site's line intact at its translated position, so op B's site verdicts at `X` carry over
there; a site inside a resolution window rests on the review of the resolution (R6.RECON.24) and on op D at the
landing, which finds new hits. No expectation of an existing control changes.
Sources: %(src)s. Controls: RECON-TRIAL.

**R6.RECON.24** **Conflict detection: RC14** %(mark)s. For each entry of a reconciliation record:
(a) each splice's context window at `H` (the bytes from the start of the first line that overlaps the splice's span
to the end of the last such line, widened, for a corpus path, to the sentences of splitter version 2 that overlap the
span) occurs exactly once at `M`, at the splice's translated offset less its distance from the window's start, with
the same bytes; (b) the line of each retained site of the path (the ledger interface's `retained`, resolved at `H`
through the site map) occurs exactly once at `M`, with the same bytes. Otherwise RC14 fails: the record does not apply,
the path stays `base-drift`, and the result names RC14 and the splice or site. "Exactly once" is deliberately strict: a
window or line repeated verbatim at `M` (for example identical table rows) fails RC14 even when the change on `M` lies
elsewhere; a repeated splice window is resolved explicitly as below, and a retained-site conflict, a repeated
retained-site line included, waits for a revised plan. A change on `M` that touches a planned retirement edit's context is
reported as a conflict and never resolved by translation; a translation that relocates a splice whose span `M` changed
fails here. **Explicit resolution (category 2).** A conflict is resolved only by an entry's `resolutions`, one for each
conflicting splice: the window at `M` (`start_M`, `end_M`, `sha256`) and the resolved bytes' sha256. Where `H`'s
context window still occurs exactly once at `M`, the resolution window equals it. Otherwise (the span or its context
changed, or the window is repeated at `M`), the writer chooses a window that occurs exactly once at `M`, and the
reviewer verifies it: the review record confirms, as an item of
the resolution, that the window covers every byte `M` changed in the splice's context, and that every byte `M` changed
inside the window is kept in the resolved bytes or that dropping it is justified; the tool checks only that the window
occurs once at `M` and that the review covers and accepts that item. The resolution applies only if the window occurs exactly once at `M`, the
resolved bytes contain the splice's approved new bytes exactly once, the entry's `l` equals the resolved composition
(R6.TREE.12), the entry's `scientific_effect` names the splice in `conclusions` with verdict `no-effect` (the renewed
scientific review), and the review record covers each resolution and accepts it. A resolved splice is not translated:
for it RC4 to RC6 are read on the resolution window (the window occurs once at `M`, its bytes hash to the resolution's
`sha256`, and the resolved bytes carry the new bytes once), RC3 still holds at `H`, and RC9 is read outside the
resolution windows. This covers a splice whose span `M` changed. The tool checks these from git objects; the
resolution's wording within the window is the reviewer's judgement. With an applying resolution RC14 holds for the
splice, and the path is reconciled with category 2. A conflict on a retained site's line has no resolution: a retained
site is a decision of the plan with no new bytes to keep, so changing it is a change to the plan, and the path stays
`base-drift` until a revised plan (a new configuration version and a new freeze, R6.CFG.3).
Sources: %(src3)s. Controls: RECON-CONFLICT, RECON-CATEGORY, RECON-OVERLAP.

**R6.RECON.25** **Scientific verification: the reviewed scientific effect** %(mark)s. Whether a
change on `M` affects the scientific justification for the retirement is established by the independent review, not
by the tool. Each path entry of a reconciliation record carries `scientific_effect`: `conclusions`, the ledger edit ids,
of any path, whose justification the change could bear on (for example an executable change bearing on a manuscript
claim), or `none`; `assessment`, the writer's statement of the effect; `method`, what was re-derived or re-run to
establish it; and `verdict`, `no-effect` or `invalidates`, the latter with `invalidated`, each an edit id with the
canonical sha256 of its edit-list entry. For an entry whose path is executed by a check (a script, a Lean file, a
workflow), `method` names the check re-run at the entry's composed blob `l` and its result. The review record covers
`scientific_effect` as an item of the entry, and the reviewer re-derives it under R6.REC.2; "accept" means the
assessment and verdict are correct, whatever they conclude. An entry applies only if its reviewed verdict is
`no-effect`; an entry whose reviewed verdict is `invalidates` never applies and blocks under R6.RECON.26. The tool
checks only the form: the field and its parts are present and non-empty; each named edit id is an edit id of the
ledger, and each `invalidated` sha256 equals that edit-list entry's; the review's verdicts cover the item and accept it;
record lint holds (R6.REC.6). It does not and cannot check that the assessment is true, that the conclusions listed are
complete, or that the files of the corpus stay consistent with one another in meaning; those rest on the review. A
failure of form is FAIL `record-invalid`.
Sources: %(src)s. Controls: RECON-SCI, RECON-BLOCK.

**R6.RECON.26** **Category 3: the blocking state** %(mark)s. An invalidating finding blocks the
retirement. A finding is either a reconciliation record entry whose review accepts a `scientific_effect` with verdict
`invalidates`, or a non-author review record (passing record lint) whose verdict on an entry's `scientific_effect` finds
that the change invalidates the basis of a planned edit, whatever the writer's verdict; such a review verdict names
`invalidated`, each an edit id with the canonical sha256 of its edit-list entry. A record or review record carrying a
finding is landed on `main` at once, by its own commit outside any run (under the owner's merge approval, AGENTS.md
sec. A.50 item 1), before any further run of the retirement's landing; R6.RECON.20's re-resolution of `M` before the
landing brings it into every later run's `M`. Every run scans `M`'s tree, and the records the run reads and the scanned
sets of `F`'s tree and, for a post-freeze run, of `REV`'s tree, for findings, by the scan of R6.RECON.2 (d), whether or
not any path differs between `H` and `M`, chain runs without `--classify` included. A finding found there blocks every
run whose `M` contains one of the entry's `side_change_commits`, with an item FAIL `retirement-blocked` (obligation
`RET`): the entry's path takes the disposition `retirement-blocked` when it differs between `H` and `M`; when it does not
(for example after a revert to `H`'s bytes), the item is a run-level item naming the path. The block holds for as long as the configuration's ledger holds, for each
invalidated edit id, an edit-list entry with the same canonical sha256. A finding counts whether or not a later record
supersedes the entry and whatever `REV` a run names; no reconciliation record, resolution, supersession, or later
commit that reverts or repairs the change clears the block. The block is scoped to the frozen plan: it binds every
configuration whose ledger carries an invalidated edit-list entry unchanged, and nothing else. A repair on `main` never
lifts it; the finding and the repair stay on `main` as evidence, the repair recorded by a reconciliation record entry
of the repairing change, with its own reviewed `scientific_effect`. A revised plan, a new configuration version with a
new freeze (R6.CFG.3; AGENTS.md sec. A.50 item 5) whose ledger no longer carries an invalidated entry or carries a
revised one, is not blocked by the old finding; its renewed verification and trials run under this design as any
run's do, and the retirement becomes eligible for approval again only when they pass. A later repair can resolve the
underlying scientific problem, but cannot validate the invalidated frozen plan. The tool cannot find a category-3 change by itself: it relies on the review, and it enforces mechanically that a
recorded finding blocks.
Sources: %(src4)s. Controls: RECON-BLOCK.
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
        'Each drifted path falls in one of three categories (R6.RECON.22):',
        '',
        '| Category | When | Disposition | Determined by | Controls |',
        '|---|---|---|---|---|',
    ] + ['| %s | %s | %s | %s | %s |' % c for c in CATEGORIES] + [
        '',
        'What the tool can check mechanically: every changed ledgered or corpus path and its disposition; each record '
        'entry\'s binding and RC1-RC14 from git objects; the absence, at the landing, of any profile finding or '
        'postcondition failure that the candidate does not have; category 1 and category 2; that a recorded '
        'category-3 verdict blocks; the form of the scientific review and of a resolution. What it cannot '
        'check: whether a change bears on the scientific justification beyond what the profiles and postconditions '
        'detect (for example a change to a verification script\'s logic, or a change in a sentence\'s meaning that no '
        'profile matches), and so it cannot find a category-3 change or judge a category-2 resolution\'s wording; '
        'those rest on the independent review of R6.RECON.24 and R6.RECON.25. The obligation to land a category-3 '
        'finding on `main` at once is procedural: the tool enforces the block only from the commit that lands the '
        'finding (R6.RECON.26).',
        '',
        'Preserved, stated before the change as its controls (AGENTS.md sec. A.29): the meaning of RC1-RC9, RC12 and '
        'RC13 for each path; the composition and translation rules (R6.TREE.12, R6.TREE.13), extended only for a path '
        'with an applying category-2 resolution; `base-drift` for every '
        'drifted path that no applying record covers (R6.TREE.7); identical items on `X` with and without the records '
        '(R6.RECON.3); the composition\'s authority over a record\'s `l` (R6.RECON.19); the post-freeze route and its '
        'one record per path (R6.RECON.2); RT-L2\'s three values; and every existing control row and expectation, none '
        'of which changes. With one drifted ledgered path and no other side change, RC10 and RC11 as amended give the '
        'verdicts they gave before. Whether every existing positive control (TT8, POSTF-1 and the other positive '
        'reconciliation fixtures) also satisfies RC14 and the reconciled-state trial is a check for the tool revision; '
        'the independent review found no change of verdict for TT8 at 933b1efd or for the B4 AGENTS.md record (splice '
        'D296).',
        '',
        'Category-3 lifecycle (owner decision at #1169 comment 7185092393, item 4): the block is scoped to the frozen '
        'plan, keyed to its ledger\'s invalidated edit-list entries; a repair on `main` never lifts it, and the finding '
        'and the recorded repair stay on `main` as evidence; a revised plan, frozen anew, whose ledger no longer '
        'carries an invalidated entry or carries a revised one, is not blocked by the old finding, and its renewed '
        'verification and trials run normally (R6.RECON.26).',
        '',
        'Design note for the owner: a configuration frozen at `F` that references a reconciliation record closes that '
        'record\'s paths to the post-freeze route (R6.RECON.2 (d) and (e)), so a record that fails at a later `M` can be '
        'replaced only by a new freeze. The recommendation is that the configuration at `F` reference no reconciliation '
        'records. Cross-file semantic consistency (two files that stay byte-compatible but disagree in meaning) is left '
        'to the independent review (R6.RECON.25).',
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
             "review and the owner's acceptance; they change the record's shape incompatibly, so its schema is\n"
             "`oi-reconciliation/2`.\n"
             "Sources: V2-146. Controls: N3, N4, POSTF-5, RECON-SCI.",
             'R6.RECON.1 controls')
    t = once(t, "reconciliation records and requiring identical items on `X`; any difference is FAIL `record-invalid`.\n"
                "Sources: E-1342, V2-147, RV-027. Controls: N2, N3, N3-config-route.",
             "reconciliation records and requiring identical items on `X`; any difference is FAIL `record-invalid`.\n"
             "A record may also name a corpus path that `M` changes and the ledger does not list (the only-`M`-changed\n"
             "case of R6.TREE.12, `base-drift` under R6.TREE.7); its entry has no splices, and the same conditions\n"
             "apply, with RC8 reading: `x` is the path's blob at `H` and the ledger has no `files` entry for the path;\n"
             "and RC9 reading: over the whole file, `l` equals `m` %s.\n"
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
    t = once(t, "  - any other conflict, including a ledgered path whose `L[p]` differs from the composition, is FAIL\n"
                "    `landing-conflict-unresolved`.",
             "  - any other conflict, including a ledgered path whose `L[p]` differs from the composition, is FAIL\n"
             "    `landing-conflict-unresolved`. For a path with an applying category-2 resolution (R6.RECON.24), the\n"
             "    composition is the resolved composition: `M`'s bytes with every unresolved splice at its\n"
             "    `M`-translated offset and each resolution window replaced by its resolved bytes; a resolved splice is\n"
             "    not translated %s." % MARK, 'R6.TREE.12 resolved composition')
    t = once(t, "TT10, TT11, RL, RT-L, N10, N11, LC-1, LC-2, LC-3, LC-4, LC-5, LC-6, LC-7.\n",
             "TT10, TT11, RL, RT-L, N10, N11, LC-1, LC-2, LC-3, LC-4, LC-5, LC-6, LC-7, RECON-OVERLAP.\n",
             'R6.TREE.12 controls')
    t = once(t, "| `base-drift` | a side change on `M` to a ledgered or corpus path not covered by a reconciliation record "
                "that applies (sec. 23) |\n\nSources: E-1076, RV-057. Controls: TT3, TT4, TT9, R15, TT10, TT7, N10, "
                "TT11, N4, N5, N16-file.",
             "| `base-drift` | a side change on `M` to a ledgered or corpus path not covered by a reconciliation record "
             "that applies (sec. 23) |\n| `retirement-blocked` | a change on `M` that a reviewed `scientific_effect` "
             "finds to invalidate the basis of a planned edit (R6.RECON.26) %s |\n\nSources: E-1076, RV-057. "
             "Controls: TT3, TT4, TT9, R15, TT10, TT7, N10, TT11, N4, N5, N16-file, RECON-BLOCK." % MARK,
             'R6.CLASS.10')
    t = once(t, "- (g) **Use.** It is used only to reconcile `base-drift` on `M` under RC1-RC13, and the comparison of",
             "- (g) **Use.** It is used only to reconcile `base-drift` on `M` under RC1-RC14 %s, and the\n"
             "  comparison of" % MARK, 'R6.RECON.2 (g)')
    t = once(t, "R8-S6. Each condition RC1-RC13 of sec. 23 has its own control: N5 (RC1), N7 (RC2), N12 (RC3), N8\n"
                "(RC4), N13 (RC5), N14 (RC6), N9 (RC7), N15 (RC8), N6 (RC9), N16 (RC10), N17 (RC11), N18 (RC12) and N4\n"
                "(RC13).",
             "R8-S6. Each condition RC1-RC14 of sec. 23 has its own control: N5 (RC1), N7 (RC2), N12 (RC3), N8\n"
             "(RC4), N13 (RC5), N14 (RC6), N9 (RC7), N15 (RC8), N6 (RC9), N16 (RC10), N17 (RC11), N18 (RC12), N4\n"
             "(RC13) and RECON-CONFLICT (RC14). The positive fixtures of TT8 and POSTF-1 must also satisfy RC14 and the\n"
             "reconciled-state trial (R6.RECON.23); their rows are unchanged %s." % MARK, 'R6.CTRL.21')
    t = once(t, "E-1324, E-1325, E-1326, E-1327, E-1328. Controls: N1, N2, N3, N3-config-route, N4, N5, N6, N7, N8, N9, N10, "
                "N11, N12, N13, N14, N15, N16, N16-file, N17, N18, N18-record, R8-S6.",
             "E-1324, E-1325, E-1326, E-1327, E-1328. Controls: N1, N2, N3, N3-config-route, N4, N5, N6, N7, N8, N9, N10, "
             "N11, N12, N13, N14, N15, N16, N16-file, N17, N18, N18-record, R8-S6, RECON-CONFLICT.", 'R6.CTRL.21 ctl')
    # schema bump: oi-reconciliation/2 in the requirements that define and admit the record
    t = once(t, "**R6.RECON.1** A reconciliation record (schema `oi-reconciliation/1`) is reviewed and immutable, and",
             "**R6.RECON.1** A reconciliation record (schema `oi-reconciliation/2`) is reviewed and immutable, and",
             'R6.RECON.1 schema')
    t = once(t, "- (a) **Kind and binding.** Its schema is `oi-reconciliation/1`, and it names",
             "- (a) **Kind and binding.** Its schema is `oi-reconciliation/2`, and it names", 'R6.RECON.2 (a) schema')
    t = once(t, "  `oi-reconciliation/1` (the scanned set; review records",
             "  `oi-reconciliation/2` (the scanned set; review records", 'R6.RECON.2 (d) schema')
    t = once(t, "  `oi-side-change-classes/1`, `oi-reconciliation/1`, `oi-review-record/1`);",
             "  `oi-side-change-classes/1`, `oi-reconciliation/2` %s, `oi-review-record/1`);" % MARK, 'R6.CORE.5 schema')
    t = once(t, "\n***\n\n## 24. Engine, purity scope (Z9), generality",
             NEW_REQ_TEXT % {'mark': MARK, 'src': 'amendment 3 (#1169 comments 7184569981 and 7184626125)',
                             'src3': 'amendment 3 (#1169 comments 7184569981, 7184626125 and 7184808247)',
                             'src4': 'amendment 3 (#1169 comments 7184569981, 7184626125, 7184808247 and 7185092393)'}
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
            'sources': ['#1169 comment 7184569981', '#1169 comment 7184626125'] +
                       (['#1169 comment 7184808247'] if q in ('R6.RECON.22', 'R6.RECON.24', 'R6.RECON.26') else []) +
                       (['#1169 comment 7185092393'] if q == 'R6.RECON.26' else []),
            'controls': list(REQ_CONTROLS[q]),
            'verification': ['controls', 'review'] if q in ('R6.RECON.25', 'R6.RECON.26') else ['controls'], 'open': [],
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
   engine/reconcile.py). At `main` eb3a69f4 eleven of the ledger's 44 paths differ from `H` (below), so the B4
   AGENTS.md record cannot apply. Amendment 3 reads RC10 over the run's locally valid entries.
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

Drift inventory at `main` eb3a69f4 (after #1582's merge), computed against `H` 53c6601a over the 44 paths of the
retirement ledger (blob ba37c1cd): eleven paths differ, each needing a disposition under R6.RECON.22: AGENTS.md;
verification/lean/edge_rigidity_probe.py; papers/Main.md, papers/SM.md and papers/Substratum.md;
book/The-Incompleteness-of-Observation-FULL.md, book/appendix-c-objections.md, book/ch01-observation.md,
book/ch07-gravity.md, book/ch09-universality.md and book/ch18-beyond.md. Amendment 3 names none of them in a rule; its
rules apply to any path.
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
    lines += ['## 2a. Categories (#1169 comment 7184808247, item 3)', '',
              '| Category | When | Disposition | Determined by | Controls |', '|---|---|---|---|---|'] + \
        ['| %s | %s | %s | %s | %s |' % c for c in CATEGORIES] + ['',
                                                                     'Category 2 is computed from git objects and is '
                                                                     'never reconciled by translation; its resolution '
                                                                     'is explicit, reviewed, keeps the planned edit\'s '
                                                                     'new bytes, and carries a renewed scientific '
                                                                     'review. Category 3 cannot be found by the tool: '
                                                                     'it is the review\'s verdict, and the tool '
                                                                     'enforces that a recorded verdict blocks, whatever '
                                                                     'later record exists, until a revised plan changes '
                                                                     'the path\'s ledger binding.', '']
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
              '| DESIGN-r6.md | R6.RECON.22 to R6.RECON.26 (new) | mechanical verification with categories, trial '
              'verification, conflict detection (RC14 and explicit resolution), scientific verification, the '
              'category-3 blocking state |',
              '| DESIGN-r6.md | R6.TREE.12 | the resolved composition for a path with an applying category-2 '
              'resolution |',
              '| DESIGN-r6.md | R6.CLASS.10 | the class `retirement-blocked` |',
              '| DESIGN-r6.md | R6.CTRL.3, Table 17.1 | %d rows counted and added after RTL2-BIND |' % len(ROWS),
              '| EXPECTATIONS.json | rows %s (new) | each records both directions; runner null |' % ', '.join(NEW_IDS),
              '| REQUIREMENTS.json | R6.RECON.22 to R6.RECON.26 (new); %s | controls appended; '
              '`pending_owner_confirmation` added |' % ', '.join(TOUCHED), '']
    lines += ['## 4. Preserved results (stated in advance; AGENTS.md sec. A.29)', '',
              '- The meaning of RC1 to RC9, RC12 and RC13 for each path, and their controls N3 to N18, TT8 and '
              'N3-config-route, unchanged.',
              '- The composition and translation rules R6.TREE.12 and R6.TREE.13 and their controls LC-1 to LC-7, RL, '
              'RT-L, TT7 and TT8, unchanged for every path without an applying category-2 resolution.',
              '- `base-drift` for every drifted path that no applying entry covers (R6.TREE.7): no path is exempt.',
              '- Identical items on `X` with and without the records (R6.RECON.3), and the composition\'s authority '
              'over `l` (R6.RECON.19).',
              '- The post-freeze route (R6.RECON.2, POSTF-1 to POSTF-5), RT-L2\'s three values (R6.GATE.16, GATE-13 to '
              'GATE-15, GATE-19, RTL2-BIND).',
              '- No existing expectation row changes, and no requirement loses a control (checked by the generator).',
              '- Hard-to-vary check: with one drifted ledgered path and no other side change, RC10 and RC11 as amended '
              'reduce to the old RC10 and RC11. Whether the existing positive controls (TT8, POSTF-1 and the other '
              'positive reconciliation fixtures) also satisfy RC14 and the reconciled-state trial is a check for the '
              'tool revision; the independent review found no change of verdict for TT8 at 933b1efd or for the B4 '
              'AGENTS.md record (D296), and found every one of the 201 splice windows on the eleven drifted paths '
              'exactly once at #1582\'s head 7a01b4c9 at line level, so the line-level RC14 prediction comes out "no '
              'conflict". Beyond the case it was '
              'built for, the amendment predicts checkable outcomes at `main` eb3a69f4 (which carries #1582): with '
              'AGENTS.md alone reconciled, RC10 fails naming the ten other drifted ledger paths; and RC14 decides, from '
              'the bytes, whether any restored correction touches the context of a retirement splice (sentence-level '
              'windows remain to be checked when the records are drafted).', '']
    lines += ['## 4a. Owner decisions on the block and on retained sites', '',
              '- Category-3 lifecycle, decided by the owner (amaybaum, 2026-11-26T07:05:39Z, #1169 comment 7185092393, '
              'item 4; quoted in DESIGN-r6.md sec. 0.4). Encoded in R6.RECON.26: the block is scoped to the frozen '
              'plan, keyed to its ledger\'s invalidated edit-list entries; a repair on `main` never lifts it; the '
              'original finding and the recorded repair (a reconciliation record entry of the repairing change, with '
              'its own reviewed `scientific_effect`) stay on `main` as evidence; a revised plan, frozen anew, whose '
              'ledger no longer carries an invalidated entry or carries a revised one, is not blocked by the old '
              'finding, and its renewed verification and trials run normally, the retirement becoming eligible for '
              'approval again when they pass. RECON-BLOCK covers both directions: the repair and a new freeze with the '
              'entry unchanged stay blocked; a revised plan that changes or removes the entry is not blocked.', '',
              '- Changed-span resolution windows (R6.RECON.24): option (b) is chosen, the writer choosing the window '
              'and the review confirming it. It adds no rule to the tool beyond a review item; option (a), windows '
              'bounded by the nearest unique unchanged lines, would add an anchor search whose result can still cut '
              'through a change, so the review would have to check it anyway.', '',
              '- Retained-site conflicts (R6.RECON.24): the minimal option is chosen. A retained site is a plan decision '
              'with no new bytes to keep, so no objective resolution check exists; a conflict on its line stays '
              '`base-drift` until a revised plan. Defining a resolution for it would add a rule the tool cannot check.',
              '']
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
              'lines and, for corpus paths, splitter-v2 sentences; retained sites through the site map); RC14 in '
              '`condition_order`.',
              '- The result and its JSON Schema: one disposition per drifted ledgered or corpus path (R6.RECON.22).',
              '- The reconciled-state trial: op D and op C\'s postconditions at the landing or in-memory landing, '
              'compared with the candidate by fingerprint (R6.RECON.23); RT-L2\'s runner includes it.',
              '- Record lint of `scientific_effect` with its verdict (R6.RECON.25), and of `resolutions` with the '
              'resolved composition (R6.RECON.24, R6.TREE.12).',
              '- Categories in each disposition (R6.RECON.22); the blocking state and the class `retirement-blocked` '
              '(R6.RECON.26, R6.CLASS.10), found over every reviewed entry regardless of supersession; the class added '
              'to the result schema and the engine enumerations.',
              '- The purity lint allowlist (R6.CORE.5) and schema list: the schema id `oi-reconciliation/2`; the '
              'enumerations `RC14`, `reconciled-state`, `reconciled`, `reconciled-resolved`, `retirement-blocked`, '
              '`no-effect` and `invalidates` where the engine holds them as literals; the field names '
              '`scientific_effect`, `conclusions`, `assessment`, `invalidated`, `resolutions`, `ledger_binding` and '
              '`ledger_base` (already-listed names such as `method`, `verdict`, `start_M` need no addition only where '
              'present).',
              '- Fingerprint matching at the landing that counts multiplicities and excludes the tree field; run-level '
              '`reconciled-state` items (R6.RECON.23).',
              '- Runners for %s.' % ', '.join(NEW_IDS),
              '- The B4 records rebuilt in schema `oi-reconciliation/2` (per-path binding, `scientific_effect` with '
              'its verdict), with an entry for each drifted path.', '']
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
    para = ('\nAmendment 3 (owner decisions of 2026-11-26T06:34:32Z, 2026-11-26T06:37:58Z and 2026-11-26T06:48:37Z, '
            'amaybaum, #1169 comments 7184569981, 7184626125 and 7184808247, and 2026-11-26T07:05:39Z, #1169 comment '
            '7185092393, item 4, quoted in DESIGN-r6.md sec. 0.4): DESIGN-r6.md, EXPECTATIONS.json and '
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
