"""Generator of amendment 4 to design r6: category-3 keying and the predicted-M record base (owner decision of
2026-11-26T07:31:59Z, #1169 comment 7185562871, items 2, 3 and 7).

Usage: python3 -I -B amend4.py BASE OUT

BASE holds DESIGN-r6.md, EXPECTATIONS.json, REQUIREMENTS.json and LANDING-MANIFEST.md as amendment 3 leaves them
(each checked against its sha256 below). The script reads owner-decisions-amendment4.json beside itself and writes
into OUT the amended DESIGN-r6.md, EXPECTATIONS.json and REQUIREMENTS.json, the change record AMENDMENT-4.md and the
updated LANDING-MANIFEST.md. Every text edit is anchored on an exact string that must occur the stated number of times.
Self-checks: correspondence for every touched row and requirement, a second direction on every new row, the closed
invariant vocabulary, new ids unused in the base files, no existing expectation row changed, no requirement losing a
control, and the amendment-4 mark on every touched requirement. Standard library only; deterministic.
"""
import copy
import hashlib
import json
import os
import re
import sys

BASE_SHA256 = {
    'DESIGN-r6.md': '4e7be527592948fe5360e97713f0484f5f0463ba1d42411036791e50d2f66fe4',
    'EXPECTATIONS.json': '35c8d35f8156c34e812da67c1bda5de658bda34a51beb8461ddc6a9955ff545a',
    'REQUIREMENTS.json': '21c4cfc14c0e56c564ca87aa42c5bef7c134943224ce84f4bd7f2ff5c923ba36',
    'LANDING-MANIFEST.md': 'ecde12a0a84ff9759b1890c4dda795f387ad4fd2f6c6c3b25e9e5ff80cb4aa95',
}
HERE = os.path.dirname(os.path.abspath(__file__))
SRC = 'r6 amendment 4 (owner decision of 2026-11-26T07:31:59Z, #1169 comment 7185562871, items 2 and 3)'
FLAG = 'added by amendment 4; no runner records it before the tool revision implements it'
PENDING = ('amendment 4 (category-3 keying and the predicted-M record base): drafted under the owner\'s direction of '
           '2026-11-26T07:31:59Z (#1169 comment 7185562871); needs independent review and the owner\'s acceptance '
           'before any tool revision implements it')
MARK = '(amendment 4, sec. 0.5: pending independent review and the owner\'s acceptance)'
BLOCKED = {'outcome': 'FAIL', 'classes_include': ['retirement-blocked']}
NOT_BLOCKED = {'outcome': 'ANY', 'invariants': [{'not_class': ['retirement-blocked']}]}
TARGET = 'and its target (the path, `start_H` and `old_sha256` of the edit at `H`)'


def sha(b):
    return hashlib.sha256(b).hexdigest()


def once(text, old, new, what, n=1):
    c = text.count(old)
    if c != n:
        raise SystemExit('anchor for %s occurs %d times' % (what, c))
    return text.replace(old, new)


def dumpj(doc):
    return (json.dumps(doc, indent=1, ensure_ascii=False) + '\n').encode('utf-8')


def row(rid, req, direction, expect, restored, case):
    r = {'id': rid, 'requirements': req, 'runner': None, 'operations': ['execution']}
    if direction != 'adversarial':
        r['direction'] = direction
    r['expect'] = expect
    if restored is not None:
        r['restored'] = restored
    r['source'] = SRC
    r['flags'] = [FLAG]
    return r, case


def c(case, base):
    return dict(case=case, **base)


def rinv(case, extra=()):
    return {'case': case, 'outcome': 'FAIL', 'classes_include': ['record-invalid'] + list(extra)}


ROWS = [
    row('BLOCK-KEY', ['R6.RECON.26', 'R6.RECON.27', 'R6.CFG.4'], 'both', {'cases': [
        c('the edit\'s wording changed in a revised configuration (new bytes or reason; the same id and target), '
          'no reassessment cited', BLOCKED),
        c('the edit id renamed in a revised configuration, the rename recorded under AGENTS.md sec. A.48 item 3',
          BLOCKED),
        c('the edit id renamed with no recorded migration (the target unchanged)', BLOCKED),
        c('a scientific repair landed on M, the original frozen configuration unchanged', BLOCKED),
        c('an applying reassessment exists on M, the original frozen configuration (which does not cite it) unchanged',
          BLOCKED),
        c('a revised configuration citing a reassessment whose edit_sha256 differs from the edit as now worded',
          BLOCKED),
        c('a configuration of the same retirement in a new config_id lineage, carrying the edit, citing no '
          'reassessment', BLOCKED),
        c('countercase: a revised configuration, frozen anew, citing an applying reassessment of the edit as now '
          'worded (positive)', NOT_BLOCKED),
        c('countercase: a revised configuration that removes the edit (neither its id, a migrated id nor its target '
          'remains), citing no reassessment (positive)', NOT_BLOCKED)]},
        None,
        'the block is keyed by the edit\'s stable id within the retirement\'s plan lineage, followed through recorded '
        'migrations and by its target; wording changes and repairs do not lift it; a revised plan proceeds only by '
        'removing the edit or by citing an applying reassessment'),
    row('REASSESS-FORM', ['R6.RECON.27'], 'adversarial', {'cases': [
        rinv('a reassessment with no non-author review, or whose reviewer equals its author', ['retirement-blocked']),
        rinv('a reassessment naming no finding, or a path that holds no finding at M', ['retirement-blocked']),
        rinv('a reassessment whose repair names no commit on M\'s first-parent chain', ['retirement-blocked']),
        rinv('a reassessment with an empty re-derivation of the edit\'s justification', ['retirement-blocked']),
        rinv('a reassessment whose verdict is not no-effect', ['retirement-blocked']),
        rinv('a reassessment cited under kind reassessment but failing record lint (a schema error)',
             ['retirement-blocked'])]},
        {'outcome': 'ANY', 'invariants': [{'not_class': ['retirement-blocked', 'record-invalid']},
                                          {'baseline': 'the same revised configuration citing a valid reassessment'}]},
        'the reassessment\'s form, review and citation are checked; a failure keeps the block'),
    row('RECORD-BASE', ['R6.RECON.2', 'R6.RECON.21', 'R6.GATE.16'], 'both', {'cases': [
        {'case': 'a run on a predicted M built from M0 by in-memory commits adding tool-landing paths whose blobs equal '
                 'their pins, named with --record-base M0; REV\'s single parent is M0 (positive)',
         'outcome': 'ANY', 'invariants': [{'record_admitted': '$record'}, {'not_class': ['record-invalid']},
                                          {'equals': 'inputs.record_base is M0'}]},
        rinv('countercase: REV\'s parent is the predicted M'),
        rinv('countercase: REV\'s parent is an intermediate in-memory commit (RT-O9 shape)'),
        rinv('countercase: REV\'s parent is an ancestor of M0'),
        rinv('countercase: a ledgered, corpus, unclassified or reconciliation-directory change lies between M0 and M'),
        rinv('countercase: a merge lies between M0 and M'),
        rinv('countercase: a change between M0 and M that a later step reverts (the aggregate diff is empty for it)'),
        rinv('countercase: a pin path of the tool-landing class with a different blob, or deleted'),
        rinv('countercase: --record-base names an in-memory commit'),
        rinv('countercase: the configuration lies in a directory that is not an authorized record directory'),
        rinv('countercase: a reviewed class record named by --classify whose prefixes cover the offending change'),
        {'case': 'countercase: --record-base given in a chain-admitted run', 'outcome': 'USAGE', 'exit': 64},
        {'case': 'countercase: the result\'s inputs.record_base differs from the runner\'s pinned main commit',
         'outcome': 'FAIL', 'invariants': [{'rt_l2_status': 'FAIL'}]}]},
        None,
        'the predicted-M record base is named explicitly and admitted only after the tool establishes it from git '
        'objects; naming it establishes nothing'),
]
NEW_IDS = [r['id'] for r, _ in ROWS]
REQ_CONTROLS = {}
for _r, _ in ROWS:
    for _q in _r['requirements']:
        REQ_CONTROLS.setdefault(_q, []).append(_r['id'])
NEW_REQS = ['R6.RECON.27']
TOUCHED = ['R6.RECON.2', 'R6.RECON.21', 'R6.RECON.25', 'R6.RECON.26', 'R6.GATE.16', 'R6.CFG.4']

LIFECYCLE = [
    ('Edit wording changes', 'Block persists.', 'the block is keyed by the edit id (and target), not by its bytes',
     'BLOCK-KEY'),
    ('Edit identifier is renamed', 'Block follows the recorded migration.', 'the renamed edit is found by the recorded '
     'migration and, mechanically, by its unchanged target', 'BLOCK-KEY'),
    ('Scientific repair lands', 'Block persists for the original frozen plan.', 'a frozen configuration cannot cite a '
     'later reassessment', 'BLOCK-KEY'),
    ('Independent reassessment accepts the repair', 'Revised plan becomes eligible for review and freezing.',
     'R6.RECON.27: a reviewed reassessment of the edit as now worded', 'BLOCK-KEY, REASSESS-FORM'),
    ('Revised plan is frozen', 'New verification and trials may proceed.', 'a configuration whose freeze cites the '
     'applying reassessment, or that removes the edit, is not blocked', 'BLOCK-KEY'),
]

NEW_REQ = '''
**R6.RECON.27** **Reassessment of an invalidated edit** %(mark)s. A reassessment record (schema
`oi-reassessment/1`) is reviewed and immutable, under the ownership chain of sec. 11, and names: `finding`, the
`{path, blob_sha256}` of the record or review record carrying the category-3 finding (R6.RECON.26); `repair`, the
commits of the repairing change on `main` and the `{path, blob_sha256}` of the reconciliation record entry that records
it; `edit`, the edit id and the canonical sha256 of its edit-list entry as worded in the configuration that cites the
reassessment; `rederivation`, the edit's justification re-derived at the repaired state, with what was re-run; and
`verdict`, which must be `no-effect` for the edit as now worded. A configuration's freeze cites it by listing it in
`records` with kind `reassessment` (R6.CFG.4). It applies only if: a non-author review record names its blob and accepts
every item, and record lint holds (R6.REC.6, R6.REC.7); the named finding is a finding the scan of R6.RECON.26 finds at
the run's `M`; the repair's commits lie on `M`'s first-parent chain; `rederivation` is non-empty; the verdict is
`no-effect`; and `edit` names an edit of the citing configuration's ledger whose canonical sha256 equals the recorded
one. The tool checks this form, the review and the citation; it cannot check that the re-derivation is sound, which
rests on the review. A cited reassessment that does not apply is FAIL `record-invalid`, and the block stands.
Sources: %(src)s. Controls: BLOCK-KEY, REASSESS-FORM.
'''


def note(owner):
    out = ['', '### 0.5 Amendment 4 of 2026-11-26', '']
    for d in owner['decisions']:
        out += ['The owner decided at %s (%s, %s, relayed by the %s). Excerpt of items 2, 3 and 7, in the order of the '
                'source (table cells joined by " | ", table padding removed; headings left out; each line prefixed by '
                '"> "; "[...]" marks text left out):' % (d['record'], d['author'], d['time'], d['relayed_by']), '']
        out.append('\n>\n'.join('> ' + (x if x is not None else '[...]') for x in d['quotes']))
        out.append('')
    out += [
        'Amendment 4 is limited to these two questions; it is pending independent review and the owner\'s acceptance, '
        'and it reopens nothing else of amendment 3.',
        '',
        '- Category-3 keying (R6.RECON.26, new R6.RECON.27, R6.RECON.25, R6.CFG.4; controls BLOCK-KEY, REASSESS-FORM). '
        'The block is keyed by the edit\'s stable id within the plan lineage of the retirement (the configurations '
        'naming the same `retirement`), not by its bytes. A finding records each invalidated edit\'s id, the sha256 of '
        'its edit-list entry (evidence) and its target at `H`. A configuration carries the blocked edit when its ledger '
        'holds that id, an id the edit was renamed to under a migration recorded under AGENTS.md sec. A.48 item 3, or '
        'an edit with the same target. The lifecycle:',
        '',
        '| Event | Outcome | How | Controls |',
        '|---|---|---|---|',
    ] + ['| %s | %s | %s | %s |' % r for r in LIFECYCLE] + [
        '',
        '  A plan that removes the edit needs no reassessment. The tool checks the reassessment\'s form, its review and '
        'its citation by the new freeze; it cannot check the soundness of the re-derivation.',
        '- The predicted-M record base (R6.RECON.2 (c), R6.RECON.21, R6.GATE.16; control RECORD-BASE). A run on a '
        'predicted `M` names its record base with `--record-base M0`; the tool establishes `M0`\'s admissibility from '
        'git objects (that `M0` is a real commit, that `M` descends from it by single-parent in-memory commits whose '
        'changes are tool-landing or authorized plan-directory paths, and that no ledgered, corpus or scanned-set path '
        'changes), so naming it establishes nothing. The gate compares the recorded `M0` with the runner\'s pinned '
        '`main`.',
        '',
    ]
    return '\n'.join(out)


def amend_design(t, owner):
    # Question 1
    t = once(t, "the latter with `invalidated`, each an edit id with the\ncanonical sha256 of its edit-list entry.",
             "the latter with `invalidated`, each an edit id with the\ncanonical sha256 of its edit-list entry %s %s."
             % (TARGET, MARK), 'R6.RECON.25 invalidated')
    t = once(t, "`invalidated`, each an edit id with the canonical sha256 of its edit-list entry. A record or review record "
                "carrying a",
             "`invalidated`, each an edit id with the canonical sha256 of its edit-list entry %s. A record or review "
             "record carrying a" % TARGET, 'R6.RECON.26 invalidated')
    t = once(t, "The block holds for as long as the configuration's ledger holds, for each\n"
                "invalidated edit id, an edit-list entry with the same canonical sha256.",
             "The block holds for every configuration that carries an invalidated edit %s: one whose `retirement` names\n"
             "the same retirement as the configuration the finding was made under (its plan lineage), and whose ledger\n"
             "holds the edit's id, an id the edit was renamed to under a migration recorded under AGENTS.md sec. A.48\n"
             "item 3, or an edit with the same target. The sha256 recorded with each invalidated edit is evidence, not\n"
             "the edit's identity: a change of the edit's wording does not lift the block." % MARK,
             'R6.RECON.26 keying')
    t = once(t, "The block is scoped to the frozen plan: it binds every\n"
                "configuration whose ledger carries an invalidated edit-list entry unchanged, and nothing else.",
             "The block is scoped to the plan lineage: it binds every\n"
             "configuration that carries an invalidated edit, unless that configuration's freeze cites an applying\n"
             "reassessment of the edit (R6.RECON.27), and nothing else.", 'R6.RECON.26 scope')
    t = once(t, "new freeze (R6.CFG.3; AGENTS.md sec. A.50 item 5) whose ledger no longer carries an invalidated entry or "
                "carries a\nrevised one, is not blocked by the old finding;",
             "new freeze (R6.CFG.3; AGENTS.md sec. A.50 item 5) that no longer carries the invalidated edit, or whose freeze\n"
             "cites an applying reassessment of the edit as now worded (R6.RECON.27), is not blocked by the old finding; a "
             "plan\nthat removes the edit needs no reassessment;", 'R6.RECON.26 revised plan')
    t = once(t, "Sources: amendment 3 (#1169 comments 7184569981, 7184626125, 7184808247 and 7185092393). Controls: RECON-BLOCK.",
             "Sources: amendment 3 (#1169 comments 7184569981, 7184626125, 7184808247 and 7185092393); amendment 4 "
             "(#1169 comment 7185562871). Controls: RECON-BLOCK, BLOCK-KEY.", 'R6.RECON.26 controls')
    t = once(t, "  design does not define, such as `oi-owner-authorization/1`, is ERROR `CONFIG_INVALID`;",
             "  design does not define, such as `oi-owner-authorization/1`, is ERROR `CONFIG_INVALID`; a reassessment\n"
             "  record that the freeze cites (R6.RECON.27) is listed with kind `reassessment` %s;" % MARK, 'R6.CFG.4')
    # Question 2
    t = once(t, "  The record base is the run's `M`, or, for a run on a predicted `M` (R6.RECON.21), the pinned `main`\n"
                "  commit `M0` it is built from.",
             "  The record base is the run's `M`. A run on a predicted `M` (R6.RECON.21) names its record base with\n"
             "  `--record-base M0`, `M0` being the pinned `main` commit from which the runner built the predicted `M`\n"
             "  (in RT-L2 and RT-O9-L2, the runner's `--main`); the tool admits `REV` only if its single parent is\n"
             "  exactly `M0`, and only if it verifies from git objects that: (1) `M0` is a full commit id read by the\n"
             "  verified reader from the repository object store, not an in-memory commit; (2) `M` descends from `M0`\n"
             "  by a chain of single-parent in-memory commits (R6.TREE.15); (3) for each step of that chain and for the\n"
             "  aggregate diff `M0..M`, every path whose mode or object id differs, deletions included, either lies\n"
             "  under a prefix of the class `tool-landing` in the side-change class record the configuration pins\n"
             "  (`roles.side_change_classes`) or is a pin of that class whose blob at `M` equals the pinned blob, or\n"
             "  lies inside the plan's record directory, which must be the directory of the configuration path and an\n"
             "  authorized record directory; and every path a step changes also differs in the aggregate diff; (4) no\n"
             "  changed path is a ledgered or corpus path, or a path of the scanned set of (d) at `M0` or at `M`. Class\n"
             "  records named by `--classify` never contribute to that domain, to placement (f) or to the scanned set\n"
             "  (d). Naming `M0` establishes nothing: any failed check is FAIL `record-invalid`. Without `--record-base`\n"
             "  the record base is `M`; in a chain-admitted run the option is a usage error (USAGE, exit 64). The result\n"
             "  records `M0` in `inputs.record_base` %s." % MARK, 'R6.RECON.2 (c)')
    t = once(t, "(a) and (c) to (g) of R6.RECON.2, with `M0` as the record base on a predicted `M` and the run's `M` on\n"
                "a re-run on `main` (R6.EVID.8);",
             "(a) and (c) to (g) of R6.RECON.2, with `M0`, named by `--record-base` and admitted under R6.RECON.2 (c), as\n"
             "the record base on a predicted `M` %s, and the run's `M` on a re-run on `main` (R6.EVID.8);" % MARK,
             'R6.RECON.21')
    t = once(t, "Sources: E-1355, OC-3. Controls: RT-L2, RT-O9-L2, GATE-13, GATE-14, GATE-15, GATE-19, RTL2-BIND, RECON-TRIAL.",
             "Sources: E-1355, OC-3. Controls: RT-L2, RT-O9-L2, GATE-13, GATE-14, GATE-15, GATE-19, RTL2-BIND, RECON-TRIAL, "
             "RECORD-BASE.", 'R6.RECON.21 controls')
    t = once(t, "The gate's `rtl2` predicate compares the `H`, `M` and `C` each record names with the run's roles; in\n",
             "The gate's `rtl2` predicate compares the `H`, `M` and `C` each record names with the run's roles, and, for a\n"
             "run on a predicted `M`, the result's `inputs.record_base` with the runner's pinned `main` commit %s; in\n"
             % MARK, 'R6.GATE.16')
    t = once(t, "Sources: E-1341, RV-027. Controls: O8, N2, POSTF-1, POSTF-2, POSTF-3, POSTF-4, POSTF-5.",
             "Sources: E-1341, RV-027. Controls: O8, N2, POSTF-1, POSTF-2, POSTF-3, POSTF-4, POSTF-5, RECORD-BASE.",
             'R6.RECON.2 controls')
    t = once(t, "A-115, A-116, A-117, A-024, A-129, OD-1, OD-2, OD-7, OD-23, RD-32. Controls: Z1, Z2, Z3, Z6, Z6b,\n"
                "CONFIG-LINT, Z8.",
             "A-115, A-116, A-117, A-024, A-129, OD-1, OD-2, OD-7, OD-23, RD-32. Controls: Z1, Z2, Z3, Z6, Z6b,\n"
             "CONFIG-LINT, Z8, BLOCK-KEY.", 'R6.CFG.4 controls')
    t = once(t, "Sources: OD-18, Q2. Controls: RT-L2, GATE-13, GATE-14, GATE-15, GATE-19, RTL2-BIND.",
             "Sources: OD-18, Q2. Controls: RT-L2, GATE-13, GATE-14, GATE-15, GATE-19, RTL2-BIND, RECORD-BASE.",
             'R6.GATE.16 controls')
    t = once(t, "Sources: amendment 3 (#1169 comments 7184569981 and 7184626125). Controls: RECON-SCI, RECON-BLOCK.",
             "Sources: amendment 3 (#1169 comments 7184569981 and 7184626125). Controls: RECON-SCI, RECON-BLOCK, "
             "BLOCK-KEY.", 'R6.RECON.25 controls')
    t = once(t, "\n***\n\n## 24. Engine, purity scope (Z9), generality",
             NEW_REQ % {'mark': MARK, 'src': 'amendment 4 (#1169 comment 7185562871)'}
             + "\n***\n\n## 24. Engine, purity scope (Z9), generality", 'R6.RECON.27')
    # R6.CTRL.3 rows and recount
    t = once(t, "direction on each of those 42 rows and adds 14 rows (B1) and 6 rows (B4), each with one, and amendment 3\n"
                "adds 9 rows (sec. 0.4), each with one. Counted",
             "direction on each of those 42 rows and adds 14 rows (B1) and 6 rows (B4), each with one, amendment 3\n"
             "adds 9 rows (sec. 0.4), and amendment 4 adds %d rows (sec. 0.5), each with one. Counted" % len(ROWS),
             'R6.CTRL.3 rows')
    m = re.search(r"\(\d+ rows, \d+ of them recording `scope: \"outside\"`; \d+ carry a `restored` expectation, \d+ "
                  r"declare direction `both`, \d+ name `paired_with`, \d+ are exempt as observations\)", t)
    if not m or t.count(m.group(0)) != 1:
        raise SystemExit('R6.CTRL.3 counts')
    t = t.replace(m.group(0), '(%s)' % COUNTS)
    anchor = [x for x in re.finditer(r'^\| RECON-BLOCK \| [^\n]*$', t, re.M)]
    if len(anchor) != 1:
        raise SystemExit('RECON-BLOCK table row')
    t = t[:anchor[0].end()] + '\n' + '\n'.join(table_row(r, cs) for r, cs in ROWS) + t[anchor[0].end():]
    a = t.index('### 0.4 Amendment 3 of 2026-11-26')
    b = t.index('\n***\n\n## 1. Notation and symbols', a)
    t = t[:b] + '\n' + note(owner) + t[b:]
    return t


def table_row(r, case):
    d = r.get('direction', 'adversarial')
    dirs = {'adversarial': 'adv', 'positive': 'pos', 'both': 'both'}[d]
    return '| %s | %s | to be implemented (tool revision) | decl | %s | %s (amendment 4) |' % (
        r['id'], ', '.join(r['requirements']), dirs, case)


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
    for rid, ctl in sorted(REQ_CONTROLS.items()):
        if rid in NEW_REQS:
            continue
        q = by[rid]
        if q['kind'] != 'testable' or set(ctl) & set(q['controls']):
            raise SystemExit('%s: controls' % rid)
        q['controls'] = q['controls'] + ctl
    for rid in TOUCHED:
        by[rid]['pending_owner_confirmation'] = by[rid]['pending_owner_confirmation'] + [PENDING]
    i = [k for k, q in enumerate(R) if q['id'] == 'R6.RECON.26'][0]
    new = [{'id': 'R6.RECON.27', 'section': 'RECON', 'section_number': 23, 'kind': 'testable',
            'sources': ['#1169 comment 7185562871'], 'controls': list(REQ_CONTROLS['R6.RECON.27']),
            'verification': ['controls', 'review'], 'open': [], 'pending_owner_confirmation': [PENDING],
            'owner_decision': []}]
    return R[:i + 1] + new + R[i + 1:]


def vocabulary(t):
    a = t.index('### 16.10 Annex: invariant vocabulary')
    b = t.index('***', a)
    return set(re.findall(r'`([A-Za-z_0-9]+)`', t[t.index('\n\n', t.index('A key outside it', a)):b]))


def self_checks(E0, E, R0, R, t, base_texts):
    problems = []
    rows = {r['id']: r for r in E['rows']}
    reqs = {q['id']: q for q in R}
    for rid in NEW_IDS + NEW_REQS + ['oi-reassessment/1', '--record-base', 'record_base']:
        for name, b in base_texts.items():
            if re.search(r'(?<![A-Za-z0-9.-])%s(?![A-Za-z0-9-])' % re.escape(rid), b):
                problems.append('%s already occurs in base %s' % (rid, name))
    for r, _ in ROWS:
        for q in r['requirements']:
            if r['id'] not in reqs[q]['controls']:
                problems.append('%s lists %s, which does not name it' % (r['id'], q))
        if r.get('direction', 'adversarial') != 'both' and r.get('restored') is None:
            problems.append('%s: no second direction' % r['id'])
    for q in list(REQ_CONTROLS):
        for cc in reqs[q]['controls']:
            if cc not in rows or q not in rows[cc]['requirements']:
                problems.append('%s names %s, which does not list it' % (q, cc))
        start = t.index('**%s**' % q)
        nxt = re.compile(r'\n(?:\*\*R6\.|\*\*\*|#)').search(t, start + 1)
        block = t[start:nxt.start()]
        cl = block.split('Controls:')[-1]
        for cc in REQ_CONTROLS[q]:
            if not re.search(r'(?<![A-Za-z0-9-])%s(?![A-Za-z0-9-])' % re.escape(cc), cl):
                problems.append('%s: DESIGN Controls line does not name %s' % (q, cc))
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
        for cs in e.get('cases', []):
            walk(rid, cs)
    for r, _ in ROWS:
        walk(r['id'], r['expect'])
        walk(r['id'], r.get('restored'))
    r0 = {r['id']: r for r in E0['rows']}
    for rid, r in r0.items():
        if rows.get(rid) != r:
            problems.append('existing row %s changed' % rid)
    if {k: v for k, v in E0.items() if k != 'rows'} != {k: v for k, v in E.items() if k != 'rows'}:
        problems.append('EXPECTATIONS.json top-level fields changed')
    for rid, q in {q['id']: q for q in R0}.items():
        q1 = reqs[rid]
        if q1['controls'][:len(q['controls'])] != q['controls']:
            problems.append('requirement %s lost or reordered a control' % rid)
        for f in q:
            if f not in ('controls', 'pending_owner_confirmation') and q[f] != q1[f]:
                problems.append('requirement %s field %s changed' % (rid, f))
    for rid in TOUCHED + NEW_REQS:
        start = t.index('**%s**' % rid)
        nxt = re.compile(r'\n(?:\*\*R6\.|\*\*\*|#)').search(t, start + 1)
        if MARK not in t[start:nxt.start()]:
            problems.append('%s does not carry the amendment-4 mark' % rid)
    return problems


def change_record(owner, outs, gen_sha, owner_sha):
    d = owner['decisions'][0]
    lines = ['# r6 amendment 4: change record', '',
             'Owner decision: %s, %s (%s), items 2, 3 and 7, quoted as an excerpt in DESIGN-r6.md sec. 0.5. Generated by '
             'generator-amendment4/amend4.py (sha256 %s) from the amendment-3 outputs and '
             'generator-amendment4/owner-decisions-amendment4.json (sha256 %s). Amendment 4 is a draft limited to the two '
             'questions of that decision; it needs independent review and the owner\'s acceptance, reopens nothing else '
             'of amendment 3, and authorizes no merge, dispatch, freeze or trial.'
             % (d['author'], d['time'], d['record'], gen_sha, owner_sha), '',
             '## 1. Question 1: category-3 keying', '',
             'Source of the recommendation: the delta-2 review of amendment 3 (PR #1586, comment 7185180822), finding 3: '
             'keying the block by the sha256 of the edit-list entry over-blocks an unchanged edit after a verified repair, '
             'and is lifted by a nominal rewording (each edit-list entry carries a free-text `reason`). Amendment 4 keys '
             'the block by the edit\'s stable id within the retirement\'s plan lineage, follows a recorded migration and, '
             'mechanically, the edit\'s target at `H`, keeps the sha256 as evidence, and lets a revised plan proceed only '
             'by removing the edit or by citing an applying reassessment (new R6.RECON.27).', '',
             '| Event | Outcome | How | Controls |', '|---|---|---|---|'] + \
        ['| %s | %s | %s | %s |' % r for r in LIFECYCLE] + ['',
             'Changed: R6.RECON.25 and R6.RECON.26 (each invalidated edit records its target; keying; scope; revised '
             'plan), new R6.RECON.27 (reassessment record), R6.CFG.4 (record kind `reassessment`). Controls: BLOCK-KEY '
             '(both directions, one case or more per row of the owner\'s table), REASSESS-FORM.', '',
             '## 2. Question 2: the predicted-M record base', '',
             'Source: the independent review on PR #1577 (#1577, the comment of 2026-11-26T07:12:10Z), proposed text '
             '(c′), adopted with the explicit input the owner chose. The review found that the tool admits a set of '
             'bases wider than the design\'s single `M0`, which can narrow the scanned set (R6.RECON.2 (d), (e)). '
             'Amendment 4 states (c′) in R6.RECON.2 (c), and adds one clause the review\'s countercase "a change that a '
             'later step reverts" needs: every path a step changes also differs in the aggregate diff.', '',
             'Changed: R6.RECON.2 (c), R6.RECON.21 (RT-L2\'s route names `--record-base`), R6.GATE.16 (the gate\'s `rtl2` '
             'predicate compares the recorded `M0` with the runner\'s pinned `main`). Control: RECORD-BASE (the '
             'review\'s restored case and countercases, the chain-mode usage error, the gate comparison).', '',
             '## 3. What the tool can and cannot check', '',
             '- Can: whether a configuration carries a blocked edit (by id, recorded migration or target); a '
             'reassessment\'s form, review, finding, repair commits, verdict and its citation by the configuration; the '
             'admissibility of `M0` and of every step between `M0` and `M`; the gate\'s comparison of `M0`.',
             '- Cannot: whether a reassessment\'s re-derivation is sound; whether a recorded migration maps the edit '
             'correctly beyond its target; both rest on review. A rename that also moves the edit\'s target and records '
             'no migration escapes the mechanical match; the review of the new freeze must catch it.', '',
             '## 4. Preserved', '',
             '- Every rule of amendments 1 to 3 other than the sentences named above; every existing control row and '
             'expectation, none of which changes; no requirement loses a control (checked by the generator).',
             '- The category-3 lifecycle of the owner\'s decision of 2026-11-26T07:05:39Z: the original frozen plan stays '
             'blocked after a repair; a revised plan proceeds; the finding and the repair stay on `main`.', '',
             '## 5. Tool changes implied (not made here)', '',
             '- R6.RECON.26: match blocked edits by id within the plan lineage, by recorded migration and by target; read '
             'reassessments cited with kind `reassessment`; record lint for `oi-reassessment/1`.',
             '- R6.RECON.2 (c): the `--record-base` option and checks (1) to (4); a single admitted base; usage error in '
             'chain mode; `inputs.record_base` in the result schema.',
             '- The gate\'s `rtl2` predicate: compare `inputs.record_base` with the runner\'s pinned `main`.',
             '- Allowlist and schema list: `oi-reassessment/1`, `reassessment`, `record_base` and the reassessment\'s '
             'field names where the engine holds them as literals.',
             '- Runners for %s.' % ', '.join(NEW_IDS), '',
             '## 6. Outputs', '', '| File | sha256 |', '|---|---|']
    for n in ('DESIGN-r6.md', 'EXPECTATIONS.json', 'REQUIREMENTS.json'):
        lines.append('| %s | %s |' % (n, sha(outs[n])))
    lines += ['', 'Self-checks: correspondence for every touched row and requirement, second directions, the '
              'invariant vocabulary, new ids unused, no existing row changed, no requirement losing a control, the '
              'amendment-4 mark on every touched requirement.', '']
    return '\n'.join(lines)


def manifest(m, outs, gen_sha, owner_sha):
    for n, label in (('DESIGN-r6.md', 'final r6 document (the design)'),
                     ('EXPECTATIONS.json', 'final r6 document (expectation file)'),
                     ('REQUIREMENTS.json', 'final r6 document (requirement index)')):
        mm = [x for x in re.finditer(r'^\| %s \| [^\n]*$' % re.escape(n), m, re.M)]
        if len(mm) != 1:
            raise SystemExit('manifest row %s' % n)
        m = m[:mm[0].start()] + '| %s | %s | amendment-4 output | %s |' % (n, label, sha(outs[n])) + m[mm[0].end():]
    rows = ('| AMENDMENT-4.md | change record of amendment 4 | amendment-4 output | %s |\n'
            '| generator-amendment4/amend4.py | amendment-4 generator | amendment-4 generator | %s |\n'
            '| generator-amendment4/owner-decisions-amendment4.json | amendment-4 generator input (the owner decision '
            'quoted) | amendment-4 generator | %s |\n' % (sha(outs['AMENDMENT-4.md']), gen_sha, owner_sha))
    m = once(m, '| LANDING-MANIFEST.md | this manifest (A5) | amendment-3 output | (this file) |',
             rows + '| LANDING-MANIFEST.md | this manifest (A5) | amendment-4 output | (this file) |', 'manifest self')
    para = ('\nAmendment 4 (owner decision of 2026-11-26T07:31:59Z, amaybaum, #1169 comment 7185562871, items 2, 3 and 7, '
            'quoted in DESIGN-r6.md sec. 0.5): DESIGN-r6.md, EXPECTATIONS.json and REQUIREMENTS.json are amended, and '
            'AMENDMENT-4.md records the changes. Recipe: run the amendment-3 recipe into `out3/` and run `python3 -I -B '
            'generator-amendment4/amend4.py out3 out4`. It checks the four files against their sha256, exits 0 and '
            'writes into `out4/` the files of sec. 1 marked "amendment-4 output" with the sha256 stated and this '
            'manifest.\n')
    m = once(m, '\n## 2. Files left to Git history', para + '\n## 2. Files left to Git history', 'manifest recipe')
    return m


def main():
    global COUNTS
    if len(sys.argv) != 3:
        sys.stderr.write('usage: amend4.py BASE OUT\n')
        return 64
    base, out = sys.argv[1], sys.argv[2]
    data = {}
    for n, h in BASE_SHA256.items():
        with open(os.path.join(base, n), 'rb') as f:
            data[n] = f.read()
        if sha(data[n]) != h:
            sys.stderr.write('%s: sha256 %s, expected %s\n' % (n, sha(data[n]), h))
            return 65
    with open(os.path.join(HERE, 'owner-decisions-amendment4.json'), 'rb') as f:
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
    with open(os.path.join(HERE, 'amend4.py'), 'rb') as f:
        gen_sha = sha(f.read())
    outs['AMENDMENT-4.md'] = change_record(owner, outs, gen_sha, sha(owner_b)).encode('utf-8')
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
